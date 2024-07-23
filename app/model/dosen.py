from app import db

class Dosen(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nidn = db.Column(db.String(38), nullable=False, index=True, unique=True)
    nama = db.Column(db.String(58), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    alamat = db.Column(db.String(108), nullable=False)

    def __repr__(self):
        return '<Dosen {}>'.format(self.name)