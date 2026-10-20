"""Exact interval model C7 and a smooth separating test. GPT-6 Astra (OpenAI), CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':13,'svg.fonttype':'none','axes.spines.top':False,
                     'axes.spines.right':False,'axes.spines.left':False})
def step(t):
    t=np.asarray(t,dtype=float)
    out=np.zeros_like(t);out[t>=1]=1
    m=(t>0)&(t<1)
    a=np.exp(-1/t[m]);b=np.exp(-1/(1-t[m]))
    out[m]=a/(a+b)
    return out
def phi(x):
    # Increase only in the gap I4--I3; decrease beyond I1.
    return step((27*x-.5)/.3)*step((.41-x)/.03)
fig,axs=plt.subplots(2,1,figsize=(11,6.8),layout='constrained')
for ax,scale,limit,tail,label in [
    (axs[0],1,.43,5,r'$x$'),
    (axs[1],27,1.3,5,r'$z=27x$ (magnified near $I_3$)')]:
    xx=np.linspace(-.02,limit,2500)
    ax.plot(xx,phi(xx/scale),color='#222c43',lw=2,label=r'smooth test $\phi_3$')
    for j in range(1,5):
        lo,hi=scale*(8/9)*3.**(-j),scale*(10/9)*3.**(-j)
        if lo>limit:continue
        color='#c86a15' if j<=3 else '#247791'
        ax.plot([lo,hi],[-.13,-.13],color=color,lw=7,solid_capstyle='butt')
        ax.scatter([scale*3.**(-j)],[-.13],color=color,s=36,zorder=3)
        if scale==27 or j<=2:
            ax.text((lo+hi)/2,-.28,rf'$I_{j}$',ha='center',color=color)
    tail_end=scale*(10/9)*3.**(-tail)
    ax.axvspan(0,tail_end,ymin=.08,ymax=.19,color='#247791',alpha=.15)
    ax.scatter([0],[-.13],s=36,color='#247791',zorder=4)
    ax.set_xlim(-limit*.035,limit)
    ax.set_ylim(-.42,1.3)
    ax.set_yticks([0,1]);ax.set_xlabel(label)
    ax.grid(axis='y',alpha=.15)
axs[0].set_title('Constant near every component; transitions stay in the gaps',loc='left',pad=12)
axs[0].text(.16,.53,r'$\phi_3=1$ near $I_1,I_2,I_3$',color='#c86a15')
axs[0].text(.16,.25,r'$u(\phi_3)=3,\quad \phi_3^{(r)}|_F=0\ (r\geq1)$')
axs[0].annotate(r'$I_3$',xy=(3**-3,-.13),xytext=(.065,-.33),
                ha='center',arrowprops={'arrowstyle':'-','color':'#c86a15'},color='#c86a15')
axs[1].text(.02,.52,r'$\phi_3=0$ near the entire tail',color='#247791')
axs[1].annotate(r'$0$ and $I_j,\ j\geq5$',xy=(.065,-.15),xytext=(.18,-.36),
                ha='center',arrowprops={'arrowstyle':'-','color':'#247791'},color='#247791')
axs[1].text(.88,.42,r'$I_3=[8/9,10/9]$ in $z$',fontsize=12,ha='center',color='#c86a15')
fig.savefig(OUT/'disconnected-support-jets.png',dpi=160)
fig.savefig(OUT/'disconnected-support-jets.svg',metadata={'Creator':'GPT-6 Astra (OpenAI); CC0'})
p=OUT/'disconnected-support-jets.svg'
p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
print('Saved exact interval model and its smooth test.')
