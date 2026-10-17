"""Exact contact-node geometry and the general support-purity degree mechanism."""
from pathlib import Path
import argparse
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path);args=parser.parse_args()
out=args.output_dir.resolve() if args.output_dir else Path(__file__).resolve().parent
out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'mathtext.fontset':'dejavusans','svg.hashsalt':'holonomic-support-purity-PG-v1'})
fig=plt.figure(figsize=(16,8),dpi=140,facecolor='#fafbfd')
ax=fig.add_axes([.055,.24,.34,.59]);ax.set_aspect('equal')
ax.axhline(0,color='#25658c',linewidth=3);ax.axvline(0,color='#a14737',linewidth=3)
ax.scatter([0],[0],s=180,facecolor='#fafbfd',edgecolor='#202f45',linewidth=2.2,zorder=5)
ax.set_xlim(-1.1,1.1);ax.set_ylim(-1.1,1.1);ax.set_xlabel(r'$x$ (real slice)');ax.set_ylabel(r'$z$ (real slice)')
ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.grid(alpha=.2)
ax.text(.48,.09,r'$z=0$',color='#25658c',fontsize=15);ax.text(.07,.65,r'$x=0$',color='#a14737',fontsize=15)
ax.annotate(r'$W=\{0\}$',xy=(0,0),xytext=(-1.02,-.55),arrowprops={'arrowstyle':'->'},fontsize=15)
fig.text(.055,.93,'Support purity for full infinite-order sections',fontsize=24,weight='bold',color='#163d5a')
fig.text(.055,.865,r'Exact complex geometry: $Y=\{t=0,\ xz=0\}\subset\mathbf{C}^3$,  $\alpha=dt+z\,dx$',fontsize=16)
fig.text(.055,.16,r'Real $t=0$ slice of two complex Legendrian branches.',fontsize=13)
fig.text(.055,.115,r'$n=2$,  $\dim Y=1$,  $\mathrm{codim}\,W=3$,  $c-n=1$.',fontsize=14)
right=fig.add_axes([.45,.22,.51,.61]);right.set_xlim(0,1);right.set_ylim(0,1);right.axis('off')
def box(y,h,title,lines,face):
 right.add_patch(FancyBboxPatch((.01,y),.97,h,boxstyle='round,pad=.015',facecolor=face,edgecolor='#71859a'))
 right.text(.04,y+h-.045,title,fontsize=15,weight='bold',va='top',color='#163d5a')
 right.text(.04,y+h-.13,lines,fontsize=15,va='top',linespacing=1.7)
box(.69,.29,'Actual finite duality · PG.3',r'$N=\mathrm{Ext}^{n}_{E}(M,E)$,  $R^{-p}$: $0\leq p\leq n$'+'\n'+r'$M^\infty\simeq\mathrm{Hom}_{E^{op}}(R,B)[n]$', '#edf4fb')
box(.33,.29,'Actual support and finite Hom · PG.4',r'$C_Z=R\Gamma_Z B$,  $H^q(C_Z)=0$ for $q<c$'+'\n'+r'$R\Gamma_ZM^\infty\simeq\mathrm{Hom}_{E^{op}}(R,C_Z)[n]$', '#f0f7f2')
box(.01,.30,'Every surviving total degree · PG.5',r'$p+q-n\geq c-n$'+'\n'+r'$c>n\quad\Longrightarrow\quad H_Z^0(M^\infty)=0$', '#fff5e8')
fig.text(.055,.045,'Proof: Section 5.51, PG.1–PG.2. Geometry is a stated slice; the degree argument includes every coefficient and every resolution column.',fontsize=11)
fig.savefig(out/'holonomic-support-purity.png',facecolor=fig.get_facecolor())
fig.savefig(out/'holonomic-support-purity.svg',facecolor=fig.get_facecolor(),metadata={'Date':None,'Creator':'Open mathematics course proof diagram'})
plt.close(fig)
data={'proof_locators':['PG.1','PG.2','PG.3','PG.4','PG.5','PG.6'],'complex_coordinates':['t','x','z'],'complex_support_equations':['t=0','x*z=0'],'exceptional_set':['t=0','x=0','z=0'],'displayed_real_slice':'t=0; x,z real','contact_form':'dt+z dx','illustrative_base_dimension':2,'normalized_ambient_dimension':3,'support_complex_dimension':1,'exceptional_codimension':3,'shifted_lower_bound':1,'general_bound':'p+q-n >= c-n; 0<=p<=n; q>=c','real_module_injection_proved':False,'full_I23_I24_proved':False}
(out/'holonomic-support-purity-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('Exact support-purity geometry and degree diagram generated.')
