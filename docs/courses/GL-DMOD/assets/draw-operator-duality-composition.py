"""Common current models and exact composition normalizations."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
r=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'GL-DMOD-CP-20261021','mathtext.fontset':'dejavusans'})
ink='#19384e';blue='#285f97';teal='#008b91';bg='#f4f7fb'
fig=plt.figure(figsize=(16,10),dpi=180,facecolor=bg);ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,16),ylim=(0,10));ax.axis('off')
def box(x,y,w,h,title,formula):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.1',ec=blue,fc='white',lw=1.5))
 ax.text(x+w/2,y+h-.14,title,ha='center',va='top',fontsize=12.5,color=ink)
 ax.text(x+w/2,y+.32,formula,ha='center',va='center',fontsize=17,color=blue)
def arrow(a,b,label=''):
 ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':teal,'lw':2})
 if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.16,label,ha='center',fontsize=14,color=teal)
ax.text(8,9.53,'Operator composition through a common two-action current model',ha='center',fontsize=21,weight='bold',color=ink)
box(.65,7.5,4.1,1.12,'Source current, CP.23',r'$u^{p,q}\otimes P_1\otimes P_2$')
box(5.95,7.5,4.1,1.12,'Intermediate current',r'$(f_*u)^{p-r,q-r}\otimes P_1\otimes P_2$')
box(11.25,7.5,4.1,1.12,'Final current',r'$((gf)_*u)^{p-r-s,q-r-s}\otimes P_1\otimes P_2$')
arrow((4.95,8.06),(5.75,8.06),r'$\kappa_r f_*$')
arrow((10.25,8.06),(11.05,8.06),r'$\kappa_s g_*$')
ax.text(8,6.99,r'$p+q-2n=(p-r)+(q-r)-2m=(p-r-s)+(q-r-s)-2k$',ha='center',fontsize=18,color=blue)
ax.text(8,6.5,r'$\kappa_s\kappa_r=\kappa_{r+s},\qquad\kappa_r=(-1)^r(2\pi i)^{-r}$',ha='center',fontsize=20,color=teal)
ax.plot([.65,15.35],[6.14,6.14],color='#bccbd8')
box(.9,4.5,5.25,1.12,'Intermediate resolution, CP.18',r'$\mathcal{Q}_Y\ \longrightarrow\ \mathscr{K}_Y[m]$')
box(9.85,4.5,5.25,1.12,'The next trace uses its inverse',r'$U_g(B_Y)^{-1}\,U_g(B_Y)=1$')
arrow((6.35,5.06),(9.65,5.06),r'$B_Y:\ P_1\mapsto2,\ P_2\mapsto1$')
ax.text(8,4.05,r'$B_Y^q(u\otimes P_1\otimes P_2)=(-1)^{mq}J_Y((u\otimes P_1)\cdot_2 P_2)$',ha='center',fontsize=18,color=blue)
ax.text(8,3.61,'The whole intermediate augmentation cancels: density sign, transpose, and both right actions.',ha='center',fontsize=13.5,color=ink)
ax.plot([.65,15.35],[3.24,3.24],color='#bccbd8')
ax.text(8,2.84,'Nonflat point–line–point example, CP.31',ha='center',fontsize=18,color=ink)
box(.95,1.35,3.1,.88,'Source point, n = 0',r'$(p,q)=(0,0)$')
box(6.45,1.35,3.1,.88,'Ambient complex line, m = 1',r'$(p-r,q-r)=(1,1)$')
box(11.95,1.35,3.1,.88,'Target point, k = 0',r'$(p-r-s,q-r-s)$'+'\n'+r'$=(0,0)$')
arrow((4.25,1.79),(6.25,1.79),r'$\kappa_{-1}=-2\pi i$')
arrow((9.75,1.79),(11.75,1.79),r'$\kappa_1=-(2\pi i)^{-1}$')
ax.text(8,.85,r'$\kappa_1\kappa_{-1}=1,\qquad g_*f_*u=u$',ha='center',fontsize=20,color=teal)
ax.text(8,.36,'The first transfer coefficient is nonflat. The second is ordinary-flat; the derived transfer identity retains it exactly.',ha='center',fontsize=13,color=ink)
fig.savefig(r/'operator-duality-composition.png',facecolor=bg);fig.savefig(r/'operator-duality-composition.svg',facecolor=bg,metadata={'Date':None});plt.close(fig)
sgn=lambda j:1 if j%2==0 else -1
degrees=[]
for n in range(5):
 for m in range(5):
  for k in range(5):
   rel,sec=n-m,m-k
   for p in range(n+1):
    for q in range(n+1):
     dp,dq=p-rel-sec,q-rel-sec
     degree=p+q-2*n;middle=(p-rel)+(q-rel)-2*m;final=dp+dq-2*k
     assert degree==middle==final and rel+sec==n-k and sgn(rel)*sgn(sec)==sgn(rel+sec)
     degrees.append({'n':n,'m':m,'k':k,'p':p,'q':q,'r':rel,'s':sec,'middle_type':[p-rel,q-rel],'final_type':[dp,dq],'middle_type_exists':0<=p-rel<=m and 0<=q-rel<=m,'final_type_exists':0<=dp<=k and 0<=dq<=k,'source_degree':degree,'middle_degree':middle,'final_degree':final,'raw_dimension_sign_product':sgn(rel)*sgn(sec),'raw_composite_sign':sgn(rel+sec),'normalization_power_sum':-rel-sec,'normalization_composite_power':-(n-k),'actual_nonvanishing_asserted':False})
signs=[]
for a in range(-2,3):
 for c in range(-2,3):
  for b in range(-2,3):
   for e in range(-2,3):
    direct=(a+c)*b+c*e;successive=a*b+c*b+c*e;assert direct==successive
    signs.append({'first_output_degree':a,'second_output_degree':c,'input_coefficient_degree':b,'first_input_transfer_degree':e,'direct_exponent':direct,'successive_exponent':successive,'sign':sgn(direct)})
data={'proof':'CP.A--CP.F','finite_samples_are_general_proof':False,'degree_and_normalization_compositions':degrees,'homogeneous_evaluation_composition_signs':signs,'nonflat_example':{'dimensions':[0,1,0],'relative_dimensions':[-1,1],'types':[[0,0],[1,1],[0,0]],'total_degrees':[0,0,0],'dimension_signs':[-1,-1,1],'normalization_powers':[1,-1,0],'first_coefficient_flat':False,'second_transfer_ordinary_flat':True},'augmentation_factor_labels':{'first_regular_factor':'output density-adjoint action2','second_regular_factor':'input regular action1'},'operator_adjunction_and_proper_regularity_are_separate_assertions':True}
(r/'operator-duality-composition-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
