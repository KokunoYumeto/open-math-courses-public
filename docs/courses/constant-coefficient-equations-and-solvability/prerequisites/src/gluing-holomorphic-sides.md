# Gluing holomorphic sides

*Exposition and proofs: GPT-6 Astra and GPT-6.1 Sol (OpenAI), Ultra. Original lesson exposition: CC0. Linked programme components retain their stated licences.*

This reading proves the repeated-integral distributional extension for polynomial growth, its exact boundary source, matching-boundary holomorphic continuation and one-variable zero-boundary uniqueness. It contains the complete arguments in Sections 1–3, including the example distinguishing repeated integration from absolute integration.

The [Cauchy-kernel reading](cauchy-kernels-and-boundary-limits.md) supplies its finite-test boundary theorem, explicit compact-cutoff regularity and disk power series. [Order, positivity and distributional limits](order-positivity-and-limits.md) supplies finite-order test extension. Pairings are complex linear and \(\bar\partial=(\partial_x+i\partial_y)/2\).

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
 \begin{gathered}
 A_\phi(y)\\
 =(-1)^N\int_I G(x+iy)\partial_x^N\phi(x,y)\,dx.
 \end{gathered}
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

**Proof.** Matching makes the source (2.2) zero. Proposition 2.1 of the linked Cauchy-kernel reading proves, by its explicit kernel and compact-cutoff argument, that a distribution annihilated by \(\bar\partial\) has a holomorphic representative \(h\). Away from height zero, \(h\) and \(f\) give the same distribution. Their difference is continuous and must vanish pointwise: if nonzero at a point, multiplication by a constant phase and integration against a sufficiently small nonnegative bump would give a nonzero pairing. Thus \(h=f\) on both sides. The identity principle below proves uniqueness.

Conversely, if \(h\) is a holomorphic extension, it is smooth by the proved disk theory. For any compact horizontal test, \(h(x\pm iy)\) tends uniformly to \(h(x)\). Both boundary pairings consequently equal its ordinary trace. \(\square\)

**Lemma 3.2 (identity principle).** A holomorphic function on a connected open set which vanishes on a nonempty open subset is zero throughout the set.

**Proof.** Let \(E\) be the set where the function and all its complex derivatives vanish. The derivatives are continuous, so \(E\) is relatively closed. At any point of \(E\), the disk power series proved in the preceding lesson has every coefficient zero. The function, and hence its derivatives, vanish on that disk; \(E\) is relatively open. The initial open zero set makes \(E\) nonempty. Connectedness forces \(E\) to be the whole domain. The strips used here are connected because they are convex: a separating pair of relatively open sets would separate a segment joining them, contrary to the interval intermediate-value property. \(\square\)

<span id="zero-boundary-implies-zero-function"></span>

**Corollary 3.3 (zero boundary implies zero function).** A polynomially bounded holomorphic function on \(S^+\) whose upper boundary is zero on a nonempty open subinterval is zero on \(S^+\).

**Proof.** Restrict to that subinterval and put the lower function equal to zero. Theorem 3.1 glues the two sides. The glued holomorphic function vanishes on its lower open half, so Lemma 3.2 makes it zero on the smaller strip. This supplies an open zero set in the original upper strip. Applying the lemma again proves the assertion on the whole upper strip. \(\square\)

## References

- Debraj Chakrabarti and Rasul Shafikov, *Distributional boundary values of holomorphic functions on product domains*, author preprint, arXiv:1505.01230v1 (2015), §§2.3, 2.5–2.6. [Preprint](https://arxiv.org/abs/1505.01230v1).
- Avi Zeff, *Lecture 12: Pompeiu’s formula* (2026), §2. [Lecture](https://math.berkeley.edu/~avizeff/complex_analysis_S26/lecture_12.html).
