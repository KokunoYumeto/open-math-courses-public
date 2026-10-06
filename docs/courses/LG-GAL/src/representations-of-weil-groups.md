# Representations of Weil groups

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Weil group allows Frobenius to act by an arbitrary invertible matrix while keeping inertia compact. This separates two kinds of information: a finite inertia action and the eigenvalues, or Jordan blocks, of Frobenius. We prove how that separation controls irreducibility and semisimplicity, then compute the determinant of induction and classify the representations at a real place.

We assume Frobenius elements and determination by traces and basic finite-group representation theory over a field of characteristic zero. Section 0 proves the local reciprocity theorem needed below. The local reciprocity and Weil-group statements used here are recalled precisely in §1. All representations in §§2–5 are finite-dimensional complex representations. For a nonarchimedean Weil group, “smooth” means that every vector has an open stabilizer. At an archimedean place we use continuous representations in the usual complex topology.

## 0. Local norm foundations in both characteristics

The finite reciprocity input in §1 has a source chain that must be verified independently of the Weil-group topology. We first reconstruct the local norm facts needed by that chain, including the characteristic-\(p\) unit argument. Write \(R=\mathcal O_F\). All local fields and valuations here are those constructed in the first lesson.

**Lemma 0.1 (normal bases and Hilbert 90).** If \(L/F\) is finite Galois with group \(G\), there is an \(a\in L\) such that \(\{\sigma a\mid\sigma\in G\}\) is an \(F\)-basis. Every multiplicative cocycle \(c_{\sigma\tau}=c_\sigma\sigma(c_\tau)\) in \(L^\times\) has the form \(c_\sigma=b/\sigma b\) for some \(b\ne0\).

**Proof.** Choose a primitive element \(t\), using the separable primitive-element proof of the first lesson, and let \(d=|G|\). For variables \(X_0,\ldots,X_{d-1}\), put \(a(X)=\sum_jX_jt^j\). The linear forms \(\sigma a(X)\), over \(L\), are independent: their coefficient matrix is the Vandermonde matrix on the distinct conjugates \(\sigma t\). The polynomial \(\det(z_{\sigma\tau})_{\sigma,\tau\in G}\) in independent variables \(z_\rho\) is nonzero, since setting \(z_1=1\) and all other variables zero makes a permutation matrix. Substitute \(z_\rho=\rho a(X)\); the invertible linear change just noted preserves nonvanishing. A nonzero polynomial over \(L\) does not vanish on every \(F^d\), since \(F\) is infinite: induct on the number of variables and use the finite bound on roots in one variable. Choose \(X_j\in F\) where the determinant is nonzero. Any \(F\)-linear relation among the conjugates of \(a(X)\) would, after applying all \(\sigma\), lie in this invertible matrix's kernel. There is no such relation.

Distinct field automorphisms are linearly independent as maps, by the first lesson's minimal-relation proof. Hence some \(x\in L\) gives \(b=\sum_{\tau\in G}c_\tau\tau x\ne0\). The cocycle identity gives \(\sigma b=c_\sigma^{-1}b\), proving the formula. In a cyclic extension with generator \(s\), an element \(c\) of norm one gives such a cocycle by \(c_{s^i}=c\,s(c)\cdots s^{i-1}(c)\); the norm-one condition makes it well defined at exponent \(d\). Thus the norm-one elements are exactly the quotients \(b/sb\). \(\square\)

**Lemma 0.2 (the cyclic cohomology calculation used below).** Let \(C=\langle s\rangle\) have order \(d\), acting on an abelian group \(M\), written additively. Put \(D=s-1\) and \(N=1+s+\cdots+s^{d-1}\), and define
\[
T^0(M)=\ker D/\operatorname{im}N,\qquad
T^1(M)=\ker N/\operatorname{im}D.
\tag{0N1}
\]
For a short exact sequence, these two groups have an exact, repeating six-term sequence. If both are finite, put \(h(M)=|T^0(M)|/|T^1(M)|\). Then \(h(B)=h(A)h(Q)\) for \(0\to A\to B\to Q\to0\), whenever two of the three quotients are defined. A finite \(M\) has \(h(M)=1\), and an induced module \(\mathbf Z[C]\otimes M_0\), with \(C\) permuting its factors, has both groups zero.

**Proof.** The operators obey \(DN=ND=0\); alternate them in a two-periodic complex with every term \(M\). A short exact sequence of groups gives a termwise exact sequence of these complexes. A closed element of \(Q\) lifts to \(B\); its differential lies in \(A\), giving the connecting map. A different lift changes that element by a boundary, and applying the differential twice gives zero. This defines the six-term sequence. Exactness can be checked directly: a lift whose connecting element is a boundary can be corrected to a closed lift; a closed element mapping to a boundary can be corrected by a lifted preimage to lie in \(A\). These two corrections at either parity prove exactness everywhere.

For finite \(M\), the identities \(|\ker D||\operatorname{im}D|=|M|=|\ker N||\operatorname{im}N|\) give \(h(M)=1\). For the short exact sequence, take the alternating product of orders in the six-term sequence: writing each order as the product of its adjacent image orders makes all image factors cancel. If only two pairs of groups are known finite, exactness first makes the third pair finite. On the induced module, invariants are constant tuples, every such tuple is a norm, and a tuple of coordinate sum zero is a successive-difference tuple. Thus (0N1) vanishes. These arguments apply also to multiplicative groups, interpreting \(D\) as a quotient and \(N\) as a product. \(\square\)

**Lemma 0.3 (unit calculation without a characteristic restriction).** In a cyclic local extension \(L/F\), \(h(\mathcal O_L^\times)=1\). In fact there is an open invariant subgroup \(V\subset\mathcal O_L^\times\) with \(T^0(V)=T^1(V)=0\).

**Proof.** Scale the normal basis of Lemma 0.1 by an element of \(F^\times\) so that its elements lie in \(\mathcal O_L\). Let \(\Lambda'\) be their \(R\)-span. It is an invariant free lattice isomorphic to \(R[C]\). There is an \(n\geq0\) with \(\pi^n\mathcal O_L\subset\Lambda'\subset\mathcal O_L\), where \(\pi\) is a uniformizer of \(F\): express a finite integral basis in this \(F\)-basis and clear its denominators. Put \(\Lambda=\pi^{n+1}\Lambda'\). Then
\[
\Lambda\Lambda\subset\pi^{2n+2}\mathcal O_L
\subset\pi^{n+2}\Lambda'=\pi\Lambda.
\tag{0N2}
\]
Consequently \(V_i=1+\pi^i\Lambda\), \(i\geq0\), is a group. For the inverse use the convergent series \((1+x)^{-1}=1-x+x^2-\cdots\), with \(x^j\in\pi^{j-1}\Lambda\); the finite lattice is complete and closed. Multiplication modulo \(V_{i+1}\) is addition, and
\[
V_i/V_{i+1}\simeq\Lambda/\pi\Lambda\simeq k_F[C]
\tag{0N3}
\]
as \(C\)-modules. Lemma 0.2 makes the alternating \(D,N\) complex exact on each quotient.

It is exact on \(V=V_0\) as well. Given a closed element at either parity, reduce it in \(V_i/V_{i+1}\), express that reduction as a boundary there, and lift its preimage to \(V_i\). Subtract the boundary, in additive group notation, to leave a closed error in \(V_{i+1}\). Starting at \(i=0\) and repeating, the preimages converge in \(V\), since \(V=\varprojlim V/V_i\). The maps \(D,N\) are continuous, so the limit has boundary equal to the original element. This proves both vanishings without using a logarithm or exponential.

The subgroup \(V\) is open, and the unit group is compact by the first lesson's residue-digit description, so \(\mathcal O_L^\times/V\) is finite. Lemma 0.2 then identifies the two cohomology groups of the units with those of this finite quotient and proves their quotient of orders is one. \(\square\)

**Proposition 0.4 (cyclic norm index and openness).** For a cyclic extension \(L/F\) of degree \(d\), in either characteristic,
\[
[F^\times:N_{L/F}L^\times]=d.
\tag{0N4}
\]
For every finite separable extension the norm subgroup contains an open neighborhood of one.

**Proof.** The valuation gives a short exact sequence
\(1\to\mathcal O_L^\times\to L^\times\to\mathbf Z\to0\), with trivial action on \(\mathbf Z\). Here \(T^0(\mathbf Z)=\mathbf Z/d\mathbf Z\), \(T^1(\mathbf Z)=0\), so its quotient is \(d\). Lemmas 0.2–0.3 give \(h(L^\times)=d\). Lemma 0.1 makes \(T^1(L^\times)=0\). Hence \(T^0(L^\times)=F^\times/NL^\times\) has order \(d\), proving (0N4).

For a general finite separable extension, nondegeneracy of trace was proved in the first lesson, so choose \(t\in L\) with \(\operatorname{Tr}_{L/F}t=1\). The norm polynomial is
\(N(1+tX)=1+X+\sum_{j=2}^{[L:F]}c_jX^j\), with \(c_j\in F\): its linear coefficient is the sum of conjugates of \(t\). Choose \(a\) so large that every \(\pi^{a(j-1)}c_j\) is in \(\pi R\). For any \(y\in R\), the equation
\[
X+\sum_{j=2}^{[L:F]}\pi^{a(j-1)}c_jX^j=y
\tag{0N5}
\]
has a solution in \(R\), by the first lesson's Hensel proof, since it reduces to \(X=y\) with derivative one. Its norm is \(N(1+t\pi^aX)=1+\pi^ay\), so every \(1+\pi^aR\) element is a norm. This proves openness. \(\square\)

The all-characteristic unit construction can be compared with [Sharifi's free author notes, *Algebraic Number Theory*, §9.1, Lemma 9.1.3 and Proposition 9.1.4](https://www.math.ucla.edu/~sharifi/notes/algnum-ch09.html). The cyclic complexes, inverse-limit correction and norm-index proof used here are written above. Lemmas 0.5–0.6 and Theorem 0.7 construct finite reciprocity and functoriality, and §0C proves cofinality and completion. These additional proofs are required because (0N4) alone does not construct a reciprocity homomorphism.

### 0A. The finite cohomology calculation

We now construct finite local reciprocity from the norm calculation. The coefficient group \(A\) in the next lemma is written additively; later \(A=L^\times\) is written multiplicatively.

**Lemma 0.5 (cochains, transfer and the low-degree kernel).** Finite-group cohomology has restriction, inflation and corestriction. For \(H\leq G\),

\[
\operatorname{Cor}_H^G\operatorname{Res}_H^G=[G:H].
\tag{0C1}
\]
Positive groups are killed by \(|G|\). For \(H\triangleleft G\), if \(H^1(H,A)=0\), then

\[
0\longrightarrow H^2(G/H,A^H)\xrightarrow{\mathrm{Inf}}H^2(G,A)
\xrightarrow{\mathrm{Res}}H^2(H,A)
\tag{0C2}
\]
is exact. Cup products commute with inflation, restriction, coefficient connecting maps and satisfy the projection formula for corestriction. Corestriction on \(H^0\) is the coefficient norm. On \(H^1(H,\mathbf Q/\mathbf Z)\), with trivial coefficients, it sends a character \(\chi\) to \(\chi\circ\operatorname{Ver}_H^G\).

**Proof.** Here are the constructions and the identities needed below. The homogeneous bar resolution has \(P_r=\mathbf Z[G^{r+1}]\), diagonal left action, boundary the alternating sum omitting a coordinate, and augmentation \(P_0\to\mathbf Z\). Its square is zero because each pair of omissions occurs twice with opposite signs. It is exact on underlying abelian groups: insertion of 1 at the beginning is a contraction, with \(ds+sd=1\). Each \(P_r\) is free over \(\mathbf Z[G]\), since every diagonal orbit has a unique representative with first coordinate 1. Define cohomology by \(\operatorname{Hom}_G(P_\bullet,A)\). Equivalently use functions \(f:G^r\to A\), with

\[
(df)(g_1,\ldots,g_{r+1})=g_1f(g_2,\ldots,g_{r+1})
+\sum_{i=1}^r(-1)^if(g_1,\ldots,g_ig_{i+1},\ldots,g_{r+1})
+(-1)^{r+1}f(g_1,\ldots,g_r).
\tag{0C3}
\]
The identification evaluates a homogeneous cochain on \((1,g_1,g_1g_2,\ldots,g_1\cdots g_r)\); its inverse sends \((h_0,\ldots,h_r)\) to \(h_0f(h_0^{-1}h_1,\ldots,h_{r-1}^{-1}h_r)\). These formulas intertwine the boundaries. Short exact coefficient sequences give long exact sequences by the lift-and-correct argument of Lemma 0.2, since the bar terms are free.

The same \(P_\bullet\), restricted to \(H\), is a free \(H\)-resolution of \(\mathbf Z\). It computes \(H\)-cohomology: between it and the \(H\)-bar resolution, construct augmentation-preserving chain maps inductively, lifting each basis element's boundary through the next surjective boundary in the exact target. Two such maps are chain homotopic by the same induction on their difference. Thus the comparison is canonical on cohomology. Restriction views a \(G\)-equivariant cochain as \(H\)-equivariant. If \(\alpha:P_r\to A\) is \(H\)-equivariant, define

\[
(T\alpha)(x)=\sum_{t\in G/H}t\alpha(t^{-1}x).
\tag{0C4}
\]
Changing \(t\) to \(th\) leaves its summand unchanged. Reindexing cosets proves \(G\)-equivariance; the boundary commutes with (0C4). This defines corestriction. For a \(G\)-equivariant cochain every summand is the original cochain, proving (0C1) already on complexes. Restriction to the trivial group has zero positive cohomology, by the contraction above, so (0C1) kills positive cohomology by \(|G|\). In degree zero (0C4) is \(\sum_t ta\), namely the norm in multiplicative notation.

For cup products split a homogeneous tuple at its common coordinate: \((g_0,\ldots,g_{r+s})\mapsto(g_0,\ldots,g_r)\otimes(g_r,\ldots,g_{r+s})\). Omissions on either side give the Leibniz rule; the two terms at the common coordinate cancel. Consequently it descends to cohomology. Restriction and inflation commute with this formula. Lifting a cocycle through a coefficient surjection and applying its boundary proves compatibility with connecting maps, with sign \((-1)^r\) for the second factor whenever the corresponding tensor coefficient sequence is exact. For an \(H\)-cochain \(\alpha\) and \(G\)-cochain \(\beta\), each summand in (0C4) applied to their cup product is

\[
t\alpha(t^{-1}g_0,\ldots,t^{-1}g_r)
\otimes t\beta(t^{-1}g_r,\ldots,t^{-1}g_{r+s})
=t\alpha(t^{-1}g_0,\ldots,t^{-1}g_r)\otimes\beta(g_r,\ldots,g_{r+s}).
\]
Summing proves the projection formula, without a flatness assumption on coefficients. Below the connecting map is for \(0\to\mathbf Z\to\mathbf Q\to\mathbf Q/\mathbf Z\to0\); its commutation with restriction and corestriction follows directly from their cochain maps. No tensor-exactness assertion is needed for that commutation.

Write \(gt_i=t_{g(i)}h_i(g)\) for left \(H\)-coset representatives. The product of the \(h_i(g)\), in \(H^{\mathrm{ab}}\), is independent of representatives: replacing \(t_i\) by \(t_ik_i\) changes the factors by \(k_{g(i)}^{-1}h_i(g)k_i\), whose extra products cancel. For \(gg'\), reindexing the factors gives their two products, so this is the homomorphism \(\operatorname{Ver}\). To compute (0C4) on a character, take right-coset representatives \(t_i^{-1}\), write \(x=h(x)r(x)\), and represent the character by the homogeneous \(H\)-cochain \(\chi(h(x_1))-\chi(h(x_0))\). At \((1,g)\), (0C4) sums \(\chi(h(t_i^{-1}g))\). Inverting \(t_i^{-1}g=h r\) expresses the left-coset permutation for \(g^{-1}\); the sum is \(-\chi(\operatorname{Ver}(g^{-1}))=\chi(\operatorname{Ver}(g))\). This proves the stated character formula.

For (0C2) we give a low-degree argument. A normalized 2-cocycle \(c\) defines an extension \(A\times G\) by \((a,g)(b,h)=(a+gb+c(g,h),gh)\); its cocycle identity is exactly associativity. A section of any such extension recovers \(c\), and changing the section adds a coboundary. A cocycle can be normalized by its value at the identity; thus this description covers every class. Vanishing of a restriction means the extension splits over \(H\). Fix its splitting \(H\to\widetilde G\). Any lift of \(g\in G\) conjugates it, with its argument conjugated back by \(g^{-1}\), to another splitting over \(H\); their difference is a 1-cocycle. The hypothesis \(H^1(H,A)=0\) permits correcting that lift by an element of \(A\) to normalize the fixed splitting. Its normalizer therefore maps onto \(G\), has kernel \(A^H\), and contains the split \(H\) as a normal subgroup. Quotienting by it gives an extension of \(G/H\) by \(A^H\). Inflating that extension and then extending its coefficient kernel to \(A\) recovers the original extension: the normalizer and \(A\) together exhaust it and intersect in \(A^H\). This proves exactness at the middle. If an inflated extension splits over \(G\), correct its splitting by an element of \(A\) so it agrees with the canonical splitting on \(H\), again using \(H^1(H,A)=0\). It then descends to a splitting of that quotient extension. This proves injectivity. All constructions commute with field embeddings and with their induced coefficient maps. \(\square\)

**Lemma 0.6 (the local invariant, without using reciprocity).** Put

\[
B(F)=H^2_{\mathrm{cont}}(G_F,(F^s)^\times).
\]
There is a canonical isomorphism \(\operatorname{inv}_F:B(F)\simeq\mathbf Q/\mathbf Z\). Its normalization on an unramified cyclic extension of degree \(n\), with arithmetic Frobenius generator and parameter \(a\in F^\times\), is \(v_F(a)/n\). For finite separable \(E/F\), restriction multiplies invariants by \([E:F]\), and corestriction preserves them. A finite Galois \(L/F\) of degree \(d\) has relative group \(H^2(\operatorname{Gal}(L/F),L^\times)\) exactly the subgroup \(\frac1d\mathbf Z/\mathbf Z\).

**Proof.** For a cyclic group the free resolution alternating \(s-1\) and \(1+\cdots+s^{n-1}\) is exact: coefficient comparison in \(\mathbf Z[C]\) says that a difference-zero element is a multiple of the norm, and a coefficient-sum-zero element is a successive difference. Resolution comparison, proved in Lemma 0.5, makes this compute ordinary cohomology too. In particular \(H^2(C,L^\times)=F^\times/NL^\times\), of order \(n\) by Proposition 0.4; \(H^1=0\) by Hilbert 90.

For arbitrary finite Galois \(L/F\), the order of this relative \(H^2\) divides \(|G|\). First suppose \(G\) is a \(p\)-group and induct on its order, using a normal subgroup \(H\) of index \(p\). Such a subgroup exists: the class equation gives a nontrivial center, Cauchy's argument gives a central subgroup of order \(p\), and induction on the quotient gives an order-\(p\) quotient, unless \(G\) itself has order \(p\). Cauchy's argument is the cyclic permutation of tuples \((x_1,\ldots,x_p)\) with product one: there are \(|G|^{p-1}\) tuples, nonfixed orbits have size \(p\), and fixed tuples are \((x,\ldots,x)\) with \(x^p=1\). Divisibility by \(p\) forces a nonidentity such \(x\). Hilbert 90 and (0C2) make the degree-two restriction kernel have order \(p\); its image has order dividing \(|H|\) by induction. The asserted bound follows.

For a general \(G\), use a Sylow \(p\)-subgroup \(P\). For completeness, take a maximal \(p\)-subgroup and let it act on \(G/P\). Its fixed cosets are \(N_G(P)/P\). If \(p\) divided \([G:P]\), orbit counting and Cauchy's argument in \(N_G(P)/P\) would produce a larger \(p\)-subgroup, a contradiction. Thus the index is prime to \(p\). Equation (0C1) makes restriction injective on the \(p\)-primary part of \(H^2\); the \(p\)-group bound makes that part finite of order dividing \(|P|\). The \(|G|\)-annihilation in Lemma 0.5 permits primary decomposition, so the whole order divides \(|G|\).

Let \(F_n/F\) be the unramified degree-\(n\) extension of the first lesson. Its unit norms are onto: the cyclic norm index is \(n\), while the valuation of a norm is \(n\) times the valuation, so that index is already accounted for by valuations. Norm-one units are quotients \(b/sb\) by Hilbert 90, and multiplying \(b\) by a base-field uniformizer power makes it a unit. Thus units have zero cyclic \(H^1,H^2\). Valuation identifies the relative degree-two group with \(H^2(C_n,\mathbf Z)=\mathbf Z/n\mathbf Z\). The carry cocycle for the parameter \(a\) has invariant \(v_F(a)/n\). Equivalently the boundary for \(0\to\mathbf Z\to\mathbf Q\to\mathbf Q/\mathbf Z\to0\) identifies it with the character of arithmetic Frobenius of that value. Averaging kills positive cohomology of rational coefficients, justifying that boundary identification. Inflation preserves the character's value, so the union of unramified relative groups is \(\mathbf Q/\mathbf Z\).

For any finite separable \(E/F\), this unramified invariant is multiplied on restriction by \(ef=[E:F]\): residue Frobenius becomes its \(f\)-th power, and the normalized valuation cocycle is multiplied by the ramification index \(e\). These two operations commute with the boundary just described.

Now take arbitrary Galois \(L/F\) of degree \(d\). Every unramified class in \(\frac1d\mathbf Z/\mathbf Z\) restricts to zero over \(L\), by that multiplication calculation. In the finite compositum \(LF_d/F\), (0C2) and Hilbert 90 place it in \(H^2(G,L^\times)\). This embeds a subgroup of order \(d\); the previously proved bound forces equality. Continuous cocycles have finite image and factor through a finite quotient after adjoining their finitely many coefficients. To justify the factorization, each fibre of a continuous function from a profinite finite product to a discrete set is compact and open; finitely many coset boxes cover those fibres, and the intersection of their open normal subgroups gives a common finite quotient. Enlarge the fixed field to contain the coefficients. Hilbert 90 and (0C2) make all these relative inflations injective. Taking their directed union therefore proves \(B(F)=\mathbf Q/\mathbf Z\), and the restriction formula now applies to every class. Finally restriction \(B(F)\to B(E)\) is onto, since multiplication by \([E:F]\) on \(\mathbf Q/\mathbf Z\) is onto. Write \(c=\operatorname{Res}b\) and apply (0C1); this proves \(\operatorname{inv}_F(\operatorname{Cor}c)=\operatorname{inv}_E(c)\). No reciprocity theorem was used. \(\square\)

### 0B. Finite reciprocity and its functoriality

**Theorem 0.7 (finite abelian reciprocity).** There is a canonical continuous dense homomorphism

\[
\operatorname{rec}^{\mathrm{ar}}_F:F^\times\longrightarrow G_F^{\mathrm{ab}}
\tag{0C5}
\]
whose projection to each finite abelian \(L/F\) is onto with kernel \(N_{L/F}L^\times\). On an unramified quotient it sends a uniformizer to arithmetic Frobenius. For every finite separable \(E/F\),

\[
\operatorname{rec}^{\mathrm{ar}}_F(N_{E/F}x)
=\operatorname{incl}\bigl(\operatorname{rec}^{\mathrm{ar}}_E(x)\bigr),
\qquad
\operatorname{rec}^{\mathrm{ar}}_E(a)
=\operatorname{Ver}_{G_E}^{G_F}\bigl(\operatorname{rec}^{\mathrm{ar}}_F(a)\bigr).
\tag{0C6}
\]
Here \(x\in E^\times,a\in F^\times\). Field conjugation commutes with reciprocity. For finite abelian \(L,M/F\), \(NL^\times\subseteq NM^\times\) exactly when \(M\subseteq L\).

**Proof.** Let \(\chi:G_F\to\mathbf Q/\mathbf Z\) be a finite continuous character. Its boundary \(\delta\chi\) is represented by the integer cocycle obtained from any rational lifts: \(\widetilde\chi(g)+\widetilde\chi(h)-\widetilde\chi(gh)\). Sending an integer \(r\) to \(a^r\), for \(a\in F^\times\), defines its parameter class \(a\cup\delta\chi\in B(F)\). It is independent of lifts, and additive in \(\chi\) and multiplicative in \(a\). Define reciprocity by

\[
\chi\bigl(\operatorname{rec}^{\mathrm{ar}}_F(a)\bigr)
=\operatorname{inv}_F(a\cup\delta\chi).
\tag{0C7}
\]
This defines compatible elements in every finite abelian quotient. Here is the finite duality justification. Characters of a subgroup into \(\mathbf Q/\mathbf Z\) extend to a finite abelian group: when adjoining a generator \(b\) whose first multiple in the subgroup is \(nb\), choose a value whose \(n\)-fold multiple is the prescribed value of \(nb\). Divisibility of \(\mathbf Q/\mathbf Z\) permits the choice. Induction and the cyclic calculation show that there are exactly \(|A|\) characters of a finite abelian \(A\), and they separate its points. Evaluation therefore identifies \(A\) with its double dual.

For a character of order \(n\), choose the generator \(s\) of its cyclic quotient with \(\chi(s)=1/n\). In the extension representing \(a\cup\delta\chi\), a lift \(S\) of \(s\) satisfies \(S^n=a\): multiplying the rational-lift carry cocycle around the \(n\) powers gives that relation. Replacing \(S\) by \(bS\) replaces \(a\) by \(N_{L/F}(b)a\), and every cyclic extension class is obtained this way, by the cyclic resolution in Lemma 0.6. Thus the parameter map is precisely \(F^\times/NL^\times\simeq\frac1n\mathbf Z/\mathbf Z\). A nonzero character therefore gives a nonzero function of \(a\). For a finite abelian quotient \(A\), the map in (0C7) consequently has image all of \(A\): otherwise a nonzero character of its quotient by that image would vanish on every \(a\), a contradiction.

Norms from an abelian \(L/F\) lie in the projection kernel. Indeed (0C4) and the projection formula give

\[
(N_{L/F}x)\cup\delta\chi
=\operatorname{Cor}_{L/F}\bigl(x\cup\operatorname{Res}_{L/F}\delta\chi\bigr)=0
\]
for every character of \(\operatorname{Gal}(L/F)\). The norm quotient has order at most \([L:F]\): take a tower of cyclic prime-degree extensions, using a subgroup series of the finite abelian Galois group, and apply Proposition 0.4 at each step. Such a series exists by Cauchy's argument and induction on the abelian quotient. Norm transitivity follows by grouping the conjugates in the norm product. At a tower step \(L/M/F\), the quotient of \(N_{M/F}M^\times\) by \(N_{L/F}L^\times\) is an image of \(M^\times/N_{L/M}L^\times\), so its index is at most \([L:M]\). Induction gives the bound. Surjectivity already makes the reciprocity kernel have index exactly \([L:F]\), hence the two kernels agree. Proposition 0.4 proves openness of that kernel, and thus continuity. The compatible finite surjections prove density of (0C5).

For the norm identity in (0C6), test on any finite character of \(G_F\). Corestriction preserves invariants by Lemma 0.6, and its projection formula changes the parameter \(x\) into \(N_{E/F}x\); (0C7) gives equality. For the transfer identity test on a finite character \(\chi\) of \(G_E\). Since \(a\) is a base-field parameter,

\[
\operatorname{inv}_E(a\cup\delta\chi)
=\operatorname{inv}_F\bigl(a\cup\delta(\operatorname{Cor}\chi)\bigr).
\]
Lemma 0.5 identifies \(\operatorname{Cor}\chi\) with \(\chi\circ\operatorname{Ver}\), proving the second identity. These operations and the unramified invariant are preserved by the valued field isomorphisms in Galois conjugation, proving conjugation compatibility. For unramified characters (0C7) is \(\chi(\operatorname{Frob}_{\mathrm{ar}})v_F(a)\), by the carry-cocycle calculation, so it gives the stated normalization.

Finally take the compositum \(LM\). Its reciprocity map is onto. The inverse images of the two projection kernels are respectively \(NL^\times,NM^\times\), by what was just proved. Inclusion of norm groups therefore is exactly inclusion of those Galois kernels; taking fixed fields reverses it and gives \(M\subseteq L\). This proves the last assertion. \(\square\)

These proofs use the finite cochains and transfer construction in [Sharifi's free *Group and Galois Cohomology*, §§1.2–1.5, 1.8–1.9](https://www.math.ucla.edu/~sharifi/notes/groupcoh-ch01.html), the unramified invariant calculation in [Milne's free *Class Field Theory*, III§§1–2](https://www.jmilne.org/math/CourseNotes/CFT.pdf), and the character and norm-group framework in [Sharifi's free *Algebraic Number Theory*, §8.1–§8.2](https://www.math.ucla.edu/~sharifi/notes/algnum-ch08.html). Every used cohomological and reciprocity identity has been constructed above. The finite abelian norm calculation avoids assuming the negative-degree Tate cup-product theorem. The formal-module cofinality argument in §0C will identify the completed multiplicative group with the whole abelian Galois group; finite surjectivity alone is not that identification.

### 0C. Formal modules and abelian cofinality

**Lemma 0.8A (integral formal modules, in both characteristics).** Put \(R=\mathcal O_F\), choose a uniformizer \(\pi\), and write \(q=|R/\pi R|\). Let \(\mathcal F_\pi\) consist of the series
\[
f(X)\in R[[X]],\qquad f(X)=\pi X+O(X^2),\qquad f(X)\equiv X^q\pmod\pi.
\tag{0LT1}
\]
Every \(f\in\mathcal F_\pi\) admits a unique commutative formal group law \(F_f\) for which \(f\) is an endomorphism. There are integral scalar endomorphisms \([a]_f=aX+O(X^2)\) for all \(a\in R\), satisfying \([a+b]_f=F_f([a]_f,[b]_f)\), \([ab]_f=[a]_f\circ[b]_f\), and \([\pi]_f=f\). For \(f,g\in\mathcal F_\pi\), their formal modules are canonically isomorphic by an integral series with linear coefficient one.

**Proof.** We give the coefficient construction. For \(f,g\in\mathcal F_\pi\) and a linear form \(L\) in any finite number of variables, seek \(H=L+O(\text{degree }2)\) with
\[
f(H(X_1,\ldots,X_r))=H(g(X_1),\ldots,g(X_r)).
\tag{0LT2}
\]
Suppose this holds through degree \(d-1\), and let \(E_d\) be the degree-\(d\) part of the left side minus the right side. Modulo \(\pi\), that difference is \(\overline H^{q}-\overline H(X_1^q,\ldots,X_r^q)=0\): coefficients lie in \(\mathbf F_q\). Adding a homogeneous \(C_d\) to \(H\) changes the error to \(E_d+(\pi-\pi^d)C_d\). Since \(\pi^{d-1}-1\) is a unit, the unique correction
\[
C_d=-\frac{E_d}{\pi(1-\pi^{d-1})}
\tag{0LT3}
\]
is integral. Induction gives a unique series. All compositions are defined coefficient by coefficient because their constant terms vanish.

Take \(f=g\) and \(L=X+Y\) to obtain \(F_f\). Swapping variables gives another solution with the same linear form, hence commutativity. The two associative composites have linear form \(X+Y+Z\) and satisfy (0LT2), hence coincide. Substitution \(Y=0\) gives the unique solution with linear term \(X\), namely \(X\); thus the identity is zero. The equation \(F_f(X,i(X))=0\) determines each coefficient of \(i=-X+O(X^2)\) successively with coefficient one, proving the inverse axiom. In particular
\(F_f(X,Y)=X+Y+XYC(X,Y)\) with \(C\) integral.

Apply (0LT2) with linear term \(aX\) to obtain \([a]_f\). The series \([a]_f(F_f(X,Y))\) and \(F_f([a]_f(X),[a]_f(Y))\) have the same linear form and intertwining equation, so are equal. The same uniqueness proves the stated addition and composition identities, \([1]_f=X\), and \([\pi]_f=f\). For two choices of \(f,g\), the solution of \(gH=Hf\) with linear coefficient one is a homomorphism by the same two-variable comparison. Reversing \(f,g\) constructs its inverse. A series with unit linear coefficient also has an integral compositional inverse directly: the degree-\(d\) inverse coefficient is determined by a linear equation with that unit coefficient. Finally, these series converge on the maximal ideal of every finite extension, since an integral degree-\(d\) term has valuation tending to infinity there. The identities therefore give actual \(R\)-module laws on those ideals, compatible with Galois action. \(\square\)

**Lemma 0.8B (division fields and their exact degrees).** For \(f(X)=\pi X+X^q\), let \(\Lambda_n\) be the roots of \(f^{\circ n}\) and let \(F_{\pi,n}=F(\Lambda_n)\), \(n\geq1\). Then
\[
\Lambda_n\simeq R/\pi^nR,\qquad
\operatorname{Gal}(F_{\pi,n}/F)\simeq(R/\pi^nR)^\times,
\qquad [F_{\pi,n}:F]=(q-1)q^{n-1}=:D_n.
\tag{0LT4}
\]
The extension is totally ramified. Every primitive point is a uniformizer and generates it, and \(\pi\) is a norm from it. These assertions also hold for any \(f\in\mathcal F_\pi\), using the canonical comparison of Lemma 0.8A.

**Proof.** The iterate is monic of degree \(q^n\), reduces to \(X^{q^n}\), and has zero constant term. Every nonzero root has positive valuation: if its valuation were negative the leading term would be uniquely smallest, and if zero the leading term would be a unit while every other coefficient is in \(\pi R\). At any such argument \(x\),
\(f'(x)=\pi+q x^{q-1}\) is \(\pi\) times a unit, because \(q\in\pi R\); in characteristic \(p\) its second term is zero. The chain rule therefore shows that all roots of every iterate are distinct, including zero.

Choose \(\lambda_1\ne0\) with \(f(\lambda_1)=0\), and \(f(\lambda_n)=\lambda_{n-1}\). The primitive roots, those not killed by \(f^{\circ(n-1)}\), are precisely the roots of the monic polynomial
\[
P_n(X)=\frac{f^{\circ n}(X)}{f^{\circ(n-1)}(X)}
=\pi+\bigl(f^{\circ(n-1)}(X)\bigr)^{q-1}.
\tag{0LT5}
\]
Its degree is \(D_n\), reduction is \(X^{D_n}\), and constant term is \(\pi\). Thus it is Eisenstein. Here is the needed irreducibility argument: any monic factors over \(F\) have integral coefficients, since their roots are integral and \(R\) is integrally closed by the valuation criterion; reduction makes their constant terms divisible by \(\pi\) if both factors have positive degree. Their product would then have constant term divisible by \(\pi^2\), a contradiction. Consequently \([F(\lambda_n):F]=D_n\). In (0LT5), a positive root valuation \(r\) can cancel the constant term only when \(D_nr=1\): every intermediate term has valuation at least \(1+jr>1\). Hence the ramification index is at least \(D_n\), and the degree formula of the first lesson, Proposition 0E.1 makes it exactly \(D_n\), with residue degree one; \(\lambda_n\) is a uniformizer.

The \(q^n\) distinct roots form an \(R\)-module by Lemma 0.8A. A primitive \(\lambda_n\) generates it: its annihilator is \(\pi^nR\), for if \(a=\pi^k b\), \(k<n\), \([b]_f\) is invertible and \([\pi^k]_f(\lambda_n)\ne0\). This gives \(q^n\) distinct scalar multiples, exhausting the roots. Integral power series evaluated at \(\lambda_n\) lie in the complete field \(F(\lambda_n)\), so all roots lie there. Galois automorphisms commute with the series, by continuity and fixed coefficients; their action injects into \((R/\pi^nR)^\times\). Both its size and the field degree are \(D_n\), proving equality and (0LT4). The constant term of the minimal polynomial yields \(N(-\lambda_n)=\pi\), proving the norm assertion even when \(q=2,n=1\) and the field is \(F\). Canonical integral comparison maps evaluate in the same finite complete fields and preserve primitive points, which proves the assertion for arbitrary \(f\). \(\square\)

**Lemma 0.8C (uniformizer comparison and the explicit symbol).** Put \(F_\pi=\bigcup_n F_{\pi,n}\), and let \(F^{\mathrm{nr}}\) be the maximal unramified extension proved in the first lesson. For \(a=u\pi^m\), \(u\in R^\times\), the prescription
\[
\operatorname{Art}^{\mathrm{ar}}_{\pi}(a)|_{F^{\mathrm{nr}}}
=\operatorname{Frob}_{\mathrm{ar}}^{m},\qquad
\operatorname{Art}^{\mathrm{ar}}_{\pi}(a)(\lambda)=[u^{-1}]_f(\lambda)
\quad(\lambda\in\Lambda_n)
\tag{0LT6}
\]
defines a continuous homomorphism on \(F^{\mathrm{nr}}F_\pi/F\). This compositum and homomorphism are independent of \(\pi\). The geometric convention is its inverse. This statement constructs the symbol on these explicit fields; identifying the compositum with every abelian extension still uses the finite-reciprocity and norm argument specified below.

**Proof.** Each finite division field is totally ramified, and each finite unramified field has residue degree equal to its degree. Their intersection is \(F\); their compositum has the direct-product Galois action. Lemma 0.8B and the unramified inverse limit therefore define (0LT6), including continuity.

Let \(S\) be the valuation ring of \(\widehat{F^{\mathrm{nr}}}\), and \(\phi\) its arithmetic Frobenius. The value group remains \(\mathbf Z\), its uniformizer is \(\pi\), its residue field is \(\overline{\mathbf F}_q\), and Frobenius extends as an isometry. These assertions follow by approximating a nonzero completion element closer than its absolute value by an element of the unramified union; it then has the same valuation and residue. On \(S\), the maps \(x\mapsto\phi x-x\) and \(x\mapsto\phi x/x\) on units are onto. For the first, solve \(\bar x^q-\bar x=\bar c\) in the algebraically closed residue field and correct one \(\pi\)-adic digit at a time: adding \(\pi^j t\) changes the error digit by \(\bar t^q-\bar t\). For the second, first solve \(\bar x^{q-1}=\bar c\ne0\), then multiply by \(1+\pi^j t\), whose Frobenius ratio changes that digit by the same additive expression. Completeness gives solutions. The fixed ring is \(R\): subtract a residue representative in \(R\) from a fixed element, divide by \(\pi\), and repeat to approximate it by elements of the complete ring \(R\). Thus the respective kernels are \(R\) and \(R^\times\).

Write \(\pi'=u\pi\), choose \(\varepsilon\in S^\times\) with \(\phi\varepsilon=u\varepsilon\), and put \(g(X)=\pi'X+X^q\). We construct an integral \(\theta=\varepsilon X+O(X^2)\) satisfying
\[
g\circ\theta=(\phi\theta)\circ f.
\tag{0LT7}
\]
If \(E_d\) is its degree-\(d\) error, then \(E_d\in\pi S\): modulo \(\pi\), the two composites are \(\theta(X)^q\) and \((\phi\theta)(X^q)\). Adding \(cX^d\) changes the error by \(\pi'c-\pi^d\phi c\). For \(d\geq2\), put \(\alpha=\pi^d/\pi'\), of positive valuation. The unique correction is
\[
c=\sum_{j\geq0}\alpha^j\phi^j(-E_d/\pi'),
\tag{0LT8}
\]
which converges in \(S\). Uniqueness follows because \(c=\alpha\phi c\) forces an indefinitely increasing valuation. This same coefficient argument works for several variables with a prescribed linear form satisfying \(\pi'L=\pi\phi L\).

The two series \(\theta(F_f(X,Y))\) and \(F_g(\theta X,\theta Y)\) have linear form \(\varepsilon(X+Y)\) and satisfy the multivariable equation (0LT7); uniqueness identifies them. For the same reason, \(\theta\circ[a]_f=[a]_g\circ\theta\) for every \(a\in R\). Finally, \(\phi\theta\) and \(\theta\circ[u]_f\) both satisfy (0LT7), with linear coefficient \(u\varepsilon\); hence
\[
\phi\theta=\theta\circ[u]_f.
\tag{0LT9}
\]
The unit linear coefficient gives an integral inverse, so \(\theta\) is a formal-module isomorphism. Iterating (0LT7) gives \(g^{\circ n}\theta=(\phi^n\theta)f^{\circ n}\), so it bijects their level-\(n\) torsion.

This equality over the completion descends to the algebraic fields. Indeed, a subfield \(E\subset F^{\mathrm{sep}}\) is closed in \(F^{\mathrm{sep}}\): its fixing subgroup preserves valuation and is continuous, so it fixes every limit lying in \(F^{\mathrm{sep}}\); the fixed-field theorem of the first lesson puts that limit in \(E\). A value \(\theta(\lambda)\) is a limit in \(F^{\mathrm{nr}}F_{\pi,n}\) and is algebraic, since it is a root of \(g^{\circ n}\). Thus it belongs to that field. The inverse argument gives
\(F^{\mathrm{nr}}F_{\pi,n}=F^{\mathrm{nr}}F_{\pi',n}\).

For the symbols, (0LT6) makes \(\operatorname{Art}^{\mathrm{ar}}_\pi(\pi')\) act as Frobenius on coefficients and as \([u^{-1}]_f\) on \(\lambda\). Equations (0LT7)–(0LT9) give
\[
\operatorname{Art}^{\mathrm{ar}}_\pi(\pi')\theta(\lambda)
=(\phi\theta)([u^{-1}]_f\lambda)=\theta(\lambda).
\tag{0LT10}
\]
This agrees with \(\operatorname{Art}^{\mathrm{ar}}_{\pi'}(\pi')\), which fixes its division field and acts as Frobenius on the unramified field. The same comparison works for any other prime element in place of \(\pi'\); prime elements generate \(F^\times\), since every unit is a ratio of two prime elements. Hence the two homomorphisms agree everywhere. \(\square\)

**Theorem 0.9 (cofinality, completion and existence).** The explicit compositum of Lemma 0.8C is \(F^{\mathrm{ab}}\), and its explicit arithmetic symbol equals Theorem 0.7's reciprocity map. Consequently

\[
\widehat{F^\times}_{\mathrm{open}}
=\widehat{\mathbf Z}\times R^\times
\xrightarrow{\ \sim\ }G_F^{\mathrm{ab}}
\tag{0LT11}
\]
is a topological isomorphism. Completion here is over the open subgroups of finite index. Every such subgroup \(U\subset F^\times\) is the norm group of a unique finite abelian extension.

**Proof.** First compare the two symbols on the explicit fields. Lemma 0.8B proves that \(\pi\) is a norm from \(F_{\pi,n}\). Theorem 0.7 therefore makes \(\operatorname{rec}^{\mathrm{ar}}_F(\pi)\) fix that field at every level; on the unramified field it is arithmetic Frobenius. This is the explicit symbol of \(\pi\).

For a unit \(u\), put \(\pi'=u\pi\). Reciprocity of \(\pi'\) fixes \(F_{\pi',n}\) for the same norm reason. In the common unramified compositum in Lemma 0.8C it acts by \(\phi\) on coefficients. Its action on \(\Lambda_n\) is some scalar \([a]_f\), by Lemma 0.8B. Apply it to \(\theta(\lambda)\), a primitive \(\pi'\)-division point:

\[
\theta(\lambda)
=\operatorname{rec}^{\mathrm{ar}}_F(\pi')\theta(\lambda)
=(\phi\theta)([a]_f\lambda)
=\theta([ua]_f\lambda).
\]
The integral inverse of \(\theta\) and the annihilator of the primitive point give \(ua=1\pmod{\pi^n}\). Since reciprocity of \(\pi\) fixes \(\Lambda_n\), reciprocity of \(u=\pi'/\pi\) is \([u^{-1}]_f\) there. Units and \(\pi\) generate \(F^\times\), so the two symbols agree on every division level and unramified level.

Let \(B/F\) be any finite abelian extension. Its norm subgroup \(U_B\) is open and of finite index by Theorem 0.7 and Proposition 0.4. Thus some \(n\geq1\) gives \(1+\pi^nR\subset U_B\), and some \(m\geq1\) gives \(\pi^m\in U_B\): in the finite quotient, a positive power of \(\pi\) is identity. Set \(C=F_mF_{\pi,n}\), with \(F_m/F\) unramified of degree \(m\). The agreement of symbols just proved shows that its reciprocity kernel is exactly

\[
U_C=\pi^{m\mathbf Z}(1+\pi^nR).
\tag{0LT12}
\]
Indeed the unramified component detects valuation modulo \(m\), and the division component detects the unit modulo \(\pi^n\). Theorem 0.7 identifies this kernel with \(N_{C/F}C^\times\). It is contained in \(U_B\). The proved norm/field containment in that theorem consequently gives \(B\subset C\). Every finite abelian extension lies in the explicit compositum, proving \(F^{\mathrm{ab}}=F^{\mathrm{nr}}F_\pi\).

The same argument for any open finite-index subgroup proves that the groups (0LT12) are cofinal among them. Their quotients are
\(\mathbf Z/m\mathbf Z\times(R/\pi^nR)^\times\). Taking inverse limits gives the left side of (0LT11): a compatible system of residue units lifts uniquely to a unit by completeness of \(R\), and conversely every unit supplies such a system. Lemma 0.8B gives the division-field inverse limit \(R^\times\), while the first lesson gives the unramified inverse limit \(\widehat{\mathbf Z}\). Their disjointness at each finite level gives the right side. The symbol acts as the identity on the valuation coordinate and inverse on the scalar unit coordinate, hence is bijective and continuous. Both inverse limits are compact Hausdorff groups, so it is a homeomorphism. To justify the last topological implication, a continuous bijection from a compact space to a Hausdorff space takes closed sets to compact, hence closed, sets; its inverse is continuous.

Finally an arbitrary open finite-index \(U\) contains some \(U_C\) of (0LT12). In the finite abelian group \(\operatorname{Gal}(C/F)\), let \(H\) be the image of \(U\) and put \(M=C^H\). Finite reciprocity and its exact norm kernels give \(N_{M/F}M^\times=U\). The norm/field containment theorem gives uniqueness. This proves the existence assertion as well as cofinality, without using Hasse–Arf or abelian conductor integrality. \(\square\)

The formal-module construction and uniformizer comparison come from the actually read free Milne I§§2–3 material; their integral recurrences, division degrees and completion descent were proved in Lemmas 0.8A–0.8C. The finite invariant, exact abelian norm kernels and functoriality were proved separately in Lemmas 0.5–0.6 and Theorem 0.7. Combining them above supplies the full local prerequisite before the Weil-group quotient uses it.

## 1. The group and the reciprocity convention

Let \(F\) be a nonarchimedean local field with residue field \(k_F\) of cardinality \(q\). Its absolute Galois group has an exact sequence
\[
1\longrightarrow I_F\longrightarrow G_F\longrightarrow
\operatorname{Gal}(\bar k_F/k_F)\simeq\widehat{\mathbb Z}
\longrightarrow1.
\]
The **Weil group** \(W_F\) is the inverse image of the subgroup of integral powers of Frobenius. Give inertia its profinite topology and make it an open subgroup of \(W_F\). The quotient \(W_F/I_F\simeq\mathbb Z\) is discrete. A geometric Frobenius lift \(\Phi\) induces the inverse of \(x\mapsto x^q\) on the residue field. Write
\[
v:W_F\longrightarrow\mathbb Z,\qquad v(\Phi)=1,
\qquad \|w\|=q^{-v(w)}.
\]
The definition gives a group topology, but density by itself does not identify a profinite completion. We prove both assertions before extending any representation.

**Proposition 1.1 (topology and finite quotients).** The Weil group is the locally compact group \(I_F\rtimes\mathbb Z\), with the integer factor discrete. Its inclusion in \(G_F\) is continuous and dense, and its topology is strictly finer than the subspace topology. Every continuous homomorphism from \(W_F\) to a finite group extends uniquely and continuously to \(G_F\). Consequently the profinite completion of \(W_F\), taken over its open normal subgroups of finite index, is \(G_F\).

**Proof.** First, powers of \(\Phi\) make sense for every \(t\in\widehat{\mathbb Z}\). In a finite quotient \(G_F/U\), reduce \(t\) modulo the order of the image of \(\Phi\) and take that power. The resulting elements are compatible as \(U\) varies, so their inverse limit defines a continuous homomorphism \(t\mapsto\Phi^t\). Its residue degree is \(t\). Therefore
\[
I_F\rtimes\widehat{\mathbb Z}\longrightarrow G_F,
\qquad (i,t)\longmapsto i\Phi^t
\]
is a continuous bijection: the inverse sends \(g\) to \((g\Phi^{-v(g)},v(g))\), where the degree here has values in \(\widehat{\mathbb Z}\). Compactness of the domain and the Hausdorff property of the target make this a homeomorphism.

Restricting to integral degrees gives \(W_F=I_F\rtimes\mathbb Z\). Multiplication and inversion are continuous because conjugation by each \(\Phi^n\) is a continuous automorphism of inertia and the integer coordinate is discrete. Inertia is compact and open, so this group is locally compact. The inclusion is continuous on each open inertia coset. Density follows from density of \(\mathbb Z\) in \(\widehat{\mathbb Z}\). On the other hand, every identity neighborhood in \(G_F\) contains \(\Phi^n\) for some positive integer \(n\): take an open normal subgroup inside the neighborhood and let \(n\) be the order of \(\Phi\) in its finite quotient. This power has nonzero residue degree and is outside inertia. Thus inertia is not open in the subspace topology.

Let \(f:W_F\to Q\) be continuous, with \(Q\) finite and discrete, and put \(J=\ker(f)\cap I_F\). It is open and closed in inertia and normal in \(W_F\). It is also normal in \(G_F\): for fixed \(j\in J\), the closed set of \(g\) satisfying \(gjg^{-1}\in J\) contains the dense subgroup \(W_F\), and applying the same argument to inverses gives equality under conjugation. Hence \(H=I_F/J\) is a finite group with a continuous \(\widehat{\mathbb Z}\)-action. Some positive integer \(m\) kills that action and satisfies \(f(\Phi)^m=1\). In the splitting above, the formula
\[
\widetilde f(i\Phi^t)=f(i)\,f(\Phi)^{\,t\bmod m}
\]
is well defined and continuous. It is multiplicative: the required conjugation identity holds for integer exponents by the homomorphism property of \(f\), and holds for profinite exponents by continuity of the action on the finite group \(H\). It agrees with \(f\) on \(W_F\). Two continuous extensions agree on a dense subgroup and therefore everywhere.

Every finite continuous quotient of \(G_F\) restricts to a surjective quotient of \(W_F\), by density. Conversely the construction just made extends every finite continuous quotient of \(W_F\) and preserves its image. These constructions are compatible with quotient maps and inverse to one another. Taking their inverse limits proves the completion assertion. \(\square\)

**Proposition 1.2 (finite extensions).** For a finite separable extension \(E/F\) of residue degree \(f\), an embedding in the chosen separable closure identifies \(W_E\) with \(G_E\cap W_F\). This subgroup is open in \(W_F\), has index \([E:F]\), and satisfies \(v_F|_{W_E}=f v_E\).

**Proof.** The action on the algebraic residue field identifies the image of \(G_E\) inside \(G_F/I_F\) with \(f\widehat{\mathbb Z}\): an arithmetic Frobenius for the residue field of \(E\) is the \(f\)-th power of one for \(F\), and the same statement holds for their inverses. If an integer \(n\) lies in \(f\widehat{\mathbb Z}\), its reduction modulo \(f\) is zero, so \(n\in f\mathbb Z\). Thus membership in \(G_E\cap W_F\) is exactly the Weil condition for \(E\), and the degree formula follows. The intersection is open since \(G_E\) is open in \(G_F\). Density of \(W_F\) makes its action transitive on the finite coset set \(G_F/G_E\), and its stabilizer is precisely that intersection. Its index is therefore \([G_F:G_E]=[E:F]\). The inertia topology and the discrete degree topology agree with the Weil topology defined over \(E\). \(\square\)

The local reciprocity input is now proved here. Theorem 0.9 identifies the open finite-index completion
\[
\widehat{F^\times}_{\mathrm{open}}
=\widehat{\mathbf Z}\times\mathcal O_F^\times
\simeq G_F^{\mathrm{ab}},
\]
with arithmetic normalization. Theorem 0.7 proves its norm, conjugation and transfer identities for every finite separable extension. The additional passage from Galois reciprocity to Weil reciprocity is proved next.

**Theorem 1.3 (geometric Weil reciprocity).** Inverting arithmetic reciprocity induces a topological isomorphism
\[
\operatorname{Art}_F:F^\times\overset\sim\longrightarrow W_F^{\mathrm{ab}}.
\]
Here \(W_F^{\mathrm{ab}}=W_F/\overline{[W_F,W_F]}\) is the maximal Hausdorff abelian quotient. Units map onto the image of inertia and \(v(\operatorname{Art}_F(x))=v_F(x)\), where \(v\) uses geometric Frobenius. Consequently \(\|\operatorname{Art}_F(x)\|=|x|_F\).

**Proof.** Put \(D=\overline{[G_F,G_F]}\), with closure in \(G_F\). Since the degree quotient is abelian, \(D\subset I_F\). Every commutator of elements of \(G_F\) is a limit of commutators of elements of the dense subgroup \(W_F\), by continuity of multiplication and inversion. The same holds for finite products of commutators. Hence the closure of \([W_F,W_F]\) in \(G_F\) is \(D\). All these commutators lie in inertia, whose topology agrees in both groups; the closure in \(W_F\) is therefore also \(D\).

The quotient \(W_F/D\) embeds in \(G_F/D=G_F^{\mathrm{ab}}\) as the inverse image of integral degrees. Under the earlier completion theorem, that subgroup is exactly the image of \(F^\times=\varpi^{\mathbb Z}\mathcal O_F^\times\). Inverting arithmetic reciprocity makes a positive valuation have geometric degree \(+1\). This proves the asserted group isomorphism and its unit and degree assertions.

For topology, the image \(I_F/D\) is compact and open in \(W_F/D\). Its reciprocity map from the compact group \(\mathcal O_F^\times\) is a continuous bijection onto a Hausdorff group, hence a homeomorphism. Both \(F^\times\) and \(W_F/D\) are disjoint unions of open translates of these unit subgroups, indexed by the integers. Translation transports that homeomorphism to each coset, proving continuity of the isomorphism and its inverse everywhere. \(\square\)

Fix a uniformizer \(\varpi\). We henceforth choose the geometric lift \(\Phi\) to represent \(\operatorname{Art}_F(\varpi)\) in \(W_F^{\mathrm{ab}}\). This class does have degree one, so such a lift exists. An arbitrary degree-one lift need not represent the same abelian class: changing a lift by inertia can change that class. Propositions 1.1–1.2 hold for every lift; this choice makes
\[
\operatorname{Art}_F(\varpi)=\Phi\quad\text{modulo closed commutators}
\]
valid whenever we evaluate ramified characters. A source using arithmetic reciprocity uses the inverse map: its multiplicative character corresponding to a fixed Weil character is the inverse of ours. In the earlier Galois lessons, arithmetic Frobenius is the inverse of geometric Frobenius, up to inertia. We will keep that distinction visible in local Euler factors.

For a finite separable extension \(E/F\), Proposition 1.2 supplies the subgroup and degree normalization used in induction. The local reciprocity functoriality that we use is
\[
\begin{array}{ccc}
F^\times&\hookrightarrow&E^\times\\
\operatorname{Art}_F\downarrow&&\downarrow\operatorname{Art}_E\\
W_F^{\mathrm{ab}}&\xrightarrow{\operatorname{Ver}_{E/F}}&W_E^{\mathrm{ab}},
\end{array}
\tag{1}
\]
where the bottom arrow is transfer. Inclusion of Weil groups corresponds instead to the norm \(E^\times\to F^\times\). These are different functorialities.

For completeness, these compatibilities pass from the earlier finite reciprocity symbols to the displayed Weil maps as follows. Form inverse limits over finite Galois extensions containing \(E\). The norm identity identifies inclusion \(G_E\to G_F\) on abelianizations with the field norm; the transfer identity identifies inclusion \(F^\times\to E^\times\) with group transfer. The coset formula for transfer is unchanged on the dense Weil subgroups: Proposition 1.2 identifies their finite coset sets, and each factor \(h_i(g)\) in that formula is the same element before passing to the Galois completion. Finally \(W_E^{\mathrm{ab}}\) injects into \(G_E^{\mathrm{ab}}\) by the proof of Theorem 1.3, so equality after completion is already equality in the Weil abelianization. This proves (1) and the norm assertion for Weil groups. Inversion to geometric reciprocity preserves both diagrams, since norm and transfer are homomorphisms between abelian groups.

The free texts [Deligne 1973, §§2.2–2.3] and [Getz–Hahn, §12.1] provide comparison conventions. The topology and extension proofs are Propositions 1.1–1.2, the Weil reciprocity proof is Theorem 1.3, and finite reciprocity and its completion are proved above in Theorems 0.7 and 0.9.

## 2. Finite inertia and finite image after a twist

**Lemma 2.1.** A smooth finite-dimensional representation \(\rho\) of \(W_F\) is trivial on an open subgroup of \(I_F\). Consequently \(H=\rho(I_F)\) is finite.

**Proof.** Choose a basis \(e_1,\ldots,e_d\). The intersection of their stabilizers is open and fixes every vector. Its intersection with \(I_F\) lies in the kernel. An open subgroup of a compact group has finite index, so the image of inertia is finite. Conversely an action trivial on an open subgroup of inertia is smooth, since that subgroup is also open in \(W_F\). \(\square\)

Let \(T=\rho(\Phi)\). Conjugation by \(T\) gives an automorphism of the finite group \(H\), so for some positive integer \(m\),
\[
T^m h=hT^m\qquad(h\in H).
\tag{2}
\]
It also commutes with \(T\), hence with the entire image of \(W_F\).

**Theorem 2.2 (finite image after an unramified twist).** Every irreducible smooth complex representation of \(W_F\) is an unramified twist of a finite-image representation. The latter extends continuously to a finite-image representation of \(G_F\).

**Proof.** Here is the scalar argument, including the needed form of Schur's lemma. An operator \(A\) commuting with an irreducible complex representation has an eigenvalue \(a\). Its nonzero eigenspace \(\ker(A-a)\) is invariant, hence is the whole representation. Thus \(A=a\,1\). Applying this to the invertible operator \(T^m\) in (2) gives \(T^m=a\,1\), with \(a\in\mathbb C^\times\). Choose \(c\in\mathbb C^\times\) with \(c^m=a^{-1}\), and define the unramified character \(\eta_c(w)=c^{v(w)}\). For \(\rho'=\rho\otimes\eta_c\), inertia still has image \(H\), and \(\rho'(\Phi)=cT\) has order dividing \(m\). The image consists of the elements \(h(cT)^j\), with \(h\in H\) and \(0\le j<m\), so it is finite.

The kernel of \(\rho'\) is open and has finite index in \(W_F\). Proposition 1.1 therefore extends this finite quotient to \(G_F\). This extension is unique because \(W_F\) is dense in \(G_F\). Finally \(\rho=\rho'\otimes\eta_c^{-1}\). \(\square\)

Every unramified character is \(\eta_c\) for some \(c\ne0\), since it factors through the infinite cyclic quotient. It can also be written \(\|\cdot\|^s\): choose \(s\in\mathbb C\) with \(q^{-s}=c\), and define \(q^{-sv}=\exp(-sv\log q)\). Different choices of \(s\) differing by \(2\pi i/\log q\) give the same character. Such a character need not have finite image or extend to \(G_F\) with the usual complex topology. For example \(\|\Phi\|=q^{-1}\) has infinite image, whereas a continuous complex representation of the profinite group \(G_F\) has finite image by the first lesson.

The theorem is stated over \(\mathbb C\) so that Schur's lemma gives a scalar and the required root exists. For an absolutely irreducible representation over an \(\ell\)-adic coefficient field, the same argument works after a finite coefficient extension containing the root. An irreducible representation over a non-algebraically closed field need not be absolutely irreducible; that qualification must be checked before using the scalar argument.

## 3. The semisimplicity criterion

**Theorem 3.1.** A smooth complex representation \(\rho\) of \(W_F\) is semisimple if and only if \(\rho(\Phi)\) is a semisimple linear operator. This condition holds for one geometric Frobenius lift if and only if it holds for every such lift.

**Proof.** If \(\rho\) is semisimple, it is a direct sum of irreducibles. Theorem 2.2 expresses each summand as a finite-image representation times a scalar unramified character. A finite-order complex matrix is diagonalizable because its minimal polynomial divides \(X^n-1\), which has distinct roots in characteristic zero. Thus Frobenius is semisimple on every summand.

Conversely suppose \(T\) is semisimple. Choose \(m\) as in (2). The eigenspace decomposition
\[
V=\bigoplus_a V_a,\qquad V_a=\ker(T^m-a)
\]
is preserved by \(H\) and \(T\), hence by \(W_F\). Each \(a\ne0\). On \(V_a\), twist by \(\eta_c\) with \(c^m=a^{-1}\). The resulting representation has finite image by the same finite-set calculation as in Theorem 2.2. Maschke's averaging argument makes it semisimple: if \(U\) is invariant, average any projection \(V_a\to U\) over the finite image to obtain an equivariant projection. Twisting back preserves invariant direct summands. Therefore every \(V_a\), and hence \(V\), is semisimple.

The proof applies to any Frobenius lift: each has degree one and normalizes the same finite inertia image. Once one lift is semisimple, the representation is semisimple, so the first implication makes every lift semisimple. \(\square\)

**Example 3.2.** The action
\[
\rho(w)=\begin{pmatrix}1&v(w)\\0&1\end{pmatrix}
\]
is smooth and unramified. Its Frobenius matrix is a nonidentity unipotent matrix, so the representation is not semisimple. More explicitly, \(\mathbb Ce_1\) is invariant, but any complementary line spanned by \(ae_1+e_2\) is moved to the line spanned by \((a+1)e_1+e_2\). There is no invariant complement. Its trace is constantly two; semisimplification loses this extension.

## 4. Induction and its determinant

For an open subgroup \(J\subset W\) of finite index and a representation \(U\) of \(J\), one model of induction is
\[
\operatorname{Ind}_J^W U=\mathbb C[W]\otimes_{\mathbb C[J]}U.
\]
Choose representatives \(x_1,\ldots,x_n\) for the left cosets \(W/J\). This is the direct sum of the spaces \(x_i\otimes U\). Its dimension is \(n\dim U\); finite index removes any issue of compact support. When \(U\) is smooth, the induced representation is smooth: finitely many conjugates of open stabilizers give an open subgroup fixing any specified vector.

Frobenius reciprocity follows directly from the tensor description. A \(W\)-linear map out of induction is determined by \(u\mapsto A(1\otimes u)\), which must be \(J\)-linear; a \(J\)-linear map \(b:U\to V|_J\) extends by \(x\otimes u\mapsto xb(u)\). These constructions are inverse.

For two finite-index subgroups \(J,K\), splitting the tensor model by the double cosets \(K\backslash W/J\) gives Mackey's formula
\[
\operatorname{Res}_K^W\operatorname{Ind}_J^W U
\simeq\bigoplus_{x\in K\backslash W/J}
\operatorname{Ind}_{K\cap xJx^{-1}}^K U^x,
\tag{3}
\]
where \(h\in K\cap xJx^{-1}\) acts on \(U^x\) as \(x^{-1}hx\). To see the isomorphism on one summand, send \(k\otimes u\) to \(kx\otimes u\). The tensor relation is respected precisely because of that action. Distinct double cosets give disjoint sets of left-coset summands, so the resulting sum is bijective. Thus the familiar finite-group formulas apply here without a finiteness assumption on \(W\).

**Theorem 4.1 (determinant and transfer).** For \(E/F\) finite separable and \(U\) a smooth representation of \(W_E\) of dimension \(d\),
\[
\det\operatorname{Ind}_{W_E}^{W_F}U
=\left(\det\operatorname{Ind}_{W_E}^{W_F}1\right)^d
\left(\det U\circ\operatorname{Ver}_{E/F}\right).
\tag{4}
\]
For \(E/F\) quadratic and a character \(\chi:E^\times\to\mathbb C^\times\), identified with a Weil character by geometric reciprocity,
\[
\det\operatorname{Ind}_{W_E}^{W_F}\chi
=\omega_{E/F}\,\chi|_{F^\times}.
\tag{5}
\]

**Proof.** For \(g\in W_F\), write
\[
gx_i=x_{\sigma_g(i)}h_i(g),\qquad h_i(g)\in W_E.
\]
On the induced space, \(g\) permutes \(n\) blocks of dimension \(d\), and its map on block \(i\) is \(U(h_i(g))\). Permuting such blocks has determinant \(\operatorname{sgn}(\sigma_g)^d\): a transposition exchanges \(d\) pairs of basis vectors and has sign \((-1)^d\). Hence
\[
\det(g\mid\operatorname{Ind}U)
=\operatorname{sgn}(\sigma_g)^d\prod_i\det U(h_i(g)).
\tag{6}
\]
The transfer is the class of \(\prod_i h_i(g)\) in \(W_E^{\mathrm{ab}}\). For completeness, the identity
\[
h_i(gg')=h_{\sigma_{g'}(i)}(g)h_i(g')
\]
shows that this product is a homomorphism after abelianizing. Replacing representatives by \(x_i a_i\) changes the factors to \(a_{\sigma_g(i)}^{-1}h_i(g)a_i\); the \(a_i\)'s cancel in the abelianized product. Thus transfer is independent of the representatives. Any character of \(W_E\), including \(\det U\), evaluates that product as the product in (6). The permutation sign is \(\det\operatorname{Ind}1\). This proves (4).

In degree two the permutation sign is the nontrivial character of \(W_F/W_E\), namely \(\omega_{E/F}\). By (1), transfer corresponds to the inclusion \(F^\times\hookrightarrow E^\times\), which gives (5). \(\square\)

**Example 4.2 (unramified quadratic induction).** Suppose \(E/F\) is unramified quadratic. Take \(\Phi_E=\Phi_F^2\) and an unramified character with \(\chi(\Phi_E)=a\). On the coset basis \(1\otimes1,\Phi_F\otimes1\),
\[
\operatorname{Ind}\chi(\Phi_F)=
\begin{pmatrix}0&a\\1&0\end{pmatrix},
\qquad \det(X-\operatorname{Ind}\chi(\Phi_F))=X^2-a.
\]
The determinant is \(-a\). Formula (5) gives the same answer: \(\omega_{E/F}(\varpi_F)=-1\), while \(\varpi_F\) is also a uniformizer of \(E\), so \(\chi(\varpi_F)=a\). The representation splits into the two unramified characters whose Frobenius values are the roots \(\pm\sqrt a\). Induction from a quadratic extension is therefore not automatically irreducible.

More generally Mackey's formula gives \(\operatorname{Res}_{W_E}\operatorname{Ind}\chi=\chi\oplus\chi^\sigma\), where \(\sigma\) is the nontrivial automorphism. If \(\chi\ne\chi^\sigma\), these distinct character spaces are exchanged by an element outside \(W_E\), and any invariant subspace is a sum of character spaces; no single one is stable. Thus the induction is irreducible. If the characters agree, the outside operator has scalar nonzero square and diagonalizes, yielding two invariant lines. This also computes the quadratic irreducibility criterion.

## 5. The real Weil group

The archimedean Weil groups are
\[
W_{\mathbb C}=\mathbb C^\times,\qquad
W_{\mathbb R}=\mathbb C^\times\sqcup j\mathbb C^\times,
\qquad j^2=-1,\quad jzj^{-1}=\bar z.
\tag{7}
\]
Here \(-1\) on the right is in \(\mathbb C^\times\). The abelianization is \(\mathbb R^\times\), with \(z\mapsto |z|^2\) and \(j\mapsto-1\). Indeed the commutators \(\bar z/z\) exhaust the unit circle; quotienting by them makes \(j^2=1\), leaving a positive real factor and an order-two sign.

Every continuous character of \(\mathbb C^\times\) has the form
\[
\omega_{a,n}(re^{i\theta})=r^a e^{in\theta},
\qquad a\in\mathbb C,\quad n\in\mathbb Z,
\tag{8}
\]
where \(r^a=\exp(a\log r)\). One proof separates \(\mathbb C^\times=\mathbb R_{>0}\times S^1\). A continuous character of the first factor lifts along the exponential map to an additive function of \(\log r\), hence is \(r^a\). A character of the circle lifts to \(e^{ib\theta}\); periodicity and its compact image force \(b\in\mathbb Z\). Define \(\omega^\sigma(z)=\omega(\bar z)\). This conjugates the argument, not the value or the coefficient \(a\): \(\omega_{a,n}^\sigma=\omega_{a,-n}\).

**Theorem 5.1 (complete real classification).** The irreducible continuous finite-dimensional complex representations of \(W_{\mathbb R}\) are:

1. The characters corresponding to \(x\mapsto\operatorname{sgn}(x)^\epsilon|x|^t\) on \(\mathbb R^\times\), for \(\epsilon\in\{0,1\}\) and \(t\in\mathbb C\).
2. The two-dimensional representations \(\operatorname{Ind}_{\mathbb C^\times}^{W_{\mathbb R}}\omega_{a,n}\), for \(a\in\mathbb C\) and \(n\in\mathbb Z\setminus\{0\}\).

Two representations in the second list are isomorphic exactly when their characters are equal or exchanged by \(\sigma\); equivalently their parameters are \((a,n)\) and \((a,\pm n)\).

**Proof.** Let \(V\) be irreducible. A commuting family of complex matrices has a common eigenvector: take an eigenspace of one nonscalar member, which is preserved by every member, and repeat on that smaller space. If every member is scalar, any vector works. Apply this to the action of \(\mathbb C^\times\), obtaining \(v\ne0\) with \(zv=\omega(z)v\). The eigenvalue \(\omega(z)\) is multiplicative, and is continuous by the continuity of the action and any linear functional taking \(v\) to one. Thus \(\omega\) has form (8).

The vector \(jv\) has character \(\omega^\sigma\), because \(zj=j\bar z\). The span of \(v,jv\) is stable under \(\mathbb C^\times\) and \(j\), since \(j(jv)=\omega(-1)v\). Irreducibility makes it all of \(V\), so \(\dim V\le2\).

If \(\omega=\omega^\sigma\), then \(n=0\), and \(\mathbb C^\times\) acts by scalars on this span. The operator \(j\) has square \(\omega(-1)=1\), so it has an eigenline stable under the whole group. Irreducibility forces dimension one; \(j\) acts by \((-1)^\epsilon\). Since \(\omega_{a,0}(z)=|z|^a\), its character on \(\mathbb R^\times\) is \(\operatorname{sgn}(x)^\epsilon|x|^{a/2}\). This gives list 1.

If \(\omega\ne\omega^\sigma\), the two vectors are independent. In their basis the action is
\[
z\longmapsto\begin{pmatrix}\omega(z)&0\\0&\omega(\bar z)\end{pmatrix},
\qquad j\longmapsto\begin{pmatrix}0&(-1)^n\\1&0\end{pmatrix}.
\tag{9}
\]
These matrices satisfy (7). Their only possible invariant lines under \(\mathbb C^\times\) are the two coordinate lines, which \(j\) exchanges. Hence they form an irreducible representation, and the usual coset model identifies it with the induction in list 2.

An isomorphism restricts to an isomorphism of \(\mathbb C^\times\)-representations, so the unordered pairs \(\{\omega,\omega^\sigma\}\) must coincide. Conversely replacing \(\omega\) by \(\omega^\sigma\) just exchanges the two character lines, giving an isomorphism. This proves the criterion. \(\square\)

One often writes (8) as \(z^p\bar z^q\), with \(p-q=n\in\mathbb Z\) and \(p+q=a\). For arbitrary complex \(p,q\), the individual powers can be multivalued; the notation means the single-valued polar expression \(r^{p+q}e^{i(p-q)\theta}\). The condition for induction to be irreducible is \(p\ne q\). The parameters need not be integers: integrality is an additional algebraicity condition, not part of the continuous classification.

### 5A. Constructing the discrete series and its parameter

The weight shift in the next example requires a proof on the real representation side. We give it for every integer \(k\ge2\), including the endpoint \(k=2\). Here a discrete series is an irreducible unitary representation occurring as a closed subrepresentation of the regular \(L^2\)-representation, with the centre removed when it acts by a unitary character.

**Proposition 5.2 (the lowest-weight construction).** There is a unitary discrete series \(D_k\) of \(\mathrm{GL}_2(\mathbb R)\), trivial on positive scalar matrices, whose rotation weights are
\[
 k,k+2,k+4,\ldots\quad\text{and}\quad-k,-k-2,-k-4,\ldots,
\]
each with multiplicity one. Its central character is \(\operatorname{sgn}^k\). Its normalized infinitesimal parameters are \(\{(k-1)/2,-(k-1)/2\}\). The lowest-weight module on either connected component is uniquely determined by that lowest weight.

**Proof.** Put \(\mathbb D=\{z:|z|<1\}\), and let \(\mathcal H_k\) be the holomorphic functions with norm
\[
 \|f\|_k^2=\frac{k-1}{\pi}\int_{\mathbb D}|f(z)|^2(1-|z|^2)^{k-2}\,dA(z).
 \tag{9A}
\]
For \(f(z)=\sum a_nz^n\), angular orthogonality on each smaller circle, followed by monotone convergence of the sum of nonnegative terms, gives
\[
 \|f\|_k^2=\sum_{n\ge0}|a_n|^2 b_n,
 \qquad b_n=(k-1)\int_0^1t^n(1-t)^{k-2}\,dt
       =\frac{n!(k-1)!}{(n+k-1)!}.
 \tag{9B}
\]
The integral formula follows by repeated integration by parts, with the last integral \(\int_0^1t^n\,dt=1/(n+1)\); it holds for \(k=2\) as well. Conversely a sequence with finite weighted square sum defines a holomorphic function: Cauchy–Schwarz bounds its series uniformly on each disk \(|z|\le r<1\), since \(b_n^{-1}\) grows polynomially. Thus (9B) identifies \(\mathcal H_k\) with a complete weighted sequence space, and polynomials are dense. Differentiating the geometric series \(k-1\) times gives
\[
 K_w(z)=(1-\bar wz)^{-k}=\sum_{n\ge0} b_n^{-1}\bar w^{,n}z^n.
\]
With inner product linear in its first argument, (9B) proves \(\langle f,K_w\rangle=f(w)\), including boundedness of evaluation.

Write
\[
 g=\begin{pmatrix}\alpha&\beta\\\bar\beta&\bar\alpha\end{pmatrix}
 \in\mathrm{SU}(1,1),\qquad |\alpha|^2-|\beta|^2=1.
\]
Define
\[
 (\pi_k(g)f)(z)=(\alpha-\bar\beta z)^{-k}
 f\left(\frac{\bar\alpha z-\beta}{\alpha-\bar\beta z}\right).
 \tag{9C}
\]
The denominator has no zero in the disk, because \(|\alpha|>|\beta|\); integer \(k\) makes the expression single-valued. Matrix multiplication gives the multiplicative denominator identity for successive fractional transformations. Since the argument is \(g^{-1}z\), that identity proves \(\pi_k(g)\pi_k(h)=\pi_k(gh)\).

For \(u=g^{-1}z\), direct expansion and differentiation give
\[
 1-|u|^2=\frac{1-|z|^2}{|\alpha-\bar\beta z|^2},\qquad
 dA(u)=|\alpha-\bar\beta z|^{-4}dA(z).
\]
Substitution in (9A) proves unitarity. The action is strongly continuous: for polynomials and \(g\) near the identity the denominator is bounded away from zero on the whole closed disk, so dominated convergence applies in (9A); density and unitarity extend continuity to all vectors.

The compact subgroup \(h_\theta=\operatorname{diag}(e^{i\theta},e^{-i\theta})\) acts on \(z^n\) by \(e^{-i(k+2n)\theta}\). Differentiating (9C) on the two one-parameter subgroups with \(\beta=\sinh t\) and \(\beta=i\sinh t\), respectively, gives
\[
 E+F,\qquad-i(E-F),\qquad
 E=z^2\partial_z+kz,\quad F=-\partial_z.
\]
These derivatives exist in the Hilbert norm on every polynomial, by the same bounded-denominator argument. If a nonzero closed invariant subspace contains a function with a nonzero \(n\)-th Taylor coefficient, averaging its rotations against the corresponding character puts \(z^n\) in that subspace. Applying the two derivatives and their complex linear combinations then puts
\(Fz^n=-nz^{n-1}\) and \(Ez^n=(n+k)z^{n+1}\) in it. Repeated application reaches every monomial. Their density proves irreducibility and also the asserted multiplicity-one weights on this component.

We prove that this representation actually occurs discretely. Every \(g\) is uniquely
\[
 g=g_wh_\theta,\qquad
 g_w=(1-|w|^2)^{-1/2}
       \begin{pmatrix}1&w\\\bar w&1\end{pmatrix},
 \qquad w=\beta/\bar\alpha.
\]
The measure \(dA(w)/(1-|w|^2)^2\) is invariant under the disk action, by the two change-of-variable identities above. Consequently
\(dg=dA(w)/(1-|w|^2)^2\,d\theta/(2\pi)\) is a left Haar measure: left multiplication changes \(w\) by that disk action and changes the compact fibre coordinate by a rotation depending on \(w\), which preserves its angular measure. Formula (9C) gives
\[
 \pi_k(g)1=\alpha^{-k}K_w,
 \qquad |\langle f,\pi_k(g)1\rangle|^2
       =(1-|w|^2)^k|f(w)|^2.
\]
It follows exactly, for every \(f\in\mathcal H_k\), that
\[
 \int_{\mathrm{SU}(1,1)}|\langle f,\pi_k(g)1\rangle|^2\,dg
 =\frac{\pi}{k-1}\|f\|_k^2.
 \tag{9D}
\]
The coefficient map \(f\mapsto\langle f,\pi_k(g)1\rangle\) intertwines \(\pi_k\) with left translation, since unitarity gives
\(\langle\pi_k(h)f,\pi_k(g)1\rangle=
\langle f,\pi_k(h^{-1}g)1\rangle\).
Equation (9D) makes its image closed and its kernel zero. This supplies the discrete occurrence, including \(k=2\), without an imported orthogonality or globalization theorem.

To pass to the full real group, the Cayley matrix
\(C=2^{-1/2}\begin{pmatrix}1&i\\1&-i\end{pmatrix}\)
conjugates \(\mathrm{SL}_2(\mathbb R)\) to \(\mathrm{SU}(1,1)\). This is checked by multiplying the matrices; it takes a real rotation to \(h_\theta\). Let \(j_0=\operatorname{diag}(1,-1)\). On \(\mathcal H_k\oplus\mathcal H_k\), define the action of \(h\in\mathrm{SL}_2(\mathbb R)\) by
\[
 \pi_k(ChC^{-1})\oplus\pi_k(Cj_0hj_0C^{-1}),
\]
let \(j_0\) exchange the summands, and let positive scalars act trivially. Every positive-determinant matrix is uniquely a positive scalar times an element of \(\mathrm{SL}_2(\mathbb R)\), and a negative-determinant matrix becomes such a matrix after multiplication by \(j_0\). The identities \(j_0^2=1\) and its displayed conjugation verify that these rules define a representation of \(\mathrm{GL}_2(\mathbb R)\). Its two rotation spectra are the two lists in the statement. Rotation projections, the ladder operators, and the interchange of summands prove full irreducibility. The two coefficient embeddings (9D), on the two components of the group modulo positive scalars, give a closed regular-representation embedding of the direct sum with this action. Quotienting also by the finite central subgroup \(\{\pm1\}\), with central character retained, proves the required discrete occurrence modulo the full centre. Finally \(-1=h_\pi\) acts by \((-1)^k\); hence the central character is \(\operatorname{sgn}^k\).

Here is the weight and infinitesimal calculation, with its uniqueness argument. Put \(H=k+2z\partial_z\). The polynomial operators satisfy
\[
 [H,E]=2E,\quad[H,F]=-2F,\quad[E,F]=H.
\]
Thus the operator \(\Omega=H^2-2H+4EF\) commutes with all three, by expanding these commutators. On the vector 1, \(F1=0\) and \(H1=k\), so \(\Omega=k(k-2)\) on every monomial generated by \(E\). More generally, in any lowest-weight module with vector \(v\), \(Hv=kv\), \(Fv=0\), induction using \([F,E]=-H\) gives
\[
 H E^nv=(k+2n)E^nv,\qquad
 F E^nv=-n(k+n-1)E^{n-1}v.
 \tag{9E}
\]
No \(E^nv\) vanishes: applying \(F\) would contradict the preceding nonzero vector. Any word in \(H,E,F\) can be reordered, using the three commutators, into a sum of words \(E^aH^bF^c\): interchange an inverted adjacent pair, and the commutator term has shorter length, giving induction first on length and then on inversions. Therefore the module generated by \(v\) is exactly the span of \(E^nv\). Equations (9E) determine it uniquely. For a unitary realization, \(E^*=-F\); this follows either from differentiating the two real unitary one-parameter groups above or from (9B). Hence
\(\|E^nv\|^2=n(k+n-1)\|E^{n-1}v\|^2\), fixing its Hilbert completion up to the norm of \(v\). Its finite-weight vectors are analytic for these real generators: their iterated norms are bounded by \(A^r(n+r)!/n!\) for a fixed \(A\), so their exponential series converge for small \(|t|\). The ladder intertwiner consequently intertwines those local one-parameter groups, and then the connected group they generate. This also proves uniqueness of the unitary lowest-weight realization.

For the rank-one Lie algebra we normalize an infinitesimal parameter \(\lambda\), modulo sign, by \(\Omega=4\lambda^2-1\). This fixes the usual half-root shift explicitly. The value just computed is
\(k(k-2)=(k-1)^2-1\); taking the positive parameter gives \(\lambda=(k-1)/2\). Positive scalars act trivially, so the two \(\mathfrak{gl}_2\) parameters have sum zero and are \(\{\lambda,-\lambda\}\). This proves every assertion. \(\square\)

The disk action (9C) can be compared with [Gazeau–del Olmo–Pejhan, §II, equations (7)–(9)] at \(2\eta=k\); its construction, unitarity and discrete occurrence have been proved above. The normalized real dictionary is recorded in [Kaletha–Horawa, §7, pp.78–80]. Those free sources fix the conventions; neither supplies a missing proof in the preceding argument.

**Example 5.3 (the discrete-series parameter, with the shift proved).** For the family just constructed, the normalized real correspondence sends
\[
 D_k\longleftrightarrow\operatorname{Ind}_{\mathbb C^\times}^{W_{\mathbb R}}
 \omega_{0,k-1},\qquad k\ge2.
 \tag{9F}
\]
We verify this instance of the dictionary explicitly. An irreducible real Weil representation has form \(\operatorname{Ind}\omega_{a,n}\), by Theorem 5.1, with unordered complex exponents \(\{(a+n)/2,(a-n)/2\}\). These are the normalized infinitesimal data on the Weil side. Its determinant has real character \(|x|^a\operatorname{sgn}(x)^{n+1}\), as follows immediately from (9). Matching the trivial positive central character forces \(a=0\), since \(r^a=1\) for every positive \(r\) only when \(a=0\). Matching the infinitesimal data computed in Proposition 5.2 then forces \(|n|=k-1\). The two choices of sign are isomorphic by Theorem 5.1. Conversely every \(n\ge1\) gives the constructed discrete series \(D_{n+1}\); its lowest-weight uniqueness and the Weil isomorphism criterion prove that this is a bijection on these families. This is the explicit normalized correspondence used in the example, with its existence and uniqueness verified on both sides.

Restriction to \(\mathbb C^\times\) therefore has characters \((z/|z|)^{k-1}\) and its inverse. Formula (9) gives \(j^2=(-1)^{k-1}\), \(\det(j)=(-1)^k\), and determinant \(\operatorname{sgn}^k\), agreeing with the calculated central character. Twisting \(D_k\) by \(|\det|^t\) adds \(t\) to each infinitesimal exponent and changes the positive central character to \(|x|^{2t}\); the same calculation gives \(\operatorname{Ind}\omega_{2t,k-1}\). Thus a cohomological normalization may include this explicitly specified radial twist.

For general \(\omega_{a,n}\), the determinant of (9) on \(z\) is \(|z|^{2a}\), and on \(j\) it is \((-1)^{n+1}\). Thus its real character is \(|x|^a\operatorname{sgn}(x)^{n+1}\), consistent with the transfer formula.

## 6. The global group and its characters

For a number field \(K\), write \(C_K=\mathbb A_K^\times/K^\times\), with its quotient topology. The required global construction has an actual earlier programme proof: *Class field theory*, *Brauer groups, fundamental classes, and class field towers*, Theorem 24.6 and §7, “Relative Weil groups and their transition maps.” Theorem 24.6 proves the global class-formation hypotheses; §7 proves the relative extensions, their tower quotients, the topology of the absolute group, and local-to-global compatibility. We specify those inputs because a free account stating existence would not supply this proof.

Here is precisely the resulting earlier theorem, in the geometric convention used in this lesson. There is a locally compact group \(W_K\) with a continuous dense map to \(G_K\) and an open quotient map
\[
p_K:W_K\longrightarrow C_K,
\qquad\ker p_K=\overline{[W_K,W_K]}.
\]
For each place \(v\), the construction supplies a continuous map \(W_{K_v}\to W_K\), after compatible choices of places in finite extensions. On Hausdorff abelianizations it is the single-place idèle map \(K_v^\times\to C_K\), and the maps to Galois groups commute. Changes of compatible choices give the corresponding conjugacy ambiguity. If the earlier construction is written with arithmetic reciprocity, compose every multiplicative abelianization map with inversion to obtain these geometric maps.

The proof in the specified earlier §7 proceeds through relative groups
\[
1\longrightarrow C_L\longrightarrow W_{L/K}
\longrightarrow\operatorname{Gal}(L/K)\longrightarrow1
\]
defined by the fundamental class. Its transfer calculation proves \(W_{L/K}^{\mathrm{ab}}\simeq C_K\). For a tower \(M/L/K\), quotienting by the closed commutators in the inverse image of \(\operatorname{Gal}(M/L)\) gives \(W_{L/K}\); the transition restricts to the norm \(C_M\to C_L\) and has compact kernel. Compatible inverse limits are therefore locally compact with surjective projections. The same §7 proves that their map to \(C_K\) is open and that its kernel is exactly the closure of commutators, by lifting finite-level products of commutators. Finally its local fundamental-class and double-coset transfer calculations prove the single-place diagram. These are the earlier proved steps being used here, including the topological assertions needed for continuous characters.

**Proposition 6.1 (global one-dimensional representations).** Composition with \(p_K\) is a bijection from continuous idele-class characters \(C_K\to\mathbb C^\times\) to continuous one-dimensional complex representations of \(W_K\). Under this bijection, restriction at \(v\) corresponds to restricting the idele-class character along \(K_v^\times\to C_K\).

**Proof.** A one-dimensional representation is a homomorphism \(\rho:W_K\to\mathbb C^\times\). Since the target is abelian, it kills every commutator. Since the target is Hausdorff and \(\rho\) is continuous, its kernel is closed; it therefore kills their closure. The earlier theorem identifies that closure with \(\ker p_K\). There is consequently a unique homomorphism \(\chi:C_K\to\mathbb C^\times\) with \(\rho=\chi\circ p_K\), because \(p_K\) is surjective.

This homomorphism is continuous, not merely algebraically defined. For every open subset \(U\subset\mathbb C^\times\),
\[
\chi^{-1}(U)=p_K\bigl(\rho^{-1}(U)\bigr).
\]
The right side is open because \(p_K\) is an open quotient map. Conversely a continuous character composed with the continuous map \(p_K\) is a continuous representation. Surjectivity of \(p_K\) proves injectivity of this correspondence. The earlier local-to-global diagram says that both restrictions are the composition of \(\chi\) with the same map \(K_v^\times\to C_K\); this proves the final assertion. \(\square\)

The local subgroup description of §1 and this global extension construction are different constructions. Only the stated global theorem and Proposition 6.1 are used subsequently; their proof providers are the earlier programme argument and the proof just given.

## 7. Exercises with solutions

**Exercise 7.1 (easy).** Classify the smooth characters of \(W_F\) trivial on inertia. When does such a character have finite image?

**Solution.** It factors through \(v:W_F\to\mathbb Z\), so it is uniquely \(w\mapsto c^{v(w)}\), where \(c\) is its value at \(\Phi\). Every \(c\in\mathbb C^\times\) gives a smooth character because its kernel contains the open subgroup \(I_F\). Its image is finite exactly when \(c\) is a root of unity: finite image makes some positive power of \(c\) equal to one, and the converse is immediate. The norm character has \(c=q^{-1}\), so its image is infinite.

**Exercise 7.2 (medium).** Prove Theorem 2.2, including extension of the finite-image twist to \(G_F\). Explain why smoothness alone does not force semisimplicity.

**Solution.** Lemma 2.1 makes the inertia image finite. A power \(T^m\) of Frobenius commutes with that image and with \(T\). Irreducibility and Schur's lemma make it \(a\,1\). Twisting by \(c^{v(w)}\), with \(c^m=a^{-1}\), makes the Frobenius matrix have finite order. The image is contained in the finite set \(\{h(cT)^j:h\in H,0\le j<m\}\). Proposition 1.1 extends the finite quotient continuously to \(G_F\). Example 3.2 is smooth but has a nonsplit invariant line and nonsemisimple Frobenius. Irreducibility was used in the scalar step and cannot be omitted.

**Exercise 7.3 (medium).** Classify the irreducible continuous representations of \(W_{\mathbb R}\). For \(\omega_{2i,3}(re^{i\theta})=r^{2i}e^{3i\theta}\), give the dimension, determinant, and the character inducing the same representation after conjugation.

**Solution.** The common-eigenvector argument in Theorem 5.1 bounds the dimension by two. A conjugation-invariant character has angular exponent zero and yields the one-dimensional characters \(\operatorname{sgn}^\epsilon|\cdot|^t\). A character with nonzero angular exponent has two distinct weight lines interchanged by \(j\), giving the irreducible induction and the unordered-pair isomorphism criterion. In the requested example, \(n=3\ne0\), so the dimension is two; (9) has \(j^2=-1\) and determinant \(+1\) on \(j\). The determinant on \(\mathbb R^\times\) is \(|x|^{2i}\operatorname{sgn}(x)^4=|x|^{2i}\). The other inducing character is \(\omega_{2i,-3}\), with the same radial exponent, not \(\omega_{-2i,-3}\).

**Exercise 7.4 (hard).** Prove (4) for an arbitrary finite-index subgroup, and specialize it to a quadratic extension. Explain the sign in Example 4.2 without choosing a square root of \(a\).

**Solution.** With left-coset representatives, the matrix of \(g\) is a block permutation followed by the maps \(U(h_i(g))\). A block transposition has determinant \((-1)^d\), so its determinant is \(\operatorname{sgn}(\sigma_g)^d\prod_i\det U(h_i(g))\). The abelianized product is transfer, by the multiplication and representative-change calculations in Theorem 4.1. This proves the general formula. In index two the permutation sign is the quadratic quotient character, and local reciprocity identifies transfer with inclusion, yielding \(\omega_{E/F}\chi|_{F^\times}\). For the unramified example, Frobenius exchanges two cosets, so the permutation contributes \(-1\); the product of the two one-dimensional block maps is \(a\). Thus the determinant is \(-a\), independently of a choice of its square root.

## What this lesson does not prove

Lemmas 0.1–0.6 and Theorem 0.7 prove finite local reciprocity and all its norm, transfer and conjugation identities in both characteristics. Lemmas 0.8A–0.8C construct the formal modules, and Theorem 0.9 proves maximal-abelian cofinality, completion and existence. Propositions 1.1–1.2 prove the Weil topology, profinite completion and finite-extension subgroup assertions. Theorem 1.3 passes from the completion proved in Theorem 0.9 to Weil reciprocity, and the paragraph after (1) passes the identities of Theorem 0.7 to Weil groups. The free research locators provide material for these written proofs and fix conventions. The archimedean group presentations are [Deligne 1973, §2.2.5] or [Getz–Hahn, Examples 12.5–12.6]; their representation classification is proved here. The scalar form of Schur's lemma is proved inside Theorem 2.2; the averaging proof of Maschke's theorem was supplied in §3. Proposition 5.2 constructs the discrete series, proves its discrete occurrence and lowest-weight uniqueness, and computes its central and infinitesimal data. Example 5.3 verifies the corresponding real Weil parameter on that family by the proved classifications and explicit normalized data. The global construction, including the open abelian quotient and the local-to-global diagram, uses the actual earlier proof in *Brauer groups, fundamental classes, and class field towers*, Theorem 24.6 and §7. Proposition 6.1 proves the continuous character correspondence from those topological conclusions.

## References

- R. Sharifi, [*Algebraic Number Theory*, free author lecture notes, §9.1](https://www.math.ucla.edu/~sharifi/notes/algnum-ch09.html), for the unit lattice construction in both characteristics; Lemmas 0.1–0.3 and Proposition 0.4 supply the complete local arguments used here.
- R. Sharifi, [*Group and Galois Cohomology*, free author lecture notes, §§1.2–1.5 and 1.8–1.9](https://www.math.ucla.edu/~sharifi/notes/groupcoh-ch01.html), for finite cochains, transfer and cup products, constructed in Lemma 0.5; and [*Algebraic Number Theory*, §§8.1–8.2](https://www.math.ucla.edu/~sharifi/notes/algnum-ch08.html), for character and norm-group formulations, proved in Theorem 0.7.
- J. S. Milne, [*Class Field Theory*, free author course notes](https://www.jmilne.org/math/CourseNotes/CFT.pdf), I§§2–3 and III§§1–2, for formal modules and the unramified invariant calculation. Lemma 0.6, Lemmas 0.8A–0.8C and Theorem 0.9 supply the constructions and proofs used here.
- [Deligne 1973] Pierre Deligne, [*Les constantes des équations fonctionnelles des fonctions L*, freely readable author-institution copy](https://publications.ias.edu/sites/default/files/Number20.pdf), 1973, §§2.2–2.5. The geometric reciprocity normalization and transfer diagrams are §§2.3–2.3.2; the determinant of induction also appears in §1.2.
- [Getz–Hahn] Jayce R. Getz and Heekyoung Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*, free author draft of 22 April 2022](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), §§12.1 and 12.3. Section numbers refer to that draft.
- [Gazeau–del Olmo–Pejhan] Jean-Pierre Gazeau, Mariano A. del Olmo and Hamed Pejhan, [*The Holomorphic Discrete Series of SU(1,1): Orthogonality Relations and Tensor Products*, free arXiv preprint](https://arxiv.org/abs/2504.03901), §II, equations (7)–(9).
- [Kaletha–Horawa] Tasho Kaletha, notes by Aleksander Horawa, [*Math 679: Automorphic Forms*, freely available lecture notes](https://people.maths.ox.ac.uk/horawa/math_679.pdf), §7, pp.78–80, for the real infinitesimal and discrete-parameter conventions.
- [Blasius 2006] Don Blasius, *Hilbert modular forms and the Ramanujan conjecture*, §1.2. [Author's preprint](https://arxiv.org/abs/math/0511007).
