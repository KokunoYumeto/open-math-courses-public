"""Exact M3 frequency, filter, product and modular-band illustration."""
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':14,'svg.hashsalt':'oa-flow-arveson-real-20261004'})
fig,axs=plt.subplots(2,2,figsize=(15,10),facecolor='#f6f8fb')
fig.subplots_adjust(left=.07,right=.96,bottom=.20,top=.82,hspace=.80,wspace=.27)
a=np.array([2.,0.,-1.]);freq=a[:,None]-a[None,:]
ax=axs[0,0];ax.imshow(freq,cmap='RdBu_r',norm=TwoSlopeNorm(vmin=-3,vcenter=0,vmax=3))
for i in range(3):
 for j in range(3):ax.text(j,i,str(int(freq[i,j])),ha='center',va='center',color='white' if abs(freq[i,j])>=2 else '#20354f',fontsize=20)
ax.set_xticks(range(3),['1','2','3']);ax.set_yticks(range(3),['1','2','3']);ax.set_xlabel('column $j$');ax.set_ylabel('row $i$')
ax.set_title(r'A. Exact frequencies $r_{ij}=a_i-a_j$',loc='left',pad=14)
ax.text(.5,-.38,r'$a=(2,0,-1)$,  $\alpha_t(E_{ij})=e^{itr_{ij}}E_{ij}$',transform=ax.transAxes,ha='center')
ax=axs[0,1];r=np.linspace(-3.5,3.5,1501);s=(r-2)/.4;b=np.zeros_like(r);inside=np.abs(s)<1;b[inside]=np.exp(1-1/(1-s[inside]**2))
ax.plot(r,b,color='#147b9c',lw=2.8);ax.fill_between(r,b,color='#65b6ce',alpha=.2)
ax.scatter([-3,1,2],[0,0,1],color=['#657086','#657086','#bb5365'],s=48,zorder=4)
for rr,yy,label in [(-3,0,r'$E_{31}$'),(1,0,r'$E_{23}$'),(2,1,r'$E_{12}$')]:ax.annotate(label,(rr,yy),xytext=(5,10 if yy==0 else -20),textcoords='offset points')
ax.axvline(1.6,color='#657086',ls=':',lw=1);ax.axvline(2.4,color='#657086',ls=':',lw=1)
ax.set(xlim=(-3.5,3.5),ylim=(-.08,1.15),xlabel='additive frequency $r$',ylabel=r'$\chi(r)$')
ax.set_title('B. One smooth window detects a nonzero term',loc='left',pad=14);ax.grid(alpha=.15)
ax.text(.5,-.38,r'$T_{k_\chi}(E_{12}+E_{23}+E_{31})=E_{12}$',transform=ax.transAxes,ha='center')
ax=axs[1,0]
for row,(lo,hi,point,label,c) in enumerate([(1.6,2.4,2,r'$x=E_{12}$','#147b9c'),(.7,1.3,1,r'$y=E_{23}$','#a87439'),(2.3,3.7,3,r'$xy=E_{13}$','#bb5365')]):
 yy=2-row;ax.plot([lo,hi],[yy,yy],lw=13,color=c,alpha=.2,solid_capstyle='butt');ax.scatter([point],[yy],s=65,color=c,zorder=3);ax.text(4,yy,label,va='center',fontsize=12)
 ax.text((lo+hi)/2,yy+.22,f'[{lo:g}, {hi:g}]',ha='center',color=c)
ax.set(xlim=(0,5),ylim=(-.45,2.55),xlabel='additive frequency $r$');ax.set_yticks([]);ax.set_xticks([0,1,2,3,4]);ax.grid(axis='x',alpha=.2)
ax.set_title('C. Products add frequencies: $2+1=3$',loc='left',pad=14)
ax.text(.5,-.40,'Dots: actual singleton spectra. Bars: containing windows.\n$[1.6,2.4]+[0.7,1.3]=[2.3,3.7]$.',transform=ax.transAxes,ha='center',fontsize=10.5)
ax=axs[1,1];r=np.linspace(-2,2,501);v=np.abs(np.exp(r/2)-1);bound=np.e-1
ax.plot(r,v,color='#147b9c',lw=2.8,label=r'$|e^{r/2}-1|$');ax.axhline(bound,color='#bb5365',ls='--',lw=2,label=r'$e^{h/2}-1=e-1$,  $h=2$')
ax.scatter([2],[bound],color='#bb5365',s=55,zorder=4);ax.set(xlim=(-2.1,2.1),ylim=(0,1.95),xlabel=r'$r=\log\lambda$',ylabel='spectral multiplier magnitude')
ax.set_xticks([-2,-1,0,1,2]);ax.grid(alpha=.15);ax.legend(loc='upper left',fontsize=10);ax.set_title('D. The full modular square-root band bound',loc='left',pad=14)
ax.text(.5,-.40,r'$D=\mathrm{diag}(e^2,1,e^{-1})/Z$,  $\xi=D^{1/2}$.'+'\n'+r'For $x=E_{12}$: $\|(1-\Delta^{1/2})x\xi\|=(e-1)\|x\xi\|$.',transform=ax.transAxes,ha='center',fontsize=10.5)
fig.suptitle('Real-action spectral localization: signs, products and vector domains',fontsize=20,color='#20354f',y=.96)
fig.text(.07,.90,'Exact finite-matrix examples of RF1, AL9–11, AL16 and AL19–22. They do not satisfy the full-corner-spectrum hypothesis AL23.',fontsize=11,color='#546178')
fig.savefig(HERE/'assets/arveson-real.png',dpi=160,facecolor=fig.get_facecolor())
fig.savefig(HERE/'assets/arveson-real.svg',facecolor=fig.get_facecolor(),metadata={'Date':None})
svg=HERE/'assets/arveson-real.svg';svg.write_text(svg.read_text(encoding='utf-8'),encoding='utf-8',newline='\n')
E=lambda i,j:np.outer(np.eye(3)[i],np.eye(3)[j])
x,y=E(0,1),E(1,2);d=np.exp(a);d/=sum(d);root=np.diag(np.sqrt(d));v=x@root;right=root@x
checks={'frequencies':freq.tolist(),'product_E12_E23_E13':bool(np.array_equal(x@y,E(0,2))),'adjoint_frequency':float(freq[1,0]),'window_sum':[1.6+.7,2.4+1.3],'faithful_density':d.tolist(),'commutator_norm_squared':float(np.linalg.norm(v-right)**2),'sharp_bound_squared':float((np.e-1)**2*np.linalg.norm(v)**2),'modular_bound_sample_check':bool(np.all(np.abs(np.exp(r/2)-1)<=bound+1e-12)),'scope':'Numerical checks of exact caption formulas only; general claims have complete RF/AL proofs'}
(HERE/'FIGURE_NUMERICAL_CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(checks,indent=2))
