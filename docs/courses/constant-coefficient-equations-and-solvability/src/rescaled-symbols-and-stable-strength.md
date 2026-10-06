# Rescaled symbols and stable strength

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A derivative of a symbol is weaker than the symbol, but it need not become negligible as the frequency tends to infinity. For \(P(\xi_1,\xi_2)=\xi_1\xi_2\), the derivative \(\partial_2P=\xi_1\) remains comparable to the full derivative norm of \(P\) along \((t,0)\). To understand lower-order corrections, we enlarge the frequency window instead. This gives a stronger comparison that makes every symbol derivative negligible and explains why differentiation of coefficients preserves constant strength.

Read [Operator strength and local inverses](operator-strength-and-local-inverses.md) first; its Lemma 1.1 supplies the weak comparison and the finite-dimensional space of weaker symbols. The derivative-vector shift estimate is [Measuring regularity with weighted Fourier spaces](weighted-fourier-spaces.md), Proposition 1.3. [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html#section-2), Section 2, proves finite-dimensional norm equivalence. We also use the fact that the product of two nonzero polynomials is nonzero. The rescaling, product, domination and principal-symbol arguments used here are proved below. Malgrange [Malgrange] gives historical background on constant-coefficient equations, and Grubb's exact free lecture chapter [Grubb] gives Fourier and tempered-distribution background.

## Measuring a whole frequency window

For \(t>0\), define the rescaled derivative norm
\[
S_P(\xi,t)=\left(\sum_\alpha t^{2|\alpha|}|\partial^\alpha P(\xi)|^2\right)^{1/2}.
\tag{1}
\]
Thus \(S_P(\xi,1)=S_P(\xi)\). It is the coefficient norm of the polynomial \(z\mapsto P(\xi+tz)\).

**Lemma 1.1.** For polynomials of degree at most \(m\), there are positive constants depending only on \(m,n\) such that
\[
c\,S_P(\xi,t)\leq\sup_{|h|\leq t}|P(\xi+h)|
\leq C\,S_P(\xi,t).
\tag{2}
\]
Furthermore,
\[
S_P(\xi+h,t)\leq(1+C|h|/t)^m S_P(\xi,t).
\tag{3}
\]
For \(a\geq1\),
\[
S_P(\xi,t)\leq S_P(\xi,at)\leq a^mS_P(\xi,t).
\tag{4}
\]

**Proof.** The coefficient norm and the supremum on the real unit ball are norms on the same finite-dimensional polynomial space. Apply their equivalence to \(P(\xi+tz)\) to obtain (2). The derivative-vector shift estimate of the weighted-spaces lesson applies to this polynomial with shift \(h/t\), giving (3). Equation (4) follows term by term from (1). \(\square\)

**Proposition 1.2.** The comparison \(Q\prec P\) is equivalent to a uniform estimate
\[
S_Q(\xi,t)\leq C S_P(\xi,t)
\qquad(\xi\in\mathbb R^n,\ t\geq1).
\tag{5}
\]

**Proof.** Set \(t=1\) for one implication. For the other, \(|Q(\eta)|\leq C S_P(\eta,1)\). Using (2) twice,
\[
\begin{aligned}
S_Q(\xi,t)
&\leq C_1\sup_{|h|\leq t}|Q(\xi+h)|\\
&\leq C_2\sup_{|h|\leq t}S_P(\xi+h,1)\\
&\leq C_3\sup_{|l|\leq t+1}|P(\xi+l)|\\
&\leq C_4S_P(\xi,t+1)
\leq C_4 2^m S_P(\xi,t).
\end{aligned}
\]
The constants are independent of \(\xi,t\). \(\square\)

## Products and cancellation

**Lemma 2.1.** For polynomials \(P,Q\) of bounded degrees,
\[
cS_P(\xi,t)S_Q(\xi,t)
\leq S_{PQ}(\xi,t)
\leq CS_P(\xi,t)S_Q(\xi,t).
\tag{6}
\]
The constants depend only on the two degree bounds and the dimension, and (6) holds for every \(t>0\).

**Proof.** Consider multiplication on the two finite-dimensional polynomial spaces, using the derivative coefficient norms at zero. On the product of their unit spheres, the norm of the product is a continuous positive function: neither factor is zero, and a polynomial ring has no zero divisors. Compactness gives a positive minimum and a finite maximum. Normalize the two factors to their unit spheres and rescale. Apply the resulting inequality to \(P(\xi+tz)\) and \(Q(\xi+tz)\), whose product is \((PQ)(\xi+tz)\). \(\square\)

Consequently strength comparisons multiply:
\[
Q_1\prec P_1,\quad Q_2\prec P_2
\quad\Longrightarrow\quad Q_1Q_2\prec P_1P_2.
\tag{7}
\]
There is also cancellation. If \(Q_1Q_2\prec P_1P_2\) and \(P_2\prec Q_2\), with \(Q_2\ne0\), then \(Q_1\prec P_1\). Divide the product-norm inequality by the positive weight \(S_{Q_2}\), and use \(S_{P_2}\leq CS_{Q_2}\). These conclusions remain valid when one of the uncancelled polynomials is zero.

One can extend the comparison to rational functions: write \(R\prec S\) when \(aR\prec aS\) for one nonzero polynomial \(a\) clearing both denominators. The result is independent of \(a\). To compare two choices, multiply by both denominators and use (7) and cancellation. It follows that rational comparisons multiply and reverse on taking reciprocals of nonzero rational functions. This is an algebraic extension of the comparison, with no assertion about the behavior of pointwise rational functions at their poles.

## Corrections that disappear under rescaling

We say that \(P\) **dominates** \(Q\), and write \(Q\ll P\), if
\[
\lim_{t\to\infty}\sup_\xi\frac{S_Q(\xi,1)}{S_P(\xi,t)}=0.
\tag{8}
\]
In particular \(Q\prec P\). The denominator in (8) is enlarged in its derivative weights. This definition is different from requiring \(S_Q(\xi)/S_P(\xi)\to0\) as \(|\xi|\to\infty\).

**Proposition 3.1.** The relation \(Q\ll P\) is equivalent to
\[
\inf_{t\geq1}\sup_\xi\frac{|Q(\xi)|}{S_P(\xi,t)}=0.
\tag{9}
\]
If \(R\prec P\) and \(\alpha\ne0\), then \(\partial^\alpha R\ll P\). A dominated polynomial has degree strictly less than that of \(P\), unless it is zero.

**Proof.** Equation (8) implies (9). Conversely, denote the supremum in (9) at \(t\) by \(a_t\). Finite-dimensional norm equivalence and (3) give
\[
\begin{aligned}
S_Q(\xi,1)
&\leq C\sup_{|h|\leq1}|Q(\xi+h)|\\
&\leq Ca_t\sup_{|h|\leq1}S_P(\xi+h,t)
\leq Ca_t(1+C'/t)^mS_P(\xi,t).
\end{aligned}
\]
The values \(a_t\) decrease as \(t\) increases. Thus an infimum of zero gives (8).

For \(t\geq1\), a direct comparison of the derivative sums gives
\[
S_{\partial^\alpha R}(\xi,1)
\leq t^{-|\alpha|}S_R(\xi,t).
\]
Proposition 1.2 then proves domination. Finally a dominated polynomial is weaker, so its degree \(d\) is at most \(m=\deg P\). If \(d=m\), choose a real \(a\) with \(Q_m(a)\ne0\). For fixed \(t\), as \(s\to\infty\), the ratio \(|Q(sa)|/S_P(sa,t)\) tends to a positive number if \(P_m(a)\ne0\), and tends to infinity if \(P_m(a)=0\). The positive limit in the first case is independent of \(t\), since only the undifferentiated top-order term contributes at order \(s^m\). Both possibilities contradict (9). \(\square\)

**Proposition 3.2.** There is a further characterization:
\[
Q\ll P\quad\Longleftrightarrow\quad
\sup_\xi\frac{S_Q(\xi,t)}{S_P(\xi,t)}\longrightarrow0.
\tag{10}
\]

**Proof.** For the reverse direction use \(S_Q(\xi,1)\leq S_Q(\xi,t)\). For the forward direction, put \(a_s=\sup_\eta |Q(\eta)|/S_P(\eta,s)\), which tends to zero by (9). For \(t\geq s\geq1\), applying (2) to each window gives
\[
\begin{aligned}
S_Q(\xi,t)
&\leq C_1\sup_{|h|\leq t}|Q(\xi+h)|\\
&\leq C_1a_s\sup_{|h|\leq t}S_P(\xi+h,s)\\
&\leq C_2a_s\sup_{|l|\leq t+s}|P(\xi+l)|\\
&\leq C_3a_s S_P(\xi,t+s)
\leq C_3 2^m a_s S_P(\xi,t).
\end{aligned}
\]
The constants are independent of \(s,t,\xi\). First let \(t\to\infty\) with \(s\) fixed, and then let \(s\to\infty\). This proves (10). \(\square\)

Domination is closed under linear combinations. It also combines with weak comparison under products: if \(Q_1\ll P_1\) and \(Q_2\prec P_2\), then \(Q_1Q_2\ll P_1P_2\). Use (6) at scale \(t\), (10) for the first factor, and Proposition 1.2 for the second. Cancellation works in either factor: if \(Q_1Q_2\ll P_1P_2\) and \(P_2\prec Q_2\), then \(Q_1\ll P_1\); if \(Q_1Q_2\prec P_1P_2\) and \(P_2\ll Q_2\), then \(Q_1\ll P_1\). To verify both statements, divide the product comparison at scale \(t\) by \(S_{Q_2}(\xi,t)\). The remaining factor \(S_{P_2}(\xi,t)/S_{Q_2}(\xi,t)\) is uniformly bounded in the first case and tends uniformly to zero in the second. Apply (10).

**Lemma 3.3.** If \(R\ll P\), then \(P+R\) has equal strength to \(P\).

**Proof.** At scale one, the triangle inequality and \(R\prec P\) give \(S_{P+R}\leq CS_P\). By (10), choose a fixed \(t\geq1\) with \(S_R(\xi,t)\leq\tfrac12S_P(\xi,t)\) for all \(\xi\). The triangle inequality in the derivative vector now gives
\[
S_P(\xi,1)\leq S_P(\xi,t)
\leq2S_{P+R}(\xi,t)
\leq2t^mS_{P+R}(\xi,1).
\]
Here \(\deg R<m\) by Proposition 3.1, so \(m\) is also a degree bound for \(P+R\). This proves the reverse strength comparison. \(\square\)

## Ellipticity and a weaker principal condition

**Theorem 4.1.** A polynomial \(P\) of degree \(m\) is stronger than every polynomial of degree at most \(m\) if and only if its highest homogeneous part \(P_m\) is nonzero on every nonzero real vector.

**Proof.** If \(P_m\) has no real zero on the unit sphere, compactness and homogeneity give \(|P_m(\xi)|\geq c|\xi|^m\). The lower-degree terms are bounded by \(C(1+|\xi|)^{m-1}\), so for large \(|\xi|\), \(|P(\xi)|\geq c'|\xi|^m\). The positive lower bound for \(S_P\) handles bounded frequencies. Hence \(S_P\geq c''(1+|\xi|)^m\), and every polynomial of degree at most \(m\) is weaker by Lemma 1.1 of the previous lesson.

Conversely, if \(P_m(a)=0\) for a nonzero real \(a\), then \(S_P(sa)=O(s^{m-1})\). Choose a degree-\(m\) homogeneous polynomial \(Q\) with \(Q(a)\ne0\). It grows like \(s^m\) on that ray and cannot be weaker. \(\square\)

The condition in this theorem is ellipticity. For \(m\geq1\), there is a related criterion for dominating every polynomial of degree below \(m\).

**Theorem 4.2.** A degree-\(m\) polynomial dominates every polynomial of degree at most \(m-1\) if and only if
\[
\nabla P_m(a)\ne0\qquad(a\in\mathbb R^n\setminus\{0\}).
\tag{11}
\]

**Proof.** Suppose (11). The sum of squares of the first derivatives of \(P_m\) has a positive minimum on the unit sphere. For large \(|\xi|\), the lower-order contributions to \(\nabla P\) can be absorbed, yielding
\[
\left(\sum_{|\alpha|\geq1}|\partial^\alpha P(\xi)|^2\right)^{1/2}
\geq c(1+|\xi|)^{m-1}.
\tag{12}
\]
On bounded frequencies the left side has a positive lower bound, since some positive-order derivative of \(P\) is a nonzero constant. Therefore (12) holds globally after reducing \(c\). For \(t\geq1\), \(S_P(\xi,t)\) is at least \(t\) times the left side of (12). For every \(Q\) of degree at most \(m-1\), \(S_Q(\xi,1)\leq C_Q(1+|\xi|)^{m-1}\). Its ratio in (8) is bounded by \(C_Q/(ct)\), proving domination.

Conversely, suppose \(\nabla P_m(a)=0\) for a nonzero real \(a\). Euler's identity gives \(P_m(a)=0\). For fixed \(t\), the terms of order \(s^{m-1}\) in \(S_P(sa,t)\) can only come from the undifferentiated polynomial \(P_{m-1}(sa)\); the first derivatives of \(P_m\) vanish on this ray, and all remaining derivatives grow at most as \(s^{m-2}\). Choose \(Q\) homogeneous of degree \(m-1\) with \(Q(a)=1\). Then
\[
\frac{S_P(sa,t)^2}{|Q(sa)|^2}
\longrightarrow |P_{m-1}(a)|^2
\qquad(s\to\infty).
\]
If this limit is positive, the reciprocal ratio has a positive limit independent of \(t\); if it is zero, the reciprocal ratio is unbounded for each \(t\). Either way (9) fails. Thus \(P\) does not dominate this \(Q\). \(\square\)

Condition (11) is called principal type here. It permits real characteristic directions, provided the principal symbol has a nonvanishing gradient there. The lesson does not require the principal symbol to be real-valued.

**Corollary 4.3.** If \(P\) is of principal type and has degree \(m\), then \(Q\prec P\) if and only if \(\deg Q\leq m\) and
\[
|Q_m(\xi)|\leq C|P_m(\xi)|\qquad(\xi\in\mathbb R^n).
\tag{13}
\]
Here \(Q_m=0\) when \(\deg Q<m\).

**Proof.** Every lower-degree polynomial is dominated by \(P\), so \(P_m\) has equal strength to \(P\) by Lemma 3.3. Equation (13) makes \(Q_m\) weaker than \(P_m\). Adding the lower-degree part of \(Q\), which is weaker than \(P\), proves sufficiency. Conversely, \(Q\prec P\) implies the degree bound. Evaluate \(|Q(sa)|\leq CS_P(sa,1)\), divide by \(s^m\), and let \(s\to\infty\). The derivative terms disappear in that limit, yielding \(|Q_m(a)|\leq C|P_m(a)|\) for every real \(a\). \(\square\)

## Exercises with solutions

**Exercise 1 (entry).** For \(P=\xi_1\xi_2\), show directly that \(\partial_2P\ll P\), although \(S_{\partial_2P}/S_P\) does not tend to zero at infinity.

**Solution.** We have
\[
S_P(\xi,t)^2=\xi_1^2\xi_2^2+t^2(\xi_1^2+\xi_2^2)+t^4,
\qquad S_{\partial_2P}(\xi,1)^2=\xi_1^2+1.
\]
For \(t\geq1\), their ratio is at most \(1/t\), since the denominator is at least \(t^2(\xi_1^2+1)\). At \((s,0)\) with scale one, the two weights are equal. This verifies both claims and the distinction between the two limits.

**Exercise 2 (intermediate).** If \(P\) is elliptic of order \(m\), classify the polynomials of equal strength to \(P\).

**Solution.** A polynomial \(Q\) of equal strength has degree at most \(m\). Since \(P\prec Q\), its degree is at least \(m\), so it is exactly \(m\). If \(Q_m\) vanished on a nonzero real ray, \(S_Q\) would grow only like \(s^{m-1}\) there, whereas \(S_P\) grows like \(s^m\), contradicting \(P\prec Q\). Thus \(Q\) is elliptic of order \(m\). Conversely, two elliptic polynomials of the same order have weights comparable to \((1+|\xi|)^m\), so they have equal strength.

**Exercise 3 (intermediate).** Decide whether \(P=\xi_1^2-\xi_2^2\) and \(R=\xi_1^2\) satisfy the principal-type condition. Explain the different behavior of first-order perturbations.

**Solution.** The gradient of \(P\) is \((2\xi_1,-2\xi_2)\), nonzero away from the origin. Hence \(P\) dominates every first-order polynomial, and adding any such polynomial preserves its strength by Lemma 3.3. For \(R\), \(\nabla R\) vanishes at \((0,1)\), and \(\xi_2\) is not weaker than \(R\): its derivative norm is constant along that ray. Adding \(\xi_2\) therefore changes its strength.

**Exercise 4 (advanced).** Prove that \(P\) and \(P(\cdot+h)\) have equal strength for every fixed real \(h\), and that their difference is dominated by \(P\).

**Solution.** The derivative-vector shift estimate in both directions gives the strength equivalence. Taylor's finite polynomial formula expresses \(P(\xi+h)-P(\xi)\) as a finite linear combination of \(\partial^\alpha P(\xi)\) with \(|\alpha|\geq1\). Each such derivative is dominated by \(P\), and domination is closed under linear combinations. This also supplies a second proof of the strength equivalence through Lemma 3.3.

## References

- [Malgrange] Bernard Malgrange, *Existence et approximation des solutions des équations aux dérivées partielles et des équations de convolution*, Annales de l'Institut Fourier **6** (1956), 271–355. [Original article](https://aif.centre-mersenne.org/articles/10.5802/aif.65/).
- [Grubb] Gerd Grubb, author-hosted lecture chapter §5, *Fourier transformation of distributions*, §§5.1–5.3, from the 2007–2008 lecture notes for *Distributions and Operators*. [Exact freely readable chapter](https://www.math.ku.dk/~grubb/dist5.pdf). [Author's lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm). Fourier and tempered-distribution background; the strength and inverse proofs are supplied by the linked lessons and the present lesson.
- Internal strength proof locators: Lemma 1.1 and Proposition 1.2 (rescaled windows), Lemma 2.1 (products and cancellation), Propositions 3.1–3.2 and Lemma 3.3 (domination and stable strength), and Theorems 4.1–4.2 and Corollary 4.3 (principal-symbol criteria), all proved in this lesson.
