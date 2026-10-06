"""CC0 original exact multiplication-model illustration, no source art adapted."""
from pathlib import Path
import hashlib,json,argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
D=Path(__file__).resolve().parent
args=argparse.ArgumentParser();args.add_argument('--output-dir',type=Path);args=args.parse_args()
O=args.output_dir or D/'figures';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'axes.titlesize':18,'axes.labelsize':15,'svg.hashsalt':'OA-FLOW-DIA-T1-6'})
fig=plt.figure(figsize=(16,11),dpi=200,facecolor='white')
ax=fig.add_axes([.07,.51,.39,.34]);right=fig.add_axes([.58,.51,.35,.34])
r=np.linspace(0,1,1001);ax.plot(r,r,color='#174d6e',lw=2,label=r'$A=M_r$')
for n,color in [(4,'#b75a32'),(16,'#426e44')]:
 for j in range(1,n+1):
  x,y=(j-1)/n,j/n;ax.plot([x,y],[y,y],color=color,lw=2.5 if n==4 else 1.4)
  if n==4:
   ax.scatter([x],[y],s=25,facecolors='white',edgecolors=color,zorder=5);ax.scatter([y],[y],s=25,color=color,zorder=5)
 ax.plot([],[],color=color,label=rf'$A_k$: $N={n}$')
ax.fill_between(r,r,np.minimum(1,r+.25),color='#b75a32',alpha=.10)
ax.set(xlim=(-.02,1.02),ylim=(-.02,1.10),xlabel=r'spectral coordinate $r$',ylabel='bounded multiplier',title='Right-endpoint dyadic approximations')
ax.legend(loc='upper left',frameon=False);ax.grid(alpha=.12)
ax.text(.5,-.32,r'$0\leq A_k-A\leq N^{-1}I$',transform=ax.transAxes,ha='center',fontsize=19)
u=np.linspace(0,.95,500);right.plot(u,u/(1-u),color='#573b7d',lw=3)
right.axvline(1,color='#777777',ls='--',lw=1.5)
right.scatter([.5],[1],color='#b75a32',s=50)
right.annotate(r'$H=M_{r/(1-r)}$',(.76,.76/.24),xytext=(.18,10),arrowprops={'arrowstyle':'->'},fontsize=19)
right.text(.48,17,'Curve stops at r = 0.95;\nthe operator is unbounded.',ha='center',fontsize=14)
right.set(xlim=(0,1.04),ylim=(0,20.5),xticks=[0,.5,1],xlabel=r'bounded coordinate $r$',ylabel='positive density coordinate',title='No spectral mass at r = 0 or r = 1')
right.grid(alpha=.12)
right.text(.5,-.32,r'$1_{(t,\infty)}(H)=M_{1_{(t/(1+t),1)}}$',transform=right.transAxes,ha='center',fontsize=18)
canvas=fig.add_axes([.06,.07,.88,.32]);canvas.set(xlim=(-.025,1.025),ylim=(0,1));canvas.axis('off')
boxes=[(.005,.53,.18,.32,'Nested tails',r'$P(t)=p(f(t))$'),(.235,.53,.20,.32,'Bounded operator',r'$A_k\to A$ in norm'),(.485,.53,.20,.32,'Full Borel domain',r'$H=A/(1-A)$'),(.745,.53,.245,.32,'Faithful profile state',r'$\tau_H\to\phi_f$ by FD')]
for x,y,w,h,title,expr in boxes:
 canvas.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',edgecolor='#32586b',facecolor='#eff5f6',lw=1.4))
 canvas.text(x+w/2,y+h*.73,title,ha='center',fontsize=15)
 canvas.text(x+w/2,y+h*.33,expr,ha='center',fontsize=17)
for x1,x2 in [(.19,.223),(.447,.473),(.697,.733)]:canvas.add_patch(FancyArrowPatch((x1,.69),(x2,.69),arrowstyle='-|>',mutation_scale=20,color='#32586b'))
canvas.text(.5,.29,r'$D(H)=\{\xi:\int_0^1 r^2(1-r)^{-2}|\xi(r)|^2\,dr<\infty\}$',ha='center',fontsize=19)
canvas.text(.5,.09,r'$\xi(r)=1-r$: squared graph contribution $1/3$;  $\xi(r)=1$: infinite.',ha='center',fontsize=16)
fig.suptitle('A tail family determines an affiliated positive operator on its full domain',fontsize=23,y=.97)
fig.text(.5,.91,r'Upper panels: exact commutative model on $L^2(0,1)$; lower chain: the factor proof in Section 6.',ha='center',fontsize=16)
fig.savefig(O/'spectral-tail-construction.png',dpi=200,metadata={'Software':'OA-FLOW original mathematical illustration'},facecolor='white')
fig.savefig(O/'spectral-tail-construction.svg',metadata={'Date':None,'Creator':'OA-FLOW original mathematical illustration'},facecolor='white')
data={'native_pixels':[3200,2200],'model':'L2((0,1),Lebesgue); commutative explanatory model, not a type III factor','coordinate':'A=M_r; H=M_(r/(1-r))','dyadic_bands':{str(n):[{'left':(j-1)/n,'right':j/n,'interval':'(left,right]','value':j/n} for j in range(1,n+1)] for n in [4,16]},'operator_error_bound':'0 <= A_k-A <= 1/N I','tail_threshold':'t/(1+t)','curve_last_coordinate':.95,'curve_last_value':19,'good_vector':'1-r','good_vector_squared_graph_contribution':'1/3','bad_vector':'1','bad_vector_squared_graph_contribution':'infinity','factor_chain':'P(t)=p(f(t)) -> A_k -> A -> H -> tau_H -> phi_f; full faithful FD theorem','rights':'CC0-1.0 to the extent of rights held'}
(O/'spectral-tail-construction-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(O.glob('spectral-tail-construction*'))}))
