"""Reproducible schematic for PL3, PL4–PL7 and PL8; independent CC0-1.0."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

OUT = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "svg.fonttype": "none"})
fig = plt.figure(figsize=(15, 9), facecolor="#f7f8fb")
left = fig.add_axes([.04, .24, .42, .63])
right = fig.add_axes([.50, .24, .46, .63])
for ax in (left, right):
    ax.set(xlim=(0, 10), ylim=(0, 10))
    ax.axis("off")
fig.text(.04, .95, "Perfect cochains with the actual scalar map", size=24, weight="bold", color="#14233e")
fig.text(.04, .90, "Original compact Whitney strata • perfect stalk complexes • commutative k of finite global dimension",
         size=13, color="#40516a")
def line(ax, a, b, label=None, color="#285f91"):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=16, linewidth=1.8, color=color))
    if label:
        ax.text((a[0]+b[0])/2, (a[1]+b[1])/2+.18, label, ha="center", va="bottom", size=11, color=color)
def box(ax, x, y, w, h, text, color="#e8eff7", size=12):
    ax.add_patch(Rectangle((x, y), w, h, fc=color, ec="#8093ac", lw=1.2))
    ax.text(x+w/2, y+h/2, text, ha="center", va="center", size=size, color="#14233e")
left.text(0, 9.75, "PL3: the end coordinate and completion", weight="bold", size=16)
box(left, .25, 6.5, 2.3, 1.7, "Q = {h ≤ C}\ncompact core")
box(left, 2.55, 6.5, 6.6, 1.7, "", "#e7f4ee", 13)
left.text(5.85, 7.82, "H × [C, ∞)", ha="center", size=13)
left.text(5.85, 7.43, "Φ(b,t) = β(t−C,b)", ha="center", size=13)
left.plot([2.55,2.55],[6.35,8.4], color="#325d44", lw=2)
left.text(2.55, 8.55, "H = {h=C}", ha="center", size=11)
line(left, (4,6.75), (8.5,6.75), "v = w/dh(w),  dh(v) = 1", "#325d44")
left.text(5, 6.05, "Each finite flow segment stays in a compact h-band.", ha="center", size=11)
line(left, (5,5.85), (5,4.9), "s = (t−C)/(1+t−C)")
box(left, .25, 2.75, 2.3, 1.7, "same Q")
box(left, 2.55, 2.75, 6.6, 1.7, "", "#e7f4ee", 14)
left.text(5.85, 4.02, "H × [0,1]", ha="center", size=14)
left.text(5.85, 3.60, "S ≅ int(S̄)", ha="center", size=14)
left.plot([9.15,9.15],[2.5,4.65], color="#a63c4b", lw=3)
left.text(9.15, 4.82, "∂S̄ = H × {1}", ha="right", size=11, color="#a63c4b")
line(left, (7.8,2.94), (3.0,2.94), "r̄ collapses the attached collar")
left.text(5, 2.1, "Ā = r̄⁻¹(A|Q),   j⁻¹Ā ≃ A by NMG5", ha="center", size=13)
left.text(.25, .9, "The rectangles suppress the H-direction.\nThey do not identify H with an interval or give\ncoordinates on an arbitrary singular link.", size=11, color="#56667e")
right.text(0, 9.75, "PL4–PL7: finite constructions retain the arrows", weight="bold", size=15)
box(right, .15, 8.2, 9.6, 1.0, "RΓc(S;A) ≃ fib[ RΓ(S̄;Ā) → RΓ(∂S̄;Ā) ]", "#e7f4ee", 12)
right.text(5, 7.85, "The arrow is restriction; the comparison is extension by zero.", ha="center", size=10.5)
box(right, .15, 6.0, 9.6, 1.15, "Product-collar metric → finite convex cover of the half\nDerived Čech columns are finite sums of perfect stalk complexes.", size=11.5)
line(right, (5,7.8), (5,7.2))
box(right, .15, 4.0, 9.6, 1.15, "Original closed dimension skeleta\nRΓc(Tr;A) → RΓ(Xr;A) → RΓ(Xr−1;A) → [1]", size=12)
line(right, (5,5.9), (5,5.2))
right.text(5.45,5.48,"finite sums and cones",size=10,color="#285f91")
right.text(0, 3.4, "PL8: the coefficient square for the fixed pair", weight="bold", size=14)
right.text(.4, 2.6, "RΓ(K;A) ⊗ᴸₖ B", ha="left", size=12)
right.text(6.0, 2.6, "RΓ(L;A) ⊗ᴸₖ B", ha="left", size=12)
right.text(.4, 1.1, "RΓ(K;A ⊗ᴸₖ B)", ha="left", size=12)
right.text(6.0, 1.1, "RΓ(L;A ⊗ᴸₖ B)", ha="left", size=12)
line(right, (3.45,2.66), (5.75,2.66), "res ⊗ 1")
line(right, (3.8,1.16), (5.75,1.16), "res")
line(right, (1.6,2.4), (1.6,1.4))
line(right, (7.3,2.4), (7.3,1.4))
right.text(1.95, 1.9, "αK ≃", size=11, color="#285f91")
right.text(7.65, 1.9, "αL ≃", size=11, color="#285f91")
right.text(5, .4, "Taking fibres gives MS(A) ⊗ᴸₖ B → MS(A ⊗ᴸₖ B).", ha="center", size=12)
fig.text(.04,.15, "No global orientation is selected: the boundary-relative object retains the orientation information.",
         size=12, color="#40516a")
fig.text(.04,.105, "Proof locators: PL3 full collar; PL6 compact support; PL7 original localization; PL8 actual restriction square.",
         size=11, color="#40516a")
fig.text(.04,.065, "Internal antecedents: F2–F8, NMG5, SCF7–SCF9, DG-FND Riemannian A.1/B.5 and Geodesics A.1.",
         size=10.5, color="#56667e")
fig.savefig(OUT/"perfect-whitney-link.svg", bbox_inches="tight")
fig.savefig(OUT/"perfect-whitney-link.png", dpi=150, bbox_inches="tight")
print("Wrote perfect-whitney-link.svg and perfect-whitney-link.png")
