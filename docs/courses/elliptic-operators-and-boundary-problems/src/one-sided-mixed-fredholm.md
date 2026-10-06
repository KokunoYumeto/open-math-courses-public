# When finite defects force one-sided ellipticity

*Written and dedicated to the public domain by Codex, September 2026 (CC0).*

A closed range with only finitely many null solutions forces a pseudodifferential symbol to be injective at high frequency. A range with only finitely many missing targets forces the separate surjective condition. The two need not coincide for a rectangular system. This lesson proves both directions, then carries every source and target weight through a mixed-order system. It ends with an example showing exactly why an adapted graph domain changes the conclusion.

The required entry results are [Finite defects under perturbation](fredholm-stability.md), [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md), and [Symbols, finite defects, and the index on a closed manifold](global-elliptic-symbol-index.md). Their compactness, complete symbol composition, and order-changing maps are recalled at the points where they enter. We use \(D=-i\partial\), retain every matrix factor in its source-to-target order, and never identify distinct bundle fibers without the stated Hermitian metric.

## 1. Objects and the four one-sided assertions

Let \(X\) be a compact smooth manifold without boundary. Let \(E,F\) be finite-rank complex Hermitian bundles, with their half-density factors retained in the Sobolev spaces. Fix \(m,s\in\mathbb R\) and
\[
 P\in\Psi^m(X;E\otimes\Omega_X^{1/2},F\otimes\Omega_X^{1/2}),
 \qquad
 P_s:H^s(X;E\otimes\Omega_X^{1/2})
       \longrightarrow H^{s-m}(X;F\otimes\Omega_X^{1/2}).
 \tag{OM1}
\]
Here \(\Psi^m\) has the \(S^m_{1,0}\) full-symbol bounds in local bundle frames, and \(p\in S^m/S^{m-1}\) is its original principal class. A representative \(p\) is used when writing a pointwise high-frequency inequality. Changing representatives changes it by \(S^{m-1}\), so the inequalities below are independent of that choice after increasing the lower frequency cutoff. The positive function \(\langle\xi\rangle\) is defined by one fixed Riemannian cotangent metric; the original \(p\), its bundle maps and all orders remain explicit.

The left condition is
\[
 \|p(x,\xi)w\|_F\ge c\langle\xi\rangle^m\|w\|_E
 \quad (|\xi|\ge R,\ w\in E_x).
 \tag{OM2}
\]
The right condition is the corresponding lower bound for the actual Hermitian adjoint \(p(x,\xi)^*:F_x\to E_x\):
\[
 \|p(x,\xi)^*v\|_E\ge c'\langle\xi\rangle^m\|v\|_F
 \quad (|\xi|\ge R',\ v\in F_x).
 \tag{OM3}
\]
These conditions allow unequal ranks. The left one says injectivity with a uniform high-frequency bound, and the right one says surjectivity with a uniform high-frequency bound. Neither implies the other for a rectangular bundle map.

## 2. Finite kernel and closed range give a compact-error estimate

Assume \(P_s\) has finite-dimensional kernel \(N\) and closed range. The restriction to the orthogonal complement \(N^\perp\subset H^s(E)\) is a bounded bijection onto \(\operatorname{ran}P_s\). Both are Hilbert spaces, so the bounded inverse theorem gives
\[
 \|u\|_{H^s}
 \le C\bigl(\|P_su\|_{H^{s-m}}+\|\Pi_Nu\|_{H^s}\bigr).
 \tag{OM4}
\]
The projection \(\Pi_N\) is finite rank and compact; no smoothness of \(N\) has been assumed.

The same hypotheses give the lower-order estimate required in the original Sobolev spaces:
\[
 \|u\|_{H^s}
 \le C_s\bigl(\|P_su\|_{H^{s-m}}+\|u\|_{H^{s-1}}\bigr).
 \tag{OM5}
\]
If this failed, choose \(u_j\) with \(\|u_j\|_{H^s}=1\) and both terms on the right tending to zero. Equation (OM4) shows \(\operatorname{dist}_{H^s}(u_j,N)\to0\). Choose \(n_j\in N\) with \(\|u_j-n_j\|_{H^s}\to0\). The continuous inclusion \(H^s\hookrightarrow H^{s-1}\) gives \(\|n_j\|_{H^{s-1}}\to0\). Its restriction to the finite-dimensional \(N\) is injective, so its \(H^{s-1}\) and \(H^s\) norms on \(N\) are equivalent. Thus \(\|n_j\|_{H^s}\to0\), contradicting \(\|u_j\|_{H^s}=1\). This argument does not silently make the unknown kernel smooth.

## 3. A local wave packet tests the complete original principal map

We record the quantitative packet fact used to derive (OM2). Let \(A\in\Psi^0(X;E,F)\), with complete local symbol \(a(x,\eta)\), and choose a smaller chart whose closure lies in one bundle trivialization. Let \(\lambda=|\xi_\lambda|\to\infty\), with \(x_\lambda\) in that smaller chart, and let \(w_\lambda\) be a unit vector in its local input frame. Choose \(\chi\in C_c^\infty(\mathbb R^n)\) with \(\|\chi\|_2=1\), and set
\[
 v_\lambda(x)
  =\lambda^{n/4}\chi\!\left(\lambda^{1/2}(x-x_\lambda)\right)
     e^{\,i\langle x-x_\lambda,\xi_\lambda\rangle}w_\lambda .
 \tag{OM6}
\]
The coefficient in (OM6) is written in the coordinate half-density
frame \(|dx|^{1/2}\), using the stated input and output bundle frames.
The unit condition means
\(w_\lambda^\dagger H_E(x_\lambda)w_\lambda=1\) in the original
input metric at the center. The norm of the constant output matrix in
(OM7) is taken in the specified output frame. The complete calculation
below retains the fixed cotangent metric and its chart comparison
constants; it includes the frequency derivatives needed for the operator
estimate, not only the base derivatives.

The half-density and frame metrics vary smoothly on the shrinking support, so
\[
 \|v_\lambda\|_{L^2}=1+O(\lambda^{-1/2}),\qquad
 v_\lambda\rightharpoonup0\text{ in }L^2,\qquad
 \|Av_\lambda-a(x_\lambda,\xi_\lambda)v_\lambda\|_{L^2}
       =O(\lambda^{-1/2}).
 \tag{OM7}
\]
The weak limit follows by Cauchy–Schwarz on a shrinking ball for each fixed \(L^2\) test, first for bounded smooth tests and then by density.

For completeness, the last bound has two exact parts. On the support of \(v_\lambda\), the mean-value formula and the uniform \(x\)-derivatives of \(a\) give
\(\|(a(x,\xi_\lambda)-a(x_\lambda,\xi_\lambda))v_\lambda\|_2
 =O(\lambda^{-1/2})\).
The Fourier transform of the packet is centered at \(\xi_\lambda\), with width \(\lambda^{1/2}\). Cut it to \(|\eta-\xi_\lambda|\le\lambda/2\); the complementary Schwartz tail is \(O(\lambda^{-N})\) in every fixed Sobolev norm, for every \(N\). On the cut region the exact integral identity
\[
 a(x,\eta)-a(x,\xi_\lambda)
 =\sum_{r=1}^n(\eta_r-\xi_{\lambda,r})
   \int_0^1\partial_{\eta_r}a
       (x,\xi_\lambda+\theta(\eta-\xi_\lambda))\,d\theta
 \tag{OM8}
\]
has coefficient symbols with every fixed \(x\)-derivative bounded by \(C\lambda^{-1}\). The finite-derivative \(L^2\) symbol estimate from the linked symbol-calculus lesson, applied after the frequency cutoff, and
\(\|(D-\xi_\lambda)v_\lambda\|_2=O(\lambda^{1/2})\)
give \(O(\lambda^{-1/2})\). Operators cut off away from the coordinate diagonal have smooth kernels; repeated integration by parts in the packet's oscillation bounds their output by \(O(\lambda^{-N})\) for each \(N\). This proves (OM7), uniformly in the selected chart. A finite chart cover provides uniformity on \(X\).

### The complete coordinate packet proof

The operator bound used here is [the full finite-derivative symbol estimate](euclidean-symbol-calculus.md), (E23), proved there in (E24)--(E27) and (EC12)--(EC14). Its derivative count can be taken as \(L_n=4N_0\), with an integer \(N_0>n/2\). The Fourier conventions are (E10), and the exact kernel reconstruction is (E12).

### 1. Exact objects, metrics, density and local realization

Let \(X\) be the original compact smooth manifold without boundary,
and let \(E,F\) be the original complex Hermitian bundles. Keep their
half-density factors. Let
\[
 A\in\Psi^0_{1,0}
 (X;E\otimes\Omega_X^{1/2},F\otimes\Omega_X^{1/2}).
 \tag{PW1}
\]
We give the proof on a component of dimension \(n\geq1\).
A zero-dimensional component has no covectors tending to infinity
and consequently contributes no packet sequence to the necessity argument.

Choose one coordinate chart \(x=(x_1,\ldots,x_n)\), input and output
bundle frames, and nested relatively compact open subsets
\[
 K\subset U_0,\qquad
 \overline {U_0}\subset U_1,\qquad
 \overline {U_1}\subset U_2,\qquad
 \overline {U_2}\subset U ,
 \tag{PW2}
\]
where \(K\) is compact and every packet center \(x_\lambda\) belongs
to \(K\). Choose fixed smooth cutoffs \(\psi,\zeta\), with
\(\psi=1\) near \(\overline {U_0}\), \(\operatorname{supp}\psi\subset
U_1\), \(\zeta=1\) near \(\overline {U_1}\), and
\(\operatorname{supp}\zeta\subset U_2\).
Use the coordinate half-density frame \(|dx|^{1/2}\).
Write \(H_E(x),H_F(x)\) for the positive Hermitian metric matrices
in the two specified frames. Thus, with the Hermitian pairing linear
in its first variable,
\[
 h_E(u,v)=v^\dagger H_E(x)u,\qquad
 \|u(x)|dx|^{1/2}\|_{L^2(E)}^2
       =\int u(x)^\dagger H_E(x)u(x)\,dx .
 \tag{PW3}
\]
There is no missing density multiplier in PW3: the square of the
chosen half-density is exactly \(|dx|\). Under another coordinate
system \(y=\Phi(x)\), the coefficient transforms with
\(|\det D\Phi^{-1}(y)|^{1/2}\); squaring that factor and changing
variables preserves precisely PW3. Bundle frame changes transform
the matrices and coefficients together, preserving the same integral.

On the compact coordinate region let
\[
 0<h_E^-\leq\lambda_{\min}(H_E(x)),\qquad
 0<h_F^-\leq\lambda_{\min}(H_F(x)),\qquad
 \lambda_{\max}(H_E(x))\leq h_E^+,\quad
 \lambda_{\max}(H_F(x))\leq h_F^+ .
 \tag{PW4}
\]
All metric derivatives used below have finite suprema there.
Write \(|\eta|_{\rm c}\) for the Euclidean coordinate covector norm
and keep \(|\eta|_{g,x}\) for the fixed Riemannian cotangent norm
already chosen in OM1. There are fixed constants
\[
 0<\kappa_-\leq\kappa_+,\qquad
 \kappa_-|\eta|_{\rm c}\leq|\eta|_{g,x}
       \leq\kappa_+|\eta|_{\rm c}.
 \tag{PW5}
\]
For example their squares can be taken as the minimum and maximum
of the eigenvalues of the coordinate cotangent metric matrix on
the compact region. These are exact inequalities between the two
original norms.

Let \(a(x,\eta)\) be a complete local left symbol for \(A\), with
all the original \(S^0_{1,0}\) bounds
\[
 \|\partial_x^\alpha\partial_\eta^\beta a(x,\eta)\|
      \leq M_{\alpha,\beta}\langle\eta\rangle_{\rm c}^{-|\beta|},
 \qquad
 \langle\eta\rangle_{\rm c}=(1+|\eta|_{\rm c}^2)^{1/2}.
 \tag{PW6}
\]
Its source and target coordinate dimensions are kept distinct.
The local realization of the pseudodifferential class means
\(\zeta A\psi=\zeta\operatorname{Op}(a)\psi+R\), where \(R\)
has a smooth localized kernel. Here left quantization is exactly
\[
 \widehat u(\eta)=\int e^{-ix\cdot\eta}u(x)\,dx,\qquad
 \operatorname{Op}(a)u(x)=(2\pi)^{-n}
       \int e^{ix\cdot\eta}a(x,\eta)\widehat u(\eta)\,d\eta ,
 \qquad D_r=-i\partial_{x_r}.
 \tag{PW7}
\]
These are E10's conventions. Put \(\widetilde a=\zeta a\), extended
by zero outside the chart. It is a global Euclidean \(S^0_{1,0}\)
symbol. The exact derivative formula is
\[
 \partial_x^\alpha\partial_\eta^\beta\widetilde a
  =\sum_{\nu\leq\alpha}{\alpha\choose\nu}
       (\partial_x^\nu\zeta)
       (\partial_x^{\alpha-\nu}\partial_\eta^\beta a).
 \tag{PW8}
\]
This retains every output-cutoff contribution. In particular PW6
holds for \(\widetilde a\), with new fixed constants
\(\widetilde M_{\alpha,\beta}\) bounded by the finite sum in PW8.

### 2. The packet and its exact norm and Fourier transform

Keep the original packet profile
\(\chi\in C_c^\infty(\mathbb R^n)\) with
\(\int|\chi(z)|^2\,dz=1\), and put
\(R_\chi=\sup\{|z|_{\rm c}:z\in\operatorname{supp}\chi\}\).
For the original fixed metric define
\[
 \lambda=|\xi_\lambda|_{g,x_\lambda}\longrightarrow\infty,
 \qquad w_\lambda^\dagger H_E(x_\lambda)w_\lambda=1.
 \tag{PW9}
\]
The second equality is the meaning of unit vector needed in OM6.
It does not require an orthonormal coordinate frame.
It gives \(|w_\lambda|_{\rm c}^2\leq(h_E^-)^{-1}\).
For all sufficiently large \(\lambda\), the packet support is
contained in \(U_0\), uniformly over \(x_\lambda\in K\).
The actual section, with the local frame identifications made explicit,
is
\[
 v_\lambda(x)=
  \lambda^{n/4}\chi\!\left(\sqrt\lambda(x-x_\lambda)\right)
  e^{\,i(x-x_\lambda)\cdot\xi_\lambda}
  w_\lambda\,|dx|^{1/2}.
 \tag{PW10}
\]
The local bundle frame multiplying \(w_\lambda\) is understood in
PW10, and the section is extended by zero. Its exact norm is
\[
 \|v_\lambda\|_{L^2(E)}^2
 =\int|\chi(z)|^2
 w_\lambda^\dagger
 H_E(x_\lambda+\lambda^{-1/2}z)w_\lambda\,dz .
 \tag{PW11}
\]
This follows from the exact change
\(dx=\lambda^{-n/2}dz\); that factor cancels the
\(\lambda^{n/2}\) from the squared packet amplitude.
The full metric difference is
\[
 H_E(x_\lambda+\lambda^{-1/2}z)-H_E(x_\lambda)
 =\lambda^{-1/2}\sum_{j=1}^n z_j
       \int_0^1\partial_{x_j}H_E
          (x_\lambda+t\lambda^{-1/2}z)\,dt .
 \tag{PW12}
\]
The segments lie inside the fixed coordinate region for large
\(\lambda\). PW4, PW9 and PW12 give a uniform
\(O(\lambda^{-1/2})\) error in PW11 and therefore
\[
 \|v_\lambda\|_{L^2(E)}^2=1+O(\lambda^{-1/2}),
 \qquad \|v_\lambda\|_{L^2(E)}=1+O(\lambda^{-1/2}).
 \tag{PW13}
\]

For clarity about another possible half-density presentation, if
one writes PW10 relative to
\(\rho(x)=r(x)|dx|^{1/2}\), \(r>0\), then its norm is instead
\[
 \int|\chi(z)|^2r(x_\lambda+\lambda^{-1/2}z)^2
  w_\lambda^\dagger H_E(x_\lambda+\lambda^{-1/2}z)w_\lambda\,dz .
 \tag{PW14}
\]
Under PW9 this tends to \(r(x_\lambda)^2\), with the same uniform
metric-and-density error. Thus PW13 as written requires the
coordinate half-density frame, or the explicit center condition
\(r(x_\lambda)^2 w_\lambda^\dagger H_E(x_\lambda)w_\lambda=1\).
If a general frame is used, its \(r\) factor also stays in the
Fourier integral; it cannot be silently dropped.
The following formulas use the stated coordinate frame PW3.

Writing \(v_\lambda\) for its coordinate coefficient in PW7, its
forward Fourier transform is exactly
\[
 \widehat v_\lambda(\eta)
   =\lambda^{-n/4}e^{-ix_\lambda\cdot\eta}
      \widehat\chi\!\left(
           \frac{\eta-\xi_\lambda}{\sqrt\lambda}\right)w_\lambda .
 \tag{PW15}
\]
Indeed \(x=x_\lambda+z/\sqrt\lambda\) gives
\[
 -x\cdot\eta+(x-x_\lambda)\cdot\xi_\lambda
 =-x_\lambda\cdot\eta
    -z\cdot(\eta-\xi_\lambda)/\sqrt\lambda ,
 \quad
 \lambda^{n/4}dx=\lambda^{-n/4}dz .
\]
In particular the constant phase is \(e^{-ix_\lambda\cdot\eta}\).
Replacing it by \(e^{-ix_\lambda\cdot(\eta-\xi_\lambda)}\)
would change this original packet by the extra factor
\(e^{ix_\lambda\cdot\xi_\lambda}\).
Inverse transformation retains the complete constant:
\[
 v_\lambda(x)=
 (2\pi)^{-n}\lambda^{n/4}
 e^{i(x-x_\lambda)\cdot\xi_\lambda}
 \int e^{i\sqrt\lambda(x-x_\lambda)\cdot z}
      \widehat\chi(z)\,dz\,w_\lambda .
 \tag{PW16}
\]
Plancherel in these conventions is
\(\|u\|_{L^2(dx)}^2=(2\pi)^{-n}\int|\widehat u(\eta)|^2d\eta\).
For every multiindex \(\beta\), PW15 has the full derivative
\[
 \partial_\eta^\beta\widehat v_\lambda(\eta)
 =\lambda^{-n/4}e^{-ix_\lambda\cdot\eta}
   \sum_{\mu\leq\beta}{\beta\choose\mu}
   (-ix_\lambda)^{\beta-\mu}\lambda^{-|\mu|/2}
   (\partial^\mu\widehat\chi)
       ((\eta-\xi_\lambda)/\sqrt\lambda)w_\lambda .
 \tag{PW17}
\]
Every derivative of \(\widehat\chi\) decreases faster than every
power: differentiate its defining compact integral and integrate
by parts in each original coordinate. No Fourier constant is
introduced by that forward transform.

The exact centered differentiation identity is
\[
 (D_r-\xi_{\lambda,r})v_\lambda
   =-i\lambda^{n/4+1/2}
        (\partial_r\chi)(\sqrt\lambda(x-x_\lambda))
        e^{i(x-x_\lambda)\cdot\xi_\lambda}w_\lambda .
 \tag{PW18}
\]
Consequently its Euclidean norm squared is
\(\lambda|w_\lambda|_{\rm c}^2\int|\partial_r\chi|^2\), while
its geometric norm squared retains the exact integrand
\[
 \lambda\int|\partial_r\chi(z)|^2
      w_\lambda^\dagger H_E(x_\lambda+\lambda^{-1/2}z)
                   w_\lambda\,dz .
 \tag{PW19}
\]
Both yield a uniform \(O(\lambda^{1/2})\) norm.

### 3. The frequency cutoff, all of its derivatives and the tail

Set \(c_g=\max(1,\kappa_+)\). Choose a fixed
\(\vartheta\in C_c^\infty(\mathbb R^n)\), equal to one when
\(|q|_{\rm c}\leq1/2\), supported where \(|q|_{\rm c}\leq1\),
and with \(0\leq\vartheta\leq1\). Define
\[
 q_\lambda(\eta)=\frac{2c_g}{\lambda}(\eta-\xi_\lambda),
 \quad
 \vartheta_\lambda(\eta)=\vartheta(q_\lambda(\eta)),
 \quad
 t_\lambda=(1-\vartheta_\lambda)(D)v_\lambda .
 \tag{PW20}
\]
This keeps \(\lambda\) as the original metric norm.
The cutoff support has
\(|\eta-\xi_\lambda|_{\rm c}\leq\lambda/(2c_g)\).
When \(\lambda\) is a coordinate norm and \(c_g=1\), this is
the radius \(\lambda/2\) stated in the original OM8 discussion.
For a general metric PW20 records the needed chart constant.
On that support, for every \(0\leq\theta\leq1\),
\[
 |\xi_\lambda+\theta(\eta-\xi_\lambda)|_{\rm c}
 \geq \lambda/\kappa_+-\lambda/(2c_g)
 \geq \lambda/(2c_g),\qquad
 |\eta|_{\rm c}\leq\lambda/\kappa_-+\lambda/(2c_g).
 \tag{PW21}
\]
Every derivative of the cutoff is exactly
\[
 \partial_\eta^\gamma\vartheta_\lambda
   =(2c_g)^{|\gamma|}\lambda^{-|\gamma|}
       (\partial^\gamma\vartheta)(q_\lambda).
 \tag{PW22}
\]
It is supported in the same fixed-radius rescaled ball. Every
positive-order derivative of \(1-\vartheta_\lambda\) is the
negative of PW22; its zeroth derivative is \(1-\vartheta_\lambda\).
Thus every tail-transform derivative is exactly the product sum
\[
 \partial_\eta^\beta\widehat t_\lambda
   =\sum_{\gamma\leq\beta}{\beta\choose\gamma}
       \partial_\eta^\gamma(1-\vartheta_\lambda)
       \partial_\eta^{\beta-\gamma}\widehat v_\lambda ,
 \tag{PW23}
\]
with PW17 and PW22 supplying all factors and signs.

For every fixed real \(s\), the tail's exact Euclidean Sobolev
norm is
\[
 \begin{split}
 \|t_\lambda\|_{H^s(\mathbb R^n)}^2
  &=(2\pi)^{-n}|w_\lambda|_{\rm c}^2
    \int \langle\xi_\lambda+\sqrt\lambda z\rangle_{\rm c}^{2s}
       |1-\vartheta(2c_g z/\sqrt\lambda)|^2
       |\widehat\chi(z)|^2\,dz .
 \end{split}
 \tag{PW24}
\]
The two powers \(\lambda^{-n/2}\) and
\(\lambda^{n/2}\) from PW15 and \(d\eta\) cancel exactly.
The nonzero integrand has
\(|z|_{\rm c}\geq\sqrt\lambda/(4c_g)\).
Put \(s_+=\max(s,0)\). For \(\lambda\geq1\),
\[
 \langle\xi_\lambda+\sqrt\lambda z\rangle_{\rm c}
 \leq \sqrt2(1+\kappa_-^{-1})\lambda
                         \langle z\rangle_{\rm c}.
 \tag{PW25}
\]
Use \(|\widehat\chi(z)|\leq C_L\langle z\rangle_{\rm c}^{-L}\).
For \(\lambda\geq(4c_g)^2\) and \(2(L-s_+)>n\),
integration outside the displayed ball gives
\[
 \|t_\lambda\|_{H^s}^2
       \leq C_{s,L}\lambda^{3s_++n/2-L}.
 \tag{PW26}
\]
For example this follows by comparison with
\(\int_R^\infty r^{n-1-2(L-s_+)}dr
 =R^{n-2(L-s_+)}/(2(L-s_+)-n)\), multiplied by the sphere area;
here \(R=\sqrt\lambda/(4c_g)\). All constants from PW24--PW25
remain in \(C_{s,L}\). For each fixed \(s\) and \(N\), choosing
\(L>2N+3s_++n/2\) proves
\[
 \|t_\lambda\|_{H^s}=O(\lambda^{-N}).
 \tag{PW27}
\]
This is uniform in the centers, directions and metric-unit vectors.
It also keeps all centered differentiation factors: for a fixed
multiindex \(\delta\), replace PW24's integrand by
\(\lambda^{|\delta|}|z^\delta|^2\) times that integrand to obtain
\[
 \|(D-\xi_\lambda)^\delta t_\lambda\|_{H^s}^2
       \leq C_{s,L,\delta}
           \lambda^{3s_++2|\delta|+n/2-L}.
 \tag{PW28}
\]
Thus these tail terms decrease faster than every prescribed power as well.

### 4. Every derivative of the mean-value coefficient

The exact identity OM8, now for the cutoff-extended symbol, is
\[
 \widetilde a(x,\eta)-\widetilde a(x,\xi_\lambda)
 =\sum_{r=1}^n(\eta_r-\xi_{\lambda,r})
      \int_0^1\partial_{\eta_r}\widetilde a
        (x,\xi_\lambda+\theta(\eta-\xi_\lambda))\,d\theta .
 \tag{PW29}
\]
Define the actual cutoff coefficients
\[
 b_{\lambda,r}(x,\eta)=\vartheta_\lambda(\eta)
        \int_0^1\partial_{\eta_r}\widetilde a
          (x,\xi_\lambda+\theta(\eta-\xi_\lambda))\,d\theta .
 \tag{PW30}
\]
For all multiindices \(\alpha,\beta\), their complete derivative
formula is
\[
 \begin{split}
 \partial_x^\alpha\partial_\eta^\beta b_{\lambda,r}
 &=\sum_{\gamma\leq\beta}{\beta\choose\gamma}
       (2c_g)^{|\gamma|}\lambda^{-|\gamma|}
       (\partial^\gamma\vartheta)(q_\lambda)\\
 &\quad{}\times\int_0^1\theta^{|\beta-\gamma|}
       (\partial_x^\alpha
          \partial_\eta^{\beta-\gamma+e_r}\widetilde a)
       (x,\xi_\lambda+\theta(\eta-\xi_\lambda))\,d\theta .
 \end{split}
 \tag{PW31}
\]
If desired, substitute PW8 into the last line to retain each
individual output-cutoff derivative as well. Each factor
\(\theta^{|\beta-\gamma|}\) comes from differentiating the affine
frequency path; there is no derivative of either center parameter,
because these are fixed parameters when differentiating \(x,\eta\).
The binomial coefficients include every way derivatives can hit
the frequency cutoff. Differentiation under the integral is
justified on the compact interval by the smooth integrand and its
uniform bounds PW6 and PW21.

Every nonzero term in PW31 is supported where PW21 holds.
Consequently
\[
 \begin{split}
 \|\partial_x^\alpha\partial_\eta^\beta b_{\lambda,r}\|_\infty
 &\leq (2c_g)^{1+|\beta|}
         \lambda^{-1-|\beta|}
       \sum_{\gamma\leq\beta}{\beta\choose\gamma}
       \|\partial^\gamma\vartheta\|_\infty
       \frac{\widetilde M_{\alpha,\beta-\gamma+e_r}}
            {1+|\beta-\gamma|}.
 \end{split}
 \tag{PW32}
\]
Here the denominator is the exact integral
\(\int_0^1\theta^{|\beta-\gamma|}d\theta\).
The factor \((2c_g)^{1+|\beta|}\) is the product of the
cutoff factor in PW31 and the lower-frequency comparison in PW21.
In particular \(b_{\lambda,r}\) is a uniformly bounded family in
\(S^{-1}_{1,0}\), and \(\lambda b_{\lambda,r}\) is a uniformly
bounded family in \(S^0_{1,0}\): on its support
\(\langle\eta\rangle_{\rm c}\leq
(1+\kappa_-^{-1}+(2c_g)^{-1})\lambda\), and outside that support
all derivatives vanish. More directly, E23 and PW32 give
\[
 \|\operatorname{Op}(b_{\lambda,r})u\|_{L^2(dx)}
 \leq C_n
   \max_{|\alpha|+|\beta|\leq L_n}
       \|\partial_x^\alpha\partial_\eta^\beta b_{\lambda,r}\|_\infty
       \|u\|_{L^2(dx)}
 \leq C_r\lambda^{-1}\|u\|_{L^2(dx)} .
 \tag{PW33}
\]
This uses a fixed derivative count and finitely many original
symbol seminorms. It is therefore uniform, rather than a separate
boundedness assertion for each \(\lambda\).

### 5. Ordered decomposition and the spatial term

Let \(M_{\widetilde a(\cdot,\xi_\lambda)}\) denote multiplication
by the actual \(x\)-dependent matrix. PW29 gives the exact operator
identity on the packet
\[
 \begin{split}
 \operatorname{Op}(\widetilde a)v_\lambda
       -M_{\widetilde a(\cdot,\xi_\lambda)}v_\lambda
 &=\sum_{r=1}^n
       \operatorname{Op}(b_{\lambda,r})
          (D_r-\xi_{\lambda,r})v_\lambda\\
 &\quad{}+\operatorname{Op}(\widetilde a)t_\lambda
       -M_{\widetilde a(\cdot,\xi_\lambda)}t_\lambda .
 \end{split}
 \tag{PW34}
\]
To check every product in this identity, transform the rightmost
\((D_r-\xi_{\lambda,r})v_\lambda\). Its transform is exactly
\((\eta_r-\xi_{\lambda,r})\widehat v_\lambda\).
Thus the first line of PW34 has left symbol
\((\widetilde a(x,\eta)-\widetilde a(x,\xi_\lambda))
\vartheta_\lambda(\eta)\).
The second line has the same difference times
\(1-\vartheta_\lambda(\eta)\).
Their sum is the original left-symbol difference. The derivative
operator stands on the right; no matrix factor is commuted, and no
composition correction is discarded.

E23 also bounds the fixed operator \(\operatorname{Op}(\widetilde a)\).
Multiplication by \(\widetilde a(x,\xi_\lambda)\) is bounded
uniformly by PW6 and PW8. Hence PW18, PW27 and PW33 prove
\[
 \|\operatorname{Op}(\widetilde a)v_\lambda
       -M_{\widetilde a(\cdot,\xi_\lambda)}v_\lambda\|_{L^2(dx)}
       \leq C\lambda^{-1/2}.
 \tag{PW35}
\]
The output is supported in the fixed support of \(\zeta\);
the factor \(H_F\) in PW3 converts this to the geometric norm
with the factor \((h_F^+)^{1/2}\). The input norms in PW33
and PW18 likewise retain PW4's uniform coordinate comparison.

Let the frozen output section be
\[
 f_\lambda(x)=
 \lambda^{n/4}\chi(\sqrt\lambda(x-x_\lambda))
 e^{i(x-x_\lambda)\cdot\xi_\lambda}
 a(x_\lambda,\xi_\lambda)w_\lambda\,|dx|^{1/2},
 \tag{PW36}
\]
using the specified output frame. This is the precise meaning
of \(a(x_\lambda,\xi_\lambda)v_\lambda\) in OM7:
the constant coordinate matrix sends the input coordinates to the
output coordinates. It does not identify \(E_x\) with \(F_x\).
On the support of \(v_\lambda\), \(\zeta=1\) and
\[
 a(x,\xi_\lambda)-a(x_\lambda,\xi_\lambda)
 =\sum_{j=1}^n(x_j-x_{\lambda,j})
       \int_0^1\partial_{x_j}a
          (x_\lambda+t(x-x_\lambda),\xi_\lambda)\,dt .
 \tag{PW37}
\]
PW6, PW9, PW11 and the compact support of \(\chi\) give
\[
 \|M_{\widetilde a(\cdot,\xi_\lambda)}v_\lambda
       -f_\lambda\|_{L^2(F)}
 \leq C\lambda^{-1/2}
           \left(\int |z|_{\rm c}^2|\chi(z)|^2dz\right)^{1/2}.
 \tag{PW38}
\]
All the spatial factors and the target metric remain in this estimate.
Writing \(z_\lambda=a(x_\lambda,\xi_\lambda)w_\lambda\), its
frozen output norm is exactly
\[
 \|f_\lambda\|_{L^2(F)}^2
 =\int|\chi(z)|^2
   z_\lambda^\dagger H_F(x_\lambda+\lambda^{-1/2}z)
                         z_\lambda\,dz .
 \tag{PW39}
\]
The target version of PW12 and PW4 give
\[
 \left|\|f_\lambda\|_{L^2(F)}^2
    -\|a(x_\lambda,\xi_\lambda)w_\lambda\|_{F_{x_\lambda}}^2\right|
 \leq C\lambda^{-1/2}
        \|a(x_\lambda,\xi_\lambda)w_\lambda\|_{F_{x_\lambda}}^2 .
 \tag{PW40}
\]
This relative estimate includes the case \(z_\lambda=0\), when
both sides vanish exactly.

### 6. The off-diagonal kernel and every smoothing contribution

For large \(\lambda\), \(\psi v_\lambda=v_\lambda\). The exact
localized decomposition is
\[
 Av_\lambda
    =\operatorname{Op}(\widetilde a)v_\lambda
      +Rv_\lambda+(1-\zeta)A\psi v_\lambda .
 \tag{PW41}
\]
The \(R\) term has a smooth localized kernel by its definition.
The last term has a smooth kernel because the supports of
\(1-\zeta\) and \(\psi\) are separated. This also follows
directly from the full local Fourier kernel, with all signs retained.
For \(z=x-y\ne0\), E12 and distributional frequency integration
by parts give
\[
 \begin{split}
 \partial_x^\alpha\partial_y^\beta K_a(x,y)
 &=(2\pi)^{-n}|x-y|_{\rm c}^{-2M}
   \sum_{\gamma\leq\alpha}{\alpha\choose\gamma}
   \int e^{i(x-y)\cdot\eta}\\
 &\quad{}\times(-\Delta_\eta)^M
       \left[(i\eta)^{\alpha-\gamma}(-i\eta)^\beta
                   \partial_x^\gamma a(x,\eta)\right]\,d\eta .
 \end{split}
 \tag{PW42}
\]
Choose \(2M>n+|\alpha|+|\beta|\). The full differentiated
amplitude is
\[
 \begin{split}
 (-\Delta_\eta)^M
       [P_{\alpha,\beta,\gamma}(\eta)\partial_x^\gamma a]
 &=(-1)^M\sum_{|\nu|=M}\frac{M!}{\nu!}
       \sum_{\delta\leq2\nu}{2\nu\choose\delta}
       (\partial_\eta^{2\nu-\delta}
                          P_{\alpha,\beta,\gamma})\\
 &\qquad{}\times
       (\partial_\eta^\delta\partial_x^\gamma a),
 \quad
 P_{\alpha,\beta,\gamma}
       =(i\eta)^{\alpha-\gamma}(-i\eta)^\beta .
 \end{split}
 \tag{PW43}
\]
Its nonzero terms have frequency bound
\(C\langle\eta\rangle_{\rm c}^{|\alpha-\gamma|+|\beta|-2M}\),
which is integrable. For a monomial
\(\partial_\eta^\tau\eta^\omega\) equals
\(\omega!\eta^{\omega-\tau}/(\omega-\tau)!\) when
\(\tau\leq\omega\), and is zero otherwise; thus PW43 keeps
the full coefficient and every zero. The original inverse factor
\((2\pi)^{-n}\) and both differentiation signs stay in PW42.
The distributional identities E12 and EC15 justify PW42 before
any assertion of absolute convergence. Multiplication by
\(|x-y|_{\rm c}^{-2M}\) is smooth away from \(z=0\); the
integrable amplitude then identifies the resulting restriction.
Here is also the full compact-cutoff passage. Choose a fixed
smooth \(\omega\), equal to one on \(|\eta|_{\rm c}\leq c_0\)
and zero on \(|\eta|_{\rm c}\geq c_1\), with \(0<c_0<c_1\).
Put \(B=P_{\alpha,\beta,\gamma}\partial_x^\gamma a\) and
\(d=|\alpha-\gamma|+|\beta|\). For every \(\nu\) in PW43,
\[
 \partial_\eta^{2\nu}[B(x,\eta)\omega(\eta/R)]
 =\sum_{\sigma\leq2\nu}{2\nu\choose\sigma}
      (\partial_\eta^{2\nu-\sigma}B)(x,\eta)
      R^{-|\sigma|}(\partial^\sigma\omega)(\eta/R).
 \tag{PW43a}
\]
The derivatives of \(B\) have their full product-rule sums as
in PW43, with the corresponding total derivative order.
The \(\sigma=0\) term tends to
\(\partial_\eta^{2\nu}B\) in absolute integral by its integrable
bound. Every \(\sigma>0\) term has the original annular support
\(c_0R\leq|\eta|_{\rm c}\leq c_1R\), and its absolute integral
has the bound
\[
 {2\nu\choose\sigma}R^{-|\sigma|}
 \|\partial^\sigma\omega\|_\infty
 \int_{c_0R\leq|\eta|_{\rm c}\leq c_1R}
    C_{\nu,\sigma}\langle\eta\rangle_{\rm c}^{d-2M+|\sigma|}d\eta
 \leq C'_{\nu,\sigma}R^{n+d-2M}\longrightarrow0.
 \tag{PW43b}
\]
The constants include the annulus volume
\(\omega_nc_1^nR^n\), \(c_0,c_1\) and all polynomial
coefficients. The exponent is negative by the stated choice of
\(M\). Thus every frequency-cutoff derivative vanishes separately,
and the original oscillatory identity passes to PW42 with all
boundary terms accounted for.
For every pair \(\alpha,\beta\), this is a continuous derivative.
Consequently the kernel is smooth away from the coordinate diagonal.
For output cutoff \(c(x)\) and input cutoff \(d(y)\), the exact
remaining derivative sum is
\[
 \partial_x^\alpha\partial_y^\beta[c(x)K_a(x,y)d(y)]
 =\sum_{\rho\leq\alpha}\sum_{\sigma\leq\beta}
     {\alpha\choose\rho}{\beta\choose\sigma}
     (\partial_x^\rho c)(x)
     (\partial_x^{\alpha-\rho}\partial_y^{\beta-\sigma}K_a)(x,y)
     (\partial_y^\sigma d)(y).
 \tag{PW43c}
\]
For the actual off-diagonal term, \(c=1-\zeta\), \(d=\psi\):
the zeroth output derivative is \(1-\zeta\), and each positive
output derivative is \(-\partial_x^\rho\zeta\). All such
contributions retain the smooth-kernel bounds just proved.
In other charts the same argument applies. Compactness and the
positive support separation give uniform bounds for the resulting
global smooth kernel and all its input and output derivatives.

Here is the exact packet bound for any such smooth matrix kernel
\(S(x,y)\). Its local action on the actual coordinate half-density
coefficient is
\[
 Sv_\lambda(x)=\lambda^{n/4}
       \int S(x,y)\chi(\sqrt\lambda(y-x_\lambda))
           e^{i(y-x_\lambda)\cdot\xi_\lambda}w_\lambda\,dy .
 \tag{PW44}
\]
The input integration measure is precisely \(dy\); the kernel's
half-density factors produce the output half-density as in PW3.
Set
\[
 L_\lambda=\frac{\xi_\lambda\cdot\partial_y}
                   {i|\xi_\lambda|_{\rm c}^2};
 \qquad
 L_\lambda e^{i(y-x_\lambda)\cdot\xi_\lambda}
             =e^{i(y-x_\lambda)\cdot\xi_\lambda}.
 \tag{PW45}
\]
Compact support of the packet envelope removes all input boundary
terms. Repeated integration by parts gives the exact finite sum
\[
 \begin{split}
 Sv_\lambda(x)
 &=\frac{\lambda^{n/4}(-1)^M}
             {(i|\xi_\lambda|_{\rm c}^2)^M}
      \sum_{|\gamma|=M}\frac{M!}{\gamma!}\xi_\lambda^\gamma
      \sum_{\delta\leq\gamma}{\gamma\choose\delta}
           \lambda^{|\delta|/2}\\
 &\quad{}\times\int e^{i(y-x_\lambda)\cdot\xi_\lambda}
       (\partial_y^{\gamma-\delta}S)(x,y)
       (\partial^\delta\chi)(\sqrt\lambda(y-x_\lambda))
                w_\lambda\,dy .
 \end{split}
 \tag{PW46}
\]
The sign \((-1)^M\), denominator \(i^M\), multinomial
coefficients and all envelope derivatives remain visible.
Every fixed output derivative has the same formula with the
corresponding derivative of \(S\). PW5 gives
\[
 \frac{|\xi_\lambda^\gamma|}
          {|\xi_\lambda|_{\rm c}^{2M}}
 \leq|\xi_\lambda|_{\rm c}^{-M}
 \leq\kappa_+^M\lambda^{-M}.
\]
The envelope's exact \(L^1\) integral is
\(\lambda^{-n/2}\|\partial^\delta\chi\|_1\).
Using PW9 in PW46 therefore yields, for every fixed output
derivative order,
\[
 \|\partial_x^\alpha Sv_\lambda\|_\infty
       \leq C_{\alpha,M}\lambda^{-M/2-n/4}.
 \tag{PW47}
\]
Finitely many output charts, the retained smooth metrics and
the finite volume of \(X\) convert this to geometric \(L^2\).
For each requested power \(N\), choose \(M\geq2N\) to obtain
\[
 \|Rv_\lambda\|_{L^2(F)}
       +\|(1-\zeta)A\psi v_\lambda\|_{L^2(F)}
       =O(\lambda^{-N}).
 \tag{PW48}
\]
The proof applies separately to every smooth remainder; none is
absorbed into the symbol error without an estimate.

PW35, PW38, PW41 and PW48 prove the required full estimate
\[
 \boxed{\ \|Av_\lambda-f_\lambda\|_{L^2(F)}
                  \leq C\lambda^{-1/2}\ } .
 \tag{PW49}
\]
The constant depends only on the fixed chart, cutoffs, metric bounds,
profile and finitely many symbol seminorms. It is independent of
the moving center, covector direction, frequency and metric-unit vector.

### 7. Weak convergence, order-minus-one errors and uniform necessity

The support is contained in the coordinate ball
\(B(x_\lambda,R_\chi/\sqrt\lambda)\), whose coordinate volume is
\(\omega_nR_\chi^n\lambda^{-n/2}\). For any fixed \(g\in L^2(E)\),
geometric Cauchy--Schwarz gives
\[
 |\langle v_\lambda,g\rangle_{L^2(E)}|
 \leq \|v_\lambda\|_{L^2(E)}
       \|\mathbf1_{\operatorname{supp}v_\lambda}g\|_{L^2(E)}
       \longrightarrow0.
 \tag{PW50}
\]
Absolute continuity of the integral of
\(g^\dagger H_Eg\) proves the convergence for these moving sets,
uniformly with respect to their centers. PW13 bounds the first
factor. Thus the original packets are weakly null.

For completeness let \(\mathcal R\in\Psi^{-1}_{1,0}(X;E,F)\),
let \(r\in S^{-1}_{1,0}\) be its complete local symbol, and retain
its localized smooth remainder and off-diagonal term.
In the following Euclidean formulas use \(r=\zeta r_{\rm loc}\),
extended by zero, exactly as in PW8. Thus each base derivative
contains the full sum of derivatives of \(\zeta\) and of the
original complete symbol \(r_{\rm loc}\); at the packet center
the two symbols coincide.
Its cutoff symbol has every derivative
\[
 \partial_x^\alpha\partial_\eta^\beta
       [r(x,\eta)\vartheta_\lambda(\eta)]
 =\sum_{\gamma\leq\beta}{\beta\choose\gamma}
       (\partial_x^\alpha\partial_\eta^{\beta-\gamma}r)(x,\eta)
       (2c_g)^{|\gamma|}\lambda^{-|\gamma|}
       (\partial^\gamma\vartheta)(q_\lambda).
 \tag{PW51}
\]
On this support PW21 gives
\(\langle\eta\rangle_{\rm c}\geq\lambda/(2c_g)\).
Hence each full derivative in PW51 is
\(O(\lambda^{-1-|\beta|})\), with its finite binomial sum retained.
E23 then bounds \(\operatorname{Op}(r\vartheta_\lambda)\)
by \(C\lambda^{-1}\). The exact tail decomposition
\[
 \operatorname{Op}(r)v_\lambda
      =\operatorname{Op}(r\vartheta_\lambda)v_\lambda
            +\operatorname{Op}(r)t_\lambda
 \tag{PW52}
\]
and PW27, together with PW48 for the smoothing term, prove
\[
 \|\mathcal Rv_\lambda\|_{L^2(F)}=O(\lambda^{-1})
 \quad\text{for each fixed }\mathcal R\in\Psi^{-1}_{1,0}(X;E,F).
 \tag{PW53}
\]
Here \(\mathcal R\) is distinct from the smooth local remainder
\(R\) of PW41.

Every point of \(X\) lies in one member of a finite cover by smaller
coordinate regions \(K\) of the kind used above. Taking the maximum
of their finitely many constants proves uniformity on \(X\).
For the contradiction argument one can instead select a subsequence
whose centers all lie in one such compact smaller region.
The original metric frequency \(\lambda\) is retained on each chart
through PW5 and PW20.

Apply this to the exact operator in OM9,
\[
 A_s=J_E^{-s}:L^2(E)\longrightarrow H^s(E),\qquad
 B_{s-m}=J_F^{s-m}:H^{s-m}(F)\longrightarrow L^2(F),\qquad
 T=B_{s-m}P_sA_s .
 \tag{PW54}
\]
These are the specified bounded isomorphisms, with their original
source and target spaces, metrics and half-densities.
Retain the ordered original principal factors
\[
 \widetilde p(x,\xi)
      =\langle\xi\rangle_{g,x}^{\,s-m}
          p(x,\xi)\langle\xi\rangle_{g,x}^{-s}.
 \tag{PW55}
\]
The full local symbol of \(T\) equals this representative plus
\(r\in S^{-1}_{1,0}\), including all the lower-order composition
terms. PW53 estimates that complete error; it is not presumed zero.
The scalar factors in PW55 are positive and the displayed ordered
product has the exact value
\(\langle\xi\rangle_{g,x}^{-m}p(x,\xi)\).
This equality is an explicit comparison with the original \(p\);
it does not remove \(p\), its order or either operator factor.

If OM2 fails, choose for each integer \(j\) a covector
\((x_j,\xi_j)\) with \(|\xi_j|_{g,x_j}\geq j\) and a vector
\(\|w_j\|_{E_{x_j}}=1\) such that
\[
 \|\widetilde p(x_j,\xi_j)w_j\|_{F_{x_j}}<1/j .
 \tag{PW56}
\]
The failure of a uniform positive lower bound gives exactly these
choices. Passing to one smaller chart preserves PW9, with
\(\lambda_j=|\xi_j|_{g,x_j}\to\infty\). PW49, PW40 and PW53 give
\(\|Tv_{\lambda_j}\|_2\to0\), while PW13 gives
\(\|v_{\lambda_j}\|_2\to1\).
If \(N=\ker T\) is finite dimensional, its orthogonal projection
sends PW50's weakly null packets to zero in norm: for an actual
orthonormal basis \(e_1,\ldots,e_d\) of \(N\),
\[
 \|\Pi_Nv_{\lambda_j}\|_2^2
       =\sum_{\ell=1}^d
               |\langle v_{\lambda_j},e_\ell\rangle|^2\longrightarrow0.
 \tag{PW57}
\]
No smoothness of \(N\) is required. Closed range and finite kernel
of \(P_s\) pass through PW54 to \(T\), so the already-proved compact
estimate OM4 gives
\[
 \|v_{\lambda_j}\|_2
 \leq C\bigl(\|Tv_{\lambda_j}\|_2+
                 \|\Pi_Nv_{\lambda_j}\|_2\bigr)\longrightarrow0.
 \tag{PW58}
\]
This contradicts PW13 and proves OM2 for the original symbol \(p\)
with its original weight \(\langle\xi\rangle_{g,x}^{m}\).
The proof uses the complete \(S^0_{1,0}\) high-frequency symbol
and does not require a homogeneous cosphere representative.

Use the actual order-changing bundle isomorphisms proved in the linked global-index lesson:
\[
 A_s=J_E^{-s}:L^2(E)\xrightarrow{\;\cong\;}H^s(E),\quad
 B_{s-m}=J_F^{s-m}:H^{s-m}(F)\xrightarrow{\;\cong\;}L^2(F),\quad
 T=B_{s-m}P_sA_s.
 \tag{OM9}
\]
They are auxiliary comparison maps, not replacements for \(P_s\). Their positive scalar principal symbols are \(\langle\xi\rangle^{-s}I_E\) and \(\langle\xi\rangle^{s-m}I_F\). Keeping all factors and their order gives
\[
 \sigma_0(T)(x,\xi)
 =\langle\xi\rangle^{s-m}p(x,\xi)\langle\xi\rangle^{-s}
 =\langle\xi\rangle^{-m}p(x,\xi)
 \pmod {S^{-1}}.
 \tag{OM10}
\]
Because \(A_s,B_{s-m}\) are exact isomorphisms, \(T\) has finite kernel and closed range. If (OM2) failed, choose \((x_\lambda,\xi_\lambda,w_\lambda)\) with \(\lambda\to\infty\) and
\(\|\langle\xi_\lambda\rangle^{-m}p(x_\lambda,\xi_\lambda)w_\lambda\|\to0\).
After a subsequence the centers lie in one smaller chart. Apply (OM7) to \(T\); its \(S^{-1}\) difference from the displayed principal map tends to zero on the packets. Thus \(\|Tv_\lambda\|_2\to0\), while \(\|v_\lambda\|_2\to1\) and the finite-rank projection onto \(\ker T\) sends the weakly null packets to zero in norm. Equation (OM4) for \(T\) is contradicted. Therefore (OM2) holds. This proves the symbol lower bound directly for the original \(p\), for an arbitrary real realization order \(s\).

## 4. The exact left symbol and the full left parametrix

Assume (OM2). In the actual Hermitian metrics define \(G=p^*p\), a positive endomorphism of \(E\). At large \(|\xi|\),
\[
 \langle Gw,w\rangle=\|pw\|^2
 \ge c^2\langle\xi\rangle^{2m}\|w\|^2,\quad
 q_0=G^{-1}p^*:F\longrightarrow E,\quad
 q_0p=I_E.
 \tag{OM11}
\]
The full matrix \(G\) remains present. Its symbol derivatives satisfy
\(\partial_x^\alpha\partial_\xi^\beta G
 =O(\langle\xi\rangle^{2m-|\beta|})\).
Differentiating \(GG^{-1}=I_E\) and retaining each ordered product yields by induction
\(\partial_x^\alpha\partial_\xi^\beta G^{-1}
 =O(\langle\xi\rangle^{-2m-|\beta|})\).
Consequently \(q_0\in S^{-m}(\operatorname{Hom}(F,E))\). A smooth scalar cutoff in the fixed cotangent norm, zero below the high-frequency region and one beyond a larger region, extends \(q_0\) to a global symbol \(q\in S^{-m}\) with
\[
 qp-I_E\in S^{-\infty}\subset S^{-1}.
 \tag{OM12}
\]
The construction is invariant under unitary changes of frame because \(p^*p\) and its inverse are bundle maps; the cutoff and finite chart quantization preserve the global symbol class.

Here is the complete derivative calculation behind that construction. In a
fixed pair of local frames write the original metrics as
\(h_E(w,v)=\overline v^{\,T}H_E(x)w\) and
\(h_F(z,y)=\overline y^{\,T}H_F(x)z\). Their matrices and inverses,
with every fixed derivative, are bounded on the chart closure. The exact
adjoint and its derivatives are
\[
 \begin{aligned}
 p^*&=H_E^{-1}\overline p^{\,T}H_F,\\
 \partial_x^\alpha\partial_\xi^\beta p^*
 &=\sum_{\alpha_1+\alpha_2+\alpha_3=\alpha}
   \frac{\alpha!}{\alpha_1!\alpha_2!\alpha_3!}
   (\partial_x^{\alpha_1}H_E^{-1})
   \overline{\partial_x^{\alpha_2}\partial_\xi^\beta p}^{\,T}
   (\partial_x^{\alpha_3}H_F),\\
 \partial_x^\alpha\partial_\xi^\beta G
 &=\sum_{\substack{\alpha_1+\alpha_2=\alpha\\
                   \beta_1+\beta_2=\beta}}
   \frac{\alpha!\beta!}{\alpha_1!\alpha_2!\beta_1!\beta_2!}
   (\partial_x^{\alpha_1}\partial_\xi^{\beta_1}p^*)
   (\partial_x^{\alpha_2}\partial_\xi^{\beta_2}p).
 \end{aligned}
 \tag{OI1}
\]
Thus there are finite constants \(C_{\alpha,\beta}\), in the original
fiber operator norms, for which
\(\|\partial_x^\alpha\partial_\xi^\beta G\|
 \le C_{\alpha,\beta}\langle\xi\rangle^{2m-|\beta|}\).
The inequality in (OM11) gives
\(\|G^{-1}\|\le c^{-2}\langle\xi\rangle^{-2m}\).
For the nonzero combined multiindex \(\kappa=(\alpha,\beta)\), every
derivative of the inverse is the following finite ordered sum:
\[
 \partial_x^\alpha\partial_\xi^\beta G^{-1}
 =\sum_{r=1}^{|\alpha|+|\beta|}(-1)^r
   \sum_{\substack{\alpha_1+\cdots+\alpha_r=\alpha\\
                   \beta_1+\cdots+\beta_r=\beta\\
                   |\alpha_j|+|\beta_j|>0\ (1\le j\le r)}}
   \frac{\alpha!\beta!}
        {\alpha_1!\cdots\alpha_r!\beta_1!\cdots\beta_r!}
   G^{-1}(\partial_x^{\alpha_1}\partial_\xi^{\beta_1}G)G^{-1}
   \cdots
   (\partial_x^{\alpha_r}\partial_\xi^{\beta_r}G)G^{-1}.
 \tag{OI2}
\]
To prove the formula, at the point under consideration expand
\(G(x+y,\xi+\eta)-G(x,\xi)\) in its finite Taylor jet. The coefficients
of the inverse jet are uniquely determined by multiplying it with the jet
of \(G\) and setting the product equal to \(I_E\). The ordered expression
\(G^{-1}-G^{-1}HG^{-1}+G^{-1}HG^{-1}HG^{-1}-\cdots\), with
\(H=G(x+y,\xi+\eta)-G(x,\xi)\), gives those coefficients: in derivative
degree \(|\alpha|+|\beta|\), only the displayed finite range of \(r\)
can contribute. Expanding each factor of \(H\) gives exactly the
factorials in (OI2). This proves an identity of derivatives of the actual
smooth inverse; it does not require convergence of an infinite series.

In particular, the complete bound is
\[
 \begin{aligned}
 \|\partial_x^\alpha\partial_\xi^\beta G^{-1}\|
 &\le\langle\xi\rangle^{-2m-|\beta|}
 \sum_{r=1}^{|\alpha|+|\beta|}
 \sum_{\substack{\alpha_1+\cdots+\alpha_r=\alpha\\
                 \beta_1+\cdots+\beta_r=\beta\\
                 |\alpha_j|+|\beta_j|>0\ (1\le j\le r)}}
 \frac{\alpha!\beta!\,c^{-2(r+1)}}
      {\alpha_1!\cdots\alpha_r!\beta_1!\cdots\beta_r!}
 \prod_{j=1}^r C_{\alpha_j,\beta_j}.
 \end{aligned}
 \tag{OI3}
\]
Indeed, the \(r+1\) inverse factors contribute order \(-2m(r+1)\)
and the \(r\) differentiated \(G\) factors contribute order
\(2mr-|\beta|\). The original \(m\) is retained in both contributions.
Finally,
\[
 \partial_x^\alpha\partial_\xi^\beta q_0
 =\sum_{\substack{\alpha_1+\alpha_2=\alpha\\
                 \beta_1+\beta_2=\beta}}
 \frac{\alpha!\beta!}{\alpha_1!\alpha_2!\beta_1!\beta_2!}
 (\partial_x^{\alpha_1}\partial_\xi^{\beta_1}G^{-1})
 (\partial_x^{\alpha_2}\partial_\xi^{\beta_2}p^*)
 \tag{OI4}
\]
has order \(-m-|\beta|\). If the scalar cutoff is \(\vartheta\), then
\(q=\vartheta G^{-1}p^*\) on the region where the inverse is defined
and is zero below that region; exactly
\(qp-I_E=(\vartheta-1)I_E\). Each derivative of \(\vartheta\) is
retained by the product rule. All terms with a derivative of the cutoff,
and \((\vartheta-1)I_E\), have bounded frequency support on this compact
chart and belong to every lower symbol order. For the right construction
below, replace \(G\) by \(pp^*\), use (OM3) in the original \(F\)
metric, and retain the final order \(p^*(pp^*)^{-1}\). The same finite
derivative sums prove every symbol bound in (OM17).

Quantize \(q\) to \(Q_0\in\Psi^{-m}(F,E)\). The full composition formula, including its first derivative correction, gives
\[
 R_E=I_E-Q_0P\in\Psi^{-1}(E,E),\qquad
 Q_N=\sum_{j=0}^{N-1}R_E^jQ_0,\qquad
 Q_NP=I_E-R_E^N.
 \tag{OM13}
\]
The factor order in \(Q_N\) is fixed by the exact telescoping identity. The asymptotic-summation theorem chooses \(Q\in\Psi^{-m}(F,E)\) whose difference from \(Q_N\) lies in \(\Psi^{-m-N}\) for every \(N\). Multiplying by \(P\) and using \(R_E^N\in\Psi^{-N}\) proves
\[
 QP=I_E-S_E,\qquad S_E\in\Psi^{-\infty}(E,E).
 \tag{OM14}
\]
Conversely (OM14) gives \(qp-I_E\in S^{-1}\) by taking its principal symbol. If merely \(q\in S^{-m}\) and \(qp-I_E\in S^{-1}\), then for sufficiently large \(|\xi|\),
\[
 \tfrac12\|w\|\le\|qpw\|
       \le C\langle\xi\rangle^{-m}\|pw\|,
 \tag{OM15}
\]
so (OM2) follows. Finally (OM14) implies
\(\|u\|_{H^s}\le C(\|Pu\|_{H^{s-m}}+\|S_Eu\|_{H^s})\).
The smoothing operator is compact on \(H^s\) by the existing finite-rank kernel approximation. If a bounded sequence has convergent \(Pu_j\), first take a subsequence with convergent \(S_Eu_j\), then (OM14) makes \(u_j=QPu_j+S_Eu_j\) converge. The compactness characterization of upper semi-Fredholm maps proves finite kernel and closed range for every \(s\). Its kernel is smooth because \(Pu=0\) gives \(u=S_Eu\), independently of \(s\).

Combining Sections 2–4 proves the four equivalent left assertions: finite kernel and closed range at some \(s\), the same at every \(s\), (OM12), and (OM14). It also proves the exact estimate (OM5). No finite-cokernel conclusion was inserted.

## 5. The distinct right condition and the Fredholm consequence

If \(\operatorname{ran}P_s\) has finite algebraic codimension, it is closed by the finite-codimension bounded-range theorem in the linked Fredholm lesson. **Correction of the dual type.** With \(E^*,F^*\) denoting the ordinary complex-linear dual bundles, the following original arrow is the bilinear transpose, denoted \(P_s^*\) in this arrow. Its exact connection to the Hermitian anti-dual is proved below.
\[
 P_s^*:H^{m-s}(X;F^*\otimes\Omega_X^{1/2})
          \longrightarrow H^{-s}(X;E^*\otimes\Omega_X^{1/2}).
 \tag{OM16}
\]
Its kernel is the bilinear annihilator of \(\operatorname{ran}P_s\), so it is finite dimensional. Its range is closed: on \((\ker P_s^*)^\perp\), the inverse bound follows from the bounded inverse of \(P_s\) on \((\ker P_s)^\perp\), transported through the exact dual maps below. The left theorem applied to \(P_s^*\) yields (OM3) after the reflected-covector and Hermitian comparisons below. The transpose symbol comes from \(p\) at the reflected covector; the actual Hermitian adjoint symbol has its own metric factors. The following proof retains both maps without identifying \(E\) with \(F\).

Conversely (OM3) makes \(pp^*:F\to F\) invertible at high frequency. The right symbol
\[
 q_R=p^*(pp^*)^{-1}:F\longrightarrow E,\qquad
 pq_R=I_F,\qquad q_R\in S^{-m}
 \tag{OM17}
\]
has the same exact inverse-derivative proof as (OM11). The right-handed finite sum \(Q_{R,N}=Q_{R,0}\sum_{j<N}R_F^j\), with \(R_F=I_F-PQ_{R,0}\in\Psi^{-1}(F,F)\), satisfies
\[
 PQ_{R,N}=I_F-R_F^N,\qquad
 PQ_R=I_F-S_F,\quad S_F\in\Psi^{-\infty}(F,F).
 \tag{OM18}
\]
Taking adjoints and using the left theorem proves that \(P_s\) has closed range and finite cokernel for every \(s\). Thus finite-codimension range at some/every order, a right symbol inverse modulo \(S^{-1}\), a right smoothing parametrix, and (OM3) are equivalent. No finite-kernel conclusion was inserted.

### The complete dual-bundle comparison

Keep the original Hermitian metrics, half-densities and Sobolev orders.
Choose a smooth positive density \(\mu\), put \(\rho=\mu^{1/2}\),
and use the convention that \(h_E(w,v)\) is linear in \(w\).
For half-density sections define the conjugate-linear bundle isomorphism
\[
 C_E(v\rho)=h_E(\,\cdot,v)\rho:
       E\otimes\Omega^{1/2}\longrightarrow E^*\otimes\Omega^{1/2},
 \quad
 \mathcal B_E(u,C_Ev)=\int_Xh_E(u,v),
 \quad
 \mathcal B_E(u,\phi)=\int_X\phi(u).
 \tag{OD1}
\]
The last two integrands are densities: in the chosen presentation
they contain the full factor \(\rho^2=\mu\). The induced dual metric
makes \(C_E\) a fibrewise conjugate-linear isometry; its inverse is
smooth. Construct \(C_F\) in the same way. In a coordinate half-density
frame \(C_Ev=M_E(x)\overline v\), and every derivative is
\[
 D^\alpha(M_E\overline v)
  =\sum_{\beta\leq\alpha}\binom{\alpha}{\beta}
       (D^{\alpha-\beta}M_E)(-1)^{|\beta|}
                          \overline{D^\beta v}.
 \tag{OD2}
\]
The identical formula holds for the inverse matrix. Complex conjugation
reflects \(\xi\) to \(-\xi\), preserving the radial Sobolev weight.
Smooth multiplication and (OD2) therefore give continuous inverse maps
on every original Sobolev order. The full proof of these distribution,
metric and density maps is [Linear distribution tests and Hermitian
adjoints](global-boundary-calculus.md#linear-distribution-tests-and-hermitian-adjoints); here we use its
half-density form (OD1), with the density still present in the pairing.

Let \(P^\dagger\) denote the formal Hermitian adjoint and \(P^{\mathrm t}\)
the bilinear transpose. Their defining pairing identities give exactly
\[
 \begin{aligned}
 P^\dagger&:H^{m-s}(F\otimes\Omega^{1/2})
                          \longrightarrow H^{-s}(E\otimes\Omega^{1/2}),\\
 P^{\mathrm t}&=C_E P^\dagger C_F^{-1}:
  H^{m-s}(F^*\otimes\Omega^{1/2})
                          \longrightarrow H^{-s}(E^*\otimes\Omega^{1/2}),\\
 \mathcal B_F(Pu,C_Fv)
   &=\int_Xh_F(Pu,v)
     =\int_Xh_E(u,P^\dagger v)
     =\mathcal B_E(u,C_E P^\dagger v).
 \end{aligned}
 \tag{OD3}
\]
Two conjugate-linear maps surrounding the linear adjoint make the
transpose linear. For function-section presentations the complete
density product is
\[
 P_\mu=\mu^{-1/2}P\mu^{1/2},\qquad
 P^\dagger_\mu=\mu^{-1/2}P^\dagger\mu^{1/2},\qquad
 P^{\mathrm t}
  =\mu^{1/2}h_E^\flat P^\dagger_\mu
                     (h_F^\flat)^{-1}\mu^{-1/2},
 \qquad h_E^\flat v=h_E(\,\cdot,v).
 \tag{OD4}
\]
These are exact products. Derivatives of the density and metric in them
remain part of the actual operators.

To verify the functional anti-dual as well, let
\(\mathcal R_{E,s}:H^{-s}(E\otimes\Omega^{1/2})
 \to(H^s(E\otimes\Omega^{1/2}))^{\mathrm{anti}}\)
send \(v\) to the conjugate-linear test functional
\(\lambda_v(u)=\int h_E(v,u)=\overline{\mathcal B_E(u,C_Ev)}\).
Sobolev duality in the linked global-index lesson makes this a continuous
linear isomorphism. Let \(\mathcal I_{E,s}\) be the Hilbert Riesz
isomorphism for the actual \(H^s\) inner product, and similarly for \(F\).
If \(P'_s\lambda=\lambda\circ P_s\) and \(P_{s,\mathrm H}^*\) is
the Hilbert adjoint between the original Hilbert spaces, then
\[
 P^\dagger=\mathcal R_{E,s}^{-1}P'_s\mathcal R_{F,s-m}
 =\mathcal R_{E,s}^{-1}\mathcal I_{E,s}
       P_{s,\mathrm H}^*
       \mathcal I_{F,s-m}^{-1}\mathcal R_{F,s-m}.
 \tag{OD5}
\]
Indeed evaluation of the first product on \(u\) is
\(\lambda_v(Pu)=\int h_F(v,Pu)=\int h_E(P^\dagger v,u)\).
The defining Hilbert-adjoint identity proves the second product.
This is the exact connection between the functional anti-dual,
Hermitian formal adjoint and the ordinary dual-bundle arrow (OM16).
No original Sobolev realization is replaced by a different one.

The starred bundle in that Sobolev provider denotes the fibrewise
anti-dual. Denote it here by \(E^{\mathrm{anti}}\), keeping
\(E^*\) for the ordinary complex-linear dual in (OM16). The exact maps,
with their half-density factors retained, are
\[
 \begin{aligned}
 \mathcal J_E &:E^*\otimes\Omega^{1/2}
                  \longrightarrow E^{\mathrm{anti}}\otimes\Omega^{1/2},
 & (\mathcal J_E\phi)(w)&=\overline{\phi(w)},\\
 \mathcal A_E &:E\otimes\Omega^{1/2}
                  \longrightarrow E^{\mathrm{anti}}\otimes\Omega^{1/2},
 & (\mathcal A_Ev)(w)&=h_E(v,w),\\
 \mathcal A_E&=\mathcal J_E C_E.
 \end{aligned}
 \tag{OA0}
\]
The first map is conjugate-linear and the second is linear; both are
bijections. Their inverses are smooth, and (OD2) with the reciprocal
Fourier Sobolev weights proves continuity in both directions at every
displayed order. If \(\mathcal S_{E,s}\) denotes the provider's
integration map from its anti-dual bundle to the functional anti-dual,
then \(\mathcal R_{E,s}=\mathcal S_{E,s}\mathcal A_E\): both sides
evaluate \(u\) as \(\int h_E(v,u)\). This proves the exact provider
comparison used in (OD5).

In coordinates the inverse in (OD2) is explicitly
\(C_E^{-1}\phi=H_E^{-1}\overline\phi
=\overline{M_E^{-1}}\,\overline\phi\), with
\(M_E=H_E^T\). The product rule in (OD2) applied to this coefficient
matrix therefore retains every inverse-metric derivative and conjugation
sign as well.

For a closed range, the bounded inverse from
\((\ker P_s)^\perp\) onto \(\operatorname{ran}P_s\) transposes to a
bounded inverse for the Hilbert adjoint between the corresponding
closed complements. Thus its kernel is the range orthogonal complement,
and its range is \((\ker P_s)^\perp\), hence closed. Equations (OD3)
and (OD5) transport both conclusions to the exact displayed spaces:
\[
 \ker P^{\mathrm t}=C_F(\ker P^\dagger),\qquad
 \operatorname{ran}P^{\mathrm t}=C_E(\operatorname{ran}P^\dagger),
 \qquad
 [\phi]\longmapsto[C_E^{-1}\phi]
 \tag{OD6}
\]
is the continuous conjugate-linear quotient isomorphism from the
transpose cokernel to the adjoint cokernel. The inverse is induced by
\(C_E\). The same maps work for range closures before imposing closed
range. Finite complex dimensions and closedness are preserved.

Finally choose metric matrices by
\(h_E(w,v)=\overline v^{\,T}H_Ew\), so \(M_E=H_E^T\) in (OD2).
The original full-symbol calculus gives, in dual coordinate frames,
\[
 \begin{aligned}
 a^\dagger(x,\xi)&=H_E(x)^{-1}\overline{p(x,\xi)}^{\,T}H_F(x)
                         +r_\dagger(x,\xi),\\
 a^{\mathrm t}(x,\xi)&=p(x,-\xi)^T+r_{\mathrm t}(x,\xi),
 \qquad r_\dagger,r_{\mathrm t}\in S^{m-1}.
 \end{aligned}
 \tag{OD7}
\]
For the transpose, exchange the two kernel variables in
\((2\pi)^{-n}\int e^{i(x-y)\cdot\xi}a(x,\xi)\,d\xi\)
and change the full integration variable to \(-\xi\). The amplitude is
\(a(y,-\xi)^T\). The complete amplitude reduction, proved in the linked
symbol calculus, supplies every derivative term; its leading term is
the second line of (OD7), and its remaining terms are precisely of
order at most \(m-1\). For the Hermitian adjoint the same kernel
calculation conjugates the matrix and retains both metric factors;
all their derivatives and the density derivatives remain in the
exact product (OD4) and its lower-order remainder.
In particular the leading terms satisfy
\[
 p(x,-\xi)^T C_Fv
   =C_E\!\left(H_E^{-1}\overline{p(x,-\xi)}^{\,T}H_Fv\right),
 \qquad
 \langle-\xi\rangle=\langle\xi\rangle.
 \tag{OD8}
\]
Because the \(C\) maps are fibrewise isometries, a lower bound for the
transpose transfers to the Hermitian principal map at \(-\xi\).
Every order-\(m-1\) remainder is bounded by a constant times
\(\langle\xi\rangle^{m-1}\), so increasing the radius preserves
at least half of any positive order-\(m\) lower bound. Reflection
then gives exactly (OM3). This proves the necessity with the original
ordinary-dual arrow retained. The signs are tested by \(P=iI\),
for which \(P^\dagger=-iI\) and \(P^{\mathrm t}=iI\), and by
\(P=D=-i\partial\) with constant metrics and coordinate density, for which
\(P^\dagger=D\) and \(P^{\mathrm t}=-D\).

### Every symbol, metric and density derivative

Work in coordinate half-density frames and the original local bundle frames. Let \(a(x,\xi)\in S^m_{1,0}\) be the full local symbol of \(P\), including the chart and support cutoffs, so \(a-p\in S^{m-1}\). Retain the inverse Fourier factor. Its kernel is
\[
K_P(x,y)=(2\pi)^{-n}\int e^{i(x-y)\cdot\xi}a(x,\xi)\,d\xi.
\tag{OA1}
\]
This is the exact distributional kernel-symbol correspondence E12. Smooth pieces arising off the coordinate diagonal can be included through their exact reconstructed full symbols; their contributions are in \(S^{-\infty}\) and are retained in the exact remainders below.

The pairing identities yield exact coordinate kernels
\[
\begin{aligned}
K_{P^{\mathrm t}}(x,y)&=K_P(y,x)^T\\
 &=(2\pi)^{-n}\int e^{i(x-y)\cdot\xi}a(y,-\xi)^T\,d\xi,\\
K_{P^\dagger}(x,y)&=H_E(x)^{-1}\overline{K_P(y,x)}^{\,T}H_F(y)\\
 &=(2\pi)^{-n}\int e^{i(x-y)\cdot\xi}
 H_E(x)^{-1}\overline{a(y,\xi)}^{\,T}H_F(y)\,d\xi.
\end{aligned}
\tag{OA2}
\]
To prove the second line, substitute a smooth \(u\) into (OD3) and interchange the two compact test variables; the coefficient of \(\overline{v(y)}\) is \(\overline{K_P(y,x)}^TH_F(y)\), and multiplication by \(H_E(x)^{-1}\) solves for the adjoint. No density coefficient is missing here: coordinate half-density contraction already produces \(|dx|\), while a function-section presentation below retains its separate coefficient \(d\).

The exact left symbols are the following oscillatory integrals, in the sense of E12 and E22:
\[
\begin{aligned}
a^{\mathrm t}(x,\xi)&=(2\pi)^{-n}\iint e^{-iw\cdot\eta}
 a(x+w,-\xi-\eta)^T\,dw\,d\eta,\\
a^\dagger(x,\xi)&=(2\pi)^{-n}H_E(x)^{-1}
 \iint e^{-iw\cdot\eta}
 \overline{a(x+w,\xi+\eta)}^{\,T}H_F(x+w)\,dw\,d\eta.
\end{aligned}
\tag{OA3}
\]
Indeed insert \(y=x+w\) in the inverse formula of E12 and shift the kernel frequency by \(\eta\). The phase is exactly \(-w\cdot\eta\). Expanding the dependence on \(w\) at zero and integrating by parts in \(\eta\) gives \(D_x^\alpha\partial_\xi^\alpha/\alpha!\), with \(D=-i\partial\). The full E20--E21 remainder theorem in the \((1,0)\) class gives, for every positive integer \(N\), the exact identities
\[
\begin{aligned}
a^{\mathrm t}
&=\sum_{|\alpha|<N}\frac1{\alpha!}
 \partial_\xi^\alpha D_x^\alpha(a(x,-\xi)^T)+r_{\mathrm t,N},\\
a^\dagger
&=H_E^{-1}\sum_{|\alpha|<N}\frac1{\alpha!}
 \partial_\xi^\alpha D_x^\alpha
   (\overline{a(x,\xi)}^{\,T}H_F(x))+r_{\dagger,N},\\
r_{\mathrm t,N},r_{\dagger,N}&\in S^{m-N}_{1,0}.
\end{aligned}
\tag{OA4}
\]
Each remainder is defined as the exact full symbol minus its displayed finite sum. In particular, no infinite series is claimed to converge. Their differentiated estimates are
\(\|\partial_x^\gamma\partial_\xi^\delta r_{*,N}\|\leq C_{N,\gamma,\delta}\langle\xi\rangle^{m-N-|\delta|}\)
on the original compact chart sets, with the finite-seminorm control furnished by the provider. All support-cutoff and smooth off-diagonal contributions belong to these actual remainders.

The transpose terms can also be written without hiding reflection derivatives:
\[
\partial_\xi^\alpha D_x^\alpha(a(x,-\xi)^T)
=(-1)^{|\alpha|}(-i)^{|\alpha|}
 ((\partial_\eta^\alpha\partial_x^\alpha a)(x,-\xi))^T.
\tag{OA5}
\]
The full Hermitian terms, with every metric derivative, are
\[
H_E^{-1}\sum_{|\alpha|<N}\sum_{\beta\leq\alpha}
 \frac1{\beta!(\alpha-\beta)!}
 (\partial_\xi^\alpha D_x^\beta\overline a^{\,T})
 (D_x^{\alpha-\beta}H_F).
\tag{OA6}
\]
Every original matrix product is ordered. The output factor \(H_E^{-1}\) is left multiplication, so there is no input-variable derivative of it in this expression. When differentiating the complete symbol, Leibniz's rule also retains every derivative of \(H_E^{-1}\). This distinguishes the actual operator coefficients from derivatives used in its symbol estimates.

For \(\mu=d(x)|dx|\), \(d>0\), put \(r(x)=d(x)^{1/2}\). The original function presentations have the exact operators
\(P_\mu=M_{r^{-1}}PM_r\) and
\(P^\dagger_\mu=M_{r^{-1}}P^\dagger M_r\).
Their complete left symbols, again with exact remainder of order \(m-N\), are
\[
\begin{aligned}
a_\mu&=r^{-1}\sum_{|\alpha|<N}
 \frac{\partial_\xi^\alpha a\,D_x^\alpha r}{\alpha!}+r_{\mu,N},\\
a^\dagger_\mu&=r^{-1}H_E^{-1}
 \sum_{|\alpha|<N}\sum_{\beta+\gamma+\delta=\alpha}
 \frac{(\partial_\xi^\alpha D_x^\beta\overline a^{\,T})
       (D_x^\gamma H_F)(D_x^\delta r)}
      {\beta!\gamma!\delta!}+r_{\dagger\mu,N}.
\end{aligned}
\tag{OA7}
\]
The first identity is E21 for right multiplication by \(r\). For the second, its exact kernel is OA2 multiplied by \(r(x)^{-1}\) on the output and \(r(y)\) on the input; expand \(\overline a^TH_Fr\) by the full multinomial rule. This proves OA7 directly, including its complete metric and density derivatives. Expanding \(D^\delta r\) further means derivatives of the original \(d^{1/2}\), with no density removed or absorbed into a new symbol.

For a differential operator \(P=\sum_\alpha A_\alpha(x)D^\alpha\), the same computation is finite and exact:
\[
\begin{aligned}
P^{\mathrm t}\phi&=\sum_\alpha(-D)^\alpha(A_\alpha^T\phi),\\
P^\dagger v&=H_E^{-1}\sum_\alpha
 D^\alpha(\overline{A_\alpha}^{\,T}H_Fv),\\
P^\dagger_\mu v&=r^{-1}H_E^{-1}\sum_\alpha
 D^\alpha(\overline{A_\alpha}^{\,T}H_Fr v).
\end{aligned}
\tag{OA8}
\]
Leibniz expansion gives every coefficient, metric, density, and input derivative. The first line follows from \(D^{\mathrm t}=-D\) for the bilinear integral; the second follows from \(D^\dagger=D\) for the constant coordinate Hermitian integral and retains the full metric product. These give additional direct sign checks for the symbol calculation.

Finally separate the actual lower-order source contribution \(a-p\) without discarding it. For every \(N\geq1\),
\[
\begin{aligned}
r_{\mathrm t}&=(a-p)(x,-\xi)^T
 +\sum_{1\leq|\alpha|<N}\frac{
 \partial_\xi^\alpha D_x^\alpha(a(x,-\xi)^T)}{\alpha!}
 +r_{\mathrm t,N},\\
r_\dagger&=H_E^{-1}(\overline{a-p}^{\,T}H_F)
 +H_E^{-1}\sum_{1\leq|\alpha|<N}\frac{
 \partial_\xi^\alpha D_x^\alpha(\overline a^{\,T}H_F)}{\alpha!}
 +r_{\dagger,N}.
\end{aligned}
\tag{OA9}
\]
All terms on each right-hand side have order at most \(m-1\). Hence
\[
a^{\mathrm t}=p(x,-\xi)^T+r_{\mathrm t},
\qquad
a^\dagger=H_E^{-1}\overline{p(x,\xi)}^{\,T}H_F+r_\dagger,
\qquad r_{\mathrm t},r_\dagger\in S^{m-1}.
\tag{OA10}
\]
These are exactly OD7, now with all lower-order contributions and their controlled remainders displayed. The exact original \(P\), \(p\), metrics and density remain in every comparison.

Both sides together say that \(p:E_x\to F_x\) is a uniformly invertible high-frequency bundle map. This is equivalent to \(P_s\) being Fredholm for one, hence every, \(s\); its index is independent of \(s\) because both kernels of \(P\) and \(P^*\) are smooth and independent of \(s\). If \(p\) is polyhomogeneous, the two one-sided high-frequency conditions reduce to injectivity and surjectivity, respectively, of its actual homogeneous principal map on the cosphere: compactness of the cosphere supplies the uniform singular-value bounds, and a lower-order change cannot alter them. For unequal bundle ranks, both sides cannot hold simultaneously.

## 6. The original mixed-order system and its exact comparison

Now keep every component and weight. Let
\[
 E=\bigoplus_{k=1}^K E_k,\quad F=\bigoplus_{j=1}^J F_j,\quad
 t_k,s_j\in\mathbb R,\quad
 P_{jk}\in\Psi^{\,t_k-s_j}(X;E_k,F_j),
 \tag{OM19}
\]
and give the input and output their original Hilbert direct sums
\[
 \mathcal H_t(E)=\bigoplus_{k=1}^K H^{t_k}(E_k),\qquad
 \mathcal H_s(F)=\bigoplus_{j=1}^J H^{s_j}(F_j),\qquad
 P:\mathcal H_t(E)\longrightarrow\mathcal H_s(F).
 \tag{OM20}
\]
Each block is bounded by the exact order \(t_k-s_j\), so the finite matrix \(P\) is bounded as displayed. In every block retain a principal representative \(p_{jk}\in S^{t_k-s_j}\); no common scalar order is assigned to the raw matrix.

For an exact comparison, use the already-constructed positive-principal order-changing isomorphisms
\[
 A=\operatorname{diag}_k J_{E_k}^{-t_k}:
       \bigoplus_k L^2(E_k)\xrightarrow{\cong}\mathcal H_t(E),\qquad
 B=\operatorname{diag}_j J_{F_j}^{s_j}:
       \mathcal H_s(F)\xrightarrow{\cong}\bigoplus_jL^2(F_j).
 \tag{OM21}
\]
The auxiliary \(T=BPA\) has order zero block by block. Its full original-factor principal map is
\[
 \widetilde p_{jk}(x,\xi)
   =\langle\xi\rangle^{s_j}p_{jk}(x,\xi)
       \langle\xi\rangle^{-t_k},
 \qquad
 P=B^{-1}TA^{-1}.
 \tag{OM22}
\]
The equalities in (OM21)–(OM22) are exact operator and principal-symbol comparisons. They preserve the raw \(P_{jk}\), the two distinct weight lists, the bundle types, and every factor. The correction terms from composing full symbols are one order lower in each block.

Applying the proven one-sided results to \(T\) and transporting back gives the mixed left criterion:
\[
 \begin{array}{c}
 P:\mathcal H_t(E)\to\mathcal H_s(F)
      \text{ has finite kernel and closed range}\\
 \Longleftrightarrow
 \widetilde p\text{ has a uniform high-frequency left lower bound}\\
 \Longleftrightarrow
 \exists\,q_{kj}\in S^{s_j-t_k}\quad
       \sum_jq_{kj}p_{j\ell}-\delta_{k\ell}I_{E_k}
          \in S^{t_\ell-t_k-1}\\
 \Longleftrightarrow
 \exists\,Q_{kj}\in\Psi^{s_j-t_k}\quad
       (QP-I_E)_{k\ell}\in\Psi^{-\infty}.
 \end{array}
 \tag{OM23}
\]
Here \(q_{kj}=\langle\xi\rangle^{-t_k}\widetilde q_{kj}
\langle\xi\rangle^{s_j}\) is the actual raw left inverse obtained from
\(\widetilde q=(\widetilde p^*\widetilde p)^{-1}\widetilde p^*\) at high frequency. Direct multiplication keeps the intermediate \(j\) index and gives
\[
 \sum_j q_{kj}p_{j\ell}
 =\langle\xi\rangle^{-t_k}
      \Bigl(\sum_j\widetilde q_{kj}\widetilde p_{j\ell}\Bigr)
        \langle\xi\rangle^{t_\ell}.
 \tag{OM24}
\]
Thus the remainder in the original \((k,\ell)\) block has order
\(t_\ell-t_k-1\), not an untyped scalar \(-1\). The full operator parametrix is \(Q=A\widetilde Q B\); exact composition gives
\(QP-I_E=A(\widetilde Q T-I_E)A^{-1}\), whose every block is smoothing. This proves both the orders and the factor placement in (OM23).

The distinct mixed right criterion is
\[
 \begin{array}{c}
 \operatorname{ran}P\text{ has finite codimension}\\
 \Longleftrightarrow
 \widetilde p\text{ has a uniform high-frequency right bound}\\
 \Longleftrightarrow
 \exists\,q_{kj}\in S^{s_j-t_k}\quad
       \sum_kp_{jk}q_{kh}-\delta_{jh}I_{F_j}
          \in S^{s_h-s_j-1}\\
 \Longleftrightarrow
 \exists\,Q_{kj}\in\Psi^{s_j-t_k}\quad
       (PQ-I_F)_{jh}\in\Psi^{-\infty}.
 \end{array}
 \tag{OM25}
\]
Its raw symbol is \(q_{kj}=\langle\xi\rangle^{-t_k}
[\widetilde p^*(\widetilde p\widetilde p^*)^{-1}]_{kj}
\langle\xi\rangle^{s_j}\), with the matrix product taken before selecting the \((k,j)\) entry. The right error is on \(F_j\leftarrow F_h\), so its precise order is \(s_h-s_j-1\). The operator identity is \(PQ-I_F=B^{-1}(T\widetilde Q-I_F)B\). This proves the one-sided analogues in their full original weighted system, including rectangular total ranks.

## 7. The two-sided mixed Fredholm criterion and its index

If \(P\) is Fredholm, (OM23) and (OM25) force both **uniform** high-frequency bounds on \(\widetilde p\). They imply equal total fiber ranks and a square inverse with \(\sup_{|\xi|\ge R}\|\widetilde p(x,\xi)^{-1}\|<\infty\), uniformly in \(x\). Conversely that uniform inverse bound supplies both raw inverse symbols with the precise block orders \(s_j-t_k\), and the asymptotic series from Section 4 produces one \(Q\) with both smoothing residuals. A cosphere-only statement is available when the weighted component symbols have actual homogeneous principal representatives: their leading square map is invertible on the compact cosphere exactly when its smallest singular value has a positive uniform lower bound, and the lower-order remainder preserves that bound above a larger radius. Conversely a uniform bound for the full symbol forces the homogeneous leading map to be injective on every ray, because a null vector there would make its full image \(O(|\xi|^{-1})\); equal ranks then make it invertible. A general \(S^0_{1,0}\) symbol need not have such a homogeneous cosphere representative. To see that the two one-sided constructions agree modulo smoothing, write their difference as
\[
 Q_L-Q_R=Q_L(I_F-PQ_R)+(Q_LP-I_E)Q_R.
 \tag{OM26}
\]
Each term is smoothing with its actual source and target type. Thus
\[
 \begin{aligned}
 P:\mathcal H_t(E)\to\mathcal H_s(F)\text{ is Fredholm}
 \quad\Longleftrightarrow\quad&
 \exists R,c>0\ \forall |\xi|\ge R:
 \|\widetilde p(x,\xi)w\|\ge c\|w\|,\\
 &\hspace{53mm}
 \|\widetilde p(x,\xi)^*v\|\ge c\|v\|
 \quad\text{for all }x,w,v .
 \end{aligned}
 \tag{OM27}
\]
Equivalently, \(\widetilde p\) is square and \(\sup_{x,|\xi|\ge R}\|\widetilde p(x,\xi)^{-1}\|<\infty\). The same \(c\) may be chosen as the smaller of the two positive constants in (OM23) and (OM25). Mere pointwise invertibility at every large covector does not suffice. On \(S^1\) with \(t=s=0\), take the scalar Fourier multiplier
\(p(\xi)=1/\log(2+\xi^2)\). Every derivative of \(\log(2+\xi^2)\) of positive order is \(O(\langle\xi\rangle^{-r})\) at order \(r\); repeated quotient differentiation and the positive lower bound on the logarithm give
\(|\partial_\xi^r p(\xi)|\le C_r\langle\xi\rangle^{-r}\), so \(p\in S^0_{1,0}\). It is positive and invertible at every \(\xi\), but \(p(k)\to0\) along the normalized Fourier modes \(e^{ikx}\). Every finite Fourier sum is in the range, so the range is dense; positivity makes the multiplier injective. If that range were closed, the bounded inverse theorem on the range would give a fixed lower bound on the images of all unit Fourier modes, contradicting \(p(k)\to0\). Thus the range is nonclosed and the operator is not Fredholm. Its inverse has no uniform high-frequency bound, exactly as (OM27) now requires.
The exact comparison (OM21) gives
\[
 \ker P=A(\ker T),\quad
 \operatorname{coker}P\xrightarrow[\ B\ ]{\cong}\operatorname{coker}T,
 \qquad \operatorname{ind}P=\operatorname{ind}T.
 \tag{OM28}
\]
The positive scalar symbols in \(A\) and \(B\) have index zero, as proved for the actual order-changing maps in the global index lesson. Consequently the analytic index of the original mixed system is exactly the analytic index of \(T=BPA\), with all component factors retained. When the weighted component symbols are polyhomogeneous, the global index lesson further identifies this integer with the index of their homogeneous invertible cosphere map. For general \(S^0_{1,0}\) symbols, (OM27) uses the full uniformly invertible high-frequency map; no homogeneous cosphere map or topological index of an absent map is asserted. The comparison does not identify the raw matrix with an order-zero matrix by omission of weights.

## 8. A separate adapted-space example

The necessity in Sections 3 and 5 concerns the *standard* Sobolev realization (OM1), and (OM27) concerns the exact weighted direct sums (OM20). It does not prohibit a nonelliptic operator from being Fredholm between a different pair of spaces. On \(\mathbb T^2\), let \(P=\partial_x\), and write Fourier coordinates \((k,\ell)\in\mathbb Z^2\). Its scalar principal map \(i\xi_x\) vanishes at every nonzero covector with \(\xi_x=0\), so it is not elliptic on standard isotropic Sobolev spaces.

**Editorial restoration of the torus Fourier factors.** Use periodic coordinates on \(\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2\), with density \(dx\,dy\), and retain
\[
 \widehat f(k,\ell)=\frac1{(2\pi)^2}\int_{[0,2\pi]^2}
 e^{-i(kx+\ell y)}f(x,y)\,dx\,dy,
 \qquad \|f\|_2^2=(2\pi)^2\sum_{k,\ell}|\widehat f(k,\ell)|^2.
 \tag{OM29a}
\]
The norm of the half-density \(f|dx\,dy|^{1/2}\) is the same displayed integral; no density factor is discarded. Set
\[
 Y=\{f\in L^2(\mathbb T^2):\widehat f(0,\ell)=0
          \text{ for every }\ell\},\qquad
 D=\{u\in Y:\partial_xu\in Y\},
 \quad \|u\|_D^2=\|u\|_2^2+\|\partial_xu\|_2^2.
 \tag{OM29}
\]
The Fourier graph norm makes \(D\) complete. The map \(P:D\to Y\) has the exact inverse
\[
 \widehat{P^{-1}f}(k,\ell)=\frac{\widehat f(k,\ell)}{ik}
 \quad(k\ne0),\qquad
 \|P^{-1}f\|_D^2
 =(2\pi)^2\sum_{k\ne0,\ell}\left(1+\frac1{k^2}\right)
        |\widehat f(k,\ell)|^2\le2\|f\|_2^2.
 \tag{OM30}
\]
Thus \(P:D\to Y\) is bijective Fredholm of index zero. These are explicitly adapted spaces. The example illustrates the exact limit of standard-Sobolev necessity without asserting the more specialized constant-strength construction.

### The exact map from the standard domain to the graph domain

The graph example has a precise connection to the original standard
Sobolev realization. Its periodic completeness and every Fourier
Sobolev factor are proved in [the compact-cylinder Fourier
foundations](arbitrary-boundary-data-reduction.md#a-compact-cylinder-with-a-missing-measurement-direction),
equations CF1--CF7; the same proof applies to the present torus.
Keep the original coordinates, density, derivative \(\partial_x\)
and all missing \(k=0\) modes. Put
\[
 Z=H^1(\mathbb T^2)\cap Y,\qquad
 \|u\|_Z^2=(2\pi)^2
    \sum_{k\ne0,\ell}(1+k^2+\ell^2)|\widehat u(k,\ell)|^2,
 \qquad I:Z\longrightarrow D,\quad Iu=u .
 \tag{OG1}
\]
Both spaces are complete in their displayed norms. The coefficient
inequality \(1+k^2\leq1+k^2+\ell^2\) proves
\(\|Iu\|_D\leq\|u\|_Z\). If \(P_Z\) and \(P_D\) denote the two
realizations of the same original derivative, then the actual maps are
\[
 P_Z=P_D I:Z\longrightarrow Y,\qquad
 I=P_D^{-1}P_Z,\qquad
 \operatorname{ran}P_Z
 =\left\{f\in Y:(2\pi)^2
    \sum_{k\ne0,\ell}\frac{1+k^2+\ell^2}{k^2}
                  |\widehat f(k,\ell)|^2<\infty\right\}.
 \tag{OG2}
\]
The inverse coefficients remain \(\widehat f/(ik)\), as in (OM30).
Necessity of the displayed range condition follows by taking the
coefficients of \(P_Zu=f\); sufficiency follows by that same division.
The kernel is zero. Finite Fourier sums in \(Y\) belong to this range,
so its closure is all of \(Y\). They are also dense in \(D\) in the
graph norm, by truncating its full weighted coefficient sum.

The range is not closed, since
\[
 u_N(x,y)=\frac{e^{i(x+Ny)}}{2\pi\sqrt{N^2+2}},\qquad
 \|u_N\|_Z=1,\qquad
 \|P_Zu_N\|_Y=(N^2+2)^{-1/2}\longrightarrow0.
 \tag{OG3}
\]
A closed range would give a bounded inverse from that range to \(Z\),
contradicting (OG3). The inclusion is proper as well:
\(u_*=\sum_{\ell\geq1}\ell^{-1}e^{i(x+\ell y)}\)
has graph norm squared
\((2\pi)^2\sum_{\ell\geq1}2\ell^{-2}<\infty\), while its \(Z\)
sum is \((2\pi)^2\sum_{\ell\geq1}(2+\ell^2)\ell^{-2}=\infty\).
Thus \(I(Z)\) is a proper dense subspace of \(D\).

This also constructs the exact object specified by the range defect:
\[
 \mathfrak D=D/I(Z),\qquad
 Y/\operatorname{ran}P_Z\xrightarrow{\;\cong\;}\mathfrak D,\qquad
 [f]\longmapsto[P_D^{-1}f],\qquad
 [u]\longmapsto[P_Du]\ \text{ for the inverse}.
 \tag{OG4}
\]
Well-definedness follows from (OG2), and both composites are the identity.
These are linear isomorphisms of the algebraic quotients and continuous
inverse maps for their quotient topologies, because \(P_D\) and its
actual inverse are bounded. Both quotient seminorms are zero, since
both subspaces being divided out are dense. The quotients are therefore
not Hausdorff; their algebraic classes have not been erased.

In fact their algebraic dimension is infinite. Split the positive
integers into the disjoint infinite sets
\(S_j=\{2^{j-1}(2q-1):q\geq1\}\), \(j\geq1\), and put
\(u_j=\sum_{\ell\in S_j}\ell^{-1}e^{i(x+\ell y)}\).
Every \(u_j\) belongs to \(D\) by the full graph sum above.
For a finite combination with any nonzero coefficient \(c_j\), the
\(Z\) sum over that set is at least
\((2\pi)^2|c_j|^2\sum_{\ell\in S_j}1=\infty\).
Disjointness prevents cancellation. Thus the classes \([u_j]\) are
linearly independent in \(\mathfrak D\), and their corresponding
\([P_Du_j]\) are independent in the actual algebraic cokernel.

### The full algebraic size of the original defect

Keep the same \(D\), \(Z\), density, Fourier factors, quotient maps, and derivative. For each real \(\alpha\in(1/2,3/2]\), define
\[
u_\alpha=\sum_{\ell\geq1}\ell^{-\alpha}e^{i(x+\ell y)}.
\tag{OG5}
\]
Its graph norm is exactly
\[
\|u_\alpha\|_D^2=2(2\pi)^2\sum_{\ell\geq1}\ell^{-2\alpha}<\infty,
\qquad P_Du_\alpha=i u_\alpha.
\tag{OG6}
\]
The convergence follows from \(2\alpha>1\) and the integral comparison for the positive decreasing summands. Thus the series converges in the original complete graph norm, and its stated derivative is its distributional derivative as proved in (OM29)--(OM30). The endpoint \(\alpha=3/2\) is included.

Consider a finite nonzero combination of distinct exponents. After discarding zero coefficients and ordering the remaining ones, write
\(1/2<\alpha_1<\cdots<\alpha_r\leq3/2\), with \(c_1\ne0\). Its exact coefficient at \((1,\ell)\) is
\[
\widehat{\sum_{j=1}^r c_ju_{\alpha_j}}(1,\ell)
=\ell^{-\alpha_1}
 \left(c_1+\sum_{j=2}^r c_j\ell^{-(\alpha_j-\alpha_1)}\right).
\tag{OG7}
\]
Every term in the last sum tends to zero, since its exponent difference is strictly positive. Choose \(L\) with
\(\sum_{j=2}^r|c_j|\ell^{-(\alpha_j-\alpha_1)}\leq|c_1|/2\)
for every \(\ell\geq L\). The triangle inequality then gives a coefficient magnitude at least \((|c_1|/2)\ell^{-\alpha_1}\), without assuming any signs or phases for the complex coefficients. Its original \(Z\) norm sum is consequently at least
\[
\frac{(2\pi)^2|c_1|^2}{4}
 \sum_{\ell\geq L}(2+\ell^2)\ell^{-2\alpha_1}
\geq\frac{(2\pi)^2|c_1|^2}{4}
 \sum_{\ell\geq L}\ell^{2-2\alpha_1}=\infty.
\tag{OG8}
\]
Here \(2-2\alpha_1\geq-1\). For \(-1\leq b<0\), the integral \(\int_L^R x^b\,dx\) diverges as \(R\to\infty\), logarithmically at \(b=-1\), and comparison proves divergence of the series. For \(b\geq0\), its summands do not tend to zero. These cover all values in OG8, including the exact upper endpoint. Hence no such combination belongs to \(Z\), proving that the classes
\[
\{[u_\alpha]:\alpha\in(1/2,3/2]\}
\quad\text{in }D/I(Z)
\tag{OG9}
\]
are linearly independent over \(\mathbb C\). By the original quotient maps (OG4), their classes \([P_Du_\alpha]\) are linearly independent in \(Y/W\) as well.

The parameter interval has cardinality \(\mathfrak c=2^{\aleph_0}\), so both algebraic quotient dimensions are at least \(\mathfrak c\). They are also at most \(\mathfrak c\): Fourier coefficients inject \(D\) and \(Y\) into \(\mathbb C^{\mathbb Z^2}\), whose cardinality is \((2^{\aleph_0})^{\aleph_0}=2^{\aleph_0\cdot\aleph_0}=\mathfrak c\); any quotient has at most the cardinality of its numerator, and a basis is a subset of that quotient. Therefore their exact Hamel dimensions are \(\mathfrak c\). This strengthening is solely about the algebraic defect. Both quotient topologies remain exactly the indiscrete topologies proved following (OG4), and the same original graph-domain derivative remains the bounded isomorphism of index zero.

The map \(P_D\) is still the original bounded graph-domain isomorphism
of index zero. Equations (OG1)--(OG4) prove exactly how it is related
to the standard-domain operator whose range is dense and nonclosed.

### Retaining every mode of the full standard realization

The OG domain retains the no-\(k=0\) condition. For completeness, its relation to the full original standard map \(P_{H^1}:H^1(\mathbb T^2)\to L^2(\mathbb T^2)\) can be made exact too. Let \(K_1\) and \(K_0\) consist of the \(k=0\) modes in \(H^1\) and \(L^2\), respectively. The original full norms give orthogonal decompositions
\[
H^1=K_1\oplus Z,
\qquad L^2=K_0\oplus Y,
\qquad
\|a\|_{K_1}^2=(2\pi)^2\sum_\ell(1+\ell^2)|\widehat a(0,\ell)|^2.
\tag{OG10}
\]
The orthogonal projections simply retain or delete the \(k=0\) coefficients and have norm one. The full derivative kills \(K_1\) and is \(P_Z\) on \(Z\). Hence
\[
\ker P_{H^1}=K_1,
\quad\operatorname{ran}P_{H^1}=W,
\quad\overline{\operatorname{ran}P_{H^1}}^{\,L^2}=Y,
\quad L^2/W\cong K_0\oplus(Y/W).
\tag{OG11}
\]
The quotient isomorphism sends \([a+f]\) to \((a,[f])\), with inverse \((a,[f])\mapsto[a+f]\); well-definedness and continuous inverse maps follow from the bounded projections and quotient topology. Similarly \(H^1/K_1\to Z\), \([a+z]\mapsto z\), is an isometric quotient isomorphism. Composing it with \(I\) and then \(P_D\) recovers precisely \(P_{H^1}\) with its target included from \(Y\) into \(L^2\). This proves an exact morphism from the full standard realization to the adapted graph-domain realization, including its original infinite nullspace and missing \(k=0\) target modes.

The Hausdorff quotient of the full cokernel is \(L^2/Y\cong K_0\); the remaining dense-range defect is the nonzero algebraic quotient \(Y/W\cong D/I(Z)\) already proved above. These maps retain both the original nullspace and the full target contribution of the zero-frequency direction.

### Why a closed graph realization can have a larger domain

Bandara, Goffeng and Saratchandran distinguish a closed operator's graph domain from the full Sobolev domain obtained under an ellipticity hypothesis; their abstract framework also permits nonelliptic operators. See [*Realisations of elliptic operators on compact manifolds with boundary*, arXiv:2104.01919v2](https://arxiv.org/abs/2104.01919v2), the Notation discussion of graph norms and closed operators, the Section 2.1 proposition on minimal elliptic domains, and the Appendix B definitions of formally adjointed pairs and their Fredholm property. Here is the exact comparison for our unchanged derivative and spaces.

Regard \(P_D=\partial_x\) as a densely defined operator on the original Hilbert space \(Y\), with domain \(D\). Its smooth core is \(\mathcal C=C^\infty(\mathbb T^2)\cap Y\). For \(u\in D\), the finite Fourier truncations
\[
u_N=\sum_{\substack{0<|k|\le N\\|\ell|\le N}}
\widehat u(k,\ell)e^{i(kx+\ell y)}
\]
converge in the full graph norm, because
\[
\|u-u_N\|_D^2=(2\pi)^2
\sum_{\substack{k\ne0\\|k|>N\ \mathrm{or}\ |\ell|>N}}
(1+k^2)|\widehat u(k,\ell)|^2\longrightarrow0.
\tag{OX1}
\]
Conversely, a graph limit in \(Y\oplus Y\) retains \(\widehat{\partial_xu}=ik\widehat u\) coefficient by coefficient and therefore belongs to \(D\). The closure of the derivative on \(\mathcal C\) and its distributional maximal realization consequently have the same domain \(D\).

The adjoint on ambient \(Y\) has exactly the opposite derivative and the same graph domain:
\[
P_D^*=-P_D,\qquad\operatorname{dom}(P_D^*)=D.
\tag{OX2}
\]
Indeed, for \(u,v\in D\), the course's inner product, linear in its first variable, gives
\[
\langle P_Du,v\rangle_Y
=(2\pi)^2\sum_{k\ne0,\ell}ik\widehat u\,\overline{\widehat v}
=(2\pi)^2\sum_{k\ne0,\ell}\widehat u\,
\overline{-ik\widehat v}=\langle u,-P_Dv\rangle_Y.
\]
Every sum converges by Cauchy--Schwarz. Conversely an adjoint-domain vector \(v\) has a representative \(g\in Y\) for this functional. Testing each mode with \(k\ne0\) forces \(\widehat g=-ik\widehat v\); its finite \(Y\) norm forces the complete graph sum defining \(D\). This proves both assertions in (OX2). Conjugating the pairing changes to the source's inner-product convention and leaves this adjoint unchanged. This star is the adjoint of the unbounded operator on \(Y\); the bounded map \(D\to Y\) uses a different domain inner product.

In the source's terminology the formally adjointed pair is exactly
\[
T_{\min}=P_D,\quad T_{\min}^{\dagger}=-P_D,
\quad T_{\max}=(-P_D)^*=P_D,
\quad T_{\max}^{\dagger}=P_D^*=-P_D.
\tag{OX3}
\]
All four domains are \(D\). Formula (OM30), including its full factor \((2\pi)^2(1+k^{-2})\), proves that both minimal maps have range \(Y\) and zero kernel. Thus this is a Fredholm formally adjointed pair in the source's definition. Its Cauchy quotient is
\[
\operatorname{dom}(T_{\max})/
\operatorname{dom}(T_{\min})=D/D=0.
\tag{OX4}
\]
The range-defect object from (OG4) has the exact comparison map
\[
\mathfrak D=D/I(Z)\longrightarrow D/D,
\qquad[u]_{I(Z)}\longmapsto[u]_D=0.
\tag{OX5}
\]
It is well defined and continuous because it is induced by the identity on \(D\); its kernel is all of \(\mathfrak D\). The infinitely many algebraic classes proved in (OG4) remain present in the source of this map.

The finite truncations in (OX1) also belong to \(Z\), so the closure of the graph of \(P_Z\) in ambient \(Y\oplus Y\) is the graph of \(P_D\). This closure is proper: the original \(u_*\) above belongs to \(D\setminus Z\). Hence \(P_Z:Z\to Y\) is bounded for its specified \(H^1\) norm, but the operator with domain \(Z\) on ambient \(Y\) is not closed. It does not contain \(T_{\min}\), as the source's definition of a realization requires.

There is also an exact compactness distinction. The modes
\[
w_\ell=\frac{e^{i(x+\ell y)}}{2\pi\sqrt2}
\quad(\ell\ge1)
\tag{OX6}
\]
have graph norm one and \(Y\) norm \(1/\sqrt2\). Distinct modes have \(Y\)-distance one, so \(D\hookrightarrow Y\) is not compact. The derivative's symbol \(i\xi_x\) vanishes at nonzero covectors with \(\xi_x=0\); the ellipticity hypothesis used to identify a minimal graph domain with a full Sobolev domain is absent. Equations (OX1)--(OX6) retain the exact domain, adjoint, quotient and compactness information responsible for the different Fredholm conclusions.

### The exact circle Fourier provider for the examples

The periodic completeness proof linked above is written on the original
two-dimensional torus. Its exact map to the circle used below is
\[
 \iota:L^2(\mathbb T;dx)\longrightarrow
 L^2(\mathbb T^2;dx\,dy),\qquad
 (\iota f)(x,y)=\frac{f(x)}{\sqrt{2\pi}},\qquad
 \|\iota f\|_2^2=\frac1{2\pi}
                  \int_0^{2\pi}\int_0^{2\pi}|f(x)|^2\,dx\,dy
                =\|f\|_2^2.
 \tag{OC1}
\]
The original coefficient conventions give exactly
\[
 \widehat f(k)=\frac1{2\pi}\int_0^{2\pi}e^{-ikx}f(x)\,dx,
 \qquad
 \widehat{\iota f}(k,\ell)
     =\frac{\delta_{\ell0}}{\sqrt{2\pi}}\widehat f(k).
 \tag{OC2}
\]
If \(f\) is orthogonal to every \(e^{ikx}/\sqrt{2\pi}\), then (OC2)
shows that \(\iota f\) is orthogonal to every
\(e^{i(kx+\ell y)}/(2\pi)\). The full torus completeness theorem
therefore gives \(\iota f=0\), hence \(f=0\). This proves circle
completeness, and the torus coefficient norm yields the full circle
Parseval factor \(\|f\|_2^2=2\pi\sum_k|\widehat f(k)|^2\).
For every original real Sobolev order \(s\), the same exact coefficient
map gives
\[
 \begin{aligned}
 \|\iota f\|_{H^s(\mathbb T^2)}^2
 &=(2\pi)^2\sum_{k,\ell}(1+k^2+\ell^2)^s
       \left|\frac{\delta_{\ell0}}{\sqrt{2\pi}}\widehat f(k)\right|^2\\
 &=2\pi\sum_k(1+k^2)^s|\widehat f(k)|^2
  =\|f\|_{H^s(\mathbb T)}^2.
 \end{aligned}
 \tag{OC3}
\]
Finite sums are dense in this circle coefficient norm by convergence of
the full weighted sum. They also show directly that the original
\(D=-i\partial_x\) has coefficient \(k\widehat f(k)\), while
\(J=\langle D\rangle\) has coefficient
\((1+k^2)^{1/2}\widehat f(k)\), at every displayed source and target
order below. No circle measure or missing coefficient factor is suppressed.

## 9. Worked examples

**Example 9.1 (left and right are different).** On the circle let \(D=-i\partial_x\), with Fourier eigenvectors \(e_k(x)=e^{ikx}\). For any real \(s\), define
\[
 P_L:H^s\longrightarrow H^{s-1}\oplus H^{s-1},
 \qquad P_Lu=(Du,0),
 \tag{OM31}
\]
and
\[
 P_R:H^s\oplus H^s\longrightarrow H^{s-1},
 \qquad P_R(v,w)=Dv.
 \tag{OM32}
\]
The first principal map sends \(z\mapsto(\xi z,0)\). For \(|\xi|\ge1\), \(|\xi|\ge2^{-1/2}\langle\xi\rangle\), so it satisfies the left bound (OM2). Its kernel is the one-dimensional constant mode. Its range is the mean-zero subspace in the first target component and zero in the second, hence is closed with infinite codimension. The second principal map sends \((z_1,z_2)\mapsto\xi z_1\); it satisfies the right bound (OM3). Its range is the mean-zero subspace of \(H^{s-1}\), of codimension one, while its kernel consists of the constant first component together with every second-component function and is infinite dimensional. These exact Fourier images show that neither one-sided conclusion can be strengthened to Fredholmness.

**Example 9.2 (four distinct component orders).** On the circle let \(J=\langle D\rangle\), the positive Fourier multiplier with eigenvalues \(\langle k\rangle=(1+k^2)^{1/2}\). Keep source weights \(t=(2,0)\) and target weights \(s=(1,-1)\). The full mixed system and its inverse are
\[
 P=
 \begin{pmatrix}
 J&J^{-1}\\ J^3&2J
 \end{pmatrix}:
 H^2\oplus H^0\longrightarrow H^1\oplus H^{-1},
 \qquad
 Q=
 \begin{pmatrix}
 2J^{-1}&-J^{-3}\\ -J&J^{-1}
 \end{pmatrix}:
 H^1\oplus H^{-1}\longrightarrow H^2\oplus H^0.
 \tag{OM33}
\]
The four input-to-output orders of \(P\) are \(1,-1,3,1\) in row order; those of \(Q\) are \(-1,-3,1,-1\). With
\(A=\operatorname{diag}(J^{-2},I)\),
\(B=\operatorname{diag}(J,J^{-1})\), the exact comparison is
\[
 BPA=\begin{pmatrix}1&1\\1&2\end{pmatrix},
 \qquad
 A^{-1}QB^{-1}
     =\begin{pmatrix}2&-1\\-1&1\end{pmatrix}.
 \tag{OM34}
\]
All entries are functions of the same \(J\), so they commute in this example; direct ordered matrix multiplication gives \(QP=I_{H^2\oplus H^0}\) and \(PQ=I_{H^1\oplus H^{-1}}\) exactly. The operator is an isomorphism and has index zero. Formula (OM24) explains why its raw inverse entries have four different component orders.

## 10. Exercises and complete solutions

**Exercise 10.1.** For \(P_L\) and \(P_R\) in Example 9.1, compute their exact kernels, ranges and cokernels. Decide which principal lower bound each satisfies, keeping the source and target ranks visible.

**Solution.** If \(Du=0\), then every nonzero Fourier coefficient \(k\widehat u(k)\) is zero, so \(\ker P_L=\mathbb C e_0\). Fourier division by \(k\ne0\) maps each mean-zero \(H^{s-1}\) function to an \(H^s\) primitive, because \(\langle k\rangle^s/|k|\le\sqrt2\langle k\rangle^{s-1}\) for \(|k|\ge1\). Thus \(\operatorname{ran}P_L=\{(f,0):\widehat f(0)=0\}\). Its quotient contains the entire second \(H^{s-1}\) component, so its codimension is infinite. The symbol \((\xi,0)^T\) has the left lower bound but its adjoint kills \((0,1)^T\), so it has no right lower bound. For \(P_R\), \(\ker P_R=\mathbb C e_0\oplus H^s\) and \(\operatorname{ran}P_R=\{f:\widehat f(0)=0\}\), of codimension one. Its symbol \((\xi,0)\) is surjective for \(\xi\ne0\) with a uniform right inverse, while it kills every \((0,z_2)\) and has no left lower bound.

**Exercise 10.2.** Multiply both matrices in (OM33) in both orders without suppressing any off-diagonal term, and verify the four weighted orders in (OM23)–(OM25).

**Solution.** The product \(PQ\) has diagonal entries \(2I-I=I\) and \(-I+2I=I\). Its off-diagonal entries are \(-J^{-2}+J^{-2}=0\) and \(2J^2-2J^2=0\). The product \(QP\) has diagonal entries \(2I-I=I\) and \(-I+2I=I\), with off-diagonal entries \(2J^{-2}-2J^{-2}=0\) and \(-J^2+J^2=0\). The \(P\) entry orders are \(t_1-s_1=1\), \(t_2-s_1=-1\), \(t_1-s_2=3\), \(t_2-s_2=1\); the \(Q\) entry orders are \(s_1-t_1=-1\), \(s_2-t_1=-3\), \(s_1-t_2=1\), \(s_2-t_2=-1\). An error of one symbolic order below \(QP\) would have block order \(t_\ell-t_k-1\), while the corresponding error below \(PQ\) would have \(s_h-s_j-1\). The exact example has both errors zero.

**Exercise 10.3.** Let \(R:H^s(S^1)\to H^{s-1}(S^1)\oplus H^{s-1}(S^1)\) be the realization of a two-component operator of order zero. Prove that \(P_L+R\) still has finite kernel and closed range and identify its extended index.

**Solution.** Every order-zero component maps \(H^s\) into \(H^s\). The embedding \(H^s(S^1)\hookrightarrow H^{s-1}(S^1)\) is compact, so \(R\) is compact into the displayed target. The compact-perturbation theorem for upper semi-Fredholm maps in the linked Fredholm lesson applies to \(P_L\). It preserves closed range, finite-dimensional kernel and the extended index. Example 9.1 gives index \(1-\infty=-\infty\), so \(P_L+R\) has the same extended value. Its individual kernel dimension need not remain one; compact stability preserves the extended difference, not each defect separately.

## 11. References and onward use

The proofs use the linked Fredholm, Sobolev, Fourier, duality and symbol-calculus lessons at their stated interfaces. The graph-domain comparison uses Lashi Bandara, Magnus Goffeng and Hemanth Saratchandran, *Realisations of elliptic operators on compact manifolds with boundary*, [arXiv:2104.01919v2](https://arxiv.org/abs/2104.01919v2), Section 2.1 and Appendix B; (OX1)--(OX6) prove every receiving assertion for the original torus derivative. Sections 6–7 keep the original mixed component orders and both separate one-sided conclusions; later index lessons may use them without replacing a rectangular map by a square one.
