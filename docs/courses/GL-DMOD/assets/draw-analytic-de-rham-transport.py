"""Reproduce the de Rham comparison and exact density degree/sign diagram."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'GL-DMOD-DRP-20261021'})
r=Path(__file__).resolve().parent
fig=plt.figure(figsize=(16,9),facecolor='#f6f8fb')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,16);ax.set_ylim(0,9);ax.axis('off')
ink='#18334b';blue='#295d9f';green='#00848a'
ax.text(8,8.62,'Analytic de Rham transport',ha='center',va='center',fontsize=23,color=ink,weight='bold')
ax.text(.6,8.02,'Canonical derived comparison',fontsize=16,color=ink,weight='bold')
def box(y,text,note):
 ax.add_patch(FancyBboxPatch((.65,y),8.7,1.22,boxstyle='round,pad=0.08',facecolor='white',edgecolor=blue,linewidth=1.7))
 ax.text(5,y+.77,text,ha='center',va='center',fontsize=18,color=blue)
 ax.text(5,y+.27,note,ha='center',va='center',fontsize=10,color=ink)
box(6.15,r'$\mathrm{DR}^{\mathrm{r}}_Y(f_+M)$','Right modules; actual transfer action retained')
box(3.85,r'$Rf_*\!\left((M\otimes^L_{\mathcal{D}_X}T_f)\otimes^L_{f^{-1}\mathcal{D}_Y}f^{-1}\mathcal{O}_Y\right)$','Finite perfect projection comparison: DRP.11')
box(1.55,r'$Rf_*\!\left(M\otimes^L_{\mathcal{D}_X}\mathcal{O}_X\right)$','Split target Spencer cancellation: DRP.10')
for lo,hi in [(5.17,6.06),(2.87,3.76)]:
 ax.add_patch(FancyArrowPatch((5,hi),(5,lo),arrowstyle='-|>',mutation_scale=18,color=green,linewidth=2))
 ax.text(5.27,(lo+hi)/2,r'$\simeq$',fontsize=22,color=green,va='center')
ax.text(5,.91,'No flatness of f or its coefficients is required.',ha='center',fontsize=12,color=ink)
ax.text(5,.50,'Proper coherence and regularity have their own hypotheses and proofs.',ha='center',fontsize=11,color=ink)
ax.text(12.5,8.02,'Exact density signs',ha='center',fontsize=16,color=ink,weight='bold')
ax.text(12.5,7.49,r'$n=2,\quad a=0,\quad k=n-r$',ha='center',fontsize=17,color=blue)
columns=[10.15,11.75,13.55,15.0]
for x,label in zip(columns,['r','form degree k','sign','total degree']):ax.text(x,6.88,label,ha='center',fontsize=11,color=ink,weight='bold')
for i,values in enumerate([(0,2,'+',0),(1,1,'−',-1),(2,0,'−',-2)]):
 y=6.16-i*.88
 ax.plot([9.8,15.55],[y-.42,y-.42],color='#d2deeb',lw=.8)
 for x,value in zip(columns,values):ax.text(x,y,str(value),ha='center',va='center',fontsize=18,color=blue)
ax.text(12.6,3.17,r'$(-1)^{ar+nr+r(r+1)/2}$',ha='center',fontsize=21,color=green)
ax.text(12.6,2.63,'Determinant contraction, DRP.15',ha='center',fontsize=11,color=ink)
ax.text(12.6,1.98,r'$a-r=(n-r)+a-n$',ha='center',fontsize=17,color=blue)
ax.text(12.6,1.42,'Tensor and shifted-form degrees agree.',ha='center',fontsize=11,color=ink)
ax.text(12.6,.80,'All dimensions and coefficient degrees:',ha='center',fontsize=11,color=ink)
ax.text(12.6,.42,'the proof is DRP.16–DRP.20.',ha='center',fontsize=11,color=ink)
fig.savefig(r/'analytic-de-rham-transport.png',dpi=180,facecolor=fig.get_facecolor())
fig.savefig(r/'analytic-de-rham-transport.svg',metadata={'Date':None},facecolor=fig.get_facecolor());plt.close(fig)
records=[]
for n in range(7):
 for a in range(-2,3):
  for e in range(n+1):
   c=(-1)**(a*e+n*e+e*(e+1)//2)
   records.append({'n':n,'a':a,'r':e,'form_degree':n-e,'tensor_degree':a-e,'shifted_form_degree':n-e+a-n,'sign':c})
data={'proof':'DRP.A--DRP.G','finite_samples_are_general_proof':False,
 'left_maps':['finite perfect projection DRP.11','split target Spencer augmentation DRP.10'],
 'map_shift':0,'right_panel':{'n':2,'a':0,'rows':[x for x in records if x['n']==2 and x['a']==0]},
 'finite_degree_sign_samples':records,'identity_for_all_degrees':'c_r=(-1)^(n+r)c_(r-1); (-1)^((a+1)r)=(-1)^r(-1)^(ar)'}
(r/'analytic-de-rham-transport-data.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'degree_sign_records':len(records),'outputs':3}))
