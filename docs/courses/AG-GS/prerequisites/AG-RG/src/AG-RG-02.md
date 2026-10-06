# Regular elements and centralizers

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A maximal torus describes a reductive group by diagonal symmetries. A regular semisimple element describes the same torus by one element: the torus is the identity component of its centralizer. This observation is useful in families, where the centralizer of a section is easier to specify than a choice of eigenvectors.

We use the torus deformation and conjugacy arguments of [Tori, maximal tori and their conjugacy](AG-RG-01.md). The classical geometric input concerning Borel subgroups is used below to prove the centralizer theorem, rather than importing that theorem from a reference. All centralizers are scheme-theoretic. Over a field, a geometric assertion means an assertion after algebraic closure.

## 1. The geometry behind the centralizer theorem

We first work over an algebraically closed field $k$. A Borel subgroup of a smooth connected affine group $H$ is a maximal smooth connected solvable subgroup. Write $B=U\rtimes T$ for a Borel subgroup and one of its maximal tori. The solvable-group construction in the preceding lesson identifies $U$ with the unipotent radical of $B$.

We shall need several consequences of that construction. Every connected solvable subgroup lies in a Borel subgroup. The varieties $H/B$ are projective, and all Borel subgroups are conjugate. The scheme-theoretic normalizer theorem is proved below, after the centralizer and Borel-intersection arguments needed for its induction.

**Lemma 1.1.** The centralizer of a torus in $H$ is smooth and connected.

**Proof.** Smoothness is the invariant-cohomology argument in the preceding lesson. Choose a cocharacter $\lambda$ of $A$ that is nonzero on every nonzero $A$-weight in a finite generating subspace of $k[H]$. Then $C_H(A)=C_H(\lambda)$: in the conjugation grading, a generating function has degree zero for $\lambda$ precisely when it has weight zero for $A$, so the two fixed-subgroup ideals agree.

Use the general cocharacter construction proved in *Roots and reductive groups of rank one*, Section 3. Its proof is a grading and smoothness argument for arbitrary smooth affine groups and uses no reductive centralizer theorem. Multiplication gives an open immersion

$$
U_H(-\lambda)\times C_H(\lambda)\times U_H(\lambda)\longrightarrow H.
$$

The domain is nonempty. Its image is an open subvariety of the irreducible variety $H$, so the domain is irreducible. Its projection onto $C_H(\lambda)$ is surjective; hence that centralizer is connected. This proves the result without making an assertion about the Borel containing an arbitrary element. $\square$

The cocharacter lemma and the classical fixed-point arguments are independent of the root classification and of the reductive centralizer theorem proved below.

Put $X=H/B$, initially as a homogeneous space with stabilizer $B$. Let $T\subset B$ be maximal and $C=C_H(T)$. We justify both finiteness of $X^T$ and the assertion that $C$ fixes it, instead of assuming either one.

First $C=T\times U_C$, with $U_C$ smooth connected unipotent. Indeed $C/T$ is affine: the line detecting the central subgroup $T$ spans a representation on which $T$ acts by scalars, and the resulting projective representation has kernel exactly $T$. Its closed image gives the affine quotient. That quotient has no torus, because the inverse image of a torus would be an extension of tori by tori and contradict maximality of $T$. A smooth connected affine group without a torus is unipotent. To prove this assertion, its Borel subgroup is unipotent by solvable structure. The line detecting that Borel has trivial Borel character, so its orbit is an orbit of a vector in an affine space. The proper quotient by the Borel therefore maps to a complete affine orbit and must be a point. The whole group is that unipotent Borel. Thus $C/T$ is unipotent; $C$ is solvable, and its central torus gives the displayed direct product.

The scheme $X^T$ is smooth. Indeed an equivariant projective embedding gives a $T$-stable affine chart at each fixed point by choosing a nonzero weight coordinate. Exactness of weight projections lifts a weight basis of the cotangent space to homogeneous parameters in the completed local ring. Smoothness of $X$ identifies that ring with the power-series ring in these parameters; imposing fixedness kills precisely the parameters of nonzero weight. The remaining power-series ring proves smoothness of the fixed locus. At each fixed point, the orbit map from $C$ has surjective differential: taking invariants in $\mathfrak h/\mathfrak b'$ is exact, so its tangent space is the quotient of $\mathfrak h^T=\operatorname{Lie}C$ by $\operatorname{Lie}C_{B'}(T)$. Each $C$-orbit is therefore open in $X^T$. There are finitely many of these disjoint open orbits, and each is also closed and complete. Since $T$ fixes the point and is central in $C$, such an orbit is a $U_C$-orbit. Every homogeneous space of a unipotent group is affine: its line-stabilizer character is trivial, so it is a vector orbit, and Lemma 1.2 below makes that orbit closed in affine space. A complete affine orbit has dimension zero. Hence all these orbits are points. We have proved that $X^T$ is finite and that $C$ fixes it pointwise. In particular $C\subset B'$ for every Borel $B'$ containing $T$.

The normalizer acts transitively on $X^T$. If $gB$ is fixed, conjugate $g^{-1}Tg$ to $T$ within $B$ to obtain a representative in $N_H(T)$. Its stabilizer is $N_B(T)=C_B(T)=C$, since conjugation in the solvable decomposition induces the identity on $B/R_u(B)$. Thus $X^T$ is the set $N_H(T)/C_H(T)$, with a simply transitive action of that quotient. A cocharacter separating the finitely many weights in an equivariant projective embedding has exactly the same fixed points as $T$.

**Borel intersections.** For a torus $A\subset B$, the subgroup $C_H(A)\cap B$ is a Borel subgroup of $C_H(A)$. It is connected and smooth by the torus-fixed filtration of the solvable group $B$. To prove completeness of its quotient, put $C=C_H(A)$ and consider the closure of $CB$ in $H$. On that connected closure, the condition $g^{-1}Ag\subset B$ is closed. The composite to the torus $B/R_u(B)$ is constant as a homomorphism from $A$, since such homomorphisms are discrete. At the identity it is the given projection of $A$. Conjugate $g^{-1}Ag$ into a fixed maximal torus of $B$ by $u\in R_u(B)$. The two torus embeddings now have the same projection to $B/R_u(B)$, whose restriction to that maximal torus is an isomorphism. Thus $gu\in C$. This proves that every point of the closure already belongs to $CB$. Therefore the image $C/(C\cap B)$ is closed in the complete $H/B$ and is complete. A connected solvable subgroup with complete quotient is Borel, by the fixed-point theorem applied to a Borel acting on that quotient. Conjugacy in $C$ shows that all its Borels arise in this manner.

**Normalizer theorem.** Every Borel subgroup of a smooth connected affine group over an algebraically closed field satisfies $N_H(B)=B$ as group schemes. We give the induction which supplies the full equality.

First every element of $H$ lies in a Borel. For generic $t\in T$, none of its nonzero adjoint weights takes the value one. The conjugation map $H\times C_H(T)\to H$ has, at $(1,t)$, differential $(1-\operatorname{Ad}t)X+Y$, which is surjective since $\operatorname{Lie}C_H(T)=\mathfrak h^T$. Its image contains a dense open subset. This image lies in the union of conjugates of $B$, since $C_H(T)\subset B$. That union is closed: it is the image of the closed fixed-point incidence in $H\times H/B$ under the proper projection. Hence it is all of $H$. In particular a normal Borel of $H$ equals $H$.

The normalizer is smooth. Its tangent quotient is $(\mathfrak h/\mathfrak b)^B$, contained in $(\mathfrak h/\mathfrak b)^T=0$, because $\mathfrak h^T\subset\mathfrak b$. Thus its tangent dimension equals $\dim B$, as does its local dimension, since it contains $B$. Translation proves smoothness everywhere. It suffices to prove the assertion on geometric points.

Let $n\in N_H(B)(k)$, and conjugate $nTn^{-1}$ back to $T$ by an element of $B$. The resulting $n$ normalizes $T$. Consider the homomorphism $f:T\to T$, $t\mapsto ntn^{-1}t^{-1}$. If $T=1$, the no-torus argument above gives $H=B$. Otherwise, if $f$ is not surjective, its kernel contains a nontrivial torus $A$. Then $n\in C_H(A)$ and normalizes its Borel $C_H(A)\cap B$. If this centralizer is proper, induction on dimension puts $n$ in that Borel. If the centralizer is all of $H$, the torus $A$ is central. Apply induction to the affine quotient $H/A$; the image of $B$ is a Borel since its quotient is the same complete $H/B$. Again $n\in B$.

If $f$ is surjective, choose a representation and line with stabilizer $N_H(B)$. Write $v$ for a generator of the line, and $\chi$ for its character on this stabilizer. Since $\chi$ kills commutators, $\chi\circ f=1$; surjectivity gives $\chi|_T=1$. The unipotent radical of $B$ has no character either, so $B$ fixes $v$. The map $H/B\to V$ given by $gB\mapsto gv$ has complete image in an affine space, so is constant. Thus $H$ fixes $v$, meaning $H=N_H(B)$. The Borel is now normal, and the density argument makes $H=B$. This finishes the induction and proves the scheme equality.

We may consequently identify $H/B$ with the variety of Borel subgroups. The preceding simply transitive action on its torus-fixed points is also the action on the Borels containing $T$.

**Lemma 1.2.** A unipotent group acting on an affine variety has closed orbits.

**Proof.** Replace the variety by the closure $X$ of an orbit $O$, with reduced structure. If the boundary $Z=X\setminus O$ were nonempty, its ideal $I$ would be a nonzero stable ideal in $k[X]$. Local finiteness of representations gives a nonzero finite-dimensional stable subspace of $I$. A unipotent group has a fixed vector in every nonzero representation: triangularize it, whose diagonal characters are all trivial. Hence there is a nonzero invariant $f\in I$. It is constant on $O$, and thus on its closure. A nonzero constant cannot vanish on $Z$. This contradiction shows that the boundary is empty. $\square$

**Lemma 1.3.** Put $I=(\bigcap_{B'\in\mathcal B^T}R_u(B'))^0_{\mathrm{red}}$. Then $I\subset R_u(H)$.

**Proof.** We give the projective argument, including the affine charts that make Lemma 1.2 applicable. Embed $\mathcal B$ equivariantly in $\mathbf P(V)$ using a line with stabilizer $B$, and replace $V$ by the span of the image. Choose a cocharacter $\lambda$ that separates the finitely many $T$-weights in $V$ and whose fixed points on $\mathcal B$ are $\mathcal B^T$.

Among these fixed points there is a unique attracting point $x$ for a dense open set: project the generic point of the irreducible variety onto its lowest nonzero weight coordinate. The lowest weight space occurring there is a line. To check this last assertion, its projectivization meets $\mathcal B$ in finitely many fixed points, while the limits of the dense irreducible open form an irreducible set; nondegeneracy then makes that weight space one-dimensional. The attracting set is therefore

$$
X_x=\mathcal B\cap\{\text{the lowest-weight coordinate is nonzero}\},
$$

an affine open chart. The normalizer of $T$ acts transitively on $\mathcal B^T$, so transporting this chart gives an affine open $X_y$ for every $y\in\mathcal B^T$. It equals $\{z:y\in\overline{Tz}\}$. These charts cover $\mathcal B$: the closure of every $T$-orbit in a complete variety has a fixed point.

Each chart is stable under $I$. Here is the required check. The hyperplane complementary to $X_x$ is the kernel of the lowest-weight covector $\ell$. Every $H$-orbit in $\mathbf P(V^*)$ meets the chart where evaluation on the lowest-weight vector $v$ is nonzero: otherwise its covectors would vanish on every translate of $v$, which spans $V$. On this chart $\lambda^{-1}$ contracts to $[\ell]$. Choose a closed $H$-orbit in the projective space by the closed-orbit lemma. Its closure contains $[\ell]$, so this orbit is exactly $H[\ell]$ and is closed. Thus the stabilizer $P$ of that line has proper homogeneous quotient. The fixed-point theorem for a Borel's action on this quotient puts a conjugate of an $H$-Borel inside $P$. It is contained in $P^0$, and contains a maximal torus of $H$. Since $T\subset P^0$ is also maximal, conjugacy of maximal tori in the smooth connected group $(P^0)_{\mathrm{red}}$ gives an $H$-Borel containing $T$ inside $P$. The group $I$ belongs to its unipotent radical, hence preserves $[\ell]$ and $X_x$. Transporting by $N_H(T)$ proves stability of every $X_y$; the intersection defining $I$ is invariant under that normalizer. This argument does not presume connectedness or self-normalization of parabolic subgroups.

For $z\in\mathcal B$, the complete closure $\overline{Iz}$ has an $I$-fixed point $z_0$. Choose an invariant affine chart $X_y$ containing $z_0$. Its invariant closed complement cannot meet $Iz$, since otherwise it would contain the entire orbit closure and hence $z_0$. Thus $Iz\subset X_y$. Lemma 1.2 makes this orbit closed in $X_y$, so it contains $z_0$ and is a point. We have proved that $I$ fixes every point of $\mathcal B$.

The kernel of this action is the intersection of all Borel subgroups; its reduced identity component is a normal solvable subgroup of $H$. Its unipotent radical is normal in $H$ and contains $I$, because $I$ is unipotent. It is consequently contained in $R_u(H)$. $\square$

This is the geometric mechanism in Chevalley's description of the unipotent radical. It gives exactly the part needed for centralizers without presupposing roots.

## 2. Centralizers and weight zero

**Theorem 2.1.** If $G$ is connected reductive over an algebraically closed field and $T$ is maximal, then $C_G(T)=T$. More generally, the centralizer of any torus in $G$ is connected reductive.

**Proof.** First take $T$ maximal. We already have $C=T\times U_C$ and a finite fixed-point set on $X=G/B$. There is a direct affine-chart proof that $U_C\subset R_u(G)$. Embed $X$ equivariantly in $\mathbf P(V)$ and replace $V$ by the span of $X$. Choose a cocharacter separating its distinct torus weights. The lowest weight space meeting $X$ is one-dimensional: its projective intersection with $X$ is finite, whereas projection of the irreducible open set where that component is nonzero has irreducible image, so is one point; since $X$ spans $V$, its projections span that weight space. The corresponding nonzero-coordinate chart of $X$ is affine. It is stable under $U_C$, since $U_C$ commutes with $T$ and acts trivially on this one-dimensional weight space and its coordinate covector. Transport it by $N_G(T)$ to a chart about every fixed point. These charts remain $U_C$-stable, because that normalizer preserves the characteristic unipotent subgroup of $C$. They cover $X$: a torus orbit closure has a fixed point, and a closed torus-stable complement containing the original point would also contain that limit.

The complete closure of any $U_C$-orbit has a fixed point by the fixed-point theorem. A stable affine chart about that point contains the whole orbit: otherwise its stable closed complement would contain the orbit closure. Within this chart the orbit is closed by Lemma 1.2, so it contains the fixed point and is itself a point. Thus $U_C$ fixes all of $X$. The reduced identity component of the action kernel is a normal solvable subgroup of $G$, since it is contained in $B$. Its unipotent radical is normal in $G$ and contains $U_C$. Reductivity makes it trivial. Therefore $C=T$.

Now let $A\subset G$ be any torus and choose a maximal torus $T\supset A$. Put $C=C_G(A)$. Its Borel subgroups are the intersections $C\cap B'$ for Borel subgroups $B'$ of $G$ containing $A$. To verify this, $C\cap B'$ is connected solvable, and its quotient in $C$ is closed in $G/B'$: if $c_i b_i$ tends to $g$, rigidity of maps from $A$ to $B'/R_u(B')$, followed by conjugacy of torus embeddings in $B'$, changes $g$ by an element of $R_u(B')$ into $C$. Thus $CB'$ is closed; completeness and the fixed-point criterion identify $C\cap B'$ as a Borel subgroup. Conjugating in $C$ supplies all its Borel subgroups.

In particular $R_u(C)$ lies in each $B'$ containing $T$, and, being unipotent, in each $R_u(B')$. Lemma 1.3 gives $R_u(C)\subset R_u(G)=1$. Smoothness and connectedness were Lemma 1.1. This proves reductivity. $\square$

The closedness argument just used can also be written without limits. On the closure $\overline{CB'}$, the condition $g^{-1}Ag\subset B'$ is closed. The induced map $A\to B'/R_u(B')$ is constant as $g$ varies on the connected closure, since maps between tori form a discrete sheaf. Conjugate $g^{-1}Ag$ into a fixed maximal torus of $B'$ by an element $u\in R_u(B')$. Equality of its projection to $B'/R_u(B')$ with that of $A$ then says $gu\in C$. This proves $\overline{CB'}=CB'$ and completes the asserted quotient argument.

**Theorem 2.2.** If $G\to S$ is reductive and $T$ is a maximal $S$-torus, then $C_G(T)=T$. For any subtorus $A$, $C_G(A)$ is a reductive $S$-group.

**Proof.** The centralizer construction commutes with base change and is smooth. Each of its geometric fibres has the properties in Theorem 2.1. For maximal $T$, the inclusion $T\to C_G(T)$ is an isomorphism on geometric fibres. It is an isomorphism over $S$: both schemes are smooth of finite presentation; the differential is an isomorphism, so this inclusion is étale; an étale monomorphism is an open immersion; fibrewise surjectivity makes its image all of the target. The second assertion follows directly from the definition of a reductive group scheme. $\square$

If $T$ is split, write

$$
\mathfrak g=\mathfrak t\oplus\bigoplus_{\alpha\in\Phi}\mathfrak g_\alpha.
$$

Here $\Phi$ is the finite collection of nonzero weights on a neighbourhood where their ranks are constant. Theorem 2.2 says that the zero-weight summand is exactly $\mathfrak t$. In the next lesson we prove that the nonzero summands have rank one and construct their root groups. The arguments about regularity below need the weight decomposition and weight zero; they do not need that rank-one conclusion.

## 3. Three uses of the word regular

Let $G$ be connected reductive over an algebraically closed field, with rank $r=\dim T$. A group element is **dimension-regular** if its centralizer has the minimum dimension $r$. A **regular semisimple** element is a semisimple element $g$ such that $C_G(g)^0$ is a maximal torus. A **strongly regular semisimple** element additionally has $C_G(g)$ itself equal to that torus. This last condition is stronger.

There is also the convention used in SGA 3, Exposé XIII: a group element is regular if the generalized eigenspace for eigenvalue $1$ in its adjoint action has the minimum dimension, the nilpotent rank. For reductive groups this minimum is $r$, and this condition selects exactly the regular semisimple elements. We verify this identification below. Thus dimension-regular unipotent elements are not regular in that convention.

For $t\in T$, define

$$
T_{\mathrm{rs}}=\{t:\alpha(t)\ne1\text{ for every }\alpha\in\Phi\}.
$$

The inequalities mean invertibility of the indicated functions over a general base. Since every $\alpha$ is a nontrivial character, its equation $\alpha=1$ is a proper closed subset of a torus over an algebraically closed field. A finite union of such subsets cannot cover the irreducible torus. Hence $T_{\mathrm{rs}}$ is open and dense, and is nonempty in every geometric fibre in the relative case.

For a semisimple $t$, its centralizer is smooth: the closure of the subgroup generated by $t$ is of multiplicative type, and invariants for such a group are exact. Its Lie algebra is the fixed space of $\operatorname{Ad}(t)$. Consequently

$$
\operatorname{Lie}(C_G(t))=\mathfrak t\oplus
\bigoplus_{\alpha(t)=1}\mathfrak g_\alpha.
$$

The identity centralizer equals $T$ precisely on $T_{\mathrm{rs}}$.

**Theorem 3.1.** The regular semisimple locus $G_{\mathrm{rs}}$ is a dense open subset. Its elements lie in a unique maximal torus.

**Proof.** First construct an open set of conjugates of torus elements. Consider the conjugation map

$$
q:G\times T_{\mathrm{rs}}\longrightarrow G,\qquad(g,t)\longmapsto gtg^{-1}.
$$

After translations identify tangent spaces, its differential at $(1,t)$ is

$$
(X,Y)\longmapsto (1-\operatorname{Ad}(t))X+Y.
$$

It is surjective: the second term covers $\mathfrak t$, while the first is invertible on every nonzero weight summand. Therefore $q$ is smooth and its image is a nonempty open, hence dense in the connected smooth group $G$.

Here is a useful consequence of that density. Choose a Borel $B$ containing $T$. In $G\times G/B$ the incidence scheme

$$
I=\{(g,z):gz=z\}
$$

is closed, since the flag variety is separated. Its projection to $G$ is proper, since $G/B$ is proper. Its image contains the dense open just constructed, and is consequently all of $G$. Over our algebraically closed field, a nonempty fibre has a rational point. Thus **every element of $G$ belongs to a Borel subgroup**.

We also spell out why a semisimple element in $B$ is conjugate within $B$ into a maximal torus. Write $B=T\ltimes U$. The root products proved in [Root data, Weyl chambers and the Bruhat decomposition](AG-RG-04.md), Section 5, give a $T$-stable filtration of $U$ by root height, with vector-group successive quotients. This portion of that later lesson uses the centralizer results of this lesson, but does not use the present regularity argument.

Let $D$ be the reduced closure of the powers of a semisimple $b\in B$. Simultaneous diagonalization in a faithful representation makes $D$ diagonalizable; its finite part has order prime to the characteristic. A diagonalizable subgroup meets a unipotent group trivially, so $D\to T$ identifies it with a diagonalizable subgroup of $T$. Relative to this identification, $D\subset T\ltimes U$ is the graph of a regular crossed homomorphism $D\to U$. For every vector-group quotient of the root-height filtration, degree-one regular cohomology of $D$ vanishes: taking invariants is exact by its character decomposition. Kill the crossed homomorphism in the first quotient by conjugation by a lift in $U$, and repeat along the finite filtration. This conjugates $D$, and hence $b$, into $T$. Conjugacy of Borels and maximal tori now shows that all semisimple elements lie in maximal tori. The preceding weight computation identifies the image of $q$ with precisely the regular semisimple elements.

Any maximal torus containing $g$ belongs to $C_G(g)^0$, because a torus is connected. That identity centralizer is already a maximal torus. This proves uniqueness. $\square$

Minimum centralizer dimension is indeed $r$. On the open set just constructed it is $r$. Upper semicontinuity of fibre dimension at the identity section of the universal centralizer would make any locus of dimension less than $r$ an open set; it would meet the dense open set and contradict the computation there.

For the SGA convention, write the adjoint characteristic polynomial as

$$
P_g(x)=\det(x-\operatorname{Ad}(g))=(x-1)^rQ_g(x).
$$

This divisibility holds for all $g$, since it holds on the dense open locus already proved, and the coefficients are regular functions. The SGA regularity condition is $Q_g(1)\ne0$. Jordan decomposition $g=g_sg_u$ preserves the eigenvalues of the adjoint action, so this condition first implies that $g_s\in G_{\mathrm{rs}}$.

Choose a Borel containing $g$, by the incidence argument. Its Jordan factors belong to this Borel, and conjugating within it places $g_s$ in $T$. The torus projection of $g_u$ is a unipotent torus element and hence is one, so $g_u\in U$. In ordered root coordinates, conjugation by $g_s$ scales the $\alpha$-coordinate by $\alpha(g_s)$. Thus

$$
C_U(g_s)=\prod_{\substack{\alpha\in\Phi^+\\\alpha(g_s)=1}}U_\alpha
$$

as a variety with its ordered coordinates. In particular it is connected, and in the present regular semisimple case the product is empty: $C_U(g_s)=1$. Therefore $g_u=1$. Conversely a regular semisimple element plainly satisfies the condition. This proves the equivalence in every characteristic without any assertion about the connectedness of a cyclic unipotent subgroup.

The minimum generalized zero-eigenspace dimension for $\operatorname{ad}(X)$ similarly defines SGA regularity in a Lie algebra. It is distinct from minimum kernel dimension. Its open set is detected by the first nonzero coefficient after the universal power of $x$ in $\det(x-\operatorname{ad}(X))$. A semisimple $X\in\mathfrak t$ has Lie centralizer $\mathfrak t$ precisely when every root differential $d\alpha(X)$ is nonzero. Such vectors exist when none of the root differentials vanishes identically. In characteristic zero this always holds. In positive characteristic it may fail, and group regularity still works.

## 4. Matrix centralizers and the missing component

For a diagonal matrix $d=\operatorname{diag}(a_1,\ldots,a_n)$ over a field,

$$
(Ad-dA)_{ij}=(a_j-a_i)a_{ij}.
$$

If the eigenvalues are distinct, $A$ is diagonal. Thus a regular semisimple element in $\operatorname{GL}_n$ has diagonal-torus centralizer, and is strongly regular semisimple. Repeated eigenvalues give a product of general linear groups on the corresponding eigenspaces, of larger dimension.

In $\operatorname{SL}_2$, a noncentral diagonal element has centralizer the diagonal torus. For

$$
u=\begin{pmatrix}1&1\\0&1\end{pmatrix},
$$

commutation says $c=0$ and $d=a$ for a matrix $\begin{pmatrix}a&b\\c&d\end{pmatrix}$, and the determinant condition says $a^2=1$. Scheme-theoretically

$$
C_{\operatorname{SL}_2}(u)=
\left\{\begin{pmatrix}a&b\\0&a\end{pmatrix}:a^2=1\right\}
\simeq\mu_2\times\mathbf G_a,
$$

via $(a,x)\mapsto a\begin{pmatrix}1&x\\0&1\end{pmatrix}$. Its dimension is one; $u$ is dimension-regular and is not semisimple. In characteristic two this centralizer is non-smooth. This is why tangent dimension alone cannot define dimension-regularity in every characteristic.

For $\operatorname{PGL}_2$ over a field of characteristic different from two, take the class $t$ of $\operatorname{diag}(-1,1)$. Its root character has value $-1$, so $t$ is regular semisimple. A representative $A$ centralizes the class if $AtA^{-1}=ct$ for some scalar $c$. The eigenvalues force $c=1$ or $-1$. For $c=1$, $A$ is diagonal; for $c=-1$, it is anti-diagonal. Hence

$$
C_{\operatorname{PGL}_2}(t)=T\rtimes(\mathbb Z/2\mathbb Z).
$$

The identity component is the unique torus containing $t$, while the full centralizer has a second component. Regular semisimple must not silently be strengthened to strongly regular semisimple.

In characteristic two, $\mathfrak t\subset\mathfrak{sl}_2$ consists of scalar matrices. Every $\operatorname{ad}(X)$ for $X\in\mathfrak t$ is zero. Nevertheless a diagonal group element with $t^2\ne1$ acts on the upper root space by $t^2\ne1$. Differentiation has lost a nontrivial character.

## 5. Regular sections in a family

Let $G\to S$ be reductive. Define $G_{\mathrm{rs}}$ fibrewise using geometric regular semisimplicity. This is an open subscheme, compatible with every base change. To prove this without making assumptions about $S$, choose a maximal torus étale locally as in the preceding lesson and split it étale locally. The same differential calculation makes

$$
G\times_S T_{\mathrm{rs}}\longrightarrow G
$$

smooth. Its image is open and, on every geometric fibre, precisely the required locus. These opens agree on overlaps and descend. Their fibres are dense and nonempty.

**Theorem 5.1.** A regular semisimple section $s:S\to G$ lies in a unique maximal $S$-torus. Thus, through such a section, no additional base extension is needed. More generally every reductive group has maximal tori étale locally on its base.

**Proof.** Pull back the smooth surjection $q$ over $s$. A smooth surjection has sections étale locally on its target, so étale locally there are $g$ and $t\in T_{\mathrm{rs}}$ with $s=gtg^{-1}$. The torus $gTg^{-1}$ contains $s$.

We must prove uniqueness over bases with nilpotents, not merely uniqueness on geometric fibres. On a chart where $s\in T_{\mathrm{rs}}$, use the big cell $\Omega=U^-TU^+$ and its unique root coordinates, proved in the fourth lesson. Conjugation by $s$ fixes the torus factor and multiplies every root coordinate by $\alpha(s)$. Since all $1-\alpha(s)$ are units, the fixed scheme in this cell is exactly $T$. Consequently $T$ is an open as well as a closed subgroup of $C_G(s)$. Every fibre of a torus containing $s$ maps into this identity-component part, so the inverse image of the open and closed $T$ is the whole torus. It is therefore contained in $T$, and maximality gives equality. This proof works after every base change and makes no claim that the full centralizer is smooth over $S$.

The local tori consequently agree on double overlaps, including their descent data. Affine faithfully flat descent gives the unique global torus. The final assertion is the general torus deformation theorem of the preceding lesson; the regular-section construction supplies a useful additional description whenever such a section is given. $\square$

The full centralizer can have additional components supported on special loci. For example, in $\operatorname{PGL}_2$ take the section $\operatorname{diag}(a,1)$ over a field of characteristic different from two, with $a$ and $a-1$ invertible. Its diagonal torus is present throughout; an anti-diagonal component occurs only on $a=-1$. That component is not flat over the base. The open and closed torus just identified remains the unique maximal torus containing the section.

Here is the precise Lie-algebra version supplied by the same method. Suppose that on every geometric fibre $X$ belongs to the Lie algebra of a maximal torus and every root differential there has nonzero value on $X$. Then there is a unique maximal $S$-torus $T_X$ with $X\in\operatorname{Lie}T_X$. To prove existence, split a local maximal torus and put $\mathfrak t_{\mathrm{rs}}=\{X:d\alpha(X)\text{ is a unit for all roots}\}$. The map

$$
G\times\mathfrak t_{\mathrm{rs}}\longrightarrow\mathfrak g,
\qquad(g,X)\longmapsto\operatorname{Ad}(g)X
$$

has differential $(Y,Z)\mapsto[Y,X]+Z$, which is surjective by these inequalities. It is smooth, and the fibre hypothesis puts the section in its image. Étale local lifts give the desired tori. For uniqueness on such a chart, the equations $\operatorname{Ad}(g)X=X$ have invertible linear coefficients in every moving formal coordinate at the identity. The formal implicit-function calculation leaves exactly the torus parameters: the torus is already a solution, and the invertible moving system has a unique solution over every nilpotent thickening. Thus $T$ is open in this centralizer near the identity, and translation by $T$ makes it open along all of $T$; it is also closed. On a field fibre its identity component is $T$, since its tangent dimension is $\dim T$. A torus whose Lie algebra contains $X$ centralizes $X$ and therefore maps into this open and closed part. The same argument as above proves uniqueness over arbitrary bases, and affine descent glues the local tori.

In characteristic zero the fibre condition holds for every semisimple Lie element with centralizer dimension equal to the rank. Indeed the algebraic closure of its formal exponential is a torus $D$: in a faithful representation its entries are $e^{\lambda_i t}$, whose only Laurent relations are the integer relations among the $\lambda_i$, by exponential independence. The formal exponential lies in the group by the invariant-derivation argument in the first lesson. It follows that $X\in\operatorname{Lie}D$, and a maximal torus containing $D$ contains $X$ in its Lie algebra. The centralizer-dimension condition then says exactly that no root differential vanishes. General SGA-regular Lie sections in small characteristic need not meet this condition; the characteristic-two example above explains why the group regular-section theorem is the unrestricted reductive statement.

For a general smooth connected affine group over a field, a **Cartan subgroup** is $C_G(T)$ for a geometrically maximal torus. Lemma 1.1 and the solvable structure give a smooth connected nilpotent group; over an algebraic closure it is $T$ times a unipotent group. Cartan subgroups are geometrically conjugate by conjugacy of maximal tori. In a reductive group the unipotent factor is trivial by Theorem 2.1, so Cartan subgroups are exactly maximal tori. SGA 3's broader relative Cartan theorem requires a smooth scheme of Cartan subgroups (for instance an affine smooth group with locally constant reductive rank); the reductive case proved here satisfies those hypotheses.

## 6. Exercises and solutions

**Exercise 6.1 (first steps).** Compute the centralizer of a diagonal matrix with distinct eigenvalues in $\operatorname{GL}_n$. If its eigenvalues have multiplicities $m_1,\ldots,m_a$, compute the dimension of its centralizer.

**Solution.** The equations $(a_j-a_i)a_{ij}=0$ allow matrix entries only between equal-eigenvalue subspaces. The centralizer is $\prod_i\operatorname{GL}_{m_i}$ and has dimension $\sum_i m_i^2$. For distinct eigenvalues all $m_i=1$, giving the diagonal torus and dimension $n$.

**Exercise 6.2 (centralizers).** In characteristic different from two, prove $C_{\operatorname{SL}_2}(u)=\mu_2\times U$ for the upper unipotent element displayed above. Determine its component group. Explain what changes in characteristic two.

**Solution.** Multiplying out gives $c=0$, $a=d$ and $a^2=1$. The map $(a,x)\mapsto\begin{pmatrix}a&ax\\0&a\end{pmatrix}$ is an isomorphism of group schemes. In characteristic different from two, $\mu_2$ is étale with two points, so the component group is the constant group of order two. In characteristic two $\mu_2$ is connected and nonreduced, and the centralizer has one geometric component and a two-dimensional tangent space despite having dimension one.

**Exercise 6.3 (universal equations).** Over an arbitrary base scheme, prove that the centralizer of the diagonal torus in $\operatorname{GL}_n$ is that torus. Why is checking only the base field's rational points insufficient?

**Solution.** Use the universal diagonal matrix with independent Laurent coordinates $z_i$. The equation $a_{ij}(z_i-z_j)=0$ forces $a_{ij}=0$ for $i\ne j$ by independence of Laurent monomials over every ring. The diagonal entries are units since the matrix is invertible. Over a finite field the rational points of a torus may not separate all its characters, and over nonreduced algebras rational-point equations may miss infinitesimal conditions; the universal computation avoids both problems.

**Exercise 6.4 (geometry).** Show that the regular semisimple locus of $\operatorname{GL}_n$ is exactly the nonvanishing locus of the discriminant of its characteristic polynomial, and is dense over every algebraically closed field.

**Solution.** If the roots are $a_i$, the discriminant is $\prod_{i<j}(a_i-a_j)^2$, a symmetric polynomial in them and thus a polynomial in the characteristic coefficients. It is nonzero precisely when all eigenvalues are distinct. A matrix with this property is diagonalizable, and Exercise 6.1 gives its torus centralizer. Conversely a semisimple matrix with repeated eigenvalues has larger centralizer, so is not regular semisimple. The polynomial does not vanish identically: choose distinct nonzero elements in the infinite algebraically closed field and take their diagonal matrix. Its nonvanishing locus in the irreducible variety $\operatorname{GL}_n$ is therefore open dense. No assertion that this locus has a rational point over every finite field is needed.

The course prerequisite guide records the exact supporting statements and which lessons are published or still planned.

## References

- J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, 2017, §§17d–h, especially the geometric proof of Chevalley's theorem, and §17j.
- Brian Conrad, [*Reductive group schemes*](https://math.stanford.edu/~conrad/papers/luminysga3.pdf), 2014, §§1.1–1.2, 2.2 and 3.2. These references receive mathematical credit; the centralizer proof above is written out independently.
- A. Grothendieck and the SGA 3 contributors, [*Schémas en groupes*](https://webusers.imj-prg.fr/~patrick.polo/SGA3/), Exposé XIII, Theorem 3.1 and Corollary 3.2, for the relative regular-section theorem and its convention; Exposé XIV for the applications to maximal tori.
