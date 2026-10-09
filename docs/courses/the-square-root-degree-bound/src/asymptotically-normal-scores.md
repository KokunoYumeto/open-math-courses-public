# Asymptotically normal scores

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The constructions of this course group many independent copies of an observation and feed the normalized scores into a fixed rule designed for Gaussian inputs. This lesson proves the probability facts that justify the Gaussian design: the central limit theorem in the form used (Section 1), convergence of restricted moments (Section 2), convergence of probabilities and restricted sums for sets with Gaussian-null boundary under independent copies (Section 3), and two perturbation statements (Section 4). Notation is that of [Linear Fourier coefficients and degree](linear-fourier-coefficients-and-degree.md). Throughout, \(G\) is standard normal, \(\Phi\) its distribution function, and \(\gamma\) the standard Gaussian measure on \(\mathbb R^q\).

## 1. Asymptotic normality

A sequence of real random variables \(Z_n\) is *asymptotically standard normal* if
\[
\delta_n=\sup_{x\in\mathbb R}\bigl|\Pr(Z_n\le x)-\Phi(x)\bigr|\longrightarrow0 .
\]
Then also \(\sup_x|\Pr(Z_n<x)-\Phi(x)|\le\delta_n\), by letting \(y\uparrow x\) in \(\Pr(Z_n\le y)\), and \(\Pr(Z_n=x)\le2\delta_n\) for every \(x\).

**Theorem 1.1** (Central limit theorem). Let \(X_1,X_2,\dots\) be independent, identically distributed, with mean \(0\) and finite variance \(\sigma^2>0\). Then \((X_1+\dots+X_M)/(\sigma\sqrt M)\) is asymptotically standard normal as \(M\to\infty\).

This is the core-course result *Measure and Integration*, Fremlin's *Measure Theory*, Volume 2, Corollary 274I, which gives exactly this uniform convergence of distribution functions.

**Lemma 1.2** (Fourth moments of averages). Let \(T_1,\dots,T_M\) be independent copies of a bounded random variable \(T\) with mean \(0\) and variance \(v>0\), and \(Z_M=(T_1+\dots+T_M)/\sqrt{Mv}\). Then
\[
\mathbb EZ_M^4=\frac{\mathbb ET^4}{Mv^2}+3\,\frac{M-1}M .
\]

*Proof.* Expanding \((T_1+\dots+T_M)^4\), the terms with a single factor of some \(T_i\) have mean zero; there remain \(M\) terms \(T_i^4\) and \(3M(M-1)\) terms \(T_i^2T_j^2\), \(i\ne j\). Divide by \(M^2v^2\). \(\square\)

## 2. Restricted moments

**Lemma 2.1** (Restricted moments). Let \(Z_n\) be asymptotically standard normal with \(\mathbb EZ_n=0\) and \(\mathbb EZ_n^2=1\). For every finite union \(J\) of intervals (bounded or not, with any endpoint conventions) and \(a\in\{0,1,2\}\),
\[
\mathbb E\bigl[\mathbf 1_J(Z_n)Z_n^a\bigr]\longrightarrow\mathbb E\bigl[\mathbf 1_J(G)G^a\bigr].
\]
In particular \(\mathbb E|Z_n|\to\mathbb E|G|=\sqrt{2/\pi}\).

The proof uses only the normalization \(\mathbb EZ_n^2=1\); no bound on higher moments is needed.

*Proof.* By additivity it suffices to treat one interval. Let it have finite endpoints \(\alpha\le\beta\). For \(a=0\), the probabilities differ from \(\Phi(\beta)-\Phi(\alpha)\) by at most \(2\delta_n\). For \(a\ge1\) and \(\psi(x)=x^a\), writing \(\psi(z)=\psi(\beta)-\int_z^\beta\psi'(x)\,dx\) for \(z\in(\alpha,\beta]\) and using Fubini's theorem,
\[
\mathbb E\bigl[\psi(Z)\mathbf 1_{(\alpha,\beta]}(Z)\bigr]=\psi(\beta)F(\beta)-\psi(\alpha)F(\alpha)-\int_\alpha^\beta\psi'(x)F(x)\,dx
\]
for every random variable \(Z\) with distribution function \(F\). Hence the expectations for \(Z_n\) and \(G\) differ by at most \(\bigl(|\psi(\alpha)|+|\psi(\beta)|+\int_\alpha^\beta|\psi'|\bigr)\delta_n\); the other endpoint conventions add atoms of size at most \(\max(|\alpha|,|\beta|)^a\cdot2\delta_n\). For an unbounded interval, cut it at \(\pm K\). The remaining parts satisfy \(\Pr(|Z_n|>K)\le K^{-2}\) and \(\mathbb E[|Z_n|\mathbf 1_{\{|Z_n|>K\}}]\le K^{-1}\mathbb EZ_n^2=K^{-1}\), uniformly in \(n\). For \(a=2\), the bounded case and \(\mathbb EZ_n^2=1=\mathbb EG^2\) give
\[
\mathbb E\bigl[Z_n^2\mathbf 1_{\{|Z_n|>K\}}\bigr]=1-\mathbb E\bigl[Z_n^2\mathbf 1_{\{|Z_n|\le K\}}\bigr]\longrightarrow1-\mathbb E\bigl[G^2\mathbf 1_{\{|G|\le K\}}\bigr]=\mathbb E\bigl[G^2\mathbf 1_{\{|G|>K\}}\bigr],
\]
which is small for large \(K\). The Gaussian tails are small as well. Letting \(n\to\infty\) and then \(K\to\infty\) gives the claim. Finally \(\mathbb E|Z_n|=\mathbb E[Z_n\mathbf 1_{(0,\infty)}(Z_n)]-\mathbb E[Z_n\mathbf 1_{(-\infty,0]}(Z_n)]\). \(\square\)

**Corollary 2.2** (Product functions). Let \(Z_n\) be as in Lemma 2.1, and let \(\mathbf Z_n=(Z_{n,1},\dots,Z_{n,q})\) consist of independent copies. If \(g(z)=\prod_{k=1}^q\mathbf 1_{J_k}(z_k)z_k^{a_k}\) with finite unions of intervals \(J_k\) and exponents \(a_k\in\{0,1,2\}\), then \(\mathbb Eg(\mathbf Z_n)\to\mathbb Eg(\mathbf G)\), where \(\mathbf G\) has independent standard normal coordinates. The same holds for finite linear combinations of such functions.

*Proof.* By independence, \(\mathbb Eg(\mathbf Z_n)=\prod_k\mathbb E[\mathbf 1_{J_k}(Z_n)Z_n^{a_k}]\), and each factor converges by Lemma 2.1. \(\square\)

## 3. Sets with Gaussian-null boundary

**Lemma 3.1** (Product portmanteau). Let \(Z_n\) be asymptotically standard normal with mean \(0\) and variance \(1\), let \(\mathbf Z_n\) consist of \(q\) independent copies, \(S_n\) their sum, and \(S_G\) the sum of the coordinates of \(\mathbf G\). If \(E\subseteq\mathbb R^q\) is a Borel set with \(\gamma(\partial E)=0\), then
\[
\Pr(\mathbf Z_n\in E)\to\gamma(E),\qquad\mathbb E[S_n\mathbf 1_E(\mathbf Z_n)]\to\mathbb E[S_G\mathbf 1_E(\mathbf G)] .
\]

*Proof.* Fix \(\varepsilon>0\). Choose \(M\) with \(\gamma(\mathbb R^q\setminus Q)<\varepsilon\) and \(q/M^2<\varepsilon\), where \(Q=[-M,M)^q\); by Chebyshev's inequality \(\Pr(\mathbf Z_n\notin Q)\le q/M^2<\varepsilon\). Cut \(Q\) into half-open cubes ("boxes") of side \(\delta\). As \(\delta\downarrow0\), the union of the boxes whose closures meet \(\partial E\) is contained in the closed \(\sqrt q\,\delta\)-neighbourhood of \(\partial E\cap[-M-1,M+1]^q\), and these neighbourhoods decrease to \(\partial E\cap[-M-1,M+1]^q\), which is \(\gamma\)-null; so we may choose \(\delta\) with \(\gamma(\mathcal B)<\varepsilon\), where \(\mathcal B\) is the union of these boxes. A box whose closure misses \(\partial E\) is connected, so it lies in the interior of \(E\) or in the interior of its complement. Let \(\mathcal I\) be the finite set of boxes inside \(E\). Then \(E\) differs from \(\bigcup\mathcal I\) by a subset of \(\mathcal B\cup(\mathbb R^q\setminus Q)\).

The probability that \(\mathbf Z_n\) lies in a box is a product of \(q\) interval probabilities, so it converges to the Gaussian value by Lemma 2.1; there are finitely many boxes. Hence \(\Pr(\mathbf Z_n\in\bigcup\mathcal I)\to\gamma(\bigcup\mathcal I)\) and \(\Pr(\mathbf Z_n\in\mathcal B)\to\gamma(\mathcal B)<\varepsilon\), so \(\limsup_n|\Pr(\mathbf Z_n\in E)-\gamma(E)|\le4\varepsilon\).

For the restricted sums, \(S\) varies by at most \(q\delta\) on a box, so with \(c_b\) the centre of box \(b\),
\[
\Bigl|\mathbb E[S_n\mathbf 1_E(\mathbf Z_n)]-\sum_{b\in\mathcal I}S(c_b)\Pr(\mathbf Z_n\in b)\Bigr|\le q\delta+\sqrt q\,\Pr\bigl(\mathbf Z_n\in\mathcal B\cup(\mathbb R^q\setminus Q)\bigr)^{1/2},
\]
using Cauchy–Schwarz and \(\mathbb ES_n^2=q\) for the exceptional part; the same holds for \(\mathbf G\). The sums over \(\mathcal I\) converge, and the right-hand sides are eventually at most \(q\delta+\sqrt{3q\varepsilon}\). As \(\varepsilon\) and then \(\delta\) can be taken small, the claim follows. \(\square\)

## 4. Two perturbations

**Lemma 4.1.** (a) If \(X_n\) is asymptotically standard normal and \(\mathbb E(Y_n-X_n)^2\to0\), then \(Y_n\) is asymptotically standard normal. (b) If \(X_n\) is asymptotically standard normal and \(c_n\to1\), then \(c_nX_n\) is asymptotically standard normal.

*Proof.* (a) For \(\varepsilon>0\), \(\Pr(Y_n\le x)\le\Pr(X_n\le x+\varepsilon)+\Pr(|Y_n-X_n|>\varepsilon)\le\Phi(x+\varepsilon)+\delta_n+\varepsilon^{-2}\mathbb E(Y_n-X_n)^2\), and similarly from below with \(x-\varepsilon\). Since \(\Phi\) is uniformly continuous, \(\sup_x|\Pr(Y_n\le x)-\Phi(x)|\) is eventually as small as we like. (b) For \(c_n>0\), \(\Pr(c_nX_n\le x)=\Pr(X_n\le x/c_n)\), which is within \(\delta_n\) of \(\Phi(x/c_n)\), and \(\sup_x|\Phi(x/c_n)-\Phi(x)|\to0\) as \(c_n\to1\). \(\square\)

**Lemma 4.2** (Law of large numbers). If \(Y_1,Y_2,\dots\) are independent copies of a bounded random variable with mean \(\mu\), then \(\Pr\bigl(|\frac1K\sum_{b\le K}Y_b-\mu|\ge\varepsilon\bigr)\to0\) as \(K\to\infty\), for every \(\varepsilon>0\).

*Proof.* The average has variance \(\operatorname{Var}(Y_1)/K\); apply Chebyshev's inequality. \(\square\)

## 5. Exercises

**5.1.** Let \(Z_n\) be the normalized sum of \(n\) independent uniform signs. Check Lemma 1.2 directly for \(T=X_1\), and compute \(\mathbb E|Z_2|\) and \(\mathbb E|Z_4|\).

**5.2.** Show that the normalization \(\mathbb EZ_n^2=1\) cannot be dropped in Lemma 2.1 for \(a=2\): give centered, asymptotically standard normal \(Z_n\) with \(\mathbb EZ_n^2\to2\).

**5.3.** Give a set \(E\subseteq\mathbb R\) with \(\gamma(\partial E)>0\) and asymptotically standard normal \(Z_n\) with \(\Pr(Z_n\in E)\not\to\gamma(E)\).

## 6. Solutions

**5.1.** For \(T=X_1\), \(\mathbb ET^4=1=v\), so \(\mathbb EZ_M^4=\frac1M+3\frac{M-1}M=3-\frac2M\); for \(M=2\), \(Z_2\in\{0,\pm\sqrt2\}\) with probabilities \(\frac12,\frac14,\frac14\), and \(\mathbb EZ_2^4=4\cdot\frac12=2=3-1\). Also \(\mathbb E|Z_2|=\sqrt2/2\approx0.707\) and, with \(Z_4\in\{0,\pm1,\pm2\}\) having probabilities \(\frac38,\frac14\cdot2,\frac1{16}\cdot2\), \(\mathbb E|Z_4|=\frac12+\frac14=0.75\); both approach \(\sqrt{2/\pi}\approx0.798\).

**5.2.** Let \(Z_n\) equal a standard normal variable with probability \(1-\frac1n\) and \(\pm\sqrt n\) with probability \(\frac1{2n}\) each. It is centered, and \(\mathbb EZ_n^2=(1-\frac1n)+1\to2\). Its distribution function differs from \(\Phi\) by at most \(\frac2n\) everywhere, so it is asymptotically standard normal; but \(\mathbb E[Z_n^2\mathbf 1_{\{|Z_n|>K\}}]\ge1\) for \(n>K^2\), so the restricted second moments do not converge to the Gaussian ones.

**5.3.** Take \(E=\mathbb Q\), whose boundary is \(\mathbb R\), and \(Z_n\) the normalized sum of \(n\) independent uniform signs, asymptotically standard normal by Theorem 1.1. For \(n=k^2\), every value \((n-2j)/k\) is rational, so \(\Pr(Z_n\in\mathbb Q)=1\), while \(\gamma(\mathbb Q)=0\).

## References

- [OpenAI-SR] OpenAI, *Unbounded violations of the square-root degree bound*, OpenAI Math Release preprint, 26 September 2026. https://github.com/openai/math/blob/main/preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/paper.pdf
- Core course *Measure and Integration*: D. H. Fremlin, *Measure Theory*, Volume 2, Section 274 (the central limit theorem).
