# Schwartz idempotents and lattice projections

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In the fiber at \(t\), the twisted algebra \(C_r^*(\bar E_{\mathbb Z},tc)\) must contain a nonzero projection of trace about \(|t|^{n_{\mathrm f}}\). The continuous group \(\bar E\) has a twisted representation on \(L^2(\mathfrak n)\) in which Schwartz functions on \(\bar E\) correspond exactly to Schwartz integral kernels, so the rank-one projection onto a Gaussian comes from a Schwartz *idempotent* for twisted convolution. Rescaling it by the dilations of the grading and sampling it on the lattice \(\bar E_{\mathbb Z}\) gives an almost idempotent element of the discrete twisted algebra, which functional calculus turns into a projection; its trace is controlled by the \(\ell^2\) norm of the samples, which is about the square root of the cell volume [OpenAI-KK, Section 8.4, Lemmas 8.5 to 8.8].

- A Schwartz idempotent (Section 1).
- Weighted Riemann sums (Section 2).
- Discrete twisted projections (Section 3).
- Compact templates (Section 4).

The notation of [An affine nilpotent group](an-affine-nilpotent-group.md) is in force: \(E\), \(\bar E\), the cocycle \(c\), the dilations \(\Delta_y\), Haar measure in coordinates, the lattice \(L=\bar E_{\mathbb Z}\), and \(\mathbf e(v)=e^{2\pi iv}\). A *Schwartz function* on \(\bar E\) is one in the Euclidean coordinates \((\lambda,b-1)\in\mathfrak n^*\times\mathfrak n\). We use that the Fourier transform \(\hat f(\xi)=\int f(\lambda)\mathbf e(\lambda(\xi))\,d\lambda\) is a bijection of the Schwartz space onto itself and preserves \(L^2\) norms, also as a partial Fourier transform in some of the variables: in the Hermite basis it acts diagonally by unimodular factors, which preserves the rapidly decreasing coefficient sequences (Theorem 3.2, Proposition 2.2 and Corollary 4.2 of [Hermite functions, tempered distributions and the Schwartz kernel theorem](course:index-theory-of-elliptic-operators/hermite-functions-tempered-distributions-and-the-schwartz-kernel-theorem), after the change of variables \(x\mapsto2\pi x\) that relates the two normalizations).

## 1. A Schwartz idempotent

For a sign \(\epsilon\in\{1,-1\}\) and functions on \(\bar E\), define the twisted convolution and involution
\[
\begin{aligned}
&(J*_\epsilon K)(h)\\
&\quad=\int_{\bar E}J(a)K(a^{-1}h)\,\mathbf e\bigl(\epsilon c(a,a^{-1}h)\bigr)\,da,\\
&J^{*_\epsilon}(h)=\overline{J(h^{-1})}\,\mathbf e\bigl(-\epsilon c(h^{-1},h)\bigr) .
\end{aligned}
\]

**Lemma 1.1** (Schwartz idempotents; [OpenAI-KK, Lemma 8.5]). For each sign \(\epsilon\) there is a Schwartz function \(J_\epsilon\) on \(\bar E\) with
\[
\begin{gathered}
J_\epsilon^{*_\epsilon}=J_\epsilon,\qquad J_\epsilon*_\epsilon J_\epsilon=J_\epsilon,\\
\|J_\epsilon\|_{L^2(\bar E)}=1 .
\end{gathered}
\]

*Proof.* For \(\gamma=(\lambda,b)\) define on \(L^2(\mathfrak n)\)
\[
(\pi_\epsilon(\gamma)\phi)(x)=\mathbf e(\epsilon\lambda(x))\,\phi(A_{b^{-1}}x) .
\]
These operators are unitary, because \(A_b\) preserves Lebesgue measure, and since \(\mu(A_{b^{-1}}x)=c(\gamma,\eta)+(\mu\circ L_{b^{-1}})(x)\) for \(\eta=(\mu,b')\),
\[
\pi_\epsilon(\gamma)\pi_\epsilon(\eta)=\mathbf e\bigl(\epsilon c(\gamma,\eta)\bigr)\pi_\epsilon(\gamma\eta) .
\]
For an integrable \(J\) let \(\pi_\epsilon(J)=\int J(\gamma)\pi_\epsilon(\gamma)\,d\gamma\), of norm at most \(\|J\|_1\). By Fubini's theorem and the left invariance of Haar measure, \(\pi_\epsilon(J)\pi_\epsilon(K)=\pi_\epsilon(J*_\epsilon K)\); and since \(\pi_\epsilon(a)^*=\mathbf e(-\epsilon c(a^{-1},a))\pi_\epsilon(a^{-1})\) and inversion preserves Haar measure, \(\pi_\epsilon(J)^*=\pi_\epsilon(J^{*_\epsilon})\).

*The kernel.* Let \(\hat J_+(\xi,b)=\int_{\mathfrak n^*}J(\lambda,b)\mathbf e(\lambda(\xi))\,d\lambda\) be the partial Fourier transform. Integrating first in \(\lambda\),
\[
(\pi_\epsilon(J)\phi)(x)=\int_U\hat J_+(\epsilon x,b)\,\phi(A_{b^{-1}}x)\,db ,
\]
and the substitution \(y=b^{-1}(1+x)-1\), that is \(b=(1+x)(1+y)^{-1}\), which for fixed \(x\) has Jacobian one, gives the integral kernel
\[
\begin{aligned}
&\mathcal K_J(x,y)\\
&=\hat J_+\bigl(\epsilon x,\\
&\qquad(1+x)(1+y)^{-1}\bigr) .
\end{aligned}\tag{1.1}
\]
The map \((x,y)\mapsto(\epsilon x,(1+x)(1+y)^{-1}-1)\) and its inverse are polynomial, with Jacobian of absolute value one. Composition with such a map preserves Schwartz functions: derivatives of the composite are polynomial combinations of derivatives of the function, and a polynomial weight in one set of coordinates is bounded by a polynomial weight in the other, because the inverse map is polynomial. Together with the properties of the partial Fourier transform, \(J\mapsto\mathcal K_J\) is a bijection from Schwartz functions on \(\bar E\) onto Schwartz functions on \(\mathfrak n\times\mathfrak n\), and it preserves \(L^2\) norms. An operator determines its continuous kernel: if a continuous kernel gives the zero operator, its pairings with all products of test functions vanish, and so does the kernel.

Twisted convolution and involution preserve Schwartz functions: \((a,h)\mapsto J(a)K(a^{-1}h)\mathbf e(\epsilon c(a,a^{-1}h))\) is Schwartz on \(\bar E\times\bar E\), since \((a,h)\mapsto(a,a^{-1}h)\) is polynomial with polynomial inverse and the phase has polynomial derivatives, and integrating in \(a\) keeps rapid decay of all derivatives in \(h\).

Let \(\phi(x)=2^{n_{\mathrm f}/4}e^{-\pi|x|^2}\), of norm one, so that the orthogonal projection onto its span has the Schwartz kernel \(\phi(x)\overline{\phi(y)}\), and let \(J_\epsilon\) be the Schwartz function with this kernel. The operator of \(J_\epsilon*_\epsilon J_\epsilon\) is the square of the projection and that of \(J_\epsilon^{*_\epsilon}\) its adjoint, so both equal the projection, and by injectivity both functions equal \(J_\epsilon\). Finally \(\|J_\epsilon\|_2^2=\iint|\phi(x)|^2|\phi(y)|^2\,dx\,dy=1\). \(\square\)

## 2. Weighted Riemann sums

**Lemma 2.1** (weighted Riemann sums; [OpenAI-KK, Lemma 8.6]). Let \(w_1,\ldots,w_k\) be positive integers, and for \(0<y\le1\) let \(\mathcal L_y=\prod_ay^{w_a}\mathbb Z\subseteq\mathbb R^k\), with cell volume \(v_y=y^{w_1+\cdots+w_k}\). For a Schwartz function \(f\) on \(\mathbb R^k\), \(v_y\sum_{a\in\mathcal L_y}f(a)\to\int f\) as \(y\to0\), and \(v_y\sum_{a\in\mathcal L_y}|f(a)|\) is bounded. For a Schwartz function \(G(a,h)\) on \(\mathbb R^k\times\mathbb R^k\) and every \(M\),
\[
\begin{aligned}
&\sup_h(1+|h|)^M\\
&\quad\cdot\Bigl|v_y\sum_{a\in\mathcal L_y}G(a,h)-\int G(a,h)\,da\Bigr|\\
&\quad\le C_{G,M}\,y .
\end{aligned}
\]

*Proof.* The cells \(Q_a=a+\prod_j[0,y^{w_j})\), \(a\in\mathcal L_y\), tile \(\mathbb R^k\), have volume \(v_y\) and diameter at most \(\sqrt ky\). For \(x\in Q_a\), the mean value theorem and the Schwartz bounds give
\[
\begin{aligned}
&|G(a,h)-G(x,h)|\\
&\quad\le\sqrt ky\sup_{z\in Q_a}|\nabla_aG(z,h)|\\
&\quad\le C_{K,M}\,y(1+|a|)^{-K}(1+|h|)^{-M} ,
\end{aligned}
\]
because \(1+|z|\) and \(1+|a|\) are comparable on a cell. For \(K>k\), \(v_y\sum_a(1+|a|)^{-K}\le C\int(1+|x|)^{-K}dx\), which is finite. Integrating the difference over each cell and summing gives the estimate; the other statements follow in the same way. \(\square\)

## 3. Discrete twisted projections

For real \(\theta\), let \(C_r^*(L,\theta c)\) be the norm closure of the linear span of the unitaries \(u_\theta(\gamma)\), \(\gamma\in L\), on \(\ell^2(L)\). For \(a\in\ell^1(L)\) the series \(\sum_\gamma a_\gamma u_\theta(\gamma)\) converges in norm, with norm at most \(\sum_\gamma|a_\gamma|\), the *coefficient \(\ell^1\) norm*. Since \(c(\gamma,1)=0\), it maps \(\delta_1\) to \(\sum_\gamma a_\gamma\delta_\gamma\), whose norm is the *coefficient \(\ell^2\) norm*. Its identity trace \(\operatorname{tr}_\theta\), the coefficient \(a_1\), satisfies \(\operatorname{tr}_\theta(A^*A)=\|A\delta_1\|^2\).

**Proposition 3.1** (nonzero discrete twisted projections; [OpenAI-KK, Proposition 8.7]). There are \(\theta_0>0\) and \(C<\infty\), depending only on \(m\) and the functions \(J_\pm\), such that the following holds for \(0<|\theta|<\theta_0\). Put \(\epsilon=\operatorname{sign}\theta\), \(y=|\theta|^{1/m}\), \(\nu=y^{mn_{\mathrm f}}=|\theta|^{n_{\mathrm f}}\), and
\[
K_\theta=\sum_{\gamma\in L}\nu J_\epsilon(\Delta_y\gamma)\,u_\theta(\gamma) .
\]
Then \(K_\theta\) is self-adjoint, its coefficient \(\ell^1\) norm is at most \(C\), its coefficient \(\ell^2\) norm lies between \(C^{-1}\sqrt\nu\) and \(C\sqrt\nu\), and \(K_\theta^2-K_\theta\) has coefficient \(\ell^1\) norm at most \(Cy\) and coefficient \(\ell^2\) norm at most \(Cy\sqrt\nu\). The continuous functional calculus gives a projection \(p_\theta\in C_r^*(L,\theta c)\) with
\[
\begin{gathered}
\|p_\theta-K_\theta\|\le Cy,\\
0<\operatorname{tr}_\theta(p_\theta)\le C|\theta|^{n_{\mathrm f}} .
\end{gathered}
\]
The coefficients of \(K_\theta\) and the operators \(p_\theta\) depend measurably on \(\theta\).

*Proof.* In the coordinates of \(\bar E\), \(\Delta_yL\) is the rectangular lattice with spacing \(y^w\) in each coordinate of weight \(w\), of cell volume \(\nu\) by Lemma 2.1 of the previous lesson. Lemma 2.1, applied to \(J_\epsilon\) and \(|J_\epsilon|^2\), bounds the coefficient \(\ell^1\) norm and shows that
\[
\begin{aligned}
\nu^{-1}\sum_\gamma|\nu J_\epsilon(\Delta_y\gamma)|^2&=\nu\sum_{a\in\Delta_yL}|J_\epsilon(a)|^2\\
&\to\|J_\epsilon\|_2^2=1 ,
\end{aligned}
\]
which gives the \(\ell^2\) bounds for small \(\theta\).

*Self-adjointness.*
\[
\begin{aligned}
K_\theta^*&=\sum_\gamma\nu\overline{J_\epsilon(\Delta_y\gamma)}\\
&\qquad\cdot\mathbf e(-\theta c(\gamma^{-1},\gamma))u_\theta(\gamma^{-1}) .
\end{aligned}
\]
Since \(\Delta_y\) is an automorphism and \(\epsilon c(\Delta_y\gamma^{-1},\Delta_y\gamma)=\epsilon y^mc(\gamma^{-1},\gamma)\), which is \(\theta c(\gamma^{-1},\gamma)\), the identity \(J_\epsilon=J_\epsilon^{*_\epsilon}\) says exactly that the coefficient of \(u_\theta(\gamma)\) in \(K_\theta^*\) is \(\nu J_\epsilon(\Delta_y\gamma)\).

*The defect.* By the multiplier formula, the coefficient of \(u_\theta(\gamma)\) in \(K_\theta^2\), divided by \(\nu\), is, with \(h=\Delta_y\gamma\),
\[
\nu\sum_{a\in\Delta_yL}J_\epsilon(a)J_\epsilon(a^{-1}h)\,\mathbf e\bigl(\epsilon c(a,a^{-1}h)\bigr),
\]
a Riemann sum for \((J_\epsilon*_\epsilon J_\epsilon)(h)=J_\epsilon(h)\). Its difference \(D_y(h)\) from \(J_\epsilon(h)\) satisfies \(|D_y(h)|\le C_My(1+|h|)^{-M}\) by Lemma 2.1, so the coefficients \(\nu D_y(\Delta_y\gamma)\) of \(K_\theta^2-K_\theta\) have \(\ell^1\) norm at most \(Cy\) and \(\ell^2\) norm at most \(Cy\sqrt\nu\).

*The projection.* Since the coefficient \(\ell^1\) norm bounds the operator norm, \(\|K_\theta^2-K_\theta\|\le Cy\), and every \(\lambda\) in the spectrum of the self-adjoint \(K_\theta\) satisfies \(|\lambda^2-\lambda|\le Cy\). Outside \([-\frac14,\frac14]\cup[\frac34,\frac54]\) one has \(|\lambda^2-\lambda|>\frac3{16}\) (Exercise 5.3), so for small \(y\) the spectrum lies in these two intervals. Let \(\chi\) be continuous, \(0\) on the first interval and \(1\) on the second, and \(p_\theta=\chi(K_\theta)\), a projection in \(C_r^*(L,\theta c)\). On the two intervals \(\chi(\lambda)-\lambda=(\lambda^2-\lambda)f(\lambda)\) with \(f(\lambda)=(1-\lambda)^{-1}\), respectively \(f(\lambda)=-\lambda^{-1}\), and \(|f|\le2\), so \(\|p_\theta-K_\theta\|\le2Cy\).

If \(p_\theta=0\), the spectrum lies in \([-\frac14,\frac14]\), so \(\|K_\theta\|\le\frac14\) and \(\|(K_\theta^2-K_\theta)\delta_1\|\ge\frac34\|K_\theta\delta_1\|\); for small \(y\) this contradicts \(\|(K_\theta^2-K_\theta)\delta_1\|\le Cy\sqrt\nu\) and \(\|K_\theta\delta_1\|\ge C^{-1}\sqrt\nu\). On the two intervals \(0\le\chi(\lambda)\le4\lambda^2\), so \(0\le p_\theta\le4K_\theta^2\) and
\[
\operatorname{tr}_\theta(p_\theta)\le4\operatorname{tr}_\theta(K_\theta^2)=4\|K_\theta\delta_1\|^2\le C\nu .
\]
A nonzero projection commuting with the right operators \(v_\theta\) has positive identity trace (Lemma 2.1(3) of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md)). The coefficients are continuous in \(\theta\); norm-convergent coefficient sums give measurable fields, and so does \(\chi\) applied to them, by uniform polynomial approximation of \(\chi\) on \([-2,2]\). \(\square\)

## 4. Compact templates

**Lemma 4.1** (compact templates and scale changes; [OpenAI-KK, Lemma 8.8]). For every \(\varepsilon_0>0\) there are smooth compactly supported \(J_\pm^\flat\) such that, for small \(|\theta|\), replacing \(J_\epsilon\) by \(J_\epsilon^\flat\) in \(K_\theta\) changes the coefficients by \(\ell^1\) norm at most \(\varepsilon_0\). For fixed such \(J^\flat\), and \(\alpha,\beta>0\) small with \(|\log(\alpha/\beta)|\le a\le1\), the coefficient families \(\gamma\mapsto\alpha^{n_{\mathrm f}}J^\flat(\Delta_{\alpha^{1/m}}\gamma)\) and \(\gamma\mapsto\beta^{n_{\mathrm f}}J^\flat(\Delta_{\beta^{1/m}}\gamma)\) differ by \(\ell^1\) norm at most \(Ca\). These coefficient bounds bound the norm of the corresponding sums of any unitaries.

*Proof.* Multiply \(J_\epsilon\) by a smooth function equal to \(1\) on a large ball; by Lemma 2.1 and the rapid decay of \(J_\epsilon\), the normalized lattice sum of the discarded part is small, uniformly for small mesh. For the second statement put \(r=\alpha/\beta\) and \(h=\Delta_{\beta^{1/m}}\gamma\); after the factor \(\beta^{n_{\mathrm f}}\), the difference is \(r^{n_{\mathrm f}}J^\flat(\Delta_{r^{1/m}}h)-J^\flat(h)\). For \(e^{-1}\le r\le e\) it is supported in one compact set, and by the mean value theorem in \(r\) it is at most \(C|\log r|\); the number of points of \(\Delta_{\beta^{1/m}}L\) in a compact set, times \(\beta^{n_{\mathrm f}}\), is bounded. \(\square\)

## 5. Exercises

**5.1** (easy). Check that \(\phi(x)=2^{n_{\mathrm f}/4}e^{-\pi|x|^2}\) has \(L^2\) norm one on \(\mathbb R^{n_{\mathrm f}}\).

**5.2** (medium). For \(m=2\), so that \(\bar E\cong\mathbb R^2\) with \(c((\lambda,\beta),(\mu,\beta'))=-\mu\beta\), write \(\pi_\epsilon(\lambda,\beta)\) on \(L^2(\mathbb R)\) and recognize the Schrödinger representation.

**5.3** (medium). Show that for a self-adjoint operator \(K\) with \(\|K^2-K\|\le\delta<\frac3{16}\), the spectrum lies in \([-\frac14,\frac14]\cup[\frac34,\frac54]\).

**5.4** (medium). For the one-dimensional lattice \(y\mathbb Z\) and \(f(x)=e^{-\pi x^2}\), compare \(y\sum_{a\in y\mathbb Z}f(a)\) with \(\int f=1\) for \(y=1\) and \(y=\frac12\).

## 6. Solutions

**5.1.** \(\int2^{n_{\mathrm f}/2}e^{-2\pi|x|^2}dx=2^{n_{\mathrm f}/2}(2^{-1/2})^{n_{\mathrm f}}=1\).

**5.2.** \(A_{b^{-1}}x=x-\beta\) for \(b=1+\beta\), so \((\pi_\epsilon(\lambda,\beta)\phi)(x)=\mathbf e(\epsilon\lambda x)\phi(x-\beta)\): modulations and translations, the Schrödinger representation of the Heisenberg group with Planck constant \(\epsilon\).

**5.3.** For \(\lambda\) in the spectrum, \(|\lambda^2-\lambda|\le\delta\). If \(\lambda\) were in \((\frac14,\frac34)\), or below \(-\frac14\), or above \(\frac54\), then \(|\lambda||\lambda-1|>\frac14\cdot\frac34=\frac3{16}\).

**5.4.** By Poisson summation \(y\sum_nf(ny)=\sum_ke^{-\pi k^2/y^2}\). For \(y=1\) this is \(1+2e^{-\pi}+\cdots\approx1.0864\); for \(y=\frac12\), \(1+2e^{-4\pi}+\cdots\approx1.0000070\). The error decreases much faster than the bound \(Cy\) of Lemma 2.1, which holds for all Schwartz functions.

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Section 8.4, Lemmas 8.5, 8.6 and 8.8, Proposition 8.7. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026
