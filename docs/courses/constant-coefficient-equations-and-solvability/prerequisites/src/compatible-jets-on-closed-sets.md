# Compatible jets on closed sets

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Checked once by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

Prescribing a function and its derivatives on a closed set is more than assigning numbers at its points. Nearby assignments must fit one Taylor expansion to the required order. Whitney's extension theorem says that this compatibility is exactly what is needed. The proof glues local Taylor polynomials at a scale comparable to the distance from the set. Its estimate then describes what a finite-order distribution supported on that set can measure.

The prerequisites are [Jets, supported distributions and local operators](jets-supported-distributions-and-local-operators.md), [When a kernel is smooth](when-a-kernel-is-smooth.md), Taylor's formula, smooth mollifiers and elementary Euclidean distance geometry. We prove the extension construction and its bounds, including the partition used in the gluing. References are the original paper [Whitney 1934], the jet perspective of [Kolář–Michor–Slovák 1993], and the distribution background in [Dyatlov 2026].

## The information between two points

Fix a nonempty compact set \(F\subset\mathbb R^n\), \(n\ge1\), and an integer \(k\ge0\). A jet of order \(k\) on \(F\) is a family of continuous scalar functions \(f_\alpha:F\to\mathbb C\), indexed by \(|\alpha|\le k\). The intended meaning is \(f_\alpha=\partial^\alpha f|_F\), but no extension is assumed yet. At \(a\in F\), form the polynomial

\[
P_a(x)=\sum_{|\alpha|\le k}
\frac{f_\alpha(a)}{\alpha!}(x-a)^\alpha.
\tag{1.1}
\]

For \(a,b\in F\), \(a\ne b\), define the normalized remainder

\[
R_\alpha(a,b)=
\frac{f_\alpha(a)-\partial^\alpha P_b(a)}
{|a-b|^{k-|\alpha|}}.
\tag{1.2}
\]

On the diagonal put \(R_\alpha(a,a)=0\). The Whitney compatibility condition is that each \(R_\alpha\) is continuous on \(F\times F\), including that diagonal value. Equivalently,

\[
\omega(r)=\max_{|\alpha|\le k}
\sup_{\substack{a,b\in F\\0<|a-b|\le r}}
|R_\alpha(a,b)|\longrightarrow0
\quad(r\downarrow0).
\tag{1.3}
\]

The supremum over an empty set is zero. Continuity away from the diagonal already follows from the continuity of the \(f_\alpha\). Compactness makes continuity at all diagonal points equivalent to the uniform condition (1.3). For \(|\alpha|=k\), the denominator in (1.2) is one, so this part of the condition is simply continuity of the top jet values.

Write \(W^k(F)\) for these compatible jets, with norm

\[
\|f\|_{W^k(F)}
=\sum_{|\alpha|\le k}\sup_F|f_\alpha|
+\sum_{|\alpha|\le k}\sup_{F\times F}|R_\alpha|.
\tag{1.4}
\]

This is a norm because its first sum detects every component. The second sum is finite by continuity on the compact product. When \(F\) is a single point, that sum is zero, and any finite jet is compatible.

Every \(C^k\) function on a neighborhood of \(F\) gives a compatible jet. Indeed Taylor's formula for each \(\partial^\alpha f\) gives its remainder as \(o(|a-b|^{k-|\alpha|})\), uniformly for nearby points of \(F\). The uniformity uses continuity of the order-\(k\) derivatives on a compact neighborhood. Segments between sufficiently close points stay in that neighborhood. For \(|\alpha|=k\), ordinary continuity supplies the assertion.

We will prove the converse with a bounded linear extension. The word linear refers to the entire family of assigned jet values.

## A partition whose scale follows the distance

Put \(\Omega=\mathbb R^n\setminus F\) and \(d(x)=\operatorname{dist}(x,F)\). We need cutoffs on \(\Omega\) whose derivatives grow only like powers of \(d(x)^{-1}\). Fixed-size cutoffs would not resolve the small gaps near \(F\).

**Lemma 2.1 (a distance-adapted partition).** There is a countable locally finite smooth partition \(1=\sum_Q\psi_Q\) on \(\Omega\), with \(0\le\psi_Q\le1\), and points \(a_Q\in F\), such that:

1. At each point at most \(N_n\) functions have nonzero support there.
2. Each support is compact in \(\Omega\), its diameter is at most twice its distance from \(F\), and
\[
|\partial^\beta\psi_Q(x)|\le C_{n,\beta}d(x)^{-|\beta|}.
\tag{2.1}
\]
3. If \(x\in\operatorname{supp}\psi_Q\), then
\[
|x-a_Q|\le C_n d(x).
\tag{2.2}
\]

The constants depend on dimension and derivative order, not on a smoothness assumption about \(F\).

**Proof.** Use the usual dyadic grid of cubes, with side lengths \(2^j\), \(j\in\mathbb Z\). Select maximal cubes \(Q\) satisfying

\[
4\operatorname{diam}Q\le\operatorname{dist}(Q,F).
\tag{2.3}
\]

Distances and diameters here refer to the closed cube. Every point of \(\Omega\) is contained in sufficiently small admissible cubes. The chain of parents cannot remain admissible forever: a fixed point of \(F\) bounds the distance of any parent containing \(x\) from \(F\), while its diameter tends to infinity. Hence every small admissible cube is contained in a maximal one. Maximal dyadic cubes have disjoint interiors and their closed cubes cover \(\Omega\).

Let \(D_Q=\operatorname{diam}Q=\sqrt n\,\ell_Q\), where \(\ell_Q\) is the side length. Its parent has diameter \(2D_Q\) and fails (2.3). A point of the parent is at distance at most \(2D_Q\) from a point of \(Q\). Thus

\[
4D_Q\le\operatorname{dist}(Q,F)<10D_Q.
\tag{2.4}
\]

Let \(Q^*\) be the concentric cube with side length \(9\ell_Q/8\). Every point of \(Q^*\) lies at distance at most \(D_Q/16\) from \(Q\). Consequently, on \(Q^*\),

\[
\frac{63}{16}D_Q\le d(x)<\frac{177}{16}D_Q.
\tag{2.5}
\]

The upper bound uses the diameter of \(Q\) in addition to (2.4). In particular \(Q^*\) stays away from \(F\), and its diameter \(9D_Q/8\) is less than twice its distance from \(F\).

If several enlarged cubes contain one point \(x\), (2.5) makes all their side lengths comparable to \(d(x)\). Their disjoint original interiors lie in a ball about \(x\) of radius at most a dimensional constant times \(d(x)\), and each has volume at least a dimensional constant times \(d(x)^n\). Comparing volumes bounds their number by an integer \(N_n\). The same estimates prove local finiteness: on a compact subset of \(\Omega\), \(d\) has a positive minimum and a finite maximum, so only finitely many dyadic scales and cube centers can occur.

Choose one nonnegative smooth bump \(\eta\), equal to one on \([-1/2,1/2]^n\), supported in \((-9/16,9/16)^n\), and at most one. For the center \(c_Q\), set

\[
\eta_Q(x)=\eta((x-c_Q)/\ell_Q),\qquad
S(x)=\sum_Q\eta_Q(x),\qquad
\psi_Q(x)=\frac{\eta_Q(x)}{S(x)}.
\]

The original cubes cover \(\Omega\), so \(1\le S\le N_n\). Derivatives of \(\eta_Q\) have bounds \(C_\beta\ell_Q^{-|\beta|}\). At each point, the overlap and scale estimates give \(|\partial^\beta S|\le C_{n,\beta}d^{-|\beta|}\). Repeated differentiation of \(1/S\), using \(S\ge1\), gives the same type of bound for its derivatives. The product rule proves (2.1). These quotients are a nonnegative smooth partition, with supports contained in \(Q^*\), so they satisfy the stated diameter and overlap properties.

For each center \(c_Q\), choose a nearest point \(a_Q\in F\), once and for all. Such a point exists by compactness. Equations (2.4)–(2.5), and the diameter of \(Q^*\), bound \(|x-a_Q|\) by a dimensional constant times \(D_Q\), hence by a constant times \(d(x)\). This proves (2.2). All choices depend on \(F\), not on the jet to be extended. \(\square\)

## Comparing Taylor polynomials before gluing

Here is the estimate that makes the partition work. Since \(P_a-P_b\) is a polynomial of degree at most \(k\), its Taylor expansion at \(a\) is exact:

\[
\partial^\gamma(P_a-P_b)(x)
=\sum_{|\delta|\le k-|\gamma|}
\frac{\partial^{\gamma+\delta}(P_a-P_b)(a)}{\delta!}
(x-a)^\delta.
\tag{3.1}
\]

The coefficient in the numerator is
\[
\partial^{\gamma+\delta}(P_a-P_b)(a)
=R_{\gamma+\delta}(a,b)
|a-b|^{k-|\gamma|-|\delta|}.
\]

If \(a=b\), the difference is zero. Otherwise (3.1) gives

\[
|\partial^\gamma(P_a-P_b)(x)|
\le C_{n,k}\omega(|a-b|)
(|a-b|+|x-a|)^{k-|\gamma|}.
\tag{3.2}
\]

Replacing \(\omega\) by \(\|f\|_{W^k(F)}\) gives a corresponding bounded estimate at all distances. Most importantly, if \(a\) and \(b\) are both within \(A r\) of \(x\), then

\[
|\partial^\gamma(P_a-P_b)(x)|
\le C_{n,k,A}\omega(2Ar)r^{k-|\gamma|}.
\tag{3.3}
\]

The factors from derivatives of the partition will consume powers of \(r\); the exponent in (3.3) supplies exactly those powers.

**Theorem 3.1 (bounded extension of compatible jets).** There is a linear map

\[
E:W^k(F)\longrightarrow C_c^k(\mathbb R^n)
\]

such that

\[
\partial^\alpha(Ef)|_F=f_\alpha
\quad(|\alpha|\le k),\qquad
\|Ef\|_{C^k}\le C_{n,k}\|f\|_{W^k(F)}.
\tag{3.4}
\]

Its outputs have support in one fixed compact neighborhood of \(F\). Together with necessity above, this characterizes exactly the finite jets which come from \(C^k\) functions.

**Proof.** First define

\[
v(x)=\sum_Q\psi_Q(x)P_{a_Q}(x)
\quad(x\notin F),\qquad
v(x)=f_0(x)\quad(x\in F).
\tag{3.5}
\]

Off \(F\), the sum is locally finite and smooth. For \(x\notin F\), choose a nearest \(a\in F\). Every active \(a_Q\) lies within \(C_n d(x)\) of \(x\), and \(|a-a_Q|\le C'_n d(x)\). Subtract \(P_a\) before differentiating. The identity \(\sum\psi_Q=1\) gives

\[
\partial^\gamma v(x)-\partial^\gamma P_a(x)
=\sum_Q\sum_{\beta\le\gamma}\binom\gamma\beta
(\partial^\beta\psi_Q)(x)
\partial^{\gamma-\beta}(P_{a_Q}-P_a)(x).
\tag{3.6}
\]

The differentiated partition costs \(d^{-|\beta|}\), while (3.3) supplies \(d^{k-|\gamma|+|\beta|}\). The overlap is bounded. Hence, through order \(k\),

\[
|\partial^\gamma v(x)-\partial^\gamma P_a(x)|
\le C_{n,k}\omega(C_n d(x))d(x)^{k-|\gamma|}.
\tag{3.7}
\]

Each off-set derivative has a continuous trace \(f_\gamma\) on \(F\). For precision, fix \(b\in F\), write \(r=|x-b|\), and observe that \(d(x)\le r\) and \(|a-b|\le2r\). Combining (3.7) with (3.2) for \(P_a-P_b\) gives

\[
\partial^\gamma v(x)-\partial^\gamma P_b(x)
=o(r^{k-|\gamma|})\quad(x\notin F,\ x\to b).
\tag{3.8}
\]

The little-oh is uniform in \(b\), by (1.3). If \(x\in F\), define \(v_\gamma(x)=f_\gamma(x)\), and define \(v_\gamma=\partial^\gamma v\) off \(F\). Formula (1.2) gives the same estimate (3.8) for \(v_\gamma(x)\) on \(F\). In particular every \(v_\gamma\) is continuous globally.

These continuous functions are the actual derivatives of \(v\). For \(|\gamma|<k\), Taylor expansion of \(\partial^\gamma P_b\) at \(b\), with (3.8) on both parts of the domain, gives

\[
v_\gamma(b+h)
=f_\gamma(b)+
\sum_{j=1}^n f_{\gamma+e_j}(b)h_j+o(|h|).
\tag{3.9}
\]

Terms of polynomial degree at least two are \(O(|h|^2)\); when no such terms exist there is nothing to discard. Thus \(v_\gamma\) is differentiable at every \(b\in F\) and has gradient given by the next traces. Off \(F\) this derivative identity already holds. Starting with \(v_0=v\) and using (3.9) successively proves \(v\in C^k\) and \(\partial^\gamma v=v_\gamma\). For \(k=0\), the continuity part alone proves the assertion.

It remains to make the extension compact and bounded. Choose a nonnegative integral-one mollifier supported in the ball of radius \(1/4\), and convolve it with the indicator of the open one-neighborhood of \(F\). The resulting smooth function \(\zeta\) equals one on the \(3/4\)-neighborhood of \(F\), vanishes outside its closed \(5/4\)-neighborhood, and has derivative bounds depending only on dimension and derivative degree. Put \(Ef=\zeta v\). Its traces on \(F\) are unchanged and its support lies in that fixed compact neighborhood.

On this support, \(d(x)\le5/4\). Equations (3.6)–(3.7), with \(\omega\le\|f\|_{W^k(F)}\), bound every derivative of \(v\) through order \(k\) by that norm times a constant depending only on \(n,k\). The polynomial term is bounded too: \(|x-a|=d(x)\le5/4\), and its coefficients are the bounded jet values at \(a\). The product rule with the fixed derivative bounds of \(\zeta\) proves (3.4). On \(F\) the same bound follows from the prescribed traces. The partition, its selected points and \(\zeta\) are fixed independently of \(f\), so (3.5) and multiplication by \(\zeta\) define a linear map. \(\square\)

The construction does not presume that \(F\) is a manifold or that its complement has regular boundary. The gaps may have many different scales. It is their distance from \(F\), together with Taylor compatibility, that controls the derivatives of the extension.

## What a distribution on the closed set can measure

**Corollary 4.1 (the full jet norm on a support).** Let \(u\) be a compactly supported distribution of order at most \(k\), with support contained in \(F\). For every \(C^k\) function \(\phi\),

\[
|u(\phi)|\le C_u
\left(
\sum_{|\alpha|\le k}\sup_F|\partial^\alpha\phi|
+\sum_{|\alpha|\le k}
\sup_{\substack{a,b\in F\\a\ne b}}
\frac{|\partial^\alpha\phi(a)-
\sum_{|\beta|\le k-|\alpha|}
\partial^{\alpha+\beta}\phi(b)(a-b)^\beta/\beta!|}
{|a-b|^{k-|\alpha|}}
\right).
\tag{4.1}
\]

**Proof.** The restrictions of \(\phi\) form a compatible jet \(f\). Extend it by Theorem 3.1. All derivatives of \(\phi-Ef\) through order \(k\) vanish on \(F\), hence on \(\operatorname{supp}u\). The flat-jet theorem in the jet lesson proves \(u(\phi)=u(Ef)\). The distribution's order estimate and (3.4) bound this by \(C_u\|f\|_{W^k(F)}\), which is exactly (4.1). Arbitrary noncompact \(C^k\) functions are legitimate tests for the compact distribution by the pairing already proved in that lesson. \(\square\)

The second sum cannot always be omitted. Here is an explicit first-order example. On the line, for \(j\ge2\), let

\[
a_j=2^{-j},\qquad b_j=a_j+2^{-3j},\qquad
F=\{0\}\cup\{a_j,b_j:j\ge2\}.
\]

This is compact, and every nonzero point is isolated. Define

\[
u(\phi)=\sum_{j\ge2}2^{-j}
\frac{\phi(b_j)-\phi(a_j)}{b_j-a_j}.
\tag{4.2}
\]

The mean value integral bounds the absolute value of the \(j\)-th term by \(2^{-j}\sup_{[0,1/2]}|\phi'|\). Thus the series converges and defines a compact distribution of order at most one, with support exactly \(F\). To see equality of supports, a test confined near one isolated point detects its nonzero coefficient. Every neighborhood of zero contains such a point, so zero lies in the support too.

For a fixed \(j\), choose a smooth bump \(\phi_j\), with \(0\le\phi_j\le1\), equal to one near \(b_j\), and supported in a tiny interval containing no other point of \(F\). Then every positive-order derivative of \(\phi_j\) vanishes on \(F\), its value is one at \(b_j\) and zero at all other points, and

\[
u(\phi_j)=\frac{2^{-j}}{2^{-3j}}=2^{2j}.
\tag{4.3}
\]

The jet-value sum through order one on \(F\) is only one. No constant can bound all these pairings by that sum. Also \(\|\phi_j\|_\infty\le1\), so \(u\) has exact order one rather than zero. The normalized remainder between \(a_j\) and \(b_j\) has size \(2^{3j}\), which is precisely the information absent from the jet-value sum. The series (4.2) converges as a series of paired differences; splitting it into two divergent atomic sums would lose this cancellation.

## Exercises

**Exercise 1 (basic: the order-zero condition).** Show that \(W^0(F)\) consists of all continuous functions on \(F\). Prove that its norm is equivalent to the supremum norm, and explain how Theorem 3.1 supplies a bounded linear compactly supported continuous extension.

**Exercise 2 (intermediate: reproducing a polynomial).** On the interval \(F=[-1,1]\), prescribe \(f_0(a)=a^2\), \(f_1(a)=2a\), \(f_2(a)=2\). Verify compatibility for \(k=2\), compute the normalized remainders, and determine the extension before the final cutoff in (3.5). What remains true after that cutoff?

**Exercise 3 (intermediate: incompatible assignments).** On \(F=\{0\}\cup\{2^{-j}:j\ge1\}\), prescribe \(f_0(a)=a\) and \(f_1(a)=0\). Show that both assigned functions are continuous on \(F\), but that the jet is not compatible for \(k=1\). Prove directly that no \(C^1\) extension could have those traces.

**Exercise 4 (advanced: finite and infinite closed supports).** Prove that, on a fixed finite set \(F\), the norm (1.4) is bounded by a constant times the first jet-value sum alone. Deduce the corresponding bound for every order-at-most-\(k\) distribution supported in \(F\). Compare this with (4.2) and identify the geometric quantity that ceases to be bounded uniformly.

**Exercise 5 (advanced: completeness and a projection).** Prove that \(W^k(F)\) is complete for (1.4). Let \(C_b^k(\mathbb R^n)\) denote the functions with bounded continuous derivatives through order \(k\), with their global derivative supremum norm. Show that jet restriction \(R:C_b^k\to W^k(F)\) is bounded, and that \(ER\) is a bounded projection on \(C_b^k\), whose kernel consists exactly of functions with all these jets zero on \(F\).

## Solutions

**Solution 1.** There is only \(f_0\), and \(R_0(a,b)=f_0(a)-f_0(b)\), with diagonal value zero. A continuous function on compact \(F\) is uniformly continuous, so the compatibility condition holds. Conversely membership already requires continuity of the component. The remainder supremum is at most \(2\sup_F|f_0|\), so

\[
\sup_F|f_0|\le\|f\|_{W^0(F)}
\le3\sup_F|f_0|.
\]

The theorem with \(k=0\) gives a continuous compactly supported extension, linear in the assigned values, with supremum controlled by this norm. This is a statement about continuous extension; differentiability is not asserted at order zero.

**Solution 2.** At every \(a\in[-1,1]\), the polynomial \(P_a(x)=a^2+2a(x-a)+(x-a)^2\) equals \(x^2\). Thus every difference of Taylor polynomials is zero and all normalized remainders vanish. The jet is compatible. The partition sum off \(F\) gives \(v(x)=x^2\sum_Q\psi_Q(x)=x^2\), and it has that same value on \(F\). After the final cutoff the extension is \(\zeta(x)x^2\); it still equals the polynomial throughout the neighborhood where \(\zeta=1\), including all its prescribed jets on \(F\), but it is now compactly supported.

**Solution 3.** Both components are continuous on this set, including at zero. However \(P_0(x)=0\), so

\[
R_0(2^{-j},0)=
\frac{2^{-j}}{2^{-j}}=1.
\]

It does not tend to the diagonal value zero. If a \(C^1\) extension \(g\) existed, it would satisfy \(g(0)=0\), \(g'(0)=0\) and \(g(2^{-j})=2^{-j}\). Its difference quotients at zero along this sequence would equal one, contradicting \(g'(0)=0\). Continuity of separately assigned derivatives is therefore weaker than Taylor compatibility.

**Solution 4.** For a singleton, the remainder sum is zero. Otherwise let \(\delta=\min_{a\ne b\in F}|a-b|>0\) and \(D=\max_{a,b\in F}|a-b|\). Every numerator in (1.2) is bounded by a fixed finite sum of jet suprema times powers of \(D\); every denominator is at least the corresponding power of \(\delta\). There are finitely many multi-indices, so \(\|f\|_{W^k(F)}\le C_{F,k}\sum_{|\alpha|\le k}\sup_F|f_\alpha|\). The compatibility condition is automatic because off-diagonal pairs do not approach the diagonal. Corollary 4.1 gives the claimed distribution bound. In the infinite example there is no positive minimum separation: \(b_j-a_j=2^{-3j}\to0\). Its tests have uniformly bounded jet values on \(F\), yet the remainders divided by that separation grow. Finite-set constants cannot be carried over uniformly to those pairs.

**Solution 5.** Let \(f^{(j)}\) be Cauchy in (1.4). Each component \(f_\alpha^{(j)}\) converges uniformly on \(F\) to a continuous \(f_\alpha\). Each remainder \(R_\alpha^{(j)}\) converges uniformly on \(F\times F\) to a continuous function \(A_\alpha\), zero on the diagonal. For \(a\ne b\), pass to the limit in the finite expression (1.2). It gives \(A_\alpha(a,b)=R_\alpha(a,b)\) for the limiting jet. Thus that jet is compatible, and all its component and remainder differences tend to zero in supremum norm. This is completeness.

Taylor's formula on the whole line segment from \(b\) to \(a\) bounds (1.2), for a restricted \(g\in C_b^k\), by a constant times the global suprema of its derivatives through order \(k\). For top derivatives the bound is twice their supremum. Compatibility follows from uniform continuity on a compact neighborhood of \(F\), as in the necessity argument. Hence \(\|Rg\|_{W^k(F)}\le C_{n,k}\|g\|_{C^k}\). Theorem 3.1 makes \(E\) bounded into \(C_b^k\), and \(RE\) is the identity on \(W^k(F)\). Consequently

\[
(ER)^2=E(RE)R=ER.
\]

If \(Rg=0\), then \(ERg=0\). If \(ERg=0\), apply \(R\) and use \(RE=\mathrm{id}\) to obtain \(Rg=0\). This identifies the kernel and proves the projection assertion. Completeness and the projection are consequences of the full remainder norm; they do not justify replacing that norm by pointwise jet values on an arbitrary closed set.

## References

- [Whitney 1934] Hassler Whitney, *Analytic extensions of differentiable functions defined in closed sets*, Transactions of the American Mathematical Society 36 (1934), 63–89. [Full text](https://www.ams.org/journals/tran/1934-036-01/S0002-9947-1934-1501735-3/S0002-9947-1934-1501735-3.pdf).
- [Kolář–Michor–Slovák 1993] Ivan Kolář, Peter W. Michor and Jan Slovák, *Natural Operations in Differential Geometry*, Springer-Verlag, 1993. [Open electronic edition](https://www.mat.univie.ac.at/~michor/kmsbookh.pdf).
- [Dyatlov 2026] Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, MIT, 2026. [Open notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf).
