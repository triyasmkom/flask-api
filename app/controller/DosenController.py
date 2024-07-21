from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa
from pymysql.err import IntegrityError
from app import response, app, db
from flask import request, jsonify

def singleObject(data):
    return {
        'id': data.id,
        'nidn': data.nidn,
        'nama': data.nama,
        'phone': data.phone,
        'alamat': data.alamat,
    }

def singleDetailMahasiswa(dosen, mahasiswa):
    return {
        'id': dosen.id,
        'nidn': dosen.nidn,
        'nama': dosen.nama,
        'phone': dosen.phone,
        'alamat': dosen.alamat,
        'mahasiswa': mahasiswa
    }

def singleObjectMahasiswa(data):
    return {
        "id": data.id,
        "nim": data.nim,
        "nama": data.nama,
        "phone": data.phone,
        "alamat": data.alamat,
    }


def formatArray(datas):
    array = []
    for i in datas:
        array.append(singleObject(i))
    return array

def formatMahasiswa(data):
    array = []
    for i in data:
        array.append(singleObjectMahasiswa(i))
    return array

def index():
    try:
        dosen = Dosen.query.all()
        data = formatArray(dosen)
        return response.success(data, "success")
    except Exception as e:
        print(e)
        return response.badRequest(e.args[0], 'Error')

def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == id)|(Mahasiswa.dosen_dua == id))
        
        if not dosen:
            return response.badRequest([], "Tidak ada data dosen")
        
        dataMahasiswa =  formatMahasiswa(mahasiswa)
        data = singleDetailMahasiswa(dosen, dataMahasiswa)
        
        
        return response.success(data, "Success")
    
    except Exception as e:
        print(e)
        return response.badRequest(e.args[0], 'Error')

def save():
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        dosens = Dosen(nidn=nidn, nama=nama, phone=phone, alamat=alamat)
        db.session.add(dosens)
        db.session.commit()
        
        return response.success('', 'Success')

    except Exception as e:
        return response.badRequest(e.args[0], 'Error')

def update(id):
    try:
        nidn = request.form.get('nidn')
        nama = request.form.get('nama')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        input  =  [{
            'nidn': nidn,
            'nama': nama,
            'phone':phone,
            'alamat': alamat
        }]

        getDosen = Dosen.query.filter_by(id=id).first()
        
        getDosen.nidn = nidn
        getDosen.nama = nama
        getDosen.phone = phone
        getDosen.alamat = alamat
        db.session.commit()

        return response.success(input,'Success')
        
    except Exception as e:
        print(e)
        return response.badRequest('', 'Error')

def delete(id):
    try:
        getDosen = Dosen.query.filter_by(id=id).first()
        if not getDosen :
            return response.badRequest([], 'Error')
        
        db.session.delete(getDosen)
        db.session.commit()
        
        return response.success('', 'success')
    
    except Exception as e :
        print(e)
        return response.badRequest('', 'Error')
