"""CC0. Ball checks of the elementary numerical margins in Section 7."""
from flint import arb, ctx
from pathlib import Path
import json, math
from fractions import Fraction
ctx.dps=80
pi=arb.pi()
C2=2+arb.const_euler()-(4*pi).log()
assert 0<C2<arb('0.05')
H1000=sum((arb(1)/n for n in range(1,1001)),arb(0))
assert H1000-arb(1000).log()<arb('0.58')
assert pi>arb('3.14') and arb('2.53').exp()<arb('12.56')
T=arb(68).exp(); y=T/2
quotient_lower=1/(1+4/T**2)
assert quotient_lower>arb('0.999')
assert pi<arb(22)/7
exact_coefficient=2*Fraction(7,22)*Fraction(19,20)*Fraction(999,1000)
assert exact_coefficient==Fraction(132867,220000)>Fraction(3,5)
sine_coefficient_lower=2*(arb(19)/20)*(arb(999)/1000)/pi
assert sine_coefficient_lower>arb('0.6')
main=arb('0.6')*(68-10)/(8*pi)-arb('0.026')
assert main>arb('1.35')
# e^z >= z^6/6!, so this upper bound avoids computing an enormous exp.
tail=arb(10)**35/(T*T*y**3)+200/y+10**5*(1+y)*math.factorial(6)*(16/y)**6
assert tail<arb('0.01')
log_u_bound=arb(4).log()+4*T*68**2
assert log_u_bound<arb(78).exp()
skewes_triple_log=(arb(10).log().log()+arb(10).log()*arb(10)**34).log()
assert skewes_triple_log>79
receipt={'license':'CC0-1.0','decimal_precision':80,
 'sine_block_quotient_lower_bound':quotient_lower.str(70),
 'sine_block_exact_coefficient':str(exact_coefficient),
 'sine_block_coefficient_lower_bound':sine_coefficient_lower.str(70),
 'sine_block_explanation':'Theorem7.2 proves the sine and pi estimates locally. Its999/1000 quotient bound makes the exact rational coefficient132867/220000 greater than3/5; the downstream0.6 margin is justified.',
 'C2':C2.str(70),'negative_S_lower_bound':main.str(70),
 'smoothing_error_upper_bound':tail.str(70),
 'upper_bound_log_log_log_x':log_u_bound.log().str(70),
 'decimal_Skewes_bound_triple_log':skewes_triple_log.str(70),
 'all_checks_passed':True}
Path(__file__).with_name('lesson15_constants.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
