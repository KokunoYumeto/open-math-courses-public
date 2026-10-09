"""Original CC0 mathematical sections for E.1–E.3; exact coordinates below."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parent
epsilon=1/4
a=2
A=3
real_time=np.linspace(-2,0,401)
fig,axes=plt.subplots(1,3,figsize=(15,5.8),constrained_layout=True)
ink='#173d46';blue='#c8e4ed';orange='#ad582b'
for ax in axes:
    ax.set_facecolor('#f8faf8')
    ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=.18)

ax=axes[0]
ax.fill_between(real_time,epsilon*real_time,-epsilon*real_time,color=blue)
ax.plot(real_time,epsilon*real_time,color=ink)
ax.plot(real_time,-epsilon*real_time,color=ink)
ax.plot([-2,0],[0,0],color=orange,linestyle='--',linewidth=2.8,label='Thin negative ray')
ax.set_xlim(-2.15,.25);ax.set_ylim(-.7,.7)
ax.set_xlabel(r'$\operatorname{Re}w$');ax.set_ylabel(r'$\operatorname{Im}w$')
ax.set_title('Temporal section: spatial normal = 0',fontsize=12)
ax.text(-1.85,.45,r'$|\operatorname{Im}w|\leq \frac{1}{4}(-\operatorname{Re}w)$',fontsize=11)
ax.legend(loc='lower left',fontsize=10)

ax=axes[1]
ax.fill_between(real_time,A*real_time,-A*real_time,color=blue,label='Thick cone section')
ax.plot(real_time,A*real_time,color=ink);ax.plot(real_time,-A*real_time,color=ink)
ax.plot(real_time,a*real_time,color=orange,linestyle='--',linewidth=2)
ax.plot(real_time,-a*real_time,color=orange,linestyle='--',linewidth=2,label='Thin support boundary')
ax.set_xlim(-2.15,.25);ax.set_ylim(-6.5,6.5)
ax.set_xlabel(r'$\operatorname{Re}w$');ax.set_ylabel(r'$\operatorname{Re}\zeta$')
ax.set_title('Spatial section: both imaginary parts = 0',fontsize=12)
ax.text(-1.85,5.35,r'$|\zeta|\leq 3(-\operatorname{Re}w)$',fontsize=11)
ax.text(-1.7,1.0,r'$|\zeta|\leq 2(-\operatorname{Re}w)$',fontsize=11,color=orange)
ax.legend(loc='lower right',fontsize=9)

ax=axes[2]
final_input=-1.5
output=.5
intermediate=-.5
ax.plot([final_input,output],[0,0],color=ink,linewidth=4)
ax.scatter([final_input,intermediate,output],[0,0,0],s=[70,55,70],color=[orange,'#52776a',ink],zorder=3)
for xpos,label,ypos in [(final_input,r'Final input $v=-1.5$',.22),(intermediate,r'Intermediate $s=-0.5$',-.28),(output,r'Output $u=0.5$',.22)]:
    ax.annotate(label,(xpos,0),(xpos,ypos),ha='center',fontsize=10,arrowprops={'arrowstyle':'-','color':ink})
ax.annotate('',(final_input,.65),(intermediate,.65),arrowprops={'arrowstyle':'<->','color':orange})
ax.annotate('',(intermediate,.65),(output,.65),arrowprops={'arrowstyle':'<->','color':ink})
ax.text(-1,.73,r'$-\operatorname{Re}(v-s)=1$',ha='center',fontsize=10)
ax.text(0,.73,r'$-\operatorname{Re}(s-u)=1$',ha='center',fontsize=10)
ax.text(-.5,-.68,r'$-\operatorname{Re}(v-u)=2$',ha='center',fontsize=11)
ax.text(-.5,-.98,'Every intermediate real-time length is between 0 and 2.\n(E.8) bounds all other fibre coordinates.',ha='center',fontsize=10)
ax.set_xlim(-1.95,.95);ax.set_ylim(-1.25,1.15)
ax.set_xlabel('Real time; all imaginary and spatial coordinates = 0')
ax.set_yticks([])
ax.set_title('Proper fibre: exact real slice',fontsize=12)

fig.suptitle('Thick proper cone and bounded intermediate fibres',fontsize=18,color=ink)
fig.supxlabel('Exact sections, not the full complex cone. Proof: E.1, (E.7)–(E.8); angular regularization and finite-order current bounds: E.2–E.3.',fontsize=10)
fig.savefig(ROOT/'thick-cone-sections.png',dpi=180)
fig.savefig(ROOT/'thick-cone-sections.svg')
(ROOT/'thick-cone-figure-data.json').write_text(json.dumps({
    'epsilon':epsilon,'thin_spatial_slope':a,'thick_spatial_slope':A,
    'temporal_section':{'spatial_normal':0},
    'spatial_section':{'imaginary_time_normal':0,'imaginary_spatial_normal':0},
    'real_fibre':{'final_input':final_input,'intermediate':intermediate,'output':output,
                  'final_normal':final_input-output,'nonnegative_total_length':output-final_input},
    'proof':'E.1 (E.7)–(E.8), E.2–E.3',
    'human_sources':['Kashiwara–Schapira, freely accessible Micro-hyperbolic systems, §3.1',
                     'Kashiwara–Kawai, author-hosted HolIII, III.1/IV.2'],
    'scope':'Exact sections and real fibre sample; no numerical proof or whole-complex-cone claim.'
},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
