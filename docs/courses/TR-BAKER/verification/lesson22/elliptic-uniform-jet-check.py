"""Exact polynomial and arithmetic checks for results22.198--202."""
from pathlib import Path
from collections import Counter
from fractions import Fraction
from math import isqrt, lcm, factorial
import json
import sympy as sp

BASE = Path(__file__).resolve().parent
counts = Counter()

def check(name, value):
    assert value, name
    counts[name] += 1

X, Y, Z, u, v, w, A, B = sp.symbols('X Y Z u v w A B')
TX = -A*u**2*Z**2+A*w**2*X**2-3*B*u*w*Z**2+3*B*w**2*X*Z+2*u*v*Y*Z+u*w*Y**2-v**2*X*Z-2*v*w*X*Y
TY = A*u*v*Z**2-2*A*u*w*Y*Z+2*A*v*w*X*Z-A*w**2*X*Y+3*B*v*w*Z**2-3*B*w**2*Y*Z-3*u**2*X*Y+3*u*v*X**2-v**2*Y*Z+v*w*Y**2
TZ = A*u*w*Z**2-A*w**2*X*Z+3*u**2*X*Z-3*u*w*X**2-v**2*Z**2+w**2*Y**2
T = (TX, TY, TZ)
for f in T:
    check('bidegree_two_two', all(sum(m[:3]) == sum(m[3:]) == 2 for m, _ in sp.Poly(f,X,Y,Z,u,v,w).terms()))
for f, q in zip(T, (u,v,w)):
    check('identity_translation_scalar', sp.expand(f.subs({X:0,Y:1,Z:0})-w*q) == 0)

ring = sp.groebner([Y**2-X**3-A*X-B, v**2-u**3-A*u-B], X,u,Y,v,domain=sp.QQ[A,B])
d = X-u
nx = (Y-v)**2-(X+u)*d**2
aff = [f.subs({Z:1,w:1}) for f in T]
for f, wanted in zip(aff,(d*nx,-Y*d**3+(Y-v)*(X*d**2-nx),d**3)):
    check('chord_formula_polynomial_identity', ring.reduce(sp.expand(f-wanted))[1] == 0)
check('translated_point_on_cubic', ring.reduce(sp.expand(aff[1]**2*aff[2]-aff[0]**3-A*aff[0]*aff[2]**2-B*aff[2]**3))[1] == 0)
for aa, bb in [(0,-2),(-1,0),(1,1),(sp.Rational(2,3),sp.Rational(-5,7)),(-8,17)]:
    mm=max(1,abs(aa),abs(bb))
    for f in T:
        coefficients=sp.Poly(f.subs({A:aa,B:bb}),X,Y,Z,u,v,w).coeffs()
        check('archimedean_coefficient_sum',sum(map(abs,coefficients))<=20*mm)

# Independent chord-law evaluations on rational affine points.
fn = [sp.lambdify((X,Y,Z,u,v,w,A,B),f,modules='sympy') for f in T]
point_count=0
for aa in range(-2,3):
    for uu in range(-2,3):
        for vv in range(-2,3):
            bb=vv*vv-uu**3-aa*uu
            if 4*aa**3+27*bb**2==0:
                continue
            for xx in range(-5,6):
                yy2=xx**3+aa*xx+bb
                if xx==uu or yy2<0 or isqrt(yy2)**2!=yy2:
                    continue
                for yy in sorted({isqrt(yy2),-isqrt(yy2)}):
                    px,py,pz=[sp.Rational(f(xx,yy,1,uu,vv,1,aa,bb)) for f in fn]
                    slope=sp.Rational(yy-vv,xx-uu)
                    expected_x=slope**2-xx-uu
                    expected_y=-yy+slope*(xx-expected_x)
                    check('rational_chord_translation',pz!=0 and px/pz==expected_x and py/pz==expected_y)
                    point_count+=1

R=sp.Rational
check('discriminant_prefactor_positive',R(89,100)*6**12>28)
check('period_height_exponent',R(22,7)/6+R(1,4)<1)
exp_lower=sum(R(60,7)**r/sp.factorial(r) for r in range(31))
check('entire_lift_constant_21',exp_lower>2/R(73,1000)**3)
check('sample_height_constant_48',sum(R(6)**r/sp.factorial(r) for r in range(13))>320)
check('entire_lift_exponent_sum',3+3*R(22,7)+R(60,7)==21)

# An exact first jet with a quadratic additive factor, including its denominators.
t=sp.symbols('t'); order=13
s=sp.Integer(0)
for _ in range(order):
    nxt=sp.series(t**3-2*s**3,t,0,order).removeO()
    if nxt==s:break
    s=nxt
ell_prime=sp.series(1/(1+6*s*s),t,0,order-1).removeO()
ell=sp.integrate(ell_prime,t)
q=(R(3,5),sp.Integer(1),R(1,5))
gg=[sp.expand(f.subs({X:-t,Y:1,Z:-s,u:q[0],v:q[1],w:q[2],A:0,B:-2})) for f in T]
poly=sp.series((1+R(7,3)-R(2,5)*ell)**2*(5*gg[0]-3*gg[1]),t,0,order).removeO()
check('first_jet_constant_vanishes',poly.coeff(t,0)==0)
check('first_jet_exact_value',poly.coeff(t,1)==-R(124,9))
coefficients=[]
for n in range(order):
    delta=1
    for i in range(1,n+1):
        delta=lcm(delta,i)
        for j in range(1,n-i+1):delta=lcm(delta,i*j)
    c=sp.Rational(poly.coeff(t,n)); hc=max(abs(int(c.p)),int(c.q))
    rest=10*6*(35*2)**2*(5**2*2*20)*8**n*delta
    check('formal_coefficient_height_with_denominators',hc**6<=rest**6*2**n)
    coefficients.append({'order':n,'coefficient':str(c),'exp_height':hc,'delta':delta})

torsion=[f.subs({u:0,v:0,w:1,A:-1,B:0}) for f in T]
check('two_torsion_specialization',torsion==[-X**2,X*Y,Y**2+X*Z])
twice=[sp.expand(f.subs({X:torsion[0],Y:torsion[1],Z:torsion[2]},simultaneous=True)) for f in torsion]
for a,b in zip(twice,[-X**4,-X**3*Y,-X**3*Z]):check('two_torsion_involution_identity',a==b)
ss=sp.symbols('s')
local=[sp.expand(f.subs({X:-t,Y:1,Z:-ss})) for f in torsion]
check('two_torsion_local_tuple',local==[-t*t,-t,1+t*ss])
S=2*t**3/(1+sp.sqrt(1+4*t**4))
check('two_torsion_exact_formal_branch',sp.simplify(t*S**2+S-t**3)==0)
xx=-t*t/(1+t*S);yy=-t/(1+t*S)
check('two_torsion_formal_curve_identity',sp.simplify(yy**2-xx**3+xx)==0)
check('two_torsion_tangent',sp.diff(xx,t).subs(t,0)==0 and sp.diff(yy,t).subs(t,0)==-1)

result={'exact':{'total':sum(counts.values()),'families':dict(counts),'rational_translations':point_count,'formal_coefficient_example':coefficients,'entire_lift_exponential_lower':str(exp_lower)},'scope':'Exact identities, rational translations, explicit scalar and constant inequalities, and formal coefficient heights. These are finite checks supporting the written general proof; no full David theorem is claimed.'}
(BASE/'elliptic-uniform-jet-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exact_checks':result['exact']['total'],'families':dict(counts)}))
