"""Original exact III0 band and state-mass diagram. CC0-1.0."""
from pathlib import Path
import json, hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.hashsalt':'OA-FLOW-Z-20261004','axes.spines.top':False,'axes.spines.right':False})
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
D=Path(__file__).resolve().parent
A=D/'assets'; A.mkdir(exist_ok=True)
blue='#2364a4'; red='#b44242'; green='#287d61'; ink='#183049'
fig=plt.figure(figsize=(15,11),dpi=200,facecolor='#fbfcfe')
gs=fig.add_gridspec(3,2,height_ratios=[1,1.2,1.1],hspace=.67,wspace=.32)
ax=fig.add_subplot(gs[0,:]); ax.set_xlim(-3.2,3.2); ax.set_ylim(-.15,2.2)
ax.set_title('A. Delete the annulus, then flatten the low algebra (schematic; R = 1)',loc='left',fontweight='bold',color=ink)
for y in [.4,1.45]: ax.axhline(y,color='#a7b5c4',lw=1)
for left,right in [(-2,-1),(1,2)]:
    ax.add_patch(Rectangle((left,1.25),right-left,.4,color=red,alpha=.23))
    ax.text((left+right)/2,1.45,'excluded',ha='center',va='center',fontsize=12,color=red)
ax.plot([-1,1],[1.45,1.45],lw=9,color=blue,solid_capstyle='butt')
ax.text(0,1.84,r'$N=(eMe)(\alpha,[-R,R])$',ha='center',color=blue)
for lo,hi in [(-3.1,-2),(2,3.1)]:
    ax.plot([lo,hi],[1.45,1.45],lw=7,color=green,solid_capstyle='butt')
for lo,hi in [(-3.1,-1),(1,3.1)]:
    ax.plot([lo,hi],[.4,.4],lw=7,color=green,solid_capstyle='butt')
ax.scatter([0],[.4],s=100,color=blue,zorder=5)
ax.text(0,.78,r'$\beta_t=\operatorname{Ad}(e^{-itH})\alpha_t$',ha='center',color=ink)
ax.text(0,-.08,r'$\operatorname{Sp}(\beta)\cap(-R,R)=\{0\}$',ha='center',color=ink)
ax.set_yticks([.4,1.45],['corrected\naction','corner\naction']); ax.set_xticks([-2,-1,0,1,2],['−2R','−R','0','R','2R']); ax.spines['left'].set_visible(False); ax.spines['bottom'].set_visible(False)
ax=fig.add_subplot(gs[1,0]); ax.set_title('B. Why the high band cannot enter the gap',loc='left',fontweight='bold',color=ink)
ax.set_xlim(-1.2,1.2);ax.set_ylim(-.3,1.5)
ax.plot([-.5,.5],[1.15,1.15],lw=12,color=blue,solid_capstyle='butt');ax.text(0,1.41,r'$\operatorname{Sp}(H)\subset[-R/2,R/2]$',ha='center')
ax.plot([-1,1],[.3,.3],lw=12,color=green,solid_capstyle='butt');ax.text(0,.58,r'two factors: $[-R/2,R/2]+[-R/2,R/2]$',ha='center',fontsize=12)
ax.text(0,-.12,r'$E\subset(-\infty,-2R]\cup[2R,\infty)$'+'\n'+r'$E+[-R,R]\subset(-\infty,-R]\cup[R,\infty)$',ha='center',fontsize=12)
ax.set_xticks([-1,-.5,0,.5,1],['−R','−R/2','0','R/2','R']);ax.set_yticks([]);ax.spines['left'].set_visible(False);ax.spines['bottom'].set_visible(False)
ax=fig.add_subplot(gs[1,1]);ax.set_title('C. Exact centralizer masses: μ = 1/16',loc='left',fontweight='bold',color=ink)
mass_phi=[4/5,1/5];mass_psi=[1/5,4/5]
x=np.array([0,1]);w=.32
ax.bar(x-w/2,mass_phi,w,color=blue,label=r'$\varphi$');ax.bar(x+w/2,mass_psi,w,color=green,label=r'$\psi=\varphi_m$')
for a,v in zip(x-w/2,mass_phi):ax.text(a,v+.035,'4/5' if v==.8 else '1/5',ha='center')
for a,v in zip(x+w/2,mass_psi):ax.text(a,v+.035,'4/5' if v==.8 else '1/5',ha='center')
ax.set_xticks(x,[r'$p\in Z(M_\varphi)$',r'$1-p$']);ax.set_ylim(0,1.05);ax.set_ylabel('state mass');ax.legend(loc='upper center',ncol=2,fontsize=11,frameon=False)
ax.text(.5,-.28,r'$m=\frac{1}{4}p+4(1-p),\quad\|\varphi-\psi\|=\frac{6}{5}$',transform=ax.transAxes,ha='center',fontsize=13)
ax=fig.add_subplot(gs[2,0]);ax.axis('off');ax.set_title('D. All states stay on the original factor',loc='left',fontweight='bold',color=ink)
lines=[r'$S(M)=\{0,1\}\ \Longrightarrow\ \Gamma(\sigma^\theta)=\{0\}$',r'compact annulus $\Longrightarrow$ nonzero fixed corner $eMe$',r'bounded density $e^{-H}$ $\Longrightarrow$ faithful gap state $\psi$',r'$v^*v=1,\ vv^*=e:\quad\varphi_R(x)=\psi(vxv^*)$',r'$U\Delta_{\varphi_R}U^*=\Delta_\psi$ on full domains']
for i,s in enumerate(lines):ax.text(0,.86-i*.19,s,fontsize=12.5,color=ink)
ax=fig.add_subplot(gs[2,1]);ax.set_title('E. Exact orbit minimum\nfrom the proved GM theorem',loc='left',fontweight='bold',fontsize=12.5,color=ink)
mu=np.geomspace(1e-6,1,300);d=2*(1-np.sqrt(mu))/(1+np.sqrt(mu))
ax.plot(mu,d,color=blue,lw=2.5);ax.axhline(2,color=red,ls='--',lw=1.2);ax.scatter([1/16],[6/5],color=green,zorder=5)
ax.text(.0000018,1.70,r'$2\frac{1-\sqrt{\mu}}{1+\sqrt{\mu}}\ \longrightarrow\ 2$',fontsize=13)
ax.annotate('(1/16, 6/5)',(1/16,6/5),xytext=(.003,.85),arrowprops={'arrowstyle':'->','color':ink},fontsize=11)
ax.set_xscale('log');ax.set_xlim(1e-6,1);ax.set_ylim(0,2.13);ax.set_xlabel('gap parameter μ in the same III₀ factor');ax.set_ylabel('pair norm / orbit minimum');ax.grid(alpha=.15)
fig.suptitle('From the zero Connes intersection to wide modular gaps',fontsize=21,fontweight='bold',color=ink,y=.985)
fig.subplots_adjust(left=.12,right=.96,bottom=.065,top=.915)
fig.savefig(A/'iii0-gap-states.png',dpi=200)
fig.savefig(A/'iii0-gap-states.svg',metadata={'Date':'2026-10-04','Creator':'Original CC0 mathematical reproduction source'})
data={'R':1,'deleted_annulus':[[-2,-1],[1,2]],'implementer_enclosing_band':[-.5,.5],'two_factor_shift':[-1,1],'mu_sample':'1/16','sqrt_mu':'1/4','phi_masses':['4/5','1/5'],'psi_masses':['1/5','4/5'],'pair_norm':'6/5','orbit_equality':'by the complete earlier GM theorem','plot_samples':[[float(m),float(v)] for m,v in zip(mu,d)],'schematic_not_actual_typeIII_spectrum':True}
(A/'iii0-gap-states-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
import matplotlib as mpl
font=Path(mpl.get_data_path())/'fonts/ttf/LICENSE_DEJAVU'
if font.exists():(A/'FONT-LICENSE.txt').write_bytes(font.read_bytes())
print(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in A.iterdir()},indent=2))
