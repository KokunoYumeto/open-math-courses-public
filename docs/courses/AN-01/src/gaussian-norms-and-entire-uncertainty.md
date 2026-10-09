# Gaussian norms and entire uncertainty

*Original edition by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Repaired and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Original exposition: public domain (CC0); supplied prerequisites retain their stated licences.*

Start with a two-variable Gaussian whose coordinates are coupled. Its complex-frequency growth tells us which input direction is narrow, while its whole complex square norm recovers the Gaussian weighted input energy. We then ask which real and imaginary widths an entire function can satisfy, and how a critical direction restricts its dependence on the variables. Finally, separated normalized bumps let us compare a uniform energy bound with the relative curvature of that energy. Theorem D proves the exact norm and its converse; Theorem F proves contour independence, the sharp transformed bound, and the critical and vanishing cases.

We use \(\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)dx\), inverse factor \((2\pi)^{-n}\), \(D=-i\partial\), and complex bilinear distributional pairings.

The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves the Schwartz transform, Gaussian mass, inversion and transpose formulas. Fourier–Laplace slices and boundary poles, Lemma 0.1, proves both completed square-integral Fourier maps and their agreement with ordinary integral transforms. The supplied [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and 16, supplies the convergence, product integration, linear Jacobian, norm, completeness and density proofs. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, and [finite algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.6, supply the calculus and matrix operations.

The analytic-slice lemma, including its averaged weighted-norm converse, is Fourier–Laplace slices and boundary poles, Lemma L, formulas (L1)–(L6). The real symmetric diagonalization and matrix Gaussian transform are [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Section 2 and the real-positive-matrix part of Theorem 3.1. The coordinate Cauchy formula and derivative estimates are [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Corollary 2.2; [Holomorphic boundaries in convex cones](holomorphic-boundaries-in-convex-cones.md), Section 3 and Lemma 3.1, supplies the several-variable power series and identity principle. For the rectangle contours below, Boundary flux and weak identities, Corollary 2.4, proves Green's formula including the corners.

## Matrix roots and the entire Gaussian formula

**Lemma 0.1.** A real symmetric positive definite matrix \(Q\) has a unique real symmetric positive definite square root \(S\). It satisfies \(\det S=\sqrt{\det Q}>0\). Moreover, for every such matrix \(H\) and every \(z\in\mathbb C^n\),
\[
 \begin{gathered}
 \int_{\mathbb R^n}e^{-x^THx/2-ix\cdot z}\,dx\\
 =\frac{(2\pi)^{n/2}}{\sqrt{\det H}}
           e^{-z^TH^{-1}z/2}.
 \end{gathered}
\]
The square in this formula is complex bilinear.

**Proof.** The orthogonal diagonalization proved in U020, Section 2, writes
\(Q=O\operatorname{diag}(\lambda_j)O^T\), with \(O^TO=I\) and all \(\lambda_j>0\). Define
\[
 S=O\operatorname{diag}(\sqrt{\lambda_j})O^T.
\]
Direct multiplication gives \(S^2=Q\), symmetry and positivity. Multiplicativity of the finite determinant gives the asserted positive determinant. If another real symmetric positive definite \(T\) has \(T^2=Q\), then \(TQ=QT\), so \(T\) preserves each eigenspace of \(Q\). Diagonalize its symmetric restriction on each such space by the same theorem. Every eigenvalue there is positive and its square equals the corresponding \(\lambda_j\); it therefore equals \(\sqrt{\lambda_j}\). Thus \(T=S\). The same diagonal construction supplies \(Q^{-1}\) and \(Q^{-1/2}\), and gives \(x^TQx\ge(\min_j\lambda_j)|x|^2\).

For the integral formula, U020, Theorem 3.1, applied to \(B=H/2\) and \(t=1\), gives the displayed constant and exponent for every real \(z\). The positive lower bound just proved shows that, on each compact set of complex \(z\), the integrand and all its complex derivatives are bounded by a polynomial times \(e^{-c|x|^2+C|x|}\) for some \(c>0\). Completing scalar squares and the Gaussian estimates in F3 make these majorants integrable. Dominated difference quotients prove coordinate holomorphy and continuity; U015's polydisk proof gives holomorphy on \(\mathbb C^n\). The right side is also entire. Hold all but the first coordinate real. The difference vanishes on the real axis, so all its real derivatives there are zero. Cauchy–Riemann identifies these with its complex derivatives; its convergent local power series is therefore zero. U015, Lemma 3.1, extends this equality over the connected coordinate plane. Repeat for each coordinate, allowing those already treated to be complex. Equality follows everywhere. At \(z=0\), and after replacing \(H\) by \(2H\), this also proves the full real Gaussian mass \(\pi^{n/2}/\sqrt{\det H}\). \(\square\)

## Measure the energy of a coupled Gaussian

**Worked measurement G1.** Consider two real variables with

\[
\begin{gathered}
Q=\begin{pmatrix}2&1\\1&2\end{pmatrix},\\
Q^{-1}=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\\
f(x)=e^{-x^TQx}.
\end{gathered}
\tag{G1}
\]

The cross term couples the coordinates. The orthogonal coordinates \(t_+=(x_1+x_2)/\sqrt2\) and \(t_-=(x_1-x_2)/\sqrt2\) give \(x^TQx=3t_+^2+t_-^2\). Their Jacobian has absolute value one, and \(\det Q=3\). Thus the input's Gaussian weighted square norm is

\[
\int |f(x)|^2e^{x^TQx}dx=\frac{\pi}{\sqrt3}.
\tag{G2}
\]

Lemma 0.1 gives the entire Gaussian transform

\[
\begin{gathered}
F(z)=\frac{\pi}{\sqrt3}e^{-z^TQ^{-1}z/4},\\
z^TQ^{-1}z=\frac23(z_1^2-z_1z_2+z_2^2).
\end{gathered}
\tag{G3}
\]

All squares here are bilinear complex squares. At imaginary frequencies in the two coupled directions this yields

\[
\begin{aligned}
|F(it,it)|&=\frac{\pi}{\sqrt3}e^{t^2/6},\\
|F(it,-it)|&=\frac{\pi}{\sqrt3}e^{t^2/2}.
\end{aligned}
\tag{G4}
\]

The imaginary growth therefore records the inverse widths of the input. We can also integrate the whole complex output directly. Define \(I_Q(F)=\int |F(\xi+i\eta)|^2e^{-\eta^TQ^{-1}\eta}d\xi d\eta\). Taking the real part of the exponent in (G3) gives

\[
\begin{gathered}
I_Q(F)=\frac{\pi^2}{3}
\left(\int e^{-\xi^TQ^{-1}\xi/2}d\xi\right)\\
\left(\int e^{-\eta^TQ^{-1}\eta/2}d\eta\right)\\
=\frac{\pi^2}{3}(2\pi\sqrt3)^2=4\pi^4.
\end{gathered}
\tag{G5}
\]

The ratio of (G5) to (G2) is \(4\pi^3\sqrt3\). The next theorem explains why this same ratio holds for every eligible input with this \(Q\), and why a finite entire output norm also recovers its input. Exercise 9 lets the width vary until the weighted norm ceases to exist.

## D. An exact Gaussian norm on the entire space

**Theorem D.** Let \(Q\) be real symmetric positive definite and \(n\geq1\). If \(f e^{x^TQx/2}\in L^2(\mathbb R^n)\), its Fourier–Laplace transform is entire and

\[
\begin{gathered}
\int_{\mathbb R^{2n}}\\
|F(\xi+i\eta)|^2e^{-\eta^TQ^{-1}\eta}\,d\xi\,d\eta\\
=\pi^{n/2}(2\pi)^n\sqrt{\det Q}\\
\int_{\mathbb R^n}|f(x)|^2e^{x^TQx}\,dx.
\end{gathered}
\tag{D1}
\]

Every entire function with finite left side is the transform of exactly one such \(f\). Coupled, nondiagonal \(Q\) is included.

**Proof.** Write \(h=f e^{x^TQx/2}\in L^2\). For every real \(\eta\), Cauchy–Schwarz bounds the absolute transform integral by \(\|h\|_2\) times the square root of
\(\int e^{-x^TQx+2\eta\cdot x}dx\).
Completing the actual square with \(Q^{-1}\eta\) shows this integral is finite. Polynomial factors from any complex derivative remain Gaussian integrable, uniformly for \(\eta\) in a compact set. Thus differentiation under the integral proves the entire assertion. Also \(f e^{\eta\cdot x}\in L^2\), because \(2\eta\cdot x-x^TQx\leq\eta^TQ^{-1}\eta\). At every height completed Plancherel therefore applies.

Tonelli and the full real matrix Gaussian integral yield

\[
\begin{gathered}
I=(2\pi)^n\int |f(x)|^2\\
\left(\int e^{-\eta^TQ^{-1}\eta+2\eta\cdot x}d\eta\right)dx,\\
-\eta^TQ^{-1}\eta+2\eta\cdot x\\
=-(\eta-Qx)^TQ^{-1}(\eta-Qx)\\
+x^TQx,\\
\int e^{-(\eta-Qx)^TQ^{-1}(\eta-Qx)}d\eta\\
=\pi^{n/2}\sqrt{\det Q}.
\end{gathered}
\tag{D2}
\]

The Gaussian factor is Lemma 0.1 at zero, with its positive real determinant root and the supplied linear Jacobian. This proves (D1) with every factor intact.

Conversely suppose \(I<\infty\) for an entire \(F\). The averaged part of Lemma L, with positive weight \(e^{-\eta^TQ^{-1}\eta}\), proves the local uniform slice bound. Its first part supplies one common \(f\), with all \(f e^{\eta\cdot x}\in L^2\). The Tonelli calculation (D2) is valid with extended nonnegative values, without presupposing Gaussian integrability of \(f\). Its finite left side forces \(\int |f|^2e^{x^TQx}<\infty\). The forward entire construction for that \(f\) has the same completed transforms on every slice and hence equals the given entire function everywhere. Fourier injectivity on any one slice gives uniqueness. \(\square\)

## F. Contour independence and the strict Gaussian uncertainty bound

**Theorem F.** Let \(u\) be entire on \(\mathbb C^n\), \(n\geq1\), and suppose \(a,b>0\) and

\[
\begin{gathered}
|u(x+iy)|\\
\leq C\exp\left(\frac a2|y|^2-\frac b2|x|^2\right).
\end{gathered}
\tag{F1}
\]

For every \(\zeta=\xi+i\eta\),

\[
\begin{gathered}
U(\zeta)\\
=\int_{\mathbb R^n}e^{-i(x+iy)\cdot\zeta}u(x+iy)\,dx
\end{gathered}
\tag{F2}
\]

is independent of the real vector \(y\), is entire, and obeys

\[
\begin{gathered}
|U(\xi+i\eta)|\\
\leq C(2\pi/b)^{n/2}\\
\exp\left(\frac{|\eta|^2}{2b}-\frac{|\xi|^2}{2a}\right).
\end{gathered}
\tag{F3}
\]

If \(b>a\) then \(u=0\). At \(a=b\) the entire eligible functions are precisely \(c e^{-b z\cdot z/2}\), with \(|c|\leq C\); thus the strict inequality in the vanishing claim cannot be removed.

**Proof.** For each fixed height and frequency, (F1) makes the kernel and all frequency derivatives absolutely integrable. On compact sets of heights and frequencies the same Gaussian majorant, multiplied by a polynomial in \(x\), works for every derivative. Hence (F2) at any fixed height is entire.

To compare two heights, shift one coordinate at a time. In that coordinate use the rectangle with real sides \([-R,R]\) at the two chosen heights; the other coordinates are held on their current real lines plus fixed heights. U011, Corollary 2.4, applies Green's formula to this rectangle, including its four corners. Multiply the entire integrand by a compact smooth cutoff equal to one near the rectangle. Its Cauchy–Riemann derivative is zero inside, so the four oriented side integrals sum to zero. On either vertical side the absolute kernel, integrated over its bounded height segment and over all the other real coordinates, is bounded by
\(C_{y,y',\zeta}e^{-bR^2/2+R|\eta_j|}\).
The other coordinate factors have finite Gaussian integrals, and the height interval is compact. This bound tends to zero. Both horizontal integrals converge absolutely to the full integrals by their Gaussian tails. Fubini and dominated convergence therefore prove equality after this coordinate shift. The finite sequence of coordinate shifts proves independence of the entire real vector \(y\), retaining every vertical face and its orientation.

Taking absolute values, completing the \(x\)-square, and using the real Gaussian mass give

\[
\begin{gathered}
|U(\xi+i\eta)|\\
\leq C(2\pi/b)^{n/2}\\
e^{|\eta|^2/(2b)}e^{a|y|^2/2+y\cdot\xi}.
\end{gathered}
\tag{F4}
\]

The optimizing allowed height is exactly \(y=-\xi/a\). Substitution gives (F3).

For the final assertion form the entire function \(v(z)=e^{b z\cdot z/2}u(z)\), where the square is bilinear. Since \(\operatorname{Re}(z\cdot z)=|x|^2-|y|^2\), (F1) gives

\[
\begin{gathered}
|v(x+iy)|\leq C e^{-(b-a)|y|^2/2}.
\end{gathered}
\tag{F5}
\]

If \(b\geq a\), \(v\) is bounded on all of \(\mathbb C^n\). For each fixed choice of its other coordinates the Cauchy derivative estimate on a circle of radius \(R\) bounds its derivative in that coordinate by \(C/R\); letting \(R\to\infty\) makes the derivative zero. Thus all coordinate derivatives vanish and \(v\) is constant. If \(b>a\), take \(x=0\) and \(y=t e_1\) in (F5), and let \(|t|\to\infty\); that constant is zero. If \(b=a\), any constant with modulus at most \(C\) is allowed, giving exactly the asserted Gaussian family. Its transform is \(c(2\pi/b)^{n/2}e^{-\zeta\cdot\zeta/(2b)}\), which also realizes equality in (F3) when \(a=b\). The positive dimension supplies the imaginary direction used in the strict case. \(\square\)

## Test the coupled directions before choosing a Gaussian

**Worked measurement G2.** Suppose an entire function is required to satisfy \(|u(x+iy)|\leq C e^{y^TAy/2-x^TBx/2}\). For the matrix \(B=Q\) in (G1), compare two possible choices of \(A\).

First take

\[
\begin{gathered}
A=\begin{pmatrix}3&0\\0&5/2\end{pmatrix},\\
e=\frac1{\sqrt2}(1,1)^T,\\
e^TAe=\frac{11}{4},\qquad e^TBe=3.
\end{gathered}
\tag{G6}
\]

Both diagonal entries of \(A\) exceed the corresponding entries of \(B\). Nevertheless the direction \(e\) violates the required quadratic-form inequality. To check that it forces vanishing at every complex point, fix \(z_0=x_0+iy_0\) and substitute \(z=z_0+(r+is)e\) in the proposed bound. Its quadratic terms are \((11/4)s^2/2-3r^2/2\); its remaining terms are linear in \(r,s\), plus a constant. Completing scalar squares absorbs each linear term into \(\varepsilon r^2/2\) or \(\varepsilon s^2/2\), plus a constant. With \(\varepsilon=1/16\), the one-variable restriction has Theorem F's parameters \(a'=45/16\) and \(b'=47/16\). It vanishes by that theorem, so \(u(z_0)=0\). Since the point was arbitrary, the only eligible entire function is zero. Checking diagonal entries alone would miss this obstruction.

Now take

\[
\begin{gathered}
A=B+\begin{pmatrix}1&0\\0&0\end{pmatrix}
=\begin{pmatrix}3&1\\1&2\end{pmatrix},\\
AB-BA=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\end{gathered}
\tag{G7}
\]

Here \(A-B\) is nonnegative, even though the matrices do not commute. The choice \(u(z)=e^{-z^TBz/2}\) works. We can describe precisely what the critical second direction permits. Put \(h(z)=e^{z^TBz/2}u(z)\). The proposed bound is exactly

\[
|h(x+iy)|\leq C e^{y_1^2/2}.
\tag{G8}
\]

For every fixed complex \(z_1\), this is a constant bound as \(z_2\) varies over the whole complex plane. The coordinate Cauchy estimate used in Theorem F makes \(\partial_{z_2}h=0\). Thus every eligible function has the form

\[
\begin{gathered}
u(z)=e^{-z^TBz/2}h_1(z_1),\\
|h_1(r+is)|\leq C e^{s^2/2},
\end{gathered}
\tag{G9}
\]

where \(h_1\) is entire. Conversely every such \(h_1\) gives the stated bound by multiplying the exact Gaussian modulus. For example, every polynomial \(P\) gives \(h_1(w)=P(w)e^{-w^2/4}\): the ratio in (G8) is \(|P(r+is)|e^{-(r^2+s^2)/4}\), which is bounded. This explains how rigidity in one direction can coexist with polynomial freedom in another. Exercise 6 proves the full matrix existence criterion; Exercise 10 rotates the critical direction.

## Compare slice energy with its relative curvature

**Worked measurement G3.** In one dimension fix \(Q=1\), and form two separated Gaussian bumps

\[
\begin{gathered}
f_R(x)=e^{-(x-R)^2}\\
+e^{-(x+R)^2},\qquad R\geq0,\\
W_R=\int |f_R(x)|^2e^{x^2}dx.
\end{gathered}
\tag{G10}
\]

Each fixed \(R\) has finite weighted norm. Expanding the square before completing its three real Gaussian integrals gives

\[
\begin{gathered}
W_R=2\sqrt\pi\bigl(e^{2R^2}+e^{-2R^2}\bigr),\\
g_R=f_R/\sqrt{W_R},\\
\int |g_R|^2e^{x^2}dx=1,\\
F_R(z)=\frac{2\sqrt\pi}{\sqrt{W_R}}\\
e^{-z^2/4}\cos(Rz).
\end{gathered}
\tag{G11}
\]

Indeed the two squared bumps give \(\sqrt\pi e^{2R^2}\) each, the cross term gives \(2\sqrt\pi e^{-2R^2}\), and translation in the transform gives the two factors \(e^{\mp iRz}\). Theorem D and Solution 2 now give the same exact output norm and the same evaluation bound for every \(R\):

\[
\begin{gathered}
I_1(F_R)=2\pi^{3/2},\\
|F_R(\xi+i\eta)|\leq\pi^{1/4}e^{\eta^2/2}.
\end{gathered}
\tag{G12}
\]

To measure variation with height, define \(N_R(\eta)=\int |g_R(x)|^2e^{2\eta x}dx\). Completed Plancherel identifies the horizontal energy as \(\int |F_R(\xi+i\eta)|^2d\xi=2\pi N_R(\eta)\). Write \(E_R=e^{-2R^2}\) and \(V_R=e^{2R^2}+E_R\). Integrating the same three terms with the exponential tilt gives

\[
\begin{gathered}
N_R(\eta)=\frac{e^{\eta^2/2}}{\sqrt2 V_R}\\
\bigl(\cosh(2R\eta)+E_R\bigr),\\
(\log N_R)''(0)=1+\frac{4R^2}{1+E_R}.
\end{gathered}
\tag{G13}
\]

The last expression grows without bound. There is also a uniform bound \(N_R(\eta)\leq e^{\eta^2}\): multiply \(2\eta x-x^2\leq\eta^2\) by \(|g_R(x)|^2e^{x^2}\) and integrate. These bounds concern the size of the energy. Its logarithmic second derivative measures relative change; here \(N_R(0)\) becomes exponentially small as the two bumps separate. Solution 7 identifies that derivative with four times the variance of the tilted input. Exercise 11 carries out the complete calculation for arbitrary fixed widths \(H>Q>0\).

## Exercises

**Exercise 1 (foundation: a coupled Gaussian with its exact norm).** Let \(H,Q\) be real symmetric positive definite matrices with \(H-Q>0\), without assuming they commute. For \(f(x)=e^{-x^THx/2}\), compute its entire transform and both sides of Theorem D's norm identity. Prove the positivity of \(Q^{-1}-H^{-1}\) and the determinant identity needed for an independent output integral.

**Exercise 2 (intermediate: the sharp point-evaluation bound).** Determine the best bound on \(|F(\xi+i\eta)|\) in terms of \(\|f e^{x^TQx/2}\|_2\), and determine all equality inputs for each fixed complex point. Include the exact determinant, exponential and power of pi.

**Exercise 3 (advanced: the reproducing kernel).** Give the Hilbert space in Theorem D its actual output inner product, linear in the first variable. Derive its reproducing kernel \(K_\zeta(z)\) from the weighted input, prove reproduction, and compute the kernel's squared norm. Explain how this recovers Exercise 2's sharp constant.

**Exercise 4 (intermediate: a real coordinate change inside complex space).** Put \(S=Q^{1/2}\) and \(g(t)=f(S^{-1}t)\). Derive the exact transformation laws for the input norm, Fourier transform and complex output norm. Account for both real and complex Jacobians.

**Exercise 5 (intermediate: polynomial Gaussian examples).** Let \(0<b<c<a\) and let \(P\) be any polynomial on \(\mathbb C^n\). Prove that \(u(z)=P(z)e^{-c z\cdot z/2}\) satisfies Theorem F's hypothesis, and compute its entire transformed function by a finite differential operator. What polynomial examples remain when \(a=b=c\)?

**Exercise 6 (advanced: an exact matrix uncertainty criterion).** Let \(A,B\) be real symmetric positive definite matrices. Determine exactly when a nonzero entire \(u\) can satisfy
\[
\begin{gathered}
|u(x+iy)|\leq C\exp\bigl(y^TAy/2-x^TBx/2\bigr).
\end{gathered}
\]
Prove necessity using actual complex lines and absorbed linear terms, as well as sufficiency. Classify every solution when \(A=B\).

**Exercise 7 (advanced: positive curvature without a universal upper bound).** For a nonzero input in Theorem D, prove that the Hessian of \(\log N(\eta)\), where \(N(\eta)=\int |f(x)|^2e^{2\eta\cdot x}dx\), is positive definite. Does the fixed matrix \(Q\) impose any uniform upper bound on that Hessian over all such inputs? Test the one-dimensional two-bump family
\(f_R(x)=e^{-H(x-R)^2/2}+e^{-H(x+R)^2/2}\), with fixed \(H>Q>0\).

**Exercise 8 (foundation: three independently sharp constants).** For fixed \(a\geq b>0\), use scalar Gaussians to show that the prefactor, imaginary growth exponent and real decay exponent in Theorem F's transformed estimate are each sharp. Distinguish sharpness of the individual constants from equality in every part of the estimate simultaneously.

**Exercise 9 (foundation: reach the boundary of the weighted space).** For the coupled matrix \(Q\) in (G1) and \(\kappa>0\), set \(f_\kappa(x)=e^{-\kappa x^TQx/2}\). Determine exactly which \(\kappa\) give a finite input norm in Theorem D. Compute its transform and its whole complex output norm directly, including the coefficient. Explain what happens at \(\kappa=1\) and as \(\kappa\) decreases to one.

**Exercise 10 (intermediate: rotate a critical direction).** Keep \(B=Q\), set \(v=(1,-1)^T/\sqrt2\), and put \(A=B+vv^T\). Classify all entire functions satisfying the matrix bound in Worked measurement G2 in terms of one entire function of \(v^Tz\). Give eligible examples of arbitrarily large polynomial degree, and prove that they retain the full coupled matrix bound.

**Exercise 11 (advanced: normalize separated bumps at arbitrary widths).** Fix \(H>Q>0\) in one dimension, and use the two-bump input from Exercise 7. Compute its Gaussian weighted square norm \(W_R\), the tilted mass \(N_R\) after normalization by \(\sqrt{W_R}\), and the exact horizontal output energy. Derive \((\log N_R)''(0)\) from your closed formula, and compare its growth with the uniform bound on \(N_R(\eta)\).

## Solutions

**Solution 1.** The coupled Gaussian transform, with the positive determinant root, is
\[
\begin{gathered}
F(z)=\frac{(2\pi)^{n/2}}{\sqrt{\det H}}\\
e^{-z^TH^{-1}z/2},\\
\int |f|^2e^{x^TQx}dx=\frac{\pi^{n/2}}{\sqrt{\det(H-Q)}}.
\end{gathered}
\]
Lemma 0.1 proves the first equality on every complex point; its real mass formula with positive matrix \(H-Q\) proves the second. For \(M=Q^{-1/2}HQ^{-1/2}>I\), the proved diagonalization in U020, Section 2, gives eigenvalues of \(M\) greater than one, so \(I-M^{-1}>0\). Therefore
\(Q^{-1}-H^{-1}=Q^{-1/2}(I-M^{-1})Q^{-1/2}>0\).
No commutation of \(H\) and \(Q\) is used. The exact ordered product
\[
\begin{gathered}
Q^{-1}-H^{-1}=Q^{-1}(H-Q)H^{-1}
\end{gathered}
\]
gives \[
\begin{gathered}
\det(Q^{-1}-H^{-1})\\
=\frac{\det(H-Q)}{\det Q\det H}.
\end{gathered}
\]. Since
\(\operatorname{Re}(z^TH^{-1}z)=\xi^TH^{-1}\xi-\eta^TH^{-1}\eta\), separate real Gaussian integrations yield
\[
\begin{gathered}
I_Q(F)=\frac{(2\pi)^n}{\det H}\\
\int e^{-\xi^TH^{-1}\xi}d\xi\\
\int e^{-\eta^T(Q^{-1}-H^{-1})\eta}d\eta\\
=\frac{(2\pi)^n\pi^n\sqrt{\det Q}}{\sqrt{\det(H-Q)}}.
\end{gathered}
\]
This is exactly \(\pi^{n/2}(2\pi)^n\sqrt{\det Q}\) times the computed input norm. The independent integration checks all factors for coupled matrices.

**Solution 2.** Write \(h(x)=f(x)e^{x^TQx/2}\). The transform integral is the inner product of \(h\) with
\(k(x)=e^{-x^TQx/2+i x\cdot\xi+x\cdot\eta}\), using the convention linear in the first variable. Completing the real square gives
\[
\begin{gathered}
\|k\|_2^2=\frac{\pi^{n/2}}{\sqrt{\det Q}}\\
e^{\eta^TQ^{-1}\eta}.
\end{gathered}
\]
Thus Cauchy–Schwarz gives the sharp bound
\[
\begin{gathered}
|F(\xi+i\eta)|\leq\\
\pi^{n/4}(\det Q)^{-1/4}e^{\eta^TQ^{-1}\eta/2}\\
\|f e^{x^TQx/2}\|_2.
\end{gathered}
\]
For completeness, the squared norm decomposition
\(\|h-\langle h,k\rangle k/\|k\|_2^2\|_2^2
=\|h\|_2^2-|\langle h,k\rangle|^2/\|k\|_2^2\)
proves that equality holds exactly when \(h\) is a complex scalar multiple of \(k\). Hence all equality inputs, including the zero input, are
\(f(x)=C e^{-x^TQx+i x\cdot\xi+x\cdot\eta}\).
They satisfy the required weighted integrability for every \(C\), so the best constant is actually attained.

**Solution 3.** Set \(C_Q=\pi^{n/2}(2\pi)^n\sqrt{\det Q}\). The output inner product is \(\langle F,G\rangle_Q=\int F(\xi+i\eta)\overline{G(\xi+i\eta)}e^{-\eta^TQ^{-1}\eta}\,d\xi\,d\eta\), linear in the first variable. It is finite by Cauchy–Schwarz. Multiplication by \(e^{x^TQx/2}\) identifies the weighted input space isometrically with complete \(L^2\); the inverse multiplication is defined on every \(L^2\) function. Theorem D's onto norm identity therefore makes the output space complete as well. Expanding its norm identity for \(f+g,f-g,f+ig,f-ig\) identifies this inner product as
\(\langle F,G\rangle_Q=C_Q\int f(x)\overline{g(x)}e^{x^TQx}dx\).
For fixed \(\zeta\), choose
\(g_\zeta(x)=C_Q^{-1}e^{-x^TQx+i x\cdot\overline\zeta}\).
Its weighted norm is finite, and
\(C_Q\overline{g_\zeta(x)}e^{x^TQx}=e^{-ix\cdot\zeta}\).
Therefore \(\langle F,\widehat{g_\zeta}\rangle_Q=F(\zeta)\), with the integral justified by the bound in Solution 2. The Gaussian transform computes the kernel explicitly:
\[
\begin{gathered}
K_\zeta(z)=\frac1{(2\pi)^n\det Q}\\
\exp\!\left[-\frac14(z-\overline\zeta)^T Q^{-1}(z-\overline\zeta)\right].
\end{gathered}
\]
Reproduction applied to \(K_\zeta\) gives
\[
\begin{gathered}
\|K_\zeta\|_Q^2=K_\zeta(\zeta)\\
=\frac{e^{\eta^TQ^{-1}\eta}}{(2\pi)^n\det Q},\\
\eta=\operatorname{Im}\zeta.
\end{gathered}
\]
The formula also gives \(K_\zeta(z)=\overline{K_z(\zeta)}\) directly. The evaluation inequality \(|F(\zeta)|\leq\|F\|_Q\sqrt{K_\zeta(\zeta)}\), together with \(\|F\|_Q^2=C_Q\|h\|_2^2\), reduces to Solution 2's constant. Equality occurs for scalar multiples of this kernel, precisely the same weighted inputs.

**Solution 4.** The positive symmetric \(S\) satisfies \(Q=S^2\). Substitution \(t=Sx\) gives
\[
\begin{gathered}
\int |f(x)|^2e^{x^TQx}dx\\
=(\det S)^{-1}\int|g(t)|^2e^{|t|^2}dt,\\
F_f(z)=(\det S)^{-1}F_g(S^{-1}z).
\end{gathered}
\]
Here \(S^{-1}\) has no transpose correction because \(S\) is symmetric. Now substitute \(z=Sw\) in the complex output integral. Its real \(2n\)-dimensional Jacobian is \((\det S)^2\), whereas the squared Fourier prefactor is \((\det S)^{-2}\). Also \((\operatorname{Im}z)^TQ^{-1}\operatorname{Im}z=|\operatorname{Im}w|^2\). Thus \(I_Q(F_f)=I_I(F_g)\). The coefficient in Theorem D transforms consistently: \(\sqrt{\det Q}=\det S\) cancels the input factor \((\det S)^{-1}\). Omitting the second real Jacobian would give the wrong coefficient.

**Solution 5.** The ratio of \(|u(x+iy)|\) to Theorem F's proposed majorant is
\[
\begin{gathered}
|P(x+iy)|\\
e^{-(c-b)|x|^2/2-(a-c)|y|^2/2}.
\end{gathered}
\]
Both quadratic coefficients are strictly positive. Every monomial times this real Gaussian is bounded, so a finite sum gives the required constant \(C\). Differentiating the Gaussian transform under its absolutely convergent integral is justified by polynomial Gaussian majorants on compact complex sets. Since \(i\partial_{\zeta_j}e^{-iz\cdot\zeta}=z_j e^{-iz\cdot\zeta}\), its transform is
\[
\begin{gathered}
U(\zeta)=P(i\partial_\zeta)\\
\left[(2\pi/c)^{n/2}e^{-\zeta\cdot\zeta/(2c)}\right].
\end{gathered}
\]
Theorem F gives independence of the chosen real horizontal contour; alternatively its rectangle proof applies to each polynomial Gaussian with the same vanishing side estimates. When \(a=b=c\), the ratio becomes \(|P(z)|\). A bounded entire polynomial is constant, as follows by applying the one-variable Cauchy derivative estimate to each coordinate. Hence exactly the constant-polynomial Gaussians remain, in agreement with the critical classification in Theorem F.

**Solution 6.** A nonzero function exists exactly when \(B\leq A\) as real quadratic forms. If that inequality holds, \(u(z)=e^{-z^TBz/2}\) has modulus
\(e^{-x^TBx/2+y^TBy/2}\), which is bounded by the stated expression with \(C=1\).

Conversely, if \(B\nleq A\), choose a real unit vector \(e\) with \(b_e=e^TBe>a_e=e^TAe>0\). Fix any complex point \(z_0=x_0+iy_0\) and restrict to \(z_0+te\), \(t=r+is\). Its bound has exponent
\[
\begin{gathered}
\tfrac12a_e s^2-\tfrac12b_e r^2\\
+s\,e^TAy_0-r\,e^TBx_0\\
+\tfrac12y_0^TAy_0-\tfrac12x_0^TBx_0.
\end{gathered}
\]
For any \(\varepsilon>0\), completing scalar squares bounds each linear term by \(\varepsilon r^2/2\) or \(\varepsilon s^2/2\), respectively, plus a constant depending on \(z_0,\varepsilon\). Choose \(0<\varepsilon<(b_e-a_e)/2\), also \(\varepsilon<b_e\). The entire one-variable restriction then has a bound with \(a'=a_e+\varepsilon\) and \(b'=b_e-\varepsilon>a'\). The strict part of Theorem F forces that restriction to vanish. In particular \(u(z_0)=0\). Since \(z_0\) was arbitrary, \(u=0\), proving necessity.

If \(A=B\), the entire function \(v(z)=e^{z^TBz/2}u(z)\) is bounded by \(C\) everywhere. With all other coordinates fixed, the one-variable Cauchy estimate makes each coordinate derivative zero. Thus \(v\) is constant, and all solutions are \(u(z)=c e^{-z^TBz/2}\). No classification of all functions for a strict matrix inequality is needed for the existence criterion.

**Solution 7.** The Gaussian weighted hypothesis gives all moments locally uniformly in \(\eta\): for \(\eta\) in a compact set, every polynomial times \(e^{2\eta\cdot x-x^TQx}\) is bounded. Multiplication by the integrable \(|f|^2e^{x^TQx}\) therefore justifies differentiating \(N\) twice. Under the probability measure
\(d\nu_\eta=|f(x)|^2e^{2\eta\cdot x}dx/N(\eta)\), direct quotient differentiation gives
\[
\begin{gathered}
\nabla^2\log N(\eta)=4\bigl(\mathbb E_{\nu_\eta}[xx^T]\\
-\mathbb E_{\nu_\eta}[x]\\
\mathbb E_{\nu_\eta}[x]^T\bigr).
\end{gathered}
\]
For a nonzero real vector \(v\), its quadratic form is \(4\operatorname{Var}_{\nu_\eta}(v\cdot x)\). Zero variance would confine the nonzero input to one affine hyperplane, which has Lebesgue measure zero: choose a nonzero coordinate of \(v\), solve for that coordinate, and use Tonelli, since each section is a singleton of one-dimensional measure zero. This is impossible for a nonzero \(L^2\) function. The Hessian is therefore positive definite at every height.

For the one-dimensional family, each fixed \(R\) has finite Gaussian weighted norm because the tail's quadratic coefficient is \(H-Q>0\). At \(\eta=0\) symmetry gives mean zero. Expanding its square gives two translated Gaussians and the cross term \(2e^{-Hx^2-HR^2}\). The mass is \(2\sqrt{\pi/H}(1+e^{-HR^2})\), and its second moment divided by that mass is
\[
\begin{gathered}
\operatorname{Var}_{\nu_0}(x)\\
=\frac1{2H}+\frac{R^2}{1+e^{-HR^2}}.
\end{gathered}
\]
Thus \((\log N)''(0)=4\operatorname{Var}_{\nu_0}(x)\to\infty\). Rescaling each \(f_R\) to have weighted norm one changes neither \(\nu_0\) nor this Hessian. Even that normalization gives no upper bound depending only on \(Q\).

**Solution 8.** For every \(c\in[b,a]\), the entire function \(u_c(z)=e^{-c z\cdot z/2}\) satisfies the original bound with \(C=1\), and
\[
\begin{gathered}
U_c(\xi+i\eta)=(2\pi/c)^{n/2}\\
e^{-(\xi+i\eta)\cdot(\xi+i\eta)/(2c)},\\
|U_c|=(2\pi/c)^{n/2}e^{|\eta|^2/(2c)-|\xi|^2/(2c)}.
\end{gathered}
\]
For \(c=b\) and \(\xi=\eta=0\), the prefactor is exactly \((2\pi/b)^{n/2}\); it cannot be decreased uniformly. For the same input and \(\xi=0\), arbitrarily large \(|\eta|\) force the imaginary coefficient to be at least \(1/(2b)\), even if an arbitrary finite prefactor is allowed. For \(c=a\) and \(\eta=0\), arbitrarily large real \(|\xi|\) prevent replacing the real decay coefficient \(1/(2a)\) by any larger number, again with any finite prefactor. These are three separate sharpness statements. If \(a=b\), one Gaussian realizes all of them simultaneously; when \(a>b\), the first and third examples have different widths.

**Solution 9.** The weighted square of the input is \(e^{-(\kappa-1)x^TQx}\). It is integrable exactly when \(\kappa>1\). At \(\kappa=1\) it is identically one; for \(0<\kappa<1\) it is at least one everywhere. With the positive real determinant root, the Gaussian transform gives

\[
\begin{gathered}
F_\kappa(z)=\frac{2\pi}{\kappa\sqrt3}\\
e^{-z^TQ^{-1}z/(2\kappa)},\\
\int |f_\kappa|^2e^{x^TQx}dx\\
=\frac{\pi}{(\kappa-1)\sqrt3},\quad \kappa>1.
\end{gathered}
\tag{G14}
\]

Taking the squared modulus of the transform, the output integrand has the constant \(4\pi^2/(3\kappa^2)\) and exponent

\[
\begin{gathered}
-\frac1\kappa\xi^TQ^{-1}\xi\\
-\left(1-\frac1\kappa\right)\eta^TQ^{-1}\eta.
\end{gathered}
\tag{G15}
\]

For \(\kappa>1\) the two real Gaussian masses are \(\pi\kappa\sqrt3\) and \(\pi\kappa\sqrt3/(\kappa-1)\). Their product times the prefactor yields

\[
I_Q(F_\kappa)=\frac{4\pi^4}{\kappa-1}.
\tag{G16}
\]

This equals Theorem D's coefficient \(4\pi^3\sqrt3\) times the input norm in (G14). At \(\kappa=1\) the \(\eta\)-exponent is zero, so the output integral over \(\eta\) is infinite; for \(\kappa<1\) it grows instead of decaying and is also infinite. Tonelli makes these divergence conclusions valid despite the integrable real-frequency factor. As \(\kappa\downarrow1\), both squared norms diverge as \((\kappa-1)^{-1}\) with the exact respective coefficients displayed. This is the boundary of the weighted space, although the individual transforms remain entire for every \(\kappa>0\).

**Solution 10.** Let \(e=(1,1)^T/\sqrt2\), so \(v,e\) are a real orthonormal basis. For \(h(z)=e^{z^TBz/2}u(z)\), multiplying the exact Gaussian modulus turns the proposed bound into

\[
|h(x+iy)|\leq C e^{(v^Ty)^2/2}.
\tag{G17}
\]

The function \(\widetilde h(w,s)=h(wv+se)\) is entire in two complex variables. For fixed \(w\), (G17) bounds it by \(C e^{(\operatorname{Im}w)^2/2}\) for every complex \(s\). The Cauchy derivative estimate makes its derivative in \(s\) zero. Hence \(\widetilde h(w,s)=h_1(w)\) for an entire \(h_1\), and all solutions are exactly

\[
\begin{gathered}
u(z)=e^{-z^TBz/2}h_1(v^Tz),\\
|h_1(r+it)|\leq C e^{t^2/2}.
\end{gathered}
\tag{G18}
\]

Conversely substitution of (G18) gives \(|u(x+iy)|\leq C e^{-x^TBx/2+y^T(B+vv^T)y/2}\), exactly the prescribed bound. If \(h_1(w)=P(w)e^{-w^2/4}\), its ratio to \(e^{t^2/2}\) is \(|P(r+it)|e^{-(r^2+t^2)/4}\), which is bounded for every polynomial. Choosing \(P(w)=w^m\) gives every nonnegative degree \(m\). The construction retains the entire coupled quadratic form and the rotated critical direction.

**Solution 11.** Put \(S=H-Q>0\) and \(E_R=e^{-HR^2}\). The two squared bumps have exponent \(-Sx^2\pm2HRx-HR^2\) after multiplication by the input weight; the cross term is \(2E_Re^{-Sx^2}\). Completing the two translated squares therefore gives

\[
\begin{gathered}
W_R=2\sqrt{\pi/S}\,V_R,\\
V_R=e^{HQ R^2/S}+E_R.
\end{gathered}
\tag{G19}
\]

Let \(g_R=f_R/\sqrt{W_R}\). For the unweighted tilted integral the translated Gaussian masses are \(\sqrt{\pi/H}e^{\eta^2/H\pm2R\eta}\), while the cross term contributes \(2\sqrt{\pi/H}E_Re^{\eta^2/H}\). Division by (G19) gives

\[
\begin{gathered}
N_R(\eta)=\sqrt{S/H}\,
\frac{e^{\eta^2/H}}{V_R}\\
\bigl(\cosh(2R\eta)+E_R\bigr).
\end{gathered}
\tag{G20}
\]

The normalized transform, obtained by translating each Gaussian, is

\[
\begin{gathered}
F_R(z)=\frac{2\sqrt{2\pi/H}}{\sqrt{W_R}}\\
e^{-z^2/(2H)}\cos(Rz),\\
\int |F_R(\xi+i\eta)|^2d\xi\\
=2\pi N_R(\eta).
\end{gathered}
\tag{G21}
\]

The last equality follows from completed Plancherel applied to \(g_Re^{\eta x}\), whose Gaussian tails put it in both \(L^1\) and \(L^2\). Taking the logarithm of (G20), the term \(\eta^2/H\) has second derivative \(2/H\). At zero the first derivative of \(\cosh(2R\eta)+E_R\) vanishes, and its second derivative is \(4R^2\). Thus

\[
\begin{gathered}
(\log N_R)''(0)\\
=\frac2H+\frac{4R^2}{1+E_R}.
\end{gathered}
\tag{G22}
\]

It tends to infinity with \(R\). Nevertheless \(2\eta x-Qx^2\leq\eta^2/Q\), and the normalized weighted norm is one, so \(N_R(\eta)\leq e^{\eta^2/Q}\) for every \(R\). Theorem D also fixes \(I_Q(F_R)=2\pi^{3/2}\sqrt Q\), and Solution 2 fixes the evaluation bound \(|F_R(\xi+i\eta)|\leq\pi^{1/4}Q^{-1/4}e^{\eta^2/(2Q)}\). Normalization preserves the tilted probability measure and its variance; it controls absolute energy while leaving the relative curvature in (G22) unbounded.

## References

- Fourier–Laplace slices and boundary poles, Lemma 0.1 and Lemma L, formulas (L1)–(L6): full square-integral Fourier maps, common input for analytic slices and the averaged weighted-norm argument used in Theorem D's converse.
- [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Section 2 and Theorem 3.1: orthogonal diagonalization and the real matrix Gaussian transform. Lemma 0.1 here supplies the positive square root and the entire-frequency continuation explicitly.
- Supplied [Fourier](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, [integration](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and 16, [scalar](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, and [finite-algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.6, foundations: the exact Gaussian, norm, convergence, Jacobian and elementary matrix proofs. These supplied copies retain their stated licences.
- Boundary flux and weak identities, Corollary 2.4; [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Corollary 2.2; [Holomorphic boundaries in convex cones](holomorphic-boundaries-in-convex-cones.md), Section 3 and Lemma 3.1: rectangle Green, Cauchy derivative and power-series proofs.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, reprint of the second edition (1990), Exercises 7.4.4 and 7.4.6 and answers on page 415. The norm converse, sharp critical cases, coupled measurements and eleven graded exercises here are independently expressed and proved with the programme inputs identified above.
- Aline Bonami, Bruno Demange and Philippe Jaming, [*Hermite functions and uncertainty principles for the Fourier and the windowed Fourier transforms*](https://arxiv.org/abs/math/0102111v1), Proposition 2.1, for polynomial Gaussian Fourier pairs. The matrix density clause of Proposition 3.3 in this pinned version is not part of the comparison made here. Their transform uses frequency \(y\) with kernel \(e^{-2\pi i x\cdot y}\), so our real frequency is \(\xi=2\pi y\). Their real-space decay hypotheses and Theorem F's whole complex-space bound have distinct roles. The worked measurements and transfer problems here are independently derived from the stated Gaussian integral and contour proofs.
- Michael Hitrik and Johannes Sjöstrand, [*Two minicourses on analytic microlocal analysis*](https://arxiv.org/abs/1508.00649v1), Section 1.3, Theorem 1.3.3 and formulas (1.3.23)–(1.3.24): the related Gaussian-weighted unitary transform in the broader quadratic-phase setting. Here Lemma L proves the norm converse directly, and Solution 3 derives the reproducing kernel from the weighted input.
