"""Reproduce the exact two-topology boundary calculation GB1--GB15."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(11.8,6.1))
fig.patch.set_facecolor('white'); ax.set_facecolor('white')
ax.set(xlim=(0,12),ylim=(0,6.2));ax.axis('off')
def box(x,y,w,h,title,body,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',
                              facecolor=color,edgecolor='#334155',linewidth=1.1))
    ax.text(x+w/2,y+h-.28,title,ha='center',va='top',fontsize=13,fontweight='bold')
    ax.text(x+w/2,y+h-.77,body,ha='center',va='top',fontsize=11.5,linespacing=1.65)
ax.text(6,6.02,'The same full defect on two boundary topologies',ha='center',
        fontsize=17,fontweight='bold',color='#0f172a')
box(.3,3.64,4.4,1.84,'Original jets and exact projection',
    r'$P=D_r^2+D_y^2+1,\quad\Lambda=(1+D_y^2)^{1/2}$'+'\n'+
    r'$J=\operatorname{diag}(I,\Lambda^{-1}),\quad (x,y)=V^*JU$'+'\n'+
    r'$V:\quad 2^{-1/2}(1,i)^t,\quad 2^{-1/2}(1,-i)^t$', '#eef2ff')
box(7.3,3.64,4.4,1.84,'All four coefficients retained',
    'A has rows (a, b) and (c, d)'+'\n'+
    r'$Q=C+J^{-1}V\Lambda^{-1}AV^*J$'+'\n'+r'$E=Q^2-Q$', '#eef2ff')
ax.annotate('',xy=(7.06,4.55),xytext=(4.94,4.55),arrowprops=dict(arrowstyle='->',lw=1.5,color='#334155'))
ax.text(6,4.73,'GB4--GB11',ha='center',fontsize=11)
box(.3,.75,5.2,2.1,'Common grade: compact',
    r'$\mathcal{C}^s=H^{s-1/2}\oplus H^{s-3/2}$'+'\n'+
    r'$V^*JEJ^{-1}V=\Lambda^{-1}\operatorname{diag}(a,-d)$'+'\n'+
    r'$+\Lambda^{-2}A^2$'+'\n'+
    'Both full terms gain at least one derivative.  GB11', '#e8f4ed')
box(6.5,.75,5.2,2.1,'Two-derivative split: extra condition',
    r'$\mathcal{M}_2=C\mathcal{C}^0\oplus(I-C)\mathcal{C}^2$'+'\n'+
    r'$\|(x,y)\|^2=2\pi\sum_n(\lambda_n^{-1}|x_n|^2+\lambda_n^3|y_n|^2)$'+'\n'+
    r'$(W_{\mathcal{M}}EW_{\mathcal{M}}^{-1})_{21}=(ca+dc)I$'+'\n'+
    r'Compact exactly when $ca+dc=0$.  GB12--GB13', '#fff0e7')
for x in (2.5,9.5):
    ax.annotate('',xy=(x,3.08),xytext=(x,3.47),arrowprops=dict(arrowstyle='->',lw=1.5,color='#334155'))
ax.text(6,.3,r'For $a=b=c=d=1$: common-grade compactness holds; the split-space lower-left block is $2I$.',
        ha='center',fontsize=11.5,color='#0f172a')
fig.tight_layout(pad=.35)
fig.savefig(out/'graded-boundary-defect-bridge.svg')
fig.savefig(out/'graded-boundary-defect-bridge.png',dpi=170)
plt.close(fig)
