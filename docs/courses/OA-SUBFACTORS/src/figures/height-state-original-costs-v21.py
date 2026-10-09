from pathlib import Path
import datetime, json
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"]="height-state-original-costs-v21"
from matplotlib.patches import FancyBboxPatch

OUT=Path(__file__).resolve().parent
r,w,lam=sp.symbols('r w lambda',positive=True)
d=(4+lam)*(4+1/lam)
u0=1/(1+4*lam)
u1=lam/(1+4*lam)
checks={
 'reciprocal_tangent':sp.simplify(1/r-1/w+(r-w)/w**2-(r-w)**2/(w**2*r))==0,
 'u_reciprocal_sum_original_index':sp.simplify(1/u0+4/u1-d)==0,
 'original_tail_weight_identity':sp.simplify(lam/(4+lam)/((1+4*lam)/(4+lam))-u1)==0,
 'lamp_variance_constant':sp.Rational(2)*(sp.Rational(5,8))**2==sp.Rational(25,32),
 'reciprocal_variance_constant':(2*sp.Rational(5,8))**2==sp.Rational(25,16),
}
assert all(checks.values()),checks
fig,ax=plt.subplots(figsize=(13,7.5))
fig.patch.set_facecolor('#f7f9fc');ax.set_facecolor('#f7f9fc')
ax.set_xlim(0,13);ax.set_ylim(0,7.5);ax.axis('off')
ax.text(.35,7.1,'Actual height states: original bounded values that invariance must change',fontsize=16,weight='bold',color='#183448')
ax.text(.35,6.65,r'Fixed WM.22: $\lambda=1+2^{-31}25^{-198153}$, original $Z(W)$, $H$, $R_i$, and $D_1$',fontsize=12,color='#183448')
def box(x,y,width,height,text,color):
 p=FancyBboxPatch((x,y),width,height,boxstyle='round,pad=0.12,rounding_size=0.08',linewidth=1.3,edgecolor=color,facecolor='white')
 ax.add_patch(p);ax.text(x+width/2,y+height/2,text,ha='center',va='center',fontsize=13,color='#183448',linespacing=1.45)
def arrow(a,b):
 ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':'#657c8c','lw':1.6})
box(.45,4.15,3.2,1.65,'Actual joint height cluster\n'+r'$\eta,\rho$ on the full center'+'\n'+r'$a=\eta(L_0),\ q=\rho(L_0)$'+'\n'+r'$a,q\geq 5b/8>0$','#376c98')
box(4.4,4.25,3.65,1.45,'Exact original correlations\n'+r'$\eta((D_1-1)L_0)=-2a$'+'\n'+r'$\rho((R_1-u_1)L_0)=-u_1(a+q)$','#376c98')
arrow((3.78,4.95),(4.2,4.95))
box(8.65,4.25,3.8,1.45,'Actual lower bounds\n'+r'$\rho(\sum_i R_i^{-1}-d)\geq25b^2/16$'+'\n'+r'$\eta(\log D_1)\leq-25b^2/(32d^2)$','#ae6635')
arrow((8.18,4.95),(8.48,4.95))
ax.text(10.55,3.78,'HD18.3 and HD18.7',ha='center',fontsize=11,color='#824522')
box(2.6,1.95,7.8,1.2,'Every actual full-center invariant state '+r'$\omega$'+'\n'+r'$\omega(\sum_i R_i^{-1}-d)=0$'+' and '+r'$\omega(\log D_1)=0$'+'\nOriginal providers: C13.20 and E14.15','#3d8174')
ax.text(.45,.82,'The spatial logarithmic endpoint remains unresolved.',fontsize=14,weight='bold',color='#183448')
ax.text(.45,.32,'Boxes and arrows show proved identities and implications; sizes encode no probabilities or distances.',fontsize=11,color='#536877')
fig.savefig(OUT/'height-state-original-costs-v21.svg',bbox_inches='tight',metadata={'Date':None})
fig.savefig(OUT/'height-state-original-costs-v21.png',dpi=160,bbox_inches='tight')
plt.close(fig)
(OUT/'height-state-original-costs-checks.json').write_text(json.dumps({'exact_algebra_checks':checks,'verification_scope':'Symbolic identities and displayed numerical factors; full-state inequalities have the written analytic proofs HD18.1-HD18.2. No numerical replacement of WM.22 parameter.','zero_cost_endpoint_claimed':False,'universal_invariant_floor_claimed':False},indent=2)+'\n',encoding='utf-8')
print(json.dumps(checks))

svg_path=OUT/"height-state-original-costs-v21.svg"
svg_path.write_text("\n".join(x.rstrip() for x in svg_path.read_text(encoding="utf-8").splitlines()).rstrip()+"\n",encoding="utf-8")
