# Siegel's lemma, analytic estimates and the six exponentials theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol at Ultra. Public domain (CC0).*

Hermite and Lindemann built their auxiliary polynomials explicitly. A more flexible method chooses many coefficients at once, requiring their function to vanish at a large set of points. Linear algebra supplies a solution; Siegel's lemma supplies a solution whose arithmetic size is controlled. Analysis then makes a new value small, while an integral norm prevents it from being too small. The six exponentials theorem is a complete example in which all three estimates can be seen together.

We use the height conventions of Heights of algebraic numbers. In particular, the **house** of an algebraic number is

\[
 \overline{\alpha}=\max_{\sigma:\mathbb Q(\alpha)\hookrightarrow\mathbb C}
 |\sigma(\alpha)|.
\]

It is not the naive polynomial height or the absolute multiplicative height. If \(\alpha\in K\), taking the maximum over all embeddings of the number field \(K\) gives the same house, since every embedding of \(\mathbb Q(\alpha)\) extends to \(K\).

Two exact internal number-field prerequisites are used. The existing course *Number fields*, lesson *Algebraic integers and rings of integers*, Propositions 1.1–1.2, supplies the ring property of algebraic integers, denominator clearing, embeddings and the integrality of norms. Its lesson *Discriminants and integral bases*, Proposition 2.1 and Theorem 2.3, supplies the following statements for every number field \(K/\mathbb Q\) of degree \(D\): the embedding matrix of any \(\mathbb Q\)-basis is invertible, and \(\mathcal O_K\) has an integral basis of \(D\) elements. These number-field results supply the basis and denominator statements needed in the construction below.

We prove the required analytic estimates below from convergent local Taylor series. The exact open prerequisite is Theorem 3.3.1 of the Complex Analysis source, Jiří Lebl's [*Guide to Cultivating Complex Analysis*](https://www.jirka.org/ca/ca.pdf), version 1.9, July 11, 2026; Theorem 3.3.3 also proves the repeated holomorphic differentiability used with those series. The linked proofs retain [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), selected from the book's dual licence. Every auxiliary-function estimate used in this lesson is proved below.

## 1. Small solutions of integer equations

A homogeneous system with more unknowns than equations has a nonzero rational solution. Clearing its denominators proves existence of an integer solution, but gives no useful bound. Counting points in a box gives both existence and a bound.

### Lemma 5.1. Siegel's lemma with row sums

Let \(0<M<N\), let \(u_{ij}\in\mathbb Z\), and let real numbers \(A_i\) satisfy

\[
 A_i\geq\max\left(1,\sum_{j=1}^N|u_{ij}|\right)
 \qquad(1\leq i\leq M).
\]

There is a nonzero vector \(x\in\mathbb Z^N\) such that

\[
 \sum_{j=1}^N u_{ij}x_j=0\quad(1\leq i\leq M),\qquad
 \max_j|x_j|\leq
 B:=\left(\prod_{i=1}^M A_i\right)^{1/(N-M)}.
 \tag{5.1}
\]

In particular, if \(|u_{ij}|\leq U\) with \(U\geq1\), one can take

\[
 \max_j|x_j|\leq(NU)^{M/(N-M)}.
 \tag{5.2}
\]

**Proof.** Put \(H=\lfloor B\rfloor\), and map the \((H+1)^N\) integer vectors in \(\{0,\ldots,H\}^N\) to their \(M\) left sides. For row \(i\), let \(P_i\) be the sum of its positive coefficients and \(Q_i\) the sum of the absolute values of its negative coefficients. The image in that coordinate lies in the integer interval

\[
 [-HQ_i,HP_i],
\]

which has at most

\[
 H(P_i+Q_i)+1\leq HA_i+1\leq A_i(H+1)
\]

elements. Thus the whole image has at most

\[
 \left(\prod_i A_i\right)(H+1)^M
 =B^{N-M}(H+1)^M<(H+1)^N
\]

elements: the last inequality is strict because \(H+1>B\), even when \(B\) is an integer. Two distinct input vectors have the same image. Their difference is nonzero, solves the system, and has coordinates of absolute value at most \(H\leq B\). Taking every \(A_i=NU\) gives (5.2). \(\square\)

The use of a one-sided input box is what avoids an unnecessary factor of two. The row-sum version also recognizes a sparse or unusually small row.

**Example.** Consider

\[
 x_1+2x_2-x_3=0,\qquad 2x_1-x_2+x_3=0.
\]

Both row sums are \(4\). Formula (5.1) gives \(\max|x_j|\leq16\), while the entrywise bound \(U=2\) gives \(36\). In fact, substituting \(x_3=x_1+2x_2\) yields \(x_2=-3x_1\) and \(x_3=-5x_1\). Every integer solution is a multiple of \((1,-3,-5)\), so the smallest possible nonzero maximum is \(5\). Siegel's lemma is a uniform existence estimate, not a claim to find the shortest vector.

## 2. Passing to a number field

Fix an integral basis \(\omega_1,\ldots,\omega_D\) of \(\mathcal O_K\), and enumerate the embeddings \(\sigma_1,\ldots,\sigma_D:K\hookrightarrow\mathbb C\). Write

\[
 E=(\sigma_t(\omega_k))_{t,k},\qquad
 \eta=\max_k\sum_t|(E^{-1})_{kt}|,\qquad
 \Omega=\max_t\sum_k|\sigma_t(\omega_k)|.
\]

The prerequisite discriminant theorem guarantees that \(E\) is invertible. If

\[
 \alpha=\sum_k a_k\omega_k\in\mathcal O_K,
\]

then \(a_k\in\mathbb Z\) and inversion of \(E\) gives

\[
 |a_k|\leq\eta\overline\alpha.
 \tag{5.3}
\]

Multiplication in the integral basis has integer structure constants:

\[
 \omega_k\omega_\ell=\sum_m c_{k\ell m}\omega_m,
 \qquad c_{k\ell m}\in\mathbb Z.
\]

Set

\[
 \kappa=\max_{\ell,m}\sum_k|c_{k\ell m}|,\qquad
 C=\max\{1,\Omega,D\max(1,\eta\kappa)\}.
 \tag{5.4}
\]

This is one explicit choice of a constant depending only on the fixed field and basis.

### Lemma 5.2. Siegel's lemma over the ring of integers

For \(N>M>0\), suppose \(\alpha_{ij}\in\mathcal O_K\) and \(\overline{\alpha_{ij}}\leq A\), where \(A\geq1\). Then there is a nonzero vector \(x\in\mathcal O_K^N\) satisfying

\[
 \sum_j\alpha_{ij}x_j=0\quad(1\leq i\leq M),\qquad
 \overline{x_j}\leq C(CNA)^{M/(N-M)}.
 \tag{5.5}
\]

The constant in (5.4) is sufficient. If instead \(\alpha_{ij}\in K\) have house at most \(A\), and positive integers \(d_i\) clear the denominators in row \(i\), then with \(d=\max_i d_i\) the bound is

\[
 \overline{x_j}\leq C(CNdA)^{M/(N-M)}.
 \tag{5.6}
\]

**Proof.** Write \(\alpha_{ij}=\sum_k a_{ijk}\omega_k\) and seek \(x_j=\sum_\ell y_{j\ell}\omega_\ell\), with integer unknowns \(y_{j\ell}\). Equation (5.3) bounds \(|a_{ijk}|\) by \(\eta A\). Comparing basis coordinates, the original system becomes the \(DM\) integer equations

\[
 \sum_{j=1}^N\sum_{\ell=1}^D
 \left(\sum_k a_{ijk}c_{k\ell m}\right)y_{j\ell}=0
 \qquad(1\leq i\leq M,\ 1\leq m\leq D).
\]

Each coefficient has absolute value at most \(\eta\kappa A\). Apply (5.2) to these \(DN\) unknowns with

\[
 U=\max(1,\eta\kappa)A.
\]

The exponent is unchanged:

\[
 \frac{DM}{DN-DM}=\frac{M}{N-M}.
\]

We obtain a nonzero integer vector \(y\) with

\[
 |y_{j\ell}|\leq(DNU)^{M/(N-M)}
 \leq(CNA)^{M/(N-M)}.
\]

Linear independence of the integral basis ensures that the corresponding vector \(x\) is nonzero. For every embedding,

\[
 |\sigma_t(x_j)|
 \leq\sum_\ell |y_{j\ell}|\,|\sigma_t(\omega_\ell)|
 \leq\Omega(CNA)^{M/(N-M)}.
\]

This proves (5.5). For (5.6), multiply the \(i\)-th equation by \(d_i\). Its coefficients are now algebraic integers of house at most \(dA\), and its solution set is unchanged. \(\square\)

The number of embeddings introduces constants but does not multiply the Siegel exponent. This cancellation will matter when the number field containing our assumed algebraic values has a large degree.

## 3. Zeros and analytic size

For a function analytic on a neighbourhood of the closed disc \(|z|\leq R\), write

\[
 |f|_R=\max_{|z|=R}|f(z)|.
\]

We first justify why the boundary controls the whole disc.

### Proposition 5.3. Maximum modulus

If an analytic function on a connected open set has a local maximum of its modulus at an interior point, it is constant. Consequently an analytic function on a neighbourhood of a closed disc satisfies

\[
 \max_{|z|\leq R}|f(z)|=|f|_R.
\]

**Proof.** Let the local maximum occur at \(z_0\). On a sufficiently small disc its convergent Taylor expansion is

\[
 f(z_0+w)=\sum_{k\geq0}a_kw^k.
\]

For a small fixed \(r>0\), uniform convergence permits termwise integration of the product of this series and its conjugate. The integrals of \(e^{i(k-\ell)t}\) vanish unless \(k=\ell\), so

\[
 \frac1{2\pi}\int_0^{2\pi}|f(z_0+re^{it})|^2\,dt
 =\sum_{k\geq0}|a_k|^2r^{2k}.
\]

The local maximum makes the left side at most \(|a_0|^2\). All other coefficients must vanish, and \(f\) is constant near \(z_0\).

For completeness, an analytic function equal to a constant on a nonempty open subset is equal to it throughout a connected domain. A nonzero local Taylor series has a first nonzero coefficient; factoring out its corresponding power shows its zeros are isolated. Thus zeros with an interior limit point force the local series to vanish identically. The set of points having a neighbourhood on which \(f\) equals the given constant is both open and closed in the domain, and hence is the whole domain. This proves the first assertion. A maximum on a compact disc exists by continuity; if an interior maximum occurs, the function is constant, and otherwise a maximum occurs on its boundary. \(\square\)

### Lemma 5.4. Schwarz's estimate with multiplicity

If \(\Psi\) is analytic on a neighbourhood of \(|z|\leq R\) and has a zero of order at least \(T\geq0\) at \(0\), then for \(0<r\leq R\),

\[
 |\Psi|_r\leq\left(\frac rR\right)^T|\Psi|_R.
 \tag{5.7}
\]

**Proof.** The function \(g(z)=\Psi(z)/z^T\) extends analytically to \(0\) by its Taylor series. On \(|z|=R\) it has modulus at most \(|\Psi|_R/R^T\). Proposition 5.3 bounds it by the same quantity throughout the disc, and multiplication by \(|z|^T\leq r^T\) gives (5.7). \(\square\)

### Lemma 5.5. Jensen's inequality

Suppose \(f\) is analytic on a neighbourhood of \(|z|\leq R\) and \(f(0)\ne0\). List its zeros in \(|z|<R\), with multiplicity, as \(z_1,\ldots,z_q\). Then

\[
 |f(0)|\leq|f|_R\prod_{j=1}^q\frac{|z_j|}{R}.
 \tag{5.8}
\]

If \(\nu(x)\) counts its zeros in \(|z|<x\), with multiplicity, then

\[
 \int_0^R\frac{\nu(x)}x\,dx
 \leq\log|f|_R-\log|f(0)|.
 \tag{5.9}
\]

**Proof.** There are finitely many zeros in the closed disc: otherwise compactness supplies an interior accumulation point in the neighbourhood of analyticity, contradicting isolation of zeros. None of the listed zeros is \(0\). Remove their factors and form

\[
 g(z)=f(z)\prod_{j=1}^q
 \frac{R^2-\overline{z_j}z}{R(z-z_j)}.
\]

The apparent poles are removable by the specified multiplicities. On \(|z|=R\),

\[
 |R^2-\overline{z_j}z|^2
 =R^2|z-z_j|^2,
\]

so each quotient has modulus \(1\). Hence \(|g|_R=|f|_R\), while

\[
 |g(0)|=|f(0)|\prod_j\frac R{|z_j|}.
\]

Maximum modulus proves (5.8). Taking logarithms and summing the integrals

\[
 \log\frac R{|z_j|}=\int_{|z_j|}^R\frac{dx}{x}
\]

gives (5.9). Zeros on the boundary contribute neither to the list nor to the integral, so they cause no exceptional case. \(\square\)

### Corollary 5.6. A growth bound controls the number of zeros

Let \(f\) be a nonzero entire function, and suppose, for fixed \(a,b\geq0\) and \(\rho>0\), that

\[
 \log|f|_R\leq a+bR^\rho\qquad(R\geq1).
 \tag{5.10}
\]

Then \(\nu_f(R)=O_f(R^\rho)\). More explicitly, let \(T\) be the order of its zero at \(0\), and set \(g=f/z^T\), so \(g(0)\ne0\). For \(R\geq1\),

\[
 \nu_f(R)\leq T+
 \frac{a+b(2R)^\rho-T\log(2R)-\log|g(0)|}{\log2}.
 \tag{5.11}
\]

**Proof.** Every zero of \(g\) in \(|z|<R\) contributes at least \(\log2\) to (5.9) on the disc of radius \(2R\). Consequently

\[
 \nu_g(R)\log2\leq\log|g|_{2R}-\log|g(0)|.
\]

On the boundary, \(|g|_{2R}=|f|_{2R}/(2R)^T\). Use (5.10), and add the \(T\) zeros at the origin. Dropping the nonpositive term \(-T\log(2R)\) gives the asserted \(O\)-bound. \(\square\)

Here the required convention is the explicit bound (5.10), sometimes called **strict order at most \(\rho\)** or a growth bound of exponent \(\rho\). The usual order

\[
 \limsup_{R\to\infty}
 \frac{\log\log\max(e,|f|_R)}{\log R}
\]

being at most \(\rho\) only guarantees analogous bounds with exponent \(\rho+\varepsilon\), for every \(\varepsilon>0\); it need not guarantee (5.10) at the endpoint. We will always display the bound actually used. In particular a finite exponential sum has \(\log|f|_R\leq a+bR\), so its zero count is \(O_f(R)\).

### Lemma 5.7. Estimating a value from many prescribed zeros

Suppose \(f\) is analytic on a neighbourhood of \(|z|\leq R\) and vanishes at distinct points \(v_1,\ldots,v_q\) with \(|v_j|\leq V<R\). If \(|w|<R\) and \(w\ne v_j\), then

\[
 |f(w)|\leq |f|_R
 \prod_{j=1}^q\frac{|w-v_j|}{R-V}.
 \tag{5.12}
\]

**Proof.** Divide \(f(z)\) by \(\prod_j(z-v_j)\). The quotient extends analytically across the listed zeros, and on the boundary its modulus is at most \(|f|_R/(R-V)^q\). Apply maximum modulus and then multiply back at \(w\). \(\square\)

Unlike (5.8), this estimate is centred at a new evaluation point and needs no assumption about \(f(0)\). Counting each prescribed point once is enough; any additional multiplicities can only improve the estimate.

## 4. The six exponentials theorem

### Theorem 5.8. Six exponentials

Let \(x_1,x_2\in\mathbb C\) be linearly independent over \(\mathbb Q\), and let \(y_1,y_2,y_3\in\mathbb C\) be linearly independent over \(\mathbb Q\). Then at least one of the six numbers

\[
 e^{x_i y_j}\qquad(1\leq i\leq2,\ 1\leq j\leq3)
\]

is transcendental.

The theorem is due to Siegel, Lang and Ramachandra. Soundararajan's notes, §12, give the same auxiliary-function proof; Waldschmidt's *Transcendence Methods*, Theorem 3.2.1, obtains the theorem by Schneider's method, with either set of numbers in the role of the exponents. All constants below depend on the six fixed numbers and their number field, never on the parameters \(n\) and \(s\).

**Proof.** Suppose all six numbers

\[
 b_{ij}=e^{x_i y_j}
\]

are algebraic, and let \(K\subset\mathbb C\) contain them. Put \(D=[K:\mathbb Q]\). Choose a positive integer \(d\) such that every \(db_{ij}\) is an algebraic integer, and put

\[
 B=\max(1,\overline{b_{11}},\ldots,\overline{b_{23}}),
 \quad X=|x_1|+|x_2|,
 \quad Y=|y_1|+|y_2|+|y_3|.
\]

Both \(X\) and \(Y\) are positive. Let \(C\geq1\) be the constant in Lemma 5.2 for this field.

**Constructing the function.** Choose an integer \(n\geq2\), to be made sufficiently large, and set

\[
 r=\lceil8n^{3/2}\rceil.
\]

Thus

\[
 64n^3\leq r^2,\qquad r\leq9n^{3/2},\qquad
 \frac{n^3}{r^2-n^3}\leq\frac1{63}.
 \tag{5.13}
\]

Seek coefficients \(a_{uv}\in\mathcal O_K\), not all zero, such that

\[
 F(z)=\sum_{u,v=1}^r a_{uv}e^{(ux_1+vx_2)z}
 \tag{5.14}
\]

vanishes at every point

\[
 z_k=k_1y_1+k_2y_2+k_3y_3,
 \qquad 1\leq k_j\leq n.
 \tag{5.15}
\]

There are \(n^3\) linear equations in \(r^2\) unknowns. Their coefficients belong to \(K\), since

\[
 e^{(ux_1+vx_2)z_k}
 =\prod_{j=1}^3 b_{1j}^{uk_j}b_{2j}^{vk_j}.
 \tag{5.16}
\]

The total exponent in this product is at most \(6rn\). Consequently its house is at most \(B^{6rn}\), and multiplication by \(d^{6rn}\) makes it integral: write each factor as a power of \(db_{ij}\), and fill any unused denominator powers with the integer \(d\).

Lemma 5.2 gives a nonzero coefficient vector with

\[
 \overline{a_{uv}}
 \leq C\bigl(Cr^2(dB)^{6rn}\bigr)^{1/63}
 \leq e^{c_1n^{5/2}},
 \tag{5.17}
\]

where, for example, the fixed positive constant

\[
 c_1=1+\log C+
 \frac{\log C+2\log9+3+54\log(dB)}{63}
\]

is sufficient. Indeed, \(rn\leq9n^{5/2}\), \(2\log r\leq2\log9+3\log n\), and \(\log n\leq n^{5/2}\). The ceiling in \(r\) is essential: the equation \(r^2=64n^3\) need not have an integer solution. The inequalities (5.13) retain the desired exponent without this defect.

**Nonvanishing and a first new point.** The frequencies \(ux_1+vx_2\) are pairwise distinct. An equality between two of them would give a nonzero integer relation between \(x_1\) and \(x_2\). Exponentials with distinct frequencies \(\lambda_1,\ldots,\lambda_N\) are linearly independent: differentiating an identically zero relation at \(0\), for orders \(0,\ldots,N-1\), gives the matrix \((\lambda_j^k)_{0\leq k<N,\,1\leq j\leq N}\). Its determinant is

\[
 \prod_{i<j}(\lambda_j-\lambda_i)\ne0.
\]

The determinant identity follows by observing that it is an alternating polynomial of the same total degree as this product, divisible by every difference, with coefficient \(1\) in its leading term. Thus the coefficient vector in (5.17) makes \(F\) a nonzero entire function.

For every \(R>0\),

\[
 |F|_R\leq r^2\exp(c_1n^{5/2}+rXR).
 \tag{5.18}
\]

With \(n\) fixed, Corollary 5.6 therefore gives only \(O_F(R)\) zeros in a disc of radius \(R\). In contrast, the positive box

\[
 \{k_1y_1+k_2y_2+k_3y_3:1\leq k_j\leq t\}
\]

has \(t^3\) distinct points, all of modulus at most \(Yt\). Distinctness follows from the rational independence of the three \(y_j\). These boxes cannot all consist of zeros of \(F\), since \(t^3\) eventually exceeds \(O_F(Yt)\). Notice that the zero-count constant may depend on \(n\); the argument only needs it for each single function.

There is therefore a largest integer \(s\) such that \(F\) vanishes on the whole box \(1\leq k_j\leq s\). It satisfies \(s\geq n\). In the next box choose

\[
 w=k_1y_1+k_2y_2+k_3y_3,
 \qquad1\leq k_j\leq s+1,
 \qquad F(w)\ne0.
 \tag{5.19}
\]

At least one coordinate \(k_j\) equals \(s+1\). No assertion about discreteness or density of the positive boxes is required.

**The arithmetic lower bound.** By (5.16), now with \(k_j\leq s+1\),

\[
 \Theta=d^{6r(s+1)}F(w)
\]

is a nonzero algebraic integer in \(K\). For every embedding \(\sigma:K\hookrightarrow\mathbb C\), applying it to the algebraic products in (5.16) gives

\[
 |\sigma(\Theta)|
 \leq r^2\exp(c_1n^{5/2})(dB)^{6r(s+1)}
 \leq\exp(c_2s^{5/2}),
 \tag{5.20}
\]

where one may take

\[
 c_2=c_1+108\log(dB)+2\log9+3.
\]

Here \(n\leq s\), \(r\leq9s^{3/2}\) and \(s+1\leq2s\) have all been used. The norm is a nonzero integer, so

\[
 1\leq|N_{K/\mathbb Q}(\Theta)|
 \leq |\Theta|\exp((D-1)c_2s^{5/2}).
\]

Undoing the denominator yields

\[
 \log|F(w)|\geq-c_3s^{5/2},
 \qquad c_3=108\log d+(D-1)c_2.
 \tag{5.21}
\]

The norm is taken only of an algebraic value at a point of the prescribed additive group. No field automorphism is applied to \(x_i\), \(y_j\) or an arbitrary transcendental exponential.

**The analytic upper bound.** Choose

\[
 R=s^{3/2}.
\]

Take \(n\) sufficiently large that \(\sqrt n>4Y\). Then \(R>2Y(s+1)\), so the circle encloses \(w\) and the preceding \(s^3\) zeros. Every preceding zero \(z_k\) has \(|z_k|\leq Ys\), while

\[
 |w-z_k|\leq Y(s+1)+Ys\leq3Ys,
 \qquad R-Ys>R/2.
\]

Lemma 5.7 gives

\[
 |F(w)|\leq|F|_R\left(\frac{6Ys}{R}\right)^{s^3}.
 \tag{5.22}
\]

Put \(C_0=\max(1,6Y)\). Combining (5.18) and (5.22), and using \(r\leq9s^{3/2}\), gives

\[
 \begin{aligned}
 \log|F(w)|
 &\leq2\log r+c_1n^{5/2}+rXs^{3/2}
      +s^3\left(\log C_0-\tfrac12\log s\right)\\
 &\leq c_4s^{5/2}+K_0s^3-\tfrac12s^3\log s,
 \end{aligned}
 \tag{5.23}
\]

where

\[
 c_4=c_1+2\log9+3,\qquad K_0=9X+\log C_0.
\]

Bounds (5.21) and (5.23) together require

\[
 \frac12\log s\leq K_0+\frac{c_3+c_4}{\sqrt s}.
 \tag{5.24}
\]

Finally choose \(n\) so large that, in addition to the radius requirement,

\[
 \frac12\log n>K_0+\frac{c_3+c_4}{\sqrt n}.
\]

Such integers exist since the left side grows without bound. For every \(s\geq n\), the left side of (5.24) is at least \(\frac12\log n\) and its right side at most the displayed right side with \(n\). This is a contradiction. The assumption that all six exponentials are algebraic was false. \(\square\)

The estimates can be read from the following parameter table. Constants in the bounds are fixed before \(n\) is chosen.

| Quantity | Choice or bound | Role |
|---|---|---|
| Initial zeros | \(n^3\) | Three independent directions of evaluation |
| Frequencies | \(r^2\geq64n^3\) | More coefficients than equations |
| Siegel exponent | \(n^3/(r^2-n^3)\leq1/63\) | Keeps coefficients small |
| Coefficient log house | \(c_1n^{5/2}\) | Arithmetic cost of constructing \(F\) |
| Last complete box | \(s\geq n\), containing \(s^3\) zeros | Selects a nonzero algebraic value in the next box |
| Radius | \(R=s^{3/2}\) | Larger than the box; still controls growth |
| Arithmetic lower bound | \(-c_3s^{5/2}\) for \(\log\lvert F(w)\rvert\) | Integral norm cannot be arbitrarily small |
| Analytic upper bound | \(-\tfrac12s^3\log s+K_0s^3+c_4s^{5/2}\) | Gain from many zeros dominates both costs |

The role of the last complete box is worth emphasizing. An initial set of zeros does not ensure that a conveniently chosen nearby value is nonzero. Choosing \(s\) makes nonvanishing automatic at some point of the next box, while preserving the relation \(s\geq n\) needed in every estimate.

## 5. Powers of algebraic numbers and the four exponentials problem

For a positive real number \(a\) and \(t\in\mathbb C\), use

\[
 a^t=e^{t\log a},
\]

where \(\log a\) is its real logarithm. For general nonzero complex \(\alpha\), a power in this lesson always means \(e^{t\lambda}\) with a fixed choice \(\lambda\) satisfying \(e^\lambda=\alpha\).

### Corollary 5.9. Three prime bases

If \(t\in\mathbb C\) and \(2^t,3^t,5^t\) are all algebraic, then \(t\in\mathbb Q\). If all three are integers, then \(t\) is a nonnegative integer. In particular at least one of \(2^\pi,3^\pi,5^\pi\) is transcendental.

**Proof.** The real numbers \(\log2,\log3,\log5\) are linearly independent over \(\mathbb Q\). Clearing a rational relation would give

\[
 2^a3^b5^c=1\qquad(a,b,c\in\mathbb Z),
\]

and unique prime factorization, after moving negative exponents to the other side, forces \(a=b=c=0\). If \(t\notin\mathbb Q\), the pair \(1,t\) is rationally independent. Theorem 5.8 applied to these two pairs would make at least one of

\[
 2,3,5,2^t,3^t,5^t
\]

transcendental, a contradiction.

Write the resulting rational \(t=a/b\) in lowest terms, with \(b>0\). If \(2^t\) is an integer, it is positive. A negative \(a\) would make it strictly between \(0\) and \(1\), so \(a\geq0\). If \(a=0\), then \(t=0\). Otherwise set \(u=2^{a/b}\in\mathbb Z_{>0}\). From \(u^b=2^a\), prime valuations give \(b\,v_2(u)=a\). Thus \(b\mid a\), and coprimality forces \(b=1\). The final assertion follows since \(\pi\) is irrational, as already implied by its transcendence in the preceding lesson. \(\square\)

### Corollary 5.10. Three multiplicatively independent algebraic bases

Let \(\alpha_1,\alpha_2,\alpha_3\) be nonzero algebraic numbers with no nontrivial relation \(\prod_j\alpha_j^{m_j}=1\), \(m_j\in\mathbb Z\). Fix any logarithms \(\lambda_j\) of these numbers. If all three \(e^{\beta\lambda_j}\) are algebraic, then \(\beta\in\mathbb Q\).

**Proof.** A rational linear relation between the \(\lambda_j\), after clearing denominators and exponentiating, would give precisely a forbidden multiplicative relation. Hence the three logarithms are rationally independent, regardless of their chosen branches. If \(1,\beta\) were rationally independent, Theorem 5.8 would contradict the algebraicity of the six numbers \(\alpha_j,e^{\beta\lambda_j}\). Thus \(\beta\) is rational. Conversely, for \(\beta=a/b\), \(b>0\), any such branch value satisfies \(X^b-\alpha_j^a=0\) and is algebraic by closure of the algebraic numbers. \(\square\)

**The four exponentials conjecture.** If \(x_1,x_2\) are rationally independent complex numbers and \(y_1,y_2\) are rationally independent complex numbers, at least one of the four \(e^{x_i y_j}\) should be transcendental. This is Schneider's four exponentials problem, also discussed by Lang and Ramachandra. It remains a conjecture; the six exponentials proof above does not prove it. Waldschmidt's *The Four Exponentials Problem and the Schanuel Conjecture*, §4, discusses the formulation and its relation to logarithms.

Conditional on this conjecture, the same proof as Corollary 5.9, using only \(\log2,\log3\), would show that algebraicity of \(2^t\) and \(3^t\) forces \(t\in\mathbb Q\). If both were integers, it would then force a nonnegative integer. It would also show that at least one of \(2^\pi,3^\pi\) is transcendental. These are conditional statements, not consequences claimed from the six exponentials theorem alone.

The dimension balance explains the difficulty. Two evaluation directions supply \(s^2\) zeros, while the two frequency directions require \(r\) of order \(n\). Making the radius much larger than the box then costs too much exponential growth. The final exercise makes this obstruction precise; it concerns this particular construction, not a proof that every auxiliary-function method must fail.

## 6. Exercises

1. **Easy — row sums.** Prove Lemma 5.1 directly by counting a one-sided integer box. Explain why the comparison is strict even if \((A_1\cdots A_M)^{1/(N-M)}\) is an integer. Compute the two stated bounds and the smallest nonzero solution size for the two-equation example.

2. **Easy — prime powers.** Prove that at least one of \(2^\pi,3^\pi,5^\pi\) is transcendental. State exactly which logarithms are being used and why their rational independence holds.

3. **Medium — complex branches.** Suppose three nonzero algebraic numbers \(\alpha_j\) are multiplicatively independent. Fix arbitrary logarithms \(\lambda_j\). If \(e^{\beta\lambda_j}\) is algebraic for each \(j\), prove that \(\beta\) is rational. Check that changing the fixed logarithms does not invalidate the argument.

4. **Medium — removing zeros.** Prove Jensen's inequality by applying maximum modulus to

   \[
   f(z)\prod_j\frac{R^2-\overline{z_j}z}{R(z-z_j)}.
   \]

   Verify the boundary identity, removable singularities, multiplicities and the case of zeros on the outer circle.

5. **Hard — the missing dimension.** Repeat the construction with two evaluation directions. Take \(r=\lceil cn\rceil\), with fixed \(c>1\), and compare the scales of the coefficient bound, arithmetic lower bound and zero gain when \(s=n\). Show why a radius \(R=n^q\) with \(q>1\) cannot give the same asymptotic contradiction. Also analyze \(R=tn\) with fixed \(t\). More generally, if there are \(a\) frequency directions and \(b\) evaluation directions, derive the necessary interval for \(q\) in this power-counting argument.

## 7. Solutions

1. Put \(B=(\prod_iA_i)^{1/(N-M)}\) and \(H=\lfloor B\rfloor\). Row \(i\) maps \(\{0,\ldots,H\}^N\) into an integer interval of length \(H\sum_j|u_{ij}|\), containing at most \(A_i(H+1)\) integers. The whole image therefore contains at most \(B^{N-M}(H+1)^M\) points, strictly fewer than \((H+1)^N\), since \(H+1>B\). Subtract two inputs with equal image to obtain the required nonzero kernel vector of maximum at most \(H\). This includes integer \(B\), for which \(H+1=B+1\). In the example the row sums give \(4\cdot4=16\); \(N=3,M=2,U=2\) gives \(6^2=36\). Elimination gives all integer solutions \(k(1,-3,-5)\); a nonzero integer \(k\) has \(|k|\geq1\), so the minimum maximum is \(5\).

2. Use the real logarithms. A rational relation among \(\log2,\log3,\log5\) becomes \(2^a3^b5^c=1\) after clearing denominators and exponentiating. Prime factorization gives \(a=b=c=0\). The pair \(1,\pi\) is rationally independent because \(\pi\) is irrational. If the three displayed powers were algebraic, all six entries for these pairs would be algebraic, contradicting Theorem 5.8. The theorem identifies at least one transcendental entry among the three powers; this argument does not identify which one.

3. If \(\sum_jq_j\lambda_j=0\), clear denominators to obtain integers \(m_j\), and exponentiate to get \(\prod_j\alpha_j^{m_j}=1\). Multiplicative independence forces all \(m_j=0\), and hence all \(q_j=0\). Thus Theorem 5.8 applies to \(y_j=\lambda_j\) and \(x_1=1,x_2=\beta\) unless \(\beta\in\mathbb Q\). Its six exponentials would all be algebraic by the hypotheses, so this exception must occur. For any other fixed logarithms, the same exponentiation still gives the same \(\alpha_j\), and proves their rational independence again. Powers must use the very logarithms appearing in the hypothesis; one cannot change a branch while keeping an unrelated value of \(\alpha_j^\beta\).

4. For \(|z|=R\), expansion of both squares gives

   \[
   |R^2-\overline wz|^2
   =R^4-2R^2\operatorname{Re}(\overline wz)+R^2|w|^2
   =R^2|z-w|^2.
   \]

   Hence the quotient has modulus \(1\). If a zero \(w\) has multiplicity \(m\), listing it \(m\) times cancels exactly \((z-w)^m\) from the local Taylor factorization; all resulting poles are removable. Maximum modulus bounds the transformed function at \(0\) by \(|f|_R\), and its value there has modulus \(|f(0)|\prod_j R/|z_j|\). Rearranging proves (5.8). No listed \(z_j\) is zero because \(f(0)\ne0\). Zeros on \(|z|=R\) need not be removed: they lie outside the open-disc list and correspond to the factor \(\log(R/R)=0\) in the integrated inequality. Thus both the inequality and the integral formula remain valid with outer boundary zeros.

5. Two evaluation directions impose \(n^2\) conditions on \(r^2\) coefficients. With \(r\sim cn\), the Siegel exponent is asymptotically \(1/(c^2-1)\). The logarithm of the coefficient size is \(O(rn)=O(n^2)\). At a first new point after a box of side \(s\), norm estimates give \(\log|F(w)|\geq-O(n^2+rs)\geq-O(s^2)\). Zero removal gives an analytic upper estimate of the form

   \[
   \log|F(w)|\leq O(n^2)+rXR+s^2\log(C_0s/R),
   \]

   with fixed constants. The construction only ensures \(s\geq n\), so it must in particular work in the possible case \(s=n\). There, \(R=n^q\) with \(q>1\) would give a negative gain \(-(q-1)n^2\log n+O(n^2)\), but the positive growth allowance \(rXR\) has size \(n^{1+q}\). Since \(n^{q-1}/\log n\to\infty\), this allowance dominates the gain. This says the available upper estimate fails to force smallness; it does not claim the actual function attains that upper bound.

   With \(R=tn\), the zero term is \(n^2\log(C_0/t)\) and the growth term is asymptotically \(cXt\,n^2\). After division by \(n^2\), all terms are fixed constants. Increasing \(n\) supplies no new advantage, while taking \(t\to\infty\) increases the linear positive cost faster than the logarithmic negative gain. No sign contradiction uniform in the original data follows from these estimates. A very large last box could improve particular estimates, but the construction does not guarantee one.

   With \(a\) frequency directions and \(b\) evaluation directions, balancing \(r^a\) against \(n^b\) requires \(r\) of order \(n^{b/a}\). At \(s=n\), a radius \(n^q\) must have \(q>1\) to gain a negative multiple of \(n^b\log n\). To keep the growth allowance \(rR\) from exceeding this scale, one needs

   \[
   \frac ba+q\leq b.
   \]

   Thus the required interval is \(1<q\leq b-b/a\), which is nonempty exactly when \(ab>a+b\). For \((a,b)=(2,3)\), it allows \(1<q\leq3/2\), the choice in Theorem 5.8. For \((2,2)\), it demands \(1<q\leq1\), an empty interval. This identifies the dimension obstruction in this proof without resolving the four exponentials conjecture.

## References

- J.-H. Evertse, *Diophantine Approximation*, Leiden course notes: [Chapter 3](https://pub.math.leidenuniv.nl/~evertsejh/dio19-3.pdf), Theorems 3.18 and 3.20, for Siegel's lemma over \(\mathbb Z\) and over the ring of integers of a number field, with coefficients measured by the house; [Chapter 4](https://pub.math.leidenuniv.nl/~evertsejh/dio19-4.pdf), Lemmas 4.25–4.26, for the maximum modulus principle and the estimate from many zeros.
- Michel Waldschmidt, [*Transcendence Methods*](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/QueensPaper52.pdf), Queen's Papers in Pure and Applied Mathematics 52, Queen's University, Kingston, 1979: §1.2, Lemma 1.2.1, for Siegel's lemma with the bound from the sums of positive and negative coefficients; §1.3, Lemma 1.3.1, for Schwarz's lemma with multiplicities; §3.2, Theorem 3.2.1, for the six exponentials theorem by Schneider's method, in either formulation.
- K. Soundararajan, [*Transcendental Number Theory*](https://math.stanford.edu/~ksound/TransNotes.pdf), Math 249A course notes, Stanford University, Fall 2010, written up by I. Petrow, §12, Theorem 21 and Lemma 4: the auxiliary-function proof of the six exponentials theorem and the number-field Siegel lemma.
- Jiří Lebl, [*Guide to Cultivating Complex Analysis*](https://www.jirka.org/ca/ca.pdf), version 1.9, July 11, 2026: Theorems 3.3.1 and 3.3.3, the exact open Taylor-expansion and differentiability prerequisites. Copyright © 2019–2026 Jiří Lebl; dual CC BY-NC-SA 4.0 / CC BY-SA 4.0, with CC BY-SA used for these linked proofs. The original text of this lesson remains CC0.
- Michel Waldschmidt, [*The Four Exponentials Problem and the Schanuel Conjecture*](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/FourExponentialsSchanuel.pdf), author manuscript dated May 26, 2022, §4: historical attribution and the conjectural four-exponentials formulation. Its availability online is not treated as permission to reproduce its text.
- K. Ramachandra, “Contributions to the theory of transcendental numbers” [I](https://matwbn.icm.edu.pl/ksiazki/aa/aa14/aa1416.pdf) and [II](https://matwbn.icm.edu.pl/ksiazki/aa/aa14/aa1417.pdf), *Acta Arithmetica* 14 (1968), 65–72 and 73–88. Lang published the six exponentials theorem in 1966; Ramachandra notes in his first paper that the result was known earlier to Schneider and Siegel without publication. Waldschmidt's survey above, §4, recounts this history.

- J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), version 3.08, July 19, 2020: Proposition 2.26 proves nondegeneracy of the embedding matrix, and Proposition 2.29 supplies a full integral basis for a number field. These give parallel proofs of the arithmetic prerequisites specified above.
