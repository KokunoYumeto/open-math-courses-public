"""Package the supplied local NT-CFT edition, without publishing or compiling."""
from pathlib import Path
import hashlib, json, zipfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
READER=ROOT/'docs/courses/NT-CFT'
assert HERE==ROOT/'courses/NT-CFT' and (READER/'index.html').is_file()
assert not (ROOT/'.git').exists(), 'Package from the extracted course-only source ZIP, outside the programme Git checkout.'
assert all(p.name=='NT-CFT' or not (p/'src').exists() for p in (ROOT/'courses').iterdir() if p.is_dir()), 'The source tree must contain only this course body.'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,data):p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def eligible(p):
    return (p.is_file() and not p.is_symlink() and '__pycache__' not in p.parts
            and p.suffix not in ('.pyc','.zip')
            and p.name not in ('SOURCE_MANIFEST.json','READER_MANIFEST.json','prepare_release.py'))
def archive(destination,root,files):
    destination.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(files):
            assert p.resolve().is_relative_to(root.resolve())
            info=zipfile.ZipInfo(p.relative_to(root).as_posix(),date_time=(2026,10,5,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o100644<<16
            z.writestr(info,p.read_bytes())

files=[p for p in ROOT.rglob('*') if eligible(p)]
manifest=ROOT/'SOURCE_MANIFEST.json'
save(manifest,{'schema':'nt-cft-source-manifest/v2','edition':'local corrected draft',
    'excluded':['SOURCE_MANIFEST.json','READER_MANIFEST.json','ZIP archives','Python bytecode'],
    'files':[{'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)]})
source=READER/'files/class-field-theory-source.zip'
archive(source,ROOT,files+[manifest])

# The reader manifest additionally binds the downloadable source archive.
reader_files=[p for p in READER.rglob('*') if eligible(p)]+[source]
reader_manifest=READER/'READER_MANIFEST.json'
save(reader_manifest,{'schema':'nt-cft-reader-manifest/v1','edition':'local corrected draft',
    'excluded':['READER_MANIFEST.json','Python bytecode'],
    'files':[{'path':p.relative_to(READER).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(reader_files)]})
reader=ROOT/'class-field-theory-reader.zip'
archive(reader,READER,reader_files+[reader_manifest])
print(json.dumps({'source_archive':str(source),'source_sha256':sha(source),
    'reader_archive':str(reader),'reader_sha256':sha(reader),
    'source_files':len(files)+1,'reader_files':len(reader_files)+1,'remote_writes':0}))
