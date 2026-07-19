from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import String
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(String(80), unique=True, nullable=False)
    password_hash = db.Column(String(120), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class MataKuliah(db.Model):
    __tablename__ = 'mata_kuliah'
    id = db.Column(db.Integer, primary_key=True)
    nama_matkul = db.Column(String(100), nullable=False)
    dosen = db.Column(String(100), nullable=False)
    # Relationship
    tugas = db.relationship('Tugas', backref='mata_kuliah', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<MataKuliah {self.nama_matkul}>'

class Anggota(db.Model):
    __tablename__ = 'anggota'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(String(100), nullable=False)
    nim = db.Column(String(20), unique=True, nullable=False)
    kontak = db.Column(String(50))
    # Relationship
    pembagian = db.relationship('PembagianTugas', backref='anggota', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Anggota {self.nama}>'

class Tugas(db.Model):
    __tablename__ = 'tugas'
    id = db.Column(db.Integer, primary_key=True)
    matkul_id = db.Column(db.Integer, db.ForeignKey('mata_kuliah.id'), nullable=False)
    judul_tugas = db.Column(String(200), nullable=False)
    deskripsi = db.Column(db.Text)
    deadline = db.Column(db.DateTime)
    status = db.Column(String(20), default='belum')  # belum, proses, selesai
    dibuat_pada = db.Column(db.DateTime, default=datetime.utcnow)
    # Relationship
    pembagian = db.relationship('PembagianTugas', backref='tugas', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Tugas {self.judul_tugas}>'

class PembagianTugas(db.Model):
    __tablename__ = 'pembagian_tugas'
    id = db.Column(db.Integer, primary_key=True)
    tugas_id = db.Column(db.Integer, db.ForeignKey('tugas.id'), nullable=False)
    anggota_id = db.Column(db.Integer, db.ForeignKey('anggota.id'), nullable=False)
    bagian_kerja = db.Column(String(200))
    status_bagian = db.Column(String(20), default='belum')  # belum, proses, selesai

    def __repr__(self):
        return f'<PembagianTugas Tugas:{self.tugas_id} Anggota:{self.anggota_id}>'