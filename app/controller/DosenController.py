from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa
from pymysql.err import IntegrityError
from app import response, app, db
from flask import request, jsonify
import math

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


    
def get_pagination(clss, url, start, limit):
    try:
        # ambil data
        results = clss.query.all()

        # ubah format
        data = formatArray(results)

        # hitung
        count = len(data)

        obj = {}
        if count < start:
            obj['success'] = False
            obj['message'] = "Page yang dipilih melewati batas total data!"
            return obj
        else:
            obj['success'] = True
            obj['start_page'] = start
            obj['per_page'] = limit
            obj['total_data'] = count
            obj['total_page'] = math.ceil(count/limit)

            # prev link
            if start == 1:
                obj['previous'] = ''
            else:
                
                start_copy = max(1, start-limit)
                limit_copy = start - 1
                
                obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
            
            # next link
            if start + limit > count:
                
                obj["next"] = ""

            else:
                
                start_copy = start+limit
                obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
            
            obj['results'] = data[(start - 1): (start - 1 + limit)]

            return obj


    except Exception as e:
        print(e)

def paginate():
    try:
         # ambil parameter get
        start = request.args.get('start')
        limit = request.args.get('limit')

        if start == None or limit == None:
            return jsonify(get_pagination(
                Dosen,
                "http://127.0.0.1:5000/api/dosen/page",
                start=request.args.get('start',1),
                limit=request.args.get('limit',3)
            ))
        else:
            return jsonify(get_pagination(
                Dosen,
                "http://127.0.0.1:5000/api/dosen/page",
                start=int(start),
                limit=int(limit)
            ))

    except Exception as e:
        print(e)
