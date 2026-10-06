# Perfect operations and finite microlocal coefficients

The weak operation theorem preserves the geometry of constructibility. Perfect coefficients require separate arguments. Ordinary inverse image reads the same stalks; exceptional inverse image and internal Hom are controlled by constructible Verdier duality. Compact cohomology then follows by imposing the right support. Fourier–Sato uses radial contraction because its projection is usually nonproper.

Use Constructible costalks and Verdier duality for canonical biduality, Perfect coefficients on compact fibres for proper perfect direct image, and Weak constructibility under sheaf operations for boundedness and the deformation/diagonal definitions. The existing prerequisites supply normalized exceptional adjunction, the two conic zero-section contractions, and the Fourier comparison between the negative cutoff and positive supported kernel. Their individual foundational dependencies remain explicit.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

## Perfect inverse images, tensors and internal Hom

Throughout, \(k\) is commutative of finite global dimension. Manifolds and maps are real analytic, finite dimensional with uniform dimension bounds, Hausdorff and countable at infinity. Complexes are globally bounded. No Noetherianity, field, global orientation or properness of an arbitrary map is assumed.

**Theorem.** For an analytic map \(f:Y\to X\) and \(F\in D^b_{\mathbb R\text{-}c}(k_X)\), both \(f^{-1}F\) and \(f^!F\) are \(\mathbb R\)-constructible. For \(F,G\in D^b_{\mathbb R\text{-}c}(k_X)\), so are \(G\otimes^LF\) and \(R\mathcal Hom(G,F)\).

**Proof.** The weak theorem has already proved bounded weak constructibility of every output. Ordinary inverse image has stalk \((f^{-1}F)_y=F_{f(y)}\), so it preserves perfection.

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
It is the exceptional internal-Hom comparison constructed from evaluation and adjunction; it is valid for bounded \(A\). The objects \(D_XF\), \(f^{-1}D_XF\), and their Verdier dual on \(Y\) are constructible by the preceding lesson and ordinary inverse image. This proves the exceptional assertion, without replacing \(f^!\) by a fixed shift of \(f^{-1}\).

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

**Proof.** Ordinary compact-set cohomology was proved in the compact-fibre lesson by finite triangulation and derived Čech descent. For supported cohomology set

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

The object \(L_N\) is constructible by inverse image and tensor. It is conic in the first vector coordinate over \(E^*\): first-coordinate dilation pulls back the conic transport of \(F\), and preserves the negative inequality. The bounded conic operation theorem gives the coherent tensor transport.

The proper-support conic contraction prerequisite supplies the actual isomorphism

\[
i^!L_N\simeq Rq_!i_*i^!L_N
\longrightarrow Rq_!L_N.
\tag{8}
\]

It is the closed zero-section counit followed by proper-support composition. Its proof compares support on the zero section with support on closed fibre disks, using radial restriction on their complements and the disks' local cofinality among proper supports. Thus it does not assume that \(q\) is proper on \(\operatorname{supp}(L_N)\). Perfect exceptional inverse image makes its source constructible, proving perfection of \(F^\wedge\).

The ordinary-image route is the one used in source 8.4.12. Set

\[
H_C=R\Gamma_C L=R\mathcal Hom(k_C,L).
\tag{9}
\]

It is constructible by (2) and conic in the first coordinate by the bounded conic internal-Hom theorem. The positive supported-kernel comparison and ordinary conic contraction give

\[
F^\wedge\simeq Rq_*H_C
\xrightarrow{\sim}i^{-1}H_C.
\tag{10}
\]

The last map is the restriction of the projection counit to its zero section. Its proof uses compatible radial restrictions from full fibres to small disks and then stalk colimits. Ordinary inverse image preserves perfect stalks, so this also proves the claim.

For clarity, the first comparison in (10) is a specific Fourier theorem, with its positive support and negative cutoff. Its actual construction uses
\(R\Gamma_C(L_N)\simeq(H_C)_N\), then the fact that \((H_C)_N\) is supported on the first-coordinate zero section. This fact is obtained at a nonzero \(v\) by using \(t=\langle v,\eta\rangle\) as a transverse coordinate: local support on \(t\geq0\) restricts to zero on \(t\leq0\) for the coefficient pulled back from the other variables. On the zero section \(q\) is proper. The resulting chain compares \(Rq_!L_N\), \(Rq_!(H_C)_N\), \(Rq_*(H_C)_N\), and \(Rq_*H_C\) using the two contraction maps and support localization. This is the exact existing comparison theorem, whose full proof and map directions are retained as prerequisites.

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

Its boundedness and positive conicity are the previously proved deformation contracts. Fourier perfection now gives
\(\mu_MF=(\nu_MF)^\wedge\in D^b_{\mathbb R\text{-}c}(k_{T_M^*X})\).
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

The identification is \((x,x;\xi,-\xi)\mapsto(x;\xi)\), and the order of inputs is exactly that in (14). The exceptional projection retains its orientation and dimension shift. Boundedness comes from the full bounded-Hom and finite-amplitude specialization/Fourier contracts, rather than a bound inferred separately for each stalk. This proves perfect coefficient stability; the natural comparisons between these objects and their Verdier duals require the further arguments that follow.

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

Kashiwara and Schapira, *Microlocal study of sheaves*, Propositions 8.3.3–8.3.6 supplies the readable inverse-image, specialization, Fourier and tensor/Hom comparison. The source separates weak geometric control from the perfect coefficient condition and requires finite weak global dimension for the tensor statement.
- The conic zero-section contractions are the precise prerequisites used here. Ordinary positive supported Fourier presentation uses ordinary zero-section inverse image; the negative cutoff presentation uses exceptional inverse image. Their maps and the full positive/negative comparison are retained from the existing conic and Fourier lessons.
- Normal deformation, its positive-chamber open-extension formula, and the exceptional diagonal definition of microlocal Hom are the bounded specialization/microlocal prerequisites. Their transitive topology and operation contracts remain separately open.

## Readable source and dependency account

The proof here uses actual constructible biduality to control exceptional inverse image and internal Hom, and finite compact cohomology for the perfect image argument. Fourier perfection uses the appropriate zero-section contraction because the vector-bundle projection is not generally proper. The orientation shift in the exceptional factor and the positive/negative Fourier comparison are retained. The named conic and duality providers, including their map normalizations and unresolved foundations, are not replaced by a citation.

Checked editions: [Kashiwara–Schapira, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf); [Schapira, sheaf lecture notes](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf); [Schapira, microlocal review (2016)](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf). The locators above identify the passages used; these links do not claim that all three works prove every statement or every prerequisite of this lesson. Original programme exposition remains CC0; the human works retain their own rights.
