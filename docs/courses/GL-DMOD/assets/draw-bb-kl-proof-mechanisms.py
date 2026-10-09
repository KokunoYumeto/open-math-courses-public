from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
BLUE='#165b81'
AMBER='#97551c'
INK='#173247'

def box(ax, x,y,w,h,label,kind='proved'):
    color=BLUE if kind=='proved' else AMBER
    patch=FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.016,rounding_size=0.015', facecolor='#edf5fa' if kind=='proved' else '#fff1df',edgecolor=color,linewidth=1.6,linestyle='solid' if kind=='proved' else '--')
    ax.add_patch(patch)
    ax.text(x+w/2,y+h/2,label,ha='center',va='center',color=INK,fontsize=11,linespacing=1.4)

def arrow(ax,start,end,pending=False):
    color = AMBER if pending else BLUE
    ax.plot([start[0],end[0]],[start[1],end[1]],color=color,linewidth=1.5,linestyle='--' if pending else '-',clip_on=True)
    marker = '>' if end[0]>start[0] else '<' if end[0]<start[0] else '^' if end[1]>start[1] else 'v'
    ax.plot([end[0]],[end[1]],marker=marker,markersize=8,color=color,clip_on=True)

fig,ax=plt.subplots(figsize=(12,7.4),dpi=160)
ax.set(xlim=(0,1),ylim=(0,1)); ax.axis('off')
ax.text(.02,.96,'Central projection and all quasi-coherent cohomology',fontsize=19,fontweight='bold',color=INK)
box(ax,.04,.72,.41,.16,'Finite R-stable filtration E\nEach factor has one character χᵢ\nNo finite-dimensionality assumption')
box(ax,.56,.72,.40,.16,'Actual projectors eχ = pχ(z)\n(ker χ)ⁿχ E[χ] = 0\nnχ = number of factors labeled χ')
arrow(ax,(.47,.80),(.54,.80))
ax.text(.49,.83,'A.1',ha='center',color=BLUE)
box(ax,.04,.45,.41,.17,'Highest-weight factor M\nin (M ⊗ Aᴺ) ⊗ Fᴺ\nCharacter occurs once',kind='pending')
box(ax,.56,.45,.40,.17,'Multiplicity-one projection\nM ↔ selected factor\nRetraction is a k-sheaf map')
arrow(ax,(.47,.535),(.54,.535))
ax.text(.49,.565,'A.2',ha='center',color=BLUE)
arrow(ax,(.755,.70),(.755,.64))
box(ax,.04,.17,.41,.17,'Coherent E ⊂ M\nHᑫ((E ⊗ Aᴺ) ⊗ Fᴺ) = 0\nfor N large and q > 0')
box(ax,.56,.17,.40,.17,'Retraction kills Hᑫ(E → M)\nFinite Čech + directed union\nHᑫ(M) = 0 for every q > 0')
arrow(ax,(.47,.255),(.54,.255))
ax.text(.49,.285,'C.1',ha='center',color=BLUE)
arrow(ax,(.755,.43),(.755,.36))
ax.text(.03,.065,'Solid: locally proved argument. Dashed: pending flag representation identification.\nThe projector is generally not O-linear: 0 → O → O(1)² → O(2) → 0 has no O-linear retraction.',fontsize=10,color=INK)
fig.tight_layout()
fig.savefig(OUT/'bb-central-projector-cohomology.png',bbox_inches='tight')
plt.close(fig)

fig,ax=plt.subplots(figsize=(12,7.4),dpi=160)
ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.02,.96,'The exact KL coefficient mechanism',fontsize=19,fontweight='bold',color=INK)
box(ax,.04,.70,.41,.17,'Actual complex Kw on cells Cᵧ\nCᵧ ≅ ℂˡ⁽ʸ⁾\nΔᵧ = jᵧ! k[ℓ(y)]')
box(ax,.56,.70,.40,.17,'Cellular reconstruction (K.1)\n[Kw] = Σᵧ (−1)ˡ⁽ʸ⁾ χᵧ(Kw)[Δᵧ]\nχᵧ = ordinary stalk Euler characteristic')
arrow(ax,(.47,.785),(.54,.785))
box(ax,.04,.43,.41,.17,'Parity degrees: 2r − ℓ(w)\nQᵧ,w(q) = Σᵣ dim H²ʳ⁻ˡ⁽ʷ⁾ qʳ\nIC parity and stalk bounds\nremain required',kind='pending')
box(ax,.56,.43,.40,.17,'Every stalk term has sign (−1)ˡ⁽ʷ⁾\n[Kw] = Σᵧ (−1)ˡ⁽ʷ⁾⁻ˡ⁽ʸ⁾\n             Qᵧ,w(1)[Δᵧ]')
arrow(ax,(.47,.515),(.54,.515))
ax.text(.49,.548,'K.11',ha='center',color=BLUE)
arrow(ax,(.755,.68),(.755,.62))
box(ax,.04,.16,.41,.17,'Pending graded geometry\nQᵧ,w = Pᵧ,w via fixed Hecke character\nExact BB / RH / category O dictionary',kind='pending')
box(ax,.56,.16,.40,.17,'[L(−wρ − ρ)] =\nΣᵧ≤w (−1)ˡ⁽ʷ⁾⁻ˡ⁽ʸ⁾ Pᵧ,w(1)\n                         [M(−yρ − ρ)]',kind='pending')
arrow(ax,(.47,.245),(.54,.245),pending=True)
arrow(ax,(.755,.41),(.755,.35),pending=True)
ax.text(.03,.06,'Canonical-basis existence/uniqueness is locally proved in K.2.\nSolid arrows prove formal deductions; dashed boxes/arrows retain the substantive IC and dictionary obligations.',fontsize=10,color=INK)
fig.tight_layout()
fig.savefig(OUT/'kl-stalk-euler-mechanism.png',bbox_inches='tight')
plt.close(fig)
