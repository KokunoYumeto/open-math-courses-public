"""Original CC0 mathematical figures. Run: python build_figures.py.

All figures follow the exact formulas in CHARACTERISTIC.md and PERIODIC.md.
No source artwork, source page, downloaded font or third-party scene is used.
PNG and SVG are generated directly with matplotlib. See README.md for scope.
"""
from pathlib import Path
import hashlib
import json
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

HERE = Path(__file__).resolve().parent
plt.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 12,
    'axes.spines.top': False, 'axes.spines.right': False,
    'savefig.facecolor': 'white', 'svg.hashsalt': 'oa-flow-original-characteristic-20261007',
})
NAVY = '#17334d'
TEAL = '#087f8c'
ORANGE = '#b95020'
PALE = '#eef5f9'
DATA = {
    'terms': 'CC0-1.0 to the extent of author rights; no external artwork',
    'parameters': {'P': 2, 'T': 'pi', 'lambda': 'exp(-2)', 'R': 1, 'tail_cutoff_K': 10000},
    'scope': 'Exact algebraic objects and proved bounds; floating samples only illustrate formulas.',
}

def save(fig, stem):
    fig.savefig(HERE / (stem+'.png'), dpi=170, bbox_inches='tight',
                metadata={'Software': 'matplotlib; original CC0 formula-based figure'})
    fig.savefig(HERE / (stem+'.svg'), bbox_inches='tight',
                metadata={'Date': None, 'Creator': 'Original CC0 mathematical figure'})
    plt.close(fig)

def node(ax, x, y, label, sub):
    ax.add_patch(FancyBboxPatch((x-.72, y-.29), 1.44, .58,
        boxstyle='round,pad=0.035', facecolor=PALE, edgecolor=NAVY, linewidth=1.5))
    ax.text(x,y+.055,label,ha='center',va='center',fontsize=22,color=NAVY)
    ax.text(x,y-.16,sub,ha='center',va='center',fontsize=10,color=NAVY)

def arrow(ax, start, end, text, tx, ty):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=15,
                               color=NAVY,linewidth=1.4))
    ax.text(tx,ty,text,ha='center',va='center',fontsize=11,color=NAVY,
            bbox=dict(facecolor='white',edgecolor='none',pad=2))

fig, ax=plt.subplots(figsize=(12,8.4))
ax.set(xlim=(-1.15,7.55),ylim=(-.6,5.8)); ax.axis('off')
xs=[0,3.2,6.4]; ys=[4.7,2.7,.7]
labels=[[(r'$A_0$',r'$\mathcal{U}(Z(M))$'),(r'$A$',r'$\mathcal{U}(Z(C))$'),(r'$B$',r'$\delta(A)$')],
        [(r'$U$',r'$\mathcal{U}(M)$'),(r'$E$','core normalizers'),(r'$Z$','continuous cocycles')],
        [(r'$I$','inner automorphisms'),(r'$N$','core-inner restrictions'),(r'$H$',r'$Z/B$')]]
for i,y in enumerate(ys):
    for j,x in enumerate(xs): node(ax,x,y,*labels[i][j])
    arrow(ax,(.8,y),(2.4,y),'inclusion',1.6,y+.14)
for i,txt in enumerate([r'$\delta$; kernel $A_0$',r'$\delta$; kernel $U$',r'$\nu$; kernel $I$']):
    arrow(ax,(4,ys[i]),(5.6,ys[i]),txt,4.8,ys[i]+.14)
for j,x in enumerate(xs):
    arrow(ax,(x,4.36),(x,3.04),'inclusion',x+.36,3.7)
for j,txt in enumerate([r'Ad; kernel $A_0$',r'$q$; kernel $A$',r'quotient; kernel $B$']):
    arrow(ax,(xs[j],2.36),(xs[j],1.04),txt,xs[j]+.45,1.7)
ax.text(3.2,5.57,'The exact characteristic square',ha='center',fontsize=21,color=NAVY)
ax.text(3.2,-.15,'Every row and column is exact, with 1 at both ends.',ha='center',fontsize=13)
ax.text(3.2,-.46,r'$\delta(v)_s=v^*\theta_s(v)$     $q(v)=\mathrm{Ad}(v)|_M$     $\nu(q(v))=[\delta(v)]$',ha='center',fontsize=13)
save(fig,'characteristic-square')

K=10000
N=np.unique(np.geomspace(1,512,100).astype(int))
n=np.arange(1,K+1,dtype=float)
terms=4*np.sin(1/(2*n))**2
tails=np.cumsum(terms[::-1])[::-1]
lo=np.sqrt(tails[N])
hi=np.sqrt(tails[N]+1/K)
bound=1/np.sqrt(N)
defect=2*np.sin(1/(2*N))
DATA['tail_samples']=[{'N':int(a),'finite_sum_sqrt':float(b),'analytic_remainder_upper_sqrt':float(c),'bound':float(d)} for a,b,c,d in zip(N,lo,hi,bound)]
DATA['basis_samples']=[{'n':int(a),'defect_sup_R1':float(b),'quotient_norm':1} for a,b in zip(N,defect)]
fig,axs=plt.subplots(1,2,figsize=(12,5.8))
axs[0].fill_between(N,lo,hi,color=TEAL,alpha=.3,label='finite-sum tail bracket')
axs[0].loglog(N,lo,color=TEAL,linewidth=2)
axs[0].loglog(N,bound,'--',color=ORANGE,label=r'proved upper bound $1/\sqrt{N}$')
axs[0].set(title='Coboundaries approach a non-coboundary',xlabel='truncation N',ylabel='compact-time defect error, R = 1')
axs[0].legend(fontsize=10)
axs[0].text(.03,.08,r'$z(t)_n=e^{it/n}-1$'+'\n'+r'$a^{(N)}=(1,\ldots,1,0,\ldots)$',transform=axs[0].transAxes,fontsize=12)
axs[1].loglog(N,defect,color=TEAL,linewidth=2,label=r'$\sup_{|t|\leq1}\|\gamma_t e_n-e_n\|=2\sin(1/(2n))$')
axs[1].loglog(N,np.ones_like(N),'--',color=ORANGE,label=r'$\|e_n\|_2=1$')
axs[1].set(title='Inherited convergence misses quotient size',xlabel='basis index n',ylabel='norm')
axs[1].legend(fontsize=10,loc='lower left')
fig.suptitle('The topology distinction has an explicit uniform bound',fontsize=18,color=NAVY)
fig.text(.5,.005,'CS14–CS16: abstract Polish-group model. K = 10,000; omitted squared tail ≤ 1/K. No type III₀ realization is asserted.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.045,1,.94)); save(fig,'cocycle-topology')

fig,axs=plt.subplots(1,2,figsize=(12,5.7))
ax=axs[0]; ax.set(xlim=(-2.7,2.7),ylim=(-.7,2.1)); ax.axis('off')
ax.text(0,1.9,'Two densities on equal Hilbert dimensions',ha='center',fontsize=15,color=NAVY)
for r in range(-2,3):
    ax.plot(r,1,'o',color=TEAL,markersize=10)
    ax.text(r,.7,fr'$e^{{{r}}}$',ha='center',fontsize=12)
ax.text(0,1.35,'Atomic: every real r labels an eigenspace',ha='center',fontsize=12)
ax.text(0,.36,'Five labels shown; each eigenspace has infinite multiplicity.',ha='center',fontsize=9)
ax.plot([-2.3,2.3],[-.03,-.03],color=ORANGE,linewidth=12,solid_capstyle='butt',alpha=.65)
ax.text(0,-.4,r'Diffuse: $e^Q$ on $L^2(\mathbb{R})$ has no eigenvectors',ha='center',fontsize=12)
ax=axs[1]; xx=np.linspace(-1,1,401); yy=np.full_like(xx,math.sqrt(2)); yy[200]=np.nan
ax.plot(xx,yy,color=ORANGE,linewidth=2)
ax.plot([0],[math.sqrt(2)],'o',mfc='white',mec=ORANGE,markersize=8)
ax.plot([0],[0],'o',color=TEAL,markersize=8)
ax.set(xlim=(-1.08,1.08),ylim=(-.15,1.8),xticks=[-1,0,1],yticks=[0,math.sqrt(2)],yticklabels=['0',r'$\sqrt{2}$'],xlabel='modular eigenfrequency s',ylabel=r'$\|X(s)\xi-X(0)\xi\|$',title='Every eigenunitary field jumps at zero')
ax.text(.07,.35,r'$\xi$ belongs to the 1-eigenspace.'+'\n'+r'$X(s)\xi$ belongs to the $e^s$-eigenspace.',transform=ax.transAxes,fontsize=12)
fig.suptitle('Pointwise scalar transport does not imply continuous transport',fontsize=18,color=NAVY)
fig.text(.5,.015,'CS24–CS26: nonseparable pointwise-dominant example. The norm plot is exact, not an interpolation.',ha='center',fontsize=11)
fig.tight_layout(rect=(0,.06,1,.92));save(fig,'dominance-boundary')
DATA['dominance_model']={'atomic_labels':'all r in R, each multiplicity aleph_0','shown_labels':[-2,-1,0,1,2],'jump':'0 at s=0; sqrt(2) for every s!=0','diffuse_density':'exp(Q) tensor 1','claim':'No continuous modular eigenunitary field for the atomic weight'}

fig,axs=plt.subplots(1,2,figsize=(12,6.6))
for ax in axs: ax.set_aspect('equal');ax.set(xlim=(-1.65,1.65),ylim=(-1.7,1.7));ax.axis('off')
for ax,title in zip(axs,['Center-flow coordinate q','Modular representative t']):
    ax.add_patch(Circle((0,0),1,fill=False,color=TEAL,linewidth=2))
    for ang in [0,math.pi/2,math.pi,3*math.pi/2]:
        ax.plot([.95*math.cos(ang),1.06*math.cos(ang)],[.95*math.sin(ang),1.06*math.sin(ang)],color=NAVY)
    ax.text(0,1.5,title,ha='center',fontsize=16,color=NAVY)
    ax.add_patch(FancyArrowPatch((math.cos(.6),math.sin(.6)),(math.cos(.2),math.sin(.2)),connectionstyle='arc3,rad=-.1',arrowstyle='-|>',mutation_scale=18,color=ORANGE,linewidth=2))
axs[0].text(0,.23,r'$q\in\mathbb{R}/P\mathbb{Z}$',ha='center',fontsize=17)
axs[0].text(0,-.2,r'$z=e^{iTq}$',ha='center',fontsize=17)
axs[0].text(1.23,0,'0 = P',ha='center',fontsize=11)
axs[0].text(0,-1.28,r'$\theta_s f(q)=f(q-s)$',ha='center',fontsize=13)
axs[1].text(0,.23,r'$t\in\mathbb{R}/T\mathbb{Z}$',ha='center',fontsize=17)
axs[1].text(0,-.2,r'$c_P=e^{-iPt}$',ha='center',fontsize=17)
axs[1].text(1.23,0,'0 = T',ha='center',fontsize=11)
axs[1].text(0,-1.28,r'$\mathrm{Mon}(c)=c_P$',ha='center',fontsize=13)
fig.suptitle(r'One reciprocal relation, two different circles: $PT=2\pi$',fontsize=19,color=NAVY)
fig.text(.5,.075,r'Illustrative exact values: $P=2$, $T=\pi$, $\lambda=e^{-2}$.',ha='center',fontsize=13)
fig.text(.5,.027,r'PS5–PS7, PS20–PS23: crossing one center cell carries $\gamma_1$, since $\theta_P=\gamma_1\otimes\mathrm{id}$.',ha='center',fontsize=11)
fig.tight_layout(rect=(0,.1,1,.93));save(fig,'periodic-monodromy')

fig,axs=plt.subplots(2,1,figsize=(12,7.7))
for ax in axs:ax.axis('off');ax.set(xlim=(-.3,3.5),ylim=(-.8,1.1))
ax=axs[0]
ax.text(1.6,.92,'A real lift records the integer lost by reduction modulo P',ha='center',fontsize=16,color=NAVY)
ax.plot([0,3],[.25,.25],color=NAVY,linewidth=1.5)
for v,label in [(0,'0'),(1,'P'),(2,'2P'),(3,'3P')]:
    ax.plot([v,v],[.18,.32],color=NAVY);ax.text(v,.02,label,ha='center',fontsize=12)
ax.add_patch(FancyArrowPatch((0,.45),(.7,.45),arrowstyle='-|>',mutation_scale=15,color=TEAL,linewidth=2));ax.text(.35,.59,r'$r_0(\alpha)=0.7P$',ha='center',fontsize=12)
ax.add_patch(FancyArrowPatch((.7,.45),(1.5,.45),arrowstyle='-|>',mutation_scale=15,color=ORANGE,linewidth=2));ax.text(1.1,.59,r'$r_0(\beta)=0.8P$',ha='center',fontsize=12)
ax.plot([1.5,.5],[.2,-.23],':',color=ORANGE,linewidth=2)
ax.text(.5,-.4,r'$r_0(\alpha\beta)=0.5P$',ha='center',fontsize=12)
ax.text(2.4,-.28,r'$k(\alpha,\beta)=1$'+'\n'+r'$F_\alpha F_\beta=\gamma_{-1}F_{\alpha\beta}$',ha='center',fontsize=15,color=ORANGE)
ax=axs[1];ax.text(1.6,.94,'Torsion diagnostic: if m(α) = −P/3, then α³ lies in K',ha='center',fontsize=16,color=NAVY)
for i,label in enumerate(['0','−P/3','−2P/3','−P']):
    ax.plot(i,.32,'o',color=TEAL,markersize=7);ax.text(i,.04,label,ha='center',fontsize=12)
    if i<3:ax.add_patch(FancyArrowPatch((i+.05,.32),(i+.95,.32),arrowstyle='-|>',mutation_scale=15,color=TEAL,linewidth=2))
ax.text(1.5,.54,r'three uses of $r=-P/3$',ha='center',fontsize=13)
ax.text(1.5,-.37,r'$F_{\alpha,-P/3}^{\,3}=\gamma_1 F_{\alpha^3,0}$',ha='center',fontsize=21,color=ORANGE)
ax.text(1.5,-.71,'The prescribed K action requires zero carry. Every other lift changes 1 by a multiple of 3.',ha='center',fontsize=11)
fig.suptitle('The obstruction preserves the prescribed zero-modulus action',fontsize=19,color=NAVY)
fig.text(.5,.015,'PS30–PS36: exact relative splitting criterion. The lower panel is conditional, not a claimed factor realization.',ha='center',fontsize=11)
fig.tight_layout(rect=(0,.05,1,.95));save(fig,'periodic-obstruction')
DATA['obstruction_samples']={'carry':{'r_alpha_over_P':'7/10','r_beta_over_P':'4/5','r_product_over_P':'1/2','integer_k':1,'defect':'gamma_-1'},'torsion_test':{'assumption':'m(alpha)=-P/3','lift_over_P':'-1/3','third_power_defect':'gamma_1','scope':'conditional diagnostic'}}
(HERE/'MODEL_DATA.json').write_text(json.dumps(DATA,indent=2)+'\n',encoding='utf-8')
files=[p for p in HERE.iterdir() if p.suffix in ('.png','.svg','.py') or p.name=='MODEL_DATA.json']
manifest={'schema':'OA-FLOW.original-figure-hashes.v1','files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(files)},'proof_locators':{'characteristic-square':'CHARACTERISTIC.md CS1–CS5','cocycle-topology':'CHARACTERISTIC.md CS14–CS16','dominance-boundary':'CHARACTERISTIC.md CS24–CS26','periodic-monodromy':'PERIODIC.md PS5–PS7, PS20–PS23','periodic-obstruction':'PERIODIC.md PS30–PS36'}}
(HERE/'HASHES.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'figures':5,'formats':['png','svg'],'hashes':manifest['files']},indent=2))

