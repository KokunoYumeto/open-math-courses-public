# A weighted determinant in a biquadratic field

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson builds the determinant on which the proof of Theorem A rests. Its rows are the vectors \(\bigl(\theta_n^{\alpha_1}\sigma(\theta_n)^{\alpha_2}\sigma\tau(\theta_n)^{\alpha_3}\bigr)_n\) attached to the biquadratic field \(\mathbf Q(\sqrt d,\sqrt2)\). The interpolation theorem of [Interpolation on a projected integer box](interpolation-on-a-projected-integer-box.md) shows that enough of them span. Choosing them in the order of the weight \(\alpha_1+H\alpha_2+H\alpha_3\) puts most of the total degree into the first exponent, the one on which the Frobenius congruence of [Two bounds for the determinant](two-bounds-for-the-determinant.md) acts. The construction follows OpenAI [OpenAI-LS, Section 4]. Determinants of this kind, formed from values of monomials instead of auxiliary functions, are the *interpolation determinants* of Laurent [Laurent].

## 1. The field and the ring

Let \(\chi\), \(D\) and \(q=|D|\) be as in [Real zeros and the prime bias](real-zeros-and-the-prime-bias.md). Let \(d\) be the squarefree integer with \(\mathbf Q(\sqrt D)=\mathbf Q(\sqrt d)\): \(d=D\) if \(D\equiv1\pmod4\) and \(d=D/4\) otherwise. Then \(d\ne1\), \(|d|\le q\), and every odd prime \(p\nmid q\) satisfies \(p\nmid d\) and
\[
\chi(p)=\Bigl(\frac Dp\Bigr)=\Bigl(\frac dp\Bigr),
\]
the Legendre symbol: the Kronecker symbol is the Legendre symbol at odd primes [Dirichlet characters, Section 4](course:NT-DIRL/NT-DIRL-01#4-real-characters-and-quadratic-discriminants), and \((4/p)=1\).

Assume \(d\ne2\), that is \(q\ne8\). Fix complex numbers \(a\) and \(b\) with \(a^2=d\) and \(b^2=2\), and put
\[
K=\mathbf Q(a,b)\subset\mathbf C,\qquad\mathcal R=\mathbf Z[a,b].
\]

**Lemma 3.1.** The numbers \(1,a,b,ab\) are linearly independent over \(\mathbf Q\). Every element of \(\mathcal R\) has a unique expression \(z_1+z_2a+z_3b+z_4ab\) with \(z_i\in\mathbf Z\), and every element of \(K\) a unique expression with \(z_i\in\mathbf Q\). The maps \(\sigma\) and \(\tau\) defined by
\[
\begin{aligned}
\sigma(a)&=-a,&\sigma(b)&=b,\\
\tau(a)&=a,&\tau(b)&=-b
\end{aligned}
\]
extend to commuting field automorphisms of \(K\) that preserve \(\mathcal R\), and \(1,\sigma,\tau,\sigma\tau\) are four different automorphisms.

*Proof.* Suppose \(x_1+x_2a+x_3b+x_4ab=0\) with rational \(x_i\). If \(x_2+x_4b\ne0\), then \(a=-(x_1+x_3b)/(x_2+x_4b)\) lies in \(\mathbf Q(b)=\{u+vb:u,v\in\mathbf Q\}\). But \((u+vb)^2=u^2+2v^2+2uvb\) equals \(d\) only if \(uv=0\), and then \(d=u^2\) or \(d=2v^2\), impossible for a squarefree \(d\ne1,2\). Hence \(x_2+x_4b=0\), so \(x_2=x_4=0\) because \(b\) is irrational, and then \(x_1=x_3=0\). Since \(a^2\), \(b^2\) and \((ab)^2=2d\) are integers, products of \(1,a,b,ab\) are integer combinations of them. So \(\mathcal R\) is their \(\mathbf Z\)-span, and their \(\mathbf Q\)-span is a ring of dimension \(4\) over \(\mathbf Q\) without zero divisors, hence a field, which is \(K\). Define \(\sigma\) and \(\tau\) on coordinates by changing the signs of the coordinates of \(a,ab\), respectively of \(b,ab\). They are bijective and \(\mathbf Q\)-linear, and multiplicative because the rules \(a^2=d\), \(b^2=2\), \(ab=ba\) are unchanged when \(a\) or \(b\) changes sign. They commute and are different from each other, from \(\sigma\tau\) and from the identity, by their effect on \(a\) and \(b\). \(\square\)

For \(z\in K\) put
\[
\operatorname{Nm}(z)=z\,\sigma(z)\,\tau(z)\,\sigma\tau(z).
\]

**Lemma 3.2.** \(\operatorname{Nm}\) is multiplicative. For \(z\in K\), \(\operatorname{Nm}(z)\in\mathbf Q\), and \(\operatorname{Nm}(z)\in\mathbf Z\) when \(z\in\mathcal R\). If \(z\ne0\), then \(\operatorname{Nm}(z)\ne0\).

*Proof.* Multiplicativity is clear. Since \(\sigma\) and \(\tau\) commute and are involutions, each of them permutes the four factors of \(\operatorname{Nm}(z)\), which is therefore fixed by \(\sigma\) and by \(\tau\). An element fixed by both has zero coordinates at \(a\), \(b\) and \(ab\), so it is rational, and an integer if it lies in \(\mathcal R\). Automorphisms are injective, so the factors of \(\operatorname{Nm}(z)\) are nonzero when \(z\ne0\). \(\square\)

## 2. The points and the rows

Fix integers \(1\le H\le N\) and put
\[
U=N^{4/3},\qquad M=N^4=U^3 .
\]
For \(n\in E_N=\{0,\dots,N-1\}^4\) let \(\theta_n=n_1+n_2a+n_3b+n_4ab\in\mathcal R\). The matrix
\[
A=\begin{pmatrix}1&a&b&ab\\1&-a&b&-ab\\1&-a&-b&ab\end{pmatrix}
\]
satisfies \(An=(\theta_n,\sigma(\theta_n),\sigma\tau(\theta_n))\), by the definition of \(\sigma\) and \(\tau\) on coordinates.

**Lemma 3.3.** The map \(A:\mathbf C^4\to\mathbf C^3\) is surjective, and its kernel is spanned by \(c=(ab,b,-a,-1)\), whose four coordinates are linearly independent over \(\mathbf Q\).

*Proof.* Multiplying out, the three rows of \(A\) applied to \(c\) give
\[
\begin{aligned}
&ab+ab-ab-ab=0,\\
&ab-ab-ab+ab=0,\\
&ab-ab+ab-ab=0 .
\end{aligned}
\]
The minor formed by the first three columns is \(4ab\ne0\), so \(A\) has rank \(3\) and its kernel is the line \(\mathbf Cc\). The coordinates of \(c\) are \(\pm\) the numbers \(1,a,b,ab\) in another order, linearly independent by Lemma 3.1. \(\square\)

For \(\alpha\in\mathbf Z_{\ge0}^3\) put
\[
R_\alpha=\bigl(\theta_n^{\alpha_1}\sigma(\theta_n)^{\alpha_2}\sigma\tau(\theta_n)^{\alpha_3}\bigr)_{n\in E_N},
\]
an element of \(\mathcal R^{E_N}\), with \(z^0=1\), including \(z=0\). Thus \(R_\alpha=((An)^\alpha)_{n\in E_N}\), in the notation of Corollary 2.6. Define the *weight*
\[
w(\alpha)=\alpha_1+H\alpha_2+H\alpha_3 .
\]
Each weight is taken by finitely many \(\alpha\). Fix a total order \(\prec\) on \(\mathbf Z_{\ge0}^3\) with \(\alpha\prec\alpha'\) whenever \(w(\alpha)<w(\alpha')\), breaking ties by any fixed rule. Go through the indices in this order, and *retain* \(\alpha\) when \(R_\alpha\) is not in the \(K\)-linear span of the rows \(R_\beta\) of the indices \(\beta\prec\alpha\) retained before. Let \(\mathcal P\) be the set of retained indices.

**Lemma 3.4.** Put \(W_0=96H^{2/3}U\).

1. For every \(\alpha\), \(R_\alpha\) lies in the \(K\)-span of the rows \(R_\beta\), \(\beta\in\mathcal P\), \(\beta\preceq\alpha\).
2. \(\mathcal P\) has exactly \(M\) elements, and \(w(\alpha)\le W_0\) for every \(\alpha\in\mathcal P\).
3. The determinant \(\Delta=\det(R_\alpha)_{\alpha\in\mathcal P}\), with the rows in increasing order and the columns in a fixed order of \(E_N\), is a nonzero element of \(\mathcal R\).

*Proof.* Part 1 holds by the selection rule: either \(\alpha\) is retained, or \(R_\alpha\) is a combination of earlier retained rows. The retained rows are linearly independent over \(K\), so there are at most \(M\) of them. By Lemma 3.3, Corollary 2.6 applies to \(A\): the rows \(R_\alpha\) with \(\alpha_j\le T_j\) span \(\mathbf C^{E_N}\). The rank of a matrix with entries in \(K\) is the size of its largest nonzero minor, the same over \(K\) and over \(\mathbf C\); so these rows span \(K^{E_N}\). Each of them has weight at most
\[
T_1+HT_2+HT_3=3\cdot32H^{2/3}U=W_0 .
\]
By part 1, once all indices of weight at most \(W_0\) have been considered, the retained rows span \(K^{E_N}\). So \(M\) rows have been retained by then, and no later row is retained. The entries of \(R_\alpha\) lie in \(\mathcal R\), so \(\Delta\in\mathcal R\), and \(\Delta\ne0\) because its rows are linearly independent. \(\square\)

## 3. Where the degree lies

Put
\[
S_1=\sum_{\alpha\in\mathcal P}\alpha_1,\qquad S_2=\sum_{\alpha\in\mathcal P}(\alpha_2+\alpha_3).
\]

**Lemma 3.5** (OpenAI). Let \(c_0=(4\cdot97^2)^{-1}\) and \(C_0=192\). If \(1\le H\le N\) and \(H^{2/3}N^{4/3}\ge2\cdot97^2\), then
\[
\begin{aligned}
S_1&\ge c_0MH^{2/3}U,\\
S_2&\le C_0MH^{-1/3}U .
\end{aligned}
\]
In particular \(S_2\le(C_0/c_0)S_1/H\).

*Proof.* For \(\alpha\in\mathcal P\), \(H\alpha_2\le w(\alpha)\le W_0\), so \(\alpha_2\le B:=96H^{-1/3}U\), and likewise \(\alpha_3\le B\). Hence \(S_2\le2BM=C_0MH^{-1/3}U\).

For a fixed value of \(\alpha_1\), at most \(Q_0=(\lfloor B\rfloor+1)^2\) retained indices have that first coordinate. As \(H\le N\), \(H^{-1/3}U\ge N^{-1/3}N^{4/3}\ge1\), so \(\lfloor B\rfloor+1\le97H^{-1/3}U\) and
\[
Q_0\le97^2H^{-2/3}U^2 .
\]
List the first coordinates of the retained indices as \(b_1\le\dots\le b_M\). The values \(0,\dots,j-1\) occupy at most \(jQ_0\) places, so \(b_i\ge\lfloor(i-1)/Q_0\rfloor\). Write \(M=kQ_0+r\) with \(0\le r<Q_0\). Then
\[
\begin{aligned}
S_1&\ge\sum_{i=1}^M\Bigl\lfloor\frac{i-1}{Q_0}\Bigr\rfloor=Q_0\frac{k(k-1)}2+kr\\
&=\frac{M^2}{2Q_0}-\frac M2+\frac{r(Q_0-r)}{2Q_0}\\
&\ge\frac{M^2}{2Q_0}-\frac M2 .
\end{aligned}
\]
The hypothesis gives \(M=U^3\ge2\cdot97^2H^{-2/3}U^2\ge2Q_0\), so \(\frac M2\le\frac{M^2}{4Q_0}\) and
\[
\begin{aligned}
S_1\ge\frac{M^2}{4Q_0}&\ge\frac{U^3\,M}{4\cdot97^2H^{-2/3}U^2}\\
&=c_0MH^{2/3}U .
\end{aligned}
\]
\(\square\)

The constants do not depend on \(d\) or on the tie-breaking rule. For \(N=2\) and \(d=5\), a computation with exact arithmetic in \(K\), breaking ties by the smaller value of \(\alpha_2+\alpha_3\) and then of \(\alpha_2\), gives \((S_1,S_2)=(22,14)\), \((40,8)\) and \((45,7)\) for \(H=2,3,5\). The share of the second exponent sum falls as \(H\) grows.

## 4. Exercises

**3.1** (easy). Show that the sixteen points \(An\), \(n\in E_2\), are pairwise distinct, and more generally that \(n\mapsto An\) is injective on \(\mathbf Z^4\).

**3.2** (medium). Suppose \(H\ge M\). Show that \(\mathcal P=\{(j,0,0):0\le j<M\}\), that \(S_2=0\), and that \(\Delta=\pm\prod_{n<n'}(\theta_{n'}-\theta_n)\) for a suitable order of \(E_N\).

**3.3** (easy). Compute \(\operatorname{Nm}(z_1+z_2a)\) for \(z_1,z_2\in\mathbf Z\), and show that \(\operatorname{Nm}(b)=4\).

**3.4** (easy). In Lemma 3.5, check the identity \(Q_0\frac{k(k-1)}2+kr=\frac{M^2}{2Q_0}-\frac M2+\frac{r(Q_0-r)}{2Q_0}\) for \(M=kQ_0+r\).

## 5. Solutions

**3.1.** If \(An=An'\), the first coordinates give \(\theta_n=\theta_{n'}\), and Lemma 3.1 gives \(n=n'\).

**3.2.** The indices \((j,0,0)\) with \(j<M\) have weight \(j<H\), while every index with \(\alpha_2+\alpha_3\ge1\) has weight at least \(H\). So these \(M\) indices come first, in increasing order of \(j\). Their rows form the Vandermonde matrix \((\theta_n^j)\), whose determinant \(\prod_{n<n'}(\theta_{n'}-\theta_n)\) is nonzero by Exercise 3.1. So all of them are retained, and \(\mathcal P\) is complete with \(M\) elements.

**3.3.** Since \(\tau\) fixes \(z_1\pm z_2a\),
\[
\begin{aligned}
\operatorname{Nm}(z_1+z_2a)&=(z_1+z_2a)^2(z_1-z_2a)^2\\
&=(z_1^2-dz_2^2)^2 .
\end{aligned}
\]
And \(\operatorname{Nm}(b)=b\cdot b\cdot(-b)\cdot(-b)=b^4=4\).

**3.4.** Expand \(\frac{(kQ_0+r)^2}{2Q_0}=\frac{k^2Q_0}2+kr+\frac{r^2}{2Q_0}\) and subtract \(\frac{kQ_0+r}2\); adding \(\frac{r(Q_0-r)}{2Q_0}=\frac r2-\frac{r^2}{2Q_0}\) leaves \(\frac{k^2Q_0}2-\frac{kQ_0}2+kr\).

## References

- [OpenAI-LS] OpenAI, *Uniform exclusion of Landau–Siegel zeros*, OpenAI Math Release preprint, 1 October 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026
- [Laurent] M. Laurent, *Sur quelques résultats récents de transcendance*, Astérisque 198–200 (1991), 209–230. https://www.numdam.org/item/AST_1991__198-199-200__209_0/
