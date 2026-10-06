# The Pontryagin duality theorem

**Lesson HA-LCA-09.** Self-checked by the writing AI.

Let \(G\) be a locally compact Hausdorff abelian group. There is no countability assumption. Put \(\Gamma=\widehat G\) and \(D=\widehat\Gamma\), both with their compact-open topologies. Characters take values in \(\mathbb T\). We use additive notation in \(G\) and multiplicative notation for characters. Haar measure \(dx\) has the complete locally determined domain constructed in the earlier Haar reading. Its dual measure is \(d\xi\), as constructed in [HA-LCA-07, Theorem 2.1](the-fourier-inversion-theorem-and-the-dual-haar-measure.md#ha-lca-07-theorem-2-1). Our conventions are
\[
 \widehat f(\gamma)=\int_G f(x)\overline{\gamma(x)}\,dx,
 \qquad T\mu(x)=\int_\Gamma\gamma(x)\,d\mu(\gamma),
 \qquad J_G(x)(\gamma)=\gamma(x).
 \tag{1}
\]
The purpose of the lesson is to prove that \(J_G\) is a topological isomorphism, then use that identification to remove the \(B^1\) restriction from Fourier inversion.

The freely accessible source routes are D. H. Fremlin, [*Measure Theory*, §§445O and 445U](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt445.tex), version of 20 March 2008, and the quotient and subgroup statements in [Appendix 4A5J, L, M](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt4a5.tex), version of 4 August 2013. The compact-component argument in Exercise 6.5 uses A. Candel, [*Three Dimes of Topology*, pp. 29–30](https://www.csun.edu/~ac53971/research/topology_262.pdf), Math 262 notes, Winter 1995–96. Every needed assertion from these sources is proved below or at an exact earlier proof locator.

Adaptation and additional proofs: GPT-6 Astra (OpenAI), Ultra, October 2026. This combined lesson is under the [Design Science License](../assets/fremlin/DESIGN-SCIENCE-LICENSE.txt). Fremlin's copyrights 1998 and 2000 and original notices remain in the unchanged volume 4 source package. Candel's notes are linked, not reproduced.

We will use these earlier results:

- [HA-LCA-02, Proposition 1.4](characters-and-the-dual-group.md#ha-lca-02-proposition-1-4) proves joint continuity of the character pairing; [Theorem 5.2](characters-and-the-dual-group.md#ha-lca-02-theorem-5-2) proves that the dual is LCA. [HA-LCA-05, Corollary 4.2](raikovs-theorem-and-the-gelfand-raikov-theorem.md#ha-lca-05-corollary-4-2) proves that characters separate points and that \(J_G\) is continuous and injective.
- [HA-LCA-04, Proposition 2.2](functions-of-positive-type.md#ha-lca-04-proposition-2-2) proves positivity and continuity of \(u*\widetilde u\), where \(\widetilde u(x)=\overline{u(-x)}\). [HA-LCA-06, Theorem 2.1](bochners-theorem.md#ha-lca-06-theorem-2-1) proves Bochner's representation; its [Proposition 1.1](bochners-theorem.md#ha-lca-06-proposition-1-1) proves injectivity of \(T\) on finite Radon measures on the dual.
- [HA-LCA-07, Theorem 2.1](the-fourier-inversion-theorem-and-the-dual-haar-measure.md#ha-lca-07-theorem-2-1) proves pointwise inversion for \(B^1(G)=B(G)\cap L^1(G)\), where [HA-LCA-06, Proposition 4.1](bochners-theorem.md#ha-lca-06-proposition-4-1) identifies \(B(G)\) with transforms \(T\mu\) of finite complex Radon measures. [HA-LCA-08, Theorem 1.1](the-plancherel-theorem.md#ha-lca-08-theorem-1-1) proves Plancherel; its [Corollary 3.2](the-plancherel-theorem.md#ha-lca-08-corollary-3-2) gives a nonzero Fourier-algebra function supported inside any nonempty open subset of a dual group.
- [The Radon reading, Lemma 1.3](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-lemma-1-3) gives compactly supported continuous cutoffs, and its [Corollary 4.5](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-corollary-4-5) gives compact tails for finite Radon measures. [The general Haar reading, Theorems 3.1 and 3.3](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-theorem-3-1) supplies full support and uniqueness up to scale, and its [Theorem 4.1](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-theorem-4-1) gives Haar-preserving inversion in an abelian group.

## 1. Evaluation and its topology

<a id="ha-lca-09-lemma-1-1"></a>
**Lemma 1.1 — The pairing.** The map \(G\times\Gamma\to\mathbb T\), \((x,\gamma)\mapsto\gamma(x)\), is continuous.

**Proof.** Here is the compact-neighbourhood argument, also proved in HA-LCA-02, Proposition 1.4. Fix \((x_0,\gamma_0)\) and \(\varepsilon>0\). Choose a compact neighbourhood \(K\) of \(x_0\). For \(x\) in its interior,
\[
 |\gamma(x)-\gamma_0(x_0)|
 \le \sup_{y\in K}|\gamma(y)-\gamma_0(y)|
       +|\gamma_0(x)-\gamma_0(x_0)|.
\]
The first term is less than \(\varepsilon/2\) on a compact-open neighbourhood of \(\gamma_0\); continuity of the fixed character makes the second less than \(\varepsilon/2\) on a neighbourhood of \(x_0\) inside \(K\). This proves continuity at every pair. \(\square\)

<a id="ha-lca-09-lemma-1-2"></a>
**Lemma 1.2 — Locally compact subgroups are closed.** If a subgroup \(H\) of a Hausdorff topological group \(P\) is locally compact in the relative topology, then \(H\) is closed in \(P\).

**Proof.** Let \(K\) be a compact identity neighbourhood in \(H\), and choose an ambient open identity neighbourhood \(V\) with \(V\cap H\subseteq K\). The set \(K\) is compact in \(P\) and therefore closed there: a point outside a compact set can be separated from each of its points, and finitely many of those separations give an open neighbourhood disjoint from the compact set. If \(z\in\overline H\cap V\), each neighbourhood of \(z\), after intersection with the open set \(V\), meets \(H\cap V\). Hence \(z\in\overline{H\cap V}\subseteq K\). Thus
\[
 \overline H\cap V\subseteq H.
 \tag{2}
\]
Continuity of multiplication and inversion implies that \(\overline H\) is a subgroup: neighbourhoods of \(ab^{-1}\), for \(a,b\in\overline H\), contain products \(AB^{-1}\) of neighbourhoods of \(a,b\), which meet \(H\). By (2), \(H\) contains a relative open identity neighbourhood in \(\overline H\), so its translates show that it is open there. Every other coset is open too, making \(H\) closed in \(\overline H\). Its density then forces \(H=\overline H\). \(\square\)

<a id="ha-lca-09-lemma-1-3"></a>
**Lemma 1.3 — Evaluation is an embedding.** The map \(J_G:G\to D\) is a homomorphism and a homeomorphism onto its image.

**Proof.** Evaluation is a character on \(\Gamma\), and \(J_G(x+y)=J_G(x)J_G(y)\). Continuity and injectivity are already proved in HA-LCA-05, Corollary 4.2. It remains to recover the topology of \(G\) from compact convergence on \(\Gamma\).

Let \(U\) be any identity neighbourhood in \(G\). Group continuity and local compactness give a relatively compact open identity neighbourhood \(V\) with \(\overline V-\overline V\subseteq U\). To see the closure control, first choose an open identity neighbourhood \(W\) with \(W-W\subseteq U\), then use the Radon reading, Lemma 1.3, to choose \(V\) with compact closure inside \(W\). The same cutoff lemma gives a nonzero \(u\in C_c(G)\) with support in \(V\). Put \(h=u*\widetilde u\). The general Haar reading, Theorem 6.1, gives its compact support in \(\operatorname{supp}u-\operatorname{supp}u\subseteq U\); HA-LCA-04, Proposition 2.2, gives positive type and
\[
 h(0)=\int_G|u|^2\,dx>0.
\]
Strict positivity uses continuity of \(u\) and Haar full support. By Bochner's theorem \(h=T\mu\) for a positive finite Radon measure with \(\mu(\Gamma)=h(0)\). Choose a compact \(K\subseteq\Gamma\) with \(\mu(\Gamma\setminus K)<h(0)/8\). If
\(\sup_{\gamma\in K}|\gamma(x)-1|<1/4\), then
\[
 |h(x)-h(0)|
 \le \tfrac14\mu(K)+2\mu(\Gamma\setminus K)
 <\tfrac12 h(0).
 \tag{3}
\]
Consequently \(h(x)\ne0\), so \(x\in U\). The displayed condition defines the inverse image under \(J_G\) of an open identity neighbourhood in \(D\). Thus \(J_G^{-1}\), on its image, is continuous at the identity and hence everywhere by translation. This neighbourhood argument applies to arbitrary nets. \(\square\)

## 2. The bidual contains no further points

<a id="ha-lca-09-theorem-2-1"></a>
**Theorem 2.1 — Pontryagin duality.** For every LCA group \(G\), evaluation
\[
 J_G:G\longrightarrow\widehat{\widehat G},
 \qquad J_G(x)(\gamma)=\gamma(x),
 \tag{4}
\]
is an isomorphism of topological groups.

**Proof.** By Lemma 1.3, \(H=J_G(G)\) is a locally compact subgroup of the Hausdorff group \(D\). Lemma 1.2 makes it closed. Suppose it were proper. Apply HA-LCA-08, Corollary 3.2, with base group \(\Gamma\) to the nonempty open subset \(D\setminus H\). It gives \(g\in L^1(\Gamma)\) whose Fourier transform \(v=\widehat g\) is nonzero and has support inside \(D\setminus H\). For every \(x\in G\),
\[
 0=v(J_Gx)
   =\int_\Gamma g(\gamma)\overline{\gamma(x)}\,d\xi(\gamma)
   =T(g\,d\xi)(-x).
 \tag{5}
\]
The measure \(g\,d\xi\) is finite Radon by [HA-LCA-03, Lemma 4.1](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-lemma-4-1). The injectivity of \(T\) in HA-LCA-06, Proposition 1.1, is a theorem about measures on \(\Gamma=\widehat G\) and does not presuppose bidual surjectivity. It gives \(g\,d\xi=0\), hence \(g=0\) almost everywhere by the same density lemma. This contradicts \(v\ne0\). Therefore \(H=D\), and Lemma 1.3 proves the topological assertion. \(\square\)

<a id="ha-lca-09-lemma-2-2"></a>
**Lemma 2.2 — Bounded evaluation polynomials.** Let \(K\subseteq\Gamma\) be compact, let \(q\in C(K)\) satisfy \(\|q\|_K\le1\), and let \(\varepsilon>0\). There is a finite sum
\[
 p(\gamma)=\sum_{j=1}^r c_j\gamma(x_j)
 \quad\text{such that}\quad
 \sup_{\gamma\in\Gamma}|p(\gamma)|\le1,
 \qquad \sup_{\gamma\in K}|p(\gamma)-q(\gamma)|<\varepsilon.
 \tag{6}
\]

**Proof.** For \(K=\varnothing\), take \(p=0\). Otherwise the finite evaluation sums form a unital self-adjoint algebra: products add the \(x_j\), conjugation replaces \(x_j\) by \(-x_j\), and \(x=0\) gives the constant one. They separate distinct characters by the definition of distinct functions on \(G\). The [uniform approximation reading, Corollary 2.2](../prerequisites/src/uniform-approximation.md#ha-lca-pre-approx-corollary-2-2), therefore gives such a sum \(p_0\) with \(\|p_0-q\|_K<a\), for a chosen \(a>0\).

Put \(M=\sum_j|c_j|\), so \(|p_0|\le M\) globally. If \(M=0\), the choice \(p=0\) already has error less than \(a\). Assume \(M>0\). Define the continuous function
\[
 c(t)=
 \begin{cases}1,&0\le t\le1,\\ t^{-1/2},&t\ge1.\end{cases}
\]
The function \(r(z)=z c(|z|^2)\) has modulus at most one. For \(|w|\le1\),
\[
 |r(z)-w|\le |r(z)-z|+|z-w|
       =\max(0,|z|-1)+|z-w|\le2|z-w|.
\]
By [the same reading, Lemma 1.1](../prerequisites/src/uniform-approximation.md#ha-lca-pre-approx-lemma-1-1), choose a real polynomial \(R\) with \(|R(t)-c(t)|<b\) on \([0,M^2]\). The evaluation sum
\(p_1=p_0R(p_0\overline{p_0})\) satisfies
\(\|p_1-r(p_0)\|_\Gamma\le Mb\), hence \(\|p_1\|_\Gamma\le1+Mb\). Set \(p=p_1/(1+Mb)\). Then \(\|p\|_\Gamma\le1\) and \(\|p-p_1\|_\Gamma\le Mb\), so
\[
 \|p-q\|_K<2a+2Mb.
\]
Choose \(a<\varepsilon/4\), then \(b<\varepsilon/(4M)\). This proves (6), including its global bound. \(\square\)

## 3. Returning Haar measure and Plancherel to the original group

<a id="ha-lca-09-proposition-3-1"></a>
**Proposition 3.1 — Double transformation.** Let \(d\nu\) be the Haar measure on \(D=\widehat\Gamma\) dual to \(d\xi\). Then
\[
 \nu=(J_G)_*(dx).
 \tag{7}
\]
With this identification, the two Plancherel transforms satisfy
\[
 (\mathcal F_\Gamma\mathcal F_G f)(J_Gx)=f(-x)
 \quad\text{as }L^2\text{ classes}.
 \tag{8}
\]

**Proof.** The homeomorphism \(J_G\) carries \(dx\), including its complete locally determined domain, to a Haar measure on \(D\). Indeed translations, compact sets and Borel sets correspond, and the compact-local description of the completion in the general Haar reading, Theorem 3.1, is preserved. Haar uniqueness, Theorem 3.3 of that reading, gives \(\nu=c(J_G)_*dx\) for some \(c>0\).

Take \(f\in B^1(G)\). Its transform is integrable by HA-LCA-07, Theorem 2.1. It is also in \(B(\Gamma)\): the finite Radon measure
\((J_G\circ(-\mathrm{id}))_*(f\,dx)\) has \(T\)-transform on \(\Gamma\) equal to \(\widehat f\). The pushforward is finite Radon by [the product reading, Proposition 3.1](../prerequisites/src/finite-radon-products.md#ha-lca-pre-product-proposition-3-1). Hence \(\widehat f\in B^1(\Gamma)\). Inversion on \(G\) gives, at every \(x\),
\[
 \widehat{\widehat f}(J_Gx)
 =\int_\Gamma\widehat f(\gamma)\overline{\gamma(x)}\,d\xi(\gamma)
 =f(-x).
 \tag{9}
\]
Apply \(B^1\) inversion on \(\Gamma\) at its identity character \(1\):
\[
 \widehat f(1)=\int_D\widehat{\widehat f}(\chi)\,d\nu(\chi)
             =c\int_G f(-x)\,dx=c\int_G f(x)\,dx.
\]
The left side is \(\int_G f\). There exists such an \(f\) with nonzero integral: choose a nonzero nonnegative \(u\in C_c(G)\) and take \(f=u*\widetilde u\). It is in \(C_c(G)\cap P(G)\subset B^1(G)\), and the convolution integral formula gives \(\int f=(\int u)^2>0\). The convolution formula and Fubini here are those already proved in the general Haar reading, Theorem 6.1, by reduction to an open sigma-compact subgroup. It follows that \(c=1\), proving (7).

For \(f\in C_c(G)\cap P(G)\), both \(f\) and \(\widehat f\) are in the appropriate \(L^1\cap L^2\): \(f\) is bounded with compact support, \(\widehat f\in L^1\) by inversion and \(\widehat f\in L^2\) by Plancherel. Thus (9) agrees with both Plancherel transforms. The linear span of these \(f\)'s is dense in \(L^2(G)\) by [HA-LCA-05, Proposition 3.1](raikovs-theorem-and-the-gelfand-raikov-theorem.md#ha-lca-05-proposition-3-1). Both transforms are unitary, as is reflection by Haar-preserving inversion. Taking \(L^2\) limits proves (8). \(\square\)

## 4. General inversion and uniqueness

For a finite complex Radon measure \(\mu\) on \(G\), write
\(\widehat\mu(\gamma)=\int_G\overline{\gamma(x)}\,d\mu(x)\).
We now identify \(D\) with \(G\) by \(J_G\) when doing integrals, using (7).

<a id="ha-lca-09-theorem-4-1"></a>
**Theorem 4.1 — Fourier inversion for integrable transforms.** If \(f\in L^1(G)\) and \(\widehat f\in L^1(\Gamma)\), then
\[
 u(x)=\int_\Gamma \widehat f(\gamma)\gamma(x)\,d\xi(\gamma)
 \tag{10}
\]
is in \(C_0(G)\cap L^1(G)\) and equals \(f\) almost everywhere. If \(f\) has a continuous representative, (10) equals that representative everywhere.

**Proof.** We first prove the uniqueness fact needed in this argument, for all finite complex Radon measures. Given \(\mu\in M(G)\), put
\(\rho=(J_G\circ(-\mathrm{id}))_*\mu\in M(D)\). Then
\[
 T_\Gamma\rho(\gamma)
 =\int_G J_G(-x)(\gamma)\,d\mu(x)
 =\widehat\mu(\gamma).
 \tag{11}
\]
If \(\widehat\mu=0\), injectivity of \(T\) applied to the base group \(\Gamma\) gives \(\rho=0\). The map \(J_G\circ(-\mathrm{id})\) is a homeomorphism, so its inverse pushforward gives \(\mu=0\). Thus the Fourier transform separates finite measures on \(G\).

Now let \(q=\widehat f\). Formula (11) with \(\mu=f\,dx\) shows that \(q\in B(\Gamma)\), and the hypothesis gives \(q\in B^1(\Gamma)\). By HA-LCA-07, Theorem 2.1, its transform \(v=\widehat q\) is in \(L^1(D)\), and
\[
 q(\gamma)=\int_D v(\chi)\chi(\gamma)\,d\nu(\chi).
 \tag{12}
\]
The general \(L^1\) transform theorem [HA-LCA-03, Corollary 2.2](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-corollary-2-2) also gives \(v\in C_0(D)\). Define \(u(x)=v(J_G(-x))\). This is exactly (10), and (7) implies \(u\in L^1(G)\cap C_0(G)\). In (12) substitute \(\chi=J_Gx\), then replace \(x\) by \(-x\). Haar inversion gives
\[
 q(\gamma)=\int_Gu(-x)\gamma(x)\,dx
           =\int_Gu(x)\overline{\gamma(x)}\,dx=\widehat u(\gamma).
\]
Therefore \((f-u)\,dx\) has zero Fourier transform. The uniqueness just proved gives \((f-u)\,dx=0\), and the density/variation identity of HA-LCA-03, Lemma 4.1, gives \(f=u\) almost everywhere. If a continuous representative differed from \(u\) at any point, their continuous difference would have modulus bounded below by a positive constant on a nonempty open set. Haar full support makes that set have positive measure, a contradiction. \(\square\)

<a id="ha-lca-09-corollary-4-2"></a>
**Corollary 4.2 — Uniqueness and semisimplicity.** If \(\mu\in M(G)\) has \(\widehat\mu=0\), then \(\mu=0\). In particular the Fourier transform is injective on \(L^1(G)\). Both commutative Banach algebras \(L^1(G)\) and \(M(G)\) are semisimple.

**Proof.** Theorem 4.1 proved finite-measure uniqueness in (11), without an integrability assumption on \(\widehat\mu\). Its application to \(f\,dx\) proves \(L^1\) uniqueness.

For completeness, semisimplicity means that the Jacobson radical is zero. For a commutative unital Banach algebra its radical is the intersection of its maximal ideals. The [Banach reading, Theorem 3.3](../prerequisites/src/banach-spectrum.md#ha-lca-pre-banach-theorem-3-3), proves that these ideals are exactly character kernels. For a possibly nonunital algebra \(A\), take the intersection with \(A\) of the radical of its unitization. [Theorem 3.4 of that reading](../prerequisites/src/banach-spectrum.md#ha-lca-pre-banach-theorem-3-4) shows that characters of the unitization either extend a character of \(A\) or vanish on \(A\). Thus in either case the radical equals the intersection of character kernels on \(A\).

The maps \(f\mapsto\widehat f(\gamma)\) are characters on \(L^1(G)\), by [HA-LCA-03, Lemma 1.2](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-lemma-1-2). They separate its elements by uniqueness. For \(M(G)\), the maps \(\mu\mapsto\widehat\mu(\gamma)\) are linear and multiplicative, since the character identity and the finite Radon product formula give
\[
 \widehat{\mu*\eta}(\gamma)
 =\int_{G\times G}\overline{\gamma(x+y)}\,d(\mu\otimes\eta)(x,y)
 =\widehat\mu(\gamma)\widehat\eta(\gamma).
\]
The product and its full-Borel integration were proved in [the product reading, Theorems 2.1 and 3.3](../prerequisites/src/finite-radon-products.md#ha-lca-pre-product-theorem-3-3). These functionals are nonzero because their value on \(\delta_0\) is one. They too separate points by uniqueness. The intersection of all character kernels, being contained in the intersection of these kernels, is zero. This proves semisimplicity of both algebras; it does not assert that these are all the characters of \(M(G)\). \(\square\)

<a id="ha-lca-09-corollary-4-3"></a>
**Corollary 4.3 — An integrable measure transform gives a density.** If \(\mu\in M(G)\) and \(\widehat\mu\in L^1(\Gamma)\), then
\[
 \mu=u\,dx,\qquad
 u(x)=\int_\Gamma\widehat\mu(\gamma)\gamma(x)\,d\xi(\gamma)
       \in C_0(G)\cap L^1(G).
 \tag{13}
\]

**Proof.** Formula (11) says that \(q=\widehat\mu\in B(\Gamma)\). By hypothesis it is in \(B^1(\Gamma)\). Repeat the inversion step (12): \(v=\widehat q\in L^1(D)\cap C_0(D)\), and \(u(x)=v(J_G(-x))\) is in \(L^1(G)\cap C_0(G)\), has the formula (13), and satisfies \(\widehat u=q\). The finite measure \(\mu-u\,dx\) therefore has zero transform. Corollary 4.2 gives \(\mu=u\,dx\). \(\square\)

<a id="ha-lca-09-corollary-4-4"></a>
**Corollary 4.4 — Compact and discrete groups.** For every LCA group,
\[
 G\text{ compact}\ \Longleftrightarrow\ \widehat G\text{ discrete},
 \qquad
 G\text{ discrete}\ \Longleftrightarrow\ \widehat G\text{ compact}.
 \tag{14}
\]

**Proof.** The forward implications are [HA-LCA-02, Theorem 2.1](characters-and-the-dual-group.md#ha-lca-02-theorem-2-1). If \(\widehat G\) is discrete, that theorem makes \(D\) compact; if \(\widehat G\) is compact, it makes \(D\) discrete. Theorem 2.1 identifies \(G\) homeomorphically with \(D\), proving both converses. \(\square\)

## 5. Maps, naturality and examples

<a id="ha-lca-09-proposition-5-1"></a>
**Proposition 5.1 — The duality functor.** If \(p:G\to H\) is a continuous homomorphism of LCA groups, then
\[
 \widehat p:\widehat H\longrightarrow\widehat G,\qquad
 \widehat p(\eta)=\eta\circ p
 \tag{15}
\]
is a continuous homomorphism. Duality reverses composition and preserves identity maps. Evaluation satisfies
\[
 \widehat{\widehat p}\circ J_G=J_H\circ p.
 \tag{16}
\]
Consequently duality is a contravariant equivalence of the category of LCA groups with itself.

**Proof.** Composition with \(p\) preserves the character identity and continuity. Multiplying characters pointwise shows that \(\widehat p\) is a homomorphism. For each compact \(C\subseteq G\), its image \(p(C)\) is compact, and
\[
 \sup_{x\in C}|(\eta\circ p)(x)-(\zeta\circ p)(x)|
 =\sup_{y\in p(C)}|\eta(y)-\zeta(y)|.
\]
Thus a compact-open condition on \(\widehat p(\eta)\) is a compact-open condition on \(\eta\), proving continuity. If \(r:H\to K\), direct composition gives
\(\widehat{r\circ p}=\widehat p\circ\widehat r\); the identity formula is immediate. For \(x\in G\) and \(\eta\in\widehat H\),
\[
 \bigl(\widehat{\widehat p}(J_Gx)\bigr)(\eta)
 =J_Gx(\widehat p(\eta))
 =\eta(p(x))=(J_Hp(x))(\eta),
\]
which proves (16).

Here is an explicit verification of equivalence. Given any continuous homomorphism \(q:\widehat H\to\widehat G\), define
\(p=J_H^{-1}\circ\widehat q\circ J_G:G\to H\).
It is continuous, and for every \(x,\eta\),
\[
 (\widehat p(\eta))(x)
 =J_H(p(x))(\eta)
 =(\widehat q(J_Gx))(\eta)
 =(q(\eta))(x).
\]
Hence \(\widehat p=q\). If two maps have the same dual, all characters of \(H\) agree on their values, so character separation gives equality of the maps. Thus duality gives a bijection on each reversed homomorphism set. Finally every \(H\) is isomorphic to \(\widehat{\widehat H}\) by Theorem 2.1, so every object is isomorphic to an object in the image of duality. These are precisely full faithfulness and essential surjectivity. \(\square\)

<a id="ha-lca-09-example-5-2"></a>
**Example 5.2 — The familiar double duals.** With characters \(x\mapsto e^{2\pi itx}\) on \(\mathbb R\), evaluation identifies the double dual with the original real coordinate. Evaluation likewise gives the usual double-dual identifications of \(\mathbb Z\), \(\mathbb T\) and finite abelian groups.

**Proof.** [HA-LCA-02, Theorem 3.1 and Corollary 3.2](characters-and-the-dual-group.md#ha-lca-02-theorem-3-1) prove the topological identifications \(\widehat{\mathbb R}=\mathbb R\), \(\widehat{\mathbb Z}=\mathbb T\), and \(\widehat{\mathbb T}=\mathbb Z\). Under the first, \(J_{\mathbb R}(x)\) is the character \(t\mapsto e^{2\pi itx}\), whose parameter is \(x\). On \(\mathbb Z\), the character with parameter \(z\in\mathbb T\) sends \(n\) to \(z^n\); hence \(J_{\mathbb Z}(n)\) is precisely \(z\mapsto z^n\), with integer parameter \(n\). Similarly \(J_{\mathbb T}(z)\) sends \(n\) to \(z^n\), recovering \(z\).

For finite abelian \(F\), [HA-LCA-01, Theorem 1.3](fourier-analysis-on-finite-abelian-groups.md#ha-lca-01-theorem-1-3) already proves the evaluation bijection. Both groups are discrete, so it is a homeomorphism. On a cyclic factor \(\mathbb Z/N\mathbb Z\), the formula is \(J(a)(k)=e^{2\pi iak/N}\); products give the same coordinatewise formula for every finite abelian group. Theorem 2.1 extends these calculations to all LCA groups. \(\square\)

<a id="ha-lca-09-example-5-3"></a>
**Example 5.3 — The dual of the integer inclusion.** For \(i:\mathbb Z\hookrightarrow\mathbb R\), the dual map, in the preceding coordinates, is
\[
 \widehat i:\mathbb R\longrightarrow\mathbb T,\qquad t\longmapsto e^{2\pi it}.
 \tag{17}
\]
It is an open surjection with kernel \(\mathbb Z\).

**Proof.** Restricting \(x\mapsto e^{2\pi itx}\) to the integers gives \(n\mapsto(e^{2\pi it})^n\), so (17) follows. Surjectivity and the stated kernel are proved in [HA-LCA-02, Lemma 1.3](characters-and-the-dual-group.md#ha-lca-02-lemma-1-3). To check openness directly, fix an open \(U\subseteq\mathbb R\) and \(t\in U\). Choose \(0<a<1/2\) with \([t-a,t+a]\subseteq U\). The image of the compact interval \([t+a,t+1-a]\) is closed in \(\mathbb T\) and does not contain \(e^{2\pi it}\), by the kernel calculation. Its complement is an open neighbourhood of that point. Every circle point has a representative in \([t-a,t+1-a]\), so this complement is contained in the image of \((t-a,t+a)\), hence in the image of \(U\). This proves openness. \(\square\)

<a id="ha-lca-09-example-5-4"></a>
**Example 5.4 — The dual of the discrete rational group.** Give \(\mathbb Q\) the discrete topology. Its dual is the compact group
\[
 \Sigma=\{(z_n)_{n\ge1}\in\mathbb T^{\mathbb N}:
                  z_n=z_{n+1}^{\,n+1}\text{ for every }n\ge1\},
 \tag{18}
\]
called the universal solenoid. The identification is
\(\chi\mapsto(\chi(1/n!))_{n\ge1}\), and \(\widehat\Sigma\cong\mathbb Q_d\).

**Proof.** The displayed coordinates obey (18) because \(1/n!=(n+1)/(n+1)!\). Conversely, for a compatible family define
\[
 \chi(k/n!)=z_n^k.
 \tag{19}
\]
Every rational has this form. If \(m\ge n\), compatibility gives \(z_n=z_m^{m!/n!}\), so the value in (19) agrees with the denominator \(m!\). Two representations have a common factorial denominator and therefore give the same value. Addition after passage to such a denominator proves the character identity. Continuity is automatic on \(\mathbb Q_d\).

Compact subsets of a discrete space are finite: the singleton cover of a compact set has a finite subcover. Thus the compact-open topology on \(\widehat{\mathbb Q_d}\) is the topology of finitely many evaluations. Each coordinate in (18) is an evaluation, and the evaluation at any rational is a power of one coordinate by (19). Consequently the bijection and its inverse are continuous. The dual of a discrete group is compact by HA-LCA-02, Theorem 2.1; equivalently, using the arbitrary product theorem of [the Banach reading, Lemma 4.1](../prerequisites/src/banach-spectrum.md#ha-lca-pre-banach-lemma-4-1), (18) is a closed subgroup of the compact product \(\mathbb T^{\mathbb N}\), since its defining equations are closed. Finally Theorem 2.1 and Proposition 5.1 identify its dual with \(\mathbb Q_d\). Connectedness will follow from the fully proved criterion in Exercise 6.5. \(\square\)

## 6. Quotients and exercises

<a id="ha-lca-09-lemma-6-0"></a>
**Lemma 6.0 — The quotient group needed below.** If \(K\) is a closed subgroup of an LCA group \(H\), the quotient \(H/K\), with its quotient topology, is LCA. The map \(q:H\to H/K\) is open. A continuous character on \(H\) trivial on \(K\) descends to a unique continuous character on \(H/K\).

**Proof.** For every open \(U\subseteq H\),
\(q^{-1}(q(U))=U+K=\bigcup_{k\in K}(U+k)\) is open. The quotient-topology definition therefore says that \(q(U)\) is open. If \(q(a)\ne q(b)\), then \(a-b\notin K\). Since \(K\) is closed, group continuity gives an identity neighbourhood \(W\) with
\(a-b+W-W\subseteq H\setminus K\).
The open sets \(q(a+W)\) and \(q(b+W)\) are disjoint, since an intersection would put \(a-b+w_1-w_2\) in \(K\). They separate the two quotient points, proving the Hausdorff property.

The product map \(q\times q\) is an open surjection: images of open rectangles are open rectangles, and every product-open set is a union of rectangles. An open surjection is a quotient map, since if its full inverse image of a set is open, that set is the open image of its inverse image. The quotient addition is continuous because its composite with \(q\times q\) is the continuous map \((a,b)\mapsto q(a+b)\); the quotient property turns continuity of that composite into continuity of addition. Inversion is continuous by the same argument with \(q\). The group is abelian.

Choose a compact identity neighbourhood \(C\subseteq H\). Its image \(q(C)\) is compact and contains the open identity neighbourhood \(q(\operatorname{int}C)\). Translates give local compactness everywhere. Finally a character \(\chi\) trivial on \(K\) has the unique factor \(\bar\chi(q(h))=\chi(h)\), well-defined by the kernel condition. It is a homomorphism; for open \(O\subseteq\mathbb T\), \(q^{-1}(\bar\chi^{-1}(O))=\chi^{-1}(O)\) is open. The quotient topology proves continuity. \(\square\)

<a id="ha-lca-09-exercise-6-1"></a>
**Exercise 6.1 — Evaluation and point separation.** Verify directly that \(J_G\) is a homomorphism and injective. Identify exactly where character separation enters.

**Solution.** For every \(\gamma\in\Gamma\),
\[
 J_G(x+y)(\gamma)=\gamma(x+y)
                 =\gamma(x)\gamma(y)
                 =(J_G(x)J_G(y))(\gamma).
\]
Thus \(J_G(x+y)=J_G(x)J_G(y)\). If \(J_G(x)=J_G(y)\), every character takes value one at \(x-y\). [HA-LCA-05, Corollary 4.2](raikovs-theorem-and-the-gelfand-raikov-theorem.md#ha-lca-05-corollary-4-2), proved from Gelfand–Raikov, supplies a character with value different from one at every nonzero element. Therefore \(x-y=0\). Injectivity uses that theorem; it is not a formal consequence of the definition of the dual. \(\square\)

<a id="ha-lca-09-exercise-6-2"></a>
**Exercise 6.2 — A net proof of subgroup closedness.** Prove Lemma 1.2 by considering a net in \(H\) that converges in \(P\).

**Solution.** Choose \(K,V\) as in Lemma 1.2. Suppose \(h_i\in H\) converges in \(P\) to \(x\). Pick an ambient identity neighbourhood \(W\) with \(W^{-1}W\subseteq V\). Eventually all \(h_i\) lie in \(xW\). Fix one such index \(j\). For every sufficiently late \(i\),
\[
 h_j^{-1}h_i\in W^{-1}W\cap H\subseteq V\cap H\subseteq K.
\]
The tail of the net therefore lies in \(h_jK\). This set is compact and hence closed in the Hausdorff space \(P\), by the compact-closed argument in Lemma 1.2. Its limit \(x\) belongs to \(h_jK\subseteq H\).

This proves closedness because each point \(x\in\overline H\) is the limit of a net in \(H\): direct the neighbourhoods of \(x\) by reverse inclusion and choose one point of \(H\) in each. The resulting net converges to \(x\) by the definition of convergence. No first-countability assumption is involved. \(\square\)

<a id="ha-lca-09-exercise-6-3"></a>
**Exercise 6.3 — Dense image.** A continuous homomorphism \(p:G\to H\) has dense image if and only if \(\widehat p\) is injective.

**Solution.** If \(p(G)\) is dense and \(\eta\in\ker\widehat p\), the continuous character \(\eta\) equals one on a dense set. The set \(\eta^{-1}(\{1\})\) is closed, so it is all of \(H\). Thus the kernel is trivial, which is equivalent to injectivity for a homomorphism.

Conversely let \(K=\overline{p(G)}\). It is a closed subgroup, by the group-continuity argument in Lemma 1.2. If \(K\ne H\), Lemma 6.0 makes \(H/K\) a nontrivial LCA group. Choose a nonzero coset \(q(h)\). Character separation, HA-LCA-05, Corollary 4.2, gives a character \(\zeta\) of \(H/K\) with \(\zeta(q(h))\ne1\). Then \(\eta=\zeta\circ q\) is a nontrivial continuous character of \(H\) trivial on \(K\), and hence on \(p(G)\). Thus \(\widehat p(\eta)=1\), contradicting injectivity. Therefore \(K=H\). \(\square\)

<a id="ha-lca-09-exercise-6-4"></a>
**Exercise 6.4 — Open surjections.** If \(p:G\to H\) is a continuous, open, surjective homomorphism, show that its dual is injective and has the closed image
\[
 \widehat p(\widehat H)
 =(\ker p)^\perp
 :=\{\gamma\in\widehat G:\gamma(k)=1\text{ for every }k\in\ker p\}.
 \tag{20}
\]

**Solution.** Surjectivity implies injectivity of the dual: two characters agreeing after composition with \(p\) agree everywhere on \(H\). Every character in its image is trivial on \(\ker p\). Conversely, if \(\gamma\) is trivial on \(\ker p\), the formula \(\eta(p(x))=\gamma(x)\) is well-defined and multiplicative. For open \(O\subseteq\mathbb T\),
\(\eta^{-1}(O)=p(\gamma^{-1}(O))\) is open, so \(\eta\) is continuous. Thus \(\gamma=\widehat p(\eta)\).

For each \(k\in G\), evaluation \(\gamma\mapsto\gamma(k)\) is continuous in the compact-open topology, since the singleton \(\{k\}\) is compact. Its inverse image of \(\{1\}\) is closed. Intersecting these closed sets over all \(k\in\ker p\) proves that the image in (20) is closed. \(\square\)

<a id="ha-lca-09-exercise-6-5"></a>
**Exercise 6.5 — Connected compact groups.** Prove that a compact abelian group \(G\) is connected if and only if \(\widehat G\) is torsion-free. Include a proof that the identity component of \(G\) is the intersection of its open subgroups. Deduce that the universal solenoid is connected.

**Solution.** We first supply the compact-space fact used in the group argument. A space is connected if it cannot be written as the union of two disjoint nonempty relatively open sets. A set is clopen if it is both open and closed. For a compact Hausdorff space \(X\) and \(x\in X\), let \(Q_x\) be the intersection of all clopen neighbourhoods of \(x\). It is closed and compact and contains \(x\).

We claim that \(Q_x\) is connected. Otherwise write it as the disjoint union of two nonempty relatively clopen sets \(A,B\), with \(x\in A\). Both are compact, hence closed in \(X\). The compact Hausdorff separation theorem proved in [the Radon reading, Lemma 1.1](../prerequisites/src/finite-radon-representation.md#ha-lca-pre-radon-lemma-1-1) gives disjoint open \(U,V\subseteq X\) with \(A\subseteq U\), \(B\subseteq V\). The compact set \(F=X\setminus(U\cup V)\) is disjoint from \(Q_x\). For each \(y\in F\), some clopen neighbourhood \(C_y\) of \(x\) excludes \(y\), by the definition of \(Q_x\). The sets \(X\setminus C_y\) cover \(F\). A finite subcover gives a finite intersection \(C\) of the corresponding \(C_y\)'s with
\[
 Q_x\subseteq C\subseteq U\cup V.
\]
If \(F=\varnothing\), take \(C=X\). The set \(C\cap U\) is open, and its complement is the open set \((X\setminus C)\cup(C\cap V)\). It is therefore a clopen neighbourhood of \(x\) excluding \(B\). This contradicts \(B\subseteq Q_x\). Hence \(Q_x\) is connected.

Every connected subset of \(X\) containing \(x\) lies in each clopen neighbourhood of \(x\): otherwise that neighbourhood and its complement would separate the subset. Thus every such connected subset lies in \(Q_x\). As \(Q_x\) is itself connected, it is exactly the connected component of \(x\).

Now let \(X=G\) be a compact group and let \(U\) be a clopen identity neighbourhood. The function \(1_U\) is continuous with compact support. Uniform translation continuity, proved in [the general Haar reading, Lemma 1.1](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-lemma-1-1), gives an identity neighbourhood \(V\) on which
\[
 \|L_v1_U-1_U\|_\infty<1.
\]
Both functions take only the values zero and one, so they are equal. Therefore \(vU=U\). The stabilizer
\(H_U=\{g:gU=U\}\) is a subgroup: the identity preserves \(U\), compositions of preserving translations preserve it, and the inverse of a preserving translation also preserves it. It contains \(V\), so it is open. Since \(0\in U\), every \(g\in H_U\) belongs to \(gU=U\), hence \(H_U\subseteq U\).

Every open subgroup is closed, because its other cosets are open. It has finite index in a compact group: its cosets form an open cover, a finite subcover contains every coset, and distinct cosets are disjoint. Let \(G_0\) be the identity component. The compact-space argument identifies \(G_0\) with the intersection of all clopen identity neighbourhoods. Every open subgroup is one of these neighbourhoods, and each such neighbourhood contains an open subgroup \(H_U\). Consequently
\[
 G_0=\bigcap_{\substack{H\le G\\ H\ \mathrm{open}}}H.
 \tag{21}
\]
This also proves, without any separate assumption about components, that \(G_0\) is a closed subgroup.

Suppose \(G\) is connected and \(\gamma^N=1\) for a character \(\gamma\) and integer \(N\ge1\). Its image lies among the finitely many \(N\)-th roots of unity, whose description was proved in [HA-LCA-02, Lemma 1.3](characters-and-the-dual-group.md#ha-lca-02-lemma-1-3). A finite subset of a Hausdorff space is discrete in its relative topology: intersect finitely many separating neighbourhoods to isolate each point. A continuous image of a connected space is connected, since a separation of the image would pull back to a separation of the space. Thus \(\gamma(G)\), being both connected and finite discrete, is a singleton. It contains one, so \(\gamma=1\). The dual is torsion-free.

Conversely suppose \(G\) is disconnected. Then \(G_0\ne G\). Formula (21) gives a proper open subgroup \(H\). Since \(G\) is abelian, Lemma 6.0 gives the quotient group \(G/H\); it is finite by the preceding compact-cover argument and discrete because \(H\) is open. By [HA-LCA-01, Theorem 1.1](fourier-analysis-on-finite-abelian-groups.md#ha-lca-01-theorem-1-1), its characters separate points. Choose a nontrivial character \(\zeta\). If \(m=|G/H|\), every quotient element has order dividing \(m\), by the coset-counting proof in [HA-LCA-01, Lemma 0.0](fourier-analysis-on-finite-abelian-groups.md#ha-lca-01-lemma-0-0). Hence \(\zeta^m=1\). Its pullback to \(G\) is a nontrivial finite-order continuous character, so the dual is not torsion-free. This proves the equivalence.

Finally Example 5.4 gives \(\widehat\Sigma\cong\mathbb Q_d\), and the additive rational group is torsion-free: \(nq=0\), for nonzero integer \(n\), forces \(q=0\). The compact group \(\Sigma\) is therefore connected. \(\square\)

## What has been established

Evaluation is a topological isomorphism for every LCA group. The bidual Haar measure is the original Haar measure, and two Plancherel transforms give reflection. Integrable transforms have pointwise inverse integrals representing their original \(L^1\) classes or finite-measure densities. Fourier transforms separate finite measures, and the two convolution algebras considered here are semisimple.

All five exercises have complete solutions, including the compact-component fact required for the torsion-free criterion. The next lesson develops restriction of characters, annihilators and the full subgroup–quotient duality correspondence.
