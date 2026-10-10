"""Reproducible exact integral plots and root-disk geometry for lesson30."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':14,'axes.titlesize':16,'axes.labelsize':14,'figure.facecolor':'#f8fafc','axes.facecolor':'white','axes.grid':True,'grid.alpha':.18,'savefig.facecolor':'#f8fafc'})
blue='#2357a0';red='#b52d3b';green='#14745e';gray='#4b5563'
def save(fig,stem):
    fig.savefig(OUT/(stem+'.png'),dpi=150)
    fig.savefig(OUT/(stem+'.svg'))
    plt.close(fig)
L=2.;a=1/3;b=1.;ys=np.geomspace(.0001,3,800)
value=2*a*(L-ys*np.arctan(L/ys))-2j*b*np.arctan(L/ys)
fig,ax=plt.subplots(1,2,figsize=(12,5.6))
fig.suptitle('The entire boundary integral keeps its negative imaginary atom',fontsize=19,y=.98)
ax[0].semilogx(ys,value.real,c=blue,lw=2.8,label=r'$\operatorname{Re}G_L(iy)$')
ax[0].axhline(2*a*L,c=gray,ls='--',label=r'$P=2aL=4/3$')
ax[0].set_ylabel('Real part');ax[0].set_xlabel(r'Original height $y>0$')
ax[0].set_title('The principal value is retained');ax[0].legend(loc='lower left',fontsize=12)
ax[1].semilogx(ys,value.imag,c=red,lw=2.8,label=r'$\operatorname{Im}G_L(iy)$')
ax[1].axhline(-np.pi*b,c=gray,ls='--',label=r'$\pi F(0)=-\pi$')
ax[1].set_ylabel('Imaginary part');ax[1].set_xlabel(r'Original height $y>0$')
ax[1].set_title('Approach from the upper half-plane');ax[1].legend(loc='upper left',fontsize=12)
fig.text(.5,.04,r'$F(q)=q/3-1,\quad q\in[-2,2].$  Exact formulas: EX1–EX3. This density is an integral example.',ha='center',fontsize=12)
fig.tight_layout(rect=(0,.1,1,.91));save(fig,'original-boundary-integral')
m0=4.04;h=.04;m=m0-h;c=.7;P=2.;beta=3.
d=2*m0/(P-1j*beta);q=d.imag;rho=q/4
zc=c+h*d;zr=rho*h;lc=-1j*m*zc;lr=m*zr
fig,ax=plt.subplots(1,2,figsize=(12,6.0))
fig.suptitle('The full root disk becomes a disk of growing Euler rates',fontsize=19,y=.98)
ax[0].add_patch(Circle((zc.real,zc.imag),zr,facecolor='#2357a028',edgecolor=blue,lw=2.4))
ax[0].plot([c,zc.real],[0,zc.imag],color=blue,ls=':',lw=1.7)
ax[0].scatter([c,zc.real],[0,zc.imag],c=[gray,blue],s=[35,45],zorder=4)
ax[0].annotate(r'$c+hd$',(zc.real,zc.imag),xytext=(zc.real+.019,zc.imag+.012),fontsize=14)
ax[0].annotate(r'$c$',(c,0),xytext=(c-.005,-.012))
ax[0].axhline(0,color=gray,lw=1)
ax[0].axhline(zc.imag-zr,color=green,ls='--',lw=1.5)
ax[0].text(c-.02,zc.imag-zr-.008,r'$\operatorname{Im}z\geq3qh/4$',color=green,fontsize=12)
ax[0].set(xlim=(c-.025,c+.12),ylim=(-.02,.125),xlabel=r'Original $\operatorname{Re}z$',ylabel=r'Original $\operatorname{Im}z$',title=r'$|z-(c+hd)|\leq\rho h$')
ax[0].set_aspect('equal')
ax[1].add_patch(Circle((lc.real,lc.imag),lr,facecolor='#14745e28',edgecolor=green,lw=2.4))
ax[1].scatter([lc.real],[lc.imag],c=green,s=45,zorder=4)
ax[1].axvline(0,color=gray,lw=1);ax[1].axvline(lc.real-lr,color=green,ls='--',lw=1.5)
ax[1].annotate(r'$-im(c+hd)$',(lc.real,lc.imag),xytext=(.02,lc.imag+.17),arrowprops={'arrowstyle':'->','color':gray},fontsize=13)
ax[1].text(.012,lc.imag-.19,r'$\operatorname{Re}\lambda\geq3mqh/4>0$',color=green,fontsize=12)
ax[1].set(xlim=(-.025,.435),ylim=(lc.imag-.23,lc.imag+.23),xlabel=r'Original $\operatorname{Re}\lambda$',ylabel=r'Original $\operatorname{Im}\lambda$',title=r'$\lambda=-imz,\quad\mathrm{radius}=m\rho h$')
ax[1].set_aspect('equal')
fig.text(.5,.115,r'$m_0=4.04,\ h=0.04,\ m=4,\ c=0.7,\ P=2,\ \beta=3,\ d=2m_0/(P-i\beta),\ q=\operatorname{Im}d,\ \rho=q/4$',ha='center',fontsize=11)
fig.text(.5,.06,'NB26–NB36 and EX6: parameter illustration of the proved map; no vortex eigenvalue is numerically asserted.',ha='center',fontsize=11)
fig.tight_layout(rect=(0,.17,1,.91));save(fig,'original-root-disk-and-growth')
print('Two exact-formula figures rendered.')

