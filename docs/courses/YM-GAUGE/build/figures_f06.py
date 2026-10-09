"""Exact Hopf overlap and latitude transport, YM-F06 F6.50--F6.62."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def build():
    out=Path(__file__).resolve().parents[1]/'figures';out.mkdir(exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,
                         'svg.fonttype':'path','svg.hashsalt':'YM-F06-Hopf-v1'})
    fig=plt.figure(figsize=(12,10),facecolor='#fffef9')
    fig.text(.06,.95,'Two local frames; one transported vector',fontsize=22,weight='bold',color='#163e4b')
    fig.text(.06,.91,r'Equator: $w=e^{i\phi}$, $v=1/w=e^{-i\phi}$, $s_S=s_N e^{-i\phi}$',
             fontsize=16,color='#163e4b')
    ts=np.linspace(0,2*np.pi,1000);angle=np.pi/3
    for j,sign in enumerate([1,-1]):
        ax=fig.add_axes([.10+.45*j,.57,.32,.29],aspect='equal')
        ax.plot(np.cos(ts),sign*np.sin(ts),color='#316e8c',lw=2)
        ax.axhline(0,color='#bec8c8',lw=.8);ax.axvline(0,color='#bec8c8',lw=.8)
        for th in [np.pi/6,7*np.pi/6]:
            ax.annotate('',xy=(np.cos(th+.2),sign*np.sin(th+.2)),
                        xytext=(np.cos(th-.1),sign*np.sin(th-.1)),
                        arrowprops={'arrowstyle':'->','color':'#316e8c','lw':2})
        ax.scatter([np.cos(angle)],[sign*np.sin(angle)],color='#b84923',s=65,zorder=5)
        ax.plot([0,np.cos(angle)],[0,sign*np.sin(angle)],color='#b84923',lw=1.2)
        ax.set(xlim=(-1.35,1.35),ylim=(-1.35,1.35),xticks=[-1,0,1],yticks=[-1,0,1])
        ax.set_title('Northern coordinate w' if j==0 else 'Southern coordinate v',fontsize=14,pad=10)
        ax.set_xlabel('Real part');ax.set_ylabel('Imaginary part')
        for spine in ax.spines.values():spine.set_visible(False)
    fig.text(.06,.50,r'Latitude holonomy: $H(\theta)=\exp[-i\pi(1-\cos\theta)]$',
             fontsize=17,color='#163e4b')
    theta=np.linspace(0,np.pi,1001);phase=np.pi*(1-np.cos(theta))
    ax=fig.add_axes([.12,.18,.80,.26])
    ax.plot(theta,np.cos(phase),color='#216c97',lw=2.5,label='Real part of H')
    ax.plot(theta,-np.sin(phase),color='#b84923',lw=2.5,ls='--',label='Imaginary part of H')
    ax.set(xlim=(0,np.pi),ylim=(-1.18,1.18),xticks=[0,np.pi/2,np.pi],
           xticklabels=['0 (north pole)',r'$\pi/2$ (equator)',r'$\pi$ (south pole)'],
           yticks=[-1,0,1])
    ax.grid(alpha=.3);ax.set_ylabel('Phase component\n(dimensionless)',fontsize=12)
    ax.set_xlabel(r'Sphere polar angle $\theta$ (radians)',labelpad=10)
    ax.scatter([0,np.pi/2,np.pi],[1,-1,1],color='#216c97',s=35,zorder=5)
    ax.legend(loc='upper center',bbox_to_anchor=(.5,-.29),ncol=2,frameon=False,fontsize=13)
    fig.text(.06,.04,'The marked equator coordinates describe the same base point at phi = pi/3.',fontsize=12)
    fig.text(.06,.013,'Exact maps, signs, endpoint values and proofs: YM-F06, (F6.50)–(F6.62).',fontsize=12)
    fig.savefig(out/'f06-hopf-transport.svg',metadata={'Date':None,'Creator':'YM-GAUGE CC0 figure source'})
    fig.savefig(out/'f06-hopf-transport.png',dpi=150,metadata={'Software':'YM-GAUGE CC0 figure source'})
    plt.close(fig)
    p=out/'f06-hopf-transport.svg';text=p.read_text(encoding='utf-8')
    start=text.index('<svg ');end=text.index('>',start)
    text=text[:end]+' role="img" aria-labelledby="f06-title f06-desc"'+text[end:]
    end=text.index('>',start)
    text=text[:end+1]+'''
<title id="f06-title">Hopf bundle overlap and exact latitude transport</title>
<desc id="f06-desc">On the equator the northern coordinate w travels counterclockwise while the southern coordinate v equals one over w and travels clockwise. At phi equal to pi over three, the marked coordinates are one half plus or minus i square root of three over two. The southern unit frame equals the northern frame times exp minus i phi. Below, the real and imaginary parts of exp minus i pi times one minus cosine theta are plotted without discarding either part. Holonomy is one at either pole and minus one at the equator. The polar angle runs from zero to pi radians. The pole values agree with constant-loop transport.</desc>'''+text[end+1:]
    p.write_text(text,encoding='utf-8')

if __name__=='__main__':build()
