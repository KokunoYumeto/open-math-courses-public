"""Exact checks of the displayed identities, not a substitute for their proofs."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib
x,n,a,alpha,xi,eta,zeta=s.symbols('x n a alpha xi eta zeta',real=True)
n=s.symbols('n',positive=True)
rows=[]
def check(name,expr):
 result=s.simplify(expr);assert result==0,(name,result);rows.append({'name':name,'exact':True})
w=x*s.exp(-n*x)
f=-s.diff(w,x,2)+n*n*w
check('Dirichlet model forcing',f-2*n*s.exp(-n*x))
check('Dirichlet boundary value',w.subs(x,0))
check('Dirichlet value norm',s.integrate(w*w,(x,0,s.oo))-1/(4*n**3))
check('Dirichlet normal norm',s.integrate(s.diff(w,x)**2,(x,0,s.oo))-1/(4*n))
check('Dirichlet tangential norm',s.integrate(n*n*w*w,(x,0,s.oo))-1/(4*n))
check('Dirichlet energy pairing',s.integrate(f*w,(x,0,s.oo))-1/(2*n))
check('Forcing negative tangential norm',s.integrate(f*f,(x,0,s.oo))/(1+n*n)-2*n/(1+n*n))
check('Mixed graph norm',s.integrate((1+n*n)*w*w+s.diff(w,x)**2,(x,0,s.oo))-(1/(4*n**3)+1/(2*n)))
S=s.exp(alpha*x/2);v=s.Function('v')(x)
gauge=s.expand((-s.diff(S*v,x,2)+alpha*s.diff(S*v,x)+(1+a)*eta**2*S*v)/S)
check('Complex normal gauge',gauge-(-s.diff(v,x,2)+(1+a)*eta**2*v+alpha**2*v/4))
check('Gauge boundary identity',S.subs(x,0)-1)
check('Gauge inverse identity',S*s.exp(-alpha*x/2)-1)
check('Compressed equator vanishes',(zeta*zeta+x*x*(1+a)*eta*eta).subs({x:0,zeta:0}))
check('Ordinary ellipticity decomposition',xi*xi+(1+a)*eta*eta-(s.Rational(3,4)*(xi*xi+eta*eta)+xi*xi/4+(a+s.Rational(1,4))*eta*eta))
u=s.exp(-n*x)
check('Nonzero value homogeneous equation',-s.diff(u,x,2)+n*n*u)
check('Nonzero boundary value',u.subs(x,0)-1)
check('Nonzero value norm',s.integrate(u*u,(x,0,s.oo))-1/(2*n))
check('Nonzero value energy',s.integrate(s.diff(u,x)**2+n*n*u*u,(x,0,s.oo))-n)
check('Endpoint cancellation',s.diff(u,x).subs(x,0)*u.subs(x,0)+n)
T=s.Function('T')(x)
D=lambda q:-s.I*s.diff(q,x)
check('Second derivative commutator',D(D(T*v))-T*D(D(v))-(2*D(T)*D(v)+D(D(T))*v))
check('Weak normal commutator sign',2*D(T)*D(v)+D(D(T))*v-(D(2*D(T)*v)-D(D(T))*v))
for av in [-s.Rational(1,4),0,s.Rational(1,4)]:
 for tv in [-s.pi/2,0,s.pi/2]:
  xx=s.cos(tv)/s.sqrt(1+av);ss=s.sin(tv)
  check(f'Exact figure level a={av},theta={tv}',ss**2+(1+av)*xx**2-1)
root=Path(__file__).resolve().parent
out={'recorded_utc':datetime.now(timezone.utc).isoformat(),'passed':True,'source_sha256':hashlib.sha256((root/'uniform-dirichlet-estimates-in-the-boundary-elliptic-region.md').read_bytes()).hexdigest(),'total_cases':len(rows),'exact_algebraic_checks':len(rows),'numerical_checks':0,
'cases':rows,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_completeness_inferred_from_checks':False}
(root/'model-check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exact_checks':len(rows)}))
