"""Exact sampled barrier/envelope diagrams accompanying the full proof S1–S21."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
OWN=Path(__file__).resolve().parent;FIG=OWN/'figures';FIG.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':13,'axes.titlesize':17,'axes.labelsize':14,'svg.hashsalt':'AN02-slice-envelope-S1-S21','font.family':'DejaVu Sans'})

def save(fig,name):
 fig.savefig(FIG/(name+'.png'),dpi=180,bbox_inches='tight',metadata={'Software':'Original AN02 mathematical figures'})
 fig.savefig(FIG/(name+'.svg'),bbox_inches='tight',metadata={'Date':None,'Creator':'Open Mathematics Courses','Description':'Original diagram; exact functions and mathematical locators accompany the full proof.'})
 plt.close(fig)

fig,ax=plt.subplots(figsize=(12.5,7.2))
z=np.linspace(-3,3,361);t=np.linspace(1,3,181);Z,T=np.meshgrid(z,t);psi=Z**2-T**2+9
im=ax.pcolormesh(Z,T,psi,shading='auto',cmap='Blues',vmin=0,vmax=17)
contours=ax.contour(Z,T,psi,levels=[2,4,6,8,10,12,14,16],colors='#315575',linewidths=.6)
ax.clabel(contours,fontsize=10,fmt='%d')
ax.plot([-3,3],[1,1],color='#ca771c',lw=4);ax.plot([-3,3],[3,3],color='#ca771c',lw=4)
ax.plot([-3,-3],[1,3],color='#883d7d',lw=4);ax.plot([3,3],[1,3],color='#883d7d',lw=4)
ax.annotate('Top and bottom: boundary values ≤ L\nThe barrier is nonnegative here.',xy=(0,3),xytext=(0,2.62),arrowprops={'arrowstyle':'->','color':'#ca771c'},color='#87470a',ha='center',bbox={'facecolor':'white','alpha':.94,'edgecolor':'none'})
ax.text(0,-.24,'Lateral sides: C − εR² ≤ 0 for sufficiently large R',transform=ax.transAxes,color='#702766',va='center',clip_on=False)
ax.set(xlim=(-3.05,3.05),ylim=(.95,3.05),xlabel='Horizontal coordinate z',ylabel='Height t',title='A harmonic barrier on the compact slab cylinder (S10–S14)')
ax.text(.02,.035,'n = 2,  a = 1,  b = 3,  R = 3\nΨ(z,t) = z² − t² + 9,   ΔΨ = 0',transform=ax.transAxes,bbox={'facecolor':'white','alpha':.94,'edgecolor':'#abc1d2'},va='bottom')
fig.colorbar(im,ax=ax,pad=.06,label='Exact barrier value Ψ(z,t)')
fig.subplots_adjust(top=.77,right=.90,bottom=.27);save(fig,'slab-barrier')

fig,axes=plt.subplots(1,2,figsize=(15.5,6.2))
ys=np.linspace(.2,6,600);M=np.exp(-ys)-ys/4+.5
a,b=1.,3.;Ma=np.exp(-a)-a/4+.5;Mb=np.exp(-b)-b/4+.5
secant=Ma+(ys-a)*(Mb-Ma)/(b-a)
axes[0].plot(ys,M,color='#21659a',lw=2.8,label='M(t) = e⁻ᵗ − t/4 + 1/2')
axes[0].plot(ys,-ys/4+.5,'--',color='#737373',lw=1.8,label='Affine asymptote: slope γ = −1/4')
mask=(ys>=a)&(ys<=b);axes[0].plot(ys[mask],secant[mask],color='#b96d14',lw=2.4,label='Secant between heights 1 and 3')
axes[0].scatter([a,b],[Ma,Mb],color='#b96d14',zorder=5)
axes[0].set_title('A negative limiting slope is allowed (S19–S20)')
axes[1].plot(ys,np.abs(ys-2),color='#21659a',lw=2.8,label='M(t) = |t − 2|')
axes[1].plot([a,b],[1,1],color='#b96d14',lw=2.4,label='Secant between heights 1 and 3')
axes[1].scatter([a,b],[1,1],color='#b96d14',zorder=5)
axes[1].plot(ys,ys-2,'--',color='#737373',lw=1.6,label='Upper branch: limiting slope γ = 1')
axes[1].annotate('Corner at t = 2:\nsecants still apply',xy=(2,0),xytext=(2.6,-.65),arrowprops={'arrowstyle':'->'},ha='center')
axes[1].set_title('A corner needs no derivative (S21)')
for ax in axes:
 ax.set(xlabel='Height t > 0',ylabel='Horizontal envelope M(t)');ax.grid(alpha=.2);ax.legend(fontsize=10,loc='upper left');ax.axvspan(1,3,color='#b96d14',alpha=.055)
fig.suptitle('Convex envelopes lie below their secants; their limiting slopes bound every increment (S15–S18)',fontsize=17)
fig.tight_layout(rect=(0,0,1,.91));save(fig,'envelopes-and-slopes')
(FIG/'geometry.json').write_text(json.dumps({'barrier':{'n':2,'a':1,'b':3,'R':3,'formula':'z^2-t^2+9','proof_locators':['S10','S11','S13','S14']},'envelopes':{'periodic_example':{'k':1,'alpha':'-1/4','beta':'1/2','M':'exp(-t)-t/4+1/2','gamma':'-1/4'},'corner_example':{'M':'abs(t-2)','gamma':1},'secant_heights':[1,3],'sample_domain':['1/5',6],'proof_locators':['S15','S18','S20','S21']},'plot_status':'Samples of explicit exact functions; no numerical claim substitutes for the proof','source_text':'horizontal-envelopes-and-their-limiting-slope.md'},indent=2)+'\n',encoding='utf-8')
print('Rendered two original PNG/SVG figure pairs and exact geometry metadata.')
