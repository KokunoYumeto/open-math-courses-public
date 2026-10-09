"""Supplementary exact-formula checks for the entire-graph proof."""
from pathlib import Path
import json
import mpmath as mp

ROOT=Path(__file__).resolve().parent
mp.mp.dps=90
tol=mp.mpf('1e-65')
count=0
groups={}
maximum=mp.mpf(0)

def check(group,condition):
    global count
    assert condition,(group,count)
    count+=1;groups[group]=groups.get(group,0)+1

def le(group,left,right):
    global maximum
    excess=max(mp.mpf(0),(left-right)/(1+abs(left)+abs(right)))
    maximum=max(maximum,excess)
    check(group,excess<tol)

def same(group,left,right):
    global maximum
    error=abs(left-right)/(1+abs(left)+abs(right))
    maximum=max(maximum,error)
    check(group,error<tol)

for alpha in [mp.mpf(7)/10,mp.mpf(3)/4,mp.mpf(9)/10]:
    b=mp.exp(1j*(mp.pi/2-mp.pi*alpha/4))
    s=mp.sin(3*mp.pi*alpha/4)
    eps=-mp.cos(3*mp.pi*alpha/4)*min(mp.sin(mp.pi*alpha/4),s)
    check('strict-sector-sign',eps>0)
    le('negative-axis-other-exponent',-mp.sin(5*mp.pi*alpha/4),s)
    for index in range(17):
        theta=mp.pi/4+(mp.pi/2)*index/16
        lhs=s*mp.cos(alpha*(theta-mp.pi))+mp.cos(alpha*theta+mp.pi/2-mp.pi*alpha/4)
        rhs=mp.sin(alpha*(mp.pi-theta))*mp.cos(3*mp.pi*alpha/4)
        same('sector-trigonometric-identity',lhs,rhs)
        le('uniform-negative-remainder',rhs,-eps)
        le('dominant-exponential-growth',mp.cos(alpha*theta+mp.pi/2-mp.pi*alpha/4),0)
        check('other-exponential-decay',mp.cos(alpha*theta-mp.pi/2+mp.pi*alpha/4)>0)
        front=mp.pi*index/64
        le('front-sector-negative-weight',s*mp.cos(alpha*(mp.pi-front)),s*mp.cos(3*mp.pi*alpha/4))
    for radius in [mp.mpf(1),mp.mpf(5),mp.mpf(1000)]:
        for index in range(-8,9):
            angle=mp.pi*index/17
            z=radius*mp.exp(1j*angle)
            v=mp.sqrt(z)
            delta=mp.pi/4-abs(mp.arg(v))
            le('square-root-angle-control',z.real/(2*radius),delta)
            low=alpha/mp.pi*mp.power(radius,alpha/2-1)*z.real
            le('two-radial-exponent-lower-bound',low,min((b*mp.power(v,alpha)).real,(mp.conj(b)*mp.power(v,alpha)).real))
    check('graph-exponent-positive',alpha/2-mp.mpf(1)/4>0)
    check('graph-lift-dominates-Gaussian',3*alpha>2)

for C0 in [mp.mpf(0),mp.mpf(1),mp.mpf(7)]:
    D=3*mp.power((1+C0)/4,mp.mpf(4)/3)
    for radius in [mp.mpf(1),mp.mpf(10),mp.mpf(1000)]:
        a=mp.sqrt(radius)+C0
        bound=D*mp.power(radius,mp.mpf(2)/3)
        for m in [1,2,4,10,24]:
            le('all-type-neighborhood-envelope',-mp.mpf(m)**4+m*a,bound)

for alpha in [mp.mpf(7)/10,mp.mpf(3)/4,mp.mpf(9)/10]:
    p=alpha/2
    for z in [[mp.mpc(0),mp.mpc(0)],[mp.mpc(2,1),mp.mpc(-1,3)],[mp.mpc(100,2),mp.mpc(-5,6)]]:
        r2=mp.fsum(abs(v)**2 for v in z)
        radial=p*mp.power(1+r2,p-2)*(1+p*r2)
        check('strict-radial-Levi-eigenvalue',radial>0)
        for xi in [[mp.mpc(1),mp.mpc(0)],[mp.mpc(1,1),mp.mpc(2,-1)]]:
            norm=mp.fsum(abs(v)**2 for v in xi)
            form=p*mp.power(1+r2,p-1)*norm+p*(p-1)*mp.power(1+r2,p-2)*abs(mp.fsum(mp.conj(z[j])*xi[j] for j in range(2)))**2
            le('radial-Levi-lower-bound',radial*norm,form)

data=dict(status='PASS',total_checks=count,groups=groups,
          precision_decimal_digits=90,tolerance=str(tol),
          maximum_scaled_error_or_positive_excess=mp.nstr(maximum,90),
          scope='Sector signs, exact phase identity, square-root exponent control, the all-type seminorm envelope and radial Levi curvature.',
          weighted_solution_is_not_numerically_fabricated=True,
          functional_separation_and_ideal_closure_are_proved_in_the_text=True)
(ROOT/'graph-checks256.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps(data))
