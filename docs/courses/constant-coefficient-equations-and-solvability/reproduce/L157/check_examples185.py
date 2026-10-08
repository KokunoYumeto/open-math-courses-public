"""Independent Fourier pair, limit, derivative and frequency geometry probes."""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=75;HERE=Path(__file__).resolve().parent;rows=[]
def equal(name,value,expected,tol=1e-55):
 error=abs(value-expected);scale=max(mp.mpf(1),abs(expected))
 rows.append(dict(name=name,absolute_error=float(error),relative_error=float(error/scale),
  tolerance=tol,passed=bool(error<=mp.mpf(str(tol))*scale)))
def inequality(name,value,bound,upper=True,tol=1e-55):
 rows.append(dict(name=name,actual=float(value),bound=float(bound),upper_bound=upper,
  tolerance=tol,passed=bool(value<=bound+mp.mpf(str(tol)) if upper else value+mp.mpf(str(tol))>=bound)))
for a in [mp.mpf('-.75'),mp.mpf(0),mp.mpf('.5')]:
 for xi in [mp.mpf(3),mp.mpf(41)]:
  s=mp.log(abs(xi))
  for z in [mp.mpc('.4','.3'),mp.mpc('-.2','-.8')]:
   actual=mp.log(abs(mp.exp(-1j*a*(xi+s*z))))/s
   equal('point-mass-Fourier-sign-'+str((a,xi,z)),actual,a*z.imag)
for r in [0,1,2,5]:
 for R in [mp.mpf(9),mp.mpf(100),mp.mpf(10000)]:
  s=mp.log(R);a=mp.mpf('.5')
  for z in [mp.mpc('.3','.2'),mp.mpc('-.4','-.7'),mp.mpc(0,2)]:
   zeta=R+s*z
   direct=mp.log(abs(zeta**r*mp.exp(-1j*a*zeta)))/s
   expected=r+r*mp.log(abs(1+s*z/R))/s+a*z.imag
   equal('derivative-atom-direct-Fourier-'+str((r,R,z)),direct,expected)
   if abs(z)*s/R<=mp.mpf('.5'):
    inequality('derivative-uniform-error-bound-'+str((r,R,z)),abs(direct-r-a*z.imag),2*r*abs(z)/R)
   if z.real==0:
    equal('derivative-imaginary-axis-closed-error-'+str((r,R,z)),
     direct-r-a*z.imag,r*mp.log(1+(z.imag*s/R)**2)/(2*s))
for j in [1,10,100]:
 R=(2*j+1)*mp.pi;s=mp.log(R)
 inequality('persistent-zero-multiprecision-residual-'+str(j),abs(1+mp.exp(-1j*R)),mp.mpf('1e-65'))
 for eta in [mp.mpf(-2),mp.mpf('-.4'),mp.mpf('.4'),mp.mpf(2)]:
  z=mp.mpc('.17',eta)
  direct=mp.log(abs(1+mp.exp(-1j*(R+s*z))))/s
  reduced=mp.log(abs(1-mp.exp(-1j*s*z)))/s
  equal('two-atom-shifted-complex-pair-'+str((j,eta)),direct,reduced)
  if eta>0:
   value=mp.log(abs(1-mp.exp(eta*s)))/s
   equal('two-atom-positive-axis-factorization-'+str((j,eta)),
    value,eta+mp.log(1-mp.exp(-eta*s))/s)
  else:
   equal('two-atom-negative-axis-factorization-'+str((j,eta)),
    mp.log(abs(1-mp.exp(eta*s)))/s,mp.log(1-mp.exp(eta*s))/s)
for j in range(32):
 theta=2*mp.pi*j/32;x=mp.cos(theta);y=mp.sin(theta)
 equal('Euclidean-direction-norm-'+str(j),x*x+y*y,1)
 inequality('dominant-coordinate-threshold-'+str(j),max(abs(x),abs(y)),1/mp.sqrt(2),upper=False)
for eta in [mp.mpf(-3),mp.mpf('-.1'),mp.mpf(0),mp.mpf('.7'),mp.mpf(2)]:
 equal('atom-segment-support-function-'+str(eta),max(0,eta),max(mp.mpf(0)*eta,mp.mpf(1)*eta))
 for a in [mp.mpf('-.5'),mp.mpf('.5')]:
  for t in [mp.mpf(100),mp.mpf(10000)]:
   equal('derivative-recession-constant-removal-'+str((eta,a,t)),
    (2+a*t*eta)/t-a*eta,2/t)
for A in [mp.mpf(1),mp.mpf(4)]:
 for R in [mp.mpf(3),mp.mpf(50),mp.mpf(1000)]:
  inequality('whole-parameter-upper-bound-'+str((A,R)),1+R+A*mp.log(R),R*(mp.mpf('1.5')+A/mp.e))
for R in [mp.mpf(100),mp.mpf(1000),mp.mpf(10000)]:
 A=mp.mpf(2)
 inequality('dominant-coordinate-remains-large-after-complex-shift-'+str(R),
  R/mp.sqrt(2)-A*mp.log(R),R/(2*mp.sqrt(2)),upper=False)
assert all(r['passed']for r in rows),[r for r in rows if not r['passed']]
record=dict(schema='original-joint-frequency-example-checks185/v1',status='PASS',checks=len(rows),precision_decimal_digits=75,
 records=rows,maximum_relative_error=max(r.get('relative_error',0)for r in rows),
 scope='Direct multiprecision entire Fourier expressions, exact shifted phases, derivative errors and recession, persistent-zero residuals, Euclidean frequency dominance and whole-parameter carrier bound.',
 checks_are_proof_supplements=True,abstract_PSH_compactness_and_ultrafilter_proofs_supplied_in_lesson=True,
 persistent_zero_is_proved_algebraically_not_by_floating_point_residual=True)
(HERE/'independent-example-checks185.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status='PASS',checks=len(rows),maximum_relative_error=record['maximum_relative_error'])))
