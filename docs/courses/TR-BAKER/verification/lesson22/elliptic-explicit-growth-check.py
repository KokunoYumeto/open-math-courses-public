"""Exact constant certificates and numerical checks for 22.175--183."""
from collections import Counter
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import mpmath as mp
import sympy as sp


def elliptic_values(tau, z, terms=80):
    """Product and Fourier series; callers keep points away from the lattice."""
    q = mp.exp(2j * mp.pi * tau)
    w = mp.exp(2j * mp.pi * z)
    product = mp.mpc(1)
    logarithmic_derivative = mp.mpc(0)
    fourier = mp.mpf(1)/12 + w/(w-1)**2
    fourier_derivative = w*(1+w)/(1-w)**3
    qr = q
    for _ in range(terms):
        b, c = w*qr, qr/w
        product *= (1-b)*(1-c)/(1-qr)**2
        logarithmic_derivative += 2j*mp.pi*(-b/(1-b)+c/(1-c))
        fourier += b/(1-b)**2 + c/(1-c)**2 - 2*qr/(1-qr)**2
        fourier_derivative += b*(1+b)/(1-b)**3 - c*(1+c)/(1-c)**3
        qr *= q
    phi = mp.expm1(2j*mp.pi*z)/(2j*mp.pi)*product
    phip = w*product + phi*logarithmic_derivative
    wp = -4*mp.pi**2*fourier
    wpp = -8j*mp.pi**3*fourier_derivative
    return phi, phip, wp, wpp


def run_checks():
    exact, numerical = Counter(), Counter()
    def ex(name, condition):
        assert condition, name
        exact[name] += 1
    def close(name, a, b, tol=mp.mpf('1e-58')):
        assert abs(a-b) <= tol*max(1, abs(a), abs(b)), (name, a, b)
        numerical[name] += 1
    def num(name, condition):
        assert condition, name
        numerical[name] += 1

    arctan_sum = lambda t, n: sum(((-1)**k*t**(2*k+1)/F(2*k+1)
                                  for k in range(n+1)), F(0))
    ex('pi_lower_certificate', F(157,50) < 4*(arctan_sum(F(1,2),5)+arctan_sum(F(1,3),5)))
    ex('pi_upper_certificate', 4*(arctan_sum(F(1,2),4)+arctan_sum(F(1,3),4)) < F(22,7))
    ex('sqrt_three_lower', F(433,250)**2 < 3)
    x=F(67981,12500)
    ex('exponent_product', x == F(157,50)*F(433,250))
    for t, target, n in [(x, F(230),30),(x/2,F(500,33),25),(x/8,F(1000,507),20)]:
        ex('exponential_lower_certificate', sum((t**k/F(factorial(k)) for k in range(n+1)),F(0)) > target)
    Q, h = F(1,230), F(33,500)
    ex('product_exponent', 2*Q/(1-Q)**2 + h*(1+Q)/(1-Q) < F(19,250))
    b=F(19,250)
    exp_upper=sum((b**k/F(factorial(k)) for k in range(12)), F(0)) + b**12/F(factorial(12))/(1-b/13)
    ex('product_constant', exp_upper < F(1079,1000))
    ex('log_derivative_constant', h*(1+Q)/(1-Q)/(1-h) < F(72,1000))
    ex('prefactor_constant', F(1079,1000)/(2*F(157,50)) < F(172,1000))
    ex('phi_gaussian_constant', F(172,1000)*F(1507,1000) < F(26,100))
    ex('derivative_cell_constant', F(1079,1000)*(1+F(72,1000)*F(1507,1000)) < F(1197,1000))
    ex('halfperiod_lower_constant', F(7,22)*(1-4*Q/(1-Q)**2) > F(312,1000))
    ex('halfperiod_wp_constant', F(2,3)*F(22,7)**2+16*F(22,7)**2*Q/(1-Q)**3 < F(73,10))
    ex('first_coordinate_constant', F(26,100)**3 < F(176,10000))
    ex('second_coordinate_constant', F(26,100)**3*(F(73,10)+1/F(312,1000)**2) < F(309,1000))
    ex('third_coordinate_exact', 4*F(26,100)**2*F(1197,1000)/F(312,1000)**2 == F(3325,1000))
    ex('final_upper_constant', F(3325,1000) < F(333,100))
    ex('product_lower_exponent', F(72,1000)+2*Q/(1-Q)<F(81,1000))
    ex('product_lower_prefactor', F(919,1000)*F(7,44)>F(146,1000))
    ex('wp_prime_tail', h*(1+Q)/(1-Q)*(1+h)/(1-h)**3<F(1,10))
    ex('wp_tail', F(1,12)+h*(1+Q)/(1-Q)/(1-h)**2+2*Q/(1-Q)**3<F(1,5))
    ex('tuple_cell_lower', F(919,1000)**3*(F(3,4)-F(1,80))>F(73,1000)**3)
    comparison_exponent=F(13,100)*x
    ex('david_tuple_lower_constant', F(73,1000)**3*(1+comparison_exponent+comparison_exponent**2/2)>F(7,10000))
    ex('denominator_cell_lower', 8*F(157,50)**2*F(45,100)*F(146,1000)>F(73,1000))

    n, m, v, y = sp.symbols('n m v y', real=True)
    J=lambda t: t*t/y-t+y/4
    ex('gaussian_translation_identity', sp.expand(J(v+n*y)-J(v)-(2*n*v+(n*n-n)*y)) == 0)
    # Logarithms of automorphy multipliers compose up to the exact integer sign.
    z, tau = sp.symbols('z tau')
    exponent=lambda k, a: -2*k*a-k*(k-1)*tau
    ex('automorphy_cocycle', sp.expand(exponent(n,z+m*tau)+exponent(m,z)-exponent(m+n,z)) == 0)
    f,g,e=sp.symbols('f g e')
    fp,gp=sp.symbols('fp gp')
    ex('differentiated_halfperiod_cancellation', sp.expand(f*(2*e*f*fp+gp)-2*fp*(e*f*f+g)-(f*gp-2*fp*g)) == 0)
    # Half-period sign at the trigonometric limit, including the pole cancellation.
    zz=sp.symbols('zz')
    phi0=(sp.exp(2*sp.pi*sp.I*zz)-1)/(2*sp.pi*sp.I)
    wp0=sp.pi**2/sp.sin(sp.pi*zz)**2-sp.pi**2/3
    ex('normalization_at_zero', sp.limit(phi0**2*wp0,zz,0)==1)
    w=sp.symbols('w')
    ex('halfperiod_sign', sp.expand((w-1)**2/12+w-(-(w-1)**2/6+(w+1)**2/4))==0)

    mp.mp.dps=80
    taus=[1j, mp.mpf('0.5')+1j*mp.sqrt(3)/2, -mp.mpf('0.5')+1j*mp.sqrt(3)/2,
          mp.mpf('0.27')+mp.mpf('1.4')*1j]
    for tau in taus:
        y=mp.im(tau)
        half=elliptic_values(tau,mp.mpf('0.5'))
        num('halfperiod_phi_lower',abs(half[0])>mp.mpf('0.312'))
        num('halfperiod_wp_upper',abs(half[2])<mp.mpf('7.3'))
        for s,t in [(mp.mpf(1)/3,mp.mpf(0)),(mp.mpf('0.17'),mp.mpf('0.5')),
                    (-mp.mpf('0.49'),-mp.mpf('0.5')),(mp.mpf('0.001'),mp.mpf('0.002')),
                    (mp.mpf('0.43'),mp.mpf('-0.31'))]:
            z=s+t*tau; phi,phip,wp,wpp=elliptic_values(tau,z)
            j=y*(t-mp.mpf('0.5'))**2
            num('cell_phi_bound',abs(phi)<mp.mpf('0.26')*mp.exp(mp.pi*j))
            num('cell_derivative_bound',abs(phip)<mp.mpf('1.197')*mp.exp(mp.pi*j))
            num('cell_denominator_lower',abs(phi)*(1+abs(wp))>=mp.mpf('0.073'))
            left,right=elliptic_values(tau,z+mp.mpf('0.5')),elliptic_values(tau,z-mp.mpf('0.5'))
            G=left[0]*right[0]/half[0]**2
            Gp=(left[1]*right[0]+left[0]*right[1])/half[0]**2
            close('halfperiod_identity',phi**2*wp,half[2]*phi**2+G)
            close('differentiated_identity',phi**3*wpp,phi*Gp-2*phip*G)
            close('wp_fourier_derivative',mp.diff(lambda u:elliptic_values(tau,u)[2],z),wpp)
            close('product_derivative',mp.diff(lambda u:elliptic_values(tau,u)[0],z),phip)
            for n in [-3,-1,1,3]:
                target=z+1+n*tau
                translated=elliptic_values(tau,target)
                A=(-1)**n*mp.exp(-2j*mp.pi*n*z-1j*mp.pi*n*(n-1)*tau)
                close('denominator_automorphy',translated[0],A*phi)
                close('derivative_automorphy',translated[1],A*(phip-2j*mp.pi*n*phi))
                close('wp_periodicity',translated[2],wp)
                close('wp_prime_periodicity',translated[3],wpp)
                im=mp.im(target); Jt=im**2/y-im+y/4
                norm=abs(translated[0])**3*max(1,abs(translated[2]),abs(translated[3]))
                num('global_tuple_bound',norm<=mp.mpf('3.33')*mp.exp(3*mp.pi*Jt))
                num('global_tuple_lower',norm>=mp.mpf('0.073')**3*mp.exp(3*mp.pi*(Jt-y)))
                num('david_tuple_lower',norm>=mp.mpf('0.0007')*mp.exp(mp.pi*(-mp.mpf('2.51')*y-3*abs(im)+3*im**2/y)))
                num('global_denominator_lower',abs(translated[0])*(1+abs(translated[2]))>=mp.mpf('0.073')*mp.exp(-2*mp.pi*abs(im)))
    phi,phip,_,_=elliptic_values(1j,mp.mpf(1)/3)
    derivative_ratio=mp.exp(-mp.pi/4)*abs(phip+20j*mp.pi*phi)
    num('global_derivative_counterexample',derivative_ratio>mp.mpf('1.197'))
    return {'exact':{'total':sum(exact.values()),'families':dict(exact)},
            'numerical':{'total':sum(numerical.values()),'families':dict(numerical),
                         'precision_decimal_digits':80,'terms':80,'relative_tolerance':'1e-58',
                         'derivative_counterexample':{'tau':'i','z':'1/3-10i','ratio_to_exp_pi_J':mp.nstr(derivative_ratio,25)}},
            'scope':'Exact rational constants and symbolic cancellation; numerical identities and samples are supplementary, not proofs or numerical elliptic-logarithm bounds.'}


if __name__=='__main__':
    result=run_checks()
    target=Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
