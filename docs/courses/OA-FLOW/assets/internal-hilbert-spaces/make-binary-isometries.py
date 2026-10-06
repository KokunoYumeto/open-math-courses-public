"""Reproduce the exact even/odd range diagram. Original drawing and code: CC0-1.0.

Human mathematical source: Takesaki, Theory of Operator Algebras II,
Exercise XI.2.1, printed pp. 348–349. The concrete model and proof are
in OA-FLOW-L130, equations (U-Binary), (U6), and (U-ProductBasis).
Requires Python and matplotlib. Outputs are written alongside this script.
"""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans',
                     'svg.fonttype': 'path', 'font.size': 14})
fig, ax = plt.subplots(figsize=(14, 8), dpi=180)
fig.patch.set_facecolor('#f7f9fc')
ax.set(xlim=(0, 14), ylim=(0, 8))
ax.set_axis_off()
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

def text(x,y,s,size=14,weight='normal',color='#18263b',**kwargs):
    ax.text(x,y,s,fontsize=size,fontweight=weight,color=color,
            ha='center',va='center',**kwargs)

def box(x,y,w,h,label,color,sub=None):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.035,rounding_size=0.10',
                               linewidth=1.8,edgecolor=color,facecolor='white',zorder=3))
    text(x,y+(0.17 if sub else 0),label,18,color=color,zorder=4)
    if sub: text(x,y-0.27,sub,12,zorder=4)

def branch(x1,y1,x2,y2,color):
    ax.plot([x1,x2],[y1,y2],color=color,linewidth=2.0,zorder=1)

blue='#14647c'; violet='#72529d'
text(7,7.46,'One full family, then its products',24,weight='bold')
text(7,6.93,r'$H=\ell^2(\mathbb{N}_0),\qquad ue_n=e_{2n},\quad ve_n=e_{2n+1}$',18)
text(1.55,6.40,'WHOLE SPACE',11,weight='bold')
text(5.05,6.40,'TWO ORTHOGONAL RANGES',11,weight='bold')
text(10.65,6.40,'FOUR ORTHOGONAL PRODUCT RANGES',11,weight='bold')

box(1.55,3.92,2.0,1.0,r'$H$', '#345578', 'all basis vectors')
box(5.0,5.15,2.25,1.02,r'$uH$',blue,r'$\overline{\mathrm{span}}\{e_{2n}:n\geq0\}$')
box(5.0,2.70,2.25,1.02,r'$vH$',violet,r'$\overline{\mathrm{span}}\{e_{2n+1}:n\geq0\}$')
rows=[(5.62,r'$u^2H$',r'$u^2e_n=e_{4n}$',blue,0),
      (4.40,r'$uvH$',r'$uve_n=e_{4n+2}$',blue,2),
      (3.18,r'$vuH$',r'$vue_n=e_{4n+1}$',violet,1),
      (1.96,r'$v^2H$',r'$v^2e_n=e_{4n+3}$',violet,3)]
branch(2.56,3.92,3.83,5.15,blue); branch(2.56,3.92,3.83,2.70,violet)
for y,label,formula,color,residue in rows:
    box(10.55,y,5.65,.96,label+'     '+formula,color)
    branch(6.16,5.15 if color==blue else 2.70,7.68,y,color)

text(7,1.00,r'$uu^*+vv^*=1,\qquad uu^*\ne0,1$',18)
text(7,.50,r'$K=\mathbb{C}u+\mathbb{C}v\ \longrightarrow\ [KK]=\mathrm{span}\{u^2,uv,vu,v^2\}$',17)
text(7,.14,'Each range is infinite dimensional. The branches indicate orthogonal decompositions.',10)

fig.savefig(OUT/'binary-isometries.svg',metadata={'Creator':'Original CC0 mathematical diagram',
            'Description':'Exact even/odd and residue modulo four isometry ranges; see L130 U-Binary and U-ProductBasis.'})
fig.savefig(OUT/'binary-isometries.png',dpi=180,metadata={'Description':'Exact infinite-dimensional range decompositions for L130.'})
plt.close(fig)
data={'ambient_hilbert_space':'ell2(N0)', 'u_en':'e_(2n)', 'v_en':'e_(2n+1)',
      'products':{'u^2':'e_(4n)','uv':'e_(4n+2)','vu':'e_(4n+1)','v^2':'e_(4n+3)'},
      'range_labels_mean':'closed span over all n >= 0',
      'identity':'uu*+vv*=1', 'adjoint_obstruction':'uu* is a nonscalar projection',
      'proof_locators':['U-Binary','U6','U-ProductBasis'],
      'human_source':'Takesaki, Theory of Operator Algebras II, Exercise XI.2.1, pp. 348-349',
      'original_figure_and_code_terms':'CC0-1.0'}
(OUT/'binary-isometries.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
