"""Exact h(z,y)=z^2 nearby family, CC0; deterministic two-layout figure."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rcParams.update({'font.size':11,'font.family':'DejaVu Sans','svg.hashsalt':'SH02-HN10-20261009'})
ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path(__file__).parent);a=ap.parse_args();a.output.mkdir(parents=True,exist_ok=True)
blue='#2866A4';red='#BF4C45';green='#167D5E'
theta=np.linspace(0,2*np.pi,241)
def make(mode):
 fig=plt.figure(figsize=(15,6)) if mode=='wide' else plt.figure(figsize=(7,17.5))
 ax=fig.add_subplot(131 if mode=='wide' else 311,projection='3d')
 for y in [-.5,0,.5]:
  ax.plot(np.cos(theta),np.sin(theta),np.full_like(theta,y),color=blue,alpha=.55,lw=1.5)
  ax.scatter([.25,-.25],[0,0],[y,y],c=[red,green],s=45,depthshade=False)
 ax.plot([0,0],[0,0],[-.75,.75],color='#50565E',lw=2,label=r'$Y=\{z=0\}$')
 ax.set_xlabel(r'$\operatorname{Re}z$',labelpad=5);ax.set_ylabel(r'$\operatorname{Im}z$',labelpad=5);ax.set_zlabel(r'$\operatorname{Re}y$ ($\operatorname{Im}y=0$)',labelpad=8)
 ax.set_xlim(-1,1);ax.set_ylim(-1,1);ax.set_zlim(-.8,.8);ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.set_zticks([-.5,0,.5])
 ax.view_init(elev=23,azim=-54)
 ax.set_title('Normal fibres along a critical line\n'+r'$h(z,y)=z^2,\quad w=1/16$',pad=18)
 ax.text2D(.07,-.21,'Unit normal-disc boundaries; three real y samples.\nThe fibre points are z=±1/4.',transform=ax.transAxes,fontsize=10)
 bx=fig.add_subplot(132 if mode=='wide' else 312)
 ph=np.linspace(0,np.pi,180)
 bx.plot(.25*np.cos(ph),.25*np.sin(ph),color=red,lw=3,label='root starting at +1/4')
 bx.plot(-.25*np.cos(ph),-.25*np.sin(ph),color=green,lw=3,label='root starting at −1/4')
 for sign,col in [(1,red),(-1,green)]:
  q=.25*sign*np.exp(1j*np.pi*.54);p=.25*sign*np.exp(1j*np.pi*.42)
  bx.annotate('',xy=(q.real,q.imag),xytext=(p.real,p.imag),arrowprops={'arrowstyle':'->','lw':2.5,'color':col})
 bx.scatter([.25,-.25],[0,0],c=[red,green],s=60,zorder=4)
 bx.text(.25,-.075,'+1/4',ha='center');bx.text(-.25,.045,'−1/4',ha='center')
 bx.set_aspect('equal');bx.set_xlim(-.39,.39);bx.set_ylim(-.39,.39);bx.axhline(0,color='#B7BEC4',lw=.8);bx.axvline(0,color='#B7BEC4',lw=.8)
 bx.set_xlabel(r'$\operatorname{Re}z$');bx.set_ylabel(r'$\operatorname{Im}z$');bx.grid(alpha=.16)
 bx.set_title('The actual deck action\n'+r'$w(\theta)=e^{i\theta}/16,\quad0\leq\theta\leq2\pi$',pad=18)
 bx.legend(loc='upper center',bbox_to_anchor=(.5,-.16),frameon=False,fontsize=10)
 cx=fig.add_subplot(133 if mode=='wide' else 313);cx.axis('off')
 cx.text(.5,.96,'Finite complex and specialization',ha='center',va='top',fontsize=13)
 cx.text(.5,.8,'The actual diagonal specialization',ha='center',fontsize=11)
 cx.text(.5,.7,r'$P\ \longrightarrow\ P\oplus P$',ha='center',fontsize=20)
 cx.text(.5,.58,r'$\psi_h(P_M)|_Y=P\oplus P$',ha='center',fontsize=15)
 cx.text(.5,.42,r'$\Phi_h(P_M)|_Y=\operatorname{Cone}(\mathrm{diag})\simeq P$',ha='center',fontsize=14)
 cx.text(.5,.23,'Deck action on nearby cycles: swap the summands.\nDeck action on the unshifted cone: −1.',ha='center',fontsize=11)
 cx.text(.5,.05,'P is any perfect coefficient complex.\nAll equations retain the original unshifted cone.',ha='center',fontsize=10)
 fig.suptitle('A nonisolated critical locus with a finite nearby model',fontsize=16,y=.97)
 if mode=='wide':fig.subplots_adjust(left=.04,right=.99,bottom=.25,top=.75,wspace=.31)
 else:fig.subplots_adjust(left=.12,right=.93,bottom=.05,top=.87,hspace=.49)
 stem='nearby-parameter-'+mode
 fig.savefig(a.output/(stem+'.svg'),metadata={'Date':None,'Creator':'SH02 exact HN10 figure'})
 fig.savefig(a.output/(stem+'.png'),dpi=160,metadata={'Software':'SH02 exact HN10 figure'})
 fig.savefig(a.output/(stem+'.pdf'),metadata={'CreationDate':None,'ModDate':None,'Creator':'SH02 exact HN10 figure'})
 plt.close(fig)
for mode in ['wide','stacked']:make(mode)
j={'proof_locator':'HN10; theorem conventions HN0a; finite model HN6c','example_only':True,'space':'C_z x C_y','function':'h(z,y)=z^2','critical_locus':'Y={z=0}, complex dimension 1','normal_radius':1,'value':{'w':'1/16','delta':'1/8'},'fibre_points':['+1/4','-1/4'],'source_display':'real slice Im(y)=0, with normal complex z; three y samples -1/2,0,1/2','displayed_disc_boundaries':'|z|=1','value_loop':'w(theta)=exp(i theta)/16, theta in [0,2 pi]','root_paths':['z_plus(theta)=exp(i theta/2)/4','z_minus(theta)=-exp(i theta/2)/4'],'coefficient_object':'any perfect complex P over the retained commutative unital ring','nearby_model':'P direct-sum P','specialization':'P -> P direct-sum P, x -> (x,x)','cone':'unshifted Cone(diagonal) is P','deck_nearby':'swap summands','deck_cone':'-1; in characteristic two this equals +1','omitted_directions':'imaginary y direction is not displayed; equations concern full C_y','license':'CC0-1.0'}
(a.output/'nearby-parameter-math.json').write_text(json.dumps(j,indent=2)+'\n',encoding='utf-8')
