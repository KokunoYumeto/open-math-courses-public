"""Exact frequency cones and one-sided resolvent profiles; CC0-1.0."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'an04-incoming-boundary-traces-v1','font.size':11})
HERE=Path(__file__).resolve().parent;MOD=HERE.parent
fig,(ax,bx)=plt.subplots(1,2,figsize=(12,5.5),gridspec_kw={'width_ratios':[1.04,1]})
fig.subplots_adjust(left=.065,right=.985,top=.83,bottom=.26,wspace=.3)
rho=np.linspace(-1.18,1.18,600)
ax.fill_between(rho,0,abs(rho)/2,color='#d9ebf2',label=r'Elliptic caps: $|\rho|\geq2|\eta|$')
ax.plot(rho,abs(rho)/2,color='#24667e',lw=1.5)
ax.plot(rho,abs(rho)/4,color='#8b4d21',lw=1.3,ls='--',label=r'Remainder limit: $|\rho|=4|\eta|$')
t=np.linspace(0,np.pi,501)
ax.plot(np.cos(t),np.sin(t),color='#1a3148',lw=2)
ax.scatter([-1,1,0],[0,0,1],s=35,color=['#8b4d21','#8b4d21','#1a3148'],zorder=4,clip_on=False)
ax.annotate('Glancing direction\n(0, 1)',xy=(0,1),xytext=(0,.7),ha='center',arrowprops={'arrowstyle':'->','color':'#1a3148'})
ax.text(-1,-.13,'(−1, 0)',ha='center');ax.text(1,-.13,'(1, 0)',ha='center')
ax.set(xlim=(-1.18,1.18),ylim=(0,1.1),xlabel=r'Normal frequency $\rho$',ylabel=r'Tangential magnitude $|\eta|$')
ax.set_title('Separate the pure normal directions',pad=16,fontweight='bold')
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.25),fontsize=9,frameon=False)
ax.grid(alpha=.16)
u=np.linspace(0,3,501)
bx.plot(u,.5*np.exp(-u),color='#1a3148',lw=2.4,label=r'$\lambda=1$: both magnitudes')
bx.plot(u,np.exp(-4*u)/8,color='#aa6229',lw=2,label=r'$\lambda=4$: $|k_0|=e^{-4u}/8$')
bx.plot(u,np.exp(-4*u)/2,color='#247b78',lw=2,ls='--',label=r'$\lambda=4$: $|k_1|=e^{-4u}/2$')
bx.set(xlim=(0,3),ylim=(0,.55),xlabel=r'Input distance $u>0$',ylabel='Kernel magnitude')
bx.set_title('Both boundary kernels are in L²',pad=16,fontweight='bold')
bx.grid(alpha=.16)
bx.legend(loc='upper right',fontsize=9,frameon=False)
bx.text(1.02,.31,r'$\|k_0\|_2^2=1/(8\lambda^3)$'+'\n'+r'$\|k_1\|_2^2=1/(8\lambda)$',fontsize=12)
fig.suptitle('Incoming boundary traces: elliptic caps and normal-profile scaling',y=.98,fontsize=15,fontweight='bold')
out=HERE/'incoming-traces.svg'
fig.savefig(out,metadata={'Date':None});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/incoming-traces.svg','svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),
 'exact_geometry':{'frequency_projection':['rho','absolute eta'],'unit_section':'rho^2+|eta|^2=1','cap_boundary':'|rho|=2|eta|','remainder_limit':'|rho|=4|eta|','model_ellipticity_constant':'3/5','pure_normal_points':[[-1,0],[1,0]],'glancing_point':[0,1]},
 'profiles':{'lambda':[1,4],'u_interval':[0,3],'value':'exp(-lambda*u)/(2*lambda)','normal_derivative':'-i*exp(-lambda*u)/2','squared_L2_norms':['1/(8*lambda^3)','1/(8*lambda)']},
 'positive_resolvent_is_not_the_full_wave_inverse':True,'actually_inspected':False,'exact_coordinate_review_complete':False}
(MOD/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'svg':str(out),'sha256':sha(out)}))
