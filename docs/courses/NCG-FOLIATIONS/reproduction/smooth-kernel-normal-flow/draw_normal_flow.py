"""CC0 reproducible diagram of a smooth labelled kernel and normal-flow failure."""
from pathlib import Path
import argparse,json,math,os
from finite_checks import run

HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--out',type=Path,default=HERE/'figures')
parser.add_argument('--resources',type=Path,default=HERE.parent/'labelled-geometric-kernel')
args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=True)
os.environ.setdefault('MPLCONFIGDIR',str(args.out/'runtime-cache'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch
regular=FontProperties(fname=str(args.resources/'fonts/DejaVuSans.ttf'))
bold=FontProperties(fname=str(args.resources/'fonts/DejaVuSans-Bold.ttf'))
INK='#19384d';BLUE='#17628f';RED='#b34638';GREEN='#16745a';GRAY='#627789'
plt.rcParams.update({'svg.hashsalt':'smooth-labelled-kernel-normal-flow-ck1-ck9','axes.edgecolor':INK,'axes.labelcolor':INK,'xtick.color':INK,'ytick.color':INK})
def text(ax,x,y,s,size=12,strong=False,**kw):return ax.text(x,y,s,fontproperties=bold if strong else regular,fontsize=size,color=kw.pop('color',INK),**kw)
def ticks(ax):
    for item in ax.get_xticklabels()+ax.get_yticklabels():item.set_fontproperties(regular)
fig=plt.figure(figsize=(16,11),facecolor='white')
head=fig.add_axes([.04,.915,.93,.07]);head.axis('off')
text(head,0,.68,'A smooth coarse kernel need not support norm differentiation',21,True)
text(head,0,.08,'Actual irrational-rotation holonomy Z ⋉ (R/Z); ε = 1/8.  Every arrow label and inverse normal phase is retained.',12)

ax=fig.add_axes([.06,.565,.41,.30]);ax.set_xlim(-.5,8.7);ax.set_ylim(-.9,1.35);ax.axis('off')
text(ax,0,1.15,'1  Exact labelled Hilbert map at x = 1/4',15,True)
ax.plot([0,8.4],[0,0],color=GRAY,lw=1)
for n in range(9):
    value=n+(1/8 if n%2 else 0)
    ax.plot([value],[0],'o',color=BLUE,ms=7)
    text(ax,value,-.18,str(n),11,ha='center')
    if n%2:text(ax,value,.15,'n+1/8',10,ha='center')
text(ax,0,.69,'F(n,x) = n + (1/8) sin(2πn²x)',14)
text(ax,0,-.49,'max(0, |δ|−1/4) ≤ √k(gh,h) ≤ |δ|+1/4',13,color=GREEN)
text(ax,0,-.78,'Both coarse controls hold uniformly in h.  CK.1–CK.3',11)

ax=fig.add_axes([.56,.57,.39,.275])
tau=[i/800 for i in range(801)];curves=[]
for n,color in zip([4,8,16,32],[BLUE,GREEN,RED,'#76528c']):
    t=1/(4*n+2)
    values=[(1+(math.sin(2*math.pi*(n+1)**2*t*u)-math.sin(2*math.pi*n*n*t*u))/8)**2 for u in tau]
    ax.plot(tau,values,label=f'n={n}; tₙ=1/{4*n+2}',color=color,lw=1.4)
    curves.append(dict(n=n,t_exact=f'1/{4*n+2}',endpoint_sample=values[-1]))
ax.axhline(81/64,color=GRAY,ls='--',lw=1)
ax.set_ylim(.48,1.64);ax.set_xlim(0,1)
ax.set_title('2  Generator a(n, τtₙ): numerical traces',fontproperties=bold,fontsize=15,color=INK,pad=13)
ax.set_xlabel('τ; actual unit translation t = τ/(4n+2)',fontproperties=regular,fontsize=11)
ax.set_ylabel('a(n, τtₙ)',fontproperties=regular,fontsize=11)
ax.legend(prop=FontProperties(fname=str(args.resources/'fonts/DejaVuSans.ttf'),size=9),loc='upper left',ncol=2)
text(ax,.02,-.33,'Exact: a(n,tₙ)−a(n,0) ≥ 17/64 for n ∈ 4N',11,transform=ax.transAxes,color=GREEN)
ticks(ax)

ax=fig.add_axes([.075,.17,.38,.255])
ns=list(range(4,65,4));derivatives=[(2*n+1)/2 for n in ns]
ax.plot(ns,derivatives,'o-',color=RED,lw=2)
ax.set_title('3  Exact derivative grows along labels',fontproperties=bold,fontsize=15,color=INK,pad=16)
ax.set_xlabel('arrow label n',fontproperties=regular,fontsize=11)
ax.set_ylabel('∂ₓa(n,0) / π = (2n+1)/2',fontproperties=regular,fontsize=11)
ax.grid(alpha=.2);ticks(ax)
text(ax,0,-.28,'tₙ → 0, but ‖σₜₙ(a)−a‖∞ ≥ 17/64.  CK.5–CK.7',12,transform=ax.transAxes)

ax=fig.add_axes([.53,.15,.43,.30]);ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
text(ax,0,1,'4  A noncompact bounded-phase commutator',15,True)
for x,value in [(.02,'uₙ = e₁ ⊗ δₙ\northonormal columns'),(.59,'e₁₋₍ₙ₊₁₎² ⊗ δₙ\nnegative Fourier mode')]:
    ax.add_patch(FancyBboxPatch((x,.57),.37,.20,boxstyle='round,pad=.015',facecolor='#eef4f7',edgecolor=BLUE))
    text(ax,x+.185,.67,value,12,ha='center',va='center')
ax.annotate('',xy=(.58,.67),xytext=(.41,.67),arrowprops={'arrowstyle':'->','color':BLUE,'lw':2})
text(ax,.49,.82,'[Fᴅ,Mₐ]',12,ha='center')
text(ax,0,.43,'Fourier coefficient of a at −(n+1)² is exactly i/8.',12)
text(ax,0,.29,'|f(1−(n+1)²)−f(1)| > 1/2  ⇒  norm ≥ 1/16.',12,color=GREEN)
text(ax,0,.15,'A compact operator sends uₙ to a norm-null sequence.',12)
text(ax,0,.01,'The lower bound proves failure on these actual columns.  CK.8–CK.9',11)

caption=fig.add_axes([.04,.012,.93,.053]);caption.axis('off')
text(caption,0,.7,'The coarse bounds, flow margin, derivative coefficients and Fourier amplitude are exact. Curves are labelled numerical samples.',11)
text(caption,0,.12,'A different kernel or geometric connection can repair this failure; this figure does not refute a suitable graph-Dirac construction.',11)
notice=(args.resources/'FONT-NOTICE.txt').read_text(encoding='utf-8')
description='Original CC0 diagram; proofs CK.1–CK.9 and SK.1–SK.5. Numerical curves are declared samples.\n'+notice
fig.savefig(args.out/'smooth-kernel-normal-flow.png',dpi=150,metadata={'Title':'Smooth labelled kernel and normal flow','Description':description})
fig.savefig(args.out/'smooth-kernel-normal-flow.svg',metadata={'Title':'Smooth labelled kernel and normal flow','Description':description,'Date':None})
plt.close(fig)
data=run();data['numerical_traces']=curves;data['proof_locators']=['CK.1–CK.9','SK.1–SK.5']
(args.out/'figure-data.json').write_text(json.dumps(data,indent=2,sort_keys=True)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'figure':'smooth-kernel-normal-flow','finite_checks':data['count']}))
