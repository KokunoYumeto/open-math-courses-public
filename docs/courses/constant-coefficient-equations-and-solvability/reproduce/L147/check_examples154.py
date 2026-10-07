"""Independent physical quadratures for the exact logarithm and cutoff examples."""
from pathlib import Path
import cmath,json,math
from scipy.integrate import quad
HERE=Path(__file__).resolve().parent
INNER=1/12;OUTER=1/6
checks=[];disk_rows=[];error_rows=[]
def cutoff(r):
 if r<=INNER:return 1.0,0.0
 if r>=OUTER:return 0.0,0.0
 t=(r-INNER)/(OUTER-INNER);s=-1/t+1/(1-t)
 c=math.exp(-s)/(1+math.exp(-s)) if s>0 else 1/(1+math.exp(s))
 derivative=-c*(1-c)*(1/t**2+1/(1-t)**2)/(OUTER-INNER)
 return c,derivative
def check(name,actual,expected,tolerance=2e-9,details=None):
 error=abs(actual-expected)/max(abs(expected),1e-100)
 checks.append({'name':name,'actual':actual,'expected':expected,'relative_error':error,
                'tolerance':tolerance,'passed':error<=tolerance,'details':details})
 assert error<=tolerance,(name,actual,expected,error)
def log_error(r,t,N):
 # One angular period of the actual polynomial. Integer-N periodicity repeats it N times.
 z=r*complex(math.cos(t/N),math.sin(t/N));value=abs((1+z**N)/2)
 target=math.log(r) if r>1 else 0.0
 return target-math.log(value)/N
for N in [1,3,13,32]:
 for r in [.25,.75,.99,1.01,1.5,2]:
  integral,err=quad(lambda t:log_error(r,t,N),0,math.pi,epsabs=2e-12,epsrel=2e-12,limit=150)
  check(f'actual polynomial angular error N={N}, r={r}',integral/math.pi,math.log(2)/N,
        details={'periodicity_reduction':'t=N*theta; one complete period repeated N times','quadrature_error':err,'proof_locator':'GD32'})
 for R in [2]:
  def radial(r):return 2*r*quad(lambda t:log_error(r,t,N),0,math.pi,epsabs=2e-10,epsrel=2e-10,limit=150)[0]
  parts=[quad(radial,a,b,epsabs=2e-9,epsrel=2e-9,limit=150)[0] for a,b in [(0,1),(1,R)]]
  actual=sum(parts);expected=math.pi*R*R*math.log(2)/N
  check(f'physical polar disk error N={N}, R={R}',actual,expected,tolerance=2e-8,
        details={'actual_polynomial_evaluated_in_nested_quadrature':True,'split_radial_singular_circle':1,'proof_locator':'GD33'})
  disk_rows.append({'N':N,'R':R,'actual_error':actual,'exact_error':expected})
for N in [8,32,128,512,2048]:
 scaled_radial=math.pi*quad(lambda r:r*cutoff(r)[1]**2*math.exp(-2*N*(r*r-INNER*INNER)),
                           INNER,OUTER,epsabs=2e-13,epsrel=2e-12,limit=150)[0]
 def one_center(a):
  def radial(r):
   derivative=cutoff(r)[1]
   def angular(theta):
    direction=complex(math.cos(theta),math.sin(theta));z=a+r*direction
    polynomial=2*a*z-a*a;phi=abs(z)**2
    coefficient=.5*derivative*direction
    weighted=coefficient*cmath.exp(N*(polynomial-phi+INNER*INNER))
    return abs(weighted)**2
   return r*quad(angular,0,2*math.pi,epsabs=2e-12,epsrel=2e-12,limit=100)[0]
  return quad(radial,INNER,OUTER,epsabs=2e-13,epsrel=2e-12,limit=150)[0]
 scaled_physical=one_center(-.5)+one_center(.5)
 check(f'two-seed weighted error, N={N}',scaled_physical,scaled_radial,tolerance=3e-9,
       details={'actual_complex_seed_polynomial_and_cutoff_coefficient_evaluated':True,
                'rescaling_exponent':2*N*INNER*INNER,'two_disjoint_centers':[-.5,.5],'proof_locator':'L147.15'})
 I=scaled_radial*math.exp(-2*N*INNER*INNER)
 error_rows.append({'N':N,'weighted_error_squared_norm':I,'guaranteed_correction_squared_norm_bound':I/(2*N),
                    'actual_correction_values_or_attained_norm_claimed':False})
for d in [2,4,6]:
 sphere=2*math.pi**(d/2)/math.gamma(d/2)
 actual=quad(lambda r:sphere*r**(d-1)*(r**(1-d)/(2*sphere)),0,1,epsabs=1e-13)[0]
 check(f'local complex-gradient kernel L1 norm, real dimension={d}',actual,.5,
       details={'point-estimate-bounded-data-factor':4*.5,'proof_locator':'GD11–GD12'})
def bump(r):return math.exp(1-1/(1-r*r)) if r<1 else 0.0
base=2*math.pi*quad(lambda r:r*bump(r)**2,0,1,epsabs=1e-13)[0]
for eps in [.5,.25,.125]:
 actual=2*math.pi*quad(lambda r:r*bump(r/eps)**2,0,eps,epsabs=1e-13)[0]
 check(f'actual shrinking bump square norm, epsilon={eps}',actual,eps*eps*base,
       details={'point_value':1,'data_supremum_scales_as':'epsilon^(-1)','proof_locator':'L147.12'})
for A,B,r in [(1+2j,.5-.75j,.75),(-2+.25j,1+1j,.5)]:
 def radial(s):
  return s*quad(lambda t:abs(A+B*s*complex(math.cos(t),-math.sin(t)))**2,0,2*math.pi,epsabs=1e-12)[0]
 actual=quad(radial,0,r,epsabs=1e-12)[0]
 expected=math.pi*r*r*abs(A)**2+math.pi*r**4*abs(B)**2/2
 check('affine antiholomorphic physical L2 norm '+str((A,B,r)),actual,expected,
       details={'cross_term_removed_by_actual_angular_integration':True,'proof_locator':'L147.11'})
report={'schema':'AN02-entire-logarithm-example-checks154/v1','status':'PASS','quadrature_count':len(checks),
 'checks':checks,'disk_error_samples':disk_rows,'weighted_error_samples':error_rows,
 'exact_geometric_cutoff_radii':{'inner':INNER,'outer':OUTER,'center_ball_radius':.25},
 'quadratures_replace_density_lemma_or_global_existence_proofs':False,
 'weighted_correction_was_numerically_solved_or_norm_attained':False,'whole_course_complete':False}
(HERE/'independent-example-checks154.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','quadratures':len(checks),'max_relative_error':max(x['relative_error'] for x in checks),
                  'report':str(HERE/'independent-example-checks154.json')}))
