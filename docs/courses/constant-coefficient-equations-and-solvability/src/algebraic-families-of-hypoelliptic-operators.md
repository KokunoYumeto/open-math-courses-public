# Algebraic families of hypoelliptic operators

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The complex-zero criterion can be checked without locating the zeros individually. Derivative estimates prove hypoellipticity for elliptic and semielliptic polynomials, and also for a family whose ordinary principal part can have many real characteristic directions. We develop these tests and show why a simple characteristic zero in the principal part is an obstruction.

Read [Hypoellipticity and complex zeros](hypoellipticity-and-complex-zeros.md) for the equivalence between hypoellipticity and decay of every positive-order derivative ratio. [Weighted interior estimates and operator strength](weighted-interior-estimates-and-strength.md) then turns these tests into regularity gains. Grubb [Grubb] gives the Fourier and elliptic background, while Hörmander's seminar article [Hormander] provides context for the geometry of limiting symbols and singularities.

We use \(D=-i\partial\). Except where real coefficients are explicitly required, polynomial coefficients may be complex. If \(P\) has ordinary degree \(m\), write \(P_m\) for its homogeneous part of degree \(m\).

## Ellipticity and a simple-zero obstruction

**Theorem 1.1.** Every elliptic constant-coefficient operator is hypoelliptic. Conversely, if \(P(D)\) is hypoelliptic, its principal part cannot have a simple real zero away from the origin: there is no \(a\in\mathbb R^n\setminus\{0\}\) with
\[
P_m(a)=0,\qquad \nabla P_m(a)\ne0.
\tag{1}
\]
The gradient in (1) may be complex; nonzero means that at least one of its components is nonzero.

**Proof.** For a positive-degree elliptic polynomial, the compact unit sphere has
\[
\min_{|\omega|=1}|P_m(\omega)|>0.
\]
Homogeneity and the lower-order bound give \(|P(\xi)|\geq c|\xi|^m\) for sufficiently large \(|\xi|\). Every derivative satisfies
\[
|\partial^\alpha P(\xi)|\leq C_\alpha|\xi|^{m-|\alpha|}
\quad(1\leq|\alpha|\leq m,\ |\xi|\geq1).
\]
Consequently
\[
\left|\frac{\partial^\alpha P(\xi)}{P(\xi)}\right|
\leq C_\alpha|\xi|^{-|\alpha|}.
\tag{2}
\]
Derivatives of greater order vanish. The quantitative criterion proves hypoellipticity. A nonzero constant polynomial has the same conclusion directly.

For the converse suppose (1) holds, and choose \(j\) with \(\partial_jP_m(a)\ne0\). Along the real ray \(ta\), \(t\to+\infty\),
\[
\begin{aligned}
P(ta)&=O(t^{m-1}),\\
\partial_jP(ta)
&=t^{m-1}\partial_jP_m(a)+O(t^{m-2}).
\end{aligned}
\tag{3}
\]
For \(m=1\) the second remainder is zero. If \(P\) vanishes at arbitrarily large points on the ray, it fails the eventual real nonvanishing criterion. Otherwise its derivative quotient is defined there for all sufficiently large \(t\), and (3) gives a positive lower bound for \(|\partial_jP(ta)/P(ta)|\). It cannot tend to zero. In either case \(P(D)\) is not hypoelliptic. \(\square\)

The converse only excludes simple characteristic zeros. Multiple zeros can occur for hypoelliptic operators, as the examples below demonstrate.

## Anisotropic degrees

Choose positive integers \(m_1,\ldots,m_n\), and put
\[
|\alpha:\mathbf m|=\sum_{j=1}^n\frac{\alpha_j}{m_j}.
\tag{4}
\]
Suppose
\[
\begin{gathered}
P(\xi)=\sum_{|\alpha:\mathbf m|\leq1}a_\alpha\xi^\alpha,\\
P^\circ(\xi)=\sum_{|\alpha:\mathbf m|=1}a_\alpha\xi^\alpha.
\end{gathered}
\tag{5}
\]
The polynomial \(P^\circ\) is the principal part for this anisotropic degree, which need not equal the ordinary principal part. We call \(P\) **semielliptic with weights \(\mathbf m\)** if
\[
P^\circ(\xi)\ne0
\quad\text{for every real }\xi\ne0.
\tag{6}
\]
The definition depends on the existence of such a choice of weights. We make no real-coefficient assumption.

**Theorem 2.1.** Every semielliptic polynomial is hypoelliptic. More precisely, for every nonzero derivative,
\[
\begin{gathered}
\left|\frac{\partial^\alpha P(\xi)}{P(\xi)}\right|
\leq C_\alpha R_{\mathbf m}(\xi)^{-|\alpha:\mathbf m|},\\
R_{\mathbf m}(\xi)\text{ sufficiently large}.
\end{gathered}
\tag{7}
\]
where
\[
R_{\mathbf m}(\xi)=\sum_{j=1}^n|\xi_j|^{m_j}.
\tag{8}
\]

**Proof.** Under the dilation
\[
\delta_s\xi=(s^{1/m_1}\xi_1,\ldots,s^{1/m_n}\xi_n),
\quad s>0,
\]
both \(R_{\mathbf m}\) and \(P^\circ\) have degree one. The set \(R_{\mathbf m}=1\) is compact, avoids zero, and has a positive minimum of \(|P^\circ|\). Rescaling gives
\[
|P^\circ(\xi)|\geq cR_{\mathbf m}(\xi).
\tag{9}
\]
Also, for every multi-index,
\[
|\xi^\beta|\leq R_{\mathbf m}(\xi)^{|\beta:\mathbf m|}.
\tag{10}
\]
Each lower anisotropic degree is strictly smaller than one, and only finitely many terms occur. Equations (9) and (10) imply
\[
\begin{gathered}
|P(\xi)|\geq c'R_{\mathbf m}(\xi),\\
R_{\mathbf m}(\xi)\text{ sufficiently large}.
\end{gathered}
\tag{11}
\]

A surviving monomial in \(\partial^\alpha P\) comes from an index \(\beta\geq\alpha\) with \(|\beta:\mathbf m|\leq1\). Its anisotropic degree is \(|\beta:\mathbf m|-|\alpha:\mathbf m|\leq1-|\alpha:\mathbf m|\). If \(|\alpha:\mathbf m|>1\), there are no such monomials and the derivative is zero. Otherwise (10), now applied to \(\beta-\alpha\), gives
\[
\begin{gathered}
|\partial^\alpha P(\xi)|
\leq C_\alpha R_{\mathbf m}(\xi)^{1-|\alpha:\mathbf m|},\\
R_{\mathbf m}(\xi)\geq1.
\end{gathered}
\tag{12}
\]
Divide by (11) to obtain (7). For \(\alpha\ne0\) its exponent is positive, and \(R_{\mathbf m}(\xi)\to\infty\) as \(|\xi|\to\infty\). The derivative criterion proves hypoellipticity. \(\square\)

Taking all \(m_j=m\) recovers ordinary ellipticity of order \(m\). For the heat polynomial \(i\tau+|\xi|^2\), the weights are one in time frequency and two in each spatial frequency. Its anisotropic principal part is the whole polynomial and has no nonzero real zero.

The estimate also supplies a common isotropic exponent. If \(M=\max_jm_j\) and \(b=\min_jm_j\), then for large \(|\xi|\),
\[
R_{\mathbf m}(\xi)\geq c|\xi|^b,
\qquad |\alpha:\mathbf m|\geq|\alpha|/M.
\]
Thus (7) implies derivative-ratio bounds with exponent \(b/M>0\). This is a valid uniform exponent; individual polynomials can admit better ones.

## An elliptic correction to a high even power

Anisotropic ellipticity is not the only way to overcome characteristic directions. The following construction starts with an arbitrary real polynomial.

**Theorem 3.1.** Let \(Q\) be a real polynomial of degree \(m\geq1\), let \(k\geq2\) be an integer, and define
\[
\begin{aligned}
\mu&=2km-2(k-1)\\
&=2k(m-1)+2.
\end{aligned}
\tag{13}
\]
Let \(R\) be a real homogeneous polynomial of degree \(\mu\) satisfying \(R(\xi)>0\) for every real \(\xi\ne0\). Then
\[
P(\xi)=Q(\xi)^{2k}+R(\xi)
\tag{14}
\]
is hypoelliptic. For every positive-order derivative,
\[
\begin{gathered}
\left|\frac{\partial^\alpha P(\xi)}{P(\xi)}\right|
\leq C_\alpha|\xi|^{-|\alpha|/k},\\
|\xi|\text{ sufficiently large}.
\end{gathered}
\tag{15}
\]
Its ordinary principal part is \(Q_m^{2k}\).

**Proof.** Positivity on the real unit sphere and homogeneity give
\[
c|\xi|^\mu\leq R(\xi)\leq C|\xi|^\mu
\quad(\xi\ne0).
\tag{16}
\]
Since \(Q\) is real, \(Q^{2k}\geq0\) on real space, and
\[
P\geq Q^{2k},\qquad P\geq R.
\tag{17}
\]
In particular, \(P\) has no nonzero real zero. For \(1\leq j\leq2k\), taking the corresponding weighted geometric mean of these two inequalities yields
\[
|Q|^{2k-j}R^{j/(2k)}\leq P.
\tag{18}
\]

Differentiate the product of \(2k\) copies of \(Q\). Group the terms according to the number \(j\) of copies receiving at least one derivative. For \(\alpha\ne0\) this gives
\[
\partial^\alpha(Q^{2k})
=\sum_{j=1}^{\min(2k,|\alpha|)}
Q^{2k-j}F_{j,\alpha},
\tag{19}
\]
where each \(F_{j,\alpha}\) is a polynomial with
\[
\deg F_{j,\alpha}\leq jm-|\alpha|.
\tag{20}
\]
Indeed its \(j\) differentiated factors have degrees at most \(m-|\beta_\nu|\), with nonzero \(\beta_\nu\) summing to \(\alpha\). If the bound in (20) is negative, that polynomial is zero. All combinatorial constants are included in \(F_{j,\alpha}\).

For \(|\xi|\geq1\), (16), (18), and (20) imply
\[
\begin{aligned}
\frac{|Q|^{2k-j}|F_{j,\alpha}|}{P}
&\leq |F_{j,\alpha}|R^{-j/(2k)}\\
&\leq C_\alpha
|\xi|^{jm-|\alpha|-\mu j/(2k)}.
\end{aligned}
\tag{21}
\]
Since \(m-\mu/(2k)=1-1/k\) and \(j\leq|\alpha|\), the exponent on the right is at most \(-|\alpha|/k\). Summing the finitely many terms proves the desired estimate for \(\partial^\alpha(Q^{2k})/P\).

For the other summand, homogeneity and (16) give
\[
\frac{|\partial^\alpha R|}{P}
\leq\frac{|\partial^\alpha R|}{R}
\leq C_\alpha|\xi|^{-|\alpha|}
\tag{22}
\]
when the derivative is nonzero; if its order exceeds \(\mu\), it vanishes. Combine (21) and (22) to prove (15), and apply the quantitative criterion.

Finally \(\mu<2km\), since \(k\geq2\). Therefore the homogeneous part of the highest ordinary degree is \(Q_m^{2k}\). \(\square\)

The degree of the correction and the reality of \(Q\) both matter in this proof. Reality supplies the inequalities in (17). The correction degree makes each differentiated factor decay after division by \(P\).

## A concrete multiple-characteristic example

Take \(Q(\xi_1,\xi_2)=\xi_1\xi_2\), \(m=2\), \(k=2\), and
\[
\begin{aligned}
R(\xi)&=(\xi_1^2+\xi_2^2)^3,\\
P(\xi)&=\xi_1^4\xi_2^4+
(\xi_1^2+\xi_2^2)^3.
\end{aligned}
\tag{23}
\]
Here \(\mu=6\), and \(R\) is positive off zero. Theorem 3.1 proves hypoellipticity with derivative-ratio exponent \(1/2\). The ordinary principal part \(\xi_1^4\xi_2^4\) vanishes on both coordinate axes, so this operator is not elliptic. Those zeros are multiple, as required by Theorem 1.1.

In fact (23) is not semielliptic for any positive integer weights in the given coordinates. If such weights \(m_1,m_2\) existed, the pure sixth powers force \(m_1,m_2\geq6\). For the anisotropic principal part not to vanish on either axis, those pure powers must both have weight one, so \(m_1=m_2=6\). But then the mixed monomial \(\xi_1^4\xi_2^4\) has weight \(4/6+4/6>1\), contrary to (5). Thus the third family supplies a test beyond that particular semielliptic definition.

If the correction is instead
\[
P_0(\xi)=\xi_1^4\xi_2^4+
(\xi_1^2+\xi_2^2)^2,
\tag{24}
\]
the polynomial remains positive off zero, but it is not hypoelliptic. Along \((1,t)\),
\[
\begin{aligned}
P_0(1,t)&=2t^4+2t^2+1,\\
\partial_1P_0(1,t)&=4t^4+4t^2+4,
\end{aligned}
\]
so their quotient tends to two. Positivity alone does not imply the derivative decay needed for hypoellipticity.

## Exercises with complete solutions

**Exercise 1. Simple characteristics survive lower terms.** Let \(P(\xi_1,\xi_2)=\xi_1^2-\xi_2^2+i\xi_1+3\). Decide whether it is hypoelliptic, using its principal part rather than solving for complex zeros.

**Solution.** At \(a=(1,1)\), the principal part vanishes and its gradient is \((2,-2)\ne0\). Theorem 1.1 rules out hypoellipticity for every choice of lower-order terms with that principal part. Here explicitly \(P(t,t)=it+3\) and \(\partial_1P(t,t)=2t+i\), so the quotient does not tend to zero.

**Exercise 2. Anisotropic order.** Show that
\[
P(\xi_1,\xi_2)=\xi_1^6+\xi_2^4+i\xi_1^2\xi_2+7
\]
is semielliptic and hypoelliptic. Give its anisotropic principal part and one common isotropic exponent supplied by Theorem 2.1.

**Solution.** Choose \(m_1=6,m_2=4\). The mixed lower term has weight \(2/6+1/4=7/12<1\), and the constant has weight zero. Thus \(P^\circ=\xi_1^6+\xi_2^4\), positive for real \(\xi\ne0\). The theorem applies, and \(b/M=4/6=2/3\) is a valid common isotropic exponent for the derivative-ratio bounds. For example a first derivative in the first variable has the anisotropic bound \(C R_{\mathbf m}^{-1/6}\), while one in the second has \(C R_{\mathbf m}^{-1/4}\).

**Exercise 3. Why a weighted principal part must avoid zeros.** Replace the plus sign between the leading terms in Exercise 2 by a minus sign and omit the other terms. Explain why the same weights do not prove semiellipticity, and decide hypoellipticity of the resulting polynomial.

**Solution.** Its anisotropic principal part is \(\xi_1^6-\xi_2^4\), with nonzero real zeros such as \((1,1)\), so the semielliptic hypothesis fails. More directly the zeros \((t^2,t^3)\), \(t>0\), escape to infinity while lying in real space. Their distance to the complex zero set is zero. The complex-zero criterion therefore shows that this polynomial is not hypoelliptic.

**Exercise 4. Keeping track of all differentiated factors.** For \(k=2\) and \(\alpha=(1,1)\), compute \(\partial_1\partial_2(Q^4)\). Identify the terms in (19) and verify their degree bounds.

**Solution.** Direct differentiation gives
\[
\partial_1\partial_2(Q^4)
=12Q^2(\partial_1Q)(\partial_2Q)
+4Q^3\partial_1\partial_2Q.
\]
Thus \(F_{2,\alpha}=12(\partial_1Q)(\partial_2Q)\), of degree at most \(2m-2\), and \(F_{1,\alpha}=4\partial_1\partial_2Q\), of degree at most \(m-2\). These are \(jm-|\alpha|\) for \(j=2,1\), respectively. Even when a particular factor or term vanishes, the bounds remain valid. Formula (18) controls each term with the corresponding power \(R^{j/4}\), so omitting the \(j=1\) contribution would miss part of the estimate.

**Exercise 5. The low-degree case.** Let \(Q(\xi)=\xi_1\), \(k=3\), and \(R(\xi)=|\xi|^2\) on \(\mathbb R^n\). Prove hypoellipticity of \(P=\xi_1^6+|\xi|^2\), and find weights showing that this example is also semielliptic.

**Solution.** Here \(m=1\) and (13) gives \(\mu=2\). Theorem 3.1 applies with exponent \(1/3\). For semiellipticity, take \(m_1=6\) and \(m_j=2\) for \(j\geq2\). The anisotropic principal part is \(\xi_1^6+\sum_{j\geq2}\xi_j^2\); the remaining \(\xi_1^2\) has weight \(1/3\). The principal part is positive off zero. For \(n=1\) the sum is empty and the same verification uses \(m_1=6\). The two sufficient tests can apply to the same polynomial.

**Exercise 6. A correction that is positive but insufficient.** For \(P_0\) in (24), check the derivative quotient and explain precisely which conclusion remains valid despite failure of hypoellipticity.

**Solution.** Differentiate:
\[
\partial_1P_0
=4\xi_1^3\xi_2^4+
4\xi_1(\xi_1^2+\xi_2^2).
\]
At \((1,t)\) this is \(4t^4+4t^2+4\), while \(P_0=2t^4+2t^2+1\). The ratio tends to two and fails the derivative criterion. The positive correction still ensures \(P_0(\xi)>0\) for every real \(\xi\ne0\). Thus its only real zero is the origin, and it is eventually nonvanishing on real frequencies. That necessary condition is weaker than retreat of the complex zero set: the latter also needs the derivative ratios to vanish.

## References

- **[Grubb]** Gerd Grubb, *Distributions and Operators*, open lectures, sections on Fourier transformation, elliptic operators, and interior regularity. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- **[Hormander]** Lars Hörmander, “On the singularities of solutions of partial differential equations with constant coefficients,” *Séminaire Goulaouic–Schwartz*, 1971–1972, exposé 25, 1–6. [Original article](https://www.numdam.org/item/SEDP_1971-1972____A25_0/).
