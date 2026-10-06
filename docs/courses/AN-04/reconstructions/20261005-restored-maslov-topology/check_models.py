"""Bounded exact models for U025; arbitrary-loop topology is the written proof."""
import hashlib,json
from fractions import Fraction
from pathlib import Path
import numpy as np
import sympy as s
module=Path(__file__).resolve().parent;lesson=module/'maslov-index-crossings-and-global-phase.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[];t=s.symbols('t',real=True)
for direction in [1,-1]:
    x=s.cos(s.pi*t);xi=-direction*s.sin(s.pi*t);z=x-s.I*xi
    assert s.simplify(xi*s.diff(x,t)-x*s.diff(xi,t))==direction*s.pi
    assert s.simplify(s.diff(z*z,t)/(z*z)-2*s.I*direction*s.pi)==0
checks.append({'name':'both fully oriented one-dimensional generators','passed':True,
 'positive_crossing_form':'pi','positive_determinant_square_winding':1,
 'scope':'Exact vectors, full symplectic derivative and determinant square; not arbitrary-loop classification.'})
sig=[]
for B in [2,-2]:
    K=s.Matrix([[-1,1],[1,-B]])
    signature=0 if K.det()<0 else -2
    if K.det()>0:assert K.trace()<0
    sig.append(signature//2)
assert sig==[-1,0]
assert s.I**sig[0]*s.I**(-sig[1])==-s.I
assert s.I**(-sig[0])*s.I**sig[1]==s.I
for n in range(1,6):
    # Remaining equal reference complements have zero shear: each block has det -1.
    hyperbolic=s.Matrix([[0,1],[1,n+2]])
    assert hyperbolic.det()==-1
checks.append({'name':'actual ordered Gaussian coordinate and reciprocal switches','passed':True,
 'B_values':[2,-2],'half_signatures':sig,'positive_coefficient_product':'-i',
 'positive_reciprocal_frame_and_dual_product':'i',
 'scope':'Both switch directions, including zero-signature remaining blocks in five dimensions.'})
C=s.Matrix([[2+t,t],[t,-3+2*t]]);b=s.Matrix([1+t,2-t*t])
a=(b.T*C.inv()*b)[0]+t+2*t*t
A=s.Matrix.vstack(s.Matrix.hstack(s.Matrix([[a]]),b.T),s.Matrix.hstack(b,C))
h=s.factor(a-(b.T*C.inv()*b)[0]);v=s.Matrix.vstack(s.Matrix([1]),-C.inv()*b)
assert h==t*(1+2*t)
assert s.simplify(A.subs(t,0)*v.subs(t,0))==s.zeros(3,1)
assert s.simplify((v.T*A.diff(t)*v)[0]-s.diff(h,t))==0
assert s.simplify(A.det()-C.det()*h)==0
assert s.diff(A.det(),t).subs(t,0)==-6 and s.diff(h,t).subs(t,0)==1
eta=s.Matrix(s.symbols('e0:3',real=True));edot=s.Matrix(s.symbols('d0:3',real=True))
assert s.simplify((eta.T*(A.diff(t)*eta+A*edot)-(A*eta).T*edot)[0]-(eta.T*A.diff(t)*eta)[0])==0
model=s.Matrix([[t+2*t*t,t+t**3],[t+t**3,2+t*t]])
assert model.subs(t,0)==s.diag(0,2) and model.diff(t).subs(t,0)[0,0]==1
assert s.diff(model.det(),t).subs(t,0)==2
assert s.diff(s.diag(t,-2).det(),t)==-2
checks.append({'name':'full nonconstant Schur and section-derivative calculation','passed':True,
 'three_dimensional_marked_kernel':[str(z) for z in v.subs(t,0)],
 'crossing_form':1,'normal_block_determinant':-6,'full_determinant_derivative':-6,
 'scope':'Nonzero marked off-diagonal block, varying indefinite normal block, all inverse derivatives and extension-vector cancellations; also both public 2x2 examples.'})
multiple=s.diag(2*t+t*t,-3*t+t**3,1+t*t)
assert multiple.subs(t,0)==s.diag(0,0,1)
assert multiple.diff(t).subs(t,0)[:2,:2]==s.diag(2,-3)
eps=s.symbols('eps',positive=True);split=s.diag(2*(t-eps),-3*(t+eps),1)
assert split.subs(t,-eps).nullspace()==[s.Matrix([0,1,0])]
assert split.subs(t,eps).nullspace()==[s.Matrix([1,0,0])]
assert s.diff(split.det(),t).subs(t,-eps)==12*eps
assert s.diff(split.det(),t).subs(t,eps)==-12*eps
checks.append({'name':'regular indefinite crossing and exact simple split','passed':True,
 'original_crossing_form':[2,-3],'ordered_signs':[-1,1],'total':0,
 'scope':'Exact local matrices and both determinant derivatives; supported arbitrary-path homotopy remains a written argument.'})
frame_counts=[]
for n in range(1,6):
    Q=s.eye(n)
    if n>=2:Q[:2,:2]=s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],[s.Rational(4,5),s.Rational(3,5)]])
    phases=[s.Rational(3,5)+s.Rational(4,5)*s.I if j%2==0 else s.Rational(4,5)+s.Rational(3,5)*s.I for j in range(n)]
    U=Q*s.diag(*phases);R=s.diag(-1,*([1]*(n-1)))
    assert s.simplify(U.conjugate().T*U-s.eye(n))==s.zeros(n)
    X=s.re(U);Xi=-s.im(U);V=s.Matrix.vstack(X,Xi)
    assert V.T*V==s.eye(n) and Xi.T*X-X.T*Xi==s.zeros(n)
    assert s.simplify((U*R).det()**2-U.det()**2)==0
    assert s.simplify((U*R).det()+U.det())==0
    assert (V*R)*(V*R).T==V*V.T
    frame_counts.append(n)
a0=(1+s.I)/2;b0=(1-s.I)/2
SU2=s.Matrix([[a0,-s.conjugate(b0)],[b0,s.conjugate(a0)]])
assert s.simplify(SU2.conjugate().T*SU2-s.eye(2))==s.zeros(2) and s.simplify(SU2.det())==1
checks.append({'name':'five actual unitary/real plane frames and SU2 column formula','passed':True,
 'dimensions':frame_counts,'scope':'Unitary matrices, isotropic real spans, identical projection matrices after reflection, determinant sign/square and explicit SU2 formula; no simple-connectedness inference from samples.'})
A=s.Matrix([[t,t*t],[t*t,1-t]])
comm=A*A.diff(t)-A.diff(t)*A
assert s.simplify(comm[0,1]-2*t*(t-1))==0
Delta=s.factor((A-s.I*s.eye(2)).det()/(A+s.I*s.eye(2)).det())
rhs=2*s.I*((s.eye(2)+A*A).inv()*A.diff(t)).trace()
assert s.simplify(s.diff(Delta,t)/Delta-rhs)==0
assert s.simplify(Delta*s.conjugate(Delta)-1)==0
checks.append({'name':'exact noncommuting determinant ratio and phase derivative','passed':True,
 'commutator_entry':'2*t*(t-1)','scope':'Entire rational two-variable matrix path, not just diagonal or marked-point substitution.'})
for n in range(1,7):
    values=[s.Rational(j+1,j+2) for j in range(n)];Q=s.diag(*values)
    E=s.Matrix(n,n,lambda i,j:s.Rational(i+j+1,i+j+2))
    H=s.Matrix(n,n,lambda i,j:E[i,j]/(values[i]+values[j]))
    assert Q*H+H*Q==E
checks.append({'name':'positive-square-root Sylvester derivatives in six dimensions','passed':True,
 'scope':'Explicit inverse on all entries of six positive diagonal models. General smooth square-root dependence is the implicit-theorem proof in the lesson.'})
loops=[]
for ms,alphas in [([1],[Fraction(1,11)]),([-1],[Fraction(1,11)]),([4],[Fraction(1,11)]),
                  ([2,-1,3],[Fraction(1,11),Fraction(2,13),Fraction(3,17)]),
                  ([-2,1,-3],[Fraction(1,11),Fraction(2,13),Fraction(3,17)])]:
    times=[]
    for j,(m,alpha) in enumerate(zip(ms,alphas)):
        for k in range(-abs(m)-3,abs(m)+4):
            tau=(Fraction(k)+Fraction(1,2)-alpha)/m
            if 0<tau<1:times.append((tau,1 if m>0 else -1,j+1))
    assert len({row[0] for row in times})==len(times)
    assert len(times)==sum(abs(m) for m in ms)
    assert sum(sign for _,sign,_ in times)==sum(ms)
    samples=np.linspace(0,1,4001)
    determinant=np.prod([np.exp(2j*np.pi*(float(alpha)+m*samples)) for m,alpha in zip(ms,alphas)],axis=0)
    argument=np.unwrap(np.angle(determinant))
    numeric=(argument[-1]-argument[0])/(2*np.pi)
    assert abs(numeric-sum(ms))<1e-12
    product=s.simplify(s.prod((-s.I)**sign for _,sign,_ in times))
    assert product==s.simplify(s.I**(-sum(ms)))
    if ms==[2,-1,3]:
        assert {tau for tau,_,j in times if j==1}=={Fraction(9,44),Fraction(31,44)}
        assert {tau for tau,_,j in times if j==2}=={Fraction(17,26)}
        assert {tau for tau,_,j in times if j==3}=={Fraction(11,102),Fraction(15,34),Fraction(79,102)}
    loops.append({'coordinate_windings':ms,'exact_times':[str(tau) for tau,_,_ in sorted(times)],
      'index':sum(ms),'independent_numerical_winding':numeric,'coefficient_product':str(product)})
left=np.linspace(0,.5-1e-7,1601);right=np.linspace(.5+1e-7,1,1601)
for values,shift in [(left,0),(right,-2*np.pi)]:
    B=-np.tan(np.pi*values);F=-2*np.arctan(B)
    assert np.max(np.abs(F-(2*np.pi*values+shift)))<1e-12
checks.append({'name':'five exact crossing inventories and independent branch/winding samples','passed':True,
 'loops':loops,'branch_samples_per_side':1601,
 'scope':'Exact rational simple-crossing times; independent 4001-point determinant unwrapping and both transverse branch formulas. These finite samples do not prove the winding/crossing theorem.'})
x=s.cos(2*s.pi*t);xi=2-s.sin(2*s.pi*t)
v=s.Matrix([-s.sin(2*s.pi*t),-s.cos(2*s.pi*t)])
assert s.simplify(v[1]*s.diff(v[0],t)-v[0]*s.diff(v[1],t))==2*s.pi
z=v[0]-s.I*v[1];D=z*z
assert s.simplify(s.diff(D,t)/D-4*s.pi*s.I)==0
assert s.simplify(s.Matrix([s.diff(x,t),s.diff(xi,t)])-2*s.pi*v)==s.zeros(2,1)
checks.append({'name':'complete ordinary tangent Gauss-map example','passed':True,
 'unit_tangent_crossing_form':'2*pi','determinant_square_winding':2,'coefficient_product':-1,
 'scope':'Exact embedded-circle derivative, full tangent vector and determinant derivative; the circle is ordinary and not conic.'})
dimensions=[]
for n in range(1,9):
    d=n*(n+1)//2
    for k in range(1,n+1):
        a=d+1-k*(k+1)//2
        assert (a==d) if k==1 else (a<d)
    dimensions.append({'n':n,'target_dimension':d})
text=lesson.read_text(encoding='utf-8')
assert text.count('**Exercise ')==text.count('**Solution.**')==14
assert not any(ord(ch)<32 and ch not in '\t\r\n' for ch in text)
checks.append({'name':'eight bounded stratum dimension inventories and solution completeness','passed':True,
 'dimensions':dimensions,'exercise_solutions':14,
 'scope':'Arithmetic of the imported stratum codimension and exercise-marker/control-byte checks; the actual strata and critical-value proofs are written mathematics.'})

# A crossing with a persistent horizontal direction is not an x=A*xi graph.
# Check the actual common-complement shear and the fixed-frame winding.
parameter=s.symbols('parameter',real=True)
C=s.Matrix([[1,s.Rational(1,3)],[s.Rational(1,3),2]])
zero=s.zeros(2);eye=s.eye(2)
Omega=s.Matrix.vstack(s.Matrix.hstack(zero,-eye),s.Matrix.hstack(eye,zero))
T=s.Matrix.vstack(s.Matrix.hstack(eye,zero),s.Matrix.hstack(-parameter*C,eye))
assert T.T*Omega*T==Omega
X=s.diag(s.cos(s.pi*t),1);Xi=s.diag(-s.sin(s.pi*t),0)
V=s.Matrix.vstack(X,Xi);W=T*V
assert Xi.det()==0
assert (Xi-C*X).subs(t,s.Rational(1,2)).det()==2
assert s.simplify((W.T*Omega*W.diff(t)-V.T*Omega*V.diff(t)))==s.zeros(2)
samples=np.linspace(0,1,6001);winds=[]
for a in [0,.25,.5,.75,1]:
    values=[]
    for u in samples:
        xx=np.diag([np.cos(np.pi*u),1.])
        xi=np.diag([-np.sin(np.pi*u),0.])-a*np.array(C,float)@xx
        z=xx-1j*xi
        values.append(np.linalg.det(z)**2/np.linalg.det(xx.T@xx+xi.T@xi))
    values=np.array(values)
    assert np.max(np.abs(abs(values)-1))<2e-14
    winding=(np.unwrap(np.angle(values))[-1]-np.unwrap(np.angle(values))[0])/(2*np.pi)
    assert abs(winding-1)<2e-14
    winds.append({'shear_parameter':a,'winding':winding})
assert np.abs(np.linalg.det(np.eye(2)+1j*np.array(C,float))**2/np.linalg.det(np.eye(2)+np.array(C,float)@np.array(C,float))-1)>0.1
checks.append({'name':'nonunitary common-complement shear with a horizontal spectator',
 'passed':True,'original_frequency_projection_singular_for_entire_loop':True,
 'transformed_frequency_determinant_at_crossing':2,'sampled_windings':winds,
 'scope':'Exact shear symplecticity and complete crossing-form identity; five finite winding controls. The fixed-frame determinant changes pointwise, so it cannot be treated as symplectically invariant. Its winding is invariant by the written homotopy proof.'})
report={'schema':'bounded-maslov-topology-check/v1','passed':True,'lesson_sha256':sha(lesson),
 'script_sha256':sha(Path(__file__)),'checks':checks,'whole_course_complete':False,
 'generality_guard':'Exact bounded examples and finite numerical samples do not establish arbitrary-loop topology, smoothing, lifting or generic perturbation. Those require the written proofs and independent review.'}
(module/'model-check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks':len(checks),'passed':True,'lesson_sha256':sha(lesson)}),flush=True)
