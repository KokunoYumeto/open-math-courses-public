# Weak solution representations near a characteristic variety

*Original worked examples and complete solutions by GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0 1.0.*

A weak integral can use frequencies which are merely near the characteristic set. The total integral satisfies the differential equation because its moments cancel. The [complete proof](near-variety-representation-formal.md#nv1-the-exact-representation-theorem) constructs such a representation for every local weighted solution on an open convex set. One weight works for every tube radius; the representing density and its norm can depend on the radius.

Use \(D=-i\partial_x\), \(F_v(z)=v(e^{-ix\cdot z})\), ordinary Lebesgue area in one complex variable, and complex-linear distribution pairings. A compact test with weight \(k\) has physical dual weight \(1/\check k\), where \(\check k(\xi)=k(-\xi)\).

## Worked example 1. A disk integral for a double-root solution

Let \(a=1+i/2\), \(P(z)=(z-a)^2\), and take a disk of radius \(0<s<r\) centered at \(a\). Define
\[
U_s^{(0)}(a+w)=\frac1{\pi s^2},\qquad
U_s^{(1)}(a+w)=\frac{2\overline w}{i\pi s^4}
\quad(|w|<s),
\tag{L150.1}
\]
and zero outside that disk. Both are densities on \(N_P(r)\). Expanding the entire exponential uniformly on the closed disk and integrating in polar coordinates gives
\[
\int_{|w|<s}w^j\overline w^{\,l}\,dA(w)
=
\begin{cases}
\pi s^{2j+2}/(j+1),&j=l,\\
0,&j\ne l.
\end{cases}
\tag{L150.2}
\]
For unequal powers the angular integral is zero. For equal powers integrate \(2\pi \rho^{2j+1}\) from zero to \(s\).
Only the constant term survives for \(U_s^{(0)}\). For \(U_s^{(1)}\), only the term \(ixw\) in \(e^{ixw}\) survives. Therefore, for real \(x\),
\[
\int U_s^{(0)}(z)e^{ixz}\,dA(z)=e^{iax},\qquad
\int U_s^{(1)}(z)e^{ixz}\,dA(z)=xe^{iax}.
\tag{L150.3}
\]
Both are exact classical solutions of \((D-a)^2u=0\):
\((D-a)e^{iax}=0\), and \((D-a)(xe^{iax})=-ie^{iax}\).
Almost every \(z\) used by either disk integral satisfies \(P(z)\ne0\). Its individual exponential is not a solution. The cancellation belongs to the integral, not each integrand.

Their unweighted density norms are
\[
\int|U_s^{(0)}|^2\,dA=\frac1{\pi s^2},\qquad
\int|U_s^{(1)}|^2\,dA=\frac2{\pi s^4}.
\tag{L150.4}
\]
The second follows by multiplying \(4/(\pi^2s^8)\) by
\(\int|w|^2\,dA=\pi s^4/2\). For any one finite continuous theorem weight \(\Phi\), its factor \(e^{2\Phi(-z)}\) is bounded above on the closed disk; both weighted norms are finite. As \(s\) shrinks their unweighted norms grow. The theorem promises existence for every radius, not a radius-independent norm bound.

For \(s=1/2\), these norms are \(4/\pi\) and \(32/\pi\). Any choice \(r>1/2\), such as \(r=4/5\), contains this disk strictly.

![The reflected repair tube and an explicit representing disk](figures/reflected-tubes-and-disk-moments.png)

**Figure NV-A.** Left: \(Q(z)=P(-z)\) has its double zero at \(-a=-1-i/2\). The proof cutoff uses inner radius \(r/2\), indicator radius \(3r/4\), convolution radius \(r/8\), and outer tube radius \(r\). It is one inside radius \(5r/8\) and supported inside radius \(7r/8\); the shaded annulus contains its derivative support. Right: reflection sends the tube to the disk centered at \(a\), and the explicit densities above use only its radius-\(1/2\) subdisk. The linear density has a varying complex phase, indicated by arrows at selected points. The arrows are samples; L150.2–L150.3 prove the entire integral. Proof locators: NV23–NV24 and NV40–NV42.

## Worked example 2. Regularize a polynomial without introducing poles

For \(Q(z)=z^2-1\), use \(z=x+iy\) and \(M=(T^2+y^2)^{1/2}\). The exact jet norm is
\[
J_T(z)^2=|z^2-1|^2+4|z|^2M^2+4M^4.
\tag{L150.5}
\]
Here \(Q'=2z\) and \(Q''=2\); their squares contribute \(4|z|^2M^2\) and \(4M^4\). The raw value \(|Q|\) vanishes at \(1,-1\), whereas
\[
J_T(1)^2=J_T(-1)^2=4T^2+4T^4>0.
\tag{L150.6}
\]
Thus \(\log J_T\) has no pole at either root. Using \(\log|Q|\) in the repair weight would instead create a singularity precisely where the cutoff is intended to avoid division.

The defining real polynomial is
\[
A(x,y)=J_T(x+iy)^2
=x^4+(6y^2+4T^2-2)x^2
 +9y^4+(12T^2+2)y^2+4T^4+1.
\tag{L150.7}
\]
Its logarithmic Levi coefficient in one variable is
\[
\mathcal L_{\log J_T}
=\frac18\left(
\frac{A_{xx}+A_{yy}}{A}
-\frac{A_x^2+A_y^2}{A^2}\right).
\tag{L150.8}
\]
The factor \(1/8\) combines the \(1/2\) in \(\log J_T=\frac12\log A\) and the \(1/4\) in the complex Laplacian. The proof controls this perturbation by \(B/M^2\); it need not assert that \(\log J_T\) itself has nonnegative curvature.

Compare this \(M^{-2}\) scale with the available curvature
\((1+y^2)^{-3/4}\). Their ratio is
\[
R_T(y)=\frac{(1+y^2)^{3/4}}{T^2+y^2}
\le2^{3/4}T^{-1/2}.
\tag{L150.9}
\]
For \(T\ge2\), differentiation in \(s=y^2\) shows that its exact maximum is at \(s=3T^2-4\), and
\[
\max_y R_T(y)=
\frac{3^{3/4}}4(T^2-1)^{-1/4}.
\tag{L150.10}
\]
Indeed the logarithmic derivative is
\(3/[4(1+s)]-1/(T^2+s)\), which changes from positive to negative at that value. Increasing \(T\) makes the error uniformly small. This is why the available exponent \(-3/4\), equivalent to decay \(|y|^{-3/2}\), matters: the perturbation decays faster, like \(|y|^{-2}\).

![The nonsingular jet norm and the exact uniform curvature ratio](figures/polynomial-jets-and-curvature-budget.png)

**Figure NV-B.** Left: the exact \(T=2\) jet norm in L150.5 stays positive at both zeros of \(Q\); the raw modulus vanishes there. Right: the dimensionless curves \(\sqrt T R_T(Tq)\), for \(T=2,8,32\), satisfy the proved bound \(2^{3/4}\). The marked maxima use the exact values in L150.10. These are exact scalar comparison curves, not numerical evidence that any displayed \(T\) is sufficient for an arbitrary polynomial or theorem weight. Its sufficient \(T\) depends on the actual constants \(B,c\). Proof locators: NV8–NV11 and NV20–NV21.

## Worked example 3. A compact transpose multiple pairs to zero

Keep \(P(z)=(z-a)^2\), \(Q(z)=(z+a)^2\), and let
\[
v_2=Q(D)\delta_0,\qquad F_{v_2}(z)=(z+a)^2.
\tag{L150.11}
\]
The entire quotient by \(Q\) is one. Its compact inverse is \(a_0=\delta_0\), supported at zero. For \(u(x)=(1+x)e^{iax}\), direct differentiation gives
\[
u(0)=1,\quad u'(0)=1+ia,\quad
u''(0)=2ia-a^2.
\tag{L150.12}
\]
With complex-linear distribution pairings,
\((D\delta_0)(u)=iu'(0)\) and
\((D^2\delta_0)(u)=-u''(0)\). Hence
\[
v_2(u)=-u''(0)+2aiu'(0)+a^2u(0)=0.
\tag{L150.13}
\]
This is an ordinary smooth example of the transpose identity
\((P(-D)a_0)(u)=a_0(P(D)u)\). The general solution \(u\) in the theorem may be nonsmooth; the proof therefore uses the compact inverse convolved with a smooth mollifier, pairs only ordinary test functions with \(u\), and passes in a fixed weighted support stage. The example does not replace that limiting argument.

## Worked example 4. Complex characteristic growth yields local regularity

On \(\mathbb R^2\), let \(P(z)=z_1^2+z_2^2\), \(k_1=1\), and
\[
k_s(\xi)=(1+|\xi|^2)^{s/2},\qquad s\ge0.
\tag{L150.14}
\]
This is a shift weight, since
\(\sqrt{1+|\xi+h|^2}\le\sqrt{1+|\xi|^2}+|h|
\le(1+|h|)\sqrt{1+|\xi|^2}\).
Writing \(z=\xi+i\eta\), the characteristic equation is exactly
\[
|\xi|^2=|\eta|^2,\qquad \xi\cdot\eta=0.
\tag{L150.15}
\]
Thus on \(Z_P\),
\[
k_s(\xi)=(1+|\eta|^2)^{s/2}
\le(1+|\eta|)^s.
\tag{L150.16}
\]
Corollary NV10 proves that every local \(L^2\) harmonic function on an arbitrary open set belongs to every local \(B_{2,k_s}\). This gives all these Sobolev regularities from the characteristic bound, with no global convexity assumption.

For \(z\in N_P(1)\), choose \(\theta\in Z_P\) with \(|z-\theta|<1\).
Then
\(|\operatorname{Re}z|\le|\operatorname{Re}\theta|+1
=|\operatorname{Im}\theta|+1\le|\operatorname{Im}z|+2\).
Consequently
\[
k_s(\operatorname{Re}z)
\le 3^s(1+|\operatorname{Im}z|)^s.
\tag{L150.17}
\]
We used \(\sqrt{1+t^2}\le1+t\) and
\(3+t\le3(1+t)\). The constant \(3^s\) is valid for this example; it is not a sharp or universal constant for all operators.

## Exercises with complete solutions

**Exercise 1 (basic: reflected dual).** Let
\(k(\xi)=(1+\max(\xi,0))^2\). Write the physical dual weight of \(E_k\). Then find the test weight which has physical dual weight \(k\).

**Solution 1.** Reflection gives
\(\check k(\xi)=(1+\max(-\xi,0))^2\); the physical dual is
\(1/\check k(\xi)\). To have physical dual \(k\), take
\(b(\xi)=1/k(-\xi)=1/\check k(\xi)\), since
\(1/\check b(\xi)=k(\xi)\). Replacing either reflection by \(k(\xi)\) gives a different nonsymmetric weight and is incorrect. For instance the two reciprocal candidates differ at \(\xi=1\), with values \(1\) and \(1/4\).

**Exercise 2 (basic: no characteristic points).** Treat \(P\equiv3\) and \(P\equiv0\) in the representation theorem.

**Solution 2.** For \(P\equiv3\), \(3u=0\) implies \(u=0\). The zero set and every tube are empty, so the zero density on the empty tube gives both identities and finite norm zero. For \(P\equiv0\), every point is characteristic and every tube is all complex space. L149 PW11 gives the unrestricted weak representation. Neither case requires polynomial jets of a positive degree or division by zero.

**Exercise 3 (basic: exact cutoff radii).** Explain why convolution of \(\mathbf1_{N_Q(3r/4)}\) with a kernel supported in the radius-\(r/8\) ball is one on \(N_Q(5r/8)\) and supported in the closed distance-\(7r/8\) tube. Locate its derivative support.

**Solution 3.** If \(\operatorname{dist}(z,Z_Q)<5r/8\), each kernel displacement has distance from \(Z_Q\) less than \(5r/8+r/8=3r/4\), so every sampled indicator value is one. If the convolution is nonzero, some sampled point is within \(3r/4\) of \(Z_Q\), so the distance of \(z\) is less than \(3r/4+r/8=7r/8\); closure gives the stated support. The derivative vanishes where the smooth function is identically one and where it is identically zero. Its support is therefore contained in
\(5r/8\le\operatorname{dist}(z,Z_Q)\le7r/8\), which lies outside \(N_Q(r/2)\) and inside \(N_Q(r)\).

**Exercise 4 (intermediate: closed repair data).** For
\(f=(F/Q)\bar\partial\chi\), prove its closedness without multiplying a pole by a distribution at a zero of \(Q\).

**Solution 4.** On a whole neighborhood of the zero set, \(\bar\partial\chi=0\); define \(f=0\) there. Off the zero set \(F/Q\) is an ordinary holomorphic function. Thus \(f\) is globally smooth and, off the zeros,
\(\bar\partial f=\bar\partial(F/Q)\wedge\bar\partial\chi+(F/Q)\bar\partial^2\chi=0\).
The same identity holds in the open neighborhood where \(f=0\). These open sets cover space, so closedness holds globally and distributionally.

**Exercise 5 (intermediate: jet derivatives and the quarter factor).** Derive L150.8 from \(A=J_T^2\) and explain why ignoring the \(y\)-dependence of \(M_T\) gives the wrong derivative.

**Solution 5.** Ordinary differentiation gives
\((\log A)_{xx}=A_{xx}/A-A_x^2/A^2\), and the same formula in \(y\). Multiply their sum by \(1/2\), because \(\log J_T=(1/2)\log A\), and by \(1/4\), because
\(\partial_z\bar\partial_z=(\partial_x^2+\partial_y^2)/4\). This is L150.8. In L150.5 both \(M_T^2=T^2+y^2\) and \(M_T^4=(T^2+y^2)^2\) vary with \(y\); differentiating them contributes the additional terms in the explicit polynomial L150.7. Keeping them constant would omit those terms, and therefore change \(A_y,A_{yy}\) and the Levi coefficient.

**Exercise 6 (intermediate: a uniform curvature budget).** Suppose an already established perturbation Hessian bound is \(M_T^{-2}\), and the available Levi constant is \(c=1/18\) times \((1+|\eta|^2)^{-3/4}\). Prove that \(T=4096\) leaves at least half the available curvature.

**Solution 6.** NV20 bounds the ratio by
\(2^{3/4}/\sqrt T=2^{3/4}/64<1/36\). To verify the strict inequality exactly, \(36\,2^{3/4}<64\); raising positive quantities to the fourth power reduces this to
\(36^4\cdot8<64^4\), namely \(13{,}436{,}928<16{,}777{,}216\).
Thus the perturbation norm is at most
\((1/36)(1+|\eta|^2)^{-3/4}\). Subtracting it from the available \(1/18\) leaves \(1/36=c/2\). This exercise assumes its stated error constant one; it does not infer that constant for every polynomial.

**Exercise 7 (advanced: legitimate annihilation).** Why does an entire quotient \(F_{v_2}/P(-z)\) not yet justify the identity \(u(v_2)=0\)? Complete the justification.

**Solution 7.** Its entire extension must have the growth of a compact distribution with carrier inside \(X\). The verified transform \(F_{v_2}\) already has compact carrier in a convex compact \(K_{j+1}\Subset X\). L122 CF3.2 gives the same carrier growth for the entire quotient, and CF2.1 supplies \(a_j\) supported in that carrier with \(P(-D)a_j=v_2\). Smooth \(a_j\) by a compact nonnegative mollifier. Its small-radius convolutions are ordinary tests supported in one compact subset of \(X\), so the equation pairs to zero with their transposes. The transposes are \(v_2*\rho_\varepsilon\), whose transforms converge to \(F_{v_2}\) in weighted \(L^2\) by dominated convergence. Fixed-stage continuity passes their zero pairings to \(u(v_2)=0\). No direct action of a nonsmooth \(u\) on \(a_j\) was used.

**Exercise 8 (advanced: the decreasing weight integrals).** In NV38 the weights \(\Phi_j\) increase. Supply a valid limiting argument and the needed integrable majorant.

**Solution 8.** The integrands decrease to
\(|F_v|^2e^{-2\Phi}\mathbf1_{N_Q(r)}\). Choose \(j_0\) with a compact convex carrier \(L\) of \(v\) and \(L+\rho\overline B\subset K_{j_0}\). The seed lower bound gives
\(e^{-2\phi_{j_0}}\le C e^{-2H_L-2\rho|\eta|}k(\xi)^2\).
The extra factor in \(e^{-2\Phi_{j_0}}\) is \(M_T^{2m+2}\). Multiply the integrable complex-volume expression of L148 CF17 by
\(e^{-2\rho|\eta|}M_T^{2m+2}(1+|\eta|^2)^{N+2n}\), which is bounded. This proves that the \(j_0\) integrand is integrable and dominates all later ones. Dominated convergence now passes NV38 to NV39. Simply applying increasing monotone convergence to these decreasing integrands would be incorrect.

**Exercise 9 (advanced: arbitrary open sets).** Explain why the weight-transfer corollary does not require global convexity of \(X\).

**Solution 9.** Every point of an open set lies in a convex ball whose closure is inside the set. Restrict the equation and the initial local weighted membership to each such ball, and use the convex representation proof there. For any fixed smooth compact cutoff on \(X\), cover its support by finitely many of these balls and take a finite smooth subordinate partition. Multiplication by each partitioned cutoff produces a global \(B_{2,k}\) distribution by the local result on its ball. Their finite sum is the original cutoff times \(u\), and remains in the Banach space. This is exactly the definition of \(B_{2,k}^{\mathrm{loc}}(X)\).

**Exercise 10 (advanced: exact complex moments).** Find a disk density representing \(x^2e^{iax}\), and compute its unweighted square norm. Which operator annihilates this function?

**Solution 10.** For a radius-\(s\) disk, use
\[
U_s^{(2)}(a+w)=-\frac{6\overline w^{\,2}}{\pi s^6}.
\tag{L150.18}
\]
Only the quadratic term \((ixw)^2/2=-x^2w^2/2\) survives L150.2. Multiplication by the density and by the moment \(\pi s^6/3\) gives exactly \(x^2e^{iax}\). Its square norm is
\[
\frac{36}{\pi^2s^{12}}\int_{|w|<s}|w|^4\,dA
=\frac{12}{\pi s^6}.
\tag{L150.19}
\]
Each application of \(D-a\) lowers the polynomial degree by one and multiplies its ordinary derivative by \(-i\). Thus \((D-a)^3\) annihilates the function, whereas
\((D-a)^2(x^2e^{iax})=-2e^{iax}\ne0\). This is a triple-root example, distinct from the double-root solution in Example 1.

## Reproducibility and source map

The formal proof supplies the exact tube representation of Hörmander II, Theorem 15.3.1, and the complex characteristic-weight transfer of Corollary 15.3.2, printed pp. 287–291. Its NV2–NV4 prove the variable-scale polynomial correction and the nonsmooth strict existence estimate. NV7 verifies the compact weighted support needed for the pairing; NV8 constructs the density. NV10 proves the transfer and local patch argument.

The accompanying figure source retains exact centers, radii, phases, jet formula, curvature ratios and analytic maximum coordinates. The independent checks integrate the actual disk exponentials and their density norms and differentiate the physical jet norm in real coordinates; they supplement the proof. The separate real regularity equivalence exercise, surface-area representation and remaining course proofs keep their own scope.
