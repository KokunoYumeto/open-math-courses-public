"""Original exact diagram for OA-MOD-BF-02--04; no source artwork."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(9,14),dpi=100,facecolor='#fbfcfe')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,9);ax.set_ylim(0,14);ax.axis('off')
ink='#13283b';blue='#2367a4';green='#176b59';muted='#526577'
def text(x,y,s,size=16,color=ink,ha='center'):
    ax.text(x,y,s,fontsize=size,color=color,ha=ha,va='center')
def box(x,y,w,h,lines):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=.06,rounding_size=.13',facecolor='white',edgecolor=blue,linewidth=1.8))
    for dy,s,size in lines:text(x,y+dy,s,size)
def arrow(a,b,color=blue,rad=0):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=20,linewidth=2,color=color,connectionstyle=f'arc3,rad={rad}'))
text(4.5,13.55,'Flows, composition and support',24)
text(4.5,13.12,'Exact maps from OA-MOD-BF-02–04',14,muted)
text(.55,12.52,'1  One cocycle, two GNS spaces',18,ha='left')
box(2.2,11.35,3.0,1.28,[(.34,r'$H_\varphi$',23),(-.27,r'$\pi_\varphi(u_t)=\Delta_\varphi^{it}P^{-it}$',16)])
box(6.8,11.35,3.0,1.28,[(.34,r'$H_\psi$',23),(-.27,r'$\pi_\psi(u_t)=Q^{it}\Delta_\psi^{-it}$',16)])
arrow((5.17,11.52),(3.83,11.52));text(4.5,11.9,r'$W$',19,blue)
text(4.5,10.23,r'$W\pi_\psi(u_t)W^*=\pi_\varphi(u_t)$',21,blue)
text(4.5,9.72,'W is the constructed onto GNS intertwiner.',15,muted)
text(4.5,9.37,'All imaginary powers shown act on the whole indicated space.',13,muted)
text(.55,8.67,'2  Compare weight 3 to weight 1 through weight 2',17,ha='left')
for x,n in [(1.05,3),(4.5,2),(7.95,1)]:
    box(x,7.62,1.1,.90,[(0,rf'$\omega_{n}$',24)])
arrow((1.77,7.62),(3.77,7.62),green)
arrow((5.22,7.62),(7.22,7.62),green)
text(2.77,8.03,r'$c_{23}(t)$',17,green)
text(6.22,8.03,r'$c_{12}(t)$',17,green)
arrow((1.05,6.96),(7.95,6.96),green,rad=.27)
text(4.5,6.43,r'$c_{13}(t)$',18,green)
text(4.5,5.58,r'$c_{ij}(t)=[D\omega_i:D\omega_j]_t$',19)
text(4.5,5.10,r'$E_{12}E_{23}=E_{13}\quad\Longrightarrow\quad c_{13}(t)=c_{12}(t)c_{23}(t)$',18,green)
text(4.5,4.63,'The order is fixed; the factors need not commute.',14,muted)
text(.55,3.95,'3  A supported GNS embedding',18,ha='left')
text(4.5,3.47,r'$e=s(\psi),\qquad\widehat\psi=\psi+\chi((1-e)\,\cdot\,(1-e))$',18)
text(4.5,3.08,'χ is faithful normal semifinite on the complementary corner.',13,muted)
box(1.0,2.15,1.25,.96,[(0,r'$H_\psi$',22)])
box(4.5,2.15,2.25,.96,[(0,r'$Q_eH_{\widehat\psi}$',22)])
box(7.9,2.15,1.65,.96,[(0,r'$f_eH_\varphi$',22)])
arrow((1.80,2.15),(3.20,2.15));text(2.5,2.57,r'$T$',18,blue)
arrow((5.79,2.15),(6.94,2.15));text(6.37,2.57,r'$W|_{Q_eH_{\widehat\psi}}$',14,blue)
text(4.5,1.22,r'$Q_e=J_{\widehat\psi}\pi_{\widehat\psi}(e)J_{\widehat\psi}$',19)
text(4.5,.77,r'$f_e=J_\varphi\pi_\varphi(e)J_\varphi,\qquad U=WT$',19)
text(4.5,.30,'Both arrows are onto their displayed ranges; U is isometric.',13,muted)
target=Path(__file__).with_name('balanced-flow-composition-support.png')
fig.savefig(target,dpi=100,facecolor=fig.get_facecolor(),metadata={'Title':'Relative modular flows, ordered composition and supported GNS range','Author':'OpenAI Codex (AI)','Description':'Original exact diagram for BF.12-14, BF.19 and BF.24-27. No source artwork.'})
plt.close(fig)
print(target)
