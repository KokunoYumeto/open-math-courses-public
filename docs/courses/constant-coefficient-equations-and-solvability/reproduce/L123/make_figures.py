"""Reproduce the exact local polynomial-annihilator diagrams (CC0-1.0)."""
from pathlib import Path
import argparse
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle
import numpy as np

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'figures')
OUT=parser.parse_args().output
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.hashsalt':'AN02-LP045-v1','axes.spines.top':False,'axes.spines.right':False})
BLUE='#1b5ea6'; GREEN='#187747'; ORANGE='#ad5620'; RED='#ad3434'; GRAY='#425366'

def save(fig,name):
    fig.savefig(OUT/(name+'.png'),dpi=160,facecolor='white',metadata={'Software':'Open Mathematics Courses'})
    fig.savefig(OUT/(name+'.svg'),facecolor='white',metadata={'Date':None,'Creator':'Open Mathematics Courses'})
    plt.close(fig)

fig,ax=plt.subplots(figsize=(13.6,7.2));ax.set(xlim=(0,13.6),ylim=(0,7.2));ax.axis('off')
ax.text(.35,6.85,'Polynomial moments become a convergent quotient',fontsize=21,weight='bold',color=GRAY)
boxes=[(.4,3.8,3.7,2.1,BLUE),(4.8,3.8,3.7,2.1,ORANGE),(9.2,3.8,3.95,2.1,GREEN)]
for x,y,w,h,c in boxes:ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',fc=c+'10',ec=c,lw=2))
ax.text(.65,5.45,'Every polynomial solution',weight='bold',color=BLUE)
ax.text(.65,4.95,r'$P(D)h=0\ \Longrightarrow\ \mu(h)=0$',fontsize=15)
ax.text(.65,4.4,r'$D_j=-i\partial_{x_j}$',fontsize=16)
ax.text(5.05,5.45,'Algebraic transpose',weight='bold',color=ORANGE)
ax.text(5.05,4.95,r'$\mu|_V=T^*a,\quad T=P(D)$',fontsize=15)
ax.text(5.05,4.4,r'$\widehat F=P(-z)\widehat G$',fontsize=18)
ax.text(9.45,5.45,'Analytic remainder',weight='bold',color=GREEN)
ax.text(9.45,4.95,r'$F=qH+R_F,\quad\deg_t R_F<s$',fontsize=15)
ax.text(9.45,4.4,r'$R_F=0,\quad G=H/b$',fontsize=18)
for a,b in [(4.2,4.65),(8.6,9.05)]:ax.annotate('',xy=(b,4.9),xytext=(a,4.9),arrowprops={'arrowstyle':'->','lw':2,'color':GRAY})
ax.text(.55,3.15,r'$F(z)=\sum_\alpha\frac{(-i)^{|\alpha|}\mu(x^\alpha)}{\alpha!}z^\alpha$',fontsize=18,color=BLUE)
ax.text(5.0,3.15,'Formal divisibility alone\ngives no convergence bound.',fontsize=14,color=ORANGE,va='top')
ax.text(9.35,3.15,'A finite remainder and\nparameter-order induction\nforce convergence.',fontsize=14,color=GREEN,va='top')
ax.text(.55,1.85,'Exact coefficient rule (LP2–LP5)',weight='bold',color=BLUE)
ax.text(.55,1.30,'All moment orders and every\nodd-order transpose sign remain.',fontsize=14)
ax.text(5.0,1.85,'Kernel annihilator (LP6–LP7)',weight='bold',color=ORANGE)
ax.text(5.0,1.30,'The algebraic functional a\nneed not be a distribution.',fontsize=14)
ax.text(9.35,1.85,'Actual local division (LP15–LP21)',weight='bold',color=GREEN)
ax.text(9.35,1.30,'The analytic unit b is nonzero\non the certified neighborhood.',fontsize=14)
ax.text(.55,.42,'Maps are schematic; the displayed formulas are the exact maps. The theorem proves a germ at zero.',fontsize=12,color=GRAY)
fig.subplots_adjust(left=.02,right=.99,top=.99,bottom=.02);save(fig,'moments-to-local-quotient')

fig,axes=plt.subplots(1,3,figsize=(15.4,7.1),sharex=True,sharey=True)
cases=[(-1/16,[(0,-.25),(0,.25)],r'$w=-1/16$'),(0,[(0,0)],r'$w=0$'),(1/16,[(-.25,0),(.25,0)],r'$w=1/16$')]
for ax,(w,roots,title)in zip(axes,cases):
    ax.set_aspect('equal');ax.set(xlim=(-1.22,.69),ylim=(-.69,.69),xlabel=r'$\mathrm{Re}\,t$',title=title)
    ax.axhline(0,color='#c5ced5',lw=1);ax.axvline(0,color='#c5ced5',lw=1)
    ax.add_patch(Circle((0,0),.5,fill=False,ec=BLUE,lw=2.2));ax.add_patch(Circle((0,0),.25,fill=False,ec=GREEN,lw=1.4,ls=':'))
    ax.scatter([-1],[0],marker='s',s=70,color=RED,zorder=4)
    ax.annotate('unit-factor zero\nat t = −1',(-1,0),xytext=(-1.15,-.42),fontsize=11,color=RED,arrowprops={'arrowstyle':'->','color':RED})
    ax.scatter([r[0]for r in roots],[r[1]for r in roots],s=85,color=GREEN,zorder=5)
    if w==0:ax.annotate('zero with\nmultiplicity 2',(0,0),xytext=(.02,.54),fontsize=11,color=GREEN,arrowprops={'arrowstyle':'->','color':GREEN})
    elif w>0:
        ax.annotate('−1/4',(-.25,0),xytext=(-.44,.17),fontsize=12,color=GREEN)
        ax.annotate('1/4',(.25,0),xytext=(.26,.17),fontsize=12,color=GREEN)
    else:
        ax.annotate('i/4',(0,.25),xytext=(.08,.30),fontsize=12,color=GREEN)
        ax.annotate('−i/4',(0,-.25),xytext=(.08,-.33),fontsize=12,color=GREEN)
    ax.text(.05,-.60,'R = 1/2',color=BLUE,fontsize=12)
axes[0].set_ylabel(r'$\mathrm{Im}\,t$')
fig.suptitle(r'$Q(t,w)=(1+t)(t^2-w)$: one circle retains both inner roots',fontsize=21,y=.98)
fig.text(.06,.19,r'$q=t^2-w,\quad b=1+t,\quad |w|\leq1/16,\quad |q|\geq3/16\ \mathrm{on}\ |t|=1/2$',fontsize=17,color=GRAY)
fig.text(.06,.12,r'$p_0=2,\quad p_1=0,\quad p_2=2w\quad\Longrightarrow\quad q=t^2-w$',fontsize=17,color=GREEN)
fig.text(.06,.055,'The three parameter values are exact samples. The uniform circle argument includes every complex parameter in the stated disk (LP10–LP14, LP26–LP27).',fontsize=12,color=GRAY)
fig.subplots_adjust(left=.055,right=.985,bottom=.27,top=.84,wspace=.16);save(fig,'root-circle-and-analytic-unit')

fig,ax=plt.subplots(figsize=(12.3,7.0))
t=np.linspace(-.90,.9,1600);ax.plot(t,1/(1+t),color=BLUE,lw=2.6,label=r'Real slice $G(t)=1/(1+t)$')
ax.axvline(-1,color=RED,ls='--',lw=1.8);ax.text(-.97,5.8,'pole at t = −1',color=RED,fontsize=14)
ax.axvspan(-.25,.25,color=GREEN,alpha=.11)
ax.hlines(4/3,-.25,.25,color=GREEN,lw=2.4,label=r'Sharp disk bound $4/3$ for $|t|\leq1/4$')
ax.hlines(8/3,-.25,.25,color=ORANGE,lw=2.4,ls='--',label=r'General contour bound $8/3$ on that same disk')
ax.scatter([-.25],[4/3],s=65,color=GREEN,zorder=5)
ax.annotate('sharp bound attained\nat t = −1/4',(-.25,4/3),xytext=(.39,2.0),color=GREEN,fontsize=12,arrowprops={'arrowstyle':'->','color':GREEN})
ax.set(xlim=(-1.12,1.03),ylim=(0,6.8),xlabel='Real t (one slice of the holomorphic germ)',ylabel='G(t) on t > −1')
fig.suptitle('Polynomial annihilation can give a local quotient with a global pole',fontsize=19,y=.975)
fig.text(.09,.90,r'$F=t^2-w,\quad Q=(1+t)(t^2-w),\quad F/Q=1/(1+t)$',fontsize=17,color=GRAY)
ax.legend(loc='upper right',bbox_to_anchor=(1,.74),frameon=False,fontsize=12)
fig.text(.09,.045,'Example 3 and Exercise 5: the displayed curve is a real sample. The disk bounds use complex |t|≤1/4; neither bound is claimed outside it.',fontsize=11,color=GRAY)
fig.subplots_adjust(left=.09,right=.98,top=.84,bottom=.15);save(fig,'local-quotient-global-pole')

geometry={'schema':'AN02-LP045-exact-original-diagrams/v1','source':'local-polynomial-annihilator-proof.md',
    'figures':{'moments-to-local-quotient':{'kind':'exact-map schematic','proof_locators':['LP2–LP7','LP15–LP21'],'transpose_divisor':'P(-z)','D':'-i partial','algebraic_domain_V':'complex polynomials in n real variables','restricted_functional':'mu restricted to V = T* a','no_formal_functional_growth_assumed':True},
    'root-circle-and-analytic-unit':{'kind':'three exact samples of complex t-plane','Q':'(1+t)(t^2-w)','q':'t^2-w','b':'1+t','parameter_disk_radius':1/16,'circle_R':.5,'inner_radius_r':.25,'sample_parameters':[-1/16,0,1/16],'roots':[[[0,-.25],[0,.25]],[[0,0]],[[ -.25,0],[.25,0]]],'root_multiplicities':[[1,1],[2],[1,1]],'additional_root':[-1,0],'q_boundary_lower_bound':3/16,'Q_boundary_lower_bound':3/32,'proof_locators':['LP10–LP14','LP26–LP27']},
    'local-quotient-global-pole':{'kind':'real slice with certified complex disk bounds','F':'t^2-w','Q':'(1+t)(t^2-w)','G':'1/(1+t)','sample_t_interval':[-.9,.9],'sample_points':1600,'pole':-1,'certified_disk_radius':.25,'R':.5,'M':1,'beta':.75,'contour_bound':8/3,'sharp_bound':4/3,'proof_locators':['LP23','LP27','Exercise5']}},
    'authorship':'GPT-6.1 Sol (OpenAI), Ultra, October2026','original_drawing_license':'CC0-1.0','font':'DejaVu Sans; existing reader font notices apply','diagram_sources_retained':True}
(OUT/'geometry.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':3,'PNG_files':3,'SVG_files':3,'geometry':str(OUT/'geometry.json')}))
