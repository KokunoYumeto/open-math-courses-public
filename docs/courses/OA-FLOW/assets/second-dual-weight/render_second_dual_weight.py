"""Exact second-dual kernel diagram. Original code/data/art: CC0-1.0.

Run with Python 3, SymPy and Matplotlib. Outputs are relative to this file.
Font components retain the complete terms copied to FONT-LICENSE.txt.
"""
from pathlib import Path
import hashlib
import json
import shutil

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import sympy as sp

HERE = Path(__file__).resolve().parent
I = sp.I
K = [[sp.Matrix([[1, 2], [0, I]]), sp.Matrix([[0, 1], [2, 0]])],
     [sp.Matrix([[1, 0], [3, I]]), sp.Matrix([[I, 0], [1, 2]])]]
D = [sp.diag(2, 5), sp.diag(5, 2)]
Q, R = sp.diag(2, 5, 2, 5), sp.diag(2, 5, 5, 2)
c = 3
B = c * sp.BlockMatrix(K).as_explicit()
correct = [[sp.trace(D[s] * K[r][s].H * K[r][s])
            for s in range(2)] for r in range(2)]
wrong = [[sp.trace(D[r] * K[r][s].H * K[r][s])
          for s in range(2)] for r in range(2)]
Y = B.H * Q**sp.Rational(1, 2)
Z = R**sp.Rational(1, 2) * Y * Q**sp.Rational(-1, 2)
assert correct == [[27, 22], [25, 18]]
assert wrong == [[27, 13], [52, 18]]
assert sp.trace(R * B.H * B) == c*c*sum(map(sum, correct)) == 828
assert sp.trace(Z.H * Z) == 828
assert c*c*sum(map(sum, wrong)) == 990
assert Z == R**sp.Rational(1, 2)*B.H

def matrix_strings(m):
    return [[str(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]

data = {
    'license': 'CC0-1.0; font terms are separate',
    'group': 'Z/2', 'singleton_Haar_mass': 3,
    'singleton_dual_Haar_mass': '1/6', 'total_Haar_mass': 6,
    'coefficient_density': [2, 5], 'action': 'flip conjugation',
    'coordinate_order': ['(0,1)', '(0,2)', '(1,1)', '(1,2)'],
    'kernel_blocks': [[matrix_strings(k) for k in row] for row in K],
    'normalized_matrix_B': matrix_strings(B),
    'reference_density_Q': [2, 5, 2, 5],
    'second_dual_density_R': [2, 5, 5, 2],
    'correct_column_contributions': [[int(x) for x in row] for row in correct],
    'incorrect_row_contributions': [[int(x) for x in row] for row in wrong],
    'correct_weight': 828, 'incorrect_weight': 990,
    'relative_half_power_norm_squared': 828,
    'equations': {
        'matrix': 'B_rs = 3 K_rs',
        'cocycle': 'C_t = R^(it) Q^(-it)',
        'weight': '9 sum_(r,s) Tr(D_s K_rs* K_rs)',
        'relative_vector': 'Delta_(W,Omega)^(1/2) Lambda_Omega(B*) = R^(1/2) B*'},
    'proof_locators': ['OA-FLOW-L33.md#l33-finite-model',
                       'OA-FLOW-L33.md#l33-kernel-diagnostic'],
    'human_antecedent': 'Takesaki, Theory of Operator Algebras II, X.2 formula (16), p.260; the proof discussion on p.263 points to VIII.3.15',
    'verification': 'Exact SymPy matrix arithmetic, including direct full-matrix and relative-square-root calculations',
}
(HERE/'second-dual-weight-data.json').write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
font_license = Path(matplotlib.get_data_path())/'fonts/ttf/LICENSE_DEJAVU'
shutil.copyfile(font_license, HERE/'FONT-LICENSE.txt')

plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans',
                     'svg.fonttype': 'path', 'svg.hashsalt': 'OA-FLOW-L33-exact-kernel',
                     'font.size': 14})
INK, BLUE, PURPLE, GRAY = '#17273b', '#126b94', '#804eab', '#526374'
PALE_BLUE, PALE_PURPLE = '#e9f5fb', '#f4edfa'
fig = plt.figure(figsize=(16, 11.2), facecolor='#f7f9fc')
fig.text(.045, .955, 'Where the second-dual weight reads a kernel',
         fontsize=27, color=INK, weight='bold', va='top')
fig.text(.045, .911, 'Exact example: G = Z/2, singleton Haar mass 3, coefficient weight Tr(diag(2,5) ·).',
         fontsize=15, color=GRAY, va='top')

def panel(rect, title):
    ax = fig.add_axes(rect)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
    ax.add_patch(FancyBboxPatch((.008, .008), .984, .984,
                 boxstyle='round,pad=0.007,rounding_size=0.025',
                 facecolor='white', edgecolor='#d5deea', linewidth=1.2))
    ax.text(.045, .934, title, color=INK, fontsize=18, weight='bold', va='top')
    return ax

a = panel([.045, .515, .438, .354], 'A  The density is a row multiplier')
a.text(.05, .785, r'$Q=\operatorname{diag}(2,5\;|\;2,5)$', fontsize=21, color=GRAY)
a.text(.05, .650, r'$R=\operatorname{diag}(2,5\;|\;5,2)$', fontsize=21, color=BLUE)
a.text(.08, .548, 'row 0: D₀ = diag(2,5)', fontsize=14, color=BLUE)
a.text(.08, .464, 'row 1: D₁ = diag(5,2)', fontsize=14, color=PURPLE)
a.text(.05, .338, r'$[DW:D\Omega]_t=C_t=R^{it}Q^{-it}$', fontsize=20, color=INK)
a.text(.05, .222, r'$c_t(0)=1,\quad c_t(1)=\operatorname{diag}((5/2)^{it},(2/5)^{it})$',
       fontsize=16.5, color=INK)
a.text(.05, .080, 'Usual trace: every rank-one group projection has trace 1.',
       fontsize=13.4, color=GRAY)

b = panel([.517, .515, .438, .354], 'B  Haar-normalized matrix entries')
b.text(.05, .787, r'$e_s=3^{-1/2}1_{\{s\}},\qquad B_{rs}=3K_{rs}$',
       fontsize=20, color=INK)
b.text(.074, .48, r'$B=3$', fontsize=24, color=INK, va='center')
labels = [['1','2','0','1'], ['0','i','2','0'],
          ['1','0','i','0'], ['3','i','1','2']]
x0, y0, dx, dy = .32, .625, .125, .112
for r in range(4):
    for s in range(4):
        b.add_patch(Rectangle((x0+s*dx-dx/2, y0-r*dy-dy/2), dx, dy,
                             facecolor=PALE_BLUE if s<2 else PALE_PURPLE, edgecolor='white'))
        b.text(x0+s*dx, y0-r*dy, '$'+labels[r][s]+'$',
               ha='center', va='center', fontsize=22, color=INK)
b.plot([.255,.242,.242,.255],[.683,.683,.222,.222], color=INK, lw=1.5)
b.plot([.757,.770,.770,.757],[.683,.683,.222,.222], color=INK, lw=1.5)
b.plot([.503,.503],[.225,.68], color='#9eabba', lw=1)
b.plot([.25,.76],[.457,.457], color='#9eabba', lw=1)
b.text(.383, .726, 'column s = 0', ha='center', color=BLUE, fontsize=12)
b.text(.631, .726, 'column s = 1', ha='center', color=PURPLE, fontsize=12)
b.text(.05, .105, 'Group Haar mass = 6; dual singleton mass = 1/6.', fontsize=13.5, color=GRAY)
b.text(.05, .040, 'The quadratic kernel sum has factor 3² = 9.', fontsize=13.5, color=GRAY)

cc = panel([.045, .085, .438, .395], 'C  The adjoint swaps the coordinates')
steps = [(.754, PALE_BLUE, r'$K_{rs}$', 'original kernel: row r, column s'),
         (.502, PALE_PURPLE, r'$(B^*)_{sr}=3K_{rs}^*$', 'adjoint matrix: row s, column r'),
         (.250, '#edf7f0', r'$(R^{1/2}B^*)_{sr}=3D_s^{1/2}K_{rs}^*$',
          'relative half-power: density acts at row s')]
for y, color, formula, subtitle in steps:
    cc.add_patch(FancyBboxPatch((.045,y-.092),.91,.180,boxstyle='round,pad=0.006,rounding_size=.02',
                               facecolor=color,edgecolor='none'))
    cc.text(.5,y+.025,formula,ha='center',va='center',fontsize=21 if y>.3 else 19,color=INK)
    cc.text(.5,y-.049,subtitle,ha='center',va='center',fontsize=13,color=GRAY)
for y in [.632,.380]:
    cc.annotate('',xy=(.5,y-.029),xytext=(.5,y+.030),
                arrowprops={'arrowstyle':'->','color':GRAY,'lw':1.4})
cc.text(.5,.063,'Original column s becomes the row acted on by the density.',
        ha='center',fontsize=13,color=INK)

d = panel([.517, .085, .438, .395], 'D  Four exact contributions')
d.text(.055,.806,r'$a_{rs}=\operatorname{Tr}_2(D_sK_{rs}^*K_{rs})$',fontsize=21,color=INK)
d.text(.343,.722,'s = 0: weights (2,5)',ha='center',color=BLUE,fontsize=13)
d.text(.733,.722,'s = 1: weights (5,2)',ha='center',color=PURPLE,fontsize=13)
entries = [[('1·2 + 5·5','27'),('4·5 + 1·2','22')],
           [('10·2 + 1·5','25'),('2·5 + 4·2','18')]]
for r in range(2):
    yy=.585-.204*r
    d.text(.058,yy,'r = '+str(r),va='center',fontsize=13,color=GRAY)
    for s in range(2):
        xx=.343+.390*s
        d.add_patch(FancyBboxPatch((xx-.177,yy-.082),.354,.171,
                     boxstyle='round,pad=.007,rounding_size=.02',
                     facecolor=PALE_BLUE if s==0 else PALE_PURPLE,edgecolor='none'))
        d.text(xx,yy+.028,entries[r][s][0],ha='center',fontsize=14,color=GRAY)
        d.text(xx,yy-.048,entries[r][s][1],ha='center',fontsize=23,weight='bold',color=BLUE if s==0 else PURPLE)
d.text(.055,.179,r'$W(B^*B)=9(27+22+25+18)=828$',fontsize=20,color=INK)
d.text(.055,.069,'Using Dᵣ before the adjoint instead gives 990 (error 162).',
       fontsize=13.4,color=GRAY)

fig.text(.045,.045,'Proof: OA-FLOW-L33, §7 finite model and §8 Diagnostic 1.  Exact matrix data, not a numerical approximation.',
         fontsize=12,color=GRAY)
fig.text(.045,.023,'Original diagram / data / renderer: CC0-1.0.  Antecedent: Takesaki II, X.2 formula (16), p.260.  Font terms accompany the source.',
         fontsize=11,color=GRAY)
for extension in ['svg','png']:
    fig.savefig(HERE/('second-dual-weight.'+extension), dpi=200,
                metadata={'Creator':'Original mathematical renderer; CC0-1.0',
                          'Date':'2026-10-06'} if extension=='svg' else {})
plt.close(fig)
print(json.dumps({'exact_checks':'pass','correct':828,'incorrect':990,
                  'png_size':[3200,2240], 'files':[p.name for p in sorted(HERE.iterdir())]}))
