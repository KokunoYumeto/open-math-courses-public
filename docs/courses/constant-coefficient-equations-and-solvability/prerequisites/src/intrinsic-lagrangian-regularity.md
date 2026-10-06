# Recognizing a Lagrangian distribution intrinsically

A phase representation tells us how to produce a singular distribution. An intrinsic definition tells us how to recognize the same object without first choosing a phase. The link is an endpoint regularity condition: applying any sequence of first-order operators whose principal symbols vanish on the Lagrangian leaves the distribution in one fixed Besov space. Near a frequency graph, those operators become frequency derivatives of a symbol.

We use the ordinary pseudodifferential calculus, its properly supported versions, and its Sobolev and Besov mapping theorems from Symbols, operators and Sobolev scales. Coordinate and bundle invariance, conic parametrices and pseudolocality are supplied by Detecting regularity without choosing coordinates. The dyadic endpoint and local frequency Sobolev estimate are also developed in Singularities along a submanifold and smooth boundary passage. Our local geometry and Fourier reduction are in [Phase space and generating families](phase-space-and-generating-families.md) and [Oscillatory distributions and their order](oscillatory-distributions-and-order.md). The authority for the intrinsic results is [Hörmander IV, §25.1].

Throughout, \(D=-i\partial\), \(\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx\), and inverse Fourier transformation has factor \((2\pi)^{-n}\). Symbols are ordinary \(S^r=S^r_{1,0}\); a homogeneous expansion is required only when stated.

## 1. The endpoint and the vanishing ideal

Let \(X\) be a smooth \(n\)-dimensional manifold and \(E\to X\) a smooth finite-rank complex vector bundle. Write

\[
\mathcal B^s(X;E)=B^s_{2,\infty,\mathrm{loc}}(X;E).
\]

At the entry base we use completeness of \(L^2\) and density of \(C_c^\infty\) in it. The imported Schwartz Plancherel identity then extends \((2\pi)^{-n/2}\mathcal F\) uniquely to an isometry on \(L^2\): approximate an input by compact smooth functions and take the complete-space limit. The image is closed and contains Schwartz space by Fourier inversion, so it is all of \(L^2\). Pairing those approximants with Schwartz tests and using Cauchy–Schwarz shows that this extension agrees with the tempered-distribution Fourier transform. Thus the block norms below have their exact Fourier meaning, including for nonsmooth \(L^2\) functions.

In each compactly localized chart and frame, its norm is the supremum of \(2^{js}\|\Pi_j u\|_2\) over dyadic Fourier blocks. Changing charts, frames, cutoffs or dyadic partitions gives equivalent local seminorms by the imported mapping results. In particular, for every \(\varepsilon>0\),

\[
H^s_{\mathrm{loc}}\subset\mathcal B^s
\subset H^{s-\varepsilon}_{\mathrm{loc}}.
\tag{1.1}
\]

The second inclusion follows by summing the squared block estimates multiplied by \(2^{-2j\varepsilon}\). It does not identify either endpoint with the intersection of the lower Sobolev spaces.

Let \(\Lambda\subset T^*X\setminus0\) be a smooth closed conic Lagrangian. Denote by \(\mathcal J_\Lambda\) the properly supported operators in \(\Psi^1(X;E,E)\) whose order-one principal symbols vanish on \(\Lambda\). If a degree-one homogeneous principal representative \(l_1\) is used, this means \(l_1|_\Lambda=0\). More generally, for ordinary symbols the condition means that restriction of a full order-one symbol to \(\Lambda\) has order zero; this is unchanged by an order-zero change of representative. Every order-zero operator belongs to \(\mathcal J_\Lambda\).

**Definition 1.1.** A section \(u\in\mathcal D'(X;E)\) lies in \(I^m(X,\Lambda;E)\) if

\[
L_1\cdots L_Nu\in\mathcal B^{-m-n/4}(X;E)
\quad\text{for every }N\geq0
\text{ and every }L_j\in\mathcal J_\Lambda.
\tag{1.2}
\]

The case \(N=0\) is part of the definition. The constants may depend on the chosen operators and localized compact set. Equation (1.2) requires membership for each finite word; it does not assert one uniform bound for words of all lengths.

The definition is invariant under charts and bundle frames because the imported operator calculus preserves principal symbols and the local Besov scale. Taking \(E\) to be the half-density bundle gives the half-density version used in the preceding lesson. Locally, the smooth nonzero frame \(|dx|^{1/2}\) leaves the displayed estimates unchanged.

## 2. Localization and matrix-valued tests

**Theorem 2.1.** The intrinsic class has the following properties.

1. \(\operatorname{WF}(u)\subset\Lambda\) for \(u\in I^m(X,\Lambda;E)\).
2. A properly supported \(A\in\Psi^0(X;E,E)\) takes \(I^m\) to itself.
3. Conversely, if for every nonzero covector \(\gamma\) there is such an \(A\), elliptic at \(\gamma\), with \(Au\in I^m\), then \(u\in I^m\).

**Proof.** For the first assertion, fix \(\gamma\notin\Lambda\). Choose a scalar homogeneous cutoff \(q\), supported in a cone disjoint from \(\Lambda\), equal to one near \(\gamma\). An operator with principal symbol \(q(x,\xi)|\xi|I_E\) belongs to \(\mathcal J_\Lambda\) and is elliptic near \(\gamma\). Its \(N\)-th power has order \(N\), is elliptic there, and sends \(u\) into \(\mathcal B^s\), where \(s=-m-n/4\). By (1.1) and a conic parametrix, \(u\) has microlocal Sobolev regularity \(s+N-\varepsilon\). Letting \(N\) increase proves that \(\gamma\) is absent from the wavefront set.

For the second assertion, the order-one principal symbol of \([L,A]\) is \([l_1,a_0]\). It vanishes on \(\Lambda\), since \(l_1\) does. Thus \([L,A]\in\mathcal J_\Lambda\), even for matrices. Repeatedly moving \(A\) to the left gives the exact finite identity

\[
L_1\cdots L_N Au
=A L_1\cdots L_Nu
+\sum_{j=1}^N
L_1\cdots L_{j-1}[L_j,A]L_{j+1}\cdots L_Nu.
\tag{2.1}
\]

The first term belongs to \(\mathcal B^s\) by order-zero mapping. Every summand is an admissible word of length \(N\) applied to \(u\). This proves the assertion. Matrix factors have remained in their original order. In the scalar case the commutator has order zero, which is a special case of the same argument.

For the converse, choose a proper conic parametrix \(B\in\Psi^0\) for the given \(A\) near \(\gamma\). The preceding assertion gives \(BAu\in I^m\), and \(u-BAu\) is microlocally smooth there. Consequently each fixed word \(L_1\cdots L_Nu\) is microlocally in \(\mathcal B^s\) at \(\gamma\).

This local conclusion gives the actual local Besov membership required in (1.2). To see it, fix an output compact set and the word. A finite cover of its cosphere supplies finitely many elliptic tests on which that word has the stated regularity. A conic partition and the order-zero calculus reconstruct its compact localization from those regular pieces, plus a smoothing remainder. Each piece is in \(\mathcal B^s\); a smooth compact remainder belongs to every such space. The finite sum is therefore in \(\mathcal B^s\). This proves (1.2). ∎

One may consequently work with a Lagrangian defined only in an open cotangent cone. Membership at a point means that a properly supported order-zero cutoff, elliptic there and with sufficiently small microsupport in that cone, produces a section satisfying (1.2) for the local Lagrangian. The parametrix argument proves independence of the test cutoff. Smooth remainders do not affect this definition.

## 3. A frequency graph turns tests into derivatives

Base coordinates can be chosen so that, near a given point,

\[
\Lambda=\{(H'(\xi),\xi):\xi\ne0\},
\tag{3.1}
\]

with \(H\) real, smooth and homogeneous of degree one. For the next theorem take such an \(H\) on all directions of \(\mathbb R^n\setminus0\). The conic local version follows by extending \(H\) from a smaller angular cone and using Theorem 2.1. Extend \(H\) smoothly through low frequencies when an inverse Fourier transform is written; the resulting change has a smooth inverse transform.

**Theorem 3.1 (frequency-graph criterion).** If \(u\) is compactly supported, then

\[
u\in I^m(\mathbb R^n,\Lambda;\mathbb C^d)
\quad\Longleftrightarrow\quad
v(\xi)=e^{iH(\xi)}\widehat u(\xi)
\in S^{m-n/4},\qquad |\xi|>1.
\tag{3.2}
\]

Conversely, the inverse Fourier transform of \(e^{-iH}v\), for any \(v\in S^{m-n/4}\), belongs locally to this intrinsic class, without a compact-support assertion for that inverse transform.

**Proof of the forward implication.** Proper support must be kept when choosing test operators. We first replace \(H\), modulo a rapidly decreasing symbol, by a real \(h\in S^1\) whose inverse Fourier transform has compact support. Let \(H_0\) equal \(H\) above frequency two and be smooth everywhere. Its inverse Fourier transform \(K\) is smooth away from zero, and all its derivatives decrease rapidly outside any fixed neighborhood of zero. Indeed, repeated frequency integrations by parts differentiate the ordinary symbol until it is integrable, and give arbitrary spatial decay. Choose a real even compact cutoff \(\kappa\), equal to one near zero, and set \(h=\mathcal F(\kappa K)\). The removed function \((1-\kappa)K\) is Schwartz. Thus \(h-H_0\in S^{-\infty}\); the symmetry of \(K\) makes \(h\) real.

Set \(h_j=\partial_{\xi_j}h\) and

\[
Q_j=x_j-h_j(D).
\tag{3.3}
\]

The convolution kernel of \(h_j(D)\) has compact support, so \(Q_j\) is properly supported. It is locally order zero. Each \(Q_jD_k\) is a first-order admissible operator, because its principal symbol is \((x_j-H_j(\xi))\xi_k I_d\). Also

\[
[Q_j,Q_k]=0,\qquad [Q_j,D_k]=i\delta_{jk}I_d.
\tag{3.4}
\]

The first identity uses symmetry of the Hessian of \(h\). By reordering with the second identity, \(D^\beta Q^\alpha\), for \(|\alpha|=|\beta|=k\), is a finite linear combination of products of at most \(k\) operators \(Q_jD_l\), including the empty product. An induction pairs one derivative with one \(Q\); every commutation term removes that pair and leaves the same equality of the two remaining counts. Definition (1.2) therefore gives

\[
D^\beta Q^\alpha u\in B^{-m-n/4}_{2,\infty}.
\tag{3.5}
\]

These outputs have compact support, because \(u\) does and the operators are proper. Hence their local Besov membership is global membership.

With \(v_h=e^{ih}\widehat u\), Fourier transformation gives the exact gauge identity

\[
\widehat{Q^\alpha u}
=e^{-ih}i^{|\alpha|}\partial_\xi^\alpha v_h.
\tag{3.6}
\]

Applying the dyadic bound in (3.5), summing over all \(\beta\) of length \(k\), and using \(\sum_{|\beta|=k}|\xi^\beta|^2\asymp|\xi|^{2k}\), gives, on any fixed enlarged annulus,

\[
\int_{R/2<|\xi|<2R}|\partial_\xi^\alpha v_h|^2\,d\xi
\leq C_\alpha R^{2(m+n/4)-2|\alpha|},\qquad R\geq2.
\tag{3.7}
\]

Put \(r=m-n/4\) and \(v_R(\eta)=R^{-r}v_h(R\eta)\). A change of variables turns (3.7) into uniform \(L^2\) bounds for every derivative of \(v_R\) on a fixed annulus. The local frequency Sobolev estimate from the prerequisites now bounds every derivative uniformly on a smaller annulus. Rescaling gives

\[
|\partial_\xi^\alpha v_h(\xi)|
\leq C_\alpha\langle\xi\rangle^{r-|\alpha|}.
\tag{3.8}
\]

Since \(H-h\) is rapidly decreasing at high frequency, multiplication by \(e^{i(H-h)}\) preserves these bounds. This proves the forward implication for \(v\).

**Proof of the converse.** Let \(w=\mathcal F^{-1}(e^{-iH}v)\), \(v\in S^r\). Compactly localizing in \(x\) gives an oscillatory amplitude of order \(r\) with phase \(x\cdot\xi-H(\xi)\). The Fourier reduction of the preceding lesson, with \(N=n\), says that every such compact localization again has the form \(\widehat w=e^{-iH}v_0\), with \(v_0\in S^r\). Constants in the normalization do not change symbol membership.

We show that any admissible first-order \(L\) preserves this local class. Properness allows a compact input cutoff for any output compact set; the omitted input contributes a smooth output. In left quantization the localized input has amplitude \(p(x,\xi)v_0(\xi)\). The vanishing condition and the fundamental theorem of calculus give, on the working base set,

\[
p(x,\xi)=p_0(x,\xi)
+\sum_{j=1}^n (x_j-H_j(\xi))b_j(x,\xi),
\quad p_0\in S^0,\quad b_j\in S^1.
\tag{3.9}
\]

For example, \(b_j\) is the integral of \(\partial_{x_j}p\) on the straight segment from \(H'(\xi)\) to \(x\). Extend the localized symbol over that segment first. Derivatives of \(H'\) lose one frequency order, so the chain rule gives precisely \(S^1\) bounds for \(b_j\). The value \(p(H'(\xi),\xi)\) is order zero by the principal vanishing condition and supplies \(p_0\).

For the phase \(\Phi=x\cdot\xi-H(\xi)\),

\[
(x_j-H_j(\xi))e^{i\Phi}
=\frac1i\partial_{\xi_j}e^{i\Phi}.
\]

Integrating by parts converts the amplitude in (3.9) to

\[
p_0v_0+i\sum_j\partial_{\xi_j}(b_jv_0),
\tag{3.10}
\]

which is an ordinary amplitude of order \(r\). All identities hold as oscillatory integrals by frequency cutoffs and the defining integration-by-parts estimate. After a compact output cutoff, Fourier reduction again gives a reduced symbol of order \(r\). Thus the same argument can be repeated for every finite admissible word. It works componentwise for vectors and with matrix coefficients in their stated order.

A compact output with reduced symbol in \(S^r\) satisfies

\[
\int_{R/2<|\xi|<2R}|\widehat w(\xi)|^2\,d\xi
\leq C R^{2r+n}=C R^{2(m+n/4)}.
\tag{3.11}
\]

This is its \(B^{-m-n/4}_{2,\infty}\) bound. Low frequencies are harmless for a compact distribution, and smooth localized outputs have every Besov order. Hence every word satisfies (1.2). This proves the converse and the noncompact local assertion. ∎

In particular,

\[
\bigcap_{m\in\mathbb R}I^m(X,\Lambda;E)=C^\infty(X;E).
\tag{3.12}
\]

Locally, the intersection makes the reduced symbol rapidly decreasing, and Fourier inversion gives smoothness. A smooth section satisfies every localized word estimate, proving the reverse inclusion.

## 4. Every local phase gives the intrinsic class

The order in the preceding lesson can now be interpreted intrinsically. Suppose \(\phi(x,\theta)\) is a nondegenerate phase with \(N\) variables parametrizing a small part of \(\Lambda\). Then

\[
(2\pi)^{-(n+2N)/4}
\int e^{i\phi(x,\theta)}a(x,\theta)\,d\theta
\in I^m(X,\Lambda)
\quad\text{if }a\in S^{m+(n-2N)/4}
\tag{4.1}
\]

and the amplitude is supported inside a sufficiently small compact-base cone. For a clean phase of excess \(e\), the corresponding statement is

\[
(2\pi)^{-(n+2N-2e)/4}
\int e^{i\phi(x,\theta)}a(x,\theta)\,d\theta
\in I^m(X,\Lambda),
\qquad a\in S^{m+(n-2N-2e)/4}.
\tag{4.2}
\]

Both assertions follow from the Fourier-symbol reduction and Theorem 3.1, after the base change making \(\Lambda\) a frequency graph. Theorem 2.1 and coordinate invariance then remove that choice.

The extension of amplitudes uses the following symbol fact, also useful for changing the number of base or phase variables.

**Lemma 4.1 (homogeneous pullback).** Let \(\Gamma_j\subset\mathbb R^{n_j}\times(\mathbb R^{N_j}\setminus0)\) be open cones, and let \(F:\Gamma_1\to\Gamma_2\) be smooth and proper. Suppose
\[
F(x,t\theta)=(y,t\eta)\quad\text{whenever }F(x,\theta)=(y,\eta),\quad t>0.
\]
If \(a\in S^q\) has its support inside a cone whose normalized base and frequency directions form a compact subset of \(\Gamma_2\), then \(a\circ F\), extended by zero outside \(\Gamma_1\), is in \(S^q\). Here its closed ambient support is contained in \(\Gamma_2\); in particular it is separated from zero frequency on the compact base set.

**Proof.** Intersect the supporting cone with \(|\eta|=1\); this is a compact subset of \(\Gamma_2\). Its inverse image is compact by properness. On this inverse image the input frequency radius is bounded above and below by positive constants, and the input base points range over a compact set. Dilation therefore gives \(|\theta|\asymp|\eta|\) wherever \(a\circ F\) can be nonzero, with input directions in a fixed interior compact set.

On a fixed normalized input annulus, all derivatives of \(F\) are bounded. The functions \((y,\eta)\mapsto a(y,t\eta)\) and every fixed derivative in these normalized variables are bounded by \(C t^q\), for \(t\geq1\) and \(|\eta|\) in the fixed comparison annulus. The chain rule and homogeneity give the same bounds for \(a(F(x,t\theta))\) differentiated in normalized \((x,\theta)\). Returning to physical frequency derivatives divides by \(t\) for each frequency derivative and gives the \(S^q\) estimates. Bounded frequencies are covered by smoothness on the compact inverse image. Its normalized support lies strictly inside \(\Gamma_1\), so zero extension is smooth and satisfies the same estimates. ∎

**Theorem 4.2 (local converse for a prescribed phase).** Every section of \(I^m\), microlocally supported in a sufficiently small part of the Lagrangian parametrized by \(\phi\), has a representation (4.1), or (4.2) for a clean phase, modulo a smooth section. This holds in any fixed local bundle frame.

**Proof for a nondegenerate phase.** Use Theorem 3.1 to write the reduced Fourier symbol as \(v\in S^r\), \(r=m-n/4\), supported in a small angular cone modulo a rapidly decreasing symbol. At the phase-critical point mapping to \(\xi\), let \(G\) be the invertible full Hessian in \((x,\theta)\) used in Fourier reduction. Its signature is constant after shrinking the working cone. The leading reduction map is

\[
a\longmapsto(2\pi)^{n/4}
e^{i\pi\operatorname{sgn}G/4}
\frac{a|_{C_\phi}}{|\det G|^{1/2}}.
\tag{4.3}
\]

Choose an amplitude whose restriction to \(C_\phi\) is

\[
a_0|_{C_\phi}=(2\pi)^{-n/4}
e^{-i\pi\operatorname{sgn}G/4}
|\det G|^{1/2}v(\phi_x').
\tag{4.4}
\]

Homogeneous coordinates on a neighborhood of the critical set extend this to an ordinary symbol supported in the chosen compact-base cone. More explicitly, normalize the frequency radius, extend smoothly in transverse coordinates on the resulting compact set, then restore the homogeneous determinant factor and the symbol argument. The chain rule preserves the order. Since \(|\det G|^{1/2}\) has degree \((n-N)/2\), that order is

\[
r+(n-N)/2=m+(n-2N)/4.
\]

The full stationary-phase expansion makes the reduced symbol of \(a_0\) equal to \(v\) modulo \(S^{r-1}\). Apply (4.4) to that residual, obtaining \(a_1\) of one lower order. Inductively obtain \(a_j\) of order \(m+(n-2N)/4-j\), with the residual after \(j\) corrections one order lower again.

All amplitudes can have their support in one common compact-base cone: choose nested cutoffs equal to one near the smaller critical directions carrying \(v\). Residuals outside those directions are rapidly decreasing by nonstationarity and may be discarded. The imported support-preserving asymptotic summation gives \(a\sim\sum_j a_j\). Fourier reduction has remainder estimates in each lower symbol order, so its reduced symbol differs from \(v\) by \(S^{-\infty}\). Inverse Fourier transformation makes the distributional error smooth. This proves (4.1) modulo a smooth section.

**Proof for a clean phase.** On the critical set choose local fiber variables \(t=\theta''/|\xi|\), of dimension \(e\). They parametrize a small compact portion of each fiber \(C_\xi\). Let \(w(t)\) be smooth, compactly supported in this portion, with \(\int w(t)\,dt=1\). In physical fiber variables set

\[
b(\xi,\theta'')=|\xi|^{-e}w(\theta''/|\xi|),
\qquad\int b(\xi,\theta'')\,d\theta''=1.
\tag{4.5}
\]

Local fiber charts are obtained from a degree-zero transverse slice and dilation, so this formula is smooth in \(\xi\) on the cone. Let \(G'\) be the reduced normal Hessian. Choose the critical restriction

\[
a_0|_{C_\phi}=(2\pi)^{-n/4}
e^{-i\pi\operatorname{sgn}G'/4}
|\det G'|^{1/2}v(\xi)b(\xi,\theta''),
\qquad \xi=\phi_x'.
\tag{4.6}
\]

The leading fiber integral in Fourier reduction is then exactly \(v\). The determinant factor has degree \((n-N+e)/2\), while \(b\) has degree \(-e\). Thus the amplitude order is

\[
r+(n-N+e)/2-e=m+(n-2N-2e)/4.
\]

Extend off the critical set in homogeneous coordinates as before. The smooth compact fiber support keeps all parameter estimates uniform. Correct residuals successively with this same right inverse of the leading fiber integral and asymptotically sum. The full clean expansion again makes the remaining error rapidly decreasing. This proves (4.2) modulo a smooth section. ∎

This theorem identifies the distributional class for all local parametrizing phases. It does not yet identify their principal amplitudes as sections of a globally patched density and Maslov bundle; that requires tracking the transition factors between phases.

## 5. Sobolev information improves the symbol order

**Theorem 5.1.** Suppose \(u\in I^m(X,\Lambda;E)\) and \(u\) is microlocally in \(H^{s_0}\) at \(\gamma\in\Lambda\). Then

\[
u\in I^\mu\text{ at }\gamma
\quad\text{for every }\mu+s_0+n/4>0.
\tag{5.1}
\]

The inequality is strict. No conclusion at \(\mu=-s_0-n/4\) is made.

**Proof.** Choose a proper order-zero cutoff elliptic at \(\gamma\) so its output is compactly supported in a chart, has wavefront in a small cone, and belongs to \(H^{s_0}\). Theorem 2.1 preserves its intrinsic class. Change base coordinates to the frequency graph and use Theorem 3.1. Smooth errors and the portions outside a slightly larger frequency cone are harmless. With \(r=m-n/4\), put

\[
v_R(\eta)=R^{-r}v(R\eta),\qquad
t=s_0+m+n/4.
\]

The symbol estimates give uniformly bounded derivatives of \(v_R\) on each fixed annulus. The Sobolev hypothesis and \(|e^{-iH}|=1\) give

\[
\|v_R\|_{L^2(\text{annulus})}\leq C R^{-t}.
\tag{5.2}
\]

If \(t\leq0\), condition (5.1) implies \(\mu>m\), so symbol inclusion already proves the result. Assume \(t>0\).

Multiply \(v_R\) by a fixed smooth annular cutoff, equal to one on the region under examination, and call the result \(F_R\). It has \(L^2\) norm at most \(CR^{-t}\), and every fixed derivative has bounded \(L^2\) norm. For an integer \(K>|\beta|+n/2\), Fourier inversion in the \(\eta\) variable, split at a radius \(T\geq1\), gives

\[
|\partial^\beta F_R(\eta)|
\leq C_{\beta,K}\left(
T^{|\beta|+n/2}\|F_R\|_2
+T^{|\beta|+n/2-K}
\sum_{|\alpha|=K}\|\partial^\alpha F_R\|_2\right).
\tag{5.3}
\]

For the low-frequency part, Cauchy–Schwarz integrates \(|\zeta|^{2|\beta|}\) over the ball. For the tail, insert \(|\zeta|^K\widehat F_R\) and integrate \(|\zeta|^{2|\beta|-2K}\) outside the ball; its integral converges by the choice of \(K\). Plancherel bounds the weighted transform by the displayed derivative norms. This proves (5.3).

Taking \(T=R^{t/K}\) yields

\[
|\partial^\beta v_R|
\leq C R^{-t+t(|\beta|+n/2)/K}.
\]

Given any \(\varepsilon>0\), choose \(K\) large enough for the last positive exponent to be less than \(\varepsilon\). Rescaling gives

\[
|\partial_\xi^\beta v(\xi)|
\leq C_{\beta,\varepsilon}
\langle\xi\rangle^{-s_0-n/2-|\beta|+\varepsilon}.
\tag{5.4}
\]

For a fixed \(\mu\) satisfying (5.1), choose \(\varepsilon<\mu+s_0+n/4\). The bounds for every \(\beta\) place \(v\) in \(S^{\mu-n/4}\). Theorem 3.1 proves the desired intrinsic membership, and localization returns it to \(\gamma\). ∎

## 6. Examples and exercises with complete solutions

**The point mass.** On \(\mathbb R^n\), take \(H=0\). The graph is \(T^*_0\mathbb R^n\setminus0\), and \(\widehat{\delta_0}=1\). Theorem 3.1 gives \(\delta_0\in I^{n/4}\). It is not in any smaller order because a nonzero constant is not a negative-order symbol. Its limiting Besov regularity is \(-n/2\), while its Sobolev regularity is strictly below \(-n/2\).

**Exercise 6.1 (the dimension shift; introductory).** If \(v(\xi)=\langle\xi\rangle^r\), what is the intrinsic order of \(\mathcal F^{-1}(e^{-iH}v)\)? What regularity bound follows immediately?

**Solution.** The order is \(m=r+n/4\). The dyadic integral of \(|v|^2\) is bounded by \(CR^{2r+n}\); its endpoint is \(B^{-r-n/2}_{2,\infty}\). Hence every localized admissible word has this Besov order, and has Sobolev order \(-r-n/2-\varepsilon\) for every positive \(\varepsilon\). The phase factor has modulus one, but spatial localization and all iterated tests are justified by the converse proof, rather than just that modulus calculation.

**Exercise 6.2 (matrix commutators; intermediate).** On \(\mathbb R\), let \(\Lambda=T^*_0\mathbb R\setminus0\), \(L=xMD_x\), and let \(A=N\) be a constant order-zero matrix. Choose \(M,N\) so that \([L,A]\) has order one. Why does Theorem 2.1 still apply?

**Solution.** Take \(M=\begin{pmatrix}1&0\\0&0\end{pmatrix}\) and \(N=\begin{pmatrix}0&1\\0&0\end{pmatrix}\). Then \([M,N]=N\) and \([L,A]=xND_x\), an operator of order one. Its principal symbol \(xN\xi\) vanishes on \(x=0\), so it is itself admissible. Identity (2.1) therefore consists only of allowed words and the order-zero image of an allowed word. There is no scalar commutator assumption.

**Exercise 6.3 (why two counts agree; intermediate).** In one dimension, show that \(D Q=Q D-i\), and express \(D^2Q^2\) as a polynomial in \(QD\), using \([Q,D]=i\).

**Solution.** The first identity is immediate. Put \(T=QD\). Then \(Q^2D^2=T^2+iT\), since \(T^2=Q(DQ)D=Q^2D^2-iQD\). Also \(D^2Q^2=Q^2D^2-4iQD-2\), by commuting both derivatives through both \(Q\)'s. Consequently \(D^2Q^2=T^2-3iT-2\). Each term is a word in the first-order admissible operator \(T\), or the empty word. The same pair-removal mechanism proves the multi-index assertion in (3.5).

**Exercise 6.4 (a clean right inverse; intermediate).** For the redundant phase \(\phi(x,\theta_1,\theta_2)=x\theta_1\) in dimension one, restricted to \(\theta_1>0\) and \(|\theta_2|<c\theta_1\), compute the amplitude order required for excess one. Construct a leading amplitude whose fiber reduction is a prescribed \(v(\xi)\in S^{m-1/4}\), \(\xi>0\).

**Solution.** Here \(n=1,N=2,e=1\), so the amplitude order is \(m-5/4\). The normal Hessian in \((x,\theta_1)\) is \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\), with determinant \(-1\) and signature zero. For \(w\in C_c^\infty((-c,c))\), \(\int w=1\), take on the critical set
\[
a_0=(2\pi)^{-1/4}v(\theta_1)\theta_1^{-1}
w(\theta_2/\theta_1).
\]
Its order is \(m-1/4-1=m-5/4\), and \((2\pi)^{1/4}\int a_0\,d\theta_2=v(\theta_1)\). A base cutoff equal to one at zero extends the amplitude. The normalized factor in (4.2) is \((2\pi)^{-3/4}\), so integrating out \(\theta_2\) gives the inverse Fourier coefficient \((2\pi)^{-1}\), as required.

**Exercise 6.5 (the strict inequality; advanced).** Construct a symbol \(v\) such that \(\mathcal F^{-1}v\in H^{s_0}\) and \(v\in S^{-s_0-n/2+\varepsilon}\) for every \(\varepsilon>0\), but \(v\notin S^{-s_0-n/2}\). Explain why this prevents replacing the strict inequality in Theorem 5.1 by equality.

**Solution.** Let \(q=-s_0-n/2\), choose a nonzero smooth bump \(b\), supported in the unit ball with \(b(0)=1\), and choose \(a>3/n\). For sufficiently large integers \(j\), set \(R_j=2^{j^2}\), \(\xi_j=R_je_1\), and define disjoint bumps
\[
v(\xi)=\sum_j R_j^q j\,
b\left(\frac{j^a(\xi-\xi_j)}{R_j}\right).
\tag{6.1}
\]
Their widths are \(R_j/j^a\), much smaller than \(R_j\), and the series is locally finite. A derivative of order \(k\) is bounded on the \(j\)-th bump by \(C_kR_j^{q-k}j^{1+ak}\). For each fixed \(k\) and \(\varepsilon>0\), the polynomial in \(j\) is bounded by \(C_{k,\varepsilon}R_j^\varepsilon\). Thus all ordinary symbol estimates of order \(q+\varepsilon\) hold. At the centers, \(R_j^{-q}v(\xi_j)=j\), so the order-\(q\) estimate fails.

The weighted Fourier energy of the \(j\)-th bump is bounded by a constant times
\[
R_j^{2s_0}R_j^{2q}j^2(R_j/j^a)^n=j^{2-an}.
\]
The series converges because \(an>3\). Plancherel gives \(\mathcal F^{-1}v\in H^{s_0}\).

For \(H=0\), Theorem 3.1 gives membership in \(I^{-s_0-n/4+\varepsilon}\) for every \(\varepsilon>0\). To locate the failure, multiply the inverse transform by a compact cutoff \(\chi\), equal to one near zero. Fourier reduction for the phase \(x\cdot\xi\) gives
\[
\widehat{\chi\mathcal F^{-1}v}-v\in S^{q+\varepsilon-1}.
\]
Choose \(0<\varepsilon<1\). That remainder is of strictly lower order than \(q\) and cannot cancel the values \(R_j^q j\) at the centers. The compact localization is therefore not in \(I^{-s_0-n/4}\) by Theorem 3.1. Its singular directions lie on the cotangent fiber at zero; thus the asserted endpoint improvement would fail there. Multiplication preserves its \(H^{s_0}\) membership. This proves the need for the strict range.

## References

- [Hörmander IV, §25.1] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, Springer, 1985, §25.1.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Original text: public domain (CC0).*
