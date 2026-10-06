# Pure and simple sheaves from directional tests

A constant sheaf on a submanifold can have a nonzero microlocal shift even when its ordinary stalk lies in degree zero. The normalization compares a local half-space test with three tangent Lagrangian planes. Once the test's Morse index is removed, the remaining coefficient complex is independent of the test function. Purity means that this normalized complex has one cohomological degree; simplicity also specifies its coefficient module.

Use Composing hypersurface kernels with their shifts and When a kernel quantizes a contact transformation. Throughout, \(X\) is a finite-dimensional smooth real manifold, \(n=\dim X\), and \(k\) is a commutative ring of finite global dimension. Inputs are in \(D^b(k_X)\); coefficient modules need not be finitely generated. We use the exact conormal coefficient-object model, bounded support triangles, and the microlocal half-space test identification stated below. Normal forms and the shift of a submanifold transform binds the exact written parameter Morse proof, and Local existence of contact kernel equivalences proves simultaneous normalization of finitely many smooth conic Lagrangians and transverse auxiliary planes by one hypersurface contact chart. The zero-covector conormal geometry and the conormal index calculation are proved below. The ordered index proof proves alternation, the radical formula, parity, the four-plane cocycle and constant-intersection continuity. The common-pair reduction proof proves the isotropic reduction used below.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

For simplicity and assertions that its coefficient or sheaf is nonzero, assume \(1_k\ne0\). The coefficient-complex, index and transport identities still apply to the zero ring, where all coefficient complexes vanish; we make no simplicity or nonvanishing assertion in that degenerate case. This convention adds no field, finite-generation or perfectness hypothesis.

## The test function includes a covector and a transversality condition

Let \(\Lambda\subset T^*X\) be a smooth conic Lagrangian near a point \(p=(x_0;\xi_0)\). A smooth real function \(\varphi\) is a transverse test at \(p\) when

\[
\varphi(x_0)=0,\qquad d\varphi(x_0)=\xi_0,
\qquad \Lambda\pitchfork\Lambda_\varphi\text{ at }p,
\quad \Lambda_\varphi=\{(x;d\varphi(x))\}.
\tag{1}
\]

The graph \(\Lambda_\varphi\) is Lagrangian but usually is not conic. If \(\Lambda=T_M^*X\), the last condition says that \(x_0\) is a nondegenerate critical point of \(\varphi|_M\). Indeed, in coordinates \(x=(a,b)\) with \(M=\{b=0\}\), a tangent vector common to the graph and the conormal has \(\delta b=0\) and \(\delta\xi_a=0\). The graph condition then reads
\(\operatorname{Hess}(\varphi|_M)\delta a=0\). The common tangent vanishes exactly when this Hessian is invertible.

Assume \(\operatorname{SS}(F)\subset\Lambda\) on a cotangent neighborhood of \(p\). Put

\[
C_\varphi(F)=\bigl(R\Gamma_{\{\varphi\geq0\}}F\bigr)_{x_0},
\qquad V=T_p\pi_X^{-1}(x_0),
\quad A=T_p\Lambda,
\quad B_\varphi=T_p\Lambda_\varphi,
\quad \tau_\varphi=\tau(V,A,B_\varphi).
\tag{2}
\]

The support is the **closed** side \(\varphi\geq0\). The ordered index uses \(\omega=d\theta\), as in the preceding lesson. The opposite side would change the local calculation.

We need a precise support-test prerequisite: for any bounded \(F\), when \(\varphi(x_0)=0\) and \(d\varphi(x_0)=p\ne0\),

\[
C_\varphi(F)\simeq
\mu hom(k_{\{\varphi=0\}},F)_p,
\tag{3}
\]

with the positive covector \(d\varphi(x_0)\), no additional shift, and compatibility with representatives and morphisms. Here is the exact derivation from the hypersurface microlocalization and stalk theorems `SH02-MH-SUBMANIFOLD` and `SH02-MIC-STALKS`.

Write \(H=\{\varphi=0\}\) and use \(h=\varphi\) as a normal coordinate near \(x_0\). The stalk theorem computes \((\mu_HF)_p\) by local closed supports \(Z\) whose normal cone at \(x_0\) lies in the positive normal half-line, together with zero. Every such support germ is contained in \(\{h\geq0\}\). Indeed, otherwise points \((a_j,h_j)\in Z\) would approach \(x_0\) with \(h_j<0\); in the normal deformation take positive parameters \(t_j=-h_j\). Their normal coordinates \(h_j/t_j=-1\) exhibit a negative vector in \(C_H(Z)_{x_0}\), contrary to the strict pairing condition. Conversely the normal cone of \(\{h\geq0\}\) is the nonnegative normal half-line. Thus this closed half-space is terminal among the allowed support germs. The natural support maps identify the stalk colimit with \((R\Gamma_{\{h\geq0\}}F)_{x_0}\) in every cohomological degree, hence as a bounded derived object. The submanifold-Hom theorem identifies \(\mu hom(k_H,F)_p\) with \((\mu_HF)_p\), without an antipodal map or residual codimension shift. This proves (3) naturally for arbitrary bounded \(F\). Smooth-Lagrangian containment and graph transversality are additionally needed for test independence, rather than for this comparison alone.

There is also a direct check that replacing \(F\) by an isomorphic point-localized representative does not change (2). The cone of such a replacement has microsupport avoiding \(p\). The defining microsupport vanishing test for the function \(\varphi\) makes its local support complex zero. Applying the support functor therefore makes the replacement invertible. Thus the conormal coefficient-object model can be used in the calculation below.

## Conormal sheaves give the normalization explicitly

Suppose \(\Lambda=T_M^*X\), let \(\ell=\dim M\) and \(c=n-\ell\). The local conormal model gives \(F\simeq Q_M\) at \(p\), for some \(Q\in D^b(k)\). Choose coordinates and use the Morse lemma on \(M\) to write

\[
\varphi|_M=|u|^2-|v|^2,
\qquad \dim v=m,\quad \dim u=\ell-m.
\tag{4}
\]

Local cohomology depends on this restriction, so

\[
C_\varphi(F)\simeq Q[-m].
\tag{5}
\]

Here is the local calculation, including its degree. On a sufficiently small ball in \(M\), the support triangle is the relative-cohomology triangle for that ball and its open part \(\{|u|^2<|v|^2\}\). When \(m=0\), the open part is empty and the relative complex is \(Q\). When \(m>0\), decrease \(u\) to zero and then radially normalize \(v\); the open part has the homotopy type of \(S^{m-1}\). A finite good cover, with the usual constant-coefficient acyclicity on its contractible intersections, computes its cohomology by the sphere's augmented cochain complex. The relative complex is its reduced cochain complex shifted by \([-1]\), namely \(Q[-m]\). This construction retains the map from constants on the ball to constants on the open part. It works for a complex of arbitrary coefficient modules because the finite sphere complex consists of finite free modules; tensoring it with \(Q\) retains the calculation. For \(m=1\), the open part has two components: the diagonal map \(Q\to Q\oplus Q\) has a cokernel \(Q\), and the relative complex puts it in degree one. Coordinate orientation identifies the resulting rank-one negative-direction line locally; no global trivialization is assumed.

Now compute the index directly, including mixed tangential and normal derivatives of the test. Write its Hessian at the point in blocks \(H_{aa},H_{ab},H_{ba},H_{bb}\), with \(H_{ba}=H_{ab}^T\). In the ordered three planes take vectors

\[
(0,0;u,v)\in V,\qquad
(x,0;0,y)\in A,\qquad
(s,t;H_{aa}s+H_{ab}t,H_{ba}s+H_{bb}t)\in B_\varphi.
\]

For \(\omega=d\xi\wedge dx\), the defining cyclic quadratic form of this triple is

\[
u^T(x-s)+(y-v)^Tt-x^TH_{aa}s-x^TH_{ab}t.
\]

Set \(z=x-s\), \(\widetilde u=u-H_{aa}s\), and
\(\delta=y-v-H_{ba}(s+z)\). This is an invertible change of variables when \((s,z,t,v)\) are retained. The form becomes

\[
\widetilde u^Tz+\delta^Tt-s^TH_{aa}s.
\]

The first two terms are hyperbolic pairings of equal positive and negative dimensions. The free \(v\) variables are radical. The signature is therefore \(-\operatorname{sgn}H_{aa}\), where \(H_{aa}=\operatorname{Hess}(\varphi|_M)\). Its \(m\) negative and \(\ell-m\) positive eigenvalues give

\[
\tau_\varphi=m-(\ell-m)=2m-\ell.
\tag{6}
\]

Consequently, whenever the displayed shift is integral,

\[
C_\varphi(F)[j+\tau_\varphi/2]
\simeq Q[j-\ell/2].
\tag{7}
\]

The right side contains no test function. This is the cancellation that the general definition must preserve: the local Morse group changes with the negative Hessian directions, while the inertia correction changes by exactly the compensating degree.

## A hypersurface contact kernel transports the corrected test

Let \(\chi:T^*X\to T^*X'\) be a local contact transformation at the nonzero covector \(p\), with \(\dim X'=n\). Suppose its graph, using the antipodal input convention, is the conormal of a smooth hypersurface \(S\subset X'\times X\). Set \(K=k_S\), let \(p'=\chi(p)\), and let \(T(F)=\Phi_K(F)\) denote the corresponding localized transform. In \(E=T_pT^*X\), set

\[
V'=\chi_*^{-1}\bigl(T_{p'}\pi_{X'}^{-1}(\pi_{X'}p')\bigr).
\tag{8}
\]

Choose a function \(\varphi\) with \(\varphi(x_0)=0\), \(d\varphi(x_0)=p\), whose conormal hypersurface germ is carried to \(T^*_{\{\psi=0\}}X'\), with \(\psi(\pi_{X'}p')=0\) and \(d\psi(\pi_{X'}p')=p'\). The comparison in this section holds for every bounded \(F\); no smooth-Lagrangian microsupport assumption is required for it. For the later independence application, a simultaneous choice for the conic Lagrangian and both test-level conormals is proved in the linked local-existence lesson.

Let \(A\) be any tangent Lagrangian plane under consideration, including \(T_p\Lambda\). Use \(\tau_\varphi=\tau(V,A,B_\varphi)\) and \(\tau_\psi=\tau(V',A,B_\varphi)\), identifying tangent spaces by \(\chi_*\). Here the latter index uses the transported graph-test plane. When \(A=T_p\Lambda\) for a conic \(\Lambda\), it equals the index of the actual target test \(\psi\), as verified below. Choose \(j\) with \(j+\tau_\varphi/2\in\mathbb Z\). Then

\[
C_\varphi(F)[j+\tau_\varphi/2]
\simeq C_\psi(TF)[j+\tau_\psi/2+e],
\qquad e=\frac12(n-1)+\frac12\tau(V,A,V').
\tag{9}
\]

**Proof.** Write \(H=\{\varphi=0\}\). Its conormal tangent \(B_H\) contains the radial line \(\rho\) through \(p\). Homogeneity of \(\chi\) gives \(\rho\subset V\cap V'\), independently of \(A\). The proved common-pair reduction, applied to this radial line contained in both vertical planes, shows
\(\tau(V,B_\varphi,V')=\tau(V,B_H,V')\).
Indeed the reduction of \(B_\varphi\) is the image of \(B_\varphi\cap\rho^\perp\), exactly the reduction of the hypersurface conormal tangent. A tangent vector to the graph has base component tangent to \(H\) precisely when it belongs to \(\rho^\perp\). Conormalizing this base tangent and adjoining the radial direction gives the other plane. Both three-plane reductions meet the required pairwise-intersection condition through \(V\cap V'\).

Hypersurface-kernel composition gives

\[
T(k_H)\simeq k_{\{\psi=0\}}[a],
\qquad a=1-\frac12\bigl[n+1+\tau(V,B_H,V')\bigr].
\tag{10}
\]

To obtain this particular composition, we need an endpoint that is a point. Here is a direct application of the submanifold transform with its hypotheses checked; the three-nonzero-endpoint hypersurface theorem alone would not supply it.

Put \(W=S\subset X'\times X\), \(N=S\cap(X'\times H)\), and \(f=q_{X'}|_S:W\to X'\). Choose a defining function \(h\) for \(S\) with selected physical normal \((p',-p)\). Both \(d_{X'}h\) and \(d_Xh\) are nonzero. The first makes \(dh\) and \(d\varphi\), lifted from \(X\), independent: a linear relation first has zero \(X'\)-component and therefore zero coefficient of \(dh\), then zero coefficient of \(d\varphi\). Hence \(N\) is a smooth closed hypersurface in \(W\). The second makes \(f\) a submersion, since its nonzero \(X\)-derivative can solve the tangent equation for any prescribed \(X'\)-tangent vector.

The covector \(\nu=f^*p'\) on \(W\) is nonzero because \(f\) is a submersion. Modulo the normal line of \(W\), \((p',0)\) equals \((0,p)\), so \(\nu\) is the selected conormal of \(N\). Its conormal image is \(T^*_{\{\psi=0\}}X'\) by the assumed contact image of \(T_H^*X\).

For transversality, compose the contact graph with \(T_H^*X\). The graph projection to \(T^*X\) is a local diffeomorphism, so its derivative and the derivative of that conormal inclusion are transverse. The general tangent-composition proof applies with the last endpoint symplectic space equal to zero; it does not require a nonzero covector there. Its matching kernel is zero: a vector with zero output must have zero input by the graph isomorphism. The diagonal restriction and subsequent zero-middle-covector restriction therefore have no remaining middle tangent direction. Quotienting the normal line of \(W\) gives precisely the transverse intersection of \(T_N^*W\) with the target cotangent pullback required by the submanifold transform. Thus there are no null or excess directions.

We spell out the ordered index, too. Before quotienting the normal of \(W\), lift the triple from \(T^*W\) to the ambient cotangent tangent space. That normal line lies in the vertical plane and the lifted conormal plane, so the common-pair reduction preserves its index. Lift next through the middle diagonal to
\(E_{X'}\oplus E_X^a\oplus E_X\), where the planes in order are
\[
 V_{X'}\oplus V^a\oplus V,\qquad
 \lambda_S\oplus B_H,\qquad
 V_{X'}\oplus\Delta_X.
 \tag{E1}
\]
These are two comparisons of the same lifted triple (E1). Reducing its middle diagonal normal, which is common to the first and third planes, recovers the triple before that lift; the preceding reduction of the normal of \(W\) identifies this index with \(\tau_W\). To compute the same index in another way, return to (E1) and instead reduce only the endpoint vertical \(V_{X'}\), again common to its first and third planes. The graph carries this endpoint vertical to \(V'\). This alternative reduction leaves the triple
\[
 (\,V^a\oplus V,\ (V')^a\oplus B_H,\ \Delta_X\,).
 \tag{E2}
\]
The same diagonal identity as in the ordered hypersurface-composition proof gives
\(\tau_W=\tau(V,V,B_H,V')=\tau(V,B_H,V')\); the triangle index with repeated \(V\) is zero. The point endpoint contributes the zero symplectic space and no index term. Thus the order is exactly the one in (10).

Here \(\dim W=2n-1\) and the target hypersurface has dimension \(n-1\). The transverse submanifold-transform formula consequently gives
\[
 a=\frac{1+(n-1)-(2n-1)-\tau_W}{2}
   =\frac{1-n-\tau(V,B_H,V')}{2}.
 \tag{E3}
\]
This is the exponent in (10). Local coordinate orientations give the same normalized constant coefficient; no global orientation trivialization is asserted.

Finally identify the functor, not just this exponent. On a small ambient product neighborhood, stalkwise flatness of the constant closed-support sheaf gives
\(k_S\otimes^L q_X^{-1}k_H=k_N\).
The closed-embedding projection formula therefore identifies its proper-support image with \(Rf_!k_N\), with the neighborhood restriction retained. Product neighborhoods and their intersections with \(W\) give bases for these local images. The contact graph isolates the chosen middle covector. The refined cutoff and formal-comparison theorem for composition at prescribed covectors identifies the represented formal system of these images with the localized transform \(T(k_H)\), after tensor and direct image. This uses the selected local graph's admissibility; it neither assumes global properness of \(f\) nor substitutes ordinary base restrictions for all microlocal denominators. The submanifold-transform comparison now proves (10) as an isomorphism in the stated output germ category.


Contact transport of microlocal Hom, with both its arguments transported, and (3) therefore give
\(C_\varphi(F)\simeq C_\psi(TF)[-a]\).
The negative sign is forced by shifting the **first** Hom argument by \([a]\). To compare with (9), the remaining degree is

\[
2e=\tau(V,A,B_\varphi)-2a-\tau(V',A,B_\varphi).
\tag{11}
\]

Substitute (10) and apply the four-plane cocycle identity in the order \((V,A,B_\varphi,V')\). Its index terms give
\(\tau(V,A,V')+\tau(V,B_H,V')-\tau(V,B_\varphi,V')\).
The last two terms cancel by the common-line reduction just proved. The dimension term is \(n-1\), proving (9) for an arbitrary \(A\).

For the application \(A=T_p\Lambda\), conicity supplies the additional containment \(\rho\subset A\). Thus reduction through \(V\cap A\) also gives \(\tau(V,A,B_\varphi)=\tau(V,A,B_H)\). After transport, reduction through the target radial line gives equality of the indices for the transported \(B_\varphi\), the target level-hypersurface conormal tangent, and the actual graph-test tangent \(B_\psi\). This verifies the promised interpretation of \(\tau_\psi\) for the type calculation. We did not require the arbitrary plane in the lemma to contain the radial line. Every index order and the Hom-argument shift have now been fixed. \(\square\)

For reference, graph-test transversality can also be read on the level hypersurface. At a nonzero covector the intersection of its conormal tangent with \(A\) is just \(\rho\) exactly when \(B_\varphi\cap A=0\). This follows by reducing both statements by the same radial line. It is what permits the hypersurface calculation in (10) for transverse tests.

## A smooth conic Lagrangian at the zero covector is conormal

Suppose a smooth conic Lagrangian germ \(\Lambda\subset T^*X\) contains \((x_0,0)\). Then \(\Lambda\) is the conormal of an embedded base submanifold germ near that point, including its zero covectors.

**Proof.** Identify the tangent space at a zero covector with \(T_{x_0}X\oplus T_{x_0}^*X\). Its Lagrangian plane \(A\) is invariant under every positive fibre dilation \((v,\eta)\mapsto(v,t\eta)\). If \((v,\eta)\in A\), subtract its image under any fixed \(t\ne1\): both \((0,\eta)\) and \((v,0)\) belong to \(A\). Thus \(A=P\oplus Q\), with \(P\subset T_{x_0}X\) and \(Q\subset T_{x_0}^*X\). Isotropy gives \(Q\subset P^\perp\); dimension \(n\) gives equality. Choose base coordinates \(x=(a,b)\) with \(P=\{b=0\}\), and dual coordinates \((\alpha,\beta)\). The tangent plane is \(\{\delta b=\delta\alpha=0\}\).

Projection to \((a,\beta)\) has invertible derivative on \(\Lambda\). After shrinking, the inverse function theorem therefore writes the actual germ as

\[
b=g(a,\beta),\qquad \alpha=h(a,\beta).
\]

Fibre dilation and uniqueness of this graph imply, for \(0<t\leq1\) in a common small chart,

\[
g(a,t\beta)=g(a,\beta),\qquad
h(a,t\beta)=t\,h(a,\beta).
\]

Letting \(t\to0\) gives \(g(a,\beta)=g(a,0)=g_0(a)\) and \(h(a,0)=0\). Dividing the second equality by \(t\) and differentiating at zero gives \(h(a,\beta)=d_\beta h(a,0)\beta\); smoothness at the zero fibre is essential here. Let \(M=\{b=g_0(a)\}\).

The radial vector is tangent to \(\Lambda\). Since \(\Lambda\) is isotropic, its canonical form \(\theta=\iota_R\omega\) vanishes on every tangent vector, including at the zero fibre. Evaluating on the graph's \(a\)-directions gives

\[
h(a,\beta)+dg_0(a)^T\beta=0.
\]

Consequently \(\Lambda\) has exactly the equations
\(b=g_0(a)\), \(\alpha=-dg_0(a)^T\beta\), with free small \((a,\beta)\). These are the conormal equations for \(M\). The equality includes the local zero covectors. The cases \(P=0\) and \(P=T_{x_0}X\) give a cotangent-fibre germ and the zero-section germ, respectively. No global projection image or global conormal equality is asserted. \(\square\)

## Independence of the transverse test

Let \(r=\dim(V\cap T_p\Lambda)\). If

\[
j-\frac12(n+r)\in\mathbb Z,
\tag{12}
\]

then the isomorphism class of \(C_\varphi(F)[j+\tau_\varphi/2]\) is independent of the transverse test \(\varphi\).

**Proof.** The conormal case is (7). At a nonzero \(p\), apply the proved simultaneous normalization to the three conic Lagrangian germs: \(\Lambda\) and the positive conormals of the two prescribed test level hypersurfaces. It gives a single hypersurface contact kernel carrying all three to hypersurface conormal germs. The reduced radial-intersection criterion in that proof makes both transformed tests transverse. Apply (9) to the two tests. Its extra term \(e\) depends on \(V,A,V'\), not on the test. The transformed corrected complexes agree by the conormal calculation (7), hence so do the original ones.

At a zero covector, the preceding smooth-conic proof makes \(\Lambda\) a conormal germ. Use (7) directly. The base submanifold can have any codimension; its conormal need not be the zero section.

Finally, the parity rule for three Lagrangian planes says
\(\tau_\varphi\equiv n+r\pmod{2}\), because \(B_\varphi\) is transverse to both \(V\) and \(A\). Equation (12) makes \(j+\tau_\varphi/2\) an integer. We have compared actual complexes with integral cohomological shifts. The conclusion is an isomorphism class, rather than a preferred orientation-free identification between all tests. \(\square\)

## Type, purity and simplicity

Choose a number \(d\) satisfying

\[
d\equiv \frac12\dim(V\cap T_p\Lambda)\pmod{\mathbb Z}.
\tag{13}
\]

We say that \(F\) has **type \(L\) with shift \(d\)** at \(p\) along \(\Lambda\) when

\[
C_\varphi(F)\bigl[-d+n/2+\tau_\varphi/2\bigr]\simeq L
\quad\text{in }D^b(k).
\tag{14}
\]

The exponent in (14) is an integer by (13) and the parity rule. Test independence makes the definition unambiguous. Although \(d\) may be a half-integer, (14) does not introduce a half-integer shift functor on complexes.

The sheaf is **pure** at \(p\) if this type can be chosen concentrated in degree zero. It is **simple** there if, additionally, its type is a free \(k\)-module of rank one. The condition is about \(k\), rather than a field chosen later. Pure coefficients can have torsion and arbitrary rank. A zero coefficient complex is permitted by the definition of type and purity; simplicity excludes it.

There are two useful shift rules. If \(F\) has type \(L\) with shift \(d\), then

\[
F\text{ has type }L[-b]\text{ with shift }d+b,
\qquad F[b]\text{ has type }L\text{ with shift }d+b
\quad(b\in\mathbb Z).
\tag{15}
\]

Both follow by substituting into (14). In particular one must specify the shift when naming a type complex; transferring an integer between \(d\) and \(L\) changes its displayed degree.

For the conormal model \(F=Q_M[s]\), equations (5)–(6) give

\[
\text{type at shift }d=Q[s+c/2-d].
\tag{16}
\]

Thus \(k_M\) is simple with shift \(c/2\). More generally \(Q_M[s]\) has type \(Q\) with shift \(s+c/2\). This remains true for a zero conormal covector when the stated local conormal assumptions hold.

For a smooth boundary \(h=0\) at its positive covector \(dh\), the closed upper-side sheaf \(k_{\{h\geq0\}}\) is isomorphic in the point-localized category to \(k_{\{h=0\}}\). The boundary triangle gives
\(k_{\{h\geq0\}}\simeq k_{\{h<0\}}[1]\) there: the whole constant sheaf in that triangle is null at a nonzero covector. Therefore the closed upper side is simple with shift \(1/2\), while the open lower side is simple with shift \(-1/2\). They refer to the same positive boundary covector, despite lying on opposite sides in the base.

## Contact transport changes the shift by a specified index

Under the hypersurface contact kernel of (8), if \(F\) has type \(L\) with shift \(d\), then \(TF\) has the same type with shift

\[
d'=d-\frac12(n-1)-\frac12\tau(V,T_p\Lambda,V').
\tag{17}
\]

**Proof.** Select a transverse test allowed in (9). Substitute \(j=-d+n/2\). Its left side is \(L\) by (14), while its right side has exponent
\(-d+n/2+\tau_\psi/2+e=-d'+n/2+\tau_\psi/2\).
That is precisely (14) for \(TF\) with shift \(d'\). Independence of the test proves the conclusion for every allowed transverse test. The transported test exponent is integral, so (17) has the required shift parity for the transformed tangent conormal rank. \(\square\)

This statement concerns the unshifted hypersurface kernel \(k_S\). Shifting the kernel by \([b]\) adds \(b\) to the transform's shift by (15). Nor can the three-plane index be dropped solely because the contact transformation is a local diffeomorphism: the two vertical planes generally differ.

## The coefficient type is locally constant up to integer shift

Suppose \(\operatorname{SS}(F)\cap U\subset\Lambda\) on an open cotangent region \(U\). Fix \(L\in D^b(k)\), and allow the shift in its type to vary. Then

\[
\{p\in\Lambda\cap U:F\text{ is of type }L
\text{ with some allowed shift at }p\}
\tag{18}
\]

is open and closed in \(\Lambda\cap U\).

**Proof.** Work near any chosen point. A local hypersurface contact normal form takes \(\Lambda\) to a conormal. The transformed sheaf has the coefficient model \(Q_M\) at the selected point. An isomorphism in a point-localized category is represented by a finite collection of denominator arrows. Each cone avoids that point; after shrinking a cotangent neighborhood, each cone avoids the entire neighborhood. Thus the same model holds on that neighborhood. Near a zero covector use the ordinary local conormal model directly.

In the conormal chart, (16) says that the possible type complexes are exactly the integer shifts of the fixed \(Q\). Membership in the set (18) is therefore constant throughout the chart. Formula (17) preserves the coefficient type while adjusting the allowed shift; its inverse gives the converse implication. Every point consequently has a neighborhood wholly in (18) or wholly in its complement. Both sets are open, proving the assertion. This does not say that a numerical shift is constant across a varying projection rank. \(\square\)

Locally there is also a useful object decomposition. If \(F\) has type \(L\), choose a simple object \(G\) at the point so that

\[
F\simeq L_X\otimes^L G
\quad\text{in }D^b(k_X;p).
\tag{19}
\]

To construct it, take the conormal chart just used. Its coefficient model for \(F\) is \(Q_M\); if its normalized type is \(L\), (16) identifies \(Q\) with an integral shift of \(L\). Take the correspondingly shifted \(k_M\) and carry it back by the inverse contact kernel. It is simple by (17). The constant-coefficient projection formula makes the inverse transform commute with tensoring by the arbitrary bounded \(L\), yielding (19). No choice of a global simple generator, preferred orientation line or full categorical equivalence of coefficient morphisms is asserted by this local object construction.

## Exercises with complete solutions

### Two transverse tests of the same plane

*Difficulty: Introductory.*

Let \(M\) be two-dimensional in a three-dimensional \(X\), and let \(F=k_M\). A test restricts to \(a_1^2+a_2^2\) on \(M\); another restricts to \(a_1^2-a_2^2\). Compute their raw complexes, indices and normalized types at shift \(d=1/2\).

**Solution.** The negative dimensions are zero and one. The raw complexes are \(k\) and \(k[-1]\). Formula (6) gives indices \(-2\) and zero. The exponent in (14) is respectively \(-1/2+3/2-1=0\) and \(-1/2+3/2=1\). Both normalized types are \(k\). Omitting the inertia term would give two different degrees for the same conormal sheaf.

### A half-integer is not a shift functor

*Difficulty: Introductory.*

At a point with \(n=4\) and \(\dim(V\cap T_p\Lambda)=1\), an allowed shift is \(d=3/2\). Which parity must \(\tau_\varphi\) have, and why is the exponent of (14) integral?

**Solution.** Its parity is \(n+1=5\), hence it is odd. The exponent is \(-3/2+2+\tau_\varphi/2=(1+\tau_\varphi)/2\), an integer. Only this exponent acts on the complex. The number \(d\) is part of the geometric normalization.

### Purity over an integral coefficient ring

*Difficulty: Intermediate.*

Take \(k=\mathbb Z\), a codimension-two submanifold \(M\), and \(F=(\mathbb Z/2)_M\). Is \(F\) pure or simple? What about \(\mathbb Z_M\oplus\mathbb Z_M[1]\)?

**Solution.** Formula (16) gives type \(\mathbb Z/2\) with shift one, so the first sheaf is pure. Its type is not a free rank-one \(\mathbb Z\)-module, so it is not simple; moving to a residue field would change the coefficient problem. The second sheaf has two nonzero normalized cohomology degrees for every allowed integral change of shift. It is not pure.

### Keep the kernel's own degree

*Difficulty: Intermediate.*

Suppose \(n=3\), the ordered index in (17) is zero, and \(F\) is simple with shift \(d=2\). Find the shift of its transform by \(k_S\), and then by \(k_S[2]\).

**Solution.** The unshifted kernel gives \(d'=2-(3-1)/2=1\). Shifting the kernel by two shifts the entire transform by two, so its shift becomes three. The coefficient type remains \(k\) in both cases.

### The two sides at one positive covector

*Difficulty: Intermediate.*

At \((0;dx)\) on \(\mathbb R\), compare the simple shifts of \(k_{[0,\infty)}\), \(k_{\{0\}}\) and \(k_{(-\infty,0)}\). Explain the degree in their localized relation.

**Solution.** The point sheaf and the closed positive half-line have shift \(1/2\). The open negative half-line has shift \(-1/2\). The triangle \(k_{(-\infty,0)}\to k_\mathbb R\to k_{[0,\infty)}\xrightarrow{+1}\) has null middle term at the positive covector, hence \(k_{[0,\infty)}\simeq k_{(-\infty,0)}[1]\). The difference of their simple shifts is exactly one. The open positive half-line instead is null at that covector and is not the object used here.

### An object model does not compute every morphism

*Difficulty: Advanced.*

Does (19) alone prove that \(A\mapsto A_X\otimes^L G\) is fully faithful from \(D^b(k)\) to \(D^b(k_X;p)\)? Specify the additional comparison needed.

**Solution.** No. An object decomposition supplies no computation of arbitrary derived morphisms between its coefficient factors. Full faithfulness requires the natural isomorphisms \(\operatorname{Hom}_{D^b(k)}(A,B[j])\simeq\operatorname{Hom}_{D^b(k_X;p)}(A_X\otimes^L G,B_X\otimes^L G[j])\) for all bounded \(A,B\) and all integers \(j\), compatible with identity and composition. Neither the existence of \(G\) nor (19) states these comparisons. The coefficient-equivalence lesson treats that morphism normalization as an explicit separate prerequisite.

### A test must meet the chosen covector

*Difficulty: Advanced.*

For the conormal of \(M=\{b=0\}\subset\mathbb R_a\times\mathbb R_b\), fix \(p=(0;db)\). Compare \(\varphi=b+a^2\), \(\psi=b-a^2\), and \(h=b\). Which are transverse tests, and what fails for \(h\)?

**Solution.** All three vanish at zero and have differential \(db\). The restrictions of the first two to \(M\) have nonzero Hessians, so both are transverse. Their raw complexes are \(k\) and \(k[-1]\), and their indices are \(-1\) and one. At simple shift \(1/2\) their corrected types are both \(k\). The restriction of \(h\) is identically zero; its Hessian is zero, the graph and conormal tangents have a common nonzero \(a\)-direction, and the transversality in (1) fails. Matching only the value and differential is insufficient.

### Zero covectors retain a curved base submanifold

*Difficulty: Intermediate.*

On \(T^*\mathbb R^2\), with coordinates \((a,b;\alpha,\beta)\), inspect
\(\Lambda=\{b=a^2,\ \alpha=-2a\beta\}\).
Verify smoothness, conicity and the Lagrangian property, identify its zero-fibre base germ, and compare with the positive half of a cotangent fibre at its zero endpoint.

**Solution.** The free coordinates \((a,\beta)\) parameterize \(\Lambda\); projection to them is its smooth inverse, so the image is an embedded two-dimensional manifold. Positive covector dilation multiplies both \(\alpha\) and \(\beta\) and preserves its equations. Its canonical form pulls back to
\((-2a\beta)\,da+\beta\,d(a^2)=0\).
Its symplectic form therefore vanishes, and its dimension is half the ambient dimension, so it is Lagrangian. Its zero covectors are exactly those with \(\beta=\alpha=0\), over the parabola \(M=\{b=a^2\}\); the full equations are \(T_M^*\mathbb R^2\). The zero-covector theorem keeps this curved base rather than replacing it by a point or the entire zero section. By contrast \(\{x=0,\xi\geq0\}\subset T^*\mathbb R\) has a boundary at its zero endpoint. It is not a smooth submanifold without boundary there, so it does not satisfy the theorem's hypothesis and cannot be used to infer a full two-sided conormal germ.

## References

Masaki Kashiwara and Pierre Schapira's [Microlocal study of sheaves](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §7.2, Lemmas 7.2.2–7.2.4, Definition 7.2.5 and Examples 7.2.6, pp. 123–128, supplies the closed-support Morse calculation, ordered degree correction and pure/simple module conventions. The full comparison includes the positive closed half-line shift and the negative open half-line shift. Lemma 7.2.4 is a statement about the corrected cohomology modules. The bounded coefficient-object isomorphisms and contact-transport argument written in this lesson use the stronger programme inputs stated above; the comparison with that lemma does not independently prove those inputs.

Pierre Schapira's [A short review on microlocal sheaf theory](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), dated 19 January 2016, §5.2, pp. 26–27, provides a qualitative comparison of purity and simplicity. Its proof references and discussion of the Maslov shift refer elsewhere. It is not used here as a complete proof of numerical normalization, the conormal coefficient-object model or contact equivalence.

This download contains the comparisons and solved examples written above, including the zero-covector conormal geometry, but not the complete preceding programme providers. Those dependencies include the conormal coefficient-object model, `SH02-MH-SUBMANIFOLD`, `SH02-MIC-STALKS`, the parameter Morse and submanifold-transform proofs, simultaneous contact normalization, and the ordered-index and common-pair reduction proofs. Their exact revision bindings remain to be supplied before claiming a closed proof chain. Arbitrary bounded coefficients, zero covectors and the stated nonzero-ring qualification on simplicity are retained.

The lesson and solutions are independently written teaching. No human source text or figures are reproduced; the original AI expression is CC0. The source comparison does not certify the transitive prerequisites or the whole parent course.