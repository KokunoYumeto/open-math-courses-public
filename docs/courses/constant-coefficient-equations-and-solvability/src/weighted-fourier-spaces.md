# Measuring regularity with weighted Fourier spaces

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A differential equation need not gain the same number of derivatives in every direction. The polynomial \(\xi_1^2+i\xi_2\), for example, grows quadratically in one variable and linearly in the other. A single isotropic Sobolev exponent hides that distinction. We develop spaces whose weights can follow the actual polynomial, while retaining multiplication by smooth cutoffs, completeness, and a useful duality.

Read [Fundamental solutions and the directions an equation uses](fundamental-solutions-and-active-directions.md) for the polynomial derivative norm. The analytic prerequisites are the Fourier transform on Schwartz functions and tempered distributions, Hölder's inequality, the \(L^1*L^p\) convolution inequality, and the duality of \(L^p\) for \(1\leq p<\infty\). The Fourier convention and its inverse are given in [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html#AN03-DEP-001). Grubb [Grubb] and Melrose [Melrose] give background on Fourier analysis. The locally convex and Lebesgue tools used here are proved in the internal lessons linked below.

[Lebesgue duality and the functionals on Fourier spaces](lebesgue-duality-and-fourier-functionals.md), Sections 1–3, proves the finite-exponent Lebesgue duality theorem, including its endpoint and exact norm. Its final section uses only the weighted isometry defined here to identify the Fourier representation. [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html), Sections 15.0–15.4, proves Hölder, completeness, Young and finite-exponent smooth approximation. [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html), Section 13.10, constructs the cutoffs.

## Weights that tolerate frequency shifts

A positive function \(k:\mathbb R^n\to(0,\infty)\) is a **moderate weight** in this lesson if there are constants \(C,N\geq0\) such that
\[
k(\xi+h)\leq(1+C|h|)^N k(\xi)
\qquad(\xi,h\in\mathbb R^n).
\]
The factor tends to one as \(h\to0\). This convention makes every such weight continuous without imposing a separate regularity assumption. Reversing the shift gives
\[
(1+C|h|)^{-N}\leq\frac{k(\xi+h)}{k(\xi)}
\leq(1+C|h|)^N.
\]
In particular both \(k\) and \(1/k\) have at most polynomial growth. Define
\[
M_k(h)=\sup_\xi\frac{k(\xi+h)}{k(\xi)}.
\]

**Lemma 1.1.** The function \(M_k\) is continuous, submultiplicative, and satisfies
\[
1\leq M_k(h)\leq(1+C|h|)^N,
\qquad M_k(h+l)\leq M_k(h)M_k(l).
\]
If \(k_1,k_2\) are moderate, so are their sum, product, pointwise maximum and pointwise minimum. Every real power of a moderate weight is moderate. Reflection \(k^\vee(\xi)=k(-\xi)\) preserves moderation.

**Proof.** Factor the ratio for a shift \(h+l\) through the point \(\xi+l\) to prove submultiplicativity. If \(M_k(h)<1\), iteration gives \(k(\xi+rh)\leq M_k(h)^r k(\xi)\) for positive integers \(r\), whereas the reverse moderate bound gives \(k(\xi+rh)\geq(1+Cr|h|)^{-N}k(\xi)\). An exponential decay cannot dominate that polynomial lower bound for every \(r\). Thus \(M_k(h)\geq1\). Finally
\[
M_k(h+l)\leq M_k(h)(1+C|l|)^N,
\qquad M_k(h)\leq M_k(h+l)(1+C|l|)^N
\]
prove continuity. For a sum, maximum or minimum, apply a common shift bound to the two terms before combining them. For a product multiply their bounds. Reciprocal weights obey the same bound by reversing the shift; positive powers then give all real powers. Reflection simply replaces \(h\) by \(-h\). \(\square\)

**Example 1.2.** The weights \(\langle\xi\rangle^s=(1+|\xi|^2)^{s/2}\), \(s\in\mathbb R\), are moderate because \(\langle\xi+h\rangle\leq(1+|h|)\langle\xi\rangle\). Products of these weights on separate groups of variables are moderate as well. Another example in one variable is \(k(\xi)=(1+\max(\xi,0))^s\), which need not be even.

**Proposition 1.3.** If \(P\ne0\) is a polynomial of degree at most \(m\), then the derivative norm \(S_P\) is a moderate weight, with constants depending only on \(m\) and the dimension.

**Proof.** Collect all derivatives \(\partial^\alpha P(\xi)\), \(|\alpha|\leq m\), in one vector \(J(\xi)\). Differentiation of this vector in any coordinate shifts its entries to derivatives of higher order, with derivatives of order above \(m\) interpreted as zero. Denote those fixed commuting shift matrices by \(T_j\). Their joint products of total degree greater than \(m\) vanish. Taylor's formula is therefore the finite identity
\[
J(\xi+h)=\sum_{r=0}^m\frac{(\sum_jh_jT_j)^r}{r!}J(\xi).
\]
Choose \(A\) depending only on the matrices so that \(\|\sum h_jT_j\|\leq A|h|\). Since \(1/r!\leq\binom mr\) for \(0\leq r\leq m\),
\[
|J(\xi+h)|\leq\sum_{r=0}^m\frac{(A|h|)^r}{r!}|J(\xi)|
\leq(1+A|h|)^m|J(\xi)|.
\]
The norm of \(J\) is exactly \(S_P\). Positivity was proved in the preceding lesson. \(\square\)

**Proposition 1.4.** If \(\mu\) is a positive measure, the convolution
\((\mu*k)(\xi)=\int k(\xi-y)\,d\mu(y)\) is either infinite everywhere or, if finite at one point, finite everywhere. In the finite case it obeys the same shift inequality as \(k\). It is a positive moderate weight when \(\mu\ne0\).

**Proof.** Integrate both sides of the moderate shift inequality for \(k(\xi-y)\). Finiteness at one point then gives finiteness at every point. A nonzero positive measure integrates a strictly positive function to a strictly positive number. \(\square\)

## Replacing a weight by one that moves slowly

Equivalent weights define equivalent norms, but their local shift behavior can be quite different. The following construction will make perturbation estimates small.

**Theorem 2.1.** For \(\varepsilon>0\), set
\[
k_\varepsilon(\xi)=\sup_y e^{-\varepsilon|y|}k(\xi-y).
\]
Then \(k\leq k_\varepsilon\leq A_\varepsilon k\) for a finite \(A_\varepsilon\). The original moderate shift constants also work for \(k_\varepsilon\), and
\[
1\leq M_{k_\varepsilon}(h)\leq e^{\varepsilon|h|}.
\]
Thus \(M_{k_\varepsilon}\to1\) uniformly on every bounded set as \(\varepsilon\downarrow0\).

**Proof.** The choice \(y=0\) gives the lower bound. The original shift estimate gives the upper bound with
\(A_\varepsilon=\sup_{r\geq0}e^{-\varepsilon r}(1+Cr)^N<\infty\).
Keeping \(y\) fixed in the supremum proves that the original polynomial shift bound is retained. Alternatively write
\(k_\varepsilon(\xi)=\sup_z e^{-\varepsilon|\xi-z|}k(z)\).
The triangle inequality shows \(k_\varepsilon(\xi+h)\leq e^{\varepsilon|h|}k_\varepsilon(\xi)\). Apply Lemma 1.1 for the lower bound and let \(\varepsilon\downarrow0\). No differentiability of \(k_\varepsilon\) is asserted. \(\square\)

## A Banach space on each Fourier scale

Use
\[
\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx,
\qquad
\mathcal F^{-1}g(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}g(\xi)\,d\xi.
\]
For \(1\leq p\leq\infty\), define \(B_{p,k}\) to be the tempered distributions \(u\) whose Fourier transform is a measurable function with \(k\widehat u\in L^p\). Its norm is
\[
\|u\|_{p,k}=(2\pi)^{-n/p}\|k\widehat u\|_{L^p},
\]
where \(1/\infty=0\). Equality of Fourier functions is understood almost everywhere.

**Theorem 3.1.** The space \(B_{p,k}\) is Banach, and both inclusions
\[
\mathcal S\longrightarrow B_{p,k}\longrightarrow\mathcal S'
\]
are continuous. If \(p<\infty\), compactly supported smooth functions are dense in \(B_{p,k}\).

**Proof.** A measurable \(g\) with \(kg\in L^p\) defines a tempered distribution: for \(\psi\in\mathcal S\), Hölder's inequality gives
\[
\left|\int g\psi\right|\leq\|kg\|_p\|\psi/k\|_{p'}.
\]
The second factor is bounded by finitely many Schwartz seminorms because \(1/k\) has polynomial growth. Conversely \(k\) has polynomial growth, so the weighted norm of a Schwartz function is bounded by finitely many of its seminorms. Fourier inversion identifies \(B_{p,k}\) isometrically with the complete space of functions of weighted \(L^p\) norm. This proves completeness and the two continuous inclusions. The bound just given is uniform on bounded subsets of \(\mathcal S\), so it also proves continuity into the strong dual topology on \(\mathcal S'\).

For finite \(p\), first truncate a weighted \(L^p\) function to compact frequency sets. On a fixed compact set \(k\) is bounded above and bounded away from zero, so approximation there by smooth compactly supported functions in ordinary \(L^p\) is also approximation in weighted \(L^p\). Their inverse transforms lie in \(\mathcal S\). Finally, if \(u\in\mathcal S\), multiplying it by a fixed smooth cutoff equal to one near zero, dilated to larger and larger balls, converges to \(u\) in every Schwartz seminorm. Hence it converges in \(B_{p,k}\). This proves the stated density. \(\square\)

For \(p=2\), Plancherel makes \(B_{2,1}=L^2\) with the same norm. For \(k=\langle\xi\rangle^s\), \(B_{2,k}\) is the Fourier definition of \(H^s\). These familiar spaces are special cases; no evenness or radial symmetry is required of a general weight.

## Cutoffs, differential operators, and convolution

**Theorem 4.1.** For \(\chi\in\mathcal S\), multiplication by \(\chi\) is bounded on \(B_{p,k}\), and
\[
\|\chi u\|_{p,k}\leq A_k(\chi)\|u\|_{p,k},
\qquad
A_k(\chi)=(2\pi)^{-n}\int M_k(h)|\widehat\chi(h)|\,dh.
\]

**Proof.** The Fourier transform of a product is \((2\pi)^{-n}\widehat\chi*\widehat u\). The weighted pointwise bound is
\[
k(\xi)|\widehat{\chi u}(\xi)|
\leq(2\pi)^{-n}\int
M_k(\xi-\eta)|\widehat\chi(\xi-\eta)|
k(\eta)|\widehat u(\eta)|\,d\eta.
\]
The kernel \(M_k|\widehat\chi|\) is integrable. The \(L^1*L^p\) inequality proves the claim, including \(p=1\) and \(p=\infty\). The product formula holds distributionally as well: the bound proves absolute integrability after pairing with a Schwartz function, which permits Fubini in that pairing. \(\square\)

**Proposition 4.2.** For a nonzero polynomial \(Q\),
\[
Q(D):B_{p,k}\longrightarrow B_{p,k/S_Q}
\]
has norm at most one. If \(u\in B_{p,k_1}\) has compact support and \(v\in B_{\infty,k_2}\), then
\[
u*v\in B_{p,k_1k_2},\qquad
\|u*v\|_{p,k_1k_2}\leq\|u\|_{p,k_1}\|v\|_{\infty,k_2}.
\]

**Proof.** The first statement follows from \(\widehat{Q(D)u}=Q\widehat u\) and \(|Q|\leq S_Q\). The quotient weight is moderate by Lemma 1.1. For the second, compact support makes convolution defined and its transform is \(\widehat u\widehat v\). Apply the \(L^p\) bound for multiplication by a bounded function to \(k_1\widehat u\) and \(k_2\widehat v\). \(\square\)

**Theorem 4.3.** Let \(p<\infty\), \(u\in B_{p,k}\), \(\chi\in C_c^\infty\) with \(\chi(0)=1\), and \(\rho\in C_c^\infty\) with \(\int\rho=1\). Then
\[
\chi(\varepsilon x)u\longrightarrow u,
\qquad
u*\rho_\varepsilon\longrightarrow u
\quad\text{in }B_{p,k},
\qquad \rho_\varepsilon(x)=\varepsilon^{-n}\rho(x/\varepsilon).
\]

**Proof.** The cutoff bound is uniform for \(0<\varepsilon\leq1\): after substituting \(h=\varepsilon z\), its constant is at most
\((2\pi)^{-n}\int(1+C|z|)^N|\widehat\chi(z)|\,dz\).
Convergence for a compactly supported smooth \(u\) holds in its smooth test-function topology, because \(\chi(\varepsilon x)\to1\) with all derivatives on its support. Density from Theorem 3.1 and the uniform bound give convergence for every \(u\). For mollification,
\(\widehat{u*\rho_\varepsilon}(\xi)=\widehat u(\xi)\widehat\rho(\varepsilon\xi)\).
The second factor is uniformly bounded and tends pointwise to one. Dominated convergence in the weighted \(L^p\) norm completes the proof. \(\square\)

## Duality with the signs visible

For \(p<\infty\), the continuous linear functionals on \(B_{p,k}\) can be represented as
\[
L_v(u)=(2\pi)^{-n}\int
\widehat u(\xi)\overline{\widehat v(\xi)}\,d\xi,
\qquad v\in B_{p',1/k}.
\]
The map \(v\mapsto L_v\) is conjugate-linear. If instead a linear functional is written as a complex-linear distribution pairing \(\langle w,u\rangle\) on Schwartz functions, its representing distribution belongs to \(B_{p',1/k^\vee}\).

**Theorem 5.1.** Every continuous linear functional has a unique representation \(L_v\) as above, with norm \(\|v\|_{p',1/k}\). Equivalently, the bilinear distribution representation has norm \(\|w\|_{p',1/k^\vee}\). These statements include \(p=1\), \(p'=\infty\), but make no assertion that the dual of \(B_{\infty,k}\) is another weighted Fourier space.

**Proof.** Identify \(B_{p,k}\) with weighted \(L^p\) as in Theorem 3.1 and apply the \(L^p\) duality theorem to \(k\widehat u\). It gives the first representation and its exact norm; the factors \((2\pi)^{-n/p}\) and \((2\pi)^{-n/p'}\) multiply to \((2\pi)^{-n}\). Uniqueness follows either from that duality or from the density of Schwartz functions. For the bilinear convention,
\[
\langle w,u\rangle=(2\pi)^{-n}\int
\widehat w(-\xi)\widehat u(\xi)\,d\xi.
\]
Thus \(\widehat w(-\xi)=\overline{\widehat v(\xi)}\), and reflection changes \(1/k\) into \(1/k^\vee\). This proves the second statement. \(\square\)

## Exercises with solutions

**Exercise 1 (entry).** Compute \(S_P\) for \(P(\xi_1,\xi_2)=\xi_1^2+i\xi_2\). Give the weight of the target space in Proposition 4.2 when the initial weight is one.

**Solution.** The nonzero derivatives are \(P\), \(2\xi_1\), \(i\), and \(2\). Hence
\(S_P^2=\xi_1^4+\xi_2^2+4\xi_1^2+5\).
The target weight is \(1/S_P\). It allows loss measured by this anisotropic polynomial size, rather than by a uniform two-derivative isotropic weight.

**Exercise 2 (intermediate).** For finite \(p\), decide exactly when \(\delta_0\in B_{p,\langle\xi\rangle^s}\). What is the answer for \(p=\infty\)?

**Solution.** The Fourier transform of delta is one. For finite \(p\), the norm is finite exactly when \(\int\langle\xi\rangle^{sp}\,d\xi<\infty\), which by radial integration holds exactly when \(sp<-n\). The equality case diverges logarithmically. For \(p=\infty\), the weight is bounded exactly when \(s\leq0\).

**Exercise 3 (intermediate).** Show that compactly supported smooth functions are not dense in \(B_{\infty,1}\), and that the mollification conclusion of Theorem 4.3 fails there.

**Solution.** Delta belongs to \(B_{\infty,1}\) and its Fourier transform is one. A compactly supported smooth function has a rapidly decreasing Fourier transform, so its distance from delta in this norm is at least one, by taking frequencies tending to infinity. Similarly, \(\delta_0*\rho_\varepsilon=\rho_\varepsilon\) has transform \(\widehat\rho(\varepsilon\xi)\), which tends to zero at infinity for each fixed \(\varepsilon>0\). Hence its distance from delta is at least one for every \(\varepsilon\).

**Exercise 4 (advanced).** Let \(k(\xi)=(1+\max(\xi,0))^2\). State the weight of the distribution representing a bilinear linear functional on \(B_{1,k}\), and explain why simply writing \(1/k\) changes the assertion.

**Solution.** The representing distribution lies in \(B_{\infty,1/k^\vee}\), where \(k^\vee(\xi)=(1+\max(-\xi,0))^2\). These reciprocal weights impose different conditions at positive and negative infinity. For example a Fourier function that grows quadratically only at negative infinity is allowed by \(1/k^\vee\), but is not allowed by \(1/k\). The reversal comes from \(\widehat w(-\xi)\) in the bilinear pairing, not from a choice to make the weight even.

## References

- [Grubb] Gerd Grubb, *Distributions and Operators*, open lecture-note versions, 2007–2008, sections on Fourier transformation and Sobolev spaces. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- [Melrose] Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004, sections on the Schwartz space, Fourier transformation, and Sobolev embedding. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Internal inequalities: [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html#section-15-2), Section 15.2, proves Hölder, Minkowski and all Young endpoints.
- Internal completeness and density: [the same foundation](../prerequisites/banach-foundation-bridges.html#section-15-3), Section 15.3, proves completeness for every displayed exponent and compact smooth density for finite exponents.
- Internal duality: [Lebesgue duality and the functionals on Fourier spaces](lebesgue-duality-and-fourier-functionals.md), Lemmas 1.1 and 2.1–2.2 and Theorem 3.1, proves finite-exponent duality before its weighted Fourier adapter.
- Internal cutoff construction: [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html#section-13-10), Section 13.10.
