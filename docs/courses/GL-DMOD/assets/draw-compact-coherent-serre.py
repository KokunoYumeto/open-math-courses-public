"""Reproduce the compact Cauchy collar and the full nilpotent residue pairing."""
from pathlib import Path
import json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'GL-DMOD-SDC-20261021'})
r=Path(__file__).resolve().parent
fig=plt.figure(figsize=(16,9),facecolor='#f6f8fb')
fig.suptitle('Compact analytic duality: support, trace and nilpotent layers',fontsize=22,weight='bold',y=.96,color='#18334b')
ax=fig.add_axes([.065,.26,.39,.58],aspect='equal');ax.set_xlim(-1.75,1.75);ax.set_ylim(-1.75,1.75);ax.axis('off')
ax.add_patch(Circle((0,0),1.5,fill=False,ls='--',ec='#7c8d9e',lw=1.7))
ax.add_patch(Circle((0,0),1.25,fc='#f2c979',ec='#aa6910',alpha=.52))
ax.add_patch(Circle((0,0),.8,fc='#f6f8fb',ec='#aa6910',lw=1.2))
ax.add_patch(Circle((0,0),.6,fc='#a9cceb',ec='#295d9f',lw=1.5))
ax.text(0,0,r'$K$',fontsize=24,ha='center',va='center',color='#295d9f')
ax.text(0,.69,r'$\chi=1$',fontsize=11,ha='center',va='center',color='#18334b')
ax.text(0,-1.035,r'$\mathrm{supp}\,\bar\partial\chi$',fontsize=15,ha='center',va='center',color='#87520b')
ax.text(1.23,1.10,r'$P$',fontsize=20,color='#6c7c8c')
theta=np.linspace(.9*math.pi,.52*math.pi,80);ax.plot(.8*np.cos(theta),.8*np.sin(theta),color='#00848a',lw=2.6)
p0=(.8*math.cos(.55*math.pi),.8*math.sin(.55*math.pi));p1=(.8*math.cos(.52*math.pi),.8*math.sin(.52*math.pi))
ax.annotate('',xy=p1,xytext=p0,arrowprops={'arrowstyle':'-|>','color':'#00848a','lw':2,'mutation_scale':17})
ax.set_title('One integrated coordinate, SDC.B–SDC.C',fontsize=15,pad=14,color='#18334b')
fig.text(.26,.208,'K: radius 0.6; cutoff is 1 up to radius 0.8.',ha='center',fontsize=11,color='#18334b')
fig.text(.26,.174,'Derivative support: 0.8 ≤ |z| ≤ 1.25; P has radius 1.5.',ha='center',fontsize=11,color='#18334b')
fig.text(.26,.133,'The inner boundary of the annulus is clockwise.',ha='center',fontsize=12,color='#00848a')
fig.text(.26,.078,r'$-\frac{1}{2\pi i}\int \frac{ab}{z^d}\,\bar\partial\chi\wedge dz=\mathrm{Res}_0\frac{ab}{z^d}\,dz$',ha='center',fontsize=17,color='#295d9f')
ax2=fig.add_axes([.61,.31,.28,.48]);matrix=np.fliplr(np.eye(4,dtype=int));ax2.imshow(matrix,cmap=matplotlib.colors.ListedColormap(['#eef3f9','#a4cee9']),vmin=0,vmax=1)
for i in range(4):
 for j in range(4):ax2.text(j,i,str(matrix[i,j]),ha='center',va='center',fontsize=24,color='#18334b')
ax2.set_xticks(range(4),[r'$dz$',r'$z\,dz$',r'$z^2dz$',r'$z^3dz$'],fontsize=14)
ax2.set_yticks(range(4),[r'$1$',r'$z$',r'$z^2$',r'$z^3$'],fontsize=14)
ax2.set_xticks(np.arange(-.5,4,1),minor=True);ax2.set_yticks(np.arange(-.5,4,1),minor=True);ax2.grid(which='minor',color='white',lw=2);ax2.tick_params(which='minor',bottom=False,left=False)
for spine in ax2.spines.values():spine.set_visible(False)
ax2.set_title(r'$F=\mathcal{O}/(z^4)$'+'\nAll four layers pair, SDC.29–SDC.30',fontsize=15,pad=18,color='#18334b')
fig.text(.75,.215,r'$\langle z^i,z^jdz\rangle=\delta_{i+j,3}$',ha='center',fontsize=20,color='#295d9f')
fig.text(.75,.162,'Reversing the column order gives the identity matrix.',ha='center',fontsize=11,color='#18334b')
fig.text(.75,.109,'General compact coherent complexes:',ha='center',fontsize=12,color='#18334b')
fig.text(.75,.059,r'$R\Gamma_c(X,\mathbb{S}_XF)\simeq R\mathrm{Hom}_{\mathbb{C}}(R\Gamma(X,F),\mathbb{C})$',ha='center',fontsize=15,color='#00848a')
fig.savefig(r/'compact-coherent-serre.png',dpi=180,facecolor=fig.get_facecolor())
fig.savefig(r/'compact-coherent-serre.svg',metadata={'Date':None},facecolor=fig.get_facecolor());plt.close(fig)
samples=[]
for d in range(1,9):
 samples.append({'d':d,'matrix':[[int(i+j==d-1)for j in range(d)]for i in range(d)],'determinant':(-1)**(d*(d-1)//2)})
signs=[]
for n in range(1,6):
 for a in range(n+1):
  signs.append({'n':n,'hom_degree':a,'pairing_factor':(-1)**(n*a),
   'compact_differential_coefficient':(-1)**(n+a+1),'continuous_dual_differential_coefficient':(-1)**(a+1)})
data={'proof':'SDC.A--SDC.J','finite_samples_are_general_proof':False,'collar':{'input_radius':.6,'chi_one_through':.8,'chi_zero_from':1.25,'derivative_support_interval_closed':[.8,1.25],'polydisc_radius':1.5,'cutoff':'beta(R-r)/(beta(R-r)+beta(r-r0)); beta(t)=0 for t<=0 and exp(-1/t) for t>0','inner_boundary_orientation':'clockwise'},
 'residue_matrices':samples,'finite_local_shift_sign_samples':signs,'trace':'(2*pi*i)^(-n) times integral','density':'omega_X[n]','bar_dual_factor':'(-1)^p'}
(r/'compact-coherent-serre-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8');print(json.dumps({'matrices':len(samples),'sign_records':len(signs),'outputs':3}))
