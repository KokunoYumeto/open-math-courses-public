"""Exact paired real-translation model; independently drawn, deterministic assets."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
E=Path(__file__).resolve().parent;O=E/'assets';O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.hashsalt':'L113-exact-paired-displacement-v1','axes.spines.top':False,'axes.spines.right':False,'mathtext.fontset':'dejavusans'})
blue='#245a89';red='#a83c4c';green='#286953';gray='#d9dde1'
fig=plt.figure(figsize=(15,10),dpi=200)
gs=fig.add_gridspec(2,2,left=.07,right=.975,top=.845,bottom=.13,hspace=.5,wspace=.24,height_ratios=[1,1])
fig.text(.07,.955,'Norm discontinuity and local displacement',fontsize=25,weight='bold')
fig.text(.07,.912,r'Exact real-line models: $(\lambda_t\xi)(r)=\xi(r-t)$ and $T_t(r)=r+t$',fontsize=16)
a=fig.add_subplot(gs[0,0]);b=fig.add_subplot(gs[0,1]);c=fig.add_subplot(gs[1,0]);d=fig.add_subplot(gs[1,1])
a.set_title(r'1. Half-line projections in $B(L^2(\mathbb{R}))$',loc='left',fontsize=16,pad=18)
a.step([-1,0,2],[0,1,1],where='post',color=blue,lw=3,label=r'$q(r)=1_{[0,\infty)}(r)$')
a.step([-1,.5,2],[0,1,1],where='post',color=red,lw=3,linestyle='--',label=r'$\alpha_{1/2}(q)(r)=1_{[1/2,\infty)}(r)$')
a.axvspan(0,.5,color='#e5bd7b',alpha=.48)
a.text(.25,.53,'difference\nmagnitude 1',ha='center',va='center',fontsize=13)
a.set_xlim(-1,2);a.set_ylim(-.09,1.35);a.set_yticks([0,1]);a.set_xticks([-1,0,.5,1,2],['−1','0','1/2','1','2']);a.set_xlabel('r');a.legend(loc='upper right',fontsize=11,framealpha=.95)
b.set_title(r'2. A cutoff in $C_0(\mathbb{R})$',loc='left',fontsize=16,pad=18)
b.axvspan(.65,1.35,color='#cfe3d9',alpha=.65,label=r'All translated supports, $t\in U$')
b.plot([-.6,-.25,0,.25,1.6],[0,0,1,0,0],color=blue,lw=3,label=r'$f(r)=\max(1-4|r|,0)$')
b.plot([-.6,.75,1,1.25,1.6],[0,0,1,0,0],color=red,lw=3,linestyle='--',label=r'$\alpha_1(f)(r)=f(r-1)$')
b.set_xlim(-.6,1.6);b.set_ylim(-.09,1.85);b.set_xticks([-.25,0,.25,.75,1,1.25],['−1/4','0','1/4','3/4','1','5/4']);b.set_yticks([0,1]);b.set_xlabel('r');b.legend(loc='upper left',fontsize=10.5,framealpha=.95)
c.set_title('3. The exact norm obstruction',loc='left',fontsize=16,pad=18)
c.plot([-1.1,-.015],[1,1],color=red,lw=3);c.plot([.015,1.1],[1,1],color=red,lw=3)
c.scatter([0],[1],s=85,edgecolor=red,facecolor='white',lw=2,zorder=4);c.scatter([0],[0],s=85,color=blue,zorder=4)
c.set_xlim(-1.1,1.1);c.set_ylim(-.15,1.4);c.set_xticks([-1,0,1]);c.set_yticks([0,1]);c.set_xlabel('t')
c.text(.04,.55,r'$\|\alpha_t(q)-q\|=1\quad(t\ne0)$',transform=c.transAxes,fontsize=16)
c.text(.04,.34,'A normalized indicator of the interval between 0 and t\nattains norm 1; the whole orbit is strong* continuous.',transform=c.transAxes,fontsize=12)
d.set_title('4. One neighborhood works for every translate',loc='left',fontsize=16,pad=18)
rows=[(4,-.5,.5,gray,r'$O_0=(-1/2,1/2)$'),(3,.5,1.5,gray,r'$O_1=(1/2,3/2)$'),(2,-1/3,1/3,blue,r'$V=(-1/3,1/3)$'),(1,-.25,.25,blue,r'$\operatorname{supp} f=[-1/4,1/4]$'),(0,.65,1.35,green,r'$\bigcup_{t\in U}\operatorname{supp}\alpha_t(f)=(13/20,27/20)$')]
for y,l,r,col,label in rows:
 d.plot([l,r],[y,y],lw=7,color=col,solid_capstyle='butt');d.scatter([l,r],[y,y],s=45,edgecolor=col,facecolor=col if y==1 else 'white',lw=1.5,zorder=3);d.text(-.62,y+.23,label,fontsize=11)
d.set_xlim(-.65,1.65);d.set_ylim(-.4,4.7);d.set_xticks([-.5,0,.5,1,1.5],['−1/2','0','1/2','1','3/2']);d.set_yticks([]);d.set_xlabel('r')
fig.text(.07,.062,r'$U=(9/10,11/10)$: $T_t(V)\subset(17/30,43/30)\subset O_1$, so $\alpha_t(p)p=0$ for every $t\in U$.',fontsize=16)
fig.text(.07,.026,'The panels are exact models on R. The proved displacement and density statements use arbitrary LCH groups; no countable base is assumed.',fontsize=11.5)
fig.savefig(O/'paired-displacement.png',dpi=200,metadata={'Software':'L113 deterministic original figure'})
fig.savefig(O/'paired-displacement.svg',metadata={'Date':None,'Creator':'L113 deterministic original figure'})
p=O/'paired-displacement.svg';p.write_text('\n'.join(l.rstrip() for l in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8',newline='\n')
plt.close(fig)
data={'native_dimensions':[3000,2000],'model_group':'R, additive; Lebesgue left Haar','lambda':'(lambda_t xi)(r)=xi(r-t)','T':'T_t(r)=r+t','half_line':{'q':'1_[0,infinity)','plotted_t':'1/2','difference_interval':'[0,1/2)','norm_for_every_nonzero_t':'1','norm_at_zero':'0'},'cutoff':{'f':'max(1-4|r|,0)','f_support_closed':['-1/4','1/4'],'p_positive_set_open':['-1/4','1/4'],'s':'1','U_open':['9/10','11/10'],'V_open':['-1/3','1/3'],'O0_open':['-1/2','1/2'],'O1_open':['1/2','3/2'],'all_TtV_union_open':['17/30','43/30'],'all_translated_closed_f_support_union_open':['13/20','27/20'],'plotted_t':'1','plotted_translated_f_support_closed':['3/4','5/4'],'conclusion':'alpha_t(p)p=0 for every t in U'},'geometry':'Panel 4 colored bars display coordinate intervals, not membership of their endpoints; the exact open/closed conventions are in labels and this data.','drawing':'Step and triangular functions are exact piecewise-linear coordinate plots; no sampled convergence claim.','scope':'Illustrative R models; theorem arbitrary LCH G and arbitrary normal M/H.','proof_locators':['D28','D29','LD6','D7-D13'],'terms':'Original diagram and code CC0-1.0 to the extent rights held; DejaVu font terms separately retained.'}
(O/'paired-displacement-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
