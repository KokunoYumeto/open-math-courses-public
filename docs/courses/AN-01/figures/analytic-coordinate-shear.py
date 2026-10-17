"""Reproduce the analytic-shear figure in AN01-U076. CC0.

Written by GPT-6 Astra (OpenAI), Ultra, October 2026.
Requires Python, NumPy and Matplotlib. Run this file to write SVG and PNG
beside it. Curves use the exact map F(x,y)=(x,y+x*x); arrows are its
differential on the explicitly specified vector, not secant vectors.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':12,'svg.fonttype':'none',
                    'svg.hashsalt':'AN01-U076-analytic-shear',
                    'font.family':'DejaVu Sans'})
fig,axes=plt.subplots(1,2,figsize=(11,5.8),layout='constrained')
x=np.linspace(-1.5,1.5,401)
for ax,transformed in zip(axes,[False,True]):
    for c in np.linspace(-1,1,5):
        y=np.full_like(x,c)
        ax.plot(x,y+x*x if transformed else y,
                color='#216b9d' if c==0 else '#9bbacc',
                lw=2.5 if c==0 else 1.0)
    for c in np.linspace(-1.5,1.5,7):
        y=np.linspace(-1,1,101)
        ax.plot(np.full_like(y,c),y+c*c if transformed else y,
                color='#cad3db',lw=1.0,zorder=0)
    ax.set_aspect('equal',adjustable='box')
    ax.set_xlim(-1.75,1.75)
    ax.set_ylim(-1.25,3.6)
    ax.axhline(0,color='#65717d',lw=.7,zorder=0)
    ax.axvline(0,color='#65717d',lw=.7,zorder=0)
    ax.spines[['top','right']].set_visible(False)
    ax.set_xlabel('s' if transformed else 'x')
    ax.set_ylabel('t' if transformed else 'y',rotation=0)
    ax.set_title('After F(x, y) = (x, y + x²)' if transformed else 'Original coordinates',pad=14)

p=np.array([.5,0.]);v=np.array([.5,0.])
Fp=np.array([.5,.25]);DFv=np.array([.5,.5])
assert np.allclose(np.array([[1.,0.],[2*p[0],1.]])@v,DFv)
for ax,point,vector,label in [(axes[0],p,v,'v = (1/2, 0)'),
                             (axes[1],Fp,DFv,'DF(p)v = (1/2, 1/2)')]:
    ax.scatter(*point,s=35,color='#a33137',zorder=5)
    ax.annotate('',xy=point+vector,xytext=point,
                arrowprops={'arrowstyle':'-|>','color':'#a33137','lw':2.2},zorder=6)
    ax.text(-1.55,3.15,label,color='#a33137',fontsize=11)
axes[0].annotate('p = (1/2, 0)',xy=p,xytext=(-1.5,-.88),
                 arrowprops={'arrowstyle':'-','lw':.8},fontsize=10)
axes[1].annotate('F(p) = (1/2, 1/4)',xy=Fp,xytext=(-1.55,-.91),
                 arrowprops={'arrowstyle':'-','lw':.8},fontsize=10)
axes[0].text(-1.55,2.65,'Highlighted line: y = 0',color='#216b9d',fontsize=11)
axes[1].text(-1.55,2.65,'Highlighted curve: t = s²',color='#216b9d',fontsize=11)
fig.suptitle('An analytic change of coordinates preserves the derivative-growth class',fontsize=13)
out=Path(__file__).resolve().parent
description='Exact polynomial shear F(x,y)=(x,y+x²). Grid lines and tangent vectors are specified in AN01-U076, equations 15–16. CC0; GPT-6 Astra (OpenAI), Ultra.'
fig.savefig(out/'analytic-coordinate-shear.svg',metadata={'Title':'Analytic coordinate shear','Description':description,'Creator':'GPT-6 Astra (OpenAI), Ultra','Date':None})
svg=out/'analytic-coordinate-shear.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8',newline='\n')
fig.savefig(out/'analytic-coordinate-shear.png',dpi=170,metadata={'Description':description,'Software':'Matplotlib'})
plt.close(fig)
print('Wrote the exact shear figure in SVG and PNG.')
