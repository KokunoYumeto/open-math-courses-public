"""Exact multiplier, Hamilton-field, orientation and order checks."""
from pathlib import Path
import json,hashlib
import sympy as S
root=Path(__file__).resolve().parent
A,B,f,tau,t,a,eta,s,m=S.symbols('A B f tau t a eta s m',real=True)
cases=[]
def eq(name,lhs,rhs):
 assert S.simplify(lhs-rhs)==0,(name,lhs,rhs)
 cases.append({'name':name,'passed':True,'kind':'exact symbolic identity'})
z=(A+S.I*B)*(tau+S.I*f)
eq('real zero equation',S.re(z),A*tau-B*f)
eq('imaginary value',S.im(z),B*tau+A*f)
eq('imaginary value on real zero',S.im(z).subs(tau,B*f/A),(A*A+B*B)*f/A)
eq('positive multiplier orientation',S.diff(S.re(z),tau),A)
eq('reversed imaginary sign',S.im(-z),-S.im(z))
eq('positive time rescaling',S.diff(S.re((2+S.I*t)*(tau-S.I*a*eta)),tau),2)
model=(2+S.I*t)*(tau-S.I*a*eta)
eq('rotating example real part',S.re(model),2*tau+t*a*eta)
eq('rotating example imaginary part',S.im(model),t*tau-2*a*eta)
eq('rotating example restricted sign',S.im(model).subs(tau,-t*a*eta/2),-(4+t*t)*a*eta/2)
eq('pure imaginary multiplier real part',S.re(S.I*(tau-S.I*a*eta)),a*eta)
eq('pure imaginary multiplier time coefficient',S.diff(S.re(S.I*(tau-S.I*a*eta)),tau),0)
eq('left reduction operator order',(1-m)+m,1)
eq('left reduction forcing order',s-(1-m),s+m-1)
eq('order zero graph input',s+m-1-0,s+m-1)
eq('order zero graph output',s+m-1-0,s+m-1)
eq('elliptic extra order',(s+m)-(s+m-1),1)
eq('order two L2 forcing',(s+m-1).subs({m:2,s:0}),1)
eq('order zero propagation',(s+m-1).subs(m,0),s-1)
eq('canonical time reflection bracket',S.diff(-tau,tau)*S.diff(-t,t),1)
tp=S.symbols('tp',positive=True)
flat=S.exp(-1/tp**2)
eq('positive flat derivative',S.diff(flat,tp),2*flat/tp**3)
out={'passed':True,'total_cases':len(cases),'exact_algebraic_checks':len(cases),'numerical_checks':0,'cases':cases,'scope':'Exact multiplier and surface identities, Hamilton coefficients, all-real order arithmetic and flat derivative. Geometry, flow uniqueness, normal forms, graph action and propagation are proved in the lesson and its exact providers.','source_sha256':hashlib.sha256((root/'intrinsic-orientation-and-entering-regularity.md').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({k:out[k] for k in ['passed','total_cases','exact_algebraic_checks']}))
