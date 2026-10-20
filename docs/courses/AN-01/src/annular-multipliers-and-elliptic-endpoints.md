# Annular multipliers and elliptic endpoints

*Exposition and original illustrations by GPT-6 Astra (OpenAI). Public domain (CC0 1.0).*

A multiplier can be controlled by averaged derivatives on each frequency annulus. Its inverse kernels need not satisfy a pointwise gradient estimate away from the origin: integrable translation differences and integrable tails are enough. Cancellation inside cubes then gives the weak first endpoint, all finite intermediate exponents and Hölder continuity. Applied to a reciprocal elliptic polynomial, these bounds recover the derivatives of a distributional solution. At the continuous endpoint an explicit sum of shrinking annuli shows why the conclusion changes.

Use \(Ff(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx\), \(G=F^{-1}\) with coefficient \((2\pi)^{-n}\), \(D_j=-i\partial_j\), and \(n\ge1\). The complete \(L^2\) Fourier maps and their distributional agreement are proved in [*Fourier–Laplace slices and boundary poles*](fourier-laplace-slices-and-boundary-poles.md), Lemma 0.1. [*Fractional energy and sharp Fourier embeddings*](fractional-energy-and-sharp-fourier-embeddings.md), Lemma 1 and Corollary 6, gives the integer Sobolev norm, reciprocal pairing and continuous embedding. The [Schwartz Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, supplies inversion and all test-space identities.

The cube decomposition used below is the complete proof of Lemma 6.1 in [*Convolution estimates and weak-gradient embeddings*](convolution-estimates-and-weak-gradient-embeddings.md). The [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15–16, proves Hölder, Young, Tonelli, dominated convergence, completeness and smooth approximation. [*Convolution as addition of supports*](convolution-as-addition-of-supports.md), B0–B3 and Theorem 1.1, gives compact-factor convolution, finite-order parameter pairings and derivative transfer. [*Tempered growth and spectral cutoffs*](tempered-growth-and-spectral-cutoffs.md), Lemma 2.1, proves convolution with a Schwartz factor and its Fourier identity. Scalar differentiation, compact cutoffs and finite Taylor formulas are in the [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §13. The [angular foundation](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A4, supplies polar integration.

## Averaged frequency derivatives give integrable kernels

Let \(s\) be an integer with \(s>n/2\). Suppose \(b\in L^2_{\mathrm{loc}}(\mathbb R^n)\), its weak derivatives through order \(s\) exist locally away from zero, and
\[
 A^2=\sup_{R>0}\sum_{|\alpha|\le s}
 R^{2|\alpha|-n}
 \int_{R/2<|\xi|<2R}|\partial^\alpha b(\xi)|^2\,d\xi<\infty.
 \tag{M1}
\]
The value of a representative at zero is immaterial. Constants below may depend on \(n,s\) and the fixed smooth cutoffs. Put \(\varepsilon=s-n/2>0\).

Choose a radial \(0\le\chi\le1\) which equals one for \(|\eta|\le1\) and zero for \(|\eta|\ge2\), and set
\[
 \phi(\eta)=\chi(\eta)-\chi(2\eta),\qquad
 a_R(\eta)=\phi(\eta)b(R\eta),\qquad K_R=Ga_R.
 \tag{M2}
\]
Thus \(\phi\) is supported in \(1/2\le|\eta|\le2\) and equals one on the unit sphere.

**Lemma 1 (uniform annular kernels).** The symbol has a bounded representative away from zero, with \(\|b\|_\infty\le C A\). Every \(K_R\) is smooth, and
\[
 \begin{gathered}
 \|\langle x\rangle^s K_R\|_2+
       \|\langle x\rangle^s\nabla K_R\|_2\le C A,\\
 \|K_R\|_1+\|\nabla K_R\|_1+\|K_R\|_\infty\le C A,\\
 \int_{|x|>t}|K_R(x)|\,dx
          \le C A\min(1,t^{-\varepsilon}),\qquad t>0,\\
 \|K_R(\,\cdot-h)-K_R\|_1\le C A|h|.
 \end{gathered}
 \tag{M3}
\]
The same estimates hold for \(G(\zeta(\eta)b(R\eta))\), where \(\zeta\) is any fixed smooth function compactly supported away from zero, with a constant also depending on \(\zeta\).

**Proof.** The weak product and dilation rules follow directly by substitution and integration by parts against compact smooth tests. Leibniz's rule gives
\[
 \partial^\alpha a_R
 =\sum_{\beta\le\alpha}\binom{\alpha}{\beta}
       (\partial^{\alpha-\beta}\phi)
                R^{|\beta|}(\partial^\beta b)(R\,\cdot).
 \tag{M4}
\]
After \(\xi=R\eta\), each squared \(L^2\) norm on this fixed annulus is bounded by a cutoff constant times \(A^2\). These are global weak derivatives: the cutoff is compactly supported in the open set where the local weak derivatives exist. The same reasoning applies to \(\eta_j a_R\), and more generally to every fixed polynomial times \(a_R\). The integer Sobolev identity therefore bounds \(a_R\) and \(\eta_j a_R\) in \(H^s\).

The continuous Sobolev embedding gives \(\|a_R\|_\infty\le C A\). On a neighborhood of the unit sphere, \(\phi\ne0\), so \(a_R/\phi\) is a continuous representative of \(b(R\,\cdot)\). These representatives agree on overlaps: two continuous functions equal almost everywhere on an open set agree everywhere there. On \(|\eta|=1\), \(\phi=1\). Varying \(R\) proves the uniform bound on \(b\).

The functions \(a_R\) and all their frequency monomials are in \(L^1\), by compact support and Cauchy–Schwarz. Differentiation of their inverse integrals shows \(K_R\in C^\infty\). Fourier derivative identities and Parseval turn the \(H^s\) bounds just obtained into the first line of (M3), with the fixed Fourier constants absorbed into \(C\). Weighted Cauchy–Schwarz and
\[
 \int_{|x|>t}\langle x\rangle^{-2s}\,dx
              \le C t^{n-2s}\quad(t\ge1)
 \tag{M5}
\]
give the \(L^1\) and tail bounds. Polar integration proves (M5); the full integral is finite since \(2s>n\). The direct inverse integral gives the supremum bound. Finally,
\[
 K_R(x-h)-K_R(x)
       =-\int_0^1 h\cdot\nabla K_R(x-\theta h)\,d\theta.
 \tag{M6}
\]
Integrate the absolute value, use Tonelli and translation invariance, and apply the gradient \(L^1\) bound.

For a general fixed \(\zeta\), cover its compact radial range by finitely many annuli comparable to the one in (M1). A finite subordinate smooth partition reduces its derivative bounds to (M4), with radii \(c_\nu R\) and fixed positive \(c_\nu\). All the subsequent estimates are unchanged. \(\square\)

Define on \(L^2\)
\[
 T_bf=G(bFf),\qquad \|T_bf\|_2\le B\|f\|_2,\quad
 B=\|b\|_\infty\le C A.
 \tag{M7}
\]
The \(L^2\) adjoint is \(T_{\overline b}\), by Parseval. The tempered kernel is \(k=Gb\). On Schwartz functions \(T_bf=k*f\), with the full distributional kernel, by the Fourier convolution identity cited above. In particular, a constant symbol gives a multiple of \(\delta_0\), not a zero operator.

## A zero mean makes the annular sum converge off a cube

Put
\[
 L_j(x)=2^{jn}K_{2^j}(2^jx),\qquad j\in\mathbb Z.
 \tag{M8}
\]
Its Fourier transform is \(\phi(2^{-j}\xi)b(\xi)\). The telescoping identity is
\[
 \sum_{j=-N}^{N}\phi(2^{-j}\xi)
       =\chi(2^{-N}\xi)-\chi(2^{N+1}\xi)
             \longrightarrow1\quad(\xi\ne0).
 \tag{M9}
\]
The partial sums are uniformly bounded. Consequently the finite operators
\(\sum_{j=-N}^N L_j*f\) tend to \(T_bf\) in \(L^2\), by dominated convergence in Fourier variables. Also \(\sum L_j\to k\) on every Schwartz test, since \(b\) is bounded and the Fourier transform of that test is integrable.

**Lemma 2 (cancellation outside a doubled cube).** Let \(Q\) be a cube of side \(\ell>0\), let \(2Q\) be its concentric double, and let \(w\in L^1\cap L^2\) be supported in \(Q\), with \(\int w=0\). Then
\[
 \int_{(2Q)^c}|T_bw|\,dx\le C A\|w\|_1.
 \tag{M10}
\]

**Proof.** Write \(c\) for the center. If \(x\notin2Q\) and \(y\in Q\), then \(|x-y|\ge\ell/2\). Scaling the tail bound in (M3) gives, when \(2^j\ell\ge1\),
\[
 \|L_j*w\|_{L^1((2Q)^c)}
       \le C A(2^j\ell)^{-\varepsilon}\|w\|_1.
 \tag{M11}
\]
For every \(j\), the zero mean gives
\[
 L_j*w(x)=\int_Q[L_j(x-y)-L_j(x-c)]w(y)\,dy.
 \tag{M12}
\]
The translation bound in (M3), after scaling, and
\(|y-c|\le\sqrt n\,\ell/2\), give the full-space bound
\[
 \|L_j*w\|_1\le C A\,2^j\ell\|w\|_1.
 \tag{M13}
\]
All integrals here are legitimate \(L^1\) convolutions. Choose the integer \(J\) with \(1\le2^J\ell<2\). The low and high sums satisfy
\[
 \sum_{j<J}2^j\ell<2,\qquad
 \sum_{j\ge J}(2^j\ell)^{-\varepsilon}
                 \le(1-2^{-\varepsilon})^{-1}.
 \tag{M14}
\]
Thus \(\sum L_j*w\) converges absolutely in \(L^1((2Q)^c)\) and obeys (M10). Its symmetric partial sums also converge in \(L^2\) to \(T_bw\). Subsequences converging almost everywhere in these two norms identify the limits on \((2Q)^c\). Such subsequences follow, for example, by choosing summable norm differences and applying Tonelli to those differences. This proves (M10) for the original multiplier. No pointwise sum for \(k\) at its singular point was used. \(\square\)

## Weak first endpoint and every finite exponent

**Theorem 3 (annular Sobolev multiplier theorem).** Under (M1),
\[
 |\{x:|T_bf(x)|>\lambda\}|
       \le C A\,\lambda^{-1}\|f\|_1
       \quad(f\in L^1\cap L^2,\ \lambda>0),
 \tag{M15}
\]
and for every \(1<p<\infty\),
\[
 \|T_bf\|_p\le C_{n,s,p}A\|f\|_p.
 \tag{M16}
\]
The latter gives a unique bounded extension to all \(L^p\), agreeing with the \(L^2\) realization on the intersection. Estimate (M15) also defines a unique extension from \(L^1\) by convergence in measure. For Schwartz input, all these realizations are the convolution by \(k=Gb\).

**Proof of the weak estimate.** If \(A=0\), then \(b=0\) almost everywhere and every assertion is immediate. Otherwise apply the earlier dyadic decomposition to \(f\) at height \(a=\lambda/A\):
\[
 f=g+\sum_Qw_Q,\quad
 \|g\|_\infty\le2^na,\quad \|g\|_1\le\|f\|_1,\quad
 \sum_Q\|w_Q\|_1\le2\|f\|_1,\quad
 \sum_Q|Q|\le a^{-1}\|f\|_1.
 \tag{M17}
\]
Each \(w_Q\) has zero integral. Because \(f\in L^2\), the good part is also in \(L^2\), with
\(\|g\|_2^2\le2^na\|f\|_1\). The functions \(w_Q\) are the disjoint pieces of \(f-g\in L^2\); hence their sum converges in \(L^2\), as well as in \(L^1\).

Set \(\Omega=\bigcup_Q2Q\). Its measure is at most \(2^na^{-1}\|f\|_1\). Lemma 2 gives absolute \(L^1(\Omega^c)\) convergence of \(\sum T_bw_Q\), with norm at most \(C A\|f\|_1\). Its \(L^2\) partial sums converge to \(T_b(f-g)\); the same subsequence argument as before identifies the two limits. Chebyshev's inequality, which follows by integrating \(|h|^r\ge t^r1_{\{|h|>t\}}\), now gives
\[
 \begin{aligned}
 |\{|T_bf|>\lambda\}|
 &\le|\Omega|+
       4\lambda^{-2}\|T_bg\|_2^2
       +2\lambda^{-1}\|T_b(f-g)\|_{L^1(\Omega^c)}\\
 &\le C A\,\lambda^{-1}\|f\|_1.
 \end{aligned}
 \tag{M18}
\]
Here \(B\le C A\) in (M7) and \(a=\lambda/A\) retain the correct linear dependence on \(A\).

**Proof for \(1<p<2\).** Initially take \(f\in L^p\cap L^2\). Split it at \(|f|=\lambda/A\) into \(f_{\rm high}\) and \(f_{\rm low}\). The high part is in \(L^1\cap L^2\), since
\(|f|1_{\{|f|>\lambda/A\}}\le(\lambda/A)^{1-p}|f|^p\). The low part is in \(L^2\). From (M15), (M7) and the triangle inequality for level sets,
\[
 |\{|T_bf|>\lambda\}|
 \le \frac{C A}{\lambda}
                \int_{|f|>\lambda/A}|f|
       +\frac{C A^2}{\lambda^2}
                \int_{|f|\le\lambda/A}|f|^2.
 \tag{M19}
\]
The layer formula follows directly from
\(|h(x)|^p=\int_0^{|h(x)|}p\lambda^{p-1}\,d\lambda\)
and Tonelli. Apply it to (M19), then interchange the nonnegative integrals:
\[
 \begin{aligned}
 \|T_bf\|_p^p
 &\le C p A\int|f(x)|
             \int_0^{A|f(x)|}\lambda^{p-2}\,d\lambda\,dx\\
 &\quad+C p A^2\int_{\{f\ne0\}}|f(x)|^2
             \int_{A|f(x)|}^\infty\lambda^{p-3}\,d\lambda\,dx\\
 &\le C p\left(\frac1{p-1}+\frac1{2-p}\right)
                           A^p\|f\|_p^p .
 \end{aligned}
 \tag{M20}
\]
Zero values contribute zero separately. The two strict conditions on \(p\) are exactly those needed by the two scalar integrals. Compact smooth density and \(L^p\) completeness extend the operator to all \(L^p\). On \(L^p\cap L^2\), simultaneous approximation by truncation and mollification gives both limits; testing locally, or taking subsequences, shows they agree. At \(p=2\) use (M7).

**Proof for \(2<p<\infty\).** The conjugate symbol satisfies (M1) with the same \(A\). Its multiplier is the \(L^2\) adjoint of \(T_b\), and the proved bound applies to it at \(r=p/(p-1)\in(1,2)\). For Schwartz \(f\), put \(u=T_bf\in L^2\). On
\[
 E_{R,N}=\{|x|_\infty\le R,\ |u(x)|\le N\},\qquad
 h_{R,N}=1_{E_{R,N}}|u|^{p-2}u,
 \tag{M21}
\]
with value zero when \(u=0\), the function \(h_{R,N}\) is in \(L^2\cap L^r\). Parseval's adjoint identity and Hölder give
\[
 \int_{E_{R,N}}|u|^p
   = (u,h_{R,N})_{L^2}
   = (f,T_{\overline b}h_{R,N})_{L^2}
   \le C A\|f\|_p
             \left(\int_{E_{R,N}}|u|^p\right)^{1/r}.
 \tag{M22}
\]
The inner products are linear in the first variable. Divide only if the finite integral is positive. Let \(R,N\) increase to infinity and use monotone convergence. This proves (M16) on Schwartz input; density and completeness extend it and give the same agreement on intersections. No representation theorem for an \(L^p\) dual is needed.

**The \(L^1\) realization.** Approximate \(f\in L^1\) by \(f_j\in L^1\cap L^2\) in \(L^1\). Estimate (M15) on differences makes \(T_bf_j\) Cauchy in measure, on the whole space. Choose a subsequence with
\[
 |\{|T_bf_{j+1}-T_bf_j|>2^{-j}\}|\le2^{-j}.
 \tag{M23}
\]
Outside the limsup of these exceptional sets, whose measure is zero since the sum of their measures is finite, the values form a Cauchy sequence. Its measurable finite limit is the limit in measure of the original sequence, by the Cauchy estimate. That estimate also proves independence of approximation and linearity. For \(\lambda'<\lambda\), convergence in measure and
\(\{|u|>\lambda\}\subset\{|u_j|>\lambda'\}\cup\{|u-u_j|>\lambda-\lambda'\}\)
pass (M15) to the limit; then let \(\lambda'\uparrow\lambda\). Agreement with the \(L^2\) map on \(L^1\cap L^2\) follows from simultaneous approximation. The same truncation and mollification argument gives agreement with every finite \(L^p\) map on \(L^1\cap L^p\). The weak estimate concerns a measurable function and does not assert that it is locally integrable. \(\square\)

## Hölder continuity from smooth frequency pieces

For \(0<\gamma<1\), write
\([f]_\gamma=\sup_{x\ne y}|f(x)-f(y)|/|x-y|^\gamma\).

**Theorem 4 (the full Hölder seminorm).** If \(f\) is compactly supported and \(\gamma\)-Hölder continuous, then the \(L^2\) output \(T_bf\) has a bounded continuous representative and
\[
 [T_bf]_\gamma\le C_{n,s,\gamma} A[f]_\gamma.
 \tag{M24}
\]
No smooth approximation in the same Hölder norm is assumed.

**Proof.** The inverse transform \(q=G\phi\) is Schwartz, and
\(\int q=\phi(0)=0\). Put
\[
 f_j(x)=\int 2^{jn}q(2^jy)f(x-y)\,dy
       =\int q(y)[f(x-2^{-j}y)-f(x)]\,dy.
 \tag{M25}
\]
The second identity is absolutely convergent and gives
\[
 \|f_j\|_\infty\le C_\gamma2^{-j\gamma}[f]_\gamma,\qquad
 \|\nabla f_j\|_\infty
        \le C_\gamma2^{j(1-\gamma)}[f]_\gamma.
 \tag{M26}
\]
For the derivative, differentiate the Schwartz convolution kernel; its derivative has integral zero, and integrate its absolute value against \(|y|^\gamma\). Those moments are finite by Schwartz decay.

Choose a fixed smooth \(\zeta\), compactly supported away from zero, equal to one on \(\operatorname{supp}\phi\), and let
\(\widetilde K_R=G(\zeta(\eta)b(R\eta))\).
Lemma 1 gives \(\|\widetilde K_R\|_1\le C A\). The frequency identity \(\zeta\phi=\phi\) shows
\[
 T_bf_j=2^{jn}\widetilde K_{2^j}(2^j\,\cdot)*f_j.
 \tag{M27}
\]
This identity follows first in \(L^2\); the convolutions with bounded smooth \(f_j\) and its bounded derivatives give its continuous representative. Thus
\[
 \|T_bf_j\|_\infty\le C_\gamma A\,2^{-j\gamma}[f]_\gamma,\qquad
 \|\nabla T_bf_j\|_\infty
       \le C_\gamma A\,2^{j(1-\gamma)}[f]_\gamma.
 \tag{M28}
\]

There is also a low-frequency value bound, needed to identify an actual function rather than only its differences. Since \(T_bf_j=L_j*f\) and
\(\|L_j\|_\infty\le C A\,2^{jn}\),
\[
 \|T_bf_j\|_\infty\le C A\,2^{jn}\|f\|_1.
 \tag{M29}
\]
For \(j<0\), (M29) is summable because \(n\ge1\); for \(j\ge0\), the first bound in (M28) is summable. The series therefore converges uniformly to a bounded continuous function. Its symmetric partial sums converge in \(L^2\) to \(T_bf\) by (M9), so the function represents that same output.

For \(d=|x-y|>0\), use the derivative estimate in (M28) when \(2^jd\le1\), and twice the supremum estimate otherwise:
\[
 \begin{aligned}
 |T_bf(x)-T_bf(y)|
 &\le C_\gamma A[f]_\gamma
 \left(d\sum_{2^jd\le1}2^{j(1-\gamma)}
                +2\sum_{2^jd>1}2^{-j\gamma}\right)\\
 &\le C_\gamma A[f]_\gamma d^\gamma
 \left(\frac1{1-2^{-(1-\gamma)}}
                +\frac2{1-2^{-\gamma}}\right).
 \end{aligned}
 \tag{M30}
\]
The last two geometric sums include all integer scales. Their denominators are positive exactly for \(0<\gamma<1\). This proves (M24). \(\square\)

## Elliptic equations with arbitrary distributional input

A constant-coefficient polynomial \(P(\xi)\) of degree \(m\ge1\) is elliptic if its principal homogeneous part \(P_m\) has no zero on the real unit sphere. Complex coefficients are allowed.

**Lemma 5 (a smooth inverse away from the origin).** There is a smooth symbol \(a\) such that \(E=Ga\) satisfies
\[
 P(D)E=\delta_0-h,\qquad h\in\mathcal S,
 \tag{M31}
\]
and \(E\) is smooth off zero. For every multiindex \(\beta\),
\[
 |\partial^\beta a(\xi)|\le C_\beta\langle\xi\rangle^{-m-|\beta|}.
 \tag{M32}
\]
For every \(|\alpha|\le m\), the symbol \(b_\alpha(\xi)=\xi^\alpha a(\xi)\) satisfies (M1).

**Proof.** Compactness of the sphere gives \(|P_m(\xi)|\ge c|\xi|^m\). The lower terms are \(O(|\xi|^{m-1})\), so
\(|P(\xi)|\ge(c/2)|\xi|^m\) for \(|\xi|\ge R_0\), after increasing \(R_0\ge1\). Choose a compact smooth \(\theta=1\) on a neighborhood of \(\{|\xi|\le R_0\}\), and set \(a=(1-\theta)/P\), with value zero where the numerator vanishes. Choose its transition inside the region where the denominator is nonzero. Then \(Pa=1-\theta\), so (M31) follows with \(h=G\theta\).

For large \(|\xi|\), differentiation of \(Pa=1\) gives
\[
 P\,\partial^\beta a
   =-\sum_{0<\nu\le\beta}\binom{\beta}{\nu}
            (\partial^\nu P)(\partial^{\beta-\nu}a).
 \tag{M33}
\]
Induction, \(|\partial^\nu P|\le C_\nu|\xi|^{m-|\nu|}\) when \(|\nu|\le m\), and the lower bound on \(P\), prove (M32) there. The compact transition region supplies the remaining constants.

For completeness, smoothness of the inverse distribution away from zero follows from a convergent differentiated annular series. Localize \(a\) by \(\phi(2^{-j}\xi)\). Since \(a=0\) near zero, only \(j\) above a fixed lower bound occur. Rescaling its inverse transform and integrating repeatedly in a frequency coordinate whose paired spatial coordinate is largest gives, for every \(\mu\) and every integer \(N\ge0\),
\[
 |\partial_x^\mu G(\phi(2^{-j}\,\cdot)a)(x)|
 \le C_{\mu,N}\,2^{j(n-m+|\mu|)}
                         (1+2^j|x|)^{-N}.
 \tag{M34}
\]
Here the rescaled amplitude and each of its derivatives are bounded by \(C2^{-jm}\) on a fixed compact annulus, by (M32). Its compact inverse integral gives the bound when \(2^j|x|\le1\); repeated integration by parts gives the other bound. Choosing \(N>n-m+|\mu|\) makes the series uniformly convergent on each compact set away from zero, for every derivative. The finite fundamental theorem of calculus identifies the derivatives of the limit. The telescoping formula and Schwartz decay show that the same series tends to \(Ga\) as a tempered distribution, so the smooth function is its restriction off zero.

Finally the product rule gives
\(|\partial^\nu b_\alpha(\xi)|\le C_\nu\langle\xi\rangle^{|\alpha|-m-|\nu|}\).
It vanishes near zero. On large annuli,
\[
 R^{2|\nu|-n}\int_{R/2<|\xi|<2R}
              |\partial^\nu b_\alpha|^2
                    \le C_\nu R^{2(|\alpha|-m)}\le C_\nu.
 \tag{M35}
\]
Annuli in a fixed bounded range have uniformly bounded contributions; sufficiently small annuli contribute zero. Summing through any fixed integer \(s>n/2\) proves (M1). \(\square\)

**Theorem 6 (interior \(L^p\) and Hölder regularity).** Let \(X\subset\mathbb R^n\) be open and \(u\in\mathcal D'(X)\). For an elliptic constant-coefficient \(P(D)\) of order \(m\ge1\),
\[
 \begin{aligned}
 P(D)u\in L^p_{\mathrm{loc}}(X),\ 1<p<\infty
       &\ \Longrightarrow\
          D^\alpha u\in L^p_{\mathrm{loc}}(X)\quad(|\alpha|\le m),\\
 P(D)u\in C^\gamma_{\mathrm{loc}}(X),\ 0<\gamma<1
       &\ \Longrightarrow\
          D^\alpha u\in C^\gamma_{\mathrm{loc}}(X)\quad(|\alpha|\le m).
 \end{aligned}
 \tag{M36}
\]
No regularity of \(u\) beyond being a distribution is assumed. A nonzero operator of order zero has the same conclusions immediately by division by its constant.

**Proof.** Fix a relatively compact neighborhood \(Y\) of any chosen point, and a compact cutoff \(\eta\) in \(X\) equal to one near \(\overline Y\). Write
\[
 v=\eta u,\qquad
 P(D)v=f+q,\qquad f=\eta P(D)u,\quad q=[P(D),\eta]u.
 \tag{M37}
\]
Extend these compactly supported distributions to the whole space. Every coefficient of the commutator contains a derivative of \(\eta\), so \(q\) has compact support separated from \(\overline Y\). Compact-factor convolution and derivative transfer, applied to (M31), give
\[
 v=E*f+E*q+h*v.
 \tag{M38}
\]
The last term is smooth by finite-order parameter pairing. The term \(E*q\) is smooth near \(\overline Y\): every relevant \(x-y\) stays away from zero, where Lemma 5 supplies all derivatives of \(E\), and the compact support of \(q\) permits the same parameter argument.

It remains to identify \(D^\alpha E*f\) with the multiplier \(T_{b_\alpha}f\) in the appropriate function space. For compact smooth \(f\), this is the exact Fourier convolution identity. For compactly supported \(L^p\) input, mollification with one common bounded support converges in \(L^p\) and \(L^1\). The multiplier outputs converge in \(L^p\) by Theorem 3. The distributional convolutions converge on tests, because the inner smooth function paired with \(f\) is uniformly bounded on that fixed support; the \(L^1\) difference therefore controls the pairing. Uniqueness of the distributional limit identifies the two outputs. If \(f\) is compact Hölder, it is also in \(L^2\), and Theorem 4 gives the Hölder representative of the same multiplier. Multiplication by the smooth compact cutoff makes the local Hölder datum into a global compact Hölder function, by the product difference formula and a finite compact cover.

Differentiate (M38), apply Theorem 3 or 4 to \(b_\alpha\), and retain the smooth remainder on \(Y\). This gives (M36) there, for all \(|\alpha|\le m\). Such neighborhoods cover \(X\). \(\square\)

## Continuous forcing can leave every top derivative discontinuous

**Theorem 7 (an explicit continuous endpoint obstruction).** Let \(n>1\), let \(X\) be a nonempty open set, and let \(P(D)\) be any constant-coefficient operator of order \(m>0\). There is a compactly supported
\[
 u\in C^{m-1}(X)\setminus C^m(X),\qquad P(D)u\in C_c(X).
 \tag{M39}
\]
One can choose the same \(u\) so that every \(D^\alpha u\), \(|\alpha|=m\), for which the monomial \(\xi^\alpha\) is not proportional to \(P_m(\xi)\), has no continuous representative. In fact each such derivative is unbounded in every neighborhood of one point. The assertion includes elliptic operators.

**Proof: choose one polynomial.** Translate a point of \(X\) to zero. Let \(V_m\) be the complex vector space of homogeneous polynomials of degree \(m\). The map
\[
 L:V_m\to\mathbb C,\qquad L(U)=P_m(D)U
 \tag{M40}
\]
is a nonzero linear functional: on a monomial \(x^\beta\), it extracts its corresponding coefficient in \(P_m\), multiplied by \((-i)^m\beta!\). Since \(n>1,m>0\), \(V_m\) contains at least two distinct monomials, so \(\ker L\ne\{0\}\).

For \(|\alpha|=m\), put \(L_\alpha(U)=D^\alpha U\), another scalar functional. Its restriction to \(\ker L\) is zero exactly when it is proportional to \(L\). Indeed, choose \(e\) with \(L(e)=1\); then \(v-L(v)e\in\ker L\) shows \(L_\alpha(v)=L(v)L_\alpha(e)\) in that case. In the monomial basis this proportionality is precisely that of \(\xi^\alpha\) and \(P_m\).

There are only finitely many multiindices. Choose \(U\in\ker L\) for which every nonzero restricted \(L_\alpha\) is nonzero. Here is a direct finite-dimensional construction. If \(v_1,\ldots,v_d\) is a basis of \(\ker L\), the vector
\(\sum_{\nu=1}^d z^{\nu-1}v_\nu\) has, under each such functional, a nonzero polynomial in \(z\). A nonzero polynomial has at most its degree many roots, by repeated division by \(z-z_0\). Choose a complex \(z\) outside their finite union of roots. At least one restricted functional is nonzero, since the coordinate coefficient functionals separate nonzero polynomials. Thus this \(U\) is nonzero and
\[
 P_m(D)U=0,\qquad
 d_\alpha:=D^\alpha U\ne0
       \quad\hbox{whenever }\xi^\alpha\notin\mathbb C P_m.
 \tag{M41}
\]

**Proof: put the forcing on disjoint annuli.** Choose a radius \(r_0>0\) whose closed ball lies in \(X\), and a smooth radial cutoff \(\rho\) equal to one on \(|x|\le1/2\), zero on \(|x|\ge1\). Put
\[
 u_j(x)=\rho(2^jx/r_0)U(x),\qquad
 a_j=\frac1{j+1},\qquad
 u=\sum_{j=0}^\infty a_j u_j.
 \tag{M42}
\]
Homogeneity gives \(u_j(x)=(r_0\,2^{-j})^m(\rho U)(2^jx/r_0)\). Therefore, for every \(\beta\),
\[
 \|D^\beta u_j\|_\infty
       \le C_\beta(r_0\,2^{-j})^{m-|\beta|}.
 \tag{M43}
\]
For \(|\beta|\le m-1\) the weighted series is uniformly absolutely convergent. Repeatedly applying the fundamental theorem of calculus to the finite partial sums and passing to the uniform limits proves \(u\in C^{m-1}\), with precisely these derivatives. Its support lies in the closed \(r_0\)-ball. Every derivative of order below \(m\) vanishes at zero.

On the inner half-ball \(u_j=U\), and \(P_m(D)U=0\); outside its ball \(u_j=0\). Thus
\[
 \operatorname{supp}P_m(D)u_j
   \subset\{r_0\,2^{-j-1}\le|x|\le r_0\,2^{-j}\},\qquad
 \|P_m(D)u_j\|_\infty\le C.
 \tag{M44}
\]
The interiors of these annuli are disjoint. At their boundary spheres the terms vanish, by smoothness and the constant values of the cutoff on either side. Hence every tail satisfies
\[
 \left\|\sum_{j\ge N}a_jP_m(D)u_j\right\|_\infty
                    \le C\sup_{j\ge N}a_j\longrightarrow0.
 \tag{M45}
\]
The sum is continuous and zero at the origin. The lower-order part of \(P(D)u\) is continuous by the already established \(C^{m-1}\) convergence. Distributional differentiation of the uniform limit of the partial sums identifies their continuous output limit with \(P(D)u\). This proves the forcing assertion in (M39).

**Proof: the top derivatives accumulate.** Away from zero, only finitely many terms in (M42) can be nonzero locally, so \(u\) is smooth there. If
\(r_0\,2^{-J-1}<|x|\le r_0\,2^{-J}\), then all terms with \(j<J\) have at \(x\) the derivatives of \(U\), all terms with \(j>J\) vanish, and at most the \(J\)-th term is in transition. Boundary values obey the same identities by smoothness. For \(|\alpha|=m\),
\[
 D^\alpha u(x)
   =d_\alpha\sum_{j=0}^{J-1}\frac1{j+1}
           +\frac{D^\alpha u_J(x)}{J+1},\qquad
 \left|\frac{D^\alpha u_J(x)}{J+1}\right|\le\frac{C_\alpha}{J+1}.
 \tag{M46}
\]
The harmonic partial sums tend to infinity: every block from \(2^k\) to \(2^{k+1}-1\) contributes at least \(1/2\). If \(d_\alpha\ne0\), (M46) consequently tends to infinity in modulus as \(x\to0\), \(x\ne0\). A continuous representative of the distributional derivative would agree with this smooth function off zero and be bounded near zero, which is impossible. At least one such derivative exists, so \(u\notin C^m\). This proves every assertion. \(\square\)

![Summable cancellation across scales and a shrinking-annulus continuous-forcing example.](../figures/annular-cancellation-and-continuous-endpoint.png)

*Left: the bound \(\min(z,z^{-\varepsilon})\), \(z=2^j\ell\), which is summable across dyadic scales in Lemma 2. Middle and right: the explicit planar example in Exercise 4, at \(x_j=(3\,2^{-j}/4,0)\). Its normalized value is \(u(x_j)/|x_j|^2=H_j+1/[2(j+1)]\), while \(P(D)u(x_j)=30/(j+1)\to0\). Here \(H_j=\sum_{k=1}^j1/k\), including \(H_0=0\). The formulas and their limits are proved below; the plots are finite samples. [Reproducible figure source](../figures/annular-cancellation-and-continuous-endpoint.py).*

## Exercises with complete solutions

**Exercise 1 (foundation: a kernel concentrated on the diagonal).** Let \(b=c\) be constant. Check (M1), identify \(k\) and \(T_b\), and explain why Lemma 2 does not discard this operator.

**Solution.** Only the zeroth derivative contributes:
\[
 A^2=|c|^2\,|\{\eta:1/2<|\eta|<2\}|.
 \tag{M47}
\]
Fourier inversion gives \(k=c\delta_0\) and \(T_bf=cf\). For a mean-zero \(w\) supported in \(Q\), \(T_bw=cw\) vanishes off \(2Q\), so (M10) holds with zero left side. The full multiplier still acts inside the cube and in its \(L^2\) estimate. A kernel description valid only off the origin would not determine this diagonal contribution.

**Exercise 2 (intermediate: how many annular derivatives are needed).** In dimension three take \(s=2\). Evaluate the geometric high-scale constant in (M14), and show that pointwise derivative bounds
\(|\partial^\alpha b(\xi)|\le M|\xi|^{-|\alpha|}\), \(|\alpha|\le2\), imply (M1).

**Solution.** Here \(\varepsilon=1/2\), so the constant is
\((1-2^{-1/2})^{-1}\). On the annulus, substitute \(\xi=R\eta\):
\[
 R^{2|\alpha|-3}\int_{R/2<|\xi|<2R}
           |\partial^\alpha b(\xi)|^2\,d\xi
 \le M^2\int_{1/2<|\eta|<2}|\eta|^{-2|\alpha|}\,d\eta.
 \tag{M48}
\]
Each integral is finite because the domain is compact and avoids zero. Sum over the finitely many \(\alpha\). Thus pointwise control is a sufficient special case; the theorem itself requires only the averaged condition.

**Exercise 3 (advanced: both strong endpoints fail).** On the line let \(b(\xi)=-i\,\operatorname{sgn}\xi\) for \(\xi\ne0\). Prove (M1), and show that \(T_b\) sends \(1_{(0,1)}\) to neither \(L^1\) nor \(L^\infty\).

**Solution.** Away from zero all positive derivatives vanish, and the zeroth annular average is constant. The locally square-integrable symbol therefore satisfies (M1) for every integer \(s\ge1\). For \(\delta>0\), regularize it by \(b_\delta=b e^{-\delta|\xi|}\). Direct integration of the two half-line exponentials gives
\[
 Gb_\delta(x)=\frac{x}{\pi(x^2+\delta^2)},\qquad
 T_{b_\delta}1_{(0,1)}(x)
 =\frac1{2\pi}\log
       \frac{x^2+\delta^2}{(x-1)^2+\delta^2}.
 \tag{M49}
\]
The convolution integral is justified by the compact integrable input and the bounded inverse integral of \(b_\delta\in L^1\). Since \(|b_\delta|\le1\) and \(b_\delta\to b\) almost everywhere, Plancherel and dominated convergence give convergence of the outputs in \(L^2\). Their pointwise limit away from \(0,1\) identifies
\[
 T_b1_{(0,1)}(x)=\frac1\pi\log\left|\frac{x}{x-1}\right|
                       \quad\hbox{almost everywhere}.
 \tag{M50}
\]
This is unbounded near both endpoints. For \(x\ge2\),
\(\log(x/(x-1))=\log(1+1/(x-1))\ge1/x\), by integrating
\((1+t)^{-1}\) from \(0\) to \(1/(x-1)\). Its positive tail has infinite integral. The input belongs to both \(L^1\) and \(L^\infty\), proving failure of both strong endpoint conclusions.

**Exercise 4 (advanced: a planar continuous-forcing example).** For \(P(D)=D_1^2+D_2^2=-\Delta\), make Theorem 7 explicit with
\(U(x)=x_1^2-x_2^2+x_1x_2\), \(r_0=1\). Compute the two formulas in the figure.

**Solution.** The polynomial is harmonic. Its three top derivatives are
\[
 D_1^2U=-2,\qquad D_1D_2U=-1,\qquad D_2^2U=2.
 \tag{M51}
\]
Thus the single construction makes every second coordinate derivative unbounded near zero, while \(-\Delta u\) is continuous. Write \(\rho(x)=\vartheta(|x|)\), where
\[
 E(t)=
 \begin{cases}e^{-1/t},&t>0,\\0,&t\le0,\end{cases}
 \qquad
 \vartheta(r)=\frac{E(1-r)}{E(1-r)+E(r-1/2)}
               \quad(1/2<r<1),
 \tag{M52}
\]
extended by one below \(1/2\) and zero above \(1\). Every derivative of \(E\) on \(t>0\) is a polynomial in \(1/t\) times \(e^{-1/t}\), which tends to zero at \(0\) by the exponential series bound; hence the stated extension is smooth. At \(r=3/4\), symmetry gives
\(\vartheta=1/2\), \(\vartheta'=-8\), \(\vartheta''=0\).
For example write \(\vartheta=(1+e^h)^{-1}\), with
\(h=(1-r)^{-1}-(r-1/2)^{-1}\); at this point \(h=0,h'=32,h''=0\), giving all three values by differentiation.

Euler's identity \(x\cdot\nabla U=2U\) follows by differentiating its monomials. Since \(\Delta U=0\), the product rule in dimension two gives
\[
 -\Delta\bigl(\vartheta(|x|)U(x)\bigr)
      =-U(x)\left(\vartheta''(|x|)
                              +\frac5{|x|}\vartheta'(|x|)\right).
 \tag{M53}
\]
At \(x_j=(3\,2^{-j}/4,0)\), the terms with index less than \(j\) are in their polynomial cores, the term with index \(j\) has cutoff \(1/2\), and later terms vanish. Since \(U(x_j)=|x_j|^2\),
\[
 \frac{u(x_j)}{|x_j|^2}=H_j+\frac1{2(j+1)},\qquad
 -\Delta u(x_j)=\frac{30}{j+1}.
 \tag{M54}
\]
The second identity uses (M53), scaling and
\(-5(3/4)(-8)=30\). These exact values display the accumulating polynomial coefficient and the vanishing forcing on successively smaller annuli. The continuity at zero and divergence of the top derivatives follow from the full estimates (M43)–(M46), not from the finite plotted samples.

## References

Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition, Springer, 2003, §7.9, Theorems 7.9.5–7.9.8 and the remark following Theorem 7.9.8. The exact programme proofs for Fourier transformation, integration, cube decomposition and distributional convolution are linked at the beginning of the lesson.
