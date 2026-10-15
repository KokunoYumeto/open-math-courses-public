"""Original, deterministic mathematical diagram; expression dedicated CC0-1.0."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.hashsalt':'oa-flow-ccm-20261004','mathtext.fontset':'dejavusans'})
fig = plt.figure(figsize=(17,12),dpi=200,facecolor='#f8fafc')
fig.text(.045,.97,'The full crossed-product commutant',fontsize=29,fontweight='bold',color='#15243c')
fig.text(.045,.938,'Arbitrary locally compact group; arbitrary Hilbert space; both inclusions are proved.',fontsize=17,color='#46566a')
blue,red,green='#1464b0','#bb3d47','#1c806e'

def panel(rect,title):
 ax=fig.add_axes(rect);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
 ax.add_patch(FancyBboxPatch((.005,.005),.99,.99,boxstyle='round,pad=0.005,rounding_size=0.02',facecolor='white',edgecolor='#ccd6e2',lw=1.3))
 ax.text(.045,.935,title,fontsize=20,fontweight='bold',color='#15243c',va='center');return ax
def arrow(ax,a,b,c=blue): ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=15,lw=2.1,color=c))

a=panel([.035,.535,.455,.38],'1  The exact left and right generators')
rows=[(.78,r'$\pi(x)\xi(t)=\alpha_{t^{-1}}(x)\xi(t)$',blue),(.65,r'$\lambda_s\xi(t)=\xi(s^{-1}t)$',blue),(.47,r'$b(y)\xi(t)=y\xi(t),\quad y\in M^{\prime}$',red),(.34,r'$\rho_s\xi(t)=\Delta(s)^{1/2}U_s\xi(ts)$',red)]
for y,t,c in rows:a.text(.055,y,t,fontsize=19,color=c)
a.text(.055,.18,r'$R=\{\pi(M),\lambda(G)\}^{\prime\prime}$',fontsize=19,color=blue)
a.text(.055,.065,r'$R^{\prime}=\{b(M^{\prime}),\rho(G)\}^{\prime\prime}$',fontsize=19,color=red)
a.text(.79,.58,'commute',ha='right',fontsize=14,color=green)
arrow(a,(.84,.72),(.84,.41),green)

b=panel([.51,.535,.455,.38],'2  Exact four-coordinate example')
b.text(.045,.82,r'$G=\mathbb{Z}/2\mathbb{Z},\quad H=\mathbb{C}^2,\quad M=$ diagonal',fontsize=17,color='#46566a')
xs=[.18,.78];ys=[.60,.30]
coords={1:(xs[0],ys[0]),2:(xs[1],ys[0]),3:(xs[0],ys[1]),4:(xs[1],ys[1])}
for i,(x,y) in coords.items():
 b.scatter([x],[y],s=950,c=blue if i in [1,4] else '#80b7df',edgecolors='white',linewidths=2,zorder=4)
 b.text(x,y,str(i),color='white',fontsize=20,fontweight='bold',ha='center',va='center',zorder=5)
 label_x=x+(-.08 if i==3 else .08 if i==4 else 0)
 label_y=y+(.08 if i in [1,2] else 0)
 b.text(label_x,label_y,('a' if i in [1,4] else 'b'),color=blue,fontsize=19,ha='center',va='center' if i in [3,4] else 'baseline')
for i,j in [(1,3),(2,4)]:b.add_patch(FancyArrowPatch(coords[i],coords[j],arrowstyle='<->',mutation_scale=15,shrinkA=17,shrinkB=17,lw=2.1,color=blue))
for i,j in [(1,4),(2,3)]:b.add_patch(FancyArrowPatch(coords[i],coords[j],arrowstyle='<->',mutation_scale=15,shrinkA=17,shrinkB=17,lw=2.1,color=red))
b.text(.045,.44,r'$\lambda_1$',color=blue,fontsize=18)
b.text(.52,.37,r'$\rho_1$',color=red,fontsize=18)
b.text(.045,.14,r'$\pi(a,b)=\mathrm{diag}(a,b,b,a)$',fontsize=17,color=blue)
b.text(.045,.045,r'$b(c,d)=\mathrm{diag}(c,d,c,d);\quad \dim R=\dim R^{\prime}=4$',fontsize=16,color=red)

c=panel([.035,.065,.455,.43],'3  The standard model: modular conjugation')
c.text(.05,.80,r'$\widehat J\xi(t)=\Delta(t)^{-1/2}(U_t^0)^*J\xi(t^{-1})$',fontsize=18,color='#15243c')
c.text(.05,.66,r'$\widehat J\pi(x)\widehat J=b(JxJ)$',fontsize=21,color=blue)
c.text(.05,.53,r'$\widehat J\lambda_s\widehat J=\rho_s^0$',fontsize=21,color=red)
arrow(c,(.48,.46),(.48,.37),green)
c.text(.05,.29,r'$R_0^{\prime}=\widehat J R_0\widehat J=\{b(M_0^{\prime}),\rho^0(G)\}^{\prime\prime}$',fontsize=19,color=green)
c.text(.05,.15,'GDW supplies the full closed modular operators.',fontsize=16,color='#46566a')
c.text(.05,.07,'MW supplies the entire commutant, including the reverse inclusion.',fontsize=13,color='#46566a')

d=panel([.51,.065,.455,.43],'4  Transfer when the projection moves')
d.text(.14,.78,r'$eH_a$',fontsize=24,color=blue,ha='center')
d.text(.84,.78,r'$e_sH_a$',fontsize=24,color=red,ha='center')
arrow(d,(.27,.79),(.71,.79),blue)
d.text(.49,.82,r'$U_s^a$',fontsize=18,color=blue,ha='center')
arrow(d,(.72,.64),(.26,.64),green)
d.text(.49,.66,r'$w_s\in D$',fontsize=18,color=green,ha='center')
d.text(.05,.51,r'$w_s^*w_s=e_s,\qquad w_sw_s^*=e$',fontsize=20,color='#15243c')
d.text(.05,.39,r'$\widetilde\rho_s=b(w_s)\rho_s^aE$',fontsize=20,color=red)
d.text(.05,.26,r'$E\,b(d)\rho_s^aE=b(edw_s^*)\widetilde\rho_s$',fontsize=18,color=green)
d.text(.05,.15,r'$edw_s^*\in eDe$; bounded word limits give the whole corner.',fontsize=14,color='#46566a')
d.text(.05,.065,r'$E=b(e),\quad e_s=U_s^ae(U_s^a)^*;\quad$ no assumption $e_s=e$.',fontsize=14,color='#46566a')

fig.text(.04,.025,'CCM: full modular proof and exact reducing-projection transport accompany this diagram.  Original CC0 illustration; 3400 × 2400 pixels.',fontsize=14,color='#526176')
fig.savefig(ASSETS/'crossed-product-commutant.png',dpi=200,metadata={'Software':'OA-FLOW original reproducible diagram'})
fig.savefig(ASSETS/'crossed-product-commutant.svg',metadata={'Date':None,'Creator':'OA-FLOW original reproducible diagram'})
plt.close(fig)
data={'finite_example': {'group': 'Z/2Z', 'coordinate_order': ['t=0,e1', 't=0,e2', 't=1,e1', 't=1,e2'], 'pi_diagonal': ['a', 'b', 'b', 'a'], 'b_diagonal': ['c', 'd', 'c', 'd'], 'lambda_permutation': [3, 4, 1, 2], 'rho_permutation': [4, 3, 2, 1], 'left_complex_dimension': 4, 'right_complex_dimension': 4}, 'standard_model': {'Jhat': 'Jhat xi(t)=Delta(t)^(-1/2) (U_t^0)* J xi(t^(-1))', 'coefficient_conjugation': 'Jhat pi(x) Jhat=b(J x J)', 'group_conjugation': 'Jhat lambda_s Jhat=rho_s^0', 'whole_commutant': 'R0_prime=Jhat R0 Jhat'}, 'corner_transport': {'N': 'sigma(M) tensor 1', 'D': 'N_prime', 'e': 'reducing projection in D', 'e_s': 'U_s^a e (U_s^a)*', 'w_s': 'V U_s V* (U_s^a)*', 'w_s_in_D': True, 'initial_projection': 'e_s', 'final_projection': 'e', 'E': 'b(e)', 'right_unitary': 'tilde_rho_s=b(w_s) rho_s^a E', 'compressed_word': 'E b(d) rho_s^a E=b(e d w_s*) tilde_rho_s', 'invariant_projection_required': False, 'whole_corner_passage': 'uniformly bounded strong limits of finite coefficient/group words'}, 'native_pixels': [3400, 2400], 'license': 'CC0-1.0 to the extent of rights held'}
(ASSETS/'crossed-product-commutant-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('Rendered original PNG, SVG and exact data.')
