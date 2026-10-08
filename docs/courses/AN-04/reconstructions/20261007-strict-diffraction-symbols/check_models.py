"""Symbolic and exact finite checks supplementing the complete symbol proofs."""
from pathlib import Path
from itertools import product
import hashlib,json
import sympy as S
HERE=Path(__file__).resolve().parent
groups=[]
t,r,a,b,m,d=S.symbols('t r a b M delta',real=True)
gap=5*t*t-t+S.Rational(1,4)
assert S.expand(gap-(5*(t-S.Rational(1,10))**2+S.Rational(1,5)))==0
assert S.diff(gap,t).subs(t,S.Rational(1,10))==0
for value in [S.Rational(k,10) for k in range(-20,21)]:
    assert gap.subs(t,value)>=S.Rational(1,5)
groups.append({'name':'DS36 exact completion and minimum','cases':43})
ratio=(a/d**2+(m-b)/d)/(2*(a/d-m))
assert S.simplify(ratio-(1/(2*d)+(2*m-b)/(2*(a-m*d))))==0
count=1
for av,mv,bv in product([S.Rational(1,2),S.Integer(1),S.Integer(3)],
                        [S.Integer(0),S.Integer(1),S.Integer(7)],
                        [S.Integer(-2),S.Integer(0),S.Integer(5)]):
    dv=av/(128*(1+2*mv+abs(bv)))
    q=ratio.subs({a:av,m:mv,b:bv})
    assert q.subs(d,dv/2)>q.subs(d,dv)
    assert av/dv-mv>0
    count+=1
q=ratio.subs({a:1,m:1,b:0})
assert q.subs(d,S.Rational(1,32))==S.Rational(528,31)
assert q.subs(d,S.Rational(1,64))==S.Rational(2080,63)
assert S.Rational(2080,63)-S.Rational(528,31)==S.Rational(31216,1953)
groups.append({'name':'DS32–DS33 two-width row independence','cases':count+3})
# Verify the Hamilton identity for an arbitrary smooth tangential symbol in dimension two.
x,z,xi,ze=S.symbols('x z xi zeta',real=True)
rr=S.Function('r')(x,z,ze)
ww=S.Function('w')(x,z,ze)
lam=S.Function('lambda')(ze)
p=xi**2-rr
phi=ww+xi/lam
hp=lambda f:S.diff(p,xi)*S.diff(f,x)-S.diff(p,x)*S.diff(f,xi)+S.diff(p,ze)*S.diff(f,z)-S.diff(p,z)*S.diff(f,ze)
bracket=lambda f,g:S.diff(f,ze)*S.diff(g,z)-S.diff(f,z)*S.diff(g,ze)
expected=xi*(2*S.diff(ww,x)-bracket(rr,1/lam))+S.diff(rr,x)/lam-bracket(rr,ww)
assert S.simplify(hp(phi)-expected)==0
groups.append({'name':'DS25 variable tangential Hamilton identity','cases':1})
# The scalar square used in DS15 is valid for every positive rational a tested.
count=0
for av,tv in product([S.Rational(1,16),S.Rational(1,4),S.Integer(1),S.Integer(4)],
                     [S.Rational(k,4) for k in range(-12,13)]):
    assert abs(tv)/(tv*tv+av)<=1/(2*S.sqrt(av))
    count+=1
groups.append({'name':'DS15 negative-root quadratic domination','cases':count})
# A concrete primitive with power-flat derivative checks the quotient parity numerically
# through an exact polynomial case away from zeros; smooth flat gluing is proved in S1–S2.
s,c=S.symbols('s c',real=True)
primitive=lambda u:u+u**3/S.Integer(3)
quot=S.cancel((primitive(c+s)-primitive(c-s))/(2*s))
assert S.expand(quot-(1+c*c+s*s/3))==0
assert S.simplify(quot.subs(s,-s)-quot)==0
groups.append({'name':'DS5–DS6 exact even averaged derivative','cases':2})
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
j={'passed':True,'groups':groups,'total_cases':sum(g['cases'] for g in groups),
   'source_sha256':sha(HERE/'characteristic-squares-and-diffractive-commutants.md'),
   'script_sha256':sha(Path(__file__)),'finite_checks_do_not_replace_proofs':True,
   'strict_diffraction_propagation_proved':False}
(HERE/'model-check.json').write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(j,ensure_ascii=False))
