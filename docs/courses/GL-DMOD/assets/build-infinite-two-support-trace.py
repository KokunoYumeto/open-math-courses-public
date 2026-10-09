"""Exact TC.4–TC.13 annulus margins and full two-support cube roof."""
from pathlib import Path
from fractions import Fraction
import argparse,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge

parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent)
out=parser.parse_args().output;out.mkdir(parents=True,exist_ok=True)
matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':10.5,'svg.hashsalt':'two-support-trace-v1'})
c=Fraction(1,8);k1=Fraction(1,8);k2=Fraction(1,4)
data={'c':'1/8','kappa_1':'1/8','kappa_2':'1/4','transition_inner_radius':str(k1*c),
    'transition_outer_radius':str(k2*c),'distance_to_b_pole_at_least':str((1-k2)*c),
    'residue_circle_radius':'1/16','source_radius':'1','collar_one_radius':'1/3','collar_support_radius':'1/2',
    'at_c_zero_a_nonzero':'rho_A=1 locally; delta rho_A=0',
    'excluded_intersection':'a=c=0','source_cube':'(0,0,0,f)',
    'source_relative_pair':'(0,delta rho_A*f)','target_relative_pair':'(0,-integral f da)',
    'whole_domain_rho_A_f_asserted':False}
(out/'infinite-two-support-trace-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
fig,axs=plt.subplots(1,3,figsize=(16.2,5.7));fig.patch.set_facecolor('#f7fafc')
ax=axs[0];r1=float(k1*c);r2=float(k2*c)
ax.add_patch(Wedge((0,0),r2,0,360,width=r2-r1,facecolor='#9ac8b5',edgecolor='#138477',alpha=.8))
ax.add_patch(Circle((0,0),float(Fraction(1,16)),fill=False,color='#315b94',linestyle='--',linewidth=1.8))
ax.scatter([0,float(c)],[0,0],s=40,color=['#315b94','#a24676'],zorder=4)
ax.text(-.008,-.018,r'$a=0$',ha='right');ax.text(float(c)+.006,.008,r'$b=0:\ a=c$',ha='left')
ax.annotate(r'$1/64\leq|a|\leq1/32$',xy=(0,r2),xytext=(-.085,.096),
    arrowprops={'arrowstyle':'->','color':'#138477'},fontsize=10)
ax.text(.025,-.091,r'$|b|\geq3/32$',fontsize=11)
ax.set_title('Transition avoids both poles',fontweight='bold');ax.set_aspect('equal')
ax.set_xlim(-.11,.21);ax.set_ylim(-.13,.13);ax.set_xticks([]);ax.set_yticks([])
ax.axhline(0,color='#d0d8df',lw=.7);ax.axvline(0,color='#d0d8df',lw=.7)
for sp in ax.spines.values():sp.set_visible(False)
ax=axs[1];cx=np.linspace(0,.125,100)
ax.fill_between(cx,k1.numerator/k1.denominator*cx,k2.numerator/k2.denominator*cx,color='#d2e9df')
ax.fill_between(cx,-k2.numerator/k2.denominator*cx,-k1.numerator/k1.denominator*cx,color='#d2e9df')
ax.plot(cx,.25*cx,color='#138477');ax.plot(cx,-.25*cx,color='#138477')
ax.scatter([0],[0],marker='x',color='#ad5b29',s=65,zorder=5)
ax.set_xlim(-.007,.138);ax.set_ylim(-.042,.042)
ax.set_xlabel(r'real slice $c$');ax.set_ylabel(r'real slice $a$')
ax.set_title('Smooth on the actual union complement',fontweight='bold')
ax.text(.0625,.036,r'$\rho_A=1$ at $c=0,a\ne0$',ha='center',fontsize=10)
ax.text(.076,-.038,'The marked intersection is excluded.',ha='center',fontsize=9)
ax=axs[2];ax.axis('off');ax.set_title('Keep the complete relative roof',fontweight='bold')
items=[(r'cube $(0,0,0,f)$ on $U_A\cap U_B$',.83),
       (r'$\Phi:\ (0,\delta\rho_A f)$ on $U_A\cup U_B$',.60),
       (r'$L_\eta:\ (0,\delta\rho_A f)$; first entry is zero',.37),
       (r'trace $(0,-\oint f\,da)$ on $c\ne0$',.14)]
for label,y in items:
    ax.text(.5,y,label,ha='center',va='center',transform=ax.transAxes,fontsize=10,
        bbox={'boxstyle':'round,pad=.7','facecolor':'#e8eef6','edgecolor':'#9aacbf'})
for y in [.71,.48,.25]:
    ax.annotate('',xy=(.5,y-.055),xytext=(.5,y+.055),xycoords='axes fraction',
        arrowprops={'arrowstyle':'->','color':'#315b94','lw':1.5})
fig.suptitle('Corrected ordinary canonical trace: exact two-pole margins and retained complement cochain',fontsize=14,fontweight='bold',y=.98)
fig.text(.5,.025,'TC.1–TC.3. Actual complex annulus at c=1/8; real parameter slice only in the center. No whole-domain rho_A f cochain or pole extension is used.',ha='center',fontsize=9.4)
fig.subplots_adjust(left=.06,right=.985,top=.86,bottom=.16,wspace=.28)
fig.savefig(out/'infinite-two-support-trace.png',dpi=150,facecolor=fig.get_facecolor(),metadata={'Software':'Matplotlib'})
fig.savefig(out/'infinite-two-support-trace.svg',facecolor=fig.get_facecolor(),metadata={'Date':None,'Creator':'Matplotlib'})
plt.close(fig)
print(json.dumps({'outputs':['infinite-two-support-trace.png','infinite-two-support-trace.svg','infinite-two-support-trace-data.json']}))
