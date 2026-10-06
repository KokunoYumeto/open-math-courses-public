"""Build the reading PDFs in the current lesson order from complete TeX sources."""
import ctypes,datetime,hashlib,json,os,shutil,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parent;build=root/'build';build.mkdir(exist_ok=True)
handle=None;kernel=None
try:
    if os.name=='nt':
        kernel=ctypes.WinDLL('kernel32',use_last_error=True)
        kernel.CreateMutexW.argtypes=[ctypes.c_void_p,ctypes.c_int,ctypes.c_wchar_p]
        kernel.CreateMutexW.restype=ctypes.c_void_p
        kernel.WaitForSingleObject.argtypes=[ctypes.c_void_p,ctypes.c_ulong]
        kernel.ReleaseMutex.argtypes=[ctypes.c_void_p]
        kernel.CloseHandle.argtypes=[ctypes.c_void_p]
        handle=kernel.CreateMutexW(None,False,r'Global\InterlanguageTeXSlotV1')
        if not handle:raise OSError('Could not open the TeX mutex')
        result=kernel.WaitForSingleObject(handle,0)
        if result not in (0,128):
            kernel.CloseHandle(handle);handle=None
            raise RuntimeError('TeX slot occupied; no engine launched. Continue source editing and compile later.')
        if result==128:print('Recovered an abandoned TeX mutex.')
    engine=shutil.which('pdflatex')
    if not engine:raise RuntimeError('No configured pdflatex executable is available.')
    version=subprocess.run([engine,'--version'],capture_output=True,text=True,check=True).stdout
    extra=['--disable-installer'] if 'MiKTeX' in version else []
    catalog=json.loads((root/'catalogue.json').read_text(encoding='utf8'))
    names=['Reductive-group-schemes',*[u['id'] for u in catalog['courses'][0]['units']]]
    selected=sys.argv[1:] or names
    if any(name not in names for name in selected):raise ValueError('Unknown PDF document')
    for name in selected:
        for run in (1,2):
            proc=subprocess.run([engine,*extra,'-interaction=nonstopmode','-halt-on-error',
                '-output-directory='+build.as_posix(),name+'.tex'],cwd=root,capture_output=True)
            (build/f'{name}.pass-{run}.txt').write_bytes(proc.stdout+proc.stderr)
            if proc.returncode:raise RuntimeError('Compilation failed: '+name+'; inspect build logs.')
        shutil.copyfile(build/(name+'.pdf'),root/(name+'.pdf'))
        receipt_path=build/'build-receipts.json'
        receipts=json.loads(receipt_path.read_text(encoding='utf8')) if receipt_path.exists() else {}
        receipts[name]={'built_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'source_sha256':hashlib.sha256((root/(name+'.tex')).read_bytes()).hexdigest().upper(),
            'pdf_sha256':hashlib.sha256((root/(name+'.pdf')).read_bytes()).hexdigest().upper(),
            'engine':version.splitlines()[0],'passes':2}
        receipt_path.write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf8')
        print('Built '+name+'.pdf',flush=True)
finally:
    if handle:kernel.ReleaseMutex(handle);kernel.CloseHandle(handle)
