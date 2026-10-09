# Boundary operators of every nonnegative real order

This companion retains the complete Section 14 proof of AN03-U032, *Totally characteristic operators on the half space*. Original author: Claude Opus 5.5 (Anthropic), September 2026; editorial additions: Codex, September 2026; both CC0. Exact prerequisite connections and the analytic justifications below: AN-04 course-writing task and OpenAI Codex, 5 October 2026, CC0. The source's seventeen numbered mathematical displays remain unchanged. Its original illustration is retained with the final output label corrected: \(v\) is an operator output, while \(F_{f,g}(m)\) is the scalar pairing \((v,g)\).

The approved mathematical antecedent is Hörmander III, 2007 eBook, ISBN 978-3-540-49938-1, Section 18.3. Reading, proof construction and ordinary citation are valid. The complete proof uses the exact programme results linked below; the book citation is not a proof substitute.

## Exact earlier proofs

Original section numbers below refer to the four components of the [local boundary calculus](../20261005-local-boundary-calculus/boundary-tests-and-lacunary-symbols.md). Its [kernel component](../20261005-local-boundary-calculus/resolved-corner-kernels.md) proves the full residual bounds; its [operator component](../20261005-local-boundary-calculus/boundary-adjoints-composition-and-distributions.md) proves complete composition, adjoints and actual distribution actions; its [continuity component](../20261005-local-boundary-calculus/boundary-bounds-and-conormal-action.md) proves the order-zero estimates for every real index, full quotient duality, homogeneous finite-seminorm bounds and the residual no-gain obstruction.

The half-space companion H4 proves the right-half-plane logarithm, real one-sided Laplace kernel and exact supported isometries. The [Fourier proof](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md) and [measure proof](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) supply inversion, Plancherel, Fubini and dominated differentiation. The elementary exponential and real integration proofs are in the [earlier stationary-phase foundations](../20261004-free-stationary-phase/exponential-prerequisite-completions.md). Each earlier component retains its own licence.

## Analytic facts used in the strip argument

All scalar holomorphic functions below are constructed with continuous real derivatives of every order and the Cauchy--Riemann equations. No regularity theorem for initially nonsmooth complex differentiable functions is needed. On the right half-plane use
\[
 L(h+i\tau)=\tfrac12\log(h^2+\tau^2)+i\arctan(\tau/h),\qquad h>0.
 \tag{PB1}
\]
The direct derivatives are \(L_h=(h+i\tau)^{-1}\) and \(L_\tau=i(h+i\tau)^{-1}\). The real logarithm, trigonometric functions and inverse tangent here are those proved in the earlier elementary foundations; the same branch and its derivative are proved in H4. Thus \(L\) is smooth and satisfies Cauchy--Riemann, and \(\exp(zL)\) is entire in \(z\). Its parameter derivatives are \(L^j\exp(zL)\).

Here is the exact rectangle maximum estimate needed below. If a complex function \(G=u+iv\) is \(C^2\) on a neighborhood of a closed rectangle and satisfies Cauchy--Riemann in it, differentiating those equations gives \(\Delta u=\Delta v=0\), and hence
\[
 \Delta |G|^2=4\bigl(u_x^2+u_y^2\bigr)=4|G'|^2\ge0.
 \tag{PB2}
\]
For \(\delta>0\), the real function \(|G|^2+\delta(x^2+y^2)\) has strictly positive Laplacian. Its maximum on the compact rectangle cannot occur in the interior: the second derivative test along the two coordinate lines would give a nonpositive Laplacian there. The maximum is therefore on the boundary. Its boundary value is at most \(\sup_{\partial R}|G|^2+\delta\sup_{\partial R}(x^2+y^2)\). Letting \(\delta\downarrow0\) gives \(\sup_R|G|\le\sup_{\partial R}|G|\). This proves the precise maximum principle used for the smooth scalar pairing in (PS13). Products with the displayed entire exponential normalizations satisfy the same hypotheses.

## 14. Positive order on both original Sobolev spaces

The following proof extends the zero-order bounds without changing the compressed operator or its distribution action.

### The original theorem and spaces

Let \(m\ge0\), \(s\in\mathbb R\), and let
\(a\in S^m_{\mathrm{la}}\) take values in
\(L(\mathbb C^p,\mathbb C^q)\), with \(p,q\) fixed finite positive integers.
Use the original symbol estimates
\[
 |\partial_\xi^\alpha\partial_x^\beta a(x,\xi)|
 \le C_{\alpha\beta\nu}
 (1+|\xi|)^{m-|\alpha|}(1+x_n)^{-\nu},
 \quad x_n\ge0,\quad \nu\ge0,
 \qquad
 \operatorname{supp}\mathcal F_n a\subset[-1,\infty).
 \tag{PS1}
\]
The forward Fourier kernel is \(e^{-ix\cdot\xi}\), \(D=-i\partial\), and
\[
 a^\flat(x,\xi)=a(x,\xi',x_n\xi_n)\quad(x_n\ge0),\qquad
 a^\flat(x,\xi)=0\quad(x_n<0),\qquad
 T_a u=(2\pi)^{-n}\int e^{ix\cdot\xi}a^\flat(x,\xi)\widehat u(\xi)\,d\xi .
 \tag{PS2}
\]
The full-space norm is
\(\|u\|_{(s)}^2=(2\pi)^{-n}\int(1+|\xi|^2)^s|\widehat u(\xi)|^2\,d\xi\).
The supported space is the closed subspace of this \(H_{(s)}\) consisting of
distributions supported in \(\{x_n\ge0\}\). The restricted space is its
original ambient restriction quotient, with the infimum norm over
\(H_{(s)}\) extensions. Neither space is replaced.

We prove
\[
 T_a:\dot H_{(s)}(\overline{\mathbb R}{}^n_+;\mathbb C^p)
       \longrightarrow
       \dot H_{(s-m)}(\overline{\mathbb R}{}^n_+;\mathbb C^q),
 \qquad
 T_a:\overline H_{(s)}(\mathbb R^n_+;\mathbb C^p)
       \longrightarrow
       \overline H_{(s-m)}(\mathbb R^n_+;\mathbb C^q)
 \tag{PS3}
\]
continuously. For each fixed \(m,s\), a finite sum \(p_{m,s}(a)\) of the
original symbol seminorms bounds both operator norms. The maps agree with
the original distribution action in Theorem 9.1.

### Exact integer-order decomposition

Fix the same normal convolution \(\rho\) as Lemma 4.4, including its inverse
Fourier convention, \(\widehat\rho=1\) near zero and
\(\operatorname{supp}\widehat\rho\subset(-1/2,1)\).
For an integer \(M\ge1\) and \(a\in S^M_{\mathrm{la}}\), put
\[
 w_j=\frac{\xi_j a}{1+|\xi|^2},\quad
 a_j=(w_j)_\rho\quad(1\le j\le n),\qquad
 a_0=a-\sum_{j=1}^n\xi_j a_j
     =\frac{a}{1+|\xi|^2}
       +\sum_{j=1}^n\xi_j(w_j-a_j).
 \tag{PS4}
\]
Every \(w_j\in S^{M-1}_+\). Lemma 4.4 gives
\(a_j\in S^{M-1}_{\mathrm{la}}\) and
\(w_j-a_j\in S^{-\infty}_+\), continuously with all the stipulated
seminorms. Thus \(a_0\in S^{M-2}_+\subset S^{M-1}_+\). It is lacunary because
the first definition in (PS4) is a difference of lacunary symbols.
The residual sum in the second definition is retained exactly; its separate
summands need not themselves be lacunary.

Multiplication of a symbol by \(x_n\) preserves every original order and
lacunarity: a weighted seminorm uses one extra \(x_n\)-decay seminorm, and
differentiating \(x_n\) produces only a derivative of \(a_j\).
On the original test spaces the exact left-quantization identity is
\[
 T_a=\sum_{j<n}T_{a_j}D_j+
       T_{x_n a_n}D_n+T_{a_0}
     =\sum_{j<n}T_{a_j}D_j+
       x_n T_{a_n}D_n+T_{a_0}.
 \tag{PS5}
\]
In the normal term the uncompressed derivative frequency is \(\xi_n\);
the left factor \(x_n\) supplies precisely the original compression
\(x_n\xi_n\). No derivative is commuted past this factor.

The zero-order theorem is the induction base, for every real \(s\), on both
spaces. Suppose the bound of order \(M-1\) has been proved for every \(s\).
Each ambient \(D_j:H_{(s)}\to H_{(s-1)}\) has norm at most one, since
\(|\xi_j|^2\le1+|\xi|^2\). Derivatives preserve supported distributions and
descend continuously to the restriction quotient. Hence every derivative
term in (PS5) maps index \(s\) to \(s-M\). The term \(T_{a_0}\) maps index
\(s\) to \(s-(M-1)\), which embeds into index \(s-M\) with norm at most one.
The same inequality descends to quotient norms. This proves both integer
bounds, with finite original symbol seminorm control.

The identities initially hold on supported or restricted Schwartz test
functions. Proposition 10.2(a) gives density for every real index,
and Theorem 9.1 gives their weakly continuous distribution actions.
Consequently the bounded extensions retain precisely (PS5) and the original
distribution action; no boundary delta term is removed by an arbitrary
extension. The supported proof uses functions smooth and flat on the boundary
before taking density.

### A support-preserving exact change of Sobolev index

Set
\[
 \ell(\xi)=\sqrt{1+|\xi'|^2}+i\xi_n,\qquad
 -\frac{\pi}{2}<\arg\ell<\frac{\pi}{2},\qquad
 \Lambda_+^z=\mathcal F^{-1}\ell(\xi)^z\mathcal F,
 \quad \ell^z=\exp(z\log\ell).
 \tag{PS6}
\]
In dimension one the first term is \(1\), with its zero-dimensional Fourier
factor. The full factor \(\ell\) is retained. In particular
\[
 |\ell|^2=1+|\xi'|^2+\xi_n^2=1+|\xi|^2,\qquad
 |\ell^z|=(1+|\xi|^2)^{\operatorname{Re}z/2}
           e^{-\operatorname{Im}z\,\arg\ell}.
 \tag{PS7}
\]
It follows by the original Plancherel norm that
\[
 \|\Lambda_+^z u\|_{(r-\operatorname{Re}z)}
 \le e^{\pi|\operatorname{Im}z|/2}\|u\|_{(r)}.
 \tag{PS8}
\]
For real \(z\) this is equality. The inverse is the literal multiplier
\(\Lambda_+^{-z}\), so the real-index map is an isometry onto the full
\(H_{(r-z)}\), and it will be an isometry of the supported subspaces once
support is proved. All multipliers have smooth derivatives of polynomial
growth; they act continuously on \(\mathcal S,\mathcal S'\).
On each bounded real strip their Schwartz operator seminorms grow at most
as a polynomial in \(|\operatorname{Im}z|\) times
\(e^{\pi|\operatorname{Im}z|/2}\). This follows by differentiating the full
\(\ell^z\): every derivative is a finite sum of derivatives of \(\ell\),
powers of \(\ell^{-1}\), and polynomial factors in \(z\).
Parameter derivatives add powers of \(\log\ell\), bounded by any fixed
positive power of \(1+|\xi|\), which proves holomorphy on the test spaces.

Here is a proof of support, with the transform constants. For
\(\operatorname{Re}q>0\), the elementary Laplace identity gives
\[
 \ell^{-q}=\frac1{\Gamma(q)}
       \int_0^\infty t^{q-1}
          e^{-t\sqrt{1+|\xi'|^2}}e^{-it\xi_n}\,dt .
 \tag{PS9}
\]
We prove this identity for every complex \(q\) with
\(\operatorname{Re}q>0\), without leaving an identity theorem as a
prerequisite. Write \(\ell=h+i\tau\), \(h>0\), and
\(I(\tau)=\int_0^\infty t^{q-1}e^{-(h+i\tau)t}\,dt\), where
\(t^{q-1}=\exp((q-1)\log t)\). The absolute near-zero bound is
\(t^{\operatorname{Re}q-1}\), and the exponential dominates every
required large-\(t\) factor. Dominated differentiation and integration
by parts of \(t^qe^{-(h+i\tau)t}\), whose two boundary values vanish,
give
\[
 I'(\tau)=-\frac{iq}{h+i\tau}I(\tau),\qquad
 I(0)=h^{-q}\Gamma(q).
 \tag{PB3}
\]
The derivative in (PB1) shows that \((h+i\tau)^q I(\tau)\) has
derivative zero on the real line. Its value at zero is \(\Gamma(q)\).
Thus \(I(\tau)=\Gamma(q)(h+i\tau)^{-q}\) with precisely the indicated
branch. The nonzero denominator is proved next. The same dominated
bounds with powers of \(\log t\) justify every complex-\(q\) derivative
on compact subsets of \(\operatorname{Re}q>0\).

For clarity, the gamma denominator here is nonzero. Integration by parts
in the beta integral gives
\[
 \int_0^1 u^{q-1}(1-u)^N\,du
 =\frac{N!}{q(q+1)\cdots(q+N)}.
\]
Multiply by \(N^q\) and put \(t=Nu\). The integrand is bounded in modulus by
\(t^{\operatorname{Re}q-1}e^{-t}\) on \(0<t<N\), so dominated convergence
gives \(\Gamma(q)\). Rewriting the finite product, its limit is
\[
 \Gamma(q)=\frac1q\exp\!\left(
   -\gamma q+\sum_{k\ge1}
        \left[\frac qk-\log\left(1+\frac qk\right)\right]\right),
 \quad
 \gamma=\lim_{N\to\infty}\left(\sum_{k=1}^N\frac1k-\log N\right).
\]
For the real limit, \(H_N-\log N\) is positive by comparison
with \(\int_1^N dx/x\), and is decreasing because
\(\log(1+1/N)>1/(N+1)\). Hence it converges by completeness of the
real numbers. For the complex series, the derivative of the right
half-plane logarithm gives
\[
 \log(1+w)-w=-w^2\int_0^1\frac{t}{1+tw}\,dt,\qquad |w|<1.
 \tag{PB4}
\]
For \(|w|\le1/2\) its modulus is at most \(|w|^2\). Apply this with
\(w=q/k\) for all sufficiently large \(k\), bounding the finite initial
part separately. Thus the displayed series is absolutely convergent,
with its actual \(O(k^{-2})\) tail. Each logarithm is in the
right half-plane branch, so the displayed value is nonzero. This proves the
division in (PS9), including complex \(q\).

Let
\[
 E_t(x')=(2\pi)^{-(n-1)}
       \int e^{ix'\cdot\xi'}e^{-t\sqrt{1+|\xi'|^2}}\,d\xi'.
\]
In dimension one \(E_t=e^{-t}\). The inverse Fourier kernel of (PS9) is
\[
 K_{-q}(x',x_n)=\frac1{\Gamma(q)}
        \int_0^\infty t^{q-1}E_t(x')\delta(x_n-t)\,dt .
 \tag{PS10}
\]
This is a tempered distribution: near zero the tested integrand has the
integrable bound \(C t^{\operatorname{Re}q-1}\), and at infinity the factor
\(e^{-t}\), with finitely many test seminorms, makes it integrable.
The kernel is supported in \(x_n\ge0\). The tangential Fourier factor is
exactly \((2\pi)^{-(n-1)}\); inverse transformation of \(e^{-it\xi_n}\) is
the displayed delta, without an extra factor.

For arbitrary \(z\in\mathbb C\), choose an integer \(k\ge0\) with
\(k>\operatorname{Re}z\). Then
\(\ell^z=\ell^k\ell^{-(k-z)}\).
The second multiplier has the kernel (PS10); the first is the finite
operator
\((\sqrt{1+|D'|^2}+\partial_n)^k\).
Tangential multipliers and normal derivatives preserve normal support.
Thus \(\Lambda_+^z\) preserves support for every \(z\). More explicitly, its
action on a Schwartz function supported in the positive half space has
that support by (PS10) and the finite operator; the one-sided mollification
and compact cutoff approximation in Theorem 9.1(e) extends this conclusion
to every supported tempered distribution. All the operators are continuous
on \(\mathcal S'\), so the support is retained in the weak limit. The same
argument applies to \(-z\).

It follows that, for real \(r\),
\[
 \Lambda_+^{-r}:\dot H_{(0)}\longrightarrow\dot H_{(r)},
 \qquad
 \Lambda_+^{r}:\dot H_{(r)}\longrightarrow\dot H_{(0)}
 \tag{PS11}
\]
are inverse isometries, with exactly the original full-space norms.
This proves the support-preserving index change rather than assuming that
the multiplier \((1+|D|^2)^{r/2}\) preserves half-space support.

### The original analytic symbol family and the strip estimate

Fix \(0<m<M\), with \(M\) an integer, and retain
\[
 b_z=a(1+|\xi|^2)^{(z-m)/2},\qquad
 A_z=(b_z)_\rho+(a-a_\rho),\qquad 0\le\operatorname{Re}z\le M.
 \tag{PS12}
\]
The residual contribution is present for every \(z\); \(A_m=a\) exactly.
For each \(z\), \(A_z\in S^{\operatorname{Re}z}_{\mathrm{la}}\).
Frequency differentiation of the displayed scalar factor yields finite
polynomials in \(z-m\), the full powers of \(1+|\xi|^2\), and the original
frequency coordinates. Hence each indicated symbol seminorm is bounded by
\(C(1+|\operatorname{Im}z|)^L p(a)\), uniformly on this real strip, with
a finite original seminorm \(p\). The convolution and residual bounds of
Lemma 4.4 retain the same property. Holomorphy holds in any fixed slightly
larger symbol order, such as \(S^{M+1}_+\): parameter derivatives produce
powers of \(\log(1+|\xi|^2)\), which the one extra order bounds.
No assertion of order-\(M\) holomorphy at its borderline is needed.

For \(f,g\) in the original supported Schwartz spaces of dimensions \(p,q\),
respectively, set
\[
 F_{f,g}(z)=
  \left(\Lambda_+^{s-z}T_{A_z}\Lambda_+^{-s}f,g\right)_{L^2}.
 \tag{PS13}
\]
The expression acts in the supported Schwartz space at every
stage. The multipliers preserve that space by their full Schwartz
estimates and the kernel support proof. The local Theorem 5.1 gives
all boundary jets of \(T_{A_z}u\); all are zero when the input is
supported Schwartz and hence flat on the boundary. Extension by zero
is therefore Schwartz, with every seminorm bounded by that theorem.
These bounds are continuous in \(A_z\) in a fixed sufficiently large
symbol order, including the extra order for each prescribed finite
number of parameter derivatives. Difference quotients converge by
the exponential Taylor formula and those same weighted estimates;
the product rule proves complex differentiability of the composition
and of its scalar pairing. All real derivatives are continuous.
This is holomorphic on the strip, continuous on its closed boundary,
and \(C^2\) on a neighborhood of each finite closed rectangle.
The preceding test-space estimates and Theorem 5.1 bound its
growth throughout the strip by
\(C_{f,g}(1+|\operatorname{Im}z|)^L
 e^{\pi|\operatorname{Im}z|/2}\).
On the two boundary lines, the proved integer bounds, (PS8) and (PS11) give
\[
 |F_{f,g}(i\tau)|
 \le C_0(1+|\tau|)^L e^{\pi|\tau|/2}
        p(a)\|f\|_2\|g\|_2,\qquad
 |F_{f,g}(M+i\tau)|
 \le C_M(1+|\tau|)^L e^{\pi|\tau|/2}
        p(a)\|f\|_2\|g\|_2 .
 \tag{PS14}
\]
Take a single finite seminorm \(p\) large enough for both endpoints.
The zero-order norm depends continuously on finitely many original symbol
seminorms, as proved in Section 10. Rescaling a symbol by their sum gives
a linear bound in that sum; the integer induction uses only continuous
linear symbol operations. Thus the stated \(p(a)\) bounds are homogeneous,
including \(p(a)=0\).

For any fixed \(\varepsilon>0\), multiply \(F\) by
\(\exp(\varepsilon(z-m)^2)\). Its boundary bounds now have finite constants
\(C'_0,C'_M\), since
\((1+|\tau|)^L e^{\pi|\tau|/2-\varepsilon\tau^2}\) is bounded.
Its modulus tends to zero on the horizontal edges of large rectangles in
the strip. Dividing it by
\(p(a)\|f\|_2\|g\|_2 C'_0\) and multiplying by
\(\exp[-(z/M)\log(C'_M/C'_0)]\) makes the two vertical-edge bounds at most
one. The proved rectangle maximum principle (PB2), followed by the expanding
limit, therefore gives
\[
 |F_{f,g}(m)|
 \le (C'_0)^{1-m/M}(C'_M)^{m/M}
      p(a)\|f\|_2\|g\|_2 .
 \tag{PS15}
\]
The zero-seminorm or zero-test-function case is immediate and does not
require dividing by zero. This is the required strip estimate with its
growth control proved.

Since \(A_m=a\), duality in the supported \(L^2\) space and density of its
Schwartz subspace show that
\(\Lambda_+^{s-m}T_a\Lambda_+^{-s}\) is bounded on supported \(L^2\).
Conjugating by the exact isometries (PS11) gives the supported bound (PS3)
for this real \(m\), with finite original seminorm control.
Together with the integer case it covers every \(m\ge0\) and every real
\(s\). The bounded extension agrees with the original supported distribution
action by test-space density and its weak continuity.

### The full restriction quotient

Theorem 7.3 gives
\(a^\dagger\in S^m_{\mathrm{la}}\), continuously and conjugate-linearly,
with the original reversed vector dimensions. Apply the supported result
at the index \(m-s\):
\[
 T_{a^\dagger}:\dot H_{(m-s)}(\mathbb C^q)
      \longrightarrow\dot H_{(-s)}(\mathbb C^p).
 \tag{PS16}
\]
For the supported/restricted duality of Proposition 10.2(b),
\[
 |(T_a u,v)|=|(u,T_{a^\dagger}v)|
 \le C p_{m,s}(a)
       \|u\|_{\overline H_{(s)}}\|v\|_{\dot H_{(m-s)}} .
 \tag{PS17}
\]
The antidual of \(\dot H_{(m-s)}\) is exactly
\(\overline H_{(s-m)}\) with its original quotient norm, so (PS17) proves
the restricted bound, without choosing or identifying a supported extension
of the restricted input. Density and Theorem 9.1(d) retain the original
quotient distribution action. This completes both assertions of (PS3).

For \(m<0\), the same zero-order membership proves boundedness at the same
index, but the argument above does not assert a gain of \(-m\). Theorem 12.1 gives nonzero residual examples forbidding every such gain.
The full residual term, and this exact limitation, remain part of the
calculus.

[![Figure PS-F1. PS6–PS11 keeps the full multiplier sqrt(1+|xi'|^2)+i xi_n, the original weighted norm, Gamma(q), the inverse Fourier factor and normal kernel support, with Re q>0. PS12–PS15 uses integer M>m and epsilon>0, retaining the residual in A_z. The strip is a schematic with 0<m<M. All four spaces and arrows have their original vector dimensions; PS16–PS17 gives the restriction quotient. The last vector is v = Lambda_+^(s-m) T_a Lambda_+^(-s) f, and F_(f,g)(m) = (v,g). The figure source is figures/positive_order_halfspace.py.](figures/positive_order_halfspace.png)](figures/positive_order_halfspace.svg)

