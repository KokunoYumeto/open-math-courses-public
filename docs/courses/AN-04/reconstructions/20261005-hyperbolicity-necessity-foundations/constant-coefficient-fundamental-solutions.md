# A fundamental solution without ellipticity

Let \(P(D)\) be any nonzero constant-coefficient differential operator on \(\mathbb R^n\), with \(D=-i\partial\). We construct a distribution \(E\) satisfying \(P(D)E=\delta_0\), and then the fixed smooth local inverse needed by the hyperbolicity transport recursion. Neither ellipticity nor a continuous choice as \(P\) varies is assumed.

Independent programme exposition and proof: GPT-6 Astra (OpenAI), Ultra, 5 October 2026; CC0. The mathematical source is Hörmander I, approved 2003 eBook, ISBN 978-3-642-61497-2, Theorems 7.3.10–7.3.12. Hörmander II, approved 2005 eBook, ISBN 978-3-540-26964-9, Theorem 10.2.1 gives a stronger regularity treatment. We need only the fundamental solution and smooth convolution bounds proved here. Exact earlier polynomial, Fourier, measure and finite-calculus proofs are identified in the proof map.

The [exact map](proof-map.json) connects the complete [polynomial proof](../20261005-restored-quadratic-forms/spectral-algebra-and-contour-projections.md), [exponential series and circle calculus](../20261004-free-stationary-phase/exponential-prerequisite-completions.md), [Fourier inversion](../20261004-free-stationary-phase/quadratic-stationary-phase.md) and [measure and distribution foundations](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md). The [convex-support companion and exact figure](convex-support-and-finite-jets.md) supply the other U032 prerequisite and illustrate the rotating set used here.

## F1. Avoiding polynomial zeros on a rotating compact set

Let \(\mathcal P_m\) be the finite-dimensional complex vector space of polynomials in \(n\) variables of degree at most \(m\), equipped with
\[
 \|Q\|_{\mathcal P_m}^2=\sum_{|\alpha|\le m}|\partial^\alpha Q(0)|^2.
 \tag{FS1}
\]
This is a norm because the finite Taylor formula gives every coefficient. On a fixed compact set of \(\zeta\)'s, evaluation is a bounded linear functional of these coefficients, uniformly in \(\zeta\).

For each nonzero \(Q\), there is a point \(a\in\mathbb C^n\) such that the polynomial \(q(z)=Q(za)\) is not identically zero. Here is a direct algebraic verification. A nonzero polynomial in one variable has at most its degree many zeros by successive division. In several variables, regard it as a polynomial in the last variable; by induction choose the earlier variables so one of its nonzero coefficient polynomials is nonzero. The resulting one-variable polynomial is nonzero, and a value outside its finite zero set gives \(a\) with \(Q(a)\ne0\). Hence \(q(1)\ne0\).

The polynomial \(q\) has finitely many nonzero roots. Choose a radius \(r>0\), small enough that \(|ra|<1/4\), distinct from their absolute values. If \(a=0\), any sufficiently small radius is suitable and the orbit below is the single point zero. The compact orbit
\[
 \{e^{i\theta}ra:0\le\theta\le2\pi\}
 \tag{FS2}
\]
contains no zero of \(Q\). Its minimum \(|Q|\) is positive. A sufficiently small neighborhood of this orbit is still contained in \(\{|\zeta|<1/2\}\) and has a positive lower bound for \(|Q|\). Take a nonnegative smooth bump \(\psi\) of integral one supported in a small ball about \(ra\), whose entire rotation orbit is in that neighborhood, and define, for Lebesgue measure \(dA\) on \(\mathbb C^n=\mathbb R^{2n}\),
\[
 \phi_Q(\zeta)=\frac1{2\pi}\int_0^{2\pi}\psi(e^{i\theta}\zeta)\,d\theta.
 \tag{FS3}
\]
It is smooth, nonnegative, rotation invariant, compactly supported in the ball of radius \(1/2\), and has integral one. Differentiation under the compact integral proves smoothness; a shift of the periodic angular variable proves invariance; the real rotation has Jacobian one, so the affine substitution theorem and Fubini prove the integral assertion. Its support consists only of rotations of points in \(\operatorname{supp}\psi\), where \(|Q|\) has the positive lower bound.

## F2. One smoothly varying averaging kernel

Normalize polynomials by FS1. For each point \(Q_j\) of the unit sphere the preceding bump works for every polynomial in a sufficiently small neighborhood \(U_j\) of \(Q_j\), with a uniform lower bound \(c_j>0\) on its support. Indeed, evaluation is uniformly continuous in the coefficients on that compact support. Compactness of the coefficient sphere gives finitely many such neighborhoods.

We spell out the finite partition used here. Shrink finitely many coefficient balls so they still cover the sphere and their closed larger balls lie in the respective \(U_j\). Smooth coefficient bumps equal to one on the smaller balls and zero outside the larger balls have a positive sum on the sphere. Divide each by that sum. Their restrictions \(\lambda_j\) form a smooth nonnegative partition with supports contained in \(U_j\). Set
\[
 \Phi(Q,\zeta)=\sum_j\lambda_j(Q/\|Q\|_{\mathcal P_m})\phi_{Q_j}(\zeta),
 \qquad Q\ne0.
 \tag{FS4}
\]
It is smooth jointly in \(Q\ne0,\zeta\), nonnegative, rotation invariant in \(\zeta\), of integral one, and all its \(\zeta\)-supports lie in a fixed compact set \(Z\subset\{|\zeta|<1/2\}\). Finiteness gives constants \(c,C>0\) with
\[
 0\le\Phi\le C,\qquad
 |Q(\zeta)|\ge c\|Q\|_{\mathcal P_m}
       \quad\hbox{on }\operatorname{supp}_{\zeta}\Phi(Q,\cdot).
 \tag{FS5}
\]
At a support point at least one relevant bump has that lower bound; taking the minimum of the finitely many constants proves FS5, including limits at support boundaries. The quotient \(\Phi(Q,\zeta)/Q(\zeta)\), defined as zero near zeros of \(Q\), is smooth. Locally in \(Q\ne0\), FS5 separates the support by a positive margin from those zeros, which justifies this extension.

## F3. The needed averaging identity, proved from exponentials

For a compactly supported smooth test \(\varphi\), define for complex \(w\)
\[
 \widehat\varphi(w)=\int_{\mathbb R^n}e^{-ix\cdot w}\varphi(x)\,dx.
 \tag{FS6}
\]
The integral is over a compact real set. For fixed real \(\xi\) and complex \(\zeta\), uniform convergence of the exponential series on that set shows
\[
 \frac1{2\pi}\int_0^{2\pi}
     \widehat\varphi(-\xi-e^{i\theta}\zeta)\,d\theta
 =\widehat\varphi(-\xi).
 \tag{FS7}
\]
In detail, expand \(\exp(i e^{i\theta}x\cdot\zeta)\). Its degree \(j\) term contains \(e^{ij\theta}\), whose angular average is zero for \(j\ge1\) by direct integration, and is one for \(j=0\). Uniform convergence permits integration term by term. The factor \(e^{ix\cdot\xi}\varphi(x)\) is integrable, and uniform convergence on the compact support permits the remaining exchange. The elementary exponential and circle integrals are proved in U001.

If \(\Phi(Q,\zeta)\) is our rotation-invariant kernel, average the change of variables \(\zeta\mapsto e^{i\theta}\zeta\) in its integral against FS6. Fubini is legitimate on these compact sets, and FS7 gives
\[
 \int_{\mathbb C^n}\Phi(Q,\zeta)
       \widehat\varphi(-\xi-\zeta)\,dA(\zeta)
 =\widehat\varphi(-\xi).
 \tag{FS8}
\]
Thus the precise mean-value assertion used below has its full proof. No general theorem about holomorphic extension or division is being substituted for it.

## F4. Construction of the distribution and verification of its equation

For a fixed nonzero polynomial \(P\) of degree at most \(m\), put \(P_\xi(\zeta)=P(\xi+\zeta)\). If \(d\) is its actual degree and \(\partial^\alpha P\) is a nonzero derivative of degree \(d\), that derivative is a fixed nonzero constant. Its term in FS1 gives
\[
 \|P_\xi\|_{\mathcal P_m}\ge c_P>0\quad\hbox{for every real }\xi.
 \tag{FS9}
\]
The statement also holds for a nonzero constant \(P\). Define the bilinear distribution candidate
\[
 E(\varphi)=(2\pi)^{-n}\int_{\mathbb R^n}\int_{\mathbb C^n}
 \frac{\Phi(P_\xi,\zeta)}{P(\xi+\zeta)}
       \widehat\varphi(-\xi-\zeta)\,dA(\zeta)\,d\xi.
 \tag{FS10}
\]
We first justify it. If \(\operatorname{supp}\varphi\subset A\), with \(A\) compact, write FS6 at \(-\xi-\zeta\) as the ordinary Fourier integral with real phase \(x\cdot\xi\) and amplitude \(e^{ix\cdot\zeta}\varphi(x)\). Repeated integration by parts with \(1-\Delta_x\), whose action on \(e^{ix\cdot\xi}\) is multiplication by \(1+|\xi|^2\), gives
\[
 |\widehat\varphi(-\xi-\zeta)|
 \le C_{A,N,Z}(1+|\xi|^2)^{-N}
       \max_{|\alpha|\le2N}\sup_A|\partial^\alpha\varphi|,
 \qquad \zeta\in Z.
 \tag{FS11}
\]
The exponential and all the finitely many derivatives are bounded uniformly on \(A\times Z\). The support has finite volume, so the integral remainder is bounded as written. Choose \(2N>n\); the \(\xi\) weight is integrable, as follows by summing dyadic annuli of volume at most \(C2^{jn}\). FS5 and FS9 uniformly bound the quotient in FS10. The \(\zeta\)-support has finite volume. Thus FS10 is absolutely convergent, linear and bounded by a finite smooth-test seminorm on each compact \(A\). It defines a distribution of finite order on every such compact.

The transpose of \(P(D)\) in the bilinear convention is \(P(-D)\), without coefficient conjugation. Integration by parts in the compact test integral proves, also for complex frequencies,
\[
 \widehat{P(-D)\varphi}(-\xi-\zeta)
   =P(\xi+\zeta)\widehat\varphi(-\xi-\zeta).
 \tag{FS12}
\]
Using the absolutely convergent defining formula with this test, cancel the denominator. The resulting integral is still absolutely convergent by FS11 and boundedness of \(\Phi\). Equations FS8 and the earlier full Fourier inversion theorem now give
\[
 (P(D)E)(\varphi)=E(P(-D)\varphi)
  =(2\pi)^{-n}\int_{\mathbb R^n}\widehat\varphi(-\xi)\,d\xi
  =\varphi(0).
 \tag{FS13}
\]
Hence \(P(D)E=\delta_0\). This proves existence for every nonzero constant-coefficient operator. It asserts neither temperedness of this construction nor causal support. If there are zero variables, a nonzero constant operator is inverted simply by multiplication by its reciprocal.

## F5. A fixed local right inverse, with every parameter derivative

Let \(V\Subset U\) be relatively compact patches, and choose a fixed compact smooth \(\chi\) supported in \(U\), equal to one on a neighborhood of \(\overline V\). For \(g\in C^\infty(U)\), extend \(\chi g\) by zero and set
\[
 Tg(x)=E_y\bigl((\chi g)(x-y)\bigr).
 \tag{FS14}
\]
For \(x\) in any compact output set \(A\), the test in \(y\) is supported in the fixed compact difference set \(A-\operatorname{supp}\chi\). On a slightly enlarged such set, \(E\) has some order \(k\). Difference quotients of the smooth compact input, with all derivatives through \(k\), converge uniformly by the integral Taylor formula. Passing them through the finite-order distribution bound proves differentiation under the pairing. Repeating it for output derivatives and passive parameters gives joint smoothness and
\[
 \sup_{A\times L}|\partial_x^\alpha\partial_\lambda^\beta Tg|
 \le C\sum_{|\gamma|\le k}
 \sup_{\operatorname{supp}\chi\times L}
 |\partial_x^{\alpha+\gamma}\partial_\lambda^\beta(\chi g)|.
 \tag{FS15}
\]
Here \(L\) is any fixed compact parameter set in its open parameter domain. The same Taylor argument on a slightly larger parameter compact proves continuity of these derivatives. The finite product rule replaces the right side by finitely many seminorms of \(g\), with constants fixed by \(\chi,A,L\).

Constant-coefficient differentiation of FS14, and the definition of distributional derivatives, give \(P(D)Tg=\chi g\), hence \(P(D)Tg=g\) on \(V\). The output is smooth on all of \(\mathbb R^n\), so a finite transport recursion can always form its next right side on the original larger patch \(U\), apply the same cutoff and inverse, and retain the equation on the same \(V\). There is no accumulated loss of domain. For a smooth nonvanishing coefficient \(a\), applying this inverse to \(g/a\) solves \(aP(D)w=g\); no commutation with \(a\) is needed.

These statements supply the general local inverse in U032, including its nonelliptic cone operator. The separate planar inverse for \(D_t-iD_s=-2\partial_{\bar z}\), with its precise sign, remains the previously proved function-normal-form provider.
