"""Exact number-field example for the kernel/image volume identity.

Original certificate: GPT-6.1 Sol (OpenAI), Codex, Ultra; October 2026. CC0.
This supplements the universal proof; one example is not that proof.
"""
from fractions import Fraction as F
import json
import sympy as s
from laurent_constant import Interval

root = s.sqrt(2)
# K=Q(sqrt(2)), Delta=8, Gamma=2 O_K direct_sum O_K direct_sum O_K.
# Archimedean weights at +sqrt(2): (2,1/2,1); at -sqrt(2): (3,5,1).
# The finite weight on column 1 is 1/4 at the norm-two prime (sqrt(2)).
weights = [[s.Rational(2), s.Rational(1, 2), s.Rational(1)],
           [s.Rational(3), s.Rational(5), s.Rational(1)]]
embedding = s.zeros(6, 6)
for place, conjugate in enumerate((root, -root)):
    for column, multiple in enumerate((2, 1, 1)):
        embedding[3*place+column, 2*column] = multiple/weights[place][column]
        embedding[3*place+column, 2*column+1] = multiple*conjugate/weights[place][column]

# Coordinates of A p in the integral basis (1,sqrt(2)), for A=(1,sqrt(2),1+sqrt(2)).
integer_map = s.Matrix([[2, 0, 0, 2, 1, 2],
                        [0, 2, 1, 0, 1, 1]])
# All kernel points: freely choose a,b,d,f, then e=-2a-2d-2f,
# c=2a-2b+2d+f. Thus these columns form the full integer kernel.
kernel = s.Matrix([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [2, -2, 2, 1],
                   [0, 0, 1, 0],
                   [-2, 0, -2, -2],
                   [0, 0, 0, 1]])
assert integer_map*kernel == s.zeros(2, 4)
# Column p3 contributes the unit 1+sqrt(2): its norm is -1, so A Gamma=O_K.
assert s.Matrix([[1, 2], [1, 1]]).det() == -1
image_covolume_squared = s.Integer(8)
kernel_gram = (embedding*kernel).T*(embedding*kernel)
kernel_covolume_squared = s.simplify(kernel_gram.det())
full_covolume_squared = s.simplify(embedding.det()**2)
assert s.simplify(full_covolume_squared-8**3*s.Rational(4, 15)**2) == 0
local_row_squared = []
for place, conjugate in enumerate((root, -root)):
    row = [1, conjugate, 1+conjugate]
    local_row_squared.append(s.expand(sum((row[j]*weights[place][j])**2 for j in range(3))))
jacobian_squared = s.expand(local_row_squared[0]*local_row_squared[1])
assert s.simplify(kernel_covolume_squared*image_covolume_squared
                  -full_covolume_squared*jacobian_squared) == 0

# Witness p=(0,1,-2+sqrt(2)) meets the finite constraints and A p=0.
assert s.simplify(root+(1+root)*(-2+root)) == 0
root_interval = Interval(2).sqrt()
local_plus_squared = 4+(-2+root_interval)**2
local_minus_squared = F(1, 25)+(2+root_interval)**2
witness_height_fourth = local_plus_squared*local_minus_squared
jacobian = ((F(15, 2)+2*root_interval)*(62-2*root_interval)).sqrt()
# Exact row sums: 15/2+2sqrt(2) and 62-2sqrt(2).
assert s.simplify(local_row_squared[0]-(s.Rational(15, 2)+2*root)) == 0
assert s.simplify(local_row_squared[1]-(62-2*root)) == 0
bound_fourth = F(128, 15)*jacobian
assert witness_height_fourth.hi < bound_fourth.lo

RESULT = {
    'status': 'exact algebraic kernel/image identity and rational witness comparison passed',
    'field': 'Q(sqrt(2))', 'discriminant': 8,
    'module': '2 O_K direct_sum O_K direct_sum O_K',
    'archimedean_weights': [['2', '1/2', '1'], ['3', '5', '1']],
    'finite_weights': 'q_1=1/4 at (sqrt(2)); all other finite weights are one',
    'full_covolume_squared': str(full_covolume_squared),
    'kernel_covolume_squared': str(kernel_covolume_squared),
    'image_covolume_squared': str(image_covolume_squared),
    'real_jacobian_squared': str(jacobian_squared),
    'identity': 'covol(kernel)^2*covol(image)^2 = covol(full)^2*Jacobian^2',
    'witness': ['0', '1', '-2+sqrt(2)'],
    'witness_height_fourth_upper_bound': str(witness_height_fourth.hi),
    'siegel_bound_fourth_lower_bound': str(bound_fourth.lo),
    'use': 'finite supplement to the complete number-field proof',
}
if __name__ == '__main__':
    print(json.dumps(RESULT, indent=2))
