"""Original, deterministic mathematical diagram; expression dedicated CC0-1.0."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.hashsalt':'oa-flow-ccm-20261004','mathtext.fontset':'dejavusans'})
fig = plt.figure(figsize=(17,12),dpi=200,facecolor='#f8fafc')
fig.text(.045,.97,'The full crossed-product commutant',fontsize=29,fontweight='bold',color='#15243c')
fig.text(.045,.938,'Arbitrary locally compact group; arbitrary Hilbert space; both inclusions are proved.',fontsize=17,color='#46566a')
blue,red,green='#1464b0','#bb3d47','#1c806e'

def panel(rect,title):
 ax=fig.add_axes(rect);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
 ax.add_patch(FancyBboxPatch((.005,.005),.99,.99,boxstyle='round,pad=0.005,rounding_size=0.02',facecolor='white',edgecolor='#ccd6e2',lw=1.3))
 ax.text(.045,.935,title,fontsize=20,fontweight='bold',color='#15243c',va='center');return ax
def arrow(ax,a,b,c=blue): ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=15,lw=2.1,color=c))

a=panel([.035,.535,.455,.38],'1  The exact left and right generators')
rows=[(.78,r'$\pi(x)\xi(t)=\alpha_{t^{-1}}(x)\xi(t)$',blue),(.65,r'$\lambda_s\xi(t)=\xi(s^{-1}t)$',blue),(.47,r'$b(y)\xi(t)=y\xi(t),\quad y\in M^{\prime}$',red),(.34,r'$\rho_s\xi(t)=\Delta(s)^{1/2}U_s\xi(ts)$',red)]
for y,t,c in rows:a.text(.055,y,t,fontsize=19,color=c)
a.text(.055,.18,r'$R=\{\pi(M),\lambda(G)\}^{\prime\prime}$',fontsize=19,color=blue)
a.text(.055,.065,r'$R^{\prime}=\{b(M^{\prime}),\rho(G)\}^{\prime\prime}$',fontsize=19,color=red)
a.text(.79,.58,'commute',ha='right',fontsize=14,color=green)
arrow(a,(.84,.72),(.84,.41),green)

b=panel([.51,.535,.455,.38],'2  Exact four-coordinate example')
b.text(.045,.82,r'$G=\mathbb{Z}/2\mathbb{Z},\quad H=\mathbb{C}^2,\quad M=$ diagonal',fontsize=17,color='#46566a')
xs=[.18,.78];ys=[.60,.30]
coords={1:(xs[0],ys[0]),2:(xs[1],ys[0]),3:(xs[0],ys[1]),4:(xs[1],ys[1])}
for i,(x,y) in coords.items():
 b.scatter([x],[y],s=950,c=blue if i in [1,4] else '#80b7df',edgecolors='white',linewidths=2,zorder=4)
 b.text(x,y,str(i),color='white',fontsize=20,fontweight='bold',ha='center',va='center',zorder=5)
 label_x=x+(-.08 if i==3 else .08 if i==4 else 0)
 label_y=y+(.08 if i in [1,2] else 0)
 b.text(label_x,label_y,('a' if i in [1,4] else 'b'),color=blue,fontsize=19,ha='center',va='center' if i in [3,4] else 'baseline')
for i,j in [(1,3),(2,4)]:b.add_patch(FancyArrowPatch(coords[i],coords[j],arrowstyle='<->',mutation_scale=15,shrinkA=17,shrinkB=17,lw=2.1,color=blue))
for i,j in [(1,4),(2,3)]:b.add_patch(FancyArrowPatch(coords[i],coords[j],arrowstyle='<->',mutation_scale=15,shrinkA=17,shrinkB=17,lw=2.1,color=red))
b.text(.045,.44,r'$\lambda_1$',color=blue,fontsize=18)
b.text(.52,.37,r'$\rho_1$',color=red,fontsize=18)
b.text(.045,.14,r'$\pi(a,b)=\mathrm{diag}(a,b,b,a)$',fontsize=17,color=blue)
b.text(.045,.045,r'$b(c,d)=\mathrm{diag}(c,d,c,d);\quad \dim R=\dim R^{\prime}=4$',fontsize=16,color=red)

c=panel([.035,.065,.455,.43],'3  The reverse inclusion: a bounded projection')
c.text(.05,.79,r'$P=P^*=P^2,\quad$ blocks: $p,r,r^*,q$',fontsize=22,color='#15243c')
c.text(.05,.66,r'$p(1-p)=rr^*,\quad q(1-q)=r^*r$',fontsize=18,color=blue)
c.text(.05,.52,r'$\|r^*\zeta_1\|^2=-k\|r\zeta_2\|^2,\quad k>0$',fontsize=19,color=red)
arrow(c,(.49,.465),(.49,.385),green)
c.text(.05,.33,r'$r^*\zeta_1=0,\quad r\zeta_2=0$',fontsize=20,color=green)
c.text(.05,.21,'Full ideal identities force the two orthogonal',fontsize=16,color='#46566a')
c.text(.05,.15,'test vectors to vanish on both map ranges.',fontsize=16,color='#46566a')
c.text(.05,.06,'CCM2 + compact paired density + CCM3 give '+r'$R^{\prime}=Q$.',fontsize=16,color='#15243c')

d=panel([.51,.065,.455,.43],'4  Compact inversion pairs')
d.text(.045,.82,r'$K=[-1,1],\quad V=(-2.1,2.1),\quad t^{-1}=-t$',fontsize=17,color='#46566a')
plot=fig.add_axes([.56,.22,.36,.16]);plot.set_facecolor('white')
t=np.linspace(-2.2,2.2,881);w=np.maximum(0,np.minimum(1,2-np.abs(t)));g1=w*(2-t)/4;g2=w*(2+t)/4
plot.axvspan(-1,1,color='#dfe8f3',alpha=.6);plot.plot(t,g1,color=blue,lw=2.4,label=r'$g_1(t)$');plot.plot(t,g2,color=red,lw=2.4,label=r'$g_2(t)=g_1(-t)$');plot.plot(t,w,color=green,lw=2,ls='--',label=r'$g_1+g_2=w$')
plot.set_xlim(-2.2,2.2);plot.set_ylim(-.035,1.1);plot.set_xticks([-2,-1,0,1,2]);plot.set_yticks([0,.5,1]);plot.tick_params(labelsize=13);plot.legend(loc='upper right',fontsize=12,framealpha=.95)
plot.spines[['top','right']].set_visible(False)
d.text(.045,.23,r'$\Xi(t)=\sum_j[g_j(t)\Psi_j(t)+g_j(t^{-1})X_j(t^{-1})]$',fontsize=15,color='#15243c')
d.text(.045,.14,r'$\|2\Phi-\Xi\|_2\leq6\varepsilon\mu(V)^{1/2}$',fontsize=18,color=green)
d.text(.045,.055,'General CCM6 uses finite covers; the plotted cutoffs are only on '+r'$\mathbb{R}$.',fontsize=14,color='#46566a')

fig.text(.04,.025,'CCM1–8: full proof and exact domains accompany this diagram.  Original CC0 illustration; 3400 × 2400 pixels.',fontsize=14,color='#526176')
fig.savefig(ASSETS/'crossed-product-commutant.png',dpi=200,metadata={'Software':'OA-FLOW original reproducible diagram'})
fig.savefig(ASSETS/'crossed-product-commutant.svg',metadata={'Date':None,'Creator':'OA-FLOW original reproducible diagram'})
plt.close(fig)
data={'finite_example':{'group':'Z/2Z','coordinate_order':['t=0,e1','t=0,e2','t=1,e1','t=1,e2'],'pi_diagonal':['a','b','b','a'],'b_diagonal':['c','d','c','d'],'lambda_permutation':[3,4,1,2],'rho_permutation':[4,3,2,1],'left_complex_dimension':4,'right_complex_dimension':4},'cutoffs':{'group':'R additive','K':[-1,1],'V':[-2.1,2.1],'w':'max(0,min(1,2-|t|))','g1':'w(t)(2-t)/4','g2':'w(t)(2+t)/4','t':t.tolist(),'g1_values':g1.tolist(),'g2_values':g2.tolist(),'w_values':w.tolist()},'general_bound':'||2 Phi-Xi||_2 <= 6 epsilon sqrt(mu(V))','projection_identity':'||r* zeta1||^2 = -k ||r zeta2||^2, k>0','native_pixels':[3400,2400],'license':'CC0-1.0 to the extent of rights held'}
(ASSETS/'crossed-product-commutant-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('Rendered original PNG, SVG and exact data.')
