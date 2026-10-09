from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

root = Path(__file__).resolve().parent
out = root/'assets'
out.mkdir(exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 14, 'svg.hashsalt': 'DLG-exact-cube-route-v1'})
fig, ax = plt.subplots(figsize=(13.2, 11.2), dpi=160)
fig.patch.set_facecolor('#f8fafc')
ax.set_xlim(0, 13.2)
ax.set_ylim(0, 11.2)
ax.axis('off')

def box(x, y, w, h, title, formula, color='#e6effa', size=18):
    ax.add_patch(FancyBboxPatch((x,y), w,h, boxstyle='round,pad=0.10,rounding_size=0.12', facecolor=color, edgecolor='#42566e', linewidth=1.1))
    ax.text(x+0.20,y+h-0.32,title,fontsize=13,color='#405169',va='top')
    ax.text(x+w/2,y+h*0.42,formula,fontsize=size,ha='center',va='center',color='#172d45')

def arrow(x, y, xx, yy):
    ax.add_patch(FancyArrowPatch((x,y),(xx,yy),arrowstyle='-|>',mutation_scale=18,linewidth=1.5,color='#42566e'))

ax.text(6.6,10.88,'The full relative-cube route for an arbitrary kernel',ha='center',fontsize=21,weight='bold',color='#172d45')
ax.text(6.6,10.45,'Full relative representatives, in every input degree',ha='center',fontsize=14,color='#405169')
box(0.45,9.05,5.8,1.02,'Kernel support A; total degree p',r'$k=(a,b)$',size=23)
box(6.95,9.05,5.8,1.02,'Input support B; total degree q',r'$e=(c,f)$',size=23)
arrow(3.35,8.92,3.35,8.48)
arrow(9.85,8.92,9.85,8.48)
ax.text(6.6,8.57,'Four entries of the cup cube F(k,e)  ·  DLG.3',ha='center',fontsize=15,color='#172d45')
box(0.45,7.02,5.8,1.20,'Whole domain M',r'$x=a\wedge c$',color='#e3f1ec',size=22)
box(6.95,7.02,5.8,1.20,r'$U_A=M\setminus A$',r'$x_A=b\wedge c$',color='#f3eaf9',size=22)
box(0.45,5.43,5.8,1.20,r'$U_B=M\setminus B$',r'$x_B=(-1)^p a\wedge f$',color='#f3eaf9',size=22)
box(6.95,5.43,5.8,1.20,r'$U_A\cap U_B$',r'$z=(-1)^{p-1}b\wedge f$',color='#faeee1',size=22)
arrow(6.6,5.32,6.6,4.96)
box(0.45,3.64,12.3,1.27,'Full intersection cone; U = U_A union U_B  ·  DLG.5',r'$\Phi_\rho(x,x_A,x_B,z)=(x,\ \rho_A x_A+\rho_B x_B+\delta\rho_A\wedge z)$',size=20)
ax.text(6.6,3.33,r'$\rho_A+\rho_B=1$ on $U$;  $\Phi_\rho\iota=1$;  $1-\iota\Phi_\rho=d_KH_\rho+H_\rho d_K$',ha='center',fontsize=15,color='#405169')
arrow(6.6,3.11,6.6,2.77)
box(0.45,1.53,12.3,1.15,'Proper collar applied after cube reduction  ·  DLG.15',r'$L_\eta(x,\beta)=(\eta x+\delta\eta\wedge\beta,\ \eta\beta)$',color='#e3f1ec',size=22)
arrow(6.6,1.40,6.6,1.08)
ax.text(6.6,0.83,r'$\mathcal{A}_k=Q_N L_\eta\Phi_\rho F(k,-),\qquad d\mathcal{A}_k=\mathcal{A}_kd$',ha='center',fontsize=21,color='#172d45')
ax.text(6.6,0.37,r'Normalized all-degree trace, for $p=N$ and $dk=0$  ·  DLG.16',ha='center',fontsize=14,color='#405169')
fig.subplots_adjust(left=0.01,right=0.99,bottom=0.01,top=0.99)
fig.savefig(out/'whole-kernel-cube-route.png',metadata={'Software':'Exact DLG figure source'})
fig.savefig(out/'whole-kernel-cube-route.svg',metadata={'Date':None,'Creator':'Exact DLG figure source'})
plt.close(fig)
data = {'kind': 'exact cochain diagram', 'kernel': {'cochain': ['a','b'], 'total_degree': 'p', 'support': 'A'}, 'input': {'cochain': ['c','f'], 'total_degree': 'q', 'support': 'B'}, 'cup_cube': {'M':'a wedge c', 'U_A':'b wedge c', 'U_B':'(-1)^p a wedge f', 'U_A_intersect_U_B':'(-1)^(p-1) b wedge f'}, 'full_cone_second_component':'rho_A x_A + rho_B x_B + delta rho_A wedge z', 'collar':'(eta x + delta eta wedge beta, eta beta)', 'final_operator':'Q_N L_eta Phi_rho F(k,-)', 'hypotheses': ['p=N', 'dk=0', 'A intersect B proper over output', 'p(A intersect B) contained in output support'], 'proof_locators':['DLG.3','DLG.5','DLG.6','DLG.15','DLG.16'], 'figure_axes': 'layout coordinates only; no numerical geometric projection is asserted'}
(out/'whole-kernel-figure-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(out/'whole-kernel-cube-route.png')
