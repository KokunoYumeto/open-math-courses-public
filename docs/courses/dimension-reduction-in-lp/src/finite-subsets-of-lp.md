# Finite subsets of L_p

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The Johnson–Lindenstrauss lemma places any \(n\) points of a Hilbert space into a Euclidean space of dimension \(O_D(\log n)\) with distortion at most \(D\), for every \(D>1\). Johnson and Lindenstrauss asked what happens in other spaces; for the spaces \(L_p\) the question is how many coordinates of \(\ell_p\) are needed to represent \(n\) points of \(L_p\) with small distortion [Naor]. This course presents OpenAI's answer [OpenAI-LP]: for every fixed \(1<p<\infty\) and \(D>1\), a number of coordinates that grows more slowly than every power of \(n\) suffices, while exact representation needs a number of order \(n^2\).

All spaces are real. For a measure space \((X,\mu)\), \(L_p(\mu)\) is the space of classes of measurable functions with \(\|x\|_p=(\int|x|^p\,d\mu)^{1/p}<\infty\), and \(\ell_p^d\) is \(\mathbb R^d\) with \(\|y\|_p=(\sum_a|y_a|^p)^{1/p}\). For \(1\le p<\infty\), an integer \(n\ge2\) and \(D\ge1\), let \(d_p(n,D)\) be the least integer \(d\) such that for every \(n\)-point subset \(\{x_1,\dots,x_n\}\) of every space \(L_p(\mu)\) there are \(y_1,\dots,y_n\in\ell_p^d\) and \(s>0\) with
\[
s\|x_i-x_j\|_p\le\|y_i-y_j\|_p\le Ds\|x_i-x_j\|_p\qquad(1\le i,j\le n).\tag{0.1}
\]
The images are arbitrary points; no linear map is required.

**Theorem 5.1** (OpenAI 2026). Let \(1<p<\infty\), \(p\neq2\), and \(\gamma(p)=2-p\) for \(p<2\), \(\gamma(p)=1-\frac2p\) for \(p>2\). For every \(D>1\) there is \(C_{p,D}<\infty\) such that for every \(n\ge2\)
\[
\frac{\log n}{\log(1+2D)}\le d_p(n,D)\le\exp\bigl(C_{p,D}(\log n)^{\gamma(p)}\bigr),
\]
while for \(D=1\) and \(n\ge9\)
\[
\Bigl\lfloor\frac{n-1}4\Bigr\rfloor^2\le d_p(n,1)\le\binom n2 .
\]
Hence \(\log d_p(n,D)/\log n\) tends to \(0\) for \(D>1\) and to \(2\) for \(D=1\).

**History.** Ball proved the exact bound \(\binom n2\) and its quadratic sharpness for \(1\le p<2\). Below \(2\), Schechtman showed that \(O_{p,D}(n)\) coordinates suffice [Schechtman]. Bourgain, Lindenstrauss and Milman, and Talagrand, preserved whole subspaces by linear maps, which for \(n\) points gives dimension at least of order \(n\). Linear maps can indeed need dimension proportional to \(n\) when \(p\neq2\) (Lee, Mendel and Naor); at \(p=1\), Brinkman and Charikar showed that dimension reduction fails even for nonlinear maps. For \(p>2\), Naor and Ren showed that \(O_{p,D}(\log n)\) coordinates are not enough [NR]. Theorem 5.1 gives subpolynomial dimension for \(1<p<\infty\); its exponent \(\gamma(p)\) is not claimed to be optimal.

This lesson proves everything in Theorem 5.1 except the upper bound for \(D>1\): the convexity tools used throughout (Section 1), the exact upper bound (Section 2), the counting lower bound (Section 3), and the quadratic lower bound for exact embeddings (Section 4). The upper bound is proved in the four following lessons, from [Weighted moments and sampling](weighted-moments-and-sampling.md) to [Truncation ramps and exponents above two](truncation-ramps-above-two.md).

## 1. Convexity in finite dimensions

**Lemma 1.1** (Carathéodory). If \(A\subseteq\mathbb R^N\) lies in an affine subspace of dimension \(k\), every point of the convex hull of \(A\) is a convex combination of at most \(k+1\) points of \(A\).

**Proof.** Let \(x=\sum_{a=1}^r\theta_aw_a\) with \(w_a\in A\), \(\theta_a>0\), \(\sum\theta_a=1\) and \(r\) minimal. If \(r>k+1\), the points \(w_a\) are affinely dependent: there are \(\beta_a\), not all zero, with \(\sum\beta_aw_a=0\) and \(\sum\beta_a=0\). Some \(\beta_a>0\); let \(t=\min\{\theta_a/\beta_a:\beta_a>0\}\). Then \(x=\sum(\theta_a-t\beta_a)w_a\) is a convex combination with a zero coefficient, against minimality. \(\square\)

**Lemma 1.2.** The convex hull of a compact set \(A\subseteq\mathbb R^N\) is compact.

**Proof.** By Lemma 1.1 it is the image of the compact set \(\Delta_N\times A^{N+1}\), where \(\Delta_N\) is the standard simplex of coefficients, under the continuous map \((\theta,w)\mapsto\sum\theta_aw_a\). \(\square\)

**Lemma 1.3** (separation). Let \(C\subseteq\mathbb R^N\) be compact, convex and nonempty.

1. If \(x\notin C\), there is \(a\in\mathbb R^N\) with \(a\cdot x>\max_{c\in C}a\cdot c\).
2. If \(C'\) is another compact convex set disjoint from \(C\), there is \(a\) with \(\min_{c\in C}a\cdot c>\max_{c'\in C'}a\cdot c'\).

**Proof.** 2. The continuous function \(|c-c'|\) on \(C\times C'\) attains a positive minimum at some \((c_0,c_0')\). Put \(a=c_0-c_0'\). For \(c\in C\) and \(0<t\le1\), the point \(c_0+t(c-c_0)\) lies in \(C\), so \(|c_0-c_0'+t(c-c_0)|^2\ge|a|^2\); expanding and letting \(t\to0\) gives \(a\cdot(c-c_0)\ge0\). Likewise \(a\cdot(c'-c_0')\le0\) for \(c'\in C'\). Hence \(a\cdot c\ge a\cdot c_0=a\cdot c_0'+|a|^2>a\cdot c'\). 1 is the case \(C'=\{x\}\). \(\square\)

**Lemma 1.4** (barycenters). Let \(C\subseteq\mathbb R^N\) be compact and convex, and let \(f\) be a measurable map from a probability space to \(C\). Then \(\mathbb Ef\in C\).

**Proof.** \(f\) is bounded, so \(\mathbb Ef\) exists. If \(\mathbb Ef\notin C\), Lemma 1.3 gives \(a\) with \(a\cdot\mathbb Ef>\max_Ca\cdot c\ge a\cdot f\) pointwise, and taking expectations gives \(a\cdot\mathbb Ef<a\cdot\mathbb Ef\). \(\square\)

## 2. Exact discretization

**Proposition 2.1** (Ball's bound). Let \(1\le p<\infty\). Every \(n\)-point subset of an \(L_p\) space embeds isometrically into \(\ell_p^{N}\), \(N=\binom n2\).

**Proof.** Let \(x_1,\dots,x_n\in L_p(\mu)\) be distinct, fix representatives, and let \(E\) be the set of pairs \(i<j\), so \(|E|=N\). Put \(q(t)=\bigl(|x_i(t)-x_j(t)|^p\bigr)_{ij\in E}\), \(s(t)=\sum_{e\in E}q_e(t)\) and \(S=\int s\,d\mu\), so \(0<S<\infty\). Let
\[
\mathcal K=\Bigl\{\bigl(|z_i-z_j|^p\bigr)_{ij\in E}:z\in\mathbb R^n,\ z_n=0,\ \sum_{ij\in E}|z_i-z_j|^p=1\Bigr\}.
\]
It is compact, since its parameters \(z\) form a closed set with \(|z_i|=|z_i-z_n|\le1\), and it lies in the affine hyperplane where the coordinates add up to \(1\). Where \(s(t)>0\), the vector \(q(t)/s(t)\) lies in \(\mathcal K\) (take \(z_i=(x_i(t)-x_n(t))/s(t)^{1/p}\)). By Lemma 1.4, applied to the probability measure \(s\,d\mu/S\) on \(\{s>0\}\) and the compact convex hull of \(\mathcal K\) (Lemma 1.2),
\[
\frac1S\int q\,d\mu=\int_{\{s>0\}}\frac{q}{s}\,\frac{s\,d\mu}S\in\operatorname{conv}\mathcal K .
\]
By Lemma 1.1, with \(k=N-1\), this vector is \(\sum_{a=1}^N\theta_a\bigl(|z^{(a)}_i-z^{(a)}_j|^p\bigr)_{ij}\) for some \(z^{(a)}\) and convex weights \(\theta_a\). The points \(y_i=\bigl((S\theta_a)^{1/p}z^{(a)}_i\bigr)_{a=1}^N\in\ell_p^N\) satisfy \(\|y_i-y_j\|_p^p=S\sum_a\theta_a|z^{(a)}_i-z^{(a)}_j|^p=\int|x_i-x_j|^p\,d\mu\). \(\square\)

In particular, for the upper bound of Theorem 5.1 we may assume that the points lie in some \(\ell_p^m\).

## 3. A counting lower bound

**Proposition 3.1.** For \(1\le p<\infty\) and \(D\ge1\), \(d_p(n,D)\ge\log n/\log(1+2D)\).

**Proof.** The \(n\) unit vectors of \(\ell_p^n\) are at mutual distance \(2^{1/p}\). Take images in \(\ell_p^d\) satisfying (0.1), and rescale them so that the smallest image distance is at least \(1\) and all image distances are at most \(D\). The open balls of radius \(\frac12\) about the images are disjoint and lie in the ball of radius \(D+\frac12\) about the first image. Lebesgue measure scales by \(r^d\) under \(y\mapsto ry\), so \(n(\frac12)^d\le(D+\frac12)^d\), that is, \(n\le(1+2D)^d\). \(\square\)

## 4. Exact embeddings need quadratically many coordinates

For real \(a,b\) let \(\Delta_p(a,b)=|a+b|^p+|a-b|^p-2|a|^p-2|b|^p\).

**Lemma 4.1.** Let \(1<p<\infty\), \(p\neq2\). If \(ab=0\), then \(\Delta_p(a,b)=0\); if \(ab\neq0\), then \(\Delta_p(a,b)\) is nonzero and has the sign of \(p-2\).

**Proof.** The case \(ab=0\) is direct. Let \(ab\neq0\) and \(r=p/2\). The numbers \((a+b)^2\) and \((a-b)^2\) have average \(a^2+b^2\). If \(r>1\), convexity of \(x\mapsto x^r\) gives \(\frac12(|a+b|^p+|a-b|^p)\ge(a^2+b^2)^r\), and \((a^2+b^2)^r>|a|^p+|b|^p\) because \((s+t)^r>s^r+t^r\) for \(s,t>0\) and \(r>1\). If \(r<1\), both inequalities reverse. \(\square\)

**Lemma 4.2.** Let \(1<p<\infty\), \(p\neq2\), and \(u,w\in\ell_p^d\). Then
\[
\|u+w\|_p^p+\|u-w\|_p^p=2\|u\|_p^p+2\|w\|_p^p
\]
if and only if \(u\) and \(w\) have disjoint supports.

**Proof.** The difference of the two sides is \(\sum_a\Delta_p(u_a,w_a)\), whose nonzero terms all have the sign of \(p-2\) by Lemma 4.1, and a term is nonzero exactly when \(u_aw_a\neq0\). \(\square\)

**Lemma 4.3.** Let \(1<p<\infty\) and let \(u,w\in\ell_p^d\) with \(\|u\|_p=\|w\|_p\) and \(\|u+w\|_p=2\|u\|_p\). Then \(u=w\).

**Proof.** We may assume \(\|u\|_p=1\). If \(u\neq w\), then \(u_a\neq w_a\) for some \(a\), and strict convexity of \(t\mapsto|t|^p\) gives \(\bigl|\frac{u_a+w_a}2\bigr|^p<\frac12(|u_a|^p+|w_a|^p)\), while the other coordinates satisfy the weak inequality. Summing, \(\|\frac{u+w}2\|_p^p<1\), a contradiction. \(\square\)

**Proposition 4.4** (OpenAI). Let \(1<p<\infty\), \(p\neq2\), and \(n\ge9\). Then \(d_p(n,1)\ge\lfloor\frac{n-1}4\rfloor^2\).

**Proof.** Let \(k=\lfloor\frac{n-1}4\rfloor\ge2\). In \(\ell_p^{k^2}\), with coordinates indexed by \(\{1,\dots,k\}^2\), let \(r_i\) be the indicator of row \(i\) and \(c_j\) that of column \(j\), and consider the \(4k+1\le n\) points \(\mathcal X=\{0\}\cup\{\pm r_i\}\cup\{\pm c_j\}\), completed by further distinct points to an \(n\)-point set. Suppose that \(\mathcal X\) embeds with distortion \(1\) into \(\ell_p^d\); after translation and rescaling, the embedding \(f\) is an isometry with \(f(0)=0\).

*Antipodes.* For \(x\in\mathcal X\), the vectors \(f(x)\) and \(-f(-x)\) both have norm \(\|x\|_p\), and their sum has norm \(\|f(x)-f(-x)\|_p=\|x-(-x)\|_p=2\|x\|_p\). By Lemma 4.3, \(f(-x)=-f(x)\).

*Supports.* For \(x,y\in\mathcal X\), \(\|f(x)+f(y)\|_p=\|f(x)-f(-y)\|_p=\|x+y\|_p\) and \(\|f(x)-f(y)\|_p=\|x-y\|_p\). So the expression of Lemma 4.2 for \(f(x),f(y)\) equals the one for \(x,y\). Different rows have disjoint supports, hence so do \(f(r_i)\) and \(f(r_{i'})\), and the same holds for columns. A row and a column meet in one coordinate, and their expression equals \((2k-2+2^p)+(2k-2)-4k=2^p-4\neq0\); hence the supports of \(f(r_i)\) and \(f(c_j)\) meet for every \(i,j\). A coordinate lies in at most one row support and at most one column support, so it accounts for at most one of these \(k^2\) intersections, and \(d\ge k^2\). \(\square\)

For \(p=2\) every \(n\) points lie isometrically in \(\ell_2^{n-1}\), and Lemma 4.1 fails because \(\Delta_2\equiv0\).

## 5. The theorem and the plan

Propositions 2.1, 3.1 and 4.4 prove all bounds of Theorem 5.1 except the upper bound for \(D>1\). The limits follow from the bounds, since \(0<\gamma(p)<1\).

The upper bound is constructed as follows. In [Weighted moments and sampling](weighted-moments-and-sampling.md), a random vector of *normalized gradients* whose \(p\)-th moments are nearly the same on every pair of points is turned into an embedding by sampling; by convexity, it suffices to achieve this on average for each weighting of the pairs. [Electrical flows and a weighted projection](electrical-flows-and-a-weighted-projection.md) projects onto normalized gradients with a projection whose rows have absolute sums \(O(\log n)\), by a bound for electrical flows. The random vectors are built from a measure under which every normalized increment of the points has the same distribution of sizes: for \(1<p<2\) by heavy-tailed sums, clipped and projected ([Signed Poisson sums and exponents below two](signed-poisson-sums-below-two.md)), and for \(p>2\) by overlapping truncations and Poisson sampling ([Truncation ramps and exponents above two](truncation-ramps-above-two.md)).

## 6. Exercises

**Exercise 6.1** (easy). Show that \(d_p(n,D)\) is nondecreasing in \(n\) and nonincreasing in \(D\).

**Exercise 6.2** (easy). Compute \(\Delta_p(1,1)\) and check its sign against Lemma 4.1. Show that \(\Delta_2\equiv0\).

**Exercise 6.3** (medium). Show that Lemma 4.3 fails for \(p=1\): find \(u\neq w\) in \(\ell_1^2\) with \(\|u\|_1=\|w\|_1=1\) and \(\|u+w\|_1=2\).

**Exercise 6.4** (medium). Show that the step \(f(-x)=-f(x)\) in the proof of Proposition 4.4 can fail for \(p=1\): find an isometric map \(f\) of \(\{0,x,-x\}\subseteq\ell_1^2\) into \(\ell_1^2\) with \(f(0)=0\) and \(f(-x)\neq-f(x)\).

## 7. Solutions

**6.1.** An embedding of \(n+1\) points restricts to one of any \(n\) of them, and every \(n\)-point set extends to an \((n+1)\)-point set; a map of distortion at most \(D\) has distortion at most \(D'\) for \(D'\ge D\).

**6.2.** \(\Delta_p(1,1)=2^p-4\), positive for \(p>2\) and negative for \(p<2\). For \(p=2\), \((a+b)^2+(a-b)^2=2a^2+2b^2\).

**6.3.** \(u=(1,0)\), \(w=(\frac12,\frac12)\): \(\|u+w\|_1=\frac32+\frac12=2\).

**6.4.** Take \(x=(1,0)\), \(f(x)=(1,0)\) and \(f(-x)=(0,-1)\). Then \(\|f(x)\|_1=\|f(-x)\|_1=1\) and \(\|f(x)-f(-x)\|_1=2\), as for the original points, but \(f(-x)\neq(-1,0)\). This is possible because \(\ell_1^2\) is not strictly convex, so Lemma 4.3 fails.

## References

- [OpenAI-LP] OpenAI, *Subpolynomial dimension reduction in L_p*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026
- [Naor] A. Naor, *Metric dimension reduction: a snapshot of the Ribe program*, Proceedings of the ICM 2018. https://arxiv.org/abs/1809.02376
- [Schechtman] G. Schechtman, *Dimension reduction in L_p, 0<p<2*, 2011. https://arxiv.org/abs/1110.2148
- [NR] A. Naor and K. Ren, *A threshold phenomenon for embeddings of Euclidean snowflakes and impossibility of dimension reduction*, 2026. https://arxiv.org/abs/2609.01079
