# Missing boundary rank produces a causal solution

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A boundary matrix that misses one decaying normal mode at every admissible frequency leaves a nonzero causal solution with homogeneous boundary data. We construct that solution from cofactors, prove its full cone support, and show that its support reaches the corner. Tangential smoothing then produces a nonzero smooth solution with zero initial and boundary data.

Read [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md), [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md), [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies the Schwartz Fourier transform; [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html) supplies finite algebra and matrices; Boundary flux and weak identities supplies the complex Green identity.

The homogeneous real-root hyperbolic polynomial component is an open convex cone, every direction in it is hyperbolic, and its imaginary tube is zero-free; [Real roots and their convex component](../AN02-L192.html#4-pass-to-multiple-roots-and-obtain-convexity), Theorem 4.1, gives the full proof. The remaining analytic-order prerequisite is planned in [Distributions, kernels and analytic singularities](../prerequisites/planned-foundation-proofs.html): a holomorphic germ of \(z\)-axis order \(d\), whose local zeros for a real parameter \(r\) satisfy \(\operatorname{Im}z\le C|r|\), has total Taylor order at least \(d\). Their full contracts are stated in [Hyperbolicity and lower order terms](hyperbolicity-and-lower-order-terms.md). Only the analytic-order uses remain conditional on the planned proof.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's treatment of constant-coefficient equations. The linked prerequisite lessons supply the proofs used below.

## Statement and support convention

Normalize the barrier to one and choose dual coordinates as in [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md), so the time and boundary normals are \(N=e_n\), \(\theta=e_1\). Write \(x=(a,x')\), \(a=x_1\), \(\zeta=(\zeta_1,\zeta')\), and
\[
\begin{gathered}
H=\{x_n\ge0\},\\
\qquad H'=\{a\ge0\},\\
\qquad
 C=\Gamma(P_m,N)^*,\\
\qquad h=m_+.
\end{gathered}
\tag{1}
\]
The upper factor \(P_+(w,\zeta)\) is defined in
\(\mathcal T=\mathbb R^n+i(N-\Gamma)\).
For given polynomial boundary symbols \(B_1,\ldots,B_\mu\), form the \(\mu\)-by-\(h\) matrix in [equation 5 in Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md). Assume
\[
 \operatorname{rank}M(\zeta)<h
       \quad\text{for every }\zeta\in\mathcal T.
 \tag{2}
\]
This forces \(h\ge1\); rank is never strictly less than zero.

**Theorem.** There is a family \(a\mapsto u_a\in\mathcal D'(\mathbb R^{n-1})\), smooth for \(a\ge0\) with every one-sided derivative, such that the associated distribution on the interior of \(H'\) satisfies
\[
\begin{gathered}
P(D)u=0,\\
\qquad B_j(D)u|_{a=0}=0
       \\
\quad(1\le j\le\mu),\\
\qquad
 0\in\operatorname{supp}u\subset H'\cap C .
\end{gathered}
\tag{3}
\]
Here the support is the closure of its interior distributional support, as in the theorem statement. Traces are those of the distribution-valued smooth family. In particular the constructed solution is nonzero.

## Augmenting a deficient matrix

Let \(r<h\) be the largest rank attained by the original matrix. Choose a point where that rank occurs and \(r\) original rows independent there. At this point the \(h\) rows supplied by the polynomial symbols \(1,\xi_1,\ldots,\xi_1^{h-1}\) form a basis: their normal polynomials are \(1,\zeta_1+w,\ldots,(\zeta_1+w)^{h-1}\), whose remainders form a triangular change of the standard monomial basis. [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md)'s pairing is nondegenerate.

Add enough of these fixed polynomial boundary symbols to obtain \(h-1\) rows, denoted \(C_1,\ldots,C_{h-1}\), independent at the chosen point. The first \(r\) are the selected original rows. At every parameter where those \(r\) remain independent, all original rows lie in their span, since the original matrix has rank at most \(r\). Thus for every original \(B_j\),
\[
 L(C_1,\ldots,C_{h-1},B_j;P_+)=0.
 \tag{4}
\]
These determinant functions are analytic on the connected tube. They vanish on a nonempty open parameter neighborhood and therefore identically, by the analytic identity principle. The augmented rows themselves have rank \(h-1\) on a nonempty open dense subset: at least one of their \((h-1)\)-minors is a nonzero analytic function, whose zero set has empty interior. At \(h=1\), the augmented list is empty and has rank zero everywhere.

Write their matrix entries as \(\beta_\zeta(C_j(\zeta+w e_1),w^{k-1})\), \(1\le k\le h\). Let \(A_{\widehat k}(\zeta)\) be the augmented \((h-1)\)-row matrix with column \(k\) removed. Let \(c_k(\zeta)\) be the signed cofactor for that column when a final row is appended, and put
\[
\begin{gathered}
K(w,\zeta)=\sum_{k=1}^h c_k(\zeta)w^{k-1},
 \\
\qquad
 c_k=(-1)^{h+k}
     \det A_{\widehat k}(\zeta).
\end{gathered}
\tag{5}
\]
For \(h=1\), \(K=1\). The coefficients are analytic and polynomial expressions in the upper-factor and boundary-symbol coefficients. Expanding a determinant along its final row gives, for every polynomial \(b\),
\[
\begin{gathered}
\beta_\zeta(b,K)\\
= L(C_1(\zeta+\cdot\,e_1),\ldots,
                   \\
C_{h-1}(\zeta+\cdot\,e_1),b;P_+).
\end{gathered}
\tag{6}
\]
It follows that \(K\) is not identically zero: at any point of augmented rank \(h-1\), a cofactor is nonzero. Nondegeneracy of [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md)'s pairing then makes the functional of \(b\) in 6 nonzero. No division by a potentially vanishing minor has been made.

The cofactor polynomial is covariant under real normal translation:
\[
\begin{gathered}
K(w,\zeta+c e_1)=K(w+c,\zeta)
       \\
\quad(c\in\mathbb R).
\end{gathered}
\tag{7}
\]
To prove it, translate the full determinant in 6 and substitute \(y=w+c\) in its pairing. The simultaneous boundary-symbol translation changes the monomial columns by a triangular matrix with determinant one. The two resulting pairings agree for every \(b\). Nondegeneracy makes their polynomial representatives of degree below \(h\) equal, giving 7. Differentiation gives its complex differential identity on each tube fiber, exactly as in [equation 2 in Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)–[equation 3 in Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md).

In particular \(K(w,(0,\zeta'))\) is not identically zero on the intersection tube
\[
 \Omega_\cap=\{\zeta':(0,\operatorname{Im}\zeta')\in-\Gamma\}.
 \tag{8}
\]
If it were zero there, 7 would give zero at every real first coordinate over this open set. Holomorphy in the first coordinate extends that equality to a full parameter neighborhood, and the identity principle would make \(K\) zero on all of \(\mathcal T\), a contradiction.

## The normal contour solution

For \(a\ge0\), \(\zeta'\in\Omega_\cap\), define
\[
\begin{gathered}
U(a,\zeta')\\
=\frac1{2\pi i}\int_{\mathcal C_+}
       \frac{K(w,(0,\zeta'))e^{iaw}}
            {P_+(w,(0,\zeta'))}\,dw.
\end{gathered}
\tag{9}
\]
The contour surrounds all upper roots and no other singularity. Repeated roots are included. Locally in \(\zeta'\) a fixed finite union of zero-free circles is valid; contour differentiation proves that \(U\) is holomorphic in \(\zeta'\) and smooth in \(a\), with all derivatives continuous at \(a=0\).

There are uniform polynomial bounds
\[
\begin{gathered}
|D_a^jU(a,\zeta')|
       \le C_j e^{2a}(1+|\zeta'|)^{M_j},
 \\
\quad a\ge0,\\
\quad \zeta'\in\Omega_\cap,\\
\quad j\ge0.
\end{gathered}
\tag{10}
\]
Here is a contour estimate with all constants controlled. Surround every upper root by a disk of a common radius \(\rho\in[1,2]\), and use the positive outer boundary of their union. Choose a radius avoiding the finitely many tangencies and multiple-intersection degeneracies; the boundary then consists of finitely many circular arcs, with total length at most \(4\pi h\). On it every root has distance at least \(\rho\ge1\), so \(|P_+|\ge1\). It lies in \(\operatorname{Im}w>-2\), hence \(|e^{iaw}|\le e^{2a}\), and \(|w|\) is at most two plus the largest root modulus. [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)/[Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md) give polynomial bounds for that modulus and all coefficients of \(K\). Differentiating in \(a\) inserts \(w^j\) with the exact \(D=-i\partial\) phase. These estimates prove 10. The circle choice is used for a bound only; holomorphy was already proved with locally fixed contours.

Multiplication by the normal polynomial removes the denominator:
\[
\begin{gathered}
P(D_a,\zeta')U(a,\zeta')
   \\
=\frac{q((0,\zeta'))}{2\pi i}
       \int_{\mathcal C_+}
              P_-(w,(0,\zeta'))\\
K(w,(0,\zeta'))e^{iaw}\,dw
   \\
=0.
\end{gathered}
\tag{11}
\]
The integrand is entire in \(w\), so each closed contour integral is zero by the complex Green identity. Original boundary symbols likewise give, at \(a=0\),
\[
\begin{gathered}
B_j(D_a,\zeta')U(0,\zeta')
      \\
=L(C_1,\ldots,C_{h-1},B_j;P_+)((0,\zeta'))\\
=0.
\end{gathered}
\tag{12}
\]
This uses 4, not just vanishing of one chosen minor at one parameter.

The cone \(V_\cap=\{\eta':(0,\eta')\in\Gamma\}\) is open and convex and contains \(N'\). Apply [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s complete flat-tube inverse to 9 on \(\mathbb R^{n-1}-iV_\cap\), using 10 for each derivative on compact \(a\)-intervals. It gives a smooth distribution-valued family \(u_a\), with
\[
 \operatorname{supp}u_a\subset V_\cap^*
       \subset\{x':x'\cdot N'\ge0\}.
 \tag{13}
\]
The construction commutes with the \(a\)-derivatives and tangential polynomial operators, so 11–12 become the asserted interior equation and boundary conditions. Extending the family by zero to \(a<0\) defines a distribution \(\widetilde u\) on all of \(\mathbb R^n\), supported in \(H\cap H'\).

## Boundary jets have the sharper cone support

For any fixed full-frequency polynomial \(B\), the trace \(B(D)u|_{a=0}\) has transform
\[
\begin{gathered}
F_B(\zeta')=
      L(C_1,\ldots,C_{h-1},B;P_+)\\
((0,\zeta'))
       \\
(\zeta'\in\Omega_\cap).
\end{gathered}
\tag{14}
\]
[Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md) proves that this maximal determinant extends holomorphically to
\(\mathbb R^{n-1}-i\pi\Gamma\), with a uniform polynomial bound and the explicit nonzero-leading-coefficient algebraic relation. By uniqueness of [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s inverse, its boundary distribution is the same trace constructed on the intersection tube. Consequently
\[
\begin{gathered}
\operatorname{supp}\bigl(B(D)u|_{a=0}\bigr)
      \\
\subset\{x':(0,x')\in C\}.
\end{gathered}
\tag{15}
\]
Thus every normal derivative and every tangential polynomial combination of a trace is supported on the section of \(C\), not only on the larger intersection-cone polar.

Write \(P(w,\zeta')=\sum_{k=0}^d A_k(\zeta')w^k\). The zero-extension formula is
\[
\begin{gathered}
D_a^k(\mathbf1_{a\ge0}u_a)\\
= \mathbf1_{a\ge0}D_a^ku_a+
       \\
\sum_{j=0}^{k-1}(-i)^{j+1}\delta^{(j)}(a)
                         (D_a^{k-1-j}u)_0 .
\end{gathered}
\tag{16}
\]
It follows by testing the first derivative and iterating ordinary integration by parts; equivalently start with
\(\partial^k(Hv)=H\partial^kv+\sum_{j<k}\delta^{(j)}v^{(k-1-j)}(0)\)
and multiply by \((-i)^k\). It is valid for this smooth distribution-valued family with compact tests, and requires no classical point values in the tangential variables.

Using the interior equation,
\[
\begin{gathered}
P(D)\widetilde u=f_\partial,\\
f_\partial=\sum_{k=1}^d\sum_{j=0}^{k-1}
      (-i)^{j+1}\delta^{(j)}(a)\otimes
               \\
A_k(D')(D_a^{k-1-j}u)_0,\\
\operatorname{supp}f_\partial\subset C\cap\{a=0\}.
\end{gathered}
\tag{17}
\]
The support assertion follows from 15 for every polynomial
\(B(w,\zeta')=A_k(\zeta')w^{k-1-j}\).
Its transform is a finite sum of polynomial normal factors times the corresponding extended \(F_B\):
\[
\begin{gathered}
\mathcal F_\partial(\zeta)
   \\
=\sum_{k=1}^d\sum_{j=0}^{k-1}
       (-i)^{j+1}(i\zeta_1)^j
                F_{A_kw^{k-1-j}}(\zeta').
\end{gathered}
\tag{18}
\]
[Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s polynomial bound makes this holomorphic and uniformly polynomially bounded on \(\mathbb R^n-i\Gamma\). The tensor and differentiation formulas, or direct compact-test Fourier inversion, identify its inverse with the boundary distribution in 17.

## The full cone support

There is a uniform denominator lower bound throughout the same full tube:
\[
\begin{gathered}
|P(\xi-i\eta)|\ge |P_m(N)|
       \\
\quad(\xi\in\mathbb R^n,\ \eta\in\Gamma).
\end{gathered}
\tag{19}
\]
For fixed \(\xi,\eta\), the polynomial \(z\mapsto P(\xi-i\eta+zN)\) has degree \(m\) and leading coefficient \(P_m(N)\). If a root has imaginary part \(b<1\), absorb its real \(N\)-shift into \(\xi\). The vector \(bN-\eta=N-(\eta+(1-b)N)\) lies in \(N-\Gamma\), contradicting the full barrier. All roots have imaginary part at least one, so their distances from zero are at least one; factorization proves 19.

[Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s inverse applied to \(\mathcal F_\partial/P\) gives a distribution \(v\) supported in \(C\), with \(P(D)v=f_\partial\). We identify it with \(\widetilde u\) by a transform for this particular family. Fix \(\lambda>2\), and then take \(T>0\) so large that
\(\lambda e_1+TN\in\Gamma\); this is possible because \(N\) is interior. At the imaginary vector \(\eta=-\lambda e_1-TN\), 10 implies that \(e^{\eta\cdot x}\widetilde u\) is tempered and has Fourier transform
\[
\begin{gathered}
\widehat{e^{\eta\cdot x}\widetilde u}(\xi_1,\xi')
       \\
=\int_0^\infty e^{-i\xi_1a-\lambda a}
                     U(a,\xi'-iTN')\,da.
\end{gathered}
\tag{20}
\]
For a Schwartz test, the tangential inverse bound is a fixed finite seminorm times \(e^{2a}\); the factor \(e^{-\lambda a}\) makes its integral finite. The displayed function has polynomial growth in \(\xi'\), uniformly in \(\xi_1\), and differentiating in \(\xi_1\) adds integrable powers of \(a\). Fubini and Schwartz Fourier inversion justify 20. This establishes the needed global tempering rather than assuming it.

Transform the distributional equation 17 at this fixed imaginary vector. The shifted differential operator multiplies the transform by \(P(\xi+i\eta)\), which is nonzero. Therefore
\[
 \widehat{e^{\eta\cdot x}\widetilde u}
      =\frac{\mathcal F_\partial(\xi+i\eta)}
                    {P(\xi+i\eta)}
      =\widehat{e^{\eta\cdot x}v}.
 \tag{21}
\]
[Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s construction gives the last equality. Fourier injectivity and invertibility of multiplication by the smooth nonzero exponential in ordinary distributions imply \(\widetilde u=v\). Hence
\[
 \operatorname{supp}\widetilde u\subset C\cap H'.
 \tag{22}
\]
Only this constructed exponential bound was used. We have not concluded uniqueness for every distribution of arbitrary growth from a Fourier transform that might not exist.

## The corner belongs to the support

8 and nondegeneracy of the pairing show that at least one fixed normal monomial \(B=\xi_1^k\), \(0\le k<h\), has \(F_B\not\equiv0\): if all its pairings with \(K\) vanished on the intersection tube, \(K\) would vanish there. Its extended determinant is nonzero as well. It is algebraic with the explicit leading \(q\)-power relation, and is polynomially bounded on the projected tube. [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s algebraic origin-support theorem gives
\[
\begin{gathered}
0\in\operatorname{supp}(D_a^ku)_0
       \\
\quad\text{for at least one }0\le k<h.
\end{gathered}
\tag{23}
\]
If the origin were outside the closure of the interior support of \(u\), the family would vanish on a product neighborhood
\(0<a<\varepsilon,\ |x'|<\varepsilon\).
Pair it with any tangential test supported there. The resulting smooth scalar function is zero for those positive \(a\), so all its one-sided derivatives at zero are zero. Every trace in 23 would vanish near the tangential origin, a contradiction. This proves exactly the support convention in 3 and completes the theorem.

## A smooth witness with zero initial data

Choose compact smooth tangential approximate identities \(\rho_\varepsilon\) of mass one, supported where \(x'\cdot N'>0\), and converging to the point mass at zero. For example translate a fixed small positive-ball bump by a vector of size \(O(\varepsilon)\) in the \(N'\) direction and scale its support by \(\varepsilon\). Put
\[
\begin{gathered}
u^\varepsilon(a,x')=(u_a*\rho_\varepsilon)(x'),
       \\
\qquad a\ge0.
\end{gathered}
\tag{24}
\]
Compact tangential convolution and the smooth distribution-valued family make this smooth in all variables up to \(a=0\); mixed derivatives are the corresponding pairings with derivatives of the translated compact bump. They commute with \(P(D)\) and \(B_j(D)\), so all equation and boundary data are zero. Its support is in \(H\cap H'\), since the original solution and the bump both have nonnegative time. Smoothness therefore makes every derivative vanish on the initial plane \(x_n=0\), including at the corner; for fixed \(a\ge0\), the smooth function is identically zero in the open past.

At least one sufficiently small \(\varepsilon\) gives a nonzero solution. Otherwise a sequence \(\varepsilon\downarrow0\) with every convolution zero would converge in distributions to \(u=0\), contradicting 23. Convergence follows by passing the compact-test convolution with an approximate identity through the distributional pairing. Thus 2 prevents unique smooth solvability with all forcing, initial jets and boundary data zero.

In particular a necessary condition for mixed uniqueness is that the original matrix have rank \(h\) on a nonempty open dense parameter set. If every \(h\)-minor were identically zero, 2 would hold. A nonzero analytic minor gives full rank away from its zero set, which has empty interior. This is a necessary condition only; the remaining determinant annihilation and invertibility theory is still required.

## Exercises with complete solutions

**Exercise 1 (entry: an outgoing boundary factor).** In two variables take
\(P(\xi,s)=(s-i)^2-\xi^2\), \(N=e_s\), \(\theta=e_\xi\), and \(B(\xi,s)=\xi+s-i\). Construct the deficient-rank solution and its smooth witness explicitly.

**Solution.** The upper factor is \(w+s-i\), with \(h=1\). Its pairing with \(B\) is zero, so the rank is zero at every parameter. There are no augmented rows and \(K=1\). The residue in 9 gives
\[
\begin{gathered}
U(a,s)=e^{-a}e^{-ias},\\
\qquad
 u_a(t)=e^{-a}\delta(t-a).
\end{gathered}
\tag{25}
\]
Its support is the forward ray \(t=a\ge0\), in the wave cone \(t\ge|a|\), and it reaches the origin. Direct differentiation shows
\((D_a+D_t-i)u=0\), hence \(P(D)u=0\) in \(a>0\), and \(B(D)u|_{a=0}=0\). For a nonzero smooth compact \(\rho\) supported in \(t>0\), the function \(e^{-a}\rho(t-a)\) is a nonzero smooth witness. All its derivatives vanish at \(t=0\), and the same first-order factor annihilates it. The zero initial and boundary data therefore do not give uniqueness. The zero-extended distribution's full transform is \(-i/(\xi+s-i)\), so multiplication by \(P\) gives \(i\xi-is-1\), confirming the boundary-phase formula 17–18.

**Exercise 2 (intermediate: a vanishing zeroth trace).** Take
\(P(\xi,s)=(s-i+\xi)^2(s-i-\xi)\) and only the Dirichlet symbol \(B_1=1\). Determine \(K,U\), and a trace that proves the corner belongs to the support.

**Solution.** The principal line has the positive root one twice and the negative root minus one, so \(h=2\). The upper factor is \((w+s-i)^2=(w-\rho)^2\), \(\rho=i-s\). The row for \(B_1=1\) is \((0,1)\), hence the cofactor polynomial is \(K=-1\). The repeated residue gives
\[
\begin{gathered}
U(a,s)=-ia\,e^{-a}e^{-ias},\\
\qquad
 u_a(t)=-ia\,e^{-a}\delta(t-a),\\
\qquad
 u_0=0,\\
\quad(D_au)_0=-\delta_0.
\end{gathered}
\tag{26}
\]
The nonzero first normal trace supplies 23 even though the prescribed zeroth trace vanishes. Applying \(D_a+D_t-i\) once gives \(-e^{-a}\delta(t-a)\), and applying it again gives zero, so the full \(P\) annihilates \(u\) in the interior. Tangential smoothing gives \(-ia e^{-a}\rho(t-a)\), again a nonzero smooth homogeneous witness with zero initial and Dirichlet data. A repeated decaying root contributes a second independent mode; one boundary datum cannot remove it.

**Exercise 3 (advanced: generic rank and isolated loss).** Explain why \(\mu<h\) always triggers the theorem. For the wave polynomial in Exercise1, compare \(B=\xi+s-i\) with \(B=\xi-2i\), whose determinant is \(-s-i\). Does a zero of the latter determinant alone meet 2?

**Solution.** A \(\mu\)-by-\(h\) matrix has rank at most \(\mu\), so \(\mu<h\) makes it deficient at every parameter. At \(h=0\), by contrast, 2 is impossible and the theorem has no witness to construct. The first wave boundary symbol has determinant identically zero and does trigger the construction. The second determinant vanishes at \(s=-i\) but is nonzero on a nonempty open set, so its matrix has generic full rank one. Its isolated zero does not satisfy the hypothesis that rank be deficient everywhere. The cofactor construction for \(h=1\) has \(K=1\), and its trace under this second \(B\) is precisely \(-s-i\), which is not the zero analytic function. It therefore would not satisfy the required homogeneous boundary condition. This example proves why one cannot replace identically deficient rank by a single zero frequency. Generic full rank remains only a necessary condition here; no general mixed uniqueness is inferred from it.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Open lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
