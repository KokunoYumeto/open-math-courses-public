# A Picard-zero deformation of the Fermat quartic

Starting with the Fermat quartic, this reading constructs a convergent family of deformation tensors and uses the finite-regularity coordinate theorem to obtain a holomorphic family. It then proves the Kähler-stability, period and integral Picard-group assertions needed to find a Picard-zero fibre. The coordinate input is stated precisely in Section 3; the convergent tensors are constructed before it is used.

*Original programme exposition by GPT-6 Astra (OpenAI), Ultra, October 2026. This independently expressed exposition is dedicated under CC0-1.0. Human sources retain their own terms.*

Take the smooth quartic surface \(X_0=\{P=0\}\subset\mathbb {CP}^3\) of The ordinary topology of the Fermat quartic, with \(P\) homogeneous of degree four. That route supplies compact connectedness, ordinary \(\pi_1(X_0)=1\) and \(b_2(X_0)=22\). Holomorphic canonical triviality is proved here, so that the complete starting data are
\[
 K_{X_0}\simeq\mathcal O_{X_0},\qquad
 \pi_1(X_0)=1,\qquad b_2(X_0)=22.                 \tag{A1}
\]
Its induced Fubini–Study metric is Kähler. The surface is kept throughout. The final sheaf counterexample continues to use \(\mathbb Q\), both arbitrary-rank weak coefficients and finite coefficients, and all complex refinements.

Here is the promised holomorphic trivialization, including the signs on overlaps. On \(\mathbb C^4\setminus\{0\}\), let \(E=\sum_{i=0}^3z_i\partial_{z_i}\) and
\[
\Omega=\iota_E(dz_0\wedge dz_1\wedge dz_2\wedge dz_3)
 =\sum_{i=0}^3(-1)^i z_i\,
 dz_0\wedge\cdots\wedge\widehat{dz_i}\wedge\cdots\wedge dz_3,
\qquad \eta=\frac{\Omega}{P}.
\]
The form \(\Omega\) has scaling weight four, as does \(P\), and \(\iota_E\Omega=0\). Hence \(\eta\) is invariant and horizontal under scalar multiplication. More explicitly, two local sections of the projective quotient differ by multiplication by a nowhere-zero holomorphic function \(a\). Pullback along this multiplication adds terms containing its derivative times \(E\); horizontality kills these terms and scaling invariance identifies the remaining terms. Thus \(\eta\) descends to one meromorphic three-form on \(\mathbb {CP}^3\), with a simple pole along \(X_0\).

On the affine chart \(z_i=1\), order the remaining three coordinates as \(w_1,w_2,w_3\) in the order of the original homogeneous coordinates with \(z_i\) omitted. Write \(P_i=P|_{z_i=1}\). The pullback of the descended form is exactly
\((-1)^i\,dw_1\wedge dw_2\wedge dw_3/P_i\).
At a point where \(\partial P_i/\partial w_j\ne0\), use \(u=P_i\) as the transverse coordinate and put \(du/u\) first in the pole decomposition. Its residue is
\[
\sigma_0\big|_{\{\partial_jP_i\ne0\}}
 =\left.
 \frac{(-1)^{\,i+j-1}\,
 dw_1\wedge\cdots\wedge\widehat{dw_j}\wedge\cdots\wedge dw_3}
 {\partial P_i/\partial w_j}
 \right|_{X_0}.
\]
Indeed \(dP_i\wedge(dw_1\wedge\cdots\widehat{dw_j}\cdots\wedge dw_3)
=(-1)^{j-1}(\partial_jP_i)\,dw_1\wedge dw_2\wedge dw_3\), which verifies both signs. The restriction is independent of the auxiliary coordinates: for the same \(u\), subtracting two pole decompositions makes their coefficient difference wedge to zero with \(du\), so their restrictions to \(u=0\) agree. Replacing \(u\) by \(u'=a u\), with \(a\) a holomorphic unit, changes \(du/u\) to \(du/u+da/a\); the extra term is holomorphic and has zero residue. Equivalently \((u'\eta)|_{X_0}=a(u\eta)|_{X_0}\) and \(du'|_{X_0}=a\,du|_{X_0}\), so the coefficient two-form is unchanged. The affine expressions therefore glue, because their meromorphic three-forms already agree.

Smoothness of the divisor means some \(\partial_jP_i\) is nonzero at each point. The two remaining coordinate differentials restrict to a basis on its tangent space, so the displayed residue is a nowhere-zero holomorphic two-form. It trivializes \(K_{X_0}\) holomorphically. No inference from topological \(c_1=0\) to holomorphic triviality has been made.

## 1. The precise linear analytic inputs and their consequences

The Dolbeault complex, Theorem 2.2, Corollary 2.3 and Theorem 3.2, proves the local \(\bar\partial\) lemma, its vector-bundle resolution, and
\[
 H^q(X,\mathcal O(E))
  =H^q\bigl(A^{0,\bullet}(X,E),\bar\partial_E\bigr).       \tag{A2}
\]
Elliptic complexes, diagonal traces, and fixed points, equations EC4–EC14a and §§11.2,13.1, supplies the compact elliptic Green operators on all Sobolev orders.

The comparison with topological cohomology has a separate precise route. On a star-shaped real chart, radial integration gives the homotopy
\(K\alpha(x)=\int_0^1t^{q-1}\iota_x\alpha(tx)\,dt\)
on a \(q\)-form, with \(dK+Kd=1\) in positive degrees and \(1-\operatorname{ev}_0\) in degree zero. The identity follows by differentiating pullback along \(x\mapsto tx\) and integrating from zero to one. Thus the smooth de Rham complex resolves the constant complex sheaf. Its terms are fine, and the partition-of-unity homotopy in the Dolbeault provider applies unchanged. Theorem 1.3 of Sheaf cohomology and singular cohomology on manifolds identifies the resulting constant-sheaf cohomology with singular cohomology. The wedge product extends constant multiplication and hence induces the same cohomology product. Its top-degree integral has the complex orientation normalization: on a chart a positive compactly supported top form of integral one represents the positive local class, and Stokes makes the integral vanish on exact forms. This identifies the form pairing below with the usual intersection pairing. The comparison uses the singular small-chain and acyclic-resolution inputs stated in that reading.

Here is the application, including the bundle and degree conventions. On a compact Hermitian complex manifold, choose a Hermitian metric on \(E\), put \(D=\bar\partial_E\), and use the formal adjoint for the volume form and these metrics. If the provider is expressed on half-densities, conjugate \(D\) by multiplication by the square root of this volume density. For a nonzero real covector \(\xi\), the symbol is multiplication by \(i\xi^{0,1}\). Its complex is exact because exterior multiplication by a nonzero covector is contracted by any vector pairing to one. The provider therefore gives
\[
 \Delta_q=D_{q-1}D_{q-1}^{*}+D_q^{*}D_q,\quad
 \Delta_qG_q=G_q\Delta_q=1-P_q,\quad
 G_q:H^s\longrightarrow H^{s+2}.                        \tag{A3}
\]
Here \(P_q\) is the finite-rank smooth harmonic projection; \(G_qP_q=P_qG_q=0\). The operators intertwine with \(D\) and its adjoint. Closed forms differ from their harmonic representatives by \(D D^*G\). This gives finite-dimensional Dolbeault cohomology and the actual primitives, rather than only a dimension statement.

We also need analytic Serre duality, but no algebraic-to-analytic substitution. It follows from (A3) as follows. The Hermitian metrics define an antilinear pointwise isomorphism
\[
 \#:A^{0,q}(E)\longrightarrow A^{n,n-q}(E^*)
 \quad\hbox{with}\quad
 \int_X u\wedge\#v=\langle u,v\rangle_{L^2}.              \tag{A4}
\]
The fibre contraction is included in the wedge. Integration by parts shows that if \(v\) is \(D\)-closed and \(D^*\)-closed, then \(\#v\) is closed and co-closed for the dual Dolbeault complex. For example, pairing \(D a\) with \(\#v\) gives \(\langle Da,v\rangle=0\), which by Stokes says \(D(\#v)=0\). Pairing \(v\) with \(D b\) in the dual complex similarly proves co-closedness of \(\#v\). The pointwise inverse gives the converse. Thus (A4) identifies the harmonic spaces in complementary degrees. The pairing is nondegenerate because \(v\) paired with \(\#v\) has value \(\|v\|^2\). Together with (A2)–(A3), this proves exactly
\[
 H^q(X,\mathcal O(E))^*
       \simeq H^{n-q}(X,\mathcal O(E^*\otimes K_X)).      \tag{A5}
\]
This proof works without assuming \(X\) is Kähler.

For the initial Kähler surface, the additional Hodge decomposition can also be obtained from (A3). In holomorphic normal coordinates for a Kähler metric, put \(\omega=i\sum_j dz_j\wedge d\bar z_j\) at the centre. Such coordinates exist because the Kähler condition makes the first holomorphic metric derivatives symmetric, and a quadratic holomorphic coordinate change cancels them. Let \(\epsilon_j,\bar\epsilon_j\) be exterior multiplication and \(\iota_j,\bar\iota_j\) the corresponding contractions. At that centre,
\[
 \Lambda=-i\sum_j\bar\iota_j\iota_j,\qquad
 [\Lambda,\partial]=i\bar\partial^*,\qquad
 [\Lambda,\bar\partial]=-i\partial^*.                    \tag{A6}
\]
Indeed the anticommutators of exterior multiplication and contraction are the Kronecker identities; the first metric derivatives vanish, so the formal adjoints have no extra coefficient terms there. Since the centre is arbitrary, the identities hold globally. The graded commutator calculation, using \(\partial^2=\bar\partial^2=\partial\bar\partial+\bar\partial\partial=0\), gives
\[
 \Delta_d=2\Delta_{\bar\partial}=2\Delta_{\partial}.       \tag{A7}
\]
For example \(\bar\partial^*=-i[\Lambda,\partial]\) yields
\(\{\bar\partial,\bar\partial^*\}=-i\{\bar\partial,[\Lambda,\partial]\}
=\{\partial,\partial^*\}\); the two mixed anticommutators vanish by the same identities. Applying (A3) to the de Rham and scalar Dolbeault complexes now decomposes de Rham harmonic forms by type. Complex conjugation interchanges their two type indices.

By (A1), \(b_1=0\); hence \(H^1(\mathcal O_{X_0})=H^0(\Omega^1_{X_0})=0\). Choose a nonzero holomorphic section \(\sigma_0\) of the trivial canonical bundle. It is nowhere zero, and contraction gives a holomorphic bundle isomorphism \(T_{X_0}\simeq\Omega^1_{X_0}\). Compact connectedness gives \(h^{2,0}=1\), conjugation gives \(h^{0,2}=1\), and \(b_2=22\) gives \(h^{1,1}=20\). Finally (A5) gives
\[
 H^2(X_0,T_{X_0})=0,\qquad
 H^0(X_0,T_{X_0})=0,\qquad
 \dim_{\mathbb C}H^1(X_0,T_{X_0})=20.                    \tag{A8}
\]
Only the last two displayed dimensions and the first vanishing are being derived. No classification of K3 lattices or general surface-degeneration theorem is used.

## 2. A convergent gauge-fixed construction

Work with \(T_{X_0}\)-valued \((0,q)\)-forms for the original complex structure. Let \(\mathcal H^1\) be their harmonic degree-one space. It is a complex vector space of dimension 20. Fix the Sobolev exponent \(s=8\) on the underlying real four-manifold.

The required multiplication estimate is elementary in finite charts. For \(r>2\), the Fourier weight inequality and Young's convolution estimate give
\[
 \|fg\|_{H^r}\leq C_r\bigl(
 \|\langle\xi\rangle^r\widehat f\|_2\|\widehat g\|_1+
 \|\widehat f\|_1\|\langle\xi\rangle^r\widehat g\|_2\bigr)
 \leq C'_r\|f\|_{H^r}\|g\|_{H^r}.                       \tag{A9}
\]
The last inequality follows by Cauchy–Schwarz and integrability of
\(\langle\xi\rangle^{-2r}\) in four dimensions. Finite smooth cutoffs and bundle frames transfer it to the compact surface.

In holomorphic coordinates, write
\(\phi=\phi_{\bar j}^{\,a}\,d\bar z_j\otimes\partial_{z_a}\).
For a degree-one tensor, fix the bracket convention
\[
 \tfrac12[\phi,\phi]_{\bar j\bar k}^{\,a}
   =\phi_{\bar j}^{\,b}\partial_b\phi_{\bar k}^{\,a}
    -\phi_{\bar k}^{\,b}\partial_b\phi_{\bar j}^{\,a}.
                                                               \tag{A10}
\]
Its polarized bracket is complex bilinear and symmetric in degree one. Its coordinate rule is the usual bracket of vector-valued forms, so it defines a global tensor. Estimate (A9) in degree seven yields
\[
 \|[\phi,\psi]\|_{H^7}\leq C\|\phi\|_{H^8}\|\psi\|_{H^8}.
                                                               \tag{A11}
\]
There is one derivative in this bracket. The Green operator in degree two gains two derivatives and \(\bar\partial^*\) loses one. Thus the symmetric bilinear map
\[
 B(\phi,\psi)=\tfrac12\bar\partial^*G_2[\phi,\psi]:
                H^8\times H^8\longrightarrow H^8
                                                               \tag{A12}
\]
has a bound \(\|B(\phi,\psi)\|_8\leq C_B\|\phi\|_8\|\psi\|_8\). This is the derivative balance needed for convergence; no unbounded formal inverse is being used.

Choose \(R>0\) with \(2C_BR<1/2\). For \(\|h\|_8<R/2\), \(h\in\mathcal H^1\), the map
\(\phi\mapsto h+B(\phi,\phi)\) takes the closed \(H^8\)-ball of radius \(R\) into itself and has contraction constant at most \(2C_BR<1/2\). Iteration therefore gives a unique solution in that ball:
\[
 \phi(h)=h+\tfrac12\bar\partial^*G_2[\phi(h),\phi(h)].     \tag{A13}
\]
For completeness, the iterates are Cauchy because each successive difference is at most \(2C_BR\) times the preceding one. Completeness of \(H^8\) gives the limit; the same estimate gives uniqueness.

The dependence on \(h\) is complex analytic. This can be checked without invoking a separate Banach implicit-function theorem: set \(\Phi_1(h)=h\) and
\(\Phi_n=\sum_{a+b=n}B(\Phi_a,\Phi_b)\).
The Catalan recursion bounds
\(\|\Phi_n(h)\|_8\leq C_{n-1}C_B^{n-1}\|h\|_8^n
\leq(4C_B)^{n-1}\|h\|_8^n\).
Thus the homogeneous complex-polynomial series converges normally on a smaller parameter ball and equals (A13). In particular
\[
 \phi(0)=0,\qquad d\phi_0(h)=h,\qquad
 \bar\partial^*\phi(h)=0,\qquad P_1\phi(h)=h.             \tag{A14}
\]
The last two equations follow from \((\bar\partial^*)^2=0\) and orthogonality to harmonics.

The surface dimension makes the integrability check especially direct. There are no \(T\)-valued \((0,3)\)-forms, and (A8) says \(P_2=0\). Hence the full degree-two Laplacian is just
\(\Delta_2=\bar\partial\bar\partial^*\), with
\(\bar\partial\bar\partial^*G_2=1\).
Applying \(\bar\partial\) to (A13) proves the actual equation
\[
       \bar\partial\phi=\tfrac12[\phi,\phi].             \tag{A15}
\]
It holds first in Sobolev spaces and then pointwise, since \(H^8\) embeds continuously into \(C^{5,\alpha}\) for every \(0<\alpha<1\). There is no unverified residual harmonic obstruction in (A15).

## 3. Precisely where a complex family is obtained

The construction uses the following coordinate theorem.

**NN.** An almost-complex structure of class \(C^{5,1/2}\) on a real 44-dimensional manifold whose \((0,1)\)-distribution is involutive admits local complex coordinates of class at least \(C^2\) in which that structure is the standard one. The coordinate changes are holomorphic. The usual stronger \(C^{6,1/2}\) coordinate conclusion suffices.

The coordinate input is developed in Integrable structures and finite-regularity coordinates, Section 1. Its finite regularity is enough for the total almost-complex structure constructed next.

On the smooth product \(X_0\times B\), for a sufficiently small ball \(B\subset\mathcal H^1\), declare the \((0,1)\)-distribution to be generated locally by
\[
 W_{\bar j}=\partial_{\bar z_j}
              -\phi_{\bar j}^{\,a}(h)\partial_{z_a},
          \qquad \partial_{\bar h_\nu}.                \tag{A16}
\]
Smallness in \(C^0\) makes this distribution complementary to its complex conjugate. Formula (A10) computes its vertical brackets: their \((1,0)\) coefficient is
\(-\bar\partial\phi+\tfrac12[\phi,\phi]\), hence zero by (A15). Brackets with \(\partial_{\bar h_\nu}\) vanish because (A13) depends holomorphically on \(h\); the parameter brackets also vanish.

The regularity here is sufficient on the total product, not just separately on each fibre. Normal convergence of the Banach-valued series gives bounded derivatives of every parameter order on smaller parameter balls with values in \(H^8\). Sobolev embedding gives their uniform spatial \(C^{5,1/2}\) bounds. The usual mean-value estimate in the parameter variables and the spatial Hölder bound give joint \(C^{5,1/2}\) regularity. The real almost-complex structure obtained from (A16) and its conjugate is therefore of that class.

By NN, (A16) gives a complex manifold \(\mathcal X\). The coordinate functions \(h_\nu\) satisfy its Cauchy–Riemann equations, so
\(\pi:\mathcal X\to B\) is holomorphic. Its complex differential is onto, since the parameter coordinates are independent; it is a holomorphic submersion. Its underlying map is the product projection, which is proper because \(X_0\) is compact. The central fibre has its original complex structure.

The Kodaira–Spencer map is the actual boundary map of
\[
 0\longrightarrow T_{X_0}\longrightarrow
 T_{\mathcal X}|_{X_0}\longrightarrow
 \mathcal O_{X_0}\otimes T_0B\longrightarrow0 .
                                                               \tag{A17}
\]
For the lift of a parameter vector \(\partial_{h_\nu}\), its Dolbeault boundary on \(W_{\bar j}\) is the vertical \((1,0)\) part of
\([W_{\bar j},\partial_{h_\nu}]
=(\partial_{h_\nu}\phi_{\bar j}^{\,a})\partial_{z_a}\).
By (A14), it represents the chosen harmonic parameter. Thus (A17) identifies \(T_0B\) with \(H^1(X_0,T_{X_0})\), with the displayed positive sign. No completeness or universality assertion about all deformations is required for the example or claimed here.

The regularity of this lift deserves an explicit check. The old product lift is only \(C^1\) in the new \(C^{2,1/4}\) coordinate atlas, while its computed central Dolbeault derivative is the smooth harmonic representative of the parameter. Choose a smooth lift of the same constant parameter section in (A17), using a smooth splitting along the central fibre. The difference is a vertical \(C^1\) section \(v\) with smooth \(\bar\partial v\). Applying \(\bar\partial^*\) gives a smooth right-hand side for the central degree-zero Dolbeault Laplacian. The smooth central-fibre elliptic regularity in (A3), applied to this distributional equation, makes \(v\) smooth. The two lifts therefore give the same Dolbeault boundary class, with the positive sign computed above. This comparison uses regularity on the original smooth central fibre and does not assume additional smoothness of the old product atlas on the total family.

## 4. Nearby canonical bundles and smooth harmonic choices

Once \(\pi\) is a proper holomorphic submersion, it has a smooth local trivialization. A short proof in this case is useful. Choose a smooth complement to its vertical tangent bundle, lift the radial paths in a smaller base ball horizontally, and solve the resulting time-dependent smooth vector-field equations. The inverse maps come from reversed paths. Properness keeps every such path lift in a compact inverse image, so local solutions extend across the whole time interval. Local existence, uniqueness and smooth parameter dependence follow from contraction of the integral equation on a sufficiently short interval; differentiation gives a linear integral equation for each parameter derivative, and induction gives all orders. Finitely many intervals suffice on that compact set. This produces a smooth trivialization and fixes the integral cohomology and fundamental group of all nearby fibres.

Using this trivialization and smooth metrics, transport the Dolbeault Laplacians to fixed Sobolev bundles. At \(0\), the degree-one scalar Laplacian has zero kernel. Its inverse \(H^{r}\to H^{r+2}\) exists by (A3). The difference from the nearby Laplacian is small as a map \(H^{r+2}\to H^r\), for instance at \(r=0\). A Neumann series therefore preserves invertibility after shrinking the base. It follows that
\[
                 H^1(X_h,\mathcal O_{X_h})=0.           \tag{A18}
\]
This proves the needed openness directly, without using a formal algebraic semicontinuity result on this analytic family.

The underlying vertical complex tangent bundle varies continuously in the family, so \(c_1(K_{X_h})=c_1(K_{X_0})=0\) under the integral identification. The locally exact holomorphic exponential sequence
\[
 0\longrightarrow\mathbb Z\longrightarrow\mathcal O
      \xrightarrow{\,f\mapsto e^{2\pi i f}\,}\mathcal O^*
      \longrightarrow1
                                                               \tag{A19}
\]
and (A18) make \(c_1:\operatorname{Pic}(X_h)\to H^2(X_h;\mathbb Z)\) injective. Consequently \(K_{X_h}\) is holomorphically trivial. Compact connectedness gives \(h^0(K_{X_h})=1\); (A5) gives \(h^2(\mathcal O_{X_h})=1\).

The harmonic projections and Green operators in these constant-dimensional spaces can be chosen smoothly in the parameter. Here is an operator justification. For a smooth family \(A_h\) of the relevant Laplacians, let \(P_0\) be the old harmonic projection. The operator \(A_h+P_0:H^{r+2}\to H^r\) remains invertible by a Neumann series. Its restriction
\(U_h=(A_h+P_0)^{-1}|_{\ker A_0}\) identifies \(\ker A_0\) with \(\ker A_h\) when the kernel dimensions are equal: \(P_0\) is injective on \(\ker A_h\), since an element in its kernel would be killed by the invertible \(A_h+P_0\); equal finite dimensions make it bijective, and the displayed inverse gives \(U_h\). The actual orthogonal projection is
\[
       P_h=U_h(U_h^*U_h)^{-1}U_h^*.                    \tag{A20}
\]
All operations are smooth. The inverse of \(A_h+P_h\), followed by \(1-P_h\), gives \(G_h\). The inverse is first constructed on \(H^2\to L^2\) on one fixed base neighbourhood. For a smooth right-hand side, elliptic regularity for the now smooth coefficients upgrades its solution to every Sobolev order. On a compact parameter neighbourhood, the elliptic estimates have uniform constants at each fixed order, since they use finitely many smooth coefficient seminorms. Differentiating the equation for the inverse gives its parameter derivatives by the same inverse and derivatives of \(A_h\); induction and those estimates prove smooth dependence in every Sobolev norm on this same neighbourhood. This does not require a new parameter ball for each derivative order. In particular there is a smooth choice of nowhere-zero fibrewise holomorphic two-form \(\sigma_h\), agreeing with \(\sigma_0\) at the origin.

## 5. The exact Kähler-stability assertion needed here

This step does not assume a general Kähler-stability theorem. Let \(\omega_0\) be the original Kähler form, and use the smooth trivialization to view all forms on a fixed manifold. The real closed forms \(\operatorname{Re}\sigma_0,\operatorname{Im}\sigma_0\) span a plane on which the pairing with \(\sigma_0\) is a real-linear isomorphism onto \(\mathbb C\), because
\(\int\sigma_0^2=0\) and \(\int\sigma_0\wedge\bar\sigma_0>0\).
The corresponding two-by-two real matrix remains invertible nearby. There are therefore unique small real numbers \(a(h),b(h)\), depending smoothly on \(h\), such that the real closed form
\[
 \eta_h=\omega_0+a(h)\operatorname{Re}\sigma_0
                    +b(h)\operatorname{Im}\sigma_0
 \quad\hbox{satisfies}\quad \int_{X_h}\eta_h\wedge\sigma_h=0.
                                                               \tag{A21}
\]
At the origin \(a=b=0\).

Put \(\beta_h=(\eta_h)^{0,2}\). It is \(\bar\partial_h\)-closed because there are no \((0,3)\)-forms. Its Serre-duality pairing with the one-dimensional \(H^0(K_{X_h})\) is zero by (A21); thus its cohomology class and harmonic projection vanish. The actual primitive is
\[
 u_h=\bar\partial_h^*G_{h,2}\beta_h,\qquad
 \bar\partial_hu_h=\beta_h .
                                                               \tag{A22}
\]
Then
\[
              \omega_h=\eta_h-d(u_h+\bar u_h)            \tag{A23}
\]
is real and closed. Its \((0,2)\) part vanishes by (A22), and its \((2,0)\) part vanishes by conjugation. It is therefore of type \((1,1)\). At \(0\), \(\beta_0=0\) and \(u_0=0\); smooth dependence shows \(\omega_h\to\omega_0\) in \(C^0\). Positive definiteness is open uniformly on the compact surface, so \(\omega_h\) is Kähler for small \(h\). This proves exactly the nearby-fibre assertion needed for this family.

## 6. Holomorphic periods and their actual differential

A holomorphic relative two-form can be obtained without an analytic base-change theorem. Start with the smooth nonzero fibrewise holomorphic \(\sigma_h\) above, regarded as a smooth section of \(K_{\mathcal X/B}\). In local holomorphic submersion coordinates \((z,h)\), its coefficient is holomorphic in \(z\). Its \(\bar\partial\) therefore has only base \((0,1)\) components, and those coefficients are again fibrewise holomorphic. Since each fibre's space of holomorphic two-forms has dimension one, there is a smooth base \((0,1)\)-form \(\alpha\) with
\(\bar\partial\sigma=\pi^*\alpha\otimes\sigma\).
The equality \(\bar\partial^2=0\) gives \(\bar\partial\alpha=0\). The programme's local Dolbeault lemma on a smaller base polydisc writes \(\alpha=\bar\partial v\). Replacing \(\sigma\) by \(e^{-v}\sigma\) yields a nonzero holomorphic relative two-form. Multiply by a constant to preserve its prescribed central value.

Every fibrewise holomorphic two-form is closed, because the fibres have complex dimension two. Its classes define a holomorphic map into the fixed cohomology space. To check holomorphicity directly, lift \(\sigma\) smoothly to a total \((2,0)\)-form \(\widetilde\sigma\). Relative holomorphicity says that \(\bar\partial\widetilde\sigma\) lies in the ideal generated by holomorphic base differentials. If \(V\) is a \((0,1)\) lift of a base \((0,1)\) vector, then \(\iota_V\widetilde\sigma=0\) and the restriction of \(\iota_Vd\widetilde\sigma\) to a fibre is zero: the \(\partial\) part has type \((3,0)\), and every remaining term retains a holomorphic base differential. Cartan's formula therefore makes the derivative of the fibre de Rham class in that base direction zero. The derivative formula follows by differentiating transported closed forms along a lift; changing the lift changes the derivative by an exact Lie derivative along a vertical field. Thus the actual periods are holomorphic.

Let \(L=H^2(X_0;\mathbb Z)\), \(V=L\otimes\mathbb C\), and \(q\) its intersection form. The map
\[
 \mathcal P:B\longrightarrow
 D=\{[\omega]\in\mathbb P(V):q(\omega,\omega)=0,\
                              q(\omega,\bar\omega)>0\},
 \qquad h\longmapsto[\sigma_h]                           \tag{A24}
\]
is consequently holomorphic. Its values lie in \(D\) because a two-form of type \((2,0)\) squares to zero on a surface, while its wedge with its conjugate is a positive volume form.

The sign and map in its derivative can be seen in the coordinates used in (A16). To first order, the deformed \((1,0)\)-covectors are
\(dz_a+\phi_{\bar j}^{\,a}\,d\bar z_j\).
Expanding a deformed \((2,0)\)-form therefore gives mixed component
\[
                  \dot\phi\mathbin{\lrcorner}\sigma_0. \tag{A25}
\]
Here the convention is
\((d\bar z_j\otimes v)\mathbin{\lrcorner}\sigma_0
=d\bar z_j\wedge\iota_v\sigma_0\); this agrees with the positive boundary-map sign in (A17). Differentiation of closedness makes the total first derivative a closed two-form. Its \((0,2)\) component is zero. Its \((1,1)\) component is \(\bar\partial\)-closed, and (A3),(A7) identify its Dolbeault class with the \((1,1)\) harmonic component of its de Rham class. The possible \((2,0)\) harmonic component is a multiple of \(\sigma_0\), which disappears upon projectivizing.

Differentiating the quadric equation identifies
\[
 T_{[\sigma_0]}D
   =\operatorname{Hom}(\mathbb C\sigma_0,
                          \sigma_0^\perp/\mathbb C\sigma_0).
                                                               \tag{A26}
\]
The central Hodge decomposition identifies the quotient with \(H^{1,1}(X_0)\). Equations (A14),(A17),(A25) show that \(d\mathcal P_0\) is exactly contraction
\(H^1(T_{X_0})\to H^1(\Omega^1_{X_0})\), after evaluating on \(\sigma_0\). It is an isomorphism. Both sides have dimension 20. The finite-dimensional holomorphic inverse-function theorem now makes \(\mathcal P\) an isomorphism onto a nonempty open part of \(D\), after shrinking. That theorem also follows from the contraction proof used above, applied to a holomorphic map whose derivative has been normalized to the identity. No global period-surjectivity theorem or global Torelli theorem is needed.

## 7. The integral Picard group, not just its rank

Simple connectivity implies \(H_1(X_0;\mathbb Z)=0\). The universal-coefficient sequence makes \(L\) torsion-free, and compactness makes it finitely generated of rank 22. Poincaré duality makes \(q\) nondegenerate. These properties persist on every fibre by the product topology.

For \(0\ne\lambda\in L\), the equation \(q(\lambda,\omega)=0\) cuts a closed analytic subset \(D_\lambda\) with empty interior in \(D\). Here is an elementary verification of the last assertion. Near any isotropic line, choose an isotropic partner pairing to one and the nondegenerate complementary space \(W\). In the projective chart the quadric is
\[
      \omega=(1,-q_W(w)/2,w),\qquad w\in W .
                                                               \tag{A27}
\]
A linear functional restricting to zero on a nonempty open set would give a polynomial
\(a-bq_W(w)/2+\ell(w)\) identically zero. Its quadratic, linear and constant terms force \(b=0,\ell=0,a=0\). Thus the linear functional is zero; nondegeneracy of \(q\) would force \(\lambda=0\), a contradiction.

Enumerate the nonzero elements of the countable lattice. Inside the open period image choose a closed coordinate ball. Successively choose a smaller closed ball inside the interior of the preceding ball and outside \(D_{\lambda_n}\), with radius less than \(2^{-n}\). This is possible because each \(D_{\lambda_n}\) is closed with empty interior. Compactness of the initial ball and the nested-ball property give a point in all these balls. Its period is orthogonal to no nonzero integral class.

For a holomorphic line bundle \(A\) on the corresponding fibre, \(c_1(A)\) has a real closed representative of type \((1,1)\). This fact does not require the converse Lefschetz \((1,1)\) theorem. Choose a Hermitian metric in holomorphic local frames. Its Chern connection has local form \(\partial\log h\), and the curvature is \(F=\bar\partial\partial\log h\), of type \((1,1)\). Transition by a holomorphic nowhere-zero function changes the connection by its logarithmic differential; the curvature glues, and the exponential-sequence cocycle computation identifies \([iF/(2\pi)]\) with the image of the integral \(c_1(A)\) in the usual positive complex convention. Indeed choose local logarithms of the transition functions; their sums on triple overlaps are \(2\pi i\) times the integral connecting cocycle, and the differences of the local connection forms are the differentials of those logarithms. This is the Čech–de Rham representative calculation, with the dual change for coefficients versus frames. Wedge with \(\sigma_h\) has type \((3,1)\), so
\(q(c_1(A),\sigma_h)=0\).
The selected period therefore kills \(c_1(A)\) in the torsion-free integral lattice, not merely after quotienting by torsion. By the injection from (A18)–(A19), \(A\) is trivial. Hence
\[
              \operatorname{Pic}(X_h)=0,\quad
              \pi_1(X_h)=1,\quad
              H^2(X_h;\mathbb Q)\simeq\mathbb Q^{22}.    \tag{A28}
\]
The fibre is a compact connected complex K3 surface. Together with NN and the ordinary quartic topology, it gives exactly the geometry required by the complex-constructible sheaf example.

## 8. Why finite regularity suffices

The construction above proves complex-analytic parameter dependence into \(H^8\) and joint \(C^{5,1/2}\) regularity. A formal differentiation of (A15) and the gauge equation has linearized principal operator
\[
 \psi\longmapsto
       \bigl(\bar\partial\psi-[\phi,\psi],
                              \bar\partial^*\psi\bigr). \tag{A29}
\]
For small \(\|\phi\|_{C^0}\), its symbol is an invertible perturbation of the elliptic odd-to-even Dolbeault–Dirac symbol. This suggests the usual quasilinear elliptic bootstrap. It does not, by itself, prove that bootstrap: the coefficients initially have only the regularity already obtained for \(\phi\), whereas the programme parametrix theorem is stated for smooth coefficients. Re-running the contraction separately in every higher Sobolev space also does not give one common nonzero parameter ball unless uniform radii are proved.

The construction uses NN at finite regularity and requires no rough-coefficient bootstrap estimate. A separately proved quasilinear estimate giving smooth spatial and joint parameter regularity would allow a smooth coordinate theorem instead; that optional upgrade is not used here.

## Sources and mathematical scope

Daniel Huybrechts’s [*Lectures on K3 surfaces*, 449-page author final draft dated 4 January 2016](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf) is the source edition used here. The [author’s edition page](https://www.math.uni-bonn.de/people/huybrech/K3.html) distinguishes this draft from the corrected published edition. Chapter 6, pp.103–108, gives the local-period framework and attributes the general existence theorem to Kuranishi and Kodaira; p.103 expressly says that existence is only stated, and Theorem 2.5 on p.107 has no supplied proof. The derivative discussion on pp.105–106 describes Griffiths transversality and a spectral-sequence route. The proof above instead supplies the gauge equation, actual Sobolev convergence, surface integrability calculation, canonical-line and Kähler correction, relative-form argument, and explicit tensor derivative. Those are independently written classical arguments, not a claim of new theorems.

Chapter 1, pp.13–17, records the K3 invariants and exponential-sequence facts but invokes additional Hodge and Riemann–Roch inputs; the argument here uses the separately retained quartic topology and proves its precise Hodge/Serre bridges from the programme's compact elliptic and Dolbeault contracts. Chapter 16, p.354, states the very-general Picard-zero assertion; its coherent-derived-category material is not used. The author makes the draft available for personal use and forbids its sale or redistribution. Its terms are separate from the CC0 dedication of this independently written exposition.
