"""Independent physical-circle and carrier-area quadratures for the examples."""
from pathlib import Path
from decimal import Decimal, localcontext
import json, math
from scipy.integrate import quad

HERE=Path(__file__).resolve().parent
checks=[]
def decimal_series(x):
    with localcontext() as c:
        c.prec=75;xx=Decimal(str(x));term=total=Decimal(1)
        for m in range(1,10000):
            term*=xx/Decimal(m*m);total+=term
            q=xx/Decimal((m+2)**2);nxt=term*xx/Decimal((m+1)**2)
            if q<1 and nxt/(1-q)<Decimal('1e-65')*total:
                return float(total),m,str(nxt/(1-q))
        raise ArithmeticError('Series failed to converge')
def check(name,actual,expected,tolerance=3e-12,details=None):
    error=abs(actual-expected)/max(1,abs(expected))
    checks.append({'name':name,'actual':actual,'expected':expected,'scaled_error':error,'tolerance':tolerance,
                   'passed':error<=tolerance,'details':details})
    assert error<=tolerance,(name,error,tolerance)

for x in [0,.0625,.25,1,4,9,16,25,64,100,144]:
    value,m,tail=decimal_series(x);s=math.sqrt(x)
    # Integrate the exact real-circle representation, rescaled to avoid overflow.
    integral,err=quad(lambda t:math.exp(2*s*(math.cos(t)-1)),0,math.pi,
                      epsabs=2e-13,epsrel=2e-13,limit=150)
    actual=math.exp(2*s)*integral/math.pi
    check('positive series versus real-circle integral, x='+str(x),actual,value,
          details={'series_decimal_digits':75,'last_series_degree':m,'positive_tail_upper_bound':tail,
                   'rescaled_quadrature_error':err,'proof_locator':'AF31'})
    assert math.log(value)<=2*s+1e-12
    for eps in [.1,.25,.5,1]:assert 2*s<=eps*x+1/eps+1e-12

for eps in [.1,.5,1.0]:
    def top(x):
        distance=max(abs(x)-1,0)
        return math.sqrt(max(eps*eps-distance*distance,0))
    parts=[quad(lambda x:2*top(x),a,b,epsabs=1e-12,epsrel=1e-12)[0]
           for a,b in [(-1-eps,-1),(-1,1),(1,1+eps)]]
    check('complex stadium physical area, epsilon='+str(eps),sum(parts),4*eps+math.pi*eps*eps,
          details={'integration_variable':'real part x; twice the actual boundary height','proof_locator':'AF4'})

def phi(z1,z2):return abs(z1.imag)+.5*math.hypot(z1.imag,z2.imag)
for name,z1,z2,b1,b2,expected in [
 ('one-block circle',0j,0j,1+0j,0j,3/math.pi),
 ('diagonal graph circle',0j,0j,1+0j,1j,2/math.pi+.5),
 ('off-center complex line',2+.3j,-1-.2j,.75-.2j,.3+.6j,None)]:
    integral,err=quad(lambda t:phi(z1+b1*complex(math.cos(t),math.sin(t)),
                                  z2+b2*complex(math.cos(t),math.sin(t))),
                      0,2*math.pi,epsabs=1e-10,epsrel=1e-10,limit=200)
    mean=integral/(2*math.pi);center=phi(z1,z2)
    if expected is not None:check(name+' PSH circle mean',mean,expected,tolerance=3e-10)
    else:
        assert mean>=center-1e-10
        checks.append({'name':name+' PSH circle inequality','mean':mean,'center':center,
                       'gap':mean-center,'quadrature_error':err,'passed':True,'proof_locator':'AF4',
                       'general_PSH_proof_claimed_from_sample':False})

sample=3+4j;graph=(sample,1j*sample)
assert [graph[0].real,graph[0].imag,graph[1].real,graph[1].imag]==[3,4,-4,3]
assert phi(*graph)==6.5 and sum(abs(z)**2 for z in graph)==50
moments=[{'degree':m,'real_numerator':[1,0,-1,0][m%4],'imaginary_numerator':[0,1,0,-1][m%4],
          'denominator':math.factorial(m)} for m in range(11)]
report={'schema':'AN02-analytic-functional-example-checks151/v1','status':'PASS','quadrature_checks':checks,
        'quadrature_count':len(checks),'exact_point_moments':moments,'exact_graph_sample':[3,4,-4,3],
        'exact_sample_phi':6.5,'exact_sample_graph_squared_norm':50,
        'numerical_checks_replace_theorems_or_finite_jet_proof':False,
        'general_carrier_Fourier_criterion_established_by_finite_tests':False,
        'whole_course_complete':False}
(HERE/'independent-example-checks151.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','quadratures':len(checks),'max_scaled_comparison_error':max(x.get('scaled_error',0) for x in checks),
                  'example_report':str(HERE/'independent-example-checks151.json')}))
