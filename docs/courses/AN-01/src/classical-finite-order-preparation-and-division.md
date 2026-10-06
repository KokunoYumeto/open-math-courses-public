# Classical finite-order preparation and division

*Written and assembled by GPT-6.1 Sol (OpenAI), Ultra, October 2026. The new exposition, proofs, worked examples, and eight exercises with complete solutions are dedicated to CC0 1.0 to the extent rights exist. Referenced human and course components retain their own authorship and terms.*

*Prerequisite integration and source/proof self-check by GPT-6 Astra (OpenAI), Ultra, October 2026. Historical authorship and each component’s terms are preserved.*

The conclusions have different hypotheses and different uniqueness properties:

- For a holomorphic function of complex variables with distinguished order \(k\ge1\), the linked complete analytic provider gives a unique monic preparation and unique quotient and polynomial remainder. The variable, coefficient, and unit map is stated below.
- The finite Newton identities recover holomorphic polynomial coefficients from fixed-contour power sums, with repeated and zero roots counted correctly. Distinguished order alone gives vanishing coefficients; stronger graded coefficient bounds require the extra ambient-order hypothesis.
- For every fixed \(k\ge1\), the proof here constructs complex-linear smooth division operators for the generic monic polynomial, through colliding and nonreal roots. It proves every real coefficient and auxiliary-parameter derivative estimate, with the stated finite losses.
- For a complex-valued smooth function of real variables with distinguished order \(k\ge1\), the separate complete order-one component and the higher-degree construction here give a monic smooth preparation and division of every smooth dividend on a neighborhood inside its actual original domain. Real data admit real factors. Existence is proved; smooth preparation and division are not asserted unique.
- For dividends supplied on a prescribed common domain, the cutoff and output neighborhood can be fixed in advance. Unrelated local germs instead use their own supplied-domain intersections. The order-one complex smooth result is reused from the separately owned complete companion component identified below.

The teaching order follows the mechanism. First identify the exact analytic theorem being reused and recover its symmetric coefficients without choosing variable root labels. Next construct uniform division on thin strips. Then sum entire Fourier pieces with every differentiated tail. Finally cancel the smooth remainders by a finite-dimensional implicit map, preserve the unit, and substitute on each actual dividend domain. The existing order-one proof is reused separately, with its preparation consequence stated before the higher-degree construction. Eight graded problems and complete solutions test these steps.

Equation tags use prefixes \(H\) for the analytic statements, \(N\) for the finite symmetric-coefficient receiver, \(S\) for thin-strip division, \(F\) for Fourier summation, \(P\) for smooth preparation, and \(O\) for the order-one receiving consequence. Identical notation introduced in a later stage retains that stage's stated domain.

The complete [integral Taylor proof](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods) supplies the finite-order remainders used here, including signed increments, complex-valued functions, directional derivatives and uniform bounds for all required derivatives on compact neighborhoods.

## The holomorphic theorems and their exact by-reference map

Let \(n\ge0\), let \((t,z)\in\mathbb C\times\mathbb C^n\), and let \(f\) be holomorphic on an actual open neighborhood of \((0,0)\). Suppose, for a fixed integer \(k\ge1\),

\[
\partial_t^j f(0,0)=0\quad(0\le j<k),\qquad
\lambda=\frac{\partial_t^k f(0,0)}{k!}\ne0.
\tag{H1}
\]

Then there are holomorphic germs \(a_0,\ldots,a_{k-1}\) at \(z=0\) and a holomorphic unit \(c\) at \((0,0)\) such that

\[
f(t,z)=c(t,z)P(t,z),\qquad
P(t,z)=t^k+\sum_{j=0}^{k-1}a_j(z)t^j,\qquad
a_j(0)=0,\qquad c(0,0)=\lambda.
\tag{H2}
\]

The monic polynomial and unit are unique as germs. For every holomorphic dividend \(g\) on an actual supplied neighborhood of the same mark, there are unique holomorphic germs \(q\) and \(r_0,\ldots,r_{k-1}\) such that

\[
g(t,z)=q(t,z)f(t,z)+\sum_{j=0}^{k-1}t^jr_j(z).
\tag{H3}
\]

The identity holds after shrinking within the intersection of the actual divisor and dividend domains. For a bounded family on one prescribed common adapted polydisc, the linked division proof also gives a common smaller polydisc and bounds depending on the fixed divisor and polydiscs, rather than on the individual dividend. Absorbing the holomorphic unit uses its bounded reciprocal on a still smaller closed polydisc.

These are received by reference from Jean-Pierre Demailly's complete [preparation argument](../prerequisites/U011-free-foundations/weierstrass-preparation-U070.md#preparation-by-the-zeros-in-one-fibre) and [Cauchy division argument](../prerequisites/U011-free-foundations/weierstrass-preparation-U070.md#division-finite-generation-and-elementary-algebra). The following table fixes the notation and the quotient for the original divisor; the general analytic proof is not duplicated here.

| This receiver | Linked analytic provider |
|---|---|
| Complex base \(z\in\mathbb C^n\) and distinguished variable \(t\) | \(z'\in\mathbb C^n\) and \(w\), respectively |
| Divisor \(f(t,z)\), distinguished order \(k\) | \(g(z',w)\), distinguished order \(s=k\) |
| \(P(t,z)=t^k+\sum_{j<k}a_j(z)t^j\) | \(P(z',w)=w^s+\sum_{\ell=1}^s A_\ell(z')w^{s-\ell}\), with its descending coefficient named \(a_\ell\) in that source |
| Ascending coefficient \(a_j(z)\) | Descending coefficient \(A_{k-j}(z')\), \(0\le j<k\) |
| Holomorphic unit \(c(t,z)\) | Unit \(u(z',w)\) in \(g=uP\) |
| Dividend \(g(t,z)\) in (H3) | The dividend named \(f(z',w)\) in the provider's division section |
| Quotient \(\widetilde q\) for division by \(P\), polynomial remainder \(\sum_{j<k}t^jr_j\) | Its Cauchy quotient \(q\) and polynomial \(R(z',w)\) |
| Quotient \(q\) in (H3), for division by the original \(f=cP\) | Provider's polynomial quotient divided by its unit: \(\widetilde q/c=q_{\mathrm{provider}}/u\) |

The hypothesis (H1) concerns the order on the distinguished axis. It does not say that the total ambient Taylor order of \(f\) is \(k\). The additional estimate \(A_\ell(z)=O(|z|^\ell)\), or equivalently \(a_j(z)=O(|z|^{k-j})\), requires that additional ambient-order assumption. The symmetric-coefficient argument below proves the precise receiving calculation and the corresponding root bound with that extra hypothesis.

## The separately owned smooth order-one component

Assume \(f\in C^\infty(U_f;\mathbb C)\) on an actual neighborhood of the origin in \(\mathbb R\times\mathbb R^n\), with \(f(0,0)=0\) and \(\lambda=\partial_tf(0,0)\ne0\). The separate [complete complex smooth order-one component](../prerequisites/U011-free-foundations/AN04-order-one-division.md) is the existing AN-04 proof, retained with its ownership and component notice.

That proof constructs a smooth complex function \(T(x)\), and proves an exact smooth identity on real variables,

\[
f(t,x)=(t-T(x))U(t,x),\qquad T(0)=0,\qquad
U(0,0)=\partial_tf(0,0)=\lambda\ne0.
\tag{O1}
\]

The construction includes the flat antiholomorphic-error correction and the nonvanishing of \(U\) after shrinking. No real root graph for a complex-valued divisor is assumed. Its immediate preparation consequence is

\[
a_0(x)=-T(x),\qquad P(t,x)=t+a_0(x),\qquad
c(t,x)=U(t,x),\qquad f=cP,\qquad a_0(0)=0.
\tag{O2}
\]

This is a monic degree-one preparation with a nonzero smooth unit. For each dividend \(g\) on its actual supplied domain, the same complete component proves \(g=(t-T)V+S(x)\) after the required domain intersection. Therefore

\[
g(t,x)=f(t,x)\frac{V(t,x)}{U(t,x)}+S(x).
\tag{O3}
\]

The unit reciprocal is smooth on the shrunken domain. The complex order-one theorem is received in full by reference; its almost-analytic construction is not reauthored here.

For the real-valued option, suppose \(f\) is real. The linked complete real finite-dimensional implicit construction gives a real smooth \(T(x)\), with \(T(0)=0\) and \(f(T(x),x)=0\). Choose a product neighborhood so that \(T(x)\), \(t\), and the segment between them stay in the divisor's actual domain. The fundamental theorem of calculus gives the exact real smooth factor
\[
c_f(t,x)=\int_0^1
\partial_tf(T(x)+s(t-T(x)),x)\,ds,\qquad
f(t,x)=(t-T(x))c_f(t,x),\qquad c_f(0,0)=\lambda.
\tag{O4}
\]
The finite integral is smooth by differentiation under the integral on compact parameter neighborhoods. By continuity, shrink so that \(|c_f-\lambda|<|\lambda|/2\); it is then a real nonvanishing unit.

For a real smooth dividend \(g\), choose the product inside its actual domain as well, with the segment still inside that domain, and put
\[
V_g(t,x)=\int_0^1
\partial_tg(T(x)+s(t-T(x)),x)\,ds,\qquad
g(t,x)=f(t,x)\frac{V_g(t,x)}{c_f(t,x)}+g(T(x),x).
\tag{O5}
\]
This gives real quotient and remainder, and real preparation with coefficient \(-T(x)\). The same fixed product works for dividends actually supplied on one common domain; unrelated local germs use their individual intersections. All these conclusions concern smooth existence.

## Symmetric coefficients and the analytic receiver

Zeros of a holomorphic family can meet, and individual zeros need not admit holomorphic names. Their symmetric functions can nevertheless be holomorphic. A fixed contour computes the power sums without choosing names; a finite polynomial identity then recovers every coefficient of the monic polynomial. This section supplies that elementary step in the existing Weierstrass preparation proof.

We use the already proved one-variable local power series and isolated-zero multiplicity, fixed-contour integration with holomorphic parameters, winding numbers and the finite-pole residue theorem. We do not prove preparation or division again. The complex variables are \((z',w)\in\mathbb C^d\times\mathbb C\), with \(d\ge0\), and the distinguished zero order is an integer \(k\ge1\).

### A finite identity that does not distinguish repeated roots

For any list \(\lambda_1,\ldots,\lambda_k\in\mathbb C\), repetitions allowed, define

\[
S_\ell=\sum_{i=1}^k\lambda_i^\ell\quad(\ell\ge1),\qquad
e_0=1,\qquad
e_j=\sum_{1\le i_1<\cdots<i_j\le k}
\lambda_{i_1}\cdots\lambda_{i_j}\quad(1\le j\le k).
\tag{N1}
\]

The indices in the definition of \(e_j\) select occurrences in the list, even when their values coincide. Set \(e_j=0\) for \(j>k\). The finite Newton identities are

\[
j e_j=\sum_{\ell=1}^j(-1)^{\ell-1}e_{j-\ell}S_\ell,
\qquad 1\le j\le k.
\tag{N2}
\]

**Proof.** Work first in the polynomial ring
\(R=\mathbb C[\lambda_1,\ldots,\lambda_k]\), treating the \(\lambda_i\) as indeterminates. Introduce a formal variable \(X\) and the finite polynomial

\[
E(X)=\prod_{i=1}^k(1+\lambda_iX)
     =\sum_{j=0}^k e_jX^j.
\tag{N3}
\]

Each factor has constant coefficient one, so it is invertible in \(R[[X]]\), with formal inverse
\(\sum_{m\ge0}(-\lambda_iX)^m\). Formal differentiation of the finite product gives

\[
\begin{aligned}
E'(X)
&=\sum_{i=1}^k\lambda_i\prod_{h\ne i}(1+\lambda_hX)\\
&=E(X)\sum_{i=1}^k\frac{\lambda_i}{1+\lambda_iX}\\
&=E(X)\sum_{\ell\ge1}(-1)^{\ell-1}S_\ell X^{\ell-1}.
\end{aligned}
\tag{N4}
\]

Equality of the coefficients of \(X^{j-1}\) is exactly (N2). There is no analytic convergence or division by a root. To make the argument entirely finite, truncate each geometric inverse after degree \(k-1\) and work modulo \(X^k\); its product with \(1+\lambda_iX\) is one modulo \(X^k\). This determines all the coefficients used in (N2). Finally specialize the indeterminates to the given complex numbers. Polynomial identities remain valid when values coincide or vanish. \(\square\)

Since division by the positive integer \(j\) is allowed in \(\mathbb C\), (N2) recursively expresses every \(e_j\), \(1\le j\le k\), as a polynomial with rational coefficients in \(S_1,\ldots,S_j\). For indices not exceeding \(k\),

\[
e_1=S_1,\qquad
e_2=\frac{S_1^2-S_2}{2},\qquad
e_3=\frac{S_1^3-3S_1S_2+2S_3}{6}.
\tag{N5}
\]

For the descending coefficients of

\[
P(w)=\prod_{i=1}^k(w-\lambda_i)
    =w^k+A_1w^{k-1}+\cdots+A_k,
\tag{N6}
\]

we have \(A_0=1\) and \(A_j=(-1)^je_j\). Thus the equivalent coefficient recursion is

\[
jA_j+\sum_{\ell=1}^j A_{j-\ell}S_\ell=0,
\qquad 1\le j\le k.
\tag{N7}
\]

For example, where the indices do not exceed \(k\), \(A_1=-S_1\), \(A_2=(S_1^2-S_2)/2\), and
\(A_3=(-S_1^3+3S_1S_2-2S_3)/6\). These signs correspond to the factors \(w-\lambda_i\).

### What the fixed contour counts

Let \(g(z',w)\) be holomorphic near \((0,0)\) and suppose

\[
\partial_w^j g(0,0)=0\quad(0\le j<k),\qquad
\partial_w^k g(0,0)\ne0.
\tag{N8}
\]

The one-variable power series gives
\(g(0,w)=w^kh_0(w)\), where \(h_0\) is holomorphic and \(h_0(0)\ne0\). Choose \(r>0\) and \(\eta>0\) so that \(g\) is defined on a neighborhood of a closed product containing \(|w|\le r+\eta\), and \(h_0\) has no zero there. After shrinking to a connected base polydisc \(B\) about zero, compactness and continuity give a common positive lower bound for \(|g(z',w)|\) on

\[
z'\in B,\qquad r-\eta\le |w|\le r+\eta,
\tag{N9}
\]

with \(0<\eta<r\). The contour \(\Gamma=\{|w|=r\}\) is positively oriented. Every fibre is nonidentically zero and has finitely many zeros inside \(\Gamma\): isolated zeros cannot accumulate in a compact subdisk, and the collar (N9) excludes accumulation at its boundary.

For \(j\ge0\), set

\[
\mathscr S_j(z')=
\frac1{2\pi i}\int_\Gamma
w^j\frac{\partial_wg(z',w)}{g(z',w)}\,dw.
\tag{N10}
\]

If \(\lambda\) is a zero of the fixed fibre of multiplicity \(m\), its local power series gives
\(g(z',w)=(w-\lambda)^m h(w)\), with \(h(\lambda)\ne0\). Hence

\[
\frac{\partial_wg}{g}
=\frac{m}{w-\lambda}+\frac{h'}h.
\tag{N11}
\]

The second term is holomorphic near \(\lambda\). For \(j\ge1\), write
\(w^j=\lambda^j+(w-\lambda)H_j(w)\), with \(H_j\) a polynomial. Therefore

\[
\operatorname{Res}_{w=\lambda}
\left(w^j\frac{\partial_wg}{g}\right)=m\lambda^j.
\tag{N12}
\]

For \(j=0\) the weight is the constant one and the residue is \(m\), including at \(\lambda=0\); no value of \(0^0\) is needed.

Apply the already proved finite-pole residue theorem in the disk \(|w|<r+\eta\). All poles are these finitely many zeros, all lie inside \(\Gamma\), and the contour has winding one at each of them and winding zero outside the disk. Consequently

\[
\mathscr S_0(z')=\sum_\lambda m(\lambda,z'),\qquad
\mathscr S_j(z')=\sum_\lambda m(\lambda,z')\lambda^j
\quad(j\ge1).
\tag{N13}
\]

On each compact base subset, the denominator on the fixed contour is bounded away from zero, while \(g\), \(\partial_wg\) and the contour weights have compact bounds. The fixed-contour holomorphic integral theorem therefore makes every \(\mathscr S_j\) jointly holomorphic in \(z'\). In particular \(\mathscr S_0\) is continuous and integer valued. It is constant on the connected base, and its value at zero is the multiplicity \(k\). Thus every fibre has exactly \(k\) zeros counted with multiplicity. For \(d=0\), the base is a single point and the same assertion is immediate.

At any one fibre, list its \(k\) zeros with repetitions. Formula (N13) identifies \(\mathscr S_j\) with the power sums in (N1). Recursion (N7), with \(S_j=\mathscr S_j(z')\), then defines holomorphic coefficients \(A_j(z')\), and the pointwise identity (N6) shows that the resulting polynomial has exactly this root multiset. No labels are required to vary continuously, smoothly or holomorphically with the base. The existing preparation proof supplies the subsequent holomorphic unit and its uniqueness; the existing division proof supplies the quotient and remainder.

In the linked analytic provider's notation, \(s=k\), \(w=t\), \(z'=z\), and \(g(z',w)=f(t,z)\) after this variable identification. Its descending coefficient \(a_j\) is \(A_j\). If the receiving statement instead writes
\(P(t,z)=t^k+\sum_{\nu=0}^{k-1}a_\nu(z)t^\nu\), the exact conversion is

\[
a_\nu(z)=A_{k-\nu}(z),\qquad 0\le\nu<k.
\tag{N14}
\]

### Vanishing coefficients and stronger order estimates

At the base origin the only fibre zero is zero, with multiplicity \(k\). Hence \(\mathscr S_j(0)=0\) for every \(j\ge1\). Recursion (N7) gives \(A_j(0)=0\) for \(1\le j\le k\). This conclusion uses only the distinguished-variable condition (N8).

The stronger estimate \(A_j(z')=O(|z'|^j)\) requires an additional hypothesis: the total ambient Taylor order of \(g\) at \((0,0)\) is \(k\). Under that hypothesis the first homogeneous term is \(cw^k+H_k(z',w)\), where \(c=\partial_w^k g(0,0)/k!\ne0\) and every monomial of \(H_k\) contains a base variable. Fix a norm on the base. If \(|w|\ge C|z'|\), the finite sum \(H_k\) has modulus at most a constant times \(C^{-1}|w|^k\). The Taylor remainder is bounded by a constant times \((|z'|+|w|)^{k+1}\). Choose \(C\) large and the neighborhood small; the sum of both error bounds is then less than \(|c||w|^k/2\). Thus a nonzero fibre root in that neighborhood must satisfy \(|w|<C|z'|\).

All selected fibre roots lie in this neighborhood after another base shrinking: for each sufficiently small \(\rho>0\), the central fibre is nonzero on the compact annulus \(\rho\le|w|\le r\), and continuity preserves that fact on a smaller base. Taking symmetric products of the root bound gives
\(|A_j(z')|\le\binom{k}{j}C^j|z'|^j\). The additional ambient-order assumption has not been deduced from (N8).

### Examples and a worked calculation

**A triple repeated root.** For \(g(z,w)=(w-z)^3\), the root list is \(z,z,z\), so \(\mathscr S_j=3z^j\) for \(j\ge1\), and \(\mathscr S_0=3\). Equations (N5) and (N7) give

\[
A_1=-3z,\qquad A_2=3z^2,\qquad A_3=-z^3.
\]

Repeated roots cause no difficulty. Here both the distinguished and ambient orders are three, and the stronger estimates hold.

**A collision without holomorphic root labels.** For \(g(z,w)=w^2-z\), choose a fixed small circle and \(|z|<r^2/2\). Then \(|w^2-z|\ge r^2/2\) on \(|w|=r\). The two roots have total multiplicity two, including the double root at \(z=0\). Their power sums are \(\mathscr S_1=0\) and \(\mathscr S_2=2z\). Consequently \(A_1=0\) and \(A_2=-z\). Neither root can be a holomorphic function on a neighborhood of zero: a holomorphic square root of \(z\) would have an integer zero order whose double is one. Nevertheless both coefficients are holomorphic. Distinguished order two gives \(A_2(0)=0\), but the ambient order is one and \(A_2\) is not \(O(|z|^2)\).

**Worked example.** A degree-three fibre has roots \(\alpha,\alpha,\beta\), with occurrences counted separately. Recover its monic coefficients from its first three power sums, including the cases \(\alpha=\beta\) and \(\alpha=0\). What does the weighted contour assign to the repeated root?

**Calculation.** The power sums are \(S_j=2\alpha^j+\beta^j\). Equations (N5) and (N7) give

\[
A_1=-(2\alpha+\beta),\qquad
A_2=\alpha^2+2\alpha\beta,\qquad
A_3=-\alpha^2\beta.
\]

Thus \(P(w)=(w-\alpha)^2(w-\beta)\). If \(\alpha\ne\beta\), the weighted residue at \(\alpha\) is \(2\alpha^j\) for \(j\ge1\), and two for \(j=0\). If \(\alpha=\beta\), the actual multiplicity is three and the residue is \(3\alpha^j\), or three for \(j=0\). At a zero root, positive-degree moments contribute zero although its zero-count contribution remains its full multiplicity. Every formula remains valid in all these cases.

## Division through colliding roots on thin strips

The difficult coefficient values include collisions and nonreal roots. We avoid naming roots as functions of the coefficients. At each coefficient value we choose a rectangle in the dividend's actual strip, keep that rectangle fixed on a small coefficient ball, and combine the resulting linear division formulas with a scaled smooth partition. The constants below are independent of the strip width and of the dividend.

### Statement and actual domains

Fix an integer \(k\ge1\). Write \(b_j=u_j+iv_j\), use the Euclidean norm on \(b\in\mathbb C^k\simeq\mathbb R^{2k}\), and put

\[
\Omega=\left\{b:\sum_{j=0}^{k-1}|b_j|<1\right\},\qquad
p(t,b)=t^k+\sum_{j=0}^{k-1}b_jt^j.
\tag{S1}
\]

For \(0<\varepsilon\le1\), the common dividend and quotient domains are

\[
D_\varepsilon=\{z\in\mathbb C:|\operatorname{Re}z|<3,
\ |\operatorname{Im}z|<\varepsilon\},\qquad
E_\varepsilon=\{t\in\mathbb C:|\operatorname{Re}t|<3/2,
\ |\operatorname{Im}t|<\varepsilon/4\}.
\tag{S2}
\]

There are complex-linear maps, depending on \(k,\varepsilon\) and the fixed geometric choices, which send every bounded holomorphic \(g\) on \(D_\varepsilon\) to

\[
q^\varepsilon[g]\in C^\infty(E_\varepsilon\times\mathbb C^k),\qquad
r_j^\varepsilon[g]\in C^\infty(\mathbb C^k),\quad 0\le j<k.
\]

Here smoothness in \(t\) means smoothness in its two real coordinates; the quotient is also holomorphic in \(t\). They satisfy

\
g(t)=p(t,b)q^\varepsilon[g
        +\sum_{j=0}^{k-1}t^j r_j^\varepsilong
\quad(t\in E_\varepsilon,\ b\in\Omega).
\tag{S3}
\]

For every integer \(\alpha\ge0\) and real-coordinate multiindex \(\beta\in\mathbb N^{2k}\), there are constants depending only on \(k,\alpha,\beta\) such that, with \(M=\sup_{D_\varepsilon}|g|\),

\
\left|\partial_t^\alpha\partial_b^\beta q^\varepsilon[g\right|
\le C_{k,\alpha,\beta}M
\varepsilon^{-\alpha-1-k(|\beta|+1)},
\tag{S4}
\]

\
\left|\partial_b^\beta r_j^\varepsilon[g\right|
\le C_{k,\beta}M\varepsilon^{-k(|\beta|+1)}.
\tag{S5}
\]

The bounds hold on the whole displayed output domains; the identity (S3) is required only on \(\Omega\). The symbol \(\partial_t\) in (S4) is the holomorphic derivative. On the real axis it is the ordinary real \(t\)-derivative; general real derivatives in the complex \(t\)-plane have the same bound, up to a harmless factor, by the Cauchy–Riemann equations. There is no assertion that the maps vary smoothly with \(\varepsilon\), or that all unrelated dividend germs possess the domain (S2). The lemma applies to a dividend actually defined on that domain, or to an explicitly supplied smaller/scaled version of it.

The maps can be chosen to respect conjugation. Thus, if \(g(\bar t)=\overline{g(t)}\), the quotient and remainder coefficients are real when \(t\) and \(b\) are real. Reality is asserted on the real coefficient subspace, not for arbitrary complex \(b\).

If the dividend is bounded and holomorphic on the full strip
\(S_\varepsilon=\{z:|\operatorname{Im}z|<\varepsilon\}\), the quotient extends to the full reduced strip \(S_{\varepsilon/4}\), with the same uniform estimates and equality (S3) there. In particular the equality holds for every real \(t\). The proof of this full-strip version, which is the later Fourier construction's interface, is given below; it does not impose a fictitious global domain on a local germ.

The width restriction in these uniform estimates is essential. For an arbitrary supplied width \(\varepsilon>0\), put \(\varepsilon_*=\min(\varepsilon,1)\) and apply the construction after restricting the input to \(D_{\varepsilon_*}\), or to \(S_{\varepsilon_*}\) in the full-strip case. The output domains are then \(E_{\varepsilon_*}\) and \(S_{\varepsilon_*/4}\), respectively; the latter still contains every real evaluation point. The quotient and remainder losses become \(\max(1,\varepsilon^{-\alpha-1-k(|\beta|+1)})\) and \(\max(1,\varepsilon^{-k(|\beta|+1)})\). A bound with the uncapped negative powers and constants independent of every \(\varepsilon>0\) would be false: for \(g=1\) and \(b=0\), (S3) at \(t=0\) forces \(r_0=1\), whereas \(C\varepsilon^{-k}\) tends to zero as the width tends to infinity. All later frequency pieces use \(0<\varepsilon\le1\) and the exact losses (S4)–(S5).

### Root bound and a rectangle avoiding every root

Fix \(b^0\in\Omega\). Every root \(\lambda\) of \(p(\cdot,b^0)\) has \(|\lambda|<1\). Indeed, if \(|\lambda|\ge1\), then

\[
|\lambda|^k
=\left|\sum_{j=0}^{k-1}b_j^0\lambda^j\right|
\le\sum_j|b_j^0|\,|\lambda|^{k-1}
<|\lambda|^{k-1},
\]

which is impossible. Ordinary complex polynomial factorization therefore gives

\[
p(z,b^0)=\prod_{\ell=1}^k(z-\lambda_\ell),
\tag{S6}
\]

with repetitions recording multiplicities. Only this pointwise list is used.

Set

\[
c_k=\frac1{8(k+1)}.
\tag{S7}
\]

We first choose a height \(h_+\in[\varepsilon/2,3\varepsilon/4]\) whose distance from every \(\operatorname{Im}\lambda_\ell\) is at least \(c_k\varepsilon\). Take the distinct root heights lying in that closed interval, arrange them in increasing order, and add the two endpoints. The resulting at most \(k+1\) consecutive intervals have total length \(\varepsilon/4\); one has length at least \(\varepsilon/[4(k+1)]\). Choose its midpoint. Its distance from the two ends of that interval is at least \(c_k\varepsilon\). Root heights in the original interval lie beyond those ends, and root heights outside it lie beyond an original endpoint, so the same distance bound holds for all root heights. A height equal to an original endpoint is already one of the cuts; repeated heights merely reduce the number of intervals.

Apply the same argument to \(-\operatorname{Im}\lambda_\ell\) to choose \(h_-\in[\varepsilon/2,3\varepsilon/4]\) with

\[
|h_+-\operatorname{Im}\lambda_\ell|\ge c_k\varepsilon,
\qquad
|-h_--\operatorname{Im}\lambda_\ell|\ge c_k\varepsilon.
\tag{S8}
\]

Let \(\Gamma(b^0,\varepsilon)\) be the positively oriented boundary of

\[
\{-2\le\operatorname{Re}z\le2,
\ -h_-\le\operatorname{Im}z\le h_+\}.
\tag{S9}
\]

Its entire closed interior is contained in \(D_\varepsilon\). Its length is
\(8+2(h_++h_-)\le11\), and every contour point satisfies \(|z|<3\).
On the horizontal edges (S8) gives \(|z-\lambda_\ell|\ge c_k\varepsilon\).
On the vertical edges,
\(|z-\lambda_\ell|\ge|\operatorname{Re}z-\operatorname{Re}\lambda_\ell|>1\ge c_k\varepsilon\).
Consequently

\[
|p(z,b^0)|\ge(c_k\varepsilon)^k
\quad(z\in\Gamma(b^0,\varepsilon)).
\tag{S10}
\]

Every \(t\in E_\varepsilon\) lies strictly inside the rectangle. Its distance from a horizontal edge is at least \(\varepsilon/4\); its distance from a vertical edge is at least \(1/2\ge\varepsilon/2\). Thus

\[
|z-t|\ge\varepsilon/4
\quad(z\in\Gamma(b^0,\varepsilon),\ t\in E_\varepsilon).
\tag{S11}
\]

The contour need not surround every nonreal root. The Cauchy identity will surround the evaluation point \(t\). This is sufficient for division on \(E_\varepsilon\); it is the reason a thin strip is available even when some polynomial roots lie far from the real axis.

### Coefficient balls on which the contour stays valid

Define

\[
K_k=\sqrt{k}\,3^{k-1},\qquad
\rho_k=\frac{c_k^k}{2K_k},\qquad
a_k=\frac{c_k^k}{2}.
\tag{S12}
\]

For \(|z|<3\), the Cauchy–Schwarz inequality gives

\[
|p(z,b)-p(z,b^0)|
\le\sum_{j=0}^{k-1}|b_j-b_j^0|\,3^j
\le K_k\|b-b^0\|.
\tag{S13}
\]

Therefore, on the Euclidean ball

\[
V(b^0,\varepsilon)=
\{b:\|b-b^0\|<\rho_k\varepsilon^k\},
\tag{S14}
\]

the fixed contour chosen at \(b^0\) satisfies

\[
|p(z,b)|\ge a_k\varepsilon^k
\quad(z\in\Gamma(b^0,\varepsilon)).
\tag{S15}
\]

This follows directly by subtracting (S13) from (S10); it does not require continuous root labels or a quantitative root-continuity theorem. Since
\(\sqrt{k}\rho_k=c_k^k/(2\,3^{k-1})\le1/32\) and \(\varepsilon\le1\), every \(b\) in this ball also obeys

\[
\sum_j|b_j|
\le\sum_j|b_j^0|+\sqrt{k}\|b-b^0\|<33/32<2.
\tag{S16}
\]

Thus these balls have radius exactly a fixed positive multiple of \(\varepsilon^k\), and all their numerator coefficient bounds are uniform. They are allowed to extend outside \(\Omega\); (S15) is valid throughout the ball.

### An explicit scaled coefficient partition

Let \(d=2k\). Choose the fixed one-variable bump

\[
\theta(s)=
\begin{cases}
\exp[-1/(1-s^2)],&|s|<1,\\
0,&|s|\ge1,
\end{cases}
\qquad
\psi(v)=\prod_{i=1}^d\theta(v_i).
\tag{S17}
\]

This bump is smooth. Inside \((-1,1)\), each derivative of \(\theta\) is a finite sum of a polynomial in \(s\), a power of \((1-s^2)^{-1}\), and the exponential in (S17). Every such expression tends to zero at \(s=\pm1\), because \(u^N e^{-u}\to0\) as \(u\to\infty\) for each fixed \(N\). Successive zero extensions therefore have continuous derivatives of every order. The product \(\psi\) is positive on \([-1/2,1/2]^d\) and has support \([-1,1]^d\).

Put

\[
\delta_\varepsilon=\frac{\rho_k}{4\sqrt d}\varepsilon^k,
\qquad
S(v)=\sum_{m\in\mathbb Z^d}\psi(v-m),
\qquad
\chi_m^\varepsilon(b)
=\frac{\psi(b/\delta_\varepsilon-m)}{S(b/\delta_\varepsilon)}.
\tag{S18}
\]

At every \(v\), at most \(3^d\) summands have support containing \(v\): each coordinate permits at most three integers at distance at most one. The sum is locally finite and smooth. Choose a nearest integer in every coordinate; the corresponding translate is at least
\(s_0=\min_{[-1/2,1/2]^d}\psi>0\). Thus \(S\ge s_0\). Every derivative of \(S\) is uniformly bounded by \(3^d\) times a fixed bump-derivative bound. Differentiating \(S(1/S)=1\), and inducting on the derivative order, shows that every derivative of \(1/S\) is uniformly bounded: the highest derivative is divided by \(S\ge s_0\), and all other terms use lower derivatives already bounded. Leibniz's rule in (S18), followed by the dilation, gives

\[
\sum_m\chi_m^\varepsilon=1,\qquad
0\le\chi_m^\varepsilon\le1,\qquad
|\partial_b^\beta\chi_m^\varepsilon|
\le B_{k,\beta}\varepsilon^{-k|\beta|}.
\tag{S19}
\]

These bounds hold on the full real coefficient space and are uniform in \(m,\varepsilon\). Their support overlap is at most \(3^d\).

Retain only indices \(m\) for which the open cube where
\(\psi(b/\delta_\varepsilon-m)>0\) meets \(\Omega\). For each retained index choose once and for all a point \(b^m\) in that intersection, and use its contour \(\Gamma_m=\Gamma(b^m,\varepsilon)\) and coefficient ball \(V_m=V(b^m,\varepsilon)\). If \(b\) lies in the closed support of \(\chi_m^\varepsilon\), both \(b\) and \(b^m\) are in the same closed cube, so

\[
\|b-b^m\|\le2\sqrt d\,\delta_\varepsilon
=\frac{\rho_k}{2}\varepsilon^k.
\tag{S20}
\]

In particular the whole support, including its boundary, lies a positive distance inside \(V_m\). Every omitted summand vanishes identically on \(\Omega\), so the retained sum is still one there. The retained family is finite for each \(\varepsilon\), because \(\Omega\) is bounded and only a bounded set of lattice centers can have such an intersection. The number of patches need not be uniform in \(\varepsilon\); the uniform bound on their overlap is what will control the estimates.

### Fixed-contour division on each patch

For \(t\in E_\varepsilon\), \(b\in V_m\), set

\
Q_m[g=\frac1{2\pi i}
\int_{\Gamma_m}\frac{g(z)}{(z-t)p(z,b)}\,dz,
\tag{S21}
\]

\
R_m[g=\frac1{2\pi i}
\int_{\Gamma_m}
\frac{p(z,b)-p(t,b)}{z-t}\frac{g(z)}{p(z,b)}\,dz.
\tag{S22}
\]

All denominators are nonzero on the contour by (S11) and (S15), and the dividend is holomorphic on an open neighborhood of the entire closed rectangle. Adding \(p(t,b)Q_m\) to (S22) leaves the Cauchy integral of \(g(z)/(z-t)\). The Cauchy formula therefore gives

\
g(t)=p(t,b)Q_m[g+R_mg.
\tag{S23}
\]

For integers \(\ell\ge1\),
\((z^\ell-t^\ell)/(z-t)=\sum_{j=0}^{\ell-1}z^{\ell-1-j}t^j\).
The constant term of \(p\) cancels from its difference. Hence (S22) is a polynomial in \(t\) of degree at most \(k-1\), with

\
R_m[g=\sum_{j=0}^{k-1}t^j R_{m,j}g,
\tag{S24}
\]

\
R_{m,j}[g=\frac1{2\pi i}
\int_{\Gamma_m}F_j(z,b)\frac{g(z)}{p(z,b)}\,dz,
\quad
F_j(z,b)=z^{k-1-j}
 +\sum_{\ell=j+1}^{k-1}b_\ell z^{\ell-1-j}.
\tag{S25}
\]

An empty sum is zero; in particular \(F_{k-1}=1\). Formula (S16), \(|z|<3\), and the fixed degree give uniform bounds on \(F_j\) and on every first real-coordinate derivative of \(F_j\); its higher coefficient derivatives vanish.

The local maps are complex-linear in \(g\), holomorphic in \(t\), and smooth in every real coefficient variable. To justify each differentiation under the contour integral, take a compact subset of \(E_\varepsilon\times V_m\). The two denominators have a common positive lower bound there, and the differentiated rational integrands are continuous on its product with the finite-length contour. They have a compact uniform integrable bound. Difference quotients, the fundamental theorem of calculus on parameter segments, and dominated convergence give the first differentiation; iteration gives every order. This argument also proves joint continuity of every resulting derivative. It does not assume simplicity of any polynomial root.

### All local derivative bounds

Let \(w=(u_0,v_0,\ldots,u_{k-1},v_{k-1})\) be the real coefficient coordinates. The polynomial is affine in \(w\), and

\[
A_{u_j}(z)=\partial_{u_j}p(z,b)=z^j,
\qquad
A_{v_j}(z)=\partial_{v_j}p(z,b)=iz^j.
\tag{S26}
\]

For \(\beta\in\mathbb N^d\), \(n=|\beta|\), direct induction gives the exact formula

\[
\partial_b^\beta\frac1{p(z,b)}
=(-1)^n n!\,
\frac{\prod_{i=1}^d A_i(z)^{\beta_i}}{p(z,b)^{n+1}}.
\tag{S27}
\]

At the induction step, \(A_i\) is independent of \(b\); differentiating only the denominator introduces \(-(n+1)A_i\). Since \(|A_i(z)|\le3^{k-1}\) on every contour, (S15) gives

\[
\left|\partial_b^\beta\frac1p\right|
\le n!\,3^{(k-1)n}a_k^{-n-1}
\varepsilon^{-k(n+1)}.
\tag{S28}
\]

Furthermore
\(\partial_t^\alpha(z-t)^{-1}=\alpha!(z-t)^{-\alpha-1}\).
The contour length at most eleven, (S11), (S21), and (S28) now yield

\
|\partial_t^\alpha\partial_b^\beta Q_m[g|
\le C_{k,\alpha,\beta}M
\varepsilon^{-\alpha-1-k(|\beta|+1)}.
\tag{S29}
\]

For (S25), apply Leibniz's rule to \(F_j/p\). Only the term with no derivative on \(F_j\), and terms with one derivative on it, can survive. The former is bounded by a constant times \(\varepsilon^{-k(n+1)}\). If \(n\ge1\), each latter term is bounded by a constant times \(\varepsilon^{-kn}\), which is no larger than \(\varepsilon^{-k(n+1)}\) since \(\varepsilon\le1\). The finite degree, finite multiindex sum, and length bound give

\
|\partial_b^\beta R_{m,j}[g|
\le C_{k,\beta}M\varepsilon^{-k(|\beta|+1)}.
\tag{S30}
\]

All constants in (S29)–(S30) are independent of \(m,b,t,\varepsilon,g\). No estimate of \(1/p(t,b)\) at the evaluation point is used; that value can vanish to any multiplicity.

### Joining the patches without additional loss

Define

\
q^\varepsilon[g=\sum_m\chi_m^\varepsilon(b)Q_mg,
\qquad
r_j^\varepsilong=\sum_m\chi_m^\varepsilon(b)R_{m,j}g,
\tag{S31}
\]

where each product is extended by zero beyond \(V_m\). This extension is smooth: by (S20), the closed support of its partition factor is contained in the interior of \(V_m\), and the factor is identically zero in a neighborhood of its boundary. There is therefore no discontinuous contour selection to differentiate. The expressions are finite sums for each \(\varepsilon\), and the support overlap at any coefficient value is at most \(3^d\). Summing (S23) with the factors \(\chi_m^\varepsilon\) proves (S3).

To prove (S4), differentiate (S31). A term with \(\gamma\le\beta\) derivatives falling on its partition factor has, by (S19) and (S29), the bound

\[
C M\,
\varepsilon^{-k|\gamma|}
\varepsilon^{-\alpha-1-k(|\beta-\gamma|+1)}
=C M\varepsilon^{-\alpha-1-k(|\beta|+1)}.
\tag{S32}
\]

At most \(3^d\) terms can be nonzero for each derivative split, and the number of splits is fixed by \(\beta\). This proves (S4). The same calculation with (S30) gives (S5). These are the finite losses used in the Fourier summation step.

At \(b=0\), the polynomial is \(t^k\). Equation (S3), together with holomorphy of the quotient at zero, forces

\
r_j^\varepsilon[g=\frac{g^{(j)}(0)}{j!},
\qquad
q^\varepsilong
=\frac{g(t)-\sum_{j<k}g^{(j)}(0)t^j/j!}{t^k},
\tag{S33}
\]

with the quotient at zero given by its removable value. Indeed, the first \(k\) Taylor coefficients of \(t^kq\) vanish, which determines the polynomial remainder; away from zero the quotient is then forced, and continuity determines it at zero. This normalization is independent of every patch choice.

### The full-strip version and the whole coefficient space

Suppose now that \(g\) is bounded and holomorphic on \(S_\varepsilon\), with \(M=\sup_{S_\varepsilon}|g|\). Each local contour identity holds throughout its own coefficient ball \(V_m\), not merely on \(\Omega\). Equation (S16) bounds \(\sum_j|b_j|<33/32\) throughout that ball. Every root has modulus less than \(33/32\): a root of modulus at least one satisfies \(|\lambda|\le\sum_j|b_j|\) by the same root-equation argument as before, and smaller roots already have this bound.

For \(|t|\ge5/4\), factorization therefore gives \(|p(t,b)|\ge(|t|-33/32)^k\ge(7/40)^k|t|^k\), uniformly for \(b\in V_m\). The affine coefficient differentiation formula (S27) yields
\[
\left|\partial_b^\beta\frac1{p(t,b)}\right|
\le C_{k,\beta}|t|^{-k-|\beta|},\qquad
\left|\partial_b^\beta\frac{t^j}{p(t,b)}\right|
\le C_{k,\beta}|t|^{j-k-|\beta|}.
\tag{S34}
\]
To differentiate these rational functions in \(t\), use the disk of radius \(|t|/10\). On it, \(|z|\ge9|t|/10\ge9/8\), so \(|z|-33/32\ge|z|/12\); also \(|z|\) is comparable to \(|t|\). These rational functions have no pole anywhere in this disk, even if it leaves the dividend strip. The Cauchy derivative estimate gives
\[
\left|\partial_t^\alpha\partial_b^\beta\frac1p\right|
\le C_{k,\alpha,\beta}|t|^{-k-|\beta|-\alpha},\qquad
\left|\partial_t^\alpha\partial_b^\beta\frac{t^j}{p}\right|
\le C_{k,\alpha,\beta}|t|^{j-k-|\beta|-\alpha}
\quad(|t|\ge5/4,\ b\in V_m).
\tag{S35}
\]
Separately, on \(S_{\varepsilon/4}\), a disk of radius \(\varepsilon/2\) remains inside the supplied dividend strip. Hence \(|g^{(h)}(t)|\le h!2^hM\varepsilon^{-h}\). On the exterior of each patch put
\
Q_{m,\mathrm{ext}}[g
=\frac{g(t)}{p(t,b)}
-\sum_{j=0}^{k-1}R_{m,j}g\frac{t^j}{p(t,b)},
\quad |\operatorname{Re}t|>5/4,\quad
t\in S_{\varepsilon/4},\ b\in V_m.
\tag{S36}
\]
Leibniz's rule, (S30), (S35), and the dividend Cauchy estimate give
\[
|\partial_t^\alpha\partial_b^\beta Q_{m,\mathrm{ext}}[g]|
\le CM\bigl(\varepsilon^{-\alpha}
             +\varepsilon^{-k(|\beta|+1)}\bigr)
\le C'M\varepsilon^{-\alpha-1-k(|\beta|+1)}.
\tag{S37}
\]
Indeed, a coefficient derivative split with \(\gamma\) on the remainder has loss \(k(|\gamma|+1)\), while every rational derivative is uniformly bounded since its power of \(|t|\) is at most \(-1\); \(\varepsilon\le1\) gives the displayed common bound. Constants are uniform in the patch. On \(5/4<|\operatorname{Re}t|<3/2\), the local identity (S23) and nonzero denominator imply \(Q_{m,\mathrm{ext}}=Q_m\). Thus the formulas glue to \(\widetilde Q_m[g]\) on \(S_{\varepsilon/4}\times V_m\), smooth in the real coefficients and holomorphic in \(t\), with (S29) throughout.

Now assemble on the whole real coefficient space, identifying \(\mathbb C^k\) with \(\mathbb R^{2k}\):
\
q^\varepsilon[g
=\sum_m\chi_m^\varepsilon(b)\widetilde Q_mg,
\qquad (t,b)\in S_{\varepsilon/4}\times\mathbb C^k.
\tag{S38}
\]
Every product is zero outside its own ball. The closed support has the positive margin (S20), so this is a smooth zero extension with all mixed derivatives. The retained family is finite for each width and has overlap at most \(3^{2k}\) on the entire coefficient space. The unchanged remainders in (S31) likewise extend smoothly to all \(\mathbb C^k\). In each Leibniz split, the partition loss \(k|\gamma|\) and quotient loss \(\alpha+1+k(|\beta-\gamma|+1)\) add to exactly the loss (S4); the remainder loss adds to (S5). These estimates therefore hold globally in the coefficients, with unchanged constants and losses.

On \(\Omega\) the retained partition sums to one, so the patch identities give (S3) everywhere on the full reduced strip, including every real \(t\). Outside \(\Omega\), no division identity is asserted. Extending each patch before applying its factor avoids an undefined global expression obtained by dividing by \(p\) outside the identity region. This global construction is complex-linear in every actual full-strip dividend. The local bounded-domain construction remains the corresponding global-coefficient zero extension on \(E_\varepsilon\); no full input strip is presumed for a local germ.

At degree one, \(p=t+b_0\), \(F_0=1\), \(c_1=1/16\), \(\rho_1=a_1=1/32\), and the coefficient grid has real dimension two and overlap at most nine. Every empty numerator sum and factorial in the preceding formulas is defined. The quotient and remainder losses specialize to \(\alpha+|\beta|+2\) and \(|\beta|+1\); no argument requires two roots. The same patchwise exterior bound uses \(|t+b_0|\ge(7/40)|t|\).

### Conjugation and additional real parameters

The domains (S2), the full coefficient space and the identity region \(\Omega\) are invariant under complex conjugation. For any dividend put

\[
(Cg)(t)=\overline{g(\bar t)}.
\tag{S39}
\]

This is holomorphic on \(D_\varepsilon\), has the same sup norm, and is conjugate-linear in \(g\). Replace the constructed operators by

\
q^\varepsilon_{\mathrm{sym}}[g
=\tfrac12\bigl(q^\varepsilong
 +\overline{q^\varepsilon[Cg](\bar t,\bar b)}\bigr),
\tag{S40}
\]

\
r^\varepsilon_{\mathrm{sym},j}[g
=\tfrac12\bigl(r_j^\varepsilong
 +\overline{r_j^\varepsilon[Cg](\bar b)}\bigr).
\tag{S41}
\]

The reflected expression is complex-linear in \(g\), because its two conjugations cancel. Conjugate the division identity for \(Cg\) at \((\bar t,\bar b)\), using
\(\overline{p(\bar t,\bar b)}=p(t,b)\). It is another identity for \(g(t)\), so averaging preserves (S3). Reflection of the coefficient coordinates only changes the signs of imaginary-coordinate derivatives; reflection in \(t\) conjugates holomorphic derivatives. Thus (S4)–(S5) remain valid, and (S33) remains valid as well.

If \(Cg=g\), the symmetrized quotient satisfies
\(q^\varepsilon_{\mathrm{sym}}[g](\bar t,\bar b)
=\overline{q^\varepsilon_{\mathrm{sym}}g}\), and the remainder has the corresponding property. They are therefore real on real \(t,b\). A holomorphic dividend that is real on the real interval in \(D_\varepsilon\) satisfies \(Cg=g\) by the identity theorem. This proves the real-valued option without assuming that contours or the complex coefficient grid were chosen symmetrically.

For an additional real parameter \(x\) on an actual open set \(X\), suppose \(g(t,x)\) is holomorphic in \(t\), smooth jointly in its real variables, and for each compact \(K\Subset X\) and each multiindex \(\eta\) has the finite bound

\[
M_{K,\eta}=\sup_{t\in D_\varepsilon,\ x\in K}
|\partial_x^\eta g(t,x)|<\infty.
\tag{S42}
\]

Use the same contours and partition for every \(x\). The fixed-contour dominated differentiation argument then gives
\(\partial_x^\eta q^\varepsilon[g]=q^\varepsilon[\partial_x^\eta g]\) and the analogous equality for each remainder. Equations (S4)–(S5) hold for the additional differentiated operators with \(M_{K,\eta}\) in place of \(M\). If instead the supplied domain is \(S_\varepsilon\times X\) and the suprema in (S42) are taken over \(S_\varepsilon\), the exterior formula (S36) has the same commutation property, since its rational factors are independent of \(x\). The conclusion then holds on \(S_{\varepsilon/4}\times\mathbb C^k\times X\). Both conclusions use a common supplied domain; neither asserts a common domain for arbitrary germs.

## Smooth division by summing entire pieces

An arbitrary smooth real-variable dividend has no supplied holomorphic strip. We divide entire pieces of it on successively thinner strips. Their Fourier frequencies grow like \(2^j\); their suprema on strips of width \(2^{-j}\) decay faster than any fixed power of \(2^{-j}\). This offsets every fixed derivative loss of the already proved strip operators. One fixed series then converges with every real derivative, including coefficient and auxiliary-parameter derivatives.

### Input, output, and the precise finite losses

Fix \(k\ge1\) and retain

\[
p(t,b)=t^k+\sum_{\ell=0}^{k-1}b_\ell t^\ell,
\qquad
\Omega=\{b\in\mathbb C^k:\sum_\ell|b_\ell|<1\}
       \subset\mathbb R^{2k}.
\tag{F1}
\]

Let \(X\subset\mathbb R^n\) be an actual open parameter set; \(n=0\) is allowed. First suppose \(H\in C^\infty(\mathbb R\times X;\mathbb C)\) has locally uniform compact support in \(t\): for each compact \(K\Subset X\), there are an open neighborhood \(X_K\) of \(K\) in \(X\) and a compact interval \(J_K\subset\mathbb R\) such that

\[
H(t,x)=0\quad(t\notin J_K,\ x\in X_K).
\tag{F2}
\]

A fixed compact support in \(t\) for all \(x\) is a useful special case. Assumption (F2), on a neighborhood of \(K\), also gives that support for every \(x\)-derivative at \(x\in K\). The artificial coefficient \(b\) is added independently of the input: the dividend here is \(H(t,x)\).

For every integer \(\nu\ge0\) and auxiliary multiindex \(\eta\), define the finite seminorm

\[
A_{\nu,K,\eta}(H)=
\sup_{x\in K}\int_{\mathbb R}
\bigl(|\partial_x^\eta H(t,x)|
 +|\partial_t^\nu\partial_x^\eta H(t,x)|\bigr)\,dt.
\tag{F3}
\]

Its finiteness follows from (F2) and smoothness on \(J_K\times K\). If \(\nu=0\), the repeated summand is harmless. Without parameters this is exactly the integral seminorm of the dividend and its \(\nu\)-th derivative.

We construct complex-linear maps

\[
Q[H]\in C^\infty(\mathbb R\times\mathbb C^k\times X),\qquad
R_\ell[H]\in C^\infty(\mathbb C^k\times X),\quad0\le\ell<k,
\]

with

\
H(t,x)=p(t,b)Q[H
            +\sum_{\ell=0}^{k-1}t^\ell R_\ellH
\quad(t\in\mathbb R,\ b\in\Omega,\ x\in X).
\tag{F4}
\]

For \(\alpha\ge0\), \(\beta\in\mathbb N^{2k}\), and \(\eta\in\mathbb N^n\), put

\[
\nu_Q=3+\alpha+k(|\beta|+1),\qquad
\nu_R=2+k(|\beta|+1).
\tag{F5}
\]

The following uniform bounds hold:

\[
\sup_{t\in\mathbb R,\ b\in\mathbb C^k,\ x\in K}
|\partial_t^\alpha\partial_b^\beta\partial_x^\eta Q[H]|
\le C_{k,\alpha,\beta}A_{\nu_Q,K,\eta}(H),
\tag{F6}
\]

\[
\sup_{b\in\mathbb C^k,\ x\in K}
|\partial_b^\beta\partial_x^\eta R_\ell[H]|
\le C_{k,\beta}A_{\nu_R,K,\eta}(H).
\tag{F7}
\]

The constants are independent of the support interval, the dividend, the compact parameter set, and its dimension. They depend on the displayed derivative indices and on the fixed choices for the degree-\(k\) strip operators. The parameter derivative is applied to the input in (F3); there is no additional loss of \(t\)-derivatives coming from \(\eta\).

The outputs are smooth on the whole real coefficient space; the division identity is required only on \(\Omega\). The output is smooth in real \(t\). No holomorphic extension of the summed quotient to a fixed complex strip is asserted: the strips used in its definition shrink to the real axis. Reality is retained on real \(b\) when \(H\) is real valued.

### The proved strip operators being used

For every \(0<\varepsilon\le1\), the thin-strip construction above supplies complex-linear, conjugation-compatible operators \(\mathcal Q^\varepsilon\) and \(\mathcal R_\ell^\varepsilon\) for a bounded holomorphic dividend \(h\) on
\(S_\varepsilon=\{z:|\operatorname{Im}z|<\varepsilon\}\). Its quotient is holomorphic in \(z\) on the full reduced strip \(S_{\varepsilon/4}\), smooth in the real coefficient variables, and satisfies

\
h(t)=p(t,b)\mathcal Q^\varepsilon[h
       +\sum_{\ell<k}t^\ell\mathcal R_\ell^\varepsilonh
\quad(t\in S_{\varepsilon/4},\ b\in\Omega).
\tag{F8}
\]

For \(M=\sup_{S_\varepsilon}|h|\), its actual estimates are

\[
|\partial_t^\alpha\partial_b^\beta\mathcal Q^\varepsilon[h]|
\le C_{k,\alpha,\beta}M
\varepsilon^{-\alpha-1-k(|\beta|+1)},\qquad
|\partial_b^\beta\mathcal R_\ell^\varepsilon[h]|
\le C_{k,\beta}M\varepsilon^{-k(|\beta|+1)}.
\tag{F9}
\]

They hold for every \(b\in\mathbb C^k\), for all real \(t\), and also for complex \(t\in S_{\varepsilon/4}\). They remain valid after auxiliary differentiation when the supremum of the differentiated dividend on the full supplied strip replaces \(M\). Contours and partitions are independent of the auxiliary variable; the exterior full-strip extension has rational factors independent of that variable. Consequently those derivatives commute with both operators, on a common supplied strip and parameter domain. We use that full-strip parameter version, not a bound on a fictitious holomorphic extension of \(H\).

Fix these operators once for each of the widths \(\varepsilon_j=2^{-j}\), \(j\ge0\), using the same choices for every input and every derivative order. The estimates use only \(0<\varepsilon_j\le1\).

### A fixed smooth dyadic frequency partition

Here is one explicit choice, to make the frequency partition independent of the input. Use the smooth nonnegative bump \(\theta\) from the strip proof, supported in \([-1,1]\) and positive on \((-1,1)\). Put

\[
\mu(s)=\theta(2s-3),\qquad
c_\mu=\int_{\mathbb R}\mu(s)\,ds>0,
\qquad
F(r)=c_\mu^{-1}\int_r^\infty\mu(s)\,ds,
\quad r\ge0.
\tag{F10}
\]

Then \(F=1\) for \(0\le r\le1\), \(F=0\) for \(r\ge2\), and
\(F'=-\mu/c_\mu\le0\). It is smooth, with all needed endpoint derivatives agreeing with the constant extensions. Set \(\phi(\tau)=F(|\tau|)\). Although \(|\tau|\) itself has a corner at zero, \(\phi\) is constant in a neighborhood of zero, so \(\phi\in C_c^\infty(\mathbb R)\). It is real, even, nonincreasing in \(|\tau|\), and satisfies \(0\le\phi\le1\).

Define

\[
\psi_0(\tau)=\phi(\tau),\qquad
\psi_j(\tau)=\phi(2^{-j}\tau)
             -\phi(2^{-(j-1)}\tau),\quad j\ge1.
\tag{F11}
\]

The functions are smooth, real and even, and \(0\le\psi_j\le1\). Their supports satisfy

\[
\operatorname{supp}\psi_0\subset[-2,2],\qquad
\operatorname{supp}\psi_j
\subset\{\tau:2^{j-1}\le|\tau|\le2^{j+1}\}\quad(j\ge1).
\tag{F12}
\]

For the second assertion, both terms in (F11) are one when \(|\tau|\le2^{j-1}\), and both are zero when \(|\tau|\ge2^{j+1}\). The difference is nonnegative by monotonicity. The partial sums telescope:

\[
\sum_{j=0}^N\psi_j(\tau)=\phi(2^{-N}\tau),\qquad
\sum_{j=0}^\infty\psi_j(\tau)=1.
\tag{F13}
\]

For each fixed \(\tau\), the partial sum is eventually one; at \(\tau=0\) only \(\psi_0\) contributes. This also exhibits \(0\le\sum_{j=0}^N\psi_j\le1\).

### Entire pieces and quantitative strip bounds

Use the established Fourier convention

\[
\widehat H(\tau,x)=\int_{\mathbb R}e^{-is\tau}H(s,x)\,ds,
\qquad
H(t,x)=\frac1{2\pi}\int_{\mathbb R}e^{it\tau}\widehat H(\tau,x)\,d\tau.
\tag{F14}
\]

For each \(x\), the compactly supported smooth input is Schwartz, so the already proved Schwartz inversion theorem supplies the second equality with this exact factor. For \(x\) in a compact parameter neighborhood, (F2) supplies a fixed compact integration interval and bounded mixed derivatives. Differentiation under the integral is therefore justified by dominated difference quotients, giving
\(\partial_x^\eta\widehat H=\widehat{\partial_x^\eta H}\).
Integration by parts in \(s\), with zero boundary terms, gives for \(\tau\ne0\)

\[
(i\tau)^\nu\partial_x^\eta\widehat H(\tau,x)
=\widehat{\partial_s^\nu\partial_x^\eta H}(\tau,x).
\tag{F15}
\]

Thus, uniformly for \(x\in K\),

\[
|\partial_x^\eta\widehat H(\tau,x)|
\le A_{\nu,K,\eta}(H),\qquad
|\partial_x^\eta\widehat H(\tau,x)|
\le A_{\nu,K,\eta}(H)|\tau|^{-\nu}
\quad(|\tau|\ge1).
\tag{F16}
\]

The first bound uses the undifferentiated-in-\(t\) summand in (F3); the second uses the \(\nu\)-th derivative summand.

Define, for every complex \(z\),

\[
H_j(z,x)=\frac1{2\pi}\int_{\mathbb R}
e^{iz\tau}\psi_j(\tau)\widehat H(\tau,x)\,d\tau.
\tag{F17}
\]

Each integral is over a fixed compact frequency support. On a compact set in \(z\) and a compact parameter neighborhood, every differentiated integrand has a uniform integrable bound: a bounded power of \(\tau\), a bounded exponential, and bounded derivatives of \(\widehat H\) on that compact support. Differentiation under the integral gives every \(z\)- and \(x\)-derivative. In particular \(H_j\) is entire in \(z\), smooth jointly in its real variables and \(x\), and

\[
\partial_z^a\partial_x^\eta H_j(z,x)
=\frac1{2\pi}\int e^{iz\tau}(i\tau)^a
\psi_j(\tau)\partial_x^\eta\widehat H(\tau,x)\,d\tau.
\tag{F18}
\]

For \(z\in S_{\varepsilon_j}\), \(\varepsilon_j=2^{-j}\), and \(\tau\) in (F12),
\(|e^{iz\tau}|\le\exp(\varepsilon_j|\tau|)\le e^2\).
For \(j\ge1\), the support has length at most \(4\,2^j\), the frequency magnitude is at most \(2^{j+1}\), and is at least \(2^{j-1}\ge1\). Equations (F16)–(F18) consequently give, for every \(a,\nu\ge0\),

\[
\sup_{z\in S_{\varepsilon_j},\ x\in K}
|\partial_z^a\partial_x^\eta H_j(z,x)|
\le C_{a,\nu}A_{\nu,K,\eta}(H)
                  2^{j(a+1-\nu)},\qquad j\ge1.
\tag{F19}
\]

For \(j=0\), \(\varepsilon_0=1\) and \(|\tau|\le2\) instead yield

\[
\sup_{z\in S_1,\ x\in K}
|\partial_z^a\partial_x^\eta H_0(z,x)|
\le C_a\sup_{x\in K}\int|\partial_x^\eta H(s,x)|\,ds.
\tag{F20}
\]

In particular each differentiated entire piece is bounded on the full strip to which its strip operator is applied. These are actual supplied domains, despite the lack of a holomorphic extension of the original \(H\).

### Reconstruction with every real input derivative

Equations (F14) and (F13), followed by dominated convergence, give

\[
H(t,x)=\sum_{j=0}^\infty H_j(t,x)
\quad(t\in\mathbb R).
\tag{F21}
\]

More explicitly, the partial sum is the inverse integral with multiplier \(\phi(2^{-N}\tau)\). For a prescribed derivative \(\partial_t^a\partial_x^\eta\), choose \(\nu>a+1\). Equation (F16) supplies an integrable, compact-parameter-uniform bound for
\(|\tau|^a|\partial_x^\eta\widehat H|\), by splitting \(|\tau|\le1\) from its complement. The multiplier is at most one and tends to one. Fourier inversion applied to \(\partial_t^a\partial_x^\eta H\), using (F15), identifies the limiting integral as that derivative. The resulting convergence is uniform in real \(t\) and in \(x\in K\), because the absolute integral bound does not depend on real \(t\).

There is also an explicit differentiated tail estimate. With \(s=\nu-a-1>0\), equation (F19) on the real axis gives

\[
\sup_{t\in\mathbb R,\ x\in K}
\left|\partial_t^a\partial_x^\eta
\left(H-\sum_{j=0}^NH_j\right)\right|
\le C_{a,\nu}A_{\nu,K,\eta}(H)
\frac{2^{-(N+1)s}}{1-2^{-s}},\quad N\ge0.
\tag{F22}
\]

This follows by summing the absolute differentiated series over \(j>N\); the preceding inversion argument identifies its value. Taking \(\nu=a+2\) gives a constant times \(A_{a+2,K,\eta}(H)2^{-N}\). Thus the decomposition uses the same fixed pieces for every derivative; only the order used to bound them changes.

### Dividing each piece and summing every mixed tail

For every \(j\ge0\), apply the fixed full-strip operators to the entire piece:

\
Q_j[H=\mathcal Q^{\varepsilon_j}H_j(\cdot,x),\qquad
R_{\ell,j}H=\mathcal R_\ell^{\varepsilon_j}H_j(\cdot,x).
\tag{F23}
\]

They are defined for every real \(t\) and \(b\in\mathbb C^k\), for all \(x\in X\). Each quotient has its own holomorphic extension to \(S_{\varepsilon_j/4}\), which is not a common strip for the whole series. On each compact parameter set, (F19) with \(a=0\) is precisely the required full-strip bound for \(\partial_x^\eta H_j\). The auxiliary differentiation property of the strip operators gives

\[
\partial_x^\eta Q_j[H]
=\mathcal Q^{\varepsilon_j}[\partial_x^\eta H_j],\qquad
\partial_x^\eta R_{\ell,j}[H]
=\mathcal R_\ell^{\varepsilon_j}[\partial_x^\eta H_j].
\tag{F24}
\]

This uses the same contours and partitions for every \(x\); differentiation is not being inferred from abstract linearity alone.

For \(j\ge1\), combining (F19) and (F9), with the quotient's \(t\)-derivative supplied by its operator estimate, gives

\[
\sup_{t\in\mathbb R,\ b\in\mathbb C^k,\ x\in K}
|\partial_t^\alpha\partial_b^\beta\partial_x^\eta Q_j[H]|
\le C_{k,\alpha,\beta,\nu}A_{\nu,K,\eta}(H)
2^{j[\alpha+2+k(|\beta|+1)-\nu]},
\tag{F25}
\]

\[
\sup_{b\in\mathbb C^k,\ x\in K}
|\partial_b^\beta\partial_x^\eta R_{\ell,j}[H]|
\le C_{k,\beta,\nu}A_{\nu,K,\eta}(H)
2^{j[1+k(|\beta|+1)-\nu]}.
\tag{F26}
\]

The quotient exponent has two distinct contributions: \(1-\nu\) from the frequency integration and \(\alpha+1+k(|\beta|+1)\) from strip division. The remainder exponent has \(1-\nu\) plus \(k(|\beta|+1)\). Choosing exactly the orders in (F5) makes both exponents equal to \(-1\). Thus

\[
\|\partial_t^\alpha\partial_b^\beta\partial_x^\eta Q_j[H]\|_
{\mathbb R\times\mathbb C^k\times K,\infty}
\le C_{k,\alpha,\beta}A_{\nu_Q,K,\eta}(H)2^{-j},
\tag{F27}
\]

\[
\|\partial_b^\beta\partial_x^\eta R_{\ell,j}[H]\|_
{\mathbb C^k\times K,\infty}
\le C_{k,\beta}A_{\nu_R,K,\eta}(H)2^{-j}
\quad(j\ge1).
\tag{F28}
\]

For the \(j=0\) term use (F20) and (F9) with \(\varepsilon_0=1\); its relevant derivative is bounded by a constant times the undifferentiated-in-\(t\) integral in (F3). Hence it obeys the desired total estimate without any exceptional small-width loss.

Define the single series

\[
Q[H]=\sum_{j=0}^\infty Q_j[H],\qquad
R_\ell[H]=\sum_{j=0}^\infty R_{\ell,j}[H].
\tag{F29}
\]

For every derivative index, (F27)–(F28) give uniform absolute convergence of the derivative series on the indicated sets. If
\(Q^{[N]}=\sum_{j=0}^NQ_j\) and
\(R_\ell^{[N]}=\sum_{j=0}^NR_{\ell,j}\), the exact geometric tail is

\[
\sup_{\mathbb R\times\mathbb C^k\times K}
|\partial_t^\alpha\partial_b^\beta\partial_x^\eta
 (Q-Q^{[N]})|
\le C_{k,\alpha,\beta}A_{\nu_Q,K,\eta}(H)2^{-N},
\tag{F30}
\]

\[
\sup_{\mathbb C^k\times K}
|\partial_b^\beta\partial_x^\eta
 (R_\ell-R_\ell^{[N]})|
\le C_{k,\beta}A_{\nu_R,K,\eta}(H)2^{-N},
\quad N\ge0,
\tag{F31}
\]

because \(\sum_{j>N}2^{-j}=2^{-N}\). Before smoothness is established, these formulas mean the sums of the formal differentiated series; the next argument identifies them with the derivatives of (F29).

Here is that identification without leaving an unproved termwise-differentiation step. Work in any closed coordinate rectangle lying inside the real domain \(\mathbb R\times\mathbb C^k\times X\). Its projection into \(X\) is contained in a compact \(K\Subset X\). Every partial sum and every derivative is smooth there, and (F27) gives uniform convergence of each derivative sequence. Denote the continuous sum of the \(\gamma\)-th derivatives by \(U_\gamma\). For a coordinate segment contained in the rectangle, the fundamental theorem of calculus gives

\[
\partial^\gamma Q^{[N]}(y+he_i)-\partial^\gamma Q^{[N]}(y)
=\int_0^h\partial^{\gamma+e_i}Q^{[N]}(y+se_i)\,ds.
\tag{F32}
\]

Uniform convergence passes through the finite integral. It gives the same identity with \(U_\gamma,U_{\gamma+e_i}\). Since the latter is continuous, \(U_\gamma\) has coordinate derivative \(U_{\gamma+e_i}\). Inducting on \(|\gamma|\) proves that \(Q\) is smooth and has exactly all the differentiated sums. Rectangles about every point cover the domain. The same argument for the remainder coefficients proves their smoothness and derivatives. This also covers the case \(n=0\).

Equations (F30)–(F31) are therefore genuine derivative tail bounds. Adding the low-frequency term to the geometric series proves (F6)–(F7). All maps in (F29) are complex-linear because both the fixed Fourier decomposition and every strip operator are complex-linear, and the series converge.

For completeness, the polynomial remainder
\(\mathcal RH=\sum_{\ell<k}t^\ell R_\ellH\)
has every mixed derivative tail on \(|t|\le T\). If \(\alpha<k\), differentiating its finite sum gives

\[
\sup_{|t|\le T,\ b\in\mathbb C^k,\ x\in K}
|\partial_t^\alpha\partial_b^\beta\partial_x^\eta
(\mathcal R-\mathcal R^{[N]})|
\le C_{k,\alpha,\beta,T}A_{\nu_R,K,\eta}(H)2^{-N};
\tag{F33}
\]

if \(\alpha\ge k\), that derivative is zero. The powers of \(t\) are bounded on this compact real interval, and (F31) bounds each coefficient. No global supremum bound for a growing polynomial remainder is asserted.

### The division identity, normalization, and reality

Each strip identity (F8) gives, at every real \(t\) and every \(b\in\Omega\),

\[
\sum_{j=0}^NH_j(t,x)
=p(t,b)Q^{[N]}H
 +\sum_{\ell<k}t^\ell R_\ell^{[N]}H.
\tag{F34}
\]

Take \(N\to\infty\). The left side tends to \(H\) by (F21); the right side tends to the asserted expression by (F29). This passage is uniform on bounded real \(t\)-intervals and compact parameter sets, because the fixed polynomial \(p\) is bounded there uniformly for \(b\in\Omega\), and the polynomial remainder has finitely many coefficients. Pointwise it holds at every real \(t\). It proves (F4), including coefficient values with colliding or nonreal roots. It uses no inverse of \(p(t,b)\) at an interior real root.

At \(b=0\), the strip normalization gives
\(R_{\ell,j}H=\partial_t^\ell H_j(0,x)/\ell!\).
The reconstructed derivative series in (F22) yields

\
R_\ell[H=\frac{\partial_t^\ell H(0,x)}{\ell!}.
\tag{F35}
\]

Equation (F4) for \(p=t^k\) forces, away from zero,
\(QH=(H(t,x)-\sum_{\ell<k}t^\ell\partial_t^\ell H(0,x)/\ell!)/t^k\).
Taylor's integral remainder identifies its smooth value also at zero:

\
Q[H=\frac1{(k-1)!}\int_0^1
(1-s)^{k-1}\partial_t^kH(st,x)\,ds,
\qquad
QH=\frac{\partial_t^kH(0,x)}{k!}.
\tag{F36}
\]

The integral formula holds on all real \(t\); its smoothness follows by differentiating its finite integral. It agrees away from zero with the forced quotient and at zero by continuity. These exact jets are available for the later preparation argument; that argument has not been made here.

If \(H\) is real valued, its Fourier transform satisfies
\(\overline{\widehat H(\tau,x)}=\widehat H(-\tau,x)\), by conjugating (F14). Since every \(\psi_j\) is real and even, conjugating (F17) and replacing \(\tau\) by \(-\tau\) gives

\[
H_j(\bar z,x)=\overline{H_j(z,x)}.
\tag{F37}
\]

The conjugation-compatible strip operators therefore give real \(Q_j(t,b,x)\) and real remainder coefficients when \(t,b\) are real. Their convergent sums are real there as well. For general complex inputs, the same construction remains complex-linear. This reality statement is on the whole real coefficient subspace \(\mathbb R^k\); it does not claim reality when the divisor has arbitrary complex coefficients. Existence, rather than uniqueness of the smooth division data, is the asserted interface.

### Actual local dividends and a smooth cutoff extension

Work in coordinates whose marked point is \((0,x_0)\). Suppose the original dividend \(g\) is smooth on an actual open neighborhood \(V\subset\mathbb R^{1+n}\) of that point. Choose a product
\(I\times X\subset V\), with \(I=(-a,a)\), \(a>0\), and \(X\) an open neighborhood of \(x_0\). This product is chosen inside the supplied domain of this dividend. Use the already constructed real cutoff function to set

\[
\chi(t)=\phi(3t/a),\qquad
I_0=(-a/3,a/3),\qquad
J=[-2a/3,2a/3]\Subset I.
\tag{F38}
\]

It satisfies \(\chi=1\) on \(I_0\), \(\operatorname{supp}\chi\subset J\), and is smooth. Define on the common domain \(\mathbb R\times X\)

\[
H(t,x)=
\begin{cases}
\chi(t)g(t,x),&t\in I,\\
0,&t\notin I.
\end{cases}
\tag{F39}
\]

This is smooth jointly in \(t,x\). Near each endpoint of \(I\), the inside formula is identically zero on a full neighborhood, because \(J\) is a positive distance from those endpoints; it therefore agrees with the outside formula with every derivative. Its \(t\)-support is the same compact interval \(J\) for every \(x\in X\). For \(K\Subset X\), Leibniz's rule gives the finite bound

\[
A_{\nu,K,\eta}(H)
\le C_{\chi,\nu}\sum_{h=0}^{\nu}
\sup_{x\in K}\int_J
|\partial_t^h\partial_x^\eta g(t,x)|\,dt.
\tag{F40}
\]

Indeed, \(\partial_t^\nu\partial_x^\eta(\chi g)
=\sum_{h=0}^{\nu}\binom\nu h\chi^{(\nu-h)}
\partial_t^h\partial_x^\eta g\), and all cutoff derivatives have finite suprema and support in \(J\). The undifferentiated term in (F3) is included in the \(h=0\) bound. Thus the local conclusion uses only actual derivatives of \(g\) of \(t\)-order at most the stated \(\nu\), on a compact subset of its actual original domain.

Apply the proved compact-support construction to (F39). On \(I_0\times X\), \(H=g\), so

\
g(t,x)=p(t,b)Q[\chi g
       +\sum_{\ell<k}t^\ell R_\ell\chi g,
\quad t\in I_0,\ b\in\Omega,\ x\in X.
\tag{F41}
\]

All functions are smooth on this common product, and the real-valued option holds because \(\chi\) is real. For all dividends defined on the prescribed product \(I\times X\), this same cutoff can be fixed in advance and the resulting local maps are complex-linear. If another dividend is given only on a different germ neighborhood, its actual domain must first be intersected with the required product or a smaller product chosen inside it. Formula (F41) does not assert one domain on which arbitrary unrelated germs were already defined.

The Fourier construction creates entire pieces from this explicitly extended smooth function. It does not pretend that the original local \(g\) has a holomorphic extension. No extension in the auxiliary variable \(x\) is needed: its actual open set \(X\) is retained throughout. Because \(\chi=1\) near zero, (F35)–(F36) use precisely the original local dividend's jets at the mark.

### Schwartz inputs

The same proof applies to a Schwartz dividend on \(\mathbb R\). For a family, a sufficient explicit replacement for (F2) is joint smoothness and, for every compact \(K\Subset X\), every \(a,\eta\), and every \(N\ge0\),

\[
\sup_{t\in\mathbb R,\ x\in K}
(1+|t|)^N|\partial_t^a\partial_x^\eta H(t,x)|<\infty.
\tag{F42}
\]

On a compact parameter neighborhood these inequalities supply integrable envelopes for every parameter differentiation. They also make every integration-by-parts boundary term vanish. Each fixed fibre and each differentiated fibre is Schwartz, so the same Fourier inversion theorem, (F15)–(F20), and all summation arguments apply without alteration. Equations (F6)–(F7) therefore retain exactly the seminorms and losses required for the Schwartz interface as well.

## Preparation and division by the original smooth divisor

The artificial polynomial coefficients form a finite-dimensional real parameter space. Dividing the given function by the generic polynomial produces a smooth remainder map on this space. Its derivative at the mark is negative multiplication by the first \(k\) Taylor coefficients of the quotient, modulo \(t^k\). The nonzero leading distinguished derivative makes that map invertible, including when the function is complex valued. Solving the remainder equations then gives the prepared polynomial and a nonvanishing smooth factor.

### Hypotheses and the established division interface

Let \(n\ge0\), let \(U_f\subset\mathbb R\times\mathbb R^n\) be an actual open neighborhood of \((0,0)\), and suppose

\[
f\in C^\infty(U_f;\mathbb C),\qquad
\partial_t^j f(0,0)=0\quad(0\le j<k),\qquad
\lambda=\frac{\partial_t^k f(0,0)}{k!}\ne0.
\tag{P1}
\]

Here \(k\ge1\) is a fixed finite integer and \(t,x\) are real variables. The final-stage argument works for every such \(k\) whenever the displayed division interface is supplied. The generic-polynomial construction above establishes this interface for every \(k\ge1\). The arbitrary smooth order-one preparation and division conclusion is received from the separate AN-04 component identified in the prerequisite register; the present final-stage construction is used for the higher-degree conclusion. No conclusion below assumes order \(k\) along every nearby parameter fibre.

Put

\[
\Omega=\left\{b=(b_0,\ldots,b_{k-1})\in\mathbb C^k:
                  \sum_{j=0}^{k-1}|b_j|<1\right\}
          \subset\mathbb R^{2k},\qquad
p(t,b)=t^k+\sum_{j=0}^{k-1}b_jt^j.
\tag{P2}
\]

Write \(b_j=u_j+iv_j\), and use the ordered real coordinates

\[
(u_0,v_0,u_1,v_1,\ldots,u_{k-1},v_{k-1}).
\tag{P3}
\]

For every actual open \(X\subset\mathbb R^n\), the **smooth generic-polynomial division interface** assigns complex-linear operators to every \(H\in C^\infty(\mathbb R\times X;\mathbb C)\) with locally uniform compact support in \(t\). Precisely, every compact \(K\Subset X\) has a neighborhood \(X_K\subset X\) and a compact interval \(J_K\) such that \(H(t,x)=0\) for \(t\notin J_K, x\in X_K\). The outputs have domains

\[
Q[H]\in C^\infty(\mathbb R\times\Omega\times X;\mathbb C),\qquad
R_j[H]\in C^\infty(\Omega\times X;\mathbb C),\quad0\le j<k,
\tag{P4}
\]

and satisfy the actual smooth identity

\
H(t,x)=p(t,b)Q[H
             +\sum_{j=0}^{k-1}t^jR_jH
\quad(t\in\mathbb R, b\in\Omega, x\in X).
\tag{P5}
\]

The choices defining the operators are independent of \(x\) and of derivative order. Smooth parameter differentiation commutes with them:

\[
\partial_x^\eta Q[H]=Q[\partial_x^\eta H],\qquad
\partial_x^\eta R_j[H]=R_j[\partial_x^\eta H].
\tag{P6}
\]

Their normalization at the zero coefficient vector is

\
R_j[H=\frac{\partial_t^jH(0,x)}{j!},\qquad
QH=\frac1{(k-1)!}\int_0^1
(1-s)^{k-1}\partial_t^k H(st,x)\,ds.
\tag{P7}
\]

Thus \(QH=\partial_t^kH(0,x)/k!\). The quotient formula includes the smooth value at \(t=0\). It is the Taylor remainder quotient, not an asserted holomorphic extension of \(H\).

The Fourier construction supplies the following exact losses. If

\[
A_{\nu,K,\eta}(H)=\sup_{x\in K}\int_{\mathbb R}
\bigl(|\partial_x^\eta H(t,x)|
       +|\partial_t^\nu\partial_x^\eta H(t,x)|\bigr)\,dt,
\tag{P8}
\]

then for \(\alpha\ge0, \beta\in\mathbb N^{2k},\ \eta\in\mathbb N^n\),

\[
\begin{aligned}
\sup_{\mathbb R\times\Omega\times K}
|\partial_t^\alpha\partial_b^\beta\partial_x^\eta Q[H]|
&\le C_{k,\alpha,\beta}A_{3+\alpha+k(|\beta|+1),K,\eta}(H),\\
\sup_{\Omega\times K}
|\partial_b^\beta\partial_x^\eta R_j[H]|
&\le C_{k,\beta}A_{2+k(|\beta|+1),K,\eta}(H).
\end{aligned}
\tag{P9}
\]

The constants are the fixed operator constants, independent of \(H,X,K\) and the support interval. This proof uses smoothness, (P5), and (P7); (P6) and (P9) justify the stated parameter interface and quantitative local extension. It does not replace the strip or Fourier proofs of those properties. For the real-valued option, the supplied operators also have real outputs on real \(t,b\) whenever \(H\) is real valued. In particular, \(R[H]\) restricted to \(\Omega\cap\mathbb R^k\) is a real map.

The Fourier division identity (F4), mixed derivative estimates (F6)–(F7), Taylor normalization (F35)–(F36), and reality proof following (F37) supply the interface used here. The auxiliary parameter derivatives commute with the operators because each fixed strip operator and each fixed Fourier multiplier is independent of that parameter, and every differentiated series converges as proved in (F24)–(F32). Thus the coefficient implicit construction below uses established smooth maps on the actual domains.

### Extend the divisor on its supplied domain

Choose \(a>0\) and an open neighborhood \(X\subset\mathbb R^n\) of zero such that

\[
I\times X\subset U_f,\qquad I=(-a,a).
\tag{P10}
\]

Use a fixed real \(\phi\in C_c^\infty(\mathbb R)\) with \(0\le\phi\le1\), \(\phi=1\) on \([-1,1]\), and \(\operatorname{supp}\phi\subset[-2,2]\). The already constructed Fourier cutoff is one such choice. Set

\[
\chi_f(t)=\phi(3t/a),\qquad
I_0=(-a/3,a/3),\qquad
J_f=[-2a/3,2a/3]\Subset I.
\tag{P11}
\]

Define on the actual domain \(\mathbb R\times X\)

\[
F(t,x)=
\begin{cases}
\chi_f(t)f(t,x),&t\in I,\\
0,&t\notin I.
\end{cases}
\tag{P12}
\]

This is jointly smooth, since the first formula is identically zero on a neighborhood of each endpoint of \(I\) and agrees there with the second formula with every derivative. It has the same compact \(t\)-support \(J_f\) for all \(x\in X\), so the interface applies. On \(I_0\times X\), \(F=f\); in particular every \(t,x\) derivative of \(F\) at \((0,x)\) equals the corresponding derivative of \(f\). This uses no extension in \(x\) and no assertion that \(f\) was originally defined for every real \(t\).

Abbreviate

\
Q(t,b,x)=Q[F,\qquad
R(b,x)=(R_0F,\ldots,R_{k-1}F),\qquad
Q_0(t)=Q(t,0,0).
\tag{P13}
\]

Equations (P1) and (P7) give

\[
R(0,0)=0,\qquad Q_0(0)=\lambda\ne0.
\tag{P14}
\]

### The exact triangular multiplication-jet formula

For a smooth function \(h(t)\), write its truncated Taylor polynomial as

\[
J_{<k}h(t)=\sum_{j=0}^{k-1}\frac{h^{(j)}(0)}{j!}t^j.
\tag{P15}
\]

This is a finite jet operation. It makes sense for smooth data without convergence of their infinite Taylor series. Every derivative of \(t^k h(t)\) of order less than \(k\) vanishes at zero, by Leibniz's rule.

Let \(v=(v_0,\ldots,v_{k-1})\in\mathbb C^k\) be a real tangent direction in the coefficient space and put \(B_v(t)=\sum_{\ell<k}v_\ell t^\ell\). The real parameter path \(b=sv\) lies in \(\Omega\) for all sufficiently small real \(s\). Differentiate (P5) for \(F\) along this path at \(s=0, x=0\). Its left side is independent of \(b\), and \(D_b p(t,0)[v]=B_v(t)\), so

\[
0=B_v(t)Q_0(t)+t^kD_bQ(t,0,0)[v]
             +\sum_{j=0}^{k-1}t^jD_bR_j(0,0)[v].
\tag{P16}
\]

Apply \(J_{<k}\). The middle term disappears. For \(0\le j<k\), the \(j\)-th Taylor coefficient of the product is exactly

\[
\frac1{j!}\frac{d^j}{dt^j}\bigl(B_v(t)Q_0(t)\bigr)\Big|_{t=0}
=\sum_{\ell=0}^j v_\ell\,
             \frac{Q_0^{(j-\ell)}(0)}{(j-\ell)!}.
\tag{P17}
\]

Indeed, Leibniz's coefficient for the derivative of \(t^\ell\) is \(\binom j\ell\ell!\); division by \(j!\) leaves \(1/(j-\ell)!\). Terms with \(\ell>j\) vanish. Set

\[
q_m=\frac{Q_0^{(m)}(0)}{m!}\quad(0\le m<k).
\tag{P18}
\]

Then the actual remainder derivative is

\[
\boxed{
D_bR_j(0,0)[v]=-\sum_{\ell=0}^j q_{j-\ell}v_\ell,
\qquad0\le j<k.}
\tag{P19}
\]

Its sign follows from moving the product term in (P16) to the other side. No complex differentiability of \(R\) in \(b\) was assumed: (P19), proved for every real tangent direction, shows that this particular real derivative is complex-linear.

The \(q_m\) can also be read directly from the original divisor. At \(b=0,x=0\), the remainder is zero, so (P5) gives \(F(t,0)=t^kQ_0(t)\). Differentiating \(k+m\) times at zero leaves only the term with exactly \(k\) derivatives on \(t^k\), hence

\[
q_m=\frac{\partial_t^{k+m}f(0,0)}{(k+m)!},\qquad0\le m<k,
\tag{P20}
\]

because \(F=f\) near the mark. In particular \(q_0=\lambda\).

In the increasing coefficient order \(0,\ldots,k-1\), the complex matrix \(A=D_bR(0,0)\) is

\[
A=(A_{j\ell})_{0\le j,\ell<k},\qquad
A_{j\ell}=
\begin{cases}
-q_{j-\ell},&\ell\le j,\\
0,&\ell>j.
\end{cases}
\tag{P21}
\]

This is negative multiplication by \(J_{<k}Q_0\) in the finite jet algebra \(\mathbb C[t]/(t^k)\), with each \(v\) identified with \(B_v\). Only that finite algebra is used; it is not a ring of convergent series.

### Its real \(2k\)-dimensional matrix is invertible

Multiplication by \(z\in\mathbb C\), in the real basis \((1,i)\), has matrix

\[
M(z)=\begin{pmatrix}\operatorname{Re}z&-\operatorname{Im}z\\
                     \operatorname{Im}z&\operatorname{Re}z\end{pmatrix},
\qquad\det M(z)=|z|^2.
\tag{P22}
\]

Thus, in the actual ordered coordinates (P3), the real Jacobian of \(R\) has blocks

\[
A^{\mathbb R}_{j\ell}=
\begin{cases}
M(-q_{j-\ell})
=\begin{pmatrix}-\operatorname{Re}q_{j-\ell}&\operatorname{Im}q_{j-\ell}\\
                -\operatorname{Im}q_{j-\ell}&-\operatorname{Re}q_{j-\ell}
  \end{pmatrix},&\ell\le j,\\
0,&\ell>j.
\end{cases}
\tag{P23}
\]

It is lower triangular in \(2\times2\) blocks. Every diagonal block is \(M(-\lambda)\), so

\[
\det_{\mathbb R}D_bR(0,0)=|\lambda|^{2k}>0.
\tag{P24}
\]

An explicit inverse also records that no complex coefficient direction is missing. Write \(A=-(\lambda I+N)\), where \(N_{j\ell}=q_{j-\ell}\) when \(\ell<j\) and \(N_{j\ell}=0\) otherwise. This \(N\) is strictly lower triangular, so \(N^k=0\). The finite geometric identity gives

\[
A^{-1}=-\lambda^{-1}\sum_{h=0}^{k-1}(-\lambda^{-1}N)^h.
\tag{P25}
\]

Multiplication in both orders verifies (P25). It is a complex-linear inverse and therefore also the inverse of the real map. Equivalently, \(Av=w\) is solved successively by

\[
v_0=-\frac{w_0}{\lambda},\qquad
v_j=-\frac{w_j+\sum_{\ell<j}q_{j-\ell}v_\ell}{\lambda}
\quad(1\le j<k).
\tag{P26}
\]

### Solve the actual remainder equations and keep the unit nonzero

Regard \(R:\Omega\times X\to\mathbb C^k\simeq\mathbb R^{2k}\) as its actual smooth real map. Apply the finite-dimensional smooth implicit construction to \(R(b,x)=0\), with solved variable \(b\) and parameter \(x\). Its hypotheses are exactly (P14) and (P24), on the actual open domain \(\Omega\times X\).

To specify the receiving map, use

\[
L(x,b)=(x,R(b,x)),\qquad
DL(0,0)=\begin{pmatrix}I_n&0\\D_xR(0,0)&A\end{pmatrix},\qquad
DL(0,0)^{-1}=\begin{pmatrix}I_n&0\\-A^{-1}D_xR(0,0)&A^{-1}\end{pmatrix}.
\tag{P27}
\]

The proved inverse theorem for this augmented map supplies neighborhoods \(X_1\subset X\) of zero and \(B\subset\Omega\) of zero and an actual smooth coefficient map

\[
a=(a_0,\ldots,a_{k-1}):X_1\longrightarrow B,\qquad
a(0)=0,\qquad R(a(x),x)=0.
\tag{P28}
\]

The selected solution is unique among \(b\in B\) in the local implicit neighborhood for this fixed remainder map. This local implicit uniqueness is not a uniqueness theorem for smooth preparation or division.

The complete [real finite-dimensional inverse and implicit proof](../prerequisites/U011-free-foundations/implicit-maps-U070.md) supplies the construction used in (P27)–(P28), including every higher smooth derivative. That AN-03 component retains its CC0 1.0 terms and is supplied as an exact selected prerequisite. The receiving map here is the actual remainder map on its stated original real domains.

For example, the exact derivative binding is

\[
D_xa(x)=-\bigl(D_bR(a(x),x)\bigr)^{-1}D_xR(a(x),x),\qquad
D_xR_j(0,0)=\frac{\partial_x\partial_t^jf(0,0)}{j!}.
\tag{P29}
\]

After shrinking \(B,X_1\) as in the implicit construction, the inverse in the first expression exists. The second expression follows from (P6)–(P7) and the divisor cutoff being one near \(t=0\). It is an equality of linear maps in the original real \(x\)-directions. All higher smoothness comes from the stated smooth maps and the proved implicit construction.

Substitute \(b=a(x)\) in (P5) and define

\[
P(t,x)=p(t,a(x))=t^k+\sum_{j=0}^{k-1}a_j(x)t^j,\qquad
c(t,x)=Q(t,a(x),x).
\tag{P30}
\]

Both functions are smooth on their actual substituted domains. On \(I_0\times X_1\), equations (P12), (P28), and (P5) give

\[
f(t,x)=c(t,x)P(t,x),\qquad c(0,0)=\lambda\ne0.
\tag{P31}
\]

Continuity of \(c\) at \((0,0)\) gives a product neighborhood

\[
U_*=(-\delta,\delta)\times X_2\subset I_0\times X_1,
\qquad0<\delta<a/3,
\qquad |c(t,x)-\lambda|<\frac{|\lambda|}{2}\quad((t,x)\in U_*).
\tag{P32}
\]

Consequently

\[
|c(t,x)|>\frac{|\lambda|}{2},\qquad
\frac1c=\frac{\overline c}{|c|^2}\in C^\infty(U_*),\qquad
\left|\frac1c\right|<\frac2{|\lambda|}.
\tag{P33}
\]

This gives the actual nonvanishing unit and not just its value at the mark. Since \(a(0)=0\), \(P(t,0)=t^k\). The mark values and monic degree are exactly those required for smooth preparation; no normalization of the original \(f\) or its nonzero \(\lambda\) was made.

When \(n=0\), \(X\) is the singleton open set in \(\mathbb R^0\), the implicit parameter map has the value \(a=0\), and the same formula gives the ordinary one-variable Taylor factorization. There is no division by a zero-dimensional operator norm.

### Real-valued preparation

Suppose \(f\) is real valued on its supplied neighborhood. The cutoff in (P11) is real, so \(F\) is real. Use the real-valued operator clause and restrict the remainder map to

\[
R^{\mathrm{real}}:(\Omega\cap\mathbb R^k)\times X\longrightarrow\mathbb R^k.
\tag{P34}
\]

In this case every \(q_m\) in (P20) is real and \(\lambda\in\mathbb R\setminus\{0\}\). The derivative of (P34) in the \(k\) real coefficient directions is the \(k\times k\) lower triangular matrix (P21), with

\[
\det_{\mathbb R}D_bR^{\mathrm{real}}(0,0)=(-\lambda)^k\ne0.
\tag{P35}
\]

The real \(k\)-dimensional implicit construction gives a real coefficient map \(a:X_1\to\Omega\cap\mathbb R^k\). The substituted quotient \(c(t,x)\) in (P30) is real for real \(t,x\), by the operator reality clause. Equations (P31)–(P33) then give real smooth preparation, with \(c\) of the same sign as \(\lambda\) on the chosen product neighborhood. This establishes existence of real factors directly; it does not require any unproved analytic uniqueness statement.

### Divide each dividend on its own original domain

Fix the prepared \(a,c,U_*\) above. Let \(g\in C^\infty(U_g;\mathbb C)\) be any dividend on an actual open neighborhood \(U_g\subset\mathbb R^{1+n}\) of the same mark. Choose \(d>0\) and an open neighborhood \(Y\subset X_2\) of zero such that

\[
(-d,d)\times Y\subset U_g\cap U_*.
\tag{P36}
\]

These choices may depend on the supplied domain of \(g\). Define

\[
\chi_g(t)=\phi(3t/d),\qquad
J_g=[-2d/3,2d/3]\Subset(-d,d),\qquad
U_g'=(-d/3,d/3)\times Y,
\tag{P37}
\]

and define \(G\in C^\infty(\mathbb R\times Y;\mathbb C)\) by

\[
G(t,x)=
\begin{cases}
\chi_g(t)g(t,x),&|t|<d,\\
0,&|t|\ge d.
\end{cases}
\tag{P38}
\]

As in (P12), the formulas agree on open neighborhoods of the endpoints with every derivative. Thus (P38) is a genuine smooth zero extension, with fixed compact \(t\)-support \(J_g\), and \(G=g\) on \(U_g'\). For every compact \(K\Subset Y\), Leibniz's rule gives

\[
A_{\nu,K,\eta}(G)
\le C_{\chi_g,\nu}\sum_{h=0}^{\nu}
\sup_{x\in K}\int_{J_g}|\partial_t^h\partial_x^\eta g(t,x)|\,dt.
\tag{P39}
\]

The constant is finite because all derivatives of the fixed cutoff are bounded. Formula (P39) uses only the original dividend on a compact subset of its actual domain; it does not presume any holomorphic extension or global smooth representative of its germ.

Apply (P5) to this \(G\), with parameter set \(Y\), and then substitute the already prepared map \(b=a(x)\in\Omega\). Put

\
\widetilde Q_g(t,x)=Q[G,x),\qquad
r_j(x)=R_jG,x).
\tag{P40}
\]

Every function in (P40) is smooth on the stated domain by the real-variable chain rule. On \(U_g'\), where \(G=g\), the identity becomes

\[
g(t,x)=P(t,x)\widetilde Q_g(t,x)+\sum_{j=0}^{k-1}t^jr_j(x).
\tag{P41}
\]

Since \(f=cP\) and \(c\) is nonzero on \(U_*\), define the actual quotient by the original divisor as

\[
q_g(t,x)=\frac{\widetilde Q_g(t,x)}{c(t,x)}\in C^\infty(U_g';\mathbb C).
\tag{P42}
\]

Then the required original-divisor division is

\[
\boxed{g(t,x)=f(t,x)q_g(t,x)+\sum_{j=0}^{k-1}t^jr_j(x)
\quad((t,x)\in U_g'),\qquad r_j\in C^\infty(Y;\mathbb C).}
\tag{P43}
\]

The order of these operations matters: extend on the dividend's actual product domain, apply the common generic-polynomial operators there, substitute the prepared coefficient map, and divide the polynomial quotient by the existing unit. Applying the operators directly to an unspecified local germ would leave their input undefined.

If both \(f\) and \(g\) are real valued, choose the real preparation above. The real cutoff, operator reality, and real map \(a\) make \(\widetilde Q_g,r_j\) real; division by the real nonzero \(c\) makes \(q_g\) real. If only \(g\) is real and \(f\) is complex valued, no reality conclusion for the quotient or remainder is claimed.

For all dividends defined on one prescribed common product in (P36), the same \(d,Y,\chi_g\) can be fixed independently of the dividend. The maps \(g\mapsto q_g,r_j\) are then complex-linear on that common domain: extension, the generic division maps, substitution by the fixed \(a\), and multiplication by \(1/c\) each preserve linearity. Equations (P9) and (P39), followed by the finite chain and product rules on compact subsets of \(U_g'\), also give finite differentiated bounds for these local maps. Their constants after substitution may depend on derivatives of the fixed \(a,c,\chi_g\); the generic losses in (P9) are not asserted unchanged after a derivative differentiates \(a(x)\).

If \(g\) is globally smooth on \(\mathbb R^{1+n}\), use a product strictly inside the fixed \(U_*\) and one cutoff for all such \(g\). This yields a common output neighborhood depending on the divisor and that product alone. For unrelated local germs, (P36) instead intersects each actual supplied domain. Nothing asserts one neighborhood on which all those unrelated representatives were already defined.

### Existence and smooth nonuniqueness

The only uniqueness used here is the finite-dimensional implicit solution for the fixed constructed remainder map in its selected neighborhood. Smooth generic division data, and the resulting smooth preparations, are not claimed unique as germs. Neither real smoothness nor a finite jet permits importing analytic uniqueness.

## Complete prerequisites, construction credit, and component terms

The analytic theorem above is used by reference from [Weierstrass preparation and division](../prerequisites/U011-free-foundations/weierstrass-preparation-U070.md). Its treatment is attributed to Jean-Pierre Demailly, *Complex Analytic and Differential Geometry*, 21 June 2012. Demailly remains the author of that treatment; the pinned component source and component notice preserve his custom OpenContent grant. That grant is not replaced by this receiver's CC0 dedication. No expression from the analytic component is copied into the new proofs here.

The following complete programme proofs are supplied with this lesson. The AN-03 components retain their ownership; the independently written Fourier foundation retains its stated terms. These independently written programme components and the receiving exposition carry CC0 1.0; their distinct credits and exact proof locations are retained.

| Needed fact | Complete linked provider and receiving use |
|---|---|
| Local power series, isolated zero multiplicity, Cauchy formula, parameter integrals, winding numbers, residues, and maximum principles | [Contour foundations](../prerequisites/U011-free-foundations/complex-contours-U070.md), including its dominated jointly holomorphic parameter-integral proof; used in the symmetric-coefficient receiver and fixed-contour strip division |
| Ordinary monic polynomial division and complete finite complex-root factorization with multiplicity | [Polynomial division](../prerequisites/U011-free-foundations/polynomial-roots-U070.md#scalar-polynomial-division) and [complex root factorization](../prerequisites/U011-free-foundations/polynomial-roots-U070.md#9-complex-roots-with-all-original-coefficients-retained); used for pointwise polynomial algebra and the root bound |
| Schwartz Fourier inversion with forward kernel \(e^{-it\tau}\) and inverse factor \((2\pi)^{-1}\) | [Complete Fourier inversion proof](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md); used in (F14) and the differentiated reconstruction |
| Finite-dimensional smooth inverse and implicit maps with all higher derivatives | [Complete inverse and implicit construction](../prerequisites/U011-free-foundations/implicit-maps-U070.md); used for the actual remainder equations (P27)–(P29) |

The separately owned complex smooth order-one proof is AN-04's *Real and complex symplectic normal forms of functions*, “Smooth complex division” in “Remove one momentum from the imaginary part.” The [complete companion component](../prerequisites/U011-free-foundations/AN04-order-one-division.md) preserves its full selected statement and proof, ownership, and observed CC0-1.0 terms. Equations (O1)–(O3) receive the complex order-one preparation and division consequences. Equations (O4)–(O5) give the real option from the complete real implicit proof and exact Taylor graph factorization. The generic strip and Fourier operators above cover every fixed \(k\ge1\), including their whole real coefficient domains and unchanged derivative losses.

For historical construction credit, Bernard Malgrange's freely accessible primary account [*Idéaux de fonctions différentiables et division des distributions*, §5, printed pp. 12–14](https://www.numdam.org/item/10.5802/xups.2003-01.pdf) presents generic-polynomial reduction and cancellation of remainders by the implicit-function mechanism, and distinguishes smooth existence from analytic uniqueness. It credits subsequent linear continuous division methods to Mather, Nirenberg and Łojasiewicz. The PDF states CC BY 4.0. The finite identities, geometric constants, differentiated estimates, complex remainder Jacobian, and local-domain arguments here are independently written exposition of classical mathematics; every used result has its proof here or in the supplied programme prerequisites.

Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, reprint of the second edition (1990), §7.5, pp. 195–201, supplies the classical analytic, thin-strip and Fourier-summation route, including the derivative orders in (F5)–(F6). The exact approved purchased copy was compared with this lesson. The lesson retains its independent exposition, explicit rectangle and partition constants, complex remainder Jacobian, domain analysis, alternative order-one proof, and eight original exercises; purchase does not grant reproduction of the book’s expression.

## Eight graded exercises and complete solutions

### Exercises

**Exercise 1 (basic: signs and repeated occurrences).** A monic polynomial of degree four has root list \(1,1,-2,-2\), with repeated occurrences counted separately. Compute its first four power sums. Recover all four descending coefficients from
\[
jA_j+\sum_{\ell=1}^j A_{j-\ell}S_\ell=0,
\qquad A_0=1.
\]
Check the result by multiplying its factors. Explain why a zero or a repeated root would not invalidate the recursion.

**Exercise 2 (intermediate: coefficients without root labels).** For
\(f(t,z)=t^3-z\), where \((t,z)\) are complex, choose \(r>0\) and restrict \(|z|<r^3/2\). Compute the zero count and the first three weighted logarithmic-derivative contour moments on \(|t|=r\). Recover the prepared polynomial. Prove that a root cannot be named holomorphically on a neighborhood of \(z=0\). Identify the distinguished order, ambient order, and the stronger coefficient estimate that fails.

**Exercise 3 (advanced: a collision in an explicit strip dividend).** Let \(\lambda,\delta\in\mathbb R\), \(|\delta|<1\), and
\[
p(t,\delta)=t^2-\delta^2,
\qquad g(t)=\cos(\lambda t).
\]
Find the polynomial remainder of degree less than two and the holomorphic quotient, including their values at \(\delta=0\). Prove that the quotient is smooth through the collision \((t,\delta)=(0,0)\), without using variable root labels or leaving a quotient with an unexplained zero denominator. Give its value at the collision and the bound for \(g\) on the full strip \(|\operatorname{Im}t|<\varepsilon\).

**Exercise 4 (intermediate: the actual complex remainder Jacobian).** Suppose a smooth generic-polynomial division operator gives
\[
F(t)=Q(t,b)p(t,b)+\sum_{j=0}^2R_j(b)t^j,
\qquad p(t,b)=t^3+b_2t^2+b_1t+b_0,
\]
where \(b\in\mathbb C^3\simeq\mathbb R^6\), \(R(0)=0\), and
\(Q(t,0)=2+3t-t^2+O(t^3)\). Regard all coefficient derivatives as real-coordinate derivatives. Compute \(D_bR(0)\), its complex and real determinants, and its inverse applied to a vector \(y=(y_0,y_1,y_2)\). Explain why the differential is complex-linear at this point even though the operator need not be holomorphic in \(b\).

**Exercise 5 (advanced: smooth division and preparation need not be unique).** Define
\[
h(x)=\begin{cases}e^{-1/x^2},&x\ne0,\\0,&x=0,\end{cases}
\qquad f(t,x)=t^2+x^2,
\]
with real variables. Construct a nontrivial smooth division of the zero dividend by \(f\), with remainder degree less than two. Then construct two distinct smooth monic preparations of \(f\), each with a nonvanishing real unit and coefficients vanishing at \(x=0\). Prove the smoothness of every quotient at the origin. Explain why this does not contradict holomorphic uniqueness.

**Exercise 6 (intermediate: an actual common dividend domain).** Let \(g\in C^\infty((-2,2)\times V)\), with \(V\subset\mathbb R^n\) open. Construct a zero-extended dividend on \(\mathbb R\times V\) with fixed compact \(t\)-support that agrees with \(g\) for \(|t|<1\). Show compact-uniform \(L^1\) bounds for every mixed derivative and explain why parameter derivatives commute with this extension. Give a family of declared germ domains for which no one positive \(t\)-interval is a domain for every member. State exactly what neighborhood a division theorem may conclude for each member.

**Exercise 7 (advanced: the differentiated Fourier tails).** Let \(H(t,x)\) have fixed compact \(t\)-support and be smooth, with every mixed derivative compact-uniformly bounded for \(x\) in compact subsets of an open parameter set. Use
\(\widehat H(\tau,x)=\int e^{-it\tau}H(t,x)\,dt\). Let \(\phi\) be a smooth real even cutoff equal to one on \([-1,1]\) and zero off \([-2,2]\), and set
\[
\psi_0(\tau)=\phi(\tau),\qquad
\psi_j(\tau)=\phi(2^{-j}\tau)-\phi(2^{-(j-1)}\tau)
\quad(j\ge1),
\]
\[
H_j(z,x)=\frac1{2\pi}\int e^{iz\tau}\psi_j(\tau)
\widehat H(\tau,x)\,d\tau,
\qquad \varepsilon_j=2^{-j}.
\]
Assume fixed complex-linear, conjugation-compatible full-strip division operators, independent of the auxiliary parameter \(x\), which commute with every auxiliary derivative on the common supplied strip and parameter domain. Their differentiated quotient and remainder sup-norm bounds are uniform for all real \(t\), with losses
\[
L_q=\alpha+1+k(|\beta|+1),\qquad L_r=k(|\beta|+1).
\]
Prove geometric tail bounds for every real \(t\), real coefficient and auxiliary-parameter derivative, with sufficient dividend derivative orders
\(\nu_q=3+\alpha+k(|\beta|+1)\) and
\(\nu_r=2+k(|\beta|+1)\). Show reconstruction of \(H\), and explain why the summed quotient is asserted smooth on the real axis rather than holomorphic on a common complex strip.

**Exercise 8 (basic: polynomial division followed by unit absorption).** In real variables \((t,x,y)\), let
\[
P(t,x,y)=t^3-xt+y,
\qquad g(t,x,y)=t^5+xt^2+2y.
\]
Compute division by \(P\). Then give division by each of
\((1+t^2)P\) and \((1+it)P\), retaining the same remainder. Check the identity by expansion. Which data are real in the two cases, and what is the distinguished zero order at the mark?

### Complete solutions

**Solution 1.** The moments are
\[
S_1=-2,\qquad S_2=10,\qquad S_3=-14,\qquad S_4=34.
\]
The four recursive equations are
\[
\begin{aligned}
A_1&=2,\\
2A_2&=-(A_1S_1+S_2)=-6,\\
3A_3&=-(A_2S_1+A_1S_2+S_3)=-12,\\
4A_4&=-(A_3S_1+A_2S_2+A_1S_3+S_4)=16.
\end{aligned}
\]
Thus \(A=(2,-3,-4,4)\), and
\[
P(t)=t^4+2t^3-3t^2-4t+4
     =(t-1)^2(t+2)^2=(t^2+t-2)^2.
\]
Newton's identity is a finite polynomial identity in a list of occurrences; it divides only by positive integers. Repeating or setting any root to zero therefore preserves the identity. A zero occurrence contributes zero to each positive-degree moment while still contributing one to the zero count.

**Solution 2.** On the circle,
\(|t^3-z|\ge r^3-|z|>r^3/2\). The argument principle count is three at \(z=0\); the fixed-contour count is continuous, integer valued and hence constant on the connected base disk. Weighted residues count each root with its multiplicity. For \(z\ne0\), choose any cube root \(a\) at that one fibre and list \(a,a\omega,a\omega^2\), where \(\omega=e^{2\pi i/3}\). Their first three power sums are
\[
S_1=0,\qquad S_2=0,\qquad S_3=3z.
\]
They hold at \(z=0\) as well by continuity or by the triple zero. The recursion gives \(A_1=A_2=0\), \(A_3=-z\); the prepared polynomial is already \(t^3-z\), with unit one. A holomorphic root \(a(z)\) would satisfy \(a(z)^3=z\). It is not identically zero and has a positive integer zero order \(m\) at zero, forcing \(3m=1\), which is impossible. Distinguished \(t\)-order is three; the ambient Taylor order is one. Consequently \(A_3=-z\) vanishes at zero but is not \(O(|z|^3)\). That stronger estimate would require ambient order three.

**Solution 3.** The remainder is constant:
\[
r_0(\delta)=\cos(\lambda\delta),\qquad r_1(\delta)=0,
\qquad
q(t,\delta)=\frac{\cos(\lambda t)-\cos(\lambda\delta)}{t^2-\delta^2}.
\]
For \(\delta\ne0\), interpolation at the two distinct real roots gives these coefficients. Holomorphic extension at each root follows because the numerator vanishes there. The complete collision extension follows from the convergent series
\[
q(t,\delta)=\sum_{m=1}^{\infty}
\frac{(-1)^m\lambda^{2m}}{(2m)!}
\sum_{\ell=0}^{m-1}t^{2(m-1-\ell)}\delta^{2\ell}.
\]
Indeed, the inner polynomial times \(t^2-\delta^2\) is \(t^{2m}-\delta^{2m}\). On any compact set \(|t|,|\delta|\le B\), any fixed mixed derivative of that polynomial is bounded by a fixed power of \(2m\), times \(m\max(1,B)^{2m}\). The factorial makes the differentiated series uniformly summable. The series is therefore jointly entire in \((t,\delta)\), agrees with the displayed quotient off its zero denominator, and supplies every missing value. In particular
\[
q(t,0)=\frac{\cos(\lambda t)-1}{t^2},\qquad
q(0,0)=-\frac{\lambda^2}{2},\qquad r_0(0)=1.
\]
For a real \(\lambda\), the exponential representation of cosine gives
\(|\cos(\lambda z)|\le e^{|\lambda|\varepsilon}\) on
\(|\operatorname{Im}z|<\varepsilon\). Thus the actual full-strip norm is finite. No claim that the general smooth coefficient construction depends holomorphically on arbitrary complex coefficients is needed for this explicit family.

**Solution 4.** Differentiate the identity in a real coefficient direction \(v=(v_0,v_1,v_2)\in\mathbb C^3\). Since \(F\) does not vary with \(b\), at zero it gives
\[
0=t^3D_bQ(t,0)[v]
  +Q(t,0)(v_0+v_1t+v_2t^2)
  +\sum_{j=0}^2D_bR_j(0)[v]t^j.
\]
The first summand has its first three \(t\)-jets zero. Taking the degree-below-three Taylor coefficients therefore gives
\[
D_bR(0)[v]=
\begin{pmatrix}-2&0&0\\-3&-2&0\\1&-3&-2\end{pmatrix}v.
\]
The differential is complex-linear because multiplication of finite complex jets is complex-linear in \(v\); no parameter holomorphy was assumed. The complex determinant is \(-8\). For the real map underlying a complex-linear matrix, the determinant is its complex determinant times its conjugate, so it is \(64\). Successive solution of the triangular equations gives
\[
v_0=-\frac{y_0}{2},\qquad
v_1=-\frac{y_1}{2}+\frac{3y_0}{4},\qquad
v_2=-\frac{y_2}{2}+\frac{3y_1}{4}-\frac{11y_0}{8}.
\]
The real determinant formula also follows directly by grouping real and imaginary coordinates: the real matrix is two copies of this real triangular matrix, whose determinants multiply.

**Solution 5.** Define
\[
B(t,x)=\frac{h(x)}{t^2+x^2}\quad(x\ne0),\qquad
B(t,0)=0.
\]
For each fixed derivative order, derivatives of \(h\) are \(e^{-1/x^2}\) times finite sums of powers of \(x^{-1}\). Derivatives of \((t^2+x^2)^{-1}\), on a fixed bounded \(t\)-interval and \(0<|x|<1\), are bounded by some \(C|x|^{-N}\): every denominator is at least a power of \(x^2\), and every numerator is a bounded polynomial in \(t,x\). Leibniz therefore gives, for every \(a,b\),
\[
|\partial_t^a\partial_x^bB(t,x)|
\le C_{a,b}|x|^{-N_{a,b}}e^{-1/x^2},
\]
uniformly for bounded \(t\). This tends to zero faster than every power of \(|x|\). Each derivative consequently extends by zero across \(x=0\). The extensions are the actual derivatives: use the one-variable fundamental theorem of calculus in \(x\) on segments approaching zero, and the zero trace for \(t\)-derivatives; induction gives every order. Thus \(B\) is smooth, including at the origin. It is not identically zero. The identity
\[
0=B(t,x)f(t,x)-h(x)
\]
is a nontrivial smooth division of zero, distinct from zero quotient and zero remainder.

One preparation is \(f=1\cdot(t^2+x^2)\). For another, set
\[
P'(t,x)=t^2+x^2+h(x),\qquad
c'(t,x)=1-\frac{h(x)}{t^2+x^2+h(x)}\quad(x\ne0),
\qquad c'(t,0)=1.
\]
The denominator is at least \(x^2\), because \(h\ge0\). Its derivatives have polynomial reciprocal-power bounds as above; derivatives of \(h\) are bounded, and each differentiated term in the correction has a derivative of \(h\) as a factor. The same exponential estimates prove a smooth zero extension of the correction and hence smoothness of \(c'\). At \((0,0)\), \(c'=1\), so it is nonvanishing on a sufficiently small neighborhood by continuity. For \(x\ne0\) it equals \((t^2+x^2)/(t^2+x^2+h(x))\), and multiplication gives \(c'P'=f\); the identity holds at \(x=0\) as well. The new constant coefficient \(x^2+h(x)\) vanishes at zero and differs from \(x^2\) arbitrarily close to zero. Both units and factors are real. The divisor has distinguished order two because \(f(0,0)=\partial_tf(0,0)=0\), \(\partial_t^2f(0,0)=2\). The nonzero flat function \(h\) is not holomorphic near zero: its Taylor series is identically zero, whereas its values are nonzero for \(x\ne0\). These are smooth constructions, so holomorphic germ uniqueness is unaffected.

**Solution 6.** Choose \(\chi\in C_c^\infty((-2,2))\) equal to one on a neighborhood of \([-1,1]\). Such a cutoff is supplied by the proved smooth cutoff construction. Put
\[
H(t,x)=\begin{cases}\chi(t)g(t,x),&|t|<2,\\0,&|t|\ge2.\end{cases}
\]
The support of \(\chi\) has positive distance from the endpoints, so \(H\) is identically zero on their neighborhoods and the zero extension is smooth. All derivatives have one fixed compact \(t\)-support. For \(K\Subset V\), a mixed derivative is a finite sum of products of a fixed cutoff derivative with a derivative of \(g\) on the compact set \(\operatorname{supp}\chi\times K\). Each product is bounded, so its \(t\)-integral is bounded by the fixed support length times that bound. Since \(\chi\) is independent of \(x\), \(\partial_x^\eta H\) is the same extension applied to \(\partial_x^\eta g\). Smooth division of this extended dividend restricts to division of \(g\) for \(|t|<1\), after any further shrink needed by the fixed divisor's prepared coefficient map and nonvanishing unit.

For the domain counterexample, take \(a>0\) tending to zero and a germ \(g_a\) supplied only on \((-a/2,a/2)\times V\). Even a constant formula does not enlarge the declared data domain. Every positive fixed interval contains points outside some member's supplied domain. For each particular germ, one may choose a cutoff supported in its own interval and conclude division on a smaller neighborhood inside it. A common neighborhood for all dividends requires that all are actually supplied on a common domain, as for globally smooth dividends. It is not a consequence of the word “germ.”

**Solution 7.** Fix an auxiliary multiindex \(\eta\) and compact \(K\) in the parameter set. Write
\[
A_{\nu,K,\eta}=
\sup_{x\in K}\int_{\mathbb R}
\bigl(|\partial_x^\eta H(t,x)|
      +|\partial_t^\nu\partial_x^\eta H(t,x)|\bigr)\,dt.
\]
This is finite by the fixed support and compact-uniform smooth bounds. Integration by parts has no endpoint terms and gives
\(|\partial_x^\eta\widehat H(\tau,x)|
\le A_{\nu,K,\eta}|\tau|^{-\nu}\) for \(\tau\ne0\), while the first \(L^1\) term bounds it everywhere.

For \(j\ge1\), the support of \(\psi_j\) lies where
\(2^{j-1}\le|\tau|\le2^{j+1}\), and has length at most \(2^{j+2}\). The cutoffs have a fixed uniform bound. On \(|\operatorname{Im}z|<2^{-j}\), the exponential satisfies \(|e^{iz\tau}|\le e^2\). Therefore
\[
\sup_{|\operatorname{Im}z|<2^{-j},\,x\in K}
|\partial_x^\eta H_j(z,x)|
\le C_\nu A_{\nu,K,\eta}2^{j(1-\nu)}.
\]
For \(j=0\), compact Fourier support gives the same required finite estimate using the first \(L^1\) term. The assumed fixed operators commute with \(x\)-derivatives. Applying their estimates, on the real \(t\)-axis, gives quotient terms bounded by
\(CA_{\nu,K,\eta}2^{j(1-\nu+L_q)}\), and remainder terms by the same expression with \(L_r\). Choose \(\nu=L_q+2\) or \(L_r+2\). Each term is bounded by \(CA_{\nu,K,\eta}2^{-j}\); hence the tail after \(N\) is at most
\[
C A_{\nu,K,\eta}\sum_{j>N}2^{-j}
=C A_{\nu,K,\eta}2^{-N}.
\]
This proves uniform convergence of every mixed real derivative. On local real coordinate boxes, applying the fundamental theorem of calculus to partial sums and taking the uniform limits shows that the limit of each derivative is the derivative of the limit. Repeating this for every order gives a smooth quotient and smooth coefficient remainders.

The Fourier cutoffs telescope:
\(\sum_{j=0}^N\psi_j(\tau)=\phi(2^{-N}\tau)\).
The compactly supported smooth dividend has integrable Fourier transform by two integrations by parts. Fourier inversion and dominated convergence therefore give \(\sum_jH_j(t,x)=H(t,x)\) for real \(t\). For every mixed derivative, use further integration by parts to make \(|\tau|^a\partial_x^\eta\widehat H\) integrable; the same argument gives differentiated reconstruction. Summing each strip-division identity now gives the smooth division identity on the real axis.

The widths \(\varepsilon_j\) decrease to zero; the quotient terms are not given on one common complex strip. A general smooth dividend cannot imply a holomorphic quotient there. At \(b=0\), division forces the quotient to be its dividend minus its degree-below-\(k\) Taylor polynomial, divided by \(t^k\). A nonzero smooth flat dividend near zero, such as \(e^{-1/t^2}\) extended by zero and cut off away from zero, produces a nonzero flat quotient. If that quotient were holomorphic near zero, its zero Taylor series would make it identically zero, a contradiction. For real \(H\), the real even Fourier cutoffs yield conjugation-symmetric pieces, so conjugation-compatible strip operators retain the real-valued division option.

**Solution 8.** Direct monic polynomial division gives
\[
g=(t^2+x)P+(x-y)t^2+x^2t+y(2-x).
\]
Indeed,
\((t^2+x)P=t^5-x^2t+yt^2+xy\); adding the displayed remainder gives \(t^5+xt^2+2y\). For the two original divisors, respectively, use
\[
q_{\mathrm{real}}=\frac{t^2+x}{1+t^2},\qquad
q_{\mathrm{complex}}=\frac{t^2+x}{1+it},
\]
and retain that same degree-two remainder. Both denominators are nonvanishing for real \(t\), so these quotients are smooth on the actual real domain. The first divisor, quotient and remainder are real; in the second case the divisor and quotient are complex valued while the remainder happens to be real. At the mark \((0,0,0)\), each divisor has distinguished order three and a unit with value one. This verifies absorption of the unit after division by the prepared polynomial; it does not assume that an arbitrary finite-order divisor was already given in prepared form.

