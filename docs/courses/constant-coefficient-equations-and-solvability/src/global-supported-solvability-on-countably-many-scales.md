# Global supported solvability on countably many scales

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The local theorem gives supported solutions with compact data. The approximation theorem lets us modify successive solutions by homogeneous corrections, so their differences become summable on each compact set. A carefully chosen polytope supplies every support condition needed for that approximation. A one-sided approximate identity keeps the time support throughout the smoothing step.

Read [Local supported solutions with the exact symbol gain](local-supported-solutions-with-exact-symbol-gain.md), [Supported smooth approximation](supported-smooth-approximation.md), [Local regularity, sharp embeddings, and compactness](local-regularity-and-compactness.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz Fourier inversion; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies finite coordinates, scalar calculus and compact cutoffs; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the norm, extension and integration estimates. [Tensor products and smooth parameters](../prerequisites/tensor-products-and-parameters.html) and [Convolution as addition of supports](../prerequisites/convolution-as-addition-of-supports.html) supply parameter pairings and compact convolution.

The local distributional Holmgren theorem is proved in [Analytic coefficients and one-sided uniqueness](../AN02-L191.html#3-a-continuously-differentiable-surface-needs-no-analytic-flattening), Theorem 3.2: a distribution solving an analytic-coefficient equation and vanishing on one side of a noncharacteristic \(C^1\) surface vanishes near that surface. The uses of the Holmgren theorem draw on that complete proof.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs use the linked prerequisite lessons and any stated planned theorem.

## The global statement

Let \(P\ne0\) satisfy the analytic-root condition([equation 1 in Local supported solutions with the exact symbol gain](local-supported-solutions-with-exact-symbol-gain.md)), and write \(H=\{t\ge0\}\). Let \(k_j\) be moderate weights and \(1\le p_j<\infty\), \(j=1,2,\ldots\). Define
\[
\begin{gathered}
\mathcal F=\bigcap_{j\ge1}B^{\rm loc}_{p_j,k_j}(\mathbb R^n),
       \\
\qquad
 \mathcal G=\bigcap_{j\ge1}B^{\rm loc}_{p_j,k_jS_P}(\mathbb R^n).
\end{gathered}
\tag{1}
\]
These spaces have all their compact-cutoff seminorms.

**Theorem, using the available Holmgren theorem.** If \(f\in\mathcal F\) and \(\operatorname{supp}f\subset H\), then there is \(u\in\mathcal G\) with
\[
               P(D)u=f\text{ on }\mathbb R^n,\qquad
                            \operatorname{supp}u\subset H.
 \tag{2}
\]
No uniqueness or continuous linear choice is asserted. The exponent restriction concerns the smoothing argument below; no general infinity-endpoint approximation is assumed. For a nonzero constant \(P=c\), simply take \(u=f/c\). Since \(S_P=|c|\), all conclusions follow directly. We henceforth suppose \(m=\deg P\ge1\), and let \(p_m\) be its nonzero homogeneous principal part.

## A finite set of noncharacteristic perturbations

Take \(N=e_t\). There are \(n\) real vectors \(\xi^1,\ldots,\xi^n\) forming a basis, with
\[
\begin{gathered}
p_m(\xi^j)\ne0,\\
\qquad
                  N=\sum_{j=1}^n c_j\xi^j,\\
\quad c_j>0.
\end{gathered}
\tag{3}
\]
To construct them for \(n\ge2\), start with \(N+e_1,\ldots,N+e_{n-1}\) and \(N-\sum_{a<n}e_a\), whose sum is \(nN\). They are independent: in a zero linear combination, tangential coordinates make every coefficient equal to the last, and the normal coordinate then makes them all zero. The coefficients of \(N\) in this basis are \(1/n>0\). Invertibility and those positive coefficients persist under sufficiently small perturbations, by continuity of the inverse matrix.

A nonzero real-variable complex polynomial cannot vanish on an open box. Induction on the number of variables proves this: hold all but one variable fixed; a scalar polynomial vanishing on an interval has every coefficient zero, and then apply the induction to those coefficient polynomials. Applying this on an arbitrary open box proves that its zero set has empty interior. We can therefore perturb each starting vector slightly to make \(p_m(\xi^j)\ne0\), within the preceding common neighborhood. For \(n=1\), choose \(\xi^1=N\); \(p_m(N)\ne0\) and \(c_1=1\).

The nonnegative span of \(\xi^1,\ldots,\xi^n,-N\) is all of \(\mathbb R^n\). Indeed(3) gives
\[
 -\xi^j=c_j^{-1}
              \left(\sum_{\ell\ne j}c_\ell\xi^\ell-N\right);
 \tag{4}
\]
thus both signs of every basis vector belong to that span.

The scalar polynomial \(p_m(N+s\xi^j)\) is not identically zero: its coefficient of \(s^m\) is \(p_m(\xi^j)\ne0\). Its positive roots are finite. Choose \(\varepsilon>0\) sufficiently small that none has \(0<s\le\varepsilon\). Put \(N^j=N+\varepsilon\xi^j\). For every \(a>0,b\ge0\), homogeneity gives
\[
\begin{gathered}
p_m(aN^j+bN)
       \\
=(a+b)^m p_m\left(N+
                   \frac{a\varepsilon}{a+b}\xi^j\right)\ne0.
\end{gathered}
\tag{5}
\]
This permits \(p_m(N)=0\). The coefficient of \(N^j\) must be strictly positive.

## Compact-support continuation in a positive-time wedge

**Lemma.** Let \(\mu\in\mathcal E'(\mathbb R^n)\), and suppose \(P(-D)\mu=0\) in
\(W_j(a)=\{t>0,\ y\cdot N^j>a\}\).
Then \(\mu=0\) in \(W_j(a)\), using the available local Holmgren theorem.

**Proof.** If a support point \(y_0\) lies there, write \(\ell(y)=y\cdot N^j\), and take \(T\ge1\) above every positive time coordinate in the compact support. Choose \(\delta>0\) so small that
\[
\begin{gathered}
\ell(y_0)-a+\delta\log t_0>\delta\log T,
        \\
\qquad F(y)=\ell(y)-a+\delta\log t.
\end{gathered}
\tag{6}
\]
If \(t_0=T\), every positive \(\delta\) works; otherwise choose it below \((\ell(y_0)-a)/\log(T/t_0)\).

On \(S=\operatorname{supp}\mu\cap\{t>0,\ell\ge a\}\), the function \(F\) attains a maximum. To see this despite the missing time boundary, \(\ell\) is bounded on the compact support and \(\log t\to-\infty\) uniformly in that bound as \(t\downarrow0\). Choose \(0<t_{\min}<t_0\) so that \(F<F(y_0)-1\) at all support points with \(0<t<t_{\min}\). The set \(\operatorname{supp}\mu\cap\{t\ge t_{\min},\ell\ge a\}\) is compact and contains \(y_0\). Its maximum of \(F\) is therefore also the maximum on \(S\). That maximum exceeds \(\delta\log T\) by(6), whereas at \(\ell=a\) it is at most \(\delta\log T\). Hence a maximizing support point \(y_*\) has \(t_*>0,\ell(y_*)>a\).

Near \(y_*\), \(\mu\) is supported on the side \(F\le F(y_*)\), and solves the homogeneous equation. Its level surface has normal
\[
                   dF=N^j+\delta t_*^{-1}N.
 \tag{7}
\]
It is noncharacteristic by(5); the principal part of \(P(-D)\) differs from \(p_m\) only by the nonzero scalar \((-1)^m\). In particular \(dF\ne0\), so the local level surface is \(C^1\). The declared local Holmgren theorem makes \(\mu\) zero near \(y_*\), contradicting its being a support point. This proves the lemma. All uses of the logarithm occur at strictly positive time. \(\square\)

This is a compact-support adapter, not an asserted proof of all wedge continuation for arbitrary distributions.

## A support exhaustion satisfying the approximation condition

Define the bounded open polytope
\[
\begin{gathered}
X=\{y:\ y\cdot N^j<1\ \\
(j=1,\ldots,n),\ \\
t>-1\},
                     \\X_r=rX\\(r>0).
\end{gathered}
\tag{8}
\]
It contains a neighborhood of zero by its finitely many strict inequalities. It is bounded: for \(y\in X\), \(-t<1\) and
\(\xi^j\cdot y=\varepsilon^{-1}(N^j\cdot y-t)<2/\varepsilon\).
By(4), each of the two signs of every coordinate vector is a nonnegative combination of the \(\xi^j,-N\), so every coordinate of \(y\) is bounded both ways. The closure is the compact set described by the weak inequalities: each weak-inequality point is approached by its multiples \(\lambda y\), \(0<\lambda<1\), which satisfy every strict inequality. For \(0<r<s\), \(\overline{X_r}\subset X_s\), and the integer dilates exhaust \(\mathbb R^n\), since \(X\) contains a ball about zero.

If a compact distribution satisfies
\(H^\circ\cap\operatorname{supp}P(-D)\mu\subset\overline{X_a}\),
the preceding lemma on each \(W_j(a)\) gives
\[
               H^\circ\cap\operatorname{supp}\mu
                                            \subset\overline{X_a}.
 \tag{9}
\]
Indeed on that wedge the transposed equation vanishes, so the support has \(N^j\cdot y\le a\) at every positive-time point. The remaining weak inequality \(t\ge-a\) is automatic. Its positive-time support closure also lies in \(\overline{X_a}\), which is compact.

For any \(0<b<c\), the pair \(X_1=X_b,X_2=X_c\) satisfies the exact condition([equation 2 in Supported smooth approximation](supported-smooth-approximation.md)). If the closure \(K\) of the positive-time support of \(P(-D)\mu\) is compact inside \(X_b\), choose \(0<a<b\) with \(K\subset\overline{X_a}\). Such an \(a\) exists: all times on \(K\) are nonnegative, and each of its finitely many maxima of \(N^j\cdot y\) is strictly less than \(b\). For \(K=\varnothing\), choose \(a=b/2\). Equation(9) now puts the positive-time support closure of \(\mu\) in \(\overline{X_a}\subset X_b\), as required. The initial condition that its positive-time support lie in \(\overline{X_c}\) is retained in([equation 2 in Supported smooth approximation](supported-smooth-approximation.md)); our compact-support argument proves the needed conclusion even without it.

## One local solution on all the scales

Fix any bounded open \(Z\). Choose \(\eta\in C_c^\infty\) equal to one near \(\overline Z\), and set \(f_c=\eta f\). Its support is compact in \(H\). The local-space definition and cutoff multiplication give \(f_c\in B_{p_j,k_j}\) globally for every \(j\).

Choose a bounded open \(\Omega\) containing \(\overline Z-\operatorname{supp}\eta\). The [Local supported solutions with the exact symbol gain](local-supported-solutions-with-exact-symbol-gain.md) consequence supplies one compact \(E\in B_{\infty,S_P}\), supported in \(H\), such that \(r=P(D)E-\delta_0\) vanishes in \(\Omega\). Then
\[
\begin{gathered}
v=E*f_c\in\bigcap_j B_{p_j,k_jS_P}(\mathbb R^n),
 \\
\quad \operatorname{supp}v\subset H,\\
\quad
                 P(D)v=f_c+r*f_c=f\text{ on }Z.
\end{gathered}
\tag{10}
\]
The regularity follows simultaneously from
\(\|E*f_c\|_{p_j,k_jS_P}\le
\|E\|_{\infty,S_P}\|f_c\|_{p_j,k_j}\);
the compact factors and the weighted Fourier product theorem justify it. The error convolution vanishes on \(Z\) because a point of its support there would require \(x-y\in\operatorname{supp}r\) with \(x\in Z,y\in\operatorname{supp}f_c\subset\operatorname{supp}\eta\), contrary to the choice of \(\Omega\). Thus one kernel treats the whole countable family, with no intersection of separately chosen solutions. The resulting \(v\) is compactly supported.

## One-sided smoothing and a common topology

Choose a nonnegative \(\rho\in C_c^\infty(H^\circ\cap B(0,1))\) with integral one, and set \(\rho_\tau(y)=\tau^{-n}\rho(y/\tau)\). Such a function is obtained from a bump on a small ball with closure inside \(H^\circ\cap B(0,1)\), divided by its positive integral.

If \(h\) is compactly supported in \(H\) and belongs globally to every output space in(10), then \(h*\rho_\tau\) is smooth, compactly supported in \(H\), and
\[
\begin{gathered}
h*\rho_\tau\longrightarrow h
            \\
\quad\text{in every }B_{p_j,k_jS_P},\\
\quad \tau\downarrow0.
\end{gathered}
\tag{11}
\]
Its Fourier multiplier is \(\widehat\rho(\tau\xi)\), bounded in modulus by one and tending pointwise to one. Dominated convergence applies to each finite \(p_j\). A finite list can therefore be made small by one sufficiently small \(\tau\). If \(P(D)h=0\) on \(X_{r+2}\), then
\[
                  P(D)(h*\rho_\tau)=0\text{ on }X_{r+1}
 \tag{12}
\]
for all sufficiently small \(\tau\). Choose \(\tau\) below the positive distance from \(\overline{X_{r+1}}\) to the complement of \(X_{r+2}\). Every subtraction by a support point of \(\rho_\tau\) remains in the larger homogeneous region; convolution support and differentiation prove the assertion.

Choose \(\psi_m\in C_c^\infty(X_{m+1})\) equal to one near \(\overline{X_m}\). The countable seminorms
\[
\begin{gathered}
q_{m,j}(u)=\|\psi_m u\|_{p_j,k_jS_P},
                                  \\
\qquad m,j\ge1,
\end{gathered}
\tag{13}
\]
generate \(\mathcal G\)'s topology. For any other compact cutoff \(\chi\), some \(\psi_m\) is one near its support, and \(\chi u=\chi(\psi_m u)\); the global cutoff bound proves domination by \(q_{m,j}\). They separate distributions. The local-space completeness theorem and its countable-intersection argument show that \(\mathcal G\) is complete: each localized Banach limit gives a distributional limit on its interior, those limits agree on overlaps, and every cutoff norm converges to that common distribution. The same statement holds for \(\mathcal F\), and \(P(D):\mathcal G\to\mathcal F\) is continuous by the global differential norm bound after localization. For the last assertion, on any fixed cutoff support insert another cutoff equal to one near it before differentiating, so the global bound applies to that larger localized solution. This avoids a commutator estimate on an unlocalized distribution.

## Making the differences summable

Use(10) first with \(Z=X_3\), obtaining compact \(u_1\) supported in \(H\), belonging globally to every output scale and solving on \(X_3\). Inductively suppose \(u_r\) has these properties and solves on \(X_{r+2}\). Use(10) again to obtain compact \(v\) with all those memberships and solving on \(X_{r+3}\). The difference \(h=v-u_r\) is homogeneous on \(X_{r+2}\).

Choose \(\tau>0\) small enough that \(g=h*\rho_\tau\) is homogeneous on \(X_{r+1}\) and, by(11) and cutoff boundedness,
\[
                         q_{m,j}(h-g)<2^{-r-1}
                                      \quad(m,j\le r).
 \tag{14}
\]
The smooth \(g\) is supported in \(H\). Apply [Supported smooth approximation](supported-smooth-approximation.md) approximation to \(X_{r+1}\subset X_{r+4}\), whose support condition was proved above. Its finite weighted-seminorm consequence provides \(w\in C^\infty(X_{r+4})\), homogeneous there and supported in \(H\) relative to that region, with
\[
\begin{gathered}
\|\psi_m(g-w)\|_{p_j,k_jS_P}<2^{-r-1}
                                      \\
\quad(m,j\le r).
\end{gathered}
\tag{15}
\]
Every \(\psi_m\) here is compactly supported in \(X_{r+1}\), including \(m=r\). Thus these are legitimate seminorms of the approximated smaller-domain solution.

Take \(\theta_r\in C_c^\infty(X_{r+4})\) equal to one near \(\overline{X_{r+3}}\), and extend \(\theta_rw\) by zero. This is a global smooth compact function supported in \(H\), hence belongs to every output space. Define \(u_{r+1}=v-\theta_rw\). It solves on \(X_{r+3}\), since the multiplier is identically one there and \(w\) is homogeneous. On every \(\operatorname{supp}\psi_m\), \(m\le r\), it also equals one. Therefore(14)–(15) give
\[
                q_{m,j}(u_{r+1}-u_r)<2^{-r}
                                      \quad(m,j\le r).
 \tag{16}
\]
The resulting \(u_{r+1}\) is compactly supported in \(H\) and belongs globally to all the output scales. The induction continues, with its equation holding on an increasing region at every step.

For fixed \(m,j\), the tail is Cauchy because for \(b>a\ge\max(m,j)\),
\[
 q_{m,j}(u_b-u_a)\le\sum_{r=a}^{b-1}2^{-r}
                                         \le2^{1-a}.
 \tag{17}
\]
Completeness gives \(u\in\mathcal G\). The continuous embedding into distributions preserves support in \(H\), since every approximant vanishes on every negative-time test. Every compact test lies in \(X_{r+2}\) for all sufficiently large \(r\), where \(P(D)u_r=f\). Distributional differentiation and the limit therefore give(2) globally. This proves the countable-scale theorem.

The homogeneous approximation is defined two buffers beyond the old equation region, and its cutoff is one on the new equation region. This preserves the new equation while controlling a finite list on the smaller region. No equations are asserted across the transition region of a correction cutoff.

## Finite-order data and a global fundamental solution

A distribution has finite order \(M\) here if the derivative order in its compact-test bound can always be chosen as the same integer \(M\), while the constant may depend on the compact set. If \(f\) has finite order \(M\), then for every compact cutoff \(\eta\),
\[
\begin{gathered}
|\widehat{\eta f}(\xi)|\le C_\eta\langle\xi\rangle^M,\\
\qquad
 f\in B^{\rm loc}_{2,\langle\xi\rangle^{-r}},
                          \\
\quad r=M+n+1.
\end{gathered}
\tag{18}
\]
The first bound follows by testing \(f\) on \(\eta(y)e^{-iy\cdot\xi}\) and differentiating through order \(M\). In the second, the weighted Fourier square is bounded by a constant times \(\langle\xi\rangle^{-2n-2}\), which is integrable. Apply the theorem to this single scale. Since \(S_P\) has a positive constant lower bound from a nonzero highest derivative, the resulting \(u\) also belongs to \(B^{\rm loc}_{2,\langle\xi\rangle^{-r}}\).

This solution has finite order. Choose any integer \(a\) with \(2a>r+n/2\). For a test \(\phi\) supported in a fixed compact \(K\), insert a cutoff \(\chi\) equal to one near \(K\). Bilinear Fourier pairing, Hölder and the same \((1-\Delta)^a\) integration by parts as in([equation 12 in Supported smooth approximation](supported-smooth-approximation.md)) give
\[
\begin{gathered}
|u(\phi)|\le (2\pi)^{-n/2}
   \|\chi u\|_{2,\langle\xi\rangle^{-r}}
       \\
\|\langle\xi\rangle^r\widehat\phi(-\xi)\|_2\\
 \le C_K\max_{|\alpha|\le2a}\sup_K|\partial^\alpha\phi|.
\end{gathered}
\tag{19}
\]
The second norm is finite with this uniform derivative order because the decay exponent \(2a-r\) exceeds \(n/2\); its fixed-support bound is the compact volume times the indicated derivative bound. Thus \(2a\) is a global finite order, even though \(C_K\) may vary. The solution retains support in \(H\).

In particular apply this result to \(\delta_0\), which has order zero and support in \(H\). It produces a global finite-order fundamental distribution supported in \(H\). Consequently this proof establishes the sufficient implications from the root condition to the weighted local solvability, finite-order solvability and supported fundamental-solution clauses of [the five-way theorem](analytic-root-barriers-and-supported-solvability.md), using the available Holmgren theorem. It does not establish the reverse necessary root implication.

## Exercises with complete solutions

**Exercise 1 (entry).** For \(P(\xi_x,\xi_t)=\xi_x\), use \(N=(0,1)\), \(\xi^1=(1,1)\), \(\xi^2=(-1,1)\), and \(\varepsilon=1/2\). Compute the polytope, prove it bounded, and verify the noncharacteristic normals despite \(p_m(N)=0\).

**Solution.** Here \(N^1=(1/2,3/2)\), \(N^2=(-1/2,3/2)\), and
\(X=\{(x,t):t>-1,\ (3/2)t+(1/2)|x|<1\}\).
Its inequalities give \(t<2/3\) and \(|x|<2-3t<5\), so it is bounded and contains a neighborhood of zero. For \(a>0,b\ge0\), the \(x\)-components of \(aN^1+bN\) and \(aN^2+bN\) are respectively \(a/2\) and \(-a/2\), both nonzero. The wedge's logarithmic normal has one of these nonzero \(x\)-components, so it is noncharacteristic for \(D_x\), although the pure time normal is characteristic. The example verifies exactly why the strictly positive coefficient in(5) is required.

**Exercise 2 (intermediate).** Explain both the support and norm roles of the one-sided mollifier. Does the weighted convergence argument extend to \(p=\infty\) merely because its Fourier multiplier is bounded by one?

**Solution.** Support addition gives \(\operatorname{supp}(h*\rho_\tau)\subset H+H=H\), since \(\rho_\tau\) is supported at positive time. A symmetric mollifier need not preserve this inclusion: convolving \(\delta_0\) with a bump extending to negative time creates negative-time support. The support radius below \(\tau\) also ensures(12) by a fixed distance between two exhaustion regions. In Fourier space, finite-\(p\) convergence follows from pointwise convergence of the bounded multiplier and dominated convergence of the integrable \(p\)-th power. The infinity norm has no such dominated convergence conclusion. Already \(\delta_0\in B_{\infty,1}\) has transform one, while \(\widehat{\rho_\tau}(\xi)\to0\) as \(|\xi|\to\infty\) for every fixed \(\tau>0\). Hence \(\|\delta_0-\rho_\tau\|_{\infty,1}\ge1\). The one-sided support condition does not remedy this norm obstruction. The theorem therefore uses finite exponents.

**Exercise 3 (advanced).** Let \(n=3\) and let \(f\) have order at most two. Give one explicit input weight for the finite-order corollary and one uniform derivative order for the produced solution. Explain why the output order does not depend on how far along the exhaustion a compact test lies.

**Solution.** Formula(18) gives \(r=M+n+1=6\) and input weight \(\langle\xi\rangle^{-6}\) with exponent two. A compactly cut-off \(f\) has transform bounded by \(C\langle\xi\rangle^2\), so its weighted Fourier square is bounded by \(C^2\langle\xi\rangle^{-8}\), integrable in three dimensions. The solution lies locally in \(B_{2,\langle\xi\rangle^{-6}S_P}\), and hence in \(B_{2,\langle\xi\rangle^{-6}}\). Choose \(a=4\): \(2a=8>6+3/2\). Formula(19) therefore bounds every compact-test pairing using derivatives through order eight. The local weighted norm of \(\chi u\) and the compact volume can change with the test region, but the Fourier decay and the fixed exponent \(r\) determine the same derivative order eight everywhere. Thus the solution has global finite order at most eight, rather than merely some unrelated order on each compact set.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
