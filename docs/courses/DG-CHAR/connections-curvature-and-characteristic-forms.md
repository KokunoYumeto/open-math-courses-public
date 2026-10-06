# Connections, curvature and characteristic forms

*Written and self-checked by the writing AI, GPT-6.1 Sol (OpenAI), at Ultra. Independently authored text dedicated under CC0. No independent mathematical review is recorded.*

A connection gives a bundle a differential calculus. Its curvature changes when the connection changes, yet invariant polynomials in that curvature give cohomology classes that stay fixed. We prove that assertion with an explicit primitive for the change, then identify the normalized forms with the real images of the integral characteristic classes already constructed. A Gaussian Thom form supplies the Euler normalization and yields generalized Gauss–Bonnet. The unit sphere and the tautological line on the projective line make the two central signs visible.

This chapter covers assigned lesson17. Six graded exercises have complete solutions. The needed de Rham comparison, its product and open-pair statements, and its orientation normalization are proved in PartA. Connection and geometric convexity foundations use the exact, fully read DG-FND proofs identified below. The detailed invariant-polynomial, Mathai–Quillen and characteristic-class arguments are supplied here.

The preceding [Thom/Euler](thom-classes-and-euler-classes.md), [Gysin/projective](gysin-sequence-and-projective-splitting.md), [Chern](chern-classes-and-the-integral-universal-ring.md), [Pontryagin](pontryagin-classes-and-oriented-universal-cohomology.md), [Schubert](schubert-cells-and-grassmannian-cohomology.md), and [manifold](manifold-duality-the-diagonal-and-wu-classes.md) chapters supply the exact singular-chain, splitting, integral normalization, symmetric-polynomial, fundamental-class and Euler-characteristic proofs used here. The arguments apply to finite-dimensional Hausdorff second-countable smooth bases without boundary. Generalized Gauss–Bonnet concerns closed oriented manifolds. Real forms represent coefficient images; integer characteristic classes and their torsion information retain their earlier definitions.

## A. Differential forms and the cohomology comparison

Throughout this lesson a smooth manifold is finite dimensional, Hausdorff and second countable, without boundary. Cohomology without a displayed coefficient group in this part has coefficients \(\mathbb R\). Complex-valued forms give the same constructions with \(\mathbb C\). Orientations and integration use the usual ordered-coordinate convention: \(dt_1\wedge\cdots\wedge dt_n\) is positive in an oriented coordinate chart.

### A.1. The differential and integration

A \(q\)-form is a smooth section of \(\Lambda^qT^*M\). In coordinates it has the form
\[
 \omega=\sum_{i_1<\cdots<i_q} f_{i_1\ldots i_q}
 dx^{i_1}\wedge\cdots\wedge dx^{i_q}.
\]
Define \(d\omega\) by differentiating each coefficient and wedging its differential on the left. This definition satisfies
\[
 d(\alpha\wedge\beta)=d\alpha\wedge\beta+
 (-1)^{\deg\alpha}\alpha\wedge d\beta,\qquad d^2=0.
\tag{A.1}
\]
The first identity follows by moving the new one-form past the factors of \(\alpha\). The second follows because the mixed second partial derivatives agree and the associated \(dx^i\wedge dx^j\) have opposite signs. These definitions agree under a smooth change of coordinates: the chain rule gives the same differential on functions, and \(d(df)=0\) shows that no extra derivative of the coordinate one-forms remains. Functions and their coordinate differentials generate the local algebra, so the product rule gives agreement on every form. This also proves that smooth pullback commutes with \(d\) and exterior products.

The **de Rham cohomology** is
\[
 H_{\mathrm{dR}}^q(M)=
 \ker(d:\Omega^q\to\Omega^{q+1})/
 \operatorname{im}(d:\Omega^{q-1}\to\Omega^q).
\tag{A.2}
\]
Equation (A.1) makes exterior multiplication a product on these groups.

For a smooth simplex \(\sigma:\Delta^q\to M\), set
\[
 I(\omega)(\sigma)=\int_{\Delta^q}\sigma^*\omega.
\tag{A.3}
\]
Here smooth means that the simplex extends smoothly to a neighbourhood of its closed domain. The standard simplex has vertices \(0,e_1,\ldots,e_q\) and its usual positive coordinate orientation. For \(q\geq1\), Stokes' formula on that simplex is
\[
 \int_{\Delta^q}d\beta
 =\sum_{j=0}^q(-1)^j
 \int_{\Delta^{q-1}}\beta|_{[0,\ldots,\widehat j,\ldots,q]}.
\tag{A.4}
\]
One can verify it directly. Write
\(\beta=\sum_i(-1)^{i-1}b_i\,dt_1\wedge\cdots\widehat{dt_i}\cdots\wedge dt_q\).
Then \(d\beta=\sum_i\partial_i b_i\,dt_1\wedge\cdots\wedge dt_q\).
For each fixed choice of the other coordinates, integrate \(t_i\) from zero to \(1-\sum_{j\ne i}t_j\). The fundamental theorem of calculus gives the negative term on \(t_i=0\) and the positive term on the sloping face. Parametrizing those faces by the remaining coordinates gives exactly their alternating oriented face signs in (A.4). Summing over \(i\) proves the formula; in degree one it is the fundamental theorem itself.

It follows that \(I(d\omega)=\delta I(\omega)\). Thus integration is a cochain map to the cochains on smooth singular simplices. We will prove that it identifies (A.2) with the singular cohomology used earlier, including products and the positive local orientation generators.

We also use integration of compactly supported top forms on an oriented manifold. A subordinate smooth partition of unity reduces it to coordinate integrals; the ordinary change-of-variables formula makes the result independent of the partition and coordinates. For a compactly supported \((n-1)\)-form on a manifold without boundary,
\[
 \int_M d\beta=0.
\tag{A.5}
\]
Indeed split \(\beta\) into finitely many compactly supported coordinate pieces on a neighbourhood of its support. Their differentiated sum is \(d\beta\), since the differentiated weights sum to zero. Each coordinate integral is zero by successive one-dimensional integration of a compactly supported derivative. This is the form of Stokes' theorem used on closed manifolds below.

### A.2. Homotopies and a good cover

For a smooth homotopy \(H:[0,1]\times U\to V\), decompose
\[
 H^*\omega=dt\wedge\beta_t+\gamma_t,
 \qquad K\omega=\int_0^1\beta_t\,dt.
\]
The \(dt\) component of \(dH^*\omega\) is
\(dt\wedge(\partial_t\gamma_t-d\beta_t)\).
Integrating that equality proves
\[
 H_1^*-H_0^*=dK+Kd.
\tag{A.6}
\]
All operations are smooth on compact parameter intervals and can be checked coefficient by coefficient. Consequently a smoothly contractible nonempty open set has de Rham cohomology \(\mathbb R\) in degree zero and zero in positive degrees: apply (A.6) to a contraction to one point. Closed zero-forms are constant on a connected set by differentiation along paths.

A **good cover** is an open cover for which every nonempty finite intersection is smoothly contractible. Here is a construction with the precise geometric premise. Give \(M\) a positive metric, whose existence was proved in DG-FND, *Linear and affine connections*, Theorem2.1. DG-FND, *Riemannian connections and convex neighbourhoods*, Theorem4.1, proves that every point has arbitrarily small strongly convex neighbourhoods. Each ordered pair in such a neighbourhood is joined by a unique minimizing geodesic in the whole connected component, with smooth endpoint dependence. Its proof, including the complete local affine-convexity and differential-equation prerequisites, is part of the exact provider reading for this lesson.

Choose a countable locally finite cover by these neighbourhoods. To see local finiteness explicitly, use a compact exhaustion \(K_j\subset\operatorname{int}K_{j+1}\) with union \(M\), as in the already proved partition-of-unity construction. Cover each compact layer \(K_j\setminus\operatorname{int}K_{j-1}\) by finitely many sufficiently small convex neighbourhoods lying in
\(\operatorname{int}K_{j+1}\setminus K_{j-2}\), with compact closures there. The resulting family is locally finite: a neighbourhood inside \(\operatorname{int}K_N\) misses all layers' chosen sets with \(j\geq N+2\), and only finitely many sets have smaller indices. The construction may also be made subordinate to any prescribed open cover by choosing the neighbourhoods small enough.

If \(U=U_{i_0}\cap\cdots\cap U_{i_p}\) is nonempty, fix \(a\in U\). The geodesic from \(a\) to \(x\in U\) supplied by any one member \(U_{i_j}\) is the same as that supplied by every other member: all are minimizing in the whole manifold, and each member asserts uniqueness there. Thus the segment stays in their intersection. Its smooth dependence in one member gives a smooth contraction of \(U\) to \(a\). The cover is good. In dimension zero take the singleton neighbourhoods. Each has the same contraction assertion.

### A.3. Two local-to-global cochain arguments

We give the comparison argument to avoid treating a topological class and a form as automatically interchangeable. Order the good cover by its countable index set. For each increasing tuple \(J=(i_0,\ldots,i_p)\), put \(U_J=\bigcap_{i\in J}U_i\), omitting empty intersections. Form the double complex
\[
 \mathcal D^{p,q}=\prod_{i_0<\cdots<i_p}\Omega^q(U_J),
 \qquad d_{\mathrm{tot}}=\check\delta+(-1)^p d.
\tag{A.7}
\]
The horizontal differential is the alternating sum of restrictions, and \(\check\delta^2=0\) by cancellation of twice omitted indices. Restrictions commute with \(d\), so the total differential squares to zero.

First the horizontal rows, augmented by the restrictions of \(\Omega^q(M)\), are exact. Let \(\rho_i\) be a subordinate locally finite smooth partition of unity. Extend alternating arrays to all tuples by the sign of reordering and by zero on a repeated index. The row contraction is
\[
 (hc)_{i_0\ldots i_{p-1}}=
 \sum_j\rho_j c_{j i_0\ldots i_{p-1}}.
\tag{A.8}
\]
Each term, originally defined on \(U_j\cap U_{i_0}\cap\cdots\), extends by zero because \(\operatorname{supp}\rho_j\subset U_j\). Local finiteness makes the sum smooth. Expanding the alternating differentials gives
\(\check\delta h+h\check\delta=1\), using \(\sum_j\rho_j=1\); for the augmented term this is the same gluing formula. Hence restriction from the global de Rham complex to (A.7) induces an isomorphism on total cohomology.

Second, each vertical column has cohomology equal to the constants in degree zero and zero above it, by the smooth contractions in A.2. Products cause no difficulty: a primitive for each tuple gives a primitive in the product. Thus the inclusion of the ordinary Čech complex
\[
 \check C^p(\mathcal U;\mathbb R)
 =\prod_{i_0<\cdots<i_p}\mathbb R
\tag{A.9}
\]
as constant zero-forms also induces an isomorphism on total cohomology.

Here is an elementary justification of both total-complex statements. A total cocycle of degree \(N\) has only the \(N+1\) bidegrees \((p,N-p)\). For exact columns above the constants, its component \((0,N)\), when \(N>0\), is vertically closed by the cocycle equation. Remove it by a total coboundary using a vertical primitive. Then remove \((1,N-1)\), and continue while \(q>0\), choosing the primitive with the sign \((-1)^p\) of the vertical differential. Only \((N,0)\) remains; its vertical derivative is zero, so its entries are constants, and its horizontal derivative is zero. This proves surjectivity from (A.9). For injectivity, suppose a constants cocycle is \(d_{\mathrm{tot}}b\). The same elimination applied to \(b\), by subtracting total coboundaries from \(b\), preserves \(d_{\mathrm{tot}}b\). Its positive-\(q\) components are vertically closed successively because that derivative has only \(q=0\). The final component of \(b\) is a constants array, whose horizontal coboundary is the original constants cocycle. Degree zero has no boundaries and the assertion is immediate.

For exact augmented rows, start instead with the component of a total cocycle having largest \(p>0\). Its horizontal derivative is zero by the cocycle equation, so a horizontal primitive removes it. Continue with decreasing \(p\). At the end the \(p=0\) component has horizontal derivative zero and is the restriction of one global element by row exactness. Its vertical derivative is zero, so that global element is closed. For injectivity, if the restriction of a global cocycle is \(d_{\mathrm{tot}}b\), eliminate the largest positive-\(p\) components of \(b\) while preserving its derivative. The remaining \(p=0\) component is the restriction of a global element, and its derivative is the original global cocycle; restriction is injective. This proves injectivity too. Both arguments are finite inductions in each total degree, even when the cover is infinite.

Repeat the construction with continuous singular cochains \(C^q(U_J;\mathbb R)\), or with smooth singular cochains \(C_{\mathrm{sm}}^q(U_J;\mathbb R)\), in place of forms. Their vertical cohomology is again just the constants: the contractions give the prism chain homotopy of the Thom/Euler chapter, Lemma1.1. In the smooth case all prism parametrizations are affine and the homotopy is smooth, so every resulting simplex is smooth. The point complex computation in that lemma gives the asserted cohomology.

For the augmented horizontal rows, use the cochains on **small** simplices of \(M\), whose images lie in some cover member. For each such simplex \(\sigma\), let \(j(\sigma)\) be the first member containing it. The contraction is (A.8) with its sum of weighted terms replaced, at \(\sigma\), by the single term
\[
 (hc)_{i_0\ldots i_{p-1}}(\sigma)
 =c_{j(\sigma)i_0\ldots i_{p-1}}(\sigma).
\tag{A.10}
\]
Every required evaluation is defined when \(\sigma\) lies in all the indicated members. The same alternating cancellation proves the row identity. Compatibility of this contraction with the vertical differential is unnecessary for exactness of a fixed row and the finite elimination just proved.

Small cochains have the cohomology of all singular cochains. The full chain homotopy equivalence was proved in the Thom/Euler chapter, Lemma2.1. That proof uses only affine subdivision, affine cones within a standard simplex, and composition with the original simplex. Every operation therefore also preserves smoothness, and proves the same small-chain equivalence for smooth simplices. Dualizing a chain homotopy gives the required cochain homotopy.

We now have quasi-isomorphisms from each of the three global complexes—forms, continuous singular cochains, and smooth singular cochains—to its corresponding total complex. All three total complexes have the same constants complex (A.9) as a quasi-isomorphic subcomplex. Integration (A.3) on every \(U_J\) commutes with both differentials by (A.4), and is the identity on constants. Restriction from continuous to smooth cochains is also the identity on constants. It follows that integration induces an isomorphism to smooth singular cohomology and that continuous-to-smooth restriction induces an isomorphism. Their composite comparison defines
\[
 \mathcal I:H_{\mathrm{dR}}^*(M)
 \ \xrightarrow{\ \cong\ }\ H^*(M;\mathbb R).
\tag{A.11}
\]

This comparison is multiplicative. To verify this without assuming that simplex integration itself preserves cup products, give each double complex the product
\[
 (a b)_{i_0\ldots i_{p+p'}}
 =(-1)^{q p'}\,
 a_{i_0\ldots i_p}\,b_{i_p\ldots i_{p+p'}},
\tag{A.12}
\]
for bidegrees \((p,q)\) and \((p',q')\), restricting both factors to the common intersection. Use wedge products for forms and the already proved singular cup product for cochains. The alternating horizontal differential and the internal differential satisfy the product rule with total-degree sign: expanding the former cancels the interior omitted-index terms, and the latter is the ordinary graded product rule with the additional sign in (A.12). Restrictions from each global complex preserve this product, as does inclusion of (A.9). Thus both cohomology rings are identified with the same Čech cohomology ring. Integration's cohomology map is that same identification because it commutes with the constant inclusions. This proves the product assertion.

The map (A.11) is natural. At the cochain level, integrating \(f^*\omega\) over \(\sigma\) is integrating \(\omega\) over \(f\circ\sigma\), so integration commutes with smooth maps. Continuous-to-smooth restriction commutes with them too. Consequently the isomorphism obtained above has the required pullback naturality, regardless of which good covers were used to prove it.

### A.4. Open pairs and orientation evaluation

For an open subset \(V\subset M\), define the relative form complex as
\[
 \Omega^q(M,V)=\Omega^q(M)\oplus\Omega^{q-1}(V),
 \quad
 d(\omega,\eta)=(d\omega,\omega|_V-d\eta).
\tag{A.13}
\]
Its long exact sequence follows from its projection to the first summand and its subcomplex consisting of the second summand; the connecting map is restriction. Apply integration to both summands. The absolute comparison (A.11) for \(M\) and \(V\), their naturality, and the exact sequences give an isomorphism
\[
 H_{\mathrm{dR}}^q(M,V)\cong H^q(M,V;\mathbb R).
\tag{A.14}
\]
To see the last target explicitly, restriction of singular cochains to \(V\) is surjective: extend a cochain by zero on the basis simplices not lying in \(V\). Its kernel is the relative singular complex. The kernel's inclusion into its restriction cone is a quasi-isomorphism: quotienting that cone by the kernel gives the cone of the identity on \(C^*(V)\), whose contraction is \(h(\omega,\eta)=(\eta,0)\). For the differential \((\delta\omega,\omega-\delta\eta)\), direct substitution gives \(dh+hd=1\). This proves the identification used in (A.14), with the signs in (A.13).

For a closed relative chain \(c\) with \(\partial c=b\) lying in \(V\), the pairing with \((\omega,\eta)\) is
\[
 \int_c\omega-\int_b\eta.
\tag{A.15}
\]
Stokes proves that it is unchanged by relative boundaries when (A.13) is closed. In particular a closed form vanishing on \(V\) represents \((\omega,0)\), and its pairing on a positive relative coordinate ball is its ordinary integral.

The comparison respects manifold orientations and top-degree integration. Use a partition subordinate to oriented coordinate neighbourhoods whose coordinate images are open cubes. Each compactly supported piece can be enclosed in a slightly smaller positive closed cube in that same chart. Triangulate this cube by the explicit ordered simplices of the earlier chain-product construction. Its positive relative chain is the local fundamental class; (A.3) evaluates the piece by its ordinary coordinate integral. Excision and local detection of fundamental classes identify this evaluation with the evaluation of its singular class on the manifold's fundamental class. For a closed oriented manifold only finitely many pieces are needed. Each is closed, since there are no forms of degree greater than the dimension. Adding their local evaluations gives
\[
 \langle\mathcal I[\omega],[M]\rangle=\int_M\omega.
\tag{A.16}
\]
The same positive-ball argument proves the fibre normalization in open relative pairs. No global triangulation of the manifold enters this comparison.

## B. Curvature polynomials and their primitives

We use column coordinates for sections: in a local frame \(e\),
\(\nabla(ev)=e(dv+Av)\). The exact DG-FND proofs in *Linear and affine connections*, Sections1–2, and *Curvature and holonomy groups*, Sections1–3, give
\[
 A'=g^{-1}Ag+g^{-1}dg,\qquad
 F=dA+A\wedge A,\qquad F'=g^{-1}Fg.
\tag{B.1}
\]
Here matrix products include exterior products of the entries. For an endomorphism-valued \(q\)-form put
\[
 D\beta=d\beta+A\wedge\beta-(-1)^q\beta\wedge A.
\tag{B.2}
\]
The same proofs establish \(DF=0\), the Bianchi identity. Connections exist, their differences are global endomorphism-valued one-forms, and compatible connections exist for positive real or Hermitian metrics. These are the precise provider statements used below. Transport and holonomy are unnecessary for the argument.

### B.1. Evaluate an invariant polynomial on forms

Let \(\mathfrak g\) be either \(\mathfrak{gl}(r,\mathbb C)\) or \(\mathfrak{so}(r)\), with frame group \(G=\mathrm{GL}(r,\mathbb C)\) or \(G=\mathrm{SO}(r)\), respectively. Let \(P\) be a \(G\)-invariant homogeneous polynomial of degree \(k\geq1\). Its symmetric polarization is the unique symmetric \(k\)-linear function \(p\) with
\(p(X,\ldots,X)=P(X)\). Explicitly,
\[
 p(X_1,\ldots,X_k)=\frac1{k!}
 \left.\frac{\partial^k}{\partial t_1\cdots\partial t_k}
 P(t_1X_1+\cdots+t_kX_k)\right|_{t=0}.
\tag{B.3}
\]
Expanding a degree-\(k\) monomial proves both multilinearity and the diagonal identity. It also proves uniqueness: the coefficient of \(t_1\cdots t_k\) in a diagonal evaluation determines the multilinear function.

For \(\mathfrak g\)-valued differential forms \(\beta_j=\sum_a\beta_j^a X_a\), define
\[
 p(\beta_1,\ldots,\beta_k)
 =\sum_{a_1,\ldots,a_k}
 p(X_{a_1},\ldots,X_{a_k})
 \beta_1^{a_1}\wedge\cdots\wedge\beta_k^{a_k}.
\tag{B.4}
\]
Multilinearity makes this independent of the chosen basis. Interchanging two arguments of degrees \(u,v\) introduces the sign \((-1)^{uv}\). Polarization of the invariance of \(P\) makes \(p\) invariant when all its arguments are conjugated by the same \(g\). Consequently
\[
 P(F):=p(F,\ldots,F)
\tag{B.5}
\]
is a globally defined \(2k\)-form. Equivalently one can substitute the two-form entries of \(F\) directly into the polynomial: those entries commute, and expansion gives (B.5).

**Lemma B.1 — Differentiate an invariant contraction.** If the degree of \(\beta_j\) is \(q_j\), then
\[
 d\,p(\beta_1,\ldots,\beta_k)
 =\sum_{j=1}^k(-1)^{q_1+\cdots+q_{j-1}}
 p(\beta_1,\ldots,D\beta_j,\ldots,\beta_k).
\tag{B.6}
\]

**Proof.** Ordinary differentiation of (B.4) gives the same formula with \(d\beta_j\) in place of \(D\beta_j\). Differentiate simultaneous conjugation by \(\exp(tZ)\) at zero. This gives the algebraic identity
\[
 \sum_jp(X_1,\ldots,[Z,X_j],\ldots,X_k)=0.
\tag{B.7}
\]
To check all the signs in the additional connection terms, it suffices by linearity to take \(A=aZ\) and \(\beta_j=b_jX_j\), where \(a\) is a one-form and \(b_j\) has degree \(q_j\). The graded commutator in (B.2) is
\([A,\beta_j]=a\wedge b_j[Z,X_j]\): in the second product moving \(a\) past \(b_j\) cancels the displayed \((-1)^{q_j}\). In the \(j\)-th summand of (B.6), moving this \(a\) to the front contributes \((-1)^{q_1+\cdots+q_{j-1}}\), which cancels that summand's original sign. The remaining sum is \(a\wedge b_1\wedge\cdots\wedge b_k\) multiplied by (B.7), and is zero. ∎

**Theorem B.2 — Closedness and explicit transgression.** The form \(P(F)\) is closed. Its de Rham class depends only on the bundle and \(P\). If \(\nabla^0,\nabla^1\) are two connections, write \(\alpha=\nabla^1-\nabla^0\), let \(\nabla^t=\nabla^0+t\alpha\), and denote its curvature by \(F_t\). Then
\[
 P(F_1)-P(F_0)=d\,\operatorname{CS}_P(\nabla^0,\nabla^1),
\qquad
 \operatorname{CS}_P=k\int_0^1p(\alpha,F_t,\ldots,F_t)\,dt.
\tag{B.8}
\]
For an orthogonal frame group both connections are required to be compatible with the same metric. Their affine path is again compatible.

**Proof.** Apply (B.6) to \(k\) copies of \(F\). Every degree is even, and \(DF=0\), so \(dP(F)=0\). Differentiate the local formula for \(F_t\):
\[
 \dot F_t=d\alpha+A_t\wedge\alpha+\alpha\wedge A_t
 =D_t\alpha.
\tag{B.9}
\]
Symmetry and the even degrees of the curvature arguments give
\[
 \frac{d}{dt}P(F_t)
 =k\,p(D_t\alpha,F_t,\ldots,F_t)
 =k\,d\,p(\alpha,F_t,\ldots,F_t).
\tag{B.10}
\]
In the last equality the remaining terms of (B.6) contain \(D_tF_t=0\). Integration in \(t\) proves (B.8). The primitive is global: the connection difference transforms by conjugation without the \(g^{-1}dg\) term, and so do all the curvatures. Smooth integration over a compact parameter interval commutes with \(d\), as is checked on each coefficient in a coordinate chart. Thus the difference of forms is exact. Pullback of the local connection and curvature formulas also proves naturality under every smooth base map. ∎

A nonhomogeneous polynomial is handled degree by degree, including its constant term. An invariant formal power series also makes sense: on a finite-dimensional base only finitely many of its positive-degree curvature terms survive. No assertion about integer periods has been used in this theorem.

### B.2. The characteristic forms to be identified

For a complex rank-\(r\) bundle define
\[
 \det\!\left(I+t\frac{iF}{2\pi}\right)
 =\sum_{j=0}^r t^j c_j(\nabla),\qquad
 \operatorname{ch}(\nabla)=\operatorname{tr}
 \exp\!\left(\frac{iF}{2\pi}\right).
\tag{B.11}
\]
Thus \(c_0=1\), \(c_1=(i/2\pi)\operatorname{tr}F\), and
\[
 c_2=\frac12\left(\frac{i}{2\pi}\right)^2
 \bigl((\operatorname{tr}F)^2-\operatorname{tr}(F\wedge F)\bigr).
\tag{B.12}
\]
Their polynomials are invariant, so all these forms are closed and have the exact transgression of Theorem B.2. A block diagonal connection has block diagonal curvature; the determinant therefore multiplies under a direct sum, while the trace of the exponential adds.

For a real bundle, complexify its connection and set
\[
 p_j(\nabla)=(-1)^j c_{2j}(\nabla_{\mathbb C}).
\tag{B.13}
\]
This is precisely the coefficient of \(t^{2j}\) in
\(\det(I+tF/2\pi)\), since \(i^{2j}=(-1)^j\). For a metric connection,
\[
 p_1(\nabla)=-\frac1{8\pi^2}\operatorname{tr}(F\wedge F).
\tag{B.14}
\]
Indeed its skew matrix has trace zero, and (B.12)–(B.13) give (B.14). For an arbitrary real connection the coefficient (B.13) is
\[
 \frac1{8\pi^2}
 \bigl((\operatorname{tr}F)^2-\operatorname{tr}(F\wedge F)\bigr).
\tag{B.14a}
\]
Its class still agrees with the class of (B.14). The trace polynomial has zero curvature form for a metric connection, so transgression supplies a global one-form \(b\) with \(\operatorname{tr}F=db\). The additional term is exact because \((\operatorname{tr}F)^2=d(b\wedge db)\).

For a metric connection every odd coefficient of \(\det(I+tF/2\pi)\) vanishes: transposition gives \(\det(I+tF)=\det(I-tF)\). For any other real connection those odd coefficient forms are exact by (B.8).

**Exercise B.3 — A complete transgression calculation (medium).** For two complex connections, prove that their forms for any homogeneous invariant polynomial differ by an exact form. Then find an explicit primitive for
\(\operatorname{tr}(F_1\wedge F_1)-\operatorname{tr}(F_0\wedge F_0)\).

**Solution.** Put \(\alpha=\nabla^1-\nabla^0\), \(\nabla^t=\nabla^0+t\alpha\). For a degree-\(k\) invariant polynomial with polarization \(p\), differentiating the curvature gives \(\dot F_t=D_t\alpha\). The product rule for an invariant contraction and Bianchi therefore give
\[
 \frac{d}{dt}p(F_t,\ldots,F_t)
 =k\,p(D_t\alpha,F_t,\ldots,F_t)
 =k\,d\,p(\alpha,F_t,\ldots,F_t).
\]
Integrate from zero to one. The globally defined primitive is \(k\int_0^1p(\alpha,F_t,\ldots,F_t)\,dt\): all arguments transform by conjugation on an overlap, so invariance makes their contraction independent of the frame. This proves exactness for every such polynomial.

For the requested calculation, polarization of \(P(X)=\operatorname{tr}X^2\) is
\(p(X,Y)=\tfrac12\operatorname{tr}(XY+YX)\). With a one-form and a two-form the trace permits cyclic exchange with sign \(+1\), so \(p(\alpha,F_t)=\operatorname{tr}(\alpha\wedge F_t)\). Furthermore
\[
 F_t=F_0+tD_0\alpha+t^2\alpha\wedge\alpha.
\]
Substitution in (B.8) gives the global three-form
\[
 2\operatorname{tr}(\alpha\wedge F_0)
 +\operatorname{tr}(\alpha\wedge D_0\alpha)
 +\frac23\operatorname{tr}(\alpha\wedge\alpha\wedge\alpha).
\tag{B.15}
\]
Its exterior derivative is the requested difference, by (B.9)–(B.10). This formula does not require a global frame: each of \(\alpha,F_0,D_0\alpha\) transforms by conjugation. ∎

## C. A normalized Thom form and the Euler form

Let \(E\to M\) be an oriented real bundle of rank \(r=2m>0\), equipped with a positive metric and a compatible connection. The base is a finite-dimensional Hausdorff second-countable smooth manifold without boundary. Write \(\pi:E\to M\). In an oriented orthonormal frame its connection and curvature matrices are skew:
\[
 A^T=-A,\qquad F^T=-F.
\tag{C.1}
\]
The second identity follows either from the connection on the metric tensor, or directly by transposing \(dA+A\wedge A\): transposing the product of two one-form matrices contributes an additional minus sign.

### C.1. Fix the Pfaffian convention

For a skew \(2m\times2m\) matrix \(B\) with commuting entries, introduce formal exterior generators \(\theta_1,\ldots,\theta_{2m}\) and define
\[
 \operatorname{Pf}(B)=
 [\theta_1\cdots\theta_{2m}]
 \exp\!\left(\sum_{i<j}B_{ij}\theta_i\theta_j\right).
\tag{C.2}
\]
The brackets mean take the coefficient of the ordered top exterior monomial. Only the \(m\)-th power contributes, so this is a polynomial. Its coefficients are integers: expansion groups the ordered factors into unordered pairings, and the factor \(m!\) in the exponential cancels the orderings of the pairs. For example,
\[
 \operatorname{Pf}
 \begin{pmatrix}0&b\\-b&0\end{pmatrix}=b,
 \qquad
 \operatorname{Pf}(B)_{r=4}
 =B_{12}B_{34}-B_{13}B_{24}+B_{14}B_{23}.
\tag{C.3}
\]
Changing generators by a matrix \(Q\) multiplies their top exterior monomial by \(\det Q\). Apply this change to the alternating two-tensor in (C.2) to obtain
\[
 \operatorname{Pf}(QBQ^T)=\det(Q)\operatorname{Pf}(B).
\tag{C.4}
\]
This polynomial identity holds over every commutative ring because it follows by expansion with integer coefficients.

For completeness, \(\operatorname{Pf}(B)^2=\det B\). First take a real skew matrix. The symmetric operator \(-B^2\) has nonnegative eigenvalues. If \(v\) is a unit eigenvector with eigenvalue \(\lambda^2>0\), then \(v,Bv/\lambda\) are orthonormal, their span is \(B\)-invariant, and its orthogonal complement is \(B\)-invariant. Repeating gives orthogonal two-dimensional blocks and a zero block on the kernel. On these blocks the identity is immediate from (C.3), and (C.4) proves it in the original frame. Since the difference of the two polynomials vanishes at every real assignment of its independent entries, it is the zero polynomial: successively regard it as a one-variable polynomial with the other real variables fixed. The identity therefore holds over every commutative ring.

Substitution of the commuting two-form entries of \(F\) is legitimate. Equation (C.4) with \(Q\in\mathrm{SO}(2m)\) proves that
\[
 \mathcal E(\nabla)=\operatorname{Pf}\!\left(\frac{F}{2\pi}\right)
\tag{C.5}
\]
is a global real \(2m\)-form. We now construct a Thom form whose restriction to the zero section is exactly (C.5). This will also fix its normalization as the topological Euler class.

### C.2. An exterior algebra with two degrees

On the total space \(E\), work in
\[
 \mathscr A^{a,b}=\Omega^a(E;\Lambda^b\pi^*E)\otimes_{\mathbb R}\mathbb C.
\tag{C.6}
\]
The multiplication is
\[
 (\alpha\otimes u)(\beta\otimes v)
 =(-1)^{b\,\deg\beta}(\alpha\wedge\beta)\otimes(u\wedge v),
 \qquad u\in\Lambda^b\pi^*E.
\tag{C.7}
\]
Thus it is commutative with the sign from the *total* degrees \(a+b\). This follows by moving the two differential forms past each other, the two exterior vectors past each other, and including the two signs in (C.7); the combined exponent is their total-degree product.

The connection induces an exterior covariant derivative \(\nabla\) of degree \((1,0)\). Locally this is the usual exterior derivative plus the action of \(A\) on each exterior-vector factor, with the signs required by (C.7). It is a derivation for total degree. This can be checked on functions, ordinary one-forms and individual exterior generators, which generate the algebra, and then extended by the product rule.

Let \(x\) be the tautological section of \(\pi^*E\): at a vector \(v\in E\), its value is \(v\) in the fibre over \(\pi(v)\). In a frame put
\[
 x=\sum_i y_i\theta_i,\qquad
 \nabla x=\sum_i\eta_i\theta_i,\qquad
 \eta=dy+Ay.
\tag{C.8}
\]
Define a contraction of total degree minus one by
\[
 a(x)(\alpha\otimes u)
 =(-1)^{\deg\alpha}\alpha\otimes\iota_xu.
\tag{C.9}
\]
Here \(\iota_x\) is contraction using the metric, so
\(\iota_x(\theta_i\theta_j)=y_i\theta_j-y_j\theta_i\).
The ordinary exterior-contraction rule and (C.7) show that (C.9) is a derivation for total degree.

Convert the curvature to an element of \(\mathscr A^{2,2}\) by
\[
 R=\sum_{i<j}F_{ji}\theta_i\theta_j
 =-\sum_{i<j}F_{ij}\theta_i\theta_j.
\tag{C.10}
\]
This is a global element: it is the alternating tensor associated, by the metric, with the skew endomorphism \(F\). The reversed indices in (C.10) are part of the convention and determine the Euler sign.

Let \(T:\mathscr A\to\Omega(E;\mathbb C)\) extract the coefficient of \(\theta_1\cdots\theta_r\). An oriented orthonormal frame change has determinant one, so \(T\) is global. Moreover,
\[
 T a(x)=0,\qquad dT(u)=T(\nabla u).
\tag{C.11}
\]
The first identity holds because contraction lowers the exterior-vector degree and no input has degree greater than \(r\). For the second, the connection preserves the oriented unit exterior volume: its derivative is multiplication by \(\operatorname{tr}A=0\). Apply the product rule to its coefficient; lower exterior degrees remain lower and do not contribute.

### C.3. Closedness with all cancellation signs

Set
\[
 S=\frac{|x|^2}{2}+i\nabla x+R,
 \qquad
 U=(2\pi)^{-m}T(e^{-S}).
\tag{C.12}
\]
The exponential is the ordinary scalar Gaussian times a finite exponential of the nilpotent positive exterior-vector degree terms. Every term of \(i\nabla x+R\) has equal differential-form and exterior-vector degrees. Extracting degree \(r\) therefore makes \(U\) an \(r\)-form.

**Lemma C.1 — The Gaussian cancellation.** We have
\[
 (\nabla-i a(x))S=0,\qquad dU=0.
\tag{C.13}
\]

**Proof.** In the frame (C.8), compatibility gives
\[
 \frac12d|x|^2=\sum_i y_i\eta_i,
 \qquad
 a(x)\nabla x=-\sum_i y_i\eta_i.
\tag{C.14}
\]
The minus sign in the second equality is the \((-1)^{\deg\eta_i}\) in (C.9). Applying the connection twice to \(x\), or expanding \(d\eta+A\wedge\eta\), gives
\[
 \nabla(\nabla x)=\sum_{i,j}F_{ij}y_j\theta_i=a(x)R.
\tag{C.15}
\]
To verify the last equality, contract each term \(F_{ji}\theta_i\theta_j\) in (C.10). The coefficient of \(\theta_i\) from \(j>i\) is \(-F_{ji}y_j=F_{ij}y_j\); the terms with \(j<i\) give the remaining entries of the same sum. Finally \(\nabla R=0\), the Bianchi identity transported by the metric identification in (C.10).

Consequently the derivative of the scalar term in \(S\) cancels \(a(x)\nabla x\), and \(i\nabla(\nabla x)\) cancels \(-i a(x)R\). This proves the first identity in (C.13). The operator \(\nabla-i a(x)\) is an odd derivation and \(S\) is even, so differentiation of its finite exponential and scalar Gaussian gives
\((\nabla-i a(x))e^{-S}=0\). Equation (C.11) now gives
\[
 dU=(2\pi)^{-m}T((\nabla-i a(x))e^{-S})=0.
\]
Although complex coefficients were convenient for this calculation, \(U\) is real: a term contributing to exterior degree \(2m\) uses \(2m-2b\) factors from \(i\nabla x\) and \(b\) factors from \(R\), and that power of \(i\) is real. All other coefficients and all product signs are real. ∎

**Lemma C.2 — Fibre normalization and zero-section value.** On every oriented fibre,
\[
 U|_{E_p}=(2\pi)^{-m}e^{-|y|^2/2}
 dy_1\wedge\cdots\wedge dy_{2m},\qquad
 \int_{E_p}U=1.
\tag{C.16}
\]
If \(j:M\to E\) is the zero section, then
\[
 j^*U=\operatorname{Pf}(F/2\pi).
\tag{C.17}
\]

**Proof.** On a fibre the base forms \(A,F\) vanish and \(\eta=dy\). The product of all the factors \(-i\,dy_i\theta_i\) contributes
\[
 (-i)^{2m}(-1)^{(2m)(2m-1)/2}=1
\]
to the ordered product of the \(dy_i\)'s and the \(\theta_i\)'s. This gives the first formula. The one-dimensional Gaussian integral is \(\sqrt{2\pi}\): square the integral, apply polar coordinates in the plane to obtain \(2\pi\int_0^\infty e^{-s^2/2}s\,ds=2\pi\), and use positivity. Products give (C.16).

On the zero section \(x=0\) and \(j^*\nabla x=0\). The remaining exponential is
\(\exp(-R)=\exp(\sum_{i<j}F_{ij}\theta_i\theta_j)\).
Definition (C.2), including the factor \((2\pi)^{-m}\), gives (C.17). ∎

**Pullback by any smooth section.** Let \(s:M\to E\) be any smooth section of the oriented metric bundle of even rank \(2m>0\), with the fixed connection used in (C.12). The form \(s^*U\) is closed and represents \(e(E)_{\mathbb R}\), with no condition on the zeros of \(s\). Here is the complete homotopy calculation. For two sections \(s_0,s_1\), put
\[
 H(t,p)=(1-t)s_0(p)+t s_1(p),\qquad
 H^*U=dt\wedge\beta_t+\gamma_t.
\]
The addition and scalar multiplication in a vector bundle make \(H\) smooth, and pullback commutes with the differential. Since \(dU=0\), the \(dt\) component of \(dH^*U=0\) gives \(\partial_t\gamma_t=d\beta_t\). Therefore
\[
 s_1^*U-s_0^*U=d\int_0^1\beta_t\,dt.
\]
This is a global primitive: the decomposition by the distinguished parameter is intrinsic, and coefficientwise integration over a compact interval preserves smoothness. Take \(s_0\) to be the zero section. LemmaC.2 gives its pullback as \(\operatorname{Pf}(F/2\pi)\), whose Euler-class identification follows below. In particular every finite real multiple of \(s\) gives the same Euler class, with this explicit primitive between any two multiples. Wu's Section2.2 presents this section dependence; the calculation supplies it directly from the closed Gaussian form. No limit at an unbounded parameter is needed for this assertion.

### C.4. Support and the topological normalization

The Gaussian is not compactly supported in a fibre. Use the orientation-preserving fibre diffeomorphism
\[
 \Phi:\{|y|<1\}\longrightarrow E,\qquad
 \Phi(y)=\frac{y}{\sqrt{1-|y|^2}},
\tag{C.18}
\]
and extend \(\Phi^*U\) by zero outside the unit ball bundle. Its inverse is \(z\mapsto z/\sqrt{1+|z|^2}\). The radial radius function \(r/\sqrt{1-r^2}\) has positive derivative, and tangential directions have positive scaling, proving the asserted orientation preservation. Denote the extension by \(U_c\). It is smooth. Indeed, on a compact base-coordinate neighbourhood every coefficient of \(U\) is a polynomial in fibre coordinates times \(e^{-|y|^2/2}\), with smooth base coefficients. After (C.18), any fixed number of derivatives is bounded by a finite sum of powers of \((1-|y|^2)^{-1/2}\), multiplied by
\[
 \exp\!\left(-\frac{|y|^2}{2(1-|y|^2)}\right).
\]
As \(|y|\to1\), each such product tends to zero: putting \(s=(1-|y|^2)^{-1}\), the exponential is a constant times \(e^{-s/2}\), which dominates every power of \(s\). Thus all derivatives extend by zero. The extension is closed, its oriented fibre integral remains one by substitution, and its zero-section pullback remains (C.17).

The de Rham comparison for pairs in PartA and this normalization identify \(U_c\) with the real Thom class. Here is the precise relative pair. Take
\(E_{>1}=\{v:|v|>1\}\). The form \(U_c\) vanishes there, so the relative de Rham cone represents it by \((U_c,0)\). Its restriction to each fibre pair \((\mathbb R^{2m},\{|y|>1\})\) evaluates to one on the positive relative ball. The inclusion \(E_{>1}\hookrightarrow E\setminus j(M)\) is a homotopy equivalence: radial scaling moves every positive radius to radius two and keeps the radii greater than one in that region throughout. The long exact sequences of pairs identify
\[
 H^{2m}(E,E\setminus j(M);\mathbb R)
 \ \cong\ H^{2m}(E,E_{>1};\mathbb R).
\tag{C.19}
\]
The uniqueness of the oriented Thom class, proved in the Thom/Euler chapter, therefore identifies the inverse image of \([U_c,0]\) with that class. Pulling its absolute image back along \(j\) proves
\[
 [\operatorname{Pf}(F/2\pi)]=e(E)_{\mathbb R}.
\tag{C.20}
\]
This is the Euler-form theorem with its exact sign and normalization. Orientation reversal changes the top coefficient \(T\) and the Euler form by a minus sign. For rank zero the class and the empty Pfaffian are both \(1\); the Gaussian and support construction are unnecessary.

In odd rank the real Euler class is zero. The bundle map \(-I\) reverses each fibre orientation and is thus an orientation-preserving isomorphism from \(E\) with its given orientation to \(E\) with the reversed orientation. Euler naturality and the orientation-reversal rule proved in the Thom/Euler chapter give \(e(E)=-e(E)\), hence \(2e(E)=0\). Its real image is zero. Defining the odd-size Pfaffian to be zero consequently gives the same real Euler statement in odd rank.

**Exercise C.3 — The oriented plane sign (medium).** For an oriented metric two-plane bundle, write
\[
 A=\begin{pmatrix}0&-a\\a&0\end{pmatrix}.
\]
Relate the Pfaffian form to the first Chern form for the complex structure \(Je_1=e_2\), and explain why the preceding Thom construction determines the sign.

**Solution.** As a complex line with complex frame \(e_1\), the derivative is
\(\nabla e_1=a e_2=i a e_1\). Its complex connection potential is \(ia\), and its curvature is \(i\,da\). The first Chern form is
\[
 \frac{i}{2\pi}(i\,da)=-\frac{da}{2\pi}.
\]
The real curvature has upper-right entry \(-da\), so (C.2) gives exactly the same Pfaffian form. The Gaussian's restriction to the oriented fibre is the positive normalized volume form (C.16); hence its relative class is the positive Thom class. Pullback along the zero section is therefore the Euler class defined earlier, rather than its negative. The equality \(c_1(E,J)=e(E)\) is consequently respected. ∎

**Exercise C.4 — Prove the Euler-form identification (hard).** For an oriented metric bundle of rank \(2m>0\), prove that \(\operatorname{Pf}(F/2\pi)\) represents its Euler class. Your proof must fix the fibre normalization and deal with the Gaussian's support.

**Solution.** In the algebra with multiplication (C.7), set
\[
 S=|x|^2/2+i\nabla x-\sum_{i<j}F_{ij}\theta_i\theta_j,
 \qquad U=(2\pi)^{-m}T(e^{-S}).
\]
Metric compatibility gives \(d|x|^2/2=-a(x)\nabla x\). Curvature gives \(\nabla(\nabla x)=a(x)R\), for \(R=-\sum_{i<j}F_{ij}\theta_i\theta_j\), and Bianchi gives \(\nabla R=0\). Hence \((\nabla-i a(x))S=0\). Since this is a derivation and \(T a(x)=0\), \(dU=0\). Its exterior-vector top coefficient is a differential form of degree \(2m\).

On a fibre, \(F\) and \(A\) vanish and \(\nabla x=\sum_i dy_i\theta_i\). The coefficient sign is
\((-i)^{2m}(-1)^{m(2m-1)}=1\). Thus
\[
 U|_{E_p}=(2\pi)^{-m}e^{-|y|^2/2}dy_1\wedge\cdots\wedge dy_{2m},
\]
whose integral is one by the product Gaussian integral. On the zero section, only \(R\) remains in the exponential, so
\[
 j^*U=(2\pi)^{-m}T\exp\!\left(\sum_{i<j}F_{ij}\theta_i\theta_j\right)
 =\operatorname{Pf}(F/2\pi).
\]

Pull \(U\) back by \(y\mapsto y/\sqrt{1-|y|^2}\) on the unit ball bundle and extend by zero. Each derivative near its boundary is a finite sum of terms bounded by a power of \((1-|y|^2)^{-1}\) times \(\exp(-|y|^2/(2(1-|y|^2)))\). These tend to zero to every order. The extension \(U_c\) is therefore smooth and closed. The fibre map is orientation preserving, so its fibre integral remains one, and its zero-section pullback is unchanged.

The relative form \((U_c,0)\) for \((E,E_{>1})\) consequently evaluates to one on each positive fibre ball. The relative de Rham comparison identifies it with the fibre-normalized real Thom class in that pair. Radial scaling makes \(E_{>1}\to E\setminus j(M)\) a homotopy equivalence, so the corresponding class in \((E,E\setminus j(M))\) is the Thom class defined earlier. Its absolute image pulled back to the zero section is, by definition, \(e(E)_{\mathbb R}\). The displayed zero-section formula proves the required Pfaffian identification, including its positive sign. ∎

## D. Identify the integral classes' real images

The notation \(c_j(E)_{\mathbb R}\), \(p_j(E)_{\mathbb R}\) and \(e(E)_{\mathbb R}\) means the coefficient image of the previously defined integral class, interpreted as a de Rham class through (A.11). The forms do not define a replacement integral theory.

**Theorem D.1 — Chern and Pontryagin identification.** For every complex smooth bundle with any connection,
\[
 [c_j(\nabla)]=c_j(E)_{\mathbb R},\qquad
 [\operatorname{ch}(\nabla)]=\operatorname{ch}(E)_{\mathbb R}.
\tag{D.1}
\]
For every real smooth bundle with any real connection,
\[
 [p_j(\nabla)]=p_j(E)_{\mathbb R}.
\tag{D.2}
\]
If the complex connection is Hermitian-compatible, the Chern forms themselves are real.

**Proof: a line.** Rank zero has determinant \(1\), trace \(0\), and no positive Chern or Pontryagin classes, so first consider positive rank. Equip a complex line with a Hermitian metric and choose a compatible connection. Regard it as an oriented real two-plane, with its complex orientation. In a unit complex frame, its potential is \(ia\) for a real one-form \(a\). In the real frame \((e,ie)\), the potential and curvature are
\[
 A_{\mathbb R}=\begin{pmatrix}0&-a\\a&0\end{pmatrix},
 \qquad F_{\mathbb R}=\begin{pmatrix}0&-da\\da&0\end{pmatrix}.
\]
Thus its first Chern form is \(i(i\,da)/(2\pi)=-da/(2\pi)\), equal to the real Pfaffian form. The normalized Thom proof (C.20) identifies this with \(e(E_{\mathbb R})_{\mathbb R}\). The integral Chern construction already proved \(c_1(E)=e(E_{\mathbb R})\), so (D.1) holds for a line. All higher Chern forms of a line vanish, just as the higher integral classes do. An arbitrary connection gives the same class by transgression to the compatible one.

**Proof: split the bundle without losing cohomology.** The Gysin/projective chapter, Theorems4.1 and5.1, constructs a complete complex flag bundle \(f:\operatorname{Flag}(E)\to M\) for which
\[
 f^*E=L_1\oplus\cdots\oplus L_r,\qquad
 f^*:H^*(M;\mathbb R)\hookrightarrow
 H^*(\operatorname{Flag}(E);\mathbb R).
\tag{D.3}
\]
Its construction is smooth for a smooth metric bundle: it iteratively projectivizes smooth bundles, and takes the orthogonal complement by the smooth projection formula. Local bundle charts have finite-dimensional projective fibres; they show that the flag space is a finite-dimensional second-countable smooth manifold. The Hausdorff and paracompactness checks were included in that chapter.

Choose connections on the lines and their direct sum on \(f^*E\). For that connection the curvature is block diagonal, hence
\[
 \sum_j c_j(\nabla)=\prod_{\ell=1}^r
 \bigl(1+c_1(\nabla^{L_\ell})\bigr).
\tag{D.4}
\]
By the line case, the product of their de Rham classes is
\(\prod_\ell(1+c_1(L_\ell)_{\mathbb R})\).
The integral Whitney formula from the Chern chapter makes this the real image of \(c(f^*E)\). Transgression compares the direct-sum connection to \(f^*\nabla\), and naturality of (A.11) and curvature compares its classes to the pullbacks of those on \(M\). Injectivity in (D.3) proves the Chern equalities on \(M\).

On a line, the curvature exponential gives \(\operatorname{ch}=e^{c_1(\nabla)}\). Its trace is additive on a direct sum, so the same flag argument identifies it with \(\sum_\ell e^{c_1(L_\ell)}\), the Chern character polynomial previously constructed from the Chern classes. Each fixed form degree uses only a finite truncation of the exponential.

For a real bundle, the complexified connection has the same real curvature matrix, now acting complex linearly. By definition of the integral Pontryagin class,
\(p_j(E)=(-1)^j c_{2j}(E_{\mathbb C})\). Apply the Chern result and (B.13) to prove (D.2).

Finally, in a unitary frame \(F^*=-F\), where the star is conjugate transpose. The even-degree matrix \(iF\) is therefore Hermitian. Transposition does not change a determinant, and conjugating \(\det(I+t iF/2\pi)\) gives that same determinant. All its coefficient forms are real. ∎

**Lemma D.2 — All complex invariant polynomials.** Every conjugation-invariant polynomial on \(\mathfrak{gl}(r,\mathbb C)\) is a polynomial in the elementary coefficient functions \(s_j\) defined by
\[
 \det(I+tX)=\sum_{j=0}^r t^j s_j(X).
\tag{D.5}
\]
Consequently, if \(P(X)=Q(s_1(X),\ldots,s_r(X))\), then
\[
 [P(F)]=Q\bigl((-2\pi i)c_1(E)_{\mathbb R},
 \ldots,(-2\pi i)^r c_r(E)_{\mathbb R}\bigr).
\tag{D.6}
\]

**Proof.** Triangularize a complex matrix by successively taking an eigenvector and passing to its quotient; this finite-dimensional linear-algebra construction gives a basis in which the matrix is upper triangular. Conjugate that matrix by
\(\operatorname{diag}(\epsilon^{r-1},\epsilon^{r-2},\ldots,1)\).
Every strictly upper entry in position \(i<j\) is multiplied by \(\epsilon^{j-i}\), and tends to zero as \(\epsilon\downarrow0\). Invariance and polynomial continuity therefore make \(P(X)\) equal to its value on the diagonal of this triangular matrix. Its diagonal restriction is symmetric under permutation matrices. The full symmetric-polynomial theorem proved in the Schubert chapter expresses that restriction as \(Q(s_1,\ldots,s_r)\). The diagonal reduction proves the identity for every matrix.

It is a polynomial identity in the matrix entries, so it remains true after substitution of the commuting two-form entries of \(F\). From (B.11),
\(s_j(F)=(-2\pi i)^j c_j(\nabla)\).
Theorem D.1 and the multiplicative de Rham comparison prove (D.6). ∎

Equations (B.8) and (D.6) are the Chern–Weil theorem in the present convention: closed invariant curvature forms are natural and connection-independent, and their cohomology classes are the specified polynomials in the already normalized characteristic classes. The metric Euler form is the additional oriented polynomial proved in PartC.

Passing to real coefficients loses every torsion class. On a compact manifold the homology groups are finitely generated, as proved in the manifold chapter; the coefficient theorem then shows that the kernel of the integral-to-real map is precisely the torsion subgroup. On an arbitrary noncompact base no such conclusion about that kernel is asserted. In particular, vanishing of curvature characteristic forms by itself gives vanishing of the real images, with no automatic assertion that an integral class vanishes.

### D.3. The tautological line on \(\mathbb{CP}^1\)

View the tautological bundle as a subbundle of the product \(\mathbb{CP}^1\times\mathbb C^2\), with the usual Hermitian metric, antilinear in its first argument. Orthogonally projecting the ordinary derivative onto this subbundle defines its induced, or Fubini–Study, connection. The projection is smooth, and the derivative rule follows because projecting \(df\,s\) leaves \(df\,s\).

On the affine chart \([1:z]\), take the unit frame
\[
 s(z)=\frac{(1,z)}{\sqrt{1+|z|^2}}.
\]
Projection gives its potential
\[
 A=s^*ds=
 \frac{\bar z\,dz-z\,d\bar z}{2(1+|z|^2)},\qquad
 F=dA=\frac{d\bar z\wedge dz}{(1+|z|^2)^2}.
\tag{D.7}
\]
For the derivative, put \(h=1+|z|^2\): the numerator's derivative is \(2d\bar z\wedge dz\), and differentiating \(h^{-1}\) supplies the term subtracting \(|z|^2/h^2\) from \(1/h\). Since the bundle is a line \(A\wedge A=0\).

Writing \(z=x+iy\), the complex orientation is \(dx\wedge dy>0\), and
\[
 c_1(\nabla)=\frac{iF}{2\pi}
 =-\frac{dx\wedge dy}{\pi(1+x^2+y^2)^2}.
\tag{D.8}
\]
This formula is smooth across the missing point because the projection construction was global. Alternatively on the other affine chart \(w=1/z\), the unit frames differ by \(|z|/z\), and (B.1) gives the matching potential and curvature.

**Exercise D.3 — Compute the tautological Chern number (medium).** Integrate (D.8) over the projective line and compare with the integral sign fixed earlier.

**Solution.** Polar coordinates on the affine chart give
\[
 \int_{\mathbb{CP}^1}c_1(\nabla)
 =-\frac1\pi\int_0^{2\pi}\!\int_0^\infty
 \frac{r}{(1+r^2)^2}\,dr\,d\theta=-1,
\tag{D.9}
\]
because the inner integral is \(1/2\). The missing point has measure zero in a smooth coordinate chart, so exhaustion of the affine chart gives the integral of the global smooth form. The projective cohomology calculation fixed \(u\) by \(\langle u,[\mathbb{CP}^1]\rangle=1\) and proved \(c_1(\gamma)=-u\). Thus the connection gives precisely that integral class's real image, with the same orientation. ∎

## E. Gauss–Bonnet and the round sphere

**Theorem E.1 — Generalized Gauss–Bonnet.** Let \(M^{2m}\) be a closed oriented Riemannian manifold and let \(F\) be the curvature matrix of its Levi-Civita connection in oriented orthonormal frames. In dimension zero use the canonical orientation of the tangent zero-planes. Then
\[
 \int_M\operatorname{Pf}(F/2\pi)=\chi(M).
\tag{E.1}
\]

**Proof.** The exact Levi-Civita existence and uniqueness proof is DG-FND, *Riemannian connections and convex neighbourhoods*, Theorem2.1. It is a compatible connection on \(TM\), so (C.20) identifies its Pfaffian form with \(e(TM)_{\mathbb R}\). The orientation-evaluation comparison (A.16) identifies its integral with \(\langle e(TM),[M]\rangle\). The manifold chapter, Corollary4.2, proved that this integer is \(\chi(M)\), by the signed diagonal formula and Poincaré duality. Those three proved equalities give (E.1). Disconnected manifolds are handled component by component. In dimension zero use the canonical orientation of the tangent zero-planes; the empty Pfaffian integrates to the number of points. ∎

### E.2. The unit two-sphere

On the unit sphere away from its poles use colatitude \(\theta\in(0,\pi)\) and longitude \(\phi\), with metric and positive area
\[
 g=d\theta^2+\sin^2\theta\,d\phi^2,\qquad
 d\mathrm{Area}=\sin\theta\,d\theta\wedge d\phi.
\tag{E.2}
\]
The orthonormal frame is \(e_1=\partial_\theta\), \(e_2=(\sin\theta)^{-1}\partial_\phi\). The Koszul formula gives
\[
 \nabla_{e_1}e_1=\nabla_{e_1}e_2=0,\qquad
 \nabla_{e_2}e_1=\cot\theta\,e_2,\qquad
 \nabla_{e_2}e_2=-\cot\theta\,e_1.
\]
For example \([e_1,e_2]=-\cot\theta\,e_2\), and inserting this bracket and the constant frame pairings into the Koszul formula gives all four derivatives. Thus, in column convention,
\[
 A=\begin{pmatrix}
 0&-\cos\theta\,d\phi\\
 \cos\theta\,d\phi&0
 \end{pmatrix},\qquad
 F_{12}=\sin\theta\,d\theta\wedge d\phi.
\tag{E.3}
\]
The product \(A\wedge A\) is zero here. The Gaussian curvature convention is
\(K=\langle R(e_1,e_2)e_2,e_1\rangle\), which by (E.3) equals one. Consequently the Euler form is \(d\mathrm{Area}/(2\pi)\).

**Exercise E.3 — Check the curvature integral (easy).** Compute the Gaussian curvature integral of the unit round sphere, and of a sphere of radius \(R>0\), and verify (E.1).

**Solution.** From (E.2),
\[
 \int_{S^2}K\,d\mathrm{Area}
 =\int_0^{2\pi}\!\int_0^\pi\sin\theta\,d\theta\,d\phi
 =4\pi.
\]
For radius \(R\), multiply the metric by \(R^2\). Its Christoffel formula is unchanged because the inverse metric contributes \(R^{-2}\) and the metric derivatives contribute \(R^2\). Hence the connection and curvature operator are unchanged, while an orthonormal frame is divided by \(R\); this gives \(K=R^{-2}\). Area is multiplied by \(R^2\), so its curvature integral is still \(4\pi\). Dividing by \(2\pi\) gives \(2=\chi(S^2)\). The polar coordinate exceptions consist of two points, which do not affect integration of the smooth area form. ∎

**Exercise E.4 — The rank-four Euler density (medium).** Write the Euler form of an oriented metric four-plane bundle, check its behavior under orientation reversal, and explain the meaning of its integral over a closed oriented four-manifold when the bundle is the tangent bundle.

**Solution.** Formula (C.3) gives
\[
 \mathcal E(\nabla)=\frac1{4\pi^2}
 \bigl(F_{12}\wedge F_{34}
 -F_{13}\wedge F_{24}
 +F_{14}\wedge F_{23}\bigr).
\]
For the reversed bundle orientation, an oriented frame reverses the old orientation and has determinant minus one relative to it. Thus (C.4) changes the Pfaffian's sign, exactly as reversing the bundle orientation changes its Euler class. For the oriented tangent bundle with its Levi-Civita connection, (E.1) gives integral \(\chi(M)\). Reversing the manifold orientation reverses both the tangent-bundle Euler form and the integration orientation; the two signs cancel, leaving the same Euler characteristic. ∎

## Sources and exact proof scope

Johan Dupont, [Fibre Bundles and Chern–Weil Theory](https://data.math.au.dk/publications/ln/2003/imf-ln-2003-69.pdf), Chapters9–10, develops polarization, invariant curvature forms, connection independence and the Pontryagin, Euler and Chern polynomials. Theorem9.5 uses a homotopy connection on a product; PartB gives the explicit transgression primitive and its full graded contraction calculation. Example10.6 computes the tautological line's negative Chern number; SectionD.3 obtains that sign directly from its projection connection. All formulas here use column frames, ordinary oriented-coordinate integration and the normalization \(c(\nabla)=\det(I+iF/2\pi)\).

Siye Wu, [Mathai–Quillen Formalism](https://arxiv.org/pdf/hep-th/0505003), Section2, describes Berezin extraction and the Gaussian representatives of the Euler and Thom classes. The construction is due to Varghese Mathai and Daniel Quillen. Wu's presentation also credits the formulation of Nicole Berline, Ezra Getzler, Michèle Vergne and Weiping Zhang. PartC gives the graded cancellation, positive fibre integral, radial support correction and relative Thom identification in the conventions stated here. The Euler form and the integral classes' real images are then identified using the complete Thom and splitting proofs.

Liviu I. Nicolaescu, [Lectures on the Geometry of Manifolds](https://academicweb.nd.edu/~lnicolae/Lectures.pdf), Sections8.1–8.2, develops principal connections, invariant polynomials and characteristic forms. Theorem8.1.13 gives the explicit affine-path transgression primitive used in PartB. The all-degree contraction calculation proves its graded differentiation rule here. Nicolaescu's Chern normalization agrees with the column convention above; his Pfaffian convention translates to the Euler sign fixed by the positive fibre integral. His integral Chern comparison is attributed to Kunihiko Kodaira and Donald Spencer, and his topological Euler identification is deferred. PartsC–D supply the complete Thom and splitting identifications used in this lesson.

The exact DG-FND prerequisites are [Connections and parallel transport](../DG-FND/connections-and-parallel-transport.html), Sections1–3, for connection forms, gauge changes, differences and existence; [Curvature and holonomy groups](../DG-FND/curvature-and-holonomy-groups.html), Sections1–3, for covariant exterior derivatives and Bianchi; and [Linear and affine connections](../DG-FND/linear-and-affine-connections.html), Sections1–2, for the frame correspondence, tensor derivatives and compatible metric connections. The cited current versions supply these complete used proofs; their conditions agree with the column convention and base hypotheses here.

For the good cover in PartA, [Riemannian connections and convex neighbourhoods](../DG-FND/riemannian-connections-and-convex-neighbourhoods.html), Sections1–4, supplies the full distance, Koszul, Gauss-lemma, whole-manifold minimization and strong-convexity proofs. Its needed predecessors are [Geodesics, normal coordinates and curvature](../DG-FND/geodesics-normal-coordinates-and-curvature.html), Sections1–2, and [Local tools for bundles and transport](../DG-FND/local-tools-for-bundles-and-transport.html), Sections1–3. The cited current versions give smooth parameter dependence, continuation and the complete affine-convexity velocity bound needed for these steps. Later transport, holonomy and completeness results are not premises of this chapter.

Smooth-triangulation, relative compatibility and integral PL-refinement proofs are supplied in [the triangulation companion](smooth-triangulations-and-the-integral-pl-obstruction.md). The full Stiefel–Whitney-number detection theorem is proved in [the unoriented detection companion](stiefel-whitney-numbers-and-unoriented-bordism.md). The chapter was self-checked by its writing AI; no independent mathematical review is claimed.
