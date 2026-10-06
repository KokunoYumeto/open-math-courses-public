"""Six bounded exact/numerical U024 checks; arbitrary smooth equivalence is a written proof."""
import hashlib,json
from pathlib import Path
import numpy as np
import sympy as s
c=Path(__file__).resolve().parents[1];checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

a,b,z1,z2,v1,v2,t=s.symbols('a b z1 z2 v1 v2 t',real=True)
shift=s.Matrix([a*a,a*b]);z=s.Matrix([z1,z2]);v=s.Matrix([v1,v2]);vv=z-shift
f=vv[0]**2/2-vv[1]**2+(a+b)*vv[0]**3+(1+a*a)*vv[0]*vv[1]**2+vv[1]**4
critical=dict(zip(z,shift));assert s.Matrix([s.diff(f,q) for q in z]).subs(critical,simultaneous=True)==s.zeros(2,1)
along=dict(zip(z,shift+t*v));H=s.hessian(f,z)
A=H.subs(along,simultaneous=True).applyfunc(lambda e:2*s.integrate((1-t)*e,(t,0,1)))
expected=s.expand(f.subs(dict(zip(z,shift+v)),simultaneous=True)-f.subs(critical,simultaneous=True))
assert s.simplify((v.T*A*v)[0]/2-expected)==0
assert A==A.T and A.subs({v1:0,v2:0})==s.diag(1,-2)
assert s.simplify((v.T*(A/2)*v)[0]/2-expected/2)==0
d1=A[0,0];l=A[1,0]/d1;d2=s.simplify(A[1,1]-A[1,0]**2/d1)
L=s.Matrix([[1,0],[l,1]]);D=s.diag(d1,d2);B=s.diag(s.sqrt(d1),s.sqrt(-d2))*L.T
assert s.simplify(L*D*L.T-A)==s.zeros(2)
assert s.simplify(B.T*s.diag(1,-1)*B-A)==s.zeros(2)
Z=B*v;assert s.simplify((Z.T*s.diag(1,-1)*Z)[0]/2-expected)==0
assert Z.jacobian(v).subs({v1:0,v2:0}).det()==s.sqrt(2)
checks.append({'name':'Taylor integral factor and full nonlinear indefinite matrix change','passed':True,
 'critical_point':['a^2','a*b'],'marked_Hessian':[1,-2],
 'parameter_coordinate_determinant':'sqrt(2)',
 'scope':'Actual polynomial with parameter-dependent critical shift, exact Taylor integral, nonconstant LDL congruence and local coordinate derivative; signs fixed on a neighborhood of v=0.'})

rank_models=[]
for n,k,N in [(2,1,1),(2,1,3),(2,2,4),(3,2,5),(3,3,4),(4,3,6)]:
    x=s.symbols('x0:'+str(n));eta=s.symbols('e0:'+str(k));zz=s.symbols('z0:'+str(N-k))
    theta=s.Matrix([*eta,*zz]);ambient=s.Matrix([*x,*theta]);signs=[1 if j%2==0 else -1 for j in range(N-k)]
    psi=sum(x[n-k+j]*eta[j] for j in range(k))
    if n>k:psi+=x[0]**2*eta[0]
    phase=psi+sum(signs[j]*zz[j]**2 for j in range(N-k))/(2*eta[0])
    point={**{q:0 for q in ambient},eta[0]:1}
    gradient=s.Matrix([s.diff(phase,q) for q in theta]);M=gradient.jacobian(ambient).subs(point,simultaneous=True)
    assert M.rank()==N
    critical_tangent=s.Matrix.hstack(*M.nullspace())
    critical_map=s.Matrix([*x,*[s.diff(phase,q) for q in x]])
    tangent=critical_map.jacobian(ambient).subs(point,simultaneous=True)*critical_tangent
    assert tangent.rank()==n and tangent[:n,:].rank()==n-k
    Hess=s.hessian(phase,theta).subs(point,simultaneous=True)
    assert Hess==s.diag(*([0]*k+signs)) and len(Hess.nullspace())==k
    rank_models.append({'n':n,'N':N,'k':k,'critical_equation_rank':N,'critical_map_rank':n,
      'base_projection_rank':n-k,'fiber_Hessian_rank':N-k,'signature':sum(signs)})
checks.append({'name':'actual phase equations, critical maps and fiber Hessian nullity','passed':True,'models':rank_models,
 'scope':'Six complete phase/critical-map tangent models, including a curved base graph and empty quadratic block; not a general smooth rank certification.'})

x1,x2,p,q,tt=s.symbols('x1 x2 p q t',real=True);eta=s.Matrix([p,q]);v=q/p
S=-q**3/(3*p*p)-q**4/(4*p**3);psi=x1*p+x2*q+S
g=s.Matrix([-s.diff(S,p),-s.diff(S,q)]);u=s.Matrix([x1,x2])-g
B=s.diag(p/2,0);G=(u.T*B*u)[0];F=psi+tt*G
T=s.Matrix(2,2,lambda j,l:sum(u[m]*s.diff(B[m,l],eta[j]) for m in range(2)))
C=s.eye(2)+tt*(-2*g.jacobian(eta).T*B+T)
grad=s.Matrix([s.diff(F,e) for e in eta])
assert s.simplify(grad-C*u)==s.zeros(2,1)
marked={x1:0,x2:0,p:1,q:0};assert C.subs(marked,simultaneous=True)==s.eye(2)
assert g.jacobian(eta).subs({p:1,q:0})==s.zeros(2)
assert g.jacobian(eta).subs({p:2,q:s.Rational(1,4)}).rank()==1
V=-C.T.inv()*B*u
assert s.simplify(G+(grad.T*V)[0])==0
assert s.simplify(V.jacobian(eta)*eta-V)==s.zeros(2,1)
on_graph={x1:g[0],x2:g[1]}
assert s.simplify(V.subs(on_graph,simultaneous=True))==s.zeros(2,1)
assert s.simplify(s.Matrix([s.diff(F,x1),s.diff(F,x2)]).subs(on_graph,simultaneous=True)-eta)==s.zeros(2,1)
assert grad.jacobian(s.Matrix([x1,x2,p,q])).subs(marked,simultaneous=True).rank()==2
r=s.symbols('r',positive=True);delta=s.Rational(3,2)*x1+x1*x1*(x2**3-2*x2)
Dt=1+tt*delta;flow=r/Dt;radialV=-r*delta/Dt
assert s.simplify(s.diff(flow,tt)-radialV.subs(r,flow))==0
assert s.simplify((r*x1*Dt).subs(r,flow)-r*x1)==0
assert flow.subs(x1,0)==r
checks.append({'name':'varying-rank minimal homotopy and independently differentiated exact radial flow','passed':True,
 'cusp':'g=(-2v^3/3-3v^4/4,v^2+v^3), v=q/p',
 'scope':'Full rational C_t and vertical field, exact cancellation, Euler degree, critical fixation, covectors and nondegeneracy; nonzero nearby g_eta. A separate conormal flow is solved and differentiated exactly. Domains retain p>0 and invertible C_t.'})

z,w=s.symbols('z w',real=True);D=s.symbols('D',positive=True);theta=s.Matrix([r,z,w])
phase=x1*r*D+z*z/r-w*w/(2*r);target=x1*r+z*z/r-w*w/(2*r)
old=s.Matrix([r/D,z/s.sqrt(D),w/s.sqrt(D)]);sub=dict(zip(theta,old))
assert s.simplify(phase.subs(sub,simultaneous=True)-target)==0
inverse=s.Matrix([r*D,z*s.sqrt(D),w*s.sqrt(D)])
assert s.simplify(inverse.subs(sub,simultaneous=True)-theta)==s.zeros(3,1)
assert s.simplify(old.subs(dict(zip(theta,inverse)),simultaneous=True)-theta)==s.zeros(3,1)
assert s.simplify(old.jacobian(theta)*theta-old)==s.zeros(3,1)
assert old.jacobian(theta).det()==D**(-2)
wrong={r:r/D,z:z*s.sqrt(D),w:w*s.sqrt(D)}
assert s.simplify(phase.subs(wrong,simultaneous=True)-target-(D*D-1)*(z*z-w*w/2)/r)==0
actualD=1+delta;actual=phase.subs(D,actualD);critical={x1:0,z:0,w:0}
H=s.hessian(actual,theta).subs(critical,simultaneous=True);assert H==s.diag(0,2/r,-1/r)
plus=actual+ w*w/r;assert s.hessian(plus,theta).subs(critical,simultaneous=True)==s.diag(0,2/r,1/r)
amplitude=r**s.Rational(-1,2)*(1+x2*x2)*s.exp(-(z*z+w*w)/(r*r))
transformed=amplitude.subs(sub,simultaneous=True)*D**(-2)
expected=r**s.Rational(-1,2)*D**s.Rational(-3,2)*(1+x2*x2)*s.exp(-D*(z*z+w*w)/(r*r))
assert s.simplify(transformed-expected)==0
actual_b=expected.subs(D,actualD)
for base_derivative,frequency_derivative,degree in [(0,[],s.Rational(-1,2)),(1,[r,z],s.Rational(-5,2)),(2,[z,w,r],s.Rational(-7,2))]:
    e=s.diff(actual_b,x1,base_derivative)
    for frequency in frequency_derivative:e=s.diff(e,frequency)
    assert s.simplify(sum(v*s.diff(e,v) for v in theta)-degree*e)==0
checks.append({'name':'complete homogeneous map, two-sided inverse, radius defect and mixed amplitude degrees','passed':True,
 'phase_variable_determinant':'D^(-2)','unequal_signatures':[0,2],
 'scope':'Exact full three-variable map, wrong square-root coefficient D^2, opposite Hessian signature, and nonconstant amplitude with base/frequency mixed derivatives; D>0 and compact angular/base domains explicit.'})

stable=[]
for k,sign1,sign2 in [(1,[],[]),(1,[],[1]),(2,[1,1],[1,-1,-1]),(3,[1,-1],[-1]),(2,[-1],[-1])]:
    b1=len(sign1);b2=len(sign2);N=k+b1+b2
    ee=s.symbols('e0:'+str(k));zz=s.symbols('z0:'+str(b1));ww=s.symbols('w0:'+str(b2));x=s.symbols('x0:'+str(k))
    variables=s.Matrix([*ee,*zz,*ww]);first=sum(x[j]*ee[j] for j in range(k))
    first+=(sum(sign1[j]*zz[j]**2 for j in range(b1))+sum(sign2[j]*ww[j]**2 for j in range(b2)))/(2*ee[0])
    perm=[*range(k),*range(k+b1,N),*range(k,k+b1)]
    second_variables=s.Matrix([variables[j] for j in perm]);second=sum(x[j]*second_variables[j] for j in range(k))
    second+=(sum(sign2[j]*second_variables[k+j]**2 for j in range(b2))+sum(sign1[j]*second_variables[k+b2+j]**2 for j in range(b1)))/(2*second_variables[0])
    assert s.simplify(first-second)==0 and abs(second_variables.jacobian(variables).det())==1
    marked={**{v:0 for v in [*x,*variables]},ee[0]:1}
    grad=s.Matrix([s.diff(first,v) for v in variables]);assert grad.jacobian(s.Matrix([*x,*variables])).subs(marked,simultaneous=True).rank()==N
    H=s.hessian(first,variables).subs(marked,simultaneous=True);assert H==s.diag(*([0]*k+sign1+sign2))
    stable.append({'k':k,'original_N':[k+b1,k+b2],'stabilized_N':N,'combined_signature':sum(sign1+sign2),
      'full_phase_block_permutation':[i+1 for i in perm],'absolute_permutation_Jacobian':1})
checks.append({'name':'actual stable phases and full block permutations including empty blocks','passed':True,'models':stable,
 'scope':'Five exact stabilized phases, full variable maps, nondegenerate equations and Hessian signs; not just numerical dimension/signature counts.'})

# Independent quadratures in source and target boxes at a fixed nonlinear base point.
base_x1=1/5;base_x2=1/3;D0=float(s.Rational(1721,1350));nodes,weights=np.polynomial.legendre.leggauss(32)
def integrate(bounds,which):
    axes=[(hi+lo)/2+(hi-lo)*nodes/2 for lo,hi in bounds]
    ws=[(hi-lo)*weights/2 for lo,hi in bounds]
    rr,zz,ww=np.meshgrid(*axes,indexing='ij');W=ws[0][:,None,None]*ws[1][None,:,None]*ws[2][None,None,:]
    if which=='source':
        value=np.exp(1j*(base_x1*rr*D0+zz*zz/rr-ww*ww/(2*rr)))
        value*=np.exp(-(rr-.9)**2-2*zz*zz-3*ww*ww)
    else:
        oldr=rr/D0;oldz=zz/np.sqrt(D0);oldw=ww/np.sqrt(D0)
        value=np.exp(1j*(base_x1*rr+zz*zz/rr-ww*ww/(2*rr)))
        value*=np.exp(-(oldr-.9)**2-2*oldz*oldz-3*oldw*oldw)
        if which=='target':value*=D0**(-2)
    return np.sum(W*value)
target_bounds=[(.7,1.3),(-.2,.2),(-.2,.2)]
source_bounds=[(.7/D0,1.3/D0),(-.2/np.sqrt(D0),.2/np.sqrt(D0)),(-.2/np.sqrt(D0),.2/np.sqrt(D0))]
source_value=integrate(source_bounds,'source');target_value=integrate(target_bounds,'target');wrong_value=integrate(target_bounds,'wrong')
error=abs(source_value-target_value);assert error<2e-14
assert abs(wrong_value-D0**2*target_value)<2e-14 and abs(wrong_value-source_value)>1e-3
checks.append({'name':'independent bounded source/target integral comparison and omitted-Jacobian defect','passed':True,
 'base_point':[base_x1,base_x2],'D_exact':'1721/1350','Gauss_nodes_per_axis':32,
 'target_box':target_bounds,'absolute_integral_difference':float(error),
 'omitted_Jacobian_absolute_defect':float(abs(wrong_value-source_value)),
 'scope':'Absolutely integrable finite boxes, independently assembled source/target phases, amplitudes, bounds and weights; not verification of the unrestricted oscillatory cutoff limit.'})

assert len(checks)==6 and all(r['passed'] for r in checks)
lesson=c/'homogeneous-phase-equivalence-and-stabilization.md'
report={'schema':'homogeneous-phase-equivalence-bounded-check/v1','passed':True,'checks':checks,
 'lesson_sha256':sha(lesson),'script_sha256':sha(Path(__file__)),
 'general_smooth_proof_independently_certified':False,'whole_source_parent_closed':False}
(c/'checks/bounded-checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks':len(checks),'passed':True,'lesson_sha256':report['lesson_sha256']}))
