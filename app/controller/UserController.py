from app.model.user import User
from app import response, app, db
from flask_jwt_extended import *
from flask import request
from datetime import datetime, timedelta

app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

def singleObject(data):
    return {
        "id": data.id,
        "name": data.name,
        "email": data.email,
        "level": data.level
    }

def createAdmin():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        level = 1

        user = User(name=name, email=email, level=level)
        user.setPassword(password)
        db.session.add(user)
        db.session.commit()

        return response.success('', "Success create admin")

    except Exception as e:
        print(e)
        return response.badRequest('', "Error")

def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:
            return response.badRequest([], 'Email tidak terdaftar')
        
        if not user.checkPassword(password):
            return response.badRequest([], 'Kombinasi email dan password salah')

        data = singleObject(user)

    

        expires = timedelta(days=7)
        expires_refresh = timedelta(days=7)

        access_token = create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)

        return response.success({
            "email": data["email"],
            "name": data["name"],
            "access_token":access_token,
            "refresh_token": refresh_token
        }, "Success")


    except Exception as e:
        print(e)
        return response.badRequest('', 'Error')