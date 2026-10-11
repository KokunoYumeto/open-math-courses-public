"""Reproducible coordinate and error figures for finite lattice probability."""
from pathlib import Path
import json,math
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
def build():
 OUT.mkdir(exist_ok=True)
 plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'text.color':INK,'axes.labelcolor':INK,'axes.edgecolor':INK,
  'xtick.color':INK,'ytick.color':INK,'svg.hashsalt':'YM-F15-20261010','figure.facecolor':'#fffef9','axes.facecolor':'#fffef9'})
 fig,ax=plt.subplots(figsize=(11.4,8));fig.subplots_adjust(left=.13,right=.91,bottom=.27,top=.77)
 fig.suptitle('From original links to independent plaquettes',fontsize=19,y=.96,weight='bold')
 fig.text(.08,.865,r'Open rectangle: $n_0=2$, $n_1=3$; 12 vertices, 17 links, 11 tree coordinates, 6 plaquettes.',fontsize=13)
 for i in range(3):
  for j in range(3):
   ax.annotate('',xy=(j+1,i),xytext=(j,i),arrowprops={'arrowstyle':'-|>','color':TEAL,'lw':2,'mutation_scale':15,'shrinkA':5,'shrinkB':5})
   ax.text(j+.5,i-.13,'1',color=TEAL,ha='center',va='top')
 for i in range(2):
  for j in range(4):
   color=TEAL if j==0 else BLUE
   ax.annotate('',xy=(j,i+1),xytext=(j,i),arrowprops={'arrowstyle':'-|>','color':color,'lw':2,'mutation_scale':15,'shrinkA':5,'shrinkB':5})
   label='1' if j==0 else r'$V('+str(i)+','+str(j)+')$'
   ax.text(j-.055,i+.5,label,color=color,ha='right',va='center',fontsize=11)
 for i in range(2):
  for j in range(3):ax.text(j+.5,i+.5,r'$P_{'+str(i)+str(j)+'}$',ha='center',va='center',color=OCHRE,fontsize=17)
 for i in range(3):
  for j in range(4):ax.plot(j,i,'o',color=INK,ms=5)
 ax.set_xlim(-.28,3.2);ax.set_ylim(-.27,2.15);ax.set_xticks([0,1,2,3]);ax.set_yticks([0,1,2])
 ax.set_xlabel(r'Spatial vertex index $j$; physical spacing $a_1$',loc='center')
 ax.set_ylabel(r'Time vertex index $i$; spacing $a_0=c\Delta\tau$',loc='center')
 for spine in ax.spines.values():spine.set_visible(False)
 fig.text(.08,.16,r'$P_{ij}=V(i,j+1)^{-1}V(i,j)$, $V(i,0)=1$, $V(i,j)=\prod_{k=0}^{j-1}P_{ik}^{-1}$.',fontsize=15)
 fig.text(.08,.095,'Teal links belong to the tree and become identity after the specified gauge change; their original coordinates remain.',fontsize=11)
 fig.text(.08,.045,'Proof: SC.4–SC.6. Schematic coordinate drawing; the inverse map preserves every original Haar factor.',fontsize=11)
 save(fig,'f15-plaquette-coordinates')
 beta=np.linspace(0,1,501);x=beta*beta/4
 A0=sum(x**k/math.factorial(k)**2 for k in range(21));A1=sum(x**k/(math.factorial(k)*math.factorial(k+1)) for k in range(21))
 r1=beta*A1/(2*A0);p5=beta/2-beta**3/16+beta**5/96
 error=np.abs(r1*r1-p5*p5);bound=beta**8/128
 fig,axes=plt.subplots(1,2,figsize=(11.4,7.5));fig.subplots_adjust(left=.09,right=.96,bottom=.29,top=.77,wspace=.32)
 fig.suptitle('A strong-coupling expansion with its full area error',fontsize=18,y=.96,weight='bold')
 fig.text(.08,.86,r'$r_1(\beta)=I_1(\beta)/I_0(\beta)$; $p_5(\beta)=\beta/2-\beta^3/16+\beta^5/96$; $0\leq\beta\leq1$.',fontsize=13)
 for k,col in [(1,TEAL),(2,BLUE),(4,OCHRE)]:axes[0].plot(beta,r1**k,color=col,lw=2,label='$K='+str(k)+'$')
 axes[0].set_ylabel(r'Exact loop mean $r_1(\beta)^K$',loc='center');axes[0].legend();axes[0].set_ylim(0,.5)
 axes[1].plot(beta,error,color=BLUE,lw=2,label='Series-evaluated absolute error')
 axes[1].plot(beta,bound,color=TEAL,lw=2,ls='--',label=r'Proved bound $\beta^8/128$')
 axes[1].set_ylabel(r'$|r_1(\beta)^2-p_5(\beta)^2|$',loc='center');axes[1].legend(fontsize=9);axes[1].set_ylim(0,.0085)
 for ax in axes:ax.set_xlim(0,1);ax.set_xlabel(r'$\beta$',loc='center');ax.grid(alpha=.2)
 fig.text(.08,.17,r'$|r_1^K-p_5^K|\leq K(\beta/2)^{K-1}\beta^7/128$; right panel: $K=2$.',fontsize=16)
 fig.text(.08,.105,'Both sides retain the loop area count. Refinement at fixed e eventually leaves this strong-coupling interval.',fontsize=12)
 fig.text(.08,.045,'Proof: SC.5 and SC.9–SC.12. Numerical series evaluations; dashed curve is an analytic error bound.',fontsize=11)
 save(fig,'f15-strong-coupling')
 lags=np.arange(0,13);M=np.arange(1,81);rows={}
 fig,axes=plt.subplots(1,2,figsize=(11.4,7.5));fig.subplots_adjust(left=.1,right=.96,bottom=.29,top=.77,wspace=.32)
 fig.suptitle('Update correlation changes while the physical measure stays fixed',fontsize=16.5,y=.96,weight='bold')
 fig.text(.08,.86,r'Original four-link sign model: $\beta=(\log2)/2$, $\pi(u=1)=2/3$, $\pi(u=-1)=1/3$, $v=8/9$.',fontsize=12.5)
 for name,r,col in [('Metropolis',.25,TEAL),('Refresh, probability 1/4',.75,BLUE)]:
  cov=r**lags;infl=np.array([1+2*sum((1-k/m)*r**k for k in range(1,m)) for m in M]);limit=(1+r)/(1-r)
  axes[0].plot(lags,cov,'o-',color=col,lw=1.8,ms=4,label=name)
  axes[1].plot(M,infl,color=col,lw=2,label=name);axes[1].axhline(limit,color=col,ls='--',lw=1)
  rows[name]={'r':r,'covariance_over_v':cov.tolist(),'M_variance_over_v':infl.tolist(),'limit':limit}
 axes[0].set_yscale('log');axes[0].set_xlabel('Attempted-update lag k',loc='center');axes[0].set_ylabel('Covariance / v',loc='center');axes[0].legend(fontsize=9)
 axes[1].set_xlabel('Recorded sample count M',loc='center');axes[1].set_ylabel('M Var(sample mean) / v',loc='center');axes[1].set_ylim(0,7.5)
 for ax in axes:ax.grid(alpha=.2)
 fig.text(.08,.17,r'$M\operatorname{Var}(\widehat m)/v=1+2\sum_{k=1}^{M-1}(1-k/M)r^k$; all finite-count terms are retained.',fontsize=13)
 fig.text(.08,.105,'The limits are 5/3 and 7. These kernels share the intended mean 1/3; accepted-event recording instead gives 1/5.',fontsize=11.5)
 fig.text(.08,.045,'Proof: SC.33, F15.9–F15.10 and Example 2. Update counts are algorithm parameters, not physical time.',fontsize=11)
 save(fig,'f15-update-correlation')
 (OUT/'f15-figure-data.json').write_text(json.dumps({'coordinates':{'n0':2,'n1':3,'vertices':12,'links':17,'tree':11,'plaquettes':6},
  'strong':{'beta':beta.tolist(),'r1_series':r1.tolist(),'p5':p5.tolist(),'K2_absolute_error':error.tolist(),'K2_bound':bound.tolist(),'series_terms':21,'evaluation':'floating-point samples of proved convergent series; analytic remainder is SC.11'},
  'correlation':{'lags':lags.tolist(),'M':M.tolist(),'variance':'8/9','algorithms':rows}},separators=(',',':'))+'\n',encoding='utf8')
if __name__=='__main__':build()
