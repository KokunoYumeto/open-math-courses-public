"""CC0 reproducible exact-domain diagram for Proposition 52.2a.

Run with Python and matplotlib to produce SVG and PNG beside this file.
Boxes and coordinates are schematic; the labels retain actual map domains.
"""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'normal-core-extension-v28',
                     'svg.fonttype':'path','font.size':21})
W,H=1600,1430
fig=plt.figure(figsize=(16,14.3),dpi=100)
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,W); ax.set_ylim(H,0); ax.axis('off')
fig.patch.set_facecolor('#f8fafc')
ink='#173047'; blue='#216997'; green='#23775b'; muted='#43586a'

def label(x,y,t,size=22,color=ink,align='left'):
    t=re.sub(r'\\mathcal\s+([A-Za-z])',r'\\mathcal{\1}',t)
    ax.text(x,y,t,fontsize=size,color=color,va='top',ha=align,linespacing=1.35)
def box(x,y,w,h,title,body,color='#ffffff'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=10',
                              facecolor=color,edgecolor=ink,linewidth=1.7))
    label(x+20,y+18,title,25)
    label(x+20,y+60,body,20,muted)
def arrow(x1,y1,x2,y2,color=blue):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=22,
                                linewidth=2.4,color=color))
def panel(y,h,color):
    ax.add_patch(FancyBboxPatch((30,y),1540,h,boxstyle='round,pad=0,rounding_size=14',
                              facecolor=color,edgecolor='#c7d3dc',linewidth=1.2))

label(45,25,'The canonical expectation from a physical reduction',31)
label(45,76,'Proposition 52.2a · all actual cores · arbitrary centers and Hilbert-space cardinality',20,muted)

panel(120,485,'#eaf2f8')
label(55,138,'Actual operator domains and the normal maps',24,blue)
box(65,190,560,115,r'$\mathcal B=\langle M,e\rangle\subset B(H)$',r'$H=L^2(M),\quad e=e_R^M$', '#ffffff')
box(65,425,560,115,r'$\mathcal A=\langle N,e\rangle\subset B(H)$',r'$e\in\mathcal A\subset\mathcal B$; full central support', '#eef8f1')
box(970,425,565,115,r'$\mathcal A_{\rm std}=\langle N,e_S^N\rangle$',r'acts on $K=L^2(N)=pH$', '#ffffff')
arrow(335,312,335,414,green)
label(55,339,r'$E_{\mathcal A}=\Phi^{-1}C$',22,green)
arrow(635,482,955,482,green)
label(795,437,r'$\Phi$ normal *-isomorphism',18,green,'center')
arrow(640,280,1230,412,blue)
label(740,338,r'$C(T)=pTp|_K$',21,blue)
box(970,190,565,132,r'$p=e_N^M\in\mathcal A^{\prime}$',
    r'$pe=ep,\quad e|_K=e_S^N$'+'\n'+r'$p\in\mathcal A$ or $p\in\mathcal B$ is not assumed', '#f1f6fc')
label(70,565,r'$E_{\mathcal A}|_M=E_N$     ·     normal, faithful, UCP and $\mathcal A$-bimodular',21,green)

panel(635,355,'#eef6f0')
label(55,651,'The full e-corners give the entire semifinite trace identity',24,green)
box(65,710,465,98,r'$e\mathcal B e=Re$',r'$\operatorname{Tr}_{\mathcal B}(re)=\tau_R(r)$')
box(1065,710,465,98,r'$e\mathcal A e=Se$',r'$\operatorname{Tr}_{\mathcal A}(se)=\tau_S(s)$')
arrow(545,760,1050,760,green)
label(800,712,r'$re\longmapsto E_S(r)e$',22,green,'center')
label(800,782,r'$\tau_R(r)=\tau_S(E_S(r))$',21,green,'center')
label(70,841,r'$v_i\in\mathcal A e,\quad v_i^*v_i\leq e,\quad q_i=v_iv_i^*,\quad \sum_iq_i=1$',23)
label(70,888,r'$\operatorname{Tr}_{\mathcal B}(T)=\sum_i\tau_R(r_i)'
      r'=\sum_i\tau_S(E_S(r_i))=\operatorname{Tr}_{\mathcal A}(E_{\mathcal A}T)$',22)
label(70,942,r'Sums are suprema over finite subsets. The positive net is $T^{1/2}q_FT^{1/2}\uparrow T$.',20,muted)

panel(1020,340,'#f5f0e6')
label(55,1037,'A nonfactor canonical-square fixture: n = 2, r = 3',24,'#865f1c')
label(55,1080,'A genuine commuting square with a common basis; no arbitrary-P tunnel-core realization is asserted.',18,muted)
box(65,1130,610,137,r'$\mathcal B=P\,\bar\otimes\,(\mathrm{Mat}_6\oplus\mathrm{Mat}_6)$',
    r'corner $e$: rank 3 in each block'+'\n'+r'trace coefficient $1/6$ in each block')
box(920,1130,610,137,r'$\mathcal A=P\,\bar\otimes\,(\mathrm{Mat}_2\oplus\mathrm{Mat}_2)$',
    r'corner $e$: rank 1 in each block'+'\n'+r'trace coefficient $1/2$ in each block')
arrow(690,1205,905,1205,'#865f1c')
label(800,1154,r'$\mathrm{id}\otimes\mathrm{tr}_3$',20,'#865f1c','center')
label(70,1293,r'$\operatorname{Tr}_{\mathcal A}(e)=\operatorname{Tr}_{\mathcal B}(e)=1,\quad'
      r'\operatorname{Tr}_{\mathcal A}(1)=\operatorname{Tr}_{\mathcal B}(1)=2$',22)
label(70,1333,'Here p has rank one in the last standard leg and lies in A′, but not in A or B.',19,muted)

label(45,1383,'Proofs: 52.7a–52.7m and 52.7j.1–52.7j.4. Human context: Popa (1994), Example 2.3.3(a). CC0.',17,muted)
fig.savefig(HERE/'normal-core-extension-v28.svg',format='svg',metadata={'Date':None})
fig.savefig(HERE/'normal-core-extension-v28.png',format='png',dpi=110,
            metadata={'Software':'Normal canonical core expectation, CC0'})
plt.close(fig)
print('Wrote reproducible SVG and PNG; diagram coordinates are schematic.')
