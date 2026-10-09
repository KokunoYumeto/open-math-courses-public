# Springer theory

*Written and revised by OpenAI models in Codex at Ultra effort, October 2026. Self-checked by the models that wrote it. Public domain (CC0).*

A nilpotent matrix determines a space of compatible flags. For a nonzero nilpotent \(2\times2\) matrix that space is a point; for the zero matrix it is a projective line. The cohomology of these fibres nevertheless carries the same symmetric group, with different representations in different degrees. Our task is to construct that action, determine its normalization, and explain why irreducible representations are attached to intersection complexes.

We begin with the fibres themselves. Pairs of flags then supply the dimension estimates needed for the global sheaf. Restriction with supports identifies its endomorphisms after passage to the nilpotent cone. Finally, explicit Fourier kernels lead to a second action, whose difference from the first is the sign character. This order separates the geometry of the resolution, the construction of an action, and the comparison of two constructions.

The geometric sheaf arguments use [Semismall maps and small resolutions](semismall-maps-and-small-resolutions.md), [Intermediate extensions and intersection complexes](intermediate-extensions-and-intersection-complexes.md), and the operations of Constructible complexes on algebraic varieties. Their exact foundational scope and the Lie-theory inputs specified below are prerequisites, including where they still require proofs. A reference to a free paper does not supply those missing proofs.

Unless coefficients are explicitly changed, let \(\Lambda\) be an algebraically closed field of characteristic zero and work on complex varieties. The arithmetic version uses geometric \(\overline{\mathbb Q}_\ell\)-sheaves, \(\ell\ne p\), on a split connected semisimple group in the adjoint-quotient range of Juteau, §4.1: \(p\) is not a torsion prime, and \(p>2\) for a type \(C\) component. The matrix examples use \(p>3\). Tate twists are retained in arithmetic formulas and suppressed classically. Fourier theory additionally requires a specified nondegenerate invariant symmetric form.

## 1. What the flag fibres look like

### Two-dimensional vector spaces

Write an element of \(\mathfrak{sl}_2\) as
\[
x=\begin{pmatrix}z&a\\-b&-z\end{pmatrix}.
\]
Its nilpotent cone is the surface \(z^2=ab\). Let \(V\) be the two-dimensional vector space over the ground field. A complete flag is a line \(L\subset V\). Compatibility with a nilpotent endomorphism means
\[
\operatorname{im}x\subset L\subset\ker x.
\tag{1.1}
\]
For \(x\ne0\), image and kernel are the same line, so there is one flag. For \(x=0\), every line is allowed and the fibre is \(\mathbb P^1\).

Fixing \(L\), the possible matrices are exactly \(\operatorname{Hom}(V/L,L)\). Over \(\mathbb P(V)\), the tautological line is \(\mathcal O(-1)\), and \(V/L\) is \(\mathcal O(1)\) after fixing a volume form on \(V\). Hence the incidence variety in (1.1) is
\[
Y_0=\operatorname{Tot}\mathcal O_{\mathbb P^1}(-2)
=T^*\mathbb P^1.
\tag{1.2}
\]
It is smooth. Its map to the cone is proper because the incidence conditions are closed in \(\mathcal N\times\mathbb P^1\). Away from the vertex its inverse sends \(x\) to \(\operatorname{im}x\), a regular map on either nonzero-column chart. Thus this is a resolution with a single exceptional curve. Its normalized pushforward has stalks
\[
(R\pi_{0*}\Lambda[2])_x=
\begin{cases}
\Lambda[2],&x\ne0,\\
R\Gamma(\mathbb P^1,\Lambda)[2],&x=0.
\end{cases}
\tag{1.3}
\]
At the vertex the two nonzero cohomology groups have degrees \(-2\) and \(0\), the latter carrying twist \((-1)\). Determining their Weyl-group labels requires the action constructed below; a picture of the exceptional curve alone does not determine them.

### Three-dimensional vector spaces

A flag now has the form \(L\subset H\subset V\), with dimensions one and two. The nilpotent incidence conditions are
\[
xL=0,\qquad xH\subset L,\qquad xV\subset H.
\tag{1.4}
\]
For a regular Jordan block of length three, these force \(L=\ker x\) and \(H=\ker x^2\). At zero the fibre is the full flag variety: choosing \(L\) gives \(\mathbb P^2\), and choosing \(H\) above it gives a projective-line bundle. The projective-bundle unit and first Chern class compute its cohomology as
\[
\dim H^{2a}(\mathcal B,\Lambda)=1,2,2,1
\quad(a=0,1,2,3),\qquad H^{2a+1}=0.
\tag{1.5}
\]
The degree \(2a\) terms have twist \((-a)\).

The remaining Jordan type has a basis with \(xe_2=e_1\) and \(xe_1=xe_3=0\). Put \(I=\langle e_1\rangle\) and \(K=\langle e_1,e_3\rangle\). If \(H=K\), (1.4) permits every line of \(K\); these flags form a curve \(C_1\simeq\mathbb P^1\). If \(H\ne K\), then \(xH=I\), so \(L=I\). Conversely every plane through \(I\), paired with \(L=I\), satisfies (1.4). These flags form \(C_2\simeq\mathbb P^1\). Their only common point is \((I,K)\).

Consequently the reduced subregular fibre is \(C_1\cup C_2\). Nilpotent thickenings do not change the classical or étale sheaf calculation. The difference of restriction values gives the exact sequence
\[
0\longrightarrow\Lambda_{C_1\cup C_2}
\longrightarrow\Lambda_{C_1}\oplus\Lambda_{C_2}
\longrightarrow\Lambda_{(I,K)}\longrightarrow0.
\tag{1.6}
\]
On degree-zero cohomology the last map is \((u,v)\mapsto u-v\), hence is surjective. Its long exact sequence gives \(H^0=\Lambda\), \(H^1=0\), and \(H^2=\Lambda(-1)^2\), with no other groups. The two top classes will carry the two-dimensional standard representation of \(S_3\), rather than an action obtained merely by permuting the two components.

## 2. Pairs of flags construct the global action

Now let \(G\) be a connected reductive group, \(B\) a Borel subgroup, \(T\subset B\) a maximal torus, and \(\mathfrak n\) the nilradical of \(\mathfrak b\). Use
\[
\mathcal B=G/B,\qquad W=N_G(T)/T,\qquad
r=\dim T,\quad n=\dim\mathcal B=|\Phi^+|,\quad D=2n+r.
\]
The Lie-theory prerequisites used here are the Bruhat decomposition and its root-space descriptions, the regular semisimple Cartan and adjoint-quotient theory, and the assertion that each Lie algebra element belongs to a Borel. For the nilpotent cone we also need irreducibility, dimension \(2n\), finitely many orbits, and uniqueness of a containing Borel for a regular nilpotent element. These inputs are not proved by the ensuing dimension calculation. We define \(\mathcal N\) by conjugates of Borel nilradicals; a central torus therefore contributes only its zero element.

Consider the two vector bundles and their proper projections:
\[
Y=G\times^B\mathfrak b\xrightarrow{\pi}\mathfrak g,
\qquad Y_0=G\times^B\mathfrak n\xrightarrow{\pi_0}\mathcal N.
\tag{2.1}
\]
They are smooth of dimensions \(D\) and \(2n\). Both incidence varieties are closed in the product of their target with the projective flag variety. In particular their projections are projective. The specified Lie inputs imply surjectivity.

### The dimension calculation

Diagonal \(G\)-orbits in \(\mathcal B\times\mathcal B\) have relative positions \(w\in W\). For \((B,wBw^{-1})\), the common positive roots number \(n-\ell(w)\). A common Cartan contributes the remaining \(r\) dimensions in the Borel intersection. Thus
\[
\begin{array}{c|c}
\text{space}&\text{dimension}\\ \hline
G\cdot(B,wBw^{-1})&n+\ell(w)\\
\mathfrak b\cap w\mathfrak b&r+n-\ell(w)\\
\mathfrak n\cap w\mathfrak n&n-\ell(w).
\end{array}
\tag{2.2}
\]
The part of \(Z=Y\times_{\mathfrak g}Y\) above that pair orbit is the vector bundle with fibre \(\mathfrak b\cap w\mathfrak b\); call it \(Z_w\). Its dimension is \(D\). The corresponding part \(Z_{0,w}\) of \(Z_0=Y_0\times_{\mathcal N}Y_0\) has dimension \(2n\). The fibre-product criterion of Lesson 9 therefore proves semismallness of both projections.

For \(\pi\), the inequality is strict away from the regular semisimple locus. Indeed, the common Cartan in every intersection of Borels contains regular semisimple elements. Intersecting that vector space with \(C=\mathfrak g\setminus\mathfrak g^{\rm rs}\) gives a proper closed subset and lowers dimension by at least one. Hence \(\dim Z|_C\le D-1\). If \(S\subset C\) is an adapted stratum and \(x\in S\), the dimension of its fibre product is
\[
\dim S+2\dim\pi^{-1}(x)\le D-1.
\tag{2.3}
\]
This proves smallness, without knowing each Springer fibre separately.

### From a torsor to an intermediate extension

Let \(\mathfrak t^{\rm reg}\) be the complement of the root hyperplanes. The Cartan description identifies the regular semisimple restriction of \(\pi\) with
\[
Y^{\rm rs}\simeq\mathfrak g^{\rm rs}
\times_{\mathfrak t^{\rm reg}/W}\mathfrak t^{\rm reg}.
\tag{2.4}
\]
The map assigns the class of an element in the containing Borel modulo its nilradical. The free action on \(\mathfrak t^{\rm reg}\) makes this a finite étale \(W\)-torsor. The Cartan isomorphism, including étaleness, is needed here: counting \(|W|\) points would not establish it.

Put \(L=\pi^{\rm rs}_*\Lambda\), without a shift. Smallness and the strict boundary characterization in Lessons 4 and 9 give
\[
\mathsf S_{\mathfrak g}:=R\pi_*\Lambda_Y[D]
=\operatorname{IC}_{\mathfrak g}(L).
\tag{2.5}
\]
Every map of local systems extends uniquely to a map of intermediate extensions. For existence, apply the map to the natural morphisms from perverse extension by zero to perverse direct image, then take their images. For uniqueness, an endomorphism zero on the open set has image supported on the boundary; an intermediate extension has no such nonzero subobject. This proves the full faithfulness being used.

Since \(Y\) is irreducible, \(Y^{\rm rs}\) is connected. Thus the monodromy of its torsor is the full group \(W\), acting regularly on its fibre. Label a basis by \(e_a\), \(a\in W\), so monodromy acts on the left. Define the deck convention by
\[
\rho(w)e_a=e_{aw^{-1}}.
\tag{2.6}
\]
Then \(\rho(w)\rho(v)=\rho(wv)\). A commuting endomorphism is determined by its value on \(e_1\), and any value defines one by equivariance. Its space has dimension \(|W|\), with basis the operators (2.6). Consequently
\[
\operatorname{End}(\mathsf S_{\mathfrak g})
=\operatorname{End}(L)=\Lambda[W].
\tag{2.7}
\]
All endomorphisms in this lesson have degree zero. For characteristic-zero coefficients the regular bimodule decomposes into \(V\otimes V^\vee\). The first factor describes monodromy; the dual describes deck multiplicity. We shall label the eventual correspondence by the deck representations, retaining this left/right convention.

### Why the same small-map argument works integrally

Later we need (2.5)–(2.7) over \(\mathbb Z\) or a coefficient discrete valuation ring \(A\), not merely a field. Here is the additional bound rather than an appeal to self-duality of an entire integral perverse heart. Write \(K=R\pi_*A[D]\). Properness and smooth orientation give \(\mathbb D K=K(D)\). For a boundary stratum of dimension \(s\), smallness and the fibre-cohomology bound give
\[
i_S^*K\in D^{\le -s-1}.
\]
Refine the stratum so its cohomology sheaves are locally constant. Its dualizing complex is \(A[2s](s)\). The spectral sequence computing \(R\operatorname{Hom}_A(C,A)\) for a bounded complex \(C\in D^{\le -s-1}\) has terms from nonnegative Ext degrees only, so it lies in \(D^{\ge s+1}\). Dualizing on the stratum and shifting by \([2s]\) therefore yields
\[
i_S^!K\in D^{\ge -s+1}.
\tag{2.8}
\]
The two strict bounds, together with the free local system on the open stratum, characterize the integral intermediate extension. This uses constructible duality over a ring of finite global dimension; it does not assert that Verdier duality is exact for the ordinary integral perverse heart. Full faithfulness and the regular-module calculation above then prove \(\operatorname{End}(K)=A[W]\). The ordinary and adic operation foundations at this coefficient scope remain required.

## 3. Restriction retains every endomorphism

Let \(i:\mathcal N\hookrightarrow\mathfrak g\). Proper base change in (2.1) and the equality \(D=2n+r\) give
\[
\mathsf S_{\mathcal N}:=R\pi_{0*}\Lambda_{Y_0}[2n]
=i^*\mathsf S_{\mathfrak g}[-r].
\tag{3.1}
\]
Semismallness makes this perverse. Applying \(i^*[-r]\) to the deck action defines the *restriction action* \(\rho\). The shift is minus the rank: for a one-dimensional torus the global resolution is the identity on a line, and restriction takes \(\Lambda[1]\) to the same complex on a point. Only \([-1]\) gives the point's perverse constant sheaf. Formula (3.1) says nothing about exactness of restriction on arbitrary perverse sheaves.

We will show that restriction gives an algebra isomorphism
\[
\operatorname{End}(\mathsf S_{\mathfrak g})
\xrightarrow{\ \sim\ }\operatorname{End}(\mathsf S_{\mathcal N}).
\tag{3.2}
\]
It is essential to identify this particular map. Equality of dimensions of the two algebras would not suffice.

### Expressing the map by cohomology with supports

For a proper map \(f:Y\to X\) from a smooth \(d\)-fold, put \(Z=Y\times_XY\) and let \(p_2:Z\to Y\) be the second projection. Define Borel–Moore homology by \(H_b^{\rm BM}(Z)=H^{-b}(Z,\omega_Z)\). Proper base change followed by the adjunctions \((f^*,Rf_*)\) and \((Rp_{2!},p_2^!)\) yields
\[
\begin{aligned}
\operatorname{End}(Rf_*\Lambda[d])
&=\operatorname{Hom}(f^*Rf_*\Lambda[d],\Lambda[d])\\
&=\operatorname{Hom}(Rp_{2*}\Lambda_Z[d],\Lambda_Y[d])\\
&=\operatorname{Hom}(\Lambda_Z,\omega_Z[-2d](-d))\\
&=H_{2d}^{\rm BM}(Z)(-d).
\end{aligned}
\tag{3.3}
\]
The orientation identity used in the third line is \(\omega_Y=\Lambda(d)[2d]\); \(Z\) itself need not be smooth.

For our two maps use the notation \(Z,Z_0\) of §2. Nilpotence forces the Cartan class in any containing Borel to be zero, so also \(Z_0=Y\times_{\mathfrak g}Y_0\). Inside the smooth spaces \(M=Y\times Y\) and \(M_0=Y\times Y_0\), respectively, the groups in (3.3) become
\[
\begin{aligned}
H_{2D}^{\rm BM}(Z)(-D)&=H_Z^{2D}(M)(D),\\
H_{4n}^{\rm BM}(Z_0)(-2n)&=H_{Z_0}^{2D}(M_0)(D).
\end{aligned}
\tag{3.4}
\]
For a smooth ambient \(h\)-fold this is the identity
\(H_b^{\rm BM}(Z)=H_Z^{2h-b}(M)(h)\), obtained from \(\omega_Z=e^!\omega_M\). Pullback of relative cochains for the pair \((M,M\setminus Z)\) to \((M_0,M_0\setminus Z_0)\) defines a map in (3.4). In the étale formulation, pull back the supported morphism \(\Lambda_M\to e_*e^!\Lambda_M[2D](D)\) and use closed-support exchange. This decreases the Borel–Moore degree by \(2r\); it is not ordinary restriction of homology to a closed subset.

To verify that it gives (3.2), set \(P=R\pi_*\Lambda[D]\) and \(e_0:Y_0\hookrightarrow Y\). Under adjunction,
\[
\operatorname{End}(i^*P)=\operatorname{Hom}(P,i_*i^*P).
\]
Restriction of an endomorphism \(\alpha\) corresponds to the composite of \(\alpha\) with the unit \(P\to i_*i^*P\). Proper base change identifies this unit with the pushforward of
\(\Lambda_Y[D]\to e_{0*}\Lambda_{Y_0}[D]\).
Applying the two adjunctions of (3.3) to that composite restricts its second factor from \(Y\) to \(Y_0\). In particular \(Rp_{2*}\Lambda_Z[D]\) changes to the corresponding pushforward from \(Z_0\), and the target becomes \(\Lambda_{Y_0}[D]\). The final orientation is \(\omega_{Y_0}=\Lambda(2n)[4n]\), giving the second group of (3.4). The closed unit used here is the same unit defining pullback with supports; the base-change morphisms are its adjunction mates. Hence these identifications take restriction of endomorphisms to that pullback, with no undetermined scalar. Notice that \(i^*P=\mathsf S_{\mathcal N}[r]\): the mixed Hom target before canceling equal shifts must retain \([r]\).

### Computing restriction on top component classes

Order the Bruhat strata by a linear extension of Bruhat order. A downward-closed set \(I\subset W\) gives closed unions \(Z_I\) and \(Z_{0,I}\). Their maximal-dimensional components are the closures of the smooth connected bundles \(Z_w\) and \(Z_{0,w}\) in (2.2). Top Borel–Moore homology is free on these component classes: remove the intersections and singular loci of the components, whose dimensions are smaller, and apply localization and the top-dimension bound. This is the top-class argument in Lesson 9, applicable also to integral coefficients.

If \(w\) is a new maximal member and \(J=I\setminus\{w\}\), localization therefore gives
\[
0\longrightarrow H_{2D}^{\rm BM}(Z_J)
\longrightarrow H_{2D}^{\rm BM}(Z_I)
\longrightarrow H_{2D}^{\rm BM}(Z_w)\longrightarrow0,
\tag{3.5}
\]
and the analogous sequence in degree \(4n\) for \(Z_0\). Surjectivity at the right is supplied by the class of \(\overline{Z_w}\), which restricts to the fundamental class of \(Z_w\). No vanishing assertion about the previous odd-degree group is needed.

The intersection of \(Z_w\) with \(M_0\) is transverse. Indeed, the second Borel's Cartan-class map \(Z_w\to\mathfrak t\) is surjective on each vector fibre: a common Cartan maps isomorphically to the Cartan quotient. It is therefore smooth, and its zero fibre is \(Z_{0,w}\). In local normal coordinates, the supported orientation class is the product of the oriented normal-coordinate classes. Pulling it back along a transverse coordinate inclusion gives precisely the corresponding product for the intersection. Its coefficient is \(+1\), by complex orientation, or by normalized smooth trace in the étale coordinates. Thus the top-class map for each pair \(Z_w,Z_{0,w}\) is an isomorphism.

The maps with closed support and with open complement commute with pullback of these relative cochains. Equivalently the closed units and their base-change mates commute with the localization triangles. Hence the two sequences (3.5) form a commutative diagram with the restriction maps. Induction on \(I\) proves the isomorphism for \(I=W\). By the map identification in (3.4), this proves (3.2) as an algebra map:
\[
\operatorname{End}(\mathsf S_{\mathcal N})=\Lambda[W].
\tag{3.6}
\]
The argument neither divides by \(|W|\) nor computes a convolution table. Together with §2's coefficient bounds it works over coefficient fields and, with the stated operation foundations, over \(\mathbb Z\) and a coefficient discrete valuation ring.

### From the algebra to Springer pairs

Return to characteristic-zero coefficients. Averaging makes the regular \(W\)-local system semisimple; its global IC extension has a decomposition
\(\mathsf S_{\mathfrak g}=\bigoplus_V Q_V\otimes V\)
with distinct simple \(Q_V\), indexed by irreducible deck representations. Applying \(i^*[-r]\) preserves this direct-sum decomposition. Each resulting constituent is perverse because it is a direct summand of (3.1). The semismall decomposition theorem in Lesson 9 makes the latter sheaf semisimple. Finally (3.2) preserves its primitive matrix blocks: the restricted \(Q_V\) is nonzero, has endomorphism field \(\Lambda\), and has no morphisms to a different restricted constituent. A nonzero semisimple object with that endomorphism field is simple. Thus
\[
\mathsf S_{\mathcal N}\simeq
\bigoplus_{V\in\operatorname{Irr}W}
\operatorname{IC}_{\overline{\mathcal O_V}}(E_V)\otimes V.
\tag{3.7}
\]
ICs are normalized by the dimension of their support. The pairs \((\mathcal O_V,E_V)\) form the *Springer pairs*. This is a bijection onto the pairs occurring in this sheaf; it does not assert that every equivariant local system on every orbit occurs.

At a relevant orbit of dimension \(s\), the multiplicity local system is top fibre cohomology \(H^{2n-s}(\pi_0^{-1}(x),\Lambda)\). The component group \(A_x=\pi_0Z_G(x)\) acts on the components of that fibre. Its action commutes with the Weyl action, and its irreducible constituents specify the orbit local systems in (3.7). The regular nilpotent fibre is a point and receives the trivial deck representation. More globally, the invariant summand of \(\mathsf S_{\mathfrak g}\) is \(\operatorname{IC}_{\mathfrak g}(\Lambda)=\Lambda_{\mathfrak g}[D]\); restriction gives \(\Lambda_{\mathcal N}[2n]\). The simplicity just proved identifies this with the full-support constituent.

This deduction uses geometric semisimplicity at exactly the scope of Lessons 7–9. The endomorphism calculation alone does not prove semisimplicity, and so cannot substitute for those prerequisites.

## 4. The two Fourier kernels and their normalizations

Fix a nondegenerate invariant symmetric pairing on \(\mathfrak g\). Invariance under the torus makes root spaces orthogonal unless their weights are opposite. It follows that \(\mathfrak b^\perp\) contains \(\mathfrak n\); their dimensions agree, so
\(\mathfrak b^\perp=\mathfrak n\).
In particular the nilradical bundle in (2.1) is \(T^*\mathcal B\). The pairing is a real hypothesis. A reductive Lie algebra's Killing form vanishes on its centre. In characteristic zero one can combine the semisimple Killing form with a nondegenerate form on that centre. For \(\mathfrak{sl}_m\), \(m=2,3\), the trace pairing works when \(p\nmid m\): inside all matrices the orthogonal complement of the traceless matrices is the scalar line, and its intersection with them is zero precisely under that condition.

### Compact integration of a character

Over a field of characteristic \(p\), choose a nontrivial character \(\psi:\mathbb F_p\to k^\times\), where the coefficient field \(k\) has characteristic different from \(p\) and contains the necessary roots of unity. The étale Artin–Schreier covering \(t\mapsto t^p-t\) has group \(\mathbb F_p\). Its character projectors are defined because \(p\) is invertible. Its compact cohomology is that of the covering affine line, namely \(k(-1)[-2]\). Each deck translation extends to a degree-one automorphism of the projective line and therefore fixes the top trace class. Only the trivial character contributes to this cohomology. Thus its nontrivial character sheaf satisfies
\[
R\Gamma_c(\mathbb A^1,\mathcal L_\psi)=0.
\tag{4.1}
\]
The affine-line trace, iterated by compact-support composition and projection, also gives \(R\Gamma_c(\mathbb A^b,k)=k(-b)[-2b]\). Any nonzero linear functional is a coordinate after a linear change of basis. Its character sheaf has zero compact integral by (4.1) and the same iteration.

For a rank-\(D\) vector bundle \(E\to S\), define the relative arithmetic transform on the dual bundle by
\[
\mathcal F_E(K)=Rp_{2!}\bigl(p_1^*K\otimes\mathcal L_\psi(\langle x,\xi\rangle)\bigr)[D].
\]
If \(v:V\hookrightarrow E\) is a rank-\(b\) subbundle, its value at a covector is the compact integral over \(V_s\), with total shift \([D+b]\). It vanishes unless the covector annihilates \(V_s\). On the annihilator the kernel is canonically constant, and the vector trace supplies \(k(-b)[D-b]\). Closed base change followed by localization therefore identifies the whole complex:
\[
\mathcal F_E(v_*k_V[b])
=v^\perp_*k_{V^\perp}[D-b](-b).
\tag{4.2}
\]
This is stronger than an equality of stalk dimensions. A complex vanishing on the complementary open is the closed extension of its restriction, and the restriction here comes with the specified trace isomorphism. The traces agree under changes of frame.

The arithmetic kernel also proves inversion without a perverse-exactness theorem. In two successive transforms, integration over the middle vector \(y\) has kernel \(\mathcal L_\psi(\langle y,x+z\rangle)\). The character-addition isomorphism follows by adding lifts in the two Artin–Schreier torsors. Formula (4.1) makes this integral zero off \(x+z=0\); on that graph it is \(k(-D)[-2D]\). Localization identifies its graph extension. The two shifts \([D]\) cancel the cohomological shift, giving, for \(a(x)=-x\),
\[
\mathcal F_{E^\vee}\mathcal F_E(K)=a_*K(-D).
\tag{4.3}
\]
Fubini for compact pushforwards and the projection formula move an arbitrary constructible \(K\) outside the middle integration. Thus (4.3) is functorial, proves a derived equivalence, and specifies its inverse using negation and twist \((D)\).

### Compact integration of a half-space

On a complex vector bundle instead use
\[
Q=\{(x,\xi):\operatorname{Re}\langle x,\xi\rangle\le0\},
\qquad \mathcal F_E^{\rm S}=R\check q_!q^*[D],
\]
with projections from \(Q\). Above a covector annihilating \(V_s\), the fibre of this kernel on \(V\) is the entire complex \(b\)-space. Otherwise it is a closed real half-space, homeomorphic to \(\mathbb R^{2b-1}\times[0,\infty)\). The compact cohomology of the last factor is zero: its one-point compactification computes the relative cohomology of an interval and one endpoint, and that endpoint inclusion is a homotopy equivalence. Integrating the other real coordinates preserves zero. At the annihilator complex orientation gives \(k[-2b]\). Closed base change, localization and gluing of the oriented trace prove
\[
\mathcal F_E^{\rm S}(v_*k_V[b])
=v^\perp_*k_{V^\perp}[D-b].
\tag{4.4}
\]
The proof also works over \(\mathbb Z\). It fixes the exchange map by trace. General conic inversion and general perverse exactness are separate assertions: SH-02's kernel-calculus unit develops kernel composition relative to its operation inputs but still leaves conic Fourier–Sato theory open.

### Apply the kernels to the incidence bundle

Take \(E=\mathcal B\times\mathfrak g\), with subbundle \(Y\) of rank \(b=n+r\) and annihilator \(Y_0\) of rank \(n\). Its source normalization \([D]\) is \([b]\) followed by \([n]\). The proper projection off \(\mathcal B\) commutes with both kernel operations: both composite expressions integrate over the same flag and vector variables, with the same pulled-back kernel. Proper base change, projection and composition identify these maps. Equations (4.2) and (4.4) now give
\[
\mathcal F_\psi(\mathsf S_{\mathfrak g})
=i_*\mathsf S_{\mathcal N}(-n-r),\qquad
\mathcal F^{\rm S}(\mathsf S_{\mathfrak g})=i_*\mathsf S_{\mathcal N}.
\tag{4.5}
\]
For the arithmetic transform, (4.3) and the negation-invariance of the incidence bundle imply
\[
\mathcal F_\psi(i_*\mathsf S_{\mathcal N})=\mathsf S_{\mathfrak g}(-n).
\tag{4.6}
\]
The twists add to \((-D)\), as inversion requires. Closed extension is fully faithful, so arithmetic Fourier equivalence gives another algebra isomorphism from \(\Lambda[W]\) to \(\operatorname{End}(\mathsf S_{\mathcal N})\).

Let \(\phi(w)\) denote the deck endomorphism transported through the specified exchange (4.5), and retain \(\rho(w)\) for restriction. Neither object identity identifies these actions. We next prove their precise comparison,
\[
\phi(w)=\varepsilon(w)\rho(w),\qquad \varepsilon(w)=(-1)^{\ell(w)}.
\tag{4.7}
\]
For adic coefficients the kernel operations above require the normalized adic pushforward and coefficient foundations of Lesson 1. The finite character calculation does not by itself construct those functors.

## 5. Why the classical actions differ by sign

Work over \(\mathbb C\), initially with integral cohomology. The Lie-theory input identifies
\(q_T:G/T\to\mathcal B\)
as a locally trivial affine-space bundle of complex rank \(n\). Ordinary pullback and compact oriented trace transport the right normalizer maps on \(G/T\) to two actions on flag cohomology, written \(O\) and \(C\), respectively. For each \(w\), use pullback under \(gT\mapsto g\dot wT\), equivalently covariant transport under \(gT\mapsto g\dot w^{-1}T\). Right translations compose in reverse order, so these pullbacks give \(O(w)O(v)=O(wv)\), and likewise for \(C\).

### The top class and the mixed pairing

On \(G/T\), the pullback of \(T\mathcal B\) splits into the root lines of \(\mathfrak g/\mathfrak b\), with weights \(-\Phi^+\). If \(L_\chi=G\times^T\mathbb C_\chi\), right translation pulls it back to \(L_{w\chi}\): its frame changes by \(\chi(\dot w^{-1}t\dot w)\). The product expression for the top Chern class and \(c_1(L_{-\alpha})=-c_1(L_\alpha)\) give
\[
q_T^*c_n(T\mathcal B)=\prod_{\alpha>0}c_1(L_{-\alpha}),
\qquad O(w)c_n(T\mathcal B)=\varepsilon(w)c_n(T\mathcal B).
\tag{5.1}
\]
Exactly \(\ell(w)\) positive roots change sign; all Chern factors have even degree and commute.

This class is nonzero integrally. A regular Cartan element induces a vector field on \(\mathcal B\) with precisely \(|W|\) zeros, the Borels containing it. At each zero, the root eigenvalues of its tangent linearization are nonzero. The local index is \(+1\), since an invertible complex-linear map has positive real determinant \(|\det_{\mathbb C}|^2\). Restricting the oriented Thom class to disjoint neighbourhoods of these zeros and using localization computes the Euler class as their sum. Complex line normalization and multiplicativity identify that Euler class with \(c_n\). Therefore \(\int_{\mathcal B}c_n=|W|\). Since \(H^{2n}(\mathcal B,\mathbb Z)=\mathbb Z\), equation (5.1) forces the ordinary top action to be \(\varepsilon\). This integral conclusion precedes any reduction modulo a prime; no modular division by \(|W|\) occurs.

The compact top action is trivial. Its trace identification comes from \(H_c^{4n}(G/T,\mathbb Z)\), whose complex-oriented generator is fixed by every holomorphic right translation. Put \(u:H_c^\bullet(\mathcal B)\to H^\bullet(\mathcal B)\) for the usual identification on the proper flag variety. Bruhat cells have even real dimension, so the integral cellular complex has zero differentials and free cohomology. Poincaré duality gives a perfect cup pairing. The mixed ordinary/compact pairing on \(G/T\), and the projection formula for \(q_T\), make it equivariant for \(O,C\). For complementary \(v,z\) this gives
\[
O(w)v\cdot uC(w)z=v\cdot uz,\qquad
O(w)v\cdot O(w)uz=\varepsilon(w)v\cdot uz.
\]
Perfection, allowing \(O(w)v\) to range over every complementary class, proves
\[
uC(w)=\varepsilon(w)O(w)u.
\tag{5.2}
\]
The pairing and the equality hold integrally and after extension to every coefficient field.

### Faithfulness in characteristic zero

The right \(W\)-action on \(G/T\) is free: \(g\dot wT=gT\) implies \(\dot w\in T\). We use here the explicit topological prerequisite that its semialgebraic quotient has a finite triangulation compatible with a frontier filtration. Each open cell is a real ball; its inverse image in the finite covering is \(|W|\) balls permuted regularly. Choose the orientations of the lifted balls by deck transport from one lift. Their compact cohomology is one regular \(\mathbb Q[W]\)-module in the cell's degree.

In an equivariant long exact cohomology sequence, alternating traces add, since the traces on successive images cancel. Compact localization along the finite cell filtration therefore gives zero Euler trace on \(G/T\) for \(w\ne1\). Compact trace for \(q_T\) identifies its cohomology with flag cohomology shifted by \(2n\); all the flag degrees are even. Hence this Euler trace is the character of total flag cohomology under \(C\). At \(1\) the dimension is the number \(|W|\) of Bruhat cells. It is the regular character. Averaging and the characteristic-zero character criterion identify the representation as regular, so it is faithful as a group-algebra representation. Equation (5.2) makes \(O\) regular as well. Tensoring the free integral modules with \(\mathbb Q\) also proves integral faithfulness. This argument makes no claim of modular faithfulness or of an Euler-character formula for wild étale covers.

### Identify the two sheaf actions on a flag fibre

The regular semisimple Cartan description refines (2.4) to
\[
Y^{\rm rs}=G/T\times\mathfrak t^{\rm reg},\qquad
(gT,h)\longmapsto(\operatorname{Ad}(g)h,gBg^{-1}).
\tag{5.3}
\]
Its inverse uses unique conjugation by the Borel unipotent radical to the Cartan representative, one of the stated Lie inputs. The deck map for \(w\) is \((gT,h)\mapsto(g\dot w^{-1}T,wh)\).

Ordinary restriction \(H^\bullet(Y)\to H^\bullet(Y^{\rm rs})\) sends a flag class \(v\) to \(q_T^*v\otimes1\). It is injective: evaluate at any Cartan point and use the affine-bundle pullback isomorphism. Naturality of restriction identifies the extended deck action on \(H^\bullet(Y)\) with \(O\). Restriction to the zero section identifies that cohomology with \(H^\bullet(\mathcal B)\); proper base change identifies the latter with the zero stalk of the normalized pushforward. These are actual restriction maps, so \(\rho\) acts there by \(O\).

For compact supports choose the trace-one top class \(\eta\in H_c^{2r}(\mathfrak t^{\rm reg},\mathbb Z)\). The external product and open extension give
\[
H_c^a(G/T)\otimes\mathbb Z\eta
\longrightarrow H_c^{a+2r}(Y^{\rm rs})
\longrightarrow H_c^{a+2r}(Y).
\tag{5.4}
\]
After compact traces to \(\mathcal B\), this composite is an isomorphism. To check the map, trivialize over a flag chart. The open fibre \(B/T\times\mathfrak t^{\rm reg}\) maps into the Borel vector space; extension by zero sends its oriented top class to the oriented top class with coefficient \(+1\), by excision. The trace identifications glue and give the identity on the shifted constant flag sheaf, hence in every flag cohomology degree. Normalizer translation fixes \(\eta\) by complex orientation. Naturality of open extension therefore identifies the extended deck action on \(H_c^\bullet(Y)\) with \(C\).

At the zero covector the classical Fourier kernel is the entire vector space. Base change in (4.5) gives
\[
(\mathcal F^{\rm S}\mathsf S_{\mathfrak g})_0
=R\Gamma_c(Y,k)[2D]
=R\Gamma(\mathcal B,k)[2n].
\tag{5.5}
\]
The last map is the rank-\((n+r)\) vector trace. It is exactly the zero restriction of the exchange map (4.4): integrating the flag and vector variables in either order uses the same composed trace, normalized to \(+1\) on each complex vector fibre. Thus the Fourier action is \(uCu^{-1}\) on this stalk, with no freedom to choose a different identification.

For characteristic-zero coefficients, (5.2) proves (4.7) on flag cohomology. The map from sheaf endomorphisms to endomorphisms of this cohomology is injective: composing with (3.2) gives the faithful \(O\)-representation of the group algebra. This proves the equality of sheaf endomorphisms.

### Extend the equality to other classical coefficients

By the integral smallness bounds in §2 and the free top-component calculation in §3, the integral restriction algebra is \(\mathbb Z[W]\). It injects into its rational version. The integral endomorphism \(\phi(w)-\varepsilon(w)\rho(w)\) becomes zero rationally by the preceding proof, so it is zero already over \(\mathbb Z\).

Derived tensor with a field \(k\) preserves all the maps defining these actions. A field, regarded as a \(\mathbb Z\)-module, has a free resolution of length at most one. Pullback commutes with that tensor complex; proper and compact pushforward do so by projection, or by bounded c-soft models and direct sums. The closed units, composition maps and orientation traces retain their integral normalization on these models. Both constant pushforward complexes become their \(k\)-coefficient versions. On the regular semisimple open the reduced map is the deck action; uniqueness of intermediate extension identifies its global extension. The half-space trace reduces to the specific exchange (4.4). Thus (4.7) holds over every classical coefficient field, including characteristic two, without testing modular sheaf maps on fibre cohomology.

## 6. Transport the compact action to finite characteristic

The arithmetic comparison needs more than identical root systems. We must transport the specified compact action, retain its trace normalization, and only then recover the ordinary action. The providers used for this are Pinnings and the classification of split reductive groups, Automorphisms, forms and parabolic subgroups, and the proper-support, cup-product and point-orientation parts of Comparison with singular cohomology. Their own stated prerequisites remain part of the proof obligation.

There is a precise scope for the curve comparison at the base of the latter provider's dimension induction. Serre's comparison theorems and Chow's theorem, §§1–5, supplies projective GAGA relative to its analytic foundations. Algebraizing a coherent analytic line bundle and descending rank-one local freeness by faithful flatness gives the line-bundle comparison; full faithfulness and tensor compatibility give the Picard comparison. Comparison with the topological fundamental group, §§1–3, puts an analytic structure on a finite cover and algebraizes its coherent algebra. Multiplication and the unit algebraize by full faithfulness; faithful flatness descends finite local freeness and the vanishing of relative differentials, hence étaleness. The same argument applies to algebra maps and group actions. On a smooth projective curve these steps require projective GAGA, not the stronger proper-scheme assertion. In the later induction, algebraic finite local systems are trivialized by algebraic finite étale covers; a general finite-type Riemann-existence theorem and a resolution-of-singularities comparison are not used here.

### Affine bundles, with both pushforwards specified

Start with \(A_m=\mathbb Z/\ell^m\), \(\ell\ne p\). For an affine-space bundle \(q\) of rank \(d\) over an algebraically closed field of characteristic different from \(\ell\), we need
\[
Rq_*A_m=A_m,\qquad Rq_!A_m=A_m(-d)[-2d].
\tag{6.1}
\]
For the ordinary assertion, compactify an affine line to \(g:\mathbb P^1_S\to S\). The unit and \(c_1(\mathcal O(1))\) identify \(Rg_*A_m=A_m\oplus A_m(-1)[-2]\), as proper base change checks on each fibre. The support triangle for infinity, using the smooth-pair purity of Lesson 1, has Gysin map equal to the identity on the second summand: the infinity point has degree one. Its cone is the first summand, proving the affine-line unit isomorphism. Products give affine space; the canonical unit glues it over bundle charts. The compact assertion is the normalized affine-space trace. These apply to \(q_T:G/T\to\mathcal B\), whose fibre \(B/T\) is affine \(n\)-space in ordered root coordinates, and to \(Y\to\mathcal B\). They define \(O_{A_m}\) and \(C_{A_m}\) with §5's right-translation convention.

### Use a proper family to compare the actions

A pinning gives a split integral group with compatible torus, Borel and normalizer representatives. Over \(S=\operatorname{Spec}\mathbb Z[1/\ell]\) its flag family \(a:\mathcal B_S\to S\) is smooth projective of relative dimension \(n\). Put \(h:(G/T)_S\to S\). There is a specified relative compact-trace isomorphism
\[
Rh_!A_m=Ra_*A_m(-n)[-2n].
\tag{6.2}
\]
One can construct this without absolute purity over a mixed-characteristic trait. On an affine-line chart use the open–closed triangle for \(\mathbb A^1\subset\mathbb P^1\). Restriction to infinity is the identity on the unit summand of the projective-line formula and zero on its Chern-class summand, because \(\mathcal O(1)\) restricts trivially to the section. The triangle gives \(Rq_!A_m=A_m(-1)[-2]\). Iterate and glue. Changes of affine-space frame preserve the point-normalized trace on every geometric fibre, so proper-support base change verifies agreement of these trace maps on overlaps. This proves (6.2) compatibly with base change and coefficient reduction.

Right normalizer translation is defined over \(S\) and acts on \(Rh_!A_m\). Transfer that action through (6.2) to the proper complex \(Ra_*A_m\). Its fibre is precisely \(C_{A_m}\). Naturality of proper base change preserves the action, and proper smooth specialization is invertible by Smooth base change and local acyclicity, Corollary 11.3. A strict henselian trait above \(p\) compares the positive-characteristic flag to a geometric characteristic-zero flag. Since the generic group is defined over \(\mathbb Q\), geometric proper base change compares this with the complex flag through \(\overline{\mathbb Q}\).

Over \(\mathbb C\), proper-support comparison for \(G/T\), proper comparison for the flag, and the normalized trace commute with (6.2). Thus the transported action is the classical \(C_{A_m}\) itself. The maps preserve cup products, the flag trace and reduction \(A_{m+1}\to A_m\). Classical flag cohomology is free and concentrated in even degrees; the compared \(A_m\)-modules have perfect cup pairing and degree-one point class at the top.

Only compact cohomology of \(G/T\) has been transported. Recover the ordinary action on each fibre from its mixed pairing with \(C_{A_m}\): projection makes the pairing equivariant, and translation fixes the top compact trace. Its perfection determines \(O_{A_m}\) uniquely. Transporting (5.2) therefore gives
\[
uC_{A_m}(w)=\varepsilon(w)O_{A_m}(w)u
\tag{6.3}
\]
even when \(\ell\mid|W|\). This avoids any claim of smooth proper specialization for a nonproper ordinary direct image.

The coefficient limit here is legitimate on the proper flag complex. The classical cellular model is bounded and finite free, with surjective maps on its coefficient quotients. In cohomology the towers have stabilizing images, so their first derived limits vanish. It follows that the \(\mathbb Z_\ell\)-cohomology is integral classical flag cohomology tensored with \(\mathbb Z_\ell\), with the compatible limiting actions. Flat extension to a finite coefficient DVR \(\mathcal O\), followed by passage to its fraction field \(K\), preserves (6.3). The \(O_K\)-representation is faithful because it is scalar extension of the characteristic-zero regular representation in §5. This calculation on a proper flag does not establish the general theory of adic pushforwards.

### Identify Fourier and restriction after this transport

The Cartan isomorphism (5.3) holds under the arithmetic Lie hypotheses. The ordinary units of (6.1) make \(H^\bullet(Y,A_m)\to H^\bullet(Y^{\rm rs},A_m)\) injective: restrict to one Cartan point and then use \(q_T^*\). The zero section identifies the source with flag cohomology. Naturality of restriction and proper base change therefore identify the sheaf action \(\rho\) at zero with \(O_{A_m}\).

For compact supports take the trace-one element
\(\eta\in H_c^{2r}(\mathfrak t^{\rm reg},A_m(r))\).
This top group is \(A_m\), since the Cartan open is connected and smooth; point normalization makes its Weyl action trivial. In the arithmetic version of (5.4), extension by zero from the open fibre \(B/T\times\mathfrak t^{\rm reg}\) into the Borel vector space preserves a point-normalized top class. Its coefficient is \(+1\). Relative trace and proper-support base change glue that calculation to the identity on the shifted constant flag sheaf. Thus the global deck action on \(H_c^\bullet(Y,A_m)\) is \(C_{A_m}\). Units, open extensions and traces commute with the same coefficient limits.

At the zero covector the character kernel has its canonical trivialization. The exchange (4.5) consequently has zero-stalk map
\[
(\mathcal F_\psi\mathsf S_{\mathfrak g})_0
=R\Gamma_c(Y,K)[2D]
=R\Gamma(\mathcal B,K)[2n](-n-r).
\tag{6.4}
\]
This is exactly the rank-\((n+r)\) trace used in the subbundle formula, by composition of compact integrations. The twist has trivial Weyl action. Hence \(\phi_K=uC_Ku^{-1}\) there. Equation (6.3), the restriction algebra (3.2), and faithfulness of \(O_K\) prove \(\phi_K(w)=\varepsilon(w)\rho_K(w)\) as sheaf maps.

Finally choose \(\mathcal O\) to contain the needed primitive \(p\)-th root of unity; a finite unramified extension of \(\mathbb Z_\ell\) suffices. Sections 2–3 give the injective coefficient map
\[
\operatorname{End}(\mathsf S_{\mathcal N,\mathcal O})
=\mathcal O[W]\hookrightarrow K[W].
\tag{6.5}
\]
The character projector uses division by \(p\), a unit in \(\mathcal O\). Thus (4.1)–(4.5) and their trace maps exist over \(\mathcal O\). The difference of the two sides of (4.7) is an integral endomorphism zero over \(K\); (6.5) makes it zero integrally.

Derived reduction to the residue field uses its two-term finite free DVR resolution. Pullbacks and closed units commute with this resolution, and projection proves the compatibility for proper and compact pushforward. The character projector reduces because \(p\) is a unit; the trace keeps its normalization. The reduced action is the deck action on the regular semisimple open, so uniqueness of its intermediate extension identifies its global extension. This proves (4.7) over the residue field and, by flat extension, over every larger finite coefficient field defining the character. Extension from a finite fraction field also gives the \(\overline{\mathbb Q}_\ell\) statement. These integral and rational adic arguments retain the general operation foundations of Lesson 1 as prerequisites.

## 7. Representation labels and the change of coefficients

Return first to characteristic-zero coefficients and the concrete fibres of §1. For \(SL_2\), the semismall calculation in Lesson 9, with the finite-quotient IC computation of Lesson 8, gives
\[
\mathsf S_{\mathcal N}
=\Lambda_{\mathcal N}[2]\otimes\mathbf1
\ \oplus\ \Lambda_{\{0\}}(-1)\otimes\operatorname{sgn}.
\tag{7.1}
\]
Indeed \(\operatorname{IC}_{\mathcal N}=\Lambda_{\mathcal N}[2]\), the full-support term is trivial by §3, and the restriction algebra forces the other simple term to receive the other irreducible \(S_2\)-representation. At zero, \(H^0(\mathbb P^1)\) is trivial and \(H^2(\mathbb P^1)=\Lambda(-1)\otimes\operatorname{sgn}\). This action cannot be induced by algebraic automorphisms of \(\mathbb P^1\), which all preserve its top class.

The corresponding global decomposition is
\[
\mathsf S_{\mathfrak{sl}_2}
=\Lambda_{\mathfrak{sl}_2}[3]\oplus
\operatorname{IC}_{\mathfrak{sl}_2}(L_{\rm sgn}).
\tag{7.2}
\]
On the regular semisimple open its two eigenlines form the regular representation. At a nonzero nilpotent its only stalk group has degree \(-3\). At zero its stalk groups have degrees \(-3,-1\), with twists \(0,-1\), by the projective-line fibre. The constant summand accounts for degree \(-3\); the sign IC vanishes on the nonzero nilpotent orbit and contributes only degree \(-1\) at zero. Applying \([-1]\) gives degrees \(-2,0\), confirming (7.1). The opposite shift would give \(-4,-2\).

For \(SL_3\), the regular and zero orbits have dimensions \(6,0\). For the subregular matrix in §1 the invertible commuting matrices have form
\[
\begin{pmatrix}a&b&c\\0&a&0\\0&d&e\end{pmatrix},\qquad a^2e\ne0.
\tag{7.3}
\]
The determinant-one condition gives \(e=a^{-2}\). This centralizer is connected of dimension four, so its orbit has dimension \(8-4=4\), and its equivariant component local systems are trivial. The zero centralizer is connected too; the regular orbit's point fibre already supplies a constant top local system, independently of its centralizer's component group.

The fibre dimensions \(0,1,3\) satisfy \(s+2\dim\mathcal B_x=6\) on all three orbits. Their top-cohomology multiplicities have ranks \(1,2,1\), by §1. Section 3 identifies them with distinct irreducible \(S_3\)-representations: the regular orbit receives the trivial one, the zero orbit the other one-dimensional representation, and the subregular orbit the standard two-dimensional representation. Thus
\[
\mathsf S_{\mathcal N}
=\operatorname{IC}_{\mathcal N}\otimes\mathbf1
\oplus\operatorname{IC}_{\overline{\mathcal O}_{(2,1)}}(\Lambda)
\otimes V_{\rm std}(-1)
\oplus\Lambda_{\{0\}}\otimes\operatorname{sgn}(-3).
\tag{7.4}
\]
The standard representation is the three-coordinate permutation representation with its constant line removed. Subtracting the trivial character from \(3,1,0\) gives its character \(2,0,-1\) on the identity, transpositions and three-cycles. In the Fourier normalization every label in (7.1) and (7.4) is tensored with sign.

### What fails in modular coefficients

The small-map description, minus-rank shift, and restriction endomorphism algebra do not divide by \(|W|\). The semisimple decomposition does. Over a field \(k\), the regular \(k[W]\)-module is semisimple precisely when \(\operatorname{char}k\nmid|W|\). Averaging proves sufficiency. Conversely, a splitting of its augmentation to the trivial module would provide an invariant vector of augmentation \(1\). Every invariant vector is a scalar multiple of \(\sum_{w\in W}w\), whose augmentation is \(|W|\). When that number vanishes in \(k\), no splitting exists. Since intermediate extension is additive, fully faithful and preserves simplicity of irreducible local systems, the global IC sheaf of this nonsemisimple regular system is nonsemisimple as well.

For the complex \(SL_2\) nilpotent resolution and coefficient characteristic two, the exceptional intersection form is \((-2)\). Lesson 9's criterion makes its pushforward indecomposable, with no point summand. Nevertheless (3.6) still gives
\[
\operatorname{End}(\mathsf S_{\mathcal N,k})
=k[S_2]=k[\epsilon]/(\epsilon^2),\qquad \epsilon=w-1.
\tag{7.5}
\]
This algebra has no nontrivial idempotents, consistently with indecomposability. Its nonzero element \(\epsilon\) acts as zero on both one-dimensional cohomology groups of the zero fibre: a one-dimensional \(S_2\)-representation in characteristic two is trivial. Thus that fibre's individual cohomology groups do not detect all sheaf maps. Equation (4.7) still holds, with sign now trivial, by integral reduction; characteristic-zero faithfulness was used before reduction. General modular and generalized Springer correspondences require their own constructions and are not proved by (7.5).

## 8. Exercises with solutions

### Exercise 1 — the cotangent resolution

Construct the rank-one nilpotent resolution from a line in a two-dimensional vector space. Identify its bundle, its map to the cone, and its properness.

**Solution.** Let \(L\subset V\) be a line. The compatible endomorphisms factor as \(V\to V/L\to L\to V\), so their vector space is \(\operatorname{Hom}(V/L,L)\). The tangent space to the line variety at \(L\) is \(\operatorname{Hom}(L,V/L)\), and composition followed by trace is a perfect pairing between these two one-dimensional spaces. The incidence bundle is therefore \(T^*\mathbb P(V)\). Its line-bundle description is \(\operatorname{Hom}(\mathcal O(1),\mathcal O(-1))=\mathcal O(-2)\). Composition produces a traceless square-zero matrix, hence a point of \(z^2=ab\). Conversely every incident pair in (1.1) factors in this way. The conditions defining the pair are closed in \(\mathcal N\times\mathbb P(V)\), so projection is projective. The total space is smooth, and the unique line \(\operatorname{im}x\) gives its inverse over the nonzero cone. These facts prove it is the claimed resolution.

### Exercise 2 — rank-one cohomology and its labels

Calculate both nilpotent fibres for \(SL_2\), their cohomology, and their restriction and Fourier representation labels.

**Solution.** A nonzero nilpotent has rank one and square zero, whence \(\operatorname{im}x=\ker x\); its fibre is one line, with \(H^0=\Lambda\). Zero permits all lines, giving \(\mathbb P^1\), whose unit and hyperplane class give \(H^0=\Lambda\) and \(H^2=\Lambda(-1)\), with no other cohomology. The semismall decomposition is the constant IC of the \(A_1\) cone together with \(\Lambda_0(-1)\): the quotient IC calculation and the nonzero intersection form are supplied in Lessons 8–9. Restriction of the global deck-invariant constant summand gives the full-support constituent with trivial label. The restriction algebra is \(\Lambda[S_2]\), so the distinct simple point constituent must have the other irreducible label, sign. Thus the nonzero fibre is trivial and the zero fibre has trivial \(H^0\), sign \(H^2\). Formula (4.7) interchanges these labels for Fourier transport, while retaining their degrees and Tate twists. This answer assumes characteristic-zero coefficients; equation (7.5) explains the characteristic-two failure of the direct sum.

### Exercise 3 — establish the two dimension inequalities

Prove the Grothendieck map is small and the nilpotent map is semismall by using their fibre products. Locate the step where strictness enters.

**Solution.** Relative-position \(w\) flag pairs have dimension \(n+\ell(w)\). Their common Borel algebra has dimension \(r+n-\ell(w)\), so the global fibre-product piece has dimension \(2n+r=D\). Every common Borel algebra contains a Cartan with a nonempty regular semisimple open. Its intersection with the closed non-regular-semisimple set therefore has dimension at most \(r+n-\ell(w)-1\). The global fibre product over that closed set has dimension at most \(D-1\). For an adapted boundary stratum \(S\) with fibre dimension \(h\), its part has dimension \(\dim S+2h\). Hence \(\dim S+2h<D\); over the regular semisimple open the Cartan description supplies the finite étale torsor. These are the smallness conditions. For nilpotence replace the common Borel algebra by the common nilradical, of dimension \(n-\ell(w)\). Each resulting piece has dimension \(2n\), the dimension of the nilpotent source. This proves the non-strict semismall inequalities. There is no corresponding dimension loss on every nilpotent boundary stratum; the exceptional fibres of §1 realize equality.

### Exercise 4 — extend maps and compute the algebra

Show directly that degree-zero maps of an intermediate extension are determined by their open restriction. Apply this to the regular system of a connected \(W\)-torsor, including the multiplication convention.

**Solution.** Given a map of open local systems, perverse extension by zero and perverse direct image produce a commutative square. Taking the images of the horizontal natural maps defines a map of their intermediate extensions. If a map of those images vanishes on the open, its image in the perverse heart is boundary-supported. The target intermediate extension has no such nonzero subobject, so the map is zero. This proves both existence and uniqueness.

For the connected torsor, monodromy is the full left regular group on the basis \(\{e_a:a\in W\}\). If a commuting endomorphism sends \(e_1\) to \(\sum_b c_b e_b\), it must send \(e_a\) to \(\sum_b c_b e_{ab}\); conversely that formula commutes with every left translation. Thus the centralizer has dimension \(|W|\). The operators \(R_w(e_a)=e_{aw^{-1}}\) are independent and satisfy \(R_wR_v(e_a)=e_{av^{-1}w^{-1}}=R_{wv}(e_a)\). They form its basis and identify its algebra with \(\Lambda[W]\). Full faithfulness gives the same algebra on the global IC. This argument computes degree-zero endomorphisms, not all derived Ext groups.

### Exercise 5 — the subregular fibre and its character

For \(xe_2=e_1\), \(xe_1=xe_3=0\) in \(\mathfrak{sl}_3\), describe every compatible flag and calculate the character on its top cohomology. Exhibit matrices for the adjacent transpositions in a representation basis.

**Solution.** Put \(I=\operatorname{im}x=\langle e_1\rangle\) and \(K=\ker x=\langle e_1,e_3\rangle\). The flag conditions give \(L\subset K\), \(I\subset H\), and \(xH\subset L\). With \(H=K\), any line of \(K\) works, a projective line. With \(H\ne K\), its image is \(I\), forcing \(L=I\); the planes through \(I\) form another projective line, including \(K\). Thus the two families meet at exactly \((I,K)\). In the normalization sequence (1.6) the degree-zero map is \((u,v)\mapsto u-v\), which is onto. Its kernel is the diagonal line, and there is no degree-one cohomology on either component. It follows that \(H^0=\Lambda\), \(H^1=0\), and \(H^2=\Lambda(-1)^2\), with no higher groups.

The centralizer computation (7.3) gives a connected group and an orbit of dimension four. Thus its rank-two top local system is constant. The other relevant orbits have top multiplicity ranks one and one; all three obey \(s+2h=6\). The restriction endomorphism theorem and semisimplicity attach distinct irreducible \(S_3\)-modules to these three supports. The regular orbit has the trivial label, so the middle rank-two multiplicity must be \(V_{\rm std}\), and the zero-orbit label is sign. Hence the requested top cohomology is \(V_{\rm std}(-1)\).

The permutation character on three coordinates counts fixed coordinates and is \(3,1,0\) on the three conjugacy classes. Removing its constant line gives \(2,0,-1\). On the root-space basis \(\alpha_1=e_1-e_2,\alpha_2=e_2-e_3\), the adjacent transpositions are
\[
s_1=\begin{pmatrix}-1&1\\0&1\end{pmatrix},
\qquad s_2=\begin{pmatrix}1&0\\1&-1\end{pmatrix}.
\]
Their squares are the identity, and \(s_1s_2=\begin{pmatrix}0&-1\\1&-1\end{pmatrix}\) has characteristic polynomial \(t^2+t+1\) and cube the identity. Its trace is \(-1\); each transposition has trace zero. This specifies the representation, with a chosen algebraic basis rather than a claimed permutation basis of the two curve components.

## Exact prerequisites still required

The general group arguments use the Bruhat and root-intersection geometry, regular semisimple Cartan isomorphisms, adjoint-quotient hypotheses, and regular nilpotent uniqueness specified in §2. The root and normalizer prerequisites include Roots and the Weyl group of a compact Lie group. The classical faithfulness proof also requires finite semialgebraic triangulation of the free Weyl quotient. These are explicit inputs, not consequences of counting the dimensions of the two fibre products.

The degree-zero restriction argument uses smooth orientation, constructible duality, supported pullback and its adjunction compatibility, localization, and the integral top-component bounds. Its arithmetic form requires the corresponding finite and normalized adic operations. The integral costalk bound in §2 supplies a specific step needed for the coefficient argument, without settling this entire foundation. The characteristic-zero correspondence additionally uses the geometric semisimplicity of Lessons 7–9 and their own prerequisites.

Sections 4–6 compute the particular Fourier exchanges, arithmetic inversion, flag comparison and sign equality relative to these operations and the exact comparison providers identified in §6. The classical conic equivalence and its full perversity theorem remain separate SH-02 obligations. The projective GAGA, finite-cover, integral-group and smooth-specialization providers still require their own stated foundational proofs to be checked. The proper flag's coefficient limit does not provide general adic functors.

The assigned broader generalized and modular Springer correspondences remain to be proved in the expanded programme. The modular obstruction and the coefficient-compatible equality of the two actions here are parts of that subject, not substitutes for those correspondences. No arbitrary restriction functor has been asserted to preserve perversity, simplicity or semisimplicity.

## References

- D. Nadler, [*Springer theory via the Hitchin fibration*](https://arxiv.org/abs/0806.4566), §4.1, free author manuscript. With the normalizations used here, proper base change gives \(i^*\mathsf S_{\mathfrak g}[-r]=\mathsf S_{\mathcal N}\). A nondegenerate invariant form must be specified for the Fourier identification.
- D. Juteau, [*Modular Springer correspondence, decomposition matrices and basic sets*](https://arxiv.org/abs/1410.1471), version 1 (2014), free author manuscript, especially §§4.1–4.2 for the Lie hypotheses, restriction normalization and Fourier formulas.
- S. Riche, [*Borel–Moore homology and the Springer correspondence by restriction*](https://riche.perso.math.cnrs.fr/springer-restriction-final.pdf), freely available notes (2013). The degree-zero supported-restriction proof here uses transverse Cartan restriction and top component classes; it does not claim the full equivariant graded theorem of these notes.
- P. N. Achar, A. Henderson, D. Juteau and S. Riche, [*Weyl group actions on the Springer sheaf*](https://arxiv.org/abs/1304.2642v2), version 2 (2013), free author manuscript. The sign comparison here tracks the ordinary and compact flag actions, their trace identifications and coefficient passage.
- M. A. A. de Cataldo and L. Migliorini, [*The decomposition theorem, perverse sheaves and the topology of algebraic maps*](https://arxiv.org/abs/0712.0349), free author manuscript, §4.2.2. The nilpotent restriction requires the rank shift in (3.1).
