from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE=Path(__file__).resolve().parent
ss=np.linspace(-.4,.4,501)
x=ss**3; z=ss**2; t=-3*ss**5/5
xx=x+z; tt=t-z*z/2
fig=plt.figure(figsize=(15,10),facecolor='white')
gs=fig.add_gridspec(2,2,height_ratios=[1.1,1],hspace=.34,wspace=.26)
ax=fig.add_subplot(gs[0,0]); bx=fig.add_subplot(gs[0,1]); cx=fig.add_subplot(gs[1,:])
for a in (ax,bx):
    a.grid(alpha=.2); a.axhline(0,color='#536173',lw=.8); a.axvline(0,color='#536173',lw=.8)
    a.set_xlabel('x coordinate'); a.set_ylabel('z coordinate')
ax.plot(x,z,color='#1d63a1',lw=3,label='Singular Legendrian: x=s³, z=s²')
ax.plot([0,0],[0,.175],color='#8b3a86',lw=2,ls='--',label='Tangent cone: x=0')
ax.plot([-.17,.01],[.17,-.01],color='#cc792a',lw=2,ls=':',label='Chosen fibre tangent: x+z=0')
ax.scatter([0],[0],color='black',s=30,zorder=5)
ax.set_title('Whole singular germ before the shear (Q.21)',fontsize=13)
ax.set_xlim(-.18,.09); ax.set_ylim(-.015,.19)
ax.legend(loc='upper left',fontsize=10)
bx.plot(xx,z,color='#238b65',lw=3,label="Image: x'=s³+s², z'=s²")
bx.plot([0,0],[-.01,.19],color='#cc792a',lw=2,ls=':',label="New fibre: x'=0")
bx.scatter([0],[0],color='black',s=30,zorder=5)
bx.set_xlabel("x' coordinate"); bx.set_ylabel("z' coordinate")
bx.set_xlim(-.025,.245); bx.set_ylim(-.015,.19)
bx.set_title('After C=1: the local fibre meets only the origin',fontsize=13)
bx.legend(loc='upper left',fontsize=10)
fig.text(.07,.445,'Real-coordinate slice, |s| ≤ 0.4. The theorem concerns the complex germ and all branches.\n'
         "t=−3s⁵/5, t'=t−z²/2; dt+z dx=dt'+z' dx'=0. The other root s=−1 is outside this neighbourhood.",fontsize=11,color='#384657')
cx.set_xlim(0,1); cx.set_ylim(0,1); cx.axis('off')
def box(pos,w,h,text,color):
    xx0,yy0=pos
    cx.add_patch(FancyBboxPatch((xx0,yy0),w,h,boxstyle='round,pad=0.012',fc=color,ec='#465366',lw=1.3))
    cx.text(xx0+w/2,yy0+h/2,text,ha='center',va='center',fontsize=12,linespacing=1.45)
box((.025,.51),.29,.36,'Actual symbols (Q.8)\ncommon coefficient domain\n|pₙ| ≤ B Cₚⁿ n!', '#eaf2fc')
box((.38,.51),.59,.36,'Convergent quantization (Q.9–Q.17)\nT_C = base translation followed by exp(Rₐ)\n|qₙ| ≤ B(Cₚ+L)ⁿ n!;  T₋C T_C = 1\nL = 32(d+1)² max(1,Aₐ) max(1,1/(δε))²','#eaf7ef')
cx.annotate('',xy=(.365,.69),xytext=(.328,.69),arrowprops=dict(arrowstyle='->',lw=2,color='#465366'))
box((.025,.07),.945,.27,'Finite D-type embedding remains open (Q.8)\nSectorial operator action, continuation, separation, infinite-order linearity, finite-pole recovery\nThe contact isomorphism above does not prove those dependencies.','#fff4e5')
cx.annotate('',xy=(.68,.355),xytext=(.68,.49),arrowprops=dict(arrowstyle='->',lw=1.7,ls='--',color='#cc792a'))
fig.suptitle('Generic-position contact reduction with an actual factorial-growth quantization',fontsize=17,y=.98)
fig.text(.07,.012,'Proof locators: Q.2–Q.7. Human context: Kashiwara–Kawai, HolIII (1981), I.6 and IV.1–IV.7, freely available author PDF.\n'
         'This reproducible original figure illustrates proved local maps and the explicitly unproved realization arrow.',fontsize=10,color='#4e5866')
fig.savefig(HERE/'quadratic-contact-shear.png',dpi=160,bbox_inches='tight')
fig.savefig(HERE/'quadratic-contact-shear.svg',bbox_inches='tight')
(HERE/'figure-coordinate-samples.json').write_text(json.dumps({'parameter_interval':[-.4,.4],'sample_count':len(ss),'C':1,'curve':'x=s^3,z=s^2,t=-3s^5/5','x_prime':'s^3+s^2','t_prime':'-3s^5/5-s^4/2','sample_rows':[{'s':float(ss[i]),'x':float(x[i]),'z':float(z[i]),'t':float(t[i]),'x_prime':float(xx[i]),'t_prime':float(tt[i])} for i in (0,125,250,375,500)]},indent=2)+'\n',encoding='utf-8')
print('Rendered quadratic-contact-shear.png and .svg')
