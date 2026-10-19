"""Finite exact identities; full analytic estimates are proved in the source."""
from pathlib import Path
import hashlib,json
import sympy as s
i,j,c,k=s.symbols('i j c k',real=True);checks={}
checks['sparse_spacing_factorization']=s.expand(i**4-j**4-(i-j)*(i+j)*(i*i+j*j))==0
checks['sparse_spacing_lower_bound']=s.expand(i*i+j*j-(i+j)**2/2-(i-j)**2/2)==0
V=s.Matrix([1,1])/s.sqrt(2);Pi=V*V.conjugate().T;beta=s.diag(1,s.Rational(1,2));I=s.eye(2);P=beta*Pi*beta
zero=lambda m:all(s.simplify(x)==0 for x in m)
checks['actual_isometry']=zero(V.conjugate().T*V-s.eye(1))
checks['projection_identity']=zero(Pi*Pi-Pi)
checks['cutoff_projection_defect']=zero(P*P-s.Rational(5,8)*P) and P*P!=P
checks['cutoff_cross_identity']=zero((I-P)*beta*V-beta*Pi*(I-beta*beta)*V)
Q=s.Matrix([[s.Rational(2,3),s.I/7],[-s.I/7,s.Rational(1,4)]]);S0=s.Matrix([[s.Rational(1,3),-s.I/5]]);Sh=beta*V*S0;Qh=(I-P)*Q;E=beta*Pi*(I-beta*beta)*V*S0;A=Qh+Sh
checks['full_cross_form_identity']=zero(Qh.conjugate().T*Sh-Q.conjugate().T*E)
checks['scalar_norm_identity']=zero(A.conjugate().T*A-Qh.conjugate().T*Qh-Sh.conjugate().T*Sh-Q.conjugate().T*E-E.conjugate().T*Q)
checks['residual_projection_correction']=zero(Qh-Q+P*Q)
lam=c*k*s.erf(k)
checks['entire_shift_derivative']=s.simplify(s.diff(lam,k)-c*s.erf(k)-2*c*k*s.exp(-k*k)/s.sqrt(s.pi))==0
checks['entire_shift_evenness']=s.simplify(lam.subs(k,-k)-lam)==0
checks['concrete_cutoff_cross_vector']=zero((I-P)*beta*V-s.Rational(3,8)*beta*V)
out={'passed':all(bool(x) for x in checks.values()),'exact_checks':len(checks),'checks':{k:bool(v) for k,v in checks.items()},'source_sha256':hashlib.sha256((Path(__file__).parent/'scalar-tests-from-a-missing-tangential-direction.md').read_bytes()).hexdigest(),'scope':'Exact spacing, projection, cutoff cross-form, scalar norm and entire-function identities. They do not certify the full analytic proof.'}
(Path(__file__).parent/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8');assert out['passed'];print(json.dumps(out))
