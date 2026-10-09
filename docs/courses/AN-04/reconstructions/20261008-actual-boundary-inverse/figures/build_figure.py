"""Exact operator directions and BI22 ratio; original figure, CC0-1.0."""
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'svg.fonttype':'path'})
fig,ax=plt.subplots(1,3,figsize=(13,4.4),gridspec_kw={'width_ratios':[1.35,1,1]})
fig.patch.set_facecolor('#f3f6f8')
a=ax[0];a.set_xlim(0,1);a.set_ylim(0,1);a.axis('off');a.set_title('The actual graph conjugation')
for x,y,t in [(0.16,0.8,r'$v$ on $W$'),(0.84,0.8,r'$N_+v$ on $W$'),(0.16,0.2,r'$f=Jv$ on $Y$'),(0.84,0.2,r'$\mathcal{B}_+f$ on $Y$')]:a.text(x,y,t,ha='center',va='center',bbox={'boxstyle':'round,pad=.4','facecolor':'white','edgecolor':'#146575'})
for x0,y0,x1,y1,label in [(0.31,.8,.66,.8,r'$N_+$'),(.31,.2,.66,.2,r'$\mathcal{B}_+$'),(.16,.67,.16,.33,r'$J$'),(.84,.67,.84,.33,r'$J$')]:
 a.annotate('',(x1,y1),(x0,y0),arrowprops={'arrowstyle':'->','color':'#146575','lw':2})
 a.text((x0+x1)/2+.04,(y0+y1)/2+.05,label,ha='center')
a.text(.5,.04,r'$L\equiv J^{-1},\quad \mathcal{Q}=JQL$',ha='center')
a=ax[1];a.bar([0,1],[2/3,0],color=['#146575','#b26632'],width=.55);a.scatter([1],[0],color='#b26632',s=80,zorder=3);a.set_xticks([0,1],['Inverse Q','Reflection']);a.set_ylim(-.08,.85);a.set_yticks([0,1/3,2/3],['0','1/3','2/3']);a.set_ylabel('Proved Sobolev gain');a.set_title('Boundary estimates');a.grid(axis='y',alpha=.2);a.text(0,.7,'2/3',ha='center');a.text(1,.06,'0',ha='center')
a=ax[2];lam=np.geomspace(1,4096,180);ratio=.25*lam**(2/3);a.loglog(lam,ratio,color='#b26632',lw=2);a.set_xlabel(r'$\lambda$');a.set_ylabel(r'$\varepsilon\lambda^{2/3}$');a.set_title('Candidate pullback: BI22');a.grid(which='both',alpha=.2);a.text(.05,.92,r'$\varepsilon=1/4$',transform=a.transAxes)
fig.suptitle('Boundary inversion and its coordinate bounds',fontsize=16,y=1.01)
fig.tight_layout();out=P/'actual-boundary-inverse.svg';fig.savefig(out,bbox_inches='tight');plt.close(fig)
record={'svg':'figures/'+out.name,'svg_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'coordinates':'BI9/BI12 graph directions; B4–B6 gains 2/3 and 0; BI22 ratio epsilon*lambda^(2/3), epsilon=1/4, 1<=lambda<=4096.','actually_inspected':False,'exact_coordinate_review_complete':False}
(P.parent/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8');print(json.dumps(record))
