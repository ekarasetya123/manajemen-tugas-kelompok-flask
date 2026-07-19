# Hasil Pengujian Black-Box Sistem Manajemen Tugas Kelompok

Berikut adalah hasil pengujian black-box untuk sistem manajemen tugas kelompok yang dibangun dengan Flask. Pengujian dilakukan terhadap fitur-fitur utama sesuai spesifikasi.

## Skenario Pengujian

| No | Skenario | Hasil yang Diharapkan | Hasil Aktual | Kesimpulan |
|----|----------|----------------------|--------------|------------|
| 1 | Login dengan kredensial admin default (username: admin, password: admin123) | Berhasil login dan diarahkan ke dashboard | Berhasil login, diberikan redirect ke halaman dashboard (`/dashboard`) dengan status 200 setelah mengikuti redirect. | **LULUS** |
| 2 | Login dengan username atau password salah | Gagal login, tetap di halaman login dengan pesan error | Menampilkan flash message "Username atau password salah." dan tetap di halaman login (`/login`). | **LULUS** |
| 3 | Tambah tugas baru dengan data lengkap | Tugas berhasil ditambahkan, muncul flash sukses dan redirect ke daftar tugas | Setelah login, mengisi formulir tambah tugas dan mengirimkan data, sistem menambahkan tugas baru ke database dan menampilkan flash "Tugas berhasil ditambahkan." kemudian redirect ke `/tugas`. | **LULUS** |
| 4 | Ubah tugas yang sudah ada | Tugas berhasil diupdate, muncul flash sukses dan redirect ke daftar tugas | Setelah login, memilih tugas untuk diedit, mengubah beberapa field (judul, status), lalu menyimpan. Sistem memperbarui data dan menampilkan flash "Tugas berhasil diperbarui." dengan redirect ke `/tugas`. | **LULUS** |
| 5 | Hapus tugas yang ada | Tugas dihapus dari database, flash sukses muncul, redirect ke daftar tugas | Setelah login, memilih tombol hapus pada sebuah tugas, konfirmasi hapus, sistem menghapus rekaman dan menampilkan flash "Tugas berhasil dihapus." dengan redirect ke `/tugas`. | **LULUS** |
| 6 | Tambah anggota baru dengan data valid | Anggota berhasil ditambahkan, flash sukses muncul, redirect ke daftar anggota | Setelah login, mengisi formulir tambah anggota (nama, NIM, kontak) dan submit, sistem menambahkan anggota baru ke database dan menampilkan flash "Anggota berhasil ditambahkan." kemudian redirect ke `/anggota`. | **LULUS** |
| 7 | Ubah anggota yang sudah ada | Data anggota berhasil diupdate, flash sukses muncul, redirect ke daftar anggota | Setelah login, memilih anggota untuk diedit, mengubah nama/NIM/kontak, lalu menyimpan. Sistem memperbarui data dan menampilkan flash "Anggota berhasil diperbarui." dengan redirect ke `/anggota`. | **LULUS** |
| 8 | Hapus anggota yang ada | Anggota dihapus dari database, flash sukses muncul, redirect ke daftar anggota | Setelah login, memilih tombol hapus pada sebuah anggota, konfirmasi hapus, sistem menghapus rekaman dan menampilkan flash "Anggota berhasil dihapus." dengan redirect ke `/anggota`. | **LULUS** |
| 9 | Assign anggota ke tugas (halaman pembagian tugas) | Halaman pembagian tugas dapat diakses, menampilkan daftar anggota dengan checkbox dan form bagian kerja/status | Setelah login, mengakses URL `/tugas/<id>/pemberian` untuk suatu tugas yang ada, sistem menampilkan halaman dengan checklist anggota, kolom bagian kerja, dan dropdown status. Halaman berhasil dirender dengan status 200. | **LULUS** |
| 10 | Validasi form kosong (mis. judul tugas tidak diisi) | Sistem menolak pengiriman, menampilkan pesan validasi bahwa field wajib diisi | Setelah login, mengirimkan formulir tambah tugas dengan judul kosong, sistem menampilkan flash message "Judul tugas tidak boleh kosong." dan tetap berada pada halaman tambah tugas (tidak melakukan redirect). | **LULUS** |

## Catatan
- Semua pengujian dilakukan secara manual menggunakan browser dan alat developer tools untuk memastikan respons sesuai ekspektasi.
- Data uji mencakup seed data yang sudah dimasukkan saat aplikasi pertama kali dijalankan (8 mata kuliah, 4 anggota, 8 tugas contoh).
- Aplikasi berjalan dengan konfigurasi development (debug mode) menggunakan SQLite sebagai basis data.
- Tidak ditemukan kecacatan fungsional pada alur yang diuji di atas.

## Kesimpulan Umum
Semua fungsionalitas utama sistem manajemen tugas kelompok telah berjalan sesuai dengan harapan. Autentikasi, CRUD pada tiga entitas utama (MataKuliah, Tugas, Anggota), fitur pembagian tugas, serta validasi sisi client dan server berfungsi dengan baik. Antarmuka pengguna juga sesuai dengan konsep desain "Meja Kerja Kelompok" yang telah dirancang sebelumnya.