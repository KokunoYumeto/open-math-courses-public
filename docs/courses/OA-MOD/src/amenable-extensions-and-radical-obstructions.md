# Amenable extensions and radical obstructions

Amenability survives closed subgroups, normal extensions and increasing unions. These facts give solvable and compact examples. For an almost-connected group they also locate the entire obstruction: the quotient by the connected solvable radical must be compact. We prove this without a countable-base or unimodularity assumption, then apply normal extensions to state-preserving modular averages.

Read Haar amenability and modular averaging first. In particular, AMH01–02 prove equivalence of invariant means on Haar \(L^\infty(G)\), invariant means on bounded uniformly continuous functions, and the compact convex fixed-point property. We use left Haar measure, the locally completed convention of AMH01, and \(L_s f(t)=f(s^{-1}t)\). Write \(\mathrm{UC}(G)\) for functions uniformly continuous under both left and right translation in the supremum norm. No mean is presumed normal.

The structure arguments use exact earlier programme proofs: continuous subgroup averaging, Lemmas 1.1–1.2 and Theorem 2.1, connected second-countable Lie approximation, KT-KK-18 Theorem 12.31 and Lemmas 12.19–12.30, and radical and rank-one structure, Theorems 1A.10, 1C.5, 1C.8 and 1E.1. Section AME04 supplies the unrestricted connected Lie-approximation input to the latter lesson's conditional radical construction. The particular root, compact-representation and finite-dimensional Lie prerequisites are specified in those proofs.

## Passing to a closed subgroup

**Theorem.** Every closed subgroup \(H\) of an amenable locally compact Hausdorff group \(G\) is amenable.

Restriction of ambient measurable classes does not prove this: for example, \(\mathbb R\times\{0\}\) has zero two-dimensional Haar measure. Instead we transfer continuous functions by a probability kernel.

Put \(Q=H\backslash G\), \(q(g)=Hg\). The quotient is locally compact Hausdorff and \(q\) is open. Here \(Hg\) is an orbit for left multiplication by \(H\). Lemmas 1.1–1.2 of the continuous-averaging lesson prove that there is continuous \(\chi\geq0\) with

\[
\int_H\chi(h^{-1}g)\,dh=1,
\qquad
\operatorname{supp}\chi\cap q^{-1}(C)\ \text{compact}
\tag{AME.1}
\]

for every compact \(C\subset Q\). Their construction works without countability: an open sigma-compact subgroup of \(G\) partitions \(Q\) into clopen sigma-compact orbits for its right action; compact annuli give locally finite partitions of unity on each orbit. For \(\psi\in C_c(G)_+\), the function

\[
\beta_\psi(g)=\int_H\psi(h^{-1}g)\,dh
\]

is continuous and constant on \(H\)-orbits. The positive sets of these functions cover \(Q\). A subordinate partition \((\eta_i)\) gives

\[
\chi(g)=\sum_i
\frac{\eta_i(q(g))\psi_i(g)}{\beta_{\psi_i}(g)}.
\tag{AME.2}
\]

Each summand extends by zero outside its positive-denominator region. Local finiteness proves continuity and the compactness in (AME.1); integration gives \(\sum_i\eta_i=1\). This is the precise cutoff supplied by the earlier proof.

For \(f\in C_b(H)\), define

\[
Tf(g)=\int_H f(h)\chi(h^{-1}g)\,dh.
\tag{AME.3}
\]

It is positive, unital and contractive. It is continuous: when \(g\) ranges over a compact neighbourhood \(D\), the support in \(h\) lies in the fixed compact set \(H\cap DB^{-1}\), where \(B=\operatorname{supp}\chi\cap q^{-1}(q(D))\). Uniform continuity on this compact parameter set permits integration. For \(a\in H\), left Haar substitution \(h=ak\) gives

\[
\begin{aligned}
T(L_a f)(g)
&=\int_H f(k)\chi(k^{-1}a^{-1}g)\,dk\\
&=Tf(a^{-1}g).
\end{aligned}
\tag{AME.4}
\]

If \(M\) is an invariant Haar mean on \(G\), set \(m_H(f)=M(Tf)\) for \(f\in\mathrm{UC}(H)\). Continuous bounded functions give well-defined ambient Haar classes. Equation (AME.4) makes \(m_H\) an invariant mean. AMH01 extends it to Haar \(L^\infty(H)\), proving the theorem.

In the separable cross-section version, \(\varphi(s)=s r(Hs)^{-1}\) satisfies \(\varphi(hs)=h\varphi(s)\). The factor \(h\) is necessary for the intertwining identity. The printed identity in Example XIII.4.4(iii) omits it. The continuous-kernel proof above also establishes the full locally compact statement, beyond that source proof's separable scope.

## Normal extensions and increasing unions

**Theorem.** If \(H\) is closed and normal in \(G\), then

\[
G\ \text{amenable}
\quad\Longleftrightarrow\quad
H\ \text{and }G/H\ \text{amenable}.
\tag{AME.5}
\]

For the forward implication, use AME01 for \(H\). Any continuous affine action of \(G/H\) on a compact convex set becomes such an action of \(G\) by the continuous quotient map. A \(G\)-fixed point is a \(G/H\)-fixed point, so AMH02 proves quotient amenability.

Conversely, let \(G\) act continuously and affinely on a nonempty compact convex set \(C\), at the separate continuity hypotheses of AMH02. The set \(C^H\) of \(H\)-fixed points is nonempty by amenability of \(H\). It is compact and convex, because it is an intersection of closed affine equalizers. Normality makes it \(G\)-invariant: for \(x\in C^H\),

\[
h(gx)=g((g^{-1}hg)x)=gx.
\]

The action factors through \(G/H\). Each orbit map descends continuously through the open quotient \(G\to G/H\), and each affine transformation remains continuous. Quotient amenability gives a fixed point in \(C^H\), which is fixed by all of \(G\). AMH02 proves the converse.

**Theorem.** If \(G=\bigcup_iH_i\) is an increasing directed union of closed amenable subgroups, then \(G\) is amenable.

Choose a left invariant mean \(m_i\) on \(\mathrm{UC}(H_i)\). Restriction sends \(\mathrm{UC}(G)\) into \(\mathrm{UC}(H_i)\), since a supremum on \(H_i\) is bounded by the ambient supremum. Thus

\[
\widetilde m_i(f)=m_i(f|_{H_i})
\tag{AME.6}
\]

is a state on \(\mathrm{UC}(G)\). Its weak-star compact state space supplies a convergent subnet. For fixed \(g\in G\), there is \(i_0\) with \(g\in H_{i_0}\); for every later \(i\), \(\widetilde m_i(L_gf)=\widetilde m_i(f)\). The subnet is eventually in this tail, so its limit is invariant under every \(g\). Apply AMH01. If two-sided invariance is desired, choose two-sided means using AMH02; the identical tail argument handles right translations too. No normality or sequential compactness assertion is needed.

## Abelian, solvable and compact examples

Every locally compact abelian group is amenable. Here is a proof using finite boxes rather than an additional fixed-point theorem. For a finite set \(F=\{s_1,\ldots,s_d\}\subset G\), push the uniform probability on \(\{-n,\ldots,n\}^d\) through

\[
(k_1,\ldots,k_d)\longmapsto
s_1^{k_1}\cdots s_d^{k_d}.
\]

Call the resulting finite point probability \(\mu_{F,n}\). For each \(s_j\), its total-variation translation error is at most \(2/(2n+1)\). Indeed only the two boundary faces differ before pushforward, and pushforward cannot increase total variation: test against a bounded function and pull it back. Consequently

\[
|\mu_{F,n}(L_{s_j}f)-\mu_{F,n}(f)|
\leq \frac{2\|f\|_\infty}{2n+1}.
\tag{AME.7}
\]

Direct \(F\) by inclusion and \(n\) by increase. A weak-star cluster point on \(\mathrm{UC}(G)\) is invariant, hence gives amenability. These are point probabilities on continuous functions; they need not be Haar densities. This distinction permits nondiscrete groups.

Let \(D^0G=G\), \(D^{j+1}G=[D^jG,D^jG]\) denote the algebraic derived series, with no closure inserted. Commutator continuity proves

\[
D^j\overline A\subset\overline{D^jA}
\tag{AME.8}
\]

for every subgroup \(A\): approximate each pair by a product net, then take finite products of commutators and induct. If \(D^dG=\{e\}\), the closed normal series \(C_j=\overline{D^jG}\) terminates at \(C_d=\{e\}\), and \([C_j,C_j]\subset C_{j+1}\). Each quotient \(C_j/C_{j+1}\) is locally compact and abelian. Repeated use of (AME.5) proves that every algebraically solvable locally compact group is amenable.

For a commutative locally compact topological field \(k\), let \(T_n(k)\) be the invertible upper triangular matrices. This is closed in the open matrix group \(\mathrm{GL}_n(k)\), hence locally compact. Its diagonal quotient is abelian. The kernel is \(1+J\), where \(J\) is the strictly upper triangular algebra and \(J^n=0\). In the algebra modulo \(J^{p+q}\), the elements \(1+u\), \(1+v\), with \(u\in J^p\), \(v\in J^q\), commute. Their inverses are finite geometric sums. Therefore

\[
[1+J^p,1+J^q]\subset1+J^{p+q},
\qquad D^r(1+J)\subset1+J^{2^r}.
\tag{AME.9}
\]

The derived length of \(T_n(k)\) is at most \(1+\lceil\log_2 n\rceil\). It is amenable. Reversing the coordinate order gives the lower triangular case. This covers real, complex, \(p\)-adic and discrete fields. For the rational-field example, the discrete topology is locally compact; the usual topology on \(\mathbb Q\) is not. A compact rational neighbourhood would be compact and closed in \(\mathbb R\), but would contain a rational interval whose real closure includes irrational points.

A compact group is amenable by normalized Haar integration. With the discrete topology, every locally finite group is the directed union of its finite subgroups, so AME02 applies. In particular \(S_\infty=\bigcup_nS_n\), the finite-support permutations of \(\mathbb N\), is amenable. The union theorem requires the stated locally compact group topology; an unspecified inductive-limit topology is not being assumed to have that property.

## Lie quotients without countability

**Theorem.** Let \(G\) be connected and locally compact Hausdorff. For every open identity neighbourhood \(U\), there is compact normal \(K\subset U\) such that \(G/K\) is a connected finite-dimensional Lie group.

The substantial countable-case input is **KT-KK-18 Theorem 12.31**, at its stated second-countable locally compact hypotheses. Its proof supplies the entire chain: uniform power escape and a regularized convolution bootstrap (12.19–12.22), power-map control and finite-dimensional exponential coordinates (12.23–12.27), finite compact representation kernels (12.28), and finite and small-subgroup trapping (12.29–12.30). We use that proved result, not a claim that compact approximation alone settles general Lie approximation.

Here is the passage to arbitrary \(G\). Choose a symmetric relatively compact open identity neighbourhood \(V\). Its generated subgroup is open and closed; connectedness gives

\[
G=\bigcup_{m\geq1}V^m
=\bigcup_{m\geq1}(\overline V)^m.
\tag{AME.10}
\]

The second equality follows because \(\overline V\subset V^2\). Put \(E=\overline V\), a compact symmetric generating set. Choose symmetric relatively compact open neighbourhoods \(W_j\) with \(\overline W_1\subset U\) and

\[
\begin{gathered}
\overline W_{j+1}\subset W_j,\qquad W_{j+1}^3\subset W_j,\\
a^{-1}W_{j+1}a\subset W_j\quad(a\in E).
\end{gathered}
\tag{AME.11}
\]

Compactness of \(E\) makes the last shrinking uniform in \(a\): cover \(E\times\{e\}\) by finitely many conjugation-continuity neighbourhoods and intersect their identity factors. Local compactness permits the closure shrinking.

Set \(N=\bigcap_j\overline W_j=\bigcap_jW_j\). It is compact and contained in \(U\). Equation (AME.11) makes it a subgroup invariant under conjugation by \(E\), hence normal in \(G\). The quotient \(L=G/N\) is locally compact Hausdorff, and \(q(W_j)\) form a countable identity base. In fact every open set containing \(N\) contains some \(\overline W_j\), by the finite-intersection property inside compact \(\overline W_1\).

The quotient is second countable, not merely first countable. It is sigma-compact by (AME.10). To see the implication directly, refine its identity base to symmetric \(A_j\) with \(A_{j+1}^2\subset A_j\). Cover each compact member of a countable compact exhaustion by finitely many translates \(xA_j\). The union of all these finite families over the two integer indices is a base. For \(y\in O\) open, choose \(j\) with \(yA_j\subset O\), and a compact covering member containing \(y\). Its finite cover at level \(j+1\) puts \(y\in xA_{j+1}\subset yA_{j+1}^2\subset O\).

Since \(N\subset U\) is compact, choose an open identity neighbourhood \(W\) with \(WN\subset U\), again by a finite cover and continuity of multiplication. Then \(O=q(W)\) is open and \(q^{-1}(O)=WN\subset U\). Apply the countable theorem to connected \(L\): it gives compact normal \(B\subset O\) with \(L/B\) Lie. Put \(K=q^{-1}(B)\). This is normal, contained in \(U\), and compact. To justify the last assertion, a quotient by a compact kernel is proper: finitely many images \(q(g_iD)\), for relatively compact open \(D\), cover any compact quotient set; its inverse image is closed inside the compact union \(\bigcup_i g_i\overline D N\).

Finally the open composite \(G\to L\to L/B\) identifies \(G/K\) topologically with \(L/B\). It is connected as an image of \(G\). This proves the theorem and supplies the unrestricted connected input S2.

## Constructing the connected solvable radical

**Theorem.** Every locally compact Hausdorff group \(G\) has a largest connected algebraically solvable normal subgroup \(R\). It is closed and characteristic under continuous automorphisms. Moreover

\[
R=\operatorname{rad}(G^\circ),\qquad
\operatorname{rad}(G/R)=\{e\}.
\tag{AME.12}
\]


We first treat connected \(G\). AME04 gives a compact normal \(K\) with connected Lie quotient \(L\). The earlier radical lesson's **Theorem 1C.5**, whose proof is in Sections 1C.1–1C.3, constructs the closed Lie radical \(R_L\) and gives a finite algebraic derived-length bound \(d\). Briefly, the sum \(\mathfrak r\) of the solvable ideals is a finite sum in finite dimension and is solvable. The identity component of the kernel of

\[
L\longrightarrow\mathrm{GL}(\mathfrak l/\mathfrak r),
\qquad g\longmapsto\operatorname{Ad}_g
\tag{AME.13}
\]

has Lie algebra \(\mathfrak r\), since \(\mathfrak l/\mathfrak r\) has zero centre. Theorem 1C.5 proves that this component is the largest connected solvable normal subgroup and has derived length at most \(\dim\mathfrak r\). Its induction integrates a real Lie-algebra character on the simply connected cover, so it covers nonlinear groups and infinite centres.

For any connected solvable normal \(P\subset G\), the closure of its image in \(L\) lies in \(R_L\), by (AME.8) and that maximality. Hence \(D^dP\subset K\). Each algebraic derived subgroup of a connected group is connected: the commutator image is connected and contains the identity, as does every finite product of it and its inverse; their increasing union is the commutator subgroup. Iterate this argument. Thus \(\overline{D^dP}\) is compact, connected and solvable.

**Lemma 1C.7** of the radical lesson proves that a compact connected solvable group is abelian. Its proof takes every finite-dimensional unitary image; the image is a compact connected solvable Lie group and has abelian Lie algebra by the invariant-positive-inner-product structure theorem. Exponentials generate its connected group, so the image is abelian. Peter–Weyl point separation then kills every original commutator. Consequently

\[
D^{d+1}P=\{e\}
\tag{AME.14}
\]

for every such \(P\), with one bound independent of \(P\).

Products of two connected solvable normal subgroups are connected, normal and solvable: their quotient by the first is an image of the second. The family is therefore directed. Its union \(A\) is a connected normal subgroup, and (AME.14) holds for \(A\): each finite commutator expression uses finitely many elements, all in one member of the directed family. Equation (AME.8) gives the same bound for \(R=\overline A\). This proves existence, closedness and maximality. Every continuous automorphism permutes the defining family, so \(R\) is characteristic.

For general \(G\), apply this result to the closed characteristic identity component \(G^\circ\). Its radical is closed, connected, solvable and normal in \(G\). Every connected solvable normal subgroup of \(G\) lies in \(G^\circ\) and therefore in that radical. This proves the first equality in (AME.12).

For the second, take a connected solvable normal subgroup of \(G/R\), replace it by its closure using (AME.8), and take its inverse image \(P\). Its connected fibres \(R\) and connected quotient make \(P\) connected: a separation would separate the fibres into saturated pieces, whose open images would separate the quotient. It is solvable, because an extension of two groups with finite derived-length bounds has the sum bound. Maximality gives \(P=R\). Thus the quotient subgroup was trivial.

We call a group with trivial connected solvable radical **semisimple** here. We also need the proved compact-kernel theorem: **Theorem 1A.10** of the radical lesson says that a compact normal quotient of a connected semisimple locally compact group is semisimple. The kernel need not be solvable. The proof uses \(G=K C_G(K)\), proved there by finite compact representations and compact implementer sets. It identifies \(G/K\) with \(C_G(K)/Z(K)\). A connected solvable normal subgroup of that quotient lifts through the abelian kernel \(Z(K)\) to a solvable group. The compact-kernel component theorem 1A.9 makes its identity component map onto the given connected subgroup. Semisimplicity forces that component, and hence its image, to vanish. These are the exact earlier proofs used below.

## Closed free subgroups as an obstruction

The discrete free group \(F_2=\langle a,b\rangle\) is not amenable. Let \(A_+,A_-,B_+,B_-\) be reduced words beginning with \(a,a^{-1},b,b^{-1}\), respectively. Together with the identity they partition \(F_2\), and cancellation gives

\[
aA_-=F_2\setminus A_+,\qquad
bB_-=F_2\setminus B_+.
\tag{AME.15}
\]

An invariant probability mean gives each singleton mass zero, since arbitrarily many disjoint translates fit into mass one. Equation (AME.15) would make the sum of the four set masses both two and one. Thus \(F_2\) is nonamenable. Every discrete \(F_n\), \(n\geq2\), contains a closed copy of \(F_2\), so AME01 proves its nonamenability too.

For comparison, the source's two-sided calculation is valid after supplying singleton mass zero. Let \(S\) consist of words whose first power block is a nonzero power of \(a\). Then

\[
S\cup aSa^{-1}=F_2\setminus\{e\},
\qquad b^nSb^{-n}\cap b^mSb^{-m}=\varnothing
\quad(n\ne m).
\tag{AME.16}
\]

For the first identity, conjugate a word beginning with \(b\) by \(a^{-1}\). For the second, the initial \(b\)-power of a conjugated word is exactly \(n\), with initial \(a\)-power when \(n=0\); cancellation at the right end cannot remove its first \(a\)-block. AMH02 would provide a two-sided mean. The first identity implies \(m(S)\geq1/2\), while any \(N\) disjoint conjugates give \(Nm(S)\leq1\), a contradiction.

There is an explicit closed discrete \(F_2\) in \(\mathrm{PSL}_2(\mathbb R)\). Use the projective classes of

\[
A=\begin{pmatrix}1&3\\0&1\end{pmatrix},
\qquad B=\begin{pmatrix}1&0\\3&1\end{pmatrix}.
\tag{AME.17}
\]

Put \(X=\{|x|>1\}\cup\{\infty\}\), \(Y=\{|x|<1\}\). For every nonzero integer \(n\), \(A^nY\subset X\) and \(B^nX\subset Y\), since

\[
A^nx=x+3n,\qquad
B^nx=\frac{x}{3nx+1},\qquad
\left|\frac{x}{3nx+1}\right|<1\ (|x|>1).
\tag{AME.18}
\]

Also \(B^n\infty=1/(3n)\). Apply the rightmost block of any nonempty alternating power word to \(1\), which is outside both domains. That block enters its prescribed domain; every successive block enters the other one. The word moves \(1\), proving freeness, including for one-block words. Integer matrix entries isolate the identity in the matrix subgroup. In the projective quotient, use small neighbourhoods of \(I\) and \(-I\) containing no other integer matrices. This proves discreteness there.

Every subgroup discrete in its subspace topology is closed in a Hausdorff group. Choose an identity neighbourhood \(W\) meeting the subgroup only at \(e\), then \(V\) open with \(V^{-1}V\subset W\). Each translate \(xV\) contains at most one subgroup point. A point of the closure must equal that point, since otherwise deleting the singleton gives an open neighbourhood missing the subgroup.

**Lifting lemma.** If \(G/N\) contains a discrete free subgroup, choose arbitrary lifts of its free generators. A nonempty reduced relation upstairs would project to one downstairs, which is impossible. The generated subgroup maps bijectively to the free subgroup. The inverse image of a quotient neighbourhood isolating \(e\) also isolates \(e\) upstairs. Thus the lift is discrete and, by the preceding argument, closed. Compactness of \(N\) is unnecessary.

Finally **Theorem 1E.1**, with its complete proof in Sections 1D–1E of the radical lesson, gives a closed connected subgroup locally isomorphic to \(\mathrm{SL}_2(\mathbb R)\) in every noncompact connected semisimple Lie group. It constructs a real split triple, proves closedness of its adjoint matrix image, and takes the identity component of its closed preimage in the original group. Thus it also covers nonlinear groups with infinite centre. Such a subgroup has adjoint quotient \(\mathrm{PSL}_2(\mathbb R)\): its adjoint derivative identifies its algebra with the inner derivations of \(\mathfrak{sl}_2(\mathbb R)\), giving the connected adjoint image, with central discrete kernel. The lifting lemma applied to (AME.17) supplies a closed discrete \(F_2\) in the original Lie group.

## The full almost-connected criterion

**Theorem.** Suppose \(G/G^\circ\) is compact. With \(R=\operatorname{rad}G\), the following are equivalent:

1. \(G\) is amenable.
2. \(G/R\) is compact.
3. \(G\) contains no closed discrete subgroup isomorphic to \(F_2\).

If \(G/R\) is compact, it is amenable by Haar integration, and \(R\) is amenable by AME03. Equation (AME.5) gives amenability of \(G\). If \(G\) is amenable, AME01 and AME06 exclude a closed discrete \(F_2\).

For the remaining implication put \(S=G/R\). It is semisimple by AME05. Since \(R\) is connected and lies in \(G^\circ\),

\[
S^\circ=G^\circ/R,\qquad
S/S^\circ\cong G/G^\circ.
\tag{AME.19}
\]

Here the component equality uses the fact that \(G/G^\circ\) is totally disconnected: its quotient map is open with connected fibres, so any connected set in that quotient has connected inverse image and must be a singleton. The subgroup \(G^\circ/R\) is closed and connected, and this totally disconnected further quotient proves the equality.

Assume \(S\) is noncompact. Then \(S^\circ\) is noncompact, since a compact kernel with compact quotient has compact total group. To verify that last fact, cover the compact quotient by finitely many images \(q(g_iU)\) with \(U\) relatively compact open; the total group is then the finite union \(g_i\overline U K\) of compact sets.

The group \(S^\circ\) is semisimple: its radical is characteristic in \(S^\circ\), hence normal in \(S\), and would otherwise contradict semisimplicity of \(S\). Apply AME04 to obtain compact normal \(K\subset S^\circ\) with connected Lie quotient \(L=S^\circ/K\). The compact-kernel theorem at the end of AME05 makes \(L\) semisimple. It is noncompact by the compactness argument just given. AME06 produces a closed discrete \(F_2\) in \(L\), and its lifting lemma produces one in \(S^\circ\), hence in \(S\). Apply that lemma again through \(G\to S\). We obtain a closed discrete \(F_2\) in \(G\), contradicting assertion 3. This proves all three equivalences.

Almost connectedness is necessary for this characterization. The discrete group \(\mathbb Z\) is amenable and has trivial connected radical, but its radical quotient is not compact. The theorem is also not confined to Lie groups. For any infinite index set \(I\), the group

\[
G=\mathbb R\times\mathbb T^I
\tag{AME.20}
\]

is connected, locally compact and abelian, so \(R=G\). Compactness of the torus product follows from product compactness; its finite-support connected subgroups have dense union, proving connectedness. Every identity neighbourhood contains a nontrivial subgroup in unconstrained coordinates, so \(G\) is not Lie: an exponential chart in a Lie group contains a smaller neighbourhood with no nontrivial subgroup, because a suitable integer multiple of any nonzero small logarithm exits it while remaining in the chart. When \(I\) is uncountable there is no countable identity base: the union of the finitely many coordinates constrained by each proposed basic neighbourhood is countable and misses a coordinate whose nontrivial restriction defines another neighbourhood. The full theorem nevertheless applies.

## Modular averaging through a normal extension

**Theorem.** Let an amenable locally compact Hausdorff \(G\) act on a von Neumann algebra \(M\) by automorphisms \(\alpha_g\), continuously in the point-predual-norm topology. Suppose it preserves a faithful normal state \(\varphi\). For closed normal \(H\), put \(N=M^H\) and \(Q=G/H\). Then the state-preserving conditional expectations factor as

\[
E_G=E_Q E_H:M\longrightarrow M^G,
\tag{AME.21}
\]

where \(E_H:M\to N\), and \(E_Q:N\to N^Q=M^G\) averages the induced quotient action. All these maps are normal and faithful.

By AME01–02, \(H,Q\) are amenable. AMH06 constructs the unique \(\varphi\)-preserving conditional expectation \(E_H\), with normality and faithfulness proved there from the faithful invariant normal state. Normality of \(H\) makes \(N\) invariant under \(\alpha_g\). The conjugated map \(\alpha_gE_H\alpha_{g^{-1}}\) is again a \(\varphi\)-preserving conditional expectation onto \(N\); uniqueness gives

\[
\alpha_gE_H=E_H\alpha_g.
\tag{AME.22}
\]

The restricted action on \(N\) is trivial on \(H\), so defines \(\beta_{gH}=\alpha_g|_N\).

The quotient action has the required predual continuity. For \(\omega\in N_*\), the normal functional \(\widetilde\omega=\omega E_H\) belongs to \(M_*\) and extends \(\omega\). Restriction has norm at most one, and (AME.22) gives

\[
\|\omega\beta_{gH}-\omega\|_{N_*}
\leq\|\widetilde\omega\alpha_g-\widetilde\omega\|_{M_*}.
\tag{AME.23}
\]

This tends to zero as \(g\to e\). Since \(G\to Q\) is an open quotient, the orbit map descends continuously to \(Q\); the same holds at every coset. The state \(\varphi|_N\) is faithful, normal and invariant. AMH06 therefore supplies \(E_Q\).

The composition is a normal unital completely positive projection onto \(M^G\), is bimodular over that algebra, and preserves \(\varphi\). Uniqueness in AMH06 identifies it with \(E_G\). If its value on \(x\geq0\) is zero, then \(\varphi(x)=0\), so \(x=0\); this proves faithfulness. This is also why merely choosing arbitrary invariant means would not justify the normality claims.

In the GNS space of \(\varphi\), let \(e_H,e_G\) be the orthogonal projections onto \(\overline{N\Omega_\varphi}\), \(\overline{M^G\Omega_\varphi}\). The graph-core and spectral-domain proof of AMH07 gives

\[
e_Ge_H=e_He_G=e_G,\qquad
e_H\Lambda_\varphi(x)=\Lambda_\varphi(E_Hx).
\tag{AME.24}
\]

The analogous identity for \(e_G\) and (AME.21) show that successive averaging is precisely the nested orthogonal projection. Both projections commute with the full modular spectral measure and the modular conjugation. For every \(z\in\mathbb C\),

\[
\begin{gathered}
D(\Delta_{\varphi|_N}^{\,z})
=e_H\mathcal H_\varphi\cap D(\Delta_\varphi^{\,z}),\\
\Delta_{\varphi|_N}^{\,z}
=\Delta_\varphi^{\,z}|_{e_H\mathcal H_\varphi},
\end{gathered}
\tag{AME.25}
\]

with the corresponding formula for \(M^G\). To apply the restriction formula a second time, intersect its domain with \(e_G\mathcal H_\varphi\subset e_H\mathcal H_\varphi\); it becomes exactly \(e_G\mathcal H_\varphi\cap D(\Delta_\varphi^z)\). Thus direct and successive averaging give identical closed Tomita restrictions and identical maximal modular-power domains. This is a domain equality, not just agreement of operators on algebraic vectors.

For a finite diagnostic, take \(M=M_2\otimes M_2\), \(\varphi=\operatorname{Tr}(D\,\cdot)\otimes\operatorname{Tr}(D\,\cdot)\), \(D=\operatorname{diag}(1/3,2/3)\). Let \(G=\mathbb Z^2\) act by independent conjugations with \(u=\operatorname{diag}(1,e^{i\theta})\), where \(\theta/(2\pi)\) is irrational, and \(H=\mathbb Z\times\{0\}\). Then \(E_H\) removes the first tensor factor's off-diagonal entries, and \(E_Q\) removes the second's. Their composition is the full diagonal expectation. On \(e_{ij}\otimes e_{kl}\) the modular eigenvalue is

\[
\frac{D_{ii}}{D_{jj}}\frac{D_{kk}}{D_{ll}}.
\tag{AME.26}
\]

The first projection keeps \(i=j\), and the second also imposes \(k=l\), leaving eigenvalue one. The finite averages in each coordinate have off-diagonal factor bounded by \(2/((2n+1)|1-e^{i\theta}|)\). This tests the two averaging stages, the nontracial state and the modular restriction in the same example.

**Sources and proof route.** Takesaki, *Theory of Operator Algebras III*, Example XIII.4.4, printed pages 63–64, supplies the complete list addressed here, including the almost-connected assertion for which that example does not give a proof. The proofs here use the earlier programme results linked above. The connected Lie-approximation argument follows the classical Gleason–Yamabe theory developed in Tao's freely available author manuscript, *Hilbert's fifth problem and related topics*, Section 1.5; the actual programme proof is KT-KK-18, 12.19–12.31. The radical and closed rank-one arguments are proved in the cited programme lesson, including its explicit compact-representation, root and Lie inputs. AME08 develops the consequence for the modular theory of a state-preserving action.
