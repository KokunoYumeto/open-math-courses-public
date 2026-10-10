"""Full ring kernel samples and exact physical-volume transport maps for lesson32."""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'#f5f7fb','axes.facecolor':'#ffffff'})
ells=np.geomspace(4,256,72);d=1.0;rows=[]
for ell in ells:
 # RK14 after v=2a sin(t): retains the endpoint square-root measure exactly.
 f0=lambda t:2*ell/(d*d+4*ell*ell*math.sin(t)**2)**1.5
 f2=lambda t:2*ell*4*ell*ell*math.sin(t)**2/(d*d+4*ell*ell*math.sin(t)**2)**1.5
 j0,e0=quad(f0,0,math.pi/2,epsabs=1e-12,epsrel=1e-12,limit=300)
 j2,e2=quad(f2,0,math.pi/2,epsabs=1e-12,epsrel=1e-12,limit=300)
 kr=-d*j0/(2*math.pi)+d*j2/(4*math.pi*ell*ell);kz=-j2/(4*math.pi*ell)
 H=math.asinh(ell/d)
 radial_bound=d/(2*math.pi*ell*ell)*(H/4+math.pi+.5)+d/(4*math.pi*ell*ell)*(2*H/math.sqrt(3)+math.pi)
 axial_bound=(2*H/math.sqrt(3)+math.pi)/(4*math.pi*ell)
 assert abs(kr+1/(2*math.pi*d))<=radial_bound+1e-10 and -kz<=axial_bound+1e-10
 rows.append(dict(ell=float(ell),d=d,radial=kr,axial=kz,radial_error=abs(kr+1/(2*math.pi*d)),radial_bound=radial_bound,axial_bound=axial_bound,quadrature_error_j0=e0,quadrature_error_j2=e2))
fig,ax=plt.subplots(1,2,figsize=(13,5.5),layout='constrained')
ax[0].semilogx(ells,[v['radial'] for v in rows],color='#174b81',label=r'Full $K_\ell^r$')
ax[0].semilogx(ells,[v['axial'] for v in rows],color='#a53b2b',label=r'Full $K_\ell^z$ (curvature)')
ax[0].axhline(-1/(2*math.pi),color='#174b81',ls='--',label=r'Planar radial limit $-1/(2\pi d)$')
ax[0].axhline(0,color='#444444',lw=.7)
ax[0].set(xlabel=r'Original ring radius $\ell$',ylabel='Kernel component',title=r'Both physical components; $r=r^{\prime}=0$, $d=1$')
ax[0].legend(fontsize=9);ax[0].grid(alpha=.15)
ax[1].loglog(ells,[v['radial_error'] for v in rows],color='#174b81',label='Radial error: numerical samples')
ax[1].loglog(ells,[v['radial_bound'] for v in rows],color='#174b81',ls='--',label='Proved full radial bound, EX5')
ax[1].loglog(ells,[-v['axial'] for v in rows],color='#a53b2b',label='Curvature magnitude: numerical samples')
ax[1].loglog(ells,[v['axial_bound'] for v in rows],color='#a53b2b',ls='--',label='Proved full curvature bound, EX5')
ax[1].set(xlabel=r'Original ring radius $\ell$',ylabel='Magnitude',title='Retained terms and proved bounds')
ax[1].legend(fontsize=9);ax[1].grid(alpha=.15)
fig.suptitle('The original ring kernel approaches the planar receiver',fontsize=17)
fig.savefig(OUT/'original-ring-kernel.png',dpi=170);fig.savefig(OUT/'original-ring-kernel.svg');plt.close(fig)
(OUT/'original-ring-kernel-samples.json').write_text(json.dumps({'interpretation':'Numerical quadrature samples of the exact RK14 integrals; not proof or eigenvalue computation. EX5 gives the displayed rigorous bounds.','samples':rows},indent=2)+'\n')
fig,ax=plt.subplots(figsize=(13,6.2));fig.subplots_adjust(left=.02,right=.98,bottom=.08,top=.84);ax.set(xlim=(0,13),ylim=(0,6));ax.axis('off')
def box(x,y,title,formula):
 ax.add_patch(FancyBboxPatch((x,y),4.6,1.55,boxstyle='round,pad=.12',fc='white',ec='#174b81',lw=1.6))
 ax.text(x+2.3,y+1.13,title,ha='center',va='center',fontsize=13,color='#174b81')
 ax.text(x+2.3,y+.54,formula,ha='center',va='center',fontsize=15)
box(.3,4.1,'Original physical volume',r'$H_\ell^{\mathrm{vol}}=L^2(2\pi s\varpi\,dr\,dz)$')
box(8.1,4.1,'Original meridian space',r'$H_\ell=L^2(\varpi\,dr\,dz)$')
box(.3,.4,'Physical scalar transport',r'$f\mapsto f\circ\Phi_{-t}^{\ell}$')
box(8.1,.4,'Half-density transport',r'$g\mapsto\sqrt{J_{-t}^{\ell}}\,g\circ\Phi_{-t}^{\ell}$')
for start,end in [((5.05,4.87),(7.85,4.87)),((5.05,1.17),(7.85,1.17)),((2.6,3.83),(2.6,2.2)),((10.4,3.83),(10.4,2.2))]:
 ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=18,color='#174b81',lw=1.5))
ax.text(6.45,5.4,r'$\mathcal{I}_\ell f=\sqrt{2\pi s}\,f$',ha='center',fontsize=13)
ax.text(6.45,1.68,r'$\mathcal{I}_\ell S_\ell(t)\mathcal{I}_\ell^{-1}$',ha='center',fontsize=13)
ax.text(6.5,3.23,r'$s=\ell+r>0$',ha='center',fontsize=15)
ax.text(6.5,2.62,r'$J_{-t}^{\ell}(x)=s(x)/s(\Phi_{-t}^{\ell}x)$',ha='center',fontsize=14)
fig.suptitle('The exact isometry retains the complete physical volume',fontsize=18,y=.96)
fig.text(.5,.025,'EX1-EX3 and RT1-RT7. Both spaces, both domains and the Jacobian factor are proved in the lesson.',ha='center',fontsize=11)
fig.savefig(OUT/'original-ring-volume-map.png',dpi=170);fig.savefig(OUT/'original-ring-volume-map.svg');plt.close(fig)
print(json.dumps({'rendered':['original-ring-kernel.png','original-ring-volume-map.png'],'quadrature_samples':len(rows)}))
