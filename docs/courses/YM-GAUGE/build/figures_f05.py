"""Complete curvature contributions in YM-F05, F5.59--F5.63."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def build():
    out=Path(__file__).resolve().parents[1]/'figures';out.mkdir(exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path',
                         'svg.hashsalt':'YM-F05-curvature-contributions-v1'})
    # x is measured in metres; alpha=1 m^-1, beta=2 m^-1.
    x=np.linspace(0,2*np.pi,1201);alpha=1.;beta=2.
    fig=plt.figure(figsize=(13.5,10.5),facecolor='#fffef9')
    fig.text(.07,.953,'Curvature includes the derivative and the commutator',
             fontsize=21,weight='bold',color='#163e4b')
    fig.text(.07,.912,r'$\alpha=1\,\mathrm{m}^{-1},\ \beta=2\,\mathrm{m}^{-1}'
             r'\qquad \Gamma_x=-\alpha T_1$ in both connections',fontsize=16,color='#163e4b')
    colors=['#a4491c','#226c98','#273d45']
    ticks=np.pi*np.arange(5)/2
    labels=['0',r'$\pi/2$',r'$\pi$',r'$3\pi/2$',r'$2\pi$']
    for j in range(3):
        ax=fig.add_axes([.115,.664-.255*j,.80,.168],facecolor='white')
        ax.set(xlim=(0,2*np.pi),ylim=(-2.45,2.45),xticks=ticks,xticklabels=labels,yticks=[-2,0,2])
        ax.grid(color='#b6c5c7',alpha=.5,lw=.7)
        ax.set_ylabel(r'Coefficient ($\mathrm{m}^{-2}$)',fontsize=12)
        if j==0:
            ax.plot(x,np.full_like(x,alpha*beta),color='#006f69',lw=3)
            ax.set_title(r'Constant $\Gamma_y=-\beta T_2$: full $T_3$ curvature coefficient is $2$',
                         fontsize=15,loc='left',pad=13,color='#163e4b')
            ax.text(.035,.10,'Derivative = 0; commutator = 2. Other generator components are zero.',
                    transform=ax.transAxes,fontsize=12,color='#354e55')
        else:
            d=alpha*beta*(np.sin(alpha*x) if j==1 else -np.cos(alpha*x))
            ax.plot(x,d,color=colors[0],lw=2.7,label='Derivative contribution')
            ax.plot(x,-d,color=colors[1],lw=2.7,ls='--',label='Commutator contribution')
            ax.plot(x,np.zeros_like(x),color=colors[2],lw=2,ls=':',label='Complete curvature = 0')
            gen='2' if j==1 else '3'
            ax.set_title('Pure gauge: '+r'$T_'+gen+r'$ coefficient; both contributions retained',
                         fontsize=15,loc='left',pad=13,color='#163e4b')
        for spine in ax.spines.values():spine.set_color('#84989c')
        if j==2:
            ax.set_xlabel(r'Original coordinate $x$ (metres)',fontsize=13)
            handles,legend_labels=ax.get_legend_handles_labels()
    fig.legend(handles,legend_labels,loc='lower center',bbox_to_anchor=(.51,.060),
               ncol=3,frameon=False,fontsize=12)
    fig.text(.07,.035,r'Pure gauge: $\Gamma_y=-\beta(\cos(\alpha x)T_2+\sin(\alpha x)T_3)$; its $T_1$ curvature coefficient is zero.',
             fontsize=12,color='#354e55')
    fig.text(.07,.010,'All panels use the same vertical scale. Exact formulas and proofs: YM-F05, (F5.59)–(F5.63).',
             fontsize=11,color='#354e55')
    fig.savefig(out/'f05-curvature-cancellation.svg',metadata={'Date':None,'Creator':'YM-GAUGE CC0 figure source'})
    fig.savefig(out/'f05-curvature-cancellation.png',dpi=150,metadata={'Software':'YM-GAUGE CC0 figure source'})
    plt.close(fig)
    p=out/'f05-curvature-cancellation.svg';s=p.read_text(encoding='utf-8')
    start=s.index('<svg ');end=s.index('>',start)
    s=s[:end]+' role="img" aria-labelledby="f05-title f05-desc"'+s[end:]
    end=s.index('>',start)
    s=s[:end+1]+'''
<title id="f05-title">Derivative and commutator contributions to curvature</title>
<desc id="f05-desc">Alpha is one inverse metre and beta is two inverse metres. The x coordinate runs from zero to two pi metres. For the constant connection, the T3 curvature coefficient is two inverse square metres, entirely from the commutator. For the specified pure gauge, the T2 derivative contribution is two sine x and its commutator contribution is minus two sine x. The T3 derivative contribution is minus two cosine x and its commutator contribution is two cosine x. Both full pure-gauge curvature components vanish. All T1 curvature components and all other independent components are zero. Each graph uses the same vertical scale.</desc>'''+s[end+1:]
    p.write_text(s,encoding='utf-8')

if __name__=='__main__':build()
