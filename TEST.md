# Hasil Pengujian Black-Box Sistem Manajemen Tugas Kelompok

Berikut adalah tabel hasil pengujian black-box untuk fitur-fitur utama aplikasi. Pengujian dilakukan secara manual dengan memeriksa respons aplikasi terhadap input yang diberikan.

| No | Scenario | Hasil Diharapkan | Hasil Aktual | Kesimpulan |
|----|----------|------------------|--------------|------------|
| 1 | Login dengan kredensial default (admin / admin123) | Berhasil login dan dialihkan ke halaman dashboard | Berhasil login dan dialihkan ke halaman dashboard | ✅ Lulus |
| 2 | Login dengan username atau password salah | Gagal login, tetap di halaman login, muncul pesan error "Username atau password salah." | Gagal login, tetap di halaman login, muncul pesan error "Username atau password salah." | ✅ Lulus |
| 3 | Tambah tugas baru dengan data lengkap | Tugas berhasil ditambahkan, muncul flash message "Tugas berhasil ditambahkan." dan redirect ke daftar tugas | Tugas berhasil ditambahkan, muncul flash message "Tugas berhasil ditambahkan." dan redirect ke daftar tugas | ✅ Lulus |
| 4 | Edit tugas yang ada | Tugas berhasil diperbarui, flash message "Tugas berhasil diperbarui." dan redirect ke daftar tugas | Tugas berhasil diperbarui, flash message "Tugas berhasil diperbarui." dan redirect ke daftar tugas | ✅ Lulus |
| 5 | Hapus tugas yang ada | Tugas berhasil dihapus, flash message "Tugas berhasil dihapus." dan redirect ke daftar tugas | Tugas berhasil dihapus, flash message "Tugas berhasil dihapus." dan redirect ke daftar tugas | ✅ LULS |
| 6 | Tambah anggota baru dengan data lengkap | Anggota berhasil ditambahkan, flash message "Anggota berhasil ditambahkan." dan redirect ke daftar anggota | Anggota berhasil ditambahkan, flash message "Anggota berhasil ditambahkan." dan redirect ke daftar anggota | ✅ Lulus |
| 7 | Edit anggota yang ada | Anggota berhasil diperbarui, flash message "Anggota berhasil diperbarui." dan redirect ke daftar anggota | Anggota berhasil diperbarui, flash message "Anggota berhasil diperbarui." dan redirect ke daftar anggota | ✅ Lulus |
| 8 | Hapus anggota yang ada | Anggota berhasil dihapus, flash message "Anggota berhasil dihapus." dan redirect ke daftar anggota | Anggota berhasil dihapus, flash message "Anggota berhasil dihapus." dan redirect ke daftar anggota | ✅ Lulus |
| 9 | Akses halaman pembagian tugas (misal /tugas/1/pembagian) | Halaman pembagian tugas ditampilkan dengan daftar anggota dan checkbox untuk asignasi | Halaman pembagian tugas ditampilkan dengan daftar anggota dan checkbox untuk asignasi | ✅ Lulus |
| 10 | Validasi form tambah tugas dengan judul kosong | Form tidak disubmit, muncul pesan validasi "Judul tugas tidak boleh kosong" (client-side) atau setelah submit muncul flash error (server-side) | Setelah submit dengan judul kosong, muncul flash message error "Judul tugas tidak boleh kosong." | ✅ Lulus |

**Catatan:**
- Semua tes dilakukan versi aplikasi yang berjalan pada `http://127.0.0.1:5000`.
- Untuk keamanan, password default sebaiknya diubah setelah pertama kali login dalam produksi.
- Penggunaan flash message menggunakan Bootstrap-like styling melalui custom CSS.