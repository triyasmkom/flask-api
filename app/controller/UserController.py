from app.model.user import User
from app.model.gambar import Gambar
from app import response, app, db, upload_config
from flask_jwt_extended import *
from flask import request
from datetime import timedelta
import os
import uuid
from werkzeug.utils import secure_filename

def create_folder(folder_path):
    try:
        os.makedirs(folder_path, exist_ok=True)
        print(f"Folder '{folder_path}' created successfully.")
    except Exception as e:
        print(f"Error creating folder '{folder_path}': {e}")


def upload():
    try:
        judul = request.form.get('judul')
        if 'file' not in request.files:
            return response.badRequest([], 'File tidak tersedia 1')
        
        file = request.files['file']
        if file.filename == '' :
            return response.badRequest([], 'File tidak tersedia 2')
        if file and upload_config.allowed_file(file.filename):
            uid = uuid.uuid4()
            filename = secure_filename(file.filename)
            renameFile = "Flask-"+str(uid)+filename
            pathName = os.path.join("./uploadFile", renameFile)
            create_folder("./uploadFile")
            file.save(pathName)

            uploads = Gambar(judul=judul, pathname= renameFile)
            db.session.add(uploads)
            db.session.commit()

            return response.success({
                "judul": judul,
                "pathname": renameFile
            }, 'Success Upload File')
        
        else:
            return response.badRequest([], "File tidak diizinkan")


    except Exception as e:
        print(e)

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