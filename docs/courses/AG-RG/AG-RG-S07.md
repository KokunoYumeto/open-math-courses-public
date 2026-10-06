# Flat quotient bootstrap over an arbitrary base

*Written and self-checked by GPT-6.1 Sol (OpenAI), Codex, Ultra setting, 5 October 2026.*

This lesson proves the general flat quotient theorem used in [lesson three](AG-RG-03.md), Section 5, and [lesson five](AG-RG-05.md), Section 8. The base schemes, covering schemes and test schemes may be non-Noetherian and non-quasi-compact. Finite presentation is imposed only where stated. Freeness and equivalence relations mean uniqueness of arrows on every scheme test, including tests with nilpotents.

The proof proceeds through pointed constant fields, fibre dimensions and Cohen–Macaulay loci, regular cuts, finite-presentation descent, transverse slices, finite open subgroupoids and their division. [Descent and Zariski Main](AG-RG-S04.md) supplies the complete preceding scheme proofs: blocks A and E for descent and recognition, block B for polynomial normality, block C for affine Zariski Main and block D for its general scheme form.

## 1. The exact earlier algebra that will be used

The following earlier programme proofs provide the algebra used below. Their hypotheses and precise statements are part of each application; links identify those proof bodies, rather than replacing an unwritten argument.

* [Krull dimension and Noether normalization](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/krull-dimension-and-noether-normalization.html), Theorem 3.1 and Corollary 3.2, give normalization by polynomial changes with integer coefficients. Theorems 4.2–4.3 give dimension and height for finite-type field domains, and Theorem 6.1 gives
  \[
  \dim_x\operatorname{Spec}B=\dim B_{\mathfrak q}
     +\operatorname{trdeg}_k\kappa(\mathfrak q)
  \tag{1}
  \]
  for an arbitrary finite-type \(k\)-algebra. Its proof treats all minimal components through the point.
* [Regular local rings](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-local-rings.html), Proposition 3.3, proves directly by polynomial induction that prime localizations of a polynomial ring over a field are regular. [Regular sequences, depth and Cohen–Macaulay modules](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/regular-sequences-depth-and-cohen-macaulay-modules.html), Theorems 4.1–4.2, Corollary 4.3 and Theorems 5.1 and 6.1, prove absence of embedded associated primes, regularity of parameters, regular dimension/depth drops, localization of Cohen–Macaulay modules and Cohen–Macaulayness of regular local rings. [Associated primes and primary decomposition](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/associated-primes-and-primary-decomposition.html), Theorems 1.2 and 2.2 and Solution 8.5, prove the zero-divisor, finiteness and finite prime-avoidance statements used to choose parameters.
* [Discrete valuation rings, normal rings and Serre's criterion](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/discrete-valuation-rings-normal-rings-and-serres-criterion.html), Theorems 1.2 and 3.3, prove the discrete valuation and intersection-in-height-one tests for a Noetherian normal domain.
* [Faithful flatness and the local criterion for flatness](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/faithful-flatness-and-the-local-criterion-for-flatness.html), Theorem 4.2 and Lemma 5.1, prove the Noetherian residue-Tor criterion and lifting of an injective fibre map. Their proof uses the actual Artin–Rees/Krull intersection proof, also written in [Cohomology and models](AG-RG-S02.md), Section 1.
* [Flatness criteria, dimension and the flat locus](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/flatness-criteria.html), Theorem 3.1, proves the flat local dimension formula; Theorem 4.1 proves miracle flatness; Lemmas 6.1–6.2 and Theorems 6.3–6.4 prove the finite-obstruction approximation, arbitrary-base fibre criterion and arbitrary-base openness of flatness. The restriction to finite presentations in the last three assertions is essential.
* [Algebra and sheaf cohomology](AG-RG-S01.md), Theorem 8.4, proves finiteness of the cohomology of a coherent sheaf on projective space over a Noetherian ring. We need its degree-zero case for a coherent sheaf supported on a projective variety.
* [Descent and Zariski Main](AG-RG-S04.md), block D, Sections D2–D3 and D5–D7, proves the standard étale local form, elementary finite pieces, the open quasi-finite locus, compatibility of relative integral closure with étale base change, and finite completion of a quasi-finite separated morphism over a qcqs base.
* [Descent and Zariski Main](AG-RG-S04.md), block A and Sections E4–E5, proves faithfully flat algebra and morphism descent, invariant-open descent, quasi-affine effectivity and effectivity of separated locally quasi-finite scheme data. Its Sections E6–E8 prove the finite flat affine quotient and scheme recognition. These statements precede the present quotient bootstrap.
* [Algebraic spaces](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-GS/prerequisites/AG-AS/algebraic-spaces.html), Lemma 2.1, Theorem 2.2 and Proposition 3.2, prove local representatives, unique equality arrows, the étale scheme quotient and open gluing. Its previously external scheme-effectivity input is now the complete preceding scheme lesson; its target-local étaleness input is Lemma 5.3 below, which is independent of quotient construction. [The étale bootstrap](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-GS/prerequisites/AG-AS/bootstrap-theorem.html), Proposition 1.1, Lemma 1.2 and Theorem 2.1, proves the corresponding representability-by-spaces permanence and étale bootstrap directly from these results and scheme recognition. The scheme gluing and local quotient-coordinate constructions used in that proof are written in [Descent and Zariski Main, Lemma A1.0](AG-RG-S04.md#scheme-open-gluing) and [Lemma A1.7](AG-RG-S04.md#quotient-local-coordinates), including arbitrary set-indexed covers and uniqueness of equality arrows on tests with nilpotents.

Each use below specifies which of these actual proved statements applies. This list grants no exemption to an unspecified algebraic or geometric prerequisite. In the preceding local flatness and finite-obstruction proofs, the independence, balance and exact-sequence properties of Tor are supplied by Lemma 1.A below. In particular this binding applies to the residue-Tor and regular-cut arguments used in Sections 3–4 and to the Tor-obstruction transport used in Section 5; it applies over arbitrary rings and to arbitrary modules, without an additional finiteness assumption.

<a id="ag-rg-s07-tor"></a>

**Lemma 1.A (the Tor calculus used in the local criteria).** Let \(R\) be any commutative ring and \(M,N\) any modules. Choose a free resolution \(P_\bullet\to M\) by taking a free surjection onto the module and then onto each successive kernel, and define \(\operatorname{Tor}_i^R(M,N)=H_i(P_\bullet\otimes_R N)\). This definition is independent of the resolution, naturally symmetric in \(M,N\), and has the natural long exact sequence of a short exact sequence in either variable.

**Proof.**

For completeness, the resolution facts used here have the following algebraic proof. Given free resolutions \(P_\bullet\to M\) and \(P'_\bullet\to M'\) and a map \(M\to M'\), lift it to \(P_0\to P'_0\). If maps have been chosen through degree \(i-1\), the image of \(d(P_i)\) lies in the cycles of \(P'_{i-1}\), which are the image of \(P'_i\); freeness of \(P_i\) therefore supplies the next lift. Two such lifts are chain homotopic: after the homotopy has been chosen below degree \(i\), their degree-\(i\) difference minus the already prescribed homotopy term maps to zero under the next differential, and freeness lifts it to \(P'_{i+1}\). The same induction starts at degree zero because both lifts induce the same map on the augmentation. Tensoring preserves the homotopy identity. Thus induced homology maps are independent of the lifts, preserve compositions, and comparison maps between two resolutions of the same module are inverse on homology.

Let \(Q_\bullet\to N\) be another free resolution and form the first-quadrant double complex \(D_{p,q}=P_p\otimes_R Q_q\), with total differential \(d_P\otimes1+(-1)^p1\otimes d_Q\). Augmentation gives maps from its total complex to \(P_\bullet\otimes_R N\) and to \(M\otimes_R Q_\bullet\). Each is a homology isomorphism. Indeed, filter by the degree in the unaugmented direction. In the other direction each augmented row or column is exact because its fixed factor is free. To check the resulting homology assertion directly, start with the outermost nonzero component of a cycle in the augmented kernel and use this exactness to subtract a total boundary that removes that component; proceed to the next component. A chain in any fixed total degree has only finitely many components, so this process terminates. The same process applied to boundaries proves injectivity. The comparison maps just constructed make these two augmentation isomorphisms natural. Interchanging the two resolutions, with the sign \((-1)^{pq}\) on \(P_p\otimes_RQ_q\), consequently gives
\[
\operatorname{Tor}_i^R(M,N)\simeq\operatorname{Tor}_i^R(N,M).
\]
In particular Tor can be computed using a free resolution of either variable; a projective resolution works as well, since projectives are summands of free modules and the same lifting and exactness arguments apply.

For \(0\to N'\to N\to N''\to0\), tensoring in each degree with the free module \(P_i\) gives a short exact sequence of complexes. If a cycle in the quotient complex is lifted to the middle complex, its differential lies in the subcomplex and is a cycle there. Its homology class is independent of the lift and of the cycle representative: changing either changes that differential by a boundary. This defines the connecting map. The equations saying that a class maps to zero say precisely that one can subtract a boundary and lift it to the preceding complex; they prove exactness at each position. The construction commutes with maps of short exact sequences and gives
\[
\cdots\longrightarrow\operatorname{Tor}_i^R(M,N')
\longrightarrow\operatorname{Tor}_i^R(M,N)
\longrightarrow\operatorname{Tor}_i^R(M,N'')
\longrightarrow\operatorname{Tor}_{i-1}^R(M,N')\longrightarrow\cdots,
\]
ending in
\[
\operatorname{Tor}_1^R(M,N'')\longrightarrow M\otimes_RN'
\longrightarrow M\otimes_RN\longrightarrow M\otimes_RN''\longrightarrow0.
\]
Balance gives the corresponding sequence in the first variable. These arguments require neither Noetherianity nor finite generation. \(\square\)

## 2. Units and the field relation at an identity

We only need the following special case of uniqueness of a constant field: an affine integral scheme of finite type for two field structures, with a rational point that retracts both structures. Proving that case avoids importing the stronger assertion for every reduced connected scheme.

**Lemma 2.1 (finite normalization over a perfect field).** If \(k\) is perfect and \(B\) is a finite-type \(k\)-domain, its integral closure in its fraction field is finite over \(B\).

**Proof.** Choose a finite injective polynomial normalization \(P=k[x_1,\ldots,x_d]\subset B\) by Section 1. Put \(K=\operatorname{Frac}P\) and \(L=\operatorname{Frac}B\). The field extension \(L/K\) is finite. First suppose it is separable. Choose a \(K\)-basis \(v_i\) in \(L\), multiplying each vector by an element of \(P\setminus\{0\}\) so that it is integral over \(P\). This scaling works by clearing the coefficients of its monic equation: if \(v^n+a_1v^{n-1}+\cdots+a_n=0\), choose a common denominator \(c\), and \(cv\) has coefficients \(c^ia_i\) in \(P\).

The trace pairing is nondegenerate. To verify this field fact, a finite separable extension has a primitive element: over an infinite field, a linear combination of generators avoiding the finitely many equations equating distinct embeddings separates them; over a finite field the multiplicative group of any finite extension is cyclic, since its exponent bounds its cardinality by the root bound for \(T^e-1\), and an element attaining that exponent exists by combining elements of maximal prime-power orders. For a primitive element with distinct conjugates, the Vandermonde matrix is invertible; its Gram matrix is the trace matrix. Thus the trace matrix \(G=(\operatorname{Tr}(v_iv_j))\) has nonzero determinant \(\delta\).

For an element \(z\) integral over \(P\), all \(\operatorname{Tr}(zv_i)\) belong to \(P\): each conjugate is integral, their sum is integral and lies in \(K\), and \(P\) is normal. Solving the trace equations shows that the coordinates of \(z\) in this basis lie in \(\delta^{-1}P\). The integral closure is therefore a submodule of the finite \(P\)-module \(\sum_i\delta^{-1}Pv_i\), hence finite because \(P\) is Noetherian.

In characteristic \(p>0\), let \(L_0\) be the subfield of elements separable over \(K\). It is a finite separable extension, and \(L/L_0\) is purely inseparable of bounded exponent: for every element its irreducible polynomial is \(g(T^{p^a})\) with \(g\) separable; finitely many field generators give one exponent \(q=p^a\). Let \(Q\) be the integral closure of \(P\) in \(L_0\), finite by the preceding case, with module generators \(c_j\). If \(z\in L\) is integral over \(P\), then \(z^q\in Q\). In an algebraic closure of \(L_0\),
  \[
  z\in\sum_j P^{1/q}c_j^{1/q}.
  \]
Indeed write \(z^q=\sum_j a_jc_j\), take the unique \(q\)-th roots and use additivity of this power. Since \(k\) is perfect, \(P^{1/q}=k[x_1^{1/q},\ldots,x_d^{1/q}]\) is finite over \(P\). The displayed module is finite over \(P\), so its submodule of integral elements is finite. An element integral over \(B\) is integral over \(P\) by transitivity, and an element integral over \(P\) is integral over \(B\). This is the desired closure. A finite set of its \(P\)-module generators also generates it over \(B\). \(\square\)

**Lemma 2.2 (units over an algebraically closed field).** For a finite-type integral \(k\)-scheme \(X\), with \(k\) algebraically closed, \(\Gamma(X,\mathcal O_X)^*/k^*\) is a finitely generated abelian group.

**Proof.** Restriction to a nonempty affine open is injective, also after quotienting by \(k^*\); it suffices to treat that affine open. Take its integral projective closure \(\bar X\) in projective space. Normalize \(\bar X\) in its function field. On each affine chart Lemma 2.1 gives a finite normal algebra. Integral closure commutes with localization by the earlier integral-extension lesson, so these charts glue to a finite birational morphism \(\nu:\bar X^\nu\to\bar X\), with \(\bar X^\nu\) integral and normal.

The sheaf \(\nu_*\mathcal O_{\bar X^\nu}\) is coherent: on each Noetherian affine chart it is its finite normalization module. Its extension by the projective closed immersion is coherent, so projective finiteness from Section 1 gives a finite-dimensional \(k\)-algebra \(\Gamma(\bar X^\nu,\mathcal O)\). It is a domain; a finite-dimensional domain over a field is a field, since nonzero multiplication is an injective, hence surjective, linear map. Algebraic closedness makes this algebra equal to \(k\).

Let \(X^\nu=\nu^{-1}(X)\). Its complement has finitely many irreducible components, hence finitely many codimension-one generic points \(z_1,\ldots,z_r\). The height-one local rings of the normal scheme are DVRs by Section 1. A unit \(f\) on \(X^\nu\) defines the vector
  \[
  \bigl(\operatorname{ord}_{z_1}f,\ldots,
          \operatorname{ord}_{z_r}f\bigr)\in\mathbf Z^r.
  \]
If this vector is zero, both \(f\) and \(f^{-1}\), regarded as rational functions, are regular at every codimension-one point of \(\bar X^\nu\): at the remaining points this follows from their regularity on \(X^\nu\). The intersection-in-height-one theorem on every normal affine chart makes both functions global. Therefore \(f\in k^*\). We obtain an injection of the unit quotient into \(\mathbf Z^r\).

A subgroup of \(\mathbf Z^r\) is finitely generated: induct on \(r\), project to the last coordinate, use its least positive generator when its image is nonzero, lift that generator, and apply the induction to the kernel. Units on the original \(X\) inject into units on \(X^\nu\), with the same constants, so their quotient is finitely generated too. \(\square\)

**Lemma 2.3 (units in a pointed domain).** If \(B\) is a finite-type \(k\)-domain and \(e:B\to k\) retracts its field structure, then \(B^*/k^*\) is finitely generated.

**Proof.** Extend to an algebraic closure \(\bar k\). The finite-type \(\bar k\)-algebra \(B_{\bar k}\) is Noetherian. Choose an irreducible component of its reduction containing the point given by \(e\otimes\bar k\), and write it as the integral affine scheme \(Y\). Every minimal prime of \(B_{\bar k}\) contracts to zero in \(B\). Indeed its local map over the contraction is flat and local; going down would put a strictly smaller prime below it if that contraction were nonzero. Thus \(B\to\Gamma(Y,\mathcal O_Y)\) is injective.

If a unit of \(B\) becomes a constant \(\lambda\in\bar k^*\) on \(Y\), evaluate at the selected \(\bar k\)-point to get \(\lambda=e(b)\in k^*\). Injectivity then makes \(b\) that constant already. Thus \(B^*/k^*\) injects into \(\Gamma(Y,\mathcal O_Y)^*/\bar k^*\). Lemma 2.2 and the subgroup argument prove the claim. \(\square\)

**Lemma 2.4 (two retracted field structures).** Suppose that \(D\) is a domain, \(s,t:K\to D\) make it finite type over a field \(K\), and \(e:D\to K\) satisfies \(es=et=\operatorname{id}_K\). Then \(s=t\).

**Proof.** Write \(K_s=s(K)\), \(K_t=t(K)\), and \(K_0=K_s\cap K_t\). Lemma 2.3 for the two rational-point structures shows that \(D^*/K_s^*\) and \(D^*/K_t^*\) are finitely generated. The natural injection
  \[
  K_s^*/K_0^*\hookrightarrow D^*/K_t^*
  \]
makes its left side finitely generated. Lift generators \(\alpha_i\). Every nonzero element of \(K_s\) is a constant in \(K_0^*\) times a Laurent monomial in the \(\alpha_i\). Hence
  \[
  K_0[\alpha_1,\ldots,\alpha_n,(\alpha_1\cdots\alpha_n)^{-1}]
  =K_s.
  \]
The fully proved Zariski lemma in the earlier Nullstellensatz lesson makes \(K_s/K_0\) finite. Interchanging the structures makes \(K_t/K_0\) finite as well.

The elements of \(D\) algebraic over \(K_s\) form a field: the inverse of a nonzero algebraic element is a polynomial in it, obtained from its equation with nonzero constant term. The map \(e\) injects that field into \(K\) and is already surjective on \(K_s\). Consequently this field is exactly \(K_s\). Since \(K_t\) is algebraic over \(K_0\subset K_s\), it lies in \(K_s\). The reverse containment follows symmetrically. Finally \(e\) has inverse both \(s\) and \(t\) on the common field. Thus \(s=t\). \(\square\)

**Corollary 2.5 (field equivalence relation).** If \(R\rightrightarrows\operatorname{Spec}K\) is a scheme equivalence relation with locally finite-type projections, then its projections are locally quasi-finite.

**Proof.** At the identity choose an affine neighbourhood \(\operatorname{Spec}B\) finite type over \(K\) for both maps, and let \(\mathfrak q\) be the identity prime. For a minimal prime \(\mathfrak p\subset\mathfrak q\), put \(D=B/\mathfrak p\). The identity evaluation factors through \(D\) and retracts both field structures, so Lemma 2.4 makes those structures equal. The map \(\operatorname{Spec}D\to R\) therefore lies in the stabilizer of the one object. That stabilizer is the identity scheme: uniqueness of arrows on every test scheme is the monomorphism condition. Thus this component is a point. Every component through the identity has dimension zero, giving \(\dim_{e}\!R=0\).

For an arbitrary arrow over a residue field \(L\), extension to \(L\) followed by composition with its inverse identifies the selected source-fibre point with the identity in the other source fibre. Dimension at a point is preserved by field extension, as proved in Lemma 3.1 below. It is therefore zero. For a locally finite-type map, a fibre point of dimension zero is isolated and has finite residue extension, by the finite-type field dimension and Zariski lemmas. This is precisely local quasi-finiteness. Inversion supplies the other projection. \(\square\)

## 3. Dimension and the Cohen–Macaulay locus

**Lemma 3.1 (field extension preserves point dimension).** For a finite-type \(k\)-algebra \(B\), an extension \(k'/k\) and a point \(x'\) above \(x\), one has \(\dim_{x'}\operatorname{Spec}(B\otimes_k k')=\dim_x\operatorname{Spec}B\).

**Proof.** Present \(B=k[X_1,\ldots,X_n]/I\). At the two corresponding primes, the vertical maps on the localized polynomial rings and on the localized quotient rings are flat local maps. Their closed fibre rings are identical: both are the localization, at the selected point, of \(k'\otimes_k\kappa(x)\). The flat local dimension formula from Section 1 therefore gives
  \[
  \dim P_{x}-\dim B_x
   =\dim P'_{x'}-\dim B'_{x'}.
  \]
The polynomial height formula and (1) identify each side with \(n-\dim_x\operatorname{Spec}B\), respectively \(n-\dim_{x'}\operatorname{Spec}B'\). This proves the equality. No equality of the two local-ring dimensions is asserted. \(\square\)

**Lemma 3.2 (quasi-finite coordinates near a fibre point).** Let \(A\to B\) be finite type. If the fibre has point dimension \(d\) at \(\mathfrak q\), then, after a principal localization not removing that point, there is a quasi-finite map \(A[T_1,\ldots,T_d]\to B\).

**Proof.** Put \(\mathfrak p=A\cap\mathfrak q\). In the finite-type \(\kappa(\mathfrak p)\)-fibre, remove the finitely many components not through \(\mathfrak q\), and choose a principal neighbourhood with dimension \(d\). The same principal element lifts to \(B\). Polynomial normalization from Section 1 can be chosen by the integer-coefficient triangular substitutions in its proof; hence its \(d\) parameters are polynomials with integer coefficients in a fixed finite list of fibre algebra generators. Lift these polynomials to \(B\). The fibre algebra is finite over the parameter algebra, so \(B\) is quasi-finite over \(A[T_1,\ldots,T_d]\) at the selected point. Its quasi-finite locus is open by the affine Zariski Main theorem: that theorem gives there a principal localization of a finite subalgebra. Shrink once more inside this open. \(\square\)

**Lemma 3.3 (the polynomial coordinate test).** Suppose \(B\) is finite type over a field \(k\), and \(k[T_1,\ldots,T_d]\to B\) is quasi-finite. At a prime \(\mathfrak q\), the local map from the polynomial localization is flat if and only if \(B_{\mathfrak q}\) is Cohen–Macaulay and \(\dim_{\mathfrak q}\operatorname{Spec}B=d\).

**Proof.** Write \(\mathfrak r\) for the polynomial prime. Quasi-finiteness makes the local fibre zero-dimensional and the residue extension finite. Thus the two residue fields have the same transcendence degree over \(k\). Formula (1) and the polynomial height formula show that the point-dimension condition is equivalent to
  \[
  \dim B_{\mathfrak q}=\dim k[T]_{\mathfrak r}.
  \tag{2}
  \]
If the local map is flat, its dimension formula gives (2). A regular parameter system in the polynomial local ring remains regular in \(B_{\mathfrak q}\) by flatness. Its quotient is the zero-dimensional local fibre, so these are parameters there; the parameter criterion gives Cohen–Macaulayness. Conversely (2), Cohen–Macaulayness and the zero-dimensional fibre satisfy the fully proved miracle flatness theorem from Section 1. \(\square\)

**Theorem 3.4 (the good locus).** For a flat locally finitely presented scheme morphism \(X\to S\), the locus of points whose local fibre ring is Cohen–Macaulay is open and dense in every fibre, and it commutes with every base change. For a locally finitely presented morphism not initially flat, its Cohen–Macaulay locus is the corresponding open within its open flat locus. The locally quasi-finite locus is open and commutes with every base change.

**Proof of openness.** Work on an affine chart \(A\to B\) of finite presentation, and let the selected Cohen–Macaulay fibre point have point dimension \(d\). Lemma 3.2 gives quasi-finite coordinates \(P=A[T_1,\ldots,T_d]\to B\) near it. Lemma 3.3 makes the map on the local fibre flat. The arbitrary-base fibre criterion in Section 1, applied to \(A\to P\to B\) and the finitely presented \(B\)-module \(B\), gives flatness over \(P\) at the selected point; both \(P\) and \(B\) are essentially of finite presentation over \(A\). Arbitrary-base openness of flatness gives a neighbourhood on which \(P\to B\) is flat. Lemma 3.3, applied to every residue-field fibre, then gives Cohen–Macaulay fibre rings on that neighbourhood. This proves openness without replacing \(A\) by a Noetherian base.

**Proof of density.** A fibre is locally finite type over a field and locally Noetherian. At each generic point its local ring is zero-dimensional, so its depth and dimension are both zero; it is Cohen–Macaulay. The open just proved therefore contains all fibre generic points and is dense.

**Proof of base change.** It suffices to treat finite-type field algebras under a field extension. Near a chosen prime of \(B/k\), first remove components of larger dimension not through it, and take a finite injective polynomial normalization \(k[T_1,\ldots,T_d]\to B\) with \(d=\dim_x\operatorname{Spec}B\). It remains finite and injective after field extension. Lemma 3.1 preserves \(d\). By Lemma 3.3, Cohen–Macaulayness at either point is exactly flatness over its polynomial coordinate local ring. Flat base change preserves this flatness. It also reflects it at each point above: the two vertical local maps are faithfully flat, and have identical fibre rings; for any injection of modules over the old polynomial local ring, its kernel after tensoring with the old \(B\)-stalk is killed by the new faithfully flat \(B\)-stalk, because the new stalk is flat over the new polynomial ring and that ring is flat over the old one. Faithfulness kills the kernel. This proves equivalence of Cohen–Macaulayness at the two points and the stated arbitrary scheme base change assertion.

For a map not initially flat, openness of flatness was proved in the earlier finite-obstruction lesson. On that open apply the preceding result. Under a flat base change its flat locus is both preserved and reflected by the same faithfully flat local kernel test, and its fibre Cohen–Macaulay locus has the compatibility just proved.

The quasi-finite assertion follows locally from affine Zariski Main and Lemma 3.1: a finite-type fibre has an isolated point with finite residue field exactly when its point dimension is zero. Thus the zero-dimensional point locus is open and is preserved and reflected by arbitrary base change. \(\square\)

## 4. Regular cuts with a non-Noetherian base

**Lemma 4.1 (regular cut).** Let \(A\to B\) be a flat local map, with \(B\) essentially of finite presentation over \(A\), and let \(f\in B\) be regular in \(B/\mathfrak m_AB\). Then multiplication by \(f\) on \(B\) is injective and \(B/fB\) is flat over \(A\).

**Proof.** Use the Noetherian local models constructed explicitly in the earlier finite-obstruction Lemma 6.2: \(A=\varinjlim A_i\), \(B=\varinjlim B_i\), each \(A_i,B_i\) Noetherian local, with transition \(B_j\) a localization of \(B_i\otimes_{A_i}A_j\). Include \(f\) in one model. That lemma makes \(B_i/A_i\) flat eventually. It remains to ensure fibre regularity eventually, rather than assuming it.

Write \(k_i=A_i/\mathfrak m_i\), \(k=A/\mathfrak m\). For a fixed stage the ring \(\bar B_i\otimes_{k_i}k\), with \(\bar B_i=B_i/\mathfrak m_iB_i\), is essentially finite type over \(k\) and Noetherian. The map from it to the final fibre \(B/\mathfrak m B\) is localization at the images of all later denominators. Its kernel is a finitely generated ideal. Each of its generators vanishes after finitely many later denominators have been inverted. Their coefficients and those denominators occur at a common later stage \(j\). Consequently \(\bar B_j\otimes_{k_j}k\to B/\mathfrak m B\) is injective: any element in its kernel lifts after one of the already inverted denominators to the original finite kernel, which has been killed. This is the finite-kernel argument; no uniform control of infinitely many denominators is assumed.

Regularity of \(f\) in the final fibre therefore implies regularity in \(\bar B_j\otimes_{k_j}k\), and faithful field extension reflects it to \(\bar B_j\). The Noetherian lifting-injectivity lemma from Section 1, applied to \(B_j\xrightarrow fB_j\), makes \(f\) injective there and \(B_j/fB_j\) flat over \(A_j\). The same holds at later stages by base change and localization. Filtered colimits preserve these injections and preserve flatness after extending each flat model to \(A\); they give the asserted conclusions over \(A\). \(\square\)

For a regular sequence in a Cohen–Macaulay local fibre, apply this lemma successively. The earlier parameter theorem makes each quotient Cohen–Macaulay, with its dimension reduced by one. Thus every successive cut stays flat over the original base, however non-Noetherian that base is.

## 5. The source descent needed after dividing a finite relation

**Lemma 5.1 (flat finite presentations descend to a stage).** Let \(A=\varinjlim A_i\). A flat finitely presented \(A\)-algebra has a flat finitely presented model over some \(A_i\). If it is faithfully flat, the model may be made faithfully flat.

**Proof.** A finite presentation descends by putting its finitely many coefficients at one stage. To justify eventual flatness, first view \(A\) as the union of its finite-type \(\mathbf Z\)-subalgebras and model the presentation over these Noetherian rings. At every prime of the final algebra the earlier local finite-obstruction Lemma 6.2 supplies a Noetherian model flat at the contracted prime. Its Noetherian flat-locus theorem supplies a principal neighbourhood flat over that model. The images of these principal neighbourhoods cover the affine final algebra. Choose finitely many; put their equations at a common stage. Their covering condition is an identity \(1=\sum_j b_jg_j^{n_j}\), which holds at a later stage because it has finitely many coefficients. At that stage the finitely many flat localizations cover the algebra, so the model is flat globally.

This gives a flat model over a finite-type \(\mathbf Z\)-subalgebra \(A_0\subset A\). It is itself finitely presented over \(\mathbf Z\). The map \(A_0\to A\), the identification with the initially chosen model and its inverse all factor through one sufficiently late \(A_i\): choose the finitely many generator images and verify the finitely many defining equations there. Base-changing the flat \(A_0\)-model to that \(A_i\) gives the desired model over the given system. This step covers systems whose transition maps are not injective.

For faithfulness, the image of a flat finitely presented morphism is open. Let its closed complement in a chosen model be \(V(J)\). Images commute with base change: existence of a fibre point is existence of a prime in a nonzero residue-field algebra, a condition unchanged by faithfully flat field extension. If the limit model is surjective, \(JA=A\). A finite expression \(1=\sum a_\ell j_\ell\) occurs at a later stage, making the closed complement empty there. \(\square\)

**Lemma 5.2 (local finite presentation is fppf-local on the source).** If \(Z\to Y\) is a surjective flat locally finitely presented scheme morphism and \(Z\to T\) is locally finitely presented, then \(Y\to T\) is locally finitely presented.

**Proof.** Here is the algebra of the exact earlier Descending properties, Proposition 3.2, with its previously external approximation input replaced by Lemma 5.1. Reduce by finite affine refinements to \(R\to B\to C\), where \(C/R\) is finitely presented and \(C/B\) is faithfully flat finitely presented. Then \(D=C\otimes_B C\) is finitely presented over \(R\).

For a map \(B\to L=\varinjlim L_i\), the algebra \(C_L=L\otimes_B C\) is faithfully flat finitely presented over \(L\). Lemma 5.1 models it faithfully flat over some \(L_i\), as \(C_i\). Put \(D_i=C_i\otimes_{L_i}C_i\). Finite presentation of \(C/R\) and \(D/R\) descends their coefficient maps to \(C_i,D_i\) and the two commuting squares to a common later stage. The composite \(B\to C\to C_i\) has equal two images in \(D_i\), so the faithfully flat equalizer makes it factor through \(L_i\).

Every \(R\)-algebra is a filtered colimit of finitely presented \(R\)-algebras: use finitely many generators and finitely many relations at each stage. Apply the factorization just proved to its identity when this algebra is \(B\). Then \(B\) is a retract of a finitely presented \(R\)-algebra \(P\). If \(P=R[X_1,\ldots,X_n]/(r_1,\ldots,r_m)\) and the retract idempotent sends \(X_i\) to \(h_i(X)\), its image is \(P/(X_i-h_i(X))\). Applying the idempotent gives the inverse to this quotient identification. Thus \(B\) is finitely presented.

For schemes, over an affine open of \(Y\) lying above an affine open of \(T\), openness of the covering and quasi-compactness select finitely many affine source opens covering it. Their finite disjoint union yields the algebra situation. This proves the local assertion. Flatness is also local on this source cover: at local rings \(R\to B\to C\), the last map is faithfully flat, and every kernel of an \(R\)-module injection tensored with \(B\) vanishes after tensoring with \(C\), hence vanishes. \(\square\)

Target descent of flatness and local finite presentation is the complete earlier Descending properties, Theorem 2.1, with its elementary finite generators/finite relations/faithfully flat kernel proof. Open immersions descend by invariant-open and morphism descent in [Descent and Zariski Main](AG-RG-S04.md), Lemmas A1.5–A1.6.

**Lemma 5.3 (étaleness descends on the target).** An existing scheme morphism whose pullback by an fppf covering is étale is étale. Surjectivity is also detected by this covering.

**Proof.** First descend flatness and local finite presentation by the preceding elementary target-descent proof. On affine target and source charts, differential base change identifies the pulled-back differential module with \(A'\otimes_A\Omega_{B/A}\). It is zero after the faithfully flat affine refinement of the covering, hence was zero before it. The complete arbitrary-base flat, finitely presented, zero-differentials criterion, [Étale morphisms and their local structure](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/etale-morphisms-and-their-local-structure.html), Lemma 1.2 and Theorem 1.3, gives étaleness. That criterion's square Jacobian proof and the arbitrary-base square-chart flatness proof in [Smooth algebras over a field and the Jacobian criterion](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/smooth-algebras-over-a-field-and-the-jacobian-criterion.html), Theorems 5.1 and 6.1, are actual earlier proofs; no unproved smooth-fibre criterion is needed here. Surjectivity is detected because any point of the target has a point above it on the covering and, if the pullback is surjective, a further source point above that one; its image is the original target point. \(\square\)

This supplies the target-local input in the earlier étale quotient proof directly, without using its broader smoothness-descent assertion.

## 6. Transverse slicing of the relation

Let \(R\rightrightarrows U\) be a scheme equivalence relation with flat locally finitely presented projections \(s,t\). For \(g:V\to U\), write
  \[
  Z=R\times_{t,U,g}V,\quad h=s\operatorname{pr}_R,\qquad
  R_V=V\times_{g,U,t}R\times_{s,U,g}V.
  \]
The following is the complete geometric step underlying the earlier bootstrap Lemmas 3.3–3.4.

**Lemma 6.1 (good opens descend to objects).** For \(g\) locally finitely presented, the Cohen–Macaulay locus and the locally quasi-finite locus of \(h\) are inverse images of opens of \(V\).

**Proof.** On \(Z\times_V Z\), two arrows \(r_1:x_1\to g(v)\), \(r_2:x_2\to g(v)\) give \(r_2^{-1}r_1:x_1\to x_2\). The two resulting squares with \(h\), using \(s\) and \(t\), are Cartesian: for example \(r_1=r_2a\) recovers the missing arrow uniquely. Their horizontal base changes are flat and locally finitely presented. Theorem 3.4 and the faithfully flat local test for the flat locus show that the two inverse images of either good open agree. The identity gives a section \(\sigma:V\to Z\). If \(O\) is the good open, set \(W=\sigma^{-1}O\). Comparing each arrow with the identity at its target on this self-overlap proves \(O=Z\times_VW\), with scheme equality because these are open subschemes. \(\square\)

**Theorem 6.2 (slicing).** There is \(g:V\to U\) such that \(R_V\rightrightarrows V\) has flat locally finitely presented locally quasi-finite projections and \(V/R_V=U/R\) as fppf sheaves.

**Proof.** First use Lemma 6.1 with \(V=U\). It gives \(U_0\subset U\) whose inverse image under \(t\) is the Cohen–Macaulay locus of \(s\). This open meets every source fibre by Theorem 3.4 and the identity section. Hence \(t^{-1}U_0\to U\) is flat locally finitely presented and surjective. Restricting to \(U_0\) preserves the quotient: every object is locally joined to an object of \(U_0\) on this covering, and equality of two such objects is exactly their restricted relation. Inversion shows both restricted projections Cohen–Macaulay. Replace the relation by this restriction.

Fix \(u\) closed in an affine open \(\operatorname{Spec}A\subset U\), with maximal ideal \(\mathfrak m\). Around its identity choose affine arrow coordinates \(\operatorname{Spec}B\) with both endpoints in that open, and identity prime \(\mathfrak q\). The local source fibre
  \[
  D=B_{\mathfrak q}/s(\mathfrak m)B_{\mathfrak q}
  \]
is a Noetherian Cohen–Macaulay local ring of dimension \(d\). Restricting both endpoints to \(u\) gives \(D/t(\mathfrak m)D\); Corollary 2.5 makes its dimension zero.

Choose \(f_1,\ldots,f_d\in\mathfrak m\) whose target images are parameters in \(D\). They can be selected from this particular ideal: at each positive-dimensional Cohen–Macaulay quotient its finitely many associated primes are its minimal primes; none contains the whole target ideal since the quotient by that ideal has dimension zero. Finite prime avoidance in \(A\) chooses an \(f_i\) outside their inverse images. Its target image is regular, and the quotient remains Cohen–Macaulay of dimension one less. Repeat; for \(d=0\) choose the empty list.

Set \(V_u=\operatorname{Spec}A/(f_1,\ldots,f_d)\). The map \(h_u:R\times_{t,U}V_u\to U\) is locally finitely presented. At the identity its fibre is \(D/(t(f_1),\ldots,t(f_d))\). Lemma 4.1 applied successively makes it flat there with Cohen–Macaulay zero-dimensional fibre. Thus the identity belongs to both good opens of \(h_u\). Lemma 6.1 shrinks an affine neighbourhood of \(u\) in \(V_u\) so that the entire \(h_u\) is flat locally finitely presented and locally quasi-finite. Base change and inversion give these properties to both restricted projections.

Take the disjoint union of these slices over all points closed in some affine open. On a mixed pair of components its source projection is a base change of one of the \(h_u\); the same three properties hold. The image of \(h=\coprod h_u\) is open and contains all these finite-type points. If its closed complement were nonempty, intersect it with an affine open meeting it. The resulting nonempty closed subset of an affine scheme contains a point closed in that affine open, contradicting the construction. Hence \(h\) is surjective.

It is therefore an fppf cover. Every quotient object locally joins a slice object, and unique equality arrows between slice objects belong to \(R_V\). Sheafification gives \(V/R_V=U/R\) on every test scheme. The index is a set of points of \(U\); disjoint union is allowed within the fixed universe. \(\square\)

## 7. The finite part and invariant affine coordinates

**Lemma 7.1 (finite open subgroupoid).** Suppose \(U\) is affine and \(R\rightrightarrows U\) is an equivalence relation with flat locally finitely presented locally quasi-finite projections. At every \(u\in U\) there is an affine étale \(V\to U\), with image containing \(u\), and an open subgroupoid \(P\subset R_V\) having finite locally free projections.

**Proof.** The endpoint map to \(U\times_{\mathbf Z}U\) is a separated monomorphism. Both projections from this affine product are separated, so \(s,t\) are separated.

Consider the functor \(Y/U\) of clopen finite parts \(Z\subset R\times_{s,U}T\) containing the identity. Such parts are flat and locally finitely presented as opens of the given map, and finite. Here is the module argument, also present in [Descent and Zariski Main](AG-RG-S04.md), the proof of Lemma E4.2. On an affine base a finite algebra \(C\) is integral by the determinant argument. For finite algebra generators \(c_i\), choose monic equations \(P_i(c_i)=0\). The algebra \(F=A[T_i]/(P_i(T_i))\) is finite free on the bounded monomials and surjects onto \(C\). Finite presentation of \(C\) as an algebra makes this surjection's ideal kernel finitely generated; multiplying its ideal generators by the bounded monomial basis generates the kernel as an \(A\)-module. Thus \(C\) is a finitely presented module. With flatness, the complete finite-local-freeness proof in Lemma A1.3 of that lesson applies. Their inclusions and identity containment descend on fppf covers, by affine algebra, invariant-open and morphism descent.

Here is the local lifting which gives étale charts, using the now integrated scheme proof directly. A prescribed finite clopen part of \(R_u\) has finitely many selected points. Choose a quasi-compact open \(W\subset R\) containing them. Its map to the affine \(U\) is quasi-finite and separated. The complete elementary finite-pieces construction in [Descent and Zariski Main](AG-RG-S04.md), Proposition D3.3, gives a single elementary étale neighbourhood and disjoint finite open pieces for all selected points. The special fibre of each such piece is the whole Artinian component at its selected point: an open of the zero-dimensional fibre containing that point and no other point is exactly that component as a scheme. Their finite disjoint union therefore has exactly the prescribed special fibre. It is open in \(R\) and finite over the neighbourhood. It is also closed in \(R\): the graph of its map into the separated ambient \(R\) is closed, and its projection to \(R\) is finite. Pulling this clopen part back along the identity gives a clopen subset of the neighbourhood containing its marked point. Restrict to an affine principal neighbourhood there, so that the lifted part contains every identity. It is now a point of the stated functor, flat and locally finitely presented, hence finite locally free.

No henselization or finite-presentation assumption on a finite completion is used in this construction. Proposition D3.3 already constructs its elementary neighbourhood by finitely many polynomial factorization and idempotent equations. The current integrated Lemma E4.3 uses the same construction for all points of a fibre.

For two finite clopen parts on an arbitrary scheme \(T\), their differences are clopen in finite locally free schemes, hence finite locally free. Equality is represented by the clopen subset on which the ranks of both differences are zero. This equality description commutes with every base change. In particular, parts having equal special fibre agree on a neighbourhood of that base point.

The charts cover also parts defined over field extensions. A clopen finite part of a zero-dimensional locally finite-type fibre involves only finitely many of its Artinian components. After a separable closure these components are supported at single points; further field extension cannot split them: their reduced residue extensions are purely inseparable, and their radicals are nilpotent. Idempotents after a purely inseparable extension are unchanged, since that extension is radicial and induces a bijection of the underlying finite spectra. Each of the finitely many defining idempotents over the separable closure descends to a finite separable stage by its finite coefficients and equation. Thus any selected part after an arbitrary field extension, after a common field extension for comparison, comes from a finite separable residue stage. The complete elementary étale residue-neighbourhood construction realizes that stage; the lifting just proved supplies its chart. At any point of a general test \(T\), compare its given finite part with the chart part after this étale residue extension. Their equality locus is open and contains the point, proving that the charts cover the functor on all tests.

The relation between these scheme charts is clopen in their overlaps, hence is a scheme étale equivalence relation. The complete earlier étale quotient theorem constructs \(Y\) as an algebraic space, with \(Y\to U\) étale. The same equality locus is closed, so this map is separated. Theorem E8.1 and Corollary E8.2 of [Descent and Zariski Main](AG-RG-S04.md) therefore make \(Y\) a scheme, separated and étale over \(U\). Its universal finite part is a scheme.

Its groupoid has objects \((x,Z)\). For an arrow \(r:x\to y\) in \(Z\), define its target as
  \[
  (y,Zr^{-1}),\qquad Zr^{-1}=\{ar^{-1}:a\in Z\}.
  \tag{3}
  \]
Translation identifies source fibres, so this is again a clopen finite part containing the identity. It gives a morphism to \(Y\) by the representing property. Inversion sends \((x,Z,r)\) to \((y,Zr^{-1},r^{-1})\); applying it twice is the identity. The source is the universal finite locally free map, hence the target is finite locally free too. If \(r'\in Zr^{-1}\), then \(r'r\in Z\) and \(Z(r'r)^{-1}=Zr^{-1}(r')^{-1}\), proving closure under composition. All laws follow from those of \(R\).

Call this groupoid \(P\rightrightarrows Y\). Its inclusion in \(R_Y\) is open: over the universal finite open of \(R\times_{s,U}Y\), target rule (3) is a section of the étale projection \(R_Y\to R\times_{s,U}Y\), and an étale section is open by the proved étale diagonal criterion. It is an equivalence relation because its endpoints factor through those of \(R_Y\).

The Artinian component of the identity in \(R_u\) gives a \(\kappa(u)\)-point \(y\in Y\). Its \(P\)-orbit is finite. Choose a quasi-compact open of \(Y\) containing that orbit; general scheme Zariski Main makes this open quasi-affine over the affine \(U\). A finite set in a quasi-affine scheme has an affine neighbourhood: embed it as an open in an affine scheme, and use finite prime avoidance to find an element of the boundary ideal avoiding every selected prime. Its principal open lies inside the given open and contains the selected set. Let \(A\subset Y\) be such an affine neighbourhood.

Remove from \(Y\) the finite closed source image of arrows whose target lies outside \(A\). The remainder \(D\) is an invariant open, contained in \(A\) by the identity, and contains the entire orbit. Choose \(f\in\Gamma(A,\mathcal O)\) with that orbit in \(D_A(f)\subset D\), by the same finite prime avoidance. On \(D\), take the norm of the target pullback of \(f\) along the finite locally free source of \(P_D\). This gives a function \(N\). The conjugation/translation proof of norm invariance in the complete finite affine quotient proof applies on local free sheaf charts as well: the two multiplication endomorphisms are conjugate on the entire arrow scheme. Thus \(N\) is invariant, including nilpotents.

It is invertible at the selected orbit, since \(f\) is invertible at every point of each finite fibre there. Also \(D_D(N)\subset D_A(f)\): invertible determinant makes the target multiplication an invertible endomorphism of the finite locally free algebra, hence the target element a unit, and the identity makes \(f\) a unit. Since \(D_A(f)\subset D\),
  \[
  D_D(N)=D_{D_A(f)}(N)
  \]
is affine. Set \(V=D_D(N)\). It is invariant, so restricting \(P\) preserves finite locally free projections. It contains \(y\), maps étale to \(U\), and is affine. This proves the lemma. \(\square\)

## 8. Division and the flat quotient theorem

The earlier bootstrap Lemma 3.1 gives the following restriction fact with its complete test-scheme proof. If \(g:V\to U\) is open or étale, then \(V/R_V\to U/R\) is a representable open immersion onto the saturation of \(V\). For a general \(g\), it is an isomorphism if \(R\times_{t,U}V\to U\) is an fppf cover. The proof constructs the saturated open after local object lifts on a test scheme, descends its invariant open, and identifies its quotient sections by local arrow lifts. These are exactly invariant-open descent and uniqueness of equality arrows; the statement does not require the quotient already algebraic.

**Lemma 8.1 (division).** Let \(U\) be affine, \(R\rightrightarrows U\) a scheme groupoid with separated locally quasi-finite endpoint map, and \(P\subset R\) a finite locally free equivalence subgroupoid on all objects. There is a scheme groupoid \(\bar R\rightrightarrows\bar U=U/P\) whose restriction along \(q:U\to\bar U\) is \(R\), and \(U/R=\bar U/\bar R\).

**Proof.** The fully proved finite affine quotient theorem in [Descent and Zariski Main](AG-RG-S04.md), Theorem E6.1, gives \(q\) finite locally free surjective and \(P=U\times_{\bar U}U\). The map \(U\times_SU\to\bar U\times_S\bar U\) is a finite locally free cover. Give \(R\) its endpoint-transport descent datum: for \(r:x\to y\) and \(p:a\to y,\ p':b\to x\) in \(P\), send \(r\) to \(p^{-1}rp':b\to a\). Its inverse uses \(p\) and \((p')^{-1}\); associativity verifies its cocycle. Theorem E5.1 of that same lesson descends \(R\) to a scheme \(\bar R\) over \(\bar U\times_S\bar U\).

Composition descends explicitly. Locally lift two composable descended arrows to \(r:x\to y\), \(v:z\to w\). Their middle objects have the same \(q\)-image. The unique \(P\)-arrow \(a:y\to z\), from \(P=U\times_{\bar U}U\), gives \(var\). Changing the middle lifts cancels the two middle transport arrows; changing outer lifts performs the specified outer transport. Thus the composite is invariant and descends by morphism descent. Identities and inverses descend in the same manner, and all laws can be checked on the covering. If \(R\) is an equivalence relation, the monomorphism of its endpoint map is faithfully flat local and descends; hence \(\bar R\) is also an equivalence relation.

Every descended object and arrow locally lifts through \(q\) and its relation cover. Equality of two quotient sections is the local existence of an arrow. These lift and equality descriptions give \(U/R=\bar U/\bar R\) as sheaves on all tests. When \(R\) is an equivalence relation, its equality arrow is unique. \(\square\)

**Theorem 8.2 (general flat quotient).** Let \(R\rightrightarrows U\) be a groupoid in algebraic spaces over a scheme \(S\), with flat locally finitely presented source and target, and with endpoint monomorphism giving an equivalence relation. Then the fppf quotient \(Q=U/R\) is an algebraic space, \(U\to Q\) is flat locally finitely presented and surjective, and \(R=U\times_Q U\). Equivalently, an fppf sheaf admitting a representable-by-spaces flat locally finitely presented surjection from an algebraic space is algebraic.

**Proof.** Replace \(U\) by an étale scheme atlas. Local object and arrow lifts preserve the quotient and produce the restricted algebraic-space relation. Its endpoint map to the product of schemes is a locally finite-type monomorphism. To check local finite type, take affine charts of the product and of an étale scheme atlas of the arrow space. On their rings \(A\to B\to C\), the composite is finite type because an arrow projection is locally finitely presented. Its finite \(A\)-algebra generators also generate \(C\) as a \(B\)-algebra. Thus the endpoint map is locally finite type. A monomorphism is separated and has at most one geometric point in any fibre; a locally finite-type such morphism is locally quasi-finite. Theorem E8.1 and Corollary E8.2 of [Descent and Zariski Main](AG-RG-S04.md) make this restricted arrow space a scheme.

Theorem 6.2 now preserves the quotient while making its projections also locally quasi-finite. Restrict to affine open object schemes. Their quotients are representable open subfunctors by the restriction fact, and they cover. It suffices to make each such quotient algebraic, since the earlier algebraic-space open-gluing proof constructs its diagonal and atlas on these opens.

For an affine object scheme, Lemma 7.1 gives affine étale coordinates through every point with an open finite locally free subgroupoid \(P\). Their saturated quotient opens cover as well. On one coordinate scheme apply Lemma 8.1. We obtain an affine \(\bar U\), a scheme relation \(\bar R\), and the same quotient.

The descended projections are flat locally finitely presented. Indeed
  \[
  R\longrightarrow\bar R\times_{\bar U}U\longrightarrow U
  \]
has first map a base change of \(q\), finite locally free and surjective, and its composite is the original projection. Lemma 5.2 and its flat kernel proof descend the two properties along the source cover; their target descent along \(q:U\to\bar U\) descends them to \(\bar R\to\bar U\).

The unit \(\bar U\to\bar R\) is open. Its inverse image along the finite locally free surjective \(R\to\bar R\) is precisely \(P\subset R\). Open-immersion descent therefore applies.

This open unit makes the projections étale. Take any point \(x\) of a source fibre over an algebraically closed field \(\bar k\), and extend that field to \(L=\kappa(x)\). Its chosen \(L\)-valued arrow, composed with its inverse, identifies the selected point of the base-changed source fibre with an identity in another source fibre. The identity is an open \(\operatorname{Spec}L\), since the unit is open. Its point dimension is zero; Lemma 3.1 therefore gives point dimension zero at the original \(x\). The finite-type field dimension and Zariski lemmas make \(\kappa(x)\) finite over \(\bar k\), hence equal to \(\bar k\). Now the arrow is already \(\bar k\)-valued; translation in the original geometric relation identifies its local ring with the identity local ring \(\bar k\). Thus every local ring in every geometric source fibre is \(\bar k\). Such a locally finite-type fibre is a disjoint union of these reduced points, and its differential sheaf is zero. Base change of differentials, finite generation for a locally finitely presented map, and local Nakayama give \(\Omega_{\bar R/\bar U}=0\). The complete earlier étale criterion says that a flat locally finitely presented map with this unramified condition is étale. Inversion gives the other projection. The earlier étale quotient theorem now makes \(\bar U/\bar R\) an algebraic space. Open gluing completes the construction of \(Q\).

For any two object sections with the same image in \(Q\), sheafification supplies local arrows. The endpoint monomorphism makes those arrows unique, so their local restrictions agree and glue as sections of \(R\). Hence \(R=U\times_Q U\) on every test scheme.

For a scheme \(T\to Q\), choose an fppf scheme cover \(T_i\to T\) on which its quotient section lifts to \(U\), also using a scheme atlas of \(U\) when necessary. Over \(T_i\), its pullback of \(U\to Q\) is a base change of a projection of \(R\). Target descent on scheme atlases proves flatness and local finite presentation; local lifting proves surjectivity. These are the claimed properties of the algebraic-space map.

Finally a representable-by-spaces flat locally finitely presented surjection \(X\to F\) is an epimorphism of fppf sheaves. On a scheme test of \(F\), choose a scheme atlas of its surjective flat locally finitely presented pullback to \(X\); affine opens supply an fppf covering and local lifts. Its self-fibre product is an algebraic-space equivalence relation with the specified projections. The preceding construction gives its quotient; local representatives and equality arrows identify that quotient with \(F\). Conversely the quotient already has the asserted cover. \(\square\)

**Corollary 8.3 (free flat actions).** A flat locally finitely presented group algebraic space \(G/B\) acting freely on an algebraic space \(X/B\) has an algebraic-space quotient \(Q=X/G\). The map \(X\to Q\) is flat locally finitely presented surjective and is an fppf \(G\)-torsor:
  \[
  G\times_B X=X\times_Q X.
  \]

**Proof.** The action source is the base change of \(G/B\). The isomorphism \((g,x)\mapsto(g,gx)\) identifies target with another such source, so it has the same properties. Freeness is exactly the endpoint monomorphism on all tests. Apply Theorem 8.2. Local object sections trivialize the displayed torsor identity after a covering by affine opens in a scheme atlas of \(X\). \(\square\)

The construction is compatible with every base change. Indeed local quotient representatives and their unique equality arrows give the same sheaf quotient of the base-changed relation; the identity \(R=U\times_Q U\) and the covering property provide these descriptions on all tests. This assertion includes nonflat changes of base.

Comparison material actually read: the Stacks Project's [constant-field result, 04MK](https://stacks.math.columbia.edu/tag/04MK), [units, 04L5](https://stacks.math.columbia.edu/tag/04L5), [point dimension, 00P4](https://stacks.math.columbia.edu/tag/00P4), [polynomial coordinate test, 00RE](https://stacks.math.columbia.edu/tag/00RE), [Cohen–Macaulay locus, 00RH](https://stacks.math.columbia.edu/tag/00RH), [regular cuts, 046Y](https://stacks.math.columbia.edu/tag/046Y), [slicing, 0489](https://stacks.math.columbia.edu/tag/0489), [finite-part representability, 04RI](https://stacks.math.columbia.edu/tag/04RI), [finite-part groupoid, 04RU](https://stacks.math.columbia.edu/tag/04RU), and [flat bootstrap, 04S6](https://stacks.math.columbia.edu/tag/04S6). These citations acknowledge free material used to write and check the proofs; they replace none of those proofs.

The adapted Stacks arguments retain copyright of the Stacks Project authors and are supplied under GNU Free Documentation License 1.2 or any later version, with no invariant sections, no front-cover texts and no back-cover texts. The full [GNU FDL 1.2](assets/GFDL-1.2.txt) accompanies this edition, together with this source and modification history. Original exposition is additionally offered under CC0 where compatible with those retained rights. No paid work supplied a proof, mathematical template or citation.

## History

Source: *The Stacks Project*, the Stacks Project authors, copyright (C) 2005–2025 Johan de Jong, freely published by the Stacks Project under the GNU Free Documentation License, version 1.2 or later. The editable free source revision used is [a04446e57ec1fbc252a871afcec7752fb2807b14](https://github.com/stacks/stacks-project/tree/a04446e57ec1fbc252a871afcec7752fb2807b14). The source tags are identified above.

Modified edition: *Flat quotient bootstrap over an arbitrary base*, 5 October 2026. Author and publisher of this modified reconstruction draft: GPT-6.1 Sol (OpenAI), Codex, Ultra setting, for Open mathematics courses. The consumed constant-field input is proved in its pointed-domain form; dimensions, Cohen–Macaulay loci, regular cuts, finite-presentation descent, slicing, finite-part charts, division and the general flat quotient are written before their uses. Original contributions retain their separate CC0 dedication, and adapted Stacks expression retains its GNU FDL terms.
