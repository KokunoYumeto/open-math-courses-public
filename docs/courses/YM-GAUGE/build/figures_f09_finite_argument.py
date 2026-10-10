"""Exact scalar examples for the spatial, temporal and tension estimates."""
from pathlib import Path
import math,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def build():
    out=Path(__file__).resolve().parents[1]/'figures'
    out.mkdir(exist_ok=True)
    plt.rcParams.update({'font.size':12,'axes.spines.top':False,
      'axes.spines.right':False,'svg.fonttype':'none','svg.hashsalt':'ym-f09-m'})
    colors=['#146879','#ac4b15','#67539a']
    def save(fig,stem):
        fig.savefig(out/(stem+'.svg'),metadata={'Date':None})
        fig.savefig(out/(stem+'.png'),dpi=150,metadata={'Software':'YM-GAUGE reproducible figures'})
        plt.close(fig)
    S=4.;s=np.linspace(0,S,1200);positive=s[1:]
    kernels=[np.r_[0,positive**.25*np.log(S/positive)],
      2*s**.25*(1-np.sqrt(s/S)),s**.25*(1-s/S)]
    points=[S*math.exp(-4),S/9,S/5]
    values=[4/math.e*S**.25,2*(S/9)**.25*(1-1/3),(S/5)**.25*(1-1/5)]
    fig,ax=plt.subplots(figsize=(10,5),layout='constrained')
    names=['ℓ = 0: s¹ᐟ⁴ log(S/s)','ℓ = 1: 2s¹ᐟ⁴[1 − (s/S)¹ᐟ²]','ℓ = 2: s¹ᐟ⁴(1 − s/S)']
    for y,xm,ym,col,label in zip(kernels,points,values,colors,names):
        ax.plot(s,y,color=col,label=label,lw=2)
        ax.scatter([xm],[ym],color=col,s=30)
    for xm,ym,label,shift in zip(points,values,['s = S e⁻⁴','s = S/9','s = S/5'],[(30,12),(35,12),(30,-24)]):
        ax.annotate(label,(xm,ym),xytext=shift,textcoords='offset points',arrowprops={'arrowstyle':'-','color':'#666'},fontsize=11)
    ax.set(xlabel='Original heat time s (m²)',ylabel='Weighted temporal kernel (m¹ᐟ²)',
      title='Finite temporal kernels on 0 ≤ s ≤ S = 4 m²',xlim=(0,4),ylim=(0,2.65))
    ax.legend(loc='upper right',fontsize=10)
    save(fig,'f09-wave-interactions')
    fig,ax=plt.subplots(1,2,figsize=(12,4.5),layout='constrained')
    A=2.;lams=[.5,1.,2.]
    for lam,col in zip(lams,colors):ax[0].plot(s,A*(s/S)**lam,color=col,lw=2,label='λ = '+str(lam))
    ax[0].set(xlabel='Original heat time s (m²)',ylabel='Scalar observation h (observation units)',title='h = A(s/S)ᶿ, with θ = λ and A = 2',xlim=(0,4),ylim=(0,2.15))
    ax[0].set_title('h = A exp[λ log(s/S)], A = 2')
    ax[0].legend()
    vals=[A*A/(2*lam) for lam in lams];deriv=[lam*A*A/2 for lam in lams]
    xx=np.arange(3)
    ax[1].bar(xx-.17,vals,width=.34,color=colors[0],label='Integral of h² dτ')
    ax[1].bar(xx+.17,deriv,width=.34,color=colors[1],label='Integral of (dh/dτ)² dτ')
    ax[1].axhline(A*A,color=colors[2],ls='--',label='2 ‖h‖₂ ‖h′‖₂ = A² = 4')
    ax[1].set(xticks=xx,xticklabels=['λ = 1/2','λ = 1','λ = 2'],ylabel='Squared observation units',title='Exact trace identity on −∞ < τ ≤ 0',ylim=(0,6.3))
    ax[1].legend(fontsize=10,loc='upper center')
    save(fig,'f09-spatial-smoothing')
    fig,ax=plt.subplots(1,2,figsize=(11,4.5),layout='constrained')
    labels=['Trace\ndimension 1','Symmetric trace-free\ndimension 5','Antisymmetric\ndimension 3']
    for axis,values,title,ylims in [(ax[0],[2,-1,-3],'Exact operator eigenvalues',(-3.8,3.0)),(ax[1],[4,1,9],'Multipliers on squared norms',(0,11.5))]:
        bars=axis.bar(np.arange(3),values,color=colors,width=.65)
        axis.axhline(0,color='#555',lw=.8);axis.set(xticks=np.arange(3),xticklabels=labels,title=title,ylim=ylims)
        for bar,value in zip(bars,values):axis.text(bar.get_x()+bar.get_width()/2,value+(.2 if value>=0 else -.2),str(value),ha='center',va='bottom' if value>=0 else 'top')
    fig.suptitle('W(V) = −2V + Vᵀ + trₓ(V)I₃ on spatial labels',fontsize=15)
    save(fig,'f09-tension-forcing')
    data={'scope':'Exact scalar kernels and a finite spatial-label operator; these are not numerical Yang–Mills solutions.',
      'wave':{'S_m2':S,'maximizing_s_m2':points,'maxima_m_half':values if False else [4/math.e*S**.25,2*(S/9)**.25*(1-1/3),(S/5)**.25*(1-1/5)],'proof':'UA.10'},
      'trace':{'S_m2':S,'A':A,'lambda':lams,'integrals_h_squared':vals,'integrals_derivative_squared':deriv,'proof':'HS.14–HS.15'},
      'spatial_operator':{'eigenvalues':[2,-1,-3],'squared_multipliers':[4,1,9],'real_dimensions':[1,5,3],'proof':'TW.17–TW.18'}}
    (out/'f09-finite-argument-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':build()
