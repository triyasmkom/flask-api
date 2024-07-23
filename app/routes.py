from app import app, response
from app.controller import DosenController, UserController
from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

@app.route('/')
def index():
    return 'Hallo, API Flask'

@app.route('/dosen', methods=["GET", "POST"])
@jwt_required()
def dosen():
    if request.method == 'GET':
        return DosenController.index()
    
    if request.method == 'POST':
        return DosenController.save()

@app.route('/dosen/<id>',methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def dosenDetail(id):
    if request.method == 'GET':
        return DosenController.detail(id)
    if request.method == 'PUT':
        return DosenController.update(id)
    if request.method == 'DELETE':
        return DosenController.delete(id)
    
@app.route('/create-admin',methods=['POST'])
@jwt_required()
def createAdmin():
    return UserController.createAdmin()


@app.route('/login',methods=['POST'])
def login():
    return UserController.login()

@app.route('/protected', methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return response.success(current_user, 'success')

@app.route("/file-upload", methods=['POST'])
@jwt_required()
def uploadFile():
    return UserController.upload()