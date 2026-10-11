"""Original CC0 diagrams for SGD.6--SGD.16; no selected flow is simulated."""
from pathlib import Path
import os, io
HERE = Path(__file__).resolve().parent
os.environ.setdefault('MPLCONFIGDIR', str(HERE/'font-cache'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                     'svg.fonttype':'none','svg.hashsalt':'NCG-SGD-20261011',
                     'axes.spines.top':False,'axes.spines.right':False})
BLUE='#175c9b'; ORANGE='#b34d17'; GREEN='#287b4f'

def figures():
    fig,ax=plt.subplots(1,2,figsize=(13,5.6),gridspec_kw={'width_ratios':[1,1.2]})
    t=np.linspace(0,np.pi,401)
    ax[0].plot(np.cos(t),np.sin(t),color=BLUE,lw=4)
    ax[0].plot(np.cos(t),-np.sin(t),color=ORANGE,lw=4)
    ax[0].scatter([1,-1],[0,0],s=70,color=BLUE,zorder=5)
    ax[0].text(0,.63,'J+: regular sources',ha='center',color=BLUE)
    ax[0].text(0,.43,'source fibre = F₂',ha='center',color=BLUE)
    ax[0].text(0,.21,'Endpoints: isotropy F₂',ha='center',fontsize=10)
    ax[0].text(0,.02,'e− = 0',ha='center',fontsize=10)
    ax[0].text(0,-.38,'J− interior',ha='center',color=ORANGE)
    ax[0].text(0,-.58,'one unit per source',ha='center',color=ORANGE)
    ax[0].text(0,-.80,'e− = 1',ha='center',color=ORANGE)
    ax[0].text(1.13,0,'0',va='center');ax[0].text(-1.15,0,'∞',va='center',ha='right')
    ax[0].text(0,1.27,'x ∈ R ∪ {∞}; angle = 2 arctan(x)',ha='center',fontsize=10)
    ax[0].set(xlim=(-1.6,1.6),ylim=(-1.4,1.6),aspect='equal')
    ax[0].axis('off');ax[0].set_title('Actual germ source counts',pad=15)
    n=np.arange(0,41);c=np.sqrt(3)/2
    ax[1].semilogy(n,c**n,color=GREEN,lw=2.5,label='‖pⁿ − e−‖ ≤ (√3 / 2)ⁿ')
    ax[1].axhline(1,color=ORANGE,ls='--',lw=1.5,label='Whole reduced norm: ‖pⁿ‖ = 1')
    ax[1].set(xlabel='n',ylabel='proved bound / norm',xlim=(0,40),ylim=(.002,1.7))
    ax[1].grid(alpha=.2,which='both');ax[1].legend(loc='upper right',fontsize=10)
    ax[1].set_title('Norm convergence retains every source')
    fig.suptitle('SGD.6–SGD.11: the reduced completion splits the two arcs',fontsize=15)
    fig.text(.5,.03,'C*r(H) ≅ (C(J+) ⋊r F2) ⊕ C(J−)       e− = lim pⁿ = (0, 1)',ha='center',fontsize=12)
    fig.tight_layout(rect=(0,.09,1,.92))
    yield 'split-germ-reduced-algebra',fig

    fig,ax=plt.subplots(1,2,figsize=(13,5.8),gridspec_kw={'width_ratios':[1.2,1]})
    t=np.linspace(0,1,801);S=np.zeros_like(t)
    a=t-.25;b=.75-t;mask=(a>0)&(b>0)
    ea=np.exp(-1/a[mask]);eb=np.exp(-1/b[mask]);S[mask]=ea/(ea+eb);S[t>=.75]=1
    colors=[GREEN,BLUE,ORANGE,'#7c3b91']
    for s,color in zip([.25,.5,.75,1],colors):
        ax[0].plot(t,2*np.pi*s*S,color=color,lw=2,label=f's = {s:g}')
        angle=np.linspace(0,2*np.pi*s,401)
        ax[1].plot(np.cos(angle),np.sin(angle),color=color,lw=1.8,alpha=.85)
        ax[1].scatter([np.cos(2*np.pi*s)],[np.sin(2*np.pi*s)],color=color,s=45,zorder=5)
    ax[0].set(xlim=(0,1),ylim=(-.15,6.55),xlabel='closed positive-arc parameter t',ylabel='argument of positive component')
    ax[0].set_yticks([0,np.pi,2*np.pi],['0','π','2π'])
    ax[0].axvspan(.25,.75,color=BLUE,alpha=.07);ax[0].grid(alpha=.2)
    ax[0].legend(loc='upper left');ax[0].set_title('vₛ = (exp(i s θ), 1)')
    ax[1].scatter([1],[0],marker='s',s=100,facecolor='white',edgecolor='black',zorder=6)
    ax[1].annotate('Negative component always 1',xy=(1,0),xytext=(.15,-1.42),ha='center',arrowprops={'arrowstyle':'->'},fontsize=10)
    ax[1].text(0,1.35,'Positive endpoint = exp(2π i s)',ha='center',fontsize=11)
    ax[1].set(xlim=(-1.45,1.45),ylim=(-1.7,1.7),aspect='equal')
    ax[1].axis('off');ax[1].set_title('Endpoint values may differ between summands')
    fig.suptitle('SGD.12–SGD.16: the original disk loop is nullhomotopic',fontsize=15)
    fig.text(.5,.035,'Ordered q-fold disk product = 0  →  actual graph Morita image = 0  →  every scalar pairing = 0',ha='center',fontsize=11)
    fig.tight_layout(rect=(0,.09,1,.92))
    yield 'split-germ-bott-nullhomotopy',fig

def render_memory():
    result={}
    for slug,fig in figures():
        for ext in ('png','svg'):
            buffer=io.BytesIO()
            metadata={'Software':'Original CC0 SGD diagram; Matplotlib'} if ext=='png' else {'Date':None,'Creator':'Original CC0 SGD diagram'}
            fig.savefig(buffer,format=ext,dpi=150,metadata=metadata)
            result[slug+'.'+ext]=buffer.getvalue()
        plt.close(fig)
    return result

if __name__=='__main__':
    out=HERE/'figures';out.mkdir(exist_ok=True)
    for name,data in render_memory().items():(out/name).write_bytes(data)
