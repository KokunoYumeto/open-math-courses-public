"""Original reproducible diagram for the exact linear polynomial parameter model. CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'axes.titlesize':17})
fig=plt.figure(figsize=(15,10.4),dpi=140,facecolor='#fcfcf9')
chain=fig.add_axes([.05,.72,.90,.19]);chain.axis('off')
chain.set_xlim(0,1);chain.set_ylim(0,1)
for x,formula,length in [(.13,r'$q=\rho z+t\eta$',1),(.50,r'$\eta$',2),(.86,r'$-\rho$',3)]:
    chain.text(x,.55,formula,ha='center',va='center',fontsize=23,
        bbox={'boxstyle':'round,pad=.55','fc':'#eaf2f3','ec':'#176887','lw':1.5})
    chain.text(x,.06,f'{length} '+('leaf' if length==1 else 'leaves'),ha='center',fontsize=13)
chain.annotate('',xy=(.43,.55),xytext=(.25,.55),arrowprops={'arrowstyle':'->','lw':2,'color':'#176887'})
chain.annotate('',xy=(.80,.55),xytext=(.56,.55),arrowprops={'arrowstyle':'->','lw':2,'color':'#176887'})
chain.text(.34,.88,r'$\{\tau,\,\cdot\}$',ha='center',fontsize=17)
chain.text(.68,.88,r'$\{q,\,\cdot\}$',ha='center',fontsize=17)
ax=fig.add_axes([.09,.28,.42,.31]);ax.set_facecolor('#fcfcf9')
colors=['#176887','#a56b14','#a33828']
for r,col in zip([1,8,64],colors):
    ht=r**(-1/3);hz=r**(-2/3)
    ax.add_patch(Rectangle((-ht,-hz),2*ht,2*hz,fill=False,lw=2.2,linestyle='--',edgecolor=col,label=f'ρ = {r}'))
ax.axhline(0,lw=.7,color='#777777');ax.axvline(0,lw=.7,color='#777777')
ax.set_xlim(-1.13,1.13);ax.set_ylim(-1.13,1.13)
ax.set_xlabel(r'Time $t$');ax.set_ylabel(r'Spatial coordinate $z$')
ax.set_title('Support enclosures for the test packets',pad=14)
ax.legend(loc='upper right',fontsize=12,framealpha=.95)
ax.grid(alpha=.12)
ex=fig.add_axes([.61,.28,.34,.31]);ex.set_facecolor('#fcfcf9')
vals=[.25,1/3,1/(2*np.sqrt(2))]
ex.barh([0,1,2],vals,color=['#176887','#555555','#a33828'],height=.55)
ex.set_yticks([])
for y,label in enumerate(['Valid halving gain','Packet upper bound','Impossible claimed gain']):
    ex.text(.008,y,label,va='center',fontsize=12,color='white')
ex.set_xlim(0,.45);ex.set_xlabel('Exponent of ρ')
ex.set_title('The energy is exactly of scale ρ¹ᐟ³',pad=14)
for y,v,label in zip([0,1,2],vals,[r'$1/4$',r'$1/3$',r'$1/(2\sqrt{2})$']):
    ex.text(v+.014,y,label,va='center',fontsize=14)
ex.spines[['top','right','left']].set_visible(False);ex.grid(axis='x',alpha=.14)
fig.suptitle('Exact linear model: q = ρz + tη, with ρ ≥ 1',fontsize=22,y=.965)
fig.text(.055,.665,'Canonical convention: {τ,t} = {η,z} = 1. All words of length ≥ 4 vanish.\n'
    'At t = z = τ = 0, the bracket maximum is max(|η|, ρ); its minimum is ρ.',fontsize=13,linespacing=1.55)
fig.text(.055,.16,r'$v_\rho(t,z)=\rho^{1/2}\varphi(\rho^{1/3}t,\rho^{2/3}z),\quad \|\varphi\|=1,\quad \varphi\in C_c^\infty((-1,1)^2)$',fontsize=17)
fig.text(.055,.115,'Dashed rectangles enclose the open supports: |t| < ρ⁻¹ᐟ³, |z| < ρ⁻²ᐟ³.',fontsize=12)
fig.text(.055,.081,r'Exact scaling: $\|D_t v_\rho\|=\rho^{1/3}\|D_T\varphi\|$ and $\|(\rho z+tD_z)v_\rho\|=\rho^{1/3}\|(Z+TD_Z)\varphi\|$.',fontsize=13)
fig.text(.055,.027,'Original diagram by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. CC0.\n'
    'Self-checked draft; no independent review. Proof: lesson (7.2)–(7.5), Corollary 7.1. Reference: Hörmander, IV, Lemma 27.5.3.',fontsize=10,color='#454545')
out=Path(__file__).with_name('polynomial-parameter-gain.png')
fig.savefig(out,dpi=140,metadata={'Software':'Matplotlib; original CC0 diagram'})
plt.close(fig)
