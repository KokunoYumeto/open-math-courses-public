# Interpolation on logarithmic curves

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the interpolation theorem used in the determinant argument for \(\pi\): with separated weights, polynomials of bounded weighted degree realize every prescribed packet of Taylor coefficients along the logarithmic curves at all the centres at once. The proof turns the curve inequality of [The curve inequality](the-curve-inequality.md) into positivity. One compactifies affine space by weighted monomials, blows up the ideal of the prescribed jets, and shows with Kleiman's theorem that the pulled-back hyperplane bundle minus the exceptional divisor is ample. Serre vanishing on the blow-up then gives the surjectivity.

We use: [Intersection numbers of line bundles](course:intersection-numbers-and-positivity/intersection-numbers-of-line-bundles#3-pullback-and-positivity) (degrees on curves, normalization, pullback, positivity), [Nef line bundles and Kleiman's theorem](course:intersection-numbers-and-positivity/nef-line-bundles-and-kleimans-theorem#3-consequences) (Corollary 3.3: a positive multiple that is a positive combination of a nef and an ample bundle is ample); blow-ups of coherent ideals, which are projective with relatively ample \(\mathcal O(1)=\mathcal O(-E)\), Theorem 4.1 of [Blowing up](course:AG-MO/blowing-up#4-basic-properties); Segre embeddings, [Very ample invertible sheaves, Segre and Veronese embeddings](course:AG-MO/very-ample-sheaves-and-embeddings#3-segre-coordinates-from-two-factors); Serre's vanishing theorem and the identification of high-degree sections with graded pieces, Theorems 2.1, 2.2 and Lemma 3.2 of [Coherent sheaves on projective schemes: Serre's theorems](course:AG-QC/serres-theorems-on-projective-schemes#2-descending-induction-proves-serre-s-theorems); and the Leray comparison \(H^i(X',G)=H^i(X,p_*G)\) when all higher direct images of \(G\) vanish, [Cohomology of sheaves on ringed spaces](course:AG-QC/cohomology-of-sheaves-on-ringed-spaces#4-collecting-information-along-a-map). Notation and the standing data \(m,K,w_0,v_0,\theta,\sigma\) are those of Section 1 of the curve-inequality lesson.

## 1. The theorem

For a positive rational vector \(W=(w_0,\dots,w_m)\), let \(\mathcal P_W(H)\) be the space of polynomials in \(Y,X_1,\dots,X_m\) of \(W\)-degree at most \(H\). For a positive rational vector \(V=(v_0,\dots,v_m)\), let

\[
\mathcal J_V(H)=\mathbb C[[t,u_1,\dots,u_m]]\big/\{\text{series all of whose monomials have }V\text{-weight}\ge H\},
\]

the space of coefficient packets of \(t^su^\beta\) with \(v_0s+\sum_iv_i\beta_i<H\).

**Theorem 1.1** (separated-weight interpolation). Fix \(m,K\ge1\) and positive rationals \(w_0,v_0,\theta\) satisfying \(0<\theta<1\), \(K\theta^m<1\) and \(K(w_0/v_0)\theta^m<1\). There are successive thresholds for \(w_1,\dots,w_m\), each depending only on these data and the previously chosen weights, with the following property. If \(w_1,\dots,w_m\) exceed their thresholds, put \(W=(w_0,\dots,w_m)\) and \(V=(v_0,w_1/\theta,\dots,w_m/\theta)\). Then for any points \(a_j=(1,c_{j1},\dots,c_{jm})\), \(0\le j<K\), whose coordinates \(c_{0i},\dots,c_{K-1,i}\) are pairwise distinct for each \(i\), the map

\[
\mathcal P_W(H)\longrightarrow\bigoplus_{j=0}^{K-1}\mathcal J_V(H),\qquad P\longmapsto\Bigl(P\bigl(1+t,\,(c_{ji}+u_i+\log(1+t))_{i=1}^m\bigr)\Bigr)_j ,
\tag{1.1}
\]

is surjective for every \(H\) that is a sufficiently large multiple of an integer \(R\) depending only on the weights.

The thresholds are those of Lemma 1.2 of the curve-inequality lesson, which make the weights separated; only the final lower bound for \(H\) depends on the points. The dimension count of that lesson shows that the source of (1.1) is larger than the target, but this alone does not give surjectivity at special points.

Fix separated weights and centres \(a_j\) for the rest of the lesson.

## 2. A projective model of affine space

Choose a positive integer \(R\) such that \(R/w_a\) and \(R/v_a\) are integers for all \(0\le a\le m\). Let \(\mathcal M\) be the set of exponents \((h,\alpha)\) with \(w_0h+\sum_iw_i\alpha_i\le R\), and consider the morphism

\[
\iota:\mathbb C^{m+1}\to\mathbf P^{|\mathcal M|-1},\qquad x\mapsto[x^\mu]_{\mu\in\mathcal M},
\]

where \(x^\mu=Y^hX^\alpha\). Let \(X\) be the closure of its image, an integral projective variety, and \(L=\mathcal O_X(1)\), very ample. Let \(z_0\) be the coordinate of the constant monomial. On the chart \(z_0\ne0\) the coordinates \(z_\mu/z_0\) include \(Y\) and every \(X_i\) (because \(w_a\le R\)), and the image of \(\iota\) is the graph of the other monomials as polynomial functions of these; so \(\iota\) is a closed immersion onto \(X\cap\{z_0\ne0\}\), which we identify with \(\mathbb C^{m+1}\). The section \(z_0\) trivializes \(L\) on this chart.

**Lemma 2.1.** For every curve \(C\subseteq\mathbb C^{m+1}\), with closure \(\overline C\subseteq X\),

\[
\deg(L|_{\overline C})=R\deg_WC .
\]

**Proof.** Let \(\nu:\widetilde C\to\overline C\) be the normalization; \(\deg(L|_{\overline C})=\deg(\nu^*L)\). The sections \(s_\mu=\nu^*z_\mu\) generate \(\nu^*L\), so at each point \(P\) some \(s_\mu\) does not vanish, and \(\operatorname{ord}_P(s_0)=\max_\mu\bigl(\operatorname{ord}_Ps_0-\operatorname{ord}_Ps_\mu\bigr)=\max_{\mu\in\mathcal M}\bigl(-\operatorname{ord}_Px^\mu\bigr)\). For \(\mu=(h,\alpha)\in\mathcal M\), \(-\operatorname{ord}_Px^\mu=-h\operatorname{ord}_PY-\sum\alpha_i\operatorname{ord}_PX_i\le(w_0h+\sum w_i\alpha_i)M_P\le RM_P\), with \(M_P\) as in the definition of \(\deg_W\). Equality is attained: by the constant monomial if \(M_P=0\), and by the pure power \(Y^{R/w_0}\) or \(X_i^{R/w_i}\) realizing the maximum if \(M_P>0\). The degree of \(\nu^*L\) is the number of zeros of its nonzero section \(s_0\), that is \(\sum_PRM_P=R\deg_WC\). \(\square\)

## 3. The ideal of the jets

Choose, for each \(i\), a Taylor polynomial \(G_i(t)=\sum_{1\le n<T_i}(-1)^{n+1}t^n/n\) of \(\log(1+t)\) with \(v_0T_i>v_i\). At the centre \(a_j\) put

\[
t=Y-1,\qquad u_i'=X_i-c_{ji}-G_i(t).
\]

These are polynomials, and \(u_i'=u_i+\bigl(\log(1+t)-G_i(t)\bigr)\), where the bracket is a power series in \(t\) all of whose terms have \(V\)-weight \(v_0n\ge v_0T_i>v_i\).

**Lemma 3.1.**

1. The substitution \(u_i\mapsto u_i'\) is an automorphism of \(\mathbb C[[t,u]]\) preserving the \(V\)-weight filtration in both directions; it induces a bijection of \(\mathcal J_V(H)\) for every \(H\).
2. For every branch \(P\) of a curve at \(a_j\), the contact \(h_P\) of the curve-inequality lesson can be computed with \(u_i'\) in place of \(u_i\).

**Proof.** (1) Each \(u_i'\) is \(u_i\) plus terms of larger \(V\)-weight, so the substitution and its inverse map series of \(V\)-order at least \(H\) to series of \(V\)-order at least \(H\), and induce triangular maps with identity diagonal on the finite-dimensional quotients. (2) \(\operatorname{ord}_P(u_i'-u_i)\ge T_i\operatorname{ord}_Pt>(v_i/v_0)\operatorname{ord}_Pt\ge v_ih_P\). If \(\operatorname{ord}_Pu_i<v_i\,\operatorname{ord}_Pt/v_0\), then \(\operatorname{ord}_Pu_i'=\operatorname{ord}_Pu_i\); otherwise both \(\operatorname{ord}_Pu_i/v_i\) and \(\operatorname{ord}_Pu_i'/v_i\) are at least \(\operatorname{ord}_Pt/v_0\). In both cases the minimum defining \(h_P\) is unchanged. \(\square\)

Since \(t,u_1',\dots,u_m'\) are local parameters at \(a_j\), the ideal

\[
I_j=\bigl(t^{R/v_0},(u_1')^{R/v_1},\dots,(u_m')^{R/v_m}\bigr)\subseteq\mathcal O_{X,a_j}
\]

has finite colength. Let \(\mathcal I\subseteq\mathcal O_X\) be the coherent ideal equal to \(I_j\) at \(a_j\) and to \(\mathcal O_X\) away from the centres: the kernel of \(\mathcal O_X\to\bigoplus_j\mathcal O_{X,a_j}/I_j\).

**Lemma 3.2.** For a curve \(C\subseteq\mathbb C^{m+1}\) and a branch \(P\) of \(C\) at \(a_j\), the order at \(P\) of the ideal \(\mathcal I\mathcal O_{\widetilde C}\) is \(Rh_P\). Every generator of \(I_j\) has \(V\)-weight exactly \(R\) in the coordinates \(t,u'\), so \(I_j^n\) consists of series of \(V\)-order at least \(nR\).

**Proof.** In the discrete valuation ring at \(P\), the order of the ideal generated by the images of \(t^{R/v_0}\) and \((u_i')^{R/v_i}\) is the minimum of their orders, \(\min_a(R/v_a)\operatorname{ord}_Pz_a=Rh_P\), with \(z_0=t\), \(z_i=u_i'\), by Lemma 3.1(2). The second claim is clear. \(\square\)

## 4. Positivity on the blow-up

Let \(p:X'\to X\) be the blow-up of \(\mathcal I\). By the basic properties of blow-ups, \(X'\) is an integral projective variety, \(p\) is projective and birational, an isomorphism over the complement of the centres, and \(\mathcal I\mathcal O_{X'}=\mathcal O_{X'}(1)=\mathcal O_{X'}(-E)\) for an effective Cartier divisor \(E\) lying over the centres, with \(\mathcal O_{X'}(-E)\) relatively ample. Write the Picard group additively and put \(A=p^*L\).

**Lemma 4.1.** For every curve \(\Gamma\subseteq X'\),

\[
(A\cdot\Gamma)\ge(1+\sigma)(E\cdot\Gamma).
\]

Equivalently, writing \(\sigma=\sigma_1/\sigma_2\) in lowest terms, the line bundle \(\mathcal N=\sigma_2A-(\sigma_1+\sigma_2)E\) is nef.

**Proof.** Three cases.

*\(p(\Gamma)\) is a point.* Then \((A\cdot\Gamma)=0\) by the pullback formula. The curve \(\Gamma\) lies in a fibre of \(p\), on which the relatively ample \(\mathcal O(-E)\) restricts to an ample bundle, so \((-E\cdot\Gamma)>0\), and the inequality holds strictly.

*\(p(\Gamma)\) is a curve through no centre.* Then \(\Gamma\) misses \(E\), the canonical section of \(\mathcal O(E)\) has no zero on \(\Gamma\), and \((E\cdot\Gamma)=0\), while \((A\cdot\Gamma)=\deg(L|_{p(\Gamma)})\ge0\) because \(L\) is very ample.

*\(p(\Gamma)=\overline C\) is a curve through a centre.* Then \(C=\overline C\cap\mathbb C^{m+1}\) is a curve in affine space, and \(\Gamma\to\overline C\) is birational because \(p\) is an isomorphism away from the finitely many centres. So \((A\cdot\Gamma)=\deg(L|_{\overline C})=R\deg_WC\) by the pullback formula and Lemma 2.1. Both curves have the normalization \(\widetilde C\), and the pullback of \(\mathcal O(-E)\) to \(\widetilde C\) is the ideal \(\mathcal I\mathcal O_{\widetilde C}=\mathcal O_{\widetilde C}(-\sum_P\operatorname{ord}_P(\mathcal I)P)\). By Lemma 3.2, \((E\cdot\Gamma)=\sum_PRh_P\), the sum over the branches of \(C\) at the centres. The curve inequality gives \((A\cdot\Gamma)-(1+\sigma)(E\cdot\Gamma)=R\bigl(\deg_WC-(1+\sigma)\sum_Ph_P\bigr)\ge0\).

Every curve of \(X'\) is of one of these three types. \(\square\)

**Lemma 4.2.** There is an integer \(a\ge2\) such that \(aA-E\) is ample.

**Proof.** By Serre's theorem there is \(b\ge1\) such that \(\mathcal I\otimes L^b\) is generated by finitely many global sections, giving a surjection \(\mathcal O_X^{r+1}\to\mathcal I\otimes L^b\). On an open set where \(L\) is trivial, multiplying the degree-\(n\) piece by a trivialization of \(L^{bn}\) identifies the Rees algebra \(\bigoplus\mathcal I^n\) with \(\bigoplus(\mathcal I\otimes L^b)^n\); these identifications glue to an isomorphism of their Proj over \(X\), under which \(\mathcal O(1)\) corresponds to \(\mathcal O_{X'}(1)\otimes p^*L^b\). The surjection of the symmetric algebra of \(\mathcal O_X^{r+1}\) onto \(\bigoplus(\mathcal I\otimes L^b)^n\), which is generated in degree one, gives a closed immersion \(X'\hookrightarrow X\times\mathbf P^r\) with \(\mathcal O_{\mathbf P^r}(1)\) restricting to \(bA-E\). The Segre bundle \(L\boxtimes\mathcal O_{\mathbf P^r}(1)\) is very ample on \(X\times\mathbf P^r\), and restricts to \((b+1)A-E\). Take \(a=b+1\), or larger: \(aA-E=((b+1)A-E)+(a-b-1)A\) is ample plus nef. \(\square\)

**Proposition 4.3.** The line bundle \(A-E\) on \(X'\) is ample.

**Proof.** With \(\sigma=\sigma_1/\sigma_2\), \(\mathcal N\) from Lemma 4.1, \(\mathcal M=aA-E\) from Lemma 4.2 and \(D=a\sigma_1+a\sigma_2-\sigma_2\ge1\),

\[
(a-1)\mathcal N+\sigma_1\mathcal M=\bigl((a-1)\sigma_2+a\sigma_1\bigr)A-\bigl((a-1)(\sigma_1+\sigma_2)+\sigma_1\bigr)E=D(A-E).
\]

Here \(\mathcal N\) is nef, \(\mathcal M\) is ample and \(a-1,\sigma_1\ge1\). Corollary 3.3 of the Kleiman lesson shows that \(A-E\) is ample. \(\square\)

This is the only place where the curve inequality is used. The coefficient \(1+\sigma>1\) in Lemma 4.1 is what leaves room for an ample combination; with coefficient exactly \(1\), one would only know that \(A-E\) is nef.

## 5. Vanishing and surjectivity

**Lemma 5.1.** For all sufficiently large \(n\),

\[
p_*\mathcal O_{X'}(-nE)=\mathcal I^n,\qquad R^qp_*\mathcal O_{X'}(-nE)=0\quad(q>0).
\]

**Proof.** The statement is local on \(X\). Over an affine open \(\operatorname{Spec}B\), \(X'\) is \(\operatorname{Proj}S\) with \(S=\bigoplus_nI^n\) a graded \(B\)-algebra generated in degree one by finitely many elements, \(B\) Noetherian, and \(\mathcal O_{X'}(-nE)=\mathcal O(n)\). Serre's theorems for the closed subscheme \(\operatorname{Proj}S\) of a projective space over \(B\) give \(H^0(\operatorname{Proj}S,\mathcal O(n))=S_n=I^n\) and \(H^q(\operatorname{Proj}S,\mathcal O(n))=0\) for \(q>0\) and \(n\) large. Finitely many affine opens cover \(X\), and the largest of their thresholds works. \(\square\)

The lemma concerns the ordinary powers \(\mathcal I^n\), and only for large \(n\).

**Lemma 5.2.** For all sufficiently large \(n\), \(H^1(X,\mathcal I^n\otimes L^n)=0\).

**Proof.** By the projection formula and Lemma 5.1, \(p_*\mathcal O_{X'}(n(A-E))=\mathcal I^n\otimes L^n\) and the higher direct images vanish, for \(n\) large. The Leray comparison gives \(H^1(X,\mathcal I^n\otimes L^n)=H^1(X',\mathcal O_{X'}(n(A-E)))\), which vanishes for \(n\) large by Serre's vanishing theorem for the ample bundle \(A-E\) (Proposition 4.3). \(\square\)

**Proof of Theorem 1.1.** Let \(n\) be large. The exact sequence \(0\to\mathcal I^n\otimes L^n\to L^n\to L^n\otimes\mathcal O_X/\mathcal I^n\to0\) and Lemma 5.2 show that

\[
H^0(X,L^n)\to H^0(X,L^n\otimes\mathcal O_X/\mathcal I^n)=\bigoplus_j\mathcal O_{X,a_j}/I_j^n
\]

is surjective; the last identification uses the trivialization of \(L\) by \(z_0\) near the centres. Serre's theorem for the ideal of \(X\) in projective space shows that, for \(n\) large, every section of \(L^n\) is the restriction of a homogeneous polynomial \(\Phi\) of degree \(n\) in the \(z_\mu\). In the chart \(z_0=1\), \(\Phi\) becomes a polynomial in \(Y,X\) of \(W\)-degree at most \(nR\), since each \(z_\mu\) is a monomial of \(W\)-degree at most \(R\). So polynomials of \(W\)-degree at most \(nR\) map onto \(\bigoplus_j\mathcal O_{X,a_j}/I_j^n\). The quotient \(\mathcal O_{X,a_j}/I_j^n\) is Artinian, equal to \(\mathbb C[[t,u']]/I_j^n\), and by Lemma 3.2 it maps onto the packets of coefficients of \(V\)-weight less than \(nR\) in the coordinates \(t,u'\). Finally Lemma 3.1(1) translates these packets into those of (1.1). So (1.1) is surjective for \(H=nR\), \(n\) large. \(\square\)

## 6. Exercises

**Exercise 6.1.** For \(m=1\) and weights \(w_0=w_1=1\), \(R=1\), describe the variety \(X\) of Section 2 and the bundle \(L\).

**Exercise 6.2.** Explain why the proof needs Lemma 5.1 for the ordinary powers \(\mathcal I^n\) rather than for their integral closures, and where the inclusion \(I_j^n\subseteq\{V\text{-order}\ge nR\}\) is used.

**Exercise 6.3.** Show that if the inequality of Lemma 4.1 held only with coefficient \(1\), the argument would show only that \(A-E\) is nef. Give an example of a blow-up where \(A-E\) is nef but not ample. Why is nefness not enough for the proof?

**Exercise 6.4.** Verify the identity \((a-1)\mathcal N+\sigma_1\mathcal M=D(A-E)\) of Proposition 4.3.

## 7. Solutions

**6.1.** The monomials of degree at most \(1\) are \(1,Y,X_1\), and \(\iota(Y,X_1)=[1:Y:X_1]\), so \(X=\mathbf P^2\) and \(L=\mathcal O(1)\).

**6.2.** Lemma 5.1 identifies \(p_*\mathcal O(-nE)\) with the actual powers \(\mathcal I^n\), whose sections are the ones lifted in the proof. The surjectivity is onto \(\mathcal O/\mathcal I^n\); to pass to the coefficient packets of weight below \(nR\) one needs that every element of \(\mathcal I^n\) has weight at least \(nR\), which is the inclusion. Equality is not needed.

**6.3.** If only \((A\cdot\Gamma)\ge(E\cdot\Gamma)\) were known, \(A-E\) would be nef. On the blow-up of \(\mathbf P^2\) at a point, with \(A\) the pullback of \(\mathcal O(1)\) and \(E\) the exceptional curve, \(A-E\) is the pullback of \(\mathcal O(1)\) under the projection from the point to a line: it is globally generated, hence nef, and it has degree \(0\) on the strict transforms of the lines through the point, so it is not ample. The proof needs the vanishing of \(H^1(X',\mathcal O(n(A-E)))\) for large \(n\), which Serre's theorem guarantees for ample bundles but not for nef ones: the trivial bundle on an elliptic curve is nef, and its first cohomology is one-dimensional for every twist.

**6.4.** The coefficient of \(A\) is \((a-1)\sigma_2+a\sigma_1=D\), and the coefficient of \(-E\) is \((a-1)(\sigma_1+\sigma_2)+\sigma_1=a\sigma_1+a\sigma_2-\sigma_2=D\).

## References

- [OpenAI-Pi] OpenAI, The irrationality exponent of π is 2, preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026
- [Demailly] J.-P. Demailly, Singular hermitian metrics on positive line bundles, author's manuscript (1992). https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/bayreuth.pdf
- [Stacks] The Stacks project authors, The Stacks project, chapter Divisors, section Blowing up (Tag 01OF). https://stacks.math.columbia.edu/tag/01OF
