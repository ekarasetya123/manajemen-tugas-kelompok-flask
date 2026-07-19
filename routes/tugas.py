from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models import db, Tugas, MataKuliah, Anggota, PembagianTugas
from datetime import datetime

tugas_bp = Blueprint('tugas', __name__, url_prefix='/tugas')

@tugas_bp.route('/')
@login_required
def index():
    matkul_id = request.args.get('matkul_id', type=int)
    status = request.args.get('status')
    query = Tugas.query
    if matkul_id:
        query = query.filter_by(matkul_id=matkul_id)
    if status:
        query = query.filter_by(status=status)
    tugas_list = query.order_by(Tugas.dibuat_pada.desc()).all()
    matkul_list = MataKuliah.query.order_by(MataKuliah.nama_matkul).all()
    return render_template('tugas/index.html', tugas_list=tugas_list,
                           matkul_list=matkul_list,
                           selected_matkul=matkul_id,
                           selected_status=status)

@tugas_bp.route('/tambah', methods=['GET', 'POST'])
@login_required
def tambah():
    if request.method == 'POST':
        judul = request.form['judul_tugas']
        deskripsi = request.form['deskripsi']
        deadline_str = request.form['deadline']
        status = request.form['status']
        matkul_id = request.form['matkul_id']
        # Validation
        if not judul:
            flash('Judul tugas tidak boleh kosong.', 'danger')
            return redirect(request.url)
        try:
            deadline = datetime.strptime(deadline_str, '%Y-%m-%d') if deadline_str else None
        except ValueError:
            flashformat='Invalid date format.'
            flash('Format tanggal tidak valid.', 'danger')
            return redirect(request.url)
        tugas = Tugas(judul_tugas=judul, deskripsi=deskripsi,
                      deadline=deadline, status=status, matkul_id=matkul_id)
        db.session.add(tugas)
        db.session.commit()
        flash('Tugas berhasil ditambahkan.', 'success')
        return redirect(url_for('tugas.index'))
    matkul_list = MataKuliah.query.order_by(MataKuliah.nama_matkul).all()
    return render_template('tugas/tambah.html', matkul_list=matkul_list)

@tugas_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    tugas = Tugas.query.get_or_404(id)
    if request.method == 'POST':
        tugas.judul_tugas = request.form['judul_tugas']
        tugas.deskripsi = request.form['deskripsi']
        deadline_str = request.form['deadline']
        tugas.status = request.form['status']
        tugas.matkul_id = request.form['matkul_id']
        if not tugas.judul_tugas:
            flash('Judul tugas tidak boleh kosong.', 'danger')
            return redirect(request.url)
        try:
            tugas.deadline = datetime.strptime(deadline_str, '%Y-%m-%d') if deadline_str else None
        except ValueError:
            flash('Format tanggal tidak valid.', 'danger')
            return redirect(request.url)
        db.session.commit()
        flash('Tugas berhasil diperbarui.', 'success')
        return redirect(url_for('tugas.index'))
    matkul_list = MataKuliah.query.order_by(MataKuliah.nama_matkul).all()
    return render_template('tugas/edit.html', tugas=tugas,
                           matkul_list=matkul_list)

@tugas_bp.route('/hapus/<int:id>', methods=['POST'])
@login_required
def hapus(id):
    tugas = Tugas.query.get_or_404(id)
    db.session.delete(tugas)
    db.session.commit()
    flash('Tugas berhasil dihapus.', 'success')
    return redirect(url_for('tugas.index'))

@tugas_bp.route('/<int:id>/pembagian', methods=['GET', 'POST'])
@login_required
def pembagian(id):
    tugas = Tugas.query.get_or_404(id)
    if request.method == 'POST':
        # Clear existing assignments for this tugas (optional) or update
        # For simplicity, we'll replace all assignments
        PembagianTugas.query.filter_by(tugas_id=id).delete()
        # Get selected anggota and their bagian_kerja and status
        anggota_ids = request.form.getlist('anggota_id')
        for anggota_id in anggota_ids:
            bagian = request.form.get(f'bagian_{anggota_id}', '')
            status = request.form.get(f'status_{anggota_id}', 'belum')
            pembagian = PembagianTugas(tugas_id=id, anggota_id=int(anggota_id),
                                       bagian_kerja=bagian, status_bagian=status)
            db.session.add(pembagian)
        db.session.commit()
        flash('Pembagian tugas berhasil diperbarui.', 'success')
        return redirect(url_for('tugas.index'))
    anggota_list = Anggota.query.order_by(Anggota.nama).all()
    # Current assignments
    current = {p.anggota_id: p for p in tugas.pembagian}
    return render_template('tugas/pembagian.html', tugas=tugas,
                           anggota_list=anggota_list,
                           current=current)