# When a kernel is smooth

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026. Checked once by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Public domain (CC0).*

Smoothness of an operator's output on smooth inputs is a weak test. Differentiation passes that test. A more revealing question is what happens to point masses and their derivatives. If an operator sends every compactly supported distribution to a smooth function continuously, its entire kernel is smooth. This lesson proves both directions and explains the continuity behind the assertion.

The prerequisites are [Distributions as kernels of continuous operators](distributions-as-kernels.md), Taylor's formula with its remainder, the Arzelà–Ascoli theorem on compact sets, and smooth approximate identities. We use the bilinear distribution pairing and Euclidean Lebesgue measure. Basic references are [Dyatlov 2026], [Melrose 2016] and [Schwartz 1952].

## Compact distributions test all smooth functions

For an open \(V\subset\mathbb R^n\), put \(\mathcal E(V)=C^\infty(V)\), with seminorms
\[
p_{M,r}(f)=\max_{|\beta|\le r}\sup_{y\in M}|\partial^\beta f(y)|,
\qquad M\Subset V.
\]
An exhaustion by compact sets and the increasing derivative orders make this a Fréchet space. Its continuous dual is \(\mathcal E'(V)\). We give this dual its strong topology, whose seminorms are
\[
q_B(u)=\sup_{f\in B}|\langle u,f\rangle|
\]
for bounded \(B\subset\mathcal E(V)\). Boundedness means uniform bounds for each smooth seminorm, on each compact set; it does not require a common support for the functions in \(B\).

Every \(u\in\mathcal E'(V)\) has an estimate
\[
|\langle u,f\rangle|\le C p_{M,r}(f)
\tag{1.1}
\]
for some compact \(M\) and integer \(r\). Its restriction to test functions is therefore a distribution supported in \(M\). Conversely, a compactly supported distribution acts on arbitrary smooth functions by \(\langle u,f\rangle=\langle u,\chi f\rangle\), where \(\chi=1\) near its support and is compactly supported. This is independent of \(\chi\), since the difference vanishes near the support. A distribution estimate for \(\chi f\) gives (1.1), on a compact neighborhood of the support. Thus \(\mathcal E'(V)\) is precisely the space of compactly supported distributions.

The weak convergence used in this lesson is
\[
u_j\longrightarrow u\text{ weakly in }\mathcal E'(V)
\quad\Longleftrightarrow\quad
\langle u_j,f\rangle\longrightarrow\langle u,f\rangle
\text{ for every }f\in\mathcal E(V).
\tag{1.2}
\]
Testing against all smooth functions, rather than only compactly supported ones, matters. A point mass escaping to infinity converges to zero against every compact test, but need not converge against a smooth function growing at infinity.

## Uniform estimates for a convergent sequence

**Lemma 2.1 (weak convergence is strong convergence for sequences here).** If \(u_j\to u\) as in (1.2), then \(q_B(u_j-u)\to0\) for every bounded \(B\subset\mathcal E(V)\). Furthermore there exist \(C,M,r\), independent of \(j\), such that
\[
|\langle u_j-u,f\rangle|\le Cp_{M,r}(f)
\quad(f\in\mathcal E(V)).
\tag{2.1}
\]
The same uniform estimate holds for any pointwise bounded family of continuous functionals on \(\mathcal E(V)\).

**Proof.** Let \(v_j=u_j-u\). The sets
\[
A_N=\{f:\sup_j|\langle v_j,f\rangle|\le N\}
\]
are closed and cover \(\mathcal E(V)\), because each scalar sequence converges. Baire's theorem gives one set with nonempty interior. Subtracting two elements in a small neighborhood of an interior point gives \(\sup_j|\langle v_j,f\rangle|\le2N\) on a neighborhood of zero. That neighborhood contains a ball for one of the increasing smooth seminorms. Scaling, including the zero-seminorm case as in Lemma 2.1 of the preceding lesson, proves (2.1). The proof uses only pointwise boundedness, so it also proves the final assertion for an arbitrary family.

For bounded \(B\), Arzelà–Ascoli applied to derivatives through order \(r\) makes \(B\) totally bounded in \(p_{M,r}\). To justify this for any compact \(M\), cover it by finitely many closed coordinate boxes whose slightly larger boxes lie in \(V\). The uniform bounds for derivatives through order \(r+1\) on those larger boxes give equicontinuity of the derivatives through order \(r\). The finite collection of Arzelà–Ascoli conclusions gives a finite net on \(M\).

Choose \(f_1,\ldots,f_a\in B\) with every \(f\in B\) within \(\varepsilon\) of some \(f_i\) in \(p_{M,r}\). Then
\[
\sup_{f\in B}|\langle v_j,f\rangle|
\le\max_i|\langle v_j,f_i\rangle|+C\varepsilon.
\]
The maximum tends to zero. Then let \(\varepsilon\) tend to zero. This proves strong convergence. \(\square\)

The conclusion is about sequences in this particular dual. It does not identify the weak and strong topologies on all subsets or all nets.

**Lemma 2.2 (smooth tests approximate compact distributions strongly).** For each \(u\in\mathcal E'(V)\), there exist \(u_\varepsilon\in\mathcal D(V)\), all supported in one compact subset of \(V\), such that \(u_\varepsilon\to u\) in the strong topology of \(\mathcal E'(V)\).

**Proof.** Extend the compact distribution to \(\mathbb R^n\) using a cutoff supported in \(V\), and let \(\rho\in\mathcal D(\mathbb R^n)\) have integral one. Put \(\rho_\varepsilon(z)=\varepsilon^{-n}\rho(z/\varepsilon)\), and regularize by
\[
u_\varepsilon(x)=\langle u(y),\rho_\varepsilon(x-y)\rangle.
\]
Differentiating this test family proves that \(u_\varepsilon\) is smooth. Its support lies in \(\operatorname{supp}u+\varepsilon\operatorname{supp}\rho\), inside one compact subset of \(V\) for small \(\varepsilon\).

Let \(B\subset\mathcal E(V)\) be bounded and use (1.1) for \(u\). Testing the regularization against \(f\in B\) gives
\[
\langle u_\varepsilon-u,f\rangle
=\left\langle u,
y\longmapsto\int\rho(z)\big(f(y+\varepsilon z)-f(y)\big)\,dz
\right\rangle.
\]
The displayed function is needed only near \(\operatorname{supp}u\). Taylor's formula on a fixed compact neighborhood bounds its derivatives through order \(r\) by
\[
\varepsilon\Big(\int |z\rho(z)|\,dz\Big)
\sup_{f\in B}p_{M',r+1}(f).
\]
The last supremum is finite. The distribution estimate proves \(q_B(u_\varepsilon-u)=O(\varepsilon)\), so convergence is strong. The pairing identity follows by approximating the integral by Riemann sums in the finite derivative seminorm used by \(u\). Thus no unproved interchange with an arbitrary functional is needed. \(\square\)

## Point masses vary smoothly

For \(y\in V\), let \(\delta_y(f)=f(y)\). Spatial differentiation of a distribution and differentiation of its parameter have opposite signs:
\[
\partial_{y_k}\delta_y=-\partial_{t_k}\delta_y,
\tag{3.1}
\]
where \(t\) denotes the distribution's test variable. Indeed the left side applied to \(f\) is \(\partial_k f(y)\), while \(\partial_{t_k}\delta_y(f)=-\partial_kf(y)\).

**Lemma 3.1.** The map \(y\mapsto\delta_y\) has continuous derivatives of every order into the strong dual \(\mathcal E'(V)\). They are
\[
\partial_y^\beta\delta_y=(-1)^{|\beta|}\partial_t^\beta\delta_y.
\tag{3.2}
\]

**Proof.** On a compact parameter neighborhood \(M\Subset V\), Taylor's formula gives, for each bounded \(B\subset\mathcal E(V)\),
\[
q_B\left(\frac{\delta_{y+he_k}-\delta_y}{h}
+\partial_{t_k}\delta_y\right)
\le \frac{|h|}{2}\sup_{f\in B}p_{M,2}(f),
\]
whenever the segment stays in \(M\). This proves the first derivative in the strong topology. The same estimate applied to derivatives of \(f\) proves (3.2) inductively. Continuity of each derivative follows from the mean-value bound with one further derivative, uniformly on \(B\). \(\square\)

## The smoothing equivalence

Let \(T:\mathcal D(V)\to\mathcal D'(U)\) be weakly continuous, and let \(K\) be its kernel from the preceding lesson.

**Theorem 4.1 (smooth kernels and smoothing operators).** The following statements are equivalent:

1. \(K\) is represented by a function \(k\in C^\infty(U\times V)\).
2. \(T\) extends to a continuous linear map \(S:\mathcal E'_b(V)\to C^\infty(U)\), where the input has its strong dual topology.
3. \(T\) extends to a linear map \(S:\mathcal E'(V)\to C^\infty(U)\) carrying every sequence converging as in (1.2) to a sequence converging in every smooth seminorm on compact subsets of \(U\).

The extension is unique in either class, and is
\[
Su(x)=\langle u(y),k(x,y)\rangle.
\tag{4.1}
\]
Neither \(k\) nor its derivatives need be bounded on the whole product. There is no proper-support assumption in this theorem.

**Proof that a smooth kernel gives a continuous extension.** For a compact distribution \(u\), (1.1) and Taylor's formula for the smooth function \(k\) show that (4.1) is smooth and
\[
\partial_x^\alpha Su(x)
=\langle u(y),\partial_x^\alpha k(x,y)\rangle.
\tag{4.2}
\]
For example, the first difference quotient in \(x\) converges in the \(C^r\) seminorm in \(y\) on the compact set controlling \(u\); its pairing therefore converges. The same reasoning works at every order.

Fix \(L\Subset U\) and an integer \(a\). The family
\[
B_{L,a}=\{\partial_x^\alpha k(x,\cdot):x\in L,\ |\alpha|\le a\}
\]
is bounded in \(\mathcal E(V)\). For every \(M\Subset V\) and every \(r\), all mixed derivatives in question are bounded on \(L\times M\), by compactness. Formula (4.2) gives
\[
p_{L,a}(Su)\le q_{B_{L,a}}(u).
\tag{4.3}
\]
This proves strong-dual continuity. For a smooth compactly supported input, (4.1) is the integral against \(k\), so it agrees with \(T\) by kernel uniqueness. Lemma 2.1 shows that a weakly convergent input sequence is strongly convergent, proving statement 3 too.

**Proof that a continuous extension has a smooth kernel.** First assume statement 2 and set
\[
k(x,y)=(S\delta_y)(x).
\tag{4.4}
\]
Lemma 3.1 and continuity of \(S\) imply that \(y\mapsto S\delta_y\) has continuous derivatives of every order with values in \(C^\infty(U)\). Hence
\[
\partial_x^\alpha\partial_y^\beta k(x,y)
=(-1)^{|\beta|}
\big(\partial_x^\alpha S(\partial_t^\beta\delta_y)\big)(x).
\tag{4.5}
\]
These derivatives are jointly continuous. To check this, let \((x_j,y_j)\to(x,y)\) in one compact product neighborhood. The corresponding functions of \(x\) on the right of (4.5) converge uniformly on that neighborhood as \(y_j\to y\); evaluation at \(x_j\), followed by continuity of the limiting function, gives convergence of their values. Thus \(k\in C^\infty(U\times V)\).

If only statement 3 is assumed, the same argument still works. Every parameter difference quotient in Lemma 3.1 converges weakly as well as strongly. Applying \(S\) gives convergence in \(C^\infty(U)\). The parameter derivatives are continuous because a convergent sequence of parameters gives weak convergence of the corresponding derivatives of point masses. Sequential continuity suffices to establish continuity for this finite-dimensional parameter space. Induction gives (4.5) and the same joint smoothness.

It remains to identify this smooth function with the kernel of \(T\). For \(\phi\in\mathcal D(V)\), approximate the integral \(\int\phi(y)\delta_y\,dy\) by Riemann sums in a finite collection of rectangles covering its support. These sums converge to the regular distribution \(\phi\) strongly in \(\mathcal E'(V)\): on a bounded family of smooth functions the integrands \(\phi(y)f(y)\) have a uniform derivative bound on the fixed compact integration region, so the Riemann-sum errors tend to zero uniformly. They also converge weakly. Applying either type of \(S\) therefore gives
\[
S\phi=\int\phi(y)S\delta_y\,dy
=\int\phi(y)k(\cdot,y)\,dy
\quad\text{in }C^\infty(U).
\]
The last Riemann sums converge in each smooth output seminorm by smoothness on compact products. Thus the function kernel \(k\) gives the same test-input operator as \(K\); kernel uniqueness shows they agree as distributions.

Finally Lemma 2.2 approximates every compact distribution by smooth compactly supported inputs. Continuity, or the sequential property in statement 3, proves that the extension must be (4.1) and is unique. Since the smooth-kernel construction already satisfies (4.3), statement 3 also implies statement 2. \(\square\)

This proof explains why output smoothness on test inputs alone cannot establish the theorem: (4.4) needs the operator to act on point masses, and (4.5) needs controlled limits of their difference quotients.

## A smooth kernel can have no global size bound

Consider
\[
k(x,y)=e^{xy}+\sin(x+y^3)
\quad\text{on }\mathbb R^2.
\]
This function and its mixed derivatives are bounded on every compact product but have no useful uniform bound on the whole plane. The theorem still supplies a continuous map \(\mathcal E'_b(\mathbb R)\to C^\infty(\mathbb R)\). For instance,
\[
S\delta_a(x)=e^{ax}+\sin(x+a^3),
\]
and
\[
S\delta'_a(x)=-xe^{ax}-3a^2\cos(x+a^3).
\]
The minus sign is the sign of spatial distributional differentiation. Its input can have any fixed compact support; the output estimate uses a bounded family in \(C^\infty\), not a bound uniform over the whole plane.

The theorem's domain is compactly supported distributions. Extensions to arbitrary distributions require additional input-support control. For those geometric support conditions, see Detecting regularity without choosing coordinates. Smoothness and support control answer different questions.

## Exercises

**Exercise 1 (basic: a dipole under Gaussian smoothing).** For \(k(x,y)=e^{-(x-y)^2}\), compute \(S(2\delta_{-1}-\delta'_2)\). State a formula for \(S\partial_y^j\delta_a\), with the sign convention made explicit.

**Exercise 2 (intermediate: smoothing only to finite order).** Fix an integer \(r\ge0\). Let
\[
a(x)=|x|^{r+1/2},\qquad
Su(x)=a(x)\langle u,e^{-y^2}\rangle.
\]
Show that \(S:\mathcal E'_b(\mathbb R)\to C^r(\mathbb R)\) is continuous, but its kernel is not smooth. Explain the role of all derivative orders in Theorem 4.1.

**Exercise 3 (intermediate: smooth outputs on test inputs).** Show that the identity \(I:\mathcal D(\mathbb R)\to C^\infty(\mathbb R)\) is continuous, but has no extension of either type in Theorem 4.1. Prove this directly using an approximate identity converging to \(\delta_0\).

**Exercise 4 (advanced: extracting a kernel from moving point masses).** Suppose \(S\) is continuous as in statement 2 of Theorem 4.1. Derive a compact-set estimate for
\[
\frac{k(x,y+h)-k(x,y)}{h}-\partial_yk(x,y)
\]
that tends to zero uniformly in \(x\) on a fixed compact set, in the one-dimensional input case. Explain why differentiating \(S\delta_y\) is legitimate, while applying an arbitrary linear map to a difference quotient would not be.

**Exercise 5 (advanced: finite-rank approximation of a smoothing operator).** Let \(k_j\in C^\infty(U\times V)\) converge to \(k\) with all derivatives on compact products. Show that the corresponding maps \(S_j\) converge to \(S\), uniformly on each bounded subset of \(\mathcal E'_b(V)\), in every smooth output seminorm. Explain how locally cut-off Fourier expansions give a sequence of finite sums \(k_j(x,y)=\sum_{a=1}^{N_j}f_{j,a}(x)g_{j,a}(y)\) with this convergence.

## Solutions

**Solution 1.** Since \(\partial_yk(x,y)=2(x-y)e^{-(x-y)^2}\),
\[
S(2\delta_{-1}-\delta'_2)(x)
=2e^{-(x+1)^2}+2(x-2)e^{-(x-2)^2}.
\]
Generally the spatial derivative of the input point mass satisfies
\[
S(\partial_y^j\delta_a)(x)
=(-1)^j\partial_a^j e^{-(x-a)^2}.
\]
Here \(\partial_y^j\delta_a\) denotes distributional differentiation in its test variable; parameter differentiation in \(a\) would have the opposite sign at odd orders.

**Solution 2.** On either side of zero, a derivative of order \(j\le r\) is a constant times \(|x|^{r+1/2-j}\), with a possible sign factor. It tends to zero at zero. Inductively these derivatives extend continuously there, so \(a\in C^r\). The derivative of order \(r+1\) on a half-line is a nonzero constant times \(|x|^{-1/2}\), which cannot extend continuously. For a compact \(L\),
\[
\|Su\|_{C^r(L)}\le\|a\|_{C^r(L)}q_{\{e^{-y^2}\}}(u),
\]
proving continuity. The kernel is the function \(a(x)e^{-y^2}\), which is not \(C^{r+1}\) near \(x=0\). The smooth conclusion of Theorem 4.1 requires output estimates and parameter derivatives at every order, rather than at one prescribed finite order.

**Solution 3.** On every fixed test-support space, the inclusion into \(C^\infty\) is continuous, so the inductive-limit property gives continuity of \(I\). Choose a nonnegative bump \(\rho\) of integral one with \(\rho(0)>0\). Its rescalings \(\rho_\varepsilon(x)=\varepsilon^{-1}\rho(x/\varepsilon)\) converge strongly, and therefore weakly, to \(\delta_0\) in \(\mathcal E'\), by Lemma 2.2. An extension would make \(I\rho_\varepsilon=\rho_\varepsilon\) converge in \(C^\infty\). But their values at zero are \(\varepsilon^{-1}\rho(0)\), which diverge. Even uniform convergence near zero is impossible. The identity kernel is the distribution on the diagonal, rather than a smooth function.

**Solution 4.** Continuity of \(S\) for the output seminorm \(p_{L,0}\) gives finitely many bounded test families and constants controlling it. Combine those families, with the constants absorbed by scaling, into one bounded \(B\subset\mathcal E(V)\); then \(p_{L,0}(Sv)\le Cq_B(v)\). For \(y,y+h\) in a fixed compact interval \(M\Subset V\), Lemma 3.1 gives
\[
\sup_{x\in L}\left|
\frac{k(x,y+h)-k(x,y)}{h}-\partial_y k(x,y)
\right|
\le \frac{C|h|}{2}\sup_{f\in B}p_{M,2}(f).
\]
The right side is finite and tends to zero. Replacing the output seminorm by \(p_{L,a}\) proves the same result with every output derivative. The operation is legitimate because continuity of \(S\) transfers a proved strong-dual remainder estimate to a smooth-output remainder estimate. Algebraic linearity alone provides no such transfer of limits.

**Solution 5.** A bounded subset \(A\subset\mathcal E'_b(V)\) is pointwise bounded, since each singleton \(\{f\}\) is bounded in \(\mathcal E(V)\). The last assertion of Lemma 2.1 gives one \(C,M,r\) such that
\[
|\langle u,f\rangle|\le Cp_{M,r}(f)
\quad(u\in A).
\]
Consequently
\[
\sup_{u\in A}p_{L,a}((S_j-S)u)
\le C\max_{|\alpha|\le a,\ |\beta|\le r}
\sup_{L\times M}|\partial_x^\alpha\partial_y^\beta(k_j-k)|,
\]
which tends to zero.

For the finite-sum construction, exhaust \(U\) and \(V\) by compact sets with interiors, and choose compact cutoffs equal to one on the \(j\)-th sets. Split their product times \(k\) into finitely many pieces supported in product rectangles, using product partitions. Expand each piece periodically on a larger product rectangle and multiply the modes by separate cutoffs, as in Section 3 of the preceding lesson. Finite Fourier sums are finite sums of functions of \(x\) times functions of \(y\). Choose their truncation sufficiently large to approximate derivatives through order \(j\) on the \(j\)-th compact product within \(1/j\). Summing the finitely many pieces gives \(k_j\). On every fixed compact product, the outer cutoffs eventually equal one and the derivative errors tend to zero. Thus \(k_j\to k\) in \(C^\infty\) on compact products. Each corresponding operator has finite-dimensional range, spanned by its finitely many \(f_{j,a}\)'s. The estimate above proves the claimed operator convergence.

## References

- [Dyatlov 2026] Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, MIT, 2026. [Open notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf).
- [Melrose 2016] Richard Melrose, *18.155 Lecture 15: Schwartz's kernel theorem*, MIT, 2016. [Open lecture](https://math.mit.edu/~rbm/18.155-F16/L15.pdf).
- [Schwartz 1952] Laurent Schwartz, *Théorie des noyaux*, Proceedings of the International Congress of Mathematicians, Cambridge, Massachusetts, 1950, volume I, American Mathematical Society, 1952. [Proceedings archive](https://www.mathunion.org/icm/proceedings).
