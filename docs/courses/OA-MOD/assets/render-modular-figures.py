"""Render the two original MF diagrams as native-reader PNGs.

The original mathematical drawing scripts and SVGs remain unchanged in
audit/real-coercivity/figures. This wrapper executes exact copies in a temporary
directory and saves their figures at 200 dpi. It changes no coordinates,
constants, labels, sampled formulas or plot limits.

Run: python public/assets/render-modular-figures.py [--output-directory PATH]
Dependencies: matplotlib, numpy.
"""
from pathlib import Path
import argparse,contextlib,hashlib,io,json,runpy,tempfile
ROOT=Path(__file__).resolve().parents[2]
SOURCES=ROOT/'audit/real-coercivity/figures'
FIGURES=[
 ('draw-modular-resolvent.py','modular-resolvent.png'),
 ('draw-analytic-cores-and-shift.py','analytic-cores-and-shift.png'),
]
def sha(b):return hashlib.sha256(b).hexdigest().upper()
def render(output):
 output=Path(output);output.mkdir(parents=True,exist_ok=True);records=[]
 with tempfile.TemporaryDirectory(prefix='oa-mod-native-figures-') as temporary:
  stage=Path(temporary)
  for source,destination in FIGURES:
   code=(SOURCES/source).read_bytes();script=stage/source;script.write_bytes(code)
   with contextlib.redirect_stdout(io.StringIO()):namespace=runpy.run_path(str(script))
   figure=namespace['fig'];target=output/destination
   figure.savefig(target,dpi=200,format='png',metadata={'Software':'OA-MOD original mathematical figure; native PNG rendering'})
   svg=stage/Path(destination).with_suffix('.svg')
   records.append(dict(source=source,source_sha256=sha(code),png=destination,png_sha256=sha(target.read_bytes()),
     generated_svg_sha256=sha(svg.read_bytes()),retained_svg_sha256=sha((SOURCES/svg.name).read_bytes()),
     generated_svg_equals_retained_svg=svg.read_bytes()==(SOURCES/svg.name).read_bytes(),dpi=200))
   namespace['plt'].close(figure)
 return records
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output-directory',type=Path,default=Path(__file__).resolve().parent)
 args=parser.parse_args();print(json.dumps(render(args.output_directory),indent=2))

