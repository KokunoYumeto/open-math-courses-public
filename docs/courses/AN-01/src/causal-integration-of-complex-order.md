# Causal integration of complex order

*Reconstructed by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition by GPT-6.1 Sol (OpenAI). Original exposition: CC0. Linked programme prerequisites retain their stated licences. Self-checked by the writing AI.*

A derivative on the whole line loses an integration constant. Causal support—vanishing before time zero—makes that constant impossible. We construct the resulting integration group for every complex order and every causal distribution. A beta integral proves its composition law, and a logarithmic distribution describes its infinitesimal change of order.

The scalar constructions were compared with Sergey Lototsky's freely accessible *Basics of Gamma and Beta functions*, both pages, and the reflection argument in Imperial College London's *M2PM3 Examination Solutions 2011*, Question 3. The complete proofs and precise programme prerequisites are supplied here and linked below. In particular, the contour calculation is proved from Green's formula, and the beta calculation uses iterated one-dimensional substitutions.

## Normalization fixes the integer cases

We write \(H=\boldsymbol1_{\{x>0\}}\), \(\delta_0(\phi)=\phi(0)\), and \(\partial v(\phi)=-v(\phi')\). All distribution pairings are complex linear. A distribution is **causal** when its support is contained in \([0,\infty)\); write \(\mathcal D'_+\) for this space. For real \(x>0\), \(x^a=\exp(a\log x)\) always uses the real logarithm.

The supplied [Gamma foundations](../prerequisites/U011-free-foundations/gamma-foundations-U016.md), G0–G2 and W4a–W4e, prove the convergence of the Gamma integral, the reciprocal product, its nonvanishing tail, recurrence and zeros. They give an entire function \(G=1/\Gamma\) with

\[
G(z)=zG(z+1),\qquad G(1)=1,\qquad
G(z)=ze^{\gamma z}\prod_{j=1}^{\infty}(1+z/j)e^{-z/j},
\tag{1.1}
\]

where \(\gamma=\lim_{N\to\infty}(\sum_{j=1}^Nj^{-1}-\log N)\). Its zeros are simple and exactly \(0,-1,-2,\ldots\). Thus \(\Gamma=1/G\) has no zeros, is meromorphic, and satisfies

\[
\operatorname*{Res}_{z=-m}\Gamma(z)=\frac{(-1)^m}{m!},
\qquad m=0,1,\ldots.
\tag{1.2}
\]

These facts include the integral \(\Gamma(a)=\int_0^\infty x^{a-1}e^{-x}\,dx\) for \(\operatorname{Re}a>0\). The foundation's licence and original selection history are retained with that proof.

The normalized family constructed in [Finite parts of singular powers](finite-parts-of-singular-powers.md), N1, is shifted by one:

\[
R_a=C_{a-1},\qquad
R_a(x)=G(a)x^{a-1}H(x)\quad(\operatorname{Re}a>0).
\tag{1.3}
\]

The family is entire in every test pairing, has causal support, and obeys

\[
\partial_xR_a=R_{a-1},\qquad R_1=H,\qquad
R_0=\delta_0,\qquad R_{-m}=\delta_0^{(m)}\quad(m\ge0).
\tag{1.4}
\]

Here is the continuation formula used throughout this lesson. Given a compact parameter set, choose an integer \(N\ge0\) with \(\operatorname{Re}(a+N)>0\) on a neighborhood of that set. Then

\[
R_a=\partial_x^NR_{a+N},\qquad
R_a(\phi)=(-1)^NG(a+N)
       \int_0^\infty x^{a+N-1}\phi^{(N)}(x)\,dx.
\tag{1.5}
\]

For clarity, its compatibility has a direct check. Integrating the formula with \(N+1\) by parts gives the formula with \(N\), because the endpoint term \(x^{a+N}\phi^{(N)}(x)\) vanishes at zero and infinity and \(G(a+N)=(a+N)G(a+N+1)\). Consecutive half-plane formulas therefore agree wherever both apply. Spatial differentiation in (1.5) gives the formula for \(R_{a-1}\) with \(N+1\). At \(a=1\) the density is \(H\), and \(-\int_0^\infty\phi'=\phi(0)\) proves the remaining integer values.

If the tests have support in \([-M,M]\), take \(M\ge1\). On a compact parameter set there are constants \(0<\sigma\le\operatorname{Re}(a+N)\le A\). Each fixed parameter derivative of the integral in (1.5) is bounded by a constant times
\[
p_N(\phi)\left(\int_0^1x^{\sigma-1}|\log x|^j\,dx+
                      \int_1^M x^{A-1}(1+|\log x|^j)\,dx\right),
\qquad
p_N(\phi)=\max_{0\le l\le N}\|\phi^{(l)}\|_\infty.
\tag{1.6}
\]
The first integral is \(j!/\sigma^{j+1}\), as proved in G1. Derivatives of \(G\) are bounded on parameter compacts. The difference-quotient estimate in G2 therefore proves holomorphy, all parameter derivatives and their common finite-order bounds. No value at a negative integer is obtained by multiplying a divergent function by zero.

## The beta integral computes composition

For \(\operatorname{Re}a,\operatorname{Re}b>0\), set

\[
B(a,b)=\int_0^1 t^{a-1}(1-t)^{b-1}\,dt.
\tag{2.1}
\]

**Theorem 2.1 (Euler's beta identity).** On this parameter region,

\[
\Gamma(a)\Gamma(b)=\Gamma(a+b)B(a,b).
\tag{2.2}
\]

The beta function is jointly holomorphic there and never zero.

**Proof.** Absolute Fubini, proved in the [integration foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §15.1, identifies the product of the two Gamma integrals with

\[
\int_0^\infty\int_0^\infty e^{-(s+t)}s^{a-1}t^{b-1}\,dt\,ds.
\tag{2.3}
\]

Its absolute integral is \(\Gamma(\operatorname{Re}a)\Gamma(\operatorname{Re}b)<\infty\). For each \(s>0\), translate the inner variable by \(r=s+t\). Change the order on the region \(0<s<r<\infty\), and then substitute \(s=r\theta\) in the inner integral. These are one-dimensional affine substitutions, already proved in §15.1. Applying them also to the absolute values verifies each use of Fubini. The result is

\[
\begin{aligned}
\int_0^\infty e^{-r}\int_0^r s^{a-1}(r-s)^{b-1}\,ds\,dr
&=\left(\int_0^\infty e^{-r}r^{a+b-1}\,dr\right)
  \left(\int_0^1\theta^{a-1}(1-\theta)^{b-1}\,d\theta\right).
\end{aligned}
\tag{2.4}
\]

This proves (2.2), and the nonzero finite Gamma factors prove nonvanishing.

Fix a center \((a_0,b_0)\) in the region, and choose \(\rho>0\) smaller than both real parts. Expand
\[
t^{a_0+h-1}(1-t)^{b_0+k-1}
=t^{a_0-1}(1-t)^{b_0-1}
 \sum_{p,q\ge0}\frac{h^pk^q(\log t)^p(\log(1-t))^q}{p!\,q!}.
\tag{2.4a}
\]
For \(|h|,|k|\le\rho\), the sum of the absolute values is bounded by
\(t^{\operatorname{Re}a_0-1-\rho}(1-t)^{\operatorname{Re}b_0-1-\rho}\), an integrable function. Absolute Fubini permits termwise integration. The resulting double power series converges absolutely on this polydisk and proves joint holomorphy on its interior. All mixed differentiated integrals converge locally uniformly: split at \(t=1/2\), use G1 at the possibly singular endpoint, and bound the other logarithm there. \(\square\)

**Theorem 2.2 (all complex orders compose).** Causal convolution is defined for every \(a,b\in\mathbb C\), and

\[
R_a*R_b=R_{a+b}.
\tag{2.5}
\]

Its pairing with a compact smooth test is jointly entire in \(a,b\).

**Proof.** If \(s,t\ge0\) and \(s+t\) lies in a compact interval with upper endpoint \(M\), both \(s,t\) lie in \([0,M]\). The inverse image is also closed. Thus addition on the two fixed supports is proper. [Convolution as addition of supports](convolution-as-addition-of-supports.md), B0–B2 and Theorem 1.1, supplies the distributional convolution, support inclusion and derivative transfer.

For positive real parts, Fubini identifies that distribution with ordinary convolution. On \(x>0\), the affine substitution \(s=x\theta\) gives

\[
\begin{aligned}
(R_a*R_b)(x)
&=G(a)G(b)\int_0^x s^{a-1}(x-s)^{b-1}\,ds\\
&=G(a)G(b)x^{a+b-1}B(a,b)=R_{a+b}(x).
\end{aligned}
\tag{2.6}
\]

The absolute double integral over \(s,t\ge0,\ s+t\le M\) is bounded by the product of the two finite power integrals over \([0,M]\). Hence this is equality of locally integrable distributions across zero as well; no distribution concentrated at zero is omitted.

For arbitrary \(a,b\), choose \(N\) with both shifted real parts positive. Then

\[
\begin{aligned}
R_a*R_b
&=(\partial_x^NR_{a+N})*(\partial_x^NR_{b+N})\\
&=\partial_x^{2N}(R_{a+N}*R_{b+N})
=\partial_x^{2N}R_{a+b+2N}=R_{a+b}.
\end{aligned}
\tag{2.7}
\]

Finally \(f(z)=R_z(\phi)\) is entire. Its local Taylor series at \(a_0+b_0\) composed with \(z=a+b\) is an absolutely convergent double power series when \(|a-a_0|+|b-b_0|\) is smaller than the Taylor radius. This proves the joint assertion. The Taylor theorem used here is proved in [Cauchy kernels and boundary limits](cauchy-kernels-and-boundary-limits.md), Corollary 2.2. \(\square\)

## Causal support removes integration constants

For any finite number of nonnegative summands, a bound on their sum bounds each summand. Thus all the required addition maps are proper. Theorems 1.1 and 3.1 of the convolution lesson make \(\mathcal D'_+\) a commutative associative algebra with identity \(\delta_0\), including zero factors.

**Theorem 3.1 (the causal integration group).** Set

\[
J_a u=R_a*u,\qquad a\in\mathbb C,\quad u\in\mathcal D'_+.
\tag{3.1}
\]

These linear maps preserve causal support, and

\[
J_aJ_b=J_{a+b},\qquad J_0=\mathrm{id},\qquad
J_a^{-1}=J_{-a},\qquad \partial_xJ_a=J_{a-1}.
\tag{3.2}
\]

For each \(u\), \(J_a u\) is weakly entire. For integers \(m\ge0\), \(J_{-m}u=\partial_x^mu\). If \(m\ge1\), \(J_m u\) is the unique causal solution of \(\partial_x^mv=u\).

**Proof.** Theorem 2.2 and the proper-support associativity give

\[
R_a*(R_b*u)=(R_a*R_b)*u=R_{a+b}*u.
\tag{3.3}
\]

Now (1.4) and derivative transfer give (3.2), the negative integer assertion and \(\partial_x^mJ_m u=u\). Conversely, any causal solution \(v\) satisfies

\[
J_m u=R_m*\partial_x^mv
=(\partial_x^mR_m)*v=\delta_0*v=v.
\tag{3.4}
\]

For the parameter assertion, fix a test \(\phi\), and choose \(M>0\) larger than the positive part of its support. Take \(\chi\in C_c^\infty(\mathbb R)\) equal to one on a neighborhood of \([0,M]\). The convolution pairing is the compact tensor pairing with \(\chi(s)\chi(t)\phi(s+t)\). By B1 of the convolution lesson,
\(\psi(s)=\chi(s)\langle u(t),\chi(t)\phi(s+t)\rangle\) is a compact smooth test independent of \(a\). Thus
\(\langle J_a u,\phi\rangle=\langle R_a,\psi\rangle\) is entire. The same formula transfers every parameter derivative. \(\square\)

When \(f\) is locally integrable and zero on the negative half-line, positive-real-part orders have the concrete form

\[
(J_af)(x)=G(a)\int_0^x(x-t)^{a-1}f(t)\,dt
\quad\text{for almost every }x>0.
\tag{3.5}
\]

Indeed, on \(0<x<M\), Tonelli and an affine substitution give the absolute bound

\[
\int_0^M |G(a)|\int_0^x(x-t)^{\operatorname{Re}a-1}|f(t)|\,dt\,dx
\le |G(a)|\,\frac{M^{\operatorname{Re}a}}{\operatorname{Re}a}
          \int_0^M|f(t)|\,dt.
\tag{3.6}
\]

Fubini now proves both the almost-everywhere existence and the distributional identity. At positive integer order \(m\), the kernel is \(x^{m-1}H/(m-1)!\), and the group law identifies this with repeated causal integration.

For example, let \(c>0\) and \(f=\boldsymbol1_{(0,c)}=H-H(\,\cdot-c)\). Translation of a factor in convolution translates the result, by Theorem 1.1 of the convolution lesson. Therefore, for every complex order,

\[
J_af=R_{a+1}(x)-R_{a+1}(x-c).
\tag{3.7}
\]

At \(a=-1\), this is \(\delta_0-\delta_c\). Differentiation preserves the pulse's endpoints as point masses. On all distributions on the line a nonzero constant has derivative zero, so the causal hypothesis is essential to invertibility.

## Reflection controls the Gamma normalization

We first fix the scalar and contour details. The [scalar foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§13.1–13.9, prove the fundamental theorem, chain rule, exponential series, real logarithm and trigonometric parameterization of the circle.

For a continuous complex-valued integrand on an interval, a \(C^1\) increasing substitution is justified on compact subintervals by taking an antiderivative and applying the chain rule and fundamental theorem. If the original and transformed absolute integrals converge at the endpoints, their truncated identities pass to the full improper integrals. This proves the substitutions \(t=s/(1+s)\), \(s=x\sin^2\theta\) and \(u=s^2\) used below; their derivatives are positive on the open intervals in question. We check endpoint convergence at each use.

On \(\mathbb C\setminus[0,\infty)\), choose \(\theta=\operatorname{Arg}z\in(0,2\pi)\). The quadrant inverses in §13.9 give its unique continuous value, with the agreeing limiting value \(\pi\) across the negative axis. Put \(\operatorname{Log}z=\log|z|+i\theta\). It is holomorphic, as can be checked locally without a contour theorem. At a fixed \(z_0\) in the slit plane, the series
\[
\ell(z)=\log|z_0|+i\operatorname{Arg}z_0+
 \sum_{n\ge1}\frac{(-1)^{n+1}}{n}
                 \left(\frac{z-z_0}{z_0}\right)^n
\tag{4.0}
\]
converges for \(|z-z_0|<|z_0|\), has derivative \(1/z\), and satisfies \(e^{\ell(z)}=z\) by G0. Shrink the disk so that \(\operatorname{Im}\ell\in(0,2\pi)\). The modulus and unique circle parameter then identify \(\ell=\operatorname{Log}\). Consequently \(z^{a-1}=\exp((a-1)\operatorname{Log}z)\) is holomorphic there.

**Theorem 4.1 (Euler's reflection formula).** For \(a\notin\mathbb Z\),

\[
\Gamma(a)\Gamma(1-a)=\frac{\pi}{\sin(\pi a)}.
\tag{4.1}
\]

Equivalently, on the entire plane,

\[
G(a)G(1-a)=\frac{\sin(\pi a)}{\pi}.
\tag{4.2}
\]

**Proof.** Begin with \(0<\operatorname{Re}a<1\). The substitution \(t=s/(1+s)\) in the beta integral yields

\[
B(a,1-a)=\int_0^\infty\frac{s^{a-1}}{1+s}\,ds=:I(a).
\tag{4.3}
\]

Both absolute integrals converge: near zero the last integrand is bounded by \(s^{\operatorname{Re}a-1}\), and near infinity by \(s^{\operatorname{Re}a-2}\). The compact-interval substitution just proved therefore applies.

Take \(0<\epsilon<1<R\) and \(0<\eta<\pi/2\). Let \(\Omega\) be the annular sector
\(\epsilon<|z|<R,\ \eta<\operatorname{Arg}z<2\pi-\eta\).
Its positively oriented boundary runs outward on angle \(\eta\), counterclockwise along the outer arc, inward on angle \(2\pi-\eta\), and clockwise along the inner arc. The function
\(f(z)=z^{a-1}/(1+z)\) is holomorphic near its closure except at \(-1\).

Here is the entire single-pole argument needed for this contour. Remove a closed disk of radius \(d\) about \(-1\), small enough to lie in \(\Omega\). The complex Green formula for finitely many regular arcs and corners, proved in Boundary flux and weak identities, Corollaries 2.3–2.4, applies to \(f\) on the remaining region. If compact support is needed, multiply by a smooth cutoff equal to one on a neighborhood of that region's closure; \(\bar\partial f=0\) there. Green's formula gives zero total boundary integral. The hole is clockwise, so the outer boundary integral equals the counterclockwise circle integral around \(-1\).

Write \(h(z)=z^{a-1}\), which is continuous near \(-1\). On \(z=-1+de^{it}\),
\[
\int_{|z+1|=d}^{\mathrm{ccw}}\frac{h(z)}{z+1}\,dz
 =i\int_0^{2\pi}h(-1+de^{it})\,dt
 \longrightarrow 2\pi i h(-1)=-2\pi i e^{i\pi a}.
\tag{4.3a}
\]
The error is at most \(2\pi\sup_{|z+1|=d}|h(z)-h(-1)|\), tending to zero. The outer boundary is independent of \(d\). This proves its integral equals the displayed limit, without assuming a general residue theorem.

Now send \(\eta\downarrow0\) with \(\epsilon,R\) fixed. Parameterizations on the compact edges give uniform convergence, including the angular factor in the complex power. The outward upper edge has limit \(\int_\epsilon^R s^{a-1}/(1+s)\,ds\); the inward lower edge has the factor \(-e^{2\pi i(a-1)}=-e^{2\pi ia}\). Their sum is

\[
(1-e^{2\pi ia})\int_\epsilon^R\frac{s^{a-1}}{1+s}\,ds.
\tag{4.4}
\]

Put \(\sigma=\operatorname{Re}a\). For \(z=re^{i\theta}\) on these contours,
\(|z^{a-1}|=r^{\sigma-1}e^{-\theta\operatorname{Im}a}
\le r^{\sigma-1}e^{2\pi|\operatorname{Im}a|}\).
The outer arc integral has modulus at most
\(2\pi e^{2\pi|\operatorname{Im}a|}R^\sigma/(R-1)\);
the inner one has modulus at most
\(2\pi e^{2\pi|\operatorname{Im}a|}\epsilon^\sigma/(1-\epsilon)\).
They tend to zero as \(R\to\infty\) and \(\epsilon\downarrow0\), respectively. We obtain

\[
(1-e^{2\pi ia})I(a)=-2\pi i e^{i\pi a}.
\tag{4.5}
\]

Theorem 2.1 gives \(I(a)=\Gamma(a)\Gamma(1-a)\), which is finite and nonzero on the strip. Multiply (4.5) by \(G(a)G(1-a)\) and divide by the nonzero exponential and constant. Since
\(1-e^{2\pi ia}=-2ie^{i\pi a}\sin(\pi a)\), this proves (4.2) on the strip without assuming beforehand where the complex sine vanishes.

Both sides of (4.2) are entire. The identity principle, proved in [Gluing holomorphic sides](gluing-holomorphic-sides.md), Lemma 3.2, extends equality to \(\mathbb C\). At a noninteger neither reciprocal Gamma factor is zero, by (1.1). Thus \(\sin(\pi a)\ne0\) there, and reciprocation proves (4.1). At the integers (4.2) is still an ordinary entire identity; (4.1) expresses equality of meromorphic functions. \(\square\)

The Gamma integral is positive at every positive real argument. At \(a=1/2\), reflection therefore gives the positive value \(\Gamma(1/2)=\sqrt\pi\). For real \(t\), conjugation of the absolutely convergent Gamma integral and the exponential formula for sine give

\[
|\Gamma(1/2+it)|^2=\frac{\pi}{\cosh(\pi t)}.
\tag{4.6}
\]

Indeed \(1-(1/2+it)=1/2-it\), and
\(\sin(\pi/2+i\pi t)=(e^{-\pi t}+e^{\pi t})/2\).

## A logarithmic distribution generates all orders

The normalized finite part in the earlier lesson, Theorem 2.1 with \(k=1\), is

\[
F_1(\phi)=-\int_0^\infty\log x\,\phi'(x)\,dx.
\tag{5.1}
\]

This integral is finite and bounded by \(p_1(\phi)\) on each fixed support; it is zero on the negative half-line and equals \(x^{-1}\) on the positive half-line by integration by parts away from zero.

**Theorem 5.1 (the order generator).** Define \(K=\left.\partial_aR_a\right|_{a=0}\) in test pairings. Then

\[
K=F_1+\gamma\delta_0,\qquad
K(\phi)=-\int_0^\infty(\log x+\gamma)\phi'(x)\,dx,
\tag{5.2}
\]

and

\[
\partial_aR_a=K*R_a,\qquad
\partial_aJ_a u=K*J_a u\quad(u\in\mathcal D'_+).
\tag{5.3}
\]

For \(\tau>0\), let \(D_\tau v=v(\tau\,\cdot)\) mean
\(D_\tau v(\phi)=\tau^{-1}v(\phi(\,\cdot/\tau))\), and let \(E=x\partial_x\). Then

\[
D_\tau K=\tau^{-1}\bigl(K+(\log\tau)\delta_0\bigr),
\qquad (E+1)K=\delta_0.
\tag{5.4}
\]

**Proof.** For \(|z|<1/2\), the logarithmic power series gives
\(\left|\log(1+z/j)-z/j\right|\le2|z|^2/j^2\).
Summing this absolutely convergent bound and using the exponential series in (1.1) gives

\[
G(z)/z=1+\gamma z+O(z^2).
\tag{5.5}
\]

By recurrence this is \(G(1+z)\), including its removable value at zero. For \(a\) near zero,

\[
R_{a+1}=H(x)x^aG(1+a),\qquad R_a=\partial_xR_{a+1}.
\tag{5.6}
\]

The estimates (1.6), with any fixed \(|a|\le\eta<1\), allow parameter differentiation of the locally integrable density. Its derivative at zero is \(H(\log x+\gamma)\). Taking its spatial derivative yields (5.2), since \(\int_0^\infty\phi'=-\phi(0)\). The \(p_1\) bound proves this derivative is itself a distribution.

In \(R_{a+h}=R_h*R_a\), hold \(a\) fixed and differentiate with respect to \(h\) at zero. The compact-test currying in Theorem 3.1 transfers the difference quotient through convolution with a fixed causal factor. This proves the first identity in (5.3). The same currying with \(u\), followed by proper-support associativity, gives the second.

For \(\operatorname{Re}a>0\), an affine substitution in the density proves \(D_\tau R_a=\tau^{a-1}R_a\). Both sides are entire in each test pairing, so the identity principle extends this to every \(a\). Differentiate at \(a=0\) and use \(R_0=\delta_0\) to obtain the first identity in (5.4).

To differentiate it at \(\tau=1\), observe that for \(\tau\) in a compact interval about one the rescaled tests have common compact support; the chain rule gives their derivative and its convergence in every test seminorm. Hence any distribution satisfies

\[
\left.\frac d{d\tau}D_\tau v(\phi)\right|_{\tau=1}
=-v(\phi+x\phi')=(x\partial_xv)(\phi).
\tag{5.7}
\]

The derivative of the right side of (5.4) is \(-K+\delta_0\), giving \((E+1)K=\delta_0\). \(\square\)

## Exercises

**Exercise 1 (basic: complex beta moments).** For \(\operatorname{Re}a,\operatorname{Re}b>0\) and nonnegative integers \(p,q\), evaluate

\[
M_{p,q}=\frac1{B(a,b)}
 \int_0^1t^{a+p-1}(1-t)^{b+q-1}\,dt.
\tag{6.1}
\]

Find the normalized mean of \(t\) and its centered second moment. Explain the role of positivity.

**Solution 1.** Define \((z)_m=\prod_{j=0}^{m-1}(z+j)\), with empty product one. The beta identity and repeated Gamma recurrence give

\[
M_{p,q}=\frac{(a)_p(b)_q}{(a+b)_{p+q}}.
\tag{6.2}
\]

Theorem 2.1 proves \(B(a,b)\ne0\), and each denominator factor in (6.2) has positive real part. Put \(\mu=M_{1,0}=a/(a+b)\). Since \(M_{0,0}=1\), expansion of \((t-\mu)^2\) gives the centered moment \(M_{2,0}-\mu^2\), namely

\[
\frac{a(a+1)}{(a+b)(a+b+1)}-\frac{a^2}{(a+b)^2}
=\frac{ab}{(a+b)^2(a+b+1)}.
\tag{6.3}
\]

These are identities of complex integrals, not statements about absolute-value squared. For positive real \(a,b\) the normalized weight is also a probability density, and this centered moment is its variance.

**Exercise 2 (basic: a delayed pulse).** Let \(c>0\) and \(f=\boldsymbol1_{(c,2c)}\). Compute \(J_2f\) and its first two derivatives, including their tails, and prove uniqueness.

**Solution 2.** Use \(f=H(\,\cdot-c)-H(\,\cdot-2c)\), translation and the group law:

\[
J_2f=\tfrac12(x-c)_+^2-\tfrac12(x-2c)_+^2.
\tag{6.4}
\]

Integration by parts at the zero boundary value of \(x_+^m\), \(m\ge1\), proves \(\partial(x_+^m/m!)=x_+^{m-1}/(m-1)!\), with \(x_+^0=H\). Thus the derivatives are \((x-c)_+-(x-2c)_+\) and \(f\). For \(x>2c\) the first derivative is \(c\), and the primitive is \(cx-\tfrac32c^2\). All vanish before \(c\). Theorem 3.1 proves that this causal second primitive is unique.

**Exercise 3 (intermediate: a half-order and its inverse).** Compute \(R_{1/2}*R_{1/2}\) directly, deduce \(J_{-1/2}J_{1/2}u=u\) for all causal \(u\), and give the test formula for \(R_{-1/2}\).

**Solution 3.** Since \(\Gamma(1/2)=\sqrt\pi\), the positive-side density is

\[
\frac1\pi\int_0^x\frac{ds}{\sqrt{s(x-s)}}=1,\qquad x>0.
\tag{6.5}
\]

The substitution \(s=x\sin^2\theta\) has positive derivative on \(0<\theta<\pi/2\), and changes the integrand to \(2\,d\theta\). The two endpoint singularities of the original integral have exponent \(-1/2\), hence are integrable; the truncated substitution therefore extends to the endpoints. Theorem 2.2's absolute-integral estimate proves equality across zero, so the convolution is \(H\). Derivative transfer gives

\[
R_{-1/2}*R_{1/2}=(\partial_xR_{1/2})*R_{1/2}
=\partial_xH=\delta_0.
\tag{6.6}
\]

Associativity with \(u\) proves the inverse assertion, and

\[
R_{-1/2}(\phi)=-\frac1{\sqrt\pi}
                    \int_0^\infty x^{-1/2}\phi'(x)\,dx.
\tag{6.7}
\]

This pairing includes the extension at zero; a bare \(x^{-3/2}\) density would not be locally integrable there.

**Exercise 4 (intermediate: reflection on a vertical line).** Evaluate \(|\Gamma(1+it)|^2\) for real \(t\), including zero, and compare its asymptotics with (4.6).

**Solution 4.** If \(t\ne0\), reflection and the exponential definition of sine give

\[
\Gamma(it)\Gamma(1-it)=\frac{\pi}{i\sinh(\pi t)}.
\tag{6.8}
\]

Multiply by \(it\), use recurrence, and conjugate the Gamma integral at \(1+it\):

\[
|\Gamma(1+it)|^2=\frac{\pi t}{\sinh(\pi t)}.
\tag{6.9}
\]

The exponential series gives \(\sinh y/y\to1\) at zero, so the removable value is \(1=|\Gamma(1)|^2\). The quotient is positive and even. Since
\(\sinh(\pi|t|)=\tfrac12e^{\pi|t|}(1-e^{-2\pi|t|})\), its asymptotic value is \(2\pi|t|e^{-\pi|t|}\). Equation (4.6) is asymptotic to \(2\pi e^{-\pi|t|}\), from the corresponding plus sign for \(\cosh\).

**Exercise 5 (intermediate: residues at both kinds of integer).** Compute the residue of \(\Gamma(a)\Gamma(1-a)\) at every integer \(m\), treating the two kinds of pole separately.

**Solution 5.** At \(m=-k\le0\), the first Gamma factor has residue \((-1)^k/k!\), while the second has value \(\Gamma(1+k)=k!\). The residue is \((-1)^k=(-1)^m\). At \(m=k+1\ge1\), write \(1-a=-k-(a-m)\). The minus sign in the local parameter makes the second factor's residue \(-(-1)^k/k!\); the first has value \(k!\). The result is again \((-1)^m\). The exponential addition law and series give
\(\sin(\pi a)=(-1)^m\pi(a-m)+O((a-m)^3)\), so \(\pi/\sin(\pi a)\) has the same residue.

**Exercise 6 (advanced: singular inverses can simplify).** Prove that \(R_i\) and \(R_{-i}\) have exact distribution order one near zero, while their convolution has order zero.

**Solution 6.** In (1.5), \(N=1\) suffices: the densities \(R_{1\pm i}\) have constant modulus on the positive half-line. Thus each has an order-one bound on every compact support. On \(x>0\), \(R_{\pm i}\) equals \(G(\pm i)x^{\pm i-1}\); the nonzero coefficient follows from the zeros of \(G\).

Lemma 4.1 of [Euler equations and the order of singularities](euler-equations-and-singularity-order.md) proves that a distribution with a nonzero homogeneous punctured restriction of degree \(d\) in dimension \(n\) can have local order \(k\) only if \(k+\operatorname{Re}d+n>0\). Here this is

\[
k+\operatorname{Re}(\pm i-1)+1>0.
\tag{6.10}
\]

For \(k=0\) it fails at equality. The lemma includes this strict endpoint: geometric disjoint shrinking annuli and complex phases produce tests with bounded \(C^k\) norm but pairings growing linearly with the number of annuli. These tests fit in any prescribed neighborhood of zero. Thus the exact order is one. Theorem 2.2 gives \(R_i*R_{-i}=\delta_0\), whose exact order is zero.

**Exercise 7 (advanced: Legendre's duplication formula).** Prove from the beta integral that

\[
\Gamma(a)\Gamma(a+1/2)=2^{1-2a}\sqrt\pi\,\Gamma(2a),
\tag{6.11}
\]

and specify its continuation at poles.

**Solution 7.** Initially \(\operatorname{Re}a>0\). Substitute \(t=(1+s)/2\) in \(B(a,a)\), use symmetry in \(s\), and put \(u=s^2\) on the positive half:

\[
\begin{aligned}
B(a,a)
&=2^{1-2a}\int_{-1}^1(1-s^2)^{a-1}\,ds\\
&=2^{1-2a}\int_0^1u^{-1/2}(1-u)^{a-1}\,du
=2^{1-2a}B(1/2,a).
\end{aligned}
\tag{6.12}
\]

The square substitution follows from the compact-interval rule above. Its transformed exponents are \(-1/2\) at zero and \(\operatorname{Re}a-1>-1\) at one, so passage to endpoints is justified. All bases of powers are positive, and the real logarithm law proves the displayed powers of two without a branch choice. The beta identity and \(\Gamma(1/2)=\sqrt\pi\) give
\(\Gamma(a)^2/\Gamma(2a)=2^{1-2a}\sqrt\pi\,\Gamma(a)/\Gamma(a+1/2)\).
Cancel the nonzero Gamma factors to obtain (6.11).

Its reciprocal form is the identity between entire functions

\[
G(a)G(a+1/2)=\frac{2^{2a-1}}{\sqrt\pi}\,G(2a),
\qquad 2^{2a-1}=\exp((2a-1)\log2).
\tag{6.13}
\]

The identity principle extends it to every \(a\). Where the Gamma factors are finite, invert the equality. At poles, (6.11) means equality of meromorphic functions, hence of their local Laurent expansions, rather than substitution of infinite values.

**Exercise 8 (advanced: the generator cannot be made homogeneous).** Show that \(L=K+c\delta_0\) still has Euler defect \((E+1)L=\delta_0\). Compute \(K*H\), and decide whether any extension of \(x^{-1}\) from \(x>0\), zero for \(x<0\), can be homogeneous of degree \(-1\).

**Solution 8.** The product rule in test pairings gives \(x\delta_0'=-\delta_0\), so \((E+1)\delta_0=0\); (5.4) proves the assertion about \(L\). Differentiating \(R_{a+1}=R_a*H\) by the fixed-test argument in Theorem 3.1 and using (5.6) gives

\[
K*H=\left.\partial_aR_{a+1}\right|_{a=0}
=H(\log x+\gamma).
\tag{6.14}
\]

Any extension of the punctured density differs from \(F_1\) by a distribution supported at zero. [Finite parts of singular powers](finite-parts-of-singular-powers.md), Lemma J, proves that such a distribution is a finite sum of point jets and proves their linear independence. In test pairings,
\(x\delta_0^{(j+1)}=-(j+1)\delta_0^{(j)}\), because
\((x\phi)^{(j+1)}(0)=(j+1)\phi^{(j)}(0)\). Hence

\[
(E+1)\delta_0^{(j)}=-j\delta_0^{(j)}.
\tag{6.15}
\]

From \(F_1=K-\gamma\delta_0\) we get \((E+1)F_1=\delta_0\). Adding any finite sum \(\sum_j b_j\delta_0^{(j)}\) leaves its \(\delta_0\) coefficient equal to one: the term \(j=0\) contributes zero, and \(j\ge1\) contributes only higher derivatives. Independence of the jets prevents cancellation. Homogeneity of degree \(-1\) would, on differentiating its dilation law by (5.7), imply \((E+1)v=0\). No such extension exists.

## Programme proof locations and freely accessible sources

- [Gamma foundations](../prerequisites/U011-free-foundations/gamma-foundations-U016.md), G0–G2 and W4a–W4e: logarithmic powers, logarithmic integral bounds, dominated holomorphic differentiation, Euler integral and reciprocal product with all zeros and residues. This selected programme proof retains CC0 1.0 and its accompanying notices.
- [Scalar foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§13.1–13.9: chain rule and fundamental theorem, exponential series, real logarithms and full circle parameterization. [Integration foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.1: convergence, Tonelli, absolute Fubini and affine substitutions.
- Boundary flux and weak identities, Corollaries 2.3–2.4: complex Green formula including arc endpoints and corners. [Cauchy kernels and boundary limits](cauchy-kernels-and-boundary-limits.md), Corollary 2.2, proves the local holomorphic power series; [Gluing holomorphic sides](gluing-holomorphic-sides.md), Lemma 3.2, proves the identity principle.
- [Finite parts of singular powers](finite-parts-of-singular-powers.md), N1, Theorem 2.1 and Lemma J: normalized entire family, exact finite-part normalization and classification of point-supported distributions.
- [Convolution as addition of supports](convolution-as-addition-of-supports.md), B0–B3, Theorems 1.1 and 3.1–3.2: compact localization, smooth parameter tests, tensors, proper-support convolution, derivatives, associativity and fixed-support continuity.
- [Euler equations and the order of singularities](euler-equations-and-singularity-order.md), Lemma 4.1: strict local order bound, including the endpoint disjoint-annulus argument used in Solution 6.
- Sergey Lototsky, *Basics of Gamma and Beta functions*, updated 4 August 2023, pp. 1–2, [freely accessible USC notes](https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2023/08/GammaBetaFunctions.pdf). Beta and duplication constructions compared; this lesson supplies its own iterated-integral proof and all complex-parameter justifications.
- Imperial College London, *M2PM3 Examination Solutions 2011*, Question 3, p. 3, [freely accessible course solutions](https://www.ma.imperial.ac.uk/~bin06/M2PM3-Complex-Analysis/m2pm3examsoln%2811%29.pdf). Reflection contour compared; the required single-pole integral is proved above from the supplied Green formula.
