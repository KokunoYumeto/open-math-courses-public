"""Reproduce the BFQ operator diagram. CC0-1.0; schematic, no metric or trace-area scale."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'none'})
fig=plt.figure(figsize=(10,14),dpi=160,facecolor='#f7f9fc')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
def box(y,h,title,body,color):
 ax.add_patch(FancyBboxPatch((.06,y),.88,h,boxstyle='round,pad=0.014',facecolor=color,edgecolor='#7185a3',linewidth=1.2))
 ax.text(.085,y+h-.025,title,va='top',weight='bold',fontsize=16,color='#18314e')
 ax.text(.085,y+h-.062,body,va='top',linespacing=1.7,fontsize=14,color='#1c293a')
ax.text(.06,.975,'Common frames and central profiles',weight='bold',fontsize=25,va='top',color='#163d65')
ax.text(.06,.936,'The ordinary tunnel may be chosen after the physical targets.',fontsize=14,color='#52677e')
box(.724,.174,'BF gives a particular local support — BFQ.1–BFQ.9',
 'A unital cup-tail factor contains q; f commutes with that factor.\n'+
 r'$s=qf,\quad a=\tau(q),\quad T_S(s)=aT_S(f)$'+'\n'+
 r'$\|f-z\|_2<\eta\sqrt{\tau(f)}$'+'\n'+
 r'$\|T_S(s)-az\|_1<\eta^2\tau(s)$',
 '#e7effb')
box(.500,.165,'Return to one fixed core — BFQ.10–BFQ.15',
 r'$\Theta:S\subset R\ \longrightarrow\ \bar S\subset\bar R$'+'\n'+
 r'$p_j=s_jv_j\bar e\,v_j^*s_j\ \in\ \bar A$'+'\n'+
 r'$C_{\bar A}(p_j)=\Theta(T_S(s_j)),\quad c_j=\tau(s_j)$'+'\n'+
 'Finite physical errors use p_j; no ambient extension of Θ is needed.',
 '#e9f4ee')
box(.289,.151,'The affine inclusion obstructs BF — BFQ.3',
 r'BF would give $\delta_u(p)\to0$ and one-level error $\to0$.'+'\n'+
 r'IRG.13 gives $\liminf\inf_{t,z}\|C_{\bar A}(p)-tz\|_1/c\geq3/110$.'+'\n'+
 'The same actual index-ten pair and original traces occur on both sides.',
 '#fff0e0')
box(.079,.151,'Exact scope — BFQ.4 and the second local form',
 'Constant-multiplicity Følner input fails even with a freely chosen core.\n'+
 'Variable integer multiplicities and the first local form remain valid.\n'+
 'The bare second local form allows a more general tail projection s₀.\n'+
 'It does not include the cup-factor profile identity as a hypothesis.',
 '#eef0fa')
for hi,lo in [(.710,.685),(.486,.460),(.275,.249)]:
 ax.annotate('',xy=(.5,lo),xytext=(.5,hi),arrowprops=dict(arrowstyle='->',lw=2,color='#234d79'))
ax.text(.06,.034,'Proof locators: 46.6; 53.5; 57.14–57.35; IRG.13; BFQ.1–BFQ.17.',fontsize=11,color='#52677e')
ax.text(.06,.015,'Context: Popa (1994), Theorem 4.2.2 and Corollary 4.2.3, pp. 213–215.',fontsize=11,color='#52677e')
stem='bounded-frame-quantifiers'
fig.savefig(out/(stem+'.png'),dpi=160);fig.savefig(out/(stem+'.svg'))
p=out/(stem+'.svg');p.write_text(re.sub(r'[ \t]+(?=\r?$)','',p.read_text(),flags=re.M),encoding='utf-8')
