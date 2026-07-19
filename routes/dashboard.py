from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from models import db, MataKuliah, Tugas, Anggota, PembagianTugas
from datetime import datetime, timedelta

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
@login_required
def index():
    # Statistics
    total_tugas = Tugas.query.count()
    total_anggota = Anggota.query.count()
    tugas_belum = Tugas.query.filter_by(status='belum').count()
    tugas_proses = Tugas.query.filter_by(status='proses').count()
    tugas_selesai = Tugas.query.filter_by(status='selesai').count()
    # Deadline soon (within 3 days)
    three_days_later = datetime.now() + timedelta(days=3)
    tugas_deadline_soon = Tugas.query.filter(Tugas.deadline <= three_days_later, Tugas.deadline >= datetime.now(), Tugas.status != 'selesai').count()
    # Data for chart: status distribution
    status_data = {
        'belum': tugas_belum,
        'proses': tugas_proses,
        'selesai': tugas_selesai
    }
    recent_tugas = Tugas.query.order_by(Tugas.dibuat_pada.desc()).limit(5).all()
    return render_template('dashboard/index.html',
                           total_tugas=total_tugas,
                           total_anggota=total_anggota,
                           tugas_belum=tugas_belum,
                           tugas_proses=tugas_proses,
                           tugas_selesai=tugas_selesai,
                           tugas_deadline_soon=tugas_deadline_soon,
                           status_data=status_data,
                           recent_tugas=recent_tugas)
