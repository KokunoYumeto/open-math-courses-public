"""Reproducible figures for the exact finite lattice constructions."""
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
def build():
 OUT.mkdir(exist_ok=True)
 plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'text.color':INK,'axes.labelcolor':INK,'axes.edgecolor':INK,
  'xtick.color':INK,'ytick.color':INK,'svg.hashsalt':'YM-F14-20261010','figure.facecolor':'#fffef9','axes.facecolor':'#fffef9'})
 fig,ax=plt.subplots(figsize=(11.4,8));fig.subplots_adjust(left=.1,right=.9,bottom=.25,top=.76)
 fig.suptitle('A plaquette is a composed transport map',fontsize=19,y=.96,weight='bold')
 fig.text(.07,.865,r'Path order: $+\mu,\ +\nu,\ -\mu,\ -\nu$.  Matrix multiplication acts from the right.',fontsize=14)
 points=[(0,0),(4,0),(4,2.3),(0,2.3)]
 for i,(a,b) in enumerate(zip(points,points[1:]+points[:1])):
  ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'-|>','color':TEAL,'lw':2.5,'mutation_scale':18,'shrinkA':8,'shrinkB':8})
 ax.scatter(*zip(*points),s=65,color=INK,zorder=3)
 for (x,y),label,dy in zip(points,[r'$x$',r'$x+a_\mu\hat\mu$',r'$x+a_\mu\hat\mu+a_\nu\hat\nu$',r'$x+a_\nu\hat\nu$'],[-.43,-.43,.22,.22]):ax.text(x,y+dy,label,ha='center',fontsize=14)
 ax.text(2,.22,r'$U_\mu(x)$',ha='center',fontsize=15)
 ax.text(2,2.01,r'$U_\mu(x+a_\nu\hat\nu)^{-1}$',ha='center',fontsize=15)
 ax.text(4.18,1.15,r'$U_\nu(x+a_\mu\hat\mu)$',ha='left',va='center',fontsize=13)
 ax.text(-.18,1.15,r'$U_\nu(x)^{-1}$',ha='right',va='center',fontsize=13)
 ax.set_xlim(-1.35,6.2);ax.set_ylim(-.65,3);ax.set_axis_off()
 fig.text(.07,.18,r'$P_{\mu\nu}(x)=U_\nu(x)^{-1}U_\mu(x+a_\nu\hat\nu)^{-1}U_\nu(x+a_\mu\hat\mu)U_\mu(x)$.',fontsize=15)
 fig.text(.07,.105,r'$P^h=h_x P h_x^{-1}$; $W(P)=N-\operatorname{Re}\operatorname{tr}P=\frac{1}{2}\|I-P\|_{\rm HS}^2$.',fontsize=15)
 fig.text(.07,.045,'Proof: L.1–L.6. Schematic coordinate face; drawn lengths and aspect ratio do not fix the physical spacings.',fontsize=11)
 save(fig,'f14-plaquette')
 n=np.arange(2,17);vals=8*n.astype(float)**4*np.sin(1/(2*n))**4;lower=.5*(1-1/(6*n*n))
 fig,ax=plt.subplots(figsize=(11.4,7.5));fig.subplots_adjust(left=.12,right=.94,bottom=.29,top=.78)
 fig.suptitle('An exact non-Abelian lattice action approaches its limit',fontsize=18,y=.96,weight='bold')
 fig.text(.08,.86,r'$A_1=T_1/L_*,\ A_2=T_2/L_*,\ L_1=L_2=L_*,\ a_1=a_2=L_*/n$; integer $n\geq2$.',fontsize=13)
 ax.scatter(n,vals,color=BLUE,s=45,label='Exact lattice action',zorder=3)
 ax.scatter(n,lower,color=TEAL,s=38,marker='_',label='Proved lower bound',zorder=3)
 for x,y in zip(n,lower):ax.plot([x,x],[y,.5],color=TEAL,alpha=.25)
 ax.axhline(.5,color=OCHRE,label='Original continuum action',lw=1.5)
 ax.set_xlim(1.5,16.5);ax.set_ylim(.478,.502);ax.set_xticks([2,4,6,8,10,12,14,16]);ax.grid(alpha=.18)
 ax.set_xlabel(r'Integer mesh count $n$',loc='center');ax.set_ylabel(r'$S/Q$',loc='center');ax.legend(loc='lower right',fontsize=11)
 fig.text(.08,.17,r'$Q=\hbar\operatorname{Vol}/(g_{\rm YM}^2L_*^4)$, $S_E=Q/2$, $S_a=8Qn^4\sin^4(1/(2n))$.',fontsize=14)
 fig.text(.08,.105,r'$0\leq S_E-S_a\leq S_E/(6n^2)$. Vertical intervals show the proved action bounds.',fontsize=13)
 fig.text(.08,.045,'Proof: F14.2–F14.4. Original torus, connection and coupling fixed; exact formulas sampled at integer meshes.',fontsize=11)
 save(fig,'f14-action-error')
 beta=np.linspace(.15,2.2,501);q=np.exp(-2*beta);lam0=(1+q)/2;lam1=(1-q)/2;gap=np.log(lam0/lam1)
 fig,axes=plt.subplots(1,2,figsize=(11.4,7.5));fig.subplots_adjust(left=.09,right=.96,bottom=.3,top=.77,wspace=.32)
 fig.suptitle('A positive gap at every fixed regulator',fontsize=19,y=.96,weight='bold')
 fig.text(.08,.86,r'$G=\{1,-1\}$, one loop edge, no spatial potential; fixed $\Delta\tau>0$ and $\hbar>0$.',fontsize=13)
 ax=axes[0];ax.plot(beta,lam0,color=TEAL,lw=2,label=r'$\lambda_0=(1+e^{-2\beta})/2$');ax.plot(beta,lam1,color=BLUE,lw=2,label=r'$\lambda_1=(1-e^{-2\beta})/2$')
 ax.set_ylim(0,1);ax.set_ylabel('Transfer eigenvalue',loc='center');ax.legend(fontsize=10)
 ax=axes[1];ax.plot(beta,gap,color=OCHRE,lw=2);ax.set_ylim(0,2);ax.set_ylabel(r'$\Delta\tau\,\Delta E/\hbar$',loc='center')
 for ax in axes:ax.set_xlabel(r'$\beta$',loc='center');ax.grid(alpha=.2);ax.set_xlim(.15,2.2)
 fig.text(.08,.18,r'$\Delta E=(\hbar/\Delta\tau)\log[(1+e^{-2\beta})/(1-e^{-2\beta})]>0$.',fontsize=16)
 fig.text(.08,.11,r'As $\beta\to\infty$, $\lambda_0,\lambda_1\to1/2$ and $\Delta E\to0$. All partition factors are retained.',fontsize=12)
 fig.text(.08,.045,'Proof: F14.5–F14.7. This varies a parameter of the specified finite model; no spacetime limit is taken.',fontsize=11)
 save(fig,'f14-transfer-spectrum')
 (OUT/'f14-figure-data.json').write_text(json.dumps({'plaquette':{'kind':'schematic coordinate face','path':['+mu','+nu','-mu','-nu'],'proof':'L.1–L.6'},
  'action':{'n':n.tolist(),'S_a_over_Q':vals.tolist(),'lower_over_Q':lower.tolist(),'S_E_over_Q':.5,'Q':'hbar Vol/(gYM² Lstar⁴)'},
  'transfer':{'beta':beta.tolist(),'lambda0':lam0.tolist(),'lambda1':lam1.tolist(),'energy_gap_times_dt_over_hbar':gap.tolist()}},separators=(',',':'))+'\n',encoding='utf8')
if __name__=='__main__':build()
