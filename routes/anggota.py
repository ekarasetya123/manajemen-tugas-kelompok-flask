from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from models import db, Anggota

anggota_bp = Blueprint('anggota', __name__, url_prefix='/anggota')

@anggota_bp.route('/')
@login_required
def index():
    anggota_list = Anggota.query.order_by(Anggota.nama).all()
    return render_template('anggota/index.html', anggota_list=anggota_list)

@anggota_bp.route('/tambah', methods=['GET', 'POST'])
@login_required
def tambah():
    if request.method == 'POST':
        nama = request.form['nama']
        nim = request.form['nim']
        kontak = request.form.get('kontak', '')
        if not nama or not nim:
            flash('Nama dan NIM wajib diisi.', 'danger')
            return redirect(request.url)
        if Anggota.query.filter_by(nim=nim).first():
            flash('NIM sudah terdaftar.', 'danger')
            return redirect(request.url)
        anggota = Anggota(nama=nama, nim=nim, kontak=kontak)
        db.session.add(anggota)
        db.session.commit()
        flash('Anggota berhasil ditambahkan.', 'success')
        return redirect(url_for('anggota.index'))
    return render_template('anggota/tambah.html')

@anggota_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    anggota = Anggota.query.get_or_404(id)
    if request.method == 'POST':
        nama = request.form['nama']
        nim = request.form['nim']
        kontak = request.form.get('kontak', '')
        if not nama or not nim:
            flash('Nama dan NIM wajib diisi.', 'danger')
            return redirect(request.url)
        # Check NIM uniqueness excluding current
        existing = Anggota.query.filter(Anggota.nim==nim, Anggota.id!=id).first()
        if existing:
            flash('NIM sudah digunakan oleh anggota lain.', 'danger')
            return redirect(request.url)
        anggota.nama = nama
        anggota.nim = nim
        anggota.kontak = kontak
        db.session.commit()
        flash('Anggota berhasil diperbarui.', 'success')
        return redirect(url_for('anggota.index'))
    return render_template('anggota/edit.html', anggota=anggota)

@anggota_bp.route('/hapus/<int:id>', methods=['POST'])
@login_required
def hapus(id):
    anggota = Anggota.query.get_or_404(id)
    db.session.delete(anggota)
    db.session.commit()
    flash('Anggota berhasil dihapus.', 'success')
    return redirect(url_for('anggota.index'))