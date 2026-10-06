from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
from matplotlib import font_manager

ROOT=Path(__file__).resolve().parent
DATA={'group':'R x Z','subgroup':'R x {0}','displayed_cosets':[-2,-1,0,1,2],'horizontal_window':[-3,3],'corner_indices':[-1,0,1],'formula':'(Ind_H^G N) rtimes G = (N rtimes H) bar_tensor B(l2(G/H))','finite_compression_only':True}
(ROOT/'data.json').write_text(json.dumps(DATA,indent=2)+'\n',encoding='utf-8')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.hashsalt':'oa-flow-open-cosets','savefig.facecolor':'white'})
fig,(left,right)=plt.subplots(1,2,figsize=(15,7),gridspec_kw={'width_ratios':[1.15,1]})
fig.suptitle('An open subgroup keeps a full regular corner',fontsize=23,y=.97)
for n in DATA['displayed_cosets']:
    color='#006d77' if n==0 else '#627c93'
    left.plot([-3,3],[n,n],color=color,lw=4 if n==0 else 2)
    left.text(-3.08,n+.14,rf'$H$' if n==0 else rf'$\mathbb{{R}}\times\{{{n}\}}$',fontsize=14,va='bottom')
    left.plot([3.0],[n],marker='>',color=color)
    left.plot([-3.0],[n],marker='<',color=color)
for x,n,label in [(-.6,2,r'$v_2$'),(.8,-1,r'$v_{-1}$')]:
    left.add_patch(FancyArrowPatch((x,0),(x,n),arrowstyle='-|>',mutation_scale=22,color='#cb542c',lw=2.4))
    left.text(x+.15,n/2,label,color='#aa3f1e',fontsize=19)
left.set(xlim=(-3.8,3.4),ylim=(-2.7,2.8),xlabel=r'real coordinate $x$')
left.set_yticks([-2,-1,0,1,2]);left.set_ylabel(r'discrete coordinate $n$')
left.set_title(r'$G=\mathbb{R}\times\mathbb{Z}$,  $H=\mathbb{R}\times\{0\}$',pad=18)
left.spines[['top','right']].set_visible(False)
left.text(.5,-.20,'Only five cosets are shown.\nEach line is open in the product topology.',transform=left.transAxes,ha='center',fontsize=13)
right.set_xlim(0,6);right.set_ylim(0,6.5);right.axis('off')
right.text(3,6.05,r'$Q=p_HPp_H\cong N\rtimes_\beta\mathbb{R}$',ha='center',fontsize=21)
right.text(3,5.45,r'Each entry belongs to $Q$',ha='center',fontsize=15)
indices=[-1,0,1];x0=1.2;y0=1.55;size=1.2
for row,i in enumerate(indices):
    for col,j in enumerate(indices):
        x=x0+col*size;y=y0+(2-row)*size
        right.add_patch(Rectangle((x,y),size,size,facecolor='#eef5f5' if i==j else '#f6f8fa',edgecolor='#6e8595',lw=1.5))
        right.text(x+size/2,y+size/2,rf'$q_{{{i},{j}}}$',ha='center',va='center',fontsize=19)
right.text(3,.95,r'$U^*PU=B(\ell^2\mathbb{Z})\,\bar\otimes\,Q$',ha='center',fontsize=21)
right.text(3,.25,'The array is a finite compression.\nThe whole algebra uses every finite set of indices.',ha='center',fontsize=13)
fig.subplots_adjust(top=.84,bottom=.20,left=.08,right=.98,wspace=.18)
fig.savefig(ROOT/'open-cosets.png',dpi=200)
fig.savefig(ROOT/'open-cosets.svg',metadata={'Date':None,'Creator':'OA-FLOW course project'})
font=Path(font_manager.findfont('DejaVu Sans'))
lic=font.parent/'LICENSE_DEJAVU'
if lic.exists():(ROOT/'FONT-LICENSE.txt').write_bytes(lic.read_bytes())
else:
    candidates=list(Path(matplotlib.get_data_path()).rglob('*LICENSE*'))
    found=next((p for p in candidates if 'DEJAVU' in p.name.upper()),None)
    if found:(ROOT/'FONT-LICENSE.txt').write_bytes(found.read_bytes())
print(ROOT/'open-cosets.png')

