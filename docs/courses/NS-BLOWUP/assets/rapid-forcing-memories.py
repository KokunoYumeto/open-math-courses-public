"""Exact memory maps for the rapid-forcing proof, RC0–RC9."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none',
    'mathtext.fontset':'dejavusans','font.size':15})
fig=plt.figure(figsize=(14,18),dpi=100,facecolor='#f6f8fb')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ink='#17304a'
def txt(x,y,s,size=16,**kw):ax.text(x,y,s,color=ink,fontsize=size,va='top',**kw)
def box(x,y,w,h,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012,rounding_size=.008',
        facecolor=color,edgecolor='#8fa9be',linewidth=1.1))
def arrow(x1,y1,x2,y2):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=18,
        color='#426b91',linewidth=1.8))
txt(.5,.974,'Three exact memories with rapidly vanishing forcing',25,ha='center',weight='bold')
txt(.5,.943,'One machine step per unit physical time; every old record remains.',17,ha='center')

box(.055,.705,.89,.195,'#e4edf6')
txt(.075,.884,'RC2–RC3  |  Addressed moving curls',20,weight='bold')
txt(.08,.852,r'$y_n=\sum_{j=0}^{n}\delta_jk_j$',20)
arrow(.34,.834,.435,.834)
txt(.455,.852,r'$(y_n/\delta_n)\operatorname{mod} M_n=k_n$',20)
txt(.08,.81,r'$c_{n,m}=(-1,m\delta_n,0)+\theta(\sigma)d_{n,m}$',19)
txt(.08,.777,r'$d_{n,m}=(-b_nh_n(k),\ \delta_{n+1}F_n(k),\ 0)$',19)
txt(.08,.743,r'$b_n\leq\delta_n^{\,n+10}<\delta_n/8$',18)
txt(.49,.743,'Disjoint moving supports keep addresses apart.',15)

box(.055,.478,.89,.195,'#e6f0e8')
txt(.075,.657,'RC4–RC5  |  Alternating fractional memories',20,weight='bold')
txt(.08,.622,r'Even slot: donor $x$ fixed',18)
arrow(.395,.607,.485,.607)
txt(.505,.622,r'$y\longmapsto y+\epsilon_{n+1}C_{n+1}$',19)
txt(.08,.585,r'Odd slot: donor $y$ fixed',18)
arrow(.395,.57,.485,.57)
txt(.505,.585,r'$x\longmapsto x+\epsilon_{n+1}C_{n+1}$',19)
txt(.08,.546,r'$z:\ -\epsilon_n\longmapsto-\epsilon_{n+1}$  if nonhalting',18)
txt(.08,.512,r'$z:\ -\epsilon_n\longmapsto+\epsilon_{n+1}$  at the first halt',18)

box(.055,.251,.89,.195,'#f4ecdd')
txt(.075,.43,'RC6–RC7  |  Periodic lattice memory',20,weight='bold')
txt(.08,.394,r'$j_*=(Y_2-y_*)/\epsilon_n,\quad j_*\operatorname{mod} P_n=c_n,\quad y_*=1/2$',19)
txt(.08,.355,r'$\Delta Y_2=\sigma(\tau)\epsilon_{n+1}F_n(j_*)<\epsilon_n/4$',19)
txt(.08,.32,'The whole write stays inside the selector plateau.',17)
txt(.08,.287,r'$Y_1:\ 1/2-\beta_n\longmapsto1/2+\beta_{n+1}$  at the first halt',18)

box(.055,.073,.89,.146,'#e4e8f3')
txt(.075,.203,'The original incompressible lift and complete force',20,weight='bold')
txt(.08,.169,r'$U=(\eta^\prime(z)v_1,\ \eta^\prime(z)v_2,\ -\eta(z)\operatorname{div}_{\xi}v)$',19)
txt(.08,.135,r'$\eta(1/2)=0,\quad\eta^\prime(1/2)=1:\quad U|_{z=1/2}=(v,0)$',18)
txt(.08,.102,r'$g=U_t+(U\cdot\nabla)U-\nu\Delta U,\qquad f=g-\nabla\phi,\quad p=-\phi$',19)
txt(.5,.049,'Exact construction maps, not sampled trajectories. Detector signals shrink with the slot index.',14,ha='center')
txt(.5,.026,'Source: OpenAI, Computation under Rapidly Vanishing Navier–Stokes Forcing (2026); proof RC0–RC9.',13,ha='center')
out=Path(__file__).with_suffix('')
fig.savefig(out.with_suffix('.svg'),metadata={'Date':None})
fig.savefig(out.with_suffix('.png'))
plt.close(fig)
p=out.with_suffix('.svg')
p.write_text(p.read_text(encoding='utf8').replace('width="1008pt" height="1296pt"',
    'width="1400" height="1800"'),encoding='utf8')
