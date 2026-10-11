"""Bounded coordinates for the complete weak equation, MA07 (MA.26--28).

Free human background: Rieffel--Van Daele (1977), Lemmas 4.6--4.8.
The general positive-operator argument, including existence, is written in MA07.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.size':14,'svg.fonttype':'path','svg.hashsalt':'oa-mod-analytic-weak-equation-v1'})
fig=plt.figure(figsize=(12,6.4));ax=fig.add_axes([.025,.02,.95,.96]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.5,.975,'The weak equation has bounded coordinates',ha='center',va='top',fontsize=20,fontweight='bold')
ax.text(.5,.89,r'$R=2(I+A)^{-1},\quad C=\sqrt{R},\quad D=\sqrt{2I-R},\quad T=CD$',ha='center',fontsize=17)
ax.text(.5,.815,r'$\mathcal{V}=D(A^{1/2})\cap D(A^{-1/2})=\operatorname{ran}T$',ha='center',fontsize=16)
def box(x,y,w,h,label,color):
 ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=.014',facecolor=color,edgecolor='#32546b',linewidth=1.2))
 ax.text(x,y,label,ha='center',va='center',fontsize=17)
box(.22,.63,.24,.12,r'$\xi=Tu$', '#ecf4f7');box(.78,.63,.24,.12,r'$\eta=Tv$','#ecf4f7')
box(.22,.40,.36,.12,r'$A^{-1/2}\xi=C^2u$'+'\n'+r'$A^{1/2}\xi=D^2u$','#f0f5ed')
box(.78,.40,.36,.12,r'$A^{-1/2}\eta=C^2v$'+'\n'+r'$A^{1/2}\eta=D^2v$','#f0f5ed')
for x in [.22,.78]:ax.annotate('',(x,.48),(x,.55),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#32546b'})
ax.text(.5,.62,r'$u,v\in H$',ha='center',fontsize=16)
ax.text(.5,.535,'exact domains',ha='center',fontsize=12,color='#32546b')
box(.5,.205,.88,.12,r'$TXT=D^2YC^2+e^sC^2YD^2$', '#fcf0e8')
ax.text(.5,.086,r'$Y=e^{-s/2}\int_{\mathbb{R}}\frac{e^{-ist}}{2\cosh(\pi t)}\,A^{it}XA^{-it}\,dt$',ha='center',fontsize=17)
ax.text(.5,.012,'Every u,v is allowed. The strip identity proves existence and uniqueness. Proof: MA07, (MA.26)–(MA.28).',ha='center',fontsize=11)
out=Path(__file__).with_name('analytic-weak-equation.svg');fig.savefig(out,metadata={'Date':None,'Creator':'Original course illustration; MA07'});print(out)
