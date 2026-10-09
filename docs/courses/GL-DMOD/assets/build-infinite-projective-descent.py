"""Exact slices and phase intervals for IG.1–IG.4; proofs retain every spatial index."""
from pathlib import Path
from fractions import Fraction
import argparse,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Arc

parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent)
out=parser.parse_args().output;out.mkdir(parents=True,exist_ok=True)
matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':10.5,'svg.hashsalt':'projective-descent-v1'})
data={'normal_cone_margin_mu':'2/3','spatial_standard_B':'2','standard_half_angle_in_pi_units':'1/3',
    'phase_grid_step_in_pi_units':'1/4','one_normal_complement_aperture_in_pi_units':'4/3',
    'neighbor_union_support_aperture_in_pi_units':'11/12','neighbor_common_complement_aperture_in_pi_units':'13/12',
    'normalized_covariable_radius':'1/16','phase_half_neighborhood_in_pi_units':'1/24',
    'polar_lower_bound':'cos(3*pi/8)-1/8 > 0',
    'outer_source_normal_radius':'3','outer_source_spatial_radius':'3','endpoint_time_span':'1',
    'real_slice_initial_spatial_radius':'sqrt(5)*sigma/2','real_slice_enlarged_spatial_radius':'2*sigma',
    'zero_test':'K0-LG=J; one normal circuit gives 2*pi*i*G=0; negative Laurent uniqueness gives K0=0'}
(out/'infinite-projective-descent-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
fig,axes=plt.subplots(1,3,figsize=(16.8,5.8));fig.patch.set_facecolor('#f7fafc')
s=np.linspace(0,1,201)
ax=axes[0]
ax.fill_between(s,-2*s,2*s,color='#e2edf7',label='standard thick support, B=2')
ax.fill_between(s,-np.sqrt(5)*s/2,np.sqrt(5)*s/2,color='#9dbddc',label='initial strict-polar normal cone')
ax.plot(s,2*s,color='#315b94');ax.plot(s,-2*s,color='#315b94')
ax.set_title('Cofinal actual supports',fontweight='bold')
ax.set_xlabel(r'$\sigma=-\mathrm{Re}\,w$');ax.set_ylabel(r'real slice $\mathrm{Re}\,\zeta$')
ax.set_xlim(0,1.07);ax.set_ylim(-2.3,2.3);ax.legend(loc='upper left',fontsize=8.5)
ax.text(.58,.07,r'$\mu=2/3$',fontsize=12)
ax.text(.54,-1.85,r'$|\mathrm{Re}\,\zeta|\leq2\sigma$',fontsize=11,ha='center')
ax=axes[1];ax.set_title('A connected angular overlap',fontweight='bold')
ax.add_patch(Circle((0,0),1,facecolor='#e4f0e9',edgecolor='#93b9a4'))
ax.add_patch(Wedge((0,0),1,120,240,facecolor='#c7d7ed',edgecolor='#315b94',alpha=.9))
ax.add_patch(Wedge((0,0),1,75,195,facecolor='#f3d9b7',edgecolor='#b87324',alpha=.55))
ax.add_patch(Arc((0,0),2.28,2.28,theta1=240,theta2=435,color='#138477',linewidth=3))
ax.text(-.52,-.32,r'$T_0$',color='#315b94',fontsize=12)
ax.text(.06,.59,r'$T_1$',color='#a96c24',fontsize=12)
ax.text(.93,-.98,r'$\Omega_0\cap\Omega_1$',color='#138477',ha='center',fontsize=11)
ax.text(0,-1.45,r'support union $11\pi/12$; complement $13\pi/12$',ha='center',fontsize=10)
ax.text(0,1.46,r'$\lambda=\pi/3,\quad h=\pi/4$',ha='center',fontsize=12)
ax.set_aspect('equal');ax.set_xlim(-1.6,1.6);ax.set_ylim(-1.75,1.7);ax.axis('off')
ax=axes[2];ax.set_title('Actual zero witnesses give descent',fontweight='bold');ax.axis('off')
boxes=[('IG.10: literal missing-face boundary',.86),
       (r'$\Pi_-$ kills spatial faces; $H_i$ extends to $w=0$',.63),
       (r'$F(L+2\pi i)-F(L)=\sum_i H_i$',.40),
       (r'zero class: $G=0$, then $K_0=0$',.17)]
for label,y in boxes:
    ax.text(.5,y,label,ha='center',va='center',transform=ax.transAxes,fontsize=10.5,
        bbox={'boxstyle':'round,pad=.6','facecolor':'#edf2f7','edgecolor':'#a7b8c9'})
for y in [.75,.52,.29]:
    ax.annotate('',xy=(.5,y-.055),xytext=(.5,y+.055),xycoords='axes fraction',
        arrowprops={'arrowstyle':'->','color':'#4b6681','lw':1.5})
fig.suptitle('Source-defined support germs, connected phase overlaps, and geometric zero detection',fontsize=15,fontweight='bold',y=.98)
fig.text(.5,.035,'IG.1–IG.5. Exact real slices and angular apertures; full proofs use closed complex spatial cones, whole holomorphic domains and every coefficient index.',ha='center',fontsize=9.5)
fig.subplots_adjust(left=.065,right=.985,top=.85,bottom=.15,wspace=.27)
fig.savefig(out/'infinite-projective-descent.png',dpi=150,facecolor=fig.get_facecolor(),metadata={'Software':'Matplotlib'})
fig.savefig(out/'infinite-projective-descent.svg',facecolor=fig.get_facecolor(),metadata={'Date':None,'Creator':'Matplotlib'})
plt.close(fig)
print(json.dumps({'outputs':['infinite-projective-descent.png','infinite-projective-descent.svg','infinite-projective-descent-data.json']}))
