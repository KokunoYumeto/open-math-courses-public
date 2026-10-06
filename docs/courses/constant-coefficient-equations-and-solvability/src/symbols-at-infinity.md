# Symbols at infinity

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A polynomial seen through a fixed frequency window can approach a simpler polynomial as the center of the window escapes to infinity. The limiting polynomial retains information that its highest homogeneous part alone can miss. For example, a product symbol viewed near one coordinate axis becomes a first-order symbol in the other coordinate. We will prove that these limits can be reached along polynomial paths, identify a direction that every limit loses, and obtain a uniform power estimate for approaching the family of limits.

Read [Fundamental solutions and the directions an equation uses](fundamental-solutions-and-active-directions.md) and [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md) first. We use finite-dimensional polynomial norms, elementary complex analysis, and polynomial division. Coste's notes [Coste] explain the real algebraic geometry behind the argument. Grubb's freely readable lecture chapter §5 [Grubb] supplies Fourier and tempered-distribution background for the later analytic applications; the polynomial and real-algebraic arguments here are given below. The proofs below include the specific real algebraic tools we need.

Let \(P\ne0\) be a complex polynomial on \(\mathbb R^n\), of degree \(m\), and write
\[
\begin{gathered}
|q|_J^2=\sum_{|\alpha|\leq m}|\partial^\alpha q(0)|^2,\\
S_P(\eta)=|P(\eta+\cdot)|_J,\\
T_P(\eta)=\frac{P(\eta+\cdot)}{S_P(\eta)}.
\end{gathered}
\tag{1}
\]
The coefficient space is viewed as a real vector space when discussing algebraic inequalities: its coordinates are real and imaginary parts. A highest-order derivative of \(P\) is a nonzero constant, so \(S_P\) never vanishes.

## The family of limiting windows

A **normalized localization** of \(P\) is a coefficient limit of \(T_P(\eta_j)\) along a sequence \(|\eta_j|\to\infty\). Denote the set of these limits by \(\mathcal L(P)\). For \(\theta\ne0\), let \(\mathcal L_\theta(P)\) consist of the limits for which
\[
\frac{\eta_j}{|\eta_j|}\longrightarrow\frac{\theta}{|\theta|}.
\tag{2}
\]
We also call any nonzero scalar multiple of a normalized localization a localization; statements involving a numerical normalization will always use the normalized set.

Every \(\mathcal L_\theta(P)\) is a nonempty compact subset of the unit coefficient sphere. Indeed \(T_P(\eta)\) has norm one. A sequence \(\eta=r\theta\) has a coefficient-convergent subsequence. Closedness follows by a diagonal choice: if \(Q_j\in\mathcal L_\theta(P)\) tends to \(Q\), choose a center of length greater than \(j\) whose direction and normalized polynomial are within \(1/j\) of \(\theta/|\theta|\) and \(Q_j\). The resulting sequence tends to \(Q\). The same argument gives compactness of the joint graph
\[
\mathcal G_P=\{(\omega,Q):
|\omega|=1,\ Q\in\mathcal L_\omega(P)\}.
\tag{3}
\]
It also proves that \(\mathcal L(P)\) is the union of the directional sets: extract a convergent subsequence of directions from any sequence defining a localization.

## Algebraic inequalities survive projection

A subset of a real finite-dimensional space is **semialgebraic** if it is defined by a finite Boolean combination of polynomial equalities and strict inequalities. Weak inequalities can be expressed in the same language. A map is semialgebraic when its graph is.

**Lemma 2.1 (projection).** A coordinate projection of a semialgebraic set is semialgebraic. Consequently any condition built from polynomial equalities and inequalities by finitely many real existential or universal quantifiers defines a semialgebraic set.

**Proof.** It suffices to eliminate one real variable \(s\). We describe a finite procedure that decides which sign combinations of a finite family of polynomials in \(s\) occur. Their coefficients depend polynomially on the remaining parameters \(x\).

For fixed coefficients, arrange all distinct real roots of the nonzero polynomials in increasing order. Record the sign of each polynomial at each root and on each intervening open interval, including the two unbounded intervals. Call this its ordered sign table. Identically zero polynomials have sign zero throughout. The number of roots is bounded by the sum of the degrees, so there are finitely many possible tables.

We prove that a finite collection of polynomial sign tests on the coefficients determines the table. The induction is on the largest degree and, for a fixed largest degree, on the number of polynomials with that degree. For degree zero, the signs of the constants give the table. Branching on whether leading coefficients vanish first fixes all actual degrees.

Choose a polynomial \(p\) of maximal positive degree. Form a reduced family from all the other polynomials, \(p'\), and the remainders of \(p\) on division by every nonconstant member of the family consisting of the other polynomials and \(p'\). Omit identically zero members after recording that fact. Each remainder has smaller degree than its divisor; \(p'\) has smaller degree than \(p\). The reduced family therefore has one fewer member of maximal degree. Its coefficients are rational functions of the original coefficients on each branch where the relevant leading coefficients are nonzero.

By induction we know the reduced sign table. From it select the roots of the other original polynomials and \(p'\), ignoring roots introduced only by the remainders. At a selected root of a divisor \(r\), the value of \(p\) has the sign of its remainder on division by \(r\). Thus the table gives the sign of \(p\) at every selected point. At infinity the sign is determined by its leading coefficient and degree.

Between successive selected points, \(p'\) has a fixed nonzero sign, so \(p\) is strictly monotone. It has exactly one root inside such an interval if its endpoint signs are strictly opposite, and none otherwise. An endpoint sign of zero already accounts for that endpoint root. These rules include the unbounded intervals using the signs at infinity. At a newly inserted root, every other original polynomial has the constant sign it had throughout the interval. On the two parts of that interval the sign of \(p\) is determined by monotonicity. We have recovered the complete original table.

This procedure has finite branching. The induction decreases the number of polynomials of the current maximal degree before decreasing that degree. A rational coefficient test can be converted into a polynomial test by clearing denominators with a positive even power; branches with zero denominators were already separated by the degree tests. It follows that the parameters producing each table form a semialgebraic set.

For any prescribed Boolean combination of the original polynomial signs, the existence of a real \(s\) satisfying it is decided by whether that combination holds in a point or interval of the table. The projection is a finite union of the corresponding parameter branches. This proves the assertion for one coordinate, hence for any finite projection by iteration. Complements turn universal quantifiers into existential ones. \(\square\)

Here are two useful consequences, with their quantifiers made explicit. The closure of a semialgebraic set is semialgebraic, because membership in the closure says that every positive-radius ball meets it. If a continuous semialgebraic function is minimized over nonempty compact semialgebraic fibers, both the minimum and its minimizer set are semialgebraic: the minimum is attained, and a point is a minimizer exactly when no point in that fiber has a smaller value.

## One parameter has a power expansion

**Lemma 3.1.** A finite-valued semialgebraic function \(h:(R,\infty)\to\mathbb R\) has, after increasing \(R\), a convergent expansion
\[
h(t)=\sum_{j=j_0}^{\infty}a_j t^{-j/\ell}
\tag{4}
\]
for some integer \(\ell>0\) and an integer \(j_0\). There are only finitely many positive powers of \(t^{1/\ell}\). In particular \(h\) is eventually zero or
\[
\begin{gathered}
h(t)=a\,t^\gamma(1+o(1)),\\
a\ne0,\qquad\gamma\in\mathbb Q.
\end{gathered}
\tag{5}
\]

**Proof.** Choose finitely many nonzero real polynomials defining the graph by sign conditions. At each graph point at least one of them must vanish: otherwise all their signs would be constant in a small two-dimensional ball, and the graph would contain that ball. Their product gives a nonzero polynomial \(F(t,y)\) with \(F(t,h(t))=0\).

Over the rational function field \(\mathbb R(t)\), replace \(F\) by its squarefree part as a polynomial in \(y\), and clear denominators. Polynomial division computes this part from \(F\) and its \(y\)-derivative. After excluding finitely many real values of \(t\), its leading coefficient and discriminant are nonzero. Its real roots are then distinct analytic functions, ordered increasingly; their number is constant on the remaining final interval. The graph of each ordered root is semialgebraic, since being the \(j\)-th real root can be expressed by finitely many quantifiers and inequalities. Lemma 2.1 applies.

For each root branch, the set of \(t\)'s where \(h\) equals that branch is semialgebraic. A semialgebraic subset of the line is a finite union of points and intervals: the finitely many real zeros of its defining polynomials divide the line into intervals of constant signs. Since the branches cover the graph, one branch equals \(h\) on a final interval. Thus \(h\) is eventually a single algebraic analytic branch.

For completeness, its fractional-power expansion follows from ordinary one-variable complex analysis. Set \(z=1/t\), clear powers of \(z\), and write its polynomial equation as
\[
\sum_{j=0}^d b_j(z)y^j=0,\qquad b_d\not\equiv0.
\tag{6}
\]
The coefficients are holomorphic near zero. After taking the squarefree part and shrinking the disk, the leading coefficient and discriminant have no zeros on the punctured disk. The roots can be continued locally there by the holomorphic implicit function theorem. Continuing once around zero permutes a finite set of roots. After a finite number \(\ell\) of turns the selected root returns to itself, so substitution \(z=u^\ell\) gives a single-valued holomorphic branch on a punctured \(u\)-disk.

The product \(w=b_d(z)y\) satisfies a monic polynomial whose coefficients are holomorphic at zero. Indeed multiplying (6) by \(b_d^{d-1}\) makes its coefficient of \(w^d\) one, its coefficient of \(w^{d-1}\) equal to \(b_{d-1}\), and each remaining coefficient a nonnegative power of \(b_d\) times a \(b_j\). The elementary root bound for a monic polynomial makes \(w\) bounded near zero. It therefore has a removable singularity on the \(u\)-disk. Dividing its Taylor series by \(b_d(u^\ell)\), which has a finite-order zero or is nonzero at zero, gives a convergent Laurent series with only finitely many negative powers. Returning to \(t\) proves (4). Its coefficients are real because the branch is real on the positive axis. The first nonzero term gives (5). \(\square\)

**Corollary 3.2.** A nonnegative semialgebraic function \(h(t)\) with \(\liminf_{t\to\infty}h(t)=0\) either vanishes eventually or satisfies
\[
0\leq h(t)\leq C t^{-b}
\quad(t\geq R)
\tag{7}
\]
for some \(C,b>0\). A positive semialgebraic function is bounded below by \(c t^{-N}\) for large \(t\), for some \(c>0\) and \(N\geq0\).

**Proof.** In (5), nonnegativity forces \(a>0\). A zero lower limit forces \(\gamma<0\). For a positive function choose \(N\geq\max(0,-\gamma)\) and decrease \(c\). The eventually zero alternative is excluded in the second statement. \(\square\)

**Corollary 3.3.** Let compact nonempty sets \(K_t\subset\mathbb R^d\), \(t>R\), have a semialgebraic graph. There is a semialgebraic selection \(a(t)\in K_t\), and its coordinates have expansions (4).

**Proof.** Choose the smallest first coordinate occurring in \(K_t\), then the smallest second coordinate among points with that first coordinate, and continue through coordinate \(d\). Compactness ensures that each minimum is attained and each successive fiber is compact and nonempty. The resulting point is unique. Its graph is semialgebraic by Lemma 2.1, since each minimum condition says that no competing point has a smaller specified coordinate. Apply Lemma 3.1 to its coordinates. \(\square\)

As another consequence, if a real polynomial \(q\) is strictly positive on all of \(\mathbb R^n\), then
\[
q(\xi)\geq c(1+|\xi|)^{-N}.
\tag{8}
\]
To see this, minimize it on the sphere \(|\xi|=r\). The minimum is positive, attained and semialgebraic in \(r\). Corollary 3.2 gives the lower bound for large \(r\), while compactness gives a positive bound on the remaining ball.

## Reaching a limit on a polynomial path

**Theorem 4.1.** If \(Q\in\mathcal L_\theta(P)\), \(\theta\ne0\), there is a real polynomial path
\[
\eta(t)=\theta t^k+\sum_{j=0}^{k-1}\theta_j t^j,
\qquad k>0,
\tag{9}
\]
such that \(T_P(\eta(t))\to Q\) in coefficient norm.

**Proof.** For \(r>0\), minimize
\[
\begin{gathered}
\left|\frac{\eta}{r}-\theta\right|^2
+|T_P(\eta)-Q|_J^2,\\
|\eta|=r|\theta|.
\end{gathered}
\tag{10}
\]
This sphere is compact. The objective and its minimizer set are semialgebraic: introduce a positive variable \(a\) with \(a^2S_P(\eta)^2=1\) to express \(T_P(\eta)=aP(\eta+\cdot)\) using polynomial conditions.

A sequence defining \(Q\) gives radii \(r_j=|\eta_j|/|\theta|\to\infty\) at which the minimum tends to zero. By Corollary 3.2 the minimum tends to zero along all large radii. Select a minimizer \(\widetilde\eta(r)\) by Corollary 3.3. Then
\[
\frac{\widetilde\eta(r)}r\to\theta,
\qquad T_P(\widetilde\eta(r))\to Q.
\tag{11}
\]
Choose a common denominator \(k\) for the finitely many fractional exponents in the coordinate expansions and substitute \(r=t^k\). Equation (11) implies that the resulting Laurent series has leading term \(\theta t^k\), no higher positive powers, and only integer powers. Retain its nonnegative powers to obtain (9). The discarded part is \(O(t^{-1})\).

This small absolute error preserves the normalized polynomial limit. To verify it uniformly, let \(\mathsf T_h q=q(\cdot+h)\). On the unit coefficient sphere,
\[
|\mathsf T_hq-q|_J\leq C|h|\quad(|h|\leq1),
\tag{12}
\]
by the finite Taylor formula and norm equivalence. Its norm differs from one by at most \(C|h|\). Normalizing \(\mathsf T_hq\) therefore changes \(q\) by \(O(|h|)\). Apply this to \(q=T_P(\widetilde\eta(t^k))\) and \(h=\eta(t)-\widetilde\eta(t^k)\). Since this \(h\) tends to zero, the truncated polynomial path has the same limit \(Q\). \(\square\)

The leading coefficient in (9) is the prescribed vector \(\theta\), including its length. The degree \(k\) and the lower coefficients depend on the localization.

## The direction that disappears

For a polynomial \(q\), let
\[
\begin{gathered}
N_q=\{v\in\mathbb R^n: \partial_vq\equiv0\},\\
V_q=N_q^\perp.
\end{gathered}
\tag{13}
\]
Here \(\partial_v=v\cdot\partial_\xi\); the condition is equivalent to \(q(\xi+sv)=q(\xi)\) for every \(\xi,s\). These are its inactive and active subspaces.

**Theorem 5.1.** Every \(Q\in\mathcal L_\theta(P)\) satisfies \(\theta\in N_Q\). If \(\theta\notin N_P\), then \(\deg Q<\deg P\).

**Proof.** Use the polynomial path (9). Each derivative of \(P\), evaluated on that path, is a polynomial in \(t\). The sum of their squared absolute values consequently has an asymptotic
\[
\begin{gathered}
S_P(\eta(t))=a t^\sigma(1+o(1)),\\
a>0,\qquad\sigma\in\mathbb Z_{\geq0}.
\end{gathered}
\tag{14}
\]
The exponent is nonnegative because one of those derivatives is a nonzero constant.

Fix \(s\in\mathbb R\) and put \(t_s=t+(s/k)t^{1-k}\). Expanding the finite polynomial path gives
\[
\eta(t_s)=\eta(t)+s\theta+O(t^{-1}).
\tag{15}
\]
For \(k=1\) the error is zero; for larger \(k\) the derivatives of the lower powers and the quadratic remainder give the stated bound. Also \(t_s/t\to1\), so (14) gives
\[
\frac{S_P(\eta(t_s))}{S_P(\eta(t))}\to1.
\tag{16}
\]
The limit of \(P(\xi+\eta(t_s))/S_P(\eta(t))\) is therefore \(Q(\xi)\). By (15), coefficient convergence and continuity of translation, the same limit is \(Q(\xi+s\theta)\). Thus \(Q\) is constant along \(\theta\).

If \(\theta\notin N_P\), projection of (9) onto \(N_P^\perp\) tends to infinity in norm. The properness theorem in the active-directions lesson, Theorem 4.1, gives \(S_P(\eta(t))\to\infty\). All derivatives of \(P\) of order \(m\) are constant, so their normalized coefficients tend to zero. The degree of \(Q\) is strictly smaller than \(m\). \(\square\)

In particular \(x\cdot\theta=0\) whenever \(x\in V_Q\) and \(Q\in\mathcal L_\theta(P)\). This orthogonality will determine a restriction on the wavefront set of a regular kernel.

## A uniform rate toward the limiting graph

**Theorem 6.1.** The compact graph \(\mathcal G_P\) in (3) is semialgebraic. There are constants \(C,b,R>0\), depending on \(P\), such that
\[
\begin{gathered}
\operatorname{dist}\left(
\left(\frac{\eta}{|\eta|},T_P(\eta)\right),\mathcal G_P\right)\\
\leq C|\eta|^{-b},\qquad|\eta|\geq R.
\end{gathered}
\tag{17}
\]
Distance uses the Euclidean norm of the direction and the coefficient norm of the polynomial.

**Proof.** Membership of \((\omega,Q)\) in \(\mathcal G_P\) is equivalent to \(|\omega|=|Q|_J=1\) and the following condition: for every \(\epsilon>0\) and \(r>0\) there is \(\eta\) with \(|\eta|>r\), such that its normalized direction is within \(\epsilon\) of \(\omega\) and \(T_P(\eta)\) is within \(\epsilon\) of \(Q\). Introduce positive auxiliary variables for \(|\eta|\) and \(S_P(\eta)^{-1}\); squaring the inequalities expresses this using polynomial conditions and quantifiers. Lemma 2.1 proves semialgebraicity.

Define
\[
h(r)=\max_{|\eta|=r}
\operatorname{dist}\left(
\left(\frac{\eta}{r},T_P(\eta)\right),
\mathcal G_P\right).
\tag{18}
\]
The distance is a minimum over a fixed nonempty compact graph, so it and the attained maximum in (18) are semialgebraic by Lemma 2.1.

We first prove \(h(r)\to0\). Otherwise choose \(r_j\to\infty\) and maximizing centers for which the distance is bounded below by a positive number. After taking a subsequence, their directions and unit-norm polynomials converge to a pair \((\omega,Q)\). By the definition of directional localization this pair belongs to \(\mathcal G_P\), contradicting the distance bound.

Corollary 3.2 now gives \(h(r)\leq Cr^{-b}\), unless it is eventually zero, when any positive exponent works after increasing \(R\). This proves (17). \(\square\)

The direction of the nearby localization in (17) may differ slightly from \(\eta/|\eta|\). Controlling the polynomial and direction together is essential when excluding a whole neighborhood of a candidate wavefront point.

## Differentiating homogeneous coefficient functions

The coefficient norm also converts a derivative estimate for a polynomial path into an estimate for any smooth homogeneous function of its coefficients.

**Lemma 7.1.** Let \(Y\) be a finite-dimensional real normed space. Suppose \(f\) is smooth on \(Y\setminus\{0\}\) and \(f(ay)=a^\mu f(y)\) for \(a>0\). If \(y(s)\) is a \(C^k\) curve and \(y(s)\ne0\), then, for \(k\geq1\),
\[
\begin{aligned}
&\left|\frac{d^k}{ds^k}f(y(s))\right|\\
&\quad\leq C_k |y(s)|^\mu\\
&\qquad\cdot\max_{1\leq j\leq k}
\left(\frac{|y^{(j)}(s)|}{|y(s)|}\right)^{k/j}.
\end{aligned}
\tag{19}
\]
The constant depends on the derivatives of \(f\) through order \(k\) on the unit sphere. It can be chosen uniformly for a compact smooth family of such functions.

**Proof.** Homogeneity gives the multilinear differential estimate
\[
|d^\ell f(y)|\leq C_\ell |y|^{\mu-\ell}.
\tag{20}
\]
Repeated differentiation of a composition gives a finite sum of terms
\[
\begin{gathered}
d^\ell f(y)[y^{(j_1)},\ldots,y^{(j_\ell)}],\\
j_1+\cdots+j_\ell=k,\qquad j_i\geq1.
\end{gathered}
\tag{21}
\]
with constants depending only on \(k\). This form follows by induction: one more derivative either differentiates \(f\) and adds a factor \(y'\), or increases the derivative order of one existing factor.

Let \(M=\max_{1\leq j\leq k}(|y^{(j)}|/|y|)^{1/j}\). Each term in (21), by (20), is bounded by \(C|y|^\mu M^k\). This is (19), since \(M^k\) equals the maximum displayed there. If \(M=0\), all terms are zero. Compactness gives uniform constants for a compact parameter family. \(\square\)

The exponent \(k/j\) is forced by differentiation: a \(j\)-th curve derivative accounts for \(j\) of the total \(k\) differentiations. Using exponent \(k\) for every \(j\) would be incorrect.

## Exercises with complete solutions

**Exercise 1. Elliptic windows.** Compute \(\mathcal L_\theta(P)\) for \(P(\xi)=1+|\xi|^2\). More generally suppose the principal part \(P_m\) never vanishes at a nonzero real point. Find the directional localization.

**Solution.** In the first case \(P(\eta+\xi)=|\eta|^2+2\eta\cdot\xi+|\xi|^2+1\), and \(S_P(\eta)/|\eta|^2\to1\), uniformly in the direction. Thus every normalized limit is the constant \(1\).

For the general elliptic polynomial, compactness of the real unit sphere gives \(|P_m(\omega)|\geq c>0\). As \(\eta=r\omega\), the undifferentiated polynomial is \(r^mP_m(\omega)+O(r^{m-1})\), while all its nonzero derivatives are \(O(r^{m-1})\), uniformly in \(\omega\). Therefore \(S_P(r\omega)=r^m|P_m(\omega)|(1+O(r^{-1}))\). All nonconstant coefficients vanish after normalization, leaving the constant \(P_m(\theta)/|P_m(\theta)|\). This formula includes its complex phase and is unchanged by replacing \(\theta\) with a positive scalar multiple.

**Exercise 2. A whole family along one axis.** For \(P(\xi_1,\xi_2)=\xi_1\xi_2\), show that
\[
\begin{aligned}
\mathcal L_{e_2}(P)
&=\left\{\frac{a+\xi_1}{\sqrt{1+a^2}}:a\in\mathbb R\right\}\\
&\quad\cup\{-1,1\}.
\end{aligned}
\tag{22}
\]

**Solution.** At a center \((u,v)\),
\[
S_P(u,v)^2=(1+u^2)(1+v^2).
\]
In direction \(e_2\), \(v\to+\infty\) and \(u/v\to0\). If \(u\to a\) along a subsequence, the constant coefficient tends to \(a/\sqrt{1+a^2}\), the \(\xi_1\) coefficient to \(1/\sqrt{1+a^2}\), and the other coefficients to zero. If \(|u|\to\infty\), take a subsequence with fixed sign. The constant coefficient tends to that sign and every other coefficient to zero. Any sequence has a subsequence of one of these two types, which exhausts its possible polynomial limits. Paths \((a,t)\), \((t,t^2)\), and \((-t,t^2)\) attain all the stated values. Each limit is independent of \(\xi_2\), as Theorem 5.1 requires.

**Exercise 3. When degree does not decrease.** Let \(P(\xi_1,\xi_2)=\xi_1\). Compute a localization in direction \(e_2\) with the same degree as \(P\). Explain the missing hypothesis in the degree conclusion.

**Solution.** The path \(\eta(t)=(0,t)\) gives \(T_P(\eta(t))=\xi_1\), since \(S_P(0,t)=1\). Thus the degree remains one. Here \(e_2\in N_P\), so the strict-degree clause of Theorem 5.1 does not apply. Its inactive-direction conclusion does apply, and \(\xi_1\) is indeed independent of \(\xi_2\).

**Exercise 4. Discarding a negative power.** For \(P(\xi)=\xi_1\xi_2-1\), compare the paths \((t^{-1},t)\) and \((0,t)\). What normalized limit do they share?

**Solution.** On the first path the translated polynomial is
\[
t\xi_1+t^{-1}\xi_2+\xi_1\xi_2,
\]
and its derivative norm is asymptotic to \(t\). The limit is \(\xi_1\). On the second path the translated polynomial is \(t\xi_1+\xi_1\xi_2-1\), again with norm asymptotic to \(t\), and the same limit results. The centers differ by \((t^{-1},0)\to0\), exactly the absolute error controlled by (12). Replacing the second path by \((0,2t)\) prescribes leading coefficient \(2e_2\) and still gives \(\xi_1\).

**Exercise 5. Why compactness does not give a power.** Consider the unit vectors
\[
v(r)=\frac{(1,a(r))}{\sqrt{1+a(r)^2}},
\qquad a(r)=\frac1{\log(r+e)}.
\]
Show that \(v(r)\to(1,0)\), but its distance from that limit is not \(O(r^{-b})\) for any \(b>0\). Deduce that this curve is not semialgebraic.

**Solution.** For small positive \(a\), its second coordinate is between \(a/2\) and \(a\), while the first-coordinate error is \(O(a^2)\). The distance is therefore comparable to \(1/\log(r+e)\). For each \(b>0\), \(r^b/\log(r+e)\to\infty\), as follows for example by differentiating numerator and denominator in the quotient \(\log r/r^b\). Hence no power bound holds. If the curve were semialgebraic, its distance from \((1,0)\) would be a nonnegative semialgebraic function tending to zero. Corollary 3.2 would give such a bound, a contradiction.

**Exercise 6. The second curve derivative matters.** Take \(f(y)=1/y\) on \(Y=\mathbb R\setminus\{0\}\) and \(y(s)=1+As^2/2\), \(A>0\). Compute \((f\circ y)''(0)\). Check the power \(k/j\) in (19) for \(k=2\), and show that replacing it by \(k\) fails uniformly as \(A\to0\).

**Solution.** At zero, \(y=1\), \(y'=0\), \(y''=A\), and \((1/y)''=-A\). The maximum in (19) is \(\max(0,A^{2/2})=A\), giving the correct scale. Replacing \(2/2\) by \(2\) would bound \(A\) by \(CA^2\) with a constant independent of \(A\), which fails for arbitrarily small positive \(A\).

## References

- **[Coste]** Michel Coste, *Real Algebraic Sets*, lecture notes, 2003, §1.1 on projection and §1.5 on algebraic curves and fractional powers. [ICTP notes](https://indico.ictp.it/event/a02455/session/9/contribution/6/material/0/0.pdf).
- Internal continuation and cyclic descent: [A finite cover and a convergent Laurent series](two-dimensional-evolution-roots-and-model-components.md#a-finite-cover-and-a-convergent-laurent-series), equation (4) and the complete path, homotopy and monodromy argument. Lemma 3.1 here applies that polynomial-at-infinity proof to its original algebraic equation and inverts the covered parameter. Inversion preserves the selected cycle length; a common cover of all root cycles is not needed.
- Internal bounded-removal proof: the bounded-extension argument in [the same finite-cover section](two-dimensional-evolution-roots-and-model-components.md#a-finite-cover-and-a-convergent-laurent-series), following equation (6), and the explicit annular formula and inner-circle estimate in [Covering all arguments and removing infinity](fourier-windows-and-sector-vanishing.md#covering-all-arguments-and-removing-infinity), equations (11)–(12). In Lemma 3.1 here, this argument applies to the bounded product of the selected branch and the leading coefficient. Dividing by that coefficient then permits only a finite pole.
- **[Grubb]** Gerd Grubb, *Distributions and Operators*, author-hosted lecture chapter §5, *Fourier transformation of distributions*: §§5.1–5.3, Definitions 5.1 and 5.8 and Theorems 5.16–5.17 (native pp. 5.1, 5.9 and 5.13). [Exact freely readable chapter](https://www.math.ku.dk/~grubb/dist5.pdf). [Author's notes](https://web.math.ku.dk/~grubb/).
