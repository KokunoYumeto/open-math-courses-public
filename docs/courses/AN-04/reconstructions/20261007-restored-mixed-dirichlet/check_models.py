"""Finite exact sign and geometry models, not a certificate of the general proof."""
from pathlib import Path
import datetime,hashlib,json
import sympy as S
r=Path(__file__).resolve().parent;checks=[]
def zero(name,value):
    value=S.simplify(S.expand_complex(value))
    assert value==0,(name,value)
def done(name):checks.append({'name':name,'passed':True,'scope':'Finite model identity only.'})
t,x,y,k,v=S.symbols('t r y k v',real=True)
a,b,c,d,e,f,u0,u1=S.symbols('a b c d e f u0 u1',real=True)
ut,ur,uy=a+S.I*b,c+S.I*d,e+S.I*f
U=u0+S.I*u1
G=S.diag(-1,-1,1);du=S.Matrix([ur,uy,ut]);F=S.Matrix([k,0,1])
quad=(du.T*G*S.conjugate(du))[0]
FU=(F.T*du)[0]
J=2*S.re(G*du*S.conjugate(FU))-F*quad+F*U*S.conjugate(U)
expected=ut*S.conjugate(ut)+ur*S.conjugate(ur)+uy*S.conjugate(uy)+2*k*S.re(ut*S.conjugate(ur))+U*S.conjugate(U)
zero('complex temporal density',J[2]-expected)
zero('zero Dirichlet outward flux',-J[0].subs({a:0,b:0,e:0,f:0,u0:0,u1:0})-k*ur*S.conjugate(ur))
done('Full complex flat temporal density and inward boundary sign')
coords=[x,y,t];w=t*t*x+y**3+S.I*(t*x*x+t*y+x*y*y)
grad=S.Matrix([S.diff(w,z) for z in coords]);Fw=(F.T*grad)[0]
q=(grad.T*G*S.conjugate(grad))[0]
current=2*S.re(G*grad*S.conjugate(Fw))-F*q+F*w*S.conjugate(w)
Lw=S.diff(w,t,2)-S.diff(w,x,2)-S.diff(w,y,2)
zero('constant metric complete divergence',sum(S.diff(current[j],coords[j]) for j in range(3))-2*S.re(Lw*S.conjugate(Fw))-2*S.re(w*S.conjugate(Fw)))
done('Complex polynomial divergence, including the mass contribution')
wall=S.Matrix([[1,-v],[-v,v*v-1]])
inverse=S.Matrix([[1-v*v,-v],[-v,-1]])
assert S.simplify(wall*inverse)==S.eye(2)
zero('wall determinant',wall.det()+1)
ff=S.Matrix([1,k])
zero('wall tangent square',(ff.T*inverse*ff)[0]-(1-(v+k)**2))
zero('normalized wall conormal',wall[1,1]/(1-v*v)+1)
done('Moving-wall matrix, inverse, normalizer and timelike margin')
rho,tau,lamb=S.symbols('rho tau lambda',real=True)
zero('quadratic discriminant',S.discriminant((tau+lamb)**2-rho**2,lamb)-4*rho**2)
aa,bb,zz,tt=S.symbols('a0 b0 Z tau',real=True)
expression=2*(aa*tt-zz)*bb*tt-(tt*tt-rho*rho)*aa*bb
zero('Lorentz flux formula',expression-bb*(aa*(tt*tt+rho*rho)-2*tt*zz))
done('Strict quadratic discriminant and Lorentz flux block')
eta=S.symbols('eta',real=True)
e1=S.sqrt(1+eta*eta)-S.I*tau
zero('mixed multiplier second frequency derivative',S.diff(e1,eta,2).subs(eta,0)-1)
wave=S.exp(-(t-x)**2)
zero('exact incoming boundary wave',S.diff(wave,t,2)-S.diff(wave,x,2))
zero('actual boundary value',wave.subs(x,0)-S.exp(-t*t))
done('One-sided multiplier isotropic distinction and exact boundary-wave equation')
Gv=S.Matrix([[-1-t*t,x*y,t],[x*y,-2-x*x,y],[t,y,3+x*x]])
Fv=S.Matrix([1+x,y-t,2+t+x*x]);Fvw=(Fv.T*grad)[0]
cv=[x+S.I*y,y-S.I*t,t+S.I*x];c0=1+S.I*(x+t)
qv=(grad.T*Gv*S.conjugate(grad))[0]
Jv=2*S.re(Gv*grad*S.conjugate(Fvw))-Fv*qv+Fv*w*S.conjugate(w)
divF=sum(S.diff(Fv[i],coords[i]) for i in range(3))
Lv=sum(Gv[i,j]*S.diff(w,coords[i],coords[j]) for i in range(3) for j in range(3))+sum(cv[i]*grad[i] for i in range(3))+c0*w
Rv=2*S.re(sum(S.diff(Gv[i,j],coords[i])*grad[j]*S.conjugate(Fvw)+Gv[i,j]*grad[j]*S.conjugate(sum(S.diff(Fv[k],coords[i])*grad[k] for k in range(3))) for i in range(3) for j in range(3)))
Rv-=divF*qv+sum(Fv[i]*S.diff(Gv[j,k],coords[i])*grad[j]*S.conjugate(grad[k]) for i in range(3) for j in range(3) for k in range(3))
Rv+=divF*w*S.conjugate(w)+2*S.re(w*S.conjugate(Fvw))-2*S.re((sum(cv[i]*grad[i] for i in range(3))+c0*w)*S.conjugate(Fvw))
zero('variable metric full remainder',sum(S.diff(Jv[i],coords[i]) for i in range(3))-2*S.re(Lv*S.conjugate(Fvw))-Rv)
done('Dense variable coefficient, variable multiplier and complex lower-term remainder')
source=r/'mixed-dirichlet-cauchy-energy-preparation.md'
d={'schema':'an04-mixed-dirichlet-finite-models/v1',
   'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
   'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
   'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
   'checks':checks,'finite_groups':len(checks),'passed':True,'general_theorem_certified':False,
   'scope':'Exact finite symbolic checks of signs and original model formulas. The full general proof requires the author argument and exact programme prerequisites.'}
(r/'model-check.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf8')
print(json.dumps({'passed':True,'finite_groups':len(checks),'general_proof_certificate':False}))
