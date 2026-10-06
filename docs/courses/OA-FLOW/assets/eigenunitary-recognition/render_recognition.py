"""Original OA-FLOW finite eigenunitary model. CC0-1.0 to the extent of rights held.

Reproduce with Python, Matplotlib 3.10.9 and NumPy 2.4.4:
    python render_recognition.py --output OUTPUT_DIRECTORY

No TeX, external images or network access. SVG glyph notices are in ASSET_TERMS.md.
Output includes the figure, mathematical diagnostic data and private build reports.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, required=True)
out = parser.parse_args().output.resolve()
out.mkdir(parents=True, exist_ok=True)
os.environ['MPLCONFIGDIR'] = str(out/'runtime-cache')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.text import Text

plt.rcParams.update({'font.family':'DejaVu Sans', 'mathtext.fontset':'dejavusans',
    'text.usetex':False, 'svg.fonttype':'path', 'svg.hashsalt':'OA-FLOW-L29-original-20261006'})
ink, blue, green, purple = '#193342', '#185f8f', '#16705b', '#714d9a'
muted, border = '#4b626d', '#c8d4dc'
colors = [blue, green, purple]

def save_json(name, obj):
    (out/name).write_bytes((json.dumps(obj,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))

# Exact third-root calculations in the rational basis (1, omega), omega^2=-1-omega.
root_coefficients = [(1,0),(0,1),(-1,-1)]
projection_values = []
for j in range(3):
    values = []
    for ell in range(3):
        terms = [root_coefficients[((ell-j)*k)%3] for k in range(3)]
        totals = [sum(x[i] for x in terms) for i in range(2)]
        assert totals == ([3,0] if ell==j else [0,0])
        values.append(totals[0]//3)
    projection_values.append(values)
assert all(((j-k)*s-j*s+k*s)%3==0 for j in range(3) for k in range(3) for s in range(3))

omega = np.exp(2j*np.pi/3)
D = np.diag([1,omega])
I2, I6, I18 = np.eye(2), np.eye(6), np.eye(18)

def blockdiag(blocks):
    size = sum(b.shape[0] for b in blocks)
    result = np.zeros((size,size),complex)
    offset = 0
    for b in blocks:
        n = b.shape[0]
        result[offset:offset+n,offset:offset+n] = b
        offset += n
    return result

def constant(a):
    return blockdiag([a]*3)

u = [blockdiag([omega**(j*s)*np.linalg.matrix_power(D,s) for j in range(3)]) for s in range(3)]
z = u[1]@constant(D.conj().T)
projectors = [sum((omega**(-j*k)*np.linalg.matrix_power(z,k) for k in range(3)),start=np.zeros((6,6),complex))/3 for j in range(3)]
F = np.array([[omega**(k*t)/np.sqrt(3) for t in range(3)] for k in range(3)])
W = np.kron(F,I6)@blockdiag(u)
errors = {}

def error(name, matrix):
    value = float(np.max(np.abs(matrix)))
    assert value < 1e-12, (name,value)
    errors[name] = value

error('W_star_W_minus_identity',W.conj().T@W-I18)
error('W_W_star_minus_identity',W@W.conj().T-I18)
error('sum_central_projections_minus_identity',sum(projectors)-I6)
for s in range(3):
    for t in range(3):
        error(f'unitary_representation_s{s}_t{t}',u[s]@u[t]-u[(s+t)%3])
    for k in range(3):
        shifted=blockdiag([u[s][2*((j-k)%3):2*((j-k)%3)+2,2*((j-k)%3):2*((j-k)%3)+2] for j in range(3)])
        error(f'eigencharacter_k{k}_s{s}',shifted-omega**(-k*s)*u[s])
    shift=np.zeros((3,3))
    for t in range(3):
        shift[t,(t-s)%3]=1
    lam=np.kron(shift,I6)
    target=blockdiag([omega**(k*s)*u[s] for k in range(3)])
    error(f'group_intertwiner_s{s}',W@lam@W.conj().T-target)
for j,p in enumerate(projectors):
    target=blockdiag([I2 if ell==j else np.zeros((2,2)) for ell in range(3)])
    error(f'projection_block_j{j}',p-target)
    error(f'projection_idempotence_j{j}',p@p-p)
matrix_units=[]
for a in range(2):
    for b in range(2):
        e=np.zeros((2,2));e[a,b]=1
        matrix_units.append(e)
        pi=blockdiag([u[t].conj().T@constant(e)@u[t] for t in range(3)])
        error(f'coefficient_intertwiner_e{a+1}{b+1}',W@pi@W.conj().T-np.kron(np.eye(3),constant(e)))
        error(f'coefficient_action_e{a+1}{b+1}',D@e@D.conj().T-omega**(a-b)*e)
span=np.column_stack([(p@constant(e)).reshape(-1) for p in projectors for e in matrix_units])
assert np.linalg.matrix_rank(span,tol=1e-10)==12

save_json('recognition-data.json',{
    'license':'CC0-1.0 to the extent of rights held; numerical facts are not claimed as exclusive property.',
    'model':{'G':'Z/3Z','H':'Z/3Z','pairing':'chi_k(s)=omega^(ks)',
        'omega':'exp(2*pi*i/3)','D_diagonal_exponents':[0,1],
        'u1_diagonal_exponents_by_block':[[0,1],[1,2],[2,0]],
        'z_scalar_exponents_by_block':[0,1,2],
        'alpha1_matrix_unit_exponents':[[0,2],[1,0]],
        'beta1_projection_destination':[1,2,0],
        'original_group_singleton_mass':1,'dual_group_singleton_mass':'1/3',
        'Euclidean_target_coordinate':'eta_hat_k=eta(k)/sqrt(3)',
        'W_block_k_t':'omega^(k*t)*u_t/sqrt(3)',
        'Hilbert_dimension':18,'algebra_dimension':12},
    'exact_projection_values':projection_values,
    'exact_phase_covariance_checked_for_all_27_triples':True,
    'exact_root_basis':'(1,omega) with omega^2=-1-omega',
    'numerical_checks':errors,
    'numeric_tolerance':1e-12,
    'generated_matrix_space_rank':12,
    'interpretation':'Exact finite model plus floating-point residual diagnostics. The arbitrary-group proof is OA-FLOW-L29, Section 5.'})

fig=plt.figure(figsize=(14,16),dpi=160,facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')

def text(x,y,s,size=18,color=ink,weight='normal',ha='left'):
    return ax.text(x,y,s,fontsize=size,color=color,fontweight=weight,ha=ha,va='center',transform=ax.transAxes)

def box(x,y,w,h,color=border,face='#f6f9fb'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.009,rounding_size=0.008',
        linewidth=1.5,edgecolor=color,facecolor=face,transform=ax.transAxes))

def arrow(x1,y1,x2,y2,color=blue,arc=0):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=21,
        linewidth=2,color=color,connectionstyle=f'arc3,rad={arc}',transform=ax.transAxes))

def rule(y):
    ax.plot([.05,.95],[y,y],lw=1.2,color=border,transform=ax.transAxes)

text(.05,.971,'Recover the matrix algebra, then identify its crossed product',24,weight='bold')
text(.05,.941,r'$G=\mathbb{Z}/3,\quad \omega=e^{2\pi i/3},\quad D=\mathrm{diag}(1,\omega),\quad N=M_2\oplus M_2\oplus M_2$',19,color=muted)

text(.05,.900,'1   One matrix algebra sits in all three blocks',19,color=blue,weight='bold')
text(.05,.867,r'$M=N^\beta=\{(a,a,a):a\in M_2\},\qquad [\beta_k(X)]_j=X_{j-k}$',21)
centers=[.205,.5,.795]
entries=[r'$u_1=\mathrm{diag}(1,\omega)$',r'$u_1=\mathrm{diag}(\omega,\omega^2)$',r'$u_1=\mathrm{diag}(\omega^2,1)$']
zentries=[r'$z=I$',r'$z=\omega I$',r'$z=\omega^2 I$']
for j,c in enumerate(centers):
    box(c-.127,.672,.254,.151,color=colors[j])
    text(c,.799,rf'Block $j={j}$',17,color=colors[j],weight='bold',ha='center')
    text(c,.763,r'$a\in M_2$',22,ha='center')
    text(c,.724,entries[j],17,ha='center')
    text(c,.688,zentries[j],19,color=colors[j],ha='center')
arrow(.335,.751,.369,.751,color=muted)
arrow(.630,.751,.664,.751,color=muted)
arrow(.795,.659,.205,.659,color=muted,arc=-.020)
text(.5,.635,r'$\beta_1:p_0\mapsto p_1\mapsto p_2\mapsto p_0$',16,color=muted,ha='center')
text(.05,.607,r'$\alpha_1(a)=DaD^*:\qquad e_{12}\mapsto\omega^2 e_{12},\quad e_{21}\mapsto\omega e_{21}$',21,color=green)
text(.05,.579,'The dual action cycles blocks; the coefficient action changes entries inside each matrix.',14,color=muted)
rule(.556)

text(.05,.529,'2   The central roots reveal each whole matrix block',19,color=blue,weight='bold')
text(.05,.493,r'$z=u_1(D^*,D^*,D^*),\qquad p_j=\frac{1}{3}\sum_{k=0}^2\omega^{-jk}z^k$',22)
for j,c in enumerate(centers):
    box(c-.127,.407,.254,.048,color=colors[j],face='white')
    labels=[r'$p_0=(I,0,0)$',r'$p_1=(0,I,0)$',r'$p_2=(0,0,I)$']
    text(c,.431,labels[j],21,color=colors[j],ha='center')
text(.05,.361,r'$X=\sum_{j=0}^2p_j(X_j,X_j,X_j)\quad\Longrightarrow\quad N=(M\cup u(G))^{\prime\prime}$',21)
rule(.326)

text(.05,.307,'3   A concrete unitary compares the regular generators',19,color=blue,weight='bold')
text(.05,.277,r'$K=\mathbb{C}^2\oplus\mathbb{C}^2\oplus\mathbb{C}^2;\qquad \mathbb{C}^3\otimes K\ \longrightarrow\ \mathbb{C}^3\otimes K$',19,color=muted)
box(.065,.190,.23,.061,color=blue,face='white')
box(.385,.190,.23,.061,color=green,face='white')
box(.705,.190,.23,.061,color=purple,face='white')
text(.180,.221,r'$\xi_t$',23,ha='center')
text(.500,.221,r'$u_t\xi_t$',23,ha='center')
text(.820,.221,r'$\widehat\eta_k$',23,ha='center')
arrow(.302,.221,.377,.221,color=blue)
arrow(.622,.221,.697,.221,color=green)
text(.34,.257,r'$D_u$',15,color=blue,ha='center')
text(.66,.257,r'$\widetilde{\mathcal{F}}_+$',15,color=green,ha='center')
text(.05,.153,r'$\widehat\eta_k=(\widetilde{W}\xi)_k=\frac{1}{\sqrt{3}}\sum_{t=0}^2\omega^{kt}u_t\xi_t$',21)
text(.05,.114,r'$\pi_\alpha(a)\ \longmapsto\ (\widehat\eta_k\mapsto(a,a,a)\widehat\eta_k),\qquad \lambda(s)\ \longmapsto\ (\widehat\eta_k\mapsto\omega^{ks}u_s\widehat\eta_k)$',17)
text(.05,.091,r'Both spaces have dimension 18. Haar masses: $1$ on $G$, $1/3$ on $H$; $\widehat\eta_k=\eta(k)/\sqrt{3}$.',13,color=muted)
rule(.076)
text(.05,.056,'Proof: OA-FLOW-L29, l29-7-finite, equations (L29.7.a)–(L29.7.e); general recognition: l29-5.',11.7,color=muted)
text(.05,.034,'Antecedent: M. Takesaki, Theory of Operator Algebras II, Proposition X.2.6, pp.263–265.',11.7,color=muted)
text(.05,.014,'Original course illustration. This finite model illustrates the proof; it does not restrict the theorem to finite spaces.',11.7,color=muted)

fig.canvas.draw()
renderer=fig.canvas.get_renderer()
layout=[]
for t in fig.findobj(Text):
    if not t.get_text() or not t.get_visible():
        continue
    x,y,w,h=t.get_window_extent(renderer).bounds
    inside=bool(x>=0 and y>=0 and x+w<=fig.bbox.width and y+h<=fig.bbox.height)
    layout.append({'text':t.get_text(),'bbox_px':[round(v,3) for v in (x,y,w,h)],'inside_canvas':inside})
assert all(item['inside_canvas'] for item in layout),[item for item in layout if not item['inside_canvas']]
manifest=[]
for ext in ['png','svg']:
    p=out/f'recognition.{ext}'
    metadata={'Software':'OA-FLOW original mathematical illustration'} if ext=='png' else {'Date':None,'Creator':'OA-FLOW original mathematical illustration'}
    fig.savefig(p,dpi=160,format=ext,metadata=metadata,facecolor='white')
    if ext=='svg':
        p.write_bytes(re.sub(br'<!DOCTYPE svg PUBLIC[^>]*>\r?\n',b'',p.read_bytes(),count=1))
    manifest.append({'path':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
save_json('LAYOUT_CHECKS.json',{'canvas_px':list(fig.canvas.get_width_height()),'text_checks':layout})
save_json('BUILD_RECEIPT.json',{'runtime':{'matplotlib':matplotlib.__version__,'numpy':np.__version__,'tex_used':False},
    'outputs':manifest,'numerical_check_count':len(errors),'maximum_numeric_residual':max(errors.values()),
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
print(json.dumps({'artifacts':len(manifest),'exact_projection_values':projection_values,
    'numerical_checks':len(errors),'maximum_residual':max(errors.values()),'all_text_inside_canvas':True}))
