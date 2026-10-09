# Weighted moments and sampling

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson turns the upper bound of Theorem 5.1 of [Finite subsets of L_p](finite-subsets-of-lp.md) into a question about one random vector. A coordinate of an embedding is a real label \(z_i\) for each point \(x_i\); what matters is the *normalized gradient* \(\bigl((z_i-z_j)/\|x_i-x_j\|_p\bigr)\) on the pairs. If a random normalized gradient has the same \(p\)-th moment \(b\) on every pair, then independent copies of it, used as coordinates, give an embedding of distortion close to \(1\) once there are enough of them (Lemma 3.1). OpenAI's argument [OpenAI-LP, Section 3] shows by convex separation that it is enough to make the moments nearly equal *on average* for each weighting of the pairs, with the size bound \(K\) and the moment \(b\) independent of the weighting. The sampling step is an instance of Maurey's empirical method [Pisier].

## 1. Normalized gradients

By Proposition 2.1 of [Finite subsets of L_p](finite-subsets-of-lp.md) we may fix distinct points \(x_1,\dots,x_n\) in some \(\ell_p^m\). Let \(E\) be the set of pairs \(e=ij\) with \(i<j\), oriented from \(i\) to \(j\), and \(\delta_e=\|x_i-x_j\|_p>0\). The space of *normalized gradients* is
\[
V=\Bigl\{\Bigl(\frac{z_i-z_j}{\delta_e}\Bigr)_{e=ij\in E}:z\in\mathbb R^n\Bigr\}\subseteq\mathbb R^E .
\]
It is a linear subspace. The labels of an element of \(V\) are determined up to adding a constant, since the pairs connect all points; normalizing \(z_n=0\) makes them a linear function of the gradient. So finitely many normalized gradients \(F^{(1)},\dots,F^{(d)}\) are the coordinate differences of one map \(x_i\mapsto(z^{(1)}_i,\dots,z^{(d)}_i)\). For a probability vector \(\sigma=(\sigma_e)\) with positive entries let \(\|f\|_{2,\sigma}^2=\sum_e\sigma_e|f_e|^2\).

## 2. Sums of bounded variables

**Lemma 2.1.** Let \(X_1,\dots,X_d\) be independent copies of a random variable \(X\) with \(0\le X\le R\), and let \(\epsilon>0\). Then
\[
\mathbb P\Bigl(\Bigl|\frac1d\sum_{a=1}^dX_a-\mathbb EX\Bigr|>\epsilon\Bigr)\le2\exp\Bigl(-\frac{d\epsilon^2}{2R^2}\Bigr).
\]

**Proof.** Let \(X'\) be an independent copy of \(X\) and \(t>0\). By Jensen's inequality \(\mathbb Ee^{-tX'}\ge e^{-t\mathbb EX}\), so \(\mathbb Ee^{t(X-\mathbb EX)}\le\mathbb Ee^{t(X-X')}\). The variable \(X-X'\) is symmetric with \(|X-X'|\le R\), so \(\mathbb Ee^{t(X-X')}=\mathbb E\cosh(t(X-X'))\le e^{t^2R^2/2}\), using \(\cosh u\le e^{u^2/2}\). By independence and Markov's inequality,
\[
\mathbb P\Bigl(\sum_a(X_a-\mathbb EX)>d\epsilon\Bigr)\le e^{-td\epsilon}e^{dt^2R^2/2}=e^{-d\epsilon^2/(2R^2)}
\]
for \(t=\epsilon/R^2\). The lower tail is the same with \(-X\). \(\square\)

This is a weak form of Hoeffding's inequality, enough here.

## 3. The weighted moment criterion

**Lemma 3.1** (OpenAI). Let \(0<\eta<\frac13\) and \(b,K\ge1\). Suppose that for every probability vector \(\lambda\) on \(E\) with positive entries there is a random \(F\) with values in \(V\) such that
\[
\|F\|_\infty\le K\ \text{almost surely},\qquad\sum_{e\in E}\lambda_e\bigl|\mathbb E|F_e|^p-b\bigr|\le\eta b,\tag{3.1}
\]
where \(b\) and \(K\) do not depend on \(\lambda\). Then the points embed into \(\ell_p^d\) with distortion at most \(\bigl(\frac{1+3\eta}{1-3\eta}\bigr)^{1/p}\) for some
\[
d\le\Bigl\lceil C\max\Bigl\{1,\frac{K^{2p}}{\eta^2b^2}\Bigr\}\log(2n)\Bigr\rceil,\tag{3.2}
\]
with an absolute constant \(C\).

**Proof.** *One distribution for all pairs.* The set \(\mathcal G=\{f\in V:\|f\|_\infty\le K\}\) is compact, so the set of vectors \(\bigl(|f_e|^p\bigr)_e\), \(f\in\mathcal G\), is compact, and its convex hull \(\mathcal C\) is compact by Lemma 1.2 of [Finite subsets of L_p](finite-subsets-of-lp.md). By Lemma 1.4 there, the moment vector \(\bigl(\mathbb E|F_e|^p\bigr)_e\) of every random \(F\) with values in \(\mathcal G\) lies in \(\mathcal C\). Let \(\overline{\mathcal B}\) be the closed box of vectors \(m\) with \(|m_e-b|\le2\eta b\) for all \(e\). We claim that \(\mathcal C\) meets \(\overline{\mathcal B}\). Otherwise, Lemma 1.3 there gives \(a\neq0\), which we normalize by \(\sum_e|a_e|=1\), with \(\min_{m\in\mathcal C}a\cdot m>\max_{\beta\in\overline{\mathcal B}}a\cdot\beta=b\sum_ea_e+2\eta b\), that is,
\[
\sum_ea_e(m_e-b)>2\eta b\qquad(m\in\mathcal C).
\]
Apply the hypothesis with \(\lambda_e=\frac34|a_e|+\frac1{4|E|}\), a probability vector with positive entries; its moment vector \(m\in\mathcal C\) satisfies
\[
\sum_ea_e(m_e-b)\le\sum_e|a_e|\,|m_e-b|\le\frac43\sum_e\lambda_e|m_e-b|\le\frac43\eta b,
\]
a contradiction. So some \(m\in\mathcal C\) has \(|m_e-b|\le2\eta b\) for every \(e\). By definition of the convex hull, \(m=\sum_c\theta_c\bigl(|f^{(c)}_e|^p\bigr)_e\) for finitely many \(f^{(c)}\in\mathcal G\) and convex weights \(\theta_c\); the random gradient \(F\) equal to \(f^{(c)}\) with probability \(\theta_c\) has \(\bigl|\mathbb E|F_e|^p-b\bigr|\le2\eta b\) for every pair.

*Sampling.* Let \(F^{(1)},\dots,F^{(d)}\) be independent copies of this \(F\). For each pair, \(X=|F_e|^p\) satisfies \(0\le X\le K^p\), so by Lemma 2.1 with \(\epsilon=\eta b\) the empirical mean \(\frac1d\sum_a|F^{(a)}_e|^p\) differs from \(\mathbb E|F_e|^p\) by more than \(\eta b\) with probability at most \(2e^{-d\eta^2b^2/(2K^{2p})}\). There are fewer than \(n^2/2\) pairs, so for \(d\) as in (3.2) with \(C\) large enough, the union bound leaves an outcome in which every empirical mean lies in \([(1-3\eta)b,(1+3\eta)b]\). Let \(z^{(a)}\) be labels of \(F^{(a)}\) and \(y_i=d^{-1/p}\bigl(z^{(1)}_i,\dots,z^{(d)}_i\bigr)\in\ell_p^d\). Then
\[
\frac{\|y_i-y_j\|_p^p}{\delta_{ij}^p}=\frac1d\sum_{a=1}^d|F^{(a)}_{ij}|^p\in\bigl[(1-3\eta)b,(1+3\eta)b\bigr],
\]
which is (0.1) of [Finite subsets of L_p](finite-subsets-of-lp.md) with \(s=((1-3\eta)b)^{1/p}\) and the stated distortion. \(\square\)

The moment \(b\) may be as large as we like: multiplying all distances by one factor does not change the distortion. This freedom absorbs additive errors later.

## 4. What the constructions must deliver

Fix \(1<p<\infty\), \(p\neq2\), and \(D>1\), and choose \(0<\eta<\frac16\) with
\[
\Bigl(\frac{1+3\eta}{1-3\eta}\Bigr)^{1/p}\le D.\tag{4.1}
\]

**Proposition 4.1.** Suppose there are \(n_0\) and \(C_0\), depending only on \(p\) and \(D\), such that for every \(n\ge n_0\) and every \(n\) distinct points of every \(\ell_p^m\) the hypothesis of Lemma 3.1 holds with some \(b,K\ge1\) and \(\log K\le C_0(\log n)^{\gamma(p)}\). Then the upper bound of Theorem 5.1 of [Finite subsets of L_p](finite-subsets-of-lp.md) holds.

**Proof.** For \(n\ge n_0\), Lemma 3.1 gives distortion at most \(D\) by (4.1), and since \(b\ge1\),
\[
\log d\le C_1+2p\log K+\log\log(2n)\le C_{p,D}(\log n)^{\gamma(p)},
\]
because \(\log\log n\) is small compared with \((\log n)^{\gamma(p)}\) for large \(n\). For the finitely many \(n<n_0\), enlarge \(C_{p,D}\) and use Proposition 2.1 there; points of an arbitrary \(L_p\) space can first be moved isometrically into some \(\ell_p^m\) by the same proposition. \(\square\)

The constructions of [Signed Poisson sums and exponents below two](signed-poisson-sums-below-two.md) and [Truncation ramps and exponents above two](truncation-ramps-above-two.md) provide these parameters. Both use, for each weighting \(\lambda\), the projection of [Electrical flows and a weighted projection](electrical-flows-and-a-weighted-projection.md).

## 5. Exercises

**Exercise 5.1** (easy). Show that \(\dim V=n-1\).

**Exercise 5.2** (easy). Show that Lemma 2.1 with \(R=1\) and \(\epsilon=\frac1{10}\) guarantees, for \(d=1000\), that the average of \(d\) independent fair coin flips (values \(0,1\)) is within \(\frac1{10}\) of \(\frac12\) with probability at least \(1-2e^{-5}\).

**Exercise 5.3** (medium). In the proof of Lemma 3.1, why is the weighting \(\lambda_e=\frac34|a_e|+\frac1{4|E|}\) used instead of \(\lambda_e=|a_e|\)?

**Exercise 5.4** (medium). Show that the condition (3.1) for a single weighting does not suffice: for three points at equal mutual distances and \(\lambda_{23}\le\eta\), find \(F\in V\) with \(\sum_e\lambda_e\bigl|\mathbb E|F_e|^p-b\bigr|\le\eta b\) such that every embedding built from copies of \(F\) maps \(x_2\) and \(x_3\) to the same point.

## 6. Solutions

**5.1.** The map \(z\mapsto\bigl((z_i-z_j)/\delta_e\bigr)_e\) from \(\mathbb R^n\) has kernel the constants, since the pairs connect all points, so its image has dimension \(n-1\).

**5.2.** \(2\exp(-1000\cdot\frac1{100}/2)=2e^{-5}\).

**5.3.** The hypothesis requires a probability vector with positive entries, and \(|a|\) may have zero entries; the mixture with the uniform vector fixes this, at the price of the factor \(\frac43\) in \(|a_e|\le\frac43\lambda_e\).

**5.4.** Let \(\delta\) be the common distance and take the labels \(z=(\delta b^{1/p},0,0)\). Then \(F_{12}=F_{13}=b^{1/p}\) and \(F_{23}=0\), so the weighted error is \(\lambda_{23}b\le\eta b\). Every coordinate built from \(F\) gives \(x_2\) and \(x_3\) the same label. Lemma 3.1 needs (3.1) for every weighting, so that convex separation produces one distribution that is good on every pair.

## References

- [OpenAI-LP] OpenAI, *Subpolynomial dimension reduction in L_p*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026
- [Pisier] G. Pisier, *Remarques sur un résultat non publié de B. Maurey*, Séminaire d'analyse fonctionnelle 1980–1981, exposé 5 (open access). https://numdam.org/item/SAF_1980-1981____A5_0/
