"""Euler ray rotation for both signs, with exact finite contours; CC0.
GPT-6 Astra (OpenAI). AN01-U017 Lemma H1a, (R1)-(R4).
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
if out.name=='work':out=out/'advanced-U187-20261022/new'
out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':12,'svg.hashsalt':'AN01-euler-rays-and-arc-estimates'})
fig,axes=plt.subplots(1,2,figsize=(12,6.4),layout='constrained')
for ax,sign in zip(axes,[1,-1]):
    theta=sign*np.pi/3
    r,R=.5,3
    angles=np.linspace(0,theta,160)
    for radius,color,name in [(r,'#a44425',r'$r=1/2$'),(R,'#18658f',r'$R=3$')]:
        ax.plot(radius*np.cos(angles),radius*np.sin(angles),color=color,lw=2.8)
    for angle in [0,theta]:
        a=np.array([np.cos(angle),np.sin(angle)])
        ax.plot([r*a[0],R*a[0]],[r*a[1],R*a[1]],color='#333333',lw=1.7)
        ax.annotate('',xy=2.1*a,xytext=1.4*a,arrowprops={'arrowstyle':'->','color':'#333333','lw':2})
    ax.annotate(r'$r$',xy=(r*np.cos(theta/2),r*np.sin(theta/2)),
                xytext=(-25,sign*12),textcoords='offset points',color='#a44425')
    ax.annotate(r'$R$',xy=(R*np.cos(theta/2),R*np.sin(theta/2)),
                xytext=(12,sign*10),textcoords='offset points',color='#18658f')
    ax.text(1.1,sign*.36,r'$\theta='+('' if sign==1 else '-')+r'\pi/3$',fontsize=13)
    ax.scatter([0],[0],s=18,color='#333333')
    ax.text(-.16,-.24,'0')
    ax.axhline(0,color='#777777',lw=.6,zorder=0);ax.axvline(0,color='#777777',lw=.6,zorder=0)
    ax.set(xlim=(-.35,3.55),ylim=(-.45,3.2) if sign==1 else (-3.2,.45),
           xlabel=r'$\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z$',
           title='Upper sector' if sign==1 else 'Lower sector',aspect='equal')
    ax.set_xticks([0,1,2,3]);ax.grid(alpha=.14)
fig.suptitle('Euler ray integrals: both radial paths are oriented outward',fontsize=15)
fig.supxlabel(r'Inner arc $\leq |\theta|e^{|b||\theta|}r^s$; outer arc $\leq |\theta|e^{|b||\theta|}R^s e^{-R\cos|\theta|}$'+'\n'+r'$s=\operatorname{Re}\mu>0,\quad b=\operatorname{Im}\mu$',fontsize=12)
for ext in ['png','svg']:
    p=out/('euler-rays-and-arc-estimates.'+ext)
    fig.savefig(p,dpi=160,metadata={'Date':None} if ext=='svg' else {})
    if ext=='svg':p.write_text('\n'.join(line.rstrip() for line in p.read_text().splitlines())+'\n',encoding='utf-8',newline='\n')
if out.name=='new':(out/'euler-rays-and-arc-estimates.py').write_bytes(Path(__file__).read_bytes())
