# Sistem Manajemen Tugas Kelompok Mata Kuliah

Aplikasi web berbasis Flask untuk membantu mahasiswa mengelola pembagian tugas kelompok dan memantau progres pengerjaan.

## Fitur Utama
- Autentikasi admin
- CRUD Mata Kuliah, Tugas, Anggota, Pembagian Tugas
- Dashboard dengan ringkasan dan grafik
- Validasi input client-side dan server-side
- Flash message dan navigasi jelas

## Cara Instalasi
1. Clone repo ini
2. `pip install -r requirements.txt`
3. Atur variabel lingkungan (FLASK_APP, FLASK_ENV, SECRET_KEY, DATABASE_URL jika perlu)
4. Jalankan migrasi database (jika menggunakan Flask-Migrate) atau buat SQLite otomatis
5. Jalankan aplikasi: `flask run` atau `python app.py`

## Catatan
- Kredensial default admin untuk testing: `admin` / `admin123` (ubah di production)
- Pastikan SQLite database terbuat di `instance/database.db`

## Lisensi
MIT