"""Reproduce the two locally proved mechanisms of Theorem1.2C."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from PIL import Image
root=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13})
fig,ax=plt.subplots(figsize=(5,16),dpi=180)
ax.set(xlim=(0,5),ylim=(0,16));ax.axis('off')
ax.text(2.5,15.55,'Ramified tensors and\nsemistable logarithm',ha='center',va='center',fontsize=19,weight='bold')
ax.text(2.5,14.87,'Every finite K; every prime, including p = 2',ha='center',fontsize=11)
boxes=[
 (13.92,r'$\psi:C=A_{\rm cris}\ \to\ \mathcal{B}_s$',r'$r=\sqrt{2},\ s=r/p;\quad\iota_s\psi=j\varphi$','Complete quotient bound; PE11–PE14','#edf4ff'),
 (12.22,r'$\alpha=\Phi^{-1}\psi:C\hookrightarrow\mathcal{B}_r$',r'$\nu(F^\times)\subset\mathbf{Z}+\sqrt{2}\mathbf{Q}$',r'$F={\rm Frac}(C);\quad\nu(F^\times)\cap\mathbf{Q}\subset\mathbf{Z}$'+'; PE15–PE16','#edf4ff'),
 (10.52,'Eisenstein polynomial stays irreducible','Proper factors each have one least weight','Polynomial has two: constant and leading; PE17–PE19','#edf8ef'),
 (8.82,r'$L=K\otimes_{K_0}F\hookrightarrow B_{\rm dR}$','L is a field; the map sends 1 to 1','Restrict to crystalline tensors; PE19','#edf8ef'),
 (6.73,r'$\beta=1-u/p;\quad\mathcal{S}=\{\sum a_n\beta^n\}$',r'$a_n\in A$'+'; primitive tail, integral leading terms','Coefficient recursion and separation; PE22–PE26','#fff4dc'),
 (5.03,r'$y=\log(1-\beta)$',r'Degree $N=p^j$: coefficient $-1/p$','Truncate strictly before 2N; PE27–PE31','#fff4dc'),
 (3.33,'y is transcendental over F and L','Galois cocycle + minimal polynomial coefficient','De Rham invariant field proved locally; PE32–PE35','#fff4dc'),
 (1.63,r'$K\otimes_{K_0}B_{\rm st}\hookrightarrow B_{\rm dR}$','Ring and fraction-field invariants equal K0','Tensor bases and scalar intersections; PE36–PE38','#edf8ef'),
]
for y,title,body,loc,colour in boxes:
 ax.add_patch(FancyBboxPatch((.22,y-.63),4.56,1.26,boxstyle='round,pad=.08',facecolor=colour,edgecolor='#27445f',linewidth=1.3))
 ax.text(2.5,y+.31,title,ha='center',va='center',fontsize=13)
 ax.text(2.5,y-.05,body,ha='center',va='center',fontsize=11)
 ax.text(2.5,y-.44,loc,ha='center',fontsize=8.6,color='#37516a')
for ys in ([13.92,12.22,10.52,8.82],[6.73,5.03,3.33,1.63]):
 for a,b in zip(ys,ys[1:]):
  ax.add_patch(FancyArrowPatch((2.5,a-.74),(2.5,b+.74),arrowstyle='-|>',mutation_scale=17,color='#27445f',linewidth=1.4))
ax.text(2.5,7.72,'Second mechanism: the logarithm obstruction',ha='center',fontsize=11,weight='bold')
ax.text(2.5,.44,'Arrows summarize the indicated proof steps.\nNo Frobenius on the de Rham ring is asserted.',ha='center',fontsize=10)
fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
p=root/'assets/ramified-semistable-proof-map.png'
fig.savefig(p,facecolor='white',metadata={'Software':'Matplotlib'});plt.close(fig)
with Image.open(p) as im:im.copy().save(p)
