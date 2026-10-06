# Tangent zooms and quadratic models

To inspect a singularity at a particular covector, remove a matching oscillation and magnify a shrinking neighborhood of its base point. For a Lagrangian distribution, the resulting model is quadratic. Its Hessians describe two tangent Lagrangian planes, and its coefficient is the leading amplitude at the selected frequency. Ordinary symbols need not have a limiting leading coefficient, so the general result is an asymptotic comparison rather than an assertion that every zoom converges.

The exact earlier programme proofs are:

- The restored [intrinsic-regularity lesson](../20261005-restored-intrinsic-regularity/intrinsic-lagrangian-regularity.md), especially its frequency-graph criterion, and the restored [oscillatory-distribution lesson](../20261005-restored-oscillatory/oscillatory-distributions-and-order.md), including its exact localization and Fourier reduction.
- Quadratic stationary phase, Q1–Q6: the compact-plus-tail limit rule, Gaussian factors, Schwartz estimates, Fourier inversion, symmetric diagonalization and the regularized quadratic identity. [The full stationary-phase proof](../20261004-free-stationary-phase/stationary-phase-and-critical-manifolds.md) supplies the nonstationary integration-by-parts bound with its transposed vector field.
- [Wavefront tests and pullbacks, T0–W5](../20261004-free-intrinsic-graph/prerequisites/coordinate-and-wavefront-localization.md), together with the earlier tangent companion's compact-distribution Fourier estimate T3 and rapid regular zoom T4.
- [Uniform local distribution bounds and moving tests, U1](../20261004-free-tangent-zoom/prerequisites/uniform-distribution-bounds.md). Its [complete-test-space component](../20261004-free-tangent-zoom/prerequisites/complete-test-spaces.md), Sections 6, 14.1–14.2 and 19, proves the Baire and completeness inputs at the declared logical base. That separate component retains its [GFDL 1.2 licence and notices](../20261004-free-tangent-zoom/prerequisites/notices/COPYING).

The [exact proof map](proof-map.json) records every dependency. The primary sources for this restoration are the approved purchased reprints of Hörmander IV, Section 25.1 and Hörmander III, Section 21.6. They supply the mathematical results; this lesson supplies its own exposition, exercises and full programme proofs. The earlier tangent companion remains available, including its uniform \(O_{\mathcal D'}(t^{-1})\) estimate, Gaussian-symbol identification and reproducible figures.

We keep \(D=-i\partial\), the Fourier phase \(-x\cdot\xi\), and the inverse coefficient \((2\pi)^{-n}\). Half densities are written in the local frame \(|dx|^{1/2}\).

## 1. Two scales select one tangent problem

Suppose the Lagrangian has the frequency graph

\[
\Lambda=\{(H'(\xi),\xi)\},
\]

where \(H\) is real, smooth and homogeneous of degree one away from zero. Extend it smoothly through low frequencies when writing a Fourier integral. For a compactly supported \(u\in I^m(\mathbb R^n,\Lambda)\), define the normalized symbol

\[
b(\xi)=(2\pi)^{-n/4}e^{iH(\xi)}\widehat u(\xi),
\qquad b\in S^r,\quad r=m-n/4.
\tag{1.1}
\]

Thus, up to a smooth low-frequency term,

\[
u(x)=(2\pi)^{-3n/4}
\int e^{i(x\cdot\xi-H(\xi))}b(\xi)\,d\xi.
\tag{1.2}
\]

The normalization in (1.1) differs by a constant from the reduced symbol in the preceding lesson. It is chosen so that the coefficient of the quadratic model will later be a half density on \(\Lambda\).

Fix \(\gamma_0=(x_0,\xi_0)\in\Lambda\), \(\xi_0\ne0\). Choose a real smooth function \(\psi\) near \(x_0\) with

\[
\psi(x_0)=0,\qquad \psi'(x_0)=\xi_0.
\tag{1.3}
\]

For \(t\to+\infty\), examine

\[
W_t(x)=t^{-2m-n/2}
\big(u e^{-it^2\psi}\big)(x_0+x/t).
\tag{1.4}
\]

This defines a distribution on every fixed compact set of the new \(x\) variables for sufficiently large \(t\). The factor \(t^{-n/2}\) is the half-density Jacobian of the map \(x\mapsto x_0+x/t\); the remaining \(t^{-2m}\) measures order at frequency \(t^2\xi_0\). The spatial scale is \(t^{-1}\), and the frequency deviations from that center have scale \(t\).

Put

\[
A=H''(\xi_0),\qquad B=\psi''(x_0),
\qquad
Q_{A,B}(x,\eta)=x\cdot\eta-\tfrac12 x^TBx-\tfrac12\eta^TA\eta.
\tag{1.5}
\]

Define the tempered quadratic distribution

\[
U_{A,B}(x)=(2\pi)^{-3n/4}
\int e^{iQ_{A,B}(x,\eta)}\,d\eta.
\tag{1.6}
\]

This is \((2\pi)^{n/4}\) times the inverse Fourier transform of \(e^{-i\eta^TA\eta/2}\), multiplied by \(e^{-ix^TBx/2}\). Both operations are defined on tempered distributions: derivatives of each quadratic exponential are polynomially bounded, so multiplication preserves Schwartz space and extends by transposition.

## 2. The asymptotic comparison and its tail estimate

**Theorem 2.1 (tangent zoom).** With the preceding hypotheses,

\[
W_t-t^{-2r}b(t^2\xi_0)U_{A,B}\longrightarrow0
\quad\text{in }\mathcal D'(\mathbb R^n).
\tag{2.1}
\]

The scalar coefficient is bounded, but need not converge. The result holds for finite-dimensional vector-valued amplitudes componentwise. A smooth localized error in \(u\) contributes a term tending to zero faster than every inverse power of \(t\).

**Proof.** Fix a compactly supported smooth test function \(f\). In (1.2), substitute \(\xi=t^2\xi_0+t\eta\). The measure contributes \(t^n\), so (1.4) paired with \(f\) is

\[
(2\pi)^{-3n/4}\int b_t(\eta)F_t(\eta)\,d\eta,
\qquad b_t(\eta)=t^{-2r}b(t^2\xi_0+t\eta),
\tag{2.2}
\]

where

\[
\begin{aligned}
F_t(\eta)&=\int e^{iE_t(x,\eta)}f(x)\,dx,\\
E_t(x,\eta)&=(x_0+x/t)\cdot(t^2\xi_0+t\eta)
-t^2\psi(x_0+x/t)-H(t^2\xi_0+t\eta).
\end{aligned}
\tag{2.3}
\]

These identities can first be taken with frequency cutoffs. The estimates below make their test pairings absolutely convergent and justify removing those cutoffs.

Euler's identity and the graph condition give \(H(\xi_0)=x_0\cdot\xi_0\) and \(H'(\xi_0)=x_0\). For bounded \(\eta\), homogeneity and Taylor expansion give

\[
H(t^2\xi_0+t\eta)
=t^2H(\xi_0)+t x_0\cdot\eta
+\tfrac12\eta^TA\eta+O(t^{-1}).
\]

The analogous expansion of \(t^2\psi(x_0+x/t)\) has linear term \(t\xi_0\cdot x\) and quadratic term \(x^TBx/2\). All constant and linear terms cancel in (2.3), leaving

\[
E_t(x,\eta)\longrightarrow Q_{A,B}(x,\eta)
\]

uniformly on compact sets, with the needed fixed \(x\) derivatives. Consequently \(F_t\to F\) on compact \(\eta\) sets, where \(F(\eta)=\int e^{iQ_{A,B}}f\,dx\).

The tails are uniformly controlled. On the fixed support of \(f\),

\[
\partial_x E_t=t\xi_0+\eta-t\psi'(x_0+x/t)=\eta+O(1).
\tag{2.4}
\]

Every \(x\) derivative of order at least two is bounded uniformly: at order \(k\) its phase contribution is \(-t^{2-k}\psi^{(k)}(x_0+x/t)\). For large \(|\eta|\), (2.4) therefore has size at least \(|\eta|/2\). The full transposed nonstationary vector field from the stationary-phase lesson, including its divergence, gives

\[
|F_t(\eta)|+|F(\eta)|\leq C_N\langle\eta\rangle^{-N}
\quad\text{for every }N,
\tag{2.5}
\]

uniformly in large \(t\). Each bound uses only finitely many derivatives of \(f\).

The symbol variation can now be frozen at the central frequency. In \(|\eta|<c t\), with \(c<|\xi_0|/2\), the segment from \(t^2\xi_0\) to \(t^2\xi_0+t\eta\) remains in a fixed high-frequency annulus after scaling by \(t^2\). The derivative estimate for \(b\) gives

\[
|b_t(\eta)-b_t(0)|\leq C t^{-1}|\eta|.
\tag{2.6}
\]

For the complementary region \(|\eta|\geq c t\), we only need a uniform polynomial bound. There \(t\leq C\langle\eta\rangle\). If \(r\geq0\), the growth bound for \(b\) gives \(|b_t(\eta)|\leq C\langle\eta\rangle^{2r}\). If \(r<0\), boundedness of \(b\) at all frequencies gives \(|b_t(\eta)|\leq C\langle\eta\rangle^{-2r}\). Thus

\[
|b_t(\eta)|\leq C\langle\eta\rangle^{2|r|},
\qquad |b_t(0)|\leq C.
\tag{2.7}
\]

On the small region, (2.5)–(2.6) bound the integral of \((b_t-b_t(0))F_t\) by \(C/t\). On the complementary region, (2.5)–(2.7), with \(N>2|r|+n+1\), give a tail tending to zero. Hence

\[
\int (b_t(\eta)-b_t(0))F_t(\eta)\,d\eta\longrightarrow0.
\]

Compact convergence and (2.5) also give \(\int F_t\,d\eta\to\int F\,d\eta\). Multiplying by the bounded \(b_t(0)\) proves (2.1).

Finally, a compactly localized smooth distribution has a rapidly decreasing Fourier transform. In the same integral, its transform decreases rapidly near \(t^2\xi_0\), while (2.4) controls the complementary frequencies. The more general wavefront-regular argument in the next section proves the asserted rapid decay, including the fixed polynomial factor in (1.4). ∎

If \(b\) is classical with leading term \(b_r\) homogeneous of the real degree \(r\), then

\[
t^{-2r}b(t^2\xi_0)\longrightarrow b_r(\xi_0),
\qquad
W_t\longrightarrow b_r(\xi_0)U_{A,B}.
\tag{2.8}
\]

The remainder of symbol order \(r-1\) contributes \(O(t^{-2})\) to this coefficient. A complex homogeneous degree \(r+i\nu\) has the additional factor \(t^{2i\nu}\); without removing that factor, (2.8) is not a claimed limit when \(\nu\ne0\).

## 3. A regular covector disappears under every zoom

**Proposition 3.1.** Let \(u\in\mathcal D'\) near \(x_0\), with \((x_0,\xi_0)\notin\operatorname{WF}(u)\), \(\xi_0\ne0\). For \(\psi\) satisfying (1.3), and every real \(K\),

\[
t^K\big(u e^{-it^2\psi}\big)(x_0+x/t)
\longrightarrow0\quad\text{in }\mathcal D'.
\tag{3.1}
\]

**Proof.** Insert a compact cutoff equal to one near \(x_0\), small enough that the compact distribution's Fourier transform is rapidly decreasing in a cone about \(\xi_0\). On every fixed zoomed test support, this replacement is exact for large \(t\).

First take \(\psi_0(y)=\xi_0\cdot(y-x_0)\). The Fourier transform in the zoomed \(x\) variable is

\[
t^{K+n}e^{ix_0\cdot(t^2\xi_0+t\eta)}
\widehat u(t^2\xi_0+t\eta).
\tag{3.2}
\]

For \(|\eta|<c t\), with \(c\) sufficiently small, the argument stays in the good cone and has size comparable to \(t^2\). Its rapid decrease beats the fixed factor \(t^{K+n}\), uniformly on every bounded \(\eta\) set. A compact distribution has a global polynomial Fourier bound. For \(|\eta|\geq c t\), the inequalities \(t\leq C\langle\eta\rangle\) and \(|t^2\xi_0+t\eta|\leq C\langle\eta\rangle^2\) therefore bound (3.2) by one fixed polynomial in \(\eta\), independently of \(t\). The inner region is bounded as well, by choosing enough decay in the good cone. Dominated convergence against Schwartz functions gives convergence to zero in \(\mathcal S'\).

For the actual \(\psi\), write \(p=\psi-\psi_0\). Both its value and first derivative vanish at \(x_0\), so

\[
t^2p(x_0+x/t)\longrightarrow\tfrac12x^T\psi''(x_0)x
\quad\text{in }C^\infty\text{ on compact sets}.
\]

The additional exponential multipliers and all their derivatives consequently converge on each compact test support. They preserve the conclusion just obtained. Explicitly, along any sequence \(t_j\to\infty\), the convergent distributions in (3.2) have a common finite-order bound there; applying that bound to the difference between the varying multiplied test and its limit, then using weak convergence on the fixed limit test, proves (3.1). Since this works along every such sequence, it proves the full limit. ∎

This result makes the tangent model microlocal. Changes in a distribution away from the selected wavefront direction cannot change the model, even if they are singular in other directions.

## 4. Nonlinear coordinates become linear in the limit

**Lemma 4.1 (rescaling a change of coordinates).** Let \(M_\varepsilon(x)=\varepsilon x\), and suppose distributions \(u_\varepsilon\), defined near zero, satisfy

\[
M_\varepsilon^*u_\varepsilon\longrightarrow V
\quad\text{in }\mathcal D',\qquad\varepsilon\downarrow0.
\]

If \(\kappa\) is a smooth local diffeomorphism, \(\kappa(0)=0\), and \(T=\kappa'(0)\), then

\[
M_\varepsilon^*\kappa^*u_\varepsilon\longrightarrow T^*V.
\tag{4.1}
\]

The statement holds for scalar distributions and for half-density distributions, with their respective pullback conventions.

**Proof.** Put \(v_\varepsilon=M_\varepsilon^*u_\varepsilon\). The exact conjugated map is

\[
\kappa_\varepsilon=M_\varepsilon^{-1}\circ\kappa\circ M_\varepsilon,
\qquad \kappa_\varepsilon(x)=\varepsilon^{-1}\kappa(\varepsilon x).
\]

Thus the left side of (4.1) is \(\kappa_\varepsilon^*v_\varepsilon\). Taylor's formula and differentiation give \(\kappa_\varepsilon\to T\) in \(C^\infty\) on every compact set. The inverse maps are \(\varepsilon^{-1}\kappa^{-1}(\varepsilon y)\), which likewise converge to \(T^{-1}\).

For a fixed compact test support, the transposed pullbacks of that test have their supports in one fixed compact set. For scalars, the transposed test is

\[
f(\kappa_\varepsilon^{-1}(y))
|\det D\kappa_\varepsilon^{-1}(y)|.
\]

For half densities its Jacobian exponent is \(1/2\). In either case these tests converge in \(C_c^\infty\) to the corresponding test for \(T\). Along an arbitrary sequence \(\varepsilon_j\downarrow0\), uniform boundedness of the convergent \(v_{\varepsilon_j}\) supplies a common finite-order estimate. It bounds their pairing with the difference of the varying test and its limit by a quantity tending to zero. Their pairing with the fixed limit test tends to that of \(V\). This proves (4.1) along every sequence, and hence the result. ∎

After centering charts at \(x_0\), the lemma says that an existing tangent limit is a distribution on \(T_{x_0}X\). For half densities, it transforms with the half-density Jacobian of the tangent linear map. Changing a smooth bundle frame contributes only its value at \(x_0\), by the same varying-test argument, so vector coefficients belong to the fiber \(E_{x_0}\).

The function \(\psi\) is also a choice. If it is replaced by \(\psi+p\), where \(p(x_0)=p'(x_0)=0\), then the tangent limit is multiplied by

\[
e^{-ix^Tp''(x_0)x/2}.
\tag{4.2}
\]

Equivalently \(B\) in the quadratic model becomes \(B+p''(x_0)\). These chirp identifications are transitive because their exponents add. They are the elementary change between the linear reference Lagrangian planes \(\eta=Bx\).

## 5. Evaluate the model even when the Hessian is singular

Let \(A\) be any real symmetric matrix, with rank \(k\). Split orthogonally

\[
\mathbb R^n=\operatorname{ran}A\oplus\ker A,
\qquad x=(y,z),\qquad A_R=A|_{\operatorname{ran}A}.
\]

The restriction \(A_R\) is invertible, and let \(B_R\) be the restriction of the quadratic form \(B\) to \(\operatorname{ran}A\). Exact Fourier inversion in the kernel variables gives a point mass \(\delta_0(z)\). The Fresnel identity in the other \(k\) variables gives

\[
\begin{aligned}
U_{A,B}(y,z)
={}&(2\pi)^{n/4-k/2}|\det A_R|^{-1/2}
e^{-i\pi\operatorname{sgn}A_R/4}\\
&\quad\times
e^{iy^T(A_R^{-1}-B_R)y/2}\delta_0(z).
\end{aligned}
\tag{5.1}
\]

When \(k=0\), the empty determinant is one, the empty signature is zero, and (5.1) is \((2\pi)^{n/4}\delta_0(x)\). The sign in the Fresnel factor is negative because the frequency Hessian of the phase is \(-A_R\). Terms in \(B\) containing \(z\) vanish on multiplication with \(\delta_0(z)\), so only \(B_R\) remains.

For the tangent model of a conic graph, \(A\xi_0=0\): differentiate Euler's identity for \(H\). Thus its frequency Hessian is always singular at a nonzero covector. Formula (5.1) covers precisely that possibility, and the model is a nonzero Gaussian simple layer on \(\operatorname{ran}A\).

The phase in (1.6) has critical equation \(x=A\eta\) and output covector \(\eta-Bx\). Its linear Lagrangian is therefore

\[
\lambda_{A,B}=\{(A\eta,\eta-BA\eta):\eta\in\mathbb R^n\}.
\tag{5.2}
\]

The tangent plane of the original graph is \(\{(A\eta,\eta)\}\). Removing the Hessian of \(\psi\) applies the canonical shear \((x,\eta)\mapsto(x,\eta-Bx)\). This explains why the model is determined by those two tangent planes rather than by higher derivatives of \(H\) or \(\psi\).

## 6. Exercises with complete solutions

**Exercise 6.1 (the two scales; introductory).** Replace the substitution in the zoom proof by \(\xi=t^a\xi_0+t^b\eta\) and the spatial scale by \(x_0+t^{-c}x\). Determine the relations among \(a,b,c\) that keep both the cross term \(x\cdot\eta\) and the quadratic frequency term at order one.

**Solution.** The cross term has factor \(t^{b-c}\), so \(b=c\). By degree-one homogeneity the frequency Hessian at \(t^a\xi_0\) is \(t^{-a}H''(\xi_0)\), so its quadratic deviation has factor \(t^{2b-a}\); thus \(a=2b=2c\). The phase-removal frequency is \(t^a\), and its spatial quadratic term has factor \(t^{a-2c}=1\) as well. Taking \(c=1\) gives the scales \(t^2,t,t^{-1}\) used above. If the particular Hessian vanishes, its term imposes no constraint, but these relations give the common nondegenerate quadratic scaling across all graphs.

**Exercise 6.2 (a sphere tangent model; intermediate).** Take \(H(\xi)=c|\xi|\), \(c\ne0\), \(\xi_0=s e_1\), \(s>0\), and \(\psi(x)=\xi_0\cdot(x-ce_1)\). Compute \(U_{A,0}\).

**Solution.** Here \(x_0=ce_1\) and
\[
A=\frac cs(I-e_1e_1^T).
\]
It has kernel \(\mathbb R e_1\), rank \(n-1\), and signature \((n-1)\operatorname{sgn}c\). Writing \(x=(x_1,x')\), formula (5.1) gives
\[
U_{A,0}=(2\pi)^{n/4-(n-1)/2}
|c/s|^{-(n-1)/2}
e^{-i\pi(n-1)\operatorname{sgn}c/4}
e^{is|x'|^2/(2c)}\delta_0(x_1).
\]
The supporting hyperplane is the tangent plane of the sphere \(|x|=|c|\) at \(ce_1\), in the translated tangent variables. For \(n=1\) the empty-factor convention gives \((2\pi)^{1/4}\delta_0\).

**Exercise 6.3 (an ordinary symbol with no zoom limit; intermediate).** In dimension one take \(H=0\), \(\xi_0=1\), and, for positive high frequencies,
\[
b(\xi)=\xi^r\big(2+\sin(\log\xi)\big),
\]
with a smooth cutoff that removes low and negative frequencies. Show that this is an ordinary symbol and that a compact localization of its inverse phase integral can have no limit in (1.4).

**Solution.** Each frequency derivative is bounded by \(C_k\xi^{r-k}\), because differentiating \(\log\xi\) or the power costs one inverse frequency. Thus \(b\in S^r\), with \(m=r+1/4\). The normalized central coefficient is \(t^{-2r}b(t^2)=2+\sin(2\log t)\). A compact base cutoff equal to one near zero changes the reduced symbol only by \(S^{r-1}\), by Fourier reduction for \(x\xi\); that change contributes \(O(t^{-2})\) to the coefficient. Take \(\psi(x)=x\). Here \(A=B=0\) and \(U=(2\pi)^{1/4}\delta_0\). Along \(t_j=\exp(\pi j+\pi/4)\) the coefficient tends to three, and along \(s_j=\exp(\pi j+3\pi/4)\) it tends to one. Theorem 2.1 gives these two distinct distributional limits. A test nonzero at zero distinguishes them. The general asymptotic comparison is therefore strictly more general than (2.8).

**Exercise 6.4 (a nonlinear chart; intermediate).** In dimension one let \(\kappa(x)=a x+d x^2\), \(a\ne0\), near zero. If a rescaled half-density family has limit \(C\delta_0\), compute its limit after changing coordinates by \(\kappa\).

**Solution.** The conjugated map is \(\varepsilon^{-1}\kappa(\varepsilon x)=a x+d\varepsilon x^2\), converging to multiplication by \(a\). The scalar pullback of \(\delta_0\) is \(|a|^{-1}\delta_0\). Half-density pullback contributes the Jacobian factor \(|a|^{1/2}\), so the resulting coefficient is \(C|a|^{-1/2}\delta_0\) in the new half-density frame. The quadratic chart coefficient \(d\) does not enter the tangent pullback. This concerns the full rescaled family; its phase-removal function must be transformed with the same coordinate change.

**Exercise 6.5 (complex conjugation; advanced).** Show directly that \(\overline{U_{A,B}}=U_{-A,-B}\). If the Fourier phase of \(u\) is \(H\), find the graph phase and central covector for \(\overline u\).

**Solution.** Conjugate (1.6) and replace \(\eta\) by \(-\eta\). The cross term returns to \(x\cdot\eta\), and both quadratic matrices change sign. This proves the model identity, including the opposite Fresnel signature. Since \(\widehat{\overline u}(\xi)=\overline{\widehat u(-\xi)}\), the new graph function is \(\widetilde H(\xi)=-H(-\xi)\), and its base gradient is \(H'(-\xi)\). The selected point is therefore \((x_0,-\xi_0)\), and the new normalized amplitude is \(\overline{b(-\xi)}\). The Hessian at \(-\xi_0\) is \(-A\); taking phase removal \(-\psi\) gives \(-B\). Thus the conjugated zoom has exactly the conjugated quadratic model. Patching this statement globally will also require conjugating the Maslov transition factors.

**Exercise 6.6 (an exact distributional zoom; advanced).** On \(\mathbb R\), take \(u=D^q\delta_0\), with \(q\) a nonnegative integer, \(H=0\), and \(\psi(y)=\xi_0y\), \(\xi_0\ne0\). Compute (1.4) exactly and identify its limit.

**Solution.** The Fourier transform of \(u\) is \(\xi^q\), so its intrinsic order is \(m=q+1/4\). Fourier transformation of the rescaled and modulated distribution gives
\[
\widehat W_t(\eta)=t^{-2q}(t\eta+t^2\xi_0)^q
=(\xi_0+\eta/t)^q.
\]
Thus the exact formula is
\[
W_t=\sum_{k=0}^q\binom qk\xi_0^{q-k}t^{-k}D^k\delta_0.
\]
The limit is \(\xi_0^q\delta_0\). In Theorem 2.1, the normalized coefficient is \((2\pi)^{-1/4}\xi_0^q\), and \(U_{0,0}=(2\pi)^{1/4}\delta_0\), giving exactly that limit. For \(q\geq1\), the first correction is \(q\xi_0^{q-1}t^{-1}D\delta_0\); its order shows why a universal \(O(t^{-2})\) error is not supplied by the classical coefficient's \(O(t^{-2})\) remainder alone.

## References

- [Hörmander III, §21.6] Lars Hörmander, *The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*, corrected second printing, Springer, 1994, §21.6, especially. The exact approved purchased reprint was read for this restoration.
- [Hörmander IV, §25.1] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, corrected second printing, Springer, 1994, §25.1, especially Proposition 25.1.7, its wavefront remark and Lemma 25.1.8. The exact approved purchased reprint was read for this restoration.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Restoration and exact prerequisite review: GPT-6 Astra (OpenAI), Ultra, 5 October 2026. The course owner checked this lesson and its programme proof chain; human mathematical review remains pending. Original text: public domain (CC0).*
