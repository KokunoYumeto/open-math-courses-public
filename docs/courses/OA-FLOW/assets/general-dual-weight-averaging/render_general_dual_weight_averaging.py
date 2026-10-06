"""Original reproducible proof illustration; CC0-1.0 to the extent of rights held."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 15,
                     'svg.fonttype': 'none', 'svg.hashsalt': 'GDA-20261005'})
fig = plt.figure(figsize=(18, 13), dpi=200, facecolor='#f4f7fb')
grid = fig.add_gridspec(2, 2, left=.055, right=.965, bottom=.055, top=.875,
                       wspace=.17, hspace=.25)
axes = [fig.add_subplot(grid[i, j]) for i in range(2) for j in range(2)]
for ax in axes:
    ax.set_facecolor('white')
    for spine in ax.spines.values(): spine.set_color('#cad5e3')
fig.suptitle('Whole-cone averaging of general dual weights', fontsize=27,
             fontweight='bold', y=.973, color='#152d49')
fig.text(.5, .923, 'Directed positive kernels  •  exact coefficient values  •  normalized comparison  •  infinite values',
         ha='center', fontsize=16, color='#40546e')

ax = axes[0]; ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
ax.set_title('A  Arbitrary-group proof mechanism', loc='left', fontweight='bold', pad=16)
def box(y, text, color='#edf3fb'):
    ax.add_patch(FancyBboxPatch((.025, y), .95, .15,
                 boxstyle='round,pad=.014', facecolor=color, edgecolor='#a6bdd9'))
    ax.text(.5, y+.075, text, ha='center', va='center', fontsize=15)
box(.79, r'$p\in\mathcal{P}^\circ$: directed strict normal minorants')
box(.55, r'$F_p(X)=V_p^*(X\otimes1)V_p$'+'\n'+r'$F_p(\lambda_s)=p(s)\lambda_s$', '#e9f5f4')
box(.29, r'$S(X)=\sup_p F_p(X)\in\widehat{Q}_+$'+'\n'+r'$S(A_\xi)(\omega_\eta)=\int\delta(t)|\langle\xi(t),\eta(t)\rangle|^2dt$')
box(.045, r'$X\in R_+\ \Longrightarrow\ T(X)\in\widehat{R\cap Q}_+$'+'\n'+r'$R\cap Q=\pi(M)$', '#fff4df')
for y in [.75, .51, .25]:
    ax.add_patch(FancyArrowPatch((.5, y), (.5, y-.055), arrowstyle='-|>',
                 mutation_scale=24, color='#547696', linewidth=2))

ax = axes[1]; ax.axis('off'); ax.set_title('B  Counting measure on a two-point group', loc='left', fontweight='bold', pad=16)
rank=np.array([[1,2],[2,4]]); diagonal=np.diag([1,4])
def matrix(parent, rect, values, title, signed=False):
    a=parent.inset_axes(rect)
    a.imshow(values,cmap='RdBu' if signed else 'Blues',vmin=-1 if signed else 0,
             vmax=1 if signed else 4,interpolation='nearest')
    for (i,j), value in np.ndenumerate(values):
        a.text(j,i,str(int(value)),ha='center',va='center',fontsize=21,
               color='white' if abs(value)>=3 or (signed and abs(value)==1) else '#14334d',fontweight='bold')
    a.set_xticks([]); a.set_yticks([]); a.set_title(title,fontsize=17,pad=12)
    for spine in a.spines.values():spine.set_color('#adc2d8')
    return a
matrix(ax,[.015,.37,.37,.43],rank,r'$A_{(1,2)}$')
matrix(ax,[.61,.37,.37,.43],diagonal,r'$S(A_{(1,2)})$')
ax.text(.50,.57,r'$S$',ha='center',fontsize=22,color='#376487')
ax.annotate('',xy=(.59,.55),xytext=(.405,.55),xycoords='axes fraction',
            arrowprops={'arrowstyle':'-|>','color':'#376487','lw':2})
ax.text(.5,.25,r'$S(A_\xi)(\omega_\eta)=|\eta_0|^2+4|\eta_1|^2$',ha='center',fontsize=17)
ax.text(.5,.11,'Exact rank-one → rank-two diagonal value\n'+r'$\delta=1$; no sampled-form inference',ha='center',fontsize=15,color='#40546e')

ax=axes[2]; ax.axis('off'); ax.set_title('C  The same T transports two matrix weights',loc='left',fontweight='bold',pad=16)
u=np.array([[0,-1],[1,0]]); piu=np.block([[u,np.zeros((2,2),dtype=int)],[np.zeros((2,2),dtype=int),-u]])
matrix(ax,[.035,.11,.39,.62],piu,r'$\pi(u_{r_*})$',signed=True)
ax.text(.49,.83,r'$d=\mathrm{diag}(1,3),\quad e=R dR^*$',fontsize=15)
ax.text(.49,.69,r'$q=I+E_{22}=\mathrm{diag}(1,2)$',fontsize=15)
ax.text(.49,.55,r'$\widehat\varphi(L_x^*L_x)=7$',fontsize=18,color='#1a6385')
ax.text(.49,.44,r'$\widehat\psi(L_x^*L_x)=6$',fontsize=18,color='#aa4057')
ax.text(.49,.29,r'$u_r=e^{ir}d^{-ir},\quad r_*={\pi}/{\log3}$',fontsize=15)
ax.text(.49,.16,'4×4 faithful regular model\nWeight GNS dimension: 8',fontsize=14,color='#40546e')
ax.text(.5,.018,r'$(D\widehat\psi:D\widehat\varphi)_r=\pi((D\psi:D\varphi)_r)$',ha='center',fontsize=16)

ax=axes[3]; ax.set_title('D  A bounded identity with infinite value',loc='left',fontweight='bold',pad=16)
eps=np.geomspace(1/16,1,180)
ax.plot(eps,2/(3*eps),color='#177f8b',lw=3)
ax.set_xscale('log',base=2);ax.set_xticks([1/16,1/8,1/4,1/2,1],['1/16','1/8','1/4','1/2','1'])
ax.set_xlim(1/17,1.06);ax.set_ylim(0,12.4);ax.set_xlabel(r'$\varepsilon$',fontsize=18)
ax.set_ylabel(r'Exact lower bound $2/(3\varepsilon)$',fontsize=15)
ax.grid(color='#d9e3ee',lw=.7);ax.tick_params(labelsize=14)
ax.text(.96,.92,r'$G=\mathbb{R}$, Lebesgue Haar'+'\n'+r'$f_\varepsilon(t)=\varepsilon^{-1}(1-|t|/\varepsilon)_+$',
        transform=ax.transAxes,ha='right',va='top',fontsize=15,
        bbox={'facecolor':'white','edgecolor':'#cad5e3','boxstyle':'round,pad=.4'})
ax.text(.96,.60,r'$\|\lambda(f_\varepsilon)\|\leq1$'+'\n'+r'$T(I)\geq2/(3\varepsilon)$ for every $\varepsilon>0$'+'\n'+r'$\Longrightarrow\ T(I)=+\infty$',
        transform=ax.transAxes,ha='right',va='top',fontsize=16,
        bbox={'facecolor':'#fff4df','edgecolor':'#d5bf8f','boxstyle':'round,pad=.4'})
ax.text(.97,.18,'The curve plots lower bounds,\nnot finite values of T(I).',transform=ax.transAxes,ha='right',fontsize=14,color='#40546e')

data={'scope':'Panels B/C: counting Haar on Z/2; panel D: Lebesgue Haar on R; panel A: exact general theorem schematic.',
      'rank_one':rank.tolist(),'diagonal_value':diagonal.tolist(),'d':[[1,0],[0,3]],
      'e':[[2,-1],[-1,2]],'q':[[1,0],[0,2]],'phi_q':7,'psi_q':6,
      'cocycle_time':'pi/log(3)','pi_cocycle_at_time':piu.tolist(),
      'real_group_bound':{'formula':'2/(3*epsilon)','valid_domain':'epsilon>0',
                          'plotted_epsilon_interval':['1/16','1'],
                          'exact_samples':[['1/16','32/3'],['1/8','16/3'],['1/4','8/3'],['1/2','4/3'],['1','2/3']]},
      'dimensions':[3600,2600],'licence':'CC0-1.0 to the extent of rights held'}
(ROOT/'figure-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
fig.savefig(OUT/'general-dual-weight-averaging.png',dpi=200,metadata={'Software':'Original GDA proof figure'})
fig.savefig(OUT/'general-dual-weight-averaging.svg',metadata={'Date':'2026-10-05','Creator':'Original GDA proof figure'})
plt.close(fig)
