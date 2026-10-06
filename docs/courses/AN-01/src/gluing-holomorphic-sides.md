# Gluing holomorphic sides

*Reconstructed by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. The earlier edition was written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original lesson exposition and exercises: CC0. The separately credited programme prerequisites retain their own licences.*

The boundary value of a holomorphic function can exist as a distribution even when the function has no ordinary boundary trace. The difference between the upper and lower boundary distributions measures the failure of two holomorphic sides to join. We construct the joining distribution, compute its source, and prove that equality of the two boundaries is exactly the condition for holomorphic continuation. We then recover local polynomial growth from boundary measurements alone.

The complete analytical inputs are available in [Order, positivity and distributional limits](order-positivity-and-limits.md), including finite-order tests and complete smooth support spaces, and [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), including the finite-test boundary theorem, relative Cauchy–Pompeiu formula, radial averaging, harmonic distribution regularity and disk power series. Their accompanying scalar, integration and functional foundation selections supply the elementary proofs they use. The finite-\(C^k\) completeness argument needed here is included below. All distributional pairings are complex linear, and \(\bar\partial=(\partial_x+i\partial_y)/2\).

## Integrating the growth into a logarithm

Let \(I\) be a nonempty open interval and \(\gamma>0\). Write

\[
 S=I+i(-\gamma,\gamma),\qquad
 S^+=I+i(0,\gamma),\qquad S^-=I+i(-\gamma,0).
 \tag{1.1}
\]

Initially suppose that \(f\) is holomorphic separately on \(S^+\) and \(S^-\), and, for an integer \(N\ge0\),

\[
 |f(x+iy)|\le C|y|^{-N}.
 \tag{1.2}
\]

The preceding boundary theorem supplies upper and lower distributions \(f_+,f_-\), with continuous actions on compact \(C^{N+1}\) tests. Its uniform estimates also permit moving tests in that same norm.

**Lemma 1.1 (a primitive with integrable growth).** On each side there is a holomorphic \(G\) with \(\partial_x^NG=f\). For every compact interval \(J\Subset I\), and a fixed \(0<T<\gamma\), it satisfies

\[
 |G(x+iy)|\le C_J\bigl(1+\log(T/|y|)\bigr),
 \qquad x\in J,\quad 0<|y|<T.
 \tag{1.3}
\]

For \(N=0\) take \(G=f\). Arbitrary values on the real interval make the piecewise \(G\) a locally integrable function on \(S\).

**Proof.** A primitive on the upper side can be constructed without a path-independence theorem. Fix \(x_0\in I\) and put

\[
 H(x+iy)=\int_{x_0}^x f(s+iT)\,ds
                  +i\int_T^y f(x+it)\,dt.
 \tag{1.4}
\]

These are integrals over compact intervals of smooth functions at each positive height. The fundamental theorem and the Cauchy–Riemann equation \(f_y=if_x\) give

\[
 H_y=if(x+iy),\qquad
 H_x=f(x+iT)+\int_T^y f_y(x+it)\,dt=f(x+iy).
 \tag{1.5}
\]

Thus \(H\) is holomorphic and \(H_x=f\). The horizontal integral is bounded when \(x\) stays in \(J\), by taking the compact interval joining \(J\) to \(x_0\). If the input has a bound by \(t^{-q}\) on a compact horizontal interval, the vertical integral is bounded by a constant plus \(y^{-(q-1)}/(q-1)\) for \(q>1\), and by a constant plus \(\log(T/y)\) for \(q=1\). Apply this construction \(N\) times. Each of the first \(N-1\) steps reduces the integer exponent by one; the last gives the logarithm. When \(N=0\), boundedness gives (1.3) directly.

On the lower side use reference height \(-T\) and the same two integrals, with the vertical parameter negative. Their absolute estimates are unchanged after replacing height by its absolute value. Finally, the nonnegative integration theorem from the supplied foundation gives

\[
 \int_0^T\log(T/y)\,dy
 =\int_0^T\int_y^T\frac{dt}{t}\,dy
 =\int_0^T\frac{t}{t}\,dt=T.
\]

The logarithmic majorant therefore has integral \(2T\). On compact sets away from height zero, \(G\) is smooth and bounded. This proves the local integrability. \(\square\)

## The repeated integral gives the extension and its source

At a nonzero height define the horizontal pairing

\[
 A_\phi(y)=\int_I f(x+iy)\phi(x,y)\,dx.
\]

**Theorem 2.1 (order of the extension and the jump).** For \(\phi\in C_c^N(S)\), the repeated integral

\[
 F(\phi)=\int_{-\gamma}^{\gamma}A_\phi(y)\,dy
 \tag{2.1}
\]

exists, with the inner \(x\)-integral taken first and its value at height zero ignored. The outer integral is absolutely convergent. On smooth tests it defines an order-at-most-\(N\) distribution equal to \(f\) away from the real interval, and

\[
 \bar\partial F=\frac{i}{2}(f_+-f_-)\otimes\delta_{y=0}.
 \tag{2.2}
\]

Here \((b\otimes\delta_{y=0})(\phi)=b(\phi(\cdot,0))\). Restriction of a smooth compact test to this line has compact support and its derivative seminorms are bounded by those of the test, so this formula defines a distribution. Equality (2.2) also holds on compact \(C^{N+1}\) tests.

**Proof.** Put the horizontal projection of the support inside a compact interval \(J\Subset I\). Integrating by parts \(N\) times gives

\[
 A_\phi(y)=(-1)^N\int_I G(x+iy)\partial_x^N\phi(x,y)\,dx.
 \tag{2.3}
\]

Every end term vanishes because the test and its derivatives are zero outside a compact subinterval. This argument needs only \(C^N\) regularity. Near height zero the right side is bounded by
\(C_J|J|\|\phi\|_{C^N}(1+\log(T/|y|))\); on the remaining compact height range it is bounded by smoothness. Thus the outer integral is absolutely convergent. The absolutely integrable expression on the right permits Fubini and yields

\[
 F(\phi)=(-1)^N\int_S G(x+iy)\partial_x^N\phi(x,y)\,dx\,dy.
 \tag{2.4}
\]

The local integral of \(|G|\) bounds this by a constant times the test's \(C^N\) norm. This proves the order. Definition (2.1) contains no primitive, so different choices in Lemma 1.1 give the same extension. For support away from the real interval, it is the usual integral of \(f\phi\).

Take now \(\phi\in C_c^{N+1}(S)\). By the preceding absolute outer convergence,

\[
 (\bar\partial F)(\phi)
       =-\lim_{\varepsilon\downarrow0}
           \int_{|y|>\varepsilon}A_{\bar\partial\phi}(y)\,dy.
 \tag{2.5}
\]

The signs can be obtained directly by coordinate integration. On either truncated side,
\(f\bar\partial\phi=\bar\partial(f\phi)\), because \(f\) is holomorphic. The integral of the \(x\)-derivative is zero. The integral of the \(y\)-derivative is \(-A_\phi(\varepsilon)\) on the upper side and \(A_\phi(-\varepsilon)\) on the lower side. The minus sign in the distributional derivative therefore gives

\[
 (\bar\partial F)(\phi)
       =\lim_{\varepsilon\downarrow0}\frac{i}{2}
                   \bigl(A_\phi(\varepsilon)-A_\phi(-\varepsilon)\bigr).
 \tag{2.6}
\]

The functions \(\phi(\cdot,\pm\varepsilon)\) have one compact horizontal support. Uniform continuity of their horizontal derivatives through degree \(N+1\) shows convergence to \(\phi(\cdot,0)\) in \(C^{N+1}\). The moving-test boundary estimate in the preceding lesson applies, proving (2.2) on exactly the stated finite-regularity tests. \(\square\)

**Example 2.2 (why the order of integration matters).** Take \(f(z)=z^{-2}\) and a smooth test equal to one near zero. Its growth is bounded by \(|y|^{-2}\), so Theorem 2.1 applies. Its joint absolute integral diverges. For a direct proof using only the supplied disk-area formula, take disjoint annuli
\(r2^{-j-1}<|z|<r2^{-j}\) in the disk where the test is one. Each has area \(3\pi r^2 4^{-j}/4\), and on it \(|z|^{-2}\ge r^{-2}4^j\). Every annulus contributes at least \(3\pi/4\); summing gives infinity. Thus the ordinary absolute version of Fubini does not apply to \(f\phi\), whereas (2.3) gives an integrable majorant for its horizontal pairing.

For \(z^{-1}\), the preceding lesson proves planar local integrability. Its jump is \(-2\pi i\delta_0\), so (2.2) gives \(\bar\partial F=\pi\delta_{(0,0)}\). The jump of \(z^{-2}\) is \(2\pi i\delta'_0\), giving \(\bar\partial F=-\pi\partial_x\delta_{(0,0)}\).

## Matching boundary distributions forces continuation

**Theorem 3.1 (matching is exactly the continuation condition).** Under (1.2), \(f\) extends to a holomorphic function on \(S\) if and only if \(f_+=f_-\). That holomorphic extension is unique.

**Proof.** Matching makes the source (2.2) zero. The harmonic distribution lemma and Proposition 2.1 of the preceding lesson prove, by local radial averaging, that a distribution annihilated by \(\bar\partial\) has a holomorphic representative \(h\). Away from height zero, \(h\) and \(f\) give the same distribution. Their difference is continuous and must vanish pointwise: if nonzero at a point, multiplication by a constant phase and integration against a sufficiently small nonnegative bump would give a nonzero pairing. Thus \(h=f\) on both sides. The identity principle below proves uniqueness.

Conversely, if \(h\) is a holomorphic extension, it is smooth by the proved disk theory. For any compact horizontal test, \(h(x\pm iy)\) tends uniformly to \(h(x)\). Both boundary pairings consequently equal its ordinary trace. \(\square\)

**Lemma 3.2 (identity principle).** A holomorphic function on a connected open set which vanishes on a nonempty open subset is zero throughout the set.

**Proof.** Let \(E\) be the set where the function and all its complex derivatives vanish. The derivatives are continuous, so \(E\) is relatively closed. At any point of \(E\), the disk power series proved in the preceding lesson has every coefficient zero. The function, and hence its derivatives, vanish on that disk; \(E\) is relatively open. The initial open zero set makes \(E\) nonempty. Connectedness forces \(E\) to be the whole domain. The strips used here are connected because they are convex: a separating pair of relatively open sets would separate a segment joining them, contrary to the interval intermediate-value property. \(\square\)

**Corollary 3.3 (zero boundary implies zero function).** A polynomially bounded holomorphic function on \(S^+\) whose upper boundary is zero on a nonempty open subinterval is zero on \(S^+\).

**Proof.** Restrict to that subinterval and put the lower function equal to zero. Theorem 3.1 glues the two sides. The glued holomorphic function vanishes on its lower open half, so Lemma 3.2 makes it zero on the smaller strip. This supplies an open zero set in the original upper strip. Applying the lemma again proves the assertion on the whole upper strip. \(\square\)

## A finite test limit also bounds the growth

We first supply the precise completeness and family estimate used in both growth arguments.

**Finite-support completeness and the family estimate.** For compact \(K\subset I\), let \(E_K^k\) be the complex \(C^k\) functions on \(\mathbb R\) supported in \(K\), with norm \(p_k(\psi)=\max_{0\le j\le k}\|\psi^{(j)}\|_\infty\). This is complete. Indeed, a norm-Cauchy sequence has uniform continuous limits \(g_j\) of its derivatives, all zero outside \(K\). For \(j<k\), pass to the limit in

\[
 \psi_l^{(j)}(x+h)-\psi_l^{(j)}(x)
      =\int_0^h\psi_l^{(j+1)}(x+s)\,ds.
 \tag{F1}
\]

The error is at most \(|h|\) times the uniform derivative error. Dividing the limiting identity by \(h\) and using continuity proves \(g_j'=g_{j+1}\). Thus \(g_0\in E_K^k\), with convergence in the original norm. For \(k=0\), uniform convergence alone proves the assertion. Scalar completeness and the three-term continuity estimate justify the continuous uniform limits, as in the supplied functional foundation.

The smooth space \(E_K^\infty\), with all \(p_r\), is complete for its seminorm metric by the full proof in that same foundation, Sections 14.1–14.2. Suppose a family \((T_a)\) of continuous linear forms on either space is pointwise bounded. The closed sets
\(A_m=\{\psi:\sup_a|T_a\psi|\le m\}\), \(m\ge1\), cover it. Baire's complete-metric theorem, proved in Section 6 of the supplied foundation, gives an interior point and a neighborhood \(p_r(h)<\delta\) whose translate is in some \(A_m\); here \(r=k\) in the finite space. Subtract the value at the interior point to obtain \(|T_a h|\le2m\) on that neighborhood. Rescaling a nonzero test by \(\delta/(2p_r(\psi))\) gives

\[
 |T_a\psi|\le M p_r(\psi),\qquad M=4m/\delta.
 \tag{F2}
\]

The zero test is immediate. The family may be indexed by all positive heights; countability of its index set was never needed. Pointwise limits inherit this bound. If \(T_t\psi\to b(\psi)\) on fixed tests and \(p_r(\psi_t-\psi)\to0\), the same bound gives convergence on the moving tests by splitting off \(T_t(\psi_t-\psi)\).

**Theorem 4.1 (converse growth from \(C^k\) boundary convergence).** Let \(k\ge0\) and let \(f\) be holomorphic on \(S^+\). Assume that
\(L_t(\psi)=\int_I f(x+it)\psi(x)\,dx\) has a limit as \(t\downarrow0\) for every \(\psi\in C_c^k(I)\). Then for each compact interval \(J\Subset I\),

\[
 |f(x+iy)|\le C_Jy^{-k-1},\qquad x\in J,\quad0<y<\gamma/2.
 \tag{4.1}
\]

There is no initial growth hypothesis.

**Proof.** On each \(E_K^k\), every \(L_t\) is continuous, with its fixed-height integral bounded by a multiple of \(p_0\). The assumed limit bounds each fixed pairing near zero. On any remaining closed positive-height interval, continuity of \(f\) on the support rectangle bounds it. Thus (F2) gives, for some \(M\) depending on \(K\),

\[
 |L_t(\psi)|\le M p_k(\psi),\qquad 0<t\le7\gamma/8.
 \tag{4.2}
\]

Here is a direct way to track the exponent. Put \(H=\gamma/2\); choose \(d>0\) so that \(K=J+[-d,d]\Subset I\), and choose \(0<a\le1/2\) with \(aH\le d/2\). Let \(\rho\) be a nonnegative smooth radial function on the plane, supported in the unit disk, with integral one. The included cutoff construction and normalization supply it. For \(\zeta=x_0+iy\), put \(r=ay\) and

\[
 \psi_t(x)=r^{-2}\rho\left(\frac{x-x_0}{r},\frac{t-y}{r}\right).
 \tag{F3}
\]

These smooth probes are supported in \(K\), and vanish unless \(y-r<t<y+r\). That height interval lies in \((0,3\gamma/4)\). Since holomorphic functions are harmonic, the proved radial averaging identity (R5) in the preceding lesson gives
\(f(\zeta)=\int_{y-r}^{y+r}L_t(\psi_t)\,dt\). All integrals here lie compactly inside the upper strip, so ordinary absolute Fubini applies. Set

\[
 B_k=\max_{0\le j\le k}
            \|\partial_s^j\rho\|_\infty(aH)^{k-j}.
\]

Differentiating (F3) in \(x\) and using \(r\le aH\) gives \(p_k(\psi_t)\le B_k r^{-k-2}\). The interval of integration has length \(2r\). Consequently

\[
 |f(\zeta)|\le2M B_k r^{-k-1}
             =2M B_k a^{-k-1}y^{-k-1}.
 \tag{F4}
\]

This proves (4.1) with an explicit constant. Only the family bound on smooth probes was used after (4.2); that observation will be useful below. \(\square\)

### The complete relative Cauchy formula

We retain a second, useful expression for the same estimate. Choose \(\chi\in C_c^\infty(I)\), equal to one near \(J\), and a smooth \(0\le\eta\le1\) equal to one for \(0\le t\le3\gamma/4\) and zero for \(t\ge7\gamma/8\). Let \(d_0>0\) separate \(J\) from \(\operatorname{supp}\chi'\). When that support is empty the term involving it is zero. For \(0<\varepsilon<y/2\), set
\(Q_t^b(\zeta)=L_t(b(x)/(x+it-\zeta))\) wherever the quotient is smooth on its support. The relative Cauchy–Pompeiu theorem in the preceding lesson gives

\[
 \begin{aligned}
 f(\zeta)={}&\frac{1}{2\pi i}Q_\varepsilon^\chi(\zeta)\\
 &-\frac1{2\pi}\int_\varepsilon^{7\gamma/8}
                     \eta(t)Q_t^{\chi'}(\zeta)\,dt\\
 &-\frac{i}{2\pi}\int_{3\gamma/4}^{7\gamma/8}
                     \eta'(t)Q_t^\chi(\zeta)\,dt.
 \end{aligned}
 \tag{4.3}
\]

To check applicability, take the region above height \(\varepsilon\). Multiply \(\chi\eta f\) by a lower cutoff which vanishes below \(\varepsilon/2\) and equals one above \(3\varepsilon/4\). This makes it compactly supported in the ambient upper strip without changing the function or derivatives in the integration region. The lower boundary is oriented toward increasing \(x\). The area derivative is \((\chi'\eta+i\chi\eta')f/2\); the relative formula's minus area term gives exactly the two coefficients in (4.3).

The second quotient is separated horizontally from \(x_0\) by \(d_0\). At \(t=y\) define it as zero near \(x_0\), where \(\chi'\) vanishes. The third is separated vertically by \(\gamma/4\). All their \(C^k\) norms are uniformly bounded, so (4.2) bounds both integrals; the second has an absolutely convergent limit as \(\varepsilon\downarrow0\). The first test converges in \(C^k\) on one support to \(\chi/(x-\zeta)\). Its moving-test pairing tends to \(b(\chi/(x-\zeta))\), where \(b=\lim_{t\downarrow0}L_t\). The derivative formula
\(\partial_x^j(x-\zeta)^{-1}=(-1)^j j!(x-\zeta)^{-j-1}\), proved by induction, and \(|x-\zeta|\ge y\) give

\[
 \left\|\frac{\chi}{x-\zeta}\right\|_{C^k}
                  \le C_{K,k,\gamma}y^{-k-1}.
 \tag{4.4}
\]

The product rule and \(y<\gamma/2\) absorb lower derivatives into the same power. Thus (4.3) also proves (4.1), including both bounded cutoff contributions.

## Smooth boundary measurements supply local growth

**Lemma 5.1 (one common order for the measured family).** Suppose that for every \(\psi\in C_c^\infty(I)\) the limit

\[
 b(\psi)=\lim_{t\downarrow0}L_t(\psi),\qquad
 L_t(\psi)=\int_I f(x+it)\psi(x)\,dx
 \tag{5.1}
\]

exists. Then \(b\) is a distribution, and on every fixed compact interval \(K\Subset I\) there are \(M<\infty\) and an integer \(r\ge0\) with

\[
 |L_t(\psi)|\le M p_r(\psi),\qquad
 p_r(\psi)=\max_{0\le j\le r}\|\psi^{(j)}\|_\infty,
 \qquad0<t\le7\gamma/8.
 \tag{5.2}
\]

The limit inherits the same estimate.

**Proof.** Use the complete smooth space \(E_K^\infty\) in (F2). Fixed-height continuity and pointwise boundedness follow exactly as in Theorem 4.1, now for smooth tests. The selected seminorm degree is a finite \(r\), which can depend on \(K\). Limits preserve linearity and (5.2), so the local estimate defines a distribution as in U008. On moving smooth tests with common support in \(K\),

\[
 |L_t(\psi_t)-b(\psi)|
 \le M p_r(\psi_t-\psi)+|(L_t-b)(\psi)|\longrightarrow0
 \tag{5.3}
\]

whenever \(p_r(\psi_t-\psi)\to0\). The estimate concerns the whole measured family; it makes no claim that \(r\) is the smallest order of the limiting distribution. \(\square\)

**Theorem 5.2 (smooth-test limits and local growth are equivalent).** A holomorphic function on \(S^+\) has all the limits (5.1) if and only if, for every compact interval \(J\Subset I\), there are \(C_J<\infty\) and an integer \(N_J\ge0\) such that

\[
 |f(x+iy)|\le C_Jy^{-N_J},\qquad x\in J,\quad0<y<\gamma/2.
 \tag{5.4}
\]

In the forward direction one may take \(N_J=r+1\), using the family order on a larger support interval.

**Proof.** Lemma 5.1 supplies the common smooth-test bound. The probes (F3) are smooth, so the radial estimate (F4) applies with \(k=r\) and gives the stated exponent. This uses no unasserted convergence on all \(C^r\) tests.

For precise constants in the alternative Cauchy representation, choose \(\chi,\eta,d_0\) as above and define

\[
 \begin{aligned}
 c_{j\ell}(a)&=\binom j\ell\|a^{(j-\ell)}\|_\infty\ell!,\\
 B_r(a,\rho)&=\max_{0\le j\le r}
                         \sum_{\ell=0}^j c_{j\ell}(a)\rho^{-\ell-1}.
 \end{aligned}
 \tag{5.5}
\]

The product rule bounds the second quotient's \(p_r\) norm by \(B_r(\chi',d_0)\), and the third by \(B_r(\chi,\gamma/4)\). Equation (5.3) handles the first moving quotient, whose derivatives of every fixed order converge on its compact support. Thus (4.3) and its limiting form hold under smooth-test convergence alone. With \(H=\gamma/2\), put

\[
 \begin{aligned}
 A&=\max_{0\le j\le r}\sum_{\ell=0}^j c_{j\ell}(\chi)H^{r-\ell},\\
 V_\eta&=\int_{3\gamma/4}^{7\gamma/8}|\eta'(t)|\,dt,\\
 D_1&=\frac{7\gamma M}{16\pi}B_r(\chi',d_0),\\
 D_2&=\frac{M V_\eta}{2\pi}B_r(\chi,\gamma/4),\qquad D=D_1+D_2.
 \end{aligned}
 \tag{5.6}
\]

The second integral has length at most \(7\gamma/8\) and \(|\eta|\le1\), giving \(D_1\); the third gives \(D_2\). Since \(y^{r-\ell}\le H^{r-\ell}\), the first term is bounded by \(MAy^{-r-1}/(2\pi)\). Hence the unchanged full representation gives

\[
 C_J=\frac{MA}{2\pi}+DH^{r+1},\qquad
 |f(x+iy)|\le\frac{MA}{2\pi}y^{-r-1}+D\le C_Jy^{-r-1}.
 \tag{5.7}
\]

Conversely, put any smooth test's support inside the interior of a larger compact interval \(J\Subset I\). Restrict to that horizontal interval and heights less than \(\gamma/2\). Bound (5.4) is the polynomial hypothesis of the preceding finite-test boundary theorem, which supplies its pairing limit. Different choices agree because a scalar limit is unique. Thus the limits exist for every compact smooth test. \(\square\)

**Theorem 5.3 (gluing from measured boundary distributions).** Suppose \(f\) is holomorphic separately on the two sides, and both limits on every compact smooth horizontal test exist, with boundary distributions \(b_+,b_-\). The repeated integral (2.1) defines a canonical distribution on \(S\), equal to \(f\) off the interval, with

\[
 \bar\partial F=\frac{i}{2}(b_+-b_-)\otimes\delta_{y=0}.
 \tag{5.8}
\]

It extends holomorphically across the whole interval exactly when \(b_+=b_-\); that holomorphic extension is unique. A single global exponent or growth constant is not required. A boundary which vanishes on a nonempty open subinterval forces the upper function to be zero throughout \(S^+\).

**Proof.** Apply Theorem 5.2 on the upper side. For the lower side use \(g(z)=f(-z)\) over the reflected interval \(-I\); the substitution \(x\mapsto-x\) takes compact tests to compact tests and transfers the assumed limits. On a fixed enlarged compact interval both sides therefore have bounds with exponents \(N_+,N_-\). With \(H=\gamma/2\), take

\[
 N=\max(N_+,N_-),\qquad
 C=C_+H^{N-N_+}+C_-H^{N-N_-}.
 \tag{5.9}
\]

For \(0<|y|<H\), this gives (1.2) on that interval. Lemma 1.1 and Theorem 2.1 construct the repeated-integral extension on a slightly smaller open interval. Its boundary distributions are \(b_\pm\) there by uniqueness of the same scalar limits.

For any compact test in the whole strip, use one enlarged horizontal interval and a smooth height cutoff equal to one near zero and supported in \((-H,H)\). The near-boundary part has Theorem 2.1's finite-order estimate and absolute outer convergence. The remainder has support away from zero and is an ordinary integral against the smooth \(f\). This constructs (2.1) on every test and proves continuity on every fixed compact support. On overlaps these definitions coincide because they give the same repeated integral; the height cutoff is only an estimate, not part of the definition. The local jump calculation gives (5.8), and away from the interval the source is zero by holomorphy.

If the boundaries match, the proved radial regularity gives a holomorphic representative, as in Theorem 3.1. Conversely a holomorphic extension has equal ordinary traces on each compact interval. Lemma 3.2 proves uniqueness. For a boundary vanishing on a subinterval, glue the upper function to zero below that subinterval and apply the two identity-principle steps of Corollary 3.3. \(\square\)

**Example 5.4 (growth at infinity does not obstruct local gluing).** On the strip over \(\mathbb R\), take \(f(z)=e^z\) on both sides. The boundary pairings are \(\int e^x\psi(x)\,dx\), since convergence is uniform on compact intervals. Each compact interval has a bound with exponent zero. At a fixed nonzero height the modulus \(e^x\) is unbounded, so there is no bound (1.2) uniform in \(x\). Theorem 5.3 still gives the entire extension \(e^z\).

## Exercises

1. **Primitive growth — foundation.** Evaluate \(\int_y^Tt^{-q}\,dt\) for \(q>1\) and \(q=1\). Explain why \(N\) primitives suffice and prove integrability of the final majorant.
2. **Order bounds — intermediate.** State the supplied orders of \(F\), \(f_\pm\) and \(\bar\partial F\). Improve the order for \(z^{-1}\) and compute its planar source.
3. **Unmatched multiples — intermediate.** With \(0\in I\), put \(A/z\) above and \(B/z\) below. Find the source and all pairs \((A,B)\) permitting holomorphic extension through the entire interval.
4. **Cancellation — advanced.** For a test equal to one near zero, show joint absolute divergence for \(z^{-2}\) and finiteness of its repeated pairing. State precisely why absolute Fubini gives no contradiction.
5. **The prescribed norm — advanced.** Give the ball-and-differences argument for (4.2). Explain why smooth-test convergence alone need not select the prescribed degree \(k\).
6. **Local boundary uniqueness — intermediate.** Under polynomial growth, show that a boundary zero on one open subinterval forces the function and boundary to vanish everywhere. Separate the roles of local gluing and connectedness.
7. **Local and global bounds — foundation.** Compute both boundaries of \(e^z\), give its compact-interval bound and disprove every global bound of the form (1.2).
8. **Moving probes — intermediate.** Under Lemma 5.1, prove \(L_t(\psi_t)\to b(\psi)\) when the probes share a compact support and converge in its selected \(p_r\). Explain why a bound for \(b\) alone is insufficient.
9. **Unbounded local pole orders — advanced.** On the two sides of the strip with \(I=\mathbb R\), \(\gamma=1\), set

\[
 f(z)=\sum_{n=1}^\infty 2^{-n}(z-n)^{-n}.
\]

Prove holomorphy away from the positive integers and existence of both distributional boundaries. Show that no fixed polynomial exponent controls every compact horizontal interval. Compute the entire jump and canonical source, with every coefficient, and decide whether the boundaries match.

## Complete solutions

**Solution 1.** For \(q>1\), the integral is \((y^{1-q}-T^{1-q})/(q-1)\), at most \(y^{-(q-1)}/(q-1)\). For \(q=1\) it is \(\log(T/y)\). Each reference-height horizontal integral adds only a compact-interval constant. Starting with positive integer \(N\), after \(N-1\) primitives the exponent is one, and one more primitive gives the logarithm. For \(N=0\) the function is already bounded. The nonnegative double integral in Lemma 1.1 gives \(\int_0^T(1+\log(T/y))\,dy=2T\), proving the required integrability.

**Solution 2.** The supplied upper bounds are \(N\) for \(F\) and \(N+1\) for the two boundary distributions and for \(\bar\partial F\). The last follows either by differentiating the finite-order estimate or from the jump identity and the continuous trace map. These are upper bounds, not assertions of minimal order. For \(z^{-1}\), the preceding lesson proves that the integral of its modulus over a disk of radius \(r\) is \(2\pi r\). Thus its ordinary integral is an order-zero distribution and equals the repeated integral by absolute Fubini. Its jump \(-2\pi i\delta_0\) gives the source \(\pi\delta_{(0,0)}\).

**Solution 3.** The simple-pole formulas in the preceding lesson give
\(f_+=A\operatorname{pv}(1/x)-i\pi A\delta_0\) and
\(f_-=B\operatorname{pv}(1/x)+i\pi B\delta_0\). Hence

\[
 \bar\partial F=\frac{i}{2}(A-B)\operatorname{pv}(1/x)\otimes\delta_{y=0}
                       +\frac\pi2(A+B)\delta_{(0,0)}.
\]

For a zero jump, tests supported in a nonempty subinterval missing zero first force \(A-B=0\), since the ordinary function \(1/x\) there is nonzero. A test equal to one at zero then forces \(A+B=0\). Thus \(A=B=0\), which clearly suffices. Equal nonzero multiples have the same formula on the two sides but still have a pole at the joining interval.

**Solution 4.** Choose the dyadic annuli in Example 2.2 within a disk where the test equals one. Each absolute integral is at least \(3\pi/4\), so their disjoint sum is infinite. On the other hand \(|z|^{-2}\le|y|^{-2}\), and two primitives give the height-integrable bound in (2.3), proving finiteness of the repeated pairing. The absolute version of Fubini requires joint integrability of \(|f\phi|\), which this example violates. We instead apply it to the different, integrable expression \(G\partial_x^2\phi\) after the justified horizontal integrations by parts.

**Solution 5.** In the complete normed space \(E_K^k\), the closed sets \(A_m=\{\psi:\sup_t|L_t\psi|\le m\}\) cover the space. Baire gives a ball \(B(\psi_0,\delta)\subset A_m\). For \(\|h\|<\delta\), both \(\psi_0+h\) and \(\psi_0\) lie in the ball, so \(|L_t h|\le2m\). Apply this to \(h=\delta\psi/(2\|\psi\|)\) for \(\psi\ne0\), giving \(|L_t\psi|\le4m\|\psi\|/\delta\). The norm here is exactly \(p_k\). In the smooth space, an interior neighborhood instead involves one of the increasing seminorms \(p_r\); Baire does not specify \(r=k\). Pointwise convergence on every \(C^k\) test is the extra hypothesis that permits the Banach-space argument with the prescribed degree.

**Solution 6.** On the subinterval with zero boundary, attach the zero lower function. The matching theorem gives a holomorphic function on the smaller full strip; the identity principle makes it zero because its lower half is zero. The original upper function thus has a nonempty open zero set. Connectedness of the full upper strip and a second application of the identity principle give zero everywhere. Its boundary pairings are consequently limits of zero pairings, hence the zero distribution. Local gluing produces the initial open zero set; connectedness propagates it.

**Solution 7.** For each compact test, \(e^{x\pm it}\to e^x\) uniformly on its support, so both boundaries have the stated integral action. For compact \(J\), the choices \(N_J=0\) and \(C_J=e^{\max J}\) prove (5.4). At any fixed \(0<|y|<1\), \(C|y|^{-N}\) is a finite constant while \(|e^{x+iy}|=e^x\to\infty\). Thus a global bound fails, although the extension is the entire exponential, whose power series and derivative are proved in the supplied scalar foundation.

**Solution 8.** Add and subtract \(L_t(\psi)\) to obtain exactly (5.3). Its first term tends to zero by the common family estimate; its second tends to zero by the assumed fixed-probe convergence. A finite-order estimate for \(b\) only controls \(b(\psi_t-\psi)\), not \(L_t(\psi_t-\psi)\) at the current height. The uniform bound for the measured family is therefore essential to this argument.

**Solution 9.** Put \(g_n(z)=2^{-n}(z-n)^{-n}\). On \(|z|\le R\), for \(n\ge2(R+1)\) and fixed \(q\ge0\), repeated differentiation gives

\[
 \begin{aligned}
 P_{n,q}&=n(n+1)\cdots(n+q-1),\\
 |\partial_z^q g_n(z)|
 &\le2^{-n}P_{n,q}(n/2)^{-n-q}
 \le2^q(1+q)^q n^{-n}.
 \end{aligned}
 \tag{5.10}
\]

For \(q=0\), both the empty product and \((1+q)^q\) are one. For \(q>0\), every factor of \(P_{n,q}\) is at most \((1+q)n\), proving the estimate. The majorant is summable because \(n^{-n}\le2^{-n}\) for \(n\ge2\). Hence all differentiated tails converge uniformly on the fixed disk. For each holomorphic summand, \(\partial_x^a\partial_y^b g_n=i^b\partial_z^{a+b}g_n\), by repeated Cauchy–Riemann differentiation, so the same bounds cover every real coordinate derivative. On a compact set avoiding the integers, the finite initial sum is smooth as well. Passing the coordinate fundamental identity (F1) to these uniform limits identifies all derivatives; the Cauchy–Riemann equations pass to the limit. The sum is holomorphic there.

On a bounded horizontal interval, choose \(m\) so large that the tail poles lie outside a closed complex neighborhood of that interval for \(|y|\le1/2\). The same estimate bounds the tail uniformly there. For \(n\le m\) and \(0<|y|<1\),
\(2^{-n}|z-n|^{-n}\le2^{-n}|y|^{-m}\). The finite initial sum and bounded tail therefore give a local polynomial bound. Theorem 5.2, and its lower-side reflection, give both boundaries.

Near a fixed integer \(n\), write \(f(z)=2^{-n}(z-n)^{-n}+h_n(z)\). The remaining finite terms have no pole on a sufficiently small closed disk about \(n\), and the tail and its derivatives converge uniformly there. Thus \(h_n\) is holomorphic and bounded there, say by \(B_n\). For any proposed global exponent \(N<n\),
\(y^N|f(n+iy)|\ge2^{-n}y^{N-n}-B_n y^N\to\infty\). No one exponent works on every compact interval, even with interval-dependent constants.

The higher-pole boundary formula in the preceding lesson gives

\[
 \begin{aligned}
 a_n&=\frac{2^{-n}(-1)^{n-1}}{(n-1)!},\\
 b_+-b_-&=-2\pi i\sum_{n=1}^\infty a_n\delta_n^{(n-1)},\\
 \bar\partial F&=\pi\sum_{n=1}^\infty
                           a_n\partial_x^{n-1}\delta_{(n,0)}.
 \end{aligned}
 \tag{5.11}
\]

Both point-supported sums are locally finite and therefore define distributions: on each compact set only finitely many derivative evaluations remain, giving a finite-order bound. For a compact horizontal test, split off all the finitely many nearby poles. The remaining tail is holomorphic through a neighborhood of its support and has equal upper and lower traces there, so it has zero jump. This proves the first distribution identity without an unjustified exchange of infinite boundary limits. Formula (5.8) supplies the second, with \((i/2)(-2\pi i)=\pi\). A test supported near \(1\), equal to one at that point, detects \(a_1=1/2\), so the jump is nonzero and the two sides do not extend holomorphically through the whole interval.

## Programme proof locations and freely accessible sources

- [Order, positivity and distributional limits](order-positivity-and-limits.md), Proposition 1.2 and Theorem 5.1, and its supplied [functional foundation](../prerequisites/U011-free-foundations/functional-foundations-U008.md), Sections 6 and 14.1–14.2: finite-order extension, Baire and complete smooth support spaces. The finite-\(C^k\) completeness proof is (F1) above. The original lesson is CC0; the selected functional foundation retains CC0 1.0.
- [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Theorem 1.1, the harmonic distribution lemma, Proposition 2.1, Corollary 2.2, Theorem 3.1, Corollary 3.2 and the pole formulas in Section 4: relative Cauchy–Pompeiu, radial averaging (R5), regularity, power series, finite-test boundaries and exact jumps. The lesson is CC0; its three supplied foundational selections retain CC0 1.0.
- Debraj Chakrabarti and Rasul Shafikov, [*Distributional boundary values of holomorphic functions on product domains*, free author preprint, arXiv:1505.01230v1 (2015)](https://arxiv.org/abs/1505.01230v1), Sections 2.3, 2.5 and 2.6: distributional-extension growth, canonical extension and its boundary current. The scaled radial test in Section 2.3 provides a comparison for the growth argument; here the horizontal family bound and the height integral give the precise power \(k+1\). All strip-specific proofs and prerequisites are supplied above or in the exact preceding programme texts.
- Avi Zeff, [*Lecture 12: Pompeiu's formula* (2026)](https://math.berkeley.edu/~avizeff/complex_analysis_S26/lecture_12.html), Section 2. The complete relative identity used here is proved in the preceding Cauchy-kernel lesson; this free lecture supplies the human-source comparison.
