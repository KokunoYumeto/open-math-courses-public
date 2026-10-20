"""Reproduce both full II-star regimes with unbounded third valuation."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

fig,ax=plt.subplots(figsize=(9,31),dpi=100)
fig.patch.set_facecolor('white');ax.set(xlim=(0,9),ylim=(0,31));ax.axis('off')
plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
ax.text(4.5,30.46,'II* with unbounded third valuation',ha='center',fontsize=21,fontweight='bold')
ax.text(4.5,29.97,'Two complete regimes; one shift and one normalized trace',ha='center',fontsize=13)
def box(y,height,title,body,locator,color,size=12,x=.52,width=7.96):
 ax.add_patch(FancyBboxPatch((x,y),width,height,boxstyle='round,pad=.02,rounding_size=.17',facecolor=color,edgecolor='#365675',linewidth=1.5))
 center=x+width/2
 ax.text(center,y+height-.4,title,ha='center',fontsize=16 if width>5 else 14,fontweight='bold')
 ax.text(center,y+height/2-.05,body,ha='center',va='center',fontsize=size,linespacing=1.6)
 ax.text(center,y+.17,locator,ha='center',fontsize=10.2 if width>5 else 9.7,color='#365675')
box(26.12,3.14,'The actual minimal II* preparation',
 'v(π) = 1; finite h = v(a₁) ≥ 2; e = v(2) ≥ h\n'
 'v(a₂) ≥ h + 1; z = v(a₃) ≥ h + 2; v(a₄) ≥ h + 3; v(a₆) = 5\n'
 'Infinite second/third/fourth valuations allowed\n'
 't = min(2(z − h), 2(e − h) + 5) is finite and at least four\n'
 'c = 1 + 2ζ; c² = −3; v(c + 3) = e; M = 9',
 '6.0Y.1: UT1–UT2; finite unramified cube-root extension','#edf4ff',11.65)
box(21.79,3.77,'The entire quartic integer ring, both parities',
 'v(b₂) = 2h; v(b₄) ≥ 2h + 2; v(b₆) = 2h + t; v(b₈) = 2h + 5\n'
 'r = 2h + 5; every quartic root has v(x) = r/4\n'
 'mⱼ = floor(jr/4); full basis: 1, x/π^m₁, x²/π^m₂, x³/π^m₃\n'
 'i₄ = 3h + 6; h even: τ = x/π^m₁; h odd: τ = x³/π^m₃\n'
 'v_F(τ) = 1; full B₄ = R[τ]; residue degree one\n'
 'v(c₄) = 4h; v(j) ≥ 6h − 5 > 0',
 '6.0Y.2–3: UT3–UT6; unique minima and coefficientwise integrality','#eaf7ef',11.4)
box(16.36,4.87,'One complete point shift and every error coefficient',
 'A = a₁x + a₃; G = x³ + a₂x² + a₄x + a₆\n'
 'w = (cx² + a₄)/a₁; v(w) = 5/2\n'
 'E = w² + Aw − G = J₃x³ + J₂x² + J₁x + J₀\n'
 'J₃ = c + 4a₂/a₁²\n'
 'J₂ = (c + 3)a₃/a₁ − a₂ + 2(c + 3)a₄/a₁²\n'
 'J₁ = 3b₆/a₁²; J₀ = a₂b₆/a₁²\n'
 'a₁²(E − J₃x³ − J₂x² − J₁x − J₀) = (c² + 3)x⁴ − 3q(x)\n'
 'v(J₃) = 0; v(J₂) ≥ h + 1; v(J₁) = t; v(J₀) ≥ h + 1 + t',
 '6.0Y.4: UT7–UT11; unrestricted global expansion, including the constant','#fff5e6',11.0)
box(12.57,3.22,'Low regime: 4 ≤ t ≤ h + 2',
 'Unique Δ leader: −27b₆²\n'
 'd = 4h + 2t\n'
 'Unique error leader: J₁x\n'
 'v_F(E) = 4t + 2h + 5\n'
 'ℓ = 2t + h + 2\n'
 'v_F(A + 2w) = 4h + 2t',
 '6.0Y.2, 4–5: UT4, UT11–UT12','#edf4ff',10.9,x=.52,width=3.79)
box(12.57,3.22,'High regime: t ≥ h + 3',
 'Unique Δ leader: −b₂²b₈\n'
 'd = 6h + 5\n'
 'Unique error leader: J₃x³\n'
 'v_F(E) = 6h + 15\n'
 'ℓ = 3h + 7\n'
 'v_F(A + 2w) = 6h + 5',
 '6.0Y.2, 4–5: UT4, UT11–UT12','#eaf7ef',10.9,x=4.69,width=3.79)
for start in (2.42,6.58):
 ax.add_patch(FancyArrowPatch((start,12.48),(4.5,12.06),arrowstyle='-|>',mutation_scale=14,color='#365675',linewidth=1.4))
box(8.33,3.52,'Both regimes give the entire point integer ring',
 'η = (y − w)/τ^ℓ; full B₈ = B₄[η]; exact point index ℓ\n'
 'v_F(E) − 2ℓ = 1; v_F(A + 2w) − ℓ = 3h − 2\n'
 'Eisenstein quadratic; coefficientwise parity proves the full ring\n'
 'Point derivative values: 8e + 1 and 6h − 4\n'
 '8e − 6h + 5 ≥ 2h + 5 > 0; relative different = 6h − 4\n'
 'D₈ = 2D₄ + 6h − 4; i₈ = 2i₄ + ℓ',
 '6.0Y.5: UT12–UT13; residue degree one, full different and index tower','#edf4ff',11.5)
def table(bottom,height,headers,rows):
 tb=ax.table(cellText=rows,colLabels=headers,cellLoc='center',bbox=[.05,bottom/31,.9,height/31])
 tb.auto_set_font_size(False);tb.set_fontsize(11.4)
 for (row,col),cell in tb.get_celld().items():
  cell.set_edgecolor('#9cb0c7');cell.set_linewidth(.8);cell.set_facecolor('#e8f0fa' if row==0 else '#f5f8fc')
  if row==0:cell.get_text().set_fontweight('bold')
table(6.49,1.28,['Regime','d','D₄','ℓ'],
 [['Low','4h + 2t','2h + 4t − 12','2t + h + 2'],['High','6h + 5','6h − 2','3h + 7']])
table(4.74,1.28,['Regime','D₈','i₈','δ','f'],
 [['Low','10h + 8t − 28','7h + 2t + 14','4h + 2t − 10','4h + 2t − 8'],
  ['High','18h − 8','9h + 19','6h − 5','6h − 3']])
ax.text(4.5,4.34,'Both: M = 9; i₄ = 3h + 6; ε₄ = 3; ε₈ = 7; ν = 0',ha='center',fontsize=12)
ax.text(4.5,3.88,'f(E/K) = d − 8; i₄ + ℓ = d + 8 = d + M − 1',ha='center',fontsize=12)
ax.text(4.5,3.4,'−Art(X/R) = 9 − 1 + f(E/K) = d',ha='center',fontsize=15,fontweight='bold')
ax.text(4.5,2.25,
 'Base valuations: v(π) = 1; quartic valuations: v_F(π) = 4.\n'
 'D₄ and D₈ are base discriminant exponents; relative different is in the point valuation.\n'
 'i₄ and i₈ are R-lengths; ℓ is a B₄-length. Both quartic/point residue degrees are one.',
 ha='center',va='center',fontsize=10.3,linespacing=1.65)
ax.text(4.5,.86,
 'Full proof: Lesson 8, Sections 6.0Y.1–7, UT1–UT14. Entire stated preparation only.\nGeneral conductor–index identity: JM30–JM32, Section6.0BI.\nSource: Milne, Algebraic Number Theory, Prop. 7.55 / Rem. 7.56.',
 ha='center',va='center',fontsize=10.2,linespacing=1.65)
fig.canvas.draw();renderer=fig.canvas.get_renderer()
for label in ax.texts:
 bounds=label.get_window_extent(renderer)
 assert bounds.x0>=0 and bounds.x1<=900 and bounds.y0>=0 and bounds.y1<=3100,label.get_text()
dest=Path(__file__).resolve().parents[1]/'assets/unbounded-third-II-star-proof-map.png'
fig.savefig(dest,dpi=100,metadata={'Title':'II-star with unbounded third valuation: both full regimes'})
plt.close(fig);print(dest.name)
