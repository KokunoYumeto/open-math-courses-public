from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

out=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none','svg.hashsalt':'generator-prefix-tests-v1'})
fig,ax=plt.subplots(figsize=(6.4,19.5));fig.patch.set_facecolor('white');ax.set_xlim(0,10);ax.set_ylim(0,31);ax.axis('off')
def box(y,h,color):
 ax.add_patch(FancyBboxPatch((.28,y),9.44,h,boxstyle='round,pad=0.10',facecolor=color,edgecolor='#24526d',linewidth=1.5))
def txt(y,text,size=21,color='#162e40',weight='normal'):
 ax.text(5,y,text,ha='center',va='center',fontsize=size,color=color,fontweight=weight)
def arrow(y1,y2):ax.annotate('',xy=(5,y2),xytext=(5,y1),arrowprops={'arrowstyle':'->','lw':2,'color':'#24526d'})
txt(30.1,'Keep the group generators fixed',23,weight='bold')
txt(29.3,'Transport the functional at each prefix',19)
for y,prefix,factor,test in [(24.8,'e',r'$u_a$',r'$[u_a,\psi]$'),(20.4,'a',r'$\delta_a(u_b)$',r'$[u_b,\psi\delta_a]$'),(16.0,'ab',r'$\delta_{ab}(u_a)$',r'$[u_a,\psi\delta_{ab}]$')]:
 box(y,3.75,'#eaf5ff');txt(y+3.05,'Prefix '+prefix,21,weight='bold');txt(y+1.93,'Factor '+factor,24);txt(y+.75,'Test '+test,22)
arrow(24.65,24.25);arrow(20.25,19.85)
txt(15.35,r'$u_{aba}=u_a\,\delta_a(u_b)\,\delta_{ab}(u_a)$',22)
box(9.55,4.85,'#e8f7ef');txt(13.6,'A word of length at most L',22,weight='bold');txt(12.55,'Generator bound a gives label bound La',18)
txt(11.38,r'$a=\dfrac{\varepsilon_f}{4\max(1,m)L}$',27)
txt(10.18,r'$mLa\leq\varepsilon_f/4$',24)
box(2.0,6.55,'#fff1e9');txt(7.76,'The exact quantifiers',23,weight='bold');txt(6.73,'Group inputs and outputs: the same S',19)
txt(5.70,r'Functional inputs: $\{\psi\delta_p:p\in P\}$',19)
txt(4.60,'The finite prefix list P depends on accuracy.',18)
txt(3.60,'Its transported functionals depend on δ.',18)
txt(2.60,'A quotient law remains a quotient law.',18)
txt(1.12,'Proof: (3.1)–(3.4), (5.3)–(5.4)',17)
txt(.38,'Word example in S3; no finite matrix central-freeness claim.',13)
fig.subplots_adjust(left=.03,right=.97,bottom=.015,top=.995)
fig.savefig(out/'generator-prefix-tests.svg',metadata={'Date':None,'Creator':'OA-CLASSIFY Writing AI'})
fig.savefig(out/'generator-prefix-tests.png',dpi=160,metadata={'Software':'OA-CLASSIFY Writing AI'})
plt.close(fig)
