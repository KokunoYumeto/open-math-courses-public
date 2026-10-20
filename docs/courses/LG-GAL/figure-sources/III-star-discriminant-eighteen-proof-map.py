"""Reproduce both locally proved full-ring alternatives in the d18 family."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig,ax=plt.subplots(figsize=(9,28),dpi=100)
fig.patch.set_facecolor('white');ax.set(xlim=(0,9),ylim=(0,28));ax.axis('off')
plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
ax.text(4.5,27.45,'III* at discriminant valuation eighteen',ha='center',fontsize=21,fontweight='bold')
ax.text(4.5,26.95,'Two ramification alternatives; the same full-ring invariants',ha='center',fontsize=13)
def box(y,h,title,body,locator,color,size=12.5):
    ax.add_patch(FancyBboxPatch((.52,y),7.96,h,boxstyle='round,pad=.02,rounding_size=.17',facecolor=color,edgecolor='#365675',linewidth=1.5))
    ax.text(4.5,y+h-.4,title,ha='center',fontsize=16,fontweight='bold')
    ax.text(4.5,y+h/2-.05,body,ha='center',va='center',fontsize=size,linespacing=1.65)
    ax.text(4.5,y+.17,locator,ha='center',fontsize=10.2,color='#365675')
box(23.45,2.95,'Actual translated III* preparation',
    'v(π) = 1; e = v(2) ≥ 2; v(a₁) ≥ 3; v(a₂) ≥ 2\n'
    'v(a₃) ≥ 5; v(a₄) = 3; Lemma 6.0D raises v(a₆) to ≥ 6\n'
    'On these translated coefficients: v(b₂) = 6\n'
    'c² = −3; A₀ = a₄/c; t = x² + A₀; d = 18; M = 8',
    '6.0U.1–2: DE1–DE4; higher or infinite allowed coefficients retained','#edf4ff')
box(19.99,2.95,'A trace congruence prevents cancellation',
    'H₂ = π²λ² − a₂; v(H₂) ≥ 3; w₁ = πλx\n'
    '(a₁ + 2πλ)² − b₂ = 4a₁πλ + 4H₂ has value ≥ 7\n'
    'Since v(b₂) = 6, the trace coefficient has exact value 3\n'
    'α₁ = (a₁ + 2πλ)x + a₃ has exact base value 9/2',
    '6.0U.2: DE5–DE7; λ is a residue square-root lift','#edf4ff')
box(15.57,3.91,'Alternative A: e ≥ 3',
    'The invariant condition forces v(a₁) = 3\n'
    'v(x) = 3/2; v(t) = 21/4; τ = t/π⁵\n'
    'Full B₄ basis: 1, x/π, t/π⁵, xt/π⁶; i₄ = 12; D₄ = 12\n'
    'K = −H₂A₀ − a₆; v(K) ≥ 6\n'
    'Choose μ by v(K + μ²A₀²) ≥ 7; w₂ = μx²\n'
    'Final leading error −xt: base value 27/4; trace value 9/2',
    '6.0U.3: DE8–DE11; all seven error bounds are strictly higher','#eaf7ef',12.4)
box(8.57,6.49,'Alternative B: e = 2',
    'v(C₂) = 7; v(t) = 5; choose v(C₂A₀ − u²π¹⁰) ≥ 11\n'
    'm = uπ⁵; s = t − m; P = A₀ − m; x² = s − P\n'
    'D = C₂ + 2m; H₀ = C₂A₀ − m² − C₂m − C₀/3\n'
    's² = (b₂P/3 − b₆)x − (b₂/3)xs − Ds + H₀\n'
    'v(s) = 21/4; τ = s/π⁵; full basis uses s in place of t\n'
    'U = m + a₄(1 − 1/c); v(U) = 5, proved by its square\n'
    'U² = (m² − C₂A₀) + a₁a₃A₀ − 4a₄²/c² + 2ma₄(1 − 1/c)\n'
    'Choose μ by v(K + μ²P²) ≥ 7; w₂ = μx²; K = −H₂P − a₆\n'
    'V = (b₂P/3 − b₆)/π⁴; v(V) = 5; choose v(ξ²V − U) ≥ 6\n'
    'w₃ = ξs/π² cancels the −Ux term\n'
    'Final leading error −xs: base value 27/4; trace value 9/2',
    '6.0U.4–5: DE12–DE17; μ and ξ are residue lifts only','#fff5e6',12.15)
box(5.55,2.51,'Common full point ring',
    'w is the sum of the shifts used; η = (y − w)/τ¹³\n'
    'Normalized constant 1, trace 5; full B₈ = B₄[η]\n'
    'Upper different min(8e + 1, 10) = 10; point index ℓ = 13',
    '6.0U.6: DE18–DE20; Eisenstein polynomial gives the entire ring','#edf4ff')
cols=['d','M','i₄','i₈','D₄','D₈','ℓ','δ','f']
table=ax.table(cellText=[['18','8','12','37','12','34','13','9','11']],colLabels=cols,cellLoc='center',bbox=[.05,4.1/28,.9,1.03/28])
table.auto_set_font_size(False);table.set_fontsize(12)
for (row,col),cell in table.get_celld().items():
    cell.set_edgecolor('#9cb0c7');cell.set_linewidth(.8);cell.set_facecolor('#e8f0fa' if row==0 else '#f5f8fc')
    if row==0:cell.get_text().set_fontweight('bold')
ax.text(4.5,3.73,'Both: ε₄ = 3; ε₈ = 7; ν = 0; i₄ + ℓ = 25 = d + M − 1',ha='center',fontsize=12.5)
ax.text(4.5,3.3,'−Art(X/R) = 8 + 1 + 9 = 18 = d',ha='center',fontsize=16,fontweight='bold')
ax.text(4.5,2.43,'Base valuations v(π) = 1; quartic valuations v_F(π) = 4.\n'
    'Normalized point constants and traces use the quartic valuation.\n'
    'Relative different exponents use the upper point-field valuation.\n'
    'Dⱼ are base discriminant exponents; iⱼ are R-lengths; ℓ is a B₄-length.',
    ha='center',va='center',fontsize=10.7,linespacing=1.65)
ax.text(4.5,1.07,'Exact hypotheses and proofs: Lesson 8, Sections 6.0U.1–7, DE1–DE20.\nThe boxes are alternatives; complementary values lie outside their hypotheses.\nGeneral conductor–index identity: JM30–JM32, Section6.0BI.\nSource: Milne, Algebraic Number Theory, Prop. 7.55 / Rem. 7.56.',
    ha='center',va='center',fontsize=10.5,linespacing=1.65)
dest=Path(__file__).resolve().parents[1]/'assets/III-star-discriminant-eighteen-proof-map.png'
fig.savefig(dest,dpi=100,metadata={'Title':'Both full-ring alternatives for the discriminant-eighteen III-star family'})
plt.close(fig);print(dest.name)
