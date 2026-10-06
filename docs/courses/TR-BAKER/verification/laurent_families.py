"""Outward rational certificates for Laurent's eleven numerical pairs.

GPT-6.1 Sol (OpenAI), Codex, Ultra; October 2026. CC0.
Mathematical source: Laurent (2008), numerical corollaries and parameter
tables. The course gives the parameter checks and monotonicity proof.
"""
from fractions import Fraction as F
import json
from laurent_constant import Interval, constants, decimal_out

rows = [
    (10,'32.3','.54','5.9','25.2','.52','5.0'),
    (12,'29.9','.54','6.0','23.4','.53','5.1'),
    (14,'28.2','.55','6.1','22.1','.54','5.2'),
    (16,'26.9','.56','6.2','21.1','.55','5.2'),
    (18,'26.0','.56','6.3','20.3','.55','5.3'),
    (20,'25.2','.56','6.3','19.7','.56','5.3'),
    (22,'24.5','.57','6.4','19.2','.56','5.4'),
    (24,'24.0','.57','6.4','18.8','.56','5.4'),
    (26,'23.5','.57','6.4','18.4','.57','5.4'),
    (28,'23.1','.57','6.5','18.1','.57','5.4'),
    (30,'22.8','.58','6.5','17.9','.57','5.5'),
]
results = []
for m,C1,mu1,rho1,C2,mu2,rho2 in rows:
    for kind,target,mu,rho,shift,offset in [
        ('complex',C1,mu1,rho1,2,F(21,100)),
        ('real',C2,mu2,rho2,1,F(19,50))]:
        mu,rho,target = map(F,(mu,rho,target))
        A = rho+shift
        value,lam = constants(m,A,A,rho=rho,mu=mu)
        assert value.hi < target
        assert (-Interval(A).log()+lam.log()+F(181,100)).hi < offset
        assert lam.hi < m
        assert lam.hi < A
        # The remaining cutoff is h0 >= D_*, so h0 >= D_*log(2)/2.
        assert Interval(2).log().hi < 2
        # Same-sign and one-zero-coefficient reductions from Corollary 7.5.
        assert F(8,1)/(target*m)+F(6,1)/target < F(39,100)
        results.append({'m':m,'kind':kind,'mu':str(mu),'rho':str(rho),
                        'scale':str(A),'target':str(target),
                        'constant_interval':[decimal_out(value.lo,8),decimal_out(value.hi,8,True)]})

RESULT = {'status':'all 22 numerical constants and parameter cutoffs passed',
          'results':results,'arithmetic':'128-bit outward rational intervals; integers and Fraction only',
          'scope':'general monotonicity and sign reductions are supplied in the lesson'}
if __name__ == '__main__':
    print(json.dumps(RESULT,indent=2))
