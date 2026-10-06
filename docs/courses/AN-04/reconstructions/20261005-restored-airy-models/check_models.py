"""Six bounded independent checks for U020; not a certification of the analytic proofs."""
import hashlib
import json
import math
from pathlib import Path
import numpy as np
import scipy.integrate as integrate
import scipy.special as special
import sympy as sp

here=Path(__file__).resolve().parent
name='airy-functions-and-fold-model-operators.md'; lesson=here/name
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def cq(fun):
    real,er=integrate.quad(lambda t:float(np.real(fun(t))),-np.inf,np.inf,epsabs=2e-10,epsrel=2e-10,limit=350)
    imag,ei=integrate.quad(lambda t:float(np.imag(fun(t))),-np.inf,np.inf,epsabs=2e-10,epsrel=2e-10,limit=350)
    return real+1j*imag,max(er,ei)

x=sp.symbols('x',real=True)
polys=[(sp.Integer(1),sp.Integer(0))]
for k in range(6):
    a,b=polys[-1];polys.append((sp.diff(a,x)+x*b,a+sp.diff(b,x)))
def airy_k(r,k):
    ai,aip,_,_=special.airy(r);a,b=polys[k]
    return float(a.subs(x,r))*ai+float(b.subs(x,r))*aip

rows=[]
contour=[]
for r in [-3.,0.,2.]:
    for k in range(6):
        height=1.1
        value,err=cq(lambda t:(1j*(t+1j*height))**k*np.exp(1j*((t+1j*height)**3/3+r*(t+1j*height)))/(2*np.pi))
        expected=airy_k(r,k)
        assert abs(value-expected)<2e-8
        contour.append({'r':r,'derivative':k,'error':abs(value-expected),'quadrature_error_estimate':err})
rows.append({'name':'Gaussian contour versus independent Airy implementation and ODE derivatives','passed':True,'samples':contour})

asymptotic=[]
for k in range(4):
    for R in [10.,20.,40.]:
        leading=math.pi**-.5*R**(k/2-.25)*math.cos(2*R**1.5/3-math.pi/4-k*math.pi/2)
        error=abs(airy_k(-R,k)-leading)
        scaled=error/R**(k/2-1.75)
        assert scaled<3
        asymptotic.append({'k':k,'R':R,'scaled_error':scaled})
rows.append({'name':'Both stationary phases, derivative signs and predicted remainder powers','passed':True,'samples':asymptotic,'guard':'Finite samples only; all-ray bounds are analytic proofs.'})

rho=1.4;xi1=.9;height=.85
r=-xi1*rho**(-1/3)
mom=[]
for degree in [0,1]:
    value,err=cq(lambda t:(-rho**(-1/3)*(t+1j*height))**degree*rho**(-1/3)*np.exp(1j*((t+1j*height)**3/3+r*(t+1j*height))))
    expected=2*np.pi*(rho**(-1/3)*special.airy(r)[0] if degree==0 else 1j*rho**(-2/3)*special.airy(r)[1])
    assert abs(value-expected)<2e-8
    mom.append({'degree':degree,'error':abs(value-expected),'quadrature_error_estimate':err})
b0=1.2-.3j;b1=.7+.2j
value,err=cq(lambda t:(rho**(1/3)*b0-1j*(-rho**(-1/3)*(t+1j*height))*rho**(2/3)*b1)*rho**(-1/3)*np.exp(1j*((t+1j*height)**3/3+r*(t+1j*height))))
expected=2*np.pi*(special.airy(r)[0]*b0+special.airy(r)[1]*b1)
assert abs(value-expected)<2e-8
rows.append({'name':'Cubic Fourier moments, negative-i coefficient and full 2pi normalization','passed':True,'moments':mom,'combined_error':abs(value-expected)})

s,z=sp.symbols('s z',real=True)
P=lambda a:sp.factor(-sp.diff(a/(sp.I*(z-s*s)),s))
amp=1+2*s
tail=[]
for N in range(1,6):
    amp=P(amp)
    for p in range(3):
        for gamma in range(3):
            expression=sp.factor(sp.diff(amp,s,p,z,gamma))
            if expression==0: continue
            numerator,denominator=sp.fraction(expression)
            degree=sp.degree(numerator,s)-sp.degree(denominator,s)
            assert degree<=1-3*N-p
            tail.append({'iterations':N,'s_derivatives':p,'angular_derivatives':gamma,'degree_at_infinity':int(degree)})
rows.append({'name':'Five exact transpose-field iterates with mixed derivatives and noncompact weights','passed':True,'frequency_power':'Each normalized transpose contributes rho^-1.','samples':tail})

u,v=sp.symbols('u v',positive=True)
argument=-u*v**(-sp.Rational(1,3)); chains=[]
for a in range(5):
    for b in range(5-a):
        if a+b==0:continue
        d=sp.diff(argument,u,a,v,b)
        assert sp.simplify(u*sp.diff(d,u)+v*sp.diff(d,v)-(sp.Rational(2,3)-a-b)*d)==0
        chains.append({'xi1_derivatives':a,'rho_derivatives':b,'homogeneous_degree':str(sp.Rational(2,3)-a-b)})
counter=[]
for j in [5,10,20]:
    value_rho=1.5*(.75*np.pi+2*np.pi*j)
    derivative=-value_rho**(-1/3)*special.airy(-value_rho**(2/3))[1]
    scaled=-derivative*value_rho**(1/6)
    assert abs(scaled-math.pi**-.5)<.01
    counter.append({'j':j,'rho':value_rho,'scaled_derivative':scaled,'rho_times_absolute_derivative':value_rho*abs(derivative)})
square=sp.symbols('square',positive=True)
sheet=(1+s/sp.sqrt(square))/2
assert sheet.subs({s:-1,square:1})==0
transverse=sp.diff(sheet,square).subs({s:-1,square:1})
assert transverse==sp.Rational(1,4)
rows.append({'name':'Argument homogeneity, ordinary-symbol counterexample and reflected-sheet support guard','passed':True,'chain_samples':chains,'counterexample_samples':counter,
             'sheet_guard':{'critical_value':0,'off_critical_square_derivative':'1/4','implication':'Leading cancellation alone does not exclude lower-order reflected-sheet wavefront; use one symmetric support neighborhood.'}})

orders=[]
for m in [sp.Rational(-2,3),sp.Rational(-1,6),sp.Rational(1,2)]:
    o0=m+sp.Rational(1,6);o1=m-sp.Rational(1,6);mu=m+sp.Rational(1,2)
    assert o0+sp.Rational(1,3)==mu==o1+sp.Rational(2,3)
    assert mu-1==m-sp.Rational(1,2)
    for beta in range(5):
        M=5;N=max(beta+1,int(sp.ceiling(mu+M+beta)))
        assert 3*N>2+3*beta and mu-N<=-M-beta
        orders.append({'m':str(m),'beta':beta,'N':N,'s_weight':1-3*N+3*beta,'rho_order':str(mu-N)})
assert sp.simplify((2*sp.pi)**(-sp.Rational(5,2))*2*sp.pi-(2*sp.pi)**(-sp.Rational(3,2)))==0
assert sp.simplify(-sp.I*sp.I)==1
rows.append({'name':'Exact coefficient and homogeneous orders, all differentiated-tail choices and Fourier factors','passed':True,'samples':orders})

report={'schema':'bounded-airy-model-self-check/v1','lesson':name,'lesson_sha256':sha(lesson),'script_sha256':sha(Path(__file__)),
        'passed':all(r['passed'] for r in rows),'checks':rows,
        'scope':'Six bounded checks complement author proofs; not arbitrary-symbol representation, global analytic or independent mathematical certification.'}
(here/'model-check.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'passed':report['passed'],'checks':len(rows),'lesson_sha256':report['lesson_sha256'],'max_contour_error':max(r['error'] for r in contour)}))
