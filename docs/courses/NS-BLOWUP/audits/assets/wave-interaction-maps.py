"""Exact interaction-map diagram. Proofs: wave-interaction-audit.md, W2, W4-W7.

Source: OpenAI, Finite Time Blowup for Navier-Stokes, (7.39), Lemma 9.2.
This is a schematic of algebraic maps and estimates, with no sampled flow data.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

out=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(12.8,8.5),dpi=150)
fig.patch.set_facecolor('#f7fafc'); ax.set_facecolor('#f7fafc')
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(.035,.97,'Exact nonlinear interaction maps',fontsize=21,weight='bold',va='top',color='#132f4c')
ax.text(.035,.915,'Cylindrical components; full velocities and cutoff terms retained',fontsize=12,color='#42566b')

def box(x,y,w,h,face):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012,rounding_size=0.012',
                               facecolor=face,edgecolor='#aab9c7',linewidth=1.2))
def arrow(x1,y1,x2,y2):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops={'arrowstyle':'->','lw':2,'color':'#234e70'})

box(.035,.58,.36,.27,'#e8f2fc');box(.62,.58,.345,.27,'#eaf5ee')
ax.text(.055,.815,'Mean increment + one wave',weight='bold',fontsize=14)
ax.text(.055,.760,r'$d=(\delta\beta,\delta v,\delta\gamma)$',fontsize=17)
ax.text(.055,.710,r'$\delta\beta\in\mathsf{M}_{\mu+1},\quad\delta v,\delta\gamma\in\mathsf{M}_{\mu}$',fontsize=14)
ax.text(.055,.653,r'$w=a\,e^{ikm\Phi},\quad a\in\mathsf{W}_{\alpha}$',fontsize=15)
arrow(.41,.72,.605,.72)
ax.text(.51,.778,r'$\mathcal{B}(d,w)+\mathcal{B}(w,d)$',ha='center',fontsize=12)
ax.text(.64,.812,'Same label and harmonic',weight='bold',fontsize=14)
ax.text(.64,.749,r'$\mathcal{Q}_m(d,a)\in\mathsf{W}_{\alpha+\mu-1/2}$',fontsize=17)
ax.text(.64,.693,'Wave support and envelope retained',fontsize=11)
ax.text(.64,.642,'Cylindrical angular mean = 0',fontsize=12)
ax.text(.055,.598,'Full formula: W5.1; receiver: W7.3',fontsize=10,color='#42566b')

box(.035,.18,.36,.28,'#e8f2fc');box(.62,.18,.345,.28,'#eaf5ee')
ax.text(.055,.422,'Two waves with the same label',weight='bold',fontsize=14)
ax.text(.055,.368,r'$a\in\mathsf{W}_{\alpha},\quad b\in\mathsf{W}_{\alpha^\prime}$',fontsize=16)
ax.text(.055,.314,r'$ikm\,n\!\cdot\!a=-[(D_r+R^{-1})a_r+D_za_z]$',fontsize=12)
ax.text(.055,.263,'Exact divergence removes the phase loss',fontsize=11)
ax.text(.055,.211,r'$m,m^\prime\ne0;\quad\mathcal{B}(w,w^\prime)$',fontsize=13)
arrow(.41,.32,.605,.32)
ax.text(.51,.378,'Full coefficient: W6.2',ha='center',fontsize=12)
ax.text(.64,.423,'Output harmonic',weight='bold',fontsize=14)
ax.text(.64,.365,r'$m+m^\prime\ne0:\quad\mathsf{W}_{\alpha+\alpha^\prime-\kappa_s}$',fontsize=15)
ax.text(.64,.302,r'$m+m^\prime=0:\quad\mathsf{M}_{\alpha+\alpha^\prime-\kappa_s}$',fontsize=15)
ax.text(.64,.239,'Mean output uses actual cut fields',fontsize=11)
ax.text(.64,.201,r'$\kappa_s=10^{-5}$',fontsize=12)

ax.text(.035,.119,'Different labels: disjoint closed supports give zero products, including all derivatives (W2).',fontsize=11)
ax.text(.035,.077,'These maps check parts of the iteration. The whole blowup theorem remains unverified.',fontsize=11,color='#7c3f21')
ax.text(.035,.035,'Source: OpenAI, Finite Time Blowup for Navier-Stokes, (7.39), Lemma 9.2. Proof note: W2, W4-W7.',fontsize=9,color='#42566b')
fig.subplots_adjust(left=.015,right=.985,top=.985,bottom=.015)
fig.savefig(out/'wave-interaction-maps.png',dpi=150)
fig.savefig(out/'wave-interaction-maps.svg')
plt.close(fig)
print(out/'wave-interaction-maps.png')
