"""Exact parity and coordinate diagram for the full relative unit form."""
from pathlib import Path
from fractions import Fraction as F
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,FancyBboxPatch
from matplotlib.colors import ListedColormap
import numpy as np
root=Path(__file__).resolve().parent;out=root if root.name=='assets'else root/'assets';out.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'UC-relative-unit'})
fig,axes=plt.subplots(2,2,figsize=(14,9))
fig.suptitle('The full relative diagonal unit and its hyperplane coordinates',fontsize=18,y=.99)
parities=[]
for N in range(1,9):
 r=(-1)**(N*(N-1)//2)
 parities.append({'N':N,'d':N-1,'r_N':r,'top_cube_sign':r*(-1)**N,'reverse_parameter_Jacobian':(-1)**(N-1)})
ax=axes[0,0];matrix=np.array([[p[k]for p in parities]for k in ['r_N','top_cube_sign','reverse_parameter_Jacobian']])
ax.imshow(matrix,cmap=ListedColormap(['#f4d9c6','#dceaf2']),vmin=-1,vmax=1,aspect='auto')
for row in range(3):
 for col in range(8):ax.text(col,row,'+1'if matrix[row,col]>0 else'−1',ha='center',va='center',color='black')
ax.set_yticks([0,1,2]);ax.set_yticklabels([r'$r_N$',r'$r_N(-1)^N$',r'$(-1)^d$'])
ax.set_xticks(list(range(8)));ax.set_xticklabels([p['N']for p in parities])
ax.set(xlabel='Complex normal dimension N; d = N − 1',title='A. Three separate orientation signs; UC.1, UC.15, UC.19')
ax=axes[0,1];weights=[]
for k in range(121):
 q=F(k,40);rho0=1/(1+q*q);rho1=q*q/(1+q*q)
 weights.append({'q':str(q),'rho0':str(rho0),'rho1':str(rho1)})
ax.plot([float(F(x['q']))for x in weights],[float(F(x['rho0']))for x in weights],color='#26678a',label=r'$\rho_0=1/(1+q^2)$')
ax.plot([float(F(x['q']))for x in weights],[float(F(x['rho1']))for x in weights],color='#b65f26',label=r'$\rho_1=q^2/(1+q^2)$')
ax.set(xlabel='Real slice w = (1,q), N = 2',ylabel='Partition weights',title='B. Exact generating weights; UC.12–UC.14',ylim=(-.05,1.05))
ax.text(1.65,.86,r'$\rho_1=q^2/(1+q^2)$',color='#b65f26',fontsize=11)
ax.text(1.65,.12,r'$\rho_0=1/(1+q^2)$',color='#26678a',fontsize=11)
ax.text(.52,.43,'Weights on this real slice only;\nno normal period is plotted.',transform=ax.transAxes,fontsize=9)
ax=axes[1,0];ax.axis('off');ax.set(xlim=(-.1,1.15),ylim=(-.15,1.1));ax.set_title('C. A parameter simplex retains all its faces',fontsize=12)
points=[(.1,.08),(.95,.08),(.525,.85)]
for x,y,label in [(points[i][0],points[i][1],rf'$a^{i}$')for i in range(3)]:
 ax.plot([x],[y],'o',color='#26678a',ms=7);ax.text(x,y+(.04 if label==r'$a^2$'else-.09),label,ha='center',fontsize=14)
for a,b in [(0,1),(1,2),(2,0)]:
 ax.add_patch(FancyArrowPatch(points[a],points[b],arrowstyle='->',mutation_scale=13,color='#26678a',lw=1.5,shrinkA=8,shrinkB=8))
ax.text(.525,.38,r'$\sum_{j=0}^{2}u_j a^j$',ha='center',fontsize=15)
ax.text(.525,.23,r'$u_0+u_1+u_2=1,\quad u_j\geq0$',ha='center',fontsize=12)
ax.text(.525,1.02,r'$\bar\partial H_{012}=-H_{12}+H_{02}-H_{01}$',ha='center',fontsize=13)
ax.text(.525,-.14,'N ≥ 3; the simplex is a parameter domain (UC.11).',ha='center',fontsize=10)
ax=axes[1,1];ax.axis('off');ax.set_title('D. The reverse spatial parameter has a Jacobian',fontsize=12)
for y,title,formula in [(.6,'Forward',r'$w=(\Delta t,\Delta x),\quad \xi=(1,y)$'),
 (.23,'Reverse',r"$w'=(\Delta s,\Delta y),\quad \xi'=(1,-x)$")]:
 ax.add_patch(FancyBboxPatch((.03,y),.92,.22,boxstyle='round,pad=.02',facecolor='#e4eff3',edgecolor='#26678a'))
 ax.text(.49,y+.15,title,ha='center',fontsize=12)
 ax.text(.49,y+.045,formula,ha='center',fontsize=13)
ax.text(.49,.05,r'$d(-x_1)\wedge\cdots\wedge d(-x_d)=(-1)^d\,dx_1\wedge\cdots\wedge dx_d$',ha='center',fontsize=11)
ax.text(.49,-.065,'Both ordinary normal residues are positive; UC.19 concerns the spatial form.',ha='center',fontsize=9)
for ax in [axes[0,1]]:ax.spines[['top','right']].set_visible(False)
fig.text(.5,.009,'The current identity and complete complement-cube comparison are UC.6–UC.15. The universal form is UC.16–UC.19; its identification with an incidence composition is a separate assertion.',
 ha='center',fontsize=9)
fig.tight_layout(rect=(0,.06,1,.95))
fig.savefig(out/'relative-unit-form-and-parameters.png',dpi=180,facecolor='white')
fig.savefig(out/'relative-unit-form-and-parameters.svg',facecolor='white',metadata={'Date':None})
record={'signs':parities,'N2_real_slice_weights':weights,
 'parameter_simplex':{'dimension':2,'minimum_N':3,'identity':'dbar H012=-H12+H02-H01','vertices':[[str(x),str(y)]for x,y in points]},
 'coordinates':{'forward':['Delta t','Delta x','1','y'],'reverse':['Delta s','Delta y','1','-x'],'Jacobian':'(-1)^d'},
 'proof_locators':['UC.1','UC.6–UC.15','UC.16–UC.19'],
 'free_context':'https://haroldpboas.gitlab.io/courses/685-2005c/notes.pdf',
 'analytic_incidence_inverse_product_claimed':False}
(out/'relative-unit-form-and-parameters-exact-data.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print('Wrote 2520x1620 PNG, deterministic SVG and exact sign/weight data.')
