# Mackey theory and Clifford's theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the AI that wrote it. Public domain (CC0).*

Induction assembles a representation from coset copies. When we restrict that representation to a second subgroup, some copies can move into one another and some cannot. The resulting blocks are indexed by double cosets. Mackey's formula describes each block and turns irreducibility into a question about representations of intersections.

A normal subgroup gives a different kind of structure. Its irreducible types inside an irreducible representation of the whole group form one conjugacy orbit. Clifford's theorem identifies their common multiplicity, and Clifford's correspondence reconstructs the representation from one isotypic component and its stabilizer. The component can contain several copies of its subgroup type.

All groups here are finite, all vector spaces are finite-dimensional over \(\mathbb C\), and all modules are left modules. We use the two natural adjunctions, the tensor construction and its coset decomposition from [Induced representations and Frobenius reciprocity](RT-FIN-06.md), Propositions 2.1 and 4.1 and Theorem 3.1. Complete reducibility, Schur's lemma and intrinsic isotypic components are proved in [Representations and complete reducibility](RT-FIN-01.md), Theorems 2.3 and 3.1 and Proposition 4.2. Character inner products are linear in the first variable. Basic references for the induction formulas are [Gruson–Serganova 2018]; the normal-subgroup theorem is due to [Clifford 1937].

## 1. Blocks that a subgroup can reach

For \(H,K\le G\), a **double coset** is a subset \(KsH\). Two such subsets are equal or disjoint: if \(k_1sh_1=k_2th_2\), then \(s\in KtH\), and multiplication on either side gives both inclusions. They therefore partition \(G\). The set of blocks is denoted \(K\backslash G/H\).

There is an equivalent description that explains their role in induction. The left \(K\)-orbits on \(G/H\) are exactly the collections of cosets contained in one \(KsH\). The stabilizer in \(K\) of \(sH\) is

\[
J_s=K\cap sHs^{-1}.
\tag{1}
\]

Indeed, \(ksH=sH\) if and only if \(s^{-1}ks\in H\). The map \(kJ_s\mapsto ksH\) identifies \(K/J_s\) with this orbit.

Let \(W\) be an \(H\)-representation with action \(\rho\). On the same vector space define

\[
W^s(x)=\rho(s^{-1}xs),\qquad x\in sHs^{-1}.
\tag{2}
\]

We use the same notation for its restriction to \(J_s\), specifying the acting group when needed.

**Theorem 1.1 (Mackey's restriction formula).** Choose one representative \(s\) of each double coset. There is a \(K\)-isomorphism

\[
\operatorname{Res}_K^G\operatorname{Ind}_H^G W
\simeq
\bigoplus_{s\in K\backslash G/H}
\operatorname{Ind}_{J_s}^K(W^s|_{J_s}).
\tag{3}
\]

**Proof.** In the coset decomposition of \(\mathbb C[G]\otimes_{\mathbb C[H]}W\), group together the copies indexed by the cosets in one \(KsH\). Its subspace

\[
B_s=\mathbb C[KsH]\otimes_{\mathbb C[H]}W
\]

is \(K\)-invariant, and the different subspaces give a direct sum. Define

\[
\begin{aligned}
\Phi_s:\mathbb C[K]\otimes_{\mathbb C[J_s]}W^s&\longrightarrow B_s,\\
k\otimes w&\longmapsto ks\otimes w.
\end{aligned}
\tag{4}
\]

For \(j\in J_s\), the two balanced inputs give

\[
kjs\otimes w
=ks(s^{-1}js)\otimes w
=ks\otimes\rho(s^{-1}js)w.
\]

Thus the map is well-defined. It commutes with left \(K\)-multiplication. Every tensor from the double coset has first factor \(ksh\), and its image equals \(ks\otimes hw\), so the map is surjective.

Choose representatives \(Q_s\) of \(K/J_s\). The cosets \(qsH\), for \(q\in Q_s\), are distinct and exhaust the \(K\)-orbit of \(sH\). On the corresponding decompositions, (4) maps each copy \(q\otimes W\) identically to the copy \(qs\otimes W\). It is therefore injective and gives the explicit inverse on these copies. Summing (4) proves (3). The maps commute with every \(H\)-intertwiner \(W\to W'\), giving naturality. \(\square\)

The choice of representatives describes the summands; the \(K\)-invariant block for a double coset does not depend on that choice. For example, replacing \(s\) by \(k_0sh_0\) merely changes the basis and the identification of its stabilizer.

The dimensions provide a useful independent check:

\[
[G:H]=\sum_s[K:J_s].
\tag{5}
\]

This equality counts the cosets in the separate \(K\)-orbits. Multiplying by \(\dim W\) gives the dimension identity in (3).

**Corollary 1.2 (intertwining numbers).** Let \(Z\) be a \(K\)-representation, with character \(\phi\), and let \(\psi=\chi_W\). Then

\[
\begin{aligned}
\operatorname{Hom}_G(\operatorname{Ind}_H^G W,\operatorname{Ind}_K^G Z)
&\simeq
\bigoplus_s
\operatorname{Hom}_{J_s}(W^s|_{J_s},Z|_{J_s}),\\
\left\langle\operatorname{Ind}_H^G\psi,\operatorname{Ind}_K^G\phi\right\rangle_G
&=\sum_s
\left\langle\psi^s|_{J_s},\phi|_{J_s}\right\rangle_{J_s}.
\end{aligned}
\tag{6}
\]

**Proof.** The adjunction with an induced target changes the first Hom space to
\(\operatorname{Hom}_K(\operatorname{Res}_K\operatorname{Ind}_H W,Z)\).
Substitute (3), and use the adjunction with an induced source on each summand. This gives the first line of (6). Taking dimensions and using the character–Hom identity gives the second. Characters span the class-function spaces, so the second line extends by linearity and conjugate linearity to arbitrary class functions on \(H\) and \(K\). \(\square\)

## 2. When the coset copies form one irreducible

Representations of a group are **disjoint** if they have no common irreducible constituent. By complete reducibility and Schur's lemma, this is equivalent to a zero Hom space, or to an inner product of characters equal to zero.

**Theorem 2.1 (Mackey's irreducibility criterion).** For \(W\ne0\), the representation \(\operatorname{Ind}_H^G W\) is irreducible if and only if:

- \(W\) is irreducible;
- for every \(s\notin H\), the representations \(W^s\) and \(W\), restricted to \(H\cap sHs^{-1}\), are disjoint.

It suffices to check the second condition on representatives of the nonidentity double cosets in \(H\backslash G/H\).

**Proof.** Apply (6) with \(K=H\) and \(Z=W\), choosing \(1\) for the double coset \(H\). It gives

\[
\dim\operatorname{End}_G(\operatorname{Ind}_H^G W)
=\dim\operatorname{End}_H(W)
+\sum_{s\ne1}
\dim\operatorname{Hom}_{H\cap sHs^{-1}}(W^s,W).
\tag{7}
\]

For any nonzero semisimple complex representation \(\bigoplus_i V_i^{\oplus m_i}\), its endomorphism dimension is \(\sum_i m_i^2\). It equals one exactly for an irreducible representation. All terms in (7) are nonnegative integers, and its first term is at least one. Thus the left side is one exactly when the first term is one and all remaining terms vanish. These are the two conditions.

To justify checking all \(s\notin H\), let \(s'=h_1sh_2\), with \(h_1,h_2\in H\). Its intersection subgroup is the conjugate by \(h_1\) of \(H\cap sHs^{-1}\). Transporting both representations along that conjugation and applying the \(H\)-operators for \(h_1,h_2\) identifies their Hom spaces. Hence vanishing depends only on the double coset. \(\square\)

**Corollary 2.2 (normal-subgroup criterion).** If \(H\triangleleft G\), then

\[
\operatorname{Res}_H^G\operatorname{Ind}_H^G W
\simeq\bigoplus_{s\in G/H}W^s.
\tag{8}
\]

For irreducible \(W\), its induction is irreducible exactly when \(W^s\not\simeq W\) for every \(s\notin H\).

**Proof.** In (3) take \(K=H\). Normality makes every \(J_s=H\) and identifies double cosets with cosets. The criterion now compares irreducible representations of all of \(H\), so Schur's lemma turns disjointness into nonisomorphism. \(\square\)

For a nonnormal subgroup, the intersection in Theorem 2.1 is essential. If it is the trivial group for some nonidentity double coset, any two nonzero restrictions have a common trivial constituent, so induction cannot be irreducible.

For instance, \(H=\langle(12)\rangle\le S_3\) has double cosets represented by \(1\) and \((13)\); the latter intersection is trivial. Inducing either of its linear characters is reducible. For the nontrivial character the two terms in (7) are \(1\) and \(1\), consistent with the decomposition into the sign line and the standard plane.

## 3. A normal subgroup's types move together

Let \(N\triangleleft G\). Conjugation acts on isomorphism classes of irreducible \(N\)-representations by (2). Since \((W^t)^s=W^{st}\), this is a left action. An element of \(N\) fixes every class: its operator in \(W\) intertwines the inner-conjugate representation with \(W\).

For an irreducible \(N\)-representation \(W\), define its **inertia group**

\[
I=I_G(W)=\{g\in G:W^g\simeq W\}.
\tag{9}
\]

It is a subgroup containing \(N\). For a \(G\)-representation \(V\), let \(V[W]\) denote the intrinsic \(W\)-isotypic component of its restriction to \(N\): the sum of all \(N\)-submodules isomorphic to \(W\).

**Theorem 3.1 (Clifford's theorem).** If \(V\) is an irreducible \(G\)-representation and \(W\) is a constituent of \(\operatorname{Res}_N^G V\), then

\[
\operatorname{Res}_N^G V
\simeq\bigoplus_{j=1}^t W_j^{\oplus e},
\qquad e\ge1,\qquad t=[G:I_G(W)],
\tag{10}
\]

where the \(W_j\) are precisely the distinct \(G\)-conjugates of \(W\). In particular,

\[
\dim V=e[G:I_G(W)]\dim W.
\tag{11}
\]

**Proof.** Complete reducibility over \(N\) gives its intrinsic isotypic decomposition. If \(U\subset V\) has type \(W\), then for \(g\in G\),

\[
n(gu)=g(g^{-1}ng)u,\qquad n\in N.
\tag{12}
\]

Thus \(gU\) has type \(W^g\), and \(gV[W]=V[W^g]\). The equality follows by applying the same inclusion with \(g^{-1}\). Consequently \(G\) permutes the nonzero components.

The sum of all components in any one orbit is a nonzero \(G\)-invariant subspace. Irreducibility makes it all of \(V\), so there is exactly one orbit. The stabilizer of the component \(V[W]\) is exactly \(I_G(W)\), because distinct nonzero isotypic components have distinct types. The orbit therefore has \([G:I_G(W)]\) members.

The maps \(g:V[W]\to V[W^g]\) are vector-space isomorphisms. They preserve the dimension of the component; all conjugate irreducibles also have the same dimension. Dividing the component dimension by \(\dim W\) shows that every multiplicity is the same positive integer \(e\). This proves (10) and (11). \(\square\)

The assertion has two separate parts: all types belong to one orbit, and every type has the same multiplicity. It does not assert that the multiplicity is one.

For example, the irreducible degree-two representation of \(Q_8\), restricted to its center \(N=\{1,-1\}\), is two copies of the character taking \(-1\) to \(-1\). There is one type, \(I=Q_8\), and \(e=2\). This linear character of the center does not extend to a linear character of \(Q_8\): the element \(-1=[i,j]\) is a commutator, whereas every linear character kills commutators. No extension assumption will enter the next theorem.

## 4. Recovering the whole representation from one component

Say that an irreducible representation **lies over** \(W\) if its restriction to \(N\) contains \(W\).

**Theorem 4.1 (Clifford correspondence).** Fix \(W\in\operatorname{Irr}(N)\) and put \(I=I_G(W)\). Induction gives a bijection

\[
\left\{\begin{array}{c}
\text{irreducible }I\text{-representations}\\
\text{lying over }W
\end{array}\right\}
\longleftrightarrow
\left\{\begin{array}{c}
\text{irreducible }G\text{-representations}\\
\text{lying over }W
\end{array}\right\}.
\tag{13}
\]

Its inverse is \(V\mapsto V[W]\), with the inherited \(I\)-action. Both sets are sets of isomorphism classes.

**Proof, from \(G\) to \(I\).** Let \(V\) be irreducible over \(G\), lying over \(W\), and put \(U=V[W]\). Formula (12) makes \(U\) \(I\)-invariant. Choose representatives \(T\) of \(G/I\), including \(1\). Theorem 3.1 gives

\[
V=\bigoplus_{t\in T}tU,
\tag{14}
\]

where the summands have pairwise distinct \(N\)-types \(W^t\).

If \(0\ne L\subset U\) is an \(I\)-submodule, then \(\sum_{t\in T}tL\) is a \(G\)-submodule: for \(a\in G\), write \(at=t'i\), and use \(iL=L\). It is nonzero, hence all of \(V\). Intersecting this sum with the component \(U\) gives exactly \(L\), since all other summands have distinct \(N\)-types. Therefore \(L=U\). This proves that \(U\) is irreducible over \(I\).

Define

\[
\operatorname{Ind}_I^G U\longrightarrow V,
\qquad g\otimes u\longmapsto gu.
\tag{15}
\]

The map respects balancing and the \(G\)-action. It identifies its separate coset copies with the summands in (14), so it is an isomorphism.

**Proof, from \(I\) to \(G\).** Let \(U\) be irreducible over \(I\), lying over \(W\). Apply Theorem 3.1 to \(N\triangleleft I\). All \(I\)-conjugates of \(W\) are isomorphic to \(W\), by the definition of \(I\). Hence

\[
\operatorname{Res}_N^I U\simeq W^{\oplus e}.
\tag{16}
\]

For \(s\notin I\), the group \(J_s=I\cap sIs^{-1}\) contains \(N\). The restrictions of \(U\) and \(U^s\) to \(N\) have respectively the distinct types \(W\) and \(W^s\). Thus an intertwiner between their \(J_s\)-restrictions must be zero: it would already be an \(N\)-intertwiner between disjoint types. Theorem 2.1 shows that \(\operatorname{Ind}_I^G U\) is irreducible.

Its restriction to \(N\) has one coset component of type \(W^t\) for each \(tI\), with multiplicity \(e\). This follows from (3) with \(K=N,H=I\); normality and \(N\subset I\) make the relevant double cosets \(G/I\). Only the identity coset has type \(W\), since \(W^t\simeq W\) precisely when \(t\in I\). Therefore its \(W\)-isotypic component is the original \(U\).

The two constructions undo one another. A \(G\)-isomorphism preserves the intrinsic \(W\)-component, and an \(I\)-isomorphism induces a \(G\)-isomorphism, so this is a bijection on isomorphism classes. \(\square\)

The \(I\)-module in (13) has dimension \(e\dim W\). It is an actual representation of \(I\), obtained from the whole isotypic component. Replacing it by one chosen copy of \(W\) would generally lose its \(I\)-action.

## 5. Abelian normal subgroups and degree divisibility

When \(N\) is abelian, its irreducibles are linear characters. Formula (11) gives \(\dim V=e[G:I]\). The remaining factor \(e\) need not be one, but it divides \([I:N]\).

**Theorem 5.1 (Itô's degree divisibility theorem).** If \(N\triangleleft G\) is abelian and \(V\) is an irreducible complex representation, then

\[
\dim V\mid [G:N].
\tag{17}
\]

**Proof.** Let \(\lambda\) be a constituent over \(N\), let \(I=I_G(\lambda)\), and let \(U=V[\lambda]\). Theorem 4.1 makes \(U\) irreducible over \(I\), and \(N\) acts on it by the scalar \(\lambda(n)\). Put \(K=\ker\lambda\), as a subgroup of \(N\).

Since \(\lambda\) is invariant under \(I\), the subgroup \(K\) is normal in \(I\). For \(i\in I,n\in N\), invariance gives

\[
\lambda(ini^{-1}n^{-1})=1.
\]

Consequently \(N/K\subset Z(I/K)\). The representation \(U\) factors through the finite group \(I/K\) and remains irreducible. The central refinement of degree divisibility, proved in Theorem 2.2 of [Integrality of characters and Burnside's theorem](RT-FIN-05.md), gives

\[
\dim U\mid [I/K:Z(I/K)]\mid[I/K:N/K]=[I:N].
\tag{18}
\]

Here \(\dim U=e\), because \(\lambda\) is one-dimensional. Finally \(\dim V=[G:I]\dim U\), by (15), and multiplying the divisibility in (18) by \([G:I]\) proves (17). \(\square\)

This proof uses scalar action after quotienting by its kernel. It does not require \(N\) itself to be central, nor does it assume that \(\lambda\) extends to \(I\).

For a split group \(G=N\rtimes H\), write \(H_\lambda\) for the stabilizer of \(\lambda\) in \(H\). Then \(I=N\rtimes H_\lambda\). In this situation there is an explicit extension

\[
\widetilde\lambda(nh)=\lambda(n),\qquad n\in N,\ h\in H_\lambda.
\tag{19}
\]

Indeed the multiplication rule \(n_1h_1n_2h_2=n_1(h_1n_2h_1^{-1})h_1h_2\), together with \(H_\lambda\)-invariance, makes (19) multiplicative. Tensoring an irreducible \(U\) over \(\lambda\) with \(\widetilde\lambda^{-1}\) makes \(N\) act trivially. Thus it is the inflation of an irreducible representation \(T\) of \(H_\lambda\), and

\[
U\simeq\widetilde\lambda\otimes T,\qquad
\dim V=[H:H_\lambda]\dim T.
\tag{20}
\]

Ordinary degree divisibility for \(H_\lambda\) now proves that this degree divides \(|H|=[G:N]\). The following lesson develops (20) into a complete classification.

## 6. Orbits in small groups

### The tetrahedral group from its four-element normal subgroup

Let \(N=V_4\triangleleft A_4\), whose three nonidentity elements are
\((12)(34),(13)(24),(14)(23)\). Conjugation by \((123)\) cycles these elements. A nontrivial linear character \(\nu\) of \(V_4\) has an order-two kernel, so the same conjugation cycles the three nontrivial characters. Its inertia group in \(A_4\) is therefore \(V_4\).

Corollary 2.2 proves that

\[
R=\operatorname{Ind}_{V_4}^{A_4}\nu
\tag{21}
\]

is irreducible of dimension three. It vanishes on 3-cycles because its inducing subgroup is normal. On \(V_4\), its character is the sum of all three nontrivial linear characters. This sum is \(3\) at the identity and \(-1\) at every other element: including the trivial character gives the regular character of \(V_4\), which is zero off the identity. Hence the row of \(R\) is

\[
(3,-1,0,0)
\]

on \(1\), the double transpositions and the two 3-cycle classes.

The quotient \(A_4/V_4\simeq C_3\) supplies the three linear characters \(1,\alpha,\alpha^2\). Together with \(R\), their degree squares total \(1+1+1+9=12\), so they exhaust \(\operatorname{Irr}(A_4)\). Their restrictions to \(V_4\) have respectively one copy of the trivial character or one copy of each member of the nontrivial three-character orbit.

### Two normal subgroups in \(S_4\)

Use the irreducibles \(1,\mathrm{sign},U,W,W\otimes\mathrm{sign}\) constructed in the preceding lesson, of degrees \(1,1,2,3,3\). Their restrictions to \(A_4\) are

\[
\begin{array}{c|c|c|c}
S_4\text{-representation}&A_4\text{-restriction}&e&t\\ \hline
1&1&1&1\\
\mathrm{sign}&1&1&1\\
U&\alpha\oplus\alpha^2&1&2\\
W&R&1&1\\
W\otimes\mathrm{sign}&R&1&1
\end{array}
\tag{22}
\]

This follows by restricting the earlier character rows and using character determination; Exercise 1 gives the entries explicitly. In particular the two linear types in \(U\) are interchanged by an odd permutation, and each has inertia group \(A_4\).

Restricting further to \(V_4\) gives

\[
1|_{V_4}=\mathrm{sign}|_{V_4}=1,\qquad
U|_{V_4}=1^{\oplus2},\qquad
W|_{V_4}=(W\otimes\mathrm{sign})|_{V_4}
=\nu_1\oplus\nu_2\oplus\nu_3.
\tag{23}
\]

The representation \(U\) now has \(e=2,t=1\). The two degree-three representations have \(e=1,t=3\). Thus even an abelian normal subgroup permits multiplicity greater than one.

For a nontrivial \(\nu\) whose kernel is \(\{1,(13)(24)\}\), its inertia group in \(S_4\) is the centralizer of \((13)(24)\): preserving its kernel means fixing that element by conjugation. This centralizer has order \(8\) and equals

\[
I=\langle r=(1234),s=(13)\rangle\simeq D_4.
\]

The linear character \(\eta(r)=-1,\eta(s)=1\) restricts to this \(\nu\), since its values on \(r^2,rs,r^3s\) are \(1,-1,-1\). The construction \(W=\operatorname{Ind}_I^{S_4}\eta\) from the preceding lesson is therefore an explicit instance of Theorem 4.1. The sign twist gives the corresponding inertia representation for \(W\otimes\mathrm{sign}\).

### The rotation subgroup in a dihedral group

For \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\), put \(N=\langle r\rangle\) and \(\theta_k(r)=e^{2\pi i k/n}\). Reflection sends \(\theta_k\) to \(\theta_{-k}\). If \(2k\not\equiv0\pmod n\), its inertia group is \(N\), and induction is irreducible of degree two. If \(2k\equiv0\pmod n\), its inertia group is all of \(D_n\), and the induced representation is reducible. The two eigenspaces of the reflection give its two linear constituents, as shown by the explicit matrices in the preceding lesson.

This recovers every odd and even dihedral case. For \(n=1,2\), every rotation character is invariant, so there are only the linear cases.

## 7. Exercises with complete solutions

### Exercise 1. See the orbit and the multiplicity separately

Compute the restrictions of every irreducible of \(S_4\) to \(A_4\). Verify the orbit and equal-multiplicity assertions, and explain what changes upon restricting to \(V_4\).

**Solution.** Order the \(A_4\) classes as \(1,22,3_+,3_-\), with sizes \(1,3,4,4\); choose \(3_+\) so that \(\alpha(3_+)=\omega\), where \(\omega^3=1,\omega\ne1\). The four constructed irreducible rows are

\[
\begin{array}{c|rrrr}
1&1&1&1&1\\
\alpha&1&1&\omega&\omega^2\\
\alpha^2&1&1&\omega^2&\omega\\
R&3&-1&0&0
\end{array}.
\]

The \(S_4\) rows restrict to

\[
(1,1,1,1),\quad(1,1,1,1),\quad
(2,2,-1,-1),\quad(3,-1,0,0),\quad(3,-1,0,0).
\]

Since \(\omega+\omega^2=-1\), these are \(1,1,\alpha+\alpha^2,R,R\). They give (22) by character determination. The \(A_4\)-type \(R\) is fixed under all of \(S_4\), as is the trivial type, so their orbit has one member. The two nontrivial linear types are interchanged by odd permutations and have stabilizer \(A_4\); their orbit has two members. Every listed multiplicity is one.

On \(V_4\), both \(\alpha\) and \(\alpha^2\) are trivial, hence \(U\) becomes two copies of the trivial character. The degree-three row on \(V_4\) is the sum of its three nontrivial characters, by (21). These types are permuted transitively by \(S_4\). Thus \(U\) has \(e=2,t=1\), whereas each degree-three representation has \(e=1,t=3\). The identities \(\dim V=et\dim W\) hold in every case.

### Exercise 2. Follow both adjunctions

Derive the intertwining-number formula (6) directly from Mackey's decomposition and Frobenius reciprocity. Apply it to the sign character of \(\langle(12)\rangle\le S_3\).

**Solution.** Put \(X=\operatorname{Ind}_H^G W\). The right adjunction gives

\[
\operatorname{Hom}_G(X,\operatorname{Ind}_K^G Z)
\simeq\operatorname{Hom}_K(\operatorname{Res}_K^G X,Z).
\]

Mackey's decomposition replaces the source on the right by the sum over \(s\) of \(\operatorname{Ind}_{J_s}^K W^s\). A map from that direct sum is a tuple of maps from its summands. The left adjunction identifies the map space for each summand with \(\operatorname{Hom}_{J_s}(W^s,Z|_{J_s})\). Taking dimensions gives exactly

\[
\sum_s\langle\psi^s|_{J_s},\phi|_{J_s}\rangle_{J_s}.
\]

Both adjunctions are needed because the first induced representation is the source and the second is the target.

For \(H=K=\langle(12)\rangle\) and \(W=Z\) its nontrivial line, the two double-coset representatives are \(1,(13)\). Their intersections have orders \(2,1\). The first Hom dimension is one by Schur's lemma; the second is one because both restrictions to the trivial group are lines. The induced character therefore has squared norm \(2\). Its known decomposition into the sign line and standard plane has precisely this norm.

### Exercise 3. Prove degree divisibility without an extension assumption

Let \(N\triangleleft G\) be abelian. Prove that every irreducible degree divides \([G:N]\). Give a separate proof of the remaining multiplicity divisibility when \(G=N\rtimes H\).

**Solution.** For a constituent \(\lambda\) of \(\operatorname{Res}_N V\), let \(I\) be its inertia group and \(U=V[\lambda]\). Clifford correspondence gives \(\dim V=[G:I]\dim U\), and \(N\) acts on \(U\) by \(\lambda\). Set \(K=\ker\lambda\). Invariance under \(I\) makes \(K\triangleleft I\) and makes every commutator between \(I\) and \(N\) belong to \(K\). Hence \(N/K\) is central in \(I/K\).

The irreducible representation \(U\) descends to \(I/K\). The earlier central-index divisibility theorem gives \(\dim U\mid[I/K:Z(I/K)]\). Since \(N/K\) is contained in this center, that index divides \([I:N]\). Multiplying by \([G:I]\) proves \(\dim V\mid[G:N]\).

In the split case \(I=N\rtimes H_\lambda\), the character \(\widetilde\lambda(nh)=\lambda(n)\) is an extension, as checked in (19). Twisting \(U\) by its inverse kills \(N\), and the resulting irreducible representation factors through \(I/N\simeq H_\lambda\). If it is \(T\), then \(\dim U=\dim T\mid|H_\lambda|\) by ordinary degree divisibility. This again gives \(\dim V=[H:H_\lambda]\dim T\mid|H|\). The split argument constructs the extension; it does not assume one in the general case.

### Exercise 4. A second proof of the correspondence

Prove Theorem 4.1, replacing its use of Mackey's irreducibility criterion by a direct argument with the normal subgroup's isotypic projections.

**Solution.** Let \(U\) be irreducible over \(I\) and lying over \(W\). Its restriction to \(N\) is a multiple of \(W\), by Clifford's theorem applied within \(I\). In \(X=\operatorname{Ind}_I^G U=\bigoplus_{t\in G/I}t\otimes U\), the summands have pairwise distinct types \(W^t\). They are exactly the intrinsic \(N\)-isotypic components.

Suppose \(0\ne L\subset X\) is a \(G\)-submodule. Canonical isotypic projections preserve \(L\): the projections are natural for the \(N\)-equivariant inclusion \(L\hookrightarrow X\), by the earlier isotypic-component theorem. Thus \(L\) is the sum of its intersections with those components. One intersection is nonzero, and translating by its coset representative's inverse shows that \(L\cap(1\otimes U)\ne0\).

This intersection is \(I\)-invariant. Irreducibility of \(U\) forces \(1\otimes U\subset L\). Its \(G\)-translates span \(X\), so \(L=X\). Thus \(X\) is irreducible. Only its identity component has type \(W\), so its \(W\)-component recovers \(U\).

Conversely, for an irreducible \(G\)-representation \(V\) lying over \(W\), set \(U=V[W]\). If \(L\) is a nonzero \(I\)-submodule of \(U\), the direct sum of its coset translates is \(G\)-invariant and therefore all of \(V\). Its \(W\)-component is exactly \(L\), whence \(L=U\). Thus \(U\) is \(I\)-irreducible. The map \(g\otimes u\mapsto gu\) identifies the induction coset copies with all of \(V\)'s isotypic components, hence is a \(G\)-isomorphism. Isomorphisms preserve these intrinsic components, so the two constructions give the asserted bijection on isomorphism classes.

## 8. What this lesson assumes

Mackey's formula and criterion, the normal-subgroup criterion, Clifford's theorem and correspondence, and the abelian-normal degree theorem were proved here. The opening paragraph identifies the exact earlier induction, semisimplicity, Schur and isotypic results used.

The character–Hom formula is Proposition 2.3, and determination by characters is Theorem 3.1, in Characters and the orthogonality relations; the regular degree-square identity used for \(A_4\) is Theorem 3.2 there, and the class-function basis is Theorem 4.1. Theorem 2.2 of [Integrality of characters and Burnside's theorem](RT-FIN-05.md) states both ordinary and central-index degree divisibility. The \(S_4\), \(Q_8\) and dihedral representations referenced in the examples were explicitly constructed in the preceding lessons.

Coset partition and subgroup-orbit counting are proved in [the Fourier lesson, Lemma 6.1](RT-FIN-03.md#lemma-6-1). No assertion that a subgroup type always extends to its inertia group is imported or needed.

## References

- **C. Lassueur**, [*Character Theory of Finite Groups*](https://kluedo.ub.rptu.de/frontdoor/index/index/year/2021/docId/6228), lecture notes, TU Kaiserslautern, 2020, §20, Theorem 20.5, for Clifford's theorem and the Clifford correspondence. The normal-subgroup theorem goes back to A. H. Clifford (1937).
- **C. Gruson and V. Serganova**, *A Journey Through Representation Theory: From Finite Groups to Quivers via Algebras*, 2018, Chapter 2 §7, Theorem 7.4 and Corollary 7.6, and §8, Theorem 8.1 and Corollary 8.2, for Mackey's formulas and criterion.
- **Earlier course proof:** [the Fourier lesson, Lemma 6.1](RT-FIN-03.md#lemma-6-1), for cosets, orbit–stabilizer, centralizers and normalizers.
