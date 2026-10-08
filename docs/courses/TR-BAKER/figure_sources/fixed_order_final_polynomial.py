"""Exact conditional final-support geometry for proposed10.143; CC0.
GPT-6.1 Sol (OpenAI), Ultra. All coordinate and count bounds are proved
in multiplicity-stop-endpoints-final-root.md. Font licences are retained.
"""
from pathlib import Path
from fractions import Fraction
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyBboxPatch

b=Fraction(145,28672);ratio=Fraction(171,58)
assert 2*b==Fraction(145,14336)<1 and ratio>1
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(13,6.8),dpi=180,facecolor='#f6f8fb')
gs=fig.add_gridspec(1,3,width_ratios=[1,1,1.1],left=.055,right=.98,bottom=.19,top=.77,wspace=.31)
ax=fig.add_subplot(gs[0,0]);zoom=fig.add_subplot(gs[0,1]);flow=fig.add_subplot(gs[0,2])
fig.suptitle('Terminal fixed-order support and root count',y=.965,fontsize=20,weight='bold',color='#16324f')
fig.text(.5,.888,r'Assume the admissible stage-$I_3$ family has the required integer zeros.',ha='center',fontsize=12.3,color='#42566d')
for a in [ax,zoom]:
 a.set_facecolor('white');a.set_aspect('equal')
 a.axhline(0,color='#b6c2cc',lw=.8);a.axvline(0,color='#b6c2cc',lw=.8)
 a.add_patch(Rectangle((-float(b),-float(b)),2*float(b),2*float(b),fill=False,edgecolor='#b04b3b',ls='--',lw=2.2))
 a.set_xlabel(r'$m_1$',fontsize=12);a.set_ylabel(r'$m_2$',fontsize=12,rotation=0,labelpad=10)
ax.set_xlim(-1.15,1.15);ax.set_ylim(-1.15,1.15);ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.grid(color='#d8e0e8',lw=.6)
for x in [-1,0,1]:
 for y in [-1,0,1]:ax.scatter([x],[y],s=28,color='#62788d',zorder=3)
ax.scatter([0],[0],s=55,color='#176a85',zorder=4)
ax.set_title('Two-coordinate projection\nof the integral support',fontsize=13,pad=12)
zoom.set_xlim(-.013,.013);zoom.set_ylim(-.013,.013)
zoom.set_xticks([-float(b),0,float(b)],['−b','0','b']);zoom.set_yticks([-float(b),0,float(b)],['−b','0','b'])
zoom.scatter([0],[0],s=65,color='#176a85',zorder=4)
zoom.set_title('Exact enlargement\nof the central box',fontsize=13,pad=12)
zoom.text(.5,-.25,r'$b=145/28672<1$',transform=zoom.transAxes,ha='center',fontsize=12,color='#b04b3b')
flow.set_xlim(0,1);flow.set_ylim(0,1);flow.axis('off')
nodes=[(.74,'All coordinates, every rank',r'$m_j\in\mathbb{Z},\quad |m_j|<b\ \Longrightarrow\ m_j=0$'),
       (.43,'Nonzero additive polynomial',r'$P(X)\ne0,\quad\deg P\leq D_{\mathrm{a}}=kL$'),
       (.12,'Too many distinct roots',r'$2R+1>\frac{171}{58}D_{\mathrm{a}}>D_{\mathrm{a}}$')]
for y,title,formula in nodes:
 flow.add_patch(FancyBboxPatch((.015,y),.97,.19,boxstyle='round,pad=.012',facecolor='white',edgecolor='#8da8bc',lw=1.3))
 flow.text(.5,y+.135,title,ha='center',fontsize=12.7,weight='bold',color='#16324f')
 flow.text(.5,y+.054,formula,ha='center',fontsize=11.6,color='#21384c')
for upper,lower in zip(nodes,nodes[1:]):
 flow.annotate('',xy=(.5,lower[0]+.208),xytext=(.5,upper[0]-.015),arrowprops={'arrowstyle':'-|>','color':'#176a85','lw':2,'mutation_scale':17})
fig.text(.055,.045,'The drawn box is the strict coordinate bound; its dashed boundary is excluded.\nOnly the origin can be an integral support point. The coordinate argument holds in every rank.',fontsize=11.3,color='#42566d')
target=Path(__file__).resolve().parent/'fixed-order-final-polynomial.png'
fig.savefig(target,facecolor=fig.get_facecolor());plt.close(fig);print(target)
