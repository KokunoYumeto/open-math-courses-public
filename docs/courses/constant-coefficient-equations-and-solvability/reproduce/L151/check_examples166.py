"""Independent actual jets, contour remainder, graph Jacobians and area data."""
from pathlib import Path
import json
import math
import numpy as np
import mpmath as mp

HERE=Path(__file__).resolve().parent
mp.mp.dps=65
checks=[]
def equal(name,actual,expected,tol=2e-10):
    actual,expected=complex(actual),complex(expected)
    error=abs(actual-expected)
    limit=tol*(1+abs(expected))
    checks.append(dict(name=name,absolute_error=error,allowed_error=limit,passed=error<=limit))
    assert checks[-1]['passed'],(name,actual,expected,error)
def bound(name,lhs,rhs):
    lhs,rhs=float(lhs),float(rhs)
    checks.append(dict(name=name,lhs=lhs,rhs=rhs,passed=lhs<=rhs+1e-12*(1+abs(rhs))))
    assert checks[-1]['passed'],(name,lhs,rhs)
def fit(nodes,multiplicities,data):
    degree=sum(multiplicities)
    rows=[]
    for node,mult in zip(nodes,multiplicities):
        for a in range(mult):
            rows.append([mp.diff(lambda z,j=j:z**j,node,a) for j in range(degree)])
    return mp.lu_solve(mp.matrix(rows),mp.matrix(data))
def value(coeff,z):
    return sum(c*z**j for j,c in enumerate(coeff))

for eps in [mp.mpf('.03'),mp.mpf('.2'),mp.mpf('.4'),mp.mpf('.8')]:
    coeff=fit([0,eps],[2,2],[0,0,-1,0])
    expected=[0,0,-3/eps**2,2/eps**3]
    for j in range(4):equal(f'actual-jet-linear-solve-eps{eps}-coefficient{j}',coeff[j],expected[j])
    q=lambda z:value(coeff,z)
    for node,target in [(0,0),(eps,-1)]:
        equal(f'actual-Hermite-value-eps{eps}-node{node}',q(node),target)
        equal(f'physical-Hermite-first-derivative-eps{eps}-node{node}',mp.diff(q,node),0)
    norm=max(abs(q(mp.exp(2j*mp.pi*l/128))) for l in range(128))
    exact=3/eps**2+2/eps**3
    equal(f'actual-complex-circle-norm-eps{eps}',norm,exact)
    equal(f'unordered-normalization-eps{eps}',eps**3*norm,2+3*eps)
    equal(f'ordered-normalization-eps{eps}',eps**6*norm,2*eps**3+3*eps**4)
    equal(f'discriminant-half-integer-scale-eps{eps}',mp.power(eps**2,mp.mpf('1.5')),eps**3)

nodes=[mp.mpc('.1','.2'),mp.mpc('.5','-.15'),mp.mpc('-.3','.05')]
multiplicities=[2,1,2]
coeff0=[1,mp.mpc('-.3','.4'),mp.mpf('.7'),mp.mpc(0,'-.2'),mp.mpf('.2')]
q=lambda z:value(coeff0,z)
data=[mp.diff(q,node,a) for node,mult in zip(nodes,multiplicities) for a in range(mult)]
coeff1=fit(nodes,multiplicities,data)
for j in range(5):equal(f'complex-three-node-jet-reconstruction-coefficient{j}',coeff1[j],coeff0[j])
for z in [0,mp.mpc('.7','.1'),mp.mpc('-.2','.4')]:
    actual=0
    for j,(node,mult) in enumerate(zip(nodes,multiplicities)):
        pj=lambda w:mp.fprod((w-nodes[i])**multiplicities[i] for i in range(len(nodes)) if i!=j)
        taylor=mp.taylor(lambda w:q(w)/pj(w),node,mult-1)
        actual+=value(taylor,z-node)*pj(z)
    equal(f'Taylor-reciprocal-Hermite-versus-actual-jets-at{z}',actual,value(coeff1,z))
D=mp.fprod(abs(nodes[i]-nodes[j]) for i in range(3) for j in range(i+1,3))
Delta=mp.fprod(abs(nodes[i]-nodes[j]) for i in range(3) for j in range(3) if i!=j)
equal('full-ordered-versus-unordered-complex-root-product',Delta,D*D)

# Direct numerical circle integral is independent of the entire coefficient
# series. Parameters include the exact collision y=0.
rho=.6
theta=np.arange(1024)*2*np.pi/1024
w=rho*np.exp(1j*theta)
for y in [0,.04+.03j,.12-.08j]:
    yy=mp.mpc(y)
    A=mp.fsum(yy**j/mp.factorial(2*j) for j in range(50))
    B=mp.fsum(yy**j/mp.factorial(2*j+1) for j in range(50))
    for t in [0,.1+.03j,-.2]:
        contour=np.mean(np.exp(w)*(w*w-complex(t)**2)/((w-complex(t))*(w*w-y))*w)
        h=A+mp.mpc(t)*B
        equal(f'actual-contour-remainder-at{t},{y}',contour,h)
        tt=mp.mpc(t)
        g=mp.fsum((1/mp.factorial(2*j)+tt/mp.factorial(2*j+1))
                 *mp.fsum(tt**(2*(j-1-l))*yy**l for l in range(j))
                 for j in range(1,50))
        equal(f'entire-series-quotient-identity-at{t},{y}',
              mp.exp(tt),(tt*tt-yy)*g+h)
    for t in [mp.sqrt(yy),-mp.sqrt(yy)]:
        equal(f'actual-branch-value-at{t},{y}',mp.exp(t),A+t*B)
equal('collision-first-jet-from-remainder',mp.diff(lambda t:1+t,0),mp.diff(mp.exp,0))

# Differentiate the physical real graph map, then form the metric determinant.
def gram_area(x,v):
    maps=[lambda a,b:a,lambda a,b:b,lambda a,b:a*a-b*b,lambda a,b:2*a*b]
    J=mp.matrix([[mp.diff(fn,(x,v),(1,0)),mp.diff(fn,(x,v),(0,1))] for fn in maps])
    gram=J.T*J
    return mp.sqrt(mp.det(gram)),mp.det(mp.matrix([[J[2,0],J[2,1]],[J[3,0],J[3,1]]]))
for x,v in [(0,0),(.2,.3),(-.4,.1),(.45,0)]:
    xx,vv=mp.mpf(str(x)),mp.mpf(str(v))
    area,projected=gram_area(xx,vv)
    equal(f'actual-real-Gram-area-at{x},{v}',area,1+4*(xx*xx+vv*vv))
    equal(f'actual-projection-Jacobian-at{x},{v}',projected,4*(xx*xx+vv*vv))
    bound(f'surface-projection-density-at{x},{v}',projected,area)
b=(mp.sqrt(5)-1)/2
rad=mp.sqrt(b)
surface=2*mp.pi*mp.quad(lambda r:r*r*gram_area(r,0)[0],[0,rad])
fiber=2*mp.pi*mp.quad(lambda s:s*(abs(mp.sqrt(s))+abs(-mp.sqrt(s))),[0,b])
equal('actual-surface-data-integral',surface,2*mp.pi*(b**mp.mpf('1.5')/3+4*b**mp.mpf('2.5')/5))
equal('actual-two-root-fiber-data-integral',fiber,8*mp.pi*b**mp.mpf('2.5')/5)
equal('actual-surface-minus-projected-data',surface-fiber,2*mp.pi*b**mp.mpf('1.5')/3)
equal('actual-unit-ball-boundary-radius',rad*rad+rad**4,1)
bound('full-area-dominates-fiber-data',fiber,surface)

for eps in [0,.1,.2+.3j]:
    R=lambda y:y**3+mp.mpc(eps)
    strength=mp.sqrt(mp.fsum(abs(mp.diff(R,0,j))**2 for j in range(4)))
    equal(f'actual-derivative-strength-at-central-zero-{eps}',strength,mp.sqrt(abs(mp.mpc(eps))**2+36))
for degree in [1,2,3]:
    for exponent in [.5,1.5]:
        integral=2*mp.pi*mp.quad(lambda r:r*abs(r**degree)**mp.mpf(str(exponent)),[0,1])
        equal(f'actual-polynomial-weighted-mean-degree{degree}-power{exponent}',integral,
              2*mp.pi/(degree*exponent+2))
    logmean=2*mp.quad(lambda r:r*mp.log(r**degree/mp.factorial(degree)),[0,1])
    equal(f'actual-normalized-polynomial-log-mean-degree{degree}',logmean,
          -mp.mpf(degree)/2-mp.log(mp.factorial(degree)))

root2=mp.sqrt(2)
pole=mp.matrix([mp.mpf(4)/5,root2-mp.mpf(4)/5])
bound('pole-first-coordinate-inside-polydisk',abs(pole[0]),1)
bound('pole-second-coordinate-inside-polydisk',abs(pole[1]),1)
bound('pole-outside-unit-ball',1,mp.fsum(abs(x)**2 for x in pole))
equal('actual-polydisk-pole-denominator',1-(pole[0]+pole[1])/root2,0)
for t,y in [(.02,.03),(.06+.02j,-.04+.01j),(-.07,.01)]:
    tt,yy=mp.mpc(t),mp.mpc(y)
    f=1/(1-(tt+yy)/root2)
    h=root2/(root2-2*yy)
    g=root2/((root2-tt-yy)*(root2-2*yy))
    equal(f'actual-unit-ball-rational-division-at{t},{y}',f,(tt-yy)*g+h)
    equal(f'actual-outside-factor-division-at{t},{y}',
          tt*tt,(tt-yy)*(tt-3)*(tt+yy)/(tt-3)+yy*yy)

result=dict(schema='AN02-L151-independent-example-checks166/v1',status='PASS',
            checks=len(checks),records=checks,
            maximum_equality_error=max(r.get('absolute_error',0) for r in checks),
            scope='Independent actual Hermite jet linear solves and complex-circle norms, contour remainders, entire quotient series, real graph Jacobians, two-root fiber and full surface integrals, polynomial weighted/log means and Euclidean-ball division.',
            calculations_are_proof_supplements=True,general_proof_or_recursive_closure_inferred=False)
(HERE/'independent-example-checks166.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','checks','maximum_equality_error','scope']},ensure_ascii=False))
