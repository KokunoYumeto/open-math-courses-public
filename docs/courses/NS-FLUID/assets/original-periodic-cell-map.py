"""Original periodic cell averaging and its exact signed integral kernel."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
L=2*np.pi;m=4;h=L/m
fig,ax=plt.subplots(1,2,figsize=(13,5.5))
x=np.linspace(0,L,1201)
ax[0].plot(x,2+.4*np.sin(x),color='#1565a8',label=r'$f(x)=2+0.4\sin x$')
ax[0].plot(x,1+np.cos(4*x),color='#16805d',label=r'$g(x)=1+\cos(4x)$')
for j in range(m):
 a=j*h;b=(j+1)*h
 ax[0].axvspan(a,b,color='#c5dcee' if j%2==0 else '#f2e6ca',alpha=.35)
 mean=2+.4*(np.cos(a)-np.cos(b))/h
 ax[0].plot([a,b],[mean,mean],color='#1565a8',lw=3,ls='--',label='Exact cell average of f' if j==0 else None)
ax[0].set(xlim=(0,L),ylim=(-.15,2.75),xlabel='Original coordinate x',ylabel='Scalar amplitude',title='Equal periodic mass in each cell')
ax[0].set_xticks([0,h,2*h,3*h,L],['0',r'$\pi/2$',r'$\pi$',r'$3\pi/2$',r'$2\pi$'])
ax[0].legend(loc='lower left',fontsize=10)
x0=L/3;s1=np.linspace(0,x0,301);s2=np.linspace(x0,L,601)
ax[1].plot(s1,s1/L,color='#743a8c',lw=2)
ax[1].plot(s2,s2/L-1,color='#743a8c',lw=2)
ax[1].plot([x0],[x0/L],'o',color='#743a8c')
ax[1].plot([x0],[x0/L-1],'o',mfc='white',mec='#743a8c')
ax[1].annotate('',xy=(x0,x0/L-1),xytext=(x0,x0/L),arrowprops={'arrowstyle':'->','linestyle':'--','color':'#555'})
ax[1].text(x0+.12,-.16,'Jump = −1',fontsize=11)
ax[1].axhline(0,color='#888',lw=.6)
ax[1].set(xlim=(0,L),ylim=(-.78,.5),xlabel='Original integration coordinate s',ylabel=r'$b_x(s)$',title=r'Signed kernel at $x=L/3$')
ax[1].set_xticks([0,x0,L],['0',r'$x=L/3$',r'$L=2\pi$'])
fig.subplots_adjust(bottom=.27,wspace=.28,top=.86)
fig.text(.05,.12,'Exact identities: DC2, DC7 and DC18–DC21. Curves illustrate the maps; complete proofs accompany the figure.',fontsize=11)
fig.text(.05,.065,'Human comparison: Buckmaster–Vicol, arXiv:1709.10033v4, Lemma lem:Lp:independence and its appendix.',fontsize=10)
for ext in ['png','svg']:fig.savefig(R/f'original-periodic-cell-map.{ext}',dpi=180)
