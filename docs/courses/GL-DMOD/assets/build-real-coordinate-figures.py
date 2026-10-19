"""Reproduce exact coordinate support slices and certified rational coefficient plots."""
from pathlib import Path
from fractions import Fraction
from math import factorial
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np

parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,default=Path(__file__).parent)
out=parser.parse_args().output_dir;out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.hashsalt':'GL-DMOD-BCT-exact-coordinate-maps-v1'})
ink,blue,green,muted='#152640','#155ca5','#17765d','#52627a'

def save(fig,name):
 fig.savefig(out/(name+'.png'),dpi=150,facecolor=fig.get_facecolor())
 fig.savefig(out/(name+'.svg'),metadata={'Date':None})
 plt.close(fig)

def arrow(fig,p,q,label=None):
 a=FancyArrowPatch(p,q,transform=fig.transFigure,arrowstyle='-|>',mutation_scale=20,lw=1.7,color=blue)
 fig.add_artist(a)
 if label:fig.text((p[0]+q[0])/2,(p[1]+q[1])/2+.018,label,ha='center',va='bottom',fontsize=20,color=blue)

f=plt.figure(figsize=(16,10),dpi=150,facecolor='#f7f9fc')
f.text(.5,.95,'Ordinary coordinates transport the whole real-kernel ring',ha='center',fontsize=24,color=ink)
f.text(.5,.898,r"$F_\varphi(t,x)=(t-x^2/2,x),\quad (\tau',z')=(\tau,z+x),\quad j_F=1$",ha='center',fontsize=19,color=muted)
ax=f.add_axes([.08,.49,.35,.31]);x=np.linspace(-.65,.65,401);t=x*x/2
ax.fill_between(x,-.25,t,color='#d8eee6');ax.plot(x,t,color=green,lw=2)
ax.axhline(0,color=muted,lw=1,ls=':');ax.set(xlim=(-.65,.65),ylim=(-.25,.30),xlabel=r'$x$ (real)',ylabel=r'$t$ (real)',title=r'Pulled-back halfspace: $t<x^2/2$')
ax.text(-.53,-.17,r'$\Re(t-\varphi(x))<0$',color=green,fontsize=17)
ax.text(.08,.07,r"$t'=0$",color=green,fontsize=16);ax.grid(alpha=.16)
ax=f.add_axes([.56,.49,.36,.31]);z=np.linspace(-.5,.5,401);curved=z*z/2-np.abs(z);linear=-.75*np.abs(z)
ax.fill_between(z,-.65,linear,color='#e3e9f2');ax.fill_between(z,-.65,curved,color='#c8e7dc')
ax.plot(z,linear,color=blue,lw=2,ls='--',label=r'$w=-3|\zeta|/4$')
ax.plot(z,curved,color=green,lw=2,label=r'$w=\zeta^2/2-|\zeta|$')
ax.scatter([-.5,0,.5],[-.375,0,-.375],s=25,color=ink,zorder=4)
ax.set(xlim=(-.5,.5),ylim=(-.65,.10),xlabel=r'$\zeta$ (real)',ylabel=r'$w$ (real)',title=r'Normal slice at $u=0$, $|\zeta|\leq1/2$')
ax.text(-.43,-.58,r'$-w\geq3|(w,\zeta)|/5$',fontsize=16,color=green)
ax.legend(loc='lower center',bbox_to_anchor=(.5,-.49),ncol=1,fontsize=12,frameon=False);ax.grid(alpha=.16)
f.text(.26,.395,'Full support proof: BCT.4–BCT.7\nExact slice: BCT.45–BCT.47',ha='center',fontsize=14,color=muted,linespacing=1.45)
for xx,yy,label in [(.25,.29,r"$B'\otimes_{E'}M' $"),(.75,.29,r"$C'\otimes_{E'}M' $"),(.25,.13,r"$B\otimes_E M$"),(.75,.13,r"$C\otimes_E M$")]:
 f.text(xx,yy,label,ha='center',va='center',fontsize=25,color=ink)
arrow(f,(.39,.29),(.61,.29),r"$\eta_{M'}$");arrow(f,(.39,.13),(.61,.13),r"$\eta_M$")
arrow(f,(.25,.25),(.25,.17));arrow(f,(.75,.25),(.75,.17))
f.text(.28,.21,r'$\Psi_B\;\cong$',va='center',fontsize=20,color=green);f.text(.78,.21,r'$\Psi_C\;\cong$',va='center',fontsize=20,color=green)
f.text(.5,.045,r"$\Psi_C\eta_{M'}=\eta_M\Psi_B$  for the whole module.  [BCT.33–BCT.35]",ha='center',fontsize=18,color=green)
save(f,'real-coordinate-supports-and-comparison')

def term(j,k):return Fraction(factorial(2*k),2**k*factorial(k)*factorial(j+k)**2)
def pair(q):return {'numerator':str(q.numerator),'denominator':str(q.denominator)}
coefficients=[]
for j in range(-4,5):
 lower=sum((term(j,k) for k in range(max(0,-j),25)),Fraction())
 tail=2*term(j,25);coefficients.append({'j':j,'R':24,'lower':pair(lower),'tail_bound':pair(tail),'upper':pair(lower+tail)})
f=plt.figure(figsize=(16,10),dpi=150,facecolor='#f7f9fc')
f.text(.5,.95,'A positive head produces every negative output degree',ha='center',fontsize=24,color=ink)
f.text(.5,.89,r'$P=\left(\sum_{m\geq0}\tau^m/(m!)^2\right)(1-z)^{-1},\quad \varphi(x)=x^2/2$',ha='center',fontsize=20,color=muted)
ax=f.add_axes([.09,.36,.37,.43]);js=[r['j'] for r in coefficients]
values=[Fraction(int(r['lower']['numerator']),int(r['lower']['denominator'])) for r in coefficients]
tails=[Fraction(int(r['tail_bound']['numerator']),int(r['tail_bound']['denominator'])) for r in coefficients]
ax.axvspan(-4.5,-.5,color='#d8eee6',alpha=.8)
ax.errorbar(js,[float(v) for v in values],yerr=[[0]*9,[float(v) for v in tails]],fmt='o',color=blue,ecolor=green,capsize=6,ms=7)
ax.set(yscale='log',xlim=(-4.5,4.5),xticks=js,xlabel=r'Output homogeneous degree $j$',ylabel='Coefficient enclosure (log scale)',title=r'Exact lower sums $S_{j,24}$ and certified upper tails')
ax.text(.02,.04,'Negative outputs are all nonzero.',transform=ax.transAxes,color=green,fontsize=14);ax.grid(alpha=.18)
ax=f.add_axes([.56,.36,.36,.43]);ratios=[]
for j,color in [(-4,green),(0,blue),(4,'#a75227')]:
 ks=list(range(max(0,-j),29));rr=[Fraction(2*k+1,(j+k+1)**2) for k in ks]
 ax.plot(ks,[float(v) for v in rr],color=color,lw=2,label=f'j={j}')
 ratios.append({'j':j,'points':[{'K':k,'ratio':pair(v)} for k,v in zip(ks,rr)]})
ax.axvspan(14,28,color='#d8eee6',alpha=.6);ax.axhline(.5,color=muted,ls='--',lw=1.5)
ax.axvline(24,color=muted,ls=':',lw=1.2);ax.text(24.25,.033,'R=24',color=muted,fontsize=12)
ax.set(yscale='log',xlim=(0,28),ylim=(.025,12),xlabel=r'Summand index $K$',ylabel='Exact successive-term ratio',title=r'$b_{j,K+1}/b_{j,K}=(2K+1)/(j+K+1)^2$')
ax.legend(loc='upper right',frameon=False);ax.grid(alpha=.18)
f.text(.5,.235,r'$q_j(0)=\sum_{K\geq\max(0,-j)}(2K)!\,/\,[2^K K!(j+K)!^2]$',ha='center',fontsize=22,color=ink)
f.text(.5,.155,r'$S_{j,24}<q_j(0)\leq S_{j,24}+2b_{j,25}\quad(-4\leq j\leq4)$',ha='center',fontsize=21,color=green)
f.text(.5,.085,'BCT.39–BCT.43 prove every index and the exact tail bound. Error bars are narrower than the markers at this scale.',ha='center',fontsize=14,color=muted)
f.text(.5,.04,'Data retain exact rational numerators and denominators; plotted coordinates are numerical.',ha='center',fontsize=14,color=muted)
save(f,'full-positive-time-shift-calibration')
data={'kind':'Exact mathematical support slices, module maps and certified rational coefficient enclosures','coordinate_map':{'base':'F(t,x)=(t-x^2/2,x)','cotangent':'tau_new=tau, z_new=z+x','input_jacobian':1,'normal_at_u_zero':'w_new=w-zeta^2/2, zeta_new=zeta','real_pulled_back_halfspace':'t<x^2/2','target_cone':'l_new=-Re w_new>=0, |zeta|<=l_new, |Im w_new|<=l_new/4','normal_radius':'|zeta|<=1/2','old_containing_cone':'|zeta|<=4l/3, |Im w|<=2l/3, l=-Re w','full_complex_polar_margin':'3/sqrt(29)','real_slice_polar_margin':'3/5','proof':'BCT.1--BCT.3; BCT.45--BCT.47'},'balanced_comparison':{'maps':'Psi_B and Psi_C are the exact full tensor isomorphisms induced by the compatible E,B,C coordinate maps','identity':'Psi_C eta_Mprime=eta_M Psi_B','scope':'Every algebraic left E module for the stated linear/time-shift changes; no C flatness','proof':'BCT.32--BCT.37'},'positive_head_example':{'input':'H(tau)/(1-z), H(tau)=sum tau^m/(m!)^2','phi':'x^2/2','a_K':'(2K)!/(2^K K!)','Q':'sum tau^-K a_K/(1-x-z)^(2K+1)','inverse_identity':'((1-x)D_t-D_x) Q=D_t','coefficient_summand':'b_jK=(2K)!/(2^K K!(j+K)!^2)','proof':'BCT.38--BCT.43','coefficient_enclosures':coefficients,'ratio_points':ratios},'no_nonbase_real_contact_quantization_claimed':True}
(out/'real-coordinate-transport-exact-data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'outputs':sorted(p.name for p in out.iterdir() if p.is_file())}))
