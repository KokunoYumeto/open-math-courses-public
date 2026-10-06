# Hermite functions, tempered distributions and the Schwartz kernel theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).* *Coefficient correspondence and growth conventions checked and clarified by GPT-6 Astra (OpenAI), Codex, Ultra reasoning effort. Self-checked by that AI; no independent human review is claimed.*

The Hermite functions \(h_\alpha\) form an orthonormal basis of \(L^2(\mathbb R^n)\) of Schwartz functions on which the harmonic oscillator and the Fourier transform act diagonally. In this basis the Schwartz space \(\mathcal S(\mathbb R^n)\) becomes the space of rapidly decreasing coefficient sequences (Theorem 3.2), and the tempered distributions become the polynomially bounded sequences (Theorem 4.1). Three facts that are used throughout the analysis of pseudodifferential operators then follow quickly: the Fourier transform is an isomorphism of \(\mathcal S\) and of \(\mathcal S'\) (Corollary 4.2); every continuous linear map \(\mathcal S(\mathbb R^n)\to\mathcal S'(\mathbb R^m)\) has a tempered distribution kernel (Theorem 5.1, the Schwartz kernel theorem); and a tempered solution of the Bott oscillator equation of the lesson [The Bott operator, suspension, and reduction of the index to Euclidean space](the-bott-operator-suspension-and-reduction-of-the-index-to-euclidean-space.md) is a multiple of the Gaussian (Proposition 6.1).

The kernel theorem is due to Schwartz [Schwartz 1952]. The approach through Hermite expansions follows [Simon 1971].

We use from the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) the Lebesgue integral, Fubini's theorem and dominated convergence; Parseval's identity for orthonormal bases from [Hilbert spaces and compact operators](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators#OA-FND-HS-04); the Baire category theorem from [Hahn–Banach, Baire and the basic theorems on Banach spaces, Theorem 3.1](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces#OA-FND-HB-03); and the uniqueness theorem for the Fourier transform on \(L^1(\mathbb R^n)\), a consequence of [The Fourier inversion theorem and the dual Haar measure](course:HA-LCA/HA-LCA-07).

## 1. Conventions

\(\mathcal S=\mathcal S(\mathbb R^n)\) is the space of smooth functions \(\varphi\) with \(p_{\beta,\gamma}(\varphi)=\sup_x|x^\beta\partial^\gamma\varphi(x)|<\infty\) for all multi-indices \(\beta,\gamma\), with the topology of these seminorms. A *tempered distribution* is a continuous linear functional on \(\mathcal S\); they form \(\mathcal S'\). The Fourier transform is \(\mathcal F\varphi(\xi)=\int e^{-ix\cdot\xi}\varphi(x)\,dx\). For \(\varphi\in\mathcal S\), differentiation under the integral and integration by parts give
\[
\mathcal F(x_j\varphi)=i\,\partial_{\xi_j}\mathcal F\varphi,\qquad\mathcal F(\partial_j\varphi)=i\xi_j\,\mathcal F\varphi .
\tag{1.1}
\]
On \(\mathcal S\) put \(A_j=x_j+\partial_j\) and \(A_j^\dagger=x_j-\partial_j\). Integration by parts gives \(\int(A_j\varphi)\psi=\int\varphi(A_j^\dagger\psi)\) for real or complex \(\varphi,\psi\in\mathcal S\), and \([A_j,A_l]=[A_j^\dagger,A_l^\dagger]=0\), \([A_j,A_l^\dagger]=2\delta_{jl}\). Moreover \(\sum_jA_j^\dagger A_j=-\Delta+|x|^2-n\), and
\[
x_j=\tfrac12(A_j+A_j^\dagger),\qquad\partial_j=\tfrac12(A_j-A_j^\dagger).
\tag{1.2}
\]
A multi-index \(\alpha\in\mathbb N^n\) has \(|\alpha|=\alpha_1+\dots+\alpha_n\), and \(e_j\) is the \(j\)-th unit multi-index. There are at most \((k+1)^{n-1}\) multi-indices with \(|\alpha|=k\), so
\[
\sum_{\alpha\in\mathbb N^n}(1+|\alpha|)^{-n-1}\le\sum_{k\ge0}(k+1)^{-2}<\infty .
\tag{1.3}
\]

## 2. Hermite functions

In one variable let \(h_0(x)=\pi^{-1/4}e^{-x^2/2}\) and \(h_k=(2^kk!)^{-1/2}(A^\dagger)^kh_0\). In \(n\) variables let \(h_\alpha(x)=h_{\alpha_1}(x_1)\cdots h_{\alpha_n}(x_n)\).

**Proposition 2.1.**

1. \(h_k(x)=H_k(x)e^{-x^2/2}\) with a real polynomial \(H_k\) of degree \(k\), and \(h_k(-x)=(-1)^kh_k(x)\).
2. \(A_jh_\alpha=\sqrt{2\alpha_j}\,h_{\alpha-e_j}\) (zero if \(\alpha_j=0\)), \(A_j^\dagger h_\alpha=\sqrt{2(\alpha_j+1)}\,h_{\alpha+e_j}\), and \((-\Delta+|x|^2)h_\alpha=(2|\alpha|+n)h_\alpha\).
3. The \(h_\alpha\) form an orthonormal basis of \(L^2(\mathbb R^n)\).

*Proof.* (1) \(A^\dagger(qe^{-x^2/2})=(2xq-q')e^{-x^2/2}\) raises the degree of the polynomial \(q\) by one and changes its parity.

(2) \(Ah_0=0\). From \([A,A^\dagger]=2\), induction gives \(A(A^\dagger)^kh_0=2k(A^\dagger)^{k-1}h_0\), so \(Ah_k=(2^kk!)^{-1/2}2k(2^{k-1}(k-1)!)^{1/2}h_{k-1}=\sqrt{2k}\,h_{k-1}\); the formula for \(A^\dagger\) is the definition. In \(n\) variables \(A_j\) and \(A_j^\dagger\) act on the \(j\)-th factor, so \(A_j^\dagger A_jh_\alpha=2\alpha_jh_\alpha\), and \(-\Delta+|x|^2=\sum_jA_j^\dagger A_j+n\).

(3) \(\int h_0^2=1\). The operator \(A^\dagger A\) is symmetric on \(\mathcal S\) and \(A^\dagger Ah_k=2kh_k\), so \(h_k\perp h_l\) for \(k\ne l\); and \(\|h_{k+1}\|^2=\frac1{2(k+1)}\int(AA^\dagger h_k)h_k=\frac1{2(k+1)}\int\bigl((A^\dagger A+2)h_k\bigr)h_k=\|h_k\|^2\). By Fubini the products \(h_\alpha\) are orthonormal in \(L^2(\mathbb R^n)\). For completeness let \(f\in L^2(\mathbb R^n)\) be orthogonal to all \(h_\alpha\). By (1) it is orthogonal to every \(x^\beta e^{-|x|^2/2}\). Put \(g=fe^{-|x|^2/2}\); for every \(t>0\), \(\int|g|e^{t|x|}\le\|f\|_2\bigl\|e^{-|x|^2/2+t|x|}\bigr\|_2<\infty\). For \(\xi\in\mathbb R^n\) expand \(e^{-ix\cdot\xi}=\sum_\beta\frac{(-i\xi)^\beta x^\beta}{\beta!}\); the series of absolute values is \(\prod_je^{|\xi_j||x_j|}\le e^{|\xi|_1|x|}\), so dominated convergence gives \(\mathcal Fg(\xi)=\sum_\beta\frac{(-i\xi)^\beta}{\beta!}\int g\,x^\beta=0\). By the uniqueness of the Fourier transform on \(L^1\), \(g=0\), hence \(f=0\). \(\square\)

**Proposition 2.2** (Fourier transform). \(\mathcal Fh_\alpha=(2\pi)^{n/2}(-i)^{|\alpha|}h_\alpha\).

*Proof.* In one variable, \(G(\xi)=\int e^{-x^2/2-ix\xi}dx\) satisfies \(G'(\xi)=\int(-ix)e^{-x^2/2-ix\xi}dx=-\xi G(\xi)\), by integrating \(\frac{d}{dx}e^{-x^2/2}\) by parts; so \(G(\xi)=G(0)e^{-\xi^2/2}=\sqrt{2\pi}\,e^{-\xi^2/2}\), that is, \(\mathcal Fh_0=\sqrt{2\pi}\,h_0\). By (1.1), \(\mathcal F(A^\dagger\varphi)=i\partial_\xi\mathcal F\varphi-i\xi\mathcal F\varphi=-iA^\dagger\mathcal F\varphi\). Induction gives \(\mathcal Fh_k=\sqrt{2\pi}(-i)^kh_k\), and Fubini gives the product formula. \(\square\)

## 3. The Schwartz space in Hermite coordinates

For \(\varphi\in L^2(\mathbb R^n)\) let \(c_\alpha(\varphi)=\int\varphi\,h_\alpha\), and for \(N\ge0\)
\[
\|\varphi\|_N=\Bigl(\sum_\alpha(2|\alpha|+n)^{2N}|c_\alpha(\varphi)|^2\Bigr)^{1/2}\in[0,\infty] .
\]
These norms increase with \(N\). A sequence \((c_\alpha)\) is *rapidly decreasing* if \(\sup_\alpha(1+|\alpha|)^N|c_\alpha|<\infty\) for every integer \(N\ge0\). It is *polynomially bounded* if \(\sup_\alpha(1+|\alpha|)^{-N}|c_\alpha|<\infty\) for some integer \(N\ge0\); equivalently, \(|c_\alpha|\le C(1+|\alpha|)^N\) for some \(C,N\).

**Lemma 3.1.** For multi-indices \(\beta,\gamma\) there are \(C\) and \(M\) such that \(p_{\beta,\gamma}(h_\alpha)\le C(1+|\alpha|)^M\) for all \(\alpha\).

*Proof.* A word \(W\) of length \(m\) in the operators \(A_j\), \(A_j^\dagger\) maps \(h_\alpha\) to \(ch_{\alpha'}\) with \(|c|\le(2(|\alpha|+m))^{m/2}\), by Proposition 2.1(2). By (1.2), every operator \(x^\beta\partial^\gamma\), and more generally every product of \(x_j\)'s and \(\partial_j\)'s, is a sum of finitely many such words with bounded coefficients; so \(\|x^\beta\partial^\gamma h_\alpha\|_2\le C(1+|\alpha|)^{(|\beta|+|\gamma|)/2}\), and the same holds for \((1-\Delta)^nx^\beta\partial^\gamma h_\alpha\) with exponent \((|\beta|+|\gamma|+2n)/2\). For a finite linear combination \(\psi\) of Hermite functions, Proposition 2.2 and the parity \(h_\alpha(-x)=(-1)^{|\alpha|}h_\alpha(x)\) give \(\mathcal F\mathcal F\psi(x)=(2\pi)^n\psi(-x)\), that is \(\psi(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}\mathcal F\psi(\xi)\,d\xi\); and \(\|\mathcal F\psi\|_2=(2\pi)^{n/2}\|\psi\|_2\). Hence, by Cauchy–Schwarz and (1.1),
\[
\|\psi\|_\infty\le(2\pi)^{-n}\|\mathcal F\psi\|_1\le(2\pi)^{-n}\bigl\|(1+|\xi|^2)^{-n}\bigr\|_2\,\bigl\|(1+|\xi|^2)^n\mathcal F\psi\bigr\|_2=C_n\|(1-\Delta)^n\psi\|_2 .
\]
Apply this to \(\psi=x^\beta\partial^\gamma h_\alpha\), a finite combination of Hermite functions. \(\square\)

**Theorem 3.2.**

1. If \(\varphi\in\mathcal S\), then \(\|\varphi\|_N=\|(-\Delta+|x|^2)^N\varphi\|_2<\infty\) for every \(N\); so \((c_\alpha(\varphi))\) is rapidly decreasing.
2. If \((c_\alpha)\) is rapidly decreasing, the series \(\sum_\alpha c_\alpha h_\alpha\) converges in every seminorm \(p_{\beta,\gamma}\) to a function \(\varphi\in\mathcal S\) with \(c_\alpha(\varphi)=c_\alpha\).
3. The norms \(\|\cdot\|_N\) define the topology of \(\mathcal S\), and \(\mathcal S\) is complete for the metric \(d(\varphi,\psi)=\sum_N2^{-N}\min(1,\|\varphi-\psi\|_N)\).

*Proof.* (1) \(L=-\Delta+|x|^2\) maps \(\mathcal S\) into \(\mathcal S\) and is symmetric, so \(c_\alpha(L^N\varphi)=\int\varphi\,L^Nh_\alpha=(2|\alpha|+n)^Nc_\alpha(\varphi)\), and Parseval gives the identity. Expanding \(L^N\) and bounding \(\|x^\beta\partial^\gamma\varphi\|_2\le\|(1+|x|^2)^{-n}\|_2\,p(\varphi)\) for a finite sum \(p\) of seminorms \(p_{\beta',\gamma}\), we get \(\|\varphi\|_N\le Cp(\varphi)\) for a finite sum \(p\) of seminorms.

(2) By Lemma 3.1 and (1.3), \(\sum_\alpha|c_\alpha|\,p_{\beta,\gamma}(h_\alpha)\le C\sum_\alpha(1+|\alpha|)^{-n-1}\cdot\sup_\alpha(1+|\alpha|)^{M+n+1}|c_\alpha|<\infty\). So all derivatives of the partial sums, multiplied by \(x^\beta\), converge uniformly; the limit \(\varphi\) is smooth, its derivatives are the limits, and \(p_{\beta,\gamma}(\varphi)<\infty\). The partial sums also converge in \(L^2\), so \(c_\alpha(\varphi)=c_\alpha\).

(3) The estimate in (2), with \(c_\alpha=c_\alpha(\varphi)\) and \(\sup_\alpha(1+|\alpha|)^K|c_\alpha|\le\|\varphi\|_K\), gives \(p_{\beta,\gamma}(\varphi)\le C\|\varphi\|_{M+n+1}\), and (1) gives the reverse bounds. So both families of seminorms define the same topology. If \((\varphi_k)\) is Cauchy for every \(\|\cdot\|_N\), the coefficients \(c_\alpha(\varphi_k)\) converge to some \(c_\alpha\) with \(\sum_\alpha(2|\alpha|+n)^{2N}|c_\alpha-c_\alpha(\varphi_k)|^2\to0\) for every \(N\), as for \(\ell^2\); then \((c_\alpha)\) is rapidly decreasing, and the \(\varphi\) of (2) is the limit. \(\square\)

## 4. Tempered distributions and the Fourier transform

**Theorem 4.1.** The map \(u\mapsto(u(h_\alpha))\) is a bijection from \(\mathcal S'\) onto the polynomially bounded sequences. For \(u\in\mathcal S'\) there are \(C,N\) with \(|u(h_\alpha)|\le C(1+|\alpha|)^N\), and \(u(\varphi)=\sum_\alpha c_\alpha(\varphi)u(h_\alpha)\) for every \(\varphi\in\mathcal S\), with absolute convergence. Conversely, a polynomially bounded sequence \((b_\alpha)\) defines a unique tempered distribution by \(u_b(\varphi)=\sum_\alpha c_\alpha(\varphi)b_\alpha\). Thus an arbitrary linear functional on \(\mathcal S\) is continuous if and only if it has this series representation for some polynomially bounded sequence.

*Proof.* First let \(u\in\mathcal S'\). Since the norms \(\|\cdot\|_N\) increase and define the topology, continuity gives \(|u(\varphi)|\le C\|\varphi\|_N\) for some \(C,N\). Indeed, a basic neighbourhood on which \(|u|<1\) contains a ball for one of these increasing norms, and rescaling gives the bound. Consequently \(|u(h_\alpha)|\le C(2|\alpha|+n)^N\). Conversely, if \(|b_\alpha|\le C(1+|\alpha|)^N\), then \(|\sum_\alpha c_\alpha(\varphi)b_\alpha|\le C\sum_\alpha(1+|\alpha|)^{-n-1}\sup_\alpha(1+|\alpha|)^{N+n+1}|c_\alpha(\varphi)|\le C'\|\varphi\|_{N+n+1}\) by (1.3), so \(\varphi\mapsto\sum_\alpha c_\alpha(\varphi)b_\alpha\) is continuous. A continuous \(u\) agrees with this functional for \(b_\alpha=u(h_\alpha)\), because the series of Theorem 3.2(2) converges in \(\mathcal S\). \(\square\)

**Corollary 4.2** (Fourier transform on \(\mathcal S\) and \(\mathcal S'\)). \(\mathcal F\) maps \(\mathcal S\) onto \(\mathcal S\) as a topological isomorphism, with \(c_\alpha(\mathcal F\varphi)=(2\pi)^{n/2}(-i)^{|\alpha|}c_\alpha(\varphi)\), the inverse \(\varphi(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}\mathcal F\varphi(\xi)\,d\xi\), and \(\|\mathcal F\varphi\|_2=(2\pi)^{n/2}\|\varphi\|_2\). The formula \((\mathcal Fu)(\varphi)=u(\mathcal F\varphi)\) defines an isomorphism of \(\mathcal S'\), which agrees with the Fourier transform on integrable functions.

*Proof.* By Lemma 3.1, \(\|h_\alpha\|_1\le\|(1+|x|^2)^{-n}\|_2\|(1+|x|^2)^nh_\alpha\|_2\le C(1+|\alpha|)^n\), so for \(\varphi\in\mathcal S\) the series \(\sum_\alpha c_\alpha(\varphi)h_\alpha\) converges in \(L^1\), and \(\mathcal F\varphi=\sum_\alpha c_\alpha(\varphi)\mathcal Fh_\alpha\) uniformly. Proposition 2.2 and Theorem 3.2 give the coefficient formula, the isomorphism, the norm identity (Parseval) and the inverse, which multiplies coefficients by \((2\pi)^{-n/2}i^{|\alpha|}\) and is the stated integral by the computation in Lemma 3.1. The transpose of an isomorphism of \(\mathcal S\) is an isomorphism of \(\mathcal S'\). For integrable \(f\) and \(\varphi\in\mathcal S\), Fubini gives \(\int(\mathcal Ff)\varphi=\int f\,\mathcal F\varphi\). \(\square\)

## 5. The Schwartz kernel theorem

For \(\psi\in\mathcal S(\mathbb R^m)\) and \(\varphi\in\mathcal S(\mathbb R^n)\) write \((\psi\otimes\varphi)(y,x)=\psi(y)\varphi(x)\). The Hermite functions of \(\mathbb R^{m+n}\) are \(h_\alpha\otimes h_\beta\), and \(c_{(\alpha,\beta)}(\psi\otimes\varphi)=c_\alpha(\psi)c_\beta(\varphi)\); so \(\psi\otimes\varphi\in\mathcal S(\mathbb R^{m+n})\) by Theorem 3.2(2).

**Theorem 5.1** (Schwartz). Let \(T:\mathcal S(\mathbb R^n)\to\mathcal S'(\mathbb R^m)\) be linear and continuous for the topology of pointwise convergence on \(\mathcal S'\). There is exactly one \(K\in\mathcal S'(\mathbb R^{m+n})\) with
\[
(T\varphi)(\psi)=K(\psi\otimes\varphi)\qquad(\varphi\in\mathcal S(\mathbb R^n),\ \psi\in\mathcal S(\mathbb R^m)).
\]
Conversely, every \(K\in\mathcal S'(\mathbb R^{m+n})\) defines such a map.

*Proof.* Write \(B(\psi,\varphi)=(T\varphi)(\psi)\), and use the norms \(\|\cdot\|_N\) on both spaces. *A joint bound.* For \(k\ge1\) let \(E_k\) be the set of \(\varphi\in\mathcal S(\mathbb R^n)\) with \(|B(\psi,\varphi)|\le k\|\psi\|_k\) for every \(\psi\). It is closed, because \(\varphi\mapsto B(\psi,\varphi)\) is continuous for each \(\psi\). Every \(\varphi\) lies in some \(E_k\), because \(T\varphi\in\mathcal S'\) satisfies \(|B(\psi,\varphi)|\le C\|\psi\|_N\) (Theorem 4.1) and the norms increase. By Theorem 3.2(3) and the Baire category theorem, some \(E_k\) contains a ball \(\{\varphi:\|\varphi-\varphi_0\|_{k'}<r\}\). For \(\|\varphi\|_{k'}<r\), both \(\varphi_0+\varphi\) and \(\varphi_0\) lie in \(E_k\), so \(|B(\psi,\varphi)|\le2k\|\psi\|_k\). By homogeneity,
\[
|B(\psi,\varphi)|\le\tfrac{2k}r\,\|\psi\|_k\,\|\varphi\|_{k'}\qquad\text{for all }\psi,\varphi .
\]
*The kernel.* Put \(b_{\alpha\beta}=B(h_\alpha,h_\beta)\). Then \(|b_{\alpha\beta}|\le C(2|\alpha|+m)^k(2|\beta|+n)^{k'}\le C'(1+|\alpha|+|\beta|)^{k+k'}\), a polynomially bounded sequence on \(\mathbb N^{m+n}\). By Theorem 4.1 there is a unique \(K\in\mathcal S'(\mathbb R^{m+n})\) with \(K(h_\alpha\otimes h_\beta)=b_{\alpha\beta}\), and
\[
K(\psi\otimes\varphi)=\sum_{\alpha,\beta}c_\alpha(\psi)c_\beta(\varphi)b_{\alpha\beta}=\sum_\beta c_\beta(\varphi)B(\psi,h_\beta)=B(\psi,\varphi),
\]
using Theorem 4.1 for \(T h_\beta\) and the continuity of \(B\) in \(\varphi\); the double series converges absolutely by the joint bound. Uniqueness: \(K\) is determined by its values on the \(h_\alpha\otimes h_\beta\).

*Converse.* For \(K\in\mathcal S'(\mathbb R^{m+n})\), \(|K(\psi\otimes\varphi)|\le C\|\psi\otimes\varphi\|_N\), and \((2|\alpha|+2|\beta|+m+n)^N\le(2|\alpha|+m)^N(2|\beta|+n)^N2^N\) gives \(\|\psi\otimes\varphi\|_N\le2^N\|\psi\|_N\|\varphi\|_N\). So \(\psi\mapsto K(\psi\otimes\varphi)\) lies in \(\mathcal S'(\mathbb R^m)\) and depends continuously on \(\varphi\). \(\square\)

## 6. Tempered solutions of the Bott oscillator

Let \(\Lambda\) be the exterior algebra of \(\mathbb C^n\) with the basis \(e_J\), the operators \(\varepsilon_j\), \(\iota_j\) and the degree operator \(\mathcal N\), and let \(\mathcal D=\sum_jA_j\varepsilon_j+\sum_jA_j^\dagger\iota_j\) and \(P=\mathcal D\) on even forms, as in Sections 3 and 4 of the lesson on the Bott operator. Differential operators with polynomial coefficients act on \(\mathcal S'\) by transposition, and \(\mathcal D^2=\sum_jA_j^\dagger A_j+2\mathcal N\) there (Lemma 4.1 of that lesson).

**Proposition 6.1.** If \(u\in\mathcal S'(\mathbb R^n)\otimes\Lambda^e\) and \(Pu=0\), then \(u=c\,e^{-|x|^2/2}\) for a constant \(c\), regarded as a form of degree \(0\). In particular \(u\) is a Schwartz function.

*Proof.* \(\mathcal D^2u=\mathcal D(Pu)=0\). The operator \(\sum_jA_j^\dagger A_j+2\mathcal N\) is its own transpose on \(\mathcal S\otimes\Lambda\) and multiplies \(h_\alpha e_J\) by \(2|\alpha|+2|J|\) (Proposition 2.1(2) and \(\mathcal Ne_J=|J|e_J\)). Writing \(u=\sum_Ju_Je_J\), we get \((2|\alpha|+2|J|)\,u_J(h_\alpha)=0\) for all \(\alpha\) and \(J\). So \(u_J(h_\alpha)=0\) unless \(\alpha=0\) and \(J=\emptyset\), and by Theorem 4.1, \(u_\emptyset=c_0h_0\) and the other \(u_J\) vanish. \(\square\)

## 7. Exercises

**Exercise 7.1.** Compute \(h_1\) and \(h_2\).

*Solution.* \(h_1=2^{-1/2}A^\dagger h_0=\sqrt2\,\pi^{-1/4}xe^{-x^2/2}\), and \(h_2=(8)^{-1/2}(A^\dagger)^2h_0=2^{-1/2}\pi^{-1/4}(2x^2-1)e^{-x^2/2}\).

**Exercise 7.2.** Show that \(\delta_0(\varphi)=\varphi(0)\) is a tempered distribution with \(|\delta_0(h_\alpha)|\le C(1+|\alpha|)^M\), and compute \(\mathcal F\delta_0\).

*Solution.* Point evaluation is linear and satisfies \(|\delta_0(\varphi)|\le p_{0,0}(\varphi)\), so it is continuous on \(\mathcal S\) and hence is a tempered distribution. Its coefficients satisfy \(|\delta_0(h_\alpha)|=|h_\alpha(0)|\le p_{0,0}(h_\alpha)\le C(1+|\alpha|)^M\) by Lemma 3.1, and Theorem 4.1 gives its series representation. Finally \((\mathcal F\delta_0)(\varphi)=\mathcal F\varphi(0)=\int\varphi\), so \(\mathcal F\delta_0\) is the constant function \(1\).

**Exercise 7.3.** Show that \(L=-\Delta+|x|^2\) is an isomorphism of \(\mathcal S\) onto itself.

*Solution.* \(c_\alpha(L\varphi)=(2|\alpha|+n)c_\alpha(\varphi)\), and division by \(2|\alpha|+n\ge1\) preserves rapid decrease; Theorem 3.2 gives the inverse and its continuity.

## Where this leads

The lessons [Totally characteristic operators on the half space](course:totally-characteristic-operators/totally-characteristic-operators-on-the-half-space) and [The Bott operator, suspension, and reduction of the index to Euclidean space](the-bott-operator-suspension-and-reduction-of-the-index-to-euclidean-space.md) use the Fourier transform on \(\mathcal S'\), the kernel theorem and Proposition 6.1.

## References

- [Schwartz 1952] L. Schwartz, Théorie des noyaux, in *Proceedings of the International Congress of Mathematicians*, Cambridge, Massachusetts, 1950, Volume 1, American Mathematical Society, Providence, 1952, 220–230; [free at the International Mathematical Union](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1950.1/ICM1950.1.ocr.pdf).
- [Simon 1971] B. Simon, Distributions and their Hermite expansions, *Journal of Mathematical Physics* 12 (1971), 140–148, [doi:10.1063/1.1665472](https://doi.org/10.1063/1.1665472). Free from the author at https://math.caltech.edu/SimonPapers/12.pdf
