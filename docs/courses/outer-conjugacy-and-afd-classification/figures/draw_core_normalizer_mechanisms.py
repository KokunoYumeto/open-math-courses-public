"""Reproducible exact indexed-orbit sample and algebraic tower cancellation."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'core-normalizer-v1','font.family':'DejaVu Sans'})
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
here=Path(__file__).resolve().parent
fig=plt.figure(figsize=(6.6,10.6),facecolor='white')
fig.text(.5,.966,'A core unitary and a central witness',ha='center',fontsize=19,color='#174b61')
fig.text(.5,.932,r'$G(x,r)=(Tx,r-R(x)),\quad R(x)\geq\delta>0$',ha='center',fontsize=16)
ax=fig.add_axes([.12,.595,.82,.30])
ax.set_xlim(-1.45,3.4);ax.set_ylim(-3.9,2.1)
ax.axhline(0,color='#666666',lw=1)
roofs=[1.,1.2,.8,1.6,1.]
points=[1.5,.5,-.7,-1.5,-3.1]
for k,j in enumerate(range(-1,4)):
    ax.add_patch(Rectangle((j-.19,0),.38,roofs[k],facecolor='#d9ecdf',edgecolor='#659478'))
    ax.scatter([j],[points[k]],s=45,color='#155f78',zorder=4)
    ax.text(j+.06,points[k]-.26,str(points[k]),fontsize=10,color='#174b61')
    if j<3:
        ax.annotate('',xy=(j+1,points[k+1]),xytext=(j,points[k]),arrowprops={'arrowstyle':'->','color':'#155f78','lw':1.6})
    ax.text(j,1.84,r'$R_{'+str(j)+r'}='+str(roofs[k])+'$',ha='center',fontsize=10)
ax.set_xticks(range(-1,4),[r'$x_{-1}$',r'$x_0$',r'$x_1$',r'$x_2$',r'$x_3$'],fontsize=13)
ax.set_ylabel('real coordinate r',fontsize=12)
ax.spines[['top','right']].set_visible(False)
fig.text(.5,.536,'Green: the slab 0 ≤ r < R(x) at each sampled base point.',ha='center',fontsize=11)
fig.text(.5,.506,r'$z_0=(x_0,0.5)\in D;\quad n(G^jz_0)=j$',ha='center',fontsize=16)
fig.text(.5,.475,r'$w(Gz)=d(\pi_X(Gz))w(z),\quad w\gamma(w^*)=d$',ha='center',fontsize=16)
fig.text(.5,.443,'Exact orbit sample; base spacing depicts no metric.',ha='center',fontsize=10,color='#555555')
fig.text(.5,.401,'The tower interior cancels',ha='center',fontsize=17,color='#174b61')
ax2=fig.add_axes([.06,.278,.88,.085]);ax2.axis('off');ax2.set_xlim(-.5,5.5);ax2.set_ylim(0,1)
for j in range(6):
    ax2.add_patch(Rectangle((j-.42,.17),.84,.56,facecolor=('#f7dec9' if j in [0,5] else '#dcecf2'),edgecolor='#174b61'))
    label=r'$e_n$' if j==0 else r'$\theta^{'+str(j)+r'}e_n$'
    ax2.text(j,.45,label,ha='center',va='center',fontsize=13)
    if j<5:ax2.annotate('',xy=(j+.53,.93),xytext=(j+.02,.93),arrowprops={'arrowstyle':'->','color':'#155f78','lw':1.4})
fig.text(.5,.257,'Height n = 5 is schematic; only levels 0–4 are disjoint.',ha='center',fontsize=11)
fig.text(.5,.225,r'$\theta(x_n)-x_n=\theta^n(ue_n)-ue_n$',ha='center',fontsize=17)
fig.text(.5,.188,r'$\mu(e_n)\leq 1/n,\quad \mu(\theta^ne_n)\leq 2/n$',ha='center',fontsize=16)
fig.text(.5,.15,r'$\|\theta(x_n)-x_n\|_\Phi^\sharp\leq(2+\sqrt{2})/\sqrt{n}$',ha='center',fontsize=16)
fig.text(.5,.111,r'$\|\alpha(x_n)-x_n\|_\Phi^\sharp\ \longrightarrow\ \sqrt{2}|1-y|>0$',ha='center',fontsize=16)
fig.text(.5,.077,'Endpoint box widths do not represent their measures or overlap.',ha='center',fontsize=10,color='#555555')
fig.text(.5,.043,'Lemma 3.1; Proposition 3.2, (3.6); Lemma 5.1; Proposition 6.1.',ha='center',fontsize=10)
fig.text(.5,.02,'Human source: Kawahigashi–Sutherland–Takesaki (1992), Lemmas 10–12.',ha='center',fontsize=9)
fig.savefig(here/'core-normalizer-mechanisms.svg',metadata={'Date':None})
fig.savefig(here/'core-normalizer-mechanisms.png',dpi=150,metadata={'Software':'matplotlib'})
plt.close(fig)
