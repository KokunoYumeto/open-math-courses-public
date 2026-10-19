"""Reproducible contour and continuation-domain illustration for AN01-U078.

Written by GPT-6 Astra (OpenAI), Ultra. CC0.
NumPy and Matplotlib are required. All displayed contour coordinates and
strip boundaries are the exact formulas in equations (11) and (17).
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'svg.fonttype':'none'})
fig,(ax,bx)=plt.subplots(1,2,figsize=(12.5,5.8),layout='constrained')
q=np.array([1,-1])/np.sqrt(2)
A=np.array([0.,0.]);B=np.array([2.,0.]);C=B+3*q;D=A+3*q
ax.add_patch(Polygon([A,B,C,D],facecolor='#eaf1f7',edgecolor='none'))
def arrow(a,b,color,lw=2.5):
 ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':color,'lw':lw})
arrow(A,B,'#c65324')
arrow(A,D,'#1e669b');arrow(D,C,'#1e669b');arrow(C,B,'#1e669b')
ax.scatter([0,2],[0,0],color='#243a50',s=25)
ax.text(-.12,.14,'0');ax.text(1.95,.14,'2')
ax.text(.5,.36,'Original segment',color='#a63d17')
ax.text(.15,-.9,r'$L_0: qr$',color='#1e669b',rotation=-45)
ax.text(3.25,-.6,r'$L_2: 2+qr$',color='#1e669b',rotation=-45)
ax.text(2.7,-2.47,'Connecting edge at R = 3',ha='center',fontsize=11)
ax.set(xlim=(-.5,4.6),ylim=(-2.8,.7),aspect='equal',xlabel=r'Re $s$',ylabel=r'Im $s$',title='Two endpoint rays, with the return orientation')
ax.grid(alpha=.15)
x=np.linspace(-2.3,2.3,601)
bx.axhspan(-1,1,color='#cad5df',alpha=.4)
bx.fill_between(x,x-1,x+1,color='#69a4c9',alpha=.26)
bx.plot(x,x-1,color='#32759f',ls='--',lw=1)
bx.plot(x,x+1,color='#32759f',ls='--',lw=1)
bx.axhline(-1,color='#7d8b98',ls=':',lw=1)
bx.axhline(1,color='#7d8b98',ls=':',lw=1)
bx.axhline(0,color='#aab3bd',lw=.7)
bx.axvline(0,color='#aab3bd',lw=.7)
bx.plot([0,0],[1,2.45],color='#b7352b',lw=3)
bx.plot([0,0],[-1,-2.45],color='#b7352b',lw=3)
bx.scatter([0,0],[-1,1],color='#b7352b',s=40,zorder=4)
bx.text(.12,1.05,r'$i$',color='#b7352b')
bx.text(.12,-1.18,r'$-i$',color='#b7352b')
bx.scatter([1.5],[1.5],s=45,color='#134f76',zorder=5)
bx.annotate(r'$3/2+3i/2$',xy=(1.5,1.5),xytext=(.35,2.13),arrowprops={'arrowstyle':'-','color':'#134f76'},fontsize=12)
bx.text(-2.15,.45,r'$Z_0: |v|<1$',fontsize=12)
bx.text(-2.15,-2.05,r'$Z_{-1}: |v-u|<1$',fontsize=12,color='#245c80')
bx.set(xlim=(-2.3,2.3),ylim=(-2.45,2.45),aspect='equal',xlabel=r'$u=\mathrm{Re}\,w$',ylabel=r'$v=\mathrm{Im}\,w$',title='Overlapping strips continue the scalar kernel')
fig.savefig(out/'spherical-kernel-contours.png',dpi=170,metadata={'Software':'Matplotlib; original AN01-U078 illustration; CC0'})
svg=out/'spherical-kernel-contours.svg'
fig.savefig(svg,metadata={'Creator':'GPT-6 Astra (OpenAI), Ultra; CC0','Date':None})
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8',newline='\n')
plt.close(fig)
