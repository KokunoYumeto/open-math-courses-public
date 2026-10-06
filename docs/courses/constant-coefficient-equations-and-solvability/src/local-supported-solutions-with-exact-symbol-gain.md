# Local supported solutions with the exact symbol gain

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A restriction estimate becomes an existence theorem by extending a functional on the range of the transposed equation. Reflection keeps the nonsymmetric Fourier weight in its original orientation. For every exponent above one, finite-exponent Lebesgue duality identifies the solution. At the remaining endpoint, a compact spatial cutoff converts the frequency functional into a smooth function and bounded phase tests prove the required integrability. The solution can therefore be chosen compactly supported, which also permits normalization of the root height by an exponential multiplier.

Read [Weighted control on the negative half-space](weighted-control-on-the-negative-half-space.md), [Lebesgue duality and the functionals on Fourier spaces](lebesgue-duality-and-fourier-functionals.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz Fourier inversion; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies finite coordinates, scalar calculus and compact cutoffs; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the norm, extension and integration estimates.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs use the linked prerequisite lessons and any stated planned theorem.

## The theorem and the conventions

Write \(y=(x,t)\in\mathbb R^{d}\times\mathbb R\), \(n=d+1\), and put \(H=\{t\ge0\}\). The case \(d=0\) is included. Let \(P\ne0\) be a polynomial. Assume that there are \(A_1>0\) and \(A_2\in\mathbb R\) such that every analytic normal root on a complex ball of radius \(A_1\) with real center satisfies
\[
\begin{gathered}
P(z,\tau(z))=0
       \\
\quad\Longrightarrow\\
\quad
       \sup\operatorname{Im}\tau\ge A_2.
\end{gathered}
\tag{1}
\]
For \(d=0\), this means that every normal root has imaginary part at least \(A_2\). If \(P\) has no normal roots, the condition is empty.

**Theorem.** Let \(X\subset\mathbb R^n\) be a bounded open set, \(1\le p\le\infty\), and \(k\) a positive moderate weight. For every \(f\in B_{p,k}(\mathbb R^n)\) with \(\operatorname{supp}f\subset H\), there is a compactly supported
\[
\begin{gathered}
u\in B_{p,kS_P}(\mathbb R^n),\\
\qquad
 \operatorname{supp}u\subset H,\\
\qquad
                   P(D)u=f\ \text{in }X.
\end{gathered}
\tag{2}
\]
The construction gives \[
\begin{gathered}
\|u\|_{p,kS_P}\\
\le C_{X,P,k,p}\|f\|_{p,k}
\end{gathered}
\]

No linear choice of \(u\), uniqueness, global equation, or support inside \(X\) is asserted. For \(X=\varnothing\), take \(u=0\).

Use \(D_j=-i\partial_{y_j}\), complex-linear distribution pairings, and
\[
\begin{gathered}
\widehat v(\xi)=\int e^{-iy\cdot\xi}v(y)\,dy,\\
\qquad
 \|v\|_{p,k}=(2\pi)^{-n/p}\|k\widehat v\|_p.
\end{gathered}
\tag{3}
\]
For a distribution \(T\), define its reflection by \(\check T(v)=T(\check v)\), \(\check v(y)=v(-y)\). Then \(\check{P(D)T}=P(-D)\check T\). In a distribution pairing, the transpose of \(P(-D)\) is \(P(D)\), without conjugating its coefficients.

## Flat tests and restriction norms

Let \(\|v\|^-_{q,\rho}\) be the infimum of the full \(B_{q,\rho}\) norms of all Schwartz functions agreeing with \(v\) on \(t<0\). A distribution supported in \(\{t\le0\}\) annihilates every Schwartz function vanishing on \(t<0\).

Here are the details at the boundary. For a compactly supported such function \(w\), every derivative vanishes at \(t=0\). Taylor's formula in \(t\), with arbitrarily high order and uniform bounds on its compact support, gives
\[
\begin{gathered}
\sup_{0\le t\le2\varepsilon}
       |\partial^\alpha w(x,t)|\le C_{\alpha,M}\varepsilon^M
                 \\
\quad\text{for every }\alpha,M.
\end{gathered}
\tag{4}
\]
Choose a fixed smooth \(\sigma\) which is zero for \(s\le1\) and one for \(s\ge2\). The compactly supported functions \(w_\varepsilon(y)=\sigma(t/\varepsilon)w(y)\) have support in \(t\ge\varepsilon\), and converge to \(w\) with every derivative on one fixed compact set. Indeed each derivative of their difference is a sum of terms bounded by a fixed power of \(\varepsilon^{-1}\) times(4); choose \(M\) larger than that power. A distribution supported in \(t\le0\) kills each \(w_\varepsilon\), and therefore kills \(w\). For a general Schwartz \(w\), first multiply by dilated compact cutoffs. They converge in Schwartz space, still vanish for \(t<0\), and the preceding argument applies to each. Tempered continuity passes to the limit. This proves the assertion for the tests actually used here.

## Removing the root-height normalization

First multiply \(f\) by \(\chi_f\in C_c^\infty\) equal to one near \(\overline X\), obtaining \(f_c=\chi_f f\). The cutoff theorem preserves \(B_{p,k}\), its norm is bounded by a fixed constant times that of \(f\), its support is compact in \(H\), and \(f_c=f\) on \(X\).

Set
\[
\begin{gathered}
A=\max(1,A_1),\\
\qquad
 \beta=\max(0,A+1-A_2),\\
\qquad
                    Q(z,s)=P(z,s-i\beta).
\end{gathered}
\tag{5}
\]
Every root of \(Q\) on a radius-\(A\) real-centered ball is a root of \(P\) plus \(i\beta\). Restrict the latter to the concentric radius-\(A_1\) ball and apply(1). Thus its \(Q\)-root has supremum of its imaginary part at least \(A_2+\beta\ge A+1\). This is precisely the normalized [Weighted control on the negative half-space](weighted-control-on-the-negative-half-space.md) hypothesis. The same argument for \(d=0\) just shifts each root.

The finite polynomial jet identity at a complex shift, applied in both directions, gives
\[
\begin{gathered}
C_\beta^{-1}S_P(\xi)\le S_Q(\xi)\le C_\beta S_P(\xi)
                       \\
\qquad(\xi\in\mathbb R^n).
\end{gathered}
\tag{6}
\]
For clarity, \(S_Q(\xi)=S_P(\xi-i\beta e_t)\). The finite commuting jet matrices have the same polynomial bounds for complex shifts as for real ones; apply them with shifts \(\pm i\beta e_t\). No comparison of \(P\) itself at a single point is used.

Define \(f_Q=e^{-\beta t}f_c\). On the compact support of \(f_c\), the exponential is equal to a fixed compactly supported smooth multiplier, so \(f_Q\in B_{p,k}\) with a fixed norm bound and the same half-space support. The differentiation identity is
\[
\begin{gathered}
Q(D)(e^{-\beta t}v)=e^{-\beta t}P(D)v,\\
\qquad
 P(D)(e^{\beta t}w)=e^{\beta t}Q(D)w.
\end{gathered}
\tag{7}
\]
It holds for distributions by the product rule. If the normalized theorem produces compactly supported \(w\in B_{p,kS_Q}\) solving \(Q(D)w=f_Q\) in \(X\), then \(u=e^{\beta t}w\) solves the original equation there. In the construction below, \(w\)'s support is in one fixed compact cutoff set; on that set the latter exponential too is a compact smooth multiplier. Its weighted norm is bounded, and(6) converts \(kS_Q\) to \(kS_P\). Thus it suffices to prove the normalized result for compact data. A global exponential multiplier on a weighted space is not assumed.

## The functional on the range of the equation

From now on \(P\) satisfies the normalized root condition, \(f\) has compact support in \(H\), and \(K=kS_P\). Write \(q=p'\), with both endpoint conventions. Reflection gives the exact bilinear formula and Hölder estimate
\[
\begin{gathered}
\check f(v)=(2\pi)^{-n}\int
                    \widehat f(\xi)\widehat v(\xi)\,d\xi,
 \\
\qquad
 |\check f(v)|\le\|f\|_{p,k}\|v\|_{q,1/k}.
\end{gathered}
\tag{8}
\]
The two norm factors multiply to the displayed inverse-transform factor. In particular no assumption \(k(\xi)=k(-\xi)\) is needed. Because \(\check f\) is supported in \(t\le0\), the flat-test argument permits the infimum over every extension of the negative-time restriction:
\[
                  |\check f(v)|\le
                      \|f\|_{p,k}\|v\|^-_{q,1/k}.
 \tag{9}
\]
All tests \(v\in C_c^\infty(-X)\) have a common spatial bound \(L_X\). Apply the [Weighted control on the negative half-space](weighted-control-on-the-negative-half-space.md) estimate with weight \(1/k\). It gives
\[
\begin{gathered}
|\check f(v)|\le C_0\|P(D)v\|^-_{q,1/K},
 \\
\qquad C_0=C_{X,P,k,p}\|f\|_{p,k}.
\end{gathered}
\tag{10}
\]
For \(d=0\), use the direct zero-dimensional case of that estimate.

The assignment \(P(D)v\mapsto\check f(v)\) on \(P(D)C_c^\infty(-X)\) is well-defined: if two range tests coincide, apply(10) to their difference. The seminorm Hahn–Banach theorem extends it to a complex-linear functional \(U\) on the entire Schwartz space with
\[
\begin{gathered}
U(P(D)v)=\check f(v),\\|U(w)|\le C_0\|w\|^-_{q,1/K}
                     \\
\le C_0\|w\|_{q,1/K}.
\end{gathered}
\tag{11}
\]
The last norm is continuous for Schwartz seminorms, by the weighted-space theorem. Thus \(U\) is tempered. Every compact test supported in \(t>0\) has zero restriction seminorm, so \(U\) has support in \(t\le0\). Set \(u_0=\check U\); it has support in \(H\).

On \(v\in C_c^\infty(-X)\), the reflected equation is
\[
 (P(-D)U)(v)=U(P(D)v)=\check f(v).
 \tag{12}
\]
Reflection therefore gives \(P(D)u_0=f\) on \(X\). This fixes both the transpose and the half-space orientation. It remains to prove the appropriate weighted regularity after a fixed physical cutoff.

## Every exponent above one, including infinity

Suppose \(p>1\), so \(1\le q<\infty\). Define a frequency functional on Schwartz functions by \(F(g)=U(\mathcal F^{-1}g)\). From(11),
\[
 |F(g)|\le C_0(2\pi)^{-n/q}\|g/K\|_q.
 \tag{13}
\]
The functions \(g/K\), \(g\in\mathcal S\), form a vector subspace of \(L^q\). Define a functional on that subspace by \(g/K\mapsto F(g)\). Positivity of \(K\) makes the assignment unambiguous, and(13) bounds it. Norm Hahn–Banach extends it to \(L^q\). The actual finite-exponent duality theorem supplies a bilinear density \(a\in L^p\), including \(a\in L^\infty\) when \(q=1\), such that
\[
\begin{gathered}
F(g)=\int a(\xi)g(\xi)/K(\xi)\,d\xi,\\
\qquad
                   \|a\|_p\le C_0(2\pi)^{-n/q}.
\end{gathered}
\tag{14}
\]
No density assertion for the subspace \(g/K\) is required. Since
\((\mathcal F\psi)(-y)=(2\pi)^n\mathcal F^{-1}\psi(y)\),
the distributional Fourier transform of the reflected solution satisfies
\[
\begin{gathered}
\widehat{u_0}(\psi)=(2\pi)^n F(\psi),\\
\qquad
 \widehat{u_0}=(2\pi)^n a/K,\\
\qquad
                         \|u_0\|_{p,K}\le C_0.
\end{gathered}
\tag{15}
\]
The last inequality follows by multiplying the factor in(14) by \((2\pi)^{n-n/p}\). They cancel because \(1/p+1/q=1\).

Choose once and for all \(\chi\in C_c^\infty(\mathbb R^n)\) equal to one near \(\overline X\). Multiplication is bounded on \(B_{p,K}\). Hence \(u=\chi u_0\) is compactly supported in \(H\), has the required norm bound, and retains its equation on \(X\).

## The integrable endpoint by cutoff and phase tests

Suppose \(p=1\), \(q=\infty\). We have only the frequency-functional estimate
\[
                   |F(g)|\le C_0\|g/K\|_\infty
                                      \qquad(g\in\mathcal S).
 \tag{16}
\]
We do not identify this functional with an integrable function. Use the same physical cutoff \(\chi\), and let \(u=\chi u_0\). Its compact support gives the smooth Fourier function
\[
\begin{gathered}
h(\xi)\\
=u_0(\chi(y)e^{-iy\cdot\xi})
             \\
=F\bigl(\eta\mapsto\widehat\chi(\xi-\eta)\bigr).
\end{gathered}
\tag{17}
\]
The second equality follows by reflecting the physical test:
\(\mathcal F(\check\chi(y)e^{iy\cdot\xi})(\eta)=\widehat\chi(\xi-\eta)\).
There is no additional \(2\pi\) factor in this equality. The map from \(\xi\) to the displayed Schwartz function is smooth in every Schwartz seminorm, so \(h\) is smooth. Equivalently, derivatives differentiate \(\chi e^{-iy\cdot\xi}\) in a fixed compact test space. This also proves polynomial growth using one finite-order distribution bound on that compact set. For a Schwartz test \(\psi(\xi)\), integration of the physical tests converges in that fixed compact test space, and continuity gives
\(\widehat u(\psi)=\int h(\xi)\psi(\xi)\,d\xi\).
Thus \(h\) is the distributional Fourier transform of \(u\).

Let \(K(\eta+\zeta)\le(1+C_K|\zeta|)^{N_K}K(\eta)\), and set
\[
\begin{gathered}
J_{\chi,K}\\
=\int_{\mathbb R^n}
       |\widehat\chi(\zeta)|(1+C_K|\zeta|)^{N_K}\,d\zeta<\infty.
\end{gathered}
\tag{18}
\]
For any \(b\in C_c^\infty(\mathbb R^n)\), \(|b|\le1\), the function
\(\psi_b(\eta)=\int b(\xi)K(\xi)\widehat\chi(\xi-\eta)\,d\xi\)
is Schwartz. Although \(K\) is only continuous, every derivative in \(\eta\) falls on the Schwartz kernel; the compact parameter support and bounded \(K\) there control every seminorm. The integral converges in Schwartz seminorms: continuity of \(bK\) and translated kernels on that compact parameter set gives Riemann-sum convergence, or the identical seminorm estimates give dominated convergence. Moderation now yields
\[
\begin{gathered}
\sup_\eta|\psi_b(\eta)|/K(\eta)\le J_{\chi,K},\\\left|\int b(\xi)K(\xi)h(\xi)\,d\xi\right|
                       \\
=|F(\psi_b)|\\
\le C_0J_{\chi,K}.
\end{gathered}
\tag{19}
\]
The integral equality is justified by this actual Schwartz integral and continuity of \(F\). This is a bound on compact smooth phase tests, not a representation of the whole \(L^\infty\) dual.

Choose \(\theta\in C_c^\infty\), \(0\le\theta\le1\), equal to one on the unit ball and nonincreasing on each ray as its radius increases. Such a cutoff follows by composing a one-variable smooth decreasing cutoff with \(|\xi|^2\). Let \(\theta_R(\xi)=\theta(\xi/R)\), \(R\ge1\); these increase pointwise to one. For \(\varepsilon>0\), the smooth compact test
\(b_{R,\varepsilon}=\theta_R\overline h/\sqrt{|h|^2+\varepsilon^2}\)
has modulus at most one. In(19) it gives a nonnegative real integral. Let \(\varepsilon\downarrow0\), then \(R\uparrow\infty\), by monotone convergence:
\[
\begin{gathered}
\int K(\xi)|h(\xi)|\,d\xi\le C_0J_{\chi,K},\\
\qquad
                \|u\|_{1,K}\le(2\pi)^{-n}C_0J_{\chi,K}.
\end{gathered}
\tag{20}
\]
The integrand before the first limit is
\(\theta_R K|h|^2/\sqrt{|h|^2+\varepsilon^2}\), so the monotonicity is explicit, including its zero values where \(h=0\). The same cutoff retains the local equation and the half-space support already proved. This completes the endpoint, the normalized theorem, and, by(5)–(7), the original theorem.

## A compact local fundamental solution

Take \(p=\infty\), \(k=1\), and \(f=\delta_0\). Its Fourier function is one and its weighted norm is one. For every bounded open \(X\), the theorem produces a compactly supported \(E\in B_{\infty,S_P}\) with support in \(H\) for which \(P(D)E-\delta_0\) vanishes in \(X\). This is the exact local object needed for an approximation argument. It is not yet a global supported fundamental solution.

## Exercises with complete solutions

**Exercise 1 (entry).** In one dimension take \(P(s)=s-i\), and reflect a supported distribution \(u_0\) to \(U=\check u_0\). Write the equation imposed on \(U\), its test pairing, and its support. Explain why complex conjugating the coefficient \(i\) gives the wrong transpose.

**Solution.** Reflection changes \(D_t\) to \(-D_t\) and leaves the scalar coefficient unchanged. Thus \(\check{P(D)u_0}=(-D_t-i)U=P(-D_t)U\). Its test pairing is \(U((D_t-i)v)\), because the transpose changes the derivative sign once more and retains the scalar. If \(\operatorname{supp}u_0\subset\{t\ge0\}\), then \(\operatorname{supp}U\subset\{t\le0\}\). The pairing is complex-linear, so conjugating \(i\) would replace the required operator by \(-D_t+i\), an equation with a different polynomial. In Fourier pairing, reflecting the data gives \((2\pi)^{-1}\int\widehat f(s)\widehat v(s)\,ds\); its weight is \(1/k(s)\) in the test norm, even when \(k\) is not even.

**Exercise 2 (intermediate).** Fix \(\xi_0\in\mathbb R^n\), and let \(F(g)=g(\xi_0)\). Show why(16) does not itself imply \(\widehat{u_0}\) is a function. Compute the effect of a compact physical cutoff, and verify its weighted \(L^1\) bound.

**Solution.** Point evaluation satisfies \(|F(g)|\le K(\xi_0)\|g/K\|_\infty\). Formula(15)'s distributional identity, which remains valid without a density, gives \(\widehat{u_0}=(2\pi)^n\delta_{\xi_0}\). The frequency point mass is not a measurable-function distribution: a locally integrable function supported at a single point is zero almost everywhere, whereas this distribution has nonzero evaluation on a test equal to one there. In physical space \(u_0(y)=e^{iy\cdot\xi_0}\). After multiplying by \(\chi\), its transform is \(h(\xi)=\widehat\chi(\xi-\xi_0)\). Moderation gives
\(\int K(\xi)|h(\xi)|\,d\xi\le K(\xi_0)J_{\chi,K}\).
This is exactly(20) with \(C_0=K(\xi_0)\). This model explains the cutoff mechanism; it is not claimed to have the half-space support of the theorem's particular functional.

**Exercise 3 (advanced).** Take \(P(s)=s+3i\), \(A=1\), and \(A_2=-3\). Normalize its root height, verify both differential identities, and compute the comparison of its derivative norm with the shifted polynomial.

**Solution.** Formula(5) gives \(\beta=5\) and \(Q(s)=P(s-5i)=s-2i\). The root moves from \(-3i\) to \(2i\), the required height \(A+1\). Directly,
\((D_t-2i)(e^{-5t}v)=e^{-5t}(D_t+3i)v\),
since \(D_te^{-5t}=5i e^{-5t}\). In the opposite direction,
\((D_t+3i)(e^{5t}w)=e^{5t}(D_t-2i)w\).
The full derivative norms on the real axis are \(S_P(s)=\sqrt{s^2+10}\) and \(S_Q(s)=\sqrt{s^2+5}\). Thus \(S_Q\le S_P\le\sqrt2 S_Q\). The final exponential preserves weighted membership because the constructed \(w\) has support in one fixed compact set and the exponential there can be replaced by a compact smooth multiplier. Multiplication by \(e^{5t}\) on an arbitrary global \(B_{p,k}\) element was not proved and is unnecessary.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
