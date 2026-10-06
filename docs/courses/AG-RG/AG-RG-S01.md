# Algebra and sheaf cohomology before reductive groups

*Written and self-checked by GPT-6.1 Sol (OpenAI), Codex, Ultra effort, October 2026. Draft. Original explanations are CC0. The explicitly identified programme proof reproduced in Section 6 retains its existing component terms.*

This supporting lesson supplies the algebra, affine sheaf correspondence, injective resolutions and finite-cover comparisons used by the reductive-group lessons. Rings are commutative with identity. A scheme means a locally ringed space covered by spectra of rings, with their localization structure sheaves; a quasi-coherent module means a sheaf locally obtained from a module. These are definitions, not vanishing or descent theorems. No Noetherian or finite-generation assumption is implicit.

## 1. The algebra of localization

For a multiplicative subset $S$ of a ring $A$, define $S^{-1}M$ by pairs $(m,s)$ with $(m,s)=(n,t)$ when $u(tm-sn)=0$ for some $u\in S$. Addition and scalar multiplication have the usual common-denominator formulas. The map $S^{-1}A\otimes_A M\to S^{-1}M$, $(a/s)\otimes m\mapsto am/s$, has inverse $m/s\mapsto (1/s)\otimes m$; the defining equivalence makes both maps well defined.

**Lemma 1.1.** Localization is exact. Filtered colimits of modules are exact. A module is zero if all its localizations at prime ideals are zero.

**Proof.** A fraction $m/s$ maps to zero precisely when some $u\in S$ kills the image of $m$. Replace $m/s$ by $um/(us)$ to lift it from the kernel. An element of the localization of an injected module maps to zero only when the same multiplier kills it in that module. Surjectivity is obtained by lifting the numerator. This proves exactness. In a filtered colimit every element is represented at one stage, and an equality between finitely many representatives holds at a common later stage. Applying these two facts to kernels and surjections proves exactness of filtered colimits. If $m\ne0$, its annihilator is a proper ideal. It lies in a maximal ideal $\mathfrak m$, by Zorn's lemma applied to proper ideals; then $m/1\ne0$ in $M_{\mathfrak m}$, since an element outside $\mathfrak m$ cannot annihilate $m$. This proves the last assertion. $\square$

A module is **flat** when tensoring with it preserves injections, and consequently short exact sequences, since tensor is right exact by its presentation as generators and bilinear relations. Exactness of localization proves that $S^{-1}A$ is flat. An exact functor preserves the kernel and image of a differential, so flat tensor commutes with the cohomology of every complex. Tensor commutes with finite sums and products because both are the same finite direct sum.

**Lemma 1.2 (Nakayama and local finite projectivity).** If $M$ is finitely generated and $M=JM$, then some $a\in J$ satisfies $(1-a)M=0$. If $J$ is contained in the Jacobson radical, $M=0$. A finitely presented flat module over a local ring is finite free; over any ring it is locally finite free.

**Proof.** Write generators $m_i$ as $m_i=\sum_j a_{ij}m_j$, with $a_{ij}\in J$. Multiply the matrix equation $(I-(a_{ij}))m=0$ by its adjugate. Its determinant is $1-a$ for $a\in J$, proving the first assertion. Elements $1-a$ are units when $J$ lies in every maximal ideal: otherwise a maximal ideal containing $1-a$ would contain one. This proves the second assertion.

Over a local ring $(A,\mathfrak m)$ lift a basis of $M/\mathfrak m M$ to obtain a surjection $A^r\to M$ by Nakayama. Its kernel $K$ is finite, by finite presentation. Flatness of $M$ makes $0\to K\otimes A/\mathfrak m\to (A/\mathfrak m)^r\to M/\mathfrak mM\to0$ exact: tensor the presentation and use preservation of kernels in a free presentation, equivalently resolve the last module by free modules and use exact flat tensor. The last map is an isomorphism, so $K/\mathfrak mK=0$. Nakayama gives $K=0$. For a prime of a general ring the same argument applies after localization. The resulting basis and its inverse use finitely many elements, relations and denominators; clearing their denominators gives a principal neighbourhood on which the presentation is free. This proves local finite freeness. $\square$

Here the elementary tensor-kernel assertion can be established without derived notation: if $0\to K\to F\to M\to0$ with $F$ free and $M$ flat, and $N$ is presented as $F_1\to F_0\to N\to0$ with the $F_i$ free, lift a proposed kernel element to $K\otimes F_0$. Its image in $F\otimes F_0$ comes from $F\otimes F_1$. Its image in $M\otimes F_1$ maps to zero in $M\otimes F_0$; flatness identifies this kernel with the image of $M\otimes\ker(F_1\to F_0)$. Lift those elements to $F$, subtract them, and then lift the remaining element from $K\otimes F_1$. The proposed element was zero in $K\otimes N$.

**Lemma 1.3 (the Noetherian inputs).** A finitely generated algebra over a Noetherian ring is Noetherian. Submodules of finite modules over a Noetherian ring are finite.

**Proof.** For an ideal $I\subset A[x]$, the leading coefficients of elements of degree at most $d$ form an ascending sequence of ideals $L_d$ of $A$. This sequence stabilizes, and every $L_d$ before stabilization is finitely generated. Choose polynomials of the corresponding degrees whose leading coefficients generate these finitely many ideals. Given any polynomial in $I$, subtract suitable multiples of these chosen polynomials to cancel its highest term; for degrees above stabilization multiply the stabilized generators by powers of $x$. Induction on degree expresses it in the ideal of the finitely many chosen polynomials. Thus $A[x]$ is Noetherian. Iterate and take a quotient. For a submodule of $A^r$, projection to the last coordinate has image an ideal, and its kernel is a submodule of $A^{r-1}$. Induction and lifting ideal generators make the submodule finite. A finite module is a quotient of some $A^r$; apply the same statement to the inverse image of its submodule. $\square$

<a id="tor-calculus"></a>

**Lemma 1.A (Tor for arbitrary modules).** Let \(R\) be any commutative ring and \(M,N\) any modules. Choose a free resolution \(P_\bullet\to M\) by taking a free surjection onto the module and then onto each successive kernel, and define \(\operatorname{Tor}_i^R(M,N)=H_i(P_\bullet\otimes_R N)\). This definition is independent of the resolution, naturally symmetric in \(M,N\), and has the natural long exact sequence of a short exact sequence in either variable.

**Proof.**

For completeness, the resolution facts used here have the following algebraic proof. Given free resolutions \(P_\bullet\to M\) and \(P'_\bullet\to M'\) and a map \(M\to M'\), lift it to \(P_0\to P'_0\). If maps have been chosen through degree \(i-1\), the image of \(d(P_i)\) lies in the cycles of \(P'_{i-1}\), which are the image of \(P'_i\); freeness of \(P_i\) therefore supplies the next lift. Two such lifts are chain homotopic: after the homotopy has been chosen below degree \(i\), their degree-\(i\) difference minus the already prescribed homotopy term maps to zero under the next differential, and freeness lifts it to \(P'_{i+1}\). The same induction starts at degree zero because both lifts induce the same map on the augmentation. Tensoring preserves the homotopy identity. Thus induced homology maps are independent of the lifts, preserve compositions, and comparison maps between two resolutions of the same module are inverse on homology.

Let \(Q_\bullet\to N\) be another free resolution and form the first-quadrant double complex \(D_{p,q}=P_p\otimes_R Q_q\), with total differential \(d_P\otimes1+(-1)^p1\otimes d_Q\). Augmentation gives maps from its total complex to \(P_\bullet\otimes_R N\) and to \(M\otimes_R Q_\bullet\). Each is a homology isomorphism. Indeed, filter by the degree in the unaugmented direction. In the other direction each augmented row or column is exact because its fixed factor is free. To check the resulting homology assertion directly, start with the outermost nonzero component of a cycle in the augmented kernel and use this exactness to subtract a total boundary that removes that component; proceed to the next component. A chain in any fixed total degree has only finitely many components, so this process terminates. The same process applied to boundaries proves injectivity. The comparison maps just constructed make these two augmentation isomorphisms natural. Interchanging the two resolutions, with the sign \((-1)^{pq}\) on \(P_p\otimes_RQ_q\), consequently gives
\[
\operatorname{Tor}_i^R(M,N)\simeq\operatorname{Tor}_i^R(N,M).
\]
In particular Tor can be computed using a free resolution of either variable; a projective resolution works as well, since projectives are summands of free modules and the same lifting and exactness arguments apply.

For \(0\to N'\to N\to N''\to0\), tensoring in each degree with the free module \(P_i\) gives a short exact sequence of complexes. If a cycle in the quotient complex is lifted to the middle complex, its differential lies in the subcomplex and is a cycle there. Its homology class is independent of the lift and of the cycle representative: changing either changes that differential by a boundary. This defines the connecting map. The equations saying that a class maps to zero say precisely that one can subtract a boundary and lift it to the preceding complex; they prove exactness at each position. The construction commutes with maps of short exact sequences and gives
\[
\cdots\longrightarrow\operatorname{Tor}_i^R(M,N')
\longrightarrow\operatorname{Tor}_i^R(M,N)
\longrightarrow\operatorname{Tor}_i^R(M,N'')
\longrightarrow\operatorname{Tor}_{i-1}^R(M,N')\longrightarrow\cdots,
\]
ending in
\[
\operatorname{Tor}_1^R(M,N'')\longrightarrow M\otimes_RN'
\longrightarrow M\otimes_RN\longrightarrow M\otimes_RN''\longrightarrow0.
\]
Balance gives the corresponding sequence in the first variable. These arguments require neither Noetherianity nor finite generation. \(\square\)

## 2. Modules on an affine scheme

**Lemma 2.1 (the principal-cover calculation).** If $f_1,\ldots,f_r$ generate the unit ideal in $A$, the augmented alternating complex

$$
0\longrightarrow M\longrightarrow\prod_i M_{f_i}
\longrightarrow\prod_{i<j}M_{f_if_j}\longrightarrow\cdots
$$

is exact for every $A$-module $M$.

**Proof.** Localize at $f_a$. Regard an ordered cochain as alternating, with repeated indices zero. Inserting $a$ as its first index defines a homotopy $h$ lowering degree, including projection to $M_{f_a}$ in degree zero. Every extra denominator $f_a$ is already a unit. Expanding the alternating differential gives $dh+hd=1$. The localized augmented complex is contractible. Localization commutes with its finite products and its cohomology by Lemma 1.1. If an element of a cohomology module vanishes at every $f_a$, powers $f_a^{n_a}$ all kill it. These powers generate one: an ideal they generate, if proper, lies in a maximal ideal containing every $f_a$, contradicting the unit-ideal hypothesis. A linear combination equal to one kills the element. Thus the original cohomology is zero. $\square$

The opens $D(f)$ form a basis of $\operatorname{Spec}A$. A collection of them covers precisely when its elements generate one: a proper generated ideal lies in a maximal ideal, and otherwise a finite linear combination already equals one. This also proves quasi-compactness and existence of finite principal refinements of arbitrary open covers.

Define $\widetilde M$ on this basis by $\widetilde M(D(f))=M_f$. The first three terms of Lemma 2.1 give the sheaf gluing axiom on every finite principal cover. An arbitrary cover has a finite principal refinement, so these basis values extend to a sheaf, uniquely. Its stalk at $\mathfrak p$ is $M_{\mathfrak p}$. Exactness of localization therefore makes $M\mapsto\widetilde M$ exact.

**Proposition 2.2 (affine module-sheaf correspondence).** Every quasi-coherent module on $\operatorname{Spec}A$ is $\widetilde M$ for $M=\Gamma(\operatorname{Spec}A,\mathcal F)$. Maps between associated sheaves correspond bijectively to module maps. In particular taking sections on the affine is exact on quasi-coherent modules.

**Proof.** Choose a finite principal cover $D(f_i)$ on which $\mathcal F$ is associated to an $A_{f_i}$-module $M_i$. Restrictions on the overlaps identify $(M_i)_{f_j}$ with $(M_j)_{f_i}$ and satisfy the cocycle equations. Put

$$
M=\ker\left(\prod_i M_i\longrightarrow\prod_{i<j}(M_i)_{f_j}\right),
$$

where the arrow is the difference after these identifications. The sheaf axiom identifies $M$ with the global sections. Localize this finite kernel diagram at $f_a$. Its cover now has a member equal to the whole spectrum. Compatibility then says that every tuple is uniquely determined by its $a$-th component, and every such component supplies the other components by restriction and the overlap identifications. Thus $M_{f_a}\simeq M_a$. The associated sheaf is therefore isomorphic to $\mathcal F$ on this cover, compatibly on overlaps, and hence globally. A sheaf map gives a map of global sections; on each $D(f)$ its action is the localization of that map, since a fraction $m/f^n$ must map to its image divided by $f^n$. Conversely localizing a module map defines a sheaf map. These operations are inverse. Exactness of associated sheaves and the equivalence prove exactness on global sections. $\square$

Kernels, images and cokernels of maps between quasi-coherent modules are quasi-coherent: on an affine they are the corresponding module operations by Proposition 2.2, and exactness can be checked on stalks. Closure under extensions is proved after affine vanishing in Section 5. Localization also identifies pullback along $A\to B$ with $\widetilde{M\otimes_A B}$.

**Proposition 2.3 (maps into an affine).** For any locally ringed space $X$, maps $X\to\operatorname{Spec}A$ correspond bijectively to ring maps $A\to\Gamma(X,\mathcal O_X)$.

**Proof.** From a ring map $\phi$ send $x$ to the inverse image of $\mathfrak m_x$ under $A\to\mathcal O_{X,x}$. This is prime. The inverse image of $D(a)$ is the open set where $\phi(a)$ is a unit in the local ring; a local inverse exists on a neighbourhood, so this set is open. On it the universal property of localization defines $A_a\to\Gamma(X_{\phi(a)},\mathcal O_X)$. The maps agree on intersections and define the sheaf map. The stalk maps are local by the definition of the image prime. Conversely locality forces that image prime, and localization forces each basis sheaf map; hence the construction is unique. It recovers $\phi$ on global sections and is inverse to taking global sections. $\square$

## 3. Injectives, resolutions and extensible sections

An object is **injective** when a map to it extends across every injection. We supply the existence assertions used to define cohomology.

**Lemma 3.1.** Module categories and sheaf-module categories have enough injectives. An injective sheaf restricts to an injective on every open and is flasque, meaning that every restriction of sections is surjective.

**Proof.** First $\mathbf Q/\mathbf Z$ is injective as an abelian group. Indeed a map from a subgroup can be extended one new generator at a time: if the first positive multiple $n a$ lying in that subgroup exists, choose a preimage under multiplication by $n$, which is surjective in $\mathbf Q/\mathbf Z$; if none exists choose the image arbitrarily. This defines the extension to the subgroup plus $\mathbf Za$. Zorn's lemma makes the extension global. The same argument shows that homomorphisms to $\mathbf Q/\mathbf Z$ separate nonzero elements, by first mapping their cyclic subgroup nontrivially.

For any ring $R$, the module $E=\operatorname{Hom}_{\mathbf Z}(R,\mathbf Q/\mathbf Z)$ is injective, with $(r\lambda)(s)=\lambda(rs)$: evaluation at one identifies $\operatorname{Hom}_R(N,E)$ with $\operatorname{Hom}_{\mathbf Z}(N,\mathbf Q/\mathbf Z)$. Map $N$ into the product of copies of $E$ indexed by its additive characters, sending $n$ in the character-$\lambda$ component to $r\mapsto\lambda(rn)$. Separation makes the map injective. Products of injectives are injective because extension can be made component by component.

For a ringed space choose, for each point $x$, an injection $\mathcal F_x\hookrightarrow E_x$ into an injective $\mathcal O_{X,x}$-module. The sheaf $i_{x*}E_x$ has sections $E_x$ on an open containing $x$, zero otherwise, and the induced ring action. The adjunction

$$
\operatorname{Hom}_{\mathcal O_X}(\mathcal G,i_{x*}E_x)
=\operatorname{Hom}_{\mathcal O_{X,x}}(\mathcal G_x,E_x)
$$

and exactness of stalks make it injective. The natural map $\mathcal F\to\prod_xi_{x*}E_x$ is injective: projecting its stalk at $x$ to the $x$-component recovers the chosen injection. Thus sheaf modules have enough injectives.

For an open immersion $j:U\hookrightarrow X$, extension by zero $j_!$ is an exact left adjoint to restriction; its stalks are unchanged on $U$ and zero outside. Adjunction makes restriction preserve injectives. To extend a section of an injective $\mathcal I$ from $U$ to $V$, use the injection $j_!\mathcal O_U\to\mathcal O_V$. Homomorphisms from these two modules to $\mathcal I|_V$ are exactly sections on $U$ and $V$. Injectivity gives the desired extension. $\square$

Repeatedly embed a sheaf and its successive cokernels into injectives. This gives an exact resolution $0\to\mathcal F\to\mathcal I^0\to\mathcal I^1\to\cdots$. Define $H^q(U,\mathcal F)$ as the cohomology of its section complex. A map between sheaves extends to a chain map between resolutions: after degrees below $n$ have been treated, exactness makes the required degree-$n$ map well defined on the image of the previous differential, and target injectivity extends it. Two extensions are homotopic by the same induction, applied to their difference. This proves independence of resolutions and naturality. For a short exact sequence, choose injectives for the two end terms and extend into their direct sum; iterating on cokernels produces a degreewise split short exact sequence of resolutions. Taking sections and lifting cocycles then gives the long exact cohomology sequence, with its usual connecting map. These constructions prove the properties of derived cohomology needed here.

**Lemma 3.2 (flasque lifting and acyclicity).** In $0\to\mathcal A\to\mathcal B\to\mathcal C\to0$, if $\mathcal A$ is flasque, every section of $\mathcal C$ lifts to $\mathcal B$ on every open. If $\mathcal B$ is also flasque, so is $\mathcal C$. A flasque sheaf has zero positive cohomology on every open.

**Proof.** Choose local lifts of a given section and well order their covering opens. At a successor step the new lift and the already glued lift differ on their overlap by a section of $\mathcal A$. Extend that difference to the new open using flasqueness, correct its lift, and glue. At a limit step the compatible previous lifts glue by the sheaf axiom. This constructs the lift on the whole open. To extend a section of $\mathcal C$ from a smaller open, lift it to $\mathcal B$, extend there by flasqueness, and project. Finally embed a flasque sheaf into an injective. Its cokernel is flasque by the assertion just proved. Iterate. Every successive short exact sequence is exact on sections by the lifting assertion, so the section complex of this injective resolution is exact in positive degrees. $\square$

More generally a resolution by section-acyclic sheaves computes cohomology: writing its successive kernels, their long exact sequences identify the cohomology of its section complex degree by degree with the groups defined by an injective resolution. This dimension-shifting argument uses only finitely many kernels in each degree. Direct image sends flasque sheaves to flasque sheaves because its restriction maps are restrictions between inverse-image opens. Its higher direct images are the sheafification of $V\mapsto H^q(f^{-1}V,\mathcal F)$: both are obtained from the same section complexes, and passing to a stalk commutes with kernels and cokernels by exactness of filtered colimits. Consequently flasque sheaves are also direct-image-acyclic. Applying the acyclic-resolution comparison twice proves

$$
R\Gamma(Y,Rf_*\mathcal F)=R\Gamma(X,\mathcal F)
$$

for a sheaf in degree zero, with the actual scalar action induced by the ring map. The notation here denotes the resolution complexes up to quasi-isomorphism; the equality follows from their common section complex, not from a separate composition theorem.

## 4. Finite covers and the spectral-sequence calculation

For a finite open cover $U_1,\ldots,U_r$, set $U_I=\bigcap_{i\in I}U_i$ for increasing index tuples $I$, and let $j_I:U_I\to X$. The augmented sheaf complex of finite products $\prod_{|I|=p+1}(j_I)_*(\mathcal G|_{U_I})$ is exact. At $x$ choose $a$ with $x\in U_a$ and restrict to a neighbourhood contained in $U_a$. Inserting $a$ as the first index gives a homotopy, exactly as in Lemma 2.1; it works on that neighbourhood even for a boundary stalk of a direct image. This proves exactness on stalks.

Apply this complex to every term of an injective resolution. Restriction preserves injectives by Lemma 3.1; direct image under an open immersion preserves them because it is right adjoint to exact restriction. The augmented rows are finite exact rows of injectives. Their first injection splits; its cokernel is an injective direct summand, so induction splits the row. Thus taking sections leaves the rows exact. The section double complex

$$
C^{p,q}=\prod_{|I|=p+1}\Gamma(U_I,\mathcal I^q),
\qquad 0\le p<r,\quad q\ge0,
$$

with differential $d_C+(-1)^pd_I$, has total complex quasi-isomorphic to $\Gamma(X,\mathcal I^\bullet)$ by the horizontal-row calculation.

For precision we give the filtered-complex calculation used in both directions. Write $K=\operatorname{Tot}C$ and $F^pK^n=\bigoplus_{a\ge p}C^{a,n-a}$. For $s\ge1$ put

$$
Z_s^{p,q}=\{z\in F^pK^{p+q}:dz\in F^{p+s}K^{p+q+1}\},
\qquad
E_s^{p,q}=Z_s^{p,q}/\bigl(Z_{s-1}^{p+1,q-1}+dZ_{s-1}^{p-s+1,q+s-2}\bigr),
$$

with $Z_0^{p,q}=F^pK^{p+q}$. Both terms in the denominator lie in the numerator: their differentials lie in $F^{p+s}$ or are zero. The differential of a representative gives a well-defined map $d_s:E_s^{p,q}\to E_s^{p+s,q-s+1}$. If its class is zero, write $dz=a+db$ with $a\in Z_{s-1}^{p+s+1,q-s}$ and $b\in Z_{s-1}^{p+1,q-1}$. Replacing $z$ by $z-b$ raises the filtration of its differential by one. Conversely every such raised cycle lies in the kernel. Quotienting also by the image of $d_s$ adds the boundaries with preimages in filtration $p-s$. These are precisely the numerator and denominator for $E_{s+1}$. Thus $E_{s+1}=H(E_s,d_s)$. At the first page this gives vertical cohomology, followed by the horizontal restriction differential.

The filtration has only $r$ pieces. For large $s$ its numerator consists of genuine cycles and its denominator consists of the next filtration of cycles plus all boundaries lying in $F^p$. Hence $E_\infty^{p,q}$ is the corresponding successive quotient of the filtration on $H^{p+q}(K)$. No infinite convergence assertion is being assumed. We have proved

$$
E_1^{p,q}=\prod_{|I|=p+1}H^q(U_I,\mathcal F)
\quad\Longrightarrow\quad H^{p+q}(X,\mathcal F).
$$

### 4.1. The general Leray comparison

**Theorem 4.1 (Leray).** For a morphism of ringed spaces $f:X\to Y$ and a sheaf of $\mathcal O_X$-modules $\mathcal F$, there is a first-quadrant spectral sequence

$$
H^p(Y,R^qf_*\mathcal F)\Longrightarrow H^{p+q}(X,\mathcal F).
$$

The $\mathcal O_Y$-action is induced by the given morphism of structure sheaves.

**Proof.** We give the double resolution used in this assertion. First, if $0\to A\to B\to C\to0$ is a short exact sequence of module sheaves and injective resolutions of $A$ and $C$ have been chosen, it has a compatible injective resolution of $B$ whose degree-$p$ term is the direct sum of their degree-$p$ terms. At degree zero extend the map $A\to I_A^0$ to $B\to I_A^0$ by injectivity and combine it with $B\to C\to I_C^0$. This map $B\to I_A^0\oplus I_C^0$ is injective: a vector killed by its second component belongs to $A$, where its first component is the chosen injection. Its cokernels form a short exact sequence
$0\to I_A^0/A\to(I_A^0\oplus I_C^0)/B\to I_C^0/C\to0$.
For the middle kernel calculation, subtract a lift in $B$ of the element of $C$ represented by the second coordinate; the remaining representative has second coordinate zero, and its ambiguity is exactly $A$. Repeat the construction on these cokernels. Composing each quotient with its next injection defines the differentials, and proves exactness and compatibility in every degree. The resulting short exact sequence of resolutions is split in each degree by its direct-sum description.

Now let $K^\bullet$ be any complex of sheaves in nonnegative degrees. Put $B^q=\operatorname{im}d^{q-1}$, $Z^q=\ker d^q$ and $H^q=Z^q/B^q$. Choose injective resolutions of the $B^q$ and $H^q$, taking $B^0=0$. Apply the preceding construction to $0\to B^q\to Z^q\to H^q\to0$ and then to $0\to Z^q\to K^q\to B^{q+1}\to0$. This gives resolutions $J^{\bullet,q}$ of $K^q$, with degreewise split exact sequences for both rows. Define their vertical differential by the composite
$$
J^{p,q}\longrightarrow I_B^{p,q+1}
\longrightarrow I_Z^{p,q+1}\longrightarrow J^{p,q+1}.
$$
Here the first arrow is the second resolution's quotient map and the other arrows are its compatible inclusions. Its square is zero because the quotient in the next degree kills the included $Z^{q+1}$. These are maps of resolutions, so the vertical and horizontal differentials commute. At fixed $p$, the vertical boundaries, cycles and cohomology are respectively $I_B^{p,q}$, $I_Z^{p,q}$ and $I_H^{p,q}$. All these sheaves are injective, and their short exact sequences split. Taking sections therefore preserves this description. Every term $J^{p,q}$ is injective, and the horizontal complexes resolve $K^q$.

Take an injective resolution $\mathcal I^\bullet$ of $\mathcal F$ on $X$ and apply this construction to $K^\bullet=f_*\mathcal I^\bullet$. Each $K^q$ is flasque, by Section 3, hence acyclic for sections on $Y$. The horizontal cohomology of $\Gamma(Y,J^{\bullet,q})$ is consequently $\Gamma(Y,K^q)$ in degree zero and zero in positive degrees. The corresponding filtration of the section double complex identifies its total cohomology with that of $\Gamma(Y,K^\bullet)=\Gamma(X,\mathcal I^\bullet)$, namely $H^*(X,\mathcal F)$.

For the other filtration, the split boundary and cycle sequences just constructed identify vertical cohomology with $\Gamma(Y,I_H^{p,q})$. Its horizontal cohomology is $H^p(Y,H^q(K^\bullet))$, since $I_H^{\bullet,q}$ resolves that sheaf. By the definition of higher direct image, $H^q(K^\bullet)=R^qf_*\mathcal F$. Use the same alternating-sign total differential and filtered-complex calculation given above. In each total degree only finitely many pairs $p,q\ge0$ occur, so the filtration is finite and converges to the stated total cohomology. This proves the claimed spectral sequence, including its target, without presuming a composition theorem. $\square$

## 5. Affine vanishing without a cited replacement proof

**Theorem 5.1.** For every ring $A$, every $A$-module $M$ and every $q>0$, $H^q(\operatorname{Spec}A,\widetilde M)=0$.

**Proof.** Induct on $q$, simultaneously for all rings and modules. A positive-degree cohomology class is locally zero: represent it by a cocycle in an injective resolution; exactness of the resolution as sheaves makes this cocycle a boundary on a neighbourhood of each point. Choose a finite principal cover on which the class is zero. Apply the spectral sequence of Section 4. Its intersections are principal affines with the localized module. For $q=1$ the kernel of restriction to the $E_1^{0,1}$ terms is the first filtration piece; the only possible term there is the positive-degree cohomology of the section complex in row zero, which is zero by Lemma 2.1. For general $q$, all rows $1,\ldots,q-1$ vanish by induction on those affine intersections. The row-zero positive cohomology is again zero by Lemma 2.1. A class restricting to zero on the covering members lies in filtration at least one, whose total-degree-$q$ successive quotients are therefore all zero. It is zero. This completes the induction. $\square$

**Corollary 5.2 (extensions remain quasi-coherent).** In an exact sequence of module sheaves $0\to\mathcal F_1\to\mathcal F_2\to\mathcal F_3\to0$, quasi-coherence of the two end terms implies quasi-coherence of the middle term.

**Proof.** Work on $X=\operatorname{Spec}A$. Theorem 5.1 and the long exact sequence give an exact sequence $0\to M_1\to M_2\to M_3\to0$ of their section modules. The same holds on every principal $D(f)$. Localize the first sequence and compare it with the latter. Proposition 2.2 identifies the two end modules with their localizations, so an elementary kernel-and-lift argument identifies $M_{2,f}$ with $\Gamma(D(f),\mathcal F_2)$: lift an element through the right term and correct its difference in the left term; the same diagram detects a zero element. These identifications commute with restriction, and therefore give $\widetilde M_2\simeq\mathcal F_2$. This is local on $X$ and proves the assertion. $\square$

For a separated scheme over an affine base, finite intersections of affine opens are affine: the closed diagonal pulls their affine product back to that intersection. Thus the row-zero section complex computes quasi-coherent cohomology by Section 4 and Theorem 5.1. For a quasi-compact quasi-separated scheme, intersections in a finite affine cover are quasi-compact separated opens of one affine member. Keep their cohomology in the spectral sequence instead of treating them as affine.

## 6. Flat base change and localization of quasi-coherent cohomology

**Statement.** Let $X$ be a quasi-compact quasi-separated scheme over $\operatorname{Spec}A$, let $\mathcal F$ be quasi-coherent, and let $B$ be any flat $A$-algebra. Write $g:X_B\to X$ for the projection and $\mathcal F_B=g^*\mathcal F$. For every $q\geq0$, the canonical map is an isomorphism

$$
H^q(X,\mathcal F)\otimes_A B
\longrightarrow H^q(X_B,\mathcal F_B).
$$

Theorem 5.1 above proves affine vanishing: for every ring $R$ and every $R$-module $M$, $H^q(\operatorname{Spec}R,\widetilde M)=0$ for $q>0$. Proposition 2.2 above proves the affine module-sheaf correspondence, and Sections 3-4 construct the injective and filtered-cover comparisons used in the proof. No finite generation, Noetherianity or finite presentation is assumed for $A$, $B$ or $\mathcal F$.

**The separated case and the ordered cover construction.**

First suppose that $X$ is separated over the affine base. Choose a finite affine open cover $U_1,\ldots,U_r$. For a strictly increasing tuple $I=(i_0<\cdots<i_p)$ put $U_I=U_{i_0}\cap\cdots\cap U_{i_p}$, and let $j_I:U_I\hookrightarrow X$. Empty intersections contribute zero. Every $U_I$ is affine: the intersection of two affine opens is the inverse image of their affine product under the closed diagonal, and induction gives the assertion for finite intersections.

We construct the cohomological comparison rather than assume that a section complex computes it. For any sheaf of modules $\mathcal G$, form the augmented alternating sheaf complex

$$
0\longrightarrow\mathcal G\longrightarrow
\mathcal C^0(\mathcal G)\longrightarrow\cdots\longrightarrow
\mathcal C^{r-1}(\mathcal G)\longrightarrow0,
\qquad
\mathcal C^p(\mathcal G)=\prod_{i_0<\cdots<i_p}(j_I)_*(\mathcal G|_{U_I}).
$$

The differential is the alternating sum of restriction maps. This complex is exact on stalks. Indeed, near a point $x$ choose $a$ with $x\in U_a$ and restrict to a neighbourhood $V\subset U_a$. Regard an ordered cochain as alternating in all its indices, with repeated-index components zero. The map lowering the degree is

$$
(hc)_{i_0\ldots i_{p-1}}=c_{a i_0\ldots i_{p-1}}.
$$

It is well defined because $V\cap U_I\cap U_a=V\cap U_I$. In degree zero it takes $c_a$ to a section on $V$, the augmented term. Expanding the alternating differential cancels all terms except $c$, so $dh+hd=1$, including the augmented degree. This proves exactness even when a direct-image stalk at a boundary point is nonzero.

Take an injective resolution $\mathcal F\to\mathcal I^\bullet$ in sheaves of $\mathcal O_X$-modules. Restriction to an open preserves injectives: its left adjoint, extension by zero, is exact, as one checks on stalks. Direct image under an open immersion also preserves injectives because it is right adjoint to exact restriction. Thus each term of the augmented sheaf complex for $\mathcal I^q$ is injective. Its first injection splits, and successive cokernels are injective direct summands; inductively the whole finite exact row splits. Applying global sections therefore leaves it exact.

Consequently the augmentation from $\Gamma(X,\mathcal I^\bullet)$ to the total complex of

$$
C^{p,q}=\prod_{i_0<\cdots<i_p}\Gamma(U_I,\mathcal I^q|_{U_I}),
\qquad 0\leq p<r,\quad q\geq0,
$$

is a quasi-isomorphism. Here the total differential is $d_{\mathrm{cover}}+(-1)^p d_{\mathrm{resolution}}$. Exactness of the augmented horizontal rows proves the assertion by the row filtration. Each total degree contains finitely many terms.

The column filtration $F^p\operatorname{Tot}^n=\bigoplus_{a\geq p}C^{a,n-a}$ gives the ordered-cover spectral sequence

$$
E_1^{p,q}=\prod_{i_0<\cdots<i_p}H^q(U_I,\mathcal F|_{U_I})
\quad\Longrightarrow\quad H^{p+q}(X,\mathcal F),
$$

with $d_1$ the alternating restriction differential. Explicitly, for $s\geq1$ set

$$
Z_s^{p,q}=\{z\in F^p\operatorname{Tot}^{p+q}:dz\in F^{p+s}\operatorname{Tot}^{p+q+1}\},
\qquad
E_s^{p,q}=\frac{Z_s^{p,q}}
{Z_{s-1}^{p+1,q-1}+dZ_{s-1}^{p-s+1,q+s-2}},
$$

where $Z_0^{p,q}=F^p\operatorname{Tot}^{p+q}$. The total differential induces $d_s:E_s^{p,q}\to E_s^{p+s,q-s+1}$, and taking its cohomology gives the next page. Extend the filtration by $F^p=\operatorname{Tot}$ for $p\leq0$ and $F^p=0$ for $p\geq r$. For sufficiently large $s$, the cycle condition is $dz=0$ and the denominator accounts for the next filtration piece and all boundaries lying in $F^p$. Thus the stable terms are the associated graded pieces of cohomology. There are only $r$ columns, so each abutment has a finite filtration and convergence involves no infinite-product or completion issue. This construction works for any finite open cover, including covers with non-affine intersections.

For our separated affine cover, affine vanishing makes every row with $q>0$ on $E_1$ zero. The augmentation therefore canonically identifies cohomology with that of the finite section complex

$$
\check C^p(\mathcal U,\mathcal F)=\prod_{i_0<\cdots<i_p}\Gamma(U_I,\mathcal F).
$$

If $U_I=\operatorname{Spec}R$ and $\mathcal F|_{U_I}=\widetilde M$, its base change has sections

$$
M\otimes_R(R\otimes_A B)=M\otimes_A B.
$$

These identifications commute with restriction. Tensor also commutes with the finite products, so the section complex on $X_B$ is the section complex on $X$ tensored with $B$. Flat tensor preserves kernels and images and hence cohomology. This proves the claimed isomorphism in the separated case.

**Canonical comparison and nonseparated intersections.**

To identify the preceding calculation with the canonical map and compare the general cover spectral sequences, choose an injective resolution $\mathcal F_B\to\mathcal J^\bullet$ on $X_B$. The projection $g$ is flat, so $g^*\mathcal I^\bullet$ is a resolution of $\mathcal F_B$. Target injectivity extends its identity on $\mathcal F_B$ degree by degree to a chain map $g^*\mathcal I^\bullet\to\mathcal J^\bullet$. The same extension argument makes any two choices chain homotopic. Pulling back sections and multiplying by elements of $B$ gives a map of augmented double complexes

$$
C^{p,q}(X,\mathcal I)\otimes_A B
\longrightarrow C^{p,q}(X_B,\mathcal J).
$$

Its augmentation is the usual cohomology base-change map; its column maps are the canonical comparisons on the intersections. It is independent of the resolution choices and compatible with restriction and successive base changes. Since $B$ is flat, the source total complex has cohomology $H^n(X,\mathcal F)\otimes_A B$. Flat tensor also commutes with the cycles, boundaries and finite sums defining every spectral-sequence page.

Now let $X$ be merely quasi-compact and quasi-separated. Choose a finite affine cover as before. Each $U_I$ is quasi-compact, by quasi-separatedness and finite intersection, and is separated over $\operatorname{Spec}A$, since it is an open subscheme of the affine $U_{i_0}$. It need not be affine. Apply the separated result to each $U_I$. It shows that every term of the comparison on $E_1$ is an isomorphism, for all $q\geq0$. Therefore every subsequent page and every associated graded piece of the abutment is an isomorphism. Induction through the finite filtrations gives an isomorphism of the abutments themselves. This proves the statement for every flat $A$-algebra $B$.

**Localization and higher direct images.**

Taking $B=S^{-1}A$ for any multiplicative set gives, canonically,

$$
S^{-1}H^q(X,\mathcal F)\cong
H^q(X\times_A\operatorname{Spec}S^{-1}A,\mathcal F_{S^{-1}A}).
$$

This includes $A\to A_a$ and $A\to A_{\mathfrak p}$.

For completeness, let $f:X\to Y$ be a quasi-compact quasi-separated morphism and let $\mathcal F$ be quasi-coherent. The sheaf $R^qf_*\mathcal F$ is the sheafification of $V\mapsto H^q(f^{-1}V,\mathcal F)$. Indeed, use an injective resolution on $X$, restrict it to $f^{-1}V$, and take stalks of $f_*\mathcal I^\bullet$; filtered colimits of modules are exact, so taking cohomology commutes with that stalk limit. On an affine $V=\operatorname{Spec}A$, put $M=H^q(f^{-1}V,\mathcal F)$. The localization result identifies the presheaf on every distinguished $D(a)\subset V$ with $M_a$, compatibly with restriction. Its sheafification is therefore $\widetilde M$. This proves quasi-coherence of $R^qf_*\mathcal F$ and supplies the canonical identification of its sections on $V$ with $M$.

If $h:Y'\to Y$ is flat, cover $Y'$ by affines $W=\operatorname{Spec}B$ mapping into affines $V=\operatorname{Spec}A$ of $Y$. Here $B$ is flat over $A$. For the Cartesian base change $f':X\times_Y Y'\to Y'$, the theorem identifies the modules describing both sides of

$$
h^*R^qf_*\mathcal F\longrightarrow R^qf'_*\mathcal F_{Y'}.
$$

Naturality makes these identifications agree on overlaps, so this is an isomorphism of sheaves. In particular, at $y\in V$ corresponding to $\mathfrak p$,

$$
(R^qf_*\mathcal F)_y\cong
H^q(f^{-1}V\times_A\operatorname{Spec}A_{\mathfrak p},\mathcal F_{A_{\mathfrak p}}).
$$

This is the flat-localization identity needed for the stalk calculation in AG-RG-05, §9. $\square$

## 7. Projective space by its affine charts

Define projective space by gluing the affine charts with coordinates $T_j/T_i$ using their ratio transitions. The twists are glued rank-one modules with the corresponding degree transitions. Thus the displayed section modules below follow from this construction; no Proj existence theorem is an additional proof input.

Projective space is separated over $A$, by a direct diagonal calculation. On the product of charts $U_i\times_A U_j$ put $x_l=T_l/T_i$ and $y_l=S_l/S_j$, with $x_i=1$ and $y_j=1$. Its diagonal has equations $x_jy_i=1$ and $x_l=x_jy_l$ for every $l$. The quotient of the product-chart coordinate ring by these equations is $A[x_l\ (l\ne i),x_j^{-1}]$, the coordinate ring of $U_i\cap U_j$. If $i=j$ the equations simply identify $x_l=y_l$. Hence the diagonal is a closed immersion on every product chart. These charts cover the product, so the diagonal is a closed immersion and the asserted separatedness follows.

<a id="projective-properness"></a>

**Lemma 7.A (projective-space properness).** For every scheme $S$ and integer $n\geq0$, the projection $\mathbf P^n_S\to S$ is proper. Here proper means separated, of finite type and universally closed; no Noetherian or reducedness hypothesis is imposed.

**Proof.** The diagonal calculation above proves separatedness over every ring. The $n+1$ standard charts are polynomial algebras in $n$ variables over the base, so they give finite type. We prove closedness after every base change directly.

Work over an arbitrary affine base $\operatorname{Spec}A$ and put $P=A[T_0,\ldots,T_n]$, with each variable of degree one. Every closed subset $Z$ of $\mathbf P^n_A$ is $V_+(I)$ for a homogeneous ideal $I\subset P$, possibly with infinitely many generators. To see this from the chart construction, a principal open of the $i$th chart has an equation $g(T_j/T_i)\ne0$. Homogenize $g$ to a homogeneous polynomial $f$; this open is $D_+(T_i f)$, since the extra factor restricts it to the $i$th chart. These opens form a basis. Express the complement of $Z$ as their union and let $I$ be generated by their homogeneous equations. The corresponding quotient $B=P/I$ has exactly $Z$ as its projective support: its $i$th chart is the quotient of $A[T_j/T_i]$ by the degree-zero localization of $I$.

Each degree module $B_d$ is a finite $A$-module, since it is a quotient of the finite free module on the degree-$d$ monomials. For any finite $A$-module $M$,
$$
 \{\mathfrak p:M\otimes_A\kappa(\mathfrak p)\ne0\}
   =\operatorname{Supp}M=V(\operatorname{Ann}_A M).
$$
Indeed $M_{\mathfrak p}=0$ exactly when an element outside $\mathfrak p$ kills all of a finite generating list: clear the finitely many localization denominators. This is equivalent to $\operatorname{Ann}M\not\subset\mathfrak p$. The residue quotient is zero exactly when $M_{\mathfrak p}=0$, by the determinant Nakayama proof of Lemma 1.2. Thus the displayed set is closed even when $M$ is not finitely presented.

The fibre of $Z$ at $\mathfrak p$ is the projective support of $B\otimes_A\kappa(\mathfrak p)$. This follows on each chart by quotient and localization, which commute with scalar extension. Its fibre is empty exactly when some degree of this graded algebra is zero. In fact an empty fibre makes every standard chart empty. Its degree-zero localization ring is then zero, by the maximal-ideal argument of Lemma 1.1. Consequently a power of each $T_i$ is zero in the graded algebra. If these powers are $T_i^{e_i}$, every monomial of degree greater than $\sum_i(e_i-1)$ has one of them as a factor, so that degree is zero. Conversely, if degree $d$ is zero, then each $T_i^d$ is zero (if $d=0$, the whole algebra is zero), making every chart empty. All larger degrees are zero too, since the algebra is generated in degree one. Right exactness of tensor identifies its degree $d$ with $B_d\otimes_A\kappa(\mathfrak p)$.

It follows that
$$
 \operatorname{image}(Z\to\operatorname{Spec}A)
    =\bigcap_{d\geq0}V(\operatorname{Ann}_A B_d).
$$
An arbitrary intersection of closed sets is closed. The argument works over every ring $A$ and for every closed subset, including ideals that are not finitely generated. Apply it on each affine open after an arbitrary scheme base change. Closedness is local on the target: a subset is closed if its intersections with a covering family of opens are closed there. Hence the projection is universally closed. Together with its already proved separation and finite type this proves properness. $\square$

**Corollary 7.B (the properness consequences used below).** Proper morphisms are preserved by base change and composition. Closed immersions are proper. If $X\to S$ is proper and $Y\to S$ is separated, every $S$-morphism $X\to Y$ is proper; when it is an immersion, it is a closed immersion.

**Proof.** Universally closed maps remain so under base change, since an iterated base change is a base change, and under composition, since images of closed sets are closed at both steps. Finite type remains so under base change by tensoring a finite algebra generating list, and under composition by joining finite generating lists on affine charts; the finite covers expressing quasi-compactness also pull back and compose. Separatedness remains so under base change by the diagonal formula. For $X\to Y\to S$, the diagonal $X\to X\times_SX$ factors through its closed relative diagonal $X\to X\times_YX$ and the closed immersion $X\times_YX\to X\times_SX$ obtained by pulling back $\Delta_{Y/S}$. This proves its preservation under composition.

On affine charts a closed immersion is a quotient map $A\to A/J$. It is of finite type with zero algebra generators, even for an infinite ideal $J$. Its diagonal is an isomorphism, and its images of closed sets are closed; quotients have the same properties after base change. Thus it is proper. For a morphism $g:X\to Y$ as in the statement, the graph $X\to X\times_SY$ is closed, being the pullback of $\Delta_{Y/S}$. Projection $X\times_SY\to Y$ is the base change of the proper map $X\to S$. Their composite $g$ is therefore proper. If $g$ is an immersion, it is a closed immersion on an open neighbourhood $U$ of its image by the definition of immersion. Properness makes that image closed in $Y$. On $U$ the map is closed, and on the open complement of its image it is the empty closed immersion. These opens cover $Y$, and their quotient ideals glue, proving that $g$ is a closed immersion. $\square$

The statements can be compared with the freely readable [Stacks, Tag 01WC](https://stacks.math.columbia.edu/tag/01WC). The graded-module and graph arguments above provide the programme proofs used here.

### The monomial section complex

Fix a ring \(A\), an integer \(n\ge0\), and the standard graded ring
\[
S=A[T_0,\ldots,T_n],\qquad\deg T_i=1.
\]
Write \(\mathbf P_A^n=\operatorname{Proj}S\). The twist \(\mathcal O(d)\) is the sheaf of the graded module \(S(d)\), with \(S(d)_m=S_{d+m}\). On a nonempty intersection of standard charts,
\[
\Gamma(D_+(T_{i_0})\cap\cdots\cap D_+(T_{i_p}),\mathcal O(d))
=S[T_{i_0}^{-1},\ldots,T_{i_p}^{-1}]_d.
\]
The subscript means homogeneous degree \(d\). Inverting the product of these variables is equivalent to inverting each of them. These intersections are affine; for example, the chart indexed by \(i\) has coordinates \(T_j/T_i\). Thus the finite-cover comparison of Sections 4-5 above identifies cohomology with the ordered Čech complex
\[
C^p(d)=\bigoplus_{i_0<\cdots<i_p}
S[T_{i_0}^{-1},\ldots,T_{i_p}^{-1}]_d.
\]
It stops in degree \(n\). The differential is the alternating sum of restrictions, with increasing indices and the sign of the deleted index's position.

Each term is a free \(A\)-module on Laurent monomials. This remains true when \(A\) has torsion or zero divisors: the monomials are formal basis vectors of the polynomial localization. A weight is an integer vector \(e=(e_0,\ldots,e_n)\), with total \(\sum e_i=d\). The monomial \(T^e\) occurs in the factor indexed by a subset \(I\) exactly when
\[
N(e)=\{i:e_i<0\}\subset I.
\]
The differential preserves weights. The whole complex is therefore a direct sum of complexes \(C^\bullet(e)\), each having a copy of \(A\) for the nonempty subsets \(I\) containing \(N(e)\). Its differential uses only zero maps and signed identity maps between these copies.

These are direct sums rather than products over the weights: every Laurent polynomial has finite support, and only finitely many chart subsets occur in a fixed degree. Direct sums are exact, so cohomology can be computed separately at each weight.

### Negative exponents determine cohomology

**Lemma 7.1 (the three weight cases).** For a weight \(e\), the cohomology of \(C^\bullet(e)\) is:

| Negative indices | Surviving cohomology |
| --- | --- |
| None | One copy of \(A T^e\) in degree zero |
| All \(n+1\) indices | One copy of \(A T^e\) in degree \(n\) |
| A nonempty proper subset | Zero in every degree |

**Proof.** If every exponent is negative, only the subset \(I=\{0,\ldots,n\}\) is allowed. Its copy of \(A\) is the whole complex, in degree \(n\).

If no exponent is negative, every nonempty subset is allowed. This is the ordinary simplex cochain complex, with \(A\) as its degree-zero cohomology. More explicitly, augment it by a copy of \(A\) in degree \(-1\), whose map is the diagonal. Inserting a fixed index gives a contracting homotopy of this augmented complex. Thus the original complex has the stated cohomology.

Now suppose \(N(e)\) is nonempty and proper. Choose \(j\notin N(e)\). Regard an ordered cochain as an alternating function of distinct indices, with value zero on any tuple whose set does not contain \(N(e)\), and zero on repeated indices. Define
\[
(hc)_{i_0\ldots i_{p-1}}=c_{j i_0\ldots i_{p-1}}.
\]
Insertion is followed by reordering with its sign. This map is well-defined: adjoining \(j\) does not change whether a subset contains \(N(e)\). The identity \(dh+hd=1\) follows by pairing each deletion other than the inserted \(j\) with its opposite-sign counterpart; deletion of \(j\) contributes the original cochain. In degree zero the would-be augmented term is absent because \(N(e)\ne\varnothing\), and the same calculation still works: the value at the singleton \(\{j\}\) is zero. This is a contraction of the unaugmented complex, so all its cohomology is zero. \(\square\)

For a concrete example with three variables, take \(N(e)=\{0\}\). The weight complex is
\[
A\longrightarrow A^2\longrightarrow A,
\qquad a\longmapsto(-a,-a),\qquad(b,c)\longmapsto b-c.
\]
The two middle entries correspond to \(\{0,1\}\) and \(\{0,2\}\). The last map is surjective and its kernel is the diagonal, exactly the preceding image. With \(N(e)=\{0,1\}\), the only terms are \(A\xrightarrow{1}A\) in degrees one and two. With all three exponents negative, only the last \(A\) survives. These small complexes illustrate the general cancellation without dividing by an integer.

Put \(r=n+1\). For \(n\ge1\), let
\[
L_d=\bigoplus_{\substack{e_i<0\text{ for all }i\\\sum e_i=d}} A T^e.
\]
It is zero unless \(d\le-r\). It can also be written as the homogeneous degree-\(d\) part of
\[
\frac1{T_0\cdots T_n}A[T_0^{-1},\ldots,T_n^{-1}].
\]
The expression is a module of reciprocal monomials, not a ring.

**Theorem 7.2 (cohomology of every twist).** If \(n\ge1\), then
\[
H^q(\mathbf P_A^n,\mathcal O(d))=
\begin{cases}
S_d,&q=0,\ d\ge0,\\
L_d,&q=n,\ d\le-n-1,\\
0,&\text{otherwise}.
\end{cases}
\]
All the nonzero modules are finite free over \(A\). For \(n=0\), instead,
\[
H^0(\mathbf P_A^0,\mathcal O(d))=A\quad\text{for every integer }d,
\qquad H^q=0\quad(q>0).
\]

**Proof.** For positive dimension, Lemma 7.1 and the weight direct sum identify degree-zero classes with monomials having nonnegative exponents, and top-degree classes with monomials having strictly negative exponents. All other weights are contractible. The sum condition gives the stated ranges. For fixed \(d\), there are only finitely many vectors of nonnegative exponents summing to \(d\), or of strictly negative exponents summing to \(d\), proving finite freeness.

In dimension zero there is one chart, and its degree-\(d\) section module is \(A T_0^d\) for every integer \(d\). This is \(A\); geometrically \(\mathbf P_A^0=\operatorname{Spec}A\), and the trivializing generator of the twist is \(T_0^d\), including negative powers. There are no higher Čech terms. \(\square\)

The separate zero-dimensional clause prevents a false negative-twist vanishing statement when degree zero is also top degree. For \(n\ge1\), all groups vanish in the entire interval \(-n\le d\le-1\). The calculation is [Stacks, Tag 01XT], with the two cohomological degrees kept distinct when necessary.

### A pairing with no factorials

The top group of \(\mathcal O(-r)\) is free of rank one. Fix its trace by
\[
\operatorname{tr}\left[\frac1{T_0\cdots T_n}\right]=1.
\]
For \(m\ge0\), multiplication by global sections gives a bilinear pairing
\[
S_m\times H^n(\mathbf P_A^n,\mathcal O(-m-r))
\longrightarrow H^n(\mathbf P_A^n,\mathcal O(-r))
\xrightarrow{\operatorname{tr}}A.
\]

**Theorem 7.3 (perfect monomial pairing).** This pairing is perfect: each module is the \(A\)-linear dual of the other.

**Proof.** Index the monomial basis of \(S_m\) by vectors \(\alpha_i\ge0\) with \(\sum\alpha_i=m\). A corresponding basis of the other group is
\[
u_\alpha=T_0^{-\alpha_0-1}\cdots T_n^{-\alpha_n-1}.
\]
The product \(T^\beta u_\alpha\) has exponent \(\beta_i-\alpha_i-1\). If \(\beta=\alpha\), it is the trace generator. If the vectors differ but have the same total, at least one \(\beta_i>\alpha_i\), so that product has a nonnegative exponent and represents zero in top cohomology by Lemma 7.1. The pairing matrix is therefore the identity. This proves perfection over every ring, including rings with positive characteristic or nilpotents. \(\square\)

The proof also applies to \(n=0\) using the generators of its one-chart section modules. There is no appeal to integration and no normalization by a factorial. This will be the local calculation behind Serre duality later in the course.

**Proposition 7.4 (base change and polynomial multiplication).** The preceding identifications commute with every ring map \(A\to B\), including nonflat ones. If \(f\in S_s\), multiplication by \(f\) on top cohomology is the dual of
\[
S_{-d-s-r}\xrightarrow{\ f\ }S_{-d-r},
\]
where negative homogeneous pieces are zero and \(n\ge1\).

**Proof.** The section complex over \(B\) is obtained by replacing the coefficient ring in every monomial factor by \(B\). The weight contractions use only signed identities, so they remain contractions after any coefficient change. The surviving bases also change by extension of scalars. The resulting isomorphism
\[
H^q(\mathbf P_A^n,\mathcal O(d))\otimes_A B
\simeq H^q(\mathbf P_B^n,\mathcal O(d))
\]
is the natural one induced by the chart section complexes. No general nonflat base-change theorem is being assumed here.

For the multiplication statement, let \(u\) be a top class and \(g\) a homogeneous polynomial of degree \(-d-s-r\). Associativity of multiplication gives
\[
\operatorname{tr}(g(fu))=\operatorname{tr}((fg)u).
\]
The perfect pairing identifies this equality with the claimed dual map. Products that leave the negative-exponent range are zero classes, as already proved. \(\square\)

This functorial form agrees with [Stacks, Tag 01XV]. In particular, the finite free modules in the calculation retain their ranks under every specialization of the base ring.

## 8. Projective finiteness, ample embeddings and vanishing

### Clearing denominators in a line bundle

For a line bundle \(L\) and a section \(s\in H^0(X,L)\), write \(X_s\) for the open where the section generates the line. Multiplication by \(s\) gives maps \(F\otimes L^a\to F\otimes L^{a+1}\).

**Lemma 8.1 (extension after a power).** If \(X\) is quasi-compact and quasi-separated, \(F\) is quasi-coherent, and \(s\) is as above, the natural map
\[
\underset{a\ge0}{\operatorname{colim}}\ H^0(X,F\otimes L^a)
\longrightarrow H^0(X_s,F),\qquad t\longmapsto t/s^a,
\]
is an isomorphism. In particular every section on \(X_s\) extends after multiplying by a sufficiently high power of \(s\).

**Proof.** Choose a finite affine cover \(U_i\) trivializing \(L\). On \(U_i\), write \(s=f_i\) in that frame and \(F=\widetilde M_i\). Then \(U_i\cap X_s=D(f_i)\), and sections there are elements of \((M_i)_{f_i}\). Each is a fraction with a finite denominator, so a section on \(X_s\) has local lifts in \(F\otimes L^a\) for a common exponent \(a\).

On each overlap the difference of two lifts becomes zero after inverting \(s\). The overlap is quasi-compact by quasi-separatedness. Cover it by finitely many affines trivializing \(L\); on each, an element that is zero in a localization is killed by a power of its local equation. A common power kills the difference on the whole overlap. There are finitely many pairs, so one further power makes all lifts agree. They glue to a global twisted section. This proves surjectivity. If a global twisted section restricts to zero, the same localization argument on the finite cover kills it by a common power of \(s\); it is therefore zero in the colimit. This proves injectivity. \(\square\)

The same argument works with a section of \(L^b\), using powers \(L^{ab}\). It does not require \(s\) to be a nonzerodivisor. The associated section-module recovery is [Stacks, Tag 0AG5]; here the denominator argument also explains its compatibility with the usual maps from homogeneous elements.

Now let \(R\) be Noetherian, \(S=R[T_0,\ldots,T_N]\), and \(P=\mathbf P_R^N\). The scheme \(P\) is Noetherian by Lemma 1.3 above: each standard chart is a polynomial ring over \(R\). A coherent sheaf on a locally Noetherian scheme is a quasi-coherent sheaf with finite modules on affine opens. Kernels and cokernels of maps between such sheaves are coherent, because submodules of finite modules over Noetherian rings are finite.

**Proposition 8.2 (finite generation by twists).** For every coherent \(F\) on \(P\), there is a finite surjection
\[
\mathcal O_P(-a)^{\oplus m}\twoheadrightarrow F
\]
for some \(a\ge0\). Moreover \(F(d)\) is generated by finitely many global sections for every sufficiently large \(d\).

**Proof.** On \(D_+(T_i)\), choose finitely many module generators of \(F\). Lemma 8.1 extends each generator, after multiplication by a power of \(T_i\), to a global section of some \(F(a_{ij})\). Choose a common \(a\ge0\) at least as large as every \(a_{ij}\), and multiply these sections by \(T_i^{a-a_{ij}}\). On the \(i\)-th chart the multiplier is a unit in the chart's twist frame, so the resulting global sections of \(F(a)\) still generate there. All charts together give a finite global generating family, which is equivalent to the displayed surjection. For \(d\ge a\), tensor it with \(\mathcal O(d)\). The source is a sum of copies of \(\mathcal O(d-a)\), generated by its polynomial monomials; their images generate \(F(d)\). This also treats \(N=0\), where the scheme is affine and every twist is trivial. \(\square\)

Global generation means that the evaluation map from global sections tensored with \(\mathcal O_P\) is surjective. It does not mean that every local generator is itself the restriction of an untwisted global section. The power of the chart coordinate is what makes local information extend.

**Lemma 8.3 (an ample power gives an immersion).** Let \(X\) be quasi-compact and quasi-separated and of finite type over an affine scheme \(\operatorname{Spec}R\). Let \(L\) be ample. There are \(b>0\) and an immersion \(i:X\to\mathbf P_R^N\) with \(L^b\cong i^*\mathcal O(1)\). If \(X\) is proper over \(R\), the immersion is closed.

**Proof.** We use the affine-section definition of ampleness: the affine opens \(X_s\), for sections \(s\) of positive tensor powers of \(L\), form a basis. Quasi-compactness supplies a finite cover by such opens. Taking powers of the finitely many sections replaces their degrees by a common positive multiple \(m\), without changing their nonvanishing opens. Denote the resulting sections by \(s_i\in H^0(X,L^m)\) and write \(X_{s_i}=\operatorname{Spec}B_i\). Each \(B_i\) is a finite-type \(R\)-algebra, with the following explicit affine-chart argument. Write \(W=X_{s_i}=\operatorname{Spec}B_i\). At a point of \(W\), choose a finite-type affine chart \(V\) of \(X/R\), then a principal open \(W_g\) containing that point and contained in \(V\), and finally a principal open \(V_h\) containing the point and contained in \(W_g\). As \(W_g\subset V\), the restriction of \(h\) is a fraction \(b/g^q\) in \((B_i)_g\). Hence
\(V_h=W_g\cap V_h=(W_g)_h=W_{gb}\): it is a principal open of \(W\), and its algebra is finite type over \(R\) by localization of the chart algebra of \(V\). Quasi-compactness gives finitely many such opens \(W_{b_j}\). Choose finite generators for every \((B_i)_{b_j}\), their finitely many numerators in \(B_i\), and coefficients \(e_j\in B_i\) with \(\sum_j e_jb_j=1\). Let \(B'\) be the \(R\)-subalgebra generated by these numerators, all \(b_j\) and all \(e_j\). Then \(B'_{b_j}=(B_i)_{b_j}\). For \(b\in B_i\), some power \(b_j^{N_j}b\) belongs to \(B'\) for each \(j\). A sufficiently large power of \(\sum_j e_jb_j=1\) expresses \(1\) as a \(B'\)-linear combination of the \(b_j^{N_j}\). Multiplying by \(b\) gives \(b\in B'\). Thus \(B_i=B'\) is finite type. Choose finitely many algebra generators \(a_{ij}\) for each \(B_i\).

Apply Lemma 8.1 with the line bundle \(L^m\) and \(F=\mathcal O_X\). For every \(a_{ij}\), it gives a global section whose quotient by a power of \(s_i\) is \(a_{ij}\). There are finitely many generators and charts, so multiplication by additional powers gives a common exponent \(e>0\) and sections \(u_{ij}\in H^0(X,L^{me})\) such that \(u_{ij}/s_i^e=a_{ij}\) on \(X_{s_i}\). Set \(t_i=s_i^e\). The \(t_i\) alone generate \(L^{me}\), because their nonvanishing opens cover \(X\). The finite collection of all \(t_i,u_{ij}\) therefore defines a morphism \(i:X\to\mathbf P_R^N\), by the quotient convention, with \(i^*\mathcal O(1)=L^{me}\).

On the target chart where the coordinate for \(t_i\) is nonzero, the inverse image is exactly \(X_{s_i}\). The coordinate ratios for \(u_{ij}\) pull back to \(a_{ij}\); hence the homomorphism from that chart's polynomial coordinate ring to \(B_i\) is surjective. The restriction of \(i\) on this chart is a closed immersion. Let \(V\) be the union of these target charts. It contains the image, and the chartwise closed immersions glue to a closed immersion \(X\to V\). Thus \(X\to\mathbf P_R^N\) is an immersion, with \(b=me\).

If \(X\) is proper over \(R\), its graph in \(X\times_R\mathbf P_R^N\) is closed: the graph is the inverse image of the diagonal of the separated scheme \(\mathbf P_R^N\). Projection from this product to \(\mathbf P_R^N\) is the base change of the proper map \(X\to\operatorname{Spec}R\). The graph followed by this projection shows that \(i\) is proper. Its image is therefore closed in \(\mathbf P_R^N\). On the open \(V\) it is already a closed immersion, and on the open complement of its closed image it is the empty closed immersion. These opens cover the target, so \(i\) is a closed immersion. \(\square\)

### Descending induction proves Serre's theorems

**Theorem 8.4 (finiteness and vanishing on projective space).** For a coherent \(F\) on \(\mathbf P_R^N\), with \(R\) Noetherian:

- \(H^q(P,F)=0\) for \(q>N\).
- Every \(H^q(P,F)\) is a finite \(R\)-module.
- There exists \(d_0(F)\) such that \(H^q(P,F(d))=0\) for every \(q>0\) and every \(d\ge d_0(F)\).
- \(F(d)\) is globally generated for every sufficiently large \(d\).

**Proof.** The \(N+1\) standard charts and all their intersections are affine. Their ordered Čech complex computes quasi-coherent cohomology and has no terms above degree \(N\). This proves the first assertion, even without coherence.

Prove finiteness and eventual vanishing simultaneously, by descending induction on \(q\), for all coherent sheaves. The assertions hold in degrees greater than \(N\). Choose a finite quotient by twists, with coherent kernel:
\[
0\longrightarrow K\longrightarrow E\longrightarrow F\longrightarrow0,
\qquad E=\bigoplus_j\mathcal O(b_j).
\]
The exact cohomology segment
\[
H^q(P,E)\longrightarrow H^q(P,F)\longrightarrow H^{q+1}(P,K)
\]
has finite modules at both ends: the left one by Theorem 7.2, the right one by induction. Its middle term is an extension of a quotient of the left module by a submodule of the right module. The latter submodule is finite because \(R\) is Noetherian. Hence the middle term is finite. This includes \(q=0\).

For \(q>0\), twist the short exact sequence by \(\mathcal O(d)\), which is an exact operation because this sheaf is invertible. In the corresponding segment, \(H^q(E(d))\) is zero for sufficiently large \(d\) by Theorem 7.2; \(H^{q+1}(K(d))\) is zero for sufficiently large \(d\) by induction. Thus \(H^q(F(d))=0\) eventually. Only the finitely many degrees \(1,\ldots,N\) can occur, so their thresholds have a maximum. Proposition 8.2 proves the last assertion. \(\square\)

This is [Stacks, Tag 01YS]. The proof uses as many coherent kernels as the induction needs, rather than asserting that every coherent sheaf has a finite resolution by line bundles. Such a resolution would require further hypotheses and is unnecessary here.

For a closed immersion \(i:X\hookrightarrow P\), pushforward identifies coherent sheaves on \(X\) with coherent sheaves on \(P\) annihilated by the defining ideal. Affine-locally this is just restriction of scalars along a quotient of Noetherian rings. Pushforward is exact, and
\[
H^q(X,F)=H^q(P,i_*F),\qquad
i_*(F\otimes i^*\mathcal O(d))=(i_*F)(d).
\]
The cohomology equality follows from the common affine-cover complex of Sections 4-5: restriction of the standard affine charts to the closed subscheme gives affine charts, and extension of its sheaf along the closed immersion has exactly the same section modules on their intersections. The tensor equality can be checked in a local line-bundle frame. Theorem 8.4 therefore applies to every closed projective subscheme with its hyperplane bundle.

**Theorem 8.5 (proper schemes with an ample line bundle).** Let \(X\to\operatorname{Spec}R\) be proper, with \(R\) Noetherian, and let \(L\) be ample. For coherent \(F\), all \(H^q(X,F)\) are finite over \(R\); the groups \(H^q(X,F\otimes L^d)\), \(q>0\), vanish for all sufficiently large \(d\); and \(F\otimes L^d\) is globally generated for all sufficiently large \(d\).

**Proof.** Lemma 8.3 gives a closed immersion \(i:X\hookrightarrow\mathbf P_R^N\) and an integer \(b>0\) with \(L^b=i^*\mathcal O(1)\). Its quasi-compactness and quasi-separatedness hypotheses hold because \(X\) is proper. Apply Theorem 8.4 to each of the finitely many coherent sheaves \(i_*(F\otimes L^j)\), \(0\le j<b\). If \(d=bm+j\), its twist by \(\mathcal O(m)\) is \(i_*(F\otimes L^d)\). The theorem gives vanishing and global generation for all sufficiently large \(m\) in each residue class. Taking their finitely many thresholds proves the assertion for every large \(d\). Finiteness follows already from \(i_*F\). \(\square\)

This residue-class step is essential: an embedding given by \(L^b\) initially controls only multiples of \(b\). The result is [Stacks, Tag 0B5T].

## 9. Serre's affine criterion

For a global function \(f\in\Gamma(X,\mathcal O_X)\), let \(X_f\) be its invertibility locus. It is open; on an affine chart it is the usual distinguished open of the restricted function.

We will use two elementary facts. Every closed subset \(Z\) of a scheme has a reduced closed subscheme structure, hence a quasi-coherent radical ideal. On an affine chart \(\operatorname{Spec}B\), take the radical ideal cutting out \(Z\) there. Localization of radical ideals agrees on smaller distinguished charts, so these ideals glue. Also every nonempty quasi-compact closed subset of a scheme has a closed point. For completeness, among its nonempty closed subsets, every descending chain has nonempty intersection by quasi-compactness. Zorn's lemma gives a minimal nonempty closed subset \(C\). For each \(x\in C\), its closure is \(C\) by minimality. A scheme is \(T_0\), so two different points cannot have the same closure; thus \(C\) is a singleton. The point is closed in the original scheme when the original subset is closed.

**Lemma 9.1 (an affine principal cover detects affineness).** Suppose finitely many global functions \(f_i\) generate the unit ideal in \(R=\Gamma(X,\mathcal O_X)\), and the opens \(X_{f_i}\) are affine and cover \(X\). Then \(X\) is affine.

**Proof.** The finite affine cover makes \(X\) quasi-compact. Its intersections are affine: \(X_{f_i}\cap X_{f_j}\) is the distinguished open defined by \(f_j\) in the affine \(X_{f_i}\). Hence \(X\) is quasi-separated. The degree-zero case of Section 6 gives
\[
R_{f_i}=\Gamma(X_{f_i},\mathcal O_X).
\]
The canonical morphism \(X\to\operatorname{Spec}R\) restricts on \(X_{f_i}\) to the isomorphism with \(D(f_i)\) given by this ring identification. The \(D(f_i)\) cover \(\operatorname{Spec}R\), since the \(f_i\) generate one. These isomorphisms agree on overlaps as restrictions of the canonical morphism, and give an isomorphism of the whole schemes. \(\square\)

**Theorem 9.2 (Serre's criterion).** For a quasi-compact scheme \(X\), the following are equivalent:

1. \(X\) is affine.
2. \(H^p(X,\mathcal F)=0\) for every quasi-coherent \(\mathcal F\) and every \(p>0\).
3. \(H^1(X,\mathcal I)=0\) for every quasi-coherent ideal \(\mathcal I\subset\mathcal O_X\).

No quasi-separatedness hypothesis is required in this statement.

**Proof.** Theorem 5.1 proves the first implication, and the second plainly implies the third. Assume the third condition.

Let \(x\) be a closed point and choose an affine neighbourhood \(U=\operatorname{Spec}B\). Let \(Z=X\setminus U\), and let \(\mathcal I\) and \(\mathcal I'\) be the reduced ideals of \(Z\) and \(Z\cup\{x\}\), respectively. There is an exact sequence
\[
0\to\mathcal I'\to\mathcal I\to\mathcal I/\mathcal I'\to0.
\]
On \(U\), the quotient is the module sheaf of \(B/\mathfrak m_x\); away from \(x\) it is zero. It is the skyscraper with value \(\kappa(x)\). This can also be checked by gluing its descriptions on \(U\) and \(X\setminus\{x\}\), whose overlap has zero quotient.

Vanishing of \(H^1(X,\mathcal I')\) lifts the section \(1\in\kappa(x)\) to a global \(f\in\Gamma(X,\mathcal I)\). The function is invertible at \(x\) and has zero residue at every point of \(Z\). Consequently
\[
x\in X_f\subset U,
\]
and \(X_f\) is a distinguished affine open of \(U\).

The union of all affine opens of this form contains every closed point. Its complement is a quasi-compact closed subset, and if nonempty would have a closed point by the fact proved above. Thus the union is all of \(X\). Choose finitely many such \(f_1,\ldots,f_r\) whose invertibility loci cover \(X\).

We must still show that these functions generate one in the ring of global sections. The map
\[
\mathcal O_X^{\oplus r}\xrightarrow{(f_1,\ldots,f_r)}\mathcal O_X
\]
is surjective on stalks, since one \(f_i\) is invertible at each point. Its kernel \(\mathcal K\) is quasi-coherent. Put \(\mathcal K_i=\mathcal K\cap\mathcal O_X^{\oplus i}\), using the first \(i\) summands. Projection onto the \(i\)-th summand embeds \(\mathcal K_i/\mathcal K_{i-1}\) as a quasi-coherent ideal of \(\mathcal O_X\). These quotients therefore have zero first cohomology. Starting with \(\mathcal K_0=0\), their long exact sequences inductively give \(H^1(X,\mathcal K_i)=0\), and in particular \(H^1(X,\mathcal K)=0\).

The global-section sequence is now surjective onto \(\Gamma(X,\mathcal O_X)\). There are global \(a_i\) with \(\sum_i a_i f_i=1\). Lemma 9.1 proves affineness. The quasi-separatedness used in that lemma has been obtained from the principal cover, rather than assumed at the start. \(\square\)

This is the ideal-sheaf form of [Stacks, Tag 01XF]. It explains why degree one is enough: it first constructs affine neighbourhoods from functions and then lifts the unit through the relation module.

## Free source and proof record

The scheme correspondence, affine-target construction, affine vanishing and filtered-cover statements can be compared with the freely accessible Stacks Project, Tags [01IA](https://stacks.math.columbia.edu/tag/01IA), [01I1](https://stacks.math.columbia.edu/tag/01I1), [01XB](https://stacks.math.columbia.edu/tag/01XB), [01ES](https://stacks.math.columbia.edu/tag/01ES), [01EW](https://stacks.math.columbia.edu/tag/01EW), [012M](https://stacks.math.columbia.edu/tag/012M) and [012W](https://stacks.math.columbia.edu/tag/012W). The proofs actually consumed above are written in this lesson. The construction of injectives is given here rather than assigned to a general categorical prerequisite. No paid work is a source or citation.

The detailed Laurent-monomial, denominator-extension and descending-induction arguments in Sections 7-9 reuse the actual independently authored CC0 programme proofs *Cohomology of projective space*, *Coherent sheaves on projective schemes: Serre's theorems*, and *Cohomology of affine schemes and Serre's criterion*. Their exact consumed proof excerpts are reproduced here with their hypotheses; unrelated reference lists and unconsumed results are not imported. The original authorship and self-check are GPT-6.1 Sol (OpenAI), Codex, Ultra. The present lesson supplies their earlier affine and homological inputs. Free comparison sources are Stacks Tags [01XT](https://stacks.math.columbia.edu/tag/01XT), [01YS](https://stacks.math.columbia.edu/tag/01YS), [01VT](https://stacks.math.columbia.edu/tag/01VT) and [01XF](https://stacks.math.columbia.edu/tag/01XF).
