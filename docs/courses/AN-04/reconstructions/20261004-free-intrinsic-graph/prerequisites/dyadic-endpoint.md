# The dyadic endpoint and localized operator bounds

This is a modified, bounded selection of AN03-U008, *Singularities along a
submanifold and smooth boundary passage*, Section 1. It retains that
section's dyadic, Schur and local Fourier proofs, with the summations and
extension arguments written out. Only the sequence endpoint
\(B^s_{2,\infty}\), and the comparison \(B^s_{2,2}=H^s\), are used here.
The original lesson's other sequence indices remain outside this selection.

Original principal author and publisher: AN-03 course-writing task /
AN-03 local course project, 2026. Earlier modification: AN-03 course-writing task and
OpenAI Codex. This selection and its connecting arguments: GPT-6 Astra
(OpenAI), Ultra, 4 October 2026; publisher: AN-04 local course project.

Original text: CC0.

## B0. Exact inputs and scope

The [measure companion, M0–M8](measure-and-l2.md) supplies measure,
Tonelli, Cauchy–Schwarz, completeness and smooth density. The
[Fourier companion, L0–L3](fourier-l2.md) supplies inversion, Parseval
and measurable multipliers with
\(\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx\) and inverse factor
\((2\pi)^{-n}\). Its earlier Schwartz proof includes integration by
parts. Smooth cutoffs are constructed in
[U001 P14.3](../../20261004-free-stationary-phase/exponential-prerequisite-completions.md#p14-3-exponential-decay-and-the-flat-cutoff-function).
The chart integrals below use the complete compact substitution proof
[U001 P21.3–P21.4](../../20261004-free-stationary-phase/change-of-variables-prerequisite-completions.md#p21-3-the-full-compact-jordan-change-of-variables-theorem).
M8 identifies these continuous compact integrals with Lebesgue integrals.

All dimensions here satisfy \(n\geq1\). For \(n=0\) there is one point,
the only block is the identity, and each assertion reduces to a
finite-dimensional norm estimate. Finite matrix ranks are allowed:
apply the scalar bounds to the entries and sum finitely many norms.

The analytic estimate B4 concerns the displayed symbol operator.
B6 applies it to an operator once its proper local symbol and smooth
remainder representation has been supplied. Establishing that
representation, composition and the symbol of a commutator belongs to
the separate [operator prerequisite P2, O1–O6](ordinary-operator-calculus.md);
none is asserted as a consequence of an endpoint estimate.

## B1. Dyadic norms and distributional convergence

Put \(A_0=\{|\xi|<2\}\) and
\(A_j=\{2^j\leq|\xi|<2^{j+1}\}\), \(j\geq1\), and let
\(\Pi_j=\mathcal F^{-1}\mathbf1_{A_j}\mathcal F\).
These sets are disjoint and exhaust frequency space, with their boundaries
assigned by the displayed inequalities.
Use
\[
 \|u\|_{H^s}^2=(2\pi)^{-n}
       \int\langle\xi\rangle^{2s}|\widehat u(\xi)|^2\,d\xi,
 \qquad
 \|u\|_{B^s}=\sup_{j\geq0}2^{js}\|\Pi_j u\|_2 .
 \tag{B1}
\]
Membership means that the Fourier transform is a locally square-integrable
function with the indicated finite norm. Such a function defines a tempered
distribution: on each annulus use Cauchy–Schwarz against a Schwartz test
function, and then sum a geometric series, choosing its decay power larger
than \(n/2+|s|+1\). Fourier transpose and inversion therefore give the
claimed distribution \(u\).

On \(A_j\), \(c_s2^{js}\leq\langle\xi\rangle^s\leq C_s2^{js}\).
Parseval gives
\[
 \|u\|_{H^s}^2\asymp\sum_{j\geq0}
                 2^{2js}\|\Pi_j u\|_2^2,\qquad
 H^s\subset B^s\subset H^{s-\epsilon}\quad(\epsilon>0).
 \tag{B2}
\]
The first inclusion bounds a supremum by the square sum; the second
uses \(\sum_{j\geq0}2^{-2j\epsilon}<\infty\). The partial block sums
converge in \(H^{s-\epsilon}\) and hence in tempered distributions, by
the same weighted Cauchy–Schwarz test estimate.

A smooth finite-overlap dyadic partition gives an equivalent norm.
Indeed each new block is a uniformly bounded Fourier multiplier on a
fixed number of neighboring old blocks. Its weighted norm is bounded
by their finite sum, since their indices differ by a bounded integer.
Conversely, on an old annulus the smooth partition sums to one and only
that bounded number of terms occurs. The triangle inequality gives the
reverse estimate. This also proves independence of the starting radius.
A smooth partition exists: take a radial smooth cutoff \(\rho\), equal
to one on the unit ball and zero outside the ball of radius two; the
differences \(\rho(2^{-j-1}\xi)-\rho(2^{-j}\xi)\), together with
\(\rho(\xi)\), telescope to one.

We will also use Schwartz density in every \(H^s\). Truncate
\(\widehat u\) to a ball; the weighted tail tends to zero by monotone
convergence. On the ball the weight and its reciprocal are bounded.
The compact smooth approximation in M7, multiplied by a fixed smooth
cutoff supported in a slightly larger ball, approximates that truncation
in the weighted norm. Inverse Fourier transforms of these compact smooth
functions are Schwartz. The same construction approximates simultaneously
in two fixed Sobolev norms on their intersection. Completeness follows
by multiplying the Fourier transform by \(\langle\xi\rangle^s\) and
using completeness of \(L^2\).

## B2. The local frequency Sobolev estimate

Let \(v\) be smooth on \(B(y,2R)\), \(R>0\). For each multiindex
\(\beta\) choose an integer \(q>|\beta|+n/2\). There is a constant
depending only on \(n,q,\beta\), such that
\[
 R^{|\beta|}|\partial^\beta v(y)|
 \leq C\sum_{|\gamma|\leq q}
              R^{|\gamma|-n/2}
                 \|\partial^\gamma v\|_{L^2(B(y,2R))}.
 \tag{B3}
\]
Here and below one may use any two fixed nested balls after rescaling.
To prove it at \(y=0,R=1\), choose a compact smooth cutoff \(\chi\)
in \(B(0,2)\), equal to one near the closed unit ball. Fourier inversion,
followed by Cauchy–Schwarz, bounds
\[
 |\partial^\beta(\chi v)(0)|
 \leq (2\pi)^{-n}
 \left(\int |\zeta|^{2|\beta|}\langle\zeta\rangle^{-2q}\,d\zeta\right)^{1/2}
 \|\langle\zeta\rangle^q\widehat{\chi v}\|_2 .
 \tag{B4}
\]
The integral is finite: its large-annulus terms are bounded by
\(C2^{j(n+2|\beta|-2q)}\), using the volume bound by a containing
cube, and its part in the unit ball is bounded. The multinomial formula
expands \((1+|\zeta|^2)^q\) as a finite positive sum of monomial squares.
Parseval identifies the last norm with a constant times a finite sum
of \(L^2\) derivative norms of \(\chi v\). The product rule and bounded
cutoff derivatives give (B3). Substitute \(x=y+Rz\) and use the affine
change of variables to obtain the stated powers of \(R\).
Translation makes the constant independent of \(y\).

## B3. Schur's estimate and the summable block matrix

Suppose a measurable kernel satisfies
\[
 \sup_\xi\int|K(\xi,\theta)|\,d\theta\leq A,\qquad
 \sup_\theta\int|K(\xi,\theta)|\,d\xi\leq B.
 \tag{B5}
\]
For bounded compact inputs, weighted Cauchy–Schwarz gives
\[
 |Tf(\xi)|^2
 \leq\left(\int|K(\xi,\theta)|\,d\theta\right)
       \int|K(\xi,\theta)||f(\theta)|^2\,d\theta .
\]
Tonelli and (B5) then give \(\|Tf\|_2^2\leq AB\|f\|_2^2\).
Truncation and \(L^2\) completeness extend this estimate to every
\(L^2\) input, independently of the approximating sequence.

If blocks of an operator satisfy
\[
 2^{l(s-d)-js}\|\Pi_lT\Pi_j\|_{2\to2}
       \leq C2^{-\epsilon|l-j|}\quad(l,j\geq0),
 \tag{B6}
\]
the weighted norm of each output block is bounded by the convolution
of \(c_k=C2^{-\epsilon|k|}\), \(k\in\mathbb Z\), with the nonnegative
input sequence \(a_j=2^{js}\|\Pi_j u\|_2\), extended by zero.
For the supremum norm this is at most
\((\sum_kc_k)\sup_ja_j\). For the square norm, Cauchy–Schwarz yields
\((\sum_k c_k a_{l-k})^2\leq(\sum_kc_k)\sum_kc_k a_{l-k}^2\).
Sum in \(l\) and use Tonelli to obtain the same bound in \(\ell^2\).
Thus (B6) proves both the \(B^s\to B^{s-d}\) bound and its Sobolev
counterpart. Finite block sums suffice for the estimate; convergence
and consistency for infinite inputs are justified in B4 and B5.

## B4. The ordinary symbol endpoint

Let \(p(x,\theta)\) be smooth, compactly supported in \(x\) in one
fixed compact set, and satisfy, for all \(\alpha,\beta\),
\[
 |\partial_x^\beta\partial_\theta^\alpha p(x,\theta)|
       \leq C_{\alpha,\beta}\langle\theta\rangle^{d-|\alpha|}.
 \tag{B7}
\]
On Schwartz inputs put
\(Pu(x)=(2\pi)^{-n}\int e^{ix\cdot\theta}p(x,\theta)\widehat u(\theta)\,d\theta\).
This integral and each \(x\) derivative converge absolutely and produce
a compactly supported smooth function. Fubini gives its Fourier kernel
\[
 \widehat{Pu}(\xi)=(2\pi)^{-n}
       \int\widehat p_x(\xi-\theta,\theta)\widehat u(\theta)\,d\theta,
 \qquad
 |\widehat p_x(\eta,\theta)|
       \leq C_M\langle\theta\rangle^d\langle\eta\rangle^{-M}.
 \tag{B8}
\]
For the last bound, integrate by parts with \((1-\Delta_x)^N\);
choose \(2N\geq M\), and use the fixed compact support and (B7).
This proves a bound using finitely many \(x\) derivatives of \(p\).

If \(|l-j|\leq2\), Schur's estimate and the integrability of
\(\langle\eta\rangle^{-M}\), \(M>n\), give
\(\|\Pi_lP\Pi_j\|\leq C2^{jd}\). If \(|l-j|>2\), then
\(|\xi-\theta|\geq c2^{\max(j,l)}\) on \(A_l\times A_j\).
The volumes of these sets are at most \(C2^{nl},C2^{nj}\);
Schur therefore gives
\[
 \|\Pi_lP\Pi_j\|
 \leq C_M 2^{jd}2^{-M\max(j,l)}2^{n(j+l)/2}.
 \tag{B9}
\]
After the weights in (B6), put \(t=s-d\). For \(l\geq j\) its
power of two is
\((n-M)j+(n/2+t-M)(l-j)\).
For \(j\geq l\) it is
\((n-M)l+(n/2-t-M)(j-l)\).
Choose \(M>n+|t|+1\). Both expressions are at most
\(-\epsilon|l-j|\) for some \(\epsilon>0\); the neighboring blocks
obey (B6) after enlarging the constant. B3 proves, for every real \(s,d\),
\[
 P:H^s\longrightarrow H^{s-d},\qquad
 P:B^s\longrightarrow B^{s-d}.
 \tag{B10}
\]

Here is the extension argument, including the endpoint.
Density from B1 gives the unique Sobolev extension. Two choices of
Sobolev exponent agree on their intersection, by simultaneous Schwartz
approximation in B1 and distributional convergence. If \(u\in B^s\),
its block partial sums converge in \(H^{s-\delta}\), \(\delta>0\).
The corresponding outputs converge in \(H^{s-d-\delta}\) and hence,
on each fixed frequency block, in \(L^2\). The uniformly bounded
weighted output blocks therefore converge to those of the Sobolev
extension and satisfy the same supremum bound. This proves (B10)
without a false assertion of Schwartz density in \(B^s_{2,\infty}\).

## B5. Multiplication and changes of coordinates

Multiplication by a compact smooth function is the special case
\(p(x,\theta)=\chi(x)\), \(d=0\), of B4.
For a chart change \(\kappa:U\to V\), with smooth inverse, consider
\[
 Tu(x)=a(x)u(\kappa(x)),\qquad a\in C_c^\infty(U),
 \tag{B11}
\]
extended by zero outside \(U\); only a compact subset of \(V\) is
sampled. On smooth inputs, the product and chain rules express each
derivative of order at most the nonnegative integer \(q\) as a finite
sum of derivatives of \(u\), composed with \(\kappa\), times smooth
compact coefficients. Compact change of variables bounds their
\(L^2\) norms. Parseval and the polynomial identity used in B2 show
that the sum of squared derivatives up to \(q\) is equivalent to
\(\|u\|_{H^q}^2\). Hence \(T:H^q\to H^q\).

Its adjoint on smooth inputs is
\[
 T^*v(y)=\overline{a(\kappa^{-1}y)}
             |\det D\kappa^{-1}(y)|\,v(\kappa^{-1}y),
 \tag{B12}
\]
on \(V\), zero elsewhere. The coefficient is compactly supported in
\(V\); (B12) has the same positive-integer bounds. The Fourier
pairing proves
\[
 \|f\|_{H^{-q}}=
   \sup_{\phi\in\mathcal S,\ \|\phi\|_{H^q}\leq1}
                          |\langle f,\phi\rangle_{L^2}|.
 \tag{B13}
\]
For completeness, the upper bound is weighted Cauchy–Schwarz.
In Fourier variables the supremum over the entire unit ball of
weighted \(L^2\) is attained in the direction
\(\langle\xi\rangle^{-2q}\widehat f(\xi)\), after normalization;
truncate and approximate that function in the \(H^q\) norm by B1
to obtain the same supremum over Schwartz functions. The zero vector
case is immediate. The same identity also defines the distributional
pairing when \(f\) has negative order.
Use (B12) in (B13) to obtain \(T:H^{-q}\to H^{-q}\), first for
Schwartz inputs and then by density. This extension is the
distributional pullback: its pairing with every compact smooth test
function is the transpose formula (B12). The adjoint test function
is itself compact smooth, so convergence in distributions preserves it.

Choose integers \(a_0<s<b_0\). For either \(q=a_0\) or \(q=b_0\),
the Sobolev bound and annular weights give
\[
 \|\Pi_lT\Pi_j\|_{2\to2}\leq C_q2^{(j-l)q}.
 \tag{B14}
\]
After multiplication by \(2^{(l-j)s}\), choose \(a_0\) when
\(j\geq l\) and \(b_0\) when \(j<l\). This is (B6), \(d=0\),
with \(\epsilon=\min(s-a_0,b_0-s)>0\).
The block partial sums converge in a Sobolev space below \(s\);
the proof of B4 therefore identifies the limit with the actual
distributional pullback and proves boundedness on \(B^s\).
Applying the same argument to the inverse chart change proves that
the local definition is independent of coordinates. Frame changes
are finite sums of smooth multiplications, so it is also independent
of a chosen smooth finite-rank frame.

## B6. Local use with a supplied proper representation

Suppose \(P\) is a distributional operator for which, for each output
cutoff \(\chi\), proper support provides a compact input cutoff \(\psi\)
and a representation
\[
 \chi Pu=\operatorname{Op}(p)(\psi u)+R(\psi u),
 \tag{B15}
\]
where \(p\) satisfies (B7) and \(R\) has a smooth kernel compactly
supported in both variables. Then
\[
 P:B^s_{\mathrm{loc}}\longrightarrow B^{s-d}_{\mathrm{loc}}.
 \tag{B16}
\]
Indeed \(\psi u\in B^s\) by the definition of the local space.
B4 estimates the first term. For the second, write
\(R f(x)=\langle f,k(x,\cdot)\rangle\). Its \(x\) derivatives are
the pairings with \(\partial_x^\alpha k(x,\cdot)\); this follows
from Taylor's formula in the compact smooth test topology. Weighted
Fourier Cauchy–Schwarz bounds these by
\(\|f\|_{H^{s-\delta}}\|\partial_x^\alpha k(x,\cdot)\|_{H^{-s+\delta}}\).
The second factor is uniformly finite: integration by parts gives
uniform rapid Fourier decay of the compact smooth kernels. Thus
\(Rf\) is compact smooth with every derivative bounded by
\(C_\alpha\|f\|_{B^s}\), using B2.
Another Fourier integration by parts proves that its \(H^t\) norm,
and hence its \(B^t\) norm, has that bound for every fixed \(t\).
Choose \(t=s-d\), which proves (B16).

For an ordinary properly supported pseudodifferential operator, (B15)
is proved in [P2, O5](ordinary-operator-calculus.md#o5-proper-operators-and-the-actual-local-representation).
B6 proves exactly the implication from that assertion to the endpoint
mapping property. The representation and the analytic estimate have
separate complete proofs.

## Free human comparison

[Sá Barreto and Wang, author draft dated 25 October 2018](https://www.math.purdue.edu/~sabarre/Papers/TripleInt.pdf),
Section 2.1, supplies the precise Besov endpoint formulation used
for conormal distributions. Its referenced normal-form proof is not
adopted here. The complete analytic arguments used in this companion
are B1–B6 and their exact earlier programme inputs. The author's PDF,
its prose and its bibliography are not reproduced.
