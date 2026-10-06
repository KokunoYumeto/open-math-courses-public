"""Reproduce the exact CF figures. Original source and outputs: CC0."""
from pathlib import Path
import argparse, json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch
import numpy as np

OWN=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--output-dir',type=Path,default=OWN/'figures')
OUT=parser.parse_args().output_dir.resolve()
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':13,'font.family':'DejaVu Sans','svg.hashsalt':'AN02-CF042-v1'})
BLUE='#245dad'; RED='#bb4138'; GREEN='#21816a'; GRAY='#536274'
def save(fig,name):
    fig.savefig(OUT/(name+'.png'),dpi=150,bbox_inches='tight',metadata={'Author':'GPT-6.1 Sol (OpenAI)','Description':'Original mathematical illustration; CC0.'})
    fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI)','Description':'Original mathematical illustration; CC0.'})
    plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(12,5),gridspec_kw={'width_ratios':[1.35,1]})
ax,tx=axes
ax.add_patch(Rectangle((-1,-.5),2,1,facecolor=BLUE,alpha=.18,edgecolor=BLUE,linewidth=2))
ax.add_patch(Circle((2,0),.25,facecolor=RED,alpha=.20,edgecolor=RED,linewidth=2))
ax.axvline(1,color=BLUE,linewidth=2)
ax.axvline(1.75,color=RED,linestyle='--',linewidth=1.5)
ax.annotate('',xy=(1.75,.65),xytext=(1,.65),arrowprops={'arrowstyle':'<->','color':GRAY})
ax.text(1.375,.77,r'$\delta=3/4$',ha='center')
ax.annotate('',xy=(2.8,-.8),xytext=(2.0,-.8),arrowprops={'arrowstyle':'->','color':GREEN,'lw':2})
ax.text(2.35,-1.05,r'$\eta=(1,0)$',ha='center',color=GREEN)
ax.text(0,0,r'$K$',ha='center',va='center',fontsize=20,color=BLUE)
ax.annotate('test carrier',xy=(2,.2),xytext=(2.2,.95),arrowprops={'arrowstyle':'->','color':RED},color=RED)
ax.text(1,-1.32,r'$x_1=H_K(\eta)=1$',ha='center',color=BLUE)
ax.set(xlim=(-1.5,3.3),ylim=(-1.55,1.35),xlabel=r'$x_1$',ylabel=r'$x_2$')
ax.set_aspect('equal');ax.grid(alpha=.14)
tx.axis('off')
tx.text(0,.91,'CF2.1: support from a strict plane',fontweight='bold')
tx.text(0,.72,r'$K=[-1,1]\times[-1/2,1/2]$')
tx.text(0,.58,r'$a=7/4,\quad H_K(\eta)=1$')
tx.text(0,.44,r'$\xi\ \longmapsto\ \xi+it\eta,\quad t\geq0$')
tx.text(0,.28,r'$|u(\phi)|\leq C_M(1+t)^{N+2M}e^{-3t/4}$')
tx.text(0,.14,r'$2M>N+2\quad\Longrightarrow\quad u(\phi)=0$')
tx.text(0,.02,'Exact geometry; no plotted distribution density.',fontsize=10,color=GRAY)
fig.suptitle('A support plane gives exponential attenuation',fontsize=17,y=1.02)
save(fig,'support-plane-decay')

fig,(ax,rx)=plt.subplots(1,2,figsize=(12,5),gridspec_kw={'width_ratios':[1,1.25]})
ang=np.linspace(0,2*np.pi,720)
ax.plot(2*np.cos(ang),2*np.sin(ang),color=GRAY,linestyle=':',label=r'$|t|=2$')
ax.plot(1.5*np.cos(ang),1.5*np.sin(ang),color=BLUE,linewidth=2.5,label=r'$|t|=3/2$')
roots=[-1,1,2]
for root in roots:
    ax.plot(root,0,'o',color=RED,markersize=7)
    ax.annotate(str(root),xy=(root,0),xytext=(root,-.34),ha='center',color=RED)
ax.axhline(0,color=GRAY,linewidth=.7);ax.axvline(0,color=GRAY,linewidth=.7)
ax.set(xlim=(-2.3,2.6),ylim=(-2.3,2.3),xlabel=r'$\operatorname{Re}t$',ylabel=r'$\operatorname{Im}t$')
ax.set_aspect('equal');ax.legend(loc='upper left',fontsize=11)
rx.set(xlim=(.75,2.28),ylim=(-.95,3.3));rx.axis('off')
rx.text(.78,3.12,r'$p(t)=(t+1)(t-1)(t-2),\quad\varepsilon_3=1/12$')
for y,root in zip([2.5,1.9,1.3],roots):
    modulus=abs(root)
    rx.plot([1,2],[y,y],color=GRAY,linewidth=1.5)
    rx.plot([modulus-1/12,modulus+1/12],[y,y],color=RED,linewidth=9,alpha=.35)
    rx.text(.79,y+.08,r'$a_j='+str(root)+'$',fontsize=11)
    rx.plot(1.5,y,'o',color=BLUE,markersize=6)
rx.plot([1.5,1.5],[1.15,2.68],color=BLUE,linestyle='--')
rx.text(1.5,.9,r'$r=3/2$',ha='center',color=BLUE)
rx.text(.8,.49,r'$|p(t)|\geq1/8\quad (|t|=3/2)$')
rx.text(.8,.16,r'General bound: $\varepsilon_3^3=1/1728$')
rx.text(.8,-.19,r'$|g(0)|\leq8\max_{|t|=3/2}|p(t)g(t)|$')
rx.text(.8,-.62,'Two roots share modulus 1; both factors count.',fontsize=10,color=GRAY)
fig.suptitle('A circle avoiding all root-modulus intervals',fontsize=17,y=1.02)
save(fig,'safe-division-circle')

fig,ax=plt.subplots(figsize=(12,5.4));ax.set(xlim=(0,12),ylim=(0,5.5));ax.axis('off')
ax.text(6,5.17,r'$P(z)=z^2,\quad P(-D)=D^2,\quad D=-i\partial$',ha='center',fontsize=19)
def box(x,y,w,h,lines,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.16',facecolor=color+'18',edgecolor=color,linewidth=1.8))
    for i,line in enumerate(lines):ax.text(x+w/2,y+h-(i+.7)*h/len(lines),line,ha='center',va='center',fontsize=14,color='#172334')
def arrow(x1,x2,y):ax.annotate('',xy=(x2,y),xytext=(x1,y),arrowprops={'arrowstyle':'->','lw':1.7,'color':GRAY})
box(.3,2.9,2.1,1.35,[r'$\mu=D\delta$',r'$F_\mu(z)=z$'],RED)
box(3.0,2.9,3.4,1.35,[r'$F_\mu(0)=\mu(1)=0$',r"$F'_\mu(0)=1,\quad\mu(x)=i$"],RED)
box(7.1,2.9,4.45,1.35,[r'$F_\mu/P(-z)=1/z$',r'Pole; no compact inverse'],RED)
arrow(2.58,2.84,3.57);arrow(6.57,6.94,3.57)
box(.3,.7,2.1,1.35,[r'$\mu=D^2\delta$',r'$F_\mu(z)=z^2$'],GREEN)
box(3.0,.7,3.4,1.35,[r'$F_\mu(0)=\mu(1)=0$',r"$F'_\mu(0)=0,\quad\mu(x)=0$"],GREEN)
box(7.1,.7,4.45,1.35,[r'$F_\mu/P(-z)=1$',r'$v=\delta,\quad D^2v=\mu$'],GREEN)
arrow(2.58,2.84,1.37);arrow(6.57,6.94,1.37)
ax.text(6,.1,'An order-two root requires both moments. Boxes show pairings, not densities.',ha='center',fontsize=11,color=GRAY)
save(fig,'double-root-moments')

geometry={
 'schema':'AN02-CF042-original-geometry/v1','license':'CC0',
 'CF-A':{'K':[[-1,1],[-.5,.5]],'eta':[1,0],'test_carrier_center':[2,0],
          'test_carrier_radius':'1/4','support_indicator':'1','minimum_projection':'7/4','gap':'3/4',
          'proof':'CF9–CF13; Theorem CF2.1','schematic_scope':'Test carrier only, not a distribution density.'},
 'CF-B':{'roots':[-1,1,2],'degree':3,'leading_coefficient':1,'epsilon':'1/12',
          'safe_radius':'3/2','outer_radius':2,'example_product_lower_bound':'1/8',
          'general_product_lower_bound':'1/1728','Cauchy_example_constant':8,
          'proof':'CF14–CF19; Lemma CF3.1 and Theorem CF3.2'},
 'CF-C':{'symbol':'z^2','D':'-i partial','transpose':'D^2',
          'first_data':{'mu':'D delta','transform':'z','constant_pairing':0,'linear_pairing':'i',
                        'F_prime_at_zero':1,'quotient':'1/z','compact_inverse':False},
          'second_data':{'mu':'D^2 delta','transform':'z^2','constant_pairing':0,'linear_pairing':0,
                         'F_prime_at_zero':0,'quotient':1,'compact_inverse':'delta'},
          'proof':'CF22–CF26; Theorem CF5.1; Example CF7.2'}
}
(OUT/'geometry.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':3,'portable_outputs':6,'geometry':'figures/geometry.json'}))
