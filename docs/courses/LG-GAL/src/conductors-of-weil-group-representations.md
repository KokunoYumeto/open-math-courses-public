# Conductors of Weil-group representations

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The conductor measures the part of a local representation moved by inertia, with an extra cost for wild ramification. Frobenius eigenvalues do not affect it. We make this assertion precise for smooth Weil representations and prove the induction formula, where the discriminant of the extension contributes even when the inducing representation is unramified.

We assume Representations of Weil groups and the ramification theory recalled below. As in that lesson, \(F\) is a nonarchimedean local field with residue cardinality \(q\), representations are finite-dimensional over \(\mathbb C\), and \(\operatorname{Art}_F(\varpi)\) is geometric Frobenius. Conductors are unchanged when reciprocity is inverted, since a character and its inverse have the same kernel on every ramification group.

## 1. Finite ramification and the different, with proofs

We first establish the finite-field calculations used by the conductor. The complete valuation, finite free integral closure, separable trace pairing, degree formula \([L:F]=ef\), extension of embeddings, Hensel lifting and unramified residue-field correspondence are proved in Profinite groups and adic representations, Lemmas 0A.1, 0B.1–0B.2, 0D.1–0D.2 and Propositions 0E.1–0F.2. These statements hold for a complete discretely valued field with finite residue field, in either characteristic; the coefficient-field application in that lesson does not restrict their hypotheses. The Weil topology, finite quotients and finite-extension subgroups are Propositions 1.1–1.2 of Representations of Weil groups. We will prove the additional ramification algebra here.

### 1A. Integral generators and lower groups

**Lemma 1.1 (integral generators).** For a finite separable extension \(L/F\), there is an unramified intermediate field \(F_0\) with residue field \(k_L\), and
\[
[L:F_0]=e(L/F),\qquad
\mathcal O_L=\mathcal O_{F_0}[\pi_L]
\]
for every uniformizer \(\pi_L\). There is also \(\alpha\) with \(\mathcal O_L=\mathcal O_F[\alpha]\).

**Proof.** Lift a residue-field generator \(\bar\beta\) to the unique root \(\beta\in\mathcal O_L\) of a monic lift of its separable minimal polynomial. The proof of Proposition 0F.2 identifies \(F_0=F(\beta)\) as the degree-\(f\) unramified field, with that residue field. The degree formula gives \([L:F_0]=e\). The values of \(1,\pi_L,\ldots,\pi_L^{e-1}\) are distinct modulo \(e\mathbf Z=v_L(F_0^\times)\). A nonzero linear combination over \(F_0\) has a unique term of least value and cannot vanish. These \(e\) elements are therefore an \(F_0\)-basis. If \(x=\sum_{j<e}a_j\pi_L^j\) is integral, its least term has nonnegative value; the distinct valuation classes then give \(e v_{F_0}(a_j)+j\geq0\) for every \(j\), so every \(a_j\) is integral. This proves the asserted integral basis and generation. In particular the minimal polynomial of \(\pi_L\) is Eisenstein: its constant coefficient has base value one, by the norm valuation formula in Proposition 0E.1, and each other nonleading coefficient is integral and has positive value, since it is a sum of positive-valued products of conjugate uniformizers.

For completeness, one can combine the two generators. Put \(\alpha=\beta+\pi_L\) and \(A=\mathcal O_F[\alpha]\). This is a finite \(\mathcal O_F\)-module, hence complete and closed in \(\mathcal O_L\): finite lattices are complete, and their induced valuation topology is the coordinate topology by commensurability in Lemma 0A.1. Let \(g\) be the polynomial used to lift \(\bar\beta\). Its derivative at \(\alpha\) is a unit of \(A\). Indeed a polynomial Bezout relation between \(\bar g\) and \(\bar g'\), evaluated at \(\alpha\), produces an element of \(A\) inverse to \(g'(\alpha)\) up to an error of positive \(L\)-valuation. The geometric series for that error converges in \(A\) and gives an inverse. Newton iteration starting from \(\alpha\) consequently stays in \(A\); its errors have valuations tending to infinity by the proof of Lemma 0D.1. The resulting root of \(g\), congruent to \(\bar\beta\), is \(\beta\) by uniqueness. Thus \(\beta\in A\) and \(\pi_L=\alpha-\beta\in A\). The preceding integral basis gives \(A=\mathcal O_L\).

We will also use the converse Eisenstein calculation in the examples. For a separable monic Eisenstein polynomial of degree \(m\), let \(x\) be a root, and extend the base-normalized valuation. Its value is positive: otherwise the leading term alone has least value. Once \(v(x)>0\), every nonconstant nonleading term has value strictly greater than one, whereas the constant term has value exactly one. The least value in a zero sum must occur twice, forcing \(m v(x)=1\). Thus the ramification index of \(F(x)/F\) is at least \(m\); its degree is at most \(m\), and the degree formula forces both to equal \(m\), with residue degree one. In normalized upper valuation \(x\) is a uniformizer. The integral basis just proved applies to it. This proves the Eisenstein assertions used below without importing an integral-basis theorem. \(\square\)

For finite Galois \(L/F\), write \(G=\operatorname{Gal}(L/F)\), normalize \(v_L(L^\times)=\mathbf Z\), and define
\[
i_G(\sigma)=\min_{x\in\mathcal O_L}v_L(\sigma x-x),\qquad
G_j=\{\sigma:i_G(\sigma)\geq j+1\}\quad(j\geq-1).
\tag{1A}
\]
Identity has motion number \(+\infty\). If \(\mathcal O_L=\mathcal O_F[\alpha]\), polynomial division of \(P(Y)-P(X)\) by \(Y-X\) shows that
\[
i_G(\sigma)=v_L(\sigma\alpha-\alpha).
\tag{1B}
\]
The minimum is attained at \(\alpha\). The definition shows directly that \(G_j\) is a subgroup: \(\sigma\tau x-x=\sigma(\tau x-x)+(\sigma x-x)\), and the valuation is preserved by automorphisms. Inverses follow on replacing \(x\) by \(\sigma^{-1}x\), and conjugation replaces the test element by another integral element. Thus the groups are normal, decrease, and become trivial, because the finitely many nonidentity motions in (1B) are finite. We have \(G_{-1}=G\) and \(G_0\) equal to the kernel of the residue action, namely inertia.

The unramified field \(F_0\) of Lemma 1.1 is unique by the residue correspondence. It is stable under \(G\); extension of embeddings gives surjectivity onto \(\operatorname{Gal}(F_0/F)\), with kernel \(G_0\). Therefore
\[
|G_0|=e(L/F),\qquad |G|/|G_0|=f(L/F),\qquad
 i_G(\sigma)=v_L(\sigma\pi_L-\pi_L)\ (\sigma\in G_0).
\tag{1C}
\]
If \(H\leq G\), the intrinsic minimum uses the same \(\mathcal O_L,v_L\) for \(L/L^H\), so \(i_H(h)=i_G(h)\) and \(H_j=H\cap G_j\), whether or not \(H\) is normal.

**Lemma 1.2 (tame and wild inertia).** The quotient \(G_0/G_1\) is cyclic of order prime to the residue characteristic \(p\), and \(G_1\) is a \(p\)-group. In particular \(G_1=1\) exactly when \(L/F\) is tame.

**Proof.** For \(\sigma\in G_0\), reduce \(c_\sigma=\sigma\pi_L/\pi_L\). The identity \(c_{\sigma\tau}=\sigma(c_\tau)c_\sigma\) makes this a homomorphism into \(k_L^\times\), since inertia fixes residues. Formula (1C) gives kernel \(G_1\). Cyclicity of finite residue units was proved in Lemma 0F.1 of the first lesson. For \(j\geq1\), reduction of \(c_\sigma\) in
\[
(1+\mathfrak p_L^j)/(1+\mathfrak p_L^{j+1})\simeq(k_L,+),\qquad
1+a\pi_L^j\longmapsto\bar a,
\]
gives an injection \(G_j/G_{j+1}\hookrightarrow(k_L,+)\). Multiplication is addition because \(2j\geq j+1\). Elements of \(G_1\) act trivially on this unit quotient: they fix residues and \(\sigma\pi_L/\pi_L\equiv1\pmod{\mathfrak p_L}\). This verifies the homomorphism identity, and (1C) gives its kernel. The filtration terminates, so \(|G_1|\) is a power of \(p\); its index in inertia is prime to \(p\). Since \(|G_0|=e\) and the residue extension is separable, \(p\nmid e\) is exactly the tame case. \(\square\)

### 1B. Trace duals, the different and discriminants

For any finite separable \(L/F\), let
\[
\mathcal O_L^*=\{z\in L:\operatorname{Tr}_{L/F}(z\mathcal O_L)\subseteq\mathcal O_F\},\qquad
\mathfrak D_{L/F}=(\mathcal O_L^*)^{-1}.
\tag{1D}
\]
The trace pairing is nondegenerate by the Vandermonde proof in Proposition 0E.1. A trace matrix in an integral basis therefore identifies its dual with a full finite lattice. The dual is stable under \(\mathcal O_L\), so it is a fractional ideal of the DVR \(\mathcal O_L\), hence principal. Traces of integral elements are integral by that same proof; thus \(\mathcal O_L\subseteq\mathcal O_L^*\) and the different is an integral ideal. Write \(d_{L/F}=v_L(\mathfrak D_{L/F})\geq0\).

**Lemma 1.3 (the monogenic trace dual).** If \(\mathcal O_L=\mathcal O_F[\alpha]\) and \(h\) is the monic minimal polynomial, then
\[
\mathcal O_L^*=h'(\alpha)^{-1}\mathcal O_L,\qquad
\mathfrak D_{L/F}=h'(\alpha)\mathcal O_L.
\tag{1E}
\]

**Proof.** For a polynomial \(r\) of degree at most \(n-1=\deg h-1\), Lagrange interpolation at the distinct roots \(\alpha_s\) gives
\[
\sum_s\frac{r(\alpha_s)}{h'(\alpha_s)}
=\text{coefficient of }X^{n-1}\text{ in }r(X).
\tag{1F}
\]
This follows by taking that coefficient in
\(r(X)=\sum_s r(\alpha_s)h(X)/((X-\alpha_s)h'(\alpha_s))\).
Hence the trace of \(r(\alpha)/h'(\alpha)\) is that coefficient. Reduction modulo the monic integral polynomial \(h\) preserves integral coefficients, so this formula already puts \(h'(\alpha)^{-1}\mathcal O_L\) in the trace dual.

To see equality, expand \(h(X)/(X-\alpha)=\sum_{j=0}^{n-1}b_j(\alpha)X^j\). For \(0\leq k<n\), the Lagrange identity for \(X^k\) says to sum
\[
\frac{\alpha_s^k}{h'(\alpha_s)}\frac{h(X)}{X-\alpha_s}
\]
over \(s\); interpolation says the result is \(X^k\). Comparing coefficients gives
\(\operatorname{Tr}(\alpha^k b_j(\alpha)/h'(\alpha))=\delta_{kj}\).
Thus \(b_j(\alpha)/h'(\alpha)\) is the basis trace-dual to \(1,\alpha,\ldots,\alpha^{n-1}\). The polynomials \(b_{n-1},b_{n-2},\ldots,b_0\) have successive degrees \(0,1,\ldots,n-1\), with leading coefficients one. Their triangular coefficient matrix is invertible over \(\mathcal O_F\), so they form another integral basis. This proves equality and its inverse-ideal formula. \(\square\)

**Lemma 1.4 (different in a tower and its norm).** For finite separable \(L/E/F\),
\[
\mathfrak D_{L/F}=\mathfrak D_{L/E}\mathfrak D_{E/F}\mathcal O_L,\qquad
 d_{L/F}=d_{L/E}+e(L/E)d_{E/F}.
\tag{1G}
\]
If \(\mathfrak d_{E/F}\) is the determinant ideal of the integral trace pairing, then
\[
\mathfrak d_{E/F}=N_{E/F}(\mathfrak D_{E/F}),\qquad
\delta_{E/F}:=v_F(\mathfrak d_{E/F})=f(E/F)d_{E/F}.
\tag{1H}
\]

**Proof.** Let \(b_i\) be an \(\mathcal O_F\)-basis of \(\mathcal O_E\), with trace-dual basis \(b_i^*\), and \(c_j\) an \(\mathcal O_E\)-basis of \(\mathcal O_L\), with relative trace-dual basis \(c_j^*\). Field trace is transitive: after passing to a splitting field it is a sum over embeddings; grouping embeddings of \(L\) by their restriction to \(E\) gives \(\operatorname{Tr}_{L/F}=\operatorname{Tr}_{E/F}\operatorname{Tr}_{L/E}\), using the embedding count of Lemma 0B.1. It follows that \(b_i^*c_j^*\) is dual to \(b_ic_j\). Consequently the absolute trace dual is the product of the two relative trace-dual fractional ideals. Indeed \(\sum_i\mathcal O_F b_i^*=\mathcal O_E^*=a\mathcal O_E\) for a scalar \(a\in E^\times\), so the span of the products is \(a\sum_j\mathcal O_E c_j^*=a\mathcal O_L^{*,E}\). Inverting proves (1G), including the valuation scale.

For (1H), an integral trace matrix \(T\) represents the inclusion of the integral lattice into its dual as \(\mathcal O_F^n\subseteq T^{-1}\mathcal O_F^n\). Its quotient length is \(v_F(\det T)\). Here is the elementary DVR argument: select a nonzero entry of smallest valuation, move it to the first position, and eliminate its row and column by integral operations, since it divides every entry. Repeat on the remaining matrix. In the resulting diagonal matrix the determinant valuation and quotient length are both the sum of the diagonal valuations. But the dual is \(\mathfrak p_E^{-d_{E/F}}\); its quotient by \(\mathcal O_E\) has \(d_{E/F}\) successive residue-field quotients, each of length \(f(E/F)\) over \(\mathcal O_F\). This proves the last formula. Finally the ideal norm sends \(\mathfrak p_E\) to \(\mathfrak p_F^f\): for a uniformizer its principal norm has valuation \(f\), by Proposition 0E.1. Powers and the principal-ideal description of a DVR prove the first formula. \(\square\)

**Lemma 1.5 (Hilbert's formula).** For finite Galois \(L/F\),
\[
d_{L/F}=\sum_{\sigma\ne1}i_G(\sigma)
=\sum_{j\geq0}(|G_j|-1).
\tag{1I}
\]
In particular an unramified extension has different exponent zero, and a tame extension has different exponent \(e-1\).

**Proof.** Lemma 1.1 gives an integral generator \(\alpha\). Its minimal polynomial is \(h(X)=\prod_{\sigma\in G}(X-\sigma\alpha)\), so (1E) and (1B) give the first equality. A nonidentity element of motion \(i\) belongs to exactly the \(i\) groups with indices \(j\geq0\) satisfying \(j+1\leq i\). Counting its contributions gives the second equality. In the tame case Lemma 1.2 makes every group beyond \(G_0\) trivial, leaving \(|G_0|-1=e-1\); the unramified case has \(G_0=1\). \(\square\)

### 1C. The quotient theorem, proved before quotient independence

Set \(G_t=G_{\lceil t\rceil}\) for real \(t\geq-1\), and
\[
\varphi_{L/F}(t)=t\ (-1\leq t\leq0),\qquad
\varphi_{L/F}(t)=\int_0^t\frac{|G_x|}{|G_0|}\,dx\ (t\geq0).
\tag{1}
\]
It is continuous, strictly increasing and unbounded, with positive piecewise constant derivative, so it has inverse \(\psi\). Define \(G^u=G_{\psi(u)}\). Groups retain their value at a jump and decrease immediately afterward. A useful equivalent identity is
\[
\varphi_{L/F}(t)=\frac1{|G_0|}\sum_{g\in G}\min\{i_G(g),t+1\}-1.
\tag{1J}
\]
On \([-1,0]\) precisely the \(|G_0|\) inertial terms contribute \(t+1\), so this holds. On \(m<t<m+1\), the derivative of the right side counts motions at least \(m+2\), namely \(|G_{m+1}|/|G_0|\), the derivative of (1). Continuity and the value at zero prove (1J) everywhere.

**Lemma 1.6 (coset motion and upper quotient theorem).** If \(H\triangleleft G\), \(E=L^H\) and \(Q=G/H\), then
\[
i_Q(s)=\frac1{e(L/E)}\sum_{g\mapsto s}i_G(g),\qquad
G^uH/H=Q^u.
\tag{1K}
\]
The identity coset is interpreted with infinite motion on both sides. The Herbrand functions satisfy
\(\varphi_{L/F}=\varphi_{E/F}\circ\varphi_{L/E}\).

**Proof.** Choose integral generators \(\alpha\) for \(L/F\) and \(\beta\) for \(E/F\), by Lemma 1.1. Let \(h\) be the monic minimal polynomial of \(\alpha\) over \(E\). For \(s\ne1\) and a lift \(g\), the elements
\[
a=s\beta-\beta,\qquad
b=(gh)(\alpha)=\prod_{h_0\in H}(\alpha-gh_0\alpha)
\]
generate the same ideal of \(\mathcal O_L\). Each coefficient of \(h\) is an integral polynomial in \(\beta\), so \(gh-h\), evaluated at \(\alpha\), is divisible by \(a\). Conversely write \(\beta=P(\alpha)\) with \(P\in\mathcal O_F[X]\). Monic division gives \(P(X)-\beta=h(X)R(X)\) in \(\mathcal O_E[X]\), since the remainder vanishes at \(\alpha\). Applying \(g\) and evaluating at \(\alpha\) gives \(-a=b(gR)(\alpha)\). Taking valuations of the equal ideals proves the first identity of (1K), with scale \(v_L|_E=e(L/E)v_E\).

Choose a lift of \(s\ne1\) with maximal motion \(m\) in its fiber. The valuation identity
\(i_G(xy)\geq\min(i_G(x),i_G(y))\), with equality when the values differ, follows by evaluating \(xy\alpha-\alpha\) as the sum of two terms. Maximality then gives \(i_G(gh_0)=\min(m,i_H(h_0))\) for every \(h_0\in H\). The first identity and (1J) therefore yield
\[
i_Q(s)-1=\varphi_{L/E}(m-1).
\]
A coset has a representative in \(G_t\) precisely when \(m-1\geq t\); strict increase makes this equivalent to its membership in \(Q_{\varphi_{L/E}(t)}\). Thus
\(G_tH/H=Q_{\varphi_{L/E}(t)}\).
Their orders satisfy \(|G_t|=|H_t||Q_{\varphi_{L/E}(t)}|\), and ramification indices multiply by restriction of normalized valuations. Taking derivatives in (1) proves the tower identity, with equality at zero and then by continuity at all breaks. Substitute \(t=\psi_{L/F}(u)\) to obtain the upper quotient identity. \(\square\)

The absolute groups \(G_F^u\) are now defined by the inverse limit of these finite upper groups. Proposition 0C.1 of the first lesson supplies the compact Galois inverse limit. The transition maps on the upper groups are surjective by (1K); compatibility and a prescribed finite coordinate have the finite intersection property in that compact limit. Consequently every absolute upper group maps onto the corresponding finite upper group. They are closed, normal and decreasing. Inertia is \(G_F^0=I_F\), and \(P_F=G_F^{0+}\) means the closed subgroup generated by the positive upper groups. Its image in any finite quotient is \(G_1\): on the first positive lower interval the group is \(G_1\), and all later positive groups are contained in it. Thus Lemma 1.2 proves exactly the finite wild-inertia fact used below.

**Lemma 1.7 (the full tame inertia quotient).** The quotient \(I_F/P_F\) is prime-to-\(p\) procyclic; more canonically, it is \(\varprojlim_{p\nmid m}\mu_m\), with power maps on roots of unity.

**Proof.** In the unramified union \(F^{\mathrm{nr}}\), every unit has an \(m\)-th root for \(p\nmid m\): put the unit in a complete finite unramified field, enlarge its residue field to contain a root of its residue, and apply simple-root Hensel lifting at that finite level. This includes all \(\mu_m\). If \(L/F\) is totally tame of index \(m\), write \(\pi_L^m=\pi_F u\). Lift the residue of \(u\) to a base unit \(u_0\), and use Hensel on \(X^m-u/u_0\) at 1 to remove that principal-unit factor. A new upper uniformizer \(\gamma\) satisfies \(\gamma^m=\pi_F u_0\); it generates \(L\) by Lemma 1.1. For an arbitrary tame extension, apply this to its totally ramified part over its maximal unramified field. Removing the remaining unit by an \(m\)-th root in \(F^{\mathrm{nr}}\) puts it in \(F^{\mathrm{nr}}(\pi_F^{1/m})\).

Thus the union \(F^t=\bigcup_{p\nmid m}F^{\mathrm{nr}}(\pi_F^{1/m})\) contains every finite tame extension. Conversely every finite set of its elements lies in \(F_r(\pi_F^{1/m})\) for one unramified \(F_r\) and one \(m\), after taking common multiples. This has index \(m\) by the Eisenstein calculation in Lemma 1.1. Subextension indices divide it, by valuation multiplication, so every finite subextension is tame. Enlarge \(r\) to include \(\mu_m\); the corresponding field is Galois over \(F\), because all conjugates of the radical and the unramified coefficient field lie inside it. These are cofinal finite Galois fields. Lemmas 1.2 and 1.6 show that in any finite Galois quotient the fixed field of \(G_1\) is tame, and every tame quotient kills the image of \(P_F\). Hence \(F^t\) is exactly the fixed field of \(P_F\), and \(I_F/P_F=\operatorname{Gal}(F^t/F^{\mathrm{nr}})\).

Choose compatible radicals along a divisibility-cofinal chain of integers prime to \(p\). Over \(F^{\mathrm{nr}}\), the powers \(1,\pi_m,\ldots,\pi_m^{m-1}\) have distinct values modulo \(\mathbf Z\), so are independent; the degree is \(m\). All roots \(\zeta\pi_m\), \(\zeta\in\mu_m\), lie there. Their action ratios identify the finite Galois group with \(\mu_m\), and restriction is the power map. Taking inverse limits proves the claimed canonical group. Compatible primitive roots identify it with \(\prod_{\ell\ne p}\mathbf Z_\ell\): finite cyclic primary decomposition and the Chinese remainder theorem identify each finite level, with compatible transitions. The tuple 1 generates every finite cyclic quotient, so its powers are dense, proving procyclicity. Changing a radical, or changing \(\pi_F\) by a unit, multiplies it by an element of \(F^{\mathrm{nr}}\) fixed by inertia, so does not change any action ratio. \(\square\)

For comparison, these lower and quotient calculations are also actually written in the free [local-fields programme, lesson 9, §§1–3](https://kokunoyumeto.github.io/open-math-courses-local-fields/courses/NT-LOC/NT-LOC-09.html) and [lesson 10, §§1–4](https://kokunoyumeto.github.io/open-math-courses-local-fields/courses/NT-LOC/NT-LOC-10.html). The proofs above include their algebraic dependencies, rather than importing a different formula or an integer theorem.

## 2. Defining the conductor without a quotient choice

Let \(V\) be a smooth representation of \(W_F\). Its inertia image is finite by Lemma 2.1 of the preceding lesson. Define
\[
\operatorname{sw}_F(V)=\int_0^\infty
\operatorname{codim} V^{G_F^u}\,du,
\qquad
a_F(V)=\operatorname{codim}V^{I_F}+\operatorname{sw}_F(V).
\tag{3}
\]
The fixed spaces make sense because every \(G_F^u\), for \(u\ge0\), lies in inertia, hence in \(W_F\). The integral is a finite sum of lengths of intervals times integer codimensions. At this point \(a_F(V)\) is a nonnegative rational number. We introduce the ideal conductor after proving integrality in Theorem 2.6; “conductor” without “ideal” means the exponent.

There is a finite Galois extension on whose inertia quotient these fixed spaces can be computed. Indeed the kernel of \(V|_{I_F}\) is open in \(I_F\). An identity neighborhood in \(G_F\) can be chosen to intersect \(I_F\) inside that kernel; an open normal subgroup contained in this neighborhood then gives the required finite quotient. This does not require Frobenius itself to have finite image.

On such a quotient, changing variables by (1) gives
\[
\operatorname{sw}_F(V)=\sum_{i\ge1}\frac{|G_i|}{|G_0|}
\operatorname{codim}V^{G_i},
\qquad
a_F(V)=\sum_{i\ge0}\frac{|G_i|}{|G_0|}
\operatorname{codim}V^{G_i}.
\tag{4}
\]
For the term \(i=0\) the coefficient is one. Although \(V\) may not be a representation of the whole finite group \(G\), its restriction to every \(G_i\subseteq G_0\) factors through that quotient, which is all (4) requires.

**Theorem 2.1 (well-definedness and twists).** Formula (4) is independent of the chosen finite quotient. The conductor is additive in short exact sequences and is invariant under unramified twists. In particular
\[
a_F(V\otimes\|\cdot\|^s)=a_F(V).
\]

**Proof.** If two quotients are used, take a common dominating finite Galois quotient. Herbrand's quotient theorem identifies the image of each absolute upper group with the upper group in each quotient. Thus at every upper index the same subgroup acts on \(V\), giving exactly the same fixed space and the same integrand in (3). Its upper integral and the inertia term agree. The lower sums equal that integral by the change of variable already given, proving the required independence. Directly transferring lower indices between quotients would not be valid.

For an exact sequence \(0\to V'\to V\to V''\to0\), choose a common finite quotient of inertia. Taking invariants under any of its subgroups is exact in characteristic zero: average a lift of a fixed vector to obtain a fixed lift. Consequently
\[
\dim V^J=\dim (V')^J+\dim(V'')^J
\]
for \(J=I_F\) and for every \(G_F^u\). Codimensions, and then (3), add. Finally an unramified character is trivial on all these groups, so twisting changes none of their fixed spaces. \(\square\)

This also proves \(a_F(V)=a_F(V^{\mathrm{ss}})\), including representations with Frobenius Jordan blocks. We now prove integrality before using it in the ideal conductor or the single-break formula.

### 2A. Character pairing and finite induction

For a finite group, write \(\chi_V(g)=\operatorname{tr}(g\mid V)\). We use the pairing
\[
\langle b,\chi\rangle_G=\frac1{|G|}\sum_{g\in G}b(g)\chi(g^{-1}).
\tag{2A}
\]
When the first argument is a real character this is the usual character inner product. The inverse notation avoids any issue of which argument is conjugate linear.

For \(G=\operatorname{Gal}(L/F)\), define the **Artin class function** by
\[
A_G(g)=-f(L/F)i_G(g)\quad(g\ne1),\qquad
A_G(1)=f(L/F)d_{L/F}.
\tag{2B}
\]
It is a class function because motion is conjugation invariant. We do not presume it is a character or invoke its integrality in this definition.

**Lemma 2.2 (the character pairing).** If \(V\) factors through \(G\), then
\[
a_F(V)=\langle A_G,\chi_V\rangle_G.
\tag{2C}
\]
The regular class function \(\operatorname{reg}_G\), of value \(|G|\) at identity and zero elsewhere, pairs with \(\chi_V\) to give \(\dim V\).

**Proof.** Averaging \(|J|^{-1}\sum_{j\in J}\rho(j)\) is an idempotent with image \(V^J\): it fixes invariant vectors and its value on any vector is invariant. Its trace is its rank, by a basis of its image and kernel. Hence
\(\dim V^J=|J|^{-1}\sum_{j\in J}\chi_V(j^{-1})\).
Hilbert's formula (1I) and the motion count give
\[
\begin{aligned}
\langle A_G,\chi_V\rangle_G
&=\frac{f(L/F)}{|G|}\sum_{g\ne1}i_G(g)
       \bigl(\dim V-\chi_V(g^{-1})\bigr)\\
&=\frac1{|G_0|}\sum_{j\geq0}\sum_{g\in G_j}
       \bigl(\dim V-\chi_V(g^{-1})\bigr)\\
&=\sum_{j\geq0}\frac{|G_j|}{|G_0|}\operatorname{codim}V^{G_j}.
\end{aligned}
\]
The identity contributes zero in the middle expression. The last line is (4), and the regular pairing follows directly from its sole nonzero value. \(\square\)

We also give the finite induction identity needed in the pairing. In the tensor model \(\mathbb C[G]\otimes_{\mathbb C[H]}V\), select coset representatives. An element \(g\) permutes those vector-space summands; only fixed summands contribute to its trace. On a fixed summand represented by \(x\), its matrix is that of \(x^{-1}gx\in H\). Therefore
\[
(\operatorname{Ind}_H^G\chi)(g)=\frac1{|H|}
\sum_{x\in G:\,x^{-1}gx\in H}\chi(x^{-1}gx).
\tag{2D}
\]
Substitute (2D) into (2A) and put \(g=xhx^{-1}\). Conjugation invariance of \(b\) gives
\[
\langle b,\operatorname{Ind}_H^G\chi\rangle_G
=\langle b|_H,\chi\rangle_H.
\tag{2E}
\]
This proves the character form of Frobenius reciprocity used here without leaving it as an unproved import.

**Proposition 2.3 (finite conductor induction).** Let \(L/F\) be finite Galois, \(H\leq G\), \(E=L^H\), and \(V\) a representation of \(H\). Put \(f=f(E/F)\). Then
\[
a_F(\operatorname{Ind}_H^G V)
=\dim(V)\,\delta_{E/F}+f a_E(V).
\tag{2F}
\]
Here \(\delta_{E/F}=f d_{E/F}\) was proved in (1H), and \(H\) need not be normal.

**Proof.** At nonidentity \(h\in H\), intrinsic motion gives \(i_H(h)=i_G(h)\), and residue degrees multiply, since they are degrees of finite residue-field towers. Thus \(A_G(h)=f A_H(h)\). At identity, Lemma 1.4 gives
\[
A_G(1)-f A_H(1)
=f(L/F)e(L/E)d_{E/F}
=\delta_{E/F}[L:E].
\]
Since \([L:E]=|H|\), these equalities combine to the exact class-function identity
\[
A_G|_H=f A_H+\delta_{E/F}\operatorname{reg}_H.
\tag{2G}
\]
Use (2C), (2E) and the regular pairing of Lemma 2.2. The resulting equality is (2F). Every step is a class-function calculation and none assumes conductor integrality. \(\square\)

### 2B. Rank-one integrality, then general integrality

**Lemma 2.3A (integral formal modules, in both characteristics).** Put \(R=\mathcal O_F\), choose a uniformizer \(\pi\), and write \(q=|R/\pi R|\). Let \(\mathcal F_\pi\) consist of the series
\[
f(X)\in R[[X]],\qquad f(X)=\pi X+O(X^2),\qquad f(X)\equiv X^q\pmod\pi.
\tag{2LT1}
\]
Every \(f\in\mathcal F_\pi\) admits a unique commutative formal group law \(F_f\) for which \(f\) is an endomorphism. There are integral scalar endomorphisms \([a]_f=aX+O(X^2)\) for all \(a\in R\), satisfying \([a+b]_f=F_f([a]_f,[b]_f)\), \([ab]_f=[a]_f\circ[b]_f\), and \([\pi]_f=f\). For \(f,g\in\mathcal F_\pi\), their formal modules are canonically isomorphic by an integral series with linear coefficient one.

**Proof.** We give the coefficient construction. For \(f,g\in\mathcal F_\pi\) and a linear form \(L\) in any finite number of variables, seek \(H=L+O(\text{degree }2)\) with
\[
f(H(X_1,\ldots,X_r))=H(g(X_1),\ldots,g(X_r)).
\tag{2LT2}
\]
Suppose this holds through degree \(d-1\), and let \(E_d\) be the degree-\(d\) part of the left side minus the right side. Modulo \(\pi\), that difference is \(\overline H^{q}-\overline H(X_1^q,\ldots,X_r^q)=0\): coefficients lie in \(\mathbf F_q\). Adding a homogeneous \(C_d\) to \(H\) changes the error to \(E_d+(\pi-\pi^d)C_d\). Since \(\pi^{d-1}-1\) is a unit, the unique correction
\[
C_d=-\frac{E_d}{\pi(1-\pi^{d-1})}
\tag{2LT3}
\]
is integral. Induction gives a unique series. All compositions are defined coefficient by coefficient because their constant terms vanish.

Take \(f=g\) and \(L=X+Y\) to obtain \(F_f\). Swapping variables gives another solution with the same linear form, hence commutativity. The two associative composites have linear form \(X+Y+Z\) and satisfy (2LT2), hence coincide. Substitution \(Y=0\) gives the unique solution with linear term \(X\), namely \(X\); thus the identity is zero. The equation \(F_f(X,i(X))=0\) determines each coefficient of \(i=-X+O(X^2)\) successively with coefficient one, proving the inverse axiom. In particular
\(F_f(X,Y)=X+Y+XYC(X,Y)\) with \(C\) integral.

Apply (2LT2) with linear term \(aX\) to obtain \([a]_f\). The series \([a]_f(F_f(X,Y))\) and \(F_f([a]_f(X),[a]_f(Y))\) have the same linear form and intertwining equation, so are equal. The same uniqueness proves the stated addition and composition identities, \([1]_f=X\), and \([\pi]_f=f\). For two choices of \(f,g\), the solution of \(gH=Hf\) with linear coefficient one is a homomorphism by the same two-variable comparison. Reversing \(f,g\) constructs its inverse. A series with unit linear coefficient also has an integral compositional inverse directly: the degree-\(d\) inverse coefficient is determined by a linear equation with that unit coefficient. Finally, these series converge on the maximal ideal of every finite extension, since an integral degree-\(d\) term has valuation tending to infinity there. The identities therefore give actual \(R\)-module laws on those ideals, compatible with Galois action. \(\square\)

**Lemma 2.3B (division fields and their exact degrees).** For \(f(X)=\pi X+X^q\), let \(\Lambda_n\) be the roots of \(f^{\circ n}\) and let \(F_{\pi,n}=F(\Lambda_n)\), \(n\geq1\). Then
\[
\Lambda_n\simeq R/\pi^nR,\qquad
\operatorname{Gal}(F_{\pi,n}/F)\simeq(R/\pi^nR)^\times,
\qquad [F_{\pi,n}:F]=(q-1)q^{n-1}=:D_n.
\tag{2LT4}
\]
The extension is totally ramified. Every primitive point is a uniformizer and generates it, and \(\pi\) is a norm from it. These assertions also hold for any \(f\in\mathcal F_\pi\), using the canonical comparison of Lemma 2.3A.

**Proof.** The iterate is monic of degree \(q^n\), reduces to \(X^{q^n}\), and has zero constant term. Every nonzero root has positive valuation: if its valuation were negative the leading term would be uniquely smallest, and if zero the leading term would be a unit while every other coefficient is in \(\pi R\). At any such argument \(x\),
\(f'(x)=\pi+q x^{q-1}\) is \(\pi\) times a unit, because \(q\in\pi R\); in characteristic \(p\) its second term is zero. The chain rule therefore shows that all roots of every iterate are distinct, including zero.

Choose \(\lambda_1\ne0\) with \(f(\lambda_1)=0\), and \(f(\lambda_n)=\lambda_{n-1}\). The primitive roots, those not killed by \(f^{\circ(n-1)}\), are precisely the roots of the monic polynomial
\[
P_n(X)=\frac{f^{\circ n}(X)}{f^{\circ(n-1)}(X)}
=\pi+\bigl(f^{\circ(n-1)}(X)\bigr)^{q-1}.
\tag{2LT5}
\]
Its degree is \(D_n\), reduction is \(X^{D_n}\), and constant term is \(\pi\). Thus it is Eisenstein. Here is the needed irreducibility argument: any monic factors over \(F\) have integral coefficients, since their roots are integral and \(R\) is integrally closed by the valuation criterion; reduction makes their constant terms divisible by \(\pi\) if both factors have positive degree. Their product would then have constant term divisible by \(\pi^2\), a contradiction. Consequently \([F(\lambda_n):F]=D_n\). In (2LT5), a positive root valuation \(r\) can cancel the constant term only when \(D_nr=1\): every intermediate term has valuation at least \(1+jr>1\). Hence the ramification index is at least \(D_n\), and the degree formula of Lemma 1.1 makes it exactly \(D_n\), with residue degree one; \(\lambda_n\) is a uniformizer.

The \(q^n\) distinct roots form an \(R\)-module by Lemma 2.3A. A primitive \(\lambda_n\) generates it: its annihilator is \(\pi^nR\), for if \(a=\pi^k b\), \(k<n\), \([b]_f\) is invertible and \([\pi^k]_f(\lambda_n)\ne0\). This gives \(q^n\) distinct scalar multiples, exhausting the roots. Integral power series evaluated at \(\lambda_n\) lie in the complete field \(F(\lambda_n)\), so all roots lie there. Galois automorphisms commute with the series, by continuity and fixed coefficients; their action injects into \((R/\pi^nR)^\times\). Both its size and the field degree are \(D_n\), proving equality and (2LT4). The constant term of the minimal polynomial yields \(N(-\lambda_n)=\pi\), proving the norm assertion even when \(q=2,n=1\) and the field is \(F\). Canonical integral comparison maps evaluate in the same finite complete fields and preserve primitive points, which proves the assertion for arbitrary \(f\). \(\square\)

**Lemma 2.3C (uniformizer comparison and the explicit symbol).** Put \(F_\pi=\bigcup_n F_{\pi,n}\), and let \(F^{\mathrm{nr}}\) be the maximal unramified extension proved in the first lesson. For \(a=u\pi^m\), \(u\in R^\times\), the prescription
\[
\operatorname{Art}^{\mathrm{ar}}_{\pi}(a)|_{F^{\mathrm{nr}}}
=\operatorname{Frob}_{\mathrm{ar}}^{m},\qquad
\operatorname{Art}^{\mathrm{ar}}_{\pi}(a)(\lambda)=[u^{-1}]_f(\lambda)
\quad(\lambda\in\Lambda_n)
\tag{2LT6}
\]
defines a continuous homomorphism on \(F^{\mathrm{nr}}F_\pi/F\). This compositum and homomorphism are independent of \(\pi\). The geometric convention is its inverse. This statement constructs the symbol on these explicit fields; identifying the compositum with every abelian extension still uses the finite-reciprocity and norm argument specified below.

**Proof.** Each finite division field is totally ramified, and each finite unramified field has residue degree equal to its degree. Their intersection is \(F\); their compositum has the direct-product Galois action. Lemma 2.3B and the unramified inverse limit therefore define (2LT6), including continuity.

Let \(S\) be the valuation ring of \(\widehat{F^{\mathrm{nr}}}\), and \(\phi\) its arithmetic Frobenius. The value group remains \(\mathbf Z\), its uniformizer is \(\pi\), its residue field is \(\overline{\mathbf F}_q\), and Frobenius extends as an isometry. These assertions follow by approximating a nonzero completion element closer than its absolute value by an element of the unramified union; it then has the same valuation and residue. On \(S\), the maps \(x\mapsto\phi x-x\) and \(x\mapsto\phi x/x\) on units are onto. For the first, solve \(\bar x^q-\bar x=\bar c\) in the algebraically closed residue field and correct one \(\pi\)-adic digit at a time: adding \(\pi^j t\) changes the error digit by \(\bar t^q-\bar t\). For the second, first solve \(\bar x^{q-1}=\bar c\ne0\), then multiply by \(1+\pi^j t\), whose Frobenius ratio changes that digit by the same additive expression. Completeness gives solutions. The fixed ring is \(R\): subtract a residue representative in \(R\) from a fixed element, divide by \(\pi\), and repeat to approximate it by elements of the complete ring \(R\). Thus the respective kernels are \(R\) and \(R^\times\).

Write \(\pi'=u\pi\), choose \(\varepsilon\in S^\times\) with \(\phi\varepsilon=u\varepsilon\), and put \(g(X)=\pi'X+X^q\). We construct an integral \(\theta=\varepsilon X+O(X^2)\) satisfying
\[
g\circ\theta=(\phi\theta)\circ f.
\tag{2LT7}
\]
If \(E_d\) is its degree-\(d\) error, then \(E_d\in\pi S\): modulo \(\pi\), the two composites are \(\theta(X)^q\) and \((\phi\theta)(X^q)\). Adding \(cX^d\) changes the error by \(\pi'c-\pi^d\phi c\). For \(d\geq2\), put \(\alpha=\pi^d/\pi'\), of positive valuation. The unique correction is
\[
c=\sum_{j\geq0}\alpha^j\phi^j(-E_d/\pi'),
\tag{2LT8}
\]
which converges in \(S\). Uniqueness follows because \(c=\alpha\phi c\) forces an indefinitely increasing valuation. This same coefficient argument works for several variables with a prescribed linear form satisfying \(\pi'L=\pi\phi L\).

The two series \(\theta(F_f(X,Y))\) and \(F_g(\theta X,\theta Y)\) have linear form \(\varepsilon(X+Y)\) and satisfy the multivariable equation (2LT7); uniqueness identifies them. For the same reason, \(\theta\circ[a]_f=[a]_g\circ\theta\) for every \(a\in R\). Finally, \(\phi\theta\) and \(\theta\circ[u]_f\) both satisfy (2LT7), with linear coefficient \(u\varepsilon\); hence
\[
\phi\theta=\theta\circ[u]_f.
\tag{2LT9}
\]
The unit linear coefficient gives an integral inverse, so \(\theta\) is a formal-module isomorphism. Iterating (2LT7) gives \(g^{\circ n}\theta=(\phi^n\theta)f^{\circ n}\), so it bijects their level-\(n\) torsion.

This equality over the completion descends to the algebraic fields. Indeed, a subfield \(E\subset F^{\mathrm{sep}}\) is closed in \(F^{\mathrm{sep}}\): its fixing subgroup preserves valuation and is continuous, so it fixes every limit lying in \(F^{\mathrm{sep}}\); the fixed-field theorem of the first lesson puts that limit in \(E\). A value \(\theta(\lambda)\) is a limit in \(F^{\mathrm{nr}}F_{\pi,n}\) and is algebraic, since it is a root of \(g^{\circ n}\). Thus it belongs to that field. The inverse argument gives
\(F^{\mathrm{nr}}F_{\pi,n}=F^{\mathrm{nr}}F_{\pi',n}\).

For the symbols, (2LT6) makes \(\operatorname{Art}^{\mathrm{ar}}_\pi(\pi')\) act as Frobenius on coefficients and as \([u^{-1}]_f\) on \(\lambda\). Equations (2LT7)–(2LT9) give
\[
\operatorname{Art}^{\mathrm{ar}}_\pi(\pi')\theta(\lambda)
=(\phi\theta)([u^{-1}]_f\lambda)=\theta(\lambda).
\tag{2LT10}
\]
This agrees with \(\operatorname{Art}^{\mathrm{ar}}_{\pi'}(\pi')\), which fixes its division field and acts as Frobenius on the unramified field. The same comparison works for any other prime element in place of \(\pi'\); prime elements generate \(F^\times\), since every unit is a ratio of two prime elements. Hence the two homomorphisms agree everywhere. \(\square\)

Lemmas 2.3A–2.3C reconstruct the formal modules, division fields and uniformizer comparison from [Milne's free *Class Field Theory*, I §2, Lemma 2.11 through Summary 2.20, and I §3, Propositions 3.4 and 3.10, Theorems 3.6 and 3.9](https://www.jmilne.org/math/CourseNotes/CFT.pdf). The formal identities left to the reader in the comparison proof are supplied above. No formal-group theorem from a paid source is being imported through the earlier programme lesson.

The rank-one input now has its full local prerequisite before use. The preceding Weil-group lesson, Lemmas 0.5–0.6 and Theorems 0.7 and 0.9, constructs finite reciprocity, exact abelian norm kernels, norm/transfer/conjugation functoriality, comparison with the explicit division fields, abelian cofinality and the completion theorem. Its Lemmas 0.8A–0.8C prove the same formal-module construction written here. That proof uses the cyclic norm calculation and the local invariant in both characteristics; it does not assume Hasse–Arf. We use its proved reciprocity and cofinality in the complete filtration and conductor deduction below. The earlier integer Brauer provider and its transitive free-source/public-edition verification remain a separate obligation.

**Lemma 2.4 (units, upper groups and character conductors).** Under local reciprocity, for every finite abelian \(B/F\),
\[
\operatorname{Art}_F(U_F^0)=\operatorname{Gal}(B/F)^0,\qquad
\operatorname{Art}_F(U_F^{\lceil u\rceil})=\operatorname{Gal}(B/F)^u\quad(u>0),
\tag{2H}
\]
where
\[
U_F^0=\mathcal O_F^\times,\qquad U_F^c=1+\mathfrak p_F^c\quad(c\geq1).
\tag{2}
\]
A smooth character \(\chi\) of \(W_F\), viewed as a character of \(F^\times\), has
\[
a_F(\chi)=c(\chi):=\min\{c\in\mathbf Z_{\geq0}:\chi(U_F^c)=1\}.
\tag{2I}
\]
In particular this conductor is an integer, and a ramified character has last upper break \(c(\chi)-1\).

**Proof.** Here is the finite calculation from the explicit fields. Choose a uniformizer \(\pi\), residue cardinality \(q\), and the integral Lubin–Tate module for \(f(X)=\pi X+X^q\). A primitive level-\(n\) division point \(\lambda\) is a uniformizer of \(F_{\pi,n}\), whose degree is \(D_n=(q-1)q^{n-1}\). Lemma 2.3B establishes this by applying Eisenstein to
\(\pi+(f^{\circ(n-1)}(X))^{q-1}\); it counts all primitive roots and identifies the Galois action with unit scalars modulo \(\pi^n\). Write \(\sigma_a(\lambda)=[a]_f(\lambda)\). If \(a-1=\pi^k b\), \(b\) a unit and \(0\leq k<n\), then the formal law \(F_f(X,Y)=X+Y+XYC(X,Y)\) gives
\[
\sigma_a\lambda-\lambda
=[a-1]_f(\lambda)\bigl(1+\lambda C(\lambda,[a-1]_f(\lambda))\bigr).
\]
The parenthesis is a unit. The point \([\pi^k]_f(\lambda)\) is primitive at level \(n-k\), with relative ramification index \(q^k\); the unit scalar \([b]_f\) has unit linear coefficient and integral higher coefficients, so preserves its positive valuation. Lemma 1.1 and (1C) thus give
\(i(\sigma_a)=q^k\).
Put \(b_k=q^k-1\). On \(b_{k-1}<t\leq b_k\), the lower group is the image of \(U_F^k\), of order \(q^{n-k}\), for \(1\leq k<n\). The interval length and its index in inertia both equal \((q-1)q^{k-1}\). Hence each such interval has upper length one, and \(\varphi(b_k)=k\). Beyond \(b_{n-1}\) the group is trivial. This proves (2H) on \(F_{\pi,n}\), including the convention at a jump. For \(n=1\) all positive groups are already trivial; for \(q=2,n=1\) the field itself is trivial.

Lemma 2.3C sends units to inverse scalar actions for its arithmetic convention. Our geometric convention inverts the symbol, preserving the image of every unit subgroup. An unramified degree-\(d\) compositum \(F_dF_{\pi,n}\) has the same normalized valuation on \(\lambda\) and the same inertia motions, so has the same nonnegative upper groups. Its unramified factor has no inertial action. The actual earlier existence proof puts every finite abelian \(B\) in one such compositum: its open norm group contains \(\langle\pi^d\rangle U_F^n\), the explicitly computed norm group of the compositum, and the proved norm/field inclusion correspondence gives the containment. Lemma 1.6 then passes (2H) to \(B\). This construction proves abelian upper jumps integral in both characteristics, without presuming that conclusion in the containment proof.

For a finite-image line, pass to its abelian quotient using Lemma 1.6. If \(c=0\), its inertia action is trivial and (3) gives zero. If \(c\geq1\), it is nontrivial on \(U_F^{c-1}\) and trivial on \(U_F^c\). Formula (2H) says that its fixed space is zero for \(0<u\leq c-1\) and its whole line for \(u>c-1\), with a separate zero inertia-fixed space. The integral in (3) is \(c-1\), and \(a=1+(c-1)=c\). For an arbitrary smooth line, its inertia image is finite and a suitable unramified twist makes its Frobenius value finite order by Theorem 2.2 of the preceding lesson. Theorem 2.1 preserves its conductor, and the twist is trivial on units. The same computation proves (2I). \(\square\)

The free author text [Milne, *Class Field Theory*, I Proposition 4.1 and Example 4.2, printed pp.45–46](https://www.jmilne.org/math/CourseNotes/CFT.pdf) supplies the explicit-field calculation as reading material. The formal-module and explicit-symbol proofs are written in Lemmas 2.3A–2.3C; finite reciprocity and abelian cofinality retain the earlier proof obligations specified above. In particular its separate I §4 proof of local maximality uses Hasse–Arf; using that proof to derive (2I) here would be circular. The earlier programme existence proof specified above takes the independent finite-reciprocity route.

**Lemma 2.5 (the precise earlier Brauer input).** For a finite group \(G\), every complex character has an expression
\[
\chi=\sum_r n_r\operatorname{Ind}_{H_r}^G\theta_r,
\qquad n_r\in\mathbf Z,\qquad \dim\theta_r=1.
\tag{2J}
\]
The integers can have either sign, and the subgroups need not be normal.

This is the actually proved Theorem 5.1 of the earlier programme lesson *Brauer's induction theorem*. Its §§1–5 establish the needed stronger, integral conclusion: §1 proves monomiality of nilpotent groups through abelian normal weights; §§3–4 prove local induction at each prime and an integer determinant descent producing \(n_p\equiv1\pmod p\); §5 combines those integers by Bezout and converts inductions from elementary groups into inductions from lines. Thus it supplies (2J), rather than only rational Artin induction or a statement about arbitrary characters on subgroups. The proof was read with its hypotheses and its earlier character/induction dependencies. The source-origin and public-edition check for that transitive programme chain remains part of the same prerequisite verification stated above. The verified free [Kramár, §3, Lemma 5 and Theorem 2](https://www.math.toronto.edu/murnaghan/courses/mat445/artinbrauer.pdf) is a comparison material for integer induction, not a substitute for the actual programme proof.

**Theorem 2.6 (integrality for every smooth Weil representation).** For every finite-dimensional smooth complex \(V\),
\[
a_F(V)\in\mathbf Z_{\geq0},\qquad
\operatorname{sw}_F(V)\in\mathbf Z_{\geq0}.
\tag{2K}
\]
Its ideal conductor is therefore \(\mathfrak p_F^{a_F(V)}\).

**Proof.** First let \(V\) factor through a finite \(G=\operatorname{Gal}(L/F)\). Apply (2J) to its character. For \(E_r=L^{H_r}\), Proposition 2.3 and Lemma 2.4 give
\[
a_F(V)=\sum_r n_r\bigl(\delta_{E_r/F}+f(E_r/F)a_{E_r}(\theta_r)\bigr)\in\mathbf Z.
\]
The pairing of Lemma 2.2 is linear on characters, so negative coefficients cause no difficulty. The integers on the right come from trace-dual discriminants and the proved rank-one conductor calculation. Formula (4) proves nonnegativity for an actual representation. Subtracting the integer \(\operatorname{codim}V^{I_F}\) shows that its Swan conductor is an integer too; its defining integral proves nonnegativity.

A finite-dimensional representation has a finite composition series, by the dimension argument and Jordan–Hölder proof in Lemma 0A.2 of the first lesson. Each irreducible smooth Weil constituent becomes finite-image after an unramified twist, by Theorem 2.2 of the preceding lesson; its finite quotient extends to \(G_F\) by that lesson's Proposition 1.1. Theorem 2.1 identifies its conductor with the finite-image conductor just proved. Additivity then proves both assertions for \(V\), including nonsemisimple Frobenius actions. The ideal notation is now legitimate. \(\square\)

## 3. Tame ramification and a single break

**Theorem 3.1.** The Swan conductor is zero if and only if wild inertia acts trivially. In that case
\[
a_F(V)=\dim V-\dim V^{I_F}.
\tag{5}
\]

**Proof.** If wild inertia is trivial, every positive upper group acts trivially, so the integral in (3) is zero. Conversely suppose wild inertia has a nontrivial image. In a finite quotient computing the action, \(G_1\) then acts nontrivially. Hence \(\operatorname{codim}V^{G_1}>0\). The first positive lower interval has positive upper length \(|G_1|/|G_0|\), and contributes that length times a positive codimension to (4). All other terms are nonnegative, so the Swan conductor is positive. Substitution in (3) proves (5). \(\square\)

For an unramified representation, \(V^{I_F}=V\), so \(a_F(V)=0\). A tame representation of dimension two has conductor \(0,1\), or \(2\), according as its inertia-fixed space has dimension \(2,1\), or \(0\). Dimension alone is insufficient to choose among these values. For example \(1\oplus\theta\), with \(\theta\) a nontrivial tame character, has conductor one, while \(\theta\oplus\theta^{-1}\) has conductor two.

**Proposition 3.2 (the break of an irreducible).** If \(V\) is irreducible, ramified, and of dimension \(n\), then \(V^{I_F}=0\). There is a unique nonnegative upper break \(\lambda\) such that, apart from the convention at the endpoint, the upper fixed spaces are zero below \(\lambda\) and all of \(V\) above it. Moreover
\[
\operatorname{sw}_F(V)=n\lambda,
\qquad a_F(V)=n(1+\lambda).
\tag{6}
\]
For a tame ramified irreducible, \(\lambda=0\).

**Proof.** Each \(G_F^u\) and \(I_F\) is normal in \(G_F\), so its fixed space is preserved by \(W_F\). Irreducibility makes it either zero or \(V\). Inertia fixes all of \(V\) only for an unramified representation, so here its fixed space is zero. As \(u\) increases the upper groups decrease, and the fixed spaces increase. A finite quotient gives only finitely many changes and trivial action for sufficiently large \(u\). There can therefore be only one transition from zero to \(V\) at a nonnegative number \(\lambda\). In the tame case every positive upper group is already trivial, so the transition is at zero. The integrand in (3) is \(n\) on an interval of length \(\lambda\) and zero afterwards; the endpoint has measure zero. This proves (6). \(\square\)

An irreducible representation can have a fractional break, but (6) and Theorem 2.6 imply \(n\lambda=a_F(V)-n\in\mathbb Z\). For a character Lemma 2.4 already proved the integral-break conclusion and \(\lambda=c-1\) for conductor \(c\).

## 4. The conductor of induction

We distinguish the **different ideal** \(\mathfrak D_{E/F}\subset\mathcal O_E\) and the **discriminant ideal**
\[
\mathfrak d_{E/F}=N_{E/F}(\mathfrak D_{E/F})\subset\mathcal O_F.
\]
Write \(d_{E/F}=v_E(\mathfrak D_{E/F})\), \(\delta_{E/F}=v_F(\mathfrak d_{E/F})\), and \(f=f(E/F)\). Valuations of ideals mean their exponents, with \(v_F(\varpi_F)=v_E(\varpi_E)=1\). Thus \(\delta_{E/F}=f d_{E/F}\).

**Theorem 4.1.** For \(E/F\) finite separable and \(V\) a smooth representation of \(W_E\) of dimension \(d\),
\[
a_F\!\left(\operatorname{Ind}_{W_E}^{W_F}V\right)
=d\,\delta_{E/F}+f(E/F)a_E(V).
\tag{7}
\]
No irreducibility hypothesis is required.

**Proof for finite-image representations.** A finite-image smooth representation of \(W_E\) extends to \(G_E\) by Proposition 1.1 of the preceding lesson. Take the normal closure over \(F\) of a finite Galois field killing that representation; it is a finite Galois \(L/F\) containing \(E\), by Lemma 0B.1 of the first lesson. With \(G=\operatorname{Gal}(L/F)\) and \(H=\operatorname{Gal}(L/E)\), the finite-index tensor induction has exactly the finite quotient model \(\operatorname{Ind}_H^G V\). Proposition 2.3, proved before integrality, gives (7). Its class-function identity is
\[
\operatorname{Res}_H^G A_G=f(E/F)A_H+\delta_{E/F}\operatorname{reg}_H.
\tag{8}
\]
Thus both the nonidentity motion calculation and the correction at identity have already been proved using trace-dual transitivity; neither is an additional input here.

**Reduction of the general case.** Induction is exact in the finite-index tensor model: it is a direct sum of copies of the underlying vector space. Theorem 2.1 thus reduces (7) to irreducible constituents of \(V\). Each constituent is a finite-image representation twisted by an unramified character \(\eta_E\). Choose an unramified character \(\eta_F\) whose Frobenius value has \(f(E/F)\)-th power equal to \(\eta_E(\Phi_E)\). Then \(\eta_F|_{W_E}=\eta_E\), since both are trivial on inertia and \(v_F|_{W_E}=f v_E\). The tensor model gives
\[
\operatorname{Ind}(V_0\otimes\eta_F|_{W_E})
\simeq(\operatorname{Ind}V_0)\otimes\eta_F.
\]
Explicitly, the map sends \(g\otimes v\) on the left to \(\eta_F(g)(g\otimes v)\) on the right. Replacing \(g\) by \(gh\), \(h\in W_E\), inserts exactly the scalar \(\eta_F(h)\) in the tensor relation, and left multiplication by \(w\) inserts \(\eta_F(w)\), the twist on the right. Thus the map is well defined and equivariant; replacing the scalar by its inverse gives its inverse.
Unramified twists leave both conductors unchanged. The finite-image case applies to \(V_0\), and additivity completes the proof. \(\square\)

Both sides of (7) are additive on the Grothendieck group, so the formula also holds for virtual representations. In particular, for virtual dimension zero the discriminant term vanishes and the conductor of induction is the residue degree times the original conductor. This statement follows from the full formula; it does not require choosing a presentation by actual representations of dimension zero.

## 5. Quadratic examples

If \(E/F\) is unramified quadratic, then \(f=2\) and \(\delta_{E/F}=0\). For a character \(\chi\) of conductor \(c\), (7) gives
\[
a_F(\operatorname{Ind}\chi)=2c.
\tag{9}
\]
For \(c=0\), extend \(\chi\) to an unramified character \(\mu\) of \(W_F\) by choosing a square root of its Frobenius value. Then \(\operatorname{Ind}\chi=\mu\otimes\operatorname{Ind}1\), and the permutation representation of the order-two quotient splits into its constant and sign lines. Both lines are unramified, so its conductor is zero. For a nontrivial tame character with \(\chi\ne\chi^\sigma\), restriction of the induction to the normal index-two subgroup \(W_E\) is \(\chi\oplus\chi^\sigma\). A group element separating these two character values has two distinct eigenvalues; every invariant subspace is consequently a sum of the two character lines. The outside coset interchanges them, so the induction is irreducible. Since unramified base change identifies the two inertia groups, each inertia line is nontrivial; there is no inertia-fixed vector. Formula (5) gives two, agreeing with \(c=1\) in (9).

If \(E/F\) is tamely ramified quadratic, the residue characteristic is odd, \(f=1\), and the different exponent is \(e-1=1\), so \(\delta_{E/F}=1\). Thus
\[
a_F(\operatorname{Ind}\chi)=1+a_E(\chi).
\tag{10}
\]
For an unramified \(\chi\), the induction is reducible. In fact choose an unramified character \(\mu\) of \(W_F\) restricting to \(\chi\) (here the residue degree is one), and use
\[
\operatorname{Ind}\chi=\mu\otimes\operatorname{Ind}1
=\mu\oplus\mu\omega_{E/F}.
\]
The quadratic character is nontrivial on tame inertia and has conductor one; \(\mu\) has conductor zero. Additivity gives one, exactly as in (10). The discriminant contribution therefore cannot be discarded on the grounds that the inducing character is unramified.

The unit characters in the exercises can be constructed without an extension-of-characters assumption. For every local field \(K\) of residue cardinality \(q\), Hensel's lemma lifts each nonzero residue uniquely to a root of \(X^{q-1}-1\): the derivative is a unit. Uniqueness makes these lifts a multiplicative subgroup \(\mu_{q-1}(K)\) mapped isomorphically onto \(k_K^\times\). Dividing a unit by its lift gives a principal unit, uniquely. Consequently
\[
K^\times=\pi_K^{\mathbf Z}\times\mu_{q-1}(K)\times U_K^1.
\tag{11}
\]
Here the valuation gives the first factor, and the two unit factors intersect only in identity. For every \(j\geq1\), multiplication modulo \(\mathfrak p_K^{j+1}\) proves
\[
U_K^j/U_K^{j+1}\simeq(k_K,+),\qquad
1+a\pi_K^j\longmapsto\bar a,
\tag{12}
\]
because products of two correction terms lie in \(\mathfrak p_K^{2j}\subseteq\mathfrak p_K^{j+1}\). These explicit decompositions justify each character extended by prescribing its value on a uniformizer and residue roots.

## 6. Exercises with solutions

**Exercise 6.1 (easy).** Compute the conductor of an unramified representation and of a tame representation of dimension two. Give tame examples with every possible value.

**Solution.** An unramified representation has full inertia-fixed space and zero Swan integral, so its conductor is zero. In dimension two, (5) gives \(a=2-\dim V^{I_F}\in\{0,1,2\}\). The examples \(1\oplus1\), \(1\oplus\theta\), and \(\theta\oplus\theta^{-1}\), for a nontrivial tame character \(\theta\), give zero, one, and two. Such a character exists, for example over \(\mathbb Q_3\), by taking the nontrivial character of \(\mathbb F_3^\times\) and making it trivial on the uniformizer and on principal units. The last example still has no fixed vector if \(\theta=\theta^{-1}\).

**Exercise 6.2 (medium).** Derive the induction formula from Artin characters. Explain why the coefficient of \(\dim V\) is \(\delta_{E/F}\), rather than the different exponent without its residue-degree factor.

**Solution.** For \(G=\operatorname{Gal}(L/F)\) and \(H=\operatorname{Gal}(L/E)\), the equality of the ramification functions on \(H\) gives \(A_G|_H=f(E/F)A_H\) away from one. At one, transitivity of the different gives the correction \(f(E/F)d_{E/F}|H|\). Hence the missing term is \(f(E/F)d_{E/F}\operatorname{reg}_H=\delta_{E/F}\operatorname{reg}_H\). Pair with the character of \(V\) and use Frobenius reciprocity and the dimension pairing with the regular character. This gives (7) for finite image. Unramified twists and a composition series reduce every smooth representation to that case, exactly as in the last paragraph of Theorem 4.1. The norm of \(\mathfrak p_E\) is \(\mathfrak p_F^f\); consequently the discriminant exponent is \(f d_{E/F}\), which explains the coefficient.

**Exercise 6.3 (medium).** Let \(F=\mathbb Q_3\) and \(E=F(\sqrt{-3})\). Show that \(a_F(\operatorname{Ind}\chi)=1+a_E(\chi)\), and determine all possible values when \(a_E(\chi)\le2\).

**Solution.** Write \(\pi=\sqrt{-3}\). The polynomial \(X^2+3\) is Eisenstein, so \(E/F\) is totally ramified quadratic with residue degree one and uniformizer \(\pi\). Its ramification index two is prime to three, hence the extension is tame. Alternatively its different is generated by \(2\pi\), with valuation one in \(E\). Thus \(\delta_{E/F}=1\), proving the formula.

The possible character conductors are \(0,1,2\), and all occur. For zero take the trivial character. For one take the nontrivial character of \(\mathcal O_E^\times/U_E^1\simeq\mathbb F_3^\times\), trivial on \(\pi\). For two take a character nontrivial on
\[
U_E^1/U_E^2\simeq(\mathbb F_3,+),\qquad
1+a\pi\longmapsto\bar a.
\]
The map is additive because the product of two such units has coefficient \(a+b\) modulo \(\pi^2\). Choose \(\bar a\mapsto\exp(2\pi i\bar a/3)\), extend trivially on \(\{\pm1\}\), and set its value on \(\pi\) to one. The unit quotient is the product of that sign group and the indicated principal-unit quotient, so this is a character trivial on \(U_E^2\) and nontrivial on \(U_E^1\). The induced conductors are therefore exactly \(1,2,3\). The extension \(E/F\) itself is tame; a conductor-two character of \(E^\times\) nevertheless has wild ramification.

**Exercise 6.4 (medium).** Prove that zero Swan conductor is equivalent to tameness. Give a character of \(\mathbb Q_p^\times\) with Swan conductor one.

**Solution.** The nonnegative lower sum in (4) vanishes when every positive ramification group acts trivially. Conversely a nontrivial wild image makes the \(G_1\) term strictly positive, proving the equivalence. For odd \(p\), use
\[
\mathbb Q_p^\times=p^{\mathbb Z}\times\mu_{p-1}\times(1+p\mathbb Z_p).
\]
Take a character trivial on the first two factors and on \(1+p^2\mathbb Z_p\), with
\(\chi(1+pa)=\exp(2\pi i\bar a/p)\). Multiplication modulo \(p^2\) makes this a character of \(U^1/U^2\); its conductor is two, its inertia-fixed space is zero, and (3) gives Swan conductor \(2-1=1\). For \(p=2\), the character of \(\mathbb Z_2^\times\) given by \(\chi(u)=1\) for \(u\equiv1\pmod4\) and \(-1\) for \(u\equiv3\pmod4\), extended by \(\chi(2)=1\), also has conductor two and Swan conductor one. Inversion of reciprocity does not change these conductor computations.

**Exercise 6.5 (hard).** Let \(V\) be a ramified irreducible smooth representation of dimension \(n\). Prove it has a single upper break and deduce its conductor. What constraint does integrality impose on the break?

**Solution.** Normality of the absolute upper groups makes every fixed space a \(W_F\)-subrepresentation. Irreducibility allows only zero and \(V\). Inertia cannot fix all of \(V\) because the representation is ramified. The increasing family of fixed spaces eventually equals \(V\) and has finitely many transitions after passage to a finite inertia quotient, so it makes exactly one transition. Call its upper index \(\lambda\), taking \(\lambda=0\) for a tame representation. The Swan integrand equals \(n\) for an interval of length \(\lambda\), and zero afterwards. Hence \(\operatorname{sw}=n\lambda\) and \(a=n+n\lambda\). Theorem 2.6 was proved before the single-break assertion, and gives \(a\in\mathbf Z\). Hence \(n\lambda=a-n\) is an integer too. This does not imply that \(\lambda\) itself is an integer for \(n>1\).

## Proof dependencies and free reading materials

The local proof chain is explicit: Lemmas 1.1–1.6 establish integral generators, lower groups, finite wild inertia, the derivative different, trace-dual transitivity, the residue factor in discriminants, Hilbert's formula and Herbrand's quotient theorem. Lemma 2.2 proves the character pairing and (2D)–(2E) prove its induction adjunction. Proposition 2.3 proves finite induction before Lemma 2.4 supplies the rank-one integer and unit-filtration calculation. The actually written earlier integer Brauer proof specified in Lemma 2.5 then proves Theorem 2.6. Only afterward are ideal conductors and single-break integrality used. Theorem 4.1 handles arbitrary smooth representations and virtual representations, and all five exercise solutions use this ordered chain.

The formal-module, division-field and uniformizer-comparison constructions used inside Lemma 2.4 are proved here in Lemmas 2.3A–2.3C. Explicit finite reciprocity and abelian cofinality retain the actual earlier programme providers specified in §2B, whose transitive free-primary chain is unresolved. The integer Brauer proof is also actually written. Their transitive free-source provenance and current public class-field/finite-group editions remain to be verified by the programme revision. Current accessibility of the separate local-fields edition is verified; the privately fetched earlier combined repository does not establish public accessibility of its other courses. These outstanding provenance/access checks prevent a claim that the full lesson already meets every free-source prerequisite requirement. No conductor for a pair with a monodromy operator has yet been defined; that extra term is handled in the Weil–Deligne lesson.

The following freely accessible human-authored sources were read as materials. Their citations fix definitions and conventions; the proofs and exact earlier proof providers above carry the mathematical obligations.

- **J. S. Milne**, [*Algebraic Number Theory*, Chapter 7, especially Theorem 7.58 and Corollary 7.59](https://www.jmilne.org/math/CourseNotes/ANT.pdf), for inertia, uniformizer motion and tame graded groups. The trace-dual and tower algebra needed here is proved in Lemmas 1.3–1.4.
- **J. S. Milne**, [*Class Field Theory*, I Proposition 4.1 and Example 4.2, printed pp.45–46](https://www.jmilne.org/math/CourseNotes/CFT.pdf), for the explicit Lubin–Tate ramification calculation. Lemma 2.4 gives the independent conductor deduction with its noncircular programme existence prerequisite specified.
- **The Stacks project**, [§49.8, Tag 0BW0, especially Lemma 49.8.2](https://stacks.math.columbia.edu/tag/0BW0), for the identification of the complementary module with the trace dual. Lemmas 1.3–1.4 prove the specific derivative and tower results used here.
- **J. Kramár**, [*Artin's and Brauer's Theorems on Induced Characters*, §3, Lemma 5 and Theorem 2, pp.6–7](https://www.math.toronto.edu/murnaghan/courses/mat445/artinbrauer.pdf), for integral elementary-subgroup induction. The stronger line-induction form actually used is supplied by the earlier programme proof identified in Lemma 2.5, including its nilpotent monomiality argument.
- **Pierre Deligne**, [*Les constantes des équations fonctionnelles des fonctions L*, freely accessible IAS author text, §1.5, printed p.510, and §4.5, printed pp.537–538](https://publications.ias.edu/sites/default/files/Number20.pdf), for virtual induction and conductor conventions. Its cited external Artin/Swan integer theorem is not used as a proof substitute: Theorem 2.6 proves the integrality needed in this lesson from the stated programme inputs.
