"""Reproduce the collapsing support family, radial comparison and finite pole model."""
from pathlib import Path
from fractions import Fraction as Q
import argparse,json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,default=Path(__file__).parent);args=parser.parse_args()
args.output_dir.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'mathtext.fontset':'dejavusans','svg.hashsalt':'GL-DMOD-HI-20261019'})
R=Q(2);L=Q(1);delta=Q(3,4)
data={'R':str(R),'L':str(L),'base_disc_radius':str(delta),
 'support':'a>=0 and b^2+|zeta|^2<=L^2*a^2',
 'radius_squared':'max(L^2*max(a,0)^2-b^2,0)',
 'polar_sign':'Re(f*p)>0 because n_f=-f','phase_in_plot':'p=1',
 'base_samples':[],'radial_profiles':[],'finite_poles':[],
 'finite_plot_data_is_not_the_general_comparison_proof':True}
for ai in range(-6,7):
 for bi in range(-6,7):
  a,b=Q(ai,8),Q(bi,8)
  if a*a+b*b>=delta*delta:continue
  rho2=max(L*L*max(a,0)**2-b*b,0)
  data['base_samples'].append({'a':str(a),'b':str(b),'rho_squared':str(rho2),'in_H':a>=0 and abs(b)<=L*a})
for rho in [Q(0),Q(1,4),Q(1,2)]:
 samples=[]
 for n in range(1,32):
  r=Q(n,16);q=rho+(1-rho/R)*r
  assert rho<q<R and R*(q-rho)/(R-rho)==r
  samples.append({'r':str(r),'q':str(q)})
 data['radial_profiles'].append({'rho':str(rho),'points':samples})
for j in range(4):data['finite_poles'].append({'derivative_order':j,'pole_order':j+1,'coefficient':(-1)**j*math.factorial(j)})

fig=plt.figure(figsize=(16,12),dpi=150,facecolor='#f5f7fc')
fig.suptitle('A holomorphic incidence class from the complete shrinking support family',fontsize=22,y=.97,fontweight='bold')
ax=fig.add_axes([.07,.49,.36,.38],aspect='equal')
aa=np.linspace(-.76,.76,401);bb=np.linspace(-.76,.76,401);a,b=np.meshgrid(aa,bb)
rho=np.sqrt(np.maximum(np.maximum(a,0)**2-b*b,0))
rho=np.ma.array(rho,mask=a*a+b*b>=float(delta)**2)
im=ax.pcolormesh(a,b,rho,shading='auto',cmap='viridis',vmin=0,vmax=float(delta),rasterized=True)
ax.add_patch(Circle((0,0),float(delta),fill=False,edgecolor='#62738b',ls='--',lw=1.5))
t=np.linspace(0,float(delta)/np.sqrt(2),100)
ax.plot(t,t,'w--',lw=1.5);ax.plot(t,-t,'w--',lw=1.5)
ax.scatter([Q(5,8)],[Q(3,8)],s=40,color='white',edgecolor='#243c60',zorder=5)
ax.annotate(r'$\rho(5/8+3i/8)=1/2$',xy=(.625,.375),xytext=(-.45,.39),fontsize=12,
 arrowprops={'arrowstyle':'->','color':'white'},color='white',clip_on=False)
ax.text(.22,-.08,r'$H$',fontsize=24,color='white')
ax.set(xlim=(-.78,.78),ylim=(-.78,.78),xlabel=r'$a=\Re f$',ylabel=r'$b=\Im f$')
ax.set_title('A. Tangent-ball radius, including the collapsed boundary',fontsize=14,pad=14)
cbar=fig.colorbar(im,ax=ax,fraction=.048,pad=.03);cbar.set_label(r'$\rho(f)$')
ax.spines[['top','right']].set_visible(False)

ax=fig.add_axes([.57,.49,.35,.38],facecolor='white')
ax.axhspan(1,2,color='#e4eaf2',alpha=.8,zorder=0)
rr=np.linspace(.001,1.999,400)
for rho,color in [(0,'#277c8e'),(.25,'#a54d79'),(.5,'#b97423')]:
 ax.plot(rr,rho+(1-rho/2)*rr,color=color,lw=2.5,label=fr'$\rho={rho:g}$')
 ax.scatter([0,2],[rho,2],s=45,facecolor='white',edgecolor=color,zorder=5)
ax.plot([0,2],[0,2],ls=':',lw=1,color='#62738b')
ax.text(.1,1.8,r'all supports have $\rho<R/2$',fontsize=12,color='#354d6d')
ax.set(xlim=(-.05,2.05),ylim=(-.05,2.05),xlabel=r'original normal radius $r$',ylabel=r'new normal radius $\psi_\rho(r)$')
ax.set_title('B. The same radial map compares both complements',fontsize=14,pad=14)
ax.legend(loc='lower right',frameon=True)
ax.spines[['top','right']].set_visible(False)
fig.text(.57,.415,r'$\psi_\rho(r)=\rho+(1-\rho/R)r,\quad 0<r<R.$',fontsize=18)

lower=fig.add_axes([.06,.09,.88,.29]);lower.axis('off')
lower.text(0,1,'C. Actual support comparison and the finite differential-operator class',fontsize=15,fontweight='bold',va='top')
lower.text(.015,.79,r'$[2m-2-(2m-2)]=[0]$',fontsize=20,color='#24557d')
lower.text(.44,.79,r'$n_f=-f,\qquad \Re(fp)>0$',fontsize=20,color='#24557d')
lower.text(.015,.60,r'$\mu\mathrm{hom}(\mathbb{C}_S[-1],F)_p\simeq\mathfrak{h}_{f,p}(F)[1]$',fontsize=22)
lower.text(.015,.38,r'$\mathcal{D}/(\mathcal{D}f+\sum_i\mathcal{D}D_{z_i})\ \hookrightarrow\ H^0\mu\mathrm{hom}(\mathbb{C}_S[-1],F)$',fontsize=21)
lower.text(.015,.15,r'$D_f^{\,j}[\eta/f]=(-1)^j j!\,[\eta/f^{j+1}]$',fontsize=20)
lower.text(.61,.15,r'$\mathrm{gr}=\mathcal{O}_S[\tau_f],\quad I=(f,\xi_z)$',fontsize=19)
fig.text(.06,.045,'HI.6–HI.18 proves the entire support comparison; HI.23–HI.32 constructs the class and finite pole module. Full E generation and inverse products are separate.',fontsize=11.5,color='#526174')
name='holomorphic-incidence-shrinking-support'
fig.savefig(args.output_dir/(name+'.png'),dpi=150,metadata={'Software':'Open mathematics course figures'})
fig.savefig(args.output_dir/(name+'.svg'),metadata={'Date':None,'Creator':'Open mathematics course figures'})
(args.output_dir/(name+'-exact-data.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
plt.close(fig)
print(json.dumps({'outputs':3,'png_size':[2400,1800],'exact_base_samples':len(data['base_samples']),'exact_radial_samples':sum(len(x['points'])for x in data['radial_profiles'])}))
