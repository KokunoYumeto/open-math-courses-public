"""The marked first higher algebras of an outer S3 action, lesson 41."""
from pathlib import Path
from html import escape

parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 1020" role="img" aria-labelledby="title desc">',
         '<title id="title">A nonabelian symmetry distinguishes an inclusion from its dual</title>',
         '<desc id="desc">For an outer S3 action, Q is the fixed factor, P the original factor, T its crossed product. Both successive indices are six. The first higher algebra of Q inside P is C plus C plus M2, which is noncommutative. That of P inside T is C to the sixth power, which is commutative. Correct reflected endpoints reconstruct the original and dual inclusions separately.</desc>',
         '<rect width="560" height="1020" fill="#ffffff"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#15283b} .small{font-size:17px}.body{font-size:20px}.head{font-size:23px;font-weight:bold}.label{font-size:19px;font-weight:bold}</style>']

def text(x, y, value, cls="body", anchor="start"):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')

def box(y, h, color="#edf4fb"):
    parts.append(f'<rect x="20" y="{y}" width="520" height="{h}" rx="10" fill="{color}" stroke="#9cb4cd"/>')

text(280, 38, "Index six does not fix the pair", "head", "middle")
box(64, 125)
text(40, 99, "An outer action of S₃ on the hyperfinite factor")
text(40, 137, "Q = P^S₃   ⊂   P   ⊂   T = P ⋊ S₃", "label")
text(40, 172, "[P : Q] = 6              [T : P] = 6", "small")
box(212, 175, "#edf6ed")
text(40, 247, "Original pair Q ⊂ P", "label")
text(40, 286, "First higher algebra: Q′ ∩ T = C[S₃]")
text(40, 323, "C ⊕ C ⊕ M₂(C) — noncommutative", "label")
text(40, 363, "Central trace weights: 1/6, 1/6, 2/3", "small")
box(409, 174, "#fff3e8")
text(40, 444, "Dual pair P ⊂ T", "label")
text(40, 483, "T₁ = M₆(P),   P′ ∩ T₁ = C⁶")
text(40, 520, "Six scalar blocks — commutative", "label")
text(40, 559, "Trace weights: 1/6 on each block", "small")
box(607, 130)
text(40, 643, "An isomorphism extends through the Jones tower.", "small")
text(40, 678, "An anti-isomorphism takes the opposite algebra.", "small")
text(40, 713, "Both preserve commutativity: these pairs differ.", "label")
box(761, 204, "#f2eefb")
text(40, 797, "Two reflected endpoints", "label")
text(40, 834, "Original N ⊂ M  →  M₁′ ∩ M∞ ⊂ M′ ∩ M∞", "small")
text(40, 872, "Dual M ⊂ M₁     →  M′ ∩ M∞ ⊂ N′ ∩ M∞", "small")
text(40, 914, "Each arrow is a trace-preserving anti-isomorphism", "small")
text(40, 942, "from a generating tunnel at finite depth.", "small")
text(40, 997, "Propositions 41.1–41.2; Theorem 41.4; Corollary 41.5", "small")
parts.append("</svg>")
Path(__file__).with_suffix(".svg").write_text("\n".join(parts)+"\n", encoding="utf-8")
