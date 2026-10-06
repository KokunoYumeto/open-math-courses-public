"""Original MH043 exact-coordinate diagrams. No imported media.

Run: python make_figures.py [--output-dir DIRECTORY]
Writes three PNG/SVG pairs and geometry.json. All outputs stay in selected directory.
"""
from pathlib import Path
import argparse,json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle,FancyArrowPatch
import numpy as np

parser=argparse.ArgumentParser()
parser.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent/'figures')
out=parser.parse_args().output_dir.resolve();out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'MH043-exact-original-diagrams'})
BLUE='#146b98';GREEN='#17704b';PURPLE='#823596';ORANGE='#bc621c';RED='#ad3038'
def save(fig,stem):
    fig.savefig(out/(stem+'.png'),dpi=180,facecolor='white')
    fig.savefig(out/(stem+'.svg'),facecolor='white',metadata={'Date':None,'Creator':'Original MH043 mathematical diagram'})
    plt.close(fig)
def arrow(ax,a,b,color=BLUE,**kw):
    ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':2,'color':color,**kw})

fig,axes=plt.subplots(1,2,figsize=(15,7))
u=np.linspace(-2,2,701);v=np.linspace(-1,1,401);U,V=np.meshgrid(u,v);Q=-U*U+V*V
ax=axes[0]
ax.contourf(U,V,Q,levels=[-5,-1,2],colors=['#d9eadb','#f3f7fc'])
ax.contour(U,V,Q,levels=[-1],colors=GREEN,linewidths=2)
ax.add_patch(Rectangle((-2,-1),4,2,fill=False,edgecolor=BLUE,lw=2))
ax.plot([-2,-2],[-1,1],color=GREEN,lw=5);ax.plot([2,2],[-1,1],color=GREEN,lw=5)
ax.plot([-2,2],[0,0],color=PURPLE,lw=3)
arrow(ax,(-.25,0),(.4,0),PURPLE)
for x in [-2,2]:ax.plot(x,0,'o',color=PURPLE,markersize=8)
for x in [-1.45,0,1.45]:
    arrow(ax,(x,1.36),(x,1.02),ORANGE);arrow(ax,(x,-1.36),(x,-1.02),ORANGE)
arrow(ax,(1.72,-.65),(2.28,-.65),ORANGE)
arrow(ax,(-1.72,-.65),(-2.28,-.65),ORANGE)
ax.plot(math.sqrt(5)/2,.5,'o',color=BLUE)
arrow(ax,(math.sqrt(5)/2,.5),(1.96,.5),BLUE)
ax.text(.1,.68,r'$q>-1$',ha='center',color=BLUE)
ax.text(-1.67,.63,r'$C$',ha='center',color=GREEN,fontsize=17)
ax.text(1.69,.72,r'$C$',ha='center',color=GREEN,fontsize=17)
ax.text(0,-.28,'relative core: boundary in C',ha='center',color=PURPLE,fontsize=11)
ax.text(0,1.6,'v-entry transverse inward',ha='center',color=ORANGE,fontsize=11)
ax.text(0,-1.57,r'u-exits: $q\leq-3<-1$',ha='center',color=GREEN,fontsize=12)
ax.set(xlim=(-2.5,2.5),ylim=(-1.85,1.85),xlabel='negative coordinate u',ylabel='positive coordinate v')
ax.set_aspect('equal');ax.set_title(r'$B=[-2,2]\times[-1,1]$, $a=-1$, $b=2$',pad=18,fontsize=14)

ax=axes[1]
ax.add_patch(Rectangle((-2,-1),4,2,facecolor='#f3f7fc',edgecolor=BLUE,lw=1.8))
tB=.5*math.log(1.5);tA=.25*math.log(2+math.sqrt(13))
tt=np.linspace(0,tB,201);post=np.linspace(tB,tA,201)
ax.plot(.5*np.exp(2*tt),1.5*np.exp(-2*tt),color=ORANGE,lw=3)
ax.plot(.5*np.exp(2*post),1.5*np.exp(-2*post),color=ORANGE,lw=2,ls='--')
ax.plot(.5,1.5,'o',color=RED,markersize=8);ax.text(.34,1.68,r'$x_0=(1/2,3/2)$',ha='left',fontsize=11)
ax.plot(.75,1,'o',color=ORANGE,markersize=9)
ax.annotate(r'first stop $(3/4,1)$'+'\n'+r'$T_B=\frac{1}{2}\log(3/2)$',xy=(.75,1),xytext=(-2.16,1.5),arrowprops={'arrowstyle':'->','color':ORANGE},color=ORANGE,fontsize=12)
end=(.5*math.exp(2*tA),1.5*math.exp(-2*tA))
ax.plot(*end,'s',color=GREEN,markersize=7)
ax.annotate('later lower hit, not used\n'+r'$T_A=\frac{1}{4}\log(2+\sqrt{13})$',xy=end,xytext=(-1.9,-1.43),arrowprops={'arrowstyle':'->','color':GREEN},color=GREEN,fontsize=11)
vs=np.linspace(-1,1,301)
ax.plot(np.sqrt(1+vs**2),vs,color=GREEN,lw=1.6);ax.plot(-np.sqrt(1+vs**2),vs,color=GREEN,lw=1.6)
arrow(ax,(.52,1.42),(.58,1.28),ORANGE)
ax.set(xlim=(-2.4,2.4),ylim=(-1.55,1.95),xlabel='u',ylabel='v')
ax.set_aspect('equal');ax.set_title(r'$\dot u=2u$, $\dot v=-2v$; stop at $A\cup B$',pad=18,fontsize=14)
fig.suptitle('Exact rescaled local Morse block and stopped flow  |  MH9–MH15, MH19–MH20',fontsize=15,y=.98)
fig.text(.5,.025,'Local coordinate model, not a global proper exhaustion. The purple core is a relative chain, not an asserted absolute loop.',ha='center',fontsize=12)
fig.subplots_adjust(top=.83,bottom=.17,wspace=.33)
save(fig,'block-and-stopping-flow')

fig,axes=plt.subplots(1,3,figsize=(15,5.7))
ax=axes[0]
ax.plot(-.8,0,'o',color=PURPLE,markersize=16);ax.text(-.8,.33,'original point',ha='center',fontsize=12)
ax.plot(.8,0,'o',color='#555555',markersize=12);ax.text(.8,.33,'disjoint basepoint *',ha='center',fontsize=11)
ax.text(0,-.55,r'pair $(D^0,\varnothing)$',ha='center',fontsize=14)
ax.text(0,-.95,r'$H_0=k$; based quotient has two points',ha='center',fontsize=11)
ax.set(xlim=(-1.7,1.7),ylim=(-1.35,1.1));ax.set_title('Index zero: ordinary H₀',fontsize=14)
ax.axis('off')
ax=axes[1]
ax.plot([-1.4,1.4],[0,0],color=PURPLE,lw=4)
for x in [-1.4,1.4]:ax.plot(x,0,'o',color=GREEN,markersize=12)
arrow(ax,(-.3,0),(.4,0),PURPLE)
ax.text(-1.4,.3,'left ∈ C',ha='center',fontsize=11);ax.text(1.4,.3,'right ∈ C',ha='center',fontsize=11)
ax.text(0,-.53,r'$\partial[\mathrm{core}]=[\mathrm{right}]-[\mathrm{left}]$',ha='center',fontsize=12)
ax.text(0,-.95,r'$H_1(D^1,S^0)=k$',ha='center',fontsize=14)
ax.set(xlim=(-2,2),ylim=(-1.35,1.1));ax.set_title('Index one: relative interval',fontsize=14);ax.axis('off')
ax=axes[2]
ax.add_patch(Circle((0,.04),.68,facecolor='#edf0fa',edgecolor=GREEN,lw=3))
ax.text(0,.09,'oriented\nnegative disc',ha='center',va='center',color=PURPLE,fontsize=12)
theta=np.linspace(-.1,1,50);ax.plot(.45*np.cos(theta),.04+.45*np.sin(theta),color=PURPLE,lw=2)
arrow(ax,(.45*np.cos(.9),.04+.45*np.sin(.9)),(.45*np.cos(1.1),.04+.45*np.sin(1.1)),PURPLE)
ax.text(0,-.9,r'$H_2(D^2,S^1)=k$',ha='center',fontsize=14)
ax.text(0,-1.25,r'$D^2/\partial D^2\cong S^2$ (quotient, not an embedding)',ha='center',fontsize=10)
ax.set(xlim=(-1.5,1.5),ylim=(-1.4,1.1));ax.set_aspect('equal');ax.set_title('Index two: boundary in C',fontsize=14);ax.axis('off')
fig.suptitle('Actual negative-disc relative pairs  |  MH4, MH16–MH20',fontsize=15,y=.97)
fig.text(.5,.025,'A relative generator need not survive absolutely. Pair exactness determines its attaching boundary in the actual lower stage.',ha='center',fontsize=12)
fig.subplots_adjust(top=.81,bottom=.17,wspace=.39)
save(fig,'relative-pairs-and-generators')

fig,axes=plt.subplots(1,2,figsize=(15,7.4))
theta=np.linspace(-math.pi,math.pi,1001)
for ax,level,title in [(axes[0],0,'Lower closed stage f ≤ 0: disc'),(axes[1],2,'Upper closed stage f ≤ 2: cylinder strip')]:
    rhs=level+np.cos(theta);ok=rhs>=0
    bound=np.sqrt(np.maximum(rhs,0))
    ax.fill_between(theta,-bound,bound,where=ok,color='#dbeaf3')
    ax.plot(theta[ok],bound[ok],color=BLUE,lw=2);ax.plot(theta[ok],-bound[ok],color=BLUE,lw=2)
    for x in [-math.pi,math.pi]:ax.axvline(x,color='#777777',ls='--',lw=1.4)
    ax.plot(0,0,'o',color=GREEN,markersize=8);ax.text(.05,-.27,'minimum (0,0), f=−1',color=GREEN,fontsize=11)
    ax.set(xlim=(-3.65,3.65),ylim=(-2.08,2.1),xlabel=r'$\theta$ modulo $2\pi$',ylabel='t')
    ax.set_xticks([-math.pi,-math.pi/2,0,math.pi/2,math.pi],['−π','−π/2','0','π/2','π'])
    ax.set_title(title,fontsize=14,pad=13)
    ax.text(0,1.95,'dashed vertical edges are identified',ha='center',fontsize=11)
axes[1].plot([-math.pi,math.pi],[0,0],color=PURPLE,lw=2.6)
arrow(axes[1],(.7,0),(1.2,0),PURPLE)
for x in [-math.pi,math.pi]:axes[1].plot(x,0,'s',color=ORANGE,markersize=9)
axes[1].text(0,.42,'t=0: actual absolute circle generator',ha='center',color=PURPLE,fontsize=11)
axes[1].text(0,-1.87,'two edge squares denote ONE saddle, f=1',ha='center',color=ORANGE,fontsize=11)
fig.suptitle(r'Actual cylinder $S^1\times\mathbb{R}$, $f(\theta,t)=t^2-\cos\theta$  |  Example 3, MH21–MH22',fontsize=15,y=.98)
fig.text(.5,.15,'Open heights:  −2  →  0  →  2  →  3       Relative groups:  k in degree 0  |  k in degree 1  |  zero',ha='center',fontsize=12)
fig.text(.5,.075,r'Absolute homology: $H_0=k$, $H_1=k$, $H_j=0$ for $j\geq2$.  Open/closed comparison is proved by the regular collar flow.',ha='center',fontsize=12)
fig.subplots_adjust(top=.80,bottom=.28,wspace=.28)
save(fig,'cylinder-sublevels-and-open-stages')

geometry={'schema':'MH043-original-exact-diagram-geometry/v1','scope':'Exact local coordinates and actual cylinder parameter plots, not numerical proofs or global embeddings',
 'figure1':{'q':'-u^2+v^2','lambda':1,'nu':1,'block':[[-2,2],[-1,1]],'lower_level':-1,'upper_level':2,'max_q_on_block':1,'max_q_on_u_exit':-3,'lower_boundary':'|u|=sqrt(1+v^2)','field':["du/dt=2u","dv/dt=-2v"],'initial_point':[.5,1.5],'first_block_entry':[.75,1],'q_at_entry':'7/16','T_B':'log(3/2)/2','hypothetical_T_A':'log(2+sqrt(13))/4','radial_point':['sqrt(5)/2','1/2'],'radial_exit':[2,.5],'q_at_radial_exit':'-15/4','interpretation':'rescaled local Morse chart; relative core is not asserted to be an absolute loop','proof':['MH9','MH10','MH11','MH12','MH13','MH14','MH15','MH19','MH20']},
 'figure2':{'standard_pairs':[['D0','empty'],['D1','S0'],['D2','S1']],'relative_nonzero_degrees':[0,1,2],'coefficient':'arbitrary unital ring k','index_zero_based_quotient':'original point disjoint added point','interval_boundary':'right minus left','index_two_quotient':'D2/boundaryD2 = S2, not planar embedding','proof':['MH4','MH16','MH17','MH18','MH19','MH20']},
 'figure3':{'manifold':'S1 x R','function':'t^2-cos(theta)','parameter_identification':'theta=-pi and theta=pi are the same edge; markers at (±pi,0) are one point','critical_points':[{'theta':0,'t':0,'value':-1,'index':0},{'theta':'pi modulo 2pi','t':0,'value':1,'index':1}],'closed_plot_levels':[0,2],'bounds':'|t| <= sqrt(level+cos(theta)) where level+cos(theta)>=0','open_stage_heights':[-2,0,2,3],'relative_group_ledger':['k at degree0','k at degree1','zero'],'actual_absolute_homology':{'H0':'k','H1':'k','Hj_j>=2':0},'proof':['MH8','MH21','MH22','learner Example 3']},
 'source_credit':'Original diagrams from the written MH043 proof; Morse-coordinate programme method AN04 Lemma4.1, inverse/ODE DGCHAR Lemma3.1, finite chains DGCHAR Thom §§1–3; classical Morse and Hatcher-style singular excision methods.',
 'blender_assessment':'Planar exact block, trajectory, relative disc pairs and cylinder parameter plots explain these objects directly; a 3D scene would not improve the finite-chain or quotient argument.'}
(out/'geometry.json').write_text(json.dumps(geometry,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'outputs':[p.name for p in sorted(out.iterdir())]},indent=2))
