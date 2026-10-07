"""Independent physical radial quadratures for exact extension examples."""
from pathlib import Path
import json,math
from scipy.integrate import quad
HERE=Path(__file__).resolve().parent;checks=[]
def check(name,actual,expected,tol=2e-9):
    assert abs(actual-expected)<=tol*max(1,abs(expected)),(name,actual,expected)
    checks.append({'name':name,'actual':actual,'expected':expected,'relative_or_absolute_tolerance':tol,'pass':True})
annular=quad(lambda r:2*math.pi/r,.5,1)[0]
check('Actual annular error square norm',annular,2*math.pi*math.log(2))
assert annular<4*math.pi
for p in [1,2,3]:
    area=2*math.pi**p/math.factorial(p-1)
    for q in [p+1,3*p]:
        for a in [.5,1,2.4]:
            physical=quad(lambda r:area*r**(2*p-1)/(a+r*r)**q,0,math.inf,epsabs=1e-10,epsrel=1e-10)[0]
            expected=math.pi**p*math.factorial(q-p-1)/math.factorial(q-1)*a**(p-q)
            check(f'Physical C^{p} radial norm,q={q},a={a}',physical,expected)
J0=quad(lambda r:2*math.pi*r*math.exp(-math.sqrt(1+r*r)),0,math.inf)[0]
check('Radial tangent constant datum norm',J0,4*math.pi/math.e)
J1=quad(lambda r:2*math.pi*r**3*math.exp(-math.sqrt(1+r*r)),0,math.inf)[0]
check('Radial tangent linear datum norm',J1,28*math.pi/math.e)
for j in [1,2,3,4]:
    dimension=1+j;area=2*math.pi**dimension/math.factorial(dimension-1)
    actual=quad(lambda r:area*r**(2*dimension-1)*math.exp(-math.sqrt(1+r*r))/(1+r*r)**(3*j),0,math.inf,epsabs=1e-10,epsrel=1e-10)[0]
    bound=math.pi**j*math.factorial(2*j-1)/math.factorial(3*j-1)*J0
    assert 0<actual<=bound
    checks.append({'name':f'Physical radial direct-extension norm on C^{dimension},j={j}','actual':actual,'proved_upper_bound':bound,'pass':True})
growth_example=quad(lambda r:2*math.pi**2*r**3/(1+r*r)**5,0,math.inf)[0]
check('Growth example actual C2 norm',growth_example,math.pi**2/12)
for epsilon in [.1,.03,.001]:
    physical=quad(lambda r:2*math.pi/r,epsilon,1)[0]
    check('Hypothetical rescaled normal pole,epsilon='+str(epsilon),physical,2*math.pi*math.log(1/epsilon))
record={'schema':'AN02-L145-independent-example-checks147/v1','status':'PASS','checks':checks,'count':len(checks),'meaning':'Physical radial quadratures supplement the complete exact integration,extension and trace proofs. The hypothetical pole checks do not claim a returned solution has a pole.'}
(HERE/'independent-example-checks147.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','count':len(checks),'actual_annular_norm':annular,'radial_input_J0':J0,'growth_example_norm':growth_example}))
