from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-operator-spectral-20261009-v1"
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 13})
fig, ax = plt.subplots(figsize=(12.8, 7.2), dpi=160)
fig.patch.set_facecolor('#f7fafc')
ax.set(xlim=(0, 12.8), ylim=(0, 7.2))
ax.axis('off')
ax.text(.45, 6.8, 'From a unitary orbit to the full spectral domain',
        fontsize=22, weight='bold', color='#18334b')
ax.text(.45, 6.35, 'An exact proof map: no separability restriction on the original Hilbert space',
        fontsize=13, color='#415569')
boxes = [
    (.5, 4.2, 'SB-1  Finite orbit polynomials',
     r'$\|p(U)\|\leq\sup_{|z|=1}|p(z)|$'+'\nContinuous unitary calculus'),
    (6.8, 4.2, 'SB-2  Scalar measure construction',
     r'$L(f)=\int f\,d\mu$'+'\nCompact metric outer measure'),
    (.5, 1.9, 'SB-3  Multiplication model',
     r'$U\cong\bigoplus_j M_z$'+'\nEach vector has countable support'),
    (6.8, 1.9, 'SB-4  Recover the whole graph',
     r'$(B+i)^{-1}=(A+i)^{-1}$'+'\n'+r'$D(B)=D(A),\quad B=A$'),
]
for x,y,title,body in boxes:
    ax.add_patch(FancyBboxPatch((x,y),5.5,1.65,boxstyle='round,pad=0.12',
                 linewidth=1.6,edgecolor='#6488a2',facecolor='white'))
    ax.text(x+.18,y+1.38,title,fontsize=15,weight='bold',color='#18334b',va='top')
    ax.text(x+.18,y+.94,body,fontsize=15,linespacing=1.7,color='#29475e',va='top')
for a,b in [((6.15,5.0),(6.58,5.0)),((3.25,4.0),(3.25,3.8)),
            ((8.2,4.0),(5.7,3.67)),((6.15,2.73),(6.58,2.73))]:
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=20,
                               linewidth=1.8,color='#367c82'))
ax.text(.55,.91,r'$D(f(A))=\{v:\int |f|^2\,d\mu_v^A<\infty\}$',
        fontsize=22,color='#18334b')
ax.text(.55,.35,'SB-5 retains the reducing sum; SB-6 retains spectral-null equivalence and covariance.',
        fontsize=12,color='#415569')
fig.savefig(OUT/'spectral-route.png',bbox_inches='tight',facecolor=fig.get_facecolor())
fig.savefig(OUT/'spectral-route.svg',bbox_inches='tight',facecolor=fig.get_facecolor(),metadata={'Date': None})
print('Rendered spectral-route.png and spectral-route.svg')
