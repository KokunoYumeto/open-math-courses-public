"""Reproducible plots of the exact spectral and gauge-model formulas."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'figures'
INK='#173f4a';TEAL='#187c78';BLUE='#445fa6';OCHRE='#a75c18'
def save(fig,name):
 fig.savefig(OUT/(name+'.svg'),metadata={'Date':None},facecolor=fig.get_facecolor())
 fig.savefig(OUT/(name+'.png'),dpi=145,metadata={'Software':'YM-GAUGE reproducible figure'},facecolor=fig.get_facecolor())
 plt.close(fig)
def setup(title,subtitle):
 fig,axes=plt.subplots(1,2,figsize=(11.4,7.8));fig.subplots_adjust(left=.1,right=.96,bottom=.29,top=.76,wspace=.30)
 fig.suptitle(title,fontsize=18,y=.965,weight='bold');fig.text(.08,.865,subtitle,fontsize=12.5)
 for ax in axes:
  ax.grid(alpha=.2)
  for side in ['top','right']:ax.spines[side].set_visible(False)
 return fig,axes
def build():
 OUT.mkdir(exist_ok=True)
 plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'text.color':INK,'axes.labelcolor':INK,'axes.edgecolor':INK,
  'xtick.color':INK,'ytick.color':INK,'svg.hashsalt':'YM-F16-20261010','figure.facecolor':'#fffef9','axes.facecolor':'#fffef9'})
 x=np.linspace(0,4,401);r=(5/3)*np.exp(-3*x);eff=2+3*r/(1+r)
 fig,ax=setup('A correlation detects its positive spectral weights',
  r'Original measure: $\mu=3\delta_{2E_*}+5\delta_{5E_*}$; $E_*>0$, $\hbar>0$ are retained.')
 ax[0].vlines([2,5],0,[3,5],colors=[TEAL,BLUE],lw=3);ax[0].scatter([2,5],[3,5],s=65,c=[TEAL,BLUE])
 for en,wt in [(2,3),(5,5)]:ax[0].text(en+.13,wt-.1,'weight '+str(wt),fontsize=11)
 ax[0].set(xlim=(0,7),ylim=(0,6),xlabel=r'Energy $E/E_*$',ylabel='Original atom weight');ax[0].set_xticks([0,2,5])
 ax[1].plot(x,eff,color=BLUE,lw=2,label=r'$E_{\rm eff}/E_*$');ax[1].axhline(2,color=TEAL,ls='--',label='Threshold 2')
 ax[1].set(xlim=(0,4),ylim=(1.8,4.1),xlabel=r'Physical time $E_*\tau/\hbar$',ylabel=r'Effective energy $E_{\rm eff}/E_*$');ax[1].legend(fontsize=10)
 fig.text(.08,.18,r'$C(\tau)=3e^{-2E_*\tau/\hbar}+5e^{-5E_*\tau/\hbar}$; $E_{\rm eff}=2E_*+3E_*r/(1+r)$.',fontsize=14)
 fig.text(.08,.11,r'$r=(5/3)e^{-3E_*\tau/\hbar}$; the finite-time bias is positive and decreases to zero.',fontsize=12)
 fig.text(.08,.045,'Proof: S.3–S.16 and F16.15. Exact formulas; plotted coordinates are numerical evaluations.',fontsize=11)
 save(fig,'f16-spectral-threshold')
 L=np.arange(1,9);xx=np.linspace(0,6,601);curves={}
 fig,ax=setup('Screening and the source that reaches the ground',
  r'Rotor: $\varepsilon_E=E_*$, $\varepsilon_M=3E_*/2$; $R=La_s$; neutral gap $4E_*$.')
 ax[0].plot(L,L,'o--',color=OCHRE,label='Wilson string')
 ax[0].plot(L,np.minimum(L,3),'s-',color=TEAL,label='Charged ground');ax[0].axhline(3,color=INK,lw=.8,ls=':')
 ax[0].set(xlim=(.7,8.3),ylim=(0,8.7),xlabel=r'Integer separation $L=R/a_s$',ylabel=r'Energy / $E_*$');ax[0].set_xticks(L);ax[0].legend(fontsize=10)
 for eta,col in [(.1,BLUE),(.01,OCHRE)]:
  rr=(1-eta*eta)/(eta*eta)*np.exp(-2*xx);ee=3+2*rr/(1+rr)
  ax[1].plot(xx,ee,color=col,lw=2,label=r'$\eta='+str(eta)+'$')
  cross=np.log((1-eta*eta)/(eta*eta))/2;ax[1].axvline(cross,color=col,lw=.9,ls=':')
  curves[str(eta)]={'effective_energy_over_Estar':ee.tolist(),'crossover_Estar_time_over_hbar':float(cross)}
 ax[1].axhline(3,color=TEAL,ls='--',label='Screened ground')
 ax[1].set(xlim=(0,6),ylim=(2.8,5.2),xlabel=r'Physical time $E_*\tau/\hbar$',ylabel=r'Effective energy / $E_*$');ax[1].legend(fontsize=10)
 fig.text(.08,.18,r'Left: $\min(E_*L,3E_*)$. Right: fixed $L=5$, $E_U=5E_*$, $E_S=3E_*$.',fontsize=14)
 fig.text(.08,.11,'Smaller ground weight delays detection. Dotted vertical lines mark equal contributions.',fontsize=12)
 fig.text(.08,.045,'Proof: W.23–W.29, C.1–C.5. Integer points are the allowed separations; segments guide the eye.',fontsize=11)
 save(fig,'f16-screening-overlap')
 x3=np.linspace(0,12,601);limit=np.ones_like(x3);limit[1:]=-np.expm1(-x3[1:])/x3[1:];riemann={};disappear={}
 fig,ax=setup('Regulator limits retain different spectral information',
  r'Both panels keep physical $E_*>0$, $\hbar>0$; the horizontal coordinate is $E_*\tau/\hbar$.')
 for n,col in [(2,OCHRE),(8,BLUE),(32,TEAL)]:
  cn=np.exp(-np.outer(np.arange(1,n+1)/n,x3)).mean(axis=0)
  ax[0].plot(x3,cn,color=col,lw=1.8,label='$n='+str(n)+'$');riemann[str(n)]=cn.tolist()
 ax[0].plot(x3,limit,color=INK,ls='--',lw=1.8,label='Uniform-measure limit')
 ax[0].set(xlim=(0,12),ylim=(0,1.03),xlabel=r'Physical time $E_*\tau/\hbar$',ylabel=r'Original correlation $C_n(\tau)$');ax[0].legend(fontsize=9)
 for n,col in [(4,OCHRE),(16,BLUE),(64,TEAL)]:
  rr=(n-1)*np.exp(-(1-1/n)*x3);ee=1/n+(1-1/n)*rr/(1+rr)
  ax[1].plot(x3,ee,color=col,lw=1.8,label='$n='+str(n)+'$');ax[1].axhline(1/n,color=col,ls=':',lw=.7);disappear[str(n)]=ee.tolist()
 ax[1].axhline(1,color=INK,ls='--',lw=1.8,label='Limit correlation threshold')
 ax[1].set(xlim=(0,12),ylim=(0,1.05),xlabel=r'Physical time $E_*\tau/\hbar$',ylabel=r'Effective energy / $E_*$');ax[1].legend(fontsize=9)
 fig.text(.08,.18,r'Left: $\mu_n=n^{-1}\sum_{j=1}^n\delta_{jE_*/n}$. Right: $\mu_n=n^{-1}\delta_{E_*/n}+(1-n^{-1})\delta_{E_*}$.',fontsize=12.8)
 fig.text(.08,.11,'Left: all weights reach a continuous gapless measure. Right: the lowest weight disappears.',fontsize=12)
 fig.text(.08,.045,'Proof: R.1–R.10, F16.1–F16.3. Different specified families; both correlations converge uniformly.',fontsize=10.8)
 save(fig,'f16-regulator-measures')
 data={'scope':'Numerical evaluation of exact proved formulas; physical coordinates retain the displayed scale dictionary.',
 'spectral':{'time_Estar_tau_over_hbar':x.tolist(),'energy_over_Estar':[2,5],'original_weights':[3,5],'effective_energy_over_Estar':eff.tolist()},
 'rotor':{'L':L.tolist(),'string_energy_over_Estar':L.tolist(),'ground_energy_over_Estar':np.minimum(L,3).tolist(),'time_Estar_tau_over_hbar':xx.tolist(),'source_curves':curves},
 'regulators':{'time_Estar_tau_over_hbar':x3.tolist(),'uniform_measure_correlation':limit.tolist(),'riemann_correlations':riemann,'disappearing_weight_effective_energies':disappear}}
 (OUT/'f16-figure-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')
if __name__=='__main__':build()
