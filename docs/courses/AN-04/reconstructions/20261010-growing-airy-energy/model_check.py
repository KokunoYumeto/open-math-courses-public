"""Exact checks for the weighted estimates; not a substitute for the proof."""
from pathlib import Path
import json,hashlib
import sympy as s
HERE=Path(__file__).resolve().parent
lam,b,q,t,m,c,C,K,v,d,z,ss,a0=s.symbols('lam b q t m c C K v d z ss a0',positive=True)
checks=[]
def eq(name,a,b=0):
 r=s.simplify(a-b);assert r==0,(name,r)
 checks.append({'name':name,'passed':True,'exact_residual':str(r)})
k=lam**s.Rational(2,3)
eq('boundary variable qk',s.diff(q*k,q),k)
eq('frequency-to-normal relation',-(-v*k)/k,v)
eq('oscillatory lower margin',(c-1/K).subs(K,8/c),7*c/8)
eq('convex phase domain margin',(c-2/K).subs(K,8/c),3*c/4)
eq('oscillatory value order after energy weight',1-s.Rational(5,6),s.Rational(1,6))
eq('oscillatory lambda cancellation',s.Rational(1,6)-s.Rational(2,3)/4)
eq('integrated square of normal majorant',s.integrate(q**(-s.Rational(1,2)),(q,0,C)),2*s.sqrt(C))
eq('layer frequency power',2-s.Rational(2,3),s.Rational(4,3))
eq('near-boundary Airy weight power',-s.Rational(1,2)-s.Rational(1,2),-1)
eq('value boundary ratio lambda power',1-s.Rational(4,3),-s.Rational(1,3))
eq('conormal boundary ratio lambda power',s.Rational(1,3)-s.Rational(4,3),-1)
eq('largest b value boundary ratio',s.simplify(lam**(-s.Rational(1,3))*s.sqrt(k)),1)
eq('largest b conormal boundary ratio',lam**(-1)*k**s.Rational(3,2),1)
eq('conormal graph Sobolev shift',s.Rational(1,6)-s.Rational(2,3),-s.Rational(1,2))
eq('flat angular order gain',(-k*z/k)**4,z**4)
eq('Airy exponential derivative',s.diff(s.Rational(2,3)*t**s.Rational(3,2),t),s.sqrt(t))
eq('squared Airy exponential derivative',s.diff(s.Rational(4,3)*t**s.Rational(3,2),t),2*s.sqrt(t))
dens=2*m*s.exp(-2*m*q)
eq('unit normal column mass',s.integrate(dens,(q,0,s.oo)),1)
eq('density maximizing frequency',s.diff(dens,m).subs(m,1/(2*q)))
eq('pointwise envelope at maximizer',dens.subs(m,1/(2*q)),1/(s.E*q))
eq('endpoint density at m1',dens.subs(m,1),2*s.exp(-2*q))
eq('envelope matching value',(1/(s.E*q)-2*s.exp(-2*q)).subs(q,s.Rational(1,2)))
eps=s.symbols('eps',positive=True)
expr=s.Rational(2,3)/eps*(a0**s.Rational(3,2)-(a0-ss*eps)**s.Rational(3,2))
eq('elliptic scaled exponent limit',s.limit(expr,eps,0),s.sqrt(a0)*ss)
eq('boundary-layer inverse width',k*s.sqrt(a0*k),s.sqrt(a0)*lam)
eq('positive endpoint energy prefactor',(lam**2/k)/(2*s.pi*b),lam**s.Rational(4,3)/(2*s.pi*b))
eq('fixed elliptic power',(lam**s.Rational(4,3)/(2*s.pi*b)).subs(b,a0*k),lam**s.Rational(2,3)/(2*s.pi*a0))
A,B,Ap,Bp,cc,cb=s.symbols('A B Ap Bp cc cb',nonzero=True)
F=cc*(A-s.I*B);Fb=cb*(A+s.I*B)
eq('exact growing basis decomposition',(Fb/cb-F/cc)/(2*s.I),B)
eq('exact growing derivative decomposition',(cb*(Ap+s.I*Bp)/cb-cc*(Ap-s.I*Bp)/cc)/(2*s.I),Bp)
eq('normal conormal row sign',-s.I*(-k),s.I*k)
nu,R,f,n,bulk,form=s.symbols('nu R f n bulk form')
eq('weak Green sign after conormal substitution',(bulk-s.I*(n-R*f))-s.I*R*f,bulk-s.I*n)
g,h,B0,B1,B2,th,gg,hh,zz=s.symbols('g h B0 B1 B2 th gg hh zz')
direct=s.I*th*(g*B0+s.I*h*B1)+gg*B0+g*B1*zz+s.I*hh*B1+s.I*h*B2*zz
expanded=(s.I*th*g+gg)*B0+(-th*h+s.I*hh+g*zz)*B1+s.I*h*zz*B2
eq('full normal derivative amplitude',direct,expanded)
eq('first illustrative cutoff at b0',(8*s.sqrt(1+b*b)).subs(b,0),8)
eq('outer illustrative cutoff at b0',(16*s.sqrt(1+b*b)).subs(b,0),16)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=HERE/'weighted-energy-bounds-for-the-growing-airy-kernel.md'
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,
 'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
 'scope':'Exact cutoff margins, frequency powers, boundary trace powers, unit column mass and its nonintegrable envelope, elliptic asymptotic constants, full derivative and Green signs. Analytic estimates remain in the lesson.',
 'checks':checks}
(HERE/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
