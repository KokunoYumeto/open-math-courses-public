"""Exact real slices of IM.18–IM.23; the proof uses complex spatial norms."""
from pathlib import Path
from fractions import Fraction
import json, argparse, math
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.hashsalt']='gl-dmod-infinite-phase-local-support-bridge-v3'
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
OUT=Path(args.output) if args.output else Path(__file__).resolve().parent/'phase-local-figures'
OUT.mkdir(parents=True,exist_ok=True)
data={'lambda_pi':'1/6','lambda_prime_pi':'1/4','h_pi':'1/12','alpha_pi':'5/24',
 'alpha_prime_pi':'7/24','neighbor_final_aperture_pi':'7/12','B':'1','B_prime':'3/2',
 'B_prime_strictly_above_B_over_cos_alpha':True,'K_max':'3/(2*cos(7*pi/24))',
 'eta_star_pi':'1/48','covector_phase_half_width_pi':'1/16','neighbor_overlap_half_width_pi':'1/48','normalized_covariable_radius':'1/64','endpoint_coordinate_radius':'1/64',
 'collar_one_polydisc_radius':'1/4','collar_support_polydisc_radius':'1/2','outer_source_radii':'3',
 'time_intermediate_bound_strictly_below':'5/64','spatial_intermediate_bound_strictly_below':'7/64',
 'phase_count':24,'supports':'One separate phase cone and one separate neighboring cone; no cone contains the whole phase circle.',
 'support_chain':['T(lambda,B,phi)','G(lambda,B,phi)','T(lambda_prime,B_prime,phi)','G(lambda_prime,B_prime,phi)'],
 'boundary_support':'T prime, then mapped forward to convex G prime; not asserted on initial G',
 'support_forgetting_injectivity_claimed':False,'slice':'Im(e^(i*phi)w)=0 and Im(zeta)=0, N=2',
 'proof_locators':['IM.18','IM.19','IM.20','IM.21','IM.22','IM.23','IM.15 full-cone Cech coordinate calibration'],
 'free_definition':'https://perso.imj-prg.fr/pierre-schapira/wp-content/uploads/schapira-pub/Microhyp.pdf section1.2 page5',
 'licence':'CC0-1.0'}
(OUT/'infinite-phase-local-support-bridge-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
fig,axs=plt.subplots(1,3,figsize=(19,7.4),gridspec_kw={'width_ratios':[1.05,1.25,1.4]})
fig.suptitle('Phase-local composition and the exact normalization support bridge',fontsize=20,weight='bold')
ax=axs[0];ax.set_aspect('equal');ax.set(xlim=(-1.35,1.35),ylim=(-1.35,1.35));ax.axis('off')
for k in range(24):
 theta=2*math.pi*k/24
 ax.plot(math.cos(theta),math.sin(theta),'o',ms=4,color='#bcc7d2')
ax.add_patch(Wedge((0,0),.88,-45,45,facecolor='#e4f0fc',edgecolor='#467cb1',lw=1.7))
ax.add_patch(Wedge((0,0),.74,-30,30,facecolor='#b3d9bf',edgecolor='#3b7657',lw=1.7))
ax.add_patch(Wedge((0,0),1.12,-15-45,-15+45,facecolor='none',edgecolor='#bc7651',lw=1.7,ls='--'))
ax.plot([0,1.2],[0,0],color='#3b7657',lw=1.5)
ax.plot([0,1.2*math.cos(math.pi/12)],[0,-1.2*math.sin(math.pi/12)],color='#bc7651',lw=1.5)
ax.text(0,-1.29,'24 separate phases; spacing h = π/12',ha='center',fontsize=12)
ax.text(0,1.22,'Only one neighboring pair is shown',ha='center',fontsize=12)
ax.text(1.05,.08,r'$\phi_i=0$',fontsize=12,color='#3b7657')
ax.text(.58,-1.06,r'$\phi_{i+1}=h$',fontsize=12,color='#bc7651')
ax.set_title('Normal q = −w plane; cone axes rotate by −φ\n2λ′ + h = 7π/12 < π',fontsize=14,pad=15)

ax=axs[1];ax.set(xlim=(0,1),ylim=(-2.3,2.3));sig=[0,1]
slopes=[(1.5/math.cos(math.pi/4),'#d6e4f3','G′'),(1.5,'#fff0dc','T′'),
        (1/math.cos(math.pi/6),'#bed7c8','G'),(1,'#83b496','T')]
for slope,color,label in slopes:
 ax.fill_between(sig,[-slope*s for s in sig],[slope*s for s in sig],color=color,edgecolor='#4b5966',lw=.9)
label_positions={'T':(.82,.52),'G':(.82,.90),'T′':(.82,1.12),'G′':(.82,1.52)}
for slope,_,label in slopes:
 x_label,y_label=label_positions[label]
 ax.text(x_label,y_label,label,fontsize=13,weight='bold',ha='center')
ax.set_xlabel(r'$\sigma=-\Re(e^{i\phi}w)$',fontsize=13)
ax.set_ylabel(r'$\Re\zeta$; imaginary coordinates are zero in this slice',fontsize=12)
ax.set_title('Actual closed-support inclusions\nT ⊂ G ⊂ T′ ⊂ G′',fontsize=14,pad=15)
ax.grid(alpha=.15)

ax=axs[2];ax.axis('off')
rows=[('Convex output Gφ','canonical cup → proper collar → trace'),
 ('Standard support T′φ','forget support; use the exact IG.7–IG.8 cubes'),
 ('Boundary on T′φ','dB = forgotten output − forward product'),
 ('Final convex support G′φ','map B forward; equality holds here')]
for k,(title,body) in enumerate(rows):
 y=.84-k*.21
 ax.text(.5,y,title,ha='center',va='center',fontsize=15,weight='bold',bbox={'boxstyle':'round,pad=.55','facecolor':'#edf3f7','edgecolor':'#5e7e99'})
 ax.text(.5,y-.070,body,ha='center',fontsize=11)
 if k<3:ax.annotate('',xy=(.5,y-.145),xytext=(.5,y-.095),arrowprops={'arrowstyle':'->','color':'#416581','lw':1.5})
ax.text(.5,.015,'One compact collar works for the finite phase system.\nNo injectivity of support forgetting is asserted.',ha='center',fontsize=12)
fig.text(.5,.028,'Exact example: λ=π/6, λ′=π/4, B=1, B′=3/2; neighboring half-angle 7π/24.\nEndpoints |coordinate|<1/64; collar one on radius 1/4, supported in radius 1/2; outer radii 3. Proof IM.18–IM.23.\nCovector phase half-width π/16; neighboring-overlap half-width π/48.',ha='center',fontsize=10)
fig.subplots_adjust(top=.80,bottom=.18,wspace=.27)
fig.savefig(OUT/'infinite-phase-local-support-bridge.png',dpi=180,bbox_inches='tight')
fig.savefig(OUT/'infinite-phase-local-support-bridge.svg',bbox_inches='tight',metadata={'Date':None})
print('Rendered exact phase-local support chain and finite common-domain example.')
