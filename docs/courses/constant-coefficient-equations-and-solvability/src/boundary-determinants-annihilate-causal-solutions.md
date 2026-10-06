# Boundary determinants annihilate causal solutions

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A square boundary matrix determines a causal convolution operator on the boundary plane. Every smooth solution of the homogeneous mixed problem is annihilated by that operator throughout the physical half-space. We derive the exact forcing representation, justify its convolutions by a bounded backward region, and prove the needed continuation from the stated local Holmgren theorem.

Read [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md), [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md), [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies the Schwartz Fourier transform; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies compact extrema and cutoffs; [Convolution as addition of supports](../prerequisites/convolution-as-addition-of-supports.html) supplies proper convolution.

The hyperbolic-cone and analytic zero-order prerequisites remain planned in [Distributions, kernels and analytic singularities](../prerequisites/planned-foundation-proofs.html); their precise statements are given in [Hyperbolicity and lower order terms](hyperbolicity-and-lower-order-terms.md). Local Holmgren uniqueness also remains planned: a distribution solving an analytic-coefficient equation and vanishing on one side of a noncharacteristic surface vanishes near that surface. The uses of these prerequisites are conditional on their planned proofs.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's treatment of constant-coefficient equations. The written prerequisite lessons supply the auxiliary proofs used below.

## The theorem and its exact prerequisites

Use the normalized notation of [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md) and [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md): the independent time and boundary normals are \(N=e_n\), \(\theta=e_1\), physical coordinates are \(x=(a,x')\), and the time coordinate \(t=x_n\) belongs to \(x'\). Put
\[
\begin{gathered}
H=\{t\ge0\},\\
\qquad H'=\{a\ge0\},\\
\qquad
 \Gamma=\Gamma(P_m,N),\\
\qquad C=\Gamma^* .
\end{gathered}
\tag{1}
\]
The nonzero complex polynomial \(P\), of total degree \(m\ge1\), is hyperbolic in \(N\). Normalize its zero-free barrier to one as in [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md). Its full time tube contains \(\mathbb R^n-i\Gamma\), and its normal factorization there has the form
\[
\begin{gathered}
P((w,\zeta'))=q(\zeta')R_+(w,\zeta')R_-(w,\zeta'),
 \\
\qquad \deg_w R_+=h=m_+,\\
\quad \deg_w R_-=\ell=m_- .
\end{gathered}
\tag{2}
\]
Here the two factors are the transported monic factors on [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s projected tube. They have their upper and lower root meanings at a zero normal representative only on
\[
\begin{gathered}
V=\{\eta':(0,\eta')\in\Gamma\},\\
\qquad
 \Omega_\cap=\mathbb R^{n-1}-iV,\\
\qquad
 D_0=V^* .
\end{gathered}
\tag{3}
\]
The open convex cone \(V\) contains the tangential time vector \(N'\). In particular its polar is a closed proper cone: choosing a small ball about \(N'\) inside \(V\) gives a number \(b>0\) with
\[
 t_z\ge b|z'|\quad(z'\in D_0).
 \tag{4}
\]
This is the elementary polar argument proved in [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md). No bounded normal lift on the larger projected tube is assumed.

Let there be exactly \(h\) polynomial boundary symbols \(B_1,\ldots,B_h\). Let \(L^\partial(\zeta')\) be their determinant, descended as in [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md), and let \(L_0\) be its causal inverse distribution. Thus
\[
\begin{gathered}
\operatorname{supp}L_0\subset C_0
\\
:=\{x':(0,x')\in C\}\subset D_0,\\
\qquad
 \mathcal L=\delta_0(a)\otimes L_0 .
\end{gathered}
\tag{5}
\]
The last inclusion follows directly by testing \((0,\eta')\in\Gamma\). The transform of \(\mathcal L\) is \(L^\partial\), independent of normal frequency. At \(h=0\), the empty determinant is one and \(L_0=\delta_0(x')\). If the determinant is identically zero, \(L_0=0\); the asserted annihilation is then meaningful but automatic.

**Theorem, relative to the stated Holmgren prerequisite.** Suppose \(u\in C^\infty(H')\), with every right derivative continuous up to \(a=0\), and
\[
\begin{gathered}
P(D)u=0\\
\quad(a>0),\\
\qquad
 B_j(D)u|_{a=0}=0\\
\quad(1\le j\le h),\\
\qquad
 \operatorname{supp}u\subset H\cap H' .
\end{gathered}
\tag{6}
\]
Then the tangential convolution, well-defined at each \(a\ge0\), satisfies
\[
                 \mathcal L*u=L_0*_{x'}u=0
                       \quad\text{on }H'.
 \tag{7}
\]
There is no growth restriction on \(u\) at spatial infinity. Smoothness on the closed half-space means right smoothness; the proof does not import an arbitrary full smooth extension of \(u\).

[Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md) supplies the factorization and its polynomial coefficient estimates. [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md) supplies the nondegenerate residue pairing and polynomial adjugate identities. [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md) supplies descent and the complete flat-tube inverse, including support and smooth-parameter statements. The Fourier, finite-matrix and compact-cutoff lessons, and the tensor and proper-convolution lessons, are the auxiliary bases.

The two prerequisites in [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md) remain planned prerequisites: the homogeneous hyperbolic cone theorem and the analytic zero-strip Taylor-order theorem. One further planned theorem is used here: local Holmgren uniqueness for a distribution solving an analytic-coefficient equation and vanishing on one side of a noncharacteristic \(C^1\) surface. The two continuation arguments below are proved from precisely this local theorem. No general convex continuation theorem or arbitrary-growth Cauchy uniqueness theorem is imported.

## A positive-time wedge from a quadratic barrier

Choose \(\delta>0\) so small that
\[
                    \overline{B(N,4\delta)}\subset\Gamma .
 \tag{8}
\]
This is possible because \(N\) is interior. We claim that any \(u\) in equation 6 vanishes where \(a>0\) and \(t<\delta a\). The claim uses the interior equation and time support only.

Assume a point \(x_0=(a_0,z_0,t_0)\) of the support satisfies \(a_0>0\), \(0\le t_0<\delta a_0\). Write \(y_s=(a,z)\) for all coordinates other than time, and choose \(\epsilon>0\) with \(4\epsilon t_0\le\delta^2\). Define on the closed half-space
\[
       F(y)=t-\delta a+\epsilon|y_s-x_{0,s}|^2 .
 \tag{9}
\]
Its value at \(x_0\) is negative. On the support, \(t\ge0\). The sublevel \(F\le F(x_0)\) is compact: with \(v=y_s-x_{0,s}\), its defining inequality is
\[
\begin{gathered}
t+\epsilon|v|^2-\delta v_1\le t_0,\\
\qquad
       0\le t\le t_0+\delta^2/(4\epsilon),\\
\qquad
       2\epsilon|v|\le\delta+\sqrt{\delta^2+4\epsilon t_0}.
\end{gathered}
\tag{10}
\]
The first bound follows by completing the square; the second follows from
\(\epsilon|v|^2-\delta|v|\le t_0\).
Consequently \(F\) attains a negative minimum on the closed support at some \(y_*\). At \(a=0\), \(F=t+\epsilon|y_s-x_{0,s}|^2\ge0\), so \(a_*>0\). A neighborhood of \(y_*\) therefore lies in the interior equation domain.

There the support lies on the side \(F\ge F(y_*)\), and
\[
\begin{gathered}
dF(y_*)=N-\delta\theta+2\epsilon(v_*,0),\\
\qquad
 |dF(y_*)-N|\\
\le(2+\sqrt2)\delta<4\delta .
\end{gathered}
\tag{11}
\]
Its normal belongs to \(\Gamma\), so \(P_m(dF(y_*))\ne0\). The level surface is smooth and noncharacteristic. The stated local Holmgren theorem makes \(u\) vanish near \(y_*\), contradicting its being a support point. Thus
\[
          \operatorname{supp}u
                  \subset\{a\ge0,\ t\ge\delta a\}.
 \tag{12}
\]
This gives a sufficient positive slope. It does not claim the optimal slope determined by the first positive principal root.

We also need full-space causal uniqueness. If a distribution \(W\) on \(\mathbb R^n\) solves \(P(D)W=0\) and has support in \(t\ge0\), then \(W=0\), relative to the same planned local Holmgren theorem. To prove this, take a support point \(x_0\), and minimize
\[
\begin{gathered}
G(y)=t+\epsilon|y_s-x_{0,s}|^2
                      \\
\quad\text{on }\operatorname{supp}W .
\end{gathered}
\tag{13}
\]
The nonempty sublevel \(G\le t_0\) is compact, so a minimum is attained. At that point
\(|dG-N|\le2\sqrt{\epsilon t_0}\).
Choose \(\epsilon\) so small that every such normal is noncharacteristic; continuity of \(P_m\) at \(N\), where \(P_m(N)\ne0\), suffices. The support lies on one side of the smooth minimum level. Local Holmgren gives the same contradiction. If \(t_0=0\), the gradient bound is zero and the argument still applies. This proves full-space causal uniqueness without any compact-support or tempering assumption on \(W\).

## The adjugate identity for an arbitrary boundary operator

Fix any polynomial \(B\), with \(b(w,\zeta')=B(w,\zeta')\). On the intersection tube, use [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md)'s residue pairing
\(\beta(a,b)=(2\pi i)^{-1}\int ab/R_+\,dw\).
Let \(M\) be the square boundary matrix with rows
\((\beta(B_j,1),\ldots,\beta(B_j,w^{h-1}))\).
Set
\[
\begin{gathered}
v_B=(\beta(b,1),\ldots,\beta(b,w^{h-1})),\\
\qquad
 (T_1,\ldots,T_h)=v_B\operatorname{adj}M .
\end{gathered}
\tag{14}
\]
Each \(T_k\) is the determinant obtained by replacing row \(k\) of \(M\) by \(v_B\), with the original row order. Hence [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s descent and uniform bound apply to it as to any maximal determinant. Let \(T_{k,0}\) be its inverse, supported in \(C_0\).

Nondegeneracy of the pairing and monic division give the polynomial identity
\[
\begin{gathered}
L^\partial b=\sum_{k=1}^hT_k B_k+R_+S_B,\\
\qquad
 S_B(w,\zeta')=\sum_{r=0}^{R}S_r(\zeta')w^r .
\end{gathered}
\tag{15}
\]
All coefficients are polynomial expressions in the upper-factor and boundary-symbol coefficients, without division by \(L^\partial\). A permissible degree bound is
\[
\begin{gathered}
\deg_w S_B\\
\le\max(\deg_w b,\deg_w B_1,\ldots,\deg_w B_h)-h
\end{gathered}
\];
a negative bound means zero. At \(h=0\), equation 15 holds with \(L^\partial=1\), an empty first sum and \(S_B=b\).

The coefficients \(S_r\) extend holomorphically and with polynomial bounds to the projected tube, using the transported \(R_+\). [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s denominator bound
\(|q(\zeta')|\ge |G(N)|>0\)
on that tube shows that every \(S_r/q\) has the same type of uniform polynomial bound. Here \(G\) is [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)'s localized homogeneous leading polynomial. No inverse minor or reciprocal distance to a cone boundary appears.

## An anti-causal representation, including the empty lower factor

Let \(v\) be smooth on \(H'\), compactly supported there, and set \(f=P(D)v\) on \(a\ge0\). For each fixed \(\zeta'\in\Omega_\cap\), its tangential Fourier–Laplace transform is right Schwartz in \(a\). If \(\ell>0\), the lower-factor inverse is
\[
\begin{gathered}
E_-(y,\zeta')
   \\
=-\frac1{2\pi}\mathbf1_{y\le0}
       \int_{\mathcal C_-}\frac{e^{iyw}}{R_-(w,\zeta')}\,dw .
\end{gathered}
\tag{16}
\]
The finite positively oriented contour surrounds every lower root, including multiplicities. For one root \(\lambda\), this is
\(-i\mathbf1_{y\le0}e^{iy\lambda}\), so
\((D_y-\lambda)E_-=\delta_0\) with \(D=-i\partial\). Products of these kernels give the monic lower-factor inverse; this is [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md)'s explicit negative-support construction. At \(\ell=0\), its inverse is \(\delta_0(y)\), not an omitted contour term.

For \(\ell>0\), define
\[
\begin{gathered}
g(a,\zeta')\\
=q(\zeta')^{-1}
       \\
\int_0^\infty E_-(-r,\zeta')\,f(a+r,\zeta')\,dr .
\end{gathered}
\tag{17}
\]
For \(\ell=0\), put \(g=f/q\). The integral uses only positive-time normal values of the forcing. Differentiation moves every normal derivative onto \(f\), and the exponentially decreasing lower-root kernel makes \(g\) right Schwartz. The equation
\(R_-(D_a)(R_+(D_a)v-g)=0\)
and [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md)'s complete decaying-mode argument show that
\[
                         R_+(D_a)v=g\quad(a\ge0).
 \tag{18}
\]
Indeed the expression is bounded and right Schwartz, and a lower-root homogeneous solution cannot be bounded unless zero. This argument requires no extension of \(f\) to negative \(a\).

Apply equation 15 at \(D_a\) and take the right trace. For \(\ell>0\),
\[
\begin{gathered}
L^\partial(\zeta')B(D_a,\zeta')v(0,\zeta')
   \\
=\sum_{k=1}^h T_k(\zeta')B_k(D_a,\zeta')v(0,\zeta')
     \\
+\sum_{r=0}^{R}\frac{S_r(\zeta')}{q(\zeta')}
           \\
\int_0^\infty E_-(-a,\zeta')D_a^rf(a,\zeta')\,da .
\end{gathered}
\tag{19}
\]
At \(\ell=0\), the final sum is exactly
\(\sum_r(S_r/q)D_a^rf(0,\zeta')\).
This boundary forcing term must be retained.

For each negative \(y\), the product \((S_r/q)E_-(y,\zeta')\) is holomorphic on \(\Omega_\cap\). It has a uniform polynomial frequency bound with factor \(e^{2|y|}\), and likewise for each \(y\)-derivative on bounded negative intervals. To prove it, surround the lower roots by disks of one common radius in \([1,2]\), avoiding finitely many tangencies. Their outer union boundary has length at most \(4\pi\ell\), stays at distance at least one from every root, has \(\operatorname{Im}w<2\), and has polynomially bounded \(|w|\). Thus the denominator modulus is at least one, the exponential is at most \(e^{2|y|}\), and the contour estimate is uniform. [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)/[Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md) control the root modulus and coefficients. Locally fixed contours prove holomorphy separately, including repeated roots.

[Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s flat-tube inverse therefore supplies tangential distribution families \(K_r(y,\cdot)\), smooth for \(y\le0\) from the left, with
\[
\begin{gathered}
\widehat{K_r(y,\cdot)}(\zeta')
       \\
=(S_r/q)(\zeta')E_-(y,\zeta'),\\
\qquad
 \operatorname{supp}K_r
       \\
\subset\{(y,z'):y\le0,\ z'\in D_0\}.
\end{gathered}
\tag{20}
\]
The step at \(y=0\) defines a joint locally integrable distribution-valued family; the left endpoint value does not affect its integral. At \(\ell=0\), instead use the distribution
\(\delta_0(y)\otimes\mathcal F^{-1}(S_r/q)\),
with its boundary action defined by the right trace in equation 19.

Tangential Fourier inversion at any fixed imaginary vector in the intersection cone, and finite normal integration, now give for \(\ell>0\)
\[
\begin{gathered}
L_0*B(D)v|_{a=0}
    \\
=\sum_{k=1}^h T_{k,0}*B_k(D)v|_{a=0}
       \\
+\sum_{r=0}^{R}\int_0^\infty
               \\
K_r(-a,\cdot)*D_a^rP(D)v(a,\cdot)\,da .
\end{gathered}
\tag{21}
\]
The tangential convolutions act in \(x'\). Since \(v\) is compactly supported, only a bounded normal interval and compact input sets occur. The inverse families have bounded distribution order and seminorms on that interval. This justifies inversion, integration and differentiation against compact tests, or equivalently by the smooth-parameter tensor pairing. For \(\ell=0\), replace the integral terms by
\(\mathcal F^{-1}(S_r/q)*D_a^rP(D)v|_{a=0}\).
Formula 21 is the forcing representation, including its empty-factor case.

## Why localization reaches every relevant input

Fix a boundary output \(x'=(z_x,t_x)\), with \(t_x\ge0\). A kernel in equation 21 can see an input \(y=(a,y')\) in the support of \(u\) only if
\[
\begin{gathered}
0\le t_y\le t_x,\\
\qquad
 0\le a\le t_y/\delta,\\
\qquad
 |x'-y'|\le b^{-1}(t_x-t_y).
\end{gathered}
\tag{22}
\]
The second inequality is equation 12. The last is equation 4 applied to the difference \(x'-y'\), which belongs to \(D_0\); the output normal coordinate is zero and the kernel normal support is negative. Thus the relevant inputs form a closed bounded set in \(H'\), hence a compact set. These bounds also hold uniformly for \(x'\) in a small relatively compact output neighborhood. Boundary kernels \(L_0,T_{k,0}\), and the \(\ell=0\) forcing kernels, have their relevant inputs in the \(a=0\) part of the same set.

Choose a compact smooth cutoff \(\chi\) equal to one on a neighborhood of that uniformly enlarged compact set and let \(v=\chi u\) on \(H'\). Right smoothness and compact support suffice for equation 21. On that neighborhood,
\[
          P(D)v=0,\qquad B_k(D)v|_{a=0}=0 .
 \tag{23}
\]
All derivatives of the first expression also vanish there. Away from \(\operatorname{supp}u\), the commutator forcing and its derivatives vanish as well. Thus no input in any kernel's relevant region contributes to the right side of equation 21. Its left side equals \(L_0*B(D)u|_{a=0}\), because \(\chi=1\) near every relevant input. We have proved, locally at every output and hence globally as a smooth function or distribution,
\[
\begin{gathered}
L_0*B(D)u|_{a=0}=0
                     \\
\quad\text{for every polynomial }B.
\end{gathered}
\tag{24}
\]
For negative output time, this equality follows directly from causal support. Convolution is proper throughout this argument: the bounded backward regions justify its usual distributional definition and every derivative. Causal time support alone would not bound the unrestricted normal integration; equation 12 is the needed additional argument.

## Zero extension after every boundary jet vanishes

Set \(U(a,x')=L_0*u(a,\cdot)(x')\) for \(a\ge0\). Its tangential convolution is proper uniformly on compact output sets by equation 4 and the time support. Distributional pairing against the smooth input proves that \(U\) is jointly smooth up to the boundary, and that differentiation commutes with convolution. Taking \(B(w,\zeta')=w^j\) in equation 24 gives
\[
                    D_a^jU|_{a=0}=0\quad(j=0,1,2,\ldots).
 \tag{25}
\]
The same holds after all tangential derivatives. Taylor's integral remainder on compact tangent sets shows that extending \(U\) by zero to \(a<0\) is globally smooth: every derivative tends to zero at the boundary, with arbitrarily high normal powers. Equivalently, the explicit zero-extension formula [equation 16 in Missing boundary rank produces a causal solution](missing-boundary-rank-produces-a-causal-solution.md) has no boundary term at any order.

The extended function has support in \(t\ge0\). The interior equation commutes with the tangential convolution; all boundary jets vanish, so there is no boundary forcing. Therefore on the full space
\[
                         P(D)U=0,\qquad
                         \operatorname{supp}U\subset H .
 \tag{26}
\]
Full-space causal uniqueness proved using equation 13 now gives \(U=0\), proving equation 7. At \(h=0\), this proves \(u=0\). At identically zero determinant, it gives the automatic convolution assertion without inferring uniqueness of \(u\). No nonzero determinant assumption was used in the annihilation theorem.

## Exercises with complete solutions

**Exercise 1 (entry: the normalized wave and two boundary choices).** Take \(P(\xi,s)=(s-i)^2-\xi^2\), \(N=e_s\), \(\theta=e_\xi\). Compare the Dirichlet symbol \(B_1=1\) with \(B_1=\xi+s-i\). Compute each boundary determinant, and reconcile the annihilation theorem with a smooth nonzero homogeneous solution for the second choice.

**Solution.** There is one upper and one lower normal mode. The transported upper factor is \(R_+(w,s)=w+s-i\), with root \(i-s\), and \(q=-1\). The scalar residue pairing evaluates the boundary symbol at this root. Dirichlet data give \(L^\partial=1\), so \(L_0=\delta_0\), and equation 7 forces every smooth causal zero-Dirichlet solution to be zero. For the second symbol, its value at \(w=i-s\) is zero, so \(L^\partial=0\) and equation 7 supplies no uniqueness. Let \(0\ne\rho\in C_c^\infty((0,\infty))\) and set \(u(a,t)=e^{-a}\rho(t-a)\). Direct differentiation gives
\[
\begin{gathered}
(D_a+D_t-i)u=0,\\
\qquad
       P(D)u=0,\\
\qquad
       \operatorname{supp}u\subset\{a\ge0,\ t\ge a\}.
\end{gathered}
\tag{27}
\]
Its boundary condition is exactly zero; its initial jets at \(t=0\) vanish because \(\rho\) vanishes for nonpositive arguments. It is nonzero, in agreement with [Missing boundary rank produces a causal solution](missing-boundary-rank-produces-a-causal-solution.md) and with the zero determinant.

**Exercise 2 (intermediate: the empty lower factor and its forcing term).** For \(P(\xi,s)=\xi+s-i\), take \(B_1=1\) and the arbitrary test operator \(B=\xi\). Derive the boundary formula when the lower factor is empty and check its phase on \(v(a,t)=\phi(a)\psi(t)\), with \(\phi\) smooth and compactly supported on the right half-line and \(\psi\in C_c^\infty(\mathbb R)\).

**Solution.** Here \(h=1,\ell=0,q=1\), \(R_+=w+s-i\), and \(L^\partial=1\). Identity 15 is
\(w=(i-s)+R_+\), so \(T_1=i-s\), \(S_B=1\). Formula 19 becomes
\[
\begin{gathered}
D_av(0,t)\\
=(i-D_t)v(0,t)+f(0,t),
                    \\
\qquad f=P(D)v .
\end{gathered}
\tag{28}
\]
The forcing is
\(f(0,t)=-i\phi'(0)\psi(t)+\phi(0)(D_t-i)\psi(t)\).
The two tangential terms in equation 28 cancel, leaving \(-i\phi'(0)\psi(t)\), exactly its left side. If \(\phi(0)=0\) and \(\phi'(0)\ne0\), dropping the forcing term would give an immediate false identity. The empty lower inverse is a delta distribution, although its empty contour integral is zero.

**Exercise 3 (advanced: why the backward region and the anti-causal phase matter).** First show that time-causal tangential support alone does not make a normal anti-causal convolution proper. Then verify the wave forcing representation for a single complex time frequency and a right-decaying normal amplitude.

**Solution.** In two physical coordinates take the illustrative kernel
\(K(a,t)=\mathbf1_{a\le0}\delta_0(t)\)
and the right-smooth input \(v(a,t)=\rho(t)\) for all \(a\ge0\), where \(\rho\) is a nonnegative nonzero bump in \((1,2)\). At a time where \(\rho(t)>0\), the formal boundary action contains \(\int_0^\infty\rho(t)\,da\), which diverges; the addition map has an unbounded normal preimage even at a fixed output. This kernel is a support illustration, not a claimed factor kernel for a specific equation. Equation 12 would instead restrict all such inputs to \(a\le t/\delta\), exactly the compactness needed in equation 22.

For the wave symbol of Exercise1 and \(B=\xi\), \(T_1=i-s\), \(S_B=1\), \(q=-1\), while the lower root is \(s-i\). Consequently the normal forcing kernel is
\[
\begin{gathered}
K(-r,t)=i e^{-r}\delta(t-r)\\
\quad(r>0),\\
\qquad
     D_av(0,t)=(i-D_t)v(0,t)
           \\
+i\int_0^\infty e^{-r}P(D)v(r,t-r)\,dr .
\end{gathered}
\tag{29}
\]
To check the phase exactly, take \(\alpha>0\), \(\operatorname{Im}s<0\), and \(v(a,t)=e^{-\alpha a}e^{ist}\). This is a frequency check, not a causal solution of the theorem. Put \(A=1+is\), so \(\operatorname{Re}A>1\). Then \(P(D)v=(\alpha^2-A^2)v\). The integral term in equation 29 is
\(i(\alpha^2-A^2)/(\alpha+A)=i(\alpha-A)\)
times \(e^{ist}\), while the boundary term is \((i-s)e^{ist}=iA e^{ist}\). Their sum is \(i\alpha e^{ist}=D_av(0,t)\). The denominator has positive real part, so every integral converges. This checks the orientation, the factor \(q=-1\), the retarded tangential shift and the \(D=-i\partial\) phase.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Open lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, Springer, 1983.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
