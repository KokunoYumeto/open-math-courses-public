<span id="bounded-factorization"></span>
# Bounded factorization

*CC0 1.0.*

Let \(M\subseteq B(H)\) be a faithfully represented von Neumann algebra. In particular, one may take \(M=B(H)\) for the [resolvent-order proof](../../reader/orbit-proof-route/target-fc.html#OA-MOD-FC-06). The lemma uses the bounded operator and Hilbert-space foundations.

Positivity refers to the inherited cone above. It does not assert that \(\ell\) is bounded for the operator norm, or that it has already been extended to a normal weight on all of \(M_+\). The order on these forms is positivity of their difference on this cone.

<a id="OA-MOD-DW-02"></a>
<a id="OA-MOD-DW-02-lemma-only"></a>

<span id="oa-mod-dw-02--a-factorization-inside-the-algebra"></span>
<span id="oa-mod-dw-02"></span>
## OA-MOD-DW-02 — A factorization inside the algebra

**Lemma.** If \(x,y\in M\) and \(y^*y\leq x^*x\), there is a unique contraction \(v\in M\) which vanishes on \(\overline{xH}^{\perp}\) and satisfies \(y=vx\), in any faithful concrete realization \(M\subseteq B(H)\).

**Proof.** On \(xH\) define \(x\xi\mapsto y\xi\). The inequality says both that this is well defined and that its norm is at most one. Extend it continuously to \(\overline{xH}\), and set it equal to zero on the orthogonal complement. This proves existence and uniqueness in \(B(H)\). Every unitary \(u\in M'\) preserves \(\overline{xH}\); because \(x,y\) commute with \(u\), both \(v\) and \(uvu^*\) have the prescribed properties. Thus \(v\) commutes with every unitary of \(M'\). Every element of a unital C*-algebra is a linear combination of unitaries: a self-adjoint contraction \(b\) is the real part of \(b+i(1-b^2)^{1/2}\). Consequently \(v\in M''=M\). This uses bounded continuous functional calculus and the bicommutant theorem, with their stated hypotheses. \(\square\)
