"""Recreate the offline download from a clean extracted edition. CC0 1.0.
Packaging code: GPT-6 Astra (OpenAI), Ultra, October 2026.
Run: python -B make-download.py
"""
from pathlib import Path
import html, json, zipfile

ROOT = Path(__file__).resolve().parent
config = json.loads((ROOT / 'course.json').read_text(encoding='utf-8'))
cid, title = config['id'], config['title']
archive = ROOT.parent.parent / 'downloads' / (cid + '.zip')
archive.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for path in sorted(ROOT.rglob('*')):
        if path.is_file() and '__pycache__' not in path.parts:
            info = zipfile.ZipInfo('courses/' + cid + '/' + path.relative_to(ROOT).as_posix(), (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, path.read_bytes())
    info = zipfile.ZipInfo('index.html', (1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    z.writestr(info, '<!doctype html><meta charset="utf-8"><title>' + html.escape(title) + '</title><p><a href="courses/' + cid + '/index.html">Read ' + html.escape(title) + '</a></p>')
print(archive.name)

