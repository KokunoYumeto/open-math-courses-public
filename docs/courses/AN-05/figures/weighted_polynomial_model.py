"""Exact weighted polynomial model, physical packets and exponent comparison. CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'axes.titlesize':17})
fig=plt.figure(figsize=(15,10.4),dpi=140,facecolor='#fcfcf9')
chain=fig.add_axes([.045,.74,.91,.17]);chain.axis('off')
chain.set_xlim(0,1);chain.set_ylim(0,1)
nodes=[(.16,r'$q=\eta+\rho tz^2/2$',1),(.46,r'$\rho z^2/2$',2),(.70,r'$\rho z$',3),(.92,r'$\rho$',4)]
for x,formula,length in nodes:
    chain.text(x,.45,formula,ha='center',va='center',fontsize=21,
        bbox={'boxstyle':'round,pad=.5','fc':'#eaf2f3','ec':'#176887','lw':1.5})
    chain.text(x,.015,f'{length} '+('leaf' if length==1 else 'leaves'),ha='center',fontsize=13)
for x0,x1,label in [(.29,.385,r'$\{\tau,\,\cdot\}$'),(.535,.65,r'$\{q,\,\cdot\}$'),(.75,.865,r'$\{q,\,\cdot\}$')]:
    chain.annotate('',xy=(x1,.45),xytext=(x0,.45),arrowprops={'arrowstyle':'->','lw':2,'color':'#176887'})
    chain.text((x0+x1)/2,.89,label,ha='center',fontsize=17)
ax=fig.add_axes([.08,.29,.41,.32]);ax.set_facecolor('#fcfcf9')
for r,col in zip([1,16,256],['#176887','#a56b14','#a33828']):
    half=.5*r**(-.25)
    ax.add_patch(Rectangle((-half,-half),2*half,2*half,fill=False,lw=2.2,linestyle='--',edgecolor=col,label=f'ρ = {r}'))
ax.axhline(0,lw=.7,color='#777777');ax.axvline(0,lw=.7,color='#777777')
ax.set_xlim(-.59,.59);ax.set_ylim(-.59,.59);ax.set_aspect('equal',adjustable='box')
ax.set_xlabel(r'Time $t$');ax.set_ylabel(r'Spatial coordinate $z$')
ax.set_title('Physical support enclosures',pad=13)
ax.legend(loc='upper right',fontsize=11,framealpha=.95)
ax.grid(alpha=.12)
ex=fig.add_axes([.58,.30,.35,.30]);ex.set_facecolor('#fcfcf9')
vals=[1/8,1/4,2**(-.3)]
ex.barh([0,1,2],vals,color=['#176887','#555555','#a33828'],height=.55)
ex.set_yticks([0,1,2],['Proved model gain','Packet upper bound','Impossible claimed gain'],fontsize=11)
ex.tick_params(axis='y',pad=8)
ex.set_xlim(0,.99);ex.set_xlabel('Exponent of ρ')
ex.set_title('The equation norm scales as ρ¹ᐟ⁴',pad=14)
for y,val,label in zip([0,1,2],vals,[r'$1/8$',r'$1/4$',r'$2^{-3/10}$']):
    ex.text(val+.017,y,label,va='center',fontsize=14)
ex.spines[['top','right','left']].set_visible(False);ex.grid(axis='x',alpha=.14)
fig.suptitle('Weighted model: G = 1, F = ρtz²/2, with ρ ≥ 1',fontsize=22,y=.966)
fig.text(.055,.675,'Canonical convention: {τ,t} = {η,z} = 1. All words of length ≥ 5 vanish.\n'
    'At t = z = τ = 0, the full bracket maximum is max(|η|, ρ); its minimum is ρ.',fontsize=13,linespacing=1.55)
fig.text(.055,.197,r'$v_\rho(t,z)=\rho^{1/4}\varphi(\rho^{1/4}t,\rho^{1/4}z),\quad \|\varphi\|=1,\quad \varphi\in C_c^\infty((-1/2,1/2)^2)$',fontsize=17)
fig.text(.055,.153,'Dashed squares enclose the supports: |t|, |z| ≤ ½ρ⁻¹ᐟ⁴. Squared amplitude ρ¹ᐟ² cancels the area Jacobian.',fontsize=12)
fig.text(.055,.116,r'$m_1=13/10,\ m_2=1/10:\quad \mathrm{wt}(tz^2)=6/5<13/10;\quad (F/G)_t=\rho z^2/2\geq0.$',fontsize=13)
fig.text(.055,.080,'The source mixed-error contribution is ρ⁻²² × ρ¹ = ρ⁻²¹. The entire real-weight class has a separate proved gain 1/4096.',fontsize=12)
fig.text(.055,.027,'Original diagram by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. CC0.\n'
    'Self-checked draft; no independent review. Proof: lesson (7.3)–(7.7), Theorem 1.1, Corollary 7.1. Reference: Hörmander, IV, Lemma 27.5.4.',fontsize=10,color='#454545')
out=Path(__file__).with_name('weighted-polynomial-model.png')
fig.savefig(out,dpi=140,metadata={'Software':'Matplotlib; original CC0 diagram'})
plt.close(fig)
