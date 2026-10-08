# Every closed oriented seven-manifold bounds

<a id="DG-CHAR-13F.proof"></a>

**Theorem.** For every closed smooth oriented seven-manifold \(M\), there exists a compact smooth oriented eight-manifold \(W\) and an orientation-preserving diffeomorphism \(\partial W\cong M\). Equivalently,
\[
 \Omega_7^{SO}=0.
\]

No simple-connectivity, homology-sphere, spin, or particular tangent-bundle assumption is imposed. Disconnected closed manifolds are included.

## Exact proof chain

1. [*Stiefel–Whitney numbers and unoriented bordism*, Theorem N.3 and Corollary N.4](stiefel-whitney-numbers-and-unoriented-bordism.md#DG-CHAR-13E.corollary-N.4), give
   \[
     G=\Omega_7^{SO}\quad\text{finite of odd order}.
   \]
   These are the geometric twofold-cover and forgetful-kernel arguments, combined with rational finite generation and rank zero. They do not themselves exclude odd-primary torsion.

2. For every odd prime \(p\), the [one-group and spectrum comparison](odd-primary-one-group-cohomology.md), Sections 1–9, together with the [coordinate calculation](odd-primary-operation-coordinates.md), Sections 1–5, identifies the **full** algebra \(A=[H\mathbb F_p,\Sigma^*H\mathbb F_p]\), with its coproduct and complex-line action. It proves input **O** of the Thom-module argument. The computation is in all degrees, and its spectrum-map comparison explicitly kills the possible inverse-limit correction.

3. [The odd-primary Thom module](odd-primary-thom-module.md), Sections 2–5, applies using that full operation-algebra computation. It gives
   \[
    H^*(MSO;\mathbb F_p)
      \cong\bigoplus_\lambda
       \Sigma^{m_\lambda}(A\otimes_E\mathbb F_p),\qquad
    E=\Lambda(Q_0,Q_1,\ldots),
   \]
   where \(A\) is free as a right \(E\)-module,
   \[
       |Q_i|=2p^i-1,\qquad 4\mid m_\lambda.
   \]
   The module statement includes the actual action, not only the same dimension series. Its proof uses the previously supplied full odd-prime universal \(BSO\) computation, the typed Whitney-sum Thom maps, and the independent distinct-root-monomial injection.

4. The [exterior resolution](odd-primary-exterior-resolution.md), equations (1)–(9), implies
   \[
     \operatorname{Ext}^{s,t}_A(H^*(MSO;\mathbb F_p),\mathbb F_p)=0
       \quad\text{unless }4\mid(t-s).
   \]
   Its possible generator bidegrees obey
   \[
    t-s=m_\lambda+\sum_{i\geq0}2\alpha_i(p^i-1).
   \]
   Since \(p\) is odd, every summand is divisible by four, including the \(i=0\) term, which is zero. In particular the entire stem \(t-s=7\) is zero.

5. \(MSO\) is connective and of finite mod-\(p\) type by the Thom calculation. [Finite Adams-tower detection](finite-adams-tower-detection.md), Sections 1–3, therefore applies with \(n=7,r=1\). It gives
   \[
       G=pG\qquad\text{for every odd prime }p.
   \]
   Sixteen tower stages suffice for each such assertion. This step does not replace a convergence theorem by an unexplained spectral-sequence abutment: the finite target has sixteen \(H\mathbb F_p\)-extension layers, and the written lifting argument gives the required divisibility.

## Elimination of every primary part

If the finite odd-order group \(G\) were nonzero, choose a nonzero element of order \(d>1\). Some odd prime \(p\) divides \(d\), and its \((d/p)\)-multiple has order \(p\). Thus multiplication by \(p\) has nonzero kernel. An endomorphism of a finite group with nonzero kernel is not onto, contradicting \(G=pG\). Therefore \(G=0\).

The full oriented Pontryagin–Thom correspondence in [*Thom spaces, transversality and the Pontryagin–Thom construction*, Theorem K.1](thom-spaces-and-the-pontryagin-thom-construction.md#DG-CHAR-13.theorem-K.1), identifies the group just calculated with geometric oriented bordism. Its construction supplies smooth collars and orientations. The zero class consequently means a compact smooth oriented filling with the asserted boundary identification, not merely a rational filling, an unoriented filling, or a filling of a multiple of \(M\). This proves the theorem.

The argument also shows why the earlier finite-odd-order result was insufficient by itself: a nonzero finite group of odd order is divisible by two. The odd-prime argument is the step which excludes those remaining groups.
