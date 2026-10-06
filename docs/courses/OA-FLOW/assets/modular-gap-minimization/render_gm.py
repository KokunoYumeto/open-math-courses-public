"""Exact finite example and explicitly schematic proof mechanisms. CC0-1.0."""
from pathlib import Path
from fractions import Fraction as F
import json,shutil
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
D=Path(__file__).resolve().parent; O=D/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'oa-flow-gm-original-20261004','axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white'})
blue='#1d5c8c';red='#ad414a';green='#19715a';gray='#516274';light='#edf3f8'
h=[F(4,5),F(1,5)];l=h[::-1];R=F(1);delta=F(1,10)
thresholds=[j*delta for j in range(10)]
P=[[int(x>r) for x in h] for r in thresholds];Q=[[int(x>r) for x in l] for r in thresholds]
z=[[a-b for a,b in zip(p,q)] for p,q in zip(P,Q)]
def fd(s,i):return sum((zj[i]*(max(s-r,F(0))-max(s-r-delta,F(0))) for r,zj in zip(thresholds,z)),F(0))
cost=sum(abs(x-y) for x,y in zip(h,l));f_cost=sum(fd(x,i)-fd(y,i) for i,(x,y) in enumerate(zip(h,l)))
assert cost==f_cost==F(6,5)
data={'scope':'Panels A/B exact commutative C^2 example; C/D/E schematic proof mechanisms, not measured data','h':[str(x) for x in h],'l':[str(x) for x in l],'a':'1/4','b':'4','modular_spectrum':['1'],'gap':['1/16','16'],'trace':'sum of the two coordinates; tau(1)=2','mesh':str(delta),'R':str(R),'thresholds':[str(x) for x in thresholds],'P':P,'Q':Q,'z':z,'trace_cost':str(cost),'trace_cut_cost':str(f_cost),'F_at_h':[str(fd(x,i)) for i,x in enumerate(h)],'F_at_l':[str(fd(x,i)) for i,x in enumerate(l)],'discrete_group':'Q with discrete topology','represented_rational_coordinates':['-1','-1/2','0','1/2','1'],'full_operator_domain':'xi_r in D(Delta_phi) and sum_r ||Delta_phi xi_r||^2 < infinity; all rational coordinates'}
(O/'gm-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
fig=plt.figure(figsize=(15,12),dpi=200)
gs=fig.add_gridspec(3,2,height_ratios=[1,1.05,1.2],hspace=.48,wspace=.25,left=.08,right=.96,top=.91,bottom=.045)
fig.suptitle('A modular gap forces the commuting pair to attain the minimum',fontsize=21,y=.975,color='#172c42')
fig.text(.5,.94,'GM-1 central cuts  →  GM-3 compact averaging  →  GM-5/6 discrete extension and return',ha='center',fontsize=13,color=gray)
ax=fig.add_subplot(gs[0,0]);idx=np.array([0,1]);width=.25
ax.bar(idx-width/2,[float(x) for x in h],width,color=blue,label=r'$h=(4/5,1/5)$')
ax.bar(idx+width/2,[float(x) for x in l],width,color=red,label=r'$l=(1/5,4/5)$')
ax.axhline(.5,color=gray,ls='--',lw=1);ax.text(1.43,.51,r'$r=1/2$',ha='right',color=gray)
ax.set_xticks(idx,['coordinate 1','coordinate 2']);ax.set_ylim(0,1.04);ax.set_ylabel('positive trace density')
ax.set_title(r'A. Exact central cut in $M=\mathbb{C}^2$',loc='left',fontsize=15,pad=12)
ax.legend(loc='upper center',ncols=2,frameon=False,fontsize=11)
ax.text(.5,-.27,r'$p_r=(1,0),\ q_r=(0,1),\ z_r=(1,-1)$'+'\n'+r'$p_rMq_r=0;\quad\tau(|h-l|)=6/5$',transform=ax.transAxes,ha='center',fontsize=12)
ax=fig.add_subplot(gs[0,1]);samples=np.linspace(-.05,1.05,301)
for i,color in enumerate([blue,red]):
    vals=[float(fd(F(str(s)),i)) for s in samples]
    ax.plot(samples,vals,lw=2.8,color=color,label=f'coordinate {i+1}')
ax.axvline(.2,color=gray,ls=':',lw=1);ax.axvline(.8,color=gray,ls=':',lw=1)
ax.set_xlim(-.05,1.05);ax.set_ylim(-.7,.7);ax.set_ylabel(r'central value $F_\delta(s)$')
ax.text(.96,.035,r'scalar input $s$',transform=ax.transAxes,ha='right',fontsize=11,color=gray)
ax.set_title(r'B. Exact contraction slopes; mesh $\delta=1/10$',loc='left',fontsize=15,pad=12)
ax.legend(loc='upper left',frameon=False,fontsize=11)
ax.text(.5,-.27,r'$z_r=(1,-1)$ for $1/5\leq r<4/5$'+'\n'+r'$\tau(F_\delta(h)-F_\delta(l))=6/5$',transform=ax.transAxes,ha='center',fontsize=12)
def canvas(ax,title):ax.set_axis_off();ax.set_title(title,loc='left',fontsize=15,pad=14);ax.set_xlim(0,1);ax.set_ylim(0,1)
def box(ax,x,y,w,h,text,color=blue,size=12):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012,rounding_size=.02',ec=color,fc=light,lw=1.2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,color='#162f43')
def arrow(ax,p,q,text='',color=gray):
    ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=13,lw=1.3,color=color))
    if text:ax.text((p[0]+q[0])/2,(p[1]+q[1])/2+.025,text,ha='center',va='bottom',color=color,fontsize=10.5)
ax=fig.add_subplot(gs[1,0]);canvas(ax,'C. Trace estimate — general mechanism')
box(ax,.02,.70,.94,.20,r'$A_t=B+t(A-B),\quad Q^\prime=p$'+'\n'+r'$\|p(A_t)\|\leq1+\eta$ by central spectral steps')
arrow(ax,(.49,.69),(.49,.55))
box(ax,.02,.34,.94,.20,r'$\frac{d}{dt}\tau(Q(A_t))=\tau(p(A_t)(A-B))$'+'\n'+r'$|\tau(p(A_t)(A-B))|\leq(1+\eta)\tau(|A-B|)$',green)
arrow(ax,(.49,.33),(.49,.19))
ax.text(.5,.10,r'$|\tau(F_\delta(A)-F_\delta(B))|\leq\tau(|A-B|)$',ha='center',fontsize=13,color=green)
ax.text(.5,-.08,'Scalar smoothing and polynomial limits in trace.\nThis is a trace bound; no operator Lipschitz claim.',ha='center',fontsize=11,color=gray)
ax=fig.add_subplot(gs[1,1]);canvas(ax,'D. Small inner period — approximation')
box(ax,.02,.70,.94,.20,r'$h=e^{a_\theta/t_0},\quad\omega=c\phi(h^{-1}\,\cdot)$'+'\n'+r'$\sigma_{t_0}^{\omega}=\mathrm{id},\quad B=M_\omega$')
arrow(ax,(.49,.69),(.49,.55))
box(ax,.02,.34,.94,.20,r'$y=E_\omega(u),\quad y=v|y|,\quad v\in\mathcal{U}(B)$'+'\n'+r'$\|u-v\|_\phi^\#\leq\delta^\prime+\sqrt{2\delta^\prime}\longrightarrow0$',green)
arrow(ax,(.49,.33),(.49,.19))
ax.text(.5,.10,r'$\phi E_\omega=\phi,\quad\psi E_\omega=\psi$',ha='center',fontsize=13,color=green)
ax.text(.5,-.08,'The restricted finite trace has bounded commuting densities.\nApply the central-cut minimum on $B$, then pass to $u$.',ha='center',fontsize=11,color=gray)
ax=fig.add_subplot(gs[2,:]);canvas(ax,'E. Countable discrete extension and exact return — schematic')
box(ax,.02,.69,.28,.21,r'original $M$'+'\n'+r'$\phi,\ \psi=\phi(k\,\cdot)$')
box(ax,.53,.69,.43,.21,r'$N=\{\pi(M),L_s:s\in\mathbb{Q}\}^{\prime\prime}$'+'\n'+r'$\widetilde\phi=\phi\pi^{-1}E,\quad E(X)=\pi(X_{0,0})$')
arrow(ax,(.31,.84),(.52,.84),r'faithful normal $\pi$')
arrow(ax,(.52,.72),(.31,.72),r'$\pi^{-1}E$')
ax.text(.5,.57,r'$(\pi(x)\xi)_r=\sigma_{-r}^{\phi}(x)\xi_r,\quad(L_s\xi)_r=\xi_{r-s}$',ha='center',fontsize=13)
box(ax,.02,.22,.46,.32,r'$H_{\widetilde\phi}=\ell^2(\mathbb{Q},H_\phi)$'+'\n'+r'$(T\xi)_r=\Delta_\phi^{-ir}S\xi_{-r}$'+'\n'+r'$\Delta_{\widetilde\phi}=\bigoplus_{r\in\mathbb{Q}}\Delta_\phi$')
box(ax,.54,.22,.42,.32,r'$\sigma_g^{\widetilde\phi}=\mathrm{Ad}(L_g),\quad g\in\mathbb{Q}$'+'\n'+r'$\operatorname{Sp}\Delta_{\widetilde\phi}=\operatorname{Sp}\Delta_\phi$'+'\n'+r'$\|\widetilde\phi^{\pi(u)}-\widetilde\psi\|=\|\phi^u-\psi\|$',green)
arrow(ax,(.49,.35),(.53,.35))
ax.text(.5,.10,r'Full domain: $\xi_r\in D(\Delta_\phi)$ and $\sum_r\|\Delta_\phi\xi_r\|^2<\infty$.',ha='center',fontsize=12)
ax.text(.5,.01,'All rational coordinates are present. Dense inner periods hold in $N$; the exact norm returns the minimum to $M$.',ha='center',fontsize=11,color=gray)
for suffix in ['png','svg']:
    metadata={'Software':'Original OA-FLOW GM mathematical figure'} if suffix=='png' else {'Date':None,'Creator':'Original OA-FLOW GM mathematical figure'}
    fig.savefig(O/f'gm-mechanisms.{suffix}',dpi=200,metadata=metadata)
plt.close(fig)
font=Path(matplotlib.get_data_path())/'fonts/ttf/LICENSE_DEJAVU';shutil.copyfile(font,O/'DEJAVU-LICENSE.txt')
print(json.dumps({'native_png':[3000,2400],'exact_trace_cost':str(cost),'asset_names':[p.name for p in sorted(O.iterdir())]},indent=2))
