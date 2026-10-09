"""CC0. Exact coordinates and reproducible illustration of CA.1/CA.2/CA.4/CA.6."""
from pathlib import Path
from fractions import Fraction as F
import json, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

root=Path(__file__).resolve().parent
a=complex(float(F(-3,20)),0)
t=complex(float(F(-3,200)),float(F(1,50)))
theta=F(13,20); sigma=F(2,5)
s=a+float(theta)*(t-a)
r=a+float(sigma)*(s-a)
delta=float(F(1,250)); kappa=float(F(2,5))
assert abs(abs(t-s)+abs(s-r)-abs(t-r))<1e-14
mu=-t.real-(t.imag*t.imag)/20
assert 2*.1*delta<=mu/8
assert .1*kappa<=1/16
data={
 'scope':'Exact real section, exact rational complex-time sample, and chain diagram; no numerical proof',
 'cone':{'epsilon':'1/4','A':3,'g':'r^2/20','L':'1/10','L_valid_radius':1,'output_Re_t':'1/10','output_x':'1/20'},
 'nested':{'a':'-3/20','t':'-3/200+i/50','theta':'13/20','sigma':'2/5','delta':'1/250','kappa':'2/5','s':{'real':str(F(-3,20)+theta*(F(-3,200)-F(-3,20))),'imag':str(theta*F(1,50))},'r':{'real':str(F(-3,20)+sigma*theta*(F(-3,200)-F(-3,20))),'imag':str(sigma*theta*F(1,50))},'outer_radius':delta+kappa*abs(t-s),'inner_radius':delta+kappa*abs(s-r),'total_radius':2*delta+kappa*abs(t-r)},
 'proof_locators':['CA.1-CA.4','CA.9-CA.11','CA.22-CA.24','CA.29-CA.35'],
 'free_context':'Bound Microhyp section3.1 and HolIII III.1/IV.2; all depicted statements proved locally',
}
plt.rcParams.update({'font.size':11,'axes.titlesize':13,'svg.hashsalt':'full-action-domain-20261009'})
fig,axes=plt.subplots(1,3,figsize=(19.5,6.8),gridspec_kw={'width_ratios':[1,1,1.23]})
ax=axes[0]
S,Y=np.meshgrid(np.linspace(-.2,.135,600),np.linspace(-.75,.75,700))
l=.1-S
cone=(l>=0)&(np.abs(Y-.05)<=3*l)
support=cone&(S>=-Y*Y/20)
ax.contourf(S,Y,cone.astype(int),levels=[.5,1.5],colors=['#dcebf3'],alpha=.85)
ax.contourf(S,Y,support.astype(int),levels=[.5,1.5],colors=['#e99c64'],alpha=.8)
yy=np.linspace(-.75,.75,400)
ax.plot(-yy*yy/20,yy,color='#354b66',label=r'$\partial\Omega_g:\ \Re s=-y^2/20$')
ss=np.linspace(-.2,.1,400)
ax.plot(ss,.05+3*(.1-ss),color='#256688')
ax.plot(ss,.05-3*(.1-ss),color='#256688',label=r'$|y-x|\leq3(\Re t-\Re s)$')
M=math.sqrt(9+1/16)
lbound=(.1+.05*.05/20)/(1-.1*M)
ax.axvline(.1-lbound,color='#a05624',ls='--',label=r'$l\leq(\Re t+g(|x|))/(1-LM)$')
ax.scatter([.1],[.05],color='black',s=35,zorder=4)
ax.annotate(r'$u=(1/10,1/20)$',(.1,.05),xytext=(-.08,.49),arrowprops={'arrowstyle':'->'})
ax.text(-.14,-.49,r'$\Omega_g$',fontsize=15,color='#354b66')
ax.text(.025,-.1,r'$S=G\cap Z_{\rm in}$',fontsize=11,color='#71340c')
ax.set(xlim=(-.2,.135),ylim=(-.75,.75),xlabel=r'input real time $\Re s$',ylabel=r'real spatial section $y$',title='Proper fibre: exact real section')
ax.legend(loc='lower left',fontsize=8.6)
ax.grid(alpha=.18)

ax=axes[1]
ax.plot([a.real,t.real],[a.imag,t.imag],color='#5a7286',lw=2)
for point,label,offset in [(a,r'$a$',(-6,-19)),(r,r'$r=a+\sigma(s-a)$',(-10,15)),(s,r'$s=a+\theta(t-a)$',(-45,20)),(t,r'$t$',(5,-16))]:
 ax.scatter([point.real],[point.imag],s=42,color='#1c5276',zorder=3)
 ax.annotate(label,(point.real,point.imag),xytext=offset,textcoords='offset points',fontsize=11)
ax.annotate('',(s.real,s.imag-.009),(t.real,t.imag-.009),arrowprops={'arrowstyle':'<->','color':'#b66830'})
ax.annotate('',(r.real,r.imag-.015),(s.real,s.imag-.015),arrowprops={'arrowstyle':'<->','color':'#258476'})
ax.text(-.148,-.058,r'$|t-s|+|s-r|=|t-r|$',fontsize=13)
ax.text(-.148,-.081,r'$R_P(s)=\delta+\kappa|t-s|$',color='#b66830',fontsize=11)
ax.text(-.148,-.104,r'$R_Q(r)=\delta+\kappa|s-r|$',color='#258476',fontsize=11)
ax.text(-.148,-.127,r'$R_P+R_Q=2\delta+\kappa|t-r|$',fontsize=11)
ax.text(-.148,-.153,r'input margin $\geq7\mu/8+3|t-r|/8>0$',fontsize=11)
ax.set(xlim=(-.17,.005),ylim=(-.175,.06),xlabel=r'complex-time real part',ylabel=r'complex-time imaginary part',title='Same anchor: two nested Cauchy families')
ax.grid(alpha=.18)

ax=axes[2]
ax.axis('off')
ax.set_title('Actual controlled primitives and cone equality',pad=16)
boxes=[
 (0.84,r'$T_{\rm root}-T_{\rm ann}=\bar\partial H_P$'+'\n'+r'$H_P=F_{\rm root}-F_{\rm ann}+\bar\partial b_P$, supported in $G$'),
 (0.63,'Spatial annulus isotopy + ordered Cauchy trace\n'+r'$\bar\partial(\chi_0K_f)-\bar\partial K_f=\bar\partial[(\chi_0-1)K_f]$'),
 (0.41,r'$E_P=E_{\rm ray}+D_{\rm time}+I_N(\bar\partial\eta\wedge H_Pf)$'+'\nAll three terms use fixed full negative-time tubes'),
 (0.18,r'$Q_NL_\eta c_F=(0,-V_P)+d(E_P+J_\chi,0)$'+'\n'+r'$c_F=(T_P\bar\partial F,(-1)^NT_P(F-f))$'+'\n'+r'Residual $F-f=(\chi-1)f$ retained'),
]
for y,text in boxes:
 ax.text(.5,y,text,ha='center',va='center',fontsize=11,bbox={'boxstyle':'round,pad=.65','facecolor':'#eef4f6','edgecolor':'#547080'},transform=ax.transAxes)
for top,bottom in [(.78,.71),(.56,.48),(.34,.27)]:
 ax.annotate('',(.5,bottom),(.5,top),xycoords='axes fraction',arrowprops={'arrowstyle':'->','lw':1.7,'color':'#547080'})
fig.suptitle('Full convergent spatial action: proper domains and explicit canonical homotopies',fontsize=17,y=.985)
fig.text(.5,.02,'Proof locators CA.1–CA.4, CA.9–CA.11, CA.22–CA.24, CA.29–CA.35. Cone panel: Im w=Im y=0; time panel: one exact rational sample.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.045,1,.95))
fig.savefig(root/'full-action-domain-and-primitives.png',dpi=160)
fig.savefig(root/'full-action-domain-and-primitives.svg',metadata={'Date':None})
(root/'full-action-domain-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure':'full-action-domain-and-primitives.png','exact_data':'full-action-domain-data.json','checked_same_anchor_identity':True,'bound_length':lbound}))
