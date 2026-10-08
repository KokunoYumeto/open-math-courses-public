# Irreducible representations of general linear groups over a local field

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Parabolic induction supplies representations, but usually supplies too many at once: an induced representation can have several irreducible constituents. Segments organize this ambiguity. A segment groups consecutive twists of one supercuspidal representation into an essentially square-integrable representation; a multisegment specifies how such groups are assembled.

We prove the general Jacquet-module criterion for supercuspidality and the existence and uniqueness of cuspidal support, including the finite Bruhat filtration used in the proof. The general Bernstein–Zelevinsky segment classifications are stated in Section 2. Appendix A proves their normalized mirabolic-derivative machinery, its canonical filtration and the Leibniz rule, together with genericity of supercuspidals, Whittaker induction, highest-derivative duality, irreducibility of every cuspidal product without adjacent twists, and the complete cuspidal-pair reducibility criterion. Appendix B proves full Whittaker uniqueness, irreducible supercuspidal mirabolic restriction and the unique generic constituent of supercuspidal induction. Appendix C proves the complete constituent and submodule-lattice descriptions for distinct support on one cuspidal line, constructs both segment representations in every rank, calculates all their Jacquet modules, duals and derivatives, and proves irreducibility of arbitrary unlinked Z-products, both adjacent disjoint-segment extensions, and the linked overlapping-pair theorem. Their rank-two dictionary uses the complete classification and Kirillov models in [Whittaker models, Kirillov models and the local classification](../../automorphic-forms-and-representations-of-gl2/src/whittaker-models-kirillov-models-and-the-local-classification.md), especially Theorem 2.3, Theorem 4.2, Section 5 and Theorem 6.1. We also prove square-integrability of the rank-two Steinberg representation by an explicit coefficient calculation, and classify the four constituents of the rank-three consecutive-character induction directly on flag spaces. References include the article [Bernstein–Zelevinsky 1977], the journal archive [Zelevinsky 1980], the author draft [Getz–Hahn 2022], the IAS edition [Jacquet–Langlands 1970] and [Wedhorn 2000].

## 1. Induction and its normalizations

Let \(F\) be a nonarchimedean local field, \(\mathcal O\) its ring of integers, \(\varpi\) a uniformizer and \(q\) the residue cardinality. Put \(G_n=\mathrm{GL}_n(F)\) and \(\nu(g)=|\det g|_F\). Unless a functor construction explicitly uses the whole smooth category, representations of general linear groups are complex, smooth and admissible; “irreducible” always includes nonzero. Intermediate unipotent and mirabolic modules are only required to be smooth.

For a standard parabolic \(P=MU\), with \(M\simeq G_{n_1}\times\cdots\times G_{n_r}\), write

\[
\pi_1\times\cdots\times\pi_r
=\operatorname{Ind}_{P}^{G_n}
 (\delta_P^{1/2}\,\pi_1\boxtimes\cdots\boxtimes\pi_r).
\tag{1.1}
\]

Induction is realized by functions with left covariance and right translation. Thus for the upper triangular Borel \(B=TN\) in \(G_2\),

\[
 f\left(\begin{pmatrix}a&x\\0&d\end{pmatrix}g\right)
 =|a/d|^{1/2}\chi_1(a)\chi_2(d)f(g)
\tag{1.2}
\]

in \(I(\chi_1,\chi_2)=\chi_1\times\chi_2\). This convention fixes which constituent is a subrepresentation and which is a quotient at a reducibility point.

The **normalized Jacquet module** is

\[
r_N(V)=\delta_B^{-1/2}\otimes
 V/\langle n v-v:n\in N,\ v\in V\rangle.
\tag{1.3}
\]

For general \(G_n\), an irreducible representation is **supercuspidal** if it is not a subquotient of induction from a proper parabolic. We now prove the equivalent vanishing of proper Jacquet modules and the intrinsic **cuspidal support** for every rank, in both characteristics. Section 4 then illustrates the construction with the two rank-one Bruhat cells.

### Exactness, adjunction and admissibility

Write \(r_PV=\delta_P^{-1/2}V_U\) for every parabolic \(P=MU\), not just for the Borel. Intermediate smooth modules need not be irreducible. All arguments below use complex coefficients and apply to every nonarchimedean local field.

**Lemma 1.1.** Normalized Jacquet modules and parabolic induction are exact. Induction preserves admissibility, and

\[
\operatorname{Hom}_{G_n}(V,i_P^{G_n}\tau)
 \simeq\operatorname{Hom}_M(r_PV,\tau).
\tag{1.4}
\]

Both constructions are transitive along refinements of a block decomposition.

**Proof.** A block upper unipotent group is an increasing union of compact open subgroups. For example, if the block indices are \(i<j\), allow the \((i,j)\)-entry in \(\varpi^{-s(j-i)}\mathcal O\). Products remain in these sets because \((j-i)+(k-j)=k-i\); inverses do too by the finite triangular inverse formula. Their union is \(U\). For a compact subgroup \(C\), normalized averaging \(E_Cv=\int_C\pi(c)v\,dc\) identifies coinvariants with invariants. Averaging lifts invariant vectors across any surjection, so this functor is exact. Passing to the increasing union gives exactness of \(V\mapsto V_U\). It also proves the useful criterion

\[
v\in\langle\pi(u)x-x:u\in U,\ x\in V\rangle
 \quad\Longleftrightarrow\quad E_Cv=0
 \text{ for some compact open }C\subset U.
\tag{1.5}
\]

Indeed finitely many coinvariant relations lie in one such \(C\), and \(v-E_Cv\) is a finite linear combination of relations because the compact orbit of a smooth vector has finitely many values.

For a compact open \(J\subset G_n\), the finite set \(P\backslash G_n/J\) determines an induced \(J\)-fixed function by finitely many values. At a representative \(g\), the allowed value is fixed by the projection to \(M\) of \(P\cap gJg^{-1}\), a compact open subgroup of \(M\); the modulus is one on this compact intersection. These fixed spaces lift by averaging. Thus induction is exact on \(J\)-fixed functions and hence exact on smooth functions. They are finite dimensional when \(\tau\) is admissible, proving admissibility of induction. Finiteness of the double-coset set follows from compactness of \(P\backslash G_n\).

Evaluation at \(1\) sends an intertwiner \(A\) to \(v\mapsto A(v)(1)\). It kills the \(U\)-relations and has \(M\)-covariance \(\delta_P^{1/2}\tau\), giving the right side of (1.4). Conversely an \(M\)-map \(T:r_PV\to\tau\) gives
\(A(v)(g)=T([\pi(g)v])\). Normalization makes its left covariance exactly \(\delta_P^{1/2}\tau\); a subgroup fixing \(v\) fixes this function on the right. These maps are inverse. For a refinement \(R\subset M\), taking \(U\)-coinvariants and then \(U_R\)-coinvariants kills exactly the relations for \(U_RU\). The modulus identity is
\(\delta_{RU}^{G_n}|_R=\delta_P^{G_n}|_R\,\delta_R^M\).
For induction in stages, the corresponding map sends \(f\) to the function with value at \(g\) given by
\(m\mapsto\delta_P(m)^{-1/2}f(mg)\); evaluation at \(m=1\) is its inverse. ∎

We will also use \(G_n=PK\), \(K=\mathrm{GL}_n(\mathcal O)\), and the Cartan decomposition
\(G_n=K\{\operatorname{diag}(\varpi^{\lambda_1},\ldots,\varpi^{\lambda_n}):\lambda_1\ge\cdots\ge\lambda_n\}K\).
These are elementary matrix facts over a discrete valuation ring. For the first, intersect the flag stabilized by \(P\) with \(\mathcal O^n\). Each intersection is saturated, and a basis adapted to these nested direct summands changes the flag by an element of \(K\). For the second, clear denominators and repeatedly move an entry of smallest valuation to a corner. Integral row and column operations clear its row and column; it divides every remaining entry. Induction gives diagonal powers, which a permutation orders. These arguments work in either characteristic.

**Lemma 1.2.** If \(V\) is admissible, \(r_PV\) is admissible. If \(V\) is finitely generated, \(r_PV\) is finitely generated as an \(M\)-module.

**Proof.** Let \(M_r=\prod_i(1+\varpi^rM_{n_i}(\mathcal O))\), \(r\ge1\). Choose \(t\ge r\) and let \(J\) consist of block matrices with diagonal blocks in \(M_r\) and off-diagonal entries in \(\varpi^t\mathcal O\). Block Gaussian elimination gives the two factorizations

\[
J=(J\cap U)M_r(J\cap\bar U)
  =(J\cap\bar U)M_r(J\cap U).
\tag{1.6}
\]

The corrections to diagonal blocks have valuation at least \(2t\), so elimination stays in the stated sets. The same valuation bound proves closure under multiplication and inversion. Product Haar measure in either order is normalized Haar measure on \(J\): elimination changes the additive block coordinates by translations and multiplication by matrices congruent to \(1\), all with unit Jacobian. Equivalently one can perform the elimination in the finite quotients modulo \(\varpi^s\), where each factorization is a bijection and uniform counting measure factors.

Choose \(a\in Z(M)\) whose successive scalar blocks have strictly decreasing valuations. It contracts \(U\) and expands \(\bar U\). Put \(q_U:V\to V_U\) and \(X=q_U(V^J)\). If \(v\in V^J\), then \(\pi(a)v\) is fixed by \(M_r\) and \(J\cap\bar U\). The first factorization in (1.6) therefore gives

\[
q_U(E_J\pi(a)v)=q_U(\pi(a)v).
\tag{1.7}
\]

Here the remaining average over \(J\cap U\) disappears in coinvariants. Consequently the unnormalized action of \(a\) preserves \(X\). It is injective; since \(X\) is finite dimensional, it is bijective on \(X\).

For any \(w\in(V_U)^{M_r}\), lift it to an \(M_r\)-fixed \(v\) by averaging. Smoothness supplies a sufficiently small subgroup of \(\bar U\) fixing \(v\). For large \(N\), expansion by \(a^N\) makes \(\pi(a^N)v\) fixed by \(J\cap\bar U\). Equation (1.7) now puts \(a^Nw\) in \(X\). Bijectivity on \(X\) implies \(w\in X\). Thus \(q_U:V^J\to(V_U)^{M_r}\) is surjective, proving its finite dimension. The normalization is trivial on \(M_r\). Any compact open subgroup of \(M\) contains some \(M_r\), so all its fixed spaces are finite dimensional.

Finally choose finitely many generators of \(V\). Each has a finite \(K\)-orbit because it is smooth and \(K\) is compact. Their finitely many orbit vectors generate \(V\) under \(P\), using \(G_n=PK\), and their images generate \(V_U\) under \(M\). ∎

Jacquet admissibility and compact-open lifting are Casselman's Proposition III.5.5 and Theorem III.5.6 [Casselman 2019].

### Irreducible representations of a Levi

**Lemma 1.3.** An irreducible admissible representation of \(\prod_iG_{n_i}\) is an external tensor product of irreducible admissible representations of its factors. Those factors are unique.

**Proof.** We give the algebra details needed in descending the rank. For a compact open \(J\) in any of these groups, put \(e_J=1_J/\operatorname{vol}(J)\) and \(A_J=e_J\mathcal H(G)e_J\), with \(\mathcal H(G)=C_c^\infty(G)\). If \(V\) is irreducible and \(V^J\ne0\), its corner \(V^J\) is simple over \(A_J\): generate \(V\) from any nonzero fixed vector, then average back by \(e_J\). Conversely a simple corner module \(S\) has exactly one irreducible smooth reconstruction. Start with
\(\mathcal H(G)e_J\otimes_{A_J}S\) and quotient by
\[
N=\{x:e_J h x=0\text{ for every }h\in\mathcal H(G)\}.
\]
Its corner is \(S\). Any nonzero submodule of the quotient either has corner zero and lies in the already killed \(N\), or has all of \(S\) and therefore generates the quotient. This proves irreducibility and uniqueness. The construction is smooth because each of its vectors involves finitely many locally constant compactly supported functions.

Let \(V\) be irreducible admissible for two factors, and choose \(J_1,J_2\) with \(W=V^{J_1\times J_2}\ne0\). This is a finite-dimensional simple module for \(A_{J_1}\otimes A_{J_2}\). Choose a simple \(A_{J_1}\)-submodule \(S_1\subset W\). Its translates by \(A_{J_2}\) are zero or simple copies of \(S_1\), and their sum is a nonzero joint submodule, hence all of \(W\). A sum of simple modules is a direct sum of simple modules after choosing a maximal independent family: a simple module not contained in their sum has zero intersection and can be added. Thus
\(W=S_1\otimes E\), \(E=\operatorname{Hom}_{A_{J_1}}(S_1,W)\).
Schur's lemma is scalar on \(S_1\), since every complex endomorphism of a finite-dimensional simple module has an eigenvalue. The commuting second algebra acts on \(E\), and simplicity of \(W\) makes \(E=S_2\) simple.

Reconstruct irreducible smooth \(\sigma_i\) from \(S_i\). To see that \(\sigma_1\boxtimes\sigma_2\) is irreducible before assuming their admissibility, use the following elementary density argument. A smooth irreducible representation of a second-countable group has countable dimension: one vector generates it from the countably many cosets of its open stabilizer. Its commuting endomorphisms are scalar. Indeed a nonscalar \(T\) would make every \(T-\lambda\) invertible, and the vectors \((T-\lambda)^{-1}v\) would be linearly independent as \(\lambda\) ranges over \(\mathbb C\): clearing a finite relation's denominators gives a nonzero polynomial in \(T\), which is invertible since it factors into those linear factors. This contradicts countable dimension. This is the same countable Schur argument proved in [Smooth local representations and the Hecke-module dictionary, Theorem 4.1](../../automorphic-forms-and-representations-of-gl2/src/smooth-local-representations-and-the-hecke-module-dictionary.md#4-schur-s-lemma-before-admissibility); only second countability and smooth irreducibility enter it.

For a simple module \(S\) with scalar endomorphisms, its acting algebra can prescribe images of any finite linearly independent list \(s_1,\ldots,s_k\). Induct on \(k\). The image of \(h\mapsto(hs_1,\ldots,hs_k)\) projects onto \(S^{k-1}\). Its kernel in the last coordinate is a submodule of \(S\), hence zero or \(S\). If zero, the image is the graph of an equivariant map \(S^{k-1}\to S\). Each component is scalar, and evaluating the identity operator would express \(s_k\) in the span of its predecessors, a contradiction. Thus the kernel is \(S\), proving surjectivity. Applying this to a nonzero finite tensor sum isolates a nonzero pure tensor; acting in both factors then generates the entire tensor product. It is irreducible.

Its \(J_1\times J_2\)-corner is \(S_1\otimes S_2=W\), so unique reconstruction gives \(V=\sigma_1\boxtimes\sigma_2\). For every compact open \(J_i'\), admissibility of \(V\) bounds
\(\dim(\sigma_i^{J_i'}\otimes\sigma_{3-i}^{J_{3-i}})\), and the second factor is nonzero. Thus \(\sigma_i\) is admissible. Restricting the product module to each factor gives a sum of copies of that \(\sigma_i\), so its simple factor is intrinsic. Induction proves the assertion for any number of factors. ∎

### Vanishing Jacquet modules and supercuspidality

**Lemma 1.4.** An irreducible admissible \(V\) is supercuspidal if and only if \(r_PV=0\) for every proper parabolic. In that case every smooth matrix coefficient is compactly supported modulo the center. After an unramified twist \(V\) admits an invariant positive Hermitian form.

**Proof.** If \(r_PV\ne0\), Lemma 1.2 makes it finitely generated and admissible. A nonzero finitely generated module has an irreducible quotient: in a chain of proper submodules the union stays proper, since otherwise the finite list of generators would lie in one member. Zorn's lemma supplies a maximal proper submodule. Compact averaging shows that this quotient \(\tau\) is admissible. Adjunction (1.4) gives a nonzero map \(V\to i_P\tau\), which is injective by irreducibility. Therefore supercuspidality implies Jacquet vanishing.

For the converse first suppose all proper Jacquet modules vanish. A smooth dual functional \(\ell\) exists and separates vectors: average an arbitrary functional through a compact open subgroup fixing a chosen nonzero vector. For \(c(g)=\ell(\pi(g)v)\), the \(K\)-orbits of \(v\) and \(\ell\) are finite. Apply (1.5) to all the resulting vectors for each maximal standard parabolic \(P_i\), obtaining compact open \(C_i\subset U_i\) whose averages kill them. Choose a common compact open subgroup fixing the dual vectors.

In the Cartan decomposition write \(a=\operatorname{diag}(\varpi^{\lambda_1},\ldots,\varpi^{\lambda_n})\), with \(\lambda_1\ge\cdots\ge\lambda_n\). If \(\lambda_i-\lambda_{i+1}\) is sufficiently large, \(aC_i a^{-1}\) lies in that common stabilizer: every upper off-diagonal block of \(U_i\) gains valuation at least this gap. Consequently
\[
\ell(\pi(a)v)=\ell(\pi(a)E_{C_i}v)=0
\]
for the relevant orbit vectors. All nonzero coefficients therefore have uniformly bounded successive Cartan gaps. Subtracting \(\lambda_n\) corresponds to multiplying by a central scalar; bounded gaps leave finitely many tuples. This proves compact support modulo the center.

The central character \(\omega\) exists by Schur's lemma; for an admissible irreducible representation, an endomorphism has an eigenvalue on a nonzero finite-dimensional fixed space, and its invariant eigenkernel is the whole representation. The absolute value of \(\omega\) is trivial on \(\mathcal O^\times\). A twist by \(|\det|^s\), with \(s\in\mathbb R\), makes \(\omega\) unitary, because its central absolute value changes by \(|z|^{ns}\). Jacquet vanishing and membership in a proper induced subquotient are unchanged by such a twist.

For the unitary central character, fix \(0\ne\ell\in V^\vee\). The map \(v\mapsto[g\mapsto\ell(\pi(g)v)]\) is injective: its kernel is invariant and \(\ell\ne0\). Its image consists of compactly supported functions modulo the center with central covariance \(\omega\). Integrating the products of these functions on \(G_n/Z\) supplies a positive Hermitian form. Right invariance of Haar measure makes the form invariant.

It remains to exclude subquotients, rather than just subrepresentations, of proper inductions. For \(0\ne v\) in this unitary twist set \(b(g)=\langle\pi(g)v,v\rangle\). The second vector defines a smooth dual functional, since a subgroup fixing \(v\) also fixes that functional. Thus \(b\) is compact modulo \(Z\). For every proper \(P=MU\) and every \(x,m,y\), its constant term is zero:
\[
\int_U b(xmuy)\,du=0.
\tag{1.8}
\]
The restriction has compact support in \(U\). Indeed \(U\) is a closed embedded subgroup in \(G_n/Z\) (in block coordinates a central scalar is removed by a diagonal entry, leaving all unipotent coordinates unchanged); multiplication by fixed \(x,m,y\) preserves this property. Choose a compact open subgroup of \(U\) containing that support and large enough that its average kills \(\pi(y)v\), by (1.5). Integrating over this subgroup gives (1.8), and the integral outside it is zero.

Choose a nonnegative locally constant compactly supported \(\theta:F^\times\to\mathbb R\), positive at \(1\), and put
\[
f(g)=\theta(\det g)\,\overline{b(g)}.
\tag{1.9}
\]
This is in \(C_c^\infty(G_n)\): support of \(b\) is compact modulo \(Z\), and bounded determinant valuation bounds the central valuation since \(\det(zI)=z^n\). Moreover
\(\langle\pi(f)v,v\rangle=\int_{G_n}\theta(\det g)|b(g)|^2\,dg>0\).
The determinant is constant on \(x m U y\), so all constant terms of \(f\) still vanish by (1.8).

For any smooth \(\tau\), convolution by \(f\) annihilates \(i_P\tau\). To see this directly at \(x\), change variables in \(\int f(g)h(xg)\,dg\) and use \(G_n=PK\). The covariance of \(h\) writes this as an integral over \(m,u,k\) of
\[
f(x^{-1}muk)\,\delta_P(m)^{1/2}\tau(m)h(k)
\]
times the scalar Iwasawa measure factor, which is independent of \(u\). The inner integral in \(u\) is zero. All integrals are locally constant integrals with compact support in the integrating group variable, so Fubini applies. Hence \(f\) annihilates every subquotient of this induction, while \(\pi(f)\ne0\). This proves the converse for arbitrary inducing modules, without a central-character assumption on them. Undo the unramified twist to finish. A compact separator for the original representation is obtained by multiplying \(f(g)\) by the same twisting character; its constant terms remain zero because that character is trivial on every unipotent group. ∎

The argument also applies inside a Levi factor. In particular, if \(\sigma=\boxtimes_i\sigma_i\) and each \(\sigma_i\) is supercuspidal, it cannot be a subquotient of an induction that splits any one of its blocks: use the function (1.9) in that factor and compact averaging in the others.

### The block Bruhat filtration

For \(P=LU_P\) and \(Q=MU_Q\), write their ordered block sizes as \((d_1,\ldots,d_r)\) and \((e_1,\ldots,e_s)\). Double cosets \(P\backslash G_n/Q\) are indexed by matrices of nonnegative integers
\((n_{ij})\) with row sums \(d_i\) and column sums \(e_j\). The entry \(n_{ij}\) is the dimension of the corresponding successive intersection of the two flags. An adapted basis simultaneously displays these intersections, proving the double-coset assertion. Choose the permutation representative \(w\) preserving the order inside each intersection; it is the representative of minimum length in \(W_L\backslash S_n/W_M\).

**Lemma 1.5 (geometric lemma for block parabolics).** The normalized Jacquet module \(r_Q(i_P\tau)\) has a finite filtration with one term for each such \(w\):

\[
i_{R_w}^{M}\left({}^{w^{-1}}r_{S_w}^{L}\tau\right),
\qquad
R_w=M\cap w^{-1}Pw,\quad S_w=L\cap wQw^{-1}.
\tag{1.10}
\]

Here \(R_w,S_w\) are parabolics in \(M,L\); their common Levi factors have block sizes \(n_{ij}\), read by columns and by rows respectively. Zero sizes are omitted. The formula is a filtration, not a claimed splitting.

**Proof.** Each cell is locally closed: prescribing all the flag-intersection dimensions imposes closed rank inequalities, given by vanishing minors, together with their open complements. Its closure is \(Q\)-stable and therefore a union of cells. Closure containment orders the finitely many cells. Two distinct cells cannot have the same closure, since each would be an open dense subset of that closure and those two open sets would have to meet. Order the cells so that successive unions are open, by taking complements of successive closed unions in this order. Filter the induced functions by compact support in these open unions in \(P\backslash G_n\). Each quotient consists of compactly supported locally constant sections on a single cell. Restriction is onto: a compactly supported section on a locally closed cell extends on finitely many local trivializations, using a clopen refinement of its compact support. Its kernel is the sections on the preceding open union.

On the \(w\)-cell write the section as \(h(q)=f(wq)\). Its stabilizer is \(H=Q\cap w^{-1}Pw\), and it satisfies
\[
h(h_0q)=\delta_P(wh_0w^{-1})^{1/2}
 \tau(\operatorname{pr}_L(wh_0w^{-1}))h(q).
\]
For the chosen \(w\), block coordinates give \(H=R_wN_w\), where
\(N_w=U_Q\cap w^{-1}Pw\). Its image in \(L\) is the unipotent radical of \(S_w\); its kernel maps into \(U_P\). Thus quotienting the values by \(N_w\)-relations gives the unnormalized \(S_w\)-Jacquet module of \(\tau\).

The \(U_Q\)-coinvariant map on this cell is fiber integration
\[
h\longmapsto F(m)=
 \int_{N_w\backslash U_Q}[h(um)]\,d\dot u.
\tag{1.11}
\]
The brackets make the integrand left \(N_w\)-invariant. The quotient measure exists because both unipotent groups are unimodular. Compact support on \(H\backslash Q\) makes its fiber integrals finite. Integration is onto, and its kernel is exactly the right \(U_Q\)-relations. The following compact-average calculation proves this, including nontrivial action of \(N_w\) on the values.

First work in one fiber, with a section \(h\) on \(N_w\backslash U_Q\). Choose a compact open \(C\subset U_Q\) containing representatives of its support. Right averaging replaces \(h\), modulo translation relations, by \(h_C=E_Ch\). This is supported in \(N_wC\), is right \(C\)-fixed, and is determined by \(z=h_C(1)\), which is fixed by \(N_w\cap C\). Its integral in the value coinvariants is
\(\operatorname{vol}(N_w\backslash N_wC)[z]\).
If this is zero, (1.5), now for \(N_w\), supplies a compact open \(D\subset N_w\) with \(E_Dz=0\). Choose a compact open \(C'\subset U_Q\) containing \(C\) and \(D\). The right \(C'\)-average of \(h_C\) is determined at \(1\) by a nonzero scalar times \(E_{N_w\cap C'}z\). This follows by writing its integral over \((N_w\cap C')C\) as the compact product integral; outside that set \(h_C\) vanishes. Since \(D\subset N_w\cap C'\), this value is zero. Hence \(h\) is zero in \(U_Q\)-coinvariants. Conversely every translation relation has integral zero. For surjectivity, choose a representative \(z\) of a value class and a small \(C\) whose intersection with \(N_w\) fixes \(z\); the section on \(N_wC\) with value \(z\) has that class times the nonzero displayed volume.

To apply the calculation to a section with varying \(m\), partition its compact base support into clopen trivializing patches. Its value vectors and compact support data are finite after a sufficiently fine partition. Compact open subgroups containing these data can be chosen from block-coordinate lattices as in Lemma 1.1; each is normalized by a sufficiently small open subgroup of \(M\). Shrink a patch around its chosen representative \(m_0\) so that the differences \(m_0^{-1}m\) normalize the finitely many subgroups \(C,C'\) used there and fix the value data. Then the fiber averages throughout that patch are realized by the single right subgroup \(m_0^{-1}Cm_0\), respectively \(m_0^{-1}C'm_0\). They preserve the patch because right \(U_Q\) does not move the base in \(R_w\backslash M\). Thus the zero-integral calculation gives actual right translation relations on the whole patch. The lifts for surjectivity extend over the same patches. Adding the finitely many pieces proves both assertions about (1.11).

For precision, let \(D_w(m)\) be the modulus of conjugation by \(m\in R_w\) on \(N_w\backslash U_Q\). It is
\[
D_w(m)=\delta_Q(m)/\delta_{N_w}(m),
\]
where \(\delta_{N_w}\) denotes its conjugation modulus, rather than the modulus of the unipotent group itself. Changing variables in (1.11) gives left covariance
\(\delta_P(wmw^{-1})^{1/2}D_w(m)\tau_{S_w,\mathrm{unnorm}}(wmw^{-1})\).
Multiply \(F(m)\) by \(\delta_Q(m)^{-1/2}\). This changes the right \(M\)-action to the normalized \(Q\)-Jacquet action. Replacing the unnormalized value module by \(r_{S_w}\tau\) gives precisely normalized \(R_w\)-induction, because

\[
\delta_P(wmw^{-1})\,\delta_Q(m)\,
 \delta_{S_w}(wmw^{-1})
 =\delta_{R_w}(m)\,\delta_{N_w}(m)^2.
\tag{1.12}
\]

One can check (1.12) root by root. A root in \(U_Q\) carried into \(U_P\) contributes twice and is in \(N_w\). One carried into the opposite of \(U_P\) cancels. One carried into \(L\) contributes once from \(Q\) and once from \(S_w\), and is again in \(N_w\). A root inside \(M\) carried into \(U_P\) contributes equally from \(P\) and \(R_w\); a root remaining in both Levi groups contributes nothing. Minimum length ensures the stated positive-root choices. These exhaust all matrix entries. Exactness from Lemma 1.1 now carries the finite cell filtration through coinvariants, proving (1.10). ∎

The geometric lemma originates in Bernstein–Zelevinsky [1977, Lemma 2.12 and §§5–6]. We have given the block-coordinate and normalization argument here, including the compactly supported fiber calculation.

### Existence and uniqueness of cuspidal support

**Theorem 1.6.** Every irreducible admissible representation of \(G_n\) embeds into an induction
\(\rho_1\times\cdots\times\rho_r\), with the \(\rho_i\) irreducible supercuspidal. If it is a subquotient of any induction of irreducible supercuspidals, the unordered multiset of those entries is the same. This multiset, including multiplicities, is its cuspidal support.

**Proof.** If all proper Jacquet modules vanish, Lemma 1.4 supplies the assertion with the single entry \(\pi\). Otherwise choose a nonzero proper \(r_P\pi\), an irreducible admissible quotient, and its tensor factorization from Lemmas 1.2–1.3. Adjunction embeds \(\pi\) in its induction. Apply the same procedure to each factor. Each descent strictly decreases the block rank, so it terminates. Exactness and induction in stages then embed \(\pi\) into an induction of supercuspidals. No finite-length theorem for arbitrary induced representations has been assumed in this construction.

For uniqueness fix such an embedding \(\pi\hookrightarrow i_Q\sigma\), with \(\sigma=\boxtimes_j\sigma_j\) supercuspidal in each \(M\)-block. Suppose also that \(\pi\) is a subquotient of \(i_P\rho\), \(\rho=\boxtimes_i\rho_i\), with every \(\rho_i\) supercuspidal. Adjunction to the first embedding gives a surjection \(r_Q\pi\to\sigma\): the map is nonzero and \(\sigma\) is simple. Exactness makes \(\sigma\) a subquotient of \(r_Q(i_P\rho)\), and hence a subquotient of at least one term in its finite filtration (1.10). To justify the last assertion without a length assumption, lift a simple quotient to a submodule and intersect it with the filtration; the first intersection with nonzero image maps onto that quotient.

If some row of \((n_{ij})\) has more than one nonzero entry, \(S_w\) splits the corresponding \(\rho_i\)-block. Its proper Jacquet module is zero by Lemma 1.4; tensor products and coinvariants commute, so this entire filtration term is zero. A surviving term therefore assigns each complete \(\rho_i\)-block to exactly one \(M\)-block. If a column contains more than one such block, \(R_w\) is a proper parabolic in that \(M\)-factor. The separator (1.9) for \(\sigma_j\) annihilates that induced factor and all its subquotients, while it acts nontrivially on \(\sigma_j\); averaging in the other factors gives a contradiction to occurrence of \(\sigma\). Thus each column contains exactly one row block as well. In this case \(R_w=M\), \(S_w=L\), and the surviving term is the permutation of \(\rho\) determined by \(w\). It is irreducible by Lemma 1.3, so it must equal \(\sigma\). The two lists agree up to permutation, with all repeated entries retained. ∎

This proves the general support theorem of Bernstein–Zelevinsky [1977, Theorem 2.9 and §4.1] in the present admissible setting and all local-field characteristics. It supplies the support used in the segment statements below; existence and uniqueness of segment constituents require the additional classification arguments.

**Corollary 1.7 (finite length).** Induction from \(r\) irreducible supercuspidal blocks has length at most \(r!\). Parabolic induction of finite-length admissible representations has finite length.

**Proof.** Let \(I=i_P\rho\) be the former induction. Consider all distinct ordered Levi block decompositions whose sizes permute those of \(P\). For each such \(Q\), the filtration of \(r_QI\) in Lemma 1.5 has only unsplit-row terms: a split row takes a proper Jacquet module of a supercuspidal and gives zero. There are \(r\) nonempty rows and \(r\) nonempty columns, so an unsplit-row term also has exactly one row in each column. It is an irreducible permutation of \(\rho\). Summing their numbers over these \(Q\) counts exactly the \(r!\) permutations of the labeled row blocks, including repeated sizes or repeated representations. Therefore
\[
\sum_Q\operatorname{length}(r_QI)=r!.
\]

For a subquotient \(W\) of \(I\), these Jacquet modules have finite length by exactness. Put \(d(W)=\sum_Q\operatorname{length}(r_QW)\). This is additive on short exact sequences. If \(W\ne0\), choose a nonzero cyclic submodule and an irreducible quotient \(\tau\) of it, using the maximal-submodule argument of Lemma 1.4. It is admissible, since subquotients of admissible representations are admissible by exact compact averaging. Theorem 1.6 gives its support \(\{\rho_i\}\) and an embedding into some \(i_Q\sigma\) on the list just considered. Adjunction makes \(r_Q\tau\ne0\); exactness therefore gives \(r_QW\ne0\) and \(d(W)\ge1\).

Every strict step of a submodule chain in \(I\) consumes at least one of the \(d(I)=r!\) units. Ascending and descending strict chains are thus bounded. Taking maximal proper submodules and descending produces a composition series with at most \(r!\) factors.

Finally an irreducible inducing representation embeds into an induction of supercuspidals by Theorem 1.6. Tensoring these embeddings, exact induction and induction in stages embed their product into an induction of supercuspidals, which has finite length by the first assertion. Finite composition series in the inducing modules and exactness then prove the assertion for finite-length admissible inputs. This proves finite length independently of the segment classification. ∎

## 2. Segments and the two classifications

Fix an irreducible supercuspidal \(\rho\) of \(G_d\). A segment on its integer twist line is

\[
\Delta=[\rho\nu^a,\rho\nu^{a+1},\ldots,\rho\nu^b],
\qquad a,b\in\mathbb Z,\quad a\le b.
\tag{2.1}
\]

An arbitrary starting representation absorbs a nonintegral twist. The degree of this segment is \(d(b-a+1)\). The interval notation records the actual representations, so translating the base \(\rho\) and the endpoints together does not change the segment.

Two segments are **linked** when their union is a segment and neither contains the other. For segments \([a,b]\) and \([c,d]\) on the same line with \(a\le c\), this means precisely

\[
a<c\le b+1\le d.
\tag{2.2}
\]

Indeed, absence of a gap says \(c\le b+1\); absence of containment says \(a<c\) and \(b<d\). Segments on different integer twist lines are never linked. Equal segments, and a segment contained in another, are never linked. Adjacent disjoint segments can be linked.

Let \(Q(\Delta)\) denote the unique irreducible quotient of the increasing induction in (2.1), and let \(Z(\Delta)\) denote its unique irreducible subrepresentation. Existence, uniqueness, all their Jacquet modules, duality and derivatives are proved in Appendix C, Theorems C.4–C.5. The square-integrability and full classification assertions below remain stated theorem inputs.

**Theorem 2.1 (segment and Langlands classification, stated).** The representations \(Q(\Delta)\) are exactly the essentially square-integrable irreducible representations of general linear groups. Write
\(Q(\Delta)=\delta_\Delta\nu^{e_\Delta}\), where \(\delta_\Delta\) is square-integrable with unitary central character and \(e_\Delta\in\mathbb R\). For a multisegment \(\mathfrak m=\{\Delta_1,\ldots,\Delta_t\}\), order the segments so that \(e_{\Delta_1}\ge\cdots\ge e_{\Delta_t}\). Then

\[
Q(\Delta_1)\times\cdots\times Q(\Delta_t)
\longtwoheadrightarrow L(\mathfrak m)
\tag{2.3}
\]

has a unique irreducible quotient. The map \(\mathfrak m\mapsto L(\mathfrak m)\) is a bijection onto all irreducible admissible representations, in each total degree. Choices among equal exponents do not change the quotient. The cuspidal support is the multiset of all entries of the segments, with their multiplicities.

The essentially square-integrable classification is described in [Getz–Hahn 2022, Theorem 8.4.3]. The Langlands quotient and its uniqueness are stated there in Theorems 8.4.1–8.4.2; the reformulation by ordered essentially square-integrable blocks is Theorems 10.5.1–10.5.2. The increasing single-segment quotient convention agrees with ours. The free original article [Zelevinsky 1980, §9] gives the square-integrable and generic segment results. These references identify the statements; their full general proofs remain to be written in this lesson.

The same classifications are summarized in [Wedhorn 2000, (2.2.9) and (2.3.9)].

**Theorem 2.2 (Zelevinsky classification, stated).** Say that \([a,b]\) precedes \([c,d]\) if \(a<c\le b+1\le d\). Order a multisegment so that no earlier segment precedes a later one. The induction of the corresponding \(Z(\Delta_i)\) has a unique irreducible subrepresentation, denoted \(Z(\mathfrak m)\). This is independent of the allowed ordering, and \(\mathfrak m\mapsto Z(\mathfrak m)\) is another bijection onto irreducible representations. See [Zelevinsky 1980, §§4 and 6].

The two labels differ. Already for a length-two segment on a character line (\(d=1\)), \(Q(\Delta)\) is a Steinberg twist whereas \(Z(\Delta)\) is a determinant character. The latter description requires \(d=1\); for higher-rank supercuspidals the segment representations have the Jacquet modules in (C.5). The involution relating the two multisegment classifications must therefore be applied before identifying their labels.

**Theorem 2.3 (irreducibility, genericity and temperedness, stated).** The induction
\(Q(\Delta_1)\times\cdots\times Q(\Delta_t)\) is irreducible if and only if no two segments are linked. An irreducible representation is generic if and only if its Langlands multisegment is unlinked. It is tempered if and only if all its segment representations are square-integrable with unitary central character. The segment induction and genericity statements are [Zelevinsky 1980, Theorem 9.7] and [Getz–Hahn 2022, Theorem 8.4.4]. The tempered characterization is [Getz–Hahn 2022, Theorem 8.4.5]. Its proof there uses the tempered induction and support theorems; those arguments are also required for a complete internal proof here.

For the equivalent multisegment statements see [Wedhorn 2000, (2.2.9)(4), (2.3.7) and (2.4.4)].

Here generic means admitting a nonzero Whittaker functional for a nondegenerate character of the upper unipotent group. Square-integrable means that matrix coefficients are square-integrable modulo the center, whose character is unitary; “essentially” permits twisting by a real power of \(\nu\).

## 3. The complete rank-two dictionary

We use the following rank-one classification input: \(I(\chi_1,\chi_2)\) is irreducible unless \(\chi_1\chi_2^{-1}=\nu^{\pm1}\); away from those ratios, interchanging the characters gives an isomorphic representation. At either exceptional ratio there are exactly two constituents, a determinant character and its Steinberg twist, in the subquotient positions stated below. Every irreducible representation of \(G_2\) is a supercuspidal, one of these irreducible principal series, a Steinberg twist, or a determinant character. The complete proofs are [Whittaker models, Kirillov models and the local classification, Theorem 4.2 and Section 5](../../automorphic-forms-and-representations-of-gl2/src/whittaker-models-kirillov-models-and-the-local-classification.md#4-principal-series-and-the-two-exceptional-extensions) for reducibility, exceptional constituents and symmetry, and [Theorem 6.1](../../automorphic-forms-and-representations-of-gl2/src/whittaker-models-kirillov-models-and-the-local-classification.md#6-classification-and-the-germs-at-zero) for exhaustion. The original principal-series result is [Jacquet–Langlands 1970, Theorem 3.3].

The Steinberg representation has the boundary realization

\[
\mathrm{St}_2=C^\infty(\mathbb P^1(F))/\mathbb C.
\tag{3.1}
\]

Indeed, (1.2) for \((\chi_1,\chi_2)=(\nu^{-1/2},\nu^{1/2})\) has trivial left \(B\)-covariance. Its functions are locally constant functions on \(B\backslash G_2\simeq\mathbb P^1(F)\); its constant functions form the trivial subrepresentation. Twisting gives the exact sequences

\[
0\longrightarrow\chi\circ\det
\longrightarrow I(\chi\nu^{-1/2},\chi\nu^{1/2})
\longrightarrow\mathrm{St}_2\otimes(\chi\circ\det)
\longrightarrow0,
\tag{3.2}
\]

\[
0\longrightarrow\mathrm{St}_2\otimes(\chi\circ\det)
\longrightarrow I(\chi\nu^{1/2},\chi\nu^{-1/2})
\longrightarrow\chi\circ\det\longrightarrow0.
\tag{3.3}
\]

The second follows also by contragredience of the first, using the complete normalized-induction duality proof in [Normalized induction and Jacquet modules, Proposition 1.2](../../automorphic-forms-and-representations-of-gl2/src/normalized-induction-and-jacquet-modules.md#1-induction-with-the-square-root-modulus) and the rank-one constituent identification.

**Proposition 3.1.** The segment classification in total degree two is exactly the rank-one classification just recalled. Singleton segments are linked exactly at its two reducibility ratios.

**Proof.** A degree-two multisegment has only three possible forms. It can be one singleton whose supercuspidal entry has degree two; its Langlands quotient is that entry itself. It can be one length-two segment of characters, necessarily
\([\chi\nu^{-1/2},\chi\nu^{1/2}]\); (3.2) identifies its \(Q\) with \(\mathrm{St}_2\otimes\chi\) and its \(Z\) with \(\chi\circ\det\). Finally, it can have two character singletons. If they are unlinked, their induction is irreducible by the rank-one input and gives the principal series. If linked, they are the two characters in (3.2). Ordering their real exponents decreasingly gives (3.3), so their Langlands quotient is \(\chi\circ\det\).

To verify the linking assertion without invoking the general criterion, two distinct singleton characters have a segment as their union exactly when one is the other times \(\nu\). Thus they are linked exactly when \(\chi_1\chi_2^{-1}=\nu\) or \(\nu^{-1}\). Equal characters fail the noncontainment condition and give an irreducible principal series. These possibilities exhaust both classifications, with the same isomorphisms and exceptional constituents. ∎

For clarity, the two exceptional Langlands labels are

| Representation | Langlands multisegment |
| --- | --- |
| \(\mathrm{St}_2\otimes\chi\) | \(\{[\chi\nu^{-1/2},\chi\nu^{1/2}]\}\) |
| \(\chi\circ\det\) | \(\{[\chi\nu^{-1/2}],[\chi\nu^{1/2}]\}\) |

The central character in both rows is \(\chi^2\). Their cuspidal supports agree; their grouping into segments does not.

## 4. The two Bruhat cells and cuspidal support

**Lemma 4.1 (rank-one geometric lemma).** The normalized Jacquet module of \(I(\chi_1,\chi_2)\) has a two-step filtration whose quotients are

\[
\chi_2\boxtimes\chi_1,\qquad
\chi_1\boxtimes\chi_2.
\tag{4.1}
\]

This asserts a filtration, not necessarily a direct sum.

**Proof.** First, coinvariants under \(N\simeq(F,+)\) are exact on smooth representations. Write \(F=\bigcup_{r\ge0}\varpi^{-r}\mathcal O\). Coinvariants are the directed limit of coinvariants for these compact groups. Each compact coinvariant functor is averaging onto invariants and is exact over \(\mathbb C\); directed limits of vector spaces are exact. The normalization twist preserves exactness.

Evaluation at the closed Bruhat cell gives a surjection \(f\mapsto f(1)\). Its kernel consists of functions supported away from that point of \(B\backslash G_2\). On the open cell, use
\(w=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\) and coordinate \(w n(x)\). The kernel is then \(C_c^\infty(F)\), and right \(n(u)\) acts by \(\phi(x)\mapsto\phi(x+u)\).

Integration \(\phi\mapsto\int_F\phi(x)\,dx\) identifies its coinvariants with \(\mathbb C\). To check injectivity of this identification, refine a compactly supported locally constant function into finitely many cosets of a common compact open additive subgroup. Translation identifies the characteristic functions of all these cosets in coinvariants. A function with integral zero is consequently a sum of their differences, and is zero in coinvariants.

For \(t=\operatorname{diag}(a,d)\), the open-cell action is

\[
\phi(x)\longmapsto
|d/a|^{1/2}\chi_1(d)\chi_2(a)\phi(xd/a).
\]

The integral picks up \(|a/d|\); after multiplication by \(\delta_B(t)^{-1/2}=|a/d|^{-1/2}\), its character is \(\chi_2(a)\chi_1(d)\). Evaluation at the closed cell has unnormalized character \(|a/d|^{1/2}\chi_1(a)\chi_2(d)\), so its normalized character is \(\chi_1(a)\chi_2(d)\). Exactness now gives (4.1). ∎

For a determinant character, \(N\) acts trivially, whence

\[
r_N(\chi\circ\det)
=\chi\nu^{-1/2}\boxtimes\chi\nu^{1/2}.
\tag{4.2}
\]

Apply Lemma 4.1 and exactness to (3.2). Subtracting the character in (4.2) from the two filtration characters leaves

\[
r_N(\mathrm{St}_2\otimes\chi)
=\chi\nu^{1/2}\boxtimes\chi\nu^{-1/2}.
\tag{4.3}
\]

**Theorem 4.2.** Cuspidal support for \(G_2\) is well defined up to order. It is read from the computed Jacquet modules as follows:

\[
\begin{array}{c|c}
\pi&\operatorname{supp}_{\mathrm{cusp}}(\pi)\\\hline
I(\chi_1,\chi_2)\text{ irreducible}&\{\chi_1,\chi_2\}\\
\mathrm{St}_2\otimes\chi&\{\chi\nu^{-1/2},\chi\nu^{1/2}\}\\
\chi\circ\det&\{\chi\nu^{-1/2},\chi\nu^{1/2}\}\\
\rho\text{ supercuspidal}&\{\rho\}.
\end{array}
\tag{4.4}
\]

**Proof.** For every non-supercuspidal irreducible, (4.1)–(4.3) give a nonzero finite-length \(T\)-module. Forgetting the order in either character of its semisimplification gives the multiset in (4.4). Suppose the same representation occurs in another induction \(I(\eta_1,\eta_2)\). By the rank-one classification that induction is either irreducible, or has precisely the two constituents in (3.2)–(3.3). The computations for each constituent show that every one of its Jacquet characters has unordered pair \(\{\eta_1,\eta_2\}\). Hence this pair equals the pair intrinsic to \(r_N(\pi)\).

A supercuspidal cannot occur in a proper induction by definition, and induction from \(G_2\) itself has only that irreducible as its constituent. Conversely all three non-supercuspidal types occur in their displayed character inductions. This proves both existence and uniqueness in rank two without using the general cuspidal-support uniqueness theorem. ∎

## 5. Why the rank-two Steinberg coefficients are square-integrable

Here the Steinberg representation has trivial central character, so work in \(\overline G=\mathrm{PGL}_2(F)\). Let \(I\) be the image of the Iwahori subgroup consisting of integral invertible matrices that are upper triangular modulo \(\varpi\), and give it volume one.

The lattice tree makes the relevant double cosets explicit. Vertices are homothety classes of rank-two \(\mathcal O\)-lattices; two vertices are adjacent when representatives \(L,L'\) satisfy \(\varpi L\subset L'\subset L\) with quotient dimension one. Each vertex has \(q+1\) neighbors. The group \(I\) fixes the two endpoints of the edge
\([\mathcal O^2],[\mathcal O e_1+\varpi\mathcal O e_2]\). Set

\[
s_0=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
s_1=\begin{pmatrix}0&\varpi^{-1}\\\varpi&0\end{pmatrix},\quad
\omega=\begin{pmatrix}0&1\\\varpi&0\end{pmatrix}.
\tag{5.1}
\]

Modulo the center, \(s_0,s_1\) are involutions, their alternating products are distinct, and \(\omega^2=1\). The latter exchanges the edge endpoints and conjugates \(s_0\) to \(s_1\). Thus the extended affine Weyl group is
\(\widetilde W=\langle s_0,s_1\rangle\rtimes\langle\omega\rangle\), with \(\ell(\omega)=0\).

The double cosets of \(I\) are \(IwI\), for \(w\in\widetilde W\), and

\[
\operatorname{vol}(IwI)=q^{\ell(w)}.
\tag{5.2}
\]

One elementary verification uses the unique path between two tree edges. Its successive wall types alternate, giving a reduced word in \(s_0,s_1\); possible endpoint exchange records \(\omega\). At each new step there are exactly \(q\) choices after excluding the edge just traversed. The edge stabilizer acts transitively on those choices: reducing the upper, respectively lower, unipotent matrix entries modulo \(\varpi\) gives the translations on the \(q\) choices. Inductively its stabilizers give transitivity on paths of the fixed wall sequence. This proves both the double-coset description and the \(q^{\ell(w)}\) count of right \(I\)-cosets. It also proves the convolution rule \(T_uT_v=T_{uv}\) when lengths add, for \(T_w=1_{IwI}\).

**Proposition 5.1.** Every matrix coefficient of \(\mathrm{St}_2\) is in \(L^2(\overline G)\).

**Proof.** In the boundary model (3.1), \(I\) has two orbits on \(\mathbb P^1(F)\), so \(\dim\mathrm{St}_2^I=1\). Each of the two maximal vertex stabilizers \(K_0,K_1\) is transitive on that boundary, so \(\mathrm{St}_2^{K_i}=0\). These assertions pass from boundary functions to their quotient because invariants for compact groups are exact by averaging.

Choose an \(I\)-fixed vector \(v\) and an \(I\)-fixed smooth dual vector \(v^\vee\) with \(\langle v,v^\vee\rangle=1\). Such a dual vector exists by averaging any functional nonzero on \(v\); admissibility identifies the dual of the invariant line with the invariant line of the smooth dual. The normalized averages over \(K_i\) act as zero. Since \(K_i=I\sqcup Is_iI\),

\[
T_{s_i}v=-v\quad(i=0,1).
\]

The element \(\omega\) acts on the invariant line by a scalar \(\zeta\) with \(\zeta^2=1\). For \(w\) of length \(r\), convolution of a reduced word therefore acts on this line by a scalar of absolute value one. The coefficient
\(c(g)=\langle\mathrm{St}_2(g)v,v^\vee\rangle\) is constant on \(IwI\), while integrating it over that coset gives the same scalar. Equation (5.2) yields

\[
|c(g)|=q^{-\ell(w)}\quad(g\in IwI).
\tag{5.3}
\]

There are two elements of length zero and four of each positive length in \(\widetilde W\). Consequently

\[
\int_{\overline G}|c(g)|^2\,dg
=2+4\sum_{r\ge1}q^{-r}
=2+\frac4{q-1}<\infty.
\tag{5.4}
\]

Both the Steinberg representation and its smooth dual are irreducible. They are generated by their nonzero invariant vectors. Every matrix coefficient is therefore a finite linear combination of left and right translates of \(c\). Haar measure on \(\overline G\) is invariant under both translations, so all those coefficients are square-integrable. ∎

A unitary character twist does not change coefficient absolute values. Thus \(\mathrm{St}_2\otimes\chi\) is square-integrable when \(\chi\) is unitary, and essentially square-integrable for any character \(\chi\). The determinant-character constituent in (3.2) has coefficient of constant absolute value when unitary, and cannot be square-integrable on the noncompact group \(\overline G\).

## 6. A three-dimensional example

Consider \(I=\nu^{-1}\times1\times\nu\). Its support contains each of the three consecutive characters once. There are four multisegments with this support:

\[
\begin{aligned}
\mathfrak m_0&=\{[-1],[0],[1]\},&
\mathfrak m_1&=\{[-1,0],[1]\},\\
\mathfrak m_2&=\{[-1],[0,1]\},&
\mathfrak m_3&=\{[-1,1]\}.
\end{aligned}
\tag{6.1}
\]

Here \([a,b]=[\nu^a,\ldots,\nu^b]\). An overlap would repeat a support character, so these are precisely the choices of cuts at the two edges. We will prove the four-constituent assertion directly, using flags and compact averages.

The normalized inducing character is \(\delta_B^{-1/2}\), so \(I\) has trivial unnormalized covariance. It is \(C^\infty(\mathcal F)\), where \(\mathcal F\) is the compact space of complete flags in \(F^3\). Let \(X\subset I\) be the pullback of the locally constant functions on planes, and \(Y\subset I\) the pullback of those on lines. Thus \(X=i_{P_{2,1}}(\nu^{-1/2}\circ\det\boxtimes\nu)\) and \(Y=i_{P_{1,2}}(\nu^{-1}\boxtimes\nu^{1/2}\circ\det)\). Their intersection is the constants: any two lines lie in a common plane, so a function depending only on a line and only on its incident plane has the same value on all flags. Define
\[
\alpha=X/\mathbb C,\qquad \beta=Y/\mathbb C,\qquad
\mathrm{St}_3=I/(X+Y).
\tag{6.2}
\]

**Lemma 6.1 (detection by an Iwahori subgroup).** Every nonzero subquotient of \(I\) has nonzero invariants under
\(J=\{g\in\mathrm{GL}_3(\mathcal O):g\bmod\varpi\text{ is upper triangular}\}\).
Consequently a subquotient with a simple \(e_J\mathcal H(G_3)e_J\)-module of invariants is irreducible.

**Proof.** The proof of Lemma 1.2 applies with
\(J=U(\mathcal O)\,T(\mathcal O)\,\bar U(\varpi\mathcal O)\).
Both orders of this factorization hold by triangular elimination; their product Haar measures are Haar measure on \(J\), as can be checked in the finite congruence quotients. A strictly contracting diagonal \(a\) gives (1.7), and the finite-dimensional image \(q_U(V^J)\) is \(a\)-stable and hence \(a\)-bijective. Lifting and translating an arbitrary \(T(\mathcal O)\)-invariant Jacquet vector therefore proves
\[
V^J\longtwoheadrightarrow (r_BV)^{T(\mathcal O)}
\]
for any admissible \(V\), just as before.

A nonzero subquotient \(W\) of \(I\) has an irreducible subquotient \(\tau\), by the cyclic-module argument. Its support is the three unramified characters of \(I\), by Theorem 1.6. That theorem embeds \(\tau\) in a Borel induction of some ordering of them; adjunction gives a nonzero unramified character quotient of \(r_B\tau\). Compact averaging and the displayed surjection imply \(\tau^J\ne0\), and exactness of \(J\)-invariants gives \(W^J\ne0\). A proper nonzero submodule and its nonzero quotient would therefore give a proper nonzero submodule of the fixed-space module, proving the last assertion. ∎

**Proposition 6.2.** The four representations \(\mathbf1,\alpha,\beta,\mathrm{St}_3\) are irreducible and pairwise distinct. Each occurs once in \(I\).

**Proof.** Reduction modulo \(\varpi\), followed by the finite-field Bruhat decomposition, gives six \(J\)-orbits on \(\mathcal F\), indexed by \(w\in S_3\). One can obtain the decomposition by ordinary row elimination, with each pivot determining the next value of the permutation. Thus \(I^J\) is the six-dimensional space of functions \(f(w)\). The plane space \(X^J\) has three coordinates, the position of \(3\) in \(w\); the line space \(Y^J\) has three coordinates, the position of \(1\). Let
\[
T_i=1_{Js_iJ},\quad s_i=(i,i+1),\quad\operatorname{vol}(J)=1,
\qquad
\Omega=\begin{pmatrix}0&1&0\\0&0&1\\\varpi&0&0\end{pmatrix}.
\]
The latter normalizes \(J\) and has cube \(\varpi I_3\), which acts trivially on \(I\). Summing the \(q\) right cosets \(n_i(t)s_iJ\), \(t\) in the residue field, gives
\[
(T_if)(w)=
\begin{cases}
qf(ws_i),&w(i)<w(i+1),\\
f(ws_i)+(q-1)f(w),&w(i)>w(i+1).
\end{cases}
\tag{6.3}
\]
For the first case the conjugate of \(n_i(t)\) is upper triangular and its covariance is one. For the second, the zero value of \(t\) gives \(ws_i\), and elementary elimination with \(t\ne0\) gives the orbit \(w\). Also
\((\Omega f)(w)=f(w(3),w(1),w(2))\): remove the diagonal powers on the left, where the covariance is one.

On the quotients by constants use coordinates \((f_1-f_3,f_2-f_3)\). The matrices are
\[
\begin{array}{c|cc}
&T_1&T_2\\ \hline
\alpha^J&
\begin{pmatrix}q-1&1\\q&0\end{pmatrix}&
\begin{pmatrix}q&-q\\0&-1\end{pmatrix}\\[2pt]
\beta^J&
\begin{pmatrix}0&q\\1&q-1\end{pmatrix}&
\begin{pmatrix}q&-1\\0&-1\end{pmatrix}.
\end{array}
\qquad
\Omega_\alpha=\Omega_\beta=
\begin{pmatrix}-1&1\\-1&0\end{pmatrix}.
\tag{6.4}
\]
There is no common eigenline for \(T_1,T_2\) in either row. In the first row the \(T_1\)-eigenlines are \((1,1)\), \((1,-q)\), whereas those of \(T_2\) are \((1,0)\), \((q,q+1)\). In the second they are \((1,1)\), \((-q,1)\), versus \((1,0)\), \((1,q+1)\). None coincide for \(q>1\). Thus both fixed modules are simple, and Lemma 6.1 makes \(\alpha,\beta\) irreducible. They are distinct since
\[
\operatorname{tr}_{\alpha^J}(T_1\Omega)=0,\qquad
\operatorname{tr}_{\beta^J}(T_1\Omega)=1-q.
\tag{6.5}
\]

Exact compact averaging gives \(\dim(X+Y)^J=3+3-1=5\), so \(\mathrm{St}_3^J\) is one dimensional and Lemma 6.1 makes \(\mathrm{St}_3\) irreducible. It has \(T_i=-1\), \(\Omega=1\). Indeed (6.3) has trace \(3(q-1)\) on \(I^J\), while each three-dimensional partial-flag space has trace \(2q-1\) and the constants have trace \(q\); subtraction leaves \(-1\). The trace of \(\Omega\) is zero on each of those three spaces, while it is one on constants, leaving \(1\) on the quotient. This distinguishes it from the constants, on which \(T_i=q\). Fixed dimensions distinguish both from \(\alpha,\beta\). Finally
\((X+Y)/\mathbb C=\alpha\oplus\beta\).
The filtration by constants, \(X+Y\), and \(I\) therefore has precisely the four asserted simple factors, each once. ∎

We also need to identify the two mixed Langlands quotients, rather than just count four factors. We record the duality details used here. For an admissible representation, compact averaging identifies \((V^\vee)^J=(V^J)^*\). It implies smooth biduality. It also makes the smooth dual irreducible when \(V\) is irreducible: a nonzero dual submodule has zero annihilator in \(V\); averaging gives zero annihilator on every finite-dimensional \(V^J\), so that submodule has all dual fixed spaces.

Normalized parabolic induction has dual \(i_P(\tau^\vee)\). Its pairing is
\(\int_K\langle f(k),h(k)\rangle\,dk\).
The integrand has left covariance \(\delta_P\). The Iwasawa Haar formula gives compact-flag change-of-variable density \(\delta_P^{-1}\), so these factors cancel under right translation. This proves invariance; the Haar formula follows directly by changing \(u\mapsto mum^{-1}\) in the block unipotent coordinates, whose Jacobian is \(\delta_P(m)\). On every fixed space, the finitely many double-coset values pair the finite-dimensional fixed spaces of \(\tau\) and \(\tau^\vee\), with nonzero volume weights. The pairing is perfect there, so taking their union gives exactly the smooth dual. This is the general block version of the complete pairing proof in [Normalized induction and Jacquet modules, Proposition 1.2](../../automorphic-forms-and-representations-of-gl2/src/normalized-induction-and-jacquet-modules.md#1-induction-with-the-square-root-modulus).

**Proposition 6.3.** In this example the Langlands quotients are
\[
\begin{array}{c|c}
\mathfrak m&L(\mathfrak m)\\ \hline
\mathfrak m_0&\mathbf1_{G_3}\\
\mathfrak m_1&\beta\\
\mathfrak m_2&\alpha\\
\mathfrak m_3&\mathrm{St}_3.
\end{array}
\tag{6.6}
\]
Each of the defining standard modules has a unique irreducible quotient.

**Proof.** Adjacent exchanges of character factors preserve the composition factors of their rank-two induction: the two exceptional sequences (3.2)–(3.3) have the same factors, and all other exchanges are isomorphisms. Exactness and induction in stages apply this to adjacent factors in a rank-three induction. Thus every ordering of these three characters has the four composition factors just computed, with the same multiplicities. In particular \(I^\vee=\nu\times1\times\nu^{-1}\) does.

On a dual fixed space \(T_i\) acts by the transpose, and \(\Omega\) by the inverse transpose, since inversion fixes \(Js_iJ\) and sends \(\Omega\) to \(\Omega^{-1}\). The two-dimensional factors must therefore dualize to \(\alpha\) or \(\beta\). Since \(\Omega^{-1}=-I-\Omega\) on (6.4), the dual trace of \(T_1\Omega\) for \(\alpha\) is \(1-q\); for \(\beta\) it is zero. Equation (6.5) proves
\(\alpha^\vee=\beta\), \(\beta^\vee=\alpha\).
The one-dimensional fixed character \(T_i=-1,\Omega=1\) similarly gives \(\mathrm{St}_3^\vee=\mathrm{St}_3\).

The extensions
\[
0\longrightarrow\beta\longrightarrow I/X
 \longrightarrow\mathrm{St}_3\longrightarrow0,\qquad
0\longrightarrow\alpha\longrightarrow I/Y
 \longrightarrow\mathrm{St}_3\longrightarrow0
\tag{6.7}
\]
do not split. Here is a check using the same operators. The simultaneous \(T_i=-1\) line in \(I^J\) is spanned by \(f_-(w)=(-q)^{-\ell(w)}\), by (6.3). Its image is the unique such line in either quotient. For justification of uniqueness, the operators \(T_i\) are self-adjoint for the finite-flag inner product with weight \(q^{\ell(w)}\); this is also seen by pairing the two entries \(w,ws_i\) in (6.3). An invariant subspace consequently has an invariant orthogonal complement, so taking either quotient cannot create an additional simultaneous sign line.

The difference \(\Omega f_- - f_-\) does not lie in \(X^J\): at \(123,213\), whose position of \(3\) is the same, its values are \(q^{-2}-1\) and \(-q^{-3}+q^{-1}\), which differ for \(q>1\). It does not lie in \(Y^J\) either: at \(123,132\), whose position of \(1\) is the same, the values are \(q^{-2}-1\) and zero. Thus the sign line in either quotient fails to be \(\Omega\)-fixed. A splitting would embed \(\mathrm{St}_3\) and its fixed character there, a contradiction.

Inducing the rank-two exact sequences gives
\[
I/X=(\mathrm{St}_2\otimes\nu^{-1/2})\times\nu,\qquad
I/Y=\nu^{-1}\times(\mathrm{St}_2\otimes\nu^{1/2}).
\]
Their duals are
\((\mathrm{St}_2\otimes\nu^{1/2})\times\nu^{-1}\) and
\(\nu\times(\mathrm{St}_2\otimes\nu^{-1/2})\), respectively. These are the decreasing mixed standard modules for \(\mathfrak m_2,\mathfrak m_1\). The nonsplit extensions (6.7) and the dual identities give unique irreducible quotients \(\alpha\) and \(\beta\), respectively. A nonsplit length-two extension of two distinct simples cannot have both as quotients: the two kernels would intersect trivially, making it the direct sum.

For \(I\) itself the only possible irreducible quotient is \(\mathrm{St}_3\). To a quotient \(\alpha\), the restriction to \(Y\) is zero, since the factors of \(Y\) are \(\mathbf1,\beta\); the map factors through \(I/Y\), contradicting its nonsplit extension. The case of \(\beta\) uses \(I/X\). A quotient onto constants would give a \(T_i=q,\Omega=1\) functional on \(I^J\).

The unique \(T_i=q\) functional on \(I^J\) has coefficients \(q^{\ell(w)}\), by the paired recurrence from (6.3). They are not invariant under the cyclic permutation \(\Omega\): the coefficients at \(123\) and \(312\) are \(1,q^2\). Thus no constant-character quotient exists, proving that \(I\) has the unique quotient \(\mathrm{St}_3\).

It also has the unique irreducible subrepresentation \(\mathbf1\). A possible \(\mathrm{St}_3\) submodule is excluded because its unique sign line \(f_-\) is not \(\Omega\)-fixed in \(I^J\). A two-dimensional simple submodule has zero image in the simple \(\mathrm{St}_3\) quotient, since otherwise it would be isomorphic to that quotient, contradicting its fixed dimension. It therefore lies in \(X+Y\). Projecting to \(\alpha\oplus\beta\) puts it in its corresponding partial-flag space. Its inclusion would split that space's extension by constants, hence give a retraction to constants. But on \(X^J\) and \(Y^J\) the unique \(T_i=q\) functional has coordinates \(q^2,q,1\), respectively \(1,q,q^2\); neither is \(\Omega\)-invariant. Such retractions are impossible. Duality now gives the unique quotient \(\mathbf1\) of \(I^\vee\). This completes every quotient identification in (6.6). ∎

Genericity can also be checked without the general criterion in Theorem 2.3. Coinvariants for a smooth character \(\psi_N\) of \(N\) are exact, by the compact averaging proof of Lemma 1.1 with the average weighted by \(\psi_N^{-1}\). Take \(\psi_N\) nontrivial on each simple-root subgroup. In the full-flag Bruhat filtration every cell except \(w_0=321\) has an adjacent ascent. Its stabilizer then contains that simple-root subgroup, acting trivially on the induced value and nontrivially through \(\psi_N\), so its twisted coinvariant is zero. The long cell has trivial stabilizer and twisted coinvariant \(\mathbb C\), given by integrating against \(\psi_N^{-1}\). The compact-average fiber proof of Lemma 1.5 works with this weight as well. Thus \(\dim I_{N,\psi_N}=1\).

For either partial-flag space a minimum-length representative preserves the order of \(1,2\), respectively \(2,3\), and therefore cannot be \(321\). Each of its three cells has an adjacent ascent, so \(X_{N,\psi_N}=Y_{N,\psi_N}=0\). Exactness proves that \(\alpha,\beta,\mathbf1\) are nongeneric and that \(\mathrm{St}_3\) is generic. This calculation proves constituent structure and genericity. It does not establish temperedness. The mixed segment centers are \(-1/2,1/2\), and the singleton centers are \(-1,0,1\); the assertion that only the full centered segment is tempered is a further known theorem whose proof remains to be supplied.

## 7. Exercises and solutions

**Exercise 7.1 (easy).** List all linked pairs of singleton segments of total degree two. Decide what happens for \(\{[\chi],[\chi]\}\) and for \(\{[\chi],[\chi\nu^2]\}\).

**Solution.** Both entries must be characters. The complete list is \(\{[\chi],[\chi\nu]\}\), with the unordered pair understood; writing \(\chi\nu^{-1}\) as the first entry gives the same list. Equal singleton segments contain each other, so are not linked. The twists separated by two have a gap, so their union is not a segment. Both of the latter pairs give irreducible principal series by the rank-one criterion.

**Exercise 7.2 (medium).** Show directly that \(Q([\nu^{-1/2},\nu^{1/2}])\) is square-integrable. Identify a coefficient and its squared integral when \(I\) has volume one.

**Solution.** Sequence (3.2) identifies the quotient with \(\mathrm{St}_2\). The invariant-line coefficient normalized to value one at the identity satisfies \(|c|=q^{-r}\) on a double coset of length \(r\), by the two Hecke eigenvalues \(-1\). The coset volume is \(q^r\), so its contribution to the squared integral is \(q^{-r}\). Counting lengths gives \(2+4/(q-1)\). Irreducibility makes all coefficients finite sums of translates of this one, completing the required square-integrability proof. This uses the computation of Section 5, rather than the square-integrability assertion of the general classification.

**Exercise 7.3 (medium).** Determine the multisegments and multiplicities of the constituents of \(\nu^{-1}\times1\times\nu\), and determine which constituents are generic. A further problem is to determine which are tempered; that part is deferred until the tempered classification is proved.

**Solution.** Choosing cuts between \(-1,0\) and \(0,1\) gives the four multisegments (6.1). The flag filtration has constants, the two partial-flag quotients \(\alpha,\beta\), and \(\mathrm{St}_3\), each once. The explicit two-dimensional operators (6.4) prove that the partial-flag quotients are irreducible and distinct; Iwahori detection proves irreducibility of the one-dimensional fixed-space Steinberg quotient. The nonsplitting and duality arguments of Proposition 6.3 identify their labels as (6.6), including the unique quotients of the two mixed standard modules.

The twisted unipotent coinvariant calculation at the end of Section 6 shows directly that only \(\mathrm{St}_3\) is generic. The further temperedness problem remains unsolved here: the mixed rows have nonzero segment centers and the singleton row has centers \(-1,0,1\), while the full Steinberg segment is centered. Converting these observations into a temperedness proof requires the missing square-integrability and tempered classification arguments.

**Exercise 7.4 (hard).** Prove uniqueness of cuspidal support for \(G_2\) from its geometric lemma. Explain why knowing only the central character would be insufficient.

**Solution.** The open-cell coinvariant is integration on \(C_c^\infty(F)\), with normalized diagonal character \(\chi_2\boxtimes\chi_1\); the closed-cell coinvariant is evaluation, with character \(\chi_1\boxtimes\chi_2\). Exactness of Jacquet modules, proved by compact averaging in Lemma 4.1, gives these two characters for a principal series. At the reducibility point the determinant character contributes (4.2), leaving (4.3) for Steinberg. Thus every non-supercuspidal irreducible has a nonzero Jacquet character whose unordered pair is precisely its support. Any other character induction containing it has, by the rank-one constituent calculation, the same unordered pair. A supercuspidal has itself as its only possible support because it cannot occur in a proper induction. This is Theorem 4.2 with every geometric-lemma step specified.

The central character records only the product of the support characters. For example, \(I(\nu^t,\nu^{-t})\) has trivial central character for every \(t\); choosing \(t=0\) and \(t=1\) gives two irreducible principal series with different supports. Their Jacquet modules distinguish them. ∎

## Appendix A. Mirabolic derivatives and their exact filtration

Segments are not classified merely by computing their support. The proof also needs functors that remove a final row while retaining its unipotent character. We establish those functors and their product rule here. All the arguments use locally constant functions and compact averages, so they work in both characteristics, including residue characteristic two.

For this appendix the intermediate categories consist of smooth complex modules. Mirabolic modules need not be admissible; imposing admissibility on them would discard the compactly induced modules below. Put \(G_0=\{1\}\) and
\[
\mathcal P_n=
\left\{\begin{pmatrix}g&u\\0&1\end{pmatrix}:
 g\in G_{n-1},\ u\in F^{n-1}\right\},
\qquad
A_n=\left\{\begin{pmatrix}I&u\\0&1\end{pmatrix}\right\}.
\tag{A.1}
\]
Thus \(\mathcal P_n=G_{n-1}A_n\), and \(A_n\) is an abelian normal subgroup. Fix a nontrivial smooth additive character \(\psi:F\to\mathbb C^\times\) and set \(\eta_n(u)=\psi(u_{n-1})\). Its stabilizer in \(G_{n-1}\) is \(\mathcal P_{n-1}\): the last row must be \((0,\ldots,0,1)\).

For an \(A\)-character \(\chi\), write
\[
V_{A,\chi}=V/\langle\pi(a)v-\chi(a)v:a\in A,\ v\in V\rangle.
\]
Weighted compact averaging proves its exactness just as in Lemma 1.1, using \(E_{C,\chi}=\operatorname{vol}(C)^{-1}\int_C\chi(c)^{-1}\pi(c)\,dc\).

### The two Fourier orbits

**Lemma A.1 (Fourier localization).** For \(A=F^m\), a smooth \(A\)-module is a nondegenerate module over \(C_c^\infty(F^m)\) with pointwise multiplication, via Fourier transformation of its integrated \(A\)-action. Its fiber at the row vector \(\xi\) is \(V_{A,\psi(\xi\,\cdot)}\). Fibers are exact, and a vector whose fibers all vanish is zero.

**Proof.** Integration sends \(f\in C_c^\infty(A)\) to \(\int f(a)\pi(a)\,da\), a finite sum on each smooth vector. Fourier transformation
\(\widehat f(\xi)=\int f(a)\psi(\xi a)\,da\)
sends convolution to pointwise multiplication. It is an isomorphism on locally constant compactly supported functions: on a compact lattice and a finite lattice quotient it is the finite Fourier transform, whose inverse follows from character orthogonality; enlarging the lattice and refining its quotient covers every test function. For completeness, if \(\psi\) is trivial on \(\varpi^c\mathcal O\) and nontrivial on \(\varpi^{c-1}\mathcal O\), the annihilator of \(\varpi^r\mathcal O\) is \(\varpi^{c-r}\mathcal O\). This follows by multiplying these ideals; below the indicated valuation their product contains an ideal on which \(\psi\) is nontrivial. The pairing between any lattice quotient and the quotient of its annihilator lattices is therefore nondegenerate and has equal finite cardinalities. Coordinate products give the same assertion for \(F^m\). Choose compatible Haar measures for the inverse. In particular a normalized compact average becomes \(1_{C^\perp}\). Every vector is fixed by such an average, so the resulting pointwise-function action is nondegenerate and each vector has compact Fourier support.

For a point \(\xi\), quotient by the ideal of test functions vanishing at \(\xi\). Since a test is locally constant, this quotient is equivalently the direct limit of \(1_DV\) as compact open neighborhoods \(D\) shrink to \(\xi\), with transition maps given by their projections. These projections are exact; filtered direct limits of vector spaces are exact.

The \(A\)-relation \(\pi(a)v-\psi(\xi a)v\) is multiplication, on the compact support of \(v\), by the locally constant function
\(\psi(\zeta a)-\psi(\xi a)\), which vanishes near \(\xi\). Conversely, if a test function vanishes near \(\xi\), cover its compact support by finitely many compact open sets on each of which such a difference is a nonzero constant. This is possible because different row vectors define different additive characters. A clopen partition subordinate to this cover writes that test's action as a sum of these \(A\)-relations. The two quotients therefore agree.

Finally, if every fiber of \(v\) is zero, each point in its compact Fourier support has a neighborhood \(D\) with \(1_Dv=0\). A finite cover and disjoint clopen refinement of that support give \(v=0\). ∎

We spell out the compact-section interpretation rather than assume a sheaf equivalence. Over a compact open set \(D\), a vector \(v\) gives the section consisting of its germs in the fibers, restricted by \(1_D\). Define local sections to be sections locally obtained this way. A compactly supported local section comes from a vector: cover its compact support by finitely many such descriptions, refine them to disjoint clopen sets, multiply their vectors by the corresponding characteristic functions, and add. The zero section comes only from the zero vector by Lemma A.1. Thus the module is precisely the space of compactly supported sections of its fiber system.

Conjugation by \(g\in G_m\) transports the fiber at \(\xi\) to the fiber at \(\xi g^{-1}\). There are two orbits: \(\{0\}\) and \(O=F^m\setminus\{0\}\). The kernel of the zero-fiber map is exactly \(C_c^\infty(O)V\): a test vanishing at zero vanishes on a neighborhood of zero and hence has compact support inside \(O\). In particular the open part has compact support inside the open orbit, not support merely compact in its closure.

For a transitive orbit the fiber system is determined by one fiber and its stabilizer action. Here is the explicit local construction. On a patch where \(\xi_j\ne0\), take a matrix \(s(\xi)\) whose last row is \(\xi\), and whose other rows are the standard rows except for the \(j\)-th one. This is invertible, with determinant \(\pm\xi_j\), and is a continuous section of \(G_m\to O\). Transport by \(s(\xi)^{-1}\) identifies the chosen fiber with the fiber at \(\xi\). Changing the section multiplies by a stabilizer element; its action on a fixed vector is locally constant by smoothness. Conversely a smooth group module gives these local identifications: near a fixed \(\xi\), the difference between its section matrices lies in a subgroup fixing any chosen lift of the fiber vector. This verifies local compatibility in both directions. Compact support and a finite clopen partition then identify the module on \(O\) with compact induction from the stabilizer.

### Normalized functors and the canonical filtration

For \(n\ge2\), define
\[
\begin{aligned}
\Psi_n^-V&=\nu^{-1/2}V_{A_n},
&\Psi_n^+\sigma&=\nu^{1/2}\sigma
   \quad\text{inflated to }\mathcal P_n,\\
\Phi_n^-V&=\nu^{-1/2}V_{A_n,\eta_n},
&\Phi_n^+\tau&=
 \operatorname{c-Ind}_{\mathcal P_{n-1}A_n}^{\mathcal P_n}
       (\nu^{1/2}\tau\otimes\eta_n).
\end{aligned}
\tag{A.2}
\]
In the compact induction, functions have left covariance
\(f(pax)=|\det p|^{1/2}\tau(p)\eta_n(a)f(x)\), compact support modulo \(\mathcal P_{n-1}A_n\), and smooth right translation. The character \(\nu\) means \(|\det|\) on the indicated smaller matrix group. On \(\mathcal P_1=G_0=\{1\}\), \(\Psi_1^\pm\) are the identity; no \(\Phi_1^\pm\) is needed.

**Theorem A.2.** All four functors are exact. There are natural identities
\[
\Psi^-\Psi^+=\mathrm{id},\qquad
\Phi^-\Phi^+=\mathrm{id},\qquad
\Psi^-\Phi^+=0,\qquad \Phi^-\Psi^+=0
\tag{A.3}
\]
and a natural short exact sequence
\[
0\longrightarrow\Phi^+\Phi^-V
 \longrightarrow V
 \longrightarrow\Psi^+\Psi^-V
 \longrightarrow0.
\tag{A.4}
\]
The first term is the open Fourier-orbit part of \(V\). Compact induction \(\Phi^+\) gives an equivalence between smooth \(\mathcal P_{n-1}\)-modules and smooth \(\mathcal P_n\)-modules with \(\Psi^-=0\).

**Proof.** Lemma A.1 gives the exact fibers at zero and at \(e_{n-1}\). The zero orbit inflates its \(G_{n-1}\)-module, while the open orbit is the compact induction constructed above. Its unnormalized stabilizer fiber is \(\nu^{1/2}\Phi^-V\); thus the square-root factors in (A.2) cancel in reconstructing it. At zero they similarly cancel between \(\Psi^-\) and \(\Psi^+\). The orbit decomposition therefore gives (A.4) and all four identities in (A.3).

The section construction on a transitive orbit has exact fibers. Compactly supported sections lift across a fiberwise surjection by choosing lifts on a finite family of trivializing patches and taking a disjoint clopen refinement. If stabilizer invariance is required on such a patch, averaging over a sufficiently small compact subgroup gives a lift with that invariance. Hence compact induction here is exact. Inflation and twists are exact as well. Evaluation at the distinguished fiber and reconstruction of its compact sections are inverse functors on the open orbit, proving the asserted equivalence. These constructions commute with homomorphisms, so all maps and identities are natural. ∎

This sequence need not split. For \(n=2\), take \(V=C_c^\infty(F)\) with
\[
\pi\!\begin{pmatrix}a&b\\0&1\end{pmatrix}f(x)
 =\psi(bx)f(ax).
\]
The exact sequence is
\(0\to C_c^\infty(F^\times)\to C_c^\infty(F)\xrightarrow{f\mapsto f(0)}\mathbb C\to0\).
Its final character is trivial on \(\mathcal P_2\), corresponding to \(\Psi_2^+(\nu^{-1/2})\). A section would supply a nonzero vector fixed by every upper unipotent. The equation \(\psi(bx)f(x)=f(x)\) for every \(b\) forces support inside \(\{0\}\); local constancy then forces \(f=0\). This proves nonsplitting and illustrates why a fiber at zero is a quotient, rather than a subspace of functions supported at that point.

For a smooth \(\mathcal P_n\)-module \(V\), its \(k\)-th derivative is
\[
V^{(k)}=\Psi_{n-k+1}^-
 \Phi_{n-k+2}^-\cdots\Phi_n^-V,
\qquad 1\le k\le n.
\tag{A.5}
\]
For a \(G_n\)-representation use its restriction to \(\mathcal P_n\), and set \(\pi^{(0)}=\pi\).

**Corollary A.3.** Every smooth \(\mathcal P_n\)-module has a canonical finite filtration with terms
\[
(\Phi^+)^{k-1}\Psi^+(V^{(k)}),\qquad 1\le k\le n.
\tag{A.6}
\]
Every irreducible smooth \(\mathcal P_n\)-module is uniquely
\((\Phi^+)^{k-1}\Psi^+\sigma\), for one \(k\) and one irreducible smooth \(G_{n-k}\)-module \(\sigma\).

**Proof.** Iterate (A.4). More explicitly \(F_0=V\),
\(F_j=(\Phi^+)^j(\Phi^-)^jV\) for \(1\le j<n\), and \(F_n=0\); the natural injections give \(F_j\subset F_{j-1}\). Exactness identifies \(F_{k-1}/F_k\) with (A.6). If \(V\) is irreducible, its open part is either zero or all of it. In the former case it is an inflated irreducible \(G_{n-1}\)-module. In the latter case the equivalence in Theorem A.2 makes \(\Phi^-V\) irreducible. Repeating gives the claimed form. Its only nonzero derivative is the indicated \(\sigma\), which proves uniqueness. This proof uses the smooth categories and does not assume admissibility of mirabolic modules. ∎

### Derivatives are partial Whittaker coinvariants

Write \(N_j\) for the upper maximal unipotent subgroup of \(G_j\), and
\(\psi_j(u)=\psi(u_{12}+\cdots+u_{j-1,j})\). Put
\(\mathcal W_j(\tau)=\tau_{N_j,\psi_j}\) and \(\mathcal W_0(\tau)=\tau\); \(\mathcal W_1\) simply forgets the \(G_1\)-action.

**Proposition A.4.** As a \(G_{n-k}\)-module,
\[
\pi^{(k)}
 \simeq\bigl(r_{(n-k,k)}\pi\bigr)_{N_k,\psi_k},
\qquad 0\le k\le n.
\tag{A.7}
\]
Here \(G_{n-k}\) acts on the first block. In particular an irreducible supercuspidal of \(G_d\) has zero derivatives for \(0<k<d\), and has nonzero top derivative \(\mathcal W_d(\rho)\). Thus every supercuspidal is generic.

**Proof.** The last-column groups successively quotiented in (A.5) generate precisely
\[
\left\{\begin{pmatrix}I_{n-k}&X\\0&u\end{pmatrix}:u\in N_k\right\}.
\]
The \(\Phi^-\) steps put \(\psi\) on the last \(k-1\) simple-root entries, and the final \(\Psi^-\) step puts the trivial character on the rectangular block. Coinvariant transitivity therefore first kills the rectangular block, then takes \(N_k,\psi_k\)-coinvariants.

There are \(k\) factors \(\nu^{-1/2}\) on \(G_{n-k}\), so their product is \(|\det|^{-k/2}\). The normalized \((n-k,k)\)-Jacquet module has exactly this factor on \(\operatorname{diag}(g,I_k)\), since conjugation on the \(k\) rectangular columns has determinant \((\det g)^k\). Its normalization on the second block is trivial on \(N_k\). This proves (A.7), including \(k=n\) and the trivial \(k=0\) convention.

For a supercuspidal, all the proper modules on the right vanish by Lemma 1.4. If its top derivative also vanished, every layer of the finite filtration (A.6) of its nonzero restriction would vanish, a contradiction. A nonzero linear functional on its top coinvariant space is a nonzero Whittaker functional. ∎

Nonzero top derivative is the existence assertion. Its dimension-one assertion is proved in Appendix B and is not inferred from this filtration: a direct sum of several copies of the open-orbit module has the same vanishing lower derivatives.

### Whittaker induction and the Leibniz filtration

**Lemma A.5.** For normalized induction from any block parabolic \(R=LU_R\),
\[
\mathcal W_n(i_R\tau)
 \simeq \tau_{N_L,\psi_L}.
\tag{A.8}
\]
For an external tensor product \(\tau=\boxtimes_i\tau_i\), this is
\(\bigotimes_i\mathcal W_{d_i}(\tau_i)\). No uniqueness or finite-dimensionality hypothesis is needed for this vector-space identity.

**Proof.** Filter the compact flag space \(R\backslash G_n\) by its \(N_n\)-orbits, exactly as for the cell filtration in Lemma 1.5. They are indexed by the minimum-length representatives in \(W_L\backslash S_n\). If \(c(w(j))\) is the \(L\)-block containing \(w(j)\), the unique open representative has the block labels in decreasing order, and has the entries inside each block in increasing order.

Every other representative has an adjacent increase \(c(w(j))<c(w(j+1))\). The corresponding simple-root subgroup is in \(N_n\cap w^{-1}U_Rw\). It acts trivially on the inducing value, whereas \(\psi_n\) is nontrivial on it. Its twisted value coinvariants, and hence this cell's contribution, vanish. The combinatorial assertion follows directly: a sequence with no adjacent increase is decreasing in its block labels; the minimum-length condition already fixes the order inside each block, so there is just one such representative.

On the open cell the stabilizer is \(H=w^{-1}N_Lw\). Its character is the restriction of \(\psi_n\), which conjugates to \(\psi_L\), since each block occurs contiguously and its entries keep their order. The fiber map is
\[
h\longmapsto
 \int_{H\backslash N_n}[h(u)]\,\psi_n(u)^{-1}\,d\dot u
 \quad\text{in }\tau_{N_L,\psi_L}.
\tag{A.9}
\]
The bracket transforms by \(\psi_n|_H\), so the integrand is well defined. The compact-average proof of (1.11) applies with each average weighted by \(\psi_n^{-1}\). In detail, averaging over a compact \(C\) makes a fiber section satisfy the right character on \(C\); its integral is a nonzero volume times the class of its value at \(1\). If that class is zero, a larger compact subgroup of \(H\) has zero weighted average of the value. Enlarge \(C\) to include it; the resulting weighted right average of the section is zero. This identifies the kernel with the twisted translation relations. Choosing a small compact \(C\) fixing a lifted value through the character gives surjectivity. Thus (A.9) identifies the open-cell coinvariant with the asserted space. Exactness of weighted coinvariants removes all the other cells. The tensor assertion follows by taking the separate factor coinvariants; their relation spaces quotient a tensor product to the tensor product of the quotients. ∎

**Theorem A.6 (Leibniz rule).** For smooth \(\sigma\) on \(G_a\), smooth \(\tau\) on \(G_b\), and \(0\le k\le a+b\), \((\sigma\times\tau)^{(k)}\) has a finite filtration with terms
\[
\sigma^{(i)}\times\tau^{(j)},
\qquad i+j=k,\quad 0\le i\le a,\quad0\le j\le b.
\tag{A.10}
\]
This asserts a filtration and does not split it. If their highest nonzero derivative orders are \(r,s\), the product's highest order is \(r+s\), and its highest derivative is
\(\sigma^{(r)}\times\tau^{(s)}\).

**Proof.** Apply Proposition A.4 and the block geometric lemma to
\(r_{(a+b-k,k)}(i_{(a,b)}(\sigma\boxtimes\tau))\).
Its intersection matrices are precisely
\[
\begin{pmatrix}a-i&i\\b-j&j\end{pmatrix},
\qquad i+j=k.
\]
The term associated to this matrix first takes \(r_{(a-i,i)}\sigma\) and \(r_{(b-j,j)}\tau\), then induces their first components into \(G_{a+b-k}\) and their second components into \(G_k\), with the factors regrouped by columns. Taking the final \(N_k,\psi_k\)-coinvariant and applying Lemma A.5 to that second induction gives (A.10), by (A.7) for each row.

All statements remain statements about the original modules, rather than just their composition factors. Coinvariants commute with compactly supported induction in the other factor: use its finite clopen value descriptions, perform the fiber integrals on those values, and use the same lifts and compact-average kernel calculation as in (1.11). This produces the natural cell isomorphisms even when a row Jacquet module is an extension instead of a tensor sum. Normalizations also agree: the row Jacquet factors followed by the column induction have the modulus identity (1.12), and (A.7) accounts for the remaining \(k\) half powers. Thus no extra unramified twist occurs.

For \(k>r+s\), every term has a vanishing factor. At \(k=r+s\) the only possibly nonzero term has \(i=r,j=s\); it is nonzero because induction of a nonzero external tensor product is nonzero, as is seen by extending a nonzero value over a small clopen patch of its flag space. The single-term filtration gives the claimed isomorphism. ∎

For \(k=a+b\), this recovers the particularly useful identity
\[
\mathcal W_{a+b}(\sigma\times\tau)
 \simeq\mathcal W_a(\sigma)\otimes\mathcal W_b(\tau).
\tag{A.11}
\]
Consequently any induction of supercuspidals is generic. When the factors' Whittaker spaces have finite dimensions, those dimensions multiply. Appendix B proves dimension one for supercuspidals and Whittaker uniqueness for every irreducible. The general cuspidal product reducibility calculation and subsequent segment and multisegment arguments require their own proofs; the existence and product identities alone do not establish them.

### Distinct unitary supercuspidals

The finite-length and geometric results also prove an initial all-rank irreducibility case without a reducibility calculation.

**Proposition A.7.** Let \(\rho_1,\ldots,\rho_t\) be pairwise nonisomorphic irreducible supercuspidals, each with unitary central character. Then
\[
\rho_1\times\cdots\times\rho_t
\tag{A.12}
\]
is irreducible and unitary. It is generic by Lemma A.5. The same irreducibility conclusion holds after a common twist \(\nu^s\). Repeated factors and independently chosen nonunitary twists are outside this proposition.

**Proof.** Lemma 1.4 gives each \(\rho_i\) an invariant positive Hermitian form. Their tensor product has such a form as well. In the compact model of normalized induction the form
\(\langle f,h\rangle=\int_K\langle f(k),h(k)\rangle\,dk\)
is positive and nondegenerate. The block Haar calculation in Section 6 proves invariance: the inducing covariance contributes \(\delta_P\), and the compact-flag change of variables contributes \(\delta_P^{-1}\).

We justify the use of semisimplicity on the smooth module. If an admissible smooth unitary module \(V\) has an invariant submodule \(W\), and \(v\in V^J\), take the ordinary finite-dimensional orthogonal projection \(w\) of \(v\) onto \(W^J\). For \(z\in W\), compact averaging gives
\(\langle v-w,z\rangle=\langle v-w,E_Jz\rangle=0\).
Thus \(v=w+(v-w)\) lies in \(W+W^\perp\). Every vector is fixed by some \(J\), so \(V=W\oplus W^\perp\); the orthogonal complement is invariant. A finite-length such module is therefore a finite direct sum of irreducibles. Our induced module is admissible by Lemma 1.1 and has finite length by Corollary 1.7, so this argument applies.

Write \(\sigma=\boxtimes_i\rho_i\) and let \(P\) have the corresponding ordered block sizes. Frobenius adjunction identifies its endomorphism space with
\[
\operatorname{Hom}_M\!\left(r_Pi_P\sigma,\sigma\right).
\]
In the geometric filtration of this Jacquet module, a row split into two nonzero entries gives a proper Jacquet module of its supercuspidal and hence contributes zero. A column containing two or more unsplit rows cannot have the required supercuspidal factor as a subquotient, by Lemma 1.4. Hence only permutations of whole blocks can contribute \(\sigma\). Such a term contributes precisely when it preserves both the block sizes and their representation labels. Pairwise nonisomorphism leaves only the identity permutation, whose term is \(\sigma\) once.

Each relevant Levi module has finite length: the nonzero cell terms are inductions of supercuspidals, covered by Corollary 1.7. In a finite-length module the dimension of \(\operatorname{Hom}(-,\sigma)\) is at most the multiplicity of \(\sigma\): apply the left-exact Hom functor to a composition series and use scalar Schur's lemma from Lemma 1.3. Thus the induced module has endomorphism space of dimension at most one, and its identity endomorphism makes the dimension exactly one. A nontrivial finite direct sum has at least two independent summand projections. Semisimplicity therefore forces this induced module to be irreducible. A common determinant twist is an equivalence and preserves irreducibility. ∎

### Pairings on the mirabolic group

The next step needs duality on a nonunimodular group. We fix its factor explicitly. For a locally profinite group \(H\), let \(\Delta_H\) denote its modular character, with right translation on left Haar integrals multiplying them by \(\Delta_H(h)^{-1}\). On \(\mathcal P_n=G_{n-1}\ltimes F^{n-1}\),
\[
\Delta_{\mathcal P_n}(p)=\nu(p)^{-1}.
\tag{A.13}
\]
Indeed left Haar measure in these coordinates is \(|\det g|^{-1}dg\,du\), where \(dg\) is Haar measure on the unimodular matrix group. Right translation by \(g_0\) changes this integral by \(|\det g_0|\). The unipotent translations have factor one. For \(\mathcal P_1=\{1\}\), all factors are one.

Call a bilinear form on \(V\times Y\) a modular pairing when
\[
B(pv,py)=\nu(p)B(v,y).
\tag{A.14}
\]
It corresponds to a map \(V\to D_nY\), where
\(D_nY=(\Delta_{\mathcal P_n}Y)^\vee=\nu Y^\vee\)
and the superscript denotes the smooth dual. A form is nondegenerate in \(V\) when this map is injective. Smoothness of its functional on \(Y\) follows from a compact open stabilizer of \(v\); \(\nu\) is trivial there.

**Lemma A.8 (normalized pairing identities).** Modular pairings of \(\Psi^+\sigma\) and \(\Psi^+\sigma'\) are exactly invariant pairings of \(\sigma\) and \(\sigma'\). Modular pairings of \(\Phi^+\tau\) and \(\Phi^+\tau'\) are exactly modular pairings of \(\tau\) and \(\tau'\) on \(\mathcal P_{n-1}\). Both correspondences preserve nondegeneracy in either argument. A modular pairing of a \(\Psi^+\)-module and a \(\Phi^+\)-module is zero, in either order.

**Proof.** We establish the smooth-dual calculation used for the open orbit, including its measure factor. Put \(Q=\mathcal P_{n-1}A_n\subset\mathcal P_n\), and let \(\widehat\Phi^+\) denote the ordinary smooth induction with the same covariance as \(\Phi^+\), without its compact-support condition. The stabilizer projection \(Q\to\mathcal P_{n-1}\) has the additive kernel \(A_n\). Its conjugation determinant is \(\nu\), so
\[
\Delta_Q=\nu^{-2},\qquad
\frac{\Delta_{\mathcal P_n}|_Q}{\Delta_Q}=\nu.
\tag{A.15}
\]
For \(n=2\), the stabilizer's determinant is one, so these equalities on \(Q=A_2\) still hold.

Here is the integration rule underlying induction duality. If functions have left \(Q\)-covariance \(W\), their dual inducing values have covariance
\((\Delta_{\mathcal P_n}|_Q/\Delta_Q)W^\vee\).
The scalar product of the two values then has left covariance
\(a=\Delta_{\mathcal P_n}|_Q/\Delta_Q\); integrate it as a quotient density on \(Q\backslash\mathcal P_n\). This density has a right-invariant integral. To construct that integral rather than assume it, use the local sections of the nonzero Fourier orbit supplied in Lemma A.1. In the local coordinates \(qs(x)\), right Haar measure disintegrates as
\[
d_Rp=a(q)^{-1}\,d_Rq\,d\mu(x).
\]
The factor follows by left translation: its change is \(a(q_0)\Delta_Q(q_0)=\Delta_{\mathcal P_n}(q_0)\), exactly the change of right Haar measure. Local densities obtained this way agree on overlapping sections by this same change-of-variables identity. Equivalently, for a compact test \(f\), its quotient density is
\(Af(p)=\int_Q a(q)^{-1}f(qp)\,d_Rq\),
and its integral is \(\int_{\mathcal P_n}f(p)\,d_Rp\), by these coordinates. A finite clopen partition proves this equality for arbitrary compact supports and shows that the integral is independent of their descriptions. Right invariance follows from right invariance of \(d_Rp\).

Thus a compact section and an ordinary smooth dual section pair by this integral. All smooth functionals on the compact section module arise in this way. Indeed, a functional fixed by a compact open \(J\) can be evaluated on sections of sufficiently small compact open patches whose lifted values are fixed by their stabilizers. On each such patch, divide the resulting functional of the value by its nonzero density volume. Right \(J\)-invariance makes it constant under refinement of that patch. Changing a lift gives exactly the dual covariance above. The stabilizer's compact open intersection with \(pJp^{-1}\) fixes this value functional, so it lies in the smooth dual of the inducing space. Conversely such a smooth section defines a \(J\)-fixed functional by integration. Compact supports have finite clopen partitions, so these two constructions are inverse. They work for arbitrary smooth inducing modules, with no admissibility assumption.

Apply this rule to \(W=\nu^{1/2}\tau\otimes\eta_n\). The factor \(\nu\) in (A.15) gives the dual covariance \(\nu^{1/2}\tau^\vee\otimes\eta_n^{-1}\). The inverse additive character can be changed back to \(\eta_n\) by conjugation with \(\operatorname{diag}(-I_{n-1},1)\); this matrix centralizes the embedded stabilizer \(\mathcal P_{n-1}\), and its automorphism is inner in \(\mathcal P_n\). Twisting by \(\nu\) may be passed into induction by multiplying functions by \(\nu(p)\). Consequently
\[
D_n\Phi^+\tau\simeq\widehat\Phi^+(D_{n-1}\tau),
\qquad
D_n\Psi^+\sigma\simeq\Psi^+(\sigma^\vee).
\tag{A.16}
\]
For the second identity, the inflated module is \(\nu^{1/2}\sigma\), whose smooth dual is \(\nu^{-1/2}\sigma^\vee\); the factor \(\nu\) in \(D_n\) supplies the asserted half power.

We also prove the adjunction used here. Evaluation at \(1\) identifies a map \(V\to\widehat\Phi^+\lambda\) with a map
\(\Phi^-V\to\lambda\).
The value kills \(\pi(u)v-\eta_n(u)v\); its stabilizer covariance is \(\nu^{1/2}\lambda\), and the twist \(\nu^{-1/2}\) in \(\Phi^-\) removes this factor. Conversely a map \(T:\Phi^-V\to\lambda\) gives the function \(p\mapsto T([\pi(p)v])\). It satisfies the required covariance, and a compact open stabilizer of \(v\) fixes it on the right. These constructions are inverse. In particular \(\Phi^-\widehat\Phi^+\lambda=\lambda\): evaluate at the distinguished Fourier fiber, using the same compact averages as in Lemma A.1. Noncompact sections cause no problem for this fiber; projection onto a sufficiently small compact neighborhood of the nonzero row makes their germ a compact section.

Equations (A.16), the adjunction and \(\Phi^-\Phi^+=\mathrm{id}\) now give
\[
\operatorname{Hom}(\Phi^+\tau,D_n\Phi^+\tau')
 \simeq\operatorname{Hom}(\tau,D_{n-1}\tau').
\tag{A.17}
\]
This proves the pairing correspondence. Its map preserves injectivity: a kernel in \(\Phi^+\tau\) is an open-orbit module by Theorem A.2, so it is zero precisely when its exact \(\Phi^-\)-fiber is zero. That fiber is the kernel of the corresponding map on the right of (A.17). Symmetry of bilinear forms proves the same assertion in the other argument.

The \(\Psi^+\) identity follows directly from its two half powers: their product is \(\nu\), leaving an invariant form on the \(G_{n-1}\)-values. Finally,
\(\operatorname{Hom}(\Psi^+\sigma,D_n\Phi^+\tau)=0\)
by the adjunction and \(\Phi^-\Psi^+=0\). Interchanging the arguments of a bilinear form proves the other order. ∎

**Lemma A.9 (highest-derivative pairing).** Suppose a modular pairing of smooth \(\mathcal P_n\)-modules \(T,Y\) is nondegenerate in \(T\). If \(T^{(k)}\) is its highest nonzero derivative, there is an invariant pairing of \(T^{(k)}\) with \(Y^{(k)}\), nondegenerate in \(T^{(k)}\).

**Proof.** Induct on \(k\). If \(k=1\), all derivatives of \(\Phi^-T\) vanish, so its canonical filtration makes it zero. Thus \(T=\Psi^+T^{(1)}\). Lemma A.8 annihilates the pairing with the open part \(\Phi^+\Phi^-Y\); the resulting pairing with \(\Psi^+Y^{(1)}\) remains nondegenerate in \(T\). The \(\Psi^+\) identity gives the claimed invariant pairing.

For \(k>1\), put \(T_0=\Phi^+\Phi^-T\) and \(Y_0=\Phi^+\Phi^-Y\). The radical in \(T_0\) of the restricted pairing is an invariant submodule \(R\). It is an open-orbit module. Its pairing with \(Y\) factors through \(Y/Y_0=\Psi^+\Psi^-Y\), and this pairing is zero by Lemma A.8. Original nondegeneracy forces \(R=0\). The \(\Phi^+\) identity therefore yields a modular pairing of \(\Phi^-T\) with \(\Phi^-Y\), nondegenerate in the first argument. Its highest derivative has order \(k-1\), and these derivatives are \(T^{(k)}\) and \(Y^{(k)}\). Induction finishes the proof. ∎

### Cuspidal products without adjacent twists

**Theorem A.10.** Let \(\rho_i\) be any finite list of irreducible supercuspidals of \(G_{d_i}\). If
\[
\rho_j\not\simeq\nu\rho_i\quad\text{for every }i,j,
\tag{A.18}
\]
then \(I=\rho_1\times\cdots\times\rho_t\) is irreducible and generic. This includes repeated factors and independent nonunitary twists. In particular a pair is irreducible whenever neither member is a \(\nu\)-twist of the other.

**Proof.** Set \(n=\sum d_i\), and write \(S\) for the cuspidal-support multiset. By Theorem B.3 and the Leibniz rule, every \(I^{(k)}\) has a finite filtration whose nonzero terms are inductions of those \(\rho_i\) not removed: a removed block contributes its one-dimensional top derivative, and its removed rank is \(d_i\). Corollary 1.7 and Lemma 1.1 give these terms finite length and admissibility; exact compact averaging gives the same for their extensions. Theorem 1.6 therefore gives
\[
\operatorname{supp}\sigma\subseteq S
\quad\text{for every irreducible constituent }
\sigma\text{ of }I^{(k)}.
\tag{A.19}
\]
For \(G_0\) this means the empty multiset.

Here is the second support constraint on a highest derivative of a submodule. Smooth duals are exact on admissible modules: on every compact open fixed space they are the ordinary finite-dimensional duals, because averaging identifies \((V^\vee)^J=(V^J)^*\). These identifications also give \(V^{\vee\vee}=V\) and preservation of irreducibility. A supercuspidal's dual is supercuspidal by the compact-coefficient/unitary-twist argument in Theorem B.3. Normalized-induction duality, with its full proof in [Normalized induction and Jacquet modules, Proposition 1.2](../../automorphic-forms-and-representations-of-gl2/src/normalized-induction-and-jacquet-modules.md#1-induction-with-the-square-root-modulus), gives
\[
Y=\nu I^\vee\simeq
(\nu\rho_1^\vee)\times\cdots\times(\nu\rho_t^\vee).
\tag{A.20}
\]
The evaluation pairing of \(I\) with \(Y\) has covariance (A.14) on \(\mathcal P_n\) and separates every vector of \(I\).

Let \(T\) be a nonzero \(\mathcal P_n\)-submodule of \(I\), and let \(k\) be its highest derivative. Such a derivative exists by the canonical filtration. It embeds into \(I^{(k)}\), so it has finite length and has an irreducible submodule \(\sigma\). Lemma A.9 supplies an invariant pairing of \(\sigma\) with \(Y^{(k)}\), nondegenerate in \(\sigma\). Choose a vector of \(Y^{(k)}\) pairing nontrivially with \(\sigma\). It defines a nonzero smooth functional on \(\sigma\); the associated map \(Y^{(k)}\to\sigma^\vee\) is a surjection since \(\sigma^\vee\) is irreducible. Applying (A.19) to (A.20), and then taking duals of the cuspidal supports, gives
\[
\operatorname{supp}\sigma\subseteq\nu^{-1}S.
\tag{A.21}
\]
To justify the support dualization explicitly, embed \(\sigma\) into its cuspidal-support induction using Theorem 1.6. Exact admissible duality and normalized-induction duality make \(\sigma^\vee\) a quotient of the induction of the dual cuspidal entries. The uniqueness in Theorem 1.6 identifies its support with exactly that dual multiset. Together (A.19) and (A.21) therefore force \(\operatorname{supp}\sigma\) into \(S\cap\nu^{-1}S\). Condition (A.18) makes this intersection empty. If \(k<n\), the nonzero irreducible \(\sigma\) belongs to a positive-rank group and its cuspidal support is nonempty by Theorem 1.6. This contradiction proves \(k=n\): every nonzero mirabolic submodule of \(I\) has nonzero top derivative.

Finally \(\dim I^{(n)}=1\) by Theorem B.3. If \(I\) were reducible, finite length and exact top derivatives would give a nongeneric irreducible composition factor \(\omega\). Theorem 1.6 embeds \(\omega\) into an induction of a permutation of the multiset \(S\). This permuted product satisfies the same condition (A.18). Applying the preceding argument to the nonzero mirabolic submodule \(\omega\) would give \(\omega^{(n)}\ne0\), a contradiction. Hence \(I\) is irreducible; its nonzero top derivative proves genericity. ∎

A supercuspidal cannot equal its own \(\nu\)-twist: on a central scalar \(zI_d\), the central character would be multiplied by \(|z|^d\), which is not identically one. Thus \(\rho\times\rho\), and any number of identical copies, are covered. The theorem proves the entire nonadjacent direction for arbitrary ranks and both field characteristics. Proving reducibility at an adjacent pair \(\rho,\nu\rho\), and constructing and classifying all segments and multisegments, are the subsequent steps.

### The adjacent cuspidal pair

The support constraints (A.19) and (A.21) were proved for arbitrary cuspidal products before the no-adjacency hypothesis was used. We will also use them at the adjacent pair. First we supply the continuity argument that detects its reducibility.

**Lemma A.11 (finite-corner continuity of invariant forms).** Fix a unitary irreducible supercuspidal \(\rho_0\) of \(G_d\), and put
\[
I_s=(\nu^s\rho_0)\times(\nu^{-s}\rho_0),\qquad s\in\mathbb R.
\tag{A.22}
\]
Suppose every \(I_s\) is irreducible and admits a nondegenerate invariant Hermitian form. Then every \(I_s\) admits a positive invariant Hermitian form.

**Proof.** In the compact model all the representations have the same space \(E\) and the same \(K=\mathrm{GL}_{2d}(\mathcal O)\)-action: the norm twists are one on the compact inducing subgroup. For any compact open \(J\subset K\), the space \(E^J\) is therefore independent of \(s\), and finite-dimensional by Lemma 1.1.

The matrix of every Hecke-corner operator on \(E^J\) is real analytic in \(s\). Here is a direct verification. A compactly supported locally constant Hecke function is a finite sum of functions on compact open cosets. On each such coset and each compact-model value patch, induction acts by a fixed \(\rho_0\)-operator multiplied by
\(|\det m_1/\det m_2|^s=q^{bs}\), with \(b\in\mathbb Z\). Only finitely many \(b\) occur on those compact sets. For a fixed basis of \(E^J\), smoothness of the basis values permits a finite common clopen refinement on which these operators and exponents are fixed. Integrating is then a finite sum. Thus each matrix entry is a finite linear combination of \(q^{bs}\). Averaging on both sides by \(e_J\) gives the same conclusion for the corner \(A_J=e_J\mathcal H(G_{2d})e_J\).

An invariant Hermitian form on \(I_s\) restricts nondegenerately to \(E^J\): if a \(J\)-fixed vector pairs to zero with \(E^J\), averaging the other argument makes it pair to zero with all of \(E\). Its restriction satisfies
\[
H(A_s(h)v,w)=H(v,A_s(h^*)w),
\qquad h^*(g)=\overline{h(g^{-1})}.
\tag{A.23}
\]
The matrix group is unimodular, so there is no modular factor in this involution. Integration of the invariant form proves (A.23).

When \(E^J\ne0\), it is simple over \(A_J\) by the corner reconstruction in Lemma 1.3. The real vector space of Hermitian matrices satisfying (A.23) has dimension one. Indeed a nonzero such form is an intertwiner from this simple finite-dimensional corner module to its conjugate dual. The invariant form already supplies an isomorphism between them. Composing with its inverse reduces any other intertwiner to a commuting endomorphism, which is scalar by the eigenspace proof of Schur's lemma. The Hermitian condition restricts the scalar to \(\mathbb R\). In particular every nonzero solution is nonsingular.

These forms can be chosen real analytically near each \(s_0\), without assuming an analytic family of global intertwiners. If \(N=\dim E^J\), equations (A.23) are real linear equations on the \(N^2\) real coordinates of a Hermitian matrix, with real-analytic coefficients. At \(s_0\), finitely many of these equations already have rank \(N^2-1\): choose a basis of their row span. A nonzero minor stays nonzero nearby. A full invariant form exists at every nearby real parameter by hypothesis, so this selected system has rank exactly \(N^2-1\) there. Its one-dimensional kernel consequently agrees with the kernel of all the equations. Fixing a coordinate that is nonzero at \(s_0\), Cramer's rule produces a nonzero real-analytic matrix on a neighborhood. It is nonsingular throughout that neighborhood. This argument also covers \(N=1\), when no homogeneous equations need be selected.

The numbers of positive and negative directions of a nonsingular Hermitian matrix are locally constant. To see this directly, diagonalize a fixed form by successive Hermitian elimination. On the unit spheres of its positive and negative subspaces, its quadratic values are bounded away from zero. Sufficiently small matrix changes preserve the respective signs. The two subspace dimensions already sum to \(N\), so the signature cannot change. Thus the property that our one-dimensional line of forms is definite is locally constant in \(s\), independently of its scalar sign.

At \(s=0\), the compact integral form from the proof of Proposition A.7 is positive and invariant; that construction of the form does not require distinct inducing factors. Its corner restrictions are positive. The connectedness of \(\mathbb R\) therefore makes the invariant line definite on every nonzero \(E^J\), for every \(s\).

For a fixed \(s\), choose a nondegenerate global invariant Hermitian form \(H_s\), a nonzero vector \(v_0\), and a compact open \(J_0\subset K\) fixing it. Change the sign so that \(H_s(v_0,v_0)>0\). Given any nonzero \(v\), choose \(J\subset J_0\) fixing it as well. The definite restriction to \(E^J\) contains \(v_0\), so its sign is positive and \(H_s(v,v)>0\). Hence \(H_s\) is positive on all of \(E\). ∎

**Theorem A.12 (cuspidal-pair criterion and its two factors).** For irreducible supercuspidals \(\rho\) and \(\rho'\), the product \(\rho\times\rho'\) is reducible exactly when
\[
\rho'\simeq\nu\rho\quad\text{or}\quad\rho\simeq\nu\rho'.
\tag{A.24}
\]
At these points the product has length two, with a unique nonzero proper submodule and two distinct irreducible factors. For \(\rho' =\nu\rho\), denote the nongeneric factor by \(Z_2(\rho)\), and the generic factor by \(Q_2(\rho)\). Their sequences are
\[
\begin{aligned}
0&\longrightarrow Z_2(\rho)\longrightarrow
 \rho\times\nu\rho\longrightarrow Q_2(\rho)\longrightarrow0,\\
0&\longrightarrow Q_2(\rho)\longrightarrow
 \nu\rho\times\rho\longrightarrow Z_2(\rho)\longrightarrow0.
\end{aligned}
\tag{A.25}
\]
Both sequences are nonsplit. These assertions hold in every rank and both local-field characteristics.

**Proof.** The nonadjacent direction is Theorem A.10. For the other direction, an unramified real twist makes \(\rho\) unitary by Lemma 1.4. A common twist of both inducing factors is an equivalence. It therefore suffices to prove reducibility of the two orders of
\(\nu^{-1/2}\rho_0,\nu^{1/2}\rho_0\), with \(\rho_0\) unitary. Write \(I_s\) as in (A.22), and \(P\) for the upper \((d,d)\)-parabolic, with Levi \(M\).

First record its Jacquet module for \(s\ne0\). The block geometric lemma has only its two unsplit-row terms, since every proper Jacquet module of \(\rho_0\) vanishes. They are
\[
\sigma_s=(\nu^s\rho_0)\boxtimes(\nu^{-s}\rho_0),
\qquad \sigma_{-s}.
\]
The central Levi element \(a=\operatorname{diag}(\varpi I_d,I_d)\) acts on these terms by
\(\lambda_s=q^{-ds}\omega_{\rho_0}(\varpi)\) and \(\lambda_{-s}\).
They are different for real \(s\ne0\). Its operator on the two-step filtration is killed by \((X-\lambda_s)(X-\lambda_{-s})\); the two factors are relatively prime. The corresponding elementary polynomial projectors split the module into its two eigenspaces. Thus
\[
r_PI_s\simeq\sigma_s\oplus\sigma_{-s}\qquad(s\ne0).
\tag{A.26}
\]
Frobenius adjunction gives a nonzero map \(I_s\to I_{-s}\). If \(I_s\) is irreducible, this map is an injection. The source and target Jacquet modules both have length two, so exactness gives zero Jacquet module for its quotient. Every irreducible factor of that quotient has the two-entry support just displayed, by Theorem 1.6. The same theorem embeds such a factor into one of \(I_s,I_{-s}\), forcing its \((d,d)\)-Jacquet module to be nonzero by adjunction. A nonzero quotient is therefore impossible. The map is an isomorphism, and \(I_{-s}\) is irreducible too.

Suppose for contradiction that the adjacent product is irreducible. The preceding argument gives irreducibility at both \(s=\pm1/2\). At every other real \(s\), Theorem A.10 gives irreducibility: equality of the two cuspidals after a \(\nu\)-twist would, on their central absolute values, force \(2s=1\) or \(2s=-1\). In particular \(I_0\) is irreducible.

Every member of this now irreducible family has a nondegenerate invariant Hermitian form. The unitary inducing form gives a perfect invariant sesquilinear pairing between \(I_s\) and \(I_{-s}\), by the normalized compact-flag calculation in Proposition A.7 and the duality proof in LG-AUT-06, Proposition 1.2. For \(s\ne0\), the isomorphism just constructed converts it into a nondegenerate invariant sesquilinear form on \(I_s\). At zero the compact integral already gives a positive form. On an irreducible admissible module these sesquilinear forms span a complex line, by Schur's lemma and admissible duality. Conjugate transposition preserves that line. If \(H^*=cH\), applying it twice gives \(|c|=1\); multiplying \(H\) by a scalar \(t\) with \(\overline t c=t\) makes it Hermitian. Lemma A.11 therefore makes every \(I_s\) unitary.

We obtain a contradiction using finite-dimensional compression, so no matrix-coefficient asymptotics are left to cite. Choose a sufficiently small compact open \(M_r\) for which \(\sigma_s^{M_r}\ne0\). Lemma 1.2 supplies a compact open \(J\) with its two unipotent factorizations, and a surjection from \(I_s^J\) onto the \(M_r\)-fixed unnormalized Jacquet module. Adjunction to the identity of \(I_s\) supplies a surjection \(r_PI_s\to\sigma_s\). Compact averaging preserves surjectivity on the fixed spaces. Their composition \(L:I_s^J\to\sigma_s^{M_r}\) is thus surjective. Equation (1.7) gives, on this space,
\[
L E_J\pi_s(a)=\delta_P(a)^{1/2}\sigma_s(a)L,
\qquad
\left|\delta_P(a)^{1/2}\sigma_s(a)\right|
 =q^{-d^2/2-ds}.
\tag{A.27}
\]
Here \(\delta_P(a)=q^{-d^2}\), and the remaining scalar \(\omega_{\rho_0}(\varpi)\) has absolute value one. The element \(a\) contracts \(U\) and expands the opposite unipotent, exactly as required in Lemma 1.2.

For a unitary \(I_s\), \(E_J\) is an orthogonal projection, so \(E_J\pi_s(a)\) on \(I_s^J\) is a contraction. Every eigenvalue of a finite-dimensional quotient of a contraction has absolute value at most one: adapt a basis to its invariant kernel to see that the quotient's characteristic polynomial divides that of the original operator, and apply the norm bound to an eigenvector of the original operator. But (A.27) gives a quotient eigenvalue greater than one for \(s<-d/2\). This contradicts the conclusion that every \(I_s\) is unitary. Both adjacent orders are consequently reducible.

Corollary 1.7 bounds their length by \(2!\), so their length is exactly two. Every factor has a nonzero \((d,d)\)-Jacquet module, as shown above; (A.26) forces each of these modules to have length one, with the two different labels \(\sigma_{1/2}\) and \(\sigma_{-1/2}\). Hence the two factors are distinct. Also
\(\operatorname{End}(I_s)=\operatorname{Hom}_M(r_PI_s,\sigma_s)=\mathbb C\)
at \(s=\pm1/2\), by (A.26). A split length-two module has two independent projections, so this module is nonsplit. It has a unique simple submodule: two different simple submodules would have zero intersection and their sum would be the whole length-two module, contradicting nonsplitting. Adjunction to that embedding identifies its Jacquet module with \(\sigma_s\); the quotient has the other label.

Finally Theorem B.3 gives precisely one generic factor, once. The other factor has zero top derivative. The Leibniz rule leaves only derivative orders \(d\) and \(2d\), so its highest derivative has order \(d\). Embed this factor into one of the two cuspidal-support inductions by Theorem 1.6. The arbitrary-product support constraints (A.19) and (A.21) place its highest derivative's support in
\[
\{\nu^{-1/2}\rho_0,\nu^{1/2}\rho_0\}
\cap\{\nu^{-3/2}\rho_0,\nu^{-1/2}\rho_0\}
=\{\nu^{-1/2}\rho_0\}.
\]
Proposition A.4 and the dimension-one top derivative of its second Jacquet factor identify that derivative with its first cuspidal Jacquet entry. The nongeneric factor therefore has Jacquet label \(\sigma_{-1/2}\), and the generic factor has label \(\sigma_{1/2}\). The unique submodule in the increasing order is the former, and in the decreasing order the latter. Undoing the common real twist proves (A.25) for arbitrary \(\rho\). ∎

The cuspidal-pair result is Zelevinsky's Proposition 1.11 [Zelevinsky 1980]. Theorem A.10 and the finite-corner continuity argument above prove the criterion with both factor labels and orientations. Appendix C supplies the segment constructions and the linked-pair calculation. Square-integrability and the full multisegment and tempered classifications remain separate results.

The normalized mirabolic functors and canonical filtration are Bernstein–Zelevinsky [1977, §§3.2–3.5]; their Lemma 4.5 and §4.14 give the Leibniz rule. The partial-Jacquet formula is Zelevinsky [1980, Proposition 3.7]. The highest-derivative pairing and cuspidal irreducibility theorem are Bernstein–Zelevinsky [1977, §§3.6–3.8 and Theorem 4.2].

## Appendix B. Whittaker uniqueness in every rank

Appendix A proves existence for supercuspidals. We now prove uniqueness, including the distribution argument on which the dimension-one assertion depends. The proof is for nonarchimedean local fields in either characteristic. Locally constant tests have no transverse derivatives along a closed subspace; we will use their restriction and extension explicitly.

Put \(G=G_n\), \(N=N_n\), and
\(\chi(u)=\psi(u_{12}+\cdots+u_{n-1,n})\).
Let \(w_0\) be the permutation matrix reversing the standard basis, and define
\[
\iota(g)=w_0\,{}^tg\,w_0,\qquad
f^\iota(g)=f(\iota(g)).
\tag{B.1}
\]
This is an anti-involution of \(G\), preserves \(N\), and satisfies
\(\chi(\iota(u))=\chi(u)\). It preserves Haar measure: its pushforward is right Haar measure, which is also left Haar measure on \(G\); its possible positive scale has square one. Hence
\((f*h)^\iota=h^\iota*f^\iota\).

For tests on \(G\), use left and right translations
\[
L_u f(g)=f(u^{-1}g),\qquad R_v f(g)=f(gv^{-1}).
\tag{B.2}
\]
The right operators form the opposite group action; together these give the action of \(N\times N^{\mathrm{op}}\). Both characters in its twisted quotient are \(\chi\).

### The relevant Bruhat cells

**Lemma B.1 (Whittaker distribution symmetry).** Every linear functional \(D\) on \(C_c^\infty(G)\) satisfying
\[
D(L_uR_vf)=\chi(u)\chi(v)D(f)
\tag{B.3}
\]
is invariant under \(f\mapsto f^\iota\).

**Proof.** We first compute the twisted quotient cell by cell. The Bruhat cell of a permutation \(w\) is \(NwTN\), with \(T\) the diagonal torus. Its \(N\times N^{\mathrm{op}}\)-orbits have representatives \(g=wt\). Their stabilizer is
\[
\{(h,g^{-1}h^{-1}g):h\in H_w\},\qquad
H_w=N\cap wNw^{-1}.
\]
Consequently the stabilizer character is trivial precisely when
\[
\chi(h)=\chi(g^{-1}hg)\quad(h\in H_w).
\tag{B.4}
\]
The common positive-root groups generate \(H_w\). For
\(h=I+xE_{ij}\), where \(i<j\) and
\(p=w^{-1}(i)<w^{-1}(j)=q\), the two sides of (B.4) are
\[
\begin{cases}\psi(x),&j=i+1,\\1,&j>i+1,\end{cases}
\qquad
\begin{cases}\psi(t_p^{-1}t_qx),&q=p+1,\\1,&q>p+1.\end{cases}
\tag{B.5}
\]
If exactly one of these roots is simple, (B.4) fails for some \(x\). In particular every ascent \(w(p)<w(p+1)\) must be an ascent by one. The maximal ascending runs of such a permutation are disjoint consecutive integer intervals. The descent between two runs forces every entry of the first interval to exceed every entry of the second. Thus \(w\) consists of consecutive increasing blocks, placed in decreasing block order. Conversely these permutations satisfy the analogous simple-root condition for \(w^{-1}\) too, so (B.5) has no one-sided simple root.

For these permutations, (B.4) requires \(t_p=t_{p+1}\) inside each increasing run. Indeed equality of \(\psi(x)\) and \(\psi(ax)\) for every \(x\) forces \(a=1\): otherwise multiplication by \(1-a\) is onto \(F\). On nonsimple common roots both characters are trivial. Checking the generating roots proves sufficiency. Write \(T_w^\circ\) for this closed subtorus; it consists of one nonzero scalar per run. For all other permutations there is no allowed torus point.

We justify the passage from this stabilizer calculation to the entire cell, including the closed torus subset. Ordered upper-root coordinates give local continuous sections for the orbit map: eliminate matrix entries as in the block Bruhat calculation of Lemma 1.5, leaving the diagonal entries \(t\). Thus a compactly supported locally constant test on the cell can be described on finitely many clopen torus patches by compact sections of the homogeneous \(N\times N^{\mathrm{op}}\)-space.

On a fixed fiber the weighted compact-average calculation of (1.11) applies. When (B.4) holds, its quotient is one-dimensional, given by the weighted orbit integral. When (B.4) fails, choose a stabilizer element on which the character is nontrivial. A larger compact stabilizer subgroup then has zero weighted average of the trivial inducing value, so the same calculation gives zero quotient. One may use compact subgroups here: upper unipotent groups, and their products, are increasing unions of compact subgroups obtained by bounding their ordered root coordinates.

The kernel calculation is local in \(t\), not just pointwise. To see this, start with a compact section and partition its support into right compact-coset patches, as in (1.11). At a fixed \(t\), the proof there either lifts its weighted integral or kills a zero class by a sufficiently large compact average. The finitely many translation maps and character values involved are locally constant on that section's compact support when \(t\) varies in a sufficiently small clopen neighborhood: the stabilizer graphs are continuous in \(t\), and the test and additive character are locally constant. Hence the same finite translation relations work on that neighborhood. A finite clopen refinement of the compact torus support makes them relations for the original test. This proves both the kernel assertion and the ability to lift local integral values.

In particular the cell's quotient is the space of compactly supported locally constant sections of a one-dimensional integration line over \(T_w^\circ\). There are no further contributions supported transversely to this subtorus. More explicitly, restriction of locally constant tests to a closed subset is onto for compactly supported tests: lift each constant value to a compact open neighborhood, choose finitely many such neighborhoods, and refine them disjointly. A test restricting to zero has support disjoint from that closed subset; the preceding zero-fiber compact averages kill it on a finite cover. The same argument applies to sections after choosing the local orbit coordinates.

Now let \(w\) be an allowed permutation. Directly reversing its ascending runs gives
\[
w_0w^{-1}w_0=w,\qquad
\iota(wt)=wt\quad(t\in T_w^\circ).
\tag{B.6}
\]
For the second identity, on the run occupying positions \(p,\ldots,p+d-1\) the index \(n+1-w(j)\) is \(2p+d-1-j\). It reverses that run, where \(t\) is constant. Therefore the representative is fixed exactly, not just up to a unipotent translation.

The map \(\iota\) interchanges the left and right orbit actions and preserves their character. On an allowed orbit its pushforward of invariant quotient Haar measure is a positive scalar multiple of that measure. Since it is an involution fixing the representative, that scalar has square one and is one. It consequently acts as the identity on the one-dimensional integration line. It is also the identity on the base \(T_w^\circ\), so it acts identically on the whole cell quotient.

Finally assemble the cells. The union of Bruhat cells of length at most \(r\) is closed; this follows from the matrix-rank conditions defining Bruhat closure, or from the successive flag-cell closures used in Lemma 1.5. The open unions of cells of length at least \(r\) therefore give a finite filtration of \(C_c^\infty(G)\). Restriction and compact clopen extension identify each successive quotient with the direct sum of the tests on cells of that length. The map \(\iota\) sends \(w\) to \(w_0w^{-1}w_0\), which has the same length, so it preserves this filtration. Exactness of twisted unipotent coinvariants carries the filtration to the quotient for (B.3). On every graded piece the disallowed cells contribute zero and the allowed cells have the identity action proved above.

An involution acting identically on the graded pieces of a finite filtration acts identically on the whole space over \(\mathbb C\). Indeed on its minus-one eigenspace the leading nonzero filtration class would also have eigenvalue minus one, contradicting the graded identity. Thus \(\iota\) is the identity on this twisted quotient. Every functional satisfying (B.3) factors through it, proving the lemma. ∎

### From distributions to functionals on a representation

The next argument avoids any assertion about convolution of distributions without compact support.

**Lemma B.2 (the distribution criterion).** Let \(V\) be an irreducible admissible smooth \(G_n\)-module. If
\(\operatorname{Hom}_N(V^\vee,\chi^{-1})\ne0\), then
\[
\dim\operatorname{Hom}_N(V,\chi)\le1.
\tag{B.7}
\]

**Proof.** Put \(A=C_c^\infty(G)\). Fix
\(0\ne\mu\in\operatorname{Hom}_N(V^\vee,\chi^{-1})\).
Regard \(\mu\) as a generalized vector: for \(h\in A\), define \(v_\mu(h)\in V\) by
\[
\ell(v_\mu(h))=\mu\!\left(\pi^\vee(\check h)\ell\right),
\qquad \check h(g)=h(g^{-1}),\quad \ell\in V^\vee.
\tag{B.8}
\]
This is an actual vector. A test is left invariant by some compact open \(J\), so the right side depends only on the restriction of \(\ell\) to \(V^J\); that finite-dimensional fixed space identifies with its bidual. This also proves
\[
v_\mu(f*h)=\pi(f)v_\mu(h).
\]
Some \(v_\mu(h)\) is nonzero: take \(h=e_J\) for a fixed space on which \(\mu\) is nonzero. The span of all these vectors is a nonzero invariant subspace, so it is \(V\).

For \(0\ne\lambda\in\operatorname{Hom}_N(V,\chi)\), define
\(D_{\lambda,\mu}(h)=\lambda(v_\mu(h))\).
The \(N\)-equivariance of \(\lambda\) gives the left identity in (B.3). For the right identity, (B.8) and \(\mu\)'s character show that the generalized vector transforms by \(\chi\); explicitly
\(\pi(u)v_\mu=\chi(u)v_\mu\) in the algebraic dual of \(V^\vee\). Thus the right identity is the same one. Lemma B.1 applies, and \(D_{\lambda,\mu}(h^\iota)=D_{\lambda,\mu}(h)\).

For a functional \(D\) on \(A\), define its convolution annihilators by
\[
\begin{aligned}
\mathcal L(D)&=\{f:D(f*h)=0\text{ for every }h\in A\},\\
\mathcal R(D)&=\{h:D(f*h)=0\text{ for every }f\in A\}.
\end{aligned}
\tag{B.9}
\]
Since the \(v_\mu(h)\) span \(V\),
\(\mathcal L(D_{\lambda,\mu})=\{f:\lambda\pi(f)=0\}\).
Since the translates of nonzero \(\lambda\) separate \(V\), irreducibility also gives
\(\mathcal R(D_{\lambda,\mu})=\{h:v_\mu(h)=0\}\).
The latter does not depend on \(\lambda\). Invariance under the anti-involution and reversal of convolution imply
\(\mathcal L(D)=\mathcal R(D)^\iota\).
Hence all nonzero Whittaker functionals \(\lambda\) have the same left annihilator.

This forces proportionality; we give the finite-dimensional step. If \(V^J\ne0\), the corner \(e_JAe_J\) acts as all of \(\operatorname{End}_{\mathbb C}(V^J)\). Its module is simple by Lemma 1.3, and the finite-list density argument there, applied to a basis, prescribes an arbitrary endomorphism. Intersecting the common left annihilator with this corner therefore identifies the kernels of the rows \(\lambda|_{V^J}\). If two restrictions are nonzero, these rows are proportional. Fix a vector on which both are nonzero. Every additional vector and this one belong to a common fixed space after shrinking \(J\); the proportionality scalar is fixed by the original vector. Thus the two functionals are proportional on all of \(V\). If initially their nonzero values occur on different vectors, place both in a common fixed space first; equality of the corner annihilators ensures that neither restriction is zero. This proves (B.7). ∎

### Supercuspidals and all irreducible constituents

**Theorem B.3.** Every irreducible supercuspidal \(\rho\) of \(G_d\) has
\[
\dim\mathcal W_d(\rho)=1.
\tag{B.10}
\]
Its restriction to \(\mathcal P_d\) is irreducible. Every irreducible admissible representation of \(G_n\) has a Whittaker space of dimension zero or one. An induction of supercuspidals has exactly one generic composition factor, occurring once.

**Proof.** An unramified determinant twist makes \(\rho\)'s central character unitary and does not change its unipotent action. Lemma 1.4 then gives an invariant positive Hermitian form. This identifies \(\rho^\vee\) with its complex conjugate representation: on each finite-dimensional fixed space the form is a perfect pairing, and the union of these identifications is the smooth dual. Complex conjugation preserves all Jacquet vanishing statements, so \(\rho^\vee\) is supercuspidal too. The same is true before undoing the twist.

Proposition A.4 proves a nonzero Whittaker functional for \(\rho\) and, with the additive character replaced by its inverse, for \(\rho^\vee\). Lemma B.2 gives dimension at most one, hence exactly one for \(\rho\). The dual of the top coinvariant space is its Whittaker-functional space. If that coinvariant had two independent vectors, extending their dual coordinate functionals to a basis would give two independent functionals. Thus the coinvariant itself has dimension one, proving (B.10).

All the lower derivatives of \(\rho\) vanish by Proposition A.4. The canonical filtration now identifies its restriction with
\((\Phi^+)^{d-1}\Psi^+\mathbb C\), which is irreducible by Theorem A.2 and Corollary A.3.

For any induction \(I=\rho_1\times\cdots\times\rho_t\), Lemma A.5 and (B.10) give \(\dim\mathcal W_n(I)=1\). It has finite length by Corollary 1.7. Exactness of twisted coinvariants on a composition series then says that precisely one factor has a nonzero Whittaker space, that space has dimension one, and the factor occurs just once.

Finally Theorem 1.6 embeds any irreducible admissible representation \(V\) into such an \(I\). Exact coinvariants embed \(\mathcal W_n(V)\) into its one-dimensional Whittaker space. This proves the assertion for every \(V\), without using the segment classification or assuming beforehand that a general contragredient is generic. ∎

The symmetry method is due to Gelfand and Kazhdan; the comparison in Cogdell [2000, §1.2, Theorem 1.2] describes the relevant block permutations and anti-involution. Here the cell and closed-subtorus calculation, finite-filtration passage, generalized-vector criterion and deduction from supercuspidal support are supplied in full. These arguments close the dimension-one input in Zelevinsky [1980, §3.8]. The full cuspidal-pair criterion, including its adjacent factors, is proved in Theorems A.10 and A.12. The complete segment classification remains a separate step.

## Appendix C. Segments on one cuspidal line

We now construct both representations attached to every segment, and prove their complete Jacquet, duality and derivative formulas. The construction uses a finite support of distinct integer twists of an arbitrary supercuspidal; it places no restriction on its rank, central character or residue characteristic. Repeated entries in a general multisegment require the further classification arguments after this appendix.

Put \(\rho_e=\nu^e\rho\), where \(\rho\) is an irreducible supercuspidal of \(G_d\), and fix a finite nonempty set \(E\subset\mathbb Z\). These entries are distinct: their central characters on \(\varpi I_d\) have different absolute values. An ordering \(\lambda=(e_1,\ldots,e_r)\) of \(E\) gives
\[
I_\lambda=\rho_{e_1}\times\cdots\times\rho_{e_r},
\qquad M_0=G_d^r\subset G_{rd}.
\tag{C.1}
\]
Join \(e\) and \(e+1\) when both are in \(E\). The resulting graph \(\Gamma_E\) is a disjoint union of paths. Orient each edge from the entry occurring first in \(\lambda\) to the one occurring later; call this orientation \(\gamma_\lambda\).

### Orderings of a path forest

**Lemma C.1.** Every orientation of \(\Gamma_E\) comes from an ordering. Two orderings have the same orientation precisely when they are connected by exchanges of neighboring entries that are not joined by an edge. For any fixed edge, an ordering with a specified orientation can be chosen in which the two endpoints are neighbors.

**Proof.** An oriented forest has no directed cycle. Its edge directions define a partial order by directed reachability. A finite directed acyclic graph has a vertex with no incoming edge: otherwise repeatedly choosing an incoming predecessor eventually repeats a vertex and gives a cycle. Remove such a vertex, order the remaining graph recursively, and put the removed vertex first. This is a total ordering compatible with the orientation.

Neighboring entries with no edge can be exchanged without changing any edge direction. Conversely, take two compatible orderings. Move the first entry of the second to the beginning of the first. Each entry it passes is incomparable to it: a predecessor would have to occur before it in the second ordering, and a successor could not have occurred before it in the first. In particular none of these exchanges crosses an edge. Repeat on the remaining entries. This gives the asserted exchange chain.

For an edge \(u\to v\), contract its two endpoints to one vertex. The contracted oriented graph is still acyclic. A directed cycle after contraction would lift to a directed path from \(u\) to \(v\), or from \(v\) to \(u\), avoiding the contracted edge, and the underlying forest has no such alternative path. Choose a compatible ordering of this contraction and replace its merged vertex by the consecutive pair \(u,v\). All original edge constraints are respected. ∎

### Constituents and their exact cuspidal Jacquet labels

For an irreducible \(\omega\) of support \(\{\rho_e:e\in E\}\), let \(\mathcal J(\omega)\) be the set of orderings \(\mu\) whose tensor label
\(\sigma_\mu=\rho_{\mu_1}\boxtimes\cdots\boxtimes\rho_{\mu_r}\)
occurs in \(r_{M_0}\omega\). Below these labels occur once and this Jacquet module is their direct sum.

**Theorem C.2 (distinct support on one cuspidal line).** The irreducible representations with this support are indexed by the orientations \(\gamma\) of \(\Gamma_E\). Write them \(\omega_\gamma\). For every ordering \(\lambda\), the constituents of \(I_\lambda\) are exactly these \(2^{|\Gamma_E^1|}\) representations, each once, and
\[
r_{M_0}\omega_\gamma
 =\bigoplus_{\gamma_\mu=\gamma}\sigma_\mu.
\tag{C.2}
\]
The product has unique irreducible submodule \(\omega_{\gamma_\lambda}\) and unique irreducible quotient \(\omega_{\gamma_\lambda^{\mathrm{op}}}\), where every edge is reversed in \(\gamma_\lambda^{\mathrm{op}}\).

**Proof.** First, all orderings have the same composition-factor multiset. For neighbors whose exponents differ by more than one, Theorem A.10 makes their pair products irreducible in either order. Their two cuspidal Jacquet terms split by their different central characters, exactly as in (A.26). Adjunction gives a nonzero map between the two orders, hence an isomorphism. For exponents differing by one, (A.25) gives the same two distinct composition factors in both orders. Induction in stages and exactness therefore preserve the multiset under every neighboring exchange. Such exchanges generate all permutations. In particular orderings with the same orientation give isomorphic products, by Lemma C.1 and the isomorphisms for nonedges.

The full cuspidal Jacquet module of any \(I_\lambda\) has a filtration with the \(r!\) tensor labels \(\sigma_\mu\), each once. Indeed the block geometric lemma only retains unsplit rows; each row has size \(d\), as does each column, so its surviving intersection matrices are exactly permutation matrices multiplied by \(d\).

This filtration splits. Choose an integer \(B\ge2\) greater than \(\max E-\min E\), and put
\[
z=\operatorname{diag}(\varpi^{B^0}I_d,
 \varpi^{B^1}I_d,\ldots,\varpi^{B^{r-1}}I_d)\in Z(M_0).
\]
Its scalar on \(\sigma_\mu\) is
\[
c_\mu=\omega_\rho(\varpi)^{\sum_jB^{j-1}}
 q^{-d\sum_j\mu_jB^{j-1}}.
\tag{C.3}
\]
These scalars are distinct: subtract \(\min E\) from each exponent and use uniqueness of base-\(B\) expansions with digits between \(0\) and \(B-1\). The product \(\prod_\mu(X-c_\mu)\) kills the operator on the filtration. Its distinct roots give polynomial projectors onto the corresponding eigenspaces. Each eigenspace has exactly its one simple filtration factor. Thus
\(r_{M_0}I_\lambda=\bigoplus_\mu\sigma_\mu\).
Its subquotients, including the Jacquet modules of its constituents, also split into subsets of these distinct labels.

Every constituent \(\omega\) has a nonzero \(r_{M_0}\omega\). Theorem 1.6 embeds it into an induction of an ordering of this same support, and adjunction gives a nonzero map from this Jacquet module to that ordering's tensor label. Exactness now partitions the \(r!\) labels among the composition factors. No factor can occur twice, since it has at least one label and every label occurs once. Write \(\Omega\) for this common, multiplicity-free constituent set.

Each \(I_\lambda\) has a unique simple submodule. A simple submodule \(\omega\) must, by adjunction, have label \(\sigma_\lambda\). This label belongs to exactly one element of \(\Omega\). Any nonzero finite-length module has a simple submodule, so that unique element is the socle. More generally, whenever \(\sigma_\mu\in r_{M_0}\omega\), its direct-sum projection onto \(\sigma_\mu\) and adjunction embed \(\omega\) into \(I_\mu\). It is consequently the socle of \(I_\mu\). All orderings of a fixed orientation have the same socle by the product isomorphisms already proved.

We show that no constituent's labels cross an edge's two possible directions. Fix \(\lambda\) and an edge \(e=\{u,v\}\). Lemma C.1 puts its endpoints next to each other in an ordering with orientation \(\gamma_\lambda\); the product is isomorphic to \(I_\lambda\). Replace this pair by its unique irreducible submodule from Theorem A.12, and induce with all other entries. Exactness gives a submodule \(N_{\lambda,e}\subset I_\lambda\). Its full cuspidal Jacquet labels are exactly
\[
\mathcal H_{\lambda,e}=
 \{\mu:\text{the direction on }e\text{ in }\gamma_\mu
                    \text{ agrees with }\gamma_\lambda\}.
\tag{C.4}
\]
Here is the cell calculation. The paired row has size \(2d\), so it must split into two \(d\)-columns. Its only surviving proper Jacquet module is the ordered pair label in (A.25); a refinement into blocks smaller than \(d\) would split a supercuspidal and vanish. Its two entries are therefore placed in two columns in precisely their retained order. Every other row fills a single column. These are exactly the permutations in (C.4), once each, with no additional twist by the normalized modulus identity in Lemma 1.5.

Each \(N_{\lambda,e}\) contains a subset of the multiplicity-free factors \(\Omega\), and contains all Jacquet labels of each of its factors. Thus every \(\mathcal J(\omega)\) lies on one side of (C.4), for every edge. It is contained in one orientation class. Conversely, each label of an orientation \(\gamma\) belongs to the socle of its ordering's product, and all those socles are the same representation. That representation's labels are therefore the whole orientation class. Different orientations have disjoint labels and different factors. This proves (C.2) and the asserted indexing. Every irreducible with this support embeds into a product by Theorem 1.6, so no further irreducibles are missing.

Taking the sum of the \(N_{\lambda,e}\) over all edges gives all factors except the one whose every edge disagrees with \(\gamma_\lambda\). To justify this sum calculation, in a multiplicity-free finite-length module the factors of a sum of submodules are the union of their factor sets: use the exact sequence for the sum and intersection, and the fact that no factor can occur twice. The quotient by this sum is therefore the single irreducible \(\omega_{\gamma_\lambda^{\mathrm{op}}}\).

There cannot be another irreducible quotient. Admissible smooth duality is exact and involutive, as proved before (A.20), and normalized induction duality turns \(I_\lambda^\vee\) into the product of its ordered dual cuspidals. These are again distinct integer twists of one supercuspidal. The unique-socle result just established applies to that product, so duality gives a unique irreducible quotient of \(I_\lambda\). If there are no edges, Theorem A.10 already makes the product irreducible; the sum here is zero. ∎

### The entire submodule lattice

For an orientation \(\gamma\), write
\(D_\lambda(\gamma)=\{e\mid\gamma\text{ agrees with }\gamma_\lambda\text{ on }e\}\).
Orientations of a forest are in bijection with all subsets of its edge set, by these agreement sets.

**Theorem C.3.** Submodules \(W\subset I_\lambda\) are in bijection with the upper sets of the inclusion order on these agreement sets. The bijection sends \(W\) to the orientations of its irreducible factors. In particular the lattice is generated by the submodules \(N_{\lambda,e}\) using sums and intersections.

**Proof.** In a multiplicity-free finite-length module, factor sets determine submodules and their inclusion. If every factor of \(W_1\) occurs in \(W_2\), none occurs in \(I_\lambda/W_2\). A nonzero image of \(W_1\) in this quotient would have a simple factor common to both modules, which is impossible. Thus \(W_1\subset W_2\). The converse is immediate. Sums correspond to unions as in Theorem C.2, and intersections correspond to intersections: the sum/intersection exact sequence and multiplicity one forbid loss of a common factor or the appearance of any other one.

We prove the required closure towards \(\gamma_\lambda\). Suppose \(\omega_\gamma\) occurs in \(W\) and an edge \(\{p,p'\}\) has different directions in \(\gamma\) and \(\gamma_\lambda\). By Lemma C.1 choose an ordering \(\mu\) for \(\gamma\) in which this pair is consecutive. Its tensor label \(\sigma_\mu\) occurs in \(r_{M_0}W\) by (C.2). Merge the two corresponding \(d\)-blocks into one \(2d\)-block, giving a coarser Levi \(L\).

In the geometric filtration of \(r_LI_\lambda\), exactly one term can contribute \(\sigma_\mu\) after the further cuspidal Jacquet functor. Its merged block is the pair product in their relative order in \(\lambda\), and every other block is the indicated single cuspidal entry of \(\mu\). Indeed unsplit rows assign the two named entries to this one column and each remaining named entry to its own column. This fixes their intersection matrix. Any different assignment has a different cuspidal tuple. Filter \(r_LW\subset r_LI_\lambda\) by its intersections with these filtration terms. Exactness of the further Jacquet functor makes the contribution to \(\sigma_\mu\) come from a nonzero submodule \(T\) of this particular term.

The other Levi factors in the term are irreducible, and a submodule of its tensor product has the form \(T_0\boxtimes Y\), with \(T_0\) a submodule of the pair product. To verify this tensor assertion, write any vector of the submodule as \(\sum_i x_i\otimes y_i\) with independent \(y_i\). The finite-list density argument in Lemma 1.3 prescribes operators on the irreducible \(Y\) that send one \(y_i\) to a fixed nonzero vector and the others to zero. Hence each \(x_i\) tensored with that vector belongs to the submodule. Acting on it spans \(Y\); therefore each \(x_i\otimes Y\) belongs. The collection of all such \(x_i\) is the desired invariant \(T_0\), and the two inclusions follow.

Every nonzero submodule of the adjacent pair contains its unique simple submodule from Theorem A.12. Its cuspidal Jacquet label has the pair order in \(\lambda\). Consequently \(r_{M_0}T\), and hence \(r_{M_0}W\), contains \(\sigma_{\mu'}\), where the consecutive entries of \(\mu\) are exchanged to agree with \(\lambda\). This exchange reverses just the named edge. Theorem C.2 forces the constituent \(\omega_{\gamma'}\) to occur in \(W\), with
\(D_\lambda(\gamma')=D_\lambda(\gamma)\cup\{e\}\).
Repeating proves that its orientation set is an upper set.

Conversely, by (C.4), the submodule \(N_{\lambda,e}\) corresponds to all agreement sets containing \(e\). For a set of edges \(A\), the intersection
\(\bigcap_{e\in A}N_{\lambda,e}\)
corresponds to all agreement sets containing \(A\). An empty intersection means \(I_\lambda\). Every upper set of a finite power set is the union of the principal upper sets above its minimal members. Take the sum of these intersections over those minimal members; an empty sum means zero. This constructs exactly the requested upper set. Injectivity was proved in the first paragraph, so it gives the entire lattice. ∎

### Segment construction, Jacquet modules and duals

For \(a\le b\), put \(\ell=b-a+1\), \(n=d\ell\), and use \([a,b]\) to denote the actual segment \([\rho_a,\ldots,\rho_b]\). An empty interval represents the trivial representation of \(G_0\).

**Theorem C.4.** The increasing product
\(\rho_a\times\cdots\times\rho_b\)
has a unique irreducible submodule \(Z([a,b])\) and a unique irreducible quotient \(Q([a,b])\). The decreasing product has these two representations in the opposite positions. Their cuspidal Jacquet modules are the single labels
\[
\begin{aligned}
r_{G_d^\ell}Z([a,b])&=\rho_a\boxtimes\cdots\boxtimes\rho_b,\\
r_{G_d^\ell}Q([a,b])&=\rho_b\boxtimes\cdots\boxtimes\rho_a.
\end{aligned}
\tag{C.5}
\]
For a proper block partition \(n=n_1+\cdots+n_t\), the Jacquet module of either representation vanishes unless every \(n_i\) is divisible by \(d\). If \(n_i=dk_i\), set \(K_i=k_1+\cdots+k_i\), \(K_0=0\). Then
\[
\begin{aligned}
r_{(dk_1,\ldots,dk_t)}Z([a,b])
 &=\boxtimes_{i=1}^t Z([a+K_{i-1},a+K_i-1]),\\
r_{(dk_1,\ldots,dk_t)}Q([a,b])
 &=\boxtimes_{i=1}^t Q([b-K_i+1,b-K_{i-1}]).
\end{aligned}
\tag{C.6}
\]
With \(\Delta^\vee=[\rho_b^\vee,\rho_{b-1}^\vee,\ldots,\rho_a^\vee]\), an increasing segment on the dual line,
\[
Z(\Delta)^\vee=Z(\Delta^\vee),\qquad
Q(\Delta)^\vee=Q(\Delta^\vee).
\tag{C.7}
\]

**Proof.** For consecutive exponents the graph is a single path. The orientation of an increasing ordering has precisely one compatible ordering, that increasing one; its opposite has precisely the decreasing ordering. Theorem C.2 proves existence, uniqueness, both positions and (C.5).

Let \(L\) be the Levi of the stated block partition. Apply the geometric lemma to the Jacquet module of the full cuspidal induction. A surviving row places its whole \(d\)-block into one column. Thus each column sum must be divisible by \(d\); otherwise its Jacquet module and those of every constituent vanish. When each \(n_i=dk_i\), this Jacquet module has finite length and is admissible: its terms are tensor products of inductions of subsets of our cuspidal entries, covered by Lemma 1.1 and Corollary 1.7.

Every irreducible constituent \(\tau\) of it has nonzero Jacquet module down to \(M_0=G_d^\ell\). Indeed its irreducible Levi factors are supplied by Lemma 1.3. The geometric terms put a specified subset of \(k_i\) cuspidals in each column; Theorem 1.6 identifies that subset as the support of the corresponding factor. Embedding each factor into an ordering of those cuspidals and using adjunction gives a nonzero Jacquet module down to its \(k_i\) blocks. Their tensor product is nonzero. This applies also to every constituent of \(r_LZ(\Delta)\) or \(r_LQ(\Delta)\), by exactness.

Transitivity identifies their further Jacquet modules with (C.5), which has length one. Each nonzero composition factor of the intermediate module contributes at least one to this length. Therefore that intermediate module is itself irreducible and nonzero. Write it as \(\boxtimes_i\tau_i\). Its further Jacquet label is precisely the ordered tuple in (C.5), split into its consecutive blocks of \(k_i\) entries. Thus each \(\tau_i\) has the contiguous segment support specified in (C.6), and its cuspidal Jacquet module is its single increasing label for \(Z\), or its single decreasing label for \(Q\). Theorem C.2 identifies it with exactly the segment representation claimed. This proves (C.6), including all block lengths and the order of the decreasing intervals.

For (C.7), dualizing the increasing product gives the product of its dual entries in the same order, which is a decreasing product for \(\Delta^\vee\). Exact admissible duality turns the submodule \(Z(\Delta)\) into an irreducible quotient of that product, and its quotient \(Q(\Delta)\) into an irreducible submodule. The unique positions already proved identify these as \(Z(\Delta^\vee)\) and \(Q(\Delta^\vee)\). This argument does not assume a duality formula for Jacquet modules. ∎

When \(d=1\) and \(\rho=\chi\) is a character of \(F^\times\), we can identify the increasing submodule explicitly:
\[
Z([a,b])(g)=\chi(\det g)\,|\det g|^{(a+b)/2}.
\tag{C.8}
\]
This one-dimensional representation has normalized Borel Jacquet characters \(\chi\nu^{a+j-1}\) in position \(j\): subtracting the Borel half-modulus exponent \((\ell+1-2j)/2\) from \((a+b)/2\) gives \(a+j-1\). Adjunction embeds it into the increasing product, whose simple submodule is unique. Hence it is (C.8). For higher-rank \(\rho\), the single Jacquet label in (C.5) consists of higher-rank supercuspidals; the determinant-character description does not apply.

### Genericity and all segment derivatives

**Theorem C.5.** Of the representations in Theorem C.2, exactly one is generic: its orientation directs every edge from the higher exponent to the lower. In particular \(Q(\Delta)\) is generic, and \(Z(\Delta)\) is nongeneric whenever \(\ell>1\). For the normalized derivatives of Appendix A,
\[
Z([a,b])^{(k)}=
\begin{cases}
Z([a,b-1]),&k=d,\\
0,&1\le k\le n,\ k\ne d,
\end{cases}
\tag{C.9}
\]
and
\[
Q([a,b])^{(k)}=
\begin{cases}
Q([a+t,b]),&k=dt,\quad1\le t\le\ell,\\
0,&1\le k\le n,\quad d\nmid k.
\end{cases}
\tag{C.10}
\]
The empty-interval cases on the right are one-dimensional \(G_0\)-modules. Also \(Z(\Delta)\) remains irreducible on the mirabolic group.

**Proof.** Theorem B.3 gives exactly one generic constituent of each cuspidal product, occurring once. If an orientation has an edge from its lower exponent to its higher one, choose a compatible ordering and its edge submodule \(N_{\lambda,e}\). The paired submodule there is the nongeneric \(Z_2\) from (A.25). Lemma A.5 makes the entire induced \(N_{\lambda,e}\) have zero Whittaker space, and exactness gives the same for all its factors. By (C.4), those factors include the one with the specified orientation. Thus every orientation except the entirely decreasing one is nongeneric. The unique generic constituent must be the remaining orientation. For the connected segment this is precisely \(Q(\Delta)\), by (C.5). Its Whittaker space has dimension one by Theorem B.3.

Now use the partial Jacquet formula (A.7). If \(d\nmid k\), (C.6) gives zero. For \(k=dt\), the final \(dt\)-block of the Jacquet module of \(Z([a,b])\) is \(Z([b-t+1,b])\). It has zero Whittaker space when \(t>1\), and dimension one when \(t=1\), by supercuspidal uniqueness. Its first block is \(Z([a,b-t])\). This gives (C.9), including \(\ell=1\), when only the top derivative \(k=d\) occurs. For \(Q\), the final block is \(Q([a,a+t-1])\), which is generic with one-dimensional Whittaker space; its first block is \(Q([a+t,b])\). This proves every case in (C.10). The zero-rank endpoint is the top Whittaker line. Formula (A.7) already contains the full normalization, so no further norm twist occurs.

Finally (C.9) and the canonical mirabolic filtration identify the restriction of \(Z(\Delta)\) with
\((\Phi^+)^{d-1}\Psi^+ Z([a,b-1])\).
Its value module is irreducible, including the empty-interval case. The equivalence and classification in Theorem A.2 and Corollary A.3 therefore make this restriction irreducible. ∎

### Highest derivatives and unlinked segment products

Let \(m_\tau\) denote the cuspidal-support multiplicity function of an irreducible \(\tau\), on the set of actual supercuspidal isomorphism classes. For a finite support function, \(\nu\) denotes its pushforward under \(\kappa\mapsto\nu\kappa\).

**Lemma C.6.** If \(\tau\) is irreducible and \(\alpha\) is an irreducible submodule of its highest derivative, then
\[
\nu m_\alpha\le m_\tau.
\tag{C.11}
\]
Suppose \(\Delta_1,\ldots,\Delta_t\) are arbitrary segments, possibly on different cuspidal lines and with repeated entries, and no two are disjoint adjacent segments. If their base cuspidal ranks are \(d_i\), every irreducible constituent of \(Z(\Delta_1)\times\cdots\times Z(\Delta_t)\) has highest derivative order \(\sum_i d_i\).

**Proof.** Embed \(\tau\) into a cuspidal-support induction using Theorem 1.6. Apply Lemma A.9 to its restriction, paired with the \(\nu\)-twisted smooth dual of that induction. The argument leading to (A.21), without any no-adjacency hypothesis, gives exactly (C.11), including multiplicities: the dual highest-derivative label is a quotient of the derivative of the twisted dual induction, whose Leibniz terms delete whole cuspidal blocks. Dualizing its support gives \(\operatorname{supp}\alpha\subseteq\nu^{-1}\operatorname{supp}\tau\) as a multiset. This is (C.11). At rank zero the support function is zero.

For the product assertion put \(V=\prod_i Z(\Delta_i)\). Its highest derivative order is \(D=\sum_i d_i\), by (C.9) and Theorem A.6. Let \(\tau\) be any constituent, of highest order \(k\), and choose an irreducible submodule \(\alpha\) of \(\tau^{(k)}\). These derivative modules have finite length: the iterated Leibniz filtration has finite-length segment-product terms by Corollary 1.7. Exactness puts \(\alpha\) in one such term of \(V^{(k)}\). Each segment in that term is either unchanged or has its final entry deleted, since its only nonzero positive derivative has order \(d_i\). Call the chosen segments \(\Delta_i'\). Their support is the support of \(\alpha\): embed every segment factor into its cuspidal induction, then use exact induction and Theorem 1.6. The same argument gives \(m_\tau=\sum_i1_{\Delta_i}\).

Write \(a_i\) and \(b_i\) for the actual beginning and end cuspidals of \(\Delta_i\). If the segment is unchanged, its support minus its shifted support is \(1_{\{a_i\}}-1_{\{\nu b_i\}}\); if its final entry was deleted, this difference is just \(1_{\{a_i\}}\). Thus (C.11) says
\[
0\le m_\tau-\nu m_\alpha
 =\sum_i1_{\{a_i\}}
   -\sum_{\Delta_j'=\Delta_j}1_{\{\nu b_j\}}.
\tag{C.12}
\]
If any segment remained unchanged, its \(\nu b_j\) would have to equal some beginning \(a_i\); otherwise the value at that cuspidal would be negative. Such an equality means that these two segments are disjoint and adjacent on the same line. It cannot hold for the same segment, since a real norm twist changes the central absolute value. This contradicts the hypothesis. Every segment is therefore shortened, and \(k=D\). ∎

**Theorem C.7 (all unlinked \(Z\)-products).** If no two segments \(\Delta_i\) are linked, then
\(Z(\Delta_1)\times\cdots\times Z(\Delta_t)\)
is irreducible. This includes arbitrary cuspidal ranks and lines, repeated segments, and one segment contained in another.

**Proof.** Induct on the total degree, allowing empty segments as factors of \(G_0\). Deleting final entries preserves nonlinking. For nonempty intervals on the same line, if their shortened intervals linked, their starts could be ordered so that
\(a<c\le b\le d-1\). This implies \(a<c\le b+1\le d\), so the original intervals linked as well. Different lines remain different, and an empty interval is removed. The induction's smaller product of shortened segments is therefore irreducible.

Unlinked segments cannot be disjoint adjacent ones, so Lemma C.6 applies. The product's highest derivative, of order \(D=\sum_i d_i\), is precisely the product of those shortened segments, by Theorem A.6 and (C.9). It has length one by induction; when all segments had length one it is the trivial \(G_0\)-module. Every composition factor of the original product has nonzero derivative of this same order by Lemma C.6. Exactness on its finite composition series would give at least one nonzero factor in this length-one derivative for each original factor. Thus the original product has just one factor and is irreducible. The degree-zero induction base is the one-dimensional \(G_0\)-module. ∎

### Disjoint segment products and the adjacent boundary

**Proposition C.8.** Let the segments lie on one cuspidal line and have pairwise disjoint supports.

If there is a gap between each two neighboring segments, any product of their \(Z\)- and \(Q\)-representations is irreducible, independent of the order of the factors. If \(A=[a,c-1]\) and \(B=[c,b]\) are adjacent, their \(Z\)-product has two distinct factors: \(Z([a,b])\) and the orientation representation whose internal edges increase in both intervals but whose boundary edge decreases. Call the latter \(D_Z(A,B)\). Their unique-submodule sequences are
\[
\begin{aligned}
0&\to Z([a,b])\to Z(A)\times Z(B)\to D_Z(A,B)\to0,\\
0&\to D_Z(A,B)\to Z(B)\times Z(A)\to Z([a,b])\to0.
\end{aligned}
\tag{C.13}
\]
For the \(Q\)-products, let \(D_Q(A,B)\) have decreasing internal edges and an increasing boundary. Then
\[
\begin{aligned}
0&\to D_Q(A,B)\to Q(A)\times Q(B)\to Q([a,b])\to0,\\
0&\to Q([a,b])\to Q(B)\times Q(A)\to D_Q(A,B)\to0.
\end{aligned}
\tag{C.14}
\]
All four sequences are nonsplit. The factor \(Q([a,b])\) is generic and \(D_Q(A,B)\) is nongeneric.

**Proof.** Each segment representation embeds into a cuspidal product: use increasing order for \(Z\), decreasing for \(Q\), by Theorem C.4. Exact induction therefore embeds the stated product \(P\) into one \(I_\lambda\) for the distinct union support. It has finite length and inherits multiplicity one from Theorem C.2.

Its full cuspidal Jacquet labels are the shuffles preserving each segment's internal increasing order for \(Z\) or decreasing order for \(Q\). This follows directly from (C.6) and the block geometric lemma: a row breaks into consecutive subsegments in its indicated internal order, whose resulting cuspidal labels occupy its selected columns. Every such shuffle corresponds to one intersection matrix and occurs once; no other label survives.

If there are gaps, each segment is one connected component of the union graph. These shuffles form exactly one orientation class, with the prescribed directions inside each component. Theorem C.2 forces \(P\) to contain its one irreducible factor and no others. Thus it is irreducible. This class is independent of the order of the segment factors, proving their isomorphism for every ordering.

At an adjacent boundary there are exactly two orientation classes of shuffles, since the internal directions are fixed and the sole boundary direction is free. They both occur, so \(P\) has exactly two distinct factors as stated. Let \(L\) be the two-block Levi of this segment product and \(\tau\) its irreducible inducing tensor. The cuspidal Jacquet module of \(\tau\) is a single tuple by (C.5). Its multiplicity in \(r_LP\) is at most one, since any occurrence contributes that tuple to the full Jacquet module, where its multiplicity is one. These modules have finite length by (C.6), the geometric lemma and Corollary 1.7. Applying Hom to a composition series and using scalar Schur's lemma gives
\[
\dim\operatorname{End}(P)
 =\dim\operatorname{Hom}_L(r_LP,\tau)\le1.
\]
The identity makes the dimension one. A split sum of its two factors would have two independent projections, so \(P\) is nonsplit and has a unique simple submodule.

Adjunction to any simple embedding \(\omega\hookrightarrow P\) gives a quotient \(r_L\omega\to\tau\). Further exact Jacquet functors force the concatenated inducing tuple into \(r_{M_0}\omega\). Theorem C.2 identifies the submodule by the orientation of this tuple. For increasing \(Z\)-blocks in increasing block order it is the wholly increasing orientation, namely \(Z([a,b])\); reversing the block order changes just the boundary direction and gives \(D_Z(A,B)\). For decreasing \(Q\)-blocks the corresponding choices are \(D_Q(A,B)\) and the wholly decreasing \(Q([a,b])\). The remaining factor is the respective quotient, proving (C.13)–(C.14). The genericity assertions follow from Theorem C.5. ∎

The distinct-support and submodule-lattice theorems are Zelevinsky [1980, §§2.1–2.11]; his §§3.1–3.10 give the single-segment constructions and derivatives. The highest-level and unlinked-product results are §§4.3–4.5, and the adjacent pair is the first case of Proposition 4.6.

### Linked overlapping segments

Fix an irreducible supercuspidal \(\rho\) of \(G_m\), and continue to write \([a,b]\) for the segment of its integer twists. No unitarity hypothesis is imposed.

**Theorem C.9 (the linked pair).** Suppose
\[
a<c\le b+1\le d,
\qquad A=[a,b],\quad B=[c,d],
\]
and set \(U=[a,d]\) and \(H=[c,b]\), with \(H\) empty when \(c=b+1\). The representation
\[
M=Z(U)\times Z(H)
\tag{C.15}
\]
is irreducible. The higher-start-first product has precisely two distinct irreducible factors and a nonsplit exact sequence
\[
0\longrightarrow K(A,B)\longrightarrow
 Z(B)\times Z(A)\longrightarrow M\longrightarrow0.
\tag{C.16}
\]
Its only nonzero proper submodule is \(K(A,B)\), and its only irreducible quotient is \(M\). The opposite product also has length two with distinct factors and a nonsplit extension; its unique irreducible submodule is \(M\). These assertions hold for every cuspidal rank \(m\) and in both local-field characteristics.

**Proof.** The union and intersection are nested, so Theorem C.7 makes (C.15) irreducible, including the empty intersection. When the intervals are disjoint adjacent ones, Proposition C.8 supplies every assertion. We treat the overlapping case \(a<c\le b<d\), by induction on the total degree
\(N=m((b-a+1)+(d-c+1))\). The induction is only used for a smaller linked pair; its adjacent case has already been proved.

Put
\[
p=m(d-c+1),\quad t=m(c-a),\quad v=m(b-c+1),
\qquad u=p+t=m(d-a+1),\quad r=t+v=m(b-a+1).
\]
Thus \(N=p+r=u+v\). Write \(P=P_{(p,r)}\) and \(Q=P_{(u,v)}\), and let \(L_Q=G_u\times G_v\). Set \(V=Z(B)\times Z(A)\).

We first construct an \(L_Q\)-equivariant surjection
\[
r_QV\longtwoheadrightarrow
 \bigl(Z(B)\times Z([a,c-1])\bigr)\boxtimes Z(H).
\tag{C.17}
\]
This is a quotient term of the geometric filtration, rather than merely a composition factor. Indeed the identity double coset has intersection matrix
\[
\begin{pmatrix}p&0\\t&v\end{pmatrix}.
\tag{C.18}
\]
Its orbit is closed. In the Grassmannian description it is the set of \(p\)-planes contained in the fixed \(u\)-plane. Containment is expressed by vanishing minors and hence is closed. This orbit is the Grassmannian of \(p\)-planes in that \(u\)-plane, so is compact over \(F\). With the convention of functions on \(P\backslash G_N\), inversion gives the same closed orbit for the right \(Q\)-action.

Restriction of the smooth induced sections to this closed orbit is a surjective \(Q\)-map. Here is the required extension argument. Gaussian elimination gives local matrix charts and local sections for the flag quotient, hence local trivializations of the inducing value bundle. A smooth section on the compact closed orbit has, in these charts, finitely many locally constant value descriptions. A finite disjoint clopen refinement extends those descriptions to clopen neighborhoods in the whole compact flag space; each chart value is extended by the same vector and is zero off its chosen neighborhood. Summing gives an extending section. The finitely many value vectors and clopen patches admit a common compact open stabilizer, so this extension lies in the smooth induced module. This argument does not assume that the inducing value space is finite dimensional.

Take normalized \(Q\)-Jacquet modules of this restriction map. Exactness is Lemma 1.1. The compact-average fiber calculation in Lemma 1.5 identifies the quotient with the term for (C.18). The unsplit \(B\)-row contributes \(Z(B)\). Formula (C.6) splits the \(A\)-row into its initial interval \([a,c-1]\) and final interval \(H\); induction in the first column joins the first two factors. This proves (C.17).

The normalization can also be checked directly. For block diagonal elements \(\operatorname{diag}(x,y,z)\) of sizes \(p,t,v\), the ratio of the inducing half-modulus for \(P\) to the Jacquet half-modulus for \(Q\) is
\[
|\det x|^{t/2}|\det y|^{-(p+v)/2}|\det z|^{t/2}.
\]
Replacing the unnormalized Jacquet module of the \(A\)-factor by its normalized \((t,v)\)-Jacquet module multiplies this by
\(|\det y|^{v/2}|\det z|^{-t/2}\). The result is
\(|\det x|^{t/2}|\det y|^{-p/2}\), exactly the half-modulus for \(P_{(p,t)}\subset G_u\). Thus (C.17) has no additional norm twist.

The intervals \([a,c-1]\) and \(B\) are disjoint adjacent ones. Proposition C.8 gives a \(G_u\)-equivariant surjection
\(Z(B)\times Z([a,c-1])\twoheadrightarrow Z(U)\).
Tensor it with the identity of \(Z(H)\) and compose with (C.17). We obtain an \(L_Q\)-surjection
\(r_QV\twoheadrightarrow Z(U)\boxtimes Z(H)\).
Frobenius adjunction (1.4) turns this nonzero map into a nonzero \(G_N\)-map
\(V\to i_Q^{G_N}(Z(U)\boxtimes Z(H))=M\).
The target is irreducible, so this map is surjective.

Both original intervals overlap, so they are not disjoint adjacent ones. Lemma C.6 says that every irreducible factor of \(V\) has highest derivative order \(2m\). Theorem A.6 and (C.9) give
\[
V^{(2m)}=Z([c,d-1])\times Z([a,b-1]).
\tag{C.19}
\]
The shortened intervals are nonempty and linked. If \(c=b\) they are disjoint adjacent; if \(c<b\) they still overlap. Their total degree is \(N-2m\). By the induction hypothesis or Proposition C.8, (C.19) has exactly two distinct irreducible factors.

On the other hand the highest derivative of \(M\) is
\[
M^{(2m)}=Z([a,d-1])\times Z([c,b-1]),
\tag{C.20}
\]
where the second interval may be empty. The intervals here are nested, so this derivative is irreducible by Theorem C.7. In particular \(V\) cannot be isomorphic to \(M\). The surjection just constructed has a nonzero kernel. Exactness of the \(2m\)-th derivative on a finite composition series shows that \(V\) has length at most two: each of its irreducible factors contributes a nonzero finite-length module to the length-two module (C.19). Therefore its length is exactly two and its kernel \(K(A,B)\) is irreducible. Exactness in (C.16) identifies its derivative with the other simple factor of (C.19). That factor differs from (C.20), so \(K(A,B)\not\simeq M\).

We now exclude an embedding \(M\hookrightarrow V\). By (1.4), such a map would give
\[
\operatorname{Hom}_{L_P}
 \bigl(r_PM,\,Z(B)\boxtimes Z(A)\bigr)\ne0,
\qquad L_P=G_p\times G_r.
\tag{C.21}
\]
In every surviving geometric term of \(r_PM\), the \(U\)-row must place a nonzero part in the first column: its degree \(u\) is greater than the second column degree \(r\), since \(u-r=m(d-b)>0\). By (C.6), this part is an initial subsegment of \(U\), hence contains \(\rho\nu^a\). The first-block cuspidal support of every constituent of this term consequently contains \(\rho\nu^a\), by Theorem 1.6 and exact induction. The first factor of the target in (C.21) has support \([c,d]\) and contains no \(\rho\nu^a\). These are distinct actual cuspidals: different real norm twists have different central absolute values. Thus no term, and no constituent of \(r_PM\), can equal the target. All these Jacquet terms have finite length by (C.6), the geometric lemma and Corollary 1.7. Applying Hom to a composition series gives zero in (C.21), a contradiction.

A split (C.16) would embed \(M\) into \(V\), so the sequence is nonsplit. Since the two factors are distinct and no simple submodule can be \(M\), the only simple submodule is the displayed kernel. Every nonzero proper submodule of a length-two module is simple; its multiplicity here is one. Hence that kernel is the unique nonzero proper submodule and the quotient is uniquely \(M\). This completes the induction for the higher-start-first order.

For the opposite order use exact admissible duality and (C.7). On the dual cuspidal line its dual is
\(Z(A^\vee)\times Z(B^\vee)\), with intervals
\([-b,-a]\) and \([-d,-c]\). The first has higher start, and
\(-d<-b\le -c<-a\); thus the case just proved applies. Its irreducible quotient is the product for the dual union and intersection. Dualizing its nonsplit length-two sequence gives an embedding of exactly \(M\) into \(Z(A)\times Z(B)\), with a distinct irreducible quotient and no other nonzero proper submodule. Duality is involutive, so a splitting on this side would split the dual sequence. This proves the assertions for the opposite order. ∎

**Corollary C.10 (two-segment irreducibility).** For any two segments, of arbitrary cuspidal ranks and on arbitrary cuspidal lines, \(Z(\Delta_1)\times Z(\Delta_2)\) is irreducible if and only if they are unlinked. When they are linked its length is two in either order.

**Proof.** The unlinked direction is Theorem C.7, including coincident, nested and different-line segments. Linked segments lie on one actual cuspidal line. Translate its base and order their unequal starting points to obtain the inequalities of Theorem C.9; these changes only rename the same actual cuspidals. That theorem covers both possible orders, including adjacency and overlap, and gives reducibility with length two. ∎

The linked-pair result is Zelevinsky's Proposition 4.6 [Zelevinsky 1980]. For three or more factors, the unlinked sufficiency remains Theorem C.7. The full multisegment and Langlands classifications, the general Q-product criterion, and square-integrability and temperedness are separate results.

## What this lesson does not prove

The full Langlands and multisegment classifications, irreducibility criteria for general products of three or more segments and for Q-products, the generic classification, square-integrability and temperedness theorems in Section 2 are not proved in this lesson. Appendix C proves the full distinct-support classification and entire submodule lattice on one cuspidal line (Theorems C.2–C.3), constructs Z and Q for every segment with all block Jacquet modules and contragredients (Theorem C.4), and gives their genericity and every derivative (Theorem C.5). Its highest-level argument handles arbitrary lines, ranks and repetitions, and proves irreducibility of every unlinked Z-product, including nested and repeated segments (Lemma C.6 and Theorem C.7). Proposition C.8 proves disjoint products with gaps and both adjacent disjoint Z- and Q-pair extensions, including uniqueness and nonsplitting. Theorem C.9 proves the full linked overlapping-pair calculation, including its union/intersection quotient, length two, distinct factors, nonsplitting and unique submodule, in every cuspidal rank and both field characteristics. Corollary C.10 gives the two-segment Z-product criterion in either order. These results do not establish the full multisegment classification or the corresponding general Q-product theorem. Appendix A supplies the normalized derivative foundations, highest-derivative pairing, irreducibility of cuspidal products without adjacent twists and the full cuspidal-pair criterion. Appendix B proves full Whittaker uniqueness, irreducible supercuspidal mirabolic restriction and the unique generic constituent of cuspidal induction. The rank-three example's constituent classification, multiplicities, unique quotients and genericity are proved directly in Section 6; its temperedness assertion is recorded as unproved and is not used in those arguments. Section 1 proves the general Jacquet-module criterion, admissibility and adjunction, block geometric lemma, cuspidal support and finite length independently of the remaining classification statements.

The rank-one irreducibility, parameter symmetry and classification theorems have complete internal proofs in [Whittaker models, Kirillov models and the local classification, Theorem 4.2, Section 5 and Theorem 6.1](../../automorphic-forms-and-representations-of-gl2/src/whittaker-models-kirillov-models-and-the-local-classification.md), recalled at the beginning of Section 3. Their original principal-series reference is [Jacquet–Langlands 1970, Theorem 3.3]. Normalized induction duality is proved in [Normalized induction and Jacquet modules, Proposition 1.2](../../automorphic-forms-and-representations-of-gl2/src/normalized-induction-and-jacquet-modules.md#1-induction-with-the-square-root-modulus). We used these written proofs to establish agreement with the rank-two segment description. The rank-one geometric lemma, the resulting intrinsic support calculation and the rank-two Steinberg coefficient summation were proved here.

## References

- [Cogdell 2000] James W. Cogdell, [*Notes on L-functions for GL_n*](https://indico.ictp.it/event/a02086/contribution/1/material/0/0.pdf), ICTP lectures, 31 July–18 August 2000, §1.2, Theorem 1.2, printed pp.7–8: the Gelfand–Kazhdan symmetry method and relevant block permutations.
- [Bernstein–Zelevinsky 1977] I. N. Bernstein and A. V. Zelevinsky, [“Induced representations of reductive p-adic groups. I”](https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/BZ-induced-1.pdf), author-hosted article, *Annales scientifiques de l’École normale supérieure* 10 (1977), 441–472, Theorem 2.9, Lemma 2.12, §§3.2–3.8, Theorem4.2 and its proof in §§4.7–4.8, and §§5–6.
- [Casselman 2019] Bill Casselman, [*Introduction to admissible representations of p-adic groups*, Chapter III, “Induced representations and the Jacquet module”](https://www.math.ubc.ca/~cass/research/pdf/Jacquet.pdf), author notes revised 29 April 2019, Proposition III.5.5 and Theorem III.5.6.
- [Getz–Hahn 2022] Jayce R. Getz and Heekyoung Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), author draft of 22 April 2022, §§8.2–8.4 and §10.5.
- [Jacquet–Langlands 1970] Hervé Jacquet and Robert P. Langlands, [*Automorphic forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf), freely accessible IAS re-typeset edition, §§2–3, especially Theorem 3.3.
- [Zelevinsky 1980] Andrei V. Zelevinsky, [“Induced representations of reductive p-adic groups. II. On irreducible representations of GL(n)”](https://www.numdam.org/item/ASENS_1980_4_13_2_165_0/), free journal archive, *Annales scientifiques de l’École normale supérieure* 13 (1980), 165–210, §§1.10–1.11, §§2.1–2.11, §§3.1–3.10, §§4.3–4.6, Theorem 6.1 and §9.
- [Wedhorn 2000] Torsten Wedhorn, [*The local Langlands correspondence for GL(n) over p-adic fields*](https://arxiv.org/abs/math/0011210v2), lectures at the School on Automorphic Forms on GL(n), ICTP Trieste, 2000, §§2.2–2.4.
