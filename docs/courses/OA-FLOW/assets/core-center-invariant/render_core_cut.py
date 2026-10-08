"""Original exact core-cut model; NumPy and Matplotlib, no external assets."""
from pathlib import Path
import json, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
BG,INK,MUTED='#fcfbf7','#172d3c','#536575'
BLUE,TEAL,GOLD,RED='#236c9c','#087e80','#b88024','#b4443f'
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans',
    'font.size':12,'text.color':INK,'axes.labelcolor':INK,'axes.edgecolor':'#9ba9b1',
    'xtick.color':MUTED,'ytick.color':MUTED,'figure.facecolor':BG,'axes.facecolor':BG,
    'savefig.facecolor':BG,'svg.fonttype':'path','svg.hashsalt':'oa-flow-core-cut-20261007',
    'axes.spines.top':False,'axes.spines.right':False})

lam=np.array([.75,.25]);thresholds=-np.log(lam)
h=np.diag(lam);U=np.array([[1.,-1.],[1.,1.]])/math.sqrt(2);k=U@h@U.T
observable=np.array([[2.,1.],[1.,1.]])
def density(q,c=1.):
    q=np.asarray(q);return np.exp(-q)*sum((q>a-math.log(c)).astype(float) for a in thresholds)

def matrix(ax,x,y,values,label):
    dx=.105;dy=.105
    ax.text(x-.018,y,label,ha='right',va='center',fontsize=18)
    for i,row in enumerate(values):
        for j,v in enumerate(row):ax.text(x+(j+.5)*dx,y+(.5-i)*dy,str(v),ha='center',va='center',fontsize=17)
    for xx,d in [(x-.006,1),(x+2*dx+.006,-1)]:
        ax.plot([xx+d*.010,xx,xx,xx+d*.010],[y+dy,y+dy,y-dy,y-dy],color=INK,lw=1.3)

def plotted_density(ax,c,color,label):
    lo,hi=-.8,4
    breaks=[lo,*[float(a-math.log(c)) for a in thresholds],hi]
    for j,(left,right) in enumerate(zip(breaks[:-1],breaks[1:])):
        q=np.linspace(left,right,250);y=j*np.exp(-q)
        ax.plot(q,y,color=color,lw=2.3,label=label if j==1 else None)
    for j,a in enumerate(thresholds-math.log(c)):
        ax.plot(a,j*math.exp(-a),'o',ms=4,color=color,zorder=4)
        ax.plot(a,(j+1)*math.exp(-a),'o',ms=4,mfc=BG,mec=color,zorder=5)

def main():
    assert np.allclose(k,[[.5,.25],[.25,.5]])
    assert np.allclose(U.T@U,np.eye(2))
    assert np.all(np.linalg.eigvalsh(observable)>0)
    distance=float(np.abs(np.linalg.eigvalsh(h-k)).sum())
    assert math.isclose(distance,1/math.sqrt(2),rel_tol=1e-14)
    assert math.isclose(float(np.trace(h@observable)),7/4)
    assert math.isclose(float(np.trace(k@observable)),2)
    test=np.linspace(-.79,3.99,301)
    assert np.allclose(density(test,2),2*density(test+math.log(2)))
    assert math.isclose(sum(math.exp(-a) for a in thresholds),1)
    assert math.isclose(sum(math.exp(-(a-math.log(2))) for a in thresholds),2)

    fig=plt.figure(figsize=(15,10))
    fig.text(.05,.965,'A finite core cut remembers mass and unitary orbits',fontsize=23,weight='bold',va='top')
    fig.text(.05,.918,r'Exact $M_2(\mathbb{C})$ example: $h=\mathrm{diag}(3/4,1/4)$, $\varphi_h(x)=\mathrm{Tr}(hx)$, $H_h(q)=e^q h$.',fontsize=14)
    fig.text(.05,.879,r'$\tau(Y)=\frac{1}{2\pi}\int_{\mathbb{R}}e^{-q}\mathrm{Tr}(Y(q))\,dq$,     $\theta_sY(q)=Y(q-s)$,     $e_h(q)=1_{(1,\infty)}(H_h(q))$.',fontsize=15)
    ax=fig.add_axes([.075,.575,.365,.22])
    a,b=thresholds
    for left,right,y in [(-.8,a,0),(a,b,1),(b,4,2)]:ax.plot([left,right],[y,y],lw=3,color=BLUE)
    for x,old,new in [(a,0,1),(b,1,2)]:
        ax.plot(x,old,'o',color=BLUE,ms=6,zorder=4);ax.plot(x,new,'o',mfc=BG,mec=BLUE,ms=6,zorder=5)
        ax.axvline(x,color=MUTED,ls=':',lw=.9)
    ax.set(xlim=(-.8,4),ylim=(-.2,2.4),yticks=[0,1,2],yticklabels=[r'$0$',r'$P_1$',r'$I$'],
           xticks=[a,b,4],xticklabels=[r'$\log(4/3)$',r'$\log4$','4'],xlabel='core coordinate q',title='1. Two exact spectral thresholds')
    ax.tick_params(axis='x',labelsize=10);ax.grid(axis='y',alpha=.13)
    fig.text(.075,.507,r'$P_1$ projects onto the first coordinate; endpoints follow the strict cut.',fontsize=10.8,color=MUTED)

    ax=fig.add_axes([.59,.575,.35,.22])
    q=np.linspace(-.8,4,1800);part1=np.exp(-q)*(q>a);part2=np.exp(-q)*(q>b)
    ax.fill_between(q,0,part1,color=BLUE,alpha=.16);ax.fill_between(q,part1,part1+part2,color=TEAL,alpha=.25)
    plotted_density(ax,1,BLUE,r'$p_h(q)=e^{-q}\mathrm{Tr}(e_h(q))$')
    ax.set(xlim=(-.8,4),ylim=(0,.91),xlabel='core coordinate q',ylabel='central density',title='2. The central functional has mass one')
    ax.grid(alpha=.13)
    ax.text(.39,.83,r'$\int_{\mathbb{R}}p_h\,dq=\frac{3}{4}+\frac{1}{4}=1$',transform=ax.transAxes,fontsize=15)
    ax.text(.40,.65,r'$p_h(q)=e^{-q}\mathrm{Tr}(e_h(q))$',transform=ax.transAxes,fontsize=13)
    fig.text(.59,.507,r'$\chi_h(z)=\int p_h(q)z(q)\,dq=2\pi\tau(e_hz)$; thus $\tau(e_h)=1/(2\pi)$.',fontsize=12)
    fig.text(.59,.471,r'The mass beyond q = 4 is exactly $2e^{-4}$ and is included.',fontsize=10.8,color=MUTED)

    ax=fig.add_axes([.05,.115,.43,.305]);ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
    ax.text(.06,.98,'3. Conjugation preserves the central functional',fontsize=14,va='top')
    matrix(ax,.17,.68,[['3/4','0'],['0','1/4']],r'$h=$')
    matrix(ax,.68,.68,[['1/2','1/4'],['1/4','1/2']],r'$k=$')
    ax.text(.06,.44,r'$k=UhU^*$, with $U$ the rotation through $\pi/4$.',fontsize=14)
    ax.text(.06,.29,r'$e_k(q)=Ue_h(q)U^*$, so $\chi_k=\chi_h$.',fontsize=15,color=TEAL)
    ax.text(.06,.12,r'$\|\varphi_h-\varphi_k\|=1/\sqrt{2}$; the functionals differ.',fontsize=14)

    ax=fig.add_axes([.59,.17,.35,.22])
    plotted_density(ax,1,BLUE,r'$p_h$ (mass 1)');plotted_density(ax,2,TEAL,r'$p_{2h}$ (mass 2)')
    ax.set(xlim=(-.8,4),ylim=(0,1.8),xlabel='core coordinate q',ylabel='central density',title='4. Scaling shifts the cut to the left')
    ax.grid(alpha=.13);ax.legend(frameon=False,fontsize=11,loc='upper right')
    ax.annotate('',xy=(a-math.log(2),1.62),xytext=(a,1.62),arrowprops={'arrowstyle':'->','color':RED,'lw':1.8})
    ax.text(a-math.log(2)/2,1.68,r'$-\log2$',ha='center',fontsize=11,color=RED)
    fig.text(.59,.108,r'$p_{2h}(q)=2p_h(q+\log2)$, so $\chi_{2h}=2\chi_h\circ\theta_{\log2}$.',fontsize=13)
    fig.text(.05,.052,'Proof: A finite spectral cut of a core density, (CI3)–(CI6), (CI11)–(CI12). Thresholds, matrices and integrals are exact;',fontsize=10.5,color=MUTED)
    fig.text(.05,.033,'exponential curves are samples of the displayed formulas. The finite matrix example illustrates CI3–CI12 on the common core.',fontsize=10.5,color=MUTED)
    fig.savefig(HERE/'core-cut-normalization.png',dpi=160)
    fig.savefig(HERE/'core-cut-normalization.svg',metadata={'Date':None,'Creator':'Original OA-FLOW mathematical illustration','Rights':'CC0-1.0'})
    plt.close(fig)
    data={'model':'M2 tensor L-infinity(R), trace Tr tensor exp(-q)dq/(2pi)',
          'h':h.tolist(),'k':k.tolist(),'U':U.tolist(),'observable':observable.tolist(),
          'exact_eigenvalues':['3/4','1/4'],'thresholds_exact':['log(4/3)','log(4)'],
          'phi_h_observable_exact':'7/4','phi_k_observable_exact':'2',
          'predual_distance_exact':'1/sqrt(2)','cut_trace_exact':'1/(2*pi)',
          'central_mass_exact':1,'plot_tail_beyond_q_4_exact':'2*exp(-4)',
          'scalar_factor':2,'scaled_central_mass_exact':2,
          'scalar_density_identity':'p_(2h)(q)=2*p_h(q+log(2))',
          'dual_action':'theta_s Y(q)=Y(q-s)','dual_trace_scaling':'tau theta_s=exp(-s) tau',
          'proof_locators':['CI3','CI4','CI5','CI6','CI11','CI12'],
          'curve_status':'Samples of exact piecewise exponential formulas; open/closed threshold endpoints explicitly marked.',
          'font':'Installed DejaVu Sans; no copied font or external image',
          'license':'CC0-1.0 to the extent of rights held'}
    (HERE/'MODEL.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print('Core-cut figure rendered; exact matrix, mass, trace and scalar-covariance diagnostics passed.')

if __name__=='__main__':main()
