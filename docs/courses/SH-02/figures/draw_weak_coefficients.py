"""Exact module maps and the z-squared nearby fibre. CC0 1.0."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

parser=argparse.ArgumentParser();parser.add_argument('--out',default='.')
out=Path(parser.parse_args().out);out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'weak-coefficients-v1','axes.spines.top':False,'axes.spines.right':False})
blue='#17689b';orange='#b75a0a';ink='#183342';green='#17704c'

def module_panel(ax):
 ax.set(xlim=(-.4,2.45),ylim=(-.55,1.45));ax.axis('off')
 ax.set_title('A nonzero quotient survives',loc='left',fontweight='bold',color=ink,pad=14)
 ax.text(.02,1.08,r'$\mathbb{Z}/2$',ha='center',fontsize=17,color=blue)
 ax.text(1,1.08,r'$\mathbb{Z}/4$',ha='center',fontsize=17,color=ink)
 ax.text(2,1.08,r'$\mathbb{Z}/2$',ha='center',fontsize=17,color=orange)
 for x,vals in [(0,[0,1]),(1,[0,1,2,3]),(2,[0,1])]:
  ys=np.linspace(.75,-.05,len(vals))
  for y,v in zip(ys,vals):
   ax.scatter([x],[y],s=180,color=blue if x==0 else orange if x==2 else ink,zorder=3)
   ax.text(x,y,str(v),ha='center',va='center',color='white',fontsize=10,zorder=4)
 def arr(x1,y1,x2,y2,c):ax.annotate('',(x2-.1,y2),(x1+.1,y1),arrowprops={'arrowstyle':'->','color':c,'lw':1.5,'alpha':.85})
 arr(0,.75,1,.75,blue);arr(0,-.05,1,.75-2*.8/3,blue)
 for v in range(4):arr(1,.75-v*.8/3,2,.75 if v%2==0 else -.05,orange)
 ax.text(.48,.91,r'$a\mapsto 2a$',ha='center',color=blue,fontsize=11)
 ax.text(1.51,.91,r'$b\mapsto b\ (\mathrm{mod}\ 2)$',ha='center',color=orange,fontsize=11)
 ax.text(1,-.38,'Both lifts of 1 have order 4: no section.\nWC14 proves survival; WC20 is an algebraic example.',ha='center',va='top',fontsize=10,color=ink)

def fibre_panel(ax):
 z=np.linspace(-.42,.42,401);ax.plot(z,z*z,color=blue,lw=2)
 ax.axhline(1/16,color=orange,ls='--',lw=1.4)
 ax.scatter([-.25,.25],[1/16,1/16],color=orange,s=52,zorder=3)
 ax.annotate(r'$-1/4$',(-.25,1/16),(-.37,.093),arrowprops={'arrowstyle':'-','color':ink},fontsize=11)
 ax.annotate(r'$+1/4$',(.25,1/16),(.25,.105),arrowprops={'arrowstyle':'-','color':ink},fontsize=11)
 ax.text(-.4,.045,r'$w=1/16$',color=orange,fontsize=11)
 ax.set(xlim=(-.44,.44),ylim=(-.014,.185),xlabel=r'$\operatorname{Re}z$',ylabel=r'$\operatorname{Re}w$')
 ax.set_title(r'Two points of $w=z^2$',loc='left',fontweight='bold',color=ink,pad=14)
 ax.set_xticks([-.25,0,.25],['−1/4','0','1/4']);ax.set_yticks([0,1/16,1/8],['0','1/16','1/8'])
 ax.text(.5,-.23,'Real section Im z = Im w = 0.\nThe theorem uses the full complex map.',transform=ax.transAxes,ha='center',fontsize=10,color=ink)

def maps_panel(ax):
 ax.axis('off');ax.set_title('Infinite coefficients, actual maps',loc='left',fontweight='bold',color=ink,pad=14)
 ax.text(.02,.86,r'$M=\bigoplus_{j\geq1}\mathbb{Z}/2$',fontsize=18,color=ink)
 ax.text(.02,.68,r'$M\ \longrightarrow\ M\oplus M\ \longrightarrow\ M$',fontsize=17,color=blue)
 ax.text(.05,.54,r'$m\mapsto(m,m)\qquad (a,b)\mapsto b-a$',fontsize=13,color=blue)
 ax.text(.02,.34,r'$\Phi_{z^2}(M_{\mathbb{C}})_0\simeq M$',fontsize=18,color=green)
 ax.text(.02,.15,'The diagonal is injective; its cokernel is M.\nRoot exchange induces −1 (equal to 1 here).\nThe cone is unshifted. WC21.',fontsize=11,color=ink,linespacing=1.5)

for mode in ['wide','mobile']:
 if mode=='wide':
  fig,axes=plt.subplots(1,3,figsize=(16.5,5.25));fig.subplots_adjust(left=.025,right=.985,bottom=.2,top=.85,wspace=.3)
 else:
  fig,axes=plt.subplots(3,1,figsize=(6,14));fig.subplots_adjust(left=.12,right=.93,bottom=.055,top=.955,hspace=.48)
 for ax,draw in zip(axes,[module_panel,fibre_panel,maps_panel]):draw(ax)
 fig.patch.set_facecolor('white')
 footer='Exact maps and coordinates • Finite holomorphic maps with arbitrary weak coefficients • CC0 1.0' if mode=='wide' else 'Exact maps and coordinates • Arbitrary weak coefficients\nFinite holomorphic maps • CC0 1.0'
 fig.text(.025,.035 if mode=='wide' else .014,footer,fontsize=9,color=ink)
 for ext in ['svg','png','pdf']:
  meta={'Date':None} if ext=='svg' else {'CreationDate':None,'ModDate':None} if ext=='pdf' else {}
  fig.savefig(out/f'weak-coefficients-{mode}.{ext}',dpi=150,metadata=meta)
 plt.close(fig)
