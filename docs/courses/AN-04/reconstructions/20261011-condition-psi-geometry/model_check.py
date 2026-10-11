"""Exact checks for the orientation law and the nonlinear compact tube."""
from pathlib import Path
import hashlib,json
import sympy as s
M=Path(__file__).resolve().parent
checks=[]
def zero(name,expr):
 value=s.simplify(expr);assert value==0,(name,value)
 checks.append({'name':name,'exact':True,'passed':True})
a,b,c,d,phi=s.symbols('a b c d phi')
A=s.Matrix([[a,b],[c,d]])
S=s.Matrix([[1,0],[phi,1]])
B=a-b*phi
C=s.Matrix([[1,b/B],[0,1]])
R=s.simplify(A*S.inv()*C.inv())
for i,j,target in [(0,0,B),(0,1,0),(1,0,c-d*phi),(1,1,(a*d-b*c)/B)]:zero(f'triangular_entry_{i}{j}',R[i,j]-target)
zero('positive_determinant_preserved',R.det()-A.det())
t,z,tau,rho,theta=s.symbols('t z tau rho theta',real=True)
pb=lambda f,g:s.diff(f,tau)*s.diff(g,t)-s.diff(f,t)*s.diff(g,tau)
zero('rotation_bracket',s.trigsimp(pb(s.cos(theta)*tau+s.sin(theta)*t,s.sin(theta)*tau-s.cos(theta)*t)+1))
zero('conjugation_reverses_bracket',pb(tau,t)-1)
T,Z,Sigma,H=s.symbols('T Z Sigma H',real=True)
for k in [-3,-1,0,1,3]:
 kk=s.Rational(k);aa=kk/(1+kk**2);den=1-aa*T*Z
 zz=Z/den;rr=H*den**2;tt=Sigma-aa*Z**2*H
 zero(f'k{k}_inverse_position',zz/(1+aa*T*zz)-Z)
 zero(f'k{k}_inverse_momentum',rr*(1+aa*T*zz)**2-H)
 zero(f'k{k}_inverse_temporal',tt+aa*zz**2*rr-Sigma)
 zero(f'k{k}_primitive_dT',tt+rr*s.diff(zz,T)-Sigma)
 zero(f'k{k}_primitive_dZ',rr*s.diff(zz,Z)-H)
 zero(f'k{k}_complex_normal_form',((1+s.I*kk)*tt+s.I*zz**2*rr)/(1+s.I*kk)-Sigma-s.I*Z**2*H/(1+kk**2))
 zero(f'k{k}_temporal_independence',s.diff(zz**2*rr,Sigma))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'passed':True,'total_cases':len(checks),'exact_algebraic_checks':len(checks),'numerical_checks':0,'source_sha256':sha(M/'condition-psi-and-complex-characteristic-tubes.md'),'script_sha256':sha(Path(__file__)),'checks':checks,'scope':'Exact orientation matrix identities and seven independent inverse, primitive and symbol identities for each of five rational parameter choices. General geometry and infinite-order assertions are proved in the lesson.'}
(M/'model-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8');print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
