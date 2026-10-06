# Modified waves and the direction of escape

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: Which spatial cone corresponds to the chosen time direction?** A packet of velocity \(v\) follows \(x\approx tv\). When \(t<0\), that ray points toward \(-v\), so decay imposed only near the positive-velocity cone can miss the packet entirely. The modifier must cancel the phase along the rays selected by its sign before its residual is integrated.

A long-range force changes the phase of a travelling wave even after its coefficient becomes small. A modifier follows that phase. The remaining error can then be integrated in time. We prove this for a real polynomial free operator, a rough short-range differential perturbation, and any self-adjoint realization of their sum. The direction in which a packet escapes determines which spatial cone must have short-range decay.

Read [Smooth long-range phases from Hamilton trajectories](smooth-long-range-phases-from-hamilton-trajectories.md) for the real phase and all its frequency derivatives. The arbitrary-self-adjoint measure and equality with the original second-moment domain are proved in [Self-adjoint spectral calculus with the original domain](../providers/analysis/self-adjoint-spectral-domains.md#self-adjoint-pvm-domain). Its [unitary-group proof and both directions of the generator-domain criterion](../providers/analysis/self-adjoint-spectral-domains.md#selfadjoint-groups-and-powers) will be used below. The maximal polynomial Fourier realization and its spectral projections are proved in [Resolvents, domains and spectral density, Section 1](resolvents-domains-and-spectral-density.md#u001-specified-domains). These statements include operators with no lower bound, on arbitrary Hilbert spaces. Section 2 below proves the uniform nonstationary integral estimate. The complete finite-derivative \(L^2\) estimate and its exact dilation convention are proved in [A finite-derivative bound for left quantization](../providers/analysis/finite-derivative-l2.md#finite-derivative-l2). Its [measure and Euclidean product proofs](../providers/analysis/finite-derivative-l2.md#measure-foundations) supply dominated convergence, Fatou and Tonelli. [Approximation and convolution, Theorems 2.1 and 3.1](../providers/analysis/euclidean-approximation-and-convolution.md#finite-p-density), supplies the smooth approximation used below. The required finite seminorms are estimated in Section 4. The [elementary real powers, logarithms and trigonometry](../providers/analysis/elementary-functions-and-cutoffs.md) supply the scalar formulas used in the examples.

The free texts of Oh [O] and Teschl [T] provide background on evolution and characteristics. The comparison argument below integrates the evolution error after inserting the stated phase modifier.

<a id="modified-wave-setting"></a>

## 1. A packet has a velocity and a time direction

Use the unitary Fourier transform and \(D_j=-i\partial_{x_j}\). Let \(P_0\) be a real nonconstant polynomial on \(\mathbb R^n\). Its maximal Fourier multiplication operator is

\[
\begin{gathered}
 H_0=P_0(D),\qquad
 \mathcal D(H_0)=\{u:P_0\widehat u\in L^2\},\\
 v(\xi)=\nabla P_0(\xi),\qquad
 \Omega=\{\xi:v(\xi)\ne0\}.
\end{gathered}
\tag{1}
\]

A free packet with frequencies near \(\xi^0\) travels near \(x=tv(\xi^0)\). Positive time samples the direction \(v(\xi^0)\); negative time samples its opposite. A cone here is open and invariant under positive dilations. It need not contain the negative of any of its vectors.

Write a finite-order differential perturbation as

\[
\begin{gathered}
 V(x,D)=\sum_{|\alpha|\le p}v_\alpha(x)D^\alpha\\
       =V_L(x,D)+V_S(x,D),\\
 \int_{\mathbb R^n}\sum_\alpha
       |v_\alpha(x)|^2X^{-2M}\,dx<\infty,\\
 X=(1+|x|^2)^{1/2}.
\end{gathered}
\tag{2}
\]

The coefficients in (2) are measurable and can be complex. The operator \(H_0+V\) is assumed symmetric on Schwartz space and to have a self-adjoint extension \(H\). The weighted condition makes \(V:\mathcal S\to L^2\) continuous: after increasing \(M\) to a nonnegative integer if necessary, \(\|v_\alpha D^\alpha u\|_2\le\|v_\alpha X^{-M}\|_2\sup_x|X^M D^\alpha u(x)|\), and the finite sum is bounded by Schwartz seminorms. It does not assert that \(V\) is bounded on \(L^2\) or that \(\mathcal D(H)=\mathcal D(H_0)\).

The long coefficients are real and smooth. Fix \(0<\delta<1/3\), and assume

\[
\begin{gathered}
 |\partial^\beta v_{\alpha,L}(x)|
          \le C_{\alpha\beta}X^{-m(|\beta|)},\\
 m(j)=j+\delta\quad(0\le j\le2),\\
 m(j)=1+(1+\delta)j/2\quad(j\ge2).
\end{gathered}
\tag{3}
\]

The phase theorem in the prerequisite gives a real smooth \(W(\xi,t)\). On every compact \(K\subset\Omega\), for both sufficiently late time directions, it satisfies

\[
\begin{gathered}
 y(\xi,t)=\partial_\xi W(\xi,t),\\
 \partial_tW=P_0(\xi)+V_L(y(\xi,t),\xi),\\
 |\partial_\xi^\alpha(W-tP_0)|
       \le C_{\alpha,K}|t|^{1+|\alpha|-m(|\alpha|)} .
\end{gathered}
\tag{4}
\]

Every frequency derivative is included. The threshold depends on \(K\). In particular \(y/t=v+O(|t|^{-\delta})\). The modifier \(e^{-iW(D,t)}\) is unitary for every \(t\).

For a cone \(\Gamma\), measure the short coefficients by their unit-ball \(L^2\) envelope:

\[
\begin{aligned}
 A_\Gamma(r)&=\sup_{r<|z|<2r}\\
 &\quad\left(\int_{\substack{|y-z|<1\\ y\in\Gamma}}
       \sum_\alpha|v_{\alpha,S}(y)|^2\,dy\right)^{1/2},\\
 &\quad\int_1^\infty A_\Gamma(r)\,dr<\infty.
\end{aligned}
\tag{5}
\]

This permits narrow or irregular peaks. Only their local square integrals in the selected cone are controlled. The envelope is a measurable function of \(r>0\): if \(A_\Gamma(r_0)>a\), one center \(z\) realizes a value greater than \(a\), and its strict inequalities \(r<|z|<2r\) persist for \(r\) near \(r_0\). Thus \(\{r:A_\Gamma(r)>a\}\) is open. On a compact interval of positive radii every relevant unit ball lies in one bounded ball, so local square integrability bounds the envelope there.

Fix \(\sigma\in\{+1,-1\}\). Our short-range hypothesis for this time direction is: for almost every \(\xi\in\Omega\), there is a cone \(\Gamma\) containing \(\sigma v(\xi)\) for which (5) holds. Sections 2–4 prove the error estimates. Section 5 uses them to construct the limit at \(t\to\sigma\infty\). Section 6 explains why the sign in this hypothesis is necessary.

<a id="modified-wave-concentration"></a>

## 2. Concentration despite large high derivatives of the phase

Let \(\widehat u=a\in C_c^\infty(\Omega)\), and let \(\omega\) be a neighborhood of \(v(\operatorname{supp}a)\). Put \(u_t=e^{-iW(D,t)}u\).

**Lemma 2.1 (concentration).** For every multiindex \(\alpha\) and every \(N\), for sufficiently large \(|t|\),

\[
 |\partial_x^\alpha u_t(x)|
       \le C_{\alpha,N}(|x|+|t|)^{-N},
       \qquad x/t\notin\omega .
\tag{6}
\]

**Proof.** Set

\[
\begin{gathered}
 \tau=|t|,\qquad c=(1-\delta)/2,\qquad r=1-c,\\
 q=\tau^c,\qquad L=|x|+\tau,\qquad
 R=W-tP_0.
\end{gathered}
\tag{7}
\]

On the compact frequency support, \(R_\xi=O(\tau^{1-\delta})\) and every derivative of \(R\) of order \(j\ge2\) is \(O(\tau^{cj})\). The first estimate says that the actual velocity is close to the free velocity. The higher estimates can grow with \(j\); a fixed unscaled phase estimate would not have uniform constants.

Outside the stated velocity neighborhood,

\[
 |x-tv(\xi)|\ge\gamma L,\qquad
 |x-y(\xi,t)|\ge(\gamma/2)L
\tag{8}
\]

on a slightly enlarged compact frequency set, once \(\tau\) is large. For bounded \(x/t\), use the positive distance from the compact velocity set to the closed complement of \(\omega\). For large \(|x/t|\), use the triangle inequality. The error \(O(\tau^{1-\delta})\) is smaller than \(\gamma L/2\).

Change variables to \(\eta=q\xi\). Here is a smooth lattice partition with uniform bounds. Using the [explicit smooth bump construction](../providers/analysis/coordinate-inverses-and-integration.md#finite-partitions), choose \(b\ge0\), supported in \((-1,1)^n\) and strictly positive on \([-1/2,1/2]^n\). Set
\[
 S(\eta)=\sum_{g\in\mathbb Z^n}b(\eta-g),
 \qquad \chi_0(\eta)=b(\eta)/S(\eta).
\]
Only a uniformly bounded number of summands occur near any point. Hence \(S\) is smooth and periodic, with all derivatives bounded. Every point is within the closed half-cube of some lattice point; the positive minimum of \(b\) on that cube bounds \(S\) away from zero. Thus \(\chi_0\) has bounded derivatives, fixed compact support, and periodicity of \(S\) gives \(\sum_g\chi_0(\eta-g)=1\). At most \(Cq^n\) terms meet \(q\operatorname{supp}a\). After translation \(\eta=g+z\), every cell has a fixed support and uniformly bounded amplitude derivatives. Its oscillatory parameter and normalized phase are

\[
\begin{gathered}
 \lambda=L/q,\\
 \phi_g(z)=
 \frac{x\cdot(g+z)/q-W((g+z)/q,t)}{\lambda}.
\end{gathered}
\tag{9}
\]

Subtract \(\phi_g(0)\); this changes only a scalar of modulus one. By (8), the normalized gradient has norm at least \(\gamma/2\). All its derivatives are bounded uniformly. For order \(j\ge2\), the free part contributes at most \(C\tau q^{-j}/\lambda\le Cq^{1-j}\). The correction contributes at most \(C\tau^{cj}q^{-j}/\lambda=C/\lambda\). The first-order upper bound follows directly from \(|y|\le C\tau\). After the constant is subtracted, the zeroth-order bound follows on the fixed cell from the first-order bound. Enlarging the frequency support slightly supplies the fixed neighborhood needed for these estimates.

Here is the nonstationary bound in the exact uniform form needed. On a cell set \(B_g=\nabla\phi_g/|\nabla\phi_g|^2\). The lower gradient bound and the finite derivative bounds just established bound every fixed finite derivative of \(B_g\), uniformly in the cell and in \(x,t\). For the compactly supported cell amplitude \(a_g\), integration by parts gives

\[
 \int e^{i\lambda\phi_g}a_g
 =-\frac1{i\lambda}\int e^{i\lambda\phi_g}
                  \operatorname{div}(B_g a_g).
\]

Iterate this identity \(A\) times. Each resulting amplitude is a finite sum of products of derivatives of \(B_g\) and derivatives of \(a_g\) of orders at most \(A\); their supports lie in the same fixed compact cell. Their \(L^1\) norms are uniformly bounded. Hence the cell integral is bounded by \(C_A\lambda^{-A}\), with a constant independent of the lattice cell and of \(x,t\).

The Jacobian \(q^{-n}\) cancels the number \(O(q^n)\) of cells. Since \(q\le L^c\), we have \(\lambda\ge L^{1-c}\). Increase \(A\) to obtain any prescribed power in (6). Spatial differentiation replaces \(a\) by a fixed polynomial times \(a\), so the argument applies unchanged. The variable \(x/t\) and the estimates in \(\tau\) include negative time. ∎

We will also need a time-dependent amplitude. The same proof works when it has a fixed compact frequency support and

\[
 |\partial_\xi^\alpha a_t|\le C_\alpha q^{|\alpha|}.
\tag{10}
\]

Its rescaled cell derivatives are bounded, which is all the cancellation proof used.

<a id="modified-wave-rough-coefficients"></a>

## 3. Rough coefficients are integrable along the selected rays

Suppose the packet support \(K\) has one cone \(\Gamma\) as in (5), containing \(\sigma v(K)\). Shrink a bounded velocity neighborhood \(\omega\) so its closure avoids zero and \(\sigma\overline\omega\subset\Gamma\). For \(t=\sigma\tau\), the set \(t\omega\) lies inside \(\Gamma\), between radii \(a\tau\) and \(b\tau\), with \(0<a<b\).

**Lemma 3.1.** On this time half-line,

\[
 \int_T^\infty
   \|V_S(x,D)u_{\sigma\tau}\|_2\,d\tau<\infty .
\tag{11}
\]

**Proof.** A unit ball meeting \(t\omega\) has its center in a slightly wider annulus, with radii still comparable to \(\tau\). Cover that annulus by finitely many overlapping intervals \((d_j\tau,2d_j\tau)\). Their constants \(d_j>0\) are fixed. Every coefficient square integral on such a ball, restricted to \(t\omega\), is at most \(B(\tau)^2\), where

\[
 B(\tau)=\sum_{j=1}^J A_\Gamma(d_j\tau),\qquad
 \int_T^\infty B(\tau)\,d\tau<\infty .
\tag{12}
\]

The last assertion follows by substituting \(r=d_j\tau\). Overlapping intervals avoid any problem at strict annulus endpoints.

For an integer \(s>n/2\), a translated fixed cutoff, Fourier inversion, Cauchy–Schwarz and Plancherel give the local bound

\[
\begin{aligned}
 \sup_{B(z,1)}|\partial^\alpha w|^2
 &\le C\sum_{|\beta|\le s}
   \int_{B(z,2)}
         |\partial^{\alpha+\beta}w(y)|^2\,dy .
\end{aligned}
\tag{13}
\]

Indeed, apply the Fourier bound for the supremum to a cutoff times \(\partial^\alpha w\). The weight \((1+|\xi|^2)^{-s}\) is integrable. Integer-order Plancherel and Leibniz bound its \(H^s\) norm by the displayed local derivatives. All constants are independent of the center \(z\).

Insert
\(1=|B(0,1)|^{-1}\int 1_{\{|y-z|<1\}}\,dz\)
in the square norm on \(t\omega\). Cauchy–Schwarz in the finite coefficient sum, (12), (13) and Tonelli yield

\[
\begin{aligned}
 \|1_{t\omega}V_Su_t\|_2^2
 &\le C B(\tau)^2
      \sum_{|\nu|\le p+s}\|\partial^\nu u_t\|_2^2\\
 &\le C_u B(\tau)^2 .
\end{aligned}
\tag{14}
\]

The norms in the middle line are constant in time, because differentiation commutes with the unitary Fourier modifier.

The short coefficients also satisfy a weighted square-integrability condition as in (2): subtract the decaying long coefficients and, if needed, increase \(M\). On the complement of \(t\omega\), (6) therefore bounds the square norm by
\(C_N\sup_x X^{2M}(|x|+\tau)^{-2N}\).
Choose \(N\ge M+2\). This is at most \(C\tau^{-4}\). Consequently

\[
 \|V_Su_t\|_2
       \le C_u\bigl(B(\tau)+\tau^{-2}\bigr).
\tag{15}
\]

Both terms are integrable. This proves (11) for the chosen sign. ∎

No derivatives of the rough coefficients were taken. The proof uses their local square integrals, rather than replacing them by a pointwise bound.

<a id="modified-wave-long-range"></a>

## 4. The long-range difference gains an integrable power

We next compare a smooth coefficient at the physical position \(x\) with its value at the phase position \(y=W_\xi\). Select a small velocity ball centered at \(v^0\ne0\), of radius less than \(|v^0|/2\). Choose a compact frequency cutoff \(\chi_0\) and a velocity cutoff \(\chi\), so \(\chi=1\) near all velocities on the packet support. On their supports, for large \(\tau\), both \(x/t\) and \(y/t\) lie in this ball. The joining segment then stays at distance comparable to \(\tau\) from zero, for either time sign.

Let \(f\) be one long coefficient, satisfying (3). Set

\[
\begin{gathered}
 f_j(x,y)=
       \int_0^1\partial_jf(y+s(x-y))\,ds,\\
 f(x)-f(y)=\sum_j(x_j-y_j)f_j(x,y),\\
 G_{j,t}(x,\xi)=
       \chi(x/t)\chi_0(\xi)f_j(x,y(\xi,t)).
\end{gathered}
\tag{16}
\]

Joint derivatives of \(f_j\) of total order \(l\) have size at most \(C_l\tau^{-m(l+1)}\) in this region.

**Lemma 4.1 (all symbol derivatives).** For every \(\alpha,\beta\),

\[
\begin{aligned}
 |\partial_\xi^\alpha\partial_x^\beta G_{j,t}|
 &\le C_{\alpha\beta}
       \tau^{|\alpha|-m(|\alpha|+|\beta|+1)} .
\end{aligned}
\tag{17}
\]

**Proof.** The positive-order derivatives of \(y\) have bounds \(C_k\tau^{a(k)}\), where

\[
 a(1)=1,\qquad a(k)=c(k+1)\quad(k\ge2).
\tag{18}
\]

This follows from (4), including the free part of size \(O(\tau)\). Put \(k=|\alpha|\), \(b=|\beta|\). For \(k=0\), the joint derivative bound on \(f_j\) already gives (17). For \(k>0\), a chain-rule term has \(q\ge1\) outer \(y\) derivatives and positive inner orders \(k_i\), with \(\sum_i k_i=k\). Let \(\ell\) count the inner orders at least two. The others equal one, so

\[
\begin{aligned}
 \sum_i a(k_i)
 &=q-\ell+c(k-q+2\ell)\\
 &=ck+rq-\delta\ell .
\end{aligned}
\tag{19}
\]

Here \(r=(1+\delta)/2\). Since \(q+b+1\ge2\), the linear part of \(m\) gives the exponent

\[
\begin{aligned}
 &-m(q+b+1)+\sum_i a(k_i)\\
 &=ck-1-r(b+1)-\delta\ell\\
 &\le k-m(k+b+1).
\end{aligned}
\tag{20}
\]

This controls every finite chain partition. Frequency derivatives falling on \(\chi_0\) are harmless because \(k-m(k+b+1)\) is nondecreasing in \(k\). Each position derivative falling on \(\chi(x/t)\) contributes \(\tau^{-1}\); the increments of \(m\) are at most one, so the same target at the total position order follows. This proves (17). ∎

We need only a fixed finite number of these bounds to control the operators. Both \(G_{j,t}\) and its first frequency derivative obey the weaker convenient estimate

\[
\begin{gathered}
 |\partial_\xi^\alpha\partial_x^\beta a_t|\\
 \le C_{\alpha\beta}\tau^{-1-\delta}
                 \tau^{c|\alpha|-r|\beta|},\\
 a_t=G_{j,t}\ \text{or }\partial_{\xi_j}G_{j,t}.
\end{gathered}
\tag{21}
\]

For \(G\), the zeroth estimate is exact and the positive-order exponent in (17) is smaller by \(c\). For \(\partial_{\xi_j}G\), all relevant arguments of \(m\) are at least two, and (21) is exactly its exponent.

Let \(a_t(x,D)\) mean left, or Kohn–Nirenberg, quantization. The unitary dilation
\(U_\tau w(z)=\tau^{nc/2}w(\tau^cz)\)
conjugates its symbol to \(a_t(\tau^cz,\tau^{-c}\eta)\). Divide this symbol by \(\tau^{-1-\delta}\). Each derivative is bounded by a constant times
\(\tau^{(c-r)|\beta|}=\tau^{-\delta|\beta|}\le1\).
Choose one integer \(N>n/2\). The [finite-derivative \(L^2\) theorem](../providers/analysis/finite-derivative-l2.md#finite-derivative-l2) requires only \(|\alpha|\le2N\), \(|\beta|\le2N\) for each conjugated symbol. For both symbols in (21), (17) therefore uses at most \(2N+1\) frequency and \(2N\) position derivatives of \(G\).

<a id="modified-wave-finite-derivative-budget"></a>

The segment formula uses at most \(4N+2\) derivatives of \(f\) and \(2N+2\) derivatives of \(W\), all supplied by (3)–(4). Thus the theorem applies with constants independent of \(\tau\), and

\[
\begin{gathered}
 \|G_{j,t}(x,D)\|_{2\to2}\\
 +\|\partial_{\xi_j}G_{j,t}(x,D)\|_{2\to2}\\
       \le C\tau^{-1-\delta}.
\end{gathered}
\tag{22}
\]

This reduction needs no additional symbol-class theorem at a moving scale.

<a id="modified-wave-commutator"></a>

The order of the factors matters. Left quantization gives

\[
\begin{aligned}
 &\sum_jG_{j,t}(x,D)(x_j-y_j(D,t))\\
 &=\chi(x/t)\bigl(f(x)-f(y(D,t))\bigr)\\
 &\quad\chi_0(D)
       -i\sum_j\partial_{\xi_j}G_{j,t}(x,D).
\end{aligned}
\tag{23}
\]

To verify the sign, use
\(G(x,D)x_j=x_jG(x,D)-i(\partial_{\xi_j}G)(x,D)\),
then the scalar identity in (16). On a packet,

\[
 (x_j-y_j(D,t))u_t=e^{-iW(D,t)}(x_j u).
\tag{24}
\]

Fourier differentiation proves this identity directly. Choose \(\chi_0=1\) on a neighborhood of the Fourier support of \(u\), which also contains the supports of its frequency derivatives. Equations (22)–(24) imply

\[
\begin{aligned}
 &\|\chi(x/t)(f(x)-f(y(D,t)))u_t\|_2\\
 &\le C\tau^{-1-\delta}\\
 &\quad\left(\sum_j\|x_j u\|_2+\|u\|_2\right).
\end{aligned}
\tag{25}
\]

Both terms outside \(\chi\) are rapidly small. The \(f(x)u_t\) term follows from (6) and boundedness of \(f\). For the multiplier term, the finite chain rule gives

\[
 |\partial_\xi^\alpha f(y(\xi,t))|
       \le C_\alpha\tau^{c|\alpha|-\delta}
\tag{26}
\]

on the fixed frequency support. For order zero this is the coefficient decay. At positive order \(k\), if the outer order is one, the exponent is \(-\delta\) for \(k=1\), and \(-1-\delta+c(k+1)\le ck-\delta\) for \(k\ge2\). If the outer order is \(q\ge2\), (19) and \(m(q)=1+rq\) give \(ck-1-\delta\ell\le ck-\delta\). This proves (26), so the time-dependent-amplitude version (10) of concentration applies to \(f(y(\xi,t))\widehat u\).

Apply (25) to every packet \(D^\alpha u\) in the finite differential sum. The rapid tails have arbitrarily integrable powers. We have proved

\[
\begin{gathered}
 \int_T^\infty
 \|(V_L(x,D)\\
 -V_L(y(D,\sigma\tau),D))
                u_{\sigma\tau}\|_2\,d\tau<\infty .
\end{gathered}
\tag{27}
\]

To make the rapid-tail step explicit, a pointwise bound \(C_N(|x|+\tau)^{-N}\) has \(L^2\) norm at most \(C_N\tau^{n/2-N}\), by substituting \(x=\tau z\) in its square integral when \(2N>n\). Choose \(N>n/2+1\) to obtain a time-integrable bound. The amplitude estimate (26) and the fixed compact Fourier supports allow this choice for every differential term. This part is valid for both time directions; the short-range cone condition is where the sign enters.

<a id="modified-wave-existence"></a>

## 5. Integrate the error, then extend by density

**Theorem 5.1 (modified wave operators).** Assume (2)–(4) and the self-adjoint extension described in Section 1. Fix a sign \(\sigma\). Suppose (5) holds in a cone containing \(\sigma v(\xi)\) for almost every regular frequency \(\xi\). Then the strong limit

\[
 \mathcal W_\sigma u
   =\lim_{t\to\sigma\infty}
        e^{itH}e^{-iW(D,t)}u,\qquad u\in L^2,
\tag{28}
\]

exists and is an isometry. It satisfies, for every real \(s\),

\[
\begin{gathered}
 e^{isH}\mathcal W_\sigma
       =\mathcal W_\sigma e^{isH_0},\\
 \mathcal W_\sigma\mathcal D(H_0)\subset\mathcal D(H),
 \qquad H\mathcal W_\sigma u=\mathcal W_\sigma H_0u.
\end{gathered}
\tag{29}
\]

If the hypothesis holds for both signs, both operators exist. The theorem imposes no ellipticity, no lower bound, and no equality of the full free and perturbed domains.

**Proof.** Let \(\Omega_\sigma\) be the set of regular frequencies whose signed velocity belongs to at least one cone satisfying (5). This set is open: membership of a continuous velocity in a fixed open cone persists nearby. Its complement inside \(\Omega\) is null by hypothesis. The critical set is null as well. Indeed, one partial derivative of the nonconstant polynomial is a nonzero polynomial. In one variable a nonzero polynomial has finitely many roots: factoring out one root reduces the degree, so induction bounds their number by the degree. In dimension \(n\), write a nonzero polynomial as \(\sum_j a_j(\xi')\xi_n^j\), with at least one nonzero coefficient polynomial \(a_j\). Outside that coefficient's null zero set, supplied by induction in dimension, every one-dimensional fiber has finitely many roots. Tonelli on each bounded box makes the full zero set null; the exceptional base set contributes zero because the box has bounded height. A countable union of boxes covers the space. Applying this fact to the nonzero partial derivative proves the critical-set assertion and hence that \(\Omega_\sigma\) has full measure.

For completeness, put
\[
 K_j=\{\xi:|\xi|\le j,
       \operatorname{dist}(\xi,\Omega_\sigma^c)\ge1/j\}.
\]
When the complement is empty take its distance to be infinity. These compact subsets of \(\Omega_\sigma\) increase to that open set. For any \(a\in L^2\), dominated convergence gives \(1_{K_j}a\to a\). For fixed \(j\), convolution with a smooth unit-integral bump supported in a ball of radius \(\varepsilon<1/(2j)\) gives a compact smooth function supported inside \(\Omega_\sigma\). The programme convolution proof makes its \(L^2\) error tend to zero with \(\varepsilon\). Plancherel therefore proves that the selected packets are dense in \(L^2\).

Cover the compact support of such a packet by finitely many frequency neighborhoods, each mapped by the signed velocity into one good cone and by the velocity into one ball separated from zero. The [finite bump partition proof](../providers/analysis/coordinate-inverses-and-integration.md#finite-partitions) splits the packet into finitely many compact smooth pieces in those neighborhoods. Lemma 3.1 and (27) give an integrable residual on the chosen time end for each piece.

For bounded time intervals, \(u_t=e^{-iW(D,t)}u\) is a \(C^1\) Schwartz path. Its Fourier transform has fixed compact support and a smooth amplitude. The weighted condition makes \(Vu_t\) continuous in \(L^2\). The extension \(H\) agrees with \(H_0+V\) on this initial Schwartz domain, so \(u_t\in\mathcal D(H)\) and \(Hu_t\) is continuous. The unitary-group product rule yields

\[
\begin{aligned}
 \frac{d}{dt}(e^{itH}u_t)&\\
 &=i e^{itH}(H_0+V-W_t(D,t))u_t\\
 &=i e^{itH}
   \bigl(V_S+V_L(x,D)\\
 &\quad -V_L(y(D,t),D)\bigr)u_t
\end{aligned}
\tag{30}
\]

on the sufficiently late half-line. The last equality uses the exact equation in (4). The product rule follows by splitting a difference quotient into the change in the vector and the group derivative on a fixed domain vector. Graph continuity verifies the domain requirements.

The integral of the norm of (30) is finite. On a finite interval its continuous vector integral exists by the Riemann-sum construction in [Approximation and convolution, Section 5](../providers/analysis/euclidean-approximation-and-convolution.md#oscillatory-integrals-and-averages). Pair with an arbitrary fixed vector and apply the scalar fundamental theorem; commuting the pairing with the Riemann limit proves that this integral equals the difference of the endpoint vectors. The integral norm is bounded by the integral of the norm. Its vanishing tail therefore makes \(e^{itH}u_t\) Cauchy at the selected end. Every approximating operator is unitary, so the limit preserves the packet's norm. For a general \(u\), choose a dense packet \(h\). If \(A_t=e^{itH}e^{-iW(D,t)}\), then
\(\|A_t(u-h)-A_r(u-h)\|\le2\|u-h\|\).
This proves convergence and isometry on all of \(L^2\).

<a id="modified-wave-intertwining"></a>

To prove intertwining, fix \(s\in\mathbb R\). On every compact \(K\subset\Omega\),

\[
\begin{aligned}
 &W(\xi,t)-W(\xi,t-s)-sP_0(\xi)\\
 &=\int_{t-s}^{t}V_L(y(\xi,r),\xi)\,dr\\
 &=O_{K,s}(|t|^{-\delta}).
\end{aligned}
\tag{31}
\]

The oriented integral includes negative \(s\). Its exponential tends uniformly to one on \(K\). The multiplier has modulus one, and \(\Omega\) has full measure, so dominated convergence proves its strong convergence to the identity on all of \(L^2\). Reindexing the limit by \(t+s\) gives

\[
\begin{gathered}
 e^{isH}\mathcal W_\sigma e^{-isH_0}u\\
 =\lim_{t\to\sigma\infty}
 e^{itH}e^{-iW(D,t)}\\
 \quad e^{i(W(D,t)-W(D,t-s)-sH_0)}u\\
 =\mathcal W_\sigma u .
\end{gathered}
\tag{32}
\]

For \(u\in\mathcal D(H_0)\), the group difference quotient in (29) therefore converges on \(\mathcal W_\sigma u\) to \(i\mathcal W_\sigma H_0u\). The general self-adjoint spectral domain condition identifies this limit with \(iH\mathcal W_\sigma u\). More explicitly, boundedness of the quotients and Fatou in their spectral square integrals imply the finite second moment; dominated convergence then identifies the derivative. This proves the domain inclusion and operator identity. ∎

<a id="modified-wave-spectral-measures"></a>

**Spectral measures of the range.** The range is closed: a convergent sequence of image vectors comes from a Cauchy sequence, since the map is an isometry. Every vector in the range has an absolutely continuous spectral measure, as follows.

First consider the free measure of \(u\), which is the pushforward of \(|\widehat u(\xi)|^2d\xi\) by \(P_0\). If \(N\subset\mathbb R\) is a null Borel set, then \(P_0^{-1}(N)\) is null. The critical set was proved null above. Near each remaining point, some partial derivative is nonzero and the [coordinate inverse theorem](../providers/analysis/coordinate-inverses-and-integration.md#coordinate-inverse) gives the coordinates \((P_0(\xi),\xi')\). Tonelli makes \(N\times\mathbb R^{n-1}\) null, and the [proved change-of-variables formula](../providers/analysis/coordinate-inverses-and-integration.md#coordinate-integration) gives null measure to its preimage in that chart. A countable chart cover suffices: choose from the countable rational-ball base balls lying in these chart neighborhoods and covering the regular set. Thus every free scalar spectral measure is absolutely continuous.

Next, let \(J\) be any isometry satisfying \(e^{isH}J=Je^{isH_0}\), in particular \(J=\mathcal W_\sigma\). For \(g=Ju\), isometry and the group identity give \((e^{-itH}g,g)=(e^{-itH_0}u,u)\). For any self-adjoint \(A\) and \(\operatorname{Im}z>0\), scalar spectral integration yields

\[
 (R_A(z)f,f)
 =i\int_0^\infty e^{itz}(e^{-itA}f,f)\,dt.
\]

Indeed, the absolute double integral is bounded by \(\|f\|^2/\operatorname{Im}z\). Fubini therefore applies, and the inner scalar integral is \(i\int_0^\infty e^{it(z-\lambda)}dt=(\lambda-z)^{-1}\). The two scalar resolvent functions for \(g\) and \(u\) are consequently equal. They determine equal finite spectral measures. To check this last step including atoms, multiply the imaginary part at \(a+i\varepsilon\) by \(\varepsilon\); its kernel \(\varepsilon^2/((\lambda-a)^2+\varepsilon^2)\) is bounded by one and tends to the indicator of \(\{a\}\). Dominated convergence gives equality of atom masses. The [proved scalar Stone formula](resolvents-domains-and-spectral-density.md#u001-stone-and-density) then gives equality on every bounded open interval, including its half-endpoint terms. Equality of total masses follows from isometry. The [finite-measure uniqueness lemma](../providers/analysis/finite-derivative-l2.md#pi-lambda-uniqueness), applied to intervals and the whole line, gives equality on every Borel set. Hence the measure of \(Ju\) is absolutely continuous.

Equality of the range with the whole absolutely continuous subspace is a further assertion. Here is the isometry calculation used in Exercise 7.5. If \(J_+\) and \(J_-\) are isometries with the same range \(\mathcal K\), then \(J_\pm^*J_\pm=I\) and \(J_\pm J_\pm^*=P_{\mathcal K}\). The latter identity follows directly: it fixes each vector \(J_\pm f\) and annihilates its orthogonal complement by the adjoint pairing. Therefore, for \(S=J_+^*J_-\), both \(S^*S\) and \(SS^*\) are the identity. Without equality of ranges, the adjoint bound gives only \(\|S\|\le1\). These adjoints and orthogonal projections have their elementary proof in [Hilbert-space tools](../providers/analysis/finite-trace-ideals.md#elementary-hilbert-tools).


<a id="modified-wave-sign-counterexample"></a>

## 6. A cone for positive velocity can miss every negative-time ray

On the line, choose a real smooth \(0\le\chi_-\le1\), equal to one for \(x\le-1\) and zero for \(x\ge0\). For \(b>0\), put

\[
\begin{gathered}
 H_0=D^3,\qquad H=D^3+b\chi_-(x),\\
 V_L=0,\qquad W(\xi,t)=t\xi^3 .
\end{gathered}
\tag{33}
\]

The operator \(H\) is self-adjoint on \(H^3(\mathbb R)\). Fourier multiplication gives self-adjointness of \(D^3\), and adding the bounded real multiplier preserves self-adjointness on that domain. To verify this directly, for self-adjoint \(A\) and bounded symmetric \(B\), the adjoint equation for \(A+B\) says that the adjoint equation for \(A\) holds with the vector \(w-Bz\). Thus \(\mathcal D((A+B)^*)=\mathcal D(A^*)\), and \((A+B)^*=A+B\).

The same elementary domain calculation also justifies unitary changes of variables used in Exercise 7.4. For a unitary \(U\), testing adjoint pairings shows \((UAU^*)^*=UA^*U^*\) with domain \(UD(A^*)\). Its spectral projections are \(UE_A(B)U^*\), by bounded truncation of the moment formula and uniqueness of the spectral measure. In particular its group is \(Ue^{itA}U^*\). If \(U\) multiplies by a smooth scalar of modulus one with bounded first derivative, the weak product rule gives \(U:H^1\to H^1\); the same holds for \(U^*\). One can verify this rule first on compact smooth functions and pass to the limit using the [proved \(H^1\) density](../providers/analysis/euclidean-approximation-and-convolution.md#integer-sobolev-density) and the two bounded multiplier norms. Thus the differential conjugation in that exercise holds on the whole stated domain.

The weighted coefficient condition holds with \(M=1\). Every nonzero frequency has velocity \(3\xi^2>0\). In the cone \((0,\infty)\), the short coefficient vanishes, so (5) is exactly zero. The positive wave operator exists by Theorem 5.1.

The negative limit with this modifier fails. Take nonzero \(u\) with \(\widehat u\in C_c^\infty((a,d))\), \(0<a<d\). For negative time and \(x\ge-1\), the free phase derivative is \(x+3|t|\xi^2\), bounded below by a positive multiple of \(|x|+|t|\) for sufficiently large \(|t|\). All normalized phase derivatives are bounded. The nonstationary estimate and integration in the half-line give

\[
 \|1_{\{x\ge-1\}}e^{-itH_0}u\|_2
       \le C_N|t|^{1/2-N}.
\tag{34}
\]

Compare first with the correct constant background on the left:
\(B_t=e^{itH}e^{-it(H_0+b)}\).
Its derivative on this packet is
\(i e^{itH}b(\chi_--1)e^{-it(H_0+b)}u\).
The coefficient vanishes for \(x\le-1\). Equation (34) with \(N=2\) is integrable, so Cook's argument gives \(B_tu\to Zu\) as \(t\to-\infty\). Since each \(B_t\) is unitary, \(\|Zu\|=\|u\|>0\).

But the proposed comparison satisfies

\[
\begin{gathered}
 e^{itH}e^{-itH_0}u=e^{ibt}B_tu,\\
 t_n=-2\pi n/b,\qquad s_n=-(2n+1)\pi/b.
\end{gathered}
\tag{35}
\]

Its limits along these two sequences are \(Zu\) and \(-Zu\). They differ. The missing negative cone permits a nonzero background phase on the left; the positive cone contains no information about it.

Example (33) shows that a cone condition at the positive velocity alone does not control both time directions. Theorem 5.1 uses the signed velocity required by the general nonelliptic assertion.

When the short coefficients satisfy (5) in every direction, both signs are available. The example addresses the directional hypothesis when coefficients are allowed to behave differently in different cones.

### Use the conclusion

Apply the signed-velocity counterexample before reading the general existence proof. Keep the frequency derivatives of the phase, rough short-range coefficient bounds and arbitrary self-adjoint realization as distinct inputs.

<a id="modified-wave-exercises-and-solutions"></a>

## 7. Five exercises with complete solutions

**Exercise 7.1 (first check: frequency is not escape direction).** On the line let \(P_0(\xi)=\xi^3+\xi\). Find the regular set and the velocities of packets near \(\xi=1\) and \(\xi=-1\). For each time sign, identify the relevant half-line. Does changing the sign of frequency exchange those half-lines?

**Solution 7.1.** The derivative is \(3\xi^2+1\), which is positive everywhere. Thus \(\Omega=\mathbb R\), and both selected packets have velocity \(4\). Their positive-time centers are near \(4t>0\); their negative-time centers are near \(4t<0\). The good cone for the positive limit is the positive half-line, and for the negative limit it is the negative half-line. The two frequency signs have the same velocity. Frequency sign alone does not determine the direction sampled by this polynomial.

**Exercise 7.2 (a decay condition without a spare power).** In \(\mathbb R^n\), let
\[
 f_\beta(x)=
  \frac{1}{(e+X)\,[\log(e+X)]^\beta},
       \qquad \beta\ge0 .
\tag{36}
\]
Use this real multiplication potential as \(V_S\), with \(V_L=0\). For the cone \(\Gamma=\mathbb R^n\setminus\{0\}\), determine exactly when (5) holds. Explain why the result gives wave existence for any real nonconstant \(P_0\), although \(f_\beta\) is not bounded by a fixed \(CX^{-1-\varepsilon}\) when \(\beta>1\).

**Solution 7.2.** For large \(r\), a unit ball with center \(r<|z|<2r\) has \(X\) comparable to \(r\), and \(\log(e+X)\) comparable to \(\log r\). Its volume is fixed; removal of the single point zero changes no integral. Both upper and lower bounds therefore give

\[
 A_\Gamma(r)\asymp
          \frac1{r(\log r)^\beta}.
\tag{37}
\]

The substitution \(s=\log r\) makes its tail integral \(\int s^{-\beta}\,ds\), which is finite exactly for \(\beta>1\). The bounded initial radial interval is harmless. The potential is bounded and real, so \(H_0+f_\beta\) is self-adjoint on \(\mathcal D(H_0)\), by the bounded-perturbation argument in Section 6. The weighted condition holds after choosing \(M\) large enough. The cone contains both signed velocities, so Theorem 5.1 supplies both limits when \(\beta>1\). For every \(\varepsilon>0\), the ratio of \(f_\beta\) to \(X^{-1-\varepsilon}\) is comparable to \(X^\varepsilon/(\log X)^\beta\), which tends to infinity. The integral criterion still applies. For \(\beta\le1\), this calculation says that the stated sufficient hypothesis fails; it makes no claim about whether a wave operator can exist by another argument.

**Exercise 7.3 (the derivative count and the operator sign).** Set \(\delta=1/5\). Compute the exponent in (17) for \(|\alpha|=3\), \(|\beta|=2\), and for the same derivatives of \(\partial_{\xi_j}G_{j,t}\). Compare with (21). Check the sign of the last term in (23), and bound the integral from \(T\) to infinity of an operator error bounded by \(C\tau^{-1-\delta}\).

**Solution 7.3.** Here \(c=2/5\), \(r=3/5\), and \(m(j)=1+3j/5\) for \(j\ge2\). The two exact exponents are

\[
\begin{aligned}
 3-m(6)&=3-23/5=-8/5,\\
 4-m(7)&=4-26/5=-6/5.
\end{aligned}
\tag{38}
\]

The convenient bound (21) has exponent
\(-6/5+(2/5)3-(3/5)2=-6/5\).
It is weaker than the first exact bound by \(2/5=c\), and equals the second. After the dilation and division by \(\tau^{-6/5}\), these derivatives have exponent at most \((c-r)2=-2/5\), so they are bounded for \(\tau\ge1\).

Fourier differentiation gives
\([x_j,G(x,D)]=i(\partial_{\xi_j}G)(x,D)\).
Therefore \(G(x,D)x_j=x_jG(x,D)-i(\partial_{\xi_j}G)(x,D)\), proving the minus sign in (23). Finally

\[
 \int_T^\infty C\tau^{-6/5}\,d\tau
       =5C T^{-1/5}.
\tag{39}
\]

The frequency-derivative commutator is integrable with exactly the same operator bound as the main coefficient difference.

**Exercise 7.4 (solve a complete long-range comparison).** Let \(a>0\), \(b\in\mathbb R\), \(0<\delta<1/3\), and
\(H_0=aD\), \(H=aD+b(1+x^2)^{-\delta/2}\).
Define \(F(0)=0\), \(F'(x)=b(1+x^2)^{-\delta/2}/a\). Find a phase satisfying (4), calculate both modified wave operators, and determine whether their ranges are complete.

**Solution 7.4.** The real multiplication potential is bounded. Its \(j\)-th derivative is \(O(X^{-j-\delta})\), which implies (3): the exponents agree through order two, and for \(j\ge2\) the difference \(j+\delta-m(j)=c(j-2)\) is nonnegative. All velocities equal \(a\). Put

\[
 W(\xi,t)=at\xi+F(at).
\tag{40}
\]

Then \(W_\xi=at\) and \(W_t=a\xi+b(1+a^2t^2)^{-\delta/2}\), giving the exact equation. The correction is \(O(|t|^{1-\delta})\); all its positive frequency derivatives vanish. Thus every bound in (4) holds.

The unitary multiplier \(Uu=e^{-iF(x)}u\) preserves \(H^1\), because \(F'\) is bounded. Differentiation gives \(HU=UH_0\). Hence \(H=UH_0U^*\) on \(H^1\), and its evolution is \(Ue^{itH_0}U^*\). Since \(e^{itH_0}u(x)=u(x+at)\), the comparison operator is

\[
\begin{gathered}
 e^{itH}e^{-iW(D,t)}u(x)\\
 =e^{-iF(x)}
   e^{i(F(x+at)-F(at))}u(x).
\end{gathered}
\tag{41}
\]

For each fixed \(x\), \(F(x+at)-F(at)\) is the integral of \(F'\) over an interval of fixed length. It tends to zero at both time ends because \(F'\) tends to zero. The exponential has modulus one, so dominated convergence in the square norm gives \(\mathcal W_+=\mathcal W_-=U\). These operators are unitary onto \(L^2\). The transport operator \(aD\) has entirely absolutely continuous spectrum by Fourier multiplication and the linear change of variable \(\lambda=a\xi\). Its unitary conjugate \(H\) has the same spectral type. Thus both ranges equal \(\mathcal H_{\mathrm{ac}}(H)=L^2\).

**Exercise 7.5 (the freedom in a fixed phase).** Assume both limits in (28) exist. At each time end, replace \(W(\xi,t)\) by \(W(\xi,t)+C_\sigma(\xi)\), where \(C_\sigma\) is a real measurable finite function. Find the new wave operators, their domain intertwining, and the change in \(S=\mathcal W_+^*\mathcal W_-\). This replacement need not solve the same Hamilton–Jacobi equation.

**Solution 7.5.** Write \(M_\sigma=e^{-iC_\sigma(D)}\), a unitary Fourier multiplier. The new approximant is exactly \(A_tM_\sigma\), so

\[
\begin{gathered}
 \widetilde{\mathcal W}_\sigma=\mathcal W_\sigma M_\sigma,\\
 \widetilde S=e^{iC_+(D)}S e^{-iC_-(D)} .
\end{gathered}
\tag{42}
\]

Multiplication by a function of modulus one preserves the Fourier condition \(P_0\widehat u\in L^2\), so \(M_\sigma\) preserves \(\mathcal D(H_0)\) and commutes there with \(H_0\). It also commutes with the free unitary group. Equation (29) therefore proves both the group and domain identities for the new wave operators. Their ranges and isometry properties are unchanged. If the original two ranges coincide, \(S\) is unitary by the isometry calculation in *Wave operators and modified phases*, and the displayed formula keeps \(\widetilde S\) unitary. If their ranges have not been shown to coincide, both \(S\) and \(\widetilde S\) are only known from these assumptions to be contractions. A fixed phase changes the comparison's coordinates; it cannot supply a missing completeness proof.

## References

[O] Sung-Jin Oh, [*Lecture Notes for Math 222A*, free evolving lecture notes](https://math.berkeley.edu/~sjoh/pdfs/notes-math222a.pdf), University of California, Berkeley, Fall 2023, §2.4.1, pp. 23–24.

[T] Gerald Teschl, [*Mathematical Methods in Quantum Mechanics: With Applications to Schrödinger Operators*, free author's online second edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf), 2014, Theorem 5.1, pp. 145–146, Theorem 12.2 and Lemma 12.3, pp. 284–285.

[HW] Lars Hörmander, [*The existence of wave operators in scattering theory*, freely readable journal scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0146/LOG_0012.pdf), 1976, Theorem 3.9 and its proof, pp. 83–86, and Lemma A.1, p. 88.
