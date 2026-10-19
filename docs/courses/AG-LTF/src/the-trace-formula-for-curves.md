# The trace formula for curves

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The proper-curve fixed-point formula counts points using constant coefficients. A constructible sheaf assigns a module and a Frobenius operator to each point. The trace formula replaces the number \(1\) at that point by the trace of this operator, and equates their sum with a trace on cohomology with compact support.

We prove this in dimension at most one, allowing left Noetherian torsion coefficient rings, including noncommutative ones, and perfect stalk complexes. Compatible adic systems then give the integral and rational formulas. The main geometric step is to trivialize a locally constant sheaf on a finite étale cover. Twisting Frobenius by deck transformations then turns its cohomological contribution into a constant-coefficient fixed-point calculation. The group order need not be invertible in the coefficient ring.

## 1. The statement and the two additive quantities

Let \(k_0=\mathbf F_q\), of characteristic \(p\), and let \(k=\overline{\mathbf F}_q\). Let \(X_0\) be separated and of finite type over \(k_0\), of dimension at most one. Put \(X=X_0\times_{k_0}k\). Let \(\Lambda\) be a left Noetherian ring killed by a positive integer \(n\) prime to \(p\), and use **left** \(\Lambda\)-modules. This includes every finite ring of cardinality prime to \(p\). Let \(K_0\in D_{\mathrm{ctf}}(X_0,\Lambda)\): its cohomology sheaves are bounded and constructible and it has finite Tor amplitude. Write \(K\) for its geometric pullback.

The perfect-complex lesson, Theorems 4.3–4.4, prove that \(R\Gamma_c(X,K)\) and the stalks used below are perfect. Their traces therefore belong to the additive quotient

\[
\Lambda^\natural=\Lambda/\langle ab-ba:a,b\in\Lambda\rangle_{\mathrm{add}}.
\]

This quotient is an abelian group, not generally a ring. We never multiply arbitrary elements of it.

Let \(F_X\) be the geometric scheme Frobenius and use its descended coefficient correspondence from Lesson 3. At a rational point \(x\in X_0(k_0)\), its stalk map is the local geometric Frobenius \(F_x\). Define

\[
\begin{aligned}
T_{\mathrm{coh}}(X_0,K_0)
&=\operatorname{Tr}_\Lambda(F_X^*;R\Gamma_c(X,K)),\\
T_{\mathrm{loc}}(X_0,K_0)
&=\sum_{x\in X_0(k_0)}
\operatorname{Tr}_\Lambda(F_x;K_{\bar x}).
\end{aligned}
\tag{1.1}
\]

Traces on complexes already include alternating degree signs. If the coefficients are a field, the first expression is the alternating trace on compactly supported cohomology.

**Theorem 1.1 (curve trace formula).**

\[
T_{\mathrm{coh}}(X_0,K_0)=T_{\mathrm{loc}}(X_0,K_0)
\quad\text{in }\Lambda^\natural.
\tag{1.2}
\]

The theorem includes singular, reducible and nonreduced \(X_0\). We will use the sheaf and compact-support foundations from Lessons 1–4, and the proper-curve fixed-point formula proved in §4 below. Its finite-ring specialization is [Stacks, Tag 03UG](https://stacks.math.columbia.edu/tag/03UG). The larger coefficient scope follows from the Noetherian perfectness and flat-model arguments written in Lesson 4 and the finite-monodromy argument in §3 below.

**Lemma 1.2 (open–closed additivity).** If \(j_0:U_0\hookrightarrow X_0\) is open with closed complement \(i_0:Z_0\hookrightarrow X_0\), both quantities in (1.1) are the sum of their values on \(U_0,j_0^*K_0\) and \(Z_0,i_0^*K_0\).

**Proof.** The rational points partition into the two subsets, and coefficient restriction preserves their stalk maps, proving local additivity. For the cohomological assertion use the actual two-step filtration defined by the termwise exact sequence

\[
0\longrightarrow j_{0!}j_0^*K_0
\longrightarrow K_0
\longrightarrow i_{0*}i_0^*K_0\longrightarrow0.
\tag{1.3}
\]

One may form it on a representative complex; the open and closed functors here are exact, as is checked on geometric stalks. Its graded objects have the stated restrictions, extended by zero. The Frobenius correspondence preserves this filtration by naturality.

Applying the filtered derived functor \(R\Gamma_c\) gives graded objects \(R\Gamma_c(U,j^*K)\) and \(R\Gamma_c(Z,i^*K)\); each is perfect by Lesson 4. Theorem 3.1 there, proved using finite filtered projective models, says that their traces add to the trace of the underlying complex. This proves the assertion. The use of the filtration matters over general rings: additivity for an arbitrary three-component endomorphism of a distinguished triangle would not suffice. \(\square\)

**Lemma 1.3 (dimension zero).** Formula (1.2) holds when \(\dim X_0=0\).

**Proof.** A finite-type zero-dimensional scheme over a field is finite. After geometric base change its étale topos is a finite disjoint union of point topoi, including if the scheme has nilpotents: étale topoi are invariant under reduction. Thus

\[
R\Gamma_c(X,K)=\bigoplus_{z\in X(k)}K_z.
\tag{1.4}
\]

Frobenius permutes these summands and gives the coefficient maps between them. In projective representatives the trace of the resulting block matrix is the sum of the diagonal block traces. An orbit of length greater than one contributes none. The fixed geometric points are precisely the points over \(X_0(k_0)\), and their diagonal blocks are \(F_x\). The same argument in each complex degree, with its sign, proves (1.2). \(\square\)

## 2. Reduction to a locally constant sheaf on an open curve

We spell out the reduction for the full coefficient and complex scope. First decompose the torsion coefficient ring into its prime-primary factors. If the characteristic of \(\Lambda\) is \(\prod_\ell\ell^{e_\ell}\), the Chinese remainder idempotents in its central copy of the integers give

\[
\Lambda\simeq\prod_\ell\Lambda_\ell.
\tag{2.1}
\]

Modules, perfect complexes and the additive commutator quotient decompose accordingly. It is enough to prove (1.2) when \(\ell^e\Lambda=0\) for a single \(\ell\ne p\).

By the flat constructible model argument in Lesson 4, a \(D_{\mathrm{ctf}}\) object admits a bounded representative with constructible flat terms. Their finitely presented flat stalks are projective; the finite-presentation splitting argument is proved in Lesson 4, Lemma 4.2. Apply the finite filtration by complex degree. Its graded objects are the terms shifted to their degrees, so filtered additivity yields

\[
T(X_0,K_0)=\sum_i(-1)^iT(X_0,K_0^i)
\tag{2.2}
\]

for either \(T\). The Frobenius coefficient isomorphism is natural for all sheaves on \(X_0\), so these termwise maps commute with the differential and preserve this filtration. No projectivity of the individual cohomology sheaves of \(K_0\) is assumed.

For each term, constructibility permits a dense open subset on which it is locally constant. Work on \(X_{0,\mathrm{red}}\), using étale topological invariance; the rational points, coefficient maps and both quantities agree with those on \(X_0\). Remove the finitely many zero-dimensional components and the intersections between one-dimensional components. The remaining one-dimensional pieces are disjoint integral curves. Because \(k_0\) is perfect, their smooth loci are dense; their singular complements are finite. On each smooth piece choose an affine dense open. Its complement in the original curve is again finite. Removing the finitely many points outside the locally constant stratum leaves a smooth irreducible affine \(U_0\) and a locally constant sheaf \(\mathcal F_0\) with finitely generated projective stalks.

All discarded loci have dimension zero, so Lemmas 1.2–1.3 account for their contributions. Finally remove the finite set \(U_0(k_0)\). Additivity accounts for it as well. It is therefore enough to prove

\[
T_{\mathrm{coh}}(U_0,\mathcal F_0)=0
\quad\text{when }U_0(k_0)=\varnothing.
\tag{2.3}
\]

There is no geometric-connectedness assumption on \(U_0\); connectedness over \(k_0\) is enough to choose the cover below.

## 3. Descent on a Galois cover, including the stalk maps

Choose a connected finite étale Galois cover

\[
f_0:V_0\longrightarrow U_0
\tag{3.1}
\]

trivializing \(\mathcal F_0\). Its group \(G\) is finite and all deck transformations are defined over \(k_0\). Here normality of the smooth curve ensures that a discrete locally constant sheaf is described by the profinite étale fundamental group. The following generic-point argument also verifies the finite-image assertion for our modules.

At the generic point, the discrete stalk \(M\) has continuous absolute-Galois action. The intersection of the stabilizers of a finite generating set is open and fixes all of \(M\) by \(\Lambda\)-linearity. It is consequently the normal action kernel, of finite index. Let \(L/k_0(U_0)\) be its finite Galois extension and normalize \(U_0\) in \(L\). This normalization is finite, since the curve is of finite type over a field. At a point of \(U_0\), the sheaf becomes constant on the strict localization: a trivializing pointed étale neighbourhood admits a section there. Thus the Galois group of the strict-local fraction field acts trivially on \(M\), and the extension \(L\) splits over that field. The finite normalization is therefore étale at that point; equivalently, its branches over the strict henselian discrete valuation ring are copies of that ring. This holds at every point. On the resulting connected finite étale cover the generic constant trivialization extends to the whole locally constant sheaf. One checks this on a trivializing étale neighbourhood: its components are normal, and a map of constant sheaves on each component is determined by its generic value. The extensions therefore agree on overlaps and descend.

This gives (3.1), even when the underlying set of \(M\) is infinite. The scheme inputs are finite normalization of a curve and the strict-local criterion for an étale finite map, alongside the finite étale Galois correspondence used in Lesson 1. Normality is used here; infinite local systems on singular curves need not have profinite monodromy.

Identify

\[
f_0^*\mathcal F_0=\underline M,\qquad
M=\Gamma(V_0,f_0^*\mathcal F_0).
\]

The underlying \(\Lambda\)-module \(M\) is finite projective. Our left \(G\)-action on sections is \(g\cdot m=(g^{-1})^*m\). The same inverse-pullback action is used on \(f_{0*}\underline A\), for any constant coefficient ring \(A\). Because the trivialized sheaf is constant on \(V_0\), the canonical Frobenius correspondence acts as the identity on its value \(M\). Naturality of evaluation supplies the corresponding compatibility downstairs.

Fix \(A=\mathbf Z/\ell^N\mathbf Z\), with \(N\geq e\), so its central action on \(\Lambda\) is defined. Put

\[
\mathcal B_0=f_{0*}\underline A,\qquad
\mathcal Q_0=f_{0*}f_0^*\mathcal F_0.
\]

We claim the following three identifications, retaining the diagonal \(G\)-action:

\[
\mathcal Q_0\simeq\mathcal B_0\otimes_A\underline M,
\qquad
(\mathcal Q_0)_G\simeq\mathcal F_0,
\qquad
\Lambda\otimes_{\Lambda[G]}^{\mathbf L}\mathcal Q_0
\simeq\mathcal F_0.
\tag{3.2}
\]

Here coinvariants for left modules mean tensoring **on the left** with the right \(\Lambda[G]\)-module \(\Lambda\), whose action is through augmentation.

**Lemma 3.1.** All maps in (3.2) are isomorphisms, including their Frobenius structures.

**Proof.** The first map sends an elementary tensor \(b\otimes m\) to the section of \(f_0^*\mathcal F_0\) given at \(v\) by \(b(v)m(v)\). At a geometric point \(\bar u\), let \(T=f_0^{-1}(\bar u)\). Evaluation \(e_v:M\to\mathcal F_{\bar u}\) is an isomorphism for each \(v\in T\). The map on stalks is

\[
A^T\otimes_AM\longrightarrow\bigoplus_{v\in T}\mathcal F_{\bar u},
\qquad
(b_v)_v\otimes m\longmapsto(b_ve_v(m))_v.
\tag{3.3}
\]

It is an isomorphism: using the point-indicator basis of \(A^T\), it is the direct sum of the evaluation isomorphisms. The left action is \((g b)_v=b_{g^{-1}v}\), while \(e_v(gm)=e_{g^{-1}v}(m)\). Thus the diagonal action becomes the permutation action on the right-hand summands, with their values in the same stalk \(\mathcal F_{\bar u}\). This proves equivariance, not just equality of ranks.

The trace map \(\mathcal Q_0\to\mathcal F_0\) is the sum of those stalk values. A simply transitive \(G\)-set \(T\) has permutation coinvariants consisting of one copy of its value module: its relations identify the indicator copy at \(v\) with the copy at \(gv\). The summation map gives that identification with coefficient \(1\). There is no averaging factor \(|G|^{-1}\). This proves the second isomorphism.

To check the derived assertion, the stalk of \(\mathcal B_0\) is a rank-one free \(A[G]\)-module. Its diagonal tensor with \(M\) is a projective \(\Lambda[G]\)-module. Explicitly, on a group basis the change

\[
h\otimes m\longmapsto h\otimes h^{-1}m
\tag{3.4}
\]

takes the diagonal action to action on the first factor alone. In that form it is \(\Lambda[G]\otimes_\Lambda M\), with the factors reordered using central \(A\)-linearity. A direct-summand presentation of projective \(M\) proves projectivity. Flatness of sheaves of modules can be checked on geometric stalks; hence \(\mathcal Q_0\) is flat over \(\Lambda[G]\). Its higher derived coinvariants vanish, proving the third isomorphism.

Finally each map is constructed from pullback, evaluation, finite-cover trace or tensor. Naturality of the Frobenius correspondence makes their squares commute. On the cover it is the ordinary pullback on \(\mathcal B_0\) and the identity on the constant value \(M\); (3.3) verifies that this is precisely the descended map on \(\mathcal Q_0\). Thus the identifications preserve the required operator. \(\square\)

Let \(P=R\Gamma_c(U,\mathcal B)\). The sheaf \(\mathcal B\) has finite free \(A[G]\)-stalks, so Lesson 4 proves

\[
P\in D_{\mathrm{perf}}(A[G]).
\tag{3.5}
\]

Moreover \(R\Gamma_c(U,\mathcal B)=R\Gamma_c(V,A)\) as an \(A\)-complex with deck actions. Indeed a finite étale map has exact direct image, with stalk the finite direct sum over its geometric fibre, so its higher direct images vanish. Proper-support composition for this finite map then gives the equality. Frobenius and deck actions agree under it.

Apply the coefficient projection formula proved in Lesson 4 twice: first over \(A\) with the constant module \(M\), then over \(\Lambda[G]\) with its right augmentation module \(\Lambda\). Together with Lemma 3.1 these yield

\[
R\Gamma_c(U,\mathcal F)
\simeq
\Lambda\otimes_{\Lambda[G]}^{\mathbf L}
\bigl(P\otimes_A^{\mathbf L}M\bigr).
\tag{3.6}
\]

This also explains exactly where the group-ring projectivity is needed. In a bounded projective \(A[G]\)-model for \(P\), the ordinary tensor \(P\otimes_AM\) computes its derived tensor because the terms are \(A\)-projective. By (3.4) each resulting term is projective over \(\Lambda[G]\), so taking ordinary coinvariants computes the final derived tensor. Frobenius on (3.6) is induced by its operator on \(P\), with identity on \(M\), and commutes with \(G\).

## 4. Twisted Frobenius and the boundary

We first prove the proper constant-coefficient formula using curve duality. Subtracting the boundary then supplies the statement needed for (3.6).

**Theorem 4.1 (the proper-curve formula).** Let \(k\) be algebraically closed of characteristic exponent \(p\), let \(Y/k\) be a smooth proper scheme purely of dimension one, and let \(h:Y\to Y\) be a \(k\)-morphism with isolated fixed points. A smooth proper curve is projective; \(Y\) may have finitely many connected components. Write

\[
N(h)=\sum_{x\in\operatorname{Fix}(h)}
 \operatorname{length}_{\mathcal O_{Y,x}}\mathcal O_{\operatorname{Fix}(h),x}.
\tag{4.1}
\]

The fixed scheme is proper and zero-dimensional, hence finite. For every integer \(n\geq2\) invertible in \(k\), put \(R=\mathbf Z/n\). Then \(R\Gamma(Y,R)\) is perfect and

\[
\operatorname{Tr}_{R}\bigl(h^*;R\Gamma(Y,R)\bigr)
=\sum_{i=0}^{2}(-1)^i
 \operatorname{Tr}_{R}\bigl(h^*;H^i(Y,R)\bigr)
=N(h)\cdot1_R.
\tag{4.2}
\]

For every prime \(\ell\ne p\), its integral and rational forms are

\[
\operatorname{Tr}_{\mathbf Z_\ell}
 \bigl(h^*;R\Gamma(Y,\mathbf Z_\ell)\bigr)=N(h),
\qquad
\sum_{i=0}^{2}(-1)^i
 \operatorname{Tr}_{\mathbf Q_\ell}
 \bigl(h^*;H^i(Y,\mathbf Q_\ell)\bigr)=N(h).
\tag{4.3}
\]

Here \(h^*\) is ordinary pullback with constant coefficients. Twists used to construct divisor classes are contracted in the trace; they do not add a descended Frobenius coefficient action.

These are the precise geometric inputs:

* [The multiplicative group on a curve, Theorem 6.2](course:ag-etale-cohomology/the-multiplicative-group-on-a-curve): \(H^i(C,R)\) on a connected genus-\(g\) proper smooth curve is free of ranks \(1,2g,1\) in degrees \(0,1,2\), and zero otherwise. The canonical identification \(H^2(C,\mu_n)=R\) sends \(c_1^{(n)}(L)\) to \(\deg L\bmod n\).
* Étale Lesson 17, §2, Lemma 4.2, Corollary 10.2 and Theorem 11.1: the curve trace, its sum over components, perfect cup pairings, and the normalized point purity \(Ri_x^!\mu_n=R[-2]\). With this degree normalization the point generator has image \(c_1^{(n)}(\mathcal O_C(x))\) and trace \(+1\).
* [Smooth base change and local acyclicity, Theorem 1.1 and §7](course:ag-etale-cohomology/smooth-base-change-and-local-acyclicity): smooth base change, including the derived comparison for the open immersion \(\mathbf G_m\hookrightarrow\mathbf A^1\).
* Étale Lessons 7 and 13: exact closed-immersion pushforward and proper base change, natural in the coefficient complex and in its morphisms.
* [Cohomological dimension and the Künneth formula, Theorem 9.1 and Lemma 8.4](course:ag-etale-cohomology/cohomological-dimension-and-the-kunneth-formula): the canonical product comparison and the constant-tensor comparison. Cup products are the actual external products, with the Koszul sign.
* The trace algebra in Lesson 4, §§1–2, and the compatible-complex argument in Lesson 1, §6. The Frobenius specialization uses only Lesson 3, Theorem 5.1.

Kummer exactness, localization, sheaf adjunction and tensor functoriality are the earlier sheaf formalism. The supported-divisor calculation below constructs exactly the product orientation needed here.

### The normalized divisor map in a product of curves

Put \(S=Y\times_kY\), let \(p=p_1:S\to Y\), and let \(s=\delta:Y\hookrightarrow S\) be the diagonal. It is a section of the smooth relative curve \(p\) and is an effective Cartier divisor.

We first construct its normalized Gysin map using point purity. Étale locally near any point of \(s(Y)\), there is a function \(t\) cutting out this section such that

\[
(p,t):V\longrightarrow B\times_k\mathbf A^1
\tag{4.4}
\]

is étale, for an open \(B\subset Y\). To obtain it, take an étale local coordinate \(z\) on the second curve near the section point, and set \(t=z-z\circ s\). Its differential along the fibre is a nonzero cotangent generator. The étale inverse-function criterion gives (4.4); discard the other local branches of \(t=0\) so that its zero scheme is precisely the section on this neighbourhood. Consequently \(t:V\to\mathbf A^1\) is smooth and its inverse image of \(0\) is this divisor.

Let \(i_0:\{0\}\hookrightarrow\mathbf A^1\) and \(j_0:\mathbf G_m\hookrightarrow\mathbf A^1\). The localization triangle is

\[
(i_0)_*Ri_0^!R\longrightarrow R
 \longrightarrow R(j_0)_*R\longrightarrow.
\tag{4.5}
\]

Apply the exact inverse-image functor along \(t\). Smooth base change identifies the third term with the direct image from \(V-\{t=0\}\); finite base change identifies the first term's support with \(\{t=0\}\). Comparing the localization triangles therefore transports the point purity isomorphism to

\[
Rs^!R(1)[2]\simeq R
\quad\text{on this section neighbourhood}.
\tag{4.6}
\]

The generator is normalized by the Kummer supported divisor class. More explicitly, a line bundle with a trivialization off a divisor defines a class in \(H^1_D(S,\mathbf G_m)\). Apply the Kummer connecting map with support to the pair \((\mathcal O_S(D),1)\), obtaining \(c_D\in H^2_D(S,\mu_n)\); forgetting support gives \(c_1^{(n)}(\mathcal O_S(D))\). For \(D=(t)\), this construction is the pullback of the identical construction for \(0\subset\mathbf A^1\). The point-purity calculation in the curve-duality lesson shows that this is a generator: its local valuation is a unit modulo \(n\). We choose its sign by the supported Chern class, whose image on a proper curve is \(c_1^{(n)}(\mathcal O_C(x))\) and has degree trace \(+1\). A raw unit-localization boundary can use the opposite sign; it is this supported Chern class that fixes the convention here.

Changing the equation from \(t\) to \(ut\), with \(u\) a unit, does not change this generator: the difference of the Kummer classes on the complement extends over the whole neighbourhood, so its localization boundary is zero. This also follows at a strict local stalk from the existence of an \(n\)-th root of every unit. Thus the local orientations glue. Localization shows that the supported complex has only the degree-two cohomology sheaf, so its truncation identifies it with that sheaf; there is no additional choice of a complex-level extension to glue. We obtain (4.6) globally, with its stated normalization.

The counit for sections with closed support now gives a morphism of complexes of \(R_S\)-modules

\[
e:s_*R\longrightarrow R_S(1)[2].
\tag{4.7}
\]

Its value on \(1\), after forgetting support, is

\[
[\Delta]:=c_1^{(n)}(\mathcal O_S(\Delta))
 \in H^2(S,R(1)).
\tag{4.8}
\]

Indeed purity identifies \(H^2_\Delta(S,R(1))\) with \(H^0(Y,R)\); the supported Kummer class has value \(1\) at every local point by the calculation above. It is therefore the global section \(1\), and its counit image is (4.8).

For \(a\in H^r(Y,R)\), write \(s_*a\in H^{r+2}(S,R(1))\) for the map induced by (4.7). The closed-immersion tensor identity and functoriality of tensoring give the projection identity

\[
s_*a\cup v=s_*(a\cup s^*v).
\tag{4.9}
\]

This can be checked before taking global sections: tensor the morphism \(e\) with the morphism of the tensor unit representing \(v\), and use
\(s_*R\otimes^L v=s_*(R\otimes^Ls^*v)\).
The two composites are the two sides of (4.9). Thus (4.9) uses the counit just constructed, not an adjoint defined by an assumed surface duality.

### Product trace and the decisive normalization identity

Proper base change for the product projection gives the canonical isomorphism

\[
Rp_*R_S\simeq
 \underline{R\Gamma(Y,R)}_Y.
\tag{4.10}
\]

Use the curve trace of étale Lesson 17 on the constant complex on the right to define

\[
\tau_p:Rp_*R_S(1)[2]\longrightarrow R_Y.
\tag{4.11}
\]

The absolute product trace is obtained by taking global sections of (4.11) and then applying the first curve trace:

\[
\int_S:H^4(S,R(2))\longrightarrow R.
\tag{4.12}
\]

By the canonical Künneth map,
\(\int_S(a\boxtimes b)=(\int_Ya)(\int_Yb)\)
for \(a,b\in H^2(Y,R(1))\).
For disconnected \(Y\) this means the sum of the product traces on all \(Y_\alpha\times Y_\beta\).

We prove the exact identity needed for the diagonal:

\[
\tau_p\circ Rp_*e
=\operatorname{id}_{R_Y},
\qquad Rp_*s_*R=R_Y.
\tag{4.13}
\]

The left side is a morphism \(R_Y\to R_Y\) in the derived category. Such morphisms in degree zero are \(H^0(Y,R)\), so they are determined by their scalar on each connected component. Choose a closed \(k\)-point \(y\) on each component. Proper base change, natural in the morphism \(e\), identifies its value on \(1\) with the curve trace of

\[
[\Delta]|_{\{y\}\times Y}
=c_1^{(n)}
  \bigl(\mathcal O_S(\Delta)|_{\{y\}\times Y}\bigr).
\tag{4.14}
\]

The restriction line bundle is \(\mathcal O_Y(y)\), with the point placed in the component containing \(y\). The local coordinate \(t\) of (4.4) restricts to a uniformizer on that fibre, so this is a divisor of multiplicity exactly one. Its curve trace is \(1\). This proves (4.13) on every component.

Notice what was actually used in this fibre calculation: naturality of ordinary Kummer Chern classes under pullback and proper base change for \(Rp_*\). No assertion that \(Ri^!\) commutes with an arbitrary nonsmooth fibre pullback is needed.

Combining (4.9), (4.13), and the definition (4.12) gives, for every \(v\in H^2(S,R(1))\),

\[
\int_S[\Delta]\cup v=\int_Ys^*v.
\tag{4.15}
\]

For completeness, (4.9) identifies the left integrand with \(e(s^*v)\). After \(Rp_*\), (4.13) says that relative integration of that class is precisely \(s^*v\). Applying the first curve trace gives (4.15). This supplies the product-divisor Gysin/trace compatibility needed for the fixed-point calculation.

### The signed diagonal and the graph

Temporarily choose a primitive \(n\)-th root to trivialize the twists. Every occurrence of trace below is the curve trace with this same trivialization. Write \(V^i=H^i(Y,R)\). These are finite free modules; cup product gives perfect pairings between \(V^{2-i}\) and \(V^i\).

Choose a basis \(u_{i,j}\) of \(V^i\), and its **left dual** \(v_{i,j}\in V^{2-i}\), characterized by

\[
\int_Yv_{i,j}\cup u_{i,k}=\delta_{jk}.
\tag{4.16}
\]

The Künneth multiplication law is

\[
(a\boxtimes b)\cup(c\boxtimes d)
=(-1)^{\deg(b)\deg(c)}
 (a\cup c)\boxtimes(b\cup d).
\tag{4.17}
\]

The tensor products of the curve pairings are perfect, so the product trace pairs \(H^2(S,R)\) perfectly with itself. Identity (4.15) determines the diagonal class uniquely and gives

\[
[\Delta]=
\sum_{i=0}^{2}\sum_j(-1)^i
  v_{i,j}\boxtimes u_{i,j}.
\tag{4.18}
\]

Here is a direct sign verification. Test the right side against \(a\boxtimes b\), where \(\deg a=i\), \(\deg b=2-i\). The displayed sign and the crossing sign in (4.17) cancel. The result is
\(\sum_j(\int_Yv_{i,j}a)(\int_Yu_{i,j}b)=\int_Ya b\),
because \(a=\sum_j(\int_Yv_{i,j}a)u_{i,j}\).
This is exactly the functional on the right of (4.15). Test classes of other bidegrees pair to zero for degree reasons. Künneth and perfectness prove (4.18). In particular its degree-one contribution has a minus sign.

Let \(\gamma_h:Y\to S\), \(\gamma_h(y)=(y,h(y))\), be the graph parametrization. If
\(h^*u_{i,j}=\sum_k A^{(i)}_{kj}u_{i,k}\),
pullback of (4.18) and (4.16) give

\[
\int_Y\gamma_h^*[\Delta]
=\sum_i(-1)^i\sum_j
 \int_Yv_{i,j}\cup h^*u_{i,j}
=\sum_i(-1)^i\operatorname{Tr}_R(A^{(i)}).
\tag{4.19}
\]

This computation applies to the full cohomology of a disconnected curve. An endomorphism can move components or collapse a component to a point; no invertibility or nonconstancy assumption on \(h\) was used.

On the other hand, Chern classes commute with pullback, so

\[
\gamma_h^*[\Delta]
=c_1^{(n)}\bigl(\gamma_h^*\mathcal O_S(\Delta)\bigr).
\tag{4.20}
\]

Since the fixed points are isolated, no component of the graph is contained in the diagonal. Its pullback divisor is therefore an effective Cartier divisor on \(Y\), whose zero scheme is exactly \(\operatorname{Fix}(h)\). In a completed local ring \(k[[t]]\) at a fixed point \(x\), the diagonal equation pulls back to \(h^\#t-t\). Consequently

\[
\operatorname{length}\mathcal O_{\operatorname{Fix}(h),x}
=\dim_k k[[t]]/(h^\#t-t)
=\operatorname{ord}_t(h^\#t-t).
\tag{4.21}
\]

Completion preserves finite length. Formula (4.21) includes inseparable and constant maps, and includes nonreduced fixed points. For a component sent to a different component the pullback divisor is empty. The degree of the line bundle in (4.20) is thus \(N(h)\). The degree-normalized curve trace gives

\[
\int_Y\gamma_h^*[\Delta]=N(h)\bmod n.
\tag{4.22}
\]

Equations (4.19) and (4.22) prove the alternating-cohomology identity in (4.2), using only divisors on curves and the product compatibility proved above.

### Perfect complexes, complete coefficients, and finite coefficient rings

There is also a direct perfectness argument at finite level. A bounded complex with projective cohomology splits in the derived category as the sum of its cohomology modules in their respective degrees. Indeed, each truncation extension is a morphism from the next projective cohomology module into the lower truncation shifted by one. Derived Hom from that projective module is ordinary Hom on cohomology, and in the required degree the lower truncation has zero cohomology; the extension is zero. Apply this successively to \(R\Gamma(Y,R)\), whose cohomology is free and concentrated in degrees \(0,1,2\).

It is therefore represented by a bounded finite free complex. The trace theorem in Lesson 4, §2, identifies its perfect-complex trace with the alternating traces on these free cohomology modules. This proves all of (4.2); it does not assign matrix traces to arbitrary nonprojective torsion cohomology.

For \(R_a=\mathbf Z/\ell^a\), the canonical coefficient comparison

\[
R\Gamma(Y,R_{a+1})\otimes^L_{R_{a+1}}R_a
\simeq R\Gamma(Y,R_a)
\tag{4.23}
\]

is the constant-tensor comparison of étale Lesson 16, Lemma 8.4, applied to the coefficient module \(R_a\). It respects \(h^*\). The compatible-perfect-complex construction of Lesson 1, Theorem 6.1, gives a bounded finite free \(\mathbf Z_\ell\)-complex representing the inverse system and identifies its rational trace with the alternating trace on rational cohomology. Reduction of the integral trace modulo every \(\ell^a\) is \(N(h)\) by (4.2). Since \(\bigcap_a\ell^a\mathbf Z_\ell=0\), the integral trace is exactly \(N(h)\); rationalization proves (4.3).

The formula also has the finite-ring form used in coefficient arguments. Let \(A\) be a finite, possibly noncommutative ring killed by an integer \(n\) invertible in \(k\). The central map \(R=\mathbf Z/n\to A\) and the same constant-tensor comparison give

\[
R\Gamma(Y,A_Y)
\simeq A\otimes_R^L R\Gamma(Y,R).
\tag{4.24}
\]

Extending the bounded finite free \(R\)-model makes a bounded finite free left \(A\)-model, compatibly with pullback. Matrix trace under this extension is the image of the \(R\)-trace in the additive quotient
\(A^\natural=A/[A,A]\).
Hence

\[
\operatorname{Tr}_{A}
 \bigl(h^*;R\Gamma(Y,A_Y)\bigr)
=N(h)\,[1_A]\quad\text{in }A^\natural.
\tag{4.25}
\]

If a projective constant coefficient module \(M\) carries an endomorphism \(b\), the tensor endomorphism \(h^*\otimes b\) similarly has trace
\(N(h)\operatorname{Tr}_A(b;M)\),
by the tensor trace calculation in Lesson 4. This last statement concerns constant coefficients with their specified coefficient operator.

### Frobenius specialization and scope

Let \(Y_0/\mathbf F_q\) be smooth proper and \(Y=Y_0\otimes\overline{\mathbf F}_q\). Let \(F\) be the base change of the \(q\)-power Frobenius of \(Y_0\), with the geometric cohomological convention of Lesson 3. That lesson's Theorem 5.1 proves that \(\operatorname{Fix}(F^r)\) consists of precisely \(Y_0(\mathbf F_{q^r})\), each with length one. Applying (4.2), (4.3) or (4.25) therefore gives the proper constant-sheaf Frobenius trace formula, including geometrically disconnected curves.

The isolated-fixed-points hypothesis is essential to the finite-length interpretation. For disconnected \(Y\), requiring merely \(h\ne\operatorname{id}_Y\) is insufficient: one component may still be fixed identically. The present theorem makes no finite-point assertion for such a map.

Deligne's [SGA 4½](https://publications.ias.edu/sites/default/files/Number32.pdf), “Rapport sur la formule des traces,” Theorem 5.3, printed p. 100, states the same rational proper-curve formula and discusses its historical proof on p. 101. That statement is a comparison locator, not a premise in the argument above. The proof here establishes the product-diagonal compatibility (4.13)–(4.15) directly from the stated curve results. It does not establish general surface duality, general higher-dimensional trace, or a Riemann-hypothesis estimate.

The preceding construction proves Theorem 4.1. \(\square\)

**Proposition 4.2 (Nielsen–Wecken subtraction for curves).** Let \(Y/k\) be a smooth projective curve, possibly disconnected, let \(V\subset Y\) be open, and let \(D=Y-V\) be finite with its reduced structure. Suppose \(h:Y\to Y\) has isolated fixed points, \(h^{-1}(V)=V\), and its fixed points in \(D\) have multiplicity one. Then

\[
\sum_i(-1)^i\operatorname{Tr}(h^*;H^i_c(V,E))
=\sum_{x\in V,\ h(x)=x}m_x(h),
\tag{4.26}
\]

where \(m_x(h)\) is the local fixed-scheme length. For \(A=\mathbf Z/\ell^N\mathbf Z\) the same equality holds modulo \(\ell^N\), as a perfect-complex trace.

**Proof.** The open–closed sequence for \(V,D\) is preserved by \(h\), since its preimages preserve both loci. Filtered additivity gives

\[
\operatorname{Tr}(h^*;R\Gamma_c(V))
=\operatorname{Tr}(h^*;R\Gamma(Y))
-\operatorname{Tr}(h^*;R\Gamma(D)).
\tag{4.27}
\]

The first term on the right is the total fixed-point length by Theorem 4.1 above. On the finite reduced set \(D\), cohomology is its permutation module in degree zero. Its trace is the number of fixed points in \(D\), by the diagonal-block argument of Lemma 1.3. These equal their multiplicities by hypothesis, so subtraction leaves exactly the fixed-point length in \(V\). Use the finite perfect-complex form of Theorem 4.1, with the same filtered and permutation traces, for the finite-level assertion. \(\square\)

The isolated-fixed-point hypothesis is necessary even if \(D\) is empty: otherwise the identity on a proper curve would make the asserted point count infinite. This is the precise curve form of Deligne, [Rapport], Corollary 5.4.

Choose a smooth projective completion \(Y_0\) of \(V_0\). Existence of a smooth projective completion for a smooth curve over a perfect field is a curve-geometry prerequisite, [Stacks, Tag 0H1F](https://stacks.math.columbia.edu/tag/0H1F). Each deck transformation extends uniquely to an automorphism of \(Y_0\): it acts on the function field, and the valuative criterion on the discrete valuation rings of the smooth complete curve extends the resulting rational map everywhere, as well as its inverse. The \(q\)-power Frobenius of \(Y_0\) extends that of \(V_0\). The extensions still commute, since they commute on the dense open.

Put \(Y=Y_0\times_{k_0}k\). For \(g\in G\), define

\[
h_g=g^{-1}F_Y.
\tag{4.28}
\]

It satisfies \(h_g^{-1}(V)=V\). One way to see this exactly is to work before geometric base change: absolute \(q\)-Frobenius preserves every open subset under inverse image, and \(g\) preserves \(V_0\). Base change preserves the equality of these open inverse images.

The differential of \(F_Y\) is zero on tangent spaces, so \(dh_g=0\). At a fixed point with uniformizer \(t\), therefore, \(h_g^\#t\in(t^2)\). The fixed equation \(t-h_g^\#t\) has nonzero linear coefficient \(1\), hence its length is one. This proves simplicity on the boundary as well as in the interior. It also rules out identity on any component. Thus every fixed point is isolated, and Proposition 4.2 applies, including if \(Y\) is geometrically disconnected.

There are no such fixed points in \(V\) when \(U_0(k_0)=\varnothing\). Indeed \(f(g^{-1}F_V(v))=F_U(f(v))\). A fixed \(v\) would give \(F_U(f(v))=f(v)\), hence a rational point of \(U_0\) by Lesson 3. Consequently

\[
\operatorname{Tr}_A(h_g^*;R\Gamma_c(V,A))=0
\quad\text{for every }g\in G\text{ and every }N.
\tag{4.29}
\]

This supplies both the fixed-point argument and the boundary multiplicity check; zero fixed points on the open cover alone would not justify (4.29) without them.

## 5. Centralizer traces and completion of the proof

Let \(F\) denote the endomorphism of the perfect \(A[G]\)-complex \(P\) from §3. For \(g\in G\), let \(Z_g\) be its centralizer and set

\[
\tau_g=\operatorname{Tr}_A^{Z_g}(gF;P)\in A.
\tag{5.1}
\]

This means: restrict the complex to \(A[Z_g]\), take its group-ring projective trace, and select the coefficient of the identity conjugacy class. It is defined integrally, including when \(\ell\mid|Z_g|\). The full trace sorites proved in Lesson 4, Corollary 6.3, applied to (3.6) gives

\[
T_{\mathrm{coh}}(U_0,\mathcal F_0)
=\sum_{[g]\subset G}\tau_g\,
\operatorname{Tr}_\Lambda(g;M)
\quad\text{in }\Lambda^\natural.
\tag{5.2}
\]

The sum is over conjugacy classes. The same lift \(gF\) acts on both tensor factors: here its action on \(M\) reduces to \(g\), since the Frobenius action on that constant value is \(1\). The product in (5.2) is scalar multiplication by the central ring \(A\), which is defined on \(\Lambda^\natural\).

The identity-coefficient trace relation from Lesson 4 is

\[
|Z_g|\,\tau_g=\operatorname{Tr}_A(gF;P).
\tag{5.3}
\]

Under \(P=R\Gamma_c(V,A)\), the operator on the right is \(h_g^*\). Our deck action is \((g^{-1})^*\), and composition of pullbacks reverses composition of scheme maps, giving

\[
gF=(g^{-1})^*F_V^*=(F_Vg^{-1})^*
=(g^{-1}F_V)^*.
\]

The last equality uses commutation. Equation (4.29) therefore says that (5.3) is zero.

We cannot cancel \(|Z_g|\) in \(A\). Instead choose the precision promised in §3 as follows. Write \(a_g=v_\ell(|Z_g|)\), and choose

\[
N\geq e+v_\ell(|G|).
\tag{5.4}
\]

Write \(|Z_g|=\ell^{a_g}u_g\) with \(u_g\) prime to \(\ell\). Since \(u_g\) is a unit in \(A\), (5.3) implies \(\ell^{a_g}\tau_g=0\). The annihilator of \(\ell^{a_g}\) in \(\mathbf Z/\ell^N\) is the ideal \(\ell^{N-a_g}A\): lift an element to an integer and check divisibility by \(\ell^N\). Thus

\[
\tau_g\in\ell^{N-a_g}A\subset\ell^eA.
\tag{5.5}
\]

The second containment follows from \(a_g\leq v_\ell(|G|)\) and (5.4). Because \(\ell^e\Lambda=0\), every \(\tau_g\) maps to zero in \(\Lambda\). Each summand in (5.2) is therefore zero. This proves (2.3).

Reverse the reductions of §2, using their actual filtrations and Lemmas 1.2–1.3. We obtain (1.2) for every \(K_0\in D_{\mathrm{ctf}}\), every separated finite-type scheme of dimension at most one, and every left Noetherian ring killed by an integer prime to \(p\). This completes the proof of Theorem 1.1. Notice that projectivity was used over \(A[G]\), and extra precision was used only to descend the vanishing to \(\Lambda\). Neither step assumes that a group order is invertible.

Applying the theorem over \(\mathbf F_{q^r}\) proves the formula for every power:

\[
\operatorname{Tr}_\Lambda(F_X^{r*};R\Gamma_c(X,K))
=\sum_{z\in X_0(\mathbf F_{q^r})}
\operatorname{Tr}_\Lambda(F_X^{r*};K_z).
\tag{5.6}
\]

At a closed point of degree \(d\mid r\), the summands on its \(d\) geometric points have the conjugate operator \(F_x^{r/d}\), by Lesson 3. Thus (5.6) has the local powers needed for Euler products in the later L-functions lesson.

## 6. Coefficient endomorphisms and adic systems

The same covering argument retains a coefficient endomorphism. This is useful when counting points with an additional operator, and makes the passage to integral coefficients precise.

**Theorem 6.1 (a coefficient endomorphism).** Let \(\mathcal F_0\) be a constructible flat sheaf of finitely presented left \(\Lambda\)-modules, with \(\Lambda\) as in Theorem 1.1, and let \(u_0:\mathcal F_0\to\mathcal F_0\) be a sheaf endomorphism. Then, for every \(r\geq1\),

\[
\operatorname{Tr}_\Lambda\bigl(uF_X^{r*};R\Gamma_c(X,\mathcal F)\bigr)
=\sum_{z\in X_0(\mathbf F_{q^r})}
\operatorname{Tr}_\Lambda(u_zF_z;\mathcal F_z).
\tag{6.1}
\]

Here \(F_z\) is local geometric Frobenius for \(\mathbf F_{q^r}\). The same formula holds for a bounded constructible flat complex carrying an actual chain endomorphism \(u_0\), with alternating traces of the stalk complexes.

**Proof.** Work first over \(\mathbf F_q\). Naturality makes \(u\) commute with the descended Frobenius. The open–closed filtration in (1.3) is also preserved by \(u\); its graded traces therefore add. The dimension-zero proof works with the diagonal blocks \(u_xF_x\). We may consequently make the reductions of §2 and remove all rational points, keeping the restricted operator throughout.

On the arithmetic cover (3.1), the endomorphism of the constant sheaf \(\underline M\) is a single \(\Lambda\)-linear map \(u_M\): evaluation determines it from the images of a finite generating set, and these images are locally constant on the connected cover. Descent says that \(u_M\) commutes with \(G\). The isomorphisms of Lemma 3.1 then identify the operator on (3.6) with \(F\otimes u_M\). The integral group calculation of Lesson 4, Corollary 6.3, gives

\[
\operatorname{Tr}_\Lambda\bigl(uF;R\Gamma_c(U,\mathcal F)\bigr)
=\sum_{[g]}\tau_g\operatorname{Tr}_\Lambda(gu_M;M).
\tag{6.2}
\]

The coefficients \(\tau_g\) are exactly (5.1): the operator on the covering cohomology is still \(gF\). The proof of (5.5), at precision \(N\geq e+v_\ell(|G|)\), makes every coefficient zero on \(\Lambda^\natural\). Hence the expression vanishes when \(U_0(k_0)=\varnothing\), proving the required reduction. Add back the discarded rational points and strata. For a bounded flat complex with a chain endomorphism, its finite degree filtration is preserved by both operators. Apply the sheaf result to its graded terms and filtered additivity. Finally apply this argument after extending the ground field to \(\mathbf F_{q^r}\). No invertibility of \(u_0\) is required. \(\square\)

The chain-model hypothesis in the last assertion specifies the filtration used in its proof. A bare endomorphism of an arbitrary distinguished triangle over a nonreduced ring would not provide it; Lesson 4, §3 gives the explicit counterexample. The canonical Frobenius formula of Theorem 1.1 applies to every \(D_{\mathrm{ctf}}\) object because that correspondence is natural on any chosen flat model.

**Theorem 6.2 (compatible complete coefficients).** Let \(R\) be a commutative Noetherian ring, complete and separated for an ideal \(I\). Suppose every \(R/I^a\) is killed by an integer prime to \(p\). On \(X_0\) let \((K_{0,a})_{a\geq1}\) be a derived-compatible system with

\[
K_{0,a}\in D_{\mathrm{ctf}}(X_0,R/I^a),\qquad
K_{0,b}\otimes^L_{R/I^b}R/I^a\simeq K_{0,a}\quad(b\geq a).
\tag{6.3}
\]

Assume its compact-support complex and the geometric stalk at every closed point \(x\) of \(X_0\) are represented by perfect \(R\)-complexes \(P\) and \(P_x\), with natural compatible identifications

\[
P\otimes_R^LR/I^a\simeq R\Gamma_c(X,K_a),\qquad
P_x\otimes_R^LR/I^a\simeq (K_{0,a})_{\bar x},
\tag{6.4}
\]

including their Frobenius operators. At a closed point \(x\) of degree \(d\), the specified stalk operator is geometric Frobenius over \(\mathbf F_{q^d}\). Then

\[
\operatorname{Tr}_R(F_X^*;P)
=\sum_{x\in X_0(\mathbf F_q)}\operatorname{Tr}_R(F_x;P_x)
\quad\text{in }R.
\tag{6.5}
\]

The corresponding formula holds for every Frobenius power: a degree-\(d\) point contributes its \(d\) geometric stalks precisely when \(d\mid r\), with the operator \(F_x^{r/d}\). It also holds with coefficient endomorphisms whose reductions have the compatible chain models specified in Theorem 6.1.

**Proof.** A trace on a bounded finite projective model reduces to the trace on its scalar extension: each projective splitting and every matrix diagonal entry reduce modulo \(I^a\). Theorem 1.1 over the left Noetherian ring \(R/I^a\), and (6.4), therefore put the difference of the two sides of (6.5) in \(I^a\), for every \(a\). There are finitely many rational points, so the same finite sum is reduced at every level. Separatedness gives \(\bigcap_a I^a=0\), proving (6.5). Ground-field extension proves the power formula, and Theorem 6.1 proves the weighted assertion in the same way. This argument uses perfect complexes and coefficient reduction; it does not exchange an alternating sum with individual cohomology inverse limits. \(\square\)

The existence and compatibility of the perfect complexes in (6.4) are substantive hypotheses. For the classical adic systems of Lesson 1 they are proved by its compatible-perfect-complex and compact-support arguments. For the complete Noetherian constructions of Lesson 2 one uses its derived completion and proper comparison, after extending by zero to a compactification. Theorem 6.2 isolates exactly the comparison data required here; completeness alone does not assert that an arbitrary system has those data.

In particular take \(R=\mathcal O_E\), the ring of integers of a finite extension \(E/\mathbf Q_\ell\), and \(I=(\varpi)\), where \(\ell\ne p\). For a bounded constructible adic complex with a compatible integral lattice, Lesson 1 supplies (6.3)–(6.4). Its stalk and compact-support complexes are perfect over the discrete valuation ring. Bounded finitely generated integral cohomology suffices for this: such modules have length-one finite free resolutions, since a submodule of a finite free module over a discrete valuation ring is finite free. The truncation proof of Lesson 4, Lemma 4.2 then gives finite projective models. Reducing such a model also gives one common Tor interval for all its quotients. Individual integral cohomology modules can have torsion; they need not be free.

Tensoring (6.5) with \(E\), which is flat over \(\mathcal O_E\), gives

\[
\sum_i(-1)^i\operatorname{Tr}_E
\bigl(F_X^*;H_c^i(X,K_E)\bigr)
=\sum_{x\in X_0(\mathbf F_q)}\sum_i(-1)^i
\operatorname{Tr}_E\bigl(F_x;\mathcal H^i(K_E)_{\bar x}\bigr).
\tag{6.6}
\]

Over a field, splitting cycles and boundaries proves that the alternating chain trace equals the alternating cohomology trace, as in Lesson 4, (2.3). Thus (6.6) holds for complexes with a compatible integral lattice, including complexes with nonfree integral cohomology, and for every Frobenius power. A lisse \(E\)-sheaf on a normal curve has such a lattice by the continuous compact-monodromy argument of Lesson 1; its finite quotient lattices need not come from one fixed finite cover at all levels. The finite-cover proof is applied separately at each level.

## 7. Character sheaves and families of curves

For the character examples take \(E/\mathbf Q_\ell\) finite containing the required roots of unity. Their finite-image representations have integral lattices, so Theorem 6.2 gives their \(E\)-formula.

### A Kummer sheaf on \(\mathbf G_m\)

Let \(d\mid q-1\), and take a nontrivial character \(\eta:\mu_d(k_0)\to E^\times\). The cover \(y^d=x\) is a finite étale \(\mu_d\)-torsor. Its associated rank-one sheaf \(\mathcal L_\eta\) uses the diagonal coinvariant construction (3.2), with the character module \(\eta\). For a rational \(x\ne0\), choose a root \(y\). Frobenius sends it to

\[
y^q=y\,x^{(q-1)/d}.
\]

If \(t=x^{(q-1)/d}\), pullback on the indicator function of \(y\) sends it to the indicator function of \(t^{-1}y\). In diagonal coinvariants that indicator tensored with \(m\) equals the indicator at \(y\) tensored with \(tm\). Hence the local geometric Frobenius trace is

\[
\chi(x)=\eta\bigl(x^{(q-1)/d}\bigr).
\tag{7.1}
\]

The character is nontrivial because the exponent map from \(k_0^\times\) onto \(\mu_d\) is surjective. Choose \(a\) with \(\chi(a)\ne1\); reindexing the sum by multiplication by \(a\) gives \(\sum_x\chi(x)=\chi(a)\sum_x\chi(x)\), hence that sum is zero.

The cohomological side is also explicitly zero. The covering space is another \(\mathbf G_m\), with \(H_c^1=E\) and \(H_c^2=E(-1)\), and no other cohomology. Deck multiplication by a root of unity acts trivially on both: on degree two it extends to a degree-one automorphism of \(\mathbf P^1\); on degree one, the localization sequence identifies \(H_c^1\) with the cokernel of the diagonal \(E\to E^{\{0,\infty\}}\), and the automorphism fixes both boundary points. Over \(E\), the character idempotents \(|G|^{-1}\sum_g\eta(g)^{-1}g\) split the covering direct image. Since its entire cohomology has trivial deck action, every nontrivial character summand has zero cohomology. Thus both sides of the formula for \(\mathcal L_\eta\) are zero.

A Gauss sum appears after tensoring this sheaf with the restriction of the additive character sheaf below:

\[
\sum_{x\in\mathbf F_q^\times}\chi(x)\,
\psi\bigl(\operatorname{Tr}_{\mathbf F_q/\mathbf F_p}(x)\bigr)
=\sum_i(-1)^i\operatorname{Tr}
\bigl(F^*;H_c^i(\mathbf G_m,\mathcal L_\eta\otimes\mathcal L_\psi)\bigr).
\tag{7.2}
\]

This follows from the theorem, since the fibre traces of rank-one tensor factors multiply. It gives a cohomological meaning to the Gauss sum; no claim about its size is needed here.

### An Artin–Schreier sheaf on \(\mathbf A^1\)

Choose a nontrivial \(\psi:\mathbf F_p\to E^\times\), and use the torsor \(y^p-y=x\), with translations by \(\mathbf F_p\). If \(q=p^r\), its rational fibre satisfies

\[
y^q-y=\sum_{i=0}^{r-1}x^{p^i}
=\operatorname{Tr}_{\mathbf F_q/\mathbf F_p}(x).
\]

The same indicator/coinvariant calculation gives local trace \(\psi(\operatorname{Tr}(x))\). The trace map is a nonzero \(\mathbf F_p\)-linear functional: the polynomial \(\sum_{i=0}^{r-1}X^{p^i}\) is nonzero of degree less than \(q\), so cannot vanish on all of \(\mathbf F_q\). It is therefore surjective, with all fibres of size \(q/p\). Character orthogonality gives

\[
\sum_{x\in\mathbf F_q}\psi(\operatorname{Tr}(x))
=\frac qp\sum_{a\in\mathbf F_p}\psi(a)=0.
\tag{7.3}
\]

The cover is another \(\mathbf A^1\), whose only compactly supported cohomology is \(H_c^2=E(-1)\). Deck translations extend to degree-one automorphisms of \(\mathbf P^1\) fixing infinity, and act trivially on this cohomology. Splitting by character idempotents shows \(H_c^i(\mathbf A^1,\mathcal L_\psi)=0\) for every \(i\). The two sides of (7.3) therefore agree by direct calculation as well as by the theorem.

### Point counts in a smooth proper family

Let \(U_0\) be a smooth curve over \(\mathbf F_q\), and let \(\pi_0:Y_0\to U_0\) be smooth and proper, of relative dimension one, with geometrically connected fibres. Put \(\mathcal E_0=R^1\pi_{0*}\mathbf Q_\ell\). [Smooth base change and local acyclicity, Corollary 11.3 and Theorem 12.2](course:ag-etale-cohomology/smooth-base-change-and-local-acyclicity), together with proper base change, make the integral quotients locally constant and identify the fibre at \(x\in U_0(\mathbf F_q)\) with \(H^1(Y_{\bar x},\mathbf Q_\ell)\), compatibly with Frobenius. The compatible integral system \(R^1\pi_{0*}\mathbf Z/\ell^a\) supplies the lattice. Its stalks are finite free by the finite curve cohomology and duality results stated in Theorem 4.1.

For the smooth proper connected curve \(Y_x/\mathbf F_q\), the constant-coefficient trace formula gives

\[
\operatorname{Tr}(F_x;\mathcal E_{\bar x})
=q+1-\#Y_x(\mathbf F_q).
\tag{7.4}
\]

Indeed the degree-zero trace is \(1\), the degree-two trace is \(q\), and the degree-one term enters with a minus sign. Apply (6.6) to \(\mathcal E_0\), using the lattice just identified, to obtain

\[
\sum_{x\in U_0(\mathbf F_q)}
\bigl(q+1-\#Y_x(\mathbf F_q)\bigr)
=\sum_i(-1)^i\operatorname{Tr}
\bigl(F^*;H_c^i(U,\mathcal E)\bigr).
\tag{7.5}
\]

This turns the total deviation of the fibre point counts from \(q+1\) into a cohomological trace on the base. Replacing \(q\) by \(q^r\) gives the same identity over every finite extension. Geometric connectedness is used in (7.4) to make the degree-zero and degree-two terms exactly \(1,q\); without it their permutation traces must be retained. This is the family example in Milne, §29, Example 29.5, with its base-change and coefficient passage specified.

## 8. Exercises with complete solutions

**Exercise 8.1 (easy: a degree-two point).** Verify the trace formula for \(X_0=\operatorname{Spec}\mathbf F_{q^2}\) over \(\mathbf F_q\), first with constant \(\Lambda\), then with any \(K_0\in D_{\mathrm{ctf}}\).

**Solution.** There are no rational points, so the local side is zero. Geometrically there are two points, and Frobenius exchanges them. For constant coefficients the matrix on \(H^0\) is \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\), with trace zero; there is no higher cohomology. For a perfect stalk complex the operator has zero diagonal blocks in each projective representative, even if its off-diagonal coefficient maps are nontrivial. Its alternating trace is still zero. At the second power the points are both fixed; each contributes the local Frobenius of \(\mathbf F_{q^2}\), as (5.6) predicts.

**Exercise 8.2 (medium: constant coefficients and extension by zero).** Verify the formula for \(\mathbf P^1\) with constant \(\Lambda\), and for \(\mathbf A^1\) with \(j_!\Lambda\), where \(j:\mathbf G_m\hookrightarrow\mathbf A^1\).

**Solution.** For \(\mathbf P^1\), cohomology has the free rank-one terms in degrees zero and two with operators \(1,q\); the trace is the class of \((1+q)1_\Lambda\). Its \(q+1\) rational points each contribute \(1_\Lambda\). For the second example, compact support identifies \(R\Gamma_c(\mathbf A^1,j_!\Lambda)\) with \(R\Gamma_c(\mathbf G_m,\Lambda)\). The latter has degree-one trace \(1\) and degree-two trace \(q\), so its alternating trace is \((q-1)1_\Lambda\). The stalk at zero vanishes and its other \(q-1\) rational stalks have trace \(1_\Lambda\). In particular this is different from constant coefficients on all of \(\mathbf A^1\), whose answer is \(q1_\Lambda\). Specifying the domain of \(j\) removes an ambiguity in the exercise.

**Exercise 8.3 (medium: removing rational points).** Explain exactly why replacing \(U_0\) by \(U_0-U_0(k_0)\) is harmless.

**Solution.** The rational points form a finite closed reduced subscheme \(Z_0\). Lemma 1.2 splits both quantities into their values on the complementary open and on \(Z_0\). Lemma 1.3 says their values on \(Z_0\) agree, including their possibly nontrivial coefficient endomorphisms. Thus their difference on \(U_0\) equals their difference on the open with no rational points. This is a subtraction of known equal contributions, not an assertion that removing a point leaves either cohomology or its trace unchanged.

**Exercise 8.4 (medium: a twisted fixed point).** Prove that \(g^{-1}F_V\) has no fixed point in \(V\) if \(U_0(k_0)=\varnothing\), and prove simplicity of any boundary fixed point.

**Solution.** A fixed \(v\) satisfies \(F_V(v)=g(v)\). Applying \(f\) gives \(F_U(f(v))=f(v)\), since \(g\) is over \(U\). Lesson 3 identifies the last equality with a rational point of \(U_0\), a contradiction. On \(Y\), \(dF_Y=0\) and therefore \(d(g^{-1}F_Y)=0\). At a fixed boundary point its local expression has \(h^\#t\in(t^2)\). The quotient \(k[[t]]/(t-h^\#t)\) is \(k\), because \(t-h^\#t=t\) times a unit. The local multiplicity is one.

**Exercise 8.5 (hard: \(G=\mathbf Z/2\)).** Let \(G=\{1,s\}\) commute with \(F\). Write the trace-sorites computation explicitly, including the case \(\ell=2\).

**Solution.** Both conjugacy classes are singletons and both centralizers are \(G\). Put \(\tau_1=\operatorname{Tr}_A^G(F;P)\), \(\tau_s=\operatorname{Tr}_A^G(sF;P)\). Formula (5.2) is

\[
\operatorname{Tr}_\Lambda(F;(P\otimes_AM)_G)
=\tau_1\operatorname{Tr}_\Lambda(1;M)
+\tau_s\operatorname{Tr}_\Lambda(s;M).
\tag{8.1}
\]

The ordinary traces satisfy \(2\tau_1=\operatorname{Tr}_A(F;P)\), \(2\tau_s=\operatorname{Tr}_A(sF;P)\). In the fixed-point-free reduction both right sides vanish. If \(\ell\ne2\), \(2\) is a unit and \(\tau_1=\tau_s=0\). If \(\ell=2\), choose \(N\geq e+1\). Each \(\tau\) lies in \(2^{N-1}A\), so its image in \(\Lambda\), killed by \(2^e\), is zero. Thus (8.1) vanishes in both cases. At precision \(N=e\) one could not infer the latter vanishing; this is why an extra level is needed.

**Exercise 8.6 (hard: the prime-to-\(\ell\) part of the centralizer).** Suppose \(\ell^e\Lambda=0\), \(|Z_g|=\ell^au\), \(\ell\nmid u\), and \(|Z_g|\tau=0\) in \(A=\mathbf Z/\ell^N\). Prove the bound required in (5.5), and explain why it would be wrong to assume that every centralizer is an \(\ell\)-group.

**Solution.** Invert \(u\) in \(A\). Then \(\ell^a\tau=0\), so an integer lift \(t\) satisfies \(\ell^N\mid\ell^at\), or \(\ell^{N-a}\mid t\), provided \(N\geq a\). Hence \(\tau\in\ell^{N-a}A\). If \(N-a\geq e\), its image in \(\Lambda\) is zero. The cover's group is a finite monodromy image; no hypothesis forces its order, or that of its centralizers, to be a power of \(\ell\). The invertible factor \(u\) is essential to the correct argument.

**Exercise 8.7 (medium: an infinite coefficient ring).** Take \(\Lambda=\mathbf F_\ell[t]\), \(\ell\ne p\), let \(\mathcal F_0=\underline\Lambda\) on \(\mathbf A^1_{\mathbf F_q}\), and let \(u_0\) be multiplication by \(t\). Verify Theorem 6.1 directly. Explain which finiteness is needed for the covering argument.

**Solution.** Scalar extension of the constant \(\mathbf F_\ell\)-calculation gives \(R\Gamma_c(\mathbf A^1,\Lambda)=\Lambda(-1)[-2]\). Frobenius acts by \(q\), and \(u\) by \(t\), so the global trace is \(qt\in\Lambda\). Each of the \(q\) rational stalks has \(uF_x=t\), and their sum is also \(qt\). The ring and module have infinite underlying sets, but the stalk is generated by \(1\). A continuous discrete action fixing a finite generating set fixes the module; this, together with normality of the curve, gives finite monodromy. The proof does not require finite cardinality of \(\Lambda\).

**Exercise 8.8 (hard: a torsion integral cohomology module).** On \(X_0=\operatorname{Spec}\mathbf F_q\), take the constant integral complex \([\mathcal O_E\xrightarrow{\varpi}\mathcal O_E]\) in degrees \(0,1\), with identity Frobenius and with a chain endomorphism given by multiplication by \(a\in\mathcal O_E\) in both degrees. Compute its integral and finite-level traces. Explain why taking traces on individual integral cohomology modules would not give the appropriate definition.

**Solution.** Its cohomology is zero in degree zero and \(\mathcal O_E/\varpi\) in degree one. The latter is not projective over \(\mathcal O_E\), so its endomorphism has no projective-module trace in \(\mathcal O_E\). The displayed perfect model instead has alternating trace \(a-a=0\). Derived reduction modulo \(\varpi^b\) is computed by the same two free terms with differential \(\varpi\); the reduced chain trace is again \(\bar a-\bar a=0\), even though both kernels and cokernels can occur at finite level. These are the compatible traces in Theorem 6.2. There is one rational point, whose stalk is the same perfect complex, so the global and local traces agree at every level and integrally. Tensoring with \(E\) makes the complex acyclic and again gives trace zero.

## Proof dependencies and coefficient scope

- Étale topological invariance, the finite étale fundamental-group classification, and smooth projective completion of a curve over a perfect field. The latter is [Stacks, Tag 0H1F]. These are the geometric foundations used in §§2–4.
- The compact-support construction, finite direct-image and support-composition properties, and the bounded constructible flat models for \(D_{\mathrm{ctf}}\). Lessons 1 and 4 supply these; §3 verifies the particular cover descent and stalk projectivity directly.
- Perfectness, filtered trace additivity, coefficient projection, and the integral group trace sorites: Lesson 4, Theorems 3.1, 4.3–4.4 and 6.2, Corollary 6.3. Their full coefficient hypotheses are preserved here.
- The proper constant-coefficient curve formula, its finite-level form, and the product-diagonal compatibility are proved in Theorem 4.1. Proposition 4.2 supplies the open-curve subtraction. This proof uses the explicit degree-normalized curve duality and product comparison cited there.
- The basic constant-coefficient cohomology of \(\mathbf P^1,\mathbf A^1,\mathbf G_m\), from the first lesson and localization. Section 7 proves the character-summand vanishings from these computations.
- Compatible adic perfect complexes and scalar extension come from Lesson 1. The complete Noetherian formulation of Theorem 6.2 states all its comparison data explicitly. Proper smooth local constancy in the family example has its exact proof home in the smooth-base-change lesson, Corollary 11.3 and Theorem 12.2; its inherited general constructibility input is stated there.

<a id="references-and-source-record"></a>

## References

Deligne, *Cohomologie étale* (SGA \(4\frac12\)), [Rapport], §5, especially Lemmas 5.1–5.2, Theorem 5.3, Corollary 5.4 and §§5.12–5.13, printed pp. 100–106, gives the Nielsen–Wecken route from constant coefficients to a finite covering and back. Theorem 4.10, printed p. 96, states the general finite-coefficient trace formula; §6, pp. 107–108, records the filtration reductions. The proof above specifies the stalk isomorphisms, group-ring projectivity, boundary multiplicities and the precision estimate instead of dividing in a finite coefficient ring.

The Stacks locators are [Tag 03UF](https://stacks.math.columbia.edu/tag/03UF), [Theorem 03UG](https://stacks.math.columbia.edu/tag/03UG), and the group-trace preliminaries [03U4](https://stacks.math.columbia.edu/tag/03U4), [03UB](https://stacks.math.columbia.edu/tag/03UB), [03UC](https://stacks.math.columbia.edu/tag/03UC) and [03UD](https://stacks.math.columbia.edu/tag/03UD). They appear in [AI Integrated Stacks Project, English, The Trace Formula](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/trace.html#trace-section-proof-trace-formula), which retains these upstream locators.

Grothendieck, written up by Bucur, SGA 5, Exposé XII, “Nielsen–Wecken and Lefschetz formulas in algebraic geometry,” gives the historical covering and local-invariant framework. We use the self-contained curve and finite-coefficient arguments established in this course.

James S. Milne, [*Lectures on Étale Cohomology*, version 2.21](https://www.jmilne.org/math/CourseNotes/LEC.pdf), §29, printed pp. 163–168, supplies the mapped nonconstant-sheaf formula, its coefficient correspondence and the family example. Lemma 29.3's correspondence is proved for the larger scope in Lesson 3. Theorem 29.4 is the lisse rational-coefficient case of (6.6), and Example 29.5 becomes (7.4)–(7.5). The finite noncommutative argument and compatible-perfect-complex passage above specify the additional hypotheses and do not assume that integral cohomology is free.

Deligne and Milne retain credit for the cited results and their own source terms. This lesson's exposition and arguments are CC0. AI Integrated Stacks material retains its identified AI contribution and the underlying human Stacks Project credit and GFDL terms.

The curve Riemann hypothesis and its surface-intersection proof are separate from the trace identities established here. No Hodge index theorem or eigenvalue-size bound is an input to this lesson.
