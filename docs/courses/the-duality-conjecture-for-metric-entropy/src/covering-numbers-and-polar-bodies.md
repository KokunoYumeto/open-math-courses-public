# Covering numbers and polar bodies

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For bounded sets \(A,B\subseteq\mathbb R^n\), with \(B\) having nonempty interior, the *covering number* \(N(A,B)\) is the least number of translates \(z+B\), \(z\in\mathbb R^n\), whose union contains \(A\). Its logarithm measures the complexity of \(A\) at the resolution given by \(B\). A *convex body* is a compact convex set with nonempty interior; it is *symmetric* if \(-K=K\). The *polar* of a symmetric convex body is the symmetric convex body
\[
K^\circ=\{y\in\mathbb R^n:\langle x,y\rangle\le1\text{ for all }x\in K\}.
\]
Pietsch asked in 1972, in the language of operators and their adjoints, whether covering numbers are preserved by polarity up to universal constants. In the geometric form recorded by Artstein, Milman, Szarek and Tomczak-Jaegermann [AMSTJ, Conjecture 1], the *duality conjecture for metric entropy* asks for absolute constants \(a,b\ge1\) such that
\[
\frac1b\log N(L^\circ,aK^\circ)\le\log N(K,L)\le b\log N(L^\circ,a^{-1}K^\circ)\tag{0.1}
\]
for all dimensions and all symmetric convex bodies \(K,L\). Artstein, Milman and Szarek proved it when one of the bodies is an ellipsoid [AMS], and related versions were proved under further assumptions. OpenAI showed in September 2026 that the right-hand inequality fails for every choice of constants, already with \(L\) a cube [OpenAI-E]; passing to polar pairs, the left-hand inequality fails as well:

**Theorem.** For all \(a,b\ge1\) there are \(n\) and a symmetric convex body \(K\subseteq\mathbb R^n\) such that, for \(L=[-1,1]^n\), \(\log N(K,L)>b\log N(L^\circ,a^{-1}K^\circ)\).

This course gives the proof. The present lesson turns a real matrix into a pair of bodies and states what the matrix must achieve (Lemma 2.1): many rows that are pairwise far apart in the maximum norm, while all signed combinations of its columns with \(\ell^1\)-norm at most \(1\) are approximated, uniformly, by a short list of functions. The lesson [Compression by partitions](compression-by-partitions.md) builds column families with short approximation lists from partitions with few classes, and the lesson [Symmetric forms over finite fields](symmetric-forms-over-finite-fields.md) builds partitions with few classes whose rows are separated, and proves the theorem. Section 3 below proves a duality theorem for a related quantity, *convexified packing*, which the theorem shows to behave differently from covering numbers.

We use the separation of a point from a closed convex set and of disjoint convex sets one of which is open, in \(\mathbb R^n\), as in [Theorems 6.2 and 6.3 of the Banach space lesson](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces#OA-FND-HB-06), and compactness in \(\mathbb R^n\).

## 1. Support functions and polars

For a compact convex \(K\subseteq\mathbb R^n\) the *support function* is \(h_K(\delta)=\max_{z\in K}\langle z,\delta\rangle\). For a symmetric convex body \(K\) it is a norm, and by definition
\[
\delta\in cK^\circ\iff h_K(\delta)\le c\qquad(c>0).\tag{1.1}
\]
The support function of a Minkowski sum is the sum of the support functions, because the two maximizations are independent; that of the convex hull of finitely many points is the maximum over the points. For the cube \(B_\infty^n=[-1,1]^n\), \(h(\delta)=\sum_i|\delta_i|=\|\delta\|_1\), so \((B_\infty^n)^\circ=B_1^n\), the unit ball of \(\ell^1\). For a symmetric convex body \(K\) let \(\|x\|_K=\min\{t\ge0:x\in tK\}\) be its gauge.

**Lemma 1.1** (bipolar theorem). Let \(K\subseteq\mathbb R^n\) be a symmetric convex body. Then \(K^\circ\) is a symmetric convex body, \(K^{\circ\circ}=K\), and \(\|y\|_{K^\circ}=h_K(y)\), \(\|x\|_K=h_{K^\circ}(x)\) for all \(x,y\in\mathbb R^n\).

**Proof.** If \(z\) is an interior point of \(K\), so is \(-z\), and hence so is \(0=\frac12z+\frac12(-z)\), because the interior of a convex set is convex. So \(\rho B_2^n\subseteq K\subseteq RB_2^n\) for some \(0<\rho\le R\), where \(B_2^n\) is the Euclidean unit ball. Then \(h_K(\delta)\ge\rho|\delta|>0\) for \(\delta\neq0\), and \(R^{-1}B_2^n\subseteq K^\circ\subseteq\rho^{-1}B_2^n\); \(K^\circ\) is closed, convex and symmetric by its definition, so it is a symmetric convex body. For \(t>0\), \(y\in tK^\circ\) if and only if \(\langle x,y\rangle\le t\) for all \(x\in K\), that is \(h_K(y)\le t\); with \(h_K(y)=0\iff y=0\) this gives \(\|y\|_{K^\circ}=h_K(y)\). Clearly \(K\subseteq K^{\circ\circ}\). If \(x\notin K\), separating \(x\) from the closed convex set \(K\) gives a nonzero \(\varphi\) with \(\langle x,\varphi\rangle>\max_{z\in K}\langle z,\varphi\rangle=h_K(\varphi)>0\); then \(\varphi/h_K(\varphi)\in K^\circ\) and \(\langle x,\varphi/h_K(\varphi)\rangle>1\), so \(x\notin K^{\circ\circ}\). Finally, the formula for the gauge applied to the body \(K^\circ\) gives \(\|x\|_{K^{\circ\circ}}=h_{K^\circ}(x)\), and \(K^{\circ\circ}=K\). \(\square\)

Covering numbers are monotone: \(N(A,B)\le N(A',B')\) if \(A\subseteq A'\) and \(B\supseteq B'\), and \(N(tA,tB)=N(A,B)\) for \(t>0\).

## 2. From a matrix to a pair of bodies

**Lemma 2.1** (matrix-to-body conversion). Let \(X,Y\) be finite nonempty sets and \(g_y:X\to\mathbb R\), \(y\in Y\). Put \(R_x=(g_y(x))_{y\in Y}\in\mathbb R^Y\) (the rows) and \(f_\lambda=\sum_y\lambda_yg_y\) for \(\lambda\in\mathbb R^Y\). Suppose that

(a) \(\|R_x-R_{x'}\|_\infty\ge1\) for distinct \(x,x'\in X\), and

(b) for some \(\varepsilon>0\) there are \(M\) functions on \(X\) such that every \(f_\lambda\) with \(\|\lambda\|_1\le1\) is within \(\varepsilon\) of one of them in the maximum norm on \(X\).

For \(t>0\) let \(K=3\operatorname{absconv}\{R_x:x\in X\}+t\,B_\infty^Y\) and \(L=B_\infty^Y\), where \(\operatorname{absconv}\) is the convex hull of the points \(\pm R_x\). Then \(K\) and \(L\) are symmetric convex bodies in \(\mathbb R^Y\), and
\[
N(K,L)\ge|X|,\qquad N\bigl(L^\circ,(6\varepsilon+2t)K^\circ\bigr)\le M.\tag{2.1}
\]

**Proof.** \(K\) is compact, convex and symmetric and contains the cube \(tB_\infty^Y\), so it is a body. The points \(3R_x\) lie in \(K\) and have pairwise distance at least \(3\) in the maximum norm, while every translate of \(L\) has diameter \(2\) in that norm; so a translate contains at most one of them, and \(N(K,L)\ge|X|\).

By Section 1,
\[
h_K(\delta)=3\max_{x\in X}|\langle R_x,\delta\rangle|+t\|\delta\|_1=3\max_{x\in X}|f_\delta(x)|+t\|\delta\|_1,\tag{2.2}
\]
and \(L^\circ=B_1^Y\). Order the \(M\) functions of (b) and assign each \(\lambda\in B_1^Y\) to the first one within \(\varepsilon\) of \(f_\lambda\). This splits \(B_1^Y\) into at most \(M\) nonempty classes; choose \(\lambda^{(k)}\) in each class. For \(\lambda\) in the class of \(\lambda^{(k)}\), \(\max_X|f_\lambda-f_{\lambda^{(k)}}|\le2\varepsilon\) and \(\|\lambda-\lambda^{(k)}\|_1\le2\), so \(h_K(\lambda-\lambda^{(k)})\le6\varepsilon+2t\) by (2.2), that is \(\lambda\in\lambda^{(k)}+(6\varepsilon+2t)K^\circ\) by (1.1). These \(M\) translates cover \(L^\circ\). \(\square\)

The representatives \(\lambda^{(k)}\) are chosen in \(B_1^Y\), not among the approximating functions, because the term \(t\|\delta\|_1\) in (2.2) needs both \(\lambda\) and \(\lambda^{(k)}\) to have \(\ell^1\)-norm at most \(1\).

**Corollary 2.2** (what remains to be done). Let \(a,b\ge1\). If a matrix as in Lemma 2.1 has \(\log|X|>b\log M\) with \(6\varepsilon+2t\le a^{-1}\), then the bodies of the lemma violate the right-hand inequality of (0.1) for these constants.

**Proof.** \(N(L^\circ,a^{-1}K^\circ)\le N(L^\circ,(6\varepsilon+2t)K^\circ)\le M\) by monotonicity, since \((6\varepsilon+2t)K^\circ\subseteq a^{-1}K^\circ\), and \(\log N(K,L)\ge\log|X|>b\log M\). \(\square\)

## 3. Convexified packing

For a bounded set \(T\) and a symmetric convex body \(B\), a sequence \(x_1,\dots,x_m\in T\) is *\(B\)-convexly separated* if \((x_j+\operatorname{int}B)\cap\operatorname{conv}\{x_i:i<j\}=\varnothing\) for every \(j\), and \(\widehat M(T,B)\) is the largest length of such a sequence [AMSTJ]. The order of the points matters.

**Lemma 3.1.** A sequence \(x_1,\dots,x_m\) is \(B\)-convexly separated if and only if there are \(y_1,\dots,y_m\in B^\circ\) with \(\langle y_j,x_j-x_i\rangle\ge1\) for all \(i<j\).

**Proof.** Suppose the sequence is convexly separated and \(j\ge2\). The open convex set \(x_j+\operatorname{int}B\) and the compact convex set \(C_j=\operatorname{conv}\{x_i:i<j\}\) are disjoint, so some \(\varphi\neq0\) satisfies \(\varphi(x_j+w)\ge\varphi(z)\) for all \(w\in\operatorname{int}B\) and \(z\in C_j\). Taking the infimum over \(w\), \(\varphi(x_j)-h_B(\varphi)\ge\varphi(x_i)\) for \(i<j\), and \(h_B(\varphi)>0\) because \(B\) has nonempty interior and \(\varphi\neq0\). Then \(y_j=\varphi/h_B(\varphi)\) lies in \(B^\circ\) and satisfies \(\langle y_j,x_j-x_i\rangle\ge1\); for \(j=1\) take \(y_1=0\). Conversely, if \(x_j+w=z\in C_j\) with \(w\in\operatorname{int}B\), then \(1\le\langle y_j,x_j-z\rangle=\langle y_j,-w\rangle<1\), because \(-w\) is an interior point of \(B\), so \((1+\eta)(-w)\in B\) for some \(\eta>0\). \(\square\)

**Theorem 3.2** (Artstein, Milman, Szarek, Tomczak-Jaegermann). For symmetric convex bodies \(K,B\subseteq\mathbb R^n\),
\[
\widehat M(K,B)\le\widehat M\bigl(B^\circ,\tfrac12K^\circ\bigr)^2.
\]

**Proof.** Let \(R=\max_{x\in K}\|x\|_B>0\). Let \(x_1,\dots,x_N\) be \(B\)-convexly separated in \(K\), with functionals \(y_j\) as in Lemma 3.1. Each \(|\langle y_j,x_j\rangle|\le R\). Divide \([-R,R]\) into \(\lceil4R\rceil\) intervals of length at most \(\frac12\); one of them contains \(\langle y_j,x_j\rangle\) for at least \(N/\lceil4R\rceil\) indices \(j_1<\dots<j_M\). For \(i<j\) among these indices,
\[
\langle y_i-y_j,x_i\rangle=\bigl(\langle y_i,x_i\rangle-\langle y_j,x_j\rangle\bigr)+\langle y_j,x_j-x_i\rangle\ge-\tfrac12+1=\tfrac12.
\]
So the sequence \(y_{j_M},\dots,y_{j_1}\), in this order, satisfies the criterion of Lemma 3.1 for the body \(\frac12K^\circ\) with the functionals \(2x_{j_i}\in2K=(\frac12K^\circ)^\circ\). Hence \(\widehat M(B^\circ,\frac12K^\circ)\ge N/\lceil4R\rceil\).

Second, \(R=\max_{x\in K}h_{B^\circ}(x)=\max_{y\in B^\circ}h_K(y)=\max_{y\in B^\circ}\|y\|_{K^\circ}\), so there is \(y\in B^\circ\) with \(\|y\|_{K^\circ}=R\). Points of the segment \([-y,y]\subseteq B^\circ\) listed in increasing order along it, with consecutive \(\|\cdot\|_{K^\circ}\)-distances at least \(\frac12\), are \(\frac12K^\circ\)-convexly separated: the hull of the earlier points is a segment on the line, and reaching it from the next point requires a vector of \(K^\circ\)-norm at least \(\frac12\), which is not in \(\operatorname{int}\frac12K^\circ\). There are \(\lfloor4R\rfloor+1\) such points. Hence \(\widehat M(B^\circ,\frac12K^\circ)^2\ge\frac N{\lceil4R\rceil}(\lfloor4R\rfloor+1)\ge N\). \(\square\)

**Lemma 3.3.** \(\widehat M(T,B)\le N(T,\frac14B)\).

**Proof.** If \(x_i\) and \(x_j\), \(i<j\), lay in one translate of \(\frac14B\), then \(x_i-x_j\in\frac12B\subseteq\operatorname{int}B\), and \(x_j+(x_i-x_j)=x_i\) would lie in \(\operatorname{conv}\{x_k:k<j\}\). \(\square\)

So for convexified packing a universal duality holds; the theorem of this course shows that ordinary covering numbers have none.

## 4. Exercises

**Exercise 4.1** (easy). Show that \((tK)^\circ=t^{-1}K^\circ\) and \(K\subseteq K'\Rightarrow K'^\circ\subseteq K^\circ\).

**Exercise 4.2** (easy). Show that for the Euclidean ball \(B_2^n\), \((B_2^n)^\circ=B_2^n\), and compute \(N([-1,1]^n,[-\frac12,\frac12]^n)\).

**Exercise 4.3** (medium). In Lemma 2.1, show that the factor \(3\) in the definition of \(K\) can be replaced by any number larger than \(2\), with \(6\varepsilon\) replaced by the corresponding multiple of \(2\varepsilon\).

**Exercise 4.4** (medium). Show that in dimension one, \(\widehat M([-1,1],[-\rho,\rho])=\lfloor2/\rho\rfloor+1\) for \(0<\rho\le2\), and compare with \(N([-1,1],[-\rho,\rho])=\lceil1/\rho\rceil\).

## 5. Solutions

**4.1.** \(\langle tx,y\rangle\le1\) for all \(x\in K\) iff \(ty\in K^\circ\). If \(K\subseteq K'\), the conditions defining \(K'^\circ\) include those defining \(K^\circ\).

**4.2.** By Cauchy–Schwarz, \(\langle x,y\rangle\le1\) for all \(\|x\|_2\le1\) iff \(\|y\|_2\le1\). The cube \([-1,1]^n\) is the union of \(2^n\) translates of \([-\frac12,\frac12]^n\), and a translate of the small cube contains at most one of the \(2^n\) vertices, so \(N=2^n\).

**4.3.** With \(K=c\operatorname{absconv}\{R_x\}+tB_\infty^Y\), \(c>2\), the points \(cR_x\) have pairwise distance at least \(c>2\), so the first bound in (2.1) holds, and (2.2) becomes \(h_K(\delta)=c\max_X|f_\delta|+t\|\delta\|_1\), giving the scale \(2c\varepsilon+2t\).

**4.4.** On a line, \(x_j\) must lie at distance at least \(\rho\) from the interval spanned by \(x_1,\dots,x_{j-1}\). Each new point therefore lengthens that interval by at least \(\rho\), and the interval has length at most \(2\), so \((m-1)\rho\le2\) and \(m\le\lfloor2/\rho\rfloor+1\). The points \(-1,-1+\rho,-1+2\rho,\dots\) in \([-1,1]\) attain this. Intervals of length \(2\rho\) cover \([-1,1]\) exactly when there are at least \(\lceil1/\rho\rceil\) of them. So in dimension one the two quantities agree up to a factor of about \(2\).

## References

- [AMS] S. Artstein, V. Milman and S. J. Szarek, *Duality of metric entropy*, Ann. of Math. 159 (2004); arXiv:math/0407236. https://arxiv.org/abs/math/0407236
- [AMSTJ] S. Artstein, V. Milman, S. J. Szarek and N. Tomczak-Jaegermann, *On convexified packing and entropy duality*, Geom. Funct. Anal. 14 (2004); arXiv:math/0407238. https://arxiv.org/abs/math/0407238. Conjecture 1 and Theorem 2.
- [OpenAI-E] OpenAI, *Counterexamples to the duality conjecture for metric entropy*, OpenAI Math Release preprint, 24 September 2026, Sections 1, 2 and 5. https://github.com/openai/math/blob/main/preprints/Counterexamples-to-the-duality-conjecture-for-metric-entropy-September-24-2026
