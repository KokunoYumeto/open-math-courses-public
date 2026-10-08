# Category O and the Kazhdan–Lusztig conjecture

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Finite-dimensional highest-weight modules form a semisimple category. Verma modules reveal a different structure: a simple module can occur both as a quotient and as a submodule, extensions need not split, and characters record only part of the information. Category $\mathcal O$ provides a setting in which these infinite-dimensional modules still have finite composition series and projective covers. The connection between those covers and Verma modules is BGG reciprocity.

Throughout, $\mathfrak g$ is a finite-dimensional complex semisimple Lie algebra, with
\[
\mathfrak g=\mathfrak n^-\oplus\mathfrak h\oplus\mathfrak n^+,
\qquad \mathfrak b=\mathfrak h\oplus\mathfrak n^+.
\]
Write $Q^+=\sum_i\mathbb Z_{\geq0}\alpha_i$, $Q=\sum_i\mathbb Z\alpha_i$, and $\rho=\tfrac12\sum_{\alpha>0}\alpha$. The order $\gamma\leq\lambda$ means $\lambda-\gamma\in Q^+$. All highest weights in Sections 1–7 may be arbitrary elements of $\mathfrak h^*$; integrality enters only where explicitly specified. We use the dot action
\[
w\mathbin{\cdot}\lambda=w(\lambda+\rho)-\rho.
\]

The prerequisites are [PBW](../RT-LIE-13.html#theorem-2-1), [Noetherianity](../RT-LIE-13.html#proposition-3-3) and [triangular decomposition](../RT-LIE-13.html#proposition-4-2); [Verma modules](../RT-LIE-14.html#theorem-2-1) $M(\lambda)$ and their [unique simple quotients](../RT-LIE-14.html#theorem-3-1) $L(\lambda)$; and the [Harish-Chandra isomorphism](../RT-LIE-15.html#theorem-4-1) with its [all-complex-weight central-character criterion](../RT-LIE-15.html#corollary-5-2). We also use [Lie’s theorem](../RT-LIE-02.html#theorem-3-1), [finite-dimensional complete reducibility](../RT-LIE-04.html#theorem-4-1), [represented Jordan decomposition](../RT-LIE-04.html#theorem-5-1) and the [finite-dimensional highest-weight classification](../RT-LIE-14.html#theorem-4-1).

For the Weyl and Hecke constructions, the earlier proofs supply [exchange and length](../RT-LIE-08.html#lemma-4-2), the [longest element](../RT-LIE-08.html#theorem-5-1), [rank-two ambient lengths](../RT-LIE-08.html#lemma-7-1), [reduced-word braid moves](../RT-LIE-08.html#lemma-7-2) and the [Coxeter presentation](../RT-LIE-08.html#theorem-7-3). The coinvariant construction uses the [polynomial Weyl-invariant theorem, with its full proof in Sections 9.1–9.7](../RT-LIE-15.html#theorem-9-1). The [Serre presentation](../RT-LIE-11.html#theorem-6-1) provides the relations for the anti-involution constructed below in Section 5.

## 1. A category with bounded weight support

**Definition 1.1.** Category $\mathcal O$ is the full category of $\mathfrak g$-modules $M$ satisfying these three conditions:

1. $M$ is finitely generated over $U(\mathfrak g)$.
2. $\mathfrak h$ acts semisimply: $M=\bigoplus_{\lambda\in\mathfrak h^*}M_\lambda$.
3. $\mathfrak n^+$ acts locally finitely: $U(\mathfrak n^+)v$ is finite-dimensional for every $v\in M$.

Its morphisms are all $\mathfrak g$-linear maps. This is the definition in Bernstein–Gelfand–Gelfand, *Category of $\mathfrak g$-modules*, §3, Definition 1, with the present unshifted highest-weight notation.

**Proposition 1.2.** Every object has finite-dimensional weight spaces, and its support is contained in a finite union of sets $\lambda_j-Q^+$. Kernels, cokernels, submodules, quotients and finite direct sums belong to $\mathcal O$.

**Proof.** Replace a finite generating set by its finitely many weight components. For each resulting weight vector $v_j$, the finite-dimensional space $U(\mathfrak n^+)v_j$ is $\mathfrak h$-stable: commuting $h$ past a root monomial shows that each such monomial has a definite weight. Their sum $E$ is a finite-dimensional $\mathfrak b$-stable generating space. PBW gives a surjection
\[
U(\mathfrak n^-)\otimes E\longrightarrow M. \tag{1.1}
\]
Choose an ordered root-vector basis of $\mathfrak n^-$. A PBW monomial of weight $-\beta$ corresponds to a partition of $\beta$ into positive roots. There are finitely many such monomials: their total exponent is at most the height of $\beta$. Consequently (1.1) proves both assertions about weights.

A submodule is finitely generated because $U(\mathfrak g)$ is left Noetherian. A submodule of an $\mathfrak h$-semisimple module is a direct sum of its weight spaces: for any vector, polynomials in finitely many commuting Cartan operators separate its finitely many weight components. Quotients have the induced weight decomposition. Local $\mathfrak n^+$-finiteness passes to submodules and quotients. Finite sums preserve all three conditions. Kernels and cokernels are therefore computed in the ordinary module category and remain in $\mathcal O$, making $\mathcal O$ an abelian category. $\square$

The support bound also explains local finiteness in the opposite direction. In an $\mathfrak h$-semisimple module with finite weight spaces and support in finitely many upper cones, the weights reachable from a fixed weight by adding positive roots form a finite set. Indeed, the height of the added root combination is bounded in each cone. Thus $U(\mathfrak n^+)v$ is finite-dimensional. This observation will apply to restricted duals.

**Proposition 1.3.** If $F$ is a finite-dimensional $\mathfrak g$-module, then $F\otimes M$ belongs to $\mathcal O$ whenever $M$ does. Tensoring with $F$ is exact.

**Proof.** Finite-dimensional complete reducibility and highest-weight theory imply that $F$ is $\mathfrak h$-semisimple. Hence its tensor product is a weight module with finite weight spaces. For a pure tensor $a\otimes v$, every positive-root monomial acts inside the finite-dimensional space $F\otimes U(\mathfrak n^+)v$. This proves local finiteness.

If $v_1,\ldots,v_r$ generate $M$, a basis of $F$ tensored with these vectors generates $F\otimes M$. Induct on the length of a word in $U(\mathfrak g)$, using
\[
a\otimes xv=x(a\otimes v)-(xa)\otimes v.
\]
The same finite basis handles $xa$. Tensoring vector spaces over $\mathbb C$ is exact, and the diagonal action respects that exactness. $\square$

Every Verma module belongs to $\mathcal O$, by PBW and its upper-cone support; so does each $L(\lambda)$.

## 2. Central characters and finite length

Let $Z=Z(U(\mathfrak g))$. Harish-Chandra's theorem assigns a central character $\chi_\lambda$ to $M(\lambda)$ and gives
\[
\chi_\lambda=\chi_\mu
\quad\Longleftrightarrow\quad
\mu\in W\mathbin{\cdot}\lambda. \tag{2.1}
\]
This equivalence holds for complex weights, including singular and nonintegral ones.

**Proposition 2.1.** For every $M\in\mathcal O$, the action of $Z$ factors through a finite-dimensional commutative algebra. There is a canonical finite decomposition
\[
M=\bigoplus_\chi M_\chi,
\qquad
M_\chi=\{v:\text{some power of }\ker\chi\text{ annihilates }v\}. \tag{2.2}
\]
On each nonzero summand a single power of $\ker\chi$ annihilates the entire summand. The projection functors are exact, and maps between different summands vanish.

**Proof.** Take the finite sum $E'$ of the entire weight spaces containing a finite weight generating set. It is finite-dimensional and $Z$-stable. If a central element kills $E'$, it kills $M$. Therefore $Z/\operatorname{Ann}_Z(M)$ injects into $\operatorname{End}_{\mathbb C}(E')$.

For completeness, a finite-dimensional commuting algebra over $\mathbb C$ decomposes into its generalized joint eigenspaces. One can construct them by successively decomposing for a finite vector-space basis of the algebra; commuting operators preserve every decomposition already made. On a joint summand, each operator is its scalar eigenvalue plus a commuting nilpotent. Simultaneous upper triangularization shows that the eigenvalues define a multiplicative character. The ideal of operators with eigenvalue zero is strictly upper triangular, so its sufficiently high power is zero. Polynomial spectral projections give orthogonal idempotents whose sum is the identity. Applying these idempotents to $M$ proves (2.2), including the uniform exponent. The construction is canonical, since the annihilator condition characterizes each summand.

For an exact sequence, apply the same construction using the finite-dimensional image of $Z$ on the middle term. Its idempotents act on the two other terms and preserve exactness. Maps commute with $Z$ and hence with these idempotents; this proves the last assertion. $\square$

Write $\mathcal O_\chi$ for the category of objects satisfying the generalized-character condition. Thus
\[
\mathcal O=\bigoplus_\chi\mathcal O_\chi, \tag{2.3}
\]
where each object has only finitely many components. Generalized eigenvalues matter: imposing that every central element act by its scalar would exclude some projective covers.

**Theorem 2.2.** The simple objects are exactly $L(\lambda)$, one for each $\lambda\in\mathfrak h^*$. Every object of $\mathcal O$ has finite length.

**Proof.** Every nonzero object or subquotient has a maximal weight. Starting at any weight and ascending in the positive-root order must stop, since its height above that starting weight is bounded by the finitely many upper cones. A nonzero vector at a maximal weight is killed by $\mathfrak n^+$, so it defines a map from a Verma module. If the object is simple, this map is surjective, giving $L(\lambda)$. Two such simples cannot have different highest weights: each is generated by its highest vector, and all its weights lie below that weight. Mutual isomorphism would give both inequalities. Its highest weight space is one-dimensional, so also
\[
\operatorname{End}_{\mathfrak g}L(\lambda)=\mathbb C. \tag{2.4}
\]

The zero object has length zero, so assume $M\ne0$ and fix $M\in\mathcal O_\chi$. The character $\chi$ is of the form $\chi_\lambda$: apply the preceding highest-vector argument to $M$, and compare the scalar central action on that vector with its generalized eigenvalue. Let $S=W\mathbin{\cdot}\lambda$, a finite set. In any nonzero subquotient $N$, a highest vector of weight $\gamma$ has central character $\chi_\gamma$. The generalized-character condition and (2.1) imply $\gamma\in S$. Thus
\[
N\ne0\quad\Longrightarrow\quad
N[S]:=\bigoplus_{\gamma\in S}N_\gamma\ne0. \tag{2.5}
\]
Taking a weight space is exact in the category of weight modules. Every strict inclusion in a chain of submodules therefore contributes at least one to the dimension of $M[S]$. All chain lengths are bounded by this finite dimension. Successively taking a maximal proper submodule now terminates in a composition series. For a general object, use the finite decomposition (2.2). $\square$

The number $[M:L(\lambda)]$ of occurrences in a composition series is independent of that series. Here is the usual finite-length argument: compare two simple initial subobjects. If they coincide, pass to the quotient; if distinct, their intersection is zero and their sum is their direct sum, so quotienting by that sum exchanges their order. Induction on length proves independence.

A generalized central-character category need not be an indecomposable block. Root spaces preserve weight cosets modulo $Q$, so every object also decomposes into its finitely many root-lattice cosets, and all maps respect this decomposition. Section 7 exhibits a central character with two separate semisimple blocks. We use “block” for an indecomposable category summand.

## 3. Building projectives without an integrality restriction

An object $P$ is **projective in $\mathcal O$** if $\operatorname{Hom}_{\mathfrak g}(P,-)$ is exact on $\mathcal O$. This assertion concerns this category, not all $U(\mathfrak g)$-modules.

**Lemma 3.1.** If $\nu$ is maximal in its finite dot orbit, then $M(\nu)$ is projective in $\mathcal O$.

**Proof.** All composition factors of $X\in\mathcal O_{\chi_\nu}$ have highest weights in that orbit. Their supports, and therefore the support of $X$, lie below those highest weights. A weight strictly above $\nu$ cannot occur: it would force an orbit point strictly above $\nu$. Every vector in $X_\nu$ is consequently singular. The Verma universal property gives the natural isomorphism
\[
\operatorname{Hom}_{\mathfrak g}(M(\nu),X)=X_\nu.
\]
This is exact. Hom into other central-character summands is zero, and exact central projection extends the assertion to all of $\mathcal O$. $\square$

Finite tensor products preserve projectives, because the elementary tensor adjunction gives
\[
\operatorname{Hom}_{\mathfrak g}(F\otimes P,X)
\simeq\operatorname{Hom}_{\mathfrak g}(P,F^*\otimes X), \tag{3.1}
\]
and the functor on the right is exact. The isomorphism is obtained by contracting against a basis and its dual; the dual action on $F^*$ makes it $\mathfrak g$-equivariant.

**Theorem 3.2.** Category $\mathcal O$ has enough projectives.

**Proof.** First produce a projective mapping onto each simple $L(\mu)$. Choose a large integer $N$ and put $\eta=2N\rho$. It is a dominant integral weight. For $N$ sufficiently large, the real part of $a=\mu+\eta+\rho$ lies in the strict dominant chamber. Set $\nu=\mu+\eta$.

This $\nu$ is maximal in its dot orbit. Indeed, for a real strictly dominant $a_0$ and a reduced word $w=s_{i_1}\cdots s_{i_k}$,
\[
a_0-wa_0=
\sum_{j=1}^k\langle a_0,\alpha_{i_j}^{\vee}\rangle
 s_{i_1}\cdots s_{i_{j-1}}\alpha_{i_j}. \tag{3.2}
\]
Each root on the right is positive and each coefficient is positive. Formula (3.2) follows by telescoping $1-w$. If $w\mathbin{\cdot}\nu>\nu$, taking real parts would put both $a_0-wa_0$ and its negative in the positive-root cone, which is pointed. Strict dominance then forces $w=1$, contradicting the strict inequality.

The tensor of highest vectors in $L(\eta)\otimes L(\mu)$ is a nonzero highest vector of weight $\nu$. It gives a nonzero map from $M(\nu)$ to that tensor product. By (3.1), the projective
\[
L(\eta)^*\otimes M(\nu)
\]
has a nonzero map to $L(\mu)$, necessarily a surjection.

Finally induct on composition length. In $0\to A\to X\to L\to0$, take projectives surjecting onto $A$ and $L$. Lift the latter map to $X$ by projectivity. The sum of the lifted map and the map to $A\subset X$ is surjective onto $X$. The induction starts with the zero object and the simple case just proved. $\square$

**Theorem 3.3.** Each $L(\lambda)$ has a unique projective cover $P(\lambda)$ up to isomorphism. Every projective is a finite direct sum of these covers, and
\[
\dim\operatorname{Hom}_{\mathfrak g}(P(\lambda),X)
=[X:L(\lambda)]. \tag{3.3}
\]

**Proof.** All Hom spaces in $\mathcal O$ are finite-dimensional: a map is determined by finitely many weight generators, each of whose images lies in a finite-dimensional target weight space. Decompose a nonzero projective by repeatedly splitting direct summands until each summand is indecomposable; finite length makes this terminate.

For an endomorphism $u$ of any finite-length object, the kernels and images of $u^k$ stabilize. For a sufficiently large $k$,
\[
P=\ker u^k\oplus\operatorname{im}u^k.
\]
To verify the equality, stabilized images make $u^k$ surjective on its image, while stabilized kernels give zero intersection; length additivity then gives the whole object. On an indecomposable object, an endomorphism is therefore either invertible or nilpotent.

Let $f\colon P\twoheadrightarrow L$ be an epimorphism from an indecomposable projective to a simple. If a proper subobject $T$ still mapped onto $L$, projectivity would lift $f$ through $T$, giving an endomorphism $u$ with image in $T$ and $fu=f$. It would be nilpotent, whereas iteration gives $fu^k=f\ne0$. This contradiction shows that $f$ is an essential epimorphism: no proper subobject surjects onto its target. Every proper subobject of $P$ lies in $\ker f$, for otherwise its image in $L$ would be nonzero. Thus $\ker f$ is the unique maximal subobject and $L$ the unique simple head. This is a projective cover.

Enough projectives gives such an indecomposable summand above each simple. Two covers of the same simple lift each other's quotient maps. The two composites induce the identity on that simple, so cannot be nilpotent; they are invertible. The lifts are therefore isomorphisms. Conversely every nonzero indecomposable projective has a simple quotient and hence is one of these covers. Formula (2.4) and the unique head give
\[
\dim\operatorname{Hom}(P(\lambda),L(\mu))=\delta_{\lambda\mu}.
\]
Exactness of Hom from a projective, applied along a composition series, proves (3.3). $\square$

## 4. Why projective covers have Verma filtrations

A **Verma filtration** is a finite filtration by $\mathfrak g$-submodules whose successive quotients are Verma modules. First we build such filtrations on the tensor projectives used above.

**Lemma 4.1 (tensor identity).** For finite-dimensional $F$,
\[
F\otimes M(\nu)\simeq
U(\mathfrak g)\otimes_{U(\mathfrak b)}(F|_{\mathfrak b}\otimes\mathbb C_\nu). \tag{4.1}
\]
The map sends $u\otimes(a\otimes1)$ to $u(a\otimes v_\nu)$.

**Proof.** The diagonal $\mathfrak b$ action makes the map well-defined. PBW identifies both sides as vector spaces with $U(\mathfrak n^-)\otimes F$. Filter the negative-root factor by PBW degree. Expanding the diagonal action of a monomial $u$, the term $a\otimes uv_\nu$ has full degree on the Verma factor; all other terms have smaller degree there. Thus the map on associated graded spaces is the interchange of the two factors, an isomorphism. Induction on degree proves injectivity and surjectivity of (4.1). $\square$

Lie's theorem supplies a complete $\mathfrak b$-stable flag in $F$. Each one-dimensional quotient has some weight $\xi$ and trivial $\mathfrak n^+$ action, since $[\mathfrak b,\mathfrak b]=\mathfrak n^+$. Induction from $\mathfrak b$ is exact: PBW makes $U(\mathfrak g)$ a free right $U(\mathfrak b)$-module. Applying it to that flag in (4.1) proves that $F\otimes M(\nu)$ has Verma factors $M(\nu+\xi)$, with each weight repeated according to its multiplicity in $F$.

It remains to justify passing to a direct summand. This requires more than merely declaring that filtrations split.

Put $A=U(\mathfrak n^-)$ and let $I$ be its augmentation ideal. Give a negative root vector for $-\alpha$ degree $\operatorname{ht}(\alpha)$. The root brackets make this a positive grading, with $A_0=\mathbb C$. In a fixed weight coset modulo $Q$, choose a reference weight and grade a vector by the height of its downward displacement. Upper-cone support bounds this grading below. There are finitely many cosets, and all maps under discussion preserve weights. PBW shows that a Verma module is graded free of rank one over $A$. An extension of two finite graded free $A$-modules is graded split, by lifting homogeneous basis vectors of the quotient. Hence any Verma-filtered object is finite graded free over $A$.

**Lemma 4.2 (graded freeness).** A weight-preserving direct summand $P$ of a finite graded free $A$-module with grading bounded below is itself finite graded free, with a basis of weight vectors.

**Proof.** The elementary graded Nakayama argument is that a bounded-below graded module $N$ satisfying $N=IN$ is zero: its lowest nonzero homogeneous degree could not come from multiplication by positive-degree elements.

The quotient $P/IP$ is finite-dimensional, since it is a summand of the corresponding quotient of the original free module. Choose a weight basis and lift it to weight vectors in $P$. The resulting map from a finite graded free module $H$ to $P$ is surjective: its cokernel has zero augmentation quotient, so graded Nakayama applies. It has a weight-preserving section. To see this without assuming an ungraded section preserves weights, lift each homogeneous free basis vector of the original module through $H\to P$, extending to an $A$-linear map, then restrict to its summand $P$.

Write $H=P\oplus K$ using this section. The chosen basis makes $H/IH\to P/IP$ an isomorphism, and the splitting gives $K/IK=0$. The kernel $K$ is bounded below, so graded Nakayama gives $K=0$. The lifted vectors form the required free basis. $\square$

**Lemma 4.3.** If $X\in\mathcal O$ is finite free over $A$ with a basis of weight vectors, then $X$ has a Verma filtration.

**Proof.** Choose a maximal weight $\lambda$ among its finitely many free generators and let $v$ be the corresponding generator. Every weight of $X$ lies below some generator weight. Thus no weight $\lambda+\alpha$, $\alpha>0$, can occur, and $v$ is singular. The universal map $M(\lambda)\to X$ is injective because its PBW basis maps to the free $A$-summand $Av$. Its image is a $\mathfrak g$-submodule. The quotient remains in $\mathcal O$ and is finite graded free over $A$, of rank one less. Induct on that rank. $\square$

**Theorem 4.4.** Every projective in $\mathcal O$ has a Verma filtration.

**Proof.** A tensor projective $F\otimes M(\nu)$ surjects onto each simple $L(\lambda)$ as in Theorem 3.2. Lift that surjection through its cover $P(\lambda)$. Essentiality makes the lift surjective; projectivity of the cover splits it. Thus the cover is a weight-preserving direct summand of the tensor projective. Lemmas 4.1–4.3 give its Verma filtration. Finite direct sums give the assertion for all projectives. $\square$

This also proves that every direct summand of a Verma-filtered object is Verma-filtered. The grading is essential to the freeness argument; no assertion that arbitrary ungraded projective modules over an arbitrary algebra are free has been used.

## 5. Restricted duality and costandard modules

The Serre presentation gives an anti-involution $\omega$ of $U(\mathfrak g)$ with
\[
\omega(e_i)=f_i,\qquad \omega(f_i)=e_i,\qquad
\omega(h_i)=h_i,\qquad \omega(uv)=\omega(v)\omega(u). \tag{5.1}
\]
Here is a direct check of its existence. Reverse words in the free associative algebra on these generators and interchange $e_i,f_i$. The Cartan commutation relations are preserved: reversal changes the sign of a commutator, which is exactly compensated in the $[h_i,e_j]$ and $[h_i,f_j]$ relations. The relation $[e_i,f_j]=\delta_{ij}h_i$ maps to $[e_j,f_i]=\delta_{ij}h_i$. A repeated commutator in a Serre relation maps, up to an overall sign, to its counterpart with $e$ and $f$ exchanged. Thus the defining ideal is stable. Repeating the operation gives the identity, proving (5.1).

For a module with finite weight spaces define its **restricted dual** by
\[
D M=\bigoplus_\lambda M_\lambda^*,\qquad
(x\varphi)(v)=\varphi(\omega(x)v). \tag{5.2}
\]
Reversal in (5.1) makes (5.2) a left action. It keeps, rather than negates, the weight: $D M$ has the same weight multiplicities as $M$. Weightwise vector-space duality is exact, and finite-dimensional biduality gives a natural $D^2M\simeq M$.

**Proposition 5.1.** Restricted duality is an exact contravariant equivalence $D:\mathcal O\to\mathcal O$, and $D L(\lambda)\simeq L(\lambda)$.

**Proof.** First consider a simple $L=L(\lambda)$ in the category of all finite-weight-space modules. A proper nonzero submodule $T\subset D L$ has a proper nonzero annihilator in $L$: weight decomposition and finite-dimensional duality make both assertions true. This annihilator is $\mathfrak g$-stable by (5.1)–(5.2), contradicting simplicity. Hence $D L$ is simple. It has the same upper support and one-dimensional top of weight $\lambda$, so its top is singular and it is $L(\lambda)$.

Apply the exact functor $D$ to a finite composition series of an object $M$. Its successive quotients are the same simple highest-weight modules. This proves finite generation of $D M$: an extension of two finitely generated modules is generated by generators of the submodule and lifts of generators of the quotient. The support and finite weight spaces are unchanged, so the support observation after Proposition 1.2 proves local $\mathfrak n^+$-finiteness. Thus $D M\in\mathcal O$, and the biduality already established proves the equivalence. $\square$

Set
\[
\nabla(\mu)=D M(\mu),
\]
the **costandard module**. It has the same character and composition multiplicities as $M(\mu)$, although it generally has a different submodule structure.

**Lemma 5.2.** For all weights $\lambda,\mu$,
\[
\dim\operatorname{Hom}_{\mathfrak g}(M(\lambda),\nabla(\mu))
=\delta_{\lambda\mu},
\qquad
\operatorname{Ext}^1_{\mathcal O}(M(\lambda),\nabla(\mu))=0. \tag{5.3}
\]
Here $\operatorname{Ext}^1$ means equivalence classes of short exact sequences within $\mathcal O$.

**Proof.** A singular functional in $D M(\mu)$ annihilates $\mathfrak n^-M(\mu)$, since $\omega$ interchanges the two nilpotent algebras. The quotient $M(\mu)/\mathfrak n^-M(\mu)$ is its one-dimensional highest line. Thus singular functionals occur only at weight $\mu$, and form a one-dimensional space. The Verma universal property proves the Hom formula.

We prove the extension assertion by constructing a splitting. As a $\mathfrak b$-module, $\nabla(\mu)$ is the restricted coinduced module consisting of functions $f:U(\mathfrak b)\to\mathbb C$ with
\[
f(hu)=\mu(h)f(u),\qquad
(xf)(u)=f(ux), \tag{5.4}
\]
where only finitely many weight components are allowed. To identify it with (5.2), send a functional $\varphi$ to
\[
f(u)=\varphi(\omega(u)v_\mu).
\]
PBW, ordered with Cartan factors first, identifies $U(\mathfrak n^+)$ with the corresponding negative-root monomials under $\omega$. This proves bijectivity and verifies both rules in (5.4).

For any $\mathfrak h$-semisimple $\mathfrak b$-module $N$, evaluation at $1$ gives
\[
\operatorname{Hom}_{\mathfrak b}(N,\nabla(\mu))
\simeq\operatorname{Hom}_{\mathfrak h}(N,\mathbb C_\mu). \tag{5.5}
\]
Explicitly, the inverse sends an $\mathfrak h$-linear functional $\ell$ to the map $v\mapsto f_v$, where $f_v(u)=\ell(uv)$. For a weight vector $v$ of weight $\gamma$, this function has weight $\gamma$, and can be nonzero on positive-root monomials only at root degree $\mu-\gamma$. There are finitely many such PBW monomials. Thus it belongs to the restricted, rather than completed, coinduced module. For a general vector use its finite weight decomposition. These formulas prove both directions of (5.5).

The right side is exact on weight modules: it is the ordinary dual of the $\mu$ weight space, and vector-space functionals extend across subspaces. Consequently $\nabla(\mu)$ is injective as a $\mathfrak b$-module within this weight category.

In an extension
\[
0\to\nabla(\mu)\longrightarrow E\overset{\pi}{\longrightarrow}M(\lambda)\to0
\]
this injectivity extends the identity on $\nabla(\mu)$ to a $\mathfrak b$-linear retraction $r:E\to\nabla(\mu)$. Lift the highest vector to a weight vector $v$ in $E$ and replace $v$ by $v-r(v)$. It lies in $\ker r$ and still projects to the highest vector. Its $\mathfrak n^+$ images lie both in $\ker r$ and in $\ker\pi=\nabla(\mu)$; their intersection is zero. The corrected lift is singular, so the universal property gives a $\mathfrak g$-linear section of $\pi$. The extension splits. $\square$

## 6. BGG reciprocity

Write $(P(\lambda):M(\mu))$ for the number of occurrences of $M(\mu)$ in a Verma filtration. The following theorem proves, in particular, that this number does not depend on the filtration.

**Theorem 6.1 (BGG reciprocity).** For all complex weights $\lambda,\mu$,
\[
\boxed{(P(\lambda):M(\mu))=[M(\mu):L(\lambda)].} \tag{6.1}
\]

**Proof.** Compute $\dim\operatorname{Hom}(P(\lambda),\nabla(\mu))$ in two ways. For a filtration step
\[
0\to P_{j-1}\to P_j\to M(\gamma_j)\to0,
\]
restriction of maps into $\nabla(\mu)$ is surjective by (5.3). Indeed, pushing out this extension along any map $P_{j-1}\to\nabla(\mu)$ produces an extension of $M(\gamma_j)$ by $\nabla(\mu)$, which splits; a splitting supplies the required extension of the map. Its kernel is $\operatorname{Hom}(M(\gamma_j),\nabla(\mu))$, of dimension $\delta_{\gamma_j\mu}$. Summing along the filtration gives
\[
\dim\operatorname{Hom}(P(\lambda),\nabla(\mu))
=(P(\lambda):M(\mu)).
\]
On the other hand, projectivity and (3.3) give this same dimension as $[\nabla(\mu):L(\lambda)]$. Exact duality fixes the simples, so the latter equals $[M(\mu):L(\lambda)]$. $\square$

This is a relation between two different filtrations, not an isomorphism between a projective and a sum of Vermas. In particular, define the decomposition and Cartan matrices in a central-character summand by
\[
d_{\mu\lambda}=[M(\mu):L(\lambda)],\qquad
c_{\lambda\gamma}=[P(\gamma):L(\lambda)].
\]
There are finitely many simple labels by (2.1). Counting composition factors through a Verma filtration proves
\[
c_{\lambda\gamma}=\sum_\mu d_{\mu\lambda}d_{\mu\gamma},
\qquad C=D^{\mathsf T}D. \tag{6.2}
\]
Also $D$ is triangular with diagonal entries one in any total ordering extending the highest-weight order: all weights of $M(\mu)$ lie below $\mu$, and its highest line occurs once. Thus $\det D=1$ and $\det C=1$ within such a finite summand.

Dualizing projective covers gives injective hulls. Exact contravariant duality takes the lifting property to the extension property, so $D P(\lambda)$ is injective. The injection $L(\lambda)\to D P(\lambda)$ is essential: dualizing a nonzero subobject disjoint from it would produce a proper quotient obstruction to the essential cover. More explicitly, if $T\cap L(\lambda)=0$, the surjection $D P(\lambda)\to D P(\lambda)/T$ is injective on $L(\lambda)$; its dual identifies a proper subobject of $P(\lambda)$ still surjecting onto $L(\lambda)$ unless $T=0$. This proves essentiality. Every object embeds into a finite sum of these injectives by dualizing Theorem 3.2.

## 7. Every central-character category for $\mathfrak{sl}_2$

Use $[h,e]=2e$, $[h,f]=-2f$, $[e,f]=h$, and identify a weight with its value on $h$. On $M(\lambda)$, put $v_k=f^kv_0$. PBW and induction give
\[
fv_k=v_{k+1},\quad hv_k=(\lambda-2k)v_k,\quad
 ev_k=k(\lambda-k+1)v_{k-1}. \tag{7.1}
\]
Here $v_{-1}=0$. For example, the induction uses $ef^k=fef^{k-1}+hf^{k-1}$ and the weight of $f^{k-1}v_0$.

Any nonzero submodule has a highest weight vector, and each weight space here has dimension one. Formula (7.1) therefore implies
\[
M(\lambda)\text{ is simple}\quad\Longleftrightarrow\quad
\lambda\notin\mathbb Z_{\geq0}. \tag{7.2}
\]
For $\lambda=n\geq0$, the only proper singular line is generated by $v_{n+1}$. Its weight is $-n-2$, and its downward tail is an embedded simple $M(-n-2)$. Every proper nonzero submodule must be exactly that tail. The resulting sequence is
\[
0\to M(-n-2)\to M(n)\to L(n)\to0,
\qquad \dim L(n)=n+1. \tag{7.3}
\]
It does not split: a complement would contain the unique weight-$n$ line and hence generate all of $M(n)$.

The centre is generated by
\[
\Omega=h^2+2h+4fe,
\qquad \chi_\lambda(\Omega)=\lambda(\lambda+2), \tag{7.4}
\]
as follows also from the rank-one Harish-Chandra isomorphism. Two labels have the same character precisely when they are $\lambda$ and $-\lambda-2$.

There are three cases.

* If $\lambda\notin\mathbb Z$, the two labels lie in different cosets modulo $2\mathbb Z$. Each corresponding category has only one simple, a simple Verma. Its highest-weight functor is exact within that coset, just as in Lemma 3.1: there is no other simple highest weight above it. It is projective. Every finite composition series then splits by induction. Thus this central-character category is the direct sum of two semisimple blocks, each equivalent to finite-dimensional vector spaces.
* At $\lambda=-1$, there is just one label. The same argument makes $M(-1)=L(-1)$ projective, and the category is one semisimple block.
* Every remaining character has the pair $n,-n-2$ with $n\in\mathbb Z_{\geq0}$. Write $X=L(n)$, $Y=M(-n-2)$. Here $P_X=M(n)$, by Lemma 3.1 and its unique simple head. BGG reciprocity says $P_Y$ has one Verma factor of each label. The sequence (7.3) already shows that this category is indecomposable.

We now construct the second projective in the last case, rather than inferring its existence only from its character. The object $L(n+1)\otimes M(-1)$ is projective, since $M(-1)$ is projective. Its Verma factors, from the weights of $L(n+1)$, are
\[
M(n),M(n-2),\ldots,M(-n-2).
\]
Project to the generalized character $\chi_n$. Only the two endpoints survive, by (7.4). Taking a $\mathfrak b$-flag starting with the highest line shows that the projection $Q_n$ sits in
\[
0\to M(n)\to Q_n\to M(-n-2)\to0. \tag{7.5}
\]
It is indecomposable. Otherwise its two nonzero projective summands would each have a Verma filtration, and their nonnegative Verma multiplicities must split the two distinct factors in (7.5). One summand would then be $M(-n-2)=Y$. But $Y$ is not projective: the dual of (7.3) is a nonsplit extension
\[
0\to X\to D M(n)\to Y\to0.
\]
The additivity and independence needed in this argument also follow directly from Verma characters: multiplying a finite character relation by $\prod_{\alpha>0}(1-e^{-\alpha})$ leaves a relation between distinct exponentials.

The simple head of $Q_n$ is $Y$, so $Q_n=P_Y$. Its radical is the submodule $M(n)$ in (7.5), with its own radical $Y$. Its socle is exactly this last $Y$: a simple outside $M(n)$ would map isomorphically to the quotient $Y$ and split (7.5), while the only simple submodule inside $M(n)$ is $Y$. Thus its successive Loewy layers, from socle to head, are
\[
P_X:\ Y,X,
\qquad P_Y:\ Y,X,Y. \tag{7.6}
\]
For every regular integral block, in the order $X,Y$,
\[
D=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
C=\begin{pmatrix}1&1\\1&2\end{pmatrix}. \tag{7.7}
\]

### The principal block as an explicit tensor product

Take $n=0$. In $L(1)$ choose vectors $a,b$ with $ha=a$, $hb=-b$, $fa=b$, $eb=a$, $ea=fb=0$. In $M(-1)$ use $v_k$ as above; then $ev_k=-k^2v_{k-1}$. Put
\[
Q=L(1)\otimes M(-1),\qquad
p=a\otimes v_0,\quad q=b\otimes v_0.
\]
They have weights $0,-2$, with
\[
ep=0,\qquad eq=p,\qquad
fp=b\otimes v_0+a\otimes v_1. \tag{7.8}
\]
They freely generate $Q$ over $\mathbb C[f]$. Indeed,
\[
f^kp=a\otimes v_k+k b\otimes v_{k-1},\qquad
f^kq=b\otimes v_k,
\]
so these vectors form a triangular basis of the tensor product. The $\mathfrak g$-module is generated by $q$, since $eq=p$. The submodule generated by $p$ is $M(0)$, and its quotient is $M(-2)$; hence all of $Q$ has generalized character $\chi_0$. In particular the requested direct summand of $L(1)\otimes M(-1)$ is the entire tensor product:
\[
Q=P(-2),\qquad
0\subset U(\mathfrak g)p\subset Q,\quad
U(\mathfrak g)p\simeq M(0),\quad Q/U(\mathfrak g)p\simeq M(-2). \tag{7.9}
\]
Every weight-$-2$ lift of the quotient's top has the form $q+c fp$, and its $e$ image is always $p$, since $efp=0$. Thus (7.9) does not split. Alternatively, $Q$ is projective, has a quotient $L(-2)$, and has no map to $L(0)$: its generator $q$ has weight $-2$. The multiplicity of the head $L(-2)$ is one, so it is the cover.

The generalized central action is visible:
\[
\Omega p=0,\qquad \Omega q=4fp,\qquad \Omega^2Q=0,
\quad\Omega Q\ne0. \tag{7.10}
\]
The weight-$-2$ singular vectors are exactly multiples of $fp$. It generates the unique socle $L(-2)$.

### A five-dimensional algebra describing a regular block

Put $P=P_X\oplus P_Y$. By (3.3) and (7.7), $\operatorname{End}(P)$ has dimension five. Let $a:P_X\to P_Y$ be the inclusion in (7.5), and choose nonzero $b:P_Y\to P_X$. The image of $b$ is the socle $Y$: its image cannot surject onto the head $X$, since $P_Y$ has head $Y$. The composite $ba$ is an endomorphism of $P_X$, whose endomorphism space has dimension one; its image is proper, so $ba=0$. As $a$ is injective, $ab\ne0$, and $(ab)^2=0$.

Thus the algebra has basis
\[
1_X,1_Y,a,b,ab,
\]
and is the path algebra of two vertices $X,Y$, arrows $a:X\to Y$, $b:Y\to X$, and the relation $ba=0$, with composition read right to left. All paths of length three vanish, and these five paths already account for its dimension. For $n=0$ one can take $b(q)=fv_0$ in $M(0)$ and $b(p)=0$; the quotient $Q\to Y$ followed by its embedding into $M(0)$ proves this is a module map.

For clarity about sides, $\operatorname{Hom}(P,-)$ takes values in finite-dimensional **right** $\operatorname{End}(P)$-modules, acting by precomposition; equivalently these are left modules over the opposite algebra. On this regular block, this functor is an equivalence. Here is a proof in the present setting. Projective covers and finite length give every object a finite presentation
\[
P^r\to P^s\to M\to0:
\]
choose a surjection first, then one onto its kernel. Exact Hom from $P$ gives a presentation by free right modules. The functor is faithful: if it annihilates a morphism, exactness annihilates its image, which must be zero by (3.3). For fullness, let a module map between the Hom spaces of $M$ and $N$ be given. Compose it with the free presentation of $M$ above. A map from $\operatorname{Hom}(P,P^s)$ to $\operatorname{Hom}(P,N)$ corresponds, by its values on the free generators, to a unique map $P^s\to N$. Its composite with the relation map $P^r\to P^s$ is zero after applying the functor, and hence is zero by faithfulness. It therefore descends to $M\to N$, inducing the given module map. This proves full faithfulness. Conversely every finite-dimensional right module over this finite-dimensional algebra has a finite free presentation. Realize its matrix between free modules as a map between sums of $P$ and take the cokernel in $\mathcal O$. Exactness gives the desired module. This proves essential surjectivity and the equivalence. In particular all regular integral $\mathfrak{sl}_2$ blocks have this same algebraic description.

## 8. The Kazhdan–Lusztig theorem: one exact convention

For the Hecke algebra calculations in Sections 8.1–8.6, let \(v\) be an indeterminate and put \(A=\mathbb Z[v,v^{-1}]\), \(q=v^2\) and \(a=v-v^{-1}\). Here \(A\) is the coefficient ring, not the enveloping algebra \(U(\mathfrak n^-)\) used earlier.

Let $s_i$ be the simple reflections and $\ell$ the Coxeter length. Bruhat order is the subword order: $x\leq y$ if a reduced word for $x$ is obtained by selecting a subword of a reduced word for $y$. It is different from the weight order used earlier.

The Hecke algebra is defined over $\mathbb Z[q^{1/2},q^{-1/2}]$ by generators $T_i$, the Weyl-group braid relations, and
\[
(T_i+1)(T_i-q)=0. \tag{8.1}
\]
For a reduced expression $w=s_{i_1}\cdots s_{i_k}$, write $T_w=T_{i_1}\cdots T_{i_k}$. These elements form its standard basis. The bar involution sends $q^{1/2}$ to $q^{-1/2}$ and $T_i$ to
\[
T_i^{-1}=q^{-1}(T_i+1-q).
\]
Thus $\overline{T_w}=T_{w^{-1}}^{-1}$, with the inverse reversing the order of factors.

**Theorem 8.1 (the canonical Hecke basis).** There are unique polynomials $P_{x,y}(q)\in\mathbb Z[q]$ such that
\[
P_{y,y}=1,\qquad P_{x,y}=0\text{ if }x\nleq y,
\qquad \deg P_{x,y}\leq\frac{\ell(y)-\ell(x)-1}{2}\text{ if }x<y,
\]
and the elements
\[
C'_y=q^{-\ell(y)/2}\sum_{x\leq y}P_{x,y}(q)T_x \tag{8.2}
\]
are bar invariant. These are the Kazhdan–Lusztig polynomials in the convention used here.

We now prove both the standard-basis assertion and Theorem 8.1 over the integral Laurent ring. [The root-system lesson](RT-LIE-08.md#section-7) proves exchange, the rank-two length calculation and the reduced-word theorem; the subword and coefficient arguments needed here are supplied below. Etingof’s *Representations of Lie Groups* gives the corresponding algebraic construction.

### 8.1. The standard basis

Let \(\mathcal H\) be the \(A\)-algebra with generators \(H_s\), \(s\in S\), the braid relations of \(W\), and
\[
H_s^2=1+aH_s. \tag{8.4}
\]
The change of generators \(T_s=vH_s\) preserves each braid relation because its two words have the same length, and makes the quadratic relation precisely
\[
(T_s+1)(T_s-q)=0.
\]

For a reduced word \(w=s_1\cdots s_k\), put
\[
H_w=H_{s_1}\cdots H_{s_k},\qquad
T_w=v^{\ell(w)}H_w.
\]
The word property proves independence of the chosen reduced word.

**Proposition 8.1 (standard basis).** The elements \(H_w\), equivalently \(T_w\), form an \(A\)-basis of \(\mathcal H\). Multiplication by a simple generator is
\[
H_sH_w=
\begin{cases}
H_{sw},&\ell(sw)=\ell(w)+1,\\
H_{sw}+aH_w,&\ell(sw)=\ell(w)-1.
\end{cases} \tag{8.5}
\]
The analogous right-hand formula holds. In the original normalization,
\[
T_sT_w=
\begin{cases}
T_{sw},&\ell(sw)=\ell(w)+1,\\
qT_{sw}+(q-1)T_w,&\ell(sw)=\ell(w)-1.
\end{cases} \tag{8.6}
\]

**Proof of spanning and the multiplication formulas.** In the increasing case, \(s\) followed by a reduced word for \(w\) is a reduced word for \(sw\). In the decreasing case put \(u=sw\). Then \(w=su\) and \(\ell(w)=1+\ell(u)\), so word independence and (8.4) give
\[
H_sH_w=H_s^2H_u=H_u+aH_w.
\]
This proves (8.5). Induction on the number of generators in an arbitrary algebra word now expresses it as an \(A\)-linear combination of the \(H_w\): prepend its first generator to the expansion of its shorter tail and use (8.5). The right formula follows in exactly the same way from \(w=us\). Multiplying by the relevant powers of \(v\) gives (8.6).

To prove independence, it remains to construct an action of this presentation on a free module. Let
\[
M=\bigoplus_{w\in W}A b_w.
\]
Define \(A\)-linear operators
\[
L_s b_w=b_{sw}+a\,d_s(w)b_w,\qquad
R_t b_w=b_{wt}+a\,e_t(w)b_w, \tag{8.7}
\]
where
\[
d_s(w)=
\begin{cases}1,&\ell(sw)<\ell(w),\\0,&\ell(sw)>\ell(w),\end{cases}
\qquad
e_t(w)=
\begin{cases}1,&\ell(wt)<\ell(w),\\0,&\ell(wt)>\ell(w).\end{cases}
\]
We establish every defining relation for the \(L_s\).

**The length square and left/right commutation.** For simple \(s,t\), suppose first that \(sw\ne wt\). The sign of \(w^{-1}\alpha_s\) determines \(d_s(w)\), and the sign of
\[
(wt)^{-1}\alpha_s=t\,w^{-1}\alpha_s
\]
determines \(d_s(wt)\). By RT-LIE-08 Lemma 4.1 a simple reflection \(t\) can change a root's sign only when that root is \(\pm\alpha_t\). That exceptional condition would imply
\[
s=s_{w\alpha_t}=wtw^{-1},
\]
hence \(sw=wt\), contrary to the assumption. Therefore
\[
d_s(wt)=d_s(w).
\]
The same argument applied to \(w\alpha_t\) and \(s\,w\alpha_t\) gives
\[
e_t(sw)=e_t(w). \tag{8.8}
\]
Expanding (8.7) gives
\[
\begin{aligned}
L_sR_t b_w={}&b_{swt}
+a\,d_s(wt)b_{wt}
+a\,e_t(w)b_{sw}
+a^2e_t(w)d_s(w)b_w,\\
R_tL_s b_w={}&b_{swt}
+a\,e_t(sw)b_{sw}
+a\,d_s(w)b_{wt}
+a^2d_s(w)e_t(w)b_w.
\end{aligned}
\]
Equations (8.8) make the two expressions equal.

If \(sw=wt=:u\), both length changes agree and \(swt=w\). When \(\ell(u)=\ell(w)+1\), both compositions give
\[
b_w+ab_u.
\]
When \(\ell(u)=\ell(w)-1\), both give
\[
(1+a^2)b_w+ab_u.
\]
These cover the exceptional case as well. Thus
\[
L_sR_t=R_tL_s \quad\hbox{for all simple }s,t. \tag{8.9}
\]
This proves, rather than leaves as an exercise, the commutation check.

**Quadratic relations.** If \(\ell(sw)>\ell(w)\), the pair \(b_w,b_{sw}\) has
\[
L_s b_w=b_{sw},\qquad L_s b_{sw}=b_w+ab_{sw}.
\]
Consequently \(L_s^2=1+aL_s\) on both vectors. Every pair \(\{w,sw\}\) has exactly one shorter element, so the quadratic relation holds throughout \(M\).

**Rank-two braid relations.** Fix distinct \(s,t\), and let \(m=m_{st}\). Let \(B\) be the difference between the two alternating products of \(L_s,L_t\) of length \(m\). Both alternating group words are reduced and represent the rank-two longest element \(w_{st}\), by the proved rank-two calculation and ambient-length agreement in RT-LIE-08. Every suffix of either reduced word is reduced. Therefore applying either operator product to \(b_1\) encounters only increasing steps and gives \(b_{w_{st}}\). Hence
\[
B b_1=0. \tag{8.10}
\]
This is the actual rank-two operator check, for all four Weyl possibilities \(m=2,3,4,6\).

By (8.9), \(B\) commutes with every \(R_r\). If \(w=r_1\cdots r_k\) is reduced, every prefix is reduced; applying \(R_{r_1}\) first, then \(R_{r_2}\), and so on sends \(b_1\) to \(b_w\). It follows that
\[
B b_w=0
\]
for every \(w\). Thus the braid relation holds as an operator identity on the entire module, rather than only on its identity vector. This argument uses no unproved Hecke relation for the right operators: they are explicitly defined free-algebra operators, whose individual commutation with the left operators has already been checked.

The \(L_s\) therefore define a representation of \(\mathcal H\). For any reduced \(w\), its operator \(H_w\) sends \(b_1\) to \(b_w\). Applying a proposed relation
\[
\sum_w c_w H_w=0,\qquad c_w\in A,
\]
to \(b_1\) gives \(\sum_w c_w b_w=0\). The latter vectors are a free \(A\)-basis, so every \(c_w\) is zero. This proves independence and completes Proposition 8.1. \(\square\)

### 8.2. The subword order needed for triangularity

A reduced subword means a selection of positions in a word, retaining their order, whose selected letters form a reduced expression. Define \(x\le w\) if a reduced expression of \(x\) is a reduced subword of some reduced expression of \(w\).

**Lemma 8.1.** This condition is independent of the chosen reduced expression of \(w\). It defines a partial order. Moreover, every basis element occurring in an arbitrary product \(H_{s_1}\cdots H_{s_k}\) has a reduced expression that is a subword of the literal word \(s_1\cdots s_k\).

**Proof of reduced-expression independence.** The word property reduces the question to one braid move. Let an alternating rank-two block of length \(m\) be replaced by the other alternating block.

A reduced subword of the whole word has a selected subword inside this block. That selected block is itself reduced: otherwise replacing it by a shorter expression would shorten the whole selected expression. Its element \(v\) belongs to \(W_{\{s,t\}}\); rank-two and ambient length agree.

Every rank-two element has a reduced expression that occurs as a subword of either alternating length-\(m\) block. Indeed, length zero is the empty subword, length \(m\) is the common longest element, and a reduced alternating word of length \(j<m\) begins with one of the two letters. It occurs either in positions \(1,\ldots,j\) or in positions \(2,\ldots,j+1\) of either block. Replace the selected part by that expression in the new block. Its value and length are unchanged, so the entire selected word still represents \(x\) and is reduced. Reversing the braid move proves the converse. A sequence of braid moves proves independence.

Reflexivity is immediate. For transitivity, suppose \(x\le y\le w\), and choose a reduced word of \(w\) containing a reduced subword \(Y\) for \(y\). By the independence just proved, a reduced word for \(x\) can be selected from this particular \(Y\), hence from the chosen word of \(w\). Finally \(x\le w\) gives \(\ell(x)\le\ell(w)\); equality forces selection of every position, hence \(x=w\). This proves antisymmetry.

For the product assertion, induct on \(k\), using right multiplication in (8.5). Suppose a current basis element \(H_x\) has a reduced expression selected from the first \(k-1\) positions. If \(\ell(xs_k)=\ell(x)+1\), append the final position to obtain a reduced expression of \(xs_k\). If \(\ell(xs_k)=\ell(x)-1\), strong exchange applied to that reduced expression of \(x\) deletes one of its letters and gives a reduced expression of \(xs_k\). Both terms \(H_{xs_k}\) and \(aH_x\) in the decreasing multiplication formula therefore have the required selected expressions. This finishes the induction. \(\square\)

This proves all subword facts used below. A saturated-chain characterization or a separate lifting theorem for Bruhat order is not required.

### 8.3. The bar involution and its coefficient bounds

Equation (8.4) makes \(H_s\) invertible:
\[
H_s^{-1}=H_s-a.
\]
There is a semilinear algebra involution defined by
\[
\overline v=v^{-1},\qquad \overline{H_s}=H_s-a. \tag{8.11}
\]
To check well-definedness, note that
\[
(H_s-a)^2=1-a(H_s-a),
\]
which is the transformed quadratic relation because \(\overline a=-a\). The inverses satisfy the braid relations: invert either braid equality and reverse the alternating words; the two reversed words are again the two alternating words of the same length, possibly interchanged. Applying the proposed map twice fixes both \(v\) and every \(H_s\), so it is an involution.

For reduced \(w=s_1\cdots s_n\),
\[
\overline{H_w}=(H_{s_1}-a)\cdots(H_{s_n}-a)
=H_w+\sum_{x<w}r_{x,w}H_x. \tag{8.12}
\]
The full selection contributes \(H_w\). Every other selection has fewer than \(n\) letters. Lemma 8.1 shows that its basis support consists of reduced subwords of the chosen word for \(w\), and no such term can have length \(n\). This proves (8.12), including its exact Bruhat support.

For an integer \(d\ge0\), write
\[
A_d=\left\{\sum_{j=-d}^{d}n_jv^j:
n_j\in\mathbb Z,\ n_j=0\text{ unless }j\equiv d\pmod2\right\}.
\]
Then
\[
A_d A_e\subseteq A_{d+e},\qquad
A_{d-2}\subseteq A_d\quad(d\ge2),\qquad a\in A_1. \tag{8.13}
\]

**Lemma 8.2.** If \(x\le w\), then
\[
r_{x,w}\in A_{\ell(w)-\ell(x)}, \tag{8.14}
\]
where \(r_{w,w}=1\) and absent coefficients are zero.

**Proof.** Induct on \(n=\ell(w)\). The identity case is immediate. Write \(w=su\) reduced, so \(\ell(u)=n-1\). Multiplication gives
\[
(H_s-a)H_y=
\begin{cases}
H_{sy}-aH_y,&\ell(sy)>\ell(y),\\
H_{sy},&\ell(sy)<\ell(y).
\end{cases}
\]
Comparing coefficients in \(\overline{H_w}=(H_s-a)\overline{H_u}\) yields
\[
r_{x,w}=
\begin{cases}
r_{sx,u}-a r_{x,u},&\ell(sx)>\ell(x),\\
r_{sx,u},&\ell(sx)<\ell(x).
\end{cases} \tag{8.15}
\]
Put \(d=n-\ell(x)\). In the decreasing case the induction bound on \(r_{sx,u}\) is exactly \(A_d\). In the increasing case its bound is \(A_{d-2}\), and the bound on \(a r_{x,u}\) is \(A_d\). If \(d<2\), the first coefficient vanishes because \(\ell(sx)>\ell(u)\); otherwise use (8.13). These observations prove (8.14). The support condition needed when a coefficient is absent has already been proved in (8.12), so no unproved Bruhat lifting rule is being used in this recurrence. \(\square\)

### 8.4. Integral triangular construction of the canonical basis

**Proposition 8.2 (canonical Hecke basis).** For every \(w\in W\), there is a unique element
\[
C'_w=H_w+\sum_{x<w}c_{x,w}H_x,\qquad
c_{x,w}\in v^{-1}\mathbb Z[v^{-1}], \tag{8.16}
\]
such that \(\overline{C'_w}=C'_w\). In addition, if \(d=\ell(w)-\ell(x)>0\), every exponent occurring in \(c_{x,w}\) lies between \(-d\) and \(-1\) and has parity \(d\). Consequently
\[
P_{x,w}(q):=v^d c_{x,w}\in\mathbb Z[v^2]=\mathbb Z[q],
\qquad
\deg P_{x,w}\le\left\lfloor\frac{d-1}{2}\right\rfloor, \tag{8.17}
\]
with \(P_{w,w}=1\) and \(P_{x,w}=0\) for \(x\nleq w\). The \(C'_w\) form an \(A\)-basis.

**Proof.** We construct the elements by induction on \(\ell(w)\), while proving the additional exponent and parity bounds. The identity element is \(C'_1=1\).

Fix \(w\), assume the theorem for all shorter elements, and start with \(F=H_w\). During the construction maintain
\[
F=H_w+\sum_{y<w}b_yH_y,
\]
where each \(b_y\) has only negative exponents, all at least
\(-(\ell(w)-\ell(y))\), and parity \(\ell(w)-\ell(y)\). Zero coefficients satisfy this condition.

By (8.12), the defect
\[
D=\overline F-F=\sum_{y<w}d_yH_y
\]
is supported in the strict lower Bruhat interval of \(w\). If it is zero, construction is finished. Otherwise choose a maximal element \(x\) of its nonzero support. Since \(\overline D=-D\), unitriangularity of bar and maximality of \(x\) imply
\[
\overline{d_x}=-d_x. \tag{8.18}
\]
Indeed, no coefficient at a strictly larger supported element can contribute to \(H_x\) after applying bar.

An integral Laurent polynomial \(d\) with \(\overline d=-d\) has zero constant term and paired opposite coefficients:
\[
d=\sum_{k>0}m_k(v^k-v^{-k}),\qquad m_k\in\mathbb Z.
\]
No division by two is involved: comparison at exponent zero gives \(2d_0=0\) in \(\mathbb Z\), hence \(d_0=0\). Let \(p\) be the negative-exponent part of \(d_x\). Then
\[
p\in v^{-1}\mathbb Z[v^{-1}],\qquad
\overline p-p=-d_x. \tag{8.19}
\]
Replace
\[
F\longmapsto F+pC'_x. \tag{8.20}
\]
The element \(C'_x\) exists by induction and is bar invariant, so the new defect is \(D-d_xC'_x\). Its coefficient at \(H_x\) is zero, and its only newly changed coefficients are indexed by elements strictly below \(x\).

The process terminates. For example, first choose a nonzero defect index of largest length. The correction changes only shorter indices. The number of nonzero indices at that length strictly decreases, and after they vanish the maximum remaining length decreases. There are only finitely many elements of \(W\). The final \(F\) is therefore bar invariant.

It remains to verify the exponent bounds throughout this process. By the induction-maintained bounds on \(b_y\), Lemma 8.2 gives, for each \(z<w\), the defect coefficient
\[
d_z=r_{z,w}+\sum_{\substack{y<w\\ z\le y}}\overline{b_y}\,r_{z,y}-b_z. \tag{8.21}
\]
Every term on the right has exponents between
\(-(\ell(w)-\ell(z))\) and \(+(\ell(w)-\ell(z))\), and parity \(\ell(w)-\ell(z)\). To see this for a product term, add the bounds
\[
\ell(w)-\ell(y)\quad\hbox{and}\quad
\ell(y)-\ell(z);
\]
their sum is \(\ell(w)-\ell(z)\), and their parities add in the same way. Thus \(d_x\in A_{\ell(w)-\ell(x)}\). Its negative part \(p\) has exactly the required negative exponent range and parity for index \(x\).

For an index \(z<x\), the added coefficient in (8.20) is \(p c_{z,x}\). Both factors have negative exponents; their sum is negative and at least
\[
-(\ell(w)-\ell(x))-(\ell(x)-\ell(z))
=-(\ell(w)-\ell(z)).
\]
Their parities also add to \(\ell(w)-\ell(z)\). The coefficient added at index \(x\) is \(p\) itself. Therefore (8.20) preserves every maintained bound. The final element satisfies (8.16) and the asserted exponent and parity estimates.

For uniqueness, suppose two elements satisfy (8.16) and bar invariance. Their difference has strictly lower support, with coefficients in \(v^{-1}\mathbb Z[v^{-1}]\). At a maximal nonzero support index \(x\), unitriangularity makes its coefficient \(c\) satisfy \(\overline c=c\). A Laurent polynomial with only strictly negative exponents cannot be bar invariant unless it is zero. This contradicts the choice of \(x\), proving uniqueness.

Multiplying a coefficient \(c_{x,w}\) by \(v^d\) converts its exponent range to \(0,\ldots,d-1\) and makes every exponent even. This proves (8.17), including integrality and the exact degree bound. Finally (8.16) is a finite unitriangular change of basis when \(W\) is ordered compatibly with Bruhat order. Its inverse is obtained by successive subtraction with integral Laurent coefficients. Hence the \(C'_w\) form an \(A\)-basis. \(\square\)

Returning to \(T_x=v^{\ell(x)}H_x\), equation (8.16) becomes
\[
C'_w=v^{-\ell(w)}
\sum_{x\le w}P_{x,w}(v^2)T_x.
\]
This is exactly equation (8.2), including its normalization. Conversely, polynomials satisfying the stated support and degree conditions produce negative-power coefficients in (8.16), so the uniqueness just proved is exactly uniqueness of the polynomials in Theorem 8.1.

### 8.5. Algebraic inversion of the KL polynomial matrix

#### 8.5.1. Statement and normalization

Let \(W\) be the finite Weyl group of a finite reduced crystallographic root system, with simple reflections \(S\), length \(\ell\), reduced-subword Bruhat order and longest element \(w_0\). Reducibility and arbitrary rank are allowed. Put \(N=\ell(w_0)\),

\[
A=\mathbb Z[v,v^{-1}],\qquad q=v^2,\qquad a=v-v^{-1}.
\]

Retain the Hecke algebra normalization of Sections 8.1–8.4:

\[
H_s^2=1+aH_s,\qquad T_w=v^{\ell(w)}H_w,
\qquad \overline v=v^{-1},\quad \overline{H_s}=H_s-a.
\tag{8.22}
\]

The proved canonical basis is

\[
C'_y=\sum_x c_{x,y}H_x,
\qquad c_{x,y}=v^{\ell(x)-\ell(y)}P_{x,y}(v^2),
\tag{8.23}
\]

where \(c_{y,y}=1\), \(c_{x,y}=0\) unless \(x\leq y\), every strict-lower coefficient belongs to \(v^{-1}\mathbb Z[v^{-1}]\), and \(\overline{C'_y}=C'_y\). The standard basis, multiplication formulas, bar triangularity and canonical uniqueness were proved in Sections 8.1–8.4. RT-LIE-08 §§4–5 prove \(\ell(w)=N(w)\), inverse-length invariance, and \(w_0\Phi^+=\Phi^-\), \(w_0^2=1\). Its §7 proves reduced-word independence. No inversion formula is taken as an input.

**Theorem 8.3 (finite KL inversion).** The polynomials of Theorem 8.1 satisfy

\[
\boxed{\displaystyle
\sum_{x\leq z\leq y}(-1)^{\ell(z)-\ell(x)}
 P_{x,z}(q)P_{w_0y,w_0z}(q)=\delta_{x,y}.}
\tag{8.24}
\]

It holds over \(\mathbb Z[q]\), before evaluation at 1.

#### 8.5.2. Longest-element and order facts, with proofs

For every \(w\in W\),

\[
\ell(w_0w)=\ell(ww_0)=N-\ell(w).
\tag{8.25}
\]

Indeed, \(w_0\) reverses the sign of every root, so among the positive roots the inversions of \(w_0w\) are exactly the noninversions of \(w\). The already proved root-count formula gives the first equality. Apply inverse-length invariance to get the second.

Set \(\theta(w)=w_0ww_0\). The roots \(-w_0\alpha_i\) are simple: if one were a sum of two positive roots, applying \(-w_0\) would decompose \(\alpha_i\) into positive roots. Involutivity makes this a permutation of the simple roots. Consequently \(\theta\) permutes \(S\), preserves length and reduced-subword order, and is an involution.

Inversion preserves Bruhat order, because reversing a reduced word and its selected reduced subword gives reduced words of the inverses. Left multiplication by \(w_0\) reverses Bruhat order. Here is a proof from the available subword theorem, without importing a lifting theorem.

If \(x\leq y\) and \(sy<y\), choose a reduced word \(y=sU\). A selected reduced word for \(x\) can be taken inside this particular word. If \(sx>x\), the selected word cannot use its first letter, since such a reduced word would start with \(s\). Therefore \(x\leq sy\). If \(sx<x\), either the selection starts with the first letter, in which case deleting it proves \(sx\leq sy\), or it omits that letter, in which case \(sx\leq x\leq sy\). We have proved

\[
sy<y:\quad
\begin{cases}
sx>x\Longrightarrow x\leq sy,\\
sx<x\Longrightarrow sx\leq sy.
\end{cases}
\tag{8.26}
\]

Induct on \(\ell(y)\) to show \(w_0y\leq w_0x\) when \(x\leq y\). The identity case is immediate. For \(y\ne1\), choose \(s\) with \(sy<y\), and put \(t=\theta(s)\). If \(sx>x\), (8.26) and induction give \(w_0sy\leq w_0x\); (8.25) gives \(w_0y=t(w_0sy)<w_0sy\), proving the claim. If \(sx<x\), (8.26) and induction give \(w_0sy\leq w_0sx\). Left multiplication by \(t\) shortens both these elements by (8.25). The second case of (8.26), now applied to this pair, gives
\(t(w_0sy)\leq t(w_0sx)\), namely \(w_0y\leq w_0x\). This finishes the induction. Involutivity gives the converse. Inversion then gives the right-multiplication version:

\[
x\leq y\quad\Longleftrightarrow\quad
w_0y\leq w_0x\quad\Longleftrightarrow\quad yw_0\leq xw_0.
\tag{8.27}
\]

Thus \(b(y)=y^{-1}w_0\) is a bijection with
\(\ell(b(y))=N-\ell(y)\) and \(b(z)\leq b(y)\) exactly when \(y\leq z\).

#### 8.5.3. Trace, longest coefficient and Hecke symmetries

The map \(*\) that fixes \(A\) and each \(H_s\), and reverses products, is an anti-involution: reversing either braid relation preserves it, and each quadratic relation is fixed. Hence \(H_w^*=H_{w^{-1}}\).

Define \(\tau(h)\) to be the coefficient of \(H_1\) in \(h\). To prove its orthogonality and trace properties, give the free module with basis \(H_w\) the bilinear form
\((H_x,H_y)_0=\delta_{x,y}\). Left multiplication by \(H_s\) is self-adjoint for this form: on every pair \(\{w,sw\}\), with \(w\) the shorter element, its matrix is

\[
\begin{pmatrix}0&1\\1&a\end{pmatrix}.
\]

Taking the adjoint of the product for a reduced word gives

\[
\delta_{x,y}=(H_x,H_y)_0
 =(1,H_{x^{-1}}H_y)_0=\tau(H_{x^{-1}}H_y).
\]

Replace \(x,y\) by their inverses to obtain

\[
\tau(H_xH_{y^{-1}})=\delta_{x,y},
\qquad \tau(H_xH_y)=\delta_{x,y^{-1}}.
\tag{8.28}
\]

The latter expression is symmetric in \(x,y\). Bilinearity proves \(\tau(hk)=\tau(kh)\) for all \(h,k\). Thus \(\tau\) is a trace, and its pairing is nondegenerate over \(A\).

Let \(\lambda(h)\) be the coefficient of \(H_{w_0}\). Equation (8.28) gives

\[
\lambda(h)=\tau(hH_{w_0}).
\tag{8.29}
\]

This functional need not itself be a trace. Its relation with the longest element is explicit. The multiplication formulas and \(w_0s=\theta(s)w_0\) give

\[
H_{w_0}H_s=H_{w_0s}+aH_{w_0}
 =H_{\theta(s)}H_{w_0}.
\]

Consequently conjugation by the invertible \(H_{w_0}\) is the algebra automorphism \(\Theta(H_s)=H_{\theta(s)}\). In particular
\(H_{w_0}h=\Theta(h)H_{w_0}\). Together with the trace property, this proves the twisted trace relation

\[
\lambda(hk)=\lambda(k\Theta(h)).
\tag{8.30}
\]

The product order used below is always \(hk\); no symmetry of \(\lambda(hk)\) is assumed.

Bar is unitriangular in the \(H\)-basis and strictly lowers length away from its leading term. Since \(w_0\) is the unique element of maximum length,

\[
\lambda(\overline h)=\overline{\lambda(h)},
\qquad
\lambda(\overline h\,\overline k)=\overline{\lambda(hk)}.
\tag{8.31}
\]

Thus the longest-coefficient product pairing is compatible with bar.

We also need the \(A\)-linear involutive algebra automorphism

\[
\iota(H_s)=-H_s^{-1}=a-H_s.
\tag{8.32}
\]

Its image has square \(1+a(a-H_s)\), so it obeys the same quadratic relation. The inverses obey braid relations by reversing the inverses of the original braid words, and the common sign \((-1)^m\) preserves a length-\(m\) braid relation. Applying \(\iota\) twice fixes the generators. It commutes with bar: on each generator both composites equal \(-H_s\), and the scalar actions commute. Therefore

\[
\iota(H_w)=(-1)^{\ell(w)}\overline{H_w},
\qquad \overline{\iota(C'_w)}=\iota(C'_w).
\tag{8.33}
\]

Finally \(*\) and \(\Theta\) commute with bar, preserve the prescribed leading term and negative-power triangularity of a canonical element, and respectively carry the index to \(w^{-1}\) and \(\theta(w)\). Canonical uniqueness proves

\[
(C'_w)^*=C'_{w^{-1}},\qquad \Theta(C'_w)=C'_{\theta(w)},
\]

and, coefficient by coefficient using length preservation,

\[
P_{x,y}=P_{x^{-1},y^{-1}}=P_{\theta(x),\theta(y)}.
\tag{8.34}
\]

#### 8.5.4. The dual canonical basis

Put \(B_y=\overline{H_{b(y)}}\), where \(b(y)=y^{-1}w_0\). These form an \(A\)-basis. The length complement gives the reduced factorization
\(H_yH_{b(y)}=H_{w_0}\). Applying bar and using
\(\overline{H_y}^{-1}=H_{y^{-1}}\) and
\(\overline{H_{w_0}}=H_{w_0}^{-1}\), we get

\[
B_y=H_{y^{-1}}H_{w_0}^{-1}.
\]

Equation (8.29) now gives the exact complementary standard-basis pairing

\[
\lambda(H_xB_y)
 =\tau(H_xH_{y^{-1}}H_{w_0}^{-1}H_{w_0})
 =\delta_{x,y}.
\tag{8.35}
\]

Define

\[
D_y=(-1)^{\ell(b(y))}\iota(C'_{b(y)}).
\tag{8.36}
\]

It is bar invariant by (8.33). Expanding (8.23), and then using the complementary index \(u=b(z)\), yields

\[
\begin{aligned}
D_y
 &=\sum_{z\geq y}d_{z,y}B_z,\\
d_{z,y}
 &=(-1)^{\ell(z)-\ell(y)}c_{b(z),b(y)},
\qquad d_{y,y}=1.
\end{aligned}
\tag{8.37}
\]

The support follows from (8.27), and every coefficient with \(z>y\) belongs to \(v^{-1}\mathbb Z[v^{-1}]\). The sign is correct because
\(\ell(b(z))-\ell(b(y))=\ell(y)-\ell(z)\), whose parity is that of \(\ell(z)-\ell(y)\).

Using (8.35), the triangular expansions of \(C'_x\) and \(D_y\) show

\[
\lambda(C'_xD_y)-\delta_{x,y}
 \in v^{-1}\mathbb Z[v^{-1}].
\]

Indeed, the leading-leading pairing contributes \(\delta_{x,y}\), and every other nonzero contribution contains at least one strict-lower coefficient of \(C'_x\) or one strict-upper coefficient of \(D_y\). Each such coefficient has only negative powers, and products of two such coefficients still have only negative powers. Finitely many terms are involved. On the other hand (8.31) makes this difference bar invariant, since both elements are bar invariant. A Laurent polynomial with only strictly negative powers that is invariant under \(v\mapsto v^{-1}\) is zero. We have proved

\[
\boxed{\lambda(C'_xD_y)=\delta_{x,y}.}
\tag{8.38}
\]

This is the required duality argument. It assumes neither KL inversion nor positivity of KL coefficients.

#### 8.5.5. Extracting the longest-element matrix relation

By (8.34),
\(P_{b(z),b(y)}=P_{w_0z,w_0y}\). Combining this with (8.23), (8.25) and (8.37) gives

\[
d_{z,y}=(-1)^{\ell(z)-\ell(y)}
 v^{\ell(y)-\ell(z)}P_{w_0z,w_0y}(v^2).
\]

Substitute this and the coefficient of \(H_z\) in \(C'_x\) into (8.38):

\[
v^{\ell(y)-\ell(x)}
\sum_{y\leq z\leq x}(-1)^{\ell(z)-\ell(y)}
 P_{z,x}(q)P_{w_0z,w_0y}(q)=\delta_{x,y}.
\tag{8.39}
\]

Order the finite set \(W\) compatibly with Bruhat order. Define matrices

\[
\mathsf P_{x,y}=P_{x,y}(q),\qquad
\mathsf E_{x,y}=(-1)^{\ell(x)}\delta_{x,y},\qquad
\mathsf R_{x,y}=\delta_{x,w_0y}.
\]

Then \(\mathsf E^2=\mathsf R^2=1\),
\(\mathsf E\mathsf R=(-1)^N\mathsf R\mathsf E\), and

\[
\mathsf K=\mathsf E\mathsf P\mathsf E,
\qquad
\mathsf Q=\mathsf R\mathsf P^{\mathsf t}\mathsf R,
\qquad
\mathsf Q_{x,y}=P_{w_0y,w_0x}(q).
\tag{8.40}
\]

Both \(\mathsf K\) and \(\mathsf Q\) are upper unitriangular, by (8.27). With the indices in (8.39) renamed to \(a\leq b\), its sum differs from \((\mathsf Q\mathsf K)_{a,b}\) by the unit
\((-1)^{\ell(b)-\ell(a)}v^{\ell(a)-\ell(b)}\). For \(a=b\) that unit is 1, and for \(a\ne b\) the right side is zero. Thus

\[
\mathsf Q\mathsf K=1.
\]

No field extension or determinant division is needed to reverse this product. Since \(\mathsf K=1+\mathsf U\) with \(\mathsf U\) strictly upper triangular in a finite matrix, \(\mathsf U^{|W|}=0\), and
\(\mathsf K^{-1}=\sum_{j=0}^{|W|-1}(-\mathsf U)^j\) is a two-sided inverse over \(\mathbb Z[q]\). Hence \(\mathsf Q=\mathsf K^{-1}\) and \(\mathsf K\mathsf Q=1\). Its \((x,y)\) entry is exactly (8.24). Equivalently, the explicit longest-element matrix relation is

\[
\boxed{\mathsf K^{-1}=\mathsf R\mathsf P^{\mathsf t}\mathsf R,
\qquad
\mathsf P^{-1}=\mathsf E\mathsf R\mathsf P^{\mathsf t}\mathsf R\mathsf E.}
\tag{8.41}
\]

The opposition symmetry (8.34) finally proves the right-longest version:

\[
\boxed{Q_{x,y}(q):=(\mathsf K^{-1})_{x,y}
 =P_{w_0y,w_0x}(q)=P_{yw_0,xw_0}(q).}
\tag{8.42}
\]

Thus left and right multiplication are interchangeable **in this paired polynomial formula because opposition was proved**, not because \(w_0\) is central. It is generally not central. Rank zero gives the one-by-one identity; the proof otherwise makes no rank, root-length or irreducibility restriction.

### 8.6. The geometric multiplicity theorem

**Theorem 8.2 (Kazhdan–Lusztig multiplicities).** In the principal central-character block, with the **dominant** starting weight $0$ and the positive-root Borel fixed above,
\[
\boxed{[M(w\mathbin{\cdot}0):L(y\mathbin{\cdot}0)]
=P_{w,y}(1).} \tag{8.3}
\]
The polynomials in (8.2) have nonnegative coefficients. Formula (8.3) is zero when $w\nleq y$. More generally the same formula holds with any dominant integral starting weight $\lambda$ in place of $0$; then $\lambda+\rho$ is regular.

This is Etingof's Theorem 21.6, with his first index denoting the Verma label and his second the simple label. The multiplicity formula is proved algebraically in Sections 8.12–8.15, culminating in Theorem 8.13. The coefficient positivity assertion is proved algebraically in Theorem 8.10. The multiplicity theorem was proved in 1981 by Beilinson–Bernstein and independently by Brylinski–Kashiwara.

For orientation, take a complex group $G$ with Lie algebra $\mathfrak g$. Its flag variety $G/B$ has Bruhat cells indexed by $W$. Localization relates suitable enveloping-algebra modules to modules over differential operators. The Riemann–Hilbert correspondence then connects regular holonomic modules to constructible complexes, and simple objects are governed by intersection cohomology of Schubert closures. These links explain why Weyl-group polynomials can determine the multiplicities of infinite-dimensional representations. This paragraph describes the proof's ingredients; it does not assert a localization equivalence for all of $\mathcal O$. Brylinski–Kashiwara's §8, Theorem 8.1, gives the intersection-cohomology character statement. This geometric route requires proofs at the stated all-ranks flag-variety scope; rank-one localization or a formal perverse-sheaf construction alone does not supply the general theorem.

The starting weight and polynomial normalization cannot be changed independently. In rank one, (8.2) gives
\[
C'_s=q^{-1/2}(1+T_s),\qquad P_{1,s}=1.
\]
Consequently (8.3) gives $[M(0):L(-2)]=1$ and $[M(-2):L(0)]=0$, exactly as (7.3). This also identifies which direction of Bruhat order belongs in the formula.

#### 8.6.1. Exact inputs for the geometric deductions

The following proofs make the formal mechanisms precise. Each result states its geometric hypotheses explicitly. They do not supply the missing general geometric inputs or constitute a proof of Theorem 8.2.

Let \(W\) be a finite Weyl group, \(d_x=\ell(x)\), \(A=\mathbb Z[v,v^{-1}]\), and \(q=v^2\). Use exactly the lesson's multiplication
\[
(T_s+1)(T_s-q)=0,\qquad
H_x=v^{-d_x}T_x,\qquad
\overline v=v^{-1},\qquad
\overline{T_x}=T_{x^{-1}}^{-1}.
\tag{8.43}
\]
Thus \(\overline{H_s}=H_s-(v-v^{-1})\). The bar map is an algebra involution with semilinear coefficients. It is not the map that merely fixes each \(T_x\).

Suppose \(X\) is an ordinary finite flag variety with a finite stratification
\[
X=\coprod_{x\in W} C_x,\qquad
C_x\simeq\mathbb A^{d_x},\qquad
\overline{C_y}=\coprod_{x\le y}C_x,
\]
and write \(j_x:C_x\hookrightarrow X\). These geometric assertions, including flag existence at the stated root-system scope, are hypotheses of the conditional deductions below.

**G0: mixed coefficient and recollement data.** Assume a constructible bounded derived category \(\mathscr D(X)\) with the ordinary cohomological convention
\[
H^r(K[m])=H^{r+m}(K),
\]
cell restrictions that are bounded complexes of constant mixed coefficient objects, extension by zero \(j_{x!}\), restriction \(j_x^*\), and the usual closed/open distinguished triangles. Assume a contravariant exact Verdier duality \(\mathbb D\). The coefficient category has finite-dimensional underlying vector spaces, finite integer weight filtrations, exact weight-graded dimension, coefficient duals and exact tensor products satisfying
\[
\operatorname{wtchar}(V)
=\sum_a\dim\operatorname{Gr}^W_a(V)\,v^a,\quad
\operatorname{wtchar}(V^\vee)=\overline{\operatorname{wtchar}(V)},\quad
\operatorname{wtchar}(V\otimes U)
=\operatorname{wtchar}(V)\operatorname{wtchar}(U).
\tag{8.44}
\]
The unit \(\mathbf 1\) has weight zero. The Tate twist \((1)\) lowers weights by two, so its character is \(v^{-2}\). Geometric duality commutes with coefficient duals, specifically
\(\mathbb D(K\otimes V)=(\mathbb DK)\otimes V^\vee\)
for constant coefficients, and
\(\mathbb D(K(n))=(\mathbb DK)(-n)\).

Exactness of weight-graded dimension means that a short exact sequence of coefficients has additive weight character. In a mixed-Hodge realization this uses strictness of the weight filtration. In a mixed Weil realization it requires the corresponding actual weight-category structure. Neither mixed framework is constructed in this lesson.

Put
\[
E_x=j_{x!}\mathbf 1_{C_x},
\]
without a shift or twist.

The complete dual-standard character is a consequence of the minimal-parabolic package proved in Section 8.6.2 below. It is not an additional IC-purity assumption.

**G2: mixed IC and the strict boundary bound.** Let \(I_y\) be the mixed intermediate-extension object with
\[
I_y|_{C_y}=\mathbf 1[d_y],\qquad
\mathbb D I_y\simeq I_y(d_y),
\]
supported on \(\overline{C_y}\), and put
\[
J_y=I_y[-d_y].
\tag{8.45}
\]
Assume for \(x<y\) the strict stalk bound
\[
H^r((J_y)_x)=0\quad\text{if }r\ge d_y-d_x.
\tag{8.46}
\]
Here a point of \(C_x\) is used to compute the constant cell restriction. The equivalent bound for \(I_y\) is vanishing in degrees \(i\ge-d_x\). The top restriction of \(J_y\) is the unit in degree zero; off the closure it is zero. Finiteness follows from G0.

The argument needs no separate lower stalk bound: the formal recognition argument below will also force vanishing in negative degrees.

**G3: pointwise purity in the unshifted normalization.** For every \(x,y,r\), require
\[
H^r((J_y)_x)\text{ is pure of weight }r.
\tag{8.47}
\]
Equivalently \(H^i((I_y)_x)\) is pure of weight \(i+d_y\). This is a statement about every stalk cohomology group. The weaker statement that \(I_y\) is pure as a complex is not a substitute for (8.47). No evenness or Tate decomposition of IC stalks is assumed here.

The IC recognition below is conditional on G0, G2, G3 and the minimal-parabolic package of Section 8.6.2. The ordinary Grothendieck relation additionally requires its stated perverse-heart hypothesis. These are explicit geometric prerequisites; the lesson does not claim to construct them at the general flag-variety scope.

#### 8.6.2. Full dual-standard character from rank-one parabolics

**Proposition 8.3 (dual-standard character, conditional on MP0–MP1).** Under the exact mixed-operation and minimal-parabolic hypotheses below, the character of every dual unshifted standard is the Hecke bar of its standard basis element.

Use the Hecke algebra already proved in Sections 8.1–8.4:

\[
(T_s+1)(T_s-q)=0,\qquad q=v^2,\qquad
\overline q=q^{-1},\qquad
\overline{T_s}=T_s^{-1}=q^{-1}T_s+(q^{-1}-1).
\tag{8.48}
\]

Bar is the semilinear algebra involution, so it preserves product order. For an ordinary full flag write \(C_x\) for the Bruhat cell of dimension \(d_x=\ell(x)\), \(j_x:C_x\hookrightarrow X\), and
\(E_x=j_{x!}\mathbf1_{C_x}\), without shifts or twists. Assume the following package.

**MP0, ordinary mixed operations.** On \(X\), its minimal partial flags, their cells, and the locally closed subspaces used below, there are bounded constructible mixed derived categories with \(f^*,f^!,f_*,f_!\), functorial composition, base change for \(!\), projection formula for constant coefficient objects, closed/open recollement, and ordinary Verdier duality. The coefficient unit is one-dimensional of weight zero and is self-dual on a point. All operations displayed below stay in the stated constructible categories and commute with cohomological shifts and Tate twists. Restrictions to cells are bounded complexes of constant mixed coefficient objects; their finite weight filtrations have exact graded dimensions. Coefficient tensor products are exact with multiplicative weight character, and geometric duality tensors constant coefficients with their coefficient duals. Coefficient duals and Tate twists obey

\[
\operatorname{wtchar}(V^\vee)=\overline{\operatorname{wtchar}(V)},
\qquad \operatorname{wtchar}(V(1))=v^{-2}\operatorname{wtchar}(V).
\tag{8.49}
\]

The ordinary cohomological convention is \(H^r(K[m])=H^{r+m}(K)\). Duality satisfies
\(\mathbb D f^*=f^!\mathbb D\),
\(\mathbb D f_*=f_!\mathbb D\).
For a proper \(f\), \(f_*=f_!\). For a smooth morphism of relative complex dimension one,
\(f^!=f^*2\). These are hypotheses about the constructed mixed formalism, including its twist normalization.

**MP1, minimal-parabolic cell geometry.** For each simple reflection \(s\), the projection
\(p_s:X\to Y_s=G/P_s\) is proper and smooth of relative dimension one. The Bruhat cells of \(Y_s\) are \(D_u\), indexed by the minimal representatives \(u\) of the right cosets \(W/\langle s\rangle\), equivalently \(us>u\). For each such \(u\),

\[
p_s^{-1}(D_u)=C_u\sqcup C_{us},\qquad
p_s|_{C_u}:C_u\xrightarrow{\sim}D_u,
\tag{8.50}
\]

where \(C_u\) is closed in \(p_s^{-1}(D_u)\), and \(C_{us}\) is its open complement. The restriction \(f_u:C_{us}\to D_u\) is a locally trivial affine-line bundle. It has the ordinary compact-support orientation comparison

\
(f_u)_!\mathbf1_{C_{us}}
\simeq\mathbf1_{D_u}[-2.
\tag{8.51}
\]

Equation (8.51) is only the relative affine-line calculation. For a product \(D_u\times\mathbb A^1\), it follows from
\(R\Gamma_c(\mathbb A^1,\mathbf1)=\mathbf1-2\), followed by product base change. A locally trivial bundle gives the same comparison by its relative trace; the transition maps preserve the complex orientation. Its validity in the selected mixed realization is included explicitly here. No parity, purity or decomposition theorem for IC is included.

The geometry in (8.50) is the two-cell rank-one geometry over each partial-flag cell. It can also be expressed by a trivialization with fiber \(P_s/B\simeq\mathbb P^1\): the lower cell selects one point of the fiber, and the upper cell is its affine-line complement. The proof below needs exactly (8.50) and (8.51), not a chosen global trivialization.

**Root-coordinate verification of the two-cell geometry.**

For clarity, MP1 can be verified from the usual algebraic-group Bruhat root-coordinate package, if that package has been constructed. This paragraph does not assert that the course has already constructed every finite-type group or quotient. Write \(B=TU\), let \(U^-\) be the opposite unipotent subgroup, and put
\[
U_u=U\cap\dot uU^-\dot u^{-1},\qquad
H_u=B\cap\dot uB\dot u^{-1}.
\]
The root-coordinate input is that multiplication \(U_u\times H_u\to B\) is an isomorphism of varieties, and \(U_u\to C_u\), \(a\mapsto a\dot uB\), is the resulting affine-cell parametrization. For \(us>u\), the root \(u\alpha_s\) is positive. The only root present in \(\operatorname{Lie}(P_s)\) but absent from \(\operatorname{Lie}(B)\) is \(-\alpha_s\); its image \(-u\alpha_s\) is negative. The root-subgroup description of these intersections therefore gives
\[
B\cap\dot uP_s\dot u^{-1}=H_u.
\]
Thus \(a\mapsto a\dot uP_s\) identifies \(U_u\) with \(D_u\). Its lift \(a\mapsto a\dot u\) gives an algebraic trivialization
\[
U_u\times(P_s/B)\xrightarrow{\sim}p_s^{-1}(D_u),
\qquad (a,pB)\longmapsto a\dot upB.
\tag{8.52}
\]
Uniqueness follows by projecting to \(D_u\); the inverse is regular because the affine-cell coordinate \(a\) is regular and then determines \(pB=\dot u^{-1}a^{-1}gB\). In the rank-one quotient \(P_s/B\), the point \(B/B\) is closed and its complement is \(U_{\alpha_s}\dot sB/B\simeq\mathbb A^1\). The latter maps to \(C_{us}\): conjugation sends \(U_{\alpha_s}\) to \(U_{u\alpha_s}\subset U\), and appending \(s\) to a reduced word for \(u\) appends exactly that root coordinate to the cell parametrization. Equivalently, the positive roots of \(U_{us}\) are those of \(U_u\) together with \(u\alpha_s\). This proves (8.50), and (8.52) makes (8.51) the product affine-line calculation on each base cell.

Finally, the ordinary group-quotient package identifies \(p_s\) as the associated \(P_s/B\simeq\mathbb P^1\) bundle of \(G\to G/P_s\); properness and smoothness of relative dimension one descend from that fiber. These arguments use rank-one group geometry and Bruhat root coordinates, not IC geometry. They do not erase the need to construct those group quotients and root-coordinate facts at the requested finite-root-system scope.

**Character, Grothendieck classes and wall crossing.**

For a complex \(K\) put

\[
e_z(K)=\sum_{r,a}(-1)^r
\dim\operatorname{Gr}^W_a H^r(K_z)\,v^a,
\qquad \operatorname{ch}(K)=\sum_z e_z(K)T_z.
\tag{8.53}
\]

Here \(K_z\) is the coefficient complex at any point of \(C_z\), whose mixed constancy is part of MP0. Long exact cohomology sequences and exact weight-graded dimensions make this character additive on distinguished triangles. Reindexing gives

\
\operatorname{ch}(K[m)=(-1)^m v^{-2n}\operatorname{ch}(K),
\qquad \operatorname{ch}(E_z\otimes V)=\operatorname{wtchar}(V)T_z.
\tag{8.54}
\]

The derived Grothendieck group is generated by \([E_z\otimes V]\). Indeed, filter the finite Bruhat stratification by closed lower sets. Recollement writes the class at each step as the class on the preceding closed union plus the extension by zero of the coefficient complex on the new cell. Ordinary truncation expresses that coefficient complex as the finite alternating sum of its cohomology coefficients. This proves generation without requiring freeness over \(\mathbb Z[v,v^{-1}]\).

Define the unnormalized wall-crossing functor

\[
Q_s=p_s^*p_{s*}.
\tag{8.55}
\]

Fix \(u\) with \(us>u\), and write \(i_u:D_u\hookrightarrow Y_s\) and \(F_u=i_{u!}\mathbf1_{D_u}\). Since \(p_s\) is proper, functoriality of \(!\), (8.50) and (8.51) give actual derived comparisons

\
p_{s*}E_u=F_u,\qquad
p_{s*}E_{us}=F_u[-2.
\tag{8.56}
\]

For example, the second comparison follows by factoring \(p_sj_{us}=i_uf_u\):
\(p_{s*}j_{us!}\mathbf1=p_{s!}j_{us!}\mathbf1=i_{u!}(f_u)_!\mathbf1\).

Base change for \(!\) identifies \(p_s^*F_u\) with the extension by zero of the unit from \(Z_u=p_s^{-1}(D_u)\). The closed/open triangle for \(C_u\subset Z_u\), with open complement \(C_{us}\), therefore proves

\[
[Q_sE_u]=[E_u]+[E_{us}],\qquad
[Q_sE_{us}]=E_u[-2]+E_{us}[-2].
\tag{8.57}
\]

The shift in the second equation has positive Euler sign and the twist has character \(v^2=q\). Consequently

\[
\operatorname{ch}(Q_sE_u)=T_u+T_{us},\qquad
\operatorname{ch}(Q_sE_{us})=q(T_u+T_{us}).
\tag{8.58}
\]

These two formulas agree with right multiplication by \(T_s+1\): the proved standard Hecke multiplication gives

\[
T_u(T_s+1)=T_{us}+T_u,
\qquad T_{us}(T_s+1)=q(T_u+T_{us}).
\]

Projection formula gives the same character identities with any constant mixed coefficient \(V\) tensored in. Every cell index is exactly one member of such a pair. Grothendieck generation and additivity now prove, for every \(K\) in the category,

\[
\boxed{\operatorname{ch}(Q_sK)=\operatorname{ch}(K)(T_s+1).}
\tag{8.59}
\]

This step has not used compatibility of the character with duality; deriving that compatibility is the purpose of the next step.

**Duality recurrence and every boundary coefficient.**

Properness and smoothness of \(p_s\), in that order, give

\
\begin{aligned}
\mathbb D_XQ_sK
&\simeq p_s^!\mathbb D_{Y_s}p_{s*}K\\
&\simeq p_s^!p_{s*}\mathbb D_XK\\
&\simeq Q_s\mathbb D_XK[2.
\end{aligned}
\tag{8.60}
\]

It follows from the elementary shift/twist character rule and (8.59) that

\[
\operatorname{ch}(\mathbb DQ_sK)
=q^{-1}\operatorname{ch}(\mathbb DK)(T_s+1).
\tag{8.61}
\]

Now \(us>u\). The first equation of (8.57) implies
\([E_{us}]=[Q_sE_u]-[E_u]\).
Contravariant exact duality is additive on Grothendieck classes: it reverses a distinguished triangle, but the same sum relation results. Applying it and taking the character yields

\[
\begin{aligned}
\operatorname{ch}(\mathbb DE_{us})
&=\operatorname{ch}(\mathbb DQ_sE_u)-\operatorname{ch}(\mathbb DE_u)\\
&=\operatorname{ch}(\mathbb DE_u)
\bigl(q^{-1}(T_s+1)-1\bigr)\\
&=\operatorname{ch}(\mathbb DE_u)\overline{T_s}.
\end{aligned}
\tag{8.62}
\]

The identity cell is a closed point, so \(\mathbb DE_1=E_1\) and its character is \(T_1=1\). For a reduced word \(w=s_1\cdots s_d\), every prefix increases length when its next letter is appended. Iterating (8.62) proves

\[
\boxed{\operatorname{ch}(\mathbb DE_w)
=\overline{T_{s_1}}\cdots\overline{T_{s_d}}
=\overline{T_w}.}
\tag{8.63}
\]

In particular, the result includes the complete weighted boundary-stalk Euler character needed for IC recognition. It is not merely the smooth top-cell calculation. Reduced-word independence follows from equality with the already constructed Hecke bar.

For a completely explicit boundary recurrence, define \(B_{z,w}=[T_z]\operatorname{ch}(\mathbb DE_w)\), with \(B_{z,1}=\delta_{z,1}\). If \(ys>y\), the right-multiplication formula in (8.62) gives

\[
B_{z,ys}=
\begin{cases}
q^{-1}B_{zs,y},&zs<z,\\
B_{zs,y}+(q^{-1}-1)B_{z,y},&zs>z.
\end{cases}
\tag{8.64}
\]

Every coefficient on the left is consequently determined from a shorter standard, including the zero coefficients. For \(w=s\) it gives

\[
\operatorname{ch}(\mathbb DE_s)
=q^{-1}T_s+(q^{-1}-1)T_1.
\tag{8.65}
\]

The negative constant term at the boundary is an Euler-character contribution. It cannot be replaced by the top coefficient \(q^{-1}T_s\).

Equivalently, one may define ordinary \(R\)-polynomials by

\[
R_{z,1}=\delta_{z,1},\qquad
R_{z,ys}=
\begin{cases}
R_{zs,y},&zs<z,\\
qR_{zs,y}+(q-1)R_{z,y},&zs>z,
\end{cases}
\tag{8.66}
\]

for \(ys>y\), taking unsupported entries to be zero. Induction in (8.64), with the two possible changes of \(\ell(zs)\), proves

\[
B_{z,w}=q^{-\ell(w)}(-1)^{\ell(w)-\ell(z)}R_{z,w}(q).
\tag{8.67}
\]

Thus (8.63) also supplies the full normalized \(R\)-polynomial boundary expression. Its support is \(z\le w\), by the already proved Bruhat triangularity of Hecke bar. Here (8.66) is a computational description of coefficients already proved independent of a reduced expression; independence is not a new geometric assumption.

#### 8.6.3. The graded character and its duality

Define for \(K\in\mathscr D(X)\)
\[
e_x(K)=\sum_{r,a}(-1)^r
 \dim\operatorname{Gr}^W_a H^r((K)_x)\,v^a,
\qquad
\operatorname{ch}_{\mathcal H}(K)=\sum_x e_x(K)T_x.
\tag{8.68}
\]

**Lemma 8.3.** This character is additive on distinguished triangles, sends \(Km\) to
\((-1)^m v^{-2n}\operatorname{ch}_{\mathcal H}(K)\), and sends \(E_x\otimes V\) to \(\operatorname{wtchar}(V)T_x\).

**Proof.** Apply cell restriction to a distinguished triangle. Its finite long exact cohomology sequence has zero alternating weight character: split it into the short exact sequences of kernels and images, use G0's additivity, and cancel the image terms. This proves additivity. Reindexing the finite sum for \(K[m]\) gives the factor \((-1)^m\); the Tate rule gives \(v^{-2n}\). Extension by zero has stalk zero on all other cells, and on its own cell its stalk is the coefficient \(V\) in degree zero. This proves the last assertion. \(\square\)

**Lemma 8.4.** Every class in the derived Grothendieck group is a finite integer combination of classes \(E_x\otimes V\), with coefficient objects \(V\). Consequently the character is compatible with Verdier duality:
\[
\operatorname{ch}_{\mathcal H}(\mathbb DK)
=\overline{\operatorname{ch}_{\mathcal H}(K)}.
\tag{8.69}
\]

**Proof.** Choose a linear order of the cells compatible with the closure partial order. Successive unions in that order are closed: a lower set of cell indices is a union of their closures, hence closed. At each step apply the closed/open triangle. It writes the class of a complex as the sum of its extension-by-zero restriction to the new cell and the class on the preceding closed union. On the cell, ordinary truncation triangles express the bounded coefficient complex as the alternating sum of its finitely many cohomology coefficients. Induction proves the generation assertion. This does not require the mixed Grothendieck group itself to be free over \(\mathbb Z[v,v^{-1}]\).

For a generator \(E_x\otimes V\), duality and Proposition 8.3 give
\[
\begin{aligned}
\operatorname{ch}_{\mathcal H}(\mathbb D(E_x\otimes V))
&=\operatorname{wtchar}(V^\vee)
  \operatorname{ch}_{\mathcal H}(\mathbb D E_x)\\
&=\overline{\operatorname{wtchar}(V)}\,\overline{T_x}
=\overline{\operatorname{ch}_{\mathcal H}(E_x\otimes V)}.
\end{aligned}
\]
Duality takes shifts to opposite shifts, which have the same Grothendieck sign. Both sides are additive on triangles. The finite generation just proved therefore extends the identity to all \(K\). \(\square\)

Thus bar compatibility for arbitrary IC objects has been deduced from the exact dual-standard comparison (8.63); it has not been inferred from the name “Verdier duality.”

#### 8.6.4. Canonical recognition, parity and positivity

**Proposition 8.4 (conditional IC–KL identification).** Under G0, G2, G3 and the minimal-parabolic package MP0–MP1,
\[
H^r((J_y)_x)=0
\quad\text{unless }r=2k\ge0,
\]
and
\[
P_{x,y}(q)=\sum_{k\ge0}
 \dim H^{2k}((J_y)_x)\,q^k.
\tag{8.70}
\]
In particular every KL coefficient is a nonnegative integer. In the perverse normalization the identical formula is
\[
P_{x,y}(q)=\sum_{k\ge0}
 \dim H^{2k-d_y}((I_y)_x)\,q^k.
\tag{8.71}
\]
For \(x<y\), the possible degrees satisfy \(0\le2k<d_y-d_x\).

**Proof.** Put \(b^r_{x,y}=\dim H^r((J_y)_x)\). Pointwise purity identifies the weight-graded character with its single prescribed weight in each degree:
\[
e_x(J_y)=\sum_r(-1)^r b^r_{x,y}v^r.
\tag{8.72}
\]
This equation is the exact place where G3 is used.

By (8.45) and the shift rule for duality,
\[
\mathbb D J_y
=\mathbb D(I_y[-d_y])
\simeq I_y(d_y)[d_y]
=J_y2d_y.
\]
The even shift has Grothendieck sign \(+1\). Lemmas 8.3–8.4 therefore give
\[
\overline{\operatorname{ch}_{\mathcal H}(J_y)}
=v^{-2d_y}\operatorname{ch}_{\mathcal H}(J_y).
\]
Hence
\[
F_y=v^{-d_y}\operatorname{ch}_{\mathcal H}(J_y)
\quad\text{satisfies}\quad \overline{F_y}=F_y.
\tag{8.73}
\]
The top-cell coefficient is \(v^{-d_y}T_y=H_y\). Support is \(x\le y\). For \(x<y\), express its coefficient in the \(H_x\) basis:
\[
v^{d_x-d_y}e_x(J_y)
=\sum_r(-1)^r b^r_{x,y}v^{r-(d_y-d_x)}.
\tag{8.74}
\]
The strict bound (8.46) makes every exponent strictly negative. Thus \(F_y\) satisfies precisely (8.16) of Proposition 8.2.

The canonical-basis uniqueness used here can also be checked directly. If two such bar-invariant elements differ, choose a maximal Bruhat index in the nonzero support of their difference. Unitriangularity of bar makes its coefficient fixed by \(v\mapsto v^{-1}\). But it has only strictly negative exponents; a nonzero such Laurent polynomial cannot be fixed. This contradiction proves uniqueness. No positivity or parity theorem enters this argument.

It follows that \(F_y=C'_y\), where the already proved canonical basis has expansion
\[
C'_y=v^{-d_y}\sum_{x\le y}P_{x,y}(v^2)T_x.
\]
Equality in the proved standard basis implies
\[
\sum_r(-1)^r b^r_{x,y}v^r=P_{x,y}(v^2).
\tag{8.75}
\]
The right side has no negative exponents and no odd exponents. Each coefficient on the left comes from one cohomological degree, because of pointwise purity; different degrees cannot cancel at that weight. Therefore \(b^r_{x,y}=0\) for negative or odd \(r\). The coefficient at \(v^{2k}\) is \(b^{2k}_{x,y}\), so it is nonnegative, proving (8.70).

Finally \(J_y=I_y[-d_y]\) gives
\(H^{2k}(J_y)=H^{2k-d_y}(I_y)\), proving the exact shift (8.71). The strict boundary bound gives \(2k<d_y-d_x\), so the usual KL degree bound is recovered. \(\square\)

This deduction improves the minimal formal input list: a separate odd-stalk vanishing hypothesis is unnecessary once pointwise purity, the strict bound and Proposition 8.3’s character comparison are proved. It does not prove pointwise purity. It also does not prove that the surviving pure weight-\(2k\) spaces are sums of \(\mathbf1(-k)\); the weight-dimension character forgets Hodge type or other coefficient structure. Such a Tate statement is stronger than the positivity conclusion needed here.

Without G3, the weighted Euler sum can have contributions from distinct cohomological degrees at the same weight and can cancel. Canonical recognition of that Euler sum would then not identify individual stalk dimensions. Complex purity alone does not justify the coefficientwise step from (8.75) to (8.70).

#### 8.6.5. The ordinary perverse Grothendieck relation

Forget mixed weights. In addition assume a bounded perverse t-structure on the constructible category whose heart \(\mathscr P(X)\) is a finite-length abelian category, with distinct simples exactly
\[
I_y=j_{y!*}\mathbb Q_{C_y}[d_y],
\]
and standards
\[
\Delta_x=j_{x!}\mathbb Q_{C_x}[d_x]\in\mathscr P(X).
\tag{8.76}
\]
The assertion that all these extensions by zero are perverse is part of this hypothesis, not a consequence of the preceding Euler computation.

For any bounded complex \(K\), define the ordinary stalk Euler characteristic
\[
\chi_x(K)=\sum_r(-1)^r\dim H^r((K)_x).
\tag{8.77}
\]
The same long-exact-sequence cancellation as in Lemma 8.3 makes it additive.

**Lemma 8.5.** The derived and perverse-heart Grothendieck groups agree, the \([I_y]\) form a free basis, and the collection of \(\chi_x\) is injective on that group.

**Proof.** Bounded perverse truncation triangles give
\[
[K]=\sum_n(-1)^n[{}^pH^n(K)].
\]
This defines the inverse of the inclusion of the heart on Grothendieck groups: applying a triangle gives a finite long exact sequence in the heart, whose alternating classes cancel, and on a heart object the sum has just its degree-zero term.

In a finite-length category, a class is the sum of the classes of its simple factors. The multiplicity of each simple is independent of a composition series. One proves this by induction on length: compare two first simple subobjects; if they agree, use the quotient, and if they are different their intersection is zero and their sum admits both simples as factors, after which induction applies to the quotient by that sum. Multiplicities are additive in short exact sequences by splicing series. They consequently define inverse maps between this Grothendieck group and the free abelian group on the simple objects. Thus the \([I_y]\) form a free basis.

Support and the top-cell normalization show
\[
\chi_x(I_y)=0\quad(x\nleq y),\qquad
\chi_y(I_y)=(-1)^{d_y}.
\]
In a closure-compatible order, the matrix of these functions on the simple basis is upper triangular with diagonal entries \(+1\) or \(-1\). Successive back-substitution gives an integral inverse. Hence all \(\chi_x\) together are injective. \(\square\)

**Proposition 8.5 (conditional simple-in-standard character expansion).** If Proposition 8.4's stalk identity is available for these underlying ordinary IC objects, then
\[
[I_y]=
\sum_{x\le y}(-1)^{d_y-d_x}P_{x,y}(1)[\Delta_x].
\tag{8.78}
\]

**Proof.** Extension by zero gives
\[
\chi_z(\Delta_x)=
\begin{cases}
(-1)^{d_x},&z=x,\\
0,&z\ne x.
\end{cases}
\tag{8.79}
\]
The IC stalk identity and its shift give
\[
\chi_z(I_y)=(-1)^{d_y}P_{z,y}(1).
\tag{8.80}
\]
Applying \(\chi_z\) to the right side of (8.78) gives just
\[
(-1)^{d_y-d_z}P_{z,y}(1)(-1)^{d_z}
=(-1)^{d_y}P_{z,y}(1).
\]
It equals (8.80) for every \(z\), including indices off the support. Injectivity from Lemma 8.5 proves (8.78). \(\square\)

This is an equality of classes and characters, not a direct-sum decomposition. It expands a simple object in standard classes. It is not the statement \([\Delta_x:I_y]=P_{x,y}(1)\) in these same ordinary-flag labels.

For exact matrix accounting put
\[
S_{x,y}(q)=(-1)^{d_y-d_x}P_{x,y}(q),\qquad
Q(q)=S(q)^{-1}.
\tag{8.81}
\]
The inverse exists over \(\mathbb Z[q]\): write \(S=1+N\) with strictly upper triangular \(N\); since \(W\) is finite,
\(S^{-1}=1-N+N^2-\cdots\) is a finite sum. With row vectors of basis classes, (8.78) is \(\mathbf I=\boldsymbol\Delta S(1)\), so
\[
[\Delta_x]=\sum_y Q_{y,x}(1)[I_y],
\qquad
[\Delta_x:I_y]=Q_{y,x}(1).
\tag{8.82}
\]
The second equality follows from the actual composition-series basis of the finite-length heart. This also fixes the transpose: the first inverse index is the simple label \(y\), and the second is the standard label \(x\).

For a rank-one flag, \(P_{1,s}=1\), so
\[
[I_s]=[\Delta_s]-[\Delta_1],\qquad
[\Delta_s]=[I_s]+[I_1].
\tag{8.83}
\]
This smallest example already rules out identifying the simple-in-standard signs with standard composition multiplicities.

#### 8.6.6. Exact conversion to the dominant Verma convention

**Proposition 8.6 (conditional transfer to Verma multiplicities).** Retain the explicit geometric hypotheses of the preceding sections. Namely, suppose there is a finite-length perverse category on ordinary \(G/B\) with cell standards \(\Delta_x\), simple IC objects \(I_y\), and the proved geometric IC–KL stalk identity. Proposition 8.5 then gives

\[
[I_y]=\sum_{x\leq y}(-1)^{\ell(y)-\ell(x)}
 P_{x,y}(1)[\Delta_x].
\tag{8.84}
\]

As row vectors of Grothendieck-group elements this says \(I=\Delta\mathsf K(1)\). Theorem 8.3 gives \(\Delta=I\mathsf Q(1)\). Since the IC classes are the simple basis of a finite-length heart,

\[
[\Delta_x:I_y]=Q_{y,x}(1)=P_{xw_0,yw_0}(1).
\tag{8.85}
\]

This is the precise ordinary-flag standard multiplicity formula. Its support has \(y\leq x\).

Suppose, in addition, a correctly normalized exact localization/holonomic dictionary has been **proved** on the categories and objects under consideration, with every relevant simple accounted for, and with

\[
F(\Delta_x)=M((xw_0)\mathbin\cdot\lambda),\qquad
F(I_y)=L((yw_0)\mathbin\cdot\lambda).
\tag{8.86}
\]

An exact equivalence suffices. An exact functor with these nonzero simple images also suffices for composition-series transfer. In the principal case the label conversion is the actual identity
\(-x\rho-\rho=(xw_0)\mathbin\cdot0\), because \(w_0\rho=-\rho\). For a general dominant integral \(\lambda\), the displayed dictionary must be proved at its specified twist; it is not inferred merely from the principal case.

For dominant Verma label \(w\) and simple label \(z\), take \(x=ww_0\) and \(y=zw_0\). Exactness carries a composition series to the specified simple series. Equation (8.85) now gives

\[
\begin{aligned}[c]
[M(w\mathbin\cdot\lambda):L(z\mathbin\cdot\lambda)]
 &=Q_{zw_0,ww_0}(1)\\
 &=P_{(ww_0)w_0,(zw_0)w_0}(1)
 =P_{w,z}(1).
\end{aligned}
\tag{8.87}
\]

The condition \(y\leq x\) becomes \(w\leq z\) by the longest-element Bruhat reversal proved in Section 8.5.2, so the zero convention agrees as well. With left-longest labels instead, (8.42) gives \(P_{\theta(w),\theta(z)}=P_{w,z}\), with the same result and no silent transpose.

This proves the algebraic conversion in full. The unsupplied inputs are the actual mixed foundations and flag geometry, normalized IC with pointwise purity and strict bounds, the required perverse/regular holonomic comparison, and the exact localization dictionary. Proposition 8.4 deduces coefficient positivity from the stipulated pointwise IC purity; the purity itself remains a substantive geometric obligation.

### 8.7. Finite-Weyl bimodule foundations

The following algebraic proofs supply the reflection representation, support filtrations, Hom formula and indecomposable classification needed for a second approach to KL positivity. They work for every finite Weyl group, including products and rank zero. The indecomposable character theorem and Hodge induction are proved in Sections 8.8–8.11; the finite complex regular integral category $\mathcal O$ comparison is proved in Sections 8.12–8.15.

Use the real root span $V$, put $R=\operatorname{Sym}(V^*)$ with $\deg V^*=2$, and fix $M(n)^i=M^{i+n}$. The category $\mathcal B$ is the additive, graded, idempotent closure of the actual Bott–Samelson bimodules $R(1)\otimes_{R^s}M$. Thus its objects are constructed before any character theorem is assumed. Write $u=v^{-1}$ for the support-character grading convention used below.

The same results are treated in Wolfgang Soergel, [*Kazhdan–Lusztig-Polynome und unzerlegbare Bimoduln über Polynomringen*, freely accessible arXiv version math/0403496v2](https://arxiv.org/abs/math/0403496v2), §§4–6. The proofs below explicitly establish the finite-Weyl statements and all their algebraic prerequisites.

#### 8.7.1. The real reflection representation at the finite scope

Let \(W\) be the Weyl group of a finite real root system on its real span \(V\), equipped with the positive definite invariant root inner product. The rank-zero case is allowed. The group acts faithfully because it is defined as a subgroup of \(\operatorname{GL}(V)\). If \(w\) fixes a hyperplane, orthogonality makes the orthogonal complement stable and one-dimensional. A nonidentity \(w\) must act there by \(-1\); hence \(w\) is an orthogonal reflection.

We verify that its hyperplane is a root hyperplane. Suppose instead that a point on the fixed hyperplane avoids all root hyperplanes. The Weyl chambers form the components of the complement of the finite root hyperplane arrangement. A sufficiently small ball about that point avoids every root hyperplane. The reflection fixes the centre, preserves the ball, and therefore sends its chamber to itself. The proved Weyl-chamber action is free, so this would give \(w=1\). Thus the entire fixed hyperplane is covered by the finitely many root hyperplanes. A finite union of proper linear subspaces of a real vector space cannot cover that space: choose a line with direction and base point avoiding the finitely many defining linear conditions; each proposed covering subspace meets it in at most one point. One root hyperplane therefore equals the fixed hyperplane of \(w\). The orthogonal reflection in that hyperplane is unique, so \(w\) is the corresponding root reflection.

Consequently
\[
\operatorname{codim}V^w=1
\quad\Longleftrightarrow\quad
w\text{ is a root reflection}.
\tag{8.88}
\]
Distinct root reflections have distinct fixed hyperplanes and distinct minus eigenspaces. This supplies reflection faithfulness at the finite Weyl scope without importing the more general infinite-Coxeter realization theorem. The Weyl-chamber action used here is the actual root-system theorem already proved in the course; it is not the desired KL positivity statement.

#### 8.7.2. Graded decomposition and cancellation

Let \(A\) be a finitely generated nonnegatively graded real algebra with \(A_0=\mathbb R\), and let \(M\) be a finitely generated graded \(A\)-module. Every graded piece of \(A\), and hence of \(M\), is finite-dimensional. A degree-zero endomorphism is determined by the images of finitely many homogeneous generators, in finitely many finite-dimensional pieces. Thus \(\operatorname{End}^0_A(M)\) is finite-dimensional. All module decompositions below preserve the grading.

**Lemma 8.6.** Every such \(M\) is a finite direct sum of indecomposable modules. An indecomposable module has a local finite-dimensional degree-zero endomorphism algebra. Every element of that endomorphism algebra is either invertible or nilpotent.

**Proof.** For an endomorphism \(f\), finite-dimensionality gives a polynomial relation. Factor its minimal polynomial as \(t^a g(t)\), with \(g(0)\ne0\). If both factors occur, Bezout polynomials give a projection in \(\mathbb R[f]\) onto the generalized zero part; it is an idempotent, and its image and complementary image split \(M\). On an indecomposable module the projection is zero or one. Thus either \(f\) is nilpotent or its minimal polynomial has nonzero constant term, in which case a polynomial in \(f\) is its inverse.

Let \(E=\operatorname{End}^0_A(M)\) for indecomposable \(M\). Its nonunits form an ideal. Closure under multiplication by arbitrary elements follows from finite-dimensional linear algebra: if \(af\) were a unit, \(f\) would have a one-sided inverse and hence a two-sided inverse in the finite-dimensional algebra. For closure under addition, suppose nonunits \(f,g\) had invertible sum \(u=f+g\). Then \(u^{-1}f\) and \(u^{-1}g\) are nonunits, so they are nilpotent. But \(1-u^{-1}f=u^{-1}g\) is invertible by a finite geometric series, a contradiction. The nonunits are therefore the unique maximal ideal, proving locality.

To obtain a finite indecomposable decomposition, start splitting nontrivial idempotents. Each nonzero summand contributes a nonzero orthogonal projection, and a family of such projections is linearly independent in \(\operatorname{End}^0_A(M)\). There can be only finitely many splittings. The terminal summands are indecomposable. \(\square\)

**Lemma 8.7.** The multiset of indecomposable summands is unique, and direct-sum cancellation holds.

**Proof.** Compare two finite decompositions, with a summand \(M_1\) in the first and summands \(N_j\) in the second. Compose the inclusion of \(M_1\), projection to \(N_j\), inclusion from \(N_j\), and projection to \(M_1\). Their sum is \(1_{M_1}\). Since the nonunits in its local endomorphism algebra form an ideal, at least one composite is invertible. The corresponding maps show that \(M_1\) is a direct summand of \(N_j\): normalize the composite to one, and split the resulting idempotent on \(N_j\). Indecomposability gives \(M_1\cong N_j\).

For completeness, this matching removes summands even when the original decompositions are embedded differently. Write the comparison isomorphism in block form with the matched block \(a:M_1\to N_j\) invertible. Multiplying by invertible block triangular maps reduces it to \(a\oplus(d-ca^{-1}b)\). The second block is consequently an isomorphism of the complementary sums. Induction proves uniqueness and cancellation. In particular the split Grothendieck group is free on indecomposable isomorphism classes, so equality of two actual-object classes implies an isomorphism. \(\square\)

This applies to finitely generated graded modules over \(R\otimes R\), where \(R=\operatorname{Sym}(V^*)\) and linear forms have degree two. An \(R\)-bimodule finitely generated on the right is also finitely generated over \(R\otimes R\), by the same generators.

**Lemma 8.8.** A finitely generated graded direct summand \(P\) of a finite graded free \(R\)-module is graded free.

**Proof.** Choose a homogeneous real basis of \(P/PR_{>0}\) and homogeneous lifts. The corresponding map from a finite shifted free module \(F\) to \(P\) is surjective: its cokernel is bounded below and finitely generated, and a nonzero least-degree homogeneous element cannot equal a sum of positive-degree multiples of lower-degree elements. This is the graded Nakayama argument. Since \(P\) is a direct summand of a free module it is projective, so the surjection splits. A splitting can be made degree zero by taking its degree-zero homogeneous component. Its kernel \(K\) is finitely generated, and reduction of \(F=P\oplus K\) modulo \(R_{>0}\) shows \(K/KR_{>0}=0\), because the chosen basis makes \(F/FR_{>0}\to P/PR_{>0}\) an isomorphism. The same least-degree argument gives \(K=0\). Thus \(F\cong P\). \(\square\)

#### 8.7.3. Ext between linear graphs: the full elementary calculation

Put \(S=\operatorname{Sym}(Z^*)\) for a finite real vector space \(Z\). For a linear subspace \(U\subset Z\), let \(R(U)=S/I_U\). Write
\[
Z=C\oplus U'\oplus V'\oplus D,
\qquad U=C\oplus U',\qquad V=C\oplus V'.
\tag{8.89}
\]
Such complements exist by extending bases of \(C=U\cap V\). Set \(c=\dim C\), \(a=\dim U'\), \(b=\dim V'\), \(d=\dim D\).

The quotient \(R(U)\) has a free Koszul resolution on the coordinate functions of \(V'\oplus D\). This resolution is exact: in one coordinate the two-term complex \(S\xrightarrow{X}S\) resolves \(S/(X)\), because multiplication by \(X\) is injective; tensoring those complexes one coordinate at a time remains exact, as the remaining coordinate rings are free over the new coordinate factor. Apply \(\operatorname{Hom}_S(-,R(V))\). Each \(V'\)-coordinate acts as multiplication by its own variable on \(R(V)\); its dual two-term complex has cohomology only in degree one, equal to the quotient by that variable. Each \(D\)-coordinate acts by zero and contributes a two-term zero-differential complex, with one copy of \(\mathbb R\) in degrees zero and one. Coordinates of \(C\) contribute \(R(C)\). Coordinates of \(U'\) contribute only the scalar quotient.

The cohomology of this tensor product is computed without a Kunneth theorem import: every finite complex of vector spaces splits into its cohomology with zero differential and elementary two-term identity complexes, by choosing complements of boundaries and cycles; tensoring an identity complex is contractible. Therefore, as ungraded modules,
\[
\operatorname{Ext}^n_S(R(U),R(V))
\cong R(C)\otimes\bigwedge^{n-b}(D^*),
\quad b\le n\le b+d,
\tag{8.90}
\]
and it vanishes in every other degree. Degree shifts in the graded version are those of the Koszul generators; each coordinate has degree two.

In particular \(\operatorname{Ext}^1\) is zero when \(\operatorname{codim}_V(U\cap V)=b\ge2\). When \(b=1\), it is a free rank-one \(R(U\cap V)\)-module. When \(b=0\), the additional \(D\)-directions can contribute, so no vanishing assertion is made. This last case includes \(V\subset U\); it must not be lost in a simplified statement.

For the codimension-one case choose a linear function \(\beta\) vanishing on \(U\), whose restriction to \(V\) is nonzero. There is an exact graded sequence
\[
0\longrightarrow R(V)(-2)
\xrightarrow{\ \beta\ } R(U\cup V)
\longrightarrow R(U)\longrightarrow0.
\tag{8.91}
\]
Here \(M(k)^i=M^{i+k}\), so the generator in \(R(V)(-2)\) has degree two. Indeed, the kernel of restriction to \(U\) consists of functions supported on the \(V\)-branch and vanishing on \(U\cap V\); that ideal in \(R(V)\) is generated by \(\beta|_V\). In the two-term Koszul computation the connecting cochain of a lift of \(1\) is the nonzero generator along that normal coordinate. Thus (8.91) generates \(\operatorname{Ext}^1\); all its classes are multiples by functions on \(U\cap V\).

Apply this to
\[
G_x=\{(x\xi,\xi):\xi\in V\}\subset V\times V,
\qquad R_x=R(G_x).
\]
Projection onto the second coordinate identifies \(G_x\cap G_y\) with \(V^{x^{-1}y}\). Both graphs have dimension \(\dim V\). Distinct graphs consequently have nonzero \(\operatorname{Ext}^1\) only when \(x^{-1}y\) is a reflection, by (8.88). In that case the Ext module is rank one over the ring of their intersection, and is annihilated by the equation of the corresponding right-coordinate root hyperplane. Thus localization on the right at a different root hyperplane kills the extension. For equal graphs the self-Ext can be nonzero, as (8.90) shows; no blanket assertion that all graph extensions are reflection extensions is used.

This calculation also proves that distinct incomparable Bruhat labels have no Ext in degree one, since multiplication by a reflection makes two distinct labels Bruhat-comparable. That comparability is a root-system/subword fact already established in the course.

#### 8.7.4. Rank-one algebra, duality and adjunction

For a reflection \(s\), choose \(\alpha\in V^*\) with \(s\alpha=-\alpha\). Choose the other coordinates fixed by \(s\). Then
\[
R^s=\mathbb R[\text{fixed coordinates},\alpha^2],
\qquad R=R^s\oplus\alpha R^s.
\tag{8.92}
\]
Write \(f=f_0+\alpha f_1\) uniquely with \(f_i\in R^s\), and put \(\varepsilon(f)=f_1\). It has degree \(-2\). The pairing
\[
(f,g)\longmapsto\varepsilon(fg)
\]
has matrix \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\) in the \(R^s\)-basis \(1,\alpha\), hence is perfect. More explicitly, \(1\) maps to the functional extracting the \(\alpha\)-coefficient, and \(\alpha\) maps to the functional extracting the constant coefficient. The map
\[
R(2)\longrightarrow\operatorname{Hom}_{R^s}(R,R^s),
\qquad f\longmapsto[g\mapsto\varepsilon(fg)]
\tag{8.93}
\]
is a degree-zero \(R\)-linear isomorphism. The linearity follows by moving a multiplying element from the first to the second input of the commutative pairing.

Define left translation of a bimodule by
\[
\Theta_s M=R(1)\otimes_{R^s}M.
\]
Induction and coinduction are naturally isomorphic after the indicated shift by (8.93). The usual Hom adjunction is proved by the maps \(f\mapsto[m\mapsto f(1\otimes m)]\) and \(g\mapsto[r\otimes m\mapsto r g(m)]\); their balancing identities follow directly from \(R^s\)-linearity. Coinduction uses evaluation at \(1\), with inverse given by \(g(m)(r)=g(rm)\). Consequently \(\Theta_s\) is both the left and right adjoint of itself on graded bimodules. These maps preserve the right \(R\)-action, so the same statement holds for the whole graded Hom space as a right \(R\)-module, not merely its degree-zero part.

For a bimodule free of finite rank on the right define
\[
DM=\operatorname{Hom}_{-R}(M,R),
\qquad (r f)(m)=f(rm),\quad(f r)(m)=f(m)r.
\tag{8.94}
\]
The right-module evaluation map \(M\to DDM\) is an isomorphism, as is checked on a right free basis; it intertwines the left action by the formula in (8.94). The dual is exact on any sequence whose quotient is right free, since that sequence splits as right modules. Moreover
\[
D(R_x)\cong R_x,\qquad D(M(k))=(DM)(-k),
\qquad D\Theta_s M\cong\Theta_s DM.
\tag{8.95}
\]
The graph identity follows by evaluating a right-linear functional at \(1_x\): left multiplication by \(r\) acts on that value by the same twisted polynomial \(r(x\xi)\). The last identity follows by applying the perfect pairing (8.93) to the first tensor factor. Equivalently its explicit Hom description is
\[
R(1)\otimes_{R^s}\operatorname{Hom}_{-R}(M,R)
\cong\operatorname{Hom}_{R^s}
 \bigl(R(1),\operatorname{Hom}_{-R}(M,R)\bigr)
\cong\operatorname{Hom}_{-R}
 \bigl(R(1)\otimes_{R^s}M,R\bigr).
\]
All maps here are the tensor–Hom maps obtained from (8.93), so their degrees, balancing, and outer bimodule actions are fixed. In particular the Bott–Samelson bimodules \(\Theta_{s_1}\cdots\Theta_{s_m}R\) are self-dual by induction, without assuming the indecomposable character conjecture.

The two graph maps give exact sequences
\[
0\to R_{sx}(-2)\to R\otimes_{R^s}R_x\to R_x\to0,
\qquad
0\to R_x(-2)\to R\otimes_{R^s}R_x\to R_{sx}\to0.
\tag{8.96}
\]
To verify them, tensor the identity case with the right-twisted graph module \(R_x\). In the identity case the middle ring is the coordinate ring of \(G_e\cup G_s\): in the reflected coordinate it has equation \(a^2=b^2\), and in all fixed coordinates the two outer coordinates agree. Restricting to either branch is surjective and its kernel is generated on the other branch by \(a-b\) or \(a+b\), respectively. That generator has degree two. These are also the explicit representatives of the codimension-one Ext generator from Section 8.7.3.

#### 8.7.5. Minimal complexes without a categorical black box

Let \(\mathcal A\) be an idempotent-complete additive category with finite-dimensional real degree-zero Hom spaces and finite indecomposable decompositions as in Section 8.7.2. For indecomposable \(P,Q\), place in \(\operatorname{rad}(P,Q)\) every morphism when \(P\not\cong Q\), and the nonunits in the local endomorphism algebra when \(P=Q\). Extend this definition to matrices on sums. It is an ideal: a composite through two nonisomorphic indecomposables cannot be a unit, since a unit composite would split one as a summand of the other. In an isotypic block its quotient is a matrix algebra over the division algebra \(\operatorname{End}(P)/\operatorname{rad}(P,P)\).

A bounded complex is minimal if every differential belongs to this ideal. If a differential has a block outside the radical, some component between isomorphic indecomposables is invertible. Use block row and column operations to turn that component into an identity with all other entries in its row and column zero: the remaining block is the Schur complement. The adjacent differentials have zero components into and out of the identity block because consecutive differentials compose to zero. Thus an elementary contractible complex \(P\xrightarrow{1}P\) splits off. There are finitely many indecomposable summands in all terms, so repeated removal terminates and gives a minimal complex.

If \(f:F\to G\) is a homotopy equivalence between two minimal complexes, its homotopy inverse \(g\) has
\[
g^i f^i-1=d^{i-1}h^i+h^{i+1}d^i
\]
in the radical, and the analogous identity holds for \(f^i g^i-1\). Every matrix \(1-r\) with \(r\) in this ideal is invertible: its first diagonal entry is one minus a nonunit in a local endomorphism algebra, hence a unit; block elimination reduces the problem to one fewer summand, with Schur-complement correction still in the same ideal. Induction proves the assertion. This already makes the two displayed composites invertible, and therefore makes every \(f^i\) invertible.

The familiar nilpotence assertion can also be proved here without a noncommutative determinant argument. Let \(E\) be the finite-dimensional endomorphism algebra of a finite sum and \(J\) the matrix ideal. Its powers stabilize. If \(J^n=JJ^n\), choose a smallest generating set \(m_1,\ldots,m_k\) for the finite left \(E\)-module \(J^n\). When \(k>0\), write \(m_1=\sum_i a_i m_i\) with \(a_i\in J\). The invertibility of \(1-a_1\) expresses \(m_1\) using the other generators, a contradiction. Thus \(k=0\) and \(J^n=0\). In particular finite geometric series give the same inverse-lifting conclusion. Minimal complexes representing the same homotopy object are isomorphic term by term. No Soergel positivity input has entered.

#### 8.7.6. Graph support as a literal subspace condition

Let \(Q\) be the fraction field of \(R\), used in the right tensor factor. For different \(x,y\in W\), choose a linear form \(a\) with \(a(x\xi)-a(y\xi)\ne0\). This polynomial is a unit in \(Q\). The two graph ideals in \(R\otimes Q\) are therefore comaximal. The quotient on the graph \(x\) is \(Q\), with left action \(a\mapsto a(x\xi)\).

Consider a finite filtration of a bimodule \(M\) whose subquotients are finite sums of shifts of \(R_x\), with each fixed label appearing in only one layer. All subquotients are right free, so \(M\) is right free by splitting the successive sequences as right modules. After tensoring on the right with \(Q\), the comaximal graph ideals split all extensions between different labels. Indeed their product annihilates the extension, and the Chinese-remainder idempotents split it; this follows directly from \(I_x+I_y=1\). The layers with one fixed label are already sums of \(Q\), not extensions of that label. Hence
\[
M_Q=\bigoplus_x M_Q^x,
\tag{8.97}
\]
where the left polynomial action on \(M_Q^x\) is graph evaluation at \(x\). Right freeness embeds \(M\) into \(M_Q\).

For \(m\in M\), let \(A(m)\) be the set of its nonzero components in (8.97). Every polynomial vanishing on \(\bigcup_{x\in A(m)}G_x\) kills its image in \(M_Q\), and hence kills \(m\). Conversely, a polynomial annihilating \(m\) vanishes on each of those graphs, by looking at the nonzero component over \(Q\). Thus its annihilator is exactly the intersection of the selected graph ideals. In particular its support is a union of whole graphs, without an embedded or partial-support contribution. Consequently, for any subset \(A\subset W\),
\[
\Gamma_A M=M\cap\bigoplus_{x\in A}M_Q^x.
\tag{8.98}
\]

A length-ordered graph filtration with right-free quotients is the intrinsic support filtration: if the quotient has only the complementary generic components, an element in the selected generic components maps to zero after right localization; torsion-freeness of the quotient makes its image already zero. This proves both inclusions in the identification.

The proviso about one label in one layer is essential. An arbitrary self-extension of a graph module can have a nonsemisimple generic left action; no claim about such a module is made. The support filtrations considered next have direct sums at each length, so they satisfy the proviso.

#### 8.7.7. The two support categories

Define \(\mathcal F_\Delta\) to consist of finitely generated bimodules with finite graph support for which
\[
\Gamma_{\ge i}M/\Gamma_{\ge i+1}M
\]
is a finite direct sum of shifts of \(R_x\) with \(\ell(x)=i\). Define \(\mathcal F_\nabla\) by the analogous ascending filtration \(\Gamma_{\le i}\). Every object is right free, and Section 8.7.6 applies. Put
\[
\Delta_x=R_x(-\ell(x)),\qquad
\nabla_x=R_x(\ell(x)).
\tag{8.99}
\]
Let \((M:\Delta_x(n))\) or \((M:\nabla_x(n))\) denote the shifted multiplicity in its corresponding layer. This is well-defined by Section 8.7.2 cancellation and the right free graded ranks. These categories are closed under finite sums and summands: support intersection (8.98) commutes with direct sums, and a summand of a layer that is a sum of graph modules is again a sum of graph modules by graded projective freeness 8.8, applied separately to each graph component.

Use a variable \(u\) for the source's grading character. It satisfies \(u=v^{-1}\) for the lesson variable \(v=q^{1/2}\). Thus the standard Hecke basis in these conventions obeys
\[
H_s^2=1+(u^{-1}-u)H_s,
\qquad C_s=H_s+u,
\qquad \overline u=u^{-1}.
\tag{8.100}
\]
Set
\[
h_\Delta(M)=\sum_{x,n}(M:\Delta_x(n))u^nH_x,
\qquad
h_\nabla(M)=\sum_{x,n}(M:\nabla_x(n))u^{-n}H_x.
\tag{8.101}
\]
The inverse exponent in the second formula is intentional.

#### 8.7.8. Pairing the two adjacent levels

Fix a simple reflection \(s\) acting on the left. In descending length order, subdivide each length layer by placing its \(s\)-ascending labels before its \(s\)-descending labels. No Ext in degree one connects two distinct labels of equal length: Section 8.7.3 would require a reflection, which changes length parity. Therefore this subdivision is obtained by intrinsic support submodules and does not create new extensions within a layer.

Now group the \(s\)-descending labels of length \(i\) with the \(s\)-ascending labels of length \(i-1\). Two distinct labels from this block can differ by a reflection only if they are \(x,sx\). To check this, suppose the higher label is \(x\), the lower is \(y\), and a reflection relates them. Then \(y<x\), \(sx<x\), and \(sy>y\). The left lifting property gives \(y\le sx\). Both sides have length \(i-1\), so \(y=sx\). This lifting property follows from the reduced-subword/exchange argument already proved for the finite Weyl group; it does not involve a KL coefficient.

Each two-level block therefore splits as a sum of blocks supported on individual pairs \(\{x,sx\}\), with \(sx<x\). Here is the extension argument rather than a semisimplicity assumption. Ext in degree one is zero between graph modules in different pairs by Section 8.7.3. It is then zero between filtered sums in different pairs: induction using the Hom/Ext exact sequence in either variable has zero groups on both sides of the Ext-one term. Hence the successive extensions can be split across pairs. Inside a pair the descending flag has the exact sequence
\[
0\longrightarrow\bigoplus_a R_x(a)
\longrightarrow M_{\{x,sx\}}
\longrightarrow\bigoplus_b R_{sx}(b)\longrightarrow0.
\]
Thus it is an extension of the low layer by the high layer. Its entries are the Ext generators of Section 8.7.3, multiplied by functions on the intersection.

Restrict the left action from \(R\) to \(R^s\). The two graph modules of a pair become isomorphic. Every entry of the extension becomes zero. In fact the generator is the two-branch ring \(R(G_x\cup G_{sx})\), and its quotient onto \(R_x\) has an \(R^s\)-right-\(R\) section given by the invariants under \(s\) on the first coordinate. In the reflected coordinate this is the invariant subring of \(a^2=b^2\), and restriction to either branch is an isomorphism; fixed coordinates are unchanged. Every polynomial multiple of that generator also restricts to a split extension. Thus the restricted pair block is a direct sum of the original graph shifts, all now written with the high label \(x\).

Induce back by the flat functor \(R\otimes_{R^s}-\); flatness is the explicit free rank-two decomposition (8.92). The graph branch sequences (8.96) give its descending support flag, with high term \(R_x(-2)\) and low quotient \(R_{sx}\). This applies to every shift and every copy.

The induced pair flags, taken in descending block order, merge into a length-ordered graph flag. At a shared length between consecutive blocks, the two subsets of labels are the disjoint ascending and descending subsets, so there is no same-label extension. All different labels at that length have Ext-one zero by parity, so that layer splits. Section 8.7.6 then identifies the constructed flag with the actual intrinsic support flag. This proves
\[
\Theta_s\mathcal F_\Delta\subset\mathcal F_\Delta.
\tag{8.102}
\]

For \(sx<x\), the resulting multiplicities are exactly
\[
\begin{aligned}
(\Theta_sM:\Delta_x(n))
 &=(M:\Delta_x(n+1))+(M:\Delta_{sx}(n)),\\
(\Theta_sM:\Delta_{sx}(n))
 &=(M:\Delta_x(n))+(M:\Delta_{sx}(n-1)).
\end{aligned}
\tag{8.103}
\]
The first uses the high graph shift \(-2\) and the global shift \(+1\); the second uses the low quotient and the same global shift. Since
\[
C_sH_x=H_{sx}+u^{-1}H_x,
\qquad C_sH_{sx}=H_x+uH_{sx},
\]
equations (8.103) give the complete character rule
\[
h_\Delta(\Theta_sM)=C_sh_\Delta(M),
\qquad h_\Delta(M(1))=u h_\Delta(M).
\tag{8.104}
\]
Every coefficient was obtained from actual support layers, not from equality of generic ranks alone.

#### 8.7.9. The ascending version from actual duality

Apply the right-free dual \(D\) from Section 8.7.4 to a descending graph flag. Each short exact sequence is right split, so dualization is exact and reverses the order. Each graph shift \(R_x(n)\) becomes \(R_x(-n)\). The resulting ascending graph flag is intrinsic by Section 8.7.6. Therefore
\[
D:\mathcal F_\Delta\longleftrightarrow
 \mathcal F_\nabla^{\mathrm{op}},
\qquad h_\nabla(DM)=h_\Delta(M).
\tag{8.105}
\]
The bidual evaluation proves the reverse equivalence. Using \(D\Theta_s\cong\Theta_sD\) gives stability of \(\mathcal F_\nabla\) and
\[
h_\nabla(\Theta_sN)=C_sh_\nabla(N),
\qquad h_\nabla(N(1))=u^{-1}h_\nabla(N).
\tag{8.106}
\]
In particular any unshifted Bott–Samelson object
\[
B(\underline s)=\Theta_{s_1}\cdots\Theta_{s_m}R
\]
belongs to both support categories, is self-dual, and has
\[
h_\Delta(B(\underline s))
=h_\nabla(B(\underline s))
=C_{s_1}\cdots C_{s_m}.
\tag{8.107}
\]
No indecomposable character assertion is used in this equality.

#### 8.7.10. The full Hom formula with a Bott–Samelson target

For a right graded free module \(F\), write its rank as \(r_u(F)=\sum_j u^{a_j}\) when \(F\cong\bigoplus_jR(a_j)\), and write \(\overline{r_u(F)}=r_u(F)|_{u\mapsto u^{-1}}\). Use the standard bilinear Hecke pairing
\[
\langle H_x,H_y\rangle=\delta_{xy}.
\tag{8.108}
\]
Left multiplication by \(C_s\) is self-adjoint for this pairing: on the pair \(H_x,H_{sx}\), its matrix is \(\begin{pmatrix}u^{-1}&1\\1&u\end{pmatrix}\) when \(sx<x\), which is symmetric; these pairs partition the basis. This proves the assertion directly from the multiplication formula.

**Theorem 8.4.** If \(M\in\mathcal F_\Delta\) and \(N\) is a finite direct sum of shifted Bott–Samelson objects, then the entire graded bimodule Hom space is right graded free and
\[
\overline{r_u\operatorname{Hom}(M,N)}
=\langle h_\Delta(M),h_\nabla(N)\rangle.
\tag{8.109}
\]

**Proof.** First let \(N=R\). Every map \(M\to R\) kills \(\Gamma_{\ge1}M\): its image is supported on the identity graph, whereas the source submodule has only nonidentity graphs; their possible intersection is a proper subvariety of the identity graph and cannot support a nonzero element of the free domain \(R_e\). Equivalently Section 8.7.6 computes its generic graph components and gives zero. Hence
\[
\operatorname{Hom}(M,R)
=\operatorname{Hom}(M/\Gamma_{\ge1}M,R).
\]
The quotient is \(\bigoplus_nR(n)^{(M:\Delta_e(n))}\). Its dual is \(\bigoplus_nR(-n)^{(M:\Delta_e(n))}\), so its conjugated rank is \(\sum_n(M:\Delta_e(n))u^n\), precisely the identity coefficient of \(h_\Delta(M)\). This proves both freeness and (8.109) at the base.

For a target \(N=\Theta_sN'\), the actual rank-one self-adjunction in Section 8.7.4 gives
\[
\operatorname{Hom}(M,\Theta_sN')
\cong\operatorname{Hom}(\Theta_sM,N')
\]
as graded right modules. The induction hypothesis and (8.104), followed by self-adjointness of the Hecke pairing, give
\[
\langle h_\Delta(\Theta_sM),h_\nabla(N')\rangle
=\langle h_\Delta(M),C_sh_\nabla(N')\rangle
=\langle h_\Delta(M),h_\nabla(\Theta_sN')\rangle.
\]
The Hom isomorphism also preserves freeness, so induction proves the entire assertion for every word. A target shift by \(k\) shifts Hom by \(k\), and conjugating its rank multiplies by \(u^{-k}\), the same factor as \(h_\nabla(N(k))\). Finite sums are additive. \(\square\)

Using the duality \(D\) gives the second version: \(M\) a shifted Bott–Samelson sum and \(N\in\mathcal F_\nabla\) have the same free-Hom formula. Explicitly \(\operatorname{Hom}(M,N)\cong\operatorname{Hom}(DN,DM)\) as graded right modules under the duality in Section 8.7.4, and (8.105) identifies the two characters. The Hecke pairing is symmetric.

The formula expressed in layer multiplicities is
\[
r_u\operatorname{Hom}(M,N)
=\sum_{x,n,m}(M:\Delta_x(n))(N:\nabla_x(m))u^{m-n}.
\tag{8.110}
\]
This includes arbitrary \(M\in\mathcal F_\Delta\) with a Bott–Samelson-sum target, and the dual version just stated. It is not yet claimed for arbitrary direct summands on the Bott–Samelson side: equality of ranks for an object and its complementary summand does not by itself identify the rank for each summand. That extension will use actual Hom-surjectivity along flags and the local multiplication identities.

#### 8.7.11. A useful primitive inclusion before the local multiplication proof

Let \(B\) be a Bott–Samelson object or one of its graded summands. For any \(z\in W\), \(B\otimes_RR_z\) belongs to both support categories: for the whole object it is a sequence of left translations applied to the single graph \(R_z\), by associativity; for a summand use Section 8.7.7's summand closure. Right twisting permutes generic graph labels by \(x\mapsto xz\).

Apply this with \(z=y^{-1}\). The ascending identity layer of the twist is \(\Gamma_e(B\otimes R_{y^{-1}})\). Its inclusion has right-free quotient, because all remaining ascending layers are right free. Untwisting proves that
\[
\Gamma_yB\hookrightarrow B
\quad\text{splits as a graded right }R\text{-module}.
\tag{8.111}
\]
This is a right-module splitting, not a bimodule decomposition. In particular the induced map after tensoring on the right with \(\mathbb R=R/R_{>0}\) is injective. This is the direct-summand fact used in the Hodge embedding argument. It follows here from the actual support-transport proof and graded free flags, without assuming that the indecomposable character conjecture is true.

The same twist applied to the descending identity quotient proves that \(B/\Gamma_{\ne y}B\) is a right graded free graph module. For \(\Gamma_yB\), freeness already follows from (8.111); for the two order subquotients a complete reordering argument is still needed, and will be supplied with the local classification package.

#### 8.7.12. Reordering flags and the four support pieces

Every two linear orders compatible with a finite partial order are connected by adjacent swaps of incomparable elements. To prove this, move the first element of the desired order leftwards in the current order. Any element it passes cannot be smaller, by minimality in the desired order, and cannot be larger, by compatibility of the current order. All passed elements are incomparable. Remove the matched first element and repeat.

Apply this to Bruhat order on the finite support set. Start with the ascending length flag of an object in \(\mathcal F_\nabla\). Refine each same-length layer into individual graph labels. Distinct labels in such a layer have no Hom and no Ext-one by Section 8.7.3, so this refinement is intrinsic. In an adjacent swap of incomparable labels, their two-layer extension splits by Section 8.7.3, so either order gives the same graph multiplicities and natural support subquotients. Iterating the swaps proves that every Bruhat-compatible ascending graph order gives a right-free flag with the same shifted multiplicities. Descending orders give the analogous assertion for \(\mathcal F_\Delta\).

Consequently, for \(B\in\mathcal B\) and \(y\in W\), the natural pieces
\[
\Gamma_y^{\le}B=\Gamma_{\le y}B/\Gamma_{<y}B,
\qquad
\Gamma_y^{\ge}B=\Gamma_{\ge y}B/\Gamma_{>y}B
\tag{8.112}
\]
are right-free graph modules. Their shifted multiplicities are respectively those of \(\nabla_y\) and \(\Delta_y\). Choose an order with all labels below \(y\) first, then \(y\), to see the first assertion; use the reverse order for the second. Here labels outside the actual support can be ignored.

The elementary support formula (8.98) also gives injections
\[
\Gamma_yB\hookrightarrow\Gamma_y^{\le}B,
\qquad
\Gamma_y^{\ge}B\hookrightarrow\Gamma^yB,
\qquad \Gamma^yB=B/\Gamma_{\ne y}B.
\tag{8.113}
\]
For example \(\Gamma_yB\cap\Gamma_{<y}B=0\), and \(\Gamma_{\ge y}B\cap\Gamma_{\ne y}B=\Gamma_{>y}B\). Every module in (8.113) is free on the right: the order pieces by the argument just given, and \(\Gamma_yB,\Gamma^yB\) by Section 8.7.11's right-twist and identity-layer construction. The outer bimodule action on each factors through the single graph ring \(R_y\), by Section 8.7.7 and right torsion-freeness.

If \(y\) is maximal in the actual Bruhat support, the natural map
\[
\Gamma_y^{\le}B\longrightarrow\Gamma^yB
\tag{8.114}
\]
is an isomorphism. In a compatible order placing \(y\) last, the latter is its graph subquotient. Move \(y\) to the position immediately after its strict predecessors. It passes only incomparable labels. Each swap is the split two-layer swap above, whose natural map on the \(y\)-piece is an isomorphism. The resulting piece is precisely the source of (8.114), proving that the map itself, not just its generic rank, is an isomorphism.

#### 8.7.13. The reflection-hyperplane local decomposition

For a root reflection \(t\), let \(\alpha_t\) be an equation of its fixed hyperplane in the right-coordinate space. Let \(R_{(t)}\) be the graded localization at the multiplicative set of nonzero homogeneous polynomials not divisible by \(\alpha_t\). This retains the grading; it does not invert arbitrary nonhomogeneous polynomials. Put \(U_{z,t}=R(G_z\cup G_{zt})\), always written with \(z<zt\).

**Lemma 8.9.** The right localization of each whole Bott–Samelson object is a direct sum of shifted modules of the forms
\[
R_z\otimes_RR_{(t)},\quad z<zt,
\qquad U_{z,t}\otimes_RR_{(t)},\quad z<zt.
\tag{8.115}
\]
For an arbitrary object of \(\mathcal B\), its localization is a direct summand of such a sum. The single graph in (8.115) is the lower graph; an unrestricted high-graph single is not included.

**Proof.** The initial object \(R_e\) has the required form since \(e<t\). Assume the assertion for a word and apply a left rank-one induction \(R\otimes_{R^s}-\); the global grading shift causes no difficulty. For different right graph labels \(a,b\), Section 8.7.3 says that their Ext-one localizes to zero unless \(b=at\): a reflection extension at any other root hyperplane is annihilated by a polynomial invertible in \(R_{(t)}\). This vanishing extends to filtered graph modules with labels in disjoint right-\(t\) pairs by the Hom/Ext exact sequences, in the same way as in Section 8.7.8.

If \(z<zt\), the positive root sent by \(z\) to the reflection wall remains positive under the simple reflection \(s\), except when that root is the simple root of \(s\). Indeed a simple reflection permutes all positive roots other than its own simple root. The exception is exactly \(sz=zt\). Thus
\[
sz\ne zt\quad\Longrightarrow\quad sz<szt.
\tag{8.116}
\]
This is also the root-sign form of the lifting property. It keeps the lower labels lower after induction.

For a single \(R_z\), its induced module is the two-branch ring on \(G_z\cup G_{sz}\). If \(sz=zt\), this is the permitted \(U_{z,t}\). Otherwise the extension between its two graph branches splits after the chosen localization, and (8.116) says both resulting single graphs are lower in their respective right-\(t\) pairs.

For \(U_{z,t}\), first suppose \(sz=zt\). Its graph union is invariant under \(s\) on the first coordinate. Let \(\alpha\) be the equation of that left reflection hyperplane. The divided difference \((f-sf)/(2\alpha)\) is polynomial and descends to the union ring: if \(f\) vanishes on the union then so does the numerator; division by \(\alpha\) still vanishes on the dense subset of each graph where \(\alpha\ne0\), and therefore on the entire graph. This is legitimate since each graph projects onto the whole left-coordinate space. The plus and minus eigenspaces of \(s\) are consequently \(U^+\) and \(\alpha U^+\). The explicit free decomposition \(R=R^s\oplus\alpha R^s\) gives
\[
R\otimes_{R^s}U^+\cong U,
\qquad R\otimes_{R^s}U\cong U\oplus U(-2).
\tag{8.117}
\]
Both isomorphisms preserve the right action; they are multiplication maps in the two eigenspaces.

If \(sz\ne zt\), the rank-one branch sequence, tensored with the right-free union ring, is
\[
0\to U_{z,t}(-2)\to R\otimes_{R^s}U_{z,t}
\to U_{sz,t}\to0.
\tag{8.118}
\]
The two pairs \(\{z,zt\}\) and \(\{sz,szt\}\) are disjoint. No graph across them differs by right \(t\), since that would force \(sz=zt\). Their localized Ext-one groups vanish, so (8.118) splits after localization. Both pair labels are lower by (8.116). This completes the induction. Taking a summand commutes with localization and proves the final assertion. \(\square\)

For clarity, the relative tensoring in (8.118) is exact because the branch sequence is split as a right \(R\)-module sequence. The quotient graph module is right free. No geometric decomposition theorem enters 8.9.

#### 8.7.14. The exact multiplication identities

Define
\[
p_y=\prod_{\substack{t\text{ a root reflection}\\yt<y}}\alpha_t,
\qquad\deg p_y=2\ell(y).
\tag{8.119}
\]
There are exactly \(\ell(y)\) factors, by the root inversion count. Their linear equations are pairwise nonassociate by reflection faithfulness. The empty product for the identity is one.

**Theorem 8.5.** The injections (8.113) have the exact images
\[
\Gamma_yB\cong(\Gamma_y^{\le}B)p_y,
\qquad
\Gamma_y^{\ge}B\cong(\Gamma^yB)p_y
\tag{8.120}
\]
for every \(B\in\mathcal B\).

**Proof for whole Bott–Samelson sums.** First inspect either map after localization at \(\alpha_t\), using 8.9. Only the single-graph or two-branch summands involving \(y\) contribute. If \(y\) is the lower label of a branch pair, the first support piece \(\Gamma_y^{\le}\) is already \(\Gamma_y\), and the second support quotient \(\Gamma_y^{\ge}\) is already \(\Gamma^y\). Both maps have unit image. A lower single graph has the same behavior. If \(y\) is the higher label, either map is multiplication by \(\alpha_t\) on a single right-free graph module, as seen directly in the branch sequence Section 8.7.4. There is no high single graph in (8.115). Thus in this localization either map has image divisible by \(\alpha_t\) exactly when \(yt<y\).

The graph support functors used in this inspection commute with right localization. One can see this from Section 8.7.7: an element acquires selected support after localization exactly when the omitted generic components can be killed by an allowed denominator; those components were already zero in the fraction field. All the finitely generated submodules in question localize by that intersection description. The same conclusion follows by localizing their kernel equations for the graph ideals.

Choose a right free homogeneous basis of the target of either injection. Each coordinate polynomial of its image is divisible by every \(\alpha_t\) with \(yt<y\), by the preceding local computation. Distinct linear prime factors are relatively prime in the polynomial ring, so the coordinate is divisible by their product. This proves the two inclusions into the right sides of (8.120).

It remains to prove equality, rather than just divisibility. The whole-object Hom formula (8.110) gives
\[
\begin{aligned}
r_u(\Gamma_yB)
 &=r_u\operatorname{Hom}(R_y,B)
 =\sum_m(B:\nabla_y(m))u^{m-\ell(y)},\\
r_u(\Gamma_y^{\le}B)
 &=\sum_m(B:\nabla_y(m))u^{m+\ell(y)}.
\end{aligned}
\tag{8.121}
\]
The first Hom identification evaluates a map at \(1_y\); a vector with support on the single graph is annihilated by its graph ideal by Section 8.7.7. Multiplication by \(p_y\) lowers the grading-shift rank exponent by \(2\ell(y)\), so (8.121) gives equal graded ranks for the first inclusion.

For the second, maps \(B\to R_y\) kill \(\Gamma_{\ne y}B\) by generic graph support, and therefore identify with maps \(\Gamma^yB\to R_y\). The target quotient is graph-free by Section 8.7.12 and Section 8.7.11. Its dual rank, computed with the other version of (8.110), gives
\[
\begin{aligned}
r_u(\Gamma^yB)
 &=\sum_n(B:\Delta_y(n))u^{n+\ell(y)},\\
r_u(\Gamma_y^{\ge}B)
 &=\sum_n(B:\Delta_y(n))u^{n-\ell(y)}.
\end{aligned}
\tag{8.122}
\]
Again multiplication by \(p_y\) gives exactly the latter rank.

Every module in (8.121)–(8.122) is a finite graded free right module. Equality of its shifted rank polynomials is equality of every graded real dimension, because its Hilbert series is that rank polynomial times the common Hilbert series of \(R\), with inverse exponent if the usual dimension variable is used. Each injection thus has zero cokernel in every graded degree. This proves equality in (8.120) for whole sums and their shifts.

Finally all maps in (8.120) are natural support maps, and support functors commute with a direct-sum decomposition by Section 8.7.7. Restricting a proved isomorphism to the image of the corresponding idempotent gives the same isomorphism for each summand. Every object of \(\mathcal B\) is such a summand. This proves (8.120) at its asserted full scope. \(\square\)

#### 8.7.15. Hom formula for every summand

**Theorem 8.6.** For \(M\in\mathcal F_\Delta\) and \(N\in\mathcal B\), the graded Hom is right free and
\[
r_u\operatorname{Hom}(M,N)
=\sum_{x,n,m}(M:\Delta_x(n))(N:\nabla_x(m))u^{m-n}.
\tag{8.123}
\]
The dual statement holds for \(M\in\mathcal B\), \(N\in\mathcal F_\nabla\).

**Proof.** For a graph standard \(M=\Delta_y(n)\), evaluating at its generator gives \(\Gamma_yN\) with shift \(\ell(y)-n\). Identity (8.120) and the free order piece from Section 8.7.12 therefore give (8.123) and actual right freeness.

For a general \(M\), peel off a first layer of a refined descending graph flag. Thus there is an exact sequence
\[
0\to A\to M\to C\to0
\tag{8.124}
\]
in which \(A\) is a finite shifted sum of one graph standard and \(C\in\mathcal F_\Delta\) has a shorter flag. Its shifted multiplicities add. If the target \(N_0\) is a whole Bott–Samelson sum, (8.110) applied to all three modules shows that
\[
0\to\operatorname{Hom}(C,N_0)
\to\operatorname{Hom}(M,N_0)
\to\operatorname{Hom}(A,N_0)\to0
\tag{8.125}
\]
is exact. Left exactness gives the first two terms and identifies the image at the third. The three free rank polynomials satisfy additivity by (8.110), so their graded dimensions show that this image is the entire third term in every degree. This is the surjectivity assertion; generic rank alone would not suffice.

If \(N\) is a summand of \(N_0\), include a map \(A\to N\) into \(N_0\), extend it by (8.125), and project back to \(N\). Thus (8.125) remains exact with target \(N\). By induction its outer terms are free, so the sequence splits as right modules and gives freeness plus rank additivity. The graph-standard base already proved then establishes (8.123) for the entire flag.

For the second version, apply the exact duality \(D\) to both variables. The category \(\mathcal B\) is stable under \(D\), since whole Bott–Samelson objects are self-dual and their summands dualize to summands. By (8.105) it interchanges the two flag categories and their characters. The graded right-module Hom identification under \(D\) and the symmetry of the pairing give the claimed formula and freeness. \(\square\)

The proof also gives the exact Hom lifting that will be used below: restriction from a \(\Delta\)-flag to its first sublayer is surjective with target in \(\mathcal B\), and the dual lifting from a \(\nabla\)-flag to its last quotient is surjective with source in \(\mathcal B\). Each statement holds degree by degree.

#### 8.7.16. Construction and classification of all indecomposables

**Theorem 8.7.** For every \(x\in W\) there is a unique, up to degree-zero isomorphism, indecomposable \(B_x\in\mathcal B\) such that its support is contained in \(\{y:y\le x\}\), its \(x\)-standard multiplicity is one with shift zero, and its other \(x\)-shifted multiplicities vanish. Every indecomposable in \(\mathcal B\) is exactly one \(B_x(n)\). Moreover \(DB_x\cong B_x\).

**Construction.** Choose a reduced word for \(x\). Its Bott–Samelson character (8.107) is the corresponding product of \(C_s=H_s+u\). All standard labels are products of subwords, hence below \(x\); its \(H_x\)-coefficient is exactly one, because only the full reduced subword reaches length \(\ell(x)\). Its actual support flags therefore have one \(\Delta_x\) with shift zero. Decompose the object by Section 8.7.2. Exactly one summand has the graph \(x\) in its support, and it is indecomposable: if it split, only one further part could have that graph and the other part belongs among the complementary summands. More explicitly take the indecomposable decomposition first; nonnegative shifted layer multiplicities summing to the monomial one select a single indecomposable. Call it \(B_x\). It has the specified support and top multiplicity.

The whole object is self-dual. Duality permutes its indecomposable summands and preserves their generic graph support, since \(DR_y=R_y\). The unique summand with graph \(x\) consequently maps to itself. Thus \(DB_x\cong B_x\), without any character conjecture.

**Classification and uniqueness.** Let \(M\) be an arbitrary indecomposable in \(\mathcal B\), and choose a maximal label \(x\) in its actual Bruhat support. By Section 8.7.12 its top order piece agrees with \(\Gamma^xM\); by (8.120) the inclusion of \(\Gamma_xM\) into this quotient has image \((\Gamma^xM)p_x\). Choose a homogeneous generator \(m\) in a right free basis of \(\Gamma^xM\). Its shift is \(\ell(x)+n\) for one of the actual \(\Delta_x(n)\) multiplicities, by (8.122) and (8.120). The quotient of \(B_x(n)\) on graph \(x\) has the same generator degree. Denote its basis generator by \(b\).

There is a degree-zero graph map
\[
f_0:\Gamma^xB_x(n)\to\Gamma^xM,
\qquad b\mapsto m.
\]
By the dual Hom lifting after Section 8.7.15, it lifts to \(f:B_x(n)\to M\). This use of lifting is legitimate because \(x\) is maximal: a Bruhat-compatible ascending flag can put \(x\) last, with right-free kernel \(\Gamma_{\ne x}M\) in \(\mathcal F_\nabla\).

Let \(i_M:\Gamma_xM\to\Gamma^xM\) and \(i_B:\Gamma_xB_x(n)\to\Gamma^xB_x(n)\) be the support inclusions. They identify their sources with multiplication by \(p_x\). Define a degree-zero graph map
\[
g_0:\Gamma_xM\to\Gamma_xB_x(n),
\qquad i_M^{-1}(m p_x)\mapsto i_B^{-1}(b p_x),
\]
and send the other homogeneous basis generators to zero. By the standard Hom lifting after Section 8.7.15 it extends to \(g:M\to B_x(n)\): the maximal graph \(\Gamma_xM\) is a first sublayer of a descending flag, whose quotient lies in \(\mathcal F_\Delta\).

Naturality of the support inclusions gives
\[
f\bigl(i_B^{-1}(b p_x)\bigr)=i_M^{-1}(m p_x).
\]
Hence \(gf\) fixes the nonzero generator of \(\Gamma_xB_x(n)\). It cannot be nilpotent. 8.6 says that a nonnilpotent degree-zero endomorphism of an indecomposable is invertible. Normalize \(g\) by that inverse. The resulting composite with \(f\) is one, so \(B_x(n)\) splits from \(M\). Indecomposability of \(M\) gives \(M\cong B_x(n)\).

This argument applies to any candidate constructed from another reduced word, proving uniqueness. Different labels are distinguished by the unique maximal support label; shifts for a fixed label are distinguished by the nonzero top graph generator degree. Thus the parametrization \((x,n)\mapsto B_x(n)\) is bijective. \(\square\)

#### 8.7.17. Character duality and the degree-zero residue algebra

The construction of \(B_x\) gives actual nonnegative standard coefficients with leading term \(H_x\) and all other labels below \(x\). Self-duality and (8.105) give
\[
h_\Delta(B_x)=h_\nabla(B_x).
\tag{8.126}
\]
They also give bar invariance. Here is the needed extra induction rather than an inference from the word “self-dual.” A reduced Bott–Samelson object for \(x\) decomposes as \(B_x\) and shifts of \(B_y\), \(y<x\), by Section 8.7.16. Its self-duality and unique decomposition make the multiplicities of \(B_y(n)\) and \(B_y(-n)\) equal. The grading Laurent polynomial for these paired shifts is bar invariant. Its whole character is the bar-invariant product of the \(C_s\). By induction on \(\ell(x)\), subtracting the lower bar-invariant characters leaves the character of \(B_x\) bar invariant. Thus
\[
\overline{h_\Delta(B_x)}=h_\Delta(B_x).
\tag{8.127}
\]
This still does not give the strictly positive source-\(u\) lower powers required of a canonical element. The Hodge induction in Section 8.11 supplies precisely this remaining canonical-character condition.

Finally restriction of a degree-zero endomorphism of \(B_x\) to its free rank-one top quotient gives a real scalar, because the graph ring has degree-zero part \(\mathbb R\). This is a surjective algebra map
\[
\operatorname{End}^0(B_x)\to\mathbb R,
\tag{8.128}
\]
with section given by scalar multiples of the identity. An endomorphism with nonzero top scalar is not nilpotent, hence is a unit by 8.6. A unit has a nonzero scalar on the quotient, since its inverse also acts there. Thus the kernel is exactly the nonunit ideal of the local endomorphism algebra, and
\[
\operatorname{End}^0(B_x)/\operatorname{rad}\operatorname{End}^0(B_x)
\cong\mathbb R.
\tag{8.129}
\]
This supplies the real residue-field input for the minimal-complex decomposition in the Hodge proof. It does not assert that the entire degree-zero endomorphism algebra equals \(\mathbb R\) before the character theorem is proved.

These proofs establish actual support transport, both support characters, the whole and summand Hom formulas, exact local multiplication identities, classification and self-duality of every indecomposable $B_x$, the primitive right-module inclusion, and the elementary minimal-complex package. They do not identify $\operatorname{ch}(B_x)$ with the canonical Hecke basis. In particular, bar invariance alone in Section 8.7.17 does not prove positivity or the Verma-multiplicity statement in Theorem 8.2.

### 8.8. Finite Lefschetz linear algebra

The finite-dimensional arguments below establish the six linear-algebra tools used in the Hodge induction. The comparison source is [Elias–Williamson, arXiv:1212.0791v2, §2](https://arxiv.org/abs/1212.0791v2).

Let \(H=\bigoplus_{m\in\mathbb Z}H^m\) be a finite-dimensional graded real vector space. Let \(L:H^m\to H^{m+2}\), and suppose
\[
L^d:H^{-d}\longrightarrow H^d
\quad\text{is an isomorphism for every }d\geq0.
\tag{8.130}
\]
Let \(b\) be a symmetric bilinear form with \(b(H^m,H^n)=0\) unless \(m+n=0\), and with \(b(Lx,y)=b(x,Ly)\). When stated, nondegeneracy means nondegeneracy on all of \(H\). Put
\[
P^{-d}=\ker\bigl(L^{d+1}:H^{-d}\to H^{d+2}\bigr),
\qquad b_d(x,y)=b(x,L^dy)
\quad(x,y\in H^{-d}).
\tag{8.131}
\]

**Lemma 8.10 (primitive decomposition and orthogonality).** Under (8.130),
\[
H^{-d}=P^{-d}\oplus L H^{-d-2},\qquad
H=\bigoplus_{d\geq0}\bigoplus_{j=0}^{d}L^jP^{-d}.
\tag{8.132}
\]
If \(b\) is nondegenerate, then every \(b_d\) is nondegenerate. The summands in (8.132) lying in a given degree are orthogonal for that degree's Lefschetz form. On \(L^jP^{-d}\subset H^{-i}\), where \(d=i+2j\), that form pulls back to \(b_d|_{P^{-d}}\). These primitive forms are nondegenerate.

**Proof.** The map \(L^{d+1}\) on \(L H^{-d-2}\) is identified with the isomorphism \(L^{d+2}:H^{-d-2}\to H^{d+2}\). In particular \(L\) is injective on \(H^{-d-2}\), and the indicated restriction is an isomorphism onto \(H^{d+2}\). Subtracting its unique preimage from any element of \(H^{-d}\) leaves an element of the kernel \(P^{-d}\). The two spaces intersect trivially, giving the first formula.

Iterating gives the negative-degree portion of the second formula. For positive degree \(i\), apply the isomorphism \(L^i:H^{-i}\to H^i\) to the already obtained negative-degree decomposition. All primitive chains stop after \(L^dP^{-d}\), because \(L^{d+1}P^{-d}=0\); their maps up to that point are injective by (8.130). This proves all direct sums, including degree zero.

The grading and nondegeneracy of \(b\) identify \(H^d\) with the dual of \(H^{-d}\). Compose that perfect pairing with \(L^d\) to obtain nondegeneracy of \(b_d\).

For \(p\in P^{-d}\), \(q\in P^{-e}\), with \(L^jp,L^kq\) both in degree \(-i\), we have \(d=i+2j\), \(e=i+2k\) and
\[
b_i(L^jp,L^kq)=b(p,L^{i+j+k}q).
\tag{8.133}
\]
If \(d>e\), then \(j>k\) and \(i+j+k=e+(j-k)\geq e+1\), so the right side is zero by primitiveness of \(q\). If \(e>d\), symmetry gives the same conclusion. If \(d=e\), then \(j=k\) and (8.133) is \(b_d(p,q)\). Thus the decomposition is orthogonal with the asserted forms. Nondegeneracy of \(b_i\) now implies that each orthogonal summand form is nondegenerate. \(\square\)

Assume from now on that \(H\) lies in one parity and its lowest nonzero degree is \(-n\). The **standard Hodge sign condition** means
\[
b_d|_{P^{-d}}
\text{ is }(-1)^{(n-d)/2}\text{-definite}
\quad(0\leq d\leq n, d\equiv n\pmod2).
\tag{8.134}
\]
A definite form on a zero space is allowed. Global reversal of all signs can equally be specified. This convention puts a positive form on the lowest primitive degree.

**Lemma 8.11 (continuous deformation).** Fix \(H\) and nondegenerate \(b\). Let \(L_t\) vary continuously on a connected interval, remain self-adjoint for \(b\), and satisfy (8.130) throughout. If (8.134), with a fixed global sign, holds for one parameter, it holds for every parameter.

**Proof.** Every matrix of \(b_{d,t}\) is continuous and symmetric, and is nonsingular by Lemma 8.10. Its inertia is locally constant: at a parameter, take an orthogonal decomposition into its positive and negative eigenspaces; the least absolute eigenvalue is positive. A sufficiently small change in the matrix leaves its restrictions on those same subspaces respectively positive and negative. Hence the positive and negative indices are at least their original dimensions; since their sum is the whole dimension and the form stays nonsingular, both indices are unchanged. A locally constant function on an interval is constant.

The dimensions of \(P_t^{-d}\) are fixed, namely \(\dim H^{-d}-\dim H^{-d-2}\), by (8.132). Orthogonality shows that the positive and negative indices of \(b_{d,t}|_{P_t^{-d}}\) are the respective indices of \(b_{d,t}\) minus those of \(b_{d+2,t}\); the latter form is its restriction on \(L_tH^{-d-2}\). All these indices are therefore constant. At the initial parameter each primitive form has the prescribed definite sign. The same indices at all parameters establish exactly that sign throughout. \(\square\)

**Lemma 8.12 (balanced invariant subspaces).** Suppose (8.130) and (8.134) hold. Let \(V\subset H\) be graded and \(L\)-stable, with \(\dim V^{-d}=\dim V^d\) for every \(d\geq0\). Then the restricted operator on \(V\) satisfies (8.130); the restriction of \(b\) to \(V\) is nondegenerate; and the primitive forms of \(V\) have the signs inherited from (8.134).

**Proof.** The map \(L^d:V^{-d}\to V^d\) is injective because its extension to \(H^{-d}\) is injective. Equality of dimensions makes it an isomorphism. Lemma 8.10's decomposition proof used only (8.130), so applies to \(V\) even before knowing nondegeneracy of its form.

Its primitive space is \(P_V^{-d}=V^{-d}\cap P_H^{-d}\). The form there is the restriction of the definite ambient primitive form, hence is definite and nondegenerate. Orthogonality, proved by the computation (8.133) without a nondegeneracy assumption, gives a direct sum of nondegenerate forms on each negative-degree \(V^{-d}\). Therefore each \(b_d\) on that space is nondegenerate. The restricted \(L^d\) is an isomorphism, so the original graded form pairs \(V^{-d}\) and \(V^d\) perfectly. It follows that \(b|_V\) is nondegenerate on all degrees. The inherited signs have already been verified. \(\square\)

The lowest surviving primitive degree of \(V\) can differ from that of \(H\); its global standard sign may accordingly differ. The precise inherited sign formula (8.134) avoids assuming a new positive lowest sign without checking it.

**Lemma 8.13 (an injective-map substitute for weak Lefschetz).** Let graded spaces \(V,W\) carry degree-two operators \(L\), and let \(\phi:V\to W(1)\) be a graded \(\mathbb R[L]\)-module map. Thus \(\phi(V^m)\subseteq W^{m+1}\). Suppose \(\phi\) is injective in degrees \(m\leq-1\), \(W\) satisfies hard Lefschetz and definite primitive Hodge forms, and the symmetric graded forms satisfy
\[
b_W(\phi\alpha,\phi\beta)=b_V(\alpha,L\beta).
\tag{8.135}
\]
Then \(L^d:V^{-d}\to V^d\) is injective for every \(d\geq0\). If its source and target dimensions agree, it is an isomorphism.

**Proof.** For \(d=0\), the map is the identity. If \(d\geq1\) and a nonzero \(\alpha\in V^{-d}\) satisfied \(L^d\alpha=0\), then \(z=\phi\alpha\ne0\) lies in \(W^{-(d-1)}\), and \(L^dz=0\) by \(L\)-linearity. Thus \(z\) is primitive. Its definite primitive norm must be nonzero. But (8.135) and \(L\)-linearity give
\[
b_W(z,L^{d-1}z)
=b_V(\alpha,L^d\alpha)=0,
\]
a contradiction. This proves injectivity; the final assertion is finite-dimensional linear algebra. \(\square\)

**Lemma 8.14 (vanishing for a displaced centre).** The form \(b\) may now be degenerate. Suppose it is graded and \(L\)-self-adjoint, and that for a positive integer \(d\),
\[
L^i:H^{-d-i}\longrightarrow H^{-d+i}
\quad\text{is an isomorphism for all }i\geq0.
\tag{8.136}
\]
Then \(b(x,L^iy)=0\) for every \(x,y\in H^{-i}\), \(i\geq0\).

**Proof.** Reindexing the decomposition proof of Lemma 8.10 around centre \(-d\) gives
\[
H^m=\bigoplus_{j\geq0}L^jQ^{m-2j},\qquad
Q^{-d-t}=\ker L^{t+1}\subset H^{-d-t}\quad(t\geq0),
\]
with a summand zero when its index is not of this form. Let \(m=-i\leq0\). For generators \(L^jx,L^ky\in H^m\), with \(j\geq k\), self-adjointness gives
\[
b(L^jx,L^{i+k}y)=b(x,L^{i+j+k}y).
\]
The vector \(y\in Q^{m-2k}\) is killed by \(L^{2k-d-m+1}\). The exponent on the right satisfies
\[
i+j+k-(2k-d-m+1)=j-k+d-1\geq0.
\]
Hence the right side is zero. For \(j<k\), symmetry of the Lefschetz form interchanges the two generators and reduces to the same argument. Bilinearity and the displayed direct sum prove the assertion. No nondegeneracy of \(b\) was used. \(\square\)

**Lemma 8.15 (a large-parameter rank-one extension).** Let \(W\) satisfy (8.130) and the standard primitive sign condition (8.134), with lowest degree \(-n\). Let \(V\) be a graded space with
\[
\dim V^m=\dim W^{m+1}+\dim W^{m-1}.
\tag{8.137}
\]
Suppose \(V\) has a nondegenerate graded symmetric form and self-adjoint degree-two operators \(L_\zeta\), \(\zeta\geq0\). In degree \(-i\), suppose choices of lifts give a vector-space isomorphism
\[
\alpha:W^{-i+1}\to V^{-i},\qquad
\beta:W^{-i-1}\to V^{-i},\qquad
V^{-i}=\alpha W^{-i+1}\oplus\beta W^{-i-1}.
\tag{8.138}
\]
Here \(\alpha,\beta\) are simply chosen linear maps on these finite spaces, not assumed to descend canonically from a polynomial-module quotient. For the Lefschetz form \(F_{i,\zeta}(u,v)=b_V(u,L_\zeta^iv)\), assume
\[
\begin{split}
F_{i,\zeta}(\beta y,\beta y')&=0,\\
F_{i,\zeta}(\alpha x,\beta y)&=b_W(x,L^iy),\\
F_{i,\zeta}(\alpha p,\alpha q)
&=D_i(p,q)+\zeta i c\,b_W(p,L^{i-1}q)
\quad(i\geq1, p,q\in P_W^{-i+1}),
\end{split}
\tag{8.139}
\]
where \(c>0\) is fixed and \(D_i\) is independent of \(\zeta\). For \(i=0\), interpret \(P_W^1=0\); the first two formulas suffice. Then for all sufficiently large \(\zeta\), \(L_\zeta\) satisfies hard Lefschetz on \(V\), and its primitive forms satisfy the standard signs with lowest degree \(-n-1\).

**Proof.** Choose a basis \(e_1,\ldots,e_a\) of \(W^{-i-1}\) orthogonal for its nondegenerate Lefschetz form \(b_{i+1}\), and a basis \(p_1,\ldots,p_b\) of \(P_W^{-i+1}\). For \(i\geq1\), primitive decomposition gives
\(W^{-i+1}=LW^{-i-1}\oplus P_W^{-i+1}\). For \(i=0\), hard Lefschetz gives \(W^1=LW^{-1}\), so the same assertion holds with the primitive part zero. In the basis
\[
\alpha(Le_1),\ldots,\alpha(Le_a),\quad
\beta e_1,\ldots,\beta e_a,\quad
\alpha p_1,\ldots,\alpha p_b,
\]
the Gram matrix of \(F_{i,\zeta}\) is
\[
\begin{pmatrix}
A&J&C\\ J&0&0\\ C^{\mathsf t}&0&Q_\zeta
\end{pmatrix},
\qquad
J=\operatorname{diag}\bigl(b_W(e_j,L^{i+1}e_j)\bigr).
\tag{8.140}
\]
The diagonal \(J\) is invertible. The zero primitive-to-\(\beta\) block follows because
\(b_W(p,L^iy)=b_W(L^ip,y)=0\). The other zero block is the first equation of (8.139). The entries in \(A,C\) may depend on \(\zeta\); no bound on them is needed.

Writing the quadratic form in coordinates \((x,y,z)\), make the invertible change
\[
y'=y+\tfrac12J^{-1}Ax+J^{-1}Cz.
\]
It becomes \(2x^{\mathsf t}Jy'+z^{\mathsf t}Q_\zeta z\). Thus its inertia is that of the direct sum of the hyperbolic block \(\bigl(\begin{smallmatrix}0&J\\J&0\end{smallmatrix}\bigr)\), with indices \((a,a)\), and \(Q_\zeta\). In particular it is nondegenerate exactly when \(Q_\zeta\) is, and its signature (positive index minus negative index) equals that of \(Q_\zeta\).

For \(i\geq1\), (8.139) gives
\[
Q_\zeta=Q_0+\zeta i c Q,
\]
where \(Q\) is the definite matrix of the primitive form on \(P_W^{-i+1}\). Divide by the positive scalar \(\zeta\). For sufficiently large \(\zeta\) this is a small perturbation of the definite matrix \(icQ\), hence is definite with the same sign. If the primitive space is zero there is nothing to check. For \(i=0\), the whole form is already hyperbolic and nonsingular. Only finitely many degrees of \(V\) are nonzero; choose a single sufficiently large parameter working in all of them. Nondegeneracy of every \(F_{i,\zeta}\), and nondegeneracy of the graded form on \(V\), now imply hard Lefschetz exactly as in Lemma 8.10.

It remains to establish all primitive signs rather than only nondegeneracy. Write \(p_W(d)=\dim P_W^{-d}\) for \(d\geq0\), and set \(p_W(-1)=0\). From (8.137) and the primitive dimension formula in (8.132),
\[
p_V(d)=p_W(d-1)+p_W(d+1).
\tag{8.141}
\]
Here the assertion for \(d=0\) uses \(\dim W^1=\dim W^{-1}\). The required standard sign on \(P_V^{-d}\) is \(s_V(d)=(-1)^{(n+1-d)/2}\). The required sign on \(P_W^{-d+1}\) is exactly \(s_V(d)\), when \(d\geq1\) and that parity occurs.

If \(V\) has these standard signs, orthogonal primitive decomposition gives the signature of its degree \(-d\) Lefschetz form as
\[
\sum_{j\geq0}s_V(d+2j)
 \bigl(p_W(d+2j-1)+p_W(d+2j+1)\bigr).
\]
The signs alternate, and consecutive terms cancel in the finite sum. For \(d\geq1\) the result is \(s_V(d)p_W(d-1)\), precisely the signature of the primitive form on \(P_W^{-d+1}\). For \(d=0\), the sum is zero, since \(p_W(-1)=0\). These are exactly the signatures obtained above from (8.140).

Conversely those signatures, together with hard Lefschetz, force the required primitive signs: by orthogonality, the signature on \(P_V^{-d}\) is the signature of \(F_d\) minus the signature of \(F_{d+2}\). The preceding finite sum shows that this difference is \(s_V(d)p_V(d)\). A real nondegenerate symmetric form of dimension \(p_V(d)\) with that signature is definite with sign \(s_V(d)\). This proves every primitive sign, including the lowest positive sign, and completes the proof. \(\square\)

The matrix hypotheses (8.137)–(8.139) are the precise finite calculation corresponding to Elias–Williamson §5. Its implementation for actual bimodules additionally needs the rank-one tensor basis, the induced invariant form and the Demazure-action identities; it is not supplied merely by postulating these matrices.

### 8.9. Support splitting for actual Rouquier complexes

The full graph-layer homotopies are proved before augmentation. Compare [Libedinsky–Williamson, arXiv:1205.4206v2, §3.1 and Proposition 3.7](https://arxiv.org/html/1205.4206v2), and [Elias–Williamson, arXiv:1212.0791v2, §§6.4–6.5](https://arxiv.org/html/1212.0791v2). The two-graph transport imported by those sources is proved directly below.

#### 8.9.1. Inputs, conventions, and precise conclusion

Let \(W\) be a finite Weyl group acting on its real reflection representation \(V\). Put \(R=\operatorname{Sym}(V^*)\), with linear forms of degree 2. All modules and maps are graded; all differentials have internal degree zero. Use \(M(n)^i=M^{i+n}\), so \(R(n)\) has its generator in degree \(-n\). A complex is cohomological, and \(C[k]^i=C^{i+k}\).

The graph module \(R_w\) is the coordinate ring of \(G_w=\{(w\xi,\xi)\}\). It is free of rank one on the right, with left polynomial action evaluated at \(w\xi\). Thus \(R_a\otimes_R R_b\cong R_{ab}\). This is the same graph convention as Section 8.7, even though LW describes its underlying free module using the other coordinate.

The allowed inputs, each already proved in the foundation package, are:

1. The finite-Weyl reduced-subword and simple-reflection lifting properties. In particular, \(a\le b\) implies \(\min(a,sa)\le\min(b,sb)\) in Bruhat order. The proof of this consequence is supplied in Section 8.9.2.
2. Section 8.7.3's graph Ext calculation: Hom between distinct graph modules is zero; Ext-one between distinct graph modules can be nonzero only when their labels differ by a reflection. The extension space is generated over the intersection ring by the corresponding two-graph ring.
3. Section 8.7.4's rank-one description, with \(R=R^s\oplus\alpha_sR^s\), and the actual graph branch sequences for \(B_s=R\otimes_{R^s}R(1)\).
4. Section 8.7.6's generic graph decomposition and support-intersection formula for a graph-filtered module; its right freeness and the corresponding torsion-free assertion for every flag quotient.
5. Sections 8.7.7–8.7.9's stability of both graph-flag categories under \(B_s\otimes_R-\), and Section 8.7.12's reordering of those flags into any Bruhat-compatible linear order. The reordering proof applies to every object of the relevant flag category, not just to indecomposable bimodules.
6. Section 8.7.2's graded summand/Krull–Schmidt properties and Section 8.7.5's removal of contractible summands, only when passing to a minimal representative.

For a reduced expression \(w=s_1\cdots s_m\), define the actual tensor-product complexes
\[
 F_{\underline w}=F_{s_1}\cdots F_{s_m},\qquad
 E_{\underline w}=E_{s_1}\cdots E_{s_m},
\]
where
\[
 F_s=[B_s\xrightarrow{\mu_s}R(1)]\quad\text{in degrees }0,1,
\qquad
 E_s=[R(-1)\xrightarrow{\eta_s}B_s]\quad\text{in degrees }-1,0,
\]

and \(\eta_s(1)=(\alpha_s\otimes1+1\otimes\alpha_s)/2\). Multiplication defines \(\mu_s\). Put
\[
\Delta_y=R_y(-\ell(y)),\quad \nabla_y=R_y(\ell(y)),\quad
\gamma_y^\Delta=\Gamma_{\ge y}/\Gamma_{>y},\quad
\gamma_y^\nabla=\Gamma_{\le y}/\Gamma_{<y}.
\]

**Theorem 8.8 (support-layer homotopy splitting).** For every reduced expression, the following are homotopy equivalences of graded graph-bimodule complexes:
\[
 \gamma_y^\Delta F_{\underline w}\simeq
 \begin{cases}\Delta_w[0]&y=w,\\0&y\ne w,\end{cases}
\qquad
 \gamma_y^\nabla E_{\underline w}\simeq
 \begin{cases}\nabla_w[0]&y=w,\\0&y\ne w.\end{cases}
 \tag{8.142}
\]
The zero cases are contractible complexes of graded graph bimodules. This holds for every chosen reduced expression. It also holds for every homotopy-equivalent representative, including a minimal one. This proof does not need the separate theorem identifying different reduced expressions canonically as Rouquier complexes.

#### 8.9.2. Adjacent simple-reflection pairs in a compatible order

Fix \(s\in S\), and let \(L_s=\{a:sa>a\}\). Each left \(\langle s\rangle\)-orbit has its unique lower label \(a\in L_s\), followed by its upper label \(sa\).

The map \(\pi_s(u)=\min(u,su)\) is Bruhat monotone. To check it, take \(u\le v\). If \(sv>v\), then \(\pi_s(u)\le u\le v=\pi_s(v)\). If \(sv<v\) and \(su>u\), the simple lifting property gives \(u\le sv\). If \(sv<v\) and \(su<u\), its other branch gives \(su\le sv\). These are all cases.

Choose a linear extension of the Bruhat order restricted to \(L_s\), and replace each lower label \(a\) by the consecutive pair \(a,sa\). The result is a Bruhat-compatible increasing enumeration of \(W\). Indeed, if \(u<v\), monotonicity puts its two lower representatives in the correct pair order; if those representatives agree, \(u\) is the lower and \(v\) the upper member of that pair. Reversing this enumeration gives a compatible decreasing order with consecutive pairs \(sa,a\).

At every boundary between pairs, the set of labels already listed is stable under left multiplication by \(s\), as is its complement. This stability is the exact property needed in Section 8.9.4. Finite rank zero causes no exception: the statement is immediate for \(W=\{e\}\).

For either graph-flag category, Section 8.7.12 gives the intrinsic flag in the corresponding paired order. If \(A\subset A'\) are two consecutive pair-boundary prefixes, define
\[
 P_{A'/A}(M)=\Gamma_{A'}M/\Gamma_AM.
 \tag{8.143}
\]
This has support in one pair \(\{a,sa\}\). In an increasing order it is an extension with lower graph submodule and upper graph quotient; in a decreasing order it has upper submodule and lower quotient. The single-label pieces recovered from the pair block are naturally the order subquotients \(\gamma_y^\nabla M\) or \(\gamma_y^\Delta M\). To see naturality, use the support-intersection formula on the block and Section 8.7.12's intrinsic reordered flag. No noncanonical choice of a splitting defines these subquotient functors.

#### 8.9.3. Support and freeness under rank-one induction

Write \(T_s(M)=B_s\otimes_RM=R\otimes_{R^s}M(1)\). The induction functor is exact, since \(R\) is free as a right \(R^s\)-module. If \(M\) is right free, then \(T_sM\) is right free: the decomposition \(R=R^s\oplus\alpha_sR^s\) in the first factor expresses the underlying right module as two shifted copies of \(M\).

For a single graph \(R_z\), rank-one induction is the shifted two-graph ring
\[
 T_s(R_z)\cong R(G_z\cup G_{sz})(1).
 \tag{8.144}
\]
One can derive this by changing the left coordinate by \(z\) in \(R\otimes_{R^s}R\); the two branches correspond to the two possible lifts of the \(s\)-invariant left coordinate. It follows by applying exact induction to a graph flag that
\[
 \operatorname{supp}(T_sM)\subseteq G_{A\cup sA}
 \quad\text{if }\operatorname{supp}(M)\subseteq G_A.
 \tag{8.145}
\]
For modules with several labels, this uses their actual flag, not a false assertion that any module supported on a graph union is generically semisimple.

#### 8.9.4. Natural transport of every pair block

Let \(M\) have the increasing or decreasing flag, and let \(A\) be a pair-boundary prefix. Then
\[
 T_s(\Gamma_A M)=\Gamma_A(T_sM)
 \tag{8.146}
\]
as literal submodules under the natural inclusion.

Here is a proof of both inclusions. The quotient \(N=M/\Gamma_AM\) retains the complementary reordered graph flag and is right free. Exact induction gives
\[
 0\longrightarrow T_s(\Gamma_AM)
 \longrightarrow T_sM\longrightarrow T_sN\longrightarrow0.
\]
By (8.145), the first term has only labels in \(A\cup sA=A\), whereas the last has only labels outside \(A\), because the complement is also \(s\)-stable. Hence the first term is contained in \(\Gamma_A(T_sM)\). If an element of \(\Gamma_A(T_sM)\) maps to the last term, its image has all generic components zero: the image must have its labels simultaneously in \(A\) and its complement. Right torsion-freeness of \(T_sN\) makes that image zero before localization. This proves the reverse inclusion. It also excludes a possible spurious submodule supported only on an intersection of two graphs.

Apply (8.146) at the two boundaries \(A,A'\), and use exact induction on their quotient. The resulting isomorphism is natural in \(M\):
\[
 P_{A'/A}(T_sM)\cong T_s(P_{A'/A}M).
 \tag{8.147}
\]
Shifts and the multiplication/natural-unit maps commute with this identification. Therefore, for a complex \(C\) whose terms have the appropriate graph flags,
\[
 P(F_sC)\cong F_sP(C),\qquad
 P(E_sC)\cong E_sP(C)
 \tag{8.148}
\]
as actual complexes, where \(P=P_{A'/A}\). Total differential signs agree because (8.147) is a degree-zero natural isomorphism. This is the complete finite-Weyl provider for the transport imported in LW's proof.

#### 8.9.5. The extension argument for an unselected pair

Let \(P(C)\) be a pair-block complex, with its single-label subcomplex \(L(C)\) and quotient \(U(C)\). Suppose both are contractible as graph-bimodule complexes. Then \(T_sP(C)\) is contractible.

It is essential to restrict the **left** action to \(R^s\) before claiming a splitting of the pair extension. Section 8.7.3 says every degreewise extension entry between \(R_a\) and \(R_{sa}\) is a polynomial multiple of a two-graph extension generator. That generator becomes split upon this restriction: the subring invariant under reflection in the left coordinate restricts isomorphically onto either graph. In coordinates transverse to the wall, the ring is \(\mathbb R[a,b]/(a^2-b^2)\); its left-reflection invariant part is \(\mathbb R[b]\), with the fixed coordinates restored. Thus either quotient branch has an \(R^s\)-right-\(R\) section. Restriction kills every extension class, and finite sums and shifts preserve this conclusion.

Consequently the sequence of restricted complexes
\[
 0\longrightarrow L(C)|_{R^s}\longrightarrow P(C)|_{R^s}
 \longrightarrow U(C)|_{R^s}\longrightarrow0
 \tag{8.149}
\]
is split in every cohomological degree. Both ends remain contractible after restriction. For completeness, choose degreewise splittings and write the middle differential as
\[
 d=\begin{pmatrix}d_L&a\\0&d_U\end{pmatrix},
 \qquad d_La+ad_U=0.
\]
If \(h_L\) is a contraction of \(L\), set \(k=h_La\). Then
\[
 d_Lk-kd_U=a.
\]
The degreewise matrix \(\begin{pmatrix}1&-k\\0&1\end{pmatrix}\) is a chain isomorphism from \(L\oplus U\) to the middle complex. Its inverse is \(\begin{pmatrix}1&k\\0&1\end{pmatrix}\). This proves that the restricted middle complex is contractible using grading-preserving maps. Inducing its contraction proves that \(T_sP(C)\) is contractible as a full \(R\)-bimodule complex.

This does **not** assert that \(P(C)\) was contractible before restriction. To obtain what is needed, apply a single-label subquotient functor to the mapping-cone description of \(F_sP(C)\) or \(E_sP(C)\). Every such functor is additive, so it preserves homotopies, cones, and shifts. Its induced \(T_sP(C)\) term is contractible by the argument above, and its induced \(P(C)\) term is \(L(C)\) or \(U(C)\), also contractible. The cone is therefore contractible. This proves that both single-label pieces of \(F_sP(C)\) and \(E_sP(C)\) vanish in the homotopy category.

#### 8.9.6. Explicit selected-pair calculations and all grading shifts

Suppose \(x=sz\), with \(\ell(x)=m=\ell(z)+1\). The selected pair is \(\{z,x\}\). Put \(U_{z,x}=R(G_z\cup G_x)\). The graph ring has the two actual branch sequences
\[
 0\to R_x(-2)\to U_{z,x}\xrightarrow{\mathrm{res}_z}R_z\to0,
 \qquad
 0\to R_z(-2)\to U_{z,x}\xrightarrow{\mathrm{res}_x}R_x\to0.
 \tag{8.150}
\]

For the positive complex, the selected induction block of \(F_z\) is \(R_z(-(m-1))[0]\) up to homotopy. Tensoring on the left with \(F_s\) gives
\[
 [\,U_{z,x}(2-m)\xrightarrow{\mathrm{res}_z}R_z(2-m)\,]
 \quad\text{in degrees }0,1.
 \tag{8.151}
\]
Its decreasing upper \(x\)-piece is \(R_x(-m)[0]\), because the first kernel in (8.150) has degree shift \(-2+(2-m)=-m\). Its lower \(z\)-piece is the identity complex
\[
 [\,R_z(2-m)\xrightarrow{1}R_z(2-m)\,]
\]
in degrees \(0,1\), hence contractible.

For the negative complex the selected induction block of \(E_z\) is \(R_z(m-1)[0]\). Tensoring on the left with \(E_s\) gives
\[
 [\,R_z(m-2)\xrightarrow{\eta}U_{z,x}(m)\,]
 \quad\text{in degrees }-1,0.
 \tag{8.152}
\]
The map is the inclusion of the second kernel in (8.150), after shifting. In the rank-one coordinate it is the nonzero scalar multiple of \(a+b\) prescribed by \(\eta_s\); it vanishes on the upper branch and identifies the lower supported module. Thus its increasing lower \(z\)-piece is the identity complex \(R_z(m-2)\to R_z(m-2)\), and its upper \(x\)-piece is \(R_x(m)[0]\). The factor \(1/2\) changes neither the kernel identification nor the contraction.

These are the complete calculations. The surviving term is in cohomological degree zero in each case; no unrecorded homological shift is used.

#### 8.9.7. Induction for every label

For \(w=e\), both complexes are \(R_e[0]\), so (8.142) is immediate. Now take a nonempty reduced expression \(x=sz\), with \(m=\ell(x)\), and assume (8.142) for its reduced suffix \(z\).

Every term of \(F_z\) and \(E_z\) has both graph flags. This follows from Sections 8.7.7–8.7.9, since the terms are sums of shifted Bott–Samelson objects. Its graph labels are subwords of the reduced expression for \(z\), hence are Bruhat-below \(z\). This support assertion follows either successively from (8.145) or by expanding the tensor-product terms into choices of a graph branch at each factor. It does not require a statement about an indecomposable character.

For the selected pair \(\{z,x\}\), the \(x\)-graph is absent from every term, because \(x>z\). Its pair block is therefore naturally its single \(z\)-piece. By the induction hypothesis this is \(R_z(-(m-1))[0]\) for \(F_z\), and \(R_z(m-1)[0]\) for \(E_z\). The natural block transport (8.148), preservation of homotopies under tensoring, and the calculations (8.151)–(8.152) prove the desired assertion for \(y=z,x\).

For any other pair, its two single-label pieces in \(F_z\) are contractible by the induction hypothesis; the same is true of its two pieces in \(E_z\). Section 8.9.5 proves that both single-label pieces after tensoring with the corresponding rank-one complex are contractible. Natural block transport (8.148), followed by the intrinsic identifications in Section 8.9.2, identifies these with the required order pieces of \(F_x\) and \(E_x\).

All labels belong to one of these pairs, which completes the induction. Neither this induction nor its input list contains the KL character theorem, its positivity conclusion, or Hodge induction.

If a contractible direct summand is removed from a tensor-product complex, every order subquotient of that summand remains contractible, because its contracting homotopy is taken by an additive functor to a contracting homotopy. Thus (8.142) descends to a minimal representative using Section 8.7.5. It is not necessary to commute a support functor with passage to cohomology.

#### 8.9.8. Ordinary cohomology and the statement used in EW §6.4

There is also an entirely elementary, separate assertion:
\[
 H^i(F_{\underline w})=\delta_{i0}R_w(-m),\qquad
 H^i(E_{\underline w})=\delta_{i0}R_w(m).
 \tag{8.153}
\]
For one factor, this is (8.150): multiplication has the \(s\)-graph kernel \(R_s(-1)\), and the negative differential has cokernel \(R_s(1)\). Each term is free on both sides. Tensoring either rank-one exact sequence with a further complex of such terms preserves exactness term by term. The bounded double-complex filtration therefore reduces its cohomology to the tensor product of the graph cohomology terms. Induction and \(R_aR_b=R_{ab}\) prove (8.153).

The positive complex is also homotopy equivalent to \(R(-m)[0]\) as a complex of graded **right modules**. One may see this inductively: its rank-one multiplication sequence is split on the right, and its kernel is right free of rank one. A right-linear contraction of \(F_s\) onto \(R_s(-1)\) can be tensored on the right with the remaining factors. The resulting graph-twisted factor is still a rank-one right module, so its tensor product has the same underlying right-module homotopy type as the remaining complex, with shift \(-1\). Alternatively, (8.153) and bounded projective terms permit splitting successive boundary sequences from the right end, and the projective rank-one cohomology permits the final split.

Right augmentation to \(\mathbb R=R/R_{>0}\) preserves this actual contraction. Hence
\[
 H^i(F_{\underline w}\otimes_R\mathbb R)
 =\begin{cases}\mathbb R(-m)&i=0,\\0&i\ne0.\end{cases}
 \tag{8.154}
\]
It is the right-module splitting that justifies this specialization; exactness of an arbitrary specialized complex would not suffice. Removal of contractible bimodule summands again preserves it. This proves the provider corresponding to EW Lemma 6.4.

### 8.10. Descent along a right simple invariant ring

For $xs<x$, this section constructs a graded $(R,R^s)$-bimodule $N_x$ with $N_x\otimes_{R^s}R\cong B_x$, with no extra shift, and retains the middle-action coordinates. Compare [Williamson, *Singular Soergel bimodules*, arXiv:1010.1283v2, introduction and §7.4](https://arxiv.org/abs/1010.1283v2). The [v3 erratum](https://arxiv.org/abs/1010.1283v3) corrects the general left-singular character normalization by the length of $w_I$; here $I=\varnothing$ and that correction is zero. The proof uses actual modules and flags, with neither the erroneous general character-composition formula nor a singular canonical-character theorem as an input.

#### 8.10.1. Exact foundation inputs

Let \(W\) be a finite Weyl group acting on its real reflection representation \(V\), optionally with an additional trivial summand. Put
\[
 R=\operatorname{Sym}_{\mathbb R}(V^*),\qquad \deg V^*=2,\qquad
 M(n)^i=M^{i+n}.
 \tag{8.155}
\]
Let \(\mathcal B\) be the graded additive, idempotent-complete category generated by the Bott–Samelson bimodules
\[
 B_s=R\otimes_{R^s}R(1).
 \tag{8.156}
\]
The graph module \(R_y\) has underlying right module \(R\), with left action \(f\cdot g=f(y\xi)g(\xi)\). Its descending standard is \(R_y(-\ell(y))\); its ascending standard is \(R_y(\ell(y))\).

The internal foundation providers in Section 8.7 are:

1. **Elementary Sections 8.7.1–8.7.5:** reflection faithfulness, graded Krull–Schmidt decomposition and cancellation, the local degree-zero endomorphism lemma (an endomorphism of an indecomposable is either invertible or nilpotent), freeness of finite graded projectives over the relevant polynomial ring, graph Ext calculation, rank-one Frobenius extension and the two-branch graph sequences.
2. **Support Sections 8.7.6–8.7.10:** actual generic graph support, both support flags for Bott–Samelson objects, and the whole-object Hom formula.
3. **Classification Section 8.7.12/Section 8.7.15/Section 8.7.16:** reordering flags by any Bruhat-compatible linear extension; the Hom formula and degreewise lifting for arbitrary summands; regular classification, support of \(B_y\) in \(\{z:z\le y\}\), and top ascending quotient \(R_y(\ell(y))\).
4. **Finite Coxeter combinatorics:** exchange, reduced-subword Bruhat order, and its right lifting property, proved in Sections 8.2 and 8.7. The particular coset consequences needed here are proved in Section 8.10.2.

#### 8.10.2. The entire finite Bruhat order and its two-element cosets

Fix \(s\in S\) and put \(A=R^s\). A coset \(p\in W/W_s\) has exactly two elements
\[
 a=p_-,\qquad q=p_+=as,\qquad a<q,\qquad h_p=\ell(q)=\ell(a)+1.
 \tag{8.157}
\]
Order the cosets by \(p\le p'\) if \(p_-\le p'_-\). This also means \(p_+\le p'_+\).

Here are the required order assertions. Write \(\pi:W\to W/W_s\). The right lifting property says that removing a right descent at the upper member of a Bruhat comparison allows a right descent to be removed at its lower member, or leaves a lower right ascent below the shortened upper member. Thus, from \(u\le v\), one gets \(u_-\le v_-\), by considering whether \(us<u\) and \(vs<v\). If \(v\) is a right ascent this follows directly from \(u_-\le u\le v\). If \(v\) is a right descent, the two assertions just stated give the result. Therefore \(\pi\) is order preserving.

For \(a\le b\), both with right ascent \(s\), the right lifting property gives \(as\le bs\). One can also check this directly with subwords: choose a reduced word for \(b\), append \(s\), and append that last letter to a reduced subword for \(a\). It is still reduced because \(as>a\). This proves the equivalence of the two coset-order definitions.

Consequently
\[
 \pi^{-1}(\{p':p'\le p\})=\{y:y\le q\}.
 \tag{8.158}
\]
The forward inclusion follows from \(y\le(\pi y)_+\le q\); the reverse inclusion follows from the monotonicity of \(\pi\). Any linear extension of the coset order, with each pair \(a,q\) kept together and ordered internally by \(a<q\), is therefore a linear extension of regular Bruhat order. Every regular comparison between different pairs projects to the corresponding coset comparison. These facts justify grouped actual support flags, not just formal lists of labels.

#### 8.10.3. Singular graph modules and the induced two-branch module

For \(p=\{a,q\}\), define \(Q_p\) as an \((R,A)\)-bimodule. Its underlying left module is \(R\), with left coordinate \(u\in V\), and
\[
 g(u)\cdot f=g(u)f(q^{-1}u),\qquad f\in A.
 \tag{8.159}
\]
Replacing \(q\) by \(qs=a\) gives the same action because \(f\) is \(s\)-invariant. Restriction of either \(R_q\) or \(R_a\) from right \(R\) to right \(A\) is precisely \(Q_p\). This uses the left-module realization of a regular graph module, so no inverse is missing from (8.159). Its underlying right \(A\)-module is free of rank two: the isomorphism \(q^{-1}:R\to R\) reduces this to the rank-two freeness of \(R\) over \(A\).

Write
\[
 U(N)=N\otimes_A R,\qquad D(M)=\operatorname{Res}_{R-A}(M).
 \tag{8.160}
\]
Induction of \(Q_p\) is the coordinate ring \(E_p\) of the union of the two regular graphs \(G_q\cup G_a\). This assertion has the following explicit algebra proof. Choose normal coordinate \(t=\alpha_s(\xi)/2\) on the right copy of \(V\), and put \(d=\alpha_s(q^{-1}u)/2\) on the left copy. The remaining right coordinates are \(s\)-fixed and equal to their transforms from the left coordinates. Thus
\[
 E_p=U(Q_p)\cong R[t]/(t^2-d^2).
 \tag{8.161}
\]
The two branches are \(t=d\), labelled \(q\), and \(t=-d\), labelled \(a\). The equation has distinct linear factors in characteristic zero, so it gives the reduced union. This is a cyclic \((R,R)\)-bimodule. Its degree-zero bimodule endomorphisms are exactly its degree-zero ring elements, namely \(\mathbb R\). Thus \(E_p\), and every shift of it, is indecomposable.

The ideals \((t-d)\) and \((t+d)\) give both actual graph sequences:
\[
 \begin{aligned}
 0&\longrightarrow R_a(-2)\longrightarrow E_p\longrightarrow R_q\longrightarrow0,\\
 0&\longrightarrow R_q(-2)\longrightarrow E_p\longrightarrow R_a\longrightarrow0.
 \end{aligned}
 \tag{8.162}
\]
For example, the first injection sends a generator to \(t-d\), which has degree two and is annihilated by the equation for the \(a\)-branch. Each quotient is right and left free, so these sequences split as modules over either outer polynomial ring. They are respectively the ascending and descending two-label flags. As an \((R,A)\)-bimodule,
\[
 D(E_p)\cong Q_p\oplus Q_p(-2),
 \tag{8.163}
\]
with left \(R\)-basis \(1,t\). Every \(s\)-invariant right polynomial acts as the same transformed left polynomial on both basis terms, which proves bimodule linearity of this decomposition.

#### 8.10.4. Actual flags under restriction and induction

Call a singular ascending flag a finite actual support flag, ordered by \(W/W_s\), whose layers are finite shifted sums of \(Q_p\). Use the reverse coset order for descending flags. Every such layer is free on the left over \(R\) and on the right over \(A\).

**Restriction.** Let a regular module have an ascending support flag. Section 8.7.12 allows its graph labels to be ordered in the grouped order of §3. A block on \(\{a,q\}\) is an extension of shifted copies of one graph by shifted copies of the other. The rank-one graph Ext calculation from Section 8.7.3 says that every entry of its extension class is a polynomial multiple of the two-branch extension (8.162). Each such entry becomes zero upon right restriction to \(A\).

To verify this last assertion without assuming semisimplicity, use (8.161). The quotient onto the \(q\)-branch has an \((R,A)\)-linear section given by the constant-in-\(t\) left \(R\) submodule. The quotient onto the \(a\)-branch has the same section. Their quotient graph modules become \(Q_p\); the kernel is its indicated degree-two shift. Hence the generating extension restricts to zero, and so does every polynomial multiple, by functoriality of pushout/pullback for Yoneda extension classes. Matrices of these zero classes vanish entrywise. The restricted block is therefore a shifted sum of \(Q_p\)'s. The descending version is identical with the other branch sequence.

These are intrinsic singular support flags. One may use the left fraction field: left freeness makes a module inject into its localization, and the distinct cosets give distinct generic maps \(A\to\operatorname{Frac}(R)\). To check distinctness, use the generators of \(A\): the \(s\)-fixed linear coordinates and the square of the normal linear coordinate. Equality of two transformed maps forces equality on the fixed coordinates; equality of the normal squares, in an integral domain of characteristic zero, forces the normal forms to agree or be negatives. The two transformations therefore differ by identity or by \(s\), and their Weyl labels belong to the same coset, by faithfulness. A selected support submodule is the intersection of the module with the selected generic summands. A constructed flag with free quotient and the correct generic components has exactly that intersection: the omitted components of the quotient cannot vanish after localization without already being zero. This is the left-handed version of Section 8.7.6's torsion-free argument.

**Induction.** The ring \(R\) is free over \(A\), so \(U\) is exact. It sends each singular layer \(Q_p(n)\) to \(E_p(n)\). Refine these layers using the appropriate sequence (8.162). By §3 the resulting regular order is Bruhat compatible. Both induced ascending and descending flags are therefore actual regular support flags. The same intersection argument identifies the actual supports.

In particular, for a module supported on cosets at most \(p\), actual top-coset quotients commute with induction:
\[
 \operatorname{Top}_p(U N)=U(\operatorname{Top}_p N).
 \tag{8.164}
\]
Here the left side retains both graphs \(a,q\), and is a quotient by the lower-coset support; it is not just the individual \(q\)-graph quotient. More generally, restriction identifies the grouped regular support quotient with its singular support quotient. This follows by applying the exact functor to the flag sequence, using its free quotient and the generic-component intersection test just proved.

All these assertions survive direct summands. Actual support functors commute with direct sums and idempotents. A direct summand of a shifted sum of \(Q_p\) is a finite graded projective over its graph ring \(R\), hence is graded free by Section 8.7.2 and is again a shifted sum of \(Q_p\)'s.

#### 8.10.5. The one-sided singular category and its Hom lifting

Define
\[
 \mathcal S_s=\operatorname{Kar}\operatorname{add}\{D(B)(n):B\in\mathcal B,\ n\in\mathbb Z\}.
 \tag{8.165}
\]
Every object has both singular support flags by Section 8.10.4. It is finitely generated over the nonnegative graded algebra \(R\otimes A\); its degree-zero Hom spaces are finite dimensional. Section 8.7.2 applies to this algebra as well, giving finite indecomposable decompositions, local degree-zero endomorphism algebras, the unit-or-nilpotent assertion and cancellation. The assertion uses finite-dimensional degree-zero endomorphism algebras, not an unproved degreewise positivity theorem.

Induction sends \(\mathcal S_s\) into \(\mathcal B\), since
\[
 U D(B)=B\otimes_A R=B B_s(-1).
 \tag{8.166}
\]
This equality needs no descent hypothesis. Induction and restriction preserve sums, shifts and split idempotents. Restriction is faithful and detects zero objects because it changes only an action, not the underlying module.

Here is the needed singular Hom lifting derived from the regular one. The Frobenius trace
\[
 \partial_s(f)=\frac{f-sf}{\alpha_s}
 \tag{8.167}
\]
has degree \(-2\). The basis \(1,\alpha_s/2\) of \(R\) over \(A\) has trace-pairing matrix
\[
 \begin{pmatrix}0&1\\1&0\end{pmatrix}.
 \tag{8.168}
\]
Thus \(r\mapsto[z\mapsto\partial_s(rz)]\) gives
\[
 \operatorname{Hom}_A(R,A)\cong R(2).
 \tag{8.169}
\]
Ordinary tensor–Hom adjunction and this perfect pairing give
\[
 \begin{aligned}
 \operatorname{Hom}_{R-R}(U N,B)&\cong\operatorname{Hom}_{R-A}(N,D B),\\
 \operatorname{Hom}_{R-A}(D B,N)&\cong\operatorname{Hom}_{R-R}(B,U N(2)).
 \end{aligned}
 \tag{8.170}
\]
These are graded isomorphisms, with all outer actions respected. The second is the coinduction adjunction; its \(+2\) is fixed by (8.167)–(8.169).

The regular Hom formula Section 8.7.15 implies exactness of \(\operatorname{Hom}(B,-)\) on any short exact sequence of ascending-flag modules whose flags and multiplicities add. Here is the duality link to the formula stated with descending source and target in \(\mathcal B\). All graph-flag sequences are right-module split, so graded right-free duality is exact; it exchanges ascending and descending flags by Section 8.7.9 and preserves \(\mathcal B\). The classification gives \(D_{\mathrm{gr}}B_y(n)\cong B_y(-n)\). Thus \(\operatorname{Hom}(B,N)\cong\operatorname{Hom}(D_{\mathrm{gr}}N,D_{\mathrm{gr}}B)\) transfers the descending contravariant formula and lifting to the asserted ascending covariant version, with the same grading under this Hom identification. This graded duality is distinct from the restriction functor \(D\) in (8.160). To see that exactness also applies to a quotient containing several graph layers, rather than just one final layer, compare graded Hilbert series using that dual Section 8.7.15 formula for all three terms. Left exactness leaves a possible cokernel at the final term. Additivity of the free graded Hom numerators says that cokernel has zero dimension in every degree, hence is zero. All degree pieces are finite dimensional. This is actual surjectivity, not a generic-rank argument. The contravariant descending version follows in the same way.

Apply \(U\) to a singular ascending-flag short exact sequence. Section 8.10.4 provides regular ascending flags with additive multiplicities. (8.170) and Section 8.7.15 therefore make \(\operatorname{Hom}(D B,-)\) exact on this sequence. If \(C\) is a summand of \(D B\), project to that summand; this yields
\[
 \operatorname{Hom}_{R-A}(C,-)\text{ is exact on these singular ascending-flag sequences}
 \quad(C\in\mathcal S_s).
 \tag{8.171}
\]
The first adjunction similarly gives the contravariant descending assertion. No general singular Hom formula or singular Schur-algebroid character theorem is needed.

If \(p\) is a maximal support coset of \(N\), a linear extension can place it last. Its quotient sequence
\[
 0\longrightarrow\Gamma_{\ne p}N\longrightarrow N
 \longrightarrow\operatorname{Top}_p N\longrightarrow0
 \tag{8.172}
\]
has a singular ascending-flag kernel, so (8.171) lifts every homogeneous map from any \(C\in\mathcal S_s\) to that quotient. A map from \(C\) to a \(Q_p\)-supported module kills all other generic support components, and thus factors through \(\operatorname{Top}_p C\) whenever \(p\) is maximal for \(C\). Indeed its values on the other components vanish after left fraction-field localization, and the target is left torsion-free. Therefore all maps between the two top quotients lift, in either direction.

#### 8.10.6. Classification needed for the cancellation argument

**Lemma 8.16 (singular classification).** For each \(p\in W/W_s\), there is a unique indecomposable \(C_p\in\mathcal S_s\) supported on \(\{p'\le p\}\), with
\[
 \operatorname{Top}_p C_p=Q_p(h_p).
 \tag{8.173}
\]
Every singular indecomposable is exactly one \(C_p(n)\).

**Existence.** Take \(a=p_-\). Regular \(B_a\) has support at most \(a\) and ascending top quotient \(R_a(\ell(a))\). The module \(D(B_a)(1)\) is supported on cosets at most \(p\), by (8.158), and its top quotient is \(Q_p(\ell(a)+1)=Q_p(h_p)\). No other regular label at most \(a\) belongs to \(p\), because the other label \(q\) is strictly larger than \(a\). In its finite indecomposable decomposition, nonnegative layer multiplicities select exactly one summand with nonzero \(p\)-layer. Call it \(C_p\). Its top quotient is exactly (8.173).

**Classification and uniqueness.** Let \(M\) be any singular indecomposable and choose a maximal support coset \(p\). Its top layer is a finite shifted free sum of \(Q_p\)'s. Choose a homogeneous basis summand and choose the unique shift \(n\) making it agree with the single top summand of \(C_p(n)\). There are degree-zero top maps
\[
 \alpha:\operatorname{Top}_p M\to\operatorname{Top}_p C_p(n),
 \qquad
 \beta:\operatorname{Top}_p C_p(n)\to\operatorname{Top}_p M
 \tag{8.174}
\]
given by projection onto that summand and its inclusion. Then \(\beta\alpha\) is identity on that nonzero summand and zero on the others. Both maps lift by §6 to \(f:M\to C_p(n)\), \(g:C_p(n)\to M\). The composite \(gf\) induces this projection on the top layer; no positive power is zero. It is a nonnilpotent degree-zero endomorphism of indecomposable \(M\), hence is a unit by Section 8.7.2.

Its induced top map must consequently be invertible. A projection onto a proper free summand is not invertible, so the top layer in fact has rank one. Normalize one of the maps by \((gf)^{-1}\). The resulting maps split \(M\) as a summand of \(C_p(n)\). Since both objects are indecomposable, they are isomorphic. This also rules out any additional incomparable maximal coset of \(M\). Applying the same argument to another candidate for \(C_p\) proves uniqueness.

Different \(p\)'s have different maximal support; for a fixed \(p\), different \(n\)'s have different nonzero top generator degree. Thus there is no ambiguity in labels or shifts. This proof is the required one-sided singular classification, derived from the regular foundations instead of importing its full double-coset version.

#### 8.10.7. Strong descent by top-block indecomposability and cancellation

**Theorem 8.9 (actual right-singular descent).** For \(p=\{a,q\}\) as in (8.157),
\[
 U(C_p)\cong B_q,\qquad
 D(B_q)\cong C_p\oplus C_p(-2).
 \tag{8.175}
\]

**Proof.** By (8.164) and (8.173), the actual top-coset block of \(U(C_p)\) is
\[
 E_p(h_p).
 \tag{8.176}
\]
The module \(U(C_p)\) belongs to \(\mathcal B\) by (8.166) and is supported in \(\{y\le q\}\) by (8.158). The ascending sequence (8.162) shows that its individual top \(q\)-graph quotient is \(R_q(h_p)=R_q(\ell(q))\), with multiplicity one and no extra shift. The regular classification Section 8.7.16 therefore gives an actual decomposition
\[
 U(C_p)\cong B_q\oplus M
 \tag{8.177}
\]
with all labels of \(M\) strictly below \(q\).

It is crucial to use (8.176), not merely its \(q\)-graph multiplicity. That entire two-graph block is indecomposable by (8.161). Support quotients commute with the direct sum (8.177). The block from \(B_q\) is nonzero because it contains the \(q\)-graph. Hence the block from \(M\) is zero, and the whole block (8.176) belongs to \(B_q\). In particular \(M\) contains no residual summand \(B_a(n)\) in this coset. All its support cosets are strictly below \(p\).

Restrict (8.177). Independently, the rank-two invariant decomposition gives
\[
 D U(C_p)\cong C_p\oplus C_p(-2).
 \tag{8.178}
\]
The top singular quotient of \(D(B_q)\) is, by (8.163) and (8.176),
\[
 Q_p(h_p)\oplus Q_p(h_p-2).
 \tag{8.179}
\]
Apply the independently proved singular classification §7. Its actual nonnegative top multiplicities force
\[
 D(B_q)\cong C_p\oplus C_p(-2)\oplus N
 \tag{8.180}
\]
where \(N\) has only lower coset labels. Equations (8.177)–(8.180) combine into
\[
 C_p\oplus C_p(-2)
 \cong C_p\oplus C_p(-2)\oplus N\oplus D(M).
 \tag{8.181}
\]
Graded Krull–Schmidt cancellation gives \(N\oplus D(M)=0\). Therefore \(N=0\) and \(D(M)=0\). Faithfulness of restriction gives \(M=0\). This proves both assertions of (8.175). \(\square\)

For any \(x\in W\) with \(xs<x\), take \(p=xW_s\); then \(q=x\). Defining
\[
 \overline B_x=C_{xW_s}
 \tag{8.182}
\]
proves Theorem 8.9 at its full finite-Weyl scope, with no grading correction. This is the \(I=\varnothing,J=\{s\}\) instance of Williamson's native induction theorem. The construction did not assume \(B_x\) descends and did not assume the decomposition that descent will imply.

#### 8.10.8. The weaker splitting and the controlled basis used in the Hodge induction

Now, and only now, apply Theorem 8.9:
\[
 \begin{aligned}
 B_xB_s
 &\cong C_p\otimes_A R\otimes_A R(1)\\
 &\cong B_x(1)\oplus B_x(-1).
 \end{aligned}
 \tag{8.183}
\]
The splitting uses the **middle** \(R\) as an \((A,A)\)-bimodule, with basis \(1,\alpha_s/2\). Its two injections send \(c\otimes r\) to \(c\otimes1\otimes r\) and \(c\otimes\alpha_s/2\otimes r\). Its projections on the middle factor are
\[
 \pi_1(f)=\frac{f+sf}{2},\qquad \pi_2(f)=\partial_s(f).
 \tag{8.184}
\]
These identities hold before any right augmentation and respect both outer \(R\)-actions. They supply the particular splitting required to compute the Lefschetz matrix, rather than an abstract existence of two isomorphic summands.

For a linear form \(\rho\in V^*\), set
\[
 b=\alpha_s/2,\qquad
 a_\rho=(\rho+s\rho)/2\in A,\qquad
 c_\rho=\partial_s\rho=\rho(\alpha_s^\vee)\in\mathbb R.
 \tag{8.185}
\]
Multiplication by \(\rho=a_\rho+c_\rho b\) on the middle factor has matrix
\[
 \begin{pmatrix}
 a_\rho&c_\rho\alpha_s^2/4\\
 c_\rho&a_\rho
 \end{pmatrix}
 \tag{8.186}
\]
in the ordered basis \(1,b\). After tensoring the final right \(R\) with the augmentation \(R/R^{>0}\), the positive-degree invariant coefficients \(a_\rho,\alpha_s^2/4\) act by zero. Thus, on \(\overline{B_xB_s}=\overline B_x^{\,\mathrm{reg}}(1)\oplus\overline B_x^{\,\mathrm{reg}}(-1)\), the operator that is left multiplication by \(\rho\) plus \(\zeta\) times this internal middle multiplication has matrix
\[
 \begin{pmatrix}
 L&0\\
 \zeta c_\rho&L
 \end{pmatrix}.
 \tag{8.187}
\]
Here \(\overline B_x^{\,\mathrm{reg}}=B_x\otimes_R R/R^{>0}\), while the unadorned \(C_p=\overline B_x\) in (8.182) denotes the singular bimodule. The notations refer to different objects and must not be conflated. \(L\) is left multiplication by \(\rho\) on the regular augmentation. (8.187) is degree two under the shifts (8.183). For dominant \(\rho\), \(c_\rho>0\), and \(\zeta>0\) supplies the coefficient in the cited descending case.

The remaining linear-algebra hard-Lefschetz step, and any Hodge–Riemann input to the surrounding induction, are outside this descent lemma. (8.187) provides their exact algebraic input and checks the root sign and both shifts.

### 8.11. The finite-Weyl Hodge and character induction

The following proof expands the finite-Weyl argument of [Elias–Williamson, *The Hodge theory of Soergel bimodules*, arXiv:1212.0791v2, §§4–6](https://arxiv.org/html/1212.0791v2). All needed bimodule, support, descent and finite-linear-algebra constructions have been supplied in Sections 8.7–8.10.

#### 8.11.1. Scope, conventions and actual providers

Let \(W\) be a finite Weyl group on its real reflection representation \(V\), and let \(S\) be its simple reflections. Put \(R=\operatorname{Sym}(V^*)\), with linear functions in degree two, \(\mathfrak m=R_{>0}\), and \(\overline M=M/M\mathfrak m\). Shifts mean \(M(k)^i=M^{i+k}\). Choose \(\rho\in V^*\) with \(\rho(\alpha_s^\vee)>0\) for every \(s\). The coefficient variable in the bimodule proof is \(u\); the lesson variable is \(v\), and throughout
\[
u=v^{-1},\qquad q=v^2=u^{-2},\qquad
H_s^2=1+(u^{-1}-u)H_s,\qquad C_s=H_s+u.
\tag{8.188}
\]
Write \(C_x=H_x+\sum_{y<x}h_{y,x}(u)H_y\) for the bar-invariant canonical basis with \(h_{y,x}\in u\mathbb Z[u]\). The integral construction and uniqueness of this basis are actual internal providers in RT-LIE-18 §8.1–8.4, not positivity assumptions. The Hecke pairing has orthonormal basis \(H_x\).

The category \(\mathcal B\) is the additive idempotent closure of shifted tensors of \(B_s=R\otimes_{R^s}R(1)\). The following internal proofs supply the prerequisites:

* Sections 8.7.1–8.7.5: finite-Weyl reflection faithfulness; graded decomposition, cancellation and freeness; graph Ext; rank-one Frobenius adjunction and duality; minimal complexes and lifting through their finite-dimensional radical.
* Sections 8.7.6–8.7.11: actual support filtrations, both characters and rank-one character transport; whole-object Hom; in particular (8.111), the right-module split inclusion \(\Gamma_yB\hookrightarrow B\).
* Sections 8.7.12–8.7.17: refined free graph layers; exact multiplication by \(p_y\); arbitrary-summand Hom and Hom lifting; classification \(B_x(k)\), self-duality \(DB_x\cong B_x\), and bar-invariant characters with top term \(H_x\). The residue field of \(\operatorname{End}^0(B_x)\) is \(\mathbb R\), even before its full endomorphism algebra becomes one-dimensional.
* Lemmas 8.10–8.15: primitive decomposition, continuous signatures, balanced invariant subspaces, the degree-one injective-map lemma, displaced-centre vanishing, and the large-parameter Gram calculation. Section 8.11.2 below verifies the actual bimodule hypotheses of 8.15.

Character multiplication at arbitrary-summand scope follows from these actual providers and needs no additional categorification theorem. A reduced Bott–Samelson object for \(x\) decomposes as \(B_x\) once plus shifts of labels below \(x\). Induction on length therefore expresses every class \([B_x]\) as an integral Laurent combination of whole-word classes. For any \(B\), repeated left transport (8.104) gives
\(\operatorname{ch}(BS(\mathbf a)B)=C_{a_1}\cdots C_{a_k}\operatorname{ch}B\).
Extend this equality along that integral class expression for \(A\). It gives
\(\operatorname{ch}(AB)=\operatorname{ch}A\,\operatorname{ch}B\).
Classification makes the characters unitriangular, so all class manipulations are faithful. This proves in particular the right product rule for \(B_xB_s\) used below from the already supplied left transport.

Two further assertions are proved in Sections 8.9–8.10. Their displayed statements keep the exact interfaces used below.

**Provider RΔ (support-graded splitting).** For every reduced word \(\mathbf x\) for \(x\), let \(T_{\mathbf x}=\bigotimes_i[B_{s_i}\xrightarrow{\mu}R(1)]\), each factor in cohomological degrees \(0,1\), and let \(F_{\mathbf x}\) be a minimal direct-summand complex. For every \(y\), the support-layer complex
\[
\Gamma_{\ge y/>y}F_{\mathbf x}
\quad\text{is homotopy equivalent, as a graded bimodule complex, to}\quad
\begin{cases}\Delta_x,&y=x,\\0,&y\ne x,\end{cases}
\tag{8.189}
\]
where \(\Delta_x=R_x(-\ell(x))\). The actual provider is Sections 8.9.2–8.9.7. It orders the labels in consecutive left-simple pairs, proves natural support-prefix transport by exact induction and torsion-free complementary flags, and splits each two-graph extension after restricting the left action to \(R^s\). For an unselected pair, its two contractible single-label complexes have a degreewise split extension after restriction; the explicit off-diagonal conjugation in Section 8.9.5 contracts the extension, and induction plus the rank-one cone contracts both resulting layers. For the selected pair in \(x=sz\), the complex is
\([R(G_z\cup G_x)(2-\ell(x))\to R_z(2-\ell(x))]\);
its upper kernel is exactly \(R_x(-\ell(x))\), and its lower layer is an identity complex. This proves (8.189) by length induction before augmentation, and additive support functors preserve the contracting homotopies removed in a minimal representative. This is the precise proof interface corresponding to EW Proposition 6.8 and Libedinsky–Williamson Proposition 3.7, with their imported pair transport proved inside the provider.

**Provider Rs (descent induction).** If \(xs<x\), there exists a graded \((R,R^s)\)-bimodule \(N_x\) with
\[
B_x\cong N_x\otimes_{R^s}R.
\tag{8.190}
\]
The actual provider is Sections 8.10.2–8.10.7. Its one-sided singular category is the summand closure of regular objects restricted to \(R^s\). Actual grouped flags and the Frobenius adjunction with coinduction shift \(+2\) transfer Hom lifting; lifting top-coset projections then classifies its indecomposables \(C_p\). Inducing \(C_p\) for \(p=\{xs,x\}\) has the indecomposable entire two-graph top block \(R(G_{xs}\cup G_x)(\ell(x))\), so any complement to \(B_x\) has only lower cosets. Restriction gives \(C_p\oplus C_p(-2)\). Singular classification forces both of these top summands already inside the restricted \(B_x\), and Krull–Schmidt cancellation plus faithful restriction kills the proposed lower complement. Thus \(N_x=C_p\) gives (8.190) with no additional shift. (8.183)–(8.187) supply the controlled middle basis \(1,\alpha_s/2\), its actual outer-action compatibility and exactly the operator matrix in Section 8.11.7.1. This is the finite right-simple specialization of Williamson's theorem invoked in EW Theorem 6.19; it uses no singular canonical-character identity.

Global braid independence of Rouquier complexes and their monoidal invertibility are not assumptions of the proof below. We work with a specified reduced word, and make the descent cancellation directly from (8.190). Section 8.11.4 proves the needed cohomology directly from the rank-one graph sequence.

The conclusion from these internal providers is \(\operatorname{ch}B_x=C_x\), hard Lefschetz and the standard Hodge signs for every \(x\), and coefficient positivity of the finite-Weyl KL polynomials. Section 8.11.8 gives the induction with no geometric theorem assumed.

#### 8.11.2. Actual rank-one forms and the large parameter

For \(s\), normalize \(s\alpha_s=-\alpha_s\) and \(\alpha_s(\alpha_s^\vee)=2\). Put
\[
c_0=1\otimes1,\qquad c_1=\tfrac12(\alpha_s\otimes1+1\otimes\alpha_s),\qquad
\partial_s f=(f-sf)/\alpha_s.
\]
The decomposition \(R=R^s\oplus(\alpha_s/2)R^s\) shows that \(c_0,c_1\) are a right basis, in degrees \(-1,1\). Direct substitution gives
\[
r c_1=c_1r,\qquad r c_0=c_0(sr)+c_1\partial_s r,\qquad c_1^2=c_1\alpha_s.
\tag{8.191}
\]
These are identities in the tensor algebra; they require no indecomposable character theorem.

Suppose \(B\) is right free and has a nondegenerate graded symmetric invariant \(R\)-valued form \(b\). Use \(BB_s=B\otimes_{R^s}R(1)\), and define its form on elementary tensors by
\[
\widetilde b(b_0\otimes r,b_1\otimes r')=rr'\,\partial_s b(b_0,b_1).
\tag{8.192}
\]
The balancing relation holds because \(\partial_s(af)=a\partial_s f\) for \(a\in R^s\). Symmetry and right \(R\)-linearity are immediate; moving a left scalar through the form uses the invariance of \(b\). The degree of \(\partial_s\), namely \(-2\), is exactly compensated by the two shifts \(+1\). Thus (8.192) is a graded invariant form.

For the maps \(a(b)=bc_0\) and \(t(b)=bc_1\), expansion of \(c_1\) in (8.192) yields
\[
\begin{aligned}
\widetilde b(a b,a b')&=\partial_s b(b,b'),\\
\widetilde b(a b,t b')&=\widetilde b(t b,a b')=b(b,b'),\\
\widetilde b(t b,t b')&=\alpha_s b(b,b').
\end{aligned}
\tag{8.193}
\]
For example the middle equation is
\(\tfrac12\partial_s(\alpha_s f)+\tfrac12\alpha_s\partial_s f=f\);
the last is obtained by expanding both copies of \(c_1\). If \(e_j,e_j^*\) are dual right bases of \(B\), the right bases \(a(e_j),t(e_j)\) and \(t(e_j^*),a(e_j^*)\) give a block triangular pairing matrix with diagonal identity blocks. It is invertible over \(R\). Hence the induced form is nondegenerate. Iteration from the multiplication form on \(R\) constructs nondegenerate Bott–Samelson forms. On the commutative iterated tensor ring, they equal extraction of the coefficient of the all-\(c_1\) tensor in a product: this follows inductively from (8.193) and \(c_1^2=c_1\alpha_s\). Consequently restriction to a summand and then induction agree with restriction from the enlarged Bott–Samelson object.

On \(\overline{BB_s}\), set \(L=\rho\) on the left of \(B\), \(K=1_B\otimes(\rho\text{ on the left of }B_s)\), and \(L_\zeta=L+\zeta K\). The invariant form makes both operators self-adjoint, and they commute. Equation (8.191), after killing positive-degree right scalars, gives
\[
K(a b)=c\,t(b),\qquad K(t b)=0,\qquad K^2=0,\qquad c=\rho(\alpha_s^\vee)>0.
\tag{8.194}
\]
The map \(a\) is not being claimed to descend canonically from \(\overline B\); its values on selected homogeneous lifts are used. Equation (8.194) is an identity on the actual quotient for those lifts.

Choose homogeneous lifts of a real homogeneous basis of \(\overline B\). They form a right basis by graded Nakayama and freeness. Their \(a\)- and \(t\)-images form a right basis of \(BB_s\), so
\(\dim\overline{BB_s}^{m}=\dim\overline B^{m+1}+\dim\overline B^{m-1}\).
In degree \(-i\), (8.193)–(8.194) give
\[
\begin{aligned}
F_{i,\zeta}(t y,t y')&=0,\\
F_{i,\zeta}(a x,t y)&=b_{\overline B}(x,L^iy),\\
F_{i,\zeta}(a p,a q)
 &=F_{i,0}(a p,a q)+\zeta i c\,b_{\overline B}(p,L^{i-1}q),
\end{aligned}
\tag{8.195}
\]
where \(F_{i,\zeta}(z,z')=\widetilde b(z,L_\zeta^iz')\), \(i\ge1\) in the last formula, and \(p,q\) are lifts of primitives in \(\overline B^{-i+1}\). Indeed \(K^2=0\) gives \(L_\zeta^i=L^i+i\zeta L^{i-1}K\); the other equations follow because \(K t=0\) and the \(t,t\) pairing has a positive-degree right factor. These are precisely the actual hypotheses of Lemma 8.15, now proved rather than postulated.

Therefore, if \(\overline B\) has hard Lefschetz and the Hodge signs with lowest degree \(-n\), \(\overline{BB_s}\) has hard Lefschetz and the signs with lowest degree \(-n-1\), for sufficiently large \(\zeta\). The uniform choice of a large parameter uses only finitely many nonzero degrees. The matrix proof and its telescoping sign calculation are Lemma 8.15; no determinant estimate on the other Gram blocks is required. Once hard Lefschetz is proved along a connected parameter interval, Lemma 8.11 carries these signs along the interval.

##### 8.11.2.1. Positive normalization on the bottom degree

For a reduced word \(\mathbf x=s_1\cdots s_m\), let \(c_{\mathrm{bot}}\) be its all-\(c_0\) tensor. Moving \(\rho\) through the factors by (8.191) gives
\[
\rho=\sum_{i=1}^m\gamma_i\chi_i\phi_i+\text{right multiplication by }x^{-1}\rho,\qquad
\gamma_i=(s_{i-1}\cdots s_1\rho)(\alpha_{s_i}^\vee)>0.
\tag{8.196}
\]
Here \(\phi_i\) multiplies away the \(i\)-th factor, and \(\chi_i\) inserts \(c_1\). Positivity of \(\gamma_i\) is the root-sign criterion for reduced prefixes, supplied by the actual finite-Weyl exchange/root provider. The right scalar disappears in the quotient.

The quotient of \(B_z\), as a summand of a reduced word of length \(\ell(z)\), is supported in degrees \([-\ell(z),\ell(z)]\); therefore \(\rho^{\ell(z)+1}=0\) on it, without a character conjecture. A nonreduced word of length \(k\) has all its indecomposable labels of length strictly below \(k\), since every standard character label is a product of a subword and none has length \(k\). Thus \(\rho^k\) kills its quotient, independently of shifts of its summands.

Induct on \(m\) in (8.196). If the deletion word is reduced, its bottom vector is taken by \(\rho^{m-1}\) to a positive multiple of its top vector, by induction. Insertion carries that top vector to the top vector of \(\mathbf x\). If the deletion word is not reduced, its contribution is zero by the previous paragraph. At least deletion of the last letter is reduced. The sum of the positive surviving contributions is positive. Hence
\[
b_{\overline{BS(\mathbf x)}}(c_{\mathrm{bot}},\rho^m c_{\mathrm{bot}})>0.
\tag{8.197}
\]
The bottom degree of \(B_x\) is one-dimensional, and every summand embedding \(B_x\hookrightarrow BS(\mathbf x)\) is nonzero there. This follows from the unique top \(\nabla_x\) layer, self-duality and the degree bounds; its generator survives the least degree because the ascending support quotient is right free. Once \(\operatorname{ch}B_x=C_x\), the Hom formula gives \(\operatorname{End}^0 B_x=\mathbb R\), so its invariant form is unique up to scalar. Equation (8.197) then shows that all forms induced by reduced-word summand embeddings are positive multiples of the form normalized to be positive on the bottom Lefschetz line. Thus an assertion of Hodge signs is independent of those choices.

#### 8.11.3. The local intersection embedding and the character step

For this section let \(w=xs>x\), assume \(\operatorname{ch}B_y=C_y\) and Hodge signs for every \(y<w\), and give \(V_0=B_xB_s\) the form induced from a reduced-word embedding of \(B_x\). Suppose \(\overline{V_0}\), with left \(\rho\), has hard Lefschetz and Hodge signs with reference lowest degree \(-\ell(w)\). Let \(y<w\). The chosen positive-normalized form on \(B_y\) gives an adjoint \(f^*:V_0\to B_y\) for a degree-zero map \(f:B_y\to V_0\). Since \(\operatorname{End}^0 B_y=\mathbb R\), composition defines a real symmetric form
\[
\mathcal I_y(f,g)=g^*f
\quad\text{on }\operatorname{Hom}^0(B_y,V_0).
\tag{8.198}
\]

Here is the full injectivity argument. The top descending layer of \(B_y\) is \(\Delta_y=\Gamma_{\ge y}B_y\), since no larger label occurs. The quotient \(Q_y=B_y/\Delta_y\) has character \(C_y-H_y\in\sum_{z<y}u\mathbb Z_{\ge0}[u]H_z\). Moreover
\[
\operatorname{ch}V_0=C_xC_s\in\sum_z\mathbb Z_{\ge0}[u]H_z.
\tag{8.199}
\]
To verify the latter without the desired theorem, multiply each standard coefficient of the already known \(C_x\) by \(C_s\). The only power lowered by one is a coefficient at a descent label \(z\); that label is strictly below \(x\), so its coefficient is divisible by \(u\). Thus no negative power arises, and all coefficients are nonnegative.

The arbitrary-summand Hom formula 8.6 and its lifting give
\[
\operatorname{Hom}^0(B_y,V_0)\cong\operatorname{Hom}^0(\Delta_y,V_0).
\tag{8.200}
\]
The kernel \(\operatorname{Hom}^{\le0}(Q_y,V_0)\) vanishes: in the Hom formula every degree generator has a strictly positive degree, as follows by multiplying the strictly positive source-\(u\) character of \(Q_y\) with (8.199). Surjectivity is the actual Hom lifting along the first standard layer, not an inference from generic dimensions.

Evaluation at the graph generator identifies the right side of (8.200) with the degree-\(\ell(y)\) part of \(\Gamma_y V_0\). That submodule is right split in \(V_0\) by (8.111). All its generators have degree at least \(\ell(y)\), by the same Hom formula; hence reduction modulo \(\mathfrak m\) is injective in that least degree. The graph generator \(c\) of \(\Delta_y\) maps to a nonzero generator of \(\overline{B_y}^{\ell(y)}\). This can also be seen from the exact \(p_y\)-identity in Theorem 8.5 and the unique free rank-one top graph quotient. By hard Lefschetz it is a nonzero scalar multiple, in the quotient, of \(\rho^{\ell(y)}c_{\mathrm{bot}}\).

It follows that
\[
\iota_y:\operatorname{Hom}^0(B_y,V_0)\longrightarrow
\overline{V_0}^{-\ell(y)},\qquad f\longmapsto\overline{f(c_{\mathrm{bot}})}
\tag{8.201}
\]
is injective. Its image is primitive, since \(\rho^{\ell(y)+1}c_{\mathrm{bot}}=0\) on \(\overline{B_y}\). Put \(N_y=b_{\overline{B_y}}(c_{\mathrm{bot}},\rho^{\ell(y)}c_{\mathrm{bot}})>0\). Adjointness and left \(R\)-linearity give
\[
b_{\overline{V_0}}\bigl(\iota_y f,\rho^{\ell(y)}\iota_y g\bigr)
=N_y\,\mathcal I_y(f,g).
\tag{8.202}
\]
Thus \(\mathcal I_y\) is \((-1)^{(\ell(w)-\ell(y))/2}\)-definite, or its space is zero if the parity differs. This proves all signs and nondegeneracy of the local forms.

We next prove the character consequence directly, so no separate Soergel local-form criterion is imported. Classification gives
\[
V_0\cong B_w\oplus\bigoplus_{y<w,n}B_y(n)^{m_{y,n}},
\tag{8.203}
\]
with \(B_w\) once and unshifted, because its top standard coefficient is one. The Hom formula and (8.199) show that \(\operatorname{Hom}^{d}(B_y,V_0)=0\) for \(d<0\), for all \(y<w\). If \(B_y(n)\) occurred with \(n>0\), its identity would contribute a map of degree \(-n\); hence \(n\le0\). Self-duality of \(V_0,B_w,B_y\), together with uniqueness of indecomposable decomposition, pairs shifts \(n\) and \(-n\), so all \(n\) are zero.

Degree-zero Hom between known distinct \(B_y\)'s is zero, and their endomorphism spaces are \(\mathbb R\). A map into the \(B_w\)-summand is in the radical of (8.198): any composition \(B_y\to B_w\to B_y\) is zero, because a nonzero scalar composition would split \(B_y\) from the distinct indecomposable \(B_w\). Nondegeneracy of \(\mathcal I_y\) therefore implies
\[
m_{y,0}=\dim\operatorname{Hom}^0(B_y,V_0).
\tag{8.204}
\]
The constant term of the Hom pairing \((C_y,C_xC_s)\) is just the constant term of the \(H_y\)-coefficient of \(C_xC_s\), since all strict lower coefficients of \(C_y\) contain \(u\) and (8.199) has no negative powers. Thus (8.204) subtracts exactly every strict lower constant term. Consequently
\[
\operatorname{ch}B_w=C_xC_s-\sum_{y<w}m_{y,0}C_y
\in H_w+\sum_{y<w}u\mathbb Z[u]H_y.
\tag{8.205}
\]
Its character is bar invariant by Section 8.7.17, so canonical-basis uniqueness gives \(\operatorname{ch}B_w=C_w\). All coefficients are nonnegative because this is its actual support-layer character. This proves the character step and its coefficient positivity. The left-multiplication version of the nondegenerate-composition criterion is stated in [Soergel, arXiv:math/0403496v2, Lemma 7.1(2)](https://arxiv.org/abs/math/0403496v2).

Finally \(B_w\) is a left-\(\rho\)-stable graded summand with symmetric dimensions by self-duality. Lemma 8.12 restricts the Hodge signs and hard Lefschetz from \(\overline{V_0}\) to it. Its bottom degree agrees with the ambient degree \(-\ell(w)\), so the inherited sign is the standard positive one. Section 8.11.2.1 makes the same assertion valid for every reduced-word embedding.

#### 8.11.4. Complexes and the full linearity deduction

Write \(F_s=[B_s\xrightarrow{\mu}R(1)]\), in degrees \(0,1\). The graph sequence (8.96), with its global shift, is
\[
0\longrightarrow R_s(-1)\longrightarrow B_s
\overset{\mu}{\longrightarrow}R(1)\longrightarrow0.
\tag{8.206}
\]
Its quotient is free on the right and on the left. For a word of length \(m\), the total tensor complex therefore has bimodule cohomology \(R_x(-m)\) in degree zero and zero elsewhere. Here is the tensor justification: all terms of the other factors are left and right free, so tensoring the cone of the quasi-isomorphism in (8.206) preserves its exactness. One factor at a time replaces the complex by \(R_{s_i}(-1)\); their tensor product is \(R_x(-m)\). An elementary finite argument also shows the total complex, as a right-module complex, is homotopy equivalent to that cohomology: starting at the highest term, an exact surjection onto a free module splits, removes an identity complex, and continues downwards; at degree zero the remaining cohomology is free and the final surjection splits. Consequently, for a reduced word and any minimal summand,
\[
H^i(\overline{F_{\mathbf x}})=
\begin{cases}\mathbb R(-\ell(x)),&i=0,\\0,&i\ne0.\end{cases}
\tag{8.207}
\]
Its cohomology vector in degree zero has internal degree \(+\ell(x)\). In particular the first differential is injective in every internal degree less than \(\ell(x)\); after appending \(s\) its threshold is \(\ell(x)+1\). This proves the needed injectivity without a global braid theorem.

Call an object perverse if its character is a nonnegative integer combination of \(C_z\). When \(\operatorname{ch}B_z=C_z\), its shifted copies \(B_z(n)\) have degree-zero Hom only in shift-nondecreasing directions:
\[
\operatorname{Hom}^0(B_z,B_y(-a))=0\ (a>0),\qquad
\operatorname{Hom}^0(B_z,B_y)=\mathbb R\,\delta_{zy}.
\tag{8.208}
\]
This follows from the positive-degree/constant terms of the Hom formula and the canonical Hecke pairing. The same negative-shift vanishing holds between arbitrary perverse objects.

A summand of a perverse object is perverse. Here is a proof including the possible shifts. Characters of the \(B_z\) are unitriangular in the standard basis by classification, so are linearly independent over \(\mathbb Z[u,u^{-1}]\); hence equality of characters implies equality of indecomposable classes. A perverse object's character is bar invariant. Duality and Section 8.7.17 consequently give \(B\cong DB\). Its shifts of each \(B_z\) occur in pairs \(n,-n\). Its standard coefficients have no negative powers because the canonical elements have none. They are also nonnegative because they are actual support multiplicities. Thus no shifted summand \(B_z(n)\) with \(n<0\) occurs: its top standard coefficient \(u^nH_z\) could not be canceled by another actual character. Pairing shifts proves that every summand is unshifted and self-dual.

For such a summand, expand its bar-invariant character in the canonical basis in decreasing Bruhat order. At the maximal remaining label, the coefficient is a polynomial in nonnegative powers of \(u\) and is bar invariant, hence is constant. Its constant is the constant of the original standard coefficient at that label: strict lower coefficients of higher canonical elements contain \(u\). Thus this constant is nonnegative. Subtracting this constant canonical element leaves coefficients still in \(\mathbb Z[u]\), though coefficientwise positivity of that difference is unnecessary. Repeat. All canonical expansion coefficients are the original standard constant terms and are nonnegative. The same argument proves the perverse-summand assertion without assuming a new indecomposable's character is already canonical.

For \(zs>z\) with \(S(z)\), multiplying \(C_z\) by \(C_s\) gives a bar-invariant standard polynomial with no negative powers, as in (8.199). The same decreasing-order subtraction shows it is a nonnegative constant combination of canonical elements. Thus \(B_zB_s\) is perverse, even if the new \(B_{zs}\) character is not yet known. Its summands are perverse by the preceding argument. For a descent, input Rs and the decomposition \(R=R^s\oplus(\alpha_s/2)R^s\) give
\[
B_zB_s\cong B_z(1)\oplus B_z(-1),\qquad
B_zF_s\simeq B_z(-1).
\tag{8.209}
\]
The second assertion is an actual cancellation: in these coordinates the multiplication differential is \((1,\text{right multiplication by }\alpha_s/2)\); its identity component cancels, leaving \(B_z(-1)\). No indecomposability of a tensor functor or monoidal inverse is needed.

For a complex with perverse shifted summands, impose the lower-bound condition that a summand \(B_z(n)\) in cohomological degree \(i\) has \(n\le i\). This condition is stable under forming an extension triangle: represent the middle complex as a cone over the connecting map, whose term is the direct sum of the two end terms, and cancel identity summands if needed. It is preserved under tensoring by \(F_s\): apply (8.209) to a descent summand, and for an ascent use the perverse product in degree \(i\) together with \(B_z(n+1)\) in degree \(i+1\). Apply this term-by-term using the finite stupid filtration and its cone triangles. Induction on a reduced word, under \(S(y)\) for all \(y<x\), shows that its minimal complex has this lower-bound condition. All summand labels are \(\le x\); the only possible unknown label is \(B_x\), occurring once and unshifted in degree zero.

Assume now \(S(y)\) for every \(y\le x\), so every term has known indecomposable characters. We prove that the minimal complex is linear:
\[
{}^0F_{\mathbf x}=B_x,\qquad
{}^iF_{\mathbf x}=\bigoplus_{z<x}B_z(i)^{m_{z,i}}\quad(i>0).
\tag{8.210}
\]
Consider a summand \(B_z(j)\) in degree \(i\), with \(z<x\). Minimality and (8.208) imply that its outgoing differential can only have components into shifts \(k>j\); components at \(k=j\) would be scalar identity blocks and hence contractible. Likewise a nonzero incoming component from \(B_y(k)\) requires \(k<j\).

Apply the support-layer functor at \(z\). By RΔ the resulting complex is contractible. Tensoring its free graph modules with \(R/\mathfrak m\) keeps it contractible. Our chosen summand contributes a copy of \(\Delta_z(j)\). Its differential to any outgoing summand has zero reduction in this internal degree: the outgoing shifts are \(k>j\), and a graph-standard contribution from a higher label has an additional strictly positive shift, because \(S(y)\) is known. Thus its chosen generator must be a boundary in the reduced contractible layer complex. At least one incoming graph generator must have the same total shift \(j\) and a nonzero constant component onto it. Such a generator can only come from \(B_y(k)\), \(y\ge z\). If \(y=z\), its total shift is \(k\), which cannot equal \(j\) because \(k<j\). Hence
\[
B_z(j)\subset{}^iF_{\mathbf x},\ z<x
\quad\Longrightarrow\quad
B_y(k)\subset{}^{i-1}F_{\mathbf x}\text{ for some }y>z,\ k<j.
\tag{8.211}
\]
This generator argument allows arbitrary matrices and linear combinations of equal-shift copies; it does not assert that a specified summand must itself be paired by an individual isomorphism before a basis change.

No lower-label summand can occur in degree zero, since degree \(-1\) is zero. The top graph layer supplies precisely one \(B_x\) there. Inductively (8.211) gives \(j\ge i\) in degree \(i\), while the already proved lower-bound condition gives \(j\le i\). Therefore \(j=i\), proving (8.210). The exact point where RΔ is used is contractibility after reduction of the support-layer complex; neither a split Grothendieck identity nor (8.207) replaces it.

#### 8.11.5. Hodge signs on the terms of a minimal complex

It is useful to specify a reference \(N\), possibly larger than the actual lowest surviving degree: signs on primitive degree \(-d\) mean
\[
(-1)^{(N-d)/2}\text{-definiteness}.
\tag{8.212}
\]
Zero primitive spaces are allowed, and parity mismatches mean zero. This avoids incorrectly renormalizing the lowest sign after taking a balanced subspace.

If \(B=\bigoplus_z B_z^{m_z}\) has known characters and an invariant form with Hodge signs referenced to \(N\), distinct isotypic parts are orthogonal: their pairing is a degree-zero map to the dual and (8.208) makes it zero. In one isotypic part, the form is a real symmetric matrix on its multiplicity space times the fixed form on \(B_z\), because \(\operatorname{End}^0B_z=\mathbb R\). The bottom vectors of that part are primitive. Their Lefschetz matrix is therefore definite with sign \((-1)^{(N-\ell(z))/2}\). Choose an orthogonal real basis for it. This supplies an orthogonal decomposition of \(B\) into indecomposable copies whose forms are that sign times a positive multiple of the bottom-positive form on \(B_z\).

Suppose each relevant \(\overline{B_zB_s}\) has Hodge signs for \(L_\zeta\), referenced to \(\ell(z)+1\). Then the induced form on \(\overline{BB_s}\) has signs referenced to \(N+1\): on a primitive of degree \(-d\) the product of the two signs is
\[
(-1)^{(N-\ell(z))/2}(-1)^{(\ell(z)+1-d)/2}
=(-1)^{(N+1-d)/2}.
\tag{8.213}
\]
This proves the direct-sum tensor assertion, including its sign, without an informal “standard sign” rescaling. For \(\zeta=0\), it is only applied to ascent labels \(zs>z\).

We also need a stronger displaced-centre observation. Let \(H\) have hard Lefschetz centered at \(-a\), \(a>0\), and let a degree-zero graded symmetric form on it be \(L\)-self-adjoint; nondegeneracy is not assumed. Its restriction is identically zero. Indeed primitive chains have degrees \(-a-r+2j\), \(0\le j\le r\). Two chain vectors \(L^jp,L^kq\) can pair only when \(j+k=a+(r+t)/2\), where \(p,q\) begin chains of lengths \(r,t\). If \(r\ge t\), this exponent is strictly larger than \(t\), so moving all powers to \(q\) kills it. If \(t>r\), move all powers to \(p\). Thus every pairing is zero. This includes and strengthens Lemma 8.14 for the particular subspaces used below; it supplies an actual isometry of graded forms, not merely equality of diagonal Lefschetz norms.

For a reduced word \(\mathbf x\) of length \(m\), under \(S(\le x)\) and Hodge signs for all ascent tensors \(B_zB_t\) with \(z<x\), there is a minimal embedding
\(F_{\mathbf x}\hookrightarrow T_{\mathbf x}\) with the following property: for every \(i\), its unshifted term \({}^iF_{\mathbf x}(-i)\) has Hodge signs referenced to \(m-i\), for every choice of positive real weights on the intersection forms of the deletion subwords. The same embedding works for all such weights.

We prove this by word-length induction. The empty word is immediate. Write \(\mathbf x=\mathbf y s\). Choose the prefix embedding having this property. A minimal summand of \(F_{\mathbf y}F_s\) embeds in the full tensor word. In degree \(i\), after removing the shift \(i\), its source \(U={}^iF_{\mathbf x}(-i)\) embeds in
\[
(A^\uparrow B_s)\oplus(A^\downarrow B_s)\oplus
{}^{i-1}F_{\mathbf y}(-(i-1)),
\quad
{}^iF_{\mathbf y}(-i)=A^\uparrow\oplus A^\downarrow,
\tag{8.214}
\]
where \(A^\uparrow\) is the sum of labels \(zs>z\), and \(A^\downarrow\) the descent labels. The three indicated blocks are orthogonal for each choice of weights: the last is in the deletion block omitting the last letter; the first two are orthogonal by the isotypic Hom vanishing before induction.

By (8.209), \(A^\downarrow B_s=A^\downarrow(1)\oplus A^\downarrow(-1)\). Hom vanishing from the perverse \(U\) to the negative-shift block makes its projection land in \(A^\downarrow(1)\). Left \(\rho\) preserves this block; its hard Lefschetz center is \(-1\). Its restricted graded form is zero by the stronger observation just proved. It therefore contributes no pairing.

Projection away from this block is still a split inclusion. To prove this carefully, pass to the radical quotient of the finite indecomposable category, supplied by Section 8.7.5 and (8.129). The original inclusion is split. Its discarded component between unshifted labels and labels shifted by one has no isomorphism component, so is zero in the radical quotient. The remaining projection is consequently split in that quotient. Lift a left inverse, compose it with the projection, and invert the identity plus radical error using Section 8.7.5. This gives an actual split left inverse before reduction modulo \(\mathfrak m\). Thus
\[
\overline U\hookrightarrow
\overline{A^\uparrow B_s}\oplus
\overline{{}^{i-1}F_{\mathbf y}(-(i-1))}
\tag{8.215}
\]
is injective and is an isometry for the restricted forms.

The prefix reference for \(A^\uparrow\) is \(m-1-i\); tensoring and (8.213) give reference \(m-i\). The second block has prefix reference \((m-1)-(i-1)=m-i\). It follows that the target has hard Lefschetz and definite primitive forms with the same reference sign. The source is \(\rho\)-stable and has symmetric dimensions by (8.210) and self-duality. Lemma 8.12 therefore proves the asserted Hodge signs on \(\overline U\).

All steps used only positivity, rather than values, of the deletion weights. The prefix choice is fixed for all weights, and the final minimal cancellation is independent of the forms. This proves the simultaneous assertion required later. It expands native EW Proposition 6.13, including the split-projection and sign steps.

#### 8.11.6. Factoring a Lefschetz operator through deletion maps

In the iterated commutative tensor algebra, the maps \(\phi_i,\chi_i\) from Section 8.11.2.1 satisfy
\[
b_{\mathbf x}(a,\chi_i\phi_i b)
=b_{\mathbf x_{\widehat i}}(\phi_i a,\phi_i b).
\tag{8.216}
\]
For a pure tensor, both sides multiply the remaining factor entries pairwise and extract their all-\(c_1\) coefficient. In the omitted factor, multiplying by \(c_1\) followed by trace equals multiplication of its two \(\mu\)-values, by \(c_0c_1=c_1\), \(c_1^2=c_1\alpha_s\) and \(\mu(c_0)=1,\mu(c_1)=\alpha_s\). Multilinearity proves (8.216) for arbitrary elements. Inserting \(c_1\) preserves extraction of the coefficient in the remaining factors, so this verification also proves the required trace identity.

Combine (8.216) with the telescoping operator identity (8.196). On the right quotient, with \(\phi=(\phi_i)\),
\[
b_{\overline{BS(\mathbf x)}}(a,\rho b)
=\sum_i\gamma_i
 b_{\overline{BS(\mathbf x_{\widehat i})}}(\phi_i a,\phi_i b).
\tag{8.217}
\]
If \(\mathbf x s\) is reduced, and \(L_\zeta\) includes \(\zeta\) times multiplication at the last tensor junction, the same identity holds with the earlier weights unchanged and last weight
\[
\gamma_{m+1}=(x^{-1}\rho)(\alpha_s^\vee)
                 +\zeta\rho(\alpha_s^\vee)>0
\quad(\zeta\ge0).
\tag{8.218}
\]
To check the extra term, move the middle \(\zeta\rho\) through \(B_s\) by (8.191). Its right-scalar term vanishes; the remaining term is
\(\zeta\rho(\alpha_s^\vee)\chi_{m+1}\phi_{m+1}\).
Equations (8.217)–(8.218) are form identities on actual modules, not mere rank comparisons. The first differential of the tensor complex is exactly \((\phi_i)\), with positive sign since every factor of degree zero precedes that first differential; later total-complex signs are immaterial here.

#### 8.11.7. The three hard-Lefschetz steps

##### 8.11.7.1. A descent with \(\zeta>0\)

Assume \(xs<x\) and hard Lefschetz on \(\overline{B_x}\). Use Rs and insert the middle \(R^s\)-basis \(1,\alpha_s/2\) to identify \(B_xB_s=B_x(1)\oplus B_x(-1)\). The corresponding projections are \(r\mapsto(r+sr)/2\) and \(r\mapsto\partial_s r\). Left \(\rho\) acts diagonally. Multiplication by the middle \(\rho\) has, after killing all positive-degree outer right scalars, only its lower-left entry \(c=\rho(\alpha_s^\vee)\). Therefore
\[
L_\zeta=
\begin{pmatrix}L&0\\\zeta c&L\end{pmatrix}
\quad\text{on }\overline{B_x}(1)\oplus\overline{B_x}(-1).
\tag{8.219}
\]
This computation depends on Rs, as explicitly stated in Section 8.11.1.

For completeness the matrix has hard Lefschetz without a tensor-product representation theorem. On a primitive \(L\)-chain \(p,Lp,\ldots,L^dp\), let \(a_j=(L^jp,0)\) and \(b_j=(0,L^jp)\), and put \(\lambda=\zeta c\ne0\). Then \(Ea_j=a_{j+1}+\lambda b_j\), \(Eb_j=b_{j+1}\). The chain generated by \(a_0\) has length \(d+2\), since \(E^{d+1}a_0=(d+1)\lambda b_d\ne0\). For \(d\ge1\), a second primitive generator is
\[
r=b_0-\frac1{(d+1)\lambda}Ea_0,\qquad E^dr=0.
\]
It has length \(d\). In a common degree, the two chain vectors are
\[
E^{j+1}a_0=a_{j+1}+(j+1)\lambda b_j,\qquad
E^jr=-\frac{a_{j+1}}{(d+1)\lambda}
       +\frac{d-j}{d+1}b_j;
\]
their \(2\)-by-\(2\) coefficient determinant is one. Thus the two chains form a direct sum, centered at zero, with endpoints \(\pm(d+1)\) and \(\pm(d-1)\). For \(d=0\) only the first chain occurs. Each has hard Lefschetz, proving it for (8.219).

At \(\zeta=0\), the bottom degree \(-\ell(x)-1\) has nonzero vectors killed by \(L^{\ell(x)+1}\), so hard Lefschetz fails in a descent. If \(B_x\) has its standard Hodge signs, Section 8.11.2 gives those signs for large \(\zeta\); Lemma 8.11 and the preceding hard-Lefschetz result give them for every \(\zeta>0\).

##### 8.11.7.2. An ascent with \(\zeta>0\)

Assume \(xs>x\), \(S(\le x)\), Hodge signs for \(B_x\), the ascent signs needed for Section 8.11.5 on every smaller label, and \(HR(z,s)_\zeta\) for every \(z<x\), including descents at this positive parameter. Fix any reduced word \(\mathbf x\), choose Section 8.11.5's simultaneous embedding, and tensor it with \(F_s\). By (8.210) the first differential is
\[
d:\ B_xB_s\longrightarrow {}^1F_{\mathbf x}B_s\oplus B_x(1).
\]
Put \(A={}^1F_{\mathbf x}(-1)\), and \(W=\overline{AB_s}\oplus\overline{B_x}\). Then \(\overline d:\overline{B_xB_s}\to W(1)\) is injective in all negative degrees by (8.207), since its cohomology in degree zero is concentrated in internal degree \(\ell(x)+1\).

The first component commutes with \(L_\zeta\), because its maps act on \(B_x\) and are right \(R\)-linear before tensoring \(B_s\). The last multiplication map satisfies
\(\mu(L_\zeta b)=\rho\mu(b)+\zeta\mu(b)\rho\);
the last term dies in the right quotient. Thus \(\overline d\) is linear for \(L_\zeta\) on the source, and for \(L_\zeta\oplus L\) on \(W\). Equations (8.217)–(8.218), restricted through the chosen complex summand, give
\[
b_W(\overline d a,\overline d b)=b_{\overline{B_xB_s}}(a,L_\zeta b).
\tag{8.220}
\]

The two summands of \(W\) are orthogonal. Section 8.11.5 gives \(A\) Hodge signs referenced to \(\ell(x)-1\), for the positive earlier weights. Formula (8.213) and the assumed \(HR(z,s)_\zeta\) give \(AB_s\) signs referenced to \(\ell(x)\). The \(B_x\) summand has exactly that reference and a positive weight (8.218). Thus \(W\) has hard Lefschetz and definite primitive forms with matching signs. Lemma 8.13 applies to (8.220), proving injectivity of every \(L_\zeta^k\) from degree \(-k\) on \(\overline{B_xB_s}\). Its dimensions are symmetric because its form is nondegenerate and graded, as proved in Section 8.11.2. Hence those maps are isomorphisms.

##### 8.11.7.3. An ascent with \(\zeta=0\)

Assume \(xs>x\), \(S(\le x)\), Hodge signs for \(B_x\) and every smaller ascent tensor needed in Section 8.11.5, and hard Lefschetz for all \(B_z\) with \(z<xs\). Choose the same kind of complex embedding and positive deletion weights, now with (8.218) at zero. Decompose
\[
A={}^1F_{\mathbf x}(-1)=A^\uparrow\oplus A^\downarrow.
\]
The first two terms of \(F_{\mathbf x}F_s\) are
\[
B_xB_s\longrightarrow
B_x(1)\oplus A^\uparrow B_s(1)\oplus A^\downarrow B_s(1).
\tag{8.221}
\]
The three displayed blocks are orthogonal, for the reasons in Section 8.11.5. Descending induction gives \(A^\downarrow B_s(1)=A^\downarrow(2)\oplus A^\downarrow\).

The lower-bound condition of Section 8.11.4 says that a minimal representative has no shift \(2\) summand in cohomological degree \(1\). The incoming differential from degree zero has no isomorphism component onto \(A^\downarrow(2)\): all its degree-zero indecomposable summands are perverse and unshifted. In the radical quotient, the bad shift-\(2\) part is therefore a subspace of the kernel of no incoming isomorphism, and must be killed entirely by the outgoing differential, since it cannot survive in the minimal complex. Its outgoing differential is injective in that quotient. Lifting a left inverse and correcting the radical error as in Section 8.11.5 proves it is an actual split injection. It can consequently be canceled as an elementary contractible summand by Section 8.7.5.

After cancellation the first differential, in the remaining quotient coordinates, is
\[
\widetilde d:\ B_xB_s\longrightarrow
B_x(1)\oplus A^\uparrow B_s(1)\oplus A^\downarrow.
\tag{8.222}
\]
The two earlier components are their original projections; the last is projection to the shift-zero copy \(A^\downarrow\). Block elimination may change the remaining differential out of this term; it does not change the quotient projection of the differential into it. This precise choice of coordinates is used below. The cancellation is right split and a homotopy equivalence, so \(\overline{\widetilde d}\) remains injective in all negative degrees by (8.207). Every component is a bimodule map and hence commutes with left \(\rho\).

Let \(D=\overline{A^\downarrow}\), \(U=\overline{B_xB_s}\), and denote the last component by \(d_D:U\to D\). If \(0\ne a\in U^{-k}\) has \(d_D a\ne0\), hard Lefschetz on \(D\) gives
\(L^kd_Da=d_DL^ka\ne0\), so \(L^ka\ne0\).

For the remaining vectors take the graded stable space \(U'=\ker d_D\), and let \(W=\overline{B_x}\oplus\overline{A^\uparrow B_s}\). The first two components give an injective map \(U'\to W(1)\) in negative degrees. They commute with \(L\). To check its form identity rather than assume cancellation preserved the full target form, examine the original differential in (8.221): when \(a\in U'\), its descent component is entirely in \(A^\downarrow(2)\), which in the unshifted target of (8.217) is \(A^\downarrow(1)\). That space is \(L\)-stable with hard Lefschetz centered at \(-1\), and its restricted graded form is zero by Section 8.11.5. It is also orthogonal to the two retained blocks. Thus on \(U'\), (8.217) becomes precisely
\[
b_W(d a,d b)=b_U(a,Lb)\qquad(a,b\in U').
\tag{8.223}
\]
The form on \(U'\) need not be nondegenerate; Lemma 8.13 does not require that.

The \(B_x\) block has signs referenced to \(\ell(x)\). The \(A^\uparrow B_s\) block has the same reference by Section 8.11.5 and (8.213), using only ascent signs at the zero parameter. Therefore \(W\) has definite primitive forms. Lemma 8.13 applied to (8.223) proves \(L^k\) injective on \((U')^{-k}\). Together with the previous case this proves injectivity on every \(U^{-k}\). Symmetric dimensions of \(U\) make it hard Lefschetz.

This expands the exceptional zero-parameter argument: descent tensors themselves fail hard Lefschetz at zero; they are handled by a shifted isotropic block, cancellation, and the kernel of the remaining descent projection. No continuity through a singular descent parameter is used.

#### 8.11.8. A well-founded induction and the exact positivity conclusion

**Theorem 8.10 (finite-Weyl Hodge theory and KL positivity).** For every finite Weyl group, the actual indecomposable bimodules satisfy $\operatorname{ch}B_x=C_x$. Their right-augmented spaces satisfy hard Lefschetz and the bottom-positive primitive Hodge sign condition for every strictly dominant $\rho$. Every KL polynomial $P_{x,y}(q)$ has nonnegative integer coefficients, and the canonical-basis structure constants are nonnegative Laurent polynomials. This includes products and rank zero. The assertion concerns the real reflection realization and integer characters.

**Proof.** We use induction on length. This ensures that all smaller-label ascent tensors needed by Section 8.11.5 have already been treated, even when their last simple reflection is not one of the descents of the current target.

For each \(n\), retain the following assertions:

1. For every \(\ell(x)\le n\), \(S(x)\), hard Lefschetz and bottom-positive Hodge signs hold.
2. For every ascent \(xs>x\) with \(\ell(xs)\le n\), \(L_\zeta\) on \(\overline{B_xB_s}\) has hard Lefschetz and Hodge signs referenced to \(\ell(x)+1\), for all \(\zeta\ge0\).
3. For every descent \(xs<x\) with \(\ell(x)\le n\), those tensor assertions hold for all \(\zeta>0\).

At \(n=0\), \(B_e=R\), its quotient is \(\mathbb R\) in degree zero with multiplication form, and \(S(e)\) and its hard Lefschetz/Hodge assertions are immediate. There are no relevant tensor edges in assertions 2–3.

Assume the assertions through \(n\). Let \(\ell(x)=n\), \(xs>x\), and \(w=xs\). Every \(y<x\) has length at most \(n-1\), so every ascent \(yt>y\) has target length at most \(n\); its zero-parameter Hodge signs are already known by assertion 2. Likewise, for each fixed \(\zeta>0\), \(HR(y,s)_\zeta\) is known for every \(y<x\): use assertion 2 for an ascent and assertion 3 for a descent. Every \(z<w\) has length at most \(n\), so hard Lefschetz on \(B_z\) is already known by assertion 1.

Therefore Section 8.11.7.2 proves hard Lefschetz on \(\overline{B_xB_s}\) at every positive parameter, and Section 8.11.7.3 proves it at zero. Section 8.11.2 supplies the standard signs at one sufficiently large positive parameter. Lemma 8.11 carries these signs along each compact interval from that parameter to any chosen nonnegative parameter, including zero. This proves assertion 2 for this edge. Its zero-parameter instance satisfies exactly the hypotheses of Section 8.11.3, which gives \(S(w)\) and hard Lefschetz/Hodge signs for \(B_w\).

Do this for every \(x\) of length \(n\) and every ascent from it. Every element of length \(n+1\) has such a last-letter expression; treating all of them also proves the assertions for every reduced-word embedding, by Section 8.11.2.1. Section 8.11.7.1 then proves hard Lefschetz at every positive parameter on every descent from the new element. The same large-parameter and connected-sign argument gives its Hodge signs for all positive parameters. Thus all three assertions hold through \(n+1\).

The proof also covers the first rank-one step explicitly. If \(x=e\), \(F_e\) has no degree-one term, so Sections 8.11.7.2–8.11.7.3 have target \(W=\overline R\). The map \(B_s\to R(1)\) sends its bottom \(c_0\) to \(1\), and is injective in degree \(-1\). Its form weight is \((1+\zeta)\rho(\alpha_s^\vee)>0\). Therefore there is no unproved “inspection of all length-two cases” hidden in the base.

The length induction terminates for finite \(W\). It yields
\[
\operatorname{ch}B_y=C_y
 =\sum_{x\le y}u^{\ell(y)-\ell(x)}
             P_{x,y}(u^{-2})H_x
\quad\text{with actual nonnegative support coefficients.}
\tag{8.224}
\]
Since a monomial multiplication and substitution \(u^{-2}=q\) put the distinct coefficients of \(P_{x,y}\) in distinct powers of \(u\), all coefficients of each \(P_{x,y}\) are nonnegative integers. On returning to lesson notation \(u=v^{-1}\), this reads
\[
C'_y=\sum_{x\le y}v^{\ell(x)-\ell(y)}P_{x,y}(v^2)H_x,
\]
precisely RT-LIE-18's normalization. No switch to the other canonical basis, or unintended \(q\mapsto q^{-1}\), occurs.

The same result also yields nonnegative Laurent canonical-basis structure constants: tensoring the \(B_x\)'s decomposes into actual \(B_z(n)\)'s, whose multiplicity polynomials have nonnegative coefficients. This last assertion uses character multiplication from the actual support transport. It does not assert a geometric IC interpretation, a decomposition theorem, a localization equivalence, or the dominant Verma dictionary.

For rank zero all spaces are concentrated in degree zero and the proof reduces to \(P_{e,e}=1\). For a disconnected root system, the real reflection representation, rank-one decompositions, root-sign arguments and finite length induction apply verbatim. No irreducibility of \(W\) is used. The statement is over \(\mathbb R\), with integer character coefficients, at finite-Weyl scope; it is not being extended here to positive characteristic or to an arbitrary nonfaithful realization.

Theorem 8.10 proves finite-Weyl coefficient positivity. Sections 8.12–8.15 prove the category $\mathcal O$ comparison and general regular integral Verma multiplicities in Theorem 8.13, completing the proof of Theorem 8.2.

### 8.12. Ordinary wall translations and projective generation

The constructions below prove the finite ordinary-category translation properties used in the comparison. Compare [Soergel, MPI/89-46, §§2.4–2.5](https://archive.mpim-bonn.mpg.de/id/eprint/3653/1/preprint_1989_46.pdf) and [Fiebig, arXiv:math/0305378v2, §§2.5 and 4](https://arxiv.org/html/math/0305378v2).

Throughout, \(\mathfrak g\) is a finite-dimensional complex semisimple Lie algebra. Fix the positive-root Borel \(\mathfrak b=\mathfrak h+\mathfrak n^+\), the full integral weight lattice, \(\rho\), and
\[
w\cdot\nu=w(\nu+\rho)-\rho.
\tag{8.225}
\]
The real span of the weights has its positive definite Weyl-invariant inner product. The weight order is \(\xi\ge\eta\) when \(\xi-\eta\in Q^+\). Every category in this section is the ordinary category O over \(\mathbb C\), with generalized central characters. No deformed category, affine Weyl group, positive characteristic or derived translation is being asserted.

The actual prerequisites are RT-LIE-18, Sections 1–6, with complete proofs of finite length, projective covers, Verma filtrations, restricted duality and BGG reciprocity; RT-LIE-15, Theorem 4.1 and Corollary 5.2, for all-complex-weight Harish-Chandra and its shifted-orbit criterion; RT-LIE-14, Sections 2–5, for Verma modules, finite highest-weight modules and their weight polytope; and RT-LIE-08 with RT-LIE-18, Lemma 8.1, for root signs, exchange and expression-independent reduced-subword order. The finite deductions used in wall translation are expanded below.

The starting-object convention is essential:
\[
P(\lambda)=M(\lambda)\quad(\lambda\text{ dominant integral})
\]
generates the regular projectives under successive wall crossings and taking summands. The anti-dominant big projective \(P(w_0\cdot\lambda)\) is the object in the structure functor
\(\mathbb V=\operatorname{Hom}(P(w_0\cdot\lambda),-)\).
Its simple-wall crossings are two copies of itself; it is not the generator under those crossings.

#### 8.12.1. Central projection and tensoring

For any object \(X\) of category O, the action of \(Z=Z(U(\mathfrak g))\) factors through a finite-dimensional commutative algebra. Indeed, choose finite weight generators of \(X\) and let \(E'\) be the sum of their entire weight spaces. This is finite-dimensional and stable under \(Z\). If a central element kills \(E'\), it kills the generators and hence all of \(X\). Thus the faithful quotient of \(Z\) acting on \(X\) embeds in \(\operatorname{End}_{\mathbb C}(E')\).

A finite-dimensional commuting algebra over \(\mathbb C\) has a canonical generalized-character decomposition. Successively decompose a finite basis of its commuting operators into generalized eigenspaces. Every further operator preserves the preceding spaces. On a joint space simultaneous upper triangularization makes the eigenvalue function multiplicative, hence a character; its zero-eigenvalue ideal is strictly upper triangular and some common power is zero. The polynomial spectral projections are orthogonal idempotents summing to one. Therefore
\[
X=\bigoplus_\chi X_\chi,\qquad
X_\chi=\{x:(\ker\chi)^N x=0\text{ for some }N\}.
\tag{8.226}
\]
Only finitely many summands occur and a uniform \(N\) suffices on each summand. The displayed annihilator characterization makes them and their projections natural.

For a short exact sequence, use the finite-dimensional central image on the middle term; its idempotents also act on the subobject and quotient. Applying any one idempotent preserves exactness. This proves exactness of \(\operatorname{pr}_\chi:X\mapsto X_\chi\). A map between different generalized-character summands is zero, because it commutes with the same projections. Projection is both left and right adjoint to the inclusion of its central-character category.

Write \(\mathcal O_\nu=\mathcal O_{\chi_\nu}\). Harish-Chandra gives its simple labels \(L(w\cdot\nu)\), with repeats removed. For an integral \(\nu\), all these labels have the same root-lattice coset: \(w\cdot\nu-\nu\in Q\). Section 8.12.6 will prove that for dot-dominant integral \(\nu\) this whole central-character category is one indecomposable block, so the use of the word block there does not silently identify distinct components.

If \(F\) is finite-dimensional, \(F\otimes X\) remains in O. The Cartan decomposition and finite weight spaces are preserved. Positive-root words applied to a pure tensor stay in \(F\otimes U(\mathfrak n^+)x\), proving local finiteness. A basis of \(F\) tensored with finite generators of \(X\) generates the tensor: commute each Lie generator past the first factor using
\[
f\otimes ax=a(f\otimes x)-(af)\otimes x
\]
and induct on word length. Tensoring is exact over \(\mathbb C\).

For any two fixed central-character categories, finite tensoring followed by the target projection is thus an actual exact functor. These statements involve generalized characters, not a requirement that the whole centre act by scalars.

#### 8.12.2. Finite Weyl inequalities, with the needed order lemma proved

**Lemma 8.17 (dominant orbit inequality).** If \(a\) is strictly dominant and \(b\) is weakly dominant, then
\[
(a,rb)\le(a,b)\quad(r\in W),
\qquad
(a,rb)=(a,b)\Longleftrightarrow rb=b.
\tag{8.227}
\]
To prove this, take a reduced word \(r=s_{i_1}\cdots s_{i_k}\). Telescoping gives
\[
b-rb=\sum_{j=1}^k
\langle b,\alpha_{i_j}^{\vee}\rangle
s_{i_1}\cdots s_{i_{j-1}}\alpha_{i_j}.
\tag{8.228}
\]
The prefix roots are positive by the actual length/root-sign criterion; the coefficients are nonnegative. Hence \(b-rb\) lies in the positive root cone. Its pairing with strictly dominant \(a\) is positive unless it is zero. This proves the assertion, including the equality condition. The proof also gives \(b-rb\in Q^+\) when \(b\) is integral.

The same cone formula also proves the closed-chamber assertion needed for singular blocks. If $c$ and $d=rc$ are both weakly dominant integral, then (8.228) gives $c-d\in Q^+$ and, applied to $d,r^{-1}$, gives $d-c\in Q^+$. The simple roots are linearly independent, so this cone is pointed and $c=d$. Applying $w_0$ proves uniqueness of a weakly anti-dominant orbit point. For weakly dominant $b$ it is $w_0b$; every other $wb$ has a strictly positive simple-coroot coordinate. Applying (8.228) to $r=w_0w$ and then applying $-w_0$, which preserves $Q^+$, gives $wb-w_0b\in Q^+$, nonzero for distinct points. Subtracting $\rho$ proves the required minimality in the dot orbit.

**Lemma 8.18 (coatom containing a subword).** If \(y<w\) in reduced-subword order, some \(z\) satisfies
\[
y\le z<w,\qquad \ell(z)=\ell(w)-1.
\tag{8.229}
\]
Here is a proof from the existing subword theorem. A simple lifting consequence needed in it is:
\[
u\le c,\quad ut>u,\quad ct<c\quad\Longrightarrow\quad ut\le c.
\tag{8.230}
\]
Choose a reduced word \(c=Ct\). A selected reduced word for \(u\) inside this word cannot use the final letter: if it did, \(u\) would have a reduced word ending in \(t\), contrary to \(ut>u\). Select \(u\) in \(C\) and append the final \(t\). This selected word is reduced and gives \(ut\), proving (8.230).

Induct on \(\ell(w)\), and write \(w=vt\) reduced. If \(y\le v\), choose \(z=v\). Otherwise a selected reduced word for \(y\) in this particular word must use the last letter. Thus \(y=ut\) is reduced and \(u\le v\). Since \(y<w\), \(u<v\). By induction choose a coatom \(c<v\) with \(u\le c\). If \(ct<c\), (8.230) gives \(y=ut\le c\le v\), a contradiction. Thus \(ct>c\). Set \(z=ct\). A selected reduced word for \(c\) inside \(v\), followed by \(t\), proves \(z\le w\) and \(\ell(z)=\ell(w)-1\). A selected reduced word for \(u\) in \(c\), followed by \(t\), proves \(y\le z\). This completes the induction.

Repeated application gives a chain from \(y\) to \(w\) increasing length one at each step. Each step \(z<w\) with length difference one deletes exactly one letter from a chosen reduced word for \(w\). If that letter is in position \(j\), then
\[
z=s_\beta w,\qquad
\beta=s_{i_1}\cdots s_{i_{j-1}}\alpha_{i_j}\in\Phi^+.
\]
Since the length decreased, strong exchange's converse applied to \(w^{-1}\) gives \(w^{-1}\beta\in\Phi^-\). For strictly dominant integral \(a\),
\[
za-wa=-\langle wa,\beta^\vee\rangle\beta\in Q^+\setminus\{0\}.
\]
Adding along the chain proves
\[
y\le w\ \Longrightarrow\ ya-wa\in Q^+,\qquad
y<w\ \Longrightarrow\ ya\ne wa,\ ya-wa\in Q^+\setminus\{0\}.
\tag{8.231}
\]
This does not assume that the converse implication between weight order and Bruhat order holds.

**Lemma 8.19 (extremal norm).** If \(F\) is the finite simple module having an extremal weight \(\delta\), every weight \(\eta\) of \(F\) satisfies
\[
\|\eta\|\le\|\delta\|;
\quad\|\eta\|=\|\delta\|\Longrightarrow\eta\in W\delta.
\tag{8.232}
\]
Every weight in \(W\delta\) has multiplicity one. The actual weight-polytope theorem puts \(\eta\) in \(\operatorname{conv}(W\delta)\), and Weyl symmetry transfers the top multiplicity one to every extremal point. For a convex expression \(\eta=\sum_j t_j\delta_j\), \(t_j\ge0,\sum t_j=1,\delta_j\in W\delta\),
\[
\|\eta\|^2=\|\delta\|^2-\tfrac12\sum_{i,j}t_it_j\|\delta_i-\delta_j\|^2.
\]
Equality forces every orbit point with nonzero coefficient to be the same point, proving the norm assertion. This explicit identity excludes extra interior weights in the forthcoming block selection.

#### 8.12.3. Tensoring a Verma module gives the actual flag

For a finite module \(F\), the natural map
\[
U(\mathfrak g)\otimes_{U(\mathfrak b)}
(F|_{\mathfrak b}\otimes\mathbb C_\xi)
\longrightarrow F\otimes M(\xi),
\qquad
u\otimes(f\otimes1)\longmapsto u(f\otimes v_\xi)
\tag{8.233}
\]
is well-defined. PBW identifies both vector spaces with
\(U(\mathfrak n^-)\otimes F\).
Filter by negative-root PBW degree. In expanding the diagonal action, the term with the full PBW degree on the Verma factor is \(f\otimes uv_\xi\); every other term has smaller degree there. The associated-graded map is factor interchange and is an isomorphism. Induction on degree proves both injectivity and surjectivity.

Order the finite weight set of \(F\) so that higher weights precede lower weights. The span of an initial set is stable under \(\mathfrak n^+\), which raises weights. Refine each weight space one dimension at a time. Cartan operators are scalar there, and its positive-root images already lie in earlier spaces. This is a complete \(\mathfrak b\)-stable flag with one-dimensional quotients \(\mathbb C_\eta\), repeated according to \(\dim F_\eta\). PBW makes \(U(\mathfrak g)\) right free over \(U(\mathfrak b)\), so induction of this flag is exact. Equation (8.233) therefore gives Verma factors
\[
M(\xi+\eta),\quad\eta\in\operatorname{Wt}F,
\quad\text{each with multiplicity }\dim F_\eta.
\tag{8.234}
\]
The order can be chosen compatibly with the weight partial order, not just with an arbitrary complete flag from Lie's theorem.

Apply an exact central projection to the flag. A Verma module has scalar central character, so its projection is itself if that character is selected and zero otherwise. Omitting the zero steps gives an actual Verma filtration in the target block. Consequently tensor-and-project takes every Verma-filtered object to a Verma-filtered object; tensor its given finite filtration first, then use (8.234) on each quotient. No statement about Grothendieck classes is substituted for the construction of these filtrations.

#### 8.12.4. Construction of a simple-wall pair and exact Verma effects

Fix a dominant integral \(\lambda\) and a simple reflection \(s=s_i\). Put
\[
a=\lambda+\rho,\quad
m=\langle a,\alpha_i^\vee\rangle=\langle\lambda,\alpha_i^\vee\rangle+1,
\quad d=m\omega_i,\quad
b=a-d,\quad \mu=b-\rho.
\tag{8.235}
\]
Here \(m\) is a positive integer and \(\omega_i\) is the full fundamental weight. The coordinates of \(b\) are zero at \(i\) and positive at every other simple coroot. Thus \(b\) is in the interior of that simple wall and \(\operatorname{Stab}_W(b)=\{1,s\}\). This stabilizer assertion follows directly from (8.228): if \(rb=b\), its sum of nonnegative multiples of positive roots is zero, so every coefficient is zero. Every letter in a reduced word for \(r\) must therefore be \(s_i\). Reducedness leaves only the empty word or that single letter; both fix \(b\). No separate face-stabilizer theorem is being invoked.

Let \(E=L(d)\), a finite-dimensional module, and use its ordinary contragredient \(E^*\). This is the simple finite module whose extremal weight is \(-d\). Define on all objects of the respective blocks
\[
T_{\rm on}X=\operatorname{pr}_{\chi_\mu}(E^*\otimes X),
\qquad
T_{\rm out}Y=\operatorname{pr}_{\chi_\lambda}(E\otimes Y),
\qquad
\theta_s=T_{\rm out}T_{\rm on}.
\tag{8.236}
\]
These are the actual wall translations chosen in this proof. Section 8.12.1 proves exactness and their well-definedness.

**Theorem 8.11 (actual simple-wall translations).** For every \(w\in W\),
\[
T_{\rm on}M(w\cdot\lambda)\cong M(w\cdot\mu),
\tag{8.237}
\]
and \(T_{\rm out}M(w\cdot\mu)\) has exactly the two Verma factors
\[
M(w\cdot\lambda),\quad M(ws\cdot\lambda),
\quad\text{each once}.
\tag{8.238}
\]
These are actual filtrations, not only their characters.

**Proof of (8.237).** By Section 8.12.3 and Harish-Chandra, a tensor weight \(\eta\) survives precisely if
\[
wa+\eta=tb\quad\text{for some }t\in W.
\]
Since \(\eta\) is a weight of \(E^*\), Lemma 8.19 gives \(\|\eta\|^2\le\|d\|^2\). On the other hand Lemma 8.17 gives
\[
\|\eta\|^2=\|a\|^2+\|b\|^2-2(wa,tb)
\ge\|a\|^2+\|b\|^2-2(a,b)=\|d\|^2.
\]
Equality therefore holds. Its equality condition gives \(w^{-1}tb=b\), so \(\eta=w(b-a)=-wd\). Conversely this is an extremal weight of \(E^*\), occurs once, and produces \(w\cdot\mu\). Thus the selected Verma flag has a single quotient and is exactly that Verma module.

**Proof of (8.238).** A weight \(\eta\) of \(E\) survives precisely if \(wb+\eta=ta\). The same norm argument gives equality in \((ta,wb)\le(a,b)\). It implies \(t^{-1}wb=b\), so \(t=w\) or \(t=ws\). The two weights are \(wd\) and \(wsd\), because \(sb=b\). They are distinct: \(sd\ne d\), since \(\langle d,\alpha_i^\vee\rangle=m>0\). Each occurs once and both survive. This proves (8.238).

If \(ws>w\), then \(w\alpha_i>0\), and
\[
w\cdot\lambda-ws\cdot\lambda=m\,w\alpha_i\in Q^+\setminus\{0\}.
\]
The compatible weight flag in Section 8.12.3 puts the former factor first. Hence in this case there is an actual short exact sequence
\[
0\longrightarrow M(w\cdot\lambda)
\longrightarrow T_{\rm out}M(w\cdot\mu)
\longrightarrow M(ws\cdot\lambda)\longrightarrow0.
\tag{8.239}
\]
For \(ws<w\), the same statement has \(w\) and \(ws\) interchanged. In particular
\[
\theta_sM(w\cdot\lambda)
\cong T_{\rm out}M(w\cdot\mu)
\cong\theta_sM(ws\cdot\lambda).
\tag{8.240}
\]
The isomorphisms use \(w\cdot\mu=ws\cdot\mu\). Nonsplitting of every sequence (8.239) is not needed or asserted here.

Thus the right coset \(w\{1,s\}\), not a left coset, controls this indexing. On characters and ungraded Verma multiplicities, the operation replaces a label \(w\) by \(w\) and \(ws\).

#### 8.12.5. Both adjunctions and preservation of projectives

Finite tensor adjunction, defined by contraction with a basis and its dual, gives natural isomorphisms
\[
\operatorname{Hom}(E^*\otimes X,Y)
\cong\operatorname{Hom}(X,E\otimes Y),
\qquad
\operatorname{Hom}(Y,E^*\otimes X)
\cong\operatorname{Hom}(E\otimes Y,X).
\tag{8.241}
\]
The first is the usual right adjunction of tensoring with a finite vector space; the second is its left adjunction. The ordinary dual Lie action on \(E^*\) makes both maps \(\mathfrak g\)-equivariant.

For \(X\in\mathcal O_\lambda\), \(Y\in\mathcal O_\mu\), maps involving all other central summands vanish by Section 8.12.1. Inserting the projections therefore gives
\[
\operatorname{Hom}(T_{\rm on}X,Y)
\cong\operatorname{Hom}(X,T_{\rm out}Y),\qquad
\operatorname{Hom}(Y,T_{\rm on}X)
\cong\operatorname{Hom}(T_{\rm out}Y,X).
\tag{8.242}
\]
They are natural in both variables and retain the evaluation/coevaluation units and counits from finite tensor adjunction followed by the canonical projections. Hence \(T_{\rm on}\) and \(T_{\rm out}\) are biadjoint, and \(\theta_s\) is self-adjoint.

If \(P\) is projective in its block, the Hom functor from \(T_{\rm on}P\) is the composition of the exact Hom functor from \(P\) and the exact \(T_{\rm out}\). Thus \(T_{\rm on}P\) is projective. The other adjunction proves the analogous assertion for \(T_{\rm out}\); consequently \(\theta_s\) preserves projectives. A projective in a central-character category is also projective in all of O, because exact projection identifies its Hom functor with Hom into that projection.

#### 8.12.6. Constructing every anti-dominant big projective

This section also proves the central-character categories used above are indecomposable. Let \(b\) be any weakly dominant integral weight, put
\[
\nu=b-\rho,\qquad
\nu^-=w_0b-\rho=w_0\cdot\nu,\qquad J=\operatorname{Stab}(b).
\]
This includes the regular case \(b=\lambda+\rho\), the simple wall of Section 8.12.4, and \(b=0\).

The most-singular module \(M(-\rho)\) is simple. Indeed its dot orbit is the singleton \(\{-\rho\}\). Any nonzero proper submodule has, by the bounded-weight support and finite-length arguments in Sections 1–2, a highest vector of some lower weight. Its central character forces that weight to be \(-\rho\). But the unique top line generates the whole Verma module, a contradiction. The same highest-weight-space argument used in RT-LIE-18, Lemma 3.1, proves \(M(-\rho)\) projective: on this singleton block,
\[
\operatorname{Hom}(M(-\rho),X)=X_{-\rho}
\]
is exact. Exact projection makes it projective in all of O.

Define the actual tensor projective
\[
Q_\nu=\operatorname{pr}_{\chi_\nu}\bigl(L(b)\otimes M(-\rho)\bigr).
\tag{8.243}
\]
It is projective by Section 8.12.1 and finite tensor adjunction. Section 8.12.3 gives its Verma factors \(M(-\rho+\eta)\) for the weights of \(L(b)\) which survive. Harish-Chandra says survival is \(\eta\in Wb\). Every such extremal weight occurs once. Therefore
\[
(Q_\nu:M(w\cdot\nu))=1
\quad\text{for each distinct }wJ,\quad
\text{and no other factors occur.}
\tag{8.244}
\]

We prove its head consists solely of \(L(\nu^-)\). If \(wb\ne w_0b\), some simple coroot has \(\langle wb,\alpha_i^\vee\rangle>0\): otherwise \(wb\) would be the unique representative in the closed anti-dominant chamber. Integrality makes this integer at least one, so
\(\langle w\cdot\nu,\alpha_i^\vee\rangle\ge0\).
The simple module \(L(w\cdot\nu)\) is locally finite for that simple-root \(\mathfrak{sl}_2\), as follows directly.

For a simple highest-weight module of highest weight \(\gamma\), if \(\gamma(h_i)=n\ge0\), the vector \(f_i^{n+1}v_\gamma\) is singular: the rank-one formula kills its \(e_i\)-image and \([e_j,f_i]=0\) kills every other \(e_j\)-image. Its generated submodule has highest weight below \(\gamma\), so simplicity forces it to be zero. The locally nilpotent derivation \(\operatorname{ad} f_i\) on \(U(\mathfrak g)\), together with
\[
f_i^N(uv)=\sum_k\binom Nk(\operatorname{ad}f_i)^k(u)f_i^{N-k}v,
\]
makes \(f_i\) locally nilpotent on the whole simple module. The raising operator is locally nilpotent in O. For each weight vector, PBW for this \(\mathfrak{sl}_2\) now shows its generated space is finite-dimensional: only finitely many \(e_i^c v\) occur; each is killed by a bounded power of \(f_i\), and powers of \(h_i\) act scalarly on the weight vectors. Thus the assertion is actual local finiteness.

Finite tensoring and taking subquotients preserve this local finiteness. A locally finite \(\mathfrak{sl}_2\)-module cannot contain a highest vector of \(h_i\)-weight \(-1\), by the proved finite rank-one classification: put the vector in its finite-dimensional generated submodule and decompose it into rank-one simples. Hence
\[
\begin{aligned}
\operatorname{Hom}(Q_\nu,L(w\cdot\nu))
&=\operatorname{Hom}(L(b)\otimes M(-\rho),L(w\cdot\nu))\\
&\cong\operatorname{Hom}(M(-\rho),L(b)^*\otimes L(w\cdot\nu))
=0
\end{aligned}
\tag{8.245}
\]
for every non-anti-dominant label. Central projection was omitted in the first Hom only because the target lies in its selected block. The last vanishing uses the \(h_i\)-weight \(-1\) of the \(-\rho\) highest vector.

Projective-cover classification thus gives \(Q_\nu\cong P(\nu^-)^{\oplus k}\) for a positive integer \(k\): it is a nonzero finite-length projective, and its only possible simple head is \(L(\nu^-)\). Compare the \(M(\nu)\) coefficient by actual BGG reciprocity:
\[
1=(Q_\nu:M(\nu))
=k(P(\nu^-):M(\nu))
=k[M(\nu):L(\nu^-)].
\]
Both integers on the last side are nonnegative and \(k>0\), so \(k=1\). We have proved
\[
\boxed{Q_\nu=P(\nu^-),\qquad
(P(\nu^-):M(w\cdot\nu))=1\quad(wJ\in W/J).}
\tag{8.246}
\]
This proves rather than assumes the anti-dominant big projective and the multiplicity-one property.

BGG reciprocity immediately gives
\[
[M(w\cdot\nu):L(\nu^-)]=1,\qquad
\dim\operatorname{Hom}(P(\nu^-),M(w\cdot\nu))=1,
\qquad
\dim\operatorname{End}(P(\nu^-))=|W/J|.
\tag{8.247}
\]
For the last equality, compute the multiplicity of \(L(\nu^-)\) along the actual Verma flag (8.246) and use the projective Hom/composition formula. This is a dimension result only; it does not supply the corner algebra's multiplication or its coinvariant presentation.

Every distinct simple in this central-character category is a composition factor of \(Q_\nu\), since its own Verma module is a flag quotient. The indecomposable \(Q_\nu\) cannot have its composition factors in distinct categorical summands: the exact canonical block projections would split it. Thus all simples belong to one indecomposable block. Any further nonzero summand would have a simple by finite length. This proves indecomposability of \(\mathcal O_\nu\).

The construction also gives self-duality. Restricted duality \(D\) fixes finite simples and fixes \(M(-\rho)\), which is simple. On a finite tensor product, weightwise duality gives
\[
D(F\otimes X)\cong DF\otimes DX:
\]
each weight space is a finite direct sum, ordinary finite-dimensional tensor duality applies to each term, and the Chevalley anti-involution commutes with the primitive coproduct. The finite module \(DF\) has the same highest weight as \(F\), hence is \(F\) for simple \(F\). Duality commutes with block projection: it fixes the simple composition factors and thus preserves their generalized-character category. Therefore
\[
DP(\nu^-)\cong P(\nu^-).
\tag{8.248}
\]
Duality turns a projective into an injective by its exact bidual equivalence. Hence this big projective is also injective. No corner-ring theorem is used.

For later use, the anti-dominant Verma \(M(\nu^-)\) is simple as well. Every other point of its dot orbit is above it, by (8.228) transported by \(w_0\). A proper Verma submodule would have a highest weight below it with the same central character, an impossibility; equality would contain its top generator. The module is free over \(U(\mathfrak n^-)\), so \(f_i^N v_{\nu^-}\ne0\) for every \(i,N\). In positive rank this simple is not locally finite for any simple-root \(\mathfrak{sl}_2\). This last statement also follows because its highest \(h_i\)-weight is at most \(-1\).

#### 8.12.7. Big-projective wall effects and the kernel of the structure functor

Retain the simple wall of Section 8.12.4. Let
\[
P_-=P(w_0\cdot\lambda),\qquad
P_{\mu,-}=P(w_0\cdot\mu).
\]
Both have every distinct Verma label in their block exactly once by Section 8.12.6.

**Theorem 8.12 (big-projective wall effects).**
\[
T_{\rm out}P_{\mu,-}\cong P_-,
\qquad
T_{\rm on}P_-\cong P_{\mu,-}^{\oplus2},
\qquad
\theta_sP_-\cong P_-^{\oplus2}.
\tag{8.249}
\]
For the first assertion, biadjunction gives
\[
\operatorname{Hom}(T_{\rm out}P_{\mu,-},L(y\cdot\lambda))
\cong\operatorname{Hom}(P_{\mu,-},T_{\rm on}L(y\cdot\lambda)).
\]
If \(y\ne w_0\), the regular simple is locally finite for some simple-root \(\mathfrak{sl}_2\), by the argument of Section 8.12.6. Its image under \(T_{\rm on}\) remains so. All subquotients remain locally finite, whereas the singular anti-dominant simple \(L(w_0\cdot\mu)=M(w_0\cdot\mu)\) is not. Therefore the displayed Hom vanishes, by the actual projective Hom/composition formula. Since \(T_{\rm out}\) preserves projectives, its image consists only of copies of \(P_-\). Each singular Verma label produces the two regular labels of its right coset exactly once; together these cover \(W\) exactly once. The coefficient of \(M(\lambda)\) is therefore one. Since the same coefficient in \(P_-\) is one, there is exactly one copy.

For the second assertion use the other adjunction. A non-anti-dominant simple in the singular block is locally finite for some simple-root \(\mathfrak{sl}_2\), and \(T_{\rm out}\) preserves that property; it has no regular anti-dominant simple factor. The image \(T_{\rm on}P_-\) therefore consists only of copies of \(P_{\mu,-}\). Theorem 8.11 collapses each two-element coset of its regular Verma flag to the same singular Verma, giving two copies of every singular Verma label. The coefficient of \(M(\mu)\) is two, so there are exactly two copies. Composition proves the third assertion.

In particular this last assertion could also be proved directly by self-adjointness and local finiteness, then comparing the \(M(\lambda)\) coefficient. It has not been inferred from a structure-functor or bimodule comparison.

Let
\[
\mathbb V X=\operatorname{Hom}(P_-,X).
\]
This is an exact functor, and
\[
\dim_{\mathbb C}\mathbb V X=[X:L(w_0\cdot\lambda)].
\tag{8.250}
\]
Thus its kernel is the Serre subcategory of objects without that simple composition factor. Self-adjointness and (8.249) give
\[
\operatorname{Hom}(P_-,\theta_sX)
\cong\operatorname{Hom}(\theta_sP_-,X)
\cong\operatorname{Hom}(P_-^{\oplus2},X).
\tag{8.251}
\]
Hence \(\theta_s\) preserves \(\ker\mathbb V\). This is a statement of exact functors and underlying vector spaces after choosing the projective isomorphism; it does not identify the induced corner-ring action with two diagonal copies. The required corner-ring restriction/induction compatibility is owned by the separate transfer proof.

The same proof with the first two isomorphisms in (8.249) gives, as vector-space functors,
\[
\mathbb V_\mu T_{\rm on}\cong\mathbb V_\lambda,\qquad
\mathbb V_\lambda T_{\rm out}\cong\mathbb V_\mu^{\oplus2}.
\tag{8.252}
\]
Thus both functors preserve the corresponding kernels between the two blocks. All functors therefore descend to their abelian Serre quotients; their adjunctions descend as well because both adjoints preserve the kernels. One can prove this last assertion directly: the unit and counit natural maps descend under the exact quotient functors, and the triangle identities still hold there. Equation (8.252), like (8.251), does not identify the corner-ring actions.

#### 8.12.8. Generation and unique maximal projective summand

Fix a reduced expression \(w=s_1\cdots s_k\), and form the actual object
\[
Q_{\mathbf w}=\theta_{s_k}\cdots\theta_{s_1}M(\lambda).
\tag{8.253}
\]
The rightmost functor is applied first. Since \(\lambda\) is maximal in its dot orbit, \(M(\lambda)\) is projective by its exact highest-weight functor; its simple head makes it the cover \(P(\lambda)\). Thus \(Q_{\mathbf w}\) is projective by Section 8.12.5.

Apply the actual Verma filtrations of Section 8.12.4 successively. Its ungraded Verma multiplicities count subexpressions: at a step labelled \(s_i\), each preceding factor with label \(y\) contributes factors labelled \(y\) and \(ys_i\), with coefficient one. This remains valid for a right descent: the two labels are merely reordered in (8.239). Every subexpression product has a reduced expression selected from the literal word, by the existing deletion/subword lemma. Hence
\[
(Q_{\mathbf w}:M(y\cdot\lambda))=0\quad(y\nleq w),
\qquad
(Q_{\mathbf w}:M(w\cdot\lambda))=1.
\tag{8.254}
\]
The coefficient one follows because any proper selection uses fewer than \(k=\ell(w)\) letters and cannot have value of length \(k\); the full selection has value \(w\). The multiplicities are nonnegative actual filtration multiplicities throughout.

Decompose the finite projective \(Q_{\mathbf w}\) into projective covers. If \(P(y\cdot\lambda)\) occurs, its own factor \(M(y\cdot\lambda)\) occurs once by BGG reciprocity and the one-dimensional highest line in that Verma module. Consequently \(y\le w\). If \(y<w\), then (8.231) gives
\[
y\cdot\lambda>w\cdot\lambda
\]
in weight order. The highest weight of \(L(y\cdot\lambda)\) therefore does not occur in \(M(w\cdot\lambda)\), all of whose weights are below \(w\cdot\lambda\). BGG reciprocity gives
\[
(P(y\cdot\lambda):M(w\cdot\lambda))
=[M(w\cdot\lambda):L(y\cdot\lambda)]=0.
\]
Only \(P(w\cdot\lambda)\) can contribute the coefficient in (8.254), and its contribution is one. We have proved
\[
\boxed{Q_{\mathbf w}\cong P(w\cdot\lambda)\oplus
\bigoplus_{y<w}P(y\cdot\lambda)^{\oplus n_y},
\quad n_y\ge0.}
\tag{8.255}
\]
The maximal summand occurs once. All other labels have shorter length, so it is equivalently the unique indecomposable summand not isomorphic to a cover of smaller length. Every projective cover occurs by choosing a reduced expression for its label; all finite projectives are finite sums of these covers. This is actual generation by the wall functors and summand closure.

For completeness, \(Q_{\mathbf w}\) is also projective-injective when the starting object is replaced by \(P_-\): its start is projective-injective by Section 8.12.6 and each biadjoint exact wall functor preserves both properties. But in that case (8.249) gives only \(2^k\) copies of \(P_-\), and so it supplies no generation assertion for the other projectives.

### 8.13. Invariant jets at a regular finite orbit

The regular finite-orbit argument proves the central surjection by finite Chinese remainders and averaging. Compare [Soergel, MPI/89-46, §2.2, Endomorphismensatz 7(i), printed p.11](https://archive.mpim-bonn.mpg.de/id/eprint/3653/1/preprint_1989_46.pdf).

#### 8.13.1. Arbitrary jets at a free finite-group orbit

Let $k$ be a field of characteristic zero, $V$ a finite-dimensional $k$-vector space, and $W$ a finite linear group. Suppose $\delta\in V(k)$ has trivial stabilizer. Write $S=k[V]$, and let $\mathfrak m_a$ be the ideal of polynomials vanishing at $a\in V(k)$. **Proposition 8.7 (free-orbit invariant jets).** For every polynomial $g\in S$ and integer $N\ge0$, there is an invariant polynomial $f\in S^W$ such that

\[
f(\delta+h)\equiv g(h)\pmod{\mathfrak m_0^{N+1}}.
\tag{8.256}
\]

**Proof.** The points $w\delta$ are distinct. The ideals of distinct rational points are comaximal: a linear coordinate distinguishing $a$ and $b$, rescaled and shifted, is zero at $a$ and one at $b$, so $1$ is a sum of an element of $\mathfrak m_a$ and an element of $\mathfrak m_b$. Their powers $\mathfrak m_a^{N+1}$ and $\mathfrak m_b^{N+1}$ are also comaximal. Indeed, writing $1=u+v$ with $u\in\mathfrak m_a$, $v\in\mathfrak m_b$, expand $(u+v)^{2N+1}$; every monomial contains at least $N+1$ factors of $u$ or at least $N+1$ factors of $v$.

The finite Chinese remainder construction therefore supplies a polynomial $p$ whose jet at every orbit point is prescribed by

\[
p(X)\equiv g\bigl(w^{-1}(X-w\delta)\bigr)
\pmod{\mathfrak m_{w\delta}^{N+1}}
\qquad(w\in W).
\tag{8.257}
\]

For completeness, the construction is onto for two comaximal ideals $I,J$: choose $u\in I$, $v\in J$ with $u+v=1$; for desired residue lifts $a,b$, the polynomial $va+ub$ has residues $a$ modulo $I$ and $b$ modulo $J$. Induct on the finite family. Pairwise comaximality makes the intersection of the preceding ideals comaximal with the next one, since a product of choices equal to one modulo that next ideal belongs to the preceding intersection. This proves the finite simultaneous assertion used in (8.257).

Average using the inverse-variable action:

\[
f(X)=\frac1{|W|}\sum_{w\in W}p(w^{-1}X).
\tag{8.258}
\]

Replacing $X$ by $aX$ permutes the summands, so $f\in S^W$. At $X=\delta+h$, the summand indexed by $w$ is evaluated at $w^{-1}\delta+w^{-1}h$. Apply (8.257) at the point $w^{-1}\delta$, using the index $w^{-1}$: its prescribed jet is $g(w(w^{-1}h))=g(h)$. A linear invertible substitution carries the ideal power at that point to $\mathfrak m_0^{N+1}$. Thus every summand has the same desired jet, and the average proves (8.256). $\square$

#### 8.13.2. A finite homogeneous quotient permits exact interpolation

Let $I\subset S$ be a homogeneous ideal such that $A=S/I$ is finite-dimensional and $A_0=k$, with all coordinate functions of positive degree. Its positive-degree ideal is nilpotent. To see this explicitly, $A$ has finitely many nonzero homogeneous degrees, say none beyond $D$; a product of more than $D$ positive-degree elements has degree greater than $D$ and vanishes. Consequently $\mathfrak m_0^{N+1}\subset I$ for some integer $N$.

With $\delta$ as in Section 8.13.1, the map

\[
S^W\longrightarrow A,\qquad
f\longmapsto [h\mapsto f(\delta+h)]
\tag{8.259}
\]

is a surjective algebra homomorphism. It is an algebra homomorphism because translation followed by quotient preserves sums and products. Given a class in $A$, choose a polynomial representative $g$ and apply Section 8.13.1 with $\mathfrak m_0^{N+1}\subset I$. Its congruence is equality in $A$, proving surjectivity. No freeness of $S$ over $S^W$ is assumed.

#### 8.13.3. The finite-Weyl coinvariant application

Put $S=k[V]$ and

\[
C=S/(S^W_{>0}S).
\tag{8.260}
\]

This quotient is finite-dimensional without a polynomial invariant-ring theorem. Choose coordinate generators $x_1,\ldots,x_r$ of $S$. Each $x_i$ satisfies the monic orbit polynomial

\[
\prod_{w\in W}(T-wx_i)\in S^W[T].
\tag{8.261}
\]

Reducing powers with these monic equations shows that the finitely many monomials $x_1^{a_1}\cdots x_r^{a_r}$ with $0\le a_i<|W|$ span $S$ over $S^W$. Passing to the quotient by positive-degree invariants therefore leaves a finite-dimensional $k$-span. The quotient is graded with degree-zero part $k$, so Section 8.13.2 applies.

For a finite Weyl group and a dominant integral weight $\lambda$, let $\delta=\lambda+\rho$ in the real root span, complexified if $k=\mathbb C$. This point lies in the interior of the dominant chamber, since $\delta(\alpha_s^\vee)=\lambda(\alpha_s^\vee)+1>0$ for every simple reflection. The free action on chambers, proved in Lesson8, makes its stabilizer trivial. Thus

\[
S^W\longrightarrow C,\qquad
f\longmapsto[f(\lambda+\rho+h)]
\tag{8.262}
\]

is onto for every finite Weyl group, arbitrary rank and components. In rank zero both rings equal $k$, and the assertion is immediate.

Choose the shifted Harish-Chandra isomorphism $\gamma:Z(U\mathfrak g)\xrightarrow{\sim}S^W$ with $\chi_\lambda(z)=\gamma(z)(\lambda+\rho)$, supplied by Lesson15. Composition with (8.262) gives the exact central-to-coinvariant surjection

\[
Z(U\mathfrak g)\twoheadrightarrow C,\qquad
z\longmapsto[\gamma(z)(\lambda+\rho+h)].
\tag{8.263}
\]

The normalization is the one in Lesson 15: $\gamma(z)(t)=\xi(z)(t-\rho)$, where $\xi$ is triangular PBW projection. Hence
\[
\xi(z)(\lambda+h)=\gamma(z)(\lambda+\rho+h).
\]
Thus the translated source convention and the shifted invariant convention in (8.263) agree exactly. In rank one, with $\rho(h_i)=1$ and $\Omega=h_i^2+2h_i+4f_i e_i$, one has $\gamma(\Omega)(t)=t^2-1$. For $\lambda=n\ge0$ and $C=\mathbb C[h]/(h^2)$, the image is $n(n+2)+2(n+1)h$.

The annihilator and the endomorphism ring of the actual big projective are proved in Section 8.15; the interpolation here supplies their invariant-theory input.


### 8.14. Shapovalov determinants and ambient-root deformation

The following proof constructs the universal contravariant form, its determinant and first transverse pairing, then the nonsplit root-local extension and endomorphism order. Compare [Soergel, MPI/89-46, §2.2, Lemma 4](https://archive.mpim-bonn.mpg.de/id/eprint/3653/1/preprint_1989_46.pdf), [Fiebig v2, §2.4, Proposition 2.4 and §3.2, Lemma 3.5](https://arxiv.org/html/math/0305378v2), and [Etingof, MIT 18.757, Lecture 8, Exercise 8.15(iv)–(x), pp.45–47](https://ocw.mit.edu/courses/18-757-representations-of-lie-groups-fall-2023/mit18_757_f23_lec08.pdf).

#### 8.14.1. Exact transfer interface

Let \(\mathfrak g\) be finite-dimensional complex semisimple, with positive roots \(\Phi^+\), Cartan \(\mathfrak h\), positive Borel \(\mathfrak b\), Weyl group \(W\), and \(\rho=\frac12\sum_{\beta>0}\beta\). Use the invariant form on the real root span, extended complex bilinearly. For a dominant integral \(\lambda\), put \(p=\lambda+\rho\), which is strictly dominant. Let
\[
S=\operatorname{Sym}_{\mathbb C}(\mathfrak h),\qquad
A=S_{\mathfrak m_0},\qquad \tau\in\mathfrak h^*\otimes A
\]
be the tautological weight. Write \(\nu_w=wp-\rho=w\cdot\lambda\) and
\[
M_A(\nu_w)=U(\mathfrak g)\otimes_{U(\mathfrak b)}
A_{\nu_w+\tau}.
\tag{8.264}
\]
For every positive root \(\alpha\), define
\[
h_\alpha=\tau(\alpha^\vee),\quad
T_\alpha=A_{(h_\alpha)},\quad
k_\alpha=T_\alpha/h_\alpha T_\alpha,\quad K=\operatorname{Frac}A.
\tag{8.265}
\]
Here \(T_\alpha\) is a discrete valuation ring with uniformizer \(h_\alpha\), and \(k_\alpha\) is the rational function field of the root hyperplane. A polynomial ring is a unique factorization domain, its height-one principal-prime localization has valuations given by the exponent of that prime, and factoring out the prime gives the fraction field of its quotient; these descriptions prove the assertions directly.

Section 8.15 constructs
\[
P_A=\operatorname{pr}_{\chi_\lambda}
\bigl(L(p)\otimes M_A(-\rho)\bigr)
\]
and proves that it has every \(M_A(\nu_w)\) once in a free Verma flag, that its Hom functor over \(A\) and \(T_\alpha\) is exact on Verma-flag sequences and commutes with base change, and that \(P_A\otimes_A k_\alpha\) is projective in the actual residue category. The last assertion is proved by the singleton most-singular Casimir argument in Section 8.15.6; no global deformed-projectivity theorem is required. The present result is:

**Proposition 8.8 (ambient-root projective order).** The localized central projection splits \(P_{T_\alpha}\) into one summand for every unordered pair \(\{w,s_\alpha w\}\). Each summand has exactly those two Verma factors once. If its residue is projective, that residue is indecomposable. Consequently the endomorphism order of that summand, inside its generic two-eigenspace algebra \(K^2\), equals
\[
\mathcal C_\alpha=
\{(a,b)\in T_\alpha^2:a-b\in h_\alpha T_\alpha\},
\tag{8.266}
\]
The central image supplies \(\mathcal C_\alpha\) by Section 8.13, applied explicitly in Section 8.14.12. Actual residue projectivity at \(k_\alpha\) is the hypothesis needed by Section 8.14.10, proved in Section 8.15.6; projectivity or End base change only at \(\tau=0\) would be insufficient. Exactness on Verma-flag sequences over \(A,T_\alpha\), together with that residue statement, is the precise contract used in the corner comparison.

The actual pair lattice also has a nonsplit sequence with the upper Verma as submodule and the lower Verma as quotient. Its inclusion \(i\) admits a map \(j\) back with \(ji=h_\alpha\operatorname{id}\), as proved at the end of Section 8.14.12. Thus the statement includes the exact first-order extension on the specified pair lattice, not only an abstract residue indecomposability test.

PBW, highest-weight cyclic modules, the Chevalley anti-involution, the actual quadratic Casimir, and Harish-Chandra's polynomial central characters are the elementary enveloping/root foundations from Lessons 7–15. The needed deductions over rational function fields and local rings are proved below. No KL character theorem, deformed block theorem, Shapovalov determinant formula, Jantzen sum formula or nonsimple-root embedding theorem is assumed.

#### 8.14.2. Universal contravariant form and its actual radical

Fix the anti-involution \(\sigma\) fixing \(\mathfrak h\) and exchanging simple \(e_i,f_i\). The Chevalley relations are preserved under reversing products, so it extends to \(U(\mathfrak g)\). Opposite root vectors may be chosen compatibly with it; any nonzero scaling below only changes the constant of a determinant.

For a field \(F\) of characteristic zero and a highest weight \(\Lambda\in\mathfrak h_F^*\), PBW identifies \(M_F(\Lambda)\) with \(U(\mathfrak n^-)_F\). Let \(\pi\) be projection to \(U(\mathfrak h)\) in triangular PBW order. Define
\[
B_\Lambda(uv_\Lambda,u'v_\Lambda)
=\operatorname{ev}_\Lambda\pi(\sigma(u)u'),
\qquad u,u'\in U(\mathfrak n^-).
\tag{8.267}
\]
It is the normalized contravariant form: its top value is one, distinct weights are orthogonal, and
\[
B_\Lambda(xv,v')=B_\Lambda(v,\sigma(x)v').
\tag{8.268}
\]
These identities follow by commuting the triangular factors before applying \(\pi\); the positive-root factor annihilates the top generator, and the Cartan factor evaluates at \(\Lambda\). They can equivalently be checked on the defining induced-module relations, which proves well-definedness. Transposition has the same contravariance and top value. Contravariance moves all negative factors to the other argument and hence determines all values from the top value, so the form is symmetric.

Its radical is the unique maximal proper submodule. In fact the radical is a submodule by (8.268) and is proper by its top value. Any proper submodule has zero top weight. Pairing its vectors with \(uv_\Lambda\), and moving \(u\) across, reduces to their top component, still zero because they remain in that submodule. Thus every proper submodule lies in the radical. This proof works over any such field, including the rational fields in Section 8.14.1.

Let \(Q^+\) be the positive root lattice and let
\[
\mathsf P(\eta)=\#\{(a_\beta)_{\beta>0}\in\mathbb N^{\Phi^+}:
\textstyle\sum_\beta a_\beta\beta=\eta\},
\]
with value zero outside \(Q^+\). In root-ordered PBW bases, the weight-\(\Lambda-\eta\) form is a \(\mathsf P(\eta)\)-square matrix with polynomial entries in \(\Lambda\). Denote its determinant by \(D_\eta(\Lambda)\), with \(D_0=1\).

#### 8.14.3. Leading term: every root exponent is fixed before factorization

A PBW monomial indexed by the partition \(\mathbf a=(a_\beta)\) has length \(l(\mathbf a)=\sum a_\beta\). Each Cartan factor in the projection of \(\sigma(u_{\mathbf a})u_{\mathbf b}\) consumes at least one positive and one negative root factor. A bracket of nonopposite roots produces another root vector, rather than a Cartan factor, and consumes an extra root factor before a subsequent Cartan bracket. Hence
\[
\deg_\Lambda B_\Lambda(u_{\mathbf a}v,u_{\mathbf b}v)
\le \frac{l(\mathbf a)+l(\mathbf b)}2.
\tag{8.269}
\]
Equality requires every consumption to pair opposite roots directly. It therefore requires the two root multisets to agree, namely \(\mathbf a=\mathbf b\). On the diagonal the full-degree term is a nonzero constant times
\[
\prod_{\beta>0} a_\beta!\,
\Lambda(\beta^\vee)^{a_\beta}.
\]
Repeatedly commute a fixed opposite pair to see the factorial; all terms involving root or Cartan shifts have smaller Cartan degree. In a determinant term the sum of the bounds in (8.269) is \(\sum_{\mathbf a}l(\mathbf a)\). Equality at every entry forces the identity permutation. The leading term thus comes uniquely from the diagonal, and cannot cancel. Consequently
\[
\operatorname{in}D_\eta
=c_\eta\prod_{\beta>0}\Lambda(\beta^\vee)^{e_\beta(\eta)},
\qquad
e_\beta(\eta)=\sum_{n\ge1}\mathsf P(\eta-n\beta),
\quad c_\eta\ne0.
\tag{8.270}
\]
The exponent identity is exact: the sum of the multiplicities \(a_\beta\) over all partitions equals the sum, over \(n\ge1\), of the number of partitions with \(a_\beta\ge n\). Removing those \(n\) copies of \(\beta\) gives the displayed partition number. Only finitely many terms occur. This proves the degree and each directional leading exponent without assuming a determinant formula or an embedding.

#### 8.14.4. Casimir factorization, including the algebraic step

Normalize the Casimir so its highest-weight scalar is
\[
c(\Lambda)=(\Lambda+\rho,\Lambda+\rho)-(\rho,\rho).
\tag{8.271}
\]
The dual-root PBW expression consists of its Cartan polynomial plus positive-root terms \(2f_\beta e_\beta\) with the matching invariant-form normalization. Thus every singular vector of weight \(\Lambda-\gamma\) has scalar \(c(\Lambda-\gamma)\), whereas the entire Verma module has scalar \(c(\Lambda)\). Necessarily
\[
d_\gamma(\Lambda):=
2(\Lambda+\rho,\gamma)-(\gamma,\gamma)=0.
\tag{8.272}
\]

If \(D_\eta(\Lambda)=0\), its radical has a nonzero weight-\(\Lambda-\eta\) vector. Apply positive-root operators until a nonzero vector of maximal weight is reached. There are only finitely many weights between that vector and the top, so the process terminates. The resulting vector is singular of weight \(\Lambda-\gamma\), with \(0<\gamma\le\eta\). Thus every zero of \(D_\eta\) lies on one of the finitely many hyperplanes (8.272) with \(0<\gamma\le\eta\).

Here is the polynomial consequence, without a hidden geometric factorization assumption. Localize the polynomial ring \(\mathbb C[\mathfrak h^*]\) by the product of those linear polynomials. If \(D_\eta\) were a nonunit there, a maximal ideal containing it would give a finite-type field extension of \(\mathbb C\), hence a complex evaluation point at which all the inverted factors are nonzero and \(D_\eta\) vanishes, a contradiction. The field fact has a short proof. In a field finitely generated as an algebra, choose a maximal algebraically independent subset \(t_1,\ldots,t_r\) of its finite generators. The remaining generators are algebraic over \(\mathbb C(t_1,\ldots,t_r)\). Clear the finitely many denominators in their monic equations to make them integral over \(B=\mathbb C[t_1,\ldots,t_r,1/f]\). The whole field equals \(B\) with these generators adjoined, so is integral over \(B\). If an integral extension of a domain is a field, the domain is a field: for \(b\ne0\), a monic equation of \(b^{-1}\), multiplied by the appropriate power of \(b\), expresses \(b^{-1}\) in the domain. But if \(r>0\), choose \(a\in\mathbb C\) such that \(t_1-a\) does not divide \(f\); its inverse is absent from \(B\), a contradiction. Thus \(r=0\), the field is finite algebraic over \(\mathbb C\), and equals \(\mathbb C\). Unique factorization now says that every irreducible factor of \(D_\eta\) is one of the displayed linear polynomials.

Compare their leading linear factors with (8.270). Every \(\gamma\) that occurs must be parallel to a root. A root is primitive in the root lattice: it is a Weyl translate of a simple root, and the Weyl group acts by integral lattice automorphisms. Hence \(\gamma=n\beta\) for a positive root \(\beta\) and a positive integer \(n\). After nonzero constant rescaling, the factors are
\[
\ell_{\beta,n}(\Lambda)=\Lambda(\beta^\vee)+\rho(\beta^\vee)-n.
\]
Write their exponents as \(m_{\beta,n}(\eta)\ge0\). The leading directional exponent gives
\[
\sum_{n\ge1}m_{\beta,n}(\eta)
=\sum_{n\ge1}\mathsf P(\eta-n\beta)
\quad(\beta>0).
\tag{8.273}
\]
The next two sections determine each exponent and simultaneously prove existence of every nonsimple-root singular vector needed here.

#### 8.14.5. A generic factor hyperplane has exactly one simple Verma radical

Fix \(\alpha>0\), \(m\ge1\), and let \(F\) be the rational function field of the hyperplane
\[
\Lambda(\alpha^\vee)+\rho(\alpha^\vee)=m.
\tag{8.274}
\]
The weight \(\Lambda\) here is its generic point. For \(\gamma\in Q^+\setminus\{0\}\), equation \(d_\gamma(\Lambda)=0\) in \(F\) holds only when
\[
\gamma=m\alpha.
\tag{8.275}
\]
Indeed its linear part must vanish on the tangent hyperplane, forcing \(\gamma=t\alpha\); its constant part is then \(t(m-t)(\alpha,\alpha)\), forcing \(t=m\). This includes rank one, where the tangent space is zero and the same constant calculation applies.

Suppose at least one determinant has this hyperplane as a factor. The radical of \(M_F(\Lambda)\) is nonzero, and any nonzero submodule contains a singular vector by the finite positive-weight argument in Section 8.14.4. Its weight is forced by (8.275) to be
\[
\mu=\Lambda-m\alpha.
\]
The resulting map \(M_F(\mu)\to M_F(\Lambda)\) is injective. In PBW coordinates it is right multiplication by the nonzero singular-vector polynomial in \(U(\mathfrak n^-)_F\). That algebra is a domain: its PBW associated graded is the polynomial domain, so the highest filtered terms of two nonzero elements have nonzero product.

The lower Verma \(M_F(\mu)\) is simple. A proper submodule would have a singular vector of weight \(\mu-\epsilon\), \(\epsilon>0\). Its Casimir equation viewed in \(M_F(\Lambda)\) would require \(m\alpha+\epsilon=m\alpha\), impossible.

There cannot be two independent copies of this simple Verma in \(M_F(\Lambda)\). To see this without a Hom theorem or an Ore theorem, identify their images with left ideals \(U(\mathfrak n^-)u\) and \(U(\mathfrak n^-)v\). Write \(N=|\Phi^+|\). The total PBW filtration has dimension
\[
\dim F_jU(\mathfrak n^-)=\binom{j+N}{N}.
\]
Multiplication by either nonzero element is injective. Their two \(F_j\)-images lie in \(F_{j+d}\), where \(d\) bounds both element degrees. For large \(j\), twice the former dimension exceeds the latter; the images intersect nontrivially. Two simple submodules with nonzero intersection coincide. Their highest line is one-dimensional, so the two maps are scalar multiples.

Moreover the entire radical is this single copy. A vector in the radical can be raised to a singular vector, so all its weights are at or below \(\mu\). Its \(\mu\)-space is one-dimensional by the preceding argument. Quotient the radical by the constructed simple copy. If that quotient were nonzero, it would again have a singular vector; the only allowed weight is \(\mu\), whose space in that quotient is zero. Thus it is zero. We obtain the actual nonsplit sequence
\[
0\longrightarrow M_F(\mu)\longrightarrow M_F(\Lambda)
\longrightarrow L_F(\Lambda)\longrightarrow0.
\tag{8.276}
\]
The quotient is simple by Section 8.14.2, and the extension cannot split because the top vector generates the whole Verma. No BGG embedding criterion is used in this argument.

#### 8.14.6. The first transverse pairing is perfect

Choose \(\eta\in\mathfrak h^*\) with \(\eta(\alpha^\vee)=1\), and deform \(\Lambda\) to \(\Lambda(t)=\Lambda+t\eta\) over \(F[[t]]\). Identify each weight space by its PBW basis. Let \(N=M_F(\mu)\) be the radical just found. The coefficient of \(t\) in \(B_{\Lambda(t)}\), restricted to \(N\), is independent of the chosen lifts: changing a lift by \(t\) times any vector changes that coefficient by a value of \(B_\Lambda\) with one radical argument, hence by zero. Differentiating contravariance shows that this first pairing is contravariant on \(N\); the extra derivatives of the action also pair to zero against its radical arguments.

It remains to show its value on the highest line of \(N\) is nonzero. Suppose otherwise, and let \(z\) be its nonzero highest vector in degree \(m\alpha\). The specialized Gram matrix in that weight has kernel exactly \(Fz\), so the functional \(B'(z,-)\), which now annihilates that kernel, belongs to the image of the specialized Gram map. Correct \(z\) by a vector \(tz_1\) to obtain a homogeneous lift \(\widetilde z=z+tz_1\) satisfying
\[
B_{\Lambda(t)}(\widetilde z,-)=0\pmod{t^2}.
\tag{8.277}
\]
For each simple \(e_i\), contravariance pairs \(e_i\widetilde z\) to zero modulo \(t^2\) with its entire weight space. The form in that higher weight is invertible modulo \(t\), since the radical starts at \(m\alpha\). Therefore
\[
e_i\widetilde z=0\pmod{t^2}.
\]
The same holds for every positive-root operator, since the simple \(e_i\)'s generate them. The actual Casimir expression then makes \(\widetilde z\) a highest-weight vector modulo \(t^2\), with scalar \(c(\Lambda(t)-m\alpha)\). On the other hand its ambient Verma has scalar \(c(\Lambda(t))\). Their difference is
\[
2(\Lambda(t)+\rho,m\alpha)-(m\alpha,m\alpha)
=2t(\eta,m\alpha)\ne0\pmod{t^2}.
\tag{8.278}
\]
The coefficient is nonzero by the transverse choice. Equation (8.278) would annihilate \(\widetilde z\) modulo \(t^2\), contradicting \(z\ne0\). Thus its first pairing is a nonzero multiple of the lower Verma's normalized form, and is perfect in every weight because that lower Verma is simple.

For clarity, the determinant-order step is finite linear algebra. Choose a basis of the specialized radical and a complementary basis on which the specialized Gram matrix is invertible. The deformed matrix has blocks
\[
\begin{pmatrix}tC+O(t^2)&tE+O(t^2)\\
tE^{\mathsf T}+O(t^2)&D+O(t)\end{pmatrix},
\]
with \(C,D\) invertible. Its Schur complement has upper block \(tC+O(t^2)\). Its determinant order is exactly the radical dimension, not merely at least that dimension. Hence, whenever this hyperplane is a factor,
\[
m_{\alpha,m}(\nu)=\mathsf P(\nu-m\alpha).
\tag{8.279}
\]
At the first singular weight \(\nu=m\alpha\), this order is \(\mathsf P(0)=1\).

#### 8.14.7. Degree comparison forces the full determinant and every ambient root

For fixed \(\nu,\alpha\), every exponent in Section 8.14.4 is either zero or has the value in (8.279). In particular
\[
0\le m_{\alpha,m}(\nu)\le\mathsf P(\nu-m\alpha).
\]
Equation (8.273) says the finite sums of the two sides are equal. Every term must therefore be equal. This proves, at every weight,
\[
D_\nu(\Lambda)=c_\nu
\prod_{\alpha\in\Phi^+}\prod_{m\ge1}
\bigl(\Lambda(\alpha^\vee)+\rho(\alpha^\vee)-m\bigr)^{
\mathsf P(\nu-m\alpha)},\qquad c_\nu\ne0.
\tag{8.280}
\]
In particular every positive-root hyperplane appears already at \(\nu=m\alpha\). Sections 8.14.5–Section 8.14.6 consequently apply to every positive root, including nonsimple roots in the original Borel. This existence is deduced from the factorization and degree comparison; it was not assumed when computing either.

There is no rank restriction. Reducible root systems use the same PBW argument and Casimir with the orthogonal direct-sum form. Rank zero has no positive roots and no local assertion.

#### 8.14.8. Root-local specialization in the original ambient block

Fix the root \(\alpha\) in Section 8.14.1 and a pair \(\{w,s_\alpha w\}\). Since \(p\) is regular, \(wp(\alpha^\vee)\ne0\). Orient the pair so
\[
m=wp(\alpha^\vee)>0,\quad
\Lambda=\nu_w+\tau,\quad
\mu=\nu_{s_\alpha w}+\tau=\Lambda-m\alpha.
\tag{8.281}
\]
The difference is positive in the original Borel order, irrespective of whether \(\alpha\) is a simple ambient root.

Every factor of (8.280) for \(\beta\ne\alpha\) is a unit in \(T_\alpha\). If its constant term at zero is nonzero it is already a unit in \(A\). If that constant is zero, its nonzero linear part \(h_\beta\) is not divisible by \(h_\alpha\), because distinct positive roots have distinct coroot directions. Factors for \(\beta=\alpha\) and \(n\ne m\) also have nonzero constant term. The sole nonunit is
\[
\Lambda(\alpha^\vee)+\rho(\alpha^\vee)-m=h_\alpha.
\tag{8.282}
\]
Thus the form over \(T_\alpha\) has determinant valuation \(\mathsf P(\nu-m\alpha)\) in weight difference \(\nu\), and its residue radical has precisely that dimension. The first-order pairing is perfect. The lower Verma's forms are all invertible: its \(\alpha\)-pairing is \(-m+h_\alpha\), and has no positive-integer factor at the residue.

Writing bars for \(k_\alpha\)-specialization gives the actual sequences
\[
0\longrightarrow \overline M(\mu)
\longrightarrow\overline M(\Lambda)
\longrightarrow L(\Lambda)\longrightarrow0,
\tag{8.283}
\]
\[
0\longrightarrow L(\Lambda)
\longrightarrow\overline\nabla(\Lambda)
\longrightarrow L(\mu)\longrightarrow0,
\qquad \overline M(\mu)=L(\mu).
\tag{8.284}
\]
Restricted contravariant duality gives the second sequence from the first; both are nonsplit. The normalized form identifies \(L(\mu)\) with its restricted dual. In the ambient generic field \(K\), all root factors are nonzero and all these Verma modules are simple.

This is the required distinction from a rank-one calculation at \(\tau=0\): the calculation takes place at the generic point of each ambient root hyperplane, with all other root directions invertible. It is not obtained by changing the original Borel and asserting a correspondence without proof.

#### 8.14.9. An actual first-order two-Verma lattice

The first-order form also constructs an explicit lattice with the expected nonsplit two-Verma residue. This is useful independently of any projective classification.

Put \(M=M_{T_\alpha}(\nu_w)\) and let \(\nabla\) be its restricted contravariant dual, weight by weight. The normalized form gives an injection \(b:M\to\nabla\): its determinant is nonzero over \(K\), and the source is \(T_\alpha\)-torsion free. In each finite weight space, elementary row/column operations over the valuation ring diagonalize the matrix. One can prove this by choosing an entry of least valuation, clearing its row and column by division, and iterating. The number of nonunit diagonal entries is the residue corank, and their valuation sum is the determinant valuation. These are equal by Section 8.14.8; every nonunit entry therefore has valuation exactly one. Consequently
\[
h_\alpha\nabla\subset b(M),\qquad
\nabla/b(M)\cong L(\mu)
\tag{8.285}
\]
as \(k_\alpha\)-modules with the Lie action. To identify the second module intrinsically, reduce the form sequence: its kernel is \(L(\mu)\), and the cokernel is the restricted dual of that radical. Both are the same simple Verma by Section 8.14.8.

Let \(r:M_{T_\alpha}(\nu_{s_\alpha w})\twoheadrightarrow L(\mu)\) be reduction, and let \(c\colon\nabla\twoheadrightarrow L(\mu)\) be (8.285). Form the literal pullback
\[
E=\{(v,u)\in\nabla\oplus M_{T_\alpha}(\nu_{s_\alpha w}):c(v)=r(u)\}.
\tag{8.286}
\]
It has the two exact sequences
\[
0\to M\xrightarrow{\,v\mapsto(b(v),0)\,}E
\xrightarrow{\, (v,u)\mapsto u\,}M_{T_\alpha}(\nu_{s_\alpha w})\to0,
\tag{8.287}
\]
\[
0\to h_\alpha M_{T_\alpha}(\nu_{s_\alpha w})\to E
\xrightarrow{\, (v,u)\mapsto v\,}\nabla\to0.
\tag{8.288}
\]
The surjections follow directly from the pullback definition. All quotient weight spaces are free over \(T_\alpha\); the sequences are weightwise split and remain exact after reduction. Therefore \(\overline E\) contains the upper Verma and surjects onto its costandard, with one extra lower simple in each description.

The sequence (8.287) is nonsplit on the residue. If it split, \(\overline E\) would be \(\overline M(\Lambda)\oplus L(\mu)\). A map from the first summand to \(\overline\nabla(\Lambda)\) has image in its simple upper socle: every such map is determined by the upper highest vector, and its image is the normalized form image. A map from \(L(\mu)\) to that costandard is zero, since its socle is \(L(\Lambda)\). Such a direct sum cannot surject onto the costandard, contradicting (8.288).

In fact \(\overline E\) is indecomposable. A direct summand without an upper composition factor has only lower simple factors. Any such module is a direct sum of \(L(\mu)\)'s: its top-\(\mu\) vectors are singular, the simple Verma they generate splits off, and a quotient with zero top and only that allowed highest weight is zero. A nontrivial decomposition of \(\overline E\), whose upper multiplicity is one, would therefore have a lower simple summand. Maps from the upper Verma to that summand vanish, so (8.287) would embed its whole upper Verma into the remaining length-two summand, making that summand the upper Verma itself. This is the split case already excluded.

This constructs the nonsplit root-local extension with a genuine first-order parameter. It is not claimed to be projective solely because it has two flags. The next argument applies directly to the projective residue proved in Section 8.15.6 and proves the needed indecomposability there.

There are also literal normalized maps on this constructed lattice. Let \(i:M\to E\) be (8.287), and define
\[
j:E\longrightarrow M,\qquad j(v,u)=h_\alpha b^{-1}(v).
\tag{8.289}
\]
Although \(b^{-1}\) is initially defined over \(K\), (8.285) makes this composite integral. It commutes with the Lie action, and \(ji=h_\alpha\operatorname{id}_M\). Thus \((ij)^2=h_\alpha(ij)\) on \(E\). This supplies an actual two-Verma lattice with the first-order relation, without claiming its projectivity before the separate projective argument.

#### 8.14.10. Projective residue with these flags is necessarily indecomposable

Let \(Q\) be the residue of one localized summand of the deformed big-projective family of Section 8.15.6. The actual projectivity of \(P_A\otimes_A k_\alpha\) makes its summand \(Q\) projective. Its one-of-each Verma flag and Section 8.14.8 give
\[
[Q:L(\Lambda)]=1,\qquad [Q:L(\mu)]=2.
\tag{8.290}
\]
It is of finite length, since its two flag quotients are of lengths two and one.

Any projective object \(Q'\) with a nonzero simple quotient \(L(\mu)\) has an upper composition factor. Projectivity lifts its quotient map through the surjection \(\overline\nabla(\Lambda)\to L(\mu)\) in (8.284). The lifted map is surjective: its image maps onto the lower simple; if that image missed the upper socle, it would be a section of the nonsplit sequence, impossible. Hence \(Q'\) has both composition factors of that costandard, including \(L(\Lambda)\). A projective object with an upper simple quotient also has an upper composition factor, trivially.

If \(Q=Q_1\oplus Q_2\) with both summands nonzero, both summands are projective and have a simple quotient, because they have finite length. Every simple quotient is one of the two labels. The previous paragraph gives an upper composition factor in each summand, contradicting (8.290). Thus \(Q\) is indecomposable.

This argument uses neither BGG reciprocity over \(k_\alpha\), a deformed projective classification, nor an asserted equivalence of its block with \(\mathfrak{sl}_2\). It needs only actual projectivity in the residue category, proved in Section 8.15.6, and the ambient-root Verma/dual sequences proved here.

#### 8.14.11. Actual splitting at all height-one localizations

The Harish-Chandra character on \(M_A(\nu_w)\) evaluates invariant polynomials at \(wp+\tau\). Over the generic field these characters are distinct. At \(k_\alpha\), two are equal exactly for the pair \(\{w,s_\alpha w\}\).

Here are the polynomial details. Invariants of a finite group separate its orbits over any algebraically closed field of characteristic zero: choose a polynomial equal to zero on one finite orbit and one on the other using finite-point interpolation, then average. Averaging on each finite-dimensional polynomial degree piece also shows that invariant polynomials after field extension are scalar extensions of the original invariant polynomials. Thus equal invariant evaluations force
\[
g(wp+\tau)=vp+\tau
\tag{8.291}
\]
for some \(g\in W\), after an algebraic closure if needed. Since the group is finite, the same equality of vectors holds over the original rational field. In the generic field its tautological linear part forces \(g=1\), then \(v=w\). At the root-hyperplane field it forces \(g\) to fix the entire tangent hyperplane pointwise. A finite real orthogonal transformation with that property is the identity or its reflection \(s_\alpha\); the constant part then forces \(v=w\) or \(v=s_\alpha w\). Conversely \(s_\alpha\tau=\tau\) at that residue, proving those pairs have equal characters.

More generally, at a height-one prime \(\mathfrak q\subset A\), (8.291) requires each coordinate of \((g-1)\tau-(vp-gwp)\) to lie in \(\mathfrak q\). As \(\mathfrak q\subset\mathfrak m_0\), its constant part is zero, so \(vp=gwp\). Two independent nonzero linear coordinates cannot both belong to a height-one prime: their ideal has height two, as a linear change of variables exhibits. Hence a nonidentity \(g\) has \(\operatorname{rank}(g-1)=1\). It is an orthogonal reflection. Its fixed hyperplane must be a root hyperplane: otherwise it contains a point outside every root hyperplane, and \(g\) fixes that regular point and its unique open chamber, contradicting the Weyl group's free action on chambers. Thus \(g=s_\alpha\), and \(\mathfrak q=(h_\alpha)\) for a root \(\alpha\). Every other height-one localization has distinct characters. This proves the finite version of Fiebig's root-local splitting assertion at the actual polynomial parameter.

These character comparisons split actual finite Verma flags, not just their generic dimensions. Choose a central element whose residue scalars distinguish the finitely many pairs (or the singleton labels in the generic case); a linear combination of finitely many separating central elements does so, since only finitely many proper coefficient hyperplanes must be avoided in the infinite field \(\mathbb C\). On a flagged object the product of its central scalar factors annihilates the object: each successive factor kills its corresponding flag quotient, and the central factors commute. Products belonging to distinct groups of residue scalars are comaximal in \(T_\alpha[X]\), because every cross difference is a unit; their resultant is a unit, or direct polynomial division gives the same Bézout identity. Chinese remainders produce central polynomial idempotents. They split the actual object and its flag, yielding the stated two-Verma summands. On the generic field each component has just one Verma quotient and equals that Verma.

#### 8.14.12. First-order corner order and the exact scope

For a pair summand \(P\), a generic endomorphism is a pair of eigenvalues in \(K^2\): the two generic Verma modules are simple with distinct central characters, have zero inter-label Hom, and each has scalar endomorphisms by its highest line. Both eigenvalues lie in \(T_\alpha\). Indeed, at the lower highest weight both generic summands have nonzero weight spaces; the endomorphism acts there by a matrix over \(T_\alpha\), so both eigenvalues are integral over that ring. A valuation ring is integrally closed, as the least-valuation term in a monic equation rules out negative valuation. The map \(\operatorname{End}(P)\to K^2\) is injective because \(P\) is torsion free.

The central image is exactly \(\mathcal C_\alpha\) in (8.266), without a slice theorem. Invariant evaluation gives
\[
f(s_\alpha wp+\tau)=f(wp+s_\alpha\tau)
=f(wp+\tau-h_\alpha\alpha).
\]
Therefore every difference is divisible by \(h_\alpha\). Apply the completely proved free-orbit jet interpolation in Section 8.13.1, at the free orbit point \(wp\), prescribing a linear jet whose derivative on \(\alpha\) is one. The displayed difference divided by \(h_\alpha\) then has constant term one and is a unit in \(A\), hence in \(T_\alpha\). The associated central pair has difference \(h_\alpha u\) for a unit \(u\). Subtract its second coordinate times \((1,1)\), and multiply by \(u^{-1}\) in the scalar coefficient ring, to obtain \((h_\alpha,0)\). Together with the scalar identity, this spans \(\mathcal C_\alpha\). This proves both inclusion and first-order conductor with the exact normalization.

There are just two intermediate \(T_\alpha\)-modules between \(\mathcal C_\alpha\) and \(T_\alpha^2\). The quotient is the one-dimensional \(k_\alpha\)-space measured by the difference of coordinates. Its submodules are zero and itself. Thus the intermediate endomorphism order is either \(\mathcal C_\alpha\) or \(T_\alpha^2\). The latter contains the projector \((1,0)\). It would split the actual lattice \(P\) into its two nonzero generic components. In any weight where a component has positive generic rank, its weight space is a nonzero direct summand of a finite free \(T_\alpha\)-module. Such a summand is free over the local ring and its reduction is nonzero. The residue would therefore split into two nonzero summands, contradicting Section 8.14.10. Hence its order equals \(\mathcal C_\alpha\).

With \(e=(h_\alpha,0)\), the order has the literal basis \(1=(1,1),e\) and relation
\[
e^2=h_\alpha e.
\tag{8.292}
\]
This is the first-order relation required for the finite coinvariant corner. Multiplying \(h_\alpha\) by a nonzero root-length scalar gives Fiebig's \((\tau,\alpha)\) normalization and changes none of the order or indecomposability assertions.

It gives the actual projective-family extension maps as well. In the category of deformed weight modules whose weights are at or below \(\Lambda\), the upper Verma is projective: its Hom functor is the \(\Lambda\)-weight space, since that space is automatically killed by \(\mathfrak n^+\). Weight spaces are exact; distinct weight labels differ by nonzero complex Cartan scalars, so this assertion remains true over \(T_\alpha\). If the two-Verma flag of \(P\) placed the upper Verma in the quotient, that quotient's projectivity would split the flag. Its residue would split, contradicting Section 8.14.10. Hence its flag is necessarily the nonsplit sequence
\[
0\longrightarrow M_{T_\alpha}(\nu_w)
\xrightarrow{i}P\longrightarrow
M_{T_\alpha}(\nu_{s_\alpha w})\longrightarrow0.
\tag{8.293}
\]
The actual central endomorphism \(e=(h_\alpha,0)\) restricts to \(h_\alpha\) on its upper submodule and induces zero on its lower quotient. Its image therefore lies in that upper submodule. Factoring it through \(i\) defines an actual integral Lie-module map \(j:P\to M_{T_\alpha}(\nu_w)\), with
\[
ij=e,\qquad ji=h_\alpha\operatorname{id}.
\tag{8.294}
\]
Thus the nonsplit extension and its first-order wall parameter belong to the specified localized big-projective family itself. No identification of it with the optional Section 8.14.9 pullback lattice is needed.

### 8.15. The structure functor and the full multiplicity comparison

The proof expands the finite ordinary-category comparison of [Soergel, MPI/89-46, §§2.2–2.5](https://archive.mpim-bonn.mpg.de/id/eprint/3653/1/preprint_1989_46.pdf), with [Fiebig, arXiv:math/0305378v2, §§3–4](https://arxiv.org/html/math/0305378v2) as a deformation comparison. The ordinary full-faithfulness statement has projective target; the deformed all-Verma-flag statement is not specialized by assertion.

**Theorem 8.13 (regular integral category-O comparison and KL multiplicities).** Let $\mathfrak g$ be a finite-dimensional complex semisimple Lie algebra with positive-root Borel and let $\lambda$ be dominant integral. Put $M_w=M(w\cdot\lambda)$, $L_z=L(z\cdot\lambda)$ and $P=P(w_0\cdot\lambda)$. The central map $\phi_\lambda:z\mapsto[\gamma(z)(\lambda+\rho+h)]$ identifies $\operatorname{End}_{\mathcal O}P$ with the coinvariant ring $C$ and has kernel $\operatorname{Ann}_ZP$. The functor $V=\operatorname{Hom}_{\mathcal O}(P,-)$ is fully faithful with projective target. Wall translation acts by restriction and induction along $C^s\subset C$, and $VP_z\cong B_{z^{-1}}\otimes_R\mathbb C$ after forgetting grading. Consequently
\[
[M_w:L_z]=P_{w,z}(1)
\]
for all $w,z\in W$. This includes products and rank zero. The statement uses the KL normalization of Sections 8.1–8.4 and the dominant convention of Theorem 8.2.

**Proof.** The following subsections establish each comparison map and the final coefficient identity.

The field is \(\mathbb C\), the Lie algebra is finite-dimensional semisimple, the Borel is the positive-root Borel, and \(\lambda\) is dominant integral. Put
\[
 p=\lambda+\rho,\quad
 M_w=M(w\cdot\lambda),\quad L_w=L(w\cdot\lambda),\quad
 P_w=P(w\cdot\lambda),\quad P=P_{w_0},\quad E=\operatorname{End}_{\mathcal O}(P).
 \tag{8.295}
\]
The actual functor is \(V=\operatorname{Hom}_{\mathcal O}(P,-)\), valued in finite right \(E\)-modules by precomposition. The eventual coinvariant ring is commutative, but an opposite-ring convention must not be suppressed before that is established.


#### 8.15.1. Inputs, conventions and complex scalar extension

The following actual canonical results are used:

| Lesson | Exact result |
|---|---|
| RT-LIE-14 | Theorems 2.1 and 3.1: PBW Verma structure and unique simple head; Theorem 4.1, Lemmas 4.2–4.3, Proposition 5.1 and Exercise 7.2: finite highest-weight modules, Weyl-invariant extremal multiplicity one, and simple-root singular vectors |
| RT-LIE-15 | Proposition 1.1, Theorem 4.1 and Section 5: \(\chi_\nu(z)=\gamma(z)(\nu+\rho)\), central-character dot orbits; Theorem 9.1: polynomial Weyl invariants |
| RT-LIE-18 | Proposition 2.1 and Theorem 2.2: generalized block projections and finite length; Lemma 3.1 and Theorem 3.3: dominant Verma projectivity, projective covers and \(\dim\operatorname{Hom}(P_z,N)=[N:L_z]\); Lemma 4.1 and Theorem 4.4: tensor/Verma flags; Proposition 5.1: restricted duality; Theorem 6.1: BGG reciprocity |
| RT-LIE-08 | Longest-element/root signs, exchange and reduced words |

For bimodules use Section 8.7, in particular the support flags, Hom formula, classification and primitive inclusion proved there. Let
\[
 R=\operatorname{Sym}_{\mathbb C}(V^*),\quad \deg V^*=2,\quad
 M(n)^i=M^{i+n},\quad
 B_s=R\otimes_{R^s}R(1).
 \tag{8.296}
\]
A fixed \(W\)-equivariant Killing-form identification identifies its reflection coordinate with \(\mathfrak h^*\). Thus this polynomial ring also serves as \(S=\operatorname{Sym}(\mathfrak h)\), the polynomial functions on \(\mathfrak h^*\). For the graph module \(R_x\), left \(f\) acts as \(f(x\xi)\). Right wall translation on a Verma label \(w\) consequently corresponds to left tensoring on the inverse graph label \(w^{-1}\).

Section 8.13 gives the surjection
\[
 \phi_\lambda:Z(U\mathfrak g)\twoheadrightarrow
 C=S/(S^W_{>0}S),\qquad
 z\longmapsto[\gamma(z)(p+h)].
 \tag{8.297}
\]
That surjection alone neither proves the annihilator nor identifies \(E\).

Section 8.7 is written over \(\mathbb R\); its use over \(\mathbb C\) here has an explicit justification. Extend the actual Cartan reflection representation and every polynomial graph module by scalars. All finite support-kernel equations, graph Ext computations, split right-module flags, Hom formulas and Frobenius adjunction maps commute with this flat scalar extension. This follows from finite presentations and flat field extension, or directly by tensoring their displayed finite polynomial matrices. For a real normalized \(B_x\), Section 8.7.17 and equation (8.129) identify its degree-zero endomorphism algebra modulo its nilpotent radical with \(\mathbb R\). Tensoring with \(\mathbb C\) gives a nilpotent ideal and quotient \(\mathbb C\), hence again a local degree-zero algebra. Thus each complexified \(B_x\) remains indecomposable. A whole real word's finite indecomposable decomposition complexifies to these indecomposables; Krull–Schmidt then proves that no additional complex indecomposable labels appear in any summand of a word. The normalized classification and self-duality hold over (8.295)'s field. Each support layer keeps exactly the same integral graded rank, so the integral Hecke character is unchanged. The real character theorem, Theorem 8.10, therefore transfers \(h(B_x)=C'_x\) to this normalized complex \(B_x\). This extends the actual character conclusion, without asserting complex definiteness for a real positivity form.

#### 8.15.2. Construct the big projective without KL or localization

**Lemma 8.20 (simple-root integrability).** The simple \(L_w\), for \(w\ne w_0\), is integrable for at least one simple-root \(\mathfrak{sl}_2\). Every Verma module, and every Verma-flag object, has injective action by each negative simple-root vector \(f_i\).

**Proof.** A nonlongest element has a left ascent \(s_iw>w\). Then \(w^{-1}\alpha_i\) is positive and \(w p(\alpha_i^\vee)\) is a positive integer. Write \(w\cdot\lambda(h_i)=m\ge0\). The simple-root singular vector \(f_i^{m+1}v\) generates a proper submodule of the Verma, so it is zero in the simple head. Local nilpotence of \(\operatorname{ad}f_i\) on \(U(\mathfrak g)\), together with its local nilpotence on the highest vector, makes \(f_i\) locally nilpotent on the entire simple: expand \(f_i^Nuv\) by the commutator binomial formula. Raising operators are locally nilpotent in \(\mathcal O\). The elementary \(\mathfrak{sl}_2\) argument therefore gives the stated integrability.

On \(M(\nu)=U(\mathfrak n^-)v_\nu\), \(f_i\) acts by left multiplication. The PBW leading-symbol algebra is a polynomial domain, hence \(U(\mathfrak n^-)\) is a domain, so that action is injective. In an extension, injectivity on the subobject and quotient implies injectivity on the middle object: first project a killed vector to the quotient, then use the subobject. Induct along a Verma flag. \(\square\)

Every nonzero subobject of a Verma-flag object has a simple subobject, by finite length. Lemma 8.20 rules out every simple label except \(w_0\). Consequently all its simple subobjects are \(L_{w_0}\).

Put \(\nu=-\rho\). Its dot orbit is a singleton, so \(M(\nu)\) is simple: a proper highest-weight subquotient would have the same central character but a strictly lower weight, contrary to the singleton orbit. It is projective by Lesson18 Lemma 3.1 and is self-dual because it is simple. Thus it is also injective.

Let \(F=L(p)\), a finite-dimensional simple, and set
\[
 Q=\operatorname{pr}_{\chi_\lambda}(F\otimes M(-\rho)).
 \tag{8.298}
\]
The tensor identity and a Borel flag in \(F\) give Verma factors \(M(\eta-\rho)\), with \(\eta\) running through the weights of \(F\). Harish-Chandra says a factor belongs to \(\chi_\lambda\) precisely when \(\eta\in Wp\). Every such extremal weight occurs once. Therefore \(Q\) is projective and has exactly one factor \(M_w\) for every \(w\in W\).

For \(z\ne w_0\), tensor adjunction identifies
\[
 \operatorname{Hom}(Q,L_z)
 \subset \operatorname{Hom}(M(-\rho),F^*\otimes L_z).
 \tag{8.299}
\]
The target is integrable for the simple-root \(\mathfrak{sl}_2\) from Lemma 8.20. A highest vector of weight \(-\rho\) would have \(h_i\)-weight \(-1\), impossible in an integrable \(\mathfrak{sl}_2\)-module. Indeed \(e f^n v=n(-1-n+1)f^{n-1}v=-n^2f^{n-1}v\); a first vanishing power of \(f\) gives a contradiction. Thus (8.299) is zero.

For \(z=w_0\), \(L_{w_0}=M_{w_0}\), by minimality of its weight in the finite orbit and Harish-Chandra. The \(\chi_{-\rho}\) component of \(F^*\otimes M_{w_0}\) has one Verma factor \(M(-\rho)\): it comes from the unique extremal weight \(-w_0p\) in \(F^*\). All other tensor-flag weights have another central character. Hence
\[
 \dim\operatorname{Hom}(Q,L_{w_0})=1.
 \tag{8.300}
\]
The projective-cover decomposition of Q therefore has exactly one summand and that summand is \(P_{w_0}\). This proves the actual isomorphism
\[
 P=\operatorname{pr}_{\chi_\lambda}(L(p)\otimes M(-\rho)),
 \qquad (P:M_w)=1.
 \tag{8.301}
\]
Restricted duality fixes every finite simple and commutes with finite tensoring and block projection. It fixes \(M(-\rho)\). Thus \(DP\cong P\); projectivity makes \(P\) injective. It is the injective hull of \(L_{w_0}\), so its socle is one copy of that simple.

BGG reciprocity now gives, without a KL polynomial,
\[
 [M_w:L_{w_0}]=1,\qquad
 \dim E=[P:L_{w_0}]=|W|.
 \tag{8.302}
\]
This proves the big-projective multiplicities used in the original deformation argument instead of importing them.

#### 8.15.3. The actual corner functor and its quotient mechanism

All objects in this section are ordinary finite-length objects. Since \(P\) is projective, \(V\) is exact and
\[
 \dim VN=[N:L_{w_0}].
 \tag{8.303}
\]
Let \(\mathcal K=\{N:VN=0\}\). It is the Serre subcategory of objects with no \(L_{w_0}\) factor. No nonzero map from an object of \(\mathcal K\) to \(P\) exists: its image, being a nonzero subobject of the injective hull \(P\), would contain the socle \(L_{w_0}\).

For a finite right \(E\)-module \(N\), define
\[
 L(N)=N\otimes_E P,\qquad
 \epsilon_M:VM\otimes_E P\to M,\quad f\otimes v\mapsto f(v).
 \tag{8.304}
\]
The tensor is in \(\mathcal O\), since a finite presentation of \(N\) presents it as a quotient of a finite sum of \(P\)'s. Tensor–Hom adjunction gives \(L\dashv V\). The unit \(N\to VL(N)\) is an isomorphism on finite free modules. Both sides are right exact, so a finite presentation proves it for every \(N\). Applying exact \(V\) to the counit shows its kernel and cokernel belong to \(\mathcal K\).

Injectivity of \(P\), and the vanishing of maps from those two kernel objects to \(P\), now give
\[
 \operatorname{Hom}_{\mathcal O}(M,P)
 \xrightarrow{\sim}
 \operatorname{Hom}_{E}(VM,E).
 \tag{8.305}
\]
To see the surjectivity explicitly, factor \(\epsilon_M\) through its image. A map from its source to \(P\) kills its \(\mathcal K\)-kernel, so descends to the image; it extends from that image to \(M\) by injectivity. Uniqueness follows because the cokernel has no map to \(P\). This proves (8.305) before any coinvariant identification.

The ring \(E\) is local by the finite-dimensional endomorphism argument for indecomposable \(P\); its residue is \(\mathbb C\), by its one-dimensional simple head. Write \(J=\operatorname{rad}E\). Apply (8.305) to \(L_{w_0}\). Its \(V\)-image is the residue right module, while its Hom into \(P\) has dimension one. Hence the right socle of \(E\) has dimension one. Duality \(DP\cong P\) gives an anti-automorphism of \(E\) preserving \(J\), so its left socle also has dimension one.

This also proves \(E\) is a Frobenius algebra, independently of flag-variety cohomology. Choose a linear functional \(\omega:E\to\mathbb C\) nonzero on its right socle. Every nonzero right ideal contains that socle: multiply a nonzero element by powers of the nilpotent radical until a nonzero minimal right ideal is reached. Thus for every \(a\ne0\) some \(b\) has \(\omega(ab)\ne0\). The square bilinear pairing \((a,b)\mapsto\omega(ab)\) is nondegenerate in one variable and therefore in both.

The unique top Verma \(M_e=M(\lambda)\) embeds in \(P\), with Verma-flag quotient. This follows from the actual construction (8.301), rather than from character equality. Choose the Borel flag of \(L(p)\) with higher weights preceding lower weights. Its first line is the highest line of weight p. Exact induction gives the first submodule \(M(p-\rho)=M(\lambda)\) of \(L(p)\otimes M(-\rho)\). This line survives the selected block projection. Every subsequent surviving quotient is a Verma, so the quotient by that first submodule is Verma filtered. Its highest-weight space is one dimensional by the same flag.

Every endomorphism of \(P\) preserves this top Verma and acts on its highest line by its residue scalar. Thus \(J M_e=0\). Conversely let \(K=\{v\in P:Jv=0\}\). Then \(VK\) is the left socle of \(E\), of dimension one. If \(K/M_e\ne0\), it is a subobject of the Verma-flag object \(P/M_e\); Lemma 8.20 supplies an \(L_{w_0}\) factor. Exact (8.303) would give \(\dim VK\ge2\), a contradiction. Therefore
\[
 K=M_e,\qquad VM_e=\{a\in E:Ja=0\}.
 \tag{8.306}
\]
Taking the maps in (8.305) with image annihilated by \(J\) proves
\[
 \operatorname{Hom}_{\mathcal O}(M,M_e)
 \xrightarrow{\sim}\operatorname{Hom}_{E}(VM,VM_e).
 \tag{8.307}
\]

#### 8.15.4. Full faithfulness with projective target

The final step uses the projective generation proved in Section 8.12.8: every regular projective is a summand of a finite sum of \(F M_e\), for projective functors \(F\) made from finite tensoring, block projections and their summands, or equivalently from the wall crossings in Section 8.12. The functors and their adjoints are exact.

Here is the remaining argument, not an invocation of a Struktursatz. An indecomposable projective-injective in this block is \(P\). Its injective socle is one simple label, whereas its Verma flag and Lemma 8.20 force that label to be \(w_0\). Therefore any finite tensor/projection functor sends \(P\) to a sum of copies of \(P\): the image is projective and self-dual, hence injective. A summand retains both properties. The same holds for the adjoint.

If \(G\dashv F\) is such an adjoint pair, then for \(M\in\mathcal K\),
\[
 VFM=\operatorname{Hom}(P,FM)
 \cong\operatorname{Hom}(GP,M)=0.
 \tag{8.308}
\]
Thus both functors preserve \(\mathcal K\).

For completeness the quotient step can be carried out entirely within these finite categories. In \(\mathcal O/\mathcal K\), the counit (8.304) is invertible; \(V\) and \(L\) therefore induce inverse equivalences with right \(E\)-modules. A quotient morphism is represented by a map from a subobject of the source with \(\mathcal K\)-quotient to a quotient of the target with \(\mathcal K\)-kernel. Exact functors preserving \(\mathcal K\) act on these representatives. The adjunction unit and counit act on the same representatives and retain their triangle identities, so \(G\dashv F\) descends to \(\bar G\dashv\bar F\). This proves the descended adjunction, rather than assuming it.

Using (8.307) and both adjunctions gives
\[
 \begin{aligned}
 \operatorname{Hom}_{\mathcal O}(M,FM_e)
 &\cong\operatorname{Hom}_{\mathcal O}(GM,M_e)\\
 &\cong\operatorname{Hom}_{E}(VGM,VM_e)\\
 &\cong\operatorname{Hom}_{E}(VM,VFM_e).
 \end{aligned}
 \tag{8.309}
\]
Each isomorphism is the natural structure-functor map under the displayed adjunctions. Finite sums and target idempotents give
\[
 \operatorname{Hom}_{\mathcal O}(M,Q)
 \xrightarrow{\sim}\operatorname{Hom}_{E}(VM,VQ)
 \quad\text{for every projective }Q.
 \tag{8.310}
\]
Thus ordinary full faithfulness on projectives needs no geometric equivalence and no deformed all-Verma-flag specialization. Its dependence on Section 8.12.8 remains explicit.

#### 8.15.5. Coinvariant freeness and the invariant evaluation order

This section is algebraic and independent of the root nonsplitting obligation.

Write the homogeneous polynomial invariants, from Lesson15 Theorem 9.1, as \(q_1,\ldots,q_r\), of ordinary polynomial degrees \(d_i\). Use ordinary degree one temporarily; bimodule degree is twice this degree. The quotient \(C=S/(q_1,\ldots,q_r)\) is finite by Section 8.13.3.

The Koszul complex \(K(q;S)\) has no positive homology. Here is a finite proof of the required parameter fact. Every homology group is killed by all \(q_i\) and is finite over \(S\), hence finite dimensional. The positive-degree ideal of the finite graded quotient C is nilpotent, so every \(x_i\) acts nilpotently on these modules. Any nonzero such module has a nonzero common \(x\)-socle: choose the largest nonzero power of that nilpotent ideal acting on it. Consider the double complex \(K(x;S)\otimes K(q;S)\), where \(x_1,\ldots,x_r\) are linear coordinates. Taking \(x\)-homology first gives \(K(q;\mathbb C)\), which has zero differential and total homology only in degrees \(0,\ldots,r\). If \(j>0\) is the largest nonzero \(q\)-homology degree, taking \(q\)-homology first gives a nonzero entry in bidegree \((r,j)\): the top \(x\)-Koszul homology is that common socle. It survives every differential. An incoming differential would have first index greater than \(r\); an outgoing differential would have second index greater than \(j\). It would yield total homology in degree \(r+j>r\), a contradiction. The Koszul complex on the independent coordinates \(x\) is exact in positive degree by its elementary one-variable tensor construction. This proves the parameter assertion.

The resulting Hilbert series is
\[
 \operatorname{Hilb}C(t)=\prod_i\frac{1-t^{d_i}}{1-t}
 =\prod_i(1+t+\cdots+t^{d_i-1}).
 \tag{8.311}
\]
Choose homogeneous lifts \(b_1,\ldots,b_m\) of a graded basis of \(C\). The map \(S^W\otimes\operatorname{span}\{b_j\}\to S\) is onto by degree induction: reduce a polynomial modulo \((q_i)\), then apply the induction to the smaller-degree coefficients of the \(q_i\)'s. Its Hilbert series agrees with that of \(S\), by (8.311) and \(\operatorname{Hilb}S^W=\prod(1-t^{d_i})^{-1}\). Every degree is finite, so it is an isomorphism. Thus \(S\) is free over \(S^W\).

Molien's identity follows by averaging the trace of \(w\) on symmetric powers:
\[
 \operatorname{Hilb}S^W(t)=\frac1{|W|}
 \sum_{w\in W}\frac1{\det(1-tw)}.
 \tag{8.312}
\]
Compare the two leading Laurent terms at \(t=1\). The identity contributes the pole of order \(r\); exactly the reflections contribute to order \(r-1\), with eigenvalues \(1,\ldots,1,-1\). Reflection faithfulness excludes other contributions of that order. Hence
\[
 \prod d_i=|W|,\qquad
 \sum_i(d_i-1)=|\Phi^+|=:N.
 \tag{8.313}
\]
Palindromicity of (8.311) gives \(\sum_j\deg b_j=N|W|/2\). These assertions also hold for products; rank zero is immediate.

Let \(A=S_{(x_1,\ldots,x_r)}\), with tautological coordinate \(\tau\), and \(K=\operatorname{Frac}A\). Put
\[
 H=S\otimes_{S^W}A,\qquad
 \operatorname{ev}:H\to A^W,\quad
 f\otimes a\mapsto(f(w^{-1}\tau)a)_w.
 \tag{8.314}
\]
Its generic version is an isomorphism with \(K^W\): the \(|W|\) generic orbit points are distinct, polynomial Chinese remainders give every evaluation tuple over \(K\), and the source rank is \(|W|\). Thus its determinant in the basis \(b_j\) is nonzero.

For a positive root \(\alpha\), pair rows \(w,s_\alpha w\). Their difference is divisible by \(h_\alpha=\tau(\alpha^\vee)\). Subtract one row in each of the \(|W|/2\) pairs; the determinant is divisible by \(h_\alpha^{|W|/2}\). Its degree is \(N|W|/2\), by (8.313). Distinct positive roots give nonassociate linear factors, so
\[
 \det(b_j(w^{-1}\tau))=c\prod_{\alpha>0}h_\alpha^{|W|/2},
 \quad c\ne0.
 \tag{8.315}
\]
At the height-one localization \(T=A_{(h_\alpha)}\), the order H is exactly
\[
 \{(a_w)\in T^W:a_w\equiv a_{s_\alpha w}\pmod {h_\alpha}\}.
 \tag{8.316}
\]
Indeed the containment follows from evaluation. The larger displayed lattice has index length \(|W|/2\) in \(T^W\), one independent residue condition per pair; (8.315) gives the same length for H. Over the DVR equality follows. At every other height-one prime the evaluation determinant is a unit, so H is \(T^W\).

A free \(A\)-module is the intersection of its height-one localizations inside its fraction space: expand in a free basis and use unique factorization to detect any denominator. Therefore
\[
 H=\{(a_w)\in A^W:a_w\equiv a_{s_\alpha w}\pmod {h_\alpha}
 \text{ for every }\alpha,w\}.
 \tag{8.317}
\]
This proves the finite invariant evaluation order directly, including all ambient roots.

#### 8.15.6. Coherent big-projective deformation and all-root local completion

Define \(M_A(\eta)\) by highest weight \(\eta+\tau\). In this section deformed objects have finite Verma flags; every weight space is finite free over \(A\). Tensoring by a finite module has the same actual Borel flag as in Lesson18, with deformed Verma factors.

The block projection needed here is algebraic. For a deformed Verma factor define its central evaluation ideal
\[
 I_\eta=(z-\gamma(z)(\eta+\rho+\tau):z\in Z)\subset Z\otimes A.
 \tag{8.318}
\]
If two factors have distinct special central characters, some difference of evaluations is a unit of \(A\). Their ideals, and sufficiently high powers, are comaximal. A flagged object is killed by the product of its evaluation ideals, by induction on the flag. Finite Chinese remainders therefore split it into the specified special-character components. The resulting idempotents are natural and exact on flagged sequences; the same unit remains a unit after base change. This proves the needed projection and its base-change compatibility, without deforming arbitrary objects by assertion.

Set
\[
 P_A=\operatorname{pr}_{\chi_\lambda}(L(p)\otimes M_A(-\rho)).
 \tag{8.319}
\]
Its flags contain \(M_A(w\cdot\lambda)\), once for every \(w\), exactly as in Section 8.15.2. For a flagged \(N\) in this block, tensor adjunction identifies \(\operatorname{Hom}(P_A,N)\) with the \(-\rho\) deformed-weight space of the \(\chi_{-\rho}\) component of \(F^*\otimes N\). In that component the only possible Verma label is \(-\rho\), since its special dot orbit is a singleton. There are no weights above \(-\rho\), so taking that weight space imposes no additional highest-vector equations. It is a finite free \(A\)-module, is exact on flagged sequences, and commutes with base change. Consequently
\[
 E_A=\operatorname{End}(P_A)\text{ is }A\text{-free},\quad
 E_A/\mathfrak mE_A\cong E,\quad \operatorname{rank}_A E_A=|W|.
 \tag{8.320}
\]
This only proves the coherent Hom fact for the big projective needed here. It does not pretend to prove Soergel's general universal tensor-Verma Hom proposition by importing Kostant's separation or the Verma annihilator theorem.

The residue projectivity needed by Proposition 8.8 requires more than the flag Hom calculation. It is also available directly. Fix a positive root \(\alpha\), let \(k_\alpha=\operatorname{Frac}(S/(h_\alpha))\), and write \(\bar\tau\) for its generic Cartan coordinate. Consider actual category-O modules over this characteristic-zero field in the integral weight coset: their weights have the form \(\xi+\bar\tau\), with fixed integral \(\xi\), and their support is bounded above in finitely many root cones. The elementary finite-generation, weight-space, highest-vector and central-projection arguments of Lessons14–18 apply over this field. In particular a nonzero subquotient has a highest vector. No algebraic closure is needed for central projection: highest-weight central characters are values in \(k_\alpha\), and the finite central image decomposes by polynomial Chinese remainders just as in Section 8.12.1. Equivalently one can extend to an algebraic closure and descend the same rational spectral idempotents.

In the central component of \(F^*\otimes N\) with character \(\chi_{-\rho+\bar\tau}\), any possible highest weight \(\xi+\bar\tau\) must have the same Casimir scalar. Thus
\[
 (\xi+\rho,\xi+\rho)+2(\xi+\rho,\bar\tau)=0.
 \tag{8.321}
\]
This is a polynomial identity on the generic hyperplane \(\alpha^\perp\). Its linear term says \(\xi+\rho=c\alpha\); its constant term and positive definite real root form say c=0. This uses that \(\xi+\rho\) is in the real integral weight span. Hence the only possible highest label is \(-\rho+\bar\tau\). Any weight strictly above this label would lie below a maximal weight of the submodule it generates, yielding a forbidden highest label. There are therefore no weights above it. The most-singular Hom functor is exactly its top weight space, which is exact on all short exact sequences of these weight modules. Tensor/block adjunction proves
\[
 P_{k_\alpha}\text{ is projective in the actual residue category O.}
 \tag{8.322}
\]
To identify the projective just proved with the actual residue family, the central polynomial idempotent in (8.319) also specializes to a central idempotent on \(F\otimes M_{k_\alpha}(-\rho)\): every separating evaluation difference that was a unit of A remains a unit in its localization and residue. Thus \(P_{k_\alpha}\) is an actual central direct summand of finite tensoring of the most-singular projective. Both finite tensor adjoints are exact over this field, so tensoring preserves projectivity, and so does that summand. The same coherent Hom calculation gives base change from A to its height-one localization and then to \(k_\alpha\). Over the DVR, exactness on Verma-flag sequences was proved above. Section 8.14.10’s projective-summand argument only requires actual residue projectivity (8.322), not an unproved projectivity assertion for arbitrary torsion DVR objects. This supplies the residue projectivity required in Section 8.14.10.

Over \(K\), the Verma factors have pairwise distinct central characters. Otherwise equality would give an equation \((u-1)\tau=\text{constant}\), forcing \(u=1\) and the two labels equal. Central projections split \(P_K\) into those Vermas. Each has scalar endomorphisms, determined by its highest line, so \(E_A\otimes K=K^W\). Every scalar coordinate of an element of \(E_A\) is integral over \(A\): choose finitely many weight spaces containing generating vectors and embed its action in their finite free matrix algebra. Its characteristic polynomial is monic. Since \(A\) is a localization of a polynomial UFD, it is integrally closed; hence
\[
 E_A\subset A^W.
 \tag{8.323}
\]
In particular \(E_A\) and its special fiber E are commutative.

Here is an exact way to place H inside \(E_A\) without a slice theorem or a formal-coordinate assumption. Section 8.13.1 at order one supplies central \(z_i\) with
\[
 f_i(t):=\gamma(z_i)(p+t)=t_i+O(t^2).
 \tag{8.324}
\]
The central elements \(b_j(z_1,\ldots,z_r)\) have generic evaluation columns \(b_j(f_1(w^{-1}\tau),\ldots,f_r(w^{-1}\tau))\). These columns satisfy every congruence in (8.317). Their determinant is divisible by the right side of (8.315) and has the same lowest homogeneous term as (8.315), because the \(b_j\)'s are homogeneous and the \(f_i\)'s have linear term \(t_i\). The quotient determinant has nonzero constant term, hence is a unit of A. Relative to the H basis the determinant is therefore a unit. The central columns span exactly H. Thus
\[
 H\subset E_A\subset A^W.
 \tag{8.325}
\]
Specializing supplies a map \(C=H/\mathfrak mH\to E\). A central z acts through the class \(f_z(h)=\gamma(z)(p+h)\), by its actual generic evaluations. Hence \(\ker\phi_\lambda\) **does annihilate P**. Surjectivity/injectivity of this new map C to E has not followed merely from equal dimensions.

The precise representation-theoretic local input at this point is:

**Ambient-root nonsplitting.** For every positive root \(\alpha\), take \(T=A_{(h_\alpha)}\). The generic-residue central decomposition of \(P_A\otimes T\) has one object on each pair \(\{w,s_\alpha w\}\), with the two corresponding Verma factors once. Its reduction modulo \(h_\alpha\) is indecomposable for every pair.

This concerns all ambient positive-root hyperplanes and generic values of the other Cartan parameters. Section 8.14 supplies its full proof.
Its contract uses precisely (8.318)–(8.322), not an unproved global deformed projectivity theorem.

The proof link is explicit. Section 8.14.2 constructs the contravariant PBW form and identifies its radical with the maximal proper submodule. Section 8.14.3 computes its nonzero leading determinant and rootwise total exponents. Section 8.14.4 uses the actual Casimir to force every irreducible determinant factor to be a positive-root integer hyperplane. At any factor's generic point, Section 8.14.5 shows that the only possible singular weight is the reflected lower weight and that its simple Verma radical is unique, using PBW growth to intersect any two such copies. Section 8.14.6's first transverse pairing is perfect: a degenerate top pairing would lift a singular vector modulo the square of the wall parameter, contradicting the first-order Casimir scalar difference. Its valuation is therefore the radical dimension. Section 8.14.7 compares the total leading exponents and forces every positive-root factor with its full partition exponent. Thus Section 8.14.8 gives, at every ambient root and for the oriented pair with upper weight \(\Lambda\) and lower weight \(\mu\), the actual nonsplit dual sequence
\[
 0\longrightarrow L(\Lambda)\longrightarrow\nabla(\Lambda)
 \longrightarrow L(\mu)\longrightarrow0,
 \qquad M(\mu)=L(\mu).
 \tag{8.326}
\]
The residue pair object's two Verma factors give exactly one upper simple and two lower simples. By (8.322) it is projective. Every nonzero projective summand has a simple quotient. If that quotient is lower, projectivity lifts its map to the nonsplit costandard (8.326); the lift is onto, since a proper image mapping onto the lower simple would split that sequence. Hence that summand contains an upper simple. A summand with an upper quotient already does. Two nonzero summands would require two upper composition factors, whereas the pair object has only one. This is Section 8.14.10's proof of Proposition 8.8, now with its actual projectivity supplied. Section 8.14.11 supplies the central pair decomposition used here; Section 8.14.12 also verifies the first-order conductor from Section 8.13. No rank-one equivalence, Jantzen sum formula or imported projective classification is used to close Proposition 8.8.

**Completion of the corner proof.** At T the special central characters split the different pairs, by the same Chinese-remainder argument. On a pair, H is the first-order order
\[
 H_{\rm pair}=\{(a,b)\in T^2:a\equiv b\bmod h_\alpha\}.
 \tag{8.327}
\]
The quotient \(T^2/H_{\rm pair}\) is one dimensional over the residue field. Therefore an intermediate endomorphism order is either \(H_{\rm pair}\) or \(T^2\). In the second case its two idempotents split the pair object and its residue, contrary to Proposition 8.8. Thus \(E_A\otimes T=H\otimes T\). At other primes (8.315) already makes H equal to \(T^W\). Both H and \(E_A\) are free and are their height-one intersections, so \(E_A=H\). Specialization gives
\[
 C\xrightarrow{\sim}E,\qquad
 \operatorname{Ann}_Z P=\ker\phi_\lambda.
 \tag{8.328}
\]
This expands the original codimension-one argument, including why determinant ranks alone do not prove it and exactly where nonsplitting is used.

#### 8.15.7. Wall translation compatibility, with the central action proved

Section 8.12’s finite norm selection, actual Borel flags, biadjunctions, most-singular construction, big-projective wall effects and dominant-start generation supply the translation properties used here. In particular Theorem 8.12 proves \(T_{\rm out}P_{\mu,-}\cong P\), while (8.246) gives each singular Verma once and (8.247) gives \(\dim\operatorname{End}P_{\mu,-}=|W|/2\). No corner multiplication or central action was imported from that provider.

Here the central-action clause is derived from the proved regular corner (8.328). Fix its simple wall \(\mu\) with stabilizer \(W_s=\{1,s\}\), and put \(b=\mu+\rho\). Form
\[
 P_{\mu,A}=\operatorname{pr}_{\chi_\mu}
       (L(b)\otimes M_A(-\rho)),\qquad
 E_{\mu,A}=\operatorname{End}P_{\mu,A}.
 \tag{8.329}
\]
The same actual tensor flag gives exactly the Verma factors \(M_A(w\cdot\mu)\), indexed by \(W/W_s\), once. Tensor adjunction to the most-singular top weight space proves that \(E_{\mu,A}\) is free of rank \(|W|/2\) and commutes with specialization. This repeats the Section 8.15.6 proof with repeated labels removed; it uses no singular corner theorem.

Use the finite module and tensor/project construction from Section 8.12.4 to define deformed translation out on flagged objects, with projection given by (8.318). Its Verma factors are exactly those selected by the ordinary special characters in (8.238); all nonselected ideals differ by units of A. Consequently
\[
 U_A:=T_{\rm out,A}P_{\mu,A}
 \quad\text{has each regular Verma factor once, and}\quad
 U_A/\mathfrak mU_A\cong P.
 \tag{8.330}
\]
There is an actual isomorphism \(U_A\cong P_A\). The coherent Hom calculation for \(P_A\) and the flagged target \(U_A\) commutes with specialization, so it lifts the ordinary isomorphism \(P\cong U_A/\mathfrak m U_A\) to a map \(P_A\to U_A\). Every weight space of source and target is finite free of the same rank, by their identical Verma flags. The determinant of each weight-space map reduces to a nonzero determinant and is therefore a unit of the local ring A. The map is an isomorphism on every weight space, hence on the modules. The isomorphism can be chosen to lift the fixed ordinary translation isomorphism.

Translation of endomorphisms now gives \(E_{\mu,A}\to E_A\). Over K its source is \(K^{W/W_s}\). Translation out of the component labelled \(wW_s\) consists of the two regular Verma components labelled w and ws. A scalar on the source becomes the same scalar on both of these components. Thus its image in \(K^W\) is fixed by the **right-label** permutation \(w\mapsto ws\).

Under \(E_A=H=S\otimes_{S^W}A\), that permutation is s acting on the first S factor: evaluation of \((sf)(\xi)=f(s\xi)\) at \(w^{-1}\tau\) is evaluation of f at \((ws)^{-1}\tau\). It preserves H. Taking fixed vectors commutes with every base change because the Reynolds idempotent \((1+s)/2\) splits its inclusion. Thus
\[
 H^s=S^s\otimes_{S^W}A,\qquad
 (H^s)/\mathfrak mH^s=C^s,
 \qquad E_{\mu,A}\longrightarrow H^s\subset H.
 \tag{8.331}
\]
Specialization gives \(\operatorname{End}P_{\mu,-}\to C^s\subset C\). This map is injective. If a nonzero endomorphism f had zero translation, its nonzero image is a subobject of the injective hull \(P_{\mu,-}\), so it contains its anti-dominant socle. Hence \(V_\mu(\operatorname{im}f)\ne0\). (8.252) and exactness give \(V T_{\rm out}(\operatorname{im}f)\cong V_\mu(\operatorname{im}f)^{\oplus2}\ne0\), a contradiction. Since \(\dim\operatorname{End}P_{\mu,-}=|W|/2\) and \(\dim C^s=|W|/2\), the map is an isomorphism onto \(C^s\). The latter dimension follows by reducing the split rank-two extension \(S^s\subset S\), or directly by the Frobenius basis in (8.335).

We have therefore proved the full action clause, rather than assuming it from ordinary scalar central characters:
\[
 E_\mu=C^s,\quad T_{\rm out}P_{\mu,-}\cong P,\quad
 E_\mu\to E\text{ induced by translation is }C^s\hookrightarrow C.
 \tag{8.332}
\]
The argument used a lift of the actual projective translation and its generic paired evaluations. It avoided both a singular invariant slice theorem and an imported all-object central-translation theorem.

Changing the chosen isomorphism \(T_{\rm out}P_{\mu,-}\cong P\) conjugates the induced endomorphism map by a unit of E. Since E is now proved commutative, this conjugation is the identity. Thus the inclusion in (8.332) is independent of this choice.

Adjunction gives, naturally and with the \(C^s\)-action fixed by (8.332),
\[
 V_\mu T_{\rm on}M
 =\operatorname{Hom}(P_{\mu,-},T_{\rm on}M)
 \cong\operatorname{Hom}(T_{\rm out}P_{\mu,-},M)
 =\operatorname{Res}_{C^s}VM.
 \tag{8.333}
\]
(8.252) proves preservation of the two kernel subcategories. Both adjunctions descend by the explicit quotient argument of Section 8.15.4. Thus the adjoint of restriction is induction and
\[
 V T_{\rm out}N\cong C\otimes_{C^s}V_\mu N,
 \qquad V\theta_sM\cong C\otimes_{C^s}VM.
 \tag{8.334}
\]
These are ungraded formulas. The graded bimodule lift has the shift +1 from (8.296). No Tate twist or geometric equivalence is inserted. Since C is commutative, right corner modules are identified with left C-modules when using this tensor formula; this is the harmless convention change after (8.328), not an opposite-ring assumption made before it.

#### 8.15.8. Augmentation Hom comparison proved from the earlier actual support package

This section uses the coinvariant corner (8.328), the translation properties of Section 8.12, and their ring-linear action proved in Section 8.15.7.

For \(B\in\mathcal B\), write \(D(B)=B\otimes_R\mathbb C\), with right augmentation. Its left action factors through C: any \(W\)-invariant polynomial can be moved through every tensor factor of a Bott–Samelson object, since it is invariant under every simple reflection. Positive-degree invariants therefore act by zero after augmentation. The same holds for summands.

The extension \(C^s\subset C\) has the same rank-two Frobenius basis \(1,\alpha_s/2\) as \(R^s\subset R\). Indeed the ideal \(S^W_{>0}R\) is generated by s-invariants; reducing \(R=R^s\oplus R^s(-2)\) gives
\[
 C=C^s\oplus C^s(-2),
 \tag{8.335}
\]
where the invariant identification follows by averaging. The trace \(\partial_s\) descends and remains perfect in that basis. Thus the functor \(C\otimes_{C^s}-(1)\) is self-adjoint, with its adjunction exactly the reduction of the bimodule Frobenius adjunction.

There is a natural comparison
\[
 \beta_{B,B'}:
 \operatorname{Hom}_{R-R}(B,B')\otimes_R\mathbb C
 \longrightarrow\operatorname{Hom}_{C}(D(B),D(B')).
 \tag{8.336}
\]
It is injective for source \(B=R\). The bimodule Hom is the identity-graph submodule \(\Gamma_e B'\), and Section 8.7.11/(8.111) says its inclusion in \(B'\) is a split inclusion of right R-modules. Its augmentation is therefore injective. Its image is annihilated by the left positive-degree coordinates, as a map from the trivial module must be. This proves injection, not yet surjectivity.

Induct on the length of a Bott–Samelson source. Move its first \(B_s\) to the target by Frobenius adjunction. On the C side move \(C\otimes_{C^s}-(1)\) in exactly the same way. The comparison square commutes because both adjunctions use the same trace and basis. The target remains a Bott–Samelson sum; the base injection therefore proves (8.336) is injective for every word source. Sums, shifts and split idempotents give injection for arbitrary regular Soergel summands.

For whole words, the two dimensions agree. The regular Hom formula Section 8.7.15, specialized on the right at \(v=1\), gives the scalar product of their ungraded standard-coefficient vectors. On the category-O side (8.334) identifies D(words) with V of the corresponding projective words. Full faithfulness (8.310) and BGG give
\[
 \dim\operatorname{Hom}_{C}(VQ,VQ')
 =\dim\operatorname{Hom}_{\mathcal O}(Q,Q')
 =\sum_w(Q:M_w)(Q':M_w).
 \tag{8.337}
\]
The checked two-Verma wall formula says these word coefficients are the coefficients of the same group-algebra products \((1+s_i)\), with labels inverted. Their scalar product is unchanged by inversion. Hence (8.336) is an isomorphism for words. Projecting the actual Hom spaces to source and target idempotents proves it for every summand.

Here is the needed indecomposability detail, using the already proved Theorem 8.10 and the real-to-complex bridge in Section 8.15.1. In the source-u convention (8.100), write
\[
 h(B_x)=\sum_y h_{y,x}(u)H_y=C_x.
\]
The normalized top coefficient is \(h_{x,x}=1\), and every strict-lower coefficient belongs to \(u\mathbb Z[u]\), by the KL degree bound in that theorem. Self-duality makes the two support characters \(h_\Delta(B_x)\) and \(h_\nabla(B_x)\) equal. The actual Hom formula (8.109)/(8.123) consequently gives
\[
 \overline{r_u\operatorname{End}_{R-R}(B_x)}
 =\sum_y h_{y,x}(u)^2,
 \qquad
 r_u\operatorname{End}_{R-R}(B_x)
 =\sum_y h_{y,x}(u^{-1})^2.
 \tag{8.338}
\]
The bar and the shift convention matter here. Equation (8.108) defines \(r_u(\bigoplus_j R(a_j))=\sum_j u^{a_j}\), while (8.296) makes the generator of \(R(a_j)\) have internal degree \(-a_j\). Equivalently, a same-label pair \(\Delta_y(n),\nabla_y(m)\) contributes the shift exponent \(m-n\) in (8.123) and a free Hom generator of internal degree \(n-m\). Thus (8.338) gives exactly one free generator of internal degree zero and all remaining generators of strictly positive internal degree. Since R has no negative degrees, the bimodule endomorphism algebra has no negative homogeneous pieces and its degree-zero piece is \(\mathbb C\).

The graded isomorphism (8.336) now gives the same conclusions for \(A_x=\operatorname{End}_C(D(B_x))\): \(A_x^d=0\) for \(d<0\), and \(A_x^0=\mathbb C\). The module \(D(B_x)\) is finite-dimensional and supported in a finite interval of internal degrees. Hence the positive-degree ideal \(I_x=\bigoplus_{d>0}A_x^d\) is nilpotent: a product of more positive-degree maps than the width of that interval has degree larger than every possible endomorphism degree. Every endomorphism has a unique form \(c\,1+n\), with \(n\in I_x\). If \(c\ne0\), its inverse is the finite geometric series \(c^{-1}\sum_{j\ge0}(-c^{-1}n)^j\); if \(c=0\), it is nilpotent and cannot be a unit. Therefore the entire ungraded algebra is local, with unique maximal ideal \(I_x\) and residue \(\mathbb C\). This proves ungraded indecomposability of \(D(B_x)\) without a semisimple matrix-block classification.

If two such modules were isomorphic after forgetting grading, take homogeneous components of an isomorphism and its inverse. Their degree-zero composite is the identity and is a sum of homogeneous composites. In a local degree-zero ring at least one of these composites is a unit. It splits a graded isomorphism up to a shift. (8.336) lifts the two homogeneous maps to bimodule maps; their composite reduces to a unit and hence is not nilpotent. The local degree-zero bimodule endomorphism lemma makes it invertible. Thus the original bimodules are isomorphic up to that shift, and Section 8.7.16 distinguishes their labels. Consequently \(D(B_x)\) are pairwise distinct ungraded indecomposables.

#### 8.15.9. Exact projective indexing and Verma coefficient statement

For \(x=s_1\cdots s_n\) reduced, use the word \(B_{s_1}\cdots B_{s_n}\). After augmentation it corresponds by (8.334) to
\[
 V(\theta_{s_1}\cdots\theta_{s_n}M_e).
 \tag{8.339}
\]
Composition applies \(\theta_{s_n}\) first. Since a wall crossing changes the **right** Verma label \(w\) to \(ws\), the unique maximal-length projective in this word is \(P_{x^{-1}}\), with multiplicity one. All other labels have smaller length.

Induct on length. The regular bimodule word has the single top \(B_x\), with all other indecomposable labels below x. (8.336) matches its idempotent decomposition to the actual projective word, and Section 8.15.8 proves that \(D(B_x)\) is indecomposable. Lower labels have already been identified. Hence
\[
 V P_z\cong D(B_{z^{-1}})
 \quad\text{as ungraded C-modules}.
 \tag{8.340}
\]
There is no claim of an intrinsic ordinary category-O grading before constructing a graded lift. The displayed lift \(D(B_{z^{-1}})\) uses the normalization (8.296) and top graph shift zero.

Let \(a_{y,x}(v)\) be the coefficient of \(H_y\) in the independently constructed regular character \(h(B_x)\), using its fixed Hecke normalization. Evaluation at \(v=1\) forgets every grading shift. The word coefficients, the two actual decompositions just matched, and induction on the maximal label give
\[
 (P_z:M_w)=a_{w^{-1},z^{-1}}(1).
 \tag{8.341}
\]
Explicitly the equation holds for the whole word because its wall flags are the coefficients of the group-algebra product \((1+s_n)\cdots(1+s_1)\); inversion identifies it with the bimodule product. Subtract the matching lower projective/bimodule summands, whose ungraded multiplicities are the same by (8.336) and whose coefficients agree by induction. The remaining top summands give (8.341). This argument is about actual split idempotents; equality of word dimensions alone is not used to assign their labels.

Finally ordinary BGG reciprocity gives the exact desired comparison
\[
 \boxed{[M(w\cdot\lambda):L(z\cdot\lambda)]
 =a_{w^{-1},z^{-1}}(1).}
 \tag{8.342}
\]
The Hodge and character theorem, Theorem 8.10 and its normalization (8.224), identifies \(h(B_x)=C'_x\); Section 8.15.1 supplies its actual complex scalar-extension bridge. The anti-involution \(H_y\mapsto H_{y^{-1}}\) preserves bar, Bruhat order and the triangular degree condition. Canonical uniqueness sends \(C'_x\) to \(C'_{x^{-1}}\); thus
\[
 P_{w^{-1},z^{-1}}=P_{w,z},
 \quad [M_w:L_z]=P_{w,z}(1).
 \tag{8.343}
\]
This proves why the source's inverse index disappears in the final dominant multiplicity formula. No multiplication by \(w_0\) is inserted in this algebraic route.

## 9. The six Verma modules for $\mathfrak{sl}_3$

Let $s=s_1$, $t=s_2$, and $w_0=sts=tst$. For type $A_2$, $\rho=\alpha_1+\alpha_2$. The six simple labels in the principal block are as follows.

| $w$ | $w\mathbin{\cdot}0$ |
|---|---|
| $1$ | $0$ |
| $s$ | $-\alpha_1$ |
| $t$ | $-\alpha_2$ |
| $st$ | $-2\alpha_1-\alpha_2$ |
| $ts$ | $-\alpha_1-2\alpha_2$ |
| $w_0$ | $-2\alpha_1-2\alpha_2$ |

Bruhat order has levels $1$, then $s,t$, then $st,ts$, then $w_0$; each element in a middle level lies below both elements in the next level. All comparable pairs have polynomial one. Here is an algebraic verification of that claim, rather than an appeal to a table.

Put $v=q^{1/2}$. The two degree-one elements $v^{-1}(1+T_s)$ and $v^{-1}(1+T_t)$ are bar invariant. Their products give
\[
C'_{st}=v^{-2}(1+T_s+T_t+T_{st}),\qquad
C'_{ts}=v^{-2}(1+T_s+T_t+T_{ts}).
\]
Using $T_s^2=(q-1)T_s+q$,
\[
C'_s C'_t C'_s-C'_s
=v^{-3}(1+T_s+T_t+T_{st}+T_{ts}+T_{w_0}). \tag{9.1}
\]
The left side is bar invariant. All these expansions have the required leading coefficient and polynomial degree bounds in (8.2). Uniqueness in Theorem 8.1 identifies them as the canonical basis. Together with $C'_1=1$, they cover every element of $S_3$. Thus $P_{x,y}=1$ for $x\leq y$, and is zero otherwise. Saying “all are one” must retain this comparability condition.

Abbreviate $M_w=M(w\mathbin{\cdot}0)$ and $L_w=L(w\mathbin{\cdot}0)$. Equation (8.3) now gives the following six identities of characters, or equivalently classes in the Grothendieck group:
\[
\begin{aligned}[c]
[M_{w_0}]&=[L_{w_0}],\\
[M_{st}]&=[L_{st}]+[L_{w_0}],\\
[M_{ts}]&=[L_{ts}]+[L_{w_0}],\\
[M_s]&=[L_s]+[L_{st}]+[L_{ts}]+[L_{w_0}],\\
[M_t]&=[L_t]+[L_{st}]+[L_{ts}]+[L_{w_0}],\\
[M_1]&=[L_1]+[L_s]+[L_t]+[L_{st}]+[L_{ts}]+[L_{w_0}].
\end{aligned} \tag{9.2}
\]
These are composition-multiplicity identities, not direct-sum decompositions of modules. Each $L_w$ is the unique simple quotient of the corresponding $M_w$; $L_1$ is the trivial finite-dimensional module.

In the order $1,s,t,st,ts,w_0$, the complete decomposition matrix and its Cartan matrix are
\[
D=\begin{pmatrix}
1&1&1&1&1&1\\
0&1&0&1&1&1\\
0&0&1&1&1&1\\
0&0&0&1&0&1\\
0&0&0&0&1&1\\
0&0&0&0&0&1
\end{pmatrix},\qquad
C=\begin{pmatrix}
1&1&1&1&1&1\\
1&2&1&2&2&2\\
1&1&2&2&2&2\\
1&2&2&4&3&4\\
1&2&2&3&4&4\\
1&2&2&4&4&6
\end{pmatrix}. \tag{9.3}
\]
The second follows by the proved formula $D^{\mathsf T}D$. Reciprocity reads the Verma multiplicities of $P(y\mathbin{\cdot}0)$ from column $y$ of $D$. Explicitly its factors are:

| Projective | Verma factors, each once |
|---|---|
| $P(0)$ | $M_1$ |
| $P(s\mathbin{\cdot}0)$ | $M_1,M_s$ |
| $P(t\mathbin{\cdot}0)$ | $M_1,M_t$ |
| $P(st\mathbin{\cdot}0)$ | $M_1,M_s,M_t,M_{st}$ |
| $P(ts\mathbin{\cdot}0)$ | $M_1,M_s,M_t,M_{ts}$ |
| $P(w_0\mathbin{\cdot}0)$ | all six $M_w$ |

The table specifies multiplicities, without claiming that its listed order is the order of every filtration. Inverting $D$ also recovers the simple characters. For example,
\[
\operatorname{ch}L_1=\operatorname{ch}M_1-\operatorname{ch}M_s-\operatorname{ch}M_t
+\operatorname{ch}M_{st}+\operatorname{ch}M_{ts}-\operatorname{ch}M_{w_0},
\]
which agrees with the finite-dimensional character formula for the trivial module.

## 10. Exercises and complete solutions

### 10.1. Recognizing the finite-dimensional objects

**Exercise.** Check all three defining conditions for a finite-dimensional representation of $\mathfrak g$, and describe its simple constituents in $\mathcal O$.

**Solution.** A finite vector-space basis generates it as a $U(\mathfrak g)$-module. Complete reducibility expresses it as a finite sum of finite-dimensional highest-weight simples. Each has a Cartan weight decomposition, so the representation is $\mathfrak h$-semisimple. The orbit $U(\mathfrak n^+)v$ lies in a finite-dimensional space, proving local finiteness. The constituents are precisely $L(\lambda)$ with dominant integral $\lambda$, by the finite-dimensional highest-weight classification. Conversely each such simple is finite-dimensional, and finite sums of them give all finite-dimensional objects.

### 10.2. Locating every singular vector in a rank-one Verma module

**Exercise.** Starting from the $\mathfrak{sl}_2$ commutators, calculate the action on $f^kv_0$. Find all singular lines and the quotient when a proper singular line occurs.

**Solution.** Commuting $h$ through $k$ factors of $f$ gives $(\lambda-2k)f^kv_0$. For the $e$ action, the coefficient $c_k$ satisfies
\[
c_0=0,\qquad c_k=c_{k-1}+\lambda-2(k-1),
\]
because $ef^k=fef^{k-1}+hf^{k-1}$. Summing gives $c_k=k\lambda-k(k-1)=k(\lambda-k+1)$. The top $k=0$ is always singular. For $k>0$, singularity holds precisely when $\lambda=k-1$. Thus for $\lambda=n\geq0$ the proper singular line is $\mathbb C f^{n+1}v_0$, of weight $-n-2$; otherwise there is none. Its PBW tail is $M(-n-2)$, which is simple since $-n-2$ is not nonnegative. The quotient has basis the images of $v_0,\ldots,v_n$, dimension $n+1$. For $1\leq k\leq n$, its raising coefficient $k(n-k+1)$ is nonzero and the image of $v_{k-1}$ survives. Thus its only singular line is its top, which generates the entire quotient. Any nonzero submodule has a singular vector, so the quotient is simple. It is $L(n)$, proving (7.3).

### 10.3. Tensoring without losing finite generation

**Exercise.** Let $F$ be finite-dimensional and $M\in\mathcal O$. Prove that the diagonal tensor action preserves $\mathcal O$, paying particular attention to finite generation.

**Solution.** Choose a basis $a_1,\ldots,a_d$ of $F$ and weight generators $v_1,\ldots,v_r$ of $M$. Let $T$ be the submodule generated by $a_i\otimes v_j$. We prove $a\otimes uv_j\in T$ for every word $u$ in $\mathfrak g$ by induction on its length. The assertion at length zero is the choice of generators. If $u=xu'$,
\[
a\otimes xu'v_j=x(a\otimes u'v_j)-(xa)\otimes u'v_j;
\]
both terms belong to $T$ by induction, expanding $xa$ in the chosen basis. Thus $T=F\otimes M$.

The weights are sums of a weight of $F$ and a weight of $M$, and each weight space is a finite sum of finite-dimensional spaces. Finally, for each pure tensor, the positive-root orbit is contained in $F\otimes U(\mathfrak n^+)v$, a finite-dimensional subspace stable under that action. A finite sum of pure tensors has its orbit in the sum of these finite spaces. This proves all three defining conditions.

### 10.4. Constructing the second principal projective

**Exercise.** Construct the cover of $L(-2)$ inside $L(1)\otimes M(-1)$. Give its Verma filtration and demonstrate that its central action is not scalar.

**Solution.** Use the vectors $p,q$ from (7.8). The formulas
\[
f^kp=a\otimes v_k+k b\otimes v_{k-1},\qquad f^kq=b\otimes v_k
\]
show that they form a free two-generator $\mathbb C[f]$ basis. The vector $p$ is singular of weight zero, so its free tail is an embedded $M(0)$. Modulo that submodule, $q$ is a singular vector of weight $-2$ with a free tail, giving quotient $M(-2)=L(-2)$. This gives the flag with factors $M(0)$ and $M(-2)$.

The singleton-character Verma $M(-1)$ is projective by the highest-weight functor, so the tensor product is projective by exact dual tensor adjunction. All its factors have character $\chi_0$, and hence the full tensor product is the required central-character direct summand. Since $q$ generates it and has weight $-2$, it has no quotient $L(0)$. Its quotient $L(-2)$ occurs in its head only once: a map is determined by $q$, whose target weight space in $L(-2)$ is one-dimensional. Decomposing into indecomposable projectives would give one simple head for each summand, so there can be only one summand. It is therefore $P(-2)$.

For a direct nonsplitting check, a highest lift of the quotient would have to be $q+c fp$, but $e(q+c fp)=p\ne0$. Lastly, (7.4) gives $\Omega q=4fp$, $\Omega p=0$. Centrality implies $\Omega^2=0$ on this module, while $fp\ne0$ shows $\Omega\ne0$. Thus the centre acts with a generalized eigenvalue, not by its scalar eigenvalue alone.

### 10.5. Deriving reciprocity from a standard filtration

**Exercise.** Suppose projective covers have Verma filtrations and an exact restricted duality fixes the simple modules. Prove BGG reciprocity, supplying the needed relation between standard and costandard modules.

**Solution.** Put $\nabla(\mu)=D M(\mu)$. A highest vector in this restricted dual is a functional annihilating $\mathfrak n^-M(\mu)$, so the universal Verma property gives
\[
\dim\operatorname{Hom}(M(\gamma),\nabla(\mu))=\delta_{\gamma\mu}.
\]
As a Cartan-semisimple $\mathfrak b$-module the costandard module satisfies
\[
\operatorname{Hom}_{\mathfrak b}(N,\nabla(\mu))
\simeq\operatorname{Hom}_{\mathfrak h}(N,\mathbb C_\mu),
\]
with the inverse $\ell\mapsto[v\mapsto(u\mapsto\ell(uv))]$. A weight vector produces a function on one finite PBW root-degree space, so it lies in the restricted coinduced module. The right side is exact. An extension of $M(\gamma)$ by $\nabla(\mu)$ consequently has a $\mathfrak b$-retraction onto the submodule. Subtracting that retraction from a lift of the highest vector produces a singular lift, which gives a $\mathfrak g$-section. Thus the extension splits.

For each filtration step of $P(\lambda)$, pushout along a map from the preceding subobject into $\nabla(\mu)$ now splits. Restriction on Hom spaces is therefore surjective, with kernel of dimension $\delta_{\gamma\mu}$ for that step's Verma label $\gamma$. Summation gives
\[
\dim\operatorname{Hom}(P(\lambda),\nabla(\mu))
=(P(\lambda):M(\mu)).
\]
On a composition series of $\nabla(\mu)$, exactness of Hom from $P(\lambda)$ and its unique simple head give the same dimension as $[\nabla(\mu):L(\lambda)]$. Exact duality leaves each simple unchanged, so this is $[M(\mu):L(\lambda)]$. Equating the dimensions proves reciprocity and independence of the Verma-filtration multiplicities.

## What this lesson does not prove

The standard Hecke basis, reduced-subword order, bar triangularity, canonical basis, integral polynomial coefficients, degree bounds and full longest-element inverse-polynomial identity are proved in Section 8 for every finite Weyl group. The rank-one and $A_2$ computations are examples of these general algebraic results. The Kazhdan–Lusztig multiplicity formula is proved in Sections 8.12–8.15, Theorem 8.13, with Etingof, Theorem 21.6, fixing the convention. Sections 8.7–8.11 fully prove finite-Weyl coefficient positivity, the canonical indecomposable character theorem and Hodge theory by the algebraic route. Sections 8.12–8.15 prove the actual finite complex regular integral category $\mathcal O$ comparison and identify these coefficients with general Verma multiplicities at the dominant convention. Section 8.6 proves the full dual-standard character, IC recognition and parity/positivity, the signed Grothendieck relation and the dominant Verma conversion conditionally on explicitly stated mixed, geometric, pointwise-purity and exact-localization inputs. Those general inputs, including localization and the regular-holonomic/perverse comparison, are not proved here. Every category $\mathcal O$ finiteness, projective-cover, Verma-filtration, duality and reciprocity assertion used above has been proved, for all complex highest weights. Earlier course theorems listed in the introduction are prerequisites.

## References

- P. Etingof, *Representations of Lie Groups*, MIT 18.757, Fall 2023: §§15–16 for category $\mathcal O$ and projectives; Lemma 12.3 for graded freeness; §20, especially Corollary 20.5 and Theorem 20.6, for Verma filtrations and reciprocity; §21, Proposition 21.1 and Theorems 21.5–21.6, for the Hecke normalization and Kazhdan–Lusztig statement. [Official course notes](https://ocw.mit.edu/courses/18-757-representations-of-lie-groups-fall-2023/pages/lecture-notes/).
- J. Bernstein, I. Gelfand and S. Gelfand, *Category of $\mathfrak g$-modules*, Functional Analysis and Its Applications 10 (1976), 87–92; original Russian version 10(2), 1–8: §3, Definition 1. [Freely accessible original Russian text](https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2144&what=fullt).
- M. Kashiwara, *Representation theory and D-modules on flag varieties*, Astérisque 173–174 (1989), 55–109, §6.3 for vanishing and generation, and §6.4, Theorem 6.4.1 (p. 96), for the localization equivalence with a regular antidominant parameter. [Freely accessible original text](https://numdam.org/book-part/AST_1989__173-174__55_0/).
- J.-L. Brylinski and M. Kashiwara, *Kazhdan–Lusztig conjecture and holonomic systems*, Inventiones Mathematicae 64 (1981), 387–410: introduction and §8, Theorem 8.1. [Author-hosted paper](https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/KL.pdf).
- M. Kashiwara and T. Tanisaki, *Parabolic Kazhdan–Lusztig polynomials and Schubert varieties*, arXiv math/9908153v2: §§3 and 5, especially Propositions 5.1–5.2, Lemma 5.3 and Theorem 5.4, for the precise mixed-operation, Bruhat and IC correspondence. The conditional deductions in Section 8.6 expand the character and matrix mechanisms; they do not import the missing geometric foundations as proved course theorems. [Exact primary version](https://arxiv.org/abs/math/9908153v2).

- B. Elias and G. Williamson, *The Hodge theory of Soergel bimodules*, arXiv:1212.0791v2: §§2–6. Sections 8.8–8.11 expand the finite-Weyl forms, support splitting, minimal-complex linearity, descent and Hodge induction. [Freely accessible exact version](https://arxiv.org/abs/1212.0791v2).
- N. Libedinsky and G. Williamson, *Standard objects in 2-braid groups*, arXiv:1205.4206v2: §3.1 and Proposition 3.7 in §3.3. [Freely accessible exact version](https://arxiv.org/abs/1205.4206v2).
- G. Williamson, *Singular Soergel bimodules*, arXiv:1010.1283v2: introduction and §7.4, with the normalization correction in v3. Section 8.10 supplies the actual left-regular, right-simple construction. [Freely accessible v2](https://arxiv.org/abs/1010.1283v2), [v3 with erratum](https://arxiv.org/abs/1010.1283v3).

- W. Soergel, *Kategorie O, perverse Garben und Moduln über den Koinvarianten zur Weylgruppe*, MPI/89-46, 28 July 1989: §§2.1–2.5, especially Endomorphismensatz 7, Struktursatz 9 and Theorems 10–11. Sections 8.12–8.15 supply the finite ordinary-category proof, including its invariant, root-local and scalar-extension steps. [Freely accessible institutional original](https://archive.mpim-bonn.mpg.de/id/eprint/3653/1/preprint_1989_46.pdf).
- P. Fiebig, *The combinatorics of category O over symmetrizable Kac–Moody algebras*, arXiv:math/0305378v2, 25 February 2004: §§2–5. The deformed comparison is used as a primary reference; the proofs here retain the finite ordinary-category scope and projective-target full faithfulness. [Freely accessible exact version](https://arxiv.org/abs/math/0305378v2).
