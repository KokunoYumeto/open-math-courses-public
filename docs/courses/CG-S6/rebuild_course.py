"""Rebuild all exact checks, readers and the complete offline archive. CC0-1.0.

Requires Python 3, SymPy, NumPy, Matplotlib and Pandoc. Uses only the included course files.
"""
from pathlib import Path
import datetime,json,subprocess,sys,zipfile

root=Path(__file__).resolve().parent
for name in ['verify_finite_quotients.py','verify_normal_boundaries.py','verify_varying_fillings.py','verify_global_periods.py','draw_period_quotient.py','verify_cusp_geometry.py','draw_cusp_geometry.py','verify_integral_monodromy.py','draw_fundamental_group.py','verify_canonical_ring.py','draw_canonical_ring.py','verify_period_deformation.py','draw_period_identifications.py','verify_almost_complex.py','render_lesson11_figures.py','verify_conormal_torsion.py','verify_smooth_duality.py','verify_proper_curve.py','verify_tangent_index.py','verify_integral_homology.py','verify_morse_cancellation.py','verify_spin_six.py','draw_lesson10.py','draw_finite_twist_complex.py','draw_proper_curve.py','draw_tangent_index.py','draw_morse_cancellation.py','draw_spin_six.py','verify_affine_line_descent.py','draw_affine_line_descent.py']:
    subprocess.run([sys.executable,'-B',str(root/'checks'/name)],check=True)
subprocess.run([sys.executable,'-B',str(root/'rebuild_reader.py')],check=True)
course=json.loads((root/'course.json').read_text(encoding='utf-8'))
date=datetime.date.fromisoformat(course['author']['date'])
stamp=(date.year,date.month,date.day,0,0,0)
members=sorted(p for p in root.rglob('*') if p.is_file()
    and 'downloads' not in p.relative_to(root).parts and '__pycache__' not in p.parts)
destination=root/'downloads/CG-S6-current.zip';destination.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
    for p in members:
        info=zipfile.ZipInfo(p.relative_to(root).as_posix(),date_time=stamp)
        info.compress_type=zipfile.ZIP_DEFLATED
        archive.writestr(info,p.read_bytes())
print(json.dumps({'lessons':len(course['units']),'archive_members':len(members)}))
