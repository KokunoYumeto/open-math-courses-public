"""Reproducible diagrams of the specified reconstruction and limit maps."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'figures'
INK='#173f4a';TEAL='#187c78';BLUE='#445fa6';OCHRE='#a75c18'

def save(fig,name):
 fig.savefig(OUT/(name+'.svg'),metadata={'Date':None},facecolor=fig.get_facecolor())
 fig.savefig(OUT/(name+'.png'),dpi=145,metadata={'Software':'YM-GAUGE reproducible figure'},facecolor=fig.get_facecolor())
 plt.close(fig)

def setup(title,subtitle):
 fig,axes=plt.subplots(1,2,figsize=(11.4,7.8))
 fig.subplots_adjust(left=.1,right=.96,bottom=.29,top=.76,wspace=.32)
 fig.suptitle(title,fontsize=18,y=.965,weight='bold')
 fig.text(.08,.865,subtitle,fontsize=12.5)
 for ax in axes:
  ax.grid(alpha=.2)
  for side in ['top','right']:ax.spines[side].set_visible(False)
 return fig,axes

def build():
 OUT.mkdir(exist_ok=True)
 plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'text.color':INK,'axes.labelcolor':INK,
 'axes.edgecolor':INK,'xtick.color':INK,'ytick.color':INK,'svg.hashsalt':'YM-F17-20261010',
 'figure.facecolor':'#fffef9','axes.facecolor':'#fffef9'})
 z=np.linspace(-1.8,1.8,241);x,y=np.meshgrid(z,z)
 ordinary=x*x+x*y+y*y;reflected=(x/2+y/4)**2
 fig,ax=setup('The reflection quotient changes the state norm',
  r'$F=xX_1+yX_2$; $\tau_1=\log2/\omega$, $\tau_2=2\log2/\omega$, $A=\hbar/(2\alpha\omega)$.')
 contour0=ax[0].contour(x,y,ordinary,levels=[.25,.5,1,2,3],colors=TEAL)
 contour1=ax[1].contour(x,y,reflected,levels=[.05,.15,.3,.6],colors=BLUE)
 ax[0].clabel(contour0,inline=True,fontsize=8)
 ax[1].clabel(contour1,inline=True,fontsize=8)
 for a in ax:
  a.set(xlim=(-1.8,1.8),ylim=(-1.8,1.8),xlabel=r'Coefficient $x$',ylabel=r'Coefficient $y$')
  a.set_aspect('equal')
 ax[0].set_title(r'Ordinary norm$^2/A=x^2+xy+y^2$',fontsize=11)
 ax[1].set_title(r'Reflection norm$^2/A=(x/2+y/4)^2$',fontsize=11)
 ax[1].plot(z/2,-z,color=OCHRE,lw=2,label=r'Null line $y=-2x$')
 ax[1].scatter([.75],[-1.5],color=OCHRE,s=40)
 ax[1].annotate(r'$(3/4,-3/2)$',(.75,-1.5),xytext=(-1.6,-1.1),fontsize=10,
                arrowprops={'arrowstyle':'->','color':OCHRE})
 fig.text(.08,.18,r'The original covariance is positive definite; the reflection form has a null direction.',fontsize=13)
 fig.text(.08,.11,r'$X_1-2X_2$ maps to zero, but $(X_1-2X_2)X_2$ maps to $-3A\Omega/2$.',fontsize=13)
 fig.text(.08,.045,'Proof: CR.16–CR.23, F17.2–F17.3. Contours show the exact quadratic forms.',fontsize=11)
 save(fig,'f17-reflection-quotient')

 lam=np.linspace(1,16,301);values={}
 fig,ax=setup('The zero coordinate selects the limiting state',
  r'$L_j=\lambda\ell_j$, $\mu_\lambda=\mu_*/\lambda^p$, $b=1/(4V_\ell\mu_*)$, $\tau=1/(c\mu_*)$.')
 for p,col in [(1,TEAL),(3,BLUE),(5,OCHRE)]:
  curve=lam**(p-3)*np.exp(-lam**(-float(p)));values[str(p)]=curve.tolist()
  ax[0].plot(lam,curve,color=col,lw=2,label='$p='+str(p)+'$')
 ax[0].set(xlabel=r'Box scale $\lambda$',ylabel=r'Zero covariance $C_{\lambda,0}/b$',
           xlim=(1,16),yscale='log',ylim=(.002,300))
 ax[0].axhline(1,color=INK,ls=':',lw=.8);ax[0].legend(fontsize=10)
 ax[1].axis('off')
 boxes=[(.04,.75,.9,.2,r'Box coordinate $e_0$',r'Energy $\hbar c\mu_*/\lambda^3$'),
        (.04,.40,.9,.2,r'$J_\lambda e_0=\delta_\lambda^{-1/2}1_{Q_{\lambda,0}}$',r'Weak limit $0$; norm survives'),
        (.04,.05,.9,.2,r'Augmented map: $e_0\mapsto(0,1)$',r'Field limit $\sqrt{b}\int f$; energy $0$')]
 for xx,yy,ww,hh,title,sub in boxes:
  ax[1].add_patch(plt.Rectangle((xx,yy),ww,hh,transform=ax[1].transAxes,fill=False,lw=1.4,color=INK))
  ax[1].text(xx+ww/2,yy+.13,title,ha='center',va='center',transform=ax[1].transAxes,fontsize=10.5)
  ax[1].text(xx+ww/2,yy+.055,sub,ha='center',va='center',transform=ax[1].transAxes,fontsize=10)
 fig.text(.08,.18,r'$C_{\lambda,0}(\tau)=b\lambda^{p-3}\exp(-c\mu_*\tau/\lambda^p)$; no zero coordinate is discarded.',fontsize=13)
 fig.text(.08,.11,'At p = 3 the limit contains an independent constant Gaussian field; clustering fails.',fontsize=12)
 fig.text(.08,.045,'Proof: CR.10–CR.15, CR.36–CR.39 and F17.4. Curves evaluate the exact formula.',fontsize=11)
 save(fig,'f17-zero-coordinate')

 nodes,weights=np.polynomial.legendre.leggauss(256);u=(nodes+1)/2;weights=weights/2
 time=np.linspace(0,30,1001)
 cutoff=(2/np.pi)*(np.cos(np.outer(time,u))@(weights/(1+u*u)))
 full=np.exp(-time);star=15*np.pi/2;bound=-2*(15*np.pi-32)/(225*np.pi**3)
 fig,ax=setup('An ordinary positive cutoff can fail reflection positivity',
  r'$R=\omega>0$; $A=\hbar/(2\alpha\omega)$; plotted time is the physical product $\omega s$.')
 for a in ax:
  a.plot(time,cutoff,color=BLUE,lw=1.8,label=r'$D_\omega(s)/A$')
  a.plot(time,full,color=TEAL,lw=1.5,ls='--',label=r'$e^{-\omega s}$')
  a.axhline(0,color=INK,lw=.8);a.set(xlabel=r'Physical time $\omega s$',ylabel=r'Covariance / $A$')
 ax[0].set(xlim=(0,30),ylim=(-.15,1.03));ax[0].legend(fontsize=10)
 ax[1].set(xlim=(20,26),ylim=(-.025,.025));ax[1].axvline(star,color=OCHRE,ls=':',lw=1)
 ax[1].scatter([star],[bound],color=OCHRE,s=40,zorder=5,label='Proved negative upper bound')
 ax[1].legend(fontsize=9,loc='upper center')
 fig.text(.08,.18,r'At $s_*=15\pi/(2\omega)$, $D_\omega(s_*)/A\leq-2(15\pi-32)/(225\pi^3)<0$.',fontsize=13)
 fig.text(.08,.11,r'A unit-integral test within $1/(1000\omega)$ of $s_*/2$ retains a negative reflection form.',fontsize=11.5)
 fig.text(.08,.045,'Proof: CR.33–CR.34, F17.5–F17.6. Curves: 256-node quadrature; the sign bound is analytical.',fontsize=10.8)
 save(fig,'f17-cutoff-positivity')
 data={'scope':'Plots of fully specified original objects; scale ratios label axes, and do not replace the working formulas.',
 'reflection':{'ordinary_covariance_over_A':[[1,.5],[.5,1]],'reflection_covariance_over_A':[[.25,.125],[.125,.0625]],
 'times':['log(2)/omega','2log(2)/omega'],'original_A':'hbar/(2 alpha omega)'},
 'zero_mode':{'lambda':lam.tolist(),'physical_time':'1/(c mu_star)','original_b':'1/(4 V_ell mu_star)','Czero_over_b':values},
 'cutoff':{'omega_s':time.tolist(),'D_over_A':cutoff.tolist(),'full_over_A':full.tolist(),
 'bound_time_omega_s':float(star),'proved_bound_over_A':float(bound),'quadrature_nodes':256}}
 (OUT/'f17-figure-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')
if __name__=='__main__':build()
