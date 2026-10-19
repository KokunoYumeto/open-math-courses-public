# Local duality and finiteness

*Mathematical exposition by GPT-6.1 Sol (OpenAI). Original exposition: CC0 1.0.*

Local cohomology is usually an infinite module. Over a complete local ring, however, its dual is finite. This reverses two kinds of information: the degrees in which local cohomology vanishes become the degrees in which a finite complex vanishes, and an annihilator question becomes a support question for a finite module. We develop that reversal and use it to prove the finiteness theorem, including specialization-closed supports.

We use the Čech computation, the depth criterion, and dimension vanishing from Local cohomology. We also use injective resolutions, derived tensor and Hom, finite free resolutions bounded above, Artin–Rees, and flatness and exactness of completion on finite modules. Complexes have cohomological degrees: \(H^i(K[a])=H^{i+a}(K)\). In particular, a module shifted by \([d]\) lies in degree \(-d\). Rings are commutative and Noetherian. A finite module means a finitely generated module.

Our primary algebraic references are [Stacks] and [Grothendieck–Laszlo]. Existence of a dualizing complex is a hypothesis whenever it is used; it is not automatic for arbitrary Noetherian local rings. Proposition 2.5 supplies it for the classes considered there. The proofs below use a single convention throughout: a normalized dualizing complex \(\omega^\bullet\) over \((A,\mathfrak m,k)\) satisfies \(R\operatorname{Hom}_A(k,\omega^\bullet)=k[0]\). We prove that this is equivalent to \(R\Gamma_{\mathfrak m}(\omega^\bullet)=E[0]\), where \(E\) is the injective hull of \(k\).

## 1. The module that detects the closed point

An inclusion \(N\subset J\) is **essential** if every nonzero submodule of \(J\) meets \(N\). An injective hull is an essential inclusion into an injective module. The essential condition removes superfluous injective summands.

**Proposition 1.1 (construction of the hull).** Every module has an injective hull, unique up to an isomorphism extending its inclusion.

**Proof.** Embed \(N\) into an injective module \(J\). Among submodules of \(J\) containing \(N\) essentially, take a maximal one \(E\), using Zorn: a union of a chain remains essential.

We verify Baer's criterion for \(E\). Suppose a map \(u:\mathfrak b\to E\) from an ideal does not extend to \(A\). Form the pushout
\[
P=(E\oplus A)/\{(u(b),-b):b\in\mathfrak b\}.
\]
The natural inclusion \(E\to P\) is injective. Choose a maximal submodule \(L\subset P\) disjoint from \(E\). Then \(E\subset P/L\) is essential: otherwise the inverse image of a nonzero disjoint submodule would enlarge \(L\). Also \(P/L\ne E\). Indeed, equality would give a retraction \(P\to E\), and the image of \((0,1)\) would extend \(u\). Extend \(E\to J\) to \(P/L\to J\) by injectivity of \(J\). Its kernel is zero by essentiality. Since essential inclusions compose, its image contradicts maximality of \(E\). Thus Baer's criterion holds. For uniqueness, extend the inclusion of \(N\) from one hull into the other. Essentiality makes this map injective. Its image splits because its domain is injective, and essentiality in the target makes the complementary summand zero. ∎

Fix \((A,\mathfrak m,k)\), its hull \(E\), and
\[
D(N)=\operatorname{Hom}_A(N,E),\qquad E_n=E[\mathfrak m^n].
\]
The socle \(E[\mathfrak m]\) is exactly the given copy of \(k\). An additional independent socle vector would generate a simple submodule disjoint from it. Moreover,
\[
E=\bigcup_{n\ge1} E_n.
\tag{1.1}
\]
To see this, the torsion submodule \(\Gamma_{\mathfrak m}(E)\) is injective by the Baer–Artin–Rees argument in Local cohomology, Proposition 2.1. It contains \(k\), so it splits in \(E\), and essentiality kills the complementary summand.

**Lemma 1.2 (finite-length duality).** For every finite-length module \(L\), the evaluation map \(L\to D(D(L))\) is an isomorphism, and \(D(L)\) has the same length as \(L\).

**Proof.** The functor \(D\) is exact. Since \(D(k)=k\), a composition series proves the length assertion. Evaluation is injective: for \(0\ne x\in L\), choose a maximal proper submodule of the cyclic module \(Ax\). Its quotient is \(k\), and its quotient map, followed by \(k\subset E\), extends to \(L\to E\); it does not kill \(x\). Equality of lengths now proves surjectivity. ∎

By adjunction, \(E_n\) is injective over \(A/\mathfrak m^n\), and it is its residue-field hull. Lemma 1.2 applied to \(A/\mathfrak m^n\) gives
\[
\operatorname{End}_A(E_n)=A/\mathfrak m^n.
\]
Every endomorphism preserves \(E_n\). Restriction and (1.1) therefore identify scalar multiplication with
\[
\operatorname{End}_A(E)=\varprojlim_n A/\mathfrak m^n=\widehat A.
\tag{1.2}
\]
This also gives every \(\mathfrak m\)-power-torsion module a canonical \(\widehat A\)-action: to act on a vector killed by \(\mathfrak m^n\), use the corresponding residue class modulo \(\mathfrak m^n\).

**Lemma 1.3.** The module \(E\) is Artinian. Every Artinian \(A\)-module embeds into a finite direct sum of copies of \(E\).

**Proof.** Given a descending chain \(N_1\supset N_2\supset\cdots\) in \(E\), restriction makes \(\operatorname{End}(E)\to D(N_i)\) surjective. The kernels form an ascending chain of ideals in the Noetherian ring \(\widehat A\), hence stabilize. Exactness of \(D\) then gives \(D(N_i/N_{i+1})=0\). A nonzero torsion module has a nonzero finite-length cyclic submodule and hence a nonzero map into \(E\). The quotients must consequently be zero.

If \(N\) is Artinian, each cyclic submodule \(Ax\) is both finite and Artinian. The chain \(\mathfrak m^rAx\) stabilizes, and Nakayama applied to its stable finite term shows it eventually vanishes. Thus \(N\) is torsion. Its socle is a finite-dimensional vector space, since an infinite-dimensional vector space is not Artinian. Embed the socle into \(k^r\subset E^r\), and extend to \(N\to E^r\). A nonzero kernel would be torsion and would contain a nonzero socle, which is impossible. ∎

**Theorem 1.4 (Matlis duality).** If \(A\) is complete, \(D\) is an exact contravariant equivalence between finite and Artinian \(A\)-modules. Evaluation is an isomorphism in both categories.

**Proof.** A finite presentation \(A^s\to A^r\to M\to0\) gives
\(0\to D(M)\to E^r\to E^s\), so \(D(M)\) is Artinian. Conversely, Lemma 1.3, applied also to the quotient of an embedding, gives a copresentation \(0\to N\to E^r\to E^s\) for Artinian \(N\). Dualizing gives a finite presentation of \(D(N)\), because \(D(E)=A\) by (1.2). Evaluation is an isomorphism on \(A\) and \(E\); applying it to these presentations and copresentations, using exactness, proves it on \(M\) and \(N\). These natural evaluation isomorphisms make \(D\) an equivalence. ∎

For noncomplete \(A\), the same proof gives an equivalence between finite \(\widehat A\)-modules and Artinian \(A\)-modules. To justify using the same hull, construct the residue-field hull over \(\widehat A\). Its restriction is injective over \(A\), by flatness and tensor–restriction adjunction. Its torsion submodules have identical \(A\)- and \(\widehat A\)-submodules, because every coefficient acting on a vector killed by \(\mathfrak m^n\) can be represented in \(A/\mathfrak m^n\). Essentiality and uniqueness of hulls identify it with \(E\). One cannot replace \(\widehat A\) by \(A\) in (1.2).

**Example 1.5.** For \(A=k[[t]]\),
\[
E=k((t))/k[[t]]=\bigoplus_{j\ge1}kt^{-j}.
\]
Multiplication by every nonzero element of this discrete valuation ring is surjective on \(E\), so Baer's criterion, whose ideals are principal, proves injectivity. Every nonzero submodule meets \(kt^{-1}\), proving essentiality. Here \(E_n\) has basis \(t^{-1},\ldots,t^{-n}\); compatible endomorphisms of these submodules are precisely compatible residues of a power series. This makes (1.2) visible coefficient by coefficient. See [Stacks, [Tag 08Z4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-union-artinian), [Tag 08Z6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-endos), [Tag 08Z7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-injective-hull-has-dcc), [Tag 08Z9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-proposition-matlis)].

## 2. A finite complex that provides duality

**Definition 2.1.** A **dualizing complex** for \(A\) is a complex \(\omega\) with bounded finite cohomology, finite injective dimension, and an isomorphism
\[
A\longrightarrow R\operatorname{Hom}_A(\omega,\omega)
\tag{2.1}
\]
given by scalar multiplication. Finite injective dimension means that \(\omega\) is represented by a bounded complex of injectives. Write \(\mathcal D_\omega(K)=R\operatorname{Hom}_A(K,\omega)\). See [Stacks, [Tag 0A7B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-definition-dualizing)].

We first prove the biduality needed to control uniqueness. This step does not assume local duality.

**Lemma 2.2 (finite-complex biduality).** Evaluation gives \(K\simeq\mathcal D_\omega\mathcal D_\omega K\) for every complex with bounded finite cohomology. Its dual again has bounded finite cohomology.

**Proof.** Choose an injective representative of \(\omega\) in degrees \([a,b]\). For any module \(N\), its dual lies in \([a,b]\). For finite \(N\), its cohomology is finite: a finite free resolution and the bounded finite cohomology of \(\omega\) compute each group using finitely many finite terms. For a bounded finite complex the same assertion follows by truncation triangles.

For a finite module \(N\), both \(\mathcal D_\omega^2N\) and its cohomology lie in a fixed interval \([a-b,b-a]\), independent of \(N\). Evaluation is an isomorphism for a finite free module by (2.1), and hence for every bounded finite free complex. Truncate a finite free resolution of \(N\) far to the left. Its difference from \(N\) is a finite syzygy shifted arbitrarily far to the left. Both that syzygy and its double dual have uniform bounds before shifting. The comparison with the truncated free complex therefore proves evaluation is an isomorphism in any prescribed degree. This proves the result for modules; finitely many truncation triangles prove it for bounded finite complexes. ∎

**Theorem 2.3 (uniqueness).** If \(\omega\) and \(\omega'\) are dualizing complexes, then
\[
\omega'\simeq\omega\otimes_A^{\mathbf L}L,
\]
where \(L\) is locally a rank-one free module placed in one degree. The degree is locally constant. In particular, over a local ring \(L=A[c]\).

**Proof.** Put \(C=R\operatorname{Hom}_A(\omega,\omega')\). The natural map
\[
C\otimes_A^{\mathbf L}K\longrightarrow
\mathcal D_{\omega'}\mathcal D_\omega K
\tag{2.2}
\]
is an isomorphism for bounded finite free complexes. It remains so for finite modules by the truncation argument of Lemma 2.2: the right side has a uniform bounded interval on modules, while the left side has a uniform upper bound, since \(C\) has bounded cohomology and a module has a free resolution in nonpositive degrees. The shifted syzygy errors on both sides eventually lie below any fixed degree. Truncation extends this to bounded finite complexes.

Work locally and let \(V=R\operatorname{Hom}_A(k,\omega)\). It is a bounded finite complex of \(k\)-vector spaces. Biduality and adjunction give
\[
k\simeq R\operatorname{Hom}_k(V,V).
\]
Splitting a vector-space complex into its cohomology shows that this happens only when \(V\) is one-dimensional in a single degree: the degree-zero endomorphism space already has dimension at least the sum of the squares of all nonzero cohomology dimensions. The same holds for \(V'=R\operatorname{Hom}_A(k,\omega')\). Thus (2.2) for \(k\) gives \(C\otimes_A^{\mathbf L}k\simeq k[c]\).

A minimal free resolution of the bounded finite complex \(C\) is bounded above and has finite free terms; removing unit entries from differentials constructs it from any such free resolution. Modulo \(\mathfrak m\) its differentials are zero. The last displayed isomorphism forces exactly one term, of rank one. Hence \(C=A[c]\). For a nonlocal ring this argument applies at each prime; finite cohomology permits shrinking to an open neighborhood on which the one surviving module is invertible and the other groups vanish. Finally, (2.2) with \(K=\omega\), together with \(\mathcal D_\omega\omega=A\), identifies its right side with \(\omega'\) and proves the claimed isomorphism. ∎

**Proposition 2.4 (quotients and localization).** If \(B=A/I\), then
\[
\omega_B=R\operatorname{Hom}_A(B,\omega_A)
\tag{2.3}
\]
is dualizing over \(B\). Localization of a dualizing complex is dualizing.

**Proof.** If \(J\) is a bounded injective representative of \(\omega_A\), then \(\operatorname{Hom}_A(B,J)\) is a bounded complex of injective \(B\)-modules, by restriction–Hom adjunction. Its cohomology is finite by Lemma 2.2. For every finite \(B\)-complex \(K\), that adjunction identifies its dual over \(B\) with \(\mathcal D_{\omega_A}K\). Applying it twice and setting \(K=B\) gives precisely the homothety \(B\simeq R\operatorname{Hom}_B(\omega_B,\omega_B)\).

Over a Noetherian ring a localization of an injective module is injective: Baer's criterion reduces to finitely generated ideals and clearing denominators in their finite presentations. Finite free resolutions compute localization of derived Hom for a bounded finite first argument and a bounded target. Localizing (2.1) therefore proves the last assertion. ∎

Over a local ring, the vector-space argument in Theorem 2.3 gives a unique shift for which \(R\operatorname{Hom}_A(k,\omega)=k[0]\). We call this shift **normalized**. Quotient duality (2.3) preserves normalization when the quotient is local with the same residue field.

**Proposition 2.5 (regular and Gorenstein rings).** A regular local ring of dimension \(n\) has normalized dualizing complex \(A[n]\). Consequently it is Gorenstein. A quotient of a Gorenstein local ring has a dualizing complex. Every complete Noetherian local ring has one.

**Proof.** A regular system of parameters \(x_1,\ldots,x_n\) is a regular sequence, so its Koszul complex resolves \(k\). If \(N\) is finite, take a minimal free resolution. Computing \(\operatorname{Tor}^A_i(k,N)\) instead with the Koszul resolution shows it vanishes for \(i>n\). Minimality then makes the free terms vanish for \(i>n\). Thus all finite modules have projective dimension at most \(n\). In particular \(\operatorname{Ext}^{n+1}_A(A/\mathfrak b,A)=0\) for every ideal. Dimension shifting and Baer's criterion imply \(\operatorname{id}_A A\le n\). The self-dual Koszul complex gives
\[
\operatorname{Ext}^i_A(k,A)=
\begin{cases}k&i=n,\\0&i\ne n.\end{cases}
\]
Homothety for \(A\) is automatic, proving the first assertion.

Here a local ring is called **Gorenstein** when \(A[0]\) is dualizing, equivalently when \(A\) has finite injective dimension. Proposition 2.4 proves the quotient assertion. Cohen's structure theorem presents any complete Noetherian local ring as a quotient of a complete regular local ring, so the last assertion follows as well. Its coefficient construction is the earlier *Coefficient rings and the Cohen structure theorem*, Theorems 4.1–6.1; the structural lemma in *Local cohomology*, Section 6, proves regularity of the complete source and the required dimension and catenarity consequences. ∎

If \(B=A/(f_1,\ldots,f_c)\) for a regular sequence in a regular local ring of dimension \(n\), the Koszul resolution computes
\[
R\operatorname{Hom}_A(B,A[n])=B[n-c].
\tag{2.4}
\]
Thus complete intersections, in particular hypersurfaces, are Gorenstein. This computation also fixes the shift without guessing it from a convention in another source. See [Stacks, [Tag 0A7F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-dualizing-unique), [Tag 0A7G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-dualizing-localize), [Tag 0A7N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-normalized-quotient), [Tag 0AWX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-regular-gorenstein), [Tag 0BFR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-ubiquity-dualizing)].

## 3. Local duality, with completion in the correct place

Choose generators \(f_1,\ldots,f_r\) of \(\mathfrak m\), and let \(C\) be the extended Čech complex of \(A\), with \(A\) in degree zero. Local cohomology gives
\[
R\Gamma_{\mathfrak m}(K)=C\otimes_A^{\mathbf L}K
\tag{3.1}
\]
for every \(K\in D(A)\). The bounded flat complex \(C\) makes this formula valid for unbounded complexes too.

Here is the derived completion convention, including its universal property. A complex \(L\) is **derived complete** if \(R\operatorname{Hom}_A(A_{f_j},L)=0\) for every \(j\). Put
\[
K^\wedge=R\operatorname{Hom}_A(C,K).
\tag{3.2}
\]
The map \(C\to A\) induces \(K\to K^\wedge\). Formula (3.2) is derived completion: it is left adjoint to inclusion of derived complete complexes.

To verify this, \(C\otimes A_{f_j}\) is acyclic, since one factor \([A\to A_{f_j}]\) becomes \([A_{f_j}\to A_{f_j}]\). Tensor–Hom adjunction proves \(K^\wedge\) is complete. In the triangle \(C\to A\to U\), the complex \(U\) is a bounded complex of sums of localizations \(A_{f_{j_1}\cdots f_{j_a}}\), with \(a\ge1\). Thus the fiber of \(K\to K^\wedge\) is \(R\operatorname{Hom}_A(U,K)\), built from complexes on which at least one \(f_j\) acts invertibly. Every such complex has zero derived Hom into a complete complex: for an \(A_{f_j}\)-complex \(P\), restriction–Hom adjunction gives
\[
R\operatorname{Hom}_A(P,L)=
R\operatorname{Hom}_{A_{f_j}}(P,R\operatorname{Hom}_A(A_{f_j},L))=0.
\]
The triangle consequently proves the asserted adjunction. This also shows that the construction is independent of the generators.

Two further descriptions help connect this to ordinary completion. The Čech complex is the homotopy colimit of the cochain Koszul complexes on \(f_1^n,\ldots,f_r^n\) in degrees \(0,\ldots,r\). Dualizing those finite free complexes therefore gives
\[
K^\wedge=R\varprojlim_n
\bigl(K\otimes_A^{\mathbf L}K_\bullet(f_1^n,\ldots,f_r^n)\bigr),
\tag{3.3}
\]
where the homological Koszul complex occupies degrees \(-r,\ldots,0\). This follows directly from the mapping telescope: derived Hom changes its direct-sum triangle into the product triangle defining derived inverse limit. The following lemma proves that, over a Noetherian ring, completion of bounded finite cohomology is its ordinary module completion. The proof checks the inverse-system comparison needed in (3.3). Formula (3.2), rather than an unqualified termwise inverse limit, is our convention for arbitrary complexes.

We will also use a support adjunction, which has a similarly short Čech proof. If all cohomology of \(T\) is \(\mathfrak m\)-power torsion, then \(T_{f_j}=0\). For any \(A_{f_j}\)-complex \(P\), tensor–restriction adjunction gives \(R\operatorname{Hom}_A(T,P)=0\). Tensoring the triangle \(C\to A\to U\) with \(L\) therefore gives
\[
R\operatorname{Hom}_A(T,C\otimes_A^{\mathbf L}L)
\simeq R\operatorname{Hom}_A(T,L).
\tag{3.4}
\]
Thus (3.1) is the right adjoint for torsion complexes. These adjunctions, not any boundedness of \(K\), will prove local duality.

**Lemma (completion of bounded finite cohomology).** Let \(A\) be Noetherian, \(I=(f_1,\ldots,f_r)\), and \(K\in D(A)\) have bounded, finite cohomology. For the completion defined by (3.2),
\[
H^q(K^\wedge)\cong H^q(K)\otimes_A\widehat A
\cong\widehat{H^q(K)}.
\]
The maps are natural and are induced by completion.

**Proof.** The assertion is immediate for the zero ideal. Otherwise choose a bounded-above complex \(P\) of finite free modules representing \(K\). Such a resolution is obtained by lifting finitely many generators of the highest nonzero cohomology, taking the cone, and repeating in the next degree. At every step the next kernel is finite, by Noetherianness. The construction gives a quasi-isomorphism because in each fixed degree its cohomology has been corrected after finitely many steps.

Write \(J_m=(f_1^m,\ldots,f_r^m)\), and write \(Q_m\) for the homological Koszul complex on these generators, in degrees \(-r,\ldots,0\). Its augmentation maps to \(A/J_m\). We check why the negative Koszul cohomology disappears in the inverse system; this is the step that ordinary quotient completion alone would not establish.

Fix \(m\) and a positive homological degree \(j\). Let \(Z_j\) and \(B_j\) be the cycles and boundaries of \(Q_m\). Artin–Rees for the finite submodule \(Z_j\subset (Q_m)_j\) gives \(c\) such that
\[
Z_j\cap I^\ell(Q_m)_j\subset I^{\ell-c}Z_j
\qquad(\ell\ge c).
\]
Each \(f_i^m\) acts null-homotopically on \(Q_m\), by exterior multiplication by its Koszul basis vector. Hence \(J_m\) kills \(Z_j/B_j\). The inclusion
\(I^{r(m-1)+1}\subset J_m\)
then shows that a fixed sufficiently large power of \(I\) takes \(Z_j\) into \(B_j\).

For \(l\ge m\), the transition \(Q_l\to Q_m\) multiplies the basis vector indexed by a nonempty set \(S\) by \(\prod_{i\in S}f_i^{l-m}\). Thus its image in every positive homological degree lies in \(I^{l-m}(Q_m)_j\). Combining this with Artin–Rees shows that, for sufficiently large \(l\), the induced map
\(H_j(Q_l)\to H_j(Q_m)\)
is zero. There are only \(r\) positive degrees, so the same \(l\) works for all of them. In degree zero the augmentation identifies the inverse system exactly with \((A/J_m)\).

It follows that the augmentations induce
\[
R\varprojlim_m(P\otimes_A Q_m)
\simeq R\varprojlim_m(P/J_mP).
\]
Here is the cohomological justification. The augmented Koszul cones have bounded amplitude independent of \(m\), and all their cohomology systems have eventually zero transition maps. Tensoring with \(P\), then filtering by the bounded Koszul direction, gives a finite filtration in every total degree. On its successive pages, the maps on the rows with fixed Koszul cohomology eventually vanish: the maps of their coefficient modules are already zero, before tensoring with any term of \(P\). Finite extensions of such inverse systems again have eventually zero transition maps, by composing sufficiently many transition maps. Thus the total cone has pro-zero cohomology. For a countable pro-zero system, both its inverse limit and its first derived inverse limit vanish. The product-difference description of \(R\varprojlim\), with exact products of modules, therefore makes the derived inverse limit of this cone acyclic.

The system \(P/J_mP\) is onto in each degree. Its derived inverse limit is consequently its termwise inverse limit: the product-difference map is onto in each degree, by recursively lifting coordinates. The ideals \(J_m\) are cofinal with the powers of \(I\), since
\[
J_m\subset I^m,\qquad I^{r(m-1)+1}\subset J_m.
\]
Each term of \(P\) is finite free, so this termwise limit is \(P\otimes_A\widehat A\). Formula (3.3) identifies its left side with \(K^\wedge\). Finally Noetherian completion is flat, and for a finite module tensoring with \(\widehat A\) is ordinary completion, as proved in the earlier Completion lesson. Flatness commutes with the kernels and images computing cohomology, giving the two asserted identifications. ∎

This proves the bounded finite-cohomology case of [Stacks, Tag 0A06](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-derived-completion-pseudo-coherent) used below. The definition (3.2) and its adjunction, already proved above, still apply to arbitrary complexes; the finite-cohomology hypothesis is used to obtain a bounded-above complex of finite free modules. No finite projective dimension is asserted.

**Proposition 3.1.** If \(\omega\) is normalized, then \(R\Gamma_{\mathfrak m}(\omega)=E[0]\).

**Proof.** Set \(\mathcal D=\mathcal D_\omega\). Since \(\mathcal D(k)=k[0]\), exact triangles along a composition series show that \(\mathcal D(L)\) is concentrated in degree zero for every finite-length \(L\), and this degree-zero functor is exact and preserves length.

In particular \(F_n=H^0\mathcal D(A/\mathfrak m^n)\) is the residue-field injective hull over \(A/\mathfrak m^n\). Indeed, quotient adjunction identifies \(R\operatorname{Hom}_{A/\mathfrak m^n}(L,F_n)\) with \(\mathcal D(L)\); its positive cohomology vanishes for every module over this Artinian ring, since all finite modules have finite length and Baer's criterion tests finite ideals. Its socle is \(k\), and every nonzero submodule meets the socle. The quotient maps \(A/\mathfrak m^{n+1}\to A/\mathfrak m^n\) induce injections \(F_n\to F_{n+1}\).

The Ext-colimit computation of local cohomology, applied to a bounded injective representative of \(\omega\), gives
\[
R\Gamma_{\mathfrak m}(\omega)=
\operatorname*{hocolim}_n\mathcal D(A/\mathfrak m^n)=F[0],
\qquad F=\bigcup_n F_n.
\]
This torsion module has essential socle \(k\). Extend its socle inclusion to \(F\to E\). Essentiality makes this injective. By (3.4), \(R\operatorname{Hom}_A(k,F)=R\operatorname{Hom}_A(k,\omega)=k[0]\); in particular \(\operatorname{Ext}^1_A(k,F)=0\). The quotient \(Q=E/F\) is torsion. Applying \(\operatorname{Hom}(k,-)\) shows its socle is zero, since the socles of \(F\) and \(E\) agree and \(\operatorname{Ext}^1(k,F)=0\). A nonzero torsion module has a socle, so \(Q=0\). ∎

**Theorem 3.2 (local duality).** Let \(A\) be Noetherian local with normalized dualizing complex \(\omega\). For every \(K\in D(A)\), there is a natural isomorphism
\[
\boxed{\;
R\operatorname{Hom}_A(K,\omega)^\wedge
\simeq R\operatorname{Hom}_A(R\Gamma_{\mathfrak m}(K),E).
\;}
\tag{3.5}
\]

**Proof.** Substitute (3.2) into the left side and apply tensor–Hom adjunction:
\[
R\operatorname{Hom}_A(C,R\operatorname{Hom}_A(K,\omega))
=R\operatorname{Hom}_A(C\otimes_A^{\mathbf L}K,\omega).
\]
The first argument is torsion. Formula (3.4) lets us replace the second argument by \(R\Gamma_{\mathfrak m}(\omega)\), which is \(E[0]\) by Proposition 3.1. This gives exactly (3.5), with its natural maps. ∎

**Corollary 3.3 (finite-module form).** If \(M\) is finite, then
\[
\widehat{\operatorname{Ext}^{-i}_A(M,\omega)}
\simeq D(H^i_{\mathfrak m}(M)).
\tag{3.6}
\]
Every \(H^i_{\mathfrak m}(M)\) is Artinian. If \(A\) is complete, equivalently
\[
H^i_{\mathfrak m}(M)\simeq
D(\operatorname{Ext}^{-i}_A(M,\omega)).
\tag{3.7}
\]

**Proof.** Lemma 2.2 and exactness of completion on finite cohomology identify the left cohomology of (3.5); injectivity of \(E\) identifies the right. To check Artinianness without presupposing it, let \(N=H^i_{\mathfrak m}(M)\), a torsion module. Its dual is finite over \(\widehat A\) by (3.6). Evaluation \(N\to D(D(N))\) is injective: a nonzero cyclic torsion module has a finite-length quotient detecting its generator, and injectivity of \(E\) extends the resulting map. The target is Artinian by Theorem 1.4 over \(\widehat A\), so \(N\) is Artinian. Evaluation is then an isomorphism by Matlis duality, proving (3.7). ∎

For \(A=k[t]_{(t)}\), a noncomplete discrete valuation ring, \(\omega=A[1]\), whereas \(D(H^1_{(t)}(A))=\widehat A=k[[t]]\). The completion in (3.6) cannot be deleted. Compare [Stacks, [Tag 0A82](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-local-cohomology-of-dualizing), [Tag 0A84](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-theorem-local-duality), [Tag 0AAK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-special-case-local-duality)].

For the complete ring \(k[[t]]\), the same shift gives \(\omega=A[1]\), and the Čech complex \([A\to A_t]\) gives \(H^1_{(t)}(A)=E=k((t))/k[[t]]\). All other supported cohomology groups vanish. Thus the explicit hull of Example 1.5 is also the local-duality image of \(A\) itself.

## 4. Reading depth, dimension and the singularity from the dual

For nonzero finite \(M\), put \(d=\dim\operatorname{Supp}(M)\). The depth theorem and dimension vanishing of Local cohomology, transported through (3.6), give
\[
\operatorname{Ext}^{-i}_A(M,\omega)=0
\quad\text{if }i<\operatorname{depth}M\text{ or }i>d,
\tag{4.1}
\]
and
\[
\operatorname{depth}M=
\min\{i:\operatorname{Ext}^{-i}_A(M,\omega)\ne0\}.
\tag{4.2}
\]
Faithful flatness of completion and faithfulness of the torsion dual justify both the vanishing and the nonvanishing assertions.

The dimension bound in (4.1) also has a proof entirely in terms of finite dual modules. Induct on \(d\). For \(d=0\), finite-length duality places the dual in degree zero. If \(M\) has positive depth, choose a nonzerodivisor \(f\in\mathfrak m\). Its quotient has support dimension \(d-1\). Writing \(Q^j=\operatorname{Ext}^j_A(M,\omega)\) and \(P^j=\operatorname{Ext}^j_A(M/fM,\omega)\), the dual exact sequence gives
\[
Q^j\xrightarrow{f}Q^j\longrightarrow P^{j+1}.
\]
Induction makes the last group zero when \(j<-d\) or \(j>0\). Nakayama then makes \(Q^j=0\) in those degrees. If depth is zero, remove the finite-length module \(\Gamma_{\mathfrak m}(M)\). The quotient has positive depth, unless it is zero, and its dimension is still \(d\) when \(d>0\). The dual exact sequence adds only degree-zero cohomology, proving the same bound for \(M\). Thus the duality proof of dimension vanishing can use this bound directly.

To prove nonvanishing at the other end, and later compare primes in the finiteness theorem, we need a dimension function.

**Lemma 4.1 (dimension function of a dualizing complex).** For a possibly nonlocal \(A\) with dualizing complex \(\omega\), define \(\delta(\mathfrak p)\) by
\[
R\operatorname{Hom}_{A_{\mathfrak p}}(\kappa(\mathfrak p),\omega_{\mathfrak p})
\simeq\kappa(\mathfrak p)[\delta(\mathfrak p)].
\]
This is a bounded integer-valued function. If \(\mathfrak p\subset\mathfrak q\), then
\[
\delta(\mathfrak p)-\delta(\mathfrak q)
=\dim((A/\mathfrak p)_{\mathfrak q}).
\tag{4.3}
\]
For local \(A\) and normalized \(\omega\), \(\delta(\mathfrak m)=0\), so \(\delta(\mathfrak p)=\dim(A/\mathfrak p)\).

**Proof.** Existence follows from the residue-field argument in Theorem 2.3. A bounded injective representative in degrees \([a,b]\) remains injective after localization, so \(-\delta(\mathfrak p)\in[a,b]\); this proves boundedness. Quotient adjunction shows that the function for \(R\operatorname{Hom}_A(A/I,\omega)\) is the restriction of \(\delta\) to \(V(I)\).

It suffices to prove a drop of one for an adjacent pair of primes. Quotient by the smaller prime, localize at the larger, and normalize. The resulting ring \(B\) is a one-dimensional local domain, with fraction field \(F\). Formula (4.1) places its normalized dualizing complex in degrees \(-1,0\). Local cohomology identifies the completion of \(H^{-1}(\omega_B)\) with \(D(H^1_{\mathfrak n}(B))\).

For \(0\ne f\in\mathfrak n\), the only prime containing \(f\) is \(\mathfrak n\); hence \(H^1_{\mathfrak n}(B)=B_f/B\). It is nonzero by the dimension nonvanishing theorem for rings proved in Local cohomology, and multiplication by \(f\) is surjective. If \(H^{-1}(\omega_B)\) had finite length, Matlis duality would make \(H^1_{\mathfrak n}(B)\) finite length. Nakayama would then make it zero, a contradiction. Thus \(H^{-1}(\omega_B)\) has a nonzero generic localization. Over the field \(F\), a dualizing complex has exactly one one-dimensional cohomology group. Its degree must therefore be \(-1\). The normalized closed-point complex has generic shift \([1]\), which says exactly that the original \(\delta\) drops by one along this adjacent specialization.

Every chain can be refined to a saturated chain: boundedness of \(\delta\) bounds its length, so the refinement process terminates. Along any saturated chain from \(\mathfrak p\) to \(\mathfrak q\), its length equals the difference of the two \(\delta\)-values. Taking the supremum over chains proves (4.3). ∎

**Theorem 4.2 (dimension and Cohen–Macaulayness).** For nonzero finite \(M\),
\[
H^d_{\mathfrak m}(M)\ne0,\qquad
\operatorname{Ext}^{-d}_A(M,\omega)\ne0.
\tag{4.4}
\]
The module \(M\) is Cohen–Macaulay if and only if \(R\operatorname{Hom}_A(M,\omega)\) has exactly one nonzero cohomology group, in degree \(-d\). Moreover
\[
\dim\operatorname{Supp}\operatorname{Ext}^{-i}_A(M,\omega)\le i.
\tag{4.5}
\]

**Proof.** Choose a minimal prime \(\mathfrak p\) of \(\operatorname{Supp}M\) with \(\dim(A/\mathfrak p)=d\). The module \(M_{\mathfrak p}\) has nonzero finite length. The normalized complex at that prime is \(\omega_{\mathfrak p}[-\delta(\mathfrak p)]\). Its dual of \(M_{\mathfrak p}\) is nonzero in degree zero, by finite-length duality. Therefore
\[
\operatorname{Ext}^{-d}_A(M,\omega)_{\mathfrak p}\ne0,
\]
since \(\delta(\mathfrak p)=d\). Equations (3.6) and (4.1) prove (4.4). Together with (4.2), they prove the Cohen–Macaulay equivalence: the lower and upper nonvanishing endpoints coincide precisely when depth equals dimension.

If \(\operatorname{Ext}^{-i}_A(M,\omega)_{\mathfrak p}\ne0\), its degree with respect to the normalized complex at \(\mathfrak p\) is \(\delta(\mathfrak p)-i\). Finite-module duals of normalized complexes have no positive cohomology by (4.1) over \(A_{\mathfrak p}\). Hence \(\delta(\mathfrak p)\le i\). Formula (4.3) now bounds \(\dim(A/\mathfrak p)\) by \(i\), giving (4.5). ∎

In particular, \(A\) is Cohen–Macaulay exactly when
\[
\omega\simeq W[d],\qquad W=H^{-d}(\omega),\quad d=\dim A.
\tag{4.6}
\]
The module \(W\) is called the canonical module. It is maximal Cohen–Macaulay: homothety shows its support is all of \(\operatorname{Spec}A\), and \(R\operatorname{Hom}_A(W,\omega)=A[d]\), by applying \(R\operatorname{Hom}(-,\omega)\) to (4.6). Equations (4.2) and (4.4) then give depth \(W=d\).

**Proposition 4.3 (Gorenstein criteria).** For a local ring possessing a normalized dualizing complex, the following are equivalent:

1. \(A\) is Gorenstein.
2. \(\omega\simeq A[d]\), where \(d=\dim A\).
3. \(A\) is Cohen–Macaulay and its canonical module is free of rank one.
4. \(\operatorname{Ext}^i_A(k,A)=0\) for all sufficiently large \(i\).

**Proof.** If \(A\) is dualizing, uniqueness makes \(\omega=A[c]\). The two nonvanishing endpoints in (4.2) and (4.4), applied to \(A\), force \(c=\operatorname{depth}A=d\). The converse follows from finite injective dimension of \(\omega\). Formula (4.6) proves the equivalence with (3). Normalization in (2) gives \(\operatorname{Ext}^i_A(k,A)=0\) for \(i\ne d\), proving (4).

For (4) implies (2), biduality identifies \(A=R\operatorname{Hom}_A(\omega,\omega)\). Tensor–Hom adjunction gives
\[
R\operatorname{Hom}_A(k,A)
=R\operatorname{Hom}_k(k\otimes_A^{\mathbf L}\omega,k).
\tag{4.7}
\]
Here we used \(R\operatorname{Hom}_A(k,\omega)=k[0]\). Eventual Ext vanishing therefore makes \(k\otimes_A^{\mathbf L}\omega\) bounded below. A minimal free resolution of \(\omega\), whose differentials vanish modulo \(\mathfrak m\), must be bounded on both sides. Thus \(\omega\) is perfect. Base change of its homothety now gives
\(k=R\operatorname{Hom}_k(k\otimes\omega,k\otimes\omega)\). The vector-space argument of Theorem 2.3 forces its minimal free resolution to consist of one rank-one term. Thus \(\omega=A[c]\), and the already proved endpoint argument gives \(c=d\). ∎

**Corollary 4.4.** An arbitrary Noetherian local ring is Gorenstein if and only if \(\operatorname{Ext}^i_A(k,A)=0\) for all sufficiently large \(i\).

**Proof.** The forward implication follows from finite injective dimension. For the converse, flat completion and a resolution by finite free modules identify \(\operatorname{Ext}^i_A(k,A)\otimes_A\widehat A\) with \(\operatorname{Ext}^i_{\widehat A}(k,\widehat A)\). The complete ring has a dualizing complex by Proposition 2.5, so Proposition 4.3 makes \(\widehat A\) Gorenstein, with some finite injective-dimension bound \(b\). For every ideal \(I\), the same base change gives
\[
\operatorname{Ext}^{b+1}_A(A/I,A)\otimes_A\widehat A
=\operatorname{Ext}^{b+1}_{\widehat A}(\widehat A/I\widehat A,\widehat A)=0.
\]
Faithful flatness makes the group on the left zero before tensoring. Dimension shifting and Baer's criterion give \(\operatorname{id}_A A\le b\). ∎

For a nonlocal ring with a dualizing complex, Gorensteinness is equivalent to the complex being locally an invertible module in one degree. Its locus is open: near a prime where only one cohomology module survives and is free of rank one, finite presentation lets those conditions persist on an open neighborhood. See [Stacks, [Tag 0A7U](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-sitting-in-degrees), [Tag 0A7Z](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-dimension-function), [Tag 0AWR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-depth-in-terms-dualizing-complex), [Tag 0AWS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-apply-CM), [Tag 0DW9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-gorenstein), [Tag 0BJI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-gorenstein-ext)].

## 5. Turning finiteness into a uniform annihilator

Let \(T\subset\operatorname{Spec}A\) be stable under specialization. For a module \(N\), define
\[
\Gamma_T(N)=\{x\in N:V(\operatorname{Ann}(x))\subset T\},
\qquad H^i_T(N)=R^i\Gamma_T(N).
\]
This includes \(T=V(I)\), where it is ordinary \(I\)-power torsion. Specialization stability makes the displayed set a submodule. It is the filtered union of \(\Gamma_{V(J)}(N)\) over ideals with \(V(J)\subset T\); the union is filtered because \(V(J_1J_2)=V(J_1)\cup V(J_2)\). Exactness of filtered colimits gives
\[
H^i_T(N)=\operatorname*{colim}_{V(J)\subset T}H^i_J(N).
\tag{5.1}
\]
In particular every vector in these modules has cyclic support contained in \(T\).

The functor \(\Gamma_T\) preserves injectives. Indeed, each \(\Gamma_{V(J)}\) does by the proof in Local cohomology, and a filtered union of injectives is injective over a Noetherian ring: a map from a finitely presented ideal factors through one term, where it extends by Baer's criterion. These observations also prove the following two facts used below.

First, localization at \(\mathfrak q\) gives
\[
H^i_T(N)_{\mathfrak q}=H^i_{T_{\mathfrak q}}(N_{\mathfrak q}),
\tag{5.2}
\]
where \(T_{\mathfrak q}\) is the inverse image of \(T\) in \(\operatorname{Spec}A_{\mathfrak q}\). To check cofinality in (5.1), an ideal after localization has finitely many minimal primes. If its closed support is in \(T_{\mathfrak q}\), these primes are localizations of primes in \(T\); their product is an ideal whose global closed support is in \(T\) and whose localized radical is the given radical. Čech computation and flat localization now give (5.2).

Second, for \(\mathfrak q\in T\), composition of the two torsion functors over \(A_{\mathfrak q}\) is closed-point torsion. Preservation of injectives gives the first-quadrant spectral sequence
\[
E_2^{a,b}=H^a_{\mathfrak qA_{\mathfrak q}}
\bigl(H^b_T(M)_{\mathfrak q}\bigr)
\ \Longrightarrow\
H^{a+b}_{\mathfrak qA_{\mathfrak q}}(M_{\mathfrak q}).
\tag{5.3}
\]
It can also be constructed by resolving an injective resolution under the two functors and filtering the resulting double complex. In each total degree only finitely many first-quadrant terms contribute, so the spectral sequence supplies a finite filtration of its abutment. No finiteness of its individual terms is assumed.

**Lemma 5.1 (annihilator test).** For finite \(M\) and \(s\ge0\), the following are equivalent:

1. \(H^i_T(M)\) is finite for \(0\le i\le s\).
2. Some ideal \(J\), with \(V(J)\subset T\), kills all these modules.

For \(T=V(I)\), these are equivalent to the existence of \(e\) such that \(I^eH^i_I(M)=0\) for all \(i\le s\).

**Proof.** A finite module whose support is in \(T\) has annihilator with closed zero set in \(T\). Multiplying the annihilators of finitely many such modules proves (1) implies (2).

For the reverse implication use induction on \(s\). The case \(s=0\) follows from \(H^0_T(M)\subset M\). Remove this finite torsion submodule. It is killed by an ideal \(K\) with \(V(K)\subset T\). In the colimit (5.1), the ideals \(JK\) are cofinal and have zero sets containing \(V(K)\); the removed module is \(JK\)-power torsion, so its positive groups vanish by the Čech complex. Its higher \(T\)-supported cohomology is therefore zero. The quotient \(M'\) has \(\Gamma_T(M')=0\) and the same positive supported cohomology. If \(M'=0\) there is nothing left to prove. Otherwise every associated prime of \(M'\) is outside \(T\). Prime avoidance chooses \(f\in J\) outside these finitely many primes, because \(J\) is contained in none of them. Thus \(f\) is a nonzerodivisor on \(M'\).

In the long exact sequence for \(0\to M'\xrightarrow{f}M'\to M'/fM'\to0\), the multiplication maps on \(H^i_T(M')\) are zero for \(i\le s\). For \(0\le i<s\) we obtain
\[
0\to H^i_T(M')\to H^i_T(M'/fM')
\to H^{i+1}_T(M')\to0.
\tag{5.4}
\]
The middle groups are killed by \(J^2\). Induction makes them finite through degree \(s-1\). Their quotients in (5.4) make all positive groups through degree \(s\) finite, as required.

For the last assertion, \(V(J)\subset V(I)\) means \(I\subset\sqrt J\); finite generation gives \(I^e\subset J\) for some \(e\). Conversely one may take \(J=I^e\). ∎

This test concerns a whole initial range of degrees. A single supported cohomology module killed by an ideal need not be finite. The proof needs the preceding degrees in (5.4). See [Stacks, [Tag 0AW8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/local-cohomology.html#local-cohomology-lemma-check-finiteness-local-cohomology-by-annihilator)].

**Lemma 5.2 (finiteness for a module that is locally free off the support).** Let \(A\) be Noetherian, \(I\subset A\) an ideal and \(n\ge0\). Suppose \(H^i_I(A)\) is finite for every \(0\le i\le n\). If \(M\) is finite and its associated sheaf is locally free on \(\operatorname{Spec}A\setminus V(I)\), then \(H^i_I(M)\) is finite for every \(0\le i\le n\).

**Proof.** Take a presentation
\[
0\longrightarrow K\longrightarrow P\xrightarrow{\pi}M\longrightarrow0
\]
with \(P\) finite free. The module \(K\) is finite. Its extension class \(\xi\) lies in the finite module \(\operatorname{Ext}^1_A(M,K)\). To check finiteness and localization of this Ext module, extend the presentation by two finite free modules and compute degree-one cohomology after applying \(\operatorname{Hom}_A(-,K)\). Kernels and cokernels of these finite modules are finite and commute with localization.

At every prime outside \(V(I)\), the module \(M\) becomes free, so this Ext module becomes zero. A finite module supported in \(V(I)\) is killed by some power \(I^a\): its annihilator has radical containing \(I\), and \(I\) is finitely generated. In particular \(I^a\xi=0\). The connecting homomorphism in
\[
\operatorname{Hom}_A(M,P)\longrightarrow
\operatorname{Hom}_A(M,M)\longrightarrow
\operatorname{Ext}^1_A(M,K)
\]
sends \(u\operatorname{id}_M\) to \(u\xi\). Thus, for each \(u\in I^a\), there is a map \(v_u:M\to P\) such that
\[
\pi v_u=u\operatorname{id}_M.
\]
This lifts each scalar map; it does not assert that the presentation itself splits.

By Lemma 5.1 choose one \(b\) with \(I^bH^i_I(A)=0\) for every \(i\le n\). The same power kills \(H^i_I(P)\), since \(P\) is a finite sum of copies of \(A\). For \(u\in I^a\) and \(w\in I^b\), functoriality gives
\[
wu\,\operatorname{id}_{H^i_I(M)}
=H^i_I(\pi)\,wH^i_I(v_u)=0.
\]
Consequently \(I^{a+b}H^i_I(M)=0\) simultaneously for \(0\le i\le n\). Lemma 5.1 now gives finiteness in this entire initial range. No dualizing complex, completeness or constant rank on the complementary open was required. ∎

In particular, if \((A,\mathfrak m)\) is local of depth at least three and \(M\) is finite and locally free on the punctured spectrum, then \(H^2_{\mathfrak m}(M)\) has finite length. The depth criterion makes \(H^i_{\mathfrak m}(A)=0\) for \(i=0,1,2\), so the lemma gives finiteness. Every local-cohomology element is \(\mathfrak m\)-power torsion; finite generation gives one power killing the whole module. Its filtration by powers of \(\mathfrak m\) has finitely many finite-dimensional residue-field quotients, proving finite length.

This is the finite locally free comparison of [Stacks, Tag 0BPY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/local-cohomology.html#local-cohomology-lemma-local-finiteness-for-finite-locally-free). The proof above uses the obstruction to splitting a finite presentation to obtain its annihilator.

## 6. The annihilator and finiteness theorems

Here is the stronger statement from which finiteness follows. Its extra set \(T'\) allows the annihilator to vanish on a larger locus than the support of local cohomology.

**Theorem 6.1 (Faltings' annihilator theorem with a dualizing complex).** Suppose \(A\) possesses a dualizing complex, \(T\subset T'\subset\operatorname{Spec}A\) are stable under specialization, \(M\) is finite, and \(s\ge0\). The following are equivalent:

1. There is an ideal \(J\) with \(V(J)\subset T'\) such that \(JH^i_T(M)=0\) for every \(i\le s\).
2. For every \(\mathfrak p\notin T'\), \(\mathfrak q\in T\), \(\mathfrak p\subset\mathfrak q\),
\[
\operatorname{depth}_{A_{\mathfrak p}}M_{\mathfrak p}
+\dim((A/\mathfrak p)_{\mathfrak q})>s.
\tag{6.1}
\]
We give depth of the zero localization the value \(+\infty\).

**Proof.** Write \(\omega\) for a dualizing complex, \(\delta\) for Lemma 4.1's bounded dimension function, and
\[
Q^j=\operatorname{Ext}^j_A(M,\omega).
\]
These are finite modules. Local duality over \(A_{\mathfrak q}\), with normalized complex \(\omega_{\mathfrak q}[-\delta(\mathfrak q)]\), says that
\[
\widehat{Q^j_{\mathfrak q}}=
D_{\mathfrak q}\bigl(H^{-\delta(\mathfrak q)-j}_{\mathfrak qA_{\mathfrak q}}(M_{\mathfrak q})\bigr).
\tag{6.2}
\]
Consequently an ideal kills the finite module on the left before completion if and only if it kills the indicated local cohomology module. Faithful flatness and faithfulness of Matlis duality prove this equivalence of annihilators.

We first prove (2) implies (1). Induct on the cohomology degree \(i\le s\). Degree zero is a finite torsion submodule of \(M\), so its annihilator has zero set in \(T\subset T'\). Suppose an ideal \(J'\) with zero set in \(T'\) already kills all groups in degrees less than \(i\).

Within this step, descend through the finitely many possible values of \(\delta\). Put \(T_n=\{\mathfrak q\in T:\delta(\mathfrak q)\le n\}\). We construct an ideal \(J\), with \(V(J)\subset T'\), such that
\[
\operatorname{Ass}_A(JH^i_T(M))\subset T_n.
\tag{6.3}
\]
For \(n\) above all \(\delta\)-values, \(J=A\) works. Descending below all those values will make \(JH^i_T(M)=0\): every nonzero module over a Noetherian ring has an associated prime, by maximizing an element's annihilator.

Assume (6.3) at level \(n\). We need an ideal \(J''\), with zero set in \(T'\), which kills
\[
H^i_{\mathfrak qA_{\mathfrak q}}(M_{\mathfrak q})
\quad\text{for every }\mathfrak q\in T\text{ with }\delta(\mathfrak q)=n.
\tag{6.4}
\]
We construct it uniformly, rather than choosing separate unrelated annihilators at each point. By (6.2), it suffices to kill \(Q^{-n-i}_{\mathfrak q}\).

Fix one such \(\mathfrak q\). For \(\mathfrak p\subset\mathfrak q\) outside \(T'\), the normalized local dual at \(\mathfrak p\) relates \(Q^{-n-i}_{\mathfrak p}\) to
\[
H^{i+n-\delta(\mathfrak p)}_{\mathfrak pA_{\mathfrak p}}(M_{\mathfrak p})
=H^{i-\dim((A/\mathfrak p)_{\mathfrak q})}_{\mathfrak pA_{\mathfrak p}}(M_{\mathfrak p}).
\]
Its degree is below depth by (6.1) and \(i\le s\), so it vanishes. Thus the support of the finite module \(Q^{-n-i}_{\mathfrak q}\) is contained in \(T'\) after localization.

Here is why this supplies a global ideal with the required zero set. Take the finitely many minimal primes of \(\operatorname{Ann}_A Q^{-n-i}\) that are contained in \(\mathfrak q\). They belong to \(T'\). Their product has global zero set in \(T'\), and its localization is the radical of the localized annihilator. A sufficiently large power therefore kills \(Q^{-n-i}_{\mathfrak q}\). If there are no such primes, take the unit ideal. Since \(Q^{-n-i}\) is finite, the same ideal kills it on an open neighborhood of \(\mathfrak q\). The layer \(\{\mathfrak q\in T:\delta(\mathfrak q)=n\}\), with the induced topology, is a subspace of a Noetherian space and is quasi-compact. Finitely many neighborhoods suffice. The product of their ideals has zero set in \(T'\) and kills every localization in (6.4). This is \(J''\).

Now apply (5.3) at a point \(\mathfrak q\) of this layer. In the first column the pages form a decreasing sequence
\[
E_2^{0,i}\supset E_3^{0,i}\supset\cdots\supset E_{i+2}^{0,i}=E_\infty^{0,i}.
\]
There are no incoming differentials. Each successive quotient injects into the target of an outgoing differential, a subquotient of
\(H^r_{\mathfrak q}(H^{i-r+1}_T(M)_{\mathfrak q})\) for \(2\le r\le i+1\). It is killed by \(J'\), since \(i-r+1<i\). The last page is a subquotient of the abutment \(H^i_{\mathfrak q}(M_{\mathfrak q})\), killed by \(J''\). Hence
\[
(J')^iJ''E_2^{0,i}=0.
\tag{6.5}
\]
The module \((JH^i_T(M))_{\mathfrak q}\) is closed-point torsion. Indeed its associated primes before localization are in \(T_n\), whereas a strict generization of \(\mathfrak q\) has larger \(\delta\). A nonzero localization away from the closed point would have an associated prime there, contradicting (6.3). Each cyclic submodule therefore has closed-point support. Thus this module lies in \(E_2^{0,i}=H^0_{\mathfrak q}(H^i_T(M)_{\mathfrak q})\). Equation (6.5) kills it. Multiplying \(J\) by \((J')^iJ''\) removes all associated primes of value \(n\) and preserves (6.3) for the lower layer. The descending induction terminates and produces an annihilator of \(H^i_T(M)\). Multiply it by \(J'\) to kill all degrees through \(i\). This proves (1).

For the converse, suppose \(J\) as in (1) exists, but take a violating pair and put
\[
h=\operatorname{depth}M_{\mathfrak p},\quad
c=\dim((A/\mathfrak p)_{\mathfrak q}),\quad i=h+c\le s,\quad n=\delta(\mathfrak q).
\]
The depth theorem and (6.2) make \(Q^{-n-i}_{\mathfrak p}\ne0\), since its normalized degree is \(-h\): formula (4.3) gives \(\delta(\mathfrak p)=n+c\).

On the other hand, every \(E_2^{a,b}\) of (5.3) with \(a+b=i\) is killed by \(J\), because \(b\le i\le s\). Its abutment has a filtration of length at most \(i+1\), so \(J^{i+1}\) kills \(H^i_{\mathfrak q}(M_{\mathfrak q})\). Equation (6.2) says it kills \(Q^{-n-i}_{\mathfrak q}\) as well. Localize again at \(\mathfrak p\). Since \(\mathfrak p\notin T'\) and \(V(J)\subset T'\), \(J_{\mathfrak p}\) is the unit ideal. This forces \(Q^{-n-i}_{\mathfrak p}=0\), the contradiction. ∎

The proof has two distinct finite controls: the dual Ext modules give finitely many neighborhoods on each dimension layer, and the dimension function gives finitely many layers. Neither control requires local cohomology itself to be finite. See [Stacks, [Tag 0EFC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/local-cohomology.html#local-cohomology-proposition-annihilator)].

**Theorem 6.2 (finiteness).** Let \(A\) be Noetherian with a dualizing complex, \(T\) stable under specialization, \(M\) finite, and \(s\ge0\). Then \(H^i_T(M)\) is finite for every \(i\le s\) if and only if
\[
\operatorname{depth}M_{\mathfrak p}
+\dim((A/\mathfrak p)_{\mathfrak q})>s
\]
for all \(\mathfrak p\notin T\), \(\mathfrak q\in T\), \(\mathfrak p\subset\mathfrak q\).

**Proof.** Set \(T'=T\) in Theorem 6.1 and apply Lemma 5.1. ∎

For closed support define the **finiteness cutoff**
\[
f_I(M)=\inf_{\substack{\mathfrak p\notin V(I),\ \mathfrak q\in V(I)\\
\mathfrak p\subset\mathfrak q}}
\bigl(\operatorname{depth}M_{\mathfrak p}
+\dim((A/\mathfrak p)_{\mathfrak q})\bigr),
\tag{6.6}
\]
with the infimum of an empty set equal to \(+\infty\). In a Gorenstein local ring the theorem applies, since \(A\) itself is dualizing. For any finite \(M\), all \(H^i_I(M)\) with \(i<f_I(M)\) are finite; if the cutoff is finite, \(H^{f_I(M)}_I(M)\) is not finite. The latter assertion follows by applying the theorem at the cutoff: lower degrees are already finite, so the failure is in that degree. A cutoff of infinity means every degree is finite, and has no “degree at infinity.” Nor does a finite cutoff assert that every later degree is infinite: dimension vanishing still makes sufficiently high groups zero. Compare [Stacks, [Tag 0EFD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/local-cohomology.html#local-cohomology-proposition-finiteness), [Tag 0BJU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/local-cohomology.html#local-cohomology-lemma-local-annihilator)].

**Example 6.3.** For \(A=k[[x,y,z]]\), \(I=(x)\), \(M=A\), the pair \((0)\subset(x)\) gives cutoff one, and every eligible pair has positive interval dimension. Thus \(H^0_I(A)=0\) is finite, but \(H^1_I(A)=A_x/A\) is not finite. It is also visibly nonfinite: multiplication by \(x\) is surjective and the module is nonzero, so finiteness would contradict Nakayama. If instead \(I=\mathfrak m\), Cohen–Macaulayness of every regular localization and the dimension formula make every eligible sum equal to three. Only \(H^3_{\mathfrak m}(A)\) is nonzero, and it is not finite. Finally \(I=0\) gives \(T=\operatorname{Spec}A\), cutoff infinity and \(H^0_T(M)=M\), with all positive groups zero.

### Completion and the closed-support theorem

For closed support the dualizing-complex hypothesis can be replaced by universal catenarity and Cohen–Macaulay formal fibres. Completion supplies the dualizing complex, but we must also compare the numerical cutoff and descend finiteness. We prove these steps, including the branch-dimension statement used in that comparison.

**Lemma 6.4 (locality of a finite initial range).** Let \(A\) be Noetherian, \(I\subset A\), \(M\) finite and \(n\ge0\). The modules \(H^i_I(M)\), \(0\le i\le n\), are finite if and only if their localizations at every prime are finite over the corresponding local rings.

**Proof.** Only the reverse direction needs proof. Induct on \(n\); degree zero is a submodule of \(M\). Remove \(\Gamma_I(M)\), whose higher local cohomology is zero, as in Lemma 5.1. The quotient has zero \(I\)-torsion and the same positive local cohomology. If it is zero, the assertion follows. Otherwise prime avoidance gives an element \(f\in I\) regular on this quotient: no associated prime contains \(I\), since such a prime would give a nonzero \(I\)-torsion element. Rename the quotient \(M\).

The sequence for multiplication by \(f\), localized at any prime, makes \(H^i_I(M/fM)\) locally finite for \(i<n\). Induction makes these modules finite globally. For \(1\le i\le n\), the kernel of multiplication by \(f\) on \(N_i=H^i_I(M)\) is therefore finite, being an image of \(H^{i-1}_I(M/fM)\). Every associated prime of \(N_i\) contains \(I\): an element realizing that associated prime is killed by a power of \(I\). It is thus killed by \(f\), so that associated prime belongs to the finite associated-prime set of \(\ker(f:N_i\to N_i)\). Hence \(\operatorname{Ass}N_i\) is finite.

For any module \(N\) over a Noetherian ring, the map
\[
N\longrightarrow\prod_{\mathfrak p\in\operatorname{Ass}N}N_{\mathfrak p}
\]
is injective. Indeed, a nonzero cyclic submodule contains an element with prime annihilator; localization at that prime does not kill it, and therefore does not kill its original generator. Each \((N_i)_{\mathfrak p}\) in this finite product is finite and \(I\)-power torsion by hypothesis, so a power of \(I\) kills it. One exponent works for all the finitely many primes and degrees. The injection shows that this power kills all \(N_i\) in the initial range. Lemma 5.1 gives their global finiteness. The removed degree-zero torsion was finite already. ∎

We next isolate a finite algebraization argument. All the Hom and Ext groups used in it are computed from finite free prefixes of resolutions; these are the constructions in Resolutions, Tor and Ext, Theorem 1.1 and Section 4.

**Lemma 6.5 (algebraizing an isolated finite modification).** Let \((A,\mathfrak m)\) be Noetherian local and \(B=\widehat A\). Suppose \(E\) is a finite commutative \(B\)-algebra, \(B\to E\) is injective and \(Q=E/B\) has finite length. Then there is a finite commutative \(A\)-algebra \(D\), containing \(A\), and an isomorphism \(D\otimes_A B\simeq E\) respecting the included copy of \(B\).

**Proof.** A finite-length \(B\)-module is also a finite-length \(A\)-module, because \(A/\mathfrak m^s=B/\mathfrak m^sB\). For any finite-length \(P\) and finite \(A\)-module \(L\), the modules \(\operatorname{Hom}_A(P,L)\) and \(\operatorname{Ext}^1_A(P,L)\) are finite and vanish away from \(\mathfrak m\). They therefore have finite length and are already complete. Finite free prefixes and flatness of \(B\) identify their tensors with the corresponding Hom and Ext over \(B\). Thus completion induces isomorphisms on these Hom and Ext groups themselves.

Here the extension interpretation of \(\operatorname{Ext}^1\) can be seen directly: for a free presentation \(0\to K\to P_0\to Q\to0\), push out \(K\to P_0\) along a map \(K\to L\). Every extension is obtained this way by lifting \(P_0\) into its middle module. Two such extensions are equivalent exactly when the maps \(K\to L\) differ by the restriction of a map \(P_0\to L\). This is the cokernel computing \(\operatorname{Ext}^1_A(Q,L)\), and the construction commutes with flat base change.

Apply the comparison to \(P=Q\), \(L=A\). The class of \(0\to B\to E\to Q\to0\) comes from an extension of finite \(A\)-modules
\[
\begin{array}{ccccccccc}
0&\longrightarrow&A&\longrightarrow&D&\longrightarrow&Q&\longrightarrow&0\\
&&\downarrow&&\downarrow&&\Vert\\
0&\longrightarrow&B&\longrightarrow&E&\longrightarrow&Q&\longrightarrow&0.
\end{array}
\]
Its completed row is the specified bottom row. This gives the module \(D\) and its element \(1\), the image of \(1\in A\). It remains to algebraize multiplication, rather than assume that a module algebraization has one.

Let \(S\subset D\otimes_A D\) be the image of
\((x,y)\mapsto1\otimes x+y\otimes1\).
On \(S\) the required product must send this image to \(x+y\). This rule is well defined: a relation in its source maps after completion to a relation killed by multiplication in \(E\), and faithful flatness then says that its proposed value in \(D\) is zero. Write this map as \(\lambda:S\to D\). The quotient \(P=(D\otimes D)/S\) has finite length, since \(D=A\) away from the closed point.

The obstruction to extending \(\lambda\) to \(D\otimes D\) is its image in \(\operatorname{Ext}^1_A(P,D)\). It becomes zero after completion, because multiplication in \(E\) extends it. The Ext isomorphism just proved makes this obstruction zero over \(A\). Choose an extension \(\mu_0:D\otimes D\to D\). The difference between its completion and the specified product on \(E\) vanishes on \(S\otimes B\), hence factors through \(P\otimes B=P\). The Hom isomorphism for \(P,D\) descends that difference to a map \(P\to D\). Correcting \(\mu_0\) by this map gives a product whose completion is exactly the product of \(E\).

Associativity, commutativity and the unit equations now hold over \(A\), because the differences of their module maps vanish after the faithfully flat tensor product with \(B\). Thus \(D\) is the asserted algebra. ∎

**Example (separating the branches of a node).** Put \(A=k[x,y]_{(x,y)}/(xy)\). The two quotient maps give
\[
0\longrightarrow A\longrightarrow
D=k[y]_{(y)}\times k[x]_{(x)}
\xrightarrow{(g,h)\mapsto g(0)-h(0)}k\longrightarrow0.
\]
Indeed an element of the nodal ring is exactly a pair of local functions with the same residue at the intersection. This follows from the exact ideal sequence for \((x)\) and \((y)\), whose intersection is zero in \(A\). The two factors of \(D\) are cyclic \(A\)-modules, so the algebra is finite. Completion gives \(B=k[[x,y]]/(xy)\) and \(E=k[[y]]\times k[[x]]\), with \(E/B=k\). Thus the modification separates two branches and changes the algebra only at the closed point. The finite-length quotient in Lemma 6.5 measures this defect; the algebra itself need not be local.

**Lemma 6.6 (dimensions of completed branches).** If \(A\) is a universally catenary Noetherian local ring and \(\mathfrak p\) is prime, then \(\widehat A/\mathfrak p\widehat A\) is equidimensional of dimension \(\dim(A/\mathfrak p)\).

**Proof.** Quotients of universally catenary rings are universally catenary, and completion commutes with finite quotients. It suffices to prove that the completion \(B\) of a universally catenary local domain \(A\), of dimension \(d\), is equidimensional of dimension \(d\). Completion preserves dimension. We argue by induction on \(d\). For \(d=0\) the domain is a field. For \(d=1\), every minimal prime of the positive-dimensional local ring \(B\) is strictly below its maximal ideal, so its quotient has dimension one. These cases give the assertion.

We first explain the dimension count for a finite \(A\)-algebra \(F\). If \(\mathfrak n\) is maximal above \(\mathfrak m\) with residue field \(\kappa(\mathfrak m)\), and \(\mathfrak a\subset\mathfrak n\) contracts to zero, then
\[
\dim(F/\mathfrak a)_{\mathfrak n}=d.
\tag{6.7}
\]
Present the finite domain \(F/\mathfrak a\) as \(A[T_1,\ldots,T_s]/P\), with \(Q\) the inverse image of \(\mathfrak n\). Over \(K=\operatorname{Frac}A\), its quotient is a finite domain over \(K\), hence a field. Its coordinate images are algebraic over \(K\). Contract its maximal ideal successively to \(K[T_1,\ldots,T_i]\): each quotient is a finite field extension, and extending these contracted ideals back to the full polynomial ring gives a strict chain of length \(s\). The polynomial dimension bound gives height exactly \(s\). Primes below \(P\) all contract to zero, so localization to \(K\) preserves their entire interval and \(\operatorname{ht}P=s\). The flat local dimension formula in Dimension theory of Noetherian local rings, Theorem 5.1, gives
\(\dim A[T]_{Q}=d+s\), since its closed fibre is a polynomial local ring at a rational closed point, of dimension \(s\). Universal catenarity makes \(A[T]_{Q}\) catenary. Concatenating saturated chains from \((0)\) to \(P\) and from \(P\) to \(Q\) gives (6.7). The field polynomial height formula is proved in the earlier Krull dimension and Noether normalization lesson; no perfectness is used.

Suppose now that \(B\) has a component \(V(\mathfrak q)\) of minimal dimension \(e<d\). Its dimension is positive, since a minimal prime equal to the maximal ideal would make a local ring zero-dimensional. Every minimal prime of \(B\) contracts to zero by flat going down.

If \(e=1\), choose \(a\ne0\) in \(\mathfrak m\). It remains a nonzerodivisor in \(B\), so \(B\) has no nonzero finite-length submodule. The zero-dimensional local ring \(B_{\mathfrak q}\) is Artinian, so for some \(t\), the ideal \(J=\mathfrak q^t\) has \(J_{\mathfrak q}=0\). On the punctured spectrum \(J\) is either zero, at \(\mathfrak q\), or the unit ideal: any other prime containing \(\mathfrak q\) would have to be the closed point of its one-dimensional component. Consequently
\[
B\longrightarrow E=B/J\times B/\operatorname{Ann}_B(J)
\]
is an isomorphism off the closed point. Its kernel and cokernel have finite length. Its kernel is zero by the nonzerodivisor observation. Lemma 6.5 gives a finite \(A\)-algebra \(F\) completing to \(E\).

The first factor \(B/J\) is local, has residue field \(\kappa(\mathfrak m)\), and has dimension one. It is the completion of \(F_{\mathfrak n}\) for the corresponding maximal ideal \(\mathfrak n\) of \(F\). To see this directly, each Artinian quotient \(F/\mathfrak m^lF\) splits into its finitely many local factors by the Chinese remainder theorem. Their compatible inverse limits are the factors of \(F\otimes B\). At a selected maximal ideal, its maximal-ideal topology and its \(\mathfrak m\)-adic topology are cofinal, since both ideals have the same radical in a Noetherian ring. Thus this factor is the local completion.

The composite \(F\to B/J\to B/\mathfrak q\) has a prime kernel \(\mathfrak a\subset\mathfrak n\) contracting to zero. Formula (6.7) forces \(\dim F_{\mathfrak n}\ge d\), whereas its completion has dimension one. This contradicts \(e=1<d\).

If \(e>1\), let \(Z\) be the union of the other components of \(\operatorname{Spec}B\). Its intersection with \(V(\mathfrak q)\) has finitely many components; let \(\mathfrak r_j\) be those of positive dimension. Their contractions to \(A\) are nonmaximal, since the closed fibre of \(A\to B\) has only its closed point. Prime avoidance chooses a nonzero \(f\in\mathfrak m\) outside all these contractions.

The complete local domain \(B/\mathfrak q\) is catenary, by the structural lemma of Local cohomology. Thus every prime \(P\) minimal over \((\mathfrak q,f)\) has quotient dimension \(e-1\). Such a \(P\) lies on no other component. Indeed, if it contained another minimal prime, it would contain one of the \(\mathfrak r_j\). A proper containment lowers quotient dimension, while every intersection component has dimension at most \(e-1\). Hence that \(\mathfrak r_j\) would equal \(P\), contrary to \(f\notin\mathfrak r_j\). The zero-dimensional intersection components cannot contain \(P\), since \(e-1>0\). Therefore \(P\) is minimal over \(fB\), and gives a component of \(B/fB\) of dimension \(e-1<d-1\).

On the other hand every minimal prime \(\mathfrak p\) of \(A/fA\) has \(\dim A/\mathfrak p=d-1\): the principal ideal theorem gives height one, and catenarity of the local domain gives the remaining chain length. Each \(A/\mathfrak p\) is universally catenary of smaller dimension. By induction its completion is equidimensional of dimension \(d-1\). Flat going down for \(A/fA\to B/fB\) makes every minimal prime of the latter lie over such a minimal \(\mathfrak p\). It is then a minimal prime of \(B/\mathfrak pB\), so all these components have dimension \(d-1\). This contradicts the component just constructed and finishes the induction. ∎

We will use one consequence of the chain argument. In a catenary equidimensional local ring \(R\) of dimension \(d\),
\[
\dim R_P+\dim R/P=d.
\tag{6.8}
\]
For each minimal prime \(\mathfrak a\subset P\), concatenate a saturated chain to \(P\) with one from \(P\) to the maximal ideal in \(R/\mathfrak a\). Equidimensionality makes their total length \(d\); catenarity makes the first length \(d-\dim R/P\), independently of \(\mathfrak a\). Taking the maximal such length gives \(\dim R_P\). This proves (6.8), including rings with nilpotents or embedded associated primes.

**Lemma 6.7 (depth under a flat local map).** Let \((A,\mathfrak m)\to(S,\mathfrak n)\) be a flat local map of Noetherian local rings, and let \(M\ne0\) be finite over \(A\). For \(F=S/\mathfrak mS\),
\[
\operatorname{depth}_S(M\otimes_A S)
=\operatorname{depth}_A M+\operatorname{depth}F.
\tag{6.9}
\]

**Proof.** Recall why the first nonzero cohomology of the cochain Koszul complex on generators of the maximal ideal is depth. At depth zero its degree-zero cohomology is the nonzero socle. For positive depth choose a regular element \(f\) in that ideal. Appending \(f\) does not change the least nonzero degree: multiplication by \(f\), a linear combination of the generators, is null-homotopic on their Koszul complex, so adjoining its factor gives the direct sum of that complex and its shift by \([-1]\). Computing the \(f\)-factor first instead gives the Koszul complex of \(M/fM\), shifted by \([-1]\), because \(f\) is regular. The regular-element depth drop, proved in the earlier depth lesson, now proves the assertion by induction.

Choose generators \(x\) of \(\mathfrak m\) and lifts \(y\) of generators of the maximal ideal of \(F\); together they generate \(\mathfrak n\). Flatness identifies the cohomology of \(K^\bullet(x;M)\otimes_A S\) with \(H^j(K^\bullet(x;M))\otimes_A S\). Each coefficient module is a finite-dimensional residue-field vector space, since every \(x_i\) acts null-homotopically. Thus this cohomology is a finite free \(F\)-module, zero for \(j<a=\operatorname{depth}_A M\) and nonzero at \(a\).

The double Koszul complex on \((x,y)\) has spectral sequence
\[
E_2^{i,j}=H^i(K^\bullet(y;F))^{\beta_j}
\ \Longrightarrow\ H^{i+j}(K^\bullet(x,y;M\otimes_A S)),
\]
where \(\beta_j\) is that residue-field dimension. Put \(b=\operatorname{depth}F\). All terms with \(i<b\) or \(j<a\) are zero; the term \((b,a)\) is nonzero and no differential can enter or leave it. The bounded double complex converges, so its first nonzero total cohomology has degree \(a+b\). The Koszul criterion just proved gives (6.9). ∎

**Proposition 6.8 (the cutoff is unchanged by completion).** Suppose \(A\) is Noetherian local and universally catenary, and all its formal fibres are Cohen–Macaulay. Put \(B=\widehat A\), \(I_B=IB\), \(M_B=M\otimes_A B\). Then
\[
f_I(M)=f_{I_B}(M_B).
\tag{6.10}
\]

**Proof.** For a finite contribution to the infimum (6.6), consider primes \(P\subset Q\) of \(B\), with \(P\notin V(I_B)\), \(Q\in V(I_B)\), and contractions \(\mathfrak p\subset\mathfrak q\). Write
\[
a=\dim A/\mathfrak p,\quad b=\dim A/\mathfrak q,\quad
a'=\dim B/P,\quad b'=\dim B/Q,
\]
and let
\[
u=\dim(B_P/\mathfrak pB_P),\qquad
v=\dim(B_Q/\mathfrak qB_Q).
\]
Lemma 6.6 and (6.8), applied to the complete local quotients \(B/\mathfrak pB\) and \(B/\mathfrak qB\), give
\(a=a'+u\) and \(b=b'+v\).
These quotients are catenary by the structural lemma in Local cohomology.

The local ring \(B_P/\mathfrak pB_P\) of a formal fibre is Cohen–Macaulay. Lemma 6.7 therefore gives
\(\operatorname{depth}(M_B)_P=\operatorname{depth}M_{\mathfrak p}+u\).
Catenarity of the local domains \(A/\mathfrak p\) and \(B/P\) identifies their interval dimensions with \(a-b\) and \(a'-b'\). Consequently the two contributions satisfy
\[
\begin{aligned}
\operatorname{depth}(M_B)_P+\dim(B/P)_Q
&=\operatorname{depth}M_{\mathfrak p}+u+a'-b'\\
&=\operatorname{depth}M_{\mathfrak p}+a-b+v\\
&\ge f_I(M).
\end{aligned}
\tag{6.11}
\]
Thus the completed cutoff is no smaller. Zero localizations of \(M\) have depth \(+\infty\) and make no finite contribution; flat local faithful descent preserves this convention.

Conversely take an eligible pair \(\mathfrak p\subset\mathfrak q\) in \(A\). Choose \(Q\) minimal over \(\mathfrak qB\). It contracts to \(\mathfrak q\) by flat going down. Again going down, followed by taking a minimal prime over \(\mathfrak pB\) below it, gives \(P\subset Q\) minimal over \(\mathfrak pB\) and contracting to \(\mathfrak p\). Both fibre dimensions \(u,v\) are zero. Formula (6.11) is then equality with the contribution of this original pair. Taking infima gives the other inequality. This also handles cutoff infinity: if every original contribution is infinite, (6.11) forbids a finite completed contribution. ∎

**Theorem 6.9 (closed-support finiteness with Cohen–Macaulay formal fibres).** Let \(A\) be Noetherian and universally catenary. Assume that the formal fibres of every local ring of \(A\) are Cohen–Macaulay. For every ideal \(I\) and finite \(M\),
\[
H^i_I(M)\text{ is finite for every }0\le i<f_I(M).
\]
If \(f_I(M)<\infty\), then \(H^{f_I(M)}_I(M)\) is not finite. If \(f_I(M)=+\infty\), all the groups are finite.

**Proof.** First let \(A\) be local. Its completion \(B\) has a dualizing complex: the structural lemma of Local cohomology gives a complete regular source, and Proposition 2.4 gives the dualizing complex on its quotient. Theorem 6.2 proves all the asserted finiteness and nonfiniteness statements over \(B\). Proposition 6.8 identifies the cutoffs. Flat Čech base change gives
\[
H^i_I(M)\otimes_A B=H^i_{IB}(M\otimes_A B).
\]
Finiteness descends faithfully flatly even for a module not known in advance to be finite: take finitely many elements whose tensors span the completed module, and apply faithful flatness to the cokernel of their span. The converse is immediate, so nonfiniteness descends as well. This proves the local case.

In general localization preserves universal catenarity, and the hypothesis supplies the required formal fibres at every \(A_{\mathfrak r}\). The eligible pairs in its cutoff are precisely the original pairs lying below \(\mathfrak r\), with the same depths and interval dimensions. Hence
\[
f_I(M)=\inf_{\mathfrak r\in\operatorname{Spec}A}
f_{IA_{\mathfrak r}}(M_{\mathfrak r}).
\tag{6.12}
\]
One inequality follows by restricting the eligible pairs. For the other, each original pair occurs after localizing at its upper prime.

For any integer \(n<f_I(M)\), the local case makes every localization of \(H^i_I(M)\), \(i\le n\), finite. Lemma 6.4 makes the whole initial range finite over \(A\). If the cutoff is finite, its infimum is attained, since the finite contributions are nonnegative integers. Localize at the upper prime of an attaining pair. Its local cutoff is the same integer by (6.12), so the local theorem makes the group in that degree nonfinite. The global group therefore cannot be finite. If the cutoff is infinite, the first argument applies to every finite \(n\), proving finiteness in every degree. Unit and zero ideals have no eligible pairs and obey the same convention. ∎

Theorem 6.9 is the closed-support theorem of [Stacks, Tag 0BJV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/local-cohomology.html#local-cohomology-theorem-finiteness). It does not assert the more general specialization-closed conclusion without a dualizing complex, nor nonfiniteness in all degrees above the first nonfinite one. The local-to-global argument, the completed-branch dimension argument and the exact fibre contributions in (6.11) explain why its stated hypotheses are needed in this proof.

### Formal sections and supported cohomology

There is a useful consequence of the annihilator theorem which concerns a neighbourhood of a closed set, rather than just its infinitesimal thickenings. The distinction matters when a component can approach the closed point without meeting the rest of the closed set. We prove the supported-cohomology comparison first, so that it can also be used in the next lesson's connectedness argument.

In this subsection \((A,\mathfrak m)\) is Noetherian local, \(I\subset\mathfrak m\), and \(A\) is \(I\)-adically complete and has a dualizing complex. Normalize the latter at \(\mathfrak m\). Write \(X=\operatorname{Spec}A\), \(Y=V(I)\), \(U=X\setminus\{\mathfrak m\}\), and
\[
T=\{\mathfrak p:V(\mathfrak p)\cap Y=\{\mathfrak m\}\}.
\]
This set is stable under specialization and meets \(Y\) only at the closed point. Choose an integer \(d\ge0\) such that \(H^i_I(A)=0\) for \(i>d\). The least such integer is the cohomological dimension \(\operatorname{cd}(A,I)\).

**Lemma 6.10 (three depth tests).** For finite \(M\), put
\(g_M(\mathfrak p)=\operatorname{depth}M_{\mathfrak p}+\dim(A/\mathfrak p)\), with value infinity at zero stalks.

1. The function \(g_M\) is lower semicontinuous. Near a point \(\mathfrak p\) in its support, its restriction to \(V(\mathfrak p)\) is constant. At a proper specialization in that neighbourhood, depth is therefore strictly larger than at \(\mathfrak p\).
2. If \(S\) is stable under specialization and \(\operatorname{depth}M_{\mathfrak p}>s\) for all \(\mathfrak p\in S\), then \(H^i_S(M)=0\) for \(i\le s\). If \(Z\subset S\) is closed and this depth bound holds on \(S\setminus Z\), then \(H^i_Z(M)\to H^i_S(M)\) is an isomorphism for \(i\le s\).
3. Every module \(N\) satisfies \(H^i_I(N)=0\) for \(i>d\). Consequently \(\dim(A/\mathfrak p)\le d\) for \(\mathfrak p\in T\).

**Proof.** Put \(Q^j=\operatorname{Ext}^j_A(M,\omega)\). These are finitely many nonzero finite modules. Local duality (6.2) and the first-nonvanishing depth criterion give
\[
g_M(\mathfrak p)=-\max\{j:Q^j_{\mathfrak p}\ne0\}.
\]
Thus \(g_M\le n\) is a finite union of closed supports. If \(j_0\) is the maximum at \(\mathfrak p\), remove the supports of the finitely many \(Q^j\), \(j>j_0\), which miss \(\mathfrak p\). The support of \(Q^{j_0}\) contains all of \(V(\mathfrak p)\). Hence \(g_M\) is constant there in the resulting neighbourhood. Formula (4.3) shows that \(\dim(A/\mathfrak q)\) drops strictly at a proper specialization \(\mathfrak q\) of \(\mathfrak p\); depth must increase by the same amount. This proves 1.

For 2, suppose the first nonzero group in the forbidden range were \(H^k_S(M)\). Choose an associated prime \(\mathfrak q\) of this module. Its cyclic support is in \(S\), so \(\mathfrak q\in S\). Localizing (5.3), its nonzero socle gives a nonzero \(E_2^{0,k}\). No differential enters the first column, and every outgoing differential has second index less than \(k\), where the groups vanish. It survives to a nonzero subgroup of \(H^k_{\mathfrak qA_{\mathfrak q}}(M_{\mathfrak q})\), contrary to the depth bound. This proves vanishing. For the comparison, restrict to \(X\setminus Z\). The same argument on every distinguished affine open makes the local-cohomology sheaves with support in \(S\setminus Z\) zero through degree \(s\). Their derived global sections also have zero cohomology in that range, since the hypercohomology spectral sequence has nonnegative sheaf-cohomology index. The support localization triangle then proves the asserted isomorphisms.

For 3, tensor the bounded flat Čech complex \(C_I\) with a free resolution of \(N\) in nonpositive degrees. The spectral sequence obtained by taking Čech cohomology first has terms only in Čech degrees at most \(d\) and resolution degrees at most zero. It has no total cohomology above \(d\). The Čech degree is bounded, so each total degree has a finite filtration and there is no convergence issue. For \(N=A/\mathfrak p\), \(\mathfrak p\in T\), the ideal induced by \(I\) has maximal-ideal radical. Radical independence and the nonvanishing theorem of Local cohomology give
\(H^{\dim(A/\mathfrak p)}_I(A/\mathfrak p)\ne0\).
The bound just proved gives \(\dim(A/\mathfrak p)\le d\). ∎

**Lemma 6.11 (formal cohomology at a puncture).** For finite \(M\), write
\[
G_I(M)=\bigl(R\Gamma_{\mathfrak m}(M)\bigr)^{\wedge I}.
\]
Then \(G_I(M)\) has no negative cohomology, and
\[
H^i(G_I(M))=\varprojlim_n H^i_{\mathfrak m}(M/I^nM).
\tag{6.13}
\]
Moreover
\[
H^i\bigl(R\Gamma(U,\widetilde M|_U)^{\wedge I}\bigr)
=\varprojlim_n H^i(U,\widetilde{M/I^nM}|_U),
\tag{6.14}
\]
and the map \(H^0(G_I(M))\to M\) identifies its source with \(\Gamma_T(M)\).

**Proof.** Use a finite distinguished affine cover of \(U\), together with the extended Čech complex for the puncture. At each entry, \(M\) is finite over a localization of the Noetherian ring \(A\). The Artin–Rees comparison in the completion lemma of Section 3 applies over that localized ring: the negative Koszul cohomology is pro-zero, and the degree-zero quotients are the ordinary ideal quotients. There are finitely many Čech entries. The bounded Čech filtration therefore makes the cones of their total comparisons pro-zero as well. Taking the product-difference derived inverse limit proves
\[
G_I(M)=R\varprojlim_n R\Gamma_{\mathfrak m}(M/I^nM),
\quad
R\Gamma(U,\widetilde M|_U)^{\wedge I}
=R\varprojlim_n R\Gamma(U,\widetilde{M/I^nM}|_U).
\]
Here the Koszul-power ideals and the powers \(I^n\) are cofinal, exactly as in Section 3. This argument does not assume that a localized Čech entry is finite as an \(A\)-module.

Each \(H^i_{\mathfrak m}(M/I^nM)\) is Artinian. Indeed local duality makes its Matlis dual finite over \(\widehat A\); evaluation injects the original torsion module into the dual of that finite module, which is Artinian by Section 1. Descending images in an Artinian module stabilize, so these inverse systems are Mittag–Leffler. The product-difference description makes their first derived limits zero, proving (6.13) and the negative-degree vanishing.

Taking derived inverse limits in the puncture localization triangles gives
\[
G_I(M)\longrightarrow M\longrightarrow
R\Gamma(U,\widetilde M|_U)^{\wedge I}\longrightarrow G_I(M)[1],
\tag{6.15}
\]
since the finite module \(M\) is \(I\)-adically complete. In positive degrees, this triangle and (6.13) identify the cohomology of its third term with the inverse limits in (6.14), using the ordinary puncture support sequence at each level. In degree zero, the derived inverse limit of connective complexes has degree-zero cohomology equal to the limit of degree-zero cohomology: the product-difference exact sequence has no degree-minus-one term. This proves (6.14) in that degree too.

Finally (6.15) identifies \(H^0(G_I(M))\) with the elements of \(M\) vanishing on every thickened puncture. Such an element vanishes at every \(\mathfrak q\in Y\cap U\): in the finite stalk, membership in every \(I^nM_{\mathfrak q}\) implies zero by Krull intersection. Its cyclic support therefore meets \(Y\) only at \(\mathfrak m\). Conversely, that support condition makes its image modulo \(I^n\) supported only at \(\mathfrak m\), so the image restricts to zero on \(U\) at every level. This is precisely \(\Gamma_T(M)\). ∎

**Lemma 6.12 (a stable supported range).** Suppose \(s\ge0\) and for every \(\mathfrak p\notin T\cup Y\),
\[
\operatorname{depth}M_{\mathfrak p}\ge s
\quad\text{or}\quad g_M(\mathfrak p)>d+s.
\tag{6.16}
\]
There is an ideal \(J_0\subset\mathfrak m\) with \(V(J_0)\cap Y=\{\mathfrak m\}\). For every \(J\subset J_0\) satisfying \(V(J)\cap Y=\{\mathfrak m\}\), the comparison gives
\[
H^i_J(M)=H^i_T(M)\quad(i\le s).
\]
One power of \(IJ_0\) kills all these groups, independently of \(J\).

**Proof.** Consider the bad set
\[
B=\{\mathfrak p\in T\setminus Y:
\operatorname{depth}M_{\mathfrak p}\le s\}.
\]
We claim that the closure of \(B\cup\{\mathfrak m\}\) is contained in \(T\). Let \(\mathfrak p\) be a generic point of a component of that closure. If it belongs to \(B\cup\{\mathfrak m\}\), the claim holds. Otherwise \(B\cap V(\mathfrak p)\) is dense and consists of proper specializations of \(\mathfrak p\). It cannot have zero \(M_{\mathfrak p}\). Lemma 6.10.1 then gives \(\operatorname{depth}M_{\mathfrak p}<s\). Also every point of \(B\) satisfies \(g_M\le d+s\), by Lemma 6.10.3, so lower semicontinuity gives the same inequality at \(\mathfrak p\). The point is outside \(Y\), since its dense set \(B\) is outside that closed set. Condition (6.16) forces \(\mathfrak p\in T\). Specialization stability proves the claim for the whole closure.

Take its defining radical ideal for an initial \(J_0\). Outside \(V(J_0)\), every point of \(T\) has depth greater than \(s\). Lemma 6.10.2 gives \(H^i_{J_0}(M)=H^i_T(M)\) in the stated range. The same holds for every admissible smaller ideal \(J\), because \(V(J)\subset T\) and its missing points in \(T\) lie outside \(V(J_0)\).

Apply Theorem 6.1 to \(T\subset T\cup Y\). If \(\mathfrak p\notin T\cup Y\) and \(\mathfrak p\subset\mathfrak q\in T\), then depth at least \(s\) gives a cost greater than \(s\), since the primes are distinct. In the other case (6.16) applies. If \(\mathfrak q=\mathfrak m\), the cost is \(g_M(\mathfrak p)>d+s\ge s\). Otherwise Lemma 6.10.3 gives \(\dim(A/\mathfrak q)\le d\); subtracting this from \(g_M(\mathfrak p)>d+s\), using (4.3), again gives cost greater than \(s\). The annihilator theorem supplies an ideal \(K\), with \(V(K)\subset T\cup Y\), killing \(H^i_T(M)\) for \(i\le s\).

Enlarge \(V(J_0)\) by the finitely many components of \(V(K)\) whose generic points are outside \(Y\). Those points belong to \(T\), so this enlargement still meets \(Y\) only at \(\mathfrak m\). With the smaller defining ideal still denoted \(J_0\), we have \(V(K)\subset V(IJ_0)\). A power of \(IJ_0\) is contained in \(K\), proving the uniform annihilation. ∎

**Lemma 6.13 (annihilators of formal cohomology).** If \(g_M(\mathfrak p)>d+s\), some \(a\notin\mathfrak p\) kills \(H^i(G_I(M))\) for all \(i\le s\).

**Proof.** If \(\mathfrak p\ne\mathfrak m\), let \(S'\) be the specialization-closed set of primes not contained in \(\mathfrak p\). It contains \(\mathfrak m\). Lower semicontinuity in Lemma 6.10.1 makes \(g_M(\mathfrak p')>d+s\) at every \(\mathfrak p'\subset\mathfrak p\). Theorem 6.1, for \(\{\mathfrak m\}\subset S'\), therefore supplies an element \(a\notin\mathfrak p\) killing \(H^j_{\mathfrak m}(M)\) for \(j\le d+s\). If \(\mathfrak p=\mathfrak m\), the same groups vanish by depth and we may start with \(a=1\).

By (3.2),
\[
G_I(M)=R\operatorname{Hom}_A(C_I,R\Gamma_{\mathfrak m}(M)).
\]
The complex \(C_I\) has cohomology only in degrees \(0,\ldots,d\). In computing degrees at most \(s\), the second argument may thus be replaced by its truncation in degrees \(0,\ldots,d+s\): derived Hom from \(C_I\) into the remaining higher truncation has degrees at least \(s+1\). A power of \(a\) acts as zero on this finite truncation. Explicitly, its cohomology modules are killed by \(a\); induction on its truncation triangles shows that \(a^{d+s+1}\) acts as zero on the object itself. Applying derived Hom proves the assertion, after replacing \(a\) by that power. ∎

**Proposition 6.14 (algebraizing supported cohomology).** Under (6.16), there is an ideal \(J_0\) as in Lemma 6.12 such that, for every admissible \(J\subset J_0\), the natural map
\[
R\Gamma_J(M)\longrightarrow G_I(M)
\]
is an isomorphism on cohomology in degrees \(i\le s\).

**Proof.** The comparison is completion of the supported complex. Indeed \(\sqrt{I+J}=\mathfrak m\), and the Čech double complex gives
\(R\Gamma_I R\Gamma_J(M)=R\Gamma_{\mathfrak m}(M)\).
Completing does not change when \(R\Gamma_I\) is inserted: apply the torsion adjunction (3.4) with first argument \(C_I\). Thus \((R\Gamma_J(M))^{\wedge I}=G_I(M)\), naturally.

For \(s=0\), Lemma 6.11 identifies the target degree-zero group with the finite submodule \(\Gamma_T(M)\subset M\). Its closed support is contained in \(T\). Choose \(J_0\) whose zero set contains that support and the closed point and is still contained in \(T\). Then \(\Gamma_J(M)=\Gamma_T(M)\) for all admissible \(J\subset J_0\), proving this case. Both complexes have no negative cohomology.

Proceed by induction on \(s>0\). First remove \(L=\Gamma_{T\cup Y}(M)\). Its finite closed support lies in \(V(J_L)\cup Y\) for one admissible \(J_L\). Put \(L_1=\Gamma_{V(J_L)}(L)\) and \(L_2=\Gamma_Y(L)\). The kernel and cokernel of \(L_1\oplus L_2\to L\) have finite length, since the map is an isomorphism off \(V(J_L)\cap Y=\{\mathfrak m\}\). For every admissible \(J\subset J_L\), comparison is an isomorphism in all degrees for these four modules. For \(L_1\), supported cohomology is just the finite complete module \(L_1\). For \(L_2\), a power of \(I\) kills the module and its Čech complex, so that complex is already derived complete. The same applies to the finite-length kernel and cokernel. The exact triangles prove comparison for \(L\). Hence we can replace \(M\) by \(M/L\). Its stalks outside \(T\cup Y\) are unchanged, and all its associated primes are outside \(T\cup Y\).

For each associated prime, depth is zero. Since \(s>0\), (6.16) forces \(g_M>d+s\) there. Lemma 6.13 says that the annihilator of the initial cohomology of \(G_I(M)\) is contained in none of these primes. Lemma 6.12 gives one power of \(IJ_0\) killing \(H^i_J(M)\), \(i\le s\), for every admissible \(J\subset J_0\). Neither \(I\) nor \(J_0\) is contained in an associated prime: those primes are outside \(Y\) and outside \(T\supset V(J_0)\). Prime avoidance therefore chooses an \(M\)-regular element \(f\) which kills both initial ranges, uniformly in \(J\).

The modules \(M\) and \(M/fM\) satisfy (6.16) with \(s-1\). At a nonzero quotient stalk, regularity lowers depth and \(g_M\) by one; at a zero quotient stalk the inequalities hold automatically. Shrink the ideal using the induction hypotheses for these two modules. In degree \(s-1\), the sequence \(0\to M\xrightarrow f M\to M/fM\to0\) gives a map of short exact sequences
\[
\begin{array}{ccccccccc}
0&\to&H^{s-1}_J(M)&\to&H^{s-1}_J(M/fM)&\to&H^s_J(M)&\to&0\\
&&\downarrow&&\downarrow&&\downarrow\\
0&\to&H^{s-1}(G_I(M))&\to&H^{s-1}(G_I(M/fM))&\to&H^s(G_I(M))&\to&0.
\end{array}
\]
The outer zeros use the chosen annihilator \(f\). The first two vertical maps are isomorphisms by induction, so the third is an isomorphism. Lower degrees were already included in the induction. Intersecting the finitely many chosen ideals preserves the required intersection with \(Y\), and all arguments apply to every smaller admissible ideal. Restore \(L\) using its all-degree comparison to finish. ∎

**Theorem 6.15 (formal sections near a punctured closed set).** Let \(F\) be coherent on \(U\), let \(s\ge0\), and suppose that for every \(x\in X\setminus Y\) whose closure meets \(U\cap Y\),
\[
\operatorname{depth}F_x\ge s
\quad\text{or}\quad
\operatorname{depth}F_x+\dim\overline{\{x\}}>d+s.
\tag{6.17}
\]
There is an open \(V_0\subset U\) containing \(U\cap Y\) such that for every open \(U\cap Y\subset V\subset V_0\),
\[
H^i(V,F)=\varprojlim_n H^i(U,F/I^nF),\qquad i<s.
\tag{6.18}
\]
If also \(\operatorname{depth}F_x+\dim\overline{\{x\}}>s\) at every \(x\in U\cap Y\), these groups are finite.

**Proof.** Extend \(F\) to a finite \(A\)-module \(M\): its quasi-coherent direct image has a module of sections, and finitely many elements generate its restriction on a finite distinguished cover of \(U\). Their finite span is such an extension. Condition (6.17) is exactly (6.16), since points outside \(T\cup Y\) are precisely the off-\(Y\) points whose closures meet \(U\cap Y\).

Choose \(J_0\) from Proposition 6.14 and set \(V_0=X\setminus V(J_0)\). Every indicated \(V\) is the complement of a closed set \(V(J)\) with \(J\subset J_0\) and \(V(J)\cap Y=\{\mathfrak m\}\), after choosing defining radical ideals. Compare the support triangle for \(V\) with (6.15). The map on their finite middle terms is the identity of \(M\); Proposition 6.14 compares their first terms through degree \(s\). Their third terms therefore have isomorphic cohomology in degrees \(i<s\). Lemma 6.11 identifies the formal third term with the inverse limits in (6.18).

For finiteness apply Theorem 6.2 to \(T\). Its prime-pair test outside \(T\cup Y\) was checked in Lemma 6.12. A remaining lower prime lies in \(Y\setminus T\); any point of \(T\) above it must then be \(\mathfrak m\). The required cost is exactly the additional depth-plus-closure-dimension bound in the statement. Thus \(H^j_T(M)\), \(j\le s\), are finite. Lemma 6.12 transfers this to \(H^j_J(M)\); the puncture support sequence makes \(H^i(V,F)\) finite for \(i<s\), including degree zero. ∎

The supported comparison and its section consequence are the results of [Stacks, Tag 0DXP](https://stacks.math.columbia.edu/tag/0DXP) and [Tag 0DXQ](https://stacks.math.columbia.edu/tag/0DXQ). The proof explains both qualifications in (6.17). Low-depth components whose closures avoid the punctured closed set may be removed by shrinking. The other low-depth points require the stricter dimension inequality. Completeness enters the formal-cohomology triangle and the comparison on finite supported modules.

### Dualizing complexes and completion along an ideal

The comparison above used maximal-ideal completion. Formal geometry also requires completion along an arbitrary ideal, followed by localization. The following argument proves the fibre and dimension properties needed for that operation.

**Lemma 6.16 (polynomials and maximal-ideal completion).** A Noetherian ring with a dualizing complex is universally catenary. If \((R,\mathfrak m)\) is such a local ring with dualizing complex \(D\), then \(D\otimes_R\widehat R\) is dualizing over its maximal-ideal completion.

**Proof.** First adjoining a variable preserves existence of a dualizing complex. Put \(P=A[t]\). The complex \(D\otimes_A P\) has bounded finite cohomology, and its homothety is the flat base change of that for \(D\). To justify this Hom base change, represent the first finite complex by a bounded-above complex of finite free modules and the target by a bounded complex of finite modules. In each total degree the Hom complex uses finitely many terms, so flat tensor product commutes with it and with its cohomology.

We check finite injective dimension as well. If \(D\) has an injective representative bounded above by \(n\), then its tensor product with the free \(A\)-module \(P\) is still an injective complex over \(A\). Direct sums of injectives are injective over a Noetherian ring: a map from a finitely presented ideal has image in a finite subsum, where Baer's criterion extends it. For every \(P\)-module \(N\) there is an exact sequence
\[
0\longrightarrow P\otimes_A N
\xrightarrow{t\otimes1-1\otimes t_N}P\otimes_A N
\longrightarrow N\longrightarrow0.
\]
The last map evaluates the polynomial in its action on \(N\). Injectivity of the first map follows by comparing the highest polynomial coefficient of a finite sum; the cokernel is \(N\) by successively evaluating powers of \(t\). Induction–restriction adjunction identifies derived Hom from an induced module with derived Hom over \(A\). The resulting long exact sequence makes \(\operatorname{Ext}^i_P(N,D\otimes P)=0\) for \(i>n+1\), for every \(N\). Thus the displayed complex is dualizing over \(P\).

Iteration and Proposition 2.4 give a dualizing complex on every finite-type \(A\)-algebra. Lemma 4.1's dimension function makes each of these rings catenary: every saturated prime chain has length the difference of its endpoint values. This proves universal catenarity.

For the completion assertion, let \(S=\widehat R\), and choose a normalized dualizing complex \(\Omega\) over \(S\), using Proposition 2.5. Normalize \(D\) over \(R\) too. The finite complex \(F=D\otimes_R S\) satisfies
\[
R\operatorname{Hom}_S(k,F)=k[0],
\]
by a bounded-above resolution of the residue field by free modules of finite rank, together with flat base change. Its length need not be finite. Set \(L=R\operatorname{Hom}_S(F,\Omega)\), a bounded finite complex. Biduality and adjunction give
\[
R\operatorname{Hom}_S(k,F)
=R\operatorname{Hom}_k(k\otimes_S^{\mathbf L}L,k).
\]
A complex of vector spaces splits into its cohomology, so the right side equals \(k[0]\) only when \(k\otimes_S^{\mathbf L}L=k[0]\). In a minimal finite free resolution of \(L\), all differentials become zero over \(k\). It therefore has just one term, of rank one, in degree zero. Thus \(L=S\) and \(F=\Omega\). Undoing normalization proves the assertion for the original shift of \(D\). ∎

**Proposition 6.17 (fibres of arbitrary completion).** Let \(A\) be Noetherian with dualizing complex \(D\), let \(I\subset A\), and put \(B=\widehat A^{\,I}\). For every prime \(P\) of \(B\), the complex \(D\otimes_A B_P\) is dualizing over \(B_P\). The ring \(B\) is universally catenary. Every local fibre of \(A\to B\) is Gorenstein, hence Cohen–Macaulay.

**Proof.** Completion is Noetherian and flat by the earlier Completion lesson. Every maximal ideal of \(B\) contains \(IB\): for \(u\in IB\), the geometric series for \((1-u)^{-1}\) converges. A maximal ideal \(N\) thus corresponds to a maximal ideal \(\mathfrak q\supset I\) of \(A\), and \(N=\mathfrak qB\). For every \(l\),
\[
B/\mathfrak q^lB=A/\mathfrak q^l,
\]
because a power of \(I\) is zero in that quotient and completion is exact on finite modules. Consequently the local rings \(A_{\mathfrak q}\) and \(B_N\) have the same maximal-ideal completion, and the corresponding completed dualizing complexes coincide. Lemma 6.16 makes this common completed complex dualizing.

Here dualizing structure descends to \(B_N\). The Hom base change proved in Lemma 6.16 descends its homothety by faithful flatness. For injective dimension choose a bound \(b\) for the completed complex, enlarged to exceed its cohomology degrees. For every ideal \(K\subset B_N\), a resolution by free modules of finite rank and faithful flatness give
\[
\operatorname{Ext}^j_{B_N}(B_N/K,D\otimes B_N)=0
\quad(j>b).
\]
These cyclic-module tests give a bounded injective representative. Explicitly, take a bounded-below injective resolution \(J\) of the complex. Its tail from degree \(b\) resolves its cycle module \(Z^b\). The quotient complex in lower degrees is a bounded complex of injectives, so the displayed tests identify with \(\operatorname{Ext}^1(B_N/K,Z^b)=0\). Baer's criterion makes \(Z^b\) injective; truncate the resolution there. This proves descent of finite injective dimension. Localization now proves the assertion at every \(P\subset N\).

Each \(B_N\) is universally catenary by Lemma 6.16. This implies that \(B\) is universally catenary: a prime interval in a finite-type \(B\)-algebra can be examined after localizing \(B\) at a maximal ideal containing the contraction of its upper endpoint. Every prime in the interval survives that localization, and the localized finite-type algebra is catenary.

Finally put \(\mathfrak p=P\cap A\), \(R=A_{\mathfrak p}\), \(S=B_P\), and \(F=S/\mathfrak pS\). The flat local map carries the dualizing complex \(D_R\) to the dualizing complex \(D_R\otimes_R S\) just proved. Resolve \(\kappa(\mathfrak p)\) by finite free \(R\)-modules. Its flat tensor product resolves \(F\) over \(S\), giving
\[
R\operatorname{Hom}_S(F,D_R\otimes_R S)
=R\operatorname{Hom}_R(\kappa(\mathfrak p),D_R)\otimes_R S
=F[c]
\]
for the residue-field shift \(c\) of \(D_R\). Quotient duality makes the left side dualizing over \(F\). Thus a shift of \(F\) itself is dualizing, and Proposition 4.3 makes \(F\) Gorenstein and Cohen–Macaulay. ∎

**Proposition 6.18 (depth and prime intervals after completion).** Under Proposition 6.17, let \(M\) be finite and \(M_B=M\otimes_A B\). Suppose \(P\subset Q\) in \(\operatorname{Spec}B\), with \(Q\supset IB\), and write \(\mathfrak p=P\cap A\), \(\mathfrak q=Q\cap A\). Then
\[
\operatorname{depth}(M_B)_P\ge\operatorname{depth}M_{\mathfrak p},
\]
and
\[
\operatorname{depth}(M_B)_P+\dim((B/P)_Q)
=\operatorname{depth}M_{\mathfrak p}
+\dim((A/\mathfrak p)_{\mathfrak q}).
\tag{6.19}
\]

**Proof.** The primes containing the completed ideal correspond exactly to primes containing \(I\). In particular \(Q=\mathfrak qB\), and the flat local map \(A_{\mathfrak q}\to B_Q\) has residue-field closed fibre. Its maximal-ideal completions agree, since
\[
B_Q/\mathfrak q^lB_Q=A_{\mathfrak q}/\mathfrak q^lA_{\mathfrak q}
\quad(l\ge1).
\]
This uses the same finite-quotient argument as Proposition 6.17 and is valid even when \(\mathfrak q\) is not maximal in \(A\).

Set \(R=(B/\mathfrak pB)_Q\). The flat local dimension formula gives
\[
\dim R=D_0=\dim((A/\mathfrak p)_{\mathfrak q}).
\]
Its maximal-ideal completion is the completion of \((A/\mathfrak p)_{\mathfrak q}\), by the preceding quotient identities. Proposition 2.4 and Lemma 6.16 make this local domain universally catenary, so Lemma 6.6 makes that common completion equidimensional of dimension \(D_0\).

Equidimensionality descends here. For a minimal prime \(\mathfrak r\) of \(R\), choose a minimal prime above \(\mathfrak r\widehat R\). Flat going down makes it minimal in \(\widehat R\): any smaller prime would contract to a prime below the minimal prime \(\mathfrak r\), hence would still contain \(\mathfrak r\widehat R\). Thus every component of \(\widehat R/\mathfrak r\widehat R\) has dimension \(D_0\). Exactness and dimension preservation of completion give \(\dim R/\mathfrak r=D_0\). The ring \(R\) is therefore equidimensional, and is catenary by Proposition 6.17.

Write \(u=\dim(B_P/\mathfrak pB_P)\). The chain formula (6.8) in \(R\) gives
\[
u+\dim((B/P)_Q)=D_0.
\]
The fibre at \(P\) is Cohen–Macaulay by Proposition 6.17. The flat depth formula of Lemma 6.7 consequently gives
\[
\operatorname{depth}(M_B)_P=\operatorname{depth}M_{\mathfrak p}+u.
\]
Adding the two equalities proves (6.19), and \(u\ge0\) proves the first assertion. If a stalk of \(M\) is zero, local faithful flatness makes the corresponding completed stalk zero too; both equalities use the depth-infinity convention. ∎

This is the arbitrary-ideal comparison of [Stacks, Tag 0EHW](https://stacks.math.columbia.edu/tag/0EHW). The upper prime must contain the ideal of completion. That condition gives its residue-field fibre and the common local completion used in the dimension calculation.

## 7. Two singularity computations

**Example 7.1 (three axes).** Let
\[
A=k[[x,y,z]]/(xy,yz,zx).
\]
Every series has a unique expression
\(c+x a(x)+y b(y)+z c_1(z)\). Restriction to the three axes embeds \(A\) into
\(k[[x]]\oplus k[[y]]\oplus k[[z]]\); its image is the triples with the same constant term. Its three minimal primes define these one-dimensional axes, so \(\dim A=1\).

The element \(t=x+y+z\) acts on that embedding as multiplication by \(x,y,z\) respectively. Each is injective on its power-series ring; hence \(t\) is a nonzerodivisor on \(A\). This proves depth one and Cohen–Macaulayness. Eliminate \(z=-x-y\) in the quotient to obtain
\[
B=A/(t)=k[x,y]/(x^2,xy,y^2).
\]
Its basis is \(1,x,y\), and its socle is \(kx\oplus ky\). If \(A\) were Gorenstein, the two-term resolution for this regular element, together with (2.3), would give the normalized dualizing complex \(B[0]\). Since \(B\) is Artinian, Proposition 3.1 would make \(B\) its residue-field injective hull, whose socle has dimension one. The displayed two-dimensional socle rules this out.

The type is exactly two. Quotient adjunction and \(R\operatorname{Hom}_A(B,A)=B[-1]\) give
\[
\operatorname{Ext}^1_A(k,A)=\operatorname{Hom}_B(k,B)=k^2.
\]
For the canonical module \(W\) with \(\omega=W[1]\), (4.7) identifies this group with \(\operatorname{Hom}_k(W/\mathfrak mW,k)\). Thus \(W\) requires two generators. Cohen–Macaulayness controls the degree of the dualizing complex; it does not force its one surviving module to be \(A\).

**Example 7.2 (a module on a regular surface).** Let \(S=k[[x,y]]\) and \(M=S/(x)=k[[y]]\). The free resolution \(0\to S\xrightarrow{x}S\to M\to0\) gives
\[
\operatorname{Ext}^1_S(M,S)=M,\qquad
\operatorname{Ext}^j_S(M,S)=0\ (j\ne1).
\]
Since \(\omega_S=S[2]\), its dual of \(M\) is \(M[1]\), concentrated in degree \(-1\). Local cohomology of \(M\) is computed by \([M\to M_y]\):
\[
H^1_{\mathfrak m}(M)=k((y))/k[[y]],\qquad H^i_{\mathfrak m}(M)=0\ (i\ne1).
\]
On the other side, the inverse-monomial calculation and Proposition 3.1 identify
\[
E_S=H^2_{\mathfrak m}(S)
=\bigoplus_{a,b\ge1}kx^{-a}y^{-b}.
\]
Consequently
\[
D_S(M)=E_S[x]
=\bigoplus_{b\ge1}kx^{-1}y^{-b}
\simeq k((y))/k[[y]],
\]
via \(y^{-b}\mapsto x^{-1}y^{-b}\). Multiplication by \(x\) is zero on both sides, while multiplication by \(y\) shifts the displayed basis and kills its first term. This verifies the complete module structure in (3.7), not just a vector-space dimension.

## 8. Exercises and solutions

**Exercise 8.1 (a visible hull; introductory).** For \(A=k[[t]]\), prove that \(k((t))/k[[t]]\) is the injective hull of \(k\), and compute its endomorphism ring explicitly.

**Solution.** Every ideal is principal. A map \((a)\to E\) extends exactly when its chosen value at \(a\) is a multiple by \(a\) of an element of \(E\); division in \(k((t))\) proves this for \(a\ne0\), and the zero ideal poses no condition. Thus \(E\) is injective. A nonzero Laurent principal part with pole order \(n\) becomes a nonzero multiple of \(t^{-1}\) after multiplying by \(t^{n-1}\), proving essentiality. The submodule \(E_n\) killed by \(t^n\) is cyclic, generated by \(t^{-n}\), with annihilator \((t^n)\). An endomorphism on it is multiplication by a residue class in \(A/(t^n)\). Its restriction to \(E_{n-1}\) reduces that residue modulo \(t^{n-1}\). Compatibility over all \(n\) is therefore exactly a power series. This gives \(\operatorname{End}_A(E)=k[[t]]\), including multiplication in the ring of endomorphisms.

**Exercise 8.2 (Koszul normalization; intermediate).** Let \(A\) be regular local of dimension \(n\). Compute \(\operatorname{Ext}^i_A(k,A)\), and explain why this computation proves Gorensteinness rather than merely suggesting it.

**Solution.** The Koszul resolution on a regular system of parameters is self-dual, with its dual shifted by \(-n\). Its Hom complex has sole cohomology \(A/\mathfrak m=k\) in degree \(n\). This computes the Ext groups. To establish finite injective dimension, compute \(\operatorname{Tor}_i^A(k,N)\) for any finite \(N\) with that length-\(n\) resolution of \(k\). It vanishes above \(n\). A minimal free resolution of \(N\) then has no terms above \(n\), because its reduction modulo \(\mathfrak m\) has zero differentials. In particular \(\operatorname{Ext}^{n+1}_A(A/I,A)=0\) for every ideal \(I\); the \(n\)-th injective syzygy of \(A\) is injective by Baer's criterion. Thus \(A\) has finite injective dimension and is Gorenstein. Its Ext computation makes \(A[n]\) normalized.

**Exercise 8.3 (duality with coefficients; intermediate).** Verify local duality for \(S=k[[x,y]]\) and \(M=S/(x)\), and identify the action of each parameter on the local cohomology module.

**Solution.** Applying \(\operatorname{Hom}_S(-,S)\) to the two-term free resolution gives \([S\xrightarrow{x}S]\) in degrees zero and one. Its cohomology is \(M\) in degree one. Shifting the target by \([2]\) places this in degree \(-1\). The Čech complex on \(x,y\), tensored with \(M\), reduces to \([k[[y]]\to k((y))]\), because \(M_x=0\). Its cokernel has basis \(y^{-b}\), \(b\ge1\). In the hull \(E_S\) the elements annihilated by \(x\) are exactly \(x^{-1}y^{-b}\). Sending one basis to the other intertwines \(x\), which acts as zero, and \(y\), which lowers the pole order and kills the order-one term. All other local cohomology and dual Ext groups vanish. This proves (3.7) in every degree for this module.

**Exercise 8.4 (Cohen–Macaulay but not Gorenstein; intermediate).** Determine dimension, depth and type of the three-axes ring in Example 7.1.

**Solution.** Its minimal primes are \((x,y),(y,z),(z,x)\), with quotients one-variable power-series rings, so dimension is one. The common-constant embedding into their direct sum makes \(x+y+z\) a nonzerodivisor. Depth is therefore one, so the ring is Cohen–Macaulay. The regular-element quotient is \(B=k[x,y]/(x^2,xy,y^2)\); multiplication by either \(x\) or \(y\) kills the span of \(x,y\), and kills no vector with a nonzero constant term. Thus its socle has dimension two. Quotient adjunction identifies \(\operatorname{Ext}^1_A(k,A)\) with that socle, so type is two. A Gorenstein ring would give an Artinian Gorenstein quotient with a one-dimensional socle. This proves failure of Gorensteinness.

**Exercise 8.5 (dimension through duality; advanced).** For finite nonzero \(M\) over a local ring with normalized dualizing complex, let \(d=\dim\operatorname{Supp}M\). Prove, using local duality, that \(H^d_{\mathfrak m}(M)\ne0\) and \(H^i_{\mathfrak m}(M)=0\) for \(i>d\).

**Solution.** The finite-dual-module induction in Section 4 places \(R\operatorname{Hom}_A(M,\omega)\) in degrees \(-d,\ldots,0\). Explicitly, it starts with finite-length modules; a nonzerodivisor reduces dimension by one and Nakayama kills dual groups outside the indicated interval; removing maximal-ideal torsion reduces the depth-zero case to that case. Formula (3.6) and faithfulness of the torsion dual therefore make \(H^i_{\mathfrak m}(M)=0\) for \(i>d\). To find a nonzero group in degree \(-d\), choose a minimal support prime \(\mathfrak p\) with \(\dim(A/\mathfrak p)=d\). Its localized module is nonzero of finite length. Lemma 4.1 gives \(\delta(\mathfrak p)=d\), and normalized duality over \(A_{\mathfrak p}\) sends this module to a nonzero finite-length module in degree zero. Undoing the normalization shift makes
\[
\operatorname{Ext}^{-d}_A(M,\omega)_{\mathfrak p}
=H^0R\operatorname{Hom}_{A_{\mathfrak p}}
(M_{\mathfrak p},\omega_{\mathfrak p}[-d])\ne0.
\]
Hence the finite global Ext module is nonzero. Its completion remains nonzero by faithful flatness. Formula (3.6) makes \(D(H^d_{\mathfrak m}(M))\ne0\), and therefore \(H^d_{\mathfrak m}(M)\ne0\). The argument uses generic support and the exact shift, not an assumption that \(M\) itself is Cohen–Macaulay.

## Proof inputs

The local-cohomology computations, depth criterion, radical independence, flat base change and dimension vanishing used here are proved in Local cohomology. The algebra proofs are in the lessons linked in Local cohomology, under Proof inputs. From those and the derived-category prerequisite we use tensor–Hom adjunction, injective resolutions and Baer's criterion, minimal free resolutions, Artin–Rees, prime avoidance and associated-prime properties, regular systems of parameters in regular local rings, and faithful flatness of completion.

The structural lemma in Local cohomology proves that every complete Noetherian local ring is a quotient of a complete regular local ring, using the earlier coefficient-ring construction. This is the Cohen-structure input [Stacks, Tag 032A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-cohen-structure-theorem). Section 3 proves the completion-of-finite-cohomology lemma, including the Artin–Rees argument that removes higher Koszul cohomology from the inverse system. It establishes precisely the bounded finite-cohomology case of [Stacks, Tag 0A06](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-derived-completion-pseudo-coherent) used here. Section 3 also proves the derived completion adjunction for arbitrary complexes and the local duality isomorphism. Lemma 5.2 proves finite locally free local-cohomology comparison without a dualizing-complex hypothesis.

The closed-support finiteness theorem with universally catenary base and Cohen–Macaulay formal fibres is proved in Theorem 6.9. Lemma 6.4 proves locality of a finite initial range; Lemmas 6.5–6.6 prove the completed-branch dimension statement using finite-length extension and multiplication arguments; Lemma 6.7 proves the flat local depth formula; Proposition 6.8 proves equality of the cutoffs. This gives the full hypotheses and both finite- and infinite-cutoff cases of [Stacks, Tag 0BJV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/local-cohomology.html#local-cohomology-theorem-finiteness). The specialization-closed finiteness theorem under a dualizing-complex hypothesis remains Theorem 6.2. Lemmas 6.10–6.13 prove the depth, formal-cohomology and stable-support steps for local formal algebraization. Proposition 6.14 and Theorem 6.15 prove the full punctured formal-section comparison, including the closure-meeting condition, depth disjunction, uniform neighbourhood and optional finiteness range. The Čech, Artin–Rees and annihilator arguments are given there before their use in connectedness. Lemma 6.16 proves polynomial duality and maximal-ideal completion of a dualizing complex. Proposition 6.17 proves the local dualizing and Gorenstein-fibre properties for arbitrary ideal completion; Proposition 6.18 proves the exact depth-plus-prime-interval equality used in formal geometry, with no additional equidimensionality assumption.

## References

- [Stacks] The Stacks Project authors, *The Stacks Project*, [official project](https://stacks.math.columbia.edu/). The tag links refer to the AI Integrated Stacks Project edition. Its [English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) retains the upstream tags. Relevant sections are Dualizing Complexes, “Matlis duality,” “Dualizing complexes,” “Local duality,” and “Gorenstein rings”; Local Cohomology, “Finiteness of local cohomology”; and More on Algebra, “Branches of the completion,” for the formal-catenarity criterion. Lemmas 6.5–6.6 give the needed direction of that criterion through finite-length modifications and explicit prime-chain arguments.
- [Grothendieck–Laszlo] A. Grothendieck, *Cohomologie locale des faisceaux cohérents et théorèmes de Lefschetz locaux et globaux (SGA 2)*, revised edition edited by Y. Laszlo, [arXiv:math/0511279](https://arxiv.org/abs/math/0511279), Exposés IV–V for finite-length and local duality and Exposé VIII, Section 2 for finiteness.
