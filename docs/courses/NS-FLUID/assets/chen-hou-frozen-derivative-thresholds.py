"""Exact frozen-model exponents, original anisotropic characteristics and norm ratios."""
from pathlib import Path
import json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axes=plt.subplots(1,3,figsize=(16,5.3),layout='constrained')
k=np.arange(0,15);rate=(7-k)/2
axes[0].axhline(0,color='#7a8490',lw=1)
axes[0].plot(k,rate,'o-',color='#276897',lw=1.5)
axes[0].scatter([7,8],[0,-.5],color=['#ad7821','#18734d'],s=55,zorder=5)
axes[0].annotate('Order 7: neutral',xy=(7,0),xytext=(3,2.3),arrowprops={'arrowstyle':'->'},fontsize=10)
axes[0].annotate('Order 8: strict decay',xy=(8,-.5),xytext=(6,-2.8),arrowprops={'arrowstyle':'->'},fontsize=10)
axes[0].set(xlabel=r'Pure $x$ derivative order $k$',ylabel=r'Exact $L^2$ norm exponent $(7-k)/2$',title='Retain the field and measure factors')
axes[0].set_xticks([0,2,4,6,7,8,10,12,14])
j=np.arange(9);mixed=(7-8-10*j)/2
axes[1].bar(j,mixed,color='#276897')
axes[1].axhline(0,color='#7a8490',lw=1)
axes[1].set(xlabel=r'Number $j$ of $y$ derivatives, $i=8-j$',ylabel=r'Exact $L^2$ exponent $(-1-10j)/2$',title='Every mixed derivative at total order 8')
axes[1].set_xticks(j)
def oddfactor(n):return math.prod(range(1,n+1,2))
time=np.linspace(0,3,200)
terms=[(i,j,oddfactor(2*i+1)*oddfactor(2*j+1)) for i in range(9) for j in range(9-i)]
hom=[v for v in terms if v[0]+v[1]==8]
def squared_ratio(rows):
 denominator=sum(c for i,j,c in rows)
 return sum(c*np.exp((7-i-11*j)*time) for i,j,c in rows)/denominator
homratio=np.sqrt(squared_ratio(hom));fullratio=np.sqrt(squared_ratio(terms))
axes[2].semilogy(time,homratio,label=r'$|\eta(t)|_{\dot H^8}/|\eta_0|_{\dot H^8}$',color='#18734d',lw=2)
axes[2].semilogy(time,fullratio,label=r'$\|\eta(t)\|_{H^8}/\|\eta_0\|_{H^8}$',color='#b4463d',lw=2)
axes[2].semilogy(time,np.exp(3.5*time),label=r'$\|\eta(t)\|_2/\|\eta_0\|_2=e^{7t/2}$',color='#a36d19',ls='--')
axes[2].set(xlabel='Original model time t',ylabel='Exact norm divided by its initial value',title=r'Specified data: $\eta_0=xy\,e^{-x^2-y^2}$')
axes[2].legend(fontsize=9,loc='upper left')
for ax in axes:ax.grid(alpha=.2)
fig.suptitle(r'Original model: $a_1=1/2$, $a_2=11/2$, $a_3=1/2$; proofs LT4–LT15 and Exercise 4',fontsize=14)
fig.savefig(R/'chen-hou-frozen-derivative-thresholds.png',dpi=160)
fig.savefig(R/'chen-hou-frozen-derivative-thresholds.svg')
out={'coefficients':['1/2','11/2','1/2'],'pure_derivative_exponents':[{'k':int(n),'rate':str((7-int(n)))+'/2'} for n in k],
 'data':'eta0(x,y)=xy exp(-x^2-y^2) on the original positive quadrant',
 'exact_squared_norm_formula':'pi/128 sum (2i+1)!! (2j+1)!! exp((7-i-11j)t)',
 'scope':'Finite sums of exact proved norm formulas, evaluated numerically for the illustration; no numerical source profile or full stability certificate.',
 'samples':[{'t':float(time[n]),'homogeneous8_ratio':float(homratio[n]),'inhomogeneous8_ratio':float(fullratio[n])} for n in range(0,len(time),10)]}
(R/'chen-hou-frozen-model-samples.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({'figure':str(R/'chen-hou-frozen-derivative-thresholds.png')}))
