"""Exact rational tail samples and exact real slices of the proved support geometry."""
from pathlib import Path
from fractions import Fraction
from math import comb
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUT=Path(__file__).resolve().parent
E=Fraction(1,64);D=Fraction(2);L=Fraction(4);a=E*(D+L)
tails=[]
for R in range(3,25):
    positive=a**R/(1-a)
    negative=a**3/(1-a)**4-sum((Fraction(comb(q,3))*a**q for q in range(3,R)),Fraction(0))
    tails.append({'R':R,'positive_ell0_tail':str(positive),'negative_ell_minus3_tail_divided_by_6E_minus3':str(negative)})
sigma=[Fraction(k,40) for k in range(41)]
geometry=[{'sigma':str(s),'spatial_radius':str(2*min(s,1-s))} for s in sigma]
data={'E':str(E),'D':str(D),'L':str(L),'a':str(a),'tail_proof':'IK.6-IK.7','cone':'w real <= 0, |zeta| <= 2(-w)','endpoint_time_span':1,'cone_A':2,'proper_endpoints':[['0','0'],['-1','0']],'proper_fiber':'t=-sigma, |x| <= min(2sigma,2(1-sigma)), 0<=sigma<=1','proper_geometry':geometry,'tails':tails,'scope':'Exact one-spatial-coordinate real slices; complex discs and other coordinates are retained in the proof; finite display windows do not truncate any theorem.'}
(OUT/'infinite-kernel-geometry-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.titlesize':12,'axes.labelsize':10,'svg.hashsalt':'actual-infinite-kernel-20261009'})
fig,axes=plt.subplots(1,3,figsize=(15,6))
fig.subplots_adjust(left=.06,right=.985,bottom=.28,top=.81,wspace=.35)
ax=axes[0]
for j in range(-7,8):
    for k in range(-7,8):
        if j+k>=0:
            ax.scatter(j,k,s=19,c=('#1b7185' if j>=0 and k>=0 else '#cc7950'),zorder=3)
ax.plot([-7,7],[7,-7],color='#303a46',lw=1.3)
ax.text(-6.7,5.55,'m = j + k = 0',fontsize=9,backgroundcolor='white')
ax.annotate('',xy=(7.9,3),xytext=(6.6,3),arrowprops={'arrowstyle':'->','color':'#1b7185'})
ax.annotate('',xy=(3,7.9),xytext=(3,6.6),arrowprops={'arrowstyle':'->','color':'#1b7185'})
ax.axhline(0,color='#b6c2cd',lw=.8);ax.axvline(0,color='#b6c2cd',lw=.8)
ax.set_xlim(-8,8);ax.set_ylim(-8,8);ax.set_aspect('equal')
ax.set_xlabel('left homogeneous index j');ax.set_ylabel('right homogeneous index k')
ax.set_title('Every fixed degree has infinite sums',pad=12)
ax.text(.02,-.25,'Shown: degree 0, with contraction length m >= 0.\nOrange points retain both mixed signs.\nThe 15 x 15 window is a sample, not a cutoff.',transform=ax.transAxes,fontsize=9,va='top')
ax=axes[1]
rs=[t['R'] for t in tails]
ax.semilogy(rs,[float(Fraction(t['positive_ell0_tail'])) for t in tails],color='#1b7185',lw=2,label='degree 0: a^R / (1-a)')
ax.semilogy(rs,[float(Fraction(t['negative_ell_minus3_tail_divided_by_6E_minus3'])) for t in tails],color='#cc7950',lw=2,label='degree -3: normalized tail')
ax.set_xlabel('discarded total index q >= R');ax.set_ylabel('exact majorant sample')
ax.set_title('One common margin controls tails',pad=12)
ax.grid(alpha=.25);ax.legend(loc='upper right',fontsize=8)
ax.text(.02,-.25,'E = 1/64, D = 2, L = 4, a = 3/32.\nAll samples are exact rational numbers.\nNegative ordinate: sum binom(q,3) a^q.',transform=ax.transAxes,fontsize=9,va='top')
ax=axes[2]
ss=np.array([float(s) for s in sigma]);rr=np.array([float(Fraction(g['spatial_radius'])) for g in geometry])
ax.fill_between(-ss,-rr,rr,color='#c1dce1',alpha=.9)
ax.plot(-ss,rr,color='#1b7185',lw=2);ax.plot(-ss,-rr,color='#1b7185',lw=2)
ax.scatter([0,-1],[0,0],s=48,color='#303a46',zorder=5)
ax.text(-.03,.13,'output (0,0)',ha='right',fontsize=9)
ax.text(-.98,.13,'input (-1,0)',ha='left',fontsize=9)
ax.plot([-.5,-.5],[-1,1],color='#cc7950',lw=1.2,ls='--')
ax.text(-.48,.3,'|x| <= 1\nat sigma = 1/2',fontsize=9)
ax.set_xlim(-1.2,.2);ax.set_ylim(-1.35,1.35)
ax.set_xlabel('intermediate normal coordinate t = -sigma');ax.set_ylabel('intermediate spatial coordinate x')
ax.set_title('Proper intermediate fiber',pad=12)
ax.grid(alpha=.2)
ax.text(.02,-.25,'Exact real slice for A = 2.\nThe full spatial fibers are closed complex discs.\nA fixed outer domain supplies a positive collar.',transform=ax.transAxes,fontsize=9,va='top')
fig.suptitle('Full infinite contractions and actual thick-cone properness',fontsize=17,fontweight='bold',y=.975)
fig.text(.5,.89,'Proof: IK.2-IK.3 and IK.7. Human source geometry: Micro-hyperbolic systems, section 3.1; HolIII, III.2.',ha='center',fontsize=10,color='#536170')
fig.savefig(OUT/'infinite-kernel-geometry.png',dpi=170,metadata={'Software':'Matplotlib','Description':'Exact mathematical proof illustration; no public personal attribution.'})
fig.savefig(OUT/'infinite-kernel-geometry.svg',metadata={'Date':None,'Creator':'Matplotlib','Description':'Exact mathematical proof illustration; no public personal attribution.'})
plt.close(fig)
print(json.dumps({'tail_samples':len(tails),'proper_fiber_samples':len(geometry),'outputs':['infinite-kernel-geometry.png','infinite-kernel-geometry.svg','infinite-kernel-geometry-data.json']}))
