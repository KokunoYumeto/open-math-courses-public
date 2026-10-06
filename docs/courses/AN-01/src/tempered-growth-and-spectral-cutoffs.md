# Tempered growth and spectral cutoffs

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

Rapid oscillation can make a smooth function with exponential amplitude tempered. The decisive comparison below is between the amplitude and the scale on which the phase changes. A separate global statement characterizes compact Fourier support by an exact Schwartz-convolution identity. Finally, escaping positive masses show that local order zero need not give a small Fourier order, even on one fixed ball.

All pairings are complex linear, without conjugation. The complete [Schwartz and Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves the test space, cutoff density, every Fourier seminorm estimate, both inversion identities, the exact Gaussian transform and all transposed differential identities. We use the equivalent increasing seminorms
\[
P_N(\psi)=\max_{|\alpha|\le N}\sup_x
\langle x\rangle^N|\partial^\alpha\psi(x)|,\qquad
\langle x\rangle=(1+|x|^2)^{1/2}.
\]
Their equivalence follows from
\(\langle x\rangle\le1+|x|\le\sqrt2\langle x\rangle\)
and the monomial-weight comparison proved in F1. Thus a tempered functional satisfies \(|u(\psi)|\le CP_N(\psi)\) for some \(C,N\). The proof is the finite-neighborhood rescaling argument in F5. It restricts to a distribution on compact tests by [U008](order-positivity-and-limits.md), Proposition 1.2.

A family \(B\subset\mathcal S\) is bounded when every \(P_N\) is uniformly bounded on it. Weak convergence in \(\mathcal S'\) means convergence on each test; the strong dual seminorms are \(q_B(u)=\sup_{\psi\in B}|u(\psi)|\) for these bounded families. Our Fourier convention is
\[
\begin{gathered}
F\psi(\xi)=\int e^{-ix\cdot\xi}\psi(x)\,dx,\qquad
Gv(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}v(\xi)\,d\xi,\\
(Fu)(\psi)=u(F\psi),\qquad (Gu)(\psi)=u(G\psi).
\end{gathered}
\tag{0.1}
\]
F1–F5 proves \(FG=GF=I\) on both spaces and the compatibility with ordinary integrable functions.

The [scalar foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12, 13.1–13.5 and 13.7–13.10, supply completeness, compactness, FTC, exponential and trigonometric identities and cutoffs. The [integration foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.2 and 16, supply the absolute and dominated integrations used here. [U021](convolution-as-addition-of-supports.md), B0–B2 and Theorems 1.1–2.1, supplies compact-test localization and convolution. The exact finite-jet theorem used in Solution 5 is proved in the [angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A2–A3.

Two elementary weighted facts will be used repeatedly:
\[
\langle v+w\rangle\le\sqrt2\langle v\rangle\langle w\rangle,
\qquad
\int_{\mathbb R^n}\langle x\rangle^{-n-1}\,dx<\infty.
\]
For the first, square both sides and use
\[
1+|v+w|^2\le1+2|v|^2+2|w|^2
\le2(1+|v|^2)(1+|w|^2).
\]
For the second, the unit ball is contained in a finite cube. On each shell
\(2^j\le|x|<2^{j+1}\), \(j\ge0\), the integrand is at most \(2^{-j(n+1)}\) and the shell lies in a cube of volume \(2^{n(j+2)}\). The integral is bounded by a constant times \(\sum_{j\ge0}2^{-j}\). In particular a smooth function bounded by \(C\langle x\rangle^N\) defines a tempered distribution, with a bound by \(P_{N+n+1}\).

## When the phase absorbs the amplitude

**Theorem 1.1 (an exact growth criterion).** For even positive integers \(m,n\), the smooth function
\[
f(x)=\exp\bigl(x^n+i\exp(x^m)\bigr)
\tag{1.1}
\]
on the line has a tempered extension of its compact-test distribution if and only if \(n\le m\). Such an extension is unique.

**Proof: construction when \(n\le m\).** Put \(\Phi(x)=e^{x^m}\). On \(|x|>1\), define
\[
A(x)=\frac{e^{x^n}}{i\Phi'(x)}
=\frac{x^{1-m}}{im}e^{x^n-x^m}.
\tag{1.2}
\]
If \(n<m\), then \(x^n-x^m\le-|x|^m/2\) for sufficiently large \(|x|\), on both tails because both powers are even. Differentiation of \(A\) gives this same exponential times a finite sum of integer powers of \(x\). Every such term is bounded on \(|x|\ge1\): for any fixed polynomial power choose \(L\) large in \(e^s\ge s^L/L!\), applied to \(s=|x|^m/4\), leaving a bounded decaying factor. A finite remaining annulus causes no problem. Thus both \(A,A'\) are bounded. If \(n=m\), they are exactly \((im)^{-1}x^{1-m}\) and \((1-m)(im)^{-1}x^{-m}\), also bounded.

Choose a smooth \(0\le\chi\le1\), zero on \(|x|\le1\) and one on \(|x|\ge2\). Such cutoffs follow by composing the supplied scalar bump with \(x^2\). Extend the following cutoff expressions by zero near the origin:
\[
B=\chi A e^{i\Phi},\qquad
D=-(\chi A)'e^{i\Phi},\qquad H=(1-\chi)f.
\]
The functions \(B,D\) are bounded, and \(H\) is smooth and compactly supported. Ordinary differentiation, including the cutoff terms, gives
\[
f=B'+D+H.
\tag{1.3}
\]
Define on \(\mathcal S(\mathbb R)\)
\[
T(\psi)=-\int B\psi'+\int D\psi+\int H\psi.
\tag{1.4}
\]
All three integrals are absolutely convergent, and
\[
|T(\psi)|\le
\bigl(\pi\|B\|_\infty+\pi\|D\|_\infty+\|H\|_1\bigr)P_2(\psi),
\]
using the supplied arctangent integral \(\int(1+x^2)^{-1}dx=\pi\). On a compact test, integration by parts and (1.3) identify this with \(\int f\psi\). This is an actual continuous extension, without asserting absolute integrability of \(f\psi\) for every Schwartz test.

**Proof: uniqueness by cutoffs.** In any dimension choose \(\eta\in C_c^\infty\) equal to one on the unit ball and zero outside the radius-two ball; composition with \(|x|^2\) again gives such a cutoff. For \(R\ge1\), every product-rule term in
\(\partial^\alpha[(1-\eta(x/R))\psi]\), \(|\alpha|\le a\), is supported where \(|x|\ge R\). A derivative of the cutoff of order \(j>0\) also contributes at most \(C_jR^{-j}\), and is supported where \(|x|\le2R\). Since
\(\langle x\rangle^a|\partial^\beta\psi|\le R^{-1}P_{a+1}(\psi)\)
there for \(|\beta|\le a\), the finite sum gives
\[
P_a((1-\eta(x/R))\psi)\le C_aR^{-1}P_{a+1}(\psi).
\]
Thus \(\eta(x/R)\psi\to\psi\) in every seminorm, uniformly on bounded Schwartz families. Two continuous extensions agreeing on all compact tests agree on these approximants and therefore on every Schwartz test.

**Proof: obstruction when \(n>m\).** Suppose \(|T(\psi)|\le CP_N(\psi)\) for a tempered extension. Choose a fixed nonnegative \(\rho\in C_c^\infty((-1,1))\) with \(\int\rho>0\). For \(R\) large set
\[
\delta_R=(4mR^{m-1}e^{R^m})^{-1},
\qquad
\psi_R(x)=e^{-i\Phi(R)}
\rho\bigl((x-R)/\delta_R\bigr).
\tag{1.5}
\]
The prefactor is constant in \(x\). These are legitimate compact tests.

For \(|x-R|\le\delta_R\), the factorization of \(x^d-R^d\), or the FTC for \(x^d\), gives
\[
|x^d-R^d|\le C_dR^{d-1}\delta_R
\quad(d=m\text{ or }n)
\]
once \(R\ge2\). Both bounds tend to zero; exponential decay dominates every power by the series estimate used above. Also
\[
\frac{\Phi'(x)}{\Phi'(R)}
=\left(\frac{x}{R}\right)^{m-1}e^{x^m-R^m}
\longrightarrow1
\]
uniformly on the test support. Hence that ratio is at most two for large \(R\). The FTC then gives
\(|\Phi(x)-\Phi(R)|\le2\Phi'(R)\delta_R=1/2\).
The amplitude bound similarly gives \(e^{x^n}\ge e^{R^n}/2\). The elementary cosine bound on \([-1/2,1/2]\) therefore yields
\[
\operatorname{Re}T(\psi_R)
\ge \tfrac12\cos(1/2)e^{R^n}\delta_R\int\rho.
\tag{1.6}
\]
Here the compact-test agreement makes \(T(\psi_R)\) the ordinary integral; all its real contributions have this lower bound.

For \(\delta_R\le1\), differentiation of the rescaled bump gives
\[
P_N(\psi_R)\le C_N\langle R\rangle^N\delta_R^{-N}.
\]
The presumed tempered bound would thus bound
\(e^{R^n}\delta_R^{N+1}/\langle R\rangle^N\).
Its logarithm is
\[
R^n-(N+1)R^m
-[N+(m-1)(N+1)]\log R+O(1).
\]
Because \(n>m\), the first two terms are at least \(R^n/2\) for large \(R\), while \(\log R\le R\) and \(n\ge2\). The logarithm tends to infinity. This contradicts every possible finite \(N\), proving necessity. \(\square\)

Thus \(e^{x^2+i e^{x^4}}\) and \(e^{x^4+i e^{x^4}}\) are tempered in this extension sense, whereas \(e^{x^4+i e^{x^2}}\) is not.

## Convolution with an arbitrary Schwartz factor

**Lemma 2.1 (global smoothing and the multiplier identity).** If \(u\in\mathcal S'(\mathbb R^n)\) and \(f\in\mathcal S(\mathbb R^n)\), then
\[
(u*f)(x)=u_y\bigl(f(x-y)\bigr)
\tag{2.1}
\]
is smooth. Every derivative has a polynomial growth bound with one common exponent. It defines a regular tempered distribution, and
\[
F(u*f)=(Ff)(Fu).
\tag{2.2}
\]
For fixed \(f\), convolution is continuous for both the weak and strong topologies of \(\mathcal S'\).

The cutoff proof in Theorem 1.1 and the seminorm definitions above are part of the test-space facts used in this lemma.

**Proof: the ordinary Schwartz estimate.** For \(f,h\in\mathcal S\), the integral \(f*h(x)=\int f(x-y)h(y)\,dy\) and all its differentiated integrals converge absolutely. For each derivative, boundedness of derivatives of \(f\) and integrability of \(h\) justify differentiation by the FTC and dominated convergence. The weighted inequality above gives, for integers \(a\ge0\),
\[
\begin{aligned}
P_a(f*h)
&\le2^{a/2}P_a(f)\int\langle y\rangle^a|h(y)|\,dy\\
&\le C_{a,n}P_a(f)P_{a+n+1}(h).
\end{aligned}
\tag{2.3}
\]
The last integral is bounded by \(P_{a+n+1}(h)\int\langle y\rangle^{-n-1}dy\), whose finiteness was proved above. Thus convolution maps these tests into \(\mathcal S\) continuously in each variable. Absolute Fubini and \(x=z+y\) also prove \(F(f*h)=(Ff)(Fh)\), since the absolute double integral is \(\|f\|_1\|h\|_1\).

**Proof: smooth parameter tests and growth.** Choose \(|u(\phi)|\le CP_N(\phi)\). Reflection and the weighted inequality show
\[
P_N(f(x-\cdot))
\le2^{N/2}\langle x\rangle^N P_N(f).
\tag{2.4}
\]
Indeed \(\langle y\rangle^N\le2^{N/2}\langle x\rangle^N\langle x-y\rangle^N\), and \(y\)-derivatives differ only by signs.

We verify differentiation in the test space. For a coordinate increment \(h e_j\), the twice-FTC identity is
\[
f(x+h e_j-y)-f(x-y)-h\partial_jf(x-y)
=h^2\int_0^1(1-s)\partial_j^2f(x+s h e_j-y)\,ds.
\]
Apply every \(y\)-derivative through order \(a\), multiply by \(\langle y\rangle^a\), and use (2.4) with the appropriate derivative of \(f\). On a compact set of \(x\)'s and \(|h|\le1\), the resulting \(P_a\) remainder is at most \(C_{a,K}h^2P_{a+2}(f)\). The once-FTC version gives continuity of every translated derivative in \(P_a\). Repeating for each coordinate and derivative proves smoothness with values in \(\mathcal S\). Applying the continuous \(u\) to these difference quotients gives
\[
\begin{gathered}
\partial^\alpha(u*f)(x)
=u_y(\partial^\alpha f(x-y)),\\
|\partial^\alpha(u*f)(x)|
\le C_\alpha\langle x\rangle^N.
\end{gathered}
\tag{2.5}
\]
The exponent \(N\) is independent of \(\alpha\). The preliminary weighted integral bound makes this smooth function a regular tempered distribution.

**Proof: the integrated test and Fourier identity.** Let \(\widetilde f(z)=f(-z)\) and \(\phi\in\mathcal S\). Consider the test-valued integrand
\[
H_x(y)=f(x-y)\phi(x).
\]
For every \(a\), (2.4) gives
\(P_a(H_x)\le C_aP_a(f)\langle x\rangle^a|\phi(x)|\).
This is integrable in \(x\), and its integral outside expanding cubes tends to zero by the extra Schwartz weights.

On a fixed \(x\)-cube the map \(x\mapsto H_x\) is uniformly continuous in every seminorm, by the translated-test calculation and the smooth scalar factor. A finite cubical Riemann sum differs from its integral in \(P_a\) by at most the cube's volume times the corresponding modulus of continuity. It tends to zero as the mesh shrinks. To see the integral directly without assuming a vector integration theorem, differentiate its ordinary integral in \(y\); bounded translated derivatives on the finite cube justify this, and the same weighted estimate bounds the supremum of each error. On the full space its pointwise integral is
\(\int f(x-y)\phi(x)\,dx=(\widetilde f*\phi)(y)\), which is Schwartz by (2.3). The tail bound proves convergence of the finite-cube integrals to this particular test in every seminorm.

Pass the Riemann sums and then the tails through \(u\) using its \(P_N\) bound. On the scalar side the integrand \(u(f(x-\cdot))\phi(x)\) is absolutely integrable by (2.5). This proves the exact pairing
\[
(u*f)(\phi)=u(\widetilde f*\phi).
\tag{2.6}
\]
For \(\psi\in\mathcal S\), absolute Fubini, bounded by \(\|f\|_1\|\psi\|_1\), gives
\[
\begin{aligned}
F((Ff)\psi)(y)
&=\int f(z)F\psi(y+z)\,dz\\
&=(\widetilde f*F\psi)(y).
\end{aligned}
\]
Both sides are Schwartz functions. Hence (2.6) and the transpose convention yield
\[
F(u*f)(\psi)
=u(\widetilde f*F\psi)
=u(F((Ff)\psi))
=((Ff)(Fu))(\psi).
\]
Multiplication by \(Ff\) is legitimate on \(\mathcal S\): the product rule bounds \(P_a((Ff)\psi)\) by a constant times \(P_a(Ff)P_a(\psi)\). This proves (2.2) with its exact normalization.

Finally the test map \(L_f:\phi\mapsto\widetilde f*\phi\) is continuous by (2.3), and takes bounded sets to bounded sets. Formula (2.6) therefore gives continuity in the weak topology and, for every bounded \(B\),
\[
q_B(u*f)=q_{L_f B}(u).
\]
This is continuity in the strong topology. The same reasoning and the proved test continuity of \(F,G\) give \(q_B(Fu)=q_{FB}(u)\) and \(q_B(Gu)=q_{GB}(u)\), so both Fourier maps are also strongly continuous. \(\square\)

## Compact Fourier support is exactly the fixed-point condition

**Theorem 3.1 (spectral cutoffs).** For \(u\in\mathcal S'(\mathbb R^n)\), the following are equivalent:

1. Some \(f\in\mathcal S\) satisfies \(u=u*f\).
2. The distributional support of \(Fu\) is compact.

In this case \(u\) has a smooth representative whose derivatives all obey polynomial bounds with one common exponent.

**Proof.** Suppose \(u=u*f\). Lemma 2.1 gives \((1-Ff)Fu=0\). Since \(Ff\) is Schwartz, it tends to zero at infinity. Choose \(R\) so that \(|Ff|<1/2\) for \(|\xi|>R\). The reciprocal of \(1-Ff\) is smooth there: for a nonzero complex-valued smooth function \(h\), \(1/h=\overline h/|h|^2\) is smooth by the real quotient rule. For every compact test supported in this exterior,
\[
(Fu)(\psi)=((1-Ff)Fu)\bigl(\psi/(1-Ff)\bigr)=0.
\]
Thus \(\operatorname{supp}Fu\subset\{|\xi|\le R\}\).

Conversely let \(K=\operatorname{supp}Fu\) be compact. A compact smooth cutoff \(\eta\) equal to one on a neighborhood of \(K\) exists by the supplied bump construction. Put \(f=G\eta\); then \(f\in\mathcal S\) and \(Ff=\eta\). On compact tests \((1-\eta)Fu=0\): the product test vanishes near the support, and U021 B0's finite-partition support argument applies. Multiplication by \(1-\eta\) is continuous on \(\mathcal S\) by the product rule. The cutoff density proved in Theorem 1.1 therefore extends the zero identity to all Schwartz tests. Lemma 2.1 now gives \(F(u*f)=Fu\), and Fourier inversion gives \(u=u*f\). Its smoothing and common growth exponent follow from (2.5).

If \(K\) is empty, the same finite-partition argument makes \(Fu=0\) on all compact tests; density and inversion give \(u=0\), for which \(f=0\) suffices. \(\square\)

The cutoff must be one on a neighborhood of the spectral support; matching a value at a point need not preserve derivatives of a point mass. Solution 4 checks the exact derivative correction.

## A measure whose Fourier order is large on a small ball

**Theorem 4.1 (escaping masses).** Let \(M\subset\mathbb R^n\) be unbounded and \(m\) any integer. There is a tempered distribution \(u\) supported in \(M\), of local order zero, whose Fourier transform has order greater than \(m\) in the unit ball.

**Proof.** Set \(r=\max(m,0)+1\). Inductively choose \(x_j\in M\) with \(|x_1|\ge2\) and \(|x_{j+1}|\ge2|x_j|\), using unboundedness at each step. The points escape every compact set, hence form a closed locally finite set: a convergent sequence among them must eventually lie in a compact ball, which contains only finitely many points. Define
\[
u=\sum_{j\ge1}|x_j|^r\delta_{x_j}.
\tag{4.1}
\]
On a compact test only finitely many positive masses occur, so its pairing is bounded by a constant times the test supremum. On Schwartz tests the sum converges absolutely, since
\[
\begin{aligned}
|u(\phi)|
&\le P_{r+1}(\phi)\sum_j |x_j|^r\langle x_j\rangle^{-r-1}\\
&\le P_{r+1}(\phi)\sum_j2^{-j}.
\end{aligned}
\tag{4.2}
\]
This is a tempered distribution of local order zero. Every chosen point is detected by a bump supported away from the other points, so its exact support is the selected set, contained in \(M\). The set \(M\) itself need not be closed.

Choose real nonnegative \(\eta\in C_c^\infty(B(0,1/4))\) with \(\int\eta>0\), and set \(\chi=\eta*\widetilde\eta\). Ordinary differentiation and compact support give a smooth test supported in a compact subset of \(B(0,1/2)\). Reflection in the integral, using that \(\eta\) is real, gives
\[
F\widetilde\eta=\overline{F\eta},\qquad
F\chi=|F\eta|^2\ge0,\qquad F\chi(0)=(\int\eta)^2>0.
\]
The convolution identity here was proved in Lemma 2.1. Use the tests
\(\psi_j(\xi)=e^{ix_j\cdot\xi}\chi(\xi)\).
They all have this one fixed compact support in the unit ball. Directly,
\(F\psi_j(y)=F\chi(y-x_j)\), so
\[
\begin{aligned}
(Fu)(\psi_j)
&=\sum_l|x_l|^r|F\eta(x_l-x_j)|^2\\
&\ge |x_j|^r(\int\eta)^2.
\end{aligned}
\tag{4.3}
\]
The series is absolutely convergent for each \(j\) by (4.2) on the Schwartz test \(F\psi_j\). Its nonnegative terms cannot cancel.

If \(m\ge0\) and the restriction of \(Fu\) had order at most \(m\), its finite-order estimate on this fixed compact support would give
\[
|(Fu)(\psi_j)|\le C\max_{|\alpha|\le m}\|\partial^\alpha\psi_j\|_\infty
\le C_{\chi,m}\langle x_j\rangle^m.
\]
The last inequality is the finite product rule, since each differentiated exponential contributes a component of \(x_j\). It contradicts (4.3), because \(r=m+1\) and \(|x_j|\to\infty\). If \(m<0\), (4.3) shows that the restriction is nonzero; its ordinary distributional order is nonnegative, hence greater than \(m\). \(\square\)

## Exercises

**Exercise 1 (foundation).** For every real \(a\), prove that \(e^{a x^4+i e^{x^6}}\) has a tempered extension. Give an explicit finite-seminorm bound using bounded functions and one derivative.

**Exercise 2 (foundation).** For a compact smooth cutoff \(\eta=1\) on the unit ball and zero outside the radius-two ball, prove, for integers \(a\ge0\) and \(R\ge1\),
\[
P_a((1-\eta(x/R))\psi)\le C_aR^{-1}P_{a+1}(\psi).
\]
Deduce convergence uniformly on every bounded Schwartz family.

**Exercise 3 (intermediate).** On the line construct a Schwartz \(f\) fixing \(1+e^{3ix}\) by convolution. Explain why no Schwartz factor fixes \(\delta_0+\delta_0'\).

**Exercise 4 (intermediate).** Let \(h\in C_c^\infty(\mathbb R)\) satisfy \(h(3)=1\), \(h'(3)=2\), and put \(f=Gh\). Compute \(u-u*f\) for \(u(x)=xe^{3ix}\). Determine the necessary and sufficient conditions on a general \(h\) to fix this \(u\).

**Exercise 5 (advanced).** For \(t>0\), let
\[
h_t(x)=(4\pi t)^{-n/2}e^{-|x|^2/(4t)}.
\]
Determine all tempered distributions with \(u=u*h_t\), in every dimension. Use the complete point-support proof in the angular foundations A2–A3 and the Gaussian proof in the Fourier foundation F3.

**Exercise 6 (intermediate).** In \(\mathbb R^2\), take \(x_j=(3^j,(-1)^j)\) and \(u=\sum_{j\ge1}|x_j|^5\delta_{x_j}\). Prove a \(P_6\) bound and show that \(Fu\) has order greater than four in the unit ball.

**Exercise 7 (intermediate).** Solve \(Fu=\partial_{\xi_1}^2\delta_{(2,-1)}\) on \(\mathbb R^2\). Give a Schwartz factor fixing \(u\) and determine its local distributional order and its exact Fourier order.

**Exercise 8 (advanced).** Prove that \(e^{5x^2+i e^{x^2}}\) has a tempered extension by performing six integrations by parts on compact tests. Give an absolutely convergent formula on Schwartz tests; the bounded first-primitive argument is insufficient here.

## Solutions

**Solution 1.** On \(|x|>1\) put
\[
A_a(x)=\frac{x^{-5}}{6i}e^{a x^4-x^6}.
\]
For any fixed real \(a\), \(a x^4-x^6\le-|x|^6/2\) for sufficiently large \(|x|\). The exponential-series estimate in Theorem 1.1 bounds both \(A_a,A_a'\), including every polynomial factor produced by differentiation. Set
\[
B_a=\chi A_a e^{i e^{x^6}},\qquad
D_a=-(\chi A_a)'e^{i e^{x^6}},\qquad
H_a=(1-\chi)e^{a x^4+i e^{x^6}}.
\]
Then \(f=B_a'+D_a+H_a\). The formula
\[
T_a(\psi)=-\int B_a\psi'+\int D_a\psi+\int H_a\psi
\]
has bound
\((\pi\|B_a\|_\infty+\pi\|D_a\|_\infty+\|H_a\|_1)P_2(\psi)\).
It agrees with every original compact-test integral by integration by parts. Cutoff density gives uniqueness for positive, zero and negative \(a\).

**Solution 2.** In the product rule, the term with no cutoff derivative is supported where \(|x|\ge R\) and is bounded, after multiplication by \(\langle x\rangle^a\), by \(R^{-1}P_{a+1}(\psi)\). A cutoff derivative of total order \(j>0\) is supported in \(R\le|x|\le2R\), has magnitude at most \(C_jR^{-j}\), and multiplies a derivative of \(\psi\) of order at most \(a\). The extra weight gives
\(C_jR^{-j-1}P_{a+1}(\psi)\le C_jR^{-1}P_{a+1}(\psi)\).
Summing the finitely many multiindex terms proves the bound. The right side tends uniformly to zero when \(\psi\) ranges over a bounded Schwartz family. In particular every fixed continuous tempered functional has uniform cutoff convergence on that family.

**Solution 3.** Fourier foundation F5 gives \(F1=2\pi\delta_0\). More generally inversion at \(\lambda\) gives, for a Schwartz test,
\[
\int e^{i\lambda x}F\psi(x)\,dx=2\pi\psi(\lambda),
\]
an absolutely convergent integral since \(F\psi\) is Schwartz. Hence \(F(e^{i\lambda x})=2\pi\delta_\lambda\). Choose \(\eta\in C_c^\infty\) equal to one near \(\{0,3\}\), and take \(f=G\eta\). Theorem 3.1 proves the required fixed point. Direct integration confirms
\[
(e^{i\lambda\cdot}*f)(x)=e^{i\lambda x}Ff(\lambda).
\]
On the other hand \(F\delta_0=1\), \(F\delta_0'=i\xi\), by the proved transpose differentiation identity. The density \(1+i\xi\) is nonzero at every real point; a phase-adjusted local bump detects it. Its support is the entire line, so Theorem 3.1 excludes any fixing Schwartz factor.

**Solution 4.** Since \(f\) is Schwartz, the integrals with \(f\) and \(yf(y)\) converge absolutely. They give
\[
(u*f)(x)=e^{3ix}\left(xh(3)-\int yf(y)e^{-3iy}\,dy\right).
\]
Differentiation of \(h=Ff\), justified in Fourier foundation F2, gives
\(\int yf(y)e^{-3iy}dy=i h'(3)\).
Thus
\[
(u*f)(x)=(x-2i)e^{3ix},\qquad u-u*f=2ie^{3ix}.
\]
For arbitrary \(h\), the difference is
\(e^{3ix}[x(1-h(3))+i h'(3)]\).
It vanishes for every \(x\) exactly when \(h(3)=1\), \(h'(3)=0\), by evaluating this affine polynomial at two values of \(x\). Equivalently \(Fu=2\pi i\delta_3'\), and direct test differentiation gives
\[
(1-h)\delta_3'=(1-h(3))\delta_3'+h'(3)\delta_3.
\]
This verifies the derivative sign and the failure of value-only matching.

**Solution 5.** Fourier foundation F3, formula (F10) and product integration, gives \(Fh_t(\xi)=e^{-t|\xi|^2}\). Lemma 2.1 turns the equation into
\[
(1-e^{-t|\xi|^2})v=0,\qquad v=Fu.
\]
The multiplier is positive away from zero. The compact reciprocal-test argument of Theorem 3.1 gives \(\operatorname{supp}v\subset\{0\}\). The fully proved angular A3 theorem writes
\[
v=\sum_{|\alpha|\le N}c_\alpha\partial^\alpha\delta_0.
\]
This equality on compact tests also holds on Schwartz tests, since both sides are tempered and compact tests are dense.

The inverse of a point derivative can be checked directly, with no formal kernel pairing:
\[
G(\partial^\alpha\delta_\zeta)(\psi)
=(-1)^{|\alpha|}\partial^\alpha(G\psi)(\zeta)
=(2\pi)^{-n}\int(-ix)^\alpha e^{ix\cdot\zeta}\psi(x)\,dx.
\]
The derivative under this integral is justified by polynomially weighted absolute integrability. At \(\zeta=0\) the formula makes \(u\) a polynomial.

The exact factorization is
\[
1-e^{-t|\xi|^2}=|\xi|^2 b_t(\xi),
\qquad b_t(\xi)=\int_0^t e^{-s|\xi|^2}\,ds>0.
\]
FTC proves it, and differentiation under this finite smooth integral proves that \(b_t\) is smooth. Its reciprocal is smooth near zero. Multiply the equation locally by that reciprocal; since \(v\) is supported at zero, this proves \(|\xi|^2v=0\) on all compact tests. Density extends the equality to \(\mathcal S\). The proved identity \(F(\Delta u)=-|\xi|^2Fu\) makes the polynomial \(u\) harmonic.

Conversely a harmonic polynomial has Fourier transform supported at zero by the point-derivative formula and invertibility, and satisfies \(|\xi|^2Fu=0\). The factorization implies the original multiplier equation near zero; away from zero \(Fu\) vanishes. Compact-test localization followed by Schwartz density proves the equality globally, so \(u=u*h_t\).

All answers are therefore precisely the harmonic polynomials. In dimension one, comparing coefficients in \(u''=0\) gives the affine functions. In every dimension at least two, the polynomials \(\operatorname{Re}(x_1+i x_2)^d\), \(d=0,1,\ldots\), are nonzero harmonic polynomials of every degree: the two second derivatives cancel by \(1+i^2=0\), and the coefficient of \(x_1^d\) is one. They are independent of any additional coordinates.

**Solution 6.** The selected points are closed and locally finite because their first coordinates tend to infinity. Since \(|x_j|\ge3^j\),
\[
|u(\phi)|
\le P_6(\phi)\sum_j|x_j|^5\langle x_j\rangle^{-6}
\le P_6(\phi)\sum_j3^{-j}.
\]
This defines a positive tempered measure of local order zero. Use the same autocorrelation \(\chi\) and tests \(\psi_j=e^{ix_j\cdot\xi}\chi\) as in Theorem 4.1. Then
\[
(Fu)(\psi_j)\ge|x_j|^5(\int\eta)^2,
\qquad
\max_{|\alpha|\le4}\|\partial^\alpha\psi_j\|_\infty
\le C\langle x_j\rangle^4.
\]
Their supports are all in one compact subset of the unit ball. The ratio tends to infinity, excluding every order-four bound there.

**Solution 7.** The direct inverse point-derivative formula from Solution 5, with \(\zeta=(2,-1)\), gives
\[
u(x)=-\frac{x_1^2}{(2\pi)^2}e^{i(2x_1-x_2)}.
\]
Fourier inversion proves existence and uniqueness. A compact smooth \(\eta\) equal to one near \(\zeta\), and \(f=G\eta\), fixes \(u\) by Theorem 3.1.

The smooth function has local distributional order zero:
\[
|u(\phi)|\le\left(\int_K|u(x)|\,dx\right)\|\phi\|_\infty
\quad(\operatorname{supp}\phi\subset K).
\]
Its Fourier transform has order at most two by its defining second-derivative pairing. To exclude order one, choose a compact smooth \(\rho\) with \(\partial_1^2\rho(0)\ne0\), and set
\[
\psi_\varepsilon(\xi)=\varepsilon^2
\rho((\xi-\zeta)/\varepsilon),\qquad 0<\varepsilon\le1.
\]
These tests have common compact support, their \(C^1\) norms tend to zero, and their second derivative at \(\zeta\) is the same nonzero constant. Thus the exact Fourier order is two.

**Solution 8.** Put \(\Phi=e^{x^2}\). For smooth test amplitudes vanishing near \(|x|\le1\), define on the tails
\[
Lh=-\frac{d}{dx}\left(\frac{h}{i\Phi'}\right),
\qquad \Phi'=2xe^{x^2}.
\]
For a compact such amplitude, integration by parts in
\((e^{i\Phi})'=i\Phi'e^{i\Phi}\) gives
\(\int e^{i\Phi}h=\int e^{i\Phi}Lh\).
The amplitude and all its iterates remain smooth, compactly supported and zero near the origin, so six repetitions give
\[
\int e^{5x^2+i\Phi}\chi\psi
=\int e^{i\Phi}L^6(\chi e^{5x^2}\psi).
\tag{5.1}
\]
All boundary terms vanish for the compact test.

On either tail where \(\chi=1\), write
\[
L^r(e^{5x^2}\psi)
=e^{(5-r)x^2}\sum_{\ell=0}^r c_{r,\ell}(x)\psi^{(\ell)}(x).
\]
Here \(c_{0,0}=1\), and coefficients with indices outside \(0\le\ell\le r\) are zero. Division by \(2ix e^{x^2}\) and differentiation give the explicit recurrence
\[
c_{r+1,\ell}
=-\frac1{2i}\left[
(x^{-1}c_{r,\ell})'
+2(4-r)c_{r,\ell}
+x^{-1}c_{r,\ell-1}\right].
\]
It proves by induction that every coefficient is a finite Laurent polynomial. All additional terms involving a derivative of \(\chi\) have smooth compactly supported coefficients, because those derivatives lie in \(1\le|x|\le2\), away from division by zero.

At \(r=6\), every tail coefficient is \(e^{-x^2}\) times a Laurent polynomial on \(|x|>1\), hence integrable by the exponential-series estimate, or the explicit Gaussian bounds in Fourier foundation F3. The compact transition coefficients are integrable too. Therefore
\[
T(\psi)=
\int (1-\chi)e^{5x^2+i\Phi}\psi
+\int e^{i\Phi}L^6(\chi e^{5x^2}\psi)
\]
is absolutely convergent on Schwartz tests, with the second integral interpreted by the just-derived finite sum of derivatives of \(\psi\) and integrable coefficients. It obeys
\[
|T(\psi)|\le C\max_{0\le\ell\le6}\|\psi^{(\ell)}\|_\infty
\le CP_6(\psi).
\]
Equation (5.1) identifies its value with the original function on compact tests. The cutoff-density proof gives uniqueness. No intermediate unbounded primitive is assumed to be tempered.

## Free sources and exact proof dependencies

- Semyon Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, 2 October 2026 version, [free author notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), §§11.1.2–11.2.3, pp.120–130. The actual Fourier seminorm, Gaussian, inversion and transpose proofs were read and compared. The source leaves several test-space operations as exercises and uses a dual-density argument for Proposition 11.25; the complete weighted estimates and direct integrated-test proof used here are supplied in Lemma 2.1.
- [Schwartz and Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, supplies all Fourier operations, constants and inversion. [Angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A2–A3, supplies the full Taylor estimate and point-supported finite-jet proof. [U008](order-positivity-and-limits.md), Proposition 1.2, and [U021](convolution-as-addition-of-supports.md), B0–B2 and Theorems 1.1–2.1, supply the compact-test and local convolution inputs.
- The exact oscillatory growth criterion, global convolution and topology estimates, spectral equivalence, escaping-mass order obstruction, heat-fixed classification and all eight solutions are proved in this lesson. The external free reference replaces no programme proof.
