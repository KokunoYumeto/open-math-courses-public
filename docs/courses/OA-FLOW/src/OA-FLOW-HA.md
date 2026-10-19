# The same hyperfinite factor from different return systems


<a id="ha-result"></a>
## 1. The assertion and its exact scope

Let \(R\) be the tracial infinite tensor product of countably many copies of \(M_2(\mathbb C)\), and put \(R_\infty=R\bar\otimes B(\ell^2(\mathbb N))\). Let \(T_0x=x+\alpha\) on the circle with normalized Lebesgue measure, where \(\alpha\notin\mathbb Q\). Let \((T_1x)_j=x_{j+1}\) on \(\{0,1\}^{\mathbb Z}\) with the fair product probability. Write these standard probability spaces as \((X_i,\mu_i)\), and set
\[
 D_i=L^\infty(X_i,\mu_i),\quad \beta_i(f)=f\circ T_i^{-1},\quad
 N_i=R_\infty\bar\otimes D_i,\quad
 \alpha_i=\operatorname{id}_{R_\infty}\bar\otimes\beta_i.
 \tag{HA1}
\]

**Theorem.** Each \(N_i\) has separable predual, is of type \(\mathrm{II}_\infty\), has nonatomic full center \(D_i\), and \(\alpha_i\) acts ergodically on that center. There are normal onto star isomorphisms with normal inverses
\[
 (N_i\rtimes_{\alpha_i}\mathbb Z,\widetilde\tau_i)
       \cong (R_\infty,\tau_R\otimes\operatorname{Tr}),\qquad i=0,1,
 \tag{HA2}
\]
where the traces are specified below. Nevertheless, for every pair of nonzero central projections \(e_i\in Z(N_i)\), the induced coefficient systems \(((N_i)_{e_i},(\alpha_i)_{e_i})\) are not conjugate. Neither \(N_i\) admits a faithful normal semifinite trace contracted uniformly by \(\alpha_i\) with a constant strictly below one.

These systems satisfy the three assumptions in the literal wider induced-corner assertion: type \(\mathrm{II}_\infty\), separable predual, and ergodic action on a nonatomic center. They refute its converse. They are outside the trace-contraction hypothesis of the type \(\mathrm{III}_0\) classification. The classification under the trace-contraction hypothesis and the forward implication from induced conjugacy retain their stated scopes.

The construction combines injectivity of an amenable crossed product with finite-factor classification. Sections 3 and 4 identify the earlier programme proofs used for these two steps. It gives a second realization of the obstruction in [the induced-corner lesson](OA-FLOW-IC.md#ic-obstruction), whose infinite-tensor absorption argument also remains available.

<a id="ha-mechanism"></a>
The table shows the objects and maps of the complete argument, with exact proof locators.

| Object or map | Mathematical role |
|---|---|
| \(D_i\subset A_i=D_i\rtimes_{\beta_i}\mathbb Z\) | The faithful normal coefficient expectation gives a normalized trace; (HA4)–(HA8). |
| Abelian injectivity and an invariant mean on \(\mathbb Z\) | Make \(A_i\) injective; the retraction can be singular; Section 3. |
| \(\gamma_i:A_i\to R\) | Finite injective-factor classification, exact dyadic containment and a trace-GNS unitary; (HA13)–(HA15). |
| \(J:R\bar\otimes R\to R\) | First input occupies odd tensor positions, second occupies even positions; the inverse separates them; (HA16)–(HA19). |
| \(N_i\rtimes\mathbb Z\to R_\infty\) | Regular tensor rearrangement, \(\gamma_i\) and \(J\), retaining the matrix leg; (HA20)–(HA23). |
| Induced center transformation on \(E_i\) | Normalized entropy is \(0\) or \(\log2/\mu_1(E_1)>0\); (HA24)–(HA25). |

<a id="ha-inline-figure"></a>
![Odd and even tensor positions give the full trace-preserving absorption map and its inverse.](../assets/hyperfinite-output/tensor-interleaving.svg)

The displayed six positions are a finite window of the bijection (HA16); the dots continue through all positive integers. The diagram displays tensor positions, not a spatial projection of an operator. Equations (HA17)–(HA19) prove that the reversible local rule extends to the full normal trace-preserving isomorphism. The [editable SVG](../assets/hyperfinite-output/tensor-interleaving.svg) is the complete figure source; it uses no human source image.

<a id="ha-models"></a>
## 2. The systems and their finite crossed products

[OA-FLOW-IE, Section 8](OA-FLOW-IE.md#IE-examples) proves that both \(T_i\) are invertible, probability preserving, ergodic, essentially free and nonatomic. It constructs the Bernoulli probability from its finite cylinder values. Rotation ergodicity uses the dense cyclic subgroup and continuity of translation in \(L^2\); shift ergodicity follows from cylinder independence and mixing. It proves
\[
 h_{\mu_0}(T_0)=0,\qquad h_{\mu_1}(T_1)=\log2.
 \tag{HA3}
\]

Represent \(D_i\) on \(H_i=L^2(X_i,\mu_i)\). On \(\ell^2(\mathbb Z)\otimes H_i\), define
\[
 [\pi_i(f)\xi](k)=\beta_i^{-k}(f)\xi(k),\qquad
 [u_i\xi](k)=\xi(k-1),\qquad A_i=\{\pi_i(D_i),u_i\}''.
 \tag{HA4}
\]
The normality and representation-independence theorem [NR3–4](OA-FLOW-NR.md#oa-flow.nr.3) applies, including its arbitrary-net proof. In the discrete case normality also follows entry by entry from the normal automorphisms \(\beta_i^{-k}\).

Compression to coordinate zero defines \(E_i:A_i\to D_i\). Its range assertion follows by bounded strong-star approximation by covariant polynomials, whose zero entries lie in the ultraweakly closed multiplication algebra. It is normal, positive, unital and \(D_i\)-bimodular. For \(X\in A_i\), put \(\widehat X(n)=E_i(Xu_i^{-n})\). Calculation on polynomials followed by normality gives
\[
 X_{k,l}=\beta_i^{-k}(\widehat X(k-l)).
 \tag{HA5}
\]
Thus all coefficients determine \(X\). If \(X\ge0\) and \(E_i(X)=0\), every diagonal entry vanishes. The square root \(X^{1/2}\) kills all coordinate vectors, so \(X=0\). This proves faithfulness without requiring convergence of a Fourier series.

The state
\[
 \tau_i(X)=\int_{X_i}E_i(X)\,d\mu_i
 \tag{HA6}
\]
is faithful and normal. It is tracial: for words \(fu_i^n\) and \(gu_i^m\), both expectations vanish if \(n+m\ne0\); when \(m=-n\), invariance gives
\(\int f\beta_i^n(g)\,d\mu_i=\int\beta_i^{-n}(f)g\,d\mu_i\).
Fix one word and use normality to extend equality to every second argument, then extend in the first variable. Hence the state is tracial on the full algebra.

If \(X\) commutes with \(D_i\), bimodularity gives
\[
 (d-\beta_i^n(d))\widehat X(n)=0\qquad(d\in D_i).
 \tag{HA7}
\]
A countable Borel separating family of indicators forces the support of \(\widehat X(n)\), for \(n\ne0\), into the null fixed-point set of \(T_i^n\). Equation (HA5) gives \(X=E_i(X)\in D_i\). Consequently
\[
 D_i'\cap A_i=D_i,\qquad Z(A_i)=D_i^{\beta_i}=\mathbb C1.
 \tag{HA8}
\]
The diffuse algebra \(D_i\) cannot embed in a finite-dimensional algebra, since it has arbitrarily large finite families of nonzero orthogonal projections. Thus the finite factor \(A_i\) is \(\mathrm{II}_1\). Its regular Hilbert space is separable, and restriction of trace-class functionals gives a separable predual. These verify the hypotheses of the finite-factor theorem apart from injectivity, which we prove next.

<a id="ha-injectivity"></a>
## 3. Injectivity from finite partitions and averaging

**Abelian case without countability restrictions.** Let \(D\subset B(H)\) be any faithfully normally represented nonzero abelian von Neumann algebra. Direct its finite partitions \(\mathcal P=(p_1,\ldots,p_m)\) of the identity by refinement, omitting zero pieces. Choose unit vectors \(\xi_j\in p_jH\) and put
\[
 F_{\mathcal P}(x)=\sum_j\langle x\xi_j,\xi_j\rangle p_j\qquad(x\in B(H)).
 \tag{HA9}
\]
The inner product is linear in its first variable. Each coordinate is a vector state, so this map is ucp and fixes \(D_{\mathcal P}=\operatorname{span}\{p_j\}\). Contractivity gives
\[
 \|F_{\mathcal P}(d)-d\|\le2\inf_{b\in D_{\mathcal P}}\|d-b\|\qquad(d\in D).
 \tag{HA10}
\]
Joint finite spectral partitions approximate each finite family in \(D\) in norm, and finer partitions retain the approximants. Hence \(F_{\mathcal P}(d)\to d\) in norm for every \(d\in D\). Product ultraweak compactness of the norm balls of \(D\) supplies a subnet converging at every \(x\in B(H)\). Its limit is linear, unital and completely positive, since matrix positive cones are ultraweakly closed. It has range in \(D\) and fixes \(D\). The ucp retraction criterion in [Finite models of a von Neumann algebra](../../OA-APPROX/semidiscrete-finite-models.html#4-the-finite-models-give-an-extension-property), Proposition 4.1, proves injectivity. There was no separability or faithful scalar state assumption. The limiting retraction need not be normal.

This independently proves the abelian case of Averaging, crossed products, and injectivity, Proposition 5.3. Its more general type I conclusion is not required here.

<a id="ha-finite-retraction"></a>
### A direct retraction for the probability-preserving integer action

For the finite crossed products in (HA4), the retraction can be constructed on their actual regular Hilbert spaces. Fix one system and omit its subscript. Thus \(D=L^\infty(S,\mu)\), \(\mu(S)=1\), \(\beta\) preserves \(\mu\), and \(A=D\rtimes_\beta\mathbb Z\) has the faithful normal trace \(\tau=\mu E\) proved in Section 2. Neither ergodicity nor freeness is needed for the construction below.

Let \(H_0=L^2(S,\mu)\), \(H=\ell^2(\mathbb Z)\otimes H_0\), and \(V_s:H_0\to H\) be the inclusion into coordinate \(s\). The finite-partition construction (HA9)–(HA10) gives a ucp retraction
\[
 P:B(H_0)\longrightarrow D.
 \tag{HAFR1}
\]
It fixes every multiplication operator in \(D\), although it need not be normal. For \(n\ge0\), put \(F_n=\{-n,\ldots,n\}\) and \(N_n=2n+1\). Define
\[
 \begin{aligned}
 C_n(T)&=[P(V_s^*TV_t)]_{s,t\in F_n},
       &&T\in B(H),\\
 \Gamma_n([d_{st}])&=\frac1{N_n}
       \sum_{s,t\in F_n}u^s\pi(d_{st})u^{-t},
       &&[d_{st}]\in M_{F_n}(D),\\
 R_n&=\Gamma_n C_n:B(H)\longrightarrow A.
 \end{aligned}
 \tag{HAFR2}
\]
Compression by the isometry \(\bigoplus_{s\in F_n}V_s\) is ucp, and entrywise application of \(P\) is its matrix amplification. Hence \(C_n\) is ucp. To check the second map at every matrix level, represent \(M_{F_n}(D)\) on \(H^{F_n}\) entrywise by \(\pi\), and use the row operator
\[
 W_n=N_n^{-1/2}[u^s]_{s\in F_n}:H^{F_n}\longrightarrow H,
 \qquad W_nW_n^*=1.
\]
Then \(\Gamma_n(d)=W_n[\pi(d_{st})]W_n^*\). Thus \(\Gamma_n\), and consequently \(R_n\), is ucp. Its range lies in \(A\) by the finite sum in (HAFR2). In particular \(\|R_n(T)\|\le\|T\|\).

**The coefficient calculation.** For \(X\in A\), every \(V_s^*XV_t\) already belongs to \(D\), by (HA5), so \(P\) fixes it. Therefore the restriction \(R_n|_A\) is normal: it is a finite sum of normal coordinate compressions, normal applications of \(\pi\), and fixed left and right multiplications. For a covariant word, (HA4) gives
\[
 V_s^*\pi(f)u^rV_t
   =1_{\{s-t=r\}}\beta^{-s}(f).
\]
The covariance relation \(u^s\pi(\beta^{-s}(f))=\pi(f)u^s\) now gives the exact multiplier
\[
 R_n(\pi(f)u^r)
   =q_n(r)\pi(f)u^r,\qquad
 q_n(r)=\frac{|F_n\cap(F_n+r)|}{N_n}
       =\max\left(1-\frac{|r|}{N_n},0\right).
 \tag{HAFR3}
\]
Indeed there are \(N_n-|r|\) pairs with \(s-t=r\) when \(|r|<N_n\), and none otherwise. In particular \(q_n(r)\to1\) for each fixed integer \(r\).

**Trace and whole-algebra convergence.** For \(d\in D\),
\[
 \tau(u^s\pi(d)u^{-t})
   =1_{\{s=t\}}\int_S d\,d\mu.
\]
When \(s=t\), invariance of \(\mu\) removes \(\beta^s\); when \(s\ne t\), the zero Fourier coefficient vanishes. Applying this identity to (HAFR2) and using (HA5) gives, for every \(X\in A\),
\[
 \tau(R_n(X))
   =\frac1{N_n}\sum_{s\in F_n}
        \int_S\beta^{-s}(E(X))\,d\mu
   =\tau(X).
 \tag{HAFR4}
\]
Thus the full restriction, not just its polynomial part, preserves the trace.

A ucp map \(L\) satisfies \(L(x)^*L(x)\le L(x^*x)\). In this instance the inequality follows directly by applying its two-by-two amplification to the positive Gram matrix
\(\left[\begin{smallmatrix}x^*x&x^*\\x&1\end{smallmatrix}\right]\)
and evaluating the resulting quadratic form on \((\xi,-L(x)\xi)\).
Together with (HAFR4), this gives
\[
 \|R_n(X)\|_2\le\|X\|_2.
 \tag{HAFR5}
\]

Let \(\Omega\in H\) have value \(1\in L^2(S,\mu)\) at coordinate zero and zero elsewhere. For \(X\in A\), the definition of \(E\) gives
\(\langle X\Omega,\Omega\rangle=\tau(X)\); hence
\(\|X\Omega\|=\|X\|_2\). The word \(\pi(f)u^r\Omega\) has only coordinate \(r\), with value \(\beta^{-r}(f)\). Bounded functions are dense in \(L^2(S,\mu)\), so these word vectors span a dense subspace of \(H\). This proves directly that this is the full trace-GNS representation and that covariant polynomials are \(2\)-norm dense in \(A\).

For such a polynomial \(Y\), (HAFR3) gives
\(\|R_n(Y)-Y\|_2\to0\). For arbitrary \(X\in A\), (HAFR5) gives
\[
 \|R_n(X)-X\|_2
 \le2\|X-Y\|_2+\|R_n(Y)-Y\|_2.
\]
First choose \(Y\) close in \(2\)-norm and then let \(n\) increase. We obtain convergence for every \(X\in A\).

This implies ultraweak convergence in the actual representation, with no assumption that a Fourier series converges in operator norm. Write \(a_n=R_n(X)-X\). For \(y,z\in A\), traciality and Cauchy–Schwarz give
\[
 |\langle a_ny\Omega,z\Omega\rangle|
 =|\tau(z^*a_ny)|
 \le\|zy^*\|_2\,\|a_n\|_2\longrightarrow0.
 \tag{HAFR6}
\]
The uniform bound \(\|a_n\|\le2\|X\|\) extends this convergence from the dense vectors \(A\Omega\) to all vector pairs. For a normal functional written as a summable series of vector coefficients, a finite prefix tends to zero and its remaining tail is bounded uniformly by this same operator bound. Hence \(R_n(X)\to X\) ultraweakly.

Finally, the values \(R_n(T)\) lie in the ultraweakly compact ball of radius \(\|T\|\) of \(A\), for every \(T\in B(H)\). Product compactness supplies a subnet converging pointwise ultraweakly to a map
\[
 R:B(H)\longrightarrow A.
\]
Finite linearity and unit equations pass to the limit. Positivity at every matrix level passes by testing every finite vector tuple, so \(R\) is ucp. The whole-algebra convergence just proved gives \(R(X)=X\) for every \(X\in A\). This is a retraction in the very trace-GNS representation used for the finite-factor and hypertrace arguments. The retraction criterion already stated above proves injectivity. Normality of \(R\) is neither asserted nor needed. \(\square\)

For a concrete window, \(F_3=\{-3,-2,\ldots,3\}\) has seven points. The word of degree \(r=2\) contributes in exactly five matrix positions, so its multiplier is \(q_3(2)=5/7\). The diagonal degree has multiplier one, and degrees \(|r|\ge7\) have multiplier zero. These finite formulas illustrate the approximation; exact recovery of arbitrary \(X\in A\) uses (HAFR5)–(HAFR6) and the limiting retraction.

![Finite compression, five surviving degree-two entries, and reconstruction with exact multiplier five sevenths](../assets/hyperfinite-output/finite-window-retraction.svg)

**Finite-window retraction.** The grid lists the row and column indices of \(F_3\); a marked square has \(s-t=2\). The row-operator reconstruction in (HAFR2) assigns weight \(1/7\) to each of the five surviving entries, giving (HAFR3). The diagram displays one Fourier coefficient, not an operator-norm approximation of an arbitrary Fourier series. The [editable SVG](../assets/hyperfinite-output/finite-window-retraction.svg), [drawing script](../assets/hyperfinite-output/finite-window-retraction.py) and [exact finite data](../assets/hyperfinite-output/finite-window-retraction.json) accompany it.

**The general averaging argument.** The same conclusion also follows through commutants and an invariant mean, as follows.
The states
\[
 m_n(f)=\frac1{2n+1}\sum_{k=-n}^n f(k)\qquad(f\in\ell^\infty(\mathbb Z))
 \tag{HA11}
\]
have a weak-star cluster point. For each integer \(r\),
\( |m_n(f(\cdot+r))-m_n(f)|\le2|r|\|f\|_\infty/(2n+1)\).
The bound follows from the symmetric difference of the finite intervals. Every cluster point is therefore an invariant positive normalized mean, proving amenability of \(\mathbb Z\).

The crossed-product conclusion is Corollary 3.1 of Averaging, crossed products, and injectivity. Its proof proceeds as follows. If an injective \(P\subset B(K)\) is normalized by an amenable unitary representation \(v\), its commutant \(P'\) is injective by the lesson's full commutant theorem. For \(Q=\{P,v(G)\}''\),
\[
 Q'=(P')^{\operatorname{Ad}v}.
 \tag{HA12}
\]
An invariant mean defines a ucp retraction \(B:P'\to Q'\) by
\(\omega(Bx)=m_g\omega(v_gxv_g^*)\), \(\omega\in(P')_*\).
Matrix positivity follows by averaging positive scalar tests. Left invariance and normality of each conjugation put the range in the fixed algebra; every fixed element is fixed by the map. Composing with a retraction onto \(P'\) gives injectivity of \(Q'\), and commutant permanence gives injectivity of \(Q\). The commutant proof supplies its amplification, corner, opposite-algebra and normal-representation arguments; singular retractions are explicitly allowed.

Apply this to \(P=\pi_i(D_i)\), \(v_n=u_i^n\). Discreteness supplies continuity automatically. The faithful normal regular generators give \(Q=A_i\), so both \(A_i\) are injective. The crossed-product theorem retains arbitrary von Neumann algebras and amenable locally compact Hausdorff groups with point-ultraweakly continuous actions; this application only needs its discrete specialization.

<a id="ha-classification"></a>
## 4. The finite-factor theorem and its normal maps

We use the proved statement of [Unitary couplings and finite injective factors](../../OA-APPROX/unitary-couplings-and-finite-injective-factors.html#5-injective-finite-factors-are-locally-afd), Theorem 5.1: every injective \(\mathrm{II}_1\) factor is locally approximately finite dimensional; with separable predual it is normally isomorphic to \(R\). Here is the chain of earlier proofs:

1. [Hypertraces and finite injective algebras](../../OA-APPROX/hypertraces-finite-injectivity.html#2-a-hypertrace-with-a-prescribed-trace), Sections 1–5, starts with a prescribed faithful normal tracial state. A bimodular retraction gives a hypertrace with exactly that restriction. Trace-controlled finite-rank densities retain both the trace and approximate commutation. Finite product vectors give explicit normal ucp incoming matrix maps and cpc reconstruction maps, using the bounded correction \(w\mapsto\max(w,1)^{-1/2}\). This proves semidiscreteness directly in the finite tracial case; no continuous-core classification is needed.
2. Trace-preserving finite models, Sections 1–4, with [Tracial adjoints and rational matrix models](../../OA-APPROX/tracial-adjoints-and-rational-matrix-models.html#1-the-trace-adjoint-stays-completely-positive), Sections 1–3, perturbs the reconstruction density to strictly positive rational spectrum, realizes the rational weights by finite dimensions, and replaces contractions modeling prescribed unitaries by matrix unitaries. The weighted Hilbert adjoint uses a two-sided density sandwich. Both exact trace identities are retained.
3. [Balancing Kraus families and unitary couplings](../../OA-APPROX/balancing-kraus-families-and-unitary-couplings.html#1-filling-two-positive-defects), Lemma 1.1, Theorem 3.1 and Corollary 4.2, fills two positive defects with equal center-valued traces and supplies coupled matrix unitaries. The internal Kraus formula is Lemma 4.1 of [Properly infinite injective algebras and dyadic approximation](../../OA-APPROX/properly-infinite-injective-algebras-and-dyadic-approximation.html#4-a-finite-cp-reconstruction-is-one-compression): its finite Kraus conclusion requires no proper infiniteness.
4. [Unitary couplings](../../OA-APPROX/unitary-couplings-and-finite-injective-factors.html#1-sampling-a-countable-coupling), Sections 1–4, samples and clips the coupling, uses a faithfully tracial von Neumann ultrapower, tests every central projection in the intertwiner algebra, and compares its two diagonal projections. It produces one unitary \(w\) with all \(\|u_k-wv_kw^*\|_2\) small. The ultrapower is proved to be a von Neumann algebra in [Multiplier ultraproducts and normal embeddings](../../OA-APPROX/multiplier-ultraproducts-and-normal-embeddings.html#3-completeness-on-two-cyclic-vectors), Theorem 3.2. In the tracial case every bounded sequence is a multiplier. The proof does not assume that the ultrapower is a factor.
5. [Hyperfinite finite factors](../../OA-APPROX/hyperfinite-finite-factors.html#4-making-containment-exact), Lemmas 3.1 and 4.1 and Theorem 5.1, converts finite approximants into increasing dyadic matrix algebras with exact containment and constructs the normal trace-GNS isomorphism. Only the countable generating step requires separable predual.

<a id="ha-unital-normalization"></a>
### Strong-star approximation and the unitality defect

The matrix maps in step 1 can be made unital while retaining their approximation property. We prove this for an arbitrary von Neumann algebra \(M\). Let \(i\) run through a directed set, and suppose
\[
 S_i:M\longrightarrow M_{m_i},\qquad
 T_i:M_{m_i}\longrightarrow M,\qquad
 \Phi_i=T_iS_i,
 \tag{HAU1}
\]
where \(S_i\) is normal, unital and completely positive, and \(T_i\) is completely positive and contractive. Assume \(\Phi_i(x)\to x\) ultraweakly for every \(x\in M\). The dimensions \(m_i\) may vary, and no separability or tracial hypothesis is needed in this deduction.

For a positive normal functional \(\psi\), write
\[
 p_\psi(z)=\psi(z^*z)^{1/2},\qquad
 D_i=1-T_i(1)=1-\Phi_i(1),\qquad
 d_{i,\psi}=\psi(D_i).
 \tag{HAU2}
\]
The two seminorms \(p_\psi(z)\) and \(p_\psi(z^*)\), as \(\psi\) varies, define the intrinsic \(\sigma\)-strong-star topology. Positivity and contractivity give \(0\le D_i\le1\). Ultraweak convergence at the identity gives \(d_{i,\psi}\to0\).

**First, the uncorrected maps converge in both seminorms.** A completely positive contraction \(\Phi\) satisfies
\[
 \Phi(x)^*\Phi(x)\le\Phi(x^*x).
 \tag{HAU3}
\]
Indeed apply its size-two amplification to the positive Gram block
\(\left[\begin{smallmatrix}x^*x&x^*\\x&1\end{smallmatrix}\right]\).
Add the positive block with bottom-right entry \(1-\Phi(1)\) and other entries zero. The resulting block has bottom-right entry one. Its sandwich by the column \(\left[\begin{smallmatrix}1\\-\Phi(x)\end{smallmatrix}\right]\) is \(\Phi(x^*x)-\Phi(x)^*\Phi(x)\), proving (HAU3). Positive linear maps preserve adjoints, since every selfadjoint element is a difference of positive elements.

Define the nonnegative error
\[
 e_{i,\psi}(x)=
 \bigl|\psi(\Phi_i(x^*x)-x^*x)\bigr|
 +2\bigl|\psi(x^*(\Phi_i(x)-x))\bigr|.
 \tag{HAU4}
\]
Both terms tend to zero. For the second term, use [CP6](OA-FLOW-CP.md#oa-flow.cp.6) to write \(\psi(z)=\sum_j\langle z\xi_j,\eta_j\rangle\), with square-summable vector families. Then \(\psi(x^*z)=\sum_j\langle z\xi_j,x\eta_j\rangle\). The sum of the products of vector norms is bounded by \(\|x\|\sum_j\|\xi_j\|\|\eta_j\|<\infty\). Thus multiplication by the fixed \(x^*\) gives another normal vector-series functional, so this term also tends to zero.

Expand the square, apply (HAU3), and use that \(\psi\) preserves adjoints:
\[
 \begin{aligned}
 p_\psi(\Phi_i(x)-x)^2
 &\le \psi(\Phi_i(x^*x))
       -2\operatorname{Re}\psi(x^*\Phi_i(x))+\psi(x^*x)\\
 &\le e_{i,\psi}(x)\longrightarrow0.
 \end{aligned}
 \tag{HAU5}
\]
Applying the same calculation to \(x^*\) controls \(p_\psi((\Phi_i(x)-x)^*)\), because \(\Phi_i(x^*)=\Phi_i(x)^*\). Thus ultraweak convergence of these completely positive contractions to the identity gives pointwise \(\sigma\)-strong-star convergence. The estimates hold for the original directed net.

**Second, correct the outgoing map.** Choose any state \(\omega_i\) on each \(M_{m_i}\), and put
\[
 \widehat T_i(y)=T_i(y)+\omega_i(y)D_i,
 \qquad \widehat\Phi_i=\widehat T_iS_i.
 \tag{HAU6}
\]
For a positive matrix \([y_{ab}]\) over \(M_{m_i}\), the scalar matrix \([\omega_i(y_{ab})]\) is positive: test it on a scalar column and apply positivity of \(\omega_i\). Tensoring its positive square-root factorization with \(D_i^{1/2}\) proves positivity of \([\omega_i(y_{ab})D_i]\). This proves complete positivity of the correction at every size. Adding it to \(T_i\) preserves complete positivity, and \(\widehat T_i(1)=T_i(1)+D_i=1\). The map is normal because its domain is finite dimensional. The unital case of (HAU3) gives contractivity of \(S_i\) and \(\widehat T_i\). Thus \(\widehat\Phi_i\) is normal and unital completely positive.

The correction has an error bound uniform over the choice of matrix state. Since \(D_i^2\le D_i\) and \(|\omega_i(S_i(x))|\le\|x\|\),
\[
 \begin{aligned}
 p_\psi(\widehat\Phi_i(x)-\Phi_i(x))^2
 &=|\omega_i(S_i(x))|^2\psi(D_i^2)\\
 &\le\|x\|^2d_{i,\psi}.
 \end{aligned}
 \tag{HAU7}
\]
Together with the seminorm triangle inequality and (HAU5), this gives
\[
 \begin{aligned}
 p_\psi(\widehat\Phi_i(x)-x)
 &\le\sqrt{e_{i,\psi}(x)}+\|x\|\sqrt{d_{i,\psi}},\\
 p_\psi((\widehat\Phi_i(x)-x)^*)
 &\le\sqrt{e_{i,\psi}(x^*)}+\|x\|\sqrt{d_{i,\psi}}.
 \end{aligned}
 \tag{HAU8}
\]
Both right-hand sides tend to zero. For any finite list of operators and normal positive functionals, directedness supplies one index after which all the displayed bounds meet a prescribed tolerance. This supplies normal unital matrix approximations in the exact topology needed by step 2. Exact trace preservation is subsequently constructed there; the unitality correction alone makes no such assertion. \(\square\)

<a id="ha-defect-tails"></a>
### Finite stages of the balanced reconstruction

Step 3 involves a countable family of operators. Its finite stages have two different residuals, and their size determines the convergence available for the reconstructed maps.

Let \(M\) be any finite von Neumann algebra with a faithful normal tracial state \(\tau\). Suppose \(h,k\in M_+\) have the same center-valued trace. The [positive-defect matching theorem](../../OA-APPROX/balancing-kraus-families-and-unitary-couplings.html#countable-trace-exhaustion) supplies a finite or countable family \((a_j)\) with
\[
 \sum_{j\ge1}a_j^*a_j=h,\qquad
 \sum_{j\ge1}a_ja_j^*=k
 \tag{HADT1}
\]
in the strong topology. A finite family is extended by zeros. Put
\[
 h_n=h-\sum_{j=1}^na_j^*a_j,\qquad
 k_n=k-\sum_{j=1}^na_ja_j^*,\qquad
 r_n=\tau(h_n)=\tau(k_n).
 \tag{HADT2}
\]
Then \(h_n\downarrow0\), \(k_n\downarrow0\), and \(r_n\downarrow0\). The equality of the two scalar residuals follows from traciality of each summand and \(\tau(h)=\tau(k)\); the limits use normality. No factoriality or separable-predual assumption is imposed.

Here the matching theorem can be used with successive choices instead of a maximal family. At stage \(n\), consider all \(a\) with \(a^*a\le h_n\) and \(aa^*\le k_n\), and choose one whose squared trace Hilbert norm exceeds half the supremum of those norms. The theorem proves that this supremum is positive whenever \(h_n\ne0\), using spectral subprojections, their central supports and polar decomposition. If a nonzero residual survived all stages, one fixed positive-size match inside it would be available at every stage. This contradicts the finite total sum \(\sum_j\tau(a_j^*a_j)\le\tau(h)\). Thus the construction gives (HADT1). It does not give a uniform geometric rate for \(r_n\).

**Tail-map theorem.** For \(x,y\in M\), define
\[
 B(x)=\sum_{j\ge1}a_j^*xa_j,\qquad
 C(y)=\sum_{j\ge1}a_jya_j^*,
 \tag{HADT3}
\]
and let \(B^{(n)},C^{(n)}\) denote their first \(n\) terms. These series converge strongly for every bounded input and define normal completely positive maps. Their tails \(B_n=B-B^{(n)}\), \(C_n=C-C^{(n)}\) satisfy
\[
 \begin{aligned}
 B_n(1)&=h_n,& C_n(1)&=k_n,\\
 \|B_n\|&=\|h_n\|,& \|C_n\|&=\|k_n\|,\\
 \tau(B_n(x))&=\tau(xk_n),&
 \tau(C_n(y))&=\tau(yh_n).
 \end{aligned}
 \tag{HADT4}
\]
The trace-adjoint relation and the quantitative bounds are
\[
 \tau(yB_n(x))=\tau(C_n(y)x),
 \tag{HADT5}
\]
\[
 \begin{aligned}
 \|B_n(x)\|_2^2
   &\le\|h_n\|\,\tau(x^*xk_n)
    \le\|h\|\,\|x\|^2r_n,\\
 \|C_n(y)\|_2^2
   &\le\|k_n\|\,\tau(y^*yh_n)
    \le\|k\|\,\|y\|^2r_n.
 \end{aligned}
 \tag{HADT6}
\]
In particular the finite sums converge to the full maps in trace Hilbert norm, uniformly for inputs in a fixed operator-norm ball. This does not assert convergence in the operator norm of maps.

**Proof.** Represent \(M\) faithfully and normally on a Hilbert space \(H\). For a fixed \(n\), the column
\[
 V_n:H\longrightarrow\bigoplus_{j>n}H,
 \qquad V_n\xi=(a_j\xi)_{j>n}
 \tag{HADT7}
\]
is bounded, because the sum of squared coordinate norms is \(\langle h_n\xi,\xi\rangle\). Hence \(V_n^*V_n=h_n\) and \(\|V_n\|^2=\|h_n\|\). If \(D(x)\) acts as \(x\) on every coordinate, the finite coordinate projections \(P_N\uparrow1\) give
\[
 V_n^*P_ND(x)P_NV_n\longrightarrow V_n^*D(x)V_n
 \quad\hbox{strongly}.
 \tag{HADT8}
\]
Indeed the omitted coordinate tail of the single vector \(V_n\xi\) tends to zero, and \(D(x)\) commutes with \(P_N\). The finite operators lie in \(M\), so their limit does too. This limit is \(B_n(x)\). For \(n=0\) it defines \(B\), and subtraction of finite sums proves the tail formula. Replacing \(a_j\) by \(a_j^*\) defines \(C_n\) and \(C\).

The compression formula proves complete positivity at every matrix level: amplify the column and test positivity of the diagonal representation. It gives \(\|B_n(x)\|\le\|h_n\|\|x\|\); evaluation at the unit gives equality of the map norm with \(\|h_n\|\). The same reasoning applies to \(C_n\).

For normality, let \(0\le x_\alpha\uparrow x\). For every \(\xi\), the positive scalar series gives
\[
 \begin{aligned}
 \sup_\alpha\langle B_n(x_\alpha)\xi,\xi\rangle
 &=\sup_\alpha\sup_N
       \sum_{j=n+1}^N\langle x_\alpha a_j\xi,a_j\xi\rangle\\
 &=\sup_N\sum_{j=n+1}^N\langle xa_j\xi,a_j\xi\rangle
  =\langle B_n(x)\xi,\xi\rangle.
 \end{aligned}
 \tag{HADT9}
\]
The exchange is between suprema of nonnegative finite sums. Thus \(B_n\) preserves increasing positive suprema and is normal by the [bounded positive-map criterion](../../OA-MOD/OA-MOD-NP.html#oa-mod-np-04). The argument for \(C_n\) is identical.

The column also supplies the needed Schwarz bound without assuming that the map is unital:
\[
 \begin{aligned}
 B_n(x)^*B_n(x)
 &=V_n^*D(x)^*V_nV_n^*D(x)V_n\\
 &\le\|h_n\|V_n^*D(x^*x)V_n
  =\|h_n\|B_n(x^*x).
 \end{aligned}
 \tag{HADT10}
\]
For a positive input, traciality of each term and normality give
\[
 \tau(B_n(x))
 =\sum_{j>n}\tau(x^{1/2}a_ja_j^*x^{1/2})
 =\tau(x^{1/2}k_nx^{1/2})=\tau(xk_n).
 \tag{HADT11}
\]
Linear decomposition into four positive elements gives this identity for every \(x\in M\), and similarly for \(C_n\). Applying \(\tau\) to (HADT10) now proves (HADT6). The middle quantity \(\tau(x^*xk_n)\) is real and nonnegative, since it equals \(\tau(k_n^{1/2}x^*xk_n^{1/2})\).

For a finite sum, the trace-adjoint identity (HADT5) is just \(\tau(ya_j^*xa_j)=\tau(a_jya_j^*x)\). To pass to the full tail, its finite sums converge strongly by (HADT8) and remain uniformly bounded. Bounded strong convergence is ultraweak convergence; the functionals \(z\mapsto\tau(yz)\) and \(z\mapsto\tau(zx)\) are normal. They therefore preserve these limits. This proves (HADT5) and completes the theorem. \(\square\)

**What a truncated balanced map preserves.** In step 3 the initial finite family \((b_i)\) has sums \(\sum_i b_i^*b_i=1-h\) and \(\sum_i b_ib_i^*=1-k\). The complete map and its finite truncations are
\[
 \Psi(x)=\sum_i b_i^*xb_i+B(x),\qquad
 \Psi_n(x)=\sum_i b_i^*xb_i+B^{(n)}(x).
 \tag{HADT12}
\]
The full map is normal, unital and trace preserving. At a finite stage the exact statements are
\[
 \Psi_n(1)=1-h_n,\qquad
 \tau(\Psi_n(x))=\tau(x)-\tau(xk_n),\qquad
 \|\Psi(x)-\Psi_n(x)\|_2
       \le\|x\|\sqrt{\|h\|r_n}.
 \tag{HADT13}
\]
These follow by adding the finite initial family to (HADT4) and (HADT6). The finite map is completely positive and subunital; exact unitality and exact trace preservation belong to the full sum unless both residuals have vanished. For the balancing choice \(h=\eta1\), the last bound becomes \(\|x\|\sqrt{\eta r_n}\). If the full reconstruction differs from a prescribed map on a matrix subfactor by at most \(2\eta\|x\|\) in operator norm, then its \(n\)-th finite truncation differs by at most
\[
 \bigl(2\eta+\sqrt{\eta r_n}\bigr)\|x\|
 \quad\hbox{in trace Hilbert norm}.
 \tag{HADT14}
\]
Here \(\|z\|_2\le\|z\|\) uses \(\tau(1)=1\). This gives the finite-stage error budget while retaining both normalization defects explicitly.

**A sharp diffuse example.** Take \(M=L^\infty((0,1])\), Lebesgue trace, and
\[
 a_j=1_{(3^{-j},\,3^{-(j-1)}]},\qquad h=k=1.
 \tag{HADT15}
\]
The intervals are disjoint and exhaust \((0,1]\), so both sums in (HADT1) equal one. Both full maps are the identity. Their residuals and tails are
\[
 h_n=k_n=1_{(0,3^{-n}]},\quad r_n=3^{-n},\quad
 B_n(x)=C_n(x)=1_{(0,3^{-n}]}x.
 \tag{HADT16}
\]
Thus \(\|B_n\|=1\) for every finite \(n\), whereas \(\|B_n(1)\|_2=3^{-n/2}\). Equality holds in (HADT6) at \(x=1\). At each stage the largest admissible trace match is the whole residual projection; the chosen next interval uses two thirds of that mass and therefore satisfies the preceding greater-than-half choice rule. The geometric rate is a feature of this example, not a general bound for that rule.

![Residual intervals and exact trace, Hilbert-norm and map-norm errors](assets/hyperfinite-output/defect-exhaustion.svg)

The left panel shows the remaining interval after each finite stage. The right panel uses a base-three logarithmic vertical scale: the residual trace is \(3^{-n}\), the Hilbert error at the unit is \(3^{-n/2}\), and the map norm stays one. These are the exact values in (HADT16). The editable figure source and exact data accompany the diagram.

### Trace expectations and normal isomorphisms
The finite expectations and bounded trace topology used by the dyadic argument can also be obtained directly. Write a unital finite-dimensional subalgebra as \(B=\bigoplus_r M_{d_r}\), with matrix units \(f_{ij}^{(r)}\), and put \(t_r=\tau(f_{11}^{(r)})>0\). Its expectation is
\[
 E_B(x)=\sum_{r,i,j}t_r^{-1}\tau(f_{ji}^{(r)}x)f_{ij}^{(r)}.
 \tag{HAF1}
\]
For positivity at every matrix level, compress to the matrix of entries \(f_{1i}^{(r)}xf_{j1}^{(r)}\) and apply the positive functional \(\tau/t_r\) on the corner. Positivity of its matrix amplifications follows by testing scalar finite column vectors; the same argument with block columns proves complete positivity. Traciality identifies the resulting coefficients with those in (HAF1). Matrix multiplication shows that \(E_B\) fixes \(B\), is bimodular and is unital. The coefficient functionals are normal, so the finite sum is normal. Summing diagonal coefficients gives \(\tau E_B=\tau\). Finally \(\tau(b^*(x-E_Bx))=0\) for every \(b\in B\); hence this is the orthogonal trace-Hilbert projection and supplies precisely the nearest-point estimates used in the dyadic containment proof.

For the bounded topology, the normal functionals \(\psi_b(x)=\tau(bx)\), \(b\in M\), have norm-dense span in \(M_*\). Otherwise separation and the exact predual duality [CP6](OA-FLOW-CP.md#oa-flow.cp.6) give a nonzero \(x\in M\) with \(\tau(bx)=0\) for every \(b\); taking \(b=x^*\) contradicts faithfulness. Given a positive normal \(\psi\), choose \(b\) with \(\|\psi-\psi_b\|<\eta\). For \(\|x\|\le C\), positivity of the sandwiched trace functional gives
\[
 \psi(x^*x),\ \psi(xx^*)
 \le\|b\|\,\|x\|_2^2+\eta C^2.
 \tag{HAF2}
\]
Thus bounded convergence in trace \(2\)-norm implies convergence in every intrinsic strong-star seminorm, for arbitrary nets. Conversely the trace is one such test. These two constructions provide the exact finite-expectation and topology inputs used in Sections 3–5 of the dyadic-factor proof.

Here is how the local theorem supplies the maps in this alternative. For \(A=A_i\), choose a countable \(2\)-norm dense set of its unit ball. Exact dyadic containment supplies matrix factors \(B_n\subset B_{n+1}\), \(B_n\cong M_{2^{k_n}}\), whose union generates \(A\). Insert the successive \(M_2\) factors of their relative matrix commutants, obtaining
\[
 C_m\cong M_{2^m},\quad C_m\subset C_{m+1},\quad
 C_m'\cap C_{m+1}\cong M_2,\quad (\bigcup_m C_m)''=A.
 \tag{HA13}
\]
A unital inclusion \(M_a\subset M_b\) has \(b=ar\) and multiplicity commutant \(M_r\), by its decomposition into defining finite-dimensional modules. Here all multiplicities are powers of two. These are exact insertions; approximating an \(M_3\) by dyadic algebras would not put \(M_3\) inside a dyadic matrix level exactly.

Choose compatible matrix identifications of \(C_m\) with the first \(m\) tensor factors of \(R\). They preserve normalized trace. Their union \(\gamma_i^0\) therefore defines an isometry
\[
 V_i\Lambda_{\tau_i}(a)=\Lambda_{\tau_R}(\gamma_i^0(a)).
 \tag{HA14}
\]
Both sets of local vectors are dense, so it extends to a unitary of the full trace Hilbert spaces. It intertwines every local left multiplication with its image. Passing to the generated von Neumann algebras gives
\[
 \gamma_i:A_i\longrightarrow R,\quad
 \gamma_i(X)=V_iXV_i^*,\qquad \gamma_i^{-1}(Y)=V_i^*YV_i.
 \tag{HA15}
\]
These formulas hold in the faithful normal trace representations. Both directions are normal for arbitrary nets and onto. Transport out of those representations preserves these properties. Since the trace vectors correspond, \(\tau_R\gamma_i=\tau_i\) exactly. This supplies a full normal isomorphism, not merely an identification of algebraic unions or of their norm completions.

<a id="ha-interleaving"></a>
## 5. Tensor absorption with the full inverse

Start with the local algebra \(\mathcal D=\bigcup_n M_2^{\otimes n}\), inclusions obtained by adjoining the identity, and its product trace. Let \(R\) be the generated left algebra on its trace Hilbert completion. Right local multiplication commutes with it and has the trace vector \(\Omega\) cyclic. Thus \(\Omega\) is separating for the left algebra. Its vector state is faithful and normal, and is tracial by checking local elements and extending successively by bounded density and normality. The trace expectations to the first \(n\) tensor factors are the \(L^2\) projections onto the local vectors, and converge in \(2\)-norm to the identity. For central \(x\), each such expectation commutes with its full matrix level, hence equals \(\tau_R(x)1\). Convergence and separation give \(x=\tau_R(x)1\). Arbitrarily large matrix levels exclude finite type I. Thus this is a separable \(\mathrm{II}_1\) factor, agreeing with the \(R\) of (HA14).

Label the positions of the two inputs by \((1,n)\), \((2,n)\), \(n\ge1\), and define
\[
 j(1,n)=2n-1,\qquad j(2,n)=2n.
 \tag{HA16}
\]
Place the first finite tensor in odd positions and the second in even positions. Different positions commute, so this defines a star homomorphism \(J_0:\mathcal D\odot\mathcal D\to\mathcal D\). Regrouping a finite target tensor into odd and even positions gives a two-sided algebraic inverse. The product traces give
\[
 \tau_R(J_0(z)^*J_0(z))=(\tau_R\otimes\tau_R)(z^*z).
 \tag{HA17}
\]
After polarization, the map
\[
 W(\Lambda_R(a)\otimes\Lambda_R(b))=\Lambda_R(J_0(a\otimes b))
 \tag{HA18}
\]
is an isometry on a dense span with dense range. It extends to a unitary \(L^2(R)\otimes L^2(R)\to L^2(R)\) and intertwines local left multiplication. Consequently
\[
 J:R\bar\otimes R\longrightarrow R,\quad J(X)=WXW^*,\qquad
 J^{-1}(Y)=W^*YW
 \tag{HA19}
\]
is normal, onto, and has a normal inverse. On a target local tensor that inverse is precisely odd/even regrouping. The unitary formulas define it on the entire von Neumann algebra. Since \(W(\Omega\otimes\Omega)=\Omega\), the normalized trace is preserved. This independently completes the absorption also stated in [Hyperfinite finite factors](../../OA-APPROX/hyperfinite-finite-factors.html#4-making-containment-exact), Exercise 8.

Put \(K=\ell^2(\mathbb N)\). Reordering Hilbert factors and applying (HA15), (HA19) gives
\[
 \Psi_i:(R\bar\otimes B(K))\bar\otimes A_i\longrightarrow R\bar\otimes B(K),\qquad
 \Psi_i(r\otimes b\otimes a)=J(r\otimes\gamma_i(a))\otimes b.
 \tag{HA20}
\]
Its inverse applies \(J^{-1}\) to the \(R\) leg, \(\gamma_i^{-1}\) to the resulting even-position leg, and the opposite flip to restore the order \(R,B(K),A_i\). Each operation is implemented by a Hilbert unitary in the indicated faithful normal representations. This is a full normal inverse, not only a prescription on generators.

For a positive operator, the semifinite traces are
\[
 (\tau_R\otimes\operatorname{Tr})(X)=\sum_j\tau_R(X_{jj}),\qquad
 (\tau_R\otimes\operatorname{Tr}\otimes\tau_i)(Y)
       =\sum_j(\tau_R\otimes\tau_i)(Y_{jj}).
 \tag{HA21}
\]
These are suprema of nonnegative finite sums. Faithfulness follows from diagonal compression; normality follows by interchanging suprema. If \(p_n\) is the first \(n\) matrix coordinates, \(Xp_n\) lies in the finite left ideal and tends strongly to \(X\), proving semifiniteness. Traciality follows by comparing the two nonnegative double sums of \(\tau(x_{kj}^*x_{kj})\) and \(\tau(x_{kj}x_{kj}^*)\). They agree also at infinity. The map (HA20) fixes the matrix index and preserves each finite coefficient trace, so it preserves (HA21) on the full positive cone, with no unspecified scalar multiplier.

<a id="ha-full-crossed"></a>
## 6. Full coefficient systems and their regular products

Represent \(R_\infty\) faithfully normally on \(H_\infty\). Use the regular representation of \(N_i\) on \(\ell^2(\mathbb Z)\otimes H_\infty\otimes H_i\). The unitary
\[
 U(\delta_k\otimes\eta\otimes\xi)=\eta\otimes\delta_k\otimes\xi
 \tag{HA22}
\]
sends a coefficient \(r\otimes f\) to \(r\otimes\pi_i(f)\) and the integer shift to \(1\otimes u_i\). Its generator images contain \(R_\infty\otimes1\) and \(1\otimes A_i\), and belong to their spatial tensor product. They therefore generate exactly that tensor product. Hence
\[
 \Theta_i:N_i\rtimes_{\alpha_i}\mathbb Z\longrightarrow R_\infty\bar\otimes A_i,\quad
 \Theta_i(X)=UXU^*,\qquad \Theta_i^{-1}(Y)=U^*YU
 \tag{HA23}
\]
is a normal onto star isomorphism with normal inverse. NR4 gives the same canonical generator map for any other initial faithful normal coefficient representation. The isomorphism in (HA2) is \(\Psi_i\Theta_i\).

The trace on \(N_i\) is \(\tau_R\otimes\operatorname{Tr}\otimes\mu_i\), defined on its whole positive cone by (HA21) with finite coefficient trace \(\tau_R\otimes\mu_i\). It is invariant under \(\alpha_i\). Define \(\widetilde\tau_i\) as the pullback by \(\Theta_i\) of \(\tau_R\otimes\operatorname{Tr}\otimes\tau_i\). Equivalently it is the invariant product trace composed with the discrete coefficient expectation. To verify the latter equality on more than words, cut by a finite matrix projection. On that finite-trace corner separate normality extends equality on covariant words to the entire corner. Summing the diagonal values gives equality on the full positive cone. This fixes the scale in (HA2).

Commutation with all matrix units reduces \(Z(R_\infty)\) to \(Z(R)\otimes1=\mathbb C1\). Its rank-one matrix corner is \(R\), so \(R_\infty\) is of type \(\mathrm{II}_\infty\). The constant-field algebra \(N_i\) has full center \(1\otimes D_i\). Directly, all normal slices of a central element against the second leg lie in \(Z(R_\infty)\). Subtract \(1\otimes(\rho\otimes\operatorname{id})(X)\), for a normal state \(\rho\) of \(R_\infty\); every product normal slice then vanishes, hence the difference is zero. The rank-one matrix corner is the constant type \(\mathrm{II}_1\) field \(R\bar\otimes D_i\); countably many equivalent matrix diagonals sum to one. Thus \(N_i\) is type \(\mathrm{II}_\infty\) on every nonzero central summand. This uses the full center and central type conventions of the induced-corner lesson; it does not call \(N_i\) a factor. All Hilbert factors can be chosen separable, and the center is the nonatomic \(D_i\). Its action is exactly the ergodic \(\beta_i\).

For completeness, the full constant-field assertion used here has an elementary proof in this separable setting. Choose a countable orthonormal basis of the faithful representation space of a von Neumann algebra \(C\). Every operator commuting with the scalar multiplication algebra has matrix coefficients commuting with that scalar algebra on \(L^2(X)\). That scalar algebra is maximal abelian: an operator commuting with all multipliers sends \(1\) to a function \(g\), sends every bounded \(f\) to \(fg\), and boundedness tested on indicator functions gives \(|g|\le\|T\|\) almost everywhere. Hence all matrix coefficients are measurable functions. Tests on the countable rational finite vectors, after a single null-set deletion, give a measurable operator field with the same essential norm bound. Conversely such a field defines the original bounded operator by integration. Commutation with a countable strong-star dense subset of the unit ball of \(C'\) forces the fiber values into \(C''=C\). A countable dense subset exists because the unit ball of \(B(H)\) has a second-countable strong-star topology when \(H\) is separable, and its subspaces inherit second countability.

Every bounded measurable \(C\)-valued field belongs to \(C\bar\otimes L^\infty(X)\): approximate it on the first \(n\) basis vectors and adjoint vectors by the first suitable element of a countable strong-star dense subset of a fixed norm ball of \(C\). The choices define a countably valued measurable field. Its countable disjoint projection sum belongs to the spatial product by strong closure; bounded dominated convergence gives strong-star convergence to the original field. This proves equality with the **whole** field algebra. In particular any nonzero projection field \(p\) in the constant \(R_\infty\) field is nonabelian. At each point where \(p(x)\ne0\), the corner \(p(x)R_\infty p(x)\) is nonabelian. Some pair from a fixed countable strong-star dense family of constants has nonzero compressed commutator there. The countable union of these detection sets contains the nonzero support of \(p\), so one pair gives a nonzero global commutator in \(pN_ip\). Thus there are no nonzero abelian projections. The product trace gives semifiniteness, and the odd/even matrix isometries give proper infiniteness on every central cut. These facts establish the claimed type \(\mathrm{II}_\infty\) without leaving fiber-to-global type transfer implicit.

<a id="ha-obstruction"></a>
## 7. No positive central sections give conjugate systems

A nonzero central projection is \(e_i=1\otimes1_{E_i}\), with \(a_i=\mu_i(E_i)>0\). IE, Section 1, proves that, after an invariant null-set deletion, every orbit meeting \(E_i\) has infinitely many visits in both directions. The first-return function \(r_i\) is measurable and finite almost everywhere. The return map \(S_i=(T_i)_{E_i}\) is invertible and ergodic and preserves \(\nu_i=\mu_i|_{E_i}/a_i\). Its mean return time is \(1/a_i\); no bounded-return assumption occurs.

The induced coefficient algebra is \(R_\infty\bar\otimes L^\infty(E_i)\). On the source piece \(E_{i,n}=\{r_i=n\}\), the \(n\)-step action leaves the \(R_\infty\) coordinate unchanged. The range pieces \(T_i^nE_{i,n}\) partition \(E_i\), so its center map is exactly
\[
 f\longmapsto f\circ S_i^{-1}.
 \tag{HA24}
\]
A normal conjugacy of the full induced coefficient systems would restrict to a normal center conjugacy.

This conclusion can be used on probability measure algebras, without an additional point-realization theorem. Transport \(\nu_0\) through the center isomorphism to a faithful normal probability \(\rho\) on the second center. It is equivalent to \(\nu_1\) and invariant under \(S_1\). The scalar Radon–Nikodym argument in IE, Section 7, gives \(\rho=f\nu_1\). Invariance gives \(f=f\circ S_1^{-1}\); ergodicity makes its rational upper-level sets trivial, so \(f\) is constant. Its integral one makes it one. Thus the isomorphism preserves the **normalized** section probabilities. Finite measurable partitions correspond to finite central projection partitions, and all probabilities of their orbit joins are preserved. Entropy is preserved in both directions.

The complete unbounded-return theorem IE3 and calculations IE50–54 contradict this:
\[
 h_{\nu_0}(S_0)=0/a_0=0,\qquad
 h_{\nu_1}(S_1)=\log2/a_1>0.
 \tag{HA25}
\]
This covers every positive measurable section, including unbounded return times. It assumes neither equal section mass, preservation of unnormalized restrictions, nor existence of a finite generator. IE retains infinite entropy as well, although these two base values are finite.

There is also no alternative trace restoring contraction. Let \(\tau\) be the invariant product trace. The full density and uniqueness theorem [TD4–6](OA-FLOW-TD.md#oa-flow.td.4) writes any other faithful normal semifinite trace as \(\tau_b\), with positive affiliated density having zero kernel and no infinite-value part. Inner invariance of both traces and uniqueness force each spectral projection of \(b\) to be central. Thus \(b\) is a scalar measurable function on \(X_i\), finite and strictly positive almost everywhere. Invariance and the convention \(\beta_i(f)=f\circ T_i^{-1}\) give
\[
 \tau_b\circ\alpha_i=\tau_{b\circ T_i}.
 \tag{HA26}
\]
If \(\tau_b\circ\alpha_i\le c\tau_b\), \(0<c<1\), order reflection in TD5 gives \(b(T_i x)\le cb(x)\) almost everywhere. Delete every integer translate of its exceptional set. Some band \(B_m=\{1/m\le b\le m\}\) has positive probability. Recurrence gives arbitrarily large positive return times \(n\) to that band; iteration then gives \(1/m\le c^n m\), impossible for large \(n\). This proves the last assertion for all faithful normal semifinite traces, however unbounded their densities.

<a id="ha-diagnostics"></a>
## 8. Six solved checks

**1. Is the invariant-mean retraction normal?** In general it is not. For the shift on \(\ell^\infty(\mathbb Z)\), invariance assigns the same mean value \(t\) to every singleton projection. The inequalities \(nt\le1\) force \(t=0\). Every finite-interval projection has mean zero, though these projections increase to one. This proves failure of normality. Injectivity permits such a retraction. Every isomorphism in (HA15), (HA19), (HA20) and (HA23) is normal for the separately proved unitary reason.

**2. Where does a four-position tensor go?** For inputs \(a_1\otimes a_2\) and \(b_1\otimes b_2\), interleaving gives \(a_1\otimes b_1\otimes a_2\otimes b_2\). The inverse extracts positions \(1,3\) and \(2,4\). Its normalized trace is the product of the four normalized matrix traces, exactly the product of the two input traces. Interleaving introduces no factor of two.

**3. Does the infinite trace hide the normalization?** Let \(p,q\) be rank-one projections in the first \(M_2\) positions of the two copies of \(R\), and let \(e\in B(K)\) have rank \(k\). Before absorption the trace of \(p\otimes e\otimes q\) is \(k/4\). After absorption \(J(p\otimes q)\) has normalized trace \(1/4\), so its tensor with \(e\) again has trace \(k/4\). These finite tests and (HA21) fix the scale despite infinite trace of the unit.

**4. Can different section masses defeat the entropy argument?** If \(a_0=1/3\), \(a_1=1/4\), the normalized return entropies are \(0\) and \(4\log2\). In a point realization a hypothetical conjugacy carries the first unnormalized restriction to \((a_0/a_1)\mu_1|_{E_1}=(4/3)\mu_1|_{E_1}\). It preserves the normalized probabilities, so the entropy contradiction persists. Equal section mass was never required.

**5. Does a copy of \(R\) inside \(A_i\) suffice?** No. Containment does not say that copy generates \(A_i\). The provider approximates every finite subset, then uses exact containment of successive dyadic approximants to a dense sequence. This makes the union in (HA13) generate the entire algebra. That density makes \(V_i\) onto and transports the whole left algebra in (HA15). A bare embedded hyperfinite subfactor would leave the decisive step unproved.

**6. Could an unbounded density restore contraction?** The bands \(\{1/m\le b\le m\}\) exhaust almost all the probability space for every finite strictly positive measurable \(b\). One has positive measure, and recurrence there alone contradicts \(1/m\le c^n m\). There is no global bound assumption. The density in (HA26) is \(b\circ T_i\), not \(b\circ T_i^{-1}\): change variables in \(\int b(x)f(T_i^{-1}x)\,d\mu_i(x)\).

<a id="ha-sources"></a>
## 9. Earlier proofs and attribution

The finite injective-factor theorem is due to Connes. The earlier [finite-factor lesson](../../OA-APPROX/unitary-couplings-and-finite-injective-factors.html#5-injective-finite-factors-are-locally-afd) proves it through Haagerup's unitary-coupling method; its exact dyadic containment and normal trace-GNS conclusion are supplied by [the hyperfinite-factor lesson](../../OA-APPROX/hyperfinite-finite-factors.html#4-making-containment-exact). The arbitrary finite projection comparisons used there are proved in [PC1–7](OA-FLOW-PC.md#oa-flow.projection.pc1), with the full center-valued trace in [FCT0–8](OA-FLOW-FCT.md#oa-flow.fct.0). These are earlier programme proofs, including their nonfactor and arbitrary-cardinality statements.

The return-entropy identity is Abramov's formula, proved with unbounded returns and both infinite-entropy suprema in [IE](OA-FLOW-IE.md#IE-setting). Its irrational-rotation and Bernoulli examples provide the two exact entropy values used here. Every positive central section is covered by the normalized probability argument in Section 7.

This lesson proves the common-output alternative at its stated separable example scope. The separate [induced-corner theorem](OA-FLOW-IC.md#ic-continuous) retains its faithful semifinite whole-cone contraction hypothesis and its full normal maps and inverses.

Original exposition and the vector diagram are dedicated to CC0-1.0 to the extent of rights held. Earlier human sources and software retain their own terms.
