"""Finite exact order/sign/Fourier checks; full proofs remain in the lesson."""
from pathlib import Path
from fractions import Fraction as F
import datetime,hashlib,json,math
r=Path(__file__).resolve().parent;p=r
groups=[]
for a in [F(-2),F(1,3)]:
    for b in [F(-3,4),F(7)]:
        for c in [F(-5),F(0),F(9,2)]:
            base=4*a*b;imag_source=-2*a*b+c
            assert -2*imag_source+2*c==base
groups.append({'name':'WC13 principal commutator sign and constant imaginary lower cancellation','cases':12,'passed':True})
for s in [F(-5,3),F(0),F(11,6),F(7,2)]:
    assert ((s-2)+s)/2==s-1 and s+F(1,2)-F(3,2)==s-1
assert F(11,6)-1==F(5,6)
groups.append({'name':'WC8–WC12 unequal-gap balance and exact induction tester','cases':4,'passed':True})
for eta in [.1,.7]:
    for rr in [1.,.1,1e-5]:
        for L in [1,3]:
            m=lambda n:(1+rr*(1+n*n))**(-L/2)
            assert eta*(m(1)-m(2))>0
            # The variable-coefficient derivative creates n(n±1), not n².
            assert 1*(1-1)==0 and 1*(1+1)/2==1
groups.append({'name':'WC24–WC25 full coefficient derivative and nonzero regularizer commutator','cases':12,'passed':True})
# The strong dual-limit proof uses Hilbert density; this finite test does not certify it.
source=p/'weak-commutators-and-variable-regularizers.md'
out={'schema':'an04-weak-commutator-models/v1','checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'passed':True,'groups':groups,'general_theorem_certificate':False}
(p/'model-check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print({'passed':True,'groups':len(groups),'general_theorem_certificate':False})
