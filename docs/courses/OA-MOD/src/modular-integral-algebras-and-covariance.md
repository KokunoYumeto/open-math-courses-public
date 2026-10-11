# Modular integral algebras and covariance

Two commuting actions can be combined on one Hilbert space or placed on separate tensor factors. An integral of products in the first representation need not come with an obvious, well-defined tensor counterpart. We construct the correspondence by proving both norm inequalities. The same argument then compares the algebras obtained by adjoining integrated modular unitaries.

Let \(M\subset B(H)\) have a faithful normal state \(\varphi\), standard vector \(\xi\), and modular operator \(\Delta\). Normalize \(\|\xi\|=1\), and put

\[
 U_t=\Delta^{it},\qquad \alpha_t(X)=U_tXU_t^*,\qquad
 \chi(b)=\langle b\xi,\xi\rangle\quad(b\in M'),
\]


\[
 K=H\otimes H,\qquad \Omega=\xi\otimes\xi,\qquad
 V_t=U_t\otimes U_t.
\tag{1}
\]

We use two hypotheses:

\[
 \left\|\sum_j a_jb_j\right\|
 \le \left\|\sum_j a_j\otimes b_j\right\|_{\min},
 \qquad \mathrm B(\varphi)=\mathbb C1.
\tag{2}
\]

The first is the multiplication bound of QV01. The second uses the bicentralizer defined in QA01. The earlier results QV06 and QA06 supply the two approximation directions. No separability assumption on \(H\) or \(M_*\) is made.

## 1. Bounded operator integrals on finite measure spaces

We first specify every integral that will occur. Let \(S\) be a locally compact separable metric space, \(\mu\) a finite positive Radon measure, and \(T:S\to B(L)\) a bounded strongly continuous function on an arbitrary Hilbert space \(L\). Define its integral by

\[
 \left\langle\left(\int_S T(s)\,d\mu(s)\right)v,w\right\rangle
 =\int_S\langle T(s)v,w\rangle\,d\mu(s).
\tag{3}
\]

The scalar integrand is continuous and bounded. Its integral is a sesquilinear form bounded by
\(\mu(S)\sup_s\|T(s)\|\,\|v\|\,\|w\|\). Hilbert representation, proved in LH01, therefore gives a unique bounded operator, with

\[
 \left\|\int_S T(s)\,d\mu(s)\right\|
 \le\mu(S)\sup_s\|T(s)\|.
\tag{4}
\]

Testing (3) shows that adjoints and multiplication by a fixed bounded operator pass through the integral. Vector functionals, and finite sums of them, do as well. We will use precisely such functionals in the approximation argument.

Products use the finite-measure product construction and Fubini theorem proved in PI2–PI3. Here are the topological details ensuring that the product measures remain admissible. A separable metric space has a countable base: balls with rational radii and centers in a fixed countable dense set suffice. Local compactness gives a countable cover by open sets with compact closures, by taking suitable members of that base. Finite unions of these closures give a compact exhaustion.

Every finite Borel measure on such a space is Radon. To prove this, first consider approximation by closed subsets and open supersets. A closed set \(F\) has decreasing open neighborhoods \(\{s:d(s,F)<1/n\}\), whose measures decrease to \(\mu(F)\). The Borel sets admitting arbitrarily accurate closed–open approximation form a sigma-algebra. Complements interchange the two approximants. For countable unions, choose open supersets with summable errors; for an inner approximation first truncate the union to finitely many members using continuity from below, and then take the finite union of their closed approximants. Thus all Borel sets have the property. Intersecting a closed approximant with a sufficiently large member of the compact exhaustion makes it compact with arbitrarily small additional loss. This proves inner regularity and outer regularity.

The product of two of our parameter spaces is again locally compact, separable and metrizable. Its Borel sigma-algebra equals the product Borel sigma-algebra, because its open sets are countable unions of basic open rectangles. The finite product measure is consequently Radon by the preceding argument. Applied to scalar matrix coefficients, Fubini and (3) now prove

\[
 \left(\int_S T(s)\,d\mu(s)\right)
 \left(\int_R Q(r)\,d\nu(r)\right)
 =\int_{S\times R}T(s)Q(r)\,d(\mu\otimes\nu)(s,r)
\tag{5}
\]

for bounded strongly continuous families. For example, move the fixed operator \(T(s)\) through the inner integral, use the scalar Fubini theorem, and then use (3) again. No norm measurability of \(s\mapsto T(s)\) as a \(B(L)\)-valued map is needed.

For norm-continuous compactly supported Banach-valued functions on \(\mathbb R\), we also use the norm Riemann integral constructed in MA02. Its norm bound, continuity under bounded linear maps, and scalar Fubini applied to continuous linear functionals justify the corresponding iterated norm integrals below.

## 2. Keep the two representations paired

For bounded strong* continuous maps \(a:S\to M\), \(b:S\to M'\), form the pair

\[
 \left(
 \int_S a(s)b(s)\,d\mu(s),
 \int_S a(s)\otimes b(s)\,d\mu(s)
 \right)\in B(H)\oplus B(K).
\tag{6}
\]

Both integrands are bounded strong* continuous. For products on one Hilbert space this follows by inserting and subtracting a term with one factor fixed. For tensor products it first follows on elementary vectors and then on all vectors by the uniform operator bounds; apply the same argument to the adjoints.

Let \(\mathcal E\) be the set of pairs (6), allowing all the specified parameter spaces and measures. It is a unital *-algebra. A singleton gives \((1,1)\). Scalar multiples are absorbed into \(a\). Finite disjoint unions give addition, with the maps defined separately on each component. Taking adjoints replaces \((a,b)\) by \((a^*,b^*)\), since the two actions commute. For multiplication of two pairs, use the product parameter space and replace the maps by

\[
 a(s)c(r)\in M,\qquad b(s)d(r)\in M'.
\]

Formula (5) identifies both coordinates with the desired products.

Write \(\pi_0,\pi_1\) for the coordinate projections on \(\mathcal E\), and set

\[
 C_0=\pi_0(\mathcal E),\quad C_1=\pi_1(\mathcal E),\qquad
 C=\overline{C_0}^{\|\cdot\|},\quad
 \widehat C=\overline{C_1}^{\|\cdot\|}.
\tag{7}
\]

At this point the two projections might have different kernels. We have not defined a map from \(C_0\) to \(C_1\).

The vector \(\xi\) is cyclic for \(C_0\), since \(M\subset C_0\). The vector \(\Omega\) is cyclic for \(C_1\), because the elementary vectors \(a\xi\otimes b\xi\) have dense span: \(\xi\) is cyclic for both \(M\) and \(M'\). These are the cyclicity assertions needed for the norm comparison.

## 3. From finite product tests to integral tests

We need the following strengthened form of the two earlier approximations. Given finitely many pairs \(a_j\in M,b_j\in M'\), a time bound \(T\), and any positive error and marginal tolerances, we can choose:

- a unit vector \(\zeta\in K\) whose two marginal states are norm-close to \(\varphi,\chi\), whose product moments approximate \(\langle a_jb_j\xi,\xi\rangle\), and for which \(\sup_{|t|\le T}\|V_t\zeta-\zeta\|\) is small;
- a finite convex combination of vector states \(\Psi\) on \(B(H)\), with norm-close \(M\)-marginal and exact \(M'\)-marginal \(\chi\), whose product moments approximate \(\varphi(a_j)\chi(b_j)\), and for which \(\sup_{|t|\le T}|\Psi(U_t)-1|\) is small.

The first assertion is QV06, using the minimum of the requested tolerances. For the second, use the actual construction in QA06:

\[
 \Psi(X)=\sum_{\ell=1}^q\lambda_\ell
 \langle Xu_\ell^*\xi,u_\ell^*\xi\rangle,
 \qquad \sum_\ell\lambda_\ell=1,
 \qquad d_\varphi(u_\ell)<\delta.
\tag{8}
\]

Here \(\delta\) may be chosen arbitrarily small before the finite averaging step. Since \(\Psi(a)=\sum\lambda_\ell\varphi(u_\ell a u_\ell^*)\), the state-defect identity in QA01 gives

\[
 \|\Psi|_M-\varphi\|<\delta.
\]

Every \(u_\ell\) commutes with \(M'\), so \(\Psi|_{M'}=\chi\). The same construction has the required moments and modular estimates. Thus marginal control costs no new bicentralizer hypothesis.

We explain why these assertions remain valid when the finite tests are pairs in \(\mathcal E\). Suppose a state \(\rho\) on either displayed operator algebra has its two marginals within \(\eta\) of \(\varphi,\chi\). If \(\|a(s)\|\le A\), \(\|b(s)\|\le B\), then Cauchy–Schwarz, with the commuting actions placed in the indicated representation, gives

\[
\begin{aligned}
 |\rho(a(s)b(s)-a(r)b(r))|
 &\le B\,\varphi((a(s)-a(r))(a(s)-a(r))^*)^{1/2}\\
 &\quad+A\,\chi((b(s)-b(r))(b(s)-b(r))^*)^{1/2}
       +4AB\sqrt\eta .
\end{aligned}
\tag{9}
\]

In the tensor representation, each product in this formula means the corresponding tensor product. To obtain (9), split the difference into two terms, apply the state Cauchy–Schwarz inequality, and use
\(\rho_1(dd^*)\le\varphi(dd^*)+\eta\|d\|^2\), followed by \(\sqrt{x+y}\le\sqrt x+\sqrt y\). Each difference has norm at most twice the bound on its factor. The two target vector states, \(\omega_\xi\) and \(\omega_\Omega\), satisfy the same bound with \(\eta=0\).

Fix an integral test (6) and an error tolerance. The case \(AB=0\) or \(\mu(S)=0\) is immediate. Otherwise choose a compact \(F\subset S\) so that \(2AB\mu(S\setminus F)\) is smaller than a chosen part of the error budget. On \(F\), the two seminorms in (9) vary continuously, so finitely many neighborhoods of sample points control them. Choose \(\eta\) small enough to control the last term, and apply the finite-product approximation at those sample points with a sufficiently small moment tolerance. Comparing each point with one of the sample points makes the difference between the approximate and target moment functions uniformly small on \(F\). Its integral there is bounded by that supremum times \(\mu(F)\); outside \(F\) the bound is \(2AB\mu(S\setminus F)\). Formula (3) converts these estimates to the desired integral error.

For finitely many integral tests, take the union of the finite lists of sample points and the minimum of their positive tolerances. The compact-time modular bounds and the marginal bounds remain available, because they were required of the same finite-product approximation. We have proved, simultaneously for any finite subset of \(\mathcal E\),

\[
 \langle\pi_1(e)\zeta,\zeta\rangle
       \approx\langle\pi_0(e)\xi,\xi\rangle,
 \qquad
 \Psi(\pi_0(e))\approx\langle\pi_1(e)\Omega,\Omega\rangle,
\tag{10}
\]

with arbitrarily small errors and the prescribed modular estimates. We use finite approximations, not a sequence claimed to converge on an uncountable algebra.

## 4. Cyclicity turns scalar bounds into operator norm bounds

Here is the precise comparison argument, including the kernel issue.

**Lemma 4.1.** Let \(\mathcal F\) be a *-algebra with representations \(p_i\) on Hilbert spaces \(L_i\). Suppose \(v_0\) is a unit cyclic vector for \(p_0\), and

\[
 |\langle p_0(e)v_0,v_0\rangle|\le\|p_1(e)\|
 \qquad(e\in\mathcal F).
\tag{11}
\]

Then \(\|p_0(e)\|\le\|p_1(e)\|\) for all \(e\). The algebras need not be unital.

**Proof.** The formula \(\lambda(p_1(e))=\langle p_0(e)v_0,v_0\rangle\) is well defined by (11), and extends to a bounded functional on \(A=\overline{p_1(\mathcal F)}\). It is positive. Indeed, if \(x\ge0\) in \(A\), approximate \(x^{1/2}\) in norm by elements \(p_1(e_n)\); then

\[
 \lambda(x)=\lim_n\lambda(p_1(e_n)^*p_1(e_n))
 =\lim_n\|p_0(e_n)v_0\|^2\ge0.
\]

The square root belongs to \(A\) by the continuous functional calculus. In the nonunital case this follows from the same polynomial approximation with zero constant term, since the square-root function vanishes at zero; the bounded continuous calculus is proved in BK01.

For \(e,f\in\mathcal F\), positivity applied to
\(p_1(f)^*(\|p_1(e)\|^2 1-p_1(e)^*p_1(e))p_1(f)\in A_+\)
gives

\[
 \|p_0(e)p_0(f)v_0\|^2
 \le\|p_1(e)\|^2\|p_0(f)v_0\|^2.
\tag{12}
\]

The vectors \(p_0(f)v_0\) are dense, so (12) proves the operator norm bound. \(\square\)

Apply (10), let the scalar error decrease to zero, and bound each approximating vector or state evaluation by the operator norm. This proves (11) for \((p_0,p_1,v_0)=(\pi_0,\pi_1,\xi)\). The other approximation proves it for \((\pi_1,\pi_0,\Omega)\). The cyclicity established in Section 2 gives

\[
 \|\pi_0(e)\|=\|\pi_1(e)\|\qquad(e\in\mathcal E).
\tag{13}
\]

In particular the kernels agree. There is therefore a well-defined isometric *-isomorphism

\[
 \eta:C\longrightarrow\widehat C,
 \qquad
 \eta\left(\int_S a(s)b(s)\,d\mu(s)\right)
     =\int_S a(s)\otimes b(s)\,d\mu(s).
\tag{14}
\]

Both the well-definedness and the boundedness have been proved before extending the correspondence to the closures.

## 5. Smoothing and an automorphism of the coefficient algebra

The action \(\alpha_t\) preserves \(C_0\) and \(C\): in (6), conjugate both maps by \(U_t\). Its tensor counterpart is \(\widehat\alpha_t=\operatorname{Ad}(V_t)\), and (14) gives

\[
 \eta\alpha_t=\widehat\alpha_t\eta.
\tag{15}
\]

Define the algebra of norm-continuous elements by

\[
 A_\Delta=\{c\in C:\|\alpha_t(c)-c\|\longrightarrow0
                         \text{ as }t\longrightarrow0\}.
\tag{16}
\]

It is a closed, invariant unital *-subalgebra. Sums and adjoints preserve the condition; for products use
\(\|\alpha_t(cd)-cd\|\le\|c\|\|\alpha_t(d)-d\|+\|d\|\|\alpha_t(c)-c\|\).
Norm limits preserve it by the isometry of \(\alpha_t\). Continuity at zero implies continuity at every time by the group law.

For \(c\in C\), \(f\in C_c(\mathbb R)\), define the strong integral

\[
 \alpha_f(c)=\int_{\mathbb R}f(t)\alpha_t(c)\,dt.
\tag{17}
\]

It belongs to \(C\). For \(c\in C_0\), combine its integral presentation with the time integral over a compact interval containing \(\operatorname{supp}f\). Formula (5) and scalar Fubini express (17) as an admissible integral of
\(f(t)\alpha_t(a(s))\alpha_t(b(s))\); the maps are jointly strong* continuous. For general \(c\), approximate in norm by \(C_0\), using \(\|\alpha_f(c)\|\le\|f\|_1\|c\|\).

A change of the scalar integration variable gives

\[
 \|\alpha_r(\alpha_f(c))-\alpha_f(c)\|
 \le\|f(\,\cdot-r)-f\|_1\,\|c\|\longrightarrow0.
\tag{18}
\]

The last convergence follows from uniform continuity of \(f\) on a common compact interval containing the small translates of its support. Thus \(\alpha_f(c)\in A_\Delta\). In particular this holds for every \(c\in C^*(M,M')\), as required by the original smoothing lemma.

There is a useful compatibility that must not be inferred from normality of \(\eta\), since no such normality has been asserted:

\[
 \eta(\alpha_f(c))=\int f(t)\widehat\alpha_t(\eta(c))\,dt.
\tag{19}
\]

For \(c\in C_0\), both sides are exactly the paired double integrals just constructed. Norm approximation and the bound \(\|f\|_1\|c\|\) extend the equality to \(C\).

Choose nonnegative continuous kernels \(h_n\) of integral one supported in \([-1/n,1/n]\), for instance normalized triangular functions. Then \(\alpha_{h_n}(c)\to c\) strongly and strongly on adjoints: evaluate the difference on a vector and use strong* continuity of the unitary conjugation orbit. The same holds for the right side of (19). Consequently

\[
 \overline{A_\Delta\xi}=H,\qquad
 \overline{\eta(A_\Delta)\Omega}=K.
\tag{20}
\]

Here one first approximates the dense cyclic orbits of \(C_0\) and \(C_1\), and then uses these kernels.

Fix \(\tau\in\mathbb R\), and put \(W_\tau=U_\tau\otimes1\). Conjugation by \(W_\tau\) preserves \(C_1\): it replaces \(a(s)\) by \(\sigma_\tau^\varphi(a(s))\). It therefore preserves \(\widehat C\). Transporting this automorphism by \(\eta\) gives an automorphism \(\theta_\tau\) of \(C\) with

\[
 \theta_\tau\left(\int_S a(s)b(s)\,d\mu(s)\right)
 =\int_S\sigma_\tau^\varphi(a(s))b(s)\,d\mu(s).
\tag{21}
\]

Since \(W_\tau\) commutes with every \(V_t\), this automorphism commutes with \(\alpha\) and preserves \(A_\Delta\). The argument works for every real \(\tau\).

## 6. The integrated covariant algebras

For \(y\in C_c(\mathbb R,A_\Delta)\), set

\[
 T_0(y)=\int_{\mathbb R}y(t)U_t\,dt,
 \qquad
 T_1(y)=\int_{\mathbb R}\eta(y(t))V_t\,dt.
\tag{22}
\]

These are strong integrals, with
\(\|T_i(y)\|\le\int\|y(t)\|\,dt\).
The paired operators \((T_0(y),T_1(y))\) form a *-algebra \(\mathcal D\). To check this, define

\[
 (y*z)(r)=\int_{\mathbb R}y(s)\alpha_s(z(r-s))\,ds,
 \qquad y^\sharp(r)=\alpha_r(y(-r)^*).
\tag{23}
\]

The first integral is a norm integral in \(A_\Delta\). The map \((s,r)\mapsto\alpha_s(z(r-s))\) is jointly norm continuous: separate the variation of \(z\) from the variation of the action on one fixed element, and use that the action is isometric. On each relevant compact rectangle this continuity is uniform. It follows by the norm integral bound that \(y*z\) is continuous; its support is contained in \(\operatorname{supp}y+\operatorname{supp}z\). Also \(y^\sharp\) is continuous with compact support.

The covariance identity \(U_s c=\alpha_s(c)U_s\), followed by scalar Fubini and the substitution \(r=s+t\), gives

\[
 T_0(y)T_0(z)=T_0(y*z),\qquad T_0(y)^*=T_0(y^\sharp).
\tag{24}
\]

For example the product integrand is
\(y(s)\alpha_s(z(t))U_{s+t}\); it has compact support and bounded norm, so each matrix coefficient is absolutely integrable. Equation (15) gives the identical calculation for \(T_1\). Addition is immediate. This proves the assertion about \(\mathcal D\), without presupposing a correspondence between its coordinate ranges.

Define

\[
 B=\overline{\{T_0(y):y\in C_c(\mathbb R,A_\Delta)\}},\qquad
 \widehat B=\overline{\{T_1(y):y\in C_c(\mathbb R,A_\Delta)\}},
\tag{25}
\]

where both closures are in norm. These are C*-algebras, not assumed unital. If \(h\in C_c(\mathbb R)\) has integral one, then

\[
 T_0(hc)\xi=c\xi,
 \qquad T_1(hc)\Omega=\eta(c)\Omega
 \qquad(c\in A_\Delta),
\tag{26}
\]

because \(U_t\xi=\xi\) and \(V_t\Omega=\Omega\). By (20), the displayed coordinate representations of \(\mathcal D\) have cyclic vectors \(\xi\) and \(\Omega\).

## 7. Norm comparison after adjoining modular unitaries

The approximations of Section 3 extend from \(C_0\) to any finite collection in \(C\). Approximate each coefficient in norm by \(C_0\), use (13) for the same norm control on the tensor side, and bound state evaluations by the norm. The time and marginal requirements can be retained throughout.

For a unit vector \(\zeta\) with \(\|V_t\zeta-\zeta\|<\delta\),

\[
 |\langle\eta(c)V_t\zeta,\zeta\rangle
       -\langle\eta(c)\zeta,\zeta\rangle|
 \le\|c\|\delta.
\tag{27}
\]

For a state \(\Psi\) with \(|\Psi(U_t)-1|<\delta\), state Cauchy–Schwarz instead gives

\[
\begin{aligned}
 |\Psi(cU_t)-\Psi(c)|
 &\le\|c\|\,\Psi((U_t-1)^*(U_t-1))^{1/2}\\
 &\le\|c\|\sqrt{2\delta},
\end{aligned}
\tag{28}
\]

since that positive expectation is \(2-2\operatorname{Re}\Psi(U_t)\).

Fix finitely many functions \(y\) as in (22), and a compact time interval containing their supports. Each \(y\) has norm-compact range, so finitely many coefficient values approximate its whole range in norm. Apply the preceding finite-coefficient approximations to the union of these lists, with modular bounds valid throughout the time interval. The triangle inequality extends the coefficient-state approximation uniformly to every value \(y(t)\). Equations (27) and (28), integrated over that fixed interval, show that the following errors can be made arbitrarily small:

\[
 \langle T_1(y)\zeta,\zeta\rangle
     -\langle T_0(y)\xi,\xi\rangle,
 \qquad
 \Psi(T_0(y))-\langle T_1(y)\Omega,\Omega\rangle.
\tag{29}
\]

For the target values we used \(U_t\xi=\xi\), \(V_t\Omega=\Omega\). The integral-state interchanges on the approximation side are valid because \(\omega_\zeta\) is a vector state and \(\Psi\) is the finite sum (8). The estimates use only a finite time interval, bounded coefficient norms and freely chosen positive tolerances.

Letting those errors decrease to zero yields both scalar bounds of Lemma 4.1 for the coordinate representations of \(\mathcal D\). Their cyclic vectors were proved in (26). The lemma gives

\[
 \|T_0(y)\|=\|T_1(y)\|
 \quad\text{for every }y\in C_c(\mathbb R,A_\Delta).
\tag{30}
\]

Thus equality of the first coordinates implies equality of the second coordinates, and conversely. We obtain an isometric *-isomorphism

\[
 \eta_1:B\longrightarrow\widehat B,
 \qquad \eta_1(T_0(y))=T_1(y).
\tag{31}
\]

This proves the integrated correspondence rather than merely postulating it from the coefficient correspondence.

## 8. The extended modular automorphism

Conjugation by \(W_\tau=U_\tau\otimes1\) preserves \(\widehat B\). Indeed, it commutes with \(V_t\), and (21) gives

\[
 W_\tau T_1(y)W_\tau^*
 =\int\eta(\theta_\tau(y(t)))V_t\,dt
 =T_1(\theta_\tau\circ y).
\tag{32}
\]

The transformed coefficient function is still norm continuous, compactly supported and \(A_\Delta\)-valued. The same assertion for \(-\tau\) proves equality of the image algebra, not just inclusion. Hence

\[
 \beta_\tau=\eta_1^{-1}\operatorname{Ad}(W_\tau)\eta_1
 \in\operatorname{Aut}(B)
\]

satisfies the exact formula

\[
 \beta_\tau\left(\int y(t)\Delta^{it}\,dt\right)
 =\int\theta_\tau(y(t))\Delta^{it}\,dt.
\tag{33}
\]

It fixes every \(\int h(t)\Delta^{it}\,dt\), \(h\in C_c(\mathbb R)\), because \(\theta_\tau(1)=1\). It therefore fixes the norm-closed algebra generated by these integrated scalar functions. This last assertion is about actual elements of \(B\); no individual \(\Delta^{it}\) is being asserted to lie in \(B\).

Under the two hypotheses (2), formulas (18), (21), and (33) prove the smoothing and automorphism conclusions. Their use for a particular class of factors requires a proof of both hypotheses; no bicentralizer theorem for that class is supplied by these constructions.

## 9. A finite-dimensional check

Take \(M=M_n(\mathbb C)\) in its trace standard form on \(H=L^2(M,\operatorname{Tr}/n)\). Then \(\Delta=1\). Matrix units show that the left and right actions generate all of \(B(H)\): the map \(L_{E_{ij}}R_{E_{kl}}\) sends \(E_{pq}\) to \(\delta_{jp}\delta_{qk}E_{il}\). As the four indices vary, these are the matrix units between the basis vectors of \(H\). Thus \(C=B(H)\), and \(A_\Delta=C\).

The bicentralizer is scalar in this case. Every constant sequence in \(M\) is asymptotically central for the trace, so a bicentralizer element commutes with every element of \(M\), hence is scalar; conversely scalars satisfy the defining condition. The multiplication bound follows from the earlier semidiscrete result in QV01, applied to this finite-dimensional algebra. The conclusions above therefore apply.

Since \(U_t=1\), choosing \(y(t)=h(t)c\) with \(\int h=1\) shows \(B=C\). Both \(\theta_\tau\) and \(\beta_\tau\) are the identity. The correspondence \(\eta\) is still between the displayed representations on \(H\) and \(H\otimes H\), whose dimensions are \(n^2\) and \(n^4\). For \(n>1\) it cannot be conjugation by a unitary between those two Hilbert spaces. Isometry of the represented C*-algebras is the conclusion; equality of their representation multiplicities is not needed.

**Reference.** M. Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, Section 4, Lemmas 4.14–4.15, printed pp.384–386. The treatment above proves the integral approximation and the two norm comparisons explicitly, retains the two hypotheses (2), and allows every real value of the modular parameter. The subsequent local-intertwiner construction is a further step toward approximate innerness.
