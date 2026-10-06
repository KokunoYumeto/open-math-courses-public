"""Original exact-coordinate model and imported-proof route for TE-14–17; CC0-1.0."""
from pathlib import Path
import sys
if sys.flags.optimize:raise RuntimeError('Figure validation requires assertions; run Python without -O or -OO')
import argparse,json,hashlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Polygon,FancyBboxPatch
INK='#172438';BLUE='#185aa0';GREEN='#087c68'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
def render(out):
 out.mkdir(parents=True,exist_ok=True);p=out/'affine-fixed-point-model-v003.png';assert not p.exists()
 fig=plt.figure(figsize=(5.2,9.6));fig.suptitle('An exact model and the programme proof',fontsize=14,color=INK,fontweight='bold',y=.98)
 ax=fig.add_axes((.11,.47,.78,.47));ax.set_aspect('equal');ax.set(xlim=(-2.3,2.3),ylim=(-2.3,2.3),xticks=(-2,-1,0,1,2),yticks=(-2,-1,0,1,2));ax.grid(alpha=.16)
 pts=[(1,0),(0,1),(-1,0),(0,-1)]
 ax.add_patch(Polygon(pts,facecolor='#dbeafb',edgecolor=BLUE,lw=2,alpha=.75))
 for pt in pts:ax.add_patch(Circle(pt,1,fill=False,edgecolor=GREEN,lw=1.2,alpha=.7));ax.plot(*pt,'o',color=BLUE,ms=6)
 for pt,shift in [((1,0),(.18,.12)),((0,1),(.16,.15)),((-1,0),(-.78,.12)),((0,-1),(.15,-.32))]:ax.text(pt[0]+shift[0],pt[1]+shift[1],str(pt),fontsize=11,color=INK)
 ax.plot(0,0,'o',color='#a32d33',ms=7,zorder=5);ax.text(-.15,-.35,'u = (0, 0)',ha='right',color='#a32d33',fontsize=11)
 ax.annotate('',xy=(1,0),xytext=(0,0),arrowprops={'arrowstyle':'<->','color':INK,'lw':1.6});ax.text(.50,.15,'r = 1',ha='center',fontsize=11,color=INK)
 ax.annotate('',xy=(1,-1.6),xytext=(-1,-1.6),arrowprops={'arrowstyle':'<->','color':INK,'lw':1.5});ax.text(0,-1.88,'d = 2',ha='center',fontsize=11,color=INK)
 ax.set_xlabel('x');ax.set_ylabel('y');ax.set_title('Four unit disks have only the origin in common',fontsize=11,color=INK,pad=9)
 flow=fig.add_axes((.06,.05,.88,.39));flow.set(xlim=(0,1),ylim=(0,1));flow.axis('off')
 boxes=[(.76,'Exact finite model: average of eight symmetries','A(x) = ⅛ ∑ g(x) = 0: pair g with −g.\nThe origin is fixed by every matrix.'),(.49,'Programme Proposition 4.1: general norm','A fixed point of a positive finite average\nis fixed by every listed isometry.\nSmall-diameter complement forces the conclusion.'),(.22,'Programme Theorem 5.1: arbitrary group','One affine average has a fixed point.\nEvery finite list therefore has a common fixed point.\nClosed fixed sets have the finite-intersection property.')]
 for y,title,body in boxes:
  flow.add_patch(FancyBboxPatch((.02,y),.96,.21,boxstyle='round,pad=.01',facecolor='#f4f8fc',edgecolor=BLUE,lw=1.2));flow.text(.5,y+.18,title,va='top',ha='center',fontsize=10.5,fontweight='bold',color=BLUE);flow.text(.5,y+.12,body,va='top',ha='center',fontsize=10,color=INK,linespacing=1.18)
 for y in (.74,.47):flow.annotate('',xy=(.5,y-.03),xytext=(.5,y+.01),arrowprops={'arrowstyle':'->','lw':1.4,'color':INK})
 flow.text(.5,.10,'The full intersection is nonempty in weakly compact Q.\nNo global separability or countability assumption.',ha='center',va='center',fontsize=10.5,color=GREEN)
 fig.text(.5,.018,'Model: TE-15/17, TE.38–40. Exact imported proof: TE-14.\nProgramme Prop. 4.1/Thm. 5.1; Namioka–Asplund method.',ha='center',va='bottom',fontsize=9,color=INK)
 fig.savefig(p,dpi=200,facecolor='white',metadata={'Software':'OA-MOD original plotting code','Copyright':'CC0-1.0'});plt.close(fig)
 return {'name':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest().upper(),'width':1040,'height':1920}
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--output-directory',type=Path,default=Path(__file__).resolve().parent);args=parser.parse_args();print(json.dumps(render(args.output_directory)))
