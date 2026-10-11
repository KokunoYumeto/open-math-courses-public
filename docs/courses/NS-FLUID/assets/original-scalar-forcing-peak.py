"""Original scalar forcing kernel and quadrature of the complete EX24 expression."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
P=Path(__file__).resolve().parent
ink='#153047';blue='#176d9a';orange='#b65c26';gray='#718491'
fig=plt.figure(figsize=(16,10),facecolor='#f6f8fb');canvas=fig.add_axes([0,0,1,1]);canvas.axis('off')
canvas.text(.045,.945,'The forcing enters most strongly at an interior physical time',fontsize=25,fontweight='bold',color=ink)
canvas.text(.045,.895,'Exact scalar example RC19–RC24; complete asymptotic proof EX19–EX24. These are not cascade trajectories.',fontsize=14,color=ink)
K=1024.;T=.5+K**-.5;star=.5+(2*K)**-.5;fstar=(np.sqrt(2)-1)/3
r=np.linspace(.5,T,701);th=np.sqrt(K)*(r-.5)
exact=np.exp(np.sqrt(K)*(th-2*th**3/3-1/3))
gauss=np.exp(fstar*np.sqrt(K)-np.sqrt(2)*K**1.5*(r-star)**2)
upper=np.exp(fstar*np.sqrt(K)-(2*np.sqrt(2)/3)*K**1.5*(r-star)**2)
assert np.all(exact<=upper*(1+1e-12))
left=fig.add_axes([.07,.34,.39,.43])
left.plot(r,exact,color=orange,lw=2.8,label='Exact forcing kernel')
left.plot(r,gauss,color=blue,ls='--',lw=1.6,label='Quadratic expression near the peak')
left.plot(r,upper,color=gray,ls=':',lw=1.8,label='Proved Gaussian upper bound')
left.axvline(star,color=ink,ls='--',lw=1)
left.set_title('Original source time r, K = 1024',fontsize=16,color=ink,pad=14)
left.set_xlabel('r in the final physical interval [1/2, T]',fontsize=12)
left.set_ylabel(r'$\exp(-K\int_r^T z_K(v)\,dv)$',fontsize=17)
left.ticklabel_format(useOffset=False,axis='x');left.grid(alpha=.16)
left.legend(loc='upper left',fontsize=8.5,framealpha=.9)
ks=2.**np.arange(2,21)
def evaluate(order):
 nodes,weights=np.polynomial.legendre.leggauss(order);theta=(nodes+1)/2
 f=theta-2*theta**3/3-1/3
 values=[]
 for kval in ks:
  first=kval**-.25*(-np.expm1(-kval/2))*np.exp(-np.sqrt(2*kval)/3)
  second=kval**.25*np.dot(weights/2,np.exp(np.sqrt(kval)*(f-fstar)))
  values.append(first+second)
 return np.array(values)
values=evaluate(320);assert np.max(np.abs(values-evaluate(640)))<1e-10
right=fig.add_axes([.585,.34,.355,.43])
right.plot(ks,values,marker='o',ms=4,color=blue,lw=1.5,label='Quadrature of complete EX19')
limit=np.sqrt(np.pi/np.sqrt(2))
right.axhline(limit,color=orange,ls='--',lw=1.8,label=r'Proved limit $\sqrt{\pi/\sqrt{2}}$')
right.set_xscale('log',base=2);right.set_xlabel('Original parameter K',fontsize=12)
right.set_title('The full expression on the left of EX24',fontsize=14,color=ink,pad=14)
right.set_ylabel(r'$K^{59/4}e^{-(\sqrt{2}-1)\sqrt{K}/3}y_K(T)$',fontsize=17)
right.legend(loc='lower right',fontsize=9);right.grid(alpha=.16)
canvas.text(.055,.244,r'$r_*=\frac{1}{2}+\frac{1}{\sqrt{2K}},\qquad \max_r\left(-K\int_r^Tz_K(v)\,dv\right)=\frac{\sqrt{2}-1}{3}\sqrt{K}$',fontsize=23,color=ink)
canvas.text(.055,.163,r'$\lim_{K\to\infty}K^{59/4}\exp\left(-\frac{\sqrt{2}-1}{3}\sqrt{K}\right)y_K(T)=\sqrt{\frac{\pi}{\sqrt{2}}}$',fontsize=27,color=orange)
canvas.text(.045,.08,'Left: exact formulas restricted to the final interval; the dotted bound follows from the complete cubic identity EX20–EX21.',fontsize=11.5,color='#456376')
canvas.text(.045,.047,'Right: numerical quadrature illustrates the analytically proved limit, retaining the earlier-time contribution in EX19.',fontsize=11.5,color='#456376')
canvas.text(.045,.017,'Human comparison: Terence Tao, arXiv:1402.0290v3,2405–2443. The example tests a scalar inference, not the cascade theorem.',fontsize=11,color='#456376')
for ext in ['png','svg']:fig.savefig(P/f'original-scalar-forcing-peak.{ext}',dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)

