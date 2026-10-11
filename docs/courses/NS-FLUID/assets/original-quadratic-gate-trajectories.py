"""Samples of three exact original gate solutions; no ODE approximation."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
OUT=Path(__file__).resolve().parent
alpha=3/5;A=2;z0=3/2
t_p=np.linspace(-4,4,801);xp=A/np.cosh(alpha*A*t_p);yp=A*np.tanh(alpha*A*t_p)
t_a=np.linspace(-2,6,801);xa=A*np.tanh(alpha*A*(2-t_a));ya=A/np.cosh(alpha*A*(2-t_a))
t_r=np.linspace(0,2*np.pi/(alpha*z0),801);xr=A*np.cos(alpha*z0*t_r);yr=A*np.sin(alpha*z0*t_r)
rows=[
 ('Pump',t_p,xp,yp,r"$x'=-\alpha xy,\quad y'=\alpha x^2$",
  r'$x(0)=2,\ y(0)=0;\quad -4\leq t\leq4$'),
 ('Amplifier',t_a,xa,ya,r"$x'=-\alpha y^2,\quad y'=\alpha xy$",
  r'$x=2\tanh(1.2(2-t)),\ y=2\,\mathrm{sech}(1.2(2-t))$'),
 ('Rotor',t_r,xr,yr,r"$x'=-\alpha yz,\quad y'=\alpha xz,\quad z'=0$",
  r'$x(0)=2,\ y(0)=0,\ z=3/2;\quad 0\leq t\leq20\pi/9$')
]
fig,axes=plt.subplots(1,3,figsize=(18,10),facecolor='white')
fig.subplots_adjust(left=.045,right=.98,bottom=.34,top=.80,wspace=.24)
fig.suptitle('Three original quadratic gates on their actual energy circles',fontsize=24,y=.96)
fig.text(.5,.89,r'$\alpha=3/5,\quad x^2+y^2=4;\qquad \mathrm{rotor:}\ x^2+y^2+z^2=25/4$',ha='center',fontsize=20)
angle=np.linspace(0,2*np.pi,401)
for ax,(name,t,x,y,eq,caption) in zip(axes,rows):
    ax.plot(2*np.cos(angle),2*np.sin(angle),'--',color='#bac2c5',lw=1.2)
    ax.plot(x,y,color='#126471',lw=3)
    for j in [245,390,520]:
        ax.annotate('',xy=(x[j+12],y[j+12]),xytext=(x[j],y[j]),
                    arrowprops=dict(arrowstyle='-|>',lw=2,color='#b85b19',mutation_scale=17))
    ax.axhline(0,color='#dedede',lw=.8);ax.axvline(0,color='#dedede',lw=.8)
    ax.set_aspect('equal');ax.set_xlim(-2.35,2.35);ax.set_ylim(-2.35,2.35)
    ax.set_xticks([-2,-1,0,1,2]);ax.set_yticks([-2,-1,0,1,2])
    ax.set_xlabel('Original x',fontsize=13);ax.set_ylabel('Original y',fontsize=13)
    ax.set_title(name,fontsize=20,pad=12)
    ax.text(.5,-.20,eq,transform=ax.transAxes,ha='center',fontsize=14)
    ax.text(.5,-.30,caption,transform=ax.transAxes,ha='center',fontsize=10.5)
fig.text(.5,.12,'QG3–QG17 give the complete solutions, exceptional states, thresholds and forced identities. Arrows show increasing original time.',ha='center',fontsize=13)
fig.text(.5,.078,'Human source: Terence Tao, arXiv:1402.0290v3, original navier-blowup.tex1050–1220. Curves sample exact formulas.',ha='center',fontsize=12)
fig.text(.5,.04,'The original radius, coupling and rotor drive are retained. These are separate gates, not the later five-mode dynamics.',ha='center',fontsize=12)
for ext in ['png','svg']:fig.savefig(OUT/f'original-quadratic-gate-trajectories.{ext}',dpi=150)
plt.close(fig)
data=dict(alpha=alpha,amplitude=A,rotor_z=z0,
 equations='QG4, QG8, QG12; exact formulas sampled in original time',
 samples=[dict(gate=name,t=t.tolist(),x=x.tolist(),y=y.tolist()) for name,t,x,y,_,_ in rows])
(OUT/'original-quadratic-gate-trajectories-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
