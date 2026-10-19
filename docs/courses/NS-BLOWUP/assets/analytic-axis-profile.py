"""Reproduce the exact analytic-domain and endpoint diagram in N2.3."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'path'})
fig=plt.figure(figsize=(14,10),dpi=100,facecolor='#f6f8fb')
canvas=fig.add_axes([0,0,1,1]);canvas.set_xlim(0,1400);canvas.set_ylim(1000,0);canvas.axis('off')
ink='#152c42';blue='#17639b';orange='#a14e20'
def txt(x,y,s,size=14,color=ink,**kw):canvas.text(x,y,s,va='top',fontsize=size,color=color,**kw)
def box(x,y,w,h,fill='#e6eff7',edge='#bdd0df'):
    canvas.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=12',facecolor=fill,edgecolor=edge))
txt(35,25,'An actual analytic axis solution',24)
txt(35,66,'Coefficient estimates → nonlinear fixed point → Cartesian regularity → endpoint inequality',14)
txt(45,120,'THE JOINT ANALYTIC DOMAIN — J1, EXERCISE 2',14,blue,weight='bold')
ax=fig.add_axes([.09,.52,.35,.28],facecolor='white')
ax.fill([0,1,0],[0,0,1],color='#d7eee8')
ax.plot([0,1],[1,0],'--',color='#157d68',linewidth=2)
ax.plot(.5,.25,'o',color=blue)
ax.annotate(r'$R=10,\ r=\rho/4$',(.5,.25),xytext=(.42,.49),
    arrowprops=dict(arrowstyle='->',color=blue),fontsize=14)
ax.set(xlim=(0,1.04),ylim=(0,1.04),xlabel=r'$R/20$',ylabel=r'$r/\rho$')
ax.set_xticks([0,.5,1]);ax.set_yticks([0,.25,.5,1])
ax.text(.09,.11,r'$\frac{R}{20}+\frac{r}{\rho}<1$',fontsize=19)
txt(45,552,'R is the radius in Y; r here is the parameter-neighborhood radius.',12)
txt(45,583,'The dashed line is excluded. The marked radii are used in Exercise 2.',12)
box(45,624,615,139)
txt(62,640,'The original radial scale is retained',15,blue,weight='bold')
txt(62,678,r'$Y=\Lambda X,\qquad \partial_X^k=\Lambda^k\partial_Y^k$',18)
txt(62,722,r'$0\leq Y\leq4.1,\qquad X_0=4/\Lambda$',16)
txt(715,120,'THE ACTUAL INVERSE AND SOLUTION — J2–J4',14,blue,weight='bold')
box(715,158,640,235)
txt(734,177,r'$\|T^k\|\leq\frac{(40M_\chi)^k}{k!(k+1)!}$',22)
txt(734,234,'The full inverse series converges without requiring small T.',13)
txt(734,270,r'$\Lambda\geq\max(1,M,K),\qquad \mathsf{C}\geq\sup_{\Omega}|\phi_*|$',17)
txt(734,314,'The nonlinear map is a contraction on its actual invariant ball.',13)
txt(734,350,r'$\phi=\phi_*\Phi>0,\qquad U=U_*+\Lambda^{-1}\mathfrak{u}$',17)
txt(715,426,'TWO ENDPOINT REGIONS — J0, J5–J6',14,orange,weight='bold')
box(715,463,640,132,'#fff0e3','#e1c2a9')
txt(734,480,r'$\chi>.99\quad\Longrightarrow\quad p_1>2.3$',20)
txt(734,530,'The exact alternating-series bound controls the angular ratio.',13)
txt(734,561,r'$p_1=-2Y\Phi_Y/\Phi,\qquad Y=4$',15)
box(715,611,640,152,'#fff0e3','#e1c2a9')
txt(734,628,r'$\chi\leq.99\quad\Longrightarrow\quad |Z_*|>\delta_*$',20)
txt(734,678,r'$|p_2|=\mathsf{C}\sqrt{2/\Lambda}\,\frac{|n_s|}{\phi_*\Phi}$',18)
txt(734,728,r'$\mathsf{C}\geq\mathsf{C}_0(\Lambda)\quad\Longrightarrow\quad p_2^2/p_1\geq5/2$',16)
box(45,797,1310,150)
txt(62,814,'Zero leading stress retains a definite higher-order residual — Exercise 5',16,blue,weight='bold')
txt(62,855,r'$\mathcal{R}_\nu(u_\nu,p_\nu)(0,t)\cdot e_z'
    r'=2Aj_0\sqrt{\nu}\,\tau^{-A-2D}'
    r'=\sqrt{\nu}\,\tau^{-A-1}(2Aj_0\tau^{2h})>0$',22)
txt(62,907,'This is the actual leading inner field. Later base coefficients and corrections treat its full residual.',13)
txt(45,971,'Source: OpenAI, Section 4 and Appendix B. Complete derivation: N2.3 J0–J8. No numerical profile is depicted. CC0 figure.',11)
fig.savefig(HERE/'analytic-axis-profile.svg',metadata={'Creator':'GPT-6 Astra (OpenAI)','Title':'Analytic axis solution and endpoint regions'})
fig.savefig(HERE/'analytic-axis-profile.png',dpi=100);plt.close(fig)
p=HERE/'analytic-axis-profile.svg';t=p.read_text(encoding='utf8')
assert 'width="1008pt" height="720pt"' in t
p.write_text(t.replace('width="1008pt" height="720pt"','width="1400" height="1000"'),encoding='utf8')
