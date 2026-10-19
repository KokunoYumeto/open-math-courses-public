"""Coordinate maps and bounds for the worked exercise M4.

Mathematical context: Jiri Lebl, Basic Analysis II, section 8.5,
https://www.jirka.org/ra/html/sec_svinvfuncthm.html; Guillemin--Sternberg,
Semi-classical Analysis, author draft 13 January 2010, section 13.14.3,
https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf.
The exercise, its bounds and this illustration are independently written
programme material: GPT-6.1 Sol (OpenAI), Ultra; CC0 to the extent rights exist.
The cited human works and the plotting software retain their own terms.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':14,'svg.hashsalt':'parameter-morse-pivot-norms',
                     'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,3,figsize=(14.6,5.7))
fig.subplots_adjust(left=.045,right=.975,bottom=.31,top=.80,wspace=.36)
t=np.linspace(0,2*np.pi,801)
circle=np.array([np.cos(t),np.sin(t)])
D=np.array([[-1.,3.],[1.,-1.]])/np.sqrt(2.)
for ax,data,title,labels in [(axes[0],circle,'Unit circle',('$z_1$','$z_2$')),
                            (axes[1],D@circle,r'$F_4$ image; $|\det D_4|=1$',('$x$','$y$'))]:
    ax.plot(*data,color='#17699C',lw=2)
    ax.axhline(0,color='#D0D4D8',lw=.7)
    ax.axvline(0,color='#D0D4D8',lw=.7)
    ax.plot(0,0,'ko',ms=3)
    ax.set_aspect('equal',adjustable='box')
    ax.set(title=title,xlabel=labels[0],ylabel=labels[1])
for ax,transform in [(axes[0],np.eye(2)),(axes[1],D)]:
    for j,color in [(0,'#B54727'),(1,'#27835A')]:
        end=transform[:,j]
        ax.annotate('',xy=end,xytext=(0,0),arrowprops={'arrowstyle':'->','color':color,'lw':1.8})
        ax.annotate('$e_'+str(j+1)+'$' if ax is axes[0] else '$D_4e_'+str(j+1)+'$',
                    end,xytext=(5,5),textcoords='offset points',color=color,fontsize=13)
s=np.linspace(-8,8,801)
chosen=(np.sqrt(s*s+16)+np.abs(s))/4
universal=np.sqrt(np.abs(s))
axes[2].plot(s,chosen,color='#17699C',lw=2,label=r'$\|D_s\|_2$ in (M4.4)')
axes[2].plot(s,universal,color='#B54727',lw=1.8,ls='--',label=r'$\sqrt{|s|}$: every chart, (M4.3)')
axes[2].axhline(1,color='#777777',lw=1.3,ls=':',label=r'$|\det D_s|=1$')
axes[2].set(xlabel='$s$',ylabel='Norm or absolute determinant',
            title='Chart norm and determinant',xlim=(-8,8),ylim=(0,4.6))
axes[2].grid(alpha=.17)
axes[2].legend(fontsize=11,loc='upper center',bbox_to_anchor=(.5,-.21),frameon=False)
fig.suptitle('A zero-diagonal Hessian and its parameter-dependent coordinates',fontsize=18)
fig.text(.045,.065,'Exact formulae and proof: parameter-morse-reduction.md, M4.1-M4.4. '
         'Curves are numerical samples.',fontsize=11.5)
fig.text(.045,.025,'Source context: Lebl, section 8.5; '
         'Guillemin-Sternberg (2010), section 13.14.3.',fontsize=11.5)
fig.savefig(out/'parameter-morse-pivot-norms.png',dpi=170)
fig.savefig(out/'parameter-morse-pivot-norms.svg',metadata={'Date':None})
plt.close(fig)
