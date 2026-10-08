"""Exact rational endpoints for TR-BAKER-10 Section43. CC0.

The complete field, scalar, floor, convexity and induction proofs in
Lemmas10.134–10.135 and Theorem10.136 give these bounds their scope.
All arithmetic here is rational; no rank or depth sampling is used.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import json
from integer_comparison_bounds import rows, constants, minimum_S, lam

node_factor = F(232,231)
step_margin = F(1,100)

def log_lower(x):
    z=(x-1)/(x+1)
    assert 0<z<1
    return 2*sum(z**(2*j+1)/(2*j+1) for j in range(20))

def terms(r, uniform=False):
    row=next(x for x in rows if x[0]=='V')
    name,c0,c1,c3,c4,q,c2,y,omega,C,cs=constants(row)
    c=cs[2] if uniform else cs[0 if r==2 else 1 if r<=7 else 2]
    a=r+1;eta=1-c/a;H=eta**a
    Hup=1/sum(c**j/factorial(j) for j in range(11)) if uniform else H
    Q=q*H
    br=F(7200,29)*14**(r-2)
    eps=(3+F(14,a))/(7*br)
    g12=(1+F(5,a))/(546*br)
    Cr=F(1) if uniform else F(103*r+4,103*a)+F(17*(r-1),24*a*a)
    g9=F(107,103) if uniform else max(F(107,103),1+F(1,3*a))
    Ar=c1*(g12+eps)+(c1*eps/2+lam/c4+Cr/(c3*y)+F(117,232*c2))/(C-1)
    b=Ar+c1*(F(1,300)+1/(273*999*br))+lam/c4
    n=lam*omega/c4;e=g9/(c3*y)
    ell=F(1099,1000);Dmin=6 if uniform else 5;l=lam*ell/(Dmin*c4)
    Sm=minimum_S(name,c3,q,r)
    return dict(r=r,a=a,c=c,eta=eta,H=H,Hup=Hup,Q=Q,br=br,b=b,n=n,e=e,l=l,Sm=Sm,c1=c1,c2=c2,c3=c3,c4=c4,y=y,ell=ell,q=q)

def finite_endpoint(r, endpoint):
    t=terms(r)
    a,c,eta,H,Q,br,b,n,e,l,Sm,c1,c2,c3,c4,y,ell,q=(t[k] for k in ['a','c','eta','H','Q','br','b','n','e','l','Sm','c1','c2','c3','c4','y','ell','q'])
    invQ=1/Q if endpoint=='early' else F(1,1000)
    lI=l if endpoint=='early' else 3*lam*ell/(c4*log_lower(Q))
    common=b+n+e*H+lI+l/2
    B=[common+q*(1+1/Sm)*invQ/c2]+[common+l*j+q**(j+1)*invQ/c2 for j in range(1,r)]
    delta=[(B[0]+step_margin)/(2*q*(q-1)*a)]+[node_factor*(B[j]+step_margin)/(2*q**(j+1)*a) for j in range(1,r)]
    tau=[];current=F(1)
    for d in delta:
        current-=d;tau.append(current)
    assert all(tau[j-1]>eta**j for j in range(1,r+1))
    assert delta[0]<c/a
    mass=(q-1)*(1-H)+(tau[0]-H)+sum((q**j-q**(j-1))*(tau[j-1]-H) for j in range(2,r+1))
    floorloss=F(q*a,q**r*Sm)*(2*(q+1)*(tau[1]-H)+2*sum(tau[j-1]-H for j in range(3,r+1)))
    Gamma=F(2*q*a,q**r)*mass-floorloss
    Af=b+e*H**2+lI+3*l/2+(1/H+1/Sm)*invQ/c2+n/q**r
    beta=c1/(7*a*br)
    integer_inputs=[c1*q**(r+1)-beta-(2*delta[0]+c*H/a)/(c3*y)-B[0]]
    integer_inputs += [c1*q**(r+1)-beta-delta[j]/(c3*y)-B[j] for j in range(1,r)]
    fractional_input=c1*q-beta/q**r-(1-H+delta[0]+2*c*H/a)/(q**r*c3*y)
    assert Gamma-Af>F(19,10)
    assert fractional_input-Af>F(12,5)
    assert min(integer_inputs)>1
    terminal_B=B[0]+(l if endpoint=='late' else 0)
    terminal_gain=2*c*q*(q-1)
    terminal_input=c1*q**(r+1)-beta-3*c/(a*c3*y)
    assert terminal_gain-terminal_B>3 and terminal_input-terminal_B>1
    return {'rank':r,'endpoint':endpoint,'fractional_gap':str(Gamma-Af),'input_gap':str(fractional_input-Af),'minimum_integer_input_gap':str(min(integer_inputs)),'last_full_order_fraction':str(tau[-1]),'fractional_gap_decimal':float(Gamma-Af),'input_gap_decimal':float(fractional_input-Af),'all_original_integer_orders_retained':True,'terminal_closure_gap':str(terminal_gain-terminal_B),'terminal_closure_input_gap':str(terminal_input-terminal_B),'terminal_closure_gap_decimal':float(terminal_gain-terminal_B)}

def uniform_endpoints():
    t=terms(8,True)
    c,Hlo,Hup,Qlo,br,b,n,e,l,Sm,c1,c2,c3,c4,y,ell,q=(t[k] for k in ['c','H','Hup','Q','br','b','n','e','l','Sm','c1','c2','c3','c4','y','ell','q'])
    output=[]
    common_bounds=[]
    for endpoint in ['early','late']:
        invQ=1/Qlo if endpoint=='early' else F(1,1000)
        lI=l if endpoint=='early' else 3*lam*ell/(c4*log_lower(Qlo))
        common=b+n+e*Hup+lI+l/2
        common_bounds.append(common)
        loss=node_factor*invQ/(2*c2)+((1+node_factor)*(common+step_margin)/12+node_factor*l/8+(1+1/Sm)*invQ/(4*c2))/9
        assert 1-loss>(F(671,1000) if endpoint=='early' else F(892,1000))>F(2,3)
        Af=b+e*Hup**2+lI+3*l/2+(1/Hlo+1/Sm)*invQ/c2+n/q**8
        gain=q*9*(2-1/(q**8*Sm))*(F(2,3)-Hup)
        inp=c1*q-c1/(7*9*br*q**8)-(1-Hlo+c*(1+2*Hup)/9)/(q**8*c3*y)
        assert gain-Af>F(19,10) and inp-Af>F(12,5)
        B0=common+q*(1+1/Sm)*invQ/c2
        assert B0<8
        terminal_B=B0+(l if endpoint=='late' else 0)
        terminal_gain=2*c*q*(q-1)
        terminal_input=c1*q**9-c1/(7*9*br)-3*c/(9*c3*y)
        assert terminal_gain-terminal_B>3 and terminal_input-terminal_B>1
        output.append({'rank':'all_r_ge_8','endpoint':endpoint,'last_full_order_lower':str(1-loss),'fractional_gap':str(gain-Af),'input_gap':str(inp-Af),'closure_upper':str(B0),'fractional_gap_decimal':float(gain-Af),'input_gap_decimal':float(inp-Af),'terminal_closure_gap':str(terminal_gain-terminal_B),'terminal_closure_input_gap':str(terminal_input-terminal_B),'terminal_closure_gap_decimal':float(terminal_gain-terminal_B)})
    max_common=max(common_bounds)
    coefficient=(max_common+l)/q**2+1/(c2*Qlo)
    assert coefficient<F(3,2)
    assert node_factor*(F(3,2)+step_margin/q**2)/2<F(4,5)
    beta=c1/(7*9*br)
    full_input=q**8*(q*c1-F(3,2))-beta-F(4,5*9)/(c3*y)
    closure_input=c1*q**9-beta-(2*F(801,100)/12+c*Hup)/(9*c3*y)-8
    assert full_input>1 and closure_input>1
    assert F(801,1200)<c
    return output, {'all_integer_step_coefficient':str(coefficient),'full_input_uniform_gap':str(full_input),'deleted_input_uniform_gap':str(closure_input)}

def run():
    finite=[finite_endpoint(r,e) for r in range(2,8) for e in ['early','late']]
    uniform,extra=uniform_endpoints()
    return {'state':'rational_bounds_passed','finite':finite,'uniform':uniform,'uniform_integer_inputs':extra,'scope':'12 exact rank2–7 endpoint rows and two analytically uniform rank>=8 endpoints for originalV. Section43 proves their field/scalar/jet/floor/convexity scope and the exact phase induction. Terminal closure uses the distinct full interval [1,3D/lnQ+1].'}

if __name__=='__main__':
    data=run()
    Path(__file__).with_name('V-adaptive-rational-bounds.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'state':data['state'],'finite_rows':len(data['finite']),'uniform_rows':len(data['uniform']),'minimum_fractional_gap':min(x['fractional_gap_decimal'] for x in data['finite']+data['uniform']),'minimum_input_gap':min(x['input_gap_decimal'] for x in data['finite']+data['uniform']),'minimum_terminal_closure_gap':min(x['terminal_closure_gap_decimal'] for x in data['finite']+data['uniform'])}))
