"""Exact annular section and operator-bound schematic for U038 RA2--RA10."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np

OUT=Path(__file__).resolve().parent
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(14,8.1),facecolor='#f8fafc')
ax=fig.add_axes([.055,.19,.37,.64], facecolor='#f8fafc')
ax.set_aspect('equal')
ax.set_xlim(-8.7,8.7); ax.set_ylim(-8.7,8.7)
theta=np.linspace(0,2*np.pi,800)
# Exact annular supports in the original two-coordinate section.
for inner,outer,color,alpha in [(1,4,'#2563eb',.19),(2,8,'#ea580c',.16)]:
    ax.fill(np.r_[outer*np.cos(theta),inner*np.cos(theta[::-1])],
            np.r_[outer*np.sin(theta),inner*np.sin(theta[::-1])],color=color,alpha=alpha,lw=0)
    for r in (inner,outer):
        ax.add_patch(Circle((0,0),r,fill=False,ec=color,lw=1.5,ls='--' if r==inner else '-'))
ax.axhline(0,color='#64748b',lw=.8);ax.axvline(0,color='#64748b',lw=.8)
ax.plot(0,0,'o',color='#0f172a',ms=4)
ax.text(8.35,-.85,r'$w_{x_1}=\varepsilon x_1$',ha='right',va='top',fontsize=12)
ax.text(.55,8.1,r'$w_{\xi_1}=\varepsilon\xi_1$',ha='left',va='center',fontsize=12)
for r,col,yoff in [(1,'#2563eb',-.5),(2,'#ea580c',.4),(4,'#2563eb',-.5),(8,'#ea580c',.4)]:
    ax.text(r+.08,yoff,str(r),color=col,fontsize=12,ha='left',va='bottom' if yoff>0 else 'top',
            bbox=dict(fc='#f8fafc',ec='none',pad=.8,alpha=.9))
ax.set_xticks([]);ax.set_yticks([])
for spine in ax.spines.values():spine.set_visible(False)
fig.text(.055,.90,'Annuli in the original phase space',fontsize=19,weight='bold',color='#0f172a')
fig.text(.055,.855,r'Two-coordinate section: $w=\varepsilon z$, other coordinates zero',fontsize=12,color='#334155')
fig.text(.055,.15,r'$j=1:\ R_1=2,\quad1\leq|w|\leq4$',color='#2563eb',fontsize=13)
fig.text(.055,.105,r'$j=2:\ R_2=4,\quad2\leq|w|\leq8$',color='#c2410c',fontsize=13)
fig.text(.055,.06,'Supports overlap. The proof uses all 2n phase coordinates.',fontsize=11,color='#334155')
bx=fig.add_axes([.48,.08,.48,.79]);bx.axis('off')
def box(y,height,title,formula,sub,color):
    patch=FancyBboxPatch((0,y),1,height,boxstyle='round,pad=.013,rounding_size=.015',
                        fc='white',ec=color,lw=1.4,transform=bx.transAxes)
    bx.add_patch(patch)
    bx.text(.035,y+height-.026,title,transform=bx.transAxes,fontsize=12,weight='bold',color=color,va='top')
    bx.text(.035,y+height-.078,formula,transform=bx.transAxes,fontsize=13,color='#0f172a',va='top')
    if sub:bx.text(.035,y+.010,sub,transform=bx.transAxes,fontsize=10,color='#475569',va='bottom')
box(.79,.18,'Exact original symbol on annulus j (RA3)',
    r'$q_{\varepsilon,j}(z)=A_j u_{\varepsilon,j}(\delta_j z)$',
    r'$A_j=\varepsilon^{2M}R_j^{-2M},\quad\delta_j=\varepsilon/R_j,\quad R_j=2^j$', '#2563eb')
box(.555,.185,'Two actual Hilbert–Schmidt factors (RA5, RA8)',
    r'$q_{\varepsilon,j}^{w}=P_j^{-1}(P_j q_{\varepsilon,j}^{w})$',
    r'$\|P_j^{-1}\|_2\leq C\sqrt{\nu}\,\delta_j^{-n},\quad\|P_jq_{\varepsilon,j}^w\|_2\leq C(2\pi)^{-n/2}QA_j\delta_j^{-n}$', '#0f766e')
bx.text(.02,.50,r'$P_j=(I+\delta_j^2\sum_{r=1}^n(x_r^2+D_r^2))^{(n+1)/2}\otimes I_\nu$',
        fontsize=10,transform=bx.transAxes,color='#0f172a')
box(.295,.16,'Trace norm on each annulus (RA9)',
    r'$\|q_{\varepsilon,j}^{w}\|_1\leq C\sqrt{\nu}(2\pi)^{-n/2}Q\,\varepsilon^{2M-2n}R_j^{2n-2M}$',
    r'Original phase Jacobian: $\delta_j^{-2n}$; original fiber norm remains in $Q$.', '#c2410c')
box(.045,.19,'Exact geometric sum (RA10)',
    r'$\sum_{j=0}^{\infty}R_j^{2n-2M}=\dfrac{1}{1-2^{-2(M-n)}}$',
    r'Converges exactly when $M>n$.  $M\leq n$: the family $h_\varepsilon^M I_\nu$ fails at $\varepsilon=1$.', '#7c3aed')
fig.text(.48,.925,'Every real M > n',fontsize=22,weight='bold',color='#0f172a')
fig.text(.48,.885,'Complete original weights, domains, Fourier factors and matrix fibers',fontsize=11.5,color='#334155')
fig.text(.48,.027,'Complete programme proof: RP1–RP5 and RA1–RA14. No novelty claim.',fontsize=10.5,color='#475569')
name='scaled-remainder-real-exponent-annuli'
for ext in ('png','svg'):
    fig.savefig(OUT/f'{name}.{ext}',dpi=180,facecolor=fig.get_facecolor())
print(OUT/f'{name}.png')
