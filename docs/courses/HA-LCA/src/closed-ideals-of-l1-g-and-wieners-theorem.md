# Closed ideals of \(L^1(G)\) and Wiener's theorem

**Lesson HA-LCA-14.** Self-checked by the writing AI.

A closed convolution ideal of \(L^1(G)\) is the whole algebra exactly when its Fourier transforms have no common zero. The word *closed* matters. We prove this for every locally compact Hausdorff abelian group, and then distinguish the pointwise nonvanishing condition for \(L^1\) approximation from the almost-everywhere condition for \(L^2\).

Write \(\Gamma=\widehat G\), with the dual Haar normalization of Plancherel. In this lesson both groups are written additively; thus
\((\gamma+\eta)(x)=\gamma(x)\eta(x)\) and \((-\gamma)(x)=\overline{\gamma(x)}\). We keep
\[
 \widehat f(\gamma)=\int_G f(x)\overline{\gamma(x)}\,dx,
 \qquad L_xf(y)=f(y-x).
\]
Let
\[
 A(\Gamma)=\{\widehat f:f\in L^1(G)\},\qquad
 \|\widehat f\|_A=\|f\|_1.
\]
This is a Banach algebra of continuous functions under pointwise multiplication: the Fourier laws, completeness and uniqueness are proved in [HA-LCA-03, Theorem 3.1](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-theorem-3-1), the [Haar convolution theorem](../prerequisites/src/haar-measure.md#ha-lca-pre-haar-theorem-6-2), and [HA-LCA-09, Corollary 4.2](the-pontryagin-duality-theorem.md#ha-lca-09-corollary-4-2). Translation on \(\Gamma\) corresponds to modulation \(f(x)\mapsto\eta(x)f(x)\), an isometry of \(L^1(G)\).

The free source for the local approximation and patching arguments is Ven-shion Shu, [*Wiener's Approximation Theorem for Locally Compact Abelian Groups*](https://digital.library.unt.edu/ark:/67531/metadc663188/m2/1/high_res_d/1002773742-Shu.pdf), university thesis, August 1974: Theorems 1.9–1.14, 2.2–2.10, 2.14–2.17 and 3.13–3.35. We supply the Fourier, measure and Banach-algebra inputs through exact earlier programme proofs and give the local reciprocal argument in full.

Written and checked by GPT-6 Astra (OpenAI), Ultra, October 2026. The new exposition is released under CC0. Separately linked prerequisite readings and their retained source packages keep their own licences.

## 1. Ideals and translates

For an ideal \(I\subseteq L^1(G)\) and a set \(N\subseteq\Gamma\), define the **hull** and **kernel**
\[
 \nu(I)=\{\gamma:\widehat f(\gamma)=0\text{ for all }f\in I\},
 \qquad
 \iota(N)=\{f:\widehat f|_N=0\}.                             \tag{1}
\]
An ideal here is a complex linear subspace closed under convolution with every member of \(L^1(G)\); it need not be closed or invariant under involution unless stated.

<a id="ha-lca-14-proposition-1-1"></a>
**Proposition 1.1 — Closed ideals are the closed invariant subspaces.** A norm-closed linear subspace \(M\subseteq L^1(G)\) is an ideal if and only if \(L_xM\subseteq M\) for every \(x\in G\). For \(f\in L^1(G)\),
\[
 \overline{\operatorname{span}\{L_xf:x\in G\}}
 =\overline{\{h*f:h\in L^1(G)\}}.                           \tag{2}
\]
The hull of any ideal is closed, and \(\iota(N)\) is a closed ideal containing every ideal whose hull contains \(N\).

**Proof.** Let \(\psi_U\) be the nonnegative mass-one approximate identities of [Haar Corollary 6.3](../prerequisites/src/haar-measure.md#ha-lca-pre-haar-corollary-6-3). If \(f\in M\) and \(M\) is an ideal, then
\((L_x\psi_U)*f\in M\), while
\[
 \|(L_x\psi_U)*f-L_xf\|_1=\|\psi_U*f-f\|_1\longrightarrow0.
\]
Thus \(L_xf\in M\).

Conversely, suppose \(M\) is translation invariant and \(f\in M\). For \(h\in C_c(G)\), approximate \(h*f\) by finite linear combinations of translates of \(f\). Indeed, norm continuity of \(x\mapsto L_xf\) gives a neighbourhood \(U\) with \(\|L_xf-f\|_1<\delta\) for \(x\in U\). Cover \(K=\operatorname{supp}h\) by finitely many \(x_j+U\), and disjointify their intersections with \(K\) into Borel sets \(E_j\). Set \(c_j=\int_{E_j}h\). The [norm-integral convolution formula](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-lemma-1-1) gives
\[
 \left\|h*f-\sum_jc_jL_{x_j}f\right\|_1
 \leq\sum_j\int_{E_j}|h(x)|\,\|L_xf-L_{x_j}f\|_1\,dx
 \leq\delta\|h\|_1.
\]
Thus \(h*f\in M\). Approximate arbitrary \(h\in L^1(G)\) by \(C_c(G)\); the convolution bound \(\|(h-h_n)*f\|_1\leq\|h-h_n\|_1\|f\|_1\) gives the conclusion.

The right side of (2) is a closed ideal by associativity and norm continuity. It contains \(f\), by the approximate identity, and hence every translate and their closed span. The preceding finite-translate approximation gives the reverse inclusion.

Each map \(f\mapsto\widehat f(\gamma)\) is a bounded multiplicative functional, and each \(\widehat f\) is continuous. Intersecting their kernels proves the claims about \(\iota(N)\) and \(\nu(I)\). The containment assertion is exactly their definitions. \(\square\)

## 2. Fourier plateaux

<a id="ha-lca-14-proposition-2-1"></a>
**Proposition 2.1 — Local units.** If \(K\subseteq\Gamma\) is compact and \(W\supseteq K\) is open, there is \(h\in L^1(G)\) such that
\[
 0\leq\widehat h\leq1,\qquad
 \widehat h=1\text{ on }K,\qquad
 \operatorname{supp}\widehat h\text{ is a compact subset of }W.
                                                                  \tag{3}
\]
In particular, \(\nu(\iota(N))=N\) for every closed \(N\subseteq\Gamma\).

**Proof.** If \(K=\varnothing\), take \(h=0\). Otherwise compactness and continuity of addition give a symmetric neighbourhood \(U\) of zero with \(K+U+U\subseteq W\). Here is the uniform neighbourhood argument. For each \(k\in K\), choose an open neighbourhood \(O_k\) of \(k\) and an identity neighbourhood \(T_k\) with \(O_k+T_k\subseteq W\). A finite subcover and the intersection of its \(T_k\)'s give \(K+T\subseteq W\). Choose symmetric \(U\) with \(U+U\subseteq T\). Local compactness supplies a compact symmetric neighbourhood \(V\subseteq U\). Its Haar measure \(m(V)\) is positive and finite.

Let \(p,q\in L^2(G)\) be the inverse Plancherel transforms of \(1_V\) and \(1_{K+V}\). Their product is integrable by Cauchy–Schwarz. The [\(L^2\) product formula](the-plancherel-theorem.md#ha-lca-08-theorem-3-1) gives, for \(h=pq/m(V)\),
\[
 \widehat h(\eta)=\frac{1}{m(V)}
       \int_\Gamma1_V(t)1_{K+V}(\eta-t)\,dm(t).             \tag{4}
\]
It is continuous by that same theorem. The integral lies between zero and \(m(V)\). If \(\eta\in K\), symmetry of \(V\) gives \(\eta-t\in K+V\) for every \(t\in V\), so (4) is one. It vanishes off the compact set \(K+V+V\subseteq W\), proving (3).

Always \(N\subseteq\nu(\iota(N))\). If \(\eta\notin N\), choose an open neighbourhood \(W\subseteq\Gamma\setminus N\) and apply (3) to \(K=\{\eta\}\). The resulting \(h\) lies in \(\iota(N)\) and has \(\widehat h(\eta)=1\), so \(\eta\) is outside its hull. This proves equality, including \(N=\varnothing\) and \(N=\Gamma\). \(\square\)

## 3. Compact Fourier supports approximate in norm

Write
\[
 \mathcal B=\{f\in L^1(G):\operatorname{supp}\widehat f
                                      \text{ is compact}\}.
\]
The Fourier laws show that this is an algebraic ideal: supports of sums lie in finite unions, and supports of products lie in intersections.

<a id="ha-lca-14-lemma-3-1"></a>
**Lemma 3.1 — Density and convolution approximation.** The ideal \(\mathcal B\) is dense in \(L^1(G)\). Given \(f\in L^1(G)\) and \(\varepsilon>0\), there is \(w\in\mathcal B\) with
\[
 \|f-f*w\|_1<\varepsilon.                                  \tag{5}
\]

**Proof.** Factor \(f=uv\), where \(u=|f|^{1/2}\) and
\(v=|f|^{1/2}\operatorname{sgn}f\), with value zero where \(f=0\).
Both factors lie in \(L^2(G)\). By the proved [Plancherel theorem](the-plancherel-theorem.md#ha-lca-08-theorem-1-1) and [\(C_c\)-density in \(L^2\)](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-proposition-6-2), choose \(\phi_n,\theta_n\in C_c(\Gamma)\) converging in \(L^2\) to \(\widehat u,\widehat v\). Let \(u_n,v_n\) be their inverse transforms. Then
\[
 \|uv-u_nv_n\|_1
 \leq\|u\|_2\|v-v_n\|_2+\|u-u_n\|_2\|v_n\|_2
 \longrightarrow0.
\]
Their products have Fourier transforms \(\phi_n*\theta_n\), supported in the compact set
\(\operatorname{supp}\phi_n+\operatorname{supp}\theta_n\).
Thus \(u_nv_n\in\mathcal B\), proving density.

If \(f=0\), take \(w=0\). Otherwise choose a positive approximate-identity member \(\psi\) with
\(\|f-f*\psi\|_1<\varepsilon/2\). Approximate \(\psi\) by \(w\in\mathcal B\) with
\(\|\psi-w\|_1<\varepsilon/(2\|f\|_1)\). The convolution bound and triangle inequality prove (5). The same construction works for finitely many \(f\)'s at once, by choosing a common sufficiently small approximate-identity member and a sufficiently accurate approximation to it. \(\square\)

## 4. A small convolution at a vanishing frequency

The next estimate controls the \(L^1\) norm, which pointwise smallness of a Fourier transform alone does not control.

<a id="ha-lca-14-lemma-4-0"></a>
**Lemma 4.0 — A narrow plateau with nearly invariant translates.** Given compact \(C\subseteq G\), an open neighbourhood \(O\) of zero in \(\Gamma\), and \(\delta>0\), there is \(h\in L^1(G)\) with
\[
 \|h\|_1<\sqrt2,\quad
 \widehat h=1\text{ near }0,\quad
 \operatorname{supp}\widehat h\Subset O,\quad
 \sup_{x\in C}\|L_xh-h\|_1<\delta.                          \tag{6}
\]
The notation \(\Subset O\) means a compact subset of \(O\).

**Proof.** Choose an identity neighbourhood \(D\subseteq\Gamma\) so small that \(D+D+D\subseteq O\) and
\[
 \sup_{\substack{x\in C\\\eta\in D}}|\eta(x)-1|
 <\frac{\delta}{4\sqrt2}.                                  \tag{7}
\]
The uniform bound follows directly from the compact-open topology of \(\Gamma\), proved in [HA-LCA-02, Proposition 1.1](characters-and-the-dual-group.md#ha-lca-02-proposition-1-1). Shrink \(D\) to be symmetric if necessary. Choose a compact symmetric identity neighbourhood \(S\subseteq D\). Haar measure gives \(0<m(S)<\infty\). We can choose an open set \(A\) containing \(S\), contained in \(D\), with \(m(A)<2m(S)\). To justify this outer approximation, place \(S\) in an open \(\sigma\)-compact subgroup and use the Radon restriction of Haar measure there, proved in [nonabelian Haar Theorem 3.1 and Lemma 5.1](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-theorem-3-1), then intersect the approximating open set with \(D\).

The compact-neighbourhood argument used in Proposition 2.1 supplies a compact symmetric identity neighbourhood \(T\) so small that \(S+T\subseteq A\). In particular
\[
 m(S+T)<2m(S),\qquad S+T\subseteq D.
\]
Let \(p=\mathcal F^{-1}1_S\), \(q=\mathcal F^{-1}1_{S+T}\), and \(h=pq/m(S)\). Formula (4), now with \(K=T\) and \(V=S\), proves
\[
 0\leq\widehat h\leq1,\quad \widehat h|_T=1,\quad
 \operatorname{supp}\widehat h\subseteq S+S+T\subseteq D+D\subseteq O.
\]
Also
\[
 \|h\|_1\leq\frac{\|p\|_2\|q\|_2}{m(S)}
       =\left(\frac{m(S+T)}{m(S)}\right)^{1/2}<\sqrt2.
\]
For \(x\in C\), the [Plancherel translation law](unitary-representations-of-abelian-groups-the-spectral-theorem.md#ha-lca-13-theorem-5-2) and (7) give
\[
 \|L_xp-p\|_2\leq a\|p\|_2,\qquad
 \|L_xq-q\|_2\leq a\|q\|_2,\qquad
 a=\delta/(4\sqrt2).
\]
Now
\[
 L_x(pq)-pq=(L_xp-p)L_xq+p(L_xq-q).
\]
Cauchy–Schwarz and translation invariance of \(L^2\) yield
\[
 \|L_xh-h\|_1
 \leq 2a\,\frac{\|p\|_2\|q\|_2}{m(S)}
 <2a\sqrt2=\delta/2<\delta.
\]
All choices were on compact sets or neighbourhoods; no countable base was used. \(\square\)

<a id="ha-lca-14-lemma-4-1"></a>
**Lemma 4.1 — The small-convolution estimate.** Suppose \(f\in L^1(G)\), \(\widehat f(\gamma_0)=0\), and \(\varepsilon>0\). In any prescribed neighbourhood \(O\) of \(\gamma_0\), one can choose \(h\in L^1(G)\) with
\[
 \widehat h=1\text{ near }\gamma_0,\quad
 \operatorname{supp}\widehat h\Subset O,\quad
 \|h\|_1<\sqrt2,\quad \|f*h\|_1<\varepsilon.                \tag{8}
\]

**Proof.** First let \(\gamma_0=0\), so \(\int f=0\). Choose a compact \(C\subseteq G\) with
\(\int_{G\setminus C}|f|<\varepsilon/(8\sqrt2)\).
Such compact tails follow from the finite Radon measure \(|f|\,dx\), proved in [HA-LCA-03, Lemma 4.1](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-lemma-4-1). Choose \(\delta>0\) with
\(\delta\|f\|_1<\varepsilon/2\), which is automatic for any positive \(\delta\) when \(f=0\). Apply Lemma 4.0 to obtain \(h\). The norm-integral convolution formula gives
\[
 f*h=\int_G f(x)(L_xh-h)\,dx,
\]
because \(\int f=0\). Hence
\[
 \|f*h\|_1
 \leq\delta\int_C|f|+2\|h\|_1\int_{G\setminus C}|f|
 <\varepsilon/2+\varepsilon/4<\varepsilon.                 \tag{9}
\]

For general \(\gamma_0\), put \(f_0(x)=\overline{\gamma_0(x)}f(x)\).
Then \(\int f_0=\widehat f(\gamma_0)=0\). Apply the first case with the spectral neighbourhood \(O-\gamma_0\), obtaining \(h_0\), and put \(h(x)=\gamma_0(x)h_0(x)\). The modulation law gives
\[
 \widehat h(\gamma)=\widehat h_0(\gamma-\gamma_0),\qquad
 f*h=\gamma_0(f_0*h_0).
\]
Multiplication by \(\gamma_0\) preserves the \(L^1\) norm. All the assertions follow. \(\square\)

<a id="ha-lca-14-corollary-4-2"></a>
**Corollary 4.2 — Removing a neighbourhood of a zero.** Under the vanishing hypothesis of Lemma 4.1, there is \(u\in L^1(G)\) with
\[
 \widehat u=0\text{ near }\gamma_0,\qquad
 \|f-f*u\|_1<\varepsilon.                                  \tag{10}
\]

**Proof.** Choose a positive approximate-identity member \(a\) with
\(\|f-f*a\|_1<\varepsilon/2\). The Fourier convolution law shows that \(f*a\) still vanishes at \(\gamma_0\). Apply Lemma 4.1 to \(f*a\) with error \(\varepsilon/2\), producing \(h\). Set \(u=a-a*h\). Then
\(\widehat u=\widehat a(1-\widehat h)=0\) near \(\gamma_0\), and
\[
 \|f-f*u\|_1
 \leq\|f-f*a\|_1+\|(f*a)*h\|_1<\varepsilon.
\]
Associativity is the earlier Banach convolution law. \(\square\)

<a id="ha-lca-14-corollary-4-3"></a>
**Corollary 4.3 — A small correction to a constant Fourier value.** For \(g\in L^1(G)\), \(\gamma_0\in\Gamma\) and \(\varepsilon>0\), there is \(v\in L^1(G)\) with
\[
 \|v\|_1<\varepsilon,\qquad
 \widehat g+\widehat v=\widehat g(\gamma_0)
                       \text{ near }\gamma_0.             \tag{11}
\]

**Proof.** Choose a compact neighbourhood \(K\) of \(\gamma_0\). Proposition 2.1 gives \(b\in L^1(G)\) with \(\widehat b=1\) on \(K\). Set \(c=\widehat g(\gamma_0)\) and \(a=cb-g\); then \(\widehat a(\gamma_0)=0\). Lemma 4.1 gives \(h\) with \(\|a*h\|_1<\varepsilon\) and \(\widehat h=1\) on a neighbourhood of \(\gamma_0\). Take \(v=a*h\). On the intersection of that neighbourhood with the interior of \(K\), one has
\(\widehat v=(c-\widehat g)\cdot1\). This proves (11). \(\square\)

## 5. Local division, patching and Wiener

Say that \(f\in L^1(G)\) is **locally in \(I\) at \(\gamma\)** if some \(a\in I\) has \(\widehat a=\widehat f\) on a neighbourhood of \(\gamma\).

<a id="ha-lca-14-lemma-5-1"></a>
**Lemma 5.1 — Local division.** If \(I\) is an ideal and \(\gamma_0\notin\nu(I)\), every \(f\in L^1(G)\) is locally in \(I\) at \(\gamma_0\). The ideal need not be closed.

**Proof.** Choose \(g\in I\) with \(c=\widehat g(\gamma_0)\ne0\). Corollary 4.3 supplies \(v\in L^1(G)\) with
\(\|v\|_1<|c|\) and \(\widehat g+\widehat v=c\) near \(\gamma_0\).
In the unitization \(L^1(G)^+\), write its identity as \(\delta\). The element
\[
 b=c\delta-v
\]
is invertible by the proved [Neumann-series lemma](../prerequisites/src/banach-spectrum.md#ha-lca-pre-banach-lemma-2-1):
\[
 b^{-1}=c^{-1}\sum_{n=0}^{\infty}(v/c)^{*\,n}.               \tag{12}
\]
The series converges in the unitization, whose construction is proved in [Banach Theorem 3.4](../prerequisites/src/banach-spectrum.md#ha-lca-pre-banach-theorem-3-4). The \(n=0\) term is \(\delta\). Every character \(\gamma\) extends with value one at \(\delta\); hence the transform of \(b^{-1}\) equals \(1/(c-\widehat v)\). In the chosen neighbourhood this is \(1/\widehat g\).

Set \(a=g*b^{-1}*f\). This is in \(I\): write \(b^{-1}=\alpha\delta+k\), with \(k\in L^1(G)\), and use \(g*f\in I\) and \((g*k)*f\in I\). This uses only the algebraic ideal property, not closedness or passage of an infinite series inside \(I\). Its Fourier transform agrees with \(\widehat f\) near \(\gamma_0\), proving the assertion. \(\square\)

<a id="ha-lca-14-lemma-5-2"></a>
**Lemma 5.2 — Finite patching.** Suppose \(f\in\mathcal B\) is locally in an ideal \(I\) at every point of \(\operatorname{supp}\widehat f\). Then \(f\in I\).

**Proof.** Put \(K=\operatorname{supp}\widehat f\). If \(K=\varnothing\), Fourier uniqueness gives \(f=0\in I\). Otherwise, for each \(\gamma\in K\), choose an open neighbourhood \(U_\gamma\) and \(a_\gamma\in I\) with
\(\widehat a_\gamma=\widehat f\) on \(U_\gamma\). Choose a compact neighbourhood of \(\gamma\) inside \(U_\gamma\), and use Proposition 2.1 to find \(b_\gamma\in L^1(G)\) whose transform is one on that compact neighbourhood and is supported in \(U_\gamma\). Finitely many of the interiors on which these transforms are one cover \(K\). Denote the corresponding data by \(U_j,a_j,b_j\), \(1\leq j\leq n\).

In the unitization set
\[
 r_1=b_1,\qquad
 r_j=b_j*(\delta-b_1)*\cdots*(\delta-b_{j-1})\quad(j\geq2).
\]
Each \(r_j\) belongs to \(L^1(G)\), because expansion of the finite product leaves a factor \(b_j\) in every term. Its transform is supported in \(U_j\). The elementary telescoping identity
\[
 \sum_{j=1}^n\widehat r_j
       =1-\prod_{j=1}^n(1-\widehat b_j)                    \tag{13}
\]
follows by subtracting successive partial products; it equals one on \(K\), since at least one \(\widehat b_j\) is one there. For every \(\eta\in\Gamma\), the support condition gives
\(\widehat r_j(\eta)\widehat a_j(\eta)
 =\widehat r_j(\eta)\widehat f(\eta)\).
Therefore
\[
 \left(\sum_jr_j*a_j\right)^{\widehat{\ }}=\widehat f
\]
on \(K\), by (13), and off \(K\), because \(\widehat f=0\) there. Fourier uniqueness proves \(f=\sum_jr_j*a_j\in I\). \(\square\)

<a id="ha-lca-14-theorem-5-3"></a>
**Theorem 5.3 — Wiener's theorem.** A closed ideal \(I\subseteq L^1(G)\) satisfies
\[
 I=L^1(G)\quad\Longleftrightarrow\quad\nu(I)=\varnothing.
                                                                  \tag{14}
\]

**Proof.** If \(\nu(I)=\varnothing\), Lemma 5.1 says that every \(f\in\mathcal B\) is locally in \(I\) at each point of its Fourier support. Lemma 5.2 gives \(\mathcal B\subseteq I\). By Lemma 3.1 this is a dense subspace of \(L^1(G)\), so closedness gives \(I=L^1(G)\). Conversely, for each \(\gamma\), Proposition 2.1 supplies \(h\) with \(\widehat h(\gamma)=1\). No point can belong to the hull of the whole algebra. \(\square\)

<a id="ha-lca-14-corollary-5-4"></a>
**Corollary 5.4 — Proper closed ideals lie in evaluation kernels.** Every proper closed ideal is contained in
\[
 \iota(\{\gamma_0\})
   =\{f:\widehat f(\gamma_0)=0\}
\]
for some \(\gamma_0\in\Gamma\). Each such kernel is a maximal proper ideal and is closed.

**Proof.** By Theorem 5.3 the hull of a proper closed ideal is nonempty; choose \(\gamma_0\) in it. The required inclusion is the definition of the hull. Evaluation at \(\gamma_0\) is a continuous algebra homomorphism onto \(\mathbb C\): it takes value one on a local unit from Proposition 2.1, and scaling gives every complex value. Its kernel is closed. Any strictly larger ideal has nonzero image in the field \(\mathbb C\), hence full image. Explicitly, if it contains \(g\) with \(\widehat g(\gamma_0)=1\), then for every \(f\),
\(f-\widehat f(\gamma_0)g\) is in the kernel, so \(f\) is in that larger ideal. Thus the kernel is maximal proper. \(\square\)

## 6. The compact case

<a id="ha-lca-14-proposition-6-1"></a>
**Proposition 6.1 — Closed ideals on a compact abelian group.** If \(G\) is compact, every closed ideal satisfies
\[
 I=\iota(\nu(I)).                                          \tag{15}
\]
Consequently the closed ideals are exactly the \(\iota(N)\), for subsets \(N\) of the discrete group \(\widehat G\).

**Proof.** Let \(M=m_G(G)>0\). Each character \(\gamma\), viewed as a function on \(G\), is integrable, and direct substitution in convolution gives
\[
 f*\gamma=\widehat f(\gamma)\gamma.                         \tag{16}
\]
If \(\gamma\notin\nu(I)\), choose \(f\in I\) with \(\widehat f(\gamma)\ne0\); then (16) implies \(\gamma\in I\).

We now approximate any \(g\in\iota(\nu(I))\) by finite sums of these allowed characters. Given \(\varepsilon>0\), choose a continuous positive approximate-identity member \(\psi\) with \(\|g-g*\psi\|_1<\varepsilon/2\). Finite character polynomials are uniformly dense in \(C(G)\): they form a self-adjoint algebra containing constants, separate points by [HA-LCA-05, Corollary 4.2](raikovs-theorem-and-the-gelfand-raikov-theorem.md#ha-lca-05-corollary-4-2), and hence satisfy the proved [complex Stone–Weierstrass theorem](../prerequisites/src/uniform-approximation.md#ha-lca-pre-approx-corollary-2-2). If \(g\ne0\), choose
\(q=\sum_{j=1}^n c_j\gamma_j\) with
\(\|\psi-q\|_\infty<\varepsilon/(2M\|g\|_1)\).
Then
\[
 g*q=\sum_jc_j\widehat g(\gamma_j)\gamma_j\in I:
\]
a term vanishes when \(\gamma_j\in\nu(I)\), and otherwise its character lies in \(I\). Also
\[
 \|g-g*q\|_1
 \leq\|g-g*\psi\|_1+\|g\|_1M\|\psi-q\|_\infty<\varepsilon.
\]
The case \(g=0\) is immediate. Closedness gives \(g\in I\). The reverse inclusion in (15) holds by definition.

The dual is discrete by [HA-LCA-02, Theorem 2.1](characters-and-the-dual-group.md#ha-lca-02-theorem-2-1), so every subset \(N\) is closed. Proposition 2.1 gives \(\nu(\iota(N))=N\), while Proposition 1.1 makes \(\iota(N)\) a closed ideal. This proves the classification without assuming the dual countable. \(\square\)

## 7. Approximation by translates

<a id="ha-lca-14-corollary-7-1"></a>
**Corollary 7.1 — Wiener's \(L^1\) approximation theorem.** For \(f\in L^1(G)\), the linear span of its translates is dense in \(L^1(G)\) if and only if \(\widehat f\) has no zero.

**Proof.** Let \(I\) be the closed span in (2), a closed ideal by Proposition 1.1. Its hull is exactly \(\{\gamma:\widehat f(\gamma)=0\}\). Indeed, every translated transform is
\(\overline{\gamma(x)}\widehat f(\gamma)\), so each zero annihilates the span and its norm closure. Conversely \(f=L_0f\in I\), so a point in the hull must be a zero of \(\widehat f\). The conclusion is now (14). \(\square\)

<a id="ha-lca-14-proposition-7-2"></a>
**Proposition 7.2 — The \(L^2\) criterion.** For \(f\in L^2(G)\), its translates span a dense subspace of \(L^2(G)\) if and only if its Plancherel transform is nonzero almost everywhere on \(\Gamma\).

**Proof.** A subspace is dense exactly when its orthogonal complement is zero, by the [Hilbert projection theorem](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-corollary-2-2). Suppose \(g\) is orthogonal to every \(L_xf\). The [Plancherel translation identity](unitary-representations-of-abelian-groups-the-spectral-theorem.md#ha-lca-13-theorem-5-2) gives
\[
 0=\langle L_xf,g\rangle
   =\int_\Gamma\overline{\gamma(x)}
            \widehat f(\gamma)\overline{\widehat g(\gamma)}\,dm(\gamma)
 \quad(x\in G).                                           \tag{17}
\]
The product \(w=\widehat f\,\overline{\widehat g}\) is in \(L^1(\Gamma)\) by Cauchy–Schwarz. Formula (17) is its Fourier transform evaluated at the character
\(\gamma\mapsto\gamma(x)\). Pontryagin duality says these are all characters of \(\Gamma\); Fourier uniqueness therefore gives \(w=0\) almost everywhere. If \(\widehat f\ne0\) almost everywhere, \(\widehat g=0\) almost everywhere, so \(g=0\) by Plancherel. This proves sufficiency.

If the zero set \(Z=\{\widehat f=0\}\) has positive full Haar measure, [dual-convex Lemma 1.1](../prerequisites/src/dual-balls-and-compact-convexity.md#ha-lca-pre-dual-convex-lemma-1-1) supplies a measurable \(E\subseteq Z\) with \(0<m(E)<\infty\), by intersecting with a positive finite piece. Let \(g=\mathcal F^{-1}1_E\). Then \(g\ne0\), but (17) is zero for every \(x\), proving failure of density. This argument also covers non-\(\sigma\)-finite Haar measure. \(\square\)

## 8. Examples and the role of closedness

<a id="ha-lca-14-example-8-1"></a>
**Example 8.1 — A zero matters differently in \(L^1\) and \(L^2\).** On \(\mathbb R\), translates of \(e^{-x^2}\) are dense in both \(L^1\) and \(L^2\). Translates of \(1_{[-1,1]}\) are dense in \(L^2\) but not in \(L^1\).

**Proof.** The complete scalar calculations in [HA-LCA-03, Example 5.2](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-example-5-2) give
\[
 \widehat{e^{-x^2}}(\xi)=\sqrt\pi\,e^{-\pi^2\xi^2},\qquad
 \widehat{1_{[-1,1]}}(\xi)=
 \begin{cases}
  \sin(2\pi\xi)/(\pi\xi),&\xi\ne0,\\
  2,&\xi=0.
 \end{cases}                                               \tag{18}
\]
The Gaussian transform is everywhere positive. The interval transform has zeros exactly at \(k/2\), \(k\in\mathbb Z\setminus\{0\}\). This nonempty countable set has Lebesgue measure zero: each singleton has measure zero by the interval-length construction in [HA-LCA-02, Lemma 3.3](characters-and-the-dual-group.md#ha-lca-02-lemma-3-3), and countable subadditivity applies. Both original functions lie in \(L^1\cap L^2\). Apply Corollary 7.1 and Proposition 7.2. \(\square\)

<a id="ha-lca-14-example-8-2"></a>
**Example 8.2 — A proper dense ideal with empty hull.** If \(G\) is nondiscrete, \(\mathcal B\) is a proper dense algebraic ideal with empty hull. If \(G\) is discrete, \(\mathcal B=L^1(G)\).

**Proof.** Its ideal property and density were proved in §3. Proposition 2.1 supplies a member with value one at each prescribed spectral point, so its hull is empty.

If \(G\) is nondiscrete, \(\Gamma\) is noncompact by [HA-LCA-09, Corollary 4.4](the-pontryagin-duality-theorem.md#ha-lca-09-corollary-4-4). Choose a compact identity neighbourhood \(V\subseteq\Gamma\). Inductively select \(\eta_n\) outside
\(\bigcup_{j<n}(\eta_j+V-V)\), a compact set which cannot equal \(\Gamma\). No compact subset contains infinitely many \(\eta_n\): it is covered by finitely many translates of \(\operatorname{int}V\), and each such translate contains at most one \(\eta_n\), since two would have difference in \(V-V\).

Choose \(b\in L^1(G)\) with compactly supported \(\beta=\widehat b\), \(0\leq\beta\leq1\), and \(\beta(0)=1\), by Proposition 2.1. The norm-convergent series
\[
 f(x)=\sum_{n=1}^{\infty}2^{-n}\eta_n(x)b(x)
\]
defines an element of \(L^1(G)\): the norms of its summands sum to \(\|b\|_1\), and \(L^1\) is complete. Fourier continuity gives a uniformly convergent transform series
\[
 \widehat f(\gamma)=\sum_{n=1}^{\infty}2^{-n}\beta(\gamma-\eta_n).
\]
All terms are nonnegative, so \(\widehat f(\eta_n)\geq2^{-n}>0\). A compact Fourier support would contain all \(\eta_n\), which is impossible. Thus \(f\notin\mathcal B\), proving properness. In particular \(\mathcal B\) is not closed, and it lies in no point-evaluation kernel.

If \(G\) is discrete, \(\Gamma\) is compact by the same compact/discrete duality theorem. Every Fourier support is a closed subset of this compact space, so every \(L^1\) function belongs to \(\mathcal B\). \(\square\)

## 9. Exercises with complete solutions

<a id="ha-lca-14-exercise-9-1"></a>
**Exercise 9.1 — Hull and kernel.** Show that \(\iota(N)\) is a closed ideal, and determine its hull for arbitrary \(N\subseteq\Gamma\).

**Solution.** For fixed \(\gamma\), the bound
\(|\widehat f(\gamma)|\leq\|f\|_1\) makes evaluation continuous; its kernel is closed and linear. The product law \(\widehat{f*g}=\widehat f\,\widehat g\) makes this kernel an ideal. Their intersection over \(\gamma\in N\) is exactly \(\iota(N)\), so it is a closed ideal. Continuity of every \(\widehat f\) gives
\(\iota(N)=\iota(\overline N)\). Proposition 2.1 supplies, for every \(\eta\notin\overline N\), a compactly supported Fourier plateau equal to one at \(\eta\) and zero on \(\overline N\). Thus
\[
 \nu(\iota(N))=\overline N.
\]
In particular the hull is \(N\) when \(N\) is closed. \(\square\)

<a id="ha-lca-14-exercise-9-2"></a>
**Exercise 9.2 — Recover a compact-group ideal from its hull.** Prove the compact-group classification, allowing an uncountable dual, and describe the ideal's dense spanning family.

**Solution.** Let \(N=\nu(I)\). Formula (16) shows that every character \(\gamma\notin N\) lies in \(I\). If \(g\in\iota(N)\), choose a positive continuous approximate identity \(\psi\) adapted to \(g\), and approximate \(\psi\) uniformly by a finite character polynomial \(q=\sum c_\gamma\gamma\), as in Proposition 6.1. Then
\[
 g*q=\sum_\gamma c_\gamma\widehat g(\gamma)\gamma
\]
is a finite sum of characters outside \(N\), since all coefficients from \(N\) vanish. The explicit error bound there makes these sums approximate \(g\) in \(L^1\). Therefore
\[
 I=\iota(N)
   =\overline{\operatorname{span}\{\gamma:\gamma\notin N\}}^{\,L^1}.
\]
Every approximation uses a finite family selected for its requested accuracy; no enumeration of the entire dual is used. Conversely each subset \(N\) of the discrete dual has exactly that hull, by Proposition 2.1. \(\square\)

<a id="ha-lca-14-exercise-9-3"></a>
**Exercise 9.3 — Why closure cannot be omitted.** On \(\mathbb R\), show that \(\mathcal B\) is a proper ideal contained in no point-evaluation kernel.

**Solution.** If \(\widehat f\) and \(\widehat g\) have compact supports, their sum is supported in the union. If only \(\widehat f\) has compact support and \(h\in L^1\) is arbitrary, \(\widehat{f*h}=\widehat f\,\widehat h\) is supported there. Thus \(\mathcal B\) is an ideal. Local units show that for each \(\xi_0\) some member has transform equal to one at \(\xi_0\), so no point-evaluation kernel contains it. The Gaussian belongs to \(L^1(\mathbb R)\), but (18) is nonzero on all of \(\mathbb R\); its Fourier support is not compact. Hence \(\mathcal B\) is proper. Lemma 3.1 shows that it is dense, and therefore not closed. It satisfies the empty-hull hypothesis of Wiener while failing its closedness hypothesis, which explains the different conclusion. \(\square\)

<a id="ha-lca-14-exercise-9-4"></a>
**Exercise 9.4 — Wiener's lemma for absolutely convergent series.** Suppose \(a\in\ell^1(\mathbb Z)\) and
\[
 \widehat a(t)=\sum_{n\in\mathbb Z}a_n e^{-2\pi int}
\]
has no zero on \(\mathbb T\). Prove that \(1/\widehat a\) is another absolutely convergent Fourier series.

**Solution.** Counting Haar measure makes \(L^1(\mathbb Z)=\ell^1(\mathbb Z)\), with convolution identity \(\delta_0\). By Corollary 7.1 and (2), the principal convolution ideal generated by \(a\) is dense. Choose \(b\in\ell^1(\mathbb Z)\) with
\(\|\delta_0-a*b\|_1<1\). The Neumann series
\[
 d=\sum_{k=0}^{\infty}(\delta_0-a*b)^{*\,k}
\]
converges in this unital Banach algebra and satisfies \(d*(a*b)=\delta_0\). Thus \(c=b*d\in\ell^1(\mathbb Z)\) obeys \(a*c=\delta_0\). Fourier multiplication gives
\(\widehat c=1/\widehat a\).
Since \(\sum_n|c_n|<\infty\), the series
\(\sum_n c_ne^{-2\pi int}\) converges absolutely and uniformly, with this value. This derives the inverse assertion directly from the proved general Wiener theorem and the proved Neumann lemma. \(\square\)

## Proof dependencies and scope

Every result used above is proved here or in the exact earlier programme reading linked at its use. In particular the local reciprocal is an \(L^1\)-algebra construction, and the compact patching functions belong to the Fourier algebra. No arbitrary continuous partition is assumed to be a Fourier transform.

The equality \(I=\iota(\nu(I))\) has been proved here for compact \(G\). For general groups, Wiener's theorem proves only the empty-hull case. The next lesson treats further synthesis questions; no general hull classification is asserted here.
