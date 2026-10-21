"""Exact module maps, degree intervals and a three-layer coefficient example."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

r=Path(__file__).resolve().parent
plt.rcParams.update({'svg.hashsalt':'GL-DMOD-AP-20261021','font.family':'DejaVu Sans','font.size':13})
fig=plt.figure(figsize=(17,9),facecolor='#f7f9fc')
ax=fig.add_axes([.025,.48,.95,.49]);ax.set_axis_off()
blue,green,orange='#285ca6','#087c83','#b36a14'
def box(x,y,w,h,title,sub):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',ec=blue,fc='white',lw=1.3))
    ax.text(x+w/2,y+h*.65,title,ha='center',va='center',fontsize=17,color=blue)
    ax.text(x+w/2,y+h*.23,sub,ha='center',va='center',fontsize=11,color='#34465b')
ax.text(.5,.97,'Actual supported induced modules and their proper images',ha='center',va='top',fontsize=20,weight='bold')
box(.02,.45,.27,.26,r'$I(F)=F\otimes_{\mathcal{O}_X}\mathcal{D}_X$','Coherent F; ordinary flatness is unnecessary. AP.1–AP.4')
box(.365,.45,.27,.26,r'$F\otimes_{\mathcal{O}_X}T$','Derived transfer cancellation with all module sides. AP.7')
box(.71,.45,.27,.26,r'$Rf_*F\otimes_{\mathcal{O}_Y}\mathcal{D}_Y$','Finite order, proper union and actual right action. AP.8–AP.14')
for x in [.30,.645]:ax.annotate('',(x+.055,.58),(x,.58),arrowprops={'arrowstyle':'->','lw':2,'color':green})
ax.text(.5,.32,r'$0\to L\to I(F_s)\to\cdots\to I(F_0)\to M\to0$',ha='center',fontsize=19,color=blue)
ax.text(.5,.18,'Every coefficient and syzygy stays on the same proper closed support. AP.19–AP.22',ha='center',fontsize=14)
ax.text(.5,.06,'Uniform Spencer and real-manifold bounds precede the finite tail comparison. AP.15–AP.26',ha='center',fontsize=14,color=green)

degree=fig.add_axes([.055,.10,.52,.32]);degree.set_ylim(-.65,2.5);degree.set_xlim(-6.6,2.7)
degree.set_yticks([])
for y,label in [(0,'cone image'),(1,'actual output'),(2,'finite induced complex')]:
    degree.text(-6.35,y-.30,label,ha='left',fontsize=11)
degree.set_xticks(list(range(-6,3)));degree.grid(axis='x',alpha=.18)
degree.spines[['left','top','right']].set_visible(False)
degree.set_xlabel('Cohomological degree; sufficient bounds, with n = 1 and s = 4')
for y,a,b,col in [(2,-4,0,blue),(1,-1,2,green),(0,-6,-3,orange)]:
    degree.plot([a,b],[y,y],color=col,lw=7,solid_capstyle='butt')
    degree.scatter([a,b],[y,y],s=45,color=col,zorder=3)
    degree.text((a+b)/2,y+.19,f'[{a}, {b}]',ha='center',color=col,fontsize=13)
degree.set_title('The two cone degrees vanish at every output degree',fontsize=15,pad=17)
degree.axvline(-2,color='#777777',ls=':',lw=1)

jets=fig.add_axes([.65,.08,.33,.34]);jets.set_axis_off()
jets.text(.5,1,'One support point; three coefficient layers',ha='center',fontsize=15,weight='bold')
jets.text(.5,.84,r'$F=\mathcal{O}_{\mathbf{C}}/(z^3)$',ha='center',fontsize=21,color=blue)
for i,label in enumerate([r'$1$',r'$z$',r'$z^2$']):
    x=.12+i*.27
    jets.add_patch(FancyBboxPatch((x,.52),.20,.20,boxstyle='round,pad=.012',fc='white',ec=blue))
    jets.text(x+.10,.62,label,ha='center',va='center',fontsize=22,color=blue)
jets.text(.5,.38,'These boxes are basis layers, not distinct points.',ha='center',fontsize=11)
jets.text(.5,.22,r'$f_+I(F)=\mathbf{C}[z]/(z^3)$',ha='center',fontsize=20,color=green)
jets.text(.5,.09,'Degree 0; all three layers survive. AP.29–AP.32',ha='center',fontsize=11)
fig.savefig(r/'actual-induced-analytic-proper.png',dpi=180)
fig.savefig(r/'actual-induced-analytic-proper.svg',metadata={'Date':None})
plt.close(fig)
data={'source_proofs':['AP.1--AP.14','AP.15--AP.28','AP.29--AP.32'],
 'module_sides':{'input':'right D_X','transfer':'left D_X, right f^-1 D_Y','output':'right D_Y'},
 'actual_projection':'Rf_* F tensor_(O_Y) D_Y, with the full right action',
 'general_n_bound':['-n','2n'],'segment_length':'s=3n+1',
 'cone_bound':['-4n-2','-n-2'],
 'degree_samples':[{'n':n,'s':3*n+1,'finite_segment':[-3*n-1,0],
  'actual_output':[-n,2*n],'cone':[-4*n-2,-n-2]}for n in range(5)],
 'jet_example':{'m':3,'basis':['1','z','z^2'],'support':'one point','output_degree':0,'dimension':3},
 'diagram_scope':'Exact maps and cohomological intervals. Boxes do not depict a metric fibre.',
 'finite_samples_are_general_proof':False}
(r/'actual-induced-analytic-proper-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
