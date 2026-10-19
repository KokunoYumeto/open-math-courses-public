"""Exact coordinate and factorization diagram for SQD:D1--D3. CC0-1.0."""
from pathlib import Path
from html import escape
W,H=1120,740
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
 '<title id="title">One normalized transverse variable and the prescribed divisor</title>',
 '<desc id="desc">The degree-one two-dimensional normal form has only x after tau equals zero and xi equals one. The three-dimensional flat-family model has active x and eta after kappa equals one, with z inactive. A degenerate prescribed divisor can fail while a different exact divisor exists.</desc>',
 '<rect width="1120" height="740" rx="14" fill="#f5f8fb"/>',
 '<style>text{font-family:system-ui,sans-serif;fill:#142e43}.heading{font-size:23px;font-weight:650}.body{font-size:20px}.small{font-size:17px}.formula{font-size:23px;font-family:Georgia,serif}</style>',
 '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#247682"/></marker></defs>']
def text(x,y,s,cls='body'):parts.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(s)}</text>')
def box(x,y,w,h):parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="white" stroke="#9bb4c6"/>')
def arrow(x,y,z):parts.append(f'<path d="M{x} {y}H{z}" fill="none" stroke="#247682" stroke-width="2.4" marker-end="url(#arrow)"/>')
text(32,40,'Exact division and the cotangent slice','heading')
box(25,65,1070,195)
text(45,97,'D2 · Base dimension two','heading')
text(45,132,'(t,x; τ,ξ),  ξ > 0','formula');arrow(315,125,450)
text(335,109,'τ = 0','small');text(335,151,'ξ = 1','small')
text(475,130,'One active transverse variable: x')
text(45,179,'a(t,x) = x²A(t,x),     a(t₀,x) = x²K(x)','formula')
text(45,218,'K(0) ≠ 0    ⇒    h = A/K is smooth and nonnegative;  r = 0','formula')
text(45,244,'The sign inequality and the nonzero Hessian are both hypotheses.','small')
box(25,280,1070,190)
text(45,312,'X3 · Base dimension three','heading')
text(45,348,'(t,x,z; τ,η,κ),  κ > 0','formula');arrow(340,341,455)
text(355,325,'τ = 0','small');text(355,367,'κ = 1','small')
text(478,346,'Two active variables: (x,η);  z is inactive')
text(45,395,'p = τ + iκF(t,x,η/κ)','formula')
text(45,432,'For x > 0 and η = 0:   F(0,x,0) = 0,   F(t,x,0) = t²E₊(x)²','formula')
text(45,457,'At t ≠ 0 the numerator is nonzero on the prescribed divisor-zero set.','small')
box(25,490,1070,220)
text(45,523,'D3 · A different divisor changes the question','heading')
text(45,564,'Im p = ξ(x⁴ + t²x²)','formula')
text(45,607,'Prescribed g = ξx⁴','formula');arrow(350,599,455)
text(475,607,'h = 1 + t²/x²  (x ≠ 0): no continuous extension','body')
text(45,655,'Alternative divisor ξx²','formula');arrow(350,647,455)
text(475,655,'h* = x² + t² ≥ 0: exact smooth factorization','body')
text(45,691,'The Hessian at the prescribed time t₀ = 0 is zero.','small')
parts.append('</svg>')
dest=Path(__file__).with_name('one-transverse-variable.svg')
dest.write_bytes(('\n'.join(parts)+'\n').encode('utf-8'))
