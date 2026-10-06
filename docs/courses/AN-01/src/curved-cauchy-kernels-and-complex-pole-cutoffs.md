# Curved Cauchy kernels and complex pole cutoffs

*Reconstructed by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A singular reciprocal can have a distributional limit even when its absolute integral diverges. The region removed around the singularity is part of the definition. We examine three such regions: a strip around a curve, a circular hole around a pole, and a sublevel set of a holomorphic function. Each limit comes with a finite test-function estimate and its complete differential source.

Write \(z=x+iy\), \(dA=dx\,dy\), and
\[
\partial_z=\tfrac12(\partial_x-i\partial_y),
\qquad \bar\partial=\tfrac12(\partial_x+i\partial_y).
\]
Pairings are complex-linear; tests are never conjugated. The full Cauchy normalization and boundary-limit proofs are [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Corollary 1.2 and Theorem 4.1. We use the proved Taylor and point-jet results in [Angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A2–A3. The holomorphic coordinate and real change-of-variables proofs are [Zero hypersurfaces as curvature measures](zero-hypersurfaces-as-curvature-measures.md), Lemmas 2.1 and 3.0. All remaining proof locations are listed at the end.

The complete [integral Taylor proof](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods) supplies the finite-order remainders used here, including signed increments, complex-valued functions, directional derivatives and uniform bounds for all required derivatives on compact neighborhoods.

## A curve with only one derivative

Let \(B,C\) be real \(C^1\) functions on \(\mathbb R\), and put \(A=B+iC\). Assume

\[
B(x)\ne0\qquad(x\ne0).
\tag{1.1}
\]

This condition excludes zeros of \(A(x)+iy\) on each of the two open half-planes \(x>0\) and \(x<0\).

**Example 1.1 (an insufficient hypothesis).** The weaker requirement \(A(x)\ne0\) for \(x\ne0\) would allow \(A(x)=ix\). Its denominator is \(i(x+y)\). A nonnegative compact smooth test positive near \((1,-1)\) gives two divergent one-sided logarithmic integrals at \(y=-x\), for every \(x\) in a small interval about one. The absolute double integral also diverges, since it bounds below a positive multiple of the integral of \(1/|x+y|\) across that line. Excising \(|x|\leq\varepsilon\) leaves this singularity untouched. An additional principal-value prescription there would be a different definition.

**Theorem 1.1 (the curve limit and its source).** Under (1.1), every compact \(C^1\) test has the well-defined pairing

\[
\begin{aligned}
I_\phi(x)&=\int_{\mathbb R}\frac{\phi(x,y)}{A(x)+iy}\,dy
                    &&(x\ne0),\\
E_\varepsilon(\phi)&=\int_{|x|>\varepsilon}I_\phi(x)\,dx,\\
E_A(\phi)&=\lim_{\varepsilon\downarrow0}E_\varepsilon(\phi)
          =\int_{\mathbb R}I_\phi(x)\,dx.
\end{aligned}
\tag{1.2}
\]

The value of \(I_\phi(0)\) is irrelevant. On smooth tests, \(E_A\) is a distribution of order at most one. The continuous coefficient \(A'(x)\) has a particular multiplier action specified in the proof. With that action define

\[
P_AE_A=\partial_xE_A+i\partial_y(A'E_A).
\tag{1.3}
\]

If \(B(0)\ne0\), this source is zero. If \(B(0)=0\), let \(\sigma_+,\sigma_-\) be the respective signs of \(B\) on the positive and negative half-lines. Then

\[
P_AE_A=\pi(\sigma_+-\sigma_-)\delta_{(0,-C(0))}.
\tag{1.4}
\]

In particular, a real curve has its source at \((0,0)\) when \(A(0)=0\).

**Proof.** Fix \(\operatorname{supp}\phi\subset[-R,R]^2\), \(R>0\), and let
\(T=R+\sup_{|x|\leq R}|C(x)|+1\).
For \(x\ne0\), substitute \(\eta=y+C(x)\) and set
\(b=B(x)\), \(\psi_x(\eta)=\phi(x,\eta-C(x))\).
This test is supported inside \((-T,T)\). Separate its value at zero:
\[
I_\phi(x)=
\psi_x(0)\int_{-T}^T\frac{d\eta}{b+i\eta}
+\int_{-T}^T\frac{\psi_x(\eta)-\psi_x(0)}{b+i\eta}\,d\eta.
\]
The first scalar integral equals
\(2\operatorname{sgn}(b)\arctan(T/|b|)\): multiply by the conjugate denominator; the odd imaginary part integrates to zero and the even real part has the indicated antiderivative.
Its modulus is at most \(\pi\). In the other integral, the fundamental theorem gives
\(|\psi_x(\eta)-\psi_x(0)|\leq|\eta|\|\partial_y\phi\|_\infty\),
and \(|b+i\eta|\geq|\eta|\). Therefore

\[
|I_\phi(x)|\leq\pi\|\phi\|_\infty
                    +2T\|\partial_y\phi\|_\infty.
\tag{1.5}
\]

The function \(I_\phi\) is continuous away from zero by ordinary parameter integration and vanishes for \(|x|>R\). Assign any value at zero. It is a bounded measurable function, so dominated convergence proves (1.2), with

\[
|E_A(\phi)|\leq2\pi R\|\phi\|_\infty
                         +4RT\|\partial_y\phi\|_\infty.
\tag{1.6}
\]

This proves continuity on the stated compact \(C^1\) test spaces. For each positive \(\varepsilon\), \(B\) is bounded away from zero on the part of the compact support with \(|x|\geq\varepsilon\). Thus \(E_\varepsilon\) is the ordinary, absolutely integrable excised double integral. The limit without excision need not be jointly absolutely integrable.

For a continuous function \(m=m(x)\), define

\[
(mE_A)(\phi)=\int_{\mathbb R}m(x)I_\phi(x)\,dx.
\tag{1.7}
\]

Multiplying (1.5) by the local bound of \(|m|\) proves that this is a distribution. This construction is specific to a coefficient depending only on \(x\); it makes no assertion about multiplying an arbitrary distribution by a continuous function. It defines \(A'E_A\), since \(A'\) is continuous. For smooth \(A\) it agrees with the usual multiplication and with the notation \((\partial_x+iA'\partial_y)E_A\).

On a smooth test, (1.3) means exactly

\[
(P_AE_A)(\phi)
=-\int I_{\partial_x\phi}(x)\,dx
  -i\int A'(x)I_{\partial_y\phi}(x)\,dx.
\tag{1.8}
\]

Both integrals converge by (1.5). Off \(x=0\), \(K(x,y)=(A(x)+iy)^{-1}\) is \(C^1\) and
\(\partial_xK=-A'/(A+iy)^2\), \(\partial_yK=-i/(A+iy)^2\).
Thus \(\partial_xK+iA'\partial_yK=0\).
Integrate (1.8) first on \(x>\varepsilon\) and \(x<-\varepsilon\), and integrate the \(y\)-derivative on the whole compact support. Ordinary one-variable integration by parts is sufficient and never differentiates \(A'\) in \(x\). The interior terms cancel. The remaining boundary difference is \(J_\varepsilon^+-J_\varepsilon^-\), where

\[
J_\varepsilon^\pm
=\int_{\mathbb R}
       \frac{\phi(\pm\varepsilon,y)}{A(\pm\varepsilon)+iy}\,dy.
\tag{1.9}
\]

The positive half-strip has a positive contribution from its inner endpoint; the negative half-strip has a negative one.
If \(B(0)\ne0\), the two ordinary integrals have the same limit. Suppose \(B(0)=0\). By continuity and (1.1), each half-line has a constant sign: two opposite signs on the same interval would force a zero by the intermediate value theorem. The boundary limit proved in U013, Theorem 4.1, becomes

\[
\lim_{\substack{b\to0\\\operatorname{sgn}b=\sigma}}
 \int\frac{\psi(\eta)}{b+i\eta}\,d\eta
=\pi\sigma\psi(0)-i\,\operatorname{pv}\int\frac{\psi(\eta)}{\eta}\,d\eta.
\tag{1.10}
\]

The sign follows from \(1/(b+i\eta)=-i/(\eta-ib)\); the principal value uses symmetric excision of zero.
In (1.9) the translated tests
\(\psi_\varepsilon^\pm(\eta)=\phi(\pm\varepsilon,\eta-C(\pm\varepsilon))\)
converge to \(\psi_0(\eta)=\phi(0,\eta-C(0))\) in the \(C^1_\eta\) norm on a common compact support. Uniform continuity of \(\phi,\partial_y\phi\) proves this convergence. Estimate (1.5) bounds the effect of their difference uniformly in \(b\). Consequently one may apply (1.10) to the fixed limiting test on each side. The principal values cancel and the delta terms give exactly (1.4). \(\square\)

**Example 1.2 (crossing and tangency).** The curves \(A=x\), \(A=-x\), and \(A=x^2\) give respective sources \(2\pi\delta_0\), \(-2\pi\delta_0\), and zero.
The flat crossing \(A(x)=\operatorname{sgn}(x)e^{-1/x^2}\), with \(A(0)=0\), also has source \(2\pi\delta_0\). It is smooth and all derivatives vanish at zero. Indeed each derivative on either half-line is a polynomial in \(1/x\) times \(e^{-1/x^2}\), whose limit is zero: the exponential series implies \(e^t\geq t^m/m!\) for every \(m\), and \(t=1/x^2\) dominates any prescribed power. Induction and the fundamental theorem give the smooth extension with zero derivatives. The source is determined by the side signs.

## All circularly cut poles

**Theorem 2.1 (existence, order and normalization).** For every positive integer \(N\), the limit

\[
u_N(\phi)=\lim_{\rho\downarrow0}
               \int_{|z|>\rho}z^{-N}\phi(z)\,dA
\tag{2.1}
\]

exists on every smooth compact test. It extends continuously to compact \(C^{N-1}\) tests, and its exact distributional order is \(N-1\). It restricts to the function \(z^{-N}\) away from zero and obeys

\[
u_N(s\,\cdot)=s^{-N}u_N\quad(s>0),\qquad
u_N(R_\theta\,\cdot)=e^{-iN\theta}u_N,\quad
R_\theta z=e^{i\theta}z.
\tag{2.2}
\]

These two covariance laws uniquely select its extension. Moreover,

\[
u_N=\frac{(-1)^{N-1}}{(N-1)!}\partial_z^{N-1}u_1,
\tag{2.3}
\]

and its complete source is

\[
(\partial_x+i\partial_y)u_N
=\frac{2\pi(-1)^{N-1}}{(N-1)!}\partial_z^{N-1}\delta_0.
\tag{2.4}
\]

The cutoff \(x^2+y^2>\epsilon\) gives exactly the same family, with \(\rho=\sqrt\epsilon\).

**Proof.** At \(N=1\) the kernel is locally integrable, since its polar absolute integral near zero is \(2\pi\int_0^1dr\). For \(N\geq2\), choose a fixed radial smooth compact cutoff \(\chi=1\) near zero and let \(Q\) be the Taylor polynomial of \(\phi\) of degree \(N-2\).
Each monomial \(x^jy^k\) is a linear combination of \(z^p\bar z^q\) with \(p+q=j+k\): insert \(x=(z+\bar z)/2\) and \(y=(z-\bar z)/(2i)\) and expand.
On the circle these terms have frequency \(p-q\), of absolute value at most \(N-2\). Multiplication by \(z^{-N}=r^{-N}e^{-iN\theta}\) leaves a nonzero integer frequency, whose integral is zero because
\(\int_0^{2\pi}e^{il\theta}\,d\theta=(e^{2\pi il}-1)/(il)=0\) for \(l\ne0\).
Thus, for every \(\rho>0\),
\(\int_{|z|>\rho}z^{-N}\chi Q\,dA=0\).

Taylor's integral remainder, proved in A2, bounds
\(|\phi(z)-Q(z)|\leq C_N|z|^{N-1}\|\phi\|_{C^{N-1}}\)
on a small disk. After multiplication by \(r^{-N}\) and the area factor \(r\,dr\,d\theta\), this is an integrable constant times \(dr\,d\theta\). On the remaining fixed compact annulus there is no singularity. It follows that

\[
u_N(\phi)=\int_{\mathbb R^2}z^{-N}(\phi-\chi Q)\,dA,
\tag{2.5}
\]

with a fixed-support \(C^{N-1}\) bound. The same argument works for \(C^{N-1}\) tests, and proves the asserted upper order bound.

For precision, dilation and rotation pullbacks act by
\[
T(s\,\cdot)(\phi)=s^{-2}T(\phi(\,\cdot/s)),\qquad
T(R_\theta\,\cdot)(\phi)=T(\phi\circ R_{-\theta}).
\]
Apply the linear change of variables to the actual cut integrals. Dilation changes the radius to \(\rho/s\) and introduces \(s^{-N}\); rotation leaves the radius unchanged and introduces \(e^{-iN\theta}\). Passing to the limits proves (2.2), including the absence of extra point terms.

Here is a direct proof of sharp order. For \(N\geq2\), suppose the order were at most \(k=N-2\). Choose a smooth test \(\psi\) supported in an annulus \(r_0<|z|<R_0\) with \(c=u_N(\psi)\ne0\). Such a test exists explicitly: take \(\psi=z^N\eta\) with nonzero nonnegative smooth annular \(\eta\), so \(c=\int\eta>0\). For \(0<\varepsilon\leq1\), put
\(\psi_\varepsilon(z)=\varepsilon^k\psi(z/\varepsilon)\).
All derivatives through order \(k\) are uniformly bounded; the supports lie in one fixed disk. Homogeneity gives
\[
u_N(\psi_\varepsilon)=\varepsilon^{k+2-N}c=c.
\]
Choose a decreasing geometric sequence \(\varepsilon_j\) whose closed support annuli are disjoint, for example with ratio smaller than \(r_0/(2R_0)\). Every finite sum of the corresponding tests is smooth, supported in the same disk, and has the same uniform \(C^k\) bound, since at any point at most one summand or its derivatives is nonzero. Its pairing is the number of summands times \(c\), which is unbounded. This contradicts order at most \(k\). Any still smaller order would imply that bound as well. Thus the exact order is \(N-1\). For \(N=1\), nonzero local integrability gives exact order zero.

We next prove uniqueness of the extension. By A3, every distribution supported at zero is a finite sum of independent delta derivatives. The invertible relations between \(\partial_x,\partial_y\) and \(\partial_z,\bar\partial\) give an equivalent independent basis
\(\partial_z^p\bar\partial^q\delta_0\).
Independence can also be tested directly on a cutoff times \(z^p\bar z^q/(p!q!)\): \(\partial_z z=1\), \(\partial_z\bar z=0\), \(\bar\partial z=0\), \(\bar\partial\bar z=1\), so its jet isolates the indicated coefficient.
The pullback definitions and test chain rule give
\[
\begin{aligned}
(\partial_z^p\bar\partial^q\delta_0)(s\,\cdot)
   &=s^{-2-p-q}\partial_z^p\bar\partial^q\delta_0,\\
(\partial_z^p\bar\partial^q\delta_0)(R_\theta\,\cdot)
   &=e^{i(q-p)\theta}\partial_z^p\bar\partial^q\delta_0 .
\end{aligned}
\]
For the rotation identity one may check
\(R_\theta^*(\partial_zT)=e^{-i\theta}\partial_z(R_\theta^*T)\)
and
\(R_\theta^*(\bar\partial T)=e^{i\theta}\bar\partial(R_\theta^*T)\)
on tests, then iterate; \(\delta_0\) itself is invariant under rotations.

The difference of two extensions satisfying (2.2) is supported at zero. Independence of its jets and the dilation law force \(p+q=N-2\) for every nonzero coefficient. For \(N=1\) there are no such indices. Otherwise \(|q-p|\leq N-2\), so no such jet has rotation weight \(-N\). Equality of the required rotation factors for all \(\theta\) is impossible for a nonzero coefficient; for distinct integers \(l,l'\), some \(\theta\) has \(e^{il\theta}\ne e^{il'\theta}\). This proves uniqueness.

Now \(v=\partial_zu_N+Nu_{N+1}\) vanishes off zero by classical differentiation. The same test chain rules make it homogeneous of degree \(-N-1\) and of rotation weight \(-N-1\). A point jet of that degree has \(p+q=N-1\), hence \(|q-p|\leq N-1\); none has the required weight. Thus \(v=0\). Iterating this recurrence proves (2.3).
The exact base identity is \(\bar\partial u_1=\pi\delta_0\), proved in U013, Corollary 1.2. Distributional derivatives commute, as their test derivatives do. Applying \(2\bar\partial\) to (2.3) proves (2.4). \(\square\)

**Example 2.1 (the first source jets).** The first two nontrivial cases are
\[
(\partial_x+i\partial_y)u_2
=-\pi(\partial_x-i\partial_y)\delta_0,\qquad
(\partial_x+i\partial_y)u_3=\pi\partial_z^2\delta_0.
\]
The higher pole produces a derivative of the point mass. Its rotation law is needed to select the extension, in addition to homogeneity.

## A cutoff prescribed by a holomorphic function

**Theorem 3.1 (the modulus cutoff).** Let \(Z\subset\mathbb C\) be connected and open and \(f\) holomorphic on \(Z\), not identically zero. Then

\[
T_f(\phi)=\lim_{\epsilon\downarrow0}
 \int_{\{z\in Z:\,|f(z)|>\epsilon\}}\frac{\phi(z)}{f(z)}\,dA
\tag{3.1}
\]

exists on every smooth compact test, defines a distribution on \(Z\), and satisfies \(fT_f=1\).

**Proof.** The isolated-zero and local-logarithm proof in [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Corollary 1.2, gives
\(f(z)=(z-p)^m g(z)\) near each zero \(p\), with integer \(m\geq1\) and \(g(p)\ne0\).
There are only finitely many zeros in any fixed compact subset of \(Z\): otherwise compactness gives an accumulation point in \(Z\), contradicting the isolated-zero theorem and the connected-domain identity principle.

Shrink the neighborhood so \(|g(z)/g(p)-1|<1/2\). A logarithm of the single nonzero number \(g(p)\), together with the convergent series for \(\log(1+v)\), gives a holomorphic \(\ell\) with \(e^\ell=g\). Define

\[
h(z)=(z-p)e^{\ell(z)/m},\qquad f=h^m,\qquad h'(p)\ne0.
\tag{3.2}
\]

To justify the coordinate, apply U025, Lemma 2.1, to
\(F(t,w)=h(p+t)-w\). Its \(t\)-derivative at zero is nonzero; the full contraction-and-Cauchy proof gives a holomorphic solution \(t=a(w)\) near zero. Let \(k(w)=p+a(w)\). Choose the parameter disk \(W\) small enough that \(k(W)\) lies in the uniqueness disk \(D\) around \(p\), and set \(U=D\cap h^{-1}(W)\), an open neighborhood of \(p\). We may also shrink \(D\) so \(h'\ne0\) there. The identity \(h(k(w))=w\) and uniqueness give \(k(h(z))=z\) for \(z\in U\). In particular \(U=k(W)\); thus \(h:U\to W\) and \(k:W\to U\) are inverse holomorphic coordinates. Differentiating gives \(k'=1/h'(k)\ne0\).

For a test supported compactly within this coordinate neighborhood, the actual cut integral changes exactly to

\[
\begin{aligned}
\int_{|f|>\epsilon}\frac{\phi}{f}\,dA
 &=\int_{|w|>\epsilon^{1/m}} w^{-m}\Psi(w)\,dA_w,\\
\Psi(w)&=\phi(k(w))|k'(w)|^2 .
\end{aligned}
\tag{3.3}
\]

Here the full nonlinear change-of-variables theorem is U025, Lemma 3.0. Its hypotheses hold because both maps are \(C^\infty\). If \(k'=a+ib\), its real derivative matrix is
\(\left(\begin{smallmatrix}a&-b\\b&a\end{smallmatrix}\right)\), so its determinant is \(a^2+b^2=|k'|^2>0\). This proves the displayed density factor.
The transformed test extends smoothly by zero outside the coordinate image: its compact support is contained in that open image, so it already vanishes on a neighborhood of its boundary.
For each positive cutoff all integrals are ordinary integrable ones. Theorem 2.1 gives their limit \(u_m(\Psi)\). On a fixed compact test support, all derivatives of \(k\) and \(|k'|^2\) needed through order \(m-1\) are bounded. Repeated chain and product rules therefore give
\(\|\Psi\|_{C^{m-1}}\leq C\|\phi\|_{C^{m-1}}\), proving a local finite-order bound.

We describe the finite localization explicitly. For a compact support \(K\subset Z\), choose a compact neighborhood \(L\subset Z\) with \(K\) in its interior. It contains finitely many zeros. Around each zero lying in a neighborhood of \(K\), choose disjoint small coordinate patches as above and smooth cutoffs \(\chi_p\), supported in those patches, equal to one near the zero. Such cutoffs are supplied by the scalar foundation, §13.10. The residual test
\(\phi_0=(1-\sum_p\chi_p)\phi\) has compact support away from all zeros; hence \(|f|\) has a positive lower bound on that support. At every \(\epsilon\), the cut pairing of \(\phi\) is the finite sum of the pairings of \(\phi_0\) and \(\chi_p\phi\). The first has an ordinary integral for small \(\epsilon\), and the other limits were just proved. The maximum of their finitely many orders gives a common finite derivative bound on tests supported in \(K\). This proves both the global limit and distributional continuity. Its value is independent of coordinates and cutoffs because every computation is a limit of the same integral (3.1).

Finally, for every compact smooth test,

\[
(fT_f)(\phi)=T_f(f\phi)
=\lim_{\epsilon\downarrow0}\int_{|f|>\epsilon}\phi\,dA
=\int_Z\phi\,dA.
\tag{3.4}
\]

Only finitely many zeros meet the compact support, so their area is zero; dominated convergence proves the last equality. Thus \(fT_f=1\). \(\square\)

**Corollary 3.2 (the full local source).** On a zero patch with inverse \(k\) from (3.2), let \(H_\phi(w)=k'(w)\phi(k(w))\). Then

\[
(\bar\partial T_f)(\phi)
=\frac{\pi}{(m-1)!}\bigl(\partial_w^{m-1}H_\phi\bigr)(0).
\tag{3.5}
\]

Away from the zeros the source is zero. These formulas specify the complete point-jet source, summed over the relevant zeros.

**Proof.** Put \(\Phi=\phi\circ k\). The real chain rule and the Cauchy–Riemann equations give
\(\bar\partial_w\Phi=\overline{k'}(\bar\partial_z\phi)\circ k\).
Multiply by \(k'\) to obtain
\((\bar\partial_z\phi)(k(w))|k'|^2=k'\bar\partial_w\Phi\).
Since \(\bar\partial_wk'=0\), the exact local representation (3.3) gives
\[
(\bar\partial_zT_f)(\phi)
=-u_m(k'\bar\partial_w\Phi)
=(\bar\partial_wu_m)(k'\Phi).
\]
By (2.4),
\(\bar\partial u_m=\pi(-1)^{m-1}\partial_w^{m-1}\delta_0/(m-1)!\).
Its pairing supplies a second factor \((-1)^{m-1}\), leaving (3.5).
The reciprocal \(1/f\) is holomorphic off the zeros, so its classical and weak \(\bar\partial\) vanish there. The preceding equalities hold as distributions on each open patch; a finite smooth localization of any compact test makes them a global equality. No uncomputed boundary source remains. \(\square\)

**Example 3.1 (a simple zero).** If \(f'(p)\ne0\), choose \(m=1\), \(h=f\), so \(k'(0)=1/f'(p)\). On this patch
\[
\bar\partial T_f=\frac{\pi}{f'(p)}\delta_p.
\]
Here \(1/f\) is locally integrable, as (3.3) and the locally integrable \(1/w\) show. For higher zeros, the circular cancellation occurs in the root coordinate and retains its Jacobian.

## Exercises

**Exercise 1 (basic).** Let \(\lambda\in\mathbb R\) and \(A(x)=-x^3+i(\lambda+x^2)\). Define the curve distribution and compute its complete weak flux. Why does \(A'(0)=0\) not force that flux to vanish?

**Solution 1.** Here \(B=-x^3\) is nonzero off zero and \(C=\lambda+x^2\). Theorem 1.1 defines \(E_A\) by its ordinary inner \(y\)-integral and strip limit, with the common compact \(C^1\) bound. The coefficient action (1.7) applies to \(A'=-3x^2+2ix\), so
\[
P_AE_A=\partial_xE_A+
\partial_y\bigl((-3ix^2-2x)E_A\bigr).
\]
The signs are \(\sigma_+=-1\), \(\sigma_-=1\), and \(C(0)=\lambda\). Consequently
\[
P_AE_A=-2\pi\delta_{(0,-\lambda)}.
\]
The coefficient is the difference of the two limiting boundary masses in (1.9). Although the curve derivative vanishes at zero, these side masses do not agree. \(\square\)

**Exercise 2 (basic).** Let \(\chi\) be a compact smooth cutoff equal to one near zero, and put \(\phi(z)=\chi(z)(x+2iy)\). Evaluate
\(((\partial_x+i\partial_y)u_2)(\phi)\).

**Solution 2.** Example 2.1 gives
\(-\pi(\partial_x-i\partial_y)\delta_0\).
Since \(\partial_x\phi(0)=1\) and \(\partial_y\phi(0)=2i\), its pairing is
\[
\pi\bigl(\partial_x\phi(0)-i\partial_y\phi(0)\bigr)
=\pi(1-i(2i))=3\pi.
\]
The sign comes from the delta derivative, with no conjugation of the test. \(\square\)

**Exercise 3 (intermediate).** Set \(B(x)=e^{-1/x^2}\) for \(x\ne0\), \(B(0)=0\), and \(C=0\). Prove that \(E_B\) has zero weak flux and exact order one. Show why its kernel is not jointly locally integrable.

**Solution 3.** Smoothness of \(B\) at zero follows from the exponential estimates in Example 1.2. Its side signs are both positive, so (1.4) gives \(P_BE_B=0\).
For fixed \(a>0\) and \(x\ne0\),
\[
\int_{-a}^a\frac{dy}{\sqrt{B(x)^2+y^2}}
=2\log\frac{a+\sqrt{a^2+B(x)^2}}{B(x)}
=2\operatorname{arsinh}(a/B(x)).
\]
The first equality is checked by differentiating
\(\log(y+\sqrt{y^2+B^2})\) and evaluating the endpoints; the second uses
\(\operatorname{arsinh}t=\log(t+\sqrt{1+t^2})\).
The expression is at least \(2\log(a/B(x))=2/x^2+2\log a\).
Its \(x\)-integral diverges on every neighborhood of zero. Tonelli therefore proves failure of joint local \(L^1\).

For a direct order obstruction, fix \(0<a<1\), choose a smooth \(0\leq\theta\leq1\) supported in \((-a,a)\), equal to one on \([-a/2,a/2]\), and choose smooth
\(0\leq\eta_\delta\leq1\) supported in \((\delta,a)\), equal to one on \([2\delta,a/2]\), for sufficiently small \(\delta>0\). The scalar cutoff construction supplies these functions. Set
\[
\phi_\delta(x,y)=\eta_\delta(x)\theta(y)
       \frac{B(x)+iy}{\sqrt{B(x)^2+y^2}},
\]
and extend by zero outside that positive strip. Each test is smooth, since its support stays away from \(x=0\). All supports lie in one fixed compact rectangle, and \(\|\phi_\delta\|_\infty\leq1\). The pairings are the nonnegative numbers
\[
E_B(\phi_\delta)
=\int\frac{\eta_\delta(x)\theta(y)}
               {\sqrt{B(x)^2+y^2}}\,dx\,dy.
\]
Restricting to \(2\delta\leq x\leq a/2\) and \(|y|\leq a/2\), the preceding lower bound shows that these numbers tend to infinity. Hence no common order-zero estimate exists on that compact test space. The upper bound (1.6) proves exact order one. \(\square\)

**Exercise 4 (intermediate).** Every \(u_2+c\delta_0\), \(c\in\mathbb C\), has the same restriction away from zero and the same dilation degree as \(u_2\). Which choices preserve its rotation law? How does the differential source change?

**Solution 4.** In two dimensions both terms have degree \(-2\). A rotation fixes \(\delta_0\), while it multiplies \(u_2\) by \(e^{-2i\theta}\). At \(\theta=\pi/2\) the required factor is \(-1\), so preserving the law would give \(c=-c\). Thus \(c=0\), which does satisfy the law for all angles.
For arbitrary \(c\),
\[
(\partial_x+i\partial_y)(u_2+c\delta_0)
=-2\pi\partial_z\delta_0+2c\bar\partial\delta_0.
\]
The two first-order jets are independent by the monomial tests in Theorem 2.1. A nonzero added point mass therefore changes the source even though it preserves homogeneity. \(\square\)

**Exercise 5 (intermediate).** On a small disk about zero, let \(f(z)=z^2e^z\). Compute \(\bar\partial T_f\) for the modulus cutoff (3.1) through its inverse coordinate, without replacing that cutoff by a circle in \(z\).

**Solution 5.** Choose \(h(z)=ze^{z/2}\), so \(f=h^2\).
Differentiation gives \(h'(0)=1\), \(h''(0)=1\). For its inverse \(k\), differentiation of \(h(k(w))=w\) once and twice gives
\[
k'(0)=1,\qquad k''(0)=-1.
\]
For \(\Phi=\phi\circ k\), \(\partial_w\Phi=k'(\partial_z\phi)\circ k\); the derivative of the conjugate coordinate under \(\partial_w\) is zero. Hence
\[
\begin{aligned}
(\bar\partial T_f)(\phi)
 &=\pi\,\partial_w(k'\Phi)(0)\\
 &=\pi\bigl(k''(0)\phi(0)+k'(0)^2\partial_z\phi(0)\bigr)\\
 &=\pi\bigl(-\phi(0)+\partial_z\phi(0)\bigr).
\end{aligned}
\]
Equivalently,
\[
\bar\partial T_f=-\pi\delta_0-\pi\partial_z\delta_0.
\]
Theorem 3.1 also gives \(fT_f=1\). Both conclusions concern precisely the integrals with \(|z^2e^z|>\epsilon\), by (3.3). \(\square\)

**Exercise 6 (advanced).** For \(a\in\mathbb C\), work on a disk about zero where \(1-az\ne0\), and let \(f(z)=(z/(1-az))^3\). Find the full source \(\bar\partial T_f\).

**Solution 6.** Let \(h(z)=z/(1-az)\). Its inverse is \(k(w)=w/(1+aw)\) on small disks, as direct substitution verifies. The first derivatives at zero are
\[
k'(0)=1,\qquad k''(0)=-2a,\qquad k'''(0)=6a^2.
\]
For \(\Phi=\phi\circ k\), the complex chain rule gives
\[
\partial_w\Phi=k'(\partial_z\phi)\circ k,\qquad
\partial_w^2\Phi=k''(\partial_z\phi)\circ k
                     +(k')^2(\partial_z^2\phi)\circ k.
\]
The product rule therefore yields
\[
\partial_w^2(k'\Phi)(0)
=6a^2\phi(0)-6a\,\partial_z\phi(0)+\partial_z^2\phi(0).
\]
Multiplication by \(\pi/(3-1)!=\pi/2\) in (3.5), with the delta-derivative signs, gives
\[
\bar\partial T_f
=3\pi a^2\delta_0+3\pi a\partial_z\delta_0
                +\frac{\pi}{2}\partial_z^2\delta_0.
\]
As a check on coefficients, the punctured reciprocal is
\(z^{-3}-3az^{-2}+3a^2z^{-1}-a^3\); applying the circular sources to these terms gives the same displayed coefficients. The inverse-coordinate argument supplies the source for the actual nonlinear cutoff, without assuming that equality away from zero identifies an extension. \(\square\)

**Exercise 7 (advanced).** On \(|z|<1\), set \(h(z)=z/(1-z/3)\), \(f=h^m\), with integer \(m\geq1\). Let \(\chi\) be a real function smooth from the right at zero, smooth on \((0,\infty)\), and compactly supported in \([0,1/16)\), with \(\chi(0)=1\). Form
\[
\phi(z)=|h'(z)|^2h(z)^{m+1}\overline{h(z)}
                              \chi(|h(z)|^2).
\]
Show this is a smooth compact test. Compute its pairing and the leading error in the actual cutoff integral.

**Solution 7.** The inverse coordinate is \(k(w)=w/(1+w/3)\). If \(|w|\leq1/4\), then
\(|k(w)|\leq(1/4)/(1-1/12)=3/11<1\).
Thus the support is compactly contained in the unit disk.
The right-smooth assumption at zero suffices for the composition: for each finite integer \(q\), extend \(\chi\) to negative arguments near zero by its degree-\(q\) Taylor polynomial there. The values of the first \(q\) one-sided derivatives match, so repeated fundamental theorems of calculus make this a \(C^q\) extension. Composing with the nonnegative smooth function \(|h|^2\) shows the original composition is \(C^q\). Since \(q\) is arbitrary it is smooth. At the outer support boundary it is already a smooth function vanishing on one side, so extension by zero causes no boundary defect.

In (3.3), \(|h'(k)|^2|k'|^2=1\). Thus the transformed test is
\(w^{m+1}\bar w\,\chi(|w|^2)\), and multiplication by \(w^{-m}\) leaves
\(|w|^2\chi(|w|^2)\). Polar integration with \(s=|w|^2\) gives exactly
\[
T_f(\phi)=\pi\int_0^\infty s\chi(s)\,ds,\qquad
I_\epsilon(\phi)=\pi\int_{\epsilon^{2/m}}^\infty s\chi(s)\,ds.
\]
Since \(\chi(s)=1+O(s)\) as \(s\downarrow0\),
\[
T_f(\phi)-I_\epsilon(\phi)
=\frac{\pi}{2}\epsilon^{4/m}+O(\epsilon^{6/m}).
\]
The fractional exponent follows from the radius \(\epsilon^{1/m}\) in the root coordinate. The calculation preserves the density Jacobian at every positive cutoff. \(\square\)

**Exercise 8 (advanced).** Let \(a,b\) be nonzero real numbers, \(M(x,y)=(ax,by)\), and \(T_N=u_N\circ M\) in the distributional pullback sense. Put
\[
D_{a,b}=a^{-1}\partial_x+ib^{-1}\partial_y,\qquad
J_{a,b}=\tfrac12(a^{-1}\partial_x-ib^{-1}\partial_y).
\]
For \(E_N=|ab|T_N\), compute \(D_{a,b}E_N\) for every positive integer \(N\), and then for \(a=2,b=-3,N=2\).

**Solution 8.** The exact pullback is
\[
T_N(\phi)=|ab|^{-1}u_N(\phi\circ M^{-1}).
\]
This is continuous on compact smooth tests by the linear chain rule and the corresponding support transformation.
For a general distribution \(T\), this definition gives
\(\partial_x(M^*T)=a\,M^*(\partial_{\Re w}T)\) and
\(\partial_y(M^*T)=b\,M^*(\partial_{\Im w}T)\).
For example, transposing \(\partial_{\Re w}[\phi(M^{-1}w)]=a^{-1}(\partial_x\phi)(M^{-1}w)\) proves the first equality; the second is identical in the other coordinate. Therefore
\(D_{a,b}M^*=M^*(2\bar\partial_w)\) and
\(J_{a,b}M^*=M^*\partial_w\).
Also \(M^*\delta_0=|ab|^{-1}\delta_0\), directly from its test pairing. Applying these identities to the full source (2.4) gives
\[
D_{a,b}E_N
=\frac{2\pi(-1)^{N-1}}{(N-1)!}J_{a,b}^{N-1}\delta_0.
\]
For the specified numbers,
\[
D_{2,-3}=\tfrac12\partial_x-\tfrac i3\partial_y,\qquad
J_{2,-3}=\tfrac14\partial_x+\tfrac i6\partial_y,
\]
and hence
\[
D_{2,-3}E_2=-\frac{\pi}{2}\partial_x\delta_0
                         -\frac{i\pi}{3}\partial_y\delta_0.
\]
The normalizing density factor is \(|ab|=6\). Its absolute value is required; the negative sign of \(b\) already appears in the differential operators. \(\square\)

## Programme proof locations and freely accessible sources

The following complete earlier programme proofs supply the inputs used here. Each foundation file retains its stated license.

- [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Theorem 1.1, Corollary 1.2 and Theorem 4.1: punctured Cauchy–Green calculation, exact planar point source, and the one-dimensional pole limits with a uniform compact \(C^1\) bound.
- [Angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A2–A4: Taylor remainder with derivative bounds, complete shrinking-cutoff proof of finite point jets and their independence, and polar integration.
- [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Corollary 1.2: isolated zero orders, Taylor factorization and the local logarithm of a nonzero holomorphic function.
- [Zero hypersurfaces as curvature measures](zero-hypersurfaces-as-curvature-measures.md), Lemma 2.1 and Lemma 3.0: complete scalar holomorphic implicit-function construction and real nonlinear change of variables. The reciprocal coordinate, density and source transformation are derived explicitly above.
- [Scalar and metric foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13: compactness, intermediate values, scalar calculus, logarithm and trigonometric identities, power series and smooth cutoffs.
- [Integration foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.1: Lebesgue measure, dominated convergence, Tonelli, Fubini and linear substitutions.
- [Finite-dimensional foundations](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §10: matrix inverses and determinants for the real coordinate Jacobians.

Freely accessible human-written mathematical sources:

- Avi Zeff, [*Lecture 12: Pompeiu's formula*](https://math.berkeley.edu/~avizeff/complex_analysis_S26/lecture_12.html), March 6, 2026, §2: the punctured Cauchy–Green calculation and its small-circle normalization. The complete proof and all limiting estimates used here are supplied in U013.
- Semyon Dyatlov, [*Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDE*](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), October 2, 2026 version, §4.4, Theorem 4.19 and Lemma 4.22, pp. 53–54: the shrinking-cutoff and Taylor proof of finite point jets. A2–A3 supply that argument with its full derivative estimates; Theorem 2.1 above proves the covariance, sharp order and pole normalization needed here.
