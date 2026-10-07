# Intrinsic conormal symbols and complete operator action

This modified component retains Sections 6–7 of AN03-U008, *Singularities along a submanifold and smooth boundary passage*. The exact amplitude characterization and complete Sections 1–5 are already present in the [conormal test companion](../20261005-conormal-test-foundations/conormal-amplitudes-and-test-spaces.md). The present component supplies the coordinate and half-density law, symbol quotient, full ordered operator action and every finite remainder.

Principal author entity: AN-03 course-writing task, 2026. The AN-03 course-writing task and OpenAI Codex are responsible for the renewed edition. Current proof connections and clarifications: AN-04 course-writing task and OpenAI Codex, 5 October 2026; publisher: AN-04 local course project.

Original text: CC0.

## Exact prerequisites and scope

Use \(D=-i\partial\), the forward exponential \(e^{-ix\cdot\xi}\), and inverse coefficient \((2\pi)^{-n}\). In dimension \(n\), a conormal distribution of order \(m\) along a submanifold of codimension \(k\) has reduced amplitude order \(m+(n-2k)/4\). Equations (C1)–(C17), their Besov endpoints, coordinate/tangent characterization and every normal-reduction remainder are the complete proofs in the preceding companion. The normal-frequency statements below have \(1\le k\le n\). At codimension zero the tangent characterization gives smooth functions, the successive conormal quotients are zero, and there is no nonzero normal covector; no oscillatory normal reduction is needed.

Local statements are made in embedded submanifold charts. The global quotient (C21) uses a closed embedded submanifold, as in the diagonal and boundary-corner applications. On a larger space where the chosen submanifold is not closed, apply the statement on an open neighborhood where it is closed. This is the precise setting in which the locally finite global realization below is asserted.

The [complete quadratic multiplier estimates](../20261004-free-intrinsic-graph/prerequisites/gauss-transform-estimates.md) and [ordinary operator calculus](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md) give the distributional Gauss maps, passive-variable bounds, compact approximation and all finite remainders. The negative phase in (C5) is the explicit reflected phase already justified in the conormal test companion. The [locally finite partition proof PS5](../20261004-free-intrinsic-graph/prerequisites/global-principal-symbol.md) supplies actual chart cutoffs. The [Fourier](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md) and [measure](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) proofs supply Plancherel, Fubini and dominated convergence. The approved mathematical antecedent is Hörmander III, 2007 eBook, ISBN 978-3-540-49938-1; its use and ordinary citation are valid.

## 6. The intrinsic principal symbol and its normalization

Factor out an ambient half-density and write a local conormal section as
\[
u(t,z)=(2\pi)^{-(n+2k)/4}
\int e^{it\cdot\tau}a(z,\tau)d\tau\,|dt\,dz|^{1/2},
\qquad a\in S^{m+(n-2k)/4}.
\tag{C18}
\]
Its leading symbol is the class of
\(a(z,\tau)|dz|^{1/2}|d\tau|^{1/2}\), modulo one lower ordinary amplitude order, on the chart \((z,\tau)\mapsto(0,z;\tau,0)\) of \(N^*Y\).

We check the full coordinate law. Let \(\kappa=(\kappa_1,\kappa_2)\) preserve \(t=0\), and pull back the ambient half-density. Formula (C14) gives \(\kappa_1(t,z)=\Psi(t,z)t\), with \(\Psi(0,z)=\kappa'_{11}(0,z)\) invertible. Near the submanifold shrink the chart so that \(\Psi\) is invertible; away from it the distribution is smooth. Changing the integration variable to \(\tau=\Psi(t,z)^T\theta\) gives the full amplitude
\[
A(t,z,\tau)=a_\kappa(\kappa_2(t,z),\Psi(t,z)^{-T}\tau)
\frac{|\det\kappa'(t,z)|^{1/2}}{|\det\Psi(t,z)|}.
\tag{C19}
\]
Every base derivative of the composed symbol introduces a factor linear in \(\tau\) paired with a frequency derivative, so (C1) retains its order on compact coordinate sets. Frequency derivatives lower the order normally. Choose the compact base cutoff \(\chi\) of Section 2 equal to one on the working neighborhood and extend \(\chi A\) by zero. Reducing this global symbol by (C5) gives the exact amplitude
\(a=[e^{-i\langle D_t,D_\tau\rangle}(\chi A)]_{t=0}\) of the localized pullback. Its inverse integral agrees with the original pullback on that neighborhood, and all \(N\)-term remainders have order \(m+(n-2k)/4-N\). At the working points of \(Y\), the cutoff and all its derivatives in the expansion are respectively one and zero.

The zeroth term is
\[
a_\kappa\big(\kappa_2(0,z),\kappa'_{11}(0,z)^{-T}\tau\big)
|\det\kappa'_{11}(0,z)|^{-1/2}
|\det\kappa'_{22}(0,z)|^{1/2}.
\tag{C20}
\]
Indeed, the off-diagonal block \(\kappa'_{12}(0,z)\) vanishes, so the full determinant is the product of the two diagonal block determinants. The factor in (C20) is exactly the half-density Jacobian on \((z,\tau)\). This proves intrinsic invariance modulo one lower order, including its exact determinant powers. A bundle transition matrix contributes its value on \(Y\); every additional normal derivative of that matrix in the reduction is paired with a frequency derivative and therefore contributes only to lower orders.

On a real rank-\(k\) vector bundle \(V\to Y\), define \(S^\nu(V;\Omega_V^{1/2})\) by requiring the coefficient of \(|dz|^{1/2}|d\tau|^{1/2}\) to have ordinary order \(\nu-k/2\). Fiber dilation multiplies that coordinate half-density by the factor \(t^{k/2}\); hence its intrinsic homogeneous degree includes \(k/2\). Base/fiber changes obey the same determinant calculation and preserve these estimates. In (C18) the intrinsic symbol order is consequently \(m+n/4\), independent of codimension.

Let \(\widehat E\) be the pullback of \(E|_Y\) to \(N^*Y\). The construction gives an isomorphism
\[
\frac{I^m(X,Y;\Omega_X^{1/2}\otimes E)}{I^{m-1}(X,Y;\Omega_X^{1/2}\otimes E)}
\simeq
\frac{S^{m+n/4}(N^*Y;\Omega_{N^*Y}^{1/2}\otimes\widehat E)}
{S^{m+n/4-1}(N^*Y;\Omega_{N^*Y}^{1/2}\otimes\widehat E)}.
\tag{C21}
\]
For clarity, use the actual partition construction as follows.
Choose a locally finite family of relatively compact submanifold charts
whose smaller charts cover \(Y\), and a subordinate smooth partition
\(\lambda_i\) on \(Y\). Extend each \(\lambda_i\) to its ambient chart,
constant in the normal variable near zero, and multiply by a compact
normal cutoff equal to one on that smaller chart. The neighborhoods
can be chosen locally finite in \(X\): apply PS5 to a neighborhood
cover adapted to the closed subset \(Y\) and its complement. A compact
set then meets only finitely many chosen supports. Quantize each
localized symbol by (C18) and multiply by the ambient cutoff. Its
leading class is \(\lambda_i\) times the specified one; every derivative
on a normal cutoff contributes only a lower-order term by (C5).
The distributional sum is locally finite and has the prescribed
leading class because \(\sum_i\lambda_i=1\) on \(Y\). The same local
estimates prove continuity in every fixed compact conormal seminorm.

Surjectivity follows by realizing local amplitudes in (C18), multiplying by cutoffs in the ambient chart, and summing a locally finite partition on \(Y\). Formula (C20) makes the resulting principal symbol the prescribed one. To identify the kernel, localize compactly in a chart. The reduced amplitude is its partial Fourier transform in the normal variables, with the fixed factor in (C18), so it is unique. By the normal-form equivalence, the localized distribution belongs to \(I^{m-1}\) exactly when this amplitude has one lower order. This proves injectivity and the kernel assertion; changes off \(Y\) contribute smooth terms only.

The normalization can be checked in two ways. Before introducing (C18), put \(r=m+(n-2k)/4\) in (C8); then the power of \(R\) is \(2\operatorname{Re}m+n/2\), and with the factor \((2\pi)^{-n}\) on the energy side the limit is \((2\pi)^k\int|a_0|^2\varphi(\theta,0)\). Inserting the coefficient in (C18) multiplies that limit by \((2\pi)^{-(n+2k)/2}\). Thus the normalized amplitude has the equivalent limit with coefficient \((2\pi)^{-n/2}\) on the Fourier-energy side and coefficient one on the amplitude side.

For a pseudodifferential kernel on a \(d\)-manifold, the ambient dimension is \(n=2d\) and the diagonal codimension is \(k=d\). Formula (C18) becomes the usual \((2\pi)^{-d}\) kernel normalization, and the amplitude order is the operator order. Under \(N^*\Delta\simeq T^*X\), the cotangent symplectic density supplies \(|dx|^{1/2}|d\xi|^{1/2}\), of fiber degree \(d/2=n/4\). Multiplying the ordinary operator symbol by it gives (C21). A general conormal bundle has no such specified canonical half-density that would turn its symbols into scalar functions.

## 7. Full action on amplitudes, not only leading symbols

Let \(P=p(x,D)\) have left symbol of order \(d\), and let \(u\) have the normalized reduced amplitude \(a(z,\tau)\) of (C18), of order \(r=m+(n-2k)/4\). Work first with compact input and output localization in one chart: the exact left symbol \(p\) is extended globally with compact base support, and \(a\) is the global reduced amplitude of the compactly localized input from Section 2. Thus both factors have global symbol bounds. The output amplitude of this localized operator and input is
\[
b(z,\tau)=
\left[
\exp\big(i\langle D_w,D_\eta\rangle-i\langle D_t,D_\tau\rangle\big)
\{p(t,z,\tau,\eta)a(w,\tau)\}
\right]_{w=z,\ t=0,\ \eta=0}.
\tag{C22}
\]
The exponential means successive quadratic-multiplier restriction as below. Every truncation before total degree \(N\) has remainder in \(S^{d+r-N}\), with all base/frequency derivatives and finite-seminorm control. In particular
\[
\sigma(Pu)=\sigma(P)|_{N^*Y}\,\sigma(u).
\tag{C23}
\]

For Schwartz inputs, insert the Fourier transform of (C18) into the left quantization integral. Tangential Fourier inversion first gives the full amplitude
\[
a_1(t,z,\tau)=(2\pi)^{-(n-k)}
\iint e^{i(z-w)\cdot\eta}p(t,z,\tau,\eta)a(w,\tau)\,dw\,d\eta.
\]
This is the first quadratic multiplier in (C22), evaluated at \(w=z,\eta=0\). Its estimates follow directly from [the complete quadratic multiplier proof](../20261004-free-intrinsic-graph/prerequisites/gauss-transform-estimates.md), including the passive variables. On the space of \((x,w,\tau,\eta)\), use
\[
G=|dx|^2+|dw|^2+\langle\tau\rangle^{-2}|d\tau|^2
+\langle(\tau,\eta)\rangle^{-2}|d\eta|^2,
\quad M=\langle(\tau,\eta)\rangle^d\langle\tau\rangle^r.
\tag{C24}
\]
The product symbol obeys these derivative bounds: derivatives of \(p\) in \(\tau\) cost at most \(\langle\tau\rangle^{-1}\), and those of \(a\) have exactly that cost. Small metric displacements preserve both brackets, so slow variation and local weight comparison hold. For the phase \(\langle D_w,D_\eta\rangle\), a finite phase distance keeps \((x,\tau)\) fixed. Relative to an observation point with \(\eta=0\), the \(\eta\)-part of \(G\) at any input point is no larger, while the remaining parts agree. The weight ratio is bounded by a power of \(1+|\eta|^2\), which the phase-dual distance controls. Thus the full hypotheses of the Gauss restriction theorem hold uniformly along \(w=z,\eta=0\). When \(n-k>0\), the parameter is \(1/(2\langle\tau\rangle)\). When \(k=n\), there are no tangential variables: this first reduction is ordinary multiplication, its phase and actual Gauss parameter are zero, and the zero-phase branch of Section 8 of [the complete quadratic multiplier proof](../20261004-free-intrinsic-graph/prerequisites/gauss-transform-estimates.md) applies. It gives \(a_1\in S^{d+r}\) and every remainder order \(d+r-N\), including parameter derivatives.

Now remove the normal base dependence of \(a_1\) by (C5). This gives the second multiplier and (C22). The constant-coefficient differential operators commute before restriction. Expanding the two finite Taylor polynomials and collecting terms of total degree less than \(N\) gives the stated single exponential expansion; each contraction lowers the order by one, and the discarded finite terms and both controlled remainders have order at most \(d+r-N\).

For general symbols, take bounded compactly supported approximants. The oscillatory definition, the two weak Gauss extensions, and the Schwartz action of ordinary \(S_{1,0}\) operators and their adjoints pass the equality to distributions. Explicitly, adjoints applied to a fixed Schwartz test function converge in Schwartz space: the classical estimates from the complete Schwartz-action and bounded-approximation proofs in [the ordinary operator calculus](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md) bound all output seminorms uniformly, local smooth convergence follows by dominated oscillatory integration, and a higher uniform decay seminorm controls the tails. Pair this convergence with the bounded, distributionally convergent input approximants. For the original local operator, proper support permits a compact input cutoff equal to one at all kernel input points over a fixed output compact set. Use a compact output cutoff equal to one on its working neighborhood. Splitting into chart pieces near the diagonal then gives the globally extended symbols just used. The remaining kernel pieces are separated from the diagonal, so frequency integration by parts makes their outputs smooth there; after compact output localization their normal Fourier transforms are \(S^{-\infty}\) amplitudes and are included in the local representation. This gives equality on the working neighborhood and every claimed local remainder without imposing growth at infinity on the original symbols. All estimates are componentwise, and (C20) glues the leading term, proving (C23) for bundle operators.

If the amplitudes and operator symbols have complex polyhomogeneous expansions in steps \(h=1/q\), \(q\) a positive integer, every coordinate and action formula above preserves that expansion. A frequency derivative lowers degree by an integer, which is \(q\) steps; multiplying homogeneous components adds their step indices. At each specified degree only finitely many indices contribute, and the remainder estimates just proved justify truncation. A common reciprocal-integer step may be chosen for two different such expansions. The boundary theory below uses step one, with degrees \(m-j\); its phase formulas are not assertions for arbitrary noninteger steps.

