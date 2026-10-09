"""Coordinates of the SU(2) subgroup and its rotation image, YM-F04 F4.48."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def build():
    out=Path(__file__).resolve().parents[1]/'figures'
    out.mkdir(exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,
                         'svg.hashsalt':'YM-F04-double-cover-v1'})
    theta=np.linspace(0,4*np.pi,1601)
    fig=plt.figure(figsize=(13.5,8.5),facecolor='#fffef9')
    fig.text(.07,.946,'One matrix return takes two spatial turns',
             fontsize=23,weight='bold',color='#163e4b')
    fig.text(.07,.903,r'$U(\theta)=\mathrm{diag}(e^{-i\theta/2},e^{i\theta/2})'
             r'\qquad R_{U(\theta)}e_1=(\cos\theta,\sin\theta,0)^T$',
             fontsize=18,color='#163e4b')
    ticks=np.pi*np.arange(5)
    labels=['0',r'$\pi$',r'$2\pi$',r'$3\pi$',r'$4\pi$']
    panels=[
      (np.cos(theta/2),-np.sin(theta/2),r'$\mathrm{Re}\,U_{11}=\cos(\theta/2)$',
       r'$\mathrm{Im}\,U_{11}=-\sin(\theta/2)$','Matrix entries'),
      (np.cos(theta),np.sin(theta),r'$(R_Ue_1)_1=\cos\theta$',
       r'$(R_Ue_1)_2=\sin\theta$','Rotated vector')]
    for k,(y1,y2,label1,label2,title) in enumerate(panels):
        ax=fig.add_axes([.09,.535-.345*k,.82,.245],facecolor='white')
        ax.plot(theta,y1,color='#006f69',lw=2.8,label=label1)
        ax.plot(theta,y2,color='#8a3b94',lw=2.6,ls='--',label=label2)
        ax.set(xlim=(0,4*np.pi),ylim=(-1.2,1.2),xticks=ticks,xticklabels=labels,
               yticks=[-1,0,1])
        ax.set_ylabel(title,fontsize=13)
        ax.grid(color='#b6c5c7',alpha=.5,lw=.7)
        ax.axvline(2*np.pi,color='#ae641d',lw=1.2,ls=':')
        ax.legend(loc='upper center',bbox_to_anchor=(.5,1.38),ncol=2,
                  frameon=False,fontsize=13)
        ax.tick_params(labelsize=12)
        for spine in ax.spines.values():spine.set_color('#84989c')
        if k==1:ax.set_xlabel(r'Parameter $\theta$ (radians)',fontsize=13)
    fig.text(.09,.802,r'$U(0)=I_2$',fontsize=13,color='#163e4b')
    fig.text(.47,.802,r'$U(2\pi)=-I_2$',fontsize=13,color='#ae641d')
    fig.text(.80,.802,r'$U(4\pi)=I_2$',fontsize=13,color='#163e4b')
    fig.text(.09,.457,r'$R_{U(0)}=I_3$',fontsize=13,color='#163e4b')
    fig.text(.46,.457,r'$R_{U(2\pi)}=I_3$',fontsize=13,color='#ae641d')
    fig.text(.79,.457,r'$R_{U(4\pi)}=I_3$',fontsize=13,color='#163e4b')
    fig.text(.07,.080,r'$U_{22}=\overline{U_{11}}$; both off-diagonal entries and $(R_Ue_1)_3$ are zero.',
             fontsize=13,color='#354e55')
    fig.text(.07,.043,'All displayed coordinates use the same vertical scale. Lines sample the exact functions in (F4.48).',
             fontsize=11,color='#354e55')
    fig.text(.07,.014,'One specified subgroup curve; proof of the full covering and its kernel: YM-F04, (F4.43)–(F4.47).',
             fontsize=11,color='#354e55')
    fig.savefig(out/'f04-double-cover.svg',metadata={'Date':None,'Creator':'YM-GAUGE CC0 figure source'})
    fig.savefig(out/'f04-double-cover.png',dpi=150,metadata={'Software':'YM-GAUGE CC0 figure source'})
    plt.close(fig)
    p=out/'f04-double-cover.svg';s=p.read_text(encoding='utf-8')
    start=s.index('<svg ');end=s.index('>',start)
    s=s[:end]+' role="img" aria-labelledby="f04-title f04-desc"'+s[end:]
    end=s.index('>',start)
    s=s[:end+1]+'''
<title id="f04-title">The SU(2) curve returns after two spatial turns</title>
<desc id="f04-desc">Upper graph: real and imaginary parts of the first diagonal entry are cosine of theta over two and minus sine of theta over two. At theta equal to two pi the matrix is minus the identity; at four pi it is the identity. Lower graph: the first two coordinates of the rotated vector are cosine theta and sine theta. The rotation is the identity at both two pi and four pi. The other diagonal entry is the complex conjugate of the first, both off-diagonal entries are zero, and the third vector coordinate is zero. Both graphs use identical vertical scales and parameter interval zero to four pi.</desc>'''+s[end+1:]
    p.write_text(s,encoding='utf-8')

if __name__=='__main__':
    build()
