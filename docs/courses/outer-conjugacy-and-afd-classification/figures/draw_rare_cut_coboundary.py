"""Algebraic central levels in Theorem 4.1; lengths do not encode state masses."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'rare-cut-coboundary-v1','font.family':'DejaVu Sans'})
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

here=Path(__file__).resolve().parent
fig=plt.figure(figsize=(7.6,8.8),facecolor='white')
fig.text(.5,.951,'One exceptional wrap',ha='center',fontsize=20,color='#114e67')
fig.text(.5,.871,r'$V^{(a)}=\sum_{j=0}^{a-1}E_j b_j$',ha='center',fontsize=17)
ax=fig.add_axes([.04,.30,.92,.55]);ax.set_xlim(0,10);ax.set_ylim(-.45,5);ax.axis('off')
levels=[(4.1,r'$E_0$',r'$b_0=1$','#a33137','#fff0ef'),
        (2.9,r'$E_1$',r'$b_1=D^*$','#155f78','#edf7fa'),
        (1.7,r'$E_2$',r'$b_2=D^*\theta_\omega(D^*)$','#155f78','#edf7fa'),
        (.1,r'$E_{a-1}$',r'$b_{a-1}=D^*\cdots\theta_\omega^{a-2}(D^*)$','#155f78','#edf7fa')]
for y,label,formula,color,fill in levels:
    ax.add_patch(FancyBboxPatch((.65,y-.36),7.15,.72,boxstyle='round,pad=.04',facecolor=fill,edgecolor=color,lw=1.4))
    ax.text(1.65,y,label,ha='center',va='center',fontsize=16,color=color)
    ax.text(2.9,y,formula,ha='left',va='center',fontsize=14,color='#202020')
for top,bottom in [(4.1,2.9),(2.9,1.7)]:
    ax.annotate('',xy=(.28,bottom),xytext=(.28,top),arrowprops={'arrowstyle':'->','color':'#155f78','lw':1.8})
ax.text(.06,3.48,r'$\theta_\omega$',rotation=90,ha='center',va='center',fontsize=12,color='#155f78')
ax.plot([.28,.28],[1.33,.49],color='#155f78',lw=1.3,ls=':')
ax.text(4.1,.91,r'$\vdots$',ha='center',fontsize=22,color='#155f78')
ax.annotate('',xy=(7.95,4.1),xytext=(7.95,.1),arrowprops={'arrowstyle':'->','connectionstyle':'arc3,rad=.39','color':'#a33137','lw':2})
ax.text(9.62,2.13,'wrap',ha='center',rotation=90,fontsize=13,color='#a33137')
fig.text(.5,.259,r'$\theta_\omega(b_{j-1})=D b_j\quad(j\geq1)$',ha='center',fontsize=16,color='#155f78')
fig.text(.5,.204,r'$e_a=\theta_\omega(V^{(a)})-D V^{(a)}$',ha='center',fontsize=16)
fig.text(.5,.151,r'$e_a^*e_a,\ e_ae_a^*\leq4E_0$',ha='center',fontsize=16,color='#a33137')
fig.text(.5,.099,r'$\tau_\omega(E_0)\leq1/a\quad\Longrightarrow\quad\|e_a\|_\sharp^2\leq8/a$',ha='center',fontsize=15)
fig.text(.5,.041,'Theorem 4.1, equations (4.2)–(4.4).',ha='center',fontsize=10)
fig.text(.5,.019,'Central algebraic levels; box size does not represent state mass.',ha='center',fontsize=9,color='#555555')
fig.savefig(here/'rare-cut-coboundary.svg',metadata={'Date':None})
fig.savefig(here/'rare-cut-coboundary.png',dpi=150,metadata={'Software':'matplotlib'})
plt.close(fig)
