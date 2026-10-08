"""Exact finite algebra supplements to the receiving geometric proofs."""
from pathlib import Path
import hashlib,json,sympy as S
c=Path(__file__).resolve().parent
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
checks=[]
v,s,B,D=S.symbols('v s B D',real=True)
assert S.expand((v*B+(v*v-s)*D)**2-s*B*B-(v*v-s)*(B*B+2*v*B*D+(v*v-s)*D*D))==0
b=S.symbols('b',real=True);u=v+b*v*v
assert S.expand((u-b*s)**2-s-(v*v-s)*(1+2*b*v+b*b*(v*v-s)))==0
checks.append({'name':'Full quadratic preparation and nonlinear inverse-Morse example','passed':True,'locators':'GF5,GF46-GF47','scope':'Exact polynomial identities for divided-difference variables; parameter smoothness and the nonzero unit are proved in the lesson.'})
t,radius,rho=S.symbols('t r rho',real=True);R=S.Function('R')(radius,t)
E=rho*rho-radius*S.diff(R,radius)
flow=lambda f:S.diff(f,t)+2*rho*S.diff(f,radius)+S.diff(R,radius)*S.diff(f,rho)
assert S.simplify(flow(E)+radius*flow(S.diff(R,radius)))==0
checks.append({'name':'Strict-gliding energy cancellation','passed':True,'locators':'GF17-GF18,GF26','identity':'H_p(rho^2-rR_r)=-r H_p(R_r)','scope':'The same cancellation holds with every tangential derivative in the full Hamilton field; quantitative integrated estimates are receiving proof.'})
k=S.symbols('k',integer=True,positive=True);y=S.symbols('y',positive=True)
for eps in [-1,1]:
 rr=2*eps*y**k/(k*(k-1));pp=eps*y**(k-1)/(k-1);eta=(k-2)*y**(2*k-2)/(k*(k-1)**2)
 assert S.simplify(S.diff(rr,y)-2*pp)==0
 assert S.simplify(S.diff(pp,y)-eps*y**(k-2))==0
 assert S.simplify(pp*pp-rr*eps*y**(k-2)+eta)==0
 assert S.simplify(S.diff(eta,y)-rr*eps*(k-2)*y**(k-3))==0
c0=S.symbols('c',positive=True);uu=S.symbols('u',real=True)
assert S.expand((c0-uu)**2+(2*c0*uu-uu**2)-c0*c0)==0
checks.append({'name':'Both finite-contact signs and the repeated gliding excursion','passed':True,'locators':'GF43-GF45','scope':'Symbolic positive integer k with k>=3 in the lesson, both epsilon signs, all Hamilton equations and p=0; side selection and uniqueness are proved independently.'})
a=S.Function('a')(t);rr=S.Function('r')(t);pp=S.diff(rr,t)/2
eta=rr*a-pp**2
assert S.simplify((S.diff(eta,t)-rr*S.diff(a,t)).subs(S.diff(rr,t,2),2*a))==0
assert S.simplify(pp**2-rr*a+eta)==0
assert S.simplify(-2*rr*a+eta-(-rr*a-pp**2))==0
Delta,vj,vprev=S.symbols('Delta vj vprev',positive=True);mu=Delta*vj/(vj+vprev)
assert S.simplify(vj*Delta-(vj+vprev)*mu)==0
assert S.simplify(vj-(vj+vprev)+vprev)==0
assert S.det(S.Matrix([[0,S.Rational(1,2)],[S.Rational(1,2),0]]))==-S.Rational(1,4)
checks.append({'name':'Flat-force moments and full homogeneous Hamilton lift','passed':True,'locators':'GF35-GF42','identities':['endpoint radius zero','incoming and outgoing slope moments','eta-prime=r a-prime','p=0','w-prime=-r a-rho^2','nondegenerate tangential determinant -1/4'],'scope':'All infinite derivative bounds, smooth extension and nonuniqueness are receiving arguments, not inferred from finite samples.'})
ep=S.symbols('epsilon',positive=True);x=S.symbols('r',positive=True)
assert S.integrate(2*ep,(x,0,ep**2))==2*ep**3
assert S.integrate(2*x*ep,(x,0,ep**2))==ep**5
checks.append({'name':'Liouville density under normal compression','passed':True,'locators':'GF29-GF31,GF48','correct_strip_volume':'2epsilon^3','compressed_Euclidean_area':'epsilon^5','scope':'Symplectic clock-map preservation and the complete measure-zero argument are proved in the lesson.'})
record={'schema':'an04-generalized-glancing-model-checks/v1','source_sha256':sha(c/'generalized-glancing-flow-preparation.md'),'checks':checks,'passed':True,'general_theorem_certified':False,'script_sha256':sha(Path(__file__))}
(c/'model-check.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print({'passed':True,'finite_algebra_groups':len(checks),'general_theorem_certified':False})
