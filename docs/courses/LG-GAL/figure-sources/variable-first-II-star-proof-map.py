"""Reproduce the complete variable first-valuation II-star ring and conductor argument."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig,ax=plt.subplots(figsize=(9,29),dpi=100)
fig.patch.set_facecolor('white');ax.set(xlim=(0,9),ylim=(0,29));ax.axis('off')
plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
ax.text(4.5,28.45,'II* with variable first valuation',ha='center',fontsize=21,fontweight='bold')
ax.text(4.5,27.94,'All h ≥ 3 in the stated preparation; both parities; no upper cutoff',ha='center',fontsize=12.5)
def box(y,height,title,body,locator,color,size=12):
 ax.add_patch(FancyBboxPatch((.52,y),7.96,height,boxstyle='round,pad=.02,rounding_size=.17',facecolor=color,edgecolor='#365675',linewidth=1.5))
 ax.text(4.5,y+height-.4,title,ha='center',fontsize=16,fontweight='bold')
 ax.text(4.5,y+height/2-.08,body,ha='center',va='center',fontsize=size,linespacing=1.65)
 ax.text(4.5,y+.17,locator,ha='center',fontsize=10.2,color='#365675')
box(24.22,3.05,'The actual minimal II* preparation',
 'v(π) = 1; h = v(a₁) ≥ 3; e = v(2) ≥ h\n'
 'v(a₂) ≥ h + 1; v(a₃) = h + 2; v(a₄) ≥ h + 3; v(a₆) = 5\n'
 'Infinite second/fourth valuations allowed; actual coefficient tests\n'
 'c = 1 + 2ζ; ζ² + ζ + 1 = 0; c² = −3; v(c + 3) = e\n'
 'Lemma 6.0E gives M = 9; c₄ has value 4h; v(j) = 8h − 8 > 0',
 '6.0X.1: VI1–VI2; 6.0X.2: VI3; finite unramified cube-root extension','#edf4ff',11.65)
box(19.66,4.0,'The entire quartic integer ring, for both parities',
 'r = 2h + 5; every quartic root has v(x) = r/4\n'
 'v(b₂) = 2h; v(b₄) = 2h + 2; v(b₆) = 2h + 4; v(b₈) = r\n'
 'd = 4h + 8, uniquely led by −27b₆²\n'
 'mⱼ = floor(jr/4); full basis: 1, x/π^m₁, x²/π^m₂, x³/π^m₃\n'
 'i₄ = m₁ + m₂ + m₃ = 3h + 6; D₄ = 2h + 4\n'
 'h even: τ = x/π^m₁; h odd: τ = x³/π^m₃\n'
 'Both: v_F(τ) = 1; full B₄ = R[τ]',
 '6.0X.2–3: VI3–VI7; distinct valuation classes prove the full ring','#eaf7ef',11.6)
box(16.14,2.96,'One complete integral point shift',
 'w = (cx² + a₄)/a₁; v(w) = 5/2\n'
 'A = a₁x + a₃; G = x³ + a₂x² + a₄x + a₆\n'
 'v(a₁x) = 3h/2 + 5/4 > h + 2 = v(a₃)\n'
 'v(2w) = e + 5/2 > h + 2; v(A + 2w) = h + 2\n'
 'No scalar or residue shift is omitted',
 '6.0X.4: VI8–VI9; the displayed shift is the entire shift','#fff5e6',11.8)
box(9.93,5.65,'The complete error and its unique leading term',
 'E = w² + Aw − G = J₃x³ + J₂x² + J₁x + J₀\n'
 'J₃ = c + 4a₂/a₁²\n'
 'J₂ = (c + 3)a₃/a₁ − a₂ + 2(c + 3)a₄/a₁²\n'
 'J₁ = 3b₆/a₁²; J₀ = a₂b₆/a₁²\n'
 'a₁²(E − J₃x³ − J₂x² − J₁x − J₀) = (c² + 3)x⁴ − 3q(x)\n'
 'v(J₃) = 0; v(J₂) ≥ h + 1; v(J₁) = 4; v(J₀) ≥ h + 5\n'
 'Unique leading term: J₁x; v(E) = h/2 + 21/4\n'
 'Other-term margins: h − 3/2, 3h/2 − 7/4, h/2 − 1/4\n'
 'Every margin is strictly positive for every h ≥ 3',
 '6.0X.4–5: VI10–VI14; unrestricted expansion and every term bound','#eaf7ef',11.1)
box(5.9,3.47,'The entire point integer ring and different',
 'ℓ = h + 10; η = (y − w)/τ^ℓ; full B₈ = B₄[η]\n'
 'v_F(E) − 2ℓ = 1; v_F(A + 2w) − ℓ = 3h − 2\n'
 'The quadratic is Eisenstein; parity proves the full ring\n'
 'Derivative values upstairs: 8e + 1 and 6h − 4\n'
 'Their difference is 8e − 6h + 5 ≥ 2h + 5 > 0\n'
 'D₈/₄ = 6h − 4; D₈ = 2D₄ + D₈/₄ = 10h + 4',
 '6.0X.5: VI14–VI15; exact point index ℓ, full tower and different','#edf4ff',11.6)
table=ax.table(cellText=[['4h + 8','3h + 6','h + 10','2h + 4','10h + 4','7h + 22']],
 colLabels=['d','i₄','ℓ','D₄','D₈','i₈'],cellLoc='center',bbox=[.05,4.55/29,.9,.87/29])
table.auto_set_font_size(False);table.set_fontsize(11.5)
for (row,col),cell in table.get_celld().items():
 cell.set_edgecolor('#9cb0c7');cell.set_linewidth(.8);cell.set_facecolor('#e8f0fa' if row==0 else '#f5f8fc')
 if row==0:cell.get_text().set_fontweight('bold')
ax.text(4.5,4.17,'ε₄ = 3; ε₈ = 7; ν = 0; δ = 4h − 2; f(E/K) = 4h',ha='center',fontsize=12)
ax.text(4.5,3.73,'i₈ = 2i₄ + ℓ; i₄ + ℓ = 4h + 16 = d + M − 1',ha='center',fontsize=12)
ax.text(4.5,3.26,'−Art(X/R) = 9 − 1 + 4h = 4h + 8 = d',ha='center',fontsize=15,fontweight='bold')
ax.text(4.5,2.17,
 'Base valuations: v(π) = 1; quartic valuations: v_F(π) = 4.\n'
 'Point derivative/different exponents use the normalized point-field valuation.\n'
 'D₄ and D₈ are base discriminant exponents; i₄ and i₈ are R-lengths; ℓ is a B₄-length.',
 ha='center',va='center',fontsize=10.3,linespacing=1.65)
ax.text(4.5,.87,
 'Full proof: Lesson 8, Sections 6.0X.1–7, VI1–VI17. Exact preparation only.\nGeneral conductor–index identity: JM30–JM32, Section6.0BI.\nSource: Milne, Algebraic Number Theory, Prop. 7.55 / Rem. 7.56.',
 ha='center',va='center',fontsize=10.2,linespacing=1.65)
fig.canvas.draw()
renderer=fig.canvas.get_renderer()
for text in ax.texts:
 bounds=text.get_window_extent(renderer)
 assert bounds.x0>=0 and bounds.x1<=900 and bounds.y0>=0 and bounds.y1<=2900,text.get_text()
dest=Path(__file__).resolve().parents[1]/'assets/variable-first-II-star-proof-map.png'
fig.savefig(dest,dpi=100,metadata={'Title':'Variable first-valuation II-star family, full rings and conductor'})
plt.close(fig);print(dest.name)
