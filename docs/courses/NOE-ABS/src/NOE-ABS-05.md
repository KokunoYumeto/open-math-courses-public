# Normal integral bases in tame extensions

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A field can have a basis consisting of the conjugates of one element even when its ring of integers cannot. The obstruction is already visible in the trace. In a tame extension the trace supplies the averaging operation needed for projectivity; an additional argument turns that projectivity into a normal integral basis over a local base.

We use Three differents. Its Theorem 5.2 proves the decomposition into completed DVR factors and links the full exact-completion and faithful-flatness proofs of Completion, Theorems 3.1–3.2. Prime transitivity over a general Dedekind base is proved in Section 1 below. The finite-algebra proofs in Section 4 and the averaging argument in Section 5 supply the representation facts used here. For number fields, the prime-transitivity and inertia results are Hilbert's ramification theory in Galois extensions, Theorems 6.1 and 6.2. Its residue fields are finite; the argument below retains arbitrary residue fields. The arithmetic different is treated in **The different and the discriminant**, and the field normal basis theorem, over every base field and in every characteristic, is proved in [Hilbert 90 in Noether's form and Galois descent, Theorem 4.0](https://kokunoyumeto.github.io/open-math-courses-public/courses/NOE-HYP/NOE-HYP-06.html#normal-bases-in-every-characteristic). Section 4 proves characteristic-zero projective rigidity and the positive-characteristic step, including descent to the original coefficient DVR. Basic references are [Noether], [Milne FT] and [Swan].

## 1. The integral question and the meaning of local

Let \(A\) be a Dedekind domain with fraction field \(K\), let \(L/K\) be finite Galois with group \(G\), and let \(B\) be the integral closure of \(A\) in \(L\). The finiteness theorem in Noether's axioms for Dedekind domains makes \(B\) finite over \(A\). For a nonzero prime \(\mathfrak p\), put

\[
 R=A_{\mathfrak p},\qquad M=B\otimes_A R,\qquad
 \widehat R=\varprojlim R/\mathfrak p^nR,\qquad
 \widehat M=M\otimes_R\widehat R.
\]

Here “localized” refers to \(R,M\), and “completed” to \(\widehat R,\widehat M\). The latter is generally a product, not a domain:

\[
 \widehat M=\prod_{\mathfrak P\mid\mathfrak p}\widehat{B_{\mathfrak P}}.
\]

The group acts on this entire product, permuting its factors. Its fraction algebra is \(L\otimes_K\operatorname{Frac}(\widehat R)\).

A **normal integral basis generator** is an element \(a\in M\) for which \(\{g(a):g\in G\}\) is an \(R\)-basis. Equivalently, the map \(R[G]\to M\), \(g\mapsto g(a)\), is an isomorphism of left modules. The completed definition is identical. Both underlying modules are free of rank \(|G|\) over their DVR bases.

The [field normal basis theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/NOE-HYP/NOE-HYP-06.html#normal-bases-in-every-characteristic) says \(L\simeq K[G]\) as left \(K[G]\)-modules [Milne FT, Theorem 5.18]. Scalar extension gives the same assertion for the fraction algebra of \(\widehat M\), including when it is a product.

We call \(\mathfrak p\) **tame** when every \(e_{\mathfrak P}\) is prime to the residue characteristic and every residue extension is separable. In residue characteristic zero, the first condition is automatic. The ramification and residue conditions are constant on the primes above \(\mathfrak p\), since \(G\) acts transitively on them. This definition allows the residue degree, and even \(|G|\), to be divisible by the residue characteristic.

For completeness, prime transitivity holds over our general Dedekind base as follows. If \(\mathfrak Q\) lies outside the orbit of \(\mathfrak P\), the Chinese remainder theorem gives \(x\in\mathfrak Q\) with \(x\equiv1\) at every prime in that orbit. The norm \(N=\prod_{g\in G}g(x)\) belongs to \(B^G=B\cap K=A\), since \(A\) is integrally closed. It lies in \(\mathfrak Q\cap A=\mathfrak p\), while no factor lies in \(\mathfrak P\), a contradiction. Conjugation then identifies the corresponding localized extensions and residue extensions, so their ramification indices and separability conditions agree. This uses no perfect-residue-field hypothesis.

## 2. Trace detects tameness

**Theorem 2.1.** With this notation,

\[
 \operatorname{Tr}_{L/K}(M)=R
 \quad\Longleftrightarrow\quad
 \mathfrak p\text{ is tame}.
\]

**Proof.** Write \(\pi\) for a uniformizer of \(R\). The trace image is an ideal, so it fails to be \(R\) precisely when it lies in \(\pi R\). By the definition of the complementary module,

\[
 \operatorname{Tr}(M)\subseteq\pi R
 \Longleftrightarrow \pi^{-1}\in M^*
 \Longleftrightarrow M\subseteq\pi M^*
 =\pi\mathfrak D^{-1}.
\tag{2.1}
\]

The middle equivalence uses that \(M^*\) is an \(M\)-module. On the \(\mathfrak P\)-component, the final containment means

\[
 d_{\mathfrak P}=v_{\mathfrak P}(\mathfrak D)\ge e_{\mathfrak P}.
\tag{2.2}
\]

The complete different-exponent proof in Three differents, Theorem 5.3, gives \(d\ge e-1\), with equality precisely in the tame case, including inseparable residue extensions. This proves the assertion using that all components have the same ramification behavior.

Here is also a direct verification covering imperfect residue fields. Trace commutes with reduction of the multiplication matrix. In the \(\mathfrak P\)-component of \(M/\pi M\), the filtration by powers of its maximal ideal has \(e_{\mathfrak P}\) successive quotients isomorphic to \(\ell_{\mathfrak P}=B/\mathfrak P\). Multiplication by \(b\) acts on each quotient as multiplication by its residue. Consequently its trace over \(k=R/\pi R\) is

\[
 e_{\mathfrak P}\operatorname{Tr}_{\ell_{\mathfrak P}/k}(\bar b).
\tag{2.3}
\]

The components can be chosen independently by the Chinese remainder theorem. A finite field extension has nonzero trace exactly when it is separable, by the trace criterion in the discriminant lesson. A nonzero linear map to \(k\) is onto. Thus the trace modulo \(\pi\) is onto precisely when at least one component has separable residue extension and \(e_{\mathfrak P}\ne0\) in \(k\). In the Galois situation this says exactly tameness. Nakayama, or the ideal criterion above, lifts surjectivity to \(R\). \(\square\)

The lower-bound proof in that earlier Theorem 5.3 uses only multiplication matrices. In a completed local component \(S\), write \(\pi S=t^eS\). If \(z\in t^{1-e}S\) and \(y\in S\), then \(\pi zy\in tS\), whose multiplication matrix modulo \(\pi\) is nilpotent because \(t^e\in\pi S\). Its trace is zero in the residue field, so \(\operatorname{Tr}(zy)\in R\). This proves \(t^{1-e}S\subseteq S^*\), hence \(d\ge e-1\). Equations (2.1)–(2.3) distinguish equality from the strict alternative without a uniqueness-of-valuation premise.

For a non-Galois extension (2.3) gives a different statement: trace surjectivity requires **some** tame component. It need not make all components tame.

## 3. Higman's criterion: averaging an endomorphism

For a left \(R[G]\)-module \(N\), define

\[
 T_G(\phi)=\sum_{g\in G}g\phi g^{-1},\qquad
 \phi\in\operatorname{End}_R(N).
\]

The sum commutes with \(G\), even when \(|G|\) is not invertible.

**Theorem 3.1 (Higman's criterion).** If \(N\) is finitely generated projective over a commutative ring \(R\), then \(N\) is projective over \(R[G]\) if and only if \(T_G(\phi)=1_N\) for some \(R\)-linear \(\phi\).

**Proof.** Give \(F=R[G]\otimes_R N\) the action on its first factor only. It is projective over \(R[G]\), because an \(R\)-projective module is a summand of a free module and tensoring preserves that splitting. The equivariant map

\[
 \epsilon:F\longrightarrow N,\qquad g\otimes n\longmapsto g(n)
\]

is onto. Given \(\phi\), set

\[
 s(n)=\sum_g g\otimes\phi(g^{-1}n).
\]

Reindexing by \(g=hu\) proves \(s(hn)=h s(n)\), and \(\epsilon s=T_G(\phi)\). If this is the identity, \(N\) is a direct summand of \(F\).

Conversely, projectivity splits \(\epsilon\). Write an equivariant splitting as \(s(n)=\sum_g g\otimes\phi_g(n)\). Equivariance forces \(\phi_g(n)=\phi_1(g^{-1}n)\). Thus \(\epsilon s=1_N\) says \(T_G(\phi_1)=1_N\). \(\square\)

**Corollary 3.2.** In the tame situation, \(M\) is projective over \(R[G]\).

**Proof.** Choose \(t\in M\) with \(\operatorname{Tr}(t)=1\). For multiplication \(\phi(n)=tn\), its conjugate \(g\phi g^{-1}\) is multiplication by \(g(t)\). Their sum is multiplication by \(\sum_g g(t)=1\). Apply Theorem 3.1; \(M\) is free over the DVR \(R\). \(\square\)

This is averaging with an integral element of trace one. Replacing it by division by \(|G|\) would discard tame extensions with a residue degree divisible by the residue characteristic.

## 4. Why a completed projective lattice is free

We first prove the characteristic-zero rigidity needed for the completed lattice.

**Swan's rigidity theorem, in the form used here.** If \(S\) is a complete DVR of characteristic zero, \(F\) its fraction field, and \(P,Q\) finitely generated projective \(S[G]\)-modules, then

\[
 F\otimes_S P\simeq F\otimes_S Q
 \quad\Longrightarrow\quad P\simeq Q.
\]

This is the specialization of [Swan, Section 6, Corollary 6.4, following Theorem 6.1]. The proof below includes mixed characteristic and arbitrary residue fields. We first establish the field-descent lemma used at its final step. Positive characteristic is handled separately by Lemma 4.2.

**Lemma 4.1 (descent over fields).** Let \(C\) be a finite-dimensional algebra over a field \(k\). Finite-dimensional \(C\)-modules that become isomorphic after a field extension \(E/k\) are already isomorphic over \(k\).

**Proof.** The space of module homomorphisms is the solution space of finitely many linear equations in matrix entries, so it commutes with extending the field. Choose a \(k\)-basis of \(\operatorname{Hom}_C(U,V)\); the determinant of a linear combination is a polynomial in its coefficients. An isomorphism over \(E\) means this polynomial is not zero. For infinite \(k\), successive specialization of its variables finds a nonzero value in \(k\), giving an isomorphism.

For finite \(k\), choose a finite extension \(k'/k\) large enough that its cardinality exceeds the degree in each variable. A nonzero polynomial cannot vanish on that entire grid, by induction on the variables. This gives an isomorphism over \(k'\). Restriction of scalars then gives \(U^{\oplus d}\simeq V^{\oplus d}\), where \(d=[k':k]\).

The finite-dimensional Krull–Schmidt argument cancels these multiplicities. For completeness, repeated splitting decomposes a finite-dimensional module into indecomposables. Fitting's decomposition \(W=\ker f^n\oplus\operatorname{im}f^n\), for large \(n\), shows that an endomorphism of an indecomposable is either invertible or nilpotent. Its endomorphism ring is local: a nonunit \(f\) is nilpotent, so \(1-f\) is invertible; if a sum of two nonunits were invertible, multiplying by its inverse would contradict that property. When comparing two decompositions, the identity of one summand is a sum of the maps obtained by projecting through the other summands. One such map is a unit in this local endomorphism ring. It makes that summand a direct summand of the corresponding indecomposable on the other side, hence an isomorphic summand. Align and remove the two summands, then induct. Decomposition multiplicities are therefore unique. Equality of \(d\) times every multiplicity implies equality of the original multiplicities. \(\square\)

### A proof of characteristic-zero projective rigidity

For a projective module, \(\operatorname{Hom}(P,-)\) is exact. This lets us measure its simple constituents through homomorphisms rather than through the dimension of its fraction-field representation alone. We will produce enough integral test modules to determine those measurements. The argument proceeds through finite algebras, coefficient extensions and cyclic test modules.

**Lemma 4.A, split finite algebras.** Let \(D\) be a finite-dimensional algebra over a field \(k\). There is a finite algebraic extension \(k_1/k\) such that, for \(D_1=k_1\otimes_kD\), its Jacobson radical \(J\) is nilpotent and

\[
 D_1/J\simeq\prod_{i=1}^r M_{d_i}(k_1).
\]

Over such a splitting field, the trace functionals of the pairwise nonisomorphic simple modules are linearly independent. If two finite projective \(D_1\)-modules have the same dimensions of homomorphisms to every simple module, then they are isomorphic.

**Proof.** Here is the finite algebra argument, including the existence of a splitting extension. For any finite-dimensional algebra, define its radical as the intersection of the annihilators of its simple left modules. Every simple module is a quotient of the regular module, so its isomorphism class occurs among the finitely many factors of a composition series of that regular module. If the series has length \(N\), the radical kills every successive quotient, and consequently its \(N\)-th power is zero.

This radical is also the intersection of the maximal left ideals. One inclusion follows by applying an annihilator to the quotient by a maximal left ideal. For the other, for each nonzero vector \(v\) in a simple module, the surjection \(D\to Dv\), \(a\mapsto av\), has a maximal left ideal as kernel. An element in every such kernel kills every simple module. Finite dimension allows us to select finitely many maximal left ideals with the same intersection. Thus the regular module of the radical quotient embeds in a finite direct sum of simple modules. Such a submodule is semisimple: induct on the number of summands, intersect with the first simple summand, and either remove that contained summand or project injectively to the remaining summands.

Over an algebraic closure \(\bar k\), every endomorphism of a finite-dimensional simple module is scalar. Indeed, a nonzero endomorphism is invertible by its kernel and image, while an eigenvalue \(\lambda\) makes \(f-\lambda\) noninvertible, so \(f=\lambda\). Decompose the semisimple regular module of the radical quotient as \(\bigoplus_i V_i^{m_i}\). Homomorphisms between distinct simples are zero, so its endomorphism algebra is \(\prod_i M_{m_i}(\bar k)\). It is also the opposite of the radical quotient, by right multiplication on the regular module. Transposing the matrix factors gives the asserted product of matrix algebras. For a module \(W\) over \(M_d(k_1)\), matrix units give an isomorphism \(k_1^d\otimes_{k_1}E_{11}W\to W\), sending the \(j\)-th coordinate vector tensored with \(w\) to \(E_{j1}w\); its inverse has coordinates \(E_{1j}w\). Thus a simple module over this factor is its column space, with scalar endomorphisms. The central idempotents of a product show that a simple module is supported on exactly one factor.

Choose bases for the radical and quotient and the coefficients of this matrix-algebra isomorphism and its inverse. Finitely many algebraic coefficients are involved; put them in a finite extension \(k_1/k\). The ideal, its nilpotence identity and the quotient isomorphism then descend to \(k_1\). The descended nilpotent ideal is the radical: a nilpotent ideal kills every simple module, while the quotient product of matrix algebras has zero radical. This proves the splitting assertion, including when the extension needs an inseparable part. In a split quotient, an element lifting the matrix unit \(E_{11}\) in one factor has trace one on its corresponding simple and trace zero on all the others. The simple trace functionals are therefore independent.

Finally, if \(U\) is projective, \(U/JU\) is semisimple. Since the endomorphisms of each simple are scalars, the multiplicity of a simple \(V_i\) in this top quotient is

\[
 \dim_{k_1}\operatorname{Hom}_{D_1}(U,V_i).
\]

Equality of these numbers gives an isomorphism of the top quotients of the two projectives. Compose it with the first quotient map and lift to a module map \(f:U\to V\), using projectivity of \(U\) and the surjection \(V\to V/JV\). Its cokernel \(C\) satisfies \(C=JC\), hence \(C=J^NC=0\). The surjection splits because \(V\) is projective. Its kernel is a direct summand whose top quotient is zero, and the same nilpotence argument kills it. Thus \(f\) is an isomorphism. \(\square\)

**Lemma 4.B, extending the coefficient DVR.** Given a characteristic-zero complete DVR \(S\), a finite extension of its residue field, and a positive integer \(m\) invertible in the residue field, there is a finite field extension \(F'/F\) whose integral closure \(S'\) is a complete DVR, whose residue field contains the prescribed extension, and which contains all \(m\)-th roots of unity. Their reductions are distinct. In particular we can arrange that the residue group algebra is split and that all characters of cyclic subgroups of order prime to the residue characteristic lift to \(S'\).

**Proof.** First, the integral closure \(T\) of \(S\) in any finite extension of \(F\) is finite and Dedekind, by Noether's axioms for Dedekind domains, Theorem 4.1: characteristic zero makes this field extension separable. Its finite torsion-free \(S\)-module is free. To check the latter assertion directly, lift a basis modulo the uniformizer. These lifts generate: their finite cokernel \(M\) satisfies \(M=\pi M\); write generators as \(\pi\)-multiples of one another and apply the adjugate of the coefficient matrix to obtain \((1+\pi a)M=0\), which forces \(M=0\) because \(1+\pi a\) is a unit. A nonzero relation between the lifts, divided by the smallest uniformizer power in its coefficients, would give a nonzero relation between the residue basis vectors. Torsion-freeness permits that division. Freeness also makes \(T\) complete for the base uniformizer.

The ring \(T\) is local. Every maximal ideal contracts to the maximal ideal of \(S\), by integrality, so its maximal ideals correspond to those of \(T/\pi T\). Otherwise this finite-dimensional commutative residue algebra would have a nontrivial idempotent: its radical is nilpotent as in Lemma 4.A, the Chinese remainder theorem splits its distinct maximal ideals, and the resulting idempotents lift across the nilpotent radical. Such an idempotent lifts further to \(T\). For this last assertion, start with \(e\) whose error \(e^2-e\) lies in the uniformizer ideal and iterate

\[
 e\longmapsto e-(e^2-e)(2e-1)^{-1}.
\]

The inverse exists because \((2e-1)^2=1+4(e^2-e)\), and completeness supplies the geometric-series inverse. Each new error lies in the square of the preceding error ideal, so the iterates converge to an idempotent with the prescribed residue. The same finite iteration lifts an idempotent across a nilpotent ideal. A domain has only the idempotents zero and one, contradicting the chosen residue. Thus \(T\) has one maximal ideal. Its nonzero ideals are powers of that ideal by lesson one's factorization theorem; the maximal ideal is invertible and is principal in a local ring, by the finite expression \(1=\sum a_i b_i\) and a unit summand. Hence \(T\) is a DVR. The base-uniformizer and maximal-ideal topologies are equivalent, since the residue algebra has nilpotent maximal ideal, so it is complete as a DVR too.

Now generate the prescribed finite residue extension by finitely many elements. Successively lift each generator's monic minimal polynomial to the current DVR and adjoin a root in an algebraic closure of its fraction field. That root is integral. Its residue satisfies the original polynomial, so irreducibility over the already embedded residue subfield extends the selected embedding to the next generator. The preceding paragraph supplies a complete DVR at each stage; it does not require the residue polynomials to be separable. Finally adjoin the finitely many \(m\)-th roots of unity in characteristic zero.

If an \(m\)-th root \(\zeta\) reduces to one, then

\[
 (\zeta-1)(1+\zeta+\cdots+\zeta^{m-1})=0.
\]

The second factor reduces to the nonzero scalar \(m\), hence is a unit; therefore \(\zeta=1\). Apply this to the ratio of two roots to prove distinct reductions. The reductions identify the two cyclic groups of roots multiplicatively. Use Lemma 4.A to choose the finite residue extension splitting \(k[G]\), and take \(m\) to be the prime-to-residue-characteristic part of \(|G|\); in residue characteristic zero take \(m=|G|\). Split matrix quotients remain split after further field extension. This gives the final assertion. \(\square\)

**Lemma 4.C, cyclic test modules.** Let \(S'\) be a characteristic-zero complete DVR with fraction field \(F'\) and residue field \(k'\). Suppose that \(k'[G]\) is split as in Lemma 4.A and that \(S'\) contains all roots of unity of orders prime to the residue characteristic that divide \(|G|\). In residue characteristic zero, include every order dividing \(|G|\). The classes of the modules

\[
 k'[G]\otimes_{k'[C]} k'_\chi,
\]

where \(C\) runs through these cyclic subgroups and \(\chi:C\to k'^\times\) through their one-dimensional characters, span \(\mathbb Q\otimes_{\mathbb Z}G_0(k'[G])\). Each such module is the reduction of an \(S'\)-free \(S'[G]\)-module.

Here \(G_0\) is generated by isomorphism classes of finite-dimensional modules, with \([V]=[U]+[W]\) for each exact sequence \(0\to U\to V\to W\to0\). It is freely generated by the classes of the simple modules. To see the assertion about freeness, a composition series exists by induction on dimension. Its multiset of simple factors is independent of the series: compare two simple first submodules; if they agree, pass to the common quotient, and if they differ, their intersection is zero and their sum is their direct sum. Compare the two series through this sum, then apply induction to the smaller quotients. A series for a submodule and a series for its quotient concatenate, so each simple multiplicity is additive on exact sequences. These multiplicities give the inverse to the map from the free group on the simples to \(G_0\).

**Proof.** Call an element *regular* here if its order is prime to the residue characteristic; if that characteristic is zero, every element is regular. Let \(m\) be the prime-to-characteristic part of \(|G|\), or \(|G|\) in characteristic zero. Lemma 4.B identifies the groups of \(m\)-th roots in \(S'\) and in \(k'\). For a \(k'[G]\)-module \(V\), a regular element \(g\) acts diagonally, since its minimal polynomial divides \(X^{\operatorname{ord}(g)}-1\), which has distinct roots in \(k'\). Lift each eigenvalue multiplicatively to \(S'\) and add the lifts, with their multiplicities. Denote the resulting \(F'\)-valued function by \(\varphi_V(g)\). It is constant on conjugacy classes and additive on exact sequences: restriction to the cyclic subgroup generated by \(g\) decomposes into its eigenspaces. Thus it defines an additive character on \(G_0\), using only regular elements.

The characters \(\varphi_{V_i}\) of the distinct simple modules are linearly independent over \(F'\). First consider ordinary traces over \(k'\). In positive residue characteristic \(p\), every group element has a commuting decomposition \(g=g_0u\), where \(g_0\) has order prime to \(p\) and \(u\) has \(p\)-power order: choose the two powers of \(g\) by the Chinese remainder theorem on its order. On each eigenspace of \(g_0\), the operator \(u\) is unipotent, because \((u-1)^{p^a}=u^{p^a}-1=0\) for a suitable \(a\). Its trace is the dimension of that eigenspace. Consequently

\[
 \operatorname{tr}(g\mid V)=\operatorname{tr}(g_0\mid V).
\]

In residue characteristic zero we simply take \(g_0=g\). A linear relation between simple trace functions on regular elements would therefore hold on all group elements, hence on the whole group algebra. Lemma 4.A rules this out. Now suppose a nonzero \(F'\)-linear relation between the lifted simple characters existed. Multiply its coefficients by a suitable uniformizer power so that all lie in \(S'\) and at least one is a unit. Reduction gives a nonzero \(k'\)-linear relation between the simple trace functions on regular elements. This is the contradiction just proved.

For a cyclic subgroup \(C\) as in the statement, each character \(\chi\) has a unique multiplicative lift \(\widetilde\chi:C\to S'^\times\). Define the left \(S'[G]\)-module

\[
 T_{C,\chi}=S'[G]\otimes_{S'[C]}S'_{\widetilde\chi}.
\]

A set of left coset representatives gives an \(S'\)-basis, so this module is free over \(S'\); reducing that basis gives exactly the induced module in the statement. Its ordinary fraction-field character agrees, on regular elements, with the lifted character of its reduction. Indeed, for a regular element of order \(d\), the operators

\[
 \frac1d\sum_{j=0}^{d-1}\zeta^{-j}g^j
 \qquad(\zeta^d=1)
\]

are the \(S'\)-linear eigenprojectors on the lattice. Their images are direct summands of a free \(S'\)-module. Their ranks equal the dimensions of their reductions, and they become the corresponding eigenprojectors over \(F'\). Thus eigenvalue multiplicities agree in both fibres.

We next show that these induced characters span all \(F'\)-valued class functions supported on regular elements. The character of \(F'\otimes T_{C,\chi}\) is, by the coset basis,

\[
 u_{C,\chi}(g)=\frac1{|C|}
  \sum_{\substack{x\in G\\x^{-1}gx\in C}}
     \widetilde\chi(x^{-1}gx).
\]

It vanishes on nonregular elements, since none can be conjugate into \(C\). On the vector space of class functions supported on regular elements the bilinear pairing

\[
 \langle f,h\rangle=\frac1{|G|}\sum_{g\in G}f(g)h(g^{-1})
\]

is nondegenerate: characteristic zero makes each nonzero conjugacy-class size invertible in \(F'\), and inversion permutes the regular classes. Substituting the induced-character formula and using conjugacy invariance gives

\[
 \langle f,u_{C,\chi}\rangle
   =\frac1{|C|}\sum_{c\in C}f(c)\widetilde\chi(c^{-1}).
\]

If this is zero for every \(\chi\), cyclic Fourier inversion gives \(f(c)=0\) on \(C\). Explicitly, the sum of all characters at a nonidentity element of \(C\) is zero by a finite geometric sum, while at the identity it is \(|C|\); multiply the displayed equalities by \(\widetilde\chi(c)\) and sum over \(\chi\). Every regular element belongs to a cyclic subgroup of the permitted order, so \(f=0\). Nondegeneracy now proves the spanning assertion for the induced characters.

The restriction of each \(u_{C,\chi}\) to regular elements is an integer combination of the independent \(\varphi_{V_i}\), with coefficients the composition multiplicities of its reduction. Since the induced characters span the entire regular class-function space, their composition-multiplicity vectors have full row rank. The entries of this matrix are integers, and \(F'\) has characteristic zero, so a nonzero maximal minor is also nonzero over \(\mathbb Q\). The same vectors therefore span the rational vector space with basis \([V_i]\). This proves the assertion about \(G_0\). \(\square\)

**Proof of Swan's rigidity theorem.** Put \(k=S/\pi S\). Choose \(S'\) by Lemma 4.B, so that its residue field \(k'\) splits \(k'[G]\) and the hypotheses of Lemma 4.C hold. Scalar extension gives projective left \(S'[G]\)-modules

\[
 P'=S'\otimes_SP,\qquad Q'=S'\otimes_SQ,
\]

with isomorphic fraction-field modules. Their reductions \(P_0,Q_0\) are projective over \(k'[G]\): a finite projective is a direct summand of a finite free module, and both scalar extension and reduction preserve that splitting.

For any test lattice \(T=T_{C,\chi}\), the \(S'\)-module \(\operatorname{Hom}_{S'[G]}(P',T)\) is a direct summand of \(T^r\), for some \(r\), hence finite free over the DVR. The same direct-summand description proves both base-change identities

\[
\begin{aligned}
 F'\otimes_{S'}\operatorname{Hom}_{S'[G]}(P',T)
   &\simeq\operatorname{Hom}_{F'[G]}(F'\otimes P',F'\otimes T),\\
 k'\otimes_{S'}\operatorname{Hom}_{S'[G]}(P',T)
   &\simeq\operatorname{Hom}_{k'[G]}(P_0,k'\otimes T).
\end{aligned}
\]

These are the natural scalar-extension maps; for a free source they are the coordinate identifications, and for its direct summand they are their restrictions by the defining idempotent. The analogous identities hold for \(Q'\). The generic isomorphism of \(P'\) and \(Q'\) therefore makes these free Hom modules have equal ranks. Their residue Hom spaces have equal dimensions.

Projectivity makes \(\operatorname{Hom}_{k'[G]}(P_0,-)\) and \(\operatorname{Hom}_{k'[G]}(Q_0,-)\) exact. Their dimensions define integer-valued additive functions on \(G_0(k'[G])\). They agree on every cyclic test module, so Lemma 4.C makes them agree on every simple module. Lemma 4.A gives \(P_0\simeq Q_0\).

It remains to return to \(S\). The residue map \(S\to k'\) factors through the field embedding \(k\hookrightarrow k'\), even when \(S'/S\) is ramified. Consequently

\[
 P_0\simeq k'\otimes_k(P/\pi P),\qquad
 Q_0\simeq k'\otimes_k(Q/\pi Q).
\]

Lemma 4.1, applied to the finite-dimensional algebra \(k[G]\), descends the isomorphism to \(P/\pi P\simeq Q/\pi Q\). Compose \(P\to P/\pi P\) with this residue isomorphism and lift through the surjection \(Q\to Q/\pi Q\), using the projectivity of \(P\) as an \(S[G]\)-module. The resulting \(S[G]\)-linear map \(P\to Q\) is an isomorphism modulo \(\pi\). The underlying modules are finite free over \(S\), of equal rank by their generic isomorphism. The determinant of the lifted map is a unit, so it is an \(S\)-linear isomorphism. Its inverse is automatically \(G\)-equivariant. It is the required \(S[G]\)-isomorphism. \(\square\)

This argument includes residue characteristic zero, mixed characteristic, nonsplit group algebras and imperfect residue fields. Splitting and adjoining roots were intermediate finite extensions; the last two paragraphs prove descent to the original coefficient DVR. No assumption that \(|G|\) is invertible in \(S\) was used.

### Positive characteristic and integral normal bases

**Lemma 4.2.** For a complete DVR \(S\) of positive characteristic, a finitely generated projective \(S[G]\)-module whose fraction-field module is \(F[G]\) is \(S[G]\).

**Proof.** The coefficient-field existence theorem and complete regular-local specialization are proved in Coefficient rings and the Cohen structure theorem, Theorem 5.1 and Corollary 6.2. Choose the supplied coefficient-field embedding \(k=S/\pi S\hookrightarrow S\), which splits the residue map, and a uniformizer \(\pi\). The continuous ring homomorphism \(k[[T]]\to S\), \(T\mapsto\pi\), is the isomorphism in that corollary, so we may use \(S=k[[\pi]]\) with these choices [Stacks, Tag 0C0S]. Let \(P_0=P/\pi P\), a projective \(k[G]\)-module, and let \(Q=S\otimes_k P_0\). It is projective over \(S[G]\). The identity \(Q/\pi Q\simeq P_0\) lifts to \(Q\to P\), by projectivity of \(Q\) applied to \(P\to P_0\). Both modules are finite free over \(S\), of the same rank. The lifted map is invertible modulo \(\pi\), so its determinant is a unit, giving \(Q\simeq P\).

It follows that \(F\otimes_k P_0\simeq F[G]\). Lemma 4.1 applied to \(k[G]\) gives \(P_0\simeq k[G]\), hence \(P\simeq S[G]\). This works for finite and imperfect residue fields alike. \(\square\)

**Theorem 4.3 (local normal integral basis theorem).** The following are equivalent:

1. \(\mathfrak p\) is tame.
2. \(\widehat M\) is free of rank one over \(\widehat R[G]\).
3. \(M\) is free of rank one over \(R[G]\).

**Proof.** If tame, Corollary 3.2 and scalar extension make \(\widehat M\) projective. Its fraction algebra is the regular representation, by the field normal basis theorem. Swan's theorem, with \(Q=\widehat R[G]\), gives freeness if the fraction field has characteristic zero; Lemma 4.2 gives it otherwise.

To descend, choose a completed generator \(\hat a\). Lift its residue modulo \(\pi\) to \(a\in M\), since \(M/\pi M\simeq\widehat M/\pi\widehat M\). The map \(R[G]\to M\), \(g\mapsto g(a)\), is an isomorphism modulo \(\pi\). Its determinant between free \(R\)-modules of rank \(|G|\) is a unit, so it is an isomorphism. Localization freeness also plainly implies completion freeness.

Finally suppose \(M=R[G]a\). The invariants in the regular representation are \(R\sum_g g\), so \(M^G=R\operatorname{Tr}(a)\). But \(M^G=R\): an invariant lies in \(K\) and is integral over the integrally closed ring \(R\). Thus \(\operatorname{Tr}(a)\) is a unit and the trace is onto. Theorem 2.1 proves tameness. \(\square\)

The elementary construction behind this theorem is visible in two simpler cases. In an unramified local Galois extension, the residue extension is Galois, and [Theorem 4.0](https://kokunoyumeto.github.io/open-math-courses-public/courses/NOE-HYP/NOE-HYP-06.html#normal-bases-in-every-characteristic) supplies a normal basis over its residue field, whether finite or infinite. Lift a generator of that basis; Nakayama and a unit determinant give an integral normal basis. For a totally tamely ramified cyclic extension with \(\pi^e=c\pi_R\) and the \(e\)-th roots of unity in the base, take \(a=1+\pi+\cdots+\pi^{e-1}\). Its conjugates have coefficient matrix \((\zeta^{ij})\) in the power basis. Its Vandermonde determinant is a unit, since \(e\) is invertible and these roots remain distinct in the residue field. This explains the explicit sum construction under these additional hypotheses.

## 5. The group determinant and the global obstruction

For a local generator \(a\), use the ordered basis \((\tau^{-1}(a))_{\tau\in G}\) and all embeddings indexed by \(\sigma\in G\). Its embedding matrix is

\[
 E_{\sigma,\tau}=\sigma\tau^{-1}(a).
\]

**Proposition 5.1.** Its discriminant is \(\det(E)^2\).

**Proof.** The trace Gram matrix is \(E^{\mathsf T}E\), since its \((\tau,\upsilon)\)-entry is the sum of all conjugates of \(\tau^{-1}(a)\upsilon^{-1}(a)\). Take determinants. \(\square\)

This is the group determinant \(\Theta_G(X)=\det(X_{\sigma\tau^{-1}})\), specialized at \(X_g=g(a)\). Over a characteristic-zero splitting field it has the factorization

\[
 \Theta_G(X)=\prod_{\rho\in\operatorname{Irr}(G)}
 \det\left(\sum_gX_g\rho(g)\right)^{\dim\rho}.
\tag{5.1}
\]

Here is the full representation argument. If \(V\) is a module over a characteristic-zero field \(F\) and \(U\subset V\) a submodule, choose an \(F\)-linear projection \(q:V\to U\). The average \(|G|^{-1}\sum_g gqg^{-1}\) is a \(G\)-equivariant projection onto \(U\): it has image in \(U\) and restricts to its identity. Thus every finite representation is a direct sum of simple ones. Over a splitting field, Lemma 4.A identifies the group algebra with a product of matrix algebras, and proves that each simple \(V_\rho\) has scalar endomorphisms and no homomorphisms to a distinct simple. If its multiplicity in the regular left module is \(m_\rho\), then

\[
F^{m_\rho}\simeq\operatorname{Hom}_{F[G]}(F[G],V_\rho)
\simeq V_\rho,
\]

where the final map evaluates at the identity and its inverse sends \(v\) to \((x\mapsto xv)\). Therefore \(m_\rho=\dim\rho\). Left multiplication by \(\sum_g X_g g\), in the basis indexed by \(\tau\in G\), has \((\sigma,\tau)\)-entry \(X_{\sigma\tau^{-1}}\). Extend the fixed representation decomposition to the polynomial ring \(F[X_g:g\in G]\); its matrix becomes the direct sum of \(\dim\rho\) copies of \(\sum_gX_g\rho(g)\). Determinants prove (5.1). For abelian \(G\), commuting matrices on a simple module over a splitting field are scalar: each is an endomorphism of that module. Simplicity then forces dimension one, so all factors are linear. This proof uses characteristic zero; it does not assert the same decomposition in a modular residue field.

The arithmetic conductor-discriminant theorem says, for a finite abelian extension of number fields,

\[
 \mathfrak d_{L/K}=\prod_{\chi\in\widehat G}\mathfrak f(\chi),
\]

where \(\mathfrak f(\chi)\) is the finite Artin conductor ideal; the trivial character contributes the unit ideal. This formula is proved in Artin \(L\)-functions, conductors and discriminants, Theorem 21.5. Its proof first computes the conductor of the permutation representation and then decomposes the regular representation; for abelian \(G\), each irreducible has dimension one, giving exactly the displayed product. The finite conductor includes no infinite-place sign factor. Free source treatments are [Artin] and [Milne CFT, Chapter V, Theorem 3.27]. Identifying determinant factors with conductor ideals requires arithmetic information beyond the polynomial factorization.

Local generators at every prime need not glue to one global generator. For number fields the resulting obstruction is a locally free module class. Three landmarks delimit the question:

- **Hilbert–Speiser.** A finite abelian extension of \(\mathbb Q\) has a normal integral basis over \(\mathbb Z\) exactly when it is tame. Theorem 5.2 below proves both directions and constructs the generator; compare the freely accessible [Bergé, introduction].
- **Martinet.** There are tame Galois extensions of \(\mathbb Q\) with quaternion group of order eight whose integer rings are not free over \(\mathbb Z[G]\), although all localizations are free. Theorem 5.3 below constructs an explicit example and proves its obstruction [Martinet, Section IV].
- **Taylor (1981).** For a tame Galois extension \(L/K\) of number fields, the class \([\mathcal O_L]-[\mathcal O_K[G]]\) in \(\operatorname{Cl}(\mathbb Z[G])\) is the root number class \(W_{L/K}\), formed from the Artin root numbers of symplectic characters. This class has order dividing two [Taylor; Cassou-Noguès–Taylor, introduction, equation (1.1)]. The comparison here is after restricting scalars to \(\mathbb Z[G]\); it is not a claim about arbitrary relative \(\mathcal O_K[G]\)-class groups, nor is a stable class computation automatically a free generator.

### Tame abelian fields over the rationals

**Theorem 5.2 (Hilbert–Speiser).** A finite abelian extension \(L/\mathbb Q\) has a normal integral basis over \(\mathbb Z\) if and only if every finite prime is tame.

**Proof.** Necessity follows by localizing a normal integral basis and applying Theorem 4.3. We prove sufficiency by constructing a basis and then taking orbit sums. The earlier Kronecker–Weber lesson, Theorem 20.2, proves that \(L\subseteq F_N=\mathbb Q(\zeta_N)\) for some \(N\). The earlier Cyclotomic fields, Theorems 12.1–12.3, proves its Galois group, its full integer ring and the inertia groups used next. These are supplied programme proofs, rather than citations to the global normal-basis conclusion.

Write \(N=\prod_{p\mid N}p^{a_p}\). The Chinese remainder theorem identifies

\[
\operatorname{Gal}(F_N/\mathbb Q)
=\prod_{p\mid N}(\mathbb Z/p^{a_p}\mathbb Z)^\times.
\tag{5.2}
\]

Inertia at \(p\) is exactly the \(p^{a_p}\)-factor. Restriction of inertia onto the inertia group of a Galois subfield is surjective, by the full tower argument in Hilbert's ramification theory, Proposition 6.3, equations (6)–(7). Its order in \(L\) is the ramification index, by Theorem 6.2 there, and is prime to \(p\) by tameness. For odd \(p\), the kernel of

\[
(\mathbb Z/p^{a_p}\mathbb Z)^\times
\longrightarrow(\mathbb Z/p\mathbb Z)^\times
\]

has order \(p^{a_p-1}\). Every homomorphism from this kernel to a group of order prime to \(p\) is trivial: its image has order dividing both orders. Thus the kernel acts trivially on \(L\). For \(p=2\), the entire factor has power-of-two order and acts trivially for the same reason. It follows that

\[
L\subseteq F_m=\mathbb Q(\zeta_m),\qquad
m=\prod_{p\mid N,\ p\ne2}p,
\tag{5.3}
\]

where \(m\) is odd and square-free. To identify this fixed field explicitly, restrict (5.2) to the roots of orders \(p\) for odd \(p\mid N\). This is the surjection onto \(\prod_{p\mid m}(\mathbb Z/p\mathbb Z)^\times\), with exactly the kernels and the 2-factor just killed. The cyclotomic degree formula gives \([F_m:\mathbb Q]=\prod_{p\mid m}(p-1)\), so its fixed subgroup is precisely that kernel. This proves (5.3), including the case \(m=1\).

For each odd prime \(p\mid m\), the \(p-1\) conjugates of \(\zeta_p\) form a \(\mathbb Z\)-basis of \(\mathbb Z[\zeta_p]=\mathcal O_{F_p}\): they include the nonconstant members of the usual power basis, and the identity \(1=-\sum_{a=1}^{p-1}\zeta_p^a\) recovers its constant member. Their number is the degree, so spanning implies independence. Products of these bases span \(\mathbb Z[\zeta_p:p\mid m]\). This is \(\mathbb Z[\zeta_m]=\mathcal O_{F_m}\), by Theorem 12.2: the exponents \(m/p\) have gcd one, so integer powers of the roots of orders \(p\) generate a root of order \(m\). The number of products is \(\prod_{p\mid m}(p-1)=[F_m:\mathbb Q]\), making the products an integral basis. The product Galois group acts freely and transitively on them. In particular

\[
\alpha=\prod_{p\mid m}\zeta_p
\]

is a normal integral basis generator for \(F_m\). If \(m=1\), use \(\alpha=1\).

Put \(\Gamma=\operatorname{Gal}(F_m/\mathbb Q)\) and \(H=\operatorname{Gal}(F_m/L)\). Integrality and the fixed-field identity give \(\mathcal O_L=\mathcal O_{F_m}^H\). Write an integer of \(F_m\) uniquely in the basis \(\{\gamma(\alpha):\gamma\in\Gamma\}\). It is \(H\)-invariant exactly when its integral coefficients are constant on each \(H\)-orbit. The orbit sums are therefore a \(\mathbb Z\)-basis of \(\mathcal O_L\). Since \(\Gamma\) is abelian, these sums are precisely the distinct \(\Gamma/H\)-conjugates of

\[
\beta=\sum_{h\in H}h(\alpha)
=\operatorname{Tr}_{F_m/L}(\alpha).
\tag{5.4}
\]

Thus \(\beta\) is a normal integral basis generator. The construction sums basis vectors with integral coefficients and requires no division by \(|H|\). \(\square\)

### A tame quaternion field without an integral normal basis

**Theorem 5.3 (an explicit Martinet example).** Put

\[
\begin{aligned}
&a=\sqrt5,\quad b=\sqrt{21},\quad K=\mathbb Q(a,b),\\
&A=\frac{5+a}{2},\quad B=\frac{21+b}{2},\\
&N=K(w),\qquad w^2=-3AB.
\end{aligned}
\tag{5.5}
\]

Then \(N/\mathbb Q\) is tame and Galois with quaternion group of order eight. Its integer ring has a normal integral basis at every rational prime, but has none over \(\mathbb Z\).

**Proof: the field and its group.** The two quadratic fields are distinct, so \([K:\mathbb Q]=4\). Every real embedding of \(K\) makes \(A,B\) positive, since \(5>\sqrt5\) and \(21>\sqrt{21}\). Thus \(-3AB\) is totally negative and cannot be a square in \(K\); \([N:K]=2\), and \(N\) is totally imaginary. Define automorphisms on its generators by

\[
\begin{aligned}
\sigma(a)&=-a,&\sigma(b)&=b,&\sigma(w)&=\frac aA w,\\
\tau(a)&=a,&\tau(b)&=-b,&\tau(w)&=\frac{ab}{B}w.
\end{aligned}
\tag{5.6}
\]

These preserve the defining equation: if \(A'=(5-a)/2\) and \(B'=(21-b)/2\), then \(AA'=5=a^2\) and \(BB'=105=(ab)^2\). Applying either map twice fixes \(K\) and sends \(w\) to \(-w\). Denote this involution by \(z\). Direct substitution also gives \(\sigma\tau(w)=-\tau\sigma(w)\), while their restrictions to \(K\) commute. Consequently

\[
\sigma^2=\tau^2=z,\qquad z^2=1,\qquad
\sigma\tau=z\tau\sigma.
\]

The restrictions give all four automorphisms of \(K\), and each has two lifts differing by \(z\). Thus there are eight distinct automorphisms of the degree-eight field, proving Galoisness and the quaternion group presentation. Complex conjugation is \(z\), since it fixes the real field \(K\) and negates \(w\).

**Its integers and ramification.** Set \(c=(1+a)/2\) and \(d=(1+b)/2\). The quadratic integer-basis proof in Algebraic integers and rings of integers, Theorem 1.4, gives discriminants \(5\) and \(21\). The full coprime-discriminant lemma in Cyclotomic fields, equation (8), therefore gives

\[
\mathcal O_K=\mathbb Z[c,d],\qquad d_K=5^2 21^2=105^2.
\tag{5.7}
\]

In particular 2 is unramified in \(K\). The preceding lesson's discriminant criterion, Trace discriminants for orders, Theorem 3.1 and its maximal-order deduction, proves this assertion.

We check unramifiedness above 2 in \(N/K\) directly. Put \(c'=1-c\), \(d'=1-d\) and \(q=c'd'\). Calculation gives

\[
A+(c')^2=4,\qquad B+(d')^2=16,
\qquad -3AB\equiv q^2\pmod{4\mathcal O_K}.
\tag{5.8}
\]

The norms of \(c'\) and \(d'\) in their quadratic fields are \(-1\) and \(-5\), so \(q\) is a unit at every prime over 2. Also \(-3AB\) is a unit there. At such a prime, in its base DVR \(R\), the integral element \(\theta=(1+w/q)/2\) satisfies

\[
\theta^2-\theta+\frac{1+3AB/q^2}{4}=0.
\tag{5.9}
\]

Its polynomial discriminant \(-3AB/q^2\) is a unit of \(R\). Here is why a unit discriminant suffices for the full integer ring. The trace matrix makes the order \(R[\theta]\) equal to its trace dual. Any element integral over \(R\), multiplied by any member of this order, still has integral field trace, by lesson one's integral-trace proof. It therefore belongs to that trace dual, hence to \(R[\theta]\). Thus the order is already the integral closure. The unit-discriminant criterion of lesson three makes its residue algebra a product of separable fields, so all its ramification indices are one. This proves that 2 is unramified in \(N\). At every odd prime the ramification index divides eight, by the inertia-order theorem, and is therefore prime to the residue characteristic. Finite residue fields are separable, so \(N/\mathbb Q\) is tame.

Only 3, 5 and 7 can ramify. Indeed \(N_{K/\mathbb Q}(-3AB)=3^4 5^2 105^2\), so at a prime of \(K\) outside these three primes and 2 the element \(-3AB\) is a unit. The order defined by \(X^2+3AB\) has unit discriminant \(-12AB\) there. The same trace-dual argument proves unramifiedness. Equation (5.7) excludes any further ramification in \(K\).

We will also need the exact indices at those three primes. In a tame Galois field \(F/\mathbb Q\) of degree \(n\), the discriminant exponent at \(p\) is

\[
v_p(|d_F|)=\sum_{\mathfrak P\mid p}f_{\mathfrak P}(e_{\mathfrak P}-1)
=n\left(1-\frac1e\right).
\tag{5.10}
\]

This follows from the complete different-exponent proof in Three differents, Theorem 5.3, the norm-of-different proof in The different and the discriminant, Theorem 14.3, and \(n=efg\) in the earlier Galois decomposition theorem. For \(K\), the exponents in (5.7) are two at 3, 5 and 7, and its degree is four. Thus its ramification index is two at each of them.

Normalize valuations at primes of \(K\) to have value group \(\mathbb Z\). At 3 and 7, the field \(\mathbb Q(b)\) already has index two, so \(K/\mathbb Q(b)\) has index one. In \(\mathbb Q(b)\), \(v(b)=1\) and \(v(21)=2\), making \(v(B)=1\). The element \(A\) is a unit at these primes, since its rational norm has only the prime factor 5. Consequently \(v(-3AB)\) is three above 3 and one above 7. At 5, the field \(\mathbb Q(a)\) has index two and \(K/\mathbb Q(a)\) has index one; \(v(A)=1\), since \(v(a)=1<v(5)=2\). The other quadratic field \(\mathbb Q(b)\) is unramified at 5, so the valuation in \(K\) of its integral element \(B\) is even. Therefore \(v(-3AB)=1+v(B)\) is odd at every prime over 5. In all three cases a square root of an element of odd valuation forces ramification index two in the quadratic extension: extending the valuation literally gives \(v(w)=v(-3AB)/2\), with denominator two, and the extension degree is two. Hence \(N/\mathbb Q\) has index four at 3, 5 and 7. Formula (5.10) yields

\[
d_N=105^6.
\tag{5.11}
\]

The sign is positive because its eight embeddings form four complex pairs. Indeed, replacing each pair of conjugate embedding rows by real and imaginary parts gives a real invertible matrix; reversing that replacement multiplies its determinant by \(-2i\) per pair. In the squared embedding determinant, four pairs therefore contribute a positive factor.

**The contradiction to a global basis.** Suppose \(\mathcal O_N=\mathbb Z[G]x\). The vectors

\[
\phi=(1+z)x,\qquad \psi=(1-z)x
\]

and their four conjugates indexed by \(1,\sigma,\tau,\tau\sigma\) are bases of \(\mathcal O_K=\mathcal O_N^z\) and \(\mathcal O_N^-:=\{u:z(u)=-u\}\), respectively: in a regular integral basis, invariant coefficients are equal on each pair \(g,zg\), and anti-invariant coefficients are opposite. The sum of these two lattices has index \(2^4\) in \(\mathcal O_N\), because each pair changes basis by a matrix of determinant \(-2\).

The element \(\gamma=cd\) also generates a normal integral basis of \(K\). Each quadratic basis \(c,1-c\) and \(d,1-d\) has determinant \(\pm1\) in its power basis; their products give the full basis in (5.7). Thus \(\phi=u\gamma\) for a unit \(u\in\mathbb Z[G/\langle z\rangle]\). Every unit in this group ring, whose group is \(C_2\times C_2\), is a signed group element. To prove this, write \(u=\sum_h n_hh\). Each of the four character values is an integer unit, hence \(\pm1\). Character orthogonality here is the direct identity \(\sum_\chi\chi(h)\chi(k)=4\) for \(h=k\) and zero otherwise. It gives

\[
\sum_h n_h^2=\frac14\sum_\chi\left(\sum_h n_h\chi(h)\right)^2=1.
\]

Exactly one integral coefficient is therefore \(\pm1\). Consequently \(\phi\) is a signed conjugate of \(\gamma\), and

\[
\operatorname{Tr}_{K/\mathbb Q}(\phi^2)
=\operatorname{Tr}_{K/\mathbb Q}(\gamma^2)
=\frac{1+5+21+105}{4}=33.
\tag{5.12}
\]

On the negative eigenspace put \(T(u,v)=\operatorname{Tr}_{K/\mathbb Q}(uv)\); its products lie in \(K\), so this is defined and invariant under \(G\). For an element \(h\) of order four, \(h^2=z\) acts as \(-1\), and

\[
T(\psi,h\psi)=T(h\psi,h^2\psi)=-T(\psi,h\psi)=0.
\]

All off-diagonal pairings in the four-conjugate basis of \(\mathcal O_N^-\) vanish by applying this identity after a common conjugation. All diagonal entries equal \(t=\operatorname{Tr}_{K/\mathbb Q}(\psi^2)\). Thus its Gram determinant is \(t^4\). On \(\mathcal O_K\), the Gram determinant for the same trace convention is \(d_K\). The two eigenspaces are orthogonal for the trace of \(N\), which is twice this trace on both spaces. The index-square formula of lesson three now gives

\[
2^8 d_N=2^8 d_K t^4,\qquad
|t|=105
\]

by (5.7) and (5.11). Since \(\psi=w v\) for nonzero \(v\in K\), its square is totally negative, making \(t=-105\).

Finally \(\phi^2-\psi^2=4x z(x)\in4\mathcal O_K\). Taking traces forces \(33\equiv-105\pmod4\), which is false: their residues are one and three. This proves that no global normal integral basis exists. All local normal integral bases exist by tameness and Theorem 4.3. \(\square\)

The field (5.5) is the second example in [Martinet, Section IV, pp. 406–407]. The proof above constructs its group and ramification and derives the obstruction directly from a hypothetical basis, without assuming a classification of quaternion group-ring modules.

### An integral logarithm for the determinant comparison

Taylor's comparison requires information about determinants of integral group-ring units. The following construction supplies the integral logarithm itself, including the cancellation of its denominators. It is useful even when the residue characteristic divides the group order [Chinburg–Pappas–Taylor, Section 3.a].

Let \(p\) be a rational prime. Let \(R\) be an integral domain finite and free over \(\mathbb Z_p\), equipped with a continuous ring endomorphism \(F\) satisfying

\[
 F(r)\equiv r^p\pmod {pR}\quad(r\in R).
\]

Thus \(F\) fixes \(\mathbb Z_p\). The coefficient field \(T=R[1/p]\) is a field: a finite-dimensional domain over a field is a field, since multiplication by a nonzero element is injective and hence onto. No assertion about the existence of \(F\) for an arbitrary ramified coefficient ring is intended. For \(R=\mathbb Z_p\), take \(F=1\).

Let \(H\) be a finite \(p\)-group, let \(I=\ker(R[H]\xrightarrow{\epsilon}R)\) be its augmentation ideal, and let \(\mathcal C\) be the set of conjugacy classes of \(H\). Write \(R[\mathcal C]\) for the free module on those classes, and put

\[
 \phi\Bigl(\sum_h r_hh\Bigr)=\sum_h r_h[h],\qquad
 \Psi\Bigl(\sum_C r_C[C]\Bigr)=\sum_C F(r_C)[h_C^p].
\tag{5.12}
\]

The second formula is independent of the representative \(h_C\). The sum of coefficients defines an augmentation on \(R[\mathcal C]\); its kernel is \(\phi(I)\). Extend \(F,\Psi\) to the coefficient field.

**Lemma 5.4 (cyclic-word congruence).** For \(x\in R[H]\) and every integer \(m\geq1\),

\[
 \phi(x^{p^m})-\Psi\phi(x^{p^{m-1}})
       \in p^mR[\mathcal C].
\tag{5.13}
\]

**Proof.** Expand \(x=\sum_h a_hh\). A term of \(x^{p^m}\) is indexed by a word of length \(p^m\) in the alphabet \(H\). Rotating a word preserves its scalar coefficient and changes its group product by conjugacy. An orbit of words under rotation has size \(p^j\), for some \(0\leq j\leq m\). Choose its shortest repeated block, of length \(p^j\); denote the block's scalar coefficient by \(b\) and its group product by \(u\). The orbit contributes

\[
 p^j b^{p^{m-j}}[u^{p^{m-j}}].
\]

For \(j<m\), precisely the same block indexes an orbit in the expansion of \(x^{p^{m-1}}\), and its contribution after applying \(\Psi\) is

\[
 p^j F(b)^{p^{m-1-j}}[u^{p^{m-j}}].
\]

Here rotations of the repeated block give the same conjugacy class in both formulas. Since \(b^p-F(b)\in pR\), their coefficient difference lies in \(p^mR\). Indeed, if \(a-b\in p^rR\), with \(r\geq1\), the binomial theorem gives \(a^p-b^p\in p^{r+1}R\); iteration gives the required divisibility by \(p^{m-j}\) before multiplication by \(p^j\). Orbits of size \(p^m\) occur only in the first expansion and already have a coefficient divisible by \(p^m\). Summing over the orbits proves (5.13), including \(p=2\). \(\square\)

**Theorem 5.5 (integral determinant logarithm).** The series

\[
 \mathcal L(1-x)=(p-\Psi)\phi\bigl(\log(1-x)\bigr),\qquad
 \log(1-x)=-\sum_{n\geq1}\frac{x^n}{n},\qquad x\in I,
\tag{5.14}
\]

converges and defines a group homomorphism

\[
 \mathcal L:1+I\longrightarrow p\phi(I).
\tag{5.15}
\]

It factors through \(\operatorname{Det}(1+I)\). If \(\nu\) denotes that factor, then

\[
 \ker\nu=\operatorname{Det}(1+I)_{\mathrm{tors}}.
\tag{5.16}
\]

Here \(\operatorname{Det}(v)(\chi)=\det\rho_\chi(v)\), for an irreducible representation over a finite splitting field of \(T[H]\). The right side of (5.16) consists of the determinant functions of finite order. It does not assert that every such function is the determinant of a group element.

**Proof.** We first establish convergence. The augmentation ideal of \(\mathbb F_p[H]\) is nilpotent. One can see this without a representation theorem. A nontrivial finite \(p\)-group has a central element \(c\) of order \(p\): the class equation makes its center's order divisible by \(p\), and repeatedly taking powers of any nonidentity central element produces one of order \(p\). Induct on \(|H|\). If the augmentation ideal of \(\mathbb F_p[H/\langle c\rangle]\) has \(N\)th power zero, the \(N\)th power upstairs is contained in \((c-1)\mathbb F_p[H]\). This ideal has \(p\)th power zero, because \(c\) is central and \((c-1)^p=c^p-1=0\). The trivial group starts the induction. Tensor this universal calculation with \(R/pR\). It gives \(I^N\subset pR[H]\) for some \(N\), and hence

\[
 x^n\in p^{\lfloor n/N\rfloor}R[H].
\]

The denominators \(n\) have valuation at most \(\log_p n\), so the logarithm converges. The geometric inverse shows that every \(1+x\), with \(x\in I\), is a unit; these units form a group.

To prove integrality, regroup the convergent series as

\[
 \mathcal L(1-x)=
 -p\sum_{p\nmid n}\frac{\phi(x^n)}n
 +\sum_{n\geq1}\frac{\Psi\phi(x^n)-\phi(x^{pn})}{n}.
\tag{5.17}
\]

Write \(n=p^mr\), with \(p\nmid r\). Lemma 5.4, applied to \(x^r\) and the exponent \(m+1\), makes the numerator of the corresponding term in the second sum divisible by \(p^{m+1}\). Both sums therefore belong to \(pR[\mathcal C]\). Their augmentations are zero, since \(\epsilon(x)=0\) and \(F(0)=0\). The augmentation kernel is spanned by the differences \([C]-[1]\), so it is saturated over \(R\); consequently the value belongs to \(p\phi(I)\).

We next prove the homomorphism and determinant assertions. Choose a finite splitting field \(E/T\). Each representation has an integral lattice: start with an \(\mathcal O_E\)-lattice and sum its translates by \(H\). The sum is finite, spans the representation, and is a free lattice by the DVR argument of lesson one. On this lattice \(\rho(x)^N\) has entries in \(p\mathcal O_E\), so all eigenvalues of \(\rho(x)\) have positive valuation. Matrix logarithms and scalar logarithms of the resulting principal units converge. The formal identity

\[
 \operatorname{tr}\log(1+tA)=\log\det(1+tA)
\]

follows by differentiating: both derivatives are \(\operatorname{tr}(A(1+tA)^{-1})\), and both constant terms are zero. Convergence permits evaluation at \(t=1\). Thus

\[
 \chi\bigl(\phi\log v\bigr)=\log\operatorname{Det}(v)(\chi)
              \qquad(v\in1+I).
\tag{5.18}
\]

These evaluations determine an element of \(E[\mathcal C]\). To justify this point, the kernel of \(\phi:E[H]\to E[\mathcal C]\) is the span of additive commutators: \(ab-ba\) has conjugate group products, and \(tht^{-1}-h=[t,ht^{-1}]\) supplies every conjugacy difference. The characteristic-zero decomposition proved at the start of Section 5 identifies \(E[H]\) with a product of full matrix algebras. In a matrix algebra the additive commutators are exactly the traceless matrices, as follows from the off-diagonal matrix units and the differences of diagonal matrix units. The irreducible traces therefore detect its entire quotient by additive commutators.

The scalar logarithm is additive on products of principal units. This follows from the formal two-variable identity \(\log((1+s)(1+t))=\log(1+s)+\log(1+t)\), followed by convergent evaluation. Determinants multiply, so (5.18) and the preceding detection argument show that \(\phi\log(vw)=\phi\log v+\phi\log w\). Applying the additive map \(p-\Psi\) proves (5.15). Equation (5.18) also shows that equal determinant functions have equal values of \(\phi\log\); hence \(\mathcal L\) factors through determinants.

Finally, choose \(a\) with \(h^{p^a}=1\) for every \(h\in H\). On the augmentation kernel in \(T[\mathcal C]\), \(\Psi^a=0\): its value is \(F^a\) of the sum of coefficients, times \([1]\). The additive operator \(p-\Psi\) is consequently invertible there, with inverse

\[
 (p-\Psi)^{-1}=\sum_{j=0}^{a-1}p^{-j-1}\Psi^j.
\tag{5.19}
\]

Thus \(\nu(\operatorname{Det}v)=0\) is equivalent to every scalar logarithm in (5.18) being zero.

For a principal unit \(\lambda\) of a finite extension of \(\mathbb Q_p\), its logarithm vanishes precisely when \(\lambda\) has finite \(p\)-power order. Here is the valuation argument. Normalize \(v(p)=1\). If \(v(\lambda-1)>0\), the binomial theorem gives

\[
 v(\lambda^p-1)\geq
       \min\{1+v(\lambda-1),\ p\,v(\lambda-1)\}.
\]

Iteration sends \(\lambda^{p^b}\) arbitrarily close to one: the displayed lower-bound iteration first increases by a factor \(p\) until it reaches \(1/(p-1)\), and thereafter increases by at least one at each step. When \(v(z)>1/(p-1)\), the first term of \(\log(1+z)\) has strictly smaller valuation than every later term: \(v_p(n)\leq(n-1)/(p-1)\). For that inequality, if \(v_p(n)=j\), then \(n\geq p^j\) and \(j\leq(p^j-1)/(p-1)\). Hence this logarithm is zero only if \(z=0\). A zero logarithm of \(\lambda\) therefore makes some \(\lambda^{p^b}=1\). Conversely finite order makes its logarithm zero, because the logarithm takes values in a characteristic-zero additive group. There are finitely many irreducible characters, so their finite orders have a common multiple. This proves (5.16). \(\square\)

The next two lemmas apply to an arbitrary finite group \(H\); neither requires a Frobenius lift. Keep \(R\) finite and free over \(\mathbb Z_p\), with the notation for conjugacy classes and determinants above.

**Lemma 5.6 (matrix determinants come from units).**

\[
 \operatorname{Det}(\operatorname{GL}(R[H]))
       =\operatorname{Det}(R[H]^\times).
\tag{5.20}
\]

Here \(\operatorname{GL}\) means the union under stabilization \(U\mapsto\operatorname{diag}(U,1)\), and a character evaluates a matrix over the group algebra by applying its representation to every entry.

**Proof.** Put \(A=R[H]\). The finite-algebra argument in Lemma 4.A, before extending the field, makes the regular module of the radical quotient of \(A/pA\) semisimple. Decompose it into its simple summands. Each simple endomorphism ring is a division ring, by the kernel-and-image argument, so the endomorphism ring of this decomposition is a product of matrix algebras over division rings. It is also the opposite of the radical quotient, by right multiplication. Taking opposites therefore describes that quotient itself as a product of matrix algebras over division rings; no assertion that those division rings are fields is needed.

Let \(K\) be the inverse image of the radical of \(A/pA\). That radical is nilpotent by Lemma 4.A, so \(K^N\subset pA\) for some \(N\). Geometric series invert \(1-k\) for every \(k\in K\). Consequently a unit modulo \(K\) lifts to a unit of \(A\): lift an inverse, and remove the two inverse errors in \(K\) by these series. The resulting left and right inverses coincide.

We give the row reduction over this quotient explicitly. Suppose \(a_1A+\cdots+a_nA=A\). In one factor \(M_d(D)\) of \(A/K\), let \(A_i\) denote the corresponding endomorphisms of \(D^d\). The sum of their images is \(D^d\). Choose a complement \(V\) to \(\ker A_1\). Choose maps \(C_i\), for \(i\geq2\), vanishing on \(V\), such that \(\sum_{i\geq2} A_iC_i\) maps \(\ker A_1\) isomorphically onto a complement of \(\operatorname{im}A_1\), modulo \(\operatorname{im}A_1\). Such maps exist because the other images span that quotient and its dimension is \(\dim\ker A_1\). Then \(A_1+\sum_{i\geq2}A_iC_i\) is invertible: projecting a kernel vector to the quotient first kills its \(\ker A_1\)-component, and injectivity on \(V\) kills the rest. Perform this construction in every factor, and lift the resulting \(C_i\) to \(c_i\in A\). The element \(a_1+\sum_{i\geq2}a_ic_i\) is a unit, since it is a unit modulo \(K\).

The first row of an invertible matrix is such a row. Elementary column additions make its first entry a unit. Elementary row and column operations clear its first column and row. Induction gives a diagonal matrix whose entries are units of \(A\). Every elementary operation has determinant one in every character representation. The determinant function of the resulting diagonal matrix is the product of the determinant functions of its diagonal units, hence the determinant function of their product in \(A^\times\). Stabilization adds only determinant one. The reverse inclusion is immediate. \(\square\)

**Lemma 5.7 (the logarithm near one).** There is an isomorphism of abelian groups

\[
 \operatorname{Det}(1+p^2R[H])\xrightarrow{\ \ell\ }
       p^2R[\mathcal C],\qquad
 \ell(\operatorname{Det}v)=\phi\log v.
\tag{5.21}
\]

**Proof.** If \(z\in p^2R[H]\), both \(\log(1+z)\) and \(\exp(z)=\sum_{n\geq0}z^n/n!\) converge in \(R[H]\). For the exponential, \(v_p(n!)=\sum_{j\geq1}\lfloor n/p^j\rfloor\leq(n-1)/(p-1)\); consequently all nonconstant terms stay in \(p^2R[H]\) and their valuations tend to infinity. The same bounds hold for the logarithm. The formal one-variable identities \(\log\exp z=z\) and \(\exp\log(1+z)=1+z\) can therefore be evaluated in the complete algebra. Only powers of the one element occur, so no commutativity assumption on the entire algebra is involved.

The determinant-trace identity and detection argument in the proof of Theorem 5.5 show that \(\ell\) is well defined and additive on products. If \(\ell(\operatorname{Det}v)=0\), all its scalar determinant logarithms vanish. They are logarithms of elements of \(1+p^2\mathcal O_E\); the strict first-term estimate in that proof makes every such determinant equal to one. Thus \(\ell\) is injective. Given \(y\in p^2R[\mathcal C]\), choose \(z\in p^2R[H]\) with \(\phi(z)=y\) and set \(v=\exp z\). Then \(\ell(\operatorname{Det}v)=y\), proving surjectivity. This proof also covers \(p=2\). \(\square\)

### Locally free classes and the gluing of lattices

We now construct the class group in the global statement. This also makes precise why free modules at all primes need not have one global basis. The determinant description of this class group needs an additional argument; it is not part of the lattice gluing assertion proved here. Compare [Cougnard, Section 2] for the character description.

Put \(\Lambda=\mathbb Z[G]\), \(\Lambda_p=\mathbb Z_p[G]\) and \(A=\mathbb Q[G]\). A **\(\Lambda\)-lattice** is a left \(\Lambda\)-module that is finite and torsion-free over \(\mathbb Z\). Such a module is free as an abelian group. Indeed, after clearing denominators, any finite torsion-free abelian group embeds in \(\mathbb Z^d\). Projection to the first coordinate has image a principal subgroup of \(\mathbb Z\); a lift of its generator splits this projection. Induction on \(d\) makes the kernel, and then the entire group, free. We call a lattice **locally free of rank \(r\)** when

\[
 M_p:=\mathbb Z_p\otimes_{\mathbb Z}M\simeq\Lambda_p^r
                      \quad\text{for every rational prime }p.
\tag{5.22}
\]

The same \(r\) occurs at every prime, since the abelian rank is \(r|G|\). Lemma 4.1, applied to \(A\) and the field extension \(\mathbb Q_p/\mathbb Q\), gives \(\mathbb Q\otimes M\simeq A^r\). Thus a rational frame exists even when an integral one does not.

**Lemma 5.8 (projectivity from local frames).** Every locally free \(\Lambda\)-lattice is a finitely generated projective \(\Lambda\)-module.

**Proof.** The module is finitely generated because its finite abelian generators also generate it over \(\Lambda\). It is finitely presented: the kernel of a surjection \(\Lambda^s\to M\) is a subgroup of the finite free abelian group \(\Lambda^s\), hence is finitely generated over \(\mathbb Z\) and over \(\Lambda\).

Consider the finite abelian groups

\[
 D=\operatorname{Hom}_\Lambda(M,\Lambda),\qquad
 E=\operatorname{End}_\Lambda(M),
\]

and the homomorphism

\[
 M\otimes_{\mathbb Z}D\longrightarrow E,\qquad
 m\otimes f\longmapsto(x\mapsto f(x)m).
\tag{5.23}
\]

Here “finite” means finitely generated. The Hom and endomorphism groups are subgroups of matrix groups of finite abelian rank. The exact-completion theorem linked at the start of this lesson shows that tensoring with \(\mathbb Z_p\) is flat. Hom commutes with this tensor operation in our situation: express a \(\Lambda\)-map in abelian bases and impose the finitely many linear equations for commuting with the elements of \(G\). Flatness preserves the kernel of those equations. After completion, (5.23) is therefore the corresponding map for the free module \(\Lambda_p^r\), where the coordinate vectors and coordinate functionals express every endomorphism as a sum of these maps. Its cokernel \(C\) has \(C\otimes\mathbb Z_p=0\) for every prime.

This forces \(C=0\). Otherwise choose a nonzero cyclic subgroup, isomorphic to \(\mathbb Z\) or to \(\mathbb Z/n\) with \(n>1\). Flatness preserves its injection into \(C\); its completion is nonzero at any prime in the first case, and at a prime dividing \(n\) in the second. Thus the identity of \(M\) is a finite sum \(x\mapsto\sum_i f_i(x)m_i\). The maps

\[
 M\longrightarrow\Lambda^s,\quad x\longmapsto(f_i(x))_i,
 \qquad
 \Lambda^s\longrightarrow M,\quad(a_i)_i\longmapsto\sum_i a_im_i
\]

are left \(\Lambda\)-linear and have composite the identity. They make \(M\) a direct summand of a finite free module. \(\square\)

Let \(\mathcal P(\Lambda)\) be the commutative monoid of isomorphism classes of locally free lattices, with addition given by direct sum. Its group completion is denoted \(K_0^{\mathrm{lf}}(\Lambda)\). Explicitly, use pairs of classes, with

\[
 (M,N)\sim(M',N')
 \quad\Longleftrightarrow\quad
 M\oplus N'\oplus X\simeq M'\oplus N\oplus X
 \text{ for some locally free }X.
\]

Addition of pairs is direct sum in each entry; interchanging the entries gives the inverse. These formulas verify the group-completion relation and operations directly. The rank homomorphism is split by \(1\mapsto[\Lambda]\). Define

\[
 \operatorname{Cl}(\Lambda)=\ker\bigl(
 K_0^{\mathrm{lf}}(\Lambda)\xrightarrow{\operatorname{rank}}\mathbb Z\bigr),
 \qquad c(M)=[M]-r[\Lambda].
\tag{5.24}
\]

**Proposition 5.9 (what equality of classes means).** For locally free lattices \(M,N\) of the same rank,

\[
 c(M)=c(N)
 \quad\Longleftrightarrow\quad
 M\oplus\Lambda^s\simeq N\oplus\Lambda^s
                \text{ for some }s\geq0.
\tag{5.25}
\]

Every element of \(\operatorname{Cl}(\Lambda)\) has the form \(c(M)\). In particular \(c(M)=0\) means stable freeness.

**Proof.** Equality in the group completion says \(M\oplus X\simeq N\oplus X\) for some locally free \(X\). Lemma 5.8 gives a projective complement \(Y\) with \(X\oplus Y\simeq\Lambda^s\). Adding it proves (5.25). Conversely a free stabilizing summand is permitted in the group-completion relation.

We also need the complement to be locally free when representing an arbitrary class. If \(X\) has rank \(q\), characteristic-zero semisimplicity, proved in Section 5, gives \(\mathbb Q\otimes Y\simeq A^{s-q}\): cancel the simple multiplicities of \(A^q\) from those of \(A^s\). At each prime \(Y_p\) is projective over \(\Lambda_p\). Its fraction module is \(\mathbb Q_p[G]^{s-q}\), so Swan's rigidity theorem proved in Section 4 gives \(Y_p\simeq\Lambda_p^{s-q}\). Thus \(Y\) is locally free. Now a rank-zero class \([P]-[Q]\), with \(P,Q\) of rank \(r\), can be written

\[
 [P]-[Q]=[P\oplus Y]-s[\Lambda]=c(P\oplus Y),
       \qquad Q\oplus Y\simeq\Lambda^s.
\]

The ranks in the final expression are \(s\), as required. \(\square\)

**Theorem 5.10 (an explicit lattice gluing description).** Fix \(r\geq1\). Choose matrices

\[
 a_p\in\operatorname{GL}_r(\mathbb Q_p[G]),\qquad
 a_p\in\operatorname{GL}_r(\Lambda_p)
               \text{ for all but finitely many }p.
\tag{5.26}
\]

Use row vectors, so that right multiplication by a matrix is a map of left modules. Then

\[
 M(a)=\{v\in A^r:\ v\in\Lambda_p^r a_p
                          \text{ for every prime }p\}
\tag{5.27}
\]

is a locally free lattice, and \(M(a)_p=\Lambda_p^r a_p\). Every locally free lattice of rank \(r\), together with a rational frame, arises this way. Two tuples give isomorphic lattices precisely when

\[
 a'_p=u_p a_p b\quad\text{for every }p,
 \qquad u_p\in\operatorname{GL}_r(\Lambda_p),\quad
 b\in\operatorname{GL}_r(A).
\tag{5.28}
\]

Thus isomorphism classes have the double-coset description

\[
 \Bigl(\prod_p\operatorname{GL}_r(\Lambda_p)\Bigr)
 \backslash
 \Bigl(\prod_p{}'\operatorname{GL}_r(\mathbb Q_p[G])\Bigr)
 /\operatorname{GL}_r(A).
\tag{5.29}
\]

The prime on the product means the integrality condition (5.26). Stabilization adds an identity block to every matrix.

**Proof.** Let \(S\) be the finite exceptional set. Since each \(\Lambda_p^r a_p\) is a full \(\mathbb Z_p\)-lattice, choose \(e_p\geq1\) with

\[
 p^{e_p}\Lambda_p^r\subseteq\Lambda_p^r a_p
                         \subseteq p^{-e_p}\Lambda_p^r
                              \quad(p\in S).
\]

Put \(N=\prod_{p\in S}p^{e_p}\); if \(S\) is empty, put \(N=1\). The rational vectors integral at every prime are precisely the integral vectors: apply the prime factorization of an integer denominator to each rational coefficient. Consequently

\[
 N\Lambda^r\subseteq M(a)\subseteq N^{-1}\Lambda^r.
\tag{5.30}
\]

The second inclusion uses that \(Nv\) is integral at every prime. These bounds make \(M(a)\) finite over \(\mathbb Z\), torsion-free and of full abelian rank. They also give its claimed completions exactly, rather than just an inclusion. To check this, multiply the finite quotient

\[
 V=N^{-1}\Lambda^r/N\Lambda^r
\]

by \(N\), identifying it with \(\Lambda^r/N^2\Lambda^r\). The ordinary integer Chinese remainder theorem decomposes it as the product of its components at \(p\mid N\). These components are

\[
 V_p=N^{-1}\Lambda_p^r/N\Lambda_p^r.
\]

Within \(V_p\), the desired local lattice specifies the subgroup
\(B_p=(\Lambda_p^r a_p)/N\Lambda_p^r\). Equation (5.27) says that \(M(a)/N\Lambda^r\) is exactly the product of these \(B_p\), inside the displayed Chinese remainder decomposition. Completing this finite quotient at \(p\mid N\) retains precisely its \(p\)-component; exactness of completion therefore gives \(M(a)_p=\Lambda_p^r a_p\). At \(p\nmid N\), the two bounds in (5.30) already give \(M(a)_p=\Lambda_p^r\). Lemma 5.8 also proves its projectivity.

Conversely, choose a rational frame for \(M\). Clearing denominators of its finite abelian generators and of a rational basis chosen from \(M\) gives bounds of the form (5.30). At primes not dividing \(N\), its completion is \(\Lambda_p^r\). At each of the other primes, choose a local module basis; its row coordinates are the rows of an invertible matrix \(a_p\). The same Chinese remainder calculation recovers \(M\) from these completions and proves (5.27).

Finally, a \(\Lambda\)-isomorphism extends over \(\mathbb Q\) to an \(A\)-linear isomorphism of \(A^r\), hence to right multiplication by one \(b\in\operatorname{GL}_r(A)\). Equality of the corresponding local row lattices means that their bases differ by a left matrix \(u_p\in\operatorname{GL}_r(\Lambda_p)\). This is exactly (5.28). Conversely those matrices give equality of the local lattices after multiplication by \(b\), and (5.27) then gives an integral isomorphism. Adding a free summand is the stated identity-block stabilization. \(\square\)

**Corollary 5.11 (the integer-ring class in Taylor's statement).** If \(L/K\) is a finite tame Galois extension of number fields with group \(G\), and \(n=[K:\mathbb Q]\), then \(\mathcal O_L\) is a locally free \(\mathbb Z[G]\)-lattice of rank \(n\). Moreover

\[
 [\mathcal O_L]-[\mathcal O_K[G]]
       =c(\mathcal O_L)\in\operatorname{Cl}(\mathbb Z[G]).
\tag{5.31}
\]

It is zero precisely when \(\mathcal O_L\) is stably free as a \(\mathbb Z[G]\)-module.

**Proof.** The finiteness theorem in Noether's axioms for Dedekind domains, Theorem 4.1, makes both integer rings finite and torsion-free over \(\mathbb Z\). They span their number fields over \(\mathbb Q\), since multiplying any algebraic element by a common integer denominator of its monic equation makes it integral. The abelian freeness argument above therefore gives their ranks \([L:\mathbb Q]\) and \(n\).

The image of the relative trace \(\mathcal O_L\to\mathcal O_K\) is an ideal. By Theorem 2.1 and tameness its localization is \((\mathcal O_K)_{\mathfrak p}\) at every nonzero prime of \(\mathcal O_K\). A proper ideal would be contained in a maximal ideal and would remain proper there, so the trace ideal is all of \(\mathcal O_K\). Choose \(t\in\mathcal O_L\) with relative trace one. Multiplication by \(t\), regarded as a \(\mathbb Z\)-endomorphism of \(\mathcal O_L\), has group average equal to the identity. Higman's criterion, Theorem 3.1 over \(\mathbb Z\), proves projectivity over \(\mathbb Z[G]\).

The field normal basis theorem gives \(L\simeq K[G]\), and a \(\mathbb Q\)-basis of \(K\) identifies this with \(\mathbb Q[G]^n\). At every rational prime the completed integer module is projective with that free fraction module. Swan's rigidity theorem in Section 4 makes it \(\mathbb Z_p[G]^n\). This proves local freeness. Finally an abelian basis of \(\mathcal O_K\) gives \(\mathcal O_K[G]\simeq\mathbb Z[G]^n\). Equations (5.24)–(5.25) prove both the class formula and the last assertion. \(\square\)

### Torsion determinants of a prime-power group

The torsion kernel in Theorem 5.5 can be described exactly. This is the next ingredient for determinant descent. The proof below includes the induction and transfer calculations; compare the freely accessible [Chinburg–Pappas–Taylor, Section 7]. In this subsection \(R\) is an integral domain finite and free over \(\mathbb Z_p\), and \(H\) is a finite \(p\)-group. A Frobenius lift is unnecessary.

**Lemma 5.12 (induction for prime-power groups).** Over an algebraically closed field of characteristic zero, every irreducible representation of \(H\) is induced from a one-dimensional representation of a subgroup. A representation of dimension greater than one is induced from an irreducible representation of some subgroup of index \(p\). If an abelian subgroup \(B\subset H\) has index \(p\), every irreducible representation of dimension greater than one is induced from a one-dimensional representation of this particular \(B\). For determinants over \(R\), use the algebraic closure of \(R[1/p]\); the finitely many representations and roots of unity involved descend to a finite extension, by the coefficient argument of Lemma 4.A.

**Proof.** The class-equation argument in Theorem 5.5 supplies a nontrivial center for every nontrivial \(p\)-group. Every proper subgroup \(J\) is properly contained in its normalizer: let \(J\) act by left multiplication on \(H/J\). Its nontrivial orbit sizes are divisible by \(p\), while its fixed cosets are exactly \(N_H(J)/J\). The total number of cosets is divisible by \(p\), and at least one coset is fixed, so at least \(p\) cosets are fixed. It follows that a maximal proper subgroup is normal. Its quotient has no proper nontrivial subgroup; using its nontrivial center, it must be cyclic of order \(p\). Thus every proper subgroup is contained in one of index \(p\).

First pass to the faithful image of an irreducible representation \(V\). If this image is abelian, commuting finite-order matrices have a common eigenvector over a splitting field, and irreducibility makes \(V\) one-dimensional. If the image is nonabelian, its quotient by its center has nontrivial center. Choose an element \(b\) that is central modulo the center but not central itself. The subgroup generated by \(b\) and the center is abelian, normal and strictly larger than the center; call it \(B\).

The restriction of \(V\) to \(B\) is a direct sum of simultaneous eigenspaces. The image group permutes their characters transitively, since a sum over any orbit would be an invariant subspace. There is more than one character: otherwise \(B\) would act by scalars and faithfulness would put it in the center. Let \(J\) be the proper stabilizer of one character and \(W\) its eigenspace. The direct sum of the translates of \(W\) is \(V\), and gives explicitly

\[
 V\simeq\operatorname{Ind}_J^H W.
\tag{5.32}
\]

In (5.32), take inverse images of subgroups when returning from the faithful image to the original group. The space \(W\) is irreducible for \(J\): a proper invariant subspace would have translates whose direct sum is a proper \(H\)-submodule of \(V\). Repeating with this smaller group ends at a one-dimensional representation. The transitivity of induction follows directly by composing the tensor products of group algebras. If the initial representation is nonlinear, its final inducing subgroup is proper. Enlarge it to a subgroup \(J_1\) of index \(p\). The induced representation on \(J_1\) must be irreducible: a nontrivial direct-sum decomposition, which exists if it is reducible by characteristic-zero averaging, would induce a nontrivial direct-sum decomposition on \(H\). This proves the second assertion.

For the last assertion, the given subgroup \(B\) is normal, by the normalizer argument. Decompose \(V\) into its \(B\)-eigenspaces. Their transitive orbit has size either one or \(p\). If its size is one, \(B\) acts by scalars. One additional generator \(\gamma\) generates \(H/B\), and an eigenvector of \(\rho(\gamma)\) is then an \(H\)-invariant line, making \(V\) one-dimensional. Otherwise the stabilizer of an eigenspace is exactly \(B\). That eigenspace is irreducible for the abelian group \(B\), hence has dimension one, and its translates give (5.32) with this \(B\). \(\square\)

For any subgroup \(B\subset H\), left multiplication by \(x\in R[H]\) on the right \(R[B]\)-module \(R[H]\) gives a matrix \(M_B(x)\) using a right-module basis of left coset representatives. For a representation of \(B\) with character \(\theta\), applying that representation to the entries gives the matrix of \(x\) on \(\operatorname{Ind}_B^H\theta\). Thus

\[
 \operatorname{Det}(M_B(x))(\theta)
     =\operatorname{Det}(x)(\operatorname{Ind}_B^H\theta).
\tag{5.33}
\]

The expression on the right is defined multiplicatively on direct sums of irreducible characters. Formula (5.33) is a matrix identity and requires no induction theorem about class groups.

**Lemma 5.13 (transfer congruence).** Suppose \(B\) is abelian and has index \(p\) in \(H\). Choose \(\gamma\in H\setminus B\), and let \(\alpha\) act on \(R[B]\) by conjugation by \(\gamma\). It has order dividing \(p\). Define the additive trace subgroup

\[
 \mathcal T=\Bigl\{\sum_{i=0}^{p-1}\alpha^i(y):y\in R[B]\Bigr\}.
\]

The determinant \(N(x)=\det M_B(x)\) belongs to \(R[B]^\times\) when \(x\) is a unit, and is fixed by \(\alpha\). There is a homomorphism \(t:H\to B\), fixed by \(\alpha\), such that for \(x=\sum_h a_hh\),

\[
 N(x)\equiv\sum_{h\in H}a_h^p t(h)\pmod{\mathcal T}.
\tag{5.34}
\]

The congruence is in additive groups; \(\mathcal T\) is not assumed to be an ideal.

**Proof.** Use the basis \(1,\gamma,\ldots,\gamma^{p-1}\) over \(R[B]\). Left multiplication by one \(h\) is monomial: write

\[
 h\gamma^i=\gamma^{\sigma_h(i)}b_{h,i},\qquad b_{h,i}\in B.
\]

Define \(t(h)=\prod_i b_{h,i}\). Then \(N(h)=s(h)t(h)\), where \(s(h)\) is the sign of the coset permutation. Both \(N\) on units and \(s\) on group elements are multiplicative, so \(t\) is a homomorphism into the abelian group \(B\). It therefore kills \([H,H]\).

Right multiplication by \(\gamma\) commutes with left multiplication by \(x\) and is \(\alpha^{-1}\)-semilinear in this basis. Its matrix is a cyclic permutation with the wraparound coefficient \(\gamma^p\in B\). Commuting these two operations gives \(N(x)=\alpha^{-1}N(x)\) on taking determinants; the determinant of the semilinear change-of-basis matrix cancels on the two sides. In particular \(t(h)\) is fixed by \(\alpha\).

Now expand \(\det M_B(x)\) by multilinearity in the columns. A term chooses a label \(h_i\in H\) in each column \(i\), and is nonzero exactly when the selected rows form a permutation. Shift all column and row indices cyclically, keeping the selected labels. The scalar factor \(\prod_i a_{h_i}\) and the permutation sign stay the same. The \(B\)-coefficient changes by \(\alpha^{-1}\): the wraparound factors cancel because each input and each output index occurs exactly once. Consequently a full orbit of \(p\) terms contributes the additive trace of one coefficient and belongs to \(\mathcal T\).

The fixed terms have all labels equal to one \(h\). Conversely a constant label has the coset permutation \(\sigma_h\), a cyclic shift, and supplies exactly the term \(a_h^p N(h)\). For odd \(p\), the sign of every cyclic shift is one. For \(p=2\), replacing its possible sign minus one by plus one changes the term by \(2a_h^2t(h)\), which is in \(\mathcal T\) because \(t(h)\) is \(\alpha\)-fixed and \(\alpha\) fixes \(R\). Thus the fixed terms, together with the full orbits, give (5.34) for every \(p\). \(\square\)

**Theorem 5.14 (the torsion determinant theorem).**

\[
 \operatorname{Det}(1+I(R[H]))_{\mathrm{tors}}
      =\operatorname{Det}(H).
\tag{5.35}
\]

In particular, writing \(J=\ker(R[H]\to R[H^{\mathrm{ab}}])\), when \(R\) has a Frobenius lift as in Theorem 5.5, that theorem's determinant logarithm is injective on \(\operatorname{Det}(1+J)\).

**Proof: abelian groups.** If \(H\) is abelian, its one-dimensional character evaluations identify its group algebra over a splitting field with a product of fields, by the characteristic-zero algebra decomposition in Section 5. Thus they detect its elements and its units. An element of \(1+I\) has all evaluations principal units: nilpotence of the augmentation ideal modulo \(p\), proved in Theorem 5.5, makes the evaluation of its difference from one have positive valuation. A finite-order principal unit has \(p\)-power order. Indeed, if its order has a prime-to-\(p\) factor \(m\), apply the identity

\[
 (1+z)^m-1=z\bigl(m+\tbinom m2z+\cdots+z^{m-1}\bigr).
\]

The factor in parentheses is a unit when \(v(z)>0\) and \(p\nmid m\), so no nonidentity principal unit can have order \(m\). Taking the appropriate power of a finite-order unit proves the assertion.

Induct on \(|H|\). Choose \(c\in H\) of order \(p\). For a torsion unit \(x\in1+I\), its image in \(R[H/\langle c\rangle]\) is a group element by induction. Multiply \(x\) by the inverse of a lift of that element. We can now write

\[
 1-x=(1-c)y,\qquad y\in R[H].
\tag{5.36}
\]

Choose a one-dimensional character \(\theta\) with \(\theta(c)\ne1\). Such a character exists because all one-dimensional evaluations detect the nonidentity element \(c\). The divisibility in (5.36) implies that \(\theta(x)\) is either one or a primitive \(p\)th root of unity. To see this, a primitive root \(\zeta\) of order \(p^s\) has

\[
 v(1-\zeta)=\frac1{p^{s-1}(p-1)},\qquad v(p)=1.
\tag{5.37}
\]

This is the exact prime-power ramification identity proved in Cyclotomic fields, Theorem 12.2, equation (7), after completion. All coefficients of \(R\) are integral in the coefficient field: multiplication on the finite free \(\mathbb Z_p\)-module \(R\) supplies a monic characteristic equation. They therefore have nonnegative valuation in any extension. Divisibility of \(1-\theta(x)\) by \(1-\theta(c)\), together with (5.37), forces \(s\leq1\).

Multiplying \(x\) by a suitable power of \(c\) makes \(\theta(x)=1\) while preserving (5.36). It follows that \(\theta(y)=0\). If this new \(x\) were not one, some further character \(\eta\) would have \(\eta(x)\ne1\). Then \(\eta(c)\ne1\) by (5.36), and \(\eta(x)\) is again a primitive \(p\)th root. Equation (5.37) makes \(\eta(y)\) a unit. But, writing \(y=\sum_h b_hh\), the equality \(\theta(y)=0\) gives

\[
 \eta(y)=\sum_h b_h\bigl(\eta(h)-\theta(h)\bigr).
\]

Every root of \(p\)-power order reduces to one in the residue field, since \(X^{p^s}-1=(X-1)^{p^s}\) in characteristic \(p\). The last sum is therefore in the maximal ideal of a finite coefficient extension, contradicting that it is a unit. Thus the adjusted \(x\) is one. Reversing the two group-element multiplications proves that the original \(x\) belongs to \(H\). This proves (5.35) for abelian groups.

**Proof: an abelian subgroup of index \(p\).** Let \(B\) be such a subgroup of \(H\), and let \(x\in1+I(R[H])\) have torsion determinant. Its image in \(R[H^{\mathrm{ab}}]\) is an augmentation-one torsion unit, since one-dimensional evaluations detect that algebra. The abelian case makes this image a group element. Multiply \(x\) by the inverse of a group lift, so that its image in this abelian group algebra is one. It suffices to show that its determinant is now one.

The norm \(N(x)\) of Lemma 5.13 is torsion, by (5.33) and the one-dimensional character detection for \(B\). Its augmentation is one: \(\operatorname{Ind}_B^H1_B\) is the regular representation of the cyclic quotient \(H/B\), all of whose one-dimensional evaluations of \(x\) are one. The abelian case gives \(N(x)=b\in B\); Lemma 5.13 also makes \(b\) fixed by \(\alpha\).

Write \(x=\sum_h a_hh\). Its trivial image in \(R[H^{\mathrm{ab}}]\) means that, for each coset \(q\in H/[H,H]\),

\[
 \sum_{h\in q}a_h=
 \begin{cases}
 1,&q=[H,H],\\
 0,&q\ne[H,H].
 \end{cases}
\]

The transfer \(t\) kills \([H,H]\). The ordinary binomial theorem modulo \(p\) and (5.34) consequently give

\[
 b=N(x)\equiv1\pmod{\mathcal T+pR[B]}.
\tag{5.38}
\]

If \(b\ne1\), inspect its coefficient in \(b-1\). The element \(b\) is a fixed basis element for \(\alpha\), so every additive trace has coefficient divisible by \(p\) at \(b\). The same is true of an element of \(pR[B]\), while that coefficient in \(b-1\) is one. This contradicts (5.38). Hence \(N(x)=1\). Lemma 5.12 makes every nonlinear irreducible character an induction from this \(B\), and (5.33) gives determinant one on it. The linear characters already have value one. This proves the result in this case.

**Proof: the general group.** Induct on \(|H|\), using the abelian case to start. As before, adjust \(x\) by a group element until its image in \(R[H^{\mathrm{ab}}]\) is one. Given a nonlinear irreducible character \(\chi\), Lemma 5.12 writes it as \(\operatorname{Ind}_B^H\theta\) for a subgroup \(B\) of index \(p\). This \(B\) is normal. Its commutator subgroup \([B,B]\) is normal in \(H\), since it is preserved by every automorphism of \(B\).

The image of \(x\) in \(R[H/[B,B]]\) has torsion determinant, and its image in the abelianization is still one, because \([B,B]\subseteq[H,H]\). The index-\(p\) case, applied to \(B/[B,B]\), makes its determinant one.

Now consider the matrix \(M_B(x)\). By Lemma 5.6 its determinant function equals that of a unit \(y\in R[B]^\times\). Its augmentation is one, by (5.33) at \(1_B\) and the decomposition of the cyclic quotient's regular representation into linear characters. Thus \(y\in1+I(R[B])\). Its determinant is torsion. Passing this matrix to \(R[B/[B,B]]\) commutes with the quotient calculation just made. Formula (5.33) therefore makes all one-dimensional evaluations of its image equal to one. Since these evaluations detect the abelian algebra, the image of \(y\) in \(R[B^{\mathrm{ab}}]\) is one.

By induction on the smaller group \(B\), \(\operatorname{Det}(y)=\operatorname{Det}(b)\) for some \(b\in B\). Its abelian image is one, so \(b\in[B,B]\). The determinant of a representation is a one-dimensional group homomorphism, hence is one on every commutator. Thus \(\operatorname{Det}(y)=1\), and (5.33) gives \(\operatorname{Det}(x)(\chi)=1\). This treats every nonlinear \(\chi\); the linear values were already one. It proves the forward inclusion of (5.35). The reverse inclusion holds because each \(h\in H\) is an augmentation-one unit of finite order.

Finally, an element of \(\operatorname{Det}(1+J)\) in the logarithm kernel is torsion by Theorem 5.5. By (5.35) it is \(\operatorname{Det}(h)\) for some \(h\in H\). Its linear evaluations are all one because its abelian image is one; they detect \(H^{\mathrm{ab}}\), so \(h\in[H,H]\) and its entire determinant is one. This proves the injectivity assertion. \(\square\)

### The logarithm image and determinant descent

We retain the finite \(p\)-group \(H\) and the coefficient domain \(R\) of Theorem 5.5, including its Frobenius lift. Put

\[
 J_R=\ker(R[H]\longrightarrow R[H^{\mathrm{ab}}]),
 \qquad I_R=\ker(R[H]\longrightarrow R).
\]

The ideal \(J_R\) lies in \(I_R\), so its elements are topologically nilpotent by the convergence proof in Theorem 5.5. In the notation of that theorem, write \(\nu_R\) for the integral determinant logarithm.

**Lemma 5.15 (one central commutator).** Let \(c\) be central of order \(p\), and put \(\delta=1-c\). Then

\[
 \mathcal L_R(1+\delta R[H])
       \subseteq p\phi(\delta R[H]),\qquad
 \mathcal L_R(1+\delta I_R)
       =p\phi(\delta I_R).
\tag{5.39}
\]

If \(c\) is also a commutator in \(H\), then

\[
 \nu_R:\operatorname{Det}(1+\delta R[H])
       \xrightarrow{\ \sim\ }p\phi(\delta R[H]).
\tag{5.40}
\]

On this subgroup the logarithm is just \(p\phi\log\); it is independent of the chosen Frobenius lift.

**Proof.** The binomial equation \(c^p=1\) implies \(\delta^p\in p\delta\mathbb Z_p[\langle c\rangle]\). Since \(\delta\) is central, iteration gives

\[
 \delta^n\in p^{\lfloor(n-1)/(p-1)\rfloor}
                     \delta\mathbb Z_p[\langle c\rangle].
\]

The inequality \(\lfloor(n-1)/(p-1)\rfloor\geq v_p(n)\), proved in Theorem 5.5, shows that \(\delta^n/n\) belongs to that last principal ideal for every \(n\geq1\). Moreover \(\Psi\phi(\delta R[H])=0\): on each basis element the two terms have the same \(p\)th power because \(c\) is central and \(c^p=1\). Hence the logarithm on \(1+\delta R[H]\) is \(p\phi\log\). The convergent series and the divisibility just proved place its values in \(p\phi(\delta R[H])\).

For \(x\in I_R^m\), with \(m\geq1\), the same series gives

\[
 p^{-1}\mathcal L_R(1+\delta x)
          \equiv\phi(\delta x)\pmod{\phi(\delta I_R^{2m})}.
\tag{5.41}
\]

Indeed all terms after the first have the form \(\phi(\delta^nx^n/n)\) with \(n\geq2\). Their coefficients belong to \(\delta R[H]\) and their factors \(x^n\) belong to \(I_R^{2m}\). These ideals and their images under \(\phi\) are closed: they are submodules of finite free \(\mathbb Z_p\)-modules. For completeness, the DVR basis argument puts any such submodule in a basis of the ambient module by successively choosing a vector with a coordinate of minimal valuation and clearing that coordinate; it expresses the submodule as a sum of finitely many principal coordinate ideals, which are closed. Thus the limit has the same containment.

Given a target in \(p\phi(\delta I_R)\), choose \(x_0\in I_R\) matching its first term in (5.41). The error belongs to \(p\phi(\delta I_R^2)\); choose \(x_1\in I_R^2\) matching that error, then \(x_2\in I_R^4\), and continue. Multiplying the successive units \(1+\delta x_i\) adds their logarithms, by Theorem 5.5. The filtration \(I_R^{2^i}\) tends to zero \(p\)-adically, so the products converge to a unit in \(1+\delta I_R\), and their logarithms converge to the desired target. This proves the equality in (5.39).

Now suppose \(c=[a,b]\). Since \(R[H]=Rb+I_R\),

\[
 \delta R[H]=R(b-aba^{-1})+\delta I_R.
\]

The first summand has zero image under \(\phi\), giving \(\phi(\delta R[H])=\phi(\delta I_R)\). Thus (5.39) proves surjectivity in (5.40). Also \(\delta R[H]\subset J_R\). The injectivity assertion of Theorem 5.14 proves injectivity in (5.40). \(\square\)

**Theorem 5.16 (the logarithm on the commutator ideal).**

\[
 \nu_R:\operatorname{Det}(1+J_R)
       \xrightarrow{\ \sim\ }p\phi(J_R).
\tag{5.42}
\]

There is an exact sequence of abelian groups

\[
 0\longrightarrow p\phi(J_R)
 \xrightarrow{\nu_R^{-1}}\operatorname{Det}(R[H]^\times)
 \longrightarrow R[H^{\mathrm{ab}}]^\times\longrightarrow1.
\tag{5.43}
\]

The final map is determined by the one-dimensional character values. The symbol \(\nu_R^{-1}\) in the first arrow refers only to the subgroup in (5.42).

**Proof.** We prove the image formula by induction on \(|H|\), with the abelian case immediate since then \(J_R=0\). A nonabelian finite \(p\)-group has a central commutator of order \(p\). Here are the group details. Induction on \(|H|\) through the nontrivial center shows that the upper central series reaches \(H\). Its defining commutator containments force the lower central series to reach one. The last nontrivial lower-central term is central and generated by commutators \([a,b]\), so choose one nonidentity such commutator \(d\). If it has order \(p^k\), centrality gives \([a,b^{p^{k-1}}]=d^{p^{k-1}}\), a central commutator of order \(p\). Denote it by \(c\), and put \(\bar H=H/\langle c\rangle\). Its abelianization is still \(H^{\mathrm{ab}}\).

Multiplication by \(c\) permutes the conjugacy classes of \(H\). Its orbits correspond exactly to conjugacy classes of \(\bar H\): if two images are conjugate, their lifts differ by conjugation and by a power of \(c\), and the converse is immediate. The map on the free modules of conjugacy classes therefore has kernel

\[
 \ker(R[\mathcal C_H]\to R[\mathcal C_{\bar H}])
                     =(1-c)R[\mathcal C_H].
\tag{5.44}
\]

On each orbit this is the submodule of coefficient sum zero, generated by successive differences. The quotient is free, so the kernel is saturated; in particular its intersection with \(pR[\mathcal C_H]\) is \(p\) times itself. The map \(\phi(J_R)\to\bar\phi(J_R(\bar H))\) is onto, because the group-algebra quotient maps the commutator ideal onto the commutator ideal. Its kernel is the entire module (5.44), since \((1-c)R[H]\subset J_R\).

Given \(j\in J_R\), the induction hypothesis supplies an augmentation-one unit \(1+\bar x\), with \(\bar x\in J_R(\bar H)\), whose logarithm is \(p\bar\phi(\bar j)\). Lift \(\bar x\) to \(x\in J_R\). The difference between \(p\phi(j)\) and \(\mathcal L_R(1+x)\) is in \(pR[\mathcal C_H]\) by Theorem 5.5, and is in the kernel (5.44) by the construction. Saturation and Lemma 5.15 supply a unit in \(1+(1-c)R[H]\) with precisely this difference as logarithm. Multiply it by \(1+x\). This proves that \(p\phi(J_R)\) is contained in the image.

Conversely, given \(x\in J_R\), its logarithm maps, by induction, into \(p\bar\phi(J_R(\bar H))\). Choose a lift \(j\in J_R\) of the corresponding additive element. The difference \(\mathcal L_R(1+x)-p\phi(j)\) belongs to \(p\) times (5.44), which is contained in \(p\phi(J_R)\). This proves the opposite containment. Theorem 5.14 proves injectivity on determinants, completing (5.42).

For (5.43), a unit in \(R[H^{\mathrm{ab}}]\) lifts to a unit in \(R[H]\). Indeed lift it and its inverse arbitrarily; their two inverse errors lie in \(J_R\), and geometric series remove both errors. The image of a determinant function in the abelian group algebra is uniquely determined by its values on the linear characters, which detect that algebra as proved in Section 5. The kernel consists exactly of \(\operatorname{Det}(1+J_R)\). Equation (5.42) identifies that kernel with the first term. All assertions of exactness follow. \(\square\)

**Theorem 5.17 (descent for prime-power groups).** Let \(R\subset S\) be integral domains finite and free over \(\mathbb Z_p\), each with a Frobenius lift as in Theorem 5.5. Suppose a finite group \(\Delta\) acts on \(S\) by \(R\)-algebra automorphisms and \(S^\Delta=R\). Then, for every finite \(p\)-group \(H\),

\[
 \operatorname{Det}(S[H]^\times)^\Delta
                  =\operatorname{Det}(R[H]^\times).
\tag{5.45}
\]

The action means coefficient action on a representing unit. We also have

\[
 \operatorname{Det}(1+I_S)^\Delta
                  =\operatorname{Det}(1+I_R).
\tag{5.46}
\]

The two Frobenius lifts need not agree or commute with \(\Delta\).

**Proof.** Induct on \(|H|\). For abelian \(H\), the determinant map detects the actual unit. An invariant unit has every group coefficient in \(S^\Delta=R\), and its inverse has the same property. This proves the assertion in that case, including (5.46).

For nonabelian \(H\), choose a central commutator \(c\) of order \(p\) as in Theorem 5.16, and put \(\bar H=H/\langle c\rangle\). We first identify the kernel of the quotient map on determinants:

\[
 \ker\bigl(\operatorname{Det}(1+I_S(H))
       \to\operatorname{Det}(1+I_S(\bar H))\bigr)
           =\operatorname{Det}(1+(1-c)S[H]).
\tag{5.47}
\]

If a determinant is in that kernel, its linear character values are one because \(H\) and \(\bar H\) have the same abelianization. Hence it belongs to \(\operatorname{Det}(1+J_S)\) by (5.43). Under the isomorphism (5.42), its logarithm is in the kernel (5.44), multiplied by \(p\). Lemma 5.15 supplies a determinant from \(1+(1-c)S[H]\) with that logarithm, and injectivity on \(1+J_S\) identifies the two determinants. This proves (5.47); the reverse inclusion also follows directly from the quotient.

Now let \(d\in\operatorname{Det}(1+I_S(H))^\Delta\). Its image on \(\bar H\) descends by induction. Lift a representing augmentation-one unit from \(R[\bar H]\) to \(R[H]\), which is possible because the augmentation ideals map onto one another. Divide \(d\) by its determinant. The resulting invariant determinant lies in (5.47).

On this kernel, Lemma 5.15 identifies the logarithm with \(p\phi\log\). That map commutes with coefficient automorphisms and has the same restriction over \(R\), regardless of the Frobenius lifts. Its invariant values lie in

\[
 \bigl(p(1-c)S[\mathcal C_H]\bigr)^\Delta
                         =p(1-c)R[\mathcal C_H].
\tag{5.48}
\]

To check the equality, use the orbit description in (5.44): the module is the sum-zero submodule on each \(c\)-orbit of conjugacy classes. An invariant vector has coefficients in \(R\). After division by \(p\), its coefficients remain invariant because the rings have characteristic zero; its orbit sums remain zero. This is exactly the module on the right. Lemma 5.15 now supplies a determinant over \(R\) with that logarithm. Its injectivity over \(S\) proves equality of determinants. Restoring the previously divided determinant proves (5.46).

For a general unit, its augmentation \(a\in S^\times\) is its determinant value on the trivial character. If its determinant is invariant, \(a\in R^\times\): its inverse is invariant too. Dividing the unit by \(a\) makes it augmentation-one. Apply (5.46) and then restore the scalar unit. This proves (5.45). \(\square\)

### Norms of determinant units

The norm used in descent is the restriction of a matrix automorphism along a finite coefficient extension. Its determinant values can be computed as products of coefficient conjugates. This construction avoids choosing an order for a product of noncommuting group-ring elements.

Let \(R\subset S\) be coefficient domains as in Theorem 5.17, and suppose additionally that \(S\) is finite free over \(R\), that the extension of coefficient fields \(E/T\) is Galois with group \(\Delta\), and that \(S^\Delta=R\). Assume the coefficient trace \(\operatorname{Tr}_{E/T}:S\to R\) is onto. For an arbitrary finite group \(H\), left multiplication by \(x\in S[H]^\times\), on \(S[H]\) regarded as a right \(R[H]\)-module, gives an invertible matrix \(M_R(x)\). Lemma 5.6 shows that its determinant function is in \(\operatorname{Det}(R[H]^\times)\). Define

\[
 \mathcal N_{S/R}(\operatorname{Det}x)
          =\operatorname{Det}(M_R(x)).
\tag{5.49}
\]

**Lemma 5.18 (the norm formula).** This definition is independent of the \(R\)-basis of \(S\), is well defined on determinant functions, and is a group homomorphism. Its formula is

\[
 \mathcal N_{S/R}(d)=\prod_{\sigma\in\Delta}\sigma(d).
\tag{5.50}
\]

The product is in the abelian group of determinant functions, with \(\sigma(\operatorname{Det}x)=\operatorname{Det}(\sigma x)\). Formation of this norm commutes with passing from \(H\) to a quotient group.

**Proof.** A change of coefficient basis conjugates \(M_R(x)\), so does not change any of its character determinants. Extend scalars to an algebraically closed field \(U\) containing \(E\). The separable field-algebra decomposition is

\[
 U\otimes_T E\simeq\prod_{\sigma\in\Delta}U,
 \qquad u\otimes e\longmapsto(u\sigma(e))_\sigma.
\]

Here is the underlying field argument. The primitive-element proof in Algebraic integers and rings of integers, Section 1, supplies \(E=T(\eta)\) for a finite separable extension in characteristic zero. Its minimal polynomial has distinct roots \(\sigma(\eta)\). Evaluation at these roots and the polynomial Chinese remainder theorem give the displayed decomposition. Under it, the matrix of multiplication by \(x\) becomes a direct sum of the multiplication matrices for its coefficient conjugates. Applying a character of \(H\) and taking determinants proves (5.50). The same reasoning works for a matrix over \(S[H]\), and proves that only its determinant function matters. Multiplicativity follows either from multiplication of the matrices \(M_R(x)\) or from (5.50). The quotient assertion follows by applying the quotient homomorphism to their entries; their chosen coefficient basis stays the same. \(\square\)

**Theorem 5.19 (norm surjectivity for prime-power groups).** For a finite \(p\)-group \(H\),

\[
 \begin{aligned}
 \mathcal N_{S/R}\bigl(\operatorname{Det}(1+I_S)\bigr)
       &=\operatorname{Det}(1+I_R),\\
 \mathcal N_{S/R}\bigl(\operatorname{Det}(1+J_S)\bigr)
       &=\operatorname{Det}(1+J_R).
 \end{aligned}
\tag{5.51}
\]

The full norm \(\operatorname{Det}(S[H]^\times)\to\operatorname{Det}(R[H]^\times)\) is onto exactly when the coefficient-unit norm \(N_{E/T}:S^\times\to R^\times\) is onto. The Frobenius lifts on the two coefficient rings need not be compatible.

**Proof: the abelian case.** When \(H\) is abelian, determinants identify actual units, and (5.50) is the usual coefficient norm on the commutative group algebra. For \(z\in I_S^m\),

\[
 \prod_{\sigma\in\Delta}(1+\sigma z)
    \equiv1+\operatorname{Tr}_{E/T}(z)\pmod{I_S^{m+1}}.
\tag{5.52}
\]

Every term involving at least two factors is in \(I_S^{2m}\subseteq I_S^{m+1}\). The product is a unit over \(R\), because it and its inverse are coefficient-invariant.

We must also identify the error as an element of \(I_R^{m+1}\). The group algebra is finite free over \(R\), and \(I_S^m=S\otimes_R I_R^m\). Choose \(t\in S\) with coefficient trace one. The \(R\)-linear map \(s\mapsto\operatorname{Tr}_{E/T}(ts)\) is a retraction of \(R\subset S\). Tensoring this retraction with \(R[H]/I_R^m\) proves \(I_S^m\cap R[H]=I_R^m\). Thus (5.52) has its stated error in the ideal over \(R\) as well.

Given an error \(r\in I_R^m\), set \(z=tr\in I_S^m\); its trace is \(r\). Formula (5.52) corrects that error up to \(I_R^{m+1}\). Begin with a prescribed unit in \(1+I_R\), and successively make these corrections for \(m=1,2,3,\ldots\). The units constructed in \(1+I_S\) converge, since \(I_S^m\) tends to zero \(p\)-adically. The resulting norm is the prescribed unit, by continuity and \(\bigcap_m I_R^m=0\). This proves the first equality for abelian groups; the second is vacuous because their commutator ideal is zero.

**Proof: commutator determinants.** For nonabelian \(H\), choose a central commutator \(c\) of order \(p\) as in Theorem 5.16. On \(\operatorname{Det}(1+(1-c)S[H])\), the logarithm is \(p\phi\log\). Equations (5.50) and (5.18) imply

\[
 \nu_R\bigl(\mathcal N_{S/R}(d)\bigr)
                =\operatorname{Tr}_{E/T}\bigl(\nu_S(d)\bigr).
\tag{5.53}
\]

Here the norm belongs to the central-commutator determinant subgroup over \(R\): it belongs to the quotient kernel (5.47), since every coefficient conjugate does. On this subgroup Lemma 5.15 supplies the logarithm isomorphisms over both rings. The sum-zero conjugacy-orbit bases in (5.44) make \(p(1-c)S[\mathcal C_H]\) the scalar extension of \(p(1-c)R[\mathcal C_H]\). The trace is onto on these modules, by multiplying each coefficient by \(t\). Therefore (5.53) and the injectivity in Lemma 5.15 show

\[
 \mathcal N_{S/R}\bigl(\operatorname{Det}(1+(1-c)S[H])\bigr)
                 =\operatorname{Det}(1+(1-c)R[H]).
\tag{5.54}
\]

Now induct on \(|H|\) to prove the second equality of (5.51). Its base case is the abelian group. The quotient \(\bar H=H/\langle c\rangle\) has the same abelianization. A target determinant in \(\operatorname{Det}(1+J_R)\) has, by induction, a norm preimage in \(\operatorname{Det}(1+J_S(\bar H))\). Lift its representing commutator-ideal element to \(J_S(H)\). Dividing the target by the norm of this lift gives a determinant in the central-commutator kernel (5.47) over \(R\). Equation (5.54) supplies its remaining norm preimage, also in \(1+J_S\). Multiplying the two preimages proves the second equality.

**Proof: augmentation and all units.** Given a target in \(\operatorname{Det}(1+I_R)\), first take its abelian image. The abelian case gives a norm preimage in \(1+I_S(H^{\mathrm{ab}})\). Lift its augmentation-ideal element to \(I_S(H)\). The discrepancy after taking the norm has trivial abelian image, so lies in \(\operatorname{Det}(1+J_R)\) by (5.43). The second equality just proved supplies its norm preimage. This proves the first equality. In both equalities the reverse inclusion follows from (5.50) and the augmentation or abelianization maps.

Finally the trivial character evaluates the determinant of a unit as its coefficient augmentation. Evaluation of (5.50) on that character is the coefficient-unit norm. Its surjectivity is therefore necessary for surjectivity of the full determinant norm. If it is onto, choose a scalar preimage for the augmentation of any target determinant, divide by its scalar norm, and apply the first equality of (5.51) to the remaining augmentation-one determinant. This proves sufficiency. \(\square\)

### Character operations on integral determinants

To pass from prime-power groups to general finite groups, we need to use subgroup induction without losing integrality. We prove the required determinant operations directly with integral representation matrices [Chinburg–Pappas–Taylor, Section 5.a]. An induction formula for characters is an additional result; these operations alone do not supply one.

Here \(G\) is any finite group, \(R\) is an integral domain finite and free over \(\mathbb Z_p\), and \(T=R[1/p]\). Let \(\mathscr R(G)\) be the free abelian group on the irreducible characters over an algebraic closure of \(T\). Its addition is direct sum, and multiplication is the tensor product, extended to virtual characters. Characteristic-zero averaging and the matrix-algebra decomposition in Section 5 show that a representation is determined by its irreducible multiplicities and hence by its character. Its **contragredient** character is \(\theta^\vee(g)=\theta(g^{-1})\), as follows from the trace of the dual action.

**Lemma 5.20 (integral character action).** If \(\theta\) is the character of a finite-dimensional \(\mathbb Q_p[G]\)-representation and \(d\in\operatorname{Det}(R[G]^\times)\), define

\[
 (\theta\cdot d)(\chi)=d(\theta^\vee\chi)
                  \qquad(\chi\in\mathscr R(G)).
\tag{5.55}
\]

This belongs to \(\operatorname{Det}(R[G]^\times)\). The operation depends only on the character, and extends to virtual characters of \(\mathbb Q_p[G]\). It satisfies

\[
 (\theta_1+\theta_2)\cdot d
       =(\theta_1\cdot d)(\theta_2\cdot d),\qquad
 (\theta_1\theta_2)\cdot d
       =\theta_1\cdot(\theta_2\cdot d),\qquad
 1_G\cdot d=d.
\tag{5.56}
\]

For fixed \(\theta\), it is a homomorphism on determinant groups. It commutes with automorphisms of the coefficient ring that fix \(\mathbb Z_p\).

**Proof.** Choose a \(G\)-stable \(\mathbb Z_p\)-lattice in the representation: take a basis lattice and sum its finitely many translates by \(G\). This is finite and torsion-free over the DVR, hence free by the basis argument of lesson one. In its basis the matrices \(\rho(g)\) and their inverses lie in \(\operatorname{GL}_n(\mathbb Z_p)\).

Tensor this lattice with the free left \(R[G]\)-module \(R[G]\), giving the diagonal \(G\)-action on \(V_R\otimes_R R[G]\). It is free over \(R[G]\), as is seen from the explicit isomorphism

\[
 v\otimes g\longmapsto g\otimes\rho(g^{-1})v,
 \qquad
 g\otimes w\longmapsto\rho(g)w\otimes g.
\tag{5.57}
\]

On the right, \(G\) acts only on the first factor. Tensoring right multiplication by a group-ring unit \(x=\sum_g x_gg\) with the identity of \(V_R\) is an automorphism of the diagonal module. Using row coordinates over the left module, as in Theorem 5.10, its matrix through (5.57) is

\[
 U_\theta(x)=\sum_g x_g g\rho(g^{-1})^{\mathsf T}.
\tag{5.58}
\]

Concretely the output on a coordinate \(h\otimes w\) is \(\sum_g x_g hg\otimes\rho(g^{-1})w\); converting the coordinate column of \(w\) to the row convention accounts for the transpose in (5.58). The matrix is invertible because the inverse comes from \(x^{-1}\). Evaluating its entries in a representation with character \(\chi\) gives the sum of matrices \(x_g\rho_\chi(g)\otimes\rho(g^{-1})^{\mathsf T}\), up to the fixed permutation of tensor coordinates. The second tensor factor is precisely the dual representation. Its determinant is therefore the right side of (5.55).

Lemma 5.6 replaces the determinant of this integral matrix by the determinant of an integral group-ring unit. Thus (5.55) preserves the desired integral determinant group. Its formula proves independence of the lattice and dependence only on the character. Direct sums multiply determinants, tensor products compose the character argument, and the trivial representation leaves it unchanged; these observations prove (5.56). Negative virtual multiplicities act by inverses. Multiplicativity in \(d\) follows by evaluation on characters. Finally the matrices \(\rho(g)\) have entries in \(\mathbb Z_p\), so (5.58) commutes with the specified coefficient automorphisms. \(\square\)

**Lemma 5.21 (subgroup operations).** For \(B\subseteq G\), define

\[
 \begin{aligned}
 \operatorname{Res}^{B}_{G}(d)(\eta)
     &=d(\operatorname{Ind}_{B}^{G}\eta),\\
 \operatorname{Ind}^{G}_{B}(e)(\chi)
     &=e(\operatorname{Res}_{B}^{G}\chi).
 \end{aligned}
\tag{5.59}
\]

They give homomorphisms from \(\operatorname{Det}(R[G]^\times)\) to \(\operatorname{Det}(R[B]^\times)\) and in the opposite direction, respectively. Here the upper and lower placements distinguish the two determinant operations; the character operations inside their arguments are the ordinary restriction and induction of representations. For a virtual \(\mathbb Q_p[B]\)-character \(\theta\),

\[
 (\operatorname{Ind}_B^G\theta)\cdot d
    =\operatorname{Ind}^{G}_{B}
        \bigl(\theta\cdot\operatorname{Res}^{B}_{G}(d)\bigr).
\tag{5.60}
\]

**Proof.** Left multiplication by \(x\in R[G]^\times\) on the free right \(R[B]\)-module \(R[G]\) gives the subgroup matrix of (5.33). That equation shows that its determinant function is the first formula in (5.59), and Lemma 5.6 replaces it by the determinant of a unit in \(R[B]\). For the second formula, simply regard a unit of \(R[B]\) as a unit of \(R[G]\); restricting the representation used to evaluate it gives precisely the second formula. Both constructions are homomorphisms and depend only on the determinant functions, by the displayed formulas.

To prove (5.60), the projection formula for representations is needed. Its explicit isomorphism is

\[
 V\otimes_U\bigl(U[G]\otimes_{U[B]}W\bigr)
  \longrightarrow U[G]\otimes_{U[B]}
                    (\operatorname{Res}_{B}^{G}V\otimes_U W),
 \qquad v\otimes(g\otimes w)\longmapsto
                    g\otimes(g^{-1}v\otimes w),
\tag{5.61}
\]

over a splitting field \(U\). The relation \(gb\otimes w=g\otimes bw\) verifies that this map is well defined; its inverse is \(g\otimes(v\otimes w)\mapsto gv\otimes(g\otimes w)\). Both are \(G\)-equivariant. The dual of an induced representation is induced from the dual. One can check this by the same coset bases: pair the summands on matching cosets by the invariant evaluation pairing and pair distinct cosets by zero. This gives a nondegenerate \(G\)-invariant pairing between the two induced spaces, identifying one with the dual of the other.

Thus, for every character \(\chi\),

\[
 \chi(\operatorname{Ind}_B^G\theta)^\vee
      =\operatorname{Ind}_B^G
                   ((\operatorname{Res}_B^G\chi)\theta^\vee).
\]

Evaluate \(d\) on these equal characters. Equations (5.55) and (5.59) give (5.60). Additivity extends the proof from representations to virtual characters. \(\square\)

**Corollary 5.22 (how an induction formula is used).** Suppose the following identity has been proved for virtual \(\mathbb Q_p\)-characters:

\[
 m\,1_G=\sum_i n_i\operatorname{Ind}_{B_i}^G\theta_i,
       \qquad m,n_i\in\mathbb Z.
\tag{5.62}
\]

Let \(R\subset S\) and \(\Delta\) be as in Theorem 5.17. If an invariant determinant \(d\in\operatorname{Det}(S[G]^\times)^\Delta\) restricts to a determinant over \(R\) on each \(B_i\), then

\[
 d^m\in\operatorname{Det}(R[G]^\times).
\tag{5.63}
\]

**Proof.** Lemmas 5.20–5.21 give

\[
 d^m=\prod_i
   \operatorname{Ind}^{G}_{B_i}
     \bigl(\theta_i\cdot\operatorname{Res}^{B_i}_{G}(d)\bigr)^{n_i}.
\]

Each restricted determinant is over \(R\) by hypothesis, character action preserves integrality there by Lemma 5.20, and determinant induction preserves it by Lemma 5.21. Their product and inverse powers remain over \(R\). This proves (5.63). It does not permit extraction of an \(m\)th root without a separate argument. \(\square\)

### A rational induction identity at a fixed prime

We next prove the character identity needed for the prime-\(p\) part of determinant descent. A **\(\mathbb Q_p\)-elementary group at \(p\)** means a semidirect product \(C\rtimes P\), where \(C\) is cyclic of order prime to \(p\), \(P\) is a \(p\)-group, and conjugation by \(P\) on \(C\) acts by powers belonging to \(\operatorname{Gal}(\mathbb Q_p(\mu_{|C|})/\mathbb Q_p)\). The last condition is part of the definition; a cyclic-by-prime-power group need not satisfy it. Compare [Chinburg–Pappas–Taylor, Section 5.b] for the induction statement.

Let \(\mathscr R_p(G)\) be the character ring of finite-dimensional \(\mathbb Q_p[G]\)-representations. It is the free abelian group on their simple isomorphism classes, because characteristic-zero averaging gives semisimplicity and composition multiplicities are unique as proved in Lemma 4.C. Multiplication is tensor product. This ring maps to the character ring of Lemma 5.20 by extension of scalars.

**Lemma 5.23 (Sylow subgroups).** If \(|D|=p^am\), with \(p\nmid m\), a finite group \(D\) has a subgroup of order \(p^a\), and every \(p\)-subgroup is contained in a conjugate of one of them.

**Proof.** Let \(D\) act by left translation on its subsets of cardinality \(p^a\). Their number \(\binom{p^am}{p^a}\) is not divisible by \(p\): modulo \(p\), the polynomial identity \((1+X)^{p^am}=(1+X^{p^a})^m\) makes that coefficient congruent to \(m\). Some orbit therefore has cardinality prime to \(p\). Its stabilizer \(P\) has order divisible by \(p^a\), by the orbit-stabilizer formula. On the stabilized subset, \(P\) acts freely by left translation, so \(|P|\) divides \(p^a\). Hence \(|P|=p^a\). Any \(p\)-subgroup \(Q\) acts on the cosets \(D/P\), whose number is prime to \(p\). Its nontrivial orbits have size divisible by \(p\), so some coset is fixed. That fixed coset gives \(Q\subseteq dPd^{-1}\). Both uses of the orbit formula follow by the bijection from the cosets of a point stabilizer to its orbit. \(\square\)

**Theorem 5.24 (rational induction at \(p\)).** For any finite group \(G\), there are a positive integer \(m\) prime to \(p\), subgroups \(B_i\) that are \(\mathbb Q_p\)-elementary at \(p\), integers \(n_i\), and virtual \(\mathbb Q_p[B_i]\)-characters \(\theta_i\), such that

\[
 m\,1_G=\sum_i n_i\operatorname{Ind}_{B_i}^G\theta_i.
\tag{5.64}
\]

**Proof: the character algebra.** Put \(n=|G|\), and let \(\Gamma=\operatorname{Gal}(\mathbb Q_p(\mu_n)/\mathbb Q_p)\), regarded as a subgroup of \((\mathbb Z/n\mathbb Z)^\times\). It acts on conjugacy classes by \([g]\mapsto[g^a]\). A \(\mathbb Q_p\)-character takes values in \(\mathbb Q_p\), is constant on these orbits, and has values in \(\mathbb Z_p\). The first two assertions follow by diagonalizing the finite-order matrix of \(g\): its eigenvalues are \(n\)th roots of unity, and applying a coefficient automorphism raises them to the same power \(a\). For integrality, choose a stable \(\mathbb Z_p\)-lattice as in Lemma 5.20 and take its matrix trace.

If \(k\) is the number of these orbits, the character evaluation map identifies

\[
 \mathbb Q_p\otimes_{\mathbb Z}\mathscr R_p(G)
                  \simeq\mathbb Q_p^k
\tag{5.65}
\]

as algebras, with multiplication on the right coordinatewise. We supply the spanning argument. For a cyclic subgroup \(C\), the simple \(\mathbb Q_p[C]\)-modules are the field factors of \(\mathbb Q_p[X]/(X^{|C|}-1)\); the polynomial has distinct roots. Their characters are the sums of the roots in each Galois orbit. Write \(s=|C|\). The Fourier transform of coefficients \((a_i)\) is \(f(j)=\sum_i a_i\zeta^{ij}\); its inverse is \(a_i=s^{-1}\sum_j f(j)\zeta^{-ij}\). If the \(a_i\) are in \(\mathbb Q_p\) and constant on Galois power orbits, the transform is constant on those orbits of \(j\), and its values are Galois-fixed, hence in \(\mathbb Q_p\). Conversely, if \(f\) has these properties, the inverse formula has Galois-fixed coefficients constant on the power orbits of \(i\). Thus the transform restricts to an isomorphism between the two \(\mathbb Q_p\)-spaces of orbit-constant vectors. Transforming the root-orbit indicator basis gives exactly the cyclic characters just described. These characters therefore span all \(\mathbb Q_p\)-valued functions on \(C\) constant on the same power orbits. Restriction of \(\Gamma\) to these roots is onto their full Galois group: the cyclotomic field for \(s\) is a Galois subfield of the one for \(n\), and every automorphism of that subfield extends to the larger Galois field, by the finite Galois correspondence used in Section 5.

On functions constant on the power orbits of \(G\), the bilinear pairing

\[
 \langle f,h\rangle_G=|G|^{-1}\sum_{g\in G}f(g)h(g^{-1})
\]

is nondegenerate: indicators of the orbits pair with the indicators of their inverse orbits with a nonzero rational weight. The coset formula for an induced character gives
\(\langle f,\operatorname{Ind}_C^G\eta\rangle_G
=\langle\operatorname{Res}_C^G f,\eta\rangle_C\), by reindexing the sum over cosets. If \(f\) is perpendicular to all characters induced from cyclic subgroups, their spanning property on each \(C\) makes \(f|_C=0\). Every group element lies in its cyclic subgroup, so \(f=0\). Hence the induced cyclic characters span the entire function space.

Finally the characters of distinct simple \(\mathbb Q_p[G]\)-modules are linearly independent over \(\mathbb Q_p\). To see this without a split-field assumption, the semisimple-algebra argument in Lemma 4.A before extension of scalars gives one central primitive idempotent for each simple type. On that simple module it acts as the identity, and on the others as zero; its traces distinguish the types in characteristic zero. A character relation on group elements is also a relation on the whole group algebra, so evaluate it on these idempotents. This proves independence and (5.65).

**Proof: maximal ideals modulo \(p\).** Let

\[
 \mathcal R=\mathbb Z_p\otimes_{\mathbb Z}\mathscr R_p(G).
\]

By (5.65), it is a finite free \(\mathbb Z_p\)-subalgebra of \(\mathbb Z_p^k\), containing the diagonal copy of \(\mathbb Z_p\). Every maximal ideal of \(\mathcal R\) is the kernel of character evaluation modulo \(p\) at some \(g\in G\). Here are the algebra details. First, \(p\mathcal R\) is in every maximal ideal, since the geometric series in \(px\) inverts \(1-px\). The ring \(\mathbb Z_p^k\) is finite over \(\mathcal R\), generated by its coordinate vectors, and is a faithful \(\mathcal R\)-module. For a maximal ideal \(M\subset\mathcal R\), its extension to \(\mathbb Z_p^k\) is proper. Otherwise the finite-generator adjugate argument applied to \(M\mathbb Z_p^k=\mathbb Z_p^k\) would give an element \(1+u\), with \(u\in M\), annihilating this faithful module, which would imply \(1\in M\). Thus the nonzero finite algebra \(\mathbb Z_p^k/M\mathbb Z_p^k\) has a maximal ideal. Its preimage is a maximal ideal of the product ring \(\mathbb Z_p^k\), hence the kernel of reducing one coordinate modulo \(p\). Its contraction contains \(M\), and equals \(M\) by maximality. These coordinates are exactly the power-orbit evaluations in (5.65).

One may take the evaluating element to have order prime to \(p\). Indeed write \(g=g_0g_1\) as commuting powers of \(g\), with \(g_0\) of prime-to-\(p\) order and \(g_1\) of \(p\)-power order, using the integer Chinese remainder theorem on its order. In a coefficient extension, roots of \(p\)-power order all reduce to one. Eigenvalue traces therefore give \(\chi(g)\equiv\chi(g_0)\pmod p\). Since both traces lie in \(\mathbb Z_p\), this is a congruence there too.

**Proof: an induced character nonzero at each such point.** Fix \(g\) of order \(s\) prime to \(p\), and put \(C=\langle g\rangle\). Write \(Z=C_G(g)\), \(N=N_G(C)\), and let \(A\subseteq(\mathbb Z/s\mathbb Z)^\times\) be the image of \(N\) on \(C\); its kernel is \(Z\). The earlier Cyclotomic fields, Theorem 12.3, identifies

\[
 L=\mathbb Q_p(\zeta_s),\qquad
 \operatorname{Gal}(L/\mathbb Q_p)=\langle p\rangle
            \subseteq(\mathbb Z/s\mathbb Z)^\times.
\]

This field is unramified; its residue contains a primitive \(s\)th root. Let \(A_0=A\cap\langle p\rangle\), and let \(N_0\) be its inverse image in \(N\). Choose a Sylow \(p\)-subgroup \(P\) of \(N_0\), by Lemma 5.23, and put \(B=CP\). Since \(C\) is normal and has prime-to-\(p\) order, \(C\cap P=1\) and \(B=C\rtimes P\). It satisfies the \(\mathbb Q_p\)-elementary condition by construction. Also

\[
 |P|=|Z|_p\,|A_0|_p,
\tag{5.66}
\]

where \(|D|_p\) is the largest \(p\)-power dividing \(|D|\); this follows from \(|N_0|=|Z|\,|A_0|\).

For \(0\leq j<s\), make the \(\mathbb Q_p\)-vector space \(L\) a representation \(V_j\) of \(B\). Let \(g\) act by multiplication by \(\zeta_s^j\), and let an element of \(P\) act by the field automorphism specified by its conjugation power on \(C\). These operations satisfy the semidirect product relations. The character at \(g^a\) is \(\operatorname{Tr}_{L/\mathbb Q_p}(\zeta_s^{ja})\). The induced character \(\xi_j\) on \(G\) consequently satisfies

\[
 \begin{aligned}
 \xi_j(g)
 &=\frac{|Z|}{s|P|}\sum_{a\in A}
                   \operatorname{Tr}_{L/\mathbb Q_p}(\zeta_s^{ja})\\
 &=\frac{|Z|\,|A_0|}{s|P|}
                     \sum_{d\in A\langle p\rangle}\zeta_s^{jd}.
 \end{aligned}
\tag{5.67}
\]

For the first equality, the induction coset trace is \(|B|^{-1}\) times the sum over elements \(x\in G\) with \(x^{-1}gx\in B\). A prime-to-\(p\) element of \(B\) has trivial image in the \(p\)-group \(B/C\), so lies in \(C\). It is a generator of \(C\), hence such \(x\) lies in \(N\). For each power \(a\in A\) there are exactly \(|Z|\) such elements, proving that equality. The trace is the sum over \(\langle p\rangle\), and each element of the product subgroup \(A\langle p\rangle\) is counted \(|A_0|\) times, proving the second.

The coefficient in the second line is a \(p\)-adic unit by (5.66). At least one of the sums in that line is nonzero modulo \(p\). In fact, over the residue field containing \(\bar\zeta_s\), they are the Fourier transforms, indexed by \(j\), of the nonzero indicator vector of \(A\langle p\rangle\) in \(\mathbb Z/s\mathbb Z\). The Fourier matrix is still invertible modulo \(p\), since \(p\nmid s\). Each sum is invariant under residue Frobenius, hence belongs to \(\mathbb F_p\). Thus some \(\xi_j(g)\) is a unit in \(\mathbb Z_p\). For \(s=1\), take \(C=1\), \(P\) a Sylow subgroup of \(G\), and \(\xi_0=\operatorname{Ind}_P^G1\); its value at the identity is \([G:P]\), also prime to \(p\). This handles every point.

**Proof: the integral identity.** Let \(\mathcal I\subset\mathscr R_p(G)\) be the subgroup generated by the inductions of virtual characters from all the specified elementary subgroups. The projection formula (5.61) makes it an ideal: multiplying an induced character by another character is induction of its restriction times the original character. The preceding construction shows that its scalar extension to \(\mathcal R\) is contained in no maximal ideal. A proper ideal in this finite \(\mathbb Z_p\)-algebra would be contained in a maximal ideal, so that scalar extension is all of \(\mathcal R\).

The abelian group \(\mathscr R_p(G)/\mathcal I\) is finitely generated. Its tensor product with \(\mathbb Z_p\) is zero, so it is finite of order prime to \(p\). To check this implication directly, integer row and column operations using the Euclidean algorithm diagonalize a finite presentation matrix: choose a nonzero entry of smallest positive size, divide other entries with remainder, and repeat until it divides all entries in its row and column; remove that diagonal entry and induct. The quotient is a sum of free cyclic groups and finite cyclic groups. A free cyclic group stays nonzero on tensoring with \(\mathbb Z_p\), and a finite cyclic group does so precisely when its order is divisible by \(p\). Therefore neither occurs here. The order \(m\) of the remaining finite quotient annihilates the class of \(1_G\), so \(m1_G\in\mathcal I\). Expanding the finite sum defining that membership gives (5.64). \(\square\)

### Integral semilinear descent and unramified norms

The elementary-group reduction uses an unramified coefficient field and a group action on an additional abelian group algebra. We establish the two integral facts needed for that reduction.

Let \(L/F\) be a finite unramified Galois extension of finite extensions of \(\mathbb Q_p\). Write \(S=\mathcal O_L\), \(R=\mathcal O_F\), \(\Delta=\operatorname{Gal}(L/F)\), and \(a=[L:F]\). A **semilinear** \(\Delta\)-action on an \(S\)-module \(M\) means additive maps with the group law and

\[
 \sigma(sm)=\sigma(s)\sigma(m)
                  \quad(s\in S,\ m\in M).
\]

**Lemma 5.25 (integral descent).** For every such module, the natural map

\[
 S\otimes_R M^\Delta\longrightarrow M,
                      \qquad s\otimes m\longmapsto sm
\tag{5.68}
\]

is an isomorphism. This is an integral statement, including when \(p\mid a\).

**Proof.** The integer ring \(S\) is finite free over the DVR \(R\), by the finite-normalization theorem of lesson one and its torsion-free basis argument. Unramifiedness and Three differents, Theorem 5.3, make its different the unit ideal. The trace-dual calculation in that lesson, or the norm-of-different discriminant identity in The different and the discriminant, Theorem 14.3, therefore makes its trace pairing perfect over \(R\).

Choose an \(R\)-basis \(e_1,\ldots,e_a\) of \(S\), with trace-dual basis \(f_1,\ldots,f_a\) in \(S\). The dual basis is integral because the inverse trace Gram matrix has entries in \(R\). We have

\[
 \sum_i e_i\sigma(f_i)=
 \begin{cases}
 1,&\sigma=1,\\
 0,&\sigma\ne1.
 \end{cases}
\tag{5.69}
\]

To verify this identity, form the embedding matrices \(E_{\sigma i}=\sigma(e_i)\) and \(Q_{\sigma i}=\sigma(f_i)\). The matrix \(E\) is invertible by the separable trace criterion in lesson three, and trace duality gives \(E^{\mathsf T}Q=1\). Hence \(Q^{\mathsf T}=E^{-1}\) and \(EQ^{\mathsf T}=1\). Its entry at the identity row and the \(\sigma\)-column is (5.69).

For \(m\in M\), set

\[
 m_i=\sum_{\sigma\in\Delta}\sigma(f_i m)\in M^\Delta,
 \qquad
 \Psi(m)=\sum_i e_i\otimes m_i.
\tag{5.70}
\]

Equation (5.69) makes the composite of \(\Psi\) with (5.68) equal to
\(\sum_\sigma(\sum_i e_i\sigma(f_i))\sigma(m)=m\). In the other direction, if \(u\in M^\Delta\), then

\[
 \Psi(su)=\sum_i e_i\otimes\operatorname{Tr}_{L/F}(f_i s)u
                 =s\otimes u,
\]

by trace duality. These computations prove that \(\Psi\) is the inverse and, in particular, that it is \(S\)-linear under the natural action on the tensor product. No finiteness or freeness assumption on \(M\) was needed. \(\square\)

**Lemma 5.26 (unramified unit norms).** The coefficient norm \(S^\times\to R^\times\) is onto. More generally, let \(A\) be a finite abelian \(p\)-group and let \(\Delta\) act on it by group automorphisms. Give the commutative algebra \(B=S[A]\) the diagonal action on coefficients and group elements. Then

\[
 \mathcal N_\Delta:B^\times\longrightarrow(B^\Delta)^\times,
                 \qquad x\longmapsto\prod_{\sigma\in\Delta}\sigma(x)
\tag{5.71}
\]

is onto. For the augmentation ideal \(I_B\), the same norm maps \(1+I_B\) onto \((1+I_B)^\Delta\).

**Proof: coefficient units.** Write \(k=R/\mathfrak m_R\), \(\ell=S/\mathfrak m_S\), and \(|k|=q\). Both are finite fields, and unramifiedness gives \(|\ell|=q^a\). Their Galois group is generated by the \(q\)-power Frobenius, with these \(a\) automorphisms; the finite-field normal-basis proof linked at the start of this lesson proves that classification as well.

The multiplicative group of a finite field is cyclic. Here is the root-count proof: in a finite abelian group, let \(M\) be the least common multiple of its element orders. For each prime dividing \(M\), choose an element whose order has the maximal power of that prime; take a power of it that has exactly that prime-power order. The product of these commuting elements has order \(M\), since their orders are pairwise coprime. Every nonzero field element is a root of \(X^M-1\), so the group size is at most \(M\), while the element just constructed makes it at least \(M\). Thus that element generates the entire group. The coprime-order assertion follows by raising a product to the respective complementary orders; Lagrange's divisibility follows from its coset partition.

The finite-field norm is \(z\mapsto z^{(q^a-1)/(q-1)}\), by multiplying its Frobenius conjugates. A generator of \(\ell^\times\) therefore maps to an element of order \(q-1\), proving surjectivity onto \(k^\times\). Choose a unit of \(S\) lifting a residue norm preimage of a target in \(R^\times\).

It remains to correct the norm by principal units. Let \(\pi\) be a uniformizer of \(R\), also one of \(S\). For \(u\in S\) and \(n\geq1\),

\[
 N_{L/F}(1+\pi^n u)
       \equiv1+\pi^n\operatorname{Tr}_{L/F}(u)
                                       \pmod{\pi^{n+1}S}.
\tag{5.72}
\]

Terms with at least two factors have valuation at least \(2n\). The congruence is over \(R\), since both sides are invariant and \(\pi^{n+1}S\cap R=\pi^{n+1}R\), as their valuations agree. The coefficient trace is onto by Theorem 2.1, applied to this unramified extension. Choose \(t\in S\) with trace one. At each step multiply the current lift by a unit \(1+\pi^ntr\) to correct the next residue coefficient of the norm error. The corrections converge in the complete DVR. Formula (5.72) and continuity of the finite product of conjugates make their limiting norm the prescribed target. This proves coefficient-unit surjectivity.

**Proof: group-algebra augmentation units.** The augmentation ideal of \(B\) tends to zero under its powers: the \(p\)-group nilpotence calculation in Theorem 5.5 gives \(I_B^N\subset pB\) for some \(N\). Thus \(1+I_B\) consists of units and is complete for this filtration. If an invariant error has the form \(1+y\), with \(y\in I_B^n\), choose \(z=ty\in I_B^n\). Semilinearity and invariance of \(y\) give

\[
 \sum_{\sigma\in\Delta}\sigma(z)=y,
 \qquad
 \prod_{\sigma\in\Delta}(1+\sigma(z))
                  \equiv1+y\pmod{I_B^{n+1}}.
\tag{5.73}
\]

The first formula uses \(\sum_\sigma\sigma(t)=1\); the second again uses \(2n\geq n+1\). Begin with a target in \((1+I_B)^\Delta\), correct its error in degrees \(n=1,2,\ldots\), and multiply the successive units \(1+z\). Their limit exists in \(1+I_B\), and its norm is the target, since the intersection of the powers of \(I_B\) is zero. This proves the last assertion.

For a target in \((B^\Delta)^\times\), its augmentation belongs to \(R^\times\). Choose a scalar coefficient unit whose coefficient norm is that augmentation, by the first part. Divide the target by the norm of this scalar. The remainder is invariant and augmentation-one, so the last assertion supplies its preimage. Restoring the scalar proves (5.71). The group action on \(A\) need not be trivial, and \(|\Delta|\) need not be invertible in \(R\). \(\square\)

### Determinants in an elementary crossed algebra

We now prove the integral algebra step behind the elementary-group reduction. It includes the matrix-algebra assertion used after abelianizing the kernel; that assertion needs a proof because its quotient group can have order divisible by \(p\) [Chinburg–Pappas–Taylor, Section 6.a].

Let \(L/\mathbb Q_p\) be finite unramified Galois, let \(S=\mathcal O_L\), and suppose a finite \(p\)-group \(P\) maps onto a subgroup \(\Delta\) of \(\operatorname{Gal}(L/\mathbb Q_p)\). Write \(H\) for the kernel, \(F=L^\Delta\), \(R=\mathcal O_F\) and \(a=|\Delta|\). The group \(\Delta\) is cyclic: its action on the finite residue field is faithful and identifies it with a subgroup of the cyclic Frobenius group, by Hilbert's ramification theory in Galois extensions, Theorem 6.2. The arithmetic Frobenius of \(L/\mathbb Q_p\) gives a lift of the \(p\)-power map on \(S/pS\). It commutes with \(\Delta\). Thus \(S\) satisfies the logarithm hypotheses used above.

Define the **crossed algebra**

\[
 D=S\circ P=\bigoplus_{g\in P}Sg,
                 \qquad gs=g(s)g.
\tag{5.74}
\]

The subgroup \(H\) acts trivially on the coefficients, so \(S[H]\) is its usual group-algebra subring. On \(\operatorname{Det}(S[H]^\times)\), an element of \(\Delta\) acts by coefficient conjugation and conjugation on \(H\), using any lift in \(P\). Different lifts differ by an inner conjugation from \(H\), which does not change determinants. This is therefore a well-defined action on determinant functions. It is also well defined on \(S[H^{\mathrm{ab}}]\) and on the conjugacy-class modules used for logarithms.

Choose representatives of \(P/H\). The right \(S[H]\)-module \(D\) is free of rank \(a\); left multiplication gives a restriction homomorphism on invertible matrices. We use \(\operatorname{Det}(\operatorname{GL}(D))\) to mean its characteristic-zero determinant functions on the simple representations of \(F\otimes_R D\), after passing to an algebraic closure. This algebra is semisimple, as the matrix-corner computation in the proof below shows. Write \(r\) for the restriction homomorphism on determinant functions.

**Theorem 5.27 (crossed-algebra determinants).** Restriction induces an isomorphism

\[
 r:\operatorname{Det}(\operatorname{GL}(D))
    =\operatorname{Det}(D^\times)
           \xrightarrow{\ \sim\ }
           \operatorname{Det}(S[H]^\times)^\Delta.
\tag{5.75}
\]

For an included unit \(x\in S[H]^\times\), its restriction is the determinant norm

\[
 r(\operatorname{Det}_D x)
                =\prod_{\sigma\in\Delta}\sigma(\operatorname{Det}x).
\tag{5.76}
\]

**Proof: restriction and injectivity.** In a coset basis, an included unit acts diagonally by its conjugates, giving (5.76). For a general invertible matrix over \(D\), change the coset basis by right multiplication by a lift of \(\sigma\). That operation is semilinear on the coefficient/group-algebra entries and commutes with left multiplication. Taking determinants makes its restriction invariant. Lemma 5.6 converts the resulting determinant of a matrix over \(S[H]\) into the determinant of a unit there.

To verify that restriction is well defined on determinant functions and injective, extend to an algebraically closed field \(U\) containing \(L\). The coefficient algebra \(U\otimes_F L\) is the product of \(a\) copies of \(U\), with primitive idempotents indexed by the embeddings of \(L/F\). The group \(P\) permutes those idempotents transitively, with stabilizer \(H\). Fix the identity-embedding idempotent \(e\), and representatives \(t_i\) of \(P/H\). Then

\[
 e\,(U\otimes_R D)\,e\simeq U[H],
 \qquad E_{ij}=t_i e t_j^{-1},
 \qquad E_{ij}E_{kl}=\delta_{jk}E_{il},
 \qquad \sum_i E_{ii}=1.
\tag{5.77}
\]

The corner assertion follows since a term \(ege\) vanishes unless \(g\in H\), and such terms give exactly the group basis of \(U[H]\). The matrix-unit products follow from orthogonality of the coefficient idempotents. Every element is recovered from its corner entries \(e t_i^{-1}x t_j e\), so these formulas give

\[
 U\otimes_R D\simeq M_a(U[H]).
\tag{5.78}
\]

The simple representations are consequently the column representations obtained from the simple \(U[H]\)-modules, by the matrix-unit argument of Lemma 4.A. On evaluating the restricted matrix at the identity coefficient embedding and one of those \(H\)-representations, one obtains exactly its column representation in (5.78). Its determinant is therefore the corresponding determinant over \(D\). Evaluation at the other embeddings gives the conjugate column representations. Thus all values of \(r\) depend only on the determinant over \(D\), and its values detect every such determinant. This proves well-definedness and injectivity, for stabilized matrices as well as units.

**Proof: the abelianized quotient.** Let \(J_S=\ker(S[H]\to S[H^{\mathrm{ab}}])\), and quotient \(D\) by the ideal it generates. This gives

\[
 \bar D=S\circ(P/[H,H]),\qquad
 B=S[H^{\mathrm{ab}}]\subset\bar D.
\]

The subgroup \([H,H]\) is normal in \(P\). Choose a lift \(\gamma\in P\) of a generator of \(\Delta\). In \(\bar D\), put \(h_0=\gamma^a\in H^{\mathrm{ab}}\). Conjugation by \(\gamma\) acts on the commutative ring \(B\), with order dividing \(a\), and restricts to the generator on \(S\). It fixes \(h_0\). Lemma 5.26 supplies \(b\in B^\times\) with

\[
 \prod_{\sigma\in\Delta}\sigma(b)=h_0^{-1}.
\]

Set \(w=b\gamma\). Then \(w^a=1\), and conjugation by \(w\) is the same action on \(B\). Hence

\[
 \bar D\simeq B\rtimes\Delta.
\tag{5.79}
\]

Lemma 5.25 gives \(B\simeq S\otimes_R B_0\), where \(B_0=B^\Delta\). Thus an \(R\)-basis \((e_i)\) of \(S\) is a \(B_0\)-basis of \(B\). Multiplication by \(B\) and the semilinear action of \(\Delta\) give the explicit isomorphism

\[
 B\rtimes\Delta\xrightarrow{\ \sim\ }
           \operatorname{End}_{B_0}(B)\simeq M_a(B_0).
\tag{5.80}
\]

Here is a direct proof, including its inverse. For \(T\in\operatorname{End}_{B_0}(B)\), the element mapping to it is

\[
 \sum_{\sigma\in\Delta}
       \Bigl(\sum_i T(e_i)\sigma(f_i)\Bigr)\sigma,
\tag{5.81}
\]

where \((f_i)\) is the integral trace-dual basis in Lemma 5.25. Indeed \(x=\sum_i e_i\operatorname{Tr}_\Delta(f_i x)\) for \(x\in B\), by the descended tensor description. Expanding that trace proves that (5.81) acts as \(T\). Conversely, for an operator \(\sum_\tau b_\tau\tau\), formula (5.81) recovers \(b_\sigma\), since \(\sum_i\tau(e_i)\sigma(f_i)=\delta_{\tau\sigma}\) by (5.69). This proves the isomorphism integrally.

Restriction from \(\bar D\) to its right \(B\)-module sends a unit to its ordinary matrix determinant in \(B_0^\times\), included in \(B^\times\). To verify this last identification, the perfect trace pairing gives

\[
 \operatorname{End}_{B_0}(B)
       \simeq B\otimes_{B_0}B,\qquad
 u\otimes v\longmapsto(x\mapsto u\operatorname{Tr}_\Delta(vx)).
\]

Right multiplication by an element of \(B\) acts on the second factor; left composition by an endomorphism acts on the first. In the basis \((e_i)\) of that first factor, its restriction matrix therefore has precisely the entries of the endomorphism's \(B_0\)-matrix. Taking the commutative determinant proves the assertion. Every \(v\in B_0^\times\) occurs, by the matrix \(\operatorname{diag}(v,1,\ldots,1)\) in (5.80).

**Proof: lifting and the commutator part.** The ideal used to pass from \(D\) to \(\bar D\) is topologically nilpotent. The ideal \(J_S\) is preserved by all lifts in \(P\), and \(J_S^N\subseteq pS[H]\) for some \(N\), since it lies in the augmentation ideal of the \(p\)-group \(H\). Its generated ideal in \(D\) consequently has \(N\)th power contained in \(pD\). As in the unit-lifting argument of Theorem 5.16, geometric series therefore lift every unit of \(\bar D\) to a unit of \(D\).

Now let \(d\in\operatorname{Det}(S[H]^\times)^\Delta\). Its image on abelianization is \(v\in B_0^\times\), by (5.43). Choose a unit of \(\bar D\) with restriction determinant \(v\), as just proved, and lift it to \(x\in D^\times\). Then

\[
 d\,r(\operatorname{Det}_D x)^{-1}
                 \in\operatorname{Det}(1+J_S)^\Delta.
\tag{5.82}
\]

It remains to show that every determinant in this last group is the restriction of an included unit of \(S[H]\).

The isomorphism \(\nu_S:\operatorname{Det}(1+J_S)\simeq p\phi(J_S)\) of Theorem 5.16 commutes with this \(\Delta\)-action. The coefficient Frobenius commutes with \(\Delta\), and conjugation on \(H\) commutes with taking \(p\)th powers. Inner conjugations act trivially on both determinants and conjugacy classes, so the choice of lifts is immaterial. Thus the logarithm formula proves equivariance.

Choose \(t\in S\) with coefficient trace one, by Theorem 2.1. If \(y\in p\phi(J_S)^\Delta\), then the semilinear action gives \(\sum_\sigma\sigma(ty)=y\). Theorem 5.16 supplies \(u\in1+J_S\) with logarithm \(ty\). Equivariance and (5.76) give

\[
 \nu_S\bigl(r(\operatorname{Det}_D u)\bigr)
        =\sum_{\sigma\in\Delta}\sigma(\nu_S(\operatorname{Det}u))
        =y.
\]

Injectivity of \(\nu_S\) shows that this realizes every target determinant in (5.82). Restore the lifted unit \(x\). Restriction is now onto the entire invariant determinant group using units of \(D\). Its already proved injectivity on determinant functions proves both the isomorphism in (5.75) and the equality of the matrix and unit determinant images. \(\square\)

### Unramified descent for elementary groups

An unramified coefficient extension can split a coefficient field into several factors. We include those factors and their permutations in the descent argument.

**Lemma 5.28 (unramified tensor factors).** If \(E,L\) are finite unramified Galois extensions of \(\mathbb Q_p\), then

\[
 T=\mathcal O_E\otimes_{\mathbb Z_p}\mathcal O_L
                       =\prod_i\mathcal O_{K_i},
\tag{5.83}
\]

where every \(K_i\) is a finite unramified Galois extension of \(\mathbb Q_p\). The coefficient group \(\Xi=\operatorname{Gal}(E/\mathbb Q_p)\) acts transitively on these factors. For the stabilizer \(\Xi_i\) of a factor,

\[
 (\mathcal O_{K_i})^{\Xi_i}=\mathcal O_L.
\tag{5.84}
\]

On the right, use the embedding of \(\mathcal O_L\) in that factor. For any finite \(p\)-group \(H\),

\[
 \operatorname{Det}(T[H]^\times)^\Xi
                    =\operatorname{Det}(\mathcal O_L[H]^\times).
\tag{5.85}
\]

The right side is embedded diagonally through the coefficient embeddings in (5.83).

**Proof.** The ring \(T\) is finite free and complete over \(\mathbb Z_p\). Its reduction modulo \(p\) is a tensor product of finite fields over \(\mathbb F_p\). Write one finite field as \(\mathbb F_p[X]/(f)\), with \(f\) irreducible and separable; finite-field separability follows from the Frobenius classification in the earlier normal-basis proof. Factoring \(f\) over the other finite field and applying polynomial Chinese remainders expresses this tensor product as a product of finite fields. The orthogonal idempotents lift to \(T\) by the complete-ring idempotent iteration of Lemma 4.B. Because the ring here is commutative, they stay orthogonal and sum to one: equivalently lift successively in the complementary summands. This gives factors \(T_i\), each with residue a field.

Every such factor is a DVR with uniformizer \(p\). It is finite free over \(\mathbb Z_p\), since it is a direct summand of \(T\). An element with nonzero residue is a unit, by lifting its residue inverse and using the geometric series for the error in \(pT_i\). Every nonzero element has the form \(p^n u\) with \(u\) a unit: \(p\)-adic separation excludes infinite divisibility. A product of two such elements is nonzero because multiplication by \(p\) is injective. Every nonzero ideal is a power of \(p\), by choosing an element with least valuation in it. Finally a fraction of negative valuation cannot satisfy a monic integral equation: its highest power would be the unique term of least valuation. This proves integral closedness. Its fraction field \(K_i\) is a finite extension of \(\mathbb Q_p\), and its residue degree equals its field degree, by reduction of its free \(\mathbb Z_p\)-basis. Thus it is unramified, and \(T_i=\mathcal O_{K_i}\) by integral closedness and the finite-normalization theorem.

For completeness these \(K_i\) are Galois. If the residue degree is \(b>1\), choose a primitive element of the cyclic residue unit group of order \(p^b-1\), whose cyclicity was proved in Lemma 5.26. Lift it to a root \(\zeta\) of \(X^{p^b-1}-1\) using the simple-root lifting proof in Three differents, Lemma 5.1. Its order is exactly \(p^b-1\), since its residue has that order. The prime-to-\(p\) cyclotomic local-degree formula in Cyclotomic fields, Theorem 12.3, gives \([\mathbb Q_p(\zeta):\mathbb Q_p]=b\): the order of \(p\) modulo \(p^b-1\) is \(b\), as a smaller positive exponent would make the smaller positive integer \(p^j-1\) divisible by \(p^b-1\). Hence \(K_i=\mathbb Q_p(\zeta)\), which is Galois. If \(b=1\), its degree is one and the assertion is immediate.

The fixed ring \(T^\Xi\) is \(\mathcal O_L\). To see this directly, use a \(\mathbb Z_p\)-basis of \(\mathcal O_L\) and write the coefficients in \(\mathcal O_E\); invariance puts every coefficient in \(\mathcal O_E^\Xi=\mathbb Z_p\). If there were more than one orbit of factors, the sum of the idempotents in one orbit would be a nontrivial idempotent in this fixed domain. Thus \(\Xi\) is transitive. A \(\Xi_i\)-fixed element in one factor extends uniquely to a \(\Xi\)-fixed tuple by moving it through the orbit. Conversely an invariant tuple is determined by that factor. This proves (5.84).

Determinants of a product of coefficient rings are the product of their determinant groups, by evaluating each factor. An invariant determinant tuple is determined by a \(\Xi_i\)-invariant determinant in one factor. Apply Theorem 5.17 to \(\mathcal O_L\subset\mathcal O_{K_i}\): the fixed coefficient ring is (5.84), both rings have the Frobenius lifts of their unramified fields, and \(H\) is a \(p\)-group. The determinant therefore descends to \(\mathcal O_L[H]\). Moving it through the factor orbit gives exactly (5.85). \(\square\)

**Theorem 5.29 (elementary determinant descent).** Let \(B=C\rtimes P\) be \(\mathbb Q_p\)-elementary at \(p\), in the precise sense of Theorem 5.24. If \(E/\mathbb Q_p\) is finite unramified Galois, with integer ring \(\mathcal O_E\) and coefficient group \(\Xi\), then

\[
 \operatorname{Det}(\mathcal O_E[B]^\times)^\Xi
                     =\operatorname{Det}(\mathbb Z_p[B]^\times).
\tag{5.86}
\]

**Proof: the cyclic coefficient factors.** Put \(s=|C|\). The commutative algebra \(\mathbb Z_p[C]\) is \(\mathbb Z_p[X]/(X^s-1)\). Its rational field factors are \(L=\mathbb Q_p(\zeta_d)\), one for each Galois orbit of roots of order \(d\mid s\). Since \(p\nmid s\), each is unramified by Theorem 12.3 of the cyclotomic lesson. Its integral factor is \(\mathcal O_L\). Here is the integral check: a minimal polynomial of a root has integral coefficients, because its roots are integral and its coefficients lie in \(\mathbb Q_p\). Its reduction is the irreducible residue Frobenius-orbit polynomial, with distinct roots. Different root orbits give coprime reductions. The Chinese remainder decomposition over \(\mathbb Z_p\) follows by lifting the idempotents, or by lifting a residue Bezout relation and removing its \(p\)-adic error with a geometric series in the finite algebra. Each individual factor has field residue and principal maximal ideal \(p\), so the DVR argument of Lemma 5.28 identifies it with the full integer ring of its field.

By the elementary hypothesis, conjugation by \(P\) raises these roots to powers from their local Galois group. Thus it preserves each rational and integral factor. Consequently

\[
 \mathbb Z_p[B]=\prod_{L}\bigl(\mathcal O_L\circ P\bigr).
\tag{5.87}
\]

For one factor, write \(A\) for the image of \(P\) on \(L\), and \(H\) for its kernel. Then \(A\) is cyclic and Theorem 5.27 gives

\[
 \operatorname{Det}((\mathcal O_L\circ P)^\times)
                  \simeq\operatorname{Det}(\mathcal O_L[H]^\times)^A.
\tag{5.88}
\]

**Proof: after coefficient extension.** The corresponding factor over \(\mathcal O_E\) is \(T\circ P\), with \(T=\mathcal O_E\otimes\mathcal O_L\) as in (5.83). The group \(P\) may permute the factors of \(T\); its kernel \(H\) fixes them all. We claim that restriction gives

\[
 \operatorname{Det}((T\circ P)^\times)
                  \simeq\operatorname{Det}(T[H]^\times)^A.
\tag{5.89}
\]

To prove the claim, handle one \(P\)-orbit of factors at a time. Choose its idempotent \(e\), coefficient DVR \(T_i\), stabilizer \(P_i\subseteq P\), and coset representatives \(t_j\) of \(P/P_i\). The integral elements \(t_j e t_k^{-1}\) are matrix units exactly as in (5.77), now for the lifted coefficient idempotents. The corner is \(T_i\circ P_i\), so the orbit algebra is

\[
 M_{[P:P_i]}(T_i\circ P_i).
\tag{5.90}
\]

The action of \(P_i\) on \(T_i\) has kernel exactly \(H\): the embedding of \(L\) in its fraction field is injective, so an automorphism trivial on \(T_i\) is trivial on \(L\). The fraction field is unramified Galois over \(\mathbb Q_p\) by Lemma 5.28. Theorem 5.27 applies to this corner. It identifies its determinant group with \(\operatorname{Det}(T_i[H]^\times)^{P_i/H}\).

Taking a full matrix algebra does not change this determinant group: its simple modules are the column modules over each corner simple, as proved with matrix units in Lemma 4.A. A stabilized matrix over the corner has the same determinant values; every needed corner unit occurs as \(\operatorname{diag}(u,1,\ldots,1)\) in the full matrix algebra. Thus the equality of unit and matrix determinant images in Theorem 5.27 also holds for (5.90).

An \(A\)-invariant determinant tuple on the factor orbit is uniquely determined by a \(P_i/H\)-invariant determinant on \(T_i[H]\), because the orbit is transitive. Under the right-module restriction to \(T[H]\), evaluation at this coefficient factor gives exactly the corner restriction: after passing to a splitting field it is the column representation from (5.90), followed by the column representation from (5.78), each occurring once. The other coefficient factors give its conjugates. Apply this argument at every embedding of the coefficient center into the splitting field; it detects all the simple determinant values. Hence restriction is injective and has precisely this invariant-tuple image, proving (5.89). This argument also shows that the claim is natural for automorphisms of the coefficient ring that commute with the \(P\)-action.

The coefficient action of \(\Xi\) on \(T\) commutes with \(A\): one acts on the \(E\)-factor and the other on the \(L\)-factor and on \(H\) by conjugation. Taking \(\Xi\)-fixed points in (5.89), Lemma 5.28 gives

\[
 \begin{aligned}
 \operatorname{Det}((T\circ P)^\times)^\Xi
 &\simeq
       \bigl(\operatorname{Det}(T[H]^\times)^\Xi\bigr)^A\\
 &=\operatorname{Det}(\mathcal O_L[H]^\times)^A\\
 &\simeq\operatorname{Det}((\mathcal O_L\circ P)^\times).
 \end{aligned}
\]

The outer isomorphisms are restriction, (5.89) and (5.88), so their naturality identifies the result with the original coefficient inclusion. Finally take the product over all the factors in (5.87). This proves (5.86). \(\square\)

**Corollary 5.30 (the remaining general-group quotient).** For any finite group \(G\), the abelian quotient

\[
 \frac{\operatorname{Det}(\mathcal O_E[G]^\times)^\Xi}
      {\operatorname{Det}(\mathbb Z_p[G]^\times)}
\tag{5.91}
\]

is killed by an integer prime to \(p\).

**Proof.** Use the identity (5.64). Each subgroup determinant descends by Theorem 5.29, and Corollary 5.22 therefore puts the corresponding prime-to-\(p\) power of any numerator element in the denominator. This proves the stated assertion. To conclude that the quotient is zero, its \(p\)-primary nature still needs to be proved; (5.91) alone does not finish general-group descent. \(\square\)

### Residue algebras and the Cartan matrix

To finish general-group determinant descent we must control what a characteristic-zero determinant remembers after reduction. The following residue facts supply that control. The Cartan assertion proved here is its finite \(p\)-primary cokernel, rather than the sharper exponent statement in [Lam, Chapter 4, Section 3, Theorem 3.3].

**Lemma 5.31 (finite division rings).** Every finite division ring is a field.

**Proof.** If there is a counterexample, choose one \(D\) with least cardinality. Its center is a finite field \(\mathbb F_q\), and \(|D|=q^n\) with \(n>1\). For a noncentral element \(x\), its centralizer in \(D\) is a proper division subring, hence a commutative finite field by minimality. It contains the center and has cardinality \(q^{m_x}\), where \(m_x\) is a proper divisor of \(n\): regard \(D\) as a left vector space over that field and multiply dimensions over \(\mathbb F_q\).

The conjugacy-class equation for \(D^\times\) is consequently

\[
 q^n-1=q-1+
       \sum_x\frac{q^n-1}{q^{m_x}-1},
\tag{5.92}
\]

with one representative for each noncentral conjugacy class. The cyclotomic polynomial \(\Phi_n(X)\), integral and monic by Cyclotomic fields, Theorem 12.1, divides \(X^n-1\) and every quotient \((X^n-1)/(X^{m_x}-1)\), since \(m_x\mid n\) and \(m_x<n\). Thus the positive integer \(\Phi_n(q)\) divides \(q-1\), by (5.92). But

\[
 \Phi_n(q)=\prod_{\zeta\text{ primitive of order }n}|q-\zeta|
                                                     >q-1.
\]

Each factor is strictly larger than \(q-1\), because \(\zeta\ne1\); conjugate factors pair to positive real numbers, with \(q+1\) for the possible root \(-1\). There is at least one factor, and the product is larger than \((q-1)^{\varphi(n)}\geq q-1\), including \(q=2\). This contradiction proves the lemma. \(\square\)

Let \(k\) be a finite field of characteristic \(p\) large enough that \(k[G]\) is split in the sense of Lemma 4.A and contains every root of unity of order dividing the prime-to-\(p\) part \(n_0\) of \(|G|\). Such a finite field exists by that lemma and the finite-field extensions used in the normal-basis theorem. Let \(S_1,\ldots,S_t\) be its simple modules. For each \(i\), choose an idempotent \(e_i\) lifting a matrix unit \(E_{11}\) in the corresponding factor of \(k[G]/J(k[G])\), and put \(P_i=k[G]e_i\). Idempotents lift across the nilpotent radical by the iteration in Lemma 4.B, which terminates when the error's power vanishes. The top of \(P_i\) is \(S_i\), and

\[
 \dim_k\operatorname{Hom}_{k[G]}(P_i,S_j)=\delta_{ij}.
\tag{5.93}
\]

Indeed Hom is evaluation at \(e_i\), giving \(e_iS_j\), whose dimension is the corresponding matrix-unit rank. The modules \(P_i\) are projective. Every finite projective is a direct sum of these with the multiplicities in its top: lift the isomorphism of top modules using projectivity of the proposed direct sum, kill the cokernel by nilpotence of the radical, split the resulting surjection, and kill its kernel by the same top-module argument. This is precisely the projective-top argument proved in Lemma 4.A. Formula (5.93) makes the multiplicities unique.

Define the **Cartan matrix** by

\[
 C_{ij}=[P_j:S_i],
\tag{5.94}
\]

where the brackets denote the composition multiplicity. The Cartan map sends a projective to its module class, from the free abelian group on \(P_i\) to the free abelian group \(G_0(k[G])\) on \(S_i\), so its matrix is \(C\). Increasing the finite splitting field leaves this matrix unchanged. In fact the nilpotent radical extends to the radical after such field extension, because its quotient extends to a product of split matrix algebras. Every \(S_i\) stays simple, and every \(P_i\) has that same simple top; extending a composition series preserves its multiplicities.

**Theorem 5.32 (the Cartan cokernel at \(p\)).** The cokernel of the Cartan map is a finite abelian \(p\)-group. In particular

\[
 |\det C|=p^b\quad\text{for some integer }b\geq0.
\tag{5.95}
\]

**Proof: character coordinates.** For each \(S_i\), its lifted character \(\varphi_i\) on \(p\)-regular elements is the sum of the multiplicative lifts of its eigenvalues, as defined and proved additive in Lemma 4.C. Its values are integral combinations of \(n_0\)th roots of unity. That lemma proves that these characters are linearly independent in characteristic zero and that the characters induced from cyclic prime-to-\(p\) subgroups span every class function supported on the regular classes. Those induced characters agree on regular elements with the lifted characters of their reductions, by its integral eigenprojector proof. Their reductions are sums of the simple module classes. Hence \((\varphi_i)\) form a basis for all functions on the \(p\)-regular conjugacy classes; in particular the number of those classes is \(t\), and their square character table is invertible.

Choose an auxiliary prime \(q\ne p\), and a complete DVR \(O\) in a finite extension of \(\mathbb Q_q\) containing the \(n_0\)th roots of unity, with uniformizer \(\lambda\). View the same finite sums of roots defining \(\varphi_i\) in this field. The table remains invertible: its determinant is a nonzero element of the cyclotomic number field, and a field embedding into a \(q\)-adic field cannot make that element zero. Thus character evaluation embeds

\[
 \mathcal R=O\otimes_{\mathbb Z}G_0(k[G])\subseteq O^t,
 \qquad
 \operatorname{Frac}(O)\otimes_O\mathcal R
                     \simeq\operatorname{Frac}(O)^t.
\tag{5.96}
\]

Multiplication is coordinatewise because eigenvalue lifts multiply under tensor products on regular elements. This makes \(\mathcal R\) an algebra, containing the diagonal copy of \(O\). The finite faithful \(\mathcal R\)-module \(O^t\) and the finite-generator adjugate argument in the proof of Theorem 5.24 show that every maximal ideal of \(\mathcal R\) is reduction of one character coordinate modulo \(\lambda\). The same proof applies word for word with \(O,\lambda\) in place of \(\mathbb Z_p,p\): \(1-\lambda x\) is invertible by its series, and the maximal ideals of the product of DVRs are its residue-coordinate kernels.

For this residue evaluation, its regular element \(g\) may also be taken of order prime to \(q\). Split its order into its \(q\)-power and prime-to-\(q\) parts, as commuting powers \(g=g_0g_1\). Since \(g\) was \(p\)-regular, so is \(g_0\). Roots of \(q\)-power order reduce to one in characteristic \(q\), so the eigenvalue sums give \(\varphi_i(g)\equiv\varphi_i(g_0)\pmod\lambda\). Thus every maximal ideal is evaluation at an element of order prime to both \(p\) and \(q\).

**Proof: a projective character nonzero at each coordinate.** Fix such an element \(g\), of order \(s>1\). Put \(Z=C_G(g)\), \(N=N_G(\langle g\rangle)\), and let \(A\subseteq(\mathbb Z/s\mathbb Z)^\times\) be the image of \(N\) on \(\langle g\rangle\), with kernel \(Z\). Choose a Sylow \(q\)-subgroup \(Q\) of \(N\), and let \(A_q\) be its image in \(A\), and \(K\) its kernel. Then

\[
 |Q\cap Z|=|Z|_q,
 \qquad |A_q|=|A|_q,
 \qquad |Q|=|Z|_q|A_q|.
\tag{5.97}
\]

For the first equality, conjugate a Sylow \(q\)-subgroup of the normal subgroup \(Z\) into \(Q\), using Lemma 5.23; its conjugate is still in \(Z\). The reverse size inequality is automatic. The two remaining equalities follow by the kernel and image orders and \(|N|=|Z|\,|A|\).

The subgroup \(B=\langle g\rangle Q\) is a semidirect product and has order \(s|Q|\), prime to \(p\). Its subgroup \(\langle g\rangle K\) is the direct product \(\langle g\rangle\times K\), because \(K\) centralizes \(g\). For \(0\leq j<s\), let \(\theta_j\) be the character of the \(k[B]\)-module induced from the one-dimensional module on this direct product that sends \(g\) to the \(j\)th power of a primitive \(s\)th root and \(K\) to one. These roots belong to \(k\) by its choice. On \(g^u\), its lifted character is

\[
 \theta_j(g^u)=\sum_{a\in A_q}\zeta_s^{jua},
\]

as follows from the coset basis of \(Q/K\). Inducing further to \(G\) gives, by the same coset count as (5.67),

\[
 (\operatorname{Ind}_B^G\theta_j)(g)
      =\frac{|Z|\,|A_q|}{s|Q|}
                     \sum_{a\in A}\zeta_s^{ja}.
\tag{5.98}
\]

The prefactor is a \(q\)-adic unit by (5.97). Because \(q\nmid s\), the Fourier matrix on \(\mathbb Z/s\mathbb Z\) stays invertible in the residue field of \(O\). The indicator vector of \(A\) is nonzero, so at least one of its transforms \(\sum_{a\in A}\bar\zeta_s^{ja}\) is nonzero. Thus at least one character in (5.98) avoids the chosen maximal ideal. If \(g=1\), use \(B=Q\), a Sylow \(q\)-subgroup of \(G\), and its trivial module: the induced character value at one is \([G:Q]\), a \(q\)-adic unit.

All the modules just constructed are projective. Their inducing group \(B\) has order prime to \(p\), so Higman's criterion, Theorem 3.1 over \(k\), with the endomorphism \(|B|^{-1}\) times the identity, proves that every finite \(k[B]\)-module is projective. Induction preserves projectivity because \(k[G]\otimes_{k[B]}-\) preserves a direct summand of a finite free module.

**Proof: the cokernel.** The Cartan image is an ideal of \(G_0(k[G])\). Indeed a projective tensored over \(k\) with any finite module, with diagonal action, is projective: tensor its free-module splitting and use the explicit untwisting (5.57), whose proof works in every characteristic. The identity (5.61) also works in every characteristic and describes the induction used above. Thus the scalar-extended Cartan ideal in \(\mathcal R\) is contained in no maximal ideal, by (5.98). It equals \(\mathcal R\), so the Cartan cokernel tensor \(O\) is zero. The ring \(O\) is finite free over \(\mathbb Z_q\), and hence this also makes its tensor \(\mathbb Z_q\) zero: a free \(\mathbb Z_q\)-basis of \(O\) makes that further tensor a nonzero direct sum unless the former tensor is zero.

This holds for every \(q\ne p\). The Cartan cokernel is a finitely generated abelian group. The elementary-divisor argument at the end of Theorem 5.24 shows that it has no free part and no primary torsion at any prime other than \(p\). It is therefore a finite \(p\)-group. The same diagonalization of the square presentation matrix \(C\) identifies its order with \(|\det C|\), proving (5.95). \(\square\)

### General determinant descent over unramified and tame coefficients

We can now finish the fixed-point theorem needed in Taylor's argument. The two parts are complementary: Corollary 5.30 gives a prime-to-\(p\) annihilator, while the residue calculation below makes the remaining quotient a pro-\(p\) group.

**Lemma 5.33 (decomposition and Cartan matrices).** Choose a characteristic-zero complete DVR \(V\), finite over \(\mathbb Z_p\), whose fraction field splits \(G\), and whose finite residue field \(k\) satisfies the splitting and root hypotheses preceding Theorem 5.32. For each fraction-field simple character \(\chi\), choose a stable \(V\)-lattice and write

\[
 d_{\chi i}=[\bar M_\chi:S_i],\qquad D=(d_{\chi i}).
\]

These multiplicities are independent of the lattice, and

\[
 C=D^{\mathsf T}D.
\tag{5.99}
\]

If \(x\in V[G]^\times\), and \(u_i\in k^\times\) is its determinant on the residue simple \(S_i\), then

\[
 \overline{\operatorname{Det}(x)(\chi)}
                       =\prod_i u_i^{d_{\chi i}}.
\tag{5.100}
\]

In particular, a unit with every characteristic-zero determinant equal to one has every residue simple determinant equal to one.

**Proof.** Such coefficient rings exist: start with a finite unramified ring having the desired residue field, as constructed in Lemma 5.28, then apply the finite splitting-extension argument of Lemma 4.A to the fraction group algebra and the complete-DVR extension argument of Lemma 4.B. Increasing a residue splitting field leaves \(C\) unchanged, as proved before Theorem 5.32. We can similarly enlarge the fraction field to contain every prime-to-\(p\) root needed for the eigenprojectors of Lemma 4.C.

Lift each \(e_i\in k[G]\) to an idempotent \(\tilde e_i\in V[G]\). The iteration of Lemma 4.B works here as well: its error, \(\tilde e_i^2-\tilde e_i\), commutes with \(\tilde e_i\) and with the inverse of \(2\tilde e_i-1\), so the same polynomial calculation squares the error at each step. The geometric series supplies that inverse and completeness supplies the limit. Put \(\tilde P_i=V[G]\tilde e_i\); its reduction is \(P_i\).

For any stable lattice \(M\),

\[
 \operatorname{Hom}_{V[G]}(\tilde P_i,M)
                       \simeq\tilde e_iM.
\]

The last module is a direct summand of the free \(V\)-module \(M\), so is free; its fraction rank equals the dimension of its reduction \(e_i\bar M\). The latter equals \([\bar M:S_i]\): the Hom functor for the projective \(P_i\) is exact, and (5.93) computes its dimension on every simple factor. Apply this to a lattice \(M_\chi\) in a fraction-field simple. Its fraction Hom dimension is the multiplicity of that simple in the semisimple fraction module of \(\tilde P_i\), since the splitting field makes the simple endomorphism ring its scalar field. Therefore that multiplicity is \(d_{\chi i}\), and depends only on the fraction module, proving lattice independence.

The fraction character of \(\tilde P_j\) is consequently \(\sum_\chi d_{\chi j}\chi\). On \(p\)-regular elements, the eigenprojector proof in Lemma 4.C identifies the character of a lattice with the lifted character of its reduction. Hence, using \(\varphi_i\) for the residue lifted simple characters,

\[
 \sum_i C_{ij}\varphi_i
      =\sum_\chi d_{\chi j}\chi\big|_{\mathrm{regular}}
      =\sum_i\Bigl(\sum_\chi d_{\chi j}d_{\chi i}\Bigr)\varphi_i.
\]

Their independence proves (5.99).

The matrix of \(x\) on the reduction of \(M_\chi\) preserves a composition series of that \(k[G]\)-module. Its determinant is the product of its determinants on the successive simple quotients: in an adapted basis its matrix is block upper triangular. This proves (5.100).

If the fraction determinants are all one, (5.100) gives \(\prod_i u_i^{d_{\chi i}}=1\) for every \(\chi\). Combining these equations with the transpose matrix gives \(\prod_i u_i^{C_{ji}}=1\) for every \(j\), by (5.99). The integer adjugate of \(C\) then gives \(u_i^{\det C}=1\) for every \(i\). Theorem 5.32 makes \(|\det C|\) a power of \(p\), and a field of characteristic \(p\) has no nonidentity \(p\)-power root of one, since \(X^{p^b}-1=(X-1)^{p^b}\). Thus every \(u_i=1\). \(\square\)

**Lemma 5.34 (residue determinants and their kernel).** Let \(V\) be the integer ring of any finite extension of \(\mathbb Q_p\), with residue field \(k\). Put \(A=V[G]\), and let \(K\) be the inverse image in \(A\) of the radical of \(k[G]\). There is a well-defined surjective homomorphism

\[
 \mathrm{red}:\operatorname{Det}(A^\times)
       \longrightarrow\operatorname{Det}((k[G]/J(k[G]))^\times),
\tag{5.101}
\]

where residue determinants are evaluated on the absolutely simple residue modules. Its kernel is

\[
 \ker(\mathrm{red})=\operatorname{Det}(1+K),
\tag{5.102}
\]

a compact abelian pro-\(p\) group. All these groups and maps are natural for coefficient automorphisms.

**Proof: well-definedness and surjectivity.** Enlarge \(V\) to the splitting DVR of Lemma 5.33, using Lemma 4.B. The splitting residue matrix \(C\) has the property just proved. If two units of \(A\) have the same fraction determinant function, their quotient has fraction determinant one; Lemma 5.33 makes all of its residue simple determinants one. Therefore their residue determinants agree, and the map is well defined. Passing to the larger residue field detects all absolutely simple values, so this proves the assertion for the original \(k\) as well.

The finite residue algebra has nilpotent radical. The finite-algebra proof of Lemma 4.A before scalar extension expresses its semisimple quotient as a product of full matrix algebras over finite division rings. Lemma 5.31 makes those division rings finite fields; thus

\[
 k[G]/J(k[G])\simeq\prod_j M_{r_j}(k_j).
\tag{5.103}
\]

On each factor, its simple determinant values are the embeddings of the ordinary determinant in \(k_j^\times\). Every value in \(k_j^\times\) occurs, by a diagonal matrix with that entry and all other entries one. A unit in this quotient lifts to \(k[G]\), since the radical is nilpotent, and further to \(A\), since \(K^N\subseteq\pi A\) for some \(N\), where \(\pi\) is a uniformizer of \(V\). The geometric-series inverse removes the two errors of a lifted inverse. This proves surjectivity of (5.101).

**Proof: its kernel.** A unit with trivial residue determinants has image in \(\prod_j\operatorname{SL}_{r_j}(k_j)\). Each special linear group over a field is generated by off-diagonal elementary matrices. To verify this, Gaussian elimination uses row additions and the determinant-one interchange

\[
 w(a)=
 \begin{pmatrix}1&a\\0&1\end{pmatrix}
 \begin{pmatrix}1&0\\-a^{-1}&1\end{pmatrix}
 \begin{pmatrix}1&a\\0&1\end{pmatrix}
 =\begin{pmatrix}0&a\\-a^{-1}&0\end{pmatrix}.
\]

After elimination one has a diagonal matrix of determinant one. Its diagonal pairs are elementary too, because \(w(a)w(-1)=\operatorname{diag}(a,a^{-1})\). Multiplying such pairs expresses any determinant-one diagonal; for a one-dimensional factor the special linear group is already trivial.

Lift the complete orthogonal system of diagonal matrix idempotents in (5.103) to \(A\). The idempotent iteration used in Lemma 5.33 applies to errors in \(K\), because their successive squared powers tend to zero. Lift them successively in the complementary corner \((1-e)A(1-e)\); take the last idempotent as the complementary remainder. Thus the lifted idempotents are exactly orthogonal and sum to one. An off-diagonal residue entry lifts to an element \(z\in e_iAe_j\), with \(i\ne j\), and \(z^2=0\). The unit \(1+z\) has every fraction determinant equal to one: its image in any representation is the identity plus a square-zero matrix, whose eigenvalues are all one. These units lift the elementary matrix generators. Multiply the original unit by their inverses to remove its semisimple residue image. Its determinant has not changed, and its resulting representative lies in \(1+K\). Conversely those units have trivial semisimple residue image. This proves (5.102).

Finally \(1+K\) is a pro-\(p\) group. The filtration \(1+K^n\) has successive quotients the additive groups \(K^n/K^{n+1}\), because multiplication is addition modulo \(K^{n+1}\). Each is finite and killed by \(\pi\), hence a finite \(p\)-group. The inclusions \(K^N\subseteq\pi A\) and \(\pi A\subseteq K\) make this topology the complete separated \(\pi\)-adic topology, so \(1+K\) is the inverse limit of its finite \(p\)-group quotients. Fraction determinants are continuous functions into a finite product of unit groups of a splitting coefficient field. Their image is compact and hence closed; quotienting by their closed kernel makes this image pro-\(p\). It is abelian because determinants multiply. The constructions use coefficient reduction, radicals, module representations and determinant evaluation, all of which commute with coefficient automorphisms. \(\square\)

**Theorem 5.35 (general unramified determinant descent).** For a finite unramified Galois extension \(E/\mathbb Q_p\), with coefficient group \(\Xi\), and any finite group \(G\),

\[
 \operatorname{Det}(\mathcal O_E[G]^\times)^\Xi
                      =\operatorname{Det}(\mathbb Z_p[G]^\times).
\tag{5.104}
\]

**Proof.** Let \(\ell/\mathbb F_p\) be the residue extension. Its Galois group is \(\Xi\), by unramifiedness and the residue Frobenius calculation in Theorem 6.2 of the earlier ramification lesson. Write \(Q=\mathbb F_p[G]/J(\mathbb F_p[G])\). Field extension gives

\[
 \ell[G]/J(\ell[G])\simeq\ell\otimes_{\mathbb F_p}Q.
\tag{5.105}
\]

Indeed the extended radical is nilpotent, and its quotient is semisimple: use (5.103), and observe that a tensor product of finite fields is a product of finite fields, by the separable-polynomial Chinese remainder proof in Lemma 5.28. Hence that extended ideal is exactly the radical, by the characterization in Lemma 4.A.

If \(Q=\prod_jM_{r_j}(k_j)\), its residue determinant unit group is \(\prod_j k_j^\times\), and the extended one is \(\prod_j(\ell\otimes_{\mathbb F_p}k_j)^\times\). Taking coefficient invariants gives

\[
 \operatorname{Det}((\ell\otimes Q)^\times)^\Xi
                              =\operatorname{Det}(Q^\times).
\tag{5.106}
\]

To check this equality, expand in an \(\mathbb F_p\)-basis of each \(k_j\): an invariant tensor has all its \(\ell\)-coefficients in \(\mathbb F_p\). If it is a unit, its inverse is invariant too. This gives precisely \(k_j^\times\), component by component; the matrix determinant interpretation in (5.103) gives (5.106).

Let \(d\) be an invariant fraction determinant over \(\mathcal O_E[G]\). By Lemma 5.34 its residue determinant is invariant, so (5.106) makes it a residue determinant over \(\mathbb F_p\). Lift a corresponding residue unit to \(x\in\mathbb Z_p[G]^\times\), as in that lemma. Then \(d\operatorname{Det}(x)^{-1}\) is invariant and belongs to the pro-\(p\) residue kernel.

All determinant images here are compact and closed, being images of the unit groups of finite complete coefficient algebras. Thus the quotient (5.91) is a compact abelian group and is the continuous image of the closed invariant subgroup of that pro-\(p\) kernel. It is therefore pro-\(p\). Corollary 5.30 also kills it by an integer \(m\) prime to \(p\). On an abelian pro-\(p\) group, raising to \(m\) is an automorphism: it is an automorphism on every finite \(p\)-group quotient, with compatible inverses in their inverse limit. A group killed by such an automorphism is trivial. This proves (5.104). \(\square\)

**Theorem 5.36 (general tame determinant descent).** If \(E/\mathbb Q_p\) is finite tame Galois with coefficient group \(\Delta\), then for every finite group \(G\),

\[
 \operatorname{Det}(\mathcal O_E[G]^\times)^\Delta
                     =\operatorname{Det}(\mathbb Z_p[G]^\times).
\tag{5.107}
\]

No condition on \(|G|\) is needed.

**Proof: inertia and its unramified fixed field.** Write \(S=\mathcal O_E\), and let \(I\) be the kernel of the action on its finite residue field, of cardinality \(p^f\). The fixed field \(F=E^I\) is unramified, and \(|I|=e(E/\mathbb Q_p)\). We give the local argument. Lift a primitive residue root of order \(p^f-1\) by the simple-root Hensel proof in Lemma 5.1 of Three differents. For \(f=1\), simply take \(F_0=\mathbb Q_p\); otherwise the lifted root \(\zeta\) generates an unramified field \(F_0=\mathbb Q_p(\zeta)\) of degree \(f\), by the cyclotomic local-degree formula used in Lemma 5.28. Its residue field is the entire residue field of \(E\). Uniqueness of that simple-root lift makes inertia fix \(\zeta\), so \(I\) fixes \(F_0\). Conversely an automorphism fixing \(F_0\) fixes every residue, since the residue fields coincide. Thus \(I=\operatorname{Gal}(E/F_0)\) and \(F=F_0\), by finite Galois correspondence. If \(pS=\lambda^eS\), the successive maximal-ideal quotients of \(S/pS\) each have \(\mathbb F_p\)-dimension \(f\), while its dimension is \([E:\mathbb Q_p]\) by a free integral basis. Therefore \([E:\mathbb Q_p]=ef\), so \(|I|=e\). Tameness makes \(e\) prime to \(p\).

**Proof: inertia invariants.** Put \(R_F=\mathcal O_F\). It maps onto the residue field of \(S\). If \(x\in S[G]^\times\), its reduction modulo \(\lambda\) is a unit in the residue group algebra. Lift that unit and its inverse to \(R_F[G]\); their errors lie in \(pR_F[G]\), so geometric series give a unit lift \(y\in R_F[G]^\times\). Consequently \(xy^{-1}\in1+\lambda S[G]\), and

\[
 \operatorname{Det}(S[G]^\times)
   =\operatorname{Det}(R_F[G]^\times)
                      \operatorname{Det}(1+\lambda S[G]).
\tag{5.108}
\]

The second factor \(H_1\) is compact abelian pro-\(p\), by the additive filtration of powers of \(\lambda\), or the last argument of Lemma 5.34. Given an \(I\)-invariant determinant, use (5.108) to divide it by a determinant over \(R_F\). The remaining \(h\in H_1\) is still \(I\)-invariant.

Restriction along the finite free coefficient extension \(S/R_F\) gives a norm determinant over \(R_F[G]\). Explicitly take the matrix of left multiplication by a representing unit on the right \(R_F[G]\)-module \(S[G]\). Lemma 5.6 makes its determinant the determinant of a unit over \(R_F[G]\). Extending to a splitting field decomposes the coefficient field into its \(I\)-conjugates exactly as in the proof of Lemma 5.18; thus its determinant is \(\prod_{\sigma\in I}\sigma(h)=h^e\). This construction requires no Frobenius lift on the ramified ring. We obtain

\[
 h^e\in H_1\cap\operatorname{Det}(R_F[G]^\times).
\]

The intersection is a closed subgroup of the pro-\(p\) group \(H_1\), hence is pro-\(p\) too. Raising to the prime-to-\(p\) integer \(e\) is an automorphism on both groups. The intersection therefore contains an \(e\)th root of \(h^e\); uniqueness of that root in \(H_1\) makes it \(h\) itself. Restoring the divided determinant proves

\[
 \operatorname{Det}(S[G]^\times)^I
                          =\operatorname{Det}(R_F[G]^\times).
\]

Finally \(\Delta/I\) is \(\operatorname{Gal}(F/\mathbb Q_p)\). Apply the already proved unramified descent theorem, Theorem 5.35, to this last fixed group. This proves (5.107). \(\square\)

Theorem 5.36 supplies the fixed-point theorem used in [Taylor, Section 12, Theorem 6], with every residue, induction, logarithm and norm ingredient proved above. Its role in the root-number identity is to descend an invariant determinant once the local arithmetic comparison has produced it over tame coefficients.

### Finite Gauss sums and the symplectic signs

We next supply two arithmetic inputs for the class comparison: the finite Gauss identities, and the Galois invariance of the signs assigned to symplectic characters. Compare [Taylor, Sections 8–9] and the freely readable [Fröhlich, Section 8]. Throughout the finite-field calculations, \(k=\mathbb F_q\), \(q=p^f\), and \(\psi:k\to\mathbb C^\times\) is a nontrivial additive character. A multiplicative character \(\chi:k^\times\to\mathbb C^\times\), including the trivial character, is extended by \(\chi(0)=0\). Thus the extension of the trivial character is not the constant function on \(k\). Write
\[
 g_k(\chi,\psi)=\sum_{x\in k^\times}\chi(x)\psi(x).
 \tag{5.109}
\]

**Lemma 5.37 (Fourier calculation, units and Galois action).** The trivial multiplicative character has Gauss sum \(-1\). If \(\chi\ne1\), then
\[
 g_k(\chi,\psi)g_k(\chi^{-1},\psi)=\chi(-1)q,
 \qquad |g_k(\chi,\psi)|^2=q.
 \tag{5.110}
\]
Every Gauss sum is an algebraic integer and is a unit at every finite place of residue characteristic different from \(p\). If \(\psi_a(x)=\psi(ax)\), with \(a\in k^\times\), then
\[
 g_k(\chi,\psi_a)=\chi(a)^{-1}g_k(\chi,\psi).
 \tag{5.111}
\]
For \(\sigma\in\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)\), choose \(a_\sigma\in\mathbb F_p^\times\) by \(\sigma(\zeta_p)=\zeta_p^{a_\sigma}\). With \(\chi^\sigma(x)=\sigma(\chi(x))\),
\[
 \sigma(g_k(\chi,\psi))
 =\chi^\sigma(a_\sigma)^{-1}g_k(\chi^\sigma,\psi).
 \tag{5.112}
\]

**Proof.** A nontrivial character of a finite abelian group sums to zero: translation by an element on which it is not one multiplies its sum by a different scalar. This proves both \(\sum_{x\in k}\psi(x)=0\) and \(\sum_{x\in k^\times}\chi(x)=0\) for nontrivial \(\chi\), and gives \(g_k(1,\psi)=-1\).

For \(\chi\ne1\), write \(x=ty\) in the product on the left of (5.110). It becomes
\[
 \sum_{t\in k^\times}\chi(t)
       \sum_{y\in k^\times}\psi((t+1)y).
\]
The inner sum is \(q-1\) at \(t=-1\), and \(-1\) otherwise. The outer character sum is zero, so this expression is \(q\chi(-1)\). Conjugating the defining sum and changing \(x\) to \(-x\) gives
\(\overline{g_k(\chi,\psi)}=\chi(-1)^{-1}g_k(\chi^{-1},\psi)\); here \(\chi(-1)=\pm1\). This proves the absolute-value assertion.

The summands in (5.109) are roots of unity, hence algebraic integers. At a place not dividing \(p\), (5.110) expresses their product as a unit. Both factors are integral there, so both are units; the trivial case was already computed. Substitution \(y=ax\) proves (5.111). Additive values are \(p\)-th roots of unity, and \(\psi(x)^{a_\sigma}=\psi(a_\sigma x)\). Apply \(\sigma\) termwise to (5.109) and then use (5.111) to obtain (5.112). \(\square\)

**Lemma 5.38 (Jacobi sums and the quadratic product identity).** Define
\[
 J(\chi,\lambda)=\sum_{x\in k}\chi(x)\lambda(1-x).
\]
If \(\chi\lambda\ne1\), then
\[
 g_k(\chi,\psi)g_k(\lambda,\psi)
   =J(\chi,\lambda)g_k(\chi\lambda,\psi).
 \tag{5.113}
\]
If \(\chi\ne1\), then \(J(\chi,\chi^{-1})=-\chi(-1)\). When \(q\) is odd, let \(\eta\) be the nontrivial quadratic character. For every \(\chi\), including \(1\) and \(\eta\),
\[
 g_k(\chi,\psi)g_k(\chi\eta,\psi)
   =\chi(4)^{-1}g_k(\chi^2,\psi)g_k(\eta,\psi).
 \tag{5.114}
\]

**Proof.** In the product of the two Gauss sums, first collect the terms with \(x+y=t\). For \(t\ne0\), put \(x=tu\), \(y=t(1-u)\). Their sum is \((\chi\lambda)(t)J(\chi,\lambda)\psi(t)\). The terms with \(t=0\) sum to \(\lambda(-1)\sum_{x\ne0}(\chi\lambda)(x)=0\) under the stated hypothesis. This proves (5.113), also when exactly one of its characters is trivial. For the inverse-character formula, \(x\mapsto x/(1-x)\) is a bijection from \(k\setminus\{0,1\}\) to \(k^\times\setminus\{-1\}\). The character sum on the latter set is \(-\chi(-1)\).

The multiplicative group of a finite field is cyclic, as proved in Lemma 5.26. Consequently each \(t\in k\) has \(1+\eta(t)\) square roots, with the convention \(\eta(0)=0\). If \(\chi\ne1\), substitution \(y=2x-1\) therefore gives
\[
\begin{aligned}
 J(\chi,\chi)
 &=\chi(4)^{-1}\sum_{y\in k}\chi(1-y^2)\\
 &=\chi(4)^{-1}\sum_{t\in k}(1+\eta(t))\chi(1-t)\\
 &=\chi(4)^{-1}J(\eta,\chi).
\end{aligned}
\]
For \(\chi\notin\{1,\eta\}\), both \(\chi^2\) and \(\chi\eta\) are nontrivial. Apply (5.113) to \((\chi,\chi)\) and \((\chi,\eta)\), and cancel the nonzero Gauss sums using Lemma 5.37. This yields (5.114). For \(\chi=1\), both sides are \(-g_k(\eta,\psi)\). For \(\chi=\eta\), the same equality holds because \(\eta(4)=1\). These are all the excluded cases, so the identity is proved for every character. \(\square\)

**Theorem 5.39 (norm lifting of a Gauss sum).** Let \(k_r=\mathbb F_{q^r}\),
\(\chi_r=\chi\circ N_{k_r/k}\), and \(\psi_r=\psi\circ\operatorname{Tr}_{k_r/k}\). Then
\[
 g_{k_r}(\chi_r,\psi_r)=(-1)^{r-1}g_k(\chi,\psi)^r
 \qquad(r\geq1).
 \tag{5.115}
\]
In particular this formula includes the trivial multiplicative character. The trace character remains nontrivial even when \(p\mid r\).

**Proof.** The finite-field trace is the polynomial
\(x+x^q+\cdots+x^{q^{r-1}}\). It is a nonzero polynomial of degree less than \(q^r\), so it is not zero on all of \(k_r\). Its values lie in \(k\), and it is \(k\)-linear; its nonzero image is thus all of \(k\). This proves the last assertion without replacing trace by multiplication by \(r\).

For a monic polynomial
\(f(X)=X^n+c_1X^{n-1}+\cdots+c_n\) with \(c_n\ne0\), set
\[
 a(f)=\chi((-1)^n c_n)\psi(-c_1),\qquad a(1)=1.
\]
Products of constant terms and sums of the next-to-leading coefficients show that \(a(fh)=a(f)a(h)\). Form the formal power series over a field of characteristic zero containing the character values,
\[
 L(T)=\sum_{\substack{f\text{ monic}\\f(0)\ne0}}a(f)T^{\deg f}.
\]
Its coefficient of \(T\) is \(g_k(\chi,\psi)\), by writing \(f=X-x\). Every coefficient of degree \(n\geq2\) is zero: \(c_1\) and \(c_n\ne0\) are independent, and summing over \(c_1\) gives zero. This applies also to the trivial \(\chi\). Hence
\[
 L(T)=1+g_k(\chi,\psi)T.
 \tag{5.116}
\]
Unique factorization of polynomials, obtained by Euclidean division, gives the formal Euler product
\[
 L(T)=\prod_{\substack{P\text{ monic irreducible}\\P\ne X}}
          (1-a(P)T^{\deg P})^{-1}.
\]
Each coefficient involves finitely many factors, so this identity and its formal logarithm require no analytic convergence. To justify the finite-field orbit facts used next, the roots of \(X^{q^r}-X\) in an algebraic closure form a field: Frobenius respects addition, multiplication and inverses. The derivative is \(-1\), so there are exactly \(q^r\) distinct roots. The Frobenius orbit of a root of an irreducible polynomial has length equal to its degree: its orbit polynomial has coefficients fixed by Frobenius, hence in \(k\), and irreducibility makes that orbit polynomial the minimal polynomial. It lies in this field of \(q^r\) elements exactly when that length divides \(r\). For a generator of a separable degree-\(d\) extension, the Vandermonde evaluation matrix diagonalizes its multiplication matrix with entries the \(d\) conjugate roots. Its determinant and trace are therefore their product and sum. For an element of a subfield, use a basis of the larger field over that subfield; its multiplication matrix repeats the smaller-field matrix on the diagonal. These facts prove the norm and trace formulas used below. If \(P\) has degree \(d\) and root \(\alpha\in\mathbb F_{q^d}\), then
\[
 a(P)=\chi(N_{\mathbb F_{q^d}/k}\alpha)
          \psi(\operatorname{Tr}_{\mathbb F_{q^d}/k}\alpha).
\]
For \(d\mid r\), its \(d\) distinct roots lie in \(k_r\), and each has weight \(a(P)^{r/d}\) in the lifted sum. Indeed norm raises its smaller-field norm to \(r/d\), and trace multiplies its smaller-field trace by \(r/d\). The roots of \(X^{q^r}-X\) are distinct; a Frobenius orbit belongs to them exactly when its length divides \(r\). It follows that the coefficient of \(T^r\) in the Euler-product logarithm is
\[
 \frac1r\sum_{d\mid r}d\sum_{\deg P=d}a(P)^{r/d}
   =\frac1r g_{k_r}(\chi_r,\psi_r).
\]
On the other hand, the logarithm of (5.116) has this coefficient equal to
\((-1)^{r-1}g_k(\chi,\psi)^r/r\). Equating the coefficients proves (5.115). \(\square\)

For example, take \(k=\mathbb F_3\), \(\psi(x)=\zeta_3^x\), and its quadratic character \(\eta\). Then
\(g_k(\eta,\psi)=\zeta_3-\zeta_3^2\), whose square is \(-3\). Its lift to \(\mathbb F_9\) has Gauss sum \(3\), by (5.115). The minus sign in the lifting formula is essential in this example.

We now turn from finite sums to Artin root numbers. The local constants used below have the exact earlier proofs in Local L-factors and epsilon factors, Theorem 3.0 and Sections 3A–3D. In particular their existence includes the relation check between Brauer decompositions. That lesson's Lemma 2.1 proves the rank-one finite Gauss formula and Fourier inversion; Theorems 4.1 and 5.1 prove the exponent, additive-character change and duality identities. We use these particular proved results, rather than defining a higher-dimensional constant by an unchecked character decomposition.

**Lemma 5.40 (alternating forms and tame conductor parity).** Suppose a characteristic-zero representation \(V\) of a finite group preserves a nondegenerate alternating bilinear form. Then \(\dim V\) is even, \(V\simeq V^\vee\), and \(\det V=1\). For every subgroup \(H\), the restriction of the form to \(V^H\) is nondegenerate. Consequently, for a tame finite-image local Galois representation of this type,
\[
 a_F(V)=\dim V-\dim V^I\quad\text{is even},
 \tag{5.117}
\]
where \(I\) is inertia. At a real place the multiplicity of \(-1\) for complex conjugation is even. Galois conjugation of the character preserves symplectic type and all these dimensions.

**Proof.** An alternating nondegenerate form has a symplectic basis: choose \(v,w\) with pairing one, split off their two-dimensional plane by subtracting its two pairing coordinates, and repeat on its orthogonal complement. This proves even dimension. The pairing map \(V\to V^\vee\) is an equivariant isomorphism. If \(\dim V=2m\), the \(m\)-fold exterior product of the alternating form is a nonzero invariant element of \(\bigwedge^{2m}V^\vee\), by that basis calculation. Its invariance forces determinant one.

The averaging projection \(P_H=|H|^{-1}\sum_{h\in H}h\) onto \(V^H\) is self-adjoint for the form: moving each \(h\) across the pairing replaces it by \(h^{-1}\), which permutes the sum. Thus \(\ker P_H\) is orthogonal to \(V^H\), and a vector in \(V^H\) orthogonal to \(V^H\) is orthogonal to all of \(V\). It is zero. Apply the even-dimensional conclusion to \(V^I\). The local conductor formula, proved in Artin L-functions, conductors and discriminants, Section 3, equation (9), reduces in the tame case to (5.117): all higher inertia groups are trivial. For an involution its two eigenspaces are orthogonal and nondegenerate, so the negative eigenspace is even-dimensional too.

Representations of a finite group may be realized over \(\overline{\mathbb Q}\). Indeed its group algebra there is semisimple by averaging; a finite-dimensional division algebra over an algebraically closed field is that field, since an eigenvalue of multiplication makes every element scalar. Its simple matrix factors therefore supply all irreducibles, and scalar extension supplies the complex ones. This is also the decomposition used in Lemma 4.A. If an invariant nondegenerate alternating form exists over \(\mathbb C\), the space of invariant alternating matrices is the solution of linear equations over \(\overline{\mathbb Q}\). Its determinant polynomial is not identically zero, so a solution over that infinite field has nonzero determinant. Apply \(\sigma\) to its matrices to obtain the form for \(V^\sigma\). Ranks of the averaging projections are unchanged by \(\sigma\). The stated type and dimension invariance follows. \(\square\)

**Lemma 5.41 (algebraic covariance of a local constant).** Let \(F/\mathbb Q_p\) be finite, and give \(F\) the additive character
\(\psi_F=\psi_{\mathbb Q_p}\circ\operatorname{Tr}_{F/\mathbb Q_p}\), where
\(\psi_{\mathbb Q_p}(x)=\exp(2\pi i\{x\}_p)\) and \(\{x\}_p\) is the rational fractional part with denominator a power of \(p\). Normalize additive Haar measure \(dx_0\) by \(\operatorname{vol}(\mathcal O_F)=1\). For a finite-image representation \(V\), the constant \(\epsilon_F(0,V,\psi_F,dx_0)\) is algebraic. If \(\sigma\in\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)\) and \(\psi_F^\sigma(x)=\sigma(\psi_F(x))\), then
\[
 \sigma\bigl(\epsilon_F(0,V,\psi_F,dx_0)\bigr)
 =\epsilon_F(0,V^\sigma,\psi_F^\sigma,dx_0).
 \tag{5.118}
\]
There is \(u_\sigma\in\mathbb Z_p^\times\) such that
\(\psi_F^\sigma(x)=\psi_F(u_\sigma x)\).

**Proof.** For a character, the provider's equations (9) and (9A), with unit volume, express the constant as a finite sum of roots of unity times an integral power of \(q_F\) and a character value. Every factor is algebraic; applying \(\sigma\) gives precisely the same formula for the conjugated character and additive character. This argument applies also over each finite extension of \(F\), with its trace additive character and unit volume.

The dimension-zero character induction proved in that provider's equation (10) writes
\[
 V-(\dim V)1=\sum_j m_j\operatorname{Ind}_{H_j}^G(\chi_j-1)
\]
inside a finite quotient \(G\), with \(\chi_j\) one-dimensional. The proved rank-zero induction axiom expresses its constant as
\[
 \epsilon_F(0,1,\psi_F,dx_0)^{\dim V}
 \prod_j\left(
   \frac{\epsilon_{E_j}(0,\chi_j,\psi_F\operatorname{Tr}_{E_j/F},dx_{E_j,0})}
        {\epsilon_{E_j}(0,1,\psi_F\operatorname{Tr}_{E_j/F},dx_{E_j,0})}
          \right)^{m_j}.
\]
The quotients have virtual dimension zero, so choosing unit volume over \(E_j\) is legitimate. Apply the character calculation to every term. Conjugating the same representation identity gives the constant for \(V^\sigma\); trace commutes with the scalar \(\sigma\) on character values. This proves algebraicity and (5.118).

On the group of \(p^r\)-th roots, \(\sigma\) raises roots to a unit power \(u_r\) modulo \(p^r\). Compatibility of these actions gives \(u_\sigma\in\mathbb Z_p^\times\). The character \(\psi_{\mathbb Q_p}\) has kernel \(\mathbb Z_p\); at a fractional part of denominator \(p^r\), multiplication by \(u_\sigma\) has exactly that unit-power action. Hence \(\sigma\psi_{\mathbb Q_p}(x)=\psi_{\mathbb Q_p}(u_\sigma x)\). Taking trace proves the assertion over \(F\). \(\square\)

**Theorem 5.42 (the tame symplectic sign homomorphism).** Let \(L/K\) be a tame finite Galois extension of number fields with group \(G\). For a symplectic character \(\chi\), its global Artin root number satisfies
\[
 W_K(\chi)\in\{1,-1\},\qquad
 W_K(\chi^\sigma)=W_K(\chi)
 \quad\bigl(\sigma\in\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)\bigr).
 \tag{5.119}
\]
Its relative conductor is the square of an integral ideal. Define \(w:R_G\to\{1,-1\}\) on the irreducible-character basis by
\[
 w(\chi)=
 \begin{cases}
 W_K(\chi),&\chi\text{ irreducible and symplectic},\\
 1,&\chi\text{ irreducible and not symplectic},
 \end{cases}
 \tag{5.120}
\]
and extend multiplicatively under character addition. Then \(w\) is a Galois-equivariant homomorphism and \(w^2=1\).

**Proof.** A finite-image complex representation is unitary: average a positive definite Hermitian form over its finite image. For a symplectic representation, Lemma 5.40 gives self-duality and determinant one. The provider's duality equation (16), evaluated at \(s=1/2\) with a self-dual measure, gives
\(W_F(V,\psi)W_F(V^\vee,\psi)=\det V(-1)=1\).
Self-duality therefore gives \(W_F(V,\psi)^2=1\). The proved absolute-value statement ensures the usual unitary normalization, and the additive-character scaling formula (14) shows that this sign is independent of \(\psi\), since its determinant is one.

At a finite place put \(d=\dim V\), \(a=a_F(V)\), and \(n=n_F(\psi_F)\). The provider's Fourier inversion gives self-dual integral-ring volume \(q_F^{-n/2}\); its exponent and measure formulas consequently give
\[
 W_F(V,\psi_F)
 =\epsilon_F(0,V,\psi_F,dx_0)q_F^{-a/2-nd}.
 \tag{5.121}
\]
The tame conductor \(a\) is even by Lemma 5.40. Thus the normalizing factor in (5.121) is rational and is fixed by every \(\sigma\). The same lemma preserves \(a\) and \(d\) under conjugation. Apply Lemma 5.41 and then the additive-character formula with \(u_\sigma\): its absolute value is one and its determinant value is one. This proves
\(\sigma(W_F(V))=W_F(V^\sigma)\). The left side equals \(W_F(V)\), a rational sign. Hence every finite local sign is constant on a Galois orbit.

At a real place the finite-image representation factors through complex conjugation. With the positive exponential additive character, the provider's Section 3D gives phase \(i^{d^-}\), where \(d^-\) is the negative-eigenspace dimension. Lemma 5.40 makes this an even exponent, so it is a rational sign preserved by conjugation. Reversing the additive character has no effect because the determinant is one. At a complex place the finite Galois representation is trivial and the phase is one.

The global functional equation is proved in Artin L-functions, conductors and discriminants, Theorem 21.3. Its Section 8, the deduction through equation (43), proves for every finite-image representation that the global constant is the product of these local central constants. That argument supplies the permutation induction constants and the integer Brauer reduction. Multiplying the local signs proves (5.119). At every finite prime the relative conductor exponent is the even integer in (5.117), so its ideal is a square.

Irreducible characters form a free integral basis of \(R_G\), and Galois conjugation permutes them and preserves symplectic type by Lemma 5.40. Thus (5.120) extends uniquely to a homomorphism, and (5.119) proves equivariance on every basis element. Its values are signs, so its square is one. This constructs the sign homomorphism; identifying its locally free class and proving the equality with \(c(\mathcal O_L)\) still requires the determinant class description and the local resolvent comparison. \(\square\)

### Resolvent frames and their real signatures

The gluing construction in Theorem 5.10 can be applied directly to the integer ring. We now compute the determinants of its transition matrices and their real signs. These are the resolvent and signature steps in [Fröhlich, Sections 1 and 8]; both steps are proved below. We keep left modules and the row-vector convention of Theorem 5.10.

Let \(L/K\) be finite Galois with group \(G\), and fix a normal basis generator \(a\in L\). Its existence has the exact earlier proof in Hilbert 90 in Noether's form and Galois descent, Theorem 4.0. For any \(b\in L\) define
\[
 \mathcal R(b)=\sum_{g\in G}g(b)g^{-1}\in L[G].
 \tag{5.122}
\]
For a character \(\chi\), represented over \(\overline{\mathbb Q}\) by \(\rho_\chi\), its resolvent is
\[
 r_\chi(b)=\det\rho_\chi(\mathcal R(b)).
 \tag{5.123}
\]
The coefficients and matrices are evaluated in one common algebraic closure. Changing the representation by an isomorphism conjugates the matrix, so its determinant depends only on \(\chi\). Direct sums make the determinant multiplicative under character addition. When \(b\) is a normal basis generator it is nonzero, and therefore extends to virtual characters by taking quotients.

**Lemma 5.43 (the resolvent frame and its transformation laws).** The element \(\mathcal R(a)\) is a unit in \(L[G]\). For \(\lambda=\sum_h\lambda_hh\in K[G]\), acting on \(L\) in the usual way,
\[
 \mathcal R(\lambda a)=\lambda\mathcal R(a),\qquad
 r_\chi(\lambda a)=\operatorname{Det}(\lambda)(\chi)r_\chi(a).
 \tag{5.124}
\]
The second formula uses \(\lambda\in K[G]^\times\). If \(\gamma\in\operatorname{Gal}(\overline{\mathbb Q}/K)\) restricts to \(s\in G\), then
\[
 \gamma(\mathcal R(a))=\mathcal R(a)s,
 \qquad
 \gamma(r_\chi(a))=r_{\chi^\gamma}(a)\det\rho_{\chi^\gamma}(s).
 \tag{5.125}
\]

**Proof.** The conjugates \(h(a)\) are a \(K\)-basis of \(L\). The evaluation map
\[
 L\otimes_K L\longrightarrow\prod_{t\in G}L,
 \qquad x\otimes y\longmapsto(x\,t(y))_t
\]
is an isomorphism. To check this without assuming descent, choose a separable primitive element \(\theta\) of \(L/K\): its distinct conjugates give a Vandermonde matrix on \(1,\theta,\ldots,\theta^{|G|-1}\), with nonzero determinant. Thus evaluation is an isomorphism on that basis and hence on any basis. The primitive-element proof is the earlier Algebraic integers and rings of integers, Section 1; equivalently the full field normal-basis proof just cited supplies this separable extension setup. In particular the matrix \((t(h(a)))_{t,h}\) is invertible.

Right multiplication by \(\mathcal R(a)\), on the group basis of \(L[G]\), has entry \(k^{-1}h(a)\) in row \(k\), column \(h\): the equation \(hg^{-1}=k\) is \(g=k^{-1}h\). Its matrix is the evaluation matrix with the rows reindexed. It is therefore invertible. A bijective right multiplication in a finite-dimensional algebra means the element is a unit: its inverse image of 1 is a left inverse, and injectivity makes that inverse a right inverse too. Applying \(\rho_\chi\) shows \(r_\chi(a)\ne0\).

In \(\mathcal R(\lambda a)\), the coefficient sum is \(\sum_{g,h}\lambda_hgh(a)g^{-1}\), since \(\lambda_h\in K\). Put \(u=gh\), so \(g^{-1}=hu^{-1}\). This sum is \(\lambda\mathcal R(a)\), proving (5.124). Likewise putting \(u=sg\) in \(\sum_gsg(a)g^{-1}\) gives \(\mathcal R(a)s\). Apply \(\gamma\) also to the representation matrices; they represent \(\chi^\gamma\). Taking determinants proves (5.125). \(\square\)

For a number field \(K\), put \(n=[K:\mathbb Q]\). Choose its \(n\) embeddings \(\tau_i:K\to\overline{\mathbb Q}\), and extend each to \(L\). Define the normed resolvent by
\[
 R_a(\chi)=\prod_{i=1}^n
       \det\rho_\chi\left(\sum_{g\in G}\tau_i(g(a))g^{-1}\right)
   =\prod_{i=1}^n\tau_i\bigl(r_{\chi^{\tau_i^{-1}}}(a)\bigr).
 \tag{5.126}
\]
For the second expression extend \(\tau_i\) further to an automorphism of \(\overline{\mathbb Q}\). Equality follows because the conjugated matrices represent \(\chi\). It is the first expression that defines the norm using only the selected embeddings of \(L\). Another extension of an embedding of \(K\) differs by an element of \(G\); (5.125) changes its factor by that element's character determinant. Thus the choices change \(R_a\) by \(\operatorname{Det}(g_0)\), for some \(g_0\in G\). Since character determinants are multiplicative, any ordering of the product of the changing group elements gives the same determinant. For symplectic \(\chi\) this ambiguity is exactly one.

**Theorem 5.44 (the actual lattice transition and its resolvent determinant).** Suppose \(L/K\) is tame. For each rational prime \(p\), let
\[
 K_p=K\otimes_{\mathbb Q}\mathbb Q_p,\quad
 L_p=L\otimes_{\mathbb Q}\mathbb Q_p,\quad
 B_p=\mathcal O_K\otimes_{\mathbb Z}\mathbb Z_p.
\]
Choose \(b_p\in\mathcal O_L\otimes\mathbb Z_p\) such that this integer module is \(B_p[G]b_p\). Write
\(b_p=\mu_p a\) with \(\mu_p\in K_p[G]^\times\). On a fixed integral basis \(e_1,\ldots,e_n\) of \(\mathcal O_K\), define \(T_p\in\operatorname{GL}_n(\mathbb Q_p[G])\) by
\[
 e_i\mu_p=\sum_j(T_p)_{ij}e_j.
 \tag{5.127}
\]
Then \(c(\mathcal O_L)\) is the stabilized gluing class of the tuple \((T_p)_p\) in Theorem 5.10. Its character determinants are
\[
 \operatorname{Det}(T_p)(\chi)
   =\prod_{\eta:K_p\to\overline{\mathbb Q}_p}
          \det\rho_\chi\left(\sum_g\eta((\mu_p)_g)g\right)
   =\frac{R_{b_p,p}(\chi)}{R_{a,p}(\chi)}.
 \tag{5.128}
\]
Here \(\eta\) ranges over all \(n\) scalar embeddings of the finite product \(K_p\), and the resolvents in the last quotient use the same extended embeddings of \(L_p\) in numerator and denominator. The ratio has no embedding-extension ambiguity.

**Proof: local generators and the gluing matrix.** At a prime of \(K\), fix one prime of \(L\) above it, with decomposition group \(D\). The local tame normal integral basis theorem, Theorem 4.3, gives a generator of the completed integer ring for that prime over the completed base ring \([D]\). In the product over the primes above it, put this generator in the selected component and zero in the others. Its \(G\)-translates, indexed first by \(G/D\) and then by \(D\), form a basis of the product: coset representatives move the selected component, and the \(D\)-translates give its basis. This proves freeness over the completed base ring \([G]\). Taking the product over the primes above the rational \(p\) gives \(b_p\). The decomposition of completions and primes is the one established in Section 1 and its exact Three differents provider. The rational normal basis identifies \(L_p\) with \(K_p[G]a\); two generators of a free rank-one left module differ by a unit, proving the assertion about \(\mu_p\).

The \(e_i a\) give a rational \(\mathbb Q[G]\)-frame of \(L\), and the \(e_i b_p\) a local \(\mathbb Z_p[G]\)-frame. Equation (5.127) says exactly that their coordinate row lattice is \(\mathbb Z_p[G]^nT_p\): a row \((v_i)\) represents \(\sum_i v_i e_i b_p=\sum_{i,j}v_i(T_p)_{ij}e_j a\). The local lattices agree with the integral-frame lattice for all but finitely many primes. Indeed multiply \(a\) by an integer to make it integral; the full integral lattices \(\mathcal O_K[G]a\) and \(\mathcal O_L\) then have finite abelian index, after clearing that single denominator. Outside its finitely many prime divisors, \(a\) is already an integral generator. We may choose \(b_p=a\) there. Thus \(T_p\) is integral for almost all \(p\), and Theorem 5.10 identifies the intersection lattice with \(\mathcal O_L\). Corollary 5.11 identifies its rank-zero class with the class in Taylor's statement.

**Proof: the determinant.** Apply \(\rho_\chi\) to the group entries of (5.127). Over \(\overline{\mathbb Q}_p\), the scalar algebra \(K_p\) decomposes into its \(n\) embeddings. This follows from the same separable Vandermonde evaluation argument in Lemma 5.43, applied to a primitive element of \(K/\mathbb Q\) and then base-changed to \(\mathbb Q_p\). Under that decomposition the represented restriction matrix is a direct sum of the matrices
\(\rho_\chi(\sum_g\eta((\mu_p)_g)g)\). Their determinant product is the middle expression in (5.128). This reasoning uses row matrices, so no group-action transpose or inversion is introduced.

For each extended scalar embedding, (5.124) gives
\(r_\chi(b_p)=\operatorname{Det}(\mu_p)(\chi)r_\chi(a)\). Multiplying over the scalar embeddings proves the quotient in (5.128). Changing an extended embedding multiplies both resolvents by the same group determinant, so it cancels. A change of local generator multiplies \(T_p\) on the left by an integral invertible matrix; a change of rational frame multiplies it on the right by a rational invertible matrix. These are precisely the equivalences of (5.28), including stabilization. Hence this is a computation of the class's actual transition matrices. Passing from their stabilized matrix quotient to a complete determinant quotient is a further class-description theorem. \(\square\)

**Lemma 5.45 (positivity with a quaternionic structure).** Let \(V\) be a finite-dimensional complex representation of a finite group, with a nondegenerate invariant alternating form. There is an invertible antilinear map \(J:V\to V\), commuting with the group, such that \(J^2=-1\). If an invertible complex linear map \(A\) commutes with \(J\), then \(\det A\) is a positive real number.

**Proof.** Average a positive Hermitian form over the group, using the convention that it is linear in its first argument. Define the antilinear map \(J_1\) by
\(\beta(v,w)=h(v,J_1w)\). Nondegeneracy makes it invertible, and invariance of both forms makes it commute with the group. In an \(h\)-orthonormal basis, write \(\beta(v,w)=v^tBw\) with \(B^t=-B\). Then
\(J_1w=\overline B\,\overline w\), and
\[
 P=-J_1^2=-\overline B B=B^*B
\]
is positive Hermitian. It commutes with the group and with \(J_1\). The finite-dimensional spectral argument diagonalizes \(P\): maximize its real Rayleigh quotient on the unit sphere to obtain an eigenvector, restrict to its orthogonal complement, and induct on dimension. All eigenvalues are positive. Real polynomial interpolation on these distinct eigenvalues defines \(P^{-1/2}\) and shows it commutes with \(J_1\). Consequently \(J=P^{-1/2}J_1\) commutes with the group and has square \(-1\).

The generalized eigenspaces of \(A\) are permuted by \(J\), sending the \(\lambda\)-space to the \(\overline\lambda\)-space. These spaces decompose \(V\): Bezout identities between the relatively prime powers of the factors of the characteristic polynomial give their projections. Nonreal eigenvalues thus contribute conjugate factors of equal multiplicity, whose determinant product is positive. If \(\lambda\) is real, its generalized eigenspace is preserved by \(J\). Its complex dimension \(m\) is even: writing the antilinear restriction as \(C\) followed by coordinate conjugation gives \(C\overline C=-1\), so
\(\det C\,\overline{\det C}=(-1)^m\); the left side is positive. The corresponding nonzero real eigenvalue contributes \(\lambda^m>0\). Multiplying all these factors proves \(\det A>0\). \(\square\)

**Theorem 5.46 (the symplectic resolvent signature).** Suppose \(\chi\) is symplectic, \(a\) is a normal basis generator, and \(v\) is a real place of \(K\). Evaluate \(r_\chi(a)\) using an extension of that embedding to \(L\). Its sign is
\[
 \operatorname{sign}(r_\chi(a))
   =(-1)^{d_v^-/2}=W_v(\chi),
 \tag{5.129}
\]
where \(d_v^-\) is the negative-eigenspace dimension of the corresponding complex conjugation. The normed resolvent \(R_a(\chi)\) lies in the totally real character field \(\mathbb Q(\chi)^\times\), and at every real embedding of that field,
\[
 \operatorname{sign}(R_a(\chi))=W_\infty(\chi)
                         :=\prod_{v\mid\infty}W_v(\chi).
 \tag{5.130}
\]

**Proof: one real place.** Let \(s\in G\) be complex conjugation for the chosen extension of the real embedding; it can be the identity. Put \(S=\rho_\chi(s)\), \(A=\rho_\chi(\mathcal R(a))\), and take \(J\) from Lemma 5.45. The antilinearity of \(J\) conjugates the scalar coefficients of the resolvent, whereas it commutes with the group matrices. Formula (5.125) therefore says
\[
 JAJ^{-1}=AS.
 \tag{5.131}
\]
The involution \(S\) commutes with \(J\). Its two eigenspaces are symplectic and have even dimensions by Lemma 5.40. Write \(P_+=(1+S)/2\), \(P_-=(1-S)/2\), and set
\(A_0=P_++iP_-\). Then \(JA_0J^{-1}=A_0S\), and \(A_0\) is invertible. Equation (5.131) shows that \(AA_0^{-1}\) commutes with \(J\); its determinant is positive by Lemma 5.45. On the negative eigenspace \(A_0\) is \(i\), and on the positive eigenspace it is 1. Thus
\(\det A=(\text{positive real})i^{d_v^-}\), giving (5.129). The last equality is exactly the real local phase proved in Theorem 5.42. This also proves directly that the determinant is real and nonzero.

**Proof: norm and all real embeddings.** In (5.126) choose conjugate extensions for each pair of complex embeddings of \(K\). Their determinants are conjugate: because \(J\) commutes with every group matrix, conjugating the coefficients of any group-ring element conjugates its character determinant. The pair's product is positive. The real embeddings contribute the signs just computed, and complex places have local phase one. This proves (5.130) at the given embedding.

For symplectic \(\chi\), each group determinant is one. Thus (5.125) removes every extension-choice ambiguity in (5.126). Applying \(\sigma\) to that product merely permutes the embeddings of \(K\), changing their extensions by group elements of determinant one. It follows that
\[
 \sigma(R_a(\chi))=R_a(\chi^\sigma).
\]
In particular the product lies in the fixed field of the stabilizer of \(\chi\), namely \(\mathbb Q(\chi)\). Each conjugate character is symplectic by Lemma 5.40 and is real-valued, since it is self-dual and unitary. Hence all embeddings of \(\mathbb Q(\chi)\) are real. For any involution, its character value is the integer \(d^+-d^-\); conjugation fixes that integer and the total dimension, so it fixes \(d^-\). Therefore \(W_\infty(\chi^\sigma)=W_\infty(\chi)\). Applying the first sign calculation to \(\chi^\sigma\) proves (5.130) at every real embedding. \(\square\)

For an irreducible symplectic \(\chi\) in a tame extension, define its Gauss normalization by
\[
 \tau_K(\chi)=W_K(\chi)W_\infty(\chi)^{-1}
                         \sqrt{N_{K/\mathbb Q}\mathfrak f_K(\chi)},
 \tag{5.132}
\]
with the positive square root. Theorem 5.42 makes the conductor a square and both phases signs, so \(\tau_K(\chi)\in\mathbb Q^\times\). Its sign is \(W_K(\chi)W_\infty(\chi)\). Consequently
\[
 w(\chi)R_a(\chi)\tau_K(\chi)^{-1}
                 \quad\text{is totally positive in }\mathbb Q(\chi).
 \tag{5.133}
\]
Indeed its sign at every real embedding is
\(W_K(\chi)W_\infty(\chi)/(W_K(\chi)W_\infty(\chi))=1\), by (5.130) and the definition of \(w\). This supplies the real-sign input for the determinant class comparison. It does not yet assert the integral group-ring determinant comparison at the finite primes.

### The determinant class group and the root-number class

We now prove that determinants recover the stabilized lattice gluing class. The denominator will consist of determinants of actual rational invertible matrices. This gives a complete class description without presuming a description of that denominator by real positivity. Compare the freely accessible [Fröhlich, Locally free modules, Sections 2, 4 and 5]. We include the local norm, approximation and integral-unit arguments needed here.

Write \(A=\mathbb Q[G]\), \(\Lambda=\mathbb Z[G]\), \(A_p=\mathbb Q_p[G]\), and \(\Lambda_p=\mathbb Z_p[G]\). Elementary matrices have the form \(1+aE_{ij}\), \(i\ne j\); their inverses are \(1-aE_{ij}\). The group they generate in \(\operatorname{GL}_r(B)\) is denoted \(E_r(B)\).

The local Brauer classification used below has the exact earlier proof in Brauer groups of local and global fields, Proposition 24.1 and Theorem 24.2. It identifies the class of the unramified cyclic algebra \((E/F,\sigma,\pi^t)\), with arithmetic Frobenius \(\sigma\), with \(t/[E:F]\) modulo integers, and proves that these are all local classes. The following proof supplies the norm and its kernel, which are additional statements.

**Lemma 5.47 (local division algebras and their norms).** Let \(F/\mathbb Q_p\) be finite, with residue field \(k\) of order \(q\), and let \(D\) be a finite-dimensional central division algebra over \(F\). There are an unramified extension \(E/F\) of degree \(n\), a generator \(\sigma\) of its cyclic Galois group, and \(v\in D\), such that
\[
 D=\bigoplus_{i=0}^{n-1}E v^i,\qquad
 va=\sigma(a)v,\qquad v^n=\pi,
 \tag{5.134}
\]
where \(\pi\) is a uniformizer of \(F\). Its maximal valuation ring is
\[
 \mathcal O_D=\bigoplus_{i=0}^{n-1}\mathcal O_E v^i,
 \qquad\mathfrak m_D=v\mathcal O_D,
 \qquad\mathcal O_D/\mathfrak m_D=\mathbb F_{q^n}.
 \tag{5.135}
\]
The reduced norm \(\operatorname{nrd}:D^\times\to F^\times\) is surjective, and
\[
 \operatorname{nrd}(a)=N_{E/F}(a)\ (a\in E^\times),\qquad
 \operatorname{nrd}(v)=(-1)^{n-1}\pi.
 \tag{5.136}
\]

**Proof: the division presentation.** First recall the elementary uniqueness in a Brauer class. A semisimple algebra is a product of matrix rings over division algebras: decompose its left regular module into simple modules and take its endomorphism ring, which is the opposite algebra. A simple matrix ring's unique simple-module type recovers its division algebra as the opposite endomorphism division ring. Thus two central division algebras that become isomorphic after adjoining matrix factors are isomorphic. This is precisely uniqueness of the division representative in a Brauer class.

If the local invariant of \(D\) is zero, its division representative is \(F\) and take \(n=1\), \(v=\pi\). Otherwise write its invariant \(t/n\), with \(0<t<n\) and \((t,n)=1\). The preceding Brauer theorem realizes this invariant by
\[
 C=\bigoplus_{i=0}^{n-1}Eu^i,\qquad
 ua=\operatorname{Frob}(a)u,\quad u^n=\pi^t.
\]
This algebra is itself a division algebra. Indeed for a nonzero sum define
\[
 w\left(\sum_i a_i u^i\right)
        =\min_i\bigl(v_E(a_i)+it/n\bigr).
\]
The distinct nonzero terms have distinct fractional valuation parts, since \((t,n)=1\). A product's uniquely least term is the product of the uniquely least terms, even when its exponent wraps around using \(u^n=\pi^t\). Thus \(w(xy)=w(x)+w(y)\); in particular no two nonzero elements multiply to zero. Injectivity of multiplication in this finite-dimensional algebra makes every nonzero element invertible. Its center is \(F\): commuting with \(E\) removes all terms except the zeroth, and then commuting with \(u\) imposes Frobenius invariance. Uniqueness of the division representative identifies \(C\) with \(D\).

Choose integers \(a,b\) with \(at+bn=1\), and put \(v=u^a\pi^b\). Then \(v^n=\pi\), and its conjugation on \(E\) is \(\sigma=\operatorname{Frob}^a\), a generator because \((a,n)=1\). Powers \(v^i\) reindex the powers of \(u\), up to nonzero scalars, so give (5.134). The valuation is now
\[
 w\left(\sum_i a_i v^i\right)=\min_i(v_E(a_i)+i/n).
\]
For \(0\leq i<n\), nonnegative valuation is equivalent to every \(a_i\) being integral. This proves (5.135), including its residue and radical. The ring is complete because its displayed finite coefficient module is complete. It is maximal among finite integral \(\mathcal O_F\)-orders: if an element of negative valuation belonged to such an order, its powers would have valuations tending to minus infinity, whereas a finite coefficient lattice has a common valuation lower bound.

**Proof: the norm.** Regard \(D\) as a right \(E\)-space on the basis \(1,v,\ldots,v^{n-1}\). Left multiplication by \(a\in E\) has diagonal entries \(\sigma^{-i}(a)\); left multiplication by \(v\) is the cyclic shift, with one wrap coefficient \(\pi\). These matrices split the algebra after tensoring by \(E\). To check fullness, a primitive element of \(E/F\) gives distinct diagonal entries; polynomial interpolation with coefficients in \(E\) gives every diagonal matrix unit, and the invertible cyclic shift then gives every matrix unit. Dimensions on both sides are \(n^2\). Thus their determinant is the reduced norm, and gives (5.136).

For completeness this determinant lies in \(F\): applying \(\sigma\) to the scalar coefficients in the splitting matrix is conjugation by its cyclic-shift matrix. Its determinant is therefore fixed by \(\sigma\). The same construction defines the reduced trace, with
\(\operatorname{trd}(a v^i)=0\) for \(0<i<n\), and \(\operatorname{trd}(a)=\operatorname{Tr}_{E/F}(a)\).

The splitting matrices of \(\mathcal O_D\) are integral over \(\mathcal O_E\). For a valuation-zero unit \(z\), its inverse also lies there, so \(\operatorname{nrd}(z)\) is a unit of \(\mathcal O_F\). Its reduction is the finite-field norm of its residue: modulo \(\pi\), positive powers of the shift are strictly triangular, while the zeroth coefficient gives the conjugate diagonal entries. In particular
\[
 v_F(\operatorname{nrd}(x))=n w(x).
 \tag{5.137}
\]
To see the latter equality, write \(x=v^m z\) with \(w(z)=0\) and use (5.136). The unramified coefficient-unit norm is onto by Lemma 5.26, so (5.136) realizes every unit of \(F\). The norm of \(v\), together with such units, realizes a uniformizer. Hence every element of \(F^\times\) is a reduced norm. \(\square\)

**Lemma 5.48 (density of local norm-one commutators).** In the local topology of \(D^\times\), the subgroup generated by commutators is dense in
\(\ker\operatorname{nrd}\).

**Proof.** Commutators have norm one because their norm takes values in an abelian field-unit group. The kernel is closed. Conversely, let \(x\) have norm one. Equation (5.137) makes \(x\in\mathcal O_D^\times\), and its residue has finite-field norm one. For the finite-field generator \(\bar\sigma\),
\[
 \{\bar\sigma(y)y^{-1}:y\in\mathbb F_{q^n}^\times\}
     =\ker N_{\mathbb F_{q^n}/\mathbb F_q}.
 \tag{5.138}
\]
Indeed the left side is contained in the right by telescoping. Its size is \((q^n-1)/(q-1)\), since its kernel is the fixed field's unit group. The right side has the same size by the cyclic finite-field norm calculation in Lemma 5.26. Lift \(y\) to \(\mathcal O_E^\times\); the commutator \([v,y]=vyv^{-1}y^{-1}\) has the prescribed residue. Dividing by it puts \(x\) in \(U_1=1+\mathfrak m_D\).

Put \(U_m=1+v^m\mathcal O_D\). Its quotient \(U_m/U_{m+1}\) is the additive residue field, represented by \(1+c v^m\), \(c\in\mathcal O_E\); products of two degree-\(m\) errors have degree at least \(m+1\). We show that each degree permitted by norm one can be removed by a commutator.

If \(n\nmid m\), choose \(z\in\mathcal O_E^\times\) whose residue is not fixed by \(\bar\sigma^m\). Conjugating \(1+c v^m\) by \(z\) gives
\[
 [z,1+c v^m]
    \equiv1+c\bigl(z/\sigma^m(z)-1\bigr)v^m
                                      \pmod{v^{m+1}\mathcal O_D}.
 \tag{5.139}
\]
The parenthesized coefficient is a residue unit. Choosing \(c\) realizes every leading coefficient in this degree.

If \(m=kn\), with \(k\geq1\), an element of \(U_m\) has the form
\(1+c\pi^k+z\), \(z\in v^{kn+1}\mathcal O_D\). The splitting matrix of its error is divisible by \(\pi^k\); its trace is \(\pi^k\operatorname{Tr}_{E/F}(c)\) modulo \(\pi^{k+1}\), since the trace of \(v\mathcal O_D\) lies in \(\pi\mathcal O_F\). Expanding the determinant, every term with at least two error entries is divisible by \(\pi^{2k}\subseteq\pi^{k+1}\). Consequently
\[
 \operatorname{nrd}(1+c\pi^k+z)
       \equiv1+\pi^k\operatorname{Tr}_{E/F}(c)
                                      \pmod{\pi^{k+1}}.
 \tag{5.140}
\]
Norm one forces \(\operatorname{Tr}_{\mathbb F_{q^n}/\mathbb F_q}(\bar c)=0\). The image of \(\bar\sigma-1\) is exactly this trace kernel: its kernel is \(\mathbb F_q\), while trace is onto by the polynomial proof in Theorem 5.39, including when \(p\mid n\). Both spaces thus have dimension \(n-1\) over \(\mathbb F_q\). Choose \(b\in\mathcal O_E\) with \(\bar\sigma(\bar b)-\bar b=\bar c\). Then
\[
 [v,1+b\pi^k]
       \equiv1+(\sigma(b)-b)\pi^k
                                    \pmod{v^{kn+1}\mathcal O_D}.
 \tag{5.141}
\]
This removes the permitted leading coefficient.

After each correction, divide by its commutator; the remainder still has norm one and lies in the next \(U_m\). A finite product of these commutators therefore approximates \(x\) to any prescribed depth. This proves density. For \(n=1\) the norm is the identity and its kernel is trivial. The argument claims density, and does not need to turn an infinite convergent product into a finite commutator expression. \(\square\)

**Lemma 5.49 (local character determinants and elementary approximation).** For every finite group \(G\), define
\[
 D_p=\operatorname{Hom}_{\Omega_p}
       (R_G,\overline{\mathbb Q}_p^\times),
 \qquad \Omega_p=\operatorname{Gal}(\overline{\mathbb Q}_p/\mathbb Q_p).
 \tag{5.142}
\]
An embedding of the cyclotomic character values in \(\overline{\mathbb Q}_p\) fixes this convention. Character determinants of \(A_p^\times\) give all of \(D_p\). For \(r\geq3\),
\[
 \overline{E_r(A_p)}
       =\ker\bigl(\operatorname{Det}:\operatorname{GL}_r(A_p)\to D_p\bigr).
 \tag{5.143}
\]
The closure is in the ordinary finite-dimensional \(p\)-adic topology.

**Proof: the character coordinates.** Maschke averaging, proved in Section 5, makes \(A_p\) semisimple. Decomposing its regular module as in Lemma 5.47 gives
\(A_p=\prod_j M_{s_j}(D_j)\), with centers finite extensions \(F_j/\mathbb Q_p\). Over \(\overline{\mathbb Q}_p\), Lemma 4.A decomposes the group algebra into matrix factors indexed by absolutely irreducible characters. Its center consists of one scalar for each character. Descending those scalars means imposing precisely \(\Omega_p\)-equivariance. Since \(R_G\) is free on the irreducibles, this identifies \(D_p\) with \(\prod_j F_j^\times\). In these coordinates the character determinant on the \(j\)-th factor is the reduced norm, viewed under each embedding of \(F_j\). This follows directly by splitting that central simple factor into its character matrix algebra. Lemma 5.47 makes each norm onto, proving the surjectivity assertion, already from units of \(A_p\).

**Proof: elementary matrices.** Over a division algebra, Gaussian row and column operations reduce an invertible matrix to a diagonal matrix. A nonzero pivot can be moved using
\[
 w(t)=
 \begin{pmatrix}1&t\\0&1\end{pmatrix}
 \begin{pmatrix}1&0\\-t^{-1}&1\end{pmatrix}
 \begin{pmatrix}1&t\\0&1\end{pmatrix}
 =\begin{pmatrix}0&t\\-t^{-1}&0\end{pmatrix},
 \qquad
 w(t)w(-1)=\operatorname{diag}(t,t^{-1}).
 \tag{5.144}
\]
These are products of elementary matrices. For a pivot \(a\), subtract a row multiple \(ba^{-1}\) to clear its column and a column multiple \(a^{-1}c\) to clear its row, then induct on the remaining block. This proves generation by elementary and diagonal matrices over the division algebra, with the correct noncommutative order.

The elementary subgroup is normal: conjugation by a diagonal matrix multiplies each elementary coefficient on the left and right by the corresponding units, and the displayed generators already generate the whole group. In its quotient, a unit placed in one diagonal position equals the same unit placed in another, by the elementary interchange matrices. Such representatives can be placed in different positions and then commute. Hence the quotient is abelian, and
\(\operatorname{diag}([x,y],1,\ldots,1)\) is elementary for any two division-algebra units. Every matrix has, modulo elementary matrices, a representative \(\operatorname{diag}(d,1,\ldots,1)\); its reduced norm is \(\operatorname{nrd}(d)\). Lemma 5.48 therefore makes the norm-one matrices limits of elementary matrices.

For a factor \(M_s(D)\), identify \(\operatorname{GL}_r(M_s(D))\) with \(\operatorname{GL}_{rs}(D)\). Block elementary matrices split into scalar elementary matrices. Conversely a scalar elementary matrix with its two positions in different block rows is a block elementary matrix. For positions in the same block row, choose a position in another row and use
\([1+aE_{ik},1+E_{kj}]=1+aE_{ij}\), with distinct scalar indices \(i,j,k\). Thus the elementary groups agree under this identification. The central idempotents of the product of factors allow coefficients supported in one factor at a time. Applying the division-algebra result factor by factor proves (5.143). Elementary determinants are one; continuity makes their closure lie in that kernel as well, completing both inclusions. \(\square\)

Put
\[
 D_p^0=\operatorname{Det}(\Lambda_p^\times)
      =\operatorname{Det}(\operatorname{GL}_\infty(\Lambda_p)),
 \qquad
 D_{\mathbb Q}=\operatorname{Det}(\operatorname{GL}_\infty(A)).
 \tag{5.145}
\]
Here stabilization adds identity blocks. The equality for \(D_p^0\) is the proved matrix-to-unit result, Lemma 5.6. Each global matrix and its inverse have integral coefficients at almost every prime, so \(D_{\mathbb Q}\) embeds diagonally in the restricted product
\(\prod_p{}'D_p\), taken with respect to \(D_p^0\). This restricted product consists of tuples whose entries belong to \(D_p^0\) outside a finite set.

**Theorem 5.50 (complete determinant description of the stable class).** There is a canonical isomorphism
\[
 \operatorname{Cl}(\mathbb Z[G])
   \xrightarrow{\ \sim\ }
 \mathcal C_D(G):=
 \frac{\displaystyle\prod_p{}'D_p}
      {\displaystyle\left(\prod_p D_p^0\right)D_{\mathbb Q}}.
 \tag{5.146}
\]
It sends \(c(M)\), with gluing matrices \((a_p)\) in Theorem 5.10, to the class of \((\operatorname{Det}(a_p))_p\). In particular, two stabilized gluing tuples with the same determinant class define the same locally free class.

**Proof: well-definedness and surjectivity.** A change of integral frames multiplies the local determinants by elements of \(D_p^0\); a change of rational frame multiplies them by one element of \(D_{\mathbb Q}\), by (5.28). Stabilization has no effect. Direct sums multiply determinants, so this gives a homomorphism from the rank-zero group completion, using Proposition 5.9.

Conversely take a restricted determinant tuple. At its finitely many exceptional primes choose matrices realizing its entries, by Lemma 5.49. At every other prime Lemma 5.6 realizes the entry by one integral unit. Stabilize to one common size, using the maximum of the finitely many exceptional sizes and 1. The resulting tuple satisfies the integral condition of Theorem 5.10 and therefore gives a locally free lattice. Its class maps to the chosen determinant tuple. This proves surjectivity.

**Proof: a rational approximation with controlled denominators.** For a finite set \(S\) of rational primes,
\[
 \Lambda[1/S]\text{ is dense in }\prod_{p\in S}A_p.
 \tag{5.147}
\]
To check this, work on the group basis. For finitely many desired \(p\)-adic coefficients, multiply by an integer \(N\) supported on \(S\), large enough that all become integral. Prescribing their desired residues to any finite depths is then a system of integer congruences at distinct primes. The integer Chinese remainder theorem solves these congruences. Dividing the solutions by \(N\) gives the required approximations, and they are integral outside \(S\). The same argument works for any finite list of coefficients at once.

Suppose now that a gluing tuple has trivial determinant class. After stabilization, of size \(r\geq3\), write
\[
 \operatorname{Det}(a_p)=\operatorname{Det}(u_p)\operatorname{Det}(b),
 \quad u_p\in\operatorname{GL}_r(\Lambda_p),\quad
 b\in\operatorname{GL}_r(A).
\]
Integral determinants need only one unit before stabilization, by Lemma 5.6, and the global matrix has one finite size, so a common \(r\) exists. Set \(k_p=u_p^{-1}a_p b^{-1}\). Its determinant is one at every prime, and \(k_p\in\operatorname{GL}_r(\Lambda_p)\) outside a finite set \(S\).

At each \(p\in S\), Lemma 5.49 approximates \(k_p\) by a finite word of elementary matrices. Integral invertible matrices form an open subgroup of \(\operatorname{GL}_r(A_p)\): a sufficiently small perturbation of the identity lies in \(1+pM_r(\Lambda_p)\), whose inverse is a convergent geometric series. Choose the approximations sufficiently close that \(k_p e_p^{-1}\) is integral invertible. Combine the finitely many elementary words into one word: for a word intended at one prime, put zero in each of its elementary coefficients at the other primes. By (5.147), approximate all these coefficient tuples by coefficients in \(\Lambda[1/S]\). Continuity of this finite word gives one
\(e\in E_r(A)\), integral invertible outside \(S\), with
\[
 k_p e^{-1}\in\operatorname{GL}_r(\Lambda_p)
                                  \quad\text{for every }p.
\]
Thus \(k_p=u'_p e\), with integral \(u'_p\). Equation (5.28) makes this tuple equivalent to the free tuple. Restoring the original integral and rational factors proves that its stable lattice class is zero. This proves injectivity and the isomorphism. No rational reduced-norm image theorem has been used: \(D_{\mathbb Q}\) in (5.146) is the determinant image of actual rational matrices. \(\square\)

**Lemma 5.51 (integral determinants away from the group order).** If \(p\nmid|G|\), then
\[
 D_p^0=
 \operatorname{Hom}_{\Omega_p}
       (R_G,\overline{\mathbb Z}_p^{\times}),
 \tag{5.148}
\]
where \(\overline{\mathbb Z}_p\) is the valuation ring in \(\overline{\mathbb Q}_p\). In particular any \(\Omega_p\)-equivariant sign homomorphism is an integral determinant at such a prime.

**Proof: an integral splitting algebra.** The residue algebra \(\mathbb F_p[G]\) is semisimple by averaging, since \(|G|\) is invertible. Its division factors are finite fields by Lemma 5.31. Choose a finite residue-field extension splitting all those fields, and an unramified coefficient extension \(E/\mathbb Q_p\) with that residue field. We can enlarge it unramified if necessary. The unramified extensions and tensor splitting are supplied by Lemma 5.28. Put \(R=\mathcal O_E\); then
\(R[G]/pR[G]=\prod_j M_{d_j}(k_E)\).

Lift a complete orthogonal family of its diagonal primitive idempotents to \(R[G]\), using the idempotent Newton-and-corner construction in Lemma 5.34. Every corner \(e_iR[G]e_j\) is a direct summand of the finite free \(R\)-module \(R[G]\). Its rank is its residue dimension: zero for different residue blocks, and one for positions in the same block. In particular \(e_iR[G]e_i=R e_i\), since \(e_i\) generates its residue and Nakayama makes it generate the rank-one module.

Within one block, choose lifts \(x_i\in e_iR[G]e_1\), \(y_i\in e_1R[G]e_i\) of the residue matrix units. The product \(y_ix_i\in R e_1\) is a scalar unit times \(e_1\). Normalize \(y_i\) to make \(y_ix_i=e_1\); then \(x_i y_i\) is an idempotent in \(R e_i\), reducing to \(e_i\), so equals \(e_i\). Set \(x_1=y_1=e_1\). The elements \(x_i y_j\) are matrix units: orthogonality gives zero when the middle indices differ, and \(y_jx_j=e_1\) gives the required product when they agree. They span their rank-one corners by Nakayama. Corners between different blocks vanish. Hence
\[
 R[G]\simeq\prod_j M_{d_j}(R).
 \tag{5.149}
\]
Its generic factors are therefore the absolutely irreducible character factors; every character has an integral matrix representation over \(R\).

An integral unit, and its inverse, have unit determinants in these representations. Thus the left side of (5.148) is contained in the right. Conversely an equivariant unit-valued homomorphism has, in the split generic center, one value for each character, all in \(R^\times\). The values belong to \(E\) because its group algebra is split, so \(\operatorname{Gal}(\overline{\mathbb Q}_p/E)\) fixes every character and every equivariant value. In each matrix block of (5.149), put that value in one diagonal position and 1 in all others. This gives \(x\in R[G]^\times\) with exactly the prescribed character determinants.

Those determinants are invariant under \(\operatorname{Gal}(E/\mathbb Q_p)\). The full unramified determinant descent proved in Theorem 5.35 supplies a unit of \(\mathbb Z_p[G]\) with the same determinants. This proves the reverse inclusion, including when \(p\) divides the degree of the unramified splitting extension. \(\square\)

**Theorem 5.52 (construction of the root-number class).** Let \(L/K\) be a tame Galois extension of number fields with group \(G\), and let \(w\) be the symplectic sign homomorphism (5.120). Regard the same signs as a tuple \((w)_p\). It belongs to \(\prod_p{}'D_p\), and defines the class
\[
 W_{L/K}:=\text{the inverse image of }[(w)_p]
           \text{ under (5.146)}
       \quad\in\operatorname{Cl}(\mathbb Z[G]).
 \tag{5.150}
\]
This class depends only on the signs of the symplectic irreducible Artin root numbers, is independent of all local determinant realizations and character-coordinate choices, and satisfies
\[
 2W_{L/K}=0.
 \tag{5.151}
\]
It can be constructed by gluing matrices supported only at primes dividing \(|G|\).

**Proof.** Theorem 5.42 makes \(w\) Galois equivariant. Its values lie in \(\{1,-1\}\subset\mathbb Q^\times\). Local Galois permutations of characters are restrictions of permutations of their cyclotomic values; each such automorphism of the cyclotomic number field extends to the global algebraic closure. Hence the same homomorphism is \(\Omega_p\)-equivariant for every \(p\), and belongs to \(D_p\). Lemma 5.49 realizes it by local generic units. Lemma 5.51 realizes it by integral units whenever \(p\nmid|G|\), proving the restricted-product condition.

At the remaining finitely many primes choose any generic unit realizing \(w\); at other primes take the identity. Its determinant tuple differs from \((w)_p\) by integral determinant factors, so gives the same element of (5.146). Theorem 5.10 constructs the corresponding locally free lattice; subtracting its free rank gives (5.150). Another local realization has the same determinant class, and Theorem 5.50 proves that it gives the same stable class. Changing character coordinates merely reindexes the character determinants and leaves the construction unchanged.

Finally \(w^2=1\) by Theorem 5.42. The isomorphism (5.146) turns determinant multiplication into class addition, so proves (5.151). All nonsymplectic irreducible values are 1 by definition, so no other root numbers enter the class. This constructs the class appearing in Taylor's statement. The remaining identity with \(c(\mathcal O_L)\) is the finite-prime arithmetic comparison of its resolvent determinants (5.128) with this sign tuple. \(\square\)

**Corollary 5.53 (odd-order groups).** If \(|G|\) is odd, then \(W_{L/K}=0\).

**Proof.** An odd-order group has no irreducible symplectic character. Here is the character argument. For a complex representation \(V\) let \(T\) interchange the factors of \(V\otimes V\), and let
\(P=|G|^{-1}\sum_g\rho(g)\otimes\rho(g)\) be the averaging projection onto its invariant tensors. Directly on a basis,
\[
 \operatorname{Tr}(TP)=\frac1{|G|}\sum_g\chi(g^2).
 \tag{5.152}
\]
The identity used is \(\operatorname{Tr}(T(B\otimes B))=\operatorname{Tr}(B^2)\), obtained by summing the entries with interchanged indices. If \(V\) is irreducible symplectic, its invariant-tensor space is one-dimensional and alternating, so this trace is \(-1\). Indeed \(V\simeq V^\vee\); Schur's lemma, proved in Section 4, gives a one-dimensional equivariant pairing space, whose alternating form makes the interchange act by \(-1\). The nondegenerate form identifies the invariant tensors with that pairing space.

For odd \(|G|\), squaring is a bijection on \(G\), with inverse \(g\mapsto g^{(|G|+1)/2}\). The right side of (5.152) is therefore \(|G|^{-1}\sum_g\chi(g)\), the dimension of \(V^G\). It is zero for a nontrivial irreducible and one for the trivial representation. Neither value is \(-1\), and a one-dimensional trivial representation cannot be symplectic. Thus there are no irreducible symplectic characters, \(w=1\), and (5.150) is zero. The arithmetic equality of this class with the integer-ring class is the remaining Taylor comparison. \(\square\)

### Rational determinants and the global norm theorem

The denominator in (5.146) consists of actual rational determinants. We now identify it by a complete global norm proof. The real sign restriction is the one in [Fröhlich, Locally free modules, Section 4 and Section 5, assertion B]. The arithmetic input is the already proved local–global Brauer theorem, Section 4 and Theorem 24.4; the norm construction itself is given here.

**Lemma 5.54 (a local field generator with a prescribed norm).** Let \(F/\mathbb Q_p\) be finite, \(N\geq1\), and \(\alpha\in F^\times\). There is a degree-\(N\) field extension \(T/F\) with a generator \(a\) satisfying
\[
 N_{T/F}(a)=\alpha.
 \tag{5.153}
\]
Neither the extension nor its polynomial is required to be Galois.

**Proof: a primitive unramified unit.** An unramified extension of every degree \(g\) exists by the following complete-DVR construction, also used in Lemma 5.28. Lift an irreducible degree-\(g\) residue polynomial to a monic polynomial over \(\mathcal O_F\). Its quotient ring is finite free and complete, with residue field of degree \(g\). Every nonzero element is a power of the base uniformizer times an element of nonzero residue; that latter element is a unit by a geometric-series inverse. The ring is therefore a domain and a DVR with the same uniformizer, and its fraction field \(E\) has degree \(g\). Simple-root lifting of all residue conjugates gives all \(g\) automorphisms, identifying its Galois group with the cyclic residue Frobenius group. The finite residue field and its degree-\(g\) extension were constructed in Theorem 5.39. Simple-root lifting is the Newton argument in Lemma 5.55 below, or the earlier Lemma 5.1 of Three differents.

We show that every unit \(c\in\mathcal O_F^\times\) has a norm preimage \(u\in\mathcal O_E^\times\) that also generates \(E/F\). Lemma 5.26 supplies a unit preimage \(u_0\). If \(g=1\) it already has the asserted property. Otherwise let \(\sigma\) generate the unramified Galois group, and consider
\[
 u(t)=u_0\frac{\sigma(1+t z)}{1+t z},\qquad t\in F.
 \tag{5.154}
\]
For all sufficiently small \(t\), this is a unit and has norm \(c\), by telescoping the product of conjugates. We choose \(z\) so that \(u(t)\) avoids every proper intermediate field for some such \(t\).

There are only finitely many intermediate fields because the Galois group is cyclic. The image of \(\sigma-1\) on the \(g\)-dimensional \(F\)-space \(E\) is the trace-zero space: its kernel is \(F\), its image lies in that space, and trace is onto since \(\operatorname{Tr}(1)=g\ne0\). This image is not contained in any proper intermediate field \(E'\). Indeed \([E':F]\leq g/2<g-1\) for \(g>2\). For \(g=2\), the only such field is \(F\), whose intersection with trace zero is zero.

For each \(E'\) containing \(u_0\), the condition \(\sigma(z)-z\in E'\) is therefore a proper linear-subspace condition on \(z\). A finite union of proper subspaces does not exhaust a vector space over an infinite field: select a nonzero linear functional vanishing on each subspace, and specialize their nonzero product polynomial. The specialization argument is the one proved in Lemma 4.1. Choose \(z\) outside that finite union. If \(u_0\notin E'\), the value of (5.154) at zero already lies outside it. If \(u_0\in E'\), its derivative at zero is
\(u_0(\sigma(z)-z)\notin E'\).
In either case an \(F\)-linear functional vanishing on \(E'\) gives a nonzero rational function of \(t\) when applied to \(u(t)\). It is rational because inversion of \(1+t z\) is given by the adjugate of its multiplication matrix. A nonzero rational function has only finitely many zeros. Avoiding these finitely many values, while taking \(t\) arbitrarily small, makes \(u(t)\) belong to no proper intermediate field. Set \(u=u(t)\). It generates \(E/F\) and retains its prescribed norm.

**Proof: arbitrary valuation.** Write \(m=v_F(\alpha)\), fix a uniformizer \(\pi\), and set
\[
 g=(m,N),\quad e=N/g,\quad k=m/g,
\]
with \((0,N)=N\). Then \((k,e)=1\). Choose the unramified extension \(E/F\) of degree \(g\), and a generating unit \(u\) with
\[
 N_{E/F}(u)=(-1)^{g(e-1)}\alpha\pi^{-m},
\]
by the first part. Adjoin a root \(a\) of
\(X^e-\pi^k u\) over \(E\). With the extension of \(v_E\), its valuation is \(k/e\). The valuations of \(1,a,\ldots,a^{e-1}\) have distinct fractional parts because \((k,e)=1\); any nonzero \(E\)-linear combination has a unique least-valuation term, so cannot vanish. Thus the polynomial is irreducible and \([E(a):E]=e\), also for negative \(m\). Further \(u=a^e\pi^{-k}\), so \(F(a)\) contains \(E\). Therefore \([F(a):F]=eg=N\). Finally
\[
 N_{E(a)/E}(a)=(-1)^{e-1}\pi^k u,
 \qquad
 N_{F(a)/F}(a)=(-1)^{g(e-1)}\pi^m N_{E/F}(u)=\alpha.
\]
This proves (5.153) and every valuation case. \(\square\)

**Lemma 5.55 (weak approximation and preservation of a local generating polynomial).** Let \(F\) be a number field. Its elements are dense in a product of finitely many finite completions and all its archimedean completions. If a monic degree-\(N\) polynomial over a finite completion \(F_v\) is the minimal polynomial of a generator \(a\) of \(T/F_v\), then sufficiently close monic degree-\(N\) polynomials have a root \(b\in T\) with
\[
 F_v(b)=T.
 \tag{5.155}
\]
Closeness may be achieved by varying all coefficients except the constant coefficient, when that coefficient has already been fixed correctly.

**Proof: weak approximation.** Choose an integral basis of \(\mathcal O_F\), whose existence was proved in lesson one and Corollary 5.11. Its image in
\(F_\infty=\mathbb R^{r_1}\times\mathbb C^{r_2}\), considered as a real space of dimension \([F:\mathbb Q]\), is a lattice. Indeed the separable embedding matrix is invertible by the Vandermonde argument of Lemma 5.43; replacing each conjugate complex pair by its real and imaginary coordinates gives an invertible real matrix. Thus an integral basis identifies \(\mathbb Z^{[F:\mathbb Q]}\) with a full real lattice.

Given finitely many desired finite-place targets, multiply by one nonzero rational integer \(d\) so that they are all integral. Fix prime-ideal powers prescribing the required residue accuracies, and let \(I\) be their product. Chinese remainders in \(\mathcal O_F\) prescribe any such finite residues; the completed residue quotient equals the original one by the exact completion result linked at the start of this lesson. The ideal \(I\) is a full integer lattice of finite index: it contains a nonzero rational integer times \(\mathcal O_F\), by taking sufficiently large powers of the finitely many rational primes below its factors.

Choose a rational prime \(\ell\) below none of the selected finite places. For each \(j\), prescribe the residues of \(d\ell^j\) times the finite targets, and choose one solution coset modulo \(I\). At infinity choose an element \(c_j\) of this coset within a uniformly bounded distance of \(d\ell^j\) times the archimedean target. Such a bound is independent of the coset: express the target minus any coset representative on a lattice basis of \(I\), and round its real coordinates to integers. Now \(c_j/(d\ell^j)\) has the prescribed finite accuracies, since \(\ell\) is a unit there, and its archimedean error tends to zero. Taking sufficiently deep finite congruences first and sufficiently large \(j\) second proves density. Apply this construction separately to each coefficient when approximating a polynomial.

**Proof: a nearby root.** The minimal polynomial \(f_0\) has \(f_0'(a)\ne0\). Choose a nonzero \(\delta\in T\) sufficiently small that its absolute value is less than the distances from \(a\) to all its other conjugates. Also make the higher Taylor coefficients of
\[
 h(Y)=\frac{f(a+\delta Y)}{\delta f'(a)}
 \tag{5.156}
\]
integral when \(f\) is close to \(f_0\). This is possible: the coefficient of \(Y^i\), for \(i\geq2\), is the coefficient of \((X-a)^i\) in \(f\), multiplied by \(\delta^{i-1}/f'(a)\). First fix \(\delta\) for \(f_0\); sufficiently close coefficients preserve these valuation bounds and the nonzero derivative. Then make \(f(a)\) small enough that \(h(0)\) is in the maximal ideal. We have \(h\in\mathcal O_T[Y]\) and \(h'(0)=1\).

Here is the needed root argument. Starting at zero, iterate
\(y_{j+1}=y_j-h(y_j)/h'(y_j)\).
The derivative remains a unit on the maximal ideal. Taylor expansion over \(\mathcal O_T\) makes the new error lie in the square of the previous error ideal; the changes therefore tend to zero, and completeness gives \(y\) in that maximal ideal with \(h(y)=0\). Thus \(b=a+\delta y\in T\) is a root of \(f\), closer to \(a\) than any other conjugate of \(a\).

To justify (5.155), take a finite Galois normal closure containing \(a\) and \(b\). Every automorphism fixing \(b\) preserves the absolute value: the integral closure of a complete characteristic-zero DVR in a finite extension is the unique complete DVR proved in Lemma 4.B. Such an automorphism \(s\) satisfies
\[
 |s(a)-a|\leq\max(|s(a)-b|,|b-a|)=|b-a|.
\]
The separation of conjugates forces \(s(a)=a\). Finite Galois correspondence gives \(F_v(a)\subseteq F_v(b)\); since \(b\in T\), equality follows. Its minimal polynomial has degree \(N\), so the monic degree-\(N\) polynomial \(f\) is irreducible. This proves the preservation assertion. No coefficient needs to vary if it already has the required value, proving the last statement. \(\square\)

**Theorem 5.56 (the global reduced-norm theorem).** Let \(D\) be a central division algebra of degree \(N\) over a number field \(F\). An element \(\alpha\in F^\times\) is a reduced norm if and only if
\[
 \alpha_v>0\quad\text{at each real place }v
       \text{ where }D\otimes_F F_v\text{ has a quaternionic division factor}.
 \tag{5.157}
\]
For a matrix algebra over \(D\), the image is the same group. This is the Hasse–Schilling norm theorem in the form needed here.

**Proof: algebraic setup.** We recall why the degree and splitting arguments used in this proof apply to a central division algebra. Left and right multiplication on \(D\) have joint commutant equal to its center \(F\). Their image is a finite algebra acting faithfully and irreducibly on the \(F\)-space \(D\); its radical kills that simple module and is therefore zero. The semisimple regular-module argument of Lemma 4.A, with division endomorphism rings before extending scalars, makes this image the full \(\operatorname{End}_F(D)\), since its simple module has endomorphism field \(F\). Dimensions then give
\(D\otimes_F D^{\mathrm{op}}\simeq\operatorname{End}_F(D)\).
After any scalar extension, every two-sided ideal of the extended algebra is consequently invariant under every linear endomorphism of that algebra; it is zero or the whole space. Its center is the scalar field. Over an algebraic closure its division representative is the field, by the eigenvalue argument in Lemma 4.A. Thus it is \(M_N\), and \(\dim_FD=N^2\).

The reduced norm is the determinant in this splitting matrix algebra. It belongs to \(F\), independently of the splitting choice: an automorphism of \(M_N\) is inner. To verify the latter fact, choose a basis from the images of its diagonal matrix units; conjugation then fixes those units. Each off-diagonal unit is multiplied by a scalar, and their multiplication rule makes these scalars ratios of diagonal scalars. A second diagonal conjugation removes them all. This proves the assertion and the determinant's Galois invariance. The splitting matrices and their inverses involve finitely many algebraic coefficients, so a finite Galois splitting field suffices.

**Proof: the necessary real restriction.** The real Brauer classification in the earlier Theorem 24.2 makes a nonsplit real component \(M_m(\mathbb H)\), of degree \(2m\). Its complex splitting representation commutes with an antilinear map of square \(-1\): use the usual two-dimensional matrix representation of \(\mathbb H\), and the map \((z_1,z_2)\mapsto(\overline z_2,-\overline z_1)\), blockwise. The determinant is positive by the eigenvalue-pairing proof in Lemma 5.45. Therefore every reduced norm satisfies (5.157).

**Proof: construct a global field with norm \(\alpha\).** Assume (5.157). The Brauer class of \(D\) has finite support, by the complete support proof in the earlier Brauer lesson's Section 4. Let \(S\) contain its nonzero finite invariants and one additional finite place. At every \(v\in S\), Lemma 5.54 supplies a degree-\(N\) extension \(T_v/F_v\) and a generator \(a_v\) of norm \(\alpha_v\). Its monic minimal polynomial has constant coefficient
\(c=(-1)^N\alpha\), evaluated in \(F_v\).

At any nonsplit real place, \(N\) is even: its local degree is \(2m\). There take the target polynomial \(X^N+\alpha_v\), which is strictly positive on the real line. This property persists under sufficiently small changes in its other coefficients. In fact \(|x|^i\leq1+|x|^N\) for \(0<i<N\), and
\(x^N+\alpha_v\geq\min(1,\alpha_v)(1+|x|^N)\).
Making the sum of the absolute values of those coefficients less than \(\min(1,\alpha_v)\) preserves strict positivity. At other infinite places impose any convenient approximation targets.

Use Lemma 5.55 to choose a global monic polynomial \(f\) of degree \(N\), with constant coefficient exactly \(c\), sufficiently close to all these local polynomials. At the finite places it remains irreducible and defines \(T_v\); at the specified real places it has no real root. The additional finite place ensures global irreducibility, including when the Brauer support was entirely real. Set
\[
 T=F[X]/(f),\qquad a=X\bmod f.
\]
Then \([T:F]=N\) and \(N_{T/F}(a)=(-1)^N c=\alpha\).

**Proof: split the algebra and embed the field.** At a finite support place, write
\(D\otimes_F F_v=M_{m_v}(D_v)\), with division degree \(d_v\). Dimensions give \(N=m_vd_v\). Lemma 5.47 makes the denominator of its local invariant \(d_v\), so multiplying the invariant by \([T_v:F_v]=N\) gives zero. Restriction multiplies local invariants by the extension degree for arbitrary finite extensions, by equation (11) and Theorem 24.2 of the Brauer provider. Thus \(T_v\) splits the local algebra. Outside the finite support it was already split. At a nonsplit real place, \(f\) has no real roots, so every completion of \(T\) above it is complex and the restricted invariant is zero. All other infinite components were already split. Consequently the Brauer class of \(D\otimes_F T\) is zero at every place of \(T\). The proved global injectivity in Section 4 and Theorem 24.4 gives
\(D\otimes_F T\simeq M_N(T)\).

This degree-\(N\) splitting field embeds in \(D\). Indeed the simple \(M_N(T)\)-module \(T^N\), restricted to \(D\), has \(F\)-dimension \(N^2\), hence is free of rank one over the division algebra \(D\). Transport its commuting scalar \(T\)-action along a \(D\)-linear identification with \(D\). It gives an injection
\(T\to\operatorname{End}_D(D)=D^{\mathrm{op}}\).
Because \(T\) is commutative, the same map is an embedding into \(D\). The embedded generator \(a\) has reduced characteristic polynomial \(f\): over an algebraic closure, the distinct roots of \(f\) give eigenspace projections by polynomial interpolation. Its minimal polynomial is \(f\), so each of those \(N\) eigenspaces is nonzero. Its splitting matrix has size \(N\), so each eigenspace has dimension one. The characteristic polynomial is therefore exactly \(f\), and its reduced norm is \((-1)^N f(0)=\alpha\). This proves sufficiency.

Finally Gaussian elimination over \(D\), proved in Lemma 5.49, makes the reduced norm of an invertible matrix the product of the reduced norms of its diagonal units. This is the norm of their product in \(D^\times\). Conversely put any division unit in one diagonal position and 1 in the others. Thus a matrix algebra has exactly the same norm image. \(\square\)

Define
\[
 P_G^+=\left\{f\in\operatorname{Hom}_{\Omega_{\mathbb Q}}
       (R_G,\overline{\mathbb Q}^{\times}):
       f(\chi)\text{ is totally positive for every irreducible symplectic }\chi
                         \right\}.
 \tag{5.158}
\]
Equivariance puts \(f(\chi)\) in its character field \(\mathbb Q(\chi)\), which is totally real for symplectic \(\chi\) by Theorem 5.46.

**Theorem 5.57 (the positive rational determinant image).** For every finite group \(G\),
\[
 D_{\mathbb Q}=\operatorname{Det}(\mathbb Q[G]^\times)=P_G^+.
 \tag{5.159}
\]
Accordingly the denominator \(D_{\mathbb Q}\) in (5.146) can be replaced by \(P_G^+\), giving the positivity form of the determinant class description.

**Proof: real character type.** As in Lemma 5.49, the center of \(\mathbb Q[G]\) is identified with the \(\Omega_{\mathbb Q}\)-equivariant scalar functions on irreducible characters. Indeed extending the field gives one central scalar for each character, and the finite linear commutation equations descend the center. Thus the centers of its simple factors are the character fields, one for each Galois orbit.

We identify which real components are quaternionic. At a real embedding of a character field, the corresponding irreducible complex character \(\chi\) is real-valued. Averaging a positive Hermitian form makes its representation unitary, so its dual character is its complex conjugate. It is therefore self-dual. Schur's lemma gives a one-dimensional invariant bilinear-form space, and its nonzero form is nondegenerate. Transposing it gives either the same form or its negative, since transposing twice is the identity. These are its symmetric and alternating cases.

In the alternating case, Lemma 5.45 constructs an invariant antilinear \(J\) with \(J^2=-1\). In the symmetric case the same construction has \(J_1^2=B^*B\), because \(B^t=B\); positive spectral normalization gives an invariant \(J\) with \(J^2=1\). Its fixed real space \(V_0\) satisfies \(V=\mathbb C\otimes_{\mathbb R}V_0\): explicitly split a vector into
\((v+Jv)/2+i(v-Jv)/(2i)\).

Complex conjugation fixes the primitive character idempotent because it fixes \(\chi\); hence that idempotent has real coefficients. Its real group-algebra factor has dimension \(\chi(1)^2\); its complexification is the full character matrix algebra, by Section 5's semisimple character decomposition. In the symmetric case its action on \(V_0\) is therefore the full \(M_{\chi(1)}(\mathbb R)\), since that real endomorphism space has the same dimension. In the alternating case its action lies in the real algebra commuting with \(J\). We check that this is \(M_{\chi(1)/2}(\mathbb H)\). For \(v\ne0\), the complex vectors \(v,Jv\) are independent: a relation \(Jv=\lambda v\) would give \(-v=|\lambda|^2v\). Their plane is \(J\)-stable. Replace any positive Hermitian form \(h_0\) by
\(h(v,w)=h_0(v,w)+\overline{h_0(Jv,Jw)}\); then \(J\) is antiunitary for \(h\). The orthogonal complement of that plane is \(J\)-stable, so induction gives a basis of such pairs. In this basis each block of a complex-linear map commuting with \(J\) has the form
\(\begin{pmatrix}a&b\\-\overline b&\overline a\end{pmatrix}\).
These blocks are precisely the usual matrix representation of the quaternions, so the commuting algebra is the asserted quaternion matrix algebra and has real dimension \(\chi(1)^2\). The group-algebra action has that same dimension, so is the whole algebra. Consequently a real simple component is quaternionic exactly when its character is symplectic.

**Proof: global image.** Decompose \(\mathbb Q[G]\) into its simple factors \(M_s(D)\) over the character fields. Character determinants are their reduced norms under the respective center embeddings, just as in Lemma 5.49. Gaussian elimination over each division factor shows that stabilization does not enlarge this image: every matrix norm is the norm of one division unit, which can be put in one diagonal position of \(M_s(D)\). Thus \(D_{\mathbb Q}=\operatorname{Det}(\mathbb Q[G]^\times)\).

Theorem 5.56 describes its center values exactly by positivity at quaternionic real components. The real-type calculation identifies those with symplectic characters. Since the homomorphisms are Galois equivariant, the conditions over all real center embeddings are exactly total positivity in (5.158). This proves both inclusions in (5.159), and substitution in (5.146) proves the last assertion. \(\square\)

### Algebraic Gauss normalization of the rational frame

The positivity calculation in Theorem 5.46 treated symplectic characters. We now define the Gauss normalization on the whole character ring and prove its Galois law. This supplies the rational factor that can be removed in the determinant class quotient. The law agrees with [Fröhlich, Section 2, Theorem 3]; the proof below uses the already proved local constants and reciprocity maps.

We keep the positive exponential additive character of Lemma 5.41. The local constant lesson uses geometric reciprocity, the inverse of arithmetic reciprocity. If a one-dimensional Galois character is denoted by \(\xi\), write
\[
 \xi_{\mathrm a}(x)=\xi(\operatorname{rec}_{\mathrm{arith},F}(x)),
 \qquad
 \xi_{\mathrm g}(x)=\xi(\operatorname{rec}_{\mathrm{geom},F}(x))
                     =\xi_{\mathrm a}(x)^{-1}.
 \tag{5.160}
\]
The character formulas for the epsilon factor use \(\xi_{\mathrm g}\). The Gauss formulas below use \(\xi_{\mathrm a}\). This inverse is needed even though it disappears on a self-dual character.

Let \(F/\mathbb Q_p\) have residue cardinality \(q_F\), and let \(d_F\) be its absolute different exponent. Thus
\(\mathfrak D_{F/\mathbb Q_p}=\mathfrak p_F^{d_F}\).
Put \(\psi_F=\psi_{\mathbb Q_p}\operatorname{Tr}_{F/\mathbb Q_p}\), and use the measure \(dx_0\) of integral-ring volume one. For a finite-image representation \(V\), or its virtual class, define
\[
 \tau_F(V)=q_F^{-d_F\dim V}
                   \epsilon_F(0,V,\psi_F,dx_0).
 \tag{5.161}
\]
Both factors are multiplicative under direct sums, so the definition extends to virtual characters.

**Lemma 5.58 (the algebraic local Gauss constant).** The value in (5.161) is a nonzero algebraic number. For a one-dimensional character \(\xi\) it is
\[
 \begin{aligned}
 \tau_F(\xi)&=\xi_{\mathrm a}(\pi_F)^{-d_F},
                       &&a_F(\xi)=0,\\
 \tau_F(\xi)&=\xi_{\mathrm a}(c)^{-1}
       \sum_{u\in(\mathcal O_F/\mathfrak p_F^{a_F(\xi)})^\times}
                 \xi_{\mathrm a}(u)\psi_F(u/c),
                       &&a_F(\xi)>0,
 \end{aligned}
 \tag{5.162}
\]
where \(v_F(c)=a_F(\xi)+d_F\). The second formula is independent of the residue representatives and of the choice of \(c\). For every finite-image \(V\),
\[
 \tau_F(V)=q_F^{a_F(V)/2}W_F(V,\psi_F),
 \qquad
 |\tau_F(V)|=q_F^{a_F(V)/2}.
 \tag{5.163}
\]
The positive square root fixes the meaning of the first factor.

**Proof.** The annihilator of \(\mathcal O_F\) under \(\psi_F(xy)\) is its trace-dual module \(\mathfrak D_{F/\mathbb Q_p}^{-1}\). Indeed the canonical character of \(\mathbb Q_p\) is trivial exactly on \(\mathbb Z_p\), so annihilation says precisely that \(\operatorname{Tr}(x\mathcal O_F)\subseteq\mathbb Z_p\). The trace-dual different calculation in Three differents identifies that module. Consequently the integer \(n_F(\psi_F)\) of the local constant lesson is \(d_F\).

Algebraicity and nonvanishing now follow from Lemma 5.41 and (5.161). Equations (9) and (9A) of Local L-factors and epsilon factors, Lemma 2.1, evaluated with \(\xi_{\mathrm g}\), give (5.162) after division by \(q_F^{d_F}\). This is a direct use of their proved finite-sum formulas, with (5.160) converting the character. If a representative \(u\) changes by \(\mathfrak p_F^{a_F(\xi)}\), its character value is unchanged, and its additive argument changes by \(\mathfrak p_F^{-d_F}\), on which \(\psi_F\) is trivial. Replacing \(c\) by \(ct\), \(t\in\mathcal O_F^\times\), and replacing the residue variable by \(tu\) cancels the two factors \(\xi_{\mathrm a}(t)\). This proves the asserted independence. In the unramified case the value on a uniformizer does not depend on its choice.

The exponent and self-dual measure calculation giving (5.121) applies to every finite-image unitary representation, without the symplectic hypothesis. Averaging a positive Hermitian form makes such a representation unitary. It gives
\(W_F(V)=\epsilon_F(0,V,\psi_F,dx_0)q_F^{-a_F(V)/2-d_F\dim V}\).
Substitution proves (5.163), and the proved unitary absolute value of \(W_F\) proves its second equality. Multiplicativity proves the formulas for virtual representations too. \(\square\)

For a finite Galois extension \(L/K\) with group \(G\), define
\[
 \tau_K(\chi)=\prod_{v\text{ finite}}\tau_{K_v}
                       (\operatorname{Res}_{D_v}^G\chi).
 \tag{5.164}
\]
Here \(D_v\) is a decomposition group, embedded by a chosen prime above \(v\). Changing that prime conjugates the representation and changes no factor. Almost every factor is one: outside the finitely many primes ramified in \(L/K\) or \(K/\mathbb Q\), the representation is unramified and \(d_{K_v}=0\); decomposing its unramified cyclic representation into character lines and applying the first formula in (5.162) gives one. Thus (5.164) is a finite product of algebraic numbers and is a homomorphism on \(R_G\).

**Theorem 5.59 (global Galois covariance).** Let \(\Omega_{\mathbb Q}=\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)\), \(\Omega_K=\operatorname{Gal}(\overline{\mathbb Q}/K)\), and
\(\operatorname{Ver}_{K/\mathbb Q}:\Omega_{\mathbb Q}^{\mathrm{ab}}\to\Omega_K^{\mathrm{ab}}\)
be transfer. Evaluate its image on \(\det\chi\) through the abelianization of \(G\). Then
\[
 \sigma(\tau_K(\chi))=
      \tau_K(\chi^\sigma)
      \det\chi^\sigma(\operatorname{Ver}_{K/\mathbb Q}\sigma)
                 \qquad(\sigma\in\Omega_{\mathbb Q}).
 \tag{5.165}
\]
In particular this is the same covariance law as the normed resolvent \(R_a\).

**Proof: local covariance.** Lemma 5.41 supplies the cyclotomic unit \(u_{\sigma,p}\in\mathbb Z_p^\times\), characterized by \(\sigma(\zeta_{p^r})=\zeta_{p^r}^{u_{\sigma,p}}\). Its conjugated additive character is \(\psi_F(u_{\sigma,p}x)\). The rational factor in (5.161) is fixed by \(\sigma\). Apply (5.118), then the proved additive-character formula (13) of the local constant lesson. Because \(u_{\sigma,p}\) is a unit, its absolute value is one. The result is
\[
 \sigma(\tau_F(V))=\tau_F(V^\sigma)
         \det V^\sigma(\operatorname{rec}_{\mathrm{geom},F}(u_{\sigma,p})).
 \tag{5.166}
\]
This proof includes arbitrary finite-image representations; it does not presume a monomial decomposition or a parity of their conductor.

**Proof: the product of the determinant factors.** The compatible unit tuple
\(u_\sigma=(u_{\sigma,p})_p\) is an element of \(\widehat{\mathbb Z}^{\times}\). Give it real idèle component 1. Under geometric rational reciprocity its image is exactly the restriction of \(\sigma\) to \(\mathbb Q^{\mathrm{ab}}\). This is the explicit formula (6) in Kronecker–Weber and the maximal abelian extension of the rationals, Proposition 20.3, together with its proved Theorem 20.2. The equality on roots of unity therefore specifies the whole abelianized image, rather than only one cyclotomic subextension.

Include this rational idèle in the idèles of \(K\): at every \(v\mid p\) its component is the scalar \(u_{\sigma,p}\), and at infinity it is 1. Global reciprocity is the product of its local maps, by The global reciprocity law, Theorem 16.4 and Section 5. Inclusion corresponds to transfer, by the full functoriality proof in The reciprocity law and the class field correspondence, Proposition 5.2, equation (11). These statements are written for arithmetic reciprocity; inversion gives the same inclusion/transfer identity for geometric reciprocity. The infinite local components here have symbol one. Hence the product of the determinant factors in (5.166), over the finite places of \(K\), is
\(\det\chi^\sigma(\operatorname{Ver}_{K/\mathbb Q}\sigma)\).
At all but finitely many places this determinant factor is one because units have trivial action in an unramified abelian quotient. Multiplication of (5.166) therefore proves (5.165).

**Proof: compare the normed resolvent.** Choose a finite Galois normal closure \(M/\mathbb Q\) containing \(L\), and representatives \(s_i\) of the left cosets of \(H=\operatorname{Gal}(M/K)\) in \(\Gamma=\operatorname{Gal}(M/\mathbb Q)\). They give the embeddings used in (5.126). For the image \(s\) of \(\sigma\), write
\(ss_i=s_{j(i)}h_i\), \(h_i\in H\).
The embedding factors are permuted by \(i\mapsto j(i)\). On the \(i\)-th factor, reindexing \(g\) by \(h_i g\), with \(h_i\) restricted to \(L\), is exactly the right multiplication in (5.125). Consequently
\[
 \sigma(R_a(\chi))=
      R_a(\chi^\sigma)\prod_i\det\chi^\sigma(h_i)
   =R_a(\chi^\sigma)
      \det\chi^\sigma(\operatorname{Ver}_{K/\mathbb Q}\sigma).
 \tag{5.167}
\]
For completeness the product of the \(h_i\), in \(H^{\mathrm{ab}}\), is the definition of finite transfer. Replacing \(s_i\) by \(s_i k_i\) replaces its factor by \(k_{j(i)}^{-1}h_i k_i\), whose extra factors cancel in the abelian product. The factors for a product \(st\) are the factors for \(s\) at the cosets permuted by \(t\), followed by those for \(t\), so the product is a homomorphism and kills the commutator subgroup. These facts also make transfer compatible on finite quotients and define the displayed profinite transfer. Taking the character determinant of the product gives the last equality in (5.167). This proves the claimed agreement of covariance laws. \(\square\)

**Corollary 5.60 (the positive rational normalization).** With \(a\), \(R_a\) and \(w\) as in (5.126) and (5.120), put
\[
 f_a(\chi)=\frac{w(\chi)R_a(\chi)}{\tau_K(\chi)}.
 \tag{5.168}
\]
Then \(f_a\in P_G^+\). In particular some \(z_a\in\mathbb Q[G]^\times\) satisfies
\[
 \operatorname{Det}(z_a)=f_a.
 \tag{5.169}
\]
Thus (5.169) is an actual rational group-algebra determinant that can be removed in the quotient (5.146).

**Proof.** All three factors in (5.168) are nonzero algebraic homomorphisms on \(R_G\). Theorem 5.42 makes \(w\) equivariant, while (5.165) and (5.167) cancel the two identical transfer factors. Hence \(f_a\) is Galois equivariant.

For symplectic \(\chi\), multiply (5.163) over finite places. The local product formula for the global constant, proved in Artin L-functions, conductors and discriminants, Section 8 through equation (43), gives
\[
 \tau_K(\chi)=W_K(\chi)W_\infty(\chi)^{-1}
                              \sqrt{N_{K/\mathbb Q}\mathfrak f_K(\chi)}.
 \tag{5.170}
\]
This is precisely the symplectic normalization already used in (5.132), now obtained from the algebraic definition on all characters. The square root is positive. Theorem 5.46 proves that (5.168) is positive at every embedding of \(\mathbb Q(\chi)\). It therefore satisfies the positivity requirement in (5.158). Theorem 5.57 gives (5.169). \(\square\)

For example, let \(L=\mathbb Q(\zeta_7)\), \(K=\mathbb Q\), and \(a=\zeta_7\). Write \(\sigma_u(\zeta_7)=\zeta_7^u\) for \(u\in(\mathbb Z/7\mathbb Z)^\times\). The six conjugates of \(a\) are an integral basis: the cyclotomic integer-ring theorem gives the basis \(1,\zeta_7,\ldots,\zeta_7^5\), and \(1=-\sum_{u=1}^6\zeta_7^u\) changes it to the conjugate basis by an integral matrix of determinant a unit. Thus it is also a normal basis. The cyclotomic ramification theorem makes every nontrivial character of \(G\) tamely ramified at 7 and unramified elsewhere. At 7 the explicit arithmetic symbol of a unit \(u\) is \(\sigma_u^{-1}\), and that of the uniformizer 7 is the identity; these are the cyclotomic symbol computations in the reciprocity provider used above. Hence (5.162) gives, for every nontrivial character,
\[
 R_a(\chi)=\sum_{u=1}^6\chi(\sigma_u)^{-1}\zeta_7^u
          =\tau_{\mathbb Q}(\chi).
\]
For the trivial character, \(R_a(1)=-1\) whereas \(\tau_{\mathbb Q}(1)=1\). This cyclic group's irreducibles are one-dimensional, so none is symplectic and \(w=1\). Consequently the normalized frame has value \(-1\) on the trivial character and 1 on the others. It is the determinant of the explicit rational unit
\[
 z=1-2e_1,\qquad e_1=\frac16\sum_{g\in G}g,\qquad z^2=1.
\]
Indeed averaging projects onto the trivial representation and is zero on every other simple representation. This checks both the reciprocity inverse and the trivial-character factor in the rational normalization.

The finite-prime comparison still has to determine the integral determinant represented by a normal integral basis resolvent divided by (5.164). Corollary 5.60 supplies its rational normalization; it does not substitute for that local arithmetic comparison.

### Tame inertia and adjusted Gauss sums

The local determinant comparison uses a Gauss sum whose value is unchanged by an unramified twist. We construct it and prove its character-field properties, including the permutation sign in induction. These are the formulas in [Taylor, Section 3, equations (3.9) and (3.12)–(3.13)], with the reciprocity convention made explicit in (5.160).

Throughout this calculation \(F/\mathbb Q_p\) is finite, \(K/F\) is finite tame Galois, and \(d_E\) denotes the absolute different exponent of an intermediate field \(E\). We use the algebraic local Gauss constant (5.161).

**Lemma 5.61 (degree-zero Gauss induction).** If \(E/F\) is finite and \(U\) is a virtual finite-image representation of degree zero over \(E\), then
\[
 \tau_F(\operatorname{Ind}_{E/F}U)=\tau_E(U).
 \tag{5.171}
\]
Also \(\tau_F(1)=1\), and inflation to a larger finite Galois quotient over the same base field preserves the constant.

**Proof.** The trace character \(\psi_F\operatorname{Tr}_{E/F}\) is the canonical \(\psi_E\). Both \(\dim U\) and \(\dim\operatorname{Ind}U\) are zero, so the normalizing powers in (5.161) are one. The proved degree-zero epsilon induction in Local L-factors and epsilon factors, Theorem 3.0, gives (5.171); virtual degree zero also makes the measure choices immaterial. The trivial-line value follows from (5.162). Inflation is the same absolute Galois representation in (5.161), with the same dimension and additive character. \(\square\)

#### A common different generator

Fix a finite tame Galois extension \(K/F\), with group \(G\) and inertia \(I\), and choose once and for all
\[
 c\in F^\times,\qquad c\mathcal O_F=\mathfrak p_F\mathfrak D_F.
 \tag{5.172}
\]
For every \(F\subset E\subset K\), the same element satisfies
\[
 c\mathcal O_E=\mathfrak p_E\mathfrak D_E.
 \tag{5.173}
\]

Indeed the different in a tower gives
\(\mathfrak D_E=\mathfrak D_{E/F}\mathfrak D_F\mathcal O_E\), and tameness gives
\(v_E(\mathfrak D_{E/F})=e(E/F)-1\). Hence, writing \(e=e(E/F)\),
\[
 v_E(c)=e(d_F+1)
       =1+(e-1)+e d_F
       =1+d_E.
\]
These equal valuations prove (5.173). The tower identity has its trace-dual adjunction proof in Artin L-functions, conductors and discriminants, Section 3, equations (11)–(12). The tame exponent has its full proof in Three differents, Theorem 5.3.

For \(H\leq G\), with \(E=K^H\), let \(\delta_{c,H}\in H\) have image
\(\operatorname{Art}^{\mathrm a}_E(c)\) in \(H^{\mathrm{ab}}\). Equivalently, use the symbol of the maximal abelian subextension of \(K/E\). For a representation \(U\) of \(H\), its determinant is an abelian character, so
\[
 \operatorname{Det}(\delta_{c,H})(U)
   =\det U(\operatorname{Art}^{\mathrm a}_E(c))
 \tag{5.174}
\]
is independent of the choice of representative \(\delta_{c,H}\).

#### Cyclic inertia and the irreducible weight spaces

We first justify the tame local facts that \(I\) is cyclic and \(G/I\) is cyclic. Lemma 4.B proves that the integer ring of a finite characteristic-zero local extension is finite, free, and a complete DVR, with unique extended valuation. The degree formula \( [K:F]=ef \) follows directly: if \(S/R\) are its integer rings, the free rank is \([K:F]\), whereas the filtration of \(S/\pi_F S=S/\pi_K^e S\) has \(e\) quotients equal to \(k_K\), each of dimension \(f\) over \(k_F\). This proves the formula by comparing dimensions.

**Local structural calculation.** First, the multiplicative group of a finite field is cyclic. Let \(M\) be the least common multiple of the orders of its elements. In a finite abelian group there is an element of order \(M\): for each prime take an element whose order has the largest power of that prime, project to its primary part by taking a suitable power, and multiply these primary elements. Every element of the field's multiplicative group is a root of \(X^M-1\), so the polynomial root bound gives its order at most \(M\); the reverse inequality follows from the element just constructed. It therefore generates the group.

Choose a generator of \(k_K^\times\), which in particular generates \(k_K/k_F\), lift its monic separable minimal polynomial to \(\mathcal O_F[X]\), and apply the following simple-root lifting in \(\mathcal O_K\). Starting at a residue lift \(u_0\), iterate
\(u_{j+1}=u_j-h(u_j)/h'(u_j)\). The derivative remains a unit and the error valuation at least doubles, so completeness gives a root \(u\). A root with this residue is unique, since
\(h(v)-h(u)=(v-u)(h'(u)+(v-u)w)\).
The lifted polynomial is irreducible: a proper monic factorization over \(F\) would be integral, by the unique valuation and integrality of all its roots, and reduce to a proper factorization of the residue polynomial. Thus \(F_0=F(u)\) has degree \(f=[k_K:k_F]\), the same residue field as \(K\), and ramification index one. Every element of \(I\) fixes \(u\) by uniqueness of the root with its residue.

If \(\pi\) is a uniformizer of \(K\), its valuation has denominator \(e=[K:F_0]\) when measured in \(F_0\). Hence \([F_0(\pi):F_0]\geq e\), and therefore \(K=F_0(\pi)\). Moreover
\(\mathcal O_K=\mathcal O_{F_0}[\pi]\): residue representatives from \(\mathcal O_{F_0}\), multiplied by \(1,\pi,\ldots,\pi^{e-1}\), span
\(\mathcal O_K/\mathfrak p_{F_0}\mathcal O_K=\mathcal O_K/(\pi^e)\); apply Nakayama to the finite quotient module.

Define
\[
 t:I\longrightarrow k_K^\times,\qquad
 t(\sigma)=\overline{\sigma(\pi)/\pi}.
 \tag{5.175}
\]
It is a homomorphism because inertia acts trivially on \(k_K\). Its kernel is
\(N_1=\{\sigma:\sigma(\pi)\equiv\pi\pmod{\pi^2}\}\).
For \(r\geq1\), let
\(N_r=\{\sigma:\sigma(\pi)\equiv\pi\pmod{\pi^{r+1}}\}\).
The map
\[
 N_r/N_{r+1}\longrightarrow(k_K,+),\qquad
 \sigma\longmapsto
      \overline{(\sigma(\pi)-\pi)/\pi^{r+1}}
 \tag{5.176}
\]
is injective and additive. For additivity, write
\(\sigma\tau(\pi)-\pi=\sigma(\tau(\pi)-\pi)+\sigma(\pi)-\pi\);
after division by \(\pi^{r+1}\), inertia fixes the residue coefficient and
\((\sigma(\pi)/\pi)^{r+1}\) has residue one. The groups eventually become trivial: \(I\) is finite and an element fixing \(\pi\) and \(F_0\) fixes \(K\). Consequently \(N_1\) is a \(p\)-group.

The reduction map \(G\to\operatorname{Gal}(k_K/k_F)\) is surjective. Each residue Frobenius image of \(u\) is the residue of a unique root of \(h\) in \(K\) by the same lifting calculation. The resulting \(F\)-embedding of \(F_0\) extends to an \(F\)-automorphism of the normal separable \(K\). Thus \(|I|=e\) and \(G/I\) is the cyclic residue Galois group. Tameness makes \(e\) prime to \(p\), so \(N_1=1\), and (5.175) injects \(I\) into \(k_K^\times\).

The finite-field calculation at the start shows that \(k_K^\times\) is cyclic. A subgroup of a cyclic group is cyclic, proving the assertion for \(I\).

The same residue-lifting argument for \(K/E\), for any \(E=K^H\), gives residue quotient \(H/(H\cap I)\). Residue degrees in a field tower multiply, so
\[
 f(E/F)=\frac{|G/I|}{|H/(H\cap I)|}
        =[G:IH].
 \tag{5.177}
\]
This also verifies the residue degree used in the induction proof below, including nonnormal \(H\).

The next argument is entirely a finite-group calculation and applies to every group with cyclic normal \(I\) and cyclic \(G/I\).

**Lemma 5.62 (the monomial description).** Let \(V\) be an irreducible characteristic-zero representation of a finite group \(G\), with cyclic normal subgroup \(I\) and cyclic quotient \(G/I\). There are a subgroup \(H\) containing \(I\) and a one-dimensional character \(\alpha\) of \(H\) such that
\[
 \chi_V=\operatorname{Ind}_H^G\alpha.
 \tag{5.178}
\]
One may take \(H\) to be the stabilizer of a character \(\theta\) of \(I\) occurring in \(V|_I\). Then \(H\) is normal in \(G\), and
\[
 \chi_V|_I=\sum_{g\in G/H}\theta^g
 \tag{5.179}
\]
is a sum of distinct characters, each of multiplicity one. Here
\(\theta^g(i)=\theta(gig^{-1})\); replacing \(g\) by its inverse only reindexes this sum. If \(\theta=1\), then \(H=G\) and \(V\) is an unramified line.

**Proof.** A generator of \(I\) has finite order, so it is diagonalizable in characteristic zero. Decompose
\[
 V=\bigoplus_\theta V_\theta,\qquad
 V_\theta=\{v:iv=\theta(i)v\text{ for every }i\in I\}.
\]
The \(G\)-action permutes the nonzero weight spaces. The sum over any orbit is \(G\)-invariant, so irreducibility makes the occurring weights a single orbit.

Let \(H\) stabilize an occurring \(\theta\). It contains \(I\), and is normal because it is the inverse image of a subgroup of the abelian group \(G/I\). The space \(V_\theta\) is irreducible for \(H\): if \(0\ne W\subsetneq V_\theta\) were \(H\)-invariant, the sum of its \(G/H\)-translates would be a nonzero proper \(G\)-subrepresentation. The sum is direct because its terms have different \(I\)-weights.

Choose \(t\in H\) generating \(H/I\). On \(V_\theta\), \(I\) acts by scalars and \(t\) is diagonalizable, since it has finite order. An eigenline for \(t\) is therefore \(H\)-invariant. Irreducibility forces \(V_\theta\) itself to be that line. Its character is \(\alpha\), extending \(\theta\). The map
\(\mathbb C[G]\otimes_{\mathbb C[H]}V_\theta\to V\),
\(g\otimes v\mapsto gv\), identifies its coset summands with all the distinct weight lines. It is an isomorphism, proving both assertions. If \(\theta=1\), every conjugate weight is trivial and the irreducible representation factors through the cyclic group \(G/I\), so it is a line. \(\square\)

For this \(H\), \(E/F\) is unramified cyclic of degree
\[
 m=[G:H].
 \tag{5.180}
\]
The residue degree is \(m\), because \(H\) contains \(I\), and its ramification index is one. In particular \(d_E=d_F\), and \(q_E=q_F^m\).

#### The unramified correction

Let \(\phi_F\) denote arithmetic Frobenius in \(G/I\), and choose any lift to \(G\). For an actual representation \(V\) define
\[
 y_G(V)=(-1)^{\dim V^I}
          \det(\phi_F\mid V^I).
 \tag{5.181}
\]
The formula is independent of the lift because \(I\) acts trivially on \(V^I\). Extend it multiplicatively to virtual representations. Inertia is normal, so \(V^I\) is \(G\)-stable. On an irreducible ramified representation this space is zero and \(y_G=1\). On an unramified irreducible, a line, the formula is
\[
 y_G(\alpha)=-\alpha_{\mathrm a}(\pi_F)
            =-\alpha_{\mathrm a}(\mathfrak p_F).
 \tag{5.182}
\]
Thus (5.181) gives exactly Taylor's correction, including the minus sign.

**Lemma 5.63 (induction invariance of \(y\)).** For every subgroup \(H\leq G\), \(E=K^H\), and every virtual character \(U\) of \(H\),
\[
 y_G(\operatorname{Ind}_H^G U)=y_H(U).
 \tag{5.183}
\]

**Proof.** Put \(I_H=H\cap I\) and \(r=[G:IH]=f(E/F)\). In the coset tensor model,
\((\operatorname{Ind}_H^G U)^I\) has one copy of \(U^{I_H}\) per \(I\)-orbit on \(G/H\). An invariant vector on an orbit is determined by its value at a selected coset, and invariance at its stabilizer is precisely the condition that this value belong to \(U^{I_H}\). The \(I\)-orbits are indexed by the \(r\) cosets of \(IH/I\) in \(G/I\).

Arithmetic Frobenius cyclically permutes these \(r\) copies. After one cycle its action on a selected copy is arithmetic Frobenius of \(E\), modulo \(I_H\), since it has degree \(r\) on the residue field of \(F\). If \(d=\dim U^{I_H}\) and \(A\) is that return matrix, the Frobenius matrix on the full invariant space is a cyclic block matrix with determinant
\[
 (-1)^{(r-1)d}\det A.
 \tag{5.184}
\]
This can be checked by choosing the bases in successive copies so that all transition maps except the last are identities; the block cycle has permutation sign \((-1)^{(r-1)d}\), and the final block is \(A\). Formula (5.181) consequently gives
\[
 (-1)^{rd}(-1)^{(r-1)d}\det A
  =(-1)^d\det A
  =y_H(U).
\]
Additivity of invariant-space dimension and multiplicativity of determinant extend the assertion to virtual \(U\). \(\square\)

In the slightly delicate nonnormal case, the return map is well defined modulo \(I_H\): \(IH\) is the inverse image of a subgroup of the cyclic \(G/I\). For a Frobenius lift \(\phi\), write \(\phi^r=ih\) with \(i\in I,h\in H\). On the selected \(I\)-orbit its return map is \(h\), whose image in the residue quotient of \(H\) is the \(r\)-th arithmetic power of \(\phi\). This is the arithmetic Frobenius of \(E\).

The correction takes root-of-unity values and is Galois-equivariant. Lemma 5.62 realizes every irreducible by induced matrices with root-of-unity entries. Inertia invariants are the image of the rational averaging idempotent \(|I|^{-1}\sum_{i\in I}i\); applying a field automorphism preserves its rank and conjugates the determinant in (5.181). The sign is unchanged. Direct sums and quotients of values extend the conclusion to all virtual characters.

For a symplectic representation \(V\), the restriction of its invariant alternating form to \(V^I\) is nondegenerate. Indeed the averaging projection is self-adjoint for that form. Hence \(V^I\) has even dimension and Frobenius preserves a nondegenerate alternating form there, with determinant one. Thus \(y_G(V)=1\). These are the same averaging and top-exterior-power calculations as the independently written Gauss/root-sign fragment, Lemma 5.40.

#### The adjusted sum and its induction sign

**Theorem 5.64 (the adjusted tame Gauss sum).** Define the adjusted local homomorphism by
\[
 \tau^*_{H,c}(U)=
     \tau_E(U)y_H(U)^{-1}
     \det U(\operatorname{Art}^{\mathrm a}_E(c)),
 \qquad E=K^H.
 \tag{5.185}
\]
This is Taylor (3.9), with \(\delta_{c,H}\) as in (5.174). The subscript \(c\) records the fixed choice of different generator.

For an irreducible \(\chi=\operatorname{Ind}_H^G\alpha\) as in Lemma 5.62, with \(m=[G:H]\), the adjusted value is \((-1)^{m+1}\tau^*_{H,c}(\alpha)\). If \(\alpha\) is ramified, this last constant is its residue-field Gauss sum (5.194); if \(\chi\) is unramified, its adjusted value is \(-1\). Every adjusted value is a unit away from the residue characteristic \(p\).

**Proof: the induction sign.** Take an irreducible \(\chi=\operatorname{Ind}_H^G\alpha\) from Lemma 5.62, and let
\(\rho=\operatorname{Ind}_H^G1\). This is the regular representation of the cyclic unramified quotient \(G/H\), inflated to \(G\). Apply (5.171) to the degree-zero line difference \(\alpha-1\), and multiply out:
\[
 \frac{\tau_F(\chi)}{\tau_F(\rho)}
       =\frac{\tau_E(\alpha)}{\tau_E(1)}
       =\tau_E(\alpha),
 \qquad
 \tau_F(\chi)=\tau_E(\alpha)\tau_F(\rho).
 \tag{5.186}
\]
This proves Taylor (3.11), with the trivial-line factor accounted for.

Let \(P=\det\rho\). Arithmetic Frobenius is an \(m\)-cycle on the regular basis, so
\[
 P(\phi_F)=(-1)^{m-1}.
 \tag{5.187}
\]
All constituents of \(\rho\) are unramified lines. Their Gauss factors (5.162) multiply to
\[
 \tau_F(\rho)=P(\phi_F)^{-d_F}
             =(-1)^{(m-1)d_F}
             =\tau_F(P).
 \tag{5.188}
\]
One can also derive this directly from the epsilon induction constant. The regular constituents give
\(\epsilod_F(\rho)=P(\phi_F)^{-d_F}q_F^{md_F}\),
while \(\epsilod_E(1)=q_E^{d_E}=q_F^{md_F}\).
Their quotient is \(P(\phi_F)^{-d_F}\). The two normalizations in (5.161) have equal powers for this unramified \(E/F\), so the same factor is the full Gauss induction constant.

The determinant of an induced line is
\[
 \det\chi=(\alpha\circ\operatorname{Ver}_H^G)P.
 \tag{5.189}
\]
Here is the calculation: choose coset representatives \(t_j\) and write
\(g t_j=t_{\sigma_g(j)}h_j(g)\). The induced matrix is a monomial matrix with determinant
\(\operatorname{sgn}(\sigma_g)\prod_j\alpha(h_j(g))\). The abelianized product of the \(h_j(g)\) is transfer, and \(\operatorname{sgn}(\sigma_g)=P(g)\). This proves (5.189), including its sign.

Arithmetic reciprocity identifies transfer with inclusion \(F^\times\hookrightarrow E^\times\). Evaluating (5.189) at the symbol of \(c\) therefore gives
\[
 \det\chi(\operatorname{Art}^{\mathrm a}_F(c))
       =\alpha_{\mathrm a,E}(c)P(\operatorname{Art}^{\mathrm a}_F(c)).
 \tag{5.190}
\]
The exact inclusion/transfer proof is The reciprocity law and the class field correspondence, Proposition 5.2, equation (11), including its earlier coset proof in Proposition 4.4. Its local realization is Local reciprocity and norm groups, Theorem 6.3. Inverting both symbols preserves the transfer diagram and supplies the provider's geometric version as well.

Since \(P\) is unramified and \(v_F(c)=d_F+1\),
\[
\begin{aligned}
 P(\operatorname{Art}^{\mathrm a}_F(c))\tau_F(\rho)
  &=P(\phi_F)^{d_F+1}P(\phi_F)^{-d_F}\\
  &=P(\phi_F)=(-1)^{m-1}=(-1)^{m+1}.
\end{aligned}
 \tag{5.191}
\]
Combine (5.183), (5.185), (5.186), (5.190), and (5.191):
\[
 \boxed{\tau^*_{G,c}(\chi)
       =(-1)^{m+1}\tau^*_{H,c}(\alpha).}
 \tag{5.192}
\]
This proves Taylor (3.12) from the epsilon provider and the displayed determinant computation. Neither the different exponent nor the permutation determinant has been silently omitted.

#### The residue-field Gauss formula

If \(\alpha\) is ramified, tameness makes its conductor exponent one. To verify this also on the multiplicative character, the successive quotients \( (1+\mathfrak p_E^r)/(1+\mathfrak p_E^{r+1})\) are additive residue groups: multiplication gives the sum modulo the next ideal. A continuous character with finite image has a kernel containing one such higher unit group. Its image on \(1+\mathfrak p_E\) is therefore a finite \(p\)-group. Units map into the prime-to-\(p\) tame abelian inertia group, so that image is trivial. A ramified line is nontrivial on some unit, and hence its conductor exponent is exactly one. Its arithmetic multiplicative character is trivial on \(1+\mathfrak p_E\), and descends to a nontrivial character
\(\bar\alpha:k_E^\times\to\overline{\mathbb Q}^\times\). By (5.173),
\[
 \bar\psi_{E,c}(\bar u)=\psi_E(u/c)
 \tag{5.193}
\]
is a well-defined nontrivial additive character of \(k_E\). Well-definedness follows because
\(\mathfrak p_E/c=\mathfrak D_E^{-1}\), on which \(\psi_E\) is trivial. If it were trivial on all of \(\mathcal O_E/c\), the annihilator of \(\mathcal O_E\) would contain \(c^{-1}\mathcal O_E\), strictly larger than \(\mathfrak D_E^{-1}\), contradicting its definition. Since \(k_E\) has characteristic \(p\), its additive character values are \(p\)-th roots of unity.

Now \(y_H(\alpha)=1\), and multiplication by the determinant correction \(\alpha_{\mathrm a,E}(c)\) in (5.185) cancels exactly the inverse factor in (5.162). Thus
\[
\begin{aligned}
 \tau^*_{H,c}(\alpha)
   &=\sum_{\bar u\in k_E^\times}
       \bar\alpha(\bar u)\bar\psi_{E,c}(\bar u),\\
 \boxed{\tau^*_{G,c}(\chi)}
   &\boxed{=(-1)^{m+1}
       \sum_{\bar u\in k_E^\times}
          \bar\alpha(\bar u)\bar\psi_{E,c}(\bar u).}
\end{aligned}
 \tag{5.194}
\]
This is Taylor (3.13), with units as the summation domain. If writing a sum over all of \(k_E\), extend \(\bar\alpha(0)=0\), also for the trivial character.

For an unramified irreducible \(\chi\), Lemma 5.62 makes \(m=1\), \(H=G\), and (5.162), (5.182), (5.185) give
\[
 \tau^*_{G,c}(\chi)
   =\chi_{\mathrm a}(\pi_F)^{-d_F}
     (-\chi_{\mathrm a}(\pi_F))^{-1}
     \chi_{\mathrm a}(c)
   =-1.
 \tag{5.195}
\]
The last equality uses \(v_F(c)=d_F+1\). It is valid even when the unramified character itself has large finite order.

The sums in this formula are nonzero algebraic integers and units at every finite place of residue characteristic other than \(p\), by the full inverse-product calculation in Lemma 5.37. The unramified value \(-1\) has the same property. Multiplicativity proves this unit assertion for the adjusted sum on all virtual characters.

#### Character fields and unramified twists

Put \(C=\mathbb Q(\theta)\), the field generated by the values of the inertia weight in Lemma 5.62. Conjugation induces an injective map
\[
 \Sigma=G/H\hookrightarrow\operatorname{Gal}(C/\mathbb Q).
 \tag{5.196}
\]
Indeed a generator \(i_0\) of \(I\) has \(\theta(i_0)\) a root of unity; every conjugation automorphism of \(I\) raises \(i_0\) to a unit power, and therefore acts by that power on this root. Its kernel on \(C\) is exactly the stabilizer \(H\) of \(\theta\).

**Lemma 5.65 (the orbit character field).**
\[
 \mathbb Q(\chi|_I)=C^\Sigma.
 \tag{5.197}
\]

**Proof.** Formula (5.179) makes every value of \(\chi|_I\) fixed by \(\Sigma\). Conversely an automorphism of \(C/\mathbb Q\) fixing every such value must send the set of occurring weights to itself. To check this last step without an irreducibility criterion, characters of the cyclic group \(I\) are linearly independent: multiply a claimed linear relation by the inverse of one character and sum over \(I\); the geometric-series identity makes all other sums zero and the selected sum \(|I|\). Equality of the two orbit sums therefore means equality of their sets of weights. An automorphism carrying \(\theta\) into its \(\Sigma\)-orbit belongs to \(\Sigma\), because the values of \(\theta\) generate \(C\). Thus the stabilizer of \(\mathbb Q(\chi|_I)\) in \(\operatorname{Gal}(C/\mathbb Q)\) is exactly \(\Sigma\). Galois correspondence proves (5.197). \(\square\)

**Proposition 5.66 (field of values and twists).** For every irreducible tame local character \(\chi\),
\[
 \tau^*_{G,c}(\chi)\in
       \mathbb Q(\zeta_p)\,\mathbb Q(\chi|_I).
 \tag{5.198}
\]
For every unramified one-dimensional character \(\nu\) of \(G\), and every virtual character \(\chi\),
\[
 \tau^*_{G,c}(\nu\chi)=\tau^*_{G,c}(\chi).
 \tag{5.199}
\]
For every \(\omega\in\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q(\zeta_p))\),
\[
 \tau^*_{G,c}(\chi^\omega)
      =\omega(\tau^*_{G,c}(\chi)).
 \tag{5.200}
\]

**Proof of the field assertion.** In the ramified case, local reciprocity takes units onto the inertia subgroup of the maximal abelian quotient of \(H\). Consequently the values of \(\bar\alpha\) generate \(C=\mathbb Q(\theta)\), and (5.194) lies in \(T=\mathbb Q(\zeta_p)C\). The subgroup \(H\) is normal, so \(g\in G/H\) acts as an \(F\)-automorphism on \(E\). Equivariance of arithmetic reciprocity gives
\[
 \alpha_{\mathrm a,E}(g u)
   =\alpha(g\,\operatorname{Art}^{\mathrm a}_E(u)g^{-1}).
 \tag{5.201}
\]
If \(\sigma_g\in\Sigma\) is the associated automorphism of \(C\), then, on unit values,
\(\sigma_g(\alpha_{\mathrm a,E}(u))=\alpha_{\mathrm a,E}(g u)\).
The trace character is invariant under \(g\), and \(g(c)=c\), so
\[
 \psi_E(g u/c)=\psi_E(u/c).
 \tag{5.202}
\]

The unit-image assertion used here also has a short deduction from the proved reciprocity inputs. Let \(B/E\) be the maximal abelian subextension of \(K/E\), with residue degree \(f_B\). Units have trivial symbol in the unramified quotient by Proposition 6.4, so their symbols belong to inertia. Conversely, for an inertia element choose \(x\in E^\times\) having that symbol by Theorem 6.3. Its image in the unramified quotient is trivial, hence \(v_E(x)=t f_B\). The norm of a uniformizer of \(B\) raised to \(t\) has that valuation, because \(v_E(N_{B/E}z)=f_Bv_B(z)\), and its symbol is trivial. Dividing \(x\) by this norm produces a unit with the same inertia symbol. Thus units map onto inertia. The norm-valuation identity is the multiplication-matrix norm identity, or the proved arithmetic valuation calculation in the local-reciprocity lesson §1.

Now let an automorphism of \(T\) fix
\(\mathbb Q(\zeta_p)C^\Sigma\). Its restriction to \(C\) is some \(\sigma_g\), and it fixes every additive-character value in (5.193). Applying it to (5.194), then substituting \(v=g u\) in the finite residue-field sum and using (5.202), leaves the sum unchanged. Thus the sum is fixed by
\(\operatorname{Gal}(T/\mathbb Q(\zeta_p)C^\Sigma)\); finite Galois correspondence and (5.197) prove (5.198). This argument does not presume linear disjointness of the two cyclotomic fields. In the unramified case (5.195) is rational, proving the same assertion.

**Proof of twist invariance.** The coset tensor model gives the projection formula
\[
 \nu\otimes\operatorname{Ind}_H^G\alpha
       \simeq\operatorname{Ind}_H^G
                         (\alpha\otimes\nu|_H).
 \tag{5.203}
\]
An explicit intertwiner sends
\(v\otimes(g\otimes a)\) to
\(\nu(g)^{-1}g\otimes(v\otimes a)\).
The relation \(gh\otimes a=g\otimes\alpha(h)a\) and the scalar \(\nu(h)\) on the right make it balanced over \(H\); applying \(g_0\in G\) on both sides gives the same value, since
\(\nu(g_0)\nu(g_0g)^{-1}=\nu(g)^{-1}\).
Since \(\nu\) is trivial on inertia, the inertia weight, its stabilizer \(H\), and \(m=[G:H]\) are unchanged. Its arithmetic character over \(E\) is trivial on \(\mathcal O_E^\times\), so the unit values in (5.194) are unchanged. Formula (5.194) proves (5.199) for every ramified irreducible. An unramified irreducible and its twist are both unramified lines and both have adjusted value \(-1\) by (5.195). Tensoring with a line permutes the irreducible basis, and multiplicativity extends the result to all virtual characters.

**Proof of covariance.** The induced matrices from Lemma 5.62 have root-of-unity entries, and applying \(\omega\) to them realizes
\(\chi^\omega=\operatorname{Ind}_H^G\alpha^\omega\).
The stabilizer of \(\theta^\omega\) is the same \(H\): equality of two conjugate weights is equivalent to equality of the original weights. These induced matrices are again irreducible. Their restriction to \(I\) has distinct one-dimensional weight spaces, transitively permuted by \(G\). An invariant subspace decomposes into a subset of these lines by the cyclic spectral projections, and transitivity makes that subset empty or full. Thus the same \(m\) and the same formula (5.194) apply. Its arithmetic character values become their \(\omega\)-conjugates, and \(\omega\) fixes the additive-character values because they are in \(\mathbb Q(\zeta_p)\). Applying \(\omega\) term by term proves (5.200) in the ramified case; (5.195) gives the unramified case. Again multiplicativity gives the assertion on the full virtual representation group. \(\square\)

The remaining Taylor comparison must realize these homomorphisms by integral group-algebra determinants and compare them with the integral resolvent. The formulas above establish their values and transformation laws; they do not presume that realization.

## 6. Four computations

For \(\mathbb Q(i)\), the trace of \(a+bi\) is \(2a\), so its image on \(\mathbb Z[i]\) is \(2\mathbb Z\). The prime two is wild, with \(e=2\), and there is no localized normal integral basis there. In fact for any proposed generator \(a+bi\), the determinant of it and its conjugate in the basis \(1,i\) is \(-2ab\), never a unit over \(\mathbb Z\) or \(\mathbb Z_{(2)}\).

For \(\mathbb Q(\sqrt{-3})\), let \(\omega=(1+\sqrt{-3})/2\). Its conjugate is \(1-\omega\). These two elements have coefficient determinant \(-1\) in \(1,\omega\), so they give a global normal integral basis, hence one locally at three. Their trace is one. At three, \(e=2\) is prime to three, and the different \((\sqrt{-3})\) has exponent \(e-1=1\).

For an odd prime \(p\), the conjugates of \(\zeta_p\) are \(\zeta_p,\ldots,\zeta_p^{p-1}\). The usual power basis of \(\mathbb Z[\zeta_p]\) is \(1,\zeta_p,\ldots,\zeta_p^{p-2}\), and

\[
 \zeta_p^{p-1}=-1-\zeta_p-\cdots-\zeta_p^{p-2}.
\]

The change of basis has determinant \(\pm1\). The complete cyclotomic integer-basis proof is Cyclotomic fields, Theorem 12.2; it identifies this order with the full integer ring [Milne ANT, Chapter 6]. Thus \(\zeta_p\) is a global normal integral basis generator. At \(p\), the index of ramification is \(p-1\), which is tame.

For the cyclic cubic field inside \(\mathbb Q(\zeta_7)\), take

\[
 \eta_1=\zeta_7+\zeta_7^{-1},\quad
 \eta_2=\zeta_7^2+\zeta_7^{-2},\quad
 \eta_3=\zeta_7^3+\zeta_7^{-3}.
\]

Cyclotomic multiplication gives \(\eta_1+\eta_2+\eta_3=-1\), pairwise sum of products \(-2\), and product \(1\). Their polynomial is \(T^3+T^2-2T-1\), of discriminant \(49\). The orbit-sum construction in (5.4), with \(H=\{1,-1\}\subset(\mathbb Z/7\mathbb Z)^\times\), already proves that \(\eta_1,\eta_2,\eta_3\) form an integral basis of the cubic fixed field. They are distinct, because the six powers \(\zeta_7,\ldots,\zeta_7^6\) are linearly independent, so \(\eta_1\) generates that field. Only seven can divide the index of the order \(\mathbb Z[\eta_1]\), by the index-square formula of Trace discriminants for orders, Section 3, the displayed formula immediately after the maximal-order ramification criterion. The shift \(T=U+2\) gives \(U^3+7U^2+14U+7\), Eisenstein at seven. For any extension of the seven-adic valuation, its root \(u=\eta_1-2\) has positive valuation, since its integral residue satisfies \(\bar u^3=0\). In \(u^3+7u^2+14u+7=0\), the last three terms have respective valuations \(1+2v(u),1+v(u),1\), so their sum has valuation exactly one. Thus \(v(u)=1/3\). The cubic field has local degree three and ramification index three, making \(u\) a uniformizer and the residue field the base residue field. The digit-and-Nakayama proof in Three differents, Lemma 5.1, then gives its full completed integer ring as \(\mathbb Z_7[u]\). Thus the local index at seven is one, and the order is maximal everywhere.

Now \(\operatorname{Tr}(\eta_i^2)=5\), because \(\eta_i^2=2+\eta_j\), and \(\operatorname{Tr}(\eta_i\eta_j)=-2\) for \(i\ne j\), because the product is the sum of two periods. Their Gram matrix has diagonal five and off-diagonal minus two; its eigenvalues are \(1,7,7\), so its determinant is \(49\). Their lattice consequently has index one in the full integer ring. The periods are cyclic conjugates, proving that \(\eta_1\) generates a global normal integral basis.

## 7. Exercises

1. **Easy.** For an odd prime \(p\), prove that \(\zeta_p\) generates a normal integral basis of \(\mathbb Z[\zeta_p]\) over \(\mathbb Z\).
2. **Medium.** Determine the trace image of \(\mathbb Z[i]\) and prove it has no global normal integral basis.
3. **Medium.** Prove Higman's criterion without assuming \(|G|\) invertible.
4. **Medium.** Find a normal integral basis generator at three for \(\mathbb Q(\sqrt{-3})\).
5. **Hard.** Derive the trace-tameness criterion from the different exponents, and explain the role of the Galois hypothesis.

## 8. Solutions

**1.** All nontrivial \(p\)-th roots are conjugates of \(\zeta_p\). Their powers from one through \(p-2\) already include all but the constant member of the standard power basis. The relation \(1=-\sum_{a=1}^{p-1}\zeta_p^a\) recovers that constant integrally. The replacement matrix has determinant \(\pm1\), proving both spanning and independence. Hence the associated \(\mathbb Z[G]\)-map is an isomorphism.

**2.** The trace is \(a+bi\mapsto2a\), with image exactly \(2\mathbb Z\). A normal generator would make the invariant submodule generated by its trace, whereas the invariant submodule is \(\mathbb Z\). This would force its trace to be a unit, impossible. Independently, the conjugate coefficient determinant \(-2ab\) is never \(\pm1\).

**3.** Form \(F=R[G]\otimes_R N\) with action on the first factor. It is projective, and \(\epsilon(g\otimes n)=g(n)\) is onto. The map \(s(n)=\sum_g g\otimes\phi(g^{-1}n)\) is equivariant and has composite \(T_G(\phi)\); if that is the identity, it splits. Conversely take an equivariant splitting, extract its coefficient at the identity, and use equivariance to express every other coefficient as \(\phi(g^{-1}n)\). The composite condition yields exactly the required sum. This proves both directions with no division by the group order.

**4.** Take \(\omega=(1+\sqrt{-3})/2\). The integer ring has basis \(1,\omega\); the conjugates \(\omega,1-\omega\) have coefficient columns \((0,1)^{\mathsf T},(1,-1)^{\mathsf T}\). Their determinant is \(-1\), so the same two columns give a basis after localization at three. The trace is one.

**5.** The trace fails to be onto exactly when its image lies in the base maximal ideal. By trace duality this is \(M\subseteq\pi\mathfrak D^{-1}\), which on each component is \(d_{\mathfrak P}\ge e_{\mathfrak P}\). The exponent bound says \(d\ge e-1\), with equality precisely for tame ramification; since these are integers, the strict alternative is \(d\ge e\). Galois transitivity makes all components tame together or wild together, so trace surjectivity is equivalent to tameness at the prime. Without that transitivity the containment must hold at every component for trace failure; surjectivity therefore only requires one tame component. Formula (2.3) independently confirms the same criterion with imperfect residue fields.

## What this lesson does not prove

The field normal basis theorem has the full internal proof in [Hilbert 90 in Noether's form and Galois descent, Theorem 4.0](https://kokunoyumeto.github.io/open-math-courses-public/courses/NOE-HYP/NOE-HYP-06.html#normal-bases-in-every-characteristic). The Cohen coefficient-field and power-series results have the exact earlier proofs linked in Lemma 4.2; that linked programme lesson retains GNU FDL 1.2 or later, so its proof is an external dependency for a collection restricted to CC0 content. The conductor–discriminant formula has the earlier proof linked in Section 5. Completion, prime decomposition and the cyclotomic integer theorem now have the exact supplied earlier proofs linked at their uses; Section 5 proves the characteristic-zero regular-representation decomposition and Hilbert–Speiser. Theorem 5.3 proves the quaternion example in full, including its group, ramification and failure of a global basis. Lemmas 5.4, 5.6 and 5.7 and Theorem 5.5 supply the cyclic-word congruence, integral determinant logarithm, reduction from matrix determinants to unit determinants, and logarithm near one. Results 5.8–5.11 construct the locally free class group, prove its stable-equivalence interpretation and lattice gluing description, and establish the integer-ring class in the Taylor statement. Results 5.12–5.14 prove prime-power representation induction, the transfer congruence, and the complete torsion determinant theorem, including injectivity of the logarithm on the commutator ideal. Results 5.15–5.17 prove the complete logarithm image on the commutator ideal and determinant descent for prime-power groups. Results 5.18–5.19 construct the determinant norm and prove its complete surjectivity criteria for prime-power groups. Results 5.20–5.22 prove the integral character action, subgroup determinant operations and projection formula, and their use with a supplied induction identity. Results 5.23–5.24 prove the Sylow facts and the rational induction identity at p, including the prime-to-p multiplier and the required cyclotomic conjugation condition. Results 5.25–5.26 prove integral semilinear descent over unramified coefficient extensions and full unit-norm surjectivity, including diagonal actions on abelian prime-power group algebras. Theorem 5.27 proves the elementary crossed-algebra determinant isomorphism, including integral splitting of its abelianized quotient and the commutator lifting argument. Results 5.28–5.30 prove unramified tensor factor descent and complete elementary-group determinant descent, including permuted factors; rational induction then annihilates the remaining general-group quotient by a prime-to-p integer. Results 5.31–5.32 prove finite division-ring commutativity and the finite p-primary Cartan cokernel. Results 5.33–5.36 prove the decomposition–Cartan identity, residue determinant reduction and its pro-p kernel, and full unramified and tame determinant descent for every finite group. Results 5.37–5.42 prove the finite Gauss identities, norm lifting, tame conductor parity, algebraic covariance of local constants, and the Galois-equivariant symplectic sign homomorphism. Results 5.43–5.46 compute the resolvent frame and the actual integer-lattice transition determinants, prove the real-place signature through a quaternionic structure, and supply the totally positive symplectic normalization. Results 5.47–5.53 prove the local reduced-norm image and density of its commutator kernel, elementary approximation, the complete stable determinant quotient with actual rational determinants, the integral unit image away from the group order, and the canonical two-torsion root-number class. Results 5.54–5.66 supply the global norm and rational determinant normalization, tame cyclic inertia and monomial characters, the adjusted residue-field Gauss formulas with their induction sign, and their field and twist laws. The full proof still to supply is Taylor’s root-number identity in Section 5: the complete local resolvent/Gauss-sum integral determinant comparison, including the full Gauss logarithm and torsion congruences. The required determinant descent is proved in Theorems 5.35–5.36. Trace-tameness, Higman's criterion, tame projectivity, characteristic-zero projective rigidity, positive-characteristic freeness, descent from completion, necessity and the discriminant square are proved here.

## References

- **[Noether]** Emmy Noether, [*Normalbasis bei Körpern ohne höhere Verzweigung*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0167/LOG_0021.pdf), Journal für die reine und angewandte Mathematik **167** (1932), 147–152, Sections 1–3; [English edition](https://github.com/KokunoYumeto/emmy-noether-en). Satz 5 is printed with the sufficient condition that the residue prime does not divide the extension degree. The modern tame theorem above allows divisibility of the residue degree: an unramified quadratic extension of \(\mathbb Q_2\), for example, has an integral normal basis despite \(2\mid2\).
- **[Milne FT]** J. S. Milne, [*Fields and Galois Theory*](https://www.jmilne.org/math/CourseNotes/FT.pdf), Chapter 5, Theorem 5.18.
- **[Milne ANT]** J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 6, Theorem 6.4 (cyclotomic integer rings).
- **[Stacks]** The Stacks Project, Tags [0C0S](https://stacks.math.columbia.edu/tag/0C0S), [09E3](https://stacks.math.columbia.edu/tag/09E3), and [0EXW](https://stacks.math.columbia.edu/tag/0EXW). These are read in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html), an edition with AI-proposed corrections and additions not reviewed by the Stacks Project's maintainers.
- **[Swan]** R. G. Swan, *Induced representations and projective modules*, Russian translation by B. B. Venkov, Matematika **8**, no. 1 (1964), 3–28, Section 6, Theorem 6.1 and Corollary 6.4; [free journal translation](https://www.mathnet.ru/php/getFT.phtml?jrnid=mat&option_lang=eng&paperid=292&what=fullt), [journal record](https://www.mathnet.ru/eng/mat292).
- **[Sutherland]** Andrew V. Sutherland, *Number Theory I*, MIT 18.785 lecture notes, Fall 2021: [Lecture 11](https://math.mit.edu/classes/18.785/2021fa/LectureNotes11.pdf), *Totally ramified extensions and Krasner's lemma*, on tamely ramified extensions, and [Lecture 12](https://math.mit.edu/classes/18.785/2021fa/LectureNotes12.pdf), *The different and the discriminant*.
- **[Milne CFT]** J. S. Milne, [*Class Field Theory*](https://www.jmilne.org/math/CourseNotes/CFT.pdf), version 4.03, Chapter V, Theorem 3.27 (the conductor-discriminant formula).
- **[Artin]** Emil Artin, [*Die gruppentheoretische Struktur der Diskriminanten algebraischer Zahlkörper*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0164/LOG_0004.pdf), Journal für die reine und angewandte Mathematik **164** (1931), 1–11.
- **[Cougnard]** Jean Cougnard, [*Les travaux de A. Fröhlich, Ph. Cassou-Noguès et M. J. Taylor sur les bases normales*](https://www.numdam.org/item/SB_1982-1983__25__25_0/), Séminaire Bourbaki, exposé 598, Astérisque **105–106** (1983), 25–38, Section 1.
- **[Bergé]** Anne-Marie Bergé, [*Sur l'arithmétique d'une extension diédrale*](https://www.numdam.org/item/10.5802/aif.411.pdf), Annales de l'Institut Fourier **22** (1972), 31–59, introduction, p. 31.
- **[Martinet]** Jacques Martinet, [*Modules sur l'algèbre du groupe quaternionien*](https://www.numdam.org/articles/10.24033/asens.1216/), Annales scientifiques de l'École Normale Supérieure **4** (1971), 399–408, Section IV.
- **[Lam]** Tsit-Yuen Lam, [*Induction theorems for Grothendieck groups and Whitehead groups of finite groups*](https://www.numdam.org/articles/10.24033/asens.1161/), freely accessible original article, Annales scientifiques de l’École Normale Supérieure **1** (1968), 91–148, Chapter 4, Section 3, Theorem 3.3 (Cartan cokernel).
- **[Chinburg–Pappas–Taylor]** T. Chinburg, G. Pappas and M. Taylor, [*K_1 of a p-adic group ring I. The determinantal image*](https://arxiv.org/abs/0904.2563v1), freely accessible preprint, version 1, 16 April 2009, Sections 2–7.
- **[Fröhlich, Locally free modules]** A. Fröhlich, [*Locally free modules over arithmetic orders*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0274_0275/LOG_0014.pdf), Journal für die reine und angewandte Mathematik **274–275** (1975), 112–124, Sections 2, 4–5 (locally free classes and reduced norms).
- **[Fröhlich]** A. Fröhlich, [*Arithmetic and Galois module structure for tame extensions*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0286_0287/LOG_0033.pdf), Journal für die reine und angewandte Mathematik **286–287** (1976), 380–440, Section 1, Theorem 1 (resolvent class representative), and Section 8, Theorems 9–10 (symplectic signs and resolvent signatures).
- **[Taylor]** M. J. Taylor, [*On Fröhlich's conjecture for rings of integers of tame extensions*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0063/LOG_0010.pdf), Inventiones Mathematicae **63** (1981), 41–79. The precise class identity is also in Ph. Cassou-Noguès and M. J. Taylor, [*Galois module structure for wild extensions*](https://www.math.u-bordeaux.fr/~pcassoun/graz1.pdf), introduction, equation (1.1).
