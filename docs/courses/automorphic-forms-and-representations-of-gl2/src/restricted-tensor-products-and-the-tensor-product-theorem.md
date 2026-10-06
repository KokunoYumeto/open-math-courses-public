# Restricted tensor products and the tensor product theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Author self-check complete. Public domain (CC0).*

An adelic vector has finite level. Outside finitely many primes it is fixed by the standard maximal compact subgroup. The tensor product theorem says considerably more: in an irreducible admissible representation, every place has its own irreducible representation, and the adelic module is assembled from them. The local representations are determined by the adelic module, although a particular tensor product isomorphism and particular spherical vectors need not be canonical.

We work first over \(\mathbb Q\). Put
\[
G_p=\mathrm{GL}_2(\mathbb Q_p),\qquad K_p=\mathrm{GL}_2(\mathbb Z_p),
\qquad G_f=\mathrm{GL}_2(\mathbb A_f),
\qquad K_\infty=O(2).
\]
Normalize the finite Haar measures by \(\operatorname{vol}(K_p)=1\). At infinity our objects are compatible \((\mathfrak{gl}_2(\mathbb C),K_\infty)\)-modules. At finite places they are smooth algebraic representations. A global module is **admissible** if every space obtained by fixing a compact open subgroup of \(G_f\) and retaining finitely many \(K_\infty\)-types is finite-dimensional.

The prerequisites are the smooth Hecke-module dictionary of Lesson 5 and the archimedean modules of Lesson 11. We will prove the algebraic tensor product theorem, including the algebra lemma and compatibility of the local factors. Its application to the cuspidal spectrum uses the admissibility and comparison already isolated in Lessons 3–4.

## 1. The finite stages of a restricted tensor product

Let \(I\) be a countable set of places, and let \(V_v\) be a nonzero complex vector space for every \(v\in I\). Choose a finite subset \(S_0\) and nonzero vectors \(\xi_v\in V_v\) for \(v\notin S_0\). For a finite \(S\supset S_0\), set
\[
V_S=\bigotimes_{v\in S}V_v.
\]
For \(S\subset T\), define
\[
i_{S,T}(x)=x\otimes\bigotimes_{v\in T\setminus S}\xi_v.
\tag{1.1}
\]
These maps are injective: choose a linear functional taking each newly inserted \(\xi_v\) to \(1\), and apply their tensor product as a left inverse. They satisfy \(i_{T,U}i_{S,T}=i_{S,U}\). The **algebraic restricted tensor product** is
\[
\bigotimes_v' V_v=\varinjlim_{S\supset S_0}V_S.
\tag{1.2}
\]
Thus a vector is a finite sum of tensors whose components equal \(\xi_v\) outside a finite set. It need not itself be a pure tensor. Enlarging \(S_0\) changes neither the direct limit nor its meaning: the enlarged collection of finite stages is cofinal.

Suppose \(A_v\) are algebras and \(e_v\in A_v\) are nonzero idempotents for \(v\notin S_0\). The same construction gives
\[
A=\bigotimes_v' A_v
\]
with transitions \(a\mapsto a\otimes\bigotimes_{T\setminus S}e_v\). They preserve multiplication precisely because \(e_v^2=e_v\). If each \(V_v\) is an \(A_v\)-module and \(e_v\xi_v=\xi_v\), then
\[
\left(\bigotimes_v a_v\right)\left(\bigotimes_v x_v\right)
=\bigotimes_v(a_vx_v)
\tag{1.3}
\]
defines an \(A\)-action. To interpret the formula, choose one finite stage containing every deviation in both tensors. Outside it both \(a_v=e_v\) and \(x_v=\xi_v\); the result therefore has the required tail. This also proves that the action respects the transition maps.

**Proposition 1.1 — changing vectors on distinguished lines.** If \(\xi'_v=c_v\xi_v\), with \(c_v\ne0\), for all \(v\notin S_0\), then the two restricted tensor products are isomorphic as \(A\)-modules.

**Proof.** On the stage \(V_S\), multiply by the finite scalar
\[
c_S=\prod_{v\in S\setminus S_0}c_v.
\]
The transition to \(T\) on the first system inserts \(\xi_v\); multiplication by \(c_T\) changes the new factors to \(c_v\xi_v=\xi'_v\) and multiplies the old stage by \(c_S\). Consequently
\[
c_T i_{S,T}=i'_{S,T}c_S.
\tag{1.4}
\]
These maps induce a direct-limit isomorphism. The maps using \(c_v^{-1}\) are its inverse. Scalar multiplication commutes with every \(A_S\)-action, so the limit map is equivariant. No infinite product of the \(c_v\) is taken. \(\square\)

For spherical representations this proposition applies because the fixed line will be one-dimensional. Arbitrary choices in higher-dimensional fixed spaces are not covered. For example, take \(G_j=\{1,s_j\}\), \(K_j=\{1\}\), and \(V_j=\mathbb C_+\oplus\mathbb C_-\), with \(s_j\) acting by \(+1,-1\). For the restricted group \(\bigoplus_jG_j\), reference vectors all in \(\mathbb C_+\) produce the direct sum of characters having finitely many minus signs. Reference vectors all in \(\mathbb C_-\) produce characters having finitely many plus signs. These character sets are disjoint: an intertwiner sends each simultaneous eigenvector to a vector with the same character, and the other module has no such vector. The two representations are not isomorphic. The one-dimensional-tail hypothesis has real content.

## 2. The algebras that record finite level and compact type

Write \(\mathcal H_p=C_c^\infty(G_p)\), with convolution as in Lesson 5, and \(e_p=1_{K_p}\). Here smooth means locally constant. At another compact open subgroup \(U_p\), the correct idempotent is
\[
e_{U_p}=\operatorname{vol}(U_p)^{-1}1_{U_p}.
\]

**Proposition 2.1 — the finite adelic Hecke algebra.** Product functions give an algebra isomorphism
\[
\mathcal H_f=C_c^\infty(G_f)
\ \simeq\ \bigotimes_p'\mathcal H_p,
\tag{2.1}
\]
where the reference idempotents are \(e_p\).

**Proof.** A product function with tail \(1_{K_p}\) is locally constant and compactly supported in the restricted product. Conversely, a compact subset of \(G_f\) lies in
\[
\prod_{p\in S}G_p\times\prod_{p\notin S}K_p
\]
for some finite \(S\): these open subgroups form an increasing cover, and a finite subcover of the compact subset suffices. A locally constant compactly supported function has a compact open right stabilizer. To see this, cover its support by finitely many open cosets on which it is constant, and intersect the corresponding fixing subgroups; its support and its complement are then both preserved. A smaller stabilizer can be chosen rectangular,
\[
U=\prod_{p\in S}U_p\times\prod_{p\notin S}K_p.
\]
Only finitely many right \(U\)-cosets meet the support. Enlarge \(S\) to include all deviations of representatives of those cosets. Each coset indicator is now a product of finitely many local indicators and the tail \(1_{K_p}\). Their finite linear combination is the given function.

The map is injective at every finite stage. For a finite sum of product functions, choose bases of the finite-dimensional spans of its factors. Point evaluations span the dual of each such span: a function killed by all evaluations is zero. Applying products of those evaluations recovers each tensor coefficient, so a tensor mapped to the zero function was zero.

Convolution of product functions is the product of local convolutions. On a common finite stage this is finite-product Fubini; outside it \(e_p*e_p=e_p\), with \(\operatorname{vol}(K_p)=1\). Thus the vector-space isomorphism preserves multiplication. \(\square\)

We need an analogous algebra at infinity, but we do not identify arbitrary smooth functions on a product of real groups with an algebraic tensor product. Instead we encode the \((\mathfrak g,K_\infty)\)-action itself.

Let \(\mathcal R(K_\infty)\) be the convolution algebra of finite sums of matrix coefficients on \(K_\infty\), regarded as distributions against probability Haar measure. Compact Schur orthogonality identifies it with the algebraic direct sum of full matrix blocks
\[
\mathcal R(K_\infty)=\bigoplus_{\tau\in\widehat K_\infty}
\operatorname{End}_{\mathbb C}(V_\tau).
\]
Finite-dimensional compact representations are unitarizable and completely reducible by the compact representation lesson, Proposition 1.2. The matrix-block assertion follows from Matrix coefficients and the Peter–Weyl theorem, Theorem 2.1: integrating a suitably scaled conjugate matrix coefficient against a representation gives a matrix unit in that block and zero in the other blocks. For a finite set \(E\) of compact types, write \(e_E\) for the sum of the identity blocks. As a density it is
\[
e_E(k)=\sum_{\tau\in E}(\dim\tau)\operatorname{tr}\tau(k^{-1}).
\tag{2.2}
\]
It projects onto precisely those isotypic components.

Define \(\mathcal H_\infty=\mathcal R(\mathfrak g,K_\infty)\) to be the span of distributions \(u*h\), where \(u\in U(\mathfrak g)\) is a differential distribution at the identity and \(h\in\mathcal R(K_\infty)\). The sign of the differential distribution is chosen so that its integrated action is \(d\pi(u)\). These distributions have finite order and support in \(K_\infty\).

Here are the algebraic facts about this definition. Every \(u\) has a finite-dimensional span under \(\operatorname{Ad}(K_\infty)\), since its enveloping degree is bounded. Moving \(u\) past a compact distribution uses
\[
\delta_k*u=\operatorname{Ad}(k)(u)*\delta_k.
\tag{2.3}
\]
Expansion in that finite-dimensional span shows that a product of two \(u*h\)'s is a finite sum of the same form. Every such distribution has only finitely many left and right compact types. Its right types come from \(h\); its left types lie in the tensor product of the compact span of \(u\) and those of \(h\). A sufficiently large \(E\) therefore gives
\[
e_E*a=a=a*e_E.
\tag{2.4}
\]
Thus the \(e_E\) are local units.

A compatible \((\mathfrak g,K_\infty)\)-module acts on \(u*h\) by \(d\pi(u)\pi(h)\). Conversely, a nondegenerate \(\mathcal H_\infty\)-module is a union of its \(e_E\)-ranges. The matrix blocks recover its algebraic finite-type \(K_\infty\)-action. For \(X\in\mathfrak g\), define
\[
Xv=(X*e_E)v\quad\text{when }e_Ev=v.
\tag{2.5}
\]
If \(E\subset F\), then \((X*e_F)*e_E=X*e_E\); a common larger set compares any two choices. Hence (2.5) is independent of \(E\). Distribution multiplication supplies the Lie bracket and (2.3) supplies compact conjugation compatibility. For \(X\) tangent to \(K_\infty\), differentiating the compact matrix coefficients gives its already recovered compact infinitesimal action. These constructions are inverse, including invariant subspaces and intertwiners.

We therefore use the global algebra
\[
\mathcal H=\mathcal H_\infty\otimes\mathcal H_f.
\tag{2.6}
\]
It records exactly the mixed category in the theorem below. The analytic archimedean convolution algebra on a smooth globalization is a separate realization; it is not needed for this proof.

For clarity, an algebra \(A\) has **local units** here if any finite collection of its elements has a common two-sided idempotent unit. An \(A\)-module is nondegenerate if \(AV=V\). Then every finite collection of module vectors has a common idempotent fixing it: write them as finite sums \(a_iv_i\), and choose a common left unit of the \(a_i\). Our idempotent families are directed. For finite groups of places we use products of the local units, and for \(\mathcal H\) we use \(e_E\otimes e_U\). Global admissibility says exactly that their ranges are finite-dimensional.

## 3. Two algebraic tools: interpolation and extension from a corner

The following interpolation statement will take the place of an unproved matrix-algebra theorem.

**Lemma 3.1 — finite interpolation.** Let \(A\) have local units, and let \(M\) be a simple nondegenerate \(A\)-module with \(\operatorname{End}_A(M)=\mathbb C\). Given linearly independent \(m_1,\ldots,m_r\) and arbitrary \(n_1,\ldots,n_r\) in \(M\), some \(a\in A\) satisfies \(am_i=n_i\) for every \(i\).

**Proof.** For one vector this is \(Am_1=M\). Assume the assertion for \(r-1\), and consider the submodule
\[
L=\{(am_1,\ldots,am_r):a\in A\}\subset M^r.
\]
Its projection onto the first \(r-1\) coordinates is surjective. Its kernel, a submodule of the last copy of \(M\), is either zero or that entire copy. In the latter case \(L=M^r\).

If the kernel is zero, \(L\) is the graph of an \(A\)-linear map \(M^{r-1}\to M\). Every such map is \(\sum_{i<r}c_i\) times the respective coordinate maps, because \(\operatorname{End}_A(M)=\mathbb C\). A local unit fixing all \(m_i\) puts \((m_1,\ldots,m_r)\) in \(L\). It follows that \(m_r=\sum_{i<r}c_im_i\), a contradiction. Thus the kernel is the last copy of \(M\), proving the induction. \(\square\)

If \(M\) is finite-dimensional and simple, its commuting endomorphisms are scalars: an endomorphism has a complex eigenvalue, and its corresponding nonzero eigenspace is an invariant subspace. Lemma 3.1 then says that the image of \(A\) is all of \(\operatorname{End}_{\mathbb C}(M)\), by prescribing the image of a basis. This proves the finite-dimensional algebra assertion we need.

For an idempotent \(e\in A\), \(eAe\) is a unital algebra with identity \(e\).

The reconstruction in Lesson 5, Theorem 3.1, uses only local units and an idempotent. Its algebraic form, needed also at infinity, is the following.

**Lemma 3.2 — simple modules and one corner.**

1. If \(V\) is simple and nondegenerate and \(eV\ne0\), then \(eV\) is simple over \(eAe\).
2. Every simple unital \(eAe\)-module \(M\) extends to a unique, up to isomorphism, simple nondegenerate \(A\)-module \(S\) with \(eS\simeq M\).
3. If \(M\) is finite-dimensional, then \(\operatorname{End}_A(S)=\mathbb C\).

**Proof.** For a nonzero \(eAe\)-submodule \(W\subset eV\), simplicity gives \(AW=V\). Applying \(e\), and using \(W=eW\), gives
\[
eV=eAW=eAeW=W.
\]
This proves part 1.

For part 2 form
\[
I=Ae\otimes_{eAe}M.
\tag{3.1}
\]
It is nondegenerate and generated by \(eI\). The maps \(m\mapsto e\otimes m\) and \((eae)\otimes m\mapsto(eae)m\) identify \(eI\) with \(M\). If \(U\) is a proper submodule of \(I\), then \(eU\) is either zero or \(M\). The latter would put \(eI\) in \(U\), forcing \(U=I\). Thus every proper submodule has \(eU=0\).

Let \(N\) be the sum of all proper submodules. Then \(eN=0\), so \(N\ne I\). It contains every proper submodule and hence is the unique maximal submodule. The quotient \(S=I/N\) is simple and has \(eS=M\). If \(V\) is any other simple extension, a chosen identification \(M=eV\) induces the surjection \(I\to V\), \(ae\otimes m\mapsto am\). Its kernel is the unique maximal submodule \(N\). This proves uniqueness.

For part 3, restriction sends an \(A\)-endomorphism of \(S\) to an \(eAe\)-endomorphism of \(eS=M\). It is injective because \(S=AeS\). The target consists of scalars by the eigenvalue argument above, so the endomorphisms of \(S\) are scalars too. \(\square\)

This lemma does not require \(e\) to generate all of \(A\) as a two-sided ideal. It only describes the simple modules on which \(e\) is nonzero.

## 4. The factorization lemma for two algebras

First suppose \(A,B\) are unital and \(W\) is a finite-dimensional simple \(A\otimes B\)-module. Choose a simple \(A\)-submodule \(M\subset W\), which exists by minimal nonzero dimension. Every \(bM\), \(b\in B\), is zero or an isomorphic simple \(A\)-module, because the two actions commute. Their sum is a nonzero \(A\otimes B\)-submodule and hence equals \(W\).

This sum is a direct sum of copies of \(M\): choose a maximal linearly independent direct sum of such simple submodules; any further simple submodule either has zero intersection and enlarges the sum, or has nonzero intersection and is contained in it. Finite dimension makes the procedure terminate. Since \(\operatorname{End}_A(M)=\mathbb C\), evaluation therefore gives an isomorphism
\[
M\otimes N\longrightarrow W,\qquad m\otimes\phi\longmapsto\phi(m),
\qquad N=\operatorname{Hom}_A(M,W).
\tag{4.1}
\]
Here \(B\) acts on \(N\) by \((b\phi)(m)=b\phi(m)\). If \(N'\) were a nonzero proper \(B\)-submodule, (4.1) would give the nonzero proper \(A\otimes B\)-submodule \(M\otimes N'\). Thus \(N\) is simple. The \(A\)-isomorphism class of \(M\) is the sole simple type in the restriction of \(W\), and (4.1) then determines \(N\). Conversely, tensor products of finite-dimensional simple modules are simple: Lemma 3.1 realizes every matrix on each factor, and tensor products of matrix units realize every matrix on their tensor product. We have proved both existence and uniqueness in the finite-dimensional case.

**Theorem 4.1 — admissible factorization with local units.** Let \(A,B\) have directed families of local units. Let \(V\) be a simple nondegenerate \(A\otimes B\)-module such that
\[
\dim (e\otimes f)V<\infty
\tag{4.2}
\]
for all local units \(e,f\). Then
\[
V\simeq S\otimes T,
\tag{4.3}
\]
where \(S,T\) are simple nondegenerate modules for \(A,B\), respectively. They are admissible for their respective local-unit families and are unique up to isomorphism. Conversely, the tensor product of two such simple admissible modules is simple and admissible.

**Proof.** Choose \(e,f\) for which \(W=(e\otimes f)V\ne0\). Lemma 3.2 makes \(W\) simple over
\[
(eAe)\otimes(fBf).
\]
The finite-dimensional argument gives \(W=M\otimes N\). Extend \(M,N\) to simple \(A,B\)-modules \(S,T\) by Lemma 3.2. Their endomorphism rings are \(\mathbb C\).

We check that \(S\otimes T\) is simple even when the factors are infinite-dimensional. Write a nonzero tensor as \(\sum_{i=1}^r s_i\otimes t_i\) with the \(s_i\) independent and some \(t_1\ne0\). Lemma 3.1 gives an \(a\in A\) with \(as_1=s\ne0\) and \(as_i=0\) for \(i>1\). A local unit of \(B\) fixes the finitely many \(t_i\), so an actual element of \(A\otimes B\) sends the tensor to \(s\otimes t_1\). Simplicity of both factors now generates every pure tensor, and hence the whole tensor product.

Moreover,
\[
(e\otimes f)(S\otimes T)=eS\otimes fT=M\otimes N=W.
\]
Uniqueness of the simple extension in Lemma 3.2, applied to \(A\otimes B\), identifies \(V\) with \(S\otimes T\).

For any other local unit \(e'\) of \(A\),
\[
(e'\otimes f)V=e'S\otimes N.
\]
Its finite dimension and \(\dim N>0\) imply \(\dim e'S<\infty\). Similarly every \(f'T\) is finite-dimensional. This proves local admissibility. The converse admissibility follows from
\((e\otimes f)(S\otimes T)=eS\otimes fT\), and the simplicity proof just given applies to the converse as well.

Finally, the restriction of \(S\otimes T\) to \(A\) is an algebraic direct sum of copies of \(S\), by choosing a vector-space basis of \(T\). If \(S'\otimes T'\simeq S\otimes T\), embed \(S'\) using any nonzero vector of \(T'\), compose with the isomorphism, and project onto a nonzero coordinate copy of \(S\). This gives a nonzero homomorphism between simple modules, so \(S'\simeq S\). The same argument for \(B\) gives \(T'\simeq T\). \(\square\)

There is a natural separate \(A\)-action and \(B\)-action on a nondegenerate \(A\otimes B\)-module, even when neither algebra has an identity. If \((e\otimes f)v=v\), define
\[
av=(ae\otimes f)v,\qquad bv=(e\otimes bf)v.
\tag{4.4}
\]
Common larger local units compare two choices: multiplying on the right by \(e\otimes f\) reduces the larger formula to the smaller one. Thus these actions are well defined and commute. They are the local actions used below.

The finite-dimensional corner in (4.2) is the crucial hypothesis. The countable-dimensional versions often used in automorphic representation theory satisfy it by admissibility. Countable dimension alone is not substituted for (4.2), and no compatibility of infinitely many independently chosen finite-stage isomorphisms is presumed.

## 5. Spherical lines and the construction of adelic representations

**Lemma 5.1 — the spherical line for \(\mathrm{GL}_2\).** If \(V_p\) is an irreducible admissible \(G_p\)-representation and \(V_p^{K_p}\ne0\), then
\[
\dim V_p^{K_p}=1.
\tag{5.1}
\]

**Proof.** The spherical Hecke algebra \(e_p\mathcal H_pe_p\) is commutative. Here is a proof that does not use the Satake isomorphism of the next lesson. Transpose is a Haar-preserving anti-automorphism of \(G_p\), so
\[
(f*h)^{\mathrm t}=h^{\mathrm t}*f^{\mathrm t},\qquad
f^{\mathrm t}(g)=f(g^{\mathrm t}).
\]
It preserves Haar measure because it interchanges left and right invariant Haar measures and fixes \(K_p\) of volume one. Every \(K_p\)-double coset is fixed by transpose: the elementary-divisor decomposition writes it as
\(K_p\operatorname{diag}(p^a,p^b)K_p\), and transposing retains this double coset. Thus every bi-\(K_p\)-invariant function is fixed by transpose. Applying the displayed identity to its convolution proves commutativity.

By Lemma 3.2 and Lesson 5, \(V_p^{K_p}\) is a simple finite-dimensional module for this commutative algebra. A commuting collection of complex matrices has a common eigenvector: successively restrict to an eigenspace of a nonscalar member; these invariant spaces decrease in dimension until all remaining members are scalar. The resulting eigenline is invariant. Simplicity says it is the whole space. \(\square\)

Choose admissible local representations \(V_\infty,V_p\), and suppose \(V_p^{K_p}\) is one-dimensional for almost all \(p\). Choose a nonzero \(\xi_p\) on each of those lines. Define
\[
V=V_\infty\otimes\bigotimes_p'V_p.
\tag{5.2}
\]
The finite adelic group acts componentwise. If \(g=(g_p)\in G_f\), then \(g_p\in K_p\) for almost all \(p\); those components fix \(\xi_p\). Consequently the formula acts on the direct limit. The Lie algebra and compact group at infinity act on \(V_\infty\).

**Theorem 5.2 — restricted tensor products of admissible representations.** The module (5.2) is smooth at the finite places and globally admissible. If all its local representations are irreducible, it is irreducible. Its isomorphism class is independent of the chosen \(\xi_p\) on the distinguished lines.

**Proof.** Every vector belongs to a finite tensor stage. A finite set of local smooth vectors is fixed by suitable compact open subgroups at the active finite primes. Outside that stage the \(K_p\) fix the reference vectors. A rectangular compact open subgroup of \(G_f\) therefore fixes the given vector, proving smoothness.

Let \(S\) contain all exceptional primes, and let
\[
U=\prod_{p\in S}U_p\times\prod_{p\notin S}K_p.
\]
For a finite set \(E\) of archimedean compact types, exact averaging gives
\[
e_E V^U=
e_E V_\infty\otimes
\bigotimes_{p\in S}V_p^{U_p}\otimes
\bigotimes_{p\notin S}\mathbb C\xi_p.
\tag{5.3}
\]
Indeed a vector may initially use an enlarged finite stage \(T\). Averaging its factors at \(T\setminus S\) over \(K_p\) puts them into \(\mathbb C\xi_p\), so the vector returns to the stage \(S\). Averaging at the active primes and applying \(e_E\) give exactly the right-hand side. All displayed non-tail factors are finite-dimensional. An arbitrary compact open subgroup contains a rectangular one; its fixed space is a subspace of the corresponding finite-dimensional space. This proves global admissibility.

For irreducibility, each local simple admissible module has scalar endomorphisms by Lemma 3.2, using any nonzero finite-dimensional corner. Take a nonzero vector of a global submodule at a finite stage \(S\). Repeated use of Lemma 3.1 on its finitely many tensor factors isolates a nonzero pure tensor. At an inactive prime the vector is the nonzero \(\xi_p\); it generates \(V_p\) by local simplicity. Applying operators at any finitely many additional primes therefore generates every larger finite stage. The union of those stages is \(V\). The submodule is consequently all of \(V\).

Finally, the fixed spaces used as reference spaces are one-dimensional. Any two nonzero choices are scalar multiples outside a finite set, so Proposition 1.1 gives the equivariant isomorphism. \(\square\)

If invariant positive inner products are chosen locally and \(\|\xi_p\|=1\), the finite-stage tensor inner products are compatible, since the transition (1.1) is isometric. Their union is a pre-Hilbert space and may be completed. This describes the usual Hilbert restricted tensor product. The algebraic theorem concerns (5.2); completing a space is not part of its definition.

## 6. Flath's theorem: extracting and assembling the factors

**Theorem 6.1 — the tensor product theorem.** Every irreducible admissible
\[
(\mathfrak{gl}_2(\mathbb C),O(2))\times\mathrm{GL}_2(\mathbb A_f)
\]
module \(V\) is isomorphic to
\[
\pi_\infty\otimes\bigotimes_p'\pi_p,
\tag{6.1}
\]
where \(\pi_\infty\) is an irreducible admissible archimedean module, each \(\pi_p\) is an irreducible admissible smooth \(G_p\)-representation, and \(\pi_p^{K_p}\) is one-dimensional for almost all \(p\). Each local isomorphism class is uniquely determined by \(V\).

**Proof.** Regard \(V\) as a simple nondegenerate \(\mathcal H\)-module using Section 2. For every place \(v\), regroup the algebra into
\[
\mathcal H=\mathcal H_v\otimes\mathcal H^{\,v},
\tag{6.2}
\]
where the second algebra records all other places and has its product local units. The global admissibility condition is precisely (4.2) for this pair. Theorem 4.1 extracts a unique simple admissible factor \(\pi_v\). Formula (4.4) identifies its separate local action on \(V\). In particular, as a module for one place, \(V\) is an algebraic direct sum of copies of \(\pi_v\).

Choose \(0\ne w\in V\). Its finite stabilizer contains
\[
\prod_{p\in S_0}U_p\times\prod_{p\notin S_0}K_p
\]
for some finite \(S_0\). For \(p\notin S_0\), \(e_pw=w\ne0\). In the factorization \(V=\pi_p\otimes V^{\,p}\), this says \(e_p\pi_p\ne0\). Lemma 5.1 makes that space a line. We have proved almost-everywhere unramifiedness before constructing any infinite tensor product. Choose nonzero \(\xi_p\) on these lines.

It remains to assemble the local factors coherently. For a finite set \(S\supset\{\infty\}\cup S_0\), put
\[
K^S=\prod_{p\notin S}K_p,\qquad V_S=V^{K^S},
\qquad
\mathcal H_S=\mathcal H_\infty\otimes\bigotimes_{\substack{p\in S\\p<\infty}}\mathcal H_p.
\tag{6.3}
\]
Averaging over the compact group \(K^S\) defines a projection \(P^S\) on \(V\). This average is a finite sum on each vector: its open stabilizer in the compact group has finite index. \(P^S\) is a multiplier projection; we do not insert nonexistent identities of the active local Hecke algebras. The space \(V_S\) is nonzero because it contains \(w\), and it is admissible for \(\mathcal H_S\).

We claim it is also simple for \(\mathcal H_S\). In the local decomposition for \(p\notin S\), the algebra \(e_p\mathcal H_pe_p\) acts on the line \(e_p\pi_p\) by a character. Therefore it acts by that scalar on \(e_pV\), and in particular on \(V_S\). All the tail spherical algebras act by their scalar characters. Algebraically,
\[
P^S\mathcal H P^S=
\mathcal H_S\otimes\bigotimes_{p\notin S}'(e_p\mathcal H_pe_p)
\tag{6.4}
\]
as operators with local units. On \(V_S\), the tail in (6.4) acts scalarly.

Let \(U\ne0\) be an \(\mathcal H_S\)-submodule of \(V_S\). Simplicity of \(V\) gives \(\mathcal HU=V\). Applying \(P^S\) and using \(P^SU=U\), (6.4) gives
\[
V_S=P^S\mathcal HU
=P^S\mathcal HP^SU=U.
\]
The last equality uses the scalar tail action and nondegeneracy of the \(\mathcal H_S\)-action. This proves the claim.

Repeated application of Theorem 4.1 now gives
\[
V_S\simeq\bigotimes_{v\in S}\pi_v.
\tag{6.5}
\]
To identify these factors with the ones already extracted from \(V\), restrict the inclusion \(V_S\subset V\) to any \(v\in S\). The simple \(v\)-factor of \(V_S\) embeds into the direct sum of copies of \(\pi_v\) in \(V\); a nonzero coordinate projection identifies the two simple modules. Thus (6.5) uses one fixed isomorphism class at each place.

Enumerate the remaining primes and choose a cofinal chain
\[
B_0=S_0\cup\{\infty\}\subset B_1\subset B_2\subset\cdots
\]
adding one prime at a time. Set \(T_n=\bigotimes_{v\in B_n}\pi_v\), with transitions inserting the \(\xi_p\). Choose an isomorphism \(\phi_0:T_0\to V_{B_0}\). Suppose \(\phi_n\) has been chosen and the next prime is \(q\). Choose any isomorphism \(T_{n+1}\to V_{B_{n+1}}\) from (6.5). Its restriction to
\[
T_n\otimes\mathbb C\xi_q
=T_{n+1}^{K_q}
\]
is an isomorphism onto
\[
V_{B_{n+1}}^{K_q}=V_{B_n}.
\]
Both this restriction and \(\phi_n\) are isomorphisms of the simple \(\mathcal H_{B_n}\)-module. Their ratio is a scalar, by Lemma 3.2 using a nonzero finite-dimensional corner. Rescale the new isomorphism so that its restriction is \(\phi_n\). This constructs compatible \(\phi_n\) inductively.

Every vector of \(V\) is fixed by \(K^S\) for a sufficiently large finite \(S\), by smoothness at finite level. Hence \(\bigcup_nV_{B_n}=V\). Taking direct limits of the compatible maps proves (6.1). Any global Hecke element belongs to a sufficiently large finite stage, so the limit map is \(\mathcal H\)-equivariant. The dictionaries of Section 2 and Lesson 5 make it equivariant for the stated mixed action.

For uniqueness, restriction of (6.1) to one place is a direct sum of copies of \(\pi_v\). The nonzero-coordinate argument in Theorem 4.1 shows that any second factorization has an isomorphic factor at that place. This holds at every place. \(\square\)

The same proof works over any number field, with one archimedean algebra for the product of its real and complex places, and with \(\mathrm{GL}_2(\mathcal O_v)\) at finite places. There are countably many places, compact supports and smooth vectors have finitely many deviations, and elementary divisors and transpose prove Lemma 5.1 over each nonarchimedean local field. The finite product at infinity separates further by Theorem 4.1. Over a global function field there are no archimedean factors; the proof uses just the finite-place algebras. No special property of a rational class number is used.

## 7. What the local factors tell us about cusp forms

An irreducible cuspidal Hilbert constituent has an irreducible admissible module of finite vectors by Lessons 3–4. Theorem 6.1 applies to that module. Thus the symbols \(\pi_\infty,\pi_p\) have a precise meaning independent of a chosen realization of automorphic functions. Almost all finite components are unramified.

Local central characters are compatible with the global one. In the tensor realization, a finite idèle scalar acts by the product of the local scalars. For almost every \(p\), a central unit lies in \(K_p\) and fixes the nonzero spherical vector, so the local central character is trivial on \(\mathbb Z_p^\times\). Only finitely many factors in this product are nontrivial. This agrees with the product convention for Hecke characters used in Lesson 2.

Suppose an irreducible cuspidal constituent contains the holomorphic weight-\(k\) lift of Lesson 2, fixed by \(K_1(N)\). In particular its positive real centre acts trivially, as required by that lift's normalization. The local lowering argument of Lesson 11, Theorem 7.1, gives
\[
\pi_\infty=D_k.
\]
For \(p\nmid N\), \(K_1(N)_p=K_p\), so (5.3) gives \(\pi_p^{K_p}\ne0\). Thus \(\pi_p\) is unramified outside \(N\). At a ramified prime, the local conductor theorem of Lesson 8 gives the fixed-space dimension once the local representation is generic. The global genericity and multiplicity-one arguments establishing the general classical newform identification remain in Lesson 15.

This theorem supplies the first forward hypothesis in Lesson 8, Section 5. It does not supply its separate Whittaker factorization or multiplicity-one hypotheses. Once those are proved, the vector of minimal level is the holomorphic lowest vector at infinity tensored with each local newvector; the one-dimensional local lines make this a pure tensor. General vectors in the representation remain finite sums of pure tensors.

Here is a completely specified example which does not need a future multiplicity-one argument. Lesson 3, Section 6, proves that the lift of
\[
\Delta(z)=q\prod_{n\ge1}(1-q^n)^{24}
\]
lies in one irreducible cuspidal constituent: its level-one, holomorphic weight-twelve joint space is one-dimensional. Denote that constituent's finite-vector module by \(\pi_\Delta\). The tensor product theorem gives
\[
\pi_\Delta=D_{12}\otimes\bigotimes_p'\pi_{\Delta,p},
\qquad \pi_{\Delta,p}^{K_p}=\mathbb C\xi_p\ \text{for every }p.
\tag{7.1}
\]
The positive weight-twelve line in \(D_{12}\) killed by lowering is one-dimensional. Formula (5.3) consequently identifies the line of the lift with
\[
\mathbb C\left(v_{12}\otimes\bigotimes_p\xi_p\right).
\]
This is a line statement, not a claim of a canonical normalization of all factors.

We can compute the finite component at \(2\). Through degree \(q^3\), the product defining \(\Delta\) is
\[
q(1-q)^{24}(1-q^2)^{24}
=q-24q^2+(276-24)q^3+O(q^4).
\]
Thus \(\tau(2)=-24\) and \(\tau(3)=252\). Let
\(C_p=1_{K_p\operatorname{diag}(p,1)K_p}\).
The Hecke normalization proved in Lesson 2, Section 5, makes \(C_p\) act on the spherical line by \(p^{1-k/2}a_p\). For \(\Delta\),
\[
C_2\xi_2=-\frac34\,\xi_2.
\tag{7.2}
\]
The local classification of Lesson 7 and the conductor calculations of Lesson 8 allow two spherical possibilities: an infinite-dimensional unramified principal series or a character \(\chi\circ\det\). In the latter case, the trivial central character gives \(\chi(2)^2=1\); the mass of the double coset is \(3\), so \(C_2\) would act by \(3\chi(2)=\pm3\), contradicting (7.2). Thus the component is an unramified principal series.

For clarity, its spherical eigenvalue can be computed before any Satake theorem. If its inducing characters have values \(\alpha,\beta\) at \(p\), evaluate the \(K_p\)-fixed compact-model vector at \(1\). The right cosets of the double coset have representatives
\[
\begin{pmatrix}p&b\\0&1\end{pmatrix}\quad(b\bmod p),
\qquad \begin{pmatrix}1&0\\0&p\end{pmatrix}.
\]
Normalized induction gives the respective values \(p^{-1/2}\alpha\) and \(p^{1/2}\beta\). Each right coset has volume one. Their sum is \(\sqrt p(\alpha+\beta)\). The product \(\alpha\beta\) is the value of the central character at \(p\). Consequently the normalized parameters at \(2\) satisfy
\[
\sqrt2(\alpha_2+\beta_2)=-\frac34,\qquad
\alpha_2\beta_2=1,
\]
the second equality coming from the trivial central character. Solving the quadratic gives
\[
\alpha_2=\frac{-3+i\sqrt{119}}{8\sqrt2},
\qquad
\beta_2=\frac{-3-i\sqrt{119}}{8\sqrt2}.
\tag{7.3}
\]
Their sum is \(-3/(4\sqrt2)\), their product is \((9+119)/128=1\), and each has absolute value one. Let \(\mu_1,\mu_2\) be the unramified characters of \(\mathbb Q_2^\times\) with these values at \(2\). Their ratio has absolute value one and hence is neither \(|\cdot|_2\) nor \(|\cdot|_2^{-1}\). The local classification in Lesson 7 identifies
\[
\pi_{\Delta,2}=I(\mu_1,\mu_2),
\qquad
L(z,\pi_{\Delta,2})=
\frac1{1+\frac{3}{4\sqrt2}\,2^{-z}+2^{-2z}}.
\tag{7.4}
\]
All scalar normalizations in this example have been accounted for. The absolute values in (7.3) were computed for this particular pair; no general Ramanujan bound was inferred from unitarity.

## 8. Exercises and complete solutions

**Exercise 8.1 (easy).** Replace the spherical reference vectors \(\xi_p\) by nonzero \(\xi'_p\). Prove that the restricted tensor products are isomorphic, explain the finite-stage scalar, and determine when the resulting map preserves compatible unitary inner products.

**Solution 8.1.** At all but finitely many primes the fixed space is a line, so \(\xi'_p=c_p\xi_p\). Include the exceptional primes in \(S_0\). On the finite stage \(S\), use multiplication by \(\prod_{p\in S\setminus S_0}c_p\). When one new prime \(q\) is inserted, the old transition uses \(\xi_q\); multiplying by the new scalar changes that factor to \(c_q\xi_q=\xi'_q\). This proves compatibility, and the inverse uses the reciprocals. All maps commute with the local actions, proving the isomorphism.

If both reference vectors have norm one in the same local inner product, then \(|c_p|=1\). Every stage map is then multiplication by a scalar of absolute value one and is an isometry for the tensor inner products. It extends to an isometry of the Hilbert completions. If a reference vector has nonunit norm, the unmodified transition \(x\mapsto x\otimes\xi_p\) is not isometric; the claimed compatible tensor norms must first normalize it. The algebraic construction itself needs only nonzero vectors.

**Exercise 8.2 (medium).** Prove the factorization lemma for algebras with approximate identities. State exactly which meaning of approximate identity and which admissibility assumption are needed.

**Solution 8.2.** Here the approximate identities are algebraic local units, not merely nets converging in a norm. Thus finite sets of algebra elements and nondegenerate module vectors are fixed exactly by an idempotent from a directed family. Let \(V\) be simple and assume every product-idempotent range \((e\otimes f)V\) is finite-dimensional. A nonzero vector supplies a product idempotent with nonzero range \(W\). The argument \(RW=V\), followed by its idempotent projection, proves that \(W\) is simple over \((eAe)\otimes(fBf)\).

Choose a simple \(eAe\)-submodule \(M\). The commuting \(fBf\)-translates span \(W\) and are copies of \(M\); finite dimension gives a direct sum of such copies. Thus \(W=M\otimes N\) with \(N=\operatorname{Hom}_{eAe}(M,W)\) simple over \(fBf\). The extension
\(Ae\otimes_{eAe}M\) has a unique maximal submodule: every proper submodule has zero \(e\)-range, and their sum still does. Its simple quotient \(S\) is the unique simple extension of \(M\). Construct \(T\) from \(N\) in the same way.

Both endomorphism rings are scalar, since restriction to their finite corners is injective. The interpolation induction of Lemma 3.1 isolates a nonzero pure tensor in every nonzero submodule of \(S\otimes T\), and simple local actions generate all other pure tensors. So \(S\otimes T\) is simple. Its \(e\otimes f\)-corner is \(W\); uniqueness of the simple extension for the product algebra proves \(V=S\otimes T\). For each \(e'\), the finite range \((e'\otimes f)V=e'S\otimes N\) makes \(e'S\) finite-dimensional, and similarly for \(T\). The direct-sum restriction argument proves uniqueness. This is the full lemma; countability is not an extra step needed in this admissible proof.

**Exercise 8.3 (medium).** Prove that the local factors of an irreducible admissible adelic module are unramified at almost every prime, without putting that condition into the definition of factorization.

**Solution 8.3.** Extract the factor \(\pi_p\) from the binary algebra decomposition \(\mathcal H=\mathcal H_p\otimes\mathcal H^{\,p}\), using Exercise 8.2. Pick a single nonzero adelic vector \(w\). Its finite stabilizer contains a rectangular subgroup whose factors are \(K_p\) outside a finite set \(S_0\). Hence \(e_pw=w\ne0\) for all \(p\notin S_0\). On the binary tensor decomposition this operator is \(e_p\otimes1\); a nonzero fixed vector forces \(e_p\pi_p\ne0\). That is exactly unramifiedness.

To get the reference line rather than just a fixed space, transpose fixes every \(K_p\)-double coset by elementary divisors and reverses convolution. The spherical algebra is therefore commutative. Its nonzero simple admissible corner \(e_p\pi_p\) is finite-dimensional and has a common eigenline, which by simplicity is the whole corner. This proves \(\dim\pi_p^{K_p}=1\) at every prime outside \(S_0\).

**Exercise 8.4 (hard).** Prove uniqueness of all the local factors in (6.1). Describe a multiplicity-space reconstruction, and distinguish uniqueness of factors from uniqueness of the tensor isomorphism.

**Solution 8.4.** Fix a place \(v\). Group the proposed restricted tensor product as \(M\otimes T\), where \(M=\pi_v\) and \(T\) is the product of the other factors. Choosing a vector-space basis of \(T\) makes the restriction to \(\mathcal H_v\) a direct sum of copies of \(M\). If another factorization uses \(M'\), its submodule \(M'\otimes t'\), \(t'\ne0\), maps into this direct sum under the global isomorphism. A coordinate projection is nonzero on some nonzero image vector. Its restriction gives a nonzero \(\mathcal H_v\)-homomorphism \(M'\to M\), which is an isomorphism because both modules are simple. This works independently at every place, including the archimedean algebra.

Once a model \(M\) is fixed, put
\[
T_M=\operatorname{Hom}_{\mathcal H_v}(M,V).
\]
The remaining-place algebra acts on these homomorphisms by acting on their values. Evaluation
\[
M\otimes T_M\longrightarrow V,\qquad m\otimes\phi\longmapsto\phi(m)
\tag{8.1}
\]
is an isomorphism. Indeed \(V\) is a direct sum of copies of \(M\), and
\(\operatorname{End}_{\mathcal H_v}(M)=\mathbb C\). A homomorphism from \(M\) into that direct sum has finite coordinate support: \(M\) is cyclic, its generator has an image with finite support, and applying the algebra does not add new coordinate positions. Thus its Hom space is the algebraic direct sum of one-dimensional coordinate Hom spaces. Evaluation is the usual direct-sum isomorphism, and is equivariant for both actions.

Changing the identification of \(M\), changing its nonzero spherical vector, or scaling a global isomorphism changes the map while preserving every local isomorphism class. With fixed local models and fixed reference vectors, two global isomorphisms differ by a scalar: the global simple admissible module has scalar endomorphisms by its finite corner. The theorem asserts uniqueness of the local representations up to isomorphism, not a canonical map with canonical vectors.

## 9. What this lesson does not prove, and source comparison

The algebraic results promised here are proved: the restricted-product construction and choice independence on lines; the exact finite adelic Hecke-algebra product; the two-algebra factorization lemma with local units; admissibility and irreducibility of the constructed representations; full mixed Flath factorization; almost-everywhere unramifiedness; and uniqueness. The archimedean algebra is used through compatible \((\mathfrak g,K)\)-modules, with its local-unit realization explained in Section 2.

The following earlier inputs remain with their owners.

- Compact unitarization is in the compact representation prerequisite, Proposition 1.2, and its Hilbert-space decomposition is Theorem 3.1; Schur orthogonality is in Matrix coefficients and the Peter–Weyl theorem, Theorem 2.1. Both are linked in Section 2.
- Smooth nonarchimedean representations and nondegenerate Hecke modules are equivalent by Lesson 5, Proposition 2.1; its Proposition 1.1 gives the averaging projections. The interpolation and extension arguments needed beyond that dictionary are proved here.
- Admissibility and the finite-vector comparison for cuspidal Hilbert constituents are the analytic inputs of Lesson 3, Theorem 3.2 and Section 4, together with the discreteness theorem of Lesson 4. The new proof here applies to the resulting algebraic modules.
- The real holomorphic type \(D_k\) is proved in Lesson 11, Theorem 7.1. Its Section 11 isolates smooth globalization and the analytic comparison results. No globalization theorem is used to prove Theorem 6.1.
- The general newform-to-constituent identification, nonzero factored global Whittaker functional and global multiplicity one are reserved for Lesson 15. The conditional statements of Lesson 8, Section 5, continue to identify those separate hypotheses.

The tensor product theorem is due to Flath (Corvallis proceedings, 1979). It is treated in Jacquet–Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf), Section 9, Proposition 9.1 and Lemmas 9.1.1–9.1.2, and in Getz–Hahn, [*An Introduction to Automorphic Representations*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), draft of April 2022, Sections 5.6–5.7, Theorems 5.7.1–5.7.2.

Jacquet–Langlands builds the factorization through compatible images of finite Hecke corners. Getz–Hahn treats the finite-place restricted product. There is also a unitary Hilbert-space form of the theorem. Here the finite-corner extension lemma gives a proof in the algebraic admissible category, followed by an explicit scalar normalization along a cofinal chain. This supplies the compatibility needed to pass from finitely many local factors to the adelic module.
