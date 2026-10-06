from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

W=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(13,7.2),dpi=160)
fig.patch.set_facecolor('white');ax.set_xlim(0,13);ax.set_ylim(0,7.2);ax.axis('off')
blue='#224d74';green='#176754';ink='#152b3c'
def box(x,y,w,h,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.15',linewidth=1.6,edgecolor=color,facecolor='#f5f9fc'))
def label(x,y,s,size=18,color=ink):
    ax.text(x,y,s,ha='center',va='center',fontsize=size,color=color)
label(6.5,6.8,'Two factor pairs determine one global change of frame',23)
box(.5,4.1,5.4,1.9,blue);box(7.1,4.1,5.4,1.9,green)
label(3.2,5.65,r'$U$',24,blue)
label(9.8,5.65,r'$V=\mathbb{R}^{\nu}\backslash K$',24,green)
label(3.2,4.8,r'$G_U=A_0^{-1}\widehat A_0$',24,blue)
label(9.8,4.8,r'$G_V=A_{\infty}^{-1}\widehat A_{\infty}$',24,green)
label(6.5,3.6,r'On $U\backslash K$:  $(aA_0)^{-1}(a\widehat A_0)=A_0^{-1}\widehat A_0$',20)
box(2.5,1.2,8,1.8,ink)
label(6.5,2.65,r'$G:\mathbb{R}^{\nu}\longrightarrow\mathrm{GL}(N,\mathbb{C})$',23)
label(6.5,2.1,r'$\widehat A_0=A_0G|_U,\qquad\widehat A_{\infty}=A_{\infty}G|_V$',23)
label(6.5,1.57,r'$G(x)=G(Sx/|x|)$ for $|x|\geq S$',19)
for start,end,color in [((2.4,4.04),(4,3.02),blue),((10.6,4.04),(9,3.02),green)]:
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=20,linewidth=1.8,color=color))
label(6.5,.58,'MG1–MG4: the quotients agree on the whole overlap and glue over U ∪ V.',15)
label(6.5,.19,'This is the proved choice map for M1–M4.',13)
fig.savefig(W/'matrix-extension-choice-map.png',bbox_inches='tight',pad_inches=.12)
fig.savefig(W/'matrix-extension-choice-map.svg',bbox_inches='tight',pad_inches=.12)
plt.close(fig)
print('Exact choice-map diagram saved as PNG and SVG with reproducible source.')
