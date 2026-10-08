"""Original L129 proof diagram and exact finite-model checks. CC0-1.0."""
from pathlib import Path
import json
import shutil
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import sympy as s

O = Path(__file__).resolve().parent
assert not (O / 'PACKAGE_SEAL.json').exists()
parser = argparse.ArgumentParser()
parser.add_argument('--output', default='figure')
args = parser.parse_args()
out = (O / args.output).resolve()
assert out.is_relative_to(O.resolve()) and out != O.resolve()
out.mkdir(exist_ok=True)
I = s.eye(2)
L = s.Matrix([[0, 1], [1, 0]])
e = (I + L) / 2
p = s.diag(1, 0)
q = s.diag(0, 1)
D0, D1 = s.diag(1, s.I), s.diag(1, -s.I)
w0 = s.Matrix([[0, 1], [0, 0]])
w1 = s.I * w0
assert e * e == e and e.H == e and e.rank() == 1
assert e * s.Matrix([1, 1]) == s.Matrix([1, 1])
assert e * s.Matrix([1, -1]) == s.zeros(2, 1)
assert D0 * D1 == I
assert D0 * w1 * D0.H == w0 and D1 * w0 * D1.H == w1
for w in (w0, w1):
    assert w * w.H == p and w.H * w == q
coefficient_checks = 0
for j in range(2):
    for k in range(2):
        a = s.zeros(2); a[j, j] = 1
        b = s.zeros(2); b[k, k] = 1
        y = a * e * b
        Phi_y = 2 * s.diag(y[0, 0], y[1, 1])
        assert Phi_y == a * b
        coefficient_checks += 1
data = {
    'model': 'P=C^2, G=Z/2, alpha_s(a,b)=(b,a), Q=M_2(C)',
    'coefficient_embedding': 'diag(a,b)', 'lambda_s': [[0,1],[1,0]],
    'averaging_projection': [['1/2','1/2'],['1/2','1/2']],
    'fixed_algebra': 'B=C(1,1)', 'expectation_to_P': 'diagonal extraction',
    'eigenvectors': {'eigenvalue_1':[1,1], 'eigenvalue_0':[1,-1]},
    'cocycle_u_s': ['i','-i'], 'coboundary_v': ['1','i'],
    'gamma_s': '(X0,X1) -> (D0 X1 D0*, D1 X0 D1*)',
    'D0':'diag(1,i)', 'D1':'diag(1,-i)',
    'fixed_partial_isometry': ['E12','i E12'],
    'all_exact_model_checks_passed': True, 'coefficient_basis_checks': coefficient_checks,
    'cardinality_panel': 'Schematic of FP5 general proof; no finite simulation of infinite cardinalities',
    'proof_locators': ['FP0', 'FP5', 'FP6'],
}
(out / 'averaging-corner-data.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':13, 'svg.hashsalt':'L129-averaging-corner-20261006'})
fig = plt.figure(figsize=(15,11), dpi=200, facecolor='#f7f9fc')
ax = fig.add_axes([0,0,1,1]); ax.set(xlim=(0,15),ylim=(0,11)); ax.axis('off')
navy, blue, orange, grey = '#142b45', '#2165a8', '#b75f24', '#466078'
def text(x,y,value,size=14,color=navy,weight='normal',**kw):
    ax.text(x,y,value,fontsize=size,color=color,fontweight=weight,**kw)
def box(x,y,w,h):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.15',facecolor='white',edgecolor='#cfdae6',lw=1.3))
def arrow(x0,y0,x1,y1,color=blue):
    ax.add_patch(FancyArrowPatch((x0,y0),(x1,y1),arrowstyle='-|>',mutation_scale=16,lw=1.7,color=color))
text(.5,10.55,'Average first; compare fixed projections second',24,weight='bold')
text(.5,10.08,r'Exact model: $P=\mathbb{C}^2$, $\alpha_s(a,b)=(b,a)$, $G=\mathbb{Z}/2$.',16)
box(.55,5.55,6.7,3.95); box(7.75,5.55,6.7,3.95)
text(.78,9.12,'1  The regular averaging projection',18,weight='bold')
text(.8,8.60,r'$Q=M_2(\mathbb{C}),\quad \lambda_s=E_{12}+E_{21}$',17)
text(.8,8.10,r'$e=\frac{1}{2}(I+\lambda_s),\quad e_{ij}=\frac{1}{2}\ (i,j=1,2)$',18)
# Euclidean plane here is the real subspace of the two-dimensional model.
cx,cy,scale=2.30,6.74,.50
ax.plot([cx-.75,cx+.75],[cy,cy],color='#cad5e1',lw=1)
ax.plot([cx,cx],[cy-.75,cy+.75],color='#cad5e1',lw=1)
ax.plot([cx-.67,cx+.67],[cy-.67,cy+.67],color=blue,lw=2)
ax.plot([cx-.67,cx+.67],[cy+.67,cy-.67],color=orange,lw=2,ls='--')
arrow(cx,cy,cx+scale,cy+scale)
text(3.6,7.05,r'$e(1,1)=(1,1)$',17,color=blue)
text(3.6,6.53,r'$e(1,-1)=0$',17,color=orange)
text(.8,5.78,'FP0: range and kernel; the two vectors are orthogonal.',12,color=grey)
text(7.98,9.12,'2  The corner remembers the fixed algebra',18,weight='bold')
text(8.0,8.50,r'$B=P^\alpha=\mathbb{C}1$',19)
arrow(9.4,8.18,11.8,8.18)
text(9.80,8.39,r'$b\longmapsto be$',14,color=blue)
text(12.0,8.03,r'$eQe$',19)
text(8.0,7.48,r'$e\,\mathrm{diag}(a,b)\,e=\frac{a+b}{2}\,e$',18)
text(8.0,6.87,r'$E_P(be)=\frac{b}{2} I,\qquad \Phi=2E_P$',18)
text(8.0,6.28,r'$Z(B)=Z(P)^\alpha=\mathbb{C}1$',18)
text(8.0,5.78,'FP0: the general center proof also needs freeness and fullness.',12,color=grey)
box(.55,.85,6.7,4.10); box(7.75,.85,6.7,4.10)
text(.78,4.56,'3  An exact cocycle and its fixed bridge',18,weight='bold')
text(.8,3.99,r'$u_s=(i,-i),\quad v=(1,i),\quad u_s=v^*\alpha_s(v)$',17)
text(.8,3.43,r'$A=M_2(\mathbb{C})\oplus M_2(\mathbb{C})$',17)
text(.8,2.92,r'$w=(E_{12},iE_{12})\in A^\gamma$',18,color=blue)
text(.8,2.37,r'$ww^*=(E_{11},E_{11})=p$',18)
text(.8,1.87,r'$w^*w=(E_{22},E_{22})=q$',18)
text(.8,1.24,'FP6: gamma fixes w; the two fixed diagonal projections match.',12,color=grey)
text(7.98,4.56,'4  Why the infinite case needs sizes',18,weight='bold')
text(8.0,3.99,r'$rz=\sum_{i\in I}r_i\qquad tz=\sum_{j\in J}t_j$',18)
text(8.0,3.41,'Faithful expectation preserves sigma-finite corners.',14)
arrow(8.25,3.13,8.25,2.81)
text(8.65,2.80,r'$rz\sim_P tz\quad\Longrightarrow\quad |I|=|J|$',18,color=blue)
text(8.0,2.24,'Normal states detect each orthogonal filling family.',14)
arrow(8.25,1.97,8.25,1.65)
text(8.65,1.67,r'Match in $B$ and sum: $rz\sim_B tz$.',17,color=blue)
text(8.0,1.13,'FP5: schematic of the general proof, not a finite model.',12,color=grey)
text(.55,.36,'All finite entries are checked exactly. The general trace and arbitrary-cardinal proofs remain in the text.',12,color=grey)
fig.savefig(out/'averaging-corner.png', dpi=200)
fig.savefig(out/'averaging-corner.svg', metadata={'Date':None})
plt.close(fig)
font_license = O.parent / 'character-normalization-exact-cocycle-kernel/FONT-LICENSE.txt'
shutil.copyfile(font_license, out/'FONT-LICENSE.txt')
print(json.dumps({'pixels':[3000,2200],'exact_model_checks':True,'coefficient_basis_checks':coefficient_checks,'output':str(out)}))
