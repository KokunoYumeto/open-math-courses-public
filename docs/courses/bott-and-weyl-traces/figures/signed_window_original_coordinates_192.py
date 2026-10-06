"""Exact frozen window ellipses in their original coordinates. CC0-1.0."""
from pathlib import Path
from fractions import Fraction
import json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
out=Path(__file__).resolve().parent
params=out/'signed-window-original-coordinates-parameters.json'
image=out/'signed-window-original-coordinates.png'
rows=[]
fig,axes=plt.subplots(1,2,figsize=(14,6.8))
for ax,rho,delta,name in zip(axes,[1,-1],[0,-2],['Classical parameters','Negative parameters']):
 sigma=Fraction(rho+delta,2);kappa=rho-delta;lam=16
 Q=lam**float(sigma);wx=1/Q;wf=Q;mx=lam**(-delta);mf=lam**rho
 assert wx*wf==1 and mx*mf==16 and kappa==1
 assert abs((lam**(2*delta))*wx**2-1/16)<1e-12
 assert abs((lam**(-2*rho))*wf**2-1/16)<1e-12
 ax.add_patch(Ellipse((0,0),2*mx,2*mf,facecolor='#f0f4f8',edgecolor='#596b80',linewidth=2,label='Original metric unit ball'))
 ax.add_patch(Ellipse((0,0),2*wx,2*wf,facecolor='#45abc788',edgecolor='#006582',linewidth=2,label='Frozen window ellipse'))
 ax.axhline(0,color='#959595',lw=.7);ax.axvline(0,color='#959595',lw=.7)
 ax.set_xlim(-1.16*mx,1.16*mx);ax.set_ylim(-1.16*mf,1.16*mf)
 # Every plotted value is in the original coordinate. Different panel units are labeled.
 xticks=[-mx,-wx,0,wx,mx];yticks=[-mf,-wf,0,wf,mf]
 def label(x):
  f=Fraction(x).limit_denominator()
  return str(f.numerator) if f.denominator==1 else f'{f.numerator}/{f.denominator}'
 ax.set_xticks(xticks,labels=[label(x) for x in xticks]);ax.set_yticks(yticks,labels=[label(x) for x in yticks])
 ax.set_xlabel(r'Original position increment $y-x$',fontsize=12)
 ax.set_ylabel(r'Original frequency increment $\eta-\xi$',fontsize=12)
 ax.set_title(name+'\n'+rf'$\rho={rho},\ \delta={delta},\ \sigma={sigma},\ \kappa=1$',fontsize=13,pad=12)
 ax.legend(loc='upper right',fontsize=9,framealpha=1)
 ax.text(.5,-.24,rf'$Q={label(Q)}$: window radii $({label(wx)}, {label(wf)})$'+'\n'+rf'Metric radii $({label(mx)}, {label(mf)})$; window boundary $g=1/16$',transform=ax.transAxes,ha='center',fontsize=11)
 rows.append(dict(rho=rho,delta=delta,sigma=str(sigma),kappa=kappa,lambda_bracket=16,Q=label(Q),window_radii=[label(wx),label(wf)],metric_radii=[label(mx),label(mf)],window_area='pi',metric_area='16*pi',window_boundary_metric='1/16'))
fig.suptitle(r'Original coordinate windows at $x=0,\ \xi=\sqrt{255},\ \langle\xi\rangle=16$',fontsize=16,y=.98)
fig.subplots_adjust(left=.08,right=.985,bottom=.25,top=.81,wspace=.3)
fig.savefig(image,dpi=160,facecolor='white');plt.close(fig)
params.write_text(json.dumps(dict(license='CC0-1.0',base_point={'x':0,'xi':'sqrt(255)'},panels=rows,meaning='Frozen tangent-coordinate comparison; no assertion that the moving window is constant or that the Schwartz seed is supported in the ellipse.',proof_locators=['P8e','P28e','P34','P35--P42f']),indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(image=image.name,parameters=params.name,panels=len(rows))))
