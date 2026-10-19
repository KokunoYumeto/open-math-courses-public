"""Reproduce the original moment maps, radial supports and outer coefficient."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'path'})
fig=plt.figure(figsize=(14,12.4),dpi=100,facecolor='#f6f8fb')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1400);ax.set_ylim(1240,0);ax.axis('off')
ink='#183047';blue='#17639b';green='#166e60';orange='#98491d'
def txt(x,y,s,size=14,color=ink,**kw):ax.text(x,y,s,va='top',fontsize=size,color=color,**kw)
def box(x,y,w,h,fill='#e5eef7'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=10',
        facecolor=fill,edgecolor='#c5d2dd'))
txt(35,24,'Global coefficients: exact moments and exact stress supports',23)
txt(35,66,'One protected axis interval • five fixed bumps • one completed coefficient before the next order',15)
box(40,113,1320,360)
txt(60,131,'1. FIVE ORIGINAL MOMENTS — Y0–Y4',16,blue,weight='bold')
rows=[
    (177,r'$m_{n,1}=\int_0^\infty R U_n\,dR$', 'Closes the streamfunction and radial velocity'),
    (228,r'$m_{n,2}=\int_0^\infty R^2 E_n\,dR$', 'Cancels the angular time and viscosity moments'),
    (279,r'$m_{n,3}=\int_0^\infty \partial_R\Pi_n\,dR$', 'Removes the exterior pressure constant'),
    (330,r'$m_{n,4}=\int_0^\infty R^2\sum_{i+j=n}U_iE_j\,dR$', 'Cancels the angular momentum flux'),
    (398,r'$m_{n,5}=\int_0^\infty(R\sum_{i+j=n}U_iU_j-\frac{1}{2}R^2\partial_R\Pi_n)\,dR$', 'Cancels the axial flux, including pressure')]
for y,f,desc in rows:txt(65,y,f,19);txt(855,y+8,desc,13)
box(40,500,1320,146,'#e4f1ec')
txt(60,518,'2. THE ACTUAL FINITE CORRECTION — Y1–Y2, Y8.1–Y8.10',16,green,weight='bold')
txt(65,562,r'$\alpha_n=-B_U^{-1}d_{U,n},\qquad\beta_n=-B_E^{-1}d_{E,n},'
    r'\qquad\det B_U<0,\quad\det B_E>0$',24)
txt(65,615,'Two axial bumps and three angular bumps. All row factors retained; no small-discrepancy condition.',13)
box(40,674,1320,245)
txt(60,692,'3. COEFFICIENTS AND STRESSES HAVE DIFFERENT SUPPORTS — Y3–Y5',16,blue,weight='bold')
xs=[115,270,1080,1290];y=754
ax.plot([xs[0],xs[-1]],[y,y],color=ink,lw=2)
for x,label in zip(xs,[r'$0$',r'$X_-$',r'$X_+$',r'$X_b$']):
    ax.plot([x,x],[y-9,y+9],color=ink);txt(x,y-36,label,18,ha='center')
ax.plot([xs[0],xs[2]],[790,790],color=green,lw=7)
txt(130,763,r'$\mathbf{P}_n\quad(n\geq1)$',16,green)
ax.plot([xs[1],xs[2]],[835,835],color=blue,lw=7)
txt(315,808,r'$\mathcal{T}_n\quad(n\geq2)$',16,blue)
ax.plot([xs[1],xs[3]],[880,880],color=orange,lw=7)
txt(315,853,r'$\mathcal{T}_{1,\theta}$',16,orange)
txt(1100,809,r'$\mathcal{T}_{1,z}=0$',16,orange)
box(40,946,1320,210,'#fff0e5')
txt(60,964,'4. THE FIRST OUTER COEFFICIENT — Y8.16–Y8.27',16,orange,weight='bold')
txt(65,1009,r'$\mathcal{T}_{1,\theta}=e^{-4/\delta_b^2}\delta_b^{-3}B_1,\qquad'
    r'B_1(0,\eta)=\dfrac{16e\rho_oR_b\mathcal{E}_b(\eta)\eta^2}{L^2}$',24)
txt(65,1090,r'$\dfrac{\mathcal{T}_{1,\theta}}{\mathcal{T}_{0,\theta}}\longrightarrow'
    r'\dfrac{2X_b\eta^2}{L^2},\qquad R_b=\sqrt{2X_b},\quad'
    r'\mathcal{E}_b=c_\infty X_b^{-A}\mathcal{H}(2(1-\eta^2)/X_b)$',22)
txt(40,1180,'Support bars show containment and radial order, not scale. The first-order midpoint refinement is proved in Y8.21.',11)
txt(40,1210,'Source: OpenAI, pp.49–54, Lemma5.2; full proofs: N3.2 Y0–Y8. Original viscosity is retained in Y6.3. CC0 figure source.',11)
fig.savefig(HERE/'global-coefficient-extension.svg',metadata={'Creator':'GPT-6 Astra (OpenAI)','Title':'Global coefficient moments and outer stress'})
fig.savefig(HERE/'global-coefficient-extension.png',dpi=100);plt.close(fig)
p=HERE/'global-coefficient-extension.svg';t=p.read_text(encoding='utf8')
assert 'width="1008pt" height="892.8pt"' in t
p.write_text(t.replace('width="1008pt" height="892.8pt"','width="1400" height="1240"'),encoding='utf8')
