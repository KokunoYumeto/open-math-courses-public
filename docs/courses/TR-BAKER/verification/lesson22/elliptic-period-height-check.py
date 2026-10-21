"""Exact and supplementary numerical checks of 22.184--190."""
from collections import Counter
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import importlib.util
import json
import mpmath as mp
import sympy as sp


def invariants(tau, terms=100):
    q=mp.exp(2j*mp.pi*tau)
    s3=s5=mp.mpc(0)
    qn=q
    for n in range(1,terms+1):
        s3+=n**3*qn/(1-qn)
        s5+=n**5*qn/(1-qn)
        qn*=q
    e4,e6=1+240*s3,1-504*s5
    g2,g3=4*mp.pi**4*e4/3,8*mp.pi**6*e6/27
    return q,e4,e6,g2,g3


def checks():
    exact,numeric=Counter(),Counter()
    def ex(family,condition):
        assert condition,family
        exact[family]+=1
    def nu(family,condition):
        assert condition,family
        numeric[family]+=1
    def exp_bounds(x,n=20):
        low=sum((x**k/F(factorial(k)) for k in range(n+1)),F(0))
        high=low+x**(n+1)/F(factorial(n+1))/(1-x/F(n+2))
        return low,high
    Q=F(1,230);pi=F(22,7)
    s3=lambda q:q*(1+4*q+q*q)/(1-q)**5
    s5=lambda q:q*(1+26*q+66*q*q+26*q**3+q**4)/(1-q)**7
    ex('invariant_g2_upper',F(4,3)*pi**4*(1+240*s3(Q))<272)
    ex('invariant_g3_upper',F(8,27)*pi**6*(1+504*s5(Q))<1005)
    q=sp.symbols('q')
    E4=1+sum(240*sp.divisor_sigma(n,3)*q**n for n in range(1,5))
    E6=1-sum(504*sp.divisor_sigma(n,5)*q**n for n in range(1,5))
    expected4=[1,240,2160,6720,17520]
    expected6=[1,-504,-16632,-122976,-532728]
    ex('e4_coefficients',[int(E4.expand().coeff(q,n)) for n in range(5)]==expected4)
    ex('e6_coefficients',[int(E6.expand().coeff(q,n)) for n in range(5)]==expected6)
    discrim=sp.Poly(sp.expand(E4**3-E6**2),q)
    expected=[0,1728,-41472,435456,-2543616,5104512,1525813632,50747641344,424509633216,2050306560000,4362564096000,6188120064000,5377771008000]
    ex('discriminant_coefficients',[int(discrim.nth(n)) for n in range(13)]==expected)
    A=sum(F(abs(c))*Q**n for n,c in enumerate(expected4))
    B=sum(F(abs(c))*Q**n for n,c in enumerate(expected6))
    R4=360*5**3*Q**5/(1-F(6,5)**3*Q)
    R6=630*5**5*Q**5/(1-F(6,5)**5*Q)
    error=(sum(F(abs(c))*Q**n for n,c in enumerate(expected) if n>=2)+R4*(3*A*A+3*A*R4+R4*R4)+R6*(2*B+R6))/(1728*Q)
    ex('discriminant_tail_certificate',error<F(10924,100000)<F(11,100))
    ex('period_lower_constant',exp_bounds(F(73,40))[1]**12<(2*F(157,50))**12*F(89,100))
    ex('period_upper_constant',exp_bounds(F(37,20))[0]**12>(2*F(22,7))**12*F(111,100))
    ex('nome_at_height_one',exp_bounds(F(157,25),30)[0]>500)
    ex('E4_lower_at_height_one',240*s3(F(1,500))<F(1,2))
    ex('imaginary_part_height_constant',1+5+F(25,2)>F(222,25))
    ex('scaled_first_g2_constant',F(176,10000)**4*272**3<F(333,100)**4)
    ex('scaled_second_g2_constant',F(309,1000)**4*272<F(333,100)**4)
    ex('scaled_first_g3_constant',F(176,10000)**2*1005<F(333,100)**2)
    ex('scaled_second_g3_constant',F(309,1000)**6*1005<F(333,100)**6)
    ex('zero_invariant_example_first',F(176,10000)**2*2010<F(333,100)**2)
    ex('zero_invariant_example_second',F(309,1000)**6*2010<F(333,100)**6)
    u=F(11,35)
    ex('sine_majorant',1+u*u/(6*(1-u*u/20))<F(102,100))
    ex('local_exponential_majorant',exp_bounds(F(22,35))[1]<F(15,8))
    pole_remainder=4*pi*pi*(F(1,12)+F(15,4)*Q/(1-Q)/(1-F(15,8)*Q)**2+2*Q/(1-Q)**3)
    ex('local_pole_remainder',pole_remainder<F(43,10))
    ex('local_pole_lower',1/F(102,100)**2-F(43,1000)>F(9,10))

    x=sp.symbols('x')
    power=x/(1-x)
    for n in range(1,6):
        power=sp.simplify(x*sp.diff(power,x))
        if n==3:ex('third_power_geometric_sum',sp.simplify(power-x*(1+4*x+x*x)/(1-x)**4)==0)
        if n==5:ex('fifth_power_geometric_sum',sp.simplify(power-x*(1+26*x+66*x*x+26*x**3+x**4)/(1-x)**6)==0)
    z,a,b,g2,g3=sp.symbols('z a b g2 g3')
    wp=z**-2+a*z**2+b*z**4
    identity=sp.expand(sp.diff(wp,z)**2-4*wp**3+g2*wp+g3)
    ex('laurent_g2',identity.coeff(z,-2)==g2-20*a)
    ex('laurent_g3',identity.coeff(z,0)==g3-28*b)
    x0,x1,x2=sp.symbols('x0 x1 x2')
    for T in range(1,8):
        for t in [0,T//2,T]:
            derivative_symbol=sp.Poly(sp.expand((5*x0+x1-2*x2)**t*(-7*x0+3*x1+x2)**(T-t)),x0,x1,x2)
            for d0 in [0,1,2,4]:
                norm=sum(abs(int(c)) for powers,c in derivative_symbol.terms() if powers[0]<=d0)
                ex('additive_degree_capped_directional_bound',norm<=3**T*7**min(d0,T)*3**T)

    mp.mp.dps=80
    path=Path(__file__).with_name('elliptic-explicit-growth-check.py')
    spec=importlib.util.spec_from_file_location('growth_previous',path)
    previous=importlib.util.module_from_spec(spec);spec.loader.exec_module(previous)
    taus=[1j,mp.mpf('0.5')+1j*mp.sqrt(3)/2,-mp.mpf('0.5')+1j*mp.sqrt(3)/2,
          mp.mpf('0.23')+mp.mpf('1.1')*1j,mp.mpf('-0.4')+mp.mpf('2.5')*1j]
    for tau in taus:
        q,e4,e6,g2,g3=invariants(tau)
        delta=e4**3-e6**2
        nu('discriminant_disk',abs(delta/(1728*q)-1)<mp.mpf('0.11'))
        nu('g2_uniform_bound',abs(g2)<272)
        nu('g3_uniform_bound',abs(g3)<1005)
        j=1728*e4**3/delta;y=mp.im(tau)
        if abs(g2)>mp.mpf('1e-60'):
            for omega in [mp.mpf('0.3'),2+1j]:
                curve_g2=g2/omega**4
                factor=abs(j)**(mp.mpf(1)/12)/(12*abs(curve_g2))**(mp.mpf(1)/4)
                lower=mp.exp(mp.mpf('1.825')-mp.pi*y/6)*factor
                upper=mp.exp(mp.mpf('1.85')-mp.pi*y/6)*factor
                nu('period_two_sided',lower<=abs(omega)<=upper)
        if y>1:nu('j_controls_imaginary_part',abs(j)>mp.exp(y))
        for radius in [mp.mpf('0.001'),mp.mpf('0.03'),mp.mpf('0.1')]:
            for angle in [0,mp.pi/4,mp.pi/2,3*mp.pi/4]:
                z=radius*mp.exp(1j*angle)
                wp=previous.elliptic_values(tau,z)[2]
                nu('local_pole_bound',abs(wp)>=mp.mpf('0.9')/abs(z)**2)
    return {'exact':{'total':sum(exact.values()),'families':dict(exact),'discriminant_relative_error_upper_rational':str(error),'discriminant_relative_error_decimal':str(float(error))},
            'numerical':{'total':sum(numeric.values()),'families':dict(numeric),'precision_decimal_digits':80,'series_terms':100},
            'scope':'Exact finite certificates for constants and symbolic expansions, plus supplementary numerical examples. Does not claim the full numerical elliptic-logarithm theorem.'}


if __name__=='__main__':
    result=checks()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
