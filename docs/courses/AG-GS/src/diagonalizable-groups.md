# Diagonalizable groups and groups of multiplicative type

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A diagonal matrix acts separately on each coordinate line. A diagonalizable group scheme retains that separation even when it is nonreduced: its representations are graded by characters. Over a field, a group may become diagonalizable only after extending scalars. The Galois action on its characters records the obstruction to splitting.

We treat globally diagonalizable groups \(D_S(M)\) over arbitrary schemes \(S\), including arbitrary exponent groups, torsors and free affine quotients, and finite-presentation relative groups of multiplicative type, classified by their étale character sheaves. Statements about arbitrary subgroups require particular care: the subgroup theorem below is over a field, and general-base counterexamples explain the necessary distinctions.

## 1. From an abelian group to a group scheme

For an abelian group \(M\), written additively, define the group algebra

\[
R[M]=\bigoplus_{m\in M}R\,e^m,\qquad e^m e^n=e^{m+n}.
\]

Its Hopf operations are

\[
\Delta(e^m)=e^m\otimes e^m,\qquad
\epsilon(e^m)=1,\qquad
\iota(e^m)=e^{-m}.
\tag{1}
\]

Checking these operations on the basis verifies coassociativity, counit and antipode identities. The multiplication is commutative because \(M\) is abelian. Over a scheme \(S\), the corresponding quasi-coherent algebra is \(\mathcal O_S[M]\); put

\[
D_S(M)=\operatorname{Spec}_S\mathcal O_S[M].
\tag{2}
\]

The construction commutes with every base change. It is affine and flat over \(S\), since its coordinate module is free on each affine chart.

**Proposition 1.1. Points.** For every \(S\)-scheme \(T\),

\[
D_S(M)(T)
=\operatorname{Hom}_{\mathrm{Ab}}
\bigl(M,\Gamma(T,\mathcal O_T^\times)\bigr).
\tag{3}
\]

**Proof.** A map to the relative spectrum is an \(\mathcal O_T\)-algebra map \(\mathcal O_T[M]\to\mathcal O_T\). It is determined by the images of the global symbols \(e^m\). These images are units because \(e^m e^{-m}=1\), and they satisfy \(e^{m+n}\mapsto e^m e^n\). Thus they give the indicated group homomorphism. Conversely such a homomorphism defines an algebra map locally by the finite sums in the group algebra, and these maps glue. Formula (1) makes multiplication of points the pointwise multiplication of these unit-valued homomorphisms. \(\square\)

In particular

\[
D_S(\mathbf Z)=\mathbf G_{m,S},\qquad
D_S(\mathbf Z/n)=\mu_{n,S},\qquad
D_S(\mathbf Z^r)=\mathbf G_{m,S}^r.
\tag{4}
\]

Here \(n\geq1\). Also \(D_S(M\oplus N)=D_S(M)\times_SD_S(N)\), because the bases identify \(\mathcal O_S[M\oplus N]\) with \(\mathcal O_S[M]\otimes_{\mathcal O_S}\mathcal O_S[N]\).

When \(M\) is finitely generated, its abelian-group decomposition gives

\[
M\simeq\mathbf Z^r\oplus\bigoplus_{i=1}^a\mathbf Z/n_i,
\qquad
D_S(M)\simeq\mathbf G_m^r\times_S\prod_i\mu_{n_i}.
\tag{5}
\]

Thus \(D_S(M)\) is of finite presentation over \(S\). Conversely, if \(S\ne\varnothing\) and \(D_S(M)\) is of finite type, take a geometric fibre over \(S\). If its algebra \(K[M]\) has finitely many algebra generators, the union of their finite monomial supports generates a subgroup \(M_0\subset M\). The generated algebra lies in \(K[M_0]\). Linear independence of all the \(e^m\) forces \(M_0=M\). Hence \(M\) is finitely generated. This proves the equivalence between finite type and finite generation in (2), for a nonempty base.

## 2. Characters detect the exponent group

A **character** of a group scheme \(G/S\) is a homomorphism \(G\to\mathbf G_{m,S}\). For an affine Hopf algebra, it corresponds to a group-like element \(a\), meaning

\[
\Delta(a)=a\otimes a,\qquad\epsilon(a)=1.
\]

The antipode then provides its inverse.

**Lemma 2.1. Group-like elements over a ring.** In \(R[M]\), every group-like element has the unique form

\[
a=\sum_m c_m e^m,
\qquad c_m^2=c_m,\quad c_m c_n=0\ (m\ne n),
\quad\sum_m c_m=1,
\tag{6}
\]

with finitely many nonzero coefficients. Conversely each such expression is group-like. If \(\operatorname{Spec}R\) is nonempty and connected, exactly one coefficient is \(1\), so \(a=e^m\) for one \(m\in M\).

**Proof.** Compare coefficients of \(e^m\otimes e^n\) in \(\Delta(a)=a\otimes a\). For \(m=n\) this gives \(c_m=c_m^2\), and for \(m\ne n\) it gives \(c_m c_n=0\). The counit gives the sum condition. These conditions also prove the converse by the same computation. The inverse is \(\sum_m c_m e^{-m}\).

Idempotents correspond to open and closed subsets of \(\operatorname{Spec}R\). On a connected nonempty spectrum each is \(0\) or \(1\); orthogonality and the sum condition allow exactly one coefficient equal to \(1\). Uniqueness follows from the group-algebra basis. \(\square\)

Each \(m\) therefore gives the character

\[
\chi_m(f)=f(m)
\quad\text{for }f:M\to\Gamma(T,\mathcal O_T^\times).
\]

On a general scheme, Lemma 2.1 says that a character locally chooses one exponent \(m\). Its character sheaf is the constant sheaf \(M_S\): its sections are locally constant functions from the base to the discrete set \(M\). On a non-quasi-compact scheme their image need not be finite; the statement is sheaf-local, not an assertion that every global section is a single finite sum.

**Theorem 2.2. The diagonalizable anti-equivalence.** If \(S\) is nonempty and connected, then for any abelian groups \(M,N\),

\[
\operatorname{Hom}_{S\text{-groups}}(D_S(M),D_S(N))
\simeq\operatorname{Hom}_{\mathrm{Ab}}(N,M).
\tag{7}
\]

Consequently \(M\mapsto D_S(M)\) is an anti-equivalence between finitely generated abelian groups and finite-type globally diagonalizable group schemes over \(S\).

**Proof.** A homomorphism on the left is a Hopf algebra map \(\mathcal O_S[N]\to\mathcal O_S[M]\). Each basis element \(e^n\) maps to a group-like section. By Lemma 2.1 it locally chooses an exponent of \(M\); these choices glue to a locally constant function on \(S\). Connectedness makes that exponent constant. Multiplicativity and the unit show that the resulting rule \(n\mapsto m(n)\) is a group homomorphism.

Conversely a homomorphism \(N\to M\) gives the Hopf map \(e^n\mapsto e^{m(n)}\). These procedures are inverse and compatible with composition, proving (7). By definition a globally diagonalizable group is some \(D_S(M)\), and Section 1 proves that its finite-type condition is equivalent to finite generation of \(M\). This supplies essential surjectivity and the claimed restriction. \(\square\)

For a disconnected base, a morphism may choose different exponent maps on different open and closed pieces. If \(N\) is finitely generated, all its generator images can be chosen on one common neighbourhood of each point, so the homomorphism sheaf in (7) is the constant sheaf with value \(\operatorname{Hom}(N,M)\). The finite-generation condition is needed for this uniform local statement, and will hold in the rigidity theorem over fields.

**Proposition 2.3. Biduality as sheaves.** Write \(X^*(G)=\underline{\operatorname{Hom}}(G,\mathbf G_m)\) for the sheaf of characters, without requiring it to be represented by a finite scheme. For every abelian group \(M\), evaluation identifies

\[
\begin{gathered}
X^*(D_S(M))=M_S,\\
X^*(M_S)=D_S(M).
\end{gathered}
\]

In particular both groups are isomorphic to their character biduals. This includes infinite \(M\); it is a sheaf-duality assertion, rather than an assertion that the full linear dual of an infinite group algebra is a Hopf algebra.

**Proof.** The first identity is Lemma 2.1 and its local gluing interpretation. A homomorphism from the constant sheaf \(M_T\) to \(\mathbf G_{m,T}\) is determined by the images of its constant elements, a homomorphism \(M\to\Gamma(T,\mathcal O_T^\times)\). Conversely that rule defines the morphism locally on each constant piece and glues. Proposition 1.1 gives the second identity. Under these identifications the bidual evaluation sends \(f\in D_S(M)(T)\) to the rule \(m\mapsto f(m)\), and sends \(m\in M_T\) to the character \(\chi_m\). These are the two indicated isomorphisms, so all identifications are compatible with evaluation and every base change.

More generally a homomorphism \(G\to X^*(H)\) is the same as a pairing \(G\times H\to\mathbf G_m\) which is a homomorphism in each variable: evaluate in one direction and curry in the other. Interchanging the variables gives \(\operatorname{Hom}(G,X^*(H))=\operatorname{Hom}(H,X^*(G))\). Evaluation satisfies \(X^*(\operatorname{ev}_G)\circ\operatorname{ev}_{X^*(G)}=1\), since both sides evaluate a character on its argument. Therefore if \(\operatorname{ev}_G\) is an isomorphism, so is \(\operatorname{ev}_{X^*(G)}\). These identities prove that character duality is an anti-equivalence on the category of reflexive commutative group sheaves. The displayed diagonalizable and constant groups are its explicit examples. \(\square\)

## 3. Representations are gradings

**Theorem 3.1. Weight decomposition over any base.** Quasi-coherent representations of \(D_S(M)\) are equivalent to \(M\)-graded quasi-coherent \(\mathcal O_S\)-modules. On an affine chart this means

\[
E=\bigoplus_{m\in M}E_m.
\tag{8}
\]

Actions on an affine \(S\)-scheme correspond to \(M\)-graded quasi-coherent algebras, with \(A_m A_n\subset A_{m+n}\) and \(1\in A_0\). Invariant modules and algebras are their degree-zero parts, and taking invariants of representations is exact.

**Proof.** On \(\operatorname{Spec}R\), write the coaction of a vector \(v\) as

\[
\rho(v)=\sum_m v_m\otimes e^m,
\]

with finite support. Coassociativity and linear independence in \(R[M]\otimes_RR[M]\) give \(\rho(v_m)=v_m\otimes e^m\); the counit gives \(v=\sum_m v_m\). Define \(E_m\) by this displayed weight condition. If a finite sum of vectors of distinct weights is zero, apply \(\rho\) and compare coefficients to see that each vector is zero. Thus the sum in (8) is direct and exhaustive.

Conversely define \(\rho(v_m)=v_m\otimes e^m\) on an \(M\)-graded module. Formula (1) verifies the coaction identities. These constructions are inverse. The coefficient maps commute with restriction and localization, so the weight modules and the equivalence glue on \(S\).

For an algebra, the coaction is an algebra homomorphism exactly when products add their weights and the unit has weight zero. This proves the assertion about affine actions. Invariance \(\rho(v)=v\otimes1\) is precisely weight zero. A morphism of comodules preserves each weight. Kernels, cokernels and images are therefore taken degree by degree; in particular a surjective equivariant map is surjective on degree-zero parts. This proves exactness of invariants. \(\square\)

Over a field each weight space has a basis of one-dimensional representations. Thus representations of a diagonalizable group are semisimple, including those of \(\mu_p\) in characteristic \(p\). This is compatible with its failure of smoothness: exactness of invariants is a statement about comodules, not about reduced geometric points. Over a general base the weight modules need not be semisimple as modules over the ground ring.

*Comparison locators:* [Stacks, Tags 0EKJ–0EKL] for \(\mathbf G_m\); Milne, *Algebraic Groups*, Chapter 12d for the field case.

### 3.2. Fixed points and invariant functions

Let \(X=\operatorname{Spec}A\) carry an action of \(D_R(M)\), and use its grading \(A=\bigoplus_{m\in M}A_m\). A fixed point must remain fixed after every extension of its test algebra. This includes the universal element of the group; using only rational points would lose infinitesimal groups such as \(\mu_p\).

**Proposition 3.2. The fixed subscheme.** Put

\[
I=(A_m\mid m\ne0)\subset A.
\]

Then \(X^{D_R(M)}=\operatorname{Spec}(A/I)\) represents the fixed-point functor, and formation of this scheme commutes with arbitrary base change. If \(A\) is finitely presented over \(R\), so is \(A/I\).

**Proof.** For an \(R\)-algebra \(C\), a point is an algebra map \(f:A\to C\). Its two pullbacks under the orbit and constant maps to \(C[M]\) send \(a_m\) to \(f(a_m)e^m\) and \(f(a_m)e^0\). The basis \(e^m\) is linearly independent over \(C\). These maps are equal precisely when \(f(a_m)=0\) for every \(m\ne0\), which is precisely factorization through \(A/I\). This is an equality of universal orbit maps, so it implies fixedness after every further base change.

Weights commute with scalar extension because the coaction coefficient projectors give an actual direct sum. The extended ideal is therefore generated by the nonzero-weight parts of the extended algebra, proving base-change compatibility.

Choose finitely many algebra generators for \(A\), and replace them by the finitely many homogeneous components appearing in them. This still gives finitely many algebra generators, say \(a_1,\ldots,a_s\). The ideal \(I\) is generated by those \(a_i\) whose weight is nonzero: every homogeneous polynomial of nonzero weight has each monomial divisible by at least one such generator. Conversely each such generator belongs to \(I\). Thus only finitely many relations are added to a finite presentation of \(A\), and \(A/I\) is finitely presented. \(\square\)

For example, give \(R[x,y]\) weights \(1,-1\). Invariant functions form \(R[xy]\), whereas the fixed scheme is \(\operatorname{Spec}R\), defined by \((x,y)\). The affine invariant quotient and the fixed subscheme answer different questions. Even \(A/I\) is generally a quotient of \(A_0\), since \(I\cap A_0\) can contain products of opposite nonzero weights.

### 3.3. Smooth fixed loci, including infinitesimal acting groups

**Lemma 3.3. A coefficient calculation for cocycles.** Let \(E\) be a representation of \(D_C(M)\), with coaction \(\rho\), and let \(c\in E\otimes_C C[M]\) satisfy the universal identity

\[
(1\otimes\Delta)c=c\otimes1+(\rho\otimes1)c.
\]

If \(u\in E\) is the coefficient of \(e^0\) in \(c\), then

\[
c=u\otimes1-\rho(u).
\]

**Proof.** Apply to the last tensor factor the coefficient functional \(\lambda_0(e^m)=0\) for \(m\ne0\), \(\lambda_0(e^0)=1\). Since \(\Delta(e^m)=e^m\otimes e^m\), the left side becomes \(u\otimes1\). The two terms on the right become \(c\) and \(\rho(u)\). Rearrangement gives the result. No division by a group order or assumption on characteristic occurs. \(\square\)

**Theorem 3.4. Smoothness of the fixed locus.** Over an arbitrary ring \(R\), if \(X/R\) is affine and smooth of finite presentation, then \(X^{D_R(M)}/R\) is smooth of finite presentation. At a fixed section, its tangent functor is the invariant part of the tangent functor of \(X\).

**Proof.** Finite presentation follows from Proposition 3.2. It remains to prove the infinitesimal lifting criterion. Let \(J^2=0\) in an \(R\)-algebra \(C\), and let \(\bar x\in X^{D_R(M)}(C/J)\). Smoothness of the affine scheme \(X\) supplies a lift \(x\in X(C)\).

Put \(\bar C=C/J\). The set of lifts of \(\bar x\), after any flat extension of \(C\), is a torsor under

\[
E=\operatorname{Hom}_{\bar C}(\bar x^*\Omega_{X/R},J).
\]

Indeed differences of two coordinate maps are derivations into \(J\), and adding any such derivation gives another algebra map because \(J^2=0\). The cotangent module in this formula is finite projective over \(\bar C\), so its Hom module commutes with the flat extensions used below. Fixedness of \(\bar x\) gives its cotangent module the contragredient action, by inverse pullback; dualizing and giving \(J\) the trivial action gives \(E\) the differential action. The action on lifts is affine with this linear part: the differential sends the difference of two lifts to the corresponding difference of their translates.

Over the free, hence flat, extension \(C[M]\), let \(g\) be the universal group element. Write

\[
g x=x+c(g),\qquad c\in E\otimes_C C[M].
\]

Associativity of the action, over the equally flat extension \(C[M\oplus M]\), gives \(c(gh)=c(g)+g c(h)\). This is exactly the identity in Lemma 3.3. Hence \(c(g)=u-g u\) for its weight-zero coefficient \(u\). The lift \(x'=x+u\) satisfies

\[
g x'=x+c(g)+g u=x+u=x'
\]

for the universal element. Proposition 3.2 then makes it a fixed point over \(C\). This lifts every \(\bar x\), proving formal smoothness and, with finite presentation, smoothness. The calculation uses only the universal free extensions; it does not assume that tensoring \(J\) into an arbitrary nonflat test algebra embeds it as an ideal.

Finally a tangent vector at a fixed section belongs to the fixed scheme precisely when its universal translate is itself. This is exactly invariance of the corresponding derivation. The derivation description of tangent vectors proves the last assertion, also for square-zero coefficients. \(\square\)

In particular, if a diagonalizable group acts on a smooth affine group scheme by group automorphisms, its fixed subgroup is smooth. For conjugation by a homomorphism \(D_R(M)\to H\), this is the schematic centralizer: its universal points commute with the image after every base change. This remains true when the acting group is \(\mu_p\) in characteristic \(p\).

### 3.5. Finite presentation of invariants

**Theorem 3.5. Invariant algebras over arbitrary rings.** If an \(M\)-graded \(R\)-algebra \(A\) is of finite type, then \(A_0\) is of finite type over \(R\), and each homogeneous piece \(A_m\) is a finite \(A_0\)-module. If \(A\) is finitely presented, then \(A_0\) is finitely presented. The exponent group \(M\) is arbitrary. Thus the affine quotient in Theorem 4.9 preserves both finiteness properties.

**Proof.** Replace finitely many algebra generators by their finitely many homogeneous components. This gives homogeneous generators \(a_1,\ldots,a_r\) of weights \(m_1,\ldots,m_r\), and a graded surjection

\[
P=R[x_1,\ldots,x_r]\longrightarrow A,
\qquad \deg(x_i)=m_i.
\]

Taking degree zero is exact by Theorem 3.1, so \(P_0\to A_0\) is surjective. For \(d\in M\) put

\[
E_d=\{v\in\mathbf N^r:
\textstyle\sum_i v_i m_i=d\}.
\]

We use the elementary fact that a subset of \(\mathbf N^r\) has finitely many minimal elements under coordinatewise comparison. To prove it, every infinite sequence in \(\mathbf N^r\) has two terms, in their sequence order, with the earlier term at most the later in every coordinate. For one coordinate choose an infinite nondecreasing subsequence: either a value occurs infinitely often, or successively choose strictly larger values. Repeat this extraction for finitely many coordinates. This proves the sequence assertion and rules out an infinite antichain of minimal elements. Each vector of a subset has a minimal vector below it, by searching the finite box below that vector.

Apply this fact first to \(E_0\setminus\{0\}\). Its finitely many minimal vectors generate the monoid \(E_0\): subtract a minimal vector below a nonzero vector, obtaining another vector of weight zero with smaller coordinate sum, and continue. Hence their monomials generate \(P_0\) as an \(R\)-algebra, proving finite type of \(A_0\). For any \(d\), the finitely many minimal vectors of \(E_d\) likewise generate \(P_d\) as a \(P_0\)-module, since the difference between two comparable vectors of weight \(d\) has weight zero.

Now suppose \(A\) is finitely presented. The kernel \(I\) of this finite polynomial presentation is a finitely generated ideal. This holds for any chosen finite generating set of a finitely presented algebra: compare it with one finite presentation by adjoining both sets of variables, impose their finitely many mutual expressions, and eliminate the old variables. Because \(I\) is graded, replace its generators by their homogeneous components, still a finite generating set \(f_j\), with weights \(d_j\). Extracting weight zero from an expression in these generators gives

\[
I_0=\sum_j P_{-d_j}f_j.
\]

Each coefficient module on the right is finitely generated over \(P_0\) by the preceding paragraph. Thus \(I_0\) is a finitely generated ideal of \(P_0\).

Finally \(P_0\) itself is finitely presented over \(R\). Indeed it is the monoid algebra \(R[E_0]\). The same finite monoid generators give a finite polynomial presentation of \(\mathbf Z[E_0]\) over \(\mathbf Z\). Its relation ideal is finitely generated by the Hilbert basis theorem, since the polynomial ring over \(\mathbf Z\) is Noetherian. Tensoring this presentation with \(R\) gives a finite presentation of \(R[E_0]\); the monomial basis identifies this tensor product with \(P_0\). The finite ideal \(I_0\) then presents \(A_0=P_0/I_0\) finitely over \(R\), as required. \(\square\)

## 4. Exact sequences, subgroups and smoothness

**Theorem 4.1. Contravariant exactness.** A short exact sequence of finitely generated abelian groups

\[
0\longrightarrow M'\longrightarrow M\longrightarrow M''
\longrightarrow0
\]

gives an fppf exact sequence over every scheme \(S\):

\[
1\longrightarrow D_S(M'')\longrightarrow D_S(M)
\longrightarrow D_S(M')\longrightarrow1.
\tag{9}
\]

The first map is a closed immersion, the second is faithfully flat and of finite presentation, and its kernel is \(D_S(M'')\). Over a nonempty base the converse holds as well.

**Proof.** On an affine chart, \(R[M]\to R[M'']\) is the quotient imposing \(e^{m'}=1\) for all \(m'\in M'\). It identifies \(D_S(M'')\) with the kernel of the last map in (9).

Choose representatives for the cosets of \(M'\) in \(M\). They give the decomposition

\[
R[M]=\bigoplus_{c\in M/M'}R[M']\,e^{\widetilde c}.
\]

Thus \(R[M']\to R[M]\) is free and faithfully flat. It is finitely presented: one can present the group algebra extension by finitely many generators for \(M\), their inverses, and finitely many abelian-group relations together with the finitely many identifications for generators of \(M'\). Hence the map is an fppf covering. After its base change, every point of \(D_S(M')\) lifts to \(D_S(M)\); the kernel calculation proves fppf exactness.

For the converse take a geometric fibre over the nonempty base. Faithful flatness makes the corresponding Hopf map injective. Distinct basis elements would have equal images if \(M'\to M\) were not injective, so that group map is injective. Its kernel group scheme is \(D(M/M')\) by the already-proved calculation. The anti-equivalence over the geometric field identifies the prescribed \(M''\) with this cokernel and its quotient map. This proves exactness of the original abelian-group sequence. \(\square\)

**Theorem 4.2. Subgroups and quotients over a field.** Every closed subgroup of a finite-type diagonalizable group over a field is diagonalizable. If a faithfully flat homomorphism from such a group to a finite-type group scheme is given, its target is diagonalizable.

**Proof.** Write \(G=D_k(M)\). A closed subgroup \(H\) has a Hopf quotient \(k[M]\twoheadrightarrow B\). The images of the \(e^m\) are group-like units and span \(B\). Distinct group-like elements in a coalgebra over a field are linearly independent. Here is a proof: in a minimal nonzero dependence among them, choose a linear functional taking different values on two of the elements; this is possible since distinct group-like elements cannot be scalar multiples, their counits both being \(1\). Apply that functional to one factor of the comultiplication of the dependence and subtract a scalar multiple of the original dependence to eliminate one term but retain another. This contradicts minimality.

Let \(N\) be the group of images of \(M\) in these group-like elements. Its distinct elements form a basis of \(B\); multiplication and all Hopf operations agree with those of \(k[N]\). Hence \(B=k[N]\), and \(H=D_k(N)\), where \(M\to N\) is surjective and \(N\) is finitely generated.

Put \(L=\ker(M\to N)\). Theorem 4.1 makes \(D_k(M)\to D_k(L)\) faithfully flat with kernel \(H\). It is an \(H\)-torsor: on every test scheme two lifts differ by a unique element of the kernel, giving \(G\times H\simeq G\times_{D(L)}G\). Therefore \(D_k(L)\) represents the fppf quotient \(G/H\), by the sheaf argument of the previous lesson. A faithfully flat homomorphism \(G\to Q\) to a finite-type \(k\)-group is of finite presentation: both schemes are of finite type over a field and hence Noetherian. It is therefore an fppf cover, and the same kernel identity makes \(Q\) represent the same sheaf. It is uniquely isomorphic to \(D_k(L)\). This proves the quotient assertion. \(\square\)

**Example 4.3. Why the subgroup theorem was restricted to fields.** Over the connected base \(\operatorname{Spec}\mathbf Z\), the Hopf ideal

\[
I=(2(x-1))\subset\mathbf Z[x,x^{-1}]
\]

defines a closed subgroup \(H\subset\mathbf G_m\). Indeed its counit is zero, its antipode is a unit multiple of its generator, and

\[
\Delta(2(x-1))
=2(x-1)\otimes x+1\otimes2(x-1)
\]

belongs to the required sum of ideals. Its generic fibre is trivial, whereas its characteristic-two fibre is \(\mathbf G_m\). The nonzero class of \(x-1\) in its coordinate ring is killed by \(2\); it is nonzero because reduction modulo \(2\) still gives the Laurent polynomial ring. Thus this subgroup is not flat over \(\mathbf Z\). Every \(D_{\mathbf Z}(N)\) is flat, so \(H\) is not globally diagonalizable. An unrestricted general-base subgroup statement would be false.

**Theorem 4.4. Smoothness and finite Cartier duality.** Let \(M\) be finitely generated. Then \(D_S(M)\) is smooth over \(S\) exactly when the order of \(M_{\mathrm{tors}}\) is invertible on \(S\). If \(M\) is finite, \(D_S(M)\) is finite locally free of rank \(|M|\), and

\[
D_S(M)^D\simeq M_S,
\tag{10}
\]

where \(M_S\) is the constant finite group scheme.

**Proof.** Use (5). If all the torsion orders are units, each \(\mu_{n_i}\) is finite étale by the derivative criterion from the previous lesson, and the torus factors are smooth. Their product is smooth.

Conversely suppose some prime \(p\) dividing a torsion order is not invertible at a point of \(S\). In an algebraically closed field of that residue characteristic, the corresponding equation is

\[
X^{n_i}-1=(X^{d}-1)^{p^a},\qquad
n_i=p^a d,\quad a>0,\quad p\nmid d.
\]

It has nonzero nilpotents, and tensoring with the coordinate algebras of the other nonempty factors preserves a nonzero nilpotent. The geometric fibre is not reduced and hence cannot be smooth. Smoothness of \(D_S(M)\) would make every geometric fibre smooth, giving a contradiction.

For finite \(M\), the group algebra is free of rank \(|M|\). Let \(\delta_m\) be the basis dual to \(e^m\). The dual algebra has multiplication

\[
\delta_m\delta_n=
\begin{cases}\delta_m&m=n,\\0&m\ne n,\end{cases}
\]

and unit \(\sum_m\delta_m\); it is \(\prod_{m\in M}\mathcal O_S\). Dualizing multiplication in the group algebra gives

\[
\Delta(\delta_a)=\sum_{m+n=a}\delta_m\otimes\delta_n.
\]

These are exactly the function algebra and group law of the constant group \(M_S\). The finite locally free Cartier duality proved in the first lesson gives (10), with pairing \((f,m)\mapsto f(m)\). \(\square\)

The finite-generation assumption in the smoothness criterion is essential. For example \(D_k(\bigoplus_{i\geq1}\mathbf Z)\) has torsion-free character group but is not of finite type or locally of finite presentation, so it is not a smooth group scheme.

### 4.5. Exactness without finite generation

**Theorem 4.5. Arbitrary exponent groups.** For an exact sequence of arbitrary abelian groups

\[
0\longrightarrow M'\longrightarrow M\longrightarrow M''\longrightarrow0,
\]

the transposed sequence (9) is exact as a sequence of **fpqc** sheaves. Its last map is affine and faithfully flat, its kernel is the indicated closed subgroup, and \(D_S(M')\) represents the fpqc quotient by \(D_S(M'')\). The last map is of finite presentation if \(M''\) is finitely generated. Over a nonempty base this condition is also necessary, even for finite type of that map.

**Proof.** The kernel calculation and the nonempty free basis of coset representatives in Theorem 4.1 use no finite generation. Thus the map is affine, faithfully flat and quasi-compact. Pulling it back along a test point provides an fpqc cover on which that point lifts. Two lifts differ by a unique kernel element. These two facts identify its sheaf quotient with the target, and prove exactness.

For the finite-presentation assertion choose generators of \(M''\), lift them to \(m_1,\ldots,m_r\in M\), and choose finitely many generators \(a_j=(a_{j1},\ldots,a_{jr})\) of the relation subgroup in \(\mathbf Z^r\). Put \(b_j=\sum_i a_{ji}m_i\in M'\). Then

\[
\begin{gathered}
\mathcal O_S[M]\simeq B/J,\\
B=\mathcal O_S[M'][x_1^{\pm1},\ldots,x_r^{\pm1}],\\
J=\bigl(\prod_i x_i^{a_{ji}}-e^{b_j}\bigr)_j.
\end{gathered}
\]

Indeed the presentation sends \(x_i\) to \(e^{m_i}\); its group of exponents is the quotient of \(M'\oplus\mathbf Z^r\) by the relations \((-b_j,a_j)\), which is \(M\). This proves finite presentation without requiring \(M'\) to be finitely generated. Conversely the fibre over the identity of the target is \(D_S(M'')\). Finite type of the map implies finite type of this fibre over \(S\), and Section 1 then makes \(M''\) finitely generated when \(S\) is nonempty. \(\square\)

For a general homomorphism \(u:N\to M\), the kernel of \(D_S(M)\to D_S(N)\) is \(D_S(\operatorname{coker}u)\). If \(S\ne\varnothing\), the transposed map is faithfully flat exactly when \(u\) is injective, and is a monomorphism exactly when \(u\) is surjective; in the latter case it is a closed immersion. For the first converse faithful flatness makes the group-algebra map injective, so distinct exponent basis elements cannot be identified. For the second, a monomorphism has trivial kernel, and \(D_S(L)\) is trivial only for \(L=0\), as a geometric-fibre basis comparison shows. The forward assertions follow from the free-basis and quotient calculations above.

**Proposition 4.6. Finiteness and integrality.** For a nonempty base, \(D_S(M)\) is finite if and only if \(M\) is finite, and is integral over \(S\) if and only if \(M\) is a torsion group. It is always faithfully flat.

**Proof.** A finite \(M\) gives a free coordinate module of rank \(|M|\). Conversely on a geometric fibre finiteness bounds the number of linearly independent exponent vectors, so makes \(M\) finite. The summand \(\mathcal O_S e^0\) and the free coordinate module show faithful flatness for every \(M\).

If \(M\) is torsion, each \(e^m\) satisfies a monic equation \(X^n-1=0\). Every element of the group algebra lies in the algebra generated by finitely many such integral elements, so the whole algebra is integral over the base. Conversely on a geometric fibre integrality makes every \(e^m\) algebraic over its field. An element of infinite order has linearly independent nonnegative powers \(e^{jm}\), so satisfies no nonzero polynomial. Hence every \(m\) is torsion. \(\square\)

In particular the multiplication kernel \(D_S(M)[n]=D_S(M/nM)\) is integral over \(S\), and is finite when \(M\) is finitely generated. The exactness theorem is fpqc rather than automatically fppf: for example \(D_k(\bigoplus_{i\geq1}\mathbf Z)\to\operatorname{Spec}k\) is an affine faithfully flat cover but is not locally of finite presentation.

### 4.7. Torsors are strongly graded algebras

We use right actions here. An affine action is still encoded by \(\rho(a_m)=a_m\otimes e^m\). A **strong grading** is a grading whose products satisfy \(A_mA_n=A_{m+n}\), where products mean finite sums of products of sections.

**Theorem 4.7. Diagonalizable torsors.** An fpqc torsor under \(D_S(M)\), with \(M\) arbitrary, is affine over \(S\). Its graded coordinate algebra has

\[
\begin{gathered}
\mathcal A_0=\mathcal O_S,\\
\mathcal A_m\text{ invertible},\\
\mathcal A_m\otimes\mathcal A_n\xrightarrow{\ \sim\ }\mathcal A_{m+n}.
\end{gathered}
\]

Conversely these conditions make \(\operatorname{Spec}_S\mathcal A\) an fpqc torsor. They are equivalent to \(\mathcal A_0=\mathcal O_S\) and \(\mathcal A_m\mathcal A_{-m}=\mathcal O_S\) for every \(m\); it suffices to check the latter for a generating set of \(M\).

**Proof.** A torsor is locally the affine group itself. The affine descent proved in *Quotients and torsors*, **Corollary, Affine descent**, makes it affine over \(S\). Its trivializations identify its homogeneous modules and multiplication maps with those of \(\mathcal O_S[M]\). Their invertibility, the multiplication isomorphisms and the degree-zero identity descend by faithful flatness.

For the converse the direct sum of invertible modules is flat and contains the degree-zero copy of \(\mathcal O_S\) as a direct summand, hence is faithfully flat. Its relative spectrum is affine and quasi-compact. The canonical torsor map has coordinate map

\[
\begin{gathered}
\mathcal A\otimes\mathcal A\longrightarrow
\mathcal A\otimes\mathcal O_S[M],\\
a_m\otimes b_n\longmapsto a_mb_n\otimes e^n.
\end{gathered}
\]

It sends bidegree \((m,n)\) to \((m+n,n)\). This is a bijection of bidegrees, and each component map is the assumed multiplication isomorphism. Thus \(P\times_SD_S(M)\simeq P\times_SP\). Pull back along the fpqc cover \(P\to S\); its diagonal section trivializes the torsor.

It remains to justify the equivalent criterion. On an affine chart put \(R=A_0\). If \(A_mA_{-m}=R\), write \(1=\sum_i f_i g_i\), with \(f_i\in A_m\), \(g_i\in A_{-m}\). The opens \(D(f_ig_i)\) cover \(\operatorname{Spec}R\). On each, \(f_i\) is a homogeneous unit, with inverse \(g_i/(f_ig_i)\). Multiplication by \(f_i\) identifies \(R\) with \(A_m\): dividing any degree-\(m\) element by \(f_i\) gives degree zero. Hence \(A_m\) is invertible. For any \(m,n\), choose such units locally in both degrees. Their product is a unit of degree \(m+n\), proving the multiplication isomorphism. Finally the set of degrees having a homogeneous unit locally on the base is a subgroup: inverses give negation and products give addition. If it contains a generating set, it is all of \(M\). This proves the last assertion and the strong-grading equivalence. \(\square\)

**Corollary 4.8. Line bundles and roots.** The groupoid of \(\mathbf G_m\)-torsors over \(S\) is equivalent to the groupoid of invertible modules. The algebra attached to \(\mathcal L\) is

\[
\bigoplus_{j\in\mathbf Z}\mathcal L^{\otimes j},
\qquad \mathcal L^{\otimes(-j)}=(\mathcal L^\vee)^{\otimes j}\quad(j>0).
\]

Every such torsor is Zariski locally trivial, and their group of isomorphism classes is \(\operatorname{Pic}(S)\). For \(n\geq1\), \(\mu_n\)-torsors are invertible modules \(\mathcal L\) equipped with a trivialization \(\mathcal L^{\otimes n}\simeq\mathcal O_S\). Consequently there is an exact sequence

\[
\begin{gathered}
0\longrightarrow
\Gamma(S,\mathcal O_S^\times)/\Gamma(S,\mathcal O_S^\times)^n\\
\longrightarrow H^1_{\mathrm{fppf}}(S,\mu_n)
\longrightarrow\operatorname{Pic}(S)[n]\longrightarrow0.
\end{gathered}
\]

No invertibility assumption on \(n\) is needed.

**Proof.** For the \(\mathbf Z\)-grading, all homogeneous modules and their multiplication are determined by \(\mathcal A_1\) and its tensor powers, by Theorem 4.7. Conversely tensor powers construct the graded algebra, with its canonical associative multiplication. A local basis of \(\mathcal L\) identifies it with \(\mathcal O_S[t,t^{-1}]\), proving Zariski local triviality. Tensor product of line bundles corresponds to the contracted product of torsors: in two local trivializations both transition units multiply. This identifies the group of classes with \(\operatorname{Pic}(S)\).

For the \(\mathbf Z/n\)-grading take \(\mathcal L=\mathcal A_1\). Repeated multiplication gives the stated trivialization. Conversely form \(\bigoplus_{i=0}^{n-1}\mathcal L^{\otimes i}\), using the trivialization when a degree crosses \(n\). Locally it is \(R[t]/(t^n-u)\), with \(u\) a unit. This verifies associativity, strong grading and the torsor assertion. This algebra is finite free of rank \(n\), so these torsors are fppf torsors, even when \(\mu_n\) is not smooth.

Forgetting the trivialization maps classes onto \(\operatorname{Pic}(S)[n]\). In its kernel \(\mathcal L\simeq\mathcal O_S\); a trivialization is specified by a global unit \(u\). Changing the basis multiplies \(u\) by an \(n\)-th power. This identifies the kernel exactly as displayed, including injectivity of its first map. The tensor product of the pairs gives the group law and makes both maps homomorphisms. \(\square\)

### 4.9. Free affine actions have effective quotients

**Theorem 4.9. Free diagonalizable quotients.** Let \(D_S(M)\), with \(M\) arbitrary, act schematically freely on an affine \(S\)-scheme \(P=\operatorname{Spec}_S\mathcal A\). Then

\[
X=P/D_S(M)=\operatorname{Spec}_S\mathcal A_0
\]

represents the fpqc sheaf quotient, and \(P\to X\) is a torsor under \(D_X(M)\). In particular the action graph \(P\times_SD_S(M)\to P\times_SP\) is a closed immersion, although freeness initially requires only a monomorphism. If \(H/S\) is an affine group and \(D_S(M)\to H\) is a monomorphism, it is a closed immersion, and the right-coset quotient \(H/D_S(M)\) is affine over \(S\).

**Proof.** Formation of degree zero and of all weight modules commutes with scalar extension by Theorem 3.1. The map to \(X=\operatorname{Spec}_S\mathcal A_0\) is invariant. We may work over an affine chart of \(S\), then regard \(P\) as an affine \(X\)-scheme. Write \(A=\bigoplus_{m\in M}A_m\) and \(B=A_0\). By Theorem 4.7 it suffices to show

\[
J_m=A_mA_{-m}=B\qquad(m\in M).
\tag{11}
\]

Here the action over \(X\) is still free: equality of two action-graph points over \(X\) also gives equality over \(S\). Freeness is preserved by every base change. Reduce along each maximal ideal of \(B\). The degree-zero part becomes its residue field \(k\). Proving (11) there proves it over \(B\), since a proper ideal is contained in a maximal ideal. We therefore assume \(B=k\).

We spell out how freeness constrains the weights. Write \(e^{r,s}\) for the group-algebra basis of \(A[M\oplus M]\), and put \(d_p=e^{p,0}-e^{0,p}\). The fibre product of two copies of the action graph has coordinate algebra

\[
A[M\oplus M]/K,\qquad
K=(a_p d_p:p\in M,\ a_p\in A_p).
\]

Indeed equality of the two graph images equates their first point and then equates \(a_p e^{p,0}\) with \(a_p e^{0,p}\) for every homogeneous function. The graph is a monomorphism precisely when its diagonal is an isomorphism. On these algebras that diagonal sends \(e^{r,s}\) to \(e^{r+s}\), whose kernel before quotienting is \(K'=(d_p:p\in M)\). Thus freeness says \(K=K'\).

For every \(m\) we can consequently express \(d_m\) as a finite sum of polynomial multiples of \(a_p d_p\). Extract degree zero in the **coefficient algebra** \(A\). The coefficient multiplying \(a_p\) must have weight \(-p\), so this gives an identity in \(k[M\oplus M]\) of the form

\[
d_m=\sum_{p,r,s}\lambda_{p,r,s} e^{r,s}d_p,
\qquad \lambda_{p,r,s}\in J_p.
\]

Each \(J_p\) is either \(0\) or \(k\). Moreover \(J_p=J_{-p}\) and \(J_pJ_q\subset J_{p+q}\), by commutativity and the grading. Therefore \(N=\{p:J_p=k\}\) is a subgroup of \(M\). The last identity places every \(d_m\) in the ideal generated by the \(d_p\) with \(p\in N\). Its quotient is the group algebra

\[
k\bigl[(M\oplus M)/\{(p,-p):p\in N\}\bigr].
\]

In that group the two exponents \((m,0)\) and \((0,m)\) are equal exactly when \(m\in N\). Distinct exponent vectors are linearly independent over \(k\); hence \(d_m\) cannot vanish for \(m\notin N\). It follows that \(N=M\), proving (11) over each residue field and thus over \(B\).

Theorem 4.7 now makes \(P\to X\) a torsor. Its canonical fibre-product identity and fpqc local sections identify \(X\) with the sheaf quotient. As \(X/S\) is affine, its diagonal is closed; consequently \(P\times_XP\) is closed in \(P\times_SP\). This proves the graph assertion. Finally right translation through a monomorphism into \(H\) is free on every test scheme. Apply the theorem with \(P=H\). Restrict its closed action graph to the identity in the first coordinate; this gives the closed immersion \(D_S(M)\to H\). The quotient assertion follows at the same time. \(\square\)

The distinction between fixed points and the affine quotient in Proposition 3.2 remains essential. The quotient in this theorem is a torsor because the action is free. For the scaling action on an entire affine line, its origin is a fixed point and the invariant quotient is not a torsor.

### 4.10. Equations for universal equalities

A morphism \(Z\to S\) is **essentially free** if, locally on \(S\), an affine faithfully flat cover makes \(Z\) admit an affine open cover whose coordinate modules are free over the base. Diagonalizable groups have this property, since their coordinate modules have the exponent basis. Any scheme over a field has it. It is preserved by base change and descends fpqc locally directly from this definition, by composing the covers.

**Theorem 4.10. Closed equality loci.** Let \(Z\to S\) be essentially free and \(Y\hookrightarrow Z\) a closed immersion. The functor of \(S\)-schemes \(T\) for which \(Y_T=Z_T\) is represented by a closed subscheme of \(S\). The result remains true if the free modules in the definition are replaced by projective modules, or by modules \(E\) with the following property: for every finite subset of \(E\), some finite family \(x_i\in E\), \(f_i\in E^\vee\) reconstructs all its elements by \(v=\sum_i f_i(v)x_i\).

**Proof.** Suppose first that \(S=\operatorname{Spec}R\), \(Z=\operatorname{Spec}B\), and \(B\) is free over \(R\), with basis \(b_i\). Let \(I\subset B\) define \(Y\). Generate an ideal \(J\subset R\) by all coefficients of all elements of \(I\) in that basis. For an arbitrary \(R\)-algebra \(C\), the image of \(I\) in \(B\otimes_RC\) is zero exactly when all these coefficients vanish in \(C\). This is equivalent to factoring \(R\to C\) through \(R/J\), and exactly expresses \(Y_C=Z_C\). Neither flatness of \(C\) nor finite generation of \(I\) is used.

In the more general module case take \(J\) generated by \(f(v)\) for every \(v\in I\) and \(f\in B^\vee\). If \(v\otimes1=0\), applying each extended functional makes these coefficients zero. Conversely reconstruct \(v\) by a finite family as in the hypothesis; if the coefficients vanish, so does \(v\otimes1\). This gives the same representing closed subscheme. A projective module is a summand of a free module. Include a finite subset into that free module, use its finitely many nonzero basis coordinates, and project the basis vectors back to the summand. The resulting vectors and coordinate functionals give precisely the required reconstruction property.

For an affine open cover of \(Z\), sum the coefficient ideals from its members: equality on all charts is the simultaneous vanishing of those ideals. On a cover of \(S\) the resulting closed subschemes agree by their functors and glue. Finally after an affine faithfully flat cover of \(S\), equality of the two schemes is fpqc local, and the constructed closed subscheme has a unique descent datum. Closed immersions descend by the module and affine descent in *Quotients and torsors*: descend the ideal as a submodule of the base algebra and its inclusion, then take its quotient. This proves representability before that cover as well. \(\square\)

**Corollary 4.11. Fixed schemes, transporters and normalizers.** If an essentially free group \(G/S\) acts on a separated \(S\)-scheme \(X\), its fixed-point functor is a closed subscheme of \(X\), with formation commuting with every base change. If \(Y\subset X\) is essentially free and \(Z\subset X\) is closed, the transporter of \(Y\) into \(Z\) is a closed subscheme of \(G\). If both \(Y,Z\) are closed and essentially free, the strict transporter, requiring \(gY_T=Z_T\), is closed as well. In particular the normalizer of an essentially free closed subgroup is closed; the centralizer of an essentially free subscheme of a separated group is closed. The centre of an essentially free separated group is closed.

**Proof.** Over the parameter scheme \(X\), compare the action and projection maps \(G\times_SX\rightrightarrows X\). Their equalizer is closed by separatedness. Theorem 4.10, applied to the essentially free projection \(G\times_SX\to X\), represents the parameters for which those maps agree universally, namely fixed points. The defining universal functor also proves arbitrary base-change compatibility.

For a transporter pull back \(Z\) along \(G\times_SY\to X\). The condition that this closed subscheme be all of \(G\times_SY\) is represented by Theorem 4.10 over \(G\). For strict transport intersect this locus with the inverse image, under inversion on \(G\), of the transporter of \(Z\) into \(Y\); the two inclusions are equivalent to equality of the subschemes. Apply this to conjugation to obtain the normalizer. For a centralizer compare the two maps \(G\times_SY\rightrightarrows G\), \((g,y)\mapsto gy\) and \((g,y)\mapsto yg\), using the closed diagonal of the group and Theorem 4.10. Taking \(Y=G\) gives the centre. The functor identities also prove the asserted subgroup structures. \(\square\)

This extends the affine fixed-scheme construction of Proposition 3.2 to separated schemes. It does not assert smoothness for every such fixed scheme; the smoothness theorem proved above retains its stated affine hypotheses.

**Example 4.12. A flat monomorphism need not be closed.** Let \(S=\operatorname{Spec}k[t]\), \(U=D(t)\), and \(H=(\mathbf Z/2)_S=S\amalg S\). Keep all of its identity component and only \(U\) in its other component. The resulting open subgroup \(G=S\amalg U\to H\) is a monomorphism of smooth, separated, finitely presented \(S\)-groups, with \(G\) faithfully flat over \(S\). It is not closed: in the nonidentity component its image is the proper dense open \(U\). Its generic fibre has two elements and its fibre at \(t=0\) has one. To check the group law, multiply two nonidentity sections over \(U\) into the identity, and restrict all other products to their evident open components; inversion preserves both pieces. These maps inherit all identities from \(H\).

Thus the closed-immersion conclusion in Theorem 4.9 uses the globally diagonalizable source in an essential way. Even in characteristic zero, where the displayed example still works, flatness and finite presentation alone do not make a group monomorphism closed.

**Proposition 4.13. The real norm-one torus has two torsor classes.** Put \(T=\ker(N:\operatorname{Res}_{\mathbf C/\mathbf R}\mathbf G_m\to\mathbf G_m)\). Its fppf torsors are the norm fibres \(P_a\), \(a\in\mathbf R^\times\), and

\[
H^1_{\mathrm{fppf}}(\mathbf R,T)
=\mathbf R^\times/N(\mathbf C^\times)
=\{+1,-1\}.
\]

The torsor \(P_{-1}\), given by \(x^2+y^2=-1\), becomes trivial over \(\mathbf C\) and has no real point. Thus a nonsplit form of \(\mathbf G_m\) need not share the Zariski local triviality of \(\mathbf G_m\)-torsors.

**Proof.** Over \(\mathbf C\), restriction of scalars becomes \(\mathbf G_m^2\), with norm \((z,w)\mapsto zw\), and \(T\) becomes its kernel \((t,t^{-1})\). Each fibre of the norm is a torsor, since over a cover it has a point and the ratio of two such points is a unique kernel element. The fibre has a point after extension to \(\mathbf C\), so this applies to every \(a\).

Conversely let \(P\) be a \(T\)-torsor. Choose an affine fppf cover \(\operatorname{Spec}B\to\operatorname{Spec}\mathbf R\) trivializing it. Its transition functions \(t_{ij}\) lie in \((\mathbf C\otimes_{\mathbf R}(B\otimes_{\mathbf R}B))^\times\) and have norm one. Regard them as descent data for a free rank-one module over \(\mathbf C\otimes B\). The module descent in *Quotients and torsors*, **Lemma, Module descent**, descends that module to a complex vector space of dimension one. Choose a complex basis. Comparing it with the trivializations provides a unit \(h\in(\mathbf C\otimes B)^\times\) whose two pullbacks satisfy \(h_j=h_it_{ij}\).

Taking norms shows that the two pullbacks of \(N(h)\in B^\times\) agree. The faithfully flat equalizer descends it to a unit \(a\in\mathbf R^\times\). Mapping the local torsor section to \(h\) now identifies \(P\) with \(P_a\): the transition rule is the same, and both are torsors with the same chosen local section. Changing the complex basis multiplies \(a\) by a complex norm. Conversely multiplication by \(z\in\mathbf C^\times\) identifies \(P_a\) with \(P_{aN(z)}\). Tensoring the descent data multiplies the norms, so this classification is an isomorphism of the groups of torsor classes. Complex norms are exactly the positive real numbers; the two classes and the asserted nontrivial example follow. \(\square\)

**Lemma 4.14. Flat schemes over an Artinian base are essentially free.** Over an Artinian scheme, a morphism is essentially free if and only if it is flat.

**Proof.** The forward implication follows by descent of flatness from the free coordinate modules. For the converse work on the finitely many open and closed spectra of local Artinian rings. Let \((R,\mathfrak m)\) be such a ring, \(k=R/\mathfrak m\), and \(E\) any flat \(R\)-module. Lift a \(k\)-basis of \(E/\mathfrak mE\) to obtain a map \(F=R^{(I)}\to E\). Its cokernel \(Q\) satisfies \(Q=\mathfrak mQ\), hence \(Q=0\) because \(\mathfrak m\) is nilpotent. If \(K\) is the kernel, flatness of \(E\) makes \(K\otimes_Rk\to F\otimes_Rk\) injective. The basis choice makes the subsequent map to \(E\otimes_Rk\) an isomorphism, so \(K/\mathfrak mK=0\). Nilpotence again gives \(K=0\). Thus \(E\) is free, with no finiteness restriction. Apply this to every affine chart of a flat scheme. It gives the essentially free presentation using the identity cover of each local base. \(\square\)

**Lemma 4.15. Flat closure over a discrete valuation ring.** Let \(R\) be a DVR, with fraction field \(K\), and \(L_K\hookrightarrow H_K\) a closed subscheme of the generic fibre of an arbitrary \(R\)-scheme \(H\). Its schematic closure \(L\hookrightarrow H\) exists and is the unique closed flat \(R\)-subscheme with that generic fibre. Closure commutes with products over \(R\). A morphism of ambient schemes carrying one specified generic subscheme into another carries their closures into each other. If \(H\) is a group scheme and \(L_K\) a subgroup, its closure is a flat closed subgroup scheme.

**Proof.** On an affine chart \(\operatorname{Spec}B\subset H\), let \(J\subset B\otimes_RK\) define the generic subscheme and take its inverse image \(I\subset B\). These ideals agree under localization and glue to a quasi-coherent ideal. The algebra \(B/I\) embeds into \((B\otimes_RK)/J\), so is torsion free over the DVR and therefore flat. Its generic fibre is the given quotient. Conversely any flat quotient of \(B\) with this generic fibre is torsion free and consequently has ideal exactly the inverse image of \(J\). This proves existence and uniqueness. A product of two such closed flat models is flat and has the required product generic fibre, so uniqueness proves the product assertion. For a morphism between ambient schemes, functions vanishing on the target closure pull back to functions on the source closure which vanish on its generic fibre. Flatness makes that fibre schematically dense: on affine charts a function zero after inverting a uniformizer is zero in the torsion-free coordinate module. Thus the morphism factors through the target closure. Apply this to multiplication, using the product assertion, and to inversion and the identity section, whose source is flat. They all factor through the closure and inherit the group identities from \(H\). \(\square\)

## 5. Galois descent of characters

Fix a field \(k\), a separable closure \(k_s\), and \(\Gamma=\operatorname{Gal}(k_s/k)\) with its profinite topology. A finite-type \(k\)-group \(G\) is **of multiplicative type** if \(G_{k_s}\) is diagonalizable. Write

\[
X(G)=\operatorname{Hom}_{k_s\text{-groups}}(G_{k_s},\mathbf G_{m,k_s}).
\tag{11}
\]

It is a finitely generated abelian group. Its Galois action transports both coefficients and arguments: \(\sigma\chi=\sigma\circ\chi\circ\sigma^{-1}\). Characters defined over \(k\) are exactly \(X(G)^\Gamma\), by descent.

The usual alternative definition asks that \(G\) become diagonalizable over some field extension, or over an algebraic closure. The next proof shows that these definitions agree, including over imperfect fields. It precedes the Galois classification and does not use that classification.

**Theorem 5.0. Separable splitting.** If a finite-type group scheme \(G/k\) becomes diagonalizable over a field extension \(K/k\), then \(G_{k_s}\) is diagonalizable. Consequently all three definitions above are equivalent.

**Proof.** Affine descent, proved at the start of *Quotients and torsors*, makes \(G\) affine; write its Hopf algebra as \(A\). Choose an algebraically closed common overfield \(\Omega\) of \(K\) and \(k_s\), and fix \(A_\Omega\simeq\Omega[M]\). Such an overfield exists by taking a residue field of a prime of \(K\otimes_k k_s\) and then an algebraic closure. We will descend its individual group-like elements without descending a choice of generators for \(M\).

Every finite subset of a coalgebra over a field lies in a finite-dimensional subcoalgebra. Here is the needed deduction from *Group schemes, actions and Hopf algebras*, Lemma 5.1. Apply that lemma to the regular comodule to find a finite-dimensional subcomodule \(W\subset A\) containing the subset. For a basis \(w_j\), write \(\Delta(w_j)=\sum_i w_i\otimes a_{ij}\). Coassociativity and counitality give

\[
\Delta(a_{ij})=\sum_\ell a_{i\ell}\otimes a_{\ell j},
\qquad w_j=\sum_i\epsilon(w_i)a_{ij}.
\]

Thus the finite-dimensional span \(V\) of all \(a_{ij}\) is a subcoalgebra containing \(W\). In particular the subcoalgebras \(V\) cover \(A\).

For each such \(V\), the equations

\[
c\in V\otimes_k R,\qquad \Delta(c)=c\otimes c,\qquad\epsilon(c)=1
\]

define an affine scheme \(C_V\) of finite type over \(k\): in a basis of \(V\) they are finitely many quadratic equations and one linear equation. This scheme parametrizes group-like elements in \(V\) on every \(k\)-algebra \(R\), and its equations commute with scalar extension.

The subcoalgebra \(V_\Omega\subset\Omega[M]\) is spanned by a finite set \(F\) of the monomials \(e^m\). Indeed, if \(v=\sum c_m e^m\) belongs to it, apply to the second factor of \(\Delta(v)\in V_\Omega\otimes V_\Omega\) the linear functional extracting the coefficient of \(e^m\). The result \(c_m e^m\) lies in \(V_\Omega\), so every nonzero coefficient puts that monomial in \(V_\Omega\). Finite dimensionality then makes \(F\) finite. Lemma 2.1, now applied over every \(\Omega\)-algebra, identifies

\[
(C_V)_\Omega\simeq\coprod_{m\in F}\operatorname{Spec}\Omega.
\]

Therefore \(C_V\) is finite étale over \(k\). For clarity, this descent conclusion can be checked directly on its coordinate algebra \(E\). The algebra \(E\otimes_k\Omega\simeq\Omega^F\) is finite dimensional, so \(E\) is finite dimensional: any larger linearly independent family would remain independent after scalar extension. It is reduced by injectivity into that scalar extension. A finite reduced algebra is a product of finite field extensions, by the Artinian decomposition and the Chinese remainder theorem. Each extension is separable, since an inseparable irreducible polynomial acquires repeated roots over \(\Omega\) and would produce a nonzero nilpotent in its scalar extension. Thus \(E\) is a product of finite separable extensions, which is exactly a finite étale algebra over \(k\).

Over the separably closed field \(k_s\), every finite étale algebra is a finite product of copies of \(k_s\). Consequently every \(\Omega\)-point of \(C_V\), and hence every group-like element of \(A_\Omega\) lying in \(V_\Omega\), is the scalar extension of a unique group-like element of \(A_{k_s}\). Every monomial \(e^m\) lies in some \(V_\Omega\): its finite coefficient expression uses finitely many elements of \(A\), which lie in a subcoalgebra \(V\) as above.

Let \(N\) be the group of group-like elements of \(A_{k_s}\). Scalar extension gives a bijection \(N\to M\), compatible with products and inverses. The natural Hopf map \(k_s[N]\to A_{k_s}\) becomes the basis isomorphism \(\Omega[M]\to A_\Omega\). Faithful scalar extension detects its kernel and cokernel, so the original map is an isomorphism. Thus \(G_{k_s}=D_{k_s}(N)\), as required. The implication in the other direction is immediate by choosing \(K=k_s\), and extension from \(k_s\) to an algebraic closure preserves diagonalizability. \(\square\)

*Comparison and credit:* Milne, Chapter 12f, Theorem 12.18 and Corollary 12.19 give the same separable-splitting result. The proof here uses the preceding lessons' local-finiteness and affine-descent proofs together with the explicit group-like equations, so it also explains why purely inseparable scalar extension supplies no missing character.

**Lemma 5.1. A finite splitting field.** A finite-type group of multiplicative type is affine, splits over a finite Galois extension \(K/k\), and its character action is continuous for the discrete topology on \(X(G)\). Conversely every continuous \(\Gamma\)-action on a finitely generated abelian group factors through a finite Galois quotient.

**Proof.** Affineness descends along \(\operatorname{Spec}k_s\to\operatorname{Spec}k\), since \(G_{k_s}\) is affine. Let \(B\) be the resulting finitely generated coordinate algebra. An isomorphism \(k_s\otimes_kB\simeq k_s[M]\) and its inverse are determined by finitely many algebra generators and their finite expressions. They therefore descend to some finite subextension of \(k_s/k\); their relations and inverse identities hold there because they hold after faithfully flat extension to \(k_s\). Enlarge that field to a finite Galois \(K\).

All characters of the split \(G_K\) are defined over \(K\), by Theorem 2.2. Thus \(\operatorname{Gal}(k_s/K)\) fixes the entire character group, proving continuity. In the converse direction, choose a finite generating set of \(M\). The intersection of its open stabilizers is open and acts trivially on \(M\). The kernel of the action is therefore an open normal subgroup, corresponding to a finite Galois extension. \(\square\)

<a id="gs05-independent-field-automorphisms"></a>

**Lemma 5.1a. Independence of field automorphisms.** Distinct field automorphisms \(\sigma_1,\ldots,\sigma_s:K\to K\) are linearly independent over \(K\) as functions.

**Proof.** Suppose \(\sum_i c_i\sigma_i(x)=0\) for every \(x\in K\), with not all \(c_i\) zero. Among such relations choose one with the fewest nonzero coefficients, discard the zero terms, and divide by its first coefficient to make \(c_1=1\). A one-term relation is impossible at \(x=1\). Choose a remaining \(\sigma_j\ne\sigma_1\) and \(b\in K\) with \(\sigma_j(b)\ne\sigma_1(b)\). Subtract \(\sigma_1(b)\) times the relation at \(x\) from the relation at \(bx\). The first coefficient vanishes, while the \(j\)-th is nonzero. This is a shorter nonzero relation, a contradiction. \(\square\)

<a id="gs05-finite-galois-semilinear-descent"></a>

**Lemma 5.1b. Finite Galois descent, without a dimension bound.** Let \(K/k\) be a finite Galois extension with group \(\Delta\). Let \(V\) be any \(K\)-vector space, equipped with additive bijections \(\sigma_V:V\to V\) satisfying the group law and

\[
\sigma_V(av)=\sigma(a)\sigma_V(v)
\qquad(a\in K, v\in V, \sigma\in\Delta).
\]

Then the natural \(K\)-linear, \(\Delta\)-equivariant map

\[
\alpha_V:K\otimes_k V^\Delta\longrightarrow V,
\qquad a\otimes v\longmapsto av,
\tag{G1}
\]

is an isomorphism, where the action on its source is \(\sigma(a\otimes v)=\sigma(a)\otimes v\). Restriction to invariants gives a bijection from equivariant \(K\)-linear maps \(V\to W\) to \(k\)-linear maps \(V^\Delta\to W^\Delta\). Moreover the canonical map

\[
V^\Delta\otimes_kW^\Delta\longrightarrow(V\otimes_KW)^\Delta,
\qquad v\otimes w\longmapsto v\otimes w,
\tag{G2}
\]

is an isomorphism, for the diagonal semilinear action on the target.

**Proof.** The elementary finite Galois facts used here are \(|\Delta|=[K:k]\) and \(K^\Delta=k\). They can be checked directly in this setting. A finite separable extension has exactly its degree many embeddings into an algebraic closure: adjoin finitely many generators in a tower, and extend each embedding by each distinct root of the next minimal polynomial. Normality makes all these embeddings automorphisms of \(K\), giving the first equality. Put \(F=K^\Delta\). The vectors

\[
(\sigma(b))_{\sigma\in\Delta}\in\prod_{\sigma\in\Delta}K,
\qquad b\in K,
\]

span that finite-dimensional \(K\)-space by Lemma 5.1a: a proper span would have a nonzero linear functional annihilating it, contradicting the independence of the automorphisms. These vectors are already spanned by the images of an \(F\)-basis of \(K\), since every \(\sigma\) fixes \(F\). Thus \(|\Delta|\leq[K:F]\). Together with the degree tower \([K:k]=[K:F][F:k]\) and \(|\Delta|=[K:k]\), this forces \(F=k\).

The same spanning assertion expresses the vector with value \(1\) at the identity and \(0\) at all other automorphisms as a finite linear combination. There are therefore finite lists \(a_i,b_i\in K\) with

\[
\sum_i a_i\sigma(b_i)=
\begin{cases}
1,&\sigma=1,\\
0,&\sigma\ne1.
\end{cases}
\tag{G3}
\]

For \(v\in V\), put

\[
w_i=\sum_{\sigma\in\Delta}\sigma_V(b_iv).
\]

The group action permutes the terms, so \(w_i\in V^\Delta\). Semilinearity and (G3) give

\[
\sum_i a_iw_i
=\sum_{\sigma\in\Delta}\left(\sum_i a_i\sigma(b_i)\right)\sigma_V(v)
=v.
\]

This proves surjectivity of (G1) for every vector, irrespective of the dimension of \(V\).

A finite family of invariant vectors independent over \(k\) is independent over \(K\). Indeed, choose a shortest contrary relation \(\sum_j c_jv_j=0\), normalize \(c_1=1\), and apply any \(\sigma\in\Delta\). Subtraction gives a relation with first coefficient zero. Minimality forces \(\sigma(c_j)=c_j\) for every \(j\), so all the coefficients belong to \(K^\Delta=k\), contradicting the original independence. A \(k\)-basis of \(V^\Delta\) consequently remains independent over \(K\). This proves injectivity of (G1). Its equivariance follows directly from the displayed source action and semilinearity.

An equivariant \(K\)-linear map takes invariants to invariants and is recovered from its restriction by (G1). Conversely, scalar extension of any \(k\)-linear map between the invariant spaces, conjugated by the isomorphisms \(\alpha\), is equivariant and has that restriction. This proves the assertion about maps, including uniqueness.

For an arbitrary \(k\)-vector space \(U\), the invariants in \(K\otimes_kU\) under the scalar action are exactly \(1\otimes U\). To check this, express a tensor using a finite independent family in \(U\). Invariance makes each coefficient fixed by \(\Delta\), hence in \(k\). Now (G1) for \(V,W\) identifies

\[
V\otimes_KW\simeq K\otimes_k(V^\Delta\otimes_kW^\Delta),
\]

with their specified semilinear actions. Taking invariants by the just-proved assertion gives exactly (G2), proving it is the claimed canonical map. \(\square\)

No division by \(|\Delta|\) occurs. The argument applies when the characteristic divides the extension degree.

<a id="gs05-hopf-galois-descent"></a>

**Corollary 5.1c. Descent of Hopf operations and finite type.** Let \(A\) be a commutative Hopf \(K\)-algebra, with a semilinear action of \(\Delta\) by Hopf algebra automorphisms. Then \(B=A^\Delta\) has a unique \(k\)-Hopf algebra structure for which

\[
\alpha_A:K\otimes_kB\xrightarrow{\sim}A
\]

is a Hopf algebra isomorphism. Equivariant Hopf \(K\)-algebra maps descend uniquely to Hopf \(k\)-algebra maps. If \(A\) is finitely generated over \(K\), then \(B\) is finitely generated over \(k\), and therefore finitely presented over \(k\).

**Proof.** The unit \(K\to A\), multiplication \(A\otimes_KA\to A\), comultiplication \(A\to A\otimes_KA\), counit \(A\to K\), and antipode \(A\to A\) are equivariant \(K\)-linear maps with the indicated semilinear source and target actions. Lemma 5.1b and its canonical tensor isomorphism (G2) descend them respectively to

\[
k\to B,\quad B\otimes_kB\to B,\quad
B\to B\otimes_kB,\quad B\to k,\quad B\to B.
\]

For example, the comultiplication of an invariant element of \(A\) lies in \((A\otimes_KA)^\Delta\), which (G2) identifies canonically with \(B\otimes_kB\). The multiplication is the original multiplication restricted to the invariant subalgebra. All the algebra and Hopf identities hold: after tensoring each typed identity with \(K\), it becomes the corresponding identity in \(A\); scalar extension by a nonzero field detects equality of \(k\)-linear maps. The same reasoning descends a Hopf map and checks its structure compatibilities, and Lemma 5.1b gives uniqueness.

Suppose \(x_1,\ldots,x_t\) generate \(A\) over \(K\). Surjectivity of \(\alpha_A\) expresses each \(x_j\) as a finite \(K\)-linear combination of elements of \(B\). Let \(B_0\subseteq B\) be the \(k\)-subalgebra generated by the finitely many invariant elements appearing in these expressions. The map \(K\otimes_kB_0\to A\) contains the \(x_j\) in its image, so it is surjective. It is injective because \(B_0\subseteq B\), field extension is flat, and \(\alpha_A\) is an isomorphism. It follows that \(K\otimes_k(B/B_0)=0\). A nonzero \(k\)-vector space remains nonzero after extension to \(K\), so \(B=B_0\). Finally the Hilbert basis theorem, [*Noetherian and Artinian rings*, Theorem 2.1](../../AG-CA/src/noetherian-and-artinian-rings.md#2-polynomial-rings-and-finite-geometric-descriptions), makes the ideal of relations in a finite polynomial presentation finitely generated. Hence \(B\) is finitely presented. \(\square\)

For the actual use in Theorem 5.2, the action \(\sigma(ae^m)=\sigma(a)e^{\sigma m}\) respects each Hopf map because \(\sigma\) is an automorphism of the exponent group: it preserves \(m+n\), \(0\), and \(-m\), and sends \(e^m\otimes e^m\) to \(e^{\sigma m}\otimes e^{\sigma m}\). Thus Corollary 5.1c applies to \(A=K[M]\). A homomorphism of exponent groups commuting with \(\Delta\) induces an equivariant Hopf map and hence its unique descended map. The existing group-like coefficient calculation in Lemma 2.1 and Theorem 2.2 then identifies the geometric character group with \(M\), with exactly its given action. These are the precise structures required in the classification proof.

**Theorem 5.2. Multiplicative type and Galois modules.** The functor \(G\mapsto X(G)\) is an anti-equivalence between finite-type groups of multiplicative type over \(k\) and finitely generated abelian groups with continuous \(\Gamma\)-action. It takes fppf short exact sequences to short exact sequences in the reverse order, and conversely. Tori correspond precisely to free lattices of finite rank.

**Proof.** Let \(M\) have a continuous action, and choose \(K/k\) as in Lemma 5.1, with \(\Delta=\operatorname{Gal}(K/k)\). On \(K[M]\) define a semilinear action

\[
\sigma(ae^m)=\sigma(a)e^{\sigma m}.
\tag{12}
\]

It respects multiplication and all the Hopf operations (1). [Corollary5.1c](#gs05-hopf-galois-descent), including its arbitrary-vector-space and tensor descent proof, gives a \(k\)-Hopf algebra

\[
B=(K[M])^\Delta,\qquad K\otimes_kB\simeq K[M].
\tag{13}
\]

For example, the comultiplication descends because the descended tensor product \(B\otimes_kB\) becomes \(K[M]\otimes_KK[M]\); the latter map is semilinearly equivariant. The identities among the descended maps can be checked after the faithfully flat extension \(K/k\). Finite presentation of the algebra descends as well. Thus \(\operatorname{Spec}B\) is a finite-type group of multiplicative type.

An equivariant homomorphism \(N\to M\) induces \(K[N]\to K[M]\), \(e^n\mapsto e^{f(n)}\), commuting with (12), and hence descends to a group homomorphism in the reverse direction. Its geometric characters are exactly \(M\), with precisely the prescribed action: scalar extension in (13) identifies them, and semilinear transport of \(e^m\) gives \(e^{\sigma m}\). Thus this construction recovers every Galois module.

Conversely, for \(G\), choose a finite splitting \(K\). The canonical scalar action on \(K\otimes_k\mathcal O(G)\) sends the group-like element of a character \(m\) to that of \(\sigma m\). Theorem 2.2 consequently identifies this Hopf algebra with \(K[X(G)]\), with action (12). Taking descent recovers \(\mathcal O(G)\). A group homomorphism is, after common splitting, exactly its character homomorphism by Theorem 2.2. It descends over \(k\) exactly when that character map is equivariant. These observations prove full faithfulness and show that both constructions are inverse.

For a short exact sequence of Galois modules, choose a common finite splitting quotient. Theorem 4.1 gives the reversed fppf sequence over \(K\). Closed immersions, faithful flatness, finite presentation and the kernel identity descend to \(k\). The converse follows by scalar extension to \(K\) and Theorem 4.1. Finally \(D_{k_s}(M)\) is \(\mathbf G_m^r\) exactly when \(M\simeq\mathbf Z^r\), proving the torus assertion. \(\square\)

The torsion subgroup \(M_{\mathrm{tors}}\) is Galois-stable. Its short exact sequence gives, for every \(G\) of multiplicative type,

\[
1\longrightarrow T\longrightarrow G\longrightarrow F\longrightarrow1,
\quad
X(T)=M/M_{\mathrm{tors}},\quad X(F)=M_{\mathrm{tors}},
\tag{14}
\]

where \(T\) is a torus and \(F\) is finite of multiplicative type. It is important to keep this order: the quotient character module defines the subgroup torus.

**Example 5.3. Characters and points of roots of unity.** The group \(\mu_n\) over \(\mathbf Q\) is already \(D_{\mathbf Q}(\mathbf Z/n)\). Its geometric character module is \(\mathbf Z/n\) with **trivial** Galois action: every character \(\zeta\mapsto\zeta^m\) is defined over \(\mathbf Q\). Its geometric points, in contrast, are the roots of unity in \(\overline{\mathbf Q}\), on which Galois acts cyclotomically. These are different objects. The character module of the constant group \((\mathbf Z/n)_{\mathbf Q}\) is the group of root-of-unity-valued characters of that abstract group and does have the cyclotomic action.

In characteristic \(p\), \(D(\mathbf Z/p)=\mu_p\) is diagonalizable but not smooth, while the constant \(\mathbf Z/p\) is finite étale and is its Cartier dual. The constant group is not of multiplicative type: over an algebraic closure a diagonalizable group of order \(p\) must be \(\mu_p\), by the finite character classification, and has just one geometric point; the constant group has \(p\).

## 6. Norms give nonsplit tori

Let \(K/k\) be finite separable of degree \(d\). The **Weil restriction** \(\operatorname{Res}_{K/k}\mathbf G_m\) has functor

\[
A\longmapsto(K\otimes_kA)^\times.
\tag{15}
\]

It is represented as follows. Choose a \(k\)-basis of \(K\), giving its elements \(d\) coordinates. Multiplication by the generic element is a \(d\times d\) matrix with linear coordinate entries. An element is a unit exactly when this matrix has invertible determinant: one direction is immediate, and the other follows from the adjugate inverse, or from applying the inverse linear map to \(1\). Thus (15) is the determinant-open subscheme of \(\mathbf A^d_k\). Multiplication is polynomial, and inversion is regular on that open by the adjugate formula.

Separable scalar extension gives

\[
K\otimes_kk_s\simeq
\prod_{\tau\in\operatorname{Emb}_k(K,k_s)}k_s,
\]

so this group becomes \(\mathbf G_m^d\). Its character lattice is

\[
\mathbf Z[\operatorname{Emb}_k(K,k_s)],
\tag{16}
\]

with the Galois permutation action on embeddings. If \(K/k\) is Galois this is the permutation lattice \(\mathbf Z[\operatorname{Gal}(K/k)]\).

The determinant of multiplication defines the norm homomorphism

\[
N:\operatorname{Res}_{K/k}\mathbf G_m\longrightarrow\mathbf G_m.
\]

After splitting, it is the product of the \(d\) coordinates. That product map is smooth and surjective: an integral change of coordinates identifies it with a projection of split tori. These properties descend to \(k\). Its kernel, the **norm-one torus** \(T_{K/k}\), has rank \(d-1\) and character lattice

\[
X(T_{K/k})
=\mathbf Z[\operatorname{Emb}_k(K,k_s)]
\,/\,\mathbf Z\left(\sum_\tau[\tau]\right).
\tag{17}
\]

This follows from Theorem 5.2: the norm character sends \(1\) to the sum of the coordinate characters, a primitive vector in the permutation lattice. The quotient by the diagonal \(\mathbf G_m\), a different torus construction, instead has the augmentation **kernel** as its character lattice. Formula (17) uses the augmentation quotient.

**Example 6.1. The real circle.** For \(\mathbf C/\mathbf R\), write \(z=a+ib\); its norm is \(a^2+b^2\). Hence

\[
T_{\mathbf C/\mathbf R}
=\operatorname{Spec}\mathbf R[a,b]/(a^2+b^2-1).
\]

The map

\[
a+ib\longmapsto
\begin{pmatrix}a&-b\\ b&a\end{pmatrix}
\]

identifies this group with \(\mathrm{SO}_{2,\mathbf R}\) on every real algebra. Indeed determinant one and the orthogonal identity imply that the inverse is the transpose; comparing it with the adjugate forces this matrix form, and the remaining equation is \(a^2+b^2=1\).

Over \(\mathbf C\) the coordinates \(z=a+ib\), \(z^{-1}=a-ib\) identify the group with \(\mathbf G_m\). Complex conjugation interchanges \(z\) and \(z^{-1}\), so its character lattice is \(\mathbf Z\) with the sign action. The torus is nonsplit by Theorem 5.2, and its real points form \(S^1\).

A torus is **anisotropic** if it has no positive-dimensional split subtorus. Let \(Y(T)=\operatorname{Hom}_{k_s}(\mathbf G_m,T_{k_s})=X(T)^\vee\) be its cocharacter lattice. Then

\[
T\text{ is anisotropic}\quad\Longleftrightarrow\quad
Y(T)^\Gamma=0.
\tag{18}
\]

To prove this, an invariant cocharacter is an equivariant map \(X(T)\to\mathbf Z\), where the target has trivial action. If it is nonzero, its image is \(d\mathbf Z\) for some \(d>0\). The equivariant surjection \(X(T)\to d\mathbf Z\) defines, by Theorem 5.2, a closed rank-one split subtorus \(D_k(d\mathbf Z)\subset T\). Conversely any positive-dimensional split subtorus has a nonzero invariant cocharacter, and its inclusion remains nonzero in \(T\).

Equivalently, \(X(T)^\Gamma=0\). To see this, let the action factor through a finite group \(\Delta\), and tensor the two dual lattices with \(\mathbf Q\). The averaging projector \(|\Delta|^{-1}\sum_{\sigma\in\Delta}\sigma\) has the same rank on a vector space and its dual. Thus their invariant dimensions agree. A nonzero rational invariant can be multiplied by an integer to lie in the lattice, giving the equivalence. The averaging here occurs in rational lattices, independently of the characteristic of \(k\). In Example 6.1 the sign lattice has no nonzero invariants, so the real circle is anisotropic.

## 7. Rigidity and forms

**Theorem 7.1. The homomorphism scheme.** For finite-type groups of multiplicative type \(G,H\) over \(k\), the functor

\[
T\longmapsto\operatorname{Hom}_{T\text{-groups}}(G_T,H_T)
\]

is represented by an étale \(k\)-scheme. It need not be quasi-compact. For a split torus of rank \(r\), its automorphism scheme is the constant scheme \(\mathrm{GL}_r(\mathbf Z)_k\).

**Proof.** Choose a finite Galois \(K/k\) splitting both groups. Put \(M=X(G)\), \(N=X(H)\), and \(L=\operatorname{Hom}(N,M)\). Over an arbitrary \(K\)-scheme \(T\), Lemma 2.1 identifies each image character locally with an exponent. Since \(N\) has finitely many generators, all their images are constant on one common neighbourhood of each point. Thus the whole homomorphism is locally one fixed element of \(L\). Conversely any such locally constant choice defines a homomorphism. This represents the split functor by the constant étale scheme \(L_K\).

The group \(\Delta=\operatorname{Gal}(K/k)\) acts on \(L\) by

\[
\sigma\cdot u=\sigma_M\circ u\circ\sigma_N^{-1}.
\tag{19}
\]

Every orbit is finite. For one representative \(u\) of each orbit let \(\Delta_u\) be its stabilizer. The scheme

\[
\coprod_{u\in L/\Delta}\operatorname{Spec}(K^{\Delta_u})
\tag{20}
\]

has scalar extension \(L_K\) with exactly this permutation descent datum. Each field extension is finite separable, so (20) is étale. Homomorphisms of schemes, and the identities asserting that they respect a group law, descend faithfully flatly. Therefore the functor it represents over \(k\) is the required homomorphism functor.

The invertible endomorphisms are a Galois-stable subset of the discrete set of endomorphisms, hence define an open and closed automorphism subscheme. For a split rank-\(r\) torus, use the covariant action on its cocharacter lattice \(\mathbf Z^r\): its automorphisms are exactly \(\mathrm{GL}_r(\mathbf Z)\), with ordinary matrix multiplication. This proves the last assertion and fixes the group-composition convention. \(\square\)

Thus a family of homomorphisms between split multiplicative groups over a connected \(k\)-scheme is constant. This includes parameter schemes with nilpotents and does not require them to be of finite type. *Comparison locator:* Milne, Chapter 12i, Lemma 12.35 and Theorem 12.36.

**Theorem 7.2. Classification of tori as forms.** Rank-\(r\) tori over \(k\) are classified by

\[
H^1\bigl(\Gamma,\mathrm{GL}_r(\mathbf Z)\bigr),
\tag{21}
\]

where the coefficient group is discrete with trivial \(\Gamma\)-action and cocycles are continuous. Equivalently this is \(H^1_{\mathrm{\acute et}}(k,\mathrm{GL}_r(\mathbf Z)_k)\). Those split by a fixed finite Galois \(K/k\) correspond to

\[
H^1\bigl(\operatorname{Gal}(K/k),\mathrm{GL}_r(\mathbf Z)\bigr).
\tag{22}
\]

**Proof.** The cocharacter version of Theorem 5.2 associates to a rank-\(r\) torus a free rank-\(r\) lattice with continuous \(\Gamma\)-action. Choose a basis. Its action is a continuous homomorphism \(\rho:\Gamma\to\mathrm{GL}_r(\mathbf Z)\); changing the basis conjugates \(\rho\). Conversely every such homomorphism makes a lattice, whose dual character lattice descends a torus by Theorem 5.2. These operations identify isomorphism classes with homomorphisms modulo conjugacy.

For trivial coefficient action a nonabelian \(1\)-cocycle is exactly a homomorphism, and coboundary equivalence is exactly conjugacy. This proves (21). The étale \(H^1\) description follows either from the torsor of bases of the cocharacter lattice or from the étale-site equivalence between locally constant sheaves over a field and continuous Galois sets: its basis sheaf is a \(\mathrm{GL}_r(\mathbf Z)\)-torsor, with cocycle \(\rho\). A torsor for this constant discrete group has a point over a finite separable extension, since an étale cover has such points; choosing it gives the same cocycle. Hence both descriptions agree.

The torus is split over \(K\) exactly when \(\operatorname{Gal}(k_s/K)\) acts trivially on its lattice. Its action then factors through the finite quotient \(\operatorname{Gal}(K/k)\), giving (22). Every torus has such a finite splitting by Lemma 5.1. \(\square\)

For rank one, \(\mathrm{GL}_1(\mathbf Z)=\{\pm1\}\). Its continuous homomorphisms correspond to quadratic étale \(k\)-algebras: the trivial action gives \(k\times k\), and a nontrivial action gives the quadratic separable fixed field of its kernel. The norm-one torus of that algebra has the corresponding rank-one sign lattice, so gives all one-dimensional tori. This statement includes characteristic two, where quadratic separable extensions are Artin–Schreier extensions rather than equations with two opposite square roots.

### 7.3. What reduction modulo a nilpotent ideal detects

**Proposition 7.3. Trivial actions are rigid.** Let \(J\subset R\) be nilpotent. A representation \(E\) of \(D_R(M)\) is trivial if and only if its reduction modulo \(J\) is trivial. The same assertion holds for an action on an affine \(R\)-scheme.

**Proof.** Theorem 3.1 decomposes \(E\) into its weight modules, and this decomposition commutes with reduction. Triviality after reduction means \(E_m/JE_m=0\) for every \(m\ne0\). Thus \(E_m=JE_m=J^2E_m=\cdots=0\), since \(J\) is nilpotent. No finite generation or form of Nakayama's lemma is needed. The converse is immediate. Apply the module result to the graded coordinate algebra of an affine scheme to prove the action assertion. \(\square\)

Equality of **two** actions does not follow from equality of their reductions. Here is an explicit distinction. Over \(R=k[\delta]/(\delta^2)\), let \(D(t)=\operatorname{diag}(t,1)\) act on \(R^2\), and change basis by \(P=1+\delta E_{12}\). The conjugate action is

\[
P D(t)P^{-1}
=\begin{pmatrix}t&\delta(1-t)\\0&1\end{pmatrix}.
\]

It reduces to \(D(t)\) modulo \(\delta\), but differs from it over \(R[t,t^{-1}]\), where \(\delta(1-t)\ne0\). These representations are isomorphic by \(P\); their actions on the fixed module are unequal. This also gives two unequal actions on the affine space with projective coordinate algebra. It corrects the assertion of equality in Gille's draft, Lemma 10.1.2(2); the assertion about isomorphism classes of projective representations is a different statement. The trivial-action result in Proposition 7.3 and the homomorphism rigidity of Theorem 7.1 remain valid.

### 7.4. Homomorphisms over a general base

**Proposition 7.4. Only the target needs finite generation.** Let \(M\) be finitely generated and \(N\) any abelian group. Over every scheme \(S\), the homomorphism functor

\[
T\longmapsto\operatorname{Hom}_{T\text{-groups}}(D_T(N),D_T(M))
\]

is represented by the constant étale \(S\)-scheme with value \(\operatorname{Hom}(M,N)\). Thus the source group need not be of finite type. If \(G,H\) are Zariski locally diagonalizable and \(H\) is of finite type, their homomorphism functor is likewise represented by an étale \(S\)-scheme, by gluing these constant schemes on open subsets of \(S\).

**Proof.** A homomorphism is determined by the images of a finite set of character generators of \(M\). By Lemma 2.1 each image is a locally constant exponent of \(N\). At each point of a test scheme choose a common neighbourhood for these finitely many choices. The relations in \(M\) hold if and only if the chosen exponents define a homomorphism \(M\to N\); they already hold when the family comes from a group homomorphism. Thus the family is locally one fixed element of \(\operatorname{Hom}(M,N)\). Conversely each such locally constant choice defines the Hopf map and glues. This is exactly the functor of the indicated disjoint union of copies of \(S\), including on non-quasi-compact test schemes. Each copy is étale, so their disjoint union is étale.

For locally diagonalizable \(G,H\), take an open cover splitting both. Their local representing schemes have unique identifications on overlaps because they represent the same functor. These identifications satisfy the cocycle identity by uniqueness; ordinary open gluing gives a scheme representing the global functor. Étaleness is local on this cover. \(\square\)

**Corollary 7.5. Kernels, images and cokernels locally on the base.** For a homomorphism \(u:G\to H\) of Zariski locally diagonalizable groups, with \(H\) of finite type, its kernel is locally diagonalizable. The fpqc quotient \(G/\ker u\) exists, is locally diagonalizable and of finite type, and its induced map to \(H\) is a closed immersion. The cokernel \(H/\operatorname{im}u\) also exists and is locally diagonalizable of finite type. If \(G\) is of finite type, so is the kernel.

**Proof.** On a splitting open neighbourhood Proposition 7.4 lets us further restrict to open pieces on which the homomorphism is given by one exponent map \(f:M\to N\), where \(H=D(M)\), \(G=D(N)\), and \(M\) is finitely generated. The kernel is \(D(\operatorname{coker}f)\). Theorem 4.5 gives

\[
G/\ker u=D(\operatorname{im}f),
\qquad H/\operatorname{im}u=D(\ker f).
\]

Both exponent groups on the right are finitely generated: one is a quotient and one a subgroup of the finitely generated abelian group \(M\). The image embedding is closed because its exponent map \(M\to\operatorname{im}f\) is surjective. If \(N\) is finitely generated then \(\operatorname{coker}f\) is as well. The local kernels and the schemes representing the two sheaf quotients agree canonically on overlaps. These isomorphisms glue them and their maps over \(S\). Closed immersions and finite type are local on the open base cover. \(\square\)

### 7.6. Effective descent for the splitting scheme

The automorphisms of a split torus form an infinite discrete scheme. Affine descent alone therefore does not justify descending its scheme of splittings. We give the additional descent argument that is needed here.

**Lemma 7.6. Descent of discrete schemes.** Let \(S'\to S\) be an fpqc cover. A descent datum on a scheme which, locally over \(S'\), is a disjoint union of copies of \(S'\) is effective. Its descended scheme is separated and étale over \(S\).

**Proof.** Work over an affine open \(S=\operatorname{Spec}R\). An fpqc cover has an affine faithfully flat refinement \(X=\operatorname{Spec}B\); it suffices to descend there, since morphisms and their identities descend uniquely. Write \(V\) for the resulting discrete \(X\)-scheme. Every quasi-compact open of \(V\) is quasi-affine: it meets only finitely many of its copies of the affine scheme \(X\). In particular \(V\) is quasi-separated. The descent isomorphism defines an equivalence-relation groupoid on \(V\), with flat quasi-compact source and target maps \(s,t\colon Q\rightrightarrows V\), obtained from the two projections of \(X\times_SX\).

We first construct invariant open neighbourhoods. For a quasi-compact open \(U\subset V\), its saturation \(E_0=t(s^{-1}U)\) is quasi-compact and stable under generalization. Saturation is invariant because arrows compose and invert; stability under generalization follows from going down for the flat map \(t\). In a spectral space a quasi-compact set stable under generalization is an intersection of quasi-compact opens. Indeed, for a point outside it, the closure of that point misses the set; a finite collection of basic opens separates the set from that closure. Intersect these separating opens over all excluded points. This argument may be made inside a quasi-compact open containing \(E_0\).

Choose such an open \(U'\) containing \(E_0\), and saturate \(V\setminus U'\), obtaining \(T\). Its closure \(\overline T\) is invariant. To see this, any point of that closure specializes from a point of \(T\): for a quasi-compact scheme map this follows on an affine target by taking a finite affine source cover and a prime after localization. Flat going down along \(s\) lifts that generalization through any arrow, and its target specializes from a point of the invariant set \(T\). Moreover \(E_0\cap\overline T=\varnothing\), because \(E_0\) is stable under generalization and disjoint from \(T\). Thus

\[
U\subset W=V\setminus\overline T\subset U'
\]

is an invariant open neighbourhood. Put \(E=t(s^{-1}U')\). It is invariant, is an intersection of quasi-compact opens, and contains the open \(W\).

Here are the algebra facts for this intersection. Write \(E=\bigcap_i U_i\), with the \(U_i\) quasi-compact opens directed by reverse inclusion. Compactness in the constructible topology shows that every open neighbourhood of \(E\) contains some \(U_i\). Consequently, for the restricted structure sheaf,

\[
\Gamma(E,\mathcal O_V|_E)=\mathop{\rm colim}_i\Gamma(U_i,\mathcal O_{U_i}).
\]

For completeness, a section on \(E\) is locally the restriction of sections on opens of \(V\); finitely many suffice, and their agreement on \(E\) becomes agreement on some \(U_i\). The same finite-neighbourhood argument proves injectivity of this colimit map. Flat scalar extension commutes with these sections: for each quasi-compact quasi-separated \(U_i\), sections are an equalizer for a finite affine cover and its intersections, and flat tensor product preserves that equalizer; it also commutes with the displayed colimit.

A quasi-affine scheme \(U_i\) is canonically an open subscheme of \(\operatorname{Spec}\Gamma(U_i,\mathcal O_{U_i})\). This follows by restricting to principal affine opens and clearing denominators in a finite cover. Passing to the preceding colimit identifies the locally ringed space \(E\) with an intersection of open subsets of

\[
Z=\operatorname{Spec}\Gamma(E,\mathcal O_V|_E).
\]

The identification agrees on stalks. An open \(W\subset V\) contained in \(E\) is open also in \(Z\): for \(U_j\subset U_i\), the inverse image of \(U_j\) under the map to \(\operatorname{Spec}\Gamma(U_i,\mathcal O_{U_i})\) is exactly \(U_j\), as one checks on these principal opens. The same assertion survives the limit, and applies to the opens covering \(W\).

Invariance of \(E\) and the flat section calculation put an algebra descent datum on \(\Gamma(E,\mathcal O_V|_E)\). The faithfully flat algebra descent proved in *Quotients and torsors*, **Corollary, Affine descent**, gives an \(R\)-algebra \(C\) with \(Z\simeq\operatorname{Spec}(C\otimes_RB)\). All identifications are canonical, so the open \(W\subset Z\) is invariant under this affine descent datum and descends to an open of \(\operatorname{Spec}C\).

To justify this last topological step, an invariant open is a union of entire fibres, since pairs of points over one base point have a common lift to the fibre product. Its complementary saturated closed set has closed image under a faithfully flat quasi-compact map. Indeed a point in the closure of that image specializes from an image point by the localization argument above; flat going down and saturation force its entire fibre into the closed set. Thus the invariant open is exactly the inverse image of an open downstairs.

As \(U\) ranges over affine neighbourhoods, the invariant opens \(W\) cover \(V\). Their descended schemes glue: the intersections are invariant opens, and the overlap isomorphisms and cocycle identity descend uniquely. This gives a scheme descending \(V\). It is separated and étale, because these properties descend faithfully flatly; for étaleness one can use descent of local finite presentation and flatness and faithful detection of the vanishing of relative differentials. Finally glue over the affine opens of \(S\). \(\square\)

This is the discrete-scheme case of Gabber's effective descent theorem for ind-quasi-affine morphisms. The invariant-neighbourhood and intersection arguments are those of the Stacks Project, **Groupoid Schemes, Lemmas 39.19.2–39.19.4**, and **More on Groupoid Schemes, Lemmas 40.15.1–40.15.3**. The proof explains why an arbitrary infinite discrete scheme causes no missing descent step here.

### 7.7. Characters and relative multiplicative type

A group scheme \(G/S\) is **of multiplicative type of finite presentation** if it is fpqc locally isomorphic to \(D(M)\) with \(M\) finitely generated. A **torus** is such a group with torsion-free geometric character groups. Both definitions allow the type or rank to vary locally on the base. For a general exponent group, fpqc multiplicative type is a broader notion; the finite-generation hypotheses in this section are explicit.

**Theorem 7.7. Relative character classification.** Over every scheme \(S\), finite-presentation groups of multiplicative type are precisely the étale locally diagonalizable finite-presentation groups. They are affine, commutative and faithfully flat. Characters give an anti-equivalence with locally constant étale sheaves of finitely generated abelian groups:

\[
\begin{gathered}
G\longmapsto X^*(G)=\underline{\operatorname{Hom}}(G,\mathbf G_m),\\
F\longmapsto D(F)=\underline{\operatorname{Hom}}(F,\mathbf G_m).
\end{gathered}
\]

Evaluation identifies each object with its double character dual. Tori correspond to locally constant finite-rank free abelian sheaves.

**Proof.** Affine descent and the split formulas give affineness, commutativity, faithful flatness and finite presentation. The isomorphism type of \(M\) is locally constant on \(S\): on a splitting cover its type fibres are open and closed, they agree on overlaps by the field character theorem, and these invariant opens descend as in Lemma 7.6. Work on one such piece, with fixed \(M\).

Consider the fpqc sheaf

\[
I=\underline{\operatorname{Isom}}(G,D_S(M)).
\]

On an fpqc splitting cover it is the constant scheme \(\operatorname{Aut}(M)\). Indeed finite generation permits one common open neighbourhood on which the images of all character generators are fixed, exactly as in Proposition 7.4. The changes of trivialization provide its scheme descent datum. Lemma 7.6 makes \(I\) a separated étale scheme; it is surjective over \(S\), since it is nonempty on every geometric fibre. Its universal isomorphism therefore splits \(G\) over an étale cover. This proves the fpqc-to-étale assertion without a smoothness assumption on \(G\), even for groups such as \(\mu_p\).

The character sheaf is now locally the constant sheaf \(M\), by Proposition 2.3. Conversely, trivialize a locally constant finitely generated sheaf \(F\) on an étale cover. Its transition maps give Hopf-algebra descent data on \(\mathcal O[M]\); affine descent produces the group scheme \(D(F)\). Morphisms descend too. On each trivializing chart the two functors and the evaluation maps are the mutually inverse character operations of Proposition 2.3. Equality and isomorphisms can be checked after this faithfully flat cover, proving the anti-equivalence and biduality. The split structure theorem for finitely generated abelian groups identifies the torsion-free case with a product of copies of \(\mathbf G_m\); hence the assertion about tori. \(\square\)

Over a henselian local base, every such group splits over a finite étale cover. To check this directly, select a point over the closed point in an affine étale splitting chart. Its residue extension is finite separable. A henselian quasi-finite algebra splits into a finite part containing its closed fibre and a part with empty closed fibre, so the selected finite étale component covers the local base and splits the group. Over a strictly henselian local base that component is a copy of the base, so the group is split. The algebra input is the usual equivalent characterization of henselian rings; for the last assertion a standard étale presentation reduces the section to lifting a simple polynomial root.

**Corollary 7.8. Exactness and the maximal torus.** The category in Theorem 7.7 is abelian, with group kernels and fpqc sheaf cokernels. Every object has a canonical exact sequence

\[
1\longrightarrow T\longrightarrow G\longrightarrow E\longrightarrow1,
\]

where \(T\) is a torus and \(E\) is finite locally free of multiplicative type. The torus is maximal among closed subtori; the sequence and this maximality commute with all base changes.

**Proof.** A morphism of two locally constant finitely generated character sheaves is locally a fixed map of finitely generated groups, by a common neighbourhood for the finitely many generators. Its kernel, image and cokernel are consequently locally constant and finitely generated. Theorem 4.5, followed by affine descent, identifies their duals with the scheme kernels, closed images and fpqc quotients in the claimed order; it also gives the categorical image–coimage isomorphism.

For \(F=X^*(G)\), its torsion subsheaf \(F_{\rm tor}\) is locally constant finite, and \(F/F_{\rm tor}\) is a locally constant lattice. Dualize

\[
0\longrightarrow F_{\rm tor}\longrightarrow F
\longrightarrow F/F_{\rm tor}\longrightarrow0.
\]

The result is the displayed sequence with \(T=D(F/F_{\rm tor})\) and \(E=D(F_{\rm tor})\). A closed embedding of a torus into \(G\) corresponds to a quotient of \(F\) which is torsion-free; it therefore kills \(F_{\rm tor}\) and factors through \(F/F_{\rm tor}\). All constructions are local on the same étale charts and unchanged by their pullback to any base scheme. \(\square\)

**Proposition 7.9. Relative Hom and forms.** For two finite-presentation multiplicative-type groups \(G,H/S\), their Hom, Isom and Aut functors are represented by separated étale \(S\)-schemes. Hom is locally the constant group \(\operatorname{Hom}(X^*(H),X^*(G))\); Isom and Aut are the corresponding open and closed subsets. In particular forms of \(D_S(M)\) are classified by torsors for the constant étale group \(\operatorname{Aut}(M)\).

**Proof.** On an étale cover splitting both groups, Proposition 7.4 gives the constant Hom scheme. Isomorphisms form the subset of invertible character maps; it is open and closed in a discrete scheme. The transition identifications satisfy descent, and Lemma 7.6 makes all three functors representable. A form determines its torsor of isomorphisms. Conversely a torsor glues the split Hopf algebra by its automorphism action, using affine descent. An isomorphism of torsors is exactly an isomorphism of the glued forms, so the constructions are inverse, including at the groupoid level. \(\square\)

### 7.10. Finite splitting over a normal base

**Lemma 7.10. A torsion-free congruence kernel.** For a finitely generated abelian group \(M\), choose \(n\ge3\) divisible by the exponent of \(M_{\rm tor}\). Then

\[
\ker\bigl(\operatorname{Aut}(M)\to\operatorname{Aut}(M/nM)\bigr)
\]

has no nonidentity element of finite order.

**Proof.** First let \(M=\mathbf Z^r\). The integer \(n\) has an odd prime divisor \(p\), or is divisible by \(4\). In the second case take \(p=2\). A nonidentity matrix congruent to \(1\) modulo \(n\) has the form \(1+p^aB\), with some entry of \(B\) not divisible by \(p\), where \(a\ge1\), and \(a\ge2\) when \(p=2\). If it had finite order, a suitable power would be nonidentity of prime order \(q\), still satisfying these bounds. If \(q\ne p\), the expansion of \((1+p^aB)^q-1\), divided by \(p^a\), is nonzero modulo \(p\). If \(q=p\), divide instead by \(p^{a+1}\): its first term is \(B\), while all later terms are divisible by \(p\). For odd \(p\) this uses \(\binom pi\equiv0\pmod p\) for \(1<i<p\); for \(p=2\) it uses \(2a\ge a+2\). Both cases contradict prime order.

An automorphism in the stated kernel acts on \(M/M_{\rm tor}\) through this torsion-free matrix kernel. If it has finite order, its action there is trivial, so \(\gamma(m)-m\in M_{\rm tor}\). It is also in \(nM\). The structure theorem gives \(nM\cap M_{\rm tor}=0\), because \(n\) kills the torsion subgroup. Thus \(\gamma=1\). \(\square\)

**Theorem 7.11. Normal-base isotriviality.** On a normal scheme \(S\), every finite-presentation group of multiplicative type is Zariski locally split by a finite étale cover. If \(S\) is also irreducible, one finite étale cover of \(S\) splits it. In particular the latter conclusion holds for connected locally Noetherian normal \(S\).

**Proof.** By Theorem 7.7 use its locally constant finitely generated character sheaf \(F\). Assume first that \(S\) is irreducible; its stalk type is one fixed \(M\). For the integer \(n\) of Lemma 7.10, \(F/nF\) is a finite locally constant sheaf and is represented by a finite étale scheme, by affine descent. Its sheaf of isomorphisms with the constant group \(M/nM\) is itself finite étale and surjective: after a trivializing cover it is a finite nonempty constant set. Pull back to this finite cover. A connected component of it still covers \(S\), and is normal and irreducible. Indeed any finite étale scheme over an irreducible normal base has only finitely many irreducible components, from its finite generic fibre; normality makes these disjoint, hence open and closed. We may therefore suppose \(F/nF\) constant over an irreducible normal base.

Over its generic field, \(F\) corresponds to a continuous Galois action on \(M\). That action has finite image by finite generation. The image lies in the kernel of Lemma 7.10, and is consequently trivial. Fix a trivialization \(f_\eta:M_\eta\simeq F_\eta\).

This trivialization extends over each normal local ring \(A=\mathcal O_{S,s}\). Choose an affine étale splitting chart over \(\operatorname{Spec}A\) which meets the closed fibre. The chart is normal and has finitely many irreducible components: its generic fibre is a finite set, and flat going down sends every minimal point to the generic point of \(\operatorname{Spec}A\). Choose a component meeting the closed fibre. It is affine and irreducible; its open image contains the closed point of the local base, and therefore is the entire base. Over this chart the generic trivialization extends uniquely between constant sheaves. On its self-fibre-product the two extensions agree: that normal étale scheme has finitely many irreducible components, each meeting the generic fibre, and a map between constant finitely generated sheaves is locally constant. Thus the extension descends to \(\operatorname{Spec}A\).

It extends further to an open neighbourhood of \(s\): equivalently it is an isomorphism of affine finitely presented group schemes over \(A\); the finitely many coordinate images, relations, Hopf identities and inverse identities can all be spread after inverting finitely many elements outside the prime of \(s\). On overlapping nonempty opens the extensions are unique, since their isomorphism sheaf is étale locally discrete and the normal étale charts have every component meeting the generic fibre. They glue to \(f:M_S\simeq F\). This proves global finite splitting for irreducible normal \(S\).

For a general normal \(S\), apply the irreducible result to \(\operatorname{Spec}\mathcal O_{S,s}\), an integrally closed local domain. Its finite étale splitting cover and its group-scheme trivialization spread to a finite étale splitting cover of an open neighbourhood of \(s\), by the same finite-presentation argument. This gives the asserted Zariski local conclusion. Connected locally Noetherian normal schemes are irreducible, since their irreducible components are disjoint open and closed. \(\square\)

The irreducibility hypothesis is retained in the global assertion. Connected normal schemes need not be irreducible when local Noetherianity is omitted. The proof uses neither a Noetherian hypothesis in the irreducible case nor a claim that all relative tori have finite global monodromy over arbitrary bases.

For a rank-\(r\) torus on an irreducible normal base, the frame cover of \(X^*(T)/3X^*(T)\) already splits \(T\), by the proof and Lemma 7.10. It has degree

\[
|\mathrm{GL}_r(\mathbf F_3)|
=\prod_{i=0}^{r-1}(3^r-3^i).
\]

A connected component is a Galois splitting cover whose group is a subgroup of \(\mathrm{GL}_r(\mathbf F_3)\): the stabilizer of the component in the frame torsor acts simply transitively on its geometric fibres. In particular its degree is bounded by the displayed integer. This keeps the quantitative congruence-cover refinement as well as finite splitting itself.

For an irreducible normal \(S\), the finite-cover description and the usual finite-étale-cover definition of \(\pi_1(S,\bar s)\) identify these groups with finitely generated discrete continuous \(\pi_1\)-modules, contravariantly. Tori correspond to lattices. Finite generation makes each such continuous action factor through a finite quotient.

### 7.12. Embedding into a torus

**Theorem 7.12. Every finite-presentation multiplicative-type group embeds in a torus.** Over any scheme \(S\), not necessarily normal, each group \(G\) in Theorem 7.7 admits a closed immersion into an \(S\)-torus.

**Proof.** We construct a surjection of a locally constant lattice onto \(F=X^*(G)\). Work first on an open and closed piece where its finitely generated stalk type is fixed. Let \(Q=F_{\rm tor}\), let \(L=F/Q\), and choose an integer \(n\) killing \(Q\). The finite locally constant sheaves \(Q\) and \(F/nF\) become constant on one finite étale cover \(q:S'\to S\): use the finite sheaves of their frames, as in Theorem 7.11. Refine by open and closed pieces so that the maps between these finite constant sheaves are fixed. In the exact sequence

\[
0\longrightarrow Q\longrightarrow F/nF
\longrightarrow L/nL\longrightarrow0
\]

the last constant module is free over \(\mathbf Z/n\mathbf Z\). Hence the sequence splits over \(S'\). Composing its retraction with \(F\to F/nF\) splits \(Q\to F\), so \(F|_{S'}\simeq Q\oplus L|_{S'}\). Choose a surjection \(\mathbf Z^d\to Q\). It gives a surjection of the lattice

\[
L'=L|_{S'}\oplus\mathbf Z^d_{S'}\longrightarrow F|_{S'}.
\]

The sheaf \(q_*L'\) is a locally constant lattice: étale locally \(q\) is a finite disjoint union of copies of the base, and this pushforward is the direct sum of the corresponding lattices. Send it to \(F\) by summing the maps from those sheets. This is independent of their ordering and is surjective on every stalk, since each sheet already gives a surjection. By Theorem 4.5 and étale descent, dualizing gives a closed immersion

\[
G=D(F)\lhook\joinrel\longrightarrow D(q_*L').
\]

The target is a torus. If \(Q=0\), simply take \(L'=F\) and the identity embedding. Finally, the stalk types of \(F\) give a disjoint open and closed decomposition of \(S\); perform the construction on each piece and take their disjoint union over \(S\). A torus has locally finite rank, so no uniform rank bound on all of \(S\) is required. \(\square\)

**Proposition 7.13. A fixed splitting cover.** If \(S'\to S\) is a connected finite étale Galois torsor with group \(\Delta\), groups of multiplicative type split by this cover are anti-equivalent to finitely generated abelian groups with a \(\Delta\)-action, on a connected base. Every such group embeds in a torus split by the same cover; the torus may be chosen quasi-trivial.

**Proof.** A trivialized character sheaf over the connected \(S'\) has constant stalk group \(M\). Its descent datum on \(S'\times_SS'\simeq\Delta\times S'\) is exactly an action of \(\Delta\) on \(M\); the cocycle identity is its action law. Conversely this datum descends the split Hopf algebra, and equivariant maps descend precisely to homomorphisms. Connectedness of the splitting cover is part of this statement. For a disconnected torsor, the descent objects are equivariant locally constant sheaves on all its components; arbitrary actions on one constant module would not give this asserted equivalence.

Choose generators \(m_1,\ldots,m_d\) of \(M\). The equivariant map

\[
\mathbf Z[\Delta]^d\longrightarrow M,
\qquad [\delta]_i\longmapsto\delta m_i
\]

is surjective. Its source is a permutation lattice. The dual is a product of restrictions of scalars \(\operatorname{Res}_{S'/S}\mathbf G_m\): after the splitting cover the coordinate torus has one coordinate per sheet, with the permutation transition maps. This also constructs that restriction of scalars by affine descent, without assuming its representability separately. The surjection therefore dualizes to a closed embedding in the asserted quasi-trivial torus. \(\square\)

### 7.14. Cohomology and lifting homomorphisms

**Proposition 7.14. Vanishing of regular higher cohomology.** Let \(S=\operatorname{Spec}R\), let \(H/S\) be a group of multiplicative type, and let \(E\) be a quasi-coherent \(H\)-module. The invariants functor is exact. The regular Hochschild cochain complex

\[
C^j(H,E)=\Gamma(H^j,E_{H^j})
\]

has \(H^j=0\) for all \(j>0\). Its differential is

\[
dc=\sum_{i=0}^{j+1}(-1)^i d_i c.
\]

On a tuple \((g_1,\ldots,g_{j+1})\), the first face is \(g_1c(g_2,\ldots,g_{j+1})\), the face \(d_i\) for \(1\le i\le j\) replaces the consecutive pair \(g_i,g_{i+1}\) by their product, and the last face drops \(g_{j+1}\). Associativity and the action law give \(d^2=0\) by cancellation of consecutive faces.

These are identities of regular sections on the schemes of tuples, not identities only on rational points.

**Proof.** For \(H=D_R(M)\), invariants are the degree-zero summand, so taking them is exact. Define the invariant integral \(\int f\) on \(R[M]\) to be the coefficient of \(e^0\). The identity

\[
(\int\otimes1)\Delta(f)=(\int f)1
\]

on each basis element proves translation invariance after any scalar extension. For \(j\ge1\), set

\[
(hc)(g_1,\ldots,g_{j-1})
=\int_a a^{-1}c(a,g_1,\ldots,g_{j-1}).
\]

The action and integral give an \(R\)-linear operation on the cochain modules even when \(E\) has infinitely many weights. Expanding \(dhc+hdc\), the terms which multiply two of the \(g_i\), and the last terms, cancel in pairs. The first term of \(hdc\) is \(c\); its next term, after the substitution \(b=ag_1\) and translation invariance, is the negative of the first term of \(dhc\). Thus \(dh+hd=1\) in positive degrees. In degree zero, \(hd(v)=v-v_0\), with \(v_0\) its invariant component. This proves the claimed cohomology calculation directly.

For a relative form, choose an affine faithfully flat splitting refinement. Each \(H^j\) is affine over \(S\). Flat scalar extension commutes with its quasi-coherent sections, with the cochain differential and with cohomology, because flat tensor product preserves kernels and images. The split calculation therefore detects the vanishing faithfully flatly. The same argument applied to a short exact sequence proves exactness of invariants. \(\square\)

**Theorem 7.15. Nilpotent lifting and conjugacy.** Let \(R\) be any ring, \(J\subset R\) a nilpotent ideal, \(H/R\) a finite-presentation multiplicative-type group, and \(G/R\) a smooth group scheme. Every homomorphism

\[
f_0:H_{R/J}\longrightarrow G_{R/J}
\]

lifts to a homomorphism \(H\to G\). Any two lifts are conjugate by an element of \(\ker(G(R)\to G(R/J))\). The target need not be affine.

**Proof.** Assume first \(J^2=0\). Since \(H\) is affine, the smooth lifting and affine gluing theorem in **AG-FSE, Infinitesimal lifting and invariance under thickenings, Theorems 3.3 and 4.1**, lifts \(f_0\) as a scheme map \(f:H\to G\). Its failure to respect multiplication is a regular cochain

\[
c(g_1,g_2)=f(g_1)f(g_2)f(g_1g_2)^{-1}
\]

with values in \(V=\operatorname{Lie}(G_{R/J})\otimes_{R/J}J\), acted on through \(\operatorname{Ad}\circ f_0\). This identification is made on the universal schemes \(H^j\), which are flat over \(R\): their square-zero ideals are \(J\otimes_R\mathcal O_{H^j}\). It does not presume this tensor identification for arbitrary nonflat test algebras.

Associativity on \(H^3\) gives \(dc=0\). If the scheme lift is changed to \(b(g)f(g)\), its obstruction changes to \(c+db\). These formulas follow by moving a kernel element past \(f(g_1)\), which applies \(\operatorname{Ad}(f_0(g_1))\); products in the square-zero kernel are addition. Proposition 7.14 gives \(c=db'\). Changing the lift by \(-b'\) kills its obstruction, so produces a homomorphism. Preservation of multiplication forces its value at the identity to be the identity and also forces preservation of inverses.

For two homomorphism lifts, their ratio is a regular one-cocycle \(b\). Again Proposition 7.14 gives \(b=dw\), with \(w\in V(S)\). Conjugation by the kernel element corresponding to \(-w\) changes the first lift by this ratio, since its effect is \((-w)-g(-w)=dw(g)\). The kernel–tangent identification at the identity supplies the required element of \(G(R)\).

For a nilpotent \(J\), lift successively over \(R/J^i\), whose consecutive kernels are square-zero. To compare two final lifts, first conjugate their reductions by induction. Smooth lifting over the affine base lifts that conjugating element, choosing a lift which still reduces to the identity modulo \(J\). After this conjugation the remaining difference is in the last square-zero ideal and is corrected by the preceding argument. Composing these conjugators proves the assertion. \(\square\)

**Proposition 7.16. A trivial homomorphism is rigid without a smooth target.** Let \(J\subset R\) be nilpotent, \(H/R\) of finite-presentation multiplicative type, and \(G/R\) any group scheme. A homomorphism \(H\to G\) is trivial if its reduction modulo \(J\) is trivial. The same assertion holds for an fpqc form of \(D(M)\) with arbitrary \(M\), without finite presentation.

**Proof.** Reduce by induction to a square-zero ideal, and then faithfully flatly to \(H=D_R(M)\). Locally on the base both the homomorphism and the trivial homomorphism land in an affine neighbourhood of the identity section: their underlying images are the same because the base thickening is nilpotent. Their difference is a derivation at that section with values in \(J R[M]\). The differential of group multiplication at the identity is addition, so its value on each element of the identity cotangent module is primitive:

\[
\Delta(z)=z\otimes1+1\otimes z.
\]

The only primitive element of \(J R[M]\) is zero. For \(z=\sum j_me^m\), compare the coefficient of \((m,m)\) for \(m\ne0\) to get \(j_m=0\); for \(m=0\) the identity is \(j_0=2j_0\), hence \(j_0=0\). Each coordinate difference is therefore zero, giving the trivial homomorphism. This coefficient argument needs neither finite generation nor projectivity of the target cotangent module. Descent and the induction complete the proof. \(\square\)

**Corollary 7.17. Central vector extensions split uniquely.** Let \(S\) be affine, let \(H/S\) be a finite-presentation multiplicative-type group, and let \(V(E)\) be the additive vector group of a finite projective module \(E\). Any central extension of group schemes

\[
1\longrightarrow V(E)\longrightarrow P\longrightarrow H\longrightarrow1
\]

which is exact as fpqc sheaves is the direct product extension, with a unique homomorphism section.

**Proof.** The map \(P\to H\) is a \(V(E)\)-torsor. Over the affine scheme \(H\), it has a scheme section. Indeed choose an affine faithfully flat trivializing cover. Its two local sections differ by an additive Čech cocycle in the pulled-back quasi-coherent module. The faithfully flat module descent proof in *Quotients and torsors* gives exactness of this Amitsur complex, so the cocycle is a coboundary. Correct the local section and descend it to a section \(f\) on \(H\).

Its multiplication defect is the regular two-cocycle of Theorem 7.15. Centrality makes the action on \(E\) trivial. Proposition 7.14 kills that cocycle by a regular one-cochain, giving a homomorphism section. Any two such sections differ by a homomorphism \(H\to V(E)\). After faithfully flat splitting of \(H\) and local trivialization of \(E\), its coordinates are primitive elements of a group algebra. The coefficient argument in Proposition 7.16 shows they are zero. Thus the homomorphism section is unique. Multiplication gives the product isomorphism \(V(E)\times_SH\to P\); its inverse sends a point \(p\) to its projection \(h\) and the unique kernel element \(p f(h)^{-1}\). These formulas are natural in every test scheme. \(\square\)

**Proposition 7.18. Finite étale restriction of scalars.** Let \(q:S'\to S\) be finite étale and let \(G'/S'\) be of finite-presentation multiplicative type, with character sheaf \(F'\). Its restriction of scalars exists and is

\[
\operatorname{Res}_{S'/S}G'=D(q_*F').
\]

If \(G'\) is a torus, so is this group. If \(G'=D_{S'}(M)\), the result is split by a finite étale cover of \(S\).

**Proof.** Étale locally on \(S\), the finite étale map is a disjoint union of finitely many copies of the base. Its restriction-of-scalars functor is then the product of the groups on those sheets, whose character sheaf is the direct sum of their character sheaves, precisely \(q_*F'\). This is locally constant and finitely generated, and is a lattice in the torus case. The affine groups glue by Theorem 7.7 and their functors glue to the required functor, proving representability. When \(F'\) is constant, a finite étale cover ordering the sheets makes \(q_*F'\) a constant direct sum of copies of \(M\), which proves the final assertion. The diagonal map \(G\to\operatorname{Res}_{S'/S}G_{S'}\), when \(q\) is surjective, has dual map summing the sheet copies of \(X^*(G)\); it is a closed immersion by Theorem 4.5. \(\square\)

**Corollary 7.19. Finite multiplicative-type groups are isotrivial.** A finite locally free group of multiplicative type over any scheme is split by a finite étale cover. No normality hypothesis is needed.

**Proof.** Its character sheaf is finite locally constant: on a splitting chart the rank of the coordinate algebra is the order of the exponent group, by Proposition 4.6. On a piece of constant character type \(M\), the sheaf of its isomorphisms with \(M_S\) is a finite étale surjective scheme, since \(\operatorname{Aut}(M)\) is finite. It trivializes the character sheaf and hence its dual group. Glue these covers over the disjoint open and closed type pieces. Finiteness is local on the base, so this produces the asserted finite étale cover over arbitrary \(S\). \(\square\)

**Proposition 7.20. Isotrivial groups and the fundamental group.** Let \(S\) be connected with geometric point \(\bar s\). The full category of finite-presentation multiplicative-type groups split by some finite étale cover is anti-equivalent to finitely generated discrete continuous \(\pi_1(S,\bar s)\)-modules. It is an abelian subcategory. Each object has a minimal connected Galois splitting cover, determined by the kernel of its character action.

**Proof.** The finite-étale-cover equivalence with finite continuous \(\pi_1\)-sets identifies finite-cover descent data for a constant character group with a continuous action through a finite quotient. Conversely a continuous action on a finitely generated group has finite image: choose generators, intersect their open stabilizers, and take its finite-index normal core. This core fixes every generator and therefore all the group. The resulting finite-cover descent datum constructs its character sheaf and its dual group by Theorem 7.7. Equivariant maps give precisely the homomorphisms under this anti-equivalence.

For any morphism, the character kernel, image and cokernel are finitely generated and their actions still factor through a common finite quotient. Corollary 7.8 therefore makes this full subcategory abelian. A connected Galois cover associated with an open normal subgroup splits the group exactly when that subgroup acts trivially on its characters. The largest such subgroup is the kernel of the action, which is open and normal. Its cover is consequently minimal among connected Galois splitting covers; every other one maps to it. This description retains the chosen geometric point and uses the standard finite-étale-cover construction of the fundamental group. \(\square\)

### 7.15. Recognizing the additive group from its tangent weight

**Theorem 7.21. Rank-one additive recognition.** Let \(U\to S\) be a smooth affine group scheme whose geometric fibres are isomorphic to \(\mathbf G_a\). Suppose \(\mathbf G_{m,S}\) acts on \(U\) by group automorphisms, and acts nontrivially on the line bundle \(L=\operatorname{Lie}(U/S)\) at every geometric point. There is a unique equivariant group isomorphism

\[
W(L)=\operatorname{Spec}_S\operatorname{Sym}(L^\vee)
\xrightarrow{\ \sim\ }U
\]

whose differential at the identity is the identity of \(L\). This isomorphism is natural under arbitrary base change. No Noetherian or reducedness hypothesis on \(S\) is needed, and the nonzero integer tangent weight need not be invertible on \(S\).

**Proof.** We work locally on an affine base \(\operatorname{Spec}R\). A torus action on an invertible module has one integer weight on each open and closed piece of the base: the weight decomposition has finitely many summands locally, and the projections on a line are orthogonal idempotents summing to one. Thus we may fix a nonzero weight \(n\) for \(L\). Inverting the acting torus if necessary makes \(n>0\). Write \(A=\Gamma(U,\mathcal O_U)\), graded by its action coaction, and let \(\epsilon:A\to R\) be evaluation at the identity.

On every geometric fibre the action on \(\mathbf G_a\) is scalar multiplication by \(t^n\). Here is a scheme-level verification. An automorphism of the affine line over an algebraically closed field is linear, by the degree formula for a polynomial and its compositional inverse. A group automorphism fixes zero. The universal action over \(k[t,t^{-1}]\), a domain, is therefore \(x\mapsto c(t)x\); the action identities make \(c(t)=t^m\). Its differential identifies \(m=n\). Consequently the graded fibre algebra is \(k[x]\) with \(\deg x=n\).

By Theorem 3.5 the invariant algebra \(A_0\) is of finite type over \(R\), and each \(A_j\) is a finite \(A_0\)-module. We first prove \(A_0=R\), including on a nonreduced base. Evaluation splits its inclusion of \(R\), so \(A_0=R\oplus I\) as modules, where \(I=\ker\epsilon|_{A_0}\). The ideal \(I\) is finitely generated as an \(A_0\)-ideal: subtract the augmentation values from a finite set of algebra generators. Its quotient \(I/I^2\) is therefore finite over \(R=A_0/I\). Every fibre algebra of \(A_0\) is \(k\), since taking weight zero commutes with scalar extension. The split decomposition gives \(I\otimes_Rk=0\) for every residue field. Thus \(I/I^2\) has zero fibres, and finite-module Nakayama gives \(I/I^2=0\).

A finitely generated ideal satisfying \(I=I^2\) is generated by an idempotent. To see it without a finiteness assumption on \(R\), write its generators as \(a_i=\sum_j c_{ij}a_j\), with \(c_{ij}\in I\). The determinant trick gives \((1-b)I=0\) for some \(b\in I\). Hence \(b^2=b\) and \(I=(b)\). But \(I\) lies in every prime of \(A_0\): every such prime lies over a prime of \(R\), and the corresponding fibre is the single augmented point. Thus \(b\) is nilpotent as well as idempotent, so is zero. This proves \(A_0=R\).

Each \(A_j\) is now finite over \(R\). Its fibres vanish unless \(j\) is a nonnegative multiple of \(n\), so those other pieces vanish by Nakayama. Smoothness makes \(A\) flat over \(R\); every piece, a direct summand, is flat. In fact each piece is finitely presented. Choose finitely many homogeneous algebra generators of \(A\); the degree-zero generators can be removed since \(A_0=R\), and all the others have positive degrees. They give a graded polynomial presentation \(P\to A\). Its kernel has finitely many homogeneous generators, because \(A\) is finitely presented and replacing generators of a graded ideal by their homogeneous components preserves its generated ideal. For any degree \(j\), \(P_j\) is finite free: only finitely many monomials have that degree when all variable degrees are positive. The degree-\(j\) kernel is the image of finitely many such finite free pieces, giving a finite presentation of \(A_j\). A flat finitely presented module is projective.

The differential of evaluation gives

\[
A_n\longrightarrow\omega_U=\epsilon^*\Omega_{U/S},
\qquad a\longmapsto da.
\]

Both modules are finite projective, and the map is an isomorphism on every geometric fibre: the degree-\(n\) coordinate is \(x\), and its differential generates the identity cotangent line. A map of finite projective modules which is an isomorphism on all fibres is an isomorphism, as follows by Nakayama for its cokernel and then for the kernel of the split surjection. In particular \(A_n\) is invertible. The algebra map

\[
\operatorname{Sym}_R A_n\longrightarrow A
\]

is an isomorphism degree by degree. In degrees divisible by \(n\), it is a map of finite projective modules with fibre map the corresponding monomial isomorphism in \(k[x]\); all other positive pieces on either side vanish.

It is also an isomorphism of Hopf algebras. The coproduct preserves total degree. In degree \(n\), its only possible pieces are of bidegrees \((n,0)\) and \((0,n)\), since no smaller positive degree occurs. The counit identities consequently force

\[
\begin{gathered}
\Delta(a)=a\otimes1+1\otimes a,\\
\epsilon(a)=0\quad(a\in A_n).
\end{gathered}
\]

This is the additive vector-group Hopf algebra. Identify \(A_n\) with \(\omega_U=L^\vee\) by the differential map. The resulting group isomorphism has identity differential and the required tangent-weight action.

For uniqueness, an equivariant endomorphism of the coordinate symmetric algebra is determined by its map on its degree-\(n\) piece, since that piece generates the algebra. An identity differential forces this map to be the identity. Thus two claimed isomorphisms agree. This uniqueness glues the local constructions over \(S\) and proves their compatibility with every base change. \(\square\)

The positive grading supplies the whole coordinate algebra, rather than merely a first-order resemblance to \(\mathbf G_a\). It also explains why geometric additive fibres by themselves are not a classification of additive-group forms over an imperfect field. The torus action and its nonzero tangent weight are substantive hypotheses.

### 7.16. Flat closed subgroups of multiplicative type

The nonflat example in Section 4.3 shows that a closed subgroup of a split diagonalizable group need not be diagonalizable over a ring. With flatness and finite presentation, the conclusion holds over every base scheme. We first supply the nilpotent and finite-group steps needed for its proof.

**Lemma 7.22. Subgroups over a local nilpotent base.** Let \(R\) be a local ring whose maximal ideal \(\mathfrak m\) is nilpotent, with residue field \(k\). Let \(M\) be finitely generated and let \(H\subset D_R(M)\) be a closed subgroup flat over \(R\). Write

\[
H_k=D_k(M/N)\subset D_k(M)
\]

using the unique subgroup \(N\subset M\) from Theorem 4.2. Then \(H=D_R(M/N)\) as closed subgroups of \(D_R(M)\). The ring \(R\) need not be Noetherian.

**Proof.** Let \(R[M]\twoheadrightarrow B\) be the Hopf quotient for \(H\), and let \(b_m\) denote the image of \(e^m\). For \(n\in N\), \(b_n-1\in\mathfrak mB\). Suppose it belongs to \(\mathfrak m^rB\), where \(r\geq1\). Flatness of \(B\) identifies its class modulo \(\mathfrak m^{r+1}B\) with an element of

\[
(\mathfrak m^r/\mathfrak m^{r+1})
\otimes_k k[M/N].
\]

The identity \(\Delta(b_n)=b_n\otimes b_n\) makes that class primitive: the product of the two correction terms lies in \(\mathfrak m^{2r}(B\otimes_RB)\), hence in \(\mathfrak m^{r+1}(B\otimes_RB)\). Flatness also gives the analogous identification for this tensor product. There are no primitives in a group algebra, even with coefficients in a \(k\)-vector space \(E\). Indeed write a proposed primitive as the finite sum \(\sum_\ell c_\ell e^\ell\), with \(c_\ell\in E\). For \(\ell\ne0\), the coefficient of \(e^\ell\otimes e^\ell\) in its primitive identity forces \(c_\ell=0\). The coefficient at \((0,0)\) then says \(c_0=2c_0\), so \(c_0=0\) in every characteristic.

Thus \(b_n-1\in\mathfrak m^{r+1}B\). Induction and nilpotence give \(b_n=1\) for all \(n\in N\). The Hopf quotient factors into a surjection \(R[M/N]\twoheadrightarrow B\), whose reduction is an isomorphism. If \(J\) is its kernel, flatness of \(B\) makes reduction exact at \(J\), so \(J/\mathfrak mJ=0\). Consequently \(J=\mathfrak mJ=\mathfrak m^2J=\cdots=0\). This last argument uses nilpotence, not finite generation of \(J\). The surjection is an isomorphism, with the specified inclusion into \(D_R(M)\). \(\square\)

**Lemma 7.23. A uniform exponent for étale fibre groups.** Let \(S\) be Noetherian and quasi-compact, and let \(Q\to S\) be an étale group scheme of finite type. There is an integer \(d\) bounding the order of every geometric fibre group, and \([d!]=0\) on \(Q\) if \(Q/S\) is separated.

Here \([n]\) denotes the power morphism \(q\mapsto q^n\); it is a group homomorphism when \(Q\) is commutative, as in the applications below.

**Proof.** We prove the required bound for any finite-type quasi-finite scheme over \(S\). Use finite affine covers of the base and their inverse images. For an irreducible reduced closed piece of the base with affine ring \(A\) and fraction field \(K\), each affine source chart has a finite-type \(A\)-algebra \(B\) with \(B\otimes_AK\) finite-dimensional over \(K\). Its finitely many algebra generators satisfy monic equations over \(K\). Clearing coefficients and the finitely many errors in those equations gives a nonzero \(a\in A\) for which \(B_a\) is finite over \(A_a\). Choose a finite set of module generators. On \(D(a)\), its cardinality bounds the dimension of every residue-field algebra, hence the number of geometric points in every chart fibre. Sum these finitely many chart bounds.

Do this on the finitely many irreducible components of the base. It gives a bound on an open containing their generic points. Apply the same argument to its proper closed complement, with reduced structure. Noetherian induction gives a bound there as well. Taking the maximum, and then the maximum for the finite base cover, proves the uniform bound \(d\). For an étale fibre, the number of geometric points is its finite group order. Lagrange's theorem makes \(d!\) annihilate each such group.

To deduce equality of scheme maps, use that the diagonal of a separated étale scheme is an open and closed immersion. The equalizer of \([d!]\) and the trivial homomorphism is therefore an open and closed subscheme of \(Q\). It contains every geometric fibre and hence every point. An open immersion with the entire underlying space is an isomorphism. Thus the two maps agree on the full scheme, including nilpotent base directions. \(\square\)

**Lemma 7.24. A trivial special fibre in a diagonalizable group.** Let \(R\) be a local Noetherian ring. Let \(Q\subset D_R(N)\) be a closed subgroup, flat and of finite presentation over \(R\), where \(N\) is finitely generated. If its closed fibre is the trivial group, then \(Q\) is trivial.

**Proof.** Let \(E=e^*\Omega_{Q/R}\), a finite \(R\)-module. Its reduction is the cotangent space at the identity of the trivial closed fibre, so it is zero. Nakayama gives \(E=0\). Relative differentials have their canonical linearization under left translation. The translation equivalence in *Group schemes, actions and Hopf algebras*, Theorem 4.5, therefore gives

\[
\Omega_{Q/R}\simeq\mathcal O_Q\otimes_RE=0.
\]

Flatness and finite presentation now make \(Q/R\) étale, by *Étale morphisms and their local structure*, Theorem 1.3. Notice that this step uses only locality of \(R\), not Noetherianity.

Lemma 7.23 gives an integer \(n>0\) killing \(Q\). Hence \(Q\) is a closed subgroup of

\[
D_R(N)[n]=D_R(N/nN),
\]

which is finite over \(R\) since \(N\) is finitely generated. The étale group \(Q\) is thus finite étale. Its finite locally free rank is constant on the connected local base and is one on the closed fibre. Its identity section is an open and closed immersion, meeting the unique point of every fibre. It is surjective and therefore an isomorphism. \(\square\)

**Theorem 7.25. Flat closed relative subgroups.** Let \(S\) be any scheme, let \(H'/S\) be a finite-presentation group of multiplicative type, and let \(H\subset H'\) be a closed subgroup flat and locally of finite presentation over \(S\). Then \(H\) is of finite-presentation multiplicative type. More precisely, wherever \(H'=D_S(M)\) is split, there is a Zariski-local description

\[
H=D_S(M/N)\subset D_S(M)
\]

for a locally constant subgroup \(N\subset M\). Thus the inclusion is dual to the surjection of character sheaves

\[
X^*(H')\twoheadrightarrow X^*(H).
\]

The subgroup description and this character map commute with arbitrary base change.

**Proof.** Splitting \(H'\) on an fppf cover and restricting to affine opens reduces the proof to \(H\subset D_R(M)\), with \(M\) finitely generated. The closed immersion makes \(H\) affine and quasi-compact over this affine base. Its local finite presentation is therefore finite presentation. Write its coordinate algebra as the finitely presented flat Hopf quotient \(B=R[M]/I\).

We may first replace \(R\) by a Noetherian model. Choose finitely many generators of \(I\). Their coefficients, and finite witnesses that comultiplication, counit and antipode preserve this ideal, occur in a finitely generated \(\mathbf Z\)-subalgebra of \(R\). This constructs a finitely presented Hopf quotient \(B_i\) of \(R_i[M]\) whose scalar extension is \(B\). The exact flat finite-presentation approximation theorem, [Stacks, Tag 02JO](https://stacks.math.columbia.edu/tag/02JO), makes \(B_i\) flat at a sufficiently late stage. Here its module is \(B_i\) itself; the finite Hopf identities already descended and remain true at that later stage. Thus a Zariski-local subgroup description for this Noetherian model pulls back to the required description over \(R\).

Now suppose \(R\) is Noetherian and local, with residue field \(k\). Theorem 4.2 determines \(N\subset M\) by \(H_k=D_k(M/N)\). Pass faithfully flatly to its maximal-ideal completion. *Completion*, Theorems 3.1–3.3, proves the required faithful flatness, Noetherianity and quotient identities. We can therefore assume that \(R\) is complete with maximal ideal \(\mathfrak m\).

For every \(r\geq1\), Lemma 7.22 applied over \(R/\mathfrak m^r\) gives the canonical equality

\[
H_{R/\mathfrak m^r}
=D_{R/\mathfrak m^r}(M/N).
\]

Consider the fixed map \(R[M]\to R[M/N]\). Every element of \(I\) maps into \(\mathfrak m^rR[M/N]\) for every \(r\). An element of this group algebra has finite support, and its coefficients lie in the separated complete ring \(R\). Consequently the intersection of these submodules is zero. The map factors through a surjection \(B\twoheadrightarrow R[M/N]\). It gives a canonical closed subgroup

\[
H_0=D_R(M/N)\subset H\subset D_R(M).
\]

All these groups are commutative. The free diagonalizable quotient theorem, Theorem 4.9, represents \(K=H/H_0\) as an affine group scheme, with \(H\to K\) a torsor under \(H_0\). It also represents \(D_R(M)/H_0=D_R(N)\), by Theorem 4.5. The induced map \(K\to D_R(N)\) is a monomorphism on every test scheme. Moreover

\[
H\simeq K\times_{D_R(N)}D_R(M).
\]

Indeed local lifts of a quotient class differ exactly by \(H_0\), which lies in \(H\). Closed-immersion descent along the faithfully flat map \(D_R(M)\to D_R(N)\) thus makes \(K\) a closed subgroup of \(D_R(N)\). It is flat by faithful flat descent from \(H\), and is of finite presentation since \(N\) is finitely generated and the base is Noetherian. Formation of the diagonalizable quotient commutes with base change by its degree-zero description. Its closed fibre is \(H_k/(H_0)_k=1\). Lemma 7.24 gives \(K=1\). Hence the \(H_0\)-torsor \(H\to K=\operatorname{Spec}R\), with its identity section, identifies \(H\) with \(H_0\), with the prescribed inclusion. This proves the assertion over the complete local ring and, by faithful flatness, over the original local ring.

Finally, over a Noetherian affine base apply the local result at every prime. The ideal of \(H\) is finitely generated, as is \(N\); equality with the binomial ideal generated by \(e^n-1\) for generators of \(N\) therefore spreads from the localization to an open neighbourhood by clearing finitely many denominators in both inclusions. These neighbourhoods cover the base. The Noetherian model from the first step gives such neighbourhoods over an arbitrary affine base as well. On a nonempty overlap the two subgroups \(N\) agree: restrict to a residue field and use the uniqueness in Theorem 4.2. Thus \(N\) is locally constant. Returning to the splitting cover proves that \(H\) is of multiplicative type; Theorem 7.7 identifies its character quotient and glues it. The local binomial presentation immediately commutes with every base change, proving the final assertion. \(\square\)

This theorem supplies a proof of the fppf closed-subgroup refinement in Brian Conrad, *Reductive group schemes*, Corollary B.3.3, including arbitrary bases. Its nilpotent argument uses flat Hopf quotients and the absence of primitives in a group algebra; the subsequent affine quotient argument retains the full subgroup structure.

### 7.17. Monomorphisms into a nonaffine group

The field-level closedness theorem does not settle monomorphisms over a general base. The following arguments retain the Artinian quotient, infinitesimal and component information needed over a discrete valuation ring.

Human source: Alexander Grothendieck, *SGA 3, Exposé VIII: Groupes diagonalisables*, retyped version 1.1, 8 November 2009, [author-hosted reading copy](https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp8-8nov09.pdf). Its appendix is unrevised. The norm and component arguments below replace several intermediate appeals. Reading eligibility and mathematical proof closure are separate issues.

Write \(G[n]\) for the inverse image of the identity under the power map \([n]\). For commutative groups this is the usual multiplication kernel. In the separation lemma \(H\) need not be commutative: \(H[n]\) then means this inverse-image scheme, without asserting that the power map is a homomorphism or its fibre a subgroup.

#### Exact proof providers

- *Group schemes over a field*, Lemma 1.13: immersions and closed immersions are detected after reduction over a **nilpotent base ideal**. This does not assert that arbitrary reduction of source and target detects them.
- That lesson, Theorem 5.9: a quasi-compact monomorphism of locally finite-type groups over a field or a local Artinian ring is a closed immersion, without base flatness.
- That lesson, Proposition 5.8: the schematic image of a quasi-compact group homomorphism over a field is a closed subgroup; a reduced source is faithfully flat onto this image.
- That lesson, Lemma 7.12: a finite-type monomorphism between Noetherian schemes is an isomorphism over an open containing the generic points of its schematic image. This is not an arbitrary-base closedness criterion.
- *Quotients and torsors*, Theorem 11.1b and Theorem 11.7: scheme quotients by closed algebraic subgroups over a field, and by flat closed subgroups over a local Artinian ring, respectively. The quotient maps are fppf torsors and commute with base change. The Artinian theorem is used below only after Theorem 5.9 gives closedness.
- *Group schemes, actions and Hopf algebras*, Theorem 3.1: finite locally free commutative Cartier duality and evaluation biduality over any base.
- This lesson, Lemma 4.15: flat schematic closure over a DVR, its product property, and its inherited subgroup structure.
- *Lie algebras and smoothness of group schemes*, Theorem 4.3: Cartier's characteristic-zero smoothness theorem.
- [*Flatness criteria, dimension and the flat locus*](../../AG-FSE/src/flatness-criteria.md), Corollary 2.2: the Noetherian fibrewise flatness criterion. [*Smooth morphisms*](../../AG-FSE/src/smooth-morphisms.md), Theorem 3.1: a flat locally finitely presented morphism with smooth geometric fibres is smooth over an arbitrary base.
- [*Zariski's Main Theorem*](../../AG-MO/src/zariskis-main-theorem.md), Theorem 4.2: finite completion of a separated quasi-finite map; Theorem 5.1: proper and quasi-finite implies finite.
- [*Proper morphisms and valuative criteria*](../../AG-MO/src/proper-morphisms-and-valuative-criteria.md), Theorem 5.1 and its discrete domination argument: the Noetherian DVR criterion. Its Corollary 2.2 supplies descent of universal closedness through a surjective proper cover.
- [*Limits and Noetherian approximation*](../../AG-MO/src/limits-and-noetherian-approximation.md), Theorems 4.1 and 4.2: descent of finite-presentation objects, maps, identities, separatedness, and each **fixed** finite morphism or closed immersion. Smoothness descends by a finite standard smooth Jacobian chart cover. These facts do not descend an unspecified infinite list of properties simultaneously.

We also use the following precise dimension consequence. A finite-type flat group over a complete DVR has fibres of the same dimension. Flatness makes all irreducible components dominate the base. The generic fibre is equidimensional by translation over a field. The dimension formula over the universally catenary DVR makes every component of the special fibre have that same dimension: the uniformizer has height one in each dominating component. The relevant formula is [*Dimension of fibres*](../../AG-MO/src/dimension-of-fibres.md), Theorem 5.1, together with the principal ideal theorem. The complete DVR satisfies the required catenarity hypothesis. Constancy of the number of components is not asserted.

#### Valuation reduction and schematic dominance

**Lemma 7.26. DVR detection.** Let \(f:Y\to X\) be a finite-type monomorphism between locally Noetherian schemes over a locally Noetherian base. If all its pullbacks along maps from complete DVR spectra to that base are immersions, then \(f\) is an immersion. If all are closed immersions, \(f\) is a closed immersion.

**Proof.** A finite-type monomorphism is separated and quasi-finite. Its nonempty fibre over a field is that field's spectrum: a finite extension supplying a closed point gives a section after extension; a monomorphism with a section is an isomorphism; faithful flatness descends that conclusion. Work on an affine target open. Zariski's Main Theorem gives an open \(Y\subset T\) with \(T\to X\) finite. Replace \(T\) by the schematic closure of \(Y\), so \(Y\) is dense, and put \(B=T\setminus Y\).

If the closed image of \(B\) misses \(f(Y)\), its complement \(W\subset X\) contains \(f(Y)\), and \(T_W=Y\). The map \(Y\to W\) is then a finite monomorphism, hence a closed immersion by the finite-module argument in *Group schemes over a field*, Lemma 7.12. This gives an immersion.

Otherwise choose \(z\in B\), \(y\in Y\), with the same image \(x\). An irreducible component of \(T\) through \(z\) has its generic point in \(Y\). Discrete domination of its local domain gives a DVR curve with closed point \(z\) and generic point in \(Y\); completion preserves these properties. Its composite \(c:\operatorname{Spec}V\to X\) has a generic lift to \(Y\) and a special lift to \(Y_V\), since the nonempty special fibre of the monomorphism is the residue field's spectrum.

If \(f_V\) were an immersion, factor it as closed into an open of \(X_V\). The section defined by \(c\) lies in this open at both points. Its pulled-back ideal vanishes generically, hence vanishes in the torsion-free ring \(V\). Thus \(c\) lifts to \(Y_V\). The composite into \(T\) agrees generically with the chosen curve and has special point in \(Y\), contradicting separatedness of the finite map \(T\to X\). The contradiction proves the immersion assertion. For closedness use the Noetherian DVR criterion for properness, followed by proper quasi-finite implies finite and finite monomorphism implies closed immersion. \(\square\)

**Lemma 7.27.** A schematically dominant homomorphism \(a:F\to Q\) of finite-type groups over a field is faithfully flat, including when \(Q\) is nonreduced.

**Proof.** Its kernel \(K\) is closed, since field groups are separated. Theorem 11.1b of *Quotients and torsors* constructs the fppf quotient \(F/K\). Local representatives give a monomorphism \(F/K\to Q\); it is quasi-compact since both schemes are finite type. Theorem 5.9 of *Group schemes over a field* makes it a closed immersion. Its defining ideal pulls back to zero on \(F\), so schematic dominance makes that ideal zero. Thus \(F/K=Q\) and \(a\) is fppf. \(\square\)

#### Characteristic zero over an arbitrary base

**Theorem 7.28.** Let \(S\) be any scheme whose residue fields have characteristic zero. Let \(u:G\to H\) be a monomorphism of finite-presentation \(S\)-groups, with \(G/S\) flat. Then \(u\) is an immersion. The target need not be affine or separated over \(S\).

**Proof.** First suppose \(S\) locally Noetherian. Lemma 7.26 reduces to a complete DVR \(V\). The generic field theorem makes \(G_K\to H_K\) closed. Let \(L\subset H\) be its flat schematic closure. Lemma 4.15 factors \(u\) through \(L\), with \(G_K=L_K\). The special fibres have the same dimension. The closed inclusion \(G_k\to L_k\) therefore has underlying image a union of components: after algebraic closure and reduction, the groups are smooth, and their irreducible identity components have that common dimension.

Cartier's theorem makes the special-fibre groups themselves smooth. Their closed inclusion is consequently the induced open and closed inclusion of those components. Thus \(G_k\to L_k\) is an open immersion. The generic fibre is an isomorphism. Since \(G\) and \(L\) are \(V\)-flat, the fibrewise flatness criterion makes \(G\to L\) flat. A flat finitely presented monomorphism is an open immersion: its diagonal makes it unramified, flatness makes it étale, and an étale monomorphism is open. Its composite with the closed \(L\subset H\) is an immersion.

Now take an arbitrary affine base \(\operatorname{Spec}R\). Every positive integer belongs to no maximal ideal, so is a unit; hence \(R\) is a \(\mathbf Q\)-algebra. Cartier and the arbitrary-base fibrewise smoothness criterion make \(G/R\) smooth. Descend \(G,H,u\) and their group laws to a finitely generated \(\mathbf Q\)-subalgebra \(R_0\). Monomorphy descends by descending the inverse of the diagonal and its two inverse identities. Smoothness descends using a finite standard smooth chart cover and its finitely many unit-Jacobian identities. A common stage therefore has a smooth source and a monomorphism. Apply the Noetherian result at that stage and pull back its immersion. The affine-base results glue. Only finitely many data have been descended. \(\square\)

Closedness is false under these hypotheses: Example 4.12 applies over a base all of whose residue fields have characteristic zero.

#### The complete-DVR infinitesimal quotient

For Lemmas 7.30 through 7.34, let \(V\) be a complete DVR with uniformizer \(\pi\), fraction field \(K\), and residue field \(k\) of characteristic \(p>0\). Let \(u:G\to L\) be a monomorphism of finite-presentation flat \(V\)-groups, a generic isomorphism and a topological surjection. Assume \(G\) commutative and \(G_k\) smooth. Put

\[
 V_r=V/\pi^{r+1},\qquad G_r=G_{V_r},\qquad L_r=L_{V_r}.
\]

The group \(L\) is commutative even without assuming its separation. Its multiplication and opposite multiplication agree generically. Specially they have the same underlying point map, since \(G_k\to L_k\) is topologically surjective and \(G_k\) is commutative. Thus they have the same underlying point map everywhere. Around a source point choose a common affine target chart. Their differences on functions vanish generically and are zero by \(V\)-flatness of \(L\times_VL\). This proves equality of the multiplication maps.

The Artinian monomorphism theorem makes every \(G_r\subset L_r\) closed. The Artinian quotient theorem then gives flat groups

\[
 Q_r=L_r/G_r,\qquad L_r\longrightarrow Q_r
 \text{ an fppf }G_r\text{-torsor}.
 \tag{V.1}
\]

Their common special fibre \(Q_0\) is finite infinitesimal: the quotient has one geometric point and is finite type over \(k\). Quotient base change gives \(Q_r\times_{V_r}V_t=Q_t\), for \(t\leq r\).

Each \(Q_r\) is finite over \(V_r\). Its special fibre is affine; invariance of affineness under nilpotent thickenings makes \(Q_r=\operatorname{Spec}C_r\) affine. Lift a finite module generating set from its finite-dimensional special-fibre algebra. Its generated submodule \(N\) satisfies \(C_r=N+\pi C_r\); iteration through \(\pi^{r+1}=0\) gives \(C_r=N\). Flatness makes this finite module free over \(V_r\), of the common rank \(d=\dim_k C_0\).

Compatible lifts of a basis of \(C_0\) are bases of every \(C_r\), by Nakayama and equality of ranks. Consequently \(C=\varprojlim C_r\simeq V^d\). Finite freeness identifies the limit of the tensor products with \(C\otimes_V C\). All ring and Hopf maps pass to the limit, and their identities hold since they hold modulo every power of \(\pi\). We obtain

\[
 Q=\operatorname{Spec}C,\qquad Q/V\text{ finite locally free},
 \qquad Q_{V_r}=Q_r.
 \tag{V.2}
\]

**Lemma 7.29. Finite-flat rank annihilation.** A finite locally free commutative group \(F/S\) of constant rank \(d\) is killed by \(d\), over any base.

**Proof.** Work on an affine base and any test algebra \(B\). For \(g\in F(B)\) and a character \(\chi:F_B\to\mathbf G_{m,B}\), translation by \(g\) is an algebra automorphism sending the unit \(\chi\) to \(\chi(g)\chi\). The determinant norm is invariant under algebra automorphisms. Scalar multiplication on a rank-\(d\) module multiplies its determinant by \(\chi(g)^d\). Therefore

\[
 N(\chi)=N(\chi(g)\chi)=\chi(g)^dN(\chi).
\]

The norm of the unit \(\chi\) is a unit, so \(\chi(g)^d=1\). This holds universally, including for the universal character on the finite Cartier dual. Evaluation biduality says precisely that these characters detect \([d]_F\). Thus \([d]_F=0\). The argument glues over \(S\). \(\square\)

This supplies the commutative prerequisite and its arbitrary-base finite-flat refinement. It is not a proof of the noncommutative finite-group assertion: the latter does not admit the commutative Cartier-dual argument and its power map need not be a homomorphism.

**Corollary 7.30.** A common power \(p^a\) kills \(Q\) and every \(Q_r\).

**Proof.** Write \(d=p^a b\), with \(p\nmid b\). The finite infinitesimal algebra of \(Q_0\) has nilpotent augmentation ideal \(\mathfrak a\). On \(\mathfrak a/\mathfrak a^2\), the pullback of \([b]\) is multiplication by the nonzero residue of \(b\). It is surjective there. Lifts of a basis generate through the finite augmentation filtration, so the algebra endomorphism \([b]^*\) is surjective and hence an isomorphism. On the finite free \(V\)-module \(C\), its determinant is therefore a unit modulo \(\pi\), hence a unit in \(V\). Thus \([b]_Q\) is an automorphism. Lemma 7.29 gives \([p^ab]_Q=0\); cancelling \([b]\) gives \([p^a]_Q=0\). Base change gives the same exponent on all \(Q_r\). This proof does not need a classification or a rank formula for infinitesimal groups. \(\square\)

**Lemma 7.31.** Suppose \([p]_{G_k}\) is flat. For \(\nu\geq a\), every \(L_r[p^\nu]\) is flat over \(V_r\).

**Proof.** Since \([p^\nu]Q_r=0\), the quotient torsor factors multiplication uniquely as

\[
 L_r\xrightarrow{v_r}G_r\xrightarrow{u_r}L_r,
 \qquad v_ru_r=[p^\nu]_{G_r}.
 \tag{V.3}
\]

The image \(I\subset G_k\) of the flat finitely presented map \([p^\nu]_{G_k}\) is an open subgroup, and that map is fppf onto \(I\). The underlying image of \(v_0\) is also \(I\), by topological surjectivity of \(u_0\), so \(v_0\) factors through \(I\). Its restriction along \(G_k\to L_k\) is schematically dominant onto \(I\), making \(v_0:L_k\to I\) schematically dominant. Lemma 7.27 makes this map fppf, hence its composite into \(G_k\) flat.

Both \(L_r\) and \(G_r\) are \(V_r\)-flat. The Noetherian fibre criterion makes \(v_r\) flat. Its identity fibre is \(L_r[p^\nu]\), by monomorphy of \(u_r\), proving the claim. \(\square\)

Smoothness of \(G_k\) and finiteness of \(G_k[p]\) suffice for the flatness hypothesis just used. The reduced-source image theorem gives an fppf map to the reduced schematic image of \([p]\). The finite kernel and dimension formula give full image dimension. This closed image is therefore an induced union of components of the smooth target \(G_k\), hence open. Thus \([p]_{G_k}\) is flat, and so are its powers. No equivalence with a no-additive-subgroup structure theorem is used.

**Lemma 7.32.** Let \(G\to L\) be a topologically surjective monomorphism of finite-type commutative groups over a field of characteristic \(p>0\), and let \(Q=L/G\). For all sufficiently large \(\nu\),

\[
 1\longrightarrow G[p^\nu]\longrightarrow L[p^\nu]
 \longrightarrow Q\longrightarrow1
 \tag{V.4}
\]

is fppf exact, including the nonreduced structure.

**Proof.** The field monomorphism and quotient theorems make \(G\subset L\) closed, \(Q\) finite infinitesimal, and \(L\to Q\) fppf. Put \(A=\mathcal O_{L,e}\), with maximal ideal \(\mathfrak m\), and \(D=\mathcal O_{Q,e}\). The faithfully flat local map \(D\to A\) is injective, and \(D\) is finite dimensional over the field.

For a commutative group in characteristic \(p\),

\[
 [p^\nu]^*\mathfrak m\subset\mathfrak m^{p^\nu}.
 \tag{V.5}
\]

For completeness, this is a local assertion even when \(L\) is nonaffine. Complete at the rational identity. Iterated comultiplication is invariant under cyclic permutation of its \(p\) tensor factors. Expand in a topological vector-space basis of the completed local algebra, with \(1\) first and the other basis elements in its augmentation ideal. Diagonal pullback multiplies factors. An orbit of length \(p\) contributes \(p\) equal products, hence zero; a fixed tensor is the \(p\)-fold tensor of one basis element and contributes its \(p\)-th power. An augmentation element has zero scalar term. Thus \([p]^*\mathfrak m\subset\mathfrak m^p\) in the completion. Degreewise expansions contain only finitely many terms. Iteration gives (V.5); faithful flatness of Noetherian local completion detects membership in the finitely generated ideals and yields the assertion in \(A\).

The defining ideal of \(L[p^\nu]\) in \(A\) is consequently contained in \(\mathfrak m^{p^\nu}\), giving a map \(\mathcal O_{L[p^\nu],e}\to A/\mathfrak m^{p^\nu}\). Krull intersection gives \(\bigcap_\nu\mathfrak m^{p^\nu}=0\). The kernels of \(D\to A/\mathfrak m^{p^\nu}\) are decreasing subspaces of the finite-dimensional \(D\), with zero intersection; they are zero for all sufficiently large \(\nu\). Hence \(D\to\mathcal O_{L[p^\nu],e}\) is injective.

Since \(Q\) has one point, this makes \(L[p^\nu]\to Q\) schematically dominant. Lemma 7.27 makes it fppf. Its kernel is the schematic intersection with \(G\), precisely \(G[p^\nu]\), proving (V.4). \(\square\)

**Lemma 7.33.** In the complete-DVR situation, assume \([p]_{G_k}\) flat. There is a \(\nu_1\geq a\) such that, for every \(\nu\geq\nu_1\) and \(r\geq0\),

\[
 1\longrightarrow G_r[p^\nu]\longrightarrow L_r[p^\nu]
 \xrightarrow{w_r}Q_r\longrightarrow1
 \tag{V.6}
\]

is fppf exact.

**Proof.** Choose \(\nu_1\) from Lemma 7.32 for the special fibre, increasing it to at least \(a\). The restriction of \(L_r\to Q_r\) defines \(w_r\), with the displayed kernel. Its source is \(V_r\)-flat by Lemma 7.31 and its target is \(V_r\)-flat by construction. Its special fibre is fppf by Lemma 7.32. The Noetherian fibre criterion gives flatness. All target points lie in the special fibre, where it is surjective, so it is faithfully flat. Finite presentation follows from finite type over the Noetherian Artinian base. \(\square\)

**Lemma 7.34.** In that situation, assume also \(G[p^\nu]\) finite and \(L[p^\nu]\) separated over \(V\), for every \(\nu>0\). Then \(G\to L\) is an isomorphism.

**Proof.** Fix \(\nu\geq\max(1,\nu_1)\). The map \(G[p^\nu]\to L[p^\nu]\) is topologically surjective. This is immediate generically, and specially follows because the closed monomorphism \(G_k\to L_k\) is topologically surjective and its residue-field lifts preserve the torsion condition. The map is proper by the graph argument: its source is finite over \(V\), its target separated.

This proper surjection makes \(L[p^\nu]\to\operatorname{Spec}V\) universally closed by the proper-cover criterion. It is separated and finite type, hence proper. Its two fibres have the same underlying finite sets as those of \(G[p^\nu]\), so it is quasi-finite, hence finite.

Both finite coordinate modules are \(V\)-flat. For \(L[p^\nu]\), all reductions modulo powers of \(\pi\) are flat by Lemma 7.31. For \(G[p^\nu]\), their flatness follows by taking the identity fibres of the fppf maps (V.6). A finite \(V\)-module with all these reductions flat has no \(\pi\)-torsion: if \(\pi x=0\), freeness modulo \(\pi^{r+1}\) puts \(x\) in \(\pi^rM\) for every \(r\), and Krull intersection gives \(x=0\). Torsion-free modules over a DVR are flat.

The compatible \(w_r\) algebraize to a group map \(w:L[p^\nu]\to Q\): their coordinate algebras are finite complete \(V\)-modules, so the compatible ring and Hopf maps pass to their limits. Its restriction to \(G[p^\nu]\) is zero, since that identity holds modulo every power of \(\pi\) in finite separated modules. Its special fibre is fppf and its source and target are \(V\)-flat, so the fibre criterion gives flatness at every point of the closed fibre. Its flat locus is open. A nonempty closed subset of a finite \(V\)-scheme meets the closed fibre, so the map is flat everywhere. Its image is open by flat finite presentation and closed by properness. It contains the whole closed fibre of \(Q\), and every component of this finite \(V\)-scheme meets that fibre, so \(w\) is surjective.

Generically \(G[p^\nu]_K=L[p^\nu]_K\). The fppf map \(w_K\) has its entire source as kernel, hence \(Q_K=1\). The locally free \(Q/V\) thus has rank one and is trivial. Then \(Q_0=1\) and (V.1) makes \(G_k\to L_k\) an isomorphism. Both fibre maps of \(u\) are isomorphisms, so the fibre criterion makes \(u\) flat. This surjective flat finitely presented monomorphism is an isomorphism. \(\square\)

#### The locally Noetherian immersion theorem

**Theorem 7.35.** Let \(S\) be locally Noetherian. Let \(u:G\to H\) be a monomorphism of finite-presentation \(S\)-groups, with \(G/S\) flat. For every \(s\in S\) with residue characteristic \(p>0\), suppose over \(S_s=\operatorname{Spec}\mathcal O_{S,s}\) that

1. \(G_{S_s}\) is commutative;
2. \(G_s\) is smooth;
3. \(G_{S_s}[p^\nu]\) is finite and \(H_{S_s}[p^\nu]\) separated over \(S_s\), for every \(\nu>0\).

Then \(u\) is an immersion. The target need not be affine or separated.

**Proof.** Apply Lemma 7.26. On a complete DVR let \(L\subset H\) be the flat schematic closure of the closed generic image of \(G_K\). Then \(G\to L\) is a generic isomorphism, and the special fibres have the same dimension. The underlying closed image of \(G_k\) is therefore a union of components of \(L_k\). Delete its complementary components from that special fibre. Their complement \(L'\subset L\) is an open subgroup, with unchanged generic fibre and a topologically surjective \(G\to L'\).

In special residue characteristic zero, Cartier makes both special groups smooth, and the DVR argument in Theorem 7.28 gives the desired immersion. Otherwise the DVR map factors through the local scheme at its special-point image \(s\). The hypotheses give commutative \(G\), smooth \(G_k\), and finite \(G[p^\nu]\). The separatedness of \(H[p^\nu]\) passes to the closed \(L[p^\nu]\subset H[p^\nu]\) and its open \(L'[p^\nu]\). Smoothness and finiteness of \(G_k[p]\) give flatness of \([p]_{G_k}\), by the dimension argument following Lemma 7.31. Lemma 7.34 therefore makes \(G\to L'\) an isomorphism. Composition with open \(L'\subset L\) and closed \(L\subset H\) is an immersion. Lemma 7.26 concludes. \(\square\)

Only one sufficiently large \(p\)-power is ultimately used on each DVR. Its exponent is chosen after constructing that DVR's infinitesimal quotient and applying Krull intersection. This alone does not supply a uniform exponent on an approximation.

#### Components and the corrected closed-immersion theorem

**Lemma 7.36.** Let \(J/k\) be a finite-type commutative group. Let \(n\) be the order of its finite étale component group \(\pi_0(J)\). If \([n]:J^0\to J^0\) is surjective, then \(J[n]\to\pi_0(J)\) is surjective on underlying spaces. This holds in particular if \(J^0\) is smooth and \(J^0[n]\) finite.

**Proof.** Over an algebraic closure, each component has a rational point \(h\), with \(nh\in J^0(k)\). Choose \(a\in J^0(k)\) such that \(na=nh\). Then \(h-a\in Jn\) lies in the same component. Field descent gives the assertion. For the final clause, the reduced-source image theorem makes \(J^0\) fppf onto its reduced schematic image under \([n]\). The finite kernel gives full image dimension, making that image all of the connected irreducible \(J^0\). \(\square\)

The full no-additive-subgroup formulation, including nonaffine and nonreduced commutative groups over arbitrary fields, is proved in [Quotients and torsors, Appendix B, Theorems B.5–B.7](quotients-and-torsors.md#appendix-b-pair-forms-normalizers-and-groups-without-additive-subgroups). Those proofs establish the semiabelian geometric reduced identity component, divisibility of \(J^0(\bar k)\), and finite faithfully flat surjectivity of the kernel \(J[n]\to\pi_0(J)\) for \(n=\deg\pi_0(J)\), without requiring \(n\) prime to the characteristic. Lemma 7.36 retains the precise finite-kernel argument used below.

**Lemma 7.37.** Let \(H\) be a finite-presentation group over a complete DVR \(V\). If every inverse-image scheme \(H[n]\) is separated over \(V\), then \(H/V\) is separated.

**Proof.** Let \(E\subset H\) be the flat schematic closure of the generic identity subgroup. Its generic dimension is zero, hence so is its special-fibre dimension. Its geometric special fibre has finitely many points forming an ordinary finite group. Choose a positive integer \(m\) killing that group, for example its order. The power map \([m]:E\to E\) and the identity-valued map have the same underlying point map, generically and specially. Their equality as scheme morphisms follows by the common-affine-chart density argument for the \(V\)-flat \(E\). Thus \(E\to H\) factors through \(H[m]\), and \(E\to H[m]\) is closed as the base change of \(E\subset H\). Hence \(E/V\) is separated. Its closed identity section contains the whole generic fibre; schematic density of that fibre makes this section all of \(E\).

Apply this argument to every complete-DVR pullback to test separatedness of \(H/V\). Two sections agreeing generically have a difference factoring through the flat closure of the generic identity: functions in its ideal pull back to zero because the source ring is torsion free. That closure is the identity section by the preceding argument, so the sections agree. The Noetherian DVR separation criterion proves separatedness. \(\square\)

The finite ordinary point group supplies only the common underlying point map. Generic schematic density proves the power-map identity on the flat model. No scheme assertion about a nonreduced special fibre is inferred from its point group alone.

**Theorem 7.38.** Let \(S\) be locally Noetherian. Let \(u:G\to H\) be a monomorphism of finite-presentation \(S\)-groups, with \(G/S\) flat. At **every** \(s\in S\), suppose over \(S_s=\operatorname{Spec}\mathcal O_{S,s}\) that

1. \(G_{S_s}\) is commutative and \(G_s\) smooth;
2. \(G_{S_s}[n]\) is finite and \(H_{S_s}[n]\) separated, for every \(n>0\).

Then \(u\) is a closed immersion.

**Proof.** Theorem 7.35 gives an immersion. The Noetherian properness criterion reduces closedness to complete DVR pullbacks. Let \(L\subset H\) be the flat closure of the generic image. All torsion-kernel separation hypotheses persist under these pullbacks. Lemma 7.37 makes \(H\), and hence \(L\), separated. Since \(L_K=G_K\) is commutative, separation and schematic density of the flat \(L\times_V L\) make \(L\) commutative.

The immersion \(G\to L\) is open: in its factorization as closed into an open of \(L\), the ideal vanishes generically, hence is zero because the ambient open is \(V\)-flat. Thus \(G_k\subset L_k\) is open and closed and contains the identity component. Smoothness of \(G_k\) makes \(L_k\) smooth, since all its geometric components are translates of the same smooth identity component.

For every \(n>0\), the kernel of \([n]\) on \(G_k^0=L_k^0\) is finite. The image theorem and dimension formula make multiplication on that identity component fppf and surjective. On the full smooth \(L_k\) its image is an induced union of components, hence open, so \([n]_{L_k}\) is flat. The same argument on \(L_K=G_K\) applies: \(G/V\) is smooth by flatness and smoothness of its fibres, and \(G_K[n]\) finite. The fibre criterion makes \([n]_L\) flat; its identity fibre \(L[n]\) is \(V\)-flat.

The map \(G[n]\to L[n]\) is proper because its source is finite over \(V\) and its target separated. Its closed image contains the generic fibre of \(L[n]\), dense by flatness, so it is topologically surjective, including on the special fibre. Choose \(n=|\pi_0(L_k)|\). Lemma 7.36 makes \(L_k[n]\to\pi_0(L_k)\) surjective. Thus the open subgroup \(G_k\), already containing \(L_k^0\), meets every component, and equals \(L_k\). The generic fibres also coincide. The fibre criterion makes \(G\to L\) flat, so this surjective monomorphism is an isomorphism. Its composite \(G=L\subset H\) is closed. The DVR criterion concludes globally. \(\square\)

The all-point quantifier is essential. If torsion finiteness is required only at positive-characteristic points, all such conditions are vacuous over a base all of whose residue fields have characteristic zero, and Example 4.12 disproves closedness. Commutativity and special-fibre smoothness above are also explicitly imposed at every point. This verified scope does not assert an additional characteristic-zero noncommutative component theorem.

#### Multiplicative type over any base, with separated target

**Corollary 7.39.** Let \(S\) be any scheme, \(G/S\) a finite-presentation group of multiplicative type, and \(H/S\) a separated group of finite presentation. Every monomorphism \(u:G\to H\) is a closed immersion. The target need not be affine.

**Proof.** Closed immersions descend fpqc. The relative character theorem supplies an étale cover on which \(G=D_S(M)\), for finitely generated \(M\). Work on an affine member \(\operatorname{Spec}R\). The abelian-group structure theorem writes

\[
 G=T\times_S F,\qquad T=\mathbf G_{m,S}^{\,r},
\]

with \(F\) finite locally free diagonalizable. Its order need not be invertible.

First prove \(u_T:T\to H\) closed. Descend \(H,u_T\), the group laws and the inverse of the monomorphism's diagonal to a finitely generated \(\mathbf Z\)-subalgebra \(R_0\). Descend separatedness of \(H\). Keep the source at every stage equal to the split \(\mathbf G_m^r\). Its smoothness, commutativity and flatness are intrinsic at every stage, as is the finiteness of

\[
 T[n]=\mu_n^{\,r}\quad(n>0).
\]

Every \(H[n]\) is separated because \(H\) is separated. Thus Theorem 7.38 applies on the Noetherian model: its infinite list of source-kernel conditions is verified by explicit torus equations on that model, not descended from an infinite list at the limit. Pulling back proves \(u_T\) closed over \(R\).

Now take any valuation-ring diagram for \(u:T\times F\to H\), with valuation ring \(A\), fraction field \(K\), generic pair \((t_K,f_K)\), and prescribed image \(h\in H(A)\). Properness of the finite \(F\) extends \(f_K\) uniquely to \(f\in F(A)\). The element

\[
 h\,u_F(f)^{-1}\in H(A)
\]

extends \(u_T(t_K)\). Properness of the closed immersion \(u_T\) extends \(t_K\) uniquely to \(t\in T(A)\). The pair \((t,f)\) supplies the lift, unique by monomorphy. The general valuative criterion makes \(u\) proper; it is finite type and separated, as required. A proper monomorphism is quasi-finite, hence finite, and a finite monomorphism is closed. Descent along the splitting cover concludes. \(\square\)

The finite non-smooth factor is handled by properness. This proof neither assumes \([p]\) on \(\mu_p\) flat nor needs a scheme quotient of an arbitrary relative nonaffine target by that factor. It does not use this lesson's Lemma 7.24: that lemma assumes a subgroup already **closed** in a diagonalizable group, and cannot prove the closedness here.

#### Finite approximation and full arbitrary-base conclusions

The locally Noetherian proofs above remain separate inputs. The following finite bounds recover the infinitely many torsion conditions from finitely many specified properties and establish the arbitrary-base theorems, including a nonseparated target for multiplicative type.

#### Proof inputs and scope

The following existing complete proofs are used with their actual hypotheses.

- *Group schemes over a field*, Theorem 2.3: geometric connected components of a finite-type field group are irreducible and are translates of the identity component; Proposition 5.8: reduced-source schematic-image faithful flatness; Theorem 5.9: quasi-compact field and local-Artinian group monomorphisms are closed, including nilpotents; Lemma 7.12: a finite monomorphism is closed.
- *Quotients and torsors*, Theorems 11.1b and 11.7: the field and flat-subgroup Artinian quotient theorems, with their fppf and base-change assertions. These remain the inputs to Lemmas 7.31–7.34 in the current lesson.
- The current lesson, Lemma 4.15: flat schematic closure over a DVR; Lemma 7.26: immersion and closedness detection by complete DVR pullbacks on a Noetherian base; Lemmas 7.31–7.34: the complete-DVR infinitesimal quotient argument; Lemma 7.36: finite torsion meets every component when multiplication is surjective on the identity component; Corollary 7.39: multiplicative-type closedness into a separated target over an arbitrary base; Theorems 4.4–4.5 and 7.7: the split equations, finite-kernel computations and étale splitting for multiplicative type.
- [*Flatness criteria*](../../AG-FSE/src/flatness-criteria.md), Corollary 2.2, supplies the Noetherian fibrewise flatness criterion. [*Smooth morphisms*](../../AG-FSE/src/smooth-morphisms.md), Theorem 3.1, supplies its arbitrary-base smoothness counterpart.
- [*Zariski's Main Theorem*](../../AG-MO/src/zariskis-main-theorem.md), Theorem 4.2, supplies a finite completion of a separated quasi-finite morphism. [*Proper morphisms and valuative criteria*](../../AG-MO/src/proper-morphisms-and-valuative-criteria.md), Theorem 5.1, supplies the Noetherian DVR criterion. The separatedness criterion is [*Valuation rings and separatedness*](../../AG-MO/src/valuation-rings-and-separatedness.md), Theorem 5.2. [*Étale morphisms and their local structure*](../../AG-FSE/src/etale-morphisms-and-their-local-structure.md), Theorem 4.1, identifies flat finitely presented monomorphisms with open immersions.
- [*Limits and Noetherian approximation*](../../AG-MO/src/limits-and-noetherian-approximation.md), Theorems 4.1–4.2, supplies descent of finitely presented objects, maps, identities, and each specified finite map or separated map. Smoothness is descended by finitely many standard smooth charts and their Jacobian identities. An immersion descends by descending a quasi-compact open containing its image and the closed immersion into that open.
- [*Dimension of fibres*](../../AG-MO/src/dimension-of-fibres.md), Theorem 5.1, supplies the dimension formula over a universally catenary base. Its use below is over a complete DVR. A flat finite-type group there has pure fibre dimension equal to its generic dimension: all total-space components dominate; translation makes the generic fibre equidimensional; the dimension formula and the principal ideal theorem give the special-fibre assertion.

The finite numerical bounds and separation arguments needed in addition to these inputs are proved here. No infinite collection of conditions is descended at once.

#### A finite equation bound

**Lemma 7.40.** Fix a finite-presentation scheme over a Noetherian affine base and a finite affine-chart presentation. There is an integer \(B\geq1\) bounding the number of geometric irreducible components of every fibre. If all fibres are groups, this also bounds their geometric connected components.

**Proof.** On an affine chart choose generators and finitely many polynomial equations \(f_1,\ldots,f_a\). Put

\[
 b=\prod_{i=1}^a\max(1,\deg f_i).
 \tag{AB.1}
\]

Every field specialization of that chart has at most \(b\) irreducible components. Here is the elementary degree argument, including components of different dimensions. Start with projective space, of degree one, and homogenize the equations. At a step, retain every existing irreducible component contained in the new hypersurface; intersect every other component with it. A nonzero hypersurface of degree \(d\) on an integral projective variety of degree \(c\) has pure codimension one and total component degree at most \(dc\), counting each component once. Indeed multiplication by its equation gives the exact sequence of graded coordinate modules

\[
0\longrightarrow A(-d)\longrightarrow A
 \longrightarrow A/(f)\longrightarrow0.
\]

Taking eventual Hilbert polynomials subtracts \(P_A(n-d)\) from \(P_A(n)\), whose leading coefficient gives degree \(dc\). Each minimal component has positive integral generic multiplicity, so its degree contributes at least once. Purity follows from the principal ideal theorem and catenarity of finite-type field algebras. The Hilbert polynomial assertion itself follows by induction on the polynomial variables: the kernel/cokernel exact sequence for multiplication by the last variable gives a Hilbert series with denominator a power of \(1-z\), hence an eventual polynomial. Thus no smoothness or complete-intersection hypothesis is required.

Retaining contained components and discarding redundant components cannot increase the sum of degrees. Each step therefore multiplies that sum by at most \(\max(1,d)\). Components in the affine chart are obtained by discarding components at infinity, so their number is bounded by (AB.1). Sum these bounds over the finite affine cover. Every global fibre component meets a chart and supplies a chart component; the sum bounds their number. For a geometric field group its connected components are irreducible, by the field component theorem. \(\square\)

These bounds are preserved by every subsequent change of base: they concern the fixed equations, not just the original base's residue fields.

#### What a failure of separation can look like on a trait

**Lemma 7.41. Component injection for the closure of the identity.** Let \(V\) be a complete DVR and \(J/V\) a flat group of finite presentation. Let \(E\subset J\) be the flat schematic closure of the generic identity. Then \(E/V\) is étale, with generic fibre one point, and

\[
 E_{\bar k}(\bar k)\longrightarrow\pi_0(J_{\bar k})
 \tag{AB.2}
\]

is injective as a homomorphism of ordinary finite groups. No separation or commutativity of \(J\) is assumed.

**Proof.** Lemma 4.15 makes \(E\) a closed flat subgroup. Its fibres have dimension zero by the complete-DVR dimension formula. Choose an affine neighbourhood of its special identity. Its algebra \(A\) injects into the generic-fibre algebra \(K\), because it is torsion free. The identity section gives a retraction \(A\to V\), whose generic extension is the identity of \(K\). Thus the image of \(A\) in \(K\) is precisely \(V\). This neighbourhood is \(\operatorname{Spec}V\). The special fibre is smooth at its identity, hence at every geometric point by translation; its dimension is zero. The generic fibre is also étale. Flatness and the fibrewise smoothness criterion make \(E/V\) étale, of relative dimension zero.

Pass faithfully flatly to a complete DVR with algebraically closed residue field. One can first strictly henselize and then complete; both operations preserve the closure because its closed flat model has the specified generic fibre. Every special point \(a\) of \(E\) lifts to a section, using an étale neighbourhood and Hensel's lemma. Suppose \(a\) belongs to \(J_k^0\). Choose an affine open \(U\subset J\) meeting the identity. Its intersection with the irreducible \(J_k^0\) is nonempty and dense. This open and its translate by \(a^{-1}\) meet. Consequently there is a special point \(x\) with \(x,ax\in U\).

On \(W=U\cap a^{-1}U\), translation by the lifted section and the identity both map into the affine \(U\), and agree generically. The open \(W\) is \(V\)-flat, so its generic fibre is schematically dense. The two maps therefore agree on \(W\). In the special fibre \(ax=x\), whence \(a=e\) by cancellation. The kernel in (AB.2) is trivial. This proves injectivity. \(\square\)

**Lemma 7.42. A single power controls separation of all \(p\)-power kernels.** Let \(J\) be a commutative flat finite-presentation group on a Noetherian base, with at most \(B\) geometric components in each fibre. Let \(p\) be a prime and choose \(N\) with \(p^N>B\). If \(J[p^N]\) is separated, then every \(J[p^\nu]\) is separated.

**Proof.** Test uniqueness on a complete DVR \(V\) over the base. Let \(E\) be the closure of the generic identity in \(J_V\). Lemma 7.41 makes its special point group a subgroup of a group of order at most \(B\). Every element of its \(p\)-primary subgroup is killed by \(p^N\).

The subgroup \(E[p^N]\) is étale: the equalizer of two maps between étale schemes is open in the source. It is closed in \(J_V[p^N]\), since \(E\subset J_V\) is closed, so it is separated. Its closed identity section contains its entire generic fibre, which is schematically dense by flatness. Hence \(E[p^N]=1\), and its special point group has no nontrivial \(p\)-primary element. For every \(\nu\), \(E[p^\nu]\) then has just the identity in both fibres. The affine identity neighbourhood in the proof of 7.41 contains all its points, so \(E[p^\nu]=1\).

If two \(V\)-sections of \(J[p^\nu]\) agree generically, their difference factors through \(E\): its defining functions vanish generically in the torsion-free ring \(V\). Commutativity makes this difference \(p^\nu\)-torsion. It is therefore zero. The Noetherian DVR separatedness criterion proves the assertion. \(\square\)

The same argument works for a group over a complete DVR when the component bound is available after all complete-DVR pullbacks. It will be used for the cut flat closure of a generic image, whose fibre components coincide with those of the source.

#### Recognizing an infinite torsion condition from finite data

**Lemma 7.43. Finite recognition of all \(p\)-power kernels.** Let \(G\) be a smooth commutative finite-presentation group over a Noetherian affine base. Assume \(G[p]\) finite. Choose bounds

\[
\begin{gathered}
\#\pi_0(G_{\bar s})\leq B,\\
\operatorname{rank}G[p]\leq D,\\
B,D\geq1.
\end{gathered}
\]

Choose \(N\geq1\) such that

\[
p^N>B,\qquad (1+1/D)^N>B.
\tag{AB.3}
\]

If \(G[p^N]\) is finite, then \(G[p^\nu]\) is finite for every \(\nu>0\).

**Proof.** On a geometric fibre the finite kernel of \([p]\) makes its schematic image have full dimension. The reduced-source image theorem makes multiplication faithfully flat onto that reduced image. Since the fibre group is smooth, its image is an induced union of components, hence open. Multiplication by \(p\), and thus by every \(p^\nu\), is flat on each fibre. The fibrewise criterion makes these maps flat over the base. Their identity fibres are flat and quasi-finite. In particular the finite \(G[p]\) and \(G[p^N]\) are locally free. The latter's separation, Lemma 7.42 and (AB.3) make every kernel separated.

For a geometric fibre \(t\), put \(d_t=\deg([p]:G_t^0\to G_t^0)\). The identity-component map is surjective by its finite kernel and the dimension argument. It is finite: it is an fppf torsor under the finite kernel, and finiteness descends from that torsor's finite trivializations. Thus \(1\leq d_t\leq D\). Let \(A_t=\pi_0(G_t)\), and write \(c_t\) for the order of its \(p\)-primary subgroup. For \(\nu\geq N\), its \(p^\nu\)-torsion has stabilized because \(|A_t|\leq B<p^N\). Every component killed by \(p^\nu\) contributes a translate of the identity-component kernel. Iteration of the finite map on \(G_t^0\) consequently gives

\[
\operatorname{length}G_t[p^\nu]=d_t^\nu c_t,
\qquad 1\leq c_t\leq B.
\tag{AB.4}
\]

Pull back to any complete DVR, with generic and special geometric fibres \(\eta,s\). Finite local freeness of \(G[p^N]\) gives

\[
d_\eta^N c_\eta=d_s^N c_s.
\tag{AB.5}
\]

Two different integers between one and \(D\) have a larger/smaller ratio at least \(1+1/D\). Equations (AB.3) and (AB.5), with \(c_\eta,c_s\leq B\), exclude different \(d_\eta,d_s\). Therefore they, and then the \(c\)'s, are equal. Equation (AB.4) gives equal generic and special lengths for every \(\nu\geq N\).

A separated, quasi-finite, flat scheme \(X/V\) with these equal fibre lengths is finite. To see this, put it as an open in a finite completion \(T/V\) by Zariski's Main Theorem, and replace \(T\) by the flat closure of \(X_K\). The open restriction of that closure is \(X\), since \(X\) is flat. The finite flat \(T\) has special length equal to its generic length, already the length of \(X_s\). An open subscheme of this zero-dimensional special fibre with that full length is the entire fibre. Both fibres of \(T\) lie in \(X\), so \(T=X\).

Thus every trait pullback of \(G[p^\nu]\), \(\nu\geq N\), is finite. The Noetherian valuative criterion makes the original quasi-finite separated map proper, hence finite. If \(\nu<N\), its kernel is closed in the finite \(G[p^N]\): restrict multiplication to this finite commutative group and take the inverse image of its closed identity. These are exactly the smaller kernels. They too are finite. \(\square\)

The bound \(B\) comes from 7.40. After \(G[p]\) has descended as a finite map, \(D\) is the largest of its finitely many locally constant ranks. Both bounds concern one fixed model and survive later base change. The argument does not require the degree of a finite \(p\)-group to have been classified as a power of \(p\).

**Lemma 7.44. Finite immersion criterion.** In the setting of 7.43, assume additionally that every residue field of the base has characteristic zero or \(p\), and let \(u:G\to H\) be a monomorphism of finite-presentation groups. If \(G[p^N]\) is finite and \(H[p^N]\) separated, with \(N\) chosen by (AB.3), then \(u\) is an immersion. The target can be nonaffine and nonseparated.

**Proof.** 7.43 gives every source \(p\)-power kernel finite. Apply complete-DVR detection, Lemma 7.26. Form the flat closure \(L\subset H_V\) of the closed generic image. As in the existing DVR proof, the closed special image of \(G_k\) is a union of components of \(L_k\). Delete its complementary special components to obtain the open subgroup \(J\subset L\). Then \(G_V\to J\) is a generic isomorphism and topologically surjective. The equal-underlying-map and flat-density argument at the start of the existing infinitesimal quotient proof makes \(J\) commutative, without first assuming separation.

Its special components coincide with those of \(G_k\), and its generic components with those of \(G_K\). The same is true after further complete-DVR pullback; a pullback factoring through a field is already separated. Thus the component bound \(B\) applies to the separation argument 7.42. Since \(J[p^N]\) is an open of the closed \(L[p^N]\subset H_V[p^N]\), it is separated. Every \(J[p^\nu]\) is separated.

If the special residue characteristic is \(p\), Lemma 7.34 now makes \(G_V\to J\) an isomorphism. In characteristic zero both special field groups are smooth by Cartier's theorem; their topologically surjective closed inclusion is an isomorphism, and the existing argument in Theorem 7.28 makes \(G_V\to J\) an isomorphism. The assumed prime scope ensures these are the only cases. Composition with \(J\subset L\subset H\) is an immersion, and DVR detection concludes. \(\square\)

The prime restriction in 7.44 is intentional. A fixed \(p\)-power condition alone cannot supply the missing torsion information at another residue prime. The next theorem makes the local reduction without such an assumption on the original base.

#### The arbitrary-base immersion theorem

**Theorem 7.45.** Let \(S\) be any scheme and \(u:G\to H\) a monomorphism of finite-presentation \(S\)-groups, with \(G/S\) flat. At every \(s\) of residue characteristic \(p>0\), suppose on \(S_s=\operatorname{Spec}\mathcal O_{S,s}\) that

1. \(G_{S_s}\) is commutative and \(G_s\) is smooth;
2. \(G_{S_s}[p^\nu]\) is finite and \(H_{S_s}[p^\nu]\) separated for every \(\nu>0\).

Then \(u\) is an immersion, with no affine or separated hypothesis on \(H\).

**Proof.** Work locally on an affine base \(S=\operatorname{Spec}R\). At a point \(s\) of residue characteristic \(p\), flatness and special-fibre smoothness make the source smooth at the identity on \(S_s\). The inverse image of its smooth locus under the identity is an open containing the closed point of this local base, hence the whole local base. Translation on geometric fibres and the fibrewise smoothness criterion make the whole \(G_{S_s}\) smooth. These finitely presented smooth charts, commutativity, and the fixed finite map \(G[p]\) spread to a neighbourhood of \(s\).

To avoid other residue primes during approximation, first work on \(S_s\). Its ring is a \(\mathbf Z_{(p)}\)-algebra, so use finitely generated \(\mathbf Z_{(p)}\)-subalgebras as Noetherian stages. Every stage has only characteristic \(p\) and characteristic-zero residue fields. Descend \(G,H,u\), the group laws, smoothness, commutativity, and finiteness of \(G[p]\). Monomorphy descends by descending the inverse of its diagonal and the two inverse identities. Choose \(B,D,N\) on this fixed stage as in 7.43. Only now descend the two specified properties: finiteness of \(G[p^N]\) and separation of \(H[p^N]\). They hold over \(S_s\) by assumption. At one common later stage they hold, and the same bounds \(B,D\) still apply. Lemma 7.44, in its stated prime scope, proves that stage map an immersion. Pull it back to \(S_s\).

At a characteristic-zero point the local ring is a \(\mathbf Q\)-algebra, and Theorem 7.28 applies. Finally an immersion on \(S_s\) spreads to a neighbourhood of \(s\). Explicitly its image lies in a quasi-compact open of the target: take finitely many target neighbourhoods from its closed-into-open factorization, since the source is quasi-compact. Such an open descends along the localization limit, and so does the closed immersion into it, by the finite-presentation descent theorem. These base neighbourhoods cover \(S\). Being an immersion is local for an open cover of the target, so the local conclusions give the global conclusion. \(\square\)

Only \(G[p]\), \(G[p^N]\) and \(H[p^N]\) were descended at a positive-characteristic point. The infinitely many conditions were recovered by 7.42–7.43 on that model.

#### A uniform bound for closures of generic images

**Lemma 7.46.** Fix a finite-presentation monomorphism \(u:G\to H\) over a Noetherian affine base, with \(G\) smooth. There is \(C\geq1\), preserved by subsequent base change, such that for every map from a complete DVR \(V\) to the base, the flat closure \(L\subset H_V\) of \(u(G_K)\) has at most \(C\) geometric special components.

**Proof.** Choose finitely many affine charts \(V_b\) of \(H\), and finitely many affine charts \(U_{ab}\) covering each \(u^{-1}(V_b)\). Fix algebra generators and finite equations for these charts and polynomial representatives for the chart maps. In affine space on the source and target generators, the graph of \(U_{ab}\to V_b\) is defined by the source equations and the equations \(y_j-q_j(x)=0\). The degree-cutting proof of 7.40 bounds the sum of degrees of its geometric fibre components by a constant \(c_{ab}\).

The generic field monomorphism theorem makes \(G_K\to H_K\) closed. The image of each \(U_{ab,K}\) is open in that closed image. Projecting its graph onto the target coordinates is therefore generically an isomorphism on every component. The degree of the reduced projective closure of its image is at most the graph's degree. To verify this familiar projection inequality, intersect the image with a general linear subspace of complementary codimension, avoiding its missing open boundary. Its degree counts this zero-dimensional slice with multiplicities. Pull back those linear equations to the projective graph closure. Every image slice point has a preimage, and repeated linear cutting, as in 7.40, bounds the degree of the isolated intersection points by the graph degree; components in the centre of projection only increase the latter bound. The generically isomorphic projection preserves the slice multiplicities. This proves the inequality.

Thus the projective closure in target-coordinate projective space of \(u(G_K)\cap V_{b,K}\) has degree at most \(c_b=\sum_a c_{ab}\), after algebraic closure of \(K\). It is pure-dimensional because a smooth field group is pure-dimensional and its open restrictions have that same dimension.

Take its schematic closure \(P_b\) in projective space over \(V\). Its homogeneous coordinate module is torsion free in each degree, by saturation with respect to the uniformizer. Those degree pieces are finite free over \(V\); hence their generic and special dimensions, and consequently their eventual Hilbert polynomials, agree. The special fibre has degree equal to the generic one. It is pure-dimensional: all components of \(P_b\) dominate, and the complete-DVR dimension formula gives the same dimension to every minimal special component. Each such component has degree at least one and positive generic multiplicity, so there are at most \(c_b\) of them. On the affine target chart, this flat closure is exactly \(L\cap V_{b,V}\), by uniqueness in Lemma 4.15. Every component of \(L_{\bar k}\) meets some such chart. Therefore \(C=\max(1,\sum_b c_b)\) works.

The construction uses only the fixed finite chart equations and graph equations. Its estimates hold over arbitrary field extensions and remain the same at later stages. \(\square\)

**Lemma 7.47. Finite closedness criterion.** In 7.46 suppose also that \(G\) is commutative and \(u\) an immersion. Put \(M=C!\). If \(G[M]\) is finite and \(H[M]\) separated, then \(u\) is closed.

**Proof.** Pull back to a complete DVR and form \(L\). The immersion \(G_V\to L\) is open: in a closed-into-open factorization its ideal vanishes generically in the flat ambient open, hence vanishes. Thus \(G_k\) is an open subgroup of \(L_k\), containing its identity component. It is smooth, and translation makes all geometric components of \(L_k\) smooth.

First show \(L/V\) separated. On every further dominating complete-DVR pullback, 7.41 embeds the special group of the closure \(E\) of the generic identity into \(\pi_0(L_{\bar k})\), whose order is at most \(C\) by 7.46. Its ordinary finite group is killed by \(M=C!\). Generic and special power maps on \(E\) therefore have the same underlying map as the identity-valued map. Around any point choose a common affine target chart; equality of the maps follows from flat generic schematic density. Thus \(E\subset L[M]\). This closed subscheme is separated because \(L[M]\subset H[M]\) is closed. Its closed identity contains the dense generic fibre, so \(E=1\). Sections of \(L\) agreeing generically have difference factoring through \(E\), hence agree. A pullback factoring through a fibre field is already separated. The DVR criterion proves separation. Generic commutativity then extends to \(L\) using its closed diagonal and flatness of \(L\times_VL\).

On \(G_k^0=L_k^0\), the kernel of \([M]\) is finite, since it is a closed subgroup of the finite \(G_k[M]\). The reduced-source image and dimension argument makes \([M]\) surjective and fppf on that identity component, and flat onto an open union of components on \(L_k\). The generic-fibre statement follows in the same way from \(L_K=G_K\). The fibrewise criterion makes \([M]_L\) flat, so \(L[M]\) is \(V\)-flat.

The map \(G[M]\to L[M]\) is proper: its source is finite over \(V\), and its target separated. Its closed image contains the generic fibre of the flat \(L[M]\), so it is topologically surjective. Since \(|\pi_0(L_{\bar k})|\leq C\), multiplication by \(M\) kills that component group. Surjectivity of \([M]\) on \(L_k^0\) means every component has an \(M\)-torsion point: subtract an \(M\)-division of the \(M\)-multiple of a representative. Hence the open subgroup \(G_k\) meets every component. It contains \(L_k^0\), so it equals \(L_k\), with the full smooth scheme structures. The generic fibres coincide too. The fibrewise criterion makes \(G_V\to L\) flat; a surjective flat finitely presented monomorphism is an isomorphism. Therefore \(G_V\to H_V\) is closed. Lemma 7.26 concludes over the Noetherian base. \(\square\)

#### Closedness over an arbitrary base and the quantifier correction

**Theorem 7.48.** Let \(S\) be arbitrary and \(u:G\to H\) a monomorphism of finite-presentation \(S\)-groups, with \(G/S\) flat. At **every** \(s\in S\), suppose on \(S_s\) that \(G\) is commutative, \(G_s\) smooth, and for every \(n>0\), \(G[n]\) finite and \(H[n]\) separated. Then \(u\) is a closed immersion.

**Proof.** Theorem 7.45 first gives an immersion. Fix \(s\). As in that theorem, \(G_{S_s}\) is smooth. Descend the finite-presentation data, smoothness, commutativity, monomorphy and this immersion to a finitely generated \(\mathbf Z\)-algebra. Choose the finite chart/graph bound \(C\) there from 7.46, and put \(M=C!\). Descend only the specified finiteness of \(G[M]\) and separation of \(H[M]\) to a common later stage. Its component bound remains \(C\). Lemma 7.47 makes its map closed. Pull back to \(S_s\), and spread that closed immersion to a neighbourhood of \(s\) by fixed-property descent. The resulting base neighbourhoods cover \(S\), and closed immersions are local on the target. \(\square\)

**Example 7.49. The positive-characteristic-only closedness statement is false.** Take \(k=\mathbf Q\), \(S=\operatorname{Spec}k[t]\), \(U=D(t)\), and the constant group

\[
H=(\mathbf Z/2)_S=S\amalg S,
\qquad G=S\amalg U\subset H,
\]

with all of the identity component and only \(U\) in the other component. Multiplication of two nonidentity sections is defined over \(U\) and lands in the identity component; the other products and inversion restrict from \(H\). Hence \(G\) is an open subgroup. It is commutative, smooth, separated, flat and of finite presentation over \(S\), and \(G\to H\) is a monomorphism. Every residue field of \(S\) has characteristic zero, so conditions quantified only at positive-characteristic points hold vacuously, even when they mention all positive integers. Nevertheless the image on the nonidentity component is the proper dense open \(D(t)\), so the map is not closed. Also \(G[2]=G\) is not finite over \(S\): its nonidentity component is not universally closed, since its image \(D(t)\) is not closed.

This proves the exact failure of the printed VIII 7.12 quantifier. It does **not** give a field counterexample; finite-type group monomorphisms over a field are closed by Theorem 5.9. The corrected all-point theorem 7.48 supplies full arbitrary-base closedness under the hypotheses actually used by the component proof. It asserts no unproved noncommutative characteristic-zero variant.

#### Multiplicative type with a nonseparated target

**Lemma 7.50.** Let \(V\) be a complete DVR, \(G/V\) a finite-presentation group of multiplicative type, and \(a:G\to J\) a monomorphism into a flat finite-presentation group, generically an isomorphism and topologically surjective. Then \(J\) is separated and \(a\) is an isomorphism.

**Proof.** The common-underlying-map and flat-density argument already used in the infinitesimal quotient construction makes \(J\) commutative. To prove separation, test all complete-DVR pullbacks. Those factoring through a field are separated. On a dominating pullback the generic-isomorphism and topological-surjection conditions persist. It suffices to show that the closure \(E\) of its generic identity is the identity section.

Work faithfully flatly with algebraically closed residue field \(k\), of characteristic \(p\), with \(p=0\) allowed. The special component group of a multiplicative-type group has order prime to \(p\) when \(p>0\): after splitting, write \(G_k=D_k(\mathbf Z^r\oplus A)\); the \(p\)-primary diagonalizable factor is connected, and the prime-to-\(p\) factor is finite étale. Theorem 4.4 proves these facts from the equations. Topological surjectivity of the closed special-fibre monomorphism identifies \(\pi_0(G_{\bar k})\) with \(\pi_0(J_{\bar k})\). 7.41 therefore makes \(E_k\) a finite ordinary group of order prime to \(p\). Choose \(m\) prime to \(p\) killing it; in characteristic zero take any positive killing integer. Then \(m\) is a unit in \(V\), and \(G[m]\) is finite étale by the diagonalizable kernel equations.

We claim \(J[m]=G[m]\). First, for a finite-type commutative field group and an invertible integer \(m\), its \(m\)-kernel is finite étale. At the identity, \([m]^*\) acts by the unit \(m\) on the augmentation cotangent space. Nakayama makes the kernel's local augmentation ideal zero. Translation treats every geometric kernel point, giving a zero-dimensional geometrically reduced kernel, hence finite étale. Thus both special kernels are finite étale. Topological surjectivity of \(G_k\to J_k\) makes \(G_k[m]\to J_k[m]\) topologically surjective: the lift of a torsion point is torsion by monomorphy. The field closed-monomorphism theorem makes this a closed map, and the reduced étale structures make it an isomorphism. The generic kernels agree as well.

Near the identity this étaleness also holds over \(V\), without presupposing smoothness of \(J\). Choose a common affine chart for \([m]\) and the identity section. Its augmentation ideal \(I\) is finite, and \([m]^*I\subset I\) induces multiplication by \(m\) on \(I/I^2\). Hence \(I=[m]^*I+I^2\). At every point of the identity section, Nakayama on \(I/([m]^*I)\) gives \(I=[m]^*I\). Thus \(J[m]\) is precisely the identity section on a neighbourhood of that section. After strict henselization every special point of \(J[m]\) lifts through the finite étale \(G[m]\); translation by that lifted torsion section reduces its neighbourhood to the identity neighbourhood. Generic points are already étale. Therefore \(J[m]/V\) is étale. A map between étale \(V\)-schemes is étale, so the monomorphism \(G[m]\to J[m]\), surjective on both fibres, is a surjective étale monomorphism and an isomorphism. In particular \(J[m]\) is separated.

On the étale flat \(E\), generic and special multiplication by \(m\) have the same underlying map as the identity-valued map. Equality follows by the common-affine-chart density argument. Therefore \(E\subset J[m]\), as a closed subgroup. Separation makes its identity section closed, and generic density makes that section all of \(E\). Thus \(E=1\). Repeating the argument on each test trait proves separatedness of \(J\) by the DVR criterion.

The separated-target multiplicative-type result, Corollary 7.39, now makes \(a\) closed. Its ideal vanishes generically in the flat \(J\), hence is zero. Thus \(a\) is an isomorphism. \(\square\)

**Theorem 7.51.** Over any scheme \(S\), a monomorphism \(u:G\to H\) of finite-presentation group schemes, with \(G\) of multiplicative type, is an immersion. If \(H\) is separated, it is a closed immersion. The target need not be affine.

**Proof.** The closed conclusion is Corollary 7.39. First prove the immersion conclusion over a Noetherian base. On a complete DVR, take the flat closure \(L\) of the closed generic image. The source is flat, its special dimension is the torus rank, and the dimension formula gives the same dimension to \(L_k\). Its closed special image is consequently a union of components, as in the existing DVR reduction. Delete the remaining special components to get the open subgroup \(J\subset L\). The map \(G_V\to J\) is topologically surjective and generically an isomorphism. 7.50 makes it an isomorphism. The composite \(G_V=J\subset L\subset H_V\) is an immersion, and Lemma 7.26 concludes.

For an arbitrary base, étale-locally split \(G=D_S(M)\), with \(M\) finitely generated, by Theorem 7.7. Work on an affine splitting chart. Descend \(H,u\), all group identities, and the inverse of the monomorphism's diagonal to a finitely generated \(\mathbf Z\)-algebra. Keep the source equal to the same explicit \(D(M)\) at every stage. It is intrinsically flat and of multiplicative type there; no infinite torsion or separation condition needs descent. The Noetherian result gives an immersion on the model, and its pullback gives one on the splitting chart.

Here is the descent step for these immersions. Locally on an affine base select finitely many affine members of the splitting cover; they give a surjective, quasi-compact étale cover. Its target pullback \(q:H'\to H\) is surjective and open. Put \(A=u(G)\) and \(A'=q^{-1}(A)\), the image of the pulled-back immersion. Openness of \(q\) gives \(q^{-1}(\overline A)=\overline{A'}\): every neighbourhood of a point over \(\overline A\) has open image meeting \(A\). The restricted surjective open map \(\overline{A'}\to\overline A\) carries the relatively open \(A'\) onto \(A\). Thus \(A\) is open in \(\overline A\), and \(W=H\setminus(\overline A\setminus A)\) is an open neighbourhood of \(A\). On \(q^{-1}(W)\) the pulled-back immersion has closed image, hence is closed. Closed immersions descend by the affine and ideal descent at the start of *Quotients and torsors*. Consequently \(G\to W\) is closed, proving the immersion over \(H\). This descends the splitting-chart conclusions and proves the theorem. \(\square\)

The non-smooth finite diagonalizable factor is included throughout 7.50. Its \(p\)-primary part need not have flat multiplication by \(p\); the proof uses an integer invertible on the trait and the finite étale prime-to-residue-characteristic torsion instead.

## 8. Torsion subschemes detect functions

**Proposition 8.1. Schematic density.** For a finite-type group \(G\) of multiplicative type over \(k\), its finite subgroup schemes \(G[n]=\ker([n]:G\to G)\), \(n\geq1\), are schematically dense: a closed subscheme containing all of them is \(G\). If \(G\) is smooth, it suffices to take \(n\) prime to the characteristic.

**Proof.** Scalar extension to an algebraic closure is faithfully flat and detects whether an ideal is zero, so reduce to \(G=D(M)\) with \(M=\mathbf Z^r\oplus F\) and \(F\) finite. The coordinate kernel computation in Section 4 imposes \(e^{nm}=1\) for every \(m\), giving

\[
G[n]=D(M/nM).
\]

The quotient map on coordinates sends each monomial to its class modulo \(nM\). Let \(f\ne0\) have finite monomial support. Choose \(n\) divisible by the exponent of \(F\), and greater than every absolute coordinate difference among the free parts of the support. Then \(nM=n\mathbf Z^r\oplus0\), and all those monomials have distinct images in \(M/nM\). Their nonzero linear combination remains nonzero in \(k[M/nM]\). Thus no nonzero function lies in every defining ideal of \(G[n]\), proving the assertion about closed subschemes.

If \(G\) is smooth, Theorem 4.4 makes \(|F|\) prime to the positive characteristic \(p\). One can choose the same arbitrarily large multiples of its exponent also prime to \(p\); their subgroup schemes are finite étale by that theorem. The preceding argument then proves the strengthened assertion. In characteristic zero the prime-to-characteristic condition imposes no restriction. \(\square\)

This concerns finite **subschemes**, so it also detects nilpotent functions when \(G\) is nonsmooth. Restricting to their geometric point sets would lose that information. *Comparison locators:* Milne, Chapter 12i, Theorems 12.32–12.33.

**Example 8.2. Finite generation matters for torsion density.** For \(M=\mathbf Q\), multiplication by every integer \(n>0\) is surjective on \(M\). Theorem 4.5 gives \(D_k(\mathbf Q)[n]=D_k(\mathbf Q/n\mathbf Q)=1\) for all \(n\). These torsion subschemes all equal the identity and are not schematically dense in \(D_k(\mathbf Q)\): for example the nonzero function \(e^1-1\) vanishes on all of them. Thus Theorem 8.1 cannot be extended to arbitrary exponent groups merely by removing its finite-generation hypothesis.

## 9. Exercises

**Exercise 1 (easy): the representing algebra.** Derive the functor of points of \(D_S(M)\), including on nonaffine test schemes, and prove \(D_S(\mathbf Z/n)=\mu_{n,S}\).

**Exercise 2 (medium): coefficients of a character.** Compute the group-like elements of \(R[M]\) by comparing coefficients. Deduce the homomorphism formula over a nonempty connected base. Give a group-like element over \(R=k\times k\), with \(M=\mathbf Z\), which has different exponents on the two components.

**Exercise 3 (medium): an action is a grading.** Prove that actions of \(D_S(M)\) on an affine scheme correspond to \(M\)-gradings of its algebra. Prove, rather than assume, exactness of degree-zero invariants for equivariant modules.

**Exercise 4 (medium): a torus with real circle points.** Identify \(\mathrm{SO}_{2,\mathbf R}\) with a norm-one torus, determine its complex coordinate algebra and Galois character lattice, and prove it is nonsplit and anisotropic.

**Exercise 5 (medium): rank-one forms in every characteristic.** Classify rank-one tori over a field \(k\) by quadratic étale \(k\)-algebras. Identify the torus for a quadratic separable extension and explain why the statement still holds in characteristic two.

**Exercise 6 (hard): the smoothness criterion.** For finitely generated \(M\), prove that \(D_S(M)\) is smooth exactly when \(|M_{\mathrm{tors}}|\) is invertible on \(S\). Explain what fails if finite generation is dropped.

**Exercise 7 (hard): torsion schemes and nilpotents.** Prove schematic density of the finite \(G[n]\) in a finite-type group of multiplicative type, and the prime-to-characteristic version for smooth \(G\). Explain why geometric torsion points alone cannot supply the general statement, using \(\mu_p\).

**Exercise 8 (medium): two Galois actions.** Compare the geometric character modules of \(\mu_3\) and the constant group \((\mathbf Z/3)_{\mathbf Q}\). Prove that these groups are not isomorphic over \(\mathbf Q\), although they become isomorphic over \(\mathbf Q(\zeta_3)\). Identify the Galois action on the geometric points of \(\mu_3\).

**Exercise 9 (hard): a general-base subgroup counterexample.** Verify that \((2(x-1))\) is a Hopf ideal in \(\mathbf Z[x,x^{-1}]\). Compute the generic and characteristic-two fibres of its subgroup, and prove that it is not any \(D_{\mathbf Z}(N)\).

**Exercise 10 (medium): infinitely many rigid endomorphisms.** Determine the scheme representing group endomorphisms of \(\mathbf G_{m,k}\). Is it quasi-compact? Show that a family of such endomorphisms over \(k[\epsilon]/(\epsilon^2)\) has no infinitesimal deformation of its exponent.

**Exercise 11 (medium): invisible rational-point actions.** In characteristic \(p\), let \(\mu_p\) act on \(\mathbf A^1_k\) by multiplication. Compute the invariant algebra and the fixed subscheme, and compare them with the fixed points obtained by testing only \(\mu_p(k)\).

**Exercise 12 (medium): two meanings of rigidity.** Over \(k[\delta]/\delta^2\), compute the two actions in Section 7.3 on the standard basis of \(R^2\). Prove they are isomorphic, unequal, and have equal reductions. Explain why this does not contradict Proposition 7.3.

**Exercise 13 (medium): a free infinitesimal action.** In characteristic \(p\), let \(\mu_p\) act by multiplication on \(\mathbf G_m\). Determine its strong grading, its affine quotient and the torsor map. Explain why the trivial group \(\mu_p(k)\) does not detect this quotient.

**Exercise 14 (medium): a torsor requiring an inseparable cover.** Over \(k=\mathbf F_p(s)\), show that \(t^p=s\) defines a \(\mu_p\)-torsor which cannot be trivialized by an étale cover. Identify the line-bundle pair in Corollary 4.8.

**Exercise 15 (medium): nonaffine fixed points.** Let \(\mu_p\) act on \(\mathbf P^1_k\) by \([x:y]\mapsto[tx:y]\) in characteristic \(p\). Compute its fixed subscheme, including its scheme structure. Compare with the answer from rational group points alone.

**Exercise 16 (hard): finite presentation of invariants.** Prove that \(R[x,y]\), with weights \(1,-1\), has invariant ring \(R[xy]\). For \(R[x,y]/(xy-a)\), \(a\in R\), compute the invariant quotient and decide exactly when its \(\mathbf G_m\)-action is free. Use the criterion on all test schemes.

**Exercise 17 (medium): a finite multiplication map need not be flat.** Over a field of characteristic \(p>0\), determine the multiplication-by-\(p\) morphism of \(\mu_p\). Prove that it is finite and is not flat. Compare this with multiplication on a torus, and identify the hypothesis which distinguishes the two claims.

**Exercise 18 (hard): rank-one tori over schemes.** Extend the quadratic-étale-algebra classification in Exercise 5 from fields to an arbitrary scheme \(S\). Construct the torus attached to a quadratic finite étale \(S\)-algebra by its norm, and prove that it gives every rank-one torus, including in characteristic two.

**Exercise 19 (medium): a nonzero weight with zero differential.** In characteristic \(p\), let \(\mathbf G_m\) act on \(\mathbf G_a\) by \(t.x=t^px\). Verify every hypothesis of Theorem 7.21. Compute the derivative of the acting character \(t\mapsto t^p\) at \(1\), and explain why its vanishing does not invalidate the theorem.

## 10. Complete solutions

**Solution 1.** A map \(T\to D_S(M)\) is an algebra homomorphism \(\mathcal O_T[M]\to\mathcal O_T\). The images \(a_m\) of the basis symbols are global units satisfying \(a_{m+n}=a_ma_n\) and \(a_0=1\). Conversely this rule defines the homomorphism on each finite local sum of basis symbols and glues over \(T\). Thus the points are \(\operatorname{Hom}(M,\Gamma(T,\mathcal O_T^\times))\); the comultiplication makes their group law pointwise multiplication. For \(M=\mathbf Z/n\), a homomorphism is specified by one unit \(a\) satisfying \(a^n=1\), precisely the functor of \(\mu_n\). The coordinate algebra is \(\mathcal O_S[x]/(x^n-1)\), where \(x\) is automatically a unit.

**Solution 2.** If \(a=\sum c_m e^m\), equality of the \(e^m\otimes e^n\) coefficients gives \(c_m^2=c_m\) on the diagonal and \(c_m c_n=0\) off it. The counit gives \(\sum c_m=1\). These conditions are also sufficient. On a nonempty connected spectrum only \(0,1\) are idempotents, so \(a=e^m\). A Hopf map from \(R[N]\) to \(R[M]\) therefore sends \(e^n\) to \(e^{f(n)}\), with \(f(n+n')=f(n)+f(n')\); this proves the required contravariant homomorphism formula. On a connected scheme the locally determined exponents agree globally. For \(R=k\times k\),

\[
a=(1,0)e^1+(0,1)e^{-1}
\]

is group-like: its orthogonal coefficients sum to \(1\). It chooses exponent \(1\) on the first component and \(-1\) on the second, and is not one global basis element.

**Solution 3.** Write a coaction as \(\rho(v)=\sum v_m\otimes e^m\). Coassociativity forces each \(v_m\) to have weight \(m\), and the counit recovers \(v=\sum v_m\). Applying the coaction to a relation among distinct weights shows that each coefficient is zero, proving the direct-sum grading. If the coaction is an algebra map, \(\rho(ab)=\rho(a)\rho(b)\) gives degree addition and \(\rho(1)=1\otimes e^0\) gives the degree of the unit. Conversely those multiplication conditions make the coaction defined by the grading an algebra map, hence an action.

Equivariant maps preserve the grading. In a surjection \(E\to F\), a degree-zero element of \(F\) has a lift \(v=\sum v_m\), and its degree-zero part \(v_0\) still maps to that element, because the other degrees map to the other weight spaces. Kernels and images are likewise computed degreewise. Thus taking invariants, which selects degree zero, preserves short exact sequences. The coefficient constructions localize and glue over \(S\).

**Solution 4.** Norm one in \(\mathbf C\) means \(a^2+b^2=1\). The associated real matrix is \(\begin{pmatrix}a&-b\\b&a\end{pmatrix}\), and its determinant is that norm. Conversely for a determinant-one orthogonal matrix its transpose equals its adjugate, forcing exactly these entries. This proves the scheme isomorphism on arbitrary real algebras. Over \(\mathbf C\), let \(z=a+ib\); the relation gives \(z^{-1}=a-ib\), so the algebra is \(\mathbf C[z,z^{-1}]\). Conjugation sends \(z\) to \(z^{-1}\), inducing multiplication by \(-1\) on the lattice \(\mathbf Z\). This is not the trivial lattice of the split \(\mathbf G_m\), so the torus is nonsplit. Its cocharacter invariants vanish, proving anisotropy by (18). Its real point equation is the unit circle.

**Solution 5.** A rank-one cocharacter lattice is \(\mathbf Z\), whose automorphism group is \(\{\pm1\}\). Its continuous Galois actions are therefore continuous homomorphisms \(\Gamma\to\{\pm1\}\). Conjugacy does nothing because this group is abelian. The trivial action gives the split torus and the algebra \(k\times k\). Every nontrivial action has an index-two open kernel, hence corresponds to a quadratic separable field extension \(K/k\).

For that extension, the character lattice of the norm-one torus is \(\mathbf Z^2/\mathbf Z(1,1)\). Its nontrivial automorphism exchanges the coordinates and acts by \(-1\) on the quotient, so it gives the required form. For \(k\times k\), norm one is \(\{(a,a^{-1})\}\simeq\mathbf G_m\). These constructions exhaust and distinguish all forms by Theorem 5.2. In characteristic two a separable quadratic extension still has two distinct embeddings and the same sign action on the integral lattice. Such extensions can be described by \(z^2-z=a\); the lattice sign does not become trivial merely because the ground field has characteristic two.

**Solution 6.** Decompose \(M=\mathbf Z^r\oplus\bigoplus\mathbf Z/n_i\). Then \(D_S(M)=\mathbf G_m^r\times\prod\mu_{n_i}\). If \(|M_{\mathrm{tors}}|=\prod n_i\) is invertible, each \(n_i\) is invertible, each \(\mu_{n_i}\) is étale by its unit derivative, and the product is smooth.

If that order is not invertible, there is a residue characteristic \(p\) dividing some \(n_i\). Over an algebraic closure of that residue field, write \(n_i=p^a d\) with \(p\nmid d\) and \(a>0\). The equation \(X^{n_i}-1=(X^d-1)^{p^a}\) gives a nonreduced factor. Its nonzero nilpotent stays nonzero after tensoring with the other nonzero factor algebras. Thus this geometric fibre is not reduced and cannot be smooth. This contradicts smoothness of the original morphism.

Without finite generation, torsion-free \(M=\bigoplus_{i\geq1}\mathbf Z\) gives an infinitely generated Laurent group algebra. Section 1 proves that it cannot be of finite type; because the group is affine, local finite presentation would imply finite type. Hence this torsion-free example is not smooth.

**Solution 7.** After faithfully flat extension to an algebraic closure, write \(M=\mathbf Z^r\oplus F\) with finite \(F\). The algebra of \(G[n]\) is \(k[M/nM]\), obtained by imposing all \(e^{nm}=1\). A nonzero function has finite support. Choose \(n\) divisible by the exponent of \(F\) and larger than every coordinate difference of the free parts of that support. Distinct monomials then remain distinct modulo \(nM\), so the function does not vanish on \(G[n]\). The intersection of all defining ideals is zero; faithful flatness descends this conclusion.

If the group is smooth, \(F\) has order prime to \(p\), so the same choices can be made with \(p\nmid n\). These \(G[n]\) are finite étale, proving the strengthened result. In \(\mu_p\) over an algebraically closed field of characteristic \(p\), the function \(x-1\) is nonzero but vanishes at the sole geometric point. Geometric torsion points therefore do not detect it, whereas the finite subgroup scheme \(G[p]=\mu_p\) does.

**Solution 8.** A character of \(\mu_3\) is \(\zeta\mapsto\zeta^m\), \(m\in\mathbf Z/3\), defined over \(\mathbf Q\). Its character action is trivial. A character of the constant \(\mathbf Z/3\) is specified by the image of its distinguished generator, a cube root of unity. Its character module is \(\mu_3(\overline{\mathbf Q})\), and conjugation sends a primitive root to its inverse; the action is nontrivial. The two Galois modules are not isomorphic, so Theorem 5.2 rules out an isomorphism of the groups over \(\mathbf Q\). After adjoining \(\zeta_3\), both actions become trivial and the finite character classification gives an isomorphism. On the geometric points of \(\mu_3\), Galois also acts by its action on roots of unity, namely the cyclotomic action. This is the point action, not the character action computed first.

**Solution 9.** The counit of \(2(x-1)\) is zero. Its antipode is \(-2x^{-1}(x-1)\), in the same ideal. Its comultiplication is \(2(x-1)\otimes x+1\otimes2(x-1)\), so the ideal is a Hopf ideal. Over \(\mathbf Q\) it imposes \(x=1\), giving the trivial group; modulo \(2\) its generator vanishes, leaving \(\mathbf F_2[x,x^{-1}]\), so the fibre is \(\mathbf G_m\). The class of \(x-1\) is nonzero, since its reduction modulo \(2\) is nonzero, but is killed by \(2\). The coordinate module is not flat over \(\mathbf Z\). Every group algebra \(\mathbf Z[N]\) is free, so the subgroup cannot be \(D_{\mathbf Z}(N)\). This is a counterexample to an arbitrary-base subgroup assertion, with no contradiction to the field theorem.

**Solution 10.** By Theorem 7.1, or directly by Lemma 2.1 applied to the image of the coordinate \(x\), a family of endomorphisms is a locally constant integer exponent \(x\mapsto x^m\). The representing scheme is \(\coprod_{m\in\mathbf Z}\operatorname{Spec}k\), an étale scheme which is not quasi-compact: its disjoint open components have no finite subcover. The spectrum of \(k[\epsilon]/(\epsilon^2)\) is nonempty and connected and has no nontrivial idempotents. Its group-like elements are therefore still exactly \(x^m\), with no added infinitesimal coefficient. An exponent has no deformation in that family.

**11.** The exponent group of \(\mu_p\) is \(\mathbf Z/p\). Thus \(x^j\) has weight \(j\bmod p\), and the degree-zero algebra is \(k[x^p]\). Every nonzero-weight monomial is divisible by \(x\); since \(x\) itself has nonzero weight, the fixed ideal is exactly \((x)\). Hence the fixed scheme is the origin, while the affine invariant quotient is an affine line. In a field of characteristic \(p\), \(t^p-1=(t-1)^p\), so \(\mu_p(k)=\{1\}\). Testing that group of points alone would declare every point of the affine line fixed, which misses the universal nilpotent parameters. At the origin the tangent action has weight one, and its invariant part is zero, agreeing with the tangent space of the fixed origin.

**12.** The original action sends \(e_1\) to \(t e_1\) and \(e_2\) to \(e_2\). The conjugate sends them to \(t e_1\) and \(e_2+\delta(1-t)e_1\), respectively. The latter correction is nonzero in \(R[t,t^{-1}]\), proving inequality of the universal actions, and vanishes modulo \(\delta\), proving equality of their reductions. The relation \(P D(t)= (P D(t)P^{-1})P\) makes \(P\) an equivariant isomorphism. Proposition 7.3 concerns an action becoming **trivial** after reduction; these reductions are the same nontrivial weight-one-plus-weight-zero action. It does not assert equality of two actions on a fixed module.

**Solution 13.** With exponent group \(\mathbf Z/p\), the degree-zero algebra is \(B=k[x^p,x^{-p}]\) and \(A_i=x^iB\) for \(0\leq i<p\). Each \(x^i\) is a homogeneous unit, so the grading is strong. Theorem 4.9 gives the quotient \(\mathbf G_m\) with coordinate \(z=x^p\), and its torsor map is the finite flat degree-\(p\) map \(x\mapsto x^p\). It is not étale, since its relative derivative is zero. The action is free schematically because a unit \(x\) can be cancelled from \(tx=x\) over every test algebra, forcing \(t=1\). Although \(\mu_p(k)=\{1\}\), its universal coordinate \(t\) contains nilpotent directions; discarding those would replace the quotient map by the identity and miss its degree.

**Solution 14.** Corollary 4.8 gives the pair consisting of the trivial line and the trivialization whose value on its \(p\)-th tensor power is \(s\). The associated algebra is \(k[t]/(t^p-s)\). This is a field of degree \(p\): the polynomial is Eisenstein at \(s\) over \(\mathbf F_p[s]\), hence irreducible over its fraction field. It is nevertheless a torsor under the nonreduced group \(\mu_p\), by the strong cyclic grading. Its root is purely inseparable of degree \(p\), so belongs to no separable extension of \(k\). A trivialization over an étale cover would yield a point over a finite separable extension by choosing a point of that cover, which is impossible. The finite flat extension obtained by adjoining this root does trivialize it.

**Solution 15.** Both usual affine charts are stable. On \(y\ne0\), the coordinate \(z=x/y\) has weight \(1\), and Proposition 3.2 gives fixed ideal \((z)\). On \(x\ne0\), the coordinate \(w=y/x\) has weight \(-1\), giving ideal \((w)\). These two fixed sections have empty overlap, since the overlap requires the corresponding coordinate to be a unit. They glue to the two reduced points \([0:1]\) and \([1:0]\). This is the closed fixed subscheme supplied by Corollary 4.11. Testing only \(\mu_p(k)=\{1\}\) would incorrectly give all of \(\mathbf P^1_k\), including its one-dimensional tangent directions.

**Solution 16.** The degree-zero monomials are exactly \(x^iy^i=(xy)^i\); they are linearly independent over \(R\), so the invariant algebra is \(R[xy]\). For the graded quotient by \((xy-a)\), exactness of degree zero gives the invariant algebra \(R[xy]/(xy-a)=R\). The products of its degree-one and degree-minus-one parts lie in the ideal \((a)\subset R\), and their product contains \(xy=a\), so that ideal is exactly \((a)\). If \(a\) is a unit, \(x\) is a homogeneous unit with inverse \(y/a\); Theorem 4.7 makes the scheme a \(\mathbf G_m\)-torsor and its action free. If \(a\) is not a unit, choose a maximal ideal containing it. In that residue field the origin \(x=y=0\) lies on \(xy=a\) and has stabilizer all of \(\mathbf G_m\), so the action fails schematic freeness. Equivalently the necessary strong-grading condition in Theorem 4.9 fails. This argument includes the zero ring, where every element is a unit and all schemes involved are empty.

**Solution 17.** Multiplication by \(p\) sends \(t\) to \(t^p=1\), so factors through the identity section. In the coordinate \(x=t-1\), its algebra map is

\[
k[x]/(x^p)\longrightarrow k[x]/(x^p),
\qquad x\longmapsto0.
\]

It is finite, since its target is finite-dimensional over \(k\). It is not flat. Tensor the injection \((x)\hookrightarrow A=k[x]/(x^p)\) with the target module \(B\) for this map. Since \(x\) acts as zero on \(B\), its source is \(((x)/(x^2))\otimes_kB\ne0\), but the induced map into \(B\) is zero. Flatness would preserve injectivity. For a split rank-\(r\) torus, multiplication by a positive integer \(n\) has an injective exponent map \(n:\mathbf Z^r\to\mathbf Z^r\), with finite cokernel. Theorem 4.5 makes it finite faithfully flat of degree \(n^r\), whether or not \(n\) is invertible on the base. This descends for relative tori. The missing hypothesis in the \(\mu_p\) example is torsion-freeness of the character group; multiplication need not be injective on a torsion group.

**Solution 18.** By Theorem 7.7 a rank-one torus has a locally constant character lattice with stalk \(\mathbf Z\). Its frame torsor is a torsor for \(\operatorname{Aut}(\mathbf Z)=\{1,-1\}\). This is a finite étale double cover, so is equivalent to a quadratic finite étale algebra. Conversely such an algebra is étale locally \(\mathcal O_S\times\mathcal O_S\). Construct its restriction-of-scalars group by gluing two copies of \(\mathbf G_m\), with the transition maps permuting their coordinates. On these charts the norm is \((u,v)\mapsto uv\); this formula descends and identifies the kernel with the torus \(u\mapsto(u,u^{-1})\). Interchanging the two sheets changes \(u\) to \(u^{-1}\). Its character lattice therefore has exactly the sign action supplied by the frame torsor. Theorem 7.7 identifies it with the original torus. Algebra isomorphisms, cover isomorphisms and lattice isomorphisms correspond, proving the classification of isomorphism classes. The construction uses finite étaleness and coordinate permutation; it never divides by two, so applies in characteristic two as well.

**Solution 19.** The group \(\mathbf G_a\) is affine and smooth with additive geometric fibres. The action on its tangent line is the character \(t^p\), a nontrivial character even in characteristic \(p\): the universal Laurent monomials \(t^p\) and \(1\) are distinct. Theorem 7.21 therefore applies and gives its identity vector-group identification. On dual numbers, \((1+\epsilon a)^p=1\), so the derivative of the character at \(1\) is zero. The theorem requires a nonzero integer character, as a scheme representation; it does not require a nonzero differential of that character or invertibility of its weight. Confusing these conditions would discard this valid example and incorrectly weaken the result.

## What this lesson does not prove

The equivalence between becoming diagonalizable over an arbitrary field extension and over a separable closure is proved in Theorem 5.0. The finite splitting and Galois-module classification, the full homomorphism-scheme assertion, and the torus-form classification are also proved here.

Faithfully flat affine, algebra and module descent is proved at the start of *Quotients and torsors*. The local-finiteness proof in *Group schemes, actions and Hopf algebras*, Lemma 5.1, supplies the finite subcoalgebras used in Theorem 5.0. Descent of finite presentation and the correspondence between étale sheaves over a field and continuous Galois sets remain prerequisites; the latter has locators [Stacks, Tags 03QR and 03QT]. Finite locally free Cartier duality and the fppf quotient argument are proved in the preceding course lessons and used explicitly. The structure theorem for finitely generated abelian groups, coefficient comparison in free modules and elementary field theory are assumed.

The arbitrary-base proofs include fpqc-to-étale splitting and relative character classification for finite-presentation groups of multiplicative type, their canonical torus–finite-group sequence, torus embeddings, and finite étale splitting over an irreducible normal base. Proposition 7.4 uses finite generation only for the target character group. The congruence and descent proofs are included in Sections 7.6 and 7.10; the equivalence for finite étale covers with finite continuous fundamental-group sets and the standard henselian-ring characterizations are prerequisites. Example 4.3 explains the limitation on the subgroup theorem, and Example 4.12 explains why the closed-immersion theorem for a diagonalizable source is stronger than the corresponding assertion for arbitrary flat groups.

## References

- **[Grothendieck]** Alexander Grothendieck, *SGA 3, Exposé VIII: Groupes diagonalisables*, retyped version 1.1 of 8 November 2009. [Freely accessible text](https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp8-8nov09.pdf).
- **[Conrad]** Brian Conrad, *Reductive group schemes*, 2014, Appendix B, groups of multiplicative type. [Author's freely accessible text](https://math.stanford.edu/~conrad/papers/luminysga3smf.pdf).
- **[Gabber–Stacks]** The Stacks Project, *More on Groupoid Schemes*, [Lemma 40.15.3, effective descent for ind-quasi-affine morphisms](https://stacks.math.columbia.edu/tag/0APK), with its invariant-neighbourhood and intersection lemmas.
- **[Gille]** Philippe Gille, *Introduction to reductive group schemes over rings*, draft of 9 May 2025. [Author's freely accessible notes](https://math.univ-lyon1.fr/~gille/prenotes/reductive.pdf). The fixed-locus arguments above are independently written; Theorem 3.4 extends the noetherian-base statement in the notes by proving finite presentation directly.

J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, corrected edition dated 5 October 2021, Cambridge University Press, 2022: Chapter 12a–i for characters, diagonalizable groups, multiplicative type, tori, Galois classification, density and rigidity; Chapter 11c for Cartier duality. [Corrected author edition, freely available PDF](https://www.jmilne.org/math/Books/iAG2022.pdf).

The Stacks Project, read in **AI Integrated Stacks Project**, Groupoid Schemes, Tags 022U and 040M for \(\mathbf G_m\) and roots of unity, and Tags 0EKJ–0EKL for \(\mathbf G_m\)-actions and gradings; Descent, Tag 0CDR for Galois descent; Fundamental Groups, Tag 03QR and Étale Cohomology, Tag 03QT for Galois sets and sheaves over a field. AI Integrated Stacks Project is an AI-integrated edition; its additions have not been reviewed by the official Stacks maintainers. The cited material was checked at published revision 565b10e987aba5969b21145a0833f42d69f96790.

The finite approximation and nonseparated-target proofs in 7.40–7.51 complete the comparison with Grothendieck, SGA3 Exposé VIII7.9, the corrected all-point version of VIII7.12, and VIII7.13(b), in the retyped edition of 8 November2009. Example7.49 records the positive-characteristic-only quantifier failure over Q[t]. The original field, Artinian, trait and separated-target proofs are retained. The added exposition is independently written under CC0 1.0.
