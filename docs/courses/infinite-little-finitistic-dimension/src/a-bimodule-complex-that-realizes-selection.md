# A bimodule complex that realizes selection

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Proposition 3.1 of [Clearing denominators in a finite diagram](clearing-denominators-in-a-finite-diagram.md) gives complexes \(D_0,D_1,D_2\), chain maps \(f_a\) for the arrows of \(B\), and homotopies \(h_\rho\) for its relations. A diagram of shape \(B\) whose relations hold only up to homotopy does not, in general, come from a complex of \(B\)-bimodules: higher coherences can obstruct it [Keller, Sections 2 and 6]. For \(B\) the obstruction disappears, because every relation runs from vertex \(0\) to vertex \(2\) and nothing can be composed with it. This lesson writes down one complex \(P\) of \(B\)-bimodules in three columns whose differential contains the arrows, the maps \(f_a\) and the homotopies \(h_\rho\) (Lemma 1.1), recovers the \(D_i\) and \(f_a\) from it up to homotopy (Lemmas 2.1 and 2.2), and concludes
\[
\begin{aligned}
P\otimes^{\mathbf L}_BM(Y)\simeq{}&M(H(Y))\\
&\oplus M(H(Y))[3]
\end{aligned}
\]
for every finite-dimensional \(R\)-module \(Y\), in the derived category \(\mathrm D(B)\) of left \(B\)-modules (Theorem 3.1). The construction follows [OpenAI-FD, Section 4].

Notation is as in the previous lessons: \(B\) has vertices \(0,1,2\), arrow sets \(\mathcal A_{01}\), \(\mathcal A_{12}\), and relation basis \(\mathcal R\) with \(\rho=\sum_{a,b}\rho_{ba}\,ba\). Tensor products without subscript are over \(k\). A complex \(B\mathbf e_j\otimes D_i\) is a complex of \(B\)-bimodules: \(B\) acts on the left on the first factor and on the right on the second, and its differential is \(c\otimes v\mapsto c\otimes dv\).

## 1. The three-column complex

Form the complexes of bimodules
\[
\begin{aligned}
L'_0&=\bigoplus_{i=0}^2B\mathbf e_i\otimes D_i,\\
L'_1&=\bigoplus_{a\colon i\to j}B\mathbf e_j\otimes D_i,\\
L'_2&=\bigoplus_{\rho\in\mathcal R}B\mathbf e_2\otimes D_0,
\end{aligned}
\]
with internal differentials \(d_0,d_1,d_2\). Write \((x)_i\), \((x)_a\), \((x)_\rho\) for an element \(x\) placed in the summand with that index. Define maps of graded bimodules, with \(a\colon i\to j\) in the first line:
\[
\begin{aligned}
p(c\otimes v)_a&=(ca\otimes v)_i-(c\otimes f_a(v))_j,\\
q(c\otimes v)_\rho&=\sum_{a,b}\rho_{ba}\bigl((cb\otimes v)_a\\
&\qquad+(c\otimes f_a(v))_b\bigr),\\
h(c\otimes v)_\rho&=(c\otimes h_\rho(v))_2 .
\end{aligned}
\]
Here \(p\colon L'_1\to L'_0\) and \(q\colon L'_2\to L'_1\) have degree \(0\), and \(h\colon L'_2\to L'_0\) has degree \(-1\). The terms make sense: for \(a\colon i\to j\) and \(c\in B\mathbf e_j\), the element \(ca\) lies in \(B\mathbf e_i\); for \(b\colon1\to2\) and \(c\in B\mathbf e_2\), \(cb\in B\mathbf e_1\), and \((cb\otimes v)_a\) lies in the summand \(B\mathbf e_1\otimes D_0\) of the arrow \(a\colon0\to1\).

**Lemma 1.1.** The maps \(p\) and \(q\) commute with the internal differentials, and \(pq(c\otimes v)_\rho=-(c\otimes f_\rho(v))_2\). Consequently the graded bimodule \(P=L'_0\oplus L'_1[1]\oplus L'_2[2]\) with the differential
\[
d_P=\begin{pmatrix}d_0&p&h\\0&-d_1&q\\0&0&d_2\end{pmatrix}
\]
is a bounded complex of finite-dimensional \(B\)-bimodules whose terms are projective as right \(B\)-modules.

**Proof.** The maps \(p\) and \(q\) commute with \(c\otimes v\mapsto c\otimes dv\) because the \(f_a\) are chain maps. Expanding,
\[
\begin{aligned}
&pq(c\otimes v)_\rho\\
&=\sum_{a,b}\rho_{ba}\bigl((cba\otimes v)_0-(cb\otimes f_a(v))_1\\
&\qquad+(cb\otimes f_a(v))_1-(c\otimes f_bf_a(v))_2\bigr),
\end{aligned}
\]
and \(\sum_{a,b}\rho_{ba}cba=c\rho=0\) in \(B\), so \(pq(c\otimes v)_\rho=-(c\otimes f_\rho(v))_2\).

In degree \(n\), \(P^n=(L'_0)^n\oplus(L'_1)^{n+1}\oplus(L'_2)^{n+2}\), and \(p,q,h\) raise the total degree by one; the diagonal entries are the differentials of \(L'_0\), \(L'_1[1]\) and \(L'_2[2]\). The square \(d_P^2\) has diagonal entries \(d_i^2=0\); its entries in positions \((0,1)\) and \((1,2)\) are \(d_0p-pd_1\) and \(-d_1q+qd_2\), which vanish; and its entry in position \((0,2)\) is
\[
d_0h+pq+hd_2 .
\]
On \((c\otimes v)_\rho\) this is \(\bigl(c\otimes(dh_\rho+h_\rho d)(v)\bigr)_2\) minus \((c\otimes f_\rho(v))_2\), which is zero by the defining equation \(dh_\rho+h_\rho d=f_\rho\) of the homotopies. So \(d_P^2=0\). As a right module, \(B\mathbf e_j\otimes D_i^n\) is a direct sum of \(\dim B\mathbf e_j\) copies of \(D_i^n\), which is finitely generated projective. There are finitely many summands and the \(D_i\) are bounded, so \(P\) is bounded with finite-dimensional terms. \(\square\)

The differential has only three columns because the relations have length two and live between vertices \(0\) and \(2\): there is no relation among relations, and no further coherence condition to satisfy.

## 2. The vertices and arrows of P

Since \(P\) is a complex of bimodules, \(\mathbf e_iP\) is a complex of right modules, and left multiplication by an arrow \(a\colon i\to j\) is a chain map \(\mathbf e_iP\to\mathbf e_jP\). Define
\[
\begin{gathered}
\iota_i\colon D_i\to\mathbf e_iP,\\
\iota_i(v)=(\mathbf e_i\otimes v)_i\in\mathbf e_iL'_0 .
\end{gathered}
\]
**Lemma 2.1.** Each \(\iota_i\) is a homotopy equivalence of complexes of right \(B\)-modules.

**Proof.** The map \(\iota_i\) is a chain map, since the differential of \(P\) restricted to \(L'_0\) is \(d_0\), and it is split injective in each degree. We show that its cokernel \(Q_i\) is acyclic. Say that a summand of \(L'_0\), \(L'_1\) or \(L'_2\) has *source index* \(l\) if its second tensor factor is \(D_l\); the summands of \(L'_2\) have source index \(0\). Let \(F^r\subseteq\mathbf e_iP\) be the sum of the summands with source index at least \(r\), for \(r=0,1,2,3\). Each \(F^r\) is a subcomplex: the internal differentials and the terms \(ca\), \(cb\) of \(p\) and \(q\) keep the source index, the terms \(f_a\) raise it, and \(h\) raises it from \(0\) to \(2\). So \(F^0=\mathbf e_iP\supseteq F^1\supseteq F^2\supseteq F^3=0\), and \(\iota_i(D_i)\subseteq F^i\). On each quotient \(F^l/F^{l+1}\), only the internal differentials and the path multiplications remain.

Recall that \(\mathbf e_iB\mathbf e_l\), the span of the paths from \(l\) to \(i\), is \(k\mathbf e_i\) for \(l=i\) and zero for \(l>i\). For \(l=i\), the quotient \(F^i/F^{i+1}\) is \(\iota_i(D_i)\): the summand \(\mathbf e_iB\mathbf e_i\otimes D_i\) of \(L'_0\), while the summands of \(L'_1\) with source index \(i\) involve \(\mathbf e_iB\mathbf e_j\) with \(j>i\) and vanish. For \(l>i\) the quotient is zero. For \(l<i\) with \(i=l+1\), it is the total complex of \(D_l\) tensored with
\[
\begin{gathered}
0\to k^{\{a\colon l\to i\}}\to\mathbf e_iB\mathbf e_l\to0,\\
(a)\mapsto a,
\end{gathered}
\]
placed in degrees \(-1\) and \(0\); this map is an isomorphism, because there are no relations of length one. For \((l,i)=(0,2)\), it is the total complex of \(D_0\) tensored with
\[
0\to k^{\mathcal R}\to k^{\{(b,a)\}}\to\mathbf e_2B\mathbf e_0\to0
\]
in degrees \(-2,-1,0\), where the basis vector of \(\rho\) maps to \(\sum_{a,b}\rho_{ba}(b,a)\) and \((b,a)\) maps to the path \(ba\). This sequence is exact: the first map is injective because \(\mathcal R\) is linearly independent; the kernel of the second map is the span of the relations, which is the image of the first map, because the relations of \(B\) span the part of the ideal between vertices \(0\) and \(2\); and the second map is surjective because the paths of length two span \(\mathbf e_2B\mathbf e_0\). The signs of the total complex match: the internal differential of \(L'_1[1]\) is \(-d_1\), the sign of the tensor product with a term in degree \(-1\).

An exact bounded complex of vector spaces is split exact, so its tensor product with \(D_l\) is contractible, in particular acyclic. Thus the quotients \(F^l/F^{l+1}\) of \(Q_i\) are acyclic for \(l\neq i\), and so are their counterparts in \(Q_i\), which has the induced filtration with \(F^i/F^{i+1}\) removed. By the long exact cohomology sequences of the filtration, \(Q_i\) is acyclic, and \(\iota_i\) is a quasi-isomorphism. Its cone is a bounded acyclic complex of projective right modules; such a complex is contractible (split the surjection onto the last nonzero term, which is projective, and continue downwards). A chain map whose cone is contractible is an isomorphism in the homotopy category, that is a homotopy equivalence ([Li, Volume 2, Corollary 4.1.13](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en), applied to the cone triangle). \(\square\)

**Lemma 2.2.** For every arrow \(a\colon i\to j\), the chain maps \(a\iota_i\) and \(\iota_jf_a\colon D_i\to\mathbf e_jP\) are homotopic.

**Proof.** Let \(H_a\colon D_i\to\mathbf e_jP\), \(H_a(v)=(\mathbf e_j\otimes v)_a\), placed in \(\mathbf e_jL'_1[1]\), a map of degree \(-1\). The differential of \(P\) applied to \((\mathbf e_j\otimes v)_a\) has the internal part \(-(\mathbf e_j\otimes dv)_a\), which cancels \(H_a(dv)\), and the part \(p(\mathbf e_j\otimes v)_a=(a\otimes v)_i-(\mathbf e_j\otimes f_a(v))_j\). So
\[
d_PH_a+H_ad=a\iota_i-\iota_jf_a .\qquad\square
\]

## 3. The realization theorem

**Theorem 3.1** (OpenAI). Let \(k\) be a field, \(R\) a finitely presented \(k\)-algebra, \(e\in R\) a central idempotent, \(\alpha\) an automorphism of \(R\), and \(H(Y)={}_\alpha(eY)\). The bounded complex \(P\) of finite-dimensional \(B\)-bimodules of Lemma 1.1, projective as right modules in each degree and chosen independently of \(Y\), satisfies, for every finite-dimensional left \(R\)-module \(Y\), the isomorphism (3.1)
\[
\begin{aligned}
P\otimes^{\mathbf L}_BM(Y)\simeq{}&M(H(Y))\\
&\oplus M(H(Y))[3]
\end{aligned}
\]
in the derived category \(\mathrm D(B)\) of left \(B\)-modules.

**Proof.** A bounded complex of right modules that are projective, hence flat, is K-flat, so derived tensor products with \(P\) and with the \(D_i\) are computed by ordinary tensor products (core course [Category Theory and Homological Methods](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D80); [Li, *Methods of Algebra*, Volume 2, Propositions 4.12.4 and 4.12.9](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)). Let \(T_Y=P\otimes_BM(Y)\), a bounded complex of finite-dimensional left \(B\)-modules, with \(\mathbf e_iT_Y=\mathbf e_iP\otimes_BM(Y)\). Tensoring the homotopy equivalences \(\iota_i\) and the homotopies \(H_a\) of Lemmas 2.1 and 2.2 with \(M(Y)\) shows that the diagram of vector space complexes \(\mathbf e_iT_Y\) with the maps given by the arrows is isomorphic, in \(\mathrm D^b(k)\), to the diagram \((D_i\otimes_BM(Y),f_a\otimes\mathrm{id})\). By Proposition 3.1 of [Clearing denominators in a finite diagram](clearing-denominators-in-a-finite-diagram.md), that diagram is isomorphic to the one with \(eY\oplus(eY)[3]\) at every vertex, identities for \(s,s'\) and \(\alpha(x_h)\) on both summands for \(a_h,a'_h\).

Cohomology is a functor on \(\mathrm D^b(k)\). Applying \(H^n\) to the isomorphism of diagrams shows that the \(B\)-module \(H^n(T_Y)\), whose vertex spaces are \(H^n(\mathbf e_iT_Y)\) and whose arrows act by the induced maps, is isomorphic to the \(B\)-module with \(H^n\bigl(eY\oplus(eY)[3]\bigr)\) at each vertex and the induced arrows. This is \(M(H(Y))\) for \(n=0\) and \(n=-3\), and zero otherwise; recall that \(H(Y)\) is \(eY\) with \(x_h\) acting as \(\alpha(x_h)\).

Write \(A_0=H^0(T_Y)\) and \(A_{-3}=H^{-3}(T_Y)\). The truncation triangle ([Li, Volume 2, Definition 3.9.3, Propositions 3.9.8 and 4.4.7](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)) of the complex \(T_Y\), whose cohomology lives in degrees \(-3\) and \(0\), reads
\[
A_{-3}[3]\to T_Y\to A_0\xrightarrow{\ \delta\ }A_{-3}[4].
\]
The connecting morphism \(\delta\) lies in \(\operatorname{Hom}_{\mathrm D(B)}(A_0,A_{-3}[4])=\operatorname{Ext}^4_B(A_0,A_{-3})\) ([Li, Volume 2, Definition 4.5.8](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)), which is zero: \(B\) has global dimension at most two by Proposition 2.2 of [Directed algebras and quadratic presentations](directed-algebras-and-quadratic-presentations.md), so \(\operatorname{pd}A_0\le3\) and \(\operatorname{Ext}^4_B(A_0,-)=0\) ([Li, Volume 2, Proposition 4.9.6](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)). A distinguished triangle with zero third morphism splits ([Li, Volume 2, Proposition 4.2.6](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)), so \(T_Y\simeq A_0\oplus A_{-3}[3]\), which is \(M(H(Y))\oplus M(H(Y))[3]\). \(\square\)

The splitting uses only that the two cohomology modules are three degrees apart while \(B\) has global dimension two; that is why the odd double of [A Verdier quotient and an odd double](a-verdier-quotient-and-an-odd-double.md) was taken with the shift three. The splitting is chosen for each \(Y\) separately; no naturality in \(Y\) is claimed or needed.

**Corollary 3.2.** Let \(\Phi=P\otimes^{\mathbf L}_B-\). For every \(j\ge0\) and every finite-dimensional left \(R\)-module \(Y\),
\[
\Phi^j(M(Y))\simeq\bigoplus_{q=0}^j\bigl(M(H^{\circ j}(Y))[3q]\bigr)^{\oplus\binom jq}.
\]
**Proof.** For \(j=0\) this is \(M(Y)\). If it holds for \(j\), apply \(\Phi\), which preserves isomorphisms, finite direct sums and shifts, and apply (3.1) to the finite-dimensional module \(H^{\circ j}(Y)\) in each summand: \(M(H^{\circ j}(Y))[3q]\) becomes the sum of \(M(H^{\circ(j+1)}(Y))[3q]\) and \(M(H^{\circ(j+1)}(Y))[3q+3]\). The multiplicities add up by Pascal's rule \(\binom jq+\binom j{q-1}=\binom{j+1}q\). \(\square\)

In particular, for the modules \(Y_m\) of [A selection process with unbounded extinction](a-selection-process-with-unbounded-extinction.md), \(\Phi^j(M(Y_m))\neq0\) for \(j<m\) and \(\Phi^m(M(Y_m))=0\).

## 4. Exercises

**Exercise 4.1** (easy). Check the sign of the \((1,2)\) entry of \(d_P^2\), namely that it is \(-d_1q+qd_2\), and that it vanishes.

**Exercise 4.2** (medium). Suppose all homotopies \(h_\rho\) are zero, so the \(f_a\) satisfy the relations of \(B\) strictly. Show that \(P\) is then the total complex of a complex of bimodule complexes \(L'_2\to L'_1\to L'_0\), and that \(\mathbf e_iP\) is homotopy equivalent to \(D_i\) by Lemma 2.1.

**Exercise 4.3** (medium). Show that a bounded acyclic complex of projective modules is contractible.

**Exercise 4.4** (easy). Compute the total dimension of \(\Phi^j(M(Y))\), the sum over all degrees of the dimensions of the cohomology, in terms of \(\dim H^{\circ j}(Y)\).

## 5. Solutions

**4.1.** The \((1,2)\) entry of \(d_P^2\) is the second row of \(d_P\) times its third column: \(0\cdot h+(-d_1)q+q\,d_2\). Since \(q\) commutes with the internal differentials, \(qd_2=d_1q\), and the entry vanishes.

**4.2.** With \(h=0\), the matrix of \(d_P\) is upper triangular with entries \(d_0,-d_1,d_2\) on the diagonal and \(p,q\) above it, and \(pq=-(c\otimes f_\rho)_2=0\) because \(f_\rho=0\). So \(L'_2\xrightarrow qL'_1\xrightarrow pL'_0\) is a complex of complexes, and \(P\) is its total complex with the sign convention of the shifts. Lemma 2.1 does not use the homotopies.

**4.3.** Let \(C\) be bounded acyclic with projective terms, and let \(n\) be its largest nonzero degree. The map \(d\colon C^{n-1}\to C^n\) is surjective onto a projective module, so it splits: \(C^{n-1}=C'\oplus\ker d\) with \(d\) an isomorphism on \(C'\). Then \(C\) is the direct sum of the contractible complex \(C'\to C^n\) and a complex with top term \(\ker d\) in degree \(n-1\), again bounded, acyclic, with projective terms (\(\ker d\) is a direct summand of \(C^{n-1}\)). Induction on the length concludes.

**4.4.** By Corollary 3.2 the cohomology is the sum of \(\sum_q\binom jq=2^j\) copies of \(M(H^{\circ j}(Y))\), whose dimension is \(3\dim H^{\circ j}(Y)\). The total dimension is \(3\cdot2^j\dim H^{\circ j}(Y)\).

## References

- [OpenAI-FD] OpenAI, *An algebra of infinite little finitistic dimension*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026
- [Keller] B. Keller, *Bimodule complexes via strong homotopy actions*, Algebras and Representation Theory 3 (2000); arXiv:math/9910178. https://arxiv.org/abs/math/9910178
- [Li] W.-W. Li, *Methods of Algebra*, Volume 2, English edition. https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en
