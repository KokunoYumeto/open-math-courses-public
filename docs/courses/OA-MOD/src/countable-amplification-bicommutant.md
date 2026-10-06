# Countable amplification and the ultraweak bicommutant closure

**OA-MOD-BA-01. Exact programme bicommutant import and local weight-representation application.**

This programme proof import supplies the precise implication used after ultraweak image closure in OA-MOD-WH-02: an ultraweakly closed unital *-subalgebra of bounded operators is a concrete von Neumann algebra. It does not assume a uniform operator bound on a strongly convergent approximating net.

## Statement and conventions

Let \(K\) be an arbitrary complex Hilbert space, with inner products linear in the first variable. Let \(A\subseteq B(K)\) be a complex unital *-subalgebra, without any initial closure assumption. Then

\[
 \overline A^{\,\mathrm{ultraweak}}=A''.
 \tag{BA.1}
\]

In particular, if \(A\) is ultraweakly closed, then \(A=A''\), so \(A\) is WOT closed and SOT closed. More precisely, each \(T\in A''\) lies in the sigma-strong closure of \(A\): for every finite family of square-summable vector sequences \((u_{k,n})_n\) and positive tolerances \(\varepsilon_k\), an \(a\in A\) can be chosen with

\[
 \left(\sum_n\|(T-a)u_{k,n}\|^2\right)^{1/2}<\varepsilon_k
 \quad\text{for every }k.
 \tag{BA.2}
\]

The exact programme proof of (BA.1) directly tests the ultraweak functionals; it does not require an additional convex-closure theorem.

A unital algebra on the zero Hilbert space is included; all statements there are immediate. For a possibly degenerate represented algebra with identity projection \(p\), the theorem is applied on \(pK\).

## Exact programme proof and countable amplification

Read **Lemma 4.1 and Theorem 4.2** of [Spatial tensor products: complete proof supplement through the commutation theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-FOUND-REMAINDER/reader/supplements/spatial-tensor-products.html#4-the-bicommutant-theorem-and-the-normal-extension-principle), original text by Claude Opus 5.5 (Anthropic), September 2026, under CC0; current selection and prerequisite bindings by GPT-6.1 Sol (OpenAI), Ultra, October 2026. These complete amplified-density and bicommutant proofs belong to the existing programme supplement. The argument uses the actual square-summable vector family on the Hilbert tensor product; it assumes neither a separable ambient Hilbert space nor a bounded approximating net. Sections 1–2 supply the Hilbert tensor and operator-matrix facts; CP-03, CP-04 and CP-06 give the concrete vector-series representation used in the local ultraweak-test application.

Lemma 4.1 states that for \(T\in A''\), every square-summable family \((u_n)\) and every \(\delta>0\), there is \(a\in A\) with \(\sum_n\|(T-a)u_n\|^2<\delta^2\). Theorem 4.2 then gives the strong, weak and ultraweak closures as \(A''\), in particular (BA.1).

**Solved finite-family application.** Concatenate the finitely many square-summable families \((u_{k,n})_n\) into

\[
 \Xi=(u_{k,n})_{k,n}\in\ell^2(K).
 \tag{BA.3}
\]

Let \(D(x)\) act coordinatewise by \(x\) on this direct sum. Applying the programme lemma to this single family, with \(0<\delta<\min_k\varepsilon_k\), gives

\[
 \|D(T-a)\Xi\|<\delta.
 \tag{BA.4}
\]

Each separate family norm is at most this concatenated norm, proving the simultaneous inequalities (BA.2). If the family of tests is empty there is nothing to prove. No operator-norm bound on \(a\) is asserted. This is a specialization of the existing density theorem, not a second proof of it.

## Solved balanced ultraweak-test application

Let \(f_1,\ldots,f_m\) be a finite family of ultraweakly continuous complex linear functionals on \(B(K)\), with positive tolerances \(\varepsilon_1,\ldots,\varepsilon_m\). By CP-03, CP-04 and CP-06, each functional has a vector-series representation

\[
 f_k(x)=\sum_{n=1}^\infty\langle x u_{k,n},v_{k,n}\rangle,
 \qquad
 \sum_n\|u_{k,n}\|\,\|v_{k,n}\|<\infty.
 \tag{BA.5}
\]

Terms with a zero vector may be omitted. Rescale the two vectors in each remaining term by reciprocal positive factors, leaving the coefficient unchanged, so that both vector norms equal
\(\sqrt{\|u_{k,n}\|\,\|v_{k,n}\|}\).
After this balancing, both \((u_{k,n})_n\) and \((v_{k,n})_n\) are square summable.

Use coordinates \((k,n)\) in a single Hilbert direct sum and put

\[
 \Xi_{k,n}=u_{k,n}.
\]

The finite number of functionals makes \(\Xi\) square summable. Let \(\Eta^{(k)}\) have entries \(v_{k,n}\) in the \(k\)-th row and zero in the other rows. Then (BA.5) is exactly

\[
 f_k(x)=\langle D(x)\Xi,\Eta^{(k)}\rangle.
\]

Choose

\[
 0<\delta<\min_{1\leq k\leq m}
       \frac{\varepsilon_k}{1+\|\Eta^{(k)}\|}.
\]

Apply the programme Lemma 4.1, as specialized in (BA.4), to find one \(a\in A\) with \(\|D(T-a)\Xi\|<\delta\). Cauchy–Schwarz gives, simultaneously for every \(k\),

\[
 |f_k(T-a)|
 \leq\|D(T-a)\Xi\|\,\|\Eta^{(k)}\|
 <\varepsilon_k.
\]

If the family of tests is empty there is nothing to check. Thus every ultraweak neighborhood of \(T\) meets \(A\), proving
\(A''\subseteq\overline A^{\,\mathrm{ultraweak}}\).

Conversely, \(A''\) is WOT closed: its commutation equations are closed under matrix-coefficient convergence, because fixed left and right multiplication are WOT continuous. It is therefore ultraweakly closed, since every vector coefficient is ultraweakly continuous. Since \(A\subseteq A''\), we have
\(\overline A^{\,\mathrm{ultraweak}}\subseteq A''\).
This verifies the ultraweak-test specialization of the imported Theorem 4.2. That theorem owns (BA.1) and its strong/weak closure conclusions. \(\square\)

## Application to multiplication representations

The representation-image proof in WH-02 establishes isometry and ultraweak closure of the faithful normal representation image. Its identity is \(p=\pi(1)\). Compression and zero extension identify its inherited ultraweak topology with that on \(B(pH)\): the coefficient of the zero extension at \(\xi,\eta\in H\) equals the corner coefficient at \(p\xi,p\eta\), and the same observation applies to the square-summable vector series. Thus the image is an ultraweakly closed unital *-subalgebra of \(B(pH)\).

Apply (BA.1) on \(pH\). This proves precisely the WOT/bicommutant-closed concrete von Neumann algebra assertion in WH-02. Its following argument can then apply NP-04 and NP-06 to both directions of the positive *-isomorphism, giving the stated ultraweak and sigma-strong-star homeomorphism. For the unital GNS representation, \(p=I\).

It does not establish any natural cone, relative Tomita operator, modular automorphism theorem or Connes derivative.

## Validation and status

The bicommutant theorem (BA.1) is proved in Lemma 4.1 and Theorem 4.2 of the spatial tensor products supplement cited above; this lesson contributes the solved finite-family and balanced-functional applications and its support-corner/topology argument for WH-02. The OA-FLOW binding keeps that exact consumer consequence.