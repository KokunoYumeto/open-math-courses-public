# Boundary fundamental kernels and their propagation support

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

An invertible boundary matrix prescribes one incoming normal mode for each boundary datum. We turn its inverse into distribution kernels, including repeated roots, and prove their propagation support. Boundary traces have the boundary dual-cone support. At positive normal position the whole kernel has the combined boundary and interior cone support; these two assertions must be distinguished.

Read [Polynomial reciprocal bounds inside a mixed boundary tube](polynomial-reciprocal-bounds-inside-a-mixed-boundary-tube.md), [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md), [Missing boundary rank produces a causal solution](missing-boundary-rank-produces-a-causal-solution.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies the Fourier convention and Gaussian formula; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies scalar calculus and cutoffs. [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html) supplies finite scalar and polynomial algebra. [Tensor products and parameter-dependent distributions](../prerequisites/tensor-products-and-parameters.html) supplies compact parameter and tensor operations. [Convolution as addition of supports](../prerequisites/convolution-as-addition-of-supports.html) supplies proper convolution.

The general hyperbolic-cone and analytic zero-order theorems remain planned prerequisites, with precise statements in [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md). Their uses below are conditional on those proofs.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's treatment of constant-coefficient equations. The linked lessons supply the prerequisite proofs used below.

## Statement and the inverse residue matrix

Use coordinates \((a,x')\), with \(a\) the normal position and \(t=x'\cdot N'\) time. The time and normal covectors are independent. The polynomial \(P\), normal counts \(h,\ell\), transported factors \(R_\pm\), determinant \(L\), barrier \(\tau_0\), and cone \(\Sigma\) are those of [Extending a boundary time strip to its propagation cone](extending-a-boundary-time-strip-to-its-propagation-cone.md)/[Polynomial reciprocal bounds inside a mixed boundary tube](polynomial-reciprocal-bounds-inside-a-mixed-boundary-tube.md). The balanced boundary symbols are \(B_1,\ldots,B_h\), and \(\gamma_0\le\min(0,\tau_0)\) is the chosen zero-free-strip bound.

Write a polar with the nonnegative pairing convention, and embed the tangential polar in the full physical space at \(a=0\):
\[
 C=\Gamma^\circ,\qquad
 C_\partial=\{(0,x'):x'\in\Sigma^\circ\}.
 \tag{1}
\]
**Theorem.** There are \(h\) distribution-valued families \(e_k(a,\cdot)\), \(a\ge0\), smooth with all one-sided normal derivatives, satisfying
\[
\begin{gathered}
P(D)e_k=0\\
\quad(a>0),\\
\qquad
 B_j(D)e_k|_{a=0}=\delta_{jk}\delta_0(x'),\\
\qquad
 \operatorname{supp}(\mathbf1_{a\ge0}e_k)
                  \\
\subset (C+C_\partial)\cap\{a\ge0\}.
\end{gathered}
\tag{2}
\]
The support includes the closure of the interior distributional support, and the boundary traces are those of the smooth distribution-valued family. No kernels are required when \(h=0\); in the proof assume \(h\ge1\).

Let
\[
\begin{gathered}
M_{jr}(\zeta')=\beta_{R_+}(B_j,w^r),
       \\
\quad 1\le j\le h,\\
\quad0\le r<h,\\
\qquad
 H_k(w,\zeta')=\sum_{r=0}^{h-1}(M^{-1})_{rk}(\zeta')w^r .
\end{gathered}
\tag{3}
\]
Index r denotes a zero-based polynomial coefficient; index k is the one-based datum. Then
\(\beta_{R_+}(B_j,H_k)=\delta_{jk}\).
[Polynomial reciprocal bounds inside a mixed boundary tube](polynomial-reciprocal-bounds-inside-a-mixed-boundary-tube.md) proves that all coefficients of \(H_k\) are holomorphic in the open zero-free tube and polynomially bounded on
\[
\begin{gathered}
K_\partial=\{\operatorname{Im}\zeta'
              \in\delta N'-\overline\Sigma\},
             \\
\qquad \delta=\gamma_0-1 .
\end{gathered}
\tag{4}
\]
Their degrees in w are below h even at repeated roots.

## Construct the family where the selected roots are actually upper

Define
\[
\begin{gathered}
V_\cap=\{\eta':(0,\eta')\in\Gamma\},\\
\qquad
 V=V_\cap\cap\Sigma .
\end{gathered}
\tag{5}
\]
These are open convex cones containing \(N'\). For a frequency with
\(\operatorname{Im}\zeta'\in\delta N'-V\), the full zero normal representative is in the original [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md) tube: its difference from the barrier is
\((\tau_0-\delta)N+(0,\eta')\in\Gamma\).
Thus the transported \(R_+\) is the actual upper factor there. Set
\[
\begin{gathered}
U_k(a,\zeta')=\frac1{2\pi i}\\
\int_{\mathcal C_+}
              \frac{H_k(w,\zeta')e^{iaw}}{R_+(w,\zeta')}\,dw,
                           \\
\qquad a\ge0 .
\end{gathered}
\tag{6}
\]
The contour surrounds the entire upper root group with multiplicities. Locally a fixed finite contour remains away from all roots, so the expression is holomorphic in \(\zeta'\) and smooth in a, including all right derivatives at zero.

The buffered q bound of [Polynomial reciprocal bounds inside a mixed boundary tube](polynomial-reciprocal-bounds-inside-a-mixed-boundary-tube.md) and the transported coefficient bound give polynomial bounds for all roots and the coefficients of \(H_k\). On the union-of-disks contour of [equation 7 in A necessary time strip for smooth mixed solvability](a-necessary-time-strip-for-smooth-mixed-solvability.md), radius between one and two, the denominator has modulus at least one, contour length is at most \(4\pi h\), and imaginary height is at least minus two. Consequently for each fixed r,
\[
\begin{gathered}
|D_a^rU_k(a,\zeta')|
       \le C_r e^{2a}(1+|\zeta'|)^{M_r}
       \\
\quad(a\ge0,\ \operatorname{Im}\zeta'\in\delta N'-V).
\end{gathered}
\tag{7}
\]
The constants are uniform over this entire affine tube. The same repeated-root contour argument proves the bound; no derivative of an individual root label is taken.

Cancellation of the factor \(R_+\) in the interior polynomial leaves an entire integrand. At \(a=0\), the boundary pairing is 3. Hence
\[
\begin{gathered}
P(D_a,\zeta')U_k=0,\\
\qquad
 B_j(D_a,\zeta')U_k(0,\zeta')=\delta_{jk}.
\end{gathered}
\tag{8}
\]
All derivatives and boundary operations can be passed through the fixed local contour.

We use the affine version of [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s proved flat-tube inverse. If F is holomorphic and uniformly polynomially bounded on the tube with imaginary part \(\delta N'-V\), then
\(\widetilde F(z')=F(z'+i\delta N')\) satisfies [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md) on the negative V tube. Its inverse \(\widetilde T\) is tempered and supported in \(V^\circ\). Put
\[
\begin{gathered}
T=e^{-\delta t}\widetilde T,\\
\qquad
 \widehat{\,e^{\delta t}T\,}(z')=
                 F(z'+i\delta N').
\end{gathered}
\tag{9}
\]
This is an identity of Fourier–Laplace transforms; the sign follows from
\(\widehat{e^{\delta t}T}(z')=\widehat T(z'+i\delta N')\).
Multiplication by the nowhere zero exponential preserves ordinary distributional support.

Apply this construction to 6 and every fixed derivative in 7. The compact-test integral defining [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s inverse permits normal differentiation by its uniform polynomial bound on compact a-intervals, as proved in [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)/[Missing boundary rank produces a causal solution](missing-boundary-rank-produces-a-causal-solution.md). This gives a smooth family \(e_k(a,\cdot)\), with
\[
\begin{gathered}
\operatorname{supp}e_k(a,\cdot)\subset V^\circ,\\
\qquad
 P(D)e_k=0\ (a>0),\\
\qquad
 B_j(D)e_k|_{a=0}=\delta_{jk}\delta_0 .
\end{gathered}
\tag{10}
\]
The inverse and all its normal derivatives have a fixed finite Schwartz seminorm bound times \(C_re^{2a}\) after multiplication by \(e^{\delta t}\). In particular all right traces at \(a=0\) exist. Since \(N'\) is interior in V, its polar satisfies \(t\ge b|x'|\) for some \(b>0\): use a small ball about \(N'\) contained in V and minimize its pairing. Thus the initial family is causal. We have not asserted that its support at positive a lies in \(\Sigma^\circ\).

## Every boundary jet has the sharper boundary support

For any fixed \(r\ge0\), the normal trace transform is the finite Laurent coefficient
\[
 J_{rk}(\zeta')
       =[w^{-1}]\,\frac{w^rH_k(w,\zeta')}{R_+(w,\zeta')}.
 \tag{11}
\]
It is holomorphic on the full projected zero-free tube. The Laurent recurrence uses only finitely many coefficients for each fixed r, so [Polynomial reciprocal bounds inside a mixed boundary tube](polynomial-reciprocal-bounds-inside-a-mixed-boundary-tube.md)'s coefficient and inverse-matrix bounds make it uniformly polynomially bounded on \(K_\partial\).

Apply 9 now with \(V=\Sigma\). It gives a distribution \(T_{rk}\), supported in \(\Sigma^\circ\), with transform \(J_{rk}\) on the affine boundary tube. On the smaller tube of 5 it has the same transform as the already constructed trace \(D_a^re_k(0,\cdot)\). The affine [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md) inverse is unique, by actual Schwartz Fourier injectivity on any one common imaginary line. Therefore
\[
\begin{gathered}
D_a^re_k|_{a=0}=T_{rk},\\
\qquad
                   \operatorname{supp}T_{rk}\subset\Sigma^\circ .
\end{gathered}
\tag{12}
\]
This works for every finite r needed by P or a boundary polynomial, and for repeated roots. Transported roots outside the intersection tube can be below the real axis; the finite Laurent trace, rather than an unjustified decaying-mode integral there, is what extends across that tube.

## Zero extension and its exact boundary forcing

Extend \(e_k\) by zero to \(a<0\), as an ordinary distribution, and call it \(\mathcal E_k\). Its action on a compact test is the integral for \(a\ge0\) of the smooth distribution-valued family. Write
\(P(w,\zeta')=\sum_{r=0}^dp_r(\zeta')w^r\).
[Missing boundary rank produces a causal solution](missing-boundary-rank-produces-a-causal-solution.md)'s full zero-extension calculation gives
\[
\begin{gathered}
D_a^r\mathcal E_k
   \\
=\mathbf1_{a\ge0}D_a^re_k+
       \sum_{j=0}^{r-1}(-i)^{j+1}\delta^{(j)}(a)
                                       \\
\otimes T_{r-1-j,k}.
\end{gathered}
\tag{13}
\]
It follows by ordinary integration by parts and multiplication by \((-i)^r\). The right-smooth distribution-valued version is justified by compact-test differentiation, not point values in \(x'\).

Using the interior equation, obtain
\[
\begin{gathered}
P(D)\mathcal E_k=F_k,\\
\qquad
 F_k\\
=\sum_{r=1}^d\sum_{j=0}^{r-1}(-i)^{j+1}
           \\
\delta^{(j)}(a)\otimes p_r(D')T_{r-1-j,k},
 \\
\qquad \operatorname{supp}F_k\subset C_\partial .
\end{gathered}
\tag{14}
\]
The transform of this finite boundary distribution is
\[
\begin{gathered}
\mathscr F_k(\zeta_a,\zeta')
       \\
=-i\sum_{r=1}^d p_r(\zeta')
                     \sum_{j=0}^{r-1}\zeta_a^jJ_{r-1-j,k}(\zeta').
\end{gathered}
\tag{15}
\]
Indeed \(\widehat{\delta^{(j)}}=(i\zeta_a)^j\), and
\((-i)^{j+1}(i\zeta_a)^j=-i\zeta_a^j\). The entire sum has the same phase, without a missing factor for higher derivatives. It is polynomial in normal frequency and holomorphic in the boundary frequency, with a uniform polynomial bound whenever the latter belongs to \(K_\partial\).

## Identify the polar of the combined cone

Set
\[
 W=\Gamma\cap\pi^{-1}\Sigma,\qquad
                         S=C+C_\partial .
 \tag{16}
\]
The cone W is open and convex and contains N. The two closed polar cones C and \(C_\partial\) each have a common proper time bound, \(t\ge b_i|x|\), since N and \(N'\) are interior in their primal cones. Thus S is closed: in a convergent sequence \(c_j+d_j\), the nonnegative times of its two summands are bounded by the bounded sum times, so their full norms are bounded. Subsequence limits stay in the closed summand cones. S is also a convex cone.

We give the finite-dimensional polar identity rather than importing an unproved cone-sum rule. A closed convex cone A equals its double polar. If \(x\notin A\), take a nearest point y in A; it exists by minimizing distance in a sufficiently large compact ball. The variational inequality
\((x-y)\cdot(c-y)\le0\), \(c\in A\), follows by differentiating squared distance along the segment from y to c. Using \(c=0,2y\) gives \((x-y)\cdot y=0\). Hence \(y-x\) is nonnegative on A and has negative pairing with x. It separates x from the double polar. The other inclusion follows from the definition. This proves the identity using only the actual finite-coordinate compactness and inner-product facts.

The polar of S is
\(\overline\Gamma\cap\pi^{-1}\overline\Sigma\).
For the boundary cone, the absence of any normal component makes its dual precisely the inverse image of the closed tangential primal cone. The closure of W equals this intersection: a point in the closed intersection plus \(\epsilon N\) belongs to both open cones for every \(\epsilon>0\), by the buffered-cone argument, and tends back to that point. Taking a second polar and using S's closedness proves
\[
 W^\circ=\Gamma^\circ+C_\partial=S .
 \tag{17}
\]
All signs use nonnegative pairings. No closure of the sum is silently omitted.

## A full-tube inverse supplies the support refinement

Choose \(\delta'=\gamma_0-2\). On the full affine tube with imaginary part
\(\delta'N-W\), the projected frequency lies in \(K_\partial\):
if \(\eta\in W\), its missing boundary cone vector is
\(N'+\pi\eta\in\Sigma\). Therefore \(\mathscr F_k\) is holomorphic and polynomially bounded there.

There is a uniform denominator lower bound
\[
\begin{gathered}
|P(\zeta)|\ge|P_m(N)|>0,\\
\qquad
                     \operatorname{Im}\zeta\in\delta'N-W .
\end{gathered}
\tag{18}
\]
To verify it, the polynomial \(z\mapsto P(\zeta+zN)\) has degree m and leading coefficient \(P_m(N)\). If a root had imaginary part \(b<1\), its full imaginary vector would be
\((\delta'+b)N-\eta\). Its difference from the barrier is
\((\tau_0-\delta'-b)N+\eta\in\Gamma\), since
\(\tau_0-\delta'\ge2\) and \(\eta\in W\subset\Gamma\).
This contradicts the interior zero exclusion. Every root has imaginary part at least one, so factoring at zero proves 18. Absorbing the real part of a root into the real frequency is permitted here.

Apply the full-dimensional affine [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md) inverse to
\[
 G_k(\zeta)=\mathscr F_k(\zeta)/P(\zeta).
 \tag{19}
\]
It is holomorphic and uniformly polynomially bounded by 15 and 18. The result is a distribution \(v_k\) with
\(P(D)v_k=F_k\) and support in \(W^\circ=S\).
The equation follows from [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s differentiation rule and its inverse uniqueness, since multiplication of the transform by P gives the transform of the actual boundary distribution 14.

We identify this inverse with the constructed zero extension using a justified transform of that family. Choose \(\lambda>2\), then T sufficiently large that
\[
\begin{gathered}
\lambda e_a+(T+\delta')N\in W,\\
\qquad
 T+\delta>0,\\
\qquad
 \eta_*=-\lambda e_a-TN .
\end{gathered}
\tag{20}
\]
The first condition is possible because N is interior in W; the projection is a positive multiple of \(N'\), and the full vector tends in direction to N as T grows. This \(\eta_*\) is an admissible imaginary line of 19. The affine family estimate after 10 gives tempering of
\(e^{\eta_*\cdot x}\mathcal E_k\): its fixed tangential Schwartz seminorm grows at most as \(e^{2a}\), while \(e^{-\lambda a}\) is integrable. The extra time factor \(e^{-(T+\delta)t}\) has a globally smooth bounded-derivative extension on the causal support, by inserting a cutoff equal to one for \(t\ge0\) and zero for \(t\le-1\).

For a full Schwartz test, integrate the resulting finite tangential seminorm over \(a\ge0\). The bound is a fixed full Schwartz seminorm times
\(\int_0^\infty e^{(2-\lambda)a}\,da<\infty\).
This proves a full tempered distribution, rather than postulating a transform of an arbitrary solution. Fubini and the actual Schwartz Fourier isomorphism give
\[
\begin{gathered}
\widehat{\,e^{\eta_*\cdot x}\mathcal E_k\,}(\xi_a,\xi')
      \\
=\int_0^\infty e^{-i\xi_a a-\lambda a}
                           U_k(a,\xi'-iTN')\,da .
\end{gathered}
\tag{21}
\]
The integral and every fixed normal-frequency derivative have polynomial tangent growth, since extra powers of a are integrable.

Transform 14 at this line. Its boundary transform is exactly 15, and its shifted interior multiplier is the nonzero polynomial \(P(\xi+i\eta_*)\). Multiplication by its smooth reciprocal is valid on tempered distributions: Cauchy estimates on a small fixed imaginary neighborhood give polynomial bounds for every reciprocal derivative, using 18 on a possibly smaller interior tube. Hence
\[
 \widehat{\,e^{\eta_*\cdot x}\mathcal E_k\,}
       =\frac{\mathscr F_k(\xi+i\eta_*)}{P(\xi+i\eta_*)}
       =\widehat{\,e^{\eta_*\cdot x}v_k\,}.
 \tag{22}
\]
The second equality is the affine [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md) inverse identity. Fourier injectivity and injectivity of the nonzero exponential multiplier in ordinary distributions give \(\mathcal E_k=v_k\). Thus
\[
 \operatorname{supp}\mathcal E_k
          \subset S\cap\{a\ge0\}.
 \tag{23}
\]
This completes 2, with all original boundary conditions, exact phases, repeated roots and the correct combined cone. It does not assert uniqueness for arbitrary-growth distribution solutions by the same transform.

## Exercises with complete solutions

**Exercise 1 (entry: Dirichlet and normal-derivative wave kernels).** For \(P(w,s)=(s-i)^2-w^2\), construct the kernels for \(B=1\) and \(B=w\). Check both boundary traces and the zero-extension forcing of the Dirichlet kernel.

**Solution.** The upper root is \(\lambda=i-s\). For Dirichlet, the scalar matrix is one and the mode is \(e^{ia\lambda}\). For the normal derivative the scalar matrix is \(\lambda\), whose reciprocal is the transform of \(-iH(t)e^{-t}\). Therefore the kernels are
\[
\begin{gathered}
e_D(a,t)=e^{-a}\delta(t-a),\\
\qquad
 e_N(a,t)=-iH(t-a)e^{-t}.
\end{gathered}
\tag{24}
\]
The Fourier–Laplace transform of \(H(t)e^{-t}\) is
\(1/(1+is)=-i/(s-i)\); multiplication by \(-i\) gives \(1/(i-s)\), confirming the phase. The Dirichlet trace is \(\delta(t)\).
Since \(\partial_a e_N=i\delta(t-a)e^{-t}\), its \(D_a=-i\partial_a\) boundary trace is \(\delta(t)\). In the interior, writing either kernel as \(e^{-t}\) times a distribution in \(t-a\) reduces P to the ordinary wave difference \(-\partial_t^2+\partial_a^2\), which vanishes.

For Dirichlet, \(D_ae_D|_0=i\delta(t)+i\delta'(t)\). The normal leading coefficient of P is \(-1\), so 14 gives
\[
\begin{gathered}
P(D)(H(a)e_D)
    =\delta'(a)\otimes\delta(t)
       \\
-\delta(a)\otimes\delta'(t)
       \\
-\delta(a)\otimes\delta(t),\\
\qquad
 \mathscr F_D=i\zeta_a-is-1 .
\end{gathered}
\tag{25}
\]
Multiplying the normal transform
\(-i/(\zeta_a+s-i)\) by P gives the same polynomial. Both kernels are supported in \(t\ge a\), with the expected wave support; the Neumann kernel is not a point mass on the front.

**Exercise 2 (intermediate: two traces at a repeated root).** Square the preceding wave polynomial and take \(B_1=1,B_2=w\). Compute the inverse residue matrix and both kernels.

**Solution.** The upper factor is \((w-\lambda)^2\), \(\lambda=i-s\). The finite pairing gives
\[
\begin{gathered}
M=\begin{pmatrix}0&1\\1&2\lambda\end{pmatrix},\\
\qquad
 M^{-1}=\begin{pmatrix}-2\lambda&1\\1&0\end{pmatrix},\\
\qquad
 H_1=w-2\lambda,\\
\quad H_2=1 .
\end{gathered}
\tag{26}
\]
The double-pole residues yield
\[
\begin{gathered}
U_1(a,s)=e^{ia\lambda}(1-ia\lambda),\\
\qquad
 U_2(a,s)=ia\,e^{ia\lambda}.
\end{gathered}
\tag{27}
\]
Their value traces are \(1,0\), and their \(D_a\) traces are \(0,1\); direct differentiation supplies those four values. The polynomial squared annihilates both interior modes because the upper normal factor does. Transforming the tangent terms gives
\[
\begin{gathered}
e_1(a,t)\\
=e^{-a}\left\{\begin{gathered}(1+a)\delta(t-a)\\
+a\delta'(t-a)\end{gathered}\right\},
 \\
\qquad e_2(a,t)=ia\,e^{-a}\delta(t-a).
\end{gathered}
\tag{28}
\]
Here \(\widehat{\delta'}=is\). Every normal derivative is a finite smooth coefficient combination of translated delta derivatives, so the family is smooth in distributions through \(a=0\). Its support remains on \(t=a\). A repeated root supplies an additional normal mode and a second prescribed trace, without any simple-root label.

**Exercise 3 (advanced: the interior kernel need not have only boundary-cone support).** Take \(P(w,y,s)=s(w+s)-y^2\), \(B_1=1\). Find its projected cone, boundary cone and combined dual cone, and compute the kernel for \(a>0\). Explain the distinction between trace support and positive-a support.

**Solution.** The full principal cone and its projected boundary cone are
\[
\begin{gathered}
\Gamma\\
=\{(w,y,s):s>0,\ w+s>y^2/s\},\\
\qquad
 \Sigma=\Omega=\{(y,s):s>0\}.
\end{gathered}
\tag{29}
\]
The single normal root for real y and \(\operatorname{Im}s<0\) is
\(\rho=y^2/s-s\), whose imaginary part is positive. Thus \(h=1,L=1,\kappa=0\), and the mixed system is hyperbolic. The boundary polar is
\(\Sigma^\circ=\{(z,t):z=0,t\ge0\}\).
For the full polar, minimizing \(aw+zy+ts\) over \(w>y^2/s-s\) gives, for \(a>0\), the condition
\[
\begin{gathered}
\Gamma^\circ\\
=\{a>0,\ t\\
\ge a+z^2/(4a)\}
              \ \cup\ \{a\\
=0,z\\
=0,t\\
\ge0\}.
\end{gathered}
\tag{30}
\]
Indeed the infimum over y is
\(s(t-a-z^2/(4a))\); a negative a would make the pairing unbounded below as w grows. At \(a=0\), arbitrary y forces z zero and then positive s forces \(t\ge0\). Adding \(C_\partial\) does not enlarge this full cone, since its time ray is already contained in it.

The transform of the kernel is
\(U(a,y,s)=\exp(ia(y^2/s-s))\).
At \(s=-i\tau\), \(\tau>0\), this is \(e^{-a\tau}e^{-ay^2/\tau}\).
[Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html)'s Gaussian Fourier identity gives its inverse in z as
\(\sqrt{\tau/(4\pi a)}e^{-\tau(a+z^2/(4a))}\).
Also the Gaussian integral gives
\(\int_0^\infty e^{-\tau r}r^{-1/2}\,dr=\sqrt\pi\,\tau^{-1/2}\), by the substitution \(r=u^2/\tau\).
Thus the distributional time inverse is
\[
\begin{gathered}
e(a,z,t)=\frac1{2\pi\sqrt a}\,
      \\
\partial_t\left[
        \frac{H(t-a-z^2/(4a))}{\sqrt{\,t-a-z^2/(4a)\,}}\right],
                         \\
\qquad a>0 .
\end{gathered}
\tag{31}
\]
The bracket is locally integrable, and its derivative is a distribution, including at its front; it is not a pointwise formula at the front. Its time Laplace transform is the preceding Gaussian inverse, so uniqueness on a fixed imaginary line verifies 31. The kernel has exact support \(t\ge a+z^2/(4a)\): it vanishes below that front and its ordinary derivative is nonzero at every strict point above it. Its boundary value is \(\delta(z)\delta(t)\), as given by the limit of U and the smooth constructed family.

For \(a>0\) this support includes nonzero z. It therefore has more than the boundary polar's \(z=0\) support. All boundary jets still have transforms \(\rho^r=(y^2/s-s)^r\), finite polynomials in y with causal reciprocal powers of s; their support is \(z=0,t\ge0\), as 12 proves. The combined cone in 23 is the accurate propagation statement.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Open lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
