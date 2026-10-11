"""Three original views of MP02-05; exact rational samples, no source images."""
from pathlib import Path
from fractions import Fraction
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,
                     'mathtext.fontset':'dejavusans','savefig.facecolor':'white'})

def canvas(title,height=7.2):
    fig=plt.figure(figsize=(6,height),facecolor='white')
    ax=fig.add_axes([.035,.055,.93,.83]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
    fig.text(.5,.955,title,ha='center',va='top',fontsize=21,weight='bold')
    return fig,ax

def save(fig,name):
    fig.savefig(ROOT/name,dpi=150,metadata={'Software':'Matplotlib; original OA-MOD illustration'})
    plt.close(fig)

def render():
    fig,ax=canvas('Three finite vector domains')
    boxes=[
        (.73,'#eaf1fd',r'$F=\ker L$',r'$\varphi=\mathrm{Tr}_B$'+ '\n'+r'$q_B[\xi]=\sum n^2|\xi_n|^2\quad(\xi\in F)$'),
        (.435,'#e4f4eb',r'$E=D(A^{1/2})$',r'$E=\{\xi:\sum n^2|\xi_n|^2<\infty\}$'+'\n'+r'$F$ is energy-closed in $E$; $e_1\notin F$.'),
        (.14,'#fff1df',r'$E+\mathbb{C} v$',r'$\Psi=\varphi(a\,\cdot\,a^*)$'+'\n'+r'$Q_\Psi[\xi+tv]=q[\xi],\quad\ker Q_\Psi=\mathbb{C} v$')]
    for y,color,title,body in boxes:
        ax.add_patch(FancyBboxPatch((.025,y),.95,.225,boxstyle='round,pad=.016',facecolor=color,edgecolor='#697789',linewidth=1.3))
        ax.text(.065,y+.17,title,fontsize=21,va='center')
        ax.text(.065,y+.075,body,fontsize=17,va='center',linespacing=1.75)
    ax.text(.5,.055,r'$F\subsetneq E\subsetneq E+\mathbb{C} v$',ha='center',fontsize=20)
    fig.text(.5,.03,'All three spaces are Hilbert dense.\nDomain inclusions, not geometric regions.  MP02-03.',ha='center',fontsize=14,linespacing=1.5)
    save(fig,'modular-partition-domains.png')

    fig,ax=canvas('Input and analytic endpoint')
    ax.text(.5,.96,r'$U=A^{1/2}B^{-1/2}:H\longrightarrow v^\perp$',ha='center',fontsize=19)
    ax.text(.5,.865,r'$U^*U=1,\qquad UU^*=1-P_v$',ha='center',fontsize=19)
    ax.text(.5,.72,r'$a=U^*:H\longrightarrow H$',ha='center',fontsize=21)
    ax.text(.5,.635,r'$aa^*=1,\quad a^*a=1-P_v$',ha='center',fontsize=19)
    ax.text(.5,.51,r'$\sigma^\varphi_{-i/2}(a)=U$',ha='center',fontsize=25,color='#075b82',
            bbox={'facecolor':'#e6f2fa','edgecolor':'#4d859e','boxstyle':'round,pad=.4'})
    ax.text(.5,.34,r'$aF\subset F,\quad B^{1/2}a\xi=UB^{1/2}\xi$'+'\n'+r'for every $\xi\in F=D(B^{1/2})$',ha='center',fontsize=17,linespacing=1.85)
    ax.text(.5,.15,r'$v=S^{-1/2}(1/n)_n,\quad S=\sum n^{-2}$'+'\n'+r'$v\notin E,\qquad \ker a=\mathbb{C} v$',ha='center',fontsize=18,linespacing=1.85)
    fig.text(.5,.03,'The closed half-strip is contractive.\nThe intertwining identity holds on the full domain.  MP03.',ha='center',fontsize=14,linespacing=1.5)
    save(fig,'modular-partition-endpoint.png')

    fig=plt.figure(figsize=(6,8),facecolor='white')
    ax=fig.add_axes([.17,.34,.78,.43])
    h=Fraction(0);values=[]
    for n in range(1,21):
        h+=Fraction(1,n*n);values.append(Fraction(n)/h)
    assert values[3]==Fraction(576,205)
    ax.plot(range(1,21),list(map(float,values)),color='#126b94',marker='o',markersize=4,linewidth=2)
    ax.scatter([4],[float(values[3])],color='#b44335',s=45,zorder=4)
    ax.annotate(r'$576/205$',xy=(4,float(values[3])),xytext=(8,2.35),fontsize=16,color='#b44335',
                arrowprops={'arrowstyle':'->','color':'#b44335'})
    ax.set(xlim=(.5,20.5),ylim=(0,14.8),xticks=[1,4,8,12,16,20])
    ax.tick_params(labelsize=13);ax.set_xlabel('Truncation N',fontsize=16)
    ax.set_ylabel(r'$\Psi(P_{v_N})=N/H_N$',fontsize=18)
    ax.grid(alpha=.23)
    ax.text(.06,.94,r'$v_N\to v$ in $H$'+'\n'+r'$\Psi(P_{v_N})\to\infty$'+'\n'+r'$\Psi(P_v)=0$',transform=ax.transAxes,va='top',fontsize=16,linespacing=1.7,
            bbox={'facecolor':'white','edgecolor':'#a5adb7','boxstyle':'round,pad=.35'})
    fig.text(.5,.965,'Hilbert limit, different energy',ha='center',va='top',fontsize=21,weight='bold')
    fig.text(.5,.86,r'$H_N=\sum_{n=1}^N n^{-2},\qquad N/H_N\geq N/2$',ha='center',fontsize=17)
    fig.text(.5,.17,r'$\varphi(P_1)=\infty,\quad\Psi(P_1)=1$'+'\n'+r'$\varphi(P_v)=\infty,\quad\Psi(P_v)=0$',ha='center',fontsize=18,linespacing=1.7)
    fig.text(.5,.035,'Exact rational samples at integer N.\nThe Hilbert limit has a separate energy.\nMP03 and MP05.',ha='center',fontsize=14,linespacing=1.5)
    save(fig,'modular-partition-energies.png')

if __name__=='__main__':render()
