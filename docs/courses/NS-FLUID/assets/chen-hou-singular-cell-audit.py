"""Reproduce exact cell and primitive-domain diagrams for NC11–NC22."""
from pathlib import Path
from fractions import Fraction as F
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

root=Path(__file__).resolve().parent
a=F(1,6400);b=F(1,20000)
plt.rcParams.update({'font.size':12,'font.family':'DejaVu Sans','axes.spines.top':False,'axes.spines.right':False})
fig=plt.figure(figsize=(13,7.2),layout='constrained')
grid=fig.add_gridspec(2,2,width_ratios=[1.2,1])
ax=fig.add_subplot(grid[:,0])
xa=float(F(1,2)+a);xu=float(F(1,2)+2*a)
ax.add_patch(Rectangle((xa,0),float(a),float(b),facecolor='#cde4f6',edgecolor='#17649b',lw=2))
ax.add_patch(Rectangle((xa,float(b/2)),float(a),float(b/2),facecolor='#72bda0',alpha=.8))
ax.axvline(.5,color='#b54339',linestyle='--',lw=1.6)
ax.set_xlim(.5-float(a)/3,.5+3*float(a));ax.set_ylim(-float(b)/10,1.3*float(b))
ax.set_xticks([.5,xa,xu],[r'$1/2$',r'$1/2+1/6400$',r'$1/2+1/3200$'],rotation=18)
ax.set_yticks([0,float(b/2),float(b)],['0',r'$1/40000$',r'$1/20000$'])
ax.set_xlabel('Original horizontal coordinate x',labelpad=14);ax.set_ylabel('Original vertical coordinate z')
ax.set_title('Actual second horizontal cell Q',pad=20,fontweight='bold')
ax.text((xa+xu)/2,float(3*b/4),'Subrectangle used\nfor the exact lower bound',ha='center',va='center',fontsize=10)
ax.text(.5+float(a)/2,float(1.15*b),'Singular shift at x = 1/2',ha='left',fontsize=11,color='#98382f')
for row,offset,title,color in [(0,F(0),'Correct primitive interval: s = x − 1/2','#217956'),(1,F(1,2),'Source boundary override: s = x','#b35b29')]:
    q=fig.add_subplot(grid[row,1]);left=float(offset+a);right=float(offset+2*a)
    q.add_patch(Rectangle((left,.30),float(a),.4,facecolor=color,alpha=.65,edgecolor=color,lw=2))
    q.set_xlim(float(offset-a/4),float(offset+3*a));q.set_ylim(0,1);q.set_yticks([])
    labels=[r'$1/6400$',r'$1/3200$'] if row==0 else [r'$1/2+1/6400$',r'$1/2+1/3200$']
    q.set_xticks([left,right],labels);q.set_xlabel('Argument s of F(s, b) — separate coordinate window')
    q.set_title(title,pad=15,fontweight='bold',fontsize=12)
    q.text((left+right)/2,.5,r'$0\leq z\leq1/20000$',ha='center',va='center',color='white')
fig.suptitle('A lost coordinate shift changes the integration cell',fontweight='bold',fontsize=18)
fig.supxlabel('Exact proof: true cell integral > 10⁻⁵; old formula < 10⁻¹¹.  Full repair increase ≤ 587/(120000π) after the physical factor.\nChen–Hou source: Holder_ux_const.m 200–226.  Complete derivation: NC11–NC22.  Distinct horizontal windows are shown explicitly.',fontsize=10,y=-.035)
for ext in ['png','svg']:fig.savefig(root/('chen-hou-singular-cell-audit.'+ext),dpi=170,bbox_inches='tight')
print(root/'chen-hou-singular-cell-audit.png')
