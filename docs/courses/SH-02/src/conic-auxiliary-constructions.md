# Convex tests and radial comparisons

This supplement supplies geometric constructions and the specified sheaf maps used in conic Fourier calculations. The arguments use the previously proved results identified below. The conic and Fourier–Sato theory and its sphere-bundle applications go back to M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §2.1 and §5.1.

## SH02-CAX-CONTRACT — Objects and dependencies

For the sheaf statements, let \(k\) be a commutative unital ring of finite global dimension. All spaces called locally compact are Hausdorff. Let \(\tau:E\to B\) be a real vector bundle of fixed finite rank \(n\) over an arbitrary locally compact base, and write \(\pi:E^*\to B\) for its dual. No compactness, countability, manifold condition or finite-dimensionality is imposed on \(B\). Complexes have bounded-below cohomology, with no upper bound, constructibility condition or finite-generation assumption on stalks.

Use the Fourier functor \(T_E\), its negative-pairing convention and its positive-support ordinary-image presentation from [SH02-FS-SETUP and SH02-FS-COMPARE](../../sheaf-proof-readings/SH02-fourier-sato.html). Use the region formula FS13 in [SH02-FS-SECTIONS](../../sheaf-proof-readings/SH02-fourier-sato.html), and the canonical restriction and interval-unit isomorphisms proved in [SH02-CON-RESTRICTION and SH02-CON-CYLINDER](../../sheaf-proof-readings/SH02-conic-descent.html). The latter proof uses the closed-exhaustion comparison, Milnor calculation and noncompact-strip case in [SH02-EXH-COMPARISON, SH02-EXH-MILNOR and SH02-EXH-STRIPS](../../sheaf-proof-readings/SH02-closed-exhaustion.html).

The ordinary sheaf operations used below are exact inverse image, derived direct image and sections, adjunction, composition, localization, and stalk detection. Their comparison maps are fixed by SH02-IMP-ADJUNCTION, SH02-IMP-BASECHANGE-MORPHISM, SH02-IMP-LOCALIZATION and SH02-IMP-HOM-PULLBACK, with the adjunction verifications in the prerequisite proofs. The construction of a comparison alone never supplies its invertibility; the required ordinary base change is proved below. The Fourier results retain their separately specified proper-support and orientation dependencies.

For a locally closed \(A\subset Y\), let \(k_A^Y\) denote the constant sheaf extended by zero in \(Y\). Write

\[
R\Gamma_A(Y;H)=R\operatorname{Hom}_{k_Y}(k_A^Y,H).
\]

This is a complex of \(k\)-modules. For closed \(A\), the corresponding sheaf object is \(R\Gamma_AH=R\mathcal Hom(k_A^Y,H)\). These two notations distinguish global supported sections from their sheaf version. Positive scalar invariance means the conicity convention of SH02-FS-SETUP; on a vector bundle the nonzero positive orbits are embedded rays and the zero vectors are fixed points.

## SH02-CAX-STAR-SHAPED — Reparametrizing an open radial region

The next three results are statements about finite-dimensional real spaces and do not involve coefficients.

**Lemma.** Let \(H\) be a finite-dimensional Euclidean space, and let \(W\subset H\) be open, contain zero, and contain every segment from zero to one of its points. There is an explicit homeomorphism \(\Psi:W\to H\).

**Proof.** If \(W=H\), put \(d=1\). Otherwise put

\[
d(z)=\min\{1,\operatorname{dist}(z,H\setminus W)\}.
\]

Distance to a fixed nonempty set is 1-Lipschitz: the triangle inequality gives \(\operatorname{dist}(x,A)\le\|x-y\|+\operatorname{dist}(y,A)\), and exchanging \(x,y\) gives the other inequality. Truncation at one preserves this bound. Since \(W\) is open, \(d\) is strictly positive on \(W\). Define

\[
\Psi(z)=z\int_0^1\frac{dt}{d(tz)}.
\tag{CAX10}
\]

The segment \([0,z]\) is compact and lies in \(W\), so \(d\) has a positive minimum \(m\) on it. This proves that the integral is finite. If \(z'\) is within \(m/2\) of \(z\), the Lipschitz bound gives \(d(tz')\ge m/2\) for \(0\le t\le1\), and

\[
\left|\frac1{d(tz')}-\frac1{d(tz)}\right|
\le\frac{2}{m^2}\|z'-z\|.
\]

Integration proves continuity of the integral and hence of \(\Psi\).

Suppose first that \(\dim H>0\). For each unit vector \(u\), openness and the segment condition give

\[
\{r\ge0:ru\in W\}=[0,R(u)),\qquad 0<R(u)\le\infty.
\]

A finite endpoint is omitted because membership in the open set would allow a larger radius. Substitution in CAX10 gives

\[
\Psi(ru)=h_u(r)u,\qquad
h_u(r)=\int_0^r\frac{ds}{d(su)}.
\tag{CAX11}
\]

This is a continuous strictly increasing function with \(h_u(0)=0\) and \(h_u(r)\ge r\). Thus it tends to infinity if \(R(u)=\infty\). If \(R(u)<\infty\), the point \(R(u)u\) is outside \(W\), whence \(d(su)\le R(u)-s\). For \(0<r_0<r<R(u)\),

\[
h_u(r)-h_u(r_0)
\ge\int_{r_0}^{r}\frac{ds}{R(u)-s}
=\log\frac{R(u)-r_0}{R(u)-r}.
\]

It again tends to infinity at the endpoint. The intermediate value theorem now makes \(h_u\) a bijection from its radial interval onto \([0,\infty)\). Consequently \(\Psi\) is bijective, with inverse at \(w\ne0\) given by \(ru\), where \(u=w/\|w\|\) and \(r\) is the unique solution of \(h_u(r)=\|w\|\).

We check continuity of this inverse. At zero, \(h_u(r)\ge r\) gives \(\|\Psi^{-1}(w)\|\le\|w\|\). At \(w_0\ne0\), write \(u_0=w_0/\|w_0\|\) and let \(r_0\) be the inverse radius. Choose

\[
0<r_-<r_0<r_+<R(u_0).
\]

For directions \(u\) close to \(u_0\), openness keeps \(r_-u,r_+u\) in \(W\). Continuity of \(\Psi\) makes \(h_u(r_-)\) and \(h_u(r_+)\) continuous in these directions. Therefore, for \(w\) close to \(w_0\),

\[
h_{w/\|w\|}(r_-)<\|w\|<h_{w/\|w\|}(r_+).
\]

Its inverse radius lies between \(r_-\) and \(r_+\). These brackets can be chosen arbitrarily close to \(r_0\), proving continuity. If \(\dim H=0\), then \(W=H=\{0\}\) and CAX10 is its identity map. The proof uses no regularity assumption on the radial endpoint function \(R\). \(\square\)

## SH02-CAX-CONE-COMPLEMENT — Removing a nonzero pointed cone

**Theorem.** Let \(L\) be a finite-dimensional real vector space and \(C\subset L\) a nonzero closed convex cone containing no line. A cone here contains zero and is closed under nonnegative scalar multiplication. Then \(L\setminus C\) is homeomorphic to \(L\). The cone may have empty interior in \(L\).

**Proof.** Choose an inner product and a unit vector \(q\in C\). Pointedness gives \(-q\notin C\). Let \(H=q^\perp\). On the unit sphere, stereographic projection from \(q\) and its inverse are

\[
p(u)=\frac{u-\langle u,q\rangle q}{1-\langle u,q\rangle},
\qquad
s(z)=\frac{2z+(\|z\|^2-1)q}{1+\|z\|^2}.
\tag{CAX12}
\]

For completeness, the squared norm of the numerator of \(s(z)\) is
\(4\|z\|^2+(\|z\|^2-1)^2=(1+\|z\|^2)^2\). Its \(q\)-coordinate is strictly less than one, and substitution gives \(p(s(z))=z\). Conversely, if \(a=\langle u,q\rangle<1\), the squared norm of \(p(u)\) is \((1+a)/(1-a)\). Substitution into \(s\) gives the perpendicular component \(u-aq\) and the \(q\)-component \(a\). Thus \(s(p(u))=u\), and the displayed continuous maps are inverse homeomorphisms.

Let \(W=\{z\in H:s(z)\notin C\}\). It is open and contains zero because \(s(0)=-q\). Since \(q\in C\), stereographic projection identifies the entire sphere complement with \(W\). We verify that \(W\) has the segment property of the preceding lemma. Write

\[
v(z)=2z+(\|z\|^2-1)q.
\]

Membership of \(v(z)\) and \(s(z)\) in the cone is equivalent. For \(0<\lambda\le1\), direct comparison of the perpendicular and parallel components gives

\[
v(z)=\lambda^{-1}v(\lambda z)
+(1-\lambda)(\|z\|^2+\lambda^{-1})q.
\tag{CAX13}
\]

Both coefficients are nonnegative. If \(z\in W\) but \(\lambda z\notin W\), convexity and conicity would force \(v(z)\in C\), a contradiction. The remaining endpoint zero is in \(W\). Thus SH02-CAX-STAR-SHAPED gives the homeomorphism \(\Psi:W\to H\).

For \(x\notin C\), put \(r=\|x\|>0\) and

\[
z(x)=\frac{x-\langle x,q\rangle q}{r-\langle x,q\rangle}.
\]

The denominator is positive: equality would imply \(x=rq\in C\). The required homeomorphism and its inverse are

\[
\begin{aligned}
\Phi(x)&=-(\log r)q+\Psi(z(x)),\\
\Phi^{-1}(tq+w)&=e^{-t}s(\Psi^{-1}(w)),
\qquad t\in\mathbb R,\ w\in H.
\end{aligned}
\tag{CAX14}
\]

They are continuous by the preceding lemma and the displayed formulas. Since \(s\) has unit norm and positive scaling preserves both the cone and its complement, substitution shows that they are inverse. This proves the assertion.

In dimension one, \(H=\{0\}\); the cone is a closed halfline and the formula reduces to \(-rq\mapsto-(\log r)q\). For a single ray in any dimension, \(W=H\) and \(\Psi\) is the identity. These observations also check cones of lower dimension. A nonzero cone cannot occur in dimension zero. \(\square\)

The nonzero hypothesis is essential: \(\mathbb R\setminus\{0\}\) has two components. The choices in CAX14 are made in the individual vector space under consideration.

## SH02-CAX-FIBRE-CUT — Detecting the nonzero cone in a fibre

Let \(\Gamma\subset E\) be closed, conic, and contain the zero section. Define its polar in the full dual bundle by nonnegative pairing in every fibre. Then

\[
\operatorname{Int}(\Gamma^\circ)
=\{(b,\eta):\langle x,\eta\rangle>0
\text{ for every nonzero }x\in\Gamma_b\}.
\tag{CAX15}
\]

The interior is taken in the total bundle topology.

**Proof.** Trivialize over an open part \(B_1\subset B\), and choose a Euclidean norm on the fibre \(\mathbb R^n\). For \(n>0\), the set

\[
\{(b,\eta,u)\in B_1\times(\mathbb R^n)^*\times S^{n-1}:
(b,u)\in\Gamma,\ \langle u,\eta\rangle\le0\}
\]

is closed. Projection along the compact sphere is closed. Indeed, if a point is outside the projection of a closed subset of \(Z\times K\), choose product neighbourhoods of its pairs with all points of compact \(K\), disjoint from that closed subset. A finite subcover in \(K\), followed by intersection of the corresponding neighbourhoods in \(Z\), gives a neighbourhood outside the projection. The complement of this projection is precisely the strict-positivity set in CAX15. It is open and lies in the polar, because every nonzero cone vector can be normalized to the sphere. It therefore lies in the total interior.

Conversely, a negative pairing at a nonzero \(x\in\Gamma_b\) places \(\eta\) outside the polar. If the pairing is zero, replace \(\eta\) by \(\eta-\varepsilon x^\flat\), using the functional from the chosen inner product. This gives a negative pairing and approaches \(\eta\) as \(\varepsilon\downarrow0\), within the same fibre. Thus \(\eta\) is outside the total interior. For \(n=0\), the polar is the entire dual bundle and the strict condition is vacuous, so the equality holds directly. \(\square\)

Suppose now that \(\Gamma\) is also fibrewise convex and contains no fibre line. If \((b,\eta)\notin\operatorname{Int}(\Gamma^\circ)\), CAX15 shows that

\[
C_{b,\eta}=\Gamma_b\cap\{x:\langle x,\eta\rangle\le0\}
\]

is nonzero. It is closed, convex, conic and pointed, as an intersection of the pointed cone \(\Gamma_b\) with a closed linear halfspace. Hence CAX14 supplies \(E_b\setminus C_{b,\eta}\simeq E_b\) at the full hypotheses used in the closed-cone Fourier calculation. This conclusion is fibrewise and requires only local bundle charts. The compactly supported cohomology vanishing for this cone is also proved directly in SH02-FS-HALFSPACE; its sheaf-theoretic comparison maps retain the orientation-trace prerequisites stated there.

## SH02-CAX-SATURATION — Enlarging a convex open test set

Let \(U\subset E^*\) be open in the total space and convex in each fibre. It need not be a cone. Set

\[
B_0=\pi(U),\qquad E_0=\tau^{-1}B_0,\qquad
V=\bigcup_{s>0}sU.
\]

Define the polar with its base support included:

\[
A=U^\circ
=\{x\in E_0:\langle x,\xi\rangle\ge0
\text{ for every }\xi\in U_{\tau(x)}\}.
\tag{CAX1}
\]

**Proposition.** The set \(V\) is an open fibrewise convex cone, \(\pi(V)=B_0\), and \(V^\circ=U^\circ\). For every conic \(H\in D^+(k_{E^*})\), the actual restriction morphism

\[
\rho_U:R\Gamma(V;H)\longrightarrow R\Gamma(U;H)
\tag{CAX2}
\]

is an isomorphism. The set \(A\) is closed in \(E_0\), so it is locally closed in \(E\).

**Proof.** Scalar multiplication by a fixed positive number is a homeomorphism; hence the displayed union defining \(V\) is open. The bundle projection is open, so \(B_0\) is open. Scaling preserves the base point, giving \(\pi(V)=B_0\).

For convexity, take \(su,tv\in V_b\), where \(u,v\in U_b\) and \(s,t>0\). For \(0<\lambda<1\), put \(c=\lambda s+(1-\lambda)t>0\). Then

\[
\lambda su+(1-\lambda)tv
=c\left(\frac{\lambda s}{c}u+
\frac{(1-\lambda)t}{c}v\right)\in cU_b\subset V_b.
\]

The endpoint cases are immediate. The equality of the polars follows because a linear pairing is nonnegative on \(U_b\) exactly when it is nonnegative on every positive multiple of every point of \(U_b\). The base-image clause in the polar is identical for the two sets.

For \(\xi\in V\), the set of positive numbers \(s\) with \(s\xi\in U\) is nonempty. It is open by continuity and convex as a subset of the positive real line by fibrewise convexity of \(U\). Thus it is an interval. If \(\xi=0\), it is the entire positive group. Inversion \(s\mapsto s^{-1}\) and then logarithm preserve the interval property. Apply SH02-CON-RESTRICTION on the invariant open space \(V\), with the open subset \(U\) and the conic restriction \(H|_V\). Its specified map is precisely \(\rho_U\).

To prove relative closedness of \(A\), work in a bundle chart over \(B_0\). The condition that some \(\xi\in U_b\) have \(\langle x,\xi\rangle<0\) defines the projection onto the \(x\)-space of an open subset of the fibre product. In these coordinates that projection is an ordinary projection with a Euclidean factor, hence is open. It is exactly \(E_0\setminus A\). This proves the assertion. \(\square\)

## SH02-CAX-REGIONS — The complete convex-open section formula

**Theorem.** For \(F\in D^+_{\mathbb R_{>0}}(k_E)\) and \(U\) as above, there are natural isomorphisms

\[
R\Gamma(U;T_EF)
\simeq R\Gamma_A(E_0;F|_{E_0})
\simeq R\Gamma_A(E;F).
\tag{CAX3}
\]

They use the polar convention in CAX1, including the omission of fibres outside \(B_0\).

**Proof.** The transformed object is conic and lies in \(D^+\) by SH02-FS-SETUP. Apply CAX2 to it. FS13 applies to the cone \(V\), and \(V^\circ=A\). If \(\theta_V:R\Gamma(V;T_EF)\xrightarrow{\sim}R\Gamma_A(E;F)\) is the comparison defined by FS13, the comparison from the first to the last term of CAX3 is specifically

\[
\theta_V\circ\rho_U^{-1}.
\tag{CAX4}
\]

This specifies its normalization: both FS13 and restriction use their previously fixed maps, and the inverse of an isomorphism is unique. Naturality in \(F\) follows from their naturality.

It remains to identify the ambient spaces in supported sections. Let \(j:E_0\hookrightarrow E\). Since \(A\) is closed in \(E_0\), its locally closed extension in \(E\) is canonically \(j_!k_A^{E_0}\). The open-embedding adjunction, with exact \(j_!\) and \(j^{-1}\), gives

\[
\begin{aligned}
R\Gamma_A(E;F)
&=R\operatorname{Hom}_{k_E}(j_!k_A^{E_0},F)\\
&\simeq R\operatorname{Hom}_{k_{E_0}}(k_A^{E_0},j^{-1}F)
=R\Gamma_A(E_0;F|_{E_0}).
\end{aligned}
\]

Its inverse is the second arrow of CAX3. Thus no global closedness assertion about \(A\) is needed. If \(U=\varnothing\), all three terms are zero. The proof also includes fibres where \(U_b\) is empty and rank zero. \(\square\)

**Example.** On the trivial line bundle over \(\mathbb R\), take \(U=\{(b,\xi):0<b<1,\ 1<\xi<3\}\). Its saturation is \(\{0<b<1,\ \xi>0\}\), and its polar is \(\{0<b<1,\ x\ge0\}\). This polar is closed over \((0,1)\) and is not closed in the whole bundle. CAX3 compares exactly these locally closed supported sections with sections on the original bounded interval in each dual fibre. Over one base point, with \(F=k_{\{0\}}\), both sides are \(k\) in degree zero: the Fourier transform is the constant sheaf on the dual line.

## SH02-CAX-PRODUCT-BASECHANGE — Ordinary image under a submersion

**Lemma.** Let \(f:Y\to X\) be any continuous map of locally compact spaces and \(K\in D^+(k_Y)\). If \(g:T\to X\) is locally a projection with a finite-dimensional Euclidean factor, form the Cartesian square with \(Y'=Y\times_XT\), projections \(g':Y'\to Y\) and \(f':Y'\to T\). The canonical morphism

\[
\beta_g:g^{-1}Rf_*K\longrightarrow Rf'_*g'^{-1}K
\tag{CAX5}
\]

is an isomorphism. Neither properness nor a cohomological-dimension bound for \(f_!\) is required.

**Proof.** Fix the map first. Under \(f'^{-1}\dashv Rf'_*\), its transpose is

\[
f'^{-1}g^{-1}Rf_*K
\simeq g'^{-1}f^{-1}Rf_*K
\longrightarrow g'^{-1}K,
\]

where the last arrow is the pulled-back counit. This is SH02-IMP-BASECHANGE-MORPHISM.

First suppose \(T=X\times\mathbb R\), with \(g=p_X\). At \((x,t)\), rectangles \(W\times I\), where \(W\) is an open neighbourhood of \(x\) and \(I\) an open interval containing \(t\), form a neighbourhood basis. The degree-\(a\) right-hand stalk in CAX5 is

\[
\mathop{\mathrm{colim}}_{W,I}
H^a(f^{-1}W\times I;p_Y^{-1}K).
\]

The unit for the interval projection, proved in SH02-CON-CYLINDER, identifies the canonical pullback

\[
H^a(f^{-1}W;K)\longrightarrow
H^a(f^{-1}W\times I;p_Y^{-1}K)
\]

as an isomorphism. The coefficient complex is pulled back, so its fibre cohomology is constant without any conicity assumption on \(K\). These identifications respect restrictions in both \(W\) and \(I\). Their colimit is \(H^a(Rf_*K)_x\), the left-hand stalk of CAX5. The counit definition shows that the stalk map of \(\beta_g\) is this same pullback map. Hence \(\beta_g\) is an isomorphism by stalk detection. This is the rectangle argument in SH02-CON-FUNCTORS; its ordinary-image part does not use that section's additional equivariance and exceptional-definedness assumptions.

Iteration proves the result for \(X\times\mathbb R^d\to X\) for each finite \(d\), including \(d=0\). The pasted maps are the canonical map for the composite: transposing them cancels the adjacent unit and counit by the adjunction identities and leaves the pulled-back counit displayed above.

For general \(g\), restrict to a chart \(T_a\simeq X_a\times\mathbb R^d\), where \(X_a\) is open in \(X\). Ordinary direct image commutes with open restriction: a resolution calculation on open subsets computes both sides by the same sections on their inverse images. Thus the restriction of the globally defined \(\beta_g\) is the product comparison just proved. Each chart restriction is invertible, so the global map is invertible. The charts test one already defined map and require no additional gluing choice.

All comparisons are in \(D^+\). The cylinder argument uses its closed-exhaustion theorem only in the interval coordinate, including noncompact horizontal strips; no countability or dimension assumption on the horizontal spaces is introduced. \(\square\)

## SH02-CAX-SUPPORT — Pulling back a closed support

**Corollary.** Under the hypothesis on \(g\) in CAX5, for closed \(C\subset X\) and \(A\in D^+(k_X)\), the canonical comparison

\[
g^{-1}R\Gamma_C A\longrightarrow
R\Gamma_{g^{-1}C}(g^{-1}A)
\tag{CAX6}
\]

is an isomorphism.

**Proof.** Let \(l:X\setminus C\hookrightarrow X\). Pull back the localization triangle

\[
R\Gamma_C A\longrightarrow A\longrightarrow Rl_*l^{-1}A\longrightarrow.
\]

Compare it with localization for \(g^{-1}C\). The middle map is the identity. The third map is CAX5 for \(f=l\), followed by the identification of the two restrictions; it is therefore an isomorphism. The induced comparison between the fibres is an isomorphism as well. The localization construction identifies this map with the internal-Hom pullback comparison for first argument \(k_C\): the maps into the middle object come from evaluation on \(k_X\to k_C\), and the maps to the complementary open term are the ordinary adjunction units. This specifies CAX6, rather than an arbitrary isomorphism of its endpoints. \(\square\)

We will also use the following open-image identity. If \(u:Y_0\hookrightarrow Y\) is open, \(C\subset Y\) is closed and \(L\in D^+(k_{Y_0})\), then

\[
R\Gamma_C Ru_*L\simeq Ru_*R\Gamma_{u^{-1}C}L.
\tag{CAX7}
\]

Indeed, on each open \(W\subset Y\), ordinary derived adjunction identifies Hom from \(k_{C\cap W}\) into \(R(u|_{Y_0\cap W})_*L\) with Hom from its restriction into \(L\). The latter restriction is \(k_{C\cap Y_0\cap W}\). The identifications commute with restriction in \(W\), yielding CAX7 with its adjunction map. CAX6 is only the stated closed-support specialization; no assertion about preservation of arbitrary internal Hom by inverse image is used.

## SH02-CAX-RADIAL — The ordinary sphere correspondence

Let \(E_0=E\setminus0\), \(E^*_0=E^*\setminus0\), and let \(S=S(E)\), \(S^*=S(E^*)\) be the quotients by positive scaling. Denote the open inclusions by \(j:E_0\hookrightarrow E\) and \(j^\vee:E^*_0\hookrightarrow E^*\), and the quotient projections by \(\gamma:E_0\to S\) and \(\gamma^\vee:E^*_0\to S^*\). A superscript \(\vee\) here labels a map on the dual bundle. Put

\[
V=S\times_BS^*,\quad
D=\{(u,\eta)\in V:\langle u,\eta\rangle\ge0\},
\]

with projections \(p_s:V\to S\) and \(q_s:V\to S^*\). The pairing inequality is independent of the choice of positive representatives, and defines a closed set by local radial trivializations.

**Theorem.** For every \(F\in D^+(k_S)\), the canonical comparisons give

\[
R\gamma^\vee_*\,(j^\vee)^{-1}T_E(Rj_*\gamma^{-1}F)
\simeq Rq_{s*}R\Gamma_D(p_s^{-1}F).
\tag{CAX8}
\]

The object \(Rj_*\gamma^{-1}F\) is the conic extension by ordinary direct image. This theorem supplies the ordinary comparison in [SH02-CTA-RADIAL](../conic-and-trace-applications.html), retaining that particular extension operation.

**Proof.** The input extension is conic by transport through ordinary direct image in SH02-CON-FUNCTORS, applied to the equivariant open inclusion. The maps \(j_!\) are exact, so the exceptional-definedness condition of that theorem is satisfied; no condition on \(B\) is added.

Set

\[
W=E_0\times_BE^*_0,\qquad
r=(\gamma,\gamma^\vee):W\to V,\qquad
M=p_s^{-1}F,\qquad H=R\Gamma_D M.
\]

Let \(q_W:W\to E^*_0\) be projection. On \(E\times_BE^*\), let \(p,q\) be the two projections and \(C=\{\langle x,\xi\rangle\ge0\}\). The map \(p\) is a rank-\(n\) vector-bundle projection. CAX5, applied to \(f=j\) and \(g=p\), gives the specified isomorphism

\[
p^{-1}Rj_*\gamma^{-1}F
\xrightarrow{\sim}R\widetilde j_*p_0^{-1}\gamma^{-1}F,
\]

where \(\widetilde j:E_0\times_BE^*\hookrightarrow E\times_BE^*\), and \(p_0\) projects to \(E_0\). Apply the ordinary-image presentation of the Fourier transform, then CAX7, ordinary composition, and open restriction to \(E^*_0\). This gives

\[
(j^\vee)^{-1}T_E(Rj_*\gamma^{-1}F)
\simeq Rq_{W*}R\Gamma_{r^{-1}D}(r^{-1}M)
\simeq Rq_{W*}r^{-1}H.
\tag{CAX9}
\]

The last map is the inverse of CAX6. It applies because \(r\) is locally projection with fibre \((0,\infty)^2\), which logarithm identifies with \(\mathbb R^2\).

The unit \(H\to Rr_*r^{-1}H\) is an isomorphism. To check this, choose local trivializations of the two radial bundles and apply the iterated cylinder unit. Ordinary open restriction identifies each such calculation with the restriction of the global unit, so they agree. Only local norms are needed; a global metric on the vector bundle is unnecessary.

Finally \(\gamma^\vee q_W=q_s r\). Applying ordinary composition to CAX9 and then the inverse of the radial unit yields

\[
\begin{aligned}
R\gamma^\vee_*(j^\vee)^{-1}T_E(Rj_*\gamma^{-1}F)
&\simeq Rq_{s*}Rr_*r^{-1}H\\
&\simeq Rq_{s*}H,
\end{aligned}
\]

which is CAX8. Every arrow is a specified Fourier comparison, ordinary base-change map, support adjunction, composition map, or inverse unit. The construction is therefore natural in \(F\). Ordinary radial integration introduces no orientation factor or shift. The separate proper-support radial formula retains its orientation trace and radial shift as proved in SH02-CTA-RADIAL.

All objects and maps retain the full \(D^+\) range. For \(n=0\), both direction spaces are empty, so both sides are zero. \(\square\)

## SH02-CAX-ANTECEDENTS — Scope of the supplement

The cone-complement homeomorphism is constructed by stereographic projection and a distance integral, including cones of lower dimension. The convex-open formula follows by positive saturation and the already fixed conic restriction map. The ordinary radial formula follows by a submersion base-change proof and localization. These arguments make the geometric step, wider test sets and exact comparison maps explicit. The distinct Fourier adjunction-normalization and transformed-trace equalities remain with the Fourier normalization supplements.

The mathematical antecedents are cited above.
