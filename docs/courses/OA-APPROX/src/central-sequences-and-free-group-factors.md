# Central sequences, fullness and free group factors

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-checked relative to the stated prerequisites; not independently reviewed. New original text: public domain (CC0).*

In the [hyperfinite finite factor](hyperfinite-finite-factors.md), a trace-zero operator can move farther and farther into the tensor tail and almost commute with every fixed operator. A free group factor has the opposite behavior: commutation with just two generators controls the entire distance from the scalars. We first develop the topological criterion that turns this estimate into closedness of the inner automorphism group.

Foundational inputs are normal functional decomposition, faithful normal state GNS representations, Kaplansky density, center-valued traces on finite algebras and the intrinsic strong* topology. The only descriptive-set-theory input is the Lusin–Souslin theorem: a continuous injection between Polish spaces carries Borel sets to Borel sets. Its selected full proof is compared with the foundations producer, with topology refinement and separation retained as prerequisites. Baire's theorem for complete metric spaces is also used. General modular or expectation theory is not developed here.

## 1. Two meanings of almost commuting

For \(\omega\in M_*\) put
\[
(x\omega)(y)=\omega(yx),\qquad
(\omega x)(y)=\omega(xy),\qquad
[x,\omega]=x\omega-\omega x.
\tag{1}
\]
For \(\psi\in M_*^+\), write \(\|x\|_\psi=\psi(x^*x)^{1/2}\). Strong* convergence on bounded sets is convergence of both \(\|x\|_\psi\) and \(\|x^*\|_\psi\) for every such \(\psi\).

A norm-bounded sequence \((x_n)\) is **central** if \([x_n,a]\to0\) strong* for every \(a\in M\). It is **centralizing** if \(\|[x_n,\omega]\|\to0\) for every \(\omega\in M_*\). A sequence is **trivial** if \(x_n-z_n\to0\) strong* for some bounded sequence \(z_n\in Z(M)\).

**Lemma 1.1.** Every centralizing sequence is central. If \(M\) has a faithful normal state \(\varphi\), a central sequence is centralizing whenever \(\|[x_n,\varphi]\|\to0\).

**Proof.** For \(x,a\in M\) and \(\psi\ge0\), expansion and insertion of two intermediate terms give
\[
\psi([x,a]^*[x,a])
\le 2\|x\|\|a\|\|[x,a\psi]\|
 +2\|x\|\|a\|^2\|[x,\psi]\|.
\tag{2}
\]
Here \(a\psi(y)=\psi(ya)\). To check the expansion, write the left side as
\(\psi(a^*x^*[x,a])-\psi(x^*a^*[x,a])\). The first term has absolute value at most
\
|[x,a\psi|+|x,\psi|,
\]
after inserting \(\psi(xa^*x^*a)\). For the second insert \(\psi(xx^*a^*a)\), giving
\
|[x,a\psi|+|x,\psi|.
\]
These bounds prove (2).

If \(x_n\) is centralizing, the right side tends to zero. The identity
\[
\|[x^*,\omega]\|=\|[x,\omega^*]\|,
\qquad \omega^*(y)=\overline{\omega(y^*)},
\tag{3}
\]
shows that \(x_n^*\) is also centralizing. Applying (2) to \(x_n^*,a^*\) gives the adjoint seminorm. This proves centrality for arbitrary \(M\).

For the converse under the state hypothesis, \(M\varphi=\{a\varphi:a\in M\}\) is norm dense in \(M_*\). Indeed, its annihilator in \(M=(M_*)^*\) consists of \(y\) with \(\varphi(ya)=0\) for every \(a\); taking \(a=y^*\) and using faithfulness gives \(y=0\). Hahn–Banach proves the density. Now
\[
[x_n,a\varphi]=[x_n,a]\varphi+a[x_n,\varphi],
\tag{4}
\]
and Cauchy–Schwarz gives
\[
\|b\varphi\|\le\varphi(1)^{1/2}\|b\|_\varphi.
\tag{5}
\]
Both terms in (4) tend to zero. The uniform bound \(\|[x_n,\omega]\|\le2C\|\omega\|\), where \(\|x_n\|\le C\), extends the conclusion to every functional. \(\square\)

**Corollary 1.2.** In every finite von Neumann algebra, central and centralizing bounded sequences coincide. No separability or countable decomposition is required.

**Proof.** If there is a faithful normal tracial state, its commutator in (1) is zero and Lemma 1.1 applies. For an arbitrary finite algebra let \(T_Z:M\to Z(M)\) be its faithful normal center-valued trace. Given a nonzero \(\psi\in M_*^+\), let \(z\) be the support of \(\psi|_{Z(M)}\). On \(Mz\),
\[
\tau_z(x)=\frac{\psi(T_Z(x))}{\psi(z)}
\tag{6}
\]
is a faithful normal tracial state: \(\psi|_{Z(M)z}\) and \(T_Z|_{Mz}\) are faithful. The central sequence \(zx_n\) is centralizing there by the first case. Since \(\psi(1-z)=0\), Cauchy–Schwarz gives \(\psi(y)=\psi(zyz)\), and its commutators on \(M\) are precisely the corresponding commutators on \(Mz\). Thus \(\|[x_n,\psi]\|\to0\). Decomposing an arbitrary normal functional into four positive ones finishes the proof. \(\square\)

Centralizing sequences form a unital \(C^*\)-subalgebra of \(\ell^\infty(\mathbb N,M)\). Adjoints are covered by (3), products by
\[
[xy,\omega]=x[y,\omega]+[x,\omega]y,
\tag{7}
\]
and closure by the uniform commutator bound. Continuous functional calculus on a fixed spectral interval follows by polynomial approximation. Every self-adjoint contraction \(h_n\) in this algebra is the real part of the centralizing unitary
\[
w_n=h_n+i(1-h_n^2)^{1/2}.
\tag{8}
\]
Real and imaginary parts therefore reduce arbitrary bounded centralizing sequences to linear combinations of four unitary sequences.

## 2. Complete metrics for the relevant groups

Here and throughout Sections 2–4, \(M\) has separable predual. Its unit is nonzero. Choose a faithful normal state \(\varphi\): a norm-dense countable family of positive normal functionals separates positive elements, and a summable positive combination, normalized at \(1\), is faithful.

Let \(\operatorname{Isom}(X)\) denote the surjective linear isometries of a separable Banach space \(X\). If \((\xi_j)\) is dense in its unit ball, the metric
\[
d(S,T)=\sum_{j\ge1}2^{-j}
\bigl(\|S\xi_j-T\xi_j\|+\|S^{-1}\xi_j-T^{-1}\xi_j\|\bigr)
\tag{9}
\]
is complete and induces pointwise norm convergence. For completeness, a Cauchy sequence and its inverses have pointwise isometric limits \(S,R\). The identity
\[
\|S_nR\xi-\xi\|=\|R\xi-S_n^{-1}\xi\|\to0
\]
gives \(SR=1\), and similarly \(RS=1\). The coordinate embedding in \((X\times X)^\mathbb N\) makes the topology separable. Multiplication is continuous by the isometry estimate, and
\[
\|T_n^{-1}\xi-T^{-1}\xi\|
=\|T\xi'-T_n\xi'\|,\qquad \xi'=T^{-1}\xi,
\]
proves continuity of inversion.

Give \(\operatorname{Aut}(M)\) the **\(u\)-topology**:
\[
\alpha_n\to\alpha
\quad\Longleftrightarrow\quad
\|\omega\circ\alpha_n-\omega\circ\alpha\|\to0
\quad(\omega\in M_*).
\tag{10}
\]
The map \(T_\alpha\omega=\omega\circ\alpha^{-1}\) is an injective homomorphism into \(\operatorname{Isom}(M_*)\).

**Lemma 2.1.** This image is closed. Consequently \(\operatorname{Aut}(M)\) is a Polish group, with a complete metric obtained from (9).

**Proof.** Suppose \(T_{\alpha_n}\to T\) in \(\operatorname{Isom}(M_*)\). The adjoints \(\beta=(T^{-1})^*\) and \(\gamma=T^*\) are inverse normal linear maps on \(M\), and \(\alpha_n(x)\to\beta(x)\), \(\alpha_n^{-1}(x)\to\gamma(x)\) ultraweakly. Matrix-level positivity passes to these limits, so both maps are unital completely positive. Schwarz gives
\[
\beta(x^*x)\ge\beta(x)^*\beta(x).
\]
Apply \(\gamma\) and then its own Schwarz inequality:
\[
x^*x\ge\gamma(\beta(x)^*\beta(x))\ge x^*x.
\]
Both inequalities are equalities. Injectivity of \(\gamma\) gives equality in Schwarz for \(\beta\). Polarization yields \(\beta(x^*y)=\beta(x)^*\beta(y)\), and positivity preserves adjoints, so \(\beta\) is multiplicative. It is a normal automorphism with inverse \(\gamma\), and \(T=T_\beta\). The topology agrees with (10) by continuity of inversion in the isometry group. \(\square\)

On \(\mathcal U(M)\) put
\[
D(u,v)=\|u-v\|_\varphi+\|u^*-v^*\|_\varphi.
\tag{11}
\]
In the faithful state GNS representation, \(\Omega\) is separating, so \(M'\Omega\) is dense. A bounded family tending to zero on \(\Omega\) therefore tends strongly to zero on every vector, by commuting with \(M'\). Applied to the family and its adjoint, this shows that (11) gives strong* convergence on the unitary group. Strong convergence to a unitary also implies convergence of adjoints, since
\[
(u_n^*-u^*)\xi=u_n^*(u-u_n)u^*\xi.
\tag{12}
\]

The GNS Hilbert space is separable. One way to see this is to take a countable ultraweakly dense subset of the unit ball of \(M\), which is compact metrizable because the predual is separable. Its vectors \(x\Omega\) are weakly dense in the corresponding convex image; rational convex combinations are norm dense by Hahn–Banach. These vectors span a dense subspace of the cyclic GNS space. The strong* topology on bounded operators on that space embeds into a countable product of separable Hilbert spaces. Thus the unitary group is separable.

**Lemma 2.2.** Metric (11) is complete, and
\[
\mathcal U(M)/\mathcal U(Z(M))
\tag{13}
\]
is a Polish group with the complete quotient metric
\[
\rho(u\,\mathcal U(Z),v\,\mathcal U(Z))
=\inf_{z\in\mathcal U(Z)}D(u,vz).
\tag{14}
\]

**Proof.** A \(D\)-Cauchy sequence gives Cauchy vectors \(u_n\Omega,u_n^*\Omega\). Commutation with \(M'\) and uniform boundedness give strong limits \(u,w\in M\) on all vectors. The pairing identity gives \(w=u^*\); strong convergence of products gives \(u^*u=uu^*=1\). This proves completeness.

Central unitary multiplication preserves \(D\): it cancels in \(x^*x\), and centrality cancels it in \(xx^*\). Thus (14) is independent of representatives, symmetric and satisfies the triangle inequality by aligning representatives with two successive central unitaries. If its value is zero, \(vz_n\to u\) strong*, hence \(z_n\to v^*u\) strong*, and the closed central unitary group contains this limit. Therefore the two cosets agree.

An open \(\rho\)-ball is the image of an open \(D\)-ball, so (14) induces the quotient topology. From a \(\rho\)-Cauchy sequence choose a subsequence with successive distances less than \(2^{-n}\); choose its representatives successively so that their \(D\)-distances are also summable. Their \(D\)-limit gives the quotient limit. The full Cauchy sequence then converges. Separability passes to the quotient, and group operations are continuous because the subgroup is closed and normal. \(\square\)

The same representative argument proves the general coset lemma: if a complete compatible metric on a group is invariant under right multiplication by a closed subgroup, its infimum metric makes the left coset space complete and induces the quotient topology. Triangle inequalities come from the right-invariance and aligned representatives; arbitrary distances between closed sets need not satisfy that inequality.

For \(u\in\mathcal U(M)\),
\[
\|\omega\circ\operatorname{Ad}u-\omega\|=\|[u,\omega]\|.
\tag{15}
\]
To verify this, multiply the functional \(u^*\omega u-\omega\) by \(u\) on the left; this is an isometry of the predual and gives \(\omega u-u\omega\). Estimates (5) and its adjoint version show that \(u\mapsto\operatorname{Ad}u\) is continuous for the strong* and \(u\)-topologies. Its kernel is \(\mathcal U(Z)\).

## 3. The needed open mapping theorem

**Lemma 3.1.** If \(A\) is nonmeager and has the Baire property in a Polish group \(K\), then \(AA^{-1}\) contains a neighborhood of \(1\).

**Proof.** There is a nonempty open \(O\) such that \(O\setminus A\) is meager. Choose \(a_0\in O\). For \(k\in Oa_0^{-1}\), the set \(O\cap kO\) is nonempty and open, hence is not meager. Outside a meager subset it belongs to both \(A\) and \(kA\). Choose \(a=kb\) in this intersection, with \(a,b\in A\); then \(k=ab^{-1}\). \(\square\)

**Theorem 3.2.** A continuous bijective homomorphism between Polish groups is a homeomorphism.

**Proof.** Let \(f:G\to K\) be such a map. For a neighborhood \(V\) of \(1\), choose open \(W\) with \(WW^{-1}\subset V\). Countably many left translates of \(W\) cover \(G\), by separability. Their images cover \(K\), so the Baire theorem says \(f(W)\) is nonmeager. The Lusin–Souslin prerequisite says \(f(W)\) is Borel; Borel sets have the Baire property because the sets agreeing with open sets modulo meager sets form a sigma-algebra containing the open sets. Lemma 3.1 gives
\[
f(V)\supset f(W)f(W)^{-1}
\]
containing a neighborhood of \(1\). Translation proves that \(f\) is open everywhere. A bijective open continuous map has continuous inverse. \(\square\)

## 4. Fullness, with the center retained

Call \(M\) **full** when \(\operatorname{Int}(M)\), the inner automorphisms, is closed in \(\operatorname{Aut}(M)\) for (10).

**Theorem 4.1.** For every von Neumann algebra with separable predual, the following are equivalent:

1. \(M\) is full.
2. Every bounded centralizing sequence is trivial.
3. Whenever \(\operatorname{Ad}u_n\to\mathrm{id}\), there are central unitaries \(z_n\) with \(D(u_n,z_n)\to0\).

**Proof.** The zero algebra satisfies all three assertions trivially; suppose \(M\ne0\), as in Sections 2–3. If the inner subgroup is closed, it is Polish by Lemma 2.1. The induced map from (13) onto it is a continuous bijective homomorphism, hence a homeomorphism by Theorem 3.2. Convergence to the identity in the quotient is precisely that the infimum in (14) tends to zero. Choosing approximate minimizers proves 3.

By (15), the unitary sequences in 3 are exactly the centralizing unitary sequences. Formula (8), applied to the real and imaginary parts of a general bounded centralizing sequence, expresses it using four such sequences with fixed bounded coefficients. Replacing each by its central unitary approximant gives a bounded central approximant. This proves 3 implies 2.

Suppose 2 holds and \(u_n\) is a centralizing unitary sequence. Choose bounded \(a_n\in Z(M)\) with \(u_n-a_n\to0\) strong*. Let \(z_n\) be the phase of \(a_n\), with phase \(1\) on its zero spectral projection. The abelian von Neumann algebra generated by the normal operator \(u_n\) and \(a_n\) permits the scalar inequality
\[
|\operatorname{phase}(a)-w|\le2|a-w|
\qquad(|w|=1)
\tag{16}
\]
to be applied by joint functional calculus. Both squares of \(u_n-z_n\) are at most four times the corresponding squares of \(u_n-a_n\). Thus \(D(u_n,z_n)\to0\). This proves 2 implies 3.

It remains to show 3 implies closedness. Since both group topologies are metrizable, 3 says that the inverse of the induced bijection (13) onto \(\operatorname{Int}(M)\) is continuous at the identity, hence everywhere. In particular, for any faithful normal positive functional \(\psi\) and any \(\varepsilon>0\), there is a \(u\)-neighborhood \(\mathcal W\) of the identity such that
\[
\operatorname{Ad}v\in\mathcal W
\ \Longrightarrow\
\inf_{z\in\mathcal U(Z)}
\bigl(\|v-z\|_\psi+\|v^*-z^*\|_\psi\bigr)<\varepsilon.
\tag{17}
\]
Otherwise a decreasing countable neighborhood base would give a sequence contradicting 3. A faithful \(\psi\) gives the same bounded strong* topology as \(\varphi\).

Let \(\theta\) lie in the closure of \(\operatorname{Int}(M)\), and put \(\psi=\varphi+\varphi\circ\theta\). Choose implementing unitaries \(v_n\), after passing to a subsequence, so that \(\operatorname{Ad}v_n\to\theta\), their successive differences belong to the neighborhoods from (17) with \(\varepsilon=2^{-n}\), and
\[
\|\varphi\circ\operatorname{Ad}v_{n+1}-\varphi\circ\theta\|<4^{-n}.
\tag{18}
\]
This simultaneous choice is possible because the automorphisms converge and group operations are continuous. More explicitly, for each chosen neighborhood both indices of \((\operatorname{Ad}v_m)^{-1}\operatorname{Ad}v_l\) can be made sufficiently large.

Choose \(c_n\in\mathcal U(Z)\) with
\[
y_n=c_n-v_{n+1}^*v_n,\qquad
\|y_n\|_\psi+\|y_n^*\|_\psi<2^{-n}.
\]
Set \(\gamma_1=1\), \(\gamma_{n+1}=c_n\gamma_n\) and \(u_n=v_n\gamma_n\). Then
\[
u_{n+1}-u_n=v_{n+1}y_n\gamma_n.
\]
Centrality of \(\gamma_n\) gives
\[
\|u_{n+1}-u_n\|_\varphi^2
=\varphi(y_n^*y_n)<4^{-n}.
\tag{19}
\]
For the adjoint seminorm, (18) and \(\|y_n\|\le2\) give
\[
\|(u_{n+1}-u_n)^*\|_\varphi^2
=(\varphi\circ\operatorname{Ad}v_{n+1})(y_ny_n^*)
<5\cdot4^{-n}.
\tag{20}
\]
The \(D\)-increments are summable, so Lemma 2.2 gives a unitary limit \(u\). Continuity of \(\operatorname{Ad}\) gives \(\operatorname{Ad}u=\theta\), because \(\operatorname{Ad}u_n=\operatorname{Ad}v_n\). Thus the inner subgroup is closed. \(\square\)

For a factor, “trivial” means asymptotically scalar. For a finite factor Corollary 1.2 allows “central” in Theorem 4.1 as well. An abelian algebra is full: its inner automorphism group is \(\{\mathrm{id}\}\), and every sequence already lies in its center. The center is therefore essential in the general formulation.

## 5. An explicit free group gap

Let \(\Gamma=\mathbb F_n\), \(2\le n\le\infty\), with distinguished generators \(a,b\). Let \(\lambda\) be its left regular representation on \(\ell^2(\Gamma)\), and set \(L(\Gamma)=\lambda(\Gamma)''\).

The vector state \(\tau(x)=\langle\delta_e,x\delta_e\rangle\) is a faithful normal trace. For completeness, \(\delta_e\) is separating because the commuting right regular representation has a cyclic orbit through it. To check the trace on arbitrary \(x,y\), first note that
\(\tau(x\lambda_g)=\tau(\lambda_gx)\): the vector \(\lambda_g\delta_e=\delta_g\) is also a right-translate of \(\delta_e\), so commutation with the right representation gives the same coefficient. Extend linearly to group polynomials and then ultraweakly in the second variable; each expression is a normal functional. This proves traciality without interchanging infinite Fourier series.

The coefficients
\[
\widehat x(g)=\langle\delta_g,x\delta_e\rangle
\]
belong to \(\ell^2(\Gamma)\), and
\[
\|x-\tau(x)1\|_2^2=\sum_{g\ne e}|\widehat x(g)|^2.
\tag{21}
\]
Every nonidentity conjugacy class is infinite. Indeed, if a reduced word \(g\) is not a power of \(a\), write \(g=a^rwa^s\) with \(w\) beginning and ending in letters other than \(a^{\pm1}\). The distinct words \(a^kg a^{-k}=a^{k+r}wa^{s-k}\) are distinguished by their initial and terminal \(a\)-runs, including runs of length zero. If \(g\) is a nontrivial power of \(a\), conjugate instead by powers of \(b\). A central operator has coefficients constant on conjugacy classes, so square summability makes all its nonidentity coefficients zero. Since \(\delta_e\) is separating, the operator is scalar. Thus \(L(\Gamma)\) is a factor. It is infinite-dimensional, has a finite faithful trace, and therefore is of type \(\mathrm{II}_1\).

**Theorem 5.1.** For every \(x\in L(\Gamma)\),
\[
\|x-\tau(x)1\|_2
\le14\max\{\|[x,\lambda_a]\|_2,\|[x,\lambda_b]\|_2\}.
\tag{22}
\]

**Proof.** Let \(S\) be the nonidentity reduced words whose last letter is \(a\) or \(a^{-1}\). Then
\[
S\cup aSa^{-1}=\Gamma\setminus\{e\},
\tag{23}
\]
since a word not ending in an \(a\)-letter, conjugated by \(a^{-1}\), ends in \(a\). Also
\[
S,\quad bSb^{-1},\quad b^{-1}Sb
\tag{24}
\]
are pairwise disjoint. Words in the latter two sets end in \(b^{-1}\) and \(b\), respectively: the terminal \(a\)-letter prevents cancellation with the appended \(b\)-letter. Left cancellation cannot remove this terminal part. More generally the sets \(b^jSb^{-j}\), \(j\in\mathbb Z\), are pairwise disjoint because their terminal \(b\)-run is \(-j\), with \(j=0\) corresponding to \(S\).

Put \(\xi=(\widehat x(g))_{g\ne e}\), \(k=\|\xi\|_2^2\), and let \(\delta\) be the maximum on the right of (22) before multiplication by \(14\). Conjugation of coefficients by \(a\) or \(b\) moves \(\xi\) by distance at most \(\delta\); the same holds for their inverses. For \(\mu(A)=\sum_{g\in A}|\widehat x(g)|^2\), restriction and the reverse triangle inequality give
\[
|\sqrt{\mu(hAh^{-1})}-\sqrt{\mu(A)}|\le\delta
\quad(h=a,b,b^{-1}).
\]
Both square roots are at most \(\sqrt k\), so
\[
|\mu(hAh^{-1})-\mu(A)|\le2\sqrt k\,\delta.
\tag{25}
\]
The cover (23) gives
\[
k\le2\mu(S)+2\sqrt k\,\delta,
\qquad \mu(S)\ge k/2-\sqrt k\,\delta.
\tag{26}
\]
Each of the two other sets in (24) has measure at least \(k/2-3\sqrt k\,\delta\), by (25). Disjointness therefore gives
\[
k\ge\mu(S)+\mu(bSb^{-1})+\mu(b^{-1}Sb)
\ge3k/2-7\sqrt k\,\delta.
\tag{27}
\]
If \(k>0\), division by \(\sqrt k/2\) yields \(\sqrt k\le14\delta\). If \(k=0\), the assertion is immediate. \(\square\)

**Corollary 5.2.** Every \(L(\mathbb F_n)\), \(2\le n\le\infty\), is full and is not isomorphic to \(R\).

**Proof.** A bounded central sequence has both commutators in (22) tending to zero in \(2\)-norm. Thus \(x_m-\tau(x_m)1\to0\) in \(2\)-norm, hence strong* on bounded sets by the finite-trace topology argument in the preceding lesson. The scalar approximants are bounded. Corollary 1.2 and Theorem 4.1 prove fullness; the group is countable, so the predual is separable.

In \(R\), let \(z_m\) be the trace-zero diagonal unitary \(Z\) in tensor leg \(m\). The tail argument in the [outer-action lesson](finite-outer-actions.md#3-an-explicit-outer-finite-action) makes it central, but
\[
\inf_{c\in\mathbb C}\|z_m-c1\|_2^2
=\inf_c(1+|c|^2)=1.
\tag{28}
\]
It is nontrivial, so \(R\) is not full. Normal isomorphisms preserve predual commutators, bounded strong* convergence, centers and fullness. The two factors cannot be isomorphic. \(\square\)

This distinguishes these group factors from the AFD finite factor. It makes no assertion about isomorphisms between free group factors with different numbers of generators.

## 6. A group algebra that is hyperfinite

Let \(S_{\mathrm{fin}}\) be the permutations of \(\mathbb N\) that fix all but finitely many points. The finite symmetric group \(S_m\), acting on \(\{1,\ldots,m\}\), embeds by fixing the remaining points, and
\[
S_{\mathrm{fin}}=\bigcup_m S_m.
\tag{29}
\]

**Proposition 6.1.** The algebra \(L(S_{\mathrm{fin}})\) is an AFD factor of type \(\mathrm{II}_1\), hence is isomorphic to \(R\).

**Proof.** Every nonidentity permutation \(g\) has infinite conjugacy class. Choose a moved point \(i\) and, for each \(j\) outside its finite support, conjugate by the transposition \((i\ j)\). The resulting support is
\[
(\operatorname{supp}g\setminus\{i\})\cup\{j\}.
\]
These supports are distinct as \(j\) varies, so the conjugates are distinct. The trace and coefficient argument at the start of Section 5 applies to any countable discrete group; the infinite-conjugacy-class argument therefore makes \(L(S_{\mathrm{fin}})\) a factor. It is finite with faithful trace and infinite-dimensional, hence has type \(\mathrm{II}_1\).

The linear spans of \(\{\lambda_g:g\in S_m\}\) are increasing unital finite-dimensional star algebras. Each is already ultraweakly closed, and their union contains every group unitary by (29). They generate \(L(S_{\mathrm{fin}})\), proving AFD. The group is countable, giving separable predual, so finite AFD uniqueness applies. \(\square\)

These finite approximants are generally direct sums of matrix algebras. Their finite-dimensional centers do not force a center in the limit. Conversely the free group gap shows that finite approximants of this kind cannot exist for \(L(\mathbb F_n)\).

## 7. Exercises with complete solutions

**Exercise 1.** Verify (7) with the convention (1), and explain why checking only one faithful state is insufficient without centrality.

*Solution.* At a test variable \(t\), \(xy,\omega=\omega(txy)-\omega(ytx)\), and \([x,\omega]y(t)=\omega(ytx)-\omega(xyt)\). Their sum is \(\omega(txy)-\omega(xyt)=xy,\omega\). In \(M_2\), the normalized trace commutes with every \(x\), while the constant sequence of a nonscalar matrix fails to commute with some fixed matrix. Its commutator with the trace alone vanishes; it is not centralizing.

**Exercise 2.** Prove the norm density of \(M\varphi\) when \(\varphi\) is faithful, and identify the precise obstruction when it is not.

*Solution.* A functional annihilator \(y\in M\) satisfies \(\varphi(ya)=0\) for every \(a\). Taking \(a=y^*\) gives \(\varphi(yy^*)=0\), so faithfulness gives \(y=0\) and Hahn–Banach gives density. If \(p=s(\varphi)\ne1\), \(y=1-p\) is nonzero and \(\varphi(ya)=0\) for all \(a\), by the support and Cauchy–Schwarz. Thus the annihilator is nonzero and density fails.

**Exercise 3.** Give a strong Cauchy sequence of unitaries with a nonunitary strong limit, and explain why (11) detects the problem.

*Solution.* On \(\ell^2(\mathbb N_0)\), let \(u_n\) cyclically permute \(e_0,\ldots,e_n\) by \(e_j\mapsto e_{j+1}\) for \(j<n\), \(e_n\mapsto e_0\), and fix the rest. On each fixed basis vector, \(u_n\) eventually agrees with the unilateral shift \(S\). Hence \(u_n\to S\) strongly, and \(S\) is not unitary. But \(u_n^*e_0=e_n\) is not Cauchy. The adjoint seminorm in (11), for a faithful diagonal normal state on \(B(\ell^2)\), includes a positive multiple of this vector distance, so the sequence is not \(D\)-Cauchy.

**Exercise 4.** Why does the quotient metric require central unitaries, and what does completeness alone say about the two-sided group uniformity?

*Solution.* For \(z\) central, \((xz)(xz)^*=xx^*\) as well as \((xz)^*(xz)=x^*x\), giving simultaneous invariance of both seminorms. A general unitary preserves the first expression under the appropriate side of translation, but conjugates the second, and a general faithful state need not be invariant under that conjugation. Completeness of a compatible metric by itself identifies no left or right invariant uniformity. The closedness proof in Theorem 4.1 instead constructs representatives with summable \(D\)-increments, as (19)–(20) explicitly show.

**Exercise 5.** Prove (16), including \(a=0\), and deduce a bounded central unitary approximant from any central approximant to a unitary.

*Solution.* For \(a\ne0\), write \(a=r\zeta\), \(r>0\), \(|\zeta|=1\). The reverse triangle inequality gives \(|r-1|\le|a-w|\). Therefore \(|\zeta-w|\le|\zeta-a|+|a-w|\le2|a-w|\). For \(a=0\), choosing phase \(1\) gives \(|1-w|\le2=2|a-w|\). A unitary commutes with every central approximant, so the abelian joint spectral calculus gives the corresponding squared operator inequalities. Applying a positive normal functional to either square proves bounded strong* approximation by central phases.

**Exercise 6.** Show that every abelian von Neumann algebra with separable predual is full, and that the centralizing criterion is not a criterion for asymptotic scalarness in that setting.

*Solution.* Inner conjugation is the identity in an abelian algebra, so the inner automorphism subgroup is the closed singleton. Every bounded sequence belongs to the center and is trivial with \(z_n=x_n\). If the algebra is \(\mathbb C^2\), a constant nonscalar element illustrates that triviality need not imply approach to scalar multiples of the unit.

**Exercise 7.** In the cover (23), do the sets have to be disjoint? Explain the direction of the measure inequality actually used.

*Solution.* They may overlap. For example \(a\) belongs to both \(S\) and \(aSa^{-1}\). Subadditivity gives \(k=\mu(S\cup aSa^{-1})\le\mu(S)+\mu(aSa^{-1})\), which is the direction required for (26). The three sets in (24), used for the lower bound on \(k\), are disjoint and give an actual sum of their measures inside the total.

**Exercise 8.** An element \(x\) satisfies \(\|[x,\lambda_a]\|_2\le10^{-3}\) and \(\|[x,\lambda_b]\|_2\le2\cdot10^{-3}\). Give the scalar approximation certified by (22), and explain why its scalar is optimal.

*Solution.* The estimate gives \(\|x-\tau(x)1\|_2\le0.028\). Orthogonal projection onto the one-dimensional subspace \(\mathbb C1\) of \(L^2\) is \(x\mapsto\tau(x)1\); equivalently \(\|x-c1\|_2^2=\|x-\tau(x)1\|_2^2+|c-\tau(x)|^2\). Hence this scalar minimizes the distance.

**Exercise 9.** Why does the tail-unitary argument in \(R\) prove nontriviality even if the allowed scalar approximants vary with the index?

*Solution.* For every \(m\) and every scalar \(c_m\), trace zero and squared norm \(1\) give \(\|z_m-c_m1\|_2^2=1+|c_m|^2\ge1\). No choice of a scalar sequence makes the distance tend to zero. For bounded approximants the finite-trace equivalence of \(2\)-norm and strong* makes this exactly the required obstruction.

**Exercise 10.** Prove the criterion is invariant under normal isomorphisms, keeping the center and both strong* seminorms.

*Solution.* Let \(\theta:M\to N\) be a normal isomorphism. For \(\omega\in N_*\), evaluating at \(\theta(y)\) shows \([\theta(x),\omega]\circ\theta=[x,\omega\circ\theta]\). Pullback is isometric and onto on preduals, so centralizing is preserved in both directions. For \(\psi\in N_*^+\), \(\|\theta(x)\|_\psi=\|x\|_{\psi\circ\theta}\), with the same identity for adjoints. Thus bounded strong* equivalence is preserved. Finally \(\theta(Z(M))=Z(N)\), so bounded central approximants transport exactly. Theorem 4.1 now transports fullness.

**Exercise 11.** In \(L(S_{\mathrm{fin}})\), why is the finite-dimensional algebra from \(S_2\) not a factor, and why does its nonscalar central element cease to be central in the whole algebra?

*Solution.* If \(t=(1\ 2)\), then \(\lambda_t^2=1\) and the span of \(1,\lambda_t\) is \(\mathbb C^2\), with minimal projections \((1\pm\lambda_t)/2\). It is abelian, hence not a factor. But \(s=(2\ 3)\) does not commute with \(t\), and \(\lambda_s\lambda_t\delta_e=\delta_{st}\ne\delta_{ts}=\lambda_t\lambda_s\delta_e\). Thus \(\lambda_t\) fails to commute with a later group unitary. Centers of successive approximants are not an increasing family of central elements of the generated algebra.

## References

Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*](https://idpoisson.fr/anantharaman/publications/IIun.pdf), author draft, Theorem 15.3.2, printed pp.266–267 (PDF pp.272–273), proves the fullness criterion in the separable finite-factor setting. The complete group metrics and the proof in Section 4 here retain general von Neumann algebras with separable predual and their centers; that greater scope is established locally. Section 15.4, printed pp.267–268 (PDF pp.273–274), supplies the free-word cover and disjoint conjugates. Section 5 gives every coefficient estimate and proves the particular constant 14 directly, without invoking an unproved equivalence with property Gamma.

Christian Rosendal, [*Automatic continuity of group homomorphisms*](https://homepages.math.uic.edu/~rosendal/PapersWebsite/AutomaticContinuity06.pdf), author version dated November 2008, Section 2.1, Lemma 2.1 and Theorem 2.2, p.4, gives the full category argument. Sections 2–3 here prove the complete metrics, closed automorphism image, central-unitary quotient and Pettis step explicitly. The Lusin–Souslin Borel-image theorem is a separate prerequisite: the Anantharaman–Popa draft's Appendix B.3–B.4, printed p.315 (PDF p.321), states these descriptive-set-theory results by reference and does not prove them. Their exact freely accessible proof chain remains pending.

The Anantharaman–Popa draft's Section 1.3.2, printed p.10 (PDF p.16), gives the increasing finite group algebras for the finitely supported permutation group. Its Exercise 1.7, printed p.25 (PDF p.31), poses the conjugacy calculation. Proposition 6.1 supplies that calculation completely and retains direct sums in the finite approximants; its final identification with R uses the separately recorded finite AFD uniqueness proof. The normal-functional, bounded strong* topology and center-valued-trace foundations remain explicit dependencies. No source expression is imported.
