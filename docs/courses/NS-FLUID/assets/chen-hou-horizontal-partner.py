"""Exact physical branch geometry and the full concentrating middle measure."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.labelsize':12,'axes.titlesize':14})
a=1.3;t=.5;r=np.sqrt(a*a+t*t);hm=np.sqrt(r*r-2*t*r);hp=np.sqrt(r*r+2*t*r);b=np.sqrt(a*a-3*t*t)
def delta(x):
    return ((x+a)**2-t*t)/(2*((x+a)**2+t*t)**2)-((x-a)**2-t*t)/(2*((x-a)**2+t*t)**2)
def partner(x):return np.sqrt(r*r+4*t*t*r*r/(x*x-r*r))
fig=plt.figure(figsize=(14,10),layout='constrained');gs=fig.add_gridspec(2,2,height_ratios=[1,1])
ax=fig.add_subplot(gs[0,0]);bx=fig.add_subplot(gs[0,1]);cx=fig.add_subplot(gs[1,:])
xx=np.linspace(0,4*a,1800);ax.plot(xx,delta(xx),color='#182c43',lw=1.8)
for lo,hi,col,label in [(0,hm,'#b35549','Inner negative mass'),(hm,b,'#e1a59d','Its positive partner'),(b,r,'#d8ad38','Unmatched positive mass'),(r,hp,'#82b6d1','Outer positive partner'),(hp,4*a,'#3478a1','Outer negative mass')]:
    v=np.linspace(lo,hi,300);ax.fill_between(v,0,delta(v),color=col,alpha=.75,label=label)
ax.axhline(0,color='#46566b',lw=.8);ax.grid(alpha=.2)
ax.set_xlim(0,4*a);ax.set_xlabel(r'Original coordinate $s$');ax.set_ylabel(r'Full difference $\Delta_a(s,t)$')
ax.set_title('Signed kernel and all pairing intervals · KX2–KX7')
ax.legend(loc='upper right',fontsize=9)
ax.text(2.15,.48,r'Unmatched mass $a/(a^2+t^2)$',fontsize=11)
for lo,hi,col,label in [(0,hm,'#a84b40',r'$D_1\longrightarrow(h_-,b)$'),(hp,4*a,'#246e9c',r'$D_2\longrightarrow(r,h_+)$')]:
    ss=np.linspace(lo+1e-6,hi-1e-6,650);ts=partner(ss)
    bx.plot(ss,ts,color=col,lw=2.2,label=label)
    bx.plot(ts,ss,color=col,ls=':',lw=1.5)
bx.plot([0,4*a],[0,4*a],color='#8995a5',ls='--',label=r'$T=s$')
bx.axvspan(b,r,color='#d8ad38',alpha=.25,label=r'No distinct real partner: $b<s<r$')
bx.set_xlim(0,4*a);bx.set_ylim(0,4*a);bx.set_xlabel(r'Original input $s$');bx.set_ylabel(r'Original partner $T_{a,t}(s)$')
bx.set_title('Both bijections and their dotted inverses · KX3–KX6')
bx.grid(alpha=.2);bx.legend(loc='upper right',fontsize=9)
heights=np.linspace(0,2.8,1400)
for d,col,lab in [(a/2,'#867153',r'$M=a+13/20$'),(a/10,'#317b94',r'$M=a+13/100$'),(a/50,'#905497',r'$M=a+13/500$')]:
    mass=.5*np.arctan(heights/d)-.5*np.arctan(heights/(2*a+d))+.5*np.arctan(heights/(2*a))
    cx.plot(heights,mass,color=col,lw=2,label=lab)
cx.axhline(np.pi/4,color='#46566b',ls='--',label=r'Full positive-height mass $\pi/4$')
cx.set_ylim(0,.83);cx.set_xlim(0,2.8);cx.grid(alpha=.2)
cx.set_xlabel(r'Original upper height $T$');cx.set_ylabel(r'Accumulated mass $\int_0^T \rho_{\rm mid}(a,M,t)\,dt$')
cx.set_title('Finite middle mass concentrates at height zero · KX11–KX14')
cx.legend(loc='lower right',fontsize=11)
fig.suptitle(r'Original horizontal K2 transport · shift $a=13/10$'+'\n'+r'Upper panels: actual height $t=1/2$; every original kernel half retained',fontsize=17)
for ext in ['png','svg']:fig.savefig(R/('chen-hou-horizontal-partner.'+ext),dpi=180)
(R/'chen-hou-horizontal-partner.json').write_text(json.dumps(dict(parameters={'a':'13/10','t':'1/2','M_minus_a':['13/20','13/100','13/500']},proof='KX1–KX15',status='Numerical rendering of exact original-coordinate maps and complete mass primitives',visual_inspection='pending'),indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(dict(figure='chen-hou-horizontal-partner.png',original_shift='13/10')))
