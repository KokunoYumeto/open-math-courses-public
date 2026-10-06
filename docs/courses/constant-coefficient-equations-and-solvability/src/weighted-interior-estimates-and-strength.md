# Weighted interior estimates and operator strength

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Interior regularity comes from combining the equation with the regularity already known for its solution. Cutting off a solution introduces commutators, so the gain must pay for those terms as well as for the data. We prove an estimate that makes both requirements explicit, establish its converses, and then show that equally strong hypoelliptic operators have comparable distances to their complex zeros.

Read [Operator strength and local inverses](operator-strength-and-local-inverses.md), [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md), and [Hypoellipticity and complex zeros](hypoellipticity-and-complex-zeros.md). The local weighted spaces and their modulation estimates are developed in [Local regularity, sharp embeddings, and compactness](local-regularity-and-compactness.md). Grubb [Grubb] gives the Fourier and local regularity background. The semialgebraic growth argument below uses the results proved in [Symbols at infinity](symbols-at-infinity.md), for which Coste [Coste] provides further context.

Throughout, \(D=-i\partial\), \(1\leq p\leq\infty\), and all weights are positive moderate weights. Write \(B_{p,k}^{\mathrm{loc}}(X)\) for the space defined by the seminorms \(\|\phi u\|_{p,k}\), \(\phi\in C_c^\infty(X)\). A polynomial may have complex coefficients.

## The weight that pays for a commutator

Let \(P\) be a polynomial of positive degree \(m\). Define
\[
\begin{gathered}
S_P(\xi)^2=\sum_{|\alpha|\leq m}|\partial^\alpha P(\xi)|^2,\\
J_P(\xi)^2=\sum_{1\leq|\alpha|\leq m}|\partial^\alpha P(\xi)|^2,\\
r_P(\xi)=\frac{S_P(\xi)}{J_P(\xi)}.
\end{gathered}
\tag{1}
\]
Some derivative of order \(m\) is a nonzero constant. Consequently \(J_P\) is everywhere positive, and \(r_P\geq1\). Finite Taylor expansion of the derivative vector shows that \(S_P\) and \(J_P\) are moderate. In particular, \(J_P\) can be viewed as the norm of the collection of all positive-order derivatives of \(P\); translating that collection expresses each of its entries as a polynomial combination of the same entries. Products, quotients, sums, and minima of positive moderate weights are moderate. For the minimum, if \(a(\xi+h)\leq M(h)a(\xi)\) and \(b(\xi+h)\leq M(h)b(\xi)\), then
\[
\min(a,b)(\xi+h)\leq M(h)\min(a,b)(\xi).
\]
One may take a common polynomial bound \(M\) for any finite collection of weights.

The ratio \(r_P\) measures how much larger the full symbol weight is than the derivatives that appear in a cutoff commutator.

**Theorem 1.1.** Suppose \(X\) is open,
\[
\begin{gathered}
u\in B_{p,k_1}^{\mathrm{loc}}(X),\\
P(D)u=f\in B_{p,k_2}^{\mathrm{loc}}(X).
\end{gathered}
\tag{2}
\]
If a moderate weight \(k\) satisfies, for constants \(C>0\) and finite \(N\geq0\),
\[
\begin{aligned}
k&\leq Ck_1r_P^N,\\
k&\leq C(k_1+S_Pk_2),
\end{aligned}
\tag{3}
\]
then \(u\in B_{p,k}^{\mathrm{loc}}(X)\).

**Proof.** First suppose the first inequality has exponent one. Fix \(\chi\in C_c^\infty(X)\). The finite Leibniz formula is
\[
\begin{aligned}
P(D)(\chi u)&=\chi f\\
&+\sum_{1\leq|\alpha|\leq m}
\frac{D^\alpha\chi}{\alpha!}\,
\partial^\alpha P(D)u.
\end{aligned}
\tag{4}
\]
Since \(|\partial^\alpha P|\leq J_P\), every commutator term belongs to \(B_{p,k_1/J_P}\). This is a global membership because the multiplying coefficient has compact support. The first inequality in (3) gives
\[
\frac{k}{S_P}\leq C\frac{k_1}{J_P},
\tag{5}
\]
so all these terms belong to \(B_{p,k/S_P}\).

The differential-operator estimate applied locally to \(u\) gives \(f\in B_{p,k_1/S_P}^{\mathrm{loc}}(X)\). Thus \(\chi f\) belongs both to \(B_{p,k_2}\) and to \(B_{p,k_1/S_P}\). Their intersection is \(B_{p,k_2+k_1/S_P}\), with equivalent norms: use the triangle inequality for one inclusion, and the pointwise inequalities between each weight and their sum for the other. The second inequality in (3) therefore puts \(\chi f\) in \(B_{p,k/S_P}\).

We have proved \(P(D)(\chi u)\in B_{p,k/S_P}\). The compact-support equivalence in Theorem 2.2 of the operator-strength lesson now gives \(\chi u\in B_{p,k}\). This proves the exponent-one case for every \(p\), including infinity.

For the general case put \(B=k_1+S_Pk_2\), and define
\[
\begin{gathered}
k_j=\min(k_1r_P^j,B),\\
j=0,1,2,\ldots.
\end{gathered}
\tag{6}
\]
These are moderate weights and \(k_0=k_1\). Since \(r_P\geq1\), \(k_{j-1}\geq k_1\), and
\[
\begin{aligned}
k_j&\leq k_{j-1}r_P,\\
k_j&\leq B\leq k_{j-1}+S_Pk_2.
\end{aligned}
\tag{7}
\]
For the first inequality, compare \(k_j\) separately with \(k_1r_P^j\) and with \(Br_P\). Apply the exponent-one case successively, keeping the same data weight \(k_2\). It follows that \(u\in B_{p,k_j}^{\mathrm{loc}}(X)\) for every integer \(j\). Choose \(j\geq N\); (3) implies \(k\leq Ck_j\), which proves the result. \(\square\)

A constant polynomial needs no commutator estimate. If \(P=c\ne0\), the equation is simply \(u=f/c\); membership then follows directly from any inclusion between the data and target weights.

## The exact condition for compact inputs

The second inequality of (3) is necessary without a hypothesis on commutator growth.

**Theorem 2.1.** Fix a nonempty open set \(X\), one \(p\), and moderate weights \(k,k_1,k_2\). For any nonzero polynomial \(P\), the following are equivalent:

1. Every \(u\in\mathcal E'(X)\) satisfying \(u\in B_{p,k_1}\) and \(P(D)u\in B_{p,k_2}\) belongs to \(B_{p,k}\).
2. \(k\leq C(k_1+S_Pk_2)\) on \(\mathbb R^n\) for some \(C\).

**Proof.** The compact-support equivalence gives \(u\in B_{p,S_Pk_2}\) from the equation. Intersecting this with \(B_{p,k_1}\) puts \(u\) in \(B_{p,k_1+S_Pk_2}\), so (2) implies (1).

Conversely choose a closed ball \(K\subset X\) with nonempty interior. Consider the space
\[
\begin{gathered}
\mathcal G_K=\{u:\operatorname{supp}u\subset K,\\
u\in B_{p,k_1},\quad P(D)u\in B_{p,k_2}\},\\
\|u\|_{\mathcal G_K}=\|u\|_{p,k_1}+\|P(D)u\|_{p,k_2}.
\end{gathered}
\tag{8}
\]
It is Banach. Indeed a Cauchy sequence has limits in both weighted Banach spaces; their continuous embeddings in distributions identify the second limit with \(P(D)\) of the first and preserve the support condition. Under (1), the inclusion \(\mathcal G_K\to B_{p,k}\) has closed graph by the same distributional identification. The closed graph theorem gives
\[
\|u\|_{p,k}\leq C
\bigl(\|u\|_{p,k_1}+\|P(D)u\|_{p,k_2}\bigr).
\tag{9}
\]
Take a fixed nonzero \(\phi\in C_c^\infty(\operatorname{int}K)\) and \(u_\eta=e^{i x\cdot\eta}\phi(x)\), with real \(\eta\). The modulation estimates give
\[
\begin{gathered}
c\,k(\eta)\leq\|u_\eta\|_{p,k},\\
\|u_\eta\|_{p,k_1}\leq Ck_1(\eta).
\end{gathered}
\tag{10}
\]
Moreover
\[
P(D)u_\eta=e^{i x\cdot\eta}
\sum_{|\alpha|\leq m}
\frac{\partial^\alpha P(\eta)}{\alpha!}D^\alpha\phi.
\]
Each fixed \(D^\alpha\phi\) has the same modulation upper estimate, and \(|\partial^\alpha P(\eta)|\leq S_P(\eta)\). Hence
\[
\|P(D)u_\eta\|_{p,k_2}
\leq C S_P(\eta)k_2(\eta).
\tag{11}
\]
Substitution in (9) proves (2). \(\square\)

This converse extracts a uniform estimate from a membership assertion; no bound on the inclusion is assumed beforehand.

## What homogeneous solutions force

The first inequality of (3) also has a converse for polynomial weights. We first prove the more general bound from which it follows.

**Theorem 3.1.** Let \(P\) have positive degree, \(X\) be nonempty and open, and \(k,k_1\) be moderate weights. Suppose
\[
\begin{gathered}
P(D)u=0,\quad u\in B_{p,k_1}^{\mathrm{loc}}(X)\\
\Longrightarrow\quad u\in B_{p,k}^{\mathrm{loc}}(X).
\end{gathered}
\tag{12}
\]
Then constants \(C,L>0\) exist such that
\[
\begin{gathered}
\frac{k(\xi)}{k_1(\xi)}
\leq C(1+r_P(\xi))^L e^{Cr_P(\xi)},\\
\xi\in\mathbb R^n.
\end{gathered}
\tag{13}
\]
If the quotient \(k/k_1\) is semialgebraic, there are finite \(N\geq0\) and \(C'>0\) such that
\[
k\leq C'k_1r_P^N.
\tag{14}
\]
In particular, (14) holds when \(k,k_1\) are positive polynomial functions.

**Proof.** The homogeneous solution space in \(B_{p,k_1}^{\mathrm{loc}}(X)\) is a closed Fréchet subspace. The inclusion into \(B_{p,k}^{\mathrm{loc}}(X)\) has closed graph because both spaces embed continuously in distributions. Therefore for a fixed nonnegative, nonzero \(\phi\in C_c^\infty(X)\) there are finitely many cutoffs \(\psi_\nu\) and a constant \(C\) such that every homogeneous solution satisfies
\[
\|\phi u\|_{p,k}
\leq C\sum_{\nu=1}^s\|\psi_\nu u\|_{p,k_1}.
\tag{15}
\]
Let \(\zeta=a+ib\in\mathbb C^n\) be a zero of \(P\). The function \(u_\zeta(x)=e^{i x\cdot\zeta}\) is a homogeneous solution and belongs to every local weighted space.

Let \(M_w(h)\leq C_w\langle h\rangle^{N_w}\) be a shift bound for a weight \(w\). Fourier translation and the shift bound for \(k_1\) give
\[
\|\psi_\nu u_\zeta\|_{p,k_1}
\leq C k_1(a)(1+|b|)^L e^{R|b|}.
\tag{16}
\]
To see the uniform dependence on \(b\), differentiate \(\psi_\nu e^{-x\cdot b}\) a fixed finite number of times. On its fixed compact support every such derivative is bounded by a constant times \((1+|b|)^L e^{R|b|}\). These bounds control the polynomially weighted \(L^p\) norm of its Fourier transform, including the supremum norm.

For the output use the reverse shift inequality
\[
k(a+h)\geq\frac{k(a)}{M_k(-h)}.
\tag{17}
\]
Choose \(\rho\in C_c^\infty(X)\) nonnegative with \(\int\phi\rho>0\). Fourier pairing and Hölder's inequality show
\[
\begin{aligned}
0<c e^{-R'|b|}
&\leq\int\phi(x)\rho(x)e^{-x\cdot b}\,dx\\
&\leq C_\rho
\left\|\frac{\widehat{\phi e^{-x\cdot b}}(h)}
{M_k(-h)}\right\|_{L^p_h}.
\end{aligned}
\tag{18}
\]
Here \(C_\rho\) is finite because \(M_k\widehat\rho\) is rapidly decreasing; the harmless Fourier normalization is included in \(C_\rho\). The first inequality uses the bounded support of \(\phi\rho\) and its positive integral. Equations (17) and (18) give
\[
\|\phi u_\zeta\|_{p,k}\geq c k(a)e^{-R'|b|}.
\tag{19}
\]
This reasoning is valid for \(p=1,\infty\) with their usual dual exponents. Combining (15), (16), and (19) yields
\[
\begin{gathered}
\frac{k(a)}{k_1(a)}
\leq C(1+|b|)^L e^{C|b|},\\
P(a+ib)=0.
\end{gathered}
\tag{20}
\]

For a real \(\xi\), choose a closest zero \(a+ib\), and write \(d=d_P(\xi)\). Then \(|a-\xi|\leq d\) and \(|b|\leq d\). Transferring both weights from \(a\) to \(\xi\) with their polynomial shift bounds gives
\[
\frac{k(\xi)}{k_1(\xi)}
\leq C(1+d)^L e^{Cd}.
\tag{21}
\]
The distance lemma in the preceding lesson gives a useful comparison
\[
d_P(\xi)\leq C r_P(\xi).
\tag{22}
\]
For \(d\leq1\) this follows from \(r_P\geq1\). If \(d>1\), the Cauchy estimate there gives
\[
J_P(\xi)\leq C|P(\xi)|/d
\leq C S_P(\xi)/d,
\]
which proves (22). It also covers real zeros by the first case. Substitution into (21) proves (13).

Now suppose \(q=k/k_1\) is semialgebraic. The function \(r_P\) is semialgebraic because its square is a quotient of sums of squares of real polynomial functions, with positive denominator. For \(R\geq r_P(0)\), define
\[
h(R)=\sup\{q(\xi):r_P(\xi)\leq R\}.
\tag{23}
\]
The set is nonempty, and (13) makes its supremum finite. Its graph is semialgebraic: the assertion that a number is the supremum can be expressed by an upper-bound condition and approximation to that upper bound, using real polynomial quantifiers. The projection theorem proved in the symbols-at-infinity lesson removes those quantifiers. Its one-parameter growth theorem therefore gives \(h(R)\leq C R^N\) for all sufficiently large \(R\), increasing \(N\) to a nonnegative number if necessary. For \(\xi\) with \(r_P(\xi)\) large, use \(q(\xi)\leq h(r_P(\xi))\). For the remaining \(\xi\), (13) is a uniform bound even though that frequency set need not be bounded. Since \(r_P\geq1\), enlarging \(C\) proves (14) everywhere. \(\square\)

Semialgebraic weights include many anisotropic polynomial powers, not just polynomial functions. The last step needs their algebraic growth; moderation alone gives (13).

## The full weighted gain for hypoelliptic equations

**Theorem 4.1.** Let \(P(D)\) be hypoelliptic, \(u\in\mathcal D'(X)\), and \(k\) be moderate. Then
\[
\begin{gathered}
P(D)u\in B_{p,k}^{\mathrm{loc}}(X)\\
\Longrightarrow\quad u\in B_{p,kS_P}^{\mathrm{loc}}(X).
\end{gathered}
\tag{24}
\]

**Proof.** A constant \(P=c\ne0\) is immediate. Suppose \(P\) has positive degree. The quantitative derivative criterion in the preceding lesson gives some \(a>0\) such that
\[
\frac{J_P(\xi)}{S_P(\xi)}
\leq C\langle\xi\rangle^{-a}.
\tag{25}
\]
Indeed outside a ball the derivative ratios relative to \(P\) have a common positive power decay and \(|P|\leq S_P\); on the ball enlarge \(C\). Thus \(r_P\geq c\langle\xi\rangle^a\).

Fix \(Y\) relatively compact in \(X\). A distribution has finite order on a neighborhood of \(\overline Y\). Its compactly supported localizations have Fourier transforms growing at most as \(\langle\xi\rangle^M\), with one \(M\) valid for all cutoffs supported in \(Y\). Choosing \(M'>M+n+1\) gives
\[
u\in B_{p,k_1}^{\mathrm{loc}}(Y),
\qquad k_1(\xi)=\langle\xi\rangle^{-M'},
\tag{26}
\]
for all the indicated \(p\). A moderate weight has a polynomial upper bound, as does \(S_P\). Choose an integer \(N\) large enough that
\[
kS_P\leq Ck_1r_P^N.
\]
The other inequality required by Theorem 1.1 is immediate:
\[
kS_P\leq k_1+S_Pk.
\]
Apply that theorem on \(Y\), with data weight \(k\) and target weight \(kS_P\). Every compact subset of \(X\) is contained in such a \(Y\), proving (24). \(\square\)

The gain is the full derivative-vector weight \(S_P\), which can be anisotropic. Replacing it by an isotropic power can discard part of the estimate.

## Equal strength preserves the geometry of zeros

Recall \(S_P(\xi,t)^2=\sum_\alpha t^{2|\alpha|}|\partial^\alpha P(\xi)|^2\). Equal strength means \(S_{P_1}(\xi,1)\) and \(S_{P_2}(\xi,1)\) are comparable. Proposition 1.2 of the rescaled-symbols lesson proves that the comparison is uniform for every \(t\geq1\).

**Theorem 5.1.** Suppose \(P_1,P_2\) are nonconstant, equally strong polynomials, and \(P_1(D)\) is hypoelliptic. Then \(P_2(D)\) is hypoelliptic. Moreover, for a constant \(C\geq1\),
\[
C^{-1}\leq
\frac{1+d_{P_1}(\xi)}{1+d_{P_2}(\xi)}
\leq C
\quad(\xi\in\mathbb R^n).
\tag{27}
\]
If equally strong polynomials are constant, both are hypoelliptic; (27) is asserted only in the nonconstant case.

**Proof.** For large \(|\xi|\), put \(d_1=d_{P_1}(\xi)\geq1\). The Cauchy estimate in the distance lemma gives, after summing its finitely many bounds,
\[
S_{P_1}(\xi,d_1)\leq C|P_1(\xi)|.
\tag{28}
\]
Uniform rescaled strength comparison and ordinary strength comparison yield
\[
\begin{aligned}
S_{P_2}(\xi,d_1)
&\leq C S_{P_1}(\xi,d_1)\\
&\leq C|P_1(\xi)|
\leq C S_{P_2}(\xi,1).
\end{aligned}
\tag{29}
\]
The positive-order part of the left side is at least \(d_1J_{P_2}(\xi)\). Therefore \(J_{P_2}/S_{P_2}\leq C/d_1\to0\). Since
\[
S_{P_2}^2=|P_2|^2+J_{P_2}^2,
\]
we obtain \(|P_2|/S_{P_2}\to1\). In particular \(P_2\) is eventually nonzero, and all its positive-order derivative ratios tend to zero. The hypoellipticity criterion proves the first conclusion.

For each \(\alpha\ne0\), (29) also gives
\[
\left|\frac{\partial^\alpha P_2(\xi)}{P_2(\xi)}\right|
\leq C d_1^{-|\alpha|}.
\tag{30}
\]
Consequently \(A_{P_2}(\xi)\leq C/d_1\). The lower distance bound \(A_{P_2}\geq c/d_{P_2}\) implies \(d_{P_2}\geq c'd_1\). Both operators are now known to be hypoelliptic, so reversing their roles proves the opposite bound at large \(|\xi|\). On the remaining bounded set the distances are finite continuous functions, and \(1+d_{P_j}\geq1\). Enlarging \(C\) gives (27) globally. \(\square\)

## Quotients that recognize weaker operators

The distinction between ordinary strength and domination is especially simple for a hypoelliptic polynomial.

**Theorem 6.1.** If \(P(D)\) is hypoelliptic, then for every polynomial \(Q\),
\[
\begin{aligned}
Q\prec P&\Longleftrightarrow Q/P=O(1),\\
Q\ll P&\Longleftrightarrow Q/P\to0.
\end{aligned}
\tag{31}
\]
The quotients are taken outside a ball, where \(P\ne0\), and both conditions on the right concern the limit \(|\xi|\to\infty\). Conversely, if the second equivalence holds for every polynomial \(Q\), with eventual nonvanishing of \(P\), then \(P(D)\) is hypoelliptic.

**Proof.** First let \(P\) have positive degree. Hypoellipticity gives \(S_P(\xi)/|P(\xi)|\to1\). Ordinary weakness is equivalent to \(|Q|\leq CS_P\), so it implies the bounded quotient. Conversely a bounded quotient gives that bound outside a ball. On the ball it also holds after increasing \(C\), since \(S_P\) is positive and \(Q\) is bounded. This proves the first equivalence.

Domination has the following characterization from Proposition 3.1 of the rescaled-symbols lesson:
\[
Q\ll P
\Longleftrightarrow
\lim_{t\to\infty}\sup_{\xi\in\mathbb R^n}
\frac{|Q(\xi)|}{S_P(\xi,t)}=0.
\tag{32}
\]
If \(Q\ll P\), choose a fixed \(t\geq1\) making the supremum smaller than a prescribed \(\varepsilon>0\). At this fixed scale the derivative ratios of \(P\) imply
\[
\frac{S_P(\xi,t)}{|P(\xi)|}\longrightarrow1.
\]
Thus \(\limsup_{|\xi|\to\infty}|Q/P|\leq\varepsilon\). Let \(\varepsilon\) decrease to zero.

Conversely suppose \(Q/P\to0\). Given \(\varepsilon>0\), choose \(R\) so that \(|Q|\leq\varepsilon|P|\) when \(|\xi|>R\). On that set \(|Q|/S_P(\xi,t)\leq\varepsilon\) for all \(t\geq1\). On \(|\xi|\leq R\), \(Q\) is bounded and a nonzero top derivative gives \(S_P(\xi,t)\geq c t^m\). The quotient tends uniformly to zero on this ball. This proves (32).

For a nonzero constant \(P\), a polynomial \(Q\) is weaker exactly when it is constant, equivalently when \(Q/P\) is bounded at infinity. It is dominated exactly when it is zero, equivalently when \(Q/P\to0\).

Finally every positive-order derivative \(\partial^\alpha P\) is dominated by \(P\), as already proved in the rescaled-symbols lesson. If the asserted equivalence with quotient decay holds for every \(Q\), each derivative ratio tends to zero. Together with eventual nonvanishing, this is the hypoellipticity criterion. \(\square\)

The limit in (32) increases the window scale uniformly over all centers. The quotient limit in (31) moves the center to infinity at scale one. Hypoellipticity is precisely what permits this identification for every polynomial.

## Exercises with complete solutions

**Exercise 1. One commutator step.** Let \(P(\xi)=1+|\xi|^2\) and \(k_j(\xi)=\langle\xi\rangle^{s_j}\). Determine \(S_P,J_P,r_P\) up to equivalence, and state the gain from a single application of the exponent-one case of Theorem 1.1.

**Solution.** The undifferentiated term has size \(\langle\xi\rangle^2\), first derivatives have size at most \(2|\xi|\), and some second derivative is the constant two. Thus
\[
S_P\asymp\langle\xi\rangle^2,\quad
J_P\asymp\langle\xi\rangle,\quad
r_P\asymp\langle\xi\rangle.
\]
The first condition allows a target exponent at most \(s_1+1\). The sum \(k_1+S_Pk_2\) is comparable to \(\langle\xi\rangle^{\max(s_1,s_2+2)}\), so the second condition allows at most that exponent. One step therefore gives every
\[
s\leq\min(s_1+1,\max(s_1,s_2+2)).
\]
If the data are smoother, repeated steps reach the full exponent \(s_2+2\).

**Exercise 2. A sharp obstruction from compact inputs.** In the same elliptic example, show that if \(s>\max(s_1,s_2+2)\), some compactly supported \(u\) satisfies the two hypotheses in Theorem 2.1 but fails the target membership. Explain why modulated test functions alone need not be that counterexample.

**Solution.** The quotient
\[
\frac{\langle\xi\rangle^s}
{\langle\xi\rangle^{s_1}+S_P(\xi)\langle\xi\rangle^{s_2}}
\]
is unbounded. The equivalence in Theorem 2.1 implies that the universal compact-support membership assertion fails; hence such a \(u\) exists in every nonempty open set. Each individual modulated smooth test belongs to every weighted space, so it does not fail membership. The modulation family instead forces an impossible uniform graph estimate. Closed graph then converts that impossibility into failure of the asserted universal inclusion.

**Exercise 3. Homogeneous transport limits.** For \(P(\xi_1,\xi_2)=\xi_1\), let \(k_1=1\) and \(k=\langle\xi_2\rangle^s\) with \(s>0\). Use Theorem 3.1 to disprove the homogeneous inclusion (12).

**Solution.** Here \(S_P=(1+\xi_1^2)^{1/2}\), \(J_P=1\), and \(r_P=(1+\xi_1^2)^{1/2}\). Along \((0,t)\), \(r_P=1\), while \(k/k_1=(1+t^2)^{s/2}\to\infty\). It violates even the function bound (13). The solutions \(e^{itx_2}\), independent of \(x_1\), are the modulations that expose the missing control.

**Exercise 4. The heat weight.** For \(P(\tau,\xi)=i\tau+|\xi|^2\), compute \(S_P\) and \(J_P\), and state the full \(p=2\) interior gain from data locally in \(L^2\).

**Solution.** With \(d\) spatial variables,
\[
\begin{aligned}
S_P^2&=\tau^2+|\xi|^4+4|\xi|^2+1+4d,\\
J_P^2&=4|\xi|^2+1+4d.
\end{aligned}
\]
The time derivative has modulus one, and the \(d\) nonzero second spatial derivatives have modulus two. Hence \(S_P\asymp1+|\tau|+|\xi|^2\). The previous lesson proves that this operator is hypoelliptic. Theorem 4.1 gives \(u\in B_{2,S_P}^{\mathrm{loc}}\) for every distributional solution with locally \(L^2\) data. Equivalently, after every compact cutoff, \(u\), its time derivative, and all its spatial second derivatives are in \(L^2\); compare the squared Fourier weights using \(\sum_{j,l}\xi_j^2\xi_l^2=|\xi|^4\). This statement uses Plancherel and the equivalence of the displayed weights.

**Exercise 5. Domination without quotient decay.** Explain why \(Q(\xi)=\xi_2\) is dominated by \(P(\xi)=\xi_1\xi_2\), yet the quotient \(Q/P\) fails to tend to zero at infinity where it is defined.

**Solution.** Since \(Q=\partial_1P\), the derivative-domination theorem gives \(Q\ll P\). On \((1,t)\), \(t\ne0\), the quotient is identically one. The polynomial \(P\) is not hypoelliptic: it has unbounded real zero sets and nonconstant localizations. This example shows exactly why the hypothesis in Theorem 6.1 is needed.

**Exercise 6. A semialgebraic supremum over an unbounded set.** In (23), the set \(\{\xi:r_P(\xi)\leq R\}\) can be unbounded. Explain why \(h(R)\) is finite, why attainment is unnecessary, and how the small-\(r_P\) portion is handled when proving (14).

**Solution.** Equation (13) bounds \(q\) on that whole set by \(C(1+R)^L e^{CR}\), independently of \(\xi\). Thus the supremum is finite even without compactness. Its graph can be specified by the two assertions that \(q(\xi)\leq h\) for every eligible \(\xi\), and that for every \(\varepsilon>0\) an eligible \(\xi\) satisfies \(q(\xi)>h-\varepsilon\). These are real polynomial quantifier conditions after expressing the semialgebraic graphs of \(q,r_P\), so the projection theorem applies. Puiseux growth controls large \(R\). For a fixed upper bound on \(r_P\), (13) again gives a uniform bound on \(q\), and \(r_P^N\geq1\) absorbs it by enlarging the constant.

## References

- **[Grubb]** Gerd Grubb, *Distributions and Operators*, open lectures, sections on Fourier transformation, Sobolev spaces, and interior regularity. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- **[Coste]** Michel Coste, *Real Algebraic Sets*, lecture notes, 2003, §1.1 and §1.5. [ICTP notes](https://indico.ictp.it/event/a02455/session/9/contribution/6/material/0/0.pdf).
