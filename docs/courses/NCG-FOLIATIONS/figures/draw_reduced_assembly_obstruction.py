"""Original CC0 diagram of Theorems11A.1–2, Proposition11A.4, Lemma11A.5 and Theorem11A.6; no source illustration copied."""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

out = Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':14,
                     'mathtext.fontset':'dejavusans', 'svg.hashsalt':'ncg-assembly-obstruction-v1'})
fig = plt.figure(figsize=(14,8.6), facecolor='white')
ax = fig.add_axes([0,0,1,1]); ax.set_xlim(0,14); ax.set_ylim(0,8.6); ax.axis('off')
blue='#165a82'; orange='#b65d16'; gray='#425466'; green='#146d4e'
ax.text(.5,8.1,'Where the native reduced geometric map misses a class',
        fontsize=22,weight='bold',color='#18324b')
ax.text(.5,7.62,r'Compact smooth suspension: $B=S^1\times\mathbb{P}^1(\mathbb{R})$ is a complete transversal',
        fontsize=15,color=gray)

# The upper open arc is U=(a,b); lower closed arc is F=[b,a].
theta=np.linspace(0,math.pi,300); phi=np.linspace(math.pi,2*math.pi,300)
cx,cy,r=2.0,5.7,1.04
ax.plot(cx+r*np.cos(theta),cy+r*np.sin(theta),lw=6,color=orange)
ax.plot(cx+r*np.cos(phi),cy+r*np.sin(phi),lw=6,color=blue)
ax.scatter([cx+r,cx-r],[cy,cy],s=70,color=blue,zorder=5)
ax.text(cx+r+.13,cy,'a',va='center',fontsize=17)
ax.text(cx-r-.25,cy,'b',va='center',fontsize=17)
ax.text(cx,6.95,r'$U=\,]a,b[\,$',ha='center',color=orange,fontsize=18)
ax.text(cx,4.35,r'$F=[b,a]$',ha='center',color=blue,fontsize=18)
ax.text(cx,5.88,'circle coordinate x',ha='center',color=gray,fontsize=12)
ax.text(cx,5.48,'a, b belong to F',ha='center',color=gray,fontsize=12)
ax.text(3.85,6.80,'U: every group word has the identity germ',color=orange,fontsize=14)
ax.text(3.85,6.39,'F: distinct group words retain distinct germs',color=blue,fontsize=14)
ax.text(3.85,5.76,r'$B_r\cong D_r\oplus C([a,b]\times\mathbb{P}^1)$',fontsize=21)
ax.text(3.85,5.17,r'$c=(0,[1])\neq0$',fontsize=22,color=green)
ax.text(7.40,5.20,'Rank-one evaluation detects c.',fontsize=14,color=gray)
ax.text(3.85,4.68,'The closed trivial-action arc becomes an extra reduced summand.',
        fontsize=13,color=gray)

ax.plot([.5,13.5],[3.93,3.93],color='#ced8e2',lw=1)
xs=[2.1,6.8,11.5]; yt=3.27; yb=1.76
upper=[r'$K_0(I)$',r'$K_0(B_m)$',r'$K_0(D_m)$']
lower=[r'$K_0(C)$',r'$K_0(B_r)$',r'$K_0(D_r)$']
for x,lab in zip(xs,upper):ax.text(x,yt,lab,fontsize=22,ha='center',va='center')
for x,lab in zip(xs,lower):ax.text(x,yb,lab,fontsize=22,ha='center',va='center')
def arrow(x0,y0,x1,y1,color=gray):
    ax.add_patch(FancyArrowPatch((x0,y0),(x1,y1),arrowstyle='-|>',
                                mutation_scale=17,lw=1.8,color=color))
for y in [yt,yb]:
    arrow(2.95,y,5.63,y);arrow(7.99,y,10.39,y)
for x in xs:arrow(x,yt-.33,x,yb+.36)
ax.text(2.39,2.49,r'$\iota_*=0$',color=orange,fontsize=17,va='center')
ax.text(7.15,2.49,r'$(\lambda_T)_*$',color=gray,fontsize=17,va='center')
ax.text(11.83,2.56,r'$\lambda_{D,*}$',color=gray,fontsize=16,va='center')
ax.text(11.83,2.24,'injective',color=gray,fontsize=12,va='center')
ax.text(6.75,3.70,'Exact at the middle full group',ha='center',fontsize=12,color=gray)
ax.text(6.75,1.20,'c lies in the reduced restriction kernel, but cannot come from the full group.',
        ha='center',fontsize=14,color=green)
ax.text(.6,.62,r'Native cycles: $\mathrm{im}\,\mu_r\subseteq\mathrm{im}\,(\lambda_H)_*$; $c_H=\Phi_r(c)$ is missed.',
        fontsize=16,color=blue)
ax.text(.6,.19,'Theorems 11A.1–2, Proposition 11A.4, Lemma 11A.5, Theorem 11A.6. Foliation construction: HLS, Section 4.',
        fontsize=10,color=gray)
fig.savefig(out/'reduced-assembly-obstruction.png',dpi=180)
fig.savefig(out/'reduced-assembly-obstruction.svg', metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI), Ultra; original CC0 drawing'})
plt.close(fig)
print('Saved reduced-assembly-obstruction.png and editable SVG')
