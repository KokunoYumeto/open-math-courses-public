"""Exact finite models supporting the written fold and glancing proofs."""
from pathlib import Path
import json,hashlib
import sympy as S
ROOT=Path(__file__).resolve().parent
q,y,p,rho,z,lam,s,t,r,c,a,b=S.symbols('q y p rho z lam s t r c a b',real=True)
checks=[]
def check(name,value):
    if isinstance(value,S.MatrixBase):passed=all(S.simplify(x)==0 for x in value)
    else:passed=S.simplify(value)==0
    assert passed,name
    checks.append({'name':name,'passed':True})
def pb(f,g,positions,momenta):
    return S.expand(sum(S.diff(f,pi)*S.diff(g,qi)-S.diff(f,qi)*S.diff(g,pi) for qi,pi in zip(positions,momenta)))
g=p*p-q-rho
check('ordinary first bracket',pb(q,g,[q,y],[p,rho])+2*p)
check('ordinary second q bracket',pb(q,pb(q,g,[q,y],[p,rho]),[q,y],[p,rho])-2)
check('ordinary second g bracket',pb(g,pb(g,q,[q,y],[p,rho]),[q,y],[p,rho])-2)
orbit={q:2*s*t+t*t,p:s+t,y:y-t,rho:s*s}
check('entire ordinary orbit lies on G',g.subs(orbit,simultaneous=True))
check('ordinary normal velocity',S.diff(orbit[q],t)-2*orbit[p])
check('ordinary momentum velocity',S.diff(orbit[p],t)-1)
check('ordinary tangential velocity',S.diff(orbit[y],t)+1)
check('second endpoint q',orbit[q].subs(t,-2*s))
check('second endpoint p',orbit[p].subs(t,-2*s)+s)
check('second endpoint y',orbit[y].subs(t,-2*s)-y-2*s)
W=S.Matrix([[0,-2*p],[2*p,0]])
for name,F in [('F exchange',S.Matrix([y,-p])),('G exchange',S.Matrix([y+2*p,-p]))]:
    J=F.jacobian([y,p]);check(name+' folded form',J.T*W.subs(p,-p)*J-W)
    check(name+' involution',F.subs({y:F[0],p:F[1]},simultaneous=True)-S.Matrix([y,p]))
Q=y+p
check('ordinary transverse invariant',pb(Q,g,[q,y],[p,rho]))
check('ordinary invariant q velocity',pb(Q,q,[q,y],[p,rho])-1)
check('ordinary invariant rho velocity',pb(Q,rho,[q,y],[p,rho])+1)
gh=p*p-q*lam*lam-rho*lam;Qh=y*lam+p
check('homogeneous transverse invariant',pb(Qh,gh,[q,z,y],[p,lam,rho]))
check('homogeneous q velocity',pb(Qh,q,[q,z,y],[p,lam,rho])-1)
check('homogeneous last position velocity',pb(Qh,z,[q,z,y],[p,lam,rho])-y)
check('homogeneous last momentum velocity',pb(Qh,rho,[q,z,y],[p,lam,rho])+lam)
check('homogeneous radius retained',pb(Qh,lam,[q,z,y],[p,lam,rho]))
check('homogeneous normal momentum retained',pb(Qh,p,[q,z,y],[p,lam,rho]))
check('homogeneous base position retained',pb(Qh,y,[q,z,y],[p,lam,rho]))
phi=S.Rational(2,3)*s**3+S.Rational(2,5)*s**5
check('curved fold primitive',S.diff(phi,s)-2*s*s*(1+s*s))
C=1+S.Rational(3,5)*r
v=r*C**S.Rational(2,3)
check('curved base coordinate Jacobian',S.diff(v,r)-(1+r)*C**S.Rational(-1,3))
check('curved cubic potential identity',S.expand(phi**3-S.Rational(8,27)*s**9*(1+S.Rational(3,5)*s*s)**3))
# A nonconstant potential tests the full graph, not only psi=0.
zz,tt=S.symbols('zz tt',real=True)
vv=tt*tt;psi=zz*zz+zz*vv+vv*vv
X=S.Matrix([zz,vv,2*zz+vv,zz+2*vv+tt])
J=X.jacobian([zz,tt]);W4=S.zeros(4)
for k in range(2):W4[k,k+2]=-1;W4[k+2,k]=1
check('nonconstant potential Lagrangian pullback',J.T*W4*J)
check('fold embedding normal derivative',J[:,1].subs(tt,0)-S.Matrix([0,0,0,1]))
D=S.zeros(4);D[0,3]=-c;D[3,0]=c
A=W4.inv()*D
check('glancing form perturbation nilpotence',A*A)
check('whole linear form homotopy determinant',(W4+t*D).det()-W4.det())
check('whole linear form homotopy inverse',(W4+t*D)*(S.eye(4)-t*A)*W4.inv()-S.eye(4))
check('relative primitive exterior derivative',S.diff(c*a/2,a)-S.diff(-c*b/2,b)-c)
sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
record={'passed':True,'exact_checks':len(checks),'checks':checks,
 'source':'folded-lagrangians-and-glancing-pairs.md',
 'source_sha256':sha(ROOT/'folded-lagrangians-and-glancing-pairs.md'),
 'script_sha256':sha(Path(__file__)),
 'scope':'Exact finite coordinate models and matrix identities. General smooth normal forms, relative homotopy, common flow domains and source comparisons are written proofs, not consequences of these checks.',
 'human_or_independent_review_claimed':False}
(ROOT/'model-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print({'passed':True,'exact_checks':len(checks)})
