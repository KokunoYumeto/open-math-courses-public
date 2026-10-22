# The geometry of coefficients and strength

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026.  Public domain (CC0).*

An equation can keep its strength while its coefficients vary, then lose it at a particular parameter value. The coefficient space is finite-dimensional, but the strength comparison tests infinitely many frequencies. We show how a compact family of linear forms records all the possible losses. This also proves an exact perturbation criterion: adding every complex multiple of a polynomial preserves strength precisely when that polynomial is dominated by the original one. Reciprocal linear forms also control holomorphic hulls and exhibit the equally strong coefficient domain as a Stein manifold.

Read [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md) and [Operator strength and local inverses](operator-strength-and-local-inverses.md) first. We use compactness in finite-dimensional complex vector spaces and the frequency-window estimates already proved there. Hörmander's treatment of constant-coefficient operators [HII] is a reference for the coefficient-form description and the criterion for all complex multiples. Mantlik [Mantlik] and Malgrange [Malgrange] provide broader parameter-dependent and approximation context.

## Evaluation probes in a finite-dimensional space

Fix a nonzero polynomial \(P\). Let
\[
W=\{Q:Q\prec P\},\qquad W_0=\{Q:Q\ll P\}.
\]
Both are finite-dimensional complex vector spaces. A dominated polynomial is weaker, so \(W_0\subset W\). Write \(\mathscr E\) for the set of polynomials of equal strength to \(P\). Thus \(\mathscr E\subset W\), and \(P\in\mathscr E\).

For each real frequency, define a complex-linear form on \(W\) by
\[
\ell_\xi(Q)=\frac{Q(\xi)}{S_P(\xi)}.
\tag{1}
\]
Let \(Y\) be the closure of these forms in \(W^*\), with its finite-dimensional topology. It is a compact set that does not contain zero. To prove boundedness, fix a basis of \(W\) and use the weak comparison for each basis polynomial in (1). To exclude zero, observe that every \(\partial^\alpha P\) belongs to \(W\), and
\[
\sum_\alpha|\ell_\xi(\partial^\alpha P)|^2=1.
\tag{2}
\]
Equation (2) persists in every limit in \(Y\).

The forms relevant to changes of strength are
\[
Y_0=\{\ell\in Y:\ell(R)=0\text{ for every }R\in W_0\}.
\tag{3}
\]
This is a compact subset of \(Y\), hence it also excludes zero. We shall prove that it is nonempty and that it detects precisely the polynomials outside \(\mathscr E\).

Here is a convenient way of obtaining forms in \(Y_0\).

**Lemma 1.1.** Suppose \(t_j\to\infty\) and the frequencies \(\zeta_j\) satisfy
\[
\frac{S_P(\zeta_j,t_j)}{S_P(\zeta_j,1)}\leq C.
\tag{4}
\]
Every limit of a subsequence of \(\ell_{\zeta_j}\) belongs to \(Y_0\).

**Proof.** For \(R\in W_0\), domination gives
\[
|\ell_{\zeta_j}(R)|
\leq C\frac{S_R(\zeta_j,1)}{S_P(\zeta_j,t_j)}\longrightarrow0.
\]
Thus every limit annihilates \(W_0\). Compactness of \(Y\) ensures convergent subsequences. \(\square\)

The frequency sequence need not be specified in advance. The next argument chooses it by enlarging windows and moving within them to a point where the polynomial is large.

## The exact set where strength is preserved

**Theorem 2.1.** The set \(Y_0\) is nonempty. A polynomial \(Q\in W\) belongs to \(\mathscr E\) exactly when
\[
\ell(Q)\ne0\quad\text{for every }\ell\in Y_0.
\tag{5}
\]
Moreover,
\[
W_0=\bigcap_{\ell\in Y_0}\ker\ell.
\tag{6}
\]

**Proof.** We prove three assertions.

First, let \(Q\in W\) fail to have equal strength to \(P\). The reverse comparison fails, so there are frequencies \(\xi_j\) with \(S_Q(\xi_j,1)/S_P(\xi_j,1)\to0\). Let \(m\geq\max(1,\deg P)\). By passing to a more rapidly approaching sequence, choose \(t_j\to\infty\) with
\[
\frac{S_Q(\xi_j,t_j)}{S_P(\xi_j,t_j)}
\leq t_j^m\frac{S_Q(\xi_j,1)}{S_P(\xi_j,1)}\longrightarrow0.
\tag{7}
\]
For \(Q=0\), any \(t_j\to\infty\) and frequencies will do. Use the frequency-window norm equivalence to find \(h_j\), \(|h_j|\leq t_j\), with
\[
|P(\xi_j+h_j)|\geq c S_P(\xi_j,t_j).
\]
Put \(\zeta_j=\xi_j+h_j\). The window estimate for \(Q\) and the displayed lower bound give
\[
\frac{|Q(\zeta_j)|}{S_P(\zeta_j,1)}
\leq C\frac{S_Q(\xi_j,t_j)}{S_P(\xi_j,t_j)}\longrightarrow0.
\tag{8}
\]
The scaled shift estimate gives
\[
S_P(\zeta_j,t_j)\leq C'S_P(\xi_j,t_j)
\leq C''|P(\zeta_j)|\leq C''S_P(\zeta_j,1).
\]
Thus (4) holds. Take a limit of the forms \(\ell_{\zeta_j}\). Lemma 1.1 puts it in \(Y_0\), and (8) says that it annihilates \(Q\). Taking \(Q=0\) in this construction already proves that \(Y_0\) is nonempty.

Second, suppose \(Q\in W\) is annihilated by some \(\ell\in Y_0\). Choose \(\xi_j\) with \(\ell_{\xi_j}\to\ell\). Every positive-order derivative \(\partial^\alpha Q\) is dominated by \(P\), because \(Q\prec P\). Hence \(\ell(\partial^\alpha Q)=0\) for all \(|\alpha|\geq1\). Together with \(\ell(Q)=0\), this gives
\[
\frac{S_Q(\xi_j,1)}{S_P(\xi_j,1)}
=\left(\sum_\alpha|\ell_{\xi_j}(\partial^\alpha Q)|^2\right)^{1/2}
\longrightarrow0.
\]
The reverse comparison is impossible, so \(Q\notin\mathscr E\). This proves (5) in both directions.

Third, (3) immediately shows that \(W_0\) is contained in the intersection in (6). Suppose \(Q\in W\setminus W_0\). The symbol characterization of domination gives a number \(c>0\), scales \(t_j\to\infty\), and frequencies \(\xi_j\) with
\[
|Q(\xi_j)|\geq cS_P(\xi_j,t_j).
\tag{9}
\]
Weak comparison supplies \(|Q(\xi_j)|\leq C_Q S_P(\xi_j,1)\). Thus (9) implies (4) with \(\zeta_j=\xi_j\). A subsequential limit lies in \(Y_0\). Also
\[
|\ell_{\xi_j}(Q)|\geq c\frac{S_P(\xi_j,t_j)}{S_P(\xi_j,1)}\geq c.
\]
Its limit therefore does not annihilate \(Q\). This proves the other inclusion in (6). \(\square\)

The coefficient set \(\mathscr E\) is consequently open in \(W\). For a fixed \(Q\in\mathscr E\), compactness gives
\(\min_{\ell\in Y_0}|\ell(Q)|>0\).
The forms in \(Y_0\) have uniformly bounded norms, so small coefficient changes keep this minimum positive. Its complement is a union of complex hyperplanes, one for each \(\ell\in Y_0\).

The forms act on polynomial coefficients. They do not assert that the same single real frequency witnesses every strength loss. Some are limits along frequencies that escape to infinity.

## Holomorphic hulls stay inside the coefficient domain

The linear forms in Theorem 2.1 also describe the global complex geometry of \(\mathscr E\). Their reciprocals are holomorphic on the entire coefficient domain. They keep holomorphic hulls away from every excluded hyperplane at once.

For a nonempty compact set \(K\) in a complex manifold \(U\), its **holomorphic hull** in \(U\) is
\[
\widehat K_U=
\{Q\in U:|f(Q)|\le\sup_K|f|
                 \text{ for every }f\in\mathcal O(U)\}.
\tag{G1}
\]
The manifold is **holomorphically convex** if every such hull is compact. We use the definition of a **Stein manifold** requiring second countability, holomorphic convexity, separation of distinct points by global holomorphic functions, and global holomorphic functions that supply local coordinates at each point. Disconnected manifolds are permitted. On an open subset of a finite-dimensional complex vector space, countability and the coordinate conditions hold directly.

Choose complex coordinates \(q_1,\ldots,q_N\) on \(W\), and any Hermitian norm \(|\cdot|\). Define
\[
\delta(Q)=\min_{\ell\in Y_0}|\ell(Q)|,\qquad
M=\max_{\ell\in Y_0}\|\ell\| .
\tag{G2}
\]
Compactness, nonemptiness and exclusion of zero for \(Y_0\) were proved above. In particular \(0<M<\infty\), and
\[
|\delta(Q)-\delta(Q')|\le M|Q-Q'|,
\qquad
\mathscr E=\{Q\in W:\delta(Q)>0\}.
\tag{G3}
\]
To prove the inequality, use
\(\big||\ell(Q)|-|\ell(Q')|\big|\le M|Q-Q'|\)
for every \(\ell\), then take minima in each direction.

**Theorem 2.2 (the full coefficient domain is Stein).** Every compact \(K\subset\mathscr E\) has a compact holomorphic hull in \(\mathscr E\). More precisely, put
\[
d_K=\min_{Q\in K}\delta(Q)>0,\qquad
R_K=\max_{\substack{Q\in K\\1\le j\le N}}|q_j(Q)|.
\]
Then
\[
\widehat K_{\mathscr E}
\subset
\{Q\in W: |q_j(Q)|\le R_K\ (1\le j\le N),
                       \ \delta(Q)\ge d_K\}
\Subset\mathscr E .
\tag{G4}
\]
Consequently \(\mathscr E\), and each of its connected components, is Stein.

**Proof.** Each \(q_j\) is globally holomorphic. For every \(\ell\in Y_0\), Theorem 2.1 says that
\[
f_\ell(Q)=\frac1{\ell(Q)}
\tag{G5}
\]
is globally holomorphic on \(\mathscr E\). If \(Q\in\widehat K_{\mathscr E}\), testing the hull definition against the coordinate functions gives the coordinate bounds in (G4). Testing it against every \(f_\ell\) gives
\[
\frac1{|\ell(Q)|}
\le\sup_{Q'\in K}\frac1{|\ell(Q')|}
\le\frac1{d_K}.
\tag{G6}
\]
Thus every \(|\ell(Q)|\) is at least \(d_K\), which gives the second bound in (G4).

The set on the right of (G4) is closed and bounded in \(W\), by continuity of \(\delta\). It is therefore compact. Its positive lower bound for \(\delta\) puts it wholly in \(\mathscr E\). The hull is closed relative to \(\mathscr E\), since it is an intersection of closed modulus inequalities for continuous functions. Hence it is closed in that compact set and is itself compact.

The coordinate functions separate distinct points and have independent differentials everywhere. Euclidean countability passes to the open set \(\mathscr E\). These facts and the compact hull property prove all the stated Stein conditions. For a connected component, the same hull bounds apply; the component is closed relative to \(\mathscr E\), so its intersection with the compact set in (G4) is compact as well. This proves the component assertion. \(\square\)

The conclusion concerns all of \(\mathscr E\), rather than one small coefficient ball. It also lets the uniform strength comparisons of Proposition 5.1 apply on a holomorphic hull.

**Proposition 2.3 (an exhaustion by holomorphically convex sets).** The function
\[
\Psi(Q)=|Q|^2+\frac1{\delta(Q)^2},
\qquad Q\in\mathscr E,
\tag{G7}
\]
is continuous and has compact sublevel sets. It is strictly plurisubharmonic in the precise sense that
\(\Psi(Q)-|Q|^2\) is plurisubharmonic. Every nonempty closed sublevel is equal to its holomorphic hull in \(\mathscr E\). Every nonempty open sublevel \(U_A=\{\Psi<A\}\) is Stein, is relatively compact in \(\mathscr E\), and contains the \(\mathscr E\)-hull of each of its compact subsets. Smoothness of \(\Psi\) is not asserted.

**Proof.** Continuity follows from (G3) and positivity of \(\delta\) on \(\mathscr E\). Also
\[
\delta(Q)^{-2}
=\max_{\ell\in Y_0}|f_\ell(Q)|^2.
\tag{G8}
\]
This maximum satisfies the plurisubharmonic mean inequality directly. Let \(h\) be holomorphic on a neighborhood of the closed unit disk, with that disk's image contained in \(\mathscr E\). For every fixed \(\ell\), Cauchy's mean formula and Cauchy–Schwarz give
\[
|f_\ell(h(0))|^2
\le\frac1{2\pi}\int_0^{2\pi}
                  |f_\ell(h(e^{it}))|^2\,dt.
\]
Taking a maximum on the left and a pointwise maximum inside the integral on the right proves
\[
\delta(h(0))^{-2}
\le\frac1{2\pi}\int_0^{2\pi}
                    \delta(h(e^{it}))^{-2}\,dt.
\tag{G9}
\]
All terms are continuous and bounded on the closed disk because its image is compact in \(\mathscr E\). Thus there is no measurability or unbounded-supremum issue. This proves plurisubharmonicity, including on affine complex disks. Adding the positive quadratic norm gives the asserted strictness.

For \(A>0\), a sublevel \(\Psi\le A\) has
\[
|Q|\le\sqrt A,\qquad
\delta(Q)\ge A^{-1/2}.
\tag{G10}
\]
The set defined by these two inequalities is compact in \(W\) and lies in \(\mathscr E\). The sublevel is closed there, so it is compact. Nonpositive sublevels are empty.

Write \(K_A=\{\Psi\le A\}\), and suppose it is nonempty. If \(Q\in\mathscr E\setminus K_A\), choose \(\ell\in Y_0\) attaining the maximum in (G8) at \(Q\). In the Hermitian space \(W\oplus\mathbb C\), put
\[
G_\ell(Q')=(Q',f_\ell(Q')),\qquad
F_Q(Q')=
\frac{\langle G_\ell(Q'),G_\ell(Q)\rangle}
     {|G_\ell(Q)|}.
\tag{G11}
\]
The Hermitian product is complex linear in its first variable. Thus \(F_Q\) is a globally holomorphic scalar function on \(\mathscr E\). It satisfies \(F_Q(Q)=\sqrt{\Psi(Q)}>\sqrt A\). On \(K_A\), Cauchy–Schwarz gives
\[
|F_Q(Q')|\le |G_\ell(Q')|
\le\sqrt{\Psi(Q')}\le\sqrt A.
\]
This excludes \(Q\) from the hull of \(K_A\). Since points of \(K_A\) always belong to their own hull, equality follows.

Now let \(K\subset U_A\) be compact and nonempty, and put \(B=\max_K\Psi<A\). Monotonicity of hulls and the proved closed-sublevel equality give \(\widehat K_{\mathscr E}\subset K_B\Subset U_A\). Every holomorphic function on \(\mathscr E\) restricts to one on \(U_A\), so \(\widehat K_{U_A}\subset\widehat K_{\mathscr E}\). The former hull is closed relative to \(U_A\), hence is compact in \(K_B\). This proves holomorphic convexity of \(U_A\); the coordinate and countability conditions again follow from its being open in \(W\). Also \(\overline{U_A}\subset K_A\Subset\mathscr E\). Finally any strictly increasing sequence \(A_j\to\infty\), starting above \(\Psi(P)\), gives nonempty open sets with
\(\overline{U_{A_j}}\subset U_{A_{j+1}}\) and union \(\mathscr E\). This proves all assertions. \(\square\)

The one-variable mean and maximum principles used here and in the exercises are proved in [Cauchy bounds and root counts](cauchy-bounds-and-root-counts.md), Lemmas 1.1 and 2.1.

**Example 2.4 (the transport coefficient domain).** For \(P(\xi_1,\xi_2)=\xi_1\), the weaker polynomials are \(Q=a\xi_1+b\), and equal strength means \(a\ne0\). Indeed boundedness along \(\xi_2\) removes that variable, and growth at most linear in \(\xi_1\) removes higher degrees. Conversely these linear polynomials are weaker, and their derivative norm is comparable to \((1+\xi_1^2)^{1/2}\) exactly when \(a\ne0\). The dominated polynomials are the constants. The forms in \(Y_0\) are \(Q\mapsto a\) and \(Q\mapsto-a\), obtained as \(\xi_1\) tends to positive and negative infinity. Use the Euclidean norm for these two coefficient coordinates. Then
\[
\mathscr E=\mathbb C^*\times\mathbb C,\qquad
\delta(a,b)=|a|,\qquad
\Psi(a,b)=|a|^2+|b|^2+|a|^{-2}.
\tag{G12}
\]
This exhaustion diverges both as \(a\) approaches zero and as the coefficients escape to infinity. A sublevel \(\Psi\le A\) is empty for \(A<2\). For \(A\ge2\), its possible values of \(|a|^2\) lie in the exact interval
\[
\frac{A-\sqrt{A^2-4}}2
\le |a|^2\le
\frac{A+\sqrt{A^2-4}}2.
\tag{G13}
\]
This follows by writing \(u=|a|^2>0\) and solving \(u+u^{-1}\le A\); the permissible \(|b|^2\) are then at most \(A-u-u^{-1}\).

The Stein property identifies the global coefficient domain for analytic selection. Constructing a global family of PDE solutions requires an additional analytic argument. The local regular families are constructed in [Regular kernels and changes in the equation](regular-kernels-and-parameter-changes.md), Theorem 3.2.

Global analytic lifting and homogeneous approximation on this coefficient domain and its actual sublevels are proved in Reciprocal graphs and global analytic selection, Theorems 13.1–13.2.

The corresponding universal PDE families, including all weaker-polynomial derivatives and constant-datum pullback to arbitrary complex parameter manifolds, are constructed in Holomorphic solutions on expanding contour scales, Theorem 4.1 and Corollary 5.1.

## Perturbations by every complex multiple

**Theorem 3.1.** For a polynomial \(R\), the following are equivalent:

1. \(R\ll P\).
2. \(P+aR\) has equal strength to \(P\) for every \(a\in\mathbb C\).

**Proof.** If \(R\ll P\), then \(aR\ll P\) for every scalar \(a\), and the stable-strength lemma gives assertion 2. Conversely, assertion 2 at \(a=1\) implies \(R\in W\), by subtracting \(P\) from a polynomial weaker than \(P\). If \(R\notin W_0\), Theorem 2.1 gives \(\ell\in Y_0\) with \(\ell(R)\ne0\). Since \(P\in\mathscr E\), \(\ell(P)\ne0\). Set
\[
a=-\frac{\ell(P)}{\ell(R)}.
\]
Then \(\ell(P+aR)=0\), so \(P+aR\notin\mathscr E\) by (5), contradicting assertion 2. Thus \(R\in W_0\). \(\square\)

This theorem explains the role of dominated corrections in the formal transpose and composition formulas. Their coefficients can have arbitrary complex values at a point, and domination preserves strength for all those values. Weak comparison alone does not give that guarantee.

**Example 3.2.** Let \(P(\xi)=\xi\) in one variable and \(R=i\xi\). For every real \(t\), \(P+tR=(1+it)\xi\) has the same strength as \(P\). Yet \(R\) is not dominated by \(P\), since they have the same degree. The complex value \(a=i\) makes \(P+aR=0\). Requiring only real multiples would therefore be a different condition.

## Two coefficient geometries

### Reading the probes from the principal symbol

The compact detecting family can often be written without lower-order coefficients. Suppose that \(P\) has degree \(m\geq1\) and is of principal type in the sense of [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md#ellipticity-and-a-weaker-principal-condition): its highest homogeneous part \(P_m\) has nonzero gradient at every nonzero real vector.

**Proposition 4.1.** Put
\[
 \begin{aligned}
 \Omega&=\{\theta\in\mathbb R^n:|\theta|=1,\ P_m(\theta)\ne0\},\\
 \lambda_\theta(Q)&=\frac{Q_m(\theta)}{P_m(\theta)}
                       \quad(Q\in W,\ \theta\in\Omega),\\
 Z&=\overline{\{\lambda_\theta:\theta\in\Omega\}}\ \subset W^* .
 \end{aligned}
 \tag{PP1}
\]
Here \(Q_m=0\) if \(Q\) has smaller degree. The family \(Z\) is compact, every member takes the value one on \(P\), and
\[
 \begin{aligned}
 Z&=\left\{\frac{\ell}{\ell(P)}:\ell\in Y_0\right\},\\
 \mathscr E&=\{Q\in W:\lambda(Q)\ne0\text{ for every }\lambda\in Z\},\\
 W_0&=\bigcap_{\lambda\in Z}\ker\lambda .
 \end{aligned}
 \tag{PP2}
\]
In this case \(W_0\) is exactly the space of polynomials of degree at most \(m-1\). Thus \(Z\) acts on the top homogeneous coefficient space.

**Proof.** Theorem 4.2 and Proposition 3.1 of the rescaling lesson show, respectively, that every lower-degree polynomial is dominated by \(P\), and that every polynomial dominated by \(P\) has lower degree. This proves the assertion about \(W_0\). Corollary 4.3 of that lesson gives
\[
       |Q_m(\theta)|\leq C_Q|P_m(\theta)|\qquad(Q\in W).
 \tag{PP3}
\]
Choose a basis of the finite-dimensional space \(W\). Applying (PP3) to its finitely many basis elements bounds all the coordinate values of \(\lambda_\theta\), so \(Z\) is compact. The set \(\Omega\) is nonempty: a nonzero real-variable polynomial cannot vanish on an open real set, as follows by successively treating each variable as a one-variable polynomial. Homogeneity would make vanishing on the whole sphere equivalent to vanishing everywhere. Each \(\lambda_\theta\) takes value one on \(P\), so the same holds throughout \(Z\), which therefore excludes zero.

We prove the first equality in (PP2), including its normalization. Fix \(\theta\in\Omega\). Along its ray the original probes have the limit
\[
 \ell_{s\theta}(Q)=\frac{Q(s\theta)}{S_P(s\theta)}
       \longrightarrow\frac{Q_m(\theta)}{|P_m(\theta)|}
       =\frac{P_m(\theta)}{|P_m(\theta)|}\lambda_\theta(Q)
                  \qquad(s\longrightarrow\infty).
 \tag{PP4}
\]
Indeed, divide numerator and every term of the squared denominator by the appropriate powers of \(s^m\); only the undifferentiated top term of \(P\) remains in the denominator. The limiting form belongs to \(Y\) and annihilates \(W_0\), since all its polynomials have degree below \(m\). It therefore belongs to \(Y_0\). Dividing it by its value on \(P\) gives \(\lambda_\theta\).

Theorem 2.1 says that \(\ell(P)\ne0\) for every \(\ell\in Y_0\). Compactness gives a positive minimum for its absolute value. Consequently the normalization map \(\ell\mapsto\ell/\ell(P)\) is continuous on \(Y_0\), and its image is compact. The preceding ray limits prove that this image contains \(Z\).

For the reverse inclusion, take \(\ell\in Y_0\) and frequencies \(\xi_j\) for which \(\ell_{\xi_j}\to\ell\). For each \(Q\in W\), the difference \(Q-Q_m\) lies in \(W_0\). The same is true of \(P-P_m\). Since \(\ell\) annihilates those differences,
\[
 \frac{Q_m(\xi_j)}{S_P(\xi_j)}\longrightarrow\ell(Q),
 \qquad
 \frac{P_m(\xi_j)}{S_P(\xi_j)}\longrightarrow\ell(P)\ne0.
 \tag{PP5}
\]
Thus \(P_m(\xi_j)\ne0\) eventually, and the corresponding normalized principal probes converge to \(\ell/\ell(P)\). Homogeneity allows \(\xi_j\) to be replaced by \(\xi_j/|\xi_j|\), which belongs to \(\Omega\). Convergence on a finite basis is convergence in \(W^*\). This proves that the normalized image is contained in \(Z\), and establishes the equality. The other two identities in (PP2) now follow from Theorem 2.1: division of a linear form by a nonzero scalar changes none of its zeros. \(\square\)

**Example 4.2 (complex phase).** For \(P(\xi_1,\xi_2)=\xi_1+i\xi_2\) and \(Q=a\xi_1+b\xi_2+c\), write \(\theta=(\cos s,\sin s)\). Then
\[
       \lambda_\theta(Q)=
          \frac{a\cos s+b\sin s}{\cos s+i\sin s}.
 \tag{PP6}
\]
These forms all take value one on \(P\). The unnormalized ray limits in (PP4) instead take value \(e^{is}\) on \(P\). The two families give the same vanishing tests after normalization, while their individual linear forms differ. The constant coefficient disappears from both families, as required by the description of \(W_0\).

For the elliptic linear polynomial \(P(\xi_1,\xi_2)=\xi_1+i\xi_2\), the weaker space consists of all affine linear polynomials
\[
Q=a\xi_1+b\xi_2+c.
\]
Its dominated subspace consists of the constants. By the elliptic classification, \(Q\) has equal strength to \(P\) exactly when its linear part has no nonzero real zero. In coefficient coordinates this means
\[
\operatorname{Im}(\overline a b)\ne0.
\tag{10}
\]
Indeed the real matrix sending \((\xi_1,\xi_2)\) to the real and imaginary parts of the linear form has determinant \(\operatorname{Im}(\overline a b)\). The constant coefficient \(c\) does not affect strength. Along a continuous equal-strength path the sign of this determinant cannot change.

For \(P(\xi_1,\xi_2)=\xi_1\xi_2\), which is of principal type, the weaker space is
\[
Q=a\xi_1\xi_2+b\xi_1+c\xi_2+d.
\tag{11}
\]
To see this, the top-homogeneous comparison forces a quadratic part to vanish on both coordinate axes; it must therefore be a multiple of \(\xi_1\xi_2\). All lower-degree terms are dominated. A polynomial in (11) has equal strength exactly when \(a\ne0\). If \(a\ne0\), divide by \(a\) and apply the stable dominated-perturbation lemma. If \(a=0\), a lower-degree polynomial cannot be as strong as the quadratic \(P\). Here the set where strength is lost is the single coefficient hyperplane \(a=0\).

## Uniform estimates on compact coefficient families

**Proposition 5.1.** If \(K\) is a compact subset of \(\mathscr E\), there is a constant \(C_K\) such that
\[
C_K^{-1}S_P(\xi,t)\leq S_Q(\xi,t)\leq C_K S_P(\xi,t)
\qquad(Q\in K,\ \xi\in\mathbb R^n,\ t\geq1).
\tag{12}
\]

**Proof.** Choose any coefficient norm \(\|\cdot\|_W\). The uniform scaled comparison for each basis polynomial of \(W\) gives
\[
S_R(\xi,t)\leq C\|R\|_W S_P(\xi,t),
\qquad R\in W,\ t\geq1.
\]
This proves the upper bound on bounded \(K\). Define
\[
r(Q)=\inf_{\xi,\ t\geq1}\frac{S_Q(\xi,t)}{S_P(\xi,t)}.
\]
The derivative-vector triangle inequality and the displayed bound give
\(|r(Q)-r(Q')|\leq C\|Q-Q'\|_W\).
For \(Q\in\mathscr E\), the reverse uniform scaled comparison gives \(r(Q)>0\). The continuous positive function \(r\) has a positive minimum on \(K\), proving the lower bound in (12). \(\square\)

This is a compact-family estimate. A family approaching the complement of \(\mathscr E\) can have comparison constants tending to infinity, even if no finite parameter has yet reached that complement.

## Exercises with solutions

**Exercise 1 (entry).** Prove that the evaluation probes in (1) cannot converge to zero, even if \(P(\xi_j)\) vanishes at every point of a frequency sequence.

**Solution.** The polynomial \(P\) itself need not detect those points, but its derivative polynomials belong to \(W\). Equation (2) says that at least one of the finitely many derivative evaluations has absolute value at least the reciprocal square root of the number of derivatives in the sum. If the probes converged to zero as linear forms, each such derivative evaluation would tend to zero, contradicting that sum. This is precisely why normalization by the full derivative norm is useful.

**Exercise 2 (intermediate).** For \(P=\xi_1\xi_2\), show that the two limits obtained from \(\xi=(s,s)\) and \(\xi=(s,-s)\), \(s\to\infty\), act on (11) by \(Q\mapsto a\) and \(Q\mapsto-a\). Explain how they give (6) in this example.

**Solution.** The derivative norm is \((\xi_1^2\xi_2^2+\xi_1^2+\xi_2^2+1)^{1/2}\). On either sequence it is asymptotic to \(s^2\). The mixed quadratic term divided by that norm tends to \(a\) on the first sequence and \(-a\) on the second; all linear and constant terms tend to zero. These forms annihilate the dominated lower-degree polynomials. Their common kernel is exactly \(a=0\), which is \(W_0\) here. Both are members of \(Y_0\), so they explicitly detect every polynomial outside \(W_0\).

**Exercise 3 (intermediate).** For \(Q_t=\xi_1+i t\xi_2\), \(t>0\), determine what happens to its strength comparison with \(P=\xi_1+i\xi_2\) as \(t\downarrow0\).

**Solution.** Every \(Q_t\), \(t>0\), is elliptic of order one, hence has equal strength to \(P\). Along \((0,s)\), the ratio \(S_P/S_{Q_t}\) tends to \(1/t\) as \(s\to\infty\). Thus any reverse comparison constant is at least \(1/t\) and cannot remain bounded as \(t\downarrow0\). At zero the linear coefficient determinant in (10) vanishes, and \(Q_0=\xi_1\) loses control of the second direction. Proposition 5.1 applies on a compact parameter interval bounded away from zero.

**Exercise 4 (advanced).** Show that \(\mathscr E+W_0=\mathscr E\), and that its image in \(W/W_0\) is open. What information is discarded by this quotient?

**Solution.** Every form in \(Y_0\) annihilates \(W_0\). Therefore \(\ell(Q+R)=\ell(Q)\) for \(R\in W_0\), and (5) proves the equality. The quotient projection is open: choose a linear complement of \(W_0\), identify the quotient with that finite-dimensional complement, and observe that projections of open product neighborhoods are open. Since \(\mathscr E\) is open and is invariant under \(W_0\), its quotient image is open as well. The quotient discards precisely the dominated changes of the symbol, which preserve strength for arbitrary complex coefficients. It does not discard every lower-degree term for an arbitrary non-principal-type polynomial.

**Exercise 5 (25 points).** In \(\mathbb C^*\times\mathbb C\), let \(K=\{(a,b):|a|=r,\ |b|=s\}\), where \(r,s>0\). Find its holomorphic hull in that coefficient domain.

**Solution.** The functions \(a\) and \(1/a\) force every point of the hull to have both \(|a|\le r\) and \(|a|\ge r\). The coordinate \(b\) gives \(|b|\le s\). Conversely fix \(|a|=r\) and \(|b|\le s\). For any holomorphic \(f\) on \(\mathbb C^*\times\mathbb C\), the maximum principle in the second variable gives
\[
|f(a,b)|\le\max_{|w|=s}|f(a,w)|\le\sup_K|f|.
\]
Therefore the hull is exactly \(\{(a,b):|a|=r,\ |b|\le s\}\). The puncture in the first coefficient is preserved by the reciprocal test function. Assign 10 points to the upper containment and 15 to the reverse containment.

**Exercise 6 (25 points).** Why is compactness of the family of linear forms important? On \(\mathbb C^2\), consider only \(\ell_n(a,b)=a+b/n\), \(n\ge1\). Show that the set where every \(\ell_n\) is nonzero need not be open.

**Solution.** The point \((0,1)\) is in that set, since \(\ell_n(0,1)=1/n\ne0\) for every \(n\). Yet \((-1/n,1)\) lies in the excluded hyperplane \(\ker\ell_n\) and converges to \((0,1)\). Thus the set is not open at \((0,1)\). The bounded family of forms is missing its limit \(\ell_\infty(a,b)=a\); it is not compact. At the indicated point the infimum of their moduli is zero even though none vanishes. Assign 15 points to the convergent excluded sequence and 10 to the missing limit and zero infimum.

**Exercise 7 (25 points).** For \(P(\xi_1,\xi_2)=\xi_1+i\xi_2\), let \(Q=a\xi_1+b\xi_2+c\). Compute \(\delta(Q)\) from the limiting forms in the principal-symbol description, and identify the connected components of the equal-strength coefficient domain.

**Solution.** Here the limiting forms are \(Q\mapsto a\cos t+b\sin t\). The constant term is annihilated. The square of the minimum modulus is the smallest eigenvalue of the real symmetric matrix
\[
G=\begin{pmatrix}|a|^2&\operatorname{Re}(a\overline b)\\
                 \operatorname{Re}(a\overline b)&|b|^2
  \end{pmatrix}.
\]
Put \(S=|a|^2+|b|^2\) and \(J=\operatorname{Im}(\overline a b)\). Since \(\det G=J^2\),
\[
\delta(Q)^2=\frac{S-\sqrt{S^2-4J^2}}2.
\]
It is positive exactly when \(J\ne0\). In that case \(a\ne0\), and \(J=|a|^2\operatorname{Im}(b/a)\). The two components are therefore
\[
\{a\ne0,\ \operatorname{Im}(b/a)>0\},\qquad
\{a\ne0,\ \operatorname{Im}(b/a)<0\},
\]
with unrestricted \(c\). The coordinate change \((a,b,c)\mapsto(a,b/a,c)\) identifies each with \(\mathbb C^*\) times one open half-plane times \(\mathbb C\), so each is connected. The sign of the continuous nonzero \(J\) prevents a path between them. Assign 10 points to the Gram matrix, 8 to its minimum eigenvalue, and 7 to the components.

**Exercise 8 (25 points).** Suppose a holomorphic regular fundamental-solution family has been constructed on all of \(\mathscr E\). Show why pulling it back along a holomorphic map \(\lambda\mapsto P_\lambda\in\mathscr E\) supplies a family on an arbitrary complex parameter manifold. Must that parameter manifold itself be Stein?

**Solution.** Composition of the holomorphic maps gives the family \(\lambda\mapsto F(P_\lambda)\). Its fundamental-solution identity is the identity at \(P_\lambda\), and its regularity is the regularity of that member. Any locally specified Banach holomorphy passes to the composition in local coordinates. This conclusion is conditional on having the family on all of \(\mathscr E\); the Stein property alone is not that construction.

The parameter manifold need not be Stein. Take the Riemann sphere and the constant map \(P_\lambda=P\); any fixed regular fundamental solution gives a constant holomorphic family. Every holomorphic scalar function on the sphere attains a modulus maximum by compactness, and is constant by the local maximum principle and connectedness. Thus global holomorphic functions cannot separate its distinct points. Assign 12 points to composition and its hypotheses, and 13 to the sphere example and the separation argument.

## References

- [Mantlik] Frank Mantlik, *Partial differential operators depending analytically on a parameter*, Annales de l'Institut Fourier **41** (1991), 577–599. [Original article](https://www.numdam.org/item/10.5802/aif.1266/).
- [Malgrange] Bernard Malgrange, *Existence et approximation des solutions des équations aux dérivées partielles et des équations de convolution*, Annales de l'Institut Fourier **6** (1956), 271–355. [Original article](https://aif.centre-mersenne.org/articles/10.5802/aif.65/).
- [HII] Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 2005 (reprint of the 1983 edition), Coefficient geometry and the comparison of constant-coefficient operators. [Publisher record](https://link.springer.com/book/10.1007/b138375).
