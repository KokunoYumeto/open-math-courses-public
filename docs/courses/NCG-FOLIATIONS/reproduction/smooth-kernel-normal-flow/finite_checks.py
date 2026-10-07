"""CC0 exact finite samples for the smooth labelled-kernel example."""
from fractions import Fraction as Q
from pathlib import Path
import argparse,json

EPS=Q(1,8)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(q,a):return (q*a[0],q*a[1])
def polynomial(n):
    m=(n+1)**2;l=n*n
    s={m:(Q(0),Q(-1,2)),-m:(Q(0),Q(1,2)),l:(Q(0),Q(1,2)),-l:(Q(0),Q(-1,2))}
    a={0:(Q(1),Q(0))}
    for k,v in s.items():a[k]=add(a.get(k,(Q(0),Q(0))),scale(2*EPS,v))
    for k,v in s.items():
        for j,w in s.items():a[k+j]=add(a.get(k+j,(Q(0),Q(0))),scale(EPS*EPS,mul(v,w)))
    return {k:v for k,v in a.items() if v!=(0,0)}
def run():
    checks=[]
    def check(name,passed,scope):
        assert passed,name
        checks.append(dict(name=name,passed=bool(passed),scope=scope))
    f=lambda n:Q(n)+(EPS if n%2 else 0)
    check('quarter-circle-controls',all(max(Q(0),abs(d)-2*EPS)<=abs(f(n+d)-f(n))<=abs(d)+2*EPS for n in range(-5,6) for d in range(-4,5)), '99 exact distances at x=1/4; CK.3')
    ns=[4,8,16,32,64]
    samples=[dict(n=n,t=str(Q(1,4*n+2)),cosine_angle_over_pi=str(Q(1,4)+Q(1,8*n+4)),derivative_over_pi=str(Q(2*n+1,2))) for n in ns]
    check('normal-flow-angle-bound',all(Q(1,4)+Q(1,8*n+4)<=Q(5,18)<Q(1,3) for n in ns),'Exact rational angles imply cosine >=1/2; CK.6')
    check('exact-flow-margin',(1+EPS)**2-1==Q(17,64),'Exact margin in CK.7')
    check('negative-fourier-coefficient',all(polynomial(n).get(-(n+1)**2)==(Q(0),EPS) for n in range(4,68)),'64 exact Gaussian-rational Fourier polynomials; CK.8')
    labels=[-3,-1,0,2,5];cs=[2,-1,-2,0,1]
    quadratic=sum(Q(cs[i]*cs[j])*(f(labels[i])-f(labels[j]))**2 for i in range(5) for j in range(5))
    check('exact-squared-distance-CND',sum(cs)==0 and quadratic==-2*sum(Q(c)*f(n) for c,n in zip(cs,labels))**2,'One exact zero-sum five-label Gram calculation; CK.2')
    check('phase-margin',EPS/2==Q(1,16),'Exact bounded-phase lower margin; CK.8')
    return dict(schema='smooth-labelled-kernel-finite-samples/v1',result='passed',checks=checks,count=len(checks),epsilon=str(EPS),sample_base='x=1/4 on R/Z',samples=samples,flow_margin='17/64',phase_margin='1/16',scope='Finite exact samples supplement CK.1–CK.9; the infinite-label conclusions are proved in the lesson.')
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,default=Path('finite-checks.json'));args=parser.parse_args()
    result=run();args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(dict(result=result['result'],checks=result['count'])))
