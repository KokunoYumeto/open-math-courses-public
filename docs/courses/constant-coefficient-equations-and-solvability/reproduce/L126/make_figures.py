"""Reproduce the original compact-support and normal-circle diagrams (CC0-1.0)."""
from pathlib import Path
import argparse, json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
import numpy as np

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'figures')
OUT=parser.parse_args().output
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.hashsalt':'AN02-CO046-v1','axes.spines.top':False,'axes.spines.right':False})
BLUE='#1b5ea6'; GREEN='#187747'; ORANGE='#ad5620'; GRAY='#425366'
def save(fig,name):
    fig.savefig(OUT/(name+'.png'),dpi=160,facecolor='white',metadata={'Software':'Open Mathematics Courses'})
    fig.savefig(OUT/(name+'.svg'),facecolor='white',metadata={'Date':None,'Creator':'Open Mathematics Courses'})
    plt.close(fig)

fig,axs=plt.subplots(1,2,figsize=(14,7.6))
for ax in axs:
    ax.set(xlim=(-3.2,3.2),ylim=(-2.7,2.8));ax.axis('off')
    ax.add_patch(Rectangle((-2.75,-1.55),5.5,3.1,fc=BLUE+'0C',ec=BLUE,lw=1.2,ls='--'))
    ax.axhline(0,color=GRAY,lw=2)
    ax.text(-3.05,.11,r'$Y$',fontsize=18,color=GRAY)
    ax.text(-2.55,1.7,'A compact tube cutoff',color=BLUE,fontsize=12)
axs[0].set_title('Before the correction: a closed kernel form',fontsize=16,pad=18)
axs[0].add_patch(Ellipse((0,.0),3.45,1.45,angle=12,fc=ORANGE+'30',ec=ORANGE,lw=2))
angle=np.deg2rad(12)
intersection_half=(np.cos(angle)**2/(3.45/2)**2+np.sin(angle)**2/(1.45/2)**2)**(-.5)
axs[0].plot([-intersection_half,intersection_half],[0,0],color=ORANGE,lw=7,solid_capstyle='butt')
axs[0].text(-1.25,-1.08,r'$A=Y\cap\operatorname{supp}\alpha$',color=ORANGE,fontsize=15)
axs[0].text(-2.65,2.2,r'$i^*\alpha=0,\quad d\alpha=0$',fontsize=17)
axs[0].text(-2.65,-2.0,'Zero restriction does not yet\nmean support away from Y.',fontsize=13,color=GRAY)
axs[1].set_title('After the correction: compact support in V',fontsize=16,pad=18)
axs[1].add_patch(Ellipse((-.5,.92),2.55,.67,angle=8,fc=GREEN+'25',ec=GREEN,lw=2))
axs[1].add_patch(Ellipse((.65,-.94),2.4,.65,angle=-8,fc=GREEN+'25',ec=GREEN,lw=2))
axs[1].text(-2.65,2.2,r"$\alpha'=\alpha-d(\zeta K\alpha)$",fontsize=17)
axs[1].annotate('Zero on an open neighbourhood\nof every point of Y',xy=(1.4,.14),xytext=(-2.4,-2.05),fontsize=13,color=GREEN,
    arrowprops={'arrowstyle':'->','color':GREEN,'connectionstyle':'arc3,rad=-.25'})
fig.text(.035,.035,'Support schematic only: CO7–CO9 prove the result. The pictured shapes do not give the actual corrected support.',fontsize=12,color=GRAY)
fig.subplots_adjust(left=.025,right=.985,top=.88,bottom=.13,wspace=.22)
save(fig,'kernel-complex-to-open-support')

def cutoff(r):
    result=np.ones_like(r,dtype=float)
    result[r>=2]=0
    mask=(r>1)&(r<2);t=r[mask]-1
    a=np.exp(-1/t);b=np.exp(-1/(1-t))
    result[mask]=b/(a+b)
    return result

fig=plt.figure(figsize=(13.8,8.0));grid=fig.add_gridspec(2,1,height_ratios=[1.15,1.0],hspace=.32)
ax=fig.add_subplot(grid[0]);r=np.linspace(0,2.8,1601)
ax.axvspan(1,2,color=ORANGE,alpha=.10);ax.plot(r,cutoff(r),color=BLUE,lw=2.7)
ax.set(xlim=(0,2.8),ylim=(-.08,1.22),xlabel='Normal radius r',ylabel=r'$\chi(r)$')
ax.set_xticks([0,1,2]);ax.set_yticks([0,1])
ax.text(.14,.70,'One near the zero section',color=BLUE,fontsize=13)
ax.text(2.06,.25,'Zero beyond\nthe tube cutoff',color=GRAY,fontsize=13)
ax.text(1.02,1.07,'Annular derivative support',color=ORANGE,fontsize=13)
ax.set_title('An annular derivative produces the positive normal-circle comparison',fontsize=19,pad=18)
ax2=fig.add_subplot(grid[1]);ax2.axis('off');ax2.set(xlim=(0,13.8),ylim=(0,3.4))
ax2.text(.15,3.00,r'$d\theta\wedge\gamma_q\wedge dr\wedge\beta_p$',fontsize=22,color=BLUE)
ax2.text(6.45,3.00,r'$=(-1)^{q+1}dr\wedge d\theta\wedge\gamma_q\wedge\beta_p$',fontsize=21,color=GREEN)
ax2.text(.15,2.05,'Moving dr past q + 1 factors',fontsize=14,color=GRAY)
ax2.text(6.45,2.05,r'$\int_0^\infty\chi\,^{\prime}(r)\,dr=-1$',fontsize=22,color=ORANGE)
ax2.text(.15,.99,r'$N=2d,\quad q=N-2-p$',fontsize=21,color=GRAY)
ax2.text(6.45,.99,r'$(-1)^{q+1}(-1)=(-1)^q=(-1)^p$',fontsize=22,color=GREEN)
ax2.text(.15,.14,'Normal orientation: dr then dθ; tube orientation: positive circle before the base cycle. See CO18–CO25.',fontsize=12,color=GRAY)
fig.subplots_adjust(left=.065,right=.975,top=.89,bottom=.04)
save(fig,'radial-cutoff-and-normal-first-sign')

geometry={
 'schema':'AN02-CO046-original-figure-geometry/v1',
 'support_diagram':{'schematic_only':True,'zero_section':'y=0','cutoff_rectangle':[-2.75,-1.55,5.5,3.1],
    'original_ellipse':[0,0,3.45,1.45,12],'schematic_A_segment':[-float(intersection_half),float(intersection_half)],
    'A_segment_exact_rule':'half=(cos(12deg)^2/(3.45/2)^2+sin(12deg)^2/(1.45/2)^2)^(-1/2)',
    'corrected_schematic_ellipses':[[-.5,.92,2.55,.67,8],[.65,-.94,2.4,.65,-8]],
    'pointwise_corrected_support_formula_claimed':False,'uniform_radius_at_infinity_claimed':False},
 'radial_cutoff':{'samples':1601,'sample_interval':[0,2.8],
    'exact_function':'chi=1 for r<=1; chi=0 for r>=2; chi=exp(-1/(2-r))/(exp(-1/(r-1))+exp(-1/(2-r))) for1<r<2',
    'derivative_support_subset':[1,2],'exact_endpoint_integral':-1,'numerical_integral_used_as_proof':False},
 'orientations':{'normal':'dr before dtheta','tube':'positive circle before base','base_degree':'q=N-2-p',
    'crossing_sign':'(-1)^(q+1)','radial_integral':-1,'even_dimension_final_sign':'(-1)^p'},
 'normalized_form_duality_entry_unproved_here':True,'singular_right_cap_comparison_unproved_here':True,
}
(OUT/'geometry.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
