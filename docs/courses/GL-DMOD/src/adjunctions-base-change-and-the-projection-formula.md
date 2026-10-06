# Adjunctions, base change and the projection formula

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Direct image integrates differential equations along a map. Extraordinary inverse image asks what remains along another map, including the normal directions and their cohomological degrees. Base change says these operations fit together in a cartesian square. The projection formula then follows by putting a graph opposite a diagonal.

The field has characteristic zero. Varieties are smooth and separated; complexes have bounded, quasi-coherent cohomology over the structure sheaf. Write $d_X=\dim X$, and retain the conventions
\[
f^!N=L f_{\mathcal O}^*N[d_X-d_Y],
\qquad
f_*M=R f_{\mathrm{sh},*}
 \bigl(\mathcal D_{Y\leftarrow X}\otimes_{\mathcal D_X}^L M\bigr).
\tag{0.1}
\]
The subscript $\mathrm{sh}$ distinguishes sheaf direct image from differential-operator direct image. Ordinary derived pullback in (0.1) carries the chain-rule action established in Inverse images. The transfer conventions, composition isomorphisms and relative Spencer complex come from Direct images and the relative de Rham complex. We also use the equivalence proved in Kashiwara's equivalence and D-modules on singular spaces.

The symbol $f^*$ introduced in Section 5 denotes the duality-defined functor on holonomic complexes. It must be distinguished from $L f_{\mathcal O}^*$.

## 1. Localization and the supported part

Let $i:Z\hookrightarrow X$ be a smooth closed subvariety of codimension $c$, with open complement $j:U\hookrightarrow X$.

**Lemma 1.1.** There are natural identifications
\[
i^!j_*N=0,\qquad
R\Gamma_Z M\simeq i_*i^!M,
\tag{1.1}
\]
and a distinguished triangle
\[
i_*i^!M\longrightarrow M\longrightarrow j_*j^!M
 \longrightarrow i_*i^!M[1].
\tag{1.2}
\]
Here $R\Gamma_Z$ is algebraic local cohomology of the underlying structure-sheaf complex, with its induced differential-operator action.

**Proof.** Locally choose generators $t_1,\ldots,t_c$ of the ideal of $Z$. The complement is covered by the principal opens $X_{t_a}$. Its direct image is computed by the finite alternating Čech complex of the localizations $M_{t_{a_1}\cdots t_{a_s}}$. On each term at least one $t_a$ is invertible. The Koszul complex computing $L i_{\mathcal O}^*$ is then contractible: exterior multiplication or contraction in that direction, multiplied by $t_a^{-1}$, gives the contracting homotopy. Consequently $i^!j_*N=0$, including higher sheaf direct images.

The augmented localization complex defines the usual triangle
\[
R\Gamma_ZM\longrightarrow M\longrightarrow j_*j^!M.
\tag{1.3}
\]
Its cohomology is quasi-coherent and supported on $Z$. These cohomology modules are locally annihilated by powers of its ideal. Thus Kashiwara's equivalence applies to them. On supported modules $i^!$ is exact and concentrated in degree zero; the bounded cohomology spectral sequence extends the equivalence to the supported derived category. Apply $i^!$ to (1.3). Its last term vanishes, so $i^!R\Gamma_ZM\simeq i^!M$. Recovering the supported object by $i_*$ gives (1.1) and (1.2). All maps arise from the localization augmentation and the canonical Kashiwara evaluation, so the construction glues. $\square$

We will also need the adjunction behind the first arrow.

**Lemma 1.2.** For a smooth closed embedding,
\[
R\operatorname{Hom}_{\mathcal D_X}(i_*A,M)
 \simeq
R\operatorname{Hom}_{\mathcal D_Z}(A,i^!M),
\tag{1.4}
\]
where these are global derived Hom complexes.

**Proof.** The backward transfer is a left $i^{-1}\mathcal D_X$, right $\mathcal D_Z$ bimodule $B$. Closed direct image is $i_{\mathrm{sh},*}(B\otimes_{\mathcal D_Z}A)$, and $B$ is flat on the right. Tensor–Hom adjunction therefore reduces (1.4) to identifying the right adjoint coefficient complex $R\mathcal Hom_{i^{-1}\mathcal D_X}(B,i^{-1}M)$.

In normal coordinates, $B$ is the quotient by the right multiplications $t_a$, with the density factor $\omega_Z\otimes i^*\omega_X^{-1}$. Its Koszul resolution is exact: the order-associated graded calculation is the regular sequence $t_1,\ldots,t_c$ in $\mathcal O_X[\xi]$. Applying Hom gives the cochain Koszul complex of the operators $t_a$ on $M$, in degrees $0,\ldots,c$. The density factor turns this into
\[
L i_{\mathcal O}^*M[-c]=i^!M.
\tag{1.5}
\]
In degree zero on a supported module the intrinsic result is
$\det(\mathcal I/\mathcal I^2)\otimes\operatorname{ann}_{\mathcal I}M$,
as in the preceding lesson. Thus this calculation retains the determinant line, rather than identifying the inverse globally with an untwisted kernel. Derived tensor–Hom adjunction, followed by sheaf cohomology, proves (1.4). $\square$

For example, on the line, $i^!M$ is the two-term complex $M\xrightarrow{x}M$ in degrees $0,1$. It follows that $i^!\mathcal O_{\mathbb A^1}=k[-1]$, whereas $i^!\delta_0=k$. Support and ordinary restriction have different effects on the degree.

## 2. Base change

Consider a cartesian square
\[
\begin{array}{ccc}
X'&\xrightarrow{g'}&X\\
{\scriptstyle f'}\downarrow&&\downarrow{\scriptstyle f}\\
Y'&\xrightarrow{g}&Y .
\end{array}
\tag{2.1}
\]
Assume that all four varieties are smooth. In particular, a singular fiber product has not been silently assigned the smooth transfer formula.

**Theorem 2.1.** There is a natural isomorphism
\[
g^!f_*M\simeq f'_*g'^!M
\tag{2.2}
\]
on bounded quasi-coherent differential-operator complexes. Properness and transversality are not required.

**Proof, product case.** First let $Y'=T\times Y$ and let $g$ be the projection. Set $r=\dim T$. Then $X'=T\times X$, and
\[
g^!N=(\mathcal O_T\boxtimes N)[r],
\qquad
g'^!M=(\mathcal O_T\boxtimes M)[r].
\tag{2.3}
\]
External products commute with direct image in this situation:
\[
(\mathrm{id}_T\times f)_*(A\boxtimes M)
 \simeq A\boxtimes f_*M.
\tag{2.4}
\]
To check this, factor $f$ into its closed graph and a product projection. For the graph, the transfer and its normal derivative basis extend by external product. For the projection, use the relative Spencer complex. Its differentials act in the $X$ directions and commute with the $T$ action. On affine opens in $T$ and $Y$, a finite affine Čech cover in $X$ computes sheaf direct image. Its complex is tensored over the field with the complex representing $A$. Tensor over a field is exact, and the two finite totalizations agree with their Koszul signs. This proves (2.4) for bounded complexes and proves compatibility on overlaps. Applying it to $A=\mathcal O_T$ proves (2.2), with the same shift $[r]$ on both sides.

**Proof, closed case.** Now let $g=i:Y'\hookrightarrow Y$ be closed; then $g'=i':X'\hookrightarrow X$ is closed. Write $j:V=Y\setminus Y'\hookrightarrow Y$ and $j':V'=X\setminus X'\hookrightarrow X$. The restriction of $f$ gives $h:V'\to V$, with $f j'=j h$.

Apply $i^!f_*$ to the localization triangle on $X$. By composition and Lemma 1.1,
\[
i^!f_*j'_*j'^!M
 \simeq i^!j_*h_*j'^!M=0.
\tag{2.5}
\]
It follows that the natural map
$i^!f_*i'_*i'^!M\to i^!f_*M$ is an isomorphism. On its source, composition and Kashiwara give
\[
i^!f_*i'_*i'^!M
 \simeq i^!i_*f'_*i'^!M
 \simeq f'_*i'^!M.
\tag{2.6}
\]
Together these prove (2.2). Notice that the codimensions of $i$ and $i'$ need not agree. Their shifts are already built into (1.5) and the Kashiwara counit.

**Proof, arbitrary map.** Factor $g$ as its closed graph $Y'\hookrightarrow Y'\times Y$, followed by projection to $Y$. The intermediate pullback of $X$ is $Y'\times X$, which is smooth. The final pullback is the given smooth $X'$. Apply the product and closed cases successively, then the composition isomorphisms for inverse and direct image.

The maps in the closed case are the localization map and the Kashiwara counit; in the product case they are the tensor and Čech comparison maps. Refinement of a cover gives the same augmentation. For successive projections the tensor totalization is associative; for successive closed embeddings the Koszul evaluation and Kashiwara counits compose. These observations identify the constructed maps on successive squares and on overlaps. They establish naturality and the usual compatibility of (2.2) with composition. $\square$

This is the algebraic base change theorem stated in Etingof, Proposition 3.1. Miličić's *Lectures on Algebraic Theory of D-Modules*, Chapter IV, §10, proves it for smooth varieties with smooth fiber product by the same reduction to a product projection and a closed embedding. The proof above includes the localization calculation needed for the closed case.

**A nontransverse check.** Take $f=i:\mathrm{pt}\hookrightarrow\mathbb A^1$ and $g=i$ at the same point. The fiber product is a point and both upper maps are identities. Formula (2.2) becomes $i^!i_*k=k$. The delta module has all normal derivatives; the operator $x$ is surjective on it with kernel $k\delta$. Its Koszul complex has only degree-zero cohomology after the shift in $i^!$. Replacing $i^!$ by an unshifted structure-sheaf fiber would give the wrong degree.

**A family check.** For $p:\mathbb A^1_x\times\mathbb A^1_t\to\mathbb A^1_t$,
$p_*\mathcal O=\mathcal O_{\mathbb A^1_t}[1]$. Pulling back extraordinarily along $i:\mathrm{pt}\hookrightarrow\mathbb A^1_t$ gives $k$. On the other side, $i'^!\mathcal O=\mathcal O_{\mathbb A^1_x}[-1]$, and its direct image to a point is again $k$. These two canceled shifts are part of base change.

## 3. The projection formula and its shift

Define
\[
M\otimes^!N=\Delta_X^!(M\boxtimes N).
\tag{3.1}
\]
The derived diagonal Koszul calculation gives
\[
M\otimes^!N
 \simeq (M\otimes_{\mathcal O_X}^L N)[-d_X].
\tag{3.2}
\]
Indeed, on an affine chart the diagonal is resolved by the differences of the two coordinate systems. Tensoring that resolution with the external product is the usual resolution computing the derived tensor product over the coordinate ring. The diagonal has codimension $d_X$, accounting for $[-d_X]$. Its tangent action is the Leibniz action. This description is intrinsic and glues.

**Theorem 3.1.** For $M$ on $X$ and $N$ on $Y$,
\[
f_*(M\otimes^!f^!N)
 \simeq f_*M\otimes^!N.
\tag{3.3}
\]

**Proof.** Put $h=f\times\mathrm{id}_Y:X\times Y\to Y\times Y$. The pullback of the diagonal $\Delta_Y$ along $h$ is the graph $\gamma_f:X\to X\times Y$. Base change and (2.4) identify
\[
\begin{aligned}
f_*\gamma_f^!(M\boxtimes N)
&\simeq \Delta_Y^!h_*(M\boxtimes N)\\
&\simeq \Delta_Y^!(f_*M\boxtimes N).
\end{aligned}
\tag{3.4}
\]
The graph has codimension $d_Y$, so its derived inverse image is
\[
\gamma_f^!(M\boxtimes N)
 \simeq(M\otimes_{\mathcal O_X}^L Lf_{\mathcal O}^*N)[-d_Y]
 \simeq M\otimes^!f^!N.
\tag{3.5}
\]
The last equality uses $[d_X-d_Y]$ from $f^!$ and $[-d_X]$ from $\otimes^!$. Substitution gives (3.3). $\square$

Equivalently, canceling $[-d_Y]$ on both sides gives
\[
f_*(M\otimes_{\mathcal O_X}^L Lf_{\mathcal O}^*N)
 \simeq f_*M\otimes_{\mathcal O_Y}^L N.
\tag{3.6}
\]
The complexes remain derived unless flatness is known. In particular, a flat bundle $N$ permits ordinary tensor product. The unit for $\otimes^!$ is $\mathcal O_X[d_X]$. Using $\mathcal O_X$ as the unit would lose a shift at every tensor operation.

## 4. Proper duality: the two explicit calculations

Recall the holonomic dual from Holonomic D-modules and duality:
\[
\mathbb D_XM=
\omega_X^{-1}\otimes_{\mathcal O_X}
 R\mathcal Hom_{\mathcal D_X}(M,\mathcal D_X)[d_X].
\tag{4.1}
\]
The Hom is initially a right module. The density line in (4.1) changes sides.

The general proper-duality theorem says
\[
f_*\mathbb D_XM\simeq\mathbb D_Yf_*M
\tag{4.2}
\]
for a proper map and a bounded complex with coherent differential-operator cohomology. Etingof's notes state it in this generality, in their appendix on the six functors, and Bernstein's *Algebraic theory of D-modules* proves it for proper morphisms of quasi-projective varieties, in the section “The duality theorem for a proper morphism”. We now prove the closed-embedding and projective-product cases. A general proper morphism under our separated-variety convention need not admit a closed embedding into $\mathbb P^n\times Y$; that factorization is projective.

**Closed embeddings.** Lemma 1.2 has the sheaf form
$R\mathcal Hom_{\mathcal D_X}(i_*A,M)
=i_{\mathrm{sh},*}R\mathcal Hom_{\mathcal D_Z}(A,i^!M)$.
The counit applied to $\mathcal O_X$ gives the trace
$i_*\mathcal O_Z[d_Z]\to\mathcal O_X[d_X]$.
Apply direct image to an evaluation map, then this trace, to compare
$i_{\mathrm{sh},*}R\mathcal Hom_{\mathcal D_Z}(A,T_i)[d_Z]$
with $R\mathcal Hom_{\mathcal D_X}(i_*A,\mathcal D_X)[d_X]$.
After the same side-changing line, these are $i_*\mathbb D_ZA$ and
$\mathbb D_Xi_*A$.

For $A=\mathcal D_Z$, the first expression is
$i_{\mathrm{sh},*}T_i[d_Z]$.
The sheaf adjunction computes the second as
$i_{\mathrm{sh},*}i^!\mathcal D_X[d_X]$.
Since $\mathcal D_X$ is flat over $\mathcal O_X$,
$i^!\mathcal D_X=T_i[-c]$.
Thus the second is also $i_{\mathrm{sh},*}T_i[d_Z]$.
The counit comparison is the identity under adjunction. This gives an isomorphism on finite free source modules.

Over an affine target the source is affine. Quasi-coherence and coherence give finite free source surjections and coherent successive kernels. The finite-amplitude dévissage detailed in (4.10) below extends the comparison from free modules to coherent modules: closed direct image is exact and preserves coherence, and both duals have a fixed local Ext bound. Bounded truncation triangles then handle complexes. The counit and its evaluation are intrinsic, so they glue, proving
\[
\mathbb D_X i_*M\simeq i_*\mathbb D_ZM.
\tag{4.3}
\]
The calculation also explains why a delta module at a point is self-dual.

For the projective calculation we give the generation step as well as the trace step.

**Lemma 4.1.** If $Y$ is smooth affine, quasi-coherent $\mathcal D_{\mathbb P^n\times Y}$-modules have exact global sections and are generated by their global sections. A coherent such module therefore admits a surjection from a finite-rank free differential-operator module, and this can be repeated for its coherent kernels.

**Proof.** Let $V=\mathbb A^{n+1}\setminus\{0\}$, and pull a module $M$ back, without a dimension shift, along the scalar torsor
$q:V\times Y\to\mathbb P^n\times Y$.
The pullback has its natural scalar equivariance. The Euler field
$\theta=\sum z_a\partial_{z_a}$ acts on weight-$m$ sections by $m$.
Since $q$ is affine, descent identifies $H^r(\mathbb P^n\times Y,M)$ with the weight-zero part of $H^r(V\times Y,q_{\mathcal O}^*M)$. Taking a weight is exact for a graded vector space.

Embed $V\times Y$ openly in the affine $\mathbb A^{n+1}\times Y$. All higher direct-image cohomology is supported on $\{0\}\times Y$, and is a quasi-coherent differential-operator module. Kashiwara's normal polynomial description says that the Euler eigenvalues of every such module are
$-(n+1),-(n+2),\ldots$, even if the tangential coefficient module is infinite. Affine quasi-coherent acyclicity now gives zero weight-zero cohomology in every positive degree. This proves exactness of global sections.

For faithfulness, suppose $M\ne0$. Its pullback has a nonzero global section: it is quasi-coherent on the quasi-affine $V\times Y$, and its open direct image is quasi-coherent on an affine scheme. Take a nonzero homogeneous section $v$ of weight $m$. If $m<0$, some $z_av$ is nonzero; otherwise the section is supported at the deleted zero locus and must vanish. Repeat to reach weight zero. If $m>0$, the equality
$mv=\sum z_a\partial_{z_a}v$ implies some derivative is nonzero. Repeat to reach weight zero. Hence $\Gamma(M)\ne0$.

Let $M_0$ be the differential-operator subsheaf generated by all global sections of $M$. Exactness gives $\Gamma(M/M_0)=0$, so faithfulness gives $M=M_0$. Coherence and quasi-compactness select finitely many of these generators. Kernels of the resulting finite free surjections are coherent by Noetherianity. $\square$

**Theorem 4.2.** Formula (4.2) holds for $p:\mathbb P^n\times Y\to Y$ and every bounded coherent differential-operator complex.

**Proof.** Work on an affine open in $Y$ and write $X=\mathbb P^n\times Y$. The relative Spencer complex identifies
$p_*\mathcal O_X[n]$ with $Rp_{\mathrm{sh},*}\Omega^\bullet_{X/Y}[2n]$.
On the standard projective cover, define its trace by the coefficient
\[
\operatorname{res}
\left(\frac{dz_1\wedge\cdots\wedge dz_n}{z_1\cdots z_n}\right)=1
\tag{4.4}
\]
in Čech degree $n$ and form degree $n$. All other total degrees map to zero. This annihilates Čech boundaries. It also annihilates exterior derivatives: a Laurent derivative cannot produce an exponent $-1$ in its differentiated variable, since the only possible original exponent is zero and its derivative has coefficient zero. Thus this is a cochain trace
\[
p_*\mathcal O_X[n]\longrightarrow\mathcal O_Y.
\tag{4.5}
\]
The residue is the standard projective trace and is compatible with base coefficients and the horizontal differential-operator action.

We record its two required cohomology calculations. For $\mathcal O_{\mathbb P^n}(m)$, split the homogeneous Čech complex by Laurent monomial exponents $e_0,\ldots,e_n$ of sum $m$. A monomial occurs exactly on intersections whose index set contains every index with negative exponent. If there are some but not all negative exponents, inserting an index with nonnegative exponent contracts that subcomplex. If none are negative, its only cohomology is in degree zero. If all are negative, its only term surviving cohomology is in degree $n$. Consequently
\[
R\Gamma(\mathbb P^n,\mathcal O)=k,\qquad
R\Gamma(\mathbb P^n,\omega_{\mathbb P^n})=k[-n],
\tag{4.6}
\]
with the latter generator and trace normalized by (4.4).

Put $T_p=\mathcal D_{X\to Y}$. A coherent differential-operator complex is locally perfect, so tensor–Hom evaluation rewrites the right module underlying $p_*\mathbb D_XM$ as
\[
F(M)=Rp_{\mathrm{sh},*}
 R\mathcal Hom_{\mathcal D_X}(M,T_p)[d_X].
\tag{4.7}
\]
The corresponding right module underlying $\mathbb D_Yp_*M$ is
\[
G(M)=R\mathcal Hom_{\mathcal D_Y}(p_*M,\mathcal D_Y)[d_Y].
\tag{4.8}
\]
Both expressions subsequently have the same side-changing factor $\omega_Y^{-1}$.

Apply $p_*$ to a Hom map $M\to T_p$, then compose with the trace. More explicitly, transfer tensoring first gives a map between the transferred complexes; sheaf direct image gives the Hom comparison; finally (3.6) and (4.5) give
$p_*T_p[d_X]\to\mathcal D_Y[d_Y]$.
This constructs a natural comparison $F(M)\to G(M)$.

For $M=\mathcal D_X$, (4.6) computes both sides:
\[
F(\mathcal D_X)=\mathcal D_Y[d_Y+n],
\qquad
p_*\mathcal D_X=\mathcal D_Y[-n],
\qquad
G(\mathcal D_X)=\mathcal D_Y[d_Y+n].
\tag{4.9}
\]
Here the second formula follows immediately by tensoring the backward transfer with $\mathcal D_X$: its fiber coefficient is $\omega_{\mathbb P^n}$. The comparison evaluates a constant against the top Čech density and then applies (4.4). It is the identity with this normalization. Thus it is an isomorphism on every finite free module.

To extend this calculation, Lemma 4.1 gives, for a coherent module $M$, exact sequences
$0\to K_1\to\mathcal D_X^{r_0}\to M\to0$ and their iterates. Let $C(M)$ denote the comparison cone. Since the comparison is an isomorphism on the free middle term, the contravariant exact triangles give
\[
C(M)\simeq C(K_N)[-N]
\tag{4.10}
\]
after $N$ steps. There is a bound on the cohomological degrees of all these cones, independent of the coherent input module. For (4.7), use the local differential-operator homological-dimension bound $2d_X$, the shift $[d_X]$, and finite sheaf cohomological dimension. For (4.8), the relative Spencer–Čech complex gives $p_*K_N$ degrees between $-n$ and $n$; proper coherence and the analogous bound $2d_Y$ then bound its dual. Proper coherence used here is Schnell, Theorem 18.1.

Choose a fixed sufficiently large bound $B$ for these degrees. For any fixed $a$, taking $N>a+B$ in (4.10) proves $H^aC(M)=0$. Thus the comparison is an isomorphism for modules. Bounded truncation triangles prove it for coherent complexes. This argument does not assume the existence of a globally bounded free resolution. Restoring the common side-changing line proves (4.2) for $p$. The residue trace is intrinsic, so the construction glues over $Y$. $\square$

The two cases also prove (4.2) for projective morphisms between smooth varieties, by factoring such a morphism as a closed embedding followed by a projective-product projection and composing the two isomorphisms. The full nonprojective proper case remains the stated theorem.

## 5. Adjunctions on holonomic complexes

Write $D_h^b(X)$ for bounded complexes with holonomic cohomology. To define the next functors we use the holonomicity-preservation theorem: $f_*$ and $f^!$ preserve these categories. Its exact locator is Schnell, Theorem 18.5; its proof belongs to the next lesson, *Preservation of holonomicity and minimal extensions*. Duality and its biduality isomorphism have already been established in the duality lesson. External products preserve holonomicity: the external good filtration has characteristic support equal to the product, whose dimension is the sum of the two holonomic dimensions.

Define
\[
f_!=\mathbb D_Y f_*\mathbb D_X,
\qquad
f^*=\mathbb D_X f^!\mathbb D_Y.
\tag{5.1}
\]

**Theorem 5.1.** On these categories,
\[
f_!\dashv f^!,\qquad f^*\dashv f_*.
\tag{5.2}
\]
For a proper $f$, (4.2) identifies $f_!=f_*$, and hence $f_*\dashv f^!$.

**Proof.** For a coherent $\mathcal D_X$-complex $A$ and any coefficient complex $B$, local finite projective resolutions give the evaluation identity
\[
R\mathcal Hom_{\mathcal D_X}(A,B)
 \simeq (\omega_X\otimes\mathbb D_XA)
       \otimes_{\mathcal D_X}^L B[-d_X].
\tag{5.3}
\]
Let $T_f=\mathcal D_{X\to Y}$. Insert
$f^!N=T_f\otimes_{f^{-1}\mathcal D_Y}^L f^{-1}N[d_X-d_Y]$
in (5.3). Associativity gives
\[
\begin{aligned}
Rf_{\mathrm{sh},*}R\mathcal Hom_{\mathcal D_X}(M,f^!N)
&\simeq
 \left[f_*^r(\omega_X\otimes\mathbb D_XM)\right]
          \otimes_{\mathcal D_Y}^L N[-d_Y]\\
&\simeq
 (\omega_Y\otimes f_*\mathbb D_XM)
          \otimes_{\mathcal D_Y}^L N[-d_Y]\\
&\simeq R\mathcal Hom_{\mathcal D_Y}(f_!M,N).
\end{aligned}
\tag{5.4}
\]
The tensor–pushforward interchange in the first line is the transfer comparison proved in the composition lesson. Locally on the base it uses a finite affine Čech model and a bounded projective resolution over the differential-operator ring; projective summands and the finite totalizations preserve that comparison. Thus it applies to the complexes here. The second line is side-changing compatibility of direct image; the third is (5.3) and biduality.

Taking global cohomology in degree zero gives $f_!\dashv f^!$, including its natural unit and counit. Duality reverses morphisms and gives
\[
\begin{aligned}
\operatorname{Hom}_X(f^*N,M)
&\simeq\operatorname{Hom}_X(\mathbb D_XM,f^!\mathbb D_YN)\\
&\simeq\operatorname{Hom}_Y(f_!\mathbb D_XM,\mathbb D_YN)\\
&\simeq\operatorname{Hom}_Y(N,f_*M).
\end{aligned}
\tag{5.5}
\]
This is the second adjunction. For proper $f$, apply (4.2) to $\mathbb D_XM$ in (5.1). $\square$

For an open embedding $j$, both $j^*$ and $j^!$ are restriction: duality commutes with restriction. Also $j_*$ is derived sheaf direct image with its local differential-operator action. Ordinary sheaf restriction–direct-image adjunction, applied to modules and resolutions, gives
\[
j^*=j^!\dashv j_*.
\tag{5.6}
\]
This statement holds on quasi-coherent complexes before imposing holonomicity. Dualizing it gives $j_!\dashv j^!$ on holonomic complexes.

The proper and open cases agree with the usual reduction by compactification. If a smooth completion $\overline X$ is chosen, the graph followed by
$X\times Y\hookrightarrow\overline X\times Y\to Y$
factors a morphism into a proper closed graph, an open embedding and a proper projection. Smooth completion is an algebraic-geometric input, not needed for the direct proof (5.4). Composing the known adjunctions in these cases reproduces (5.2).

**Why properness matters.** For $p:\mathbb A^1\to\mathrm{pt}$,
$p_*\mathcal O=k[1]$, $p^!k=\mathcal O[1]$, and
$p_!\mathcal O=k[-1]$. In particular,
\[
\operatorname{Hom}(p_*\mathcal O,k[1])=k,\qquad
\operatorname{Hom}(\mathcal O,p^!k[1])
 =\operatorname{Ext}^2_{\mathcal D_{\mathbb A^1}}
        (\mathcal O,\mathcal O)=0.
\tag{5.7}
\]
The last equality follows from the one-dimensional Spencer resolution and affine de Rham calculation. Thus $p_*\dashv p^!$ fails, although both adjunctions (5.2) hold.

## 6. Boundary extensions and the six operations

Let $j:\mathbb G_m\hookrightarrow\mathbb A^1$, and put
$A=k\langle x,\partial\rangle/(\partial x-x\partial-1)$.
The duality lesson computed
\[
L=j_*\mathcal O_{\mathbb G_m}
 \simeq A/A(\partial x)=k[x,x^{-1}],
\qquad
J=j_!\mathcal O_{\mathbb G_m}\simeq A/A(x\partial).
\tag{6.1}
\]
Indeed, a generator $x^{-1}$ of $L$ satisfies $(\partial x)x^{-1}=0$.
The formal adjoint of $\partial x$ is $-x\partial$, and the dual of the cyclic resolution gives $J$.

There are nonsplit exact sequences
\[
0\to\mathcal O_{\mathbb A^1}\to L\to\delta_0\to0,
\qquad
0\to\delta_0\to J\to\mathcal O_{\mathbb A^1}\to0.
\tag{6.2}
\]
For the second, if $v$ is the cyclic generator of $J$, then $\partial v$ generates the delta submodule since $x\partial v=0$. Quotienting it out leaves $Av/A\partial v=\mathcal O$. Nonsplitting and the nonzero normal derivative basis were proved in the duality lesson. This is a differential-operator extension, with its boundary derivatives.

For $p:\mathbb P^1\to\mathrm{pt}$ the earlier Čech computation gives
\[
p_*\mathcal O_{\mathbb P^1}\simeq k[1]\oplus k[-1].
\tag{6.3}
\]
The dual exchanges the two degrees. In the de Rham presentation, the degree-zero class $1$ pairs with the top Čech class $[dx/x]$ by residue $1$. Each cohomology pairing is perfect. This proves self-duality, compatible with the trace in Theorem 4.2; the displayed splitting is not a preferred splitting of complexes.

The principal operations can be arranged as follows. All rows restrict to holonomic complexes; the tensor row is derived.

| Operation | Construction or convention | Relation |
|---|---|---|
| $f_*$ | Transfer tensor and sheaf direct image | Right adjoint to $f^*$ |
| $f^!$ | $Lf_{\mathcal O}^*[d_X-d_Y]$ | Right adjoint to $f_!$ |
| $f_!$ | $\mathbb D_Yf_*\mathbb D_X$ | Equals $f_*$ for proper $f$ |
| $f^*$ | $\mathbb D_Xf^!\mathbb D_Y$ | Restriction for an open embedding |
| $\otimes^!$ | $\Delta^!(-\boxtimes-)$ | Unit $\mathcal O_X[d_X]$; formula (3.3) |
| $\mathbb D_X$ | (4.1) | Contravariant biduality; reverses the adjunctions |

The phrase “six operations” also commonly lists ordinary tensor and internal Hom instead of external tensor and duality. The essential four map functors are the first four rows; specifying the tensor convention makes the remaining terminology unambiguous here.

Over $\mathbb C$, the regular-holonomic Riemann–Hilbert theorem identifies the covariant de Rham functor with constructible complexes and matches these four map functors and duality. We state this comparison, rather than using it to prove the algebraic results above: Bhatt–Blickle–Lyubeznik–Singh–Zhang, Section 2, Theorem 2.1, part (1), and Main Theorem C in the lecture “Riemann–Hilbert correspondence” of Bernstein's *Algebraic theory of D-modules*. A flat bundle $E$ corresponds to its horizontal local system shifted by $d_X$. In particular $\mathcal O_X[d_X]$ corresponds to the sheaf dualizing complex $\mathbb C_X[2d_X]$. The operation $\otimes^!$ corresponds to $\Delta^!$ of an external product, with that dualizing complex as unit. This explains the connection with the extraordinary tensor convention for sheaves in Six operations for sheaves on manifolds.

For a smooth map of relative dimension $r$, one furthermore has $f^!=f^*[2r]$ on holonomic complexes. Locally the smooth pullback is a product followed by an étale map. The dual of the trivial relative connection is itself: its relative Spencer resolution is the regular Koszul sequence of the vertical derivative symbols, whose dual reverses the $r$ terms and is canceled by the relative density and dimension shift. Thus duality commutes with unshifted smooth pullback; dualizing its shift $[r]$ gives $[-r]$ and the claimed difference $2r$. For a closed embedding of codimension $c$, in contrast,
$i^!\mathcal O_X=\mathcal O_Z[-c]$ and
$i^*\mathcal O_X=\mathcal O_Z[c]$.

## 7. Exercises

**Exercise 10.1 (easy).** Verify base change for $p:\mathbb A^1\to\mathrm{pt}$ and the identity inclusion $\mathrm{pt}\to\mathrm{pt}$, on both $\mathcal O$ and $\delta_0$. Then check the family square at the end of Section 2.

**Exercise 10.2 (easy).** Prove restriction is left adjoint to $j_*$ for an arbitrary open embedding. Explain why a nonaffine open embedding requires derived direct image.

**Exercise 10.3 (medium).** Compute $j_!\mathcal O_{\mathbb G_m}$. For an arbitrary holonomic $A$-module $M$, identify both sides of
$\operatorname{Hom}(J,M)=\operatorname{Hom}(\mathcal O_{\mathbb G_m},j^!M)$
explicitly and give the inverse to restriction.

**Exercise 10.4 (medium).** Check the self-duality of $p_*\mathcal O_{\mathbb P^1}$ by a Čech calculation, including the trace.

**Exercise 10.5 (hard).** Prove proper duality for
$p:\mathbb P^1\times Y\to Y$ on every bounded coherent differential-operator complex. Explain the reduction from $\mathcal D_X$ to an arbitrary coherent module.

**Exercise 10.6 (medium).** Let $i:\mathrm{pt}\hookrightarrow\mathbb A^1$ and $\delta=i_*k$. Compute $\delta\otimes^!\delta$. Check the projection formula for $i$ with $M=k$, $N=\delta$.

## 8. Solutions

**Solution 10.1.** The base-change map is the identity because both base maps are identities with dimension difference zero. The polynomial de Rham complex
$k[x]\xrightarrow{\partial}k[x]dx$ has kernel $k$ and zero cokernel, so $p_*\mathcal O=k[1]$ on both sides. For $\delta=k[\partial]\delta_0$, differentiation is multiplication by $\partial$, which is injective with cokernel $k\delta_0dx$. Thus $p_*\delta=k$ on both sides. In the nontrivial family square, $p_*\mathcal O=\mathcal O_t[1]$; $i^!\mathcal O_t=k[-1]$; therefore the first side is $k$. The pulled-back object is $\mathcal O_x[-1]$, whose pushforward is again $k$.

**Solution 10.2.** At the module level, a map $M|_U\to N$ gives the sheaf map $M\to j_{\mathrm{sh},*}N$ by restriction on each open subset and the given map on its intersection with $U$. This is inverse to restricting a map on $X$. It respects differential operators because the action is local and restricts with their coefficients. Restriction is exact. Its right adjoint consequently preserves injectives, so applying this adjunction to injective resolutions proves the derived adjunction. The direct-image complex is quasi-coherent by a finite affine Čech calculation. A nonaffine open embedding can have nonzero higher direct images: for the punctured plane, $R^1j_*\mathcal O$ is the quotient
$k[x^{\pm1},y^{\pm1}]/(k[x^{\pm1},y]+k[x,y^{\pm1}])$.
It contains $x^{-1}y^{-1}$. Keeping only degree-zero direct image would omit part of the right adjoint.

**Solution 10.3.** Since $\mathbb D\mathcal O_{\mathbb G_m}=\mathcal O_{\mathbb G_m}$, dualizing $A/A(\partial x)$ gives $J=A/A(x\partial)$ by the formal-adjoint calculation. If $v$ is its cyclic generator, a homomorphism is specified by
\[
m=\phi(v)\in M,\qquad x\partial m=0.
\tag{8.1}
\]
On the other side a homomorphism from the trivial connection is a horizontal vector in $M_x$:
\[
n\in M_x,\qquad\partial n=0.
\tag{8.2}
\]
Restriction sends $m$ to $m/1$. We construct its inverse.

Write a horizontal $n=a/x^s$ with $s\ge0$. Let $T=\ker(M\to M_x)$, the point-supported submodule, and $\theta=x\partial$. The vector
$b=(\theta-s)a$ lies in $T$. Kashiwara's polynomial normal form makes $\theta$ diagonal on $T$ with eigenvalues $-1,-2,\ldots$; every individual vector is a finite sum of eigenvectors. Hence $\theta-s$ has an inverse on $T$. Put
\[
a'=a-(\theta-s)^{-1}b,\qquad
m=\frac{\partial^s a'}{s!}.
\tag{8.3}
\]
Then $\theta a'=sa'$. Since $[\theta,\partial]=-\partial$, (8.3) satisfies $\theta m=0$. In the localization, $a'=x^s n$ and $\partial n=0$, so $\partial^s a'/s!=n$. If a vector in (8.1) restricts to zero, it is in $T$, whose negative Euler spectrum has no zero eigenspace; it is therefore zero. This proves existence, uniqueness and independence of the chosen fraction. For $M=\delta$ both Hom spaces vanish; for $M=\mathcal O$ both are $k$. The construction even works for arbitrary quasi-coherent $A$-modules.

**Solution 10.4.** Cover $\mathbb P^1$ by the $x$ and $x^{-1}$ charts. For $\mathcal O$, the Čech quotient of Laurent polynomials by polynomials in either coordinate is zero, and the intersection of the two polynomial subrings is $k$. For $\Omega^1$, the quotient leaves exactly $k[dx/x]$; a regular global form would have to be both polynomial times $dx$ and a polynomial times $-x^{-2}dx$, so it is zero. The hypercohomology of $\mathcal O\to\Omega^1$ is therefore $k$ in degrees $0,2$. After $[1]$, the direct image has degrees $-1,1$. The trace takes the coefficient of $x^{-1}dx$ and kills both Čech coboundaries and derivatives, since $\operatorname{res}d(x^m)=0$ for every integer $m$. The classes $1$ and $[dx/x]$ pair to $1$. This gives perfect pairings in opposite degrees and the desired duality isomorphism.

**Solution 10.5.** Work with $Y$ affine. The relative Spencer complex is
$[M\to\Omega^1_{X/Y}\otimes M][1]$, and the two-chart Čech complex computes its direct image. Its trace is exactly the residue from Solution 10.4, tensored with the base; thus it is $\mathcal D_Y$-linear.

Use the comparison (4.7)–(4.8). For $M=\mathcal D_X$, its first side is
$Rp_{\mathrm{sh},*}T_p[d_Y+1]=\mathcal D_Y[d_Y+1]$.
Tensoring the backward transfer with $\mathcal D_X$ gives
$p_*\mathcal D_X=Rp_{\mathrm{sh},*}(\omega_{\mathbb P^1}\boxtimes\mathcal D_Y)
=\mathcal D_Y[-1]$.
Hence its second side is also $\mathcal D_Y[d_Y+1]$. The comparison sends the constant $1$ to the functional taking $[dx/x]$ to $1$, so it is an isomorphism.

Lemma 4.1, for the scalar torsor
$(\mathbb A^2\setminus0)\times Y\to\mathbb P^1\times Y$,
provides finite free surjections for a coherent module and each successive kernel. The comparison cones satisfy $C(M)=C(K_N)[-N]$. Their degrees have a bound independent of $K_N$: the direct-image Spencer–Čech degrees are $-1,0,1$; differential-operator Ext has the fixed local dimension bound; and proper coherence permits the bounded dual on the base. Thus any fixed cohomology degree of $C(M)$ vanishes by taking $N$ sufficiently large. Truncation triangles extend the result to bounded coherent complexes. Finally side-change by $\omega_Y^{-1}$ on both sides. This proves $\mathbb D_Yp_*M=p_*\mathbb D_XM$ for the entire assigned class, and the intrinsic trace glues over affine opens in $Y$.

**Solution 10.6.** Compute the structure-sheaf derived tensor using the resolution
$[\mathcal O\xrightarrow{x}\mathcal O]$ of the residue field, or equivalently apply the point pullback and its normal Koszul model to $\delta$. Multiplication by $x$ on $\delta=k[\partial]\delta_0$ is $-d/d\partial$, surjective with kernel $k\delta_0$. Hence
$L i_{\mathcal O}^*\delta=k[1]$ and $i^!\delta=k$.
The projection formula gives
\[
i_*(k\otimes^!i^!\delta)=i_*k=\delta.
\tag{8.4}
\]
For a direct calculation of its other side, $\delta$ is locally $x$-power torsion and its normal polynomial decomposition gives
$\operatorname{Tor}^{\mathcal O}_0(\delta,\delta)=0$ and
$\operatorname{Tor}^{\mathcal O}_1(\delta,\delta)\simeq\delta$.
Indeed $\delta$ as an $\mathcal O$-module is $k[x,x^{-1}]/k[x]$ (with the factorial normal-basis identification). Tensor its flat resolution
$[\mathcal O\to\mathcal O_x]$ with $\delta$; the localization term is zero and the remaining term is $\delta$ in degree $-1$. Therefore
$\delta\otimes_{\mathcal O}^L\delta=\delta[1]$.
The diagonal shift $[-1]$ gives
$\delta\otimes^!\delta=\delta$, agreeing with (8.4). This uses the induced differential-operator action, which is also fixed by the graph–diagonal proof of (3.3).

## 9. What this lesson does not prove

The full proper-duality theorem for smooth separated varieties, beyond the closed and projective cases proved here, is stated in Etingof's notes; Bernstein's notes prove it for proper morphisms of quasi-projective varieties. The proper-coherence theorem used in Theorem 4.2 is Schnell, Theorem 18.1. Holonomicity preservation needed to close the categories in (5.1) is Schnell, Theorem 18.5; the next lesson supplies its proof. The optional reduction by smooth completion uses compactification and resolution of singularities as algebraic-geometric inputs. Finally, the regular-holonomic comparison with constructible sheaves is stated with the Section 6 locators; its correspondence theorem is treated later in the course.

These inputs are distinct from the results proved here: localization, closed adjunction, base change, the projection formula with its shift, closed and projective-product duality, both holonomic adjunctions, and every displayed boundary and degree calculation.

## References

- A. Beilinson and V. Drinfeld, [*Quantization of Hitchin's integrable system and Hecke eigensheaves*](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf), Sections 7.2.8–7.2.11: transfer and de Rham direct-image conventions. These sections provide the construction, rather than the base-change or proper-duality proofs.
- J. Bernstein, [*Algebraic theory of D-modules*](https://www.math.columbia.edu/~khovanov/resources/Bernstein-dmod.pdf), lecture notes: base change, the duality theorem for a proper morphism together with the projection formula and the holonomic adjunctions, and the Riemann–Hilbert correspondence (Main Theorem C).
- D. Miličić, [*Lectures on Algebraic Theory of D-Modules*](https://www.math.utah.edu/~milicic/Eprints/dmodules.pdf), Chapter IV, §10: base change for smooth varieties with smooth fiber product.
- P. Etingof, [*Introduction to algebraic D-modules*](https://math.mit.edu/~etingof/dmodwien.pdf), Propositions 3.1, 3.3 and 3.5, pages 11–13, and the appendix on the formalism of six functors: base change, proper adjunction, localization and proper-duality statements.
- C. Schnell, [*Algebraic D-modules*](https://www.math.stonybrook.edu/~cschnell/pdf/notes/d-modules.pdf), Theorems 18.1 and 18.5: proper coherence and holonomicity preservation.
- B. Bhatt, M. Blickle, G. Lyubeznik, A. K. Singh and W. Zhang, [*Applications of perverse sheaves in commutative algebra*](https://arxiv.org/abs/2308.03155), Section 2, Theorem 2.1, part (1): the regular-holonomic comparison with sheaf functors.
