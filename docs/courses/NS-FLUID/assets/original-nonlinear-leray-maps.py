"""Reproduce proved bounds and exact physical maps; no fluid simulation."""
from pathlib import Path
import json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
navy='#163c61';teal='#008c9e';orange='#c76b19';purple='#8251a8'
def save(fig,stem):
 fig.savefig(OUT/(stem+'.png'),dpi=160,facecolor='white');fig.savefig(OUT/(stem+'.svg'),facecolor='white');plt.close(fig)
j=np.arange(15);error=.2*(3/8)**j
a=.4;c0=.6;A0=.9;K0=.8;tstar=(c0/(2*K0))**(1/a);t=np.geomspace(1e-5,tstar,201)
lower=c0/2*t**(a+.25);upper=A0*t**(a+.25)+K0*t**(2*a+.25);rem=K0*t**(2*a+.25)
fig,ax=plt.subplots(1,2,figsize=(14,6.8));fig.subplots_adjust(left=.07,right=.97,top=.80,bottom=.24,wspace=.28)
fig.suptitle('The constructed correction and the original zero-energy trace',fontsize=20,y=.96)
ax[0].semilogy(j,error,'o-',color=navy,lw=2)
ax[0].set(title='A bound for every original Picard iterate',xlabel='Iteration j',ylabel='Weighted correction error bound')
ax[0].text(.04,.12,r'$\|R-R_j\|_{X_w}\leq\frac{1}{5}(\frac{3}{8})^j$',transform=ax[0].transAxes,color=navy,fontsize=16)
ax[0].grid(alpha=.2);ax[0].set_xticks([0,3,6,9,12,14])
ax[1].loglog(t,upper,color=navy,lw=2,label=r'$A_0t^{a+1/4}+K_0t^{2a+1/4}$')
ax[1].loglog(t,lower,color=teal,lw=2,label=r'$(c_0/2)t^{a+1/4}$')
ax[1].loglog(t,rem,'--',color=orange,lw=2,label=r'$K_0t^{2a+1/4}$ (remainder)')
ax[1].fill_between(t,lower,upper,color=teal,alpha=.10)
ax[1].set(title='Physical separation still tends to zero',xlabel='Original physical time t',ylabel=r'Bounds for the full physical $L^2$ norm')
ax[1].grid(alpha=.2,which='both');ax[1].legend(fontsize=10,loc='upper left')
fig.text(.5,.13,'NL8 proves the left bound. NL9, PP17 and PP27 give the right powers with the full spatial Jacobian.',ha='center',fontsize=11)
fig.text(.5,.084,'Right panel: illustrative a = 0.4, c₀ = 0.6, A₀ = 0.9, K₀ = 0.8; t ≤ (c₀ / 2K₀)^(1/a).',ha='center',fontsize=11)
fig.text(.5,.038,'Curves evaluate proved bounds. No fluid norm or Picard error is numerically measured.',ha='center',fontsize=11)
save(fig,'original-nonlinear-contraction-and-trace')
ell=4.;radius=.8;times=[1.,.25,.0625];colors=[navy,teal,orange]
fig,ax=plt.subplots(1,2,figsize=(14,7.3));fig.subplots_adjust(left=.06,right=.98,top=.79,bottom=.25,wspace=.24)
fig.suptitle('The same original force under the exact parabolic map',fontsize=20,y=.96)
for time,col in zip(times,colors):
 k=math.sqrt(time);ax[0].add_patch(Circle((ell*k,0),radius*k,facecolor=col,edgecolor=col,alpha=.20,lw=2));ax[0].plot(ell*k,0,'o',color=col)
 ax[0].text(ell*k,-radius*k-.18,f't = {time:g}',ha='center',color=col,fontsize=11)
ax[0].axvline(0,color='#777777',lw=1);ax[0].axhline(0,color='#999999',lw=.7)
ax[0].set(xlim=(-.2,5.2),ylim=(-1.3,1.3),aspect='equal',xlabel='Physical cylindrical radius s',ylabel='Physical axial coordinate z',title='Meridional sections of the support enclosure')
ax[0].grid(alpha=.2)
ax[0].text(.02,1.1,r'$(s-\ell\sqrt{t})^2+z^2\leq R^2t$',fontsize=13)
ax[1].axis('off')
rows=[(r'$q=e^{c/2},\quad c\leq0$',navy),
 (r'$(x,t)\longmapsto(qx,q^2t)$',navy),
 (r'$u_c(x,t)=q\,u(qx,q^2t)$',teal),
 (r'$p_c(x,t)=q^2p_0(qx,q^2t)$',teal),
 (r'$q^3 f(qx,q^2t)=f(x,t)$',orange),
 (r'$U_c(\xi,\tau)=U(\xi,\tau+c)$',purple)]
for i,(label,col) in enumerate(rows):ax[1].text(.04,.96-i*.15,label,color=col,fontsize=18,va='top')
fig.text(.5,.17,r'$F=-\frac{\beta}{2}(b+\xi\cdot\nabla b)-\nu\beta\Delta b+\beta^2 b\cdot\nabla b,\qquad f(x,t)=t^{-3/2}F(x/\sqrt{t})$',ha='center',fontsize=15)
fig.text(.5,.095,'The left picture is a section, rotated about s = 0 to give the torus. Illustrative ℓ = 4 and R = 0.8.',ha='center',fontsize=11)
fig.text(.5,.052,'PP7–PP15 and Exercise 3 prove the maps. Support containment is shown; no force field is plotted.',ha='center',fontsize=11)
save(fig,'original-forced-flow-scaling')
data={'scope':'Evaluations of proved bounds and explicit support enclosures; no fluid simulation.',
 'human_source':'Albritton, Brue and Colombo, arXiv:2112.03116v1, main.tex550–593 and2643–2934.',
 'parameters':{'a':a,'c0':c0,'A0':A0,'K0':K0,'t_star':tstar,'ell':ell,'cross_section_radius':radius},
 'picard_bounds':[{'j':int(n),'bound':float(e)} for n,e in zip(j,error)],
 'physical_bounds':[{'t':float(tt),'lower':float(lo),'upper':float(hi),'remainder':float(rr)} for tt,lo,hi,rr in zip(t,lower,upper,rem)],
 'support_sections':[{'t':tt,'center_s':ell*math.sqrt(tt),'radius':radius*math.sqrt(tt),'torus_volume':2*math.pi**2*ell*radius**2*tt**1.5} for tt in times]}
assert np.all(lower<=upper) and np.all(rem<=lower*(1+1e-12))
(OUT/'original-nonlinear-leray-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'bound_samples':len(j)+len(t),'support_sections':len(times),'figures':2}))
