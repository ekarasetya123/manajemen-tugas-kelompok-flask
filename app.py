from flask import Flask
from config import Config
from models import db, User, MataKuliah, Anggota, Tugas, PembagianTugas
from routes.auth import auth_bp, create_admin_user
from routes.dashboard import dashboard_bp
from routes.tugas import tugas_bp
from routes.anggota import anggota_bp
from flask_login import LoginManager
from datetime import datetime, timedelta

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Silakan login untuk mengakses halaman ini.'
    login_manager.login_message_category = 'info'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(tugas_bp)
    app.register_blueprint(anggota_bp)

    # Create tables, admin user, and seed data
    with app.app_context():
        db.create_all()
        create_admin_user()
        # Seed mata kuliah if none exist
        if MataKuliah.query.count() == 0:
            mata_kuliah_list = [
                ('Kewarganegaraan', 'Dr. Siti Nurhaliza'),
                ('Logika Matematika', 'Prof. Budi Santoso'),
                ('Algoritma dan Pemrograman 2', 'Dr. Ana Suryadi'),
                ('Kalkulus II', 'Prof. Dewi Lestari'),
                ('Transformasi Digital', 'Dr. Reza Pratama'),
                ('Pengantar Pemrograman', 'Pak Ahmad Fauzi'),
                ('Pemrograman Berorientasi Objek', 'Bu Lina Marlina'),
                ('Bahasa Indonesia', 'Dr. Suryaadi')
            ]
            for nama, dosen in mata_kuliah_list:
                mk = MataKuliah(nama_matkul=nama, dosen=dosen)
                db.session.add(mk)
            db.session.commit()
        # Seed anggota if none exist
        if Anggota.query.count() == 0:
            anggota_list = [
                ('Eka Prasetya Wardana', '301250023', '081234567890'),
                ('Budi Santoso', '301250024', '081234567891'),
                ('Ani Lestari', '301250025', '081234567892'),
                ('Dewi Rachmawati', '301250026', '081234567893')
            ]
            for nama, nim, kontak in anggota_list:
                agt = Anggota(nama=nama, nim=nim, kontak=kontak)
                db.session.add(agt)
            db.session.commit()
        # Seed tugas if none exist
        if Tugas.query.count() == 0:
            # Get some mata kuliah IDs
            mks = MataKuliah.query.all()
            mk_ids = [m.id for m in mks]
            # Ensure we have at least one MK
            if mk_ids:
                # Use today as base
                today = datetime.today().date()
                tugas_data = [
                    ('Tugas 1 Kewarganegaraan', 'Buat esai tentang hak dan kewajiban warga negara', mk_ids[0] if len(mk_ids) > 0 else None, today + timedelta(days=2), 'belum'),
                    ('Latihan Logika', 'Soal-soal tentang proposisi dan bukti indirekt', mk_ids[1] if len(mk_ids) > 1 else None, today + timedelta(days=5), 'proses'),
                    ('Algoritma Sorting', 'Implementasi quicksort dan mergesort dalam Python', mk_ids[2] if len(mk_ids) > 2 else None, today + timedelta(days=3), 'selesai'),
                    ('Integral Lipat Ganda', 'Hitung luas daerah terkena fungsi f(x,y)', mk_ids[3] if len(mk_ids) > 3 else None, today + timedelta(days=1), 'belum'),
                    ('Presentasi Transformasi Digital', 'Buat slide 10 halaman tentang dampak AI', mk_ids[4] if len(mk_ids) > 4 else None, today + timedelta(days=7), 'proses'),
                    ('Hello World', 'Buat program saperta console output', mk_ids[5] if len(mk_ids) > 5 else None, today + timedelta(days=4), 'belum'),
                    ('Inheritance dan Polymorphism', 'Buat kelas Hewan dan turunannya', mk_ids[6] if len(mk_ids) > 6 else None, today + timedelta(days=6), 'proses'),
                    ('Ejaan dan Struktur Paragraf', 'Latihan membuat paragraph efektif', mk_ids[7] if len(mk_ids) > 7 else None, today + timedelta(days=0), 'selesai')
                ]
                for judul, deskripsi, mk_id, deadline, status in tugas_data:
                    if mk_id is not None:
                        t = Tugas(judul_tugas=judul, deskripsi=deskripsi, matkul_id=mk_id,
                                  deadline=datetime.combine(deadline, datetime.min.time()),
                                  status=status)
                        db.session.add(t)
                db.session.commit()
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)