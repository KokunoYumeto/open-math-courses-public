# Preservation of holonomicity and minimal extensions

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A holonomic system has the smallest possible characteristic dimension. Its equations may acquire poles under localization, and its direct image may acquire cohomology, but each resulting differential-operator module still has that same minimal dimension relative to its new ambient variety. We prove this preservation before using it to extend a connection across a boundary with no extra submodule or quotient on that boundary.

The field has characteristic zero. Geometric classification is over an algebraically closed field. All varieties are smooth and separated, and modules are quasi-coherent over their structure sheaves. We use $f^!=Lf_{\mathcal O}^*[d_X-d_Y]$ and the direct-image convention of Direct images and the relative de Rham complex. The prerequisites are Bernstein-Sato polynomials and Adjunctions, base change and the projection formula.

## 1. Localization without losing finite generation

**Proposition 1.1.** If $M$ is holonomic and $g$ is a regular function, then $M_g=M[g^{-1}]$ is holonomic as a module on the original ambient variety. The zero localization is allowed.

**Proof on affine space.** Let $M$ be a holonomic $A_n$-module, with a good Bernstein filtration $F_\bullet M$. Put $d=\deg g$ when $g\ne0$. Inside $M_g$ define
\[
E_p=g^{-p}F_{(d+1)p}M,\qquad p\ge0.
\tag{1.1}
\]
Multiplication by $g$ shows $E_p\subset E_{p+1}$. Any fraction $g^{-a}m$ eventually lies in this filtration: if $m\in F_qM$, rewrite it as $g^{-p}g^{p-a}m$, and take $p\ge a$ and $q+d(p-a)\le(d+1)p$.

Both coordinate multiplication and differentiation raise the index by at most one. For example,
\[
\partial_i(g^{-p}m)
 =g^{-(p+1)}
   \bigl(g\partial_i m-p(\partial_i g)m\bigr).
\tag{1.2}
\]
The numerator is in $F_{(d+1)(p+1)}M$; coordinate multiplication has numerator $g x_i m$ with the same bound. Thus $E$ is exhaustive and compatible with the Bernstein filtration. Since $M$ is holonomic,
\[
\dim_k E_p\le \dim_k F_{(d+1)p}M=O(p^n).
\tag{1.3}
\]
The inequality accounts for elements killed by localization. The growth criterion proved in the Bernstein-Sato lesson applies even before finite generation of $M_g$ is known: an exhaustive compatible finite-dimensional filtration with this bound forces finite generation and holonomicity. It proves the result. For $g=0$ the localization is zero.

**Proof on a smooth variety.** Work on a smooth affine chart $X$, embed it closed in $\mathbb A^m$, and extend $g$ to a polynomial $G$ on that affine space. Kashiwara gives a holonomic module $i_*M$ on $\mathbb A^m$. Composition and the principal-open direct-image formula identify its localization at $G$ with $i_*(M_g)$: on the open loci this is closed/open base change, and direct image back to the ambient varieties is composition. The affine-space result makes $i_*(M_g)$ holonomic, and Kashiwara reflects coherence and holonomicity. The result is local on $X$, so these conclusions glue. $\square$

In particular, localization can remove a point-supported submodule altogether. It is incorrect to replace (1.3) by equality for an arbitrary holonomic input.

## 2. Inverse images, including characteristic embeddings

**Theorem 2.1.** Every morphism of smooth varieties preserves holonomic complexes under $f^!$.

**Proof.** First take a smooth closed embedding $i:Z\hookrightarrow X$. On an affine chart, choose finitely many generators of its ideal. The localization Čech complex of the complement uses finite sums of modules $M_{g_{a_1}\cdots g_{a_s}}$. Each is holonomic by Proposition 1.1. Its cohomology, and the cohomology of its augmentation cone, are holonomic because submodules, quotients and extensions preserve holonomicity.

The localization triangle proved in the preceding lesson identifies this cone, with its indicated shift, with $i_*i^!M$. Closed direct image is exact. Hence each $i_*H^q(i^!M)$ is holonomic, and Kashiwara's characteristic-dimension comparison implies that $H^q(i^!M)$ is holonomic on $Z$. This proves the assertion for modules and then bounded complexes by their cohomology truncations.

Smooth inverse image preserves holonomicity by the smooth characteristic-support formula proved in Inverse images; its shift does not affect holonomicity. Finally factor any $f:X\to Y$ through its closed graph $X\hookrightarrow X\times Y$ and the smooth projection to $Y$. Composition proves the theorem. $\square$

No noncharacteristic hypothesis entered the closed case. For instance, pulling a delta module back along its own point support gives nonzero normal Koszul cohomology, with $i^!\delta=k$ rather than an ordinary unshifted fiber.

## 3. One-dimensional integration and general direct image

Before making a global reduction, we prove the relative one-coordinate statement. This proves coherence as well as minimal characteristic dimension; finiteness of individual fibers alone would not establish it.

**Lemma 3.1.** For $p:\mathbb A^{n+1}\to\mathbb A^n$ forgetting $x_0$, the two cohomology modules of $p_*M$ are holonomic whenever $M$ is holonomic.

**Proof.** Define a partial Fourier change of the left Weyl action on the same vector space:
\[
x_0\cdot_{\mathrm F}m=\partial_0m,\qquad
\partial_0\cdot_{\mathrm F}m=-x_0m,
\tag{3.1}
\]
and keep all other coordinates and derivatives unchanged. The relation is correct because $[-x_0,\partial_0]=1$. This is an invertible automorphism of the Weyl algebra. It preserves the Bernstein filtration: its images of generators have degree one. A good Bernstein filtration on $M$ is therefore good on $\mathrm F M$, with the same growth degree. Thus $\mathrm F M$ is holonomic. This algebraic device is developed further in the final course lesson; the short verification here is all we need.

The relative de Rham complex for $p$ is
\[
[M\xrightarrow{\partial_0}M][1],
\tag{3.2}
\]
whose terms are in degrees $-1,0$ after identifying the last term with $M\,dx_0$. For $i:\mathbb A^n\hookrightarrow\mathbb A^{n+1}$ at $x_0=0$, ordinary derived pullback of $\mathrm F M$ is
\[
Li_{\mathcal O}^*(\mathrm F M)
 =[\,\mathrm F M\xrightarrow{x_0}\mathrm F M\,],
\tag{3.3}
\]
in those same degrees. The operators on the remaining $n$ variables are unchanged. By (3.1), (3.2) and (3.3) are the same $A_n$-complex. Theorem 2.1 says that $i^!\mathrm F M=Li_{\mathcal O}^*\mathrm F M[-1]$ is holonomic, so the same holds after undoing that shift. This proves the lemma. $\square$

For $n=0$, this is a complete finiteness proof:
\[
\dim_k\ker(\partial:M\to M)<\infty,\qquad
\dim_k(M/\partial M)<\infty
\tag{3.4}
\]
for every holonomic $A_1$-module. They are holonomic modules on a point, which means finite-dimensional vector spaces by the point case of Kashiwara. The argument includes irregular connections and point-supported modules. It does not compare the kernel or cokernel with those of the principal symbol: that comparison need not preserve finiteness.

**Theorem 3.2.** Differential-operator direct image preserves bounded holonomic complexes for every morphism of smooth separated varieties. In particular it does so in the assigned quasi-projective case.

**Proof for affine source and target.** Embed $X$ closed in $\mathbb A^a$ and $Y$ closed in $\mathbb A^b$. The graph and the two embeddings give a closed embedding
$e:X\hookrightarrow\mathbb A^a\times\mathbb A^b$
such that $q e=i_Y f$, where $q$ is the projection to $\mathbb A^b$. Kashiwara makes $e_*M$ holonomic. Factor $q$ into $a$ one-coordinate projections. Lemma 3.1 at each step, and bounded cohomology spectral sequences, make $q_*e_*M$ holonomic. Composition identifies it with $i_{Y,*}f_*M$. Kashiwara reflects holonomicity, giving the assertion on $Y$.

**Proof in general.** Restrict to an affine open in $Y$. Cover its inverse image in $X$ by finitely many affine opens. All their finite intersections are affine, because $X$ is separated. The restriction modules on these intersections are holonomic. The finite Čech resolution of $M$ has terms their open direct images. These open embeddings are affine: their inverse images of affine opens are intersections of two affine opens in a separated scheme. Hence their quasi-coherent direct image is exact, and the Čech augmentation is also a resolution by differential-operator modules.

Apply $f_*$. By composition, the image of each term is the direct image along a morphism from a smooth affine intersection to the affine target. The first part has proved that all its cohomology is holonomic. The finite total complex therefore has holonomic cohomology. This proves the theorem for a module and then for bounded complexes by truncation. $\square$

This proof also establishes finite-dimensional algebraic de Rham cohomology for a holonomic module on any smooth curve: choose a finite affine cover, apply the affine proof to the map of each intersection to a point, and use its finite Čech totalization. On an affine curve the direct-image degrees are $-1,0$, giving finiteness of both the horizontal-section kernel and de Rham cokernel. On a nonaffine curve the Čech step can add degree $1$. In particular, the curve finiteness assertion required for projection arguments has been proved, rather than assumed.

Duality already preserves holonomic complexes. Consequently $f^*=\mathbb D f^!\mathbb D$ and $f_!=\mathbb D f_*\mathbb D$ preserve them too. This closes the category assumptions used for adjunctions in the preceding lesson.

## 4. The extension with no boundary pieces

Let $j:U\hookrightarrow X$ be a smooth locally closed embedding, and $N$ a holonomic module on $U$. Choose an open $V\subset X$ in which $U$ is closed; factor $j$ into the closed embedding in $V$ followed by the open embedding in $X$.

Closed direct image is exact, while open direct image is a right-derived sheaf functor. Therefore $j_*N$ has cohomology in degrees $\ge0$. Duality gives $j_!N$ degrees $\le0$. The adjunctions and $j^!j_*N=N$ give a canonical map $j_!N\to j_*N$, corresponding to $\mathrm{id}_N$. Define on the holonomic heart
\[
j_{!*}N=
\operatorname{im}\bigl(H^0j_!N\longrightarrow H^0j_*N\bigr).
\tag{4.1}
\]

On modules supported on $\overline U$, restriction to $V$ followed by Kashiwara's inverse is an exact functor to modules on $U$. It sends (4.1) to $N$. A boundary module means a module supported on $\overline U\setminus U$, so its restriction is zero.

**Theorem 4.1.** The module $j_{!*}N$ has no nonzero boundary submodule or quotient. It is the unique holonomic extension of $N$, supported on $\overline U$, with those two properties.

**Proof.** If $B$ is a boundary module, the adjunctions give
\[
\operatorname{Hom}(B,j_*N)=0,\qquad
\operatorname{Hom}(j_!N,B)=0,
\tag{4.2}
\]
because both inverse images of $B$ along $j$ vanish. The cohomological bounds just proved imply the same statements for $H^0j_*N$ and $H^0j_!N$. Indeed, the positive truncation of $j_*N$ and the negative truncation of $j_!N$ give zero degree-zero Hom against a heart object in the relevant direction, by the derived-category orthogonality axiom.

The image (4.1) is a submodule of the first and a quotient of the second. A boundary submodule would contradict the first vanishing; a boundary quotient would contradict the second.

Now take another such extension $K$. Adjunction produces
\[
H^0j_!N\longrightarrow K\longrightarrow H^0j_*N
\tag{4.3}
\]
restricting to the identity on $N$. The cokernel of the first map is a boundary quotient of $K$, and the kernel of the second is a boundary submodule of $K$, because restriction in the supported heart is exact. They are zero. Thus $K$ identifies with the image of their composite, which is (4.1). This also proves uniqueness compatible with the prescribed restriction. $\square$

The construction is functorial, and duality exchanges its two bounds and the canonical map. Thus
\[
\mathbb D_Xj_{!*}N\simeq j_{!*}\mathbb D_UN.
\tag{4.4}
\]
If $N$ is simple, a nonzero submodule of $j_{!*}N$ restricts either to zero or to all of $N$. The first case is prohibited; in the second its quotient is a boundary module and is prohibited. Hence $j_{!*}N$ is simple.

The image definition and its uniqueness have been proved directly in differential-operator modules.

## 5. Classification and the affine-line examples

**Theorem 5.1.** Every simple holonomic $\mathcal D_X$-module is $j_{!*}E$ for an irreducible integrable connection $E$ on a smooth irreducible locally closed subvariety. Its closed support is unique, and $E$ is unique after passing to a common smaller dense open in that support.

**Proof.** First observe that restricting a simple module to an open subset gives zero or a simple module. If a nonzero proper holonomic submodule $N$ existed in that restriction, the adjunction map $H^0j_!N\to M$ would be nonzero, hence surjective onto the simple $M$. Restriction would then say $N$ surjects onto the entire restricted module, a contradiction.

The support of a coherent differential-operator module is closed. Its good characteristic support is conic; projection to $X$ agrees with intersection with the zero section and is therefore closed. The good filtration identifies that projection with the support of the original module. Choose an irreducible component $Z$ of the support and remove the other components and the singular locus of $Z$. On the resulting nonempty open $V$, the module is supported on the smooth closed subvariety $Z\cap V$. Kashiwara writes it as the direct image of a holonomic module on $Z\cap V$.

The generic-connection theorem from the duality lesson permits shrinking again so this module is a finite-rank bundle with integrable connection $E$. The preceding restriction argument and Kashiwara make $E$ simple. For a finite bundle with connection, every differential-operator submodule and its quotient are structure-sheaf coherent; the coherent-connection theorem makes them bundles. Thus simplicity means precisely irreducibility of the integrable connection.

The adjunction map $H^0j_!E\to M$ is nonzero on this restriction, so simplicity makes it surjective. Its source is supported on $Z$, which proves that the original support is exactly $Z$ and has only one irreducible component. The original simple $M$ now has no boundary submodule or quotient relative to this nonempty restriction: either would be a nonzero proper submodule or a nonzero quotient with zero restriction. Theorem 4.1 identifies $M$ with $j_{!*}E$. For any second description the closed support is the same. On the intersection of the two dense smooth opens, both connections are recovered by the same restriction and Kashiwara inverse, hence are isomorphic. Conversely Theorem 4.1 proves that every such irreducible connection has a simple minimal extension. $\square$

For $j:\mathbb G_m\hookrightarrow\mathbb A^1$ and
$\partial e=\lambda x^{-1}e$, put $E_\lambda=k[x,x^{-1}]e$.
If $\lambda\notin\mathbb Z$, then
\[
j_{!*}(E_\lambda|_{\mathbb G_m})
 =j_*E_\lambda=j_!E_\lambda
 \simeq A_1/A_1(x\partial-\lambda).
\tag{5.1}
\]
To see simplicity, $\theta=x\partial$ acts diagonally on $x^me$ with eigenvalues $\lambda+m$. Polynomial interpolation in $\theta$ extracts a single monomial from any nonzero finite Laurent sum. Multiplication by $x$ moves its exponent up, and differentiation moves it down with nonzero coefficient $\lambda+m$. Every nonzero submodule therefore contains every monomial. This proves simplicity and both no-boundary properties for the cyclic Laurent module computed in the inverse-image lesson. Duality has the same nonintegral property, so $j_!$ also equals this extension. For $\lambda=1/2$ over $\mathbb C$, the horizontal coefficient is $x^{-1/2}$ and monodromy is $-1$.

For integral $\lambda$, the connection on $\mathbb G_m$ is isomorphic to the trivial one by multiplication by an integral power of $x$, and its minimal extension is
\[
j_{!*}\mathcal O_{\mathbb G_m}=\mathcal O_{\mathbb A^1}.
\tag{5.2}
\]
The polynomial module is simple: a nonzero derivative-stable ideal contains a polynomial of minimal degree; differentiating it forces that degree to be zero. Its support is not a point, so simplicity gives both boundary conditions. In contrast $j_*\mathcal O$ and $j_!\mathcal O$ have the two distinct length-two extensions computed previously.

A simple module on the affine line whose singular set is contained in $\{0\}$ is either the point module $\delta_0$, or the minimal extension of an irreducible connection on $\mathbb G_m$. This is a description, rather than a finite list of Euler modules. Connections of higher rank or with irregular behavior are permitted. Even the nonsingular rank-one connection $A_1/A_1(\partial-1)$ belongs to the class and is simple: tensoring by this invertible connection is an equivalence taking the simple polynomial connection to it. The point module is simple because repeated multiplication by $x$ differentiates a nonzero polynomial in its normal derivative variable down to its constant coefficient, after which normal derivatives generate everything.

## 6. Exercises

**Exercise 11.1 (easy).** Show $j_*\mathcal O_{\mathbb G_m}\ne j_{!*}\mathcal O_{\mathbb G_m}$.

**Exercise 11.2 (easy).** Compute $j_{!*}E_\lambda$ for $\lambda\notin\mathbb Z$, including its cyclic relation and simplicity.

**Exercise 11.3 (medium).** Prove $H^0p_*M$ is finite-dimensional for every holonomic module on $\mathbb A^1$. Also treat $H^{-1}p_*M$, and explain why the principal-symbol cokernel does not suffice.

**Exercise 11.4 (medium).** Prove $j_{!*}$ preserves injections and surjections. Exhibit a short exact sequence on $\mathbb G_m$ whose minimal extensions fail to be exact in the middle.

**Exercise 11.5 (hard).** Localize
$M=A_2/(A_2\partial_x+A_2\partial_y)$
at $g=xy$. Give a generator, the localization growth bound, a cyclic presentation and the characteristic cycle.

## 7. Solutions

**Solution 11.1.** The direct image is $L=k[x,x^{-1}]$.
Its polynomial submodule has quotient with basis $[x^{-r}]$, $r\ge1$, identified with $\delta_0$ by
$\partial^{r-1}\delta_0\mapsto(-1)^{r-1}(r-1)![x^{-r}]$.
Thus $L$ has a nonzero boundary quotient. The minimal extension is the simple polynomial module (5.2), so the two modules differ.

**Solution 11.2.** In the cyclic quotient by $\theta-\lambda$, the normal forms are $x^av$, $a\ge0$, and $\partial^bv$, $b\ge1$. They map to $x^ae$ and
$\lambda(\lambda-1)\cdots(\lambda-b+1)x^{-b}e$.
The coefficients are nonzero for nonintegral $\lambda$, so this is a basis isomorphism with the Laurent connection. Its Euler eigenvalues are distinct. Interpolation followed by coordinate multiplication and differentiation proves simplicity exactly as in Section 5. Therefore there is no boundary submodule or quotient, and Theorem 4.1 gives (5.1).

**Solution 11.3.** The affine Spencer complex has only
$H^{-1}=\ker\partial$ and $H^0=\operatorname{coker}\partial$.
Apply (3.1) for $n=0$. Both are cohomology modules of $Li_{\mathcal O}^*\mathrm F M$. The inverse-image theorem proves they are holonomic on the point, hence finite-dimensional. This uses the localization growth bound and supported characteristic comparison that proved that theorem. For a concrete warning about symbols, take $M=k[x]$ with its good Bernstein filtration. Differentiation lowers polynomial degree; the degree-one derivative symbol therefore acts by zero on the associated graded. Its cokernel is all of $k[x]$, infinite-dimensional, even though actual differentiation is surjective and has zero cokernel.

**Solution 11.4.** Given an injection $N_1\to N_2$, the kernel of the induced map $j_{!*}N_1\to j_{!*}N_2$ has zero restriction, and is therefore a boundary submodule of $j_{!*}N_1$. It vanishes. Given a surjection $N_2\to N_3$, the cokernel of the induced map is a boundary quotient of $j_{!*}N_3$, so it vanishes. These arguments use exact restriction in the supported holonomic heart.

For failure of exactness in the middle, take the rank-two connection
\[
E=k[x,x^{-1}]e_0\oplus k[x,x^{-1}]e_1,\qquad
\partial e_0=0,\quad \partial e_1=x^{-1}e_0.
\tag{7.1}
\]
It fits into $0\to\mathcal O_{\mathbb G_m}e_0\to E\to\mathcal O_{\mathbb G_m}\to0$.
Inside its Laurent direct image, the module generated by $e_1$ is
\[
I=k[x,x^{-1}]e_0\oplus k[x]e_1.
\tag{7.2}
\]
Indeed $x\partial e_1=e_0$; differentiating $e_1$ generates all negative powers of $x$ times $e_0$, and multiplication generates the remaining indicated terms. It is stable under the connection differential.

More explicitly,
$I=A_1/A_1(\partial x\partial)$.
The relation gives
$x\partial^rv=-(r-1)\partial^{r-1}v$ for $r\ge2$.
It reduces PBW monomials to $x^av$ ($a\ge0$),
$x^a\partial v$ ($a\ge1$), and $\partial^rv$ ($r\ge1$).
Their images in (7.2) are respectively the polynomial $e_1$ terms, nonnegative-power $e_0$ terms, and distinct negative-power $e_0$ terms with nonzero factorial coefficients. Hence they form a basis, proving the presentation.

The characteristic variety of this cyclic module is the curve
$x\xi^2=0$, so it is holonomic. It has no point-supported submodule because $x$ is invertible on the surrounding Laurent connection. Its formal adjoint relation is again $\partial x\partial$, so the cyclic dual calculation makes $I$ self-dual. It has no boundary quotient either. Theorem 4.1 therefore gives $I=j_{!*}E$.

Applying minimal extension to (7.1) gives an injective map
$\mathcal O e_0\to I$ and a surjective map $I\to\mathcal O$.
The map on the right extracts the polynomial $e_1$ coefficient. Its kernel is $k[x,x^{-1}]e_0$, whereas the image on the left is only $k[x]e_0$. Their quotient is $\delta_0$. Thus exactness fails at the middle term, despite preserving the injection and surjection.

**Solution 11.5.** The quotient $M$ is $k[x,y]$ with its ordinary derivatives. Localization is $k[x^{\pm1},y^{\pm1}]$. The vector $u=(xy)^{-1}$ generates it: mixed derivatives give
\[
\partial_x^a\partial_y^bu
 =(-1)^{a+b}a!b!\,x^{-a-1}y^{-b-1},
\tag{7.3}
\]
and multiplication supplies every other Laurent monomial. Equivalently
$\partial_x\partial_y(xy)^{-r}=r^2(xy)^{-r-1}$ for $r\ge1$.

For the explicit growth step in (1.1), $d=2$ and
$E_p=(xy)^{-p}F_{3p}k[x,y]$.
Multiplication by the nonzero fraction is injective here, so
$\dim E_p=\binom{3p+2}{2}=O(p^2)$.
Formula (1.2) and its multiplication counterpart show compatibility. The growth criterion proves holonomicity and finite generation independently of the displayed generator.

The two independent one-variable Laurent presentations give
\[
M_{xy}\simeq
A_2/\bigl(A_2(x\partial_x+1)+A_2(y\partial_y+1)\bigr).
\tag{7.4}
\]
Indeed $A_2=A_{1,x}\otimes_k A_{1,y}$, and tensoring the two cyclic basis isomorphisms gives exactly (7.3). The external good order filtration has associated graded
$k[x,y,\xi,\eta]/(x\xi,y\eta)$.
Its four components are
\[
\{\xi=\eta=0\},\quad
\{x=\eta=0\},\quad
\{y=\xi=0\},\quad
\{x=y=0\}.
\tag{7.5}
\]
Each has dimension two and generic length one: at its generic point the other two coordinates are invertible and the two equations reduce to the two defining coordinate equations. Thus the characteristic cycle is the sum, with coefficient one, of the zero section and the conormals to the two axes and their intersection. Tensoring the two length-two sequences for one-variable Laurent modules also gives a length-four filtration with the four corresponding simple factors. This agrees with the characteristic calculation and does not replace it by Bernstein multiplicity.

## 8. What this lesson does not prove

The algebraic-geometric tools used for affine covers and closed affine-space embeddings are prerequisites. The filtered growth criterion, duality on holonomic modules, generic-connection theorem, transfer composition and Kashiwara equivalence are the earlier proved course results explicitly cited above. No Riemann–Hilbert or regular-singularity theorem is used.

Localization, preservation by both inverse and direct image, curve de Rham finiteness, minimal-extension uniqueness, simplicity and classification, and every exercise calculation have been proved in this lesson.

## References

- C. Schnell, [*Algebraic D-modules*](https://www.math.stonybrook.edu/~cschnell/pdf/notes/d-modules.pdf), Theorem 18.5 and Lecture 19, Lemmas 19.1, 19.4–19.6: preservation and the Weyl-algebra reduction.
- A. Beilinson and V. Drinfeld, [*Quantization of Hitchin's integrable system and Hecke eigensheaves*](https://www.math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf), freely accessible author draft, Sections 7.2.8–7.2.11 and 7.3.6–7.3.10: the direct-image construction and composition conventions.
- V. Ginzburg, [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), freely accessible lecture notes, Sections 4.3.9–4.3.14 and Proposition 4.4.4: localization, inverse images and minimal extensions.
- P. Etingof, [*Introduction to algebraic D-modules*](https://math.mit.edu/~etingof/dmodwien.pdf), Exercise 3.20: the simple-module classification.
