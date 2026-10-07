"""Exact guaranteed principal-unit depth paths; original CC0 mathematical figure.

GPT-6.1 Sol (OpenAI), Ultra. Figure10.16, Lemma10.81 and Solution36.
Human context: free Yu2013 equations2.1/4.7/4.11; preceding programme9.5.
Paths are lower bounds; no claim of simultaneous attainment of each step.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

def parameters(p,e):
    k,P=0,1
    while P*(p-1)<=2*e:
        k+=1;P*=p
    assert Q(P*(p-1),p)<=2*e<P*(p-1)
    vartheta=Q(p-2,p-1) if p>=5 and e==1 else Q(P,2*e)
    return k,P,vartheta

def path(p,e):
    k,P,vartheta=parameters(p,e)
    values=[Q(1,e)]
    for _ in range(k):
        values.append(min(p*values[-1],values[-1]+1))
    assert values[-1]>=vartheta+Q(1,p-1)
    return {'p':p,'e':e,'kappa':k,'P':P,'vartheta':vartheta,
            'values':values,'depth':vartheta+Q(1,p-1)}

CASES=[(2,2),(2,3),(3,2),(3,3),(7,2),(5,1)]

def figure():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size':12,'font.family':'DejaVu Sans'})
    fig,axes=plt.subplots(2,3,figsize=(14,8.4))
    for ax,(p,e) in zip(axes.flat,CASES):
        row=path(p,e);xs=list(range(row['kappa']+1));ys=[float(x) for x in row['values']]
        ax.plot(xs,ys,'o-',color='#176f98',lw=2.3,ms=7,label='guaranteed valuation')
        ax.axhline(float(row['depth']),color='#ae4c32',ls='--',lw=1.7,label='required final depth')
        for x,y,exact in zip(xs,ys,row['values']):
            ax.annotate(str(exact),(x,y),xytext=(0,10),textcoords='offset points',ha='center',fontsize=12)
        ax.set_title(rf'$p={p},\ e={e},\ P={row["P"]}$',fontsize=15,pad=22)
        ax.text(.02,.95,rf'$\vartheta={row["vartheta"]},\quad \vartheta+1/(p-1)={row["depth"]}$',transform=ax.transAxes,va='top',fontsize=11)
        ax.set_xticks(xs);ax.set_xlabel('power step j');ax.set_ylabel(r'lower bound for $v_p$')
        ax.set_xlim(-.25,max(.4,row['kappa']+.25));ax.set_ylim(0,max(ys+[float(row['depth'])])*1.4)
        ax.grid(alpha=.2);ax.spines[['top','right']].set_visible(False)
    handles,labels=axes.flat[0].get_legend_handles_labels()
    fig.legend(handles,labels,ncol=2,loc='lower center',bbox_to_anchor=(.5,.014),frameon=False)
    fig.suptitle('The original principal-unit power reaches the analytic depth',fontsize=19,y=.975)
    fig.subplots_adjust(left=.065,right=.985,top=.86,bottom=.14,wspace=.29,hspace=.65)
    target=Path(__file__).with_name('principal-unit-depth.png')
    fig.savefig(target,dpi=150,facecolor='white');plt.close(fig)
    return target

if __name__=='__main__':
    print(json.dumps({'figure':str(figure()),'cases':[{k:([str(x) for x in v] if isinstance(v,list) else str(v) if isinstance(v,Q) else v) for k,v in path(p,e).items()} for p,e in CASES]}))
