"""Reproducible map diagram for JB.1--JB.11; no area encodes a trace."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

D = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(13.2, 8.8))
fig.patch.set_facecolor('#fafcff')
ax.set(xlim=(0, 13.2), ylim=(0, 8.8))
ax.axis('off')
ax.text(.5, 8.35, 'A cost cut keeps the physical trace; its commutators still have a price',
        fontsize=17, weight='bold', color='#102947')
ax.text(.5, 7.93, 'Actual states and maps on the original B  •  no area represents a canonical trace',
        fontsize=11, color='#3b5270')

def box(x, y, w, h, title, lines, face='#eef5fd'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=.12',
                              facecolor=face, edgecolor='#4c6c92', linewidth=1.2))
    ax.text(x+.18, y+h-.35, title, fontsize=13, weight='bold', color='#17395e')
    for j, (text, size) in enumerate(lines):
        ax.text(x+.18, y+h-.84-.46*j, text, fontsize=size, color='#193754')
def arrow(x1, y1, x2, y2, label=None):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=15,
                                color='#315b86',linewidth=1.4))
    if label:
        ax.text((x1+x2)/2, (y1+y2)/2+.16, label, fontsize=10, ha='center', color='#24496d')
box(.6, 5.4, 4.5, 1.95, 'Available compatible hypertrace',
    [(r'$\psi E_A=\psi,\quad \psi|_M=\tau_M$',15),
     (r'$\psi(mx)=\psi(xm)$',15),
     ('Singular center restrictions are allowed.',10)])
box(7.25, 5.4, 5.35, 1.95, 'Smaller-center reweighting',
    [(r'$0\leq f\leq 1,\quad f\in Z(A),\quad t=\psi(f)>0$',13),
     (r'$\psi_f(T)=\psi(fT)/t$',15),
     (r'Exact $E_A$, $N$-centrality and physical $\tau_M$.',11)])
arrow(5.25,6.2,7.0,6.2,r'JB.8 / AS.3')
box(.6, 2.85, 5.65, 1.65, 'Actual finite physical tests',
    [(r'$r_i=\|T\mapsto \sigma(b_iT-Tb_i)\|_{B^*}$',14),
     (r'$\mathcal{E}_\sigma=\frac{\|w^{-1}\|}{d}\sum_i\|b_i\|r_i$',16)],
    face='#e9f7f1')
box(7.1, 2.85, 5.5, 1.65, 'Exact cost-cut norm',
    [(r'$\|\psi_f\,\mathrm{Ad}u-\psi_f\|=\psi(|u^*fu-f|)/t$',13),
     (r'$f\leq 1_{[0,\varepsilon]}(\mathfrak{a})'
      r'\ \Longrightarrow\ \psi_f(\mathfrak{a})\leq\varepsilon$',14)],
    face='#fff5e8')
arrow(9.8,5.2,9.8,4.68,'JB.9')
arrow(7.0,3.65,6.45,3.65)
box(.6,.6,12.0,1.4,'Unchanged original joint algebra and profile maps',
    [(r'$\|\alpha_\sigma-\alpha_\sigma P_0\|'
      r'\leq \sigma(\mathfrak{a})+\mathcal{E}_\sigma$',20),
     ('JB.4 and JB.11: a proved budget. Existence of a low-cost, low-error cut still needs proof.',11)],
    face='#f2edfa')
arrow(3.4,2.68,3.4,2.15,'JB.1')
arrow(10,2.68,10,2.15,'JB.2')
fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
for ext in ['svg','png']:
    fig.savefig(D/('cost-localization-and-state-return-v11.'+ext),dpi=130,
                facecolor=fig.get_facecolor())
p=D/'cost-localization-and-state-return-v11.svg'
p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)
(D/'budget-figure-check.json').write_text(json.dumps(dict(
    proof_locators=['JB.1','JB.4','JB.8','JB.9','JB.11','AS.3'],
    original_joint_algebra_and_both_canonical_traces_retained=True,
    trace_area_encoding=False, unrestricted_existence_claimed=False),indent=2)+'\n',encoding='utf-8')
