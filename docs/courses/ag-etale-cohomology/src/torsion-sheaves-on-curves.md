# Torsion sheaves on curves

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Links and citations revised by Claude Opus 5.5 (Anthropic), October 2026. Original text released under CC0.*

A local system on a curve may have complicated monodromy. Nevertheless, its torsion cohomology has a uniform degree bound, and finite coefficients usually give finite groups. We prove these assertions by reducing the monodromy to constant pieces while controlling the boundary. In characteristic \(p\), the map \(a\mapsto a^p-a\) supplies the missing constant-coefficient calculation. It also explains exactly why affine \(p\)-torsion cohomology can be infinite and change when the ground field grows.

The prerequisites are [The multiplicative group on a curve](the-multiplicative-group-on-a-curve.md), [Constructible sheaves and extension by zero](constructible-sheaves-and-extension-by-zero.md), and [Galois cohomology and the étale cohomology of a field](galois-cohomology-and-the-etale-cohomology-of-a-field.md). We also use the proved quasi-coherent comparison of [Topologies on schemes](topologies-on-schemes.md), the finite direct images and topological invariance of [Pushforward, pullback and finite morphisms](pushforward-pullback-and-finite-morphisms.md), and the filtered-cohomology lemma in section 3 of lesson 10. The geometric inputs are stated precisely in section 2. No proper base-change theorem for general morphisms is used here.

## 1. The assertions and their coefficient conventions

Unless stated otherwise, \(k\) is algebraically closed and \(X\) is separated, of finite type over \(k\), with \(\dim X\leq1\). Put \(p=1\) in characteristic zero and \(p=\operatorname{char}k\) otherwise. A torsion sheaf is **prime to \(p\)** if each germ has order relatively prime to \(p\). It need not have a common annihilator. A constructible abelian sheaf has finite underlying stalks on finitely many locally constant pieces, as in lesson 11; it does have a common annihilator.

**Theorem 1.1.** For a torsion abelian sheaf \(\mathcal F\) on \(X_{\mathrm{ét}}\):

1. \(H^q(X,\mathcal F)=0\) for \(q>2\).
2. If \(X\) is affine, then \(H^q(X,\mathcal F)=0\) for \(q>1\).
3. If \(p>1\) and \(\mathcal F\) is \(p\)-power torsion, then \(H^q(X,\mathcal F)=0\) for \(q>1\), including when \(X\) is proper.
4. If \(\mathcal F\) is constructible and prime to \(p\), all \(H^q(X,\mathcal F)\) are finite.
5. If \(X\) is proper and \(\mathcal F\) is constructible, all \(H^q(X,\mathcal F)\) are finite, including the \(p\)-part.
6. For an extension \(k'/k\) of algebraically closed fields and prime-to-\(p\) torsion \(\mathcal F\), the canonical pullback map

\[
H^q(X,\mathcal F)\longrightarrow
H^q(X_{k'},\mathcal F|_{X_{k'}})
\tag{1.1}
\]

is an isomorphism for every \(q\geq0\).

We prove also that (1.1) is an isomorphism for **all** torsion sheaves when \(X\) is proper. Section 9 then proves the proper statement for extensions of separably closed fields. Finiteness means finite groups in Theorem 1.1; the module theorem in section 10 instead means finitely generated modules over a specified Noetherian ring.

## 2. Geometric inputs and finite boundaries

We use these scheme-theoretic foundations, with the indicated scope:

- A smooth connected finite-type curve over an algebraically closed field has a smooth projective completion. It is either projective or affine, and every proper nonempty open of a smooth projective curve is affine. These are the curve-completion facts used in lesson 10, [Stacks, Tags 0A27 and 0H1F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-curve-affine-projective).
- Normalization of a reduced finite-type scheme over a field is finite and birational. For a curve over the perfect field \(k\), its positive-dimensional normal components are smooth; its zero-dimensional components are points. See [Tags 0BXR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-normalization-locally-algebraic) and [0B8Y](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-regular-point-on-curve). Thus normalization preserves affineness, and preserves properness when the original scheme is proper.
- Zariski's Main Theorem factors a separated quasi-finite map to a qcqs scheme as a quasi-compact open immersion followed by a finite morphism, [Zariski's Main Theorem](course:AG-MO/AG-MO-12), Theorem 4.2 (also [Tag 05K0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-quasi-finite-separated-pass-through-finite)). We use it to extend a finite étale cover of a dense open, not as a cohomological finiteness assertion.
- Coherent cohomology on a proper scheme over a field is finite dimensional, [Tags 02O5–02O6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-proper-over-affine-cohomology-finite). The Picard scheme of a smooth projective curve represents the line-bundle functor, with degree-zero part its Jacobian, [Tags 0B9Z](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pic.html#pic-proposition-pic-curve) and [0BA0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pic.html#pic-lemma-picard-pieces). These are classical geometric prerequisites. We will prove the required flat field-extension calculation directly using affine Čech complexes.

Here are consequences that will enter the reduction. A proper closed subset of an irreducible finite-type curve is a finite set of closed points. Over \(k\) each residue field is \(k\). For a reduced scheme with finitely many components, remove their pairwise intersections and the finitely many nonsmooth points of the one-dimensional components. This leaves a dense open which is a disjoint union of smooth irreducible curves and isolated points. Intersecting with the locally constant strata of a constructible sheaf and removing the remaining proper closed subsets makes that sheaf locally constant on this open. Every deletion is finite.

For a dense open \(j:U\to X\) and its complementary reduced closed subscheme \(i:Z\to X\), lesson 11 gives

\[
0\longrightarrow j_!j^{-1}\mathcal F\longrightarrow\mathcal F
\longrightarrow i_*i^{-1}\mathcal F\longrightarrow0.
\tag{2.1}
\]

The closed immersion is finite. Exact finite direct image and field-topos comparison give

\[
H^q(X,i_*i^{-1}\mathcal F)=
\begin{cases}
\displaystyle\bigoplus_{z\in Z}\mathcal F_{\bar z},&q=0,\\
0,&q>0.
\end{cases}
\tag{2.2}
\]

In particular the boundary group is finite for constructible \(\mathcal F\). After an algebraically closed extension, the same points and the same stalk groups occur; pullback on (2.2) is their identity. Nilpotents are harmless by topological invariance, so (2.2) holds for any finite zero-dimensional boundary with these underlying points.

## 3. Artin–Schreier and a semilinear calculation

In characteristic \(p>0\), there is a short exact sequence on the small étale site of any scheme \(S\):

\[
0\longrightarrow\underline{\mathbf F_p}
\longrightarrow\mathcal O_S
\xrightarrow{F-1}\mathcal O_S\longrightarrow0,
\qquad (F-1)(a)=a^p-a.
\tag{3.1}
\]

The kernel consists of locally constant choices among the distinct roots in \(\mathbf F_p\): the factors of \(T^p-T\) are pairwise coprime, so a root in any algebra yields the corresponding idempotent partition. For surjectivity, a section \(a\) over an étale object is lifted on the cover defined by \(T^p-T-a\). This algebra is free of rank \(p\), and its derivative is \(-1\), so the cover is finite étale and surjective. This proves sheaf surjectivity, including on schemes with nilpotents.

Quasi-coherent comparison from lesson 5 identifies \(H^q_{\mathrm{ét}}(S,\mathcal O_S)\) with ordinary coherent cohomology. On an affine scheme these groups vanish for \(q>0\). Thus (3.1) immediately gives

\[
H^q(S,\mathbf F_p)=0\quad(q\geq2),\qquad
H^1(S,\mathbf F_p)=
\Gamma(S,\mathcal O_S)/(a^p-a).
\tag{3.2}
\]

For proper curves we need more than affine vanishing.

**Lemma 3.1.** Let \(V\) be a finite-dimensional vector space over an algebraically closed field of characteristic \(p\), and let \(F\) be additive with \(F(av)=a^pF(v)\). Then \(F-1\) is surjective. Its fixed vectors form a finite \(\mathbf F_p\)-vector space of dimension at most \(\dim_k V\). Under an algebraically closed extension \(k'/k\), the map

\[
\ker(F-1)\longrightarrow
\ker(F'-1:V\otimes_k k'\to V\otimes_k k')
\tag{3.3}
\]

is an isomorphism, where \(F'(v\otimes a)=F(v)\otimes a^p\).

**Proof.** Because \(k\) is perfect, every image \(F^n(V)\) is a \(k\)-subspace. Their dimensions eventually stabilize. Choose \(N\) with \(W=F^N(V)=F^{N+1}(V)\). On \(W\), \(F\) is bijective; on \(V/W\) it is nilpotent. If \(F^N=0\), the additive inverse of \(F-1\) is \(-\sum_{i=0}^{N-1}F^i\); in particular the nilpotent quotient has no nonzero fixed vector.

It remains to treat the bijective part. In a basis write \(F(x)=Ax^{[p]}\), where \(A\) is invertible and \(x^{[p]}\) means coordinatewise \(p\)-th powers. The equation \(F(x)-x=y\) is equivalent to

\[
x_i^p-\sum_j(A^{-1})_{ij}x_j=(A^{-1}y)_i,
\qquad 1\leq i\leq r=\dim W.
\tag{3.4}
\]

The quotient algebra for these equations has basis the monomials \(x_1^{e_1}\cdots x_r^{e_r}\), \(0\leq e_i<p\). Here is the independence check as well as spanning. Use a degree-compatible monomial order. Each defining polynomial has leading monomial \(x_i^p\). The leading monomials for two different equations are relatively prime; their S-polynomial reduces to zero by replacing \(x_i^p\) and \(x_j^p\) with their prescribed linear polynomials, after which the two products cancel. Hence the equations form a Gröbner basis and the displayed standard monomials are a basis. The algebra has dimension \(p^r\), and the Jacobian matrix is \(-A^{-1}\), so it is finite étale over \(k\). It therefore has exactly \(p^r\) \(k\)-points. Every \(y\) has a solution and the fixed group has \(p^r\) elements.

For the original \(V\), first solve the equation in its nilpotent quotient, lift a solution, and correct the remaining error in \(W\). This proves surjectivity. A fixed vector has zero image in the nilpotent quotient, so its fixed group is the one in \(W\).

The stable image and nilpotent quotient commute with the field extension: the rank of the matrices of the iterates is unchanged, and both fields are perfect. The finite étale scheme defined by (3.4) with \(y=0\) is a disjoint union of \(k\)-points; after extension it has precisely the same points. This proves (3.3), including its canonical identification. \(\square\)

**Proposition 3.2.** For a smooth connected projective curve \(C\) of genus \(g\),

\[
\begin{aligned}
H^0(C,\mathbf F_p)&=\mathbf F_p,\\
H^1(C,\mathbf F_p)&=\ker(F-1:H^1(C,\mathcal O_C)\to H^1(C,\mathcal O_C)),\\
H^q(C,\mathbf F_p)&=0\quad(q\geq2).
\end{aligned}
\tag{3.5}
\]

The degree-one group is finite of dimension at most \(g\). All these groups are invariant under algebraically closed field extension.

**Proof.** Choose two distinct \(k\)-points of \(C\). Their complements are affine and cover \(C\); their intersection is affine, since \(C\) is separated. Quasi-coherent affine vanishing and the Čech comparison give a two-term complex computing \(H^*(C,\mathcal O_C)\). Thus it vanishes above degree one. In degrees zero and one it is finite dimensional by proper coherent finiteness. Frobenius on this complex induces the semilinear map in Lemma 3.1. The long exact sequence of (3.1) and surjectivity of \(F-1\) in both degrees prove (3.5).

For field extension, the coordinate rings of every member and overlap of the cover tensor with \(k'\). Its Čech complex therefore tensors with \(k'\). Tensoring over a field is exact, so
\(H^q(C,\mathcal O_C)\otimes_k k'=H^q(C_{k'},\mathcal O_{C_{k'}})\), with the canonical map and its compatible Frobenius. Apply (3.3) to its kernels. In degree zero, \(F-1:k\to k\) is surjective with kernel \(\mathbf F_p\). This proves every asserted base-change isomorphism. \(\square\)

Every smooth connected curve is affine or projective by section 2. Consequently constant \(\mathbf F_p\)-cohomology vanishes above one on every such curve. It is finite on proper curves, and its proper field-extension maps are isomorphisms. Points have no positive cohomology and cause no additional case.

## 4. Prime-to-characteristic constants and the actual extension map

Let \(\ell\ne p\) be prime. Choose a primitive \(\ell\)-th root of unity in \(k\), and retain that root after extension to \(k'\). It identifies \(\underline{\mathbf F_\ell}\) with \(\mu_\ell\). Lesson 10 gives, for a smooth connected projective \(C\),

\[
\begin{aligned}
H^0(C,\mu_\ell)&=\mu_\ell(k),\\
H^1(C,\mu_\ell)&=\operatorname{Pic}^0(C)[\ell],\\
H^2(C,\mu_\ell)&=\mathbf Z/\ell,\\
H^q(C,\mu_\ell)&=0\quad(q>2).
\end{aligned}
\tag{4.1}
\]

The last nonzero identification sends a Kummer Chern class to the degree of its line bundle modulo \(\ell\). For \(A=C-S\) with \(S\) nonempty and finite, the same lesson proves

\[
\begin{gathered}
0\longrightarrow H^1(C,\mu_\ell)
\longrightarrow H^1(A,\mu_\ell)
\longrightarrow V_S\longrightarrow0,\\
V_S=\ker\!\left((\mathbf Z/\ell)^S\xrightarrow{\sum}\mathbf Z/\ell\right),
\qquad H^q(A,\mu_\ell)=0\quad(q\geq2).
\end{gathered}
\tag{4.2}
\]

These are finite groups, of degree-one ranks \(2g\) and \(2g+|S|-1\). We now verify that their **canonical** field-extension maps are isomorphisms; counting ranks by itself would not establish this.

**Proposition 4.1.** For any smooth finite-type curve and constant \(\mathbf F_\ell\), \(\ell\ne p\), pullback under an algebraically closed extension is an isomorphism on all cohomology groups.

**Proof.** Let \(J=\operatorname{Pic}^0_{C/k}\). Its representation of the line-bundle functor implies that \(J_{k'}\) represents the degree-zero functor for \(C_{k'}\): restricting a represented functor to \(k'\)-schemes is represented by base change. Degree and the degree-zero component commute with extension, either from Cartier divisors or from the degree decomposition of the Picard functor. Thus pullback on the group in degree one in (4.1) is precisely
\(J[\ell](k)\to J[\ell](k')\).

Multiplication by \(\ell\) on an abelian variety is finite étale. Finiteness is the abelian-variety input used in lesson 10: [Abelian varieties](course:AG-GS/AG-GS-06#6-the-degree-and-étaleness-of-multiplication), Theorems 6.1 and 6.2, also [Tag 03RP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/groupoids.html#groupoids-proposition-review-abelian-varieties); étaleness also follows from its differential, multiplication by the nonzero scalar \(\ell\) on every tangent space, translated from the identity. Consequently \(J[\ell]\) is a finite disjoint union of \(k\)-points. Field extension supplies no new point of this finite scheme. This proves the degree-one isomorphism for its actual pullback map.

Degree zero uses \(\mu_\ell(k)=\mu_\ell(k')\). For degree two choose a \(k\)-point \(c\) of \(C\). Its line bundle \(\mathcal O_C(c)\) has degree one and pulls back to the degree-one bundle of the \(k'\)-point \(c_{k'}\). Naturality of Kummer therefore sends a generator under (4.1) to a generator with the same degree. It is the identity on \(\mathbf Z/\ell\) under the degree identifications. Higher groups vanish.

For the affine curve \(A=C-S\), \(C_{k'}\) is again a smooth projective completion and its complement consists of the same labelled points. Sequence (4.2) is natural under extension. Indeed its residue is obtained by extending a normalized Kummer line bundle and measuring the orders of its rational normalization at those points; a base-field uniformizer still has order one after extension. Each coordinate is unchanged. The outside maps in the two sequences are now isomorphisms, so the middle map is an isomorphism by the short exact sequence argument. Degree zero and the vanishing higher groups have already been handled. Disjoint unions of connected curves and points give the general assertion. \(\square\)

Together, sections 3 and 4 establish every required vanishing, finiteness and field-invariance assertion for constant prime coefficients on smooth curves. Properness is essential for the characteristic-\(p\) finiteness and invariance parts.

## 5. How the properties survive the reductions

For brevity, the **required properties** of a pair \((X,\mathcal F)\) are the vanishing bounds of Theorem 1.1, its finiteness assertions when their hypotheses apply, and field invariance prime to \(p\) or for proper \(X\). The following lemmas prove the preservation mechanisms rather than assume a general finiteness theorem.

**Lemma 5.1 (exact sequences and summands).** The required properties pass from the two outer terms of a short exact sequence to its middle term. They pass to a direct summand, with compatible field-extension projections.

**Proof.** The long exact cohomology sequence proves each vanishing bound. For finiteness, \(H^q\) of the middle term is an extension of an image of \(H^q\) of the left term by a subgroup of \(H^q\) of the right term, so it is finite. Prime-to-\(p\) and \(p\)-primary coefficient conditions are preserved under subobjects, quotients and extensions. Constructibility has the same permanence on the Noetherian \(X\), by lesson 11.

For invariance, pull back the short exact sequence; inverse image is exact. The natural long exact sequences form a commutative diagram. The maps on both outer sheaves in every degree are isomorphisms. Applying the five lemma to the segment ending with \(H^{q+1}\) of the left term proves the middle isomorphism, including \(q=0\), where the preceding group is zero. For a summand, cohomology respects the split inclusion and projection. If a natural base-change map on a direct sum is an isomorphism, its restriction to each summand is an isomorphism: its inverse is the corresponding projection composed with that inverse and the inclusion. \(\square\)

**Lemma 5.2 (finite direct image).** If \(h:Y\to X\) is finite and the required properties hold for \(\mathcal G\) on \(Y\), they hold for \(h_*\mathcal G\) on \(X\).

**Proof.** Lesson 7 proves exactness of finite direct image and
\(H^q(X,h_*\mathcal G)=H^q(Y,\mathcal G)\) for all abelian coefficients. A finite scheme over an affine scheme is affine; over proper \(X\), \(Y\) is proper. Both are still separated finite-type schemes of dimension at most one. Finite stalk sums preserve the coefficient conditions, and finite pushforward preserves constructibility by lesson 11, since finite morphisms here are of finite presentation. The finite base-change isomorphism and its compatible cohomology comparison identify the field-extension map with the one on \(Y\). All conclusions follow. \(\square\)

**Lemma 5.3 (discarding a finite boundary).** For constructible \(\mathcal F\) and dense \(j:U\to X\), the required conclusions for \(\mathcal F\), under any fixed applicable coefficient hypotheses, are equivalent to those for \(j_!j^{-1}\mathcal F\).

**Proof.** Put \(\mathcal K=j_!j^{-1}\mathcal F\) and \(B=\bigoplus_Z\mathcal F_{\bar z}\). From (2.1)–(2.2) we have

\[
\begin{gathered}
0\to H^0(X,\mathcal K)\to H^0(X,\mathcal F)\to B\\
\to H^1(X,\mathcal K)\to H^1(X,\mathcal F)\to0,\\
H^q(X,\mathcal K)\simeq H^q(X,\mathcal F)\quad(q\geq2).
\end{gathered}
\tag{5.1}
\]

The higher isomorphisms prove the vanishing equivalence. Since \(B\) is finite, the degree-zero and degree-one groups for one sheaf are finite exactly when they are finite for the other. Both sheaves are constructible.

For field extension, \(B\to B'\) is an isomorphism, and extension by zero commutes with pullback. If the maps for \(\mathcal F\) are isomorphisms, the kernel of \(H^0(\mathcal F)\to B\) gives the degree-zero isomorphism for \(\mathcal K\). The degree-one group for \(\mathcal K\) is an extension of the cokernel of that map by \(H^1(\mathcal F)\), giving its degree-one isomorphism. Conversely, \(H^0(\mathcal F)\) is an extension of \(H^0(\mathcal K)\) by the kernel of \(B\to H^1(\mathcal K)\), and \(H^1(\mathcal F)\) is its cokernel. These descriptions prove the reverse direction. For \(q\geq2\) use (5.1). Thus the equivalence concerns the canonical maps in every degree. \(\square\)

## 6. Constants on singular curves

**Proposition 6.1.** For any reduced \(X\) as above, any open \(j:U\to X\) and any prime \(\ell\), the required properties hold for \(j_!\underline{\mathbf F_\ell}\).

**Proof.** First suppose \(X\) is smooth. Work on each connected component. A component is a point or an irreducible smooth curve. Its intersection with \(U\) is empty, giving the zero sheaf, or is dense. In the dense case apply Lemma 5.3 to the constant sheaf on the component; sections 3–4 proved its required properties. This handles the smooth case.

In general let \(\nu:X^\nu\to X\) be the finite normalization. It is a disjoint union of smooth curves and points. For \(U^\nu=\nu^{-1}U\), let \(j^\nu:U^\nu\to X^\nu\). The smooth case proves the properties for \(j^\nu_!\mathbf F_\ell\), and Lemma 5.2 proves them for
\(\mathcal E=\nu_*j^\nu_!\mathbf F_\ell\).

There is a dense open \(W\subset X\) over which \(\nu\) is an isomorphism: birationality supplies such an open on each component, and the omitted intersections and closed complements are finite. Over \(W\), \(\mathcal E\) and \(j_!\mathbf F_\ell\) agree, by finite base change and the stalk characterization of extension by zero. Both are constructible. Applying Lemma 5.3 to them with the same open \(W\) transfers all the conclusions from \(\mathcal E\) to \(j_!\mathbf F_\ell\). Their common extension from \(W\) has the same natural field maps, so no assertion that normalization commutes with arbitrary field extension is needed. \(\square\)

## 7. Trace across the compactification

**Lemma 7.1.** In a cartesian square with \(h:Y\to X\) finite, \(j:U\to X\) open, \(V=Y\times_XU\), and \(j':V\to Y\), one has a natural isomorphism

\[
j_!f_*\mathcal G\simeq h_*j'_!\mathcal G,
\qquad f:V\to U.
\tag{7.1}
\]

**Proof.** Restrict the right side to \(U\). Finite base change and \((j')^{-1}j'_!=1\) identify it with \(f_*\mathcal G\). At a geometric point outside \(U\), finite-pushforward stalks are sums over points of \(Y\) outside \(V\); every summand of \(j'_!\mathcal G\) is zero. The characterization of open extension by zero gives the isomorphism, naturally: adjunction gives the unique map with the prescribed identity over \(U\), and its stalks are isomorphisms. This also proves compatibility with maps of \(\mathcal G\) and with field extension. \(\square\)

**Proposition 7.2.** Suppose \(X\) is reduced, \(U\subset X\) is a connected dense open in an irreducible component away from the others, and \(\mathcal L\) is a finite locally constant \(\mathbf F_\ell\)-sheaf on \(U\). The required properties hold for \(j_!\mathcal L\).

**Proof.** Its finite monodromy group \(G\) has an \(\ell\)-Sylow subgroup \(H\). Lesson 11 constructs the finite étale cover \(f:V\to U\) corresponding to \(G/H\). It is connected, of degree \(d=[G:H]\) prime to \(\ell\). On \(V\), the pulled-back sheaf has a finite filtration with constant \(\mathbf F_\ell\)-quotients. Recall the mechanism: an \(\ell\)-group acting on a nonzero finite \(\mathbf F_\ell\)-vector space has a nonzero fixed vector by orbit counting. Its fixed line and induction on the quotient dimension give the filtration.

Restriction followed by trace on \(\mathcal L\) is multiplication by \(d\). Choose \(a\) with \(ad\equiv1\pmod\ell\). Applying \(j_!\) to the unit and to \(a\) times trace exhibits \(j_!\mathcal L\) as a direct summand of \(j_!f_*f^{-1}\mathcal L\). These are sheaf maps, so the retraction works simultaneously in every cohomological degree and is compatible with extension of the field.

The composite \(V\to U\to X\) is separated and quasi-finite, since \(f\) is finite and \(j\) is open. Zariski's Main Theorem gives an open embedding \(V\subset Y\) with \(h:Y\to X\) finite. Replace \(Y\) by the reduced closure of \(V\) in it; \(V\) is already reduced when \(U\) is smooth, which is the case used below. More generally one can first choose the smooth open for the application. Now \(V\) is dense in \(Y\), and

\[
V=Y\times_XU.
\tag{7.2}
\]

To verify (7.2), the embedding \(V\to Y_U\) is also proper: a map from a scheme proper over \(U\) to a separated \(U\)-scheme is proper, by the closed-graph factorization. Thus it is an open and closed immersion. Its closed complement in the open \(Y_U\), if nonempty, would be an open of \(Y\) disjoint from the dense \(V\). This is impossible.

By (7.1), the sheaf of which \(j_!\mathcal L\) is a summand is
\(h_*j'_!f^{-1}\mathcal L\). Apply the exact \(j'_!\) to the filtration on \(V\). Its successive quotients are \(j'_!\mathbf F_\ell\), whose properties on the reduced \(Y\) were proved in Proposition 6.1. Lemma 5.1 gives the conclusions for \(j'_!f^{-1}\mathcal L\), Lemma 5.2 for its finite pushforward, and Lemma 5.1 for its direct summand. If \(X\) is affine, \(Y\) is affine; if \(X\) is proper, \(Y\) is proper. Thus precisely the required affine and proper hypotheses survive the argument. \(\square\)

In the proposition we may simply assume \(U\) smooth, as we do in the proof of the theorem. If a connected open initially includes singular points, delete their finite set and use Lemma 5.3 first. This proves the same conclusion without that additional smoothness assumption. In particular the reduced-closure construction above is always applied to a reduced \(V\).

The degree condition is indispensable. Multiplication by \(d\) on an \(\ell\)-torsion sheaf is invertible only if \(\ell\nmid d\). A cover merely trivializing the local system could have degree divisible by \(\ell\); it would not supply this retraction. The Sylow cover supplies the appropriate degree and a filtration instead of requiring triviality at once.

## 8. Proof for all torsion sheaves

**Proof of Theorem 1.1 and proper algebraically closed invariance.** First remove nilpotents using topological invariance. This does not change the étale topos, its cohomology, or the canonical field-extension maps. All geometric hypotheses in the theorem persist.

Suppose first that \(\mathcal F\) is constructible. It has a common annihilator \(n\): choose the orders of the finitely many finite groups in its constructible partition and take a common multiple. The primary decomposition of \(\mathbf Z/n\) gives a finite direct sum of \(\ell\)-primary subsheaves. The projections are integer polynomials in scalar multiplication, so define canonical sheaf maps. It suffices to treat one prime \(\ell\). If \(\ell^b\mathcal F=0\), the exact sequence

\[
0\longrightarrow\mathcal F[\ell]\longrightarrow\mathcal F
\longrightarrow\mathcal F/\mathcal F[\ell]\longrightarrow0
\tag{8.1}
\]

has an \(\ell\)-torsion left term and a right term killed by \(\ell^{b-1}\). Both are constructible by the Noetherian strong Serre property in lesson 11. Induction on \(b\) and Lemma 5.1 reduce to a constructible \(\mathbf F_\ell\)-sheaf.

Choose a dense smooth open \(U\), disjointly decomposed into finitely many irreducible curves and points, on which \(\mathcal F\) is locally constant, as in section 2. Lemma 5.3 reduces every required property to \(j_!\mathcal F|_U\). Extension by zero from this disjoint union is the finite direct sum of extensions from its components, since its stalk sum and adjunction commute with finite sums. Point components have no positive cohomology and finite degree-zero groups, with identical pullback groups. On each curve component Proposition 7.2 proves all the properties. This proves every vanishing, finiteness and applicable invariance assertion for constructible coefficients, including proper invariance for \(\ell=p\).

Now let \(\mathcal F\) be arbitrary torsion. Since \(X\) is Noetherian, lesson 11 proves that it is the filtered union of its constructible subsheaves \(\mathcal C_i\). This uses the Noetherian version: the analogous assertion on a general qcqs scheme would be false. A subsheaf of a prime-to-\(p\), or of a \(p\)-primary, sheaf satisfies that same coefficient condition. Each \(\mathcal C_i\) has a finite annihilator; in the \(p\)-primary case it is killed by some \(p^{b_i}\).

The filtered-cohomology lemma of lesson 10 applies to the Noetherian qc separated \(X\) and to \(X_{k'}\). It gives

\[
H^q(X,\mathcal F)=\mathop{\mathrm{colim}}_iH^q(X,\mathcal C_i).
\tag{8.2}
\]

The proved vanishing bounds for each \(\mathcal C_i\) therefore give parts 1–3 for \(\mathcal F\). Parts 4–5 already concern constructible sheaves and need no colimit finiteness assertion.

Inverse image commutes with filtered colimits, so the right side of (1.1) is the colimit of \(H^q(X_{k'},\mathcal C_i|_{X_{k'}})\). The naturality of (8.2) identifies (1.1) with the colimit of the canonical maps already proved to be isomorphisms, either for prime-to-\(p\) coefficients or for proper \(X\). Their colimit is an isomorphism. This proves part 6 and the stated proper strengthening in all degrees. \(\square\)

In particular the characteristic-\(p\) constant-coefficient vanishing holds on every affine \(X\) already by (3.2). On any proper \(X\) of dimension at most one, its finiteness follows from the theorem, with no smoothness or reducedness assumption left over.

## 9. Proper curves over separably closed fields

**Theorem 9.1.** Let \(k'/k\) be an extension of separably closed fields, \(X\) a proper \(k\)-scheme of dimension at most one, and \(\mathcal F\) a torsion abelian sheaf. Then

\[
H^q(X,\mathcal F)\longrightarrow
H^q(X_{k'},\mathcal F|_{X_{k'}})
\tag{9.1}
\]

is an isomorphism for every \(q\geq0\).

**Proof.** Embed an algebraic closure \(\bar k\) of \(k\) into an algebraic closure \(\bar k'\) of \(k'\), extending \(k\to k'\). Algebraic extensions of a separably closed field are purely inseparable: every algebraic element has a suitable \(p\)-power separable over the field, which must lie in that field. In characteristic zero the algebraic closures add nothing. Thus \(\bar k/k\) and \(\bar k'/k'\) are purely inseparable.

The base changes \(X_{\bar k}\to X\) and \(X_{\bar k'}\to X_{k'}\) are universal homeomorphisms. Indeed a purely inseparable algebraic field extension is integral, radicial and surjective on spectra, and these properties persist after any base change. Lesson 7 identifies their étale topoi and cohomology for all abelian sheaves. The pullback square therefore compares (9.1) with
\(H^q(X_{\bar k},\mathcal F|_{X_{\bar k}})\to
H^q(X_{\bar k'},\mathcal F|_{X_{\bar k'}})\).

Its source scheme is still proper of dimension at most one. The proper algebraically closed invariance proved in section 8 makes this last map an isomorphism. The two vertical maps are isomorphisms by topological invariance, and the square commutes by functoriality of inverse image. Hence (9.1) is an isomorphism. \(\square\)

This proof allows nonperfect separably closed fields. Replacing them silently by algebraically closed fields would have omitted the universal-homeomorphism step.

## 10. Finitely generated Noetherian coefficients

Let \(\Lambda\) be a commutative Noetherian ring. A constructible \(\Lambda\)-module sheaf means a finite constructible partition on whose pieces it is locally constant with finitely generated \(\Lambda\)-module values. Its underlying groups may be infinite. Suppose the underlying abelian sheaf is torsion.

**Theorem 10.1.** All \(H^q(X,\mathcal F)\) are finitely generated \(\Lambda\)-modules if \(\mathcal F\) is prime to \(p\), or if \(X\) is proper. The vanishing bounds and field-invariance conclusions of sections 1 and 9 also hold for these torsion coefficients.

**Proof.** The last sentence follows from the theorems for arbitrary torsion abelian sheaves once their cohomology is identified with module cohomology. Here is the comparison without a flatness assumption on \(\Lambda\). For an injective sheaf \(I\) of \(\Lambda\)-modules, take any étale covering of a basis object. Its augmented free-\(\Lambda\) Čech sheaf complex is exact: at a geometric stalk it is a sum of augmented complexes of a nonempty set of lifts, each contracted by choosing one covering lift. Applying \(\operatorname{Hom}_\Lambda(-,I)\) is exact and gives the augmented section Čech complex. Thus positive Čech cohomology of the underlying abelian sheaf of \(I\) vanishes on every such covering, including its basis overlaps. The vanishing criterion of lesson 3 makes that underlying sheaf acyclic on every basis object, and in particular for global sections. An injective module resolution remains exact after forgetting scalars and is an acyclic abelian resolution. Both cohomologies are consequently computed by the same section complex, with the same canonical maps.

A common integer \(n>0\) kills \(\mathcal F\). On each qc locally constant stratum choose a finite family of qc étale trivializing charts: their open images cover the stratum, so quasi-compactness permits a finite selection. Each chart has a finitely generated constant value. Choose finitely many \(\Lambda\)-generators of each of these finitely many values; torsion gives an annihilator for every generator. Their common multiple kills all values, and therefore the sheaf. There are finitely many strata, so one such \(n\) works globally. Primary decomposition is \(\Lambda\)-linear and reduces the proof to \(\ell^b\)-torsion.

We first handle constants and their open extensions. If \(\ell M=0\) for a finitely generated \(\Lambda\)-module \(M\), the canonical coefficient maps give

\[
H^q(X,j_!\underline{\mathbf F_\ell})\otimes_{\mathbf F_\ell}M
\simeq H^q(X,j_!\underline M).
\tag{10.1}
\]

To prove this, choose an \(\mathbf F_\ell\)-basis of the underlying vector space \(M\). Its finite partial spans form a filtered system, and the corresponding constant sheaves and their \(j_!\)'s have colimit \(j_!\underline M\). Cohomology commutes with that colimit by lesson 10 and with finite direct sums. The resulting direct-sum isomorphism is exactly the coefficient map in (10.1), so it is canonical and \(\Lambda\)-linear, independent of the basis. The left-hand cohomology is finite dimensional in the stated prime-to-\(p\) or proper cases by section 8. Its tensor with \(M\) is therefore finitely generated over \(\Lambda\).

For \(\ell^b M=0\), use \(0\to M[\ell]\to M\to M/M[\ell]\to0\). Both values are finitely generated because \(\Lambda\) is Noetherian, and the quotient is killed by \(\ell^{b-1}\). Exactness of constant sheafification and of \(j_!\), induction on \(b\), and the long exact sequence prove the constant-extension assertion. Kernels and images of finite modules stay finite over a Noetherian ring, as required in that sequence.

It remains to reduce a local system with possibly infinite underlying value to these constants. Choose the dense smooth irreducible opens as before. On each such normal curve, a locally constant finitely generated \(\Lambda\)-module has **finite monodromy**. Here is the additional check that finite underlying sets had supplied automatically in section 7. At a geometric generic point its value \(M\) has a continuous Galois action by lesson 8. The intersection of the open stabilizers of finitely many \(\Lambda\)-generators fixes all of \(M\); its normal core still has finite index. The action therefore has finite image.

It factors through \(\pi_1(U)\): on every strict local ring the sheaf is constant, since a trivializing étale neighborhood of its closed point has a section over the strictly henselian local scheme. It thus kills the Galois groups of the fraction fields of these strict local rings. The normal-scheme fundamental-group theorem identifies the kernel of \(G_{k(U)}\to\pi_1(U)\) with their closed normal closure, [Tags 0BQM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-proposition-normal) and [0BTD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-normal-pione-quotient-inertia). This is the precise normal-scheme geometric input. Hence the finite image is realized by a finite étale Galois cover of \(U\).

For completeness the sheaf pulled back to that cover is constant, not merely generically constant. On a normal connected étale chart, sections of a constant module are determined by their generic values: the chart is integral and its locally constant functions are constant. Local identifications of our locally constant sheaf with a constant module, using its trivial generic monodromy, therefore agree on every overlap whenever they agree generically, component by component. Their generic identifications glue to a global constant sheaf. This justifies use of its monodromy representation with these infinite coefficient modules. We have used normality of the smooth dense open; no such classification for arbitrary connected schemes is being asserted.

Choose an \(\ell\)-Sylow subgroup \(H\) of the finite monodromy image and its prime-to-\(\ell\) cover \(V\to U\). The pulled-back module has a finite filtration with constant finitely generated \(\Lambda\)-module quotients. To verify this even for infinite underlying groups, let \(J\) be the augmentation ideal of \((\mathbf Z/\ell^b)[H]\). Lesson 11 proves \(J\) nilpotent: modulo \(\ell\), induct on \(|H|\) using a central element \(z\) of order \(\ell\), with \((z-1)^\ell=0\); lifting gives \(J^N\subset\ell R\) and hence \(J^{Nb}=0\). The filtration by \(J^iM\) is \(\Lambda\)-stable because the actions commute. Its terms and quotients are finitely generated by Noetherianity, and \(H\) acts trivially on each quotient. They give the claimed constant filtration on \(V\).

Extend this cover to a finite \(Y\to X\) exactly as in section 7. Apply its natural identity (7.1), the trace retraction with \(ad\equiv1\pmod{\ell^b}\), and the constant-extension finiteness just proved on \(Y\). Extension by zero is exact, finite pushforward has the same cohomology, and finite modules are stable under extensions and summands. This gives finiteness for \(j_!\mathcal F|_U\). The boundary version of (5.1) now has a finite direct sum of finitely generated \(\Lambda\)-modules in place of \(B\); Noetherianity gives the same finiteness equivalence. It finishes the proof for \(\mathcal F\). \(\square\)

## 11. Three examples and what they distinguish

**Artin–Schreier on the affine line.** If \(p>0\), (3.2) gives

\[
H^1(\mathbf A^1_k,\mathbf F_p)=k[t]/\{f^p-f:f\in k[t]\}.
\tag{11.1}
\]

This quotient is an additive \(\mathbf F_p\)-space, not a quotient by a \(k\)-linear subspace. Every class has a unique representative

\[
\sum_{m\geq1,\ p\nmid m}a_m t^m
\quad\text{with finite support.}
\tag{11.2}
\]

Indeed constants are removed since \(a\mapsto a^p-a\) is surjective on \(k\). If a term has exponent divisible by \(p\), take a \(p\)-th root of its coefficient and subtract \((b t^{m/p})^p-bt^{m/p}\); this lowers its exponent. Repetition terminates. For uniqueness, a nonconstant \(f^p-f\) has highest exponent divisible by \(p\), whereas a nonzero polynomial of the form (11.2) does not. A constant difference is zero because both representatives have constant coefficient zero. Hence (11.1) is additively \(\bigoplus_{p\nmid m,\ m>0}k\), an infinite group. Under a proper algebraically closed extension \(k'/k\), a coefficient \(b\in k'-k\) in \(bt\) gives a new class. Both finiteness and field invariance therefore fail in this affine \(p\)-torsion example.

**Extension by zero on the projective line.** Let \(j:\mathbf A^1\to\mathbf P^1\), \(i:\{\infty\}\to\mathbf P^1\), and \(\ell\ne p\). The sequence
\(0\to j_!\mathbf F_\ell\to\mathbf F_\ell\to i_*\mathbf F_\ell\to0\) has identity map on degree-zero cohomology of its middle and right terms. Thus

\[
H^q(\mathbf P^1,j_!\mathbf F_\ell)=
\begin{cases}\mathbf F_\ell,&q=2,\\0,&q\ne2.
\end{cases}
\tag{11.3}
\]

In contrast \(j_*\mathbf F_\ell=\mathbf F_\ell\) on \(\mathbf P^1\). Over the open this is immediate, and at infinity the punctured strict local curve is the spectrum of a field, whose sections of the constant sheaf are \(\mathbf F_\ell\). The adjunction map from the constant sheaf is the identity on those stalks. Thus \(H^q(\mathbf P^1,j_*\mathbf F_\ell)\) is \(\mathbf F_\ell\) in degrees zero and two and zero elsewhere. Choosing the root of unity fixes the displayed degree-two identifications.

**A node adds one degree-one class.** Let \(C\) be an irreducible rational projective curve with one ordinary node \(s\) and no other singularities. Its normalization is \(\nu:\mathbf P^1\to C\); the node has two distinct preimages. For \(\ell\ne p\), finite-pushforward stalks give

\[
0\longrightarrow\mathbf F_{\ell,C}
\longrightarrow\nu_*\mathbf F_{\ell,\mathbf P^1}
\xrightarrow{\mathrm{difference}}i_*\mathbf F_\ell
\longrightarrow0,
\quad i:\{s\}\to C.
\tag{11.4}
\]

At the node the first map is diagonal into two copies and the second subtracts the two branch values; elsewhere the first is an isomorphism. A global section on the connected normalization has the same value on both branches, so its difference is zero. The long exact sequence and finite-pushforward comparison give

\[
\begin{aligned}
H^0(C,\mathbf F_\ell)&=\mathbf F_\ell,\\
H^1(C,\mathbf F_\ell)&=\mathbf F_\ell,\\
H^2(C,\mathbf F_\ell)&=\mathbf F_\ell,\\
H^q(C,\mathbf F_\ell)&=0\quad(q>2).
\end{aligned}
\tag{11.5}
\]

The additional degree-one class records the failure of independent branch values to arise from a global value on the normalization. The proof does not identify a singular curve with its normalization; it keeps the boundary cokernel.

## 12. Exercises and complete solutions

1. **Easy.** Compute \(H^*(\mathbf A^1_k,\mathbf F_\ell)\) for \(\ell\ne p\), and \(H^*(\mathbf A^1_k,\mathbf F_p)\) when \(p>0\). Specify the additive meaning of the latter degree-one answer.
2. **Medium.** For \(j:\mathbf A^1\to\mathbf P^1\) and \(\ell\ne p\), compute \(H^*(\mathbf P^1,j_!\mathbf F_\ell)\) and \(H^*(\mathbf P^1,j_*\mathbf F_\ell)\). Justify the stalk at infinity in the second computation.
3. **Medium.** For an irreducible nodal cubic whose normalization is \(\mathbf P^1\), compute constant prime-to-characteristic cohomology using the finite-pushforward sequence. Identify the map of degree-zero groups that creates its degree-one class.
4. **Medium.** Prove \(H^2(X,\mathcal F)=0\) for every torsion sheaf on an affine separated finite-type curve, explicitly carrying the reduction through finite covers and open extensions of constant sheaves.
5. **Hard.** Prove field-extension invariance for a smooth projective curve and \(\mathcal F=\mathbf F_\ell\), \(\ell\ne p\), directly from the Kummer computations of lesson 10. Prove the actual pullback is an isomorphism rather than just comparing dimensions.

**Solution 1.** The completion is \(\mathbf P^1\), of genus zero, and the boundary has one point. Sequence (4.2) has zero left term and zero residue kernel, so \(H^1(\mathbf A^1,\mathbf F_\ell)=0\). The affine vanishing gives zero in all degrees \(q\geq2\), and connectedness gives \(H^0=\mathbf F_\ell\).

In characteristic \(p\), Artin–Schreier and affine quasi-coherent vanishing give \(H^0=\mathbf F_p\), \(H^q=0\) for \(q\geq2\), and the additive quotient (11.1) in degree one. To compute it, remove the constant term by solving \(a^p-a=c\) in \(k\). Replace every monomial with exponent divisible by \(p\) by its equivalent monomial with exponent divided by \(p\), taking the coefficient's unique \(p\)-th root. After finitely many replacements only positive exponents prime to \(p\) remain. A nonzero difference of two such representatives cannot equal \(f^p-f\): if \(f\) is nonconstant its leading exponent is divisible by \(p\), and if \(f\) is constant the difference would be constant. Thus these representatives are unique and addition is coefficientwise. The resulting \(\mathbf F_p\)-space is \(\bigoplus_{m>0,\ p\nmid m}k\); there are infinitely many nonzero independent summands.

**Solution 2.** At a point of \(\mathbf A^1\), \(j_!\mathbf F_\ell\) has stalk \(\mathbf F_\ell\); at infinity it has stalk zero. The localization exact sequence therefore has closed term \(i_*\mathbf F_\ell\). Its degree-zero map \(H^0(\mathbf P^1,\mathbf F_\ell)\to H^0(\{\infty\},\mathbf F_\ell)\) is the identity. Both boundary higher groups and \(H^1(\mathbf P^1,\mathbf F_\ell)\) vanish. Exactness gives \(H^0(j_!)=H^1(j_!)=0\), and then \(H^2(j_!)\simeq H^2(\mathbf P^1,\mathbf F_\ell)=\mathbf F_\ell\); the groups above two vanish.

For \(j_*\), the stalk at infinity is the section group over the punctured strict local curve. Its strict henselian local ring is a discrete valuation ring, as proved in lesson 10, and removing the closed point gives its fraction field. Field-topos comparison sends the constant sheaf to a trivial Galois module, so its invariants are \(\mathbf F_\ell\). The unit \(\mathbf F_{\ell,\mathbf P^1}\to j_*\mathbf F_\ell\) is the identity on that stalk and on the open. Enough geometric points makes it an isomorphism. Consequently its cohomology is \(\mathbf F_\ell\) in degrees zero and two, and zero in all other degrees.

**Solution 3.** Order the two branches at the node and take their second value minus their first. The stalk map \(\mathbf F_\ell^2\to\mathbf F_\ell\) is surjective with diagonal kernel, while away from the node normalization is an isomorphism. This proves (11.4). Exact finite direct image identifies its middle cohomology with that of \(\mathbf P^1\). Its global sections are constant, so the difference map \(\mathbf F_\ell\to\mathbf F_\ell\) is zero. The start of the long exact sequence is
\(0\to H^0(C)\to\mathbf F_\ell\xrightarrow{0}\mathbf F_\ell\to H^1(C)\to0\).
It gives \(H^0(C)=\mathbf F_\ell\) and a connecting isomorphism from the node's \(\mathbf F_\ell\) to \(H^1(C)\). In degree two the skyscraper has no higher groups, so \(H^2(C)\simeq H^2(\mathbf P^1)=\mathbf F_\ell\); above two both groups vanish. Changing the branch order changes the chosen degree-one generator by a sign, not the group.

**Solution 4.** Remove nilpotents. Express \(\mathcal F\) as the filtered union of constructible subsheaves and use filtered cohomology; it suffices to treat one constructible sheaf. Decompose its finite annihilator into prime powers and apply (8.1) inductively; it suffices to treat an \(\mathbf F_\ell\)-sheaf. Choose a smooth dense open on which it is a finite local system. The finite boundary has zero positive cohomology, so (5.1) identifies its degree-two group with that of the extension by zero of this local system.

On each connected open component use its Sylow cover of degree prime to \(\ell\). The trace makes our extension a summand of a finite pushforward from \(Y\), and \(Y\) is affine since it is finite over the affine \(X\). Its pulled-back local system has a finite flag with constant \(\mathbf F_\ell\)-quotients. It is therefore enough to show \(H^2(Y,j'_!\mathbf F_\ell)=0\).

Normalize the reduced \(Y\). Its normalization is a finite disjoint union of affine smooth curves and points. Constant \(\mathbf F_\ell\) has zero degree-two cohomology there: for \(\ell\ne p\), use the affine Kummer computation; for \(\ell=p\), use (3.2). Removing a finite boundary does not change degree two, so the corresponding extensions by zero also have zero degree two. Finite pushforward preserves their cohomology. On a dense open where normalization is an isomorphism, its pushed extension and \(j'_!\mathbf F_\ell\) agree; discarding the finite boundary once more transfers the vanishing to \(Y\). Exactness along the flag and the trace retraction transfer it to our original sheaf. Finally filtered cohomology transfers it to arbitrary torsion \(\mathcal F\). This argument treats wild \(p\)-torsion as well as the prime-to-characteristic part.

**Solution 5.** Choose \(\zeta\in\mu_\ell(k)\) and use it in both fields. Kummer identifies \(H^1(C,\mu_\ell)\) with \(\operatorname{Pic}^0(C)[\ell]\), and \(H^2\) with degree modulo \(\ell\); \(H^0\) consists of the constant roots and higher groups vanish.

The degree-zero Picard functor is represented by its Jacobian \(J\). Restricting this represented functor to \(k'\)-schemes is represented by \(J_{k'}\), so the degree-one pullback is exactly \(J[\ell](k)\to J[\ell](k')\). The kernel of multiplication by the invertible \(\ell\) is finite étale; over an algebraically closed field it is a finite union of \(k\)-points. Hence this map is a bijection. Degree-zero roots of unity are unchanged. A \(k\)-point of \(C\) supplies a degree-one line bundle, and its pullback still has degree one. Kummer naturality sends its Chern class to the corresponding generator after extension, proving that degree-two pullback is an isomorphism. All higher groups are zero on both sides. Transferring along the same \(\zeta\) proves the assertion for \(\mathbf F_\ell\) with its actual canonical pullback map.

## 13. Sources and proof scope

The preceding proofs supply the full curve reduction, including finite boundary exactness in degrees zero and one, the finite compactification of the Sylow cover, its retraction in every degree, primary induction, filtered torsion approximation and canonical field-extension maps. The characteristic-\(p\) argument proves the semilinear lemma and its invariant kernels explicitly. The Noetherian coefficient argument retains finitely generated modules even when their underlying groups are infinite.

- **[Stacks, torsion curves]** [Tags 03SB, 0A52, 0A5B–0A5D, 0GJA, 03SG, 0A3Q, 03SD, 03SC, 03RT and 0A5E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-vanishing-torsion) are the target reduction, vanishing, finiteness and separably closed invariance results. Their compressed exact-sequence and trace reductions are written out in sections 5–9. Section 4 verifies the canonical map, strengthening the source's rank-count explanation of invariance.
- **[Stacks, Artin–Schreier]** [Tags 0A3J–0A3P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-artin-schreier), including [0A3L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-lemma-F-1) and [0HAN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-lemma-F-2), give the semilinear and proper-coefficient targets. For curves, section 3 uses the affine/projective alternative and an explicit two-affine Čech calculation; it does not require a top-coherent-cohomology theorem in arbitrary dimension.
- **[Stacks, module coefficients]** [Tags 0GJB–0GJI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-vanishing-torsion-coefficients) are compared in section 10. Formula (10.1) proves its constant-coefficient tensor calculation using filtered sums, and the normal dense open is where finite monodromy for finitely generated modules is justified.
- **[SGA 4]** M. Artin's Exposé IX, sections 3.5, 4.7–4.8 and 5.1–5.8, provides the historical Artin–Schreier, curve and trace discussion, with the prime-to-characteristic vanishing corollary at 5.7, in the [free re-edition](https://www.normalesup.org/~forgogozo/SGA4/). The proofs above do not depend on it.

The external foundational geometry is precisely the finite normalization and smooth-curve completion, Zariski's Main Theorem, proper coherent finiteness, Picard representation and the normal-scheme fundamental-group input cited where used. The finite étale classification, exact functors, trace, filtered-cohomology and Kummer tools are proved in earlier lessons or cited where used. No general proper base change, smooth base change, comparison with singular cohomology or later duality theorem is assumed in this lesson.
