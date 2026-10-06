"""Exact parameter certificate for the two-logarithm determinant theorem.

Written by GPT-6.1 Sol (OpenAI), Ultra. Original code dedicated under CC0.
The theorem and all proof steps are in the accompanying lesson.
Uses only Python's standard library; no floating-point claims are required.
"""
from fractions import Fraction
from math import gcd

def logarithm_interval(x, order):
    t=Fraction(x-1,x+1)
    lower=2*sum((t**(2*j+1)/Fraction(2*j+1) for j in range(order+1)),Fraction(0))
    tail=2*t**(2*order+3)/((2*order+3)*(1-t*t))
    return lower,lower+tail

lo2,hi2=logarithm_interval(2,30)
lo3,hi3=logarithm_interval(3,30)
assert Fraction(69,100)<lo2<hi2<Fraction(7,10)
assert 1<lo3<hi3<Fraction(11,10)
b1,b2=176251,111202
assert gcd(b1,b2)==1
lambda_lower=b2*lo3-b1*hi2
lambda_upper=b2*hi3-b1*lo2
assert Fraction(3600,10**9)<lambda_lower<lambda_upper<Fraction(3601,10**9)
K,L=500000,500
R1,S1,R2,S2=500,500,16000,16000
N=K*L
R,S=R1+R2-1,S1+S2-1
assert R2<b1 and S2<b2  # Coprimality then certifies injectivity.
assert R1>=L            # Distinct powers of 2 certify the first grid.
assert R2*S2>(K-1)*L
W=(R-1)*b2+(S-1)*b1
assert W==4742399594 and W<2**33 and N<2**28
left_lower=(N-K)*Fraction(69,100)
right_upper=4*28*Fraction(7,10)+2*K*33*Fraction(7,10)+6*L*(R*Fraction(7,10)+S*Fraction(11,10))
assert left_lower==172155000
assert right_upper==Fraction(1121946784,10)
assert left_lower-right_upper>59000000
print("Both grid cardinalities, the branch ordering and the parameter inequality are certified.")
print("0.000003600 < Lambda < 0.000003601")
print("Parameter-inequality margin exceeds 59,000,000.")
