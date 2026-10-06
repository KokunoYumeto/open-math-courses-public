# Dual kernels and an unchanged parameter

Two constructions complete the elementary localized kernel calculus. A relative dual turns a constructible kernel into a kernel for the opposite adjoint. A diagonal in an extra variable lets the original operator act while that variable remains a parameter. We will prove both constructions and keep their orientation factors and cotangent signs visible.

Use Kernels that preserve chosen cotangent directions and Adjoints of localized sheaf kernels. The exact constructibility and biduality input is Finite local data and sheaf biduality. The microlocal dual–tensor comparison is the constructible comparison in Cotangent directions that survive a limiting operation.

*Original programme exposition by GPT-6.1 Sol (OpenAI), Ultra, September 2026; source comparison and editorial revision by GPT-6 Astra (OpenAI), Ultra, October 2026. Independently expressed programme text is dedicated under CC0. Human sources retain their own terms.*

## The constructibility used by a dual kernel

The coefficient ring \(k\) is commutative with identity and finite global dimension. Manifolds are smooth, Hausdorff, finite dimensional and countable at infinity. Complexes are globally bounded. A perfect complex of \(k\)-modules means a bounded complex of finitely generated projective modules up to quasi-isomorphism; over a nonnoetherian ring, finite generation of cohomology alone is not substituted for this condition.

We use **cohomological constructibility** in its local sheaf-duality sense. At every point, the formal ind-system of ordinary cohomology on shrinking neighborhoods and the formal pro-system of compact-support cohomology are represented by perfect complexes. Their canonical comparisons identify these representatives with the stalk and costalk, respectively. Representability is an isomorphism of formal systems, not an assertion that an ordinary limit happens to be finite or that every sufficiently small neighborhood already equals the representative. The prerequisite proves the canonical compatibility and biduality statements for this condition.

On a manifold \(M\), put

\[
D'_M A=R\mathcal Hom(A,k_M),
\qquad \omega_M=\operatorname{or}_M[\dim M].
\tag{1}
\]

For a cohomologically constructible \(A\), its ordinary coefficient dual \(D'_M A\) is again cohomologically constructible, and the evaluation \(A\to D'_M D'_M A\) is an isomorphism. These follow from the corresponding Verdier-duality statements by cancelling the invertible complex \(\omega_M\). Tensoring by an invertible locally constant complex also preserves this constructibility condition.

The Hom microsupport estimate with the constant target gives

\[
\operatorname{SS}(D'_M A)\subset\operatorname{SS}(A)^a.
\]

Indeed the constant target has only zero covectors, so the noncharacteristic Hom condition is automatic. Apply this same inclusion to \(D'_M A\) and use biduality. It gives the reverse inclusion, hence

\[
\operatorname{SS}(D'_M A)=\operatorname{SS}(A)^a
\quad\text{for cohomologically constructible }A.
\tag{2}
\]

This argument uses biduality exactly where required. It makes no reflexivity claim for arbitrary sheaves.

One further precise input is needed. For cohomologically constructible \(B\) and arbitrary bounded \(E\), the evaluation morphism

\[
D'_M B\otimes^L E\longrightarrow R\mathcal Hom(B,E)
\tag{3}
\]

is a microlocal isomorphism outside
\(\operatorname{SS}(E)\widehat+_\infty\operatorname{SS}(B)^a\).
The escaping sum uses the sequence criterion for the enlarged sum, with the additional requirement that a summand covector tend to infinity. Formula (3) is not generally a global isomorphism for constructible sheaves with singular support.

## Relative duals point to different adjoints

The source of the constructible comparison is Kashiwara and Schapira, *Microlocal Study of Sheaves*, Definition 5.6.1, Proposition 5.6.2 and Corollary 5.6.4, printed pp. 98–99. They separate perfect formal local data, biduality and the comparison away from escaping covectors. Theorem 1 below uses that separation: first it cancels an invertible relative coefficient, then applies the comparison, and only afterwards uses properness to exclude escape. The distinction between the two relative coefficients in (4) remains necessary even when their cotangent relations agree.

Let \(K\) be a cohomologically constructible kernel on \(X\times Y\), and let \(q_1,q_2\) be its two projections. Define two kernels on \(Y\times X\):

\[
K_L=\mathrm t\,R\mathcal Hom(K,q_1^{-1}\omega_X),
\qquad
K_R=\mathrm t\,R\mathcal Hom(K,q_2^{-1}\omega_Y).
\tag{4}
\]

Here \(\mathrm t\) transposes the two base factors. The dualizing complex in \(K_L\) is relative to \(q_2\); the one in \(K_R\) is relative to \(q_1\). Those relative dimensions are \(\dim X\) and \(\dim Y\), respectively. The subscripts will refer to the left and right adjoints of \(\Phi_K\).

Both relative coefficient complexes are invertible. Consequently (2) says that both dual kernels have the reciprocal twisted relation: a pair \((u,v)\) for \(K\) becomes \((v,u)\). The orientation lines and shifts in (4) affect the complexes even though they do not change that relation.

**Theorem 1.** If \(K\) is forward admissible from \(\Omega_Y\) to \(\Omega_X\), then the kernel \(K_L\) on \(Y\times X\) satisfies the reverse condition selected by \(\Omega_X\), and there is a natural isomorphism

\[
\Phi_K\simeq\Psi_{K_L}:
\mathcal D_Y(\Omega_Y)\longrightarrow\mathcal D_X(\Omega_X).
\tag{5}
\]

**Proof.** Write \(W=q_1^{-1}\omega_X\) and \(Q=R\mathcal Hom(K,W)\) on \(X\times Y\). The kernel \(K_L\) is \(\mathrm tQ\). Since \(W\) is invertible,

\[
Q\simeq D'K\otimes^L W,
\qquad \operatorname{SS}(Q)=\operatorname{SS}(K)^a.
\tag{6}
\]

For \((x,y;\xi,-\alpha)\in\operatorname{SS}(K)\), the transposed dual covector is \((y,x;\alpha,-\xi)\). Thus the reverse relation for \(K_L\), selected by its input \((x,\xi)\in\Omega_X\), is exactly the reciprocal of the forward relation of \(K\). Its containment and properness are those already assumed for \(K\). The right-transform theorem therefore makes \(\Psi_{K_L}\) well-defined on the indicated quotients.

Undoing the base transposition in its ordinary formula gives

\[
\Psi_{K_L}(G)
=Rq_{1*}R\mathcal Hom(Q,q_2^!G).
\tag{7}
\]

The submersion orientation formula is \(q_2^!G=W\otimes^Lq_2^{-1}G\). Cancelling \(W\) in both Hom arguments identifies the internal Hom in (7) with \(R\mathcal Hom(D'K,q_2^{-1}G)\). Biduality identifies \(D'D'K\) with \(K\). Thus its evaluation comparison is the map

\[
K\otimes^Lq_2^{-1}G
\longrightarrow R\mathcal Hom(Q,q_2^!G),
\tag{8}
\]

obtained by tensor–Hom adjunction from \(Q\otimes K\to W\). All cancellations use evaluation and the derived tensor symmetry; orientation shifts retain their Koszul signs.

Apply (3) with \(B=D'K\), \(E=q_2^{-1}G\). Its escaping set is

\[
\operatorname{SS}(q_2^{-1}G)\widehat+_\infty\operatorname{SS}(K).
\tag{9}
\]

This set misses \(\Omega_X\times T^*Y\). To check it, a sequence for (9) has summands \((0,\gamma_n)\) and \((\xi_n,\eta_n)\), with their sum converging to an output covector whose \(X\) component is in \(\Omega_X\). The kernel's output \((x_n,\xi_n)\) eventually lies in a compact neighborhood of that component. Forward admissibility bounds its whole covector, including \(\eta_n\); convergence of \(\gamma_n+\eta_n\) bounds \(\gamma_n\). Neither summand can escape. Hence (8) has cone microsupport disjoint from that region.

Let \(C\) be its cone. The all-fibre-covector compact-control condition for \(C\) over \(\Omega_X\) is vacuous: there are no such covectors. The microlocal proper-image theorem therefore shows that \(Rq_{1*}C\) is invisible on \(\Omega_X\). Thus ordinary direct image takes (8) to a localized isomorphism. Finally the forward kernel theorem identifies proper and ordinary direct image of \(K\otimes^Lq_2^{-1}G\) on \(\Omega_X\). Combining these two canonical maps proves (5). Naturality comes from evaluation, the canonical forget-support comparison and the quotient descent of each operator. \(\square\)

**Corollary 2.** If \(K\) satisfies the reverse condition, then \(K_R\) is forward admissible in the opposite direction and

\[
\Psi_K\simeq\Phi_{K_R}.
\tag{10}
\]

If both conditions hold, the three functors form adjunctions

\[
\Phi_{K_L}\dashv\Phi_K\dashv\Phi_{K_R}.
\tag{11}
\]

**Proof.** The reciprocal relation shows that reverse admissibility of \(K\) is forward admissibility of \(K_R\). Apply Theorem 1 to \(K_R\), with the two manifolds exchanged. Its left dual is canonically \(K\): after transposition, it is the double relative dual with coefficient \(q_2^{-1}\omega_Y\), and invertible-line cancellation plus biduality gives this identification. The result is \(\Phi_{K_R}\simeq\Psi_K\), proving (10). Under both conditions both projections of the reciprocal relation are proper, so both dual kernels satisfy both conditions as well. The localized adjunction theorem therefore applies to each relevant pair. Equation (5) identifies the right adjoint of \(\Phi_{K_L}\) with \(\Phi_K\); equation (10) identifies the right adjoint of \(\Phi_K\) with \(\Phi_{K_R}\). This gives (11). \(\square\)

For example, take \(X\) to be a point and \(Y\) a compact manifold, with \(K=k_Y\). Then \(\Phi_K=R\Gamma(Y;-)\), \(K_L=k_Y\), and \(K_R=\omega_Y\). Its left adjoint is the constant-complex functor; its right adjoint tensors a constant complex with \(\omega_Y\). The reciprocal zero-section relation alone does not distinguish these two complexes.

## Inserting the identity in a parameter variable

Let \(Z\) be another smooth manifold. On \((X\times Z)\times(Y\times Z)\), with coordinates \((x,z,y,z')\), define

\[
\Theta_ZK=\operatorname{pr}_{xy}^{-1}K\otimes^L k_{\{z=z'\}}.
\tag{12}
\]

The second factor is the diagonal identity kernel on \(Z\). This construction requires no constructibility of \(K\).

**Theorem 3.** Forward admissibility of \(K\) implies forward admissibility of \(\Theta_ZK\) from \(\Omega_Y\times T^*Z\) to \(\Omega_X\times T^*Z\). For every bounded complex \(L\) on \(Y\times Z\), there is a natural isomorphism

\[
\Phi_{\Theta_ZK}(L)\simeq K\circ_YL
\quad\text{in }\mathcal D_{X\times Z}(\Omega_X\times T^*Z).
\tag{13}
\]

The construction and this identity descend in both kernel arguments. More generally, \(\Theta_ZK\) is admissible between \(\Omega_Y\times U\) and \(\Omega_X\times U\) for any open \(U\subset T^*Z\).

**Proof.** The microsupport of the first factor in (12) has zero components in both \(Z\) variables. The second factor has microsupport contained in the covectors \((0,\zeta,0,-\zeta)\) on \(z=z'\). Their only possible opposite intersection consists of zero covectors. The noncharacteristic tensor estimate therefore gives the relation containment

\[
\mathcal C_{\Theta_ZK}\subset
\{((x,\xi,z,\zeta),(y,\alpha,z,\zeta)):
((x,\xi),(y,\alpha))\in\mathcal C_K\}.
\tag{14}
\]

In particular, the unchanged \(Z\) covector is \(\zeta\) on both sides of the **twisted** relation. Its actual input component in the kernel microsupport is \(-\zeta\).

For compact \(D\subset\Omega_X\times U\), project \(D\) to its two cotangent factors. The first projection has compact preimage in \(\mathcal C_K\), and the second projection is itself compact in \(U\). The relation on the right of (14) above \(D\) is a closed subset of their product and hence compact. The actual kernel relation is a closed subset of it. This proves properness and containment, including for \(U=T^*Z\). No compactness of all of \(Z\) is required.

To prove the operator identity before localization, let
\(\delta(x,y,z)=(x,z,y,z)\).
It is a closed embedding into the fourfold product. Tensoring by \(k_{\{z=z'\}}\) identifies the tensor defining the left side of (13) with

\[
\delta_*(q_{12}^{-1}K\otimes^Lq_{23}^{-1}L)
\]

on the threefold product \(X\times Y\times Z\). This identification is the restriction map to the diagonal, checked on stalks; extension along the closed embedding is exact. The output projection composed with \(\delta\) is \(q_{13}\). Composition for proper direct image now gives (13) as an ordinary natural isomorphism. No exceptional inverse image or normal orientation shift was inserted in this closed-support calculation.

A kernel denominator for \(K\) has cone invisible on \(\Omega_X\times T^*Y\). Formula (14) puts the corresponding cone for \(\Theta_ZK\) outside its selected output region too. Thus the construction descends in \(K\). Admissibility and the convolution descent theorem handle the denominators for \(L\). The ordinary natural isomorphism therefore descends and proves the full compatibility claimed in (13). \(\square\)

## Exercises with solutions

### Two duals on a circle

*Difficulty: Intermediate.*

Take \(X=\{\mathrm{pt}\}\), \(Y=S^1\), \(k\ne0\), \(K=k_Y\), and the full cotangent regions. Choose an orientation of the circle. Compute both kernels in (4), both adjoints in (11), and their cotangent relations.

**Solution.** The coefficient for \(K_L\) is \(\omega_X=k\), so \(K_L=k_Y\). The coefficient for \(K_R\) is \(\omega_Y=k_Y[1]\) in the chosen orientation, so \(K_R=k_Y[1]\). Their left operators are respectively \(F\mapsto F_Y\) and \(F\mapsto F_Y[1]\). They are the left and right adjoints to \(R\Gamma(S^1;-)\). Both kernels have the same zero-section microsupport and reciprocal relation. A degree-zero nonzero coefficient object is placed in degree zero by the first and degree \(-1\) by the second. Thus the relation does not determine the adjoint's cohomological shift.

### Proper cotangent projections without biduality

*Difficulty: Advanced.*

Work at a point over a field \(k\). Let \(K=\bigoplus_{n\ge1}k\) in degree zero. Both cotangent conditions hold. Show that the natural map \(\Phi_K(k)\to\Psi_{K_L}(k)\) is not an isomorphism, and identify the missing hypothesis of Theorem 1.

**Solution.** All cotangent sets are points, so properness holds. But \(K\) is not perfect: its degree-zero vector space is infinite dimensional. At a point this violates cohomological constructibility. Its dual is \(K_L=K^*=\prod_{n\ge1}k\). The two sides are \(K\) and \(K^{**}=\operatorname{Hom}_k(\prod k,k)\), and the comparison is evaluation.

To see nonsurjectivity, the quotient \((\prod k)/(\bigoplus k)\) is nonzero, as the constant sequence of ones shows. Choose a nonzero linear functional on that quotient and compose with the quotient map. The resulting functional on \(\prod k\) vanishes on every finitely supported sequence but is nonzero. An evaluation functional coming from a vector of \(K\) is a finite linear combination of coordinate evaluations; if it vanishes on every coordinate vector, all its coefficients are zero. Our functional is therefore outside the image of evaluation. Theorem 1 requires constructibility in addition to its cotangent condition.

### Scaling one variable and leaving another unchanged

*Difficulty: Introductory.*

Let \(f(y)=3y\) and \(K=k_{\Gamma_f}[s]\), and take \(Z=\mathbb R\). Find the graph, twisted relation and operator of \(\Theta_ZK\).

**Solution.** The graph is \((y,z')\mapsto(3y,z')\). In kernel microsupport its equations are \(x=3y\), \(z=z'\), \(\alpha=3\xi\) and the two \(Z\) components \(\zeta,-\zeta\). The twisted relation therefore sends an input \((y,z';\alpha,\beta)\) to \((3y,z';\alpha/3,\beta)\). The operator is the direct image by this diffeomorphism followed by \([s]\). The \(Z\) variable contributes neither another antipodal sign nor a dimension shift.

### Replacing a diagonal by a constant plane

*Difficulty: Intermediate.*

For \(X=Y=\{\mathrm{pt}\}\), \(K=k\ne0\), \(Z=\mathbb R\), compare \(\Theta_ZK=k_\Delta\) with the constant-plane kernel \(k_{\mathbb R^2}\). Test their operators on \(k_\mathbb R\) and \(k_{\{0\}}\), and test admissibility on the full cotangent region.

**Solution.** The diagonal operator is the identity. The constant-plane operator gives \(k_\mathbb R[-1]\) on \(k_\mathbb R\), using compact-support cohomology of the integrated line, and \(k_\mathbb R\) on \(k_{\{0\}}\). Thus replacing the diagonal changes both tests.

The diagonal relation projects homeomorphically to its output, even on a noncompact line. The constant-plane relation lies over zero covectors but contains every intermediate base point. Above a single zero output covector it has a noncompact input zero section, so its full-region properness fails. On a punctured output region this summand is invisible instead; it still does not become the diagonal operator, since the diagonal retains the skyscraper's nonzero cotangent directions. A parameter identity is supplied by the diagonal correspondence, not by integration over a free extra variable.

## References

**Sources and the two constructions.** Kashiwara and Schapira's [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), §5.6, printed pp. 97–99, defines cohomological constructibility using representability by perfect complexes. Proposition 5.6.2 states preservation by coefficient duality, biduality and the antipodal microsupport identity. Corollary 5.6.4 proves the dual–tensor evaluation comparison away from the escaping sum by the proper/ordinary image triangle for microlocal Hom. Definition 1.2.3 and Corollary 1.2.4, p. 18, specify that sum by the limiting-sequence condition plus an unbounded summand. These are the exact constructibility and comparison inputs in (1)–(3), not a global identification of Hom with dual tensor for singular sheaves.

Proposition 6.3.1(b) and Remark 6.3.2 of that monograph, pp. 108–109, apply the comparison to kernels after properness bounds both summands. Theorem 1 uses this same compactness mechanism, but explicitly keeps the exceptional inverse image, the relative orientation coefficient, the evaluation morphism and the forget-support arrow. Corollary 2 then obtains the other adjoint by double relative duality. The source's localized-kernel discussion uses conic open regions; the compact-neighborhood proof here retains the arbitrary open regions and bounded categories established in the preceding two lessons. The orientation and finite-amplitude prerequisites are not consequences of the cotangent relation alone.

For the parameter construction, Pierre Schapira's [*A short review on microlocal sheaf theory*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), 19 January 2016, Theorem 2.8 and Corollary 2.12, pp. 10 and 13, give the external and noncharacteristic tensor estimates; §2.4, pp. 13–14, defines convolution. Theorem 3 combines these mechanisms with the diagonal's conormal, checks compactness over each output compact set, and identifies the operator through the actual closed diagonal embedding. This proves the unchanged parameter and its covector sign, including noncompact parameter manifolds and arbitrary bounded coefficients. The survey's general convolution estimate has its own support-properness and transversality assumptions; it is not substituted for the present localized admissibility proof.

The circle calculation distinguishes the two relative duals by their shifts; the infinite-dimensional point example isolates failure of biduality; the scaling and constant-plane examples test why the diagonal carries the identity parameter. Those worked arguments, and the proof by the closed diagonal embedding, are the lesson's teaching presentation of the constructions. The full constructible-biduality supplier and the enlarged and escaping estimates remain the named prerequisite proofs. Astérisque 128 states part of its duality input without a detailed derivation, and the survey explicitly delegates parts of its sheaf-operation calculus. These citations identify the mathematics used, without claiming complete transitive foundation closure or copying the human sources' expression or diagrams.

- Masaki Kashiwara and Pierre Schapira, *Microlocal Study of Sheaves*, Astérisque 128 (1985), §1.2, §5.6 and §6.3, at the locators above.
- Pierre Schapira, *A short review on microlocal sheaf theory*, 19 January 2016, §§2.3–2.4, at the locators above.
