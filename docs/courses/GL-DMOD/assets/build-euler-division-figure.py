"""Exact full-coefficient Euler-matrix division and its nilpotent remainder.

Proof locators: Section 5.52, AM.5–AM.15. This figure does not
assert a normal form for every holonomic module. All displayed coordinates
and constants are specified in the accompanying exact data.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,Polygon
import numpy as np

parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path);args=parser.parse_args()
out=args.output_dir.resolve() if args.output_dir else Path(__file__).resolve().parent
out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'mathtext.fontset':'dejavusans','svg.hashsalt':'actual-euler-model-AM-20261018'})
navy='#173d56';blue='#1f6b91';red='#a54835';bg='#f9fbfd'
def box(ax,y,height,title,lines,face='#eef4fb'):
 ax.add_patch(FancyBboxPatch((.015,y),.97,height,boxstyle='round,pad=.012',facecolor=face,edgecolor='#7290a5',linewidth=1.2))
 ax.text(.055,y+height-.055,title,fontsize=17,weight='bold',color=navy,va='top')
 for dy,text,size in lines:ax.text(.055,y+height-dy,text,fontsize=size,color=navy,va='top')
def save(fig,name):
 fig.savefig(out/(name+'.png'),dpi=150,facecolor=bg)
 fig.savefig(out/(name+'.svg'),metadata={'Date':None},facecolor=bg)
 plt.close(fig)

fig=plt.figure(figsize=(16,9),facecolor=bg)
fig.text(.035,.95,'Actual Euler-model division: one domain, two complete tails',fontsize=24,weight='bold',color=navy)
fig.text(.035,.902,r'$L=tI-(A+I)h$,   $f=QL+\sum_i H_iD_{x_i}+R$,   $R=\sum_j r_j(x)\tau^j$',fontsize=19,color=navy)
left=fig.add_axes([.035,.14,.47,.70]);left.set_xlim(0,1);left.set_ylim(0,1);left.axis('off')
box(left,.53,.44,'Exact quotient coefficients · AM.10',[
 (.14,r'$q_j=\sum_{k\geq0}(-1)^k D^{k+1}f_{j+k}$',20),
 (.25,r'$\qquad\quad\cdot\prod_{s=1}^k((j+s)I-A-I)$',20),
 (.39,r'$Dg=(g-g(0,x))/t,\quad \|D\|\leq 2/r$',17)])
box(left,.015,.44,'Nilpotent entries survive · exact size-two case',[
 (.14,'A = J = [[0, 1], [0, 0]],     J² = 0',18),
 (.26,r'$(t\tau,0)=(\tau,0)L+(0,1)$',23),
 (.36,'The remainder is the second generator.',16)],face='#fff3e8')
right=fig.add_axes([.53,.14,.435,.70]);right.set_xlim(0,1);right.set_ylim(0,1);right.axis('off')
box(right,.53,.44,'Nonnegative output · every requested epsilon',[
 (.14,r'$j\geq0:\quad \|q_j\|\leq M_\eta\eta^j/j!$',20),
 (.25,r'$b\epsilon<1/2,\quad \epsilon\leq\eta/2$',18),
 (.35,'One fixed coefficient domain for every eta.',15)])
box(right,.015,.44,'Negative output · one factorial constant',[
 (.14,r'$j=-n:\quad k<n\quad\vert\quad k=n+m$',19),
 (.25,r'$\|q_{-n}\|\leq M C^n n!\qquad(n\geq1)$',20),
 (.35,'Both pieces use the same radius and matrix.',15)],face='#edf7f1')
fig.text(.035,.075,'Complete estimates: AM.8–AM.15. Spatial division is AM.5; no spatial index is discarded.',fontsize=14,color=navy)
fig.text(.035,.037,'This is a theorem for the stated Euler matrices. Generic classification of arbitrary holonomic modules is a separate requirement.',fontsize=13,color=navy)
save(fig,'euler-model-full-coefficient-division')

data={'proof_locators':['Section5.52 AM.5–AM.15'],'matrix_A':[[0,1],[0,0]],'L':'t I-(A+I) h','row_identity':'(t tau,0)=(tau,0)L+(0,1)','positive_bounds':'every eta>0, on one fixed coefficient domain','negative_bounds':'one factorial constant for the full negative tail','arbitrary_holonomic_real_comparison_asserted':False,'free_human_context':'https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/HolIII.pdf'}
(out/'euler-division-exact-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
