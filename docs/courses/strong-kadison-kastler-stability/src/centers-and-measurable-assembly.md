# Centers and measurable assembly

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson extends strong stability from factors to all von Neumann algebras on separable Hilbert spaces (Theorem 5.1). Close algebras have close centers, by Dixmier's approximation theorem (Theorem 1.2, proved here). Christensen's theorem then makes the two centers equal after a small unitary change (Lemma 2.1). For algebras with a common center, the central decomposition writes both as direct integrals of factors over one measure space. Their fibers are at most as far apart as the algebras (Lemma 3.1), the factor theorem conjugates the fibers, and a measurable selection assembles the fiberwise unitaries into one (Lemma 4.1). The uniformity of the factor theorem is what makes the assembly possible: one bound must hold for almost every fiber [OpenAI-289, Section 9].

We use: [Close operator algebras](close-operator-algebras.md) (Lemmas 1.4 and 1.5); [Averaging and the completely positive criterion](averaging-and-the-completely-positive-criterion.md) (Theorem 3.1); [Stability of separably acting factors](stability-of-separably-acting-factors.md) (Theorem 1.1, with \(t_{\rm fac}\) and \(\eta_{\rm fac}\)); the [comparison theorem](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras#OA-FND-TY-03) for projections (Theorem 5.5 of the projections lesson); [Kaplansky's density theorem](course:foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences#OA-FND-KD-07); from [Polish spaces and standard Borel spaces](course:foundations-of-von-neumann-algebras/polish-spaces-and-standard-borel-spaces#OA-FND-PB-11), Theorem 7.7 (measurable sections, Jankov–von Neumann) and [Theorem 6.2](course:foundations-of-von-neumann-algebras/polish-spaces-and-standard-borel-spaces#OA-FND-PB-09) (Souslin sets are measurable); and from [The central decomposition and the types of the fibres](course:measurable-fields-and-direct-integrals/the-central-decomposition-and-the-types-of-the-fibres#1-conventions-and-results-used), Facts 1.1 and 1.2 on measurable fields and direct integrals, Theorem 2.1 (diagonalizing an abelian algebra) and [Theorem 4.1](course:measurable-fields-and-direct-integrals/the-central-decomposition-and-the-types-of-the-fibres#4-the-central-decomposition) (the central decomposition).

## 1. Dixmier's approximation theorem

Let \(M\) be a von Neumann algebra with center \(\mathcal Z\). An *averaging map* is a map \(\alpha(y)=\sum_{i=1}^mt_iu_iyu_i^*\) with unitaries \(u_i\in M\) and weights \(t_i\ge0\) of sum \(1\). It is linear, unital, positive, contractive and adjoint-preserving, fixes \(\mathcal Z\) pointwise, and satisfies \(\alpha(cy)=c\,\alpha(y)\) for \(c\in\mathcal Z\). Compositions of averaging maps are averaging maps, and \(\alpha(x)\) lies in the convex hull of the unitary orbit of \(x\).

**Lemma 1.1** (one averaging step). Let \(x=x^*\in M\) with \(\|x\|\le1\). There are a self-adjoint unitary \(u\in M\) and a self-adjoint \(y\in\mathcal Z\) with \(\|y\|\le\frac14\) and
\[
\bigl\|\tfrac12(x+uxu)-y\bigr\|\le\tfrac34 .
\]

**Proof.** Let \(p=1_{(0,\infty)}(x)\); then \(-(1-p)\le x\le p\). By the comparison theorem there is a central projection \(z\) with \(pz\precsim(1-p)z\) and \((1-p)(1-z)\precsim p(1-z)\). Choose partial isometries \(v,w\in M\) with \(v^*v=pz\), \(vv^*\le(1-p)z\), \(w^*w=(1-p)(1-z)\) and \(ww^*\le p(1-z)\). The projections
\[
\begin{aligned}
&pz,\ vv^*,\ (1-p)z-vv^*,\\
&\quad \ (1-p)(1-z),\ ww^*,\ p(1-z)\\
&\quad -ww^*
\end{aligned}
\]
are mutually orthogonal with sum \(1\). Put \(u=v+v^*+((1-p)z-vv^*)\)\(+w+w^*+(p(1-z)-ww^*)\). Then \(u=u^*\), \(u^2=1\), \(u\) commutes with \(z\), \(u(pz)u=vv^*\) and \(u((1-p)(1-z))u=ww^*\). Let \(a=\frac12(x+uxu)\) and \(y=\frac14(1-2z)\).

On \(zH\): \(xz\le pz\), so \(uxuz\le u(pz)u=vv^*\), and \(az\le\frac12(pz+vv^*)\le\frac12z\); also \(az\ge-z\). Since \(yz=-\frac14z\), \(-\frac34z\le(a-y)z\le\frac34z\). On \((1-z)H\): \(x(1-z)\ge-(1-p)(1-z)\), so \(uxu(1-z)\ge-ww^*\), and \(a(1-z)\ge-\frac12(1-z)\); also \(a(1-z)\le1-z\). Since \(y(1-z)=\frac14(1-z)\), \(-\frac34(1-z)\le(a-y)(1-z)\le\frac34(1-z)\). Adding, \(\|a-y\|\le\frac34\). \(\square\)

**Theorem 1.2** (Dixmier's approximation theorem). For every \(x\in M\) and \(\varepsilon>0\) there are an averaging map \(\alpha\) and \(c\in\mathcal Z\) with \(\|\alpha(x)-c\|\le\varepsilon\). If \(x\) is self-adjoint, the norm-closed convex hull of the unitary orbit of \(x\) contains an element of \(\mathcal Z\).

**Proof.** Let \(x\) be self-adjoint and put \(x_0=x\). Given a self-adjoint \(x_k\), Lemma 1.1 applied to \(x_k/\|x_k\|\) (or \(u=1\), \(y=0\) if \(x_k=0\)), and rescaled, gives an averaging map \(\alpha_{k+1}\) and a central self-adjoint \(y_{k+1}\) with \(\|y_{k+1}\|\le\frac14\|x_k\|\) and \(\|\alpha_{k+1}(x_k)-y_{k+1}\|\le\frac34\|x_k\|\). Put \(x_{k+1}=\alpha_{k+1}(x_k)-y_{k+1}\). By induction, using that averaging maps fix central elements,
\[
\begin{gathered}
\alpha_k\cdots\alpha_1(x)=x_k+y_1+\dots+y_k,\\
\|x_k\|\le(3/4)^k\|x\| .
\end{gathered}
\]
The series \(\sum_jy_j\) converges in norm to a central \(c\), and \(\alpha_k\cdots\alpha_1(x)\to c\), so \(c\) lies in the norm-closed convex hull of the orbit. For general \(x=a+ib\) with \(a,b\) self-adjoint, choose an averaging map \(\alpha\) with \(\alpha(a)\) within \(\varepsilon/2\) of \(\mathcal Z\), and then an averaging map \(\beta\) with \(\beta(\alpha(b))\) within \(\varepsilon/2\) of \(\mathcal Z\). Since \(\beta\) is contractive and fixes \(\mathcal Z\), \(\beta\alpha(a)\) is still within \(\varepsilon/2\) of \(\mathcal Z\), and \(\beta\alpha(x)\) is within \(\varepsilon\) of \(\mathcal Z\). \(\square\)

## 2. Aligning the centers

**Lemma 2.1** (close centers). For unital von Neumann algebras \(M,N\subseteq B(H)\),
\[
d\bigl(Z(M),Z(N)\bigr)\le3\,d(M,N).
\]
If \(d(M,N)<g<1/303\), there is a unitary \(w\) with \(wZ(M)w^*=Z(N)\) and \(\|w-1\|\le450g\); the algebra \(N_0=w^*Nw\) then has \(Z(N_0)=Z(M)\) and \(d(M,N_0)<901g\).

**Proof.** Let \(d(M,N)<g\), \(z\in Z(M)_1\), and \(y\in N_1\) with \(\|z-y\|<g\). For a unitary \(v\in N\) choose \(a\in M_1\) with \(\|v-a\|<g\); since \(z\) commutes with \(a\), \(\|[z,v]\|=\|[z,v-a]\|<2g\), and
\[
\begin{aligned}
\|vyv^*-z\|&\le\|v(y-z)v^*\|+\|vzv^*-z\|\\
&<3g .
\end{aligned}
\]
So every element of the convex hull of the unitary orbit of \(y\) in \(N\) is within \(3g\) of \(z\). By Theorem 1.2 in \(N\), for every \(\varepsilon>0\) there is \(c\in Z(N)\) with \(\|c-z\|\le3g+\varepsilon\) and \(\|c\|\le1+\varepsilon\); normalizing (Lemma 1.4 of [Close operator algebras](close-operator-algebras.md)) gives \(\operatorname{dist}(z,Z(N)_1)\le3g+2\varepsilon\). Exchanging \(M\) and \(N\) and letting \(g\downarrow d(M,N)\) gives the inequality.

Abelian von Neumann algebras are injective. If \(d(M,N)<g<1/303\), then \(Z(M)\subset_{3g}Z(N)\) and \(Z(N)\subset_{3g}Z(M)\) with \(3g<1/101\), and Christensen's theorem (Theorem 3.1 of the averaging lesson) gives \(w\) with \(wZ(M)w^*=Z(N)\) and \(\|w-1\|\le450g\). Then \(Z(N_0)=w^*Z(N)w=Z(M)\), and Lemma 1.5 of [Close operator algebras](close-operator-algebras.md) gives \(d(M,N_0)<g+900g\). \(\square\)

## 3. The common central decomposition and its fibers

Let \(M,N\subseteq B(H)\) be von Neumann algebras on a separable Hilbert space with the same center \(\mathcal Z\). Theorem 2.1 of the central decomposition lesson, applied to \(\mathcal Z\), gives a Borel probability measure \(\mu\) on \(\mathbb R\), a measurable field of Hilbert spaces \((H(t))\) and a unitary identifying \(H\) with \(\int^\oplus H(t)\,d\mu(t)\) and \(\mathcal Z\) with the diagonal algebra. Theorem 4.1 there, applied to \(M\) and to \(N\) with this same identification, gives measurable fields of factors \(M(t)\) and \(N(t)\) with
\[
\begin{gathered}
M=\int^\oplus M(t)\,d\mu(t),\\
N=\int^\oplus N(t)\,d\mu(t):
\end{gathered}
\]
\(M\) consists of the operators \(\int^\oplus x\) for essentially bounded measurable operator fields \(x\) with \(x(t)\in M(t)\) almost everywhere, and \(\|\int^\oplus x\|=\operatorname{ess\,sup}_t\|x(t)\|\) (Facts 1.1(e) and 1.2 there).

**Lemma 3.1** (fiber gaps). In this situation \(d(M(t),N(t))\le d(M,N)\) for almost every \(t\).

**Proof.** The strong topology on the unit ball of \(B(H)\) is metrizable and separable, so there are norm-separable unital C\*-subalgebras \(A\subseteq M\) and \(B\subseteq N\) that are strongly dense; by Theorem 4.1(2) of the central decomposition lesson, \(M(t)=A(t)''\) and \(N(t)=B(t)''\) for almost every \(t\), where \(A(t)\) is the set of fiber values of elements of \(A\). Choose countable norm-dense subsets \(\{a_j\}\subseteq A_1\) and \(\{b_j\}\subseteq B_1\), and fix fields representing them and the countably many elements of the \(\mathbb Q+i\mathbb Q\)-algebra they generate. Off one null set, the fiber map is a \(*\)-homomorphism on this countable algebra, contractive since norms are essential suprema; it extends to a \(*\)-homomorphism of \(A\) onto \(A(t)\), a quotient map. A contraction of \(A(t)\) lifts to elements of \(A\) of norm at most \(1+s\) for every \(s>0\); rescaling, the image of \(A_1\) is dense in \(A(t)_1\), so \(\{a_j(t)\}\) is norm dense in \(A(t)_1\) and, by Kaplansky's density theorem, strongly dense in \(M(t)_1\). The same holds for \(B\).

Put \(d_0=d(M,N)\). For \(j,n\ge1\) choose \(y_{j,n}\in N_1\) with \(\|a_j-y_{j,n}\|<d_0+1/n\). Off one null set, \(y_{j,n}(t)\in N(t)_1\) and \(\|a_j(t)-y_{j,n}(t)\|\le d_0+1/n\) for all \(j,n\). Fix such \(t\), \(x\in M(t)_1\) and \(n\). Take a net \(a_{j_\iota}(t)\to x\) strongly; a subnet of \(y_{j_\iota,n}(t)\) converges weakly to some \(y\in N(t)_1\), and since norm balls are weakly closed, \(\|x-y\|\le d_0+1/n\). So \(\operatorname{dist}(x,N(t)_1)\le d_0\). Making the same choices in the other direction, and discarding their null sets as well, proves both near inclusions on one conull set. \(\square\)

## 4. Measurable implementers

**Lemma 4.1** (measurable implementers). In the situation of Lemma 3.1, suppose that for some \(a>0\) and almost every \(t\) there is a unitary \(v_t\) on \(H(t)\) with \(v_tM(t)v_t^*=N(t)\) and \(\|v_t-1\|<a\). Then there is a unitary \(v\in B(H)\) with \(vMv^*=N\) and \(\|v-1\|\le a\).

**Proof.** By Fact 1.1(c) of the central decomposition lesson, the dimension function \(t\mapsto\dim H(t)\) is measurable, and on each set \(\Gamma_d\) where it equals \(d\in\{0,1,2,\dots,\infty\}\) there are measurable unitaries identifying \(H(t)\) with a fixed separable space \(K_d\). Fibers of dimension \(0\) contribute nothing. Keep the countable fields \(a_j(t)\), \(b_j(t)\) of the proof of Lemma 3.1, transported to \(K_d\), and replace \(\mathbb R\) by a Borel set of full measure on which all the identifications of that proof hold, the hypothesis holds, and the fields are Borel.

Fix \(d\) and a dense sequence \((\xi_l)\) in the unit sphere of \(K_d\). The unitary group \(\mathcal U(K_d)\) with the strong\* topology is a Polish space. Let \(R\subseteq\Gamma_d\times\mathcal U(K_d)\) be the set of pairs \((t,u)\) with \(\|(u-1)\xi_l\|\le a\) for all \(l\) and with the two families of conditions
\[
\begin{aligned}
&\forall j,m,k\ \exists q:\\
&\quad\max_{l\le m}\|(ua_j(t)u^*-b_q(t))\xi_l\|<1/k,\\
&\forall j,m,k\ \exists q:\\
&\quad\max_{l\le m}\|(u^*b_j(t)u-a_q(t))\xi_l\|<1/k .
\end{aligned}
\]
Each condition is Borel in \((t,u)\), being Borel in \(t\) and continuous in \(u\), so \(R\) is a Borel set. The first family says that \(ua_j(t)u^*\) lies in the strong closure of \(\{b_q(t)\}\), which is \(N(t)_1\); since the \(a_j(t)\) are strongly dense in \(M(t)_1\), it says \(uM(t)u^*\subseteq N(t)\). Likewise the second family says \(u^*N(t)u\subseteq M(t)\). So \(R\) consists exactly of the pairs where \(u\) conjugates \(M(t)\) onto \(N(t)\) with \(\|u-1\|\le a\), and its sections are nonempty by hypothesis.

\(R\) is a Borel subset of a Polish space, hence a Souslin space, and the projection to \(\Gamma_d\) is a Borel map onto \(\Gamma_d\). By Theorem 7.7 of the Polish spaces lesson there is a \(\mu\)-measurable selection \(t\mapsto u(t)\) with \((t,u(t))\in R\). Combining the strata, \(u(t)\) is a measurable field of unitaries with \(\|u(t)-1\|\le a\), and \(v=\int^\oplus u(t)\,d\mu(t)\) is a unitary with \(\|v-1\|\le a\). For \(x=\int^\oplus x(t)\in M\), the field \(u(t)x(t)u(t)^*\) is essentially bounded, measurable and takes values in \(N(t)\), so \(vxv^*\in N\); and \(v^*Nv\subseteq M\) in the same way. \(\square\)

## 5. All von Neumann algebras on separable spaces

**Theorem 5.1.** For every \(a>0\) there is \(\delta_{\rm sep}(a)>0\) such that, whenever \(M,N\) are unital von Neumann algebras on a separable Hilbert space \(H\) with \(d(M,N)<\delta_{\rm sep}(a)\), there is a unitary \(u\) with
\[
uMu^*=N,\qquad\|u-1\|<a .
\]
The tolerance does not depend on the algebras or the representation.

**Proof.** If \(H=\{0\}\) there is nothing to prove. Choose \(\tau\in(0,t_{\rm fac})\) with \(\eta_{\rm fac}(\tau)<a/2\), using Theorem 1.1 of the factor lesson, and then \(\delta=\delta_{\rm sep}(a)>0\) with \(\delta<1/303\), \(450\delta<a/2\) and \(901\delta<\tau\). Let \(d(M,N)<\delta\). Lemma 2.1 with \(g=\delta\) gives \(w\) with \(\|w-1\|\le450\delta<a/2\) and \(N_0=w^*Nw\) with \(Z(N_0)=Z(M)\) and \(d(M,N_0)<901\delta\). In the common central decomposition, Lemma 3.1 gives \(d(M(t),N_0(t))<901\delta\) for almost every \(t\). The fibers are factors on separable spaces, and Theorem 1.1 of the factor lesson gives unitaries \(v_t\) with \(v_tM(t)v_t^*=N_0(t)\) and \(\|v_t-1\|\le\eta_{\rm fac}(901\delta)\le\eta_{\rm fac}(\tau)<a/2\). Lemma 4.1 assembles them into \(v\) with \(vMv^*=N_0\) and \(\|v-1\|\le a/2\). Then \(u=wv\) conjugates \(M\) onto \(N\), and \(\|u-1\|\le\|w-1\|+\|v-1\|<a\). \(\square\)

## 6. Exercises

**Exercise 6.1.** Show that in Lemma 1.1 the operator \(u\) satisfies \(u^2=1\), by computing the products of its six pieces.

**Exercise 6.2.** Let \(M=M_2(\mathbb C)\) and \(x=\operatorname{diag}(1,-1)\). Find an averaging map \(\alpha\) with \(\alpha(x)=0\).

**Exercise 6.3.** Show that the inequality of Lemma 2.1 can be strict: give \(M\ne N\) with \(Z(M)=Z(N)\).

**Exercise 6.4.** Let \(M\) and \(N\) be abelian with \(d(M,N)<1/303\). What does the proof of Theorem 5.1 give, and which lemma alone suffices?

**Exercise 6.5.** In the proof of Lemma 4.1, explain why the condition \(\|(u-1)\xi_l\|\le a\) for all \(l\) is equivalent to \(\|u-1\|\le a\).

## 7. Solutions

**Solution 6.1.** With \(v=P_2vP_1\) and \(w=Q_2wQ_1\) for the six projections in the order listed, \(v^2=0\), \(vv^*\) and \(v^*v\) are the projections \(P_2,P_1\), all products of pieces supported on different projections vanish, and the squares of the two remaining projections are themselves. So \(u^2\)\(=P_1+P_2+P_3+Q_1+Q_2+Q_3\)\(=1\).

**Solution 6.2.** With the flip \(f=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), \(fxf=-x\), so \(\alpha(y)=\frac12(y+fyf)\) gives \(\alpha(x)=0\), the center element \(\frac12\operatorname{tr}(x)\cdot1\).

**Solution 6.3.** Take two distinct factors on one space, for instance \(M=M_2(\mathbb C)\otimes1\) on \(\mathbb C^2\otimes\mathbb C^2\) and \(N=uMu^*\) for a unitary \(u\) with \(uMu^*\ne M\). Both centers are \(\mathbb C1\), so \(d(Z(M),Z(N))=0\), while \(d(M,N)>0\) by Exercise 5.1 of [Close operator algebras](close-operator-algebras.md).

**Solution 6.4.** Abelian algebras are their own centers, so Lemma 2.1 already conjugates \(M\) onto \(N\) by a unitary within \(450d(M,N)\) of \(1\), by Christensen's theorem.

**Solution 6.5.** \(u-1\) is bounded, and its norm is the supremum of \(\|(u-1)\xi\|\) over the unit sphere, in which the \(\xi_l\) are dense.

## References

- [OpenAI-289] OpenAI, Universal strong Kadison–Kastler stability, preprint, 23 September 2026, Section 9. https://github.com/openai/math/tree/main/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026
- [Dixmier] J. Dixmier, Les anneaux d'opérateurs de classe finie, Annales scientifiques de l'École Normale Supérieure 66 (1949), 209–261 (the approximation theorem). https://doi.org/10.24033/asens.970
