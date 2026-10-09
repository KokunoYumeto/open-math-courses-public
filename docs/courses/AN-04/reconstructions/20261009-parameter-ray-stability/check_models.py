"""CC0: exact checks of the displayed Hamilton and comparison algebra."""
from pathlib import Path
import hashlib,json
import sympy as S
root=Path(__file__).resolve().parent
s,x,y,t,xi,eta,tau,eps=S.symbols('s x y t xi eta tau eps',real=True)
a,k=S.symbols('a k',positive=True)
p=xi**2+k*x*eta**2-2*tau*eta
curve={x:2*a*s-k*s*s,xi:a-k*s,eta:1,tau:a*a/2,t:-2*s,y:2*k*a*s*s-S.Rational(2,3)*k*k*s**3-a*a*s}
cases=[]
def check(name,left,right=0):
 z=S.simplify(left-right);assert z==0,(name,z)
 cases.append({'name':name,'passed':True})
H=[S.diff(p,xi),S.diff(p,tau),S.diff(p,eta),-S.diff(p,x),-S.diff(p,t),-S.diff(p,y)]
for q,h in zip([x,t,y,xi,tau,eta],H):check('Hamilton equation '+str(q),S.diff(curve[q],s),h.subs(curve))
check('Characteristic identity',p.subs(curve))
L=2*a/k
for name,left,right in [('Initial boundary',curve[x].subs(s,0),0),('Return boundary',curve[x].subs(s,L),0),('Incoming root',curve[xi].subs(s,L),-a),('Outgoing root',curve[xi].subs(s,0),a),('Vertex',S.diff(curve[x],s).subs(s,a/k),0),('Height',curve[x].subs(s,a/k),a*a/k),('Cycle tangential increment',curve[y].subs(s,L),2*a**3/(3*k)),('Observation time',curve[t].subs(s,S.Rational(1,2)),-1),('Compressed wall value',(curve[x]*curve[xi]).subs(s,L),0),('Tangential derivative',S.diff(curve[y],s),2*k*curve[x]-a*a)]:check(name,left,right)
v,h,X,Rx,Rxx,Fgrad=S.symbols('v h X Rx Rxx Fgrad')
check('Normalized characteristic derivative',2*v*(Rx-h*v),2*v*Rx-2*h*v*v)
check('Compressed derivative',2*v*v+X*(Rx-h*v),2*v*v+X*Rx-h*X*v)
check('Normalized energy cancellation',2*v*(Rx-h*v)-2*v*Rx-X*(2*v*Rxx+Fgrad),-2*h*v*v-X*(2*v*Rxx+Fgrad))
C=S.symbols('C',positive=True);M=S.Matrix([[0,2,0],[C,C,C],[C,0,C]])
check('Zero instantaneous position path',S.eye(3)[0,1])
check('One-edge position path',M[0,1],2)
check('Zero one-edge tangential path',M[2,1])
check('Two-edge tangential path',(M*M)[2,1],2*C)
u=S.symbols('u',nonnegative=True)
for power in [0,1,2,3]:
 check('Position moment '+str(power),S.integrate((s-u)*u**power,(u,0,s)),s**(power+2)/((power+1)*(power+2)))
 check('Tangential moment '+str(power),S.integrate((s-u)**2*u**power,(u,0,s)),2*s**(power+3)/((power+1)*(power+2)*(power+3)))
for ee in [S.Rational(-1,4),S.Integer(0),S.Rational(1,4)]:
 kk=1+ee;assert kk>=S.Rational(3,4)
 check('Height bound '+str(ee),S.Rational(4,3)*a*a-a*a/kk,a*a*(S.Rational(4,3)-1/kk))
 assert S.Rational(4,3)-1/kk>=0
q=xi**2+x*eta**2-2*eps*tau*eta;at={x:0,xi:0,tau:0,eta:1}
check('Limiting time field',S.diff(q,tau).subs(at),-2*eps)
check('Limiting second tangential field',S.diff(q,eta).subs(at))
check('Observation delay',(-2*eps*s).subs(s,1/(2*eps)),-1)
b=S.symbols('b',positive=True)
check('Positive-parameter first upper exit',((s-1)**2+b).subs(s,1+S.sqrt(2-b)),2)
check('Limiting lower touch',((s-1)**2).subs(s,1))
check('Upper exit limit',S.limit(1+S.sqrt(2-b),b,0,dir='+'),1+S.sqrt(2))
source=root/'stable-observation-for-boundary-rays.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'passed':True,'total_cases':len(cases),'exact_algebraic_checks':len(cases),'numerical_checks':0,'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),'scope':'Exact Hamilton, normalization, energy cancellation, cooperative matrix paths, forcing moments, period and exit-time identities. Compactness, maximal continuation and access are proved analytically in the lesson.','cases':cases}
(root/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8')
print(json.dumps({key:out[key] for key in ['passed','total_cases','source_sha256']}))
