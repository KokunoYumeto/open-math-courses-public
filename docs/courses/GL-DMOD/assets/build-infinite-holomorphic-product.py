"""Exact compact-complement samples and the finite normalization mechanism of IM.1–IM.5."""
from pathlib import Path
from fractions import Fraction
from math import factorial
import argparse,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent)
out=parser.parse_args().output;out.mkdir(parents=True,exist_ok=True)
matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':10.5,'svg.hashsalt':'full-holomorphic-product-v1'})
rows=[]
for k in range(2,13):
    rows.append({'k':k,'w':str(Fraction(1,k)),'full_scaled_kernel_exact':'k*exp(k)',
        'finite_scaled_kernels':{str(J):str(k*sum((Fraction(k**j,factorial(j)) for j in range(J+1)),Fraction(0))) for J in [1,3,8]}})
data={'kernel_example':'P=sum_j partial_t^j/(j!)^2; 2*pi*abs(K(1/k))=k*exp(k)',
    'samples':rows,'normalization_example_normal_dimension':2,'output_cube_cardinalities':[0,1,2],
    'output_ambient_complex_dimension':4,'retained_vertical_degrees':[0,1,2,3,4],
    'finite_inverse':'A=1-d_h*h_v+(d_h*h_v)^2','homotopy':'H=h_v*A',
    'boundary_identity':'D H + H D = 1 - i P','input_limit_topology':'Holomorphic compact convergence, then one fixed weighted graph model',
    'supported_distribution_limit_asserted':False,
    'product_difference':"D_i=F_(G_i,T_prime_i)C_i(P,Q)-kappa_prime_i(P circ Q); d B_i=D_i on T_prime_i",
 'final_boundary':"d F_(T_prime_i,G_prime_i)B_i=F_(G_i,G_prime_i)C_i-F_(T_prime_i,G_prime_i)kappa_prime_i; IM.23 on G_prime_i"}
(out/'infinite-holomorphic-product-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
fig,axs=plt.subplots(1,3,figsize=(16.8,6.1));fig.patch.set_facecolor('#f7fafc')
k=np.arange(2,13)
ax=axs[0];ax.plot(k,(k+np.log(k))/np.log(10),color='#315b94',linewidth=2.6,label='full holomorphic kernel')
for J,col in [(1,'#aa7b38'),(3,'#138477'),(8,'#a24676')]:
    values=[np.log10(float(Fraction(row['finite_scaled_kernels'][str(J)]))) for row in rows]
    ax.plot(k,values,'o-',color=col,markersize=3,linewidth=1.1,label=f'positive cutoff J={J}')
ax.set_xlabel(r'exact sample $w=1/k$');ax.set_ylabel(r'$\log_{10}(2\pi|K(w)|)$')
ax.set_title('Convergence on punctured compacts',fontweight='bold')
ax.legend(loc='upper left',fontsize=8.5)
ax.text(.5,-.19,'IM.12 retains every spatial/negative index.\nNo distribution convergence is asserted.',transform=ax.transAxes,ha='center',fontsize=9.5)
ax=axs[1];ax.set_title('A finite contraction, with all degrees',fontweight='bold');ax.axis('off')
for x,r,label in [(.13,0,'whole domain'),(.50,1,'two faces'),(.87,2,'top intersection')]:
    ax.text(x,.76,fr'$r={r}$',transform=ax.transAxes,ha='center',fontsize=13,
        bbox={'boxstyle':'round,pad=.7','facecolor':'#e7eef6','edgecolor':'#9aafc6'})
    ax.text(x,.62,label,transform=ax.transAxes,ha='center',fontsize=9.2)
for x in [.32,.69]:
    ax.annotate('',xy=(x+.065,.76),xytext=(x-.065,.76),xycoords='axes fraction',
        arrowprops={'arrowstyle':'->','color':'#315b94','lw':1.5})
ax.text(.5,.51,r'$d_hh_v$ increases $r$; $(d_hh_v)^3=0$',transform=ax.transAxes,ha='center',fontsize=11)
ax.text(.5,.38,r'$A=1-d_hh_v+(d_hh_v)^2$',transform=ax.transAxes,ha='center',fontsize=12)
ax.text(.5,.27,r'$\mathsf{H}=h_vA,\quad D\mathsf{H}+\mathsf{H} D=1-i\mathsf{P}$',transform=ax.transAxes,ha='center',fontsize=11)
ax.text(.5,.12,'N=2 example: every q=0,...,4 is retained.\nOne common domain and one fixed weight system.',transform=ax.transAxes,ha='center',fontsize=9.5)
ax=axs[2];ax.set_title('A literal full product primitive',fontweight='bold');ax.axis('off')
items=[(r'$D^{[J]}\longrightarrow D$ on actual domains',.91),
       (r'$\nu(D^{[J]})=0\ \Longrightarrow\ \nu(D)=0$',.73),
       (r'$B=\mathsf{H}D+$ actual face primitives',.54),
       (r'$dB_{P,Q,i}=\mathsf{F}_{\mathcal{G}_i,T_i^{\prime}}\mathcal{C}_i(P,Q)$'+'\n'+
        r'$-\kappa_i^{\prime}(P\circ Q)\quad\mathrm{on}\ T_i^{\prime}$',.32),
       (r'$d\mathsf{F}_{T_i^{\prime},\mathcal{G}_i^{\prime}}B_{P,Q,i}$'+'\n'+
        r'$=\mathsf{F}_{\mathcal{G}_i,\mathcal{G}_i^{\prime}}\mathcal{C}_i(P,Q)$'+'\n'+
        r'$-\mathsf{F}_{T_i^{\prime},\mathcal{G}_i^{\prime}}\kappa_i^{\prime}(P\circ Q)$',.075)]
for label,y in items:
    ax.text(.5,y,label,transform=ax.transAxes,ha='center',va='center',fontsize=10.1,
        bbox={'boxstyle':'round,pad=.55','facecolor':'#e9f2ec','edgecolor':'#94b89f'})
ax.text(.99,.43,'IM.16',ha='right',transform=ax.transAxes,fontsize=9,color='#355c4b')
ax.text(.99,.18,'IM.23 on final G′',ha='right',transform=ax.transAxes,fontsize=9,color='#355c4b')
for y in [.82,.635,.435,.19]:
    ax.annotate('',xy=(.5,y-.025),xytext=(.5,y+.025),xycoords='axes fraction',
        arrowprops={'arrowstyle':'->','color':'#138477','lw':1.6})
fig.suptitle('Full mixed holomorphic cochains: controlled tails, bounded normalization, actual boundary',fontsize=15,fontweight='bold',y=.98)
fig.text(.5,.025,'Proof: IM.1–IM.6. The essential-head graph is an exact scalar sample, the middle is a finite-cube example, and the right retains full total/complement cochains.',ha='center',fontsize=9.5)
fig.subplots_adjust(left=.065,right=.975,top=.86,bottom=.19,wspace=.30)
fig.savefig(out/'infinite-holomorphic-product.png',dpi=150,facecolor=fig.get_facecolor(),metadata={'Software':'Matplotlib'})
fig.savefig(out/'infinite-holomorphic-product.svg',facecolor=fig.get_facecolor(),metadata={'Date':None,'Creator':'Matplotlib'})
plt.close(fig)
print(json.dumps({'outputs':['infinite-holomorphic-product.png','infinite-holomorphic-product.svg','infinite-holomorphic-product-data.json']}))
