"""Exact joint trace diagram for JT1--JT14; no sampled costs or omitted entries."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

out=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':17,'svg.fonttype':'none'})
fig=plt.figure(figsize=(14,8.4),facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,14);ax.set_ylim(0,8.4);ax.axis('off')
ink='#173144';blue='#175b82';pale='#edf5f9'
def box(x,y,w,h):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.10',
                 linewidth=1.1,edgecolor=blue,facecolor=pale))
def line(x,y,text,size=17,ha='center',color=ink):
    ax.text(x,y,text,fontsize=size,ha=ha,va='center',color=color)
line(7,7.92,'All Cauchy jets: the exact extension of smallest norm',24)
line(7,7.48,r'$D_n=-i\partial_n,\quad h=(1+|\eta|^2)^{1/2},\quad s>K+1/2,\quad t\in\mathbb{R}$',19)
box(.55,5.78,4.5,1.1);box(8.95,5.78,4.5,1.1)
line(2.8,6.47,r'$H_{(s,t)}(\mathbb{R}^n;E)$',23)
line(2.8,6.03,r'weights $(h^2+\zeta^2)^s h^{2t}$',17)
line(11.2,6.33,r'$\bigoplus_{k=0}^{K}H^{s+t-k-1/2}(\mathbb{R}^{n-1};E)$',18)
ax.annotate('',xy=(8.75,6.58),xytext=(5.25,6.58),arrowprops={'arrowstyle':'->','lw':1.8,'color':blue})
line(7,6.84,r'$\Gamma_K=(\gamma_0,\ldots,\gamma_K)$',18)
ax.annotate('',xy=(5.25,5.99),xytext=(8.75,5.99),arrowprops={'arrowstyle':'->','lw':1.8,'color':blue})
line(7,5.72,r'$\mathcal{E}_{s,K},\quad\Gamma_K\mathcal{E}_{s,K}=I$',18)
line(7,5.11,r'$G_{bc}=\int_{\mathbb{R}} z^{b+c}(1+z^2)^{-s}\,dz,\quad w_c=h^{-c}\widehat f_c$',20)
line(7,4.58,r'$\min_{\Gamma_K U=f}\|U\|_{(s,t)}^2=2\pi(2\pi)^{-(n-1)}\int h^{2s+2t-1}w^*G^{-1}w\,d\eta$',19)
line(7,4.01,'Worked example: K = 2, s = 3; every matrix entry is retained',19)

def matrix(cx,cy,name,factor,rows):
    line(cx-2.1,cy,name+' '+factor,20)
    left=cx-.63;right=cx+1.56;bottom=cy-.68;top=cy+.68
    ax.plot([left+.11,left,left,left+.11],[top,top,bottom,bottom],color=ink,lw=1.5)
    ax.plot([right-.11,right,right,right-.11],[top,top,bottom,bottom],color=ink,lw=1.5)
    for i,row in enumerate(rows):
        for j,v in enumerate(row):line(cx-.26+.72*j,cy+.43-.43*i,str(v),21)
matrix(3.5,3.04,r'$G_{3,2}=$',r'$\frac{\pi}{8}$',[[3,0,1],[0,1,0],[1,0,3]])
matrix(10.2,3.04,r'$G_{3,2}^{-1}=$',r'$\frac{1}{\pi}$',[[3,0,-1],[0,8,0],[-1,0,3]])
box(.65,.82,6.1,1.25);box(7.25,.82,6.1,1.25)
line(3.7,1.70,r'$w=(\phi,0,\phi):\quad 6+6-2-2=8$',19)
line(3.7,1.15,r'minimum norm squared $=8Q_\phi$',19)
line(10.3,1.70,r'$w=(\phi,0,-\phi):\quad 6+6+2+2=16$',19)
line(10.3,1.15,r'minimum norm squared $=16Q_\phi$',19)
line(7,.41,r'$Q_\phi=(2\pi)^{-(n-1)}\int h^{2t+5}|\phi|^2\,d\eta$; proofs JT3--JT14',16)
for suffix in ['svg','png']:
    fig.savefig(out/('joint-cauchy-jet-extension.'+suffix),dpi=180,facecolor='white')
plt.close(fig)
