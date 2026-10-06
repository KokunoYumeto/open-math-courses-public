# The reciprocity law and the class field correspondence

*Written by OpenAI GPT-6.1 Sol in Codex, Ultra effort, October 2026. Self-checked by the writing AI; no independent review is claimed. Public domain (CC0).*

The preceding lesson constructed a homomorphism from Galois automorphisms to classes modulo norms. The class field axiom will make it an isomorphism. Its inverse, the norm residue symbol, expresses an automorphism in terms of an arithmetic element of the ground field. The resulting correspondence classifies finite abelian extensions by their norm subgroups.

The cyclic axiom does not restrict the conclusion to solvable extensions. We will prove the cyclic case by a valuation argument, handle abelian extensions by cyclic quotients, and then use Sylow subgroups to obtain the theorem for every finite Galois group. This order keeps the group-theoretic reduction explicit.

We retain the additive module notation, the degree map, the henselian valuation with image \(V\subset\widehat{\mathbf Z}\), and normalized valuations from [Frobenius lifts and abstract reciprocity](frobenius-lifts-and-abstract-reciprocity.md). Thus \(V\) contains \(\mathbf Z\), and \(V/nV\simeq\mathbf Z/n\mathbf Z\). For multiplicative modules, sums below mean products. Cyclic Tate groups and their exact hexagon were proved in [Cohomology of cyclic groups and the Herbrand quotient](cohomology-of-cyclic-groups-and-the-herbrand-quotient.md).

## 1. The class field axiom implies the unit axiom

The **class field axiom** is the following condition for every finite cyclic extension \(L/K\), with \(T=\operatorname{Gal}(L/K)\):

\[
|\widehat H^0(T,A_L)|=[L:K],\qquad
\widehat H^{-1}(T,A_L)=0.
\tag{1}
\]

The first assertion says that \(A_K/N_{L/K}A_L\) has exactly the extension degree many elements. The second says that every norm-zero element is a difference \((\sigma-1)a\), for a generator \(\sigma\) of \(T\). Knowing only the quotient of these two orders would not give either assertion separately.

For an unramified cyclic extension of degree \(n\), (1) implies both parts of the unit axiom used in the preceding lesson. Indeed, valuation induces a surjection

\[
A_K/N_{L/K}A_L\longrightarrow V/nV.
\]

Both groups have order \(n\), so it is an isomorphism. If \(u\in U_K\), it follows that \(u=N_{L/K}a\) for some \(a\in A_L\). The equation \(0=v_K(u)=n v_L(a)\) implies \(a\in U_L\), since \(\widehat{\mathbf Z}\) is torsion free. Thus unit norms are surjective.

If \(u\in U_L\) has norm zero, (1) gives \(u=(\sigma-1)a\), \(a\in A_L\). Choose \(b\in A_K\) with \(v_K(b)=v_L(a)\). This is possible because \(v_K\) is onto \(V\), and unramified inclusion preserves normalized valuation. Then \(a-b\in U_L\) and \((\sigma-1)(a-b)=u\). Hence the norm-zero units are precisely the differences of units. This proof works for the full allowed value group \(V\); it does not require expressing \(a\) as an integer multiple of a prime plus a unit.

Consequently the complete construction and functoriality of the preceding lesson apply. Write

\[
Q_{L/K}=A_K/N_{L/K}A_L,\qquad
r_{L/K}:\operatorname{Gal}(L/K)^{\mathrm{ab}}\longrightarrow Q_{L/K}.
\tag{2}
\]

## 2. Two elementary reduction tools

Suppose \(M/K\) is a Galois intermediate extension in a finite Galois \(L/K\). Norm transitivity gives an exact sequence

\[
A_M/N_{L/M}A_L
\xrightarrow{N_{M/K}} Q_{L/K}
\longrightarrow Q_{M/K}\longrightarrow0.
\tag{3}
\]

The last map is the quotient map. Its kernel is \(N_{M/K}A_M/N_{L/K}A_L\), exactly the image of the first map; the first map need not be injective. The corresponding Galois sequence is

\[
\operatorname{Gal}(L/M)\longrightarrow
\operatorname{Gal}(L/K)\longrightarrow
\operatorname{Gal}(M/K)\longrightarrow1.
\tag{4}
\]

Norm functoriality from Proposition 4.4 makes reciprocity commute with these two sequences, viewing each Galois group through its map to the abelianization when needed. In particular, if \(r_{M/K}\) and \(r_{L/M}\) are surjective, so is \(r_{L/K}\): lift a quotient class using the former, subtract its reciprocity value, and lift the remainder in the kernel of (3) using the latter.

We also need that cyclic quotients detect elements of a finite abelian group \(B\). Here is a direct proof. Given \(b\ne0\), define a character \(\langle b\rangle\to\mathbf Q/\mathbf Z\) taking \(b\) to an element of its exact order. Extend a character \(\chi\) from a subgroup \(D\) to \(D+\langle x\rangle\) as follows. Let \(m\) be the least positive integer with \(mx\in D\), and choose \(c\in\mathbf Q/\mathbf Z\) with \(mc=\chi(mx)\). Define the extension by \(\chi(d+jx)=\chi(d)+jc\). Any relation between two such expressions has \(j-j'\) divisible by \(m\), which proves well-definedness. Repeating this finite process extends the character to \(B\). Its image is a finite subgroup of \(\mathbf Q/\mathbf Z\), hence cyclic: a common denominator embeds it in a cyclic group. Thus some cyclic quotient of \(B\) detects \(b\).

## 3. The cyclic reciprocity theorem

First suppose \(L/K\) is cyclic of degree \(n\), and totally ramified. We prove injectivity of \(r_{L/K}\) directly.

Put \(\Gamma=\operatorname{Gal}(\widetilde L/K)\). Since \(L\cap\widetilde K=K\), restriction gives

\[
\Gamma\simeq\operatorname{Gal}(L/K)\times
\operatorname{Gal}(\widetilde K/K).
\]

Choose a generator \(\sigma\) of the first factor, acting trivially on \(\widetilde K\), and let \(\phi\) be the arithmetic Frobenius of the second, acting trivially on \(L\). They commute. The positive lift \(s=\sigma\phi\) has degree 1. Its fixed field \(\Sigma\) is a totally ramified cyclic extension of \(K\) of degree \(n\), by the degree and index calculation in section 2 of the preceding lesson. Take prime elements \(\pi_\Sigma,\pi_L\).

Let \(M=L\Sigma\subset\widetilde L\). It is finite Galois over \(K\), because \(\Gamma\) is abelian, and is unramified over both \(L\) and \(\Sigma\). If \(M_0=M\cap\widetilde K\), then \(M/M_0\) is cyclic of degree \(n\), generated by the restriction of \(\sigma\). This follows because the inertia subgroup \(\langle\sigma\rangle\) has trivial intersection with the stabilizer of \(\Sigma\). Its restrictions identify it with both \(\operatorname{Gal}(L/K)\) and \(\operatorname{Gal}(\Sigma/K)\). Therefore its norm operator \(N=1+\sigma+\cdots+\sigma^{n-1}\) restricts to \(N_{L/K}\) on \(A_L\) and to \(N_{\Sigma/K}\) on \(A_\Sigma\).

Use the normalized valuation \(w=v_M\). Both chosen primes have \(w=1\). Suppose

\[
r_{L/K}(\sigma^j)=0,\qquad 0\leq j<n.
\]

The reciprocity homomorphism and its defining prime norm give \(jN\pi_\Sigma\in N_{L/K}A_L\). Set \(u=j(\pi_\Sigma-\pi_L)\in U_M\). Then \(Nu\in N_{L/K}A_L\). Choose \(v\in A_L\) with \(Nv=Nu\). Its valuation is zero because \(v_K(Nv)=v_L(v)\) in this totally ramified extension; thus \(v\in U_L\).

Now \(N(v-u)=0\). Apply the norm-zero half of (1) to the cyclic extension \(M/M_0\). There is \(a\in A_M\) with

\[
v-u=(\sigma-1)a,\qquad
j\pi_L+v=j\pi_\Sigma+(\sigma-1)a.
\tag{5}
\]

On the left of (5), \(s\) acts as \(\sigma\), since that side is in \(A_L\). On the right, \(s\pi_\Sigma=\pi_\Sigma\). Applying \(s-1\), and using commutation of \(s,\sigma\), shows that

\[
x=j\pi_L+v-(s-1)a
\]

is fixed by \(\sigma\), hence belongs to \(A_{M_0}\). The action preserves \(w\), so \(w((s-1)a)=0\) and \(w(x)=j\). But \(M/M_0\) has ramification index \(n\). The valuation-inclusion formula (9) of the preceding lesson yields

\[
j=n v_{M_0}(x)\in nV\subset n\widehat{\mathbf Z}.
\]

An ordinary integer in \(n\widehat{\mathbf Z}\) is divisible by \(n\), by reduction modulo \(n\). Since \(0\leq j<n\), we get \(j=0\). This proves injectivity. The source and target both have order \(n\), the latter by (1), so reciprocity is an isomorphism.

For a general cyclic \(L/K\), let \(M=L\cap\widetilde K\). Then \(M/K\) is unramified and \(L/M\) is totally ramified cyclic. Their reciprocity maps are isomorphisms, the first by Proposition 4.3 and the second by the argument just given. In (3), the three groups have orders \([L:M]\), \([L:K]\), and \([M:K]\), by (1). The kernel at the middle has order \([L:M]\); hence its surjective norm map from the first group is injective as well. The matching exact Galois sequence (4) now proves that \(r_{L/K}\) is injective and surjective: lift a quotient element, and use the isomorphism on the two kernels to correct the lift. This proves cyclic reciprocity in full.

## 4. From cyclic groups to every finite Galois group

### Theorem 5.1. The general reciprocity law

For every finite Galois \(L/K\),

\[
r_{L/K}:\operatorname{Gal}(L/K)^{\mathrm{ab}}
\xrightarrow{\sim} A_K/N_{L/K}A_L.
\tag{6}
\]

**Proof for abelian groups.** Let \(T=\operatorname{Gal}(L/K)\) be abelian. If an element of \(T\) has zero reciprocity class, its restriction has zero reciprocity class in every cyclic quotient extension. Cyclic reciprocity is injective, and the character argument in section 2 says these restrictions detect every nonidentity element. Thus \(r_{L/K}\) is injective.

Surjectivity follows by induction on \(|T|\). The cyclic case is proved. If \(T\) is not cyclic, choose a nontrivial cyclic quotient and its fixed field \(M\); then both \(M/K\) and \(L/M\) have smaller degree, and the latter is abelian. Apply induction and the lifting argument in (3)–(4). This proves the abelian case.

**Injectivity for arbitrary groups.** Put \(T=\operatorname{Gal}(L/K)\), and let \(B\) be the fixed field of the commutator subgroup \(T'\). Restriction identifies \(T^{\mathrm{ab}}\) with \(\operatorname{Gal}(B/K)\). The composite

\[
T^{\mathrm{ab}}\xrightarrow{r_{L/K}}Q_{L/K}
\longrightarrow Q_{B/K}
\]

is the already proved abelian reciprocity isomorphism. Hence \(r_{L/K}\) is injective. Equivalently, the kernel of the map on \(T\) is exactly \(T'\): it contains \(T'\) because the target is abelian, and its projection to \(T/T'\) is injective.

**Surjectivity for solvable groups.** Here a finite group is solvable if its iterated commutator subgroups eventually become trivial. Induct on its order. If \(T'=1\), the abelian case applies. Otherwise \(1<T'<T\); with \(B\) as above, \(B/K\) is abelian and \(L/B\) has smaller solvable Galois group. Their maps are surjective, so (3)–(4) prove surjectivity for \(L/K\).

**The Sylow step.** First recall why finite \(p\)-groups are solvable. Conjugacy classes outside the center have size divisible by \(p\), so the class equation makes the center of a nontrivial \(p\)-group nontrivial. Quotient by this center and induct on the order. A group with an abelian normal subgroup and solvable quotient is solvable: enough commutator iterations enter the normal subgroup and one more makes them trivial. This proves the assertion about \(p\)-groups.

We need only the existence part of Sylow's theorem, which can also be proved here. Write \(|T|=p^b u\), with \(p\nmid u\), and let \(T\) act by left multiplication on the subsets of its underlying set having \(p^b\) elements. Their number is \(\binom{p^b u}{p^b}\equiv u\pmod p\): in \(\mathbf F_p[X]\), the identity \((1+X)^{p^b u}=(1+X^{p^b})^u\) proves this by comparing coefficients. Thus some orbit has cardinality prime to \(p\). Its stabilizer \(P\) has \(p\)-part of order \(p^b\), by the orbit–stabilizer formula. On the selected subset, \(P\) acts freely, since a nonidentity left multiplication fixes no group element. Hence \(|P|\) divides the subset's cardinality \(p^b\). These two facts imply \(|P|=p^b\), which is the required Sylow subgroup.

Now \(Q=Q_{L/K}\) is annihilated by \(m=|T|\). Indeed, inclusion sends \(a\in A_K\) to \(A_L\), and \(N_{L/K}a=ma\). A group annihilated by \(m=\prod_p p^{b_p}\) decomposes as \(Q=\bigoplus_p Q_p\), where \(p^{b_p}Q_p=0\). To verify this even before knowing \(Q\) finite, choose integers \(c_p\) which are 1 modulo \(p^{b_p}\) and 0 modulo the other prime powers, by the Chinese remainder theorem. Multiplication by \(c_p\) gives pairwise orthogonal projections whose sum is the identity on \(Q\).

Fix \(p\mid m\), choose a Sylow \(p\)-subgroup \(P\subset T\), and let \(F=L^P\). The extension \(F/K\) need not be Galois. The extension \(L/F\) has Galois group \(P\), so its reciprocity isomorphism is proved by the solvable case. Norm functoriality says that the image of

\[
N_{F/K}:A_F/N_{L/F}A_L\longrightarrow Q
\]

is contained in the image of \(r_{L/K}\). Inclusion also defines a map \(i:Q\to A_F/N_{L/F}A_L\): every norm from \(L/K\) is a norm from \(L/F\), by the right-coset decomposition in Proposition 4.4. On these quotients,

\[
N_{F/K}i=[F:K].
\tag{7}
\]

The integer \([F:K]\) is prime to \(p\). Multiplication by it is an automorphism of \(Q_p\), since an inverse modulo \(p^{b_p}\) acts as its inverse there. Equation (7) therefore puts all of \(Q_p\) in the image of \(N_{F/K}\), hence in the image of reciprocity. Do this for every \(p\mid m\); the primary decomposition proves surjectivity onto all of \(Q\). No solvability assumption on \(T\) was used. Together with injectivity, this proves (6). \(\square\)

The argument also proves finiteness of \(Q\) in the general case. Finiteness was not silently assumed when taking its primary parts.

## 5. The norm residue symbol

Define the **norm residue symbol** by taking the inverse of (6):

\[
(\ ,L/K):A_K\longrightarrow\operatorname{Gal}(L/K)^{\mathrm{ab}},
\qquad \ker(\ ,L/K)=N_{L/K}A_L.
\tag{8}
\]

In additive notation the symbol is a homomorphism; in multiplicative arithmetic notation it sends a product of elements to a product of automorphisms.

### Proposition 5.2. Functoriality of the symbol

For finite Galois \(L/K,L'/K'\) with \(K\subset K'\), \(L\subset L'\), and \(a'\in A_{K'}\),

\[
(N_{K'/K}a',L/K)
=\operatorname{res}_{L'/L}(a',L'/K').
\tag{9}
\]

Conjugation by \(g\in G\) gives

\[
(ga,gL/gK)=g(a,L/K)g^{-1}.
\tag{10}
\]

For \(K'\subset L\) and \(a\in A_K\subset A_{K'}\),

\[
(a,L/K')=\operatorname{Ver}_{\operatorname{Gal}(L/K')}^{\operatorname{Gal}(L/K)}(a,L/K).
\tag{11}
\]

**Proof.** Each identity is the corresponding equality of Proposition 4.4, composed with the inverse reciprocity isomorphisms. The quotient norm, conjugation and inclusion were proved well defined there. Thus these equalities hold for every representative in the stated modules, not merely for a chosen prime element. \(\square\)

For an unramified extension of degree \(n\), Proposition 4.3 gives the useful expression

\[
(a,L/K)=\varphi_{L/K}^{\,v_K(a)\bmod n}.
\tag{12}
\]

The exponent is the image in \(V/nV\simeq\mathbf Z/n\mathbf Z\). It need not come from an integer-valued valuation before reduction.

## 6. Norm limitation

### Theorem 5.4. Only the maximal abelian subextension is seen by norms

For any finite separable \(L/K\), let \(B=L\cap K^{\mathrm{ab}}\). Then

\[
N_{L/K}A_L=N_{B/K}A_B.
\tag{13}
\]

**Proof.** First suppose \(L/K\) is Galois. The left side is contained in the right by norm transitivity. Theorem 5.1 gives the same finite index \(|\operatorname{Gal}(L/K)^{\mathrm{ab}}|=[B:K]\) for both subgroups, proving equality.

For a general finite separable extension, choose its finite Galois closure \(E/K\). Put \(G=\operatorname{Gal}(E/K)\), \(H=\operatorname{Gal}(E/L)\), and let \(G'\) be the commutator subgroup. The group \(G'H\) is normal: it is the inverse image of the subgroup \(\overline H\) of the abelian quotient \(G/G'\). Its fixed field lies in \(L\) and is abelian over \(K\). Conversely, any abelian intermediate field inside \(L\) has a fixing subgroup containing both \(H\) and \(G'\), hence containing \(G'H\). Thus \(B=E^{G'H}\).

Use the already proved isomorphism
\[
r_{E/K}:G/G'\xrightarrow{\sim}
A_K/N_{E/K}A_E.
\]
The Galois extension \(E/L\) has group \(H\), even though \(L/K\) need not be Galois. Surjectivity of \(r_{E/L}\), and norm functoriality from Proposition 4.4, show that
\[
\frac{N_{L/K}A_L}{N_{E/K}A_E}
=r_{E/K}(\overline H).
\]
Indeed every element of \(A_L/N_{E/L}A_E\) is the reciprocity image of an element of \(H\), and its norm to \(K\) is the reciprocity image of that same element in \(G/G'\). This proves both inclusions in the displayed equality.

Apply the identical argument to the Galois extension \(E/B\), whose group is \(G'H\). Its image in \(G/G'\) is exactly \(\overline H\), so
\[
\frac{N_{B/K}A_B}{N_{E/K}A_E}
=r_{E/K}(\overline H)
=\frac{N_{L/K}A_L}{N_{E/K}A_E}.
\]
Both norm subgroups contain \(N_{E/K}A_E\), by norm transitivity. Equality of their images in this quotient is therefore equality of the subgroups themselves. No reciprocity map for a nonnormal extension was presumed. \(\square\)

For a nonabelian Galois extension, its full degree can therefore exceed the norm index. More generally the norm index of a finite separable extension is \([B:K]\), which need not equal \([L:K]\). For example, if a nonnormal cubic extension has Galois closure with group \(S_3\), its subgroup \(H\) has order two and \(G'H=S_3\); thus \(B=K\) and its norm subgroup is all of \(A_K\). The quadratic subfield of the Galois closure has a different norm subgroup. Passing to a Galois closure alone does not preserve the norm subgroup.

## 7. The class field correspondence

For finite abelian \(L/K\), abbreviate \(N_L=N_{L/K}A_L\). Equip \(A_K\) with the **norm topology**, whose basic neighborhoods of zero are the norm subgroups of finite Galois extensions. This is a group topology: the norm subgroup from a compositum is contained in each of the two given norm subgroups by norm transitivity, so the basic neighborhoods are directed under intersection. Translates supply neighborhoods of other elements. By norm limitation the same basis is obtained using only finite abelian extensions. A subgroup is open precisely when it contains one of these basic subgroups.

### Theorem 5.3. The correspondence

The assignment \(L\mapsto N_L\) is a bijection between finite abelian extensions of \(K\) in the fixed separable closure and open subgroups of \(A_K\) in its norm topology. Moreover,

\[
\begin{aligned}
L_1\subset L_2&\quad\Longleftrightarrow\quad N_{L_1}\supset N_{L_2},\\
N_{L_1L_2}&=N_{L_1}\cap N_{L_2},\\
N_{L_1\cap L_2}&=N_{L_1}+N_{L_2}.
\end{aligned}
\tag{14}
\]

In multiplicative notation the last sum is the product \(N_{L_1}N_{L_2}\). If \(N_L\subset H\subset A_K\), there is a unique intermediate field \(M\subset L\) with \(H=N_M\).

**Proof.** Norm transitivity gives \(N_{L_1L_2}\subset N_{L_1}\cap N_{L_2}\). Conversely, an element of both subgroups has symbol in \(\operatorname{Gal}(L_1L_2/K)\) restricting trivially to both fields, by (9). Those restrictions determine the automorphism on the compositum, so the symbol is trivial and the element belongs to \(N_{L_1L_2}\). This proves the intersection formula.

Containment \(L_1\subset L_2\) implies the reverse norm containment by transitivity. If \(N_{L_1}\supset N_{L_2}\), the intersection formula says \(N_{L_1L_2}=N_{L_2}\). Theorem 5.1 gives \([L_1L_2:K]=[L_2:K]\), hence \(L_1\subset L_2\). This proves order reversal and injectivity.

Let \(H\) contain \(N_L\) for an abelian \(L/K\). Under the isomorphism \(A_K/N_L\simeq T=\operatorname{Gal}(L/K)\), its image is a subgroup \(D\subset T\). Let \(M=L^D\). Restriction in (9) identifies the symbol for \(M/K\) with the quotient map \(T\to T/D\). Since \(H\) contains its original kernel \(N_L\), it is the full preimage of \(D\), hence exactly the kernel \(N_M\). Uniqueness follows from order reversal. Every open subgroup contains a norm subgroup, and norm limitation permits choosing that subgroup from an abelian extension. Thus the correspondence is surjective onto the open subgroups.

Finally let \(H=N_{L_1}+N_{L_2}\), which contains a norm subgroup and is open. Write \(H=N_M\) by the result just proved. Since \(H\supset N_{L_i}\), order reversal gives \(M\subset L_1\cap L_2\), hence \(N_M\supset N_{L_1\cap L_2}\). The opposite containment follows because \(L_1\cap L_2\subset L_i\) implies \(N_{L_1\cap L_2}\supset N_{L_i}\). These two containments give the sum formula in (14). \(\square\)

This abstract theorem does not say that every finite-index subgroup for an unrelated preexisting topology is a norm subgroup. The norm topology is the topology just defined. Later existence theorems identify its open subgroups in the usual arithmetic topologies.

## 8. The universal symbol and an example

As finite abelian \(L/K\) vary, the symbols are compatible under restriction by (9). The profinite correspondence in the first lesson identifies their inverse-limit Galois group with \(\operatorname{Gal}(K^{\mathrm{ab}}/K)\). Therefore they define the **universal norm residue symbol**

\[
(\ ,K^{\mathrm{ab}}/K):A_K\longrightarrow
\operatorname{Gal}(K^{\mathrm{ab}}/K).
\tag{15}
\]

Its kernel is \(\bigcap_L N_L\), the subgroup of universal norms. Its image is dense: for any finite set of quotient conditions, take their finite compositum and use the surjectivity of its finite symbol. Surjectivity onto the whole inverse limit requires an additional argument in an arithmetic application; it does not follow just from the finite quotient surjections. Formula (12) gives on the unramified tower

\[
(a,\widetilde K/K)=\varphi_K^{v_K(a)},
\qquad d_K(a,\widetilde K/K)=v_K(a),
\tag{16}
\]

where the exponent is profinite. Equality follows by reducing it modulo every positive integer.

For the finite-field degree formation, \(A_K=\mathbf Z\), all actions are trivial, and a degree-\(n\) extension has norm \(n\mathbf Z\). The cyclic Tate groups are \(\mathbf Z/n\mathbf Z\) and zero, so (1) holds. The correspondence sends \(\mathbf F_{q^{mn}}/\mathbf F_{q^m}\) to \(n\mathbf Z\). Compositum and intersection have relative degrees \(\operatorname{lcm}(n_1,n_2)\) and \(\gcd(n_1,n_2)\), matching intersection and sum of these subgroups. Its universal symbol is the dense inclusion \(\mathbf Z\to\widehat{\mathbf Z}\); it is not surjective. This is a concrete reason to keep density and surjectivity distinct in (15).

## Exercises

1. **Easy.** Deduce \(N_{L_1L_2}=N_{L_1}\cap N_{L_2}\) for two finite abelian extensions directly from Theorem 5.1 and restriction of symbols.
2. **Medium.** Prove norm limitation for a finite Galois extension, and explain why its norm index is the order of the abelianization rather than its full degree.
3. **Medium.** If \(L/K\) is finite abelian and \(N_L\subset H\subset A_K\), construct the unique \(M\subset L\) with \(H=N_M\).
4. **Hard.** Carry out the Sylow step for \(T=\operatorname{Gal}(L/K)\simeq S_3\). Treat separately the subgroups of orders 2 and 3; identify the resulting norm quotient and the maximal abelian subfield.

## Solutions

1. Transitivity gives the inclusion from the compositum's norm subgroup into each factor. If \(a\) is in both factors, its symbol in the compositum has identity restriction to both \(L_1,L_2\). An automorphism fixing both fixes the field they generate, so that symbol is identity. The kernel assertion of Theorem 5.1 places \(a\) in \(N_{L_1L_2}\), proving equality.
2. Let \(B\) be the fixed field of \(T'\). Norm transitivity gives \(N_L\subset N_B\). Theorem 5.1 computes \([A_K:N_L]=|T/T'|=[B:K]=[A_K:N_B]\). These finite indices force the contained subgroups to be equal. Thus when \(T\) is nonabelian the quotient records exactly its maximal abelian quotient, and its index can be strictly smaller than \(|T|\).
3. Map \(H\) into \(T\) by the surjective symbol for \(L/K\), and call its image \(D\). Set \(M=L^D\). Restriction identifies the symbol for \(M/K\) with the quotient by \(D\). Because \(H\supset N_L\), it equals the full preimage of \(D\), hence the kernel \(N_M\). If \(M'\) also has that norm subgroup, the order-reversing part of Theorem 5.3 gives \(M\subset M'\) and \(M'\subset M\), so \(M=M'\).
4. The quotient \(Q=A_K/N_{L/K}A_L\) is killed by 6 and decomposes as \(Q_2\oplus Q_3\). For \(P_2=\langle(12)\rangle\), the fixed field \(F_2\) has degree 3 over \(K\) and need not be Galois. Cyclic reciprocity gives \(A_{F_2}/N_{L/F_2}A_L\simeq C_2\). Inclusion followed by norm acts on \(Q\) as multiplication by 3, which is an automorphism on \(Q_2\); thus \(Q_2\) lies in this norm's image and hence in the image of the transposition under \(r_{L/K}\). For \(P_3=A_3\), the fixed field \(F_3\) has degree 2 over \(K\), and \(L/F_3\) is cyclic of degree 3. Its norm map onto \(Q\), composed with inclusion, is multiplication by 2, an automorphism on \(Q_3\). However its image under reciprocity is zero: the 3-cycles lie in the commutator subgroup of \(S_3\). Indeed, sign gives an abelian quotient \(C_2\), while the commutator of two distinct transpositions is a 3-cycle, proving \(S_3'=A_3\). Thus \(Q_3=0\). Restriction to the quadratic field \(F_3=L^{A_3}\) identifies \(T^{\mathrm{ab}}\) with \(C_2\), and cyclic reciprocity there makes the transposition's class nonzero in \(Q\). Consequently \(Q\simeq C_2\) and \(N_{L/K}A_L=N_{F_3/K}A_{F_3}\). This also shows explicitly why neither the degree-6 field nor its non-Galois cubic fixed field may be substituted for the maximal abelian subfield in norm limitation.

## Editable edition

The reading edition provides the complete LaTeX source of this lesson, the cumulative course LaTeX and the editable source ZIP. The archive contains all twenty-four Markdown lessons, complete LaTeX bodies, original diagrams, metadata and reproduction instructions.

## References

Sections 1–4 prove the cyclic, abelian, solvable and Sylow steps without assuming a finite norm quotient prematurely. Theorem 5.4 proves norm limitation for every finite separable extension, using its maximal abelian subextension. Sections 7–8 prove the norm-group correspondence, its topology and the universal symbol.

- [Kiran S. Kedlaya, Notes on class field theory, author-hosted HTML edition](https://kskedlaya.org/cft/sec_abstractcft1.html).

The [proof guide](../FREE_PROOFS.md) gives the lesson sequence and the exact prerequisite record. External references accompany the written arguments.
