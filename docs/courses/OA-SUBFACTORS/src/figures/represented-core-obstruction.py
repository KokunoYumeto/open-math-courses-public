"""CC0: exact finite checks and reproducible represented-core diagram."""
from pathlib import Path
from html import escape
import argparse
import json


def exact_checks():
    import sympy as s
    I = s.eye(2)
    E = {(i, j): I[:, i] * I[:, j].T for i in range(2) for j in range(2)}
    v = s.diag(1, -1)
    vs = [I, v]
    tensor = s.kronecker_product
    u = sum((tensor(E[i, i], I, vs[i]) for i in range(2)), s.zeros(8))
    def en(x):
        z = s.zeros(4)
        for i in range(2):
            z += x[4*i:4*i+4, 4*i:4*i+4] / 2
        return tensor(I, z)
    def ep0(x):
        z = s.zeros(4)
        for i in range(4):
            for j in range(4):
                z[i,j] = (x[2*i,2*j] + x[2*i+1,2*j+1]) / 2
        return tensor(z, I)
    def ep(x): return u * ep0(u.H*x*u) * u.H
    def eq(x): return en(ep0(x))
    a = [s.sqrt(2)*tensor(E[i,j], I, vs[i]*vs[j].H) for i in range(2) for j in range(2)]
    assert u.H*u == s.eye(8)
    assert sum((z*z.H for z in a), s.zeros(8)) == 4*s.eye(8)
    for k in range(4):
        assert ep(a[k]) == a[k]
        for l in range(4):
            assert en(a[k].H*a[l]) == (s.eye(8) if k == l else s.zeros(8))
    for i in range(8):
        for j in range(8):
            x = s.zeros(8); x[i,j] = 1
            assert en(ep(x)) == eq(x)
            assert ep(en(x)) == eq(x)
            assert sum((z*en(z.H*x) for z in a), s.zeros(8)) == x
    X = tensor(E[0,1]+E[1,0], I, I)
    assert X.H == X and X*X == s.eye(8) and ep(X) == s.zeros(8)
    # The twist fails the depth-zero smoothness test.
    dv = u*tensor(E[0,1],I,I)*u.H
    w = tensor(I,I,E[0,1]+E[1,0])
    assert dv*w != w*dv
    # Exact intersection dimension: dim(P_v cap D) = 16+4-rank(P_v+D).
    pv = [u*tensor(E[i,j],E[k,l],I)*u.H for i in range(2) for j in range(2) for k in range(2) for l in range(2)]
    dd = [tensor(E[i,j],I,I) for i in range(2) for j in range(2)]
    rank = s.Matrix.hstack(*(x.reshape(64,1) for x in pv+dd)).rank()
    assert 16+4-rank == 2
    cup = sum((tensor(E[i,j],E[i,j]) for i in range(2) for j in range(2)), s.zeros(4))/2
    assert cup*cup == cup and s.trace(cup)/4 == s.Rational(1,4)
    words = [tensor(I,E[a,b])*cup*tensor(I,E[c,d]) for a in range(2) for b in range(2) for c in range(2) for d in range(2)]
    assert s.Matrix.hstack(*(x.reshape(16,1) for x in words)).rank() == 16
    # A nonreal trace checks the conjugation order in the full parameter formula.
    phase=s.diag(1,s.I); c=(1+s.I)/2
    u=tensor(E[0,0],I,I)+tensor(E[1,1],I,phase)
    expected=c*tensor(E[0,1],I,phase.H)+s.conjugate(c)*tensor(E[1,0],I,phase)
    assert s.simplify(ep(X)-expected) == s.zeros(8)
    assert s.simplify(s.trace((X-ep(X)).H*(X-ep(X)))/8) == s.Rational(1,2)
    return dict(exact_three_site_matrix_units=64, common_basis_orthogonality_pairs=16,
                both_expectation_orders_checked=True, common_basis_reconstruction_checked=True,
                full_common_basis_index=4, first_commutant_dimension=4,
                represented_intersection_dimension=2, witness_squared_L2_distance=1,
                depth_zero_smoothness_failure=True, adjacent_cup_trace='1/4',
                nonreal_trace_parameter_checked=True, nonreal_trace_squared_distance='1/2',
                cup_and_second_site_generate_both_matrix_sites=True,
                full_II1_statement_uses_the_written_tensor_argument=True)


def draw(path):
    out = ['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="850" viewBox="0 0 1080 850">',
           '<rect width="1080" height="850" fill="#fafbfc"/>',
           '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#315b76"/></marker></defs>']
    def text(x,y,t,size=22,color='#172d3d',weight='normal'):
        out.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(t)}</text>')
    def box(x,y,w,h,title,lines,color='#eaf3f8'):
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}" stroke="#91aabb" stroke-width="2"/>')
        text(x+18,y+35,title,24,weight='bold')
        for k,line in enumerate(lines): text(x+18,y+70+30*k,line,20)
    def arrow(x1,y1,x2,y2):
        out.append(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#315b76" stroke-width="2.5" fill="none" marker-end="url(#arrow)"/>')
    text(32,42,'A commuting-square image need not be an actual core',29,weight='bold')
    text(32,78,'H = binary hyperfinite factor;  K = any II₁ factor;  v ∈ U(K).',20)
    box(32,104,1016,104,'An actual core, transported by a controlled unitary',[
        'P₀ = Mat₂ ⊗ H ⊗ 1;     u = E₀₀ ⊗ 1 ⊗ 1 + E₁₁ ⊗ 1 ⊗ v;     Pᵥ = uP₀u*.',
        'Ad(u) fixes Q pointwise and preserves the trace.  Theorem 51.7 constructs the tunnel with core P₀.'])
    box(32,252,390,112,'Q = 1 ⊗ H ⊗ 1',['The smaller represented algebra.'])
    box(606,252,442,112,'Pᵥ = { Σ Eᵢⱼ ⊗ bᵢⱼ ⊗ vᵢvⱼ* }',['v₀ = 1;  v₁ = v;  bᵢⱼ ∈ H.'])
    box(32,430,390,112,'N = 1 ⊗ H ⊗ K',['The fixed smaller II₁ factor.'])
    box(606,430,442,112,'M = Mat₂ ⊗ H ⊗ K',['[M:N] = [Pᵥ:Q] = 4.'])
    arrow(430,307,596,307); arrow(430,487,596,487)
    arrow(208,374,208,420); arrow(828,374,828,420)
    text(321,400,'E_N E_{Pᵥ} = E_{Pᵥ} E_N = E_Q',23)
    box(32,573,1016,112,'One common basis verifies nondegeneracy and the index',[
        'aᵢⱼ = √2 Eᵢⱼ ⊗ 1 ⊗ vᵢvⱼ*;     E_N(aᵢⱼ* aₖₗ) = δᵢₖδⱼₗ 1;     Σ aᵢⱼaᵢⱼ* = 4·1.',
        'Every y ∈ M equals Σ aᵢⱼ E_N(aᵢⱼ* y);   the coefficients lie in Q when y ∈ Pᵥ.'])
    box(32,710,1016,110,'Every actual core must contain D = N′ ∩ M = Mat₂ ⊗ 1 ⊗ 1',[
        'X = (E₀₁ + E₁₀) ⊗ 1 ⊗ 1 ∈ D;     dist₂(X, Pᵥ)² = 1 − |τ(v)|².',
        'For v = diag(1,−1), E_{Pᵥ}(X) = 0 and dist₂(X, Pᵥ) = 1.  Proof: (51.26), (51.38).'], '#fff0e9')
    text(33,842,'Square and tensor-factor positions are schematic. All formulas retain the normalized product traces.',16)
    out.append('</svg>')
    path.write_text('\n'.join(out)+'\n',encoding='utf-8')


if __name__ == '__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--check',action='store_true'); args=parser.parse_args()
    if args.check: print(json.dumps(exact_checks()))
    draw(Path(__file__).with_name('represented-core-obstruction.svg'))
