"""Original exact parameter geometry. Run only into this task's owned directory."""
from pathlib import Path
import argparse,json,sys
sys.dont_write_bytecode=True
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Circle,Rectangle
OWN=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'AN02-form-right-cap046',
 'axes.spines.top':False,'axes.spines.right':False})
BLUE='#176B9A';ORANGE='#B64B13';GREEN='#26734A';GRAY='#4A5563'
def arrow(ax,a,b,color,**kw):
 ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':color,'lw':2.5,**kw})
def save(fig,out,name):
 fig.savefig(out/(name+'.png'),dpi=140,metadata={'Software':'Original mathematical figure; CC0 1.0'})
 fig.savefig(out/(name+'.svg'),metadata={'Date':None,'Creator':'Original mathematical figure; CC0 1.0'})
 plt.close(fig)
def render(out):
 out=out.resolve()
 if not out.is_relative_to(OWN):raise RuntimeError('Output outside sole ownership')
 out.mkdir(parents=True,exist_ok=True)
 fig,axs=plt.subplots(1,2,figsize=(13,6),gridspec_kw={'width_ratios':[1,1.15]})
 ax=axs[0];ax.set_aspect('equal')
 ax.add_patch(Polygon([(0,0),(0,1),(1,1)],facecolor='#DCEEDC',edgecolor='none'))
 ax.add_patch(Rectangle((0,0),1,1,fill=False,ec='#A7AFB8',lw=1))
 arrow(ax,(0,0),(1,1),BLUE);arrow(ax,(0,0),(0,1),ORANGE);arrow(ax,(0,1),(1,1),ORANGE)
 for p,t,offset in [((0,0),'(0,0)',(-.08,-.13)),((0,1),'(0,1)',(-.1,.035)),((1,1),'(1,1)',(-.04,.035))]:
  ax.plot(*p,'o',color=GRAY,ms=4);ax.text(p[0]+offset[0],p[1]+offset[1],t,fontsize=11)
 ax.text(.59,.39,r'$L$',color=BLUE,fontsize=16)
 ax.text(-.13,.53,r'$W$',color=ORANGE,fontsize=16)
 ax.text(.45,1.07,r'$W$',color=ORANGE,fontsize=16)
 ax.text(.21,.78,'area = 1/2',color=GREEN,fontsize=13)
 ax.set_xlim(-.2,1.15);ax.set_ylim(-.2,1.2)
 ax.set_xlabel('u: first simplex factor');ax.set_ylabel('v: second simplex factor')
 ax.set_title('Finite carrier in the parameter square',pad=24,fontsize=14)
 ax=axs[1];ax.set_aspect('equal')
 ax.add_patch(Polygon([(0,0),(1,0),(1,1)],fc='#DFECF6',ec=BLUE,lw=1.4))
 arrow(ax,(0,0),(1,0),BLUE);arrow(ax,(1,0),(1,1),ORANGE)
 ax.text(-.08,-.12,'A=(0,0)',fontsize=11);ax.text(.78,-.12,'B=(1,0)',fontsize=11);ax.text(.82,1.04,'C=(1,1)',fontsize=11)
 ax.text(.62,.18,r'$\int_\sigma dx\wedge dy=1/2$',fontsize=11,ha='center')
 ax.text(.5,-.3,'front AB: dx integral = 1',ha='center',color=BLUE)
 ax.text(.5,-.46,'back BC: dy integral = 1',ha='center',color=ORANGE)
 ax.text(.5,-.68,'wedge - cup = 1/2 - 1 = -1/2',ha='center',fontsize=12,color=GRAY)
 ax.set_xlim(-.25,1.27);ax.set_ylim(-.78,1.2);ax.axis('off')
 ax.set_title('Actual triangle: the correction matters',pad=24,fontsize=14)
 fig.suptitle('FC12–FC16: diagonal, front/back product and a supported correction',fontsize=15,y=.98)
 fig.subplots_adjust(left=.07,right=.98,bottom=.08,top=.85,wspace=.35)
 save(fig,out,'diagonal-and-front-back')
 fig,axs=plt.subplots(1,2,figsize=(13,6),gridspec_kw={'width_ratios':[1,1.18]})
 ax=axs[0];ax.set_aspect('equal')
 boxes=[(-1.7,-1.25,2.05,2.3),(-.3,-.8,2.0,2.1)]
 for x,y,w,h in boxes:ax.add_patch(Rectangle((x,y),w,h,fill=False,ec=BLUE,lw=1.7))
 for x,y,r in [(-.78,-.1,.5),(.72,.3,.43)]:ax.add_patch(Circle((x,y),r,fc='#DCEEDC',ec=GREEN,lw=1.2))
 ax.plot([-1.7,.35],[-1.25,1.05],color='#A7AFB8',lw=1)
 ax.plot([-.3,1.7],[-.8,1.3],color='#A7AFB8',lw=1)
 ax.text(-1.45,1.14,r'$Q_1$',color=BLUE,fontsize=15);ax.text(1.2,1.4,r'$Q_2$',color=BLUE,fontsize=15)
 ax.text(-.95,-.13,r'$K_1$',color=GREEN,fontsize=14);ax.text(.54,.27,r'$K_2$',color=GREEN,fontsize=14)
 arrow(ax,(-1.48,-1.03),(-1.1,-1.03),GRAY);arrow(ax,(-1.48,-1.03),(-1.48,-.65),GRAY)
 ax.text(-1.03,-1.12,'x',fontsize=10);ax.text(-1.63,-.57,'y',fontsize=10)
 ax.text(0,-1.65,'positive boxes; boundaries outside each local support',ha='center',fontsize=10)
 ax.set_xlim(-2,2);ax.set_ylim(-1.9,1.85);ax.axis('off')
 ax.set_title('FC18–FC20: normalize a finite support',fontsize=14,pad=15)
 ax=axs[1];ax.axis('off')
 ax.text(.5,.9,'Unshifted right cap on an N-simplex',ha='center',fontsize=14,color=GRAY,transform=ax.transAxes)
 for x,t in zip([.08,.24,.49,.74,.92],['0','…','q','…','N']):
  ax.text(x,.7,t,ha='center',fontsize=17,transform=ax.transAxes)
 ax.plot([.08,.49],[.61,.61],lw=4,color=BLUE,transform=ax.transAxes)
 ax.plot([.49,.92],[.61,.61],lw=4,color=ORANGE,transform=ax.transAxes)
 ax.text(.28,.53,'front: degree q = N-p',ha='center',color=BLUE,fontsize=11,transform=ax.transAxes)
 ax.text(.72,.44,'back: degree p',ha='center',color=ORANGE,fontsize=11,transform=ax.transAxes)
 ax.text(.5,.3,r'$(I\eta)(R_{I\alpha}\sigma)=(I\eta\smile I\alpha)(\sigma)$',ha='center',fontsize=13,transform=ax.transAxes)
 ax.text(.5,.18,r'$\eta$ first, $\alpha$ second; boundary correction = 0',ha='center',fontsize=12,transform=ax.transAxes)
 ax.text(.5,.06,r'$\int_{D_{\rm right} I_c[\alpha]}\eta=\int_M\eta\wedge\alpha$',ha='center',fontsize=15,transform=ax.transAxes)
 fig.suptitle('Finite local fundamental chains fix the sign and normalization',fontsize=15,y=.98)
 fig.subplots_adjust(left=.03,right=.98,bottom=.07,top=.85,wspace=.15)
 save(fig,out,'compact-support-and-right-cap')
 data={'schema':'AN02-form-right-cap046-original-geometry/v1','parameter_square':[0,1],
 'L_vertices':[[0,0],[1,1]],'W_vertices':[[0,0],[0,1],[1,1]],
 'actual_H1':[{'coefficient':1,'vertices':[[0,0],[0,0],[1,1]]},
 {'coefficient':-1,'vertices':[[0,0],[0,0],[0,1]]},{'coefficient':-1,'vertices':[[0,0],[0,1],[1,1]]}],
 'actual_H1_signed_area':'1/2','triangle':[[0,0],[1,0],[1,1]],
 'triangle_wedge':'1/2','triangle_ordered_cup':'1','triangle_correction':'-1/2',
 'support_panel':'coordinate support schematic; no specific form density or curvature claimed',
 'right_cap_order':['eta on front q-face','alpha on back p-face'],'q':'N-p','manifold_coefficients':'real',
 'box_coordinates':boxes,'captions':'learner.md, Figure1 and Figure2'}
 (out/'geometry.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',default=str(OWN/'figures'));a=p.parse_args();render(Path(a.output))
