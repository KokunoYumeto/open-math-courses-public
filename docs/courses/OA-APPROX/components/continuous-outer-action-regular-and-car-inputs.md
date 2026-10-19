# Complete regular-representation and tracial CAR inputs

*Original programme exposition: CC0-1.0 to the extent of rights held. The linked Haar component retains its attribution to D. H. Fremlin and its separate human-source terms.*

These arguments supply the measure, Hilbert, CAR and normal-continuity inputs of [Continuous outer actions](../src/continuous-outer-actions-of-locally-compact-groups.md). Throughout, inner products are linear in the second variable. CF, CP and BD denote the complete calculus, concrete predual and bounded-density proofs; SS2 constructs the entire tracial matrix product; AF1 supplies its finite trace projections; FH3 identifies the whole tail algebras. All are complete programme proofs.

Their complete texts are the retained calculus, predual and bounded-density proofs, [whole tracial matrix products](strong-stability-matrix-and-product-inputs.md#ss2-whole-variable-matrix-tracial-product), [finite trace projections and AFD uniqueness](central-afd-uniqueness-inputs.md), and [tail and canonical trace inputs](fullness-hypercentrality-and-tail-inputs.md).

<a id="co0-compact-closures-and-bumps"></a>

## CO0. Compact closures and compactly supported cutoffs

In a Hausdorff space every compact set is closed. To separate a point outside a compact set, choose disjoint neighborhoods of the point and each compact-set point, retain finitely many of the latter neighborhoods, and intersect their partner neighborhoods. The same argument, twice, separates two disjoint compact sets.

A compact Hausdorff space is therefore normal: its closed sets are compact, so disjoint closed sets have disjoint open neighborhoods. Consequently, if \(A\) is closed and \(A\subset O\) with \(O\) open, separating \(A\) from the closed complement gives
\[
A\subset V\subset\overline V\subset O .
\tag{CO0.1}
\]
The closure inclusion follows because the disjoint partner neighborhood contains the complement of \(O\).

Let \(X\) be locally compact Hausdorff, \(x\in O\) and \(O\) open. Choose a compact neighborhood \(C\) of \(x\), and work in the compact Hausdorff space \(C\). Apply (CO0.1) to \(\{x\}\subset O\cap\operatorname{int}_X C\). The resulting relative open neighborhood lies in \(\operatorname{int}_X C\), hence is open in \(X\), and its closure in \(X\) equals its compact relative closure in \(C\). Thus
\[
x\in V,\qquad \overline V\text{ compact},\qquad \overline V\subset O.
\tag{CO0.2}
\]
A finite union of these neighborhoods proves the same statement for any compact \(A\subset O\). Compactness of a finite product follows directly from the tube argument: finite rectangles cover each compact fiber, their first-coordinate neighborhoods intersect to a neighborhood of the fiber, and finitely many such neighborhoods cover the other compact factor.

Here is the whole cutoff construction. On a normal space \(C\), with disjoint closed \(E,F\), choose open sets \(V_r\), for dyadic \(r\in[0,1]\), such that
\[
E\subset V_0,\qquad V_1=C\setminus F,\qquad
\overline{V_r}\subset V_s\quad(r<s).
\]
Start with (CO0.1) for \(E\subset C\setminus F\). At each subdivision apply (CO0.1) between the already chosen adjacent closure and open set. Define
\[
q(x)=\inf\{r:x\in V_r\},\qquad \inf\varnothing=1.
\]
It is zero on \(E\) and one on \(F\). For \(0<\alpha\le1\) and \(0\le\beta<1\),
\[
\{q<\alpha\}=\bigcup_{r<\alpha}V_r,\qquad
\{q>\beta\}=\bigcup_{s>\beta}(C\setminus\overline{V_s}).
\]
The first identity is the definition of the infimum. For the second, bracket a value larger than \(\beta\) by two dyadics and use the nested closures; conversely, missing \(\overline{V_s}\) excludes every \(V_r\) with \(r\le s\). Both sets are open; the other parameter ranges give the empty set or the whole space. Thus \(q\) is continuous.

For compact \(A\subset O\) in \(X\), choose \(A\subset V\subset C=\overline V\subset O\) by (CO0.2). Apply the construction on \(C\) to \(E=A\), \(F=C\setminus V\), and take \(f=1-q\) on \(C\), zero outside \(C\). The definitions agree on \(C\setminus V\). For a closed subset \(D\) of \([0,1]\), its inverse image is the closed relative inverse image in \(C\) if \(0\notin D\), and the union of that image with \(X\setminus V\) if \(0\in D\). It is therefore closed in \(X\). We have proved
\[
f\in C_c(X),\qquad 0\le f\le1,\qquad
f|_A=1,\qquad \operatorname{supp}f\subset O .
\tag{CO0.3}
\]
No metrizability or normality of the whole \(X\) was assumed.

<a id="co1-complete-haar-measure-route"></a>

## CO1. The complete Haar construction and its measure convention

The full compact-content proof is [Haar measure on locally compact groups, Theorem 8.3 and Lemma 8.4](../../harmonic-analysis-on-locally-compact-groups/src/haar-measure-on-locally-compact-groups.md#oa-fnd-hm-05). Its only inputs are the compact-neighborhood facts just proved, the compact product argument below, and the entire [Carathéodory proof](../../harmonic-analysis-on-locally-compact-groups/src/measure-and-hilbert-space-tools.md#1-from-an-outer-measure-to-a-measure).

For completeness, a product of compact Hausdorff spaces is compact. A family of closed sets with the finite-intersection property generates a proper filter of subsets of the product. CF's maximality consequence of choice extends it to a maximal proper filter \(\mathcal U\): unions of chains of proper filters are proper filters. Maximality implies that for every subset \(A\), either \(A\) or its complement belongs to \(\mathcal U\). Otherwise adjoining \(A\) would still generate a proper filter, since every existing filter member meets \(A\), a contradiction. Push this filter forward to each coordinate space. The closures of its members have the finite-intersection property, so compactness supplies a point in their intersection. Every neighborhood of that point belongs to the coordinate filter: otherwise its closed complement would belong and exclude the point. Choose these coordinate points using choice. Every basic product neighborhood is the intersection of finitely many coordinate inverse images, so it belongs to \(\mathcal U\). The resulting product point lies in each original closed filter member, since otherwise its open complement would also belong. Thus every closed family with the finite-intersection property intersects, which is exactly compactness by taking complements of open covers. The closed bounded coordinate intervals used below are compact by CF's complete real-box proof.

To identify the exact route, fix a compact identity neighborhood \(K_0\) and an open identity neighborhood \(V_0\subset K_0\). For a compact \(K\), the minimum number \((K:U)\) of left translates of \(U\) covering \(K\) is finite. The normalized data
\[
c_U(K)=\frac{(K:U)}{(K_0:U)},\qquad
0\le c_U(K)\le(K:V_0),\qquad c_U(K_0)=1
\]
are left invariant, monotone and subadditive. If \(K,L\) are disjoint compact sets, choose \(U\) sufficiently small that
\[
U^{-1}U\cap K^{-1}L=\varnothing .
\tag{CO1.1}
\]
No left translate of \(U\) then meets both sets. Splitting a minimal cover proves eventual disjoint additivity. The compact product of the bounded coordinate intervals has a point in every closed neighborhood tail of these data, by its finite-intersection property. That point gives an invariant compact content \(c\) with \(c(K_0)=1\).

Lemma 8.4 supplies the whole conversion:
\[
m(O)=\sup_{K\subset O,\ K\text{ compact}}c(K),\qquad
m^*(A)=\inf_{O\supset A,\ O\text{ open}}m(O).
\]
It proves countable subadditivity by finite compact-cover decomposition; proves the Carathéodory splitting inequality for every open set by a nearly maximizing compact subset; and proves finiteness on compact sets, outer regularity on Borel sets and inner regularity on open sets. Invariance transfers through the compact and open envelopes to every Borel set. The resulting measure \(\mu\) has \(1\le\mu(K_0)<\infty\), and every nonempty open set has positive measure because finitely many translates of a compact neighborhood inside that set cover \(K_0\).

These are the complete linked proofs, including the Borel conversion, rather than an invocation of an unspecified measure theorem. The proof does not need Haar uniqueness, a modular function, a product-measure theorem or a Riesz representation theorem. For the current second-countable group, relatively compact members of a countable base cover \(G\); their finite unions \(\Omega_n\) increase to \(G\) and have finite measure. Thus this particular Haar measure is sigma-finite.

The Borel measure may be completed without changing \(L^2\). Explicitly, a completed measurable set differs from a Borel set by a subset of a Borel null set. Replace the sets in countably many simple approximants to a completed measurable function by their Borel representatives. Outside the union of the resulting Borel null sets the approximants are unchanged, so their limit is a Borel representative of the same function. Norms and almost-everywhere classes are preserved. Left translations preserve null Borel sets and therefore preserve the completed measure too.

The human method comparison is Fremlin's author-supplied [2013 §441C(b–f) and §441E](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt441.tex). Its invoked §416M is replaced by the complete programme Lemma 8.4. For the left-translate separation test the expression required is \(u^{-1}v\), as (CO1.1) states; the two differing product orders in the supplied §441E do not enter our proof. Fremlin's source retains the Design Science License; no human-source expression is relabelled CC0.

<a id="co2-whole-l2-and-regular-representation"></a>

## CO2. The entire \(L^2\) space and regular representation

[Measure and Hilbert space tools, Sections 1–3](../../harmonic-analysis-on-locally-compact-groups/src/measure-and-hilbert-space-tools.md) prove measurable sequential limits, the simple-function integral, monotone convergence, Fatou and dominated convergence, and \(L^p\) completeness and simple approximation. For \(p=2\), the scalar inequality used in Hölder is just \(2ab\le a^2+b^2\). Applying it to normalized functions gives Cauchy–Schwarz; expanding a square gives Minkowski. The completeness proof selects a subsequence with summable norm differences, integrates the nonnegative increasing partial sums of their absolute values, and bounds every limiting tail by the summable tail of those norms. This supplies the complete Hilbert space with our pairing \(\langle f,h\rangle=\int\overline f h\,d\mu\).

We spell out the regularity and density arguments needed here. For a Borel set \(E\) of finite measure, choose open \(O\supset E\) with \(\mu(O\setminus E)<\varepsilon\). Cover \(O\setminus E\) by an open \(W\) with \(\mu(W)<\varepsilon\), and choose compact \(F\subset O\) with \(\mu(O\setminus F)<\varepsilon\). Then \(K=F\setminus W\subset E\) is compact and \(\mu(E\setminus K)<2\varepsilon\). Outer regularity and CO0.3 therefore give \(K\subset E\subset O'\) and \(f\in C_c(G)\) with
\[
|f-1_E|\le1_{O'\setminus K},\qquad
\|f-1_E\|_2^2\le\mu(O'\setminus K).
\tag{CO2.1}
\]
Simple approximation now proves density of \(C_c(G)\) in the whole \(L^2(G,\mu)\). The completed-measure representative argument in CO1 covers its completion.

For separability, use the relatively compact countable base and finite-measure increasing open cover \(\Omega_n\) from CO1. For \(E\subset\Omega_n\) Borel, choose compact \(K\subset E\) and open \(O\supset E\) with arbitrarily small \(\mu(O\setminus K)\). A finite union \(B\) of base members covers \(K\) and lies in \(O\). Then
\[
\mu\bigl(E\mathbin{\triangle}(B\cap\Omega_n)\bigr)
\le\mu(O\setminus K).
\]
There are only countably many such finite unions and indices. Their indicators, combined with rational complex coefficients, are a countable dense family, by simple approximation and truncation to \(\Omega_n\). This proves separability without an unproved monotone-class theorem.

Left invariance gives unitary operators
\[
\lambda(g)f(t)=f(g^{-1}t),\qquad
\lambda(g)\lambda(h)=\lambda(gh).
\tag{CO2.2}
\]
The identities follow first for indicators, then simple functions and their \(L^2\) limits. No modular multiplier occurs because these are left translations against left Haar measure.

For \(f\in C_c(G)\), restrict \(g\) near the identity to a compact neighborhood \(C\). The translated supports lie in the compact set \(C\operatorname{supp}f\). Joint continuity of \(f(g^{-1}t)-f(t)\), which is zero at \((e,t)\), gives uniform convergence to zero on that compact set: choose a product neighborhood for each \(t\), retain finitely many of their second-coordinate neighborhoods, and intersect their first-coordinate neighborhoods. Compact finiteness then gives \(L^2\) convergence. Density of \(C_c(G)\) and the common unitary bound extend it to every vector, for arbitrary parameter nets. The representation law gives continuity at every \(g\).

For \(g\ne e\), separate \(e\) and \(g\) by disjoint neighborhoods and use (CO0.2) and continuity of multiplication to choose a nonempty relatively compact open \(V\) with \(V\cap gV=\varnothing\). Its measure is positive and finite. Thus
\[
\xi=\mu(V)^{-1/2}1_V,\qquad
\|\lambda(g)\xi-\xi\|^2=2.
\tag{CO2.3}
\]
Faithfulness follows. This works for finite, discrete, noncompact and nonunimodular groups; no right translation was substituted.

<a id="co3-complete-tracial-car-action"></a>

## CO3. The full tracial CAR construction and normal action

Let \(K\) be separable infinite dimensional, with orthonormal basis \(e_1,e_2,\ldots\). SS2 constructs the entire tracial product \(R=\overline{\bigotimes}_{j\ge1}(M_2,\operatorname{tr}_2)\), with faithful normal trace, increasing finite matrix stages, separable trace Hilbert space, factoriality and no minimal projection. Thus it is the separable AFD \(\mathrm{II}_1\) factor. In its norm-closed local algebra \(A\), set
\[
Z_j=e_{11}^{(j)}-e_{22}^{(j)},\qquad
c_j=Z_1\cdots Z_{j-1}e_{12}^{(j)}.
\tag{CO3.1}
\]
The local matrix identities \(Z_je_{12}^{(j)}=e_{12}^{(j)}\) and \(e_{12}^{(j)}Z_j=-e_{12}^{(j)}\) give
\[
c_jc_k+c_kc_j=0,\qquad
c_jc_k^*+c_k^*c_j=\delta_{jk}1 .
\]
For \(j<k\), the sign comes from the single \(Z_j\) in the later parity string; all other different-site factors commute. The one-site relation is the sum of the two complementary matrix projections.

For a finite vector \(f=\sum_j f_je_j\), put \(a(f)=\sum_j\overline{f_j}c_j\). It is conjugate-linear and satisfies
\[
a(f)^2=0,\qquad a(f)^*a(f)+a(f)a(f)^*=\|f\|^21.
\]
For \(f\ne0\), \(p=a(f)^*a(f)/\|f\|^2\) is a projection: multiply the second relation on the left by \(a(f)^*\) and on the right by \(a(f)\), and use the square-zero identities. It is nonzero, since otherwise both \(a(f)\) and its adjoint would vanish, contradicting that relation. The norm of a nonzero projection is one. Hence
\[
\|a(f)\|=\|f\|.
\tag{CO3.2}
\]
This extends \(a\) in norm to every \(f\in K\), preserving all CAR relations by limits. Conversely \(a(e_j)=c_j\) recovers \(Z_j=1-2c_j^*c_j\) and \(e_{12}^{(j)}=Z_1\cdots Z_{j-1}c_j\), so these fields generate the whole \(A\).

For any finite-dimensional subspace \(E\subset K\), choose an orthonormal basis \(f_1,\ldots,f_d\), put \(n_i=a(f_i)^*a(f_i)\), and use \(b_i=(1-2n_1)\cdots(1-2n_{i-1})a(f_i)\). The CAR make \(1-2n_i\) anticommute with its own annihilator and commute with every other mode. The two resulting sign changes show that the \(b_i,b_i^*\) commute between distinct indices. At each index
\[
b_i^2=0,\qquad b_i^*b_i=n_i,\qquad b_ib_i^*=1-n_i.
\]
Thus \(1-n_i,b_i,b_i^*,n_i\) are a full one-mode matrix-unit system. Multiplying the commuting systems gives a unital star homomorphism \(M_{2^d}\) onto the generated algebra. Its kernel is zero: a nonzero ideal in a full matrix algebra contains, by multiplying a nonzero entry on the left and right by matrix units, a matrix unit and then all matrix units. A unital homomorphism cannot have that kernel. The faithful C*-norm criterion in CF proves isometry. This establishes the entire finite-mode algebra and its universal generator map, including arbitrary overlaps of subspaces.

A unitary \(u\) sends the finite family in \(E\) to that in \(uE\), giving an isometric star isomorphism \(\alpha_u\) on these finite-mode algebras. The maps agree on inclusions because they agree on every field generator. Their union is dense in \(A\), so they extend to the whole norm-complete \(A\), with inverse \(\alpha_{u^*}\), and
\[
\alpha_u(a(f))=a(uf),\qquad \alpha_u\alpha_v=\alpha_{uv}.
\tag{CO3.3}
\]
Every tracial state on a full matrix algebra has zero off-diagonal values and equal diagonal values: use \(e_{ii}e_{ij}=e_{ij}\), \(e_{ij}e_{ii}=0\), and \(e_{ij}e_{ji}=e_{ii}\), \(e_{ji}e_{ij}=e_{jj}\). Its normalization fixes those values to the reciprocal dimension. Thus the trace on \(A\) is unique on each finite mode and then on the dense union; \(\tau\alpha_u=\tau\).

On \(L^2(R,\tau)\), the formula \(W_u(x\Omega)=\alpha_u(x)\Omega\) on \(A\Omega\) is isometric and has inverse \(W_{u^*}\). Its unitary extension conjugates \(A\) onto itself and therefore conjugates its whole bicommutant \(R\) onto itself. CP proves this conjugation normal on all of \(R\). Its inverse is normal as well, and (CO3.3) holds on the whole algebra. If \(\alpha_u\) is the identity, (CO3.2) gives \(uf=f\) for every \(f\), so the map is injective.

Suppose \(u_i\to u\) strongly in the unitary group. The identity (CO3.2) proves norm convergence of the transformed fields, and finite product telescoping proves convergence on all finite field polynomials. Norm density and the common isometry bound give it on all \(A\). Consequently \(W_{u_i}\to W_u\) strongly on the whole trace Hilbert space. Also
\[
\|(u_i^*-u^*)f\|=\|f-u_i u^*f\|\longrightarrow0 ,
\]
so the same argument gives strong convergence of the \(W\)-adjoints.

CP identifies every normal functional on this concrete \(R\) as a square-summable vector-pair series \(\psi(x)=\sum_n\langle\xi_n,x\eta_n\rangle\). Its pullback by \(\alpha_{u_i}\) replaces the two lists by \(W_{u_i}^*\xi_n,W_{u_i}^*\eta_n\). Their differences tend to zero in square-sum norm: use strong convergence on finitely many vectors and bound the omitted differences by twice each vector norm. Hence
\[
\|\psi\alpha_{u_i}-\psi\alpha_u\|
\le
\|((W_{u_i}^*-W_u^*)\xi_n)_n\|_{\ell^2}\|(\eta_n)_n\|_{\ell^2}
+
\|(\xi_n)_n\|_{\ell^2}\|((W_{u_i}^*-W_u^*)\eta_n)_n\|_{\ell^2}
\longrightarrow0 .
\tag{CO3.4}
\]
This is whole point-predual norm continuity for nets, not only convergence on polynomial or bounded trace-vector tests.

If \(K\) has dimension \(d<\infty\), the same construction is \(M_{2^d}\); if \(K=0\), it is \(\mathbb C\). The infinite repetition used in the main lesson ensures that its \(K\) is always separable infinite dimensional.

<a id="co4-whole-hilbert-schmidt-innerness"></a>

## CO4. The whole complex-linear Hilbert–Schmidt criterion

We prove precisely the factor criterion used by the current lesson. It applies to every unitary on the separable infinite-dimensional complex \(K\) of CO3.

First suppose \(uf_j=e^{is_j}f_j\) on an orthonormal basis. In the commuting coordinates of CO3, \(b_j\) transforms by \(e^{-is_j}\), because \(a\) is conjugate-linear, and its occupation projection \(n_j\) is fixed. Define
\[
w_j=e^{-is_j/2}(1-n_j)+e^{is_j/2}n_j,\qquad
\tau(w_j)=\cos(s_j/2).
\tag{CO4.1}
\]
Matrix multiplication gives \(\alpha_u|_{M_2^{(j)}}=\operatorname{Ad}w_j\).

Here is the whole tracial product criterion. Adjust scalar phases of the \(w_j\)'s so \(r_j=\tau(w_j)\ge0\), and put \(v_m=w_1\cdots w_m\). If \(\alpha_u=\operatorname{Ad}v\) with \(v\in R\) unitary, then \(v_m^*v\) commutes with the first \(m\) matrix factors. FH3's entire tail-commutant identification puts it in the tail. The normal finite trace projection \(E_m\) from AF1 is therefore
\[
E_m(v)=a_m v_m,\qquad a_m=\tau(v_m^*v).
\]
Bounded finite-stage trace approximation gives \(E_m(v)\to v\) in \(L^2\), so \(|a_m|\to1\). For \(l>m\), the expectation tower and product trace give
\[
a_m=a_l\prod_{j=m+1}^l r_j.
\]
Choose \(m\) with \(|a_m|>0\). Every later overlap is positive, and, since \(|a_l|\le1\),
\[
\sum_{j=m+1}^l(1-r_j)
\le\sum_{j=m+1}^l(r_j^{-1}-1)
\le\left(\prod_{j=m+1}^l r_j\right)^{-1}-1
\le |a_m|^{-1}-1.
\tag{CO4.2}
\]
The first inequality is \(r^{-1}-1=(1-r)/r\ge1-r\). The second follows by expanding the finite product of \(1+(r_j^{-1}-1)\): all terms are nonnegative, so it is at least one plus their sum. The last follows from \(\prod r_j=|a_m|/|a_l|\ge|a_m|\). Every partial sum is bounded, proving summability without a logarithmic inequality.

Conversely, if \(\sum_j(1-r_j)<\infty\), for a local vector \(x\Omega\) and \(l>m\) beyond its support,
\[
\|(v_l-v_m)x\Omega\|^2
=2\|x\Omega\|^2\left(1-\prod_{j=m+1}^l r_j\right)
\le2\|x\Omega\|^2\sum_{j>m}(1-r_j).
\]
The same formula holds for adjoints. Density and the common unitary bound give whole strong limits of both \(v_m\) and \(v_m^*\). Multiplying their bounded limits shows they are mutually inverse, hence the limit is a unitary of \(R\). Its conjugation has the desired action on every finite stage and then normally on all \(R\). A finite prefix, including finitely many zero overlaps, imposes no tail obstruction.

With \(t_j=|\cos(s_j/2)|\),
\[
4(1-t_j)\le |e^{is_j}-1|^2
=4(1-t_j)(1+t_j)\le8(1-t_j).
\tag{CO4.3}
\]
Thus this complete product argument identifies diagonal innerness exactly with \(u-1\) being Hilbert–Schmidt.

To pass to arbitrary \(u\), the complete [Bogoliubov analytic proofs, Sections 6.1–6.5](../src/bogoliubov-automorphisms-and-innerness.md#6-complete-analytic-support-for-the-proof-route) supply the following whole constructions. The square-sum matrix description proves Hilbert–Schmidt completeness, basis independence, two-sided ideal estimates and finite-rank density. The compact self-adjoint quadratic-form maximum argument gives a full eigenbasis, including the kernel; commuting real and imaginary compact parts therefore diagonalize any compact normal operator. Continuous positive-part support limits supply nested interval projections. The [complete scalar period proof](../src/car-fock-and-quasifree-states.md#17-1-the-elementary-scalar-period-including-the-meaning-of-2-pi) and continuous calculus construct a bounded self-adjoint logarithm \(h\), \(\|h\|\le\pi\), \(u=e^{ih}\), including the \(-1\) eigenspace.

The dyadic construction in Section 6.5 is the entire required perturbation proof. In each reducing cyclic component, its initial interval vectors and subsequent parent-interval increments form a complete orthonormal basis. Their midpoint errors have full squared sum bounded by \(3M^2 2^{-N}\) for \(M>\|h\|\). Choosing the starting depths independently over the countably many cyclic components makes the total error smaller than any prescribed \(\varepsilon^2\). The diagonal midpoint operator \(d\) is bounded self-adjoint; \(k=d-h\) is self-adjoint Hilbert–Schmidt with \(\|k\|_{\mathrm{HS}}<\varepsilon\), and \(h+k=d\) has a whole eigenbasis. These are full linked arguments, without a Borel spectral theorem or an unbounded diagonal-perturbation premise.

For clarity, only bounded generators are needed here, and their exponential estimate has this complete proof. For bounded self-adjoint \(h,k\), differentiate their norm-convergent exponential series and the product
\(F(s)=e^{-ish}e^{is(h+k)}\). The derivative is
\[
F'(s)=i e^{-ish}k e^{is(h+k)}.
\]
The integrand is continuous in Hilbert–Schmidt norm by the two-sided ideal bound and norm continuity of the bounded exponentials. The entire [tagged-integral and Banach fundamental theorem proofs, R03–R04](../src/elementary-calculus-for-infinite-products.md#r03), give convergence of the sums in that complete space and identify the integral of the continuous derivative with the endpoint difference. The norm is at most the interval length times \(\|k\|_{\mathrm{HS}}\); hence
\[
e^{-ih}e^{i(h+k)}-1
=i\int_0^1e^{-ish}k e^{is(h+k)}\,ds,\qquad
\|e^{-ih}e^{i(h+k)}-1\|_{\mathrm{HS}}\le\|k\|_{\mathrm{HS}}.
\tag{CO4.4}
\]
Set \(v=e^{-ih}e^{i(h+k)}\), \(w=uv=e^{i(h+k)}\). Then \(v-1\) is Hilbert–Schmidt and compact. Since \(v\) is unitary, \(v-1\) is normal, so its complete compact diagonalization gives an eigenbasis for \(v\). The diagonal criterion already proved makes \(\alpha_v\) inner. The unitary \(w\) is diagonal on the eigenbasis of \(h+k\), so
\[
\alpha_u\text{ inner}\iff\alpha_w\text{ inner}
\iff w-1\text{ Hilbert--Schmidt}
\iff u-1\text{ Hilbert--Schmidt}.
\tag{CO4.5}
\]
The first equivalence uses \(\alpha_w=\alpha_u\alpha_v\) and the subgroup of inner automorphisms. The last uses
\(w-1=(u-1)+u(v-1)\) and the linear ideal estimate. Thus neither direction assumes the desired criterion for the original arbitrary \(u\).

The broader real-Clifford comparison does not add another branch to (CO4.5). A complex-linear \(u\), regarded as real, has real \(\pm1\) eigenspaces invariant under multiplication by \(i\); if finite, their dimensions are even. The negative real branch in Blattner and Carey requires an odd-dimensional \(+1\) eigenspace and is excluded. For a complex-linear Hilbert–Schmidt operator, using the real orthonormal basis \(e_j,ie_j\) shows that its squared real Hilbert–Schmidt norm is twice its squared complex norm. This explains the comparison; the local proof above does not import the broader real criterion.

<a id="co5-full-repetition-and-transport"></a>

## CO5. Repetition, full topology transport and the endpoint cases

For a faithful strongly continuous representation \(\lambda\) on nonzero separable \(H_0\), let \(K=\bigoplus_{n\ge1}H_0\), \(U(g)=\bigoplus_n\lambda(g)\). It is separable infinite dimensional. For a vector \(\eta=(\eta_n)\), retain finitely many summands so the remaining squared norm is small. The squared difference on that tail is at most \(4\sum_{n>N}\|\eta_n\|^2\), while the finite prefix tends to zero by strong continuity. This proves continuity on every vector, for parameter nets.

If \(g\ne e\), choose a unit vector \(\xi\) with \(\|(\lambda(g)-1)\xi\|=c>0\). The orthonormal \(\xi\otimes e_n\)'s have mutually orthogonal images of norm \(c\). Completing them to an orthonormal basis gives an infinite Hilbert–Schmidt square sum. Their images have no convergent subsequence, so \(U(g)-1\) is also noncompact. In the regular construction CO2.3 gives the exact \(c=\sqrt2\).

CO3–4 consequently give a trace-preserving continuous injective homomorphism into \(\operatorname{Aut}(R)\) with every nonidentity element outer. AF5's entire separable AFD \(\mathrm{II}_1\) uniqueness proof supplies a normal isomorphism \(\theta:R\to R_0\) for every target factor in that scope. Its full normal inverse is part of that proof. Pullback by \(\theta\) is an isometry of the entire preduals, so
\[
\|\psi\theta\alpha\theta^{-1}-\psi\theta\alpha'\theta^{-1}\|
=\|(\psi\theta)\alpha-(\psi\theta)\alpha'\|.
\]
The analogous identity for \(\theta^{-1}\) proves both directions of the topology homeomorphism. A unitary implementer is transported by \(\theta\), or pulled back by its inverse, so outerness is preserved.

For a finite group the unrepeated regular space is finite dimensional, and its CAR algebra is a finite full matrix algebra. A finite-dimensional change, even after adjoining an infinite unused trivial summand, has Hilbert–Schmidt difference and an inner CAR action. Repeating the nontrivial representation produces the required infinitely many displaced modes. For the trivial group \(H_0\) is one dimensional, but its countable repetition remains infinite dimensional; its CAR factor is still \(\mathrm{II}_1\), and the assertion about nonidentity elements is vacuous. No amenability, connectedness or unimodularity condition enters these arguments.
