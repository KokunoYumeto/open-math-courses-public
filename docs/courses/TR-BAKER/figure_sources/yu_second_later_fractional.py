"""Exact comparisons for the later second-scale fractional and contraction steps.

GPT-6 Astra (OpenAI), Ultra. Independent mathematics and figure; CC0.
The accompanying proof supplies uniform reductions and actual-family hypotheses.
Rational arithmetic only; no sampled depth argument.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
from yu_second_fractional_profile import case_data, exp_bounds


def calculate():
    lam, xi = Q(59,58), Q(101,100)
    rows=[]
    for name,c1,c3,c4,a,q,zeta,amin,dmin,w,nfactor,chi,pref,target in case_data():
        c2=Q(a,q*q)/zeta
        c=Q(27,50) if q==2 else Q(4,5)
        ell=Q(7,50) if q==2 else Q(11,50)
        logq_upper=Q(7,10) if q==2 else Q(11,10)
        rmin=3 if q==2 else 4
        comparisons=[]
        for r in range(rmin,9):
            tail=r==8
            y=Q(1,r+1);eta=1-c*y
            smin=c3*q*dmin*(r+1)**2
            tmin=Q(12,29)*(r+1)*12**r
            br=1500*12**(r-3)
            eps=Q(8*r+15,9*(r+1)*br)
            rem=Q(1,79)+Q(1,71928*br)
            hminus=eta**(r+1)
            hplus=1/exp_bounds(c)[0] if tail else hminus
            qbase=q*hminus
            assert qbase>1
            logQ_lower=2*(qbase-1)/(qbase+1)
            torus=(1/hminus+1/smin)/c2
            other=(w/(2*c2)*(1+1/(2*smin))+y*y/(c2*c3*q)
                   +(1+w/2)*c1*eps+(1+w)*c1*rem)
            b=lam*(1+ell+w+ell*Q(q,q-1))
            k=(Q(107,103)+Q(3,8)*y)*hplus**2+w*(1 if tail else 1-Q(483,824)*y)
            depth_b=3*lam*logq_upper/(c4*logQ_lower)
            if tail:
                gamma=(2*c*q/exp_bounds(c)[1]*sum(Q(1,q**j) for j in range(4))
                       -Q(2*q*9*(q+7),q**8)/smin)
            else:
                gamma=(2*c*q/Q(q**r)*(sum((q*eta)**j for j in range(r+1))+q-2)
                       -Q(q*(r+1),q**r)/smin
                       *(2*(q+1)*(eta**2-hminus)+2*sum(eta**j-hminus for j in range(3,r+1))))
            normal=lam*nfactor/(c4*q**r)
            input_lower=c1*q*chi-xi*(1-hminus+c*(1+2*hplus)*y+1/tmin)/(q**r*c3*(1+amin))
            for depth_endpoint in ['zero','maximum']:
                base=torus if depth_endpoint=='zero' else torus/32768
                linear=b/c4+(depth_b if depth_endpoint=='maximum' else 0)
                arith={'minimum':base+other+xi*(linear*amin+k/c3)/(1+amin),
                       'infinity' if tail else 'rank':base+other+xi*linear if tail else base+other+xi*(linear*r+k/c3)/(1+r)}
                for endpoint,bound in arith.items():
                    ga,gi=gamma-normal-bound,input_lower-bound
                    gc=2*c*q*(q-1)-lam*nfactor/c4-bound
                    ic=c1*chi*q**(r+1)-xi*(3*c*y+1/tmin)/(c3*(1+amin))-bound
                    assert ga>Q(7,10) and gi>Q(2,25),(name,r,depth_endpoint,endpoint)
                    assert gc>Q(7,10) and ic>9,(name,r,depth_endpoint,endpoint)
                    comparisons.append({'ranks':'all >= 8' if tail else r,
                        'depth_endpoint':depth_endpoint,'A0_endpoint':endpoint,
                        'arithmetic_upper':str(bound),'mass_lower':str(gamma),
                        'normal_loss_upper':str(normal),'input_lower':str(input_lower),
                        'mass_gap':str(ga),'input_gap':str(gi),
                        'contraction_mass_gap':str(gc),'contraction_input_gap':str(ic)})
        stated={'I.1':(Q(107,100),Q(1,5)), 'I.2':(Q(107,100),Q(2,25)),
                'II':(Q(11,10),Q(21,100)), 'III.1':(Q(103,100),Q(13,100)),
                'III.2':(Q(51,50),Q(7,25)), 'IV':(Q(26,25),Q(49,100)),
                'V':(Q(18,25),Q(39,100))}[name]
        assert all(Q(v['mass_gap'])>stated[0] and Q(v['input_gap'])>stated[1] for v in comparisons)
        rows.append({'case':name,'comparisons':comparisons,
                     'stated_mass_gap':str(stated[0]),'stated_input_gap':str(stated[1]),
                     'minimum_mass_gap':str(min(Q(v['mass_gap']) for v in comparisons)),
                     'minimum_input_gap':str(min(Q(v['input_gap']) for v in comparisons)),
                     'minimum_contraction_mass_gap':str(min(Q(v['contraction_mass_gap']) for v in comparisons)),
                     'minimum_contraction_input_gap':str(min(Q(v['contraction_input_gap']) for v in comparisons))})
    assert Q(173,200)**4>Q(1,3) and Q(21,25)**5>Q(1,3)
    assert Q(27,50)*Q(1,3)*Q(12,29)*12**3>1
    return {'state':'all_exact_later_fractional_and_contraction_comparisons_passed','scope':'Theorems207–208: I>=1, I log Q<=3B, c T_(I+1)/(r+1)>=1. Full root degree and rational denominators retained; finite ranks use the proved A0<r restriction. Corollary209 constructs the finite induction; fixed-order terminal branch remains separate.',
            'endpoint_comparisons':sum(len(r['comparisons']) for r in rows),'cases':rows}


def counting_example():
    q,r,c=2,3,Q(27,50)
    eta=1-c/(r+1);hf=eta**(r+1)
    si=Q(21,2)/hf;ti=Q(1200)*hf;output=(hf*ti).__floor__()
    radii=[q*(si.__floor__()+1)]+[(q**j*si).__floor__() for j in range(2,r+1)]
    mu=[(eta**j*ti).__floor__()-output+1 for j in range(r+1)]
    counts=[2*(q-1)*(si.__floor__()+1),2*(si.__floor__()+1)+1]+[2*(radii[j]-radii[j-1]) for j in range(1,r)]
    mass=sum(n*m for n,m in zip(counts,mu))
    layered=(2*radii[-1]+1)*mu[-1]+sum((2*radii[j]+1)*(mu[j+1]-mu[j+2]) for j in range(r-1))+counts[0]*(mu[0]-mu[1])
    assert mass==layered==37530
    assert counts==[38,39,74,150] and mu==[296,206,127,59] and output==376
    assert all(output+m-1==(eta**j*ti).__floor__() for j,m in enumerate(mu))
    assert c*hf*ti/(r+1)>=1
    lhs=(q-1)*(1-hf)+(eta-hf)+sum((q**j-q**(j-1))*(eta**j-hf) for j in range(2,r+1))
    rhs=c/(r+1)*(sum((q*eta)**j for j in range(r+1))+q-2)
    assert lhs==rhs
    return {'scope':'Exact counting illustration, not a number-field parameter instance.',
            'S_I':str(si),'T_I':str(ti),'output_order':output,'radii':radii,
            'multiplicities':mu,'counts':counts,'deleted_increment':mu[0]-mu[1],
            'mass':mass,'layered_mass':layered}


def render(result,example,path):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axes=plt.subplots(1,2,figsize=(12,4.9),layout='constrained',gridspec_kw={'width_ratios':[1.2,1]})
    ax=axes[0]
    bars=ax.bar(range(4),example['multiplicities'],color=['#175e86','#267d69','#72519a','#b26836'])
    for bar,n in zip(bars,example['counts']):
        ax.text(bar.get_x()+bar.get_width()/2,bar.get_height()+6,f'{n} nodes\norder weight {int(bar.get_height())}',ha='center',fontsize=8)
    ax.set(xticks=range(4),xticklabels=['Inner odd\n|s| <= 38','Inner even\n|s| <= 38','Annulus\n38 < |s| <= 75','Annulus\n75 < |s| <= 150'],ylim=(0,355),ylabel='Interpolation multiplicity',title='Exact mixed profile: total degree 37,530')
    ax.tick_params(axis='x',labelsize=8)
    ax=axes[1]
    labels=[v['case'] for v in result['cases']]
    bounds=[Q(v['stated_input_gap']) for v in result['cases']]
    bars=ax.bar(range(7),[float(v) for v in bounds],color='#175e86')
    for bar,v in zip(bars,bounds):ax.text(bar.get_x()+bar.get_width()/2,bar.get_height()+.012,str(v),ha='center',fontsize=8)
    ax.axhline(.08,ls='--',color='#a44436',label='Uniform strict margin 2/25')
    ax.set(xticks=range(7),xticklabels=labels,ylim=(0,.56),ylabel='Proved lower bound in normalized valuation units',title='Fractional input margins\nthrough the admissible depths')
    ax.tick_params(axis='x',labelsize=8);ax.legend(fontsize=8,loc='upper left')
    for ax in axes:ax.grid(axis='y',alpha=.18);ax.set_axisbelow(True)
    fig.savefig(path,dpi=160);plt.close(fig)


if __name__=='__main__':
    result=calculate()
    example=counting_example();result['counting_example']=example
    Path(__file__).with_name('second-later-fractional-check.json').write_text(json.dumps(result,indent=2)+'\n')
    import sys
    if '--figure' in sys.argv:render(result,example,Path(__file__).with_name('yu-second-later-fractional.png'))
    print(json.dumps({'state':result['state'],'comparisons':result['endpoint_comparisons'],
                     'gaps':[{k:r[k] for k in ['case','minimum_mass_gap','minimum_input_gap']} for r in result['cases']]}))
