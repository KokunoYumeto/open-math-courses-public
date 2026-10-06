# Kashiwara's equivalence and D-modules on singular spaces

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A module of distributions supported at a point contains the delta vector and all its normal derivatives. Kashiwara's theorem says that this is the general shape of a differential-operator module supported on a smooth closed subvariety: the normal derivatives carry no extra choice. After proving the theorem, we will use smooth ambient varieties to define modules on a singular variety and prove that the resulting category does not depend on the ambient variety.

The ground field $k$ has characteristic zero. All modules are quasi-coherent over the structure sheaf. Smooth varieties are separated, and characteristic varieties are taken only for coherent differential-operator modules. We retain the left-module convention
\[
f^!=Lf^*[d_X-d_Y].
\]
For a closed embedding of codimension $c$, this is $i^!=Li^*[-c]$, with no additional shift. Our prerequisite is Direct images and the relative de Rham complex, including closed direct image, composition, and the normal derivative description. We also use the derived Koszul calculation from Inverse images.

## 1. Support means local nilpotence

Let $i:Z\hookrightarrow X$ be a smooth closed embedding, with ideal $\mathcal I$. Let $\operatorname{Mod}_Z(\mathcal D_X)$ denote modules whose restriction to $X\setminus Z$ vanishes. This is set-theoretic support; it does not require $\mathcal I M=0$.

On an affine chart where $\mathcal I=(t_1,\ldots,t_c)$, quasi-coherence makes the support condition equivalent to
\[
\text{for every }m,\text{ some }N\text{ satisfies }\mathcal I^Nm=0.
\tag{1.1}
\]
Indeed $M_{t_a}=0$ implies $t_a^{N_a}m=0$ for each $a$. Every monomial in the $t_a$ of total degree greater than $\sum_a(N_a-1)$ has one exponent at least $N_a$ and kills $m$. Conversely (1.1) makes each localization vanish. This argument applies to arbitrary quasi-coherent modules and uses no finite-generation hypothesis.

In one normal coordinate, the Weyl relation is
\[
[\partial,t]=1.
\]
If $tv=0$, it forces
\[
t\partial^jv=-j\partial^{j-1}v,\qquad
(t\partial)\partial^jv=-(j+1)\partial^jv. \tag{1.2}
\]
Thus $t$ need not act as zero on a module supported on $t=0$. Repeated normal differentiation produces vectors on which it acts nontrivially, but locally nilpotently.

## 2. Recovering every coefficient

The key algebraic fact works with any vector space carrying operators $t,\partial$ satisfying the Weyl relation, provided $t$ is locally nilpotent. Put $V=\ker t$.

**Lemma 2.1.** The map
\[
k[\partial]\otimes_kV\longrightarrow M,\qquad
\partial^j\otimes v\longmapsto\partial^jv \tag{2.1}
\]
is an isomorphism. It commutes with every operator that commutes with both $t$ and $\partial$.

**Proof.** Define a finite sum on each vector:
\[
\pi(m)=\sum_{\ell\geq0}\frac{\partial^\ell t^\ell m}{\ell!}. \tag{2.2}
\]
The relation $t\partial^\ell=\partial^\ell t-\ell\partial^{\ell-1}$ gives $t\pi(m)=0$ by cancellation of consecutive terms. Also $\pi(v)=v$ for $v\in V$. The formula
\[
\pi(\partial^rv)=
\sum_{\ell=0}^r(-1)^\ell\binom r\ell\,\partial^rv
\]
equals $v$ if $r=0$ and zero if $r>0$.

Every vector has the expansion
\[
m=\sum_{j\geq0}\frac{(-1)^j}{j!}\,
\partial^j\pi(t^jm). \tag{2.3}
\]
To check it, substitute (2.2). The coefficient of $\partial^nt^nm$ in the resulting finite double sum is
$\sum_{j=0}^n(-1)^j/(j!(n-j)!)$, which is $1$ for $n=0$ and $0$ otherwise. This proves surjectivity of (2.1).

For uniqueness, if $\sum_{j=0}^q\partial^jv_j=0$, apply $\pi t^r$. Formula (1.2) gives
\[
\pi t^r\left(\sum_j\partial^jv_j\right)=(-1)^rr!v_r.
\tag{2.4}
\]
Characteristic zero implies $v_r=0$ for every $r$. The final assertion follows directly from the projector formulas. ∎

In particular the Euler operator $\theta=t\partial$ is diagonalizable in the algebraic direct-sum sense:
\[
M=\bigoplus_{j\geq1}M_{-j},\qquad
M_{-j}=\partial^{j-1}V,\qquad M_{-1}=V. \tag{2.5}
\]
Every vector has finitely many components. Normal differentiation is an isomorphism $M_{-j}\to M_{-j-1}$, and $t$ is a nonzero scalar multiple of its inverse between those spaces.

For commuting normal pairs $(t_a,\partial_a)$, all cross commutators vanish. The projectors $\pi_a$ commute, so $\pi=\pi_1\cdots\pi_c$ projects to
$V=\bigcap_a\ker t_a$. The same binomial calculation gives
\[
M=\bigoplus_{\alpha\in\mathbb N^c}\partial_t^\alpha V,\qquad
m=\sum_\alpha\frac{(-1)^{|\alpha|}}{\alpha!}\,
\partial_t^\alpha\pi(t^\alpha m). \tag{2.6}
\]
The sums are finite by (1.1). Tangent-coordinate operators commute with all the normal pairs, and hence act on $V$.

## 3. The equivalence, with its intrinsic inverse

**Theorem 3.1 (Kashiwara).** For a smooth closed embedding $i:Z\hookrightarrow X$, direct image is an exact equivalence
\[
i_*:\operatorname{Mod}(\mathcal D_Z)
\ \xrightarrow{\ \sim\ }\
\operatorname{Mod}_Z(\mathcal D_X). \tag{3.1}
\]
Its inverse is $K_i(M)=H^0(i^!M)$. On the supported category, $i^!M$ is concentrated in degree zero. The equivalence preserves and reflects coherence and holonomicity.

There is a density factor in the global inverse. If $\mathcal N^*_{Z/X}=\mathcal I/\mathcal I^2$, its underlying module is
\[
K_i(M)=\det(\mathcal N^*_{Z/X})
\otimes_{\mathcal O_Z}\{m\in i^{-1}M:\mathcal I m=0\}.
\tag{3.2}
\]
This formula includes the differential-operator action induced by transfer. A coordinate choice trivializes the determinant and identifies the inverse with the common kernel in (2.6); a bare common kernel without that twist is not the intrinsic left-module inverse.

**Proof of the equivalence.** An intrinsic construction of the actions and comparison maps is easiest on right modules. Let $T_i=\mathcal D_{Z\to X}$. For a right $\mathcal D_X$-module $Q$ set
\[
K_i^r(Q)
=\mathcal Hom_{\,i^{-1}\mathcal D_X^{\mathrm{op}}}
(T_i,i^{-1}Q). \tag{3.3}
\]
The left $\mathcal D_Z$-action on $T_i$ induces a right action on this Hom: $(\phi P)(t)=\phi(Pt)$. Since
$T_i=\mathcal O_Z\otimes_{i^{-1}\mathcal O_X}i^{-1}\mathcal D_X$,
tensor-Hom adjunction identifies (3.3) with the subsheaf of $Q$ killed by $\mathcal I$.

There are canonical maps
\[
N\longrightarrow K_i^r(i_*^rN),\qquad
i_*^rK_i^r(Q)\longrightarrow Q, \tag{3.4}
\]
given by $n\mapsto(t\mapsto n\otimes t)$ and evaluation $\phi\otimes t\mapsto\phi(t)$. The tensor relations verify that these maps are differential-operator linear, and their definitions imply the two adjunction identities.

Side-changing (3.3) gives the left inverse
$S_Z^{-1}K_i^rS_X$. Its underlying sheaf is the common kernel tensor
$\omega_X|_Z\otimes\omega_Z^{-1}$. The cotangent exact sequence identifies this line with $\det(\mathcal N^*_{Z/X})$, proving (3.2).

Now take adapted étale coordinates on $X$ in which the normal equations are $t_1,\ldots,t_c$ and the remaining coordinates restrict to étale coordinates on $Z$. The direct-image formula in the prerequisite identifies $i_*N$ with $N[\partial_{t_1},\ldots,\partial_{t_c}]$, after trivializing the density lines. Its common normal kernel is the constant polynomial part. Thus the first map in (3.4), side-changed, is an isomorphism.

For a module $M$ supported on $Z$, (1.1) and (2.6) identify the second comparison map with the bijection
\[
K_i(M)[\partial_{t_1},\ldots,\partial_{t_c}]
\longrightarrow M.
\]
It respects tangent operators, normal derivatives, and the normal-coordinate lowering action (1.2). It is already intrinsically $\mathcal D_X$-linear by evaluation. This last observation also handles arbitrary coefficient functions in an étale coordinate ring; no product identification of the whole ambient chart is needed. Both comparison maps are therefore isomorphisms locally and globally. Their canonical definitions supply the gluing and the unit-counit identities. Exactness of $i_*$ was proved in the preceding lesson; an inverse equivalence is exact as well. ∎

### The derived degree

Locally $Li^*M$ is the normal Koszul complex in degrees $-c,\ldots,0$. On the polynomial normal form in (2.6), $t_a$ acts as $-\partial/\partial(\partial_{t_a})$. In one variable this map on $k[\partial]$ is surjective and its kernel is $k$. Hence the one-variable Koszul complex has only its degree $-1$ cohomology. Tensoring these $c$ complexes over $k$ proves that the full Koszul complex has only degree $-c$ cohomology. Its top exterior generator supplies precisely the determinant in (3.2). The shift $[-c]$ moves this group to degree zero. Thus
\[
i^!i_*N\simeq N,\qquad
i^!M\simeq K_i(M)\quad(M\text{ supported on }Z). \tag{3.5}
\]
These identifications are the intrinsic transfer identifications above. There is no second shift to append to $H^0i^!$.

### Coherence and characteristic support

If $N$ is locally finitely generated over $\mathcal D_Z$, its generators in normal degree zero generate $i_*N$ over $\mathcal D_X$. Conversely, finitely many generators of $M$ have finite expansions (2.6). Let $N_0$ be the $\mathcal D_Z$-submodule generated by their normal coefficients. Then $i_*N_0$ contains the chosen generators and, by the intrinsic direct-image action, is a $\mathcal D_X$-submodule of $M$. It must equal $M$; taking common kernels gives $N_0=K_i(M)$. The rings of differential operators are locally Noetherian, so these finite-generation statements prove coherence in both directions.

Let $\rho:T^*X|_Z\to T^*Z$ restrict covectors to tangent vectors on $Z$. For coherent $N$,
\[
\operatorname{Ch}(i_*N)=\rho^{-1}\operatorname{Ch}(N). \tag{3.6}
\]
To prove equality, choose a good filtration $F$ on $N$ and filter the normal form by
\[
F_p(i_*N)=
\sum_{q+|\alpha|\leq p}\partial_t^\alpha F_qN.
\]
PBW and the uniqueness in (2.6) give
$\operatorname{gr}(i_*N)=\operatorname{gr}N\otimes_k k[\xi_{t_1},\ldots,\xi_{t_c}]$
in these coordinates. Normal equations act as zero on this graded module, since they lower normal degree; tangent symbols act on $\operatorname{gr}N$. The filtration is good, and its support is exactly the right side of (3.6). This proves the intrinsic formula by local gluing.

For nonzero $N$, the fibers of $\rho$ have dimension $c$, so
\[
\dim\operatorname{Ch}(i_*N)=\dim\operatorname{Ch}(N)+c.
\]
Since $d_X=d_Z+c$, the dimension criterion for holonomicity proves preservation and reflection. The zero module is preserved too.

## 4. Three concrete supported modules

At the origin in the line, $\delta_0=k[\partial]\delta$ satisfies
\[
x\partial^j\delta=-j\partial^{j-1}\delta,\qquad
(x\partial)\partial^j\delta=-(j+1)\partial^j\delta.
\]
Every quasi-coherent module supported at the origin is $\delta_0\otimes_k V$ for a vector space $V$. Choosing a basis of $V$ writes it as a direct sum of copies of $\delta_0$; this choice is not canonical. It is coherent, and hence holonomic, precisely when $V$ is finite-dimensional.

The Laurent quotient
\[
L=k[x,x^{-1}]/k[x]
\]
has basis $x^{-j}$ for $j\geq1$. Its Euler eigenvalue on $x^{-j}$ is $-j$, its common kernel is $\operatorname{span}_k\{[x^{-1}]\}$, and
\[
\partial^{j-1}[x^{-1}]
=(-1)^{j-1}(j-1)![x^{-j}].
\]
Thus $L\simeq\delta_0$ with the complete eigenspace decomposition (2.5).

A point in $\mathbb A^2$ gives
\[
\delta_0^{(2)}=k[\partial_x,\partial_y]\delta,
\qquad x\delta=y\delta=0.
\]
Its two-variable normal Koszul complex has top kernel $k\delta$ in degree $-2$ and no other cohomology. After shifting by $[-2]$, the inverse is again a vector space in degree zero. The difference between one and two ambient dimensions consists of one additional freely generated normal derivative.

## 5. A singular variety and two ambient varieties

Let $Y$ be a finite-type variety, possibly singular, with a closed embedding $e:Y\hookrightarrow X$ into a smooth variety. Define
\[
\mathcal C_X(Y)=\operatorname{Mod}_{e(Y)}(\mathcal D_X). \tag{5.1}
\]
One calls this the category of differential-operator modules on $Y$. It is defined by ambient support, not by the ring of differential operators of the singular coordinate ring.

**Theorem 5.1.** For two smooth ambient embeddings $e_a:Y\hookrightarrow X_a$, the categories $\mathcal C_{X_1}(Y)$ and $\mathcal C_{X_2}(Y)$ are canonically equivalent, with coherent comparison isomorphisms for three or more embeddings.

Here “canonically” means equivalences and natural isomorphisms obeying the composition and unit identities, rather than an identification of different sheaves as literally equal.

**Proof.** Put $W=X_1\times X_2$, and support modules on the joint embedding $e=(e_1,e_2):Y\hookrightarrow W$. Write $\mathcal C_W(Y)$ for this category. We claim that the projection direct images
\[
P_a=(p_a)_*:\mathcal C_W(Y)\longrightarrow\mathcal C_{X_a}(Y)
\tag{5.2}
\]
are exact equivalences concentrated in degree zero.

First suppose $X_2=\mathbb A^m$ and $X_1$ is affine. Each coordinate function of $e_2$ on $Y$ lifts through the surjection $\mathcal O(X_1)\to\mathcal O(Y)$. The lifts define a map $F:X_1\to\mathbb A^m$ extending $e_2$ along $e_1$. Its graph $a:X_1\hookrightarrow X_1\times\mathbb A^m$ is a smooth closed subvariety containing the joint image of $Y$. Kashiwara's equivalence, restricted to modules supported on that image, gives
\[
a_*:\mathcal C_{X_1}(Y)\xrightarrow{\sim}
\mathcal C_{X_1\times\mathbb A^m}(Y).
\]
It applies to the smooth graph, even though $Y$ may be singular. The direct-image composition theorem and $p_1a=\mathrm{id}$ show $P_1a_*=\mathrm{id}$. Hence $P_1$ is the inverse equivalence. In particular its images are in the heart. This proves the claim for this local situation.

If $X_2$ is any smooth affine variety, embed it as a closed subvariety $b:X_2\hookrightarrow\mathbb A^m$. The product $1\times b$ is a smooth closed embedding. Kashiwara identifies $\mathcal C_{X_1\times X_2}(Y)$ with $\mathcal C_{X_1\times\mathbb A^m}(Y)$, and projection composition identifies their functors to $\mathcal C_{X_1}(Y)$. The preceding argument proves that $P_1$ is an equivalence. Interchanging the factors proves the claim for $P_2$.

This argument is local around $Y$ in both factors. Fix an affine neighborhood in $X_2$ of a chosen image point. Shrink an affine neighborhood in $X_1$ so that every point of $Y$ lying over it maps into that neighborhood of $X_2$: remove the closed image under $e_1$ of the complementary closed subset of $Y$. On this piece the joint support is contained in the product of the two affine neighborhoods. Restricting a module to that product and applying derived open direct image restores the original supported module. Indeed every point outside the smaller product has a neighborhood disjoint from the closed joint support, on which the module and all these derived images vanish. Composition of direct images consequently reduces $P_1$ locally to the affine case proved above; the symmetric argument applies to $P_2$.

The affine inverse constructions and their intrinsic unit and evaluation maps commute with these restrictions. Local inverse objects therefore glue by ordinary sheaf descent. On overlaps they are inverses to the same projection functor; full faithfulness gives the unique overlap isomorphisms respecting the unit and counit, and their cocycle identity. This proves the global assertion about (5.2).

Choose a quasi-inverse $P_1^{-1}$ with its unit and counit, and define
\[
E_{12}=P_2P_1^{-1}. \tag{5.3}
\]
Any other such quasi-inverse has a unique comparison isomorphism compatible with those data. In particular the equivalence (5.3) is independent of the coordinate lifts $F$: those lifts were used to prove that the fixed functor $P_1$ is an equivalence, and do not occur in its definition.

For three embeddings, use the joint support in $X_1\times X_2\times X_3$. Every projection to a factor or to a pair of factors is an equivalence by the same argument, regarding a product of smooth varieties as one factor. Direct-image composition identifies all routes to each factor. Full faithfulness therefore gives the natural comparison
\[
E_{23}E_{12}\xrightarrow{\sim}E_{13}. \tag{5.4}
\]
For four factors, both ways of composing these comparisons become the same direct-image associativity map from the fourfold product. Faithfulness implies their equality. The diagonal graph handles repeated embeddings and yields the identity comparisons. This proves the coherence assertions. ∎

This proof never applies the smooth closed-embedding theorem to the singular immersion $Y\hookrightarrow X_a$ itself. It applies that theorem only to graphs and smooth ambient inclusions.

Every affine open of $Y$ embeds into an affine space, so the construction defines $\mathcal D$-modules even when a chosen global smooth embedding is unavailable. On overlaps use Theorem 5.1 and (5.4) to glue the categories and objects. Since support only uses the complement of $Y$, a nilpotent thickening of $Y$ gives the same category.

Coherence and holonomicity are intrinsic as well. Locally each projection equivalence in the proof is the inverse of a smooth graph direct image, possibly composed with a smooth closed ambient inclusion. Theorem 3.1 preserves and reflects both properties for each such operation. Thus the comparison equivalences preserve them, and they can be checked on the ambient open cover.

### Étale locality

The construction also descends on the étale site. Locally an étale map $Y'\to Y$ has a standard étale presentation: adjoin a variable with a polynomial relation and invert its derivative. Lift the polynomial coefficients from $\mathcal O(Y)$ to those of a smooth affine ambient $X$. The same presentation defines an étale smooth ambient $X'\to X$ with $Y'=X'\times_XY$. Étale pullback is flat; its differential-operator action is the unique lifted tangent action. Hence it gives an exact pullback between the supported categories.

For an étale cover, quasi-coherent modules and their morphisms descend by the usual faithfully flat descent theorem. The operator actions descend as maps satisfying the Leibniz and Lie identities; these identities may be checked after the faithfully flat pullback. The support condition descends because a module vanishing after a faithfully flat restriction vanishes. Thus the descended sheaf is again a supported differential-operator module. Different ambient lifts give the same descent functor through the comparisons of Theorem 5.1: on joint ambient products the étale base changes of the smooth graphs have exactly the same normal derivative description, and their unit and evaluation maps commute with base change. This also proves compatibility of the comparison isomorphisms with descent.

## 6. Two crystal conventions and a stack preview

A crystal describes how an object is transported between infinitesimal thickenings, with a composition rule. It is essential to specify the transport functor.

For a smooth variety $X$ in characteristic zero, consider the infinitesimal site of nilpotent thickenings $U\hookrightarrow T$, with $U$ open in $X$. An ordinary quasi-coherent crystal assigns an $\mathcal O_T$-module $E_T$ and isomorphisms
\[
h^*E_T\xrightarrow{\sim}E_{T'}
\tag{6.1}
\]
for maps of thickenings $h:T'\to T$, compatible with identity and composition.

The local link with left modules can be seen directly. In smooth coordinates, set $\Delta_i=x_i^{(2)}-x_i^{(1)}$ on an infinitesimal neighborhood of the diagonal. For a left module with commuting coordinate derivatives, its Taylor transport is
\[
\varepsilon(m)=
\sum_\alpha\frac{\Delta^\alpha}{\alpha!}\,\partial^\alpha m.
\tag{6.2}
\]
Only finitely many terms survive on each nilpotent neighborhood. Leibniz proves that (6.2) is balanced over the two coordinate-ring actions. Replacing $\Delta$ by $-\Delta$ gives its inverse. On a triple neighborhood, adding the coordinate differences and using the binomial formula proves the composition rule. Formal smoothness lets one locally lift $U\to X$ to $T\to X$; pull back the module along such a lift and identify different lifts by (6.2). The composition rule glues these pullbacks into (6.1).

Conversely, evaluate a crystal on $X$ and on the first neighborhood of its diagonal. The linear coefficients of its transport give the operators $\partial_i$. Balancing gives their Leibniz rule; the triple-neighborhood identity gives commuting derivatives. Its identities on higher neighborhoods force the coefficients to be $\partial^\alpha/\alpha!$, by comparing successive differences in the composition rule. Thus they recover (6.2). Coordinate changes respect the construction because these are the same crystal comparison maps, and the tangent action extends to $\mathcal D_X$ by PBW. This proves the smooth characteristic-zero correspondence with ordinary infinitesimal quasi-coherent crystals.

[Stacks, Tag 07IR](https://stacks.math.columbia.edu/tag/07IR) names quasi-coherent crystals on its divided-power crystalline site. Its preceding definition and lemma specify the ordinary-pullback comparison condition. That site and its hypotheses must be distinguished from the characteristic-zero infinitesimal site just used.

For a singular space, Beilinson and Drinfeld use a different, right-module formulation. For a finite map of affine schemes corresponding to $B\to A$, their coefficient transport is
\[
h_{\mathcal O}^!(F)=\operatorname{Hom}_B(A,F).
\tag{6.3}
\]
For a closed immersion $A=B/I$, it takes the submodule killed by $I$. This is coefficient-sheaf transport, and is distinct from our derived differential-operator functor $h^!$. A BD D-crystal assigns modules on nilpotent thickenings with comparisons using (6.3) and its quasi-finite extension, rather than ordinary tensor pullback.

We state the comparison needed for this preview: BD D-crystals on a finite-type complex algebraic space form the intrinsic category of right $\mathcal D$-modules; for a smooth space they recover right modules over its operator sheaf, and for a singular space they recover the supported ambient category. The precise references are Beilinson–Drinfeld, §§7.10.3, 7.10.8, 7.10.11–7.10.14. On smooth ambient varieties, side-changing relates this formulation to the left categories used above.

For an algebraic stack locally of finite type, one defines objects by compatible families on a smooth scheme atlas and its iterated overlaps. Overlaps may be algebraic spaces; their categories are defined by the étale descent just described. Each possibly singular scheme chart has the intrinsic category constructed in Section 5. Transition functors are the unshifted smooth inverse images; where the relative dimension is $r$, their relation with our derived convention is $f^\natural=f^![-r]$. Objects carry transition isomorphisms satisfying the identity and triple-overlap cocycle conditions, and morphisms respect them. The smooth descent formalism for these intrinsic categories is stated here from BD §1.1.7. This specifies the classical category on a nonsmooth stack; the derived stack category, its dimension normalizations and the de Rham prestack require the later lesson on stacks and ind-schemes.

## 7. Exercises and complete solutions

### Exercise 9.1 — Euler eigenvalues (easy)

Check the Euler eigenvalues of the normal derivative basis of $\delta_0$.

**Solution.** From $x\delta=0$ and $[x,\partial^j]=-j\partial^{j-1}$ we obtain
$x\partial^{j+1}\delta=-(j+1)\partial^j\delta$.
The left side is $(x\partial)\partial^j\delta$. Thus the eigenvalue on $\partial^j\delta$ is $-(j+1)$ for every $j\geq0$. The basis spans algebraically, so the eigenspaces are exactly their one-dimensional spans. In particular zero is not an Euler eigenvalue in this nonzero supported left module.

### Exercise 9.2 — the inverse image of a pushed point (easy)

Show directly that $i^!i_*=\mathrm{id}$ for the origin $i:\operatorname{Spec}k\hookrightarrow\mathbb A^1$, including the shift.

**Solution.** For a vector space $V$, $i_*V=k[\partial]\otimes V$, and $x$ acts as $-d/d\partial$. The complex for $Li^*$ is multiplication by $x$ in degrees $-1,0$. Polynomial integration proves its surjectivity and its kernel is $1\otimes V$. Thus $Li^*i_*V\simeq V[1]$. Since $i^!=Li^*[-1]$, the result is $V$ in degree zero. The inclusion of constant normal polynomials identifies this isomorphism with the unit of Theorem 3.1, so it is natural in $V$.

### Exercise 9.3 — all modules at the origin (medium)

Classify quasi-coherent $\mathcal D_{\mathbb A^1}$-modules set-theoretically supported at the origin, including maps and coherent objects.

**Solution.** Such a module has locally nilpotent $x$ by Section 1. Put $V=\ker x$. The projector (2.2) and expansion (2.3) give $M\simeq k[\partial]\otimes V$ with $x$ acting by negative polynomial differentiation. A differential-operator map preserves $V$ and is determined by its restriction to $V$, since it commutes with $\partial$. Conversely every linear map $V\to W$ extends to the indicated module map. Hence the category is equivalent to vector spaces. A basis of $V$ exhibits a direct sum of delta modules. The finite-generation argument in Section 3 proves that $M$ is coherent exactly when $\dim_kV<\infty$. Formula (3.6) gives characteristic variety the point's cotangent fiber. The associated graded is free of rank $\dim_kV$ on that fiber, so its generic length, and hence characteristic multiplicity, is $\dim_kV$. The coherent objects are holonomic. Infinite direct sums remain legitimate quasi-coherent modules, but are not coherent holonomic objects.

### Exercise 9.4 — simple objects on a smooth support (medium)

Show that simple holonomic modules supported on a smooth closed $Z\subset X$ correspond exactly to simple holonomic $\mathcal D_Z$-modules.

**Solution.** The equivalence and its inverse are exact. They therefore carry subobjects bijectively to subobjects and preserve nonzero objects. A nonzero object has no nonzero proper subobject on one side exactly when its image has none on the other. The characteristic dimension calculation (3.6) preserves and reflects holonomicity. Combining these two statements proves the assertion, including uniqueness of the source simple object up to isomorphism.

### Exercise 9.5 — a point in two ambient spaces (hard)

Construct the equivalence between modules supported at a point of $\mathbb A^1$ and modules supported at a point of $\mathbb A^2$ without using the general embedding-independence theorem.

**Solution.** Translate the points to the origins. For a line module take $V=\ker x$, and form $k[\partial_x,\partial_y]\otimes V$. Let the derivatives multiply the polynomial variables and let $x,y$ act by their respective negative derivatives. This is supported at the plane origin and satisfies the two Weyl relations. In the reverse direction, take $W=\ker x\cap\ker y$ of a plane module and form $k[\partial]\otimes W$ with the analogous line action. Formula (2.6) proves that these operations are inverse; their comparison maps send polynomial normal derivatives of the common kernel to the corresponding vectors. A map is determined by its restriction to the kernel, so the construction also gives an equivalence on morphisms. For the coordinate axis embedding $a:\mathbb A^1\hookrightarrow\mathbb A^2$, the forward operation is $a_*$ restricted to point-supported modules, and projection back is its inverse by the computation of a delta module's direct image to a point. This matches the canonical projection comparison of Section 5.

### Exercise 9.6 — powers of a normal equation (medium)

For $m\geq1$, compute the supported left module $A_1/A_1x^m$. Explain why insensitivity to a nilpotent thickening does not say that $x$ acts as zero.

**Solution.** Let $v$ be its generator. PBW gives a basis $\partial^b x^av$ with $b\geq0$ and $0\leq a<m$. The relation $x^mv=0$ and the commutator formula show that a sufficiently high power of $x$ kills every basis vector, so the module is supported at the origin. Write a general vector as
$\sum_{a=0}^{m-1}h_a(\partial)x^av$. Multiplication by $x$ gives the kernel equations
\[
h_0'=0,\qquad h_a'=h_{a-1}\quad(1\leq a<m).
\]
Their polynomial solutions are
\[
h_a(\partial)=\sum_{j=0}^a c_j\,\frac{\partial^{a-j}}{(a-j)!}.
\]
Thus $\ker x$ has dimension $m$, with independent vectors
\[
v_j=\sum_{a=j}^{m-1}
\frac{\partial^{a-j}}{(a-j)!}x^av,\qquad 0\leq j<m.
\]
Theorem 3.1 gives $A_1/A_1x^m\simeq\delta_0^{\oplus m}$. Normal multiplication is still nonzero on, for example, $\partial v_j$, since $x\partial v_j=-v_j$. The category depends on the reduced support; its individual objects retain their normal-derivative actions.

## What this lesson does not prove

The comparison between BD right D-crystals and intrinsic supported modules on arbitrary complex algebraic spaces is stated from §§7.10.8, 7.10.11–7.10.14. The smooth descent formalism used to define the classical category on nonsmooth algebraic stacks is stated from §1.1.7. The derived category of a stack and the full de Rham-prestack formalism are reserved for the later stacks lesson.

Quasi-coherent étale descent and the standard étale presentation theorem used in Section 5 are algebraic-geometric prerequisites. The two central theorems here, Kashiwara's equivalence and canonical independence of a smooth ambient embedding, were proved without importing the crystal comparison.

## References

Victor Ginzburg, [*Lectures on D-modules*, §§3.3.13–3.3.15 and Corollary 3.3.26](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), discusses Kashiwara, singular ambient support and characteristic varieties. Dragan Miličić, [*Lectures on Algebraic Theory of D-Modules*, Chapter I, Lemma 12.2 and Corollaries 12.3–12.4, pp. 50–51](https://www.math.utah.edu/~milicic/Eprints/hk_chapter1.pdf), gives the affine hyperplane argument. Christian Schnell, [*D-modules*, Theorem 13.12 and Lecture 14, pp. 66–68](https://www.math.stonybrook.edu/~cschnell/pdf/notes/d-modules.pdf), uses right modules, whose Euler eigenvalues differ from the left eigenvalues in (2.5) by transposition.

Beilinson and Drinfeld, [*Quantization of Hitchin's integrable system and Hecke eigensheaves*, §1.1.7 and §7.10](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf), give the nonsmooth-stack and right D-crystal formulations. The ordinary-pullback crystal terminology is in [Stacks, Tag 07IR](https://stacks.math.columbia.edu/tag/07IR) and its preceding definition and lemma.
