"""Two isolated fresh-process replays of the finite portable figure inputs."""
from pathlib import Path
import argparse, hashlib, json, shutil, subprocess, sys
import xml.etree.ElementTree as ET
HERE=Path(__file__).resolve().parent
PUBLIC=HERE.parent.parent
parser=argparse.ArgumentParser()
parser.add_argument('--work-dir',type=Path,default=HERE/'qa')
args=parser.parse_args()
args.work_dir=args.work_dir.resolve()
INPUTS=['draw_translation_oscillator.py','FONT-NOTICE.txt']
INPUTS += [p.relative_to(HERE).as_posix() for p in sorted((HERE/'fonts').glob('*')) if p.is_file()]
OUTPUTS=['figures/kt-translation-oscillator-graph.png',
         'figures/kt-translation-oscillator-graph.svg',
         'reproduction/translation-oscillator-graph/FIGURE-CHECKS.json']
def binding(p,base):
 b=p.read_bytes()
 return {'path':p.relative_to(base).as_posix(),'bytes':len(b),
         'sha256':hashlib.sha256(b).hexdigest().upper()}
runs=[]
for n in [1,2]:
 base=args.work_dir/('reproduction-'+str(n))
 dest=base/'reproduction/translation-oscillator-graph'
 dest.mkdir(parents=True,exist_ok=True)
 for name in INPUTS:
  target=dest/name;target.parent.mkdir(parents=True,exist_ok=True)
  shutil.copyfile(HERE/name,target)
 result=subprocess.run([sys.executable,'-B','-X','utf8',
                        str(dest/'draw_translation_oscillator.py')],
                       cwd=base,encoding='utf-8',capture_output=True)
 (base/'stdout.txt').write_text(result.stdout,encoding='utf-8')
 (base/'stderr.txt').write_text(result.stderr,encoding='utf-8')
 assert result.returncode==0,result.stderr
 assert not result.stderr.strip(),result.stderr
 matches=[]
 for name in OUTPUTS:
  assert (base/name).read_bytes()==(PUBLIC/name).read_bytes(),(n,name)
  matches.append({**binding(base/name,base),'byte_exact_reference':True})
 report=json.loads((dest/'FIGURE-CHECKS.json').read_text(encoding='utf-8'))
 fonts=report['actual_loaded_fonts'];assert len(fonts)==10
 for row in fonts:
  assert hashlib.sha256((dest/row['path']).read_bytes()).hexdigest().upper()==row['sha256']
 svg=ET.fromstring((base/OUTPUTS[1]).read_bytes())
 desc=svg.find("{http://www.w3.org/2000/svg}desc[@id='font-notices']")
 assert desc is not None
 assert desc.text==(dest/'FONT-NOTICE.txt').read_text(encoding='utf-8')
 runs.append({'run':n,'outputs':matches,'actual_font_loads':fonts,
              'stderr_empty':True,'complete_embedded_notice_exact':True})
final={'schema':'portable-to-two-process-exact-reproduction/v1',
       'pass':True,'inputs':[binding(HERE/n,HERE) for n in INPUTS],
       'reference_outputs':[binding(PUBLIC/n,PUBLIC) for n in OUTPUTS],
       'runs':runs,'reference_runtime':report['runtime'],
       'cross_platform_byte_identity_claimed':False}
args.work_dir.mkdir(parents=True,exist_ok=True)
(args.work_dir/'REPRODUCTION-CHECKS.json').write_text(
 json.dumps(final,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pass':True,'fresh_isolated_runs':2,
                  'byte_exact_outputs_each':3,'actual_fonts_each':10}))
