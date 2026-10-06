"""Exact finite trace models and proof mechanism; CC0 original code/figure.
The matrices are finite examples, not a reduction of an arbitrary algebra.
"""
from pathlib import Path
from fractions import Fraction
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path(__file__).resolve().parent)
out=ap.parse_args().output/'assets';out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.hashsalt':'finite-center-trace-20261005'})
ink='#142c45';blue='#196aa5';orange='#d46a20';green='#257b59';bg='#f5f8fc'
fig=plt.figure(figsize=(17,11),dpi=200,facecolor=bg)
fig.suptitle('A normal trace keeps every center coordinate',y=.977,fontsize=29,fontweight='bold',color=ink)
fig.text(.5,.921,'Exact finite matrix models above · full arbitrary-center construction below',ha='center',fontsize=17,color=ink)
ax=fig.add_axes([.065,.44,.41,.37]);ax.set_title('A  Distorted states converge to equal weights',loc='left',fontsize=21,pad=23,color=ink)
bs=[Fraction(1,2),Fraction(1,4),Fraction(1,8),Fraction(0)];data=[]
for j,b in enumerate(bs):
 w1=(1+b)/2;w2=(1-b)/2;a=(1+b)/(1-b);y=3-j
 ax.barh(y,float(w1),height=.55,color=blue);ax.barh(y,float(w2),left=float(w1),height=.55,color=orange)
 ax.text(float(w1)/2,y,str(w1),ha='center',va='center',color='white',fontsize=17,fontweight='bold')
 ax.text(float(w1+w2/2),y,str(w2),ha='center',va='center',color='white',fontsize=17,fontweight='bold')
 ax.text(1.045,y,f'a = {a}\nexact error = {b}',va='center',fontsize=14,color=ink)
 data.append({'b':str(b),'weights':[str(w1),str(w2)],'distortion_a':str(a),'exact_norm_error':str(b),'general_stability_bound':str(2*(a*a-1))})
ax.set_yticks([3,2,1,0],labels=['b = 1/2','b = 1/4','b = 1/8','b = 0'])
ax.set_xticks([0,.5,1],labels=['0','1/2','1']);ax.set_xlim(0,1.35);ax.set_ylim(-.65,3.65)
ax.set_xlabel('weights of the two diagonal coordinates',fontsize=15)
ax.spines[['top','right','left']].set_visible(False);ax.grid(axis='x',alpha=.15);ax.set_axisbelow(True)
fig.text(.065,.355,r'$\phi_b(xx^*)\leq a_b\phi_b(x^*x),\quad a_b=(1+b)/(1-b)$',fontsize=19,color=ink)
fig.text(.065,.309,r'$\|\phi_b-\mathrm{tr}_2\|=b$  (attained at diag(1, −1))',fontsize=18,color=ink)

right=fig.add_axes([.545,.395,.4,.405]);right.set_axis_off();right.set_title('B  Two independent center coordinates',loc='left',fontsize=21,pad=28,color=ink)
def box(x,y,w,h,text,color=ink,face='white',fs=16):
 right.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.018',facecolor=face,edgecolor=color,lw=2))
 right.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=fs,color=color)
box(.025,.605,.395,.24,'M₂ corner\nA = diag(3, 1)',blue)
box(.56,.605,.395,.24,'M₃ corner\nB = diag(6, 3, 0)',green)
box(.025,.295,.395,.22,'Tr(A)/2 = 2\ncenter unit (1, 0)',blue,fs=15)
box(.56,.295,.395,.22,'Tr(B)/3 = 3\ncenter unit (0, 1)',green,fs=15)
for x in [.2225,.7575]:right.add_patch(FancyArrowPatch((x,.585),(x,.535),arrowstyle='-|>',mutation_scale=17,color=ink,lw=2))
right.text(.49,.12,'T(A ⊕ B) = (2, 3) ∈ ℂ ⊕ ℂ\nT(1₂ ⊕ 1₃) = (1, 1)',ha='center',va='center',fontsize=18,color=ink)
fig.text(.545,.309,'Rank-one tiles: (1/2, 0) and (0, 1/3)',fontsize=17,color=ink)

route=fig.add_axes([.045,.058,.915,.18]);route.set_axis_off()
route.text(.01,1.14,'GENERAL CONSTRUCTION  ·  finite algebra, arbitrary center and Hilbert space',fontsize=18,fontweight='bold',color=ink)
labels=[('Finite central tilings','cancellation +\nmatrix / dyadic families'),('Local balancing','two maximal families\nretain the factor μ'),('Normal approximate maps','full finite matrix sum\ncentral bounded inverse'),('Operator-norm limit','‖φₘ − φₙ‖\n≤ 2(aₘ² − 1)'),('Faithful trace','T(p) = z/k\nnormality + uniqueness')]
for i,(head,body) in enumerate(labels):
 x=.012+i*.2
 route.add_patch(FancyBboxPatch((x,.12),.155,.77,boxstyle='round,pad=.008',facecolor='white',edgecolor=blue if i%2==0 else green,lw=2))
 route.text(x+.0775,.68,head,ha='center',va='center',fontsize=11.6,color=ink,fontweight='bold')
 route.text(x+.0775,.39,body,ha='center',va='center',fontsize=12.2,color=ink)
 if i<4:route.add_patch(FancyArrowPatch((x+.168,.5),(x+.189,.5),arrowstyle='-|>',mutation_scale=17,color=ink,lw=1.8))
fig.text(.065,.025,'Exact models: FCT9 · stability bound: FCT1 · finite tilings: FCT2–3 · normal assemblies: FCT4–6 · consequences: FCT7–8',fontsize=13,color=ink)
fig.savefig(out/'finite-center-trace.png',dpi=200,metadata={'Software':'original finite-center-trace renderer'})
fig.savefig(out/'finite-center-trace.svg',metadata={'Date':None,'Creator':'original finite-center-trace renderer'})
semantic={'scope':'Exact M2 and M2 direct-sum M3 examples; general proof diagram is schematic, not a finite-dimensional reduction',
 'states':data,'attaining_contraction_diagonal':[1,-1],
 'center_example':{'A_diagonal':[3,1],'B_diagonal':[6,3,0],'T_value':[2,3],'T_unit':[1,1],
 'rank_one_tile_values':[['1/2','0'],['0','1/3']]},
 'general_bound':'For m<n with a_n<=a_m: norm(phi_m-phi_n)<=2*(a_m^2-1); different from the exact model error b',
 'local_proof_anchors':['fct-1','fct-2','fct-3','fct-4','fct-5','fct-6','fct-7','fct-8','fct-9']}
(out/'finite-center-trace-data.json').write_text(json.dumps(semantic,indent=2,ensure_ascii=False)+'\n',encoding='utf8',newline='\n')
plt.close(fig)
