"""Reproduce Figure8A; all arrows and groups are proved in BC.1–BC.9."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(13,8))
ax.set(xlim=(0,13),ylim=(0,8));ax.axis('off')
blue='#166b91';green='#27815d';orange='#b85c17';ink='#233647'
def box(x,y,w,h,body,color=blue,size=15):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.13',lw=1.8,edgecolor=color,facecolor='#f7fafc'))
    ax.text(x+w/2,y+h/2,body,ha='center',va='center',fontsize=size,color=ink,linespacing=1.4)
def arrow(x0,y0,x1,y1,label='',dy=.16):
    ax.annotate('',xy=(x1,y1),xytext=(x0,y0),arrowprops=dict(arrowstyle='->',lw=1.7,color=ink))
    if label:ax.text((x0+x1)/2,(y0+y1)/2+dy,label,ha='center',fontsize=13,color=ink)
ax.text(6.5,7.65,'A covariant boundary without a global KK boundary class',ha='center',fontsize=21,color=ink)
box(.35,5.75,3.0,1.05,r'$J=\mathcal{K}(H)$'+'\n'+r'$H=\ell^2(\mathbb{N}_0)$',green)
box(4.8,5.75,3.2,1.05,r'$E=\mathcal{B}(H)\times_{\mathcal{Q}(H)}B$'+'\n'+'Unital, semisplit pullback',green,14)
box(9.4,5.75,3.2,1.05,r'$B\subseteq\mathcal{B}(H\oplus L)$'+'\n'+'Full diagonal corners\nCompact off-diagonal blocks',green,12)
arrow(3.5,6.25,4.6,6.25,r'$j$')
arrow(8.15,6.25,9.2,6.25,r'$\pi$')
ax.text(6.5,5.3,'The ideal, extension algebra and quotient are all sigma-unital.  (BC.1–BC.3)',ha='center',fontsize=13,color=ink)
box(.45,2.9,5.5,1.65,'Countably generated '+r'$J\widehat{\otimes}Cl_1$'+' modules\ngive separable tensor Hilbert spaces.\nTheir source actions of '+r'$B$'+' vanish.\n'+r'$KK_h^1(B,J)=0$',blue,14)
box(7.0,2.9,5.5,1.65,'U = [[S, R], [0, T]]'+'\n'+r'$T=S_0^*\oplus1_W,\quad Rf_0=e_0$'+'\n'+r'$U^*U=UU^*=1,\quad\tau(U)=q_H(S)$',orange,16)
ax.text(3.2,2.55,'Lemmas8A.1–8A.2; faithful tensor test (BC.4)',ha='center',fontsize=11,color=ink)
ax.text(9.75,2.55,'Exact block identities (BC.5–BC.6)',ha='center',fontsize=11,color=ink)
box(.45,.55,5.5,1.25,'Every right product by a global\n'+r'$\partial_\pi\in KK_h^1(B,J)$'+'\nis the zero map.',blue,15)
box(7.0,.55,5.5,1.25,'Actual covariant connecting map:\n'+r'$\delta_1([U])=-[p_{e_0}]=-1\neq0$'+'\n'+r'$K_1(B)\longrightarrow K_0(J)$',orange,16)
arrow(3.2,2.8,3.2,1.97)
arrow(9.75,2.8,9.75,1.97)
ax.text(6.45,1.12,r'$\neq$',ha='center',va='center',fontsize=29,color=ink)
ax.text(6.5,.08,'Theorem8A.3: natural connecting maps survive; a single global boundary class can fail.',ha='center',fontsize=13,color=ink)
fig.savefig(out/'KT-KK-14-global-boundary.png',dpi=180,bbox_inches='tight')
fig.savefig(out/'KT-KK-14-global-boundary.svg',bbox_inches='tight')
plt.close(fig)
