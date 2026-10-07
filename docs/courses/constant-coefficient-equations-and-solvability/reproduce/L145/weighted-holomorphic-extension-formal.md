# Weighted holomorphic extensions and their growth

*Original proof exposition by GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0 1.0.*

We extend an entire function from a complex linear subspace, with the precise codimension-dependent square norm estimate. The proof constructs the extension from a normal cutoff, solves its closed Cauchy–Riemann error, and proves that the corrected entire function has the required pointwise restriction. A one-sided normal weight comparison makes iteration retain the original constant. We then prove the exact polynomial growth transfer.

All lengths and induced volumes use the standard Hermitian metric on \(\mathbb C^n\). Write \(R(z)=1+|z|^2\), \(dV\) for ordinary real \(2n\)-dimensional volume, and \(dS\) for the induced volume on a complex subspace. On the zero-dimensional subspace, its single point has measure 1. The operators are \(\partial_j=(\partial_{x_j}-i\partial_{y_j})/2\) and \(\bar\partial_j=(\partial_{x_j}+i\partial_{y_j})/2\).

The actual existence input is [L144, general PSH weighted existence, W5 and W25–W28](../../AN02-L144.html#general-psh-weighted-existence): for a finite global PSH weight \(\theta\) and distributionally closed coefficient data \(f\) with finite \(\int|f|^2e^{-\theta}\), there is a solution \(\bar\partial v=f\) with

\[
\int |v|^2 e^{-\theta}R^{-2}dV
\le\tfrac12\int|f|^2e^{-\theta}dV.
\tag{EX1}
\]

We also use [L131 NP5](../../AN02-L131.html#NP5), whose full local harmonic smoothing proof gives a smooth harmonic representative of every distribution with zero Laplacian. Its mean identity is NP5.1. Ordinary local integration and distributional products have their written proofs in the linked Lebesgue/distribution foundations. The normal cutoff derivatives, holomorphic regularity step, restriction argument, iteration and radial integral are proved below.

<a id="weighted-extension-theorem"></a>
<a id="EX-theorem"></a>

## E1. The exact extension statement

**Theorem E1.** Let \(n\ge1\), and let \(\phi:\mathbb C^n\to\mathbb R\) be PSH. Suppose there is \(C>0\) such that

\[
|\phi(z)-\phi(\widetilde z)|<C
\quad\text{whenever }|z-\widetilde z|<1.
\tag{EX2}
\]

Let \(W\) be a complex linear subspace of codimension \(k\), \(0\le k\le n\). If \(u\) is entire on \(W\) and

\[
J_0=\int_W |u|^2e^{-\phi}dS<\infty,
\tag{EX3}
\]

there is an entire \(U\) on \(\mathbb C^n\) satisfying

\[
U|_W=u,\qquad
\int_{\mathbb C^n}|U|^2e^{-\phi}R^{-3k}dV
\le(6\pi e^C)^kJ_0.
\tag{EX4}
\]

The unit-oscillation assumption is global; a smooth strictly PSH weight alone need not satisfy it. The case \(k=0\) is \(U=u\), with equality of the norms. The entire restriction is pointwise, not merely an almost-everywhere trace on a subspace of zero ambient volume.

<a id="extension-growth-corollary"></a>

**Corollary E2.** With the same \(\phi,W,C\), suppose \(u\) is entire on \(W\) and, for a finite \(C_1\ge0\),

\[
|u(z)|\le C_1e^{\phi(z)}\quad(z\in W).
\tag{EX5}
\]

Then an entire extension has, for a finite constant \(C_2\),

\[
|U(z)|\le C_2(1+|z|)^{n+2k+1}e^{\phi(z)}
\quad(z\in\mathbb C^n).
\tag{EX6}
\]

No finite value of the original square norm (EX3) is assumed in this corollary. We create the needed norm by changing the weight.

<a id="distributional-holomorphic-regularity"></a>

## E3. A distributional Cauchy–Riemann solution has an entire representative

Let \(H\in L^2_{\mathrm{loc}}(\mathbb C^d)\), \(d\ge1\), satisfy \(\bar\partial_jH=0\) as distributions for all \(j\). Since

\[
\Delta=4\sum_{j=1}^d\partial_j\bar\partial_j,
\tag{EX7}
\]

its distributional Laplacian is zero. Apply NP5 to its real and imaginary parts. It has a smooth harmonic representative \(h\), with \(\bar\partial_jh=0\) as ordinary smooth functions.

Here is the required joint analyticity step. In one coordinate disk, fixing the other coordinates, the smooth restricted function \(g\) has \(\bar\partial g=0\). On the annulus between a circle surrounding a point \(a\) and a small circle centered at \(a\), the function \(g(w)/(w-a)\) has zero antiholomorphic derivative. Real Green–Stokes integration equates its outer and inner complex contour integrals. Parametrizing the small inner circle and using continuity makes its integral tend to \(2\pi i g(a)\). Thus the Cauchy formula holds in that coordinate.

Apply this formula successively in each coordinate of any polydisc whose closed torus lies in a larger open polydisc. Fubini is valid on the compact integration torus, and gives the product Cauchy formula. Expand each kernel about the polydisc center using its geometric series. On a smaller polydisc, the series are absolutely and uniformly convergent. The product geometric bound is finite, so termwise integration gives a joint power series. Equivalently, if its outer coordinate radii are \(r_j\) and \(|h|\le M\) on the torus, its coefficients satisfy

\[
|a_\alpha|\le M\prod_{j=1}^d r_j^{-\alpha_j},\qquad
\sum_{\alpha\in\mathbb N^d}|a_\alpha|\prod_j s_j^{\alpha_j}
\le M\prod_{j=1}^d(1-s_j/r_j)^{-1}<\infty
\quad(0\le s_j<r_j).
\tag{EX8}
\]

These local polydiscs cover \(\mathbb C^d\). The representative is consequently entire. Two continuous representatives of one distribution coincide: otherwise a real or imaginary component has one strict sign on a small ball and its integral against a positive compact test is nonzero. This supplies the pointwise entire representative used in the construction.

<a id="one-sided-hyperplane-extension"></a>

## E4. One hyperplane under a one-sided normal comparison

We prove a slightly more precise hyperplane lemma. Let \(d\ge1\), write \(z=(\zeta,w)\in\mathbb C^{d-1}\times\mathbb C\), and let \(\theta\) be a finite PSH weight such that

\[
\theta(\zeta,w)\ge\theta(\zeta,0)-C
\quad(|w|<1).
\tag{EX9}
\]

For entire \(u(\zeta)\) with \(J=\int|u(\zeta)|^2e^{-\theta(\zeta,0)}dV(\zeta)<\infty\), Fubini and the area of the normal unit disk give

\[
\int_{|w|<1}|u(\zeta)|^2e^{-\theta(\zeta,w)}dV(\zeta)dA(w)
\le\pi e^C J.
\tag{EX10}
\]

Choose the exact continuous Lipschitz normal cutoff

\[
\eta(w)=
\begin{cases}
1,&|w|\le\tfrac12,\\
2(1-|w|),&\tfrac12<|w|<1,\\
0,&|w|\ge1.
\end{cases}
\tag{EX11}
\]

Its weak first derivatives equal its classical derivatives off the two joining circles. Indeed, integration by parts on the three pieces cancels the boundary terms because the values agree at each joining circle. Since \(\bar\partial_w|w|=w/(2|w|)\) away from zero,

\[
\bar\partial_w\eta=-\frac{w}{|w|}\,
\mathbf1_{\{1/2<|w|<1\}},\qquad
|\bar\partial_w\eta|\le1.
\tag{EX12}
\]

Define the coefficient vector \(f\) by its zero first \(d-1\) coefficients and

\[
f_d(\zeta,w)=\frac{u(\zeta)}{w}\bar\partial_w\eta(w)
=-\frac{u(\zeta)}{|w|}\mathbf1_{\{1/2<|w|<1\}}.
\tag{EX13}
\]

Set it to zero off that annulus, in particular near \(w=0\). This is a locally square-integrable function, with \(|f|\le2|u|\) on the normal unit tube. It is distributionally closed: the only potentially nonzero cross derivatives are the antiholomorphic \(\zeta\) derivatives of its last coefficient, and they vanish because \(u\) is entire. For \(d=1\), closedness is automatic. Therefore

\[
\int|f|^2e^{-\theta}dV\le4\pi e^C J.
\tag{EX14}
\]

Apply (EX1) in complex dimension \(d\) to obtain \(v\) with

\[
\bar\partial v=f,\qquad
\int|v|^2e^{-\theta}R^{-2}dV\le2\pi e^C J.
\tag{EX15}
\]

This \(v\) is in ordinary local \(L^2\). The finite PSH function \(\theta\) is locally bounded above, and the left weight has a positive lower bound on any compact set. Let

\[
H(\zeta,w)=\eta(w)u(\zeta)-wv(\zeta,w).
\tag{EX16}
\]

It is locally square integrable. Distributional multiplication by the holomorphic coordinate \(w\), the weak derivative (EX12), and (EX13) give \(\bar\partial_jH=0\) in every coordinate. E3 supplies its unique entire representative \(U\).

<a id="pointwise-restriction-recovery"></a>

The restriction requires proof, because no value of the merely locally square-integrable \(v\) at \(w=0\) was chosen. On \(|w|<1/2\) the entire function \(G=U-u\) satisfies \(G=-wv\) almost everywhere. If \(G(\zeta_0,0)\ne0\), continuity would supply a product neighborhood and a positive \(c\) on which \(|G|\ge c\). Off the axis there, \(|v|\ge c/|w|\) almost everywhere. But

\[
\int_{0<|w|<\varepsilon}\frac{dA(w)}{|w|^2}
=2\pi\int_0^\varepsilon\frac{dr}{r}=\infty.
\tag{EX17}
\]

Fubini, using the positive volume of the \(\zeta\) neighborhood, contradicts local \(L^2\) of \(v\). When \(d=1\), the \(\zeta\) factor has dimension zero and measure 1, giving exactly the same contradiction. Thus

\[
U(\zeta,0)=u(\zeta)\quad\text{for every }\zeta.
\tag{EX18}
\]

<a id="hyperplane-norm-constant"></a>

## E5. The exact hyperplane estimate

For complex numbers \(a,b\), \(|a-b|^2\le2|a|^2+2|b|^2\). Use this in (EX16). Since \(0\le\eta\le1\), \(\eta=0\) outside the normal unit disk, \(R^{-3}\le1\), and \(|w|^2\le R\), we obtain

\[
\begin{aligned}
\int |U|^2e^{-\theta}R^{-3}dV
&\le2\int_{|w|<1}|u|^2e^{-\theta}dV
 +2\int|v|^2e^{-\theta}R^{-2}dV\\
&\le2\pi e^C J+4\pi e^C J
=6\pi e^C J.
\end{aligned}
\tag{EX19}
\]

The factor 2 in each square term, the factor 1/2 in (EX1), and the normal disk area \(\pi\) account for the displayed constant. Multiplying the correction by \(w\) costs one additional power of \(R^{-1}\); together with the two powers in (EX1), this gives exactly \(R^{-3}\). This proves the hyperplane lemma using only (EX9), not the stronger two-sided unit-oscillation condition for the modified weight.

<a id="codimension-iteration"></a>

## E6. Iterate while retaining the original constant

Choose orthonormal complex coordinates adapted to \(W\). This can be done by taking a basis of \(W\), subtracting its orthogonal projections successively and normalizing, and then repeating with vectors outside its span until obtaining a basis of \(\mathbb C^n\). The coordinate map is unitary. It preserves lengths and ordinary volumes: its complex determinant has modulus1, so its real Jacobian has absolute value1. A complex line maps to a complex line, so PSH is preserved. We may consequently take

\[
W=\mathbb C^{m}\times\{0\},\qquad m=n-k,
\quad E_j=\mathbb C^{m+j}\times\{0\}\quad(0\le j\le k).
\tag{EX20}
\]

Start with \(u_0=u\). At the \(j\)-th step use the finite PSH weight on \(E_j\)

\[
\theta_j(z)=\phi(z)+3(j-1)\log R(z).
\tag{EX21}
\]

The logarithm is PSH by the exact Levi computation in L144 W25. For the orthogonal splitting \(z=(\zeta,w)\in E_j\) relative to \(E_{j-1}\), \(R(\zeta,w)=R(\zeta,0)+|w|^2\). Therefore, for \(|w|<1\),

\[
\begin{aligned}
\theta_j(\zeta,w)-\theta_j(\zeta,0)
&=\phi(\zeta,w)-\phi(\zeta,0)
 +3(j-1)\log\frac{R(\zeta,0)+|w|^2}{R(\zeta,0)}\\
&\ge-C.
\end{aligned}
\tag{EX22}
\]

The added term is nonnegative. This is the decisive one-sided comparison with the original \(C\); taking an enlarged two-sided oscillation constant for each new weight would produce a different and unnecessarily worse estimate.

Apply the hyperplane lemma to \(u_{j-1}\) and \(\theta_j\). It yields entire \(u_j\) on \(E_j\), with pointwise restriction \(u_j|_{E_{j-1}}=u_{j-1}\), and

\[
J_j:=\int_{E_j}|u_j|^2e^{-\phi}R^{-3j}dS
\le6\pi e^C
\int_{E_{j-1}}|u_{j-1}|^2e^{-\phi}R^{-3(j-1)}dS
=6\pi e^C J_{j-1}.
\tag{EX23}
\]

Each input norm is finite by the preceding step. Repeating \(k\) times gives \(J_k\le(6\pi e^C)^kJ_0\). The pointwise restrictions compose, so \(u_k|_W=u\). Taking \(U=u_k\) proves Theorem E1, including subspaces with \(m=0\).

<a id="radial-integral-and-logarithmic-oscillation"></a>

## E7. Two elementary estimates for growth transfer

First, the real gradient of \(L(z)=\log(1+|z|^2)\) has length

\[
|\nabla L(z)|=\frac{2|z|}{1+|z|^2}\le1.
\tag{EX24}
\]

Integrating the gradient along the segment between two points shows that \(L\) is globally 1-Lipschitz.

Second, for an integer \(m\ge0\),

\[
\int_{\mathbb C^m}(1+|\zeta|^2)^{-(m+1)}dV(\zeta)
=\frac{\pi^m}{m!}.
\tag{EX25}
\]

For a direct proof, repeated integration by parts gives
\(\int_0^\infty t^m e^{-a t}dt=m!a^{-(m+1)}\) for \(a>0\). Thus

\[
(1+|\zeta|^2)^{-(m+1)}
=\frac1{m!}\int_0^\infty t^m e^{-t}e^{-t|\zeta|^2}dt.
\tag{EX26}
\]

Tonelli applies because the integrand is nonnegative. Polar integration in one complex coordinate gives \(\int_\mathbb C e^{-t|w|^2}dA=\pi/t\); multiply these \(m\) integrals by Fubini. Integrating (EX26) becomes \(\pi^m/m!\) times \(\int_0^\infty e^{-t}dt=1\). For \(m=0\), all products are empty products1, and this is the stated point measure convention. This proves (EX25) without an unproved convergence assumption.

<a id="growth-transfer-proof"></a>

## E8. Prove the exact growth exponent

Let \(m=n-k\), \(\beta=m+1\), and replace the weight by

\[
\Theta(z)=2\phi(z)+\beta\log R(z),\qquad
C_*:=2C+\beta.
\tag{EX27}
\]

It is finite PSH. For two points at distance less than1, (EX2) and (EX24) give \(|\Theta(z)-\Theta(\widetilde z)|<C_*\), so it satisfies the extension hypothesis. By (EX5) and (EX25),

\[
\int_W|u|^2e^{-\Theta}dS
\le C_1^2\int_W R^{-(m+1)}dS
=C_1^2\frac{\pi^m}{m!}.
\tag{EX28}
\]

Theorem E1 applied to \(\Theta\) gives an entire extension with

\[
A:=\int_{\mathbb C^n}|U|^2e^{-2\phi}R^{-N}dV
\le(6\pi e^{C_*})^kC_1^2\frac{\pi^m}{m!}<\infty,
\qquad N=\beta+3k=n+2k+1.
\tag{EX29}
\]

An entire function is harmonic in real dimension \(2n\), by (EX7). Its unit-ball mean equals its center value; the divergence/mean identity in NP5.1 proves this for its real and imaginary parts. Put \(b_n=|B_{\mathbb R^{2n}}(0,1)|>0\). Weighted Cauchy–Schwarz in that ball yields

\[
\begin{aligned}
|U(z)|^2
&\le b_n^{-2}
 \left(\int_{B(z,1)}|U(w)|^2e^{-2\phi(w)}R(w)^{-N}dV(w)\right)
 \left(\int_{B(z,1)}e^{2\phi(w)}R(w)^N dV(w)\right)\\
&\le \frac{A}{b_n}\, e^{2\phi(z)+2C}\,
 2^N(1+|z|)^{2N}.
\end{aligned}
\tag{EX30}
\]

Indeed, on this open ball \(\phi(w)<\phi(z)+C\), and
\(R(w)\le1+(|z|+1)^2\le2(1+|z|)^2\). Taking square roots proves (EX6), for example with

\[
C_2=e^C 2^{N/2}\sqrt{A/b_n}.
\tag{EX31}
\]

If \(C_1=0\), take \(U=0\), so the same conclusion is immediate. This completes Corollary E2. The exponent \(n+2k+1\) is the exact stated growth-transfer exponent; no claim of optimality is needed or made.

<a id="normal-monotone-comparison"></a>

## E9. An exact comparison for normal-monotone weights

The universal constant in E1 is an upper bound, not a claim that every example attains it. Here is a useful exact comparison with a directly known extension. For integers \(p\ge0\), \(q>p\), and \(a>0\), the same Laplace and Gaussian calculation as in E7 gives

\[
\int_{\mathbb C^p}(a+|w|^2)^{-q}dV(w)
=\pi^p\frac{(q-p-1)!}{(q-1)!}\,a^{p-q}.
\tag{EX32}
\]

Indeed, write the integrand as \((q-1)!^{-1}\int_0^\infty t^{q-1}e^{-at}e^{-t|w|^2}dt\), use Tonelli, multiply the \(p\) Gaussian integrals, and evaluate the remaining \(\int_0^\infty t^{q-p-1}e^{-at}dt\) by repeated integration by parts. For \(p=0\) this reduces to \(a^{-q}\), as it should.

Suppose in orthogonal coordinates \(z=(\zeta,w)\in\mathbb C^{n-k}\times\mathbb C^k\) a particular finite weight satisfies \(\phi(\zeta,w)\ge\phi(\zeta,0)\) for every \(w\), and \(k\ge1\). The directly known entire extension \(U(\zeta,w)=u(\zeta)\) then satisfies

\[
\begin{aligned}
\int |U|^2e^{-\phi}R^{-3k}dV
&\le B_k\int_W |u|^2e^{-\phi}R^{-2k}dS
\le B_kJ_0,\\
B_k&=\pi^k\frac{(2k-1)!}{(3k-1)!}.
\end{aligned}
\tag{EX33}
\]

To see the first inequality, apply (EX32) to the normal integral with \(p=k\), \(q=3k\), and \(a=R(\zeta,0)\). Tonelli is applicable to the nonnegative weighted square integrand. The last inequality uses \(R\ge1\). These extra global normal-monotonicity assumptions belong to this comparison only; E1 proves the extension under the original unit-oscillation condition without them.

## Source credit and scope

Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, §15.1, Theorem 15.1.3 and Corollary 15.1.4, printed pp. 274–276 (1983 edition; second revised printing 1990; reprint 2005), provides these classical targets. The full proof exposition above is original. The earlier original weighted existence and harmonic smoothing arguments are actually linked and read. No protected source pages or media are part of this lesson. The associated learner material supplies worked examples, complete exercises and original reproducible illustrations. Analytic-functional Fourier representation, later extension results and the remaining course targets retain their separate proof obligations.
