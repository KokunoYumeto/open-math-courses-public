"""Original exact log boundary and canonical localization diagram, CC0."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,2,figsize=(12.8,5.4),constrained_layout=True)
ink='#173d46';orange='#ad582b';green='#52776a'
ax=axes[0]
ax.axhline(0,color=ink,alpha=.25);ax.axvline(0,color=ink,alpha=.25)
ax.plot([-2,0],[0,0],color=orange,linewidth=4)
ax.scatter([0],[0],facecolors='white',edgecolors=orange,s=75,zorder=3)
ax.annotate(r'$\log(-1+i0)=+i\pi$',(-1,0),(-1.95,.55),fontsize=13,arrowprops={'arrowstyle':'->','color':ink})
ax.annotate(r'$\log(-1-i0)=-i\pi$',(-1,0),(-1.95,-.65),fontsize=13,arrowprops={'arrowstyle':'->','color':ink})
ax.text(-1.98,1.02,r'$\partial_w\log w=1/w+\pi\,\mathbf{1}_{a<0}\delta(b)$',fontsize=13,color=ink)
ax.text(-1.98,-1.13,r'$B_{\log}=\frac{1}{2i}\mathbf{1}_{a<0}\delta(b)$',fontsize=14,color=orange)
ax.text(-1.98,-1.47,'The ray correction is retained. There is no origin point mass.',fontsize=10,color=ink)
ax.set_xlim(-2.15,.35);ax.set_ylim(-1.65,1.35)
ax.set_xlabel(r'$a=\operatorname{Re}w$');ax.set_ylabel(r'$b=\operatorname{Im}w$')
ax.set_title('Exact principal-log boundary values',fontsize=14,color=ink)
ax.spines[['top','right']].set_visible(False)

ax=axes[1];ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.text(.21,.79,r'$h\circ P$',ha='center',fontsize=19,color=ink)
ax.text(.78,.79,r'$P$',ha='center',fontsize=19,color=ink)
ax.annotate('',(.68,.8),(.32,.8),arrowprops={'arrowstyle':'->','color':ink,'linewidth':2})
ax.text(.50,.87,r'$\partial_t\circ(h\circ P)=P$',ha='center',fontsize=12)
ax.text(.21,.40,r'$\kappa_0(h\circ P)$',ha='center',fontsize=18,color=ink)
ax.text(.78,.40,r'$\kappa_0(P)$',ha='center',fontsize=18,color=ink)
ax.annotate('',(.65,.42),(.35,.42),arrowprops={'arrowstyle':'->','color':green,'linewidth':2})
ax.text(.50,.48,r'$D_{\rm out}$',ha='center',fontsize=14,color=green)
for xpos in [.21,.78]:
    ax.annotate('',(xpos,.49),(xpos,.74),arrowprops={'arrowstyle':'->','color':ink,'linewidth':1.5})
    ax.text(xpos+.045,.62,r'$\kappa_0$',fontsize=13)
ax.text(.5,.22,r'$D_{\rm out}T_{h\circ P}-T_P=\bar\partial\mathcal{B}_{h\circ P,P,D}$',ha='center',fontsize=15,color=orange)
ax.text(.5,.12,r'$\operatorname{supp}\mathcal{B}_{h\circ P,P,D}\subset G$',ha='center',fontsize=14,color=orange)
ax.text(.5,.025,'The square commutes in the relative cone by its literal supported primitive.',ha='center',fontsize=10)
ax.set_title('Actual normal shift and canonical classes',fontsize=14,color=ink)
fig.suptitle('Why normal localization retains a supported correction',fontsize=19,color=ink)
fig.supxlabel('Proof: NL.2 (NL.7)-(NL.12), NL.4 (NL.22)-(NL.27). Free human context: Micro-hyperbolic systems §3.1; HolIII III.1 and IV.2.',fontsize=10)
fig.savefig(ROOT/'localization-correction.png',dpi=180)
fig.savefig(ROOT/'localization-correction.svg')
(ROOT/'localization-figure-data.json').write_text(json.dumps({'cut':{'real_interval_drawn':[-2,0],'imaginary_coordinate':0,'current_density_real_condition':'a<0','support_closure_includes_origin':True,'origin_point_mass':False},'exact_boundary_sample':{'real_coordinate':-1,'upper_log':'i*pi','lower_log':'-i*pi','jump':'2*pi*i'},'diagram':'Actual h-left shift under partial_t and its canonical class map; equality of current representatives includes dbar B.','proof':'NL.2 and NL.4','scope':'Exact boundary limits with schematic approach arrows and exact class square; no numerical distribution proof.'},indent=2)+'\n',encoding='utf-8')
