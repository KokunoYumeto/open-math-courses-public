# Perfect operations and finite microlocal coefficients

The weak operation theorem preserves the geometry of constructibility. Perfect coefficients require separate arguments. Ordinary inverse image reads the same stalks; exceptional inverse image and internal Hom are controlled by constructible Verdier duality. Compact cohomology then follows by imposing the right support. Fourier–Sato uses radial contraction because its projection is usually nonproper.

The proof combines evaluation biduality, perfect cohomology on compact fibres, and the weak operation theorem. For Fourier transformation we check both zero-section maps and derive the comparison between the negative cut and positive local support. This identifies the actual maps that preserve perfect coefficients, including at the zero covector.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

## Perfect inverse images, tensors and internal Hom

Throughout, \(k\) is commutative of finite global dimension. Manifolds and maps are real analytic, finite dimensional with uniform dimension bounds, Hausdorff and countable at infinity. Complexes are globally bounded. Here \(\mathbb R\)-constructibility includes perfect stalk complexes: each has a bounded finite-projective representative. Finite generation alone does not replace this condition over an arbitrary ring. No Noetherianity, field, global orientation or properness of an arbitrary map is assumed.

**Theorem.** For an analytic map \(f:Y\to X\) and \(F\in D^b_{\mathbb R\text{-}c}(k_X)\), both \(f^{-1}F\) and \(f^!F\) are \(\mathbb R\)-constructible. For \(F,G\in D^b_{\mathbb R\text{-}c}(k_X)\), so are \(G\otimes^LF\) and \(R\mathcal Hom(G,F)\).

**Proof.** The weak operation theorem gives bounded weak constructibility of the inverse images and tensor/internal-Hom outputs. Ordinary inverse image has stalk \((f^{-1}F)_y=F_{f(y)}\), so it preserves perfection.

For exceptional inverse image use the actual constructible evaluation and the normalized exceptional-duality identity:

\[
f^!F\simeq f^!D_XD_XF
\simeq D_Y(f^{-1}D_XF).
\tag{1}
\]

The second isomorphism follows by applying
\(f^!R\mathcal Hom(A,\omega_X)\simeq
R\mathcal Hom(f^{-1}A,f^!\omega_X)\)
to \(A=D_XF\), with \(f^!\omega_X=\omega_Y\).
It is the exceptional internal-Hom comparison (EX.26), constructed from evaluation and adjunction and valid for bounded \(A\). The objects \(D_XF\), \(f^{-1}D_XF\), and their Verdier dual on \(Y\) are constructible by constructible duality and ordinary inverse image. This proves the exceptional assertion, without replacing \(f^!\) by a fixed shift of \(f^{-1}\).

Tensor stalks are \(G_x\otimes_k^LF_x\). Bounded finite-projective representatives for these two perfect complexes have a finite total tensor complex of finite-projective terms. Every output stalk is therefore perfect.

For internal Hom substitute the actual bidual evaluation for its target and curry:

\[
\begin{aligned}
R\mathcal Hom(G,F)
&\simeq R\mathcal Hom(G,R\mathcal Hom(D_XF,\omega_X))\\
&\simeq R\mathcal Hom(D_XF\otimes^LG,\omega_X)\\
&=D_X(D_XF\otimes^LG).
\end{aligned}
\tag{2}
\]

Perfect tensor closure and constructible duality prove the result. These are natural evaluation comparisons with their Koszul tensor symmetry. They do not identify an arbitrary internal-Hom stalk with Hom of the two ordinary stalks. \(\square\)

## Compact and relatively compact cohomology

If \(Z\) is locally closed and subanalytic, \(k_Z\) is constructible: a compatible stratification has constant stalk \(k\) on its included pieces and zero elsewhere, and both coefficient complexes are perfect. Consequently the theorem applies to the cutoffs \(F\otimes k_Z\) and \(R\mathcal Hom(k_Z,F)\).

**Theorem.** For constructible \(F\):

1. If \(K\subset X\) is compact and subanalytic, both \(R\Gamma(K;F|_K)\) and \(R\Gamma_K(X;F)\) are perfect.
2. If \(\Omega\subset X\) is relatively compact, open and subanalytic, both \(R\Gamma(\Omega;F|_\Omega)\) and \(R\Gamma_c(\Omega;F|_\Omega)\) are perfect.

**Proof.** Finite triangulation and derived Čech descent prove perfection of ordinary compact-set cohomology. For supported cohomology set

\[
H_K=R\Gamma_KF=R\mathcal Hom(k_K,F).
\tag{3}
\]

The theorem makes \(H_K\) constructible; its closed support is contained in \(K\). The map to a point is thus proper on its support. Perfect proper direct image gives
\(R\Gamma_K(X;F)=R\Gamma(X;H_K)\) perfect. The ordinary restriction to \(K\) and the complex of sections supported on \(K\) are different constructions.

For the open inclusion \(j:\Omega\hookrightarrow X\), use the two actual identities

\[
H_!=j_!j^{-1}F=k_\Omega\otimes^LF,
\qquad
H_*=Rj_*j^{-1}F\simeq R\mathcal Hom(k_\Omega,F).
\tag{4}
\]

For the second, open internal-Hom adjunction gives
\(R\mathcal Hom(j_!k,F)=Rj_*R\mathcal Hom(k,j^{-1}F)\).
The inner Hom is \(j^{-1}F\); thus the formula uses the actual adjunction map. Both objects are constructible by tensor/Hom closure, and their closed supports lie in the compact set \(\overline\Omega\). Their maps to a point satisfy support properness. Accordingly

\[
R\Gamma(X;H_*)\simeq R\Gamma(\Omega;F|_\Omega),
\qquad
R\Gamma(X;H_!)\simeq R\Gamma_c(\Omega;F|_\Omega)
\tag{5}
\]

are perfect. In the second equality ordinary ambient sections equal compact ambient sections because the coefficient support is compact; open-extension composition then gives compact sections on \(\Omega\). The open set itself need not be compact, and its inclusion need not be proper. \(\square\)

## Fourier perfection by the zero section

Let \(\tau:E\to Z\) be a real analytic vector bundle of fixed finite rank, with dual \(E^*\). Let \(F\) be bounded, \(\mathbb R\)-constructible and conic under positive fibre dilation, including its zero-section behavior. Put

\[
W=E\times_ZE^*,\quad p:W\to E,\quad q:W\to E^*,
\quad i:E^*\to W,\quad i(\eta)=(0,\eta),
\]
\[
N=\{\langle v,\eta\rangle\leq0\},
\qquad C=\{\langle v,\eta\rangle\geq0\}.
\tag{6}
\]

Our Fourier convention is the negative-pairing proper-support formula

\[
F^\wedge=Rq_!L_N,
\quad L=p^{-1}F,
\quad L_N=L\otimes k_N.
\tag{7}
\]

The object \(L_N\) is constructible by inverse image and tensor. It is conic in the first vector coordinate over \(E^*\): first-coordinate dilation pulls back the conic transport of \(F\), and preserves the negative inequality. Conic transport through tensor and inverse image gives this coherent transport. The conicity includes the first-coordinate zero section.

The proper-support conic contraction theorem supplies the actual isomorphism

\[
i^!L_N\simeq Rq_!i_*i^!L_N
\longrightarrow Rq_!L_N.
\tag{8}
\]

The arrow is the closed zero-section counit \(i_*i^!L_N\to L_N\), after applying \(Rq_!\); its source is identified using \(qi=\operatorname{id}_{E^*}\). To see why this particular map is invertible, work over a trivializing open \(V\subset E^*\). Write \(r=\operatorname{rank}E\), \(Y_V=V\times\mathbb R^r\), \(S_V=V\times\{0\}\), and \(B_{V,R}=V\times\overline B_R\). On the punctured bundle, restriction to the exterior of \(B_{V,R}\) induces an isomorphism on sections of any conic complex: the dilation parameter fibre at a nonzero vector \(v\) is \((0,|v|/R)\), a nonempty interval. This is radial restriction along interval fibres.

Compare the localization triangles for support in \(S_V\) and in \(B_{V,R}\). The map on unrestricted sections is the identity, and the map on their complements is the restriction just proved invertible. The resulting inclusion-of-supports map
\(R\Gamma_{S_V}(Y_V;L_N)\to R\Gamma_{B_{V,R}}(Y_V;L_N)\) is therefore an isomorphism.

These disk supports are cofinal among proper supports after passage to a base stalk. Indeed, a closed support proper over \(V\) becomes compact over the compact closure of a smaller base neighborhood. Its fibre norm is bounded there, so it lies in one of the displayed disks after shrinking. Taking the compatible support colimits thus proves that the induced map \(i^!L_N\to Rq_!L_N\) is an isomorphism. The construction is precisely (8), since its maps are inclusion of zero-section support into proper support. No properness of \(q\) on the whole coefficient support is used. Perfect exceptional inverse image makes its source constructible, proving perfection of \(F^\wedge\).

The positive local-support presentation gives a second proof using ordinary inverse image at the zero section. Set

\[
H_C=R\Gamma_C L=R\mathcal Hom(k_C,L).
\tag{9}
\]

It is constructible by (2). Both \(k_C\) and \(L\) are conic in the first coordinate, and the first internal-Hom input \(k_C\) is bounded. Thus the conic internal-Hom comparison makes \(H_C\) conic. The negative-cut/positive-support comparison proved below, followed by ordinary conic contraction, gives

\[
F^\wedge\simeq Rq_*H_C
\xrightarrow{\sim}i^{-1}H_C.
\tag{10}
\]

The last map is the restriction to \(i\) of the projection counit \(q^{-1}Rq_*H_C\to H_C\). In a trivialization, restriction from \(V\times\mathbb R^r\) to \(V\times B_\epsilon\) is an isomorphism on conic sections: the dilation parameter fibre is \((|v|/\epsilon,\infty)\) at \(v\ne0\), and all of \(\mathbb R_{>0}\) at \(v=0\). The same radial restriction theorem applies. These actual restrictions commute when \(V\) and \(\epsilon\) shrink, and the products form a neighborhood basis of the zero vector. Exact filtered stalk colimits identify the displayed counit with an isomorphism. Ordinary inverse image preserves perfect stalks, so (10) proves the claim as well.

We now construct the first comparison in (10), with every arrow in its direction. Put \(O=W\setminus N=\{\langle v,\eta\rangle>0\}\) and \(J=(H_C)_N\). The closure of \(O\) lies in \(C\), so \(R\Gamma_C(L_O)\simeq L_O\); on \(O\), \(H_C\) is just \(L\). Apply \(R\Gamma_C\) to the localization triangle \(L_O\to L\to L_N\to\), and compare with the localization triangle \((H_C)_O\to H_C\to(H_C)_N\to\). Their first two objects and maps agree. The resulting natural identification is
\(R\Gamma_C(L_N)\simeq J\).

The object \(J\) is supported on \(i(E^*)\). To check this, fix \(v\ne0\) and use \(t=\langle v,\eta\rangle\) as one dual-fibre coordinate, keeping \(v\) and the remaining coordinates as parameters. Then \(L\) is pulled back from those parameters. The local-support triangle for \(t\geq0\) compares its sections on an interval with sections on the negative half-interval. At \(t=0\) this restriction is the identity on the pulled-back coefficient complex, by interval descent; at \(t<0\) the local-support object is zero. Hence \(H_C\) restricts to zero on \(N\) near every nonzero \(v\). This proves the asserted support, including the boundary case \(\langle v,\eta\rangle=0\).

The required chain is

\[
Rq_!L_N
\xleftarrow{\sim}Rq_!R\Gamma_C(L_N)
\xrightarrow{\sim}Rq_!J
\xrightarrow{\sim}Rq_*J
\xleftarrow{\sim}Rq_*H_C.
\]

The first arrow forgets local support. Both its inputs are conic, so the natural proper-support contractions identify its image with \(i^!R\Gamma_C(L_N)\to i^!L_N\), an isomorphism because \(i(E^*)\subset C\). The second arrow is the preceding localization identification. For the third, \(J\) is the closed extension of its zero-section restriction, and \(q\) is the identity on that section; forgetting proper support is therefore invertible on \(J\). The last arrow is induced by the restriction \(H_C\to J\). Under the natural ordinary contractions it is \(i^{-1}H_C\to i^{-1}J\), an isomorphism because \(i(E^*)\subset N\). Invert the indicated arrows to obtain the first comparison in (10). This is the negative-cut/positive-support Fourier comparison (FS4–FS6), now with its localization, support and counit maps explicit. Every operation is natural in \(F\), so the comparison glues over the base.

Neither (8) nor the last map of (10) inserts a further shift or orientation factor. They use different zero-section operations, \(i^!\) and \(i^{-1}\), on different kernels. Their eventual costalk or stalk computations contain whatever shifts the coefficients require. For rank zero all bundle maps are identities and the Fourier transform is the identity.

## Specialization and microlocal Hom

Let \(M\) be an analytic embedded submanifold, closed in the ambient neighborhood under discussion. In its normal deformation write

\[
p:\widetilde X_M\to X,\quad
\Omega=\{t>0\},\quad j:\Omega\hookrightarrow\widetilde X_M,
\quad s:T_MX\hookrightarrow\widetilde X_M.
\tag{11}
\]

In adapted coordinates \(p(v,z,t)=(tv,z)\), so \(p\) is analytic on the whole deformation, including \(t=0\). If \(F\) is constructible, so is \(p^{-1}F\). Formula (4) and internal-Hom perfection give

\[
Rj_*j^{-1}p^{-1}F
\simeq R\mathcal Hom(k_\Omega,p^{-1}F)
\quad\text{constructible}.
\tag{12}
\]

The positive chamber is subanalytic; no properness of its open inclusion is asserted. Ordinary inverse image by \(s\) proves

\[
\nu_MF=s^{-1}Rj_*j^{-1}p^{-1}F
\in D^b_{\mathbb R\text{-}c}(k_{T_MX}).
\tag{13}
\]

The positive deformation and its scaling action give conicity of \(\nu_MF\); the bounded open-extension and inverse-image operations in (12)–(13) give its boundedness. Fourier perfection now gives
\(\mu_MF=(\nu_MF)^\wedge\in D^b_{\mathbb R\text{-}c}(k_{T_M^*X})\), using the negative-transform definition (MIC1).
For a locally closed \(M\), restriction to neighborhoods where it is closed gives the same statement, since the construction and its maps are local.

Finally, for constructible \(F,G\), the exact defining diagonal kernel

\[
K_{G,F}=R\mathcal Hom(q_2^{-1}G,q_1^!F)
\tag{14}
\]

on \(X\times X\) is constructible by inverse, exceptional inverse and internal Hom. Specialization and Fourier perfection prove

\[
\mu\operatorname{hom}(G,F)=\mu_{\Delta_X}K_{G,F}
\in D^b_{\mathbb R\text{-}c}(k_{T^*X}).
\tag{15}
\]

The identification is \((x,x;\xi,-\xi)\mapsto(x;\xi)\), and the order of inputs is exactly that in (14). The exceptional projection retains its orientation and dimension shift. The bounded-Hom theorem (M44), the bounded operations in (12)–(13), and the fixed-rank Fourier cohomological bound give global boundedness; pointwise perfection alone would not supply a uniform degree bound. This proves perfect coefficient stability. Natural duality comparisons must also retain the maps, antipodes and relative orientation factors.

## Examples and exercises with solutions

### A critical inverse has different ordinary and exceptional stalks

*Difficulty: Intermediate.*

Let \(f:\mathbb R\to\mathbb R\), \(f(x)=x^2\), and let \(F=k_{(0,\infty)}\) on the target. Compute \(f^{-1}F\) and \(f^!F\), using the increasing orientations on both lines.

**Solution.** The preimage of the positive half-line is \(\mathbb R\setminus\{0\}\), so ordinary inverse image is its open extension \(k_{\mathbb R\setminus\{0\}}\). In particular its stalk at zero vanishes. Constructible duality on the target gives \(D_{\mathbb R}F=k_{[0,\infty)}[1]\). The ordinary inverse image of this closed-half-line coefficient is \(k_{\mathbb R}[1]\), since \(x^2\geq0\) everywhere. Formula (1) consequently gives
\(f^!F=D_{\mathbb R}(k_{\mathbb R}[1])=k_{\mathbb R}\).
Its stalk at zero is \(k\). Both objects are constructible and perfect. Away from zero the map is locally a diffeomorphism; the critical point is where the two ordinary stalk descriptions differ. As a local consistency check, the costalk at zero of the latter object is \(k[-1]\), equal to the target costalk of the positive open half-line, as exceptional composition requires. The formula used full duality and did not assume a submersion at zero.

### Derived tensor and Hom retain opposite torsion degrees

*Difficulty: Intermediate.*

Over \(\mathbb Z\), put \(A=\mathbb Z/m\), \(B=\mathbb Z/n\), with \(m,n>1\), and \(d=\gcd(m,n)\). Compute \(A\otimes^LB\) and \(R\operatorname{Hom}(A,B)\). Regard them also as point-supported sheaf coefficients.

**Solution.** The two-term finite-free resolution of \(A\) in degrees minus one and zero gives tensor model
\([B\xrightarrow{m}B]\) in those degrees. Multiplication by \(m\) on \(B\) has kernel and cokernel both \(\mathbb Z/d\). Thus tensor has \(\operatorname{Tor}_1(A,B)=\mathbb Z/d\) in degree minus one and \(A\otimes B=\mathbb Z/d\) in degree zero. Applying Hom to the same resolution gives \([B\xrightarrow{\pm m}B]\) in degrees zero and one, where the dual-complex sign does not affect kernel or cokernel. Its cohomology is \(\operatorname{Hom}(A,B)=\mathbb Z/d\) in degree zero and \(\operatorname{Ext}^1(A,B)=\mathbb Z/d\) in degree one.

Both complexes are perfect: use bounded finite-free representatives for both inputs in the tensor case, and dual-tensor finite-projective evaluation in the Hom case. The displayed \(B\)-term models calculate cohomology; perfection follows from the finite-projective models. For sheaves supported at a closed point, tensor and Hom have these coefficient complexes at that point and vanish off it. Replacing the derived tensor or Hom by its degree-zero group would lose one of the two torsion degrees.

### Ordinary compact restriction differs from compact support

*Difficulty: Introductory.*

On \(X=\mathbb R\), take \(F=k_X\), \(K=[0,1]\) and \(\Omega=(0,1)\). Compute all four complexes in the finite-cohomology theorem.

**Solution.** Ordinary restriction to the closed interval gives \(R\Gamma(K;F)=k\) in degree zero. The supported complex on the whole line is the fibre of
\(R\Gamma(\mathbb R;k)=k\to R\Gamma(\mathbb R\setminus K;k)=k^2\).
The map is diagonal, so \(R\Gamma_K(\mathbb R;k)=k[-1]\). Ordinary open-interval sections are \(k\), while its compact sections are \(k[-1]\) in the increasing orientation. All four complexes are perfect. The supported result comes from local support, and the ordinary compact result from restriction; compactness does not identify those two functors.

### A relatively compact annulus has two finite cohomology degrees

*Difficulty: Intermediate.*

For the open annulus \(\Omega=\{x\in\mathbb R^2:1<|x|<2\}\) and constant coefficient \(k\), calculate ordinary and compactly supported cohomology, without assuming a field.

**Solution.** Radial coordinates give \(\Omega\simeq S^1\times(1,2)\). Projection along the contractible open interval gives ordinary coefficient \(k_{S^1}\); the finite vertex-star Čech complex on the circle calculates \(R\Gamma(S^1;k)=k\oplus k[-1]\). Hence ordinary annulus cohomology has \(k\) in degrees zero and one.

For compact sections, the oriented radial interval has coefficient \(k[-1]\) under proper-support projection. The positive radial orientation makes this a constant coefficient complex on \(S^1\). Since the circle is compact, derived proper-support composition gives
\(R\Gamma_c(\Omega;k)=R\Gamma(S^1;k)[-1]=k[-1]\oplus k[-2]\).
This has \(k\) in degrees one and two. The finite circle complex has finite-free terms and an explicit decomposition, so these calculations work over the full ring \(k\). The compact closure \(1\leq|x|\leq2\) is precisely what makes both cutoff objects in (4) have proper support to a point.

### Open and closed rays have distinct Fourier boundaries

*Difficulty: Intermediate.*

In an oriented one-dimensional vector space, compute the negative-pairing transforms of \(k_{[0,\infty)}\) and \(k_{(0,\infty)}\), including their values at the zero covector.

**Solution.** For the closed ray, the coefficient fibre in (7) is
\([0,\infty)\cap\{x\xi\leq0\}\).
If \(\xi>0\) it is \(\{0\}\), with compact cohomology \(k\). If \(\xi\leq0\) it is the entire closed ray, whose compact cohomology vanishes. The latter vanishing follows from its localization pair: the compact-section extension from the open ray to the line is an isomorphism on the oriented degree-one generator. The restriction map to the origin identifies the transform on \(\xi>0\) with the constant \(k\); zero stalks on the complement then give its open extension. Thus
\((k_{[0,\infty)})^\wedge=k_{(0,\infty)}\).

For the open ray, the fibre is empty when \(\xi>0\), and the full open ray when \(\xi\leq0\), giving \(k[-1]\). Over the closed negative covector half-line the incidence space is the product of that half-line and the positive ray; the relative orientation trace identifies the entire proper-support image with its constant coefficient \(k[-1]\). Closed extension gives
\((k_{(0,\infty)})^\wedge=k_{(-\infty,0]}[-1]\).
At the zero covector the first transform is zero and the second is \(k[-1]\). The shift arises from the actual open fibre integration, not from an added shift in (8) or (10). Both outputs are perfect and constructible.

### Specialization preserves a boundary, microlocalization reads its direction

*Difficulty: Advanced.*

In \(X=\mathbb R\), let \(M=\{0\}\) and \(F=k_{[0,\infty)}\). Compute \(\nu_MF\) and \(\mu_MF\) directly from the positive deformation chamber and the ray Fourier calculation.

**Solution.** In deformation coordinates \((v,t)\), \(p(v,t)=tv\). On \(t>0\), the condition \(tv\geq0\) is exactly \(v\geq0\). The coefficient there is the product of the closed positive normal ray with the constant positive parameter interval. Ordinary extension across \(t=0\) has coefficient \(k\) in degree zero from that parameter: a small positive half-interval has ordinary cohomology \(k\) and no higher groups. These restrictions are actual product restriction maps, so central inverse image gives
\(\nu_MF=k_{[0,\infty)}\) on the normal line. Fourier transformation from the preceding solution gives
\(\mu_MF=k_{(0,\infty)}\) on the conormal line, with the positive covector convention in (6)–(7). Its zero-covector stalk is zero, whereas the specialization's zero-vector stalk is \(k\). This agrees with the original boundary costalk being zero and ordinary stalk being \(k\); no shift was inserted by the positive parameter extension.

### A torsion morphism coefficient keeps the exceptional projection shift

*Difficulty: Advanced.*

On the oriented line let \(P=\mathbb Z/m\), \(Q=\mathbb Z/n\), and take their constant sheaves \(P_X,Q_X\). Compute \(\mu\operatorname{hom}(P_X,Q_X)\), including the normal and exceptional shifts.

**Solution.** Put \(A=R\operatorname{Hom}_{\mathbb Z}(P,Q)\), a perfect coefficient complex. Since \(P\) has a bounded finite-free representative, the sheaf Hom of the constant coefficients is their constant derived coefficient Hom. The projection \(q_1:X^2\to X\) has an oriented one-dimensional fibre, so (14) is \(A_{X^2}[1]\). Specialization along the diagonal is the same constant complex \(A[1]\) on its normal line bundle: its positive parameter interval has ordinary coefficient \(k\) in degree zero. The Fourier transform of a constant coefficient on that normal line is its zero-covector extension shifted by \([-1]\). Indeed, the fibre is the whole line at \(\xi=0\), with compact coefficient \(k[-1]\), and a closed half-line at \(\xi\ne0\), with zero compact cohomology; the closed zero-section comparison constructs the extension.

The shifts \([1]\) and \([-1]\) cancel. Thus
\(\mu\operatorname{hom}(P_X,Q_X)=i_*A\), with \(i\) the zero section of \(T^*X\). The earlier torsion calculation gives \(\mathbb Z/\gcd(m,n)\) in degrees zero and one on that section and zero off it. Omitting the exceptional projection shift would move both degrees and misidentify the morphism complex.

## References

Masaki Kashiwara and Pierre Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), supplies the classical statements underlying these constructions:

- Proposition 2.1.1 and Definition 2.1.2 in §2.1, printed pp. 39–40 (PDF pp. 42–43), compare the negative-pairing cutoff with positive-pairing local support and define the Fourier transform. That section states its results without proofs. The localization and contraction argument above proves the precise comparison used in (10), with the current programme's actual counits.
- Remark 8.2.8, printed p. 148 (PDF p. 151), gives the compact perfect-cohomology result. Here finite triangulation and compact-fibre descent supply the perfect complexes used in (3)–(5), while the cutoff objects distinguish ordinary restriction from supported cohomology.
- Propositions 8.3.3–8.3.6, printed pp. 149–150 (PDF pp. 152–153), give constructibility under inverse operations (8.3.3), specialization and microlocalization (8.3.4), conic Fourier transformation (8.3.5), and tensor and internal Hom (8.3.6). The tensor statement assumes finite weak global dimension. The hypotheses in this lesson impose finite global dimension and keep the boundedness and perfect coefficient arguments explicit.

## Two zero-section tests for the same Fourier transform {#readable-source-and-dependency-account}

The negative-cut description represents the transform by the exceptional restriction \(i^!L_N\), using the closed-section counit. The positive-support description represents it by the ordinary restriction \(i^{-1}R\Gamma_C L\), using the projection counit. The localization chain above identifies these two presentations of the same transform. The projection \(q\) is not assumed proper on either full kernel support, and neither contraction adds a degree or a trivialization of an orientation line.

Perfect inverse operations and tensor/internal-Hom closure make the two restricted objects constructible. Compact cohomology uses cutoffs with genuinely proper support. Specialization uses the analytic deformation and positive-chamber open extension, and microlocal Hom uses the exceptional diagonal kernel. These constructions explain why the boundary, orientation and torsion degrees in the examples survive all the operations.
