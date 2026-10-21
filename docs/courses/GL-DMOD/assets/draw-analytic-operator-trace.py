"""Current trace, two-action kernel labels and a finite duality-tail example."""
from pathlib import Path
import json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import sympy as sp
r=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'GL-DMOD-OT-20261021','mathtext.fontset':'dejavusans'})
ink='#19384e';blue='#285f97';teal='#008b91';bg='#f4f7fb';gold='#b57c20'
fig=plt.figure(figsize=(16,10),dpi=180,facecolor=bg)
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,16),ylim=(0,10));ax.axis('off')
def box(x,y,w,h,title,formula,colour=blue):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.1',ec=colour,fc='white',lw=1.5))
 ax.text(x+w/2,y+h-.17,title,ha='center',va='top',fontsize=12.5,color=ink)
 ax.text(x+w/2,y+.34,formula,ha='center',va='center',fontsize=17,color=colour)
def arrow(a,b,label=''):
 ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':teal,'lw':2})
 if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.15,label,ha='center',fontsize=12,color=teal)
ax.text(8,9.6,'Analytic operator trace: current degrees, kernel actions and the finite tail',ha='center',fontsize=20,weight='bold',color=ink)
box(.65,7.75,5.9,1.12,'Full source Spencer–current term, OT.16',r'$u^{p,q}\otimes P,\quad p+q-2n$')
box(9.45,7.75,5.9,1.12,'Full target Spencer–current term',r'$(f_*u)^{p-r,q-r}\otimes P$')
arrow((6.8,8.28),(9.2,8.28),r'$\kappa_r f_*$')
ax.text(8,7.22,r'$(p-r)+(q-r)-2m=p+q-2n,\qquad r=n-m$',ha='center',fontsize=18,color=blue)
ax.text(8,6.79,r'Even full shifts; density-edge calibration fixes $\kappa_r=(-1)^r(2\pi i)^{-r}$, OT.18–OT.20.',ha='center',fontsize=12.5,color=ink)
ax.plot([.65,15.35],[6.48,6.48],color='#bccbd8',lw=1)
box(.65,4.76,5.9,1.15,'Kernel before the final flip, OT.25',r'$T_1\mapsto\mathrm{regular}\ 1,\quad T_2\mapsto\mathrm{adjoint}\ 2$')
box(9.45,4.76,5.9,1.15,'Dual comparison after the flip, OT.26',r'$T_2\mapsto\mathrm{input}\ 1,\quad T_1\mapsto\mathrm{output}\ 2$')
arrow((6.8,5.31),(9.2,5.31),r'$J_Y,\quad J_Y^2=1$')
ax.text(8,4.22,r'$J_Y(\nu\otimes P)=\nu\otimes P^{t,\nu},\qquad P^{t,h\nu}=h^{-1}P^{t,\nu}h$',ha='center',fontsize=18,color=blue)
ax.text(8,3.79,'The involution exchanges two commuting right actions. Density derivatives are included in the transpose.',ha='center',fontsize=12.5,color=ink)
ax.plot([.65,15.35],[3.45,3.45],color='#bccbd8',lw=1)
ax.text(8,3.05,'Uniform-tail illustration: n = 2, m = 1, s = 4n + m + 2 = 11',ha='center',fontsize=17,color=ink)
def xp(t):return 1+(t+6)*.8
ax.plot([xp(-6),xp(10)],[1.62,1.62],color=ink,lw=1)
for t in range(-6,11):
 ax.plot([xp(t),xp(t)],[1.55,1.69],color=ink,lw=1);ax.text(xp(t),1.3,str(t),ha='center',fontsize=10,color=ink)
ax.plot([xp(-5),xp(4)],[1.97,1.97],color=teal,lw=10,solid_capstyle='butt')
ax.text((xp(-5)+xp(4))/2,2.34,r'Full sufficient interval $[-2n-m,2n]=[-5,4]$',ha='center',fontsize=13,color=teal)
ax.scatter([xp(5)],[1.97],color=gold,s=65);ax.text(xp(5),2.3,r'$q+1=5$',ha='center',fontsize=11,color=gold)
ax.annotate('',xy=(xp(10),2.6),xytext=(xp(7),2.6),arrowprops={'arrowstyle':'->','color':blue,'lw':3})
ax.text((xp(7)+xp(10))/2,2.83,r'$W_Y:\ \mathrm{degree}\geq7$',ha='center',fontsize=12,color=blue)
ax.annotate('',xy=(xp(10),2.04),xytext=(xp(8),2.04),arrowprops={'arrowstyle':'->','color':blue,'lw':3})
ax.text((xp(8)+xp(10))/2,1.73,r'$W_X\geq8$',ha='center',fontsize=11,color=blue)
ax.text(8,.78,'Both q and q+1 miss the first triangle terms throughout the required interval; OT.29–OT.31 prove the general bound.',ha='center',fontsize=12.5,color=ink)
ax.text(8,.32,'The finite reduction assumes the induced-coefficient comparison is invertible. The trace construction alone does not prove that premise.',ha='center',fontsize=12.5,color=ink)
fig.savefig(r/'analytic-operator-trace.png',facecolor=bg)
fig.savefig(r/'analytic-operator-trace.svg',facecolor=bg,metadata={'Date':None});plt.close(fig)
degrees=[]
for n in range(5):
 for m in range(5):
  rel=n-m
  for p in range(n+1):
   for q in range(n+1):
    degrees.append({'n':n,'m':m,'p':p,'q':q,'r':rel,'target_p':p-rel,'target_q':q-rel,
     'target_type_exists':0<=p-rel<=m and 0<=q-rel<=m,'source_degree':p+q-2*n,'target_degree':p+q-2*rel-2*m,
     'normalization_exponent':-rel,'raw_dimension_sign':1 if rel%2==0 else -1,'source_shift_sign':1,'target_shift_sign':1})
tails=[]
for n in range(5):
 for m in range(5):
  s=4*n+m+2
  tails.append({'n':n,'m':m,'s':s,'comparison_interval':[-2*n-m,2*n],
    'source_first_triangle_term_lower':s+1-2*n,'target_first_triangle_term_lower':s+1-2*n-m,
    'largest_needed_adjacent_degree':2*n+1,'induced_invertibility_is_an_additional_premise':True})
x=sp.Symbol('x')
clean=lambda a:{k:sp.expand(v)for k,v in a.items()if sp.expand(v)!=0}
def mul(a,b):
 c={}
 for i,ai in a.items():
  for j,bj in b.items():
   for k in range(i+1):c[i-k+j]=c.get(i-k+j,0)+sp.binomial(i,k)*ai*sp.diff(bj,x,k)
 return clean(c)
def trans(a):
 c={}
 for i,ai in a.items():
  for k in range(i+1):c[i-k]=c.get(i-k,0)+(-1)**i*sp.binomial(i,k)*sp.diff(ai,x,k)
 return clean(c)
def encode(a):return {str(k):str(v)for k,v in sorted(clean(a).items())}
monomials=[{b:x**a}for a in range(4)for b in range(4)]
involutions=[]
for a in monomials:
 assert clean(trans(trans(a)))==clean(a)
 # For the nonconstant volume exp(x)dx, conjugation replaces d/dx by d/dx+1.
 def conj_exp(b):
  c={}
  for i,ai in b.items():
   for k in range(i+1):c[k]=c.get(k,0)+sp.binomial(i,k)*ai
  return clean(c)
 ta=conj_exp(trans(a));assert conj_exp(trans(ta))==clean(a)
 involutions.append({'operator':encode(a),'transpose_dx':encode(trans(a)),'transpose_exp_x_dx':encode(ta),'both_double_transposes_equal_original':True})
anti=[]
for i,a in enumerate(monomials):
 for j,b in enumerate(monomials):
  assert trans(mul(a,b))==mul(trans(b),trans(a))
  anti.append({'first':i,'second':j,'transpose_of_product_equals_reversed_transpose_product':True})
edges=[]
sgn=lambda k:1 if k%2==0 else -1
for n in range(5):
 for m in range(5):
  rel=n-m
  for q in range(n+1):
   ss,ta,raw=sgn(n*q),sgn(m*(q-rel)),sgn(rel)
   expected=sgn(rel*(q-n));assert ss*ta*raw==expected
   edges.append({'n':n,'m':m,'q':q,'r':rel,'target_type_exists':0<=q-rel<=m,'source_edge_sign':ss,'target_augmentation_sign':ta,
    'raw_dimension_sign':raw,'composite_sign':ss*ta*raw,'coherent_RCD_sign':expected})
data={'proof':'OT.A--OT.G','finite_samples_are_general_proof':False,'full_current_degree_samples':degrees,
 'finite_tail_samples':tails,'finite_coherent_edge_calibrations':edges,'finite_transpose_involution_samples':involutions,'finite_transpose_product_samples':anti,
 'tail_figure_example':next(z for z in tails if z['n']==2 and z['m']==1),
 'kernel_before_flip':{'T1':'regular action1','T2':'density adjoint action2'},
 'kernel_after_flip':{'T2':'input regular action1','T1':'output density adjoint action2'},
 'duality_invertibility_hypothesis':'the comparison is invertible on every induced coherent coefficient','induced_coefficient_invertibility_is_still_required':True}
(r/'analytic-operator-trace-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
