# Finiteness on compact complex spaces

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

On a compact complex space, the cohomology of every coherent analytic sheaf is finite-dimensional in every degree. This theorem of H. Cartan and J.-P. Serre is the analytic counterpart of the finiteness of coherent cohomology on proper schemes, and it is the input that makes Serre's comparison of algebraic and analytic geometry work for arbitrary coherent analytic sheaves. The proof compares two finite coverings by small Stein pieces, one inside the other: both compute the cohomology, and the comparison map is compact, so Schwartz's theorem gives finiteness. The only new point is that finite intersections of the pieces, which may be embedded in different charts, are again acyclic; this follows from Theorem B applied on products of balls. The last section lists where the analytic results of this course are used in the proof of the comparison theorems.

We use Cartan's coherence theorem and complex spaces, [Fréchet spaces of sections and Schwartz's theorem](frechet-spaces-of-sections-and-schwartzs-theorem.md) and [Theorems A and B on Stein manifolds](theorems-a-and-b-on-stein-manifolds.md). Čech cohomology of a covering with acyclic finite intersections computes sheaf cohomology [Stacks, Tag 01ET](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-cech-spectral-sequence-application).

Basic references are [Cartan–Serre 1953], [Demailly] and [Serre 1956].

## 1. Stein pieces and their intersections

Let \(X\) be a complex space. A **Stein piece** of \(X\) is an open set \(U\subset X\) together with an isomorphism of \(U\) onto a closed complex subspace of a Stein manifold \(V\); for example \(U=A\cap V\), where \(A\subset\Omega\subset\mathbf C^N\) is a local model of \(X\) and \(V\subset\Omega\) is a ball, so that \(A\cap V\) is closed in \(V\).

**Lemma 1.1.** Let \(U_1,\ldots,U_k\) be Stein pieces of \(X\), embedded in Stein manifolds \(V_1,\ldots,V_k\) by \(e_i:U_i\to V_i\). Then \(e=(e_1,\ldots,e_k)\) embeds \(U=U_1\cap\cdots\cap U_k\) as a closed complex subspace of the Stein manifold \(V_1\times\cdots\times V_k\). Consequently, for every coherent sheaf \(\mathcal S\) on \(X\), \(H^j(U,\mathcal S)=0\) for all \(j\geq1\).

**Proof.** *Closedness.* Let \(e(x_\nu)\to(y_1,\ldots,y_k)\) in the product. Since \(e_1(U_1)\) is closed in \(V_1\), \(y_1=e_1(x)\) for some \(x\in U_1\), and \(x_\nu\to x\) because \(e_1\) is a homeomorphism onto its image; likewise \(x_\nu\to x'\in U_2\), and so on. As \(X\) is Hausdorff, all these limits coincide, so the limit point is \(e(x)\) with \(x\in U\).

*Local structure.* Let \(x\in U\). The components of \(e_2,\ldots,e_k\) are holomorphic functions on \(U\) near \(x\); through the embedding \(e_1\) they are, near \(e_1(x)\), restrictions of holomorphic functions \(h\) on an open set of \(V_1\), because a local model's structure sheaf is a quotient of the ambient one. Near \(e(x)\), the image of \(U\) is therefore the graph \(\{(y,h(y))\}\) of \(h\) over the local model \(e_1(U)\subset V_1\), which is the local model in \(V_1\times\mathbf C^{N_2+\cdots+N_k}\) defined by the ideal of \(e_1(U_1)\) together with the equations \(w-h(y)\); projection to \(V_1\) identifies it with \(e_1(U)\) as complex spaces. So \(e\) is an isomorphism of \(U\) onto a closed complex subspace of \(V_1\times\cdots\times V_k\), whose ideal sheaf, defined locally in this way, is coherent.

*Vanishing.* The product of Stein manifolds is Stein Plurisubharmonic functions and Stein manifolds, Proposition 2.2. By Cartan's coherence theorem and complex spaces, Theorem 3.2(3), \(e_*\mathcal S\) is coherent and \(H^j(U,\mathcal S)=H^j(V_1\times\cdots\times V_k,e_*\mathcal S)\), which vanishes for \(j\geq1\) by [Theorems A and B on Stein manifolds, Theorem 4.1](theorems-a-and-b-on-stein-manifolds.md#4-theorem-b). \(\square\)

**Corollary 1.2.** Every covering of a complex space by Stein pieces is a Leray covering for every coherent sheaf: its Čech complex computes the sheaf cohomology. In particular, if \(X\) is covered by \(m\) Stein pieces, then \(H^q(X,\mathcal S)=0\) for every coherent \(\mathcal S\) and every \(q\geq m\).

**Proof.** By Lemma 1.1 and [Stacks, Tag 01ET](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-cech-spectral-sequence-application). With \(m\) opens, the alternating Čech complex has no cochains in degrees \(q\geq m\). \(\square\)

For instance, complex projective space \(\mathbf P^n\) is covered by the \(n+1\) Stein open sets \(\{T_j\neq0\}\cong\mathbf C^n\), so \(H^q(\mathbf P^n,\mathcal S)=0\) for \(q>n\) and every coherent analytic sheaf \(\mathcal S\); the same holds on every closed complex subspace of \(\mathbf P^n\).

## 2. The finiteness theorem

**Theorem 2.1 (Cartan–Serre).** Let \(X\) be a compact complex space and \(\mathcal S\) a coherent \(\mathcal O_X\)-module. Then \(H^q(X,\mathcal S)\) is finite-dimensional for every \(q\geq0\).

**Proof.** For each point of \(X\) choose a local model \(A\subset\Omega\subset\mathbf C^N\) which is a distinguished patch for \(\mathcal S\) ([Stein domains in complex space, Proposition 4.3](stein-domains-in-complex-space.md#4-coherent-sheaves-on-stein-domains)), and concentric balls \(V'\Subset V\Subset\Omega\) about the point. By compactness, finitely many of the Stein pieces \(U'_\alpha=A_\alpha\cap V'_\alpha\) cover \(X\); put \(U_\alpha=A_\alpha\cap V_\alpha\). The coverings \(\mathcal U=(U_\alpha)\) and \(\mathcal U'=(U'_\alpha)\) are Leray coverings by Corollary 1.2, so both Čech complexes compute \(H^\bullet(X,\mathcal S)\), and the restriction map \(\rho:C^\bullet(\mathcal U,\mathcal S)\to C^\bullet(\mathcal U',\mathcal S)\) induces the identity of \(H^\bullet(X,\mathcal S)\), in particular a surjection.

Each closure \(\overline{U'_\alpha}\subset A_\alpha\cap\overline{V'_\alpha}\) is compact and contained in \(U_\alpha\), so the closure of every finite intersection \(U'_{\alpha_0\ldots\alpha_k}\) is a compact subset of \(U_{\alpha_0\ldots\alpha_k}\). The Čech cochain spaces are finite products of the Fréchet spaces \(\mathcal S(U_{\alpha_0\ldots\alpha_k})\), and by [Fréchet spaces of sections, Proposition 5.2(3)](frechet-spaces-of-sections-and-schwartzs-theorem.md#5-the-topology-on-sections-of-coherent-sheaves) each restriction \(\mathcal S(U_{\alpha_0\ldots\alpha_k})\to\mathcal S(U'_{\alpha_0\ldots\alpha_k})\) is compact. So \(\rho\) is compact in every degree, and the finiteness criterion [Fréchet spaces of sections, Theorem 2.2](frechet-spaces-of-sections-and-schwartzs-theorem.md#2-schwartz-s-theorem) shows that \(H^q(X,\mathcal S)\) is finite-dimensional, and Hausdorff, for every \(q\). \(\square\)

*Reference:* [Cartan–Serre 1953] states and proves this theorem; the proof through Schwartz's theorem is arranged as in [Demailly].

**Corollary 2.2.** For every coherent sheaf \(\mathcal S\) on a compact complex space, the space of global sections \(\mathcal S(X)\) is finite-dimensional, and if \(X\) is covered by \(m\) Stein pieces, only the degrees \(q<m\) can be nonzero.

**Proof.** Theorem 2.1 with \(q=0\), and Corollary 1.2. \(\square\)

## 3. The analytic results used for the comparison theorems

The proof of Serre's comparison theorems and Chow's theorem in [Complex analytic spaces and analytification](course:AG-QC/complex-analytic-spaces-and-analytification) and [Serre's comparison theorems and Chow's theorem](course:AG-QC/serres-comparison-theorems-and-chows-theorem) uses the following analytic results, all proved in this course in the generality stated there.

| Result | Where it is proved |
|---|---|
| Weierstrass preparation and division; \(\mathcal O_n\) Noetherian with completion the formal power series ring | [Complex analytic spaces and analytification, Section 2](course:AG-QC/complex-analytic-spaces-and-analytification#2-local-analytic-algebra) |
| \(\mathcal O_n\) is a unique factorization domain | The local ring of holomorphic germs, Theorem 3.1 |
| Oka's coherence theorem | [Coherent sheaves and Oka's coherence theorem, Theorem 2.1](coherent-sheaves-and-okas-theorem.md#2-oka-s-coherence-theorem) |
| The local analytic Nullstellensatz | Analytic germs, local parametrization and the Nullstellensatz, Theorem 5.1 |
| Finite projections of irreducible germs; local dimension equals the Krull dimension of the local ring | Analytic germs, Theorems 4.1 and 5.4 |
| Cartan's coherence of vanishing ideals of analytic subsets, including singular ones | Cartan's coherence theorem and complex spaces, Theorem 1.1 |
| Vanishing of coherent cohomology in positive degrees on complex manifolds with a smooth strictly plurisubharmonic exhaustion | [Theorems A and B on Stein manifolds, Theorem 4.1](theorems-a-and-b-on-stein-manifolds.md#4-theorem-b) |
| Finite-dimensionality of coherent cohomology on compact complex analytic spaces | Theorem 2.1 above |

In particular, the standard affine cover of \(\mathbf P^n\) and all intersections of its members are Stein ([Theorems A and B on Stein manifolds, Corollary 4.2](theorems-a-and-b-on-stein-manifolds.md#4-theorem-b)), so the Čech complex of this cover computes the analytic cohomology of every coherent analytic sheaf on \(\mathbf P^n\).

## 4. Exercises

**Exercise 4.1.** Compute \(H^q(\mathbf P^1,\mathcal O(d))\) for the analytic line bundles \(\mathcal O(d)\), using the cover by two copies of \(\mathbf C\), and check that the dimensions are finite, as Theorem 2.1 asserts.

*Solution.* The cover \(\{T_0\neq0\},\{T_1\neq0\}\) consists of two Stein sets with Stein intersection \(\mathbf C^*\), so it is a Leray cover. With the coordinate \(z=T_1/T_0\) and Laurent expansions on \(\mathbf C^*\), the Čech complex is \(\mathcal O(\mathbf C)\oplus\mathcal O(\mathbf C)\to\mathcal O(\mathbf C^*)\), where the first summand contributes the exponents \(a\geq0\) and the second, after the transition factor \(z^d\), the exponents \(a\leq d\). Hence \(h^0=\max(d+1,0)\) (exponents \(0\leq a\leq d\)) and \(h^1=\max(-d-1,0)\) (exponents \(d<a<0\)), and \(h^q=0\) for \(q\geq2\). This agrees with the computation in the lesson on Serre's comparison theorems.

**Exercise 4.2.** Show that Theorem 2.1 fails for noncompact spaces, even for the structure sheaf of a Stein manifold in degree zero.

*Solution.* \(\mathcal O(\mathbf C)\) contains all polynomials, an infinite-dimensional space. The proof breaks down because the comparison of two coverings, one relatively compact in the other, is only available for finitely many relatively compact pieces covering a compact space.

**Exercise 4.3.** Let \(X\) be a compact complex space covered by \(m\) Stein pieces. Show that \(\chi(X,\mathcal S)=\sum_q(-1)^q\dim H^q(X,\mathcal S)\) is defined for every coherent \(\mathcal S\) and is additive in short exact sequences.

*Solution.* By Theorem 2.1 and Corollary 1.2, only the finitely many degrees \(q<m\) contribute, each finite-dimensional. A short exact sequence of coherent sheaves gives a long exact cohomology sequence of finite-dimensional spaces of finite length, and the alternating sum of dimensions in a finite exact sequence vanishes.

## References

- [Cartan–Serre 1953] H. Cartan and J.-P. Serre, Un théorème de finitude concernant les variétés analytiques compactes, *Comptes Rendus de l'Académie des Sciences de Paris* 237 (1953), 128–130.
- [Demailly] J.-P. Demailly, *Complex Analytic and Differential Geometry*, version of 21 June 2012, freely available from the author with permission to copy, modify and redistribute with credit. <https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf>
- [Serre 1956] J.-P. Serre, Géométrie algébrique et géométrie analytique, *Annales de l'Institut Fourier* 6 (1956), 1–42. <https://www.numdam.org/item/AIF_1956__6__1_0/>
- [Stacks] The Stacks project, cited by tag; each tag links to the same result in the AI Integrated Stacks Project. <https://stacks.math.columbia.edu/>
