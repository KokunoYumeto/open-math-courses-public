# Uniform interior estimates with distance weights

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

An interior derivative estimate has two scales: the frequency scale at which the equation controls a direction, and the physical distance left before reaching the boundary. We connect them with a Fourier weight built from the complex zeros of the symbol. The resulting estimate works on every open set, with a constant independent of its shape.

Read [Hypoellipticity and complex zeros](hypoellipticity-and-complex-zeros.md) for the quantitative comparison between zero-set distance and symbol derivatives. [Measuring regularity with weighted Fourier spaces](weighted-fourier-spaces.md) provides the convolution estimate used for multiplication by cutoffs. The local Sobolev estimates needed later are discussed in Grubb [Grubb].

Throughout, \(D=-i\partial\), \(P\) is a nonconstant hypoelliptic polynomial of degree \(m\), and
\[
\begin{gathered}
P^{(\alpha)}=\partial_\xi^\alpha P,
\\ d(\xi)=\operatorname{dist}(\xi,\{P=0\}\subset\mathbb C^n).
\end{gathered}
\tag{1}
\]
The distance is measured in the Euclidean norm of \(\mathbb C^n\). Its restriction to real \(\xi\) is \(1\)-Lipschitz. Polynomial coefficients may be complex. A nonzero constant symbol has only the zero homogeneous solution and is treated directly.

## The energy and the directional bound

For an open set \(X\) and \(\varepsilon>0\), define
\[
\begin{gathered}
E_\varepsilon(u;X)^2
\\ =\sum_{0<|\alpha|\leq m}\varepsilon^{-2|\alpha|}
\|P^{(\alpha)}(D)u\|_{L^2(X)}^2.
\end{gathered}
\tag{2}
\]
The undifferentiated symbol is excluded from this sum. Some derivative of order \(m\) is a nonzero constant, so this energy controls the \(L^2\) norm of \(u\).

Fix a real vector \(y\), and suppose that, for \(\rho\geq1\),
\[
|y\cdot\xi|\leq C(1+d(\xi))^\rho
\quad(\xi\in\mathbb R^n).
\tag{3}
\]
If \(y=0\), every directional estimate below is immediate. For a nonzero direction, no exponent smaller than one can satisfy (3): along \(\xi=ty\), the distance to any fixed complex zero is \(O(t)\), while \(|y\cdot\xi|\) grows linearly.

Write
\[
X_\delta=\{x\in X:\operatorname{dist}(x,\mathbb R^n\setminus X)>\delta\}.
\tag{4}
\]
For \(X=\mathbb R^n\), the distance in (4) is \(+\infty\).

**Theorem 1.1.** Under (3), there is a constant \(C\), independent of \(X,u,\delta\), such that every distributional solution of \(P(D)u=0\) in \(X\) satisfies
\[
\begin{gathered}
E_\delta((y\cdot D)u;X_\delta)
\\ \leq C\delta^{-\rho}E_\delta(u;X),\quad 0<\delta<1.
\end{gathered}
\tag{5}
\]
No regularity of \(\partial X\) or boundedness of \(X\) is required. An infinite right side is interpreted in the extended sense.

Hypoellipticity first makes \(u\) smooth. We prove (5) by establishing a weighted gain, localizing on a ball, and then averaging the ball estimates over their centers.

## A Fourier weight with uniform scale control

Put
\[
\begin{gathered}
w_\varepsilon(\xi)=1+\varepsilon d(\xi),
\\ \|v\|_{s,\varepsilon}^2=(2\pi)^{-n}\int
w_\varepsilon(\xi)^{2s}|\widehat v(\xi)|^2\,d\xi.
\end{gathered}
\tag{6}
\]
For every real \(s\), these are weighted \(L^2\) norms. The triangle inequality gives
\[
w_\varepsilon(\xi+\eta)
\leq w_\varepsilon(\xi)(1+\varepsilon|\eta|).
\tag{7}
\]
Interchanging the two frequency points also bounds the reciprocal ratio. Consequently
\[
\frac{w_\varepsilon(\xi)^s}{w_\varepsilon(\eta)^s}
\leq(1+\varepsilon|\xi-\eta|)^{|s|}.
\tag{8}
\]

Define the positive-symbol-derivative energy in this Fourier norm by
\[
\begin{gathered}
A_{s,\varepsilon}(v)^2
\\ =\sum_{0<|\alpha|\leq m}\varepsilon^{-2|\alpha|}
\|P^{(\alpha)}(D)v\|_{s,\varepsilon}^2.
\end{gathered}
\tag{9}
\]

**Lemma 2.1.** For every real \(s\),
\[
\begin{gathered}
A_{s+1,\varepsilon}(v)^2
\\ \leq C\bigl(A_{s,\varepsilon}(v)^2+\|P(D)v\|_{s,\varepsilon}^2\bigr).
\end{gathered}
\tag{10}
\]
The constant is independent of \(s\) and \(\varepsilon\).

**Proof.** It is enough to prove the pointwise polynomial inequality
\[
\begin{gathered}
w_\varepsilon(\xi)^2\sum_{\alpha\ne0}\varepsilon^{-2|\alpha|}|P^{(\alpha)}(\xi)|^2
\\ \leq C\sum_{\alpha}\varepsilon^{-2|\alpha|}|P^{(\alpha)}(\xi)|^2.
\end{gathered}
\tag{11}
\]
All sums stop at degree \(m\). When \(\varepsilon d(\xi)\leq1\), the left weight is at most four, so (11) is immediate.

When \(\varepsilon d(\xi)>1\), the symbol does not vanish. The derivative-distance estimate from the complex-zero criterion gives
\[
|P^{(\alpha)}(\xi)|
\leq C_\alpha d(\xi)^{-|\alpha|}|P(\xi)|.
\tag{12}
\]
For \(k=|\alpha|\geq1\), the corresponding left summand in (11) is bounded by
\[
C_\alpha(\varepsilon d(\xi))^{-2(k-1)}
|P(\xi)|^2
\leq C_\alpha|P(\xi)|^2.
\]
There are finitely many summands. This proves (11). Multiplying by
\((2\pi)^{-n}w_\varepsilon^{2s}|\widehat v|^2\) and integrating proves (10). The case of a real zero was already included in the first region; no division by \(P\) occurs there. \(\square\)

**Lemma 2.2.** Let \(\phi\in C_c^\infty(\mathbb R^n)\), and set
\(\phi_\varepsilon(x)=\phi(x/\varepsilon)\). For every multi-index \(\beta\) and real \(s\),
\[
\|(D^\beta\phi_\varepsilon)h\|_{s,\varepsilon}
\leq C_{\phi,\beta,s}\varepsilon^{-|\beta|}
\|h\|_{s,\varepsilon},
\tag{13}
\]
with a constant independent of \(\varepsilon\).

**Proof.** The Fourier transform of the scaled cutoff is
\(\widehat{\phi_\varepsilon}(\eta)=\varepsilon^n\widehat\phi(\varepsilon\eta)\).
Thus the change of variable \(\theta=\varepsilon\eta\) gives
\[
\begin{aligned}
&\int|\eta^\beta\widehat{\phi_\varepsilon}(\eta)|
(1+\varepsilon|\eta|)^{|s|}\,d\eta\\
&=\varepsilon^{-|\beta|}
\int|\theta^\beta\widehat\phi(\theta)|
(1+|\theta|)^{|s|}\,d\theta.
\end{aligned}
\tag{14}
\]
The last integral is finite because \(\widehat\phi\) is a Schwartz function. The product formula, (8), and Young's \(L^1*L^2\) inequality now imply (13), including the Fourier normalization factor \((2\pi)^{-n}\) in its constant. The argument works for negative as well as positive \(s\). \(\square\)

## Gaining weighted regularity inside a ball

**Lemma 3.1.** Suppose \(P(D)u=0\) in \(B_\varepsilon\). For every
\(\phi\in C_c^\infty(B_1)\) and integer \(s\geq0\),
\[
A_{s,\varepsilon}(\phi_\varepsilon u)
\leq C_{\phi,s}E_\varepsilon(u;B_\varepsilon).
\tag{15}
\]
The constant is independent of \(\varepsilon\) and \(u\).

**Proof.** At \(s=0\), use the exact Leibniz identity
\[
\begin{gathered}
\varepsilon^{-|\alpha|}P^{(\alpha)}(D)(\phi_\varepsilon u)
\\ =\sum_\beta b_{\beta,\varepsilon}
\varepsilon^{-|\alpha+\beta|}P^{(\alpha+\beta)}(D)u,
\end{gathered}
\tag{16}
\]
The sum is finite. If \(\alpha\ne0\), every \(\alpha+\beta\) is still positive. Here \(b_{\beta,\varepsilon}=\varepsilon^{|\beta|}D^\beta\phi_\varepsilon/\beta!\). These scaled cutoff coefficients are uniformly bounded. The finite \(L^2\) triangle inequality proves (15). This base step does not use the homogeneous equation.

Suppose the statement is proved at level \(s-1\) for every unit-ball cutoff. Choose
\(\psi\in C_c^\infty(B_1)\), equal to one near \(\operatorname{supp}\phi\).
Then
\[
\begin{gathered}
P(D)(\phi_\varepsilon u)
\\ =\sum_{\beta\ne0}\frac{D^\beta\phi_\varepsilon}{\beta!}
P^{(\beta)}(D)(\psi_\varepsilon u).
\end{gathered}
\tag{17}
\]
Indeed the zero-order term is
\(\phi_\varepsilon P(D)(\psi_\varepsilon u)
=\phi_\varepsilon P(D)u=0\); all derivatives of \(\psi_\varepsilon\) miss the relevant support.

By Lemma 2.2 and the finite-sum inequality,
\[
\|P(D)(\phi_\varepsilon u)\|_{s-1,\varepsilon}
\leq C A_{s-1,\varepsilon}(\psi_\varepsilon u).
\tag{18}
\]
Apply Lemma 2.1 to \(\phi_\varepsilon u\), and use the induction hypothesis for both \(\phi\) and \(\psi\). This proves (15) at level \(s\). \(\square\)

**Lemma 3.2.** Under (3), every homogeneous solution in \(B_\varepsilon\), \(0<\varepsilon\leq1\), satisfies
\[
\varepsilon^\rho
E_\varepsilon((y\cdot D)u;B_{\varepsilon/2})
\leq C E_\varepsilon(u;B_\varepsilon).
\tag{19}
\]

**Proof.** Let \(s=\lceil\rho\rceil\). Equation (3) gives
\[
\begin{aligned}
\varepsilon^\rho|y\cdot\xi|&\leq C(\varepsilon+\varepsilon d(\xi))^\rho\\
&\leq Cw_\varepsilon(\xi)^s.
\end{aligned}
\tag{20}
\]
By Parseval,
\(\varepsilon^\rho\|(y\cdot D)v\|_2\leq C\|v\|_{s,\varepsilon}\).
Choose \(\phi\in C_c^\infty(B_1)\), equal to one in \(B_{1/2}\), and apply this inequality to
\(v=P^{(\alpha)}(D)(\phi_\varepsilon u)\) for every \(\alpha\ne0\).
The constant-coefficient operators commute. Sum their squares with the weights in (2), and apply Lemma 3.1. In the smaller ball, the cutoff is one, so the localized expressions equal the original ones. This proves (19). \(\square\)

## Averaging over centers

**Proof of Theorem 1.1.** For every \(z\in X_\varepsilon\), apply (19) to \(u(z+\cdot)\), square it, and integrate in \(z\). Tonelli's theorem applies to all the nonnegative integrands.

For a fixed source point \(x\), the measure of right-side centers is at most
\(|B_\varepsilon|\), and is zero outside \(X\). If \(x\in X_{2\varepsilon}\), every center in \(B_{\varepsilon/2}(x)\) belongs to \(X_\varepsilon\), since boundary distance is \(1\)-Lipschitz. The left-side center measure is then exactly
\[
|B_{\varepsilon/2}|=2^{-n}|B_\varepsilon|.
\]
Discard the other nonnegative left-side contributions and cancel the common ball volume. We obtain
\[
\varepsilon^\rho
E_\varepsilon((y\cdot D)u;X_{2\varepsilon})
\leq C E_\varepsilon(u;X).
\tag{21}
\]
Set \(\varepsilon=\delta/2\). For every domain and function,
\[
E_\delta\leq E_{\delta/2}\leq2^mE_\delta.
\tag{22}
\]
Using (22) on the two sides of (21) gives exactly (5). \(\square\)

The averaging argument is why the constant does not depend on the boundary. The proof requires only that the balls centered in \(X_\varepsilon\) lie in \(X\).

## Retaining the derivatives of an inhomogeneous datum

For an integer \(r\geq0\), define
\[
F_{r,\delta}(f;X)^2
=\sum_{|\beta|\leq r}
\delta^{2|\beta|}\|D^\beta f\|_{L^2(X)}^2.
\tag{23}
\]

**Theorem 5.1.** Let \(P(D)u=f\), with \(f\) smooth in \(X\). Under (3), put \(r=\lceil\rho\rceil-1\). Then
\[
\begin{gathered}
E_\delta((y\cdot D)u;X_\delta)
\\ \leq C\delta^{-\rho}
\bigl(E_\delta(u;X)+F_{r,\delta}(f;X)\bigr),
\\ 0<\delta<1.
\end{gathered}
\tag{24}
\]
Again \(C\) is independent of \(X,u,\delta\). Smoothness of \(f\) makes a distributional \(u\) smooth by hypoellipticity.

**Proof.** The base case of Lemma 3.1 is unchanged. For higher weighted levels, (17) gains the term \(\phi_\varepsilon f\). A finite nested chain of cutoffs, with a terminal cutoff \(\chi\) equal to one near every preceding support, gives
\[
\begin{gathered}
A_{s,\varepsilon}(\phi_\varepsilon u)
\\ \leq C\bigl(E_\varepsilon(u;B_\varepsilon)
+\|\chi_\varepsilon f\|_{s-1,\varepsilon}\bigr),
\\ s\geq1.
\end{gathered}
\tag{25}
\]
To verify the induction, Lemma 2.1 at level \(s-1\) uses the positive cutoff energies at that level and the additional source norm at that level. Every source norm from a previous step has a smaller power of \(w_\varepsilon\). Since \(w_\varepsilon\geq1\), it is bounded by the terminal norm in (25). Multiplication by each intermediate cutoff has a scale-independent norm by Lemma 2.2 with \(\beta=0\). There are finitely many levels and cutoffs.

Choose one fixed complex zero \(\zeta_0\). Since \(d(\xi)\leq|\xi-\zeta_0|\), for \(0<\varepsilon\leq1\),
\[
w_\varepsilon(\xi)^{s-1}
\leq C(1+\varepsilon|\xi|)^{s-1}.
\tag{26}
\]
Integer-order polynomial norm comparison and Parseval bound the last norm in (25) by \(C F_{s-1,\varepsilon}(f;B_\varepsilon)\). The product rule justifies the cutoff here: a derivative of \(\chi_\varepsilon\) contributes \(\varepsilon^{-|\gamma|}\), which cancels the corresponding positive scale factor in the Sobolev norm.

Take \(s=\lceil\rho\rceil\), repeat the directional estimate (20), and average centers as before. The squared sum of the two right-side terms is bounded by twice the sum of their squares. Equation (22) converts the energy scale; the source norm at \(\delta/2\) is bounded by the one at \(\delta\). This proves (24). \(\square\)

For a finite iteration, let \(T=y\cdot D\), \(a=C\delta^{-\rho}\), and \(j\geq1\). Then
\[
\begin{gathered}
E_\delta(T^ju;X_{j\delta})
\\ \leq a^jE_\delta(u;X)
\\ {}+\sum_{\ell=0}^{j-1}a^{j-\ell}F_{r,\delta}(T^\ell f;X).
\end{gathered}
\tag{27}
\]
Apply (24) to each \(T^\ell u\), use \(P(D)T^\ell u=T^\ell f\), and restrict successive domains. The erosion losses add because
\[
X_{(\ell+1)\delta}\subset (X_{\ell\delta})_\delta.
\tag{28}
\]
For \(x\in X_{\ell\delta}\), its distance to the complement of that set is at least \(d_X(x)-\ell\delta\), which proves (28).

Formula (27) keeps the datum's derivative growth explicit. An arbitrary smooth \(f\) need not have analytic or Gevrey derivative bounds.

## Exercises with complete solutions

**Exercise 1. Introductory: negative weight powers.** Prove (8) when \(s<0\), and explain why a one-sided use of (7) is insufficient.

**Solution.** Interchange the frequency points in (7) to get
\(w_\varepsilon(\eta)\leq w_\varepsilon(\xi)(1+\varepsilon|\xi-\eta|)\).
For \(s=-a\), \(a>0\), the required ratio is
\((w_\varepsilon(\eta)/w_\varepsilon(\xi))^a\), which this reversed inequality bounds by the right side of (8). The original order controls the reciprocal ratio and therefore does not alone prove the negative-power assertion.

**Exercise 2. Introductory: changing the energy scale.** Prove (22), including the factor \(2^m\) rather than \(2^{2m}\).

**Solution.** Each squared summand at scale \(\delta/2\) is \(2^{2|\alpha|}\) times its counterpart at scale \(\delta\). These factors lie between one and \(2^{2m}\). Sum the inequalities and then take square roots. This yields (22).

**Exercise 3. Intermediate: the zero-order commutator.** Derive (17) from the full Leibniz formula and identify precisely where homogeneity of the equation is used.

**Solution.** Write \(\phi_\varepsilon u=\phi_\varepsilon(\psi_\varepsilon u)\). The polynomial product formula is the sum over all \(\beta\) of
\((D^\beta\phi_\varepsilon)P^{(\beta)}(D)(\psi_\varepsilon u)/\beta!\).
Its \(\beta=0\) term equals \(\phi_\varepsilon P(D)u\): near the support of \(\phi_\varepsilon\), \(\psi_\varepsilon=1\) and its derivatives vanish. Only the assertion \(P(D)u=0\) removes this term. For an inhomogeneous equation it is \(\phi_\varepsilon f\).

**Exercise 4. Intermediate: center counting on an irregular domain.** Let \(X\) be any open set. Prove that for \(x\in X_{2\varepsilon}\), the centers in \(X_\varepsilon\) satisfying \(|z-x|<\varepsilon/2\) have measure exactly \(|B_{\varepsilon/2}|\).

**Solution.** Boundary distance obeys \(d_X(z)\geq d_X(x)-|z-x|>3\varepsilon/2>\varepsilon\). Hence every point in the entire ball \(B_{\varepsilon/2}(x)\) is an admissible center. The condition \(|z-x|<\varepsilon/2\) allows no centers outside that ball. Its measure is the claimed one, irrespective of the boundary's shape.

**Exercise 5. Advanced: an equation with arbitrarily large datum growth.** Show that no conclusion of analyticity follows from smoothness of \(f\) alone, even for the elliptic operator \(P(D)=D\) in one dimension.

**Solution.** Set \(u(x)=0\) for \(x\leq0\) and \(u(x)=e^{-1/x^2}\) for \(x>0\). Differentiating on the right gives a polynomial in \(1/x\) times the same exponential; every such expression tends to zero at the origin. Thus \(u\) is smooth, and all its Taylor coefficients there vanish. It is positive immediately to the right, so it is not analytic. Its datum \(f=Du\) is smooth. Formula (27) remains valid and includes the derivatives of this \(f\); it makes no factorial bound on them.

**Exercise 6. Advanced: iterating on arbitrary open sets.** Prove (28), and use it to derive (27) by induction on \(j\).

**Solution.** If \(d_X(x)>(\ell+1)\delta\), every \(z\) with \(|z-x|<\delta\) satisfies \(d_X(z)>\ell\delta\), so \(B_\delta(x)\subset X_{\ell\delta}\). The strict inequality also leaves a positive extra margin, giving \(x\in(X_{\ell\delta})_\delta\).

For the induction, apply (24) on \(X_{(j-1)\delta}\) to \(T^{j-1}u\), restrict the left side to \(X_{j\delta}\), and enlarge the datum norm to \(X\). This gives
\[
\begin{gathered}
E_\delta(T^ju;X_{j\delta})
\\ \leq a E_\delta(T^{j-1}u;X_{(j-1)\delta})
+a F_{r,\delta}(T^{j-1}f;X).
\end{gathered}
\]
Substitute the preceding inductive formula. Multiplying its terms by \(a\), and appending the last term, gives exactly the sum in (27). The case \(j=1\) is (24).

## References

- **[Grubb]** Gerd Grubb, *Distributions and Operators*, open lectures on Fourier transformation, Sobolev spaces, and interior regularity. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
