# Stabilization of non-additive functors

*Written by Claude Opus 5.5 (Anthropic) on 20 October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(F\) be a functor between abelian categories with \(F(0)=0\), and let \(X\) be a simplicial object. The homology of \(F\) applied to the \(n\)-fold suspension \(X[n]\) changes with \(n\), but it stabilizes. The suspension maps \(H_{i+n}F(X[n])\to H_{i+n+1}F(X[n+1])\) are isomorphisms as soon as \(n>i\). This is the suspension theorem of Dold and Puppe. Its proof decomposes the bar construction of \(X\) by cross-effects. The cross-effects of order two and higher are highly connected, so only the additive part of \(F\) is seen in low degrees.

Illusie's *stabilization* \(F^{\mathrm{st}}\) realizes the stable values as the homology of a single simplicial object. One applies \(F\) to the spectrum of \(X\), kills the faces of degree zero, translates down and takes the derived colimit over the category of finite ordinals. This lesson proves the suspension theorem, constructs \(F^{\mathrm{st}}\), and shows that \(H_iF^{\mathrm{st}}(X)\cong H_{i+n}F(X[n])\) for \(n>i\). It then proves that \(F^{\mathrm{st}}\) is additive and turns degreewise split exact sequences into distinguished triangles, through a canonical isomorphism \(F^{\mathrm{st}}(X[1])\cong F^{\mathrm{st}}(X)[1]\), which anticommutes with the connecting morphisms of exact sequences of functors. The stable derived functors built from \(F^{\mathrm{st}}\) are the subject of [*Stable derived functors*](stable-derived-functors.md).

**Prerequisites.** [*Multisimplicial objects and spectral diagrams*](multisimplicial-objects-and-spectral-diagrams.md); Section 1 and Proposition 2.3 of [*Non-additive functors of complexes in a ringed topos*](non-additive-functors-of-complexes-in-a-ringed-topos.md) (cross-effects, homotopy invariance); Lemmas 1.1 and 3.1 and Theorems 2.3 and 3.3 of [*Derived colimits over a small category*](derived-colimits-over-a-small-category.md); Theorems 1.1–1.3 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex#1-simplicial-algebra-and-the-standard-resolution). From the AI-integrated Stacks project: cones and the triangle of a termwise split sequence [[Stacks, Tag 014I](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-definition-split-ses), [Tag 014O](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-rotate-cone)]; cones [[Tag 014E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-definition-cone)] and the snake lemma [[Tag 010H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-snake)]; the triangle of a short exact sequence in the derived category, functorial in the sequence [[Tag 0152](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-derived-canonical-delta-functor), [Tag 0154](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-derived-compare-triangles-split-case)].

## Conventions

\(\mathcal A\) and \(\mathcal B\) are abelian categories, and \(\mathcal B\) has small colimits and exact filtered colimits. A functor \(F\colon\mathcal A\to\mathcal B\) is arbitrary. It is the direct sum of the constant functor \(F(0)\) and the reduced functor \(F^+(M)=\ker(F(M)\to F(0))\), the kernel of \(F\) applied to \(M\to0\). Functors are applied termwise to simplicial and multisimplicial objects. The homology \(H_*\) of a simplicial object is that of its normalized complex \(N\), which equals that of its unnormalized complex (Theorem 1.1 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex)). Notation for multisimplicial objects, faces, reduction, translations and spectral diagrams is that of the lesson on multisimplicial objects; \(\bar\Delta'\) is the category of finite ordinals and injective increasing maps.

For \(X\in\operatorname{Simpl}(\mathcal A)\) and \(n\geq0\) put \(X[n]=\Gamma\bigl((NX)[n]\bigr)\). Then \(X[n]_q=0\) for \(q<n\), because \(\Gamma(C)_q=\bigoplus_{[q]\twoheadrightarrow[k]}C_k\). We say that a simplicial object \(Z\) is *\(n\)-reduced* if \(Z_q=0\) for \(q<n\).

## 1. Cross-effects and connectivity

Recall from Section 1 of the lesson on non-additive functors that for \(M=M_1\oplus\cdots\oplus M_r\) and a reduced \(F\),
\[
\begin{aligned}&F(M)\\&\quad =\bigoplus_{\varnothing\neq S\subseteq\{1,\ldots,r\}}\operatorname{cr}_SF(M_1,\ldots,M_r),\end{aligned}
\]
the images of orthogonal idempotents \(\varepsilon_S\) built from the projections \(e_R\) onto the partial sums. The cross-effect \(\operatorname{cr}_SF\) vanishes when \(M_s=0\) for some \(s\in S\), and it is natural for maps of the form \(\bigoplus_i\varphi_i\). We write \(\operatorname{cr}_rF(M_1,\ldots,M_r)=\) \(\operatorname{cr}_{\{1,\ldots,r\}}F(M_1,\ldots,M_r)\), a functor of \(r\) variables that vanishes when one variable is \(0\).

For a map of finite sets \(\varphi\colon\{1,\ldots,p\}\to\{1,\ldots,p'\}\sqcup\{\ast\}\) and an object \(M\), let \(f_\varphi\colon M^{\oplus p}\to M^{\oplus p'}\) be the *sum map* with \((f_\varphi x)_k=\sum_{\varphi(l)=k}x_l\). The faces and degeneracies of the nerve of an abelian group object are sum maps: \(d_0\) and \(d_p\) send the first or last index to \(\ast\), the inner faces \(d_i\) identify the indices \(i\) and \(i+1\), and the degeneracies are injective.

**Lemma 1.1.** Let \(F\) be reduced and \(S\subseteq\{1,\ldots,p\}\). If \(S\) meets \(\varphi^{-1}(\ast)\), then \(F(f_\varphi)\) kills \(\operatorname{cr}_SF(M,\ldots,M)\). Otherwise it maps \(\operatorname{cr}_SF(M,\ldots,M)\) into \(\operatorname{cr}_{\varphi(S)}F(M,\ldots,M)\), isomorphically if \(\varphi\) is injective on \(S\).

**Proof.** Write \(e_R\) and \(e'_{R'}\) for the projections onto the partial sums of \(M^{\oplus p}\) and \(M^{\oplus p'}\). Then \(e'_{R'}f_\varphi=f_\varphi e_{\varphi^{-1}(R')}\). By Lemma 1.1 of the lesson on non-additive functors, \(F(e_R)y=y\) for \(y\in\operatorname{cr}_SF\) if \(S\subseteq R\), and \(F(e_R)y=0\) otherwise. For \(y\in\operatorname{cr}_SF\) and \(S'\subseteq\{1,\ldots,p'\}\),
\[
\begin{aligned}&\varepsilon'_{S'}F(f_\varphi)y\\&\quad =\sum_{R'\subseteq S'}(-1)^{|S'\smallsetminus R'|}F(f_\varphi)F(e_{\varphi^{-1}(R')})y.\end{aligned}
\]
The term of \(R'\) is \(F(f_\varphi)y\) if \(S\subseteq\varphi^{-1}(R')\), and \(0\) otherwise. If \(S\) meets \(\varphi^{-1}(\ast)\), every term vanishes. Otherwise the condition is \(\varphi(S)\subseteq R'\), and the alternating sum over \(\varphi(S)\subseteq R'\subseteq S'\) is \(F(f_\varphi)y\) if \(S'=\varphi(S)\) and \(0\) otherwise. This proves the first two assertions.

If \(\varphi\) is injective on \(S\) and \(S\cap\varphi^{-1}(\ast)=\varnothing\), choose \(\psi\colon\{1,\ldots,p'\}\to\{1,\ldots,p\}\sqcup\{\ast\}\) with \(\psi(\varphi(s))=s\) for \(s\in S\) and \(\psi=\ast\) outside \(\varphi(S\)). Let \(\iota_S\) be the inclusion of the partial sum indexed by \(S\). Then \(\operatorname{cr}_SF\) lies in the image of \(F(\iota_S)\), because \(\varepsilon_S=\varepsilon_SF(e_S)\) and \(e_S\) factors through \(\iota_S\). Since \(f_{\psi\varphi}\iota_S=\iota_S\), the map \(F(f_\psi)F(f_\varphi)=F(f_{\psi\varphi})\) is the identity on \(\operatorname{cr}_SF\). In the same way \(F(f_\varphi)F(f_\psi)\) is the identity on \(\operatorname{cr}_{\varphi(S)}F\). \(\square\)

**Lemma 1.2 (connectivity).** Let \(T\colon\mathcal A^r\to\mathcal B\) be a functor of \(r\) variables that vanishes when one variable is \(0\). Let \(Z^1,\ldots,Z^r\) be simplicial objects of \(\mathcal A\), with \(Z^k\) \(n_k\)-reduced. Then the simplicial object \(q\mapsto T(Z^1_q,\ldots,Z^r_q)\) has \(H_q=0\) for \(q<n_1+\cdots+n_r\).

**Proof.** It is the diagonal of the \(r\)-simplicial object \(W(q_1,\ldots,q_r)=T(Z^1_{q_1},\ldots,Z^r_{q_r})\), which vanishes unless \(q_k\geq n_k\) for every \(k\). Its normalization is a subobject in each multidegree, so \(\operatorname{Tot}NW\) vanishes in degrees \(<\sum n_k\). By Lemma 2.6 of the lesson on multisimplicial objects, \(N\operatorname{diag}W\) is homotopy equivalent to \(\operatorname{Tot}NW\). \(\square\)

**Lemma 1.3 (homotopy invariance).** Let \(T\colon\mathcal A\to\mathcal B\) be reduced and \(f\colon Z\to Z'\) a map of simplicial objects whose normalization \(Nf\) is a chain homotopy equivalence. Then \(NT(f)\) is a chain homotopy equivalence.

**Proof.** By Lemma 1.1 of the lesson on multisimplicial objects, \(f\) is identified with \(\Gamma(Nf)\). For complexes \(C\) concentrated in nonpositive cohomological degrees, that is, chain complexes in degrees \(\geq0\), the extension of \(T\) to complexes in the lesson on non-additive functors is \(NT\Gamma C\). By Proposition 2.3 there, homotopic maps of complexes are carried to homotopic maps. So a homotopy inverse of \(Nf\) and the two homotopies are carried to a homotopy inverse of \(NT\Gamma(Nf)\) and homotopies. \(\square\)

## 2. The suspension theorem

For \(Z\in\operatorname{Simpl}(\mathcal A)\), the *bar construction* \(\mathcal BZ\) is the bisimplicial object with \(\mathcal BZ(p,q)=Z_q^{\oplus p}\), the nerve of the abelian group object \(Z_q\) in the first coordinate. By Lemma 3.4 of the lesson on multisimplicial objects, its normalization in the first coordinate is \(Z\) in degree \(p=1\). So \(N\operatorname{diag}\mathcal BZ\) is homotopy equivalent to \(NZ\) shifted up by one degree, and \(\operatorname{diag}\mathcal BZ\) is a model of the suspension of \(Z\).

Let \(T\) be reduced. In the bisimplicial object \(T(\mathcal BZ)\), \((p,q)\mapsto T(Z_q^{\oplus p})\), the first column is \(T(\mathcal BZ)(0,-)=T(0)=0\). The normalization of the second column is \(T(Z)\), since \(N_1=\ker(d_1\colon V_1\to V_0)=V_1\) when \(V_0=0\). In \(\operatorname{Tot}NT(\mathcal BZ)\), the differential leaving the column \(p=1\) stays in it, where it is \(-\partial\). So the column \(p=1\) is a subcomplex, isomorphic to \(NT(Z)\) shifted up by one degree. Its inclusion defines the *suspension*
\[
\sigma\colon H_m(TZ)\longrightarrow H_{m+1}\bigl(\operatorname{Tot}NT(\mathcal BZ)\bigr).
\]
By Lemma 2.6 of the lesson on multisimplicial objects, the target is \(H_{m+1}\) of \(T(\operatorname{diag}\mathcal BZ)=\operatorname{diag}T(\mathcal BZ)\). The map \(\sigma\) is natural in \(Z\) and \(T\).

**Theorem 2.1 (Dold–Puppe).** Let \(T\) be reduced, \(n\geq1\), and let \(Z\) be an \(n\)-reduced simplicial object. Then \(\sigma\colon H_m(TZ)\to H_{m+1}(\operatorname{Tot}NT(\mathcal BZ))\) is an isomorphism for \(m<2n\) and an epimorphism for \(m=2n\).

**Proof.** For each \((p,q)\) decompose by cross-effects:
\[
\begin{aligned}&T(Z_q^{\oplus p})\\&\quad =\bigoplus_{\varnothing\neq S\subseteq\{1,\ldots,p\}}\operatorname{cr}_ST(Z_q,\ldots,Z_q).\end{aligned}
\]
The faces and degeneracies of \(Z\) act diagonally, so they preserve each summand. The faces and degeneracies of the nerve are sum maps, so by Lemma 1.1 they carry the summand of \(S\) into the summand of a set with at most \(|S|\) elements, or to \(0\). Hence the summands with \(|S|=1\) form a bisimplicial subobject \(B_1\), and the summands with \(|S|\geq2\) form the quotient \(Q\).

*The subobject.* The summand \(\operatorname{cr}_{\{s\}}T\) is the image of \(T\) of the \(s\)-th inclusion \(Z_q\to Z_q^{\oplus p}\). The map \((TZ_q)^{\oplus p}\to T(Z_q^{\oplus p})\), \((y_s)\mapsto\sum_sT(\iota_s)y_s\), is therefore an isomorphism onto \(B_1(p,q)\). It commutes with the sum maps, because \(T(f_\varphi)T(\iota_s)=T(\iota_{\varphi(s)})\). So \(B_1\cong\mathcal B(TZ)\). Its normalization in the first coordinate is \(TZ\) in degree \(p=1\), and \(\operatorname{Tot}NB_1\) is the subcomplex defining \(\sigma\).

*The quotient.* Normalize \(Q\) in the first coordinate by the quotient by degenerate elements. The degeneracy \(s_i\) inserts a zero in position \(i+1\), and by Lemma 1.1 it maps the summand of \(S\) isomorphically onto the summand of its image. Every proper subset of \(\{1,\ldots,p\}\) misses some position and is such an image. So the degenerate part of \(Q(p,-)\) is the sum of the summands with \(S\neq\{1,\ldots,p\}\). The normalized column \(p\) is \(0\) for \(p\le1\), and for \(p\geq2\) it is the simplicial object \(\operatorname{cr}_pT(Z,\ldots,Z)\) with \(p\) arguments. By Lemma 1.2, its homology vanishes in degrees \(q<pn\). In the double complex \(NQ\), filtered by columns, the column \(p\) therefore contributes only in total degrees \(\geq p+pn\geq2n+2\). Each total degree involves finitely many columns, so \(H_k(\operatorname{Tot}NQ)=0\) for \(k\le2n+1\).

*Conclusion.* Normalization and totalization are exact, so \(0\to\) \(\operatorname{Tot}NB_1\to\) \(\operatorname{Tot}NT(\mathcal BZ)\to\) \(\operatorname{Tot}NQ\to\) \(0\) is exact. In its long exact sequence, \(H_{m+1}(\operatorname{Tot}NB_1)=\) \(H_m(TZ)\to\) \(H_{m+1}(\operatorname{Tot}NT(\mathcal BZ))\) is surjective if \(H_{m+1}(\operatorname{Tot}NQ)=0\). This holds for \(m\le2n\). It is injective if moreover \(H_{m+2}(\operatorname{Tot}NQ)=0\), which holds for \(m\le2n-1\). \(\square\)

**Corollary 2.2.** The conclusion of Theorem 2.1 holds whenever \(Z\) admits a map \(Z\to Z'\) to an \(n\)-reduced simplicial object whose normalization is a chain homotopy equivalence.

**Proof.** The map \(f\colon Z\to Z'\) induces \(T(f)\) and \(T(\mathcal Bf)\), compatible with \(\sigma\). By Lemma 1.3, \(T(f)\) induces isomorphisms in homology. The column \(p\) of \(T(\mathcal Bf)\) is the map \(T_p(f)\) for the reduced functor \(T_p(M)=T(M^{\oplus p})\), so it also induces isomorphisms in homology by Lemma 1.3. By the column filtration, \(\operatorname{Tot}NT(\mathcal Bf)\) is a quasi-isomorphism. \(\square\)

## 3. The stabilization

Let \(X\in\operatorname{Simpl}(\mathcal A)\). Regard \(X\) as an object of the abelian category \(\operatorname{Simpl}(\mathcal A)\). Its spectrum \(X(1)\) (Section 3 of the lesson on multisimplicial objects) has components \(X\langle n\rangle\in\operatorname{Simpl}_n(\operatorname{Simpl}(\mathcal A))\), which we regard as \((n+1)\)-simplicial objects of \(\mathcal A\): the \(n\) *spectral coordinates* and the last coordinate of \(X\). Concretely, \(X\langle n\rangle(p_0,\ldots,p_{n-1};q)=X_q^{\oplus p_0\cdots p_{n-1}}\). The structure maps identify \(X\langle n\rangle\) with the faces \(\partial^1_\delta X\langle m\rangle\) in the spectral coordinates.

Apply \(F\) termwise. Then \(F(X(1))\) is a spectral diagram of \(\operatorname{Simpl}(\mathcal B)\). Reduction and translation take place in the spectral coordinates, termwise in the last one.

**Lemma 3.1.** \(F(X\langle0\rangle)^{\mathrm{red}}=F(X)\), and \(F(X\langle n\rangle)^{\mathrm{red}}=F^+(X\langle n\rangle)\) for \(n\geq1\).

**Proof.** For \(n=0\) there are no spectral coordinates. For \(n\geq1\), \(X\langle n\rangle\) is reduced in the spectral coordinates, because a nerve has \(0\) in degree \(0\). So every face of degree \(0\) of \(F(X\langle n\rangle)\) is the constant object \(F(0)\). Its map \(\iota_i\) is \(F\) of a map from \(0\), the inclusion of the summand \(F(0)\), the same for every \(i\). Hence \(\partial^0F(X\langle n\rangle)=F(0)\), and the quotient is \(F^+(X\langle n\rangle)\). \(\square\)

**Definition 3.2.** Let \(E^{(n)}=F(X\langle n\rangle)^{\mathrm{red}}[-\mathbf 1]\), translated in the spectral coordinates. The large simplicial diagram \(F(X(1))^{\mathrm{red}}(-1)\) of \(\operatorname{Simpl}(\mathcal B)\) has components \(E^{(n)}\). Let
\[
\begin{gathered}D_F(X)\colon\bar\Delta'\to\operatorname{Simpl}(\mathcal B),\\ [n-1]\mapsto\operatorname{diag}E^{(n)},\end{gathered}
\]
be its diagonal over all \(n+1\) coordinates (Section 2 of the lesson on multisimplicial objects, taken together with the last coordinate). The *stabilization* of \(F\) at \(X\) is
\[
F^{\mathrm{st}}(X)=\operatorname{diag}C_\bullet\bigl(D_F(X)\bigr)\in\operatorname{Simpl}(\mathcal B),
\]
where \(C_\bullet\) is the simplicial replacement over \(\bar\Delta'\) of Section 1 of the lesson on derived colimits, applied termwise. It is a simplicial object of \(\operatorname{Simpl}(\mathcal B)\), and we take the diagonal. This is a functor \(F^{\mathrm{st}}\colon\operatorname{Simpl}(\mathcal A)\to\operatorname{Simpl}(\mathcal B)\).

All constructions act termwise in the coordinate of \(X\). Diagonals may be taken in any order. So \(F^{\mathrm{st}}(X)\) is the diagonal of the bisimplicial object \(q\mapsto F^{\mathrm{st}}(X_q)\), obtained by applying the construction to each object \(X_q\), regarded as a constant simplicial object.

**Proposition 3.3.** There is an isomorphism \(NF^{\mathrm{st}}(X)\cong L\varinjlim_{\bar\Delta'}ND_F(X)\) in \(D(\mathcal B)\), natural in \(X\). Equivalently, \(NF^{\mathrm{st}}(X)\cong L\varinjlim N\bigl(F(X(1))^{\mathrm{red}}(-1)\bigr)\), with the derived colimit on large simplicial diagrams of Section 4 of the lesson on multisimplicial objects.

**Proof.** The simplicial replacement \(C_\bullet(D_F(X))\) is bisimplicial, with \(C_p(D_F(X))_r=\bigoplus_{\tau}D_F(X)(\tau_0)_r\), the sum over the strings \(\tau=(\tau_0\to\cdots\to\tau_p)\) of \(\bar\Delta'\). By Lemma 2.6 of the lesson on multisimplicial objects, \(NF^{\mathrm{st}}(X)\) is homotopy equivalent to the total complex of its normalizations in \(p\) and \(r\). Normalizing in \(r\) commutes with \(C_\bullet\), and in \(p\) the normalized and unnormalized complexes are homotopy equivalent (Theorem 1.1 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex)). So \(NF^{\mathrm{st}}(X)\) is quasi-isomorphic to the total complex of \(C_p(ND_F(X))\), which is \(L\varinjlim_{\bar\Delta'}ND_F(X)\) by Theorem 2.3 of the lesson on derived colimits. Read cohomologically, \(ND_F(X)\) is bounded above. For the second form, Proposition 4.4 of the lesson on multisimplicial objects computes \(LH_0\) by the normalized diagonals in the spectral coordinates. The diagonal with the last coordinate is then compared by Lemma 2.6 there, naturally in \(\bar\Delta'\). \(\square\)

**Lemma 3.4.** For every \(r\geq0\), the diagram \([n-1]\mapsto D_F(X)([n-1])_r\) of \(\mathcal B\) is colimit-acyclic. Its colimit is the direct sum of \(F^+(X_r)\) and of objects \(V_k\), \(k\geq1\), defined in the proof.

**Proof.** Let \(n\geq1\) and write \(P=F^+(X\langle n\rangle)\), reduced in the spectral coordinates. By Lemma 1.1 of the lesson on multisimplicial objects, applied in the spectral coordinates, \(E^{(n)}=\Gamma\bigl((N_{\mathrm{sp}}P)[-\mathbf 1]\bigr)\), where \(N_{\mathrm{sp}}\) normalizes the spectral coordinates only. In degree \(r\) of the diagonal, this gives a decomposition
\[
\begin{aligned}&D_F(X)([n-1])_r\\&\quad =\bigoplus_{(\sigma_0,\ldots,\sigma_{n-1})}(N_{\mathrm{sp}}P)\bigl(\rho(\sigma)+\mathbf 1;r\bigr),\end{aligned}
\]
over the tuples of surjections \(\sigma_k\colon[r]\twoheadrightarrow[\rho_k]\). Let \(K(\sigma)\) be the set of \(k\) with \(\rho_k\geq1\). For \(k\notin K(\sigma)\), the summand lies in the part of \(N_{\mathrm{sp}}P\) with \(k\)-th coordinate \(1\). By Lemma 1.2 (4) of the lesson on multisimplicial objects, that part is the normalization of the face \(\partial^1_kP\). This face is \(F^+(X\langle n-1\rangle)\) through the structure map of the spectrum. So the summand of \(\sigma\) depends only on \(K=K(\sigma)\) and on the surjections \((\sigma_k)_{k\in K}\), and it equals \(V(\sigma_K)=(N_{\mathrm{sp}}F^+(X\langle|K|\rangle))(\rho_K+\mathbf 1;r)\). The map induced by \(\delta\colon[n-1]\to[n'-1]\) inserts constant surjections in the coordinates outside the image of \(\delta\) (Proposition 1.3 (2) there). So it carries the summand of \((K,\sigma_K)\) identically to the summand of \((\delta(K),\sigma_K)\).

Identify a subset \(K\) of \([n-1]\) with \(|K|=k\) with the injective increasing map \([k-1]\to[n-1]\) onto it. The part of the diagram with \(|K|\geq1\) is then the sum over \(k\geq1\) of the induced diagrams \(V_k\otimes\mathbb Z[\operatorname{Hom}_{\bar\Delta'}([k-1],-)]\), where \(V_k=\bigoplus_{\sigma_1,\ldots,\sigma_k}V(\sigma)\) over nonconstant surjections. Induced diagrams are colimit-acyclic (Lemma 1.1 of the lesson on derived colimits), with colimit \(V_k\). The part with \(K=\varnothing\) is \(F^+(X_r)\) at every \([n-1]\) with \(n\geq1\), and \(F(X_r)=F^+(X_r)\oplus F(0)\) at \([-1]\), with the projection as structure map. It is the sum of the constant diagram \(F^+(X_r)\) and of the diagram \(F(0)\) concentrated at \([-1]\). The first is colimit-acyclic with colimit \(F^+(X_r)\). The second is colimit-acyclic with colimit \(0\) (Lemma 3.1 of the lesson on derived colimits). \(\square\)

**Lemma 3.5.** Let \(i\geq0\). The diagram \([n-1]\mapsto H_i(D_F(X)([n-1]))\) is locally constant on the full subcategory of the \([n-1]\) with \(n>i\). For \(n\geq1\) there are isomorphisms \(H_i(D_F(X)([n-1]))\cong H_{i+n}F^+(X[n])\), natural in \(X\).

**Proof.** *The values.* Let \(n\geq1\) and \(P=F^+(X\langle n\rangle)\). By Lemma 2.6 of the lesson on multisimplicial objects, \(N\operatorname{diag}E^{(n)}\) is homotopy equivalent to \(\operatorname{Tot}NE^{(n)}\). Since \(NE^{(n)}\) is \(NP\) translated down by one in each spectral coordinate, \(\operatorname{Tot}NE^{(n)}\) is isomorphic, by signs \(\pm1\) on the summands, to \(\operatorname{Tot}NP\) shifted down by \(n\) degrees. By Lemma 2.6 again, \(\operatorname{Tot}NP\) is homotopy equivalent to \(NF^+(W)\), where \(W=\operatorname{diag}X\langle n\rangle\). Finally \(N W\) is homotopy equivalent to \(\operatorname{Tot}NX\langle n\rangle\). This is \(NX\) placed in spectral multidegree \(\mathbf 1\) (Lemma 3.4 there), so it is isomorphic to \((NX)[n]\) up to signs. So there is a map \(W\cong\Gamma NW\to\Gamma((NX)[n])=X[n]\) whose normalization is a homotopy equivalence. By Lemma 1.3, \(H_{i+n}F^+(W)\cong H_{i+n}F^+(X[n])\). All these maps are natural in \(X\).

*The maps.* Let \(\delta^j\colon[n-1]\to[n]\) be a coface. On \(\operatorname{Tot}NE^{(n)}\to\operatorname{Tot}NE^{(n+1)}\), it is the inclusion of the terms with \(j\)-th spectral coordinate \(0\). Under the identifications above, up to sign, it becomes the inclusion of the terms with \(j\)-th coordinate \(1\) in \(\operatorname{Tot}NF^+(X\langle n+1\rangle)\). Here the spectrum identifies \(X\langle n\rangle\) with the face \(\partial^1_jX\langle n+1\rangle\). The object \(X\langle n+1\rangle\) is the nerve, in its \(j\)-th coordinate, of the commutative group object \(X\langle n\rangle\): its value is a sum of copies of \(X_q\) indexed by a product of finite sets, and the coordinates play symmetric roles. Diagonalize all coordinates except the \(j\)-th, using Lemma 2.6 there in those coordinates. The resulting bisimplicial object is \(F^+(\mathcal BW)\), and the inclusion of the terms with \(j\)-th coordinate \(1\) is the inclusion of the column \(p=1\). So the map induced by \(\delta^j\) on \(H_i\) is, up to sign and the isomorphisms above, the suspension
\[
\begin{aligned}&\sigma \colon H_{i+n}F^+(W)\\&\quad \to H_{i+n+1}\bigl(\operatorname{Tot}NF^+(\mathcal BW)\bigr).\end{aligned}
\]
The map \(W\to X[n]\) of the first part has a homotopy equivalence as normalization, and \(X[n]\) is \(n\)-reduced. By Corollary 2.2 with \(T=F^+\), \(\sigma\) is an isomorphism for \(i+n<2n\), that is, \(n>i\). Every arrow of \(\bar\Delta'\) is a composite of cofaces. \(\square\)

**Theorem 3.6 (stabilization).** Let \(X\in\operatorname{Simpl}(\mathcal A)\).

1. The canonical map \(F^{\mathrm{st}}(X)\to\varinjlim_{\bar\Delta'}D_F(X)\), given by the augmentation of the simplicial replacement, is a quasi-isomorphism.
2. For \(i\geq0\) and \(n>i\) there is an isomorphism \(H_iF^{\mathrm{st}}(X)\cong H_{i+n}F^+(X[n])\), natural in \(X\). Under these isomorphisms, the identification for \(n\) and the one for \(n+1\) differ by the suspension of Theorem 2.1, up to sign.

**Proof.** By Proposition 3.3, \(NF^{\mathrm{st}}(X)\cong L\varinjlim ND_F(X)\). In cohomological degree \(-i\), Lemma 3.5 shows that the cohomology diagrams are locally constant on \(\bar\Delta'_{\geq i}\). By Theorem 3.3 (1) of the lesson on derived colimits, with \(n(-i)=i\), the canonical map \(H_i(D_F(X)([n-1]))\to\) \(H_iL\varinjlim ND_F(X)\) is an isomorphism for \(n-1\geq i\). Combined with Lemma 3.5, this gives (2). The terms of \(ND_F(X)\) are natural direct summands of those of the unnormalized complex, so they are colimit-acyclic by Lemma 3.4. Theorem 3.3 (2) there shows that \(L\varinjlim ND_F(X)\to\varinjlim ND_F(X)\) is an isomorphism. Through Proposition 3.3 this map is the normalization of the augmentation \(F^{\mathrm{st}}(X)\to\varinjlim D_F(X)\), which gives (1). \(\square\)

So \(H_iF^{\mathrm{st}}(X)\) is the \(i\)-th stable homology group of \(F\) at \(X\) in the sense of Dold and Puppe. By Lemma 3.4, \(\varinjlim D_F(X)\) is an explicit model of \(F^{\mathrm{st}}(X)\). In degree \(r\) it is the sum of \(F^+(X_r)\) and of the \(V_k\), \(k\geq1\).

**Corollary 3.7.** The inclusion \(F^+\to F\) induces a quasi-isomorphism \((F^+)^{\mathrm{st}}(X)\to F^{\mathrm{st}}(X)\). If \(F\) is additive, there is a canonical quasi-isomorphism \(F^{\mathrm{st}}(X)\to F(X)\).

**Proof.** The inclusion is compatible with the isomorphisms of Theorem 3.6 (2), and \((F^+)^+=F^+\). If \(F\) is additive, then \(F(0)=0\), and \(F\) commutes with nerves, normalizations and \(\Gamma\). So \(F(X\langle n\rangle)[-\mathbf 1]=F(X)\langle n\rangle[-\mathbf 1]\cong F(X)\), constant in the spectral coordinates, compatibly with the structure maps, as in the identification \((cG)(1)(-1)\cong cG\). Hence \(D_F(X)\) is the constant diagram with value \(F(X)\), whose colimit is \(F(X)\). Theorem 3.6 (1) gives the quasi-isomorphism. \(\square\)

**Corollary 3.8.** If \(f\colon X\to Y\) is a map in \(\operatorname{Simpl}(\mathcal A)\) whose normalization is a chain homotopy equivalence, for instance a simplicial homotopy equivalence, then \(F^{\mathrm{st}}(f)\) is a quasi-isomorphism.

**Proof.** \(f[n]=\Gamma((Nf)[n])\) has a homotopy equivalence as normalization. By Lemma 1.3, \(F^+(f[n])\) induces isomorphisms in homology. Apply Theorem 3.6 (2). \(\square\)

## 4. Additivity and the shift isomorphism

**Proposition 4.1.** Let \(F\) be reduced, and let \(0\to X\xrightarrow{i}Y\xrightarrow{j}Z\to0\) be an exact sequence in \(\operatorname{Simpl}(\mathcal A)\).

1. If the sequence is split by a section \(s\) of \(j\), then \(F^{\mathrm{st}}(i)+F^{\mathrm{st}}(s)\colon\) \(F^{\mathrm{st}}(X)\oplus F^{\mathrm{st}}(Z)\to\) \(F^{\mathrm{st}}(Y)\) is a quasi-isomorphism.
2. If the sequence is split in each degree, then \(F^{\mathrm{st}}(i)\) is a monomorphism, \(F^{\mathrm{st}}(j)\) is an epimorphism, \(F^{\mathrm{st}}(j)F^{\mathrm{st}}(i)=0\), and the induced map \(\operatorname{Coker}F^{\mathrm{st}}(i)\to F^{\mathrm{st}}(Z)\) is a quasi-isomorphism.

**Proof.** (1) Let \(n>m\). The isomorphism \(i[n]+s[n]\colon X[n]\oplus Z[n]\to Y[n]\) gives
\[
\begin{aligned}&F(Y[n]) \cong F(X[n]) \oplus F(Z[n])\\&\quad \oplus\operatorname{cr}_2F(X[n],Z[n]),\end{aligned}
\]
where \(F(i[n])\) and \(F(s[n])\) are the inclusions of the first two summands. Since \(X[n]\) and \(Z[n]\) are \(n\)-reduced, Lemma 1.2 gives \(H_{m+n}\operatorname{cr}_2F(X[n],Z[n])=0\), because \(m+n<2n\). So \(H_{m+n}F(i[n])+H_{m+n}F(s[n])\) is an isomorphism. By the naturality in Theorem 3.6 (2), so is \(H_m(F^{\mathrm{st}}(i)+F^{\mathrm{st}}(s))\).

(2) Since \(F(0)=0\), \(F^{\mathrm{st}}(j)F^{\mathrm{st}}(i)=F^{\mathrm{st}}(ji)\) factors through \(F^{\mathrm{st}}(0)=0\). In each degree, \(i\) has a left inverse and \(j\) a right inverse. These pass to the iterated nerves in each multidegree, to \(F\), to the reductions (summands) and to the additive constructions that follow. So \(F^{\mathrm{st}}(i)\) is a monomorphism and \(F^{\mathrm{st}}(j)\) an epimorphism in each degree. For the last assertion, first let \(X\), \(Y\), \(Z\) be objects of \(\mathcal A\), regarded as constant simplicial objects. Then the sequence is split, say by \(s\). Put \(\varphi=F^{\mathrm{st}}(i)+F^{\mathrm{st}}(s)\). The map of exact sequences, written in columns,
\[
\begin{array}{ccc}
0&&0\\
\downarrow&&\downarrow\\
F^{\mathrm{st}}(X)&=&F^{\mathrm{st}}(X)\\
\downarrow&&\downarrow\\
F^{\mathrm{st}}(X)\oplus F^{\mathrm{st}}(Z)&\xrightarrow{\varphi}&F^{\mathrm{st}}(Y)\\
\downarrow&&\downarrow\\
F^{\mathrm{st}}(Z)&\xrightarrow{c}&\operatorname{Coker}F^{\mathrm{st}}(i)\\
\downarrow&&\downarrow\\
0&&0
\end{array}
\]
has the quasi-isomorphism \(\varphi\) in the middle by (1). By the five lemma, \(c\) is a quasi-isomorphism. The composite of \(c\) with \(\operatorname{Coker}F^{\mathrm{st}}(i)\to F^{\mathrm{st}}(Z)\) is \(F^{\mathrm{st}}(js)=1\), so the latter is a quasi-isomorphism. In general, \(F^{\mathrm{st}}\) and the cokernel are diagonals of the corresponding bisimplicial objects \(q\mapsto F^{\mathrm{st}}(X_q)\). The map \(\operatorname{Coker}F^{\mathrm{st}}(i_q)\to F^{\mathrm{st}}(Z_q)\) is a quasi-isomorphism for each \(q\) by the first case. A map of bisimplicial objects that is a quasi-isomorphism in one coordinate for each fixed value of the other induces a quasi-isomorphism of total complexes, by the column filtration, hence of diagonals by Lemma 2.6 of the lesson on multisimplicial objects. \(\square\)

**The shift isomorphism.** Complexes are shifted as in the derived category: \((C[1])_m=C_{m-1}\) with differential \(-d\) for chain complexes. For a nonnegative chain complex \(C\), the cone of the identity, \(\operatorname{Cone}(1_C)_m=C_{m-1}\oplus C_m\) with \(d(c',c)=(-dc',c'+dc)\), is contractible, and \(0\to C\to\operatorname{Cone}(1_C)\to C[1]\to0\) is split in each degree. For \(X\in\operatorname{Simpl}(\mathcal A)\) put \(\gamma X=\Gamma\operatorname{Cone}(1_{NX})\) and \(\sigma X=\Gamma((NX)[1])\). This gives the *cone sequence* \(0\to X\to\gamma X\to\sigma X\to0\), split in each degree, with \(\gamma X\) homotopy equivalent to \(0\). The simplicial object \(\sigma X\) represents \(X[1]\), and it is isomorphic to the translate of the Conventions through signs.

In the derived category, the triangle of a short exact sequence of complexes is the one of [Stacks, Tag 0152]. For a sequence split in each degree, its third map is \(\pi d s\) computed with any splitting [Stacks, Tags 014I, 0154]. For the cone sequence it is the identity of \(C[1]\) [Stacks, Tag 014O].

**Proposition 4.2.** Let \(F\) be reduced and \(X\in\operatorname{Simpl}(\mathcal A)\). Let \(\partial\colon\operatorname{Coker}F^{\mathrm{st}}(i)\to F^{\mathrm{st}}(X)[1]\) be the third map of the triangle of \(0\to\) \(F^{\mathrm{st}}(X)\to\) \(F^{\mathrm{st}}(\gamma X)\to\) \(\operatorname{Coker}F^{\mathrm{st}}(i)\to\) \(0\), where \(i\colon X\to\gamma X\), and let \(q\colon\operatorname{Coker}F^{\mathrm{st}}(i)\to F^{\mathrm{st}}(\sigma X)\) be the quasi-isomorphism of Proposition 4.1 (2). Then
\[
\theta_X=\partial\circ q^{-1}\colon F^{\mathrm{st}}(\sigma X)\longrightarrow F^{\mathrm{st}}(X)[1]
\]
is an isomorphism in \(D(\mathcal B)\), natural in \(X\). For the identity functor, \(\theta_X\) is the identity of \((NX)[1]\), through the quasi-isomorphism of Corollary 3.7.

**Proof.** \(\gamma X\) is homotopy equivalent to \(0\), so \(F^{\mathrm{st}}(\gamma X)\) is acyclic by Corollary 3.8. The triangle then shows that \(\partial\) is an isomorphism. Naturality follows from the functoriality of the triangle in the short exact sequence [Stacks, Tag 0152]. For the identity functor, \(F^{\mathrm{st}}\) is identified with the identity by Corollary 3.7, the cokernel is \(\sigma X\), and \(\partial\) is the third map of the cone sequence, the identity. \(\square\)

**Proposition 4.3 (stabilization and triangles).** Let \(F\) be reduced, and let \(0\to X\xrightarrow{i}Y\xrightarrow{j}Z\to0\) be an exact sequence in \(\operatorname{Simpl}(\mathcal A)\), split in each degree. Choose splittings and let \(e\colon Z\to\sigma X\) be the map with normalization \(\pi ds\colon NZ\to(NX)[1]\). Then the triangle
\[
\begin{aligned}&F^{\mathrm{st}}(X) \to F^{\mathrm{st}}(Y) \to F^{\mathrm{st}}(Z)\\&\quad \xrightarrow{\theta_X\circ F^{\mathrm{st}}(e)}F^{\mathrm{st}}(X)[1]\end{aligned}
\]
is distinguished in \(D(\mathcal B)\).

**Proof.** Normalize, and write \(NY=NX\oplus NZ\) in each degree. The differential of \(NY\) is the matrix with rows \((d,\pi ds)\) and \((0,d)\). Then \(g(x,z)=(\pi ds\,z,x)\) defines a map of complexes \(NY\to\operatorname{Cone}(1_{NX})\), because \(\pi ds\) is a map of complexes \(NZ\to(NX)[1]\). Together with the identity of \(NX\) and \(\pi ds\), it is a map from the normalized sequence to the cone sequence. Apply \(\Gamma\). This gives a map of short exact sequences \((1,\Gamma g,e)\) from \(0\to X\to Y\to Z\to0\) to the cone sequence of \(X\). Apply \(F^{\mathrm{st}}\) and pass to the cokernels of \(F^{\mathrm{st}}(i)\). The resulting map of short exact sequences gives a map of triangles [Stacks, Tag 0152]. So the third map of the triangle of \(0\to F^{\mathrm{st}}(X)\to F^{\mathrm{st}}(Y)\to\operatorname{Coker}\to0\) is \(\partial\circ c\), where \(c\) is the induced map of cokernels. By naturality of the quasi-isomorphisms of Proposition 4.1 (2), \(q\circ c=F^{\mathrm{st}}(e)\circ q_Y\), where \(q_Y\colon\operatorname{Coker}F^{\mathrm{st}}(i)\to F^{\mathrm{st}}(Z)\). So, through \(q_Y\), this distinguished triangle is isomorphic to the triangle of the statement, whose third map is \(\partial c\,q_Y^{-1}=\partial q^{-1}F^{\mathrm{st}}(e)=\theta_X\circ F^{\mathrm{st}}(e)\). \(\square\)

With the sign conventions of the Stacks project, the third map of the cone sequence is \(+1\), and no sign enters \(\theta_X\). In conventions where that map is \(-1\), the shift isomorphism must be defined with a sign to make Proposition 4.3 hold.

**Lemma 4.4 (connecting morphisms of a \(3\times3\) diagram).** Let
\[
\begin{array}{ccccc}
X'&\xrightarrow{f'}&X&\xrightarrow{g'}&X''\\
\downarrow{\scriptstyle a'}&&\downarrow{\scriptstyle a}&&\downarrow{\scriptstyle a''}\\
Y'&\xrightarrow{f}&Y&\xrightarrow{g}&Y''\\
\downarrow{\scriptstyle b'}&&\downarrow{\scriptstyle b}&&\downarrow{\scriptstyle b''}\\
Z'&\xrightarrow{f''}&Z&\xrightarrow{g''}&Z''
\end{array}
\]
be a commutative diagram of complexes of an abelian category whose rows and columns are short exact sequences. Let \(\delta_X\colon X''\to X'[1]\) and \(\delta_Z\colon Z''\to Z'[1]\) be the third maps of the triangles of the first and the last row, and \(\delta'\colon Z'\to X'[1]\) and \(\delta''\colon Z''\to X''[1]\) those of the first and the last column [Stacks, Tag 0152]. Then
\[
\delta'[1]\circ\delta_Z=-\,\delta_X[1]\circ\delta''.
\]

**Proof.** Complexes are written cohomologically here. For a short exact sequence \(0\to A\xrightarrow{u}B\xrightarrow{v}C\to0\), the third map of its triangle is \(-p\,q^{-1}\), where \(C(u)^k=B^k\oplus A^{k+1}\) with \(d(y,x)=(dy+ux,-dx)\), \(q(y,x)=v(y)\) is a quasi-isomorphism and \(p(y,x)=x\) [Stacks, Tags 014E, 0152]. Write \(q_u\), \(p_u\) for these maps.

The square \((f',f)\) from \(a'\) to \(a\) induces \(\varphi\colon C(a')\to C(a)\), \(\varphi(y',x')=(fy',f'x')\). Its cone \(W=C(\varphi)\) has \(W^k=Y^k\oplus X^{k+1}\oplus Y'^{k+1}\oplus X'^{k+2}\) and
\[
\begin{aligned}&d(y,x,y',x')\\&\quad=\bigl(dy+ax+fy',\ -dx+f'x',\\&\qquad-dy'-a'x',\ dx'\bigr).\end{aligned}
\]
Let \(Q\colon W\to Z''\) be \((y,x,y',x')\mapsto g''b(y)\), \(\lambda\colon W\to X'[2]\) the projection \((y,x,y',x')\mapsto x'\), and \(\pi\colon W\to C(a')[1]\) the projection to \((y',x')\). The quasi-isomorphisms \(q_a\colon C(a)\to Z\) and \(q_{a'}\colon C(a')\to Z'\) satisfy \(q_a\varphi=f''q_{a'}\), so they induce a map of cones \(\kappa\colon W\to C(f'')\), \(\kappa(y,x,y',x')=(by,b'y')\), a quasi-isomorphism by the five lemma. Then \(q_{f''}\kappa=Q\), so \(Q\) is a quasi-isomorphism, and \(p_{f''}\kappa=q_{a'}[1]\,\pi\). Hence
\[
\begin{aligned}\delta'[1]\circ\delta_Z&=p_{a'}[1]\,q_{a'}[1]^{-1}\,p_{f''}\,q_{f''}^{-1}\\&=p_{a'}[1]\,q_{a'}[1]^{-1}\,q_{a'}[1]\,\pi\,Q^{-1}\\&=p_{a'}[1]\,\pi\,Q^{-1}=\lambda\,Q^{-1}.\end{aligned}
\]
Exchanging the roles of rows and columns, the square \((a,a')\) from \(f'\) to \(f\) induces \(\psi\colon C(f')\to C(f)\), and the same computation gives \(\delta_X[1]\circ\delta''=\lambda'Q'^{-1}\) on \(W'=C(\psi)\), with \(W'^k=Y^k\oplus Y'^{k+1}\oplus X^{k+1}\oplus X'^{k+2}\), \(Q'(y,y',x,x')=b''g(y)\) and \(\lambda'(y,y',x,x')=x'\). Its differential is
\[
\begin{aligned}&d(y,y',x,x')\\&\quad=\bigl(dy+fy'+ax,\ -dy'+a'x',\\&\qquad-dx-f'x',\ dx'\bigr).\end{aligned}
\] So \(\tau(y,x,y',x')=(y,y',x,-x')\) is an isomorphism of complexes \(W\to W'\), with \(Q'\tau=Q\), because \(b''g=g''b\), and \(\lambda'\tau=-\lambda\). Therefore \(\delta_X[1]\circ\delta''=\lambda'\tau\,(Q'\tau)^{-1}=-\lambda\,Q^{-1}\). \(\square\)

**Proposition 4.5 (the shift and exact sequences of functors).** Let \(0\to F'\to F\to F''\to0\) be natural transformations of reduced functors \(\mathcal A\to\mathcal B\), and \(\mathcal P\subseteq\mathcal A\) a full subcategory closed under finite direct sums and direct summands such that \(0\to F'(M)\to F(M)\to F''(M)\to0\) is exact for every \(M\in\mathcal P\). Let \(X\) be a simplicial object of \(\mathcal P\). Then the sequences \(0\to F'^{\mathrm{st}}(Y)\to F^{\mathrm{st}}(Y)\to F''^{\mathrm{st}}(Y)\to0\) are exact for \(Y=X,\gamma X,\sigma X\), and the third maps \(\delta_Y\) of their triangles satisfy
\[
\theta^{F'}_X[1]\circ\delta_{\sigma X}=-\,\delta_X[1]\circ\theta^{F''}_X.
\]

**Proof.** The terms of \(\gamma X\), \(\sigma X\) and of the components of their spectra are finite direct sums of direct summands of terms of \(X\), so they lie in \(\mathcal P\). The functors are applied termwise, and the constructions of Definition 3.2 that follow, reduction, translation, diagonals and the simplicial replacement, are exact in the functor. So the three sequences are exact. Write \(K_G=\operatorname{Coker}G^{\mathrm{st}}(i)\) for \(G=F',F,F''\), with \(i\colon X\to\gamma X\). The diagram whose rows are the sequences \(0\to G^{\mathrm{st}}(X)\to G^{\mathrm{st}}(\gamma X)\to K_G\to0\) and whose columns are the sequences of the statement for \(X\), for \(\gamma X\) and the induced sequence of the \(K_G\) is commutative. Its rows are exact by Proposition 4.1 (2), and its third column is exact by the snake lemma [Stacks, Tag 010H], since \(F''^{\mathrm{st}}(i)\) is a monomorphism. Let \(\partial^G\colon K_G\to G^{\mathrm{st}}(X)[1]\) be the third maps of the triangles of the rows and \(\delta_K\colon K_{F''}\to K_{F'}[1]\) that of the third column. Lemma 4.4 gives
\[
\delta_X[1]\circ\partial^{F''}=-\,\partial^{F'}[1]\circ\delta_K.
\]
The quasi-isomorphisms \(q_G\colon K_G\to G^{\mathrm{st}}(\sigma X)\) of Proposition 4.1 (2) are natural in \(G\), so they form a morphism from the third column to the sequence for \(\sigma X\), and \(\delta_{\sigma X}\,q_{F''}=q_{F'}[1]\,\delta_K\) [Stacks, Tag 0152]. With \(\theta^G_X=\partial^G q_G^{-1}\) (Proposition 4.2),
\[
\begin{aligned}\theta^{F'}_X[1]\circ\delta_{\sigma X}&=\partial^{F'}[1]\,q_{F'}[1]^{-1}\,\delta_{\sigma X}\\&=\partial^{F'}[1]\,\delta_K\,q_{F''}^{-1}\\&=-\,\delta_X[1]\,\partial^{F''}q_{F''}^{-1}\\&=-\,\delta_X[1]\circ\theta^{F''}_X.\end{aligned}
\]
\(\square\)

## 5. Examples

**Example 5.1 (additive functors).** If \(F\) is additive, Corollary 3.7 gives \(F^{\mathrm{st}}\simeq F\), and \(\theta_X\) is \(F\) of the identification \(\sigma X=X[1]\).

**Example 5.2 (functors of degree two built from bilinear maps).** Let \(T\colon\mathcal A\times\mathcal A\to\mathcal B\) vanish when one variable is \(0\), and \(F(M)=T(M,M)\), for instance \(F(M)=M\otimes M\) for modules. By Lemma 1.2, \(F(X[n])\) has no homology below degree \(2n\), so \(F^{\mathrm{st}}(X)\) is acyclic by Theorem 3.6 (2). In particular the stabilization of a cross-effect of order \(r\geq2\), evaluated on the diagonal, is acyclic. This is the mechanism behind Proposition 4.1 (1).

**Example 5.3 (the symmetric square of \(\mathbb Z\)).** Let \(\mathcal A=\mathcal B\) be abelian groups, \(F=S^2\) and \(X=\mathbb Z\), so that \(X[n]\) is the simplicial abelian group \(K(\mathbb Z,n)=\Gamma(\mathbb Z[n])\). Its normalized complex \(NS^2K(\mathbb Z,n)\) has a basis of the monomials \(e_ae_b\) of basis elements of \(K(\mathbb Z,n)_q\) whose jump sets cover \(\{0,\ldots,q-1\}\). These are finite complexes of free abelian groups, and their homology, computed by Smith normal forms, is as follows. The table lists the nonzero groups \(H_qS^2K(\mathbb Z,n)\) for \(q\le2n+1\).

| \(n\) | nonzero \(H_q\), \(q\le2n+1\) |
|---|---|
| \(1\) | none |
| \(2\) | \(H_4=\mathbb Z\) |
| \(3\) | \(H_5=\mathbb Z/2\) |
| \(4\) | \(H_6=\mathbb Z/2\), \(H_8=\mathbb Z\) |
| \(5\) | \(H_7=\mathbb Z/2\), \(H_9=\mathbb Z/2\) |

The groups agree with Theorem 2.1. In degrees \(q<2n\) the suspension carries \(H_{n+2}\) to \(H_{n+3}\), and in degree \(2n=4\) the group \(\mathbb Z=H_4\) for \(n=2\) maps onto \(\mathbb Z/2=H_5\) for \(n=3\). By Theorem 3.6 (2), the stable groups are \(H_i(S^2)^{\mathrm{st}}(\mathbb Z)=0\) for \(i=0,1,3\) and \(\mathbb Z/2\) for \(i=2,4\). The same computation for \(\Gamma^2\) and \(\Lambda^2\) gives the stable groups \(\mathbb Z/2\) in degrees \(0,2,4\) for \(\Gamma^2\) and in degrees \(1,3\) for \(\Lambda^2\), and \(0\) otherwise in degrees \(\le4\) and \(\le3\). For the tensor square they are \(0\), as Example 5.2 predicts. The shifts between these three functors are explained in the lesson on stable derived functors.

## 6. Exercises

**6.1.** Let \(F\) be reduced of degree \(\le1\) in the sense of the lesson on non-additive functors. Show that \(F\) is additive. Deduce \(H_iF^{\mathrm{st}}(X)\cong H_iF(X)\) directly from Theorem 3.6 (2).

**6.2.** Let \(F\) be reduced. Show that \(H_0F^{\mathrm{st}}(M)\), for an object \(M\) of \(\mathcal A\), is the cokernel of the map \(\operatorname{cr}_2F(M,M)\to F(M)\) induced by the sum \(M\oplus M\to M\).

**6.3.** Let \(\mathcal A\) be abelian groups, \(F(M)=M\otimes M\), and \(Z=K(\mathbb Z,1)\). Compute the suspension \(\sigma\colon H_mF(Z)\to H_{m+1}(\operatorname{Tot}NF(\mathcal BZ))\) for \(m\le2\), and check Theorem 2.1 for \(n=1\).

## 7. Complete solutions

**6.1.** For a reduced functor of degree \(\le1\), the cross-effects of order two vanish, so \(F(M\oplus M')=F(M)\oplus F(M')\) through the two inclusions, and the projections are \(F\) of the projections. Let \(f,g\colon M\to M'\). Then \(f+g\) is the composite of the diagonal \(\Delta\colon M\to M\oplus M\), \(f\oplus g\), and the sum \(\nabla\colon M'\oplus M'\to M'\). In the decompositions, \(F(\Delta)\) is the diagonal of \(F(M)\), \(F(f\oplus g)=F(f)\oplus F(g)\), and \(F(\nabla)\) is the sum of \(F(M')\oplus F(M')\to F(M')\). So \(F(f+g)=F(f)+F(g)\). An additive functor commutes with \(N\) and \(\Gamma\), so \(F(X[n])=\Gamma((NFX)[n])=F(X)[n]\), and Theorem 3.6 (2) gives \(H_iF^{\mathrm{st}}(X)\cong H_{i+n}(F(X)[n])=H_iF(X)\), in accordance with Corollary 3.7.

**6.2.** By Theorem 3.6 (2) with \(n=1\), \(H_0F^{\mathrm{st}}(M)=H_1F(M[1])\), and \(M[1]=K(M,1)\) is the nerve of \(M\). Its normalized complex is \(0\) in degree \(0\) and \(F(M)\) in degree \(1\). In degree \(2\) it is the quotient of \(F(M\oplus M)\) by the degenerate summands \(\operatorname{cr}_{\{1\}}\oplus\operatorname{cr}_{\{2\}}\), that is, \(\operatorname{cr}_2F(M,M)\). The faces \(d_0\) and \(d_2\) drop an index and kill \(\operatorname{cr}_2F\) by Lemma 1.1. The face \(d_1\) is \(F\) of the sum map. So \(H_1=\) \(F(M)/\operatorname{im}\bigl(\operatorname{cr}_2F(M,M)\to F(M)\bigr)\).

**6.3.** \(F(Z)=Z\otimes Z\) degreewise, the diagonal of \(Z\boxtimes Z\). By Lemma 2.6 of the lesson on multisimplicial objects its homology is that of \(NZ\otimes NZ=\mathbb Z[1]\otimes\mathbb Z[1]=\mathbb Z[2]\): \(H_2=\mathbb Z\), all other groups \(0\). The bar construction gives \(F(\mathcal BZ)(p,q)=(Z_q^{\oplus p})^{\otimes2}\), with \(\operatorname{Tot}N\) homotopy equivalent to \(N\operatorname{diag}\) of \(F(\operatorname{diag}\mathcal BZ)\simeq F(K(\mathbb Z,2))\). Its homology is that of \(\mathbb Z[2]\otimes\mathbb Z[2]=\mathbb Z[4]\). For \(m\le1\) both sides vanish, so \(\sigma\) is an isomorphism. For \(m=2=2n\), \(\sigma\colon\mathbb Z=H_2\to H_3=0\) is an epimorphism and not injective. This matches Theorem 2.1, and its range cannot be improved here.

## Sources

The cross-effect decomposition of the bar construction, the connectivity of cross-effects, the suspension theorem and the stable homology groups are due to A. Dold and D. Puppe, *Homologie nicht-additiver Funktoren. Anwendungen*, Annales de l'Institut Fourier 11 (1961), 201–312 ([Numdam](https://www.numdam.org/articles/10.5802/aif.114/)), Sections 4–8. The stabilization through spectral diagrams, its identification with the stable homology groups, and its additivity and exactness are due to Illusie, in his work on the cotangent complex. Breen used this construction in *Extensions du groupe additif*, Publications Mathématiques de l'IHÉS 48 (1978), 39–125 ([Numdam](https://www.numdam.org/item/PMIHES_1978__48__39_0/)).
