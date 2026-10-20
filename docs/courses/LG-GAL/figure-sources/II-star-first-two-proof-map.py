"""Reproduce the full II-star first-valuation-two calculation and both result rows."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(9,28),dpi=100)
fig.patch.set_facecolor('white');ax.set(xlim=(0,9),ylim=(0,28));ax.axis('off')
plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
ax.text(4.5,27.43,'II* with first valuation two',ha='center',fontsize=22,fontweight='bold')
ax.text(4.5,26.93,'One complete point shift; two discriminant and conductor rows',ha='center',fontsize=13)
def box(y,h,title,body,locator,color,size=12):
 ax.add_patch(FancyBboxPatch((.52,y),7.96,h,boxstyle='round,pad=.02,rounding_size=.17',facecolor=color,edgecolor='#365675',linewidth=1.5))
 ax.text(4.5,y+h-.4,title,ha='center',fontsize=16,fontweight='bold')
 ax.text(4.5,y+h/2-.06,body,ha='center',va='center',fontsize=size,linespacing=1.65)
 ax.text(4.5,y+.17,locator,ha='center',fontsize=10.2,color='#365675')
box(23.26,3.16,'The actual minimal II* preparation',
 'v(π) = 1; e = v(2) ≥ 2; v(a₁) = 2; v(a₂) ≥ 2\n'
 'z = v(a₃) ≥ 4; v(a₄) ≥ 5; v(a₆) = 5\n'
 'Infinite third/fourth valuations allowed; test the actual coefficients\n'
 'c = 1 + 2ζ; ζ³ = 1, ζ ≠ 1; c² = −3; v(c + 3) = e\n'
 'Lemma 6.0E gives the nine-component model: M = 9',
 '6.0W.1: FT1–FT2; finite unramified cube-root extension','#edf4ff')
box(19.46,3.24,'The entire quartic integer ring',
 'v(b₂) = 4; v(b₈) = 9; every quartic root has v(x) = 9/4\n'
 'τ = x/π²; full B₄ = R[τ] with basis 1, τ, τ², τ³\n'
 'Distinct upper valuation classes: 0, 1, 2, 3; i₄ = 2 + 4 + 6 = 12\n'
 'z = 4: v(b₆) = 8; d = 16; D₄ = 8\n'
 'z ≥ 5: v(b₄) ≥ 7, v(b₆) ≥ 9; d = 17; D₄ = 10',
 '6.0W.2: FT3–FT6; unique discriminant minima and full Eisenstein ring','#eaf7ef')
box(15.06,3.84,'The explicit integral point shift',
 'r = πλ; H₂ = r² − a₂; v(H₂) ≥ 3; λ is a residue lift\n'
 'w₀ = (cx² + a₄)/a₁; w = w₀ + r(x + a₃/a₁)\n'
 'The four shift terms have values 5/2, ≥ 3, ≥ 13/4, ≥ z − 1\n'
 'v(w) = 5/2; v(2w) ≥ e + 5/2 ≥ 9/2\n'
 'A = a₁x + a₃; G = x³ + a₂x² + a₄x + a₆; E = w² + Aw − G\n'
 'Trace value: 4 at z = 4; 17/4 at z ≥ 5',
 '6.0W.3: FT7–FT9; the scalar r a₃/a₁ cancels the even constant error','#fff5e6',11.8)
box(8.36,6.14,'The complete error identity and its bounds',
 'E = J₃x³ + J₂x² + J₁x + J₀\n'
 'J₃ = c + 4a₂/a₁² + 2cr/a₁\n'
 'J₂ = H₂ + (c + 3)a₃/a₁ + 2(c + 3)a₄/a₁²\n'
 '       + ra₁ + 2cra₃/a₁²\n'
 'J₁ = 3b₆/a₁² + 2ra₃ + 2ra₄/a₁ + 2r²a₃/a₁\n'
 'J₀ = (a₂ + r²)a₃²/a₁² + 4a₂a₆/a₁²\n'
 '       + ra₃²/a₁ + 2ra₄a₃/a₁²\n'
 'v(J₃) = 0; v(J₂) ≥ 3; v(J₀) ≥ 7\n'
 'The constant bound uses a₂ + r² = 2a₂ + H₂\n'
 'z = 4: v(J₁) = 4; unique leading term J₁x; v(E) = 25/4\n'
 'z ≥ 5: v(J₁) ≥ 5; unique leading term J₃x³; v(E) = 27/4',
 '6.0W.3–4: FT10–FT14; exact quartic expansion and every error bound','#eaf7ef',11.55)
box(4.91,2.89,'The entire point integer ring',
 'ℓ = 12 at z = 4; ℓ = 13 at z ≥ 5; η = (y − w)/τ^ℓ\n'
 'Both: v_F(E) − 2ℓ = 1; v_F(A + 2w) − ℓ = 4\n'
 'Full B₈ = B₄[η]; exact point index ℓ\n'
 'Upper relative different: min(8e + 1, 8) = 8\n'
 'D₈ = 2D₄ + 8; i₈ = (6d − D₈)/2 = 2i₄ + ℓ',
 '6.0W.5: FT15–FT18; full Eisenstein ring and tower/index calculation','#edf4ff',11.8)
cols=['z','d','M','i₄','ℓ','D₄','D₈','i₈','δ','f']
table=ax.table(cellText=[['4','16','9','12','12','8','24','36','6','8'],
                         ['≥ 5','17','9','12','13','10','28','37','7','9']],
 colLabels=cols,cellLoc='center',bbox=[.05,3.39/28,.9,1.08/28])
table.auto_set_font_size(False);table.set_fontsize(11.5)
for (row,col),cell in table.get_celld().items():
 cell.set_edgecolor('#9cb0c7');cell.set_linewidth(.8)
 cell.set_facecolor('#e8f0fa' if row==0 else '#f5f8fc')
 if row==0:cell.get_text().set_fontweight('bold')
ax.text(4.5,3.02,'Both: ε₄ = 3; ε₈ = 7; ν = 0; i₄ + ℓ = d + M − 1',ha='center',fontsize=12)
ax.text(4.5,2.64,'−Art(X/R) = 9 − 1 + f(E/K) = d',ha='center',fontsize=15,fontweight='bold')
ax.text(4.5,1.77,
 'Base valuations: v(π) = 1; quartic valuations: v_F(π) = 4.\n'
 'Normalized point constants/traces use v_F; relative differents use the upper valuation.\n'
 'Dⱼ are base discriminant exponents; iⱼ are R-lengths; ℓ is a B₄-length.',
 ha='center',va='center',fontsize=10.5,linespacing=1.65)
ax.text(4.5,.7,
 'Full proof: Lesson 8, Sections 6.0W.1–6, FT1–FT18; z = +∞ is in the second row.\nGeneral conductor–index identity: JM30–JM32, Section6.0BI.\nSource: Milne, Algebraic Number Theory, Prop. 7.55 / Rem. 7.56.',
 ha='center',va='center',fontsize=10.2,linespacing=1.65)
dest=Path(__file__).resolve().parents[1]/'assets/II-star-first-two-proof-map.png'
fig.savefig(dest,dpi=100,metadata={'Title':'Entire II-star first-valuation-two family and both conductor rows'})
plt.close(fig);print(dest.name)
