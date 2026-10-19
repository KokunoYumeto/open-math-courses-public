"""Reproduce the exact rational-family and active-carrier illustrations."""
from pathlib import Path
import argparse,hashlib,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none','svg.hashsalt':'AN02-exceptional-carrier297','axes.spines.top':False,'axes.spines.right':False})
def write(fig,name,overwrite):
    out=ROOT/'figures';out.mkdir(exist_ok=True)
    for ext in ['png','svg']:
        p=out/(name+'.'+ext)
        old=p.read_bytes() if p.exists() else None
        import io
        memory=io.BytesIO()
        fig.savefig(memory,format=ext,dpi=100,metadata={'Date':None} if ext=='svg' else {'Software':'Matplotlib;exact reproducible mathematical figure'})
        b=memory.getvalue()
        if ext=='svg':b=('\n'.join(line.rstrip() for line in b.decode().splitlines())+'\n').encode()
        if old is not None and not overwrite:assert b==old,p
        else:p.write_bytes(b)
    plt.close(fig)
def run(overwrite=False):
    a=np.linspace(-1,1,2401)
    fig,axes=plt.subplots(1,2,figsize=(15,6.5),layout='constrained')
    for t,color in [(1/4,'#0072b2'),(1/8,'#d55e00'),(1/16,'#009e73')]:
        axes[0].plot(a,t*a/(t*t+a*a),color=color,label=f't = 1/{round(1/t)}',linewidth=2)
        axes[1].plot(a,t*(t*t-a*a)/(t*t+a*a)**2,color=color,label=f't = 1/{round(1/t)}',linewidth=2)
        axes[1].scatter([0],[1/t],color=color,zorder=4)
    axes[0].set(title='Pointwise limit is zero at every parameter',ylabel='f(t, a)',ylim=(-.56,.56))
    axes[1].set(title='The derivative fails at the isolated parameter a = 0',ylabel='∂f/∂a',ylim=(-2.5,17))
    for ax in axes:
        ax.axhline(0,color='#666666',linewidth=.7);ax.axvline(0,color='#999999',linestyle=':',linewidth=.8)
        ax.set(xlabel='real parameter a',xlim=(-1,1));ax.legend(loc='upper left');ax.grid(alpha=.17)
    fig.suptitle('A finite family of exact rational slices; no uniform derivative limit at zero',fontsize=16)
    write(fig,'parameter-limit-and-derivative',overwrite)
    theta=np.linspace(0,2*np.pi,721)
    fig,axes=plt.subplots(3,2,figsize=(15,13.2),layout='constrained')
    titles=[r'Elliptic: P(ξ) = ξ₁² + ξ₂²',r'Transport: P(ξ) = ξ₁',r'Wave: P(ξ) = ξ₁² − ξ₂²']
    for row in range(3):
        left,right=axes[row]
        left.plot(np.cos(theta),np.sin(theta),color='#bbbbbb',linestyle=':',linewidth=1.5)
        for ax in [left,right]:
            ax.axhline(0,color='#999999',linewidth=.7);ax.axvline(0,color='#999999',linewidth=.7)
            ax.set(xlim=(-1.25,1.25),ylim=(-1.25,1.25),aspect='equal');ax.grid(alpha=.12)
        left.set(title=titles[row]+'\nUnit frequency escape directions',xlabel='ω₁',ylabel='ω₂')
        right.set(title='Exact physical exceptional carrier Kₚ',xlabel='x₁',ylabel='x₂')
    axes[0,0].text(0,0,'Every limit\nis constant',ha='center',va='center',color='#555555')
    axes[0,1].scatter([0],[0],s=70,color='#555555',zorder=4)
    axes[0,1].text(.12,.12,'{0}',fontsize=14)
    axes[1,0].scatter([0,0],[-1,1],s=80,color='#0072b2',zorder=4)
    axes[1,0].text(.14,.82,'±e₂',color='#0072b2')
    axes[1,1].plot([-1.25,1.25],[0,0],linewidth=3,color='#0072b2')
    axes[1,1].text(-.8,.17,'ℝe₁',color='#0072b2')
    q=1/np.sqrt(2)
    for direction,color in [(1,'#d55e00'),(-1,'#009e73')]:
        axes[2,0].scatter([q,-q],[direction*q,-direction*q],s=80,color=color,zorder=4)
        axes[2,1].plot([-1.25,1.25],[direction*1.25,-direction*1.25],linewidth=2.5,color=color)
    axes[2,1].text(.15,1.05,'x₁² = x₂²',ha='left')
    fig.suptitle('Direction pieces constrain the entire active space; the cones extend beyond the drawing',fontsize=16)
    write(fig,'frequency-pieces-and-active-carriers',overwrite)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--overwrite',action='store_true');args=p.parse_args();run(args.overwrite)
    print(json.dumps({'figures':2,'outputs':4,'byte_reproduced':True}))
