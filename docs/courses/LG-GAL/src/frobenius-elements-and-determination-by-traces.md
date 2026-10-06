# Frobenius elements and determination by traces

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An unramified prime supplies a conjugacy class in a Galois group. Chebotarev's theorem says that these classes test every finite quotient. Continuity then lets them test ℓ-adic representations, and semisimplicity turns equality of traces into an isomorphism. These are three separate steps: the construction of a local subgroup, the density argument, and the linear algebra of characters.

We use arithmetic Frobenius throughout: it acts by \(x\mapsto x^{q_v}\) on the residue field. The inverse element is geometric Frobenius. All representations considered with a topology are continuous. The local construction, finite Chebotarev theorem, and trace comparison are proved below. The analytic and reciprocity inputs to the density proof have the following exact earlier programme proof locators; a theorem title alone is not an input.

| Earlier written lesson | Result used and its proof locator |
|---|---|
| LG-GAL 01, *Profinite groups and ℓ-adic representations* | Lemmas 0B.1–0B.2 for extension of embeddings and finite Galois correspondence; Proposition 0C.1 and its preceding compactness proof for infinite Galois theory; Lemma 0D.1 for simple-root Hensel; Proposition 0E.1 for unique extended valuation, completeness, integral closure and the norm formula; Lemma 0A.2 for composition factors; Proposition 3.1 for cyclotomic Frobenius. |
| NT-ANT 05, *Decomposition of primes in extensions* | Theorems 5.1–5.2 for finite integral closures, prime norms and the fundamental identity; Theorem 5.4, including its proof's last paragraph, for finiteness of ramification. |
| NT-ANT 06, *Hilbert's ramification theory in Galois extensions* | Theorems 6.1–6.2 and Proposition 6.3 for transitivity, residue exactness, and restriction in towers; “Subfields and double cosets,” equations (8)–(10), with their proofs, for prime orbits and relative Frobenius. |
| NT-ANT 12, *Cyclotomic fields* | Theorem 12.1 and its proof for \(\operatorname{Gal}(\mathbb Q(\zeta_N)/\mathbb Q)=(\mathbb Z/N\mathbb Z)^\times\). |
| NT-ANT 16, *The Dedekind zeta function and the analytic class number formula* | Proposition 16.1 and Theorem 16.2, under “The series and its Euler product” and “Turning the counting error into continuation,” for the Euler product and positive simple pole at 1. Only that proved neighbourhood of 1 is used. |
| NT-ADL 09–10, *Tate's global theory: continuation and functional equation*; *Hecke L-functions and the Dedekind zeta function* | Theorem 9.2, equation (19) and its proof; the standard test in lesson 10, equation (3), and Theorem 10.1 and its proof, for holomorphy at 1 of a nontrivial finite-order Hecke L-function. |
| NT-CFT 06, *Local reciprocity and norm groups*; NT-CFT 16, *The global reciprocity law* | Theorem 6.3 and Proposition 6.4 with their proofs in §4 give the local norm quotient and arithmetic unramified formula. Lesson 16, §6, “Abstract reciprocity and its local comparison,” and Theorem 16.4 with its proof in §7 give the continuous surjective map on idèle classes and its local compatibility. The unit-image calculation is supplied in Lemma 3.0b below. |

The last three rows concern number fields of arbitrary degree, including the intermediate fields occurring in the proof. Section 3 gives the entire remaining density argument, rather than invoking a later or unwritten Chebotarev lesson. The freely available human sources consulted for this exposition are identified in the final section.

## 1. A local Galois group inside a global one

Let \(K\) be a number field, \(v\) a finite place, and \(K_v\) its completion. Choose an embedding \(\iota:\bar K\hookrightarrow\overline{K_v}\) extending the embedding of \(K\). It selects a prolongation \(\bar v\) of the valuation to \(\bar K\). Define
\[
 D_{\bar v}=\{g\in G_K:g\bar v=\bar v\}.
\]
The inertia subgroup \(I_{\bar v}\) consists of those elements of \(D_{\bar v}\) which act trivially on the residue field of \(\bar K\) at \(\bar v\).

We first supply the finite-level and approximation arguments needed to identify this subgroup. Write \(F=K_v\). Its finite extensions are complete and have a unique extension of its absolute value, by Proposition 0E.1 of lesson 01. In particular, every \(F\)-embedding between finite extensions is an isometry. These facts apply to \(F\): if \(K=\mathbb Q(a)\), its image lies densely in the finite complete field \(\mathbb Q_p(a)\), because rational approximations to coefficients approximate every linear combination of powers of \(a\). Thus its completion is that finite extension of \(\mathbb Q_p\).

**Lemma 1.0a (finite completion and decomposition).** If \(L/K\) is finite Galois and \(w=\bar v|_L\), extension to the completion induces
\[
D_w\xrightarrow{\sim}\operatorname{Gal}(L_w/F).
\tag{1}
\]
It identifies the global and local residue-field actions.

**Proof.** Choose a primitive element \(a\) of \(L/K\). The finite complete field \(F(\iota(a))\) contains \(\iota(L)\) densely, by coefficient approximation as above. It is therefore \(L_w\). An element of \(D_w\) is an isometry on \(L\), so extends uniquely to an \(F\)-automorphism of \(L_w\). Conversely an \(F\)-automorphism of \(L_w\) takes every element of \(\iota(L)\) to a root of its minimal polynomial over \(K\). Normality of \(L/K\) puts every such root in \(\iota(L)\). Its restriction is a \(K\)-automorphism preserving \(w\), since uniqueness of the extended absolute value makes it an isometry. These operations are inverse. The same argument for an embedding into an algebraic closure shows that \(L_w/F\) is normal; characteristic zero makes it separable.

The residue field of a valued field and of its completion agree: approximate an integral element of the completion to distance less than 1 by an element of the original field. The approximant is integral and has the same residue. The injection follows from preservation of the absolute value. Applying this to \(L\subset L_w\) proves the assertion about residue actions. A primitive element exists here by finite Galois theory: in a finite normal closure the finitely many proper intermediate fields are proper \(K\)-linear subspaces, and an infinite field's vector space is not their finite union. One proof of the latter chooses, by induction, a point outside all but the last subspace, and a line through it with direction outside the last; this line is contained in none of the subspaces and meets each in at most one point. \(\square\)

**Lemma 1.0b (Krasner and root approximation).** Suppose \(\alpha,\beta\) are algebraic over the complete field \(F\), and
\[
|\alpha-\beta|<|\alpha-\alpha'|
\quad\text{for every distinct }F\text{-conjugate }\alpha'\text{ of }\alpha.
\]
Then \(F(\alpha)\subseteq F(\beta)\). Moreover, if \(f\in F[X]\) has a simple root \(\alpha\) in a finite extension \(M/F\), every sufficiently close polynomial \(h\) of the same degree has a root in \(M\) arbitrarily close to \(\alpha\).

**Proof.** Every embedding \(\tau:F(\alpha,\beta)\to\overline F\) fixing \(F(\beta)\) is an isometry. Hence
\[
|\tau(\alpha)-\alpha|
\leq\max(|\tau(\alpha)-\beta|,|\beta-\alpha|)
=|\alpha-\beta|.
\]
The separation hypothesis forces \(\tau(\alpha)=\alpha\). The extension is separable, so the embeddings detect its degree: \(F(\alpha,\beta)=F(\beta)\).

For the second assertion write \(h(\alpha+T)=\sum_j b_jT^j\). As the coefficients of \(h\) tend to those of \(f\), one has \(b_0\to0\), \(b_1\to f'(\alpha)\ne0\), and the other \(b_j\) remain bounded. Choose a nonzero \(c\in M\) so small that the desired root distance exceeds \(|c|\), and that \(|b_jc^{j-1}/b_1|<1\) for every \(j\geq2\) throughout a fixed sufficiently small coefficient neighbourhood. After shrinking it further, \(|b_0/(cb_1)|<1\). Then
\[
H(Y)=\frac{h(\alpha+cY)}{cb_1}\in\mathcal O_M[Y],
\qquad H(0)\in\mathfrak m_M,
\qquad H'(0)=1.
\]
Lemma 0D.1 of lesson 01 gives \(y\in\mathfrak m_M\) with \(H(y)=0\). Consequently \(\beta=\alpha+cy\) is the required root and \(|\beta-\alpha|<|c|\). This also covers nonintegral \(\alpha\) and nonunit \(f'(\alpha)\); no stronger unproved version of Hensel is being invoked. \(\square\)

**Lemma 1.1 (local cofinality).** Every finite extension of \(K_v\) inside \(\overline{K_v}\) is contained in the completion, at the chosen place, of a finite Galois extension of \(K\).

**Proof.** If \(M=K_v\), take \(L=K\). Otherwise characteristic zero makes \(M/K_v\) separable. Choose a primitive element \(\alpha\), with minimal polynomial \(f\in K_v[X]\) of degree \(d>1\). Approximate the coefficients of this monic polynomial by coefficients in the dense subfield \(K\), obtaining \(h\in K[X]\) of degree \(d\). Lemma 1.0b gives a root \(\beta\in M\) of \(h\) arbitrarily close to \(\alpha\). Choose it closer than the minimum distance to the finitely many other conjugates. The same lemma gives \(K_v(\alpha)\subset K_v(\beta)\). The reverse inclusion holds because \(\beta\in M\); thus \(K_v(\beta)=M\).

The element \(\beta\) is algebraic over \(K\). Take the splitting field \(L/K\) of \(h\), embedded in \(\overline{K_v}\) so that it contains \(\beta\). Its completion contains \(K_v(\beta)=M\). This proves cofinality. \(\square\)

**Lemma 1.1a (residue fields and unramified extensions).** Let \(F\) be a finite extension of \(\mathbb Q_p\), with residue field \(k=\mathbb F_q\). In a chosen algebraic closure, there is a unique unramified extension \(U_f/F\) of each degree \(f\). Its residue field is \(\mathbb F_{q^f}\), and reduction induces
\[
\operatorname{Gal}(U_f/F)\simeq
\operatorname{Gal}(\mathbb F_{q^f}/\mathbb F_q)
=\langle x\mapsto x^q\rangle.
\tag{2}
\]
For finite Galois \(M/F\), its maximal unramified subfield is \(U_f\), where \(f=[k_M:k]\); inertia is \(\operatorname{Gal}(M/U_f)\). The residue field of \(\overline F\) is an algebraic closure of \(k\), and
\[
G_F/I_F\simeq\varprojlim_f\mathbb Z/f\mathbb Z
=\widehat{\mathbb Z}.
\tag{3}
\]

**Proof.** The roots of \(X^{q^f}-X\) in a splitting field form a field: they are closed under addition, multiplication, and inverses by the Frobenius identities. The derivative is \(-1\), so there are exactly \(q^f\) roots. They form \(k_f=\mathbb F_{q^f}\). Every finite extension of \(k\) of degree \(f\) has that cardinality and every nonzero element has \((q^f-1)\)-st power 1; hence it is this root field. The map \(x\mapsto x^q\) has order \(f\): a smaller order \(d\) would put \(q^f\) roots in the polynomial \(X^{q^d}-X\). Thus it generates the Galois group. The field is generated by one element. Indeed a finite subgroup \(A\) of a field's multiplicative group is cyclic: for each prime dividing its exponent choose an element with the largest prime-power order, and multiply these commuting elements to obtain an element of order equal to the exponent \(m\). Every member of \(A\) is a root of \(X^m-1\); the root bound gives \(|A|\leq m\), so this element generates \(A\).

Choose a monic lift \(h\in\mathcal O_F[X]\) of the minimal polynomial of a generator of \(k_f/k\), and let \(\theta\) be any root in \(\overline F\). All roots of a monic integral polynomial are integral: a root of absolute value greater than 1 would make its leading term strictly larger than every other term. Isometry of conjugates consequently makes every monic factor integral as well. Reduction of such a factorization would factor the irreducible reduction of \(h\), so \(h\) is irreducible. Its root field \(U=F(\theta)\) has degree \(f\), and its residue field contains \(k_f\).

For any finite local extension \(N/F\), the equality \([N:F]=ef\) follows directly from the earlier complete-field integral-closure theorem. Its ring of integers is free of rank \([N:F]\) over \(\mathcal O_F\); reducing modulo a base uniformizer gives that dimension over \(k\). The same quotient has a filtration with \(e\) successive quotients equal to \(k_N\), each of dimension \([k_N:k]\). Apply this equality to \(U\). Its residue degree is at least \(f=[U:F]\), so it is exactly \(f\) and its ramification index is 1.

All the distinct roots of the reduction of \(h\) lie in \(k_f\). Hensel lifting in \(U\) gives all its roots, so \(U/F\) is Galois. An automorphism with trivial residue action fixes \(\theta\), by uniqueness of the lift with its residue, and is the identity. The residue map is therefore injective between groups of the same order \(f\), and is an isomorphism.

If \(N/F\) is any unramified extension with residue field \(k_f\), lift the same residue generator in \(N\) using \(h\). Its root generates a subfield of degree \(f=[N:F]\), so generates \(N\). This proves uniqueness inside the chosen closure, since the preceding root field already contains every root of \(h\). It also proves \(U_f\subseteq U_g\) when \(f\mid g\).

For a finite Galois extension \(M/F\), lift a generator of \(k_M/k\) in \(M\). Its root field is \(U_f\subseteq M\). Restriction to \(U_f\) is onto by finite Galois theory, and reduction on that subfield is (2). An automorphism of \(M\) fixes every residue exactly when it fixes the lifted generator. Thus its inertia is \(\operatorname{Gal}(M/U_f)\). Every unramified subextension has residue degree dividing \(f\) and lies in \(U_f\), proving maximality.

Finally the residue field of \(\overline F\) is the union of the residue fields of its finite subextensions. Each is finite and all \(k_f\) occur, so that union is \(\overline k\). The residue action maps \(G_F\) onto each finite group in (2). To lift a compatible system of residue automorphisms, take the closed sets of automorphisms with the prescribed action at each finite unramified level. They are nonempty and have the finite intersection property; compactness of \(G_F\), proved in lesson 01, §0C, makes their intersection nonempty. Its kernel is precisely trivial residue action. The quotient is compact, and its target inverse limit is Hausdorff, so the induced bijection is a topological isomorphism. \(\square\)

Combining Lemmas 1.0a and 1.1a gives, at each finite global level,
\[
D_w\simeq\operatorname{Gal}(L_w/K_v),\qquad
I_w\simeq\operatorname{Gal}(L_w/L_w^{\mathrm{ur}}).
\tag{4}
\]
Here \(L_w^{\mathrm{ur}}\) is the just-constructed maximal unramified subfield; the residue-field identification in Lemma 1.0a identifies the two kernels.

**Theorem 1.2.** Restriction along \(\iota\) gives an isomorphism of topological groups
\[
 G_{K_v}\simeq D_{\bar v}\subset G_K,
 \qquad I_{K_v}\simeq I_{\bar v}.
\]
The subgroup \(D_{\bar v}\) is closed. Changing \(\iota\) conjugates the pair \((D_{\bar v},I_{\bar v})\) in \(G_K\).

**Proof.** A \(K_v\)-automorphism of \(\overline{K_v}\) preserves the elements algebraic over \(K\), hence preserves \(\iota(\bar K)\), and preserves the valuation. This defines restriction into \(D_{\bar v}\). Formula (4) identifies the restrictions at every finite Galois level. By Lemma 1.1, the local completions in those levels are cofinal among finite local extensions. Consequently their finite Galois groups have inverse limit \(G_{K_v}\). On the global side the inverse limit of the \(D_w\) is exactly the group preserving \(\bar v\): preserving a valuation can be tested on every finite subextension. The finite-level identifications therefore give the asserted isomorphism. They also identify inertia, because triviality of the residue-field action can be tested on every finite residue extension.

Each \(D_w\) is closed in a finite discrete quotient. The inverse image conditions defining \(D_{\bar v}\) show that it is closed in \(G_K\). For conjugacy, prolongations of \(v\) in a finite Galois extension are conjugate. To arrange the conjugating element compatibly, for each finite Galois \(L\) consider the nonempty closed subset of \(G_K\) sending one selected place of \(L\) to the other. These subsets have the finite intersection property, by passing to a common finite Galois overfield. Compactness produces an element in their intersection. It conjugates both decomposition groups and both inertia groups. \(\square\)

For a finite place the residue field is \(\mathbb F_{q_v}\). Lemma 1.1a and Theorem 1.2 prove that the quotient is
\[
 D_{\bar v}/I_{\bar v}\simeq
 \operatorname{Gal}(\overline{\mathbb F}_{q_v}/\mathbb F_{q_v})
 \simeq\widehat{\mathbb Z}.
\]
The arithmetic Frobenius is the element corresponding to \(1\), characterized by \(x\mapsto x^{q_v}\). A **Frobenius lift** is any preimage of this element in \(D_{\bar v}\). There is generally no distinguished lift before one kills inertia.

## 2. Frobenius invariants of an unramified representation

A representation \(\rho:G_K\to\operatorname{GL}(V)\) is **unramified at \(v\)** if it is trivial on \(I_{\bar v}\). Conjugacy makes this condition independent of the chosen embedding. In this case put
\[
 P_v(X)=\det(X-\rho(\operatorname{Frob}_v)).
\]

**Proposition 2.1.** The polynomial \(P_v\), and consequently its trace and determinant, are independent of both the Frobenius lift and the prolongation of \(v\).

**Proof.** Two lifts differ by an element of inertia, which acts as the identity. Changing the prolongation conjugates the local subgroup and the Frobenius coset. Their images under \(\rho\) are conjugate matrices. A characteristic polynomial is invariant under conjugation. \(\square\)

**Example 2.2 (quadratic splitting).** In \(\mathbb Q(\sqrt d)/\mathbb Q\), with \(d\ne1\) squarefree, an odd prime not dividing \(d\) has arithmetic Frobenius equal to \(1\) when \(d\) is a square modulo \(p\), and equal to the nontrivial automorphism otherwise. To verify unramifiedness, \(X^2-d\) has distinct roots in \(\mathbb F_{p^2}\); Lemma 1.1a and Hensel lifting put both roots in an unramified local extension. In the square case they lift already in \(\mathbb Q_p\). Otherwise Frobenius exchanges their two distinct residues and hence their unique lifts. The resulting sign is \(\left(\frac dp\right)\). For \(d=-1\), this recovers the calculation in the preceding lesson: the traces are \(1,-1,-1,1\) at \(p=5,3,7,13\), respectively.

**Example 2.3 (a cyclotomic quotient).** For \(p\nmid N\), arithmetic Frobenius in \(\operatorname{Gal}(\mathbb Q(\zeta_N)/\mathbb Q)\simeq(\mathbb Z/N\mathbb Z)^\times\) is \(p\bmod N\). The group identification has its written proof in NT-ANT 12, Theorem 12.1. For the Frobenius calculation, \(X^N-1\) has distinct roots in a finite residue extension, and Lemma 1.1a lifts all of them uniquely to an unramified extension. Residue Frobenius takes a root to its \(p\)-th power; uniqueness makes its action on the lift the same power. This is the argument of Proposition 3.1 in the preceding lesson, now for arbitrary \(N\). With \(N=7\), Frobenius at \(2\) has order \(3\), since \(2,4,1\) are its successive powers modulo \(7\). Frobenius at \(3\) has order \(6\): its successive powers are \(3,2,6,4,5,1\).

## 3. What Chebotarev makes dense

Let \(S\) be a finite set of finite places. Let \(N_S\) be the closed normal subgroup generated by the inertia groups outside \(S\), and define
\[
K_S=\bar K^{N_S},\qquad G_{K,S}=G_K/N_S.
\]
Finite Galois correspondence identifies the finite Galois subextensions of \(K_S/K\) with the finite extensions unramified outside \(S\): their inertia groups are the restriction images of the absolute ones by §1. Every finite subextension is contained in a finite Galois one. Conversely the normal closure of an unramified subextension remains unramified, because each inertia group fixes all its conjugates. Thus \(K_S\) is precisely their compositum. At \(v\notin S\), the Frobenius image in \(G_{K,S}\) is a well-defined conjugacy class.

### The finite density theorem, with its analytic inputs exposed

For a set \(A\) of finite primes of a number field \(F\), put
\[
\delta_F(A)=\lim_{s\downarrow1}
\frac{\sum_{v\in A}(Nv)^{-s}}{\Lambda(s)},
\qquad \Lambda(s)=\log\frac1{s-1},
\tag{5}
\]
when this limit exists. The parameter \(s\) is real. Every prime norm is at least 2.

**Lemma 3.0a (the prime sum and negligible relative degrees).** The full set of primes of \(F\) has Dirichlet density 1. Finite sets, and the primes of a finite extension \(M/F\) with relative residue degree greater than one, have density zero in the respective prime sums. Complements of density-one sets have density zero.

**Proof.** The proved Euler product and positive simple pole of NT-ANT 16 give
\[
\log\zeta_F(s)=\sum_v(Nv)^{-s}
 +\sum_v\sum_{r\geq2}\frac{(Nv)^{-rs}}r
=\sum_v(Nv)^{-s}+O(1).
\]
The error is uniform near 1: its absolute value is at most \(2\sum_v(Nv)^{-2}\leq2\zeta_F(2)\). Writing \(\zeta_F(s)=c_F/(s-1)+O(1)\), with \(c_F>0\), proves
\[
\sum_v(Nv)^{-s}=\Lambda(s)+O(1).
\tag{6}
\]
Finite sums are bounded. For primes \(u\) of \(M\) over \(v\) of \(F\), the earlier prime-decomposition proof gives \(Nu=(Nv)^{f(u/v)}\) and at most \([M:F]\) primes over \(v\). Hence
\[
\sum_{f(u/v)>1}(Nu)^{-s}
\leq[M:F]\sum_v(Nv)^{-2s}
\leq[M:F]\zeta_F(2)=O(1).
\tag{7}
\]
Division by \(\Lambda(s)\to\infty\) proves the assertions about zero density. Subtracting a set's weighted sum from (6) proves the complement assertion. The same nonnegative-sum calculation proves monotonicity and finite additivity when the indicated limits exist. In particular removal of a finite set changes no density. \(\square\)

**Lemma 3.0b (cyclic density).** Let \(L/F\) be finite cyclic with group \(B\) of order \(n\). For each \(b\in B\), the primes unramified in \(L\) with arithmetic Frobenius \(b\) have Dirichlet density \(1/n\).

**Proof.** Write \(B=\langle\sigma\rangle\) and list its characters
\(\chi_j(\sigma)=\exp(2\pi i j/n)\), \(0\leq j<n\).
Theorem 16.4 of the earlier *The global reciprocity law* makes
\(\omega_j=\chi_j\circ\operatorname{rec}_{L/F}\)
a continuous finite-order Hecke character on the idèle class group \(C_F\).

We verify the local unit assertion needed for its Euler factors. At a place \(v\), local reciprocity for the abelian extension \(L_w/F_v\) is onto its decomposition group \(D_v\), with kernel \(T=N_{L_w/F_v}L_w^\times\), by NT-CFT 06, Theorem 6.3. Its units map into inertia: restriction to the maximal unramified subfield has the valuation formula of Proposition 6.4. The norm formula of lesson 01, Proposition 0E.1, gives \(v_{F_v}(Na)=f\,v_{L_w}(a)\), where \(f\) is the residue degree. Hence \(v_{F_v}(T)=f\mathbb Z\), and
\[
D_v/\operatorname{rec}(\mathcal O_{F_v}^{\times})
\simeq F_v^\times/(\mathcal O_{F_v}^{\times}T)
\simeq\mathbb Z/f\mathbb Z.
\]
Inertia also has index \(f\), by Lemma 1.1a, so the unit image is exactly inertia. The uniformizer maps to arithmetic Frobenius modulo that inertia. Global–local compatibility in NT-CFT 16 now shows that \(\omega_j\)'s local unit character is trivial exactly when \(\chi_j\) kills local inertia, and at such a prime its uniformizer value is \(\chi_j(\phi_v)\), for an arithmetic Frobenius lift \(\phi_v\). Therefore its primitive Euler product is
\[
L_j(s)=\prod_{v:\chi_j(I_v)=1}
(1-\chi_j(\phi_v)(Nv)^{-s})^{-1}.
\tag{8}
\]
This equality retains a prime ramified in \(L\) whenever the individual character is unramified there. Absolute convergence for \(\Re s>1\) follows by domination by the prime sum in the zeta Euler product.

For \(j\ne0\), surjectivity of reciprocity makes \(\omega_j\) nontrivial. It cannot be a nontrivial pure imaginary norm twist: the norm takes all positive real values, and a continuous map from that connected group to a finite group is constant. The actual Hecke continuation proof in NT-ADL 09, Theorem 9.2, and its standard-test identification in NT-ADL 10, equation (3) and Theorem 10.1, thus make \(L_j\) holomorphic at 1. Dividing off the archimedean factors causes no difficulty there. A finite-order character is trivial on the connected groups \(\mathbb R_{>0}\) and \(\mathbb C^\times\); at a real place only its sign parity remains. Thus the real \(\Gamma_{\mathbb R}\) arguments at 1 are 1 or 2, and each \(\Gamma_{\mathbb C}\) argument is 1. The defining integral \(\Gamma(z)=\int_0^\infty e^{-t}t^{z-1}\,dt\) is holomorphic for \(\Re z>0\), by domination on compact parameter sets, and is positive at positive real arguments. These factors are consequently regular and nonzero near 1. This is the only Hecke analytic theorem used below.

We prove the required nonvanishing, including its Euler identity. At a prime \(v\), let the inertia order be \(e\), the residue degree \(f\), and the number of primes of \(L\) above it \(g=n/(ef)\). Exactly \(n/e\) characters kill inertia. The Frobenius in \(D_v/I_v\) has order \(f\). Evaluation of these characters on it takes each \(f\)-th root of unity exactly \(g\) times; this follows immediately by writing the characters of the cyclic quotient \(B/I_v\) as powers of its primitive root character. Consequently the product of their local factors is
\[
\prod_{\chi_j(I_v)=1}(1-\chi_j(\phi_v)T)^{-1}
=(1-T^f)^{-g},\qquad T=(Nv)^{-s}.
\]
This is exactly the zeta factor of \(L\), since its \(g\) prime norms are \((Nv)^f\). Multiplication over all primes proves
\[
\zeta_L(s)=\prod_{j=0}^{n-1}L_j(s)
=\zeta_F(s)\prod_{j=1}^{n-1}L_j(s).
\tag{9}
\]
The ratio \(\zeta_L/\zeta_F\) is holomorphic and has value \(c_L/c_F>0\) at 1 by the earlier proved simple poles. Every factor on the right is holomorphic there. None can vanish there, since otherwise their finite product would vanish. Thus \(L_j(1)\ne0\) for all \(j\ne0\).

For real \(s>1\), let
\[
S_j(s)=\sum_{v\text{ unramified in }L}
\chi_j(\operatorname{Frob}_v)(Nv)^{-s}.
\]
The Euler logarithm of \(L_j\) differs from \(S_j\) by \(O(1)\), uniformly as \(s\downarrow1\). Terms of degree at least two are bounded by the calculation in Lemma 3.0a; finitely many omitted or retained ramified prime factors are also bounded. A nonzero holomorphic function in a sufficiently small disk around 1 has a holomorphic logarithm there: the power series of its logarithmic derivative has a termwise antiderivative, and differentiation shows that multiplying the original function by the exponential of the negative antiderivative gives a constant. Choose a logarithm of that nonzero constant. This logarithm on \(1<s<1+\epsilon\) differs from the Euler logarithm by a constant integral multiple of \(2\pi i\). Hence
\[
S_j(s)=O(1)\quad(j\ne0),\qquad
S_0(s)=\Lambda(s)+O(1).
\tag{10}
\]
The geometric-series identity for \(n\)-th roots of unity gives
\[
\mathbf1_{a=b}=\frac1n\sum_{j=0}^{n-1}
\chi_j(b)^{-1}\chi_j(a)\qquad(a,b\in B).
\]
Multiplying by prime weights and summing, (10) gives
\[
\sum_{\operatorname{Frob}_v=b}(Nv)^{-s}
=\frac1n\Lambda(s)+O(1).
\tag{11}
\]
This proves the cyclic density without assuming any prime-distribution theorem. \(\square\)

**Theorem 3.0c (finite Chebotarev).** Let \(L/K\) be finite Galois with group \(H\), and let \(C\) be a conjugacy class in \(H\). The unramified primes whose arithmetic Frobenius class is \(C\) have Dirichlet density
\[
\delta_K(\mathcal P_C)=\frac{|C|}{|H|}>0.
\tag{12}
\]

**Proof.** Choose \(\sigma\in C\), let \(m\) be its order, and put \(M=L^{\langle\sigma\rangle}\). The extension \(L/M\) is cyclic of degree \(m\). By Lemma 3.0b, its primes \(u\) with Frobenius exactly \(\sigma\) have weighted sum \(m^{-1}\Lambda(s)+O(1)\). Discard primes over the finite ramification set of \(L/K\), and discard the primes with \(f(u/v)>1\), for \(v\) their contraction to \(K\). The first omission is finite and the second is bounded by (7). For the remaining primes \(Nu=Nv\).

Consider the set of primes \(w\) of \(L\) unramified over \(K\) whose Frobenius element is exactly \(\sigma\). Contraction \(w\mapsto u=w|_M\) gives a bijection to those remaining primes. Indeed their decomposition group over \(K\) is \(\langle\sigma\rangle\), their residue degree is \(m\), and the decomposition group over \(M\) is its intersection with \(\operatorname{Gal}(L/M)=\langle\sigma\rangle\), also the full group. Multiplicativity of residue degrees gives \(f(u/v)=1\); the full relative decomposition group makes \(w\) unique over \(u\). Conversely, if \(f(u/v)=1\) and the relative Frobenius is \(\sigma\), the relative Frobenius formula (10) in NT-ANT 06 identifies the global Frobenius with \(\sigma\). These facts prove both directions of the bijection, including uniqueness.

Over a fixed \(v\in\mathcal P_C\), choose \(w_0\) with Frobenius \(\sigma\). All top primes are \(h w_0\), with stabilizer \(D_{w_0}=\langle\sigma\rangle\). Their Frobenius is \(h\sigma h^{-1}\), by the proved conjugacy formula. Thus the top primes with Frobenius exactly \(\sigma\) are parametrized by
\[
Z_H(\sigma)/\langle\sigma\rangle,
\]
where \(Z_H(\sigma)\) is the centralizer. There are exactly \(|Z_H(\sigma)|/m\) such primes, and hence that many contributing \(u\) over each \(v\in\mathcal P_C\). If \(v\notin\mathcal P_C\), there are none. Equality of the degree-one norms now gives
\[
\frac1m\Lambda(s)+O(1)
=\frac{|Z_H(\sigma)|}{m}
\sum_{v\in\mathcal P_C}(Nv)^{-s}.
\]
It follows that the density is \(1/|Z_H(\sigma)|\). Orbit–stabilizer for conjugation gives \(|C|=|H|/|Z_H(\sigma)|\), proving (12). \(\square\)

Finite additivity in Lemma 3.0a also proves the usual statement for every conjugation-stable subset \(A\subseteq H\): its Frobenius primes have density \(|A|/|H|\), by taking the union of its conjugacy classes. This proof reaches every conjugacy class in an arbitrary finite Galois group. The cyclic field \(M\) varies with the chosen element; it need not be Galois over \(K\). The relative degree condition in (7) permits its prime sum to be compared to the prime sum over \(K\).

### Passing from finite density to a profinite group

**Theorem 3.1 (density of Frobenius elements).** Let \(T\) be a set of finite places of Dirichlet density one. The union of the Frobenius conjugacy classes at \(v\in T\setminus S\) is dense in \(G_{K,S}\).

**Proof.** It suffices to meet every basic open set. Such a set is the inverse image of a particular element \(h\) in a finite quotient \(H\) of \(G_{K,S}\). This quotient corresponds to a finite Galois extension \(L/K\) unramified outside \(S\). Theorem 3.0c gives positive density to the places whose Frobenius belongs to the conjugacy class of \(h\). The complement of \(T\), and the finite set \(S\), cannot contain all these places. Choose one in \(T\setminus S\). Conjugating its Frobenius image gives an element mapping exactly to \(h\). It therefore lies in the specified basic open set. \(\square\)

This proof explains why the conjugates are included. Choosing one Frobenius representative at each prime does not by itself guarantee a dense subset of a nonabelian group. It also explains why equality on an arbitrary positive-density set is insufficient. In a quadratic extension, the trivial character and its nontrivial quadratic character agree at the split primes, a set of density \(1/2\).

## 4. The linear algebra behind trace comparison

The following lemma is the characteristic-zero trace form of Brauer–Nesbitt. Its proof works for an arbitrary group, with no topology or finiteness assumption on that group.

**Lemma 4.1.** Let \(V,W\) be finite-dimensional semisimple representations of a group \(G\) over a characteristic-zero field \(E\). If
\[
 \operatorname{tr}(g\mid V)=\operatorname{tr}(g\mid W)
 \quad\text{for every }g\in G,
\]
then \(V\simeq W\) over \(E\).

**Proof.** If \(V\oplus W=0\), the conclusion is immediate. Otherwise set \(M=V\oplus W\), and let \(A\) be the \(E\)-linear span of the image of \(G\) in \(\operatorname{End}_E(M)\). Products of image elements are image elements, so \(A\) is a finite-dimensional algebra with identity. Its invariant subspaces are exactly the \(G\)-invariant subspaces. Hence \(M\) is a faithful semisimple \(A\)-module.

We describe the central projectors needed in the argument. Choose an \(E\)-basis \(m_1,\dots,m_d\) of \(M\). The map
\[
 A\longrightarrow M^d,\qquad a\longmapsto(am_1,\dots,am_d)
\]
is an injective map of left \(A\)-modules. We prove the module fact which makes its image semisimple. In a finite direct sum of simple modules every submodule has a complement, by induction on the number of summands. Write the ambient module as \(Q=M'\oplus S\), with \(S\) simple, and let \(U\) be a submodule. By induction \(U_0=U\cap M'\) has a complement \(C\) in \(M'\). In \(Q/U_0=C\oplus S\), the image of \(U\) intersects \(C\) trivially. Its projection to \(S\) is therefore injective, with image either zero or all of \(S\). In the latter case it is the graph of an \(A\)-linear map \(S\to C\); subtracting the \(U_0\)-component of a lift shows that this graph already lies in \(U\subset U_0\oplus C\oplus S\). Thus \(U\) is \(U_0\) plus a simple summand, and has complement \(C\). In the zero case \(U=U_0\) has complement \(C\oplus S\). This proves both claims inductively. Apply it to the image of \(A\) in \(M^d\); the left regular module \(A\) is semisimple.

Decompose the regular module into its isotypic parts \(A=\bigoplus_i A_i\), one for each isomorphism class of simple module occurring. A homomorphism between simple modules is zero or an isomorphism, by taking its kernel and image. Every right multiplication is a left-module homomorphism, so it preserves these isotypic parts. Thus each \(A_i\) is a two-sided ideal. The projection onto \(A_i\) commutes with left and right multiplication. If \(e_i\) is the projection of \(1\), its value at \(a\) is both \(ae_i\) and \(e_i a\). Consequently the \(e_i\) are central orthogonal idempotents and their sum is \(1\). Every simple module \(S\) is a quotient of \(A\), by \(a\mapsto as\) for a nonzero \(s\in S\). If its type is \(i\), each \(A_j\) with \(j\ne i\) has zero image in this quotient, since its summands have different simple types. Thus \(e_i\) acts as the identity on \(S\), and every other \(e_j\) acts as zero. In particular every simple type in \(M\) occurs in \(A\).

Equality of traces on \(G\) implies equality on its linear span \(A\). If \(S_i\) is the simple module of type \(i\), evaluation at \(e_i\) gives
\[
 m_i(V)\dim_ES_i=m_i(W)\dim_ES_i.
\]
Characteristic zero allows cancellation of the positive integer \(\dim_ES_i\). Thus all simple multiplicities agree, proving the isomorphism. The proof does not require \(E\) to be a splitting field. \(\square\)

**Theorem 4.2 (determination by Frobenius traces).** Let \(E/\mathbb Q_\ell\) be finite. Let \(\rho_1,\rho_2\) be semisimple continuous finite-dimensional representations of \(G_K\) over \(E\), both unramified outside a finite set \(S\). If their arithmetic-Frobenius traces agree at every prime in a Dirichlet-density-one set outside \(S\), then \(\rho_1\simeq\rho_2\).

**Proof.** Both kernels are closed normal subgroups containing every inertia group outside \(S\), hence containing their closed normal span \(N_S\). Both representations therefore factor continuously through \(G_{K,S}\). Their trace functions are continuous, because matrix trace is continuous, and are invariant under conjugation. The hypothesis and Theorem 3.1 make them equal on a dense subset. Their difference is a continuous function into the Hausdorff field \(E\), with closed zero set. It therefore vanishes everywhere. Apply Lemma 4.1. \(\square\)

Equality of characteristic polynomials implies equality of traces and hence the same conclusion. Conversely an isomorphism implies equality of all such polynomials. Two representations which are not assumed semisimple still have isomorphic semisimplifications under the trace hypothesis. A composition series exists and its simple factors are intrinsic by lesson 01, Lemma 0A.2. In a basis adapted to that series every group matrix is block upper triangular; its diagonal blocks give the factor actions. Those blocks are continuous functions of the original matrix, and their traces add and characteristic polynomials multiply. Their direct sum is therefore a continuous semisimplification with the same traces and polynomials, to which Theorem 4.2 applies. The unipotent representation of \(\mathbb Z_\ell\) in the preceding lesson and the two-dimensional trivial representation have identical traces and characteristic polynomials, but are not isomorphic. This exhibits the lost extension data.

For a one-dimensional representation, semisimplicity is automatic. Thus two ℓ-adic characters that agree at a density-one set of Frobenius elements are equal. In particular, a finite-order character of \(G_{\mathbb Q}\) trivial at almost all Frobenius elements is trivial. Its image is finite, so each point is isolated in the induced Hausdorff topology, and continuity makes its kernel open. Proposition 0C.1 of lesson 01 makes that kernel correspond to a finite extension. The finite ramification set proved in NT-ANT 05, Theorem 5.4, supplies the required \(S\).

## 5. Exercises and complete solutions

**Exercise 5.1 (easy).** Prove that an unramified Frobenius characteristic polynomial is unaffected by changing the embedding or the lift.

**Solution.** A change of lift multiplies by an inertia element, which lies in the kernel of the representation. A change of embedding conjugates the decomposition and inertia groups and the chosen Frobenius class. The resulting matrices are conjugate. Taking \(\det(X-A)\) proves invariance, as in Proposition 2.1. If inertia acts nontrivially, the first argument fails and different lifts can have different characteristic polynomials.

**Exercise 5.2 (medium).** Deduce that a finite-order character of \(G_{\mathbb Q}\) which is trivial on almost all arithmetic Frobenius elements is trivial.

**Solution.** Its kernel cuts out a finite abelian extension \(L/\mathbb Q\). Take any element \(h\) of its Galois group. Theorem 3.0c supplies positive density to the primes with Frobenius \(h\). Removing the finite exceptional set leaves a prime at which the character value is both the value at \(h\) and \(1\). Thus the character is \(1\) on every element of the finite quotient, and consequently on \(G_{\mathbb Q}\).

**Exercise 5.3 (medium).** Prove density of the Frobenius conjugacy classes in \(G_{K,S}\), retaining only a density-one set of primes.

**Solution.** A basic open neighbourhood specifies an element in a finite Galois quotient. Theorem 3.0c supplies a positive-density set of primes for its conjugacy class. A zero-density complement cannot exhaust that set. Choose an allowed prime and conjugate its Frobenius representative to the specified element of the quotient. This meets the neighbourhood. This is exactly the finite-quotient argument of Theorem 3.1; no version of Chebotarev for an infinite extension is needed.

**Exercise 5.4 (hard).** Prove determination by traces for semisimple ℓ-adic representations over a finite extension of \(\mathbb Q_\ell\). Explain why neither an algebraically closed coefficient field nor finite image is necessary.

**Solution.** Pass to the common unramified-outside-\(S\) quotient. Use Exercise 5.3, conjugacy invariance, and continuity to deduce trace equality at every group element. Form the finite-dimensional algebra spanned by the images on the direct sum of the two spaces. Its regular module embeds in a finite direct sum of the faithful semisimple representation. The central isotypic projectors constructed in Lemma 4.1 compare each simple multiplicity by trace. This proves an isomorphism over the original field. Finite dimensionality of the image algebra follows from its inclusion in a matrix algebra, even when the group image is infinite. The projector argument uses simple modules over \(E\) itself, so scalar extension to an algebraic closure is unnecessary.

## Proof dependencies and free sources

The opening table gives the precise written programme proofs used for local completeness and Hensel lifting, finite prime decomposition, cyclotomic irreducibility, the positive zeta pole, finite-order Hecke holomorphy, and global reciprocity. Those earlier proofs are inputs here. The finite completion identification, Krasner inequality, coefficient-approximation argument, finite-field and unramified-extension constructions, absolute residue exactness, cyclic Euler identity and nonvanishing, full finite Chebotarev theorem, profinite density deduction, and trace comparison are proved in this lesson. No assertion here depends on a promised later proof. Basic field, matrix and complex-function operations have their calculations displayed at the places they are used.

The human references below are freely readable primary sources. The density argument was checked against Milne's free course notes. Taylor and Deligne–Serre identify the Galois-representation application; their citations do not replace the proofs above. Taylor uses geometric Frobenius, whereas Deligne–Serre's §3 footnote and this lesson use arithmetic Frobenius.

- J. S. Milne, [*Algebraic Number Theory*, v3.08 (2020)](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Proposition 7.31, printed p.120 (simple-root lifting); Proposition 7.50 and its proof, pp.127–128 (unramified extensions and residues); Proposition 7.60 and its proof, pp.131–132 (Krasner); Proposition 8.10 and its proof, p.139 (completion and decomposition). These free locators concern the arguments proved in §1.
- J. S. Milne, [*Class Field Theory*, v4.03 (2020)](https://www.jmilne.org/math/CourseNotes/CFT.pdf), Chapter VI §4, especially Theorem 4.8 and Corollary 4.10, printed pp.197–199, and Chapter VIII §7, Theorems 7.1–7.4 and their proofs, pp.258–260. The latter gives the cyclic fixed-field reduction and its exact prime count. Section 3 above spells out the cyclic Euler-factor identity and nonvanishing before performing that count.
- Richard Taylor, [*Galois representations*](https://www.numdam.org/item/AFST_2004_6_13_1_73_0/), Annales de la Faculté des sciences de Toulouse, series 6, 13 (2004), 73–119; §1, printed pp.74–75 and p.79, for local subgroups and Frobenius density. [Free full text](https://www.numdam.org/item/AFST_2004_6_13_1_73_0.pdf).
- Pierre Deligne and Jean-Pierre Serre, [*Formes modulaires de poids 1*](https://www.numdam.org/item/ASENS_1974_4_7_4_507_0/), Annales scientifiques de l'École Normale Supérieure, series 4, 7 (1974), 507–530; §3, Lemma 3.2 and the Frobenius-convention footnote, printed p.513. [Free full text](https://www.numdam.org/article/ASENS_1974_4_7_4_507_0.pdf).
