"""Exact duplication, Bezout and height-window checks for22.191--197."""
from collections import Counter
from fractions import Fraction as F
from math import gcd,lcm
from pathlib import Path
import json
import mpmath as mp
import sympy as sp


def rational_gcd(values):
    values=[F(v) for v in values]
    den=lcm(*(v.denominator for v in values))
    return F(gcd(*(v.numerator*(den//v.denominator) for v in values)),den)


def pair_normalize(x,z):
    x,z=F(x),F(z)
    scale=rational_gcd([x,z])
    assert scale
    X,Z=int(x/scale),int(z/scale)
    if Z<0:X,Z=-X,-Z
    return X,Z


def projective_height(values):
    values=[F(x) for x in values]
    scale=rational_gcd(values)
    return max(abs(int(x/scale)) for x in values)


def telescope_data(last=8):
    mp.mp.dps=80
    N,D=3,1;out=[]
    for r in range(last+1):
        H=max(abs(N),abs(D))
        center=3*mp.log(H)/(2*4**r)
        lower=center-mp.log(912)/(2*4**r)
        upper=center+mp.log(17)/(2*4**r)
        out.append({'r':r,'numerator_bits':N.bit_length(),'denominator_bits':D.bit_length(),
                    'center':mp.nstr(center,35),'lower':mp.nstr(lower,35),'upper':mp.nstr(upper,35),
                    'width':mp.nstr(mp.log(912*17)/(2*4**r),35)})
        if r<last:
            NN=N**4+16*N*D**3;DD=4*N**3*D-8*D**4
            common=gcd(NN,DD);NN//=common;DD//=common
            if DD<0:NN,DD=-NN,-DD
            Hnext=max(abs(NN),abs(DD))
            assert Hnext<=17*H**4
            assert 912*Hnext>=H**4
            N,D=NN,DD
    return out


def run_checks():
    counts=Counter()
    def check(name,condition):
        assert condition,name
        counts[name]+=1
    X,Z,a,b=sp.symbols('X Z a b')
    delta=a**3-27*b*b
    FF=16*X**4+8*a*X**2*Z**2+32*b*X*Z**3+a*a*Z**4
    GG=64*X**3*Z-16*a*X*Z**3-16*b*Z**4
    c=[256*a**3-6912*b*b,-64*a*a*b,-48*a**4+1408*a*b*b,-48*a**3*b+1536*b**3,
       16*a*a*b,-20*a**4+512*a*b*b,-104*a**3*b+3072*b**3,-3*a**5+96*a*a*b*b]
    d=[0,-12288,0,4096*a,3072,0,1280*a,6912*b]
    d=list(map(sp.sympify,d))
    for vector,target in [(c,X**7),(d,Z**7)]:
        A=sum(vector[i]*X**(3-i)*Z**i for i in range(4))
        B=sum(vector[i+4]*X**(3-i)*Z**i for i in range(4))
        check('bezout_identity',sp.expand(A*FF+B*GG-4096*delta*target)==0)
    check('column_c_integer_norm',sum(abs(v) for t in c for v in sp.Poly(t,a,b).coeffs())==14095)
    check('column_d_integer_norm',sum(abs(v) for t in d for v in sp.Poly(t,a,b).coeffs())==27648)
    check('certificate_degree',max(sp.Poly(t,a,b).total_degree() for t in c+d)<=5)
    f=4*X**3-a*X-b
    check('duplication_identity',sp.expand(FF.subs(Z,1)-(sp.diff(f,X)**2-32*X*f))==0)
    check('singular_case_excluded',FF.subs({a:3,b:1,X:-1,Z:2})==GG.subs({a:3,b:1,X:-1,Z:2})==0)
    # All common factors at finite places are accounted for, not discarded.
    curves=[(F(0),F(8)),(F(4),F(0)),(F(-4),F(0)),(F(1),F(1)),(F(-2),F(3)),(F(1),F(-4)),(F(1,2),F(-3,4))]
    summaries=[]
    for av,bv in curves:
        env={a:sp.Rational(av.numerator,av.denominator),b:sp.Rational(bv.numerator,bv.denominator)}
        ff,gg=FF.subs(env),GG.subs(env)
        fcoef=[F(x) for x in sp.Poly(ff,X,Z).coeffs()]
        gcoef=[F(x) for x in sp.Poly(gg,X,Z).coeffs()]
        cv=[F(x.subs(env)) for x in c];dv=[F(x.subs(env)) for x in d]
        U=max(sum(map(abs,fcoef)),sum(map(abs,gcoef)))/rational_gcd(fcoef+gcoef)
        B=max(sum(map(abs,cv)),sum(map(abs,dv)))/rational_gcd(cv+dv)
        HE=projective_height([1,av,bv])
        check('coefficient_height_upper',U<=96*HE**2)
        check('certificate_height_upper',B<=27648*HE**5)
        for n in range(-5,6):
            for den in range(0,6):
                if gcd(n,den)!=1:continue
                N,D=pair_normalize(ff.subs({X:n,Z:den}),gg.subs({X:n,Z:den}))
                H0=max(abs(n),abs(den));H1=max(abs(N),abs(D))
                check('global_duplication_upper',H1<=U*H0**4)
                check('global_duplication_lower',B*H1>=H0**4)
        summaries.append({'a':str(av),'b':str(bv),'exp_U_E':str(U),'exp_B_E':str(B)})
        if av==0 and bv==8:
            check('example_U_E',U==17)
            check('example_B_E',B==912)
            check('example_certificate_gcd',rational_gcd(cv+dv)==3072)
            check('example_certificate_archimedean',max(sum(map(abs,cv)),sum(map(abs,dv)))==2801664)
    for xv in range(-2,5):
        for yv in range(0,5):
            for av in [-1,0,2]:
                bv=4*xv**3-av*xv-yv*yv
                if av**3==27*bv*bv:continue
                HE=projective_height([1,av,bv]);Hx=projective_height([1,xv]);H3=projective_height([1,xv,yv])
                check('plane_height_upper',H3**2<=6*HE*Hx**3)
                check('plane_height_lower',4*HE*H3**2>=Hx**3)
    check('example_doubled_point',F(-383,500)**2==4*F(129,100)**3-8)
    check('example_projective_height',projective_height([1,F(129,100),F(-383,500)])==645)
    check('example_positive_canonical_height',129**3>912)
    check('uniform_projective_lower_constant',4*96==384)
    check('uniform_projective_upper_constant',6*27648==165888)
    check('quadratic_height_constant',sum(F(14)**r/F(sp.factorial(r)) for r in range(21))>165888)
    data=telescope_data()
    counts['exact_duplication_interval_recurrence']+=2*(len(data)-1)
    return {'exact':{'total':sum(counts.values()),'families':dict(counts),'rational_curve_examples':summaries},
            'numerical':{'precision_decimal_digits':80,'scope':'Display of logarithms of exact integer-recurrence endpoints; interval validity proved symbolically.','telescope':data},
            'scope':'Explicit computed height errors and quadratic multiplication. These constants are not asserted to equal David Lemma3.4 sharper constants.'}


if __name__=='__main__':
    result=run_checks()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'exact':result['exact'],'last_interval':result['numerical']['telescope'][-1]},indent=2))
