"""Original diagram of the exact Hilbert-space maps in OA-MOD-BT-01--03."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(9,12),dpi=100,facecolor='#fbfcfe')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,9);ax.set_ylim(0,12);ax.axis('off')
ink='#13283b';blue='#2367a4';green='#176b59';muted='#526577'
def label(x,y,text,size=16,color=ink,ha='center'):
    ax.text(x,y,text,fontsize=size,color=color,ha=ha,va='center')
def box(x,y,title,subtitle,w=2.65,h=1.08):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.06,rounding_size=0.13',facecolor='white',edgecolor=blue,linewidth=1.8))
    label(x,y+.19,title,21);label(x,y-.22,subtitle,16,muted)
def arrow(start,end,color=green,style='-|>',rad=0):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle=style,mutation_scale=19,linewidth=2,color=color,connectionstyle=f'arc3,rad={rad}'))
label(4.5,11.57,'Two weights, four GNS corners',24)
label(4.5,11.13,'Exact corner types and maps · BT.4–5, BT.13, BT.19–22',12,muted)
label(.6,10.58,'1  Modular conjugation exchanges mixed corners',17,ha='left')
label(2.35,10.03,'Column 1: weight φ',15,blue)
label(6.65,10.03,'Column 2: weight ψ',15,blue)
box(2.35,9.12,r'$H_{11}$',r'$U_{11}:H_\varphi\to H_{11}$')
box(6.65,9.12,r'$H_{12}$',r'$U_{12}:H_\psi\to H_{12}$')
box(2.35,6.94,r'$H_{21}$',r'$U_{21}:H_\varphi\to H_{21}$')
box(6.65,6.94,r'$H_{22}$',r'$U_{22}:H_\psi\to H_{22}$')
arrow((3.36,7.56),(5.39,8.77),rad=.10)
arrow((5.65,8.50),(3.61,7.29),rad=.10)
label(3.00,8.07,r'$J_A:H_\varphi\to H_\psi$',14,green)
label(6.07,7.97,r'$J_B=J_A^{-1}$',14,green)
label(4.5,6.10,'The mixed arrows are antiunitary; both are onto.',15,green)
label(4.5,5.75,'On the diagonal corners, the restrictions are Jφ and Jψ.',14,muted)
label(.6,5.12,'2  The commutant flip exchanges columns',17,ha='left')
label(4.5,4.66,r'$C=J_\Omega\,\pi_\Omega(E_{12}+E_{21})\,J_\Omega$',19)
for y,left,right in [(3.85,r'$H_{11}$',r'$H_{12}$'),(2.78,r'$H_{21}$',r'$H_{22}$')]:
    box(2.05,y,left,r'$H_\varphi$',w=2.05,h=.86)
    box(6.95,y,right,r'$H_\psi$',w=2.05,h=.86)
    arrow((5.78,y+.18),(3.22,y+.18),blue)
    arrow((3.22,y-.18),(5.78,y-.18),blue)
    label(4.5,y+.42,r'$W$',15,blue)
    label(4.5,y-.42,r'$W^*$',15,blue)
label(4.5,1.99,'The route from H₁₂ to H₁₁',15)
xs=[1.05,3.35,5.65,7.95]
for x,t in zip(xs,[r'$H_{12}$',r'$H_{21}$',r'$H_{11}$',r'$H_{11}$']):label(x,1.42,t,20)
for a,b,t in zip(xs,xs[1:],[r'$J_\Omega$',r'$L$',r'$J_\Omega$']):
    arrow((a+.48,1.42),(b-.48,1.42),ink);label((a+b)/2,1.72,t,15)
label(4.5,.75,r'$W=U_{11}^*CU_{12}=J_\varphi J_B$',20,blue)
label(4.5,.31,'Arbitrary faithful normal semifinite weights · no common GNS space assumed',12,muted)
target=Path(__file__).with_name('balanced-gns-corners.png')
fig.savefig(target,dpi=100,facecolor=fig.get_facecolor(),metadata={'Title':'Balanced GNS corners and the commutant flip','Author':'OpenAI Codex (AI)','Description':'Original diagram of OA-MOD-BT-01--03; exact corner maps, no source artwork.'})
plt.close(fig)
print(target)
