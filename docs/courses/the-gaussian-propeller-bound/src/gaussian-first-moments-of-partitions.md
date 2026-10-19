# Gaussian first moments of partitions

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(\gamma_n\) be the standard Gaussian measure on \(\mathbb R^n\), with density \((2\pi)^{-n/2}e^{-|x|^2/2}\). The *Gaussian first moment* of a measurable set \(A\subseteq\mathbb R^n\) is the vector
\[
z(A)=\int_Ax\,d\gamma_n(x)\in\mathbb R^n .
\]
It is not divided by \(\gamma_n(A)\), so a set of small measure has a short moment. For a finite measurable partition \(\mathcal A=(A_1,\dots,A_k)\) of \(\mathbb R^n\) put
\[
\mathcal F(\mathcal A)=\sum_{i=1}^k|z(A_i)|^2 .
\]
The shapes and the measures of the cells are free. This course proves OpenAI's answer to the question how large \(\mathcal F\) can be [OpenAI-GP]:

**Theorem** (the Gaussian propeller bound). For all positive integers \(d\) and \(k\), every measurable partition \((A_1,\dots,A_k)\) of \(\mathbb R^d\) satisfies
\[
\sum_{i=1}^k\Bigl|\int_{A_i}x\,d\gamma_d(x)\Bigr|^2\le\frac9{8\pi}.
\]
If \(d\ge2\) and \(k\ge3\), equality holds for three planar sectors of angle \(2\pi/3\), each multiplied by \(\mathbb R^{d-2}\), with the remaining cells empty.

Khot and Naor met this quantity in the study of approximate kernel clustering [KhNa]. With \(k\) clusters and the identity matrix as target, their rounding algorithm and their hardness reduction meet at an approximation factor determined by the supremum of \(\mathcal F\) over partitions of \(\mathbb R^{k-1}\) into \(k\) cells; the reduction starts from Unique Games ([Kernel clustering and the Gaussian constant](kernel-clustering-and-the-gaussian-constant.md)). They computed the value \(9/(8\pi)\) for three cells and conjectured that no number of cells does better; the optimal partition looks like a three-bladed propeller, hence the *propeller conjecture*. Heilman, Jagannath and Naor proved it for all partitions of \(\mathbb R^3\) with a computer-assisted argument [HJN]. The argument of [OpenAI-GP] treats all remaining dimensions.

**What the course assumes.** One published theorem is used as a named statement and is not proved here:

- **(HJN)** For every \(k\ge1\) and every measurable partition \((A_1,\dots,A_k)\) of \(\mathbb R^3\), \(\sum_i|z(A_i)|^2\le9/(8\pi)\) [HJN, Theorem 1.1]. It is used once, in Theorem 4.3 below, to exclude optimal partitions with at most four cells of positive measure.

Ehrhard's inequality for convex sets, referred to as (EHR) [Ehrhard], is proved in full in the course [Ehrhard's inequality for convex sets](course:ehrhards-inequality-for-convex-sets/gaussian-heat-semigroups-and-a-gradient-bound#the-theorem); it is stated in [Ehrhard concavity and the loss of one score](ehrhard-concavity-and-the-loss-of-one-score.md), where it is used.

Everything else is proved in the lessons, including every numerical comparison; each comparison is stated with exact rational bounds.

**The course.**

1. This lesson: the problem, the propeller, the duality between partitions and expected maxima of Gaussian scores, and the structure of an optimal partition.
2. [Rearrangement bounds for one cell](rearrangement-bounds-for-one-cell.md): a lower bound for the measure of a cell in terms of the length of its moment.
3. [Ehrhard concavity and the loss of one score](ehrhard-concavity-and-the-loss-of-one-score.md): what deleting one score costs, and a second, linear lower bound for the measure of a cell.
4. [Two competing scores](two-competing-scores.md): the cell with the shortest moment constrains the covariances of the other scores.
5. [Five or more cells and the propeller bound](five-or-more-cells-and-the-propeller-bound.md): the bounds are incompatible; proof of the theorem and of a sharp inequality for Gaussian maxima.
6. [Kernel clustering and the Gaussian constant](kernel-clustering-and-the-gaussian-constant.md): the approximation threshold for clustering with the identity as target.

## 1. Conventions

Measurable means Borel measurable; partitions are taken up to \(\gamma_n\)-null sets, and empty cells are allowed. Norms and inner products are Euclidean. We write
\[
\begin{gathered}
\phi(x)=\frac{e^{-x^2/2}}{\sqrt{2\pi}},\\
\Phi(x)=\int_{-\infty}^x\phi(s)\,ds,\\
B=\frac3{2\sqrt{2\pi}},
\end{gathered}
\]
so that \(B^2=9/(8\pi)\) and \(B=\frac32\phi(0)\). The letter \(g\) denotes a standard Gaussian vector, a random vector with distribution \(\gamma_n\). Since \(\int|x|^2\,d\gamma_n=n\), every Gaussian first moment exists.

Two facts from the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) are used throughout.

- *Products.* \(\gamma_{d+e}\) is the product of \(\gamma_d\) and \(\gamma_e\) (Fubini's theorem, [Fremlin, *Measure Theory*, Volume 2, Theorem 252B](https://www1.essex.ac.uk/maths/people/fremlin/cont25.htm)). For \(A\subseteq\mathbb R^d\) the set \(A\times\mathbb R^e\) has measure \(\gamma_d(A)\) and moment \((z(A),0)\), because \(\int_{\mathbb R^e}y\,d\gamma_e(y)=0\).
- *Rotations.* An orthogonal map \(T\) of \(\mathbb R^n\) preserves Lebesgue measure ([Fremlin, *Measure Theory*, Volume 2, Theorem 263A](https://www1.essex.ac.uk/maths/people/fremlin/cont26.htm), with \(|\det T|=1\)) and the Gaussian density, which depends only on \(|x|\). Hence \(\gamma_n(T[A])=\gamma_n(A)\) and \(z(T[A])=Tz(A)\).

For positive integers \(d,k\) let \(C(d,k)\) be the supremum of \(\mathcal F\) over partitions of \(\mathbb R^d\) into \(k\) cells.

**Lemma 1.1.** (a) If \(d\le d'\) and \(k\le k'\), then \(C(d,k)\le C(d',k')\).
(b) \(C(d,k)\le d\).
(c) The bound of the Theorem holds for all \(d\) and \(k\) if and only if \(C(n,n+1)\le9/(8\pi)\) for every \(n\ge4\).

**Proof.** (a) Multiply each cell of a partition of \(\mathbb R^d\) by \(\mathbb R^{d'-d}\) and append \(k'-k\) empty cells; by the product rule the moments only acquire zero coordinates, so \(\mathcal F\) is unchanged.

(b) For a unit vector \(e\), the Cauchy–Schwarz inequality gives \((\int_A\langle e,x\rangle\,d\gamma_d)^2\le\gamma_d(A)\int_A|x|^2\,d\gamma_d\), so \(|z(A)|^2\le\int_A|x|^2\,d\gamma_d\). Summing over the cells gives \(\mathcal F\le\int|x|^2\,d\gamma_d=d\).

(c) Given \(d\) and \(k\), put \(n=\max\{d,k-1,4\}\); then \(C(d,k)\le C(n,n+1)\) by (a). The converse is a special case. \(\square\)

## 2. The propeller

For \(0<\alpha\le\pi\) let \(S_\alpha\) be the open sector \(\{(r\cos\theta,r\sin\theta):r>0,\ |\theta|<\alpha\}\) of the plane.

**Lemma 2.1.** \(z(S_\alpha)=\bigl(\sin\alpha/\sqrt{2\pi},\,0\bigr)\).

**Proof.** In polar coordinates ([Fremlin, *Measure Theory*, Volume 2, 263G](https://www1.essex.ac.uk/maths/people/fremlin/cont26.htm)),
\[
\begin{aligned}
z(S_\alpha)&=\frac1{2\pi}\int_0^\infty r^2e^{-r^2/2}\,dr\\
&\quad\cdot\int_{-\alpha}^\alpha(\cos\theta,\sin\theta)\,d\theta .
\end{aligned}
\]
Integration by parts gives \(\int_0^\infty r^2e^{-r^2/2}\,dr=\int_0^\infty e^{-r^2/2}\,dr=\sqrt{2\pi}/2\), and the angular integral is \((2\sin\alpha,0)\). \(\square\)

**Corollary 2.2** (the propeller). Rotate \(S_{\pi/3}\) by \(0\), \(2\pi/3\) and \(4\pi/3\). The three sectors cover the plane up to three rays, a null set. Each moment has squared length \(\sin^2(\pi/3)/(2\pi)=3/(8\pi)\), so the partition has \(\mathcal F=9/(8\pi)\). Consequently \(C(d,k)\ge9/(8\pi)\) whenever \(d\ge2\) and \(k\ge3\).

**Proof.** The value follows from Lemma 2.1 and the rotation rule, and the last assertion from Lemma 1.1(a). \(\square\)

This proves the equality statement of the Theorem. The three moments have equal lengths and point in the directions \(0\), \(2\pi/3\), \(4\pi/3\), so they sum to zero; each sector consists of the points at which the inner product with its own moment exceeds the inner products with the other two. Both properties hold for every optimal partition (Proposition 4.1).

## 3. Partitions and expected maxima

For vectors \(v_1,\dots,v_k\in\mathbb R^n\), the *score partition* \(Q(v)=(Q_1,\dots,Q_k)\) assigns \(x\) to an index with the largest *score* \(\langle v_i,x\rangle\), breaking ties in favour of the smallest index: \(Q_i\) is the set of points \(x\) with \(\langle v_i,x\rangle>\langle v_j,x\rangle\) for \(j<i\) and \(\langle v_i,x\rangle\ge\langle v_j,x\rangle\) for \(j>i\). Each \(Q_i\) is an intersection of finitely many half-spaces, so \(Q(v)\) is a measurable partition.

**Lemma 3.1.** For every measurable partition \((A_1,\dots,A_k)\) of \(\mathbb R^n\),
\[
\sum_{i=1}^k\langle v_i,z(A_i)\rangle\le\mathbb E\max_{1\le i\le k}\langle v_i,g\rangle ,
\]
with equality for the score partition.

**Proof.** The left side is \(\int\langle v_{i(x)},x\rangle\,d\gamma_n(x)\), where \(i(x)\) is the index of the cell containing \(x\), and \(\langle v_{i(x)},x\rangle\le\max_i\langle v_i,x\rangle\), with equality everywhere for the score partition. The maximum is integrable because it is at most \(|x|\max_i|v_i|\). \(\square\)

The next lemma is the normalized vector form of Khot and Naor's description of the supremum by Gaussian maxima [KhNa, Lemma 3.7].

**Lemma 3.2** (duality). Let \(n,N\ge1\) and \(C=C(n,N)\). Then
\[
\sqrt C=\max_v\,\mathbb E\max_{1\le i\le N}\langle v_i,g\rangle ,
\]
the maximum over lists \(v=(v_1,\dots,v_N)\) of vectors of \(\mathbb R^n\) with \(\sum_i|v_i|^2=1\). The maximum is attained, and some partition of \(\mathbb R^n\) into \(N\) cells has \(\mathcal F=C\). Moreover, for every \(k\le N\) and all \(v_1,\dots,v_k\in\mathbb R^n\),
\[
\mathbb E\max_{1\le i\le k}\langle v_i,g\rangle\le\sqrt C\,\Bigl(\sum_{i=1}^k|v_i|^2\Bigr)^{1/2}.
\]

**Proof.** For a partition with moments \(z_1,\dots,z_N\), the Cauchy–Schwarz inequality in \((\mathbb R^n)^N\) gives
\[
\Bigl(\sum_i|z_i|^2\Bigr)^{1/2}=\max_v\sum_i\langle v_i,z_i\rangle ,
\]
the maximum again over lists with \(\sum_i|v_i|^2=1\).
Taking the supremum over partitions and lists and exchanging the order, Lemma 3.1 identifies \(\sqrt C\) with the supremum of \(E(v)=\mathbb E\max_i\langle v_i,g\rangle\) over unit lists. Since
\[
\bigl|\max_ia_i-\max_ib_i\bigr|\le\max_i|a_i-b_i|,
\]
we have \(|E(v)-E(w)|\le\mathbb E|g|\,\max_i|v_i-w_i|\), so \(E\) is continuous, and it attains its supremum on the compact unit sphere of \((\mathbb R^n)^N\) at some list \(v^*\). Its score partition has moments \(b_i\) with \(\bigl(\sum|b_i|^2\bigr)^{1/2}\ge\sum\langle v^*_i,b_i\rangle=E(v^*)=\sqrt C\), so it attains \(C\).

For the last assertion let \(b_1,\dots,b_k\) be the moments of the score partition of \(v_1,\dots,v_k\). Appending \(N-k\) empty cells gives a partition into \(N\) cells, so \(\sum|b_i|^2\le C\), and Lemma 3.1 with the Cauchy–Schwarz inequality gives
\[
\begin{aligned}
\mathbb E\max_i\langle v_i,g\rangle&=\sum_i\langle v_i,b_i\rangle\\
&\le\Bigl(\sum_i|v_i|^2\Bigr)^{1/2}\sqrt C .
\end{aligned}
\]
\(\square\)

## 4. Optimal partitions

Fix \(n\ge4\), put \(N=n+1\) and \(C=C(n,N)\), and assume \(C>0\) (Corollary 2.2). By Lemma 3.2 there are partitions with \(\mathcal F=C\); call them *optimal*. Choose an optimal partition with the smallest possible number \(m\) of cells of positive measure, the *active* cells, and let \(z_1,\dots,z_m\) be their moments. The other cells have moment zero. Since \(\sum_{\text{all cells}}z(A)=\int x\,d\gamma_n=0\),
\[
\sum_{i=1}^mz_i=0,\qquad\sum_{i=1}^m|z_i|^2=C .
\]

**Proposition 4.1** (structure; Khot and Naor [KhNa, Theorem 1.2 and Lemma 3.3]).

(a) \(\langle z_i,z_j\rangle<0\) for \(i\ne j\). In particular \(m\ge2\), every \(z_i\) is nonzero and the \(z_i\) are distinct.

(b) Up to null sets the \(i\)-th active cell equals the closed cone \(K_i\) of the points \(x\in\mathbb R^n\) with \(\langle z_i-z_j,x\rangle\ge0\) for all \(j\ne i\). The cones \(K_1,\dots,K_m\) cover \(\mathbb R^n\), and \(K_i\cap K_j\) is a null set for \(i\ne j\).

(c) The span \(V\) of \(z_1,\dots,z_m\) has dimension \(m-1\). Every proper subset of \(\{z_1,\dots,z_m\}\) is linearly independent, and for each \(i\) the \(m-1\) vectors \(z_i-z_j\), \(j\ne i\), form a basis of \(V\).

(d) Let \(g\) be standard Gaussian in \(V\). The cone \(K_i\cap V\) has Gaussian measure \(\gamma_n(K_i)\) and moment \(z_i\) in \(V\).

(e) With \(X_i=\langle z_i,g\rangle\) for \(g\) standard Gaussian in \(V\): \(\sum_iX_i=0\), \(\mathbb E\max_iX_i=C\), and \(P_i=\gamma_V(K_i\cap V)\) satisfies \(0<P_i\le\frac12\) and \(\sum_iP_i=1\).

**Proof.** (a) Since \(C>0\), some moment is nonzero, and \(\sum z_i=0\) forces \(m\ge2\). Merging the active cells \(i\) and \(j\) into one cell and leaving one label empty gives a partition into \(N\) cells with
\[
\begin{aligned}
\mathcal F&=C+|z_i+z_j|^2-|z_i|^2-|z_j|^2\\
&=C+2\langle z_i,z_j\rangle .
\end{aligned}
\]
Optimality gives \(\langle z_i,z_j\rangle\le0\). If equality held, the merged partition would be optimal with \(m-1\) active cells, contrary to the choice of \(m\). So \(\langle z_i,z_j\rangle<0\); then no \(z_i\) is zero, and \(z_i\ne z_j\) because \(\langle z_i,z_i\rangle>0>\langle z_i,z_j\rangle\).

(b) Write \(A_1,\dots,A_m\) for the active cells. Pairing each cell with its own moment, Lemma 3.1 and the last inequality of Lemma 3.2 (with \(k=m\le N\)) give
\[
\begin{aligned}
C=\sum_i\langle z_i,z_i\rangle&\le\mathbb E\max_i\langle z_i,g\rangle\\
&\le\sqrt C\cdot\sqrt C=C .
\end{aligned}
\]
Hence \(\int\bigl(\max_j\langle z_j,x\rangle-\langle z_{i(x)},x\rangle\bigr)\,d\gamma_n=0\) with a nonnegative integrand, so almost every point of \(A_i\) lies in \(K_i\). Every point lies in some \(K_i\), and \(K_i\cap K_j\) lies in the hyperplane \(\{\langle z_i-z_j,x\rangle=0\}\), a null set because \(z_i\ne z_j\). Since the \(A_i\) cover \(\mathbb R^n\) up to a null set and \(A_i\subseteq K_i\) up to a null set, each \(K_i\setminus A_i\) is contained, up to a null set, in \(\bigcup_{j\ne i}(K_i\cap K_j)\), which is null.

(c) Let \(Q=(\langle z_i,z_j\rangle)_{i,j=1}^m\) be the Gram matrix. Its rows sum to zero, so for \(a\in\mathbb R^m\)
\[
a^{\mathsf T}Qa=\sum_{i<j}\bigl(-\langle z_i,z_j\rangle\bigr)(a_i-a_j)^2 .
\]
All weights are positive by (a), so \(a^{\mathsf T}Qa=0\) only for constant \(a\). Since \(a^{\mathsf T}Qa=|\sum a_iz_i|^2\), the linear relations among the \(z_i\) are exactly the multiples of \(\sum z_i=0\); thus \(\dim V=m-1\). A relation supported on a proper subset has a zero coefficient, so it is trivial. A relation \(\sum_{j\ne i}b_j(z_i-z_j)=0\) is a relation among all \(z_l\) whose coefficients sum to zero; a constant coefficient vector with sum zero vanishes, so all \(b_j=0\), and the \(m-1\) vectors \(z_i-z_j\) form a basis of \(V\).

(d) Whether \(x\in K_i\) depends only on the orthogonal projection of \(x\) onto \(V\). In orthonormal coordinates in which \(V=\mathbb R^{m-1}\times\{0\}\), \(K_i=(K_i\cap V)\times\mathbb R^{n-m+1}\), and the product rule of Section 1 gives the claim.

(e) \(\sum X_i=\langle\sum z_i,g\rangle=0\), and \(\mathbb E\max_iX_i=C\) by the equality in (b) and (d). The largest of numbers with sum zero is nonnegative, so \(X_i\ge0\) on \(K_i\cap V\); thus \(K_i\cap V\) lies in a half-space through the origin, and \(P_i\le\frac12\). Finally \(P_i=\gamma_n(A_i)>0\), and the \(P_i\) sum to one by (b). \(\square\)

**Remark 4.2.** In \(V\) the cone \(K_i\cap V\) is the set where the \(m-1\) linear forms \(\langle z_i-z_j,\cdot\rangle\) are nonnegative. By (c) these forms are the coordinates of a linear isomorphism of \(V\) onto \(\mathbb R^{m-1}\), which maps \(K_i\cap V\) onto the closed positive orthant. Hence \(K_i\cap V\) is a closed convex cone with nonempty interior, and it is not all of \(V\).

**Theorem 4.3.** Under (HJN), if \(m\le4\) then \(C\le9/(8\pi)\).

**Proof.** By Proposition 4.1(c), \(\dim V=m-1\le3\). By (b) and (d) the cones \(K_i\cap V\) form a partition of \(V\cong\mathbb R^{m-1}\) with moments \(z_1,\dots,z_m\). Multiplying them by \(\mathbb R^{4-m}\) gives a partition of \(\mathbb R^3\) with the same moment lengths, so (HJN) gives \(C=\sum|z_i|^2\le9/(8\pi)\). \(\square\)

**The standing setting of Lessons 2–5.** Suppose, to reach a contradiction, that \(C(n,n+1)>B^2=9/(8\pi)\) for some \(n\ge4\). Fix \(n\), put \(N=n+1\) and \(C=C(n,N)\), choose an optimal partition with the fewest active cells, and let \(z_1,\dots,z_m\) be the moments of its active cells. By Theorem 4.3, \(m\ge5\). From here on we work in \(V\cong\mathbb R^{m-1}\) with a standard Gaussian vector \(g\) of \(V\), write \(K_i\) for the cone \(K_i\cap V\), and set
\[
\begin{gathered}
X_i=\langle z_i,g\rangle,\qquad P_i=\gamma_{m-1}(K_i),\\
r_i=\frac{|z_i|}{\sqrt C}.
\end{gathered}
\]
Then:

- (S1) \(C>B^2\) and \(m\ge5\);
- (S2) \(\sum z_i=0\), \(\langle z_i,z_j\rangle<0\) for \(i\ne j\), and \(\sum r_i^2=1\);
- (S3) proper subsets of the \(z_i\) are linearly independent, and the \(z_i-z_j\), \(j\ne i\), form a basis of \(V\);
- (S4) the cones \(K_i\) cover \(V\), overlap in null sets, are closed and convex with nonempty interior, and \(\int_{K_i}x\,d\gamma_{m-1}=z_i\);
- (S5) \(\sum X_i=0\), \(\mathbb E\max_iX_i=C\), \(0<P_i\le\frac12\) and \(\sum P_i=1\);
- (S6) for every \(k\le m\) and all \(v_1,\dots,v_k\in V\),
\[
\mathbb E\max_{i\le k}\langle v_i,g\rangle\le\sqrt C\Bigl(\sum_i|v_i|^2\Bigr)^{1/2}.
\]

Property (S6) is Lemma 3.2 for lists in \(V\subseteq\mathbb R^n\): the orthogonal projection of a standard Gaussian vector of \(\mathbb R^n\) onto \(V\) is standard Gaussian in \(V\), and \(k\le m\le N\). Lessons 2–5 derive a contradiction from (S1)–(S6).

## 5. Exercises

**5.1** (easy). Compute \(\mathcal F\) for the partition of \(\mathbb R\) into \((-\infty,0)\) and \([0,\infty)\), and compare it with \(9/(8\pi)\).

**5.2** (medium). Let \(\alpha_1,\alpha_2,\alpha_3>0\) with \(\alpha_1+\alpha_2+\alpha_3=\pi\), and partition the plane into three consecutive sectors of angles \(2\alpha_1,2\alpha_2,2\alpha_3\) with vertex at the origin. Show that \(\mathcal F=\frac1{2\pi}\sum_i\sin^2\alpha_i\le\frac9{8\pi}\), with equality only when every \(\alpha_i=\pi/3\).

**5.3** (easy). Show that adding the same vector \(w\) to every \(v_i\) changes neither the score partition nor \(\mathbb E\max_i\langle v_i,g\rangle\).

**5.4** (medium). Show that \(C(1,k)=1/\pi\) for every \(k\ge2\).

**5.5** (medium). In the setting of Proposition 4.1, let \(h\in V\) satisfy \(\langle h,z_i-z_j\rangle=1\) for every \(j\ne i\). Show that \(\langle h,z_i\rangle=(m-1)/m\).

## 6. Solutions

**5.1.** \(z([0,\infty))=\int_0^\infty x\phi(x)\,dx=\phi(0)\) and \(z((-\infty,0))=-\phi(0)\). So \(\mathcal F=2\phi(0)^2=1/\pi\), and \(1/\pi=8/(8\pi)<9/(8\pi)\).

**5.2.** By Lemma 2.1 and rotation invariance, the sector of angle \(2\alpha_i\) has a moment of length \(\sin\alpha_i/\sqrt{2\pi}\), which gives the formula. Since \(\sin^2\alpha=\frac12(1-\cos2\alpha)\), the claim is \(\sum\cos2\alpha_i\ge-\frac32\). Let \(f_1,f_2,f_3\) be unit vectors at the angles \(0\), \(2\alpha_1\) and \(2\alpha_1+2\alpha_2\). The angle between consecutive vectors is \(2\alpha_1\), \(2\alpha_2\) and \(2\alpha_3\) (the last because \(2\alpha_1+2\alpha_2+2\alpha_3=2\pi\)), so
\[
0\le|f_1+f_2+f_3|^2=3+2\sum_i\cos2\alpha_i .
\]
Equality forces \(f_1+f_2+f_3=0\), so three unit vectors at mutual angles \(2\pi/3\), and every \(\alpha_i=\pi/3\).

**5.3.** The differences \(\langle v_i-v_j,x\rangle\) are unchanged, hence so is the score partition, and \(\max_i\langle v_i+w,g\rangle=\max_i\langle v_i,g\rangle+\langle w,g\rangle\) with \(\mathbb E\langle w,g\rangle=0\).

**5.4.** By Lemma 3.2 with \(n=1\), \(\sqrt{C(1,k)}\) is the maximum of \(\mathbb E\max_iv_ig\) over real \(v_1,\dots,v_k\) with \(\sum v_i^2=1\). For \(g\ge0\) the maximum of \(v_ig\) is \(g\max_iv_i\), for \(g<0\) it is \(g\min_iv_i\), so
\[
\begin{aligned}
&\mathbb E\max_iv_ig\\
&\quad=(\max_iv_i-\min_iv_i)\,\mathbb E g_+\\
&\quad=\frac{\max_iv_i-\min_iv_i}{\sqrt{2\pi}} .
\end{aligned}
\]
Since \((\max-\min)^2\le2(\max^2+\min^2)\le2\), this is at most \(1/\sqrt\pi\), with equality for \(v=(1/\sqrt2,-1/\sqrt2,0,\dots)\). Hence \(C(1,k)=1/\pi\).

**5.5.** Summing the \(m-1\) equations gives \((m-1)\langle h,z_i\rangle-\langle h,\sum_{j\ne i}z_j\rangle=m-1\). Since \(\sum_{j\ne i}z_j=-z_i\), this is \(m\langle h,z_i\rangle=m-1\).

## References

- [OpenAI-GP] OpenAI, *The Gaussian propeller bound in every dimension*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026
- [KhNa] S. Khot and A. Naor, *Approximate kernel clustering*, Mathematika 55 (2009), 129–165; arXiv:0807.4626. https://arxiv.org/abs/0807.4626
- [HJN] S. Heilman, A. Jagannath and A. Naor, *Solution of the propeller conjecture in \(\mathbb R^3\)*, Discrete & Computational Geometry 50 (2013), 263–305; arXiv:1112.2993. https://arxiv.org/abs/1112.2993
- [Ehrhard] A. Ehrhard, *Symétrisation dans l'espace de Gauss*, Mathematica Scandinavica 53 (1983), 281–301. https://journals.msp.org/mscand/article/view/1636
- [Fremlin] D. H. Fremlin, *Measure Theory*, Volumes 1 and 2, author's edition, the basis of the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10). https://www1.essex.ac.uk/maths/people/fremlin/mt.htm
