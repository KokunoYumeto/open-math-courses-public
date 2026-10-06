# A positive quantization and the sharp lower bound

The energy method needs a lower bound for an operator of order one, uniform over bounded symbol families. A pointwise nonnegative left symbol need not define a nonnegative operator. We construct a positive operator whose difference from the original has one lower order.

This is a modified selection from *Elliptic Operators & Boundary Problems: Renewed 2026 Course Draft*. Original principal author: AN-03 course-writing task. Original publisher: AN-03 local course project. Copyright © 2026 AN-03 course project contributors. The AN-03 course-writing task and OpenAI Codex are responsible for the renewed edition. Selection, current prerequisite bindings and explicitly identified connecting proofs: GPT-6 Astra (OpenAI), Ultra, 5 October 2026; publisher: AN-04 local course project.

Permission is granted to copy, distribute and modify this component under the GNU Free Documentation License, Version 1.2 only, with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. The [complete licence](notices/COPYING), [title information](notices/TITLE_PAGE.md), [history](notices/HISTORY.md) and [rights notice](notices/RIGHTS.md) accompany it.

## G0. Exact scope and complete earlier proofs

This selection retains the moving-probe and cancellation arguments of AN-03, *Positivity through a moving family of scalar probes*, Sections 4–5. Here their parameters are fixed at \(\rho=1,\delta=0,\kappa=\rho-\delta=1,\sigma=1/2\), their coefficient space is \(\mathbb C\), and all symbols are global ordinary symbols. Thus every norm-valued integral below is a scalar integral and every \(H\) is \(\mathbb C\). The wider parameter extensions are omitted from this selection; their source remains unchanged. Section G6 supplies the complete receiving inequality at every real Sobolev order using this course's current global operator proofs.

Use \(D=-i\partial\), the inner product linear in its first argument, and
\[
 \operatorname{Op}(a)u(x)=(2\pi)^{-n}
       \int e^{ix\cdot\xi}a(x,\xi)\widehat u(\xi)\,d\xi,\qquad
 p_{r,L}(a)=\max_{|\alpha|+|\beta|\le L}
       \sup_{x,\xi}\langle\xi\rangle^{-r+|\alpha|}
                  |\partial_\xi^\alpha\partial_x^\beta a(x,\xi)|.
 \tag{G1}
\]
Here \(n\ge1\). In dimension zero the operator is scalar multiplication and the nonnegative-real-part assertion is immediate. The [complete packet estimate E23–E27](../20261005-restored-airy-models/bounded-derivative-operators.md) holds globally without compact base support. The [ordinary composition and adjoint proofs O1–O3](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md) supply finite-seminorm remainders. [Fourier L1–L3](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md) and [measure M0–M8](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) supply inversion, Plancherel, every change of variables, dominated convergence, completeness and density. The [compact Taylor and derivative proof](../20261004-free-stationary-phase/proof-map.html#FTC-TAYLOR-COMPACT-PARAMETERS) supplies the Taylor estimates; smooth normalized even bumps come from [U001 Appendix A.4](../20261004-free-stationary-phase/stationary-phase-and-critical-manifolds.md#a-4-finite-smooth-cutoffs). These are actual included proofs, with exact hashes and locators in the [proof map](proof-map.json).

## G1. Global Sobolev bounds with the original norms

Put \(E_s=\langle D\rangle^s\). By the complete Fourier proof,
\[
 \|u\|_s^2=(2\pi)^{-n}\int\langle\xi\rangle^{2s}|\widehat u(\xi)|^2\,d\xi,
 \qquad E_s:H^s\longrightarrow L^2
 \quad\hbox{is an onto isometry with inverse }E_{-s}.
 \tag{G2}
\]
Completeness and simultaneous Schwartz density in any finite list of these spaces follow by applying the compact smooth density proof to the Fourier function after truncating its support; on that support all the finitely many weights are bounded above and below. Smoothing the truncated Fourier function and then inverting gives Schwartz approximants in every chosen norm. Cauchy–Schwarz in frequency shows convergence in each \(H^s\) implies convergence in tempered distributions: a Schwartz test absorbs the reciprocal polynomial weight.

If \(a\in S^r\), O3 gives a full symbol \(c\in S^0\) for \(E_{s-r}\operatorname{Op}(a)E_{-s}\). Each required bounded derivative of \(c\) is controlled by finitely many original seminorms of \(a\). The global packet estimate therefore proves
\[
 \|\operatorname{Op}(a)u\|_{s-r}
       \le C_{r,s,n}p_{r,J}(a)\|u\|_s .
 \tag{G3}
\]
The identity first holds on Schwartz functions; density extends it to \(H^s\). Simultaneous density and distributional convergence make all these extensions agree with the O3 distributional operator. Thus no compact base support is imposed. In particular a symbol of order \(2m\) maps \(H^m\) to \(H^{-m}\), and the Fourier Cauchy–Schwarz inequality gives
\[
 |(\operatorname{Op}(a)u,u)|\le C p_{2m,J}(a)\|u\|_m^2.
 \tag{G4}
\]
The dual pairing is precisely the extension of the original \(L^2\) pairing. The symbol bounds for \(\langle\xi\rangle^s\) follow by repeated differentiation: each term is a polynomial of degree at most the number of derivatives times a corresponding lower real power of \(1+|\xi|^2\), giving order \(s-|\alpha|\).

## G4. A positive scalar probe and its moving copies

Choose an even \(\varphi\in C_c^\infty(\mathbb R^{2n})\) with \(\|\varphi\|_{L^2(\mathbb R^{2n})}=1\). Even means simultaneous inversion of both variables. Let \(B=\operatorname{Op}(\varphi)\), acting on scalar functions. Its kernel is Schwartz. The kernel
\[
 K_Q(x,z)=\int\overline{K_B(t,x)}K_B(t,z)\,dt
\tag{P22}
\]
is Schwartz as well: differentiate under the integral and use the rapid decay of the two factors with any desired polynomial weights. Fourier transformation in \(x-z\) therefore defines a unique \(\psi\in\mathcal S(\mathbb R^{2n})\) with
\[
 \operatorname{Op}(\psi)=B^*B.
\tag{P23}
\]
Conjugation by parity \(u(x)\mapsto u(-x)\) fixes \(B\) because \(\varphi\) is even. It fixes \(B^*B\) too, so uniqueness of the Schwartz kernel symbol proves that \(\psi\) is even. The function \(\psi\) need not be real or pointwise nonnegative: the property being imposed is positivity of its quantization.

The normalization is precisely
\[
 \int\psi(x,\xi)\,dx\,d\xi=1.
\tag{P24}
\]
Indeed Fourier inversion on the diagonal gives
\((2\pi)^{-n}\int\psi=\int K_Q(x,x)\,dx\). By (P22) the latter equals \(\iint|K_B(t,x)|^2\,dt\,dx\). Scalar Plancherel in the kernel formula for \(B\) makes this \((2\pi)^{-n}\|\varphi\|_2^2\). Cancelling the common factor proves (P24). This computation uses ordinary integrals of Schwartz kernels, and needs no trace-class theorem.

For \(q>0\) define the scalar unitary
\[
 (U_{y,\eta,q}v)(x)=q^{n/2}e^{i\eta\cdot x}v(q(x-y)).
\tag{P25}
\]
Changing variables in (G1) gives
\[
 U_{y,\eta,q}\operatorname{Op}(\psi)U_{y,\eta,q}^*
 =\operatorname{Op}\!\left(
 \psi(q(x-y),(\xi-\eta)/q)\right).
\tag{P26}
\]
These scalar operators act on \(H\)-valued functions too, by the same kernels. A bounded coefficient \(A\in\mathcal L(H)\) commutes with them. If \(A\geq0\), then for \(u\in\mathcal S(H)\),
\[
 \left\langle U B^*B U^*Au,u\right\rangle
 =\left\langle A B U^*u,B U^*u\right\rangle_{L^2(H)}\geq0.
\tag{P27}
\]
No diagonalization of \(A\), finite rank condition, or separability assumption on \(H\) is used.

Put
\[
 \sigma=\frac{\rho+\delta}{2},\quad q(\eta)=\langle\eta\rangle^\sigma,
 \qquad 0<\sigma<1.
\tag{P28}
\]

For a scalar symbol \(b\), and any Schwartz function \(v\) on phase space, define
\[
 (\mathcal I_v b)(x,\xi)=\iint
 v\!\left(q(\eta)(x-y),\frac{\xi-\eta}{q(\eta)}\right)
 b(y,\eta)\,dy\,d\eta.
\tag{P29}
\]
This is an absolutely convergent scalar integral for every symbol of finite order. To see this, first integrate its scalar majorant in \(y\). For every large \(M\), the result is at most
\[
 C_M\int q(\eta)^{-n}\langle\eta\rangle^r
 \left(1+\frac{|\xi-\eta|}{q(\eta)}\right)^{-M}d\eta.
\tag{P30}
\]
For large \(|\eta|\) with \(\xi\) fixed, the parenthesis grows like \(\langle\eta\rangle^{1-\sigma}\), so an arbitrarily large \(M\) dominates the remaining polynomial factors. Differentiating the integrand only creates further polynomial factors and Schwartz derivatives. The same reasoning gives local uniform convergence of every differentiated integral, hence norm smoothness.

For a nonnegative \(a(x,\xi)\in\mathcal L(H)\) in any finite-order symbol class, set \(a_+=\mathcal I_\psi a\). Then
\[
 \langle\operatorname{Op}(a_+)u,u\rangle
 =\iint\left\langle a(y,\eta)B U_{y,\eta,q(\eta)}^*u,
                         B U_{y,\eta,q(\eta)}^*u\right\rangle
 \,dy\,d\eta\geq0.
\tag{P31}
\]
We verify convergence of the quadratic integral, since its parameter domain is unbounded. A direct Fourier transformation gives
\[
 B U_{y,\eta,q}^*u(t)
 =(2\pi)^{-n}q^{n/2}\int
 e^{i(t+qy)\cdot\theta}\varphi(t,\theta)
 \widehat u(\eta+q\theta)\,d\theta.
\tag{P32}
\]
For the original nonnegative range, both \(t\) and \(\theta\) in this integral lie in fixed compact sets. As \(|\eta|\to\infty\), \(q(\eta)=o(|\eta|)\), so \(|\eta+q\theta|\geq|\eta|/2\) there. Integrating by parts in \(\theta\) gives arbitrary powers of \(\langle t+qy\rangle^{-1}\); the derivatives of \(\widehat u\) still decrease faster than any frequency power, and the factors \(q\) they create have polynomial growth in \(\eta\). Since \(q\geq1\), this proves an arbitrary product decay in \(\langle y\rangle\) and \(\langle\eta\rangle\) for the \(L^2_t(H)\) norm of (P32). Bounded \(\eta\) is handled by the same integration by parts. This decay makes (P31) absolutely convergent even after the factor \(\|a(y,\eta)\|\leq C\langle\eta\rangle^r\). For compact parameter cutoffs, (P26), Fubini and polarization prove the equality in (P31). Letting the cutoffs tend to one, (P30), (P32), and dominated convergence prove the displayed equality for all Schwartz inputs. Thus (P31) constructs positivity as a quadratic-form statement, without asserting a bounded operator when the order is positive.

## G5. Two cancellations and the full error

Let \(v\in\mathcal S(\mathbb R^{2n})\) be even and let \(c_v=\int v\). For every scalar \(b\in S^r_{\rho,\delta}\),
\[
 T_vb:=\mathcal I_vb-c_vb
 \in S^{r-\kappa}_{\rho,\delta}.
\tag{P33}
\]
Every seminorm of this difference is bounded by finitely many seminorms of \(b\) and \(v\). We first prove its undifferentiated form and then derive exact identities for all derivatives.

Write \(\lambda=\langle\xi\rangle\) and \(Q=\lambda^\sigma\). Separate the integral into \(|\eta-\xi|\geq\lambda/2\) and its complement. The first region contributes \(O(\lambda^{-L})\) for every desired \(L\), using finitely many Schwartz seminorms. Here is the original nonnegative-exponent estimate behind that assertion. If \(|\eta|\leq4\lambda\), then \(q(\eta)\leq C\lambda^\sigma\) and the ratio in (P30) is at least \(c\lambda^{1-\sigma}\); its arbitrary negative power absorbs the region's polynomial volume and symbol weight. If \(|\eta|>4\lambda\), the ratio is at least \(c\langle\eta\rangle^{1-\sigma}\), and integration of the resulting power gives the same conclusion. The estimate also holds after inserting any fixed polynomial in \(y-x\) and \(\eta-\xi\): integrate the position polynomial against the Schwartz decay first, and increase \(M\). This will allow us to replace truncated polynomial moments by full moments.

In the complementary region, \(\langle\eta\rangle\), \(\langle\xi\rangle\), and the weights along their connecting segment are comparable. Set
\[
 z=Q(y-x),\qquad \theta=(\eta-\xi)/Q,
 \qquad R=\frac{q(\xi+Q\theta)}{Q}.
\tag{P34}
\]
The Jacobian \(dy\,d\eta\) is \(dz\,d\theta\). Evenness replaces the kernel by \(v(Rz,\theta/R)\). The ratios \(R,R^{-1}\) are bounded in this region. Taylor's formula for \(q\), using
\(\partial^\gamma q=O(\lambda^{\sigma-|\gamma|})\), gives
\[
 R-1=\nabla q(\xi)\cdot\theta
       +O(\lambda^{2\sigma-2}|\theta|^2),
 \qquad |R-1|\leq C\lambda^{\sigma-1}|\theta|.
\tag{P35}
\]
Define the scalar differential operator
\[
 \mathcal L v(z,\theta)=z\cdot\partial_zv-\theta\cdot\partial_\theta v.
\tag{P36}
\]
Uniformly for bounded positive \(R,R^{-1}\), Taylor expansion in the scalar dilation parameter implies, for every \(M\),
\[
 v(Rz,\theta/R)
 =v(z,\theta)+(\nabla q(\xi)\cdot\theta)\mathcal L v(z,\theta)
 +E_\xi(z,\theta),
\]
\[
 |E_\xi(z,\theta)|
 \leq C_M\lambda^{2\sigma-2}
 \langle(z,\theta)\rangle^{-M}|\theta|^2.
\tag{P37}
\]
Indeed the first and second dilation derivatives of \(v(Rz,\theta/R)\) are Schwartz with uniformly controlled seminorms on a compact interval of \(R\)'s; then use both parts of (P35). This proves (P37) without treating the moving scale as a constant.

The zeroth moment of \(\mathcal L v\) is zero, by integration by parts and equality of the two dimensions. Also \(v\) and \(\mathcal L v\) are even. Consequently the ordinary degree-one moments of \(v\), and the integral of \(\theta_j\mathcal L v\), vanish. Write \(M_{\alpha\beta}\) for the kernel moment with factor \((\eta-\xi)^\alpha(y-x)^\beta\), restricted to the complementary region. Equations (P34)–(P37), together with the tail estimate, yield
\[
 \begin{aligned}
 M_{00}&=c_v+O(\lambda^{2\sigma-2}),\\
 |M_{\alpha\beta}|&\leq C Q^{|\alpha|-|\beta|}
                         \lambda^{\sigma-1}
       &&(|\alpha|+|\beta|=1),\\
 |M_{\alpha\beta}|&\leq C Q^{|\alpha|-|\beta|}
       &&(|\alpha|+|\beta|=2).
 \end{aligned}
\tag{P38}
\]
For the first line the fixed zeroth moment is \(c_v\), the linear scale correction integrates to zero by parity, and (P37) controls the remainder. For the second line the fixed moment vanishes, the scale correction is \(O(\lambda^{\sigma-1})\), and its second-order remainder is smaller since \(\sigma<1\). For the third line an absolute Schwartz moment bound suffices. Thus the first cancellation comes from odd symbol moments and the second comes from the scale correction to total mass.

Expand \(b(y,\eta)\) at \((x,\xi)\) through total degree two. In the scaled variables, a position increment contributes \(Q^{-1}\lambda^\delta=\lambda^{-\kappa/2}\), and a frequency increment contributes \(Q\lambda^{-\rho}=\lambda^{-\kappa/2}\). The integral remainder is therefore bounded in norm by
\[
 C\lambda^{r-3\kappa/2}(|z|+|\theta|)^3.
\tag{P39}
\]
This estimate is uniform in position because the symbol bounds are global there; the frequency segment stays in the comparable-weight region. Multiplication by the actual kernel and integration leaves the same power of \(\lambda\).

The constant term after subtraction of \(c_vb\) is at most \(C\lambda^{r+2\sigma-2}\). Each linear term is at most \(C\lambda^{r-\kappa/2+\sigma-1}\); each quadratic term is at most \(C\lambda^{r-\kappa}\). Since
\[
 2\sigma-2\leq-\kappa,
 \qquad \sigma-1\leq-\kappa/2,
\tag{P40}
\]
both inequalities being equivalent to \(\rho\leq1\), these terms and (P39) prove \(\|T_vb(x,\xi)\|\leq C\lambda^{r-\kappa}\).

To obtain all derivatives, put \(F_j(\eta)=q(\eta)^{-1}\partial_jq(\eta)\in S^{-1}_{1,0}\). Direct differentiation of the kernel, followed by integration by parts in \(y\) or \(\eta\), gives the exact identities
\[
 \partial_{x_j}\mathcal I_v b=\mathcal I_v(\partial_{x_j}b),
 \qquad
 \partial_{\xi_j}\mathcal I_v b
 =\mathcal I_v(\partial_{\xi_j}b)+\mathcal I_{\mathcal L v}(F_jb).
\tag{P41}
\]
For the second identity, the sum of differentiation in \(\xi_j\) and \(\eta_j\) of the kernel is \(F_j\) times the kernel with \(v\) replaced by \(\mathcal L v\). Boundary terms vanish by (P30) with larger exponents. Since \(c_{\mathcal L v}=0\), subtraction gives
\[
 \partial_{x_j}T_vb=T_v(\partial_{x_j}b),
 \qquad
 \partial_{\xi_j}T_vb=T_v(\partial_{\xi_j}b)+T_{\mathcal L v}(F_jb).
\tag{P42}
\]
Iterating (P42) produces finitely many terms with even Schwartz kernels \(\mathcal L^kv\). Each position differentiation increases the input order by \(\delta\); each frequency differentiation either decreases it by \(\rho\) on \(b\), or introduces a factor of order minus one. Derivatives of those factors decrease their orders further. Since \(\rho\leq1\), every term after \(\alpha\) frequency and \(\beta\) position derivatives has input order at most \(r-\rho|\alpha|+\delta|\beta|\). Applying the undifferentiated estimate just proved to each term proves (P33) with its full differentiated bounds. Every step uses only finitely many input derivatives and Schwartz moments for any specified output seminorm. ∎

There is a useful more precise classical estimate. With \((\rho,\delta)=(1,0)\), so \(Q=\lambda^{1/2}\), (P38) gives for total degree at most two a coefficient bounded by \(C\lambda^{|\alpha|-1}\), except that the zeroth coefficient is understood after subtracting \(c_v\). Retaining the derivatives of \(b\) instead of bounding them by its order gives
\[
 \|T_vb(x,\xi)\|
 \leq C_1\sum_{|\alpha|+|\beta|\leq2}
 \lambda^{|\alpha|-1}
 \|\partial_\xi^\alpha\partial_x^\beta b(x,\xi)\|
 +C_2p_{r,L}(b)\lambda^{r-3/2}.
\tag{P43}
\]
Here \(L\) is finite, \(C_1,C_2\) depend on the chosen kernel, dimension and order, and the high-frequency tail has been included by choosing sufficiently many of its powers. Formula (P43) is an estimate by actual derivatives at the specified point, together with a controlled higher-derivative remainder. It is stronger than the order assertion alone.

## G6. The full sharp lower bound and its energy receiver

**Theorem.** For every real \(m\), an ordinary scalar symbol \(a\in S^{2m+1}\) with \(\operatorname{Re}a\ge0\) satisfies
\[
 \operatorname{Re}(\operatorname{Op}(a)u,u)
       \ge -C_{m,n}p_{2m+1,J}(a)\|u\|_m^2,\qquad u\in\mathcal S,
 \tag{G5}
\]
for a fixed finite \(J\). The constant is uniform over each bounded symbol family.

For real \(a\ge0\), P24 and P31 give a nonnegative quadratic form for \(a_+=\mathcal I_\psi a\), and P33–P42 give \(a-a_+\in S^{2m}\), with each output seminorm bounded by finitely many input seminorms. The full convergence proof of P31 justifies this form even for positive input order. Apply G4 to that difference. This proves G5 for real \(a\).

For complex \(a\), write \(a=A+iB\), with \(A=\operatorname{Re}a\ge0\) and \(B=\operatorname{Im}a\) real. The first case controls \(A\). O3 gives \(\operatorname{Op}(B)^*-\operatorname{Op}(B)\in\operatorname{Op}(S^{2m})\), with finite-seminorm control, and
\[
 \operatorname{Re}(i\operatorname{Op}(B)u,u)
       =\frac{i}{2}\big((\operatorname{Op}(B)-\operatorname{Op}(B)^*)u,u\big).
 \tag{G6}
\]
The inner product convention in G1 gives this sign: the second adjoint pairing is the conjugate of the first. G4 bounds the absolute value of the right side, proving G5.

For \(a\in S^1\) with \(\operatorname{Re}a\ge-C_0\), apply G5 with \(m=0\) to \(a+C_0\) and subtract \(C_0\|u\|_2^2\). We obtain a uniform \(c\) with
\[
 \operatorname{Re}(\operatorname{Op}(a)u,u)\ge-c\|u\|_2^2
       \quad(u\in H^1).
 \tag{G7}
\]
Indeed Schwartz approximation in \(H^1\) and G3 with \(r=s=1\) pass both pairings to the limit. For every real \(s\), O3 gives the full symbol of \(E_s\operatorname{Op}(a)E_{-s}\) equal to \(a+d_s\), where \(d_s\in S^0\) uniformly on bounded subsets of \(S^1\): the zeroth product is exactly \(a\), and each differentiated term and its complete remainder lose at least one order. The global packet bound for \(d_s\) then gives the same lower form bound with a constant \(c_s\). Thus all real energy orders are justified without requiring positivity of the conjugated pointwise symbol.

## G7. Strong time continuity under local symbol continuity

Suppose \(a(t)\) is bounded in \(S^r\) and continuous in distributions in \((x,\xi)\). On every compact box, the derivatives form bounded equicontinuous families, since one more derivative is uniformly bounded. Here is the needed compactness argument. Choose the countable set of rational grid points in all integer boxes and all derivative orders. Successive convergent scalar subsequences and a diagonal subsequence give convergence at all those points. Finite sufficiently fine nets and the common derivative bound turn convergence on that dense set into uniform convergence on each compact box. The fundamental theorem on coordinate segments shows that these limits are successive derivatives of one smooth function. The distributional limit identifies it with \(a(t_0)\). If local smooth convergence as \(t\to t_0\) failed, a sequence witnessing failure would have a subsequence of the preceding kind, a contradiction. Thus distributional continuity and boundedness give precisely local smooth continuity.

For fixed \(w\in\mathcal S\), the integral G1 and dominated convergence give local smooth convergence of \(\operatorname{Op}(a(t))w\). O1 bounds every output Schwartz seminorm uniformly. On the complement of a large base ball, one extra position weight makes the tail arbitrarily small; on the ball use local convergence. This proves convergence in \(\mathcal S\). Now G3 and Schwartz density give strong continuity \(H^s\to H^{s-r}\): approximate a fixed vector by a Schwartz vector, bound the difference of its two images by twice the uniform G3 constant, and then use the already proved convergence on that Schwartz vector.

For \(u\in C([0,T];H^s)\), add and subtract \(\operatorname{Op}(a(t))u(t_0)\). The uniform bound controls the varying-vector error, and strong continuity controls the fixed-vector error. Hence \(t\mapsto\operatorname{Op}(a(t))u(t)\) is continuous in \(H^{s-r}\). No operator-norm continuity or global symbol-seminorm continuity follows or is used.

## Sources and exact receiving scope

The retained P22–P43 proof is a modified ordinary-parameter selection from AN03-U011, *Positivity through a moving family of scalar probes*. Its moving-window normalization, quadratic positivity, both moment cancellations and complete differentiated remainder are retained. Wider parameter extensions were omitted, and G1, G6–G7 give explicit current receiving arguments. The mathematical antecedent is Lars Hörmander, *The Analysis of Linear Partial Differential Operators III*, the approved 2007 edition, Theorem 18.1.14 and its proof; the first-order energy application is §23.1. The book is an admitted source for mathematics and credit. No book text or files are included.

This companion completes the sharp lower-bound and global continuity inputs of U030. It does not yet certify U030's spacetime composition, restriction or entire dependency chain.
