"""CC0 independently authored schematic for E07.12--E07.17."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

nu=1.0
epsilon=0.25
radius_squared=2.0
a=nu+epsilon
b=np.linspace(0,radius_squared,801)
v=np.linspace(-nu,nu,801)
B,V=np.meshgrid(b,v)
fig,axes=plt.subplots(1,2,figsize=(12,6),layout='constrained')
mask_a=(V-B<=epsilon)
mask_b=(V-B<=-epsilon)
axes[0].contourf(B,V,mask_a.astype(int),levels=[.5,1.5],colors=['#c8e4fa'])
axes[0].contourf(B,V,mask_b.astype(int),levels=[.5,1.5],colors=['#6a9dc5'],alpha=.8)
for ax in axes:
    ax.plot(b,b+epsilon,color='#1769aa',lw=2,label='A boundary: v = b + e')
    ax.plot(b,b-epsilon,color='#8a3b13',lw=2,label='B boundary: v = b − e')
    ax.set_xlim(0,radius_squared)
    ax.set_ylim(-nu,nu)
    ax.set_xlabel('b = |y|² (negative tangential radius squared)')
    ax.set_ylabel('v = g(n) (normal height)')
    ax.set_xticks([0,epsilon,a,radius_squared],['0','e = ¼','a = 5/4','r² = 2'])
    ax.set_yticks([-nu,-epsilon,0,epsilon,nu],['−ν = −1','−e','0','e','ν = 1'])
    ax.grid(alpha=.2)
axes[0].set_title('Sum pair after collapsing the positive coordinates')
axes[0].annotate('A: v − b ≤ e',xy=(.35,.40),xytext=(.04,.78),fontsize=12,color='#1769aa',arrowprops={'arrowstyle':'->','color':'#1769aa'})
axes[0].text(.65,-.70,'B: v − b ≤ −e',fontsize=12,color='#173a59')
axes[0].text(.08,-.92,'B ⊂ A',fontsize=11,color='white')
axes[1].contourf(B,V,mask_b.astype(int),levels=[.5,1.5],colors=['#dce6ed'])
axes[1].axvspan(a,radius_squared,color='#2b8060',alpha=.30)
axes[1].plot([0,radius_squared],[-nu,-nu],color='#2b8060',lw=6)
axes[1].axvline(a,color='#2b8060',lw=2)
axes[1].text(1.36,.64,'Q: b ≥ a',color='#165c43',fontsize=12)
axes[1].text(.15,-.88,'or v = −ν',color='#165c43',fontsize=12)
for b0,v0 in [(.60,.15),(.20,-.60),(.80,-.35)]:
    # These samples lie where chi is identically zero or identically one.
    chi=0.0 if v0>=-epsilon/4 else 1.0
    time_radius=np.log(a/b0)
    time_bottom=np.inf if chi==0 else v0+nu
    times=np.linspace(0,min(time_radius,time_bottom),120)
    bs=b0*np.exp(times)
    vs=v0-chi*times
    axes[1].plot(bs,vs,color='#8d2c2c',lw=2)
    axes[1].annotate('',xy=(bs[-1],vs[-1]),xytext=(bs[-14],vs[-14]),arrowprops={'arrowstyle':'->','color':'#8d2c2c','lw':2})
axes[1].set_title('Stopped flow retracts B onto the product lower union Q')
axes[1].text(.28,.88,'db/dt = b; dv/dt = −χ(v)',fontsize=11,color='#8d2c2c')
axes[1].text(.25,.71,'Stop at b = a or v = −ν',fontsize=11,color='#8d2c2c')
fig.suptitle('Exact cut equations; ν = 1, e = ¼, r² = 2, a = ν + e = 5/4',fontsize=14)
fig.savefig(Path(__file__).with_name('e07-sum-pair.png'),dpi=160)
fig.savefig(Path(__file__).with_name('e07-sum-pair.svg'))
