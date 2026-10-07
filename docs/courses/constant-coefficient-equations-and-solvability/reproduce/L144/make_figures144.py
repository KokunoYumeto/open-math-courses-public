"""Original exact-constant illustrations for weighted dbar existence (CC0).

Matplotlib/NumPy only; no TeX process, persistent browser or cache profile.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

HERE=Path(__file__).resolve().parent;OUT=HERE/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.labelsize':11,'axes.titlesize':12,'svg.fonttype':'none','svg.hashsalt':'AN02-L144','text.usetex':False,'savefig.dpi':170})
BLUE='#2563a6';ORANGE='#bf5700';GREEN='#1f7856';GREY='#596575'

def save(fig,name):
    fig.savefig(OUT/(name+'.png'),facecolor='white',metadata={'Software':'Original AN-02 lesson144 figure script'})
    fig.savefig(OUT/(name+'.svg'),facecolor='white',metadata={'Creator':'Original AN-02 lesson144 figure script','Date':None})
    plt.close(fig)

r=np.linspace(0,4,801)
radial=2/(1+r*r)**2;tangential=2/(1+r*r)
fig,axes=plt.subplots(1,2,figsize=(11.6,5.4),gridspec_kw={'width_ratios':[1.25,1]})
fig.subplots_adjust(left=.075,right=.975,top=.81,bottom=.22,wspace=.31)
fig.suptitle('Why the general estimate has factor 2 and power 2',y=.965,fontsize=16)
fig.text(.5,.89,r'Added weight: $2\log(1+|z|^2)$; exact Levi eigenvalues',ha='center',color=GREY)
ax=axes[0];ax.semilogy(r,radial,color=BLUE,lw=2.5,label=r'Radial: $2/(1+r^2)^2$')
ax.semilogy(r,tangential,color=ORANGE,lw=2.5,label=r'Tangential: $2/(1+r^2)$')
ax.axvline(2,color=GREY,ls=':',lw=1)
ax.scatter([2,2],[2/25,2/5],color=[BLUE,ORANGE],zorder=4)
ax.set(xlabel=r'Radius $r=|z|$',ylabel='Levi eigenvalue (log scale)',title='The least curvature decays as the square')
ax.set_xlim(0,4);ax.grid(alpha=.2,which='both');ax.legend(loc='upper right',fontsize=10)
theta=np.linspace(0,2*np.pi,721);a=5/np.sqrt(2);b=np.sqrt(5/2)
ax=axes[1];ax.plot(a*np.cos(theta),b*np.sin(theta),color=GREEN,lw=2.5)
ax.axhline(0,color=GREY,lw=.8);ax.axvline(0,color=GREY,lw=.8)
ax.annotate('',xy=(a,0),xytext=(0,0),arrowprops={'arrowstyle':'->','color':BLUE,'lw':2})
ax.annotate('',xy=(0,b),xytext=(0,0),arrowprops={'arrowstyle':'->','color':ORANGE,'lw':2})
ax.text(a/2,-.40,r'$5/\sqrt{2}$',ha='center',color=BLUE)
ax.text(.15,b/2,r'$\sqrt{5/2}$',color=ORANGE,va='center')
ax.set(xlabel=r'Real radial test component $\xi_1$',ylabel=r'Real tangential component $\xi_2$',title=r'At $z=(2,0)$ in $\mathbb{C}^2$: Levi level 1')
ax.set_aspect('equal');ax.set_xlim(-4,4);ax.set_ylim(-2,2);ax.grid(alpha=.18)
fig.text(.075,.06,'The right panel is a real two-coordinate section of test vectors, not the full complex sphere.\nFormal W25–W26; learner §3. Human source: Hörmander II, Theorem 15.1.2.',fontsize=10,color=GREY)
save(fig,'levi-curvature')

r=np.linspace(0,5,1201)
modulus=np.where(r<=1,r,1/np.maximum(r,1e-30))
density=2*np.pi*r*modulus**2/(1+r*r)**2
s=r*r
inside=np.pi*(np.log1p(s)+1/(1+s)-1)
outside=np.zeros_like(s)
mask=s>1
outside[mask]=np.pi*(2*np.log(2)-1+np.log(s[mask]/(1+s[mask]))+1/(1+s[mask]))
I=np.where(mask,outside,inside);ratio=2*I/np.pi;limit=4*np.log(2)-2
fig,axes=plt.subplots(1,3,figsize=(12.7,5.3))
fig.subplots_adjust(left=.06,right=.975,top=.79,bottom=.22,wspace=.38)
fig.suptitle('An exact disk solution uses less than the weighted norm budget',y=.965,fontsize=16)
fig.text(.5,.875,r'$f=1_{|z|<1}$; $u=\bar z$ inside, $u=1/z$ outside; data norm $B_0=\pi$',ha='center',color=GREY)
axes[0].plot(r,modulus,color=BLUE,lw=2.4)
axes[0].set(xlabel=r'Radius $r$',ylabel=r'Solution modulus $|u|$',title='Matching values at the circle')
axes[1].plot(r,density,color=GREEN,lw=2.4)
axes[1].fill_between(r,density,where=r<=1,color=BLUE,alpha=.18)
axes[1].fill_between(r,density,where=r>=1,color=ORANGE,alpha=.18)
axes[1].set(xlabel=r'Radius $r$',ylabel=r'$2\pi r|u|^2/(1+r^2)^2$',title='Equal inside and outside integrals')
axes[2].plot(r,ratio,color=BLUE,lw=2.4,label=r'Accumulated $2I_R/\pi$')
axes[2].axhline(1,color=ORANGE,ls='--',lw=1.7,label='Theorem bound: 1')
axes[2].axhline(limit,color=GREEN,ls=':',lw=1.8,label=r'Limit: $4\log 2-2$')
axes[2].set(xlabel=r'Integration radius $R$',ylabel='Fraction of allowed bound',title='Exact total ratio ≈ 0.772589')
axes[2].set_ylim(0,1.08);axes[2].legend(loc='lower right',fontsize=9)
for ax in axes:
    ax.axvline(1,color=GREY,ls=':',lw=1);ax.grid(alpha=.18);ax.set_xlim(0,5)
fig.text(.06,.078,r'Each side contributes $\pi(\log 2-1/2)$. The finite-radius graph approaches the full integral.'+'\nLearner Example 2 and Exercise 6; formal W5. Human source for the estimate: Hörmander II, Theorem 15.1.2.',fontsize=10,color=GREY)
save(fig,'disk-solution-budget')

geometry={
    'schema':'AN02-L144-exact-illustration-geometry/v1',
    'levi_curvature':{'weight':'2 log(1+|z|^2)','radial_eigenvalue':'2/(1+r^2)^2','tangential_eigenvalue':'2/(1+r^2), n>=2','section':'Real xi1,xi2 of complex test vectors at z=(2,0) in C^2','at_r2_eigenvalues':[2/25,2/5],'section_semiaxes_exact':['5/sqrt(2)','sqrt(5/2)'],'proof':'formal W25-W26; learner section3'},
    'disk_solution':{'dimension':'C^1, ordinary area dA','datum':'indicator(|z|<1)','solution':'bar(z) for |z|<=1;1/z for |z|>1','norm_weight':'(1+|z|^2)^(-2)','data_norm':'pi','each_side_norm':'pi*(log(2)-1/2)','total_norm':'2*pi*(log(2)-1/2)','total_normalized_ratio':'4*log(2)-2','ratio_numeric':float(limit),'plotted_radius_max':5,'finite_radius_qualified':True,'proof':'learner Example2 and Exercise6'},
    'human_source':'Lars Hörmander, Analysis of Linear PDE II, Theorems15.1.1-15.1.2, printed271-274',
    'original_artwork_license':'CC0-1.0','font':'DejaVu Sans; separate font license retained','protected_source_images_used':False,
}
(OUT/'geometry.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Two original PNG/SVG pairs and exact geometry written.')
