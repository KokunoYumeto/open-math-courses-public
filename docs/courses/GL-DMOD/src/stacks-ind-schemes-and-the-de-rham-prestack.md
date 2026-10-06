# D-modules on stacks, ind-schemes and the de Rham prestack

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A quotient stack remembers the symmetries of its points. For a connected group acting on a point, strong equivariance leaves only vector spaces in the abelian category. Nevertheless the derived category on the quotient remembers the cohomology of the group. This difference is essential on the automorphic side of geometric Langlands.

We work over an algebraically closed field $k$ of characteristic zero. Categories in this lesson are presentable $k$-linear stable infinity-categories, or equivalently their DG models; $\operatorname{Vect}$ means complexes of vector spaces. A limit includes compatible objects, maps, and all their homotopies. Taking a limit of triangulated homotopy categories would discard part of this information.

On smooth schemes we retain left D-modules and the convention of Inverse images:
\[
f^!M=Lf^*M[r]\quad\text{if }f\text{ is smooth of relative dimension }r.
                                                               \tag{0.1}
\]
The normalized pullback $f^\natural=f^![-r]$ is exact on the usual module hearts. It is also useful to distinguish the smooth de Rham pullback
$f_{\rm dR}^*=f^![-2r]$: for a schematic quasi-compact smooth map this is the left adjoint of $f_{\rm dR,*}$. Thus $f^\natural$ and $f_{\rm dR}^*$ are different normalizations.

We use Equivariant and twisted D-modules, smooth descent for algebraic stacks, and the Spencer and Kashiwara constructions from earlier lessons. The categorical prerequisites are homotopy limits, DG modules, Ind-completion, and derived tensor products. The general theories of prestacks, $\operatorname{QCoh}$, $\operatorname{IndCoh}$, and formal completions are inputs from derived algebraic geometry.

## 1. Descent includes the higher maps

Let $\mathcal Y$ be a smooth algebraic stack with affine diagonal, initially quasi-compact. Choose a smooth surjective atlas $q:U\to\mathcal Y$ with $U$ affine. Its nerve is
\[
U_p=\underbrace{U\times_{\mathcal Y}\cdots\times_{\mathcal Y}U}_{p+1}.
\]
The affine-diagonal assumption makes these schemes affine. On components where $q$ has relative dimension $r$, the augmentation $q_p:U_p\to\mathcal Y$ has relative dimension $r_p=(p+1)r$; variable dimensions are handled componentwise.

Define
\[
\mathrm{Dmod}(\mathcal Y)=\operatorname{Tot}\bigl(\mathrm{Dmod}(U_\bullet),\,!\bigr).
                                                               \tag{1.1}
\]
An object is a complex $M_p$ on every level with equivalences between its !-pullbacks along the nerve maps, satisfying homotopy-coherent compatibility. In the heart, the normalized objects are $M_p[-r_p]$. Their face identifications use the exact pullbacks $f^\natural$, since a face map has relative dimension $r_p-r_{p-1}$.

**Theorem 1.1 (the descent heart).** The category (1.1) has a nondegenerate t-structure characterized by
\[
M\in\mathrm{Dmod}(\mathcal Y)^{\leq0}
\ \Longleftrightarrow\ q^!M[-r]\in\mathrm{Dmod}(U)^{\leq0},
                                                               \tag{1.2}
\]
and the corresponding condition for $\geq0$. Its heart is the abelian category of D-modules obtained by normalized smooth descent.

**Proof.** Work first with the face maps of the nerve; this is its semisimplicial, or fat, totalization. It computes the same descent category: units and degeneracies supply identity identifications, while the face compatibilities retain their coherent compositions. Every face pullback, after subtracting the difference of the $r_p$, is t-exact. Consequently the prescriptions
\[
(M^{\leq0})_p=\tau^{\leq0}(M_p[-r_p])[r_p],\qquad
(M^{\geq1})_p=\tau^{\geq1}(M_p[-r_p])[r_p]
\]
commute with the face identifications and their homotopies. They therefore define descent objects and a triangle
$M^{\leq0}\to M\to M^{\geq1}$.

For normalized level objects $A\in D^{\leq0}$ and $B\in D^{\geq1}$, the mapping space is contractible: its homotopy groups are
$\operatorname{Hom}(A[i],B)$ for $i\geq0$, and all vanish. Mapping spaces in the descent category are limits of the level mapping spaces. The limit is contractible too. This proves orthogonality; the shift conditions follow from the level t-structures.

The atlas pullback is conservative, since every level is obtained from level zero by a projection. Hence the t-structure is nondegenerate and (1.2) suffices to test it. An object in both halves has ordinary D-modules as all its normalized levels. Mapping spaces between such modules are discrete, so the higher descent data reduce to the ordinary isomorphism and cocycle. Conversely these ordinary data define a heart object. This identifies the heart. $\square$

For $\mathcal Y=[X/G]$ the heart is the category of strongly $G$-equivariant D-modules on $X$ calculated in the preceding lesson. The theorem does **not** identify (1.1) with the ordinary derived category of that heart. Section 5 gives an explicit obstruction.

## 2. Changing atlases and hypercovers

We give the descent argument behind Beilinson–Drinfeld, §§7.3.4 and 7.5.2. An admissible smooth hypercover has levels that are disjoint unions of quasi-compact separated smooth algebraic spaces, with the usual smooth covering maps to matching objects. Affine refinements may be chosen throughout.

The basic calculation is an augmented Čech resolution. For a faithfully flat affine cover $\pi:V\to S$ and a quasi-coherent module $E$, its terms are the iterated pullbacks to $V^{p+1}_S$, pushed to $S$. After pulling back to $V$, insert the distinguished first vertex. If $s$ is this extra degeneracy and $d$ the alternating face differential, the identities between faces give
\[
ds+sd=\operatorname{id}-\text{augmentation}.
                                                               \tag{2.1}
\]
Thus the augmented complex contracts after this faithfully flat pullback and is exact before it. For complexes, the same calculation respects the internal differential, with the total-complex signs.

For D-modules this calculation can be made in the de Rham DG-algebra model: an $\Omega_S^\bullet$-complex is localized at maps inducing isomorphisms on its associated D-module cohomology. The Spencer adjunction compares this model with D-module complexes. Affine pushforward and flat pullback make the augmented Čech calculation valid for that cohomology too; the dimension shifts used in (1.2) supply the normalization. Consequently restriction to the cover and the augmented Čech reconstruction have unit and counit inducing isomorphisms on D-module cohomology. This is effective derived descent, rather than just descent of degree-zero modules.

In an unbounded calculation, totalization means a homotopy limit, with products where necessary. One may verify the preceding assertion on normalized bounded-below truncations and then pass to their limit. On an affine chart, complexes of modules satisfy
$M\simeq\lim_n\tau^{\geq-n}M$. Exact normalized smooth pullbacks commute with these truncations, and the contraction (2.1) is compatible with them. This gives the unbounded calculation chartwise. It does not justify replacing an infinite product by an infinite direct sum.

**Theorem 2.1 (independence of the presentation).** Admissible smooth hypercovers of a smooth stack define canonically equivalent DG descent categories. These equivalences identify the normalized t-structures and hearts.

**Proof.** Begin with two atlases $U$ and $U'$. Refine $U\times_{\mathcal Y}U'$ by affine smooth charts. The two Čech directions give a bisimplicial refinement $V_{\bullet,\bullet}$. In each column the augmented Čech reconstruction above is inverse to restriction; the same is true in each row. Thus
\[
\operatorname{Tot}\mathrm{Dmod}(U_\bullet)
\ \simeq\
\operatorname{Tot}_{m,n}\mathrm{Dmod}(V_{m,n})
\ \simeq\
\operatorname{Tot}\mathrm{Dmod}(U'_\bullet).
                                                               \tag{2.2}
\]
The equivalences are those of categories and mapping complexes, since both the unit and counit were checked, not merely the cohomology of objects.

For hypercovers, perform the same refinement recursively on matching objects. At stage $n$, the previously chosen levels specify the matching data; their pullback against the covering at level $n$ admits an affine smooth cover. The augmented reconstruction in each direction gives (2.2) again. For bounded-below normalized complexes this is the usual hypercover resolution: filtering by the nerve degree and using exact augmented covering resolutions proves that its augmentation is a quasi-isomorphism. Each total cohomological degree involves only finitely many terms. For unbounded complexes use the compatible truncations and chartwise homotopy limits described above.

Finally take three presentations and a common trisimplicial refinement. An iterated homotopy limit equals the limit over the product indexing category: both satisfy the universal property of compatible cones. Hence the composite comparison from the first presentation through the second is the comparison through the third refinement. Changing an auxiliary refinement is handled by a further common refinement and the same augmentation. Inserting vertices gives the compatible contraction homotopies; repeating it supplies their higher compatibilities. This proves independence, including coherence of the comparisons. The constructions preserve normalized cohomology, so they preserve the t-structures and identify the ordinary descent hearts. $\square$

For the affine-diagonal quasi-compact stack of Section 1, the inverse can also be represented by the augmented $\Omega$-Čech complex on the stack itself: the levels map affinely to it, so the same cohomology check applies. Thus the definition by localized global $\Omega$-complexes agrees with (1.1). This completes the comparison needed for the version of Theorem 1.1 in Beilinson–Drinfeld, §7.3.4.

### Pushforward has finiteness conditions

For a schematic quasi-compact map $f:\mathcal Y\to\mathcal Z$, define $f_{\rm dR,*}$ on a chart $S\to\mathcal Z$ by the scheme pushforward on $\mathcal Y\times_{\mathcal Z}S\to S$. !-base change, proved in Adjunctions, base change and the projection formula, makes these chart objects compatible. The construction preserves colimits, composes correctly, and satisfies the projection formula. For proper $f$, $f_{\rm dR,*}\dashv f^!$; for an open immersion $j$, $j^!\dashv j_*$; for smooth schematic quasi-compact $f$, $f_{\rm dR}^*\dashv f_{\rm dR,*}$. There is no universal adjunction $f_{\rm dR,*}\dashv f^!$ for arbitrary maps.

The original $\Omega$-complex construction for a quasi-compact morphism of smooth stacks defines pushforward first on bounded-below normalized complexes; finite cohomological-dimension hypotheses permit an unbounded extension (Beilinson–Drinfeld, §§7.3.6–7.3.11 and 7.5.6). A nonrepresentable stack pushforward can fail to preserve colimits even on a quasi-compact stack. For example, de Rham global sections on $B\mathbb G_m$ fail that test in Section 5. For a non-quasi-compact source, restrictions to small opens define its category; a global direct image requires its own construction and finiteness checks.

## 3. Closed filtrations and infinitesimal neighborhoods

Let $\mathcal X=\operatorname{colim}_i X_i$ be a strict ind-scheme, presented by finite-type schemes and closed embeddings $i_{ij}:X_i\hookrightarrow X_j$. In the modern presentable theory,
\[
\mathrm{Dmod}(\mathcal X)
\simeq\operatorname{colim}_{i,\,i_{ij,\rm dR,*}}\mathrm{Dmod}(X_i)
\simeq\lim_{i,\,i_{ij}^!}\mathrm{Dmod}(X_i).
                                                               \tag{3.1}
\]
The second expression follows from the prestack definition in Section 4; the first is the general limit/colimit correspondence for a diagram of adjoint continuous functors. Closed pushforwards are fully faithful by Kashiwara's equivalence. These facts identify (3.1) with the category generated under colimits by the finite stages, and show independence of a cofinal closed presentation. The categorical limit/colimit correspondence is an input, stated in Drinfeld–Gaitsgory, *Compact generation*, Proposition 1.7.5.

An arbitrary object need not come from a single finite stage. If the stages are compactly generated and the closed pushforwards preserve compactness, compact objects do come from finite stages, after idempotent completion: a finite cone or retract of finitely many stage generators can be taken in one later stage. General objects are colimits of such objects. Finite-type D-module categories and their closed pushforwards satisfy these conditions.

The older formally smooth ind-scheme theory in Beilinson–Drinfeld, §7.11, requires care when compared with (3.1). Its derived category in §7.11.14 uses complexes with quasi-compact support; the footnote there discusses extending it and warns against the naive category of all complexes. We use the presentable completion, while retaining its finite-support calculations.

There are also two underlying module notions. On an affine formal ind-scheme
$\operatorname{colim}\operatorname{Spec}(A/I_i)$, an $\mathcal O^p$-module is described by compatible pullbacks and complete modules. An $\mathcal O^!$-module is discrete: each element is annihilated by some open ideal, and its finite-stage pieces are connected using $i^!=\operatorname{Hom}_A(A/I_i,-)$ in the abelian description. They cannot be exchanged.

For example, on $\operatorname{Spf}k[[t]]$, the complete module $k[[t]]$ is not discrete, whereas $k[t^{-1}]/k$ is discrete with its evident $k[[t]]$-action. An element represented by $t^{-m}$ is killed by $t^m$. This elementary difference explains why a completed ring of operators does not authorize using arbitrary complete modules as D-modules.

On a reasonable formally smooth ind-scheme of ind-finite type, Beilinson–Drinfeld, Propositions 7.11.8 and §7.11.11, constructs a topological differential algebra with order symbols $\operatorname{Sym}\Theta_{\mathcal X}$, acting on discrete right modules. Its crystal interpretation is §7.11.6. We state that construction, without extending the finite-dimensional formula $\omega_X\otimes M$ to a nonexistent top exterior power in infinite dimension. The left convention is implemented on finite smooth charts; an infinite-dimensional comparison needs its specified lattice and determinant data.

### A discrete Grassmannian example

For a field $k$, every invertible Laurent series is uniquely $t^n u(t)$ with $u(t)\in k[[t]]^\times$. Hence the reduced affine Grassmannian of $\mathbb G_m$ is the discrete ind-scheme $\mathbb Z$, with $n$ corresponding to the lattice $t^n k[[t]]$. This reduced-ind-scheme identification, including families, is the torus Grassmannian result recalled in Hilburn–Raskin, §2; it is not inferred from field-valued points alone.

Nilpotent directions of the full Grassmannian are invisible to its de Rham prestack. Thus its D-module category is that of $\mathbb Z$:
\[
\mathrm{Dmod}(\mathbb Z)=\prod_{n\in\mathbb Z}\operatorname{Vect}.
                                                               \tag{3.2}
\]
This means all families $(V_n)$, rather than only finite-support families. A compact object has finite support and perfect, finite-dimensional bounded complexes at its nonzero entries. Indeed each coordinate tests perfectness; an infinite-support object is the filtered colimit of its finite-support subfamilies, and its identity cannot factor through one of them. Conversely finite support and coordinatewise perfectness make its mapping functor commute with colimits.

There is an explicit character transform
\[
(V_n)_{n\in\mathbb Z}\longmapsto
\bigoplus_{n\in\mathbb Z}V_n\otimes\chi^n
\quad\text{in }\operatorname{QCoh}(B\mathbb G_m).
                                                               \tag{3.3}
\]
Rational $\mathbb G_m$-representations decompose into integer weight spaces, and weight extraction is exact. This gives the inverse and proves the DG equivalence in (3.3). Convolution of families has weight-$m$ term $\bigoplus_{a+b=m}V_a\otimes W_b$, which becomes tensor product of representations. This character Fourier transform identifies $\mathrm{Dmod}(\mathbb Z)$ with $\operatorname{QCoh}(B\mathbb G_m)$, a category different from $\mathrm{Dmod}(B\mathbb G_m)$.

## 4. The de Rham prestack and its two realizations

A prestack is a functor from derived affine schemes to spaces. For a connective commutative DG algebra $R$ put
\[
\mathcal Y_{\rm dR}(\operatorname{Spec}R)
=\mathcal Y\bigl(\operatorname{Spec}(H^0(R)_{\rm red})\bigr).
                                                               \tag{4.1}
\]
One first takes the underlying classical ring, then its reduced quotient. The canonical map $\mathcal Y\to\mathcal Y_{\rm dR}$ forgets infinitesimal information.

For $\mathbb A^1$, its value on $k[\eta]/(\eta^2)$ records $a$, whereas the ordinary affine line records $a+b\eta$. Two such lifts with the same $a$ are infinitesimally close. For a smooth scheme $X$, the terms of the nerve of $X\to X_{\rm dR}$ are the formal completions of $X^{p+1}$ along the small diagonal. Descent there is infinitesimal parallel transport; its heart is the Taylor crystal calculated in Kashiwara's equivalence and D-modules on singular spaces.

**Theorem 4.1 (foundational comparison, stated).** For a smooth finite-type scheme $X$, the DG category of left D-module complexes is equivalent to
$\operatorname{QCoh}(X_{\rm dR})$. For a prestack $\mathcal Y$ locally almost of finite type, right crystals are
$\operatorname{IndCoh}(\mathcal Y_{\rm dR})$, and the natural functor
\[
\Upsilon_{\mathcal Y_{\rm dR}}:
\operatorname{QCoh}(\mathcal Y_{\rm dR})
\ \xrightarrow{\ \sim\ }\operatorname{IndCoh}(\mathcal Y_{\rm dR})
                                                               \tag{4.2}
\]
is an equivalence. These are Gaitsgory–Rozenblyum, *Crystals and D-modules*, §5.5 and Proposition 2.4.4; right crystals are defined in §2.3.

For singular schemes the right realization supplies the canonical support-based D-module theory, rather than modules over the naive ring of differential operators on a singular scheme. But it would be incorrect to say that $\operatorname{QCoh}(X_{\rm dR})$ stops working merely because $X$ is singular: (4.2) still applies. The forgetful realizations on $X$ itself differ, and $\Upsilon_X:\operatorname{QCoh}(X)\to\operatorname{IndCoh}(X)$ need not be an equivalence.

There is a dimension normalization in applying this theorem to our !-descent category. Write $\Phi_X$ for the usual left-module/crystal equivalence, which sends a connection $M$ to its Taylor crystal. On a smooth $d$-dimensional scheme use
\[
E_X(M)=\Phi_X(M)[-d].
                                                               \tag{4.3}
\]
Then for a smooth $f:X\to Y$ of relative dimension $r$,
$E_X(f^!M)=(f_{\rm dR})^*E_Y(M)$, where the pullback on the right is **QCoh pullback on de Rham prestacks**. Indeed the shifts are $r-d_X=-d_Y$. The parenthesized $(f_{\rm dR})^*$ is separate from the smooth D-module functor $f_{\rm dR}^*=f^![-2r]$ in (0.1). In the right-crystal realization it is $(f_{\rm dR})^!$ and is simply called $f^!$.

The reason for (4.3) is that $\Upsilon_X$ tensors with the dualizing **complex**
$\omega_X[d]$, while ordinary side-changing tensors with the canonical **line** $\omega_X$. Forgetting that difference would shift the heart incorrectly. With (4.3), the tensor unit is the descent object $\omega_{\mathcal Y}$ characterized by $q^!\omega_{\mathcal Y}=\omega_U[d_U]$ in right-module notation, or $\mathcal O_U[d_U]$ on the left. On a smooth stack of dimension $d_{\mathcal Y}$ its normalized heart object is $\omega_{\mathcal Y}[-d_{\mathcal Y}]$.

For arbitrary locally almost finite-type prestacks the !-definition may also be written
\[
\mathrm{Dmod}(\mathcal Y)=
\lim_{(S\to\mathcal Y)}\mathrm{Dmod}(S),
                                                               \tag{4.4}
\]
with finite-type affine charts and !-transitions. Gaitsgory–Rozenblyum, Corollary 2.3.9, gives this comparison; for algebraic stacks smooth charts suffice (Drinfeld–Gaitsgory, *Compact generation*, §2.1). It agrees with Sections 1–2. De Rham pushforward is the corresponding pushforward of right crystals when defined, with the continuity conditions already discussed. The de Rham prestack description does not eliminate those conditions.

Gaitsgory's *Outline for GL(2)*, §3.1, uses left crystals $\operatorname{QCoh}(\mathcal Y_{\rm dR})$ and calls their pullback $f^\dagger$. Its formula uses the classical reduced derived affine, exactly as in (4.1). The comparison (4.3), rather than an unexplained equality of pullback symbols, translates that convention into ours.

### Infinite-dimensional operators require an actual category

Hilburn–Raskin's *Tate's thesis in the de Rham setting* develops $\operatorname{IndCoh}^*$ on its infinite-dimensional spectral spaces in §4, using specified coherent subcategories, colimits, and weak Grassmannian invariants. A pushforward there need not preserve bounded-below complexes (§4.2). The construction is not obtained by declaring all complexes over an arbitrary infinite polynomial ring coherent.

Its spectral space $\mathcal Y$ parametrizes a rank-one connection on the punctured formal disc with a horizontal section. In a trivialization the data are $(g,\alpha)$ satisfying $dg=g\alpha$, modulo the gauge action $(g,\alpha)\mapsto(fg,\alpha+d\log f)$. In $\mathcal Y_{\log}$ a lattice extending the line over the disc is retained; $\mathcal Z$ imposes that the section extend over it. Superscript $\leq n$ bounds the pole order of the connection form.

In §5.1 the compact object
$\mathcal F_n=\operatorname{Av}_!^{\mathrm{Gr}_{\mathbb G_m}^{\leq n},w}
(i_{n,*}\mathcal O_{\mathcal Z^{\leq n}})$
is constructed in $\operatorname{IndCoh}^*(\mathcal Y^{\leq n})$. Here $i_n$ includes the locus where the section extends, and averaging forgets the chosen lattice with its prescribed weak equivariance. The result is an action of $W_n^{\rm op}$, where $W_n$ is the differential-operator algebra on
$\operatorname{Spec}\operatorname{Sym}(t^{-n}k[[t]]\,dt/k[[t]]\,dt)\simeq\mathbb A^n$.
The function and vector-field operators obey
\[
[\xi_f,\varphi_\alpha]=-\operatorname{Res}(f\alpha)\operatorname{id}.
                                                               \tag{4.5}
\]
For bases $f_j=t^j$, $\alpha_i=t^{-i-1}dt$ ($0\leq i,j<n$), the residue is $\delta_{ij}$. Ordinary Weyl operators have $[\partial_j,x_i]=\delta_{ij}$; reversing multiplication gives the minus sign in (4.5). This proves the sign translation. The geometric construction and its later full-faithfulness theorem (§7.1) are stated inputs here.

## 5. The full category on a point quotient

Put $\mathcal B=B\mathbb G_m$ and $p:\mathrm{pt}\to\mathcal B$. Its relative dimension is one. Let $C$ be the constant descent object normalized by $p^!C=k$; it is the !-tensor unit $\omega_{\mathcal B}$. The constant object in the normalized left heart is $H=C[1]$. A different convention for the constant sheaf may shift $C$; all the self-Ext and compactness conclusions below are shift-invariant.

The functor $p^!$ is conservative by descent and preserves colimits. Its left adjoint $p_!$ exists on the whole category in this example. One can construct it on the atlas by the groupoid bar construction, using compactly supported de Rham pushforward in the nerve direction: the augmentation and extra-degeneracy identities give
$\operatorname{RHom}(p_!V,M)=\operatorname{RHom}(V,p^!M)$.
This special adjoint is also supplied by Drinfeld–Gaitsgory, *Finiteness questions*, §7.2.2. It is not an assertion that every stack map has such an adjoint.

Set $K=p_!k$. Then
\[
\operatorname{RHom}(K,M)=p^!M.
                                                               \tag{5.1}
\]
Thus $K$ is compact, and is a generator: the right side preserves colimits and detects the zero object. Base change on the groupoid identifies its endomorphism algebra, up to the opposite for left modules, with compact de Rham chains of $\mathbb G_m$, with multiplication induced by group multiplication. Equivalently these chains are the dual of the de Rham cochains of $\mathbb G_m$; the compact pushforward of its dualizing object gives the same complex by duality.

The cochains have $H^*=k\oplus k\,d t/t$ in degrees zero and one. The chains therefore have $H^*=k\oplus k\epsilon$ in degrees zero and minus one. The unit is in degree zero. This calculation also proves formality as an associative DG algebra. In a strictly unital minimal $A_\infty$ model, any operation $m_n$ on $n$ nonunit inputs has output degree
$-n+(2-n)=2-2n$; for $n\geq2$ this degree is absent. All these operations vanish. Operations with a unit vanish by strict unitality, except for multiplication by the unit. Hence the algebra is
\[
A=\Lambda(\epsilon)=k[\epsilon]/(\epsilon^2),\quad
|\epsilon|=-1,\quad d\epsilon=0.
                                                               \tag{5.2}
\]
The use of a minimal strictly unital model is the standard homological-transfer theorem for DG algebras; it is a categorical input. Here the degree argument checks every possible higher product. Since (5.2) is graded commutative, its opposite causes no change.

**Theorem 5.1.** There is an equivalence
\[
\mathrm{Dmod}(B\mathbb G_m)\simeq A\text{-}\mathrm{mod}
\simeq\operatorname{QCoh}
(\mathrm{pt}\mathbin{\times^{\mathbf R}_{\mathbb A^1}}\mathrm{pt}).
                                                               \tag{5.3}
\]
The object $K$ goes to the free module $A$, and $C$ goes to its augmentation module $k$. The normalized heart constant $H$ goes to $k[1]$.

**Proof.** With $A=\operatorname{End}(K)^{\rm op}$, let
$F=\operatorname{RHom}(K,-)$ and $L(V)=K\otimes_A^{\mathbf L}V$.
They are adjoint, $F$ preserves colimits by (5.1), and $F(K)=A$. The unit $V\to FL(V)$ is an equivalence for $V=A$, for its shifts and sums, and then for all DG modules: the usual free bar resolution expresses every module as the realization of a diagram of free modules, and both functors preserve that realization. Apply $F$ to the counit $LF(M)\to M$. The unit and triangle identities make it an equivalence after $F$, so its cone is zero because $F$ is conservative. This proves the first equivalence.

The action on $F(C)=p^!C=k$ is the augmentation: constant descent makes transport trivial, and the degree-minus-one chain generator acts by zero. Finally resolve $k$ over $k[x]$ by the Koszul DG algebra $k[x,\epsilon]$ with $|\epsilon|=-1$ and $d\epsilon=x$. Tensoring with $k$ at $x=0$ leaves exactly (5.2). Thus the derived intersection is $\operatorname{Spec}A$, whose quasi-coherent category is $A$-modules. $\square$

This proves the category equivalence mentioned in Arinkin–Gaitsgory, §11.2, and separates it from the calculation of the endomorphisms of only one object. The equivalence is not claimed t-exact for the usual DG-module t-structure.

### The constant object is not a compact generator

A semifree resolution of the augmentation module is
\[
P=\bigoplus_{n\geq0}Ae_n,\quad |e_n|=-2n,\qquad
de_0=0,\quad de_n=\epsilon e_{n-1}\ (n\geq1).
                                                               \tag{5.4}
\]
The graded Leibniz rule gives $d(\epsilon e_n)=0$. Every negative-degree cycle $\epsilon e_n$ is the boundary of $e_{n+1}$, and the remaining degree-zero class is $e_0$. Thus $P\to k$ is a resolution.

Applying $\operatorname{Hom}_A(-,k)$ gives zero differential and one class in each even nonnegative degree. The degree-two chain map $e_n\mapsto e_{n-1}$ for $n>0$, and $e_0\mapsto0$, lifts the first class. Its $m$th power followed by augmentation is nonzero on $e_m$. Consequently its Yoneda powers give
\[
\operatorname{Ext}^*_A(k,k)=k[c],\quad |c|=2.
                                                               \tag{5.5}
\]
This is $H^*_{\rm dR}(B\mathbb G_m)$: on the atlas nerve, $d t/t$ is primitive under group multiplication, and its reduced cobar tensor of length $m$ has total degree $2m$. The reduced differential is zero. Shuffle products give $\binom{a+b}{a}$ times the length-$a+b$ class; factorial rescaling identifies the polynomial products in characteristic zero. Over $\mathbb C$, degreewise de Rham comparison identifies this with topological $H^*(B\mathbb G_m,\mathbb C)$.

A compact DG $A$-module is a retract of a finite cell module. Since $A$ is bounded and finite dimensional, any such module has bounded self-Hom cohomology. Equation (5.5) is unbounded, so $k$, and hence every shift of $C$, is not compact. The free module $A$, corresponding to the compactly supported pushforward $K$, is compact.

There is a direct continuity test as well. Form the telescope
$C\xrightarrow{c}C[2]\xrightarrow{c}C[4]\to\cdots$.
After $p^!$ the maps are zero in $\operatorname{Vect}$, so its colimit is zero; conservativity proves that it was zero on $\mathcal B$. Applying $\operatorname{RHom}(C,-)$ gives successive multiplication by $c$ on shifted copies of $k[c]$. Their colimit is nonzero: the degree-zero class represented by $c^m$ at stage $m$ survives at every later stage. Thus this mapping functor, or the correspondingly normalized de Rham global-sections functor, fails to commute with colimits.

Meanwhile the normalized heart is $\operatorname{Vect}^{\heart}$: a strong rational $\mathbb G_m$-representation has zero infinitesimal action, hence only weight zero. Its ordinary derived category has no positive self-Ext for its constant one-dimensional object. Formula (5.5) proves why it cannot be (5.3).

## 6. The moduli of bundles and its dual

Let $X$ be a smooth complete connected curve and $G$ a connected reductive group. The stack $\mathrm{Bun}_G(X)$ is smooth, locally of finite type, and has affine diagonal. Its usual dimension is $(g(X)-1)\dim G$. For groups such as $\mathbb G_m$, its components have unbounded degree, so it is not quasi-compact.

For any locally finite-type stack with affine diagonal, the poset of quasi-compact opens is directed by finite unions. Intersections are quasi-compact. We have
\[
\mathrm{Dmod}(\mathcal Y)
\simeq\lim_{U\subset\mathcal Y\ {\rm qc\ open}}\mathrm{Dmod}(U),
                                                               \tag{6.1}
\]
with restriction transitions.

**Proof.** Restriction clearly defines a functor. Conversely suppose compatible objects on all $U$ are given. A quasi-compact smooth chart $S\to\mathcal Y$ has quasi-compact image. Cover that image by open finite-type neighborhoods; finitely many suffice, and their union is a quasi-compact open $U$. Pull its object to $S$. If $U'$ is another choice, $U\cup U'$ contains both and the compatibility identifies the two pullbacks.

Apply this construction to a smooth atlas and every level of its nerve, refining non-quasi-compact levels by quasi-compact charts. All face comparisons agree because they are obtained from one larger finite union whenever finitely many charts are involved. The original coherent compatibility supplies all higher comparisons. Theorem 2.1 glues these data to an object of $\mathrm{Dmod}(\mathcal Y)$ whose restriction is the given family. The same argument for maps, or the mapping-complex formula for limits, proves full faithfulness:
\[
\operatorname{RHom}_{\mathcal Y}(M,N)
\simeq\lim_U\operatorname{RHom}_U(M|_U,N|_U).
                                                               \tag{6.2}
\]
Thus the constructions are inverse. $\square$

A cofinal exhaustion gives the same limit. Compact generation does not follow just from (6.1).

**Theorem 6.1 (Drinfeld–Gaitsgory, stated).** For $G$ and $X$ as above, $\mathrm{Dmod}(\mathrm{Bun}_G)$ is compactly generated. More precisely, $\mathrm{Bun}_G$ is truncatable: it has a cofinal supply of quasi-compact co-truncative opens. For such an open $j:U\hookrightarrow\mathrm{Bun}_G$, $j_!$ is defined on all D-modules on $U$. These statements are *Compact generation*, Theorems 0.1.2 and 0.2.5, with the definition in §4.1. The analogous twisted assertion is §0.4.1. The proofs require the Harder–Narasimhan stratification and contraction arguments, which we do not reproduce.

The usual heart/coherence condition is local on smooth charts; compactness is a global mapping-functor condition. They differ even for the quasi-compact stack $B\mathbb G_m$, as Section 5 shows.

The half-twist from the preceding lesson is retained in the 2024 automorphic category. Put
\[
\mathcal C=\mathrm{Dmod}_{1/2}(\mathrm{Bun}_G),\qquad
\mathcal C_{\rm co}=
\operatorname{colim}_{U,\,(j_{12})_*}\mathrm{Dmod}_{1/2}(U).
                                                               \tag{6.3}
\]
This is the definition in *Proof of geometric Langlands IV*, §2.1. Its canonical duality is
\[
\mathcal C^\vee\simeq\mathcal C_{\rm co},\qquad
(j^!)^\vee=j_{{\rm co},*}.
                                                               \tag{6.4}
\]
The half-twist is self-opposite under the corresponding Verdier convention, since reversing the square-root character of $\mu_2$ leaves the same character.

Here is the reason for the colimit and its arrows. The category on every quasi-compact open is dualizable and Verdier self-dual. Duality changes the restriction diagram into the opposite diagram; restriction is dual to $j_*$. For $\mathrm{Bun}_G$, co-truncative opens are cofinal by Theorem 6.1. The compactness conditions there allow categorical duality to turn (6.1) into this colimit. This is the argument of Drinfeld–Gaitsgory, *Compact generation*, Corollary 4.3.2; (6.4) in the twisted conventions is explicitly recorded in geometric Langlands IV, §2.1.

There is also a naive comparison
$\mathrm{Ps\!-\!Id}^{\rm nv}:\mathcal C_{\rm co}\to\mathcal C$
characterized by
$\mathrm{Ps\!-\!Id}^{\rm nv}\circ j_{{\rm co},*}=j_*$.
It is a specified functor, not an automatic equivalence. If $\mathcal Y$ is quasi-compact, its final open supplies both categories, so this comparison is an equivalence. In the non-quasi-compact situation one must preserve which category and which comparison are intended. A different, nontrivial duality functor can give an equivalence; that would not make the naive comparison automatically invertible.

The square-root gerbe, determinant normalization and choice-dependent untwisting of $\mathcal C$ are those of Gaitsgory–Raskin, *Proof of geometric Langlands I*, §1.1, calculated in Equivariant and twisted D-modules. The co-version and !-conventions are additional structure needed to interpret the global adjunction in Beilinson–Bernstein localization.

## 7. Exercises and solutions

**Exercise 17.1 (easy).** Identify the abelian D-module category on $BG$ for connected affine $G$.

**Solution.** The normalized descent heart is strong rational representations on a point. Strongness makes the differentiated action zero. For any vector, its orbit map lies in a finite-dimensional rational subrepresentation and has zero differential. Every regular function on a connected smooth group with zero differential is constant in characteristic zero: this can be checked in its function field using a separating transcendence basis. Thus the orbit map is constant and its value is the original vector. All representations are trivial; arbitrary vector spaces with that trivial action are permitted. Morphisms are all linear maps. The category is $\operatorname{Vect}^{\heart}$, not a claim about its derived descent category.

**Exercise 17.2 (easy).** For a smooth map of smooth stacks of relative dimension $d$, prove the normalized t-exactness assertion for !-pullback.

**Solution.** Test on a smooth chart $S\to\mathcal Y$ of the source, of relative dimension $r$. Its composite with the target has relative dimension $r+d$. If $M$ is in the target heart, $(f\circ q)^!M[-r-d]$ is an ordinary module by (1.2). Since $q^!f^!=(f\circ q)^!$, the normalized pullback of $f^!M[-d]$ to $S$ is exactly this module. The same argument with truncation halves proves that $f^![-d]$ is t-exact. On schemes this is $Lf^*$, using flatness; it agrees with (0.1). The functor $f^![-2d]$ has the smooth de Rham adjunction normalization instead.

**Exercise 17.3 (medium).** Compute the graded self-Ext algebra of the constant object on $B\mathbb G_m$.

**Solution.** Under (5.3) it is the augmentation module, up to a common shift. The resolution (5.4) has exactly the displayed cycles and boundaries. Its Hom into $k$ has a basis in degrees $0,2,4,\ldots$. The degree-two shift map on the generators of the resolution has nonzero $m$th power on $e_m$ after augmentation. Hence both the groups and the products are $k[c]$, $|c|=2$, rather than just a list of even-dimensional groups. The primitive class $dt/t$ on the atlas nerve and its factorial-normalized cobar powers identify $c$ with the de Rham classifying-space generator. Over $\mathbb C$ this is the topological cohomology generator under comparison.

**Exercise 17.4 (medium).** Explain why the constant object is not compact, and identify a compact generator.

**Solution.** The augmentation $k$ has unbounded self-Ext by Exercise 17.3. A compact $A$-module is a retract of a finite cell module; its self-Hom is bounded because $A$ has just two finite-dimensional graded pieces. Thus $k$ is not compact. The same holds for the shift corresponding to the heart constant. The free module $A$ is compact, since $\operatorname{RHom}_A(A,-)$ is the underlying complex functor, and it detects zero. Its inverse image is $p_!k$. This is the compactly supported pushforward, not a substitution of ordinary $p_{\rm dR,*}k$. The telescope following (5.5) also directly exhibits the constant's failure of compactness.

**Exercise 17.5 (hard).** Prove that $\mathrm{Dmod}(\mathrm{Bun}_G)$ is the limit over quasi-compact opens, and show independence of a cofinal exhaustion.

**Solution.** The chartwise construction in (6.1) applies because $\mathrm{Bun}_G$ is locally finite type with affine diagonal. Every quasi-compact chart is contained, in the sense of its image, in a finite union of quasi-compact opens. Pull back the object on that union. Enlarging the union gives canonical comparison maps; all finite overlap and nerve diagrams lie in a larger union, where their compatibilities hold. Descent glues the objects, and (6.2) glues every mapping complex, proving essential surjectivity and full faithfulness. If $(U_i)$ is cofinal, every quasi-compact open lies in some $U_i$; use restriction from that $U_i$ to reconstruct its object. Two choices become comparable in a later $U_j$, so the reconstruction is independent and respects all higher maps. This proves the exhaustion version. It neither computes a direct image from the whole stack nor proves its compact generation.

## What this lesson does not prove

We use ordinary scheme-level Spencer theory, Kashiwara's equivalence and base change from earlier lessons. The categorical inputs are existence and universal properties of homotopy limits, module bar resolutions, the finite-cell description of compact DG modules, and strictly unital minimal-model transfer. General fppf descent of crystals is Gaitsgory–Rozenblyum, Corollary 3.2.4 (following h-descent, Proposition 3.2.2); Section 2 gives the covering reconstruction and comparison argument needed here. General prestack/crystal comparison and left/right equivalence are stated in Theorem 4.1, with §5.5, Proposition 2.4.4 and Corollary 2.3.9 as their locators. They require the planned derived algebraic geometry foundations.

The general categorical limit/colimit correspondence in (3.1) is Drinfeld–Gaitsgory, *Compact generation*, Proposition 1.7.5; finite-stage compactness is Corollary 1.9.4 and Lemma 1.9.5. The topological differential-algebra construction on formally smooth ind-schemes is Beilinson–Drinfeld, §7.11, specifically Proposition 7.11.8 and §§7.11.9–7.11.14. The reduced torus Grassmannian in families, Hilburn–Raskin, §2, and its spectral coherent-category and Weyl-action constructions, §§4–5, are stated; their full-faithfulness result is §7.1. We have proved the character transform (3.3), its compactness criterion, and the residue/Weyl sign (4.5).

Compact generation and truncatability of $\mathrm{Bun}_G$, including the twisted extension, are the stated Theorem 6.1. The dual automorphic identification uses *Compact generation*, Corollary 4.3.2, and *Proof of geometric Langlands IV*, §2.1. The determinant and half-root moduli assertions are *Proof I*, §1.1. We do not prove the geometric Langlands equivalence or a miraculous-duality theorem. Sections 1–2, 5 and the proof of (6.1) give the owned descent, point-quotient and open-exhaustion arguments.

## References

- A. Beilinson and V. Drinfeld, [*Quantization of Hitchin's integrable system and Hecke eigensheaves*](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf), §§7.3–7.5 and 7.10–7.11.
- D. Gaitsgory and N. Rozenblyum, [*Crystals and D-modules*](https://arxiv.org/abs/1111.2087), §§1.1–1.3, 2.1–2.4, 3.2 and 5.5.
- V. Drinfeld and D. Gaitsgory, [*On some finiteness questions for algebraic stacks*](https://people.mpim-bonn.mpg.de/gaitsgde/GL/Finiteness.pdf), §§5.3.5, 6.1 and 7.1–7.2.
- V. Drinfeld and D. Gaitsgory, [*Compact generation of the category of D-modules on the stack of G-bundles on a curve*](https://people.mpim-bonn.mpg.de/gaitsgde/GL/Dmod%28BunG%29.pdf), §§0.1–0.4, 1.7, 1.9, 2.1–2.3 and 4.3.
- D. Arinkin and D. Gaitsgory, [*Singular support of coherent sheaves, and the geometric Langlands conjecture*](https://arxiv.org/abs/1201.6343), §11.2.
- D. Gaitsgory, [*Outline of the proof of the geometric Langlands conjecture for GL(2)*](https://arxiv.org/abs/1302.2506), §3.1.
- D. Gaitsgory and S. Raskin, [*Proof of the geometric Langlands conjecture I: construction of the functor*](https://arxiv.org/abs/2405.03599), §1.1.
- D. Arinkin, D. Beraldo, L. Chen, J. Færgeman, D. Gaitsgory, K. Lin, S. Raskin and N. Rozenblyum, [*Proof of the geometric Langlands conjecture IV: ambidexterity*](https://arxiv.org/abs/2409.08670), §2.1.
- J. Hilburn and S. Raskin, [*Tate's thesis in the de Rham setting*](https://arxiv.org/abs/2107.11325), §§2, 4, 5.1–5.2 and 7.1.
