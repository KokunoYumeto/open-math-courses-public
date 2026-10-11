"""Exact energy-limit and global-continuation mechanisms; CC0 1.0."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
D=Path(__file__).resolve().parent.parent/'figures'
plt.rcParams.update({'svg.hashsalt':'YM-F09-EL-GC','font.family':'DejaVu Sans','font.size':12})

def box(ax,x,y,w,h,title,body):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',
        facecolor='#eef5fa',edgecolor='#28516b',linewidth=1.4))
    ax.text(x+w/2,y+h-.033,title,ha='center',va='top',fontweight='bold',fontsize=13,color='#17384d')
    ax.text(x+w/2,y+.015,body,ha='center',va='bottom',fontsize=12,linespacing=1.55)

def arrow(ax,p,q):
    ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=17,color='#28516b',linewidth=1.7))

def save(fig,stem):
    fig.savefig(D/(stem+'.svg'),metadata={'Date':None},bbox_inches='tight')
    fig.savefig(D/(stem+'.png'),dpi=150,bbox_inches='tight')
    plt.close(fig)

def build():
    D.mkdir(exist_ok=True)
    fig,ax=plt.subplots(figsize=(12,9));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
    ax.text(.5,.99,'Pass the full curvature to the energy-data limit',
        ha='center',va='top',fontsize=19,fontweight='bold')
    box(ax,.045,.755,.41,.16,'Actual temporal increment',
        r'$h_n(t)=\int_{t_*}^{t}E_n(r)\,dr$'+'\n'+r'$E_n$ Cauchy in $C(J;L^2)$')
    box(ax,.545,.755,.41,.16,'Actual potential gradient',
        r'$\partial(A_n-A_m)\to0$ in $C(J;L^2)$'+'\n'+r'$A_n=A_{*,n}+h_n$')
    arrow(ax,(.25,.737),(.4,.66));arrow(ax,(.75,.737),(.6,.66))
    box(ax,.16,.465,.68,.19,'The same increment in three spaces',
        r'$h_n$ Cauchy in $C(J;L^2\cap L^6)$'+'\n'+
        r'$\|h_n-h_m\|_3\leq\|h_n-h_m\|_2^{1/2}\|h_n-h_m\|_6^{1/2}$')
    arrow(ax,(.5,.45),(.5,.385))
    box(ax,.075,.175,.85,.20,'Every curvature term has its receiving space',
        r'$F(A_n)=F(A_{*,n})+dh_n+[A_{*,n},h_n]+[h_n,A_{*,n}]+[h_n,h_n]$'+'\n'+
        r'Initial full curvature: $C(J;L^2)$; all six difference products: $L^6L^3\subset L^2$.')
    ax.text(.5,.097,r'$F(A_n)\to F(A)$ in $C(J;L^2)$, with every ordered $(i,j)$ component.',
        ha='center',fontsize=14,color='#17384d')
    ax.text(.5,.035,'EL.14–EL.20 give the indexed identity and exact constants. The diagram abbreviates only the indices.',
        ha='center',fontsize=11)
    ax.text(.5,-.005,'EL.26–EL.28 then pass the full physical energy and flux and retain the boundary at spatial infinity.',
        ha='center',fontsize=11)
    save(fig,'f09-energy-data-limit')

    fig=plt.figure(figsize=(13,9))
    fig.suptitle('A finite horizon gives a bound for the original potential',fontsize=19,fontweight='bold',y=.985)
    left=fig.add_axes([.025,.13,.51,.80]);left.set(xlim=(0,1),ylim=(0,1));left.axis('off')
    for y,title,body in [
        (.79,'Original data and one heat endpoint',r'$R_g,\ d,\ c,\ \ell,\ S,\ H$'),
        (.585,'Fixed-time arrays at every wave anchor',r'$P_k(H),\ Q_k(H),\ M_k(H)$; GC.13–GC.22'),
        (.38,'A common covering length',r'$\tau_w(H)>0,\quad N_H=\lceil H/\tau_w(H)\rceil$'),
        (.175,'Recover the original potential',r'$M_H=(1+2C_Sp_H)\mathcal{R}_a(H)+k_H<\infty$')]:
        box(left,.03,y,.94,.15,title,body)
    for y in [.775,.57,.365]:arrow(left,(.5,y),(.5,y-.03))
    left.text(.5,.085,r'Only now: $\sigma_H=\min(S,S_{R_{\rm restart}})>0$.',
        ha='center',fontsize=12,color='#17384d')
    left.text(.5,.025,'RC constructs the actual regular restart; GC.44–GC.47.',ha='center',fontsize=11)
    right=fig.add_axes([.62,.29,.34,.53])
    alpha=np.linspace(-2,2,321);ell=2.;kappa=2.
    gradient=kappa*alpha**2*15*np.pi**1.5/(4*ell)
    right.plot(alpha,gradient,color='#265c83',lw=2.4,label=r'$\|\partial A^0\|_2^2$')
    right.plot(alpha,np.zeros_like(alpha),color='#b43d32',lw=2,label=r'$d^2=0$')
    right.set(xlabel=r'$\alpha$ (dimensionless)',ylabel=r'Squared norm (${\rm m}^{-1}$)',
        title='Exact zero-energy gauge orbit')
    right.grid(alpha=.22);right.legend(loc='upper center')
    fig.text(.79,.205,r'$A_i^0=\alpha\,\partial_i e^{-|x|^2/(2\ell^2)}T,\quad E^0=0$',ha='center',fontsize=12)
    fig.text(.79,.164,r'$\ell=2\ {\rm m},\quad T=\mathrm{diag}(i,-i),\quad\kappa_T=2$',ha='center',fontsize=11)
    fig.text(.79,.123,'GC.52–GC.53: an exact field, not a sampled evolution.',ha='center',fontsize=10)
    fig.text(.5,.046,'GC.13–GC.47 retain the nonidentity static heat gauge and the original temporal anchor on every covering piece.',
        ha='center',fontsize=11)
    fig.text(.5,.017,'Energy controls curvature. The displayed gauge derivatives supply the additional potential bound.',
        ha='center',fontsize=11)
    save(fig,'f09-global-continuation')
    (D/'f09-energy-global-data.json').write_text(json.dumps({
        'source':'GC.52–GC.53, exact Gaussian pure-gauge family',
        'ell_metres':ell,'kappa_T':kappa,'alpha':alpha.tolist(),
        'potential_gradient_squared_inverse_metres':gradient.tolist(),
        'curvature_energy_norm_squared_inverse_metres':[0.]*len(alpha),
        'scope':'Exact formula evaluated for the stated parameters; no PDE simulation.'},indent=2)+'\n',encoding='utf8')
if __name__=='__main__':build()
