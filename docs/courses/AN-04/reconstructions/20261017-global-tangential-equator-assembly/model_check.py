"""Finite identities supporting the full kernel proof; not a proof certificate."""
from pathlib import Path
import hashlib,json
import sympy as s
q,p,k,b,v=s.symbols('q p k b v', real=True)
checks={}
checks['exact_complementary_polynomial']=s.expand(q*(2-q)+(1-q)**2-1)==0
checks['weak_band_floor']=s.expand((1-q)**2-s.Rational(1,4)-(q-s.Rational(1,2))*(q-s.Rational(3,2)))==0
checks['scalar_modulus']=s.expand((q+s.I*p*(1-q)**2)*(q-s.I*p*(1-q)**2)-q*q-p*p*(1-q)**4)==0
Q=s.Matrix([[s.Rational(2,3),s.I/7],[-s.I/7,s.Rational(1,4)]]);P=s.Matrix([[s.Rational(3,5),s.Rational(1,11)],[s.Rational(1,11),s.Rational(2,5)]]);R=s.eye(2)-Q;S=R*P*R
zero=lambda m:all(s.simplify(x)==0 for x in m)
checks['sandwich_commutator']=zero(Q*S-S*Q-R*(Q*P-P*Q)*R)
checks['regularizer_recovery']=zero(P-P*(2*s.eye(2)-Q)*Q-S-(P*R-R*P)*R)
checks['noncommuting_norm_identity']=zero((Q+s.I*S).conjugate().T*(Q+s.I*S)-Q*Q-S*S-s.I*(Q*S-S*Q))
lam=1+k*k+b*b
checks['inverse_first_derivative']=s.simplify(s.diff(1/lam,k)+2*k/lam**2)==0
checks['inverse_second_derivative']=s.simplify(s.diff(1/lam,k,2)+2/lam**2-8*k*k/lam**3)==0
checks['circle_normal_transform']=s.simplify((1/(b+s.I*k)+1/(b-s.I*k))/(2*b)-1/(b*b+k*k))==0
checks['fundamental_derivative_jump']=s.simplify(-s.Rational(1,2)-s.Rational(1,2)+1)==0
checks['cutoff_support_exponents']=(-8+4+2==-2 and -8-(1+2)==-11 and -8+(1+2)==-5 and s.exp(-2)*2<1)
checks['output_test_square_integrability']=s.integrate(v**(-2),(v,1,s.oo))==1
out={'passed':all(bool(x) for x in checks.values()),'exact_checks':len(checks),'checks':{k:bool(v) for k,v in checks.items()},'source_sha256':hashlib.sha256((Path(__file__).parent/'one-scalar-test-when-all-boundary-tangential-directions-are-allowed.md').read_bytes()).hexdigest(),'scope':'Finite identities and support exponents only; full operator, kernel and Banach arguments are in the editable proof.'}
(Path(__file__).parent/'model-check.json').write_text(json.dumps(out,indent=2)+'\n','utf-8');assert out['passed'];print(json.dumps(out))
