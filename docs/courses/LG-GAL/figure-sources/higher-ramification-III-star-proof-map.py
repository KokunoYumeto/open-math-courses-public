"""Reproduce the two locally proved higher-ramification III-star families."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig,ax=plt.subplots(figsize=(9,27),dpi=100)
fig.patch.set_facecolor('white')
ax.set(xlim=(0,9),ylim=(0,27));ax.axis('off')
plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
ax.text(4.5,26.44,'III* at higher ramification',ha='center',fontsize=23,fontweight='bold')
ax.text(4.5,25.97,'Two complete families; full integer rings and conductors',ha='center',fontsize=13)

def box(y,h,title,body,locator,color,size=12.5):
    ax.add_patch(FancyBboxPatch((.52,y),7.96,h,boxstyle='round,pad=.02,rounding_size=.17',facecolor=color,edgecolor='#365675',linewidth=1.5))
    ax.text(4.5,y+h-.4,title,ha='center',fontsize=16,fontweight='bold')
    ax.text(4.5,y+h/2-.04,body,ha='center',va='center',fontsize=size,linespacing=1.65)
    ax.text(4.5,y+.17,locator,ha='center',fontsize=10.2,color='#365675')

box(23.32,2.12,'Actual translated preparation',
    'v(π) = 1; e = v(2); v(a₁), v(a₂) ≥ 2; v(a₃) ≥ 4; v(a₄) = 3\n'
    'Lemma 6.0D raises v(a₆) to ≥ 6; all symbols are then translated\n'
    'c² = −3; A₀ = a₄/c; t = x² + A₀; M = 8',
    '6.0T.1: HR1–HR3; finite unramified extensions preserve the quantities','#edf4ff')

box(19.2,3.62,'Family A: e ≥ 2 and v(a₁) = 2',
    'Every v(a₃) ≥ 4, including infinity: d = 14\n'
    'v(x) = 3/2; v(t) = 17/4; full B₄ basis: 1, x/π, t/π⁴, xt/π⁵\n'
    'τ = t/π⁴; i₄ = 10; D₄ = 8; w₁ = πλx uses a residue lift\n'
    'Point error v_F = 23; shifted trace v_F = 14\n'
    'η = (y − w₁)/τ¹¹; constant 1, trace 3; upper different 6\n'
    'Full B₈ = B₄[η]; point index ℓ = 11; D₈ = 22; i₈ = 31',
    '6.0T.2: HR4–HR8; four quartic valuation classes prove the entire ring','#eaf7ef',12.2)

box(15.28,3.42,'Family B: z = v(a₃) ≥ 4 finite',
    'e ≥ z − 2 and v(a₁) ≥ z − 1; infinite first valuation allowed\n'
    'd = 4z; v(x) = 3/2; v(t) = z + 3/4\n'
    'Full B₄ basis: 1, x/π, t/πᶻ, xt/πᶻ⁺²\n'
    'τ = xt/πᶻ⁺²; quartic valuation classes 0, 2, 3, 1\n'
    'i₄ = 2z + 3; D₄ = 4z − 6',
    '6.0T.3: HR9–HR12; all finite z are covered','#fff5e6',12.7)

box(10.42,4.37,'Family B: approximate τ⁴ by a base scalar',
    'N = π²ᶻ⁺⁴; Q = (b₆A₀ − b₂A₀²/3)/N; v(Q) = −1\n'
    'β = (−C₂A₀² + C₀A₀/3)/N; v(β) ≥ 1\n'
    'τ² = Qx + β + R₀; v(R₀) ≥ z − 7/4\n'
    'σ = −Q²A₀ + β² ∈ R; v(σ) = 1\n'
    'τ⁴ − σ = Q²t + 2Qxβ + 2(Qx + β)R₀ + R₀²\n'
    'v(τ⁴ − σ) ≥ z − 5/4\n'
    'For every n ≥ 1: v(τ⁴ⁿ − σⁿ) ≥ z + n − 9/4',
    '6.0T.4: HR13–HR19; exact six-term remainder and telescoping proof','#fff5e6',12.5)

box(5.69,4.24,'Family B: finite cancellation and the full point ring',
    'First error E₁ = −xt + K + R₁′; K ∈ R, v(K) ≥ 6\n'
    'R₁′ has value ≥ z + 5/2; first shifted trace has exact value z\n'
    'For n = 6,…,z + 2, lift √(−Kₙ/σⁿ) in the residue field\n'
    'Kₙ₊₁ = Kₙ + κₙ²σⁿ; v(Kₙ₊₁) ≥ n + 1; exactly z − 3 steps\n'
    'S = Σ κₙτ²ⁿ; v(S) ≥ 3; final error v(E) = z + 9/4\n'
    'η = (y − w₁ − S)/τ²ᶻ⁺⁴; constant 1, trace 2z − 4\n'
    'Full B₈ = B₄[η]; ℓ = 2z + 4; upper different 4z − 8',
    '6.0T.5–6: HR20–HR27; the error and trace retain their unique leading terms','#fff5e6',12.2)

cols=['family','d','i₄','i₈','D₄','D₈','ℓ','δ','f']
rows=[['A','14','10','31','8','22','11','5','7'],
      ['B','4z','2z+3','6z+10','4z−6','12z−20','2z+4','4z−9','4z−7']]
table=ax.table(cellText=rows,colLabels=cols,colWidths=[.1,.08,.12,.12,.12,.13,.12,.11,.1],cellLoc='center',bbox=[.035,3.9/27,.93,1.24/27])
table.auto_set_font_size(False);table.set_fontsize(11.3)
for (row,col),cell in table.get_celld().items():
    cell.set_edgecolor('#9cb0c7');cell.set_linewidth(.8)
    cell.set_facecolor('#e8f0fa' if row==0 else '#f5f8fc')
    if row==0:cell.get_text().set_fontweight('bold')
ax.text(4.5,3.55,'Both: ε₄ = 3; ε₈ = 7; ν = 0; i₄ + ℓ = d + M − 1',ha='center',fontsize=12.6)
ax.text(4.5,3.12,'−Art(X/R) = 8 + 1 + δ = d',ha='center',fontsize=16,fontweight='bold')
ax.text(4.5,2.23,
    'Base valuations v(π) = 1; quartic valuations v_F(π) = 4.\n'
    'Normalized point constants and traces use the quartic valuation.\n'
    'Relative different exponents use the upper point-field valuation.\n'
    'Dⱼ are base discriminant exponents; iⱼ are R-lengths; ℓ is a B₄-length.',
    ha='center',va='center',fontsize=10.7,linespacing=1.65)
ax.text(4.5,1.07,
    'These two families are the scopes of HR4 and HR9.\n'
    'Every other residual family, universal NF24 and distinct reviews remain required.\n'
    'Proof locators: Lesson 8, Sections 6.0T.1–7.\n'
    'Free human writing material: Milne, Algebraic Number Theory, Prop. 7.55 / Rem. 7.56.',
    ha='center',va='center',fontsize=10.7,linespacing=1.65)
dest=Path(__file__).resolve().parents[1]/'assets/higher-ramification-III-star-proof-map.png'
fig.savefig(dest,dpi=100,metadata={'Title':'Two proved higher-ramification III-star families'})
plt.close(fig)
print(dest.name)
