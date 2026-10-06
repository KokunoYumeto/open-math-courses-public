"""Exact supplementary checks for the full Matveev corollary.

CC0. Independently authored by OpenAI Codex, GPT-6.1 Sol, Ultra.
The lesson contains all-dimensional proofs; this is their finite certificate.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
import json
import sympy as sy
from laurent_constant import Interval,E,PI
from matveev_weighted_zero import c_log,lg
from matveev_block_parameters import exp_interval

CUT=F(4,25)

def fixed_checks():
    assert (E**2).lo>F(22,3)
    assert (E**2).hi<F(15,2)
    assert (4*E**2/30).hi<F(99,100)
    assert (100/E).hi<37
    assert (6*E/F(99,100)).hi<17
    assert (F(3,2)*E).lo>4
    assert (F(9,8)*(3/(2*PI)).sqrt()).hi<1
    pref=F(11,5)*E/(2*(2*PI).sqrt()).sqrt()
    assert pref.hi<4
    tailpref=192*exp_interval(F(11,10))/(27000*(2*PI).sqrt())
    assert tailpref.hi<F(9,1000)
    cn10=Interval(51)+F(11,2)*lg(10)
    assert (cn10/10).hi<F(32,5)
    assert (exp_interval(F(13,20))*F(15,32)).hi<1
    second_endpoint=F(486,2**20)*10**6*F(19,6)*F(15,32)**10
    assert second_endpoint<1
    assert F(675,704)+F(1,1000)<1
    assert F(34,3200)<1
    return {"constant_prefactor_upper":str(tailpref.hi),
            "second_constant_tail_endpoint":str(second_endpoint),
            "general_rank_relative_margin":str(1-F(675,704)-F(1,1000))}

def constant_checks():
    prefix=0; total=0
    maxfirst=None; maxsecond=None
    for n in range(2,101):
        cn=F(22,5)*n+7+F(11,2)*lg(n)
        fn=max(F(1),F(n,6))
        for k in [1,2]:
            lhs=lg(2)+c_log(n,k)+lg(fn)+cn.log()
            first=-lg(k)+k*(1+lg(F(n,2)))+(n+3)*lg(30)+F(7,2)*lg(n)
            second=(6*n+20)*lg(2)
            d1=lhs-first;d2=lhs-second
            assert d1.hi<0 and d2.hi<0
            if maxfirst is None or d1.hi>maxfirst[0]:
                maxfirst=(d1.hi,n,k)
            if maxsecond is None or d2.hi>maxsecond[0]:
                maxsecond=(d2.hi,n,k)
            if n<=9:prefix+=2
            total+=2
        # The cancellation in the coefficient ratio has precisely these powers.
        p=F(3*n,4)
        assert F(3*n-5,2)-p+2-p==F(-1,2)
        assert n-p+1-p==1-F(n,2)
        assert F(n+4,2)+p-2==F(5*n,4)
        assert n*(2-p)+3-n-p-n*(1-p)==3-p
        if n>=3:
            assert F(7,2)-F(11*n,8)<0
    return {"small_dimension_comparisons":prefix,
            "constant_comparisons_through_dimension100":total,
            "largest_log_ratio_first":{"upper":str(maxfirst[0]),
                                      "n":maxfirst[1],"kappa":maxfirst[2]},
            "largest_log_ratio_second":{"upper":str(maxsecond[0]),
                                       "n":maxsecond[1],"kappa":maxsecond[2]}}

def integer_rows(C):
    out=[]
    for v in C.nullspace():
        scale=sy.ilcm(*(q.q for q in v))
        row=(scale*v).T
        if next(q for q in row if q)!=abs(next(q for q in row if q)):
            row=-row
        out.append(row)
    return sy.Matrix.vstack(*out) if out else sy.zeros(0,C.cols)

def eliminate(C,I,b,weights):
    n=C.cols; r=C.rows; J=[j for j in range(n) if j not in I]
    U=integer_rows(C)
    assert U.rows==n-r and C*U.T==sy.zeros(r,n-r)
    A=U[:,J]
    delta=A.det()
    assert delta!=0
    z=A.T.inv()*(delta*sy.Matrix([b[j] for j in J]))
    assert all(q.q==1 for q in z)
    new=delta*sy.Matrix(b)-U.T*z
    assert all(new[j]==0 for j in J)
    assert C*new==delta*C*sy.Matrix(b)
    B=max([sy.Integer(1)]+[abs(b[j])*weights[j]/weights[-1] for j in range(n)])
    lengths=[max(abs(U[i,j])*weights[j] for j in range(n)) for i in range(U.rows)]
    rowprod=sy.prod(lengths)
    denominator=sy.prod(weights[j] for j in J)
    s=n-r
    assert abs(delta)**2*denominator**2<=s**s*rowprod**2
    for j in I:
        aug=sy.Matrix([b]+[list(U.row(i)) for i in range(s)])[:,J+[j]]
        assert abs(aug.det())==abs(new[j])
        assert (abs(new[j])*weights[j]*denominator)**2<=(s+1)**(s+1)*(B*weights[-1])**2*rowprod**2
    return {"delta":str(delta),"multipliers":[str(q) for q in z],
            "new_coefficients":[str(q) for q in new],
            "original_weighted_B":str(B)}

def elimination_checks():
    cases=[
        (sy.Matrix([[1,0,1],[0,1,1]]),[0,1],[3,-2,4],[1,2,3]),
        (sy.Matrix([[1,0,1,2,-1],[0,1,1,-1,3]]),[0,1],[2,-3,1,4,-2],[1,2,3,4,5]),
        (sy.Matrix([[1,0,1,2,0],[0,1,1,-1,0],[0,0,0,0,1]]),[0,1,4],[2,3,-1,4,5],[1,2,3,4,5]),
        (sy.Matrix([[1,2,3,0],[0,0,0,1]]),[0,3],[1,-2,4,3],[1,2,3,4])]
    examples=[]
    for C,I,b,A in cases:
        examples.append(eliminate(C,I,b,list(map(sy.Rational,A))))
    assert examples[0]["delta"]=="-1"
    assert examples[0]["new_coefficients"]==["-7","-2","0"]
    # Real-part projection can lose independence while retaining a nonzero form.
    # Logs are log2+2pi i, log3+4pi i, log6; coefficients (2,-1,1).
    C=sy.Matrix([[1,0,1],[0,1,1]])
    periods=sy.Matrix([[1,2,0]])
    full=C.col_join(periods)
    assert full.det()!=0
    b=sy.Matrix([2,-1,1])
    assert periods*b==sy.zeros(1,1)
    assert C*b==sy.Matrix([3,0])
    # A zero real part: logs 2pi i and log2-2pi i, coefficients (1,1).
    assert sy.Matrix([[1,-1]])*sy.Matrix([1,1])==sy.zeros(1,1)
    return examples

def deletion_checks():
    count=0
    for oldlast,newlast,B,D in product(
            [CUT,F(1,2),F(1),F(2),F(1000)],
            [CUT,F(1,3),F(1),F(7)],
            [F(1),F(3),F(10**7)],
            [1,2,100]):
        ell=1+lg(D)
        W=lg(F(3,2))+1+lg(B)+lg(D)+ell.log()
        newB=max(F(1),B*oldlast/newlast)
        newW=lg(F(3,2))+1+lg(newB)+lg(D)+ell.log()
        if oldlast==CUT and newB==B:
            assert newW.lo==W.lo and newW.hi==W.hi
        else:
            assert (newW/oldlast-W/CUT).hi<0
        count+=1
    return count

def check():
    fixed=fixed_checks()
    const=constant_checks()
    ex=elimination_checks()
    deleted=deletion_checks()
    return {"status":"passed","fixed":fixed,**const,
            "elimination_examples":ex,"zero_coefficient_deletion_cases":deleted,
            "real_branch_examples":2,
            "scope":"Full Matveev Theorem8.6 corollary, every allowed rank/branch/zero coefficient, both published constants and weighted/unweighted B. SourceTheorem2.2's broader mixed cutoff hypothesis is not claimed."}

if __name__=="__main__":
    print(json.dumps(check(),indent=2))
