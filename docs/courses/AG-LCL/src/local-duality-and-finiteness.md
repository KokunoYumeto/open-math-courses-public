# Local duality and finiteness

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by GPT-6.1 Sol, the AI that wrote it. Public domain (CC0).*

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

Here a local ring is called **Gorenstein** when \(A[0]\) is dualizing, equivalently when \(A\) has finite injective dimension. Proposition 2.4 proves the quotient assertion. Cohen's structure theorem presents any complete Noetherian local ring as a quotient of a complete regular local ring, so the last assertion follows as well. Cohen's theorem is an imported prerequisite, stated with its locator below. ∎

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
where the homological Koszul complex occupies degrees \(-r,\ldots,0\). This follows directly from the mapping telescope: derived Hom changes its direct-sum triangle into the product triangle defining derived inverse limit. Over a Noetherian ring, for bounded complexes with finite cohomology, derived completion has cohomology \(\widehat{H^i(K)}\). We use this exactness fact from completion theory; its hypotheses and locators are recorded below. Formula (3.2), rather than an unqualified termwise inverse limit, is our convention for arbitrary complexes.

We will also use a support adjunction, which has a similarly short Čech proof. If all cohomology of \(T\) is \(\mathfrak m\)-power torsion, then \(T_{f_j}=0\). For any \(A_{f_j}\)-complex \(P\), tensor–restriction adjunction gives \(R\operatorname{Hom}_A(T,P)=0\). Tensoring the triangle \(C\to A\to U\) with \(L\) therefore gives
\[
R\operatorname{Hom}_A(T,C\otimes_A^{\mathbf L}L)
\simeq R\operatorname{Hom}_A(T,L).
\tag{3.4}
\]
Thus (3.1) is the right adjoint for torsion complexes. These adjunctions, not any boundedness of \(K\), will prove local duality.

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

There is a further version for a Noetherian ring that is universally catenary and whose local rings have Cohen–Macaulay formal fibres. For an ideal \(I\) and finite \(M\), it gives the same cutoff (6.6), without assuming a dualizing complex. We state this extension, with those two hypotheses, as an imported theorem below. The theorem proved here covers arbitrary specialization-closed \(T\) under the dualizing-complex hypothesis; the cited formal-fibre extension is being asserted here only for closed support.

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

The local-cohomology computations, depth criterion, radical independence, flat base change and dimension vanishing used here are proved in Local cohomology. The algebra proofs are in the written lessons linked in Local cohomology, under Proof inputs. From those and the derived-category prerequisite we use tensor–Hom adjunction, injective resolutions and Baer's criterion, minimal free resolutions, Artin–Rees, prime avoidance and associated-prime properties, regular systems of parameters in regular local rings, and faithful flatness of completion.

Two structural completion inputs are used with their precise hypotheses. Cohen's structure theorem says that a complete Noetherian local ring is a quotient of a complete regular local ring [Stacks, [Tag 032A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-cohen-structure-theorem)]. For a Noetherian ring, a finitely generated ideal \(I\), and a complex whose cohomology modules are finite, derived \(I\)-adic completion has cohomology equal to the ordinary completions of those modules [Stacks, [Tag 0A06](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-derived-completion-pseudo-coherent)]. In this lesson that fact is needed only for bounded finite-cohomology complexes. The derived completion formula and its adjunction for arbitrary complexes, and the local duality isomorphism, are proved in Section 3.

The finiteness theorem also has the following extension, supplied with its full linked open proof [Stacks, [Tag 0BJV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/local-cohomology.html#local-cohomology-theorem-finiteness)]: if \(A\) is Noetherian and universally catenary, and every formal fibre of every local ring of \(A\) is Cohen–Macaulay, then for each ideal \(I\) and finite \(M\), the cutoff \(f_I(M)\) in (6.6) has the same finiteness meaning as above. Here a formal fibre is a fibre of \(A_{\mathfrak p}\to\widehat{A_{\mathfrak p}}\); the Cohen–Macaulay hypothesis concerns all its local rings. Thus the groups below a finite cutoff are finite and the group at it is not; an infinite cutoff means all groups are finite. The linked proof reduces to complete local rings, applies the dualizing-complex theorem, and descends finiteness faithfully flatly. Its formal-fibre hypotheses ensure that completion preserves the displayed cutoff, which is the extra step beyond Section 6. The annihilator theorem and the full specialization-closed finiteness theorem under the dualizing-complex hypothesis are proved here.

## References

Linked Stacks proofs retain their [GNU Free Documentation License](https://github.com/stacks/stacks-project/blob/master/COPYING). The CC0 dedication covers the independently written exposition here.

- [Stacks] The Stacks Project authors, *The Stacks Project*, [official project](https://stacks.math.columbia.edu/). Tag links use AI Integrated Stacks Project, an edition with AI-proposed corrections and AI-written additions, not reviewed by the Stacks Project's maintainers. Its [English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) retains the upstream tags. Relevant sections are Dualizing Complexes, “Matlis duality,” “Dualizing complexes,” “Local duality,” and “Gorenstein rings,” and Local Cohomology, “Finiteness of local cohomology.”
- [Grothendieck–Laszlo] A. Grothendieck, *Cohomologie locale des faisceaux cohérents et théorèmes de Lefschetz locaux et globaux (SGA 2)*, revised edition edited by Y. Laszlo, [arXiv:math/0511279](https://arxiv.org/abs/math/0511279), Exposés IV–V for finite-length and local duality and Exposé VIII, Section 2 for finiteness. The historical statements are compared through the common local-cohomology notation; the present lesson uses its own proof organization and exposition.
