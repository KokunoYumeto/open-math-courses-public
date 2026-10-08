"""Exact odd-prime rational bounds, TR-BAKER-10 Section44. CC0.

Lemmas10.137–10.138, Theorem10.139 and Corollary10.140 prove the continuous-depth,
all-rank, global-field and terminal-closure scope of these bounds.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import json
from integer_comparison_bounds import rows,constants,minimum_S,lam
from V_adaptive_comparison import log_lower

def exp_upper(c):
    return sum(c**j/factorial(j) for j in range(11))+c**11/(factorial(11)*(1-c/12))

def endpoint(row,r,which,uniform=False):
    name,c0,c1,c3,c4,q,c2,y,norm,C,cs=constants(row)
    assert q==2
    c=cs[2] if uniform else cs[0 if r==2 else 1 if r<=7 else 2]
    a=r+1;eta=1-c/a;H=eta**a
    Hup=1/sum(c**j/factorial(j) for j in range(11)) if uniform else H
    Q=q*H;br=F(7200,29)*14**(r-2)
    eps=(3+F(14,a))/(7*br)
    g12=F(0) if name in ['I.2','III.2'] else (1+F(5,a))/(546*br)
    Cr=F(1) if uniform else F(103*r+4,103*a)+F(17*(r-1),24*a*a)
    g9=F(107,103) if uniform or name in ['I.2','III.2'] else max(F(107,103),1+F(1,3*a))
    Ar=c1*(g12+eps)+(c1*eps/2+lam/c4+Cr/(c3*y)+F(117,232*c2))/(C-1)
    b=Ar+c1*(F(1,300)+1/(273*999*br))+lam/c4
    n=lam*norm/c4;e=g9/(c3*y)
    l=lam*F(347,500)/((6 if uniform else 5)*c4)
    Sm=minimum_S(name,c3,q,r)
    v=1/Q if which=='early' else F(1,1000)
    lI=l if which=='early' else 3*lam*F(347,500)/(c4*log_lower(Q))
    Af=b+e*Hup**2+lI+2*l+(1/H+1/Sm)*v/c2+n/q**r
    if uniform:
        gain=2*c*q/exp_upper(c)*sum(F(1,q**k) for k in range(4))-F(2*q*a*(q+r-1),q**r*Sm)
        input_=c1*q-c1/(7*a*br*q**r)-(1-H+c*(1+2*Hup)/a)/(q**r*c3*y)
    else:
        gain=F(2*c*q,q**r)*sum((q*eta)**j for j in range(r+1))
        gain-=F(q*a,q**r*Sm)*(2*(q+1)*(eta**2-H)+2*sum(eta**j-H for j in range(3,r+1)))
        input_=c1*q-c1/(7*a*br*q**r)-(1-H+c*(1+2*H)/a)/(q**r*c3*y)
    closure=b+n+e*Hup+lI+l+(l if which=='late' else 0)+q*(1+1/Sm)*v/c2
    closure_input=c1*q**(r+1)-c1/(7*a*br)-3*c/(a*c3*y)
    return {'case':name,'rank':'all_r_ge_8' if uniform else r,'endpoint':which,
      'fractional_gap':str(gain-Af),'input_gap':str(input_-Af),
      'terminal_closure_gap':str(2*c*q*(q-1)-closure),'terminal_input_gap':str(closure_input-closure),
      'fractional_gap_decimal':float(gain-Af),'input_gap_decimal':float(input_-Af),
      'terminal_closure_gap_decimal':float(2*c*q*(q-1)-closure)}

def run():
    out=[]
    for row in rows:
        if row[0]=='V':continue
        out += [endpoint(row,r,e) for r in range(2,8) for e in ['early','late']]
        out += [endpoint(row,8,e,True) for e in ['early','late']]
    assert len(out)==98
    for x in out:
        assert F(x['fractional_gap'])>F(3,4)
        assert F(x['input_gap'])>1
        assert F(x['terminal_closure_gap'])>F(1,4)
        assert F(x['terminal_input_gap'])>1
    return {'state':'rational_endpoints_passed','rows':out,
        'scope':'84 finite rank2–7 and14 analytically uniform rank>=8 rational endpoint envelopes. Section44 supplies the complete continuous-depth, all-rank, actual-field and terminal phase-induction proofs. No sampled-rank conclusion.'}

if __name__=='__main__':
    record=run();out=record['rows']
    Path(__file__).with_name('odd-depth-rational-endpoints.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'state':record['state'],'rows':len(out),
     'minimum_fractional':min(x['fractional_gap_decimal'] for x in out),
     'minimum_input':min(x['input_gap_decimal'] for x in out),
     'minimum_terminal_closure':min(x['terminal_closure_gap_decimal'] for x in out)}))
