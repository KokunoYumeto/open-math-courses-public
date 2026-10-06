# Raikov's theorem and the Gelfand–Raikov theorem

**Lesson HA-LCA-05.** Self-checked by the writing AI.

Weak-star convergence tests a function through integrals. Compact convergence tests all its values on a compact set at once. For positive-type functions normalized at the identity, these two kinds of convergence coincide. This lets the extreme-point approximation from the preceding lesson detect individual group elements.

Let \(G\) be any locally compact Hausdorff group, with the full completed, locally determined left Haar domain and the modular convention of [the general Haar reading](../prerequisites/src/nonabelian-haar-integration.md). Let \(P_1(G)\) and \(P_0(G)\) have the meanings in [the positive-type lesson](functions-of-positive-type.md#ha-lca-04-theorem-4-3). Point values always mean the unique continuous representatives proved there. We use arbitrary nets, with no countability assumption on \(G\) or on the Hilbert spaces.

The free source readings are B. Bekka, P. de la Harpe and A. Valette's [author draft of 23 February 2007](https://perso.univ-rennes1.fr/bachir.bekka/KazhdanTotal.pdf), C.5.6–C.5.9 and C.6.10; D. H. Fremlin's [*Measure Theory*, §244, version of 6 March 2009 in the volume 2 source collection of 2016](https://www1.essex.ac.uk/maths/people/fremlin/mt2.2016/mt244.tex), 244D–F, 244H(a), 244P(a)–(b); and Paul D. Nelson's [*Representations of Lie Groups*, ETH Zürich, 15 July 2019](https://metaphor.ethz.ch/x/2019/fs/401-3226-01L/ex/notes-repn.pdf), §§3.8–3.9 and §§4.7–4.8. The proof below supplies the required compact-group results without a separability hypothesis or an unproved compact-operator spectral theorem.

This adapted component is distributed under the [Design Science License](../assets/fremlin/DESIGN-SCIENCE-LICENSE.txt). Fremlin's original volume 2 source package, with its notices, is retained unchanged. The other sources' prose and figures are not reproduced.

## 1. Convolution turns integral tests into uniform control

Write \(\langle f,q\rangle=\int_G f q\,d\mu\), bilinear in the complex variables. The earlier [full-domain duality theorem](../prerequisites/src/dual-balls-and-compact-convexity.md#ha-lca-pre-dual-convex-theorem-1-2) identifies \(L^\infty(G)\) with \((L^1(G))^*\) under this pairing.

<a id="ha-lca-05-lemma-1-1"></a>
### Lemma 1.1. Uniformity on norm-compact sets of tests

On any norm-bounded subset \(B\) of the dual \(E^*\) of a normed space \(E\), the weak-star topology equals the topology of uniform convergence on norm-compact subsets of \(E\).

**Proof.** Suppose \(\|\ell\|\le M\) on \(B\). For a norm-compact \(C\subset E\) and \(\delta>0\), finitely many balls of radius \(\delta\), centred at \(x_1,\ldots,x_n\in C\), cover \(C\), by its defining open-cover compactness. For \(\ell,\ell_0\in B\) and \(x\in C\), choose \(j\) with \(\|x-x_j\|<\delta\). Then
\[
 |(\ell-\ell_0)(x)|
 \le |(\ell-\ell_0)(x_j)|+2M\delta.
\]
Given \(\varepsilon>0\), choose \(\delta\) with \(2M\delta<\varepsilon/2\) when \(M>0\), and impose the finitely many weak-star conditions
\(|(\ell-\ell_0)(x_j)|<\varepsilon/2\). They ensure
\(\sup_C|(\ell-\ell_0)(x)|<\varepsilon\). If \(M=0\), every functional is zero and the assertion is immediate. Conversely each singleton \(\{x\}\) is norm-compact, so uniform convergence on compact test sets includes every evaluation required for weak-star convergence. These neighbourhood comparisons prove equality of the two topologies, and hence the statement for arbitrary nets. \(\square\)

<a id="ha-lca-05-lemma-1-2"></a>
### Lemma 1.2. Smoothing bounded weak-star families

For \(f\in L^1(G)\), \(q\in L^\infty(G)\), define
\[
 A_fq(x)=\int_G f(y)q(y^{-1}x)\,d\mu(y).
\]
This is a well-defined bounded continuous function, independent of the representatives, with
\(\|A_fq\|_\infty\le\|f\|_1\|q\|_\infty\).
On each norm-bounded subset of \(L^\infty\), the map \(q\mapsto A_fq\) is continuous from the weak-star topology to uniform convergence on compact subsets of \(G\).

**Proof.** Inversion and right translation preserve the full Haar domain and its null sets by the earlier [modular substitution theorem](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-theorem-4-1). Thus, for each fixed \(x\), the integrand is measurable, and changing \(q\) on a null set changes it only on a null set. It is absolutely integrable with the asserted bound; changes in the representative of \(f\) also have no effect.

Put \(t=y^{-1}x\), or \(y=xt^{-1}\). Left invariance and the inversion formula give
\[
 A_fq(x)=\int_G k_x(t)q(t)\,d\mu(t),\qquad
 k_x(t)=\Delta(t)^{-1}f(xt^{-1})
       =\overline{(L_{x^{-1}}f)^*(t)}.                 \tag{1}
\]
In particular \(\|k_x\|_1=\|f\|_1\), because left translation, the modular star and complex conjugation all preserve the \(L^1\) norm. The exact earlier [translation-continuity theorem](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-proposition-5-2) implies that \(x\mapsto k_x\) is norm-continuous. Pairing with \(q\) proves continuity of \(A_fq\).

For compact \(K\subset G\), its continuous image \(\{k_x:x\in K\}\) is norm-compact in \(L^1\). Lemma 1.1 says that weak-star convergence of a bounded family is uniform on this set of tests. Equation (1) therefore gives uniform convergence of \(A_fq\) on \(K\). The neighbourhood proof in that lemma also gives the stated topological continuity directly. \(\square\)

<a id="ha-lca-05-lemma-1-3"></a>
### Lemma 1.3. A common smoothing error near a normalized function

If \(u\in L^1(G)\), \(u\ge0\), \(\int u=1\), and \(\psi\in P_1(G)\), then
\[
 \|A_u\psi-\psi\|_\infty
       \le\sqrt{\,2\bigl(1-\operatorname{Re}\langle u,\psi\rangle\bigr)}.
                                                               \tag{2}
\]
For every \(\varphi\in P_1(G)\) and \(\eta>0\), one can choose such a \(u\) in \(C_c(G)\) so that this bound is less than \(\eta\) for all \(\psi\) in a weak-star neighbourhood of \(\varphi\) in \(P_1(G)\).

**Proof.** The [right difference inequality](functions-of-positive-type.md#ha-lca-04-lemma-3-3), with its two arguments \(y^{-1}x\) and \(x\), gives
\[
 |\psi(y^{-1}x)-\psi(x)|\le\sqrt{2(1-\operatorname{Re}\psi(y))}.
\]
Indeed their ordered product in that inequality is
\(x(y^{-1}x)^{-1}=y\). Integrate with the nonnegative weight \(u\). The earlier [Cauchy–Schwarz inequality](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-lemma-1-1), applied to \(\sqrt u\) and
\(\sqrt{2u(1-\operatorname{Re}\psi)}\), yields (2), since \(\int u=1\). Both functions belong to \(L^2\), as \(|\psi|\le1\), and the bound is independent of \(x\).

Choose \(\delta>0\) with \(2\sqrt\delta<\eta\). Continuity at \(e\) and \(\varphi(e)=1\) give a neighbourhood \(V\) where
\(|1-\varphi(y)|<\delta\). The proved [compact-cutoff and full-support construction](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-corollary-6-2) supplies nonnegative \(u\in C_c(G)\) supported there with integral one. Thus
\(1-\operatorname{Re}\langle u,\varphi\rangle<\delta\).
The weak-star condition
\(|\langle u,\psi-\varphi\rangle|<\delta\)
implies \(1-\operatorname{Re}\langle u,\psi\rangle<2\delta\). Equation (2) is then bounded by \(2\sqrt\delta<\eta\), as required. \(\square\)

## 2. Raikov's theorem

<a id="ha-lca-05-theorem-2-1"></a>
### Theorem 2.1. Weak-star and compact convergence on \(P_1\)

On \(P_1(G)\), the weak-star topology and the topology of uniform convergence on compact subsets of \(G\) coincide.

**Proof.** First consider compact convergence. Every member of \(P_1\) has uniform norm one. Given \(f\in L^1\) and \(\varepsilon>0\), choose a compact \(K\) such that
\(\int_{G\setminus K}|f|<\varepsilon\). To justify this compact-tail step, the earlier [\(C_c\) density theorem](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-lemma-5-1) gives \(h\in C_c\) with \(\|f-h\|_1<\varepsilon\); take \(K=\operatorname{supp}h\). For \(\psi,\varphi\in P_1\),
\[
 |\langle f,\psi-\varphi\rangle|
 \le\|f\|_1\sup_K|\psi-\varphi|
                         +2\int_{G\setminus K}|f|.     \tag{3}
\]
By first reducing the tail and then imposing a sufficiently small compact-uniform bound, this makes the pairing difference arbitrarily small. The same reasoning for each of finitely many tests gives a compact-convergence neighbourhood inside every weak-star neighbourhood. The zero test \(f=0\) needs no condition.

For the reverse inclusion, fix \(\varphi\in P_1\), a compact \(K\), and \(\varepsilon>0\). Lemma 1.3 supplies a normalized \(u\in C_c\) and a weak-star neighbourhood \(W_1\) of \(\varphi\) in \(P_1\) on which
\(\|A_u\psi-\psi\|_\infty<\varepsilon/3\). This also holds for \(\varphi\). By Lemma 1.2 there is a weak-star neighbourhood \(W_2\) of \(\varphi\) in \(P_1\) on which
\(\sup_K|A_u\psi-A_u\varphi|<\varepsilon/3\).
For \(\psi\in W_1\cap W_2\),
\[
 \sup_K|\psi-\varphi|
 \le\|\psi-A_u\psi\|_\infty
     +\sup_K|A_u\psi-A_u\varphi|
     +\|A_u\varphi-\varphi\|_\infty<\varepsilon.
\]
Thus every compact-convergence neighbourhood contains a weak-star neighbourhood. This proves equality of topologies, and therefore covers nets as well as sequences. \(\square\)

## 3. Compactly supported positive-type functions are sufficient

For \(1\le p<\infty\), let \(L^p(G)\) be the measurable classes with
\(\|f\|_p=(\int|f|^p)^{1/p}<\infty\). To make the density assertion below valid for the entire range of \(p\), we first prove the norm and approximation facts it uses.

<a id="ha-lca-05-lemma-3-0"></a>
### Lemma 3.0. Norms and \(C_c\) density for every finite \(p\)

The displayed expression is a norm on the complex space \(L^p(G)\). Finite linear combinations of indicators of finite-measure sets are dense in this norm, and \(C_c(G)\) is dense in \(L^p(G)\), for every \(1\le p<\infty\).

**Proof.** The case \(p=1\) has the earlier [\(L^1\) norm and simple-density proofs](../prerequisites/src/integration-and-l1.md#ha-lca-pre-integral-lemma-2-1). Suppose \(p>1\), and put \(q=p/(p-1)\). For \(a,b\ge0\),
\[
 ab\le a^p/p+b^q/q.                                    \tag{4}
\]
For \(b=0\) this is immediate. For \(b>0\), the function \(t^p/p-bt\) decreases up to \(t=b^{1/(p-1)}\) and increases afterwards: its derivative is \(t^{p-1}-b\). The earlier [power, derivative and monotonicity results](../prerequisites/src/real-variable-calculations.md#ha-lca-pre-real-lemma-1-2) justify this on \((0,\infty)\), and continuity includes \(0\). Its minimum is \(-b^q/q\), proving (4).

For \(f\in L^p\), \(g\in L^q\) with nonzero norms, apply (4) to
\(|f|/\|f\|_p\) and \(|g|/\|g\|_q\) and integrate. It gives
\[
 \int|fg|\le\|f\|_p\|g\|_q.                             \tag{5}
\]
If either norm is zero, that function is zero almost everywhere by the earlier [zero-integral criterion](../prerequisites/src/integration-and-l1.md#ha-lca-pre-integral-corollary-1-3), so (5) still holds.

For \(f,g\in L^p\), the pointwise bound
\(|f+g|^p\le2^p(|f|^p+|g|^p)\) proves that \(h=f+g\) is in \(L^p\). Since \(|h|^{p-1}\in L^q\), (5) gives
\[
 \|h\|_p^p
 \le\int (|f|+|g|)|h|^{p-1}
 \le(\|f\|_p+\|g\|_p)\|h\|_p^{p-1}.
\]
Cancel the last power when \(\|h\|_p>0\); otherwise the triangle inequality is immediate. Homogeneity, positivity and definiteness on almost-everywhere classes follow from the integral and its zero criterion. This proves the norm assertion.

To prove simple density, choose a finite measurable representative of \(f\), modifying a null set if necessary; integrability of \(|f|^p\) makes it finite almost everywhere. The sets
\[
 E_n=\{1/n\le|f|\le n\}
\]
have measure at most \(n^p\|f\|_p^p\). The functions \(f1_{E_n}\) approach \(f\) in \(L^p\), since their \(p\)-th power errors tend pointwise to zero and are bounded by \(|f|^p\); apply the earlier [dominated convergence theorem](../prerequisites/src/integration-and-l1.md#ha-lca-pre-integral-theorem-2-2). On a fixed \(E_n\), subdivide the bounded square containing the real and imaginary parts of \(f\) into finitely many half-open rectangles of sufficiently small diameter, assigning one complex value to each inverse image. This gives a measurable simple function \(s\), zero outside \(E_n\), with
\[
 \|f1_{E_n}-s\|_p\le\sup_{E_n}|f-s|\,\mu(E_n)^{1/p}.
\]
A piece of measure zero causes no difficulty. Taking the rectangles small and then using the norm triangle inequality proves simple density, for \(p=1\) as well.

Finally let \(E\in\Sigma\) have finite measure. The earlier full-domain \(L^1\) density theorem gives nonnegative \(v\in C_c(G)\) arbitrarily close to \(1_E\) in \(L^1\). Put \(w=\min(v,1)\), still in \(C_c\). Pointwise clipping decreases the error from the values zero and one, so
\[
 \|w-1_E\|_p^p\le\|w-1_E\|_1\le\|v-1_E\|_1,
\]
because \(|w-1_E|\le1\). Thus each such indicator is an \(L^p\) limit of \(C_c\) functions. Approximate finitely many indicators in a simple function and use the proved triangle inequality; then use simple density. This proves \(C_c\) density on the full Haar domain without assuming sigma-finiteness. \(\square\)

<a id="ha-lca-05-proposition-3-1"></a>
### Proposition 3.1. Density of the span of compactly supported positive functions

Set
\[
 \mathcal S=\operatorname{span}_{\mathbb C}\big(C_c(G)\cap P(G)\big).
\]
Then \(f*\widetilde g\in\mathcal S\) for every \(f,g\in C_c(G)\), where
\(\widetilde g(x)=\overline{g(x^{-1})}\). In particular every convolution of two \(C_c\) functions belongs to \(\mathcal S\).

For every \(h\in C_c(G)\), there is a net \(s_U\in\mathcal S\) converging uniformly to \(h\), with the supports of \(h\) and all sufficiently late \(s_U\) in a single compact set. Hence \(\mathcal S\) is dense for the usual inductive limit topology of \(C_c(G)\), for its uniform norm, and in \(L^p(G)\) for every \(1\le p<\infty\).

**Proof.** The map \((f,g)\mapsto f*\widetilde g\) is linear in \(f\) and conjugate linear in \(g\). Expanding its diagonal expressions gives
\[
 f*\widetilde g
  =\frac14\sum_{k=0}^3 i^k
           (f+i^k g)*\widetilde{(f+i^k g)}.             \tag{6}
\]
Indeed the \(f*\widetilde g\) term has coefficient
\(\frac14\sum_k i^k i^{-k}=1\), whereas the diagonal terms have coefficient \(\frac14\sum_k i^k=0\), and the \(g*\widetilde f\) term has coefficient \(\frac14\sum_k i^{2k}=0\). Each diagonal convolution belongs to \(P(G)\) by [the autocorrelation proposition](functions-of-positive-type.md#ha-lca-04-proposition-2-2), and has compact support by the earlier [\(C_c\) convolution theorem](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-theorem-6-1). Thus (6) proves the first assertion. Since \(\widetilde{\widetilde g}=g\) and inversion preserves \(C_c\), it also proves the assertion about general \(C_c\) convolutions.

Take the two-sided \(C_c\) approximate identity \(u_U\) from [the earlier construction](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-corollary-6-2), and put \(s_U=h*u_U\). This belongs to \(\mathcal S\) by the preceding paragraph, and tends uniformly to \(h\) by the proved \(C_0\) approximation assertion. Fix a compact neighbourhood \(V\) of \(e\). On a tail, \(\operatorname{supp}u_U\subseteq V\), so
\[
 \operatorname{supp}s_U\subseteq
             (\operatorname{supp}h)V=:K.
\]
This set is compact and contains \(\operatorname{supp}h\). Consequently
\[
 \|s_U-h\|_p\le\mu(K)^{1/p}\|s_U-h\|_\infty\longrightarrow0. \tag{7}
\]
If \(h=0\), take \(s_U=0\) directly.

For clarity about the inductive limit assertion, for each compact \(K\) let \(C_K\) be the continuous functions supported there, with their uniform norm. Use the seminorm definition of the locally convex inductive limit topology on \(C_c\): it is generated by all seminorms \(p\) whose restrictions to every \(C_K\) are norm-continuous. Such continuity means \(p(f)\le c_K\|f\|_\infty\) on \(C_K\) for some finite \(c_K\): scale a norm ball on which \(p<1\). Conversely this bound gives continuity of the restriction. The generating seminorm balls and their finite intersections are convex neighbourhoods; the triangle inequality gives continuous addition, and
\[
 p(\lambda f-\lambda_0 f_0)
 \le|\lambda|p(f-f_0)+|\lambda-\lambda_0|p(f_0)
\]
gives continuous scalar multiplication. Each inclusion \(C_K\to C_c\) is continuous by the restriction bounds. The common-support convergence just proved therefore gives \(p(s_U-h)\to0\) for every defining seminorm. This proves the claimed inductive limit density.

Uniform density follows already from the construction. For \(L^p\), first approximate an arbitrary member by \(h\in C_c\) using Lemma 3.0, then approximate \(h\) by (7); the triangle inequality completes the proof. \(\square\)

## 4. Irreducible representations detect distinct elements

<a id="ha-lca-05-theorem-4-1"></a>
### Theorem 4.1. Gelfand–Raikov separation

For \(x\ne y\) in \(G\), there is a strongly continuous irreducible unitary representation \(\pi\) such that \(\pi(x)\ne\pi(y)\).

**Proof.** The earlier [compact-cutoff lemma](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-lemma-1-3) supplies an \(h\in C_c(G)\) with \(h(x)=1\), \(h(y)=0\): choose a relatively compact neighbourhood of \(x\) avoiding \(y\), then a cutoff equal to one at \(x\) and supported in that neighbourhood. By Proposition 3.1, choose \(s\in\mathcal S\) with \(\|s-h\|_\infty<1/4\). Then
\(|s(x)-s(y)|>1/2\).
In a finite expression \(s=\sum_j c_j\psi_j\), with \(\psi_j\in C_c\cap P\), at least one \(\psi_j\) must satisfy \(\psi_j(x)\ne\psi_j(y)\). Call it \(\psi\). It is nonzero, and the earlier [norm-at-identity theorem](functions-of-positive-type.md#ha-lca-04-corollary-3-2) gives \(\psi(e)>0\). Normalize \(\varphi=\psi/\psi(e)\in P_1\).

The earlier [extreme-point density theorem](functions-of-positive-type.md#ha-lca-04-theorem-4-3) gives a net of finite convex combinations of \(\operatorname{Ext}P_1\) converging weak-star to \(\varphi\). Each combination belongs to \(P_1\), so Theorem 2.1 upgrades this convergence to uniform convergence on compact sets, in particular on \(\{x,y\}\). Since \(\varphi(x)\ne\varphi(y)\), some such combination has different values at \(x,y\). At least one extreme function \(\omega\) in that finite combination therefore has \(\omega(x)\ne\omega(y)\). By the earlier [extreme-point characterization](functions-of-positive-type.md#ha-lca-04-theorem-4-1), its cyclic GNS representation \(\pi_\omega\) is irreducible. If \(\pi_\omega(x)=\pi_\omega(y)\), its coefficient at the cyclic vector would have equal values at those points, a contradiction. This representation proves the theorem. \(\square\)

<a id="ha-lca-05-corollary-4-2"></a>
### Corollary 4.2. Character separation and the map to the double dual

For an LCA group \(G\), continuous characters separate points. The canonical map
\[
 J:G\longrightarrow\widehat{\widehat G},\qquad
                  J(x)(\chi)=\chi(x)                  \tag{8}
\]
is a continuous injective homomorphism.

**Proof.** By [the abelian Schur conclusion](functions-of-positive-type.md#ha-lca-04-proposition-1-1), the irreducible representations given by Theorem 4.1 are one-dimensional continuous characters. This proves separation.

For fixed \(x\), evaluation \(\chi\mapsto\chi(x)\) is continuous in the compact-convergence topology on \(\widehat G\), since \(\{x\}\) is compact. It is a homomorphism in \(\chi\), so belongs to \(\widehat{\widehat G}\). Equation (8) also preserves the group law in \(x\), and separation proves injectivity.

For continuity, the earlier [joint-pairing theorem](characters-and-the-dual-group.md#ha-lca-02-proposition-1-4) says that \((x,\chi)\mapsto\chi(x)\) is continuous on \(G\times\widehat G\). Given compact \(C\subset\widehat G\) and \(\varepsilon>0\), joint continuity at each \((e,\chi)\) gives neighbourhoods \(U_\chi\) of \(e\) and \(V_\chi\) of \(\chi\) such that \(|\eta(a)-1|<\varepsilon\) for \(a\in U_\chi,\eta\in V_\chi\). Finitely many \(V_\chi\) cover \(C\). Their associated \(U_\chi\) have an intersection \(U\) on which
\(\sup_{\eta\in C}|J(a)(\eta)-1|<\varepsilon\).
This is continuity at the identity into the compact-convergence topology of the double dual, and the homomorphism law gives continuity everywhere. \(\square\)

## 5. Compact groups and the role of normalization

<a id="ha-lca-05-proposition-5-1"></a>
### Proposition 5.1. Peter–Weyl density in the compact case

If \(G\) is compact, every strongly continuous irreducible unitary representation is finite-dimensional. The complex linear span of the matrix coefficients of these irreducible representations is uniformly dense in \(C(G)\).

**Proof.** Keep the given Haar measure \(\mu\), and put \(M=\mu(G)\). It is finite on compact sets and positive on the nonempty open set \(G\), so \(0<M<\infty\). Let \(\pi\) be irreducible on \(\mathcal H\), and choose a unit vector \(u\). Define the bounded positive form
\[
 B(v,w)=\int_G
          \langle v,\pi(g)u\rangle\langle\pi(g)u,w\rangle\,d\mu(g).
\]
The integrand is continuous and has absolute value at most \(\|v\|\|w\|\), so \(|B(v,w)|\le M\|v\|\|w\|\). The earlier [bounded-form representation theorem](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-proposition-2-4) gives a positive operator \(T\), with \(B(v,w)=\langle Tv,w\rangle\) and \(\|T\|\le M\).
Left substitution \(g=ah\) gives
\(B(\pi(a)v,\pi(a)w)=B(v,w)\), hence \(T\) commutes with \(\pi\). Schur's lemma, already proved in [the preceding lesson's prerequisites](functions-of-positive-type.md#ha-lca-04-proposition-1-1), gives \(T=cI\), \(c\ge0\).
Moreover \(c>0\): the function \(g\mapsto|\langle u,\pi(g)u\rangle|^2\) is continuous and equals one at \(e\), so its integral \(B(u,u)=c\) is positive by full support of Haar measure.

We approximate \(T\) explicitly by finite-rank operators. The orbit \(\{\pi(g)u:g\in G\}\) is norm-compact, being a continuous image of \(G\). Given \(\delta>0\), choose finitely many orbit vectors \(u_1,\ldots,u_n\) such that every orbit vector lies within \(\delta\) of one of them. The open inverse images of these balls cover \(G\). Taking each open set minus its predecessors produces a finite Borel partition \(E_1,\ldots,E_n\) with
\(\|\pi(g)u-u_j\|<\delta\) on \(E_j\). Set
\[
 T_\delta v=\sum_{j=1}^n\mu(E_j)\langle v,u_j\rangle u_j.
\]
For unit vectors \(v,w\), subtracting the two scalar forms and inserting one intermediate product gives
\[
 |\langle(T-T_\delta)v,w\rangle|
 \le\sum_j\int_{E_j}
     \|\pi(g)u-u_j\|\,(\|\pi(g)u\|+\|u_j\|)\,d\mu(g)
 \le2M\delta.
\]
The earlier [operator norm characterization by pairings](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-proposition-2-4) therefore gives \(\|T-T_\delta\|\le2M\delta\).
Choose \(0<\delta<c/(2M)\), so \(2M\delta<c\). If \(\mathcal H\) had dimension greater than the finite span of the \(u_j\), a nonzero vector orthogonal to that span would exist: orthonormalize a basis of the span by the earlier [finite orthogonal expansion construction](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-theorem-4-2), and subtract its finite projection from a vector outside. Normalize the resulting vector to \(v\). Then \(T_\delta v=0\), whereas \(Tv=cv\), forcing \(\|T-T_\delta\|\ge c\), a contradiction. Thus \(\mathcal H\) is finite-dimensional.

Let \(\mathcal A\) be the span of coefficients of all finite-dimensional unitary representations. Any such representation is an orthogonal sum of irreducible ones: if it is reducible, split off a nonzero proper invariant subspace and its invariant orthogonal complement; induction on the finite dimension terminates. The cross terms between these summands vanish. Thus \(\mathcal A\) is also exactly the span of irreducible coefficients.

The space \(\mathcal A\) contains constants through the trivial representation. It is closed under complex conjugation and pointwise multiplication by the proved [conjugate and tensor representation constructions](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-proposition-7-3): the corresponding coefficients are conjugates and products, and the spaces remain finite-dimensional. Finally \(\mathcal A\) separates points. For \(x\ne y\), Theorem 4.1 gives an irreducible \(\pi\) with \(\pi(x)\ne\pi(y)\); it is finite-dimensional by the first part. Choose \(v\) with \(w=(\pi(x)-\pi(y))v\ne0\). The coefficient \(g\mapsto\langle\pi(g)v,w\rangle\) differs by \(\|w\|^2\) at \(x,y\). The complete earlier [complex Stone–Weierstrass theorem](../prerequisites/src/uniform-approximation.md#ha-lca-pre-approx-corollary-2-2) now applies to this unital, self-adjoint, point-separating algebra on compact \(G\), proving uniform density. \(\square\)

For comparison with a probability Haar measure, define the separate measure \(\nu=M^{-1}\mu\). Use subscripts to distinguish its averaged form, operator, finite-rank approximation and scalar from those for the given measure. Directly from their integral definitions,
\[
 B_\nu=M^{-1}B_\mu,\qquad T_\nu=M^{-1}T_\mu,\qquad
 T_{\nu,\delta}=M^{-1}T_{\mu,\delta},\qquad c_\nu=M^{-1}c_\mu.
\]
Thus \(2\delta<c_\nu\) is equivalent to \(2M\delta<c_\mu\). The proof above uses the original measure and retains all of its scale factors.

<a id="ha-lca-05-example-5-1"></a>
### Example 5.1. Explicit separation for a finite abelian group

In a finite abelian group, the separating character can be written directly from cyclic coordinates.

**Proof.** The earlier [finite cyclic decomposition theorem](fourier-analysis-on-finite-abelian-groups.md#ha-lca-01-theorem-1-2) gives
\(G\cong\prod_{j=1}^m\mathbb Z/n_j\mathbb Z\).
If \(x\ne y\), choose a coordinate \(j\) with \(x_j-y_j\not\equiv0\pmod{n_j}\). Then
\[
 \chi(z)=\exp(2\pi i z_j/n_j)
\]
is well-defined, since adding \(n_j\) to an integer representative multiplies the value by one. It is a homomorphism and is continuous on the finite discrete group. The earlier [circle-period calculation](fourier-analysis-on-finite-abelian-groups.md#ha-lca-01-lemma-0-1) gives
\(\chi(x)\ne\chi(y)\) precisely because that coordinate difference is not a multiple of \(n_j\). This is the explicit finite abelian instance of Theorem 4.1 and Proposition 5.1. \(\square\)

<a id="ha-lca-05-example-5-2"></a>
### Example 5.2. The theorem fails on \(P_0(\mathbb R)\)

The sequence
\[
 \chi_n(x)=e^{2\pi i n x},\qquad n=1,2,\ldots,
\]
converges weak-star to zero in \(P_0(\mathbb R)\), but does not converge uniformly to zero on any nonempty compact set.

**Proof.** Each \(\chi_n\) is a continuous character, so is in \(P_1\subset P_0\) by the preceding lesson. The earlier [real-dual identification](characters-and-the-dual-group.md#ha-lca-02-theorem-3-1) and [Fourier \(C_0\) theorem](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-corollary-2-2) imply that for every \(f\in L^1(\mathbb R)\),
\[
 \int_{\mathbb R}f(x)e^{2\pi i n x}\,dx=\widehat f(-n)\longrightarrow0.
\]
Indeed \(-n\) eventually leaves every compact subset of the real dual. This is exactly weak-star convergence to zero. But \(|\chi_n(x)|=1\) for every \(x\), so its supremum over any nonempty compact set is one for every \(n\). In particular all values at \(0\) remain one. The limit has lost the normalization at the identity and lies outside \(P_1\).

Compact convergence still implies weak-star convergence on \(P_0\), by the same estimate (3), since all its functions have norm at most one. Thus this example proves that the weak-star topology on \(P_0(\mathbb R)\) is strictly coarser. \(\square\)

## 6. Exercises with complete solutions

<a id="ha-lca-05-exercise-6-1"></a>
### Exercise 6.1. Compact convergence implies weak-star convergence

Give the implication for a net \(\varphi_d\to\varphi\) in \(P_1\), assuming uniform convergence on every compact set.

**Proof.** Fix \(f\in L^1\) and \(\varepsilon>0\). Choose a compact \(K\) with
\(\int_{G\setminus K}|f|<\varepsilon/4\), using the \(C_c\) approximation proved in Theorem 2.1. Since \(|\varphi_d|,|\varphi|\le1\), the integral difference over the complement has modulus less than \(\varepsilon/2\). On \(K\), choose a sufficiently late index with
\(\sup_K|\varphi_d-\varphi|<\varepsilon/(2(1+\|f\|_1))\).
Its contribution is less than \(\varepsilon/2\). The total pairing difference is therefore less than \(\varepsilon\). This works for every \(f\), which is weak-star convergence. \(\square\)

<a id="ha-lca-05-exercise-6-2"></a>
### Exercise 6.2. The polarization sign

Verify (6), including its complex coefficients, for an arbitrary nonabelian group.

**Proof.** Since tilde is conjugate linear,
\[
 (f+i^k g)*\widetilde{(f+i^k g)}
   =f*\widetilde f+i^{-k}f*\widetilde g
                 +i^k g*\widetilde f+g*\widetilde g.
\]
Multiply by \(i^k\) and sum for \(k=0,1,2,3\). The sums
\(\sum i^k\) and \(\sum i^{2k}\) are zero, while
\(\sum i^k i^{-k}=4\). Only \(4f*\widetilde g\) remains. Division by four proves (6). The computation used scalar distributivity and conjugate linearity; the order of the convolution factors was kept fixed throughout. \(\square\)

<a id="ha-lca-05-exercise-6-3"></a>
### Exercise 6.3. A direct integral check of the counterexample

Prove the weak-star convergence in Example 5.2 directly, without invoking the Fourier \(C_0\) theorem.

**Proof.** First let \(h\in C_c(\mathbb R)\), with support contained in \([-R,R]\), where \(R>0\). A continuous function on this compact interval is uniformly continuous by the earlier [compact uniformity lemma](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-lemma-1-6). Subdivide the interval into finitely many half-open intervals of sufficiently small length and replace \(h\) on each by its value at one point there. The resulting step function \(s=\sum_j c_j1_{[a_j,b_j)}\), zero outside \([-R,R]\), can be made arbitrarily close to \(h\) in \(L^1\), because the error is at most \(2R\) times the uniform oscillation bound. Endpoints have measure zero by the earlier real Haar calculation.

For each interval and each \(n\ne0\), the earlier [exponential integration rule](../prerequisites/src/real-variable-calculations.md#ha-lca-pre-real-lemma-1-3) gives
\[
 \int_{a_j}^{b_j}e^{2\pi i n x}\,dx
  =\frac{e^{2\pi i n b_j}-e^{2\pi i n a_j}}{2\pi i n},
 \qquad
 \left|\int_{a_j}^{b_j}e^{2\pi i n x}\,dx\right|
                         \le\frac1{\pi|n|}.
\]
Thus \(\int s\chi_n\to0\), since the sum is finite. The error from replacing \(h\) by \(s\) is at most \(\|h-s\|_1\), uniformly in \(n\), so \(\int h\chi_n\to0\).

For general \(f\in L^1\), approximate it in \(L^1\) by such an \(h\), using the proved \(C_c\) density. The remaining integral error is at most \(\|f-h\|_1\), again uniformly in \(n\). Hence \(\int f\chi_n\to0\) for every \(f\). Finally \(\chi_n(0)=1\) excludes compact-uniform convergence to zero on \(\{0\}\). These two verified limits establish the required counterexample. \(\square\)

<a id="ha-lca-05-exercise-6-4"></a>
### Exercise 6.4. One-dimensional irreducibles characterize abelian groups

Show that if every strongly continuous irreducible unitary representation of a locally compact group is one-dimensional, the group is abelian.

**Proof.** For \(x,y\in G\), form the commutator \(c=xyx^{-1}y^{-1}\). In any one-dimensional representation \(\pi\), its scalar values commute, so
\[
 \pi(c)=\pi(x)\pi(y)\pi(x)^{-1}\pi(y)^{-1}=1=\pi(e).
\]
Under the assumption this holds for every irreducible representation. Theorem 4.1 then forces \(c=e\); otherwise some irreducible representation would distinguish them. Multiplying \(xyx^{-1}y^{-1}=e\) by \(y\) and then by \(x\) gives \(xy=yx\). Since \(x,y\) were arbitrary, \(G\) is abelian. The converse is already proved by [Schur's lemma for abelian groups](functions-of-positive-type.md#ha-lca-04-proposition-1-1), so this is a characterization. \(\square\)

## Source reading and exact proof scope

The free author draft's C.5.6 supplies the smoothing and normalization strategy; all modular substitutions and weak-star compact-test estimates are proved above. Its C.5.8–C.5.9 supply the route from extreme positive functions to irreducible separation. The density argument here uses actual \(C_c\) approximate identities and retains a common compact support, giving the asserted inductive limit and every finite-\(p\) conclusion.

Fremlin's norm and density arguments are supplied in the complex setting in Lemma 3.0, with the full Haar domain. Nelson's coefficient-algebra and compact-group results are reconstructed in Proposition 5.1 using finite approximation of an averaged rank-one form, the already proved Schur theorem and the already proved Stone–Weierstrass theorem. Every dependency has an exact earlier proof locator at its use. The map into the double dual is proved continuous and injective here; its surjectivity and topological inverse belong to the later duality lesson.
