"""Exact-data illustration of BI normal division, transpose mixing and input map."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,log10,comb
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,FancyBboxPatch
import numpy as np
root=Path(__file__).resolve().parent
out=root if root.name=='assets'else root/'assets';out.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'BI-whole-incidence'})
c=F(1,4)
term=lambda j,m:c**(m-j)*F(factorial(m-j),factorial(m)**2)
normal=[];S=F(0)
for J in range(13):
 S+=F((-1)**J,factorial(J))
 nextS=S+F((-1)**(J+1),factorial(J+1))
 normal.append({'J':J,'partial':str(S),'lower':str(min(S,nextS)),'upper':str(max(S,nextS))})
reference=sum((F((-1)**m,factorial(m))for m in range(41)),F(0))
refnext=reference-F(1,factorial(41));reflo,refhi=refnext,reference
contributions=[]
grid=np.full((13,13),np.nan)
for row,j in enumerate(range(-6,7)):
 for m in range(13):
  if m<j:continue
  a=term(j,m);grid[row,m]=log10(float(a))
  contributions.append({'j':j,'m':m,'loss':m-j,'sign':(-1)**j if j>=0 else (-1 if j%2 else 1),'absolute_rational':str(a)})
intervals=[]
for j in range(-5,6):
 lower=sum((term(j,m)for m in range(max(0,j),41)),F(0))
 upper=lower+2*term(j,41)
 intervals.append({'j':j,'sign':-1 if j%2 else 1,'J':40,'lower_abs':str(lower),'upper_abs':str(upper)})
fig,axes=plt.subplots(2,2,figsize=(14,10))
fig.suptitle('The whole infinite-order incidence module',fontsize=19,y=.99)
ax=axes[0,0]
J=[x['J']for x in normal];vals=[float(F(x['partial']))for x in normal]
ax.plot(J,vals,'o-',color='#26678a',lw=1.3,label=r'$N(P_1^{[J]})_0$')
for x in normal:
 j=x['J'];lo=float(F(x['lower']));hi=float(F(x['upper']))
 ax.plot([j+.12,j+.12],[lo,hi],color='#b65f26',lw=2)
ax.axhspan(float(reflo),float(refhi),color='#2d7148',label=r'$e^{-1}\in[S_{41},S_{40}]$')
ax.axhline(float((reflo+refhi)/2),color='#2d7148',ls='--',lw=1)
ax.set(xlabel='Positive input cutoff J',ylabel='Normal coefficient of degree zero',xlim=(-.5,12.5),ylim=(-.08,1.08))
ax.set_xticks([0,2,4,6,8,10,12]);ax.legend(loc='upper right',fontsize=9)
ax.set_title('A. Infinitely many degrees contribute to one coefficient',fontsize=12,pad=10)
ax.text(.48,.08,r'$P_1=\sum_{m\geq0} f^m D_f^m/(m!)^2$'+'\n'+r'$N(P_1)_0=e^{-1}$; BI.16–BI.17',transform=ax.transAxes,fontsize=11)
ax=axes[0,1];cmap=plt.get_cmap('viridis').copy();cmap.set_bad('#d7dde2')
im=ax.imshow(grid,origin='lower',aspect='auto',extent=(-.5,12.5,-6.5,6.5),cmap=cmap)
ax.set(xlabel='Nonnegative input degree m',ylabel='Output j (row sign)',title='B. Transpose contributions; BI.27')
ax.set_yticks(list(range(-6,7)));ax.set_yticklabels([f'{j} ({"+"if j%2==0 else "−"})'for j in range(-6,7)])
ax.set_xticks([0,2,4,6,8,10,12])
fig.colorbar(im,ax=ax,pad=.02,label=r'$\log_{10}|a_{j,m}|$')
ax.text(.02,.03,'Gray: m < j, so the loss is negative.',transform=ax.transAxes,color='black',
 bbox={'facecolor':'white','alpha':.85,'edgecolor':'none'},fontsize=9)
ax=axes[1,0]
for row in intervals:
 j=row['j'];lo=float(F(row['lower_abs']));hi=float(F(row['upper_abs']))
 ax.vlines(j,lo,hi,color='#b65f26',lw=2)
 ax.plot(j,(lo+hi)/2,'o'if row['sign']>0 else'x',color='#26678a'if row['sign']>0 else'#b65f26',ms=7)
ax.set_yscale('log');ax.set_xticks(list(range(-5,6)))
ax.set(xlabel='Output homogeneous degree j',ylabel=r'$|(TP)_j(0)|$',title='C. Exact rational enclosures; BI.28, J = 40')
ax.text(.03,.06,'○ positive coefficient; × negative coefficient\nInterval widths are smaller than the markers.',
 transform=ax.transAxes,fontsize=10)
ax=axes[1,1];ax.axis('off');ax.set_title('D. The two actual input maps agree',fontsize=12,pad=10)
def box(x,y,label):
 ax.add_patch(FancyBboxPatch((x,y),.25,.15,boxstyle='round,pad=.02',facecolor='#e4eff3',edgecolor='#26678a'))
 ax.text(x+.125,y+.075,label,ha='center',va='center',fontsize=15)
box(.04,.7,r'$E_Y$');box(.67,.7,r'$E_X$');box(.04,.32,r'$B_Y$');box(.67,.32,r'$B_X$')
for start,end in [((.31,.775),(.65,.775)),((.31,.395),(.65,.395)),((.165,.67),(.165,.49)),((.795,.67),(.795,.49))]:
 ax.add_patch(FancyArrowPatch(start,end,arrowstyle='->',mutation_scale=14,color='#26678a',lw=1.5))
ax.text(.48,.86,r'$L_0$ (FIM.B)',ha='center',fontsize=11)
ax.text(.48,.49,r'$\Phi_B=L_0$ (BI.25)',ha='center',fontsize=11)
ax.text(.48,.17,r'$eR=L_0(R)e$',ha='center',fontsize=14)
ax.text(.48,.06,r'Cutoff error: $\rho^{J+1}$ in both coefficient classes.'+'\n'
 'Both cutoffs retain the entire negative tail.',ha='center',fontsize=10)
for ax in axes.flat:
 if ax.axison:ax.spines[['top','right']].set_visible(False)
fig.text(.5,.012,'A: alternating rational enclosures. B–C: one spatial variable, y = w = 0, normal covariable = 1, c = 1/4.\n'
 'The plots are finite windows; BI.4–BI.6 proves the whole transpose, quotient and input action on one common domain.',
 ha='center',fontsize=10)
fig.tight_layout(rect=(0,.065,1,.965))
fig.savefig(out/'infinite-incidence-positive-tails.png',dpi=180,facecolor='white')
fig.savefig(out/'infinite-incidence-positive-tails.svg',facecolor='white',metadata={'Date':None})
data={'normal_example':{'a':1,'cutoffs':normal,'reference_lower':str(reflo),'reference_upper':str(refhi),
 'reference_indices':[41,40]},'transpose_example':{'c':'1/4','y':0,'w':0,'normal_covariable':1,
 'input_m_window':[0,12],'output_j_window':[-6,6],'sign':'(-1)^j',
 'contributions':contributions,'enclosures':intervals},
 'commuting_maps':{'finite':'FIM.B','whole':'BI.25','cutoff_error':'BI.24'},
 'free_human_context':'https://arxiv.org/abs/2102.08861v2',
 'proof_locators':['BI.16–BI.17','BI.27–BI.28','BI.18–BI.25']}
(out/'infinite-incidence-positive-tails-exact-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print('Wrote 2520x1800 PNG, deterministic SVG and exact rational data.')
