from app import app
from app.controller import DosenController
from flask import request

@app.route('/')
def index():
    return 'Hallo, API Flask'

@app.route('/dosen', methods=["GET", "POST"])
def dosen():
    if request.method == 'GET':
        return DosenController.index()
    
    if request.method == 'POST':
        return DosenController.save()

@app.route('/dosen/<id>',methods=['GET', 'PUT', 'DELETE'])
def dosenDetail(id):
    if request.method == 'GET':
        return DosenController.detail(id)
    if request.method == 'PUT':
        return DosenController.update(id)
    if request.method == 'DELETE':
        return DosenController.delete(id)
    


