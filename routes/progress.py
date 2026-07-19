from flask import Blueprint, render_template, request
from flask_login import login_required
from models import db, Tugas, MataKuliah, PembagianTugas, Anggota
from sqlalchemy.orm import joinedload
from collections import defaultdict

progress_bp = Blueprint('progress', __name__, url_prefix='/progress')

@progress_bp.route('/')
def index():
    # Filter parameters
    matkul_id = request.args.get('matkul_id', type=int)
    status = request.args.get('status')

    # Base query with eager loading of pembagian and its anggota
    query = Tugas.query.options(
        joinedload(Tugas.pembagian).joinedload(PembagianTugas.anggota)
    )
    if matkul_id:
        query = query.filter_by(matkul_id=matkul_id)
    if status:
        query = query.filter_by(status=status)

    tugas_list = query.all()

    # Compute progress percentage for each task (based on assignees completed)
    for t in tugas_list:
        total = len(t.pembagian)
        done = sum(1 for p in t.pembagian if p.status_bagian == 'selesai')
        t.progress = (done / total * 100) if total > 0 else 0

    # Group tasks by mata kuliah
    groups = defaultdict(list)
    for t in tugas_list:
        groups[t.mata_kuliah].append(t)
    matkul_groups = [(matkul, tasks) for matkul, tasks in groups.items()]

    # Get all mata kuliah for filter dropdown
    mata_kuliah_list = MataKuliah.query.order_by(MataKuliah.nama_matkul).all()

    return render_template('progress/index.html',
                           matkul_groups=matkul_groups,
                           mata_kuliah_list=mata_kuliah_list,
                           selected_matkul=matkul_id,
                           selected_status=status)