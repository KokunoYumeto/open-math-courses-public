"""Reproduce the named exact support diagram in an isolated temporary directory."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,tempfile
HERE=Path(__file__).resolve().parent
EXPECTED={'hyperbolic-first-support.png': {'sha256': '0D9A994DFB30756608E67042EE3726CBE097781A6A2E8FB3A837DA8DF42838E2', 'target': 'an02-l109-hyperbolic-first-support.png'}, 'hyperbolic-first-support.svg': {'sha256': '7430E1E30C04DD10EE62EB295799663CEA78F4AC5C47EF599D65A3D7C159B54F', 'target': 'an02-l109-hyperbolic-first-support.svg'}, 'geometry.json': {'sha256': '2E804E340BCE099AC9C35B86C243B7530C7D120AB79C0AED2B158B66AA98E98D', 'target': 'an02-l109-hyperbolic-first-support-geometry.json'}}
with tempfile.TemporaryDirectory(prefix='an02-l109-figure-') as directory:
    scratch=Path(directory)
    original=scratch/'render_hyperbolic_first_support.py'
    shutil.copyfile(HERE/'an02-l109-render-hyperbolic-first-support.py',original)
    subprocess.run([sys.executable,str(original)],check=True,capture_output=True)
    for name,row in EXPECTED.items():
        data=(scratch/name).read_bytes()
        assert hashlib.sha256(data).hexdigest().upper()==row['sha256'],name
        (HERE/row['target']).write_bytes(data)
print(json.dumps({'exact_PNG_SVG_geometry_reproduced':True}))
