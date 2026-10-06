# Uniform bounds and moving distributional tests

Selected from AN-01, *Order, positivity and distributional limits*, Theorem 5.1.
The reconstructed source is by GPT-6 Astra (OpenAI), Ultra, October 2026; its
earlier edition is by GPT-6.1 Sol (OpenAI), Ultra. This selected CC0 exposition
preserves the common-order and moving-test proof. Its stronger finite-net
conclusion is not needed or imported. The sole adjustment is to state the
common compact support explicitly, so no global test-topology theorem is hidden.

Let X be open in Euclidean space. A distribution is a complex-linear functional
on smooth compactly supported functions such that on each fixed compact K it
obeys a bound C p(K,m), where p(K,m) is the maximum of the supremum norms of all
derivatives through order m. Write D_K for that fixed-support space. Weak
convergence means convergence on every fixed smooth compact test.

**Theorem U1 (weak completeness and uniform local order).** Suppose \(u_j\in\mathcal D'(X)\) and \(u_j(\phi)\) converges for each smooth compact test. The limits define a distribution \(u\). For every fixed compact \(K\), one constant \(C_K\) and one order \(m_K\) work in the local finite-order estimate stated above for all \(u_j\) and for \(u\).

If the tests \(\phi_j,\phi\) have one common compact support and
\(\phi_j\to\phi\) uniformly with every derivative, then
\(u_j(\phi_j)\to u(\phi)\).

**Proof.** Scalar limits preserve linearity. On a fixed \(\mathcal D_K\), [complete-test-spaces.md](complete-test-spaces.md), Sections 14.1–14.2, proves that the increasing derivative seminorms give a complete metric topology. The proof takes uniform limits of every derivative of the zero extensions and uses the fundamental theorem on coordinate segments to identify successive derivatives; no regularity of the boundary of \(K\) is needed.

For \(r=1,2,\ldots\), put

\[
 A_r=\{\phi\in\mathcal D_K:\sup_j|u_j(\phi)|\le r\}.
\]

Each is closed, because every \(u_j\) is continuous there, and their union is \(\mathcal D_K\), because each convergent scalar sequence is bounded. The proved Baire theorem gives a point \(\phi_0\) and a neighborhood \(p_{K,m}(h)<\varepsilon\) with \(\phi_0+h\in A_r\), including \(h=0\). Subtraction gives \(\sup_j|u_j(h)|\le2r\) in that neighborhood. If \(p_{K,m}(h)>0\), apply this to \(\varepsilon h/(2p_{K,m}(h))\), obtaining the common bound \(4r p_{K,m}(h)/\varepsilon\). If the seminorm is zero, \(h=0\), since the zeroth derivative is included. Passing to the scalar limit gives the same bound for \(u\), which proves it is a distribution.

For moving tests, their supports lie in one compact by the explicit common-support hypothesis, and

\[
 u_j(\phi_j)-u(\phi)
   =u_j(\phi_j-\phi)+(u_j-u)(\phi).
 \tag{5.1}
\]

The common derivative bound controls the first term, and fixed-test convergence controls the second.
\(\square\)

Free comparison: Semyon Dyatlov, [18.155 notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), Theorems 4.14 and 4.16, Propositions 4.17–4.18. Their complete used proof is supplied here together with the separately licensed complete-test-space component.
