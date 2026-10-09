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

### Signed normal Koszul maps and ordered counits

Here are the coefficient, density and ordering signs in Lemma 1.2. They also fix the closed counit used in proper duality below. Order the normal coordinates $t_1,\ldots,t_c$. Let $e_J$ be the ordered Koszul wedge in degree $-|J|$, and let $f_I(e_I)=1$ be its untwisted Hom dual in degree $|I|$. Put $s(I)=\sum_{i\in I}i$. The normal Koszul differential is

\[
\begin{gathered}
d e_J=\sum_{j\in J}(-1)^{\operatorname{pos}_J(j)-1}
 t_j e_{J\setminus\{j\}}.
\end{gathered}
\tag{1.5a}
\]

The Hom differential in cochain degree $r$ is $(-1)^{r+1}$ times its transpose. The structure Koszul complex shifted by $[-c]$ has differential $(-1)^c$ times the original one. The chain identification used in (1.5) is

\[
\begin{gathered}
T(f_I)=(-1)^{s(I)+c|I|-|I|(|I|-1)/2}\\
 e_{I^c}\otimes\det(\mathcal I/\mathcal I^2)^{-1}.
\end{gathered}
\tag{1.5b}
\]

The bottom coefficient is fixed by $f_\varnothing\mapsto e_{\{1,\ldots,c\}}$ times the inverse determinant. Inserting an index into $I$ on the Hom side removes it from $I^c$ on the structure Koszul side. The position signs, the displayed exponent difference, and the target shift $(-1)^c$ then give exactly the same coefficient for each $t_j$. This verifies the chain identity in every degree. Its top coefficient is positive in every codimension, since $s(\{1,\ldots,c\})=c(c+1)/2$ and the resulting exponent is $c(c+1)$. In two directions it reads

\[
\begin{gathered}
(f_\varnothing,f_1,f_2,f_{12})\\
\longmapsto(e_{12},-e_2,e_1,e_\varnothing)\\
\otimes\det(\mathcal I/\mathcal I^2)^{-1}.
\end{gathered}
\tag{1.5c}
\]

The backward transfer has the inverse normal top-density line. Taking Hom from it supplies the normal top-density line, which cancels the inverse determinant in (1.5b). This is the explicit density cancellation in (1.5), and leaves the intrinsic supported-module expression $\det(\mathcal I/\mathcal I^2)\otimes\operatorname{ann}_{\mathcal I}M$ already stated above. Under a change of normal coordinates the two determinant factors transform inversely, so these maps glue.

For one direction, $T(f_\varnothing)=e_1$ and $T(f_1)=e_\varnothing$ are both positive, and the shifted target differential is $-t$. The positive-$t$ two-term presentation in the following example replaces the degree-zero generator $e_1$ by $-e_1$ and keeps the degree-one generator $e_\varnothing$. Its differential is then $+t$. This is a separate presentation basis conversion; it changes neither the top coefficient of $T$ nor the closed counit.

The one-normal-coordinate closed counit into $\mathcal O[1]$ is the degree-one Hom cochain sending $e_1$ to $1$, with coefficient $+1$. The ordered tensor of $c$ such counits uses the actual tensor–Hom rule

\[
\begin{gathered}
(\phi_1\otimes\cdots\otimes\phi_c)\\
(p_1\otimes\cdots\otimes p_c)\\
=(-1)^{\sum_{a<b}|p_a||\phi_b|}
 \prod_a\phi_a(p_a).
\end{gathered}
\tag{1.5d}
\]

At the top Koszul input every $|p_a|=-1$ and $|\phi_b|=1$. Hence the ordered closed counit has coefficient

\[
\varepsilon_c=(-1)^{c(c-1)/2}
\tag{1.5e}
\]

in the untwisted top Hom frame. The normal density is contracted in that same order. Tensor–Hom adjunction and the shift totalization of successive closed adjunctions give precisely this ordered tensor; thus it is also the composition of their actual counits. In particular the positive top coefficient of the coefficient map $T$ alone is not the value of the ordered higher-codimension counit.

The corresponding closed proper-dual map is equally explicit. If $P_t$ is the normal point Koszul resolution, side change fixes $t_j$ and the dual shift $[c]$ gives

\[
\begin{gathered}
d_{DP_t}f_I\\
=(-1)^{c+|I|+1}\sum_j t_j f_j\wedge f_I,\\
H_t(e_J)\\
=(-1)^{s(J)+|J|(|J|+1)/2}f_{J^c}.
\end{gathered}
\tag{1.5f}
\]

Substitution in (1.5a) verifies that $H_t$ is a chain map. Both its bottom and top coefficients are positive. Transposing the counit by finite-projective evaluation sends the normal generator to $\varepsilon_c f_{\{1,\ldots,c\}}$, and the same Koszul chain identity determines all remaining coefficients. Therefore its normal proper-dual comparison is

\[
\rho_i^{\mathrm{normal}}=\varepsilon_c H_t.
\tag{1.5g}
\]

This retains the backward-transfer density and every ordering sign, and specifies the evaluation/counit map used in (4.3), rather than choosing a point-module endpoint self-duality. Tensor these finite normal matrices with the full coefficient complex and its Hom differential to get the same identification for bounded coefficients. Coordinate changes preserve the determinant contraction, so the calculation glues and respects composed closed embeddings.

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

### 3.2. Proper direct images and coherence

The projection formula does not by itself show that a direct image has finitely generated differential-operator cohomology. We establish that assertion before using it in the duality calculation.

**Lemma 3.2 (coherent generators).** On a Noetherian separated scheme, a finite-type quasi-coherent subsheaf of a quasi-coherent sheaf on a quasi-compact open extends to a coherent subsheaf on the whole scheme. Consequently, a coherent right $\mathcal D_X$-module $M$ on a smooth separated variety has a coherent $\mathcal O_X$-subsheaf $F$ for which multiplication is a surjection
\[
F\otimes_{\mathcal O_X}\mathcal D_X\longrightarrow M.
\tag{3.7}
\]
It has a resolution, concentrated in degrees at most zero, whose terms are $F^p\otimes_{\mathcal O_X}\mathcal D_X$ with $F^p$ coherent over $\mathcal O_X$.

**Proof.** We first give the extension argument. For a quasi-compact open immersion $j:U\hookrightarrow V$ with $V=\operatorname{Spec}A$, direct image of a quasi-coherent sheaf is quasi-coherent. Indeed, cover $U$ by finitely many principal opens $D(s_i)$. Sections are the kernel of the two restriction maps between the finite products of sections on $D(s_i)$ and $D(s_is_j)$. Localization at an element of $A$ commutes with this kernel and these finite products, giving the corresponding sections on $U\cap D(a)$. This is the affine criterion for quasi-coherence of $j_*$.

Let $Q$ be quasi-coherent on $V$ and let $G\subset Q|_U$ be of finite type. The kernel
\[
H=\ker\bigl(Q\longrightarrow j_*(Q|_U/G)\bigr)
\]
is quasi-coherent, lies in $Q$, and restricts to $G$. On each of finitely many $D(s_i)$ covering $U$, choose generators of $G$. Since $H$ is quasi-coherent, these generators are fractions of elements of $\Gamma(V,H)$. The finitely many numerators generate an $A$-submodule $N\subset\Gamma(V,H)$. Its associated sheaf is coherent, because $A$ is Noetherian, and restricts to $G$: it is contained in $H$ and contains all the selected generators on the principal cover.

For a general separated Noetherian scheme, add the opens of a finite affine cover one at a time. The intersection of the open already treated with the next affine open is quasi-compact. The affine construction extends the prescribed subsheaf across that affine open while preserving it on the intersection. The two subsheaves glue inside $Q$. Repeating gives the claimed extension. In particular, every finite collection of sections on one affine open is contained there in a coherent subsheaf defined on all of $X$.

Now choose finite right differential-operator generators of $M$ on each member of a finite affine cover. Extend their $\mathcal O$-spans as just proved, and take the sum of the finitely many resulting coherent subsheaves. This gives $F$, and (3.7) is surjective on each member of the cover. PBW makes $\mathcal D_X$ locally free on both structure-sheaf sides. A local finite presentation of $F$, tensored with $\mathcal D_X$ on its left structure-sheaf side, presents $F\otimes\mathcal D_X$ as the cokernel of a map between finite free right operator modules. It is therefore quasi-coherent for its actual right $\mathcal O_X$-action and locally finitely generated over $\mathcal D_X$. Its kernel in (3.7) is quasi-coherent over $\mathcal O_X$ and coherent over $\mathcal D_X$, by the Noetherianity proved in the differential-operator lessons. Apply the same construction to that kernel and then to each successive kernel. The augmentations give the required exact resolution. Its differentials are right $\mathcal D_X$-linear; they need not be induced by maps of the coefficient sheaves $F^p$. $\square$

We next bound the derived transfer tensor without assuming coherence of its direct image. Put
\[
T=\mathcal D_{X\to Y}
=\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}\mathcal D_Y.
\tag{3.8}
\]
The chain-rule action makes this a left $\mathcal D_X$, right $f^{-1}\mathcal D_Y$ bimodule. PBW on $Y$ shows that it is locally free, possibly of infinite rank, over $\mathcal O_X$.

**Lemma 3.3 (transfer amplitude).** For any morphism $f:X\to Y$ of smooth separated varieties, the functor $M\mapsto M\otimes^L_{\mathcal D_X}T$ on right modules has cohomological amplitude $[-d_X,0]$ on modules. Its values have quasi-coherent $\mathcal O_X$-terms in this interval when $M$ is quasi-coherent over $\mathcal O_X$.

**Proof.** Resolve $T$ by the augmented absolute Spencer complex. Its term in degree $-r$ is
\[
S^{-r}=\mathcal D_X\otimes_{\mathcal O_X}
\bigwedge^rT_X\otimes_{\mathcal O_X}T,
\qquad 0\leq r\leq d_X.
\tag{3.9}
\]
The augmentation sends $P\otimes t$ to $Pt$. For local vector fields $\xi_1,\ldots,\xi_r$, the differential is
\[
\begin{aligned}
d(P\otimes\xi_1\wedge\cdots\wedge\xi_r\otimes t)
={}&\sum_a(-1)^{a-1}\bigl(
P\xi_a\otimes\xi_{\widehat a}\otimes t
-P\otimes\xi_{\widehat a}\otimes\xi_at\bigr)\\
&+\sum_{a<b}(-1)^{a+b}P\otimes
[\xi_a,\xi_b]\wedge\xi_{\widehat a\widehat b}\otimes t.
\end{aligned}
\tag{3.10}
\]
The omitted wedges retain their original order. The Leibniz relations make this expression well defined over $\mathcal O_X$. The identities $[\xi,\eta]t=\xi(\eta t)-\eta(\xi t)$ and Jacobi cancel the terms in $d^2$. They also show that the construction agrees on overlapping coordinate charts. Both the augmentation and the differential are left $\mathcal D_X$-linear. They are right $f^{-1}\mathcal D_Y$-linear because the two actions on $T$ commute: $\xi(tQ)=(\xi t)Q$.

Give $S^{-r}$ filtration $F_{m-r}\mathcal D_X\otimes\bigwedge^rT_X\otimes T$, and give the augmented $T$ filtration zero below degree zero and all of $T$ from degree zero onward. In the associated graded, the first summands of (3.10) survive; the action-on-$T$ and bracket summands lower filtration. In étale coordinates the resulting augmented complex is the Koszul resolution for the cotangent variables in
$\mathcal O_X[\zeta_1,\ldots,\zeta_{d_X}]\otimes_{\mathcal O_X}T$.
Its exactness follows by tensoring the polynomial Koszul resolution with the $\mathcal O_X$-flat module $T$. Exactness lifts to the original complex: subtract a boundary with the leading symbol of a cycle, then repeat in lower filtration degrees. Every section has finite filtration degree and the filtration is bounded below, so the procedure terminates.

Each $S^{-r}$ is flat as a left $\mathcal D_X$-module: tensoring a right module with it is tensoring its underlying $\mathcal O_X$-module with $\bigwedge^rT_X\otimes T$, an $\mathcal O_X$-flat module. Thus the bounded complex (3.9) computes derived transfer tensor. After tensoring with $M$, its terms are quasi-coherent over $\mathcal O_X$ when $M$ is. This proves both assertions. $\square$

**Theorem 3.4 (proper D-module coherence).** Let $k$ have characteristic zero and let $f:X\to Y$ be a proper morphism of smooth separated finite-type $k$-varieties. In the left-module conventions (0.1),
\[
f_*:D^b_{\mathrm{coh}}(\mathcal D_X)
\longrightarrow D^b_{\mathrm{coh}}(\mathcal D_Y).
\tag{3.11}
\]
Here coherent means coherent over the differential-operator sheaf, with quasi-coherent underlying structure-sheaf module. No projectivity or holonomicity hypothesis is required.

**Proof.** We first work with right modules and write
\[
f_+M=Rf_{\mathrm{sh},*}
\bigl(M\otimes^L_{\mathcal D_X}T\bigr).
\tag{3.12}
\]
All assertions can be checked on affine opens of $Y$. Fix such an open and choose a finite affine cover of its inverse image, with $c+1$ members. Since $X$ is separated, all finite intersections are affine. The affine quasi-coherent acyclicity and Čech comparison proved in Affine cohomology and Serre's criterion and Čech cohomology therefore bound sheaf cohomology of every quasi-coherent term by $c$.

For a coherent $\mathcal O_X$-module $F$, associativity of derived tensor and the $\mathcal O_X$-flatness of $T$ give a natural right-$f^{-1}\mathcal D_Y$-linear identification
\[
\bigl(F\otimes_{\mathcal O_X}\mathcal D_X\bigr)
\otimes^L_{\mathcal D_X}T
\simeq F\otimes_{\mathcal O_X}T
=F\otimes_{f^{-1}\mathcal O_Y}f^{-1}\mathcal D_Y.
\tag{3.13}
\]
To justify the first equality for a coefficient sheaf that is not flat, take an $\mathcal O_X$-flat resolution of $F$. Its tensor with $\mathcal D_X$ is $\mathcal D_X$-flat and resolves the induced module; after tensoring with $T$ it resolves the ordinary tensor on the right, because $T$ is $\mathcal O_X$-flat. This also proves that induced modules have no positive transfer Tor.

Using the same finite affine Čech cover, the structure-sheaf projection calculation gives
\[
f_+\bigl(F\otimes_{\mathcal O_X}\mathcal D_X\bigr)
\simeq Rf_{\mathrm{sh},*}F\otimes_{\mathcal O_Y}\mathcal D_Y.
\tag{3.14}
\]
Indeed, locally on $Y$ each order piece of $\mathcal D_Y$ is a finite locally free $\mathcal O_Y$-module. Sections on each affine intersection commute with its pullback tensor; tensoring with a finite projective module is a direct summand of tensoring with a finite free module. Pass to the filtered union of the order pieces and then to the finite Čech complex. Filtered unions are exact, and $\mathcal D_Y$ is $\mathcal O_Y$-flat. Hence this calculation commutes with cohomology. The maps multiply on the $\mathcal D_Y$ factor, so (3.14) respects the right operator action, not merely the underlying $\mathcal O_Y$-modules.

For proper $f$, Proper morphisms and coherent direct images, Theorem 4.1 proves that every $R^qf_{\mathrm{sh},*}F$ is coherent over $\mathcal O_Y$. Consequently every cohomology sheaf in (3.14) is coherent over $\mathcal D_Y$.

For any right module $N$ that is quasi-coherent over $\mathcal O_X$, Lemma 3.3 computes its transferred complex in degrees $[-d_X,0]$ with quasi-coherent terms. Applying the finite affine Čech complex places $f_+N$ in $[-d_X,c]$. This bound uses neither coherence of the output nor proper duality.

Now let $M$ be coherent. Use Lemma 3.2 to resolve it by $P^p=F^p\otimes\mathcal D_X$, $p\leq0$, and let $S^\bullet\to T$ be the bounded flat resolution in Lemma 3.3. There are comparison maps
\[
\operatorname{Tot}(P^\bullet\otimes_{\mathcal D_X}S^\bullet)
\longrightarrow M\otimes_{\mathcal D_X}S^\bullet,
\qquad
\operatorname{Tot}(P^\bullet\otimes_{\mathcal D_X}S^\bullet)
\longrightarrow P^\bullet\otimes_{\mathcal D_X}T.
\tag{3.17}
\]
The first is a quasi-isomorphism because each $S^r$ is flat. The second is a quasi-isomorphism because (3.13) makes every induced column acyclic for transfer tensor. The Spencer direction is bounded, so the two double-complex comparisons have finite sums in each total degree. Thus the transferred induced resolution really computes $M\otimes^L_{\mathcal D_X}T$.

This calculation remains valid after sheaf direct image. For clarity, let $A_N$ be the brutal truncation of $P^\bullet$ in degrees $[-N,0]$, and let $K=\ker(P^{-N}\to P^{-N+1})$. Its augmentation gives the triangle
$K[N]\to A_N\to M\to K[N+1]$.
The independent bound just proved puts $f_+K$ in degrees at most $c$. Hence $\mathcal H^n(f_+A_N)\to\mathcal H^n(f_+M)$ is an isomorphism whenever $N>c-n$. The finite truncations therefore compute each fixed output degree once $N$ is large enough.

Apply the finite Čech complex to the transferred resolution. Its vertical degrees lie between zero and $c$, and its horizontal degrees are at most zero. The column filtration yields
\[
E_1^{p,q}=
\bigl(R^qf_{\mathrm{sh},*}F^p\bigr)
\otimes_{\mathcal O_Y}\mathcal D_Y
\quad\Longrightarrow\quad
\mathcal H^{p+q}(f_+M).
\tag{3.15}
\]
This is a spectral sequence of right $\mathcal D_Y$-modules. The differentials are induced by the right-linear maps of the transferred resolution; no $\mathcal O_X$-linearity of its original differentials is assumed.

Convergence here is finite in every total degree. For degree $n$, only $0\leq q\leq c$ and $p=n-q\leq0$ can occur. The filtration on that total degree is thus finite, with at most $c+1$ pieces; incoming and outgoing differentials vanish beyond page $c+1$. The spectral sequence can also be obtained from successively longer finite truncations, whose relevant degree bands stabilize by Lemma 3.3 and the Čech bound. There is no infinite product totalization or inverse-limit term. Every $E_1$ term is coherent by ordinary proper coherence. Kernels, quotients and finite extensions of coherent operator modules are coherent by Noetherianity. The finite limiting filtration therefore makes each $\mathcal H^n(f_+M)$ coherent.

The independent bound $[-d_X,c]$ also proves that only finitely many cohomology sheaves are nonzero. For a complex whose coherent cohomology lies in $[a,b]$, its finite truncation triangles express it in terms of those cohomology modules, shifted by their degrees. The triangulated functor (3.12) then has coherent cohomology in $[a-d_X,b+c]$. A finite affine cover of $Y$ gives a uniform finite bound for the whole variety.

Finally, side change takes a left module $L$ to the right module $\omega_X\otimes_{\mathcal O_X}L$ and a right module on $Y$ back to a left module by $\omega_Y^{-1}\otimes_{\mathcal O_Y}(-)$. The transfer definitions identify (0.1) with
\[
f_*L\simeq\omega_Y^{-1}\otimes_{\mathcal O_Y}
f_+\bigl(\omega_X\otimes_{\mathcal O_X}L\bigr).
\tag{3.16}
\]
These exact equivalences preserve coherence. All constructions above restrict to smaller target opens, and (3.16) is the density-line identification, so the assertions glue. This proves (3.11) for every proper morphism in the stated scope. $\square$


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
for a proper map and a bounded complex with coherent differential-operator cohomology. Theorem 4.7 below proves this for every proper morphism in our smooth separated finite-type convention, including nonprojective maps. We first retain the closed-embedding and projective-product calculations as explicit examples. A general proper morphism need not admit a closed embedding into $\mathbb P^n\times Y$; the general proof uses ordinary proper duality, finite jets and the absolute Spencer complex instead.

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
after $N$ steps. There is a bound on the cohomological degrees of all these cones, independent of the coherent input module. The finite-resolution proof in the earlier duality lesson, Lemma 3.0, gives the bounds $2d_X$ and $2d_Y$. Thus the source dual, including its shift $[d_X]$, is bounded coherent in $[-d_X,d_X]$. Theorem 3.4 bounds its proper direct image, which is (4.7) after side change, by $[-2d_X,c+d_X]$ for a finite affine Čech bound $c$. It also puts $p_*K_N$ in $[-d_X,c]$ with coherent cohomology. The target dual in (4.8) is consequently in $[-c-d_Y,d_X+d_Y]$. For this smooth projection the relative Spencer calculation also puts $p_*K_N$ between degrees $-n$ and $n$. The uniform bound just established uses coherent functors and does not presume structure-sheaf quasi-coherence of operator-Hom cochain terms. Proper coherence used here was proved in Theorem 3.4, including its uniform amplitude bound; Schnell, Theorem 18.1, is a supplementary reference.

Choose a fixed sufficiently large bound $B$ for these degrees. For any fixed $a$, taking $N>a+B$ in (4.10) proves $H^aC(M)=0$. Thus the comparison is an isomorphism for modules. Bounded truncation triangles prove it for coherent complexes. This argument does not assume the existence of a globally bounded free resolution. Restoring the common side-changing line proves (4.2) for $p$. The residue trace is intrinsic, so the construction glues over $Y$. $\square$

The two cases also prove (4.2) for projective morphisms between smooth varieties, by factoring such a morphism as a closed embedding followed by a projective-product projection and composing the two isomorphisms. Theorem 4.7 proves the full nonprojective proper case without this factorization.

### 4.3. Ordinary normalization and the first infinitesimal diagonal

We use cohomological shifts: a sheaf \(A[d]\) has its cohomology in degree \(-d\). Throughout, \(k\) has characteristic zero, and the schemes called smooth are separated and of finite type over \(k\). Write

\[
K_X=\omega_X[d_X],\qquad
\omega_X=\bigwedge^{d_X}\Omega^1_{X/k},\qquad
T_X=\mathcal Hom_{\mathcal O_X}(\Omega^1_{X/k},\mathcal O_X).
\]

For readability we assume pure dimensions. Apply the construction on the open and closed smooth components when their dimensions differ. The right action on the canonical bundle is
\(\phi\cdot\xi=-\mathcal L_\xi\phi\).

The ordinary inputs are the following exact earlier programme results. In The right adjoint of derived pushforward, Proposition 1.1 gives associative composition of the ordinary right adjoints \(a_f\), Theorem 2.3 gives restriction over an open of the target for proper maps and bounded-below quasi-coherent inputs, Theorem 3.1 gives derived finite coinduction and its evaluation-at-one counit, and Theorem 4.2 gives the relative projective-bundle adjoint with its ordered Čech trace. We use the comparison proofs of Propositions 6.1–6.2 only for the explicitly constructed compactifications specified below: their common-graph, restriction and adjoint-composition arguments require existing compactifications, and do not invoke the general Nagata existence assertion. The determinant and regular-sequence computations in Dualizing sheaves and Serre duality for projective schemes, Section 5 and Proposition 8.2, give the local conormal Koszul calculation. Below we perform the extension beyond projective schemes and the finite-jet calculation; neither extension is being inferred merely from the name of an earlier theorem.

**Lemma 4.3 (ordinary proper normalization).** For a proper morphism \(f:X\to Y\) between the smooth schemes above, there is a canonical normalization

\[
a_fK_Y\simeq K_X,\qquad
\operatorname{Tr}_f:Rf_*K_X\longrightarrow K_Y.
\tag{4.11}
\]

The second map is the ordinary counit under the first identification. These identifications restrict compatibly to target opens. For composable proper maps they respect adjoint composition, and their traces satisfy ordinary trace transitivity. Projectivity of \(f\) is not required.

**Proof.** First consider a projective bundle \(\pi:P=\mathbf P_Y^N\to Y\). The earlier ordered trace identifies \(a_\pi\mathcal O_Y\) with \(\omega_{P/Y}[N]\). It also gives

\[
a_\pi K_Y\simeq \pi^*K_Y\otimes\omega_{P/Y}[N]
\simeq\omega_P[d_Y+N].
\]

Here is the extension from input \(\mathcal O_Y\) to \(K_Y\). For a perfect complex \(Q\) on \(Y\), perfect duality and the projection formula identify

\[
\begin{aligned}
\operatorname{Hom}_P(L,a_\pi\mathcal O_Y\otimes\pi^*Q)
&=\operatorname{Hom}_P(L\otimes\pi^*Q^\vee,a_\pi\mathcal O_Y)\\
&=\operatorname{Hom}_Y(R\pi_*L\otimes Q^\vee,\mathcal O_Y)\\
&=\operatorname{Hom}_Y(R\pi_*L,Q).
\end{aligned}
\]

These identifications are natural in \(L\), so adjunction identifies the displayed object with \(a_\pi Q\). Its counit is the earlier ordered trace tensored with \(Q\). Take \(Q=K_Y\), which is a shifted line bundle. The determinant of the smooth differential sequence identifies the resulting line with \(\omega_P\); use base differentials followed by relative differentials as the exterior order.

Let \(i:U\hookrightarrow P\) be a closed immersion with \(U/k\) smooth of dimension \(d_X\). Near \(U\), its ideal is generated by a regular sequence of length \(c=d_Y+N-d_X\). This follows from the earlier smooth presentation and regular-parameter result: the independent conormal classes can be completed to regular parameters of the smooth ambient local ring. If the sequence is \(z_1,\ldots,z_c\), its ordered Koszul resolution gives

\[
a_i\bigl(\omega_P[d_Y+N]\bigr)
\simeq
\bigl(\omega_P|_U\otimes\det(I/I^2)^\vee\bigr)[d_Y+N-c]
\simeq\omega_U[d_X].
\]

For the last isomorphism take the determinant of
\(0\to I/I^2\to\Omega^1_{P/k}|_U\to\Omega^1_{U/k}\to0\).
All other Koszul Ext sheaves vanish. Replacing the regular equations by another set multiplies their top exterior product by the change-of-generators determinant; the dual Koszul term changes by its inverse. These factors cancel in the displayed determinant quotient. Thus this is a normalization of the adjoint, including its counit, rather than an isomorphism of line bundles chosen up to a scalar. The counit is the finite-coinduction evaluation map followed by the ordered projective-bundle trace.

We fix the Koszul-Hom and shift sign by this counit convention. For a section followed by its smooth projection, the composite is the identity map and its composite adjoint counit is \(+\mathrm{id}\). In coordinates with base forms first and relative forms second, the simple-pole class \(dx\wedge d\delta/(\delta_1\cdots\delta_d)\) consequently represents \(+dx\) after the section adjoint and trace. This fixes the sign when conormal factors are moved past base factors; it is the same convention as the earlier ordered Čech trace. All subsequent Koszul bases, tensor products and determinant identifications use this convention. Changing the order of equations changes both the exterior basis and its dual with the usual alternating signs.

Now work over an affine open of \(Y\), using the proper restriction theorem. Take an affine open \(U\subset X\). Its coordinate ring is a finite-type algebra over the affine base ring, so finite algebra generators give a closed immersion \(U\hookrightarrow\mathbf A_Y^N\). Let \(Z\subset\mathbf P_Y^N\) be its scheme-theoretic closure. Then \(Z\to Y\) is projective and \(U\subset Z\) is open. Let \(W\) be the scheme-theoretic closure of the graph of the two inclusions of \(U\) in \(X\times_Y Z\). The projections
\(h:W\to X\) and \(q:W\to Z\) are proper: both factors are proper over \(Y\), and \(W\) is closed in their fibre product.

Both \(h^{-1}(U)\) and \(q^{-1}(U)\) are exactly the common copy of \(U\), scheme-theoretically. Over \(U\subset X\), the graph \(U\to Z\) is already closed because \(Z/Y\) is separated. Over \(U\subset Z\), the graph \(U\to X\) is already closed because \(X/Y\) is separated. Scheme-theoretic closure restricts to an open by restriction of its defining kernel ideal, so it adds no points or nilpotents over either of these opens. Write \(s:Z\to Y\). The identities \(fh=sq\), adjoint composition, and proper restriction therefore give

\[
(a_fK_Y)|_U
\simeq(a_ha_fK_Y)|_U
\simeq(a_qa_sK_Y)|_U
\simeq(a_sK_Y)|_U.
\]

In these expressions, restriction on \(W\) is to its common open \(U\); the restrictions of \(h\) and \(q\) are identity maps. To compute the last object, write \(s=\pi i\) with \(i:Z\hookrightarrow\mathbf P_Y^N\). Remove the closed subset \(Z\setminus U\) from the ambient projective space. On the remaining ambient open, \(U\) is closed, both \(U\) and the ambient scheme are smooth over \(k\), and the conormal calculation just performed applies. Proper restriction for the finite map \(i\) gives \((a_sK_Y)|_U\simeq\omega_U[d_X]\). Every map used in this comparison is an adjunction comparison or ordinary restriction.

We check its choices and overlaps. For two projective closures of the same \(U\), take the closure of its diagonal graph in their product over \(Y\). Its projections are proper and are identity maps precisely over \(U\), by the same closed-graph argument. Compare both constructions through this refinement. Their adjoint comparisons coincide because transposing either route gives the same composite pushforward counit. Associativity of adjoint composition and of restriction makes this equality persist under a further refinement.

The determinant identification is also the same through this comparison. One may compute in the product of the two projective ambient spaces. Locally first impose the equations for \(U\) in the first ambient space and then the equations for the graph of its map to the second factor. The latter equations have the form \(v_j-b_j\); they are a regular sequence, even over a ring with nilpotents, because each is monic in a new variable. Their ordered Koszul complex computes the adjoint for this graph. In the conormal determinant, its vertical differentials cancel the relative canonical differentials of the second projective factor. The evaluation counit for the resulting identity map is evaluation at \(1\), so this cancellation has coefficient \(1\), not an unspecified unit. Computing in the opposite order gives the same result by the composition of these Koszul Hom adjunctions. Permuting a Koszul exterior basis and the corresponding determinant basis introduces the same alternating sign on both sides. This is the determinant transition already checked in the earlier conormal calculation.

For distinct affine opens \(U,V\subset X\), cover their intersection by affine opens and apply this common-product comparison to the restricted embeddings. It identifies both local normalizations with the ordinary restricted canonical bundle on every such open. The transitions are consequently the determinant transitions of \(\omega_X\); they satisfy the cocycle identity, not merely a scalar equivalence. Locally \(a_fK_Y\) has its single cohomology sheaf in degree \(-d_X\). Globally its truncation identifies it with that sheaf shifted by \(d_X\), and the local line-bundle identifications just proved glue to (4.11).

The same comparison proves compatibility with proper composition. On an affine open of the source mapping into an affine open of an intermediate smooth scheme, choose relative affine embeddings at the two stages. Their composite is an affine embedding in the product coordinate space. Appending the equations at the second stage gives the composite ordered Koszul resolution, and its top determinant is the determinant of the composite conormal sequence. Derived finite coinduction is associative, and the relative projective traces compose by their adjunction triangle identities. Hence the local normalization of \(a_fa_gK_Z\simeq a_{gf}K_Z\) is the normalization of \(K_X\). The common graph refinements above make the comparison independent of these local embeddings and show the assertion on overlaps. The counit of a composite adjunction is the first counit pushed forward and then the second one; this gives the stated trace transitivity.

For the finite-diagonal comparisons below we need only the ordinary extraordinary inverse image on a particular class of maps, with explicit compactifications. If \(S\) is affine of finite type over \(k\), finite algebra generators embed \(S\) closed in an affine space. Its projective closure \(\overline S\) is an explicit compactification of its absolute structure map. Define \(K_S^{\mathrm{aff}}\) to be the restriction of \(a_{\overline S\to\operatorname{Spec}k}k\). If \(S\) is smooth, the ambient conormal calculation gives \(K_S^{\mathrm{aff}}=\omega_S[\dim S]\), with the determinant normalization already established.

For a map \(u:S\to T\) between affine finite-type schemes, take its explicit relative projective closure in \(\mathbf P_T^N\), and define \(u^!\) by restricting the ordinary adjoint of that proper closure. The comparison proof of the earlier Proposition 6.1 applies to any two compactifications already in hand: close the graph of \(S\) in their fibre product over \(T\), whose projections are proper and are identity maps exactly over \(S\). Proper restriction and associative adjoint composition identify the two restrictions. Taking a further graph refinement proves equality of the comparison maps and their cocycle identity. No compactification-existence theorem is needed for this argument.

Composition here also uses explicitly supplied compactifications. For \(S\to T\to V\) with affine source schemes, first take the relative projective closure \(\overline T\to V\) of \(T\to V\). To compactify \(S\to\overline T\), close its graph in \(\overline S\times_k\overline T\), using the explicit absolute projective closure \(\overline S\) just constructed. The projection is proper over \(\overline T\), and its inverse image over the open \(S\subset\overline S\) is the graph itself, so it contains \(S\) as an open. This gives the nested compactifications needed in the proof of the earlier Proposition 6.2. Restriction over \(T\), ordinary proper adjoint composition and the preceding common refinements prove the associative comparison \((vu)^!\simeq u^!v^!\). Applying it to the absolute structure maps gives \(u^!K_T^{\mathrm{aff}}\simeq K_S^{\mathrm{aff}}\). All schemes compactified in this paragraph have affine source, and all their compactifications have been constructed.

There is one further available compactification that will be used. For the affine open \(U\subset X_V=f^{-1}V\) above, the proper morphism \(X_V\to V\), together with \(U\hookrightarrow X_V\), is itself a compactification of \(f|_U:U\to V\). Compare it with the relative projective closure of \(U\to V\) using the same common graph \(W\). It identifies \((a_fK_Y)|_U\) with \((f|_U)^!K_V^{\mathrm{aff}}\); this is exactly the graph comparison already proved. These local comparisons agree on smaller affine opens by the common-refinement cocycle and the conormal determinant transitions. They identify (4.11) with the associative comparisons of the explicit affine construction. For proper composition, compare on such affine source opens; the normalizing maps are maps between the single cohomology sheaves shifted by \(d_X\), so equality of their restrictions is equality of the sheaf maps. Transposing this global equality under the proper adjunctions gives trace transitivity. We do not define or invoke a global \(p_X^!\) for an arbitrary nonproper, nonaffine \(X\). \(\square\)

**Lemma 4.4 (finite-jet traces and the first Spencer obstruction).** Let \(J_X\) be the first infinitesimal diagonal in \(X\times_kX\), with projections \(p_1,p_2:J_X\to X\), and put
\(P_X^1=(p_1)_*\mathcal O_{J_X}\).
Both projections are finite flat. Their normalized finite adjoints of \(K_X\) identify with one object \(K_{J_X}\). Set
\(H_X=\mathcal Hom_{\mathcal O_X}(P_X^1,\omega_X)\), so \((p_1)_*K_{J_X}=H_X[d_X]\).
The two finite traces, written in the \(p_1\)-splitting of \(H_X\), have the formulas proved below. For proper \(f:X\to Y\), their proper comparison proves the vanishing of the first Spencer obstruction in \(D(\mathcal O_Y)\), and hence under induction adjunction in \(D(\mathcal D_Y^{\mathrm{op}})\).

**Proof of finite duality and its normalization.** Choose étale coordinates \(x_1,\ldots,x_d\) on an affine open \(U=\operatorname{Spec}R\subset X\), where \(d=d_X\). The formal lifting property of an étale algebra identifies the first principal-parts algebra with

\[
B=R[\delta_1,\ldots,\delta_d]/(\delta_1,\ldots,\delta_d)^2,
\qquad p_1(a)=a,\qquad p_2(a)=a+\sum_i\partial_i(a)\delta_i.
\]

Thus \(B\) is free of rank \(d+1\) for \(p_1\). Interchanging the two factors proves the same assertion for \(p_2\). These local statements show that the projections are finite flat globally. Separation ensures that the infinitesimal diagonal is closed; its underlying topological space is \(X\).

Here is a computation of the finite dual that also fixes its trace. Put \(A=R[\delta_1,\ldots,\delta_d]\) and
\(C=A/(\delta_1^2,\ldots,\delta_d^2)\).
The sequence defining \(C\) is regular: successively quotienting leaves a polynomial algebra in the next variable over the preceding quotient, and multiplication by the monic polynomial \(\delta_i^2\) is injective there. The ordered Koszul resolution of \(C\) gives its dualizing module relative to \(R\). Realize that dual in the top Čech local-cohomology module for the variables \(\delta_i\). This module has \(R\)-basis the negative monomials
\(\delta_1^{-a_1-1}\cdots\delta_d^{-a_d-1}\), \(a_i\geq0\), with volume \(dx_1\wedge\cdots\wedge dx_d\wedge d\delta_1\wedge\cdots\wedge d\delta_d\). Terms with a nonnegative exponent in at least one variable are zero because they come from a Čech summand missing that localization. The dual power-Koszul map sends the top dual Koszul generator for \(C\) to the class with every denominator squared. This can be checked one variable at a time from the complex \(A\xrightarrow{\delta_i^2}A\); tensoring in the indicated exterior order gives the multivariable map.

Multiplication followed by extraction of the simple-pole coefficient identifies this annihilator of all \(\delta_i^2\) with \(\operatorname{Hom}_R(C,\omega_R)\). In particular the class with all denominators squared corresponds to the functional extracting the coefficient of \(\delta_1\cdots\delta_d\). The normalization is the canonical one. In \(\mathbf P_R^d\), the homogeneous equations \(T_1^2,\ldots,T_d^2\) define a closed scheme entirely contained in \(T_0\ne0\): a chart where some \(T_i\), \(i>0\), is invertible is empty on that scheme. On \(T_0\ne0\), its algebra is exactly \(C\). Adjoint composition therefore expresses its finite counit as the closed-immersion Koszul counit followed by the projective-bundle trace.

Here is the explicit ordered class comparison. Put
\[
\Omega=\sum_{j=0}^d(-1)^jT_j\,
 dT_0\wedge\cdots\wedge\widehat{dT_j}\wedge\cdots\wedge dT_d.
\]
The ordered projective class is \([\Omega/(T_0\cdots T_d)]\). On \(T_0=1\), it is \([d\delta_1\wedge\cdots\wedge d\delta_d/(\delta_1\cdots\delta_d)]\). The ordered support Čech comparison sends this affine fraction to that projective class, and the earlier Theorem 4.2 sends the latter to \(1\). The Koszul-Hom sign is the section convention fixed above, so this is \(+1\). The transition from the Koszul complex on \(\delta_i^2\) to the one on \(\delta_i\) multiplies its top exterior generator by \(\delta_1\cdots\delta_d\); dualizing sends the simple-pole class to that same multiple of the all-squared-denominator class. Thus the power-Koszul map uses the same sign and normalization. The resulting finite trace of a functional \(\lambda\) is exactly \(\lambda(1)\). This proves compatibility with the ordinary finite adjunction, rather than only an abstract identification of Ext modules.

Now use the quotient \(C\twoheadrightarrow B\). Finite derived-Hom adjunction gives

\[
R\operatorname{Hom}_C
  \bigl(B,\operatorname{Hom}_R(C,\omega_R)\bigr)
\simeq R\operatorname{Hom}_R(B,\omega_R).
\]

Both \(C\) and \(B\) are finite free over \(R\); the right side is therefore the ordinary module \(\operatorname{Hom}_R(B,\omega_R)\) in degree zero. The left side is its finite-coinduction realization, with the evaluation counit. In the fraction model it is the annihilator of \((\delta)^2\), not the Koszul dual of a purported regular sequence \((\delta)^2\). Among the basis monomials already described, the annihilator consists exactly of the simple-pole term and the terms with one squared denominator. Indeed multiplication by \(\delta_i\delta_j\) kills these terms, whereas it detects a term having squared denominators in both \(i\) and \(j\); distinct remaining monomials are \(R\)-linearly independent. Consequently a functional \(\lambda\), with
\(\alpha=\lambda(1)\) and \(\beta_i=\lambda(\delta_i)\), has the normalized representative

\[
\lambda\ \longleftrightarrow
\frac{\alpha\wedge d\delta_1\wedge\cdots\wedge d\delta_d}
     {\delta_1\cdots\delta_d}
 +\sum_i
\frac{\beta_i\wedge d\delta_1\wedge\cdots\wedge d\delta_d}
     {\delta_1\cdots\delta_i^2\cdots\delta_d}.
\tag{4.12}
\]

Multiplication by \(1\) or by \(\delta_i\) and simple-pole extraction verifies the two evaluations directly. Finite trace transitivity from \(C\) to \(B\) preserves evaluation at \(1\). This proves the required coinduction formula without declaring the first-jet ideal regular.

**The second projection.** Write \(u_i=x_i+\delta_i\). Formal étaleness uniquely lifts this substitution to the completed ambient rings: the inverse substitution is \(x_i=u_i-\delta_i\). We need only its finite Taylor terms in (4.12). It is not being asserted that this is an automorphism of an arbitrary uncompleted étale chart. The total volume is unchanged:
\(dx_1\wedge\cdots\wedge dx_d\wedge d\delta_1\wedge\cdots\wedge d\delta_d
=du_1\wedge\cdots\wedge du_d\wedge d\delta_1\wedge\cdots\wedge d\delta_d\).
All mixed terms vanish by the exterior repetition of a \(d\delta_i\).

The formal substitution computes the canonical algebraic comparison. To see this, take the common ambient scheme in \(U_x\times U_u\times\mathbf A^d_\delta\) cut out by \(u_i-x_i-\delta_i\). Its projections to \(U_x\times\mathbf A^d_\delta\) and \(U_u\times\mathbf A^d_\delta\) are étale, by base change of the étale coordinate maps. Near the diagonal at \(\delta=0\), remove the other components of that fibre; the two projections then induce the identity on the support and the unique isomorphisms on every nilpotent thickening of it. Pull the ordered power-Koszul complexes back to this common ambient scheme. Flat étale pullback preserves their resolutions, their top dual classes and their Čech localization maps. The finite-coinduction step to the first jets is the same quotient on both sides. The ambient volume identity above and the ordered trace normalization therefore identify the same canonical duality class. Completion is only a means of writing its finite Taylor coefficients; no separate formal-residue comparison theorem is being assumed.

For \(\beta_i=b_i(x)\,dx_1\wedge\cdots\wedge dx_d\), expansion gives \(b_i(u-\delta)=b_i(u)-\sum_j\partial_jb_i(u)\delta_j+\cdots\). In the term with its \(i\)-th denominator squared, only the \(j=i\) linear term can contribute to the simple-pole coefficient. The other linear terms and every higher term lack a pole in some variable and are zero in top Čech local cohomology. The simple-pole term with coefficient \(\alpha\) contributes only its constant Taylor term. The finite trace for \(p_2\) is therefore

\[
t_{1,X}(\alpha,\beta)=\alpha,
\qquad
t_{2,X}(\alpha,\beta)
 =\alpha-\sum_i\mathcal L_{\partial_i}\beta_i
 =\alpha-\operatorname{div}_X\beta,
\qquad
\operatorname{div}_X\beta=d(\iota_\beta).
\tag{4.13}
\]

Here \(\beta\in\omega_X\otimes T_X\), and \(\iota_\beta\) contracts its vector field into its top form. On a simple tensor, \(d(\iota_\xi\phi)=\mathcal L_\xi\phi\), because a top form has zero exterior derivative. This description is intrinsic. The contraction is balanced over \(\mathcal O_X\), and the formula
\(\operatorname{div}_X(a\beta)=a\operatorname{div}_X\beta+\beta(da)\)
shows that it is well defined also when a coefficient is moved between the vector field and the top form.

The local-cohomology model is a finite-coinduction model of the normalized ambient dual. On an affine \(U\subset X\), the first-jet scheme \(J_U\) is affine because it is finite over \(U\). The explicit affine construction at the end of Lemma 4.3 identifies \(a_{p_1^U}K_U\) and \(a_{p_2^U}K_U\) with \(K_{J_U}^{\mathrm{aff}}\): the two absolute structure maps of this affine scheme are equal, and finite \(p_i^U\) themselves need only their identity-open proper compactifications. These comparisons use the explicit absolute projective closures of \(U,J_U\), and their proper common graphs. Formula (4.12) and the common étale ambient calculation fix their canonical comparison and counits. On smaller affine opens the comparisons agree by the same refinement cocycle and determinant transitions. They therefore glue to \(K_{J_X}=a_{p_1}K_X\simeq a_{p_2}K_X\). No absolute compactification or global extraordinary inverse image for \(X\) or \(J_X\) has been used. For \(d=0\), \(P_X^1=\mathcal O_X\); both traces are the identity and the divergence term is absent.

**Module structures.** The \(p_1\)-splitting is canonical because \(P_X^1=\mathcal O_X\oplus\Omega^1_{X/k}\) as a left \(\mathcal O_X\)-module, with its square-zero differential ideal. A first-jet functional is thus a pair \(\alpha\in\omega_X\), \(\beta\in\omega_X\otimes T_X\). Its two module structures are

\[
a\cdot_{p_1}(\alpha,\beta)=(a\alpha,a\beta),
\qquad
a\cdot_{p_2}(\alpha,\beta)
 =(a\alpha+\beta(da),a\beta),
\qquad
s_X(\beta)=(\operatorname{div}_X\beta,\beta).
\tag{4.14}
\]

The Leibniz formula shows that \(s_X\) is \(\mathcal O_X\)-linear for the \(p_2\)-structure, and (4.13) gives \(t_{2,X}s_X=0\) as an actual sheaf map. Moreover \(H_X\simeq\omega_X\otimes\mathcal D_X^{\leq1}\): send \((\alpha,\sum_i\beta_i\otimes\partial_i)\) to \(\alpha\otimes1+\sum_i\beta_i\otimes\partial_i\). The decomposition of an order-one operator into its value on \(1\) and its derivation part makes this identification independent of coordinates. Since \(\xi a=a\xi+\xi(a)\), right multiplication by \(a\) on this induced module is exactly the \(p_2\)-action in (4.14). The restriction of the right-D action map to order at most one is \(t_{2,X}\), because \(\phi\cdot\xi=-\mathcal L_\xi\phi\).

**Proper comparison and the obstruction.** The map \(f\times f\) induces a map \(g:J_X\to J_Y\). It factors through \(J_Y\) because diagonal ideals, and their squares, pull back into the corresponding diagonal ideals of \(X\times X\). It is proper: its composition with the closed immersion \(J_Y\hookrightarrow Y\times Y\) is proper, and base change to any \(J_Y\)-scheme is the same base change of that composition. The identities \(p_i^Yg=fp_i^X\) hold for both \(i\).

Here is the proper normalization for \(g\) and the verification of both finite-trace squares. Take an affine \(V\subset Y\) and an affine \(U\subset f^{-1}V\). The schemes \(J_V,J_U\) are affine, and all four maps in the squares
\[
p_i^V(g|_{J_U})=(f|_U)p_i^U,\qquad i=1,2,
\]
have affine source and target. The explicit affine construction therefore gives the associative normalization
\((g|_{J_U})^!K_{J_V}^{\mathrm{aff}}\simeq K_{J_U}^{\mathrm{aff}}\), compatible with both finite \(p_i\) comparisons. There is also an available compactification of \(g|_{J_U}\): use the open inclusion \(J_U\hookrightarrow J_{f^{-1}V}\) followed by the given proper map \(g_V:J_{f^{-1}V}\to J_V\). Its proper common graph with the relative projective closure of \(J_U\to J_V\) identifies
\[
(a_gK_{J_Y})|_{J_U}\simeq
(g|_{J_U})^!K_{J_V}^{\mathrm{aff}}\simeq K_{J_U}^{\mathrm{aff}}.
\]
The same comparisons agree on affine overlaps. Their local value has a single cohomology sheaf in degree \(-d_X\), by the finite-flat coinduction computation. Thus they glue as actual sheaf isomorphisms to \(a_gK_{J_Y}\simeq K_{J_X}\). Define \(\operatorname{Tr}_g\) by this normalization and the ordinary proper counit.

For each \(i\), compare the proper-adjoint composition
\(a_g a_{p_i^Y}K_Y\simeq a_{p_i^X}a_fK_Y\) with these normalizations. On \(J_U\) it is exactly the associative comparison of the displayed affine square, with the explicit compactifications just given; common proper refinements prove equality of the comparisons. Globally both normalized objects have their single cohomology sheaf in degree \(-d_X\). Consequently these normalizing isomorphisms are equal globally, since their actual sheaf maps are equal on the affine cover \(J_U\). Transpose this equality under the global **proper** adjunctions. It gives
\[
t_{i,Y}\,R(p_i^Y)_*\operatorname{Tr}_g
=\operatorname{Tr}_f\,Rf_*t_{i,X},\qquad i=1,2,
\]
with the pushforward composition identifications understood. These are the two required trace squares in their respective derived \(\mathcal O_Y\)-module categories. We have checked the normalization maps before transposition; we have not assumed that arbitrary derived trace maps are detected on source affine opens.

Let \(L_Y=\mathcal D_Y^{\leq1}\), with its coefficient left \(\mathcal O_Y\)-action and its multiplication right \(\mathcal O_Y\)-action. Restriction of first jets gives a map
\(r:H_X\to\omega_X\otimes f^*L_Y\),
\(r(\alpha,\beta)=(\alpha,df(\beta))\).
It is \(f^{-1}\mathcal O_Y\)-linear for the right actions just specified: the extra term under multiplication by \(a\in\mathcal O_Y\) is \(\beta(d f^*a)=df(\beta)(da)\). For the coefficient \(p_1\)-actions it is also an \(\mathcal O_X\)-linear map. Transport the \(P_Y^1\)-action from \(H_Y\) to \(\omega_Y\otimes L_Y\): the nilpotent element represented by \(da\) sends a vector-field coefficient \(\beta\) to the constant coefficient \(\beta(da)\), and kills the constant coefficient. On the source, that element acts by contraction with \(d f^*a\). Thus \(r\) preserves these actions. In the following projection formula use the coefficient \(p_1\)-actions and the local freeness of \(L_Y\) on its left; retain its right action as well. The underlying pushforward is through the same topological map for either projection. This gives

\[
\operatorname{Tr}_g
 = (\operatorname{Tr}_f\otimes L_Y)\,Rf_*r:
 Rf_*(H_X[d_X])\longrightarrow H_Y[d_Y].
\tag{4.15}
\]

This equality is in \(D(P_Y^1)\), before restriction through either projection. To verify it, apply finite \(p_1^Y\)-coinduction adjunction. Both maps transpose to \(\operatorname{Tr}_f\circ Rf_*t_{1,X}\), by the \(p_1\) trace square. More explicitly, multiplication by the target differential generator \(\delta y_j\) evaluates a source functional on
\(\sum_i(\partial_i f^*y_j)\delta x_i\). Thus the coinduced map has its constant component \(\operatorname{Tr}_f(\alpha)\) and its \(j\)-th differential component \(\operatorname{Tr}_f(\sum_i(\partial_i f^*y_j)\beta_i)\), exactly as in the right side of (4.15). Finite adjunction proves the equality of the derived module maps, not only an equality after forgetting their module structures.

The ordinary trace induces an actual right-\(\mathcal D_Y\) morphism
\(t_0:E_0\to K_Y\), where \(E_0=Rf_*K_X\otimes\mathcal D_Y\), by derived induction adjunction. The first Spencer column is
\(E_1=Rf_*(\omega_X\otimes T_X)[d_X]\otimes\mathcal D_Y\).
Before the global shift \([d_X]\), use the convention \(d_1(\phi\otimes\xi\otimes Q)=(\phi\cdot\xi)\otimes Q-\phi\otimes(\xi\cdot Q)\). Its induced generator, regarded inside order at most one, is
\(-r s_X(\xi\otimes\phi)\).
Indeed its constant coefficient is \(-\mathcal L_\xi\phi\) and its target vector-field coefficient is \(-df(\xi)\phi\). With the usual shifted-complex differential, the global shift \([d_X]\) multiplies this boundary by \((-1)^{d_X}\).

Take its composition with \(t_0\) and test it through derived induction adjunction. Apart from that explicitly specified common factor \((-1)^{d_X}\), the resulting \(\mathcal O_Y\)-derived map is

\[
-t_{2,Y}\operatorname{Tr}_g Rf_*s_X
 =-\operatorname{Tr}_f Rf_*(t_{2,X}s_X)
 =0
\quad\text{in }D(\mathcal O_Y).
\tag{4.16}
\]

Every map in this last equality is \(\mathcal O_Y\)-linear for the \(p_2\)-structures: \(s_X\) is \(p_2\)-linear, (4.15) is a derived \(P_Y^1\)-module map, and \(t_{2,Y}\) is the finite counit for \(p_2^Y\). The middle equality is the \(p_2\) proper trace square. Consequently this is the zero of the actual induction-adjoint obstruction; no faithfulness of the forgetful functor to \(k\)-sheaves is asserted or needed. In local coordinates its expression is the familiar integration-by-parts identity, but the proof of its zero is (4.16) in the module-derived category.

For clarity, that calculation can also be represented by strict complexes. Resolve \(K_Y\) by a bounded-below injective complex \(J\) of right D-modules. Its underlying \(\mathcal O_Y\) terms are injective, since induction \(A\mapsto A\otimes\mathcal D_Y\) is exact by PBW and is left adjoint to forgetting. Represent the ordinary trace by a chain map \(T:A_0\to J\) from a finite affine Čech model of \(Rf_*K_X\). The coinduced first-jet map is the \(P_Y^1\)-linear diagonal chain map \((T,Tdf)\) between the \(p_1\)-splittings. For the \(p_2\)-splitting of \(\mathcal Hom(P_Y^1,J)\), use \(\beta\mapsto(\operatorname{div}_J\beta,\beta)\), where \(\operatorname{div}_J(m\otimes\xi)=-m\cdot\xi\). The D-linearity of the differential makes this a chain map, and the right-module Leibniz identity makes it \(p_2\)-linear. It restricts on \(K_Y\) to the normalization (4.13). The \(p_2\) trace square says that the second-component map \(T\operatorname{div}_X-\operatorname{div}_J(Tdf)\) is zero in \(D(\mathcal O_Y)\); its negative is the first Spencer obstruction. This gives the same zero as (4.16) with actual chain representatives. \(\square\)


### 4.4. Lifting the trace through the Spencer complex

**Lemma 4.5 (the proper differential-operator trace).** The ordinary trace (4.11) extends uniquely to a right differential-operator morphism
\[
\tau_f:f_+K_X\longrightarrow K_Y.
\tag{4.17}
\]
Here $f_+$ is the right-module functor (3.12), and uniqueness means uniqueness after prescribing the ordinary trace on the canonical induced zero column. These traces respect target restriction and proper composition.

**Proof.** Put $F_r=\omega_X\otimes\bigwedge^rT_X$. Tensor the absolute Spencer resolution (3.9) with the right module $K_X=\omega_X[d_X]$, then take derived sheaf direct image. Filter by columns $0,\ldots,r$; call the resulting object $C_r$. The complex is finite, and its differentials commute with the right target operators, so this is a filtration of the actual object in $D(\mathcal D_Y^{\mathrm{op}})$. Its successive triangles are
\[
C_{r-1}\longrightarrow C_r\longrightarrow E_r[r]
 \longrightarrow C_{r-1}[1],
\qquad
E_r=Rf_{\mathrm{sh},*}F_r[d_X]\otimes_{\mathcal O_Y}\mathcal D_Y.
\tag{4.18}
\]
The projection identification is (3.14), applied to each coefficient column. We have $C_0=E_0$ and $C_{d_X}=f_+K_X$.

Right induction $A\mapsto A\otimes_{\mathcal O_Y}\mathcal D_Y$ is exact by PBW and left adjoint to forgetting the right operator action. It therefore gives the derived adjunction as well: forgetting a K-injective right-operator complex leaves an $\mathcal O_Y$-K-injective complex, since its Hom against an acyclic coefficient complex is Hom against the acyclic induced complex. Ordinary proper adjunction and (4.11) now give
\[
\begin{aligned}
\operatorname{Hom}_{D(\mathcal D_Y^{\mathrm{op}})}(E_r,K_Y[s])
&=\operatorname{Hom}_{D(\mathcal O_Y)}
       (Rf_*F_r[d_X],K_Y[s])\\
&=\operatorname{Hom}_{D(\mathcal O_X)}(F_r,\omega_X[s])
 =\operatorname{Ext}_{\mathcal O_X}^{s}(F_r,\omega_X).
\end{aligned}
\tag{4.19}
\]
These are global derived Hom groups on the indicated inverse image of a target open. In particular they vanish for $s<0$, since both coefficient arguments are sheaves.

The induction adjoint of $\operatorname{Tr}_f$ is a right-$\mathcal D_Y$ map $\tau_0:E_0\to K_Y$. To extend a map $C_{r-1}\to K_Y$ across (4.18), its obstruction belongs to
$\operatorname{Hom}(E_r,K_Y[1-r])$. At $r=1$ this is the composition with the first Spencer boundary. Lemma 4.4 proves its zero in the actual induction-adjoint category $D(\mathcal O_Y)$, including the shifted differential's sign, so the first extension exists. For $r\geq2$, (4.19) makes the obstruction group zero. At every $r\geq1$, two extensions differ by the image of $\operatorname{Hom}(E_r,K_Y[-r])$, which is zero by the same formula. Successive triangles therefore give the unique extension (4.17).

This construction supplies a derived operator map, including its homotopies. Indeed choose complexes for the finite column filtration and a K-injective right-$\mathcal D_Y$ target. A representative on column $r$ has Hom degree $-r$; the chain-map equation asks that its Hom differential be the signed composition of the previous component with the Spencer boundary. The first such cycle has zero class by Lemma 4.4. Each later cycle is closed because the preceding equations hold and the Spencer differential squares to zero; its class is in the negative group (4.19). Thus the equations can be solved successively. The same negative groups make two solutions homotopic relative to the zero column. More generally, for $j>0$ the finite filtration and (4.19) give $\operatorname{Hom}(C_{d_X},K_Y[-j])=0$. There is no replacement of an operator-derived map by a statement about underlying $k$-linear operators.

The zero-column map $E_0\to f_+K_X$ is intrinsic. It is obtained by applying transfer and pushforward to the induction counit
$\omega_X\otimes_{\mathcal O_X}\mathcal D_X\to\omega_X$, shifted by $d_X$; in the Spencer model it is precisely the zero-column inclusion. Consequently coordinate changes and changes of resolutions preserve the specified $\tau_0$. Uniqueness proves independence of these choices and target-open compatibility.

For proper $X\xrightarrow fY\xrightarrow gZ$, transfer composition identifies $g_+f_+$ with $(gf)_+$. Applying the induced calculation (3.14) to the zero column identifies $g_+E_0^f$ with $E_0^{gf}$, and the two counit maps to $(gf)_+K_X$ agree. The composite $\tau_g\circ g_+\tau_f$ restricts there to the induction adjoint of $\operatorname{Tr}_g\circ Rg_*\operatorname{Tr}_f$. By ordinary trace transitivity this is the prescribed zero-column map for $gf$. Uniqueness gives
$\tau_{gf}=\tau_g\circ g_+\tau_f$. This argument compares the canonical zero-column counits; it requires no identification of entire iterated Spencer filtrations. $\square$

### 4.5. A uniform local resolution bound

The complete finite-resolution proof is given earlier in Holonomic D-modules and duality, Lemma 3.0. It uses the proved regular-local and polynomial bounds in AG-CA, followed by the graded-projective and strict filtered lifting arguments. In particular it neither lifts an arbitrary ungraded projective resolution nor assumes that a projective symbol syzygy is already free.

**Lemma 4.6.** Every coherent left or right $\mathcal D_X$-module on a smooth variety of dimension $d$ locally has a finite free operator resolution of length at most $2d$. Consequently
\[
\mathcal Ext^{q}_{\mathcal D_X}(M,\mathcal D_X)=0\quad(q>2d),
\qquad
\mathbb D_XM\in D^{[-d,d]}_{\mathrm{coh}}(\mathcal D_X).
\tag{4.20}
\]

**Proof.** Apply the earlier lemma's local resolution. Hom into the operator ring has no terms above $2d$, and its finite free opposite-side terms have coherent cohomology by Noetherianity. The shift $[d]$ and density side change yield the displayed interval. Bounded truncation triangles give local perfection and the reversed interval $[-b-d,-a+d]$ for a coherent complex with cohomology in $[a,b]$. The module bound is uniform, independent of the input. $\square$

### 4.6. Proper duality without a projectivity assumption

**Theorem 4.7 (full proper D-module duality).** Let $f:X\to Y$ be any proper morphism of smooth separated finite-type varieties over a characteristic-zero field. For every bounded coherent differential-operator complex there is a natural isomorphism
\[
f_*\mathbb D_XM\ \simeq\ \mathbb D_Yf_*M.
\tag{4.21}
\]
It is compatible with target restriction and proper composition. In particular, nonprojective proper maps are included.

**Proof: the natural comparison.** Side-change (4.17) to obtain the left-module trace $f_*\mathcal O_X[d_X]\to\mathcal O_Y[d_Y]$. The unshifted projection formula (3.6) tensors it with $\mathcal D_Y$ and gives the transfer trace
\[
f_*T_f[d_X]\longrightarrow\mathcal D_Y[d_Y],
\qquad T_f=\mathcal D_{X\to Y}.
\tag{4.22}
\]
This is a bimodule map. The left action is the diagonal differential-operator action in the projection formula; the commuting right action is right multiplication on the original $\mathcal D_Y$ factor. Here is a chain check retaining both actions. In the right Spencer model of the side change of $T_f$, denote the original target-operator factor by $P$ and the transfer factor by $Q$. In étale target coordinates the projection change, on normal monomials $Q=\partial^a$, is
\[
P\otimes\partial^a\ \longmapsto\
 \sum_{b\leq a}(-1)^{|b|}\binom ab\,
       \partial^{a-b}\otimes\partial^bP.
\tag{4.22a}
\]
The output has the Spencer transfer factor first and the original factor last. Coefficients are balanced over $\mathcal O_Y$. Intrinsically this is the transfer-right-linear map sending $P\otimes1$ to $1\otimes P$, with output transfer action
$(m\otimes P)\cdot\xi=(m\cdot\xi)\otimes P-m\otimes\xi P$.
The formula follows by applying this rule repeatedly; the function and derivation relations make it well defined. It is triangular in transfer order with leading coefficient $1$; reversing the minus sign gives its inverse. In the Spencer differential the extra action of $df(\xi)$ on $P$ cancels the extra term from this change. On $Q=1$ and a coordinate vector field this is the two-term calculation just displayed; transfer-right-linearity gives the equality for every $Q$, and the bracket terms agree. Hence this is a chain isomorphism preserving the column filtration. Its intrinsic generator-and-action rule proves agreement on coordinate overlaps, and it commutes with original right multiplication on $P$.

After tensoring a fixed chain representative of $\tau_f$ with $\mathcal D_Y$, the output $\omega_Y\otimes\mathcal D_Y$ has transfer right action
$(\rho\otimes P)\cdot\xi=-\mathcal L_\xi\rho\otimes P-\rho\otimes\xi P$.
This is exactly the side change of the left regular operator module; the other right action is original multiplication on $P$. Side changing back proves (4.22) with its two commuting actions. Flatness of $\mathcal D_Y$ on its coefficient left-$\mathcal O_Y$ side preserves all quasi-isomorphisms. At zero Spencer column and $Q=1$, the trace sends $\phi\otimes P\otimes1$ to $\operatorname{Tr}_f(\phi)\otimes P$, with coefficient $1$.

Local perfection from Lemma 4.6 gives the tensor–Hom evaluation identification of the right module underlying the left-hand side of (4.21):
\[
F(M)=Rf_{\mathrm{sh},*}
 R\mathcal Hom_{\mathcal D_X}(M,T_f)[d_X].
\qquad
G(M)=R\mathcal Hom_{\mathcal D_Y}(f_*M,\mathcal D_Y)[d_Y]
\tag{4.23}
\]
is the right module underlying its right-hand side. Indeed a finite local free resolution gives
$R\mathcal Hom_{\mathcal D_X}(M,\mathcal D_X)\otimes^L_{\mathcal D_X}T_f
 \simeq R\mathcal Hom_{\mathcal D_X}(M,T_f)$ term by term, and these evaluation maps glue. Both $F$ and $G$ subsequently receive the same side-changing line $\omega_Y^{-1}$.

Evaluation, transfer, derived sheaf pushforward, and (4.22) construct a comparison $F(M)\to G(M)$. More explicitly, on a target open use flat transfer resolutions and injective pushforward resolutions to send a derived Hom cochain $M\to T_f$ to the cochain between its transferred and pushed-forward objects, and then compose with (4.22). The induced maps on Hom complexes sheafify; the usual Hom differential signs make this a chain map. Changing resolutions gives the canonical derived evaluation comparison. Right multiplication on $T_f$ commutes with transfer, and (4.22) retains that right action, so this is a right-$\mathcal D_Y$ comparison. Its chain construction is natural for arbitrary $\mathcal D_X$-linear maps, including differentials involving positive-order operators. It is not an objectwise collection of coefficient isomorphisms. The unique trace of Lemma 4.5 also supplies target restriction and composition compatibility for this comparison.

**Induced coefficient objects.** Let $F$ be coherent over $\mathcal O_X$ and set $I(F)=\mathcal D_X\otimes_{\mathcal O_X}F$, a left induced module. Smooth regularity and the proved commutative local bound make $F$ perfect. Put $B=\omega_X\otimes F$. Density transpose identifies the right module underlying $I(F)$ with $B\otimes_{\mathcal O_X}\mathcal D_X$. The induced transfer calculation (3.14) and derived induction–Hom adjunction now give
\[
\begin{aligned}
F(I(F))
 &=Rf_*R\mathcal Hom_{\mathcal O_X}(F,T_f)[d_X],\\
G(I(F))
 &=R\mathcal Hom_{\mathcal O_Y}
       (Rf_*B,\omega_Y\otimes_{\mathcal O_Y}\mathcal D_Y)[d_Y].
\end{aligned}
\tag{4.24}
\]
For the second line, apply side change to the source of the operator Hom in (4.23). The target becomes $\omega_Y\otimes\mathcal D_Y$, whose induced-side right action comes from side-changing its left operator action. Its other, commuting right action is multiplication on the original $\mathcal D_Y$ factor. Induction adjunction cancels the former and retains the latter, exactly the right action displayed in (4.24). Thus neither the density line nor the second operator action has been suppressed.

The ordinary proper-duality comparison, proved in The right adjoint of derived pushforward, Proposition 2.1, together with (4.11), is
\[
Rf_*R\mathcal Hom_{\mathcal O_X}(B,K_X)
 \simeq R\mathcal Hom_{\mathcal O_Y}(Rf_*B,K_Y).
\tag{4.25}
\]
Here its internal-Hom assertion genuinely applies: $B$ is perfect, and the earlier proper coherent-sheaf theorem makes $Rf_*B$ bounded coherent. Smooth regularity on $Y$ then makes $Rf_*B$ perfect. Both internal Hom complexes are therefore quasi-coherent; this is precisely the check required to pass from the quasi-coherent right-adjoint version of that proposition to actual internal Hom. No ordinary coherence assertion for a nonproper restriction has been used.

Tensor (4.25) with the flat left-$\mathcal O_Y$ module $\mathcal D_Y$. On its left, $R\mathcal Hom(B,K_X)=R\mathcal Hom(F,\mathcal O_X)[d_X]$. Perfect coefficient duality and the finite Čech projection calculation (3.14) identify the tensor with the first line of (4.24). On its right, a local finite free resolution of the perfect $Rf_*B$ permits Hom to commute with this flat tensor and gives the second line. All maps commute with right multiplication on $\mathcal D_Y$. Thus (4.25) supplies an isomorphism between the actual right-module expressions in (4.24).

It is the natural comparison already constructed. An induced Hom element is determined by its coefficient generator map $h_0:F\to T_f$. Its operator-linear extension factors canonically as
\[
I(F)\xrightarrow{I(h_0)}I(T_f)
 \xrightarrow{\text{induction counit}}T_f.
\tag{4.26}
\]
After transfer and pushforward, the second arrow is the canonical zero-column inclusion into the Spencer model for $f_*T_f$. Formula (4.22a) at $Q=1$ and the prescribed zero-column trace show that the pairing of $\phi\otimes s$ with $h_0$ is $\phi\otimes h_0(s)$ followed by the ordinary trace tensored with the original operator factor. Resolve $F$ locally by finite free coefficient modules and apply this same factorization to the Hom complex. Cancelling the induced $\mathcal D_X$ factor identifies evaluation with the ordinary coefficient pairing
$R\mathcal Hom(F,\mathcal O_X)\otimes(\omega_X\otimes F)\to\omega_X$.
In the transfer Spencer model this pairing maps to its induced zero column: the canonical map there is the counit used to define $E_0\to f_+K_X$. The subsequent trace restricts on that column to $\operatorname{Tr}_f$ by Lemma 4.5. Therefore the induced comparison is ordinary coefficient evaluation followed by $\operatorname{Tr}_f$, tensored with the target operator factor. This is exactly the counit comparison (4.25). The assertion is termwise for the finite coefficient resolution, with the evaluation differential signs; its maps are canonical, so these local identifications glue. Higher Spencer components supply the fixed homotopies for general operator maps, while this coefficient pairing uses the specified zero-column counit. The comparison is an isomorphism on every $I(F)$.

**Finite-amplitude extension.** Fix an affine target open and a finite affine cover of its inverse image with Čech upper bound $c$ as in Theorem 3.4. Lemma 3.2, side-changed if necessary, supplies successive exact sequences
$0\to K_{i+1}\to I(F_i)\to K_i\to0$, with $K_0=M$ and all $K_i$ coherent. The already natural comparison has a functorial cone $C$ on complexes. Since it is an isomorphism on the induced middle terms, the contravariant triangles give $C(M)\simeq C(K_N)[-N]$.

There is a uniform bound for all these cones. Lemma 4.6 puts $\mathbb D_XK_i$ in $[-d_X,d_X]$. Theorem 3.4 consequently puts $f_*\mathbb D_XK_i$ in $[-2d_X,c+d_X]$. The same theorem puts $f_*K_i$ in $[-d_X,c]$ with coherent cohomology. Applying Lemma 4.6 and its finite truncation triangles on $Y$ bounds $\mathbb D_Yf_*K_i$ by $[-c-d_Y,d_X+d_Y]$. These intervals, and hence an interval $[-b,b]$ containing all cone cohomology, are independent of $i$ and of the input coherent module. This argument uses the already bounded coherent functors; it does not presume quasi-coherence of an operator-Hom cochain complex's terms over $\mathcal O_X$.

For any degree $a$, choose $N>a+b$. Then
$\mathcal H^aC(M)=\mathcal H^{a-N}C(K_N)=0$.
Thus the comparison is an isomorphism for coherent modules. A bounded coherent complex is assembled from its finitely many cohomology modules by truncation triangles, so the natural exact comparison is an isomorphism for it too. Restore $\omega_Y^{-1}$ to obtain (4.21). All steps are local only on target opens; properness is retained throughout. For smooth schemes of different dimensions on their finitely many open and closed components, apply the construction componentwise and take the finite direct sum. This proves the full stated scope. $\square$

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

Full proper D-module coherence and duality for smooth separated characteristic-zero varieties, including nonprojective proper maps, are proved in Theorems 3.4 and 4.7. The latter uses the earlier ordinary duality proofs with the explicit normalization, finite-jet trace comparison and Spencer lift in Lemmas 4.3–4.5. Its uniform local resolution bound is proved in the earlier duality lesson, Lemma 3.0. The proper-coherence theorem used in Theorem 4.2 is proved in Theorem 3.4, using the earlier ordinary coherent-sheaf theorem from *Proper morphisms and coherent direct images*, Theorem 4.1. Holonomicity preservation needed to close the categories in (5.1) is Schnell, Theorem 18.5; the next lesson supplies its proof. The optional reduction by smooth completion uses compactification and resolution of singularities as algebraic-geometric inputs. Finally, the regular-holonomic comparison with constructible sheaves is stated with the Section 6 locators; its correspondence theorem is treated later in the course.

These inputs are distinct from the results proved here: localization, closed adjunction, base change, the projection formula with its shift, full proper duality, both holonomic adjunctions, and every displayed boundary and degree calculation.

## References

- A. Beilinson and V. Drinfeld, [*Quantization of Hitchin's integrable system and Hecke eigensheaves*](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf), Sections 7.2.8–7.2.11: transfer and de Rham direct-image conventions. These sections provide the construction, rather than the base-change or proper-duality proofs.
- J. Bernstein, [*Algebraic theory of D-modules*](https://www.math.columbia.edu/~khovanov/resources/Bernstein-dmod.pdf), lecture notes: base change, the duality theorem for a proper morphism together with the projection formula and the holonomic adjunctions, and the Riemann–Hilbert correspondence (Main Theorem C).
- D. Miličić, [*Lectures on Algebraic Theory of D-Modules*](https://www.math.utah.edu/~milicic/Eprints/dmodules.pdf), Chapter IV, §10: base change for smooth varieties with smooth fiber product.
- P. Etingof, [*Introduction to algebraic D-modules*](https://math.mit.edu/~etingof/dmodwien.pdf), Propositions 3.1, 3.3 and 3.5, pages 11–13, and the appendix on the formalism of six functors: base change, proper adjunction, localization and proper-duality statements.
- C. Schnell, [*Algebraic D-modules*](https://www.math.stonybrook.edu/~cschnell/pdf/notes/d-modules.pdf), Lecture 18, Lemma 18.2 and Theorems 18.1 and 18.5: induced resolutions, proper coherence and holonomicity preservation.
- B. Bhatt, M. Blickle, G. Lyubeznik, A. K. Singh and W. Zhang, [*Applications of perverse sheaves in commutative algebra*](https://arxiv.org/abs/2308.03155), Section 2, Theorem 2.1, part (1): the regular-holonomic comparison with sheaf functors.

- The Stacks Project, [Extending quasi-coherent sheaves, Tags 01PE–01PG](https://stacks.math.columbia.edu/tag/01PD): finite-type subsheaf extension and coherent approximation, also proved in Lemma 3.2.
