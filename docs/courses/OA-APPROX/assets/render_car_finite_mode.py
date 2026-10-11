"""Reproduce the CAR/expectation and dyadic perturbation diagrams (CC0)."""
from pathlib import Path
from math import cos, pi, sqrt
from cmath import exp
from html import escape

def add(a,b): return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def mul(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def adj(a): return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]
def tensor(a,b): return [[a[i][j]*b[k][l] for j in range(len(a[0])) for l in range(len(b[0]))] for i in range(len(a)) for k in range(len(b))]
def near(a,b): return all(abs(x-y)<1e-12 for ar,br in zip(a,b) for x,y in zip(ar,br))

b=[[0,1],[0,0]]; z=[[1,0],[0,-1]]; identity=[[1,0],[0,1]]
a1=tensor(b,identity); a2=tensor(z,b); i4=tensor(identity,identity)
zero=[[0]*4 for _ in range(4)]
assert add(mul(a1,a2),mul(a2,a1)) == zero
assert add(mul(a1,adj(a2)),mul(adj(a2),a1)) == zero
for a in (a1,a2):
    assert add(mul(a,adj(a)),mul(adj(a),a)) == i4
    assert mul(a,a) == zero
b2=mul(tensor(z,identity),a2)
assert b2 == tensor(identity,b)
assert mul(a1,b2) == mul(b2,a1)
for theta,overlap in ((pi/3,0.5),(pi/4,sqrt(2)/2)):
    u=[[exp(1j*theta),0],[0,exp(-1j*theta)]]
    assert abs((u[0][0]+u[1][1])/2-overlap)<1e-12
    assert near(mul(mul(u,b),adj(u)), [[0,exp(2j*theta)],[0,0]])
assert abs(cos(pi/3)*cos(pi/4)-sqrt(2)/4)<1e-12

parts=['<svg xmlns="http://www.w3.org/2000/svg" width="660" height="1060" viewBox="0 0 660 1060" role="img" aria-labelledby="title desc">',
 '<title id="title">Finite CAR modes and recovery by product-state expectations</title>',
 '<desc id="desc">Two occupation modes have parity-corrected commuting matrix legs. Their tracial GNS expectations retain one leg and average the other. In a general product state, the expectation tower of an inner implementer gives an exact overlap product tending to one.</desc>',
 '<rect width="660" height="1060" fill="#f8fafc"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#18293a;font-size:21px}.title{font-size:25px;font-weight:700}.label{font-size:22px;font-weight:700}.small{font-size:19px}.panel{fill:white;stroke:#91a6b7;stroke-width:1.5}.arrow{stroke:#246d94;stroke-width:3;fill:none}</style>',
 '<defs><marker id="head" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9Z" fill="#246d94"/></marker></defs>']
def line(x,y,text,kind=''):
    parts.append(f'<text x="{x}" y="{y}"'+(f' class="{kind}"' if kind else '')+'>'+escape(text)+'</text>')
def panel(y,h): parts.append(f'<rect x="22" y="{y}" width="616" height="{h}" rx="12" class="panel"/>')
line(28,37,'Parity, finite slices and the overlap tail','title')
panel(58,283)
line(42,93,'1. Two modes in the occupation basis','label')
line(42,129,'H_Fock = C² ⊗ C²;   b = |0⟩⟨1|;   Z = diag(1, −1)')
line(42,167,'a₁ = b ⊗ I;   a₂ = Z ⊗ b')
line(42,204,'{aᵢ, aⱼ*} = δᵢⱼ I;   {aᵢ, aⱼ} = 0')
line(42,241,'b₁ = a₁;   b₂ = (Z ⊗ I)a₂ = I ⊗ b')
line(42,278,'The b-legs commute; each leg generates M₂.')
line(42,316,'Together they generate M₂ ⊗ M₂ = M₄.','small')
panel(362,300)
line(42,397,'2. A finite tracial expectation','label')
line(42,434,'Ωⱼ = I₂ / √2 ∈ S₂(C²);   τⱼ(x) = Tr(x) / 2')
line(42,471,'Use left multiplication on Hτ = S₂(C²) ⊗ S₂(C²).','small')
line(42,508,'uⱼ = diag(eⁱᶿʲ, e⁻ⁱᶿʲ);   U = u₁ ⊗ u₂')
line(42,547,'U')
parts.append('<path d="M87 540H184" class="arrow" marker-end="url(#head)"/>')
line(111,533,'E₁','small')
line(203,547,'cos(θ₂) u₁ ⊗ I')
line(42,588,'θ₁ = π/3, θ₂ = π/4:   ‖E₁(U)Ω‖ = √2 / 2')
line(42,628,'E₀(U) = (√2 / 4) I;   Ω = Ω₁ ⊗ Ω₂')
panel(683,325)
line(42,718,'3. The full product-state innerness mechanism','label')
line(42,756,'α = Ad(u);   vₙ = u₁ ⋯ uₙ;   wₙ = vₙ* u ∈ M_tail')
line(42,794,'Eₙ(u) = aₙvₙ;   aₙ = ω(wₙ);   rⱼ = ωⱼ(uⱼ) ≥ 0')
line(42,832,'EₙEₘ = Eₙ   ⇒   aₙ = aₘ ∏ⱼ₌ₙ₊₁ᵐ rⱼ')
line(42,870,'Eₙ(u)Ω → uΩ   ⇒   |aₙ| → 1')
line(42,908,'For late n:   ∏ (j > n) rⱼ = |aₙ| > 0')
line(42,946,'Σ (j > n) (1 − rⱼ) ≤ −log|aₙ| → 0')
line(42,984,'Mⱼ factors; αⱼ preserve their normal states ωⱼ.','small')
line(28,1041,'CAR Theorem 2.1 · ITP Theorems 4.1 and 7.2 · CC0','small')
parts.append('</svg>')
svg='\n'.join(parts)
Path(__file__).with_name('car-finite-mode-reconstruction.svg').write_text(svg+'\n',encoding='utf-8')
print('Exact two-mode CAR identities and finite trace/phase values verified; SVG reproduced.')

# The displayed conditional-weight example is checked exactly in Q(sqrt(3)).
def qmul(x,y): return (x[0]*y[0]+3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qdot(x,y):
    terms=[qmul(a,b) for a,b in zip(x,y)]
    return tuple(sum(t[i] for t in terms) for i in (0,1))
p=((1,0),(0,1)); e=((0,1),(-1,0))  # both vectors are divided by 2
assert qdot(p,p)==(4,0) and qdot(e,e)==(4,0) and qdot(p,e)==(0,0)

parts=['<svg xmlns="http://www.w3.org/2000/svg" width="660" height="1090" viewBox="0 0 660 1090" role="img" aria-labelledby="title desc">',
 '<title id="title">The dyadic diagonal perturbation and its exact Hilbert–Schmidt budget</title>',
 '<desc id="desc">An increment vector belongs to its parent spectral interval. The starting vectors and all increments have a total squared error at most three M squared times two to the minus N. Choosing a starting level independently on each cyclic component yields an arbitrarily small Hilbert–Schmidt self-adjoint perturbation.</desc>',
 '<rect width="660" height="1090" fill="#f8fafc"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#18293a;font-size:21px}.title{font-size:25px;font-weight:700}.label{font-size:22px;font-weight:700}.small{font-size:19px}.panel{fill:white;stroke:#91a6b7;stroke-width:1.5}.band{stroke:#246d94;stroke-width:2}</style>']
line(28,37,'A diagonal basis with controlled square error','title')
line(28,72,'Bounded h = h*; separable K; M > ‖h‖','small')
panel(91,331)
line(42,126,'1. A new vector stays in the parent interval','label')
parts.append('<rect x="42" y="146" width="574" height="42" fill="#dbeafe" class="band"/>')
line(268,175,'parent')
parts.append('<rect x="42" y="205" width="287" height="42" fill="#dcfce7" class="band"/><rect x="329" y="205" width="287" height="42" fill="#fef3c7" class="band"/>')
line(145,234,'left child');line(426,234,'right child')
line(42,277,'l, r: normalized nonzero child projections of x','small')
line(42,312,'Conditional weights: μL = 1/4, μR = 3/4')
line(42,348,'p = (l + √3 r)/2;   e = (√3 l − r)/2')
line(42,383,'‖p‖ = ‖e‖ = 1;   ⟨p,e⟩ = 0')
line(42,409,'A zero child gives no new increment vector.','small')
panel(443,324)
line(42,478,'2. Count vectors and use the parent half-width','label')
line(42,519,'Start at level N: at most 2ᴺ vectors')
line(42,556,'Each error ≤ M 2⁻ᴺ; subtotal ≤ M² 2⁻ᴺ')
line(42,597,'Increment n > N: at most 2ⁿ⁻¹ vectors')
line(42,634,'Each error ≤ M 2⁻⁽ⁿ⁻¹⁾')
line(42,675,'All increments: subtotal ≤ 2 M² 2⁻ᴺ')
line(42,716,'Σₑ ‖(h − λₑ)e‖² ≤ 3 M² 2⁻ᴺ')
line(42,750,'λₑ is the midpoint of the supporting interval.','small')
panel(788,250)
line(42,823,'3. Assemble the reducing cyclic components','label')
line(42,864,'On component j, choose Nⱼ with')
line(42,903,'3 M² 2⁻ᴺʲ < ε² 2⁻ʲ⁻¹')
line(42,942,'d e = λₑ e;   k = d − h = k*')
line(42,981,'‖k‖²HS = Σₑ ‖(d − h)e‖² < ε²')
line(42,1018,'h + k = d has an orthonormal eigenbasis.','small')
line(28,1070,'Bogoliubov Sections 6.3–6.5 · original diagram, CC0','small')
parts.append('</svg>')
Path(__file__).with_name('bogoliubov-dyadic-perturbation.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
print('Exact conditional-weight orthogonality checked; dyadic3M²2^-N diagram reproduced.')
