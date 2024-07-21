from app import db
from app.model.dosen import Dosen

class Mahasiswa(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nim = db.Column(db.String(38), nullable=False, index=True, unique=True)
    nama = db.Column(db.String(58), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    alamat = db.Column(db.String(108), nullable=False)
    dosen_satu = db.Column(db.BigInteger, db.ForeignKey(Dosen.id,  ondelete='CASCADE'))
    dosen_dua = db.Column(db.BigInteger, db.ForeignKey(Dosen.id,  ondelete='CASCADE'))

    def __repr__(self):
        return '<Mahasiswa {}>'.format(self.name)