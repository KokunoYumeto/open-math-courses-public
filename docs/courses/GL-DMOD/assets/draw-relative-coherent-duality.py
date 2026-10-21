"""Reproducible current trace degrees and full Koszul point-test diagram."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
r=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'GL-DMOD-RCD-20261021','mathtext.fontset':'dejavusans'})
ink='#19384e';blue='#285f97';teal='#008b91';bg='#f4f7fb'
fig=plt.figure(figsize=(16,10),dpi=180,facecolor=bg)
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,16),ylim=(0,10));ax.axis('off')
def box(x,y,w,h,title,formula,colour=blue):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',ec=colour,fc='white',lw=1.5))
 ax.text(x+w/2,y+h-.26,title,ha='center',va='top',fontsize=13,color=ink)
 ax.text(x+w/2,y+.39,formula,ha='center',va='center',fontsize=17,color=colour)
def arrow(a,b,label='',colour=teal):
 ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':colour,'lw':2})
 if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.18,label,ha='center',fontsize=12,color=colour)
ax.text(8,9.58,'Proper coherent analytic duality: the actual trace and point tests',ha='center',fontsize=21,weight='bold',color=ink)
box(.7,7.48,5.6,1.36,'Source current on X, dimension n',r'$u^{n,q},\quad |u|=q-n$')
box(9.7,7.48,5.6,1.36,'Target current on Y, dimension m',r'$(f_*u)^{m,q-r},\quad |f_*u|=q-n$')
arrow((6.55,8.15),(9.45,8.15),r'$r=n-m$')
ax.text(8,6.95,r'$\tau_f^q=(-1)^{r(q-n)}(2\pi i)^{-r}f_*$',ha='center',fontsize=20,color=blue)
ax.text(8,6.5,'Proper support makes current pushforward defined. The shift signs agree: RCD.3–RCD.13.',ha='center',fontsize=13,color=ink)
ax.plot([.65,15.35],[6.1,6.1],color='#bccbd8',lw=1)
ax.text(8,5.73,r'$A=Rf_*F,\qquad B=Rf_*D_XF,\qquad P=k_y$ with its full finite Koszul resolution',ha='center',fontsize=17,color=ink)
box(.7,3.73,5.6,1.25,'Source point test, RCD.21',r'$R\mathrm{Hom}_{\mathcal{O}_Y}(P,B)$')
box(9.7,3.73,5.6,1.25,'Target point test, RCD.22',r'$R\mathrm{Hom}_{\mathcal{O}_Y}(P,D_YA)$')
arrow((6.55,4.35),(9.45,4.35),r'$R\mathrm{Hom}(P,\alpha_f)$')
box(.7,1.15,5.6,1.5,'Compact duality on X',r'$R\mathrm{Hom}_{\mathbb{C}}(R\Gamma(X,F\otimes^L Lf^*P),\mathbb{C})$',teal)
box(9.7,1.15,5.6,1.5,'Compact duality on Y',r'$R\mathrm{Hom}_{\mathbb{C}}(R\Gamma(Y,A\otimes^L P),\mathbb{C})$',teal)
arrow((3.5,3.53),(3.5,2.82));arrow((12.5,3.53),(12.5,2.82))
ax.text(2.86,3.12,r'$\simeq$',fontsize=23,color=teal);ax.text(11.86,3.12,r'$\simeq$',fontsize=23,color=teal)
arrow((6.55,1.9),(9.45,1.9),r'$\pi_P^{\vee}$')
ax.text(8,.65,'The square commutes by actual evaluation and the compact trace identity; its bottom arrow is an isomorphism.',ha='center',fontsize=12.5,color=ink)
ax.text(8,.25,'RCD.23–RCD.26: finite coherent point tests detect the cone. No underived fibre or flatness assumption is used.',ha='center',fontsize=12.5,color=ink)
fig.savefig(r/'relative-coherent-duality.png',facecolor=bg)
fig.savefig(r/'relative-coherent-duality.svg',facecolor=bg,metadata={'Date':None})
plt.close(fig)
sgn=lambda k:1 if k%2==0 else -1
degrees=[]
for n in range(5):
 for m in range(5):
  for q in range(n+1):
   rel=n-m;qt=q-rel
   degrees.append({'n':n,'m':m,'q':q,'r':rel,'target_antiholomorphic_degree':qt,
    'target_type_exists':0<=qt<=m,'source_cochain_degree':q-n,'target_cochain_degree':qt-m,
    'trace_sign':sgn(rel*(q-n)),'next_sign':sgn(rel*(q+1-n)),
    'source_differential_sign':sgn(n),'target_differential_sign':sgn(m),
    'normalization_exponent':-rel})
compositions=[]
for n in range(4):
 for m in range(4):
  for l in range(4):
   for q in range(n+1):
    rel=n-m;s=m-l
    compositions.append({'n':n,'m':m,'l':l,'q':q,
     'composed_exponent':rel*(q-n)+s*(q-rel-m),'direct_exponent':(rel+s)*(q-n),
     'composed_normalization_exponent':-rel-s,'direct_normalization_exponent':-(n-l)})
data={'proof':'RCD.A--RCD.G','finite_samples_are_general_proof':False,
 'trace_degree_samples':degrees,'composition_samples':compositions,
 'point_test':'full coordinate Koszul complex; all negative degrees and attaching maps retained',
 'compact_support':'supp(F tensor^L Lf^*k_y) is contained in the compact set S intersect f^{-1}(y)',
 'square_bottom_arrow':'scalar dual of actual finite perfect projection RCD.18',
 'square_commutation':'evaluation sign RCD.20 and normalized compact trace RCD.13',
 'cone_detection':'full finite Koszul duality RCD.25 and finite-module Nakayama RCD.26'}
(r/'relative-coherent-duality-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
