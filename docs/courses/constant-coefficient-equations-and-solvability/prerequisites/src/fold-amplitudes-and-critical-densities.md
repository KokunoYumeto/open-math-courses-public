# Fold amplitudes and critical densities

The two projection folds have already been put into an exact canonical model in Canonical relations with two folding projections. We now determine the amplitude order, Fourier constant and invariant half density of that model. We also prove that every distribution on the model, with the stated local support, has an amplitude independent of the input position and the first frequency.

We use the normalized oscillatory integrals of [Oscillatory distributions and their order](oscillatory-distributions-and-order.md), the principal-symbol isomorphism of [Gaussian lines, densities and invariant symbols](gaussian-lines-and-invariant-symbols.md), and the every-order regularity criterion of [Recognizing a Lagrangian distribution intrinsically](intrinsic-lagrangian-regularity.md). Support-preserving symbol summation is imported from [AN-03, Euclidean symbol calculus](https://open-math-course.pages.dev/courses/AN-03/euclidean-symbol-calculus.html), §2, formula (E6). The source context is [Hörmander IV, §25.3, formulas (25.3.7)–(25.3.8)]. All statements below use ordinary symbols \(S^r=S^r_{1,0}\).

## 1. The model and the two amplitude conventions

Let \(n\geq2\), write \(\xi'=(\xi_2,\ldots,\xi_n)\), and put \(\rho=\xi_n>0\). Our canonical relation is parametrized by \((x,s,\xi')\):
\[
\begin{split}
\xi&=\eta=(s^2\rho,\xi'),\\
y_1&=x_1+s,\qquad y_j=x_j\quad(2\leq j<n),\\
y_n&=x_n-s^3/3.
\end{split}
\tag{1.1}
\]
The kernel Lagrangian is \(C'\), with covectors \((\xi,-\eta)\) over \((x,y)\). In particular its base dimension is \(2n\), even though an operator acts on an \(n\)-dimensional space.

Use the convenient cubic expression
\[
\Phi(x,y,s,\xi)=(x-y)\cdot\xi+s\xi_1-s^3\rho/3.
\tag{1.2}
\]
The variable \(s\) has degree zero. The actual homogeneous phase has degree-one auxiliary variables \((\xi,\tau)\), where \(\tau=\rho s\):
\[
\phi(x,y,\xi,\tau)
=(x-y)\cdot\xi+\frac{\tau\xi_1}{\rho}
-\frac{\tau^3}{3\rho^2}.
\tag{1.3}
\]
Its nondegeneracy, including at \(s=0\), was proved in the preceding lesson.

Throughout a cubic amplitude is supported in a fixed compact set of \((x,y,s)\), with \(|s|\leq S\), and in a closed angular cone
\[
\rho\geq1,\qquad |\xi|\leq C\rho.
\tag{1.4}
\]
Bounds on all \(s\) and base derivatives are uniform. Thus \(a\in S^\mu\) in these variables means
\[
|\partial_{x,y}^{\beta}\partial_s^k\partial_\xi^\alpha a|
\leq C_{\alpha\beta k}\rho^{\mu-|\alpha|}.
\tag{1.5}
\]
We work on a slightly larger cone when extending amplitudes. A cutoff at bounded frequency only contributes a smooth kernel.

**Proposition 1.1 (the radial Jacobian and the order).** The normalized kernel integral of order \(m\) is
\[
K_a(x,y)
=(2\pi)^{-n-1/2}\iint e^{i\Phi(x,y,s,\xi)}
a(x,y,s,\xi)\,ds\,d\xi,
\qquad a\in S^{m+1/2}.
\tag{1.6}
\]
Its meaning is the homogeneous oscillatory integral with phase (1.3) and amplitude
\[
\widetilde a(x,y,\xi,\tau)
=\rho^{-1}a(x,y,\tau/\rho,\xi)\in S^{m-1/2}.
\tag{1.7}
\]
These two amplitude conditions are equivalent on the indicated compact parameter sets and cones.

**Proof.** For base dimension \(d=2n\) and \(N=n+1\) homogeneous phase variables, the normalized prefactor and amplitude order are
\[
(2\pi)^{-(d+2N)/4}=(2\pi)^{-n-1/2},
\qquad m+(d-2N)/4=m-\tfrac12.
\tag{1.8}
\]
At fixed \(\xi\), \(d\tau=\rho\,ds\). Hence (1.7) gives precisely (1.6), with no change of the prefactor.

On its support, \(|\tau|\leq S\rho\) and \(|(\xi,\tau)|\asymp\rho\). To check all symbol derivatives, the first frequency derivatives of (1.7) are
\[
\begin{split}
\partial_\tau\widetilde a&=\rho^{-2}a_s,\\
\partial_{\xi_j}\widetilde a&=\rho^{-1}a_{\xi_j}
\quad(j\ne n),\\
\partial_\rho\widetilde a&=-\rho^{-2}a
+\rho^{-1}a_\rho-s\rho^{-2}a_s.
\end{split}
\tag{1.9}
\]
The last line differentiates at fixed \(\tau\). Each auxiliary derivative loses one order; a base derivative loses none. Repeatedly applying these identities gives every higher estimate from finitely many seminorms in (1.5). Factors that depend on \(s\) remain bounded, and differentiating them either introduces \(\rho^{-1}\) or takes another bounded \(s\) derivative.

Conversely,
\[
a(x,y,s,\xi)=\rho\,\widetilde a(x,y,\xi,\rho s).
\tag{1.10}
\]
An \(s\) derivative introduces \(\rho\partial_\tau\), whose two effects cancel in the order. A \(\rho\) derivative at fixed \(s\) introduces \(\partial_\rho+s\partial_\tau\); other frequency derivatives are unchanged. Derivatives of the leading \(\rho\) factor have the corresponding one-order loss. Induction proves (1.5) with \(\mu=m+1/2\). Angular cutoffs are order zero under these same differentiations. The normalized phase-integral theorem therefore gives \(K_a\in I^m(\mathbb R^{2n},C')\). ∎

Counting \(s\) as a homogeneous frequency without changing the integration measure would miss an entire order. The change of variables and the normalized variable count must be used together.

## 2. Computing the critical density

For independent critical equations \(F=0\), the positive critical density is
\[
\delta(F)\,|d(\text{base})\,d(\text{auxiliary})|.
\tag{2.1}
\]
It is computed by choosing coordinates along the critical set and dividing the ambient coordinate density by the absolute normal Jacobian of \(F\). This is the critical-density convention used in the principal-symbol theorem.

First use the nonhomogeneous variables of (1.2). With
\[
F=(\Phi_{\xi_1},\ldots,\Phi_{\xi_n},\Phi_s),
\tag{2.2}
\]
choose tangential coordinates \((x,\xi',s)\) and normal coordinates \((y,\xi_1)\). The first \(n\) rows have \(y\) derivative \(-I_n\). The final row is \(\xi_1-s^2\rho\) and has \(\xi_1\) derivative one and no \(y\) derivative. Thus the absolute normal determinant is one, and
\[
d_{C_\Phi}=|dx\,d\xi'\,ds|.
\tag{2.3}
\]
This is a calculation with independent constraints; it does not treat \(\Phi\) as a homogeneous phase.

**Proposition 2.1 (two radial factors).** In the same critical coordinates,
\[
d_{C_\phi}=\rho^2|dx\,d\xi'\,ds|.
\tag{2.4}
\]
Consequently
\[
\widetilde a|_{C_\phi}\,d_{C_\phi}^{1/2}
=a|_{C_\Phi}\,|dx\,d\xi'\,ds|^{1/2}.
\tag{2.5}
\]

**Proof.** At fixed \(\tau\), put \(s=\tau/\rho\). The homogeneous critical equations satisfy the exact identities
\[
\begin{split}
\phi_{\xi_j}&=\Phi_{\xi_j}\quad(j\ne n),\\
\phi_\rho&=\Phi_\rho-\frac{s}{\rho}\Phi_s,\\
\phi_\tau&=\rho^{-1}\Phi_s.
\end{split}
\tag{2.6}
\]
The constraint change from \(F\) to \(F_h=(\phi_\xi,\phi_\tau)\) has determinant \(\rho^{-1}\). Meanwhile the ambient change \((\xi,s)\mapsto(\xi,\tau)\) has determinant \(\rho\). Delta density therefore contributes one factor \(\rho\), and ambient measure contributes another. This proves (2.4).

One can also calculate directly. Use tangential coordinates \((x,\xi',\tau)\) and the same normal coordinates \((y,\xi_1)\). The normal determinant of \(F_h\) has absolute value \(1/\rho\). Hence
\[
d_{C_\phi}=\rho|dx\,d\xi'\,d\tau|
=\rho^2|dx\,d\xi'\,ds|.
\tag{2.7}
\]
In the last equality, \(d\tau=\rho\,ds+s\,d\rho\); the \(d\rho\) term vanishes in the density Jacobian because \(\rho\) is already among \(\xi'\). Taking the positive square root and using \(\widetilde a=a/\rho\) proves (2.5). ∎

![The two radial Jacobians and their cancellation in the critical symbol](figures/fold-critical-density.svg)

**Figure 2.1.** The ambient measure change supplies \(\rho\), and the inverse constraint determinant supplies \(\rho\). Their product gives the critical density (2.4). Its square root cancels the amplitude factor \(\rho^{-1}\) in (1.7). Every arrow is an exact change of variables, including at the fold. See Propositions 1.1 and 2.1.

## 3. Restriction and the invariant symbol

Restrict the cubic amplitude to the whole critical set:
\[
a_c(x,s,\xi')
=a\bigl(x,(x_1+s,x_2,\ldots,x_{n-1},x_n-s^3/3),
s,(s^2\rho,\xi')\bigr).
\tag{3.1}
\]
The order here is measured in \(\xi'\), with bounded \(s\) derivatives.

**Proposition 3.1.** If \(a\in S^{m+1/2}\) in (1.5), then \(a_c\in S^{m+1/2}\) in \((x,s,\xi')\). In the Maslov frame supplied by \(\phi\), the principal symbol of \(K_a\) is represented by
\[
a_c(x,s,\xi')\,|dx|^{1/2}|d\xi'|^{1/2}|ds|^{1/2}
\quad\bmod S^{m+n/2-1}.
\tag{3.2}
\]
The displayed half density has total order \(m+n/2\).

**Proof.** The substitution in (3.1) is homogeneous in \(\xi'\). A \(\xi'\) derivative takes frequency derivatives of \(a\), with coefficients of order zero. Differentiating \(\xi_1=s^2\rho\) with respect to \(s\) gives \(2s\rho\), whose order one compensates the loss from \(\partial_{\xi_1}a\). Derivatives of the substituted positions are bounded. The same calculation iterated proves every mixed estimate. The restriction stays in a fixed larger angular cone because \(s\) is bounded.

The fixed-phase principal-symbol formula is \(\widetilde a|_{C_\phi}d_{C_\phi}^{1/2}\) in its phase frame. Proposition 2.1 gives exactly (3.2). Under dilation, \(x\) and \(s\) have degree zero, while \(\xi'\) has \(n-1\) degree-one coordinates. The positive frame in (3.2) therefore has degree \((n-1)/2\). Its sum with the scalar order \(m+1/2\) is \(m+n/2\), which is the principal-symbol order for a kernel with base dimension \(2n\). Quotienting by one lower kernel order gives the remainder in (3.2). ∎

The corresponding homogeneous calculation is
\[
\bigl(m-\tfrac12\bigr)+\tfrac{n+1}{2}=m+\tfrac n2.
\tag{3.3}
\]
Both calculations agree. The density is nonsingular at \(s=0\); the vanishing Jacobian of either projection in (1.1) is a different object.

## 4. A phase with fewer variables

Write \(\delta=y_1-x_1\). Define the homogeneous phase in \(n-1\) variables
\[
\Psi(x,y,\xi')
=\sum_{j=2}^n(x_j-y_j)\xi_j-\frac{\delta^3}{3}\rho.
\tag{4.1}
\]
Its critical equations are
\[
x_j=y_j\ (2\leq j<n),\qquad
x_n-y_n=\delta^3/3.
\tag{4.2}
\]
Their \(y_2,\ldots,y_n\) derivatives form \(-I_{n-1}\), so the phase is nondegenerate on \(\rho>0\). On its critical set,
\[
\Psi_x=(\delta^2\rho,\xi'),\qquad
-\Psi_y=(\delta^2\rho,\xi').
\tag{4.3}
\]
Thus it parametrizes the same whole relation, with \(s=\delta\), and its critical density is
\[
d_{C_\Psi}=|dx\,d\delta\,d\xi'|.
\tag{4.4}
\]
For (4.4), use tangential coordinates \((x,y_1,\xi')\), the normal variables \(y_2,\ldots,y_n\), and then \(y_1=x_1+\delta\), whose tangential Jacobian is one.

**Lemma 4.1 (exact hyperbolic elimination).** The two phase frames agree. On a local conic neighborhood of the critical set, the change
\[
\begin{split}
u&=\tau-\rho\delta,\\
v&=\xi_1-\rho\delta^2-\delta u-\frac{u^2}{3\rho}
\end{split}
\tag{4.5}
\]
is a degree-one auxiliary diffeomorphism of determinant one, and
\[
\phi=\Psi+\frac{uv}{\rho}.
\tag{4.6}
\]
The additional phase block has signature zero.

**Proof.** At fixed \(\xi'\) the inverse is
\[
\tau=u+\rho\delta,\qquad
\xi_1=v+\rho\delta^2+\delta u+u^2/(3\rho).
\tag{4.7}
\]
Both directions are smooth on \(\rho>0\), preserve the degree-one auxiliary scaling, and have determinant one. Expansion of the cube in (1.3) gives (4.6) exactly. The added critical equations give \(u=v=0\). At that set their Hessian block is
\[
\begin{pmatrix}0&\rho^{-1}\\ \rho^{-1}&0\end{pmatrix};
\tag{4.8}
\]
its eigenvalues are \(\rho^{-1}\) and \(-\rho^{-1}\). Mixed Hessian entries with \(\xi'\) vanish there. The positive Gaussian determinant factor is \(\rho\), and the signature phase is one. The fixed-phase transition law therefore identifies the two Maslov frames, with no phase rotation. The density and amplitude cancellation is already (2.5). ∎

For a coefficient \(b(x,s,\xi')\) independent of \(y\) and \(\xi_1\), Fourier inversion gives the particularly useful exact identity
\[
\begin{split}
K_b(x,y)
&=(2\pi)^{-n-1/2}
\iint e^{i\Phi(x,y,s,\xi)}b(x,s,\xi')\,ds\,d\xi\\
&=(2\pi)^{-n+1/2}
\int e^{i\Psi(x,y,\xi')}b(x,\delta,\xi')\,d\xi'.
\end{split}
\tag{4.9}
\]
The first line is understood as an iterated distributional integral: integrating \(\xi_1\) produces \(2\pi\delta_0(s-\delta)\). The second line is a standard homogeneous phase integral. Its amplitude order is
\[
m+\frac{2n-2(n-1)}4=m+\tfrac12,
\tag{4.10}
\]
and its prefactor is the one displayed in (4.9). Pairing with a compact smooth test function, Fourier inversion in \(s-\delta\), and the defining remaining oscillatory integral justify the identity. If compact base support is needed, insert a smooth cutoff equal to one near the compact base image of the critical support. Removing that cutoff changes only a smooth kernel.

This calculation is valid through the fold: it never divides by \(s\).

## 5. The omitted first-frequency cone is smooth

The first line of (4.9) does not have compact angular support in \(\xi_1\). We must justify comparing it with (1.6), rather than silently treating an amplitude constant in \(\xi_1\) as a symbol in all \(n+1\) homogeneous variables.

**Lemma 5.1 (the first-frequency tail).** Suppose \(b(x,s,\xi')\in S^\mu\), with compact \(x,s\) support, \(|s|\leq S\), and
\[
\rho\geq1,\qquad |\xi'|\leq C'\rho.
\tag{5.1}
\]
Choose \(M>2S^2\) and a smooth \(\chi\) equal to one for \(|t|\leq M\) and zero for \(|t|\geq2M\). Then
\[
T(x,\xi)=
\int e^{i(s\xi_1-s^3\rho/3)}
\bigl(1-\chi(\xi_1/\rho)\bigr)b(x,s,\xi')\,ds
\in S^{-\infty}(x,\xi).
\tag{5.2}
\]
It follows that inserting \(\chi(\xi_1/\rho)\) in the first line of (4.9) changes its kernel by a smooth function.

**Proof.** On the tail,
\[
F=\partial_s(s\xi_1-s^3\rho/3)=\xi_1-s^2\rho,
\qquad |F|\geq|\xi_1|/2.
\tag{5.3}
\]
Also \(|\xi|\asymp|\xi_1|\), since \(|\xi'|\leq C'\rho\leq(C'/M)|\xi_1|\). With \(L=(iF)^{-1}\partial_s\), \(Le^{i(s\xi_1-s^3\rho/3)}=e^{i(s\xi_1-s^3\rho/3)}\). Compact \(s\) support removes every boundary term. Each application of \(L^t=-\partial_s(\,\cdot\,/(iF))\) introduces one factor of order \(|\xi_1|^{-1}\). Indeed the derivatives \(\partial_sF=-2s\rho\) and \(\partial_s^2F=-2\rho\) are \(O(|\xi_1|)\), and higher ones vanish. Repeated differentiation of \(F^{-1}\) therefore has the same order \(|\xi_1|^{-1}\), with bounds depending on the fixed \(s\) interval.

For any fixed set of base and frequency derivatives of (5.2), differentiating its exponential only inserts bounded powers of \(s\) and \(s^3\). Derivatives of the angular cutoff occur where \(|\xi_1|\asymp\rho\), and have the usual frequency-order losses. Every derivative of \(b\) needed at a fixed stage is bounded by a constant times \(\rho^{\max(\mu,0)}\), because \(\rho\geq1\). After \(N\) integrations by parts the resulting integrand is therefore bounded by
\[
C_{\alpha\beta N}|\xi_1|^{\max(\mu,0)-N}
\tag{5.4}
\]
on a fixed compact \(s\) interval. This also bounds its integral. Given any decay order and any finite derivative set, choose \(N\) larger than their required decay exponent plus \(\max(\mu,0)\). Thus all differentiated estimates of \(S^{-\infty}(x,\xi)\) hold.

The tail kernel is the inverse Fourier integral of (5.2), times the fixed normalization. Arbitrarily rapid decay permits all base derivatives under the integral, so it is smooth. The region of bounded \(\xi'\), if it is present before the cutoff \(\rho\geq1\), is already smooth by the second line of (4.9); equivalently the compact \(s\) Fourier transform decays rapidly in \(\xi_1\). ∎

In particular the conically truncated amplitude
\[
a(x,s,\xi)=\chi(\xi_1/\rho)b(x,s,\xi')
\tag{5.5}
\]
has the ordinary order \(\mu\) on \(|\xi|\leq C''\rho\), including all \(s\) derivatives. At every critical point of its support, \(\xi_1/\rho=s^2\) and \(\chi=1\). Propositions 1.1–3.1 therefore apply to the whole distribution (4.9), modulo its smooth tail.

## 6. Every local model kernel has a reduced amplitude

Here “compactly generated” means that the intersection with a frequency dilation slice lies in a compact subset of the stated coordinate chart. In the model parameters this gives a compact set of \(x,s\) and angular \(\xi'\), with closure in \(\rho>0\). Choose a slightly larger compact parameter set and cone, still inside the chart. All coefficients below may be supported there.

**Theorem 6.1 (full reduced-amplitude representation).** Let
\[
A\in I^m(\mathbb R^{2n},C')
\tag{6.1}
\]
and suppose its entire wavefront set is contained in a compactly generated subset of the model chart, inside the preceding smaller set. Modulo a smooth kernel there is a coefficient
\[
b(x,s,\xi')\in S^{m+1/2}
\tag{6.2}
\]
supported in the chosen larger compact parameter set and cone, for which \(A=K_b\) in (4.9). Equivalently, for compact smooth inputs and with
\(\widehat f(\xi)=\int e^{-iy\cdot\xi}f(y)\,dy\),
\[
(K_bf)(x)=(2\pi)^{-n-1/2}
\iint e^{i(x\cdot\xi+s\xi_1-s^3\rho/3)}
b(x,s,\xi')\widehat f(\xi)\,ds\,d\xi.
\tag{6.3}
\]
The integral in (6.3) is absolutely convergent for these inputs. Its principal symbol is (3.2) with \(a_c=b\). Properly supported local versions are obtained by the base cutoff described after (4.9).

**Proof.** By (4.1)–(4.4), \(K_b\) is a nondegenerate phase integral of order \(m\) whenever \(b\) has order \(m+1/2\). Its principal-symbol map, in the common phase frame, is
\[
b\longmapsto b\,|dx\,ds\,d\xi'|^{1/2}.
\tag{6.4}
\]
This realizes every local symbol class of total order \(m+n/2\). In fact dividing such a section by the positive frame gives an ordinary scalar symbol of order
\[
(m+n/2)-(n-1)/2=m+1/2.
\tag{6.5}
\]
The model parametrization is a diffeomorphism onto the relation, so this scalar coefficient is a smooth function of precisely \((x,s,\xi')\). No extension in additional base variables is needed.

Choose a representative \(b_0\) for the principal symbol of \(A\), supported in the larger parameter set and rapidly decreasing, with all derivatives, on closed parameter cones disjoint from \(\operatorname{WF}(A)\). These properties follow from the microlocal symbol construction: in the compact cosphere cover used for the principal-symbol theorem, take every localization inside that larger set. The coefficient in a frequency graph is extracted from the localized distribution's Fourier transform. Where the distribution is microlocally smooth, this coefficient and all its fixed derivatives are rapidly decreasing. The smooth changes of critical coordinates, density frames and Maslov frames preserve rapid decrease. A cutoff equal to one near the smaller wavefront set therefore discards only rapidly decreasing coefficients. The partition can be finite over the compact parameter support.

The phase wavefront theorem, applied after a partition into rapidly decreasing and nonstationary pieces, now gives \(\operatorname{WF}(K_{b_0})\subset\operatorname{WF}(A)\). The symbols agree, and the kernel assertion of the principal-symbol theorem gives
\[
R_1=A-K_{b_0}\in I^{m-1}.
\tag{6.6}
\]
Its wavefront set is contained in \(\operatorname{WF}(A)\).

Repeat this construction for the residual, choosing all coefficients in one fixed larger support set. Inductively there are
\[
b_j\in S^{m+1/2-j},\qquad
R_N=A-\sum_{j<N}K_{b_j}\in I^{m-N}.
\tag{6.7}
\]
At each step choose the coefficient with the same rapid-decrease property off the residual's wavefront set. The preceding phase wavefront argument then gives \(\operatorname{WF}(R_N)\subset\operatorname{WF}(A)\) by induction. A single cutoff equal to one near that fixed wavefront set, supported in the chosen larger parameter box and cone, can therefore be used at every stage; every discarded coefficient is rapidly decreasing. This keeps the support set fixed without successive enlargement.

Apply the imported support-preserving asymptotic summation theorem to the symbols \(b_j\), with \((x,s)\) as base parameters and \(\xi'\) as frequency variables. Compact parameter support makes its usual uniform base seminorms applicable. It gives a symbol \(b\) supported in their common set with
\[
b-\sum_{j<N}b_j\in S^{m+1/2-N}
\quad\text{for every }N.
\tag{6.8}
\]
The already proved phase-order formula places the corresponding \(K\) difference in \(I^{m-N}\). Combining with (6.7) shows
\[
A-K_b\in\bigcap_{N\geq0}I^{m-N}=C^\infty.
\tag{6.9}
\]
The last equality is the every-order regularity result proved in the intrinsic lesson. More directly, its empty-word condition puts the localized remainder in Besov spaces of every order, hence in Sobolev spaces of every finite order; local Sobolev embedding gives smoothness.

Finally Fourier inversion in the first frequency, as in (4.9), identifies this \(K_b\) with its cubic integral, and integration against the input yields (6.3). A compact smooth input has a Schwartz Fourier transform, whereas \(b\) has polynomial growth and compact \(s\) support; absolute convergence follows. The first-frequency tail in Lemma 5.1 justifies the comparison with the conic \(n+1\)-variable representation. Thus both descriptions have the claimed order and the same invariant symbol. ∎

The argument proves representation for the entire local model class, rather than only for amplitudes initially written with \(\phi\). It uses the already established symbol theorem and asymptotic summation at every lower order. General stable equivalence of arbitrary phase functions is a separate theorem; it is not a premise of this particular construction.

## 7. Exact normalization examples

Take smooth compact cutoffs \(\beta(x)\) and \(\gamma(s)\), and an angular cutoff \(\omega(\xi'/\rho)\), supported in a compact subset of the cone \(\rho>0\). At high frequency set
\[
b(x,s,\xi')=\beta(x)\gamma(s)\omega(\xi'/\rho)\rho^{m+1/2}.
\tag{7.1}
\]
Include a smooth low-frequency cutoff in \(\rho\). This is an ordinary symbol of the required order: derivatives of the angular ratios lose one frequency order, whereas \(x,s\) derivatives affect only compact smooth cutoffs.

Its reduced kernel is
\[
(2\pi)^{-n+1/2}\int
e^{i\Psi(x,y,\xi')}
\beta(x)\gamma(y_1-x_1)\omega(\xi'/\rho)
\rho^{m+1/2}\,d\xi'.
\tag{7.2}
\]
Its symbol is (7.1) times the positive frame of (3.2). On any patch where the cutoffs are one this symbol is elliptic, including points with \(s=0\). Ellipticity refers to its coefficient on the Lagrangian; neither projection needs to be invertible there.

For \(n=2\) and \(m=-1/6\), the scalar amplitude order is \(1/3\), the homogeneous \(3\)-variable amplitude order is \(-2/3\), and the symbol half-density order is \(5/6\):
\[
\tfrac13+\tfrac12=\tfrac56
=-\tfrac23+\tfrac32.
\tag{7.3}
\]
These orders are an illustration of the normalization. No continuity conclusion follows from these counts alone; the Airy estimates needed for the fold bound will be proved separately.

## 8. Exercises with complete solutions

**Exercise 8.1 (kernel variable count; introductory).** For \(n=3\) and kernel order \(m=-1/4\), compute the two amplitude orders, the two normalized prefactors, and the total symbol order.

**Solution.** The base dimension is six. The \(n+1=4\) homogeneous variables give amplitude order \(-1/4-1/2=-3/4\) and prefactor \((2\pi)^{-7/2}\). In cubic coordinates the amplitude has order \(-1/4+1/2=1/4\), with the same prefactor. The reduced phase has \(n-1=2\) variables and prefactor \((2\pi)^{-5/2}\), while its amplitude still has order \(1/4\). The frame \(|dx\,ds\,d\xi'|^{1/2}\) has degree one, so the symbol order is \(1/4+1=5/4=m+n/2\). In the homogeneous description the frame degree is two, giving \(-3/4+2=5/4\).

**Exercise 8.2 (a different radial coordinate; intermediate).** Replace \(\tau=\rho s\) by \(\tau=r(\xi)s\), where \(r\) is positive, smooth and homogeneous of degree one on the cone, and \(r\asymp\rho\). Determine the amplitude and critical-density changes without assuming \(r=\xi_n\).

**Solution.** At fixed \(\xi\), the measure changes by \(r\), so \(\widetilde a=a/r\). At fixed \(\tau\), the frequency constraint vector becomes
\[
F_h=\left(\Phi_\xi-\frac{s}{r}r_\xi\Phi_s,\,
\frac{\Phi_s}{r}\right).
\]
The displayed constraint matrix has determinant \(1/r\). Its inverse delta Jacobian contributes \(r\), while ambient measure contributes \(r\). Thus \(d_{C_h}=r^2d_{C_\Phi}\) and \(\widetilde a\,d_{C_h}^{1/2}=a\,d_{C_\Phi}^{1/2}\). Positivity fixes the square root. The comparability and homogeneous derivative bounds for \(r\) give the same symbol equivalence by the chain rule, since \(\partial_\xi(\tau/r)=-s\,r_\xi/r\) has order \(-1\), and \(\partial_\tau(\tau/r)=r^{-1}\).

**Exercise 8.3 (restriction with an \(s\) derivative; intermediate).** For a general amplitude \(a(x,y,s,\xi)\), write \(\partial_s a_c\) explicitly and explain why it has the same order as \(a_c\).

**Solution.** The chain rule on (3.1) gives
\[
\partial_sa_c
=\bigl(a_s+a_{y_1}-s^2a_{y_n}
+2s\rho\,a_{\xi_1}\bigr)\big|_{C_\Phi}.
\]
The first three derivatives have the original order, and their scalar coefficients are bounded on the fixed \(s\) interval. The frequency derivative has one lower order, which is restored by \(\rho\). Hence the expression has order \(m+1/2\). Higher \(s\) derivatives differentiate these same coefficients and substitutions; each additional frequency derivative is accompanied by at most the corresponding power of \(\rho\), so the order remains unchanged.

**Exercise 8.4 (a missing density factor; intermediate).** An incorrect computation uses \(\widetilde a=a/\rho\) but claims \(d_{C_\phi}=\rho\,d_{C_\Phi}\). What coefficient does it assign to the symbol, and which Jacobian has it omitted?

**Solution.** It assigns \(a\rho^{-1/2}d_{C_\Phi}^{1/2}\), which is one half order below the actual symbol. This is an error in the claimed symbol, rather than a change to the kernel already defined. It omits one radial factor: after computing the normal constraint determinant \(1/\rho\), the density is \(\rho|dx\,d\xi'\,d\tau|\); replacing \(d\tau\) by \(\rho\,ds\) supplies the second factor. Conversely an ambient-only calculation would omit the inverse constraint determinant. Both are required.

**Exercise 8.5 (the reduced phase at the fold; intermediate).** In dimension two, compute all base covector components and the critical density of \(\Psi=(x_2-y_2)\rho-(y_1-x_1)^3\rho/3\). Verify nondegeneracy at \(y_1=x_1\).

**Solution.** With \(\delta=y_1-x_1\), the covectors are \(\Psi_x=(\delta^2\rho,\rho)\) and \(-\Psi_y=(\delta^2\rho,\rho)\). The sole critical equation is \(x_2-y_2-\delta^3/3=0\). Its \(y_2\) derivative is \(-1\), including at \(\delta=0\); its differential never vanishes. In critical coordinates \((x_1,x_2,\delta,\rho)\), the normal Jacobian is one, so the density is \(|dx_1\,dx_2\,d\delta\,d\rho|\). The vanishing of the derivative of \(\delta^2\rho\) in the fold direction does not affect independence of this phase-critical equation.

**Exercise 8.6 (the hyperbolic signature; intermediate).** Verify the auxiliary inverse in (4.7), its determinant and its stationary Gaussian constant. Explain how it accounts for the prefactor difference in (4.9).

**Solution.** Substituting \(\tau=u+\rho\delta\) into (4.5) gives \(u\), and substituting the proposed \(\xi_1\) then gives \(v\). At fixed \(\xi'\) the inverse Jacobian in \((v,u)\) has diagonal entries one and lower off-diagonal entry zero, hence determinant one. The quadratic block \(uv/\rho\) has determinant \(-\rho^{-2}\) and signature zero, so the real two-variable Gaussian factor is \(2\pi\rho\). The homogeneous amplitude at \(u=v=0\) is \(b/\rho\). Their product is \(2\pi b\), changing \((2\pi)^{-n-1/2}\) to \((2\pi)^{-n+1/2}\). The phase factor is one, in agreement with the exact first-frequency Fourier inversion.

**Exercise 8.7 (the tail requires a support hypothesis; advanced).** In Lemma 5.1 take \(S=1\) and \(M=3\). Give a lower bound for \(|F|\) on the tail. Explain why the same argument fails for an amplitude whose \(s\) support is unrestricted.

**Solution.** On the tail \(|\xi_1|\geq3\rho\) and \(s^2\rho\leq\rho\), so \(|F|\geq|\xi_1|-\rho\geq2|\xi_1|/3\), which is stronger than (5.3). If \(s\) is unrestricted and \(\xi_1>0\), the stationary points \(s=\pm\sqrt{\xi_1/\rho}\) lie in the putative tail. There is then no denominator bound and integration by parts with \(1/F\) is invalid there. Compact \(s\) support is what puts those stationary points outside the amplitude support when the first frequency is sufficiently large. The noncompact Airy integral needs its own tail argument with different support conditions.

**Exercise 8.8 (a symbol-zero kernel; advanced).** Suppose \(A\in I^m(C')\) has zero principal symbol. What does this imply, and why does it not immediately imply that \(A\) is smooth?

**Solution.** The kernel of the principal-symbol map is \(I^{m-1}(C')\), so only one order is lost. For example a reduced amplitude elliptic of order \(m-1+1/2\) defines an element of \(I^{m-1}\) with a nonzero symbol at that lower order. It is also in \(I^m\) with zero order-\(m\) symbol, yet it is not smooth: its lower-order elliptic symbol prevents membership in every smaller order. To obtain smoothness in Theorem 6.1, the residual must belong to \(I^{m-N}\) for every \(N\), not just \(N=1\).

**Exercise 8.9 (why the asymptotic sum uses fewer frequencies; advanced).** Identify the base and frequency variables to which (E6) is applied in Theorem 6.1. Show that its remainder gives the desired kernel remainder order.

**Solution.** The base parameters are \((x,s)\), all in a fixed compact set, and the frequency variables are \(\xi'\in\mathbb R^{n-1}\). We sum \(b_j\in S^{m+1/2-j}\) there, rather than summing coefficients constant in \(\xi_1\) as if they were symbols on all of \(\mathbb R^n\). The resulting remainder has scalar order \(m+1/2-N\). In the reduced phase, the kernel order equals scalar order minus \((2n-2(n-1))/4\), namely \(m-N\). Consequently both remainders in (6.9) have that order for each \(N\). Lemma 5.1 supplies the separate comparison with the full first-frequency integral.

**Exercise 8.10 (proper localization; advanced).** For \(b\) with compact \(x,s\) support as in Theorem 6.1, choose a compact base cutoff \(q(x,y)\) equal to one near the base image of the critical support. Show that \(K_b-qK_b\) is smooth and explain why its symbol is unchanged.

**Solution.** The critical base image is compact: \(y\) is determined by the continuous formulas (1.1) from compact \(x,s\) sets. Choose \(q=1\) on a neighborhood of that image and compactly supported in a larger base box. On the support of \(1-q\), the compactly generated critical support is absent. The nondegenerate phase-integral wavefront theorem therefore gives no wavefront points there; equivalently, on each compact base set disjoint from that image, the phase gradient has a positive lower bound on the closed angular support and repeated integration by parts gives a smooth kernel with all derivatives. Thus \((1-q)K_b\) is smooth. Since \(q=1\) on the critical support, its restriction multiplies (6.4) by one, so the symbol is unchanged. The localized kernel has compact base support and is properly supported.

## References

- [Hörmander IV, §25.3, formulas (25.3.7)–(25.3.8)] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, Springer, 1985, §25.3.
- [AN-03, Euclidean symbol calculus](https://open-math-course.pages.dev/courses/AN-03/euclidean-symbol-calculus.html), §2, support-preserving summation theorem (E6).

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Original text: public domain (CC0).*
