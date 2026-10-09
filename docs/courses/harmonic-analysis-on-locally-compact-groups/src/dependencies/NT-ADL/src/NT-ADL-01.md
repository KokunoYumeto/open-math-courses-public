# Restricted products and profinite completions

*Original independently authored material written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026; the section on unrestricted products by Claude Opus 5.5 (Anthropic). Self-checked by the writing AI. Original text: [CC0](https://creativecommons.org/publicdomain/zero/1.0/).*

A finite adèle records one number in each field \(\mathbb Q_p\), with an integrality condition at all but finitely many primes. Its topology must allow those finitely many exceptions while retaining a compact neighbourhood. Restricted products provide exactly this construction. They also explain how local integrals and local characters combine into global ones.

We first build the topology, then integration and characters. We apply the construction to the profinite integers and finite adèles, and finish with test functions and the topology of finite idèles. The prerequisites are point-set topology and measure and integration, together with Haar measure on locally compact groups, Characters and the dual group, [The dual group as the Gelfand spectrum of \(L^1(G)\)](prerequisites/HA-LCA-03.md), The Pontryagin duality theorem, Subgroups, quotients and annihilators, and Totally disconnected groups, the p-adic numbers and the adèles. The precise background statements used without proof are listed below.

The restricted-product construction can be compared with [Getz–Hahn, §2.3] and [Sutherland 25, §25.2]. [Bost–Connes, §3] gives the finite rational adèle ring, and [Lenstra, Example 2.2] describes the profinite integers. The general character theorem and all residue calculations needed here are proved below.

## Why an unrestricted product can fail to be locally compact

Let \((G_v)_{v\in V}\) be locally compact Hausdorff groups, and write \(1\) for the identity of each of them. Their full product \(\prod_vG_v\), with coordinatewise operations and the product topology, is locally compact precisely when \(G_v\) is compact for all but finitely many \(v\). In fact, a single compact neighbourhood of the identity already forces all but finitely many factors to be compact.

To prove this, let \(C\) be a compact neighbourhood of \(1\) in \(\prod_vG_v\). It contains a basic open set \(\prod_{v\in F}U_v\times\prod_{v\notin F}G_v\) containing \(1\), where \(F\subseteq V\) is finite and each \(U_v\) is open in \(G_v\). That basic set, and therefore \(C\), contains the subgroup
\[
T_F=\Bigl\{x\in\prod_vG_v:x_v=1\text{ for every }v\in F\Bigr\}.
\]
Points are closed in the Hausdorff groups \(G_v\), and the coordinate maps are continuous. Hence \(T_F\) is closed, as the intersection of the finitely many closed sets \(\{x:x_v=1\}\) with \(v\in F\) (the whole product when \(F\) is empty). A closed subset of the compact set \(C\) is compact, so \(T_F\) is compact. For \(w\notin F\), each \(g\in G_w\) is the \(w\)-coordinate of the element of \(T_F\) with \(g\) at \(w\) and \(1\) elsewhere. Thus \(G_w\) is the image of \(T_F\) under the continuous coordinate map, and it is compact for every \(w\) outside the finite set \(F\).

Conversely, suppose that \(G_v\) is compact for every \(v\) outside a finite set \(F\). Given \(x\in\prod_vG_v\), choose a compact neighbourhood \(C_v\) of \(x_v\) for each \(v\in F\). The set
\[
\prod_{v\in F}C_v\times\prod_{v\notin F}G_v
\]
is compact by the compact-product theorem. It contains the basic open set with the interiors of the \(C_v\) at \(v\in F\) and all of \(G_v\) elsewhere, and this basic set contains \(x\). So it is a compact neighbourhood of \(x\).

The finite adèles involve the fields \(\mathbb Q_p\), and none of them is compact. The open additive subgroups \(p^{-k}\mathbb Z_p\), \(k\geq0\), increase with \(k\), and they cover \(\mathbb Q_p\) because every nonzero element has an integer valuation. A finite subfamily has union \(p^{-m}\mathbb Z_p\) for its largest index \(m\). This union misses \(p^{-m-1}\), since every element of \(p^{-m}\mathbb Z_p\) has valuation at least \(-m\). By the criterion, \(\prod_p\mathbb Q_p\) is not locally compact, even though its subgroup \(\prod_p\mathbb Z_p\) is compact by the compact-product theorem. That compact subgroup is not a neighbourhood of \(0\) either. As in the argument above, every neighbourhood of \(0\) contains a subgroup \(T_F\), written additively, and \(T_F\) contains the tuple with coordinate \(p^{-1}\) at one prime \(p\notin F\) and \(0\) at all other primes, which lies outside \(\prod_p\mathbb Z_p\).

A restricted product keeps every factor \(G_v\) but shrinks the tails of its basic neighbourhoods. Outside a finite set \(S\), each coordinate ranges over a compact open subgroup \(K_v\) instead of all of \(G_v\). A basic neighbourhood of the identity then contains the compact subgroup \(\{1\}^S\times\prod_{v\notin S}K_v\), whereas in the full product every identity neighbourhood contains one of the subgroups \(T_F\). Proposition 1.1 proves that the restricted product is locally compact. In the finite adèles defined below, \(\prod_p\mathbb Z_p\) is a compact open subgroup. [Sutherland 25, §25.1] discusses the same obstruction for the product of the fields \(\mathbb Q_p\).

## A topology with finitely many exceptional coordinates

Let \(V\) be any index set. Each \(G_v\) is a locally compact Hausdorff group. Fix a finite set \(E\subseteq V\), and for \(v\notin E\) choose a compact open subgroup \(K_v\leq G_v\). Coordinates in \(E\) are unrestricted; this permits real or complex factors. Throughout, “almost all” means all but finitely many.

The **restricted product** is the group
\[
G=\prod_{v\in V}'(G_v,K_v)
=\left\{x\in\prod_{v\in V}G_v:
x_v\in K_v\text{ for almost all }v\notin E\right\}.
\]
For finite \(S\supseteq E\), set
\[
G_S=\prod_{v\in S}G_v\times\prod_{v\notin S}K_v.
\]
Give \(G\) the topology with basis
\[
B(S;U)=\prod_{v\in S}U_v\times\prod_{v\notin S}K_v,
\qquad U_v\subseteq G_v\text{ open}.
\tag{1}
\]
The finite set can always be enlarged: a newly included coordinate is assigned the open set \(K_v\). This observation proves that intersections of basic sets are basic sets, allowing empty factors.

**Proposition 1.1.** The restricted product is a locally compact Hausdorff topological group. It is the upward-directed union of the open subgroups \(G_S\), and each \(G_S\) has its product topology. Every compact subset of \(G\) lies in some \(G_S\).

**Proof.** Every tuple satisfies the defining restriction outside a finite set, so \(G=\bigcup_SG_S\). Coordinatewise multiplication and inversion preserve the condition because the \(K_v\) are subgroups. Thus \(G\) is an algebraic subgroup of the full product.

The sets \(G_S\) are open by (1). Intersecting (1) with \(G_S\) imposes open conditions on only finitely many factors of its product decomposition. Conversely, every product neighbourhood in \(G_S\) is obtained this way, since its finitely many conditions on tail factors are open in the corresponding \(G_v\). Hence the induced topology is the product topology.

For \(x,y\in G\), choose one \(G_S\) containing both. Multiplication is continuous on \(G_S\times G_S\), and inversion is continuous on \(G_S\). These are open neighbourhoods of the relevant points in the domain, proving continuity on \(G\).

Each coordinate projection is continuous: at a point, enlarge \(S\) to include that coordinate. Distinct tuples therefore have disjoint neighbourhoods pulled back from a Hausdorff factor. This proves the Hausdorff property.

For \(x\in G_S\), choose a compact neighbourhood \(C_v\) of \(x_v\) in each of the finitely many factors indexed by \(S\). The set
\[
\prod_{v\in S}C_v\times\prod_{v\notin S}K_v
\]
is a compact neighbourhood of \(x\), by the compact-product theorem. This proves local compactness. Finally, the open cover \((G_S)_S\) of a compact subset has a finite subcover. The union of the finitely many indexing sets gives a single chart containing that subset. \(\square\)

The inclusion \(G\hookrightarrow\prod_vG_v\) is continuous. It generally fails to be a topological embedding: (1) constrains every coordinate outside \(S\), whereas a product neighbourhood constrains only finitely many coordinates. Exercise 1 proves the exact criterion. Changing the chosen subgroups at finitely many indices changes neither the underlying restricted product nor its topology; include those indices in every chart.

There is also an intrinsic stage test for this topology: \(U\subseteq G\) is open if and only if \(U\cap G_S\) is open in every product stage. One implication follows by restriction; for the other, each \(U\cap G_S\) is open in \(G\), because \(G_S\) is open, and their union is \(U\). This explains why the product topology is correct on a fixed stage even when it fails on the full restricted product. [Getz–Hahn, §2.3, pp.46–48] describes countably indexed restricted products; [Sutherland 25, Proposition 25.5, pp.3–4] gives the open-stage description for arbitrary index sets. Our Proposition 1.1 and Exercise 1 retain that arbitrary-index scope.

## Integrating local data

Choose left Haar measures \(\mu_v\) on \(G_v\). Enlarge \(E\), if necessary, so that
\[
\mu_v(K_v)=1\qquad(v\notin E).
\tag{2}
\]
The enlargement retains any exceptional local normalization as an actual finite factor. An infinite product of arbitrary normalization constants is not part of the construction.

On the compact group \(L_S=\prod_{v\notin S}K_v\), let \(m_S\) be Haar probability. Its projection to any finite product of tail factors has the product of their normalized Haar measures: the projected measure is invariant, has total mass one, and Haar uniqueness applies. This describes the infinite product as a Radon measure on its compact product topology.

Use the **Radon product** for finite products of locally compact spaces: it is the measure determined by iterated integrals of compactly supported continuous functions. It avoids imposing a countability assumption on the Borel sets of a product.

**Proposition 1.2.** The measures
\[
\mu_S=\left(\mathop{\widehat\bigotimes}_{v\in S}\mu_v\right)
\widehat\otimes m_S
\quad\text{on }G_S
\tag{3}
\]
are compatible under restriction and determine a unique left Haar measure \(\mu\) on \(G\). If \(f_v\) are Borel integrable functions and \(f_v=1_{K_v}\) for all \(v\notin S\), where \(S\supseteq E\) is finite, then
\[
f(x)=\bigotimes_v f_v(x):=\prod_v f_v(x_v)
\]
is integrable and
\[
\int_Gf\,d\mu=\prod_v\int_{G_v}f_v\,d\mu_v.
\tag{4}
\]
The product on the right has only finitely many factors different from one. In particular, (4) applies to compactly supported continuous local functions.

**Proof.** Suppose \(S\subseteq T\). Restricting \(\mu_T\) to \(G_S\) replaces each \(\mu_v\), for \(v\in T\setminus S\), by its restriction to \(K_v\), of mass one. Their finite product with \(m_T\) is Haar probability on \(L_S\), hence is \(m_S\). This proves compatibility in (3).

For \(h\in C_c(G)\), Proposition 1.1 places its support in some \(G_S\). Define
\[
I(h)=\int_{G_S}h\,d\mu_S.
\]
Compatibility makes this independent of \(S\), and a common larger chart proves linearity and positivity. Given \(g\in G\), a chart containing both \(g\) and \(\operatorname{supp}h\) also contains \(g\operatorname{supp}h\). Its measure is a product of left Haar measures, so \(I(h(g^{-1}\cdot))=I(h)\).

The Riesz representation theorem gives a unique Radon measure representing \(I\). It is nonzero and left invariant, so it is Haar. Functions in \(C_c(G_S)\) extend by zero to \(G\), since an open subgroup is also closed. Riesz uniqueness then gives \(\mu|_{G_S}=\mu_S\), establishing the asserted restrictions and uniqueness.

For (4), \(f\) vanishes off \(G_S\), and on that chart it is a finite product of local functions, independent of \(L_S\). Each set \(\{f_v\neq0\}\) is \(\sigma\)-finite for \(\mu_v\): it is the union of the finite-measure sets \(\{|f_v|>1/j\}\). The rectangle and Tonelli theorems for Radon products therefore apply to the absolute values of these factors. They give
\[
\int_G|f|\,d\mu=\prod_{v\in S}\int|f_v|\,d\mu_v<\infty.
\]
Fubini now gives (4). This argument uses \(\sigma\)-finiteness of the nonzero sets of the particular functions, not of the ambient groups. \(\square\)

Thus the notation \(\mu=\bigotimes_v\mu_v\) means the compatible Radon measure just constructed. Its definition does not require \(G\) to be second countable or \(\sigma\)-compact.

## Characters see only finitely many integral tails

Now assume all \(G_v\) are abelian and write their law additively. Put \(\mathbb T=\{z\in\mathbb C:|z|=1\}\). The dual \(\widehat H\) of an LCA group consists of continuous homomorphisms \(H\to\mathbb T\), with uniform convergence on compact sets. For a subgroup \(K\leq H\), its annihilator is
\[
K^\perp=\{\chi\in\widehat H:\chi(k)=1\text{ for every }k\in K\}.
\]
The subgroup and quotient duality theorems imply that \(K_v^\perp\) is compact and open when \(K_v\) is compact and open. These are the distinguished subgroups on the dual side.

We use a small fact about the circle. The arc \(A=\{z\in\mathbb T:\operatorname{Re}z>0\}\) contains no nontrivial subgroup. Indeed, write a nonidentity element as \(e^{2\pi it}\) with \(0<|t|\leq1/2\). If \(|t|\geq1/4\), it is already outside \(A\). Otherwise choose the least positive integer \(m\) with \(m|t|\geq1/4\). Then \(1/4\leq m|t|<1/2\), and its \(m\)-th power is outside \(A\).

**Theorem 1.3.** There is a canonical isomorphism of topological groups
\[
\Phi:\prod_v'(\widehat G_v,K_v^\perp)
\xrightarrow{\ \sim\ }\widehat G,
\qquad
\Phi((\chi_v))(x)=\prod_v\chi_v(x_v).
\tag{5}
\]
The factors indexed by \(E\) remain unrestricted. Every continuous character of \(G\) has local restrictions trivial on \(K_v\) for almost all \(v\).

**Proof.** For a tuple on the left and an element \(x\in G\), both restrictions hold outside finite sets. Consequently all but finitely many factors in (5) equal one. On a chart containing the exceptional coordinates of the character tuple, (5) is a finite product of continuous local characters. It is therefore a continuous character on the open cover of \(G\).

Conversely, let \(\chi\in\widehat G\). Continuity provides a basic neighbourhood \(B(S;U)\) of zero whose image lies in \(A\). The compact subgroup
\[
T_S=\{0\}^{S}\times\prod_{v\notin S}K_v
\]
lies in this neighbourhood. Since \(\chi(T_S)\) is a subgroup contained in \(A\), it is trivial. Restricting \(\chi\) to the embedded coordinate group gives \(\chi_v\in\widehat G_v\), and \(\chi_v\in K_v^\perp\) outside \(S\). For any \(x\), enlarge \(S\) to contain its nonintegral coordinates. Decompose \(x\) into a finite-coordinate part and an element of \(T_S\). The latter contributes one, so \(\chi(x)=\prod_v\chi_v(x_v)\). Uniqueness follows by evaluating on individual coordinates. This proves algebraic bijectivity.

We verify both topologies explicitly. Let \(C\subseteq G\) be compact. Choose \(S\supseteq E\) with \(C\subseteq G_S\), and let \(C_v\) be its compact coordinate projections for \(v\in S\). Restrict dual tuples to the open dual chart
\[
H_S=\prod_{v\in S}\widehat G_v\times\prod_{v\notin S}K_v^\perp.
\]
Their evaluations on \(C\) have only the factors indexed by \(S\). Requiring each such factor to be uniformly within \(\varepsilon/\max(1,|S|)\) of one on \(C_v\) gives an open neighbourhood in \(H_S\). The inequality
\[
\left|\prod_{j=1}^rz_j-1\right|\leq\sum_{j=1}^r|z_j-1|\qquad(z_j\in\mathbb T)
\]
shows that its image is uniformly within \(\varepsilon\) of one on \(C\). Thus \(\Phi\) is continuous.

For the inverse, take a basic identity neighbourhood with finite-coordinate conditions \(\chi_v\in U_v\) for \(v\in S\), and the condition \(\chi_v\in K_v^\perp\) outside \(S\). Restriction \(\widehat G\to\widehat G_v\) is continuous, since a compact set in \(G_v\) embeds as a compact set in \(G\). The remaining conditions say exactly that \(\chi\) annihilates \(T_S\). Its annihilator is open: the compact-open condition \(\chi(T_S)\subseteq A\) is equivalent to triviality there. Intersecting this open annihilator with the finitely many inverse images of \(U_v\) gives the image of the chosen neighbourhood. This proves continuity of \(\Phi^{-1}\). \(\square\)

The theorem concerns a restricted product of **abelian** groups. Proposition 1.1 and the Haar construction require no commutativity.

## Integral residues and finite adèles

The Chinese remainder theorem used below has a short algebraic proof. For pairwise coprime positive integers \(m_1,\ldots,m_r\), put \(M=\prod_i m_i\). Bézout's identity gives \(b_i\) with \(b_i(M/m_i)\equiv1\pmod{m_i}\). Given residues \(a_i\), the integer \(\sum_i a_i b_i(M/m_i)\) realizes all of them. An integer divisible by every \(m_i\) is divisible by \(M\), proving uniqueness modulo \(M\).

Define the **profinite integers** by
\[
\widehat{\mathbb Z}=\varprojlim_{n\geq1}\mathbb Z/n\mathbb Z,
\]
where indices are ordered by divisibility and the transition maps are reduction maps. A point is a compatible collection of residues. The topology is inherited from the product of the finite discrete rings. Compatibility is closed, so this is a compact Hausdorff ring.

For each prime \(p\), we use \(\mathbb Z_p=\varprojlim_k\mathbb Z/p^k\mathbb Z\) and its fraction field \(\mathbb Q_p\). Its additive neighbourhoods are \(p^k\mathbb Z_p\), for \(k\in\mathbb Z\); \(\mathbb Z_p\) is compact and open. Define
\[
\mathbb A_f=\prod_p'(\mathbb Q_p,\mathbb Z_p).
\]
Addition and multiplication are coordinatewise. This is a topological ring: on each open chart \(\prod_{p\in S}\mathbb Q_p\times\prod_{p\notin S}\mathbb Z_p\) both operations are continuous and preserve the chart. Proposition 1.1 gives local compactness.

**Proposition 1.4.** There are canonical isomorphisms
\[
\widehat{\mathbb Z}\simeq\prod_p\mathbb Z_p,
\qquad
\widehat{\mathbb Z}^{\times}\simeq\prod_p\mathbb Z_p^{\times},
\tag{6}
\]
of compact topological rings and of compact topological groups, respectively. Moreover,
\[
\mathbb A_f\simeq\mathbb Q\otimes_{\mathbb Z}\widehat{\mathbb Z}
=\bigcup_{n\geq1}\frac1n\widehat{\mathbb Z}
\tag{7}
\]
as topological rings, when the tensor product is given the topology specified below. There are isomorphisms of discrete groups
\[
\mathbb A_f/\widehat{\mathbb Z}
\simeq\mathbb Q/\mathbb Z
\simeq\bigoplus_p\mathbb Q_p/\mathbb Z_p,
\qquad
\widehat{\widehat{\mathbb Z}}\simeq\mathbb Q/\mathbb Z.
\tag{8}
\]
In the last formula, the outer hat denotes the character group.

**Proof.** Restriction to the prime-power residues maps \(\widehat{\mathbb Z}\) to \(\prod_p\mathbb Z_p\). Conversely, given prime-power residues and \(n=\prod_{p\mid n}p^{a_p}\), the Chinese remainder theorem supplies a unique residue modulo \(n\). These residues are compatible as \(n\) varies. This proves (6) for rings. The map is continuous, and a continuous bijection from a compact space to a Hausdorff space is a homeomorphism. A tuple in a product ring is a unit precisely when every component is a unit; componentwise inversion is continuous on the compact product of the local unit groups. This proves the second assertion.

We will need the more precise residue calculation
\[
\widehat{\mathbb Z}/n\widehat{\mathbb Z}\simeq\mathbb Z/n\mathbb Z.
\tag{9}
\]
In \(\mathbb Z_p\), the kernel of reduction modulo \(p^a\) is \(p^a\mathbb Z_p\): a compatible tuple in the kernel can be divided by \(p^a\) by using its residues modulo \(p^{a+k}\). Multiplication by an integer prime to \(p\) is invertible, because its inverses modulo every \(p^k\) are compatible. The kernel of reduction modulo \(n\) in (6) is therefore exactly \(n\widehat{\mathbb Z}\), and reduction is surjective by the Chinese remainder theorem. This proves (9). In particular, this kernel is compact and open and has index \(n\).

Identify \(\widehat{\mathbb Z}\) with the compact open subring \(\prod_p\mathbb Z_p\) of \(\mathbb A_f\). Given \(x\in\mathbb A_f\), only finitely many coordinates have negative valuation. Choose
\[
n=\prod_p p^{\max(0,-v_p(x_p))},
\]
where zero coordinates contribute exponent zero. Then \(nx\in\widehat{\mathbb Z}\). Thus the union in (7) is all of \(\mathbb A_f\).

Every tensor can be put over a common denominator, hence written as \((1/n)\otimes z\). The map \(q\otimes z\mapsto(qz_p)_p\) is surjective by the preceding paragraph. It is injective: if the image of \((1/n)\otimes z\) is zero, every component of \(z\) is zero. This identifies the tensor product algebraically with the localization of \(\widehat{\mathbb Z}\) at the nonzero integers.

Give each stage \(n^{-1}\widehat{\mathbb Z}\) the compact topology transported by \(z\mapsto z/n\). Give their union the **stage topology**: a subset is open precisely when its intersection with each stage is open there. In \(\mathbb A_f\) the stage is
\[
\prod_{p\mid n}p^{-v_p(n)}\mathbb Z_p
\times\prod_{p\nmid n}\mathbb Z_p,
\]
so it is compact and open with exactly that transported topology. Since these open stages cover \(\mathbb A_f\), their stage topology is its topology. This proves the topological assertion in (7); the algebraic tensor product alone does not specify a topology.

The diagonal map \(\mathbb Q\to\mathbb A_f/\widehat{\mathbb Z}\) has kernel \(\mathbb Z\): a rational number integral at every prime has no prime in its reduced denominator. To prove surjectivity, write \(x=z/n\). By (9), choose \(a\in\mathbb Z\) with \(z-a\in n\widehat{\mathbb Z}\). Then \(x-a/n\in\widehat{\mathbb Z}\). Hence the first isomorphism in (8) follows. The quotient is discrete because \(\widehat{\mathbb Z}\) is open; give \(\mathbb Q/\mathbb Z\) its discrete topology.

Coordinate residues give a surjection
\[
\mathbb A_f\longrightarrow\bigoplus_p\mathbb Q_p/\mathbb Z_p
\]
with kernel \(\widehat{\mathbb Z}\): every finite collection of local cosets is represented by a tuple with zero in all other coordinates. This proves the middle identification, with the direct sum also discrete. In particular \(\mathbb Q_p/\mathbb Z_p\simeq\mathbb Z[1/p]/\mathbb Z\). For surjectivity of this local map, write \(x=p^{-k}z\) and choose an integer with the same residue as \(z\) modulo \(p^k\); its kernel consists of the ordinary integers.

Finally, duality for surjective inverse systems of compact abelian groups gives
\[
\widehat{\widehat{\mathbb Z}}
\simeq\varinjlim_n\widehat{\mathbb Z/n\mathbb Z}.
\]
This is Proposition 4.2 of Totally disconnected groups, the p-adic numbers and the adèles, applied to the surjective reduction maps ordered by divisibility. A character of \(\mathbb Z/n\mathbb Z\) is determined by an \(n\)-th root of unity, so its dual identifies with \(n^{-1}\mathbb Z/\mathbb Z\). For \(n\mid m\), pullback sends \(a/n\) to \((ma/n)/m\), the same rational class. The limit is \(\mathbb Q/\mathbb Z\). Explicitly the pairing is
\[
\langle z,a/n+\mathbb Z\rangle
=\exp\!\left(2\pi i\frac{a z_n}{n}\right),
\tag{10}
\]
where \(z_n\) is any integer representative of the residue of \(z\) modulo \(n\). Compatibility makes it independent of all representatives. The dual of a compact group is discrete, so this is a topological isomorphism. \(\square\)

For this particular inverse limit, the character factorization can also be checked directly. If \(\chi:\widehat{\mathbb Z}\to\mathbb T\) is continuous, the inverse image of the arc \(A\) used in Theorem 1.3 contains a basic neighbourhood of zero. That neighbourhood restricts only finitely many residues, say modulo \(n_1,\ldots,n_r\). Put \(n=\operatorname{lcm}(n_1,\ldots,n_r)\), with \(n=1\) when there are no conditions. Equation (9) implies that \(n\widehat{\mathbb Z}\) lies in that neighbourhood. Its image under \(\chi\) is a subgroup contained in \(A\), so is trivial. Thus \(\chi\) factors through \(\mathbb Z/n\mathbb Z\), whose characters are exactly (10). This supplies a complete elementary alternative for (8), while the preceding programme result also treats general surjective inverse systems of compact abelian groups.

### Worked example: one rational representative

Take \(x_2=1/8\), \(x_3=2/9\), and \(x_p=0\) at all other primes. Then \(72x\in\widehat{\mathbb Z}\). Its residues modulo \(8\) and \(9\) are respectively \(1\) and \(7\). The integer \(25\) has both residues, so
\[
x+\widehat{\mathbb Z}=25/72+\widehat{\mathbb Z}.
\]
Indeed, the difference at \(2\) is \(-2/9\), and the difference at \(3\) is \(-1/8\), both integral in their respective fields. At every other prime the denominator \(72\) is a unit. This illustrates how independent local residues combine into one rational class.

The stages also have a useful countable form:
\[
\mathbb A_f=\bigcup_{j\geq1}\frac1{j!}\widehat{\mathbb Z}.
\tag{11}
\]
They increase because \(j!\mid(j+1)!\), and every denominator divides some factorial. They are compact open **additive subgroups**. For \(n>1\), \(n^{-1}\widehat{\mathbb Z}\) is not a subring: if \(p\mid n\), the square of the diagonal element \(1/n\) has valuation \(-2v_p(n)<-v_p(n)\) at \(p\), so it leaves that stage.

## Finite idèles and the normalization table

An element \(x\in\mathbb A_f\) is a ring unit exactly when every \(x_p\neq0\) and \(x_p\in\mathbb Z_p^\times\) for almost all \(p\). Necessity follows because both \(x\) and its inverse must be integral at almost all primes; sufficiency follows by taking the componentwise inverse. Thus, algebraically,
\[
\mathbb A_f^\times=\prod_p'(\mathbb Q_p^\times,\mathbb Z_p^\times).
\]
We give this **finite idèle group** the restricted product topology. Its compact open subgroup is \(\widehat{\mathbb Z}^\times\). This differs from its additive subspace topology; Exercise 2 identifies the correct topology through the graph of inversion.

For example, the tuple \((p)_p\) is an adèle with no zero coordinate, yet is not a unit: its coordinatewise inverse fails integrality at every prime. In contrast, a nonzero rational number gives a finite idèle, because its numerator and denominator involve only finitely many primes. The valuation map identifies
\[
\mathbb A_f^\times/\widehat{\mathbb Z}^\times\simeq\bigoplus_p\mathbb Z.
\]
It is surjective by taking \(x_p=p^{k_p}\) for a finitely supported integer tuple \((k_p)\), and its kernel is precisely the unit subgroup. The quotient is discrete because that subgroup is open.

All measures in this lesson use the following normalizations.

| Group | Distinguished compact open subgroup | Its measure | Useful consequence |
|---|---|---:|---|
| \((\mathbb Q_p,+)\) | \(\mathbb Z_p\) | \(1\) | \(\mu_p(p^k\mathbb Z_p)=p^{-k}\) |
| \(\mathbb Q_p^\times\) | \(\mathbb Z_p^\times\) | \(1\) | \(\mu_p^\times(p^k\mathbb Z_p^\times)=1\) |
| \((\mathbb A_f,+)\) | \(\widehat{\mathbb Z}\) | \(1\) | \(\mu(n^{-1}\widehat{\mathbb Z})=n\) |
| \(\mathbb A_f^\times\) | \(\widehat{\mathbb Z}^\times\) | \(1\) | multiplicative translates have measure \(1\) |

Here \(k\in\mathbb Z\) and \(n\geq1\). The additive local formula follows by partitioning \(\mathbb Z_p\) into its \(p^k\) residue cosets for \(k\geq0\); negative \(k\) follow by partitioning the larger ball into cosets of \(\mathbb Z_p\). The multiplicative formula is Haar invariance. Equation (9) shows that \(n^{-1}\widehat{\mathbb Z}\) has \(n\) additive cosets of \(\widehat{\mathbb Z}\), proving its measure formula. Proposition 1.2 gives both global normalizations.

### Worked example: a restricted box

The compact open set
\[
B=2^{-2}\mathbb Z_2\times(1+9\mathbb Z_3)
\times\prod_{p\neq2,3}\mathbb Z_p
\]
has additive measure \(4/9\). The first factor contributes \(4\), the second contributes \(1/9\), and every other factor contributes one. Translating the centre of a local ball leaves its additive measure unchanged. This example also explains why the tail factors in (2) must have measure one.

## Test functions made from local pieces

On \(\mathbb Q_p\), define a Bruhat–Schwartz function to be a locally constant, compactly supported complex function. Write this space as \(\mathcal S(\mathbb Q_p)\). On \(\mathbb A_f\) use the same definition. Then
\[
\mathcal S(\mathbb A_f)
=\operatorname{span}\left\{\bigotimes_p f_p:
f_p\in\mathcal S(\mathbb Q_p),\quad
f_p=1_{\mathbb Z_p}\text{ for almost all }p\right\}.
\tag{12}
\]

**Proof of (12).** A tensor on the right is locally constant. Its support is a finite product of compact local supports with the compact integral tail, so it is compact. Finite sums retain both properties.

Conversely, let \(f\) be locally constant with compact support. At each point of its support, choose a compact open restricted rectangle on which \(f\) is constant. Such rectangles exist because the local balls \(a+p^k\mathbb Z_p\) form a neighbourhood basis. The rectangles can lie inside \(\{f\neq0\}\): this set equals the support, since local constancy makes its complement open. Compactness gives a finite cover by these rectangles.

Include all their exceptional coordinates in one finite set \(S\). They now have the same tail \(\prod_{p\notin S}\mathbb Z_p\), and each local factor in \(S\) is compact and open. At each of these finitely many primes, partition the union of the local factors into the finitely many disjoint sets obtained by their intersections and differences. These sets are compact and open. The resulting finite rectangular partition makes \(f\) constant on each cell, and zero on cells outside its support. The indicator of every cell is a tensor of local compact open indicators with integral tail. Expressing \(f\) as its constant value times these indicators proves (12). \(\square\)

The same proof works for restricted products of groups whose local topologies have bases of compact open sets. More generally, given local test spaces \(\mathcal S(G_v)\) containing \(1_{K_v}\) outside \(E\), define their restricted tensor space as the span of \(\bigotimes_v f_v\) with \(f_v\in\mathcal S(G_v)\) and \(f_v=1_{K_v}\) for almost all \(v\). This definition specifies the local choices; it does not identify the resulting space with all of \(C_c(G)\).

For arbitrary LCA factors, the intrinsic construction of local Bruhat–Schwartz spaces uses their structure theory and is beyond this lesson. Formula (12) proves the full identification needed for finite adèles. With a Euclidean factor, the adelic test space is defined using finite sums of products of an ordinary Schwartz function on that factor and functions in (12).

For example,
\[
f=1_B-\frac49\,1_{\widehat{\mathbb Z}}
\]
belongs to \(\mathcal S(\mathbb A_f)\) and has integral zero. Both terms are factorizable, and their integrals are the measures already computed. Such finite local descriptions are what make adelic integration practical.

## Exercises

**Exercise 1 (easy).** Prove that the restricted product topology equals the subspace topology from \(\prod_vG_v\) if and only if \(K_v=G_v\) for almost all \(v\notin E\).

**Solution.** If equality holds outside a finite set, include that set in \(S\). Then \(G\) is the full product, and (1) is its product topology. Conversely, suppose infinitely many \(K_v\) are proper. The subgroup \(G_E\) is open in the restricted topology. Any product neighbourhood of the identity constrains only a finite set \(F\) of coordinates. Choose \(v\notin E\cup F\) with \(K_v\neq G_v\), and an element \(g_v\notin K_v\). The tuple with that single nonidentity coordinate belongs to \(G\) and to the chosen product neighbourhood but not to \(G_E\). Thus \(G_E\) is not open in the subspace topology, and the two topologies differ.

**Exercise 2 (medium).** Show that inversion on \(\mathbb A_f^\times\), with the subspace topology from \(\mathbb A_f\), is discontinuous. Show also that
\[
j:x\longmapsto(x,x^{-1})
\]
identifies the restricted product topology with the topology induced from \(\mathbb A_f\times\mathbb A_f\).

**Solution.** Enumerate the primes increasingly as \(q_r\). Let \(u^{(r)}\) have coordinate \(q_r\) at \(q_r\), and coordinate one elsewhere. Each tuple is an idèle. In an additive neighbourhood of one, only finitely many coordinates have extra local conditions; outside them, membership in \(\mathbb Z_p\) suffices. Consequently \(u^{(r)}\to1\) in \(\mathbb A_f\). But \((u^{(r)})^{-1}\notin\widehat{\mathbb Z}\) for every \(r\). Since \(\widehat{\mathbb Z}\) is an additive neighbourhood of one, these inverses do not converge to one. This proves discontinuity.

Take a basic product neighbourhood of \((x,x^{-1})\) in \(\mathbb A_f\times\mathbb A_f\), and enlarge its two finite indexing sets to one \(S\) containing the exceptional coordinates of \(x\) and \(x^{-1}\). Its inverse image under \(j\) has finite-coordinate conditions
\[
y_p\in U_p\cap V_p^{-1}\qquad(p\in S),
\]
which are open in \(\mathbb Q_p^\times\). Outside \(S\), both \(y_p\) and \(y_p^{-1}\) must be integral, equivalently \(y_p\in\mathbb Z_p^\times\). The inverse image is therefore open in the restricted topology.

Conversely, let a restricted basic neighbourhood of \(x\) prescribe \(y_p\in W_p\subseteq\mathbb Q_p^\times\) for \(p\in S\), and local units elsewhere. Each \(W_p\) is open in \(\mathbb Q_p\), because \(\mathbb Q_p^\times\) is open there. Use the additive basic sets with factors \(W_p\) and \(\mathbb Q_p\), respectively, at \(p\in S\), and integral tails for both. Their product pulls back under \(j\) to precisely that restricted neighbourhood. Hence both induced topologies agree, and injectivity of \(j\) proves the claimed identification.

**Exercise 3 (medium).** Compute the multiplicative measure and the additive measure of \(\widehat{\mathbb Z}^\times\), with the normalizations in the table.

**Solution.** Its multiplicative measure is one, by Proposition 1.2. Additively, \(\mathbb Z_p^\times=\mathbb Z_p\setminus p\mathbb Z_p\) has measure \(1-1/p\). Let
\[
C_N=\prod_{p\leq N}\mathbb Z_p^\times
\times\prod_{p>N}\mathbb Z_p.
\]
These compact sets decrease to \(\widehat{\mathbb Z}^\times\), within the set \(\widehat{\mathbb Z}\) of finite additive measure one. Continuity from above and the product formula give
\[
\mu(\widehat{\mathbb Z}^\times)
=\lim_{N\to\infty}\prod_{p\leq N}(1-1/p)=0.
\]
For completeness, the limit is zero without any asymptotic theorem about primes. Multiplying the finitely many geometric series gives
\[
\prod_{p\leq N}(1-1/p)^{-1}
=\sum_{\substack{m\geq1\\\text{every prime divisor of }m\leq N}}\frac1m
\geq\sum_{m=1}^{\lfloor N\rfloor}\frac1m.
\]
The harmonic sums diverge: each block \(2^{k-1}<m\leq2^k\) contributes at least \(1/2\). This proves the zero limit. The different answers arise from two different Haar measures on two different groups.

**Exercise 4 (hard).** Reconstruct the proof of Theorem 1.3 using an open annihilator to establish the topology. Treat the compact integral tail as a whole, rather than assuming a continuous character is a finite product in advance.

**Solution.** For a tuple \((\chi_v)\) in the restricted dual product, the formula \(\chi(x)=\prod_v\chi_v(x_v)\) has only finitely many nontrivial factors. It is multiplicative and continuous on every chart containing the tuple's exceptional coordinates, hence on \(G\).

For a continuous \(\chi\) on \(G\), choose \(B(S;U)\) mapped into \(\{\operatorname{Re}z>0\}\). Its tail subgroup \(T_S\) has trivial image by the circle argument. The coordinate restrictions consequently annihilate \(K_v\) outside \(S\). Splitting any element into its finitely many exceptional coordinates and a tail element recovers the product formula and proves bijectivity.

For continuity of the product map, put a given compact set \(C\) inside \(G_S\). Within the dual chart \(H_S\), the tail contributes one on \(C\). Uniformly small evaluations on the finitely many compact projections \(C_v\) make the product uniformly small, using the product inequality in the theorem's proof.

For continuity in the other direction, the condition of belonging to \(H_S\) is exactly membership in \(T_S^\perp\). The latter is open in \(\widehat G\), because its defining triviality condition can be tested by uniform containment of the image of the compact subgroup \(T_S\) in the same circle arc. On that open subgroup, any finite-coordinate neighbourhood is obtained by the continuous restriction maps \(\widehat G\to\widehat G_v\). Thus every restricted basic neighbourhood has open image. The two continuity statements prove the topological isomorphism, including for uncountable index sets and with unrestricted factors in \(E\).

## Prerequisites and further directions

The following are the background results used here.

- The compact-product theorem is Lemma 4.1 of Spectral radius and characters of a Banach algebra, with a proof for arbitrary products using the axiom of choice. A continuous surjection \(f:X\to Y\) from a compact space to a Hausdorff space is closed: every closed subset of \(X\) is compact, so its image is compact and hence closed in \(Y\). If \(f^{-1}(B)\) is closed, surjectivity gives \(B=f(f^{-1}(B))\), which is therefore closed; the converse follows from continuity. Thus \(f\) is a quotient map. If it is also bijective, its closedness makes the inverse continuous, so it is a homeomorphism. Bézout’s identity for coprime integers is assumed; the Chinese remainder argument was given above.
- Riesz representation for positive functionals on \(C_c(X)\), Haar existence and uniqueness on locally compact Hausdorff groups, and finite Radon products with their integrable-function Fubini theorem are proved in Haar measure on locally compact groups, Theorem 2.2, Definition 4.3, Theorem 5.1, Theorems 8.3 and 9.2, and Proposition 12.1. No global \(\sigma\)-finiteness is assumed.
- The dual of an LCA group is LCA by Corollary 2.2 of [The dual group as the Gelfand spectrum of \(L^1(G)\)](prerequisites/HA-LCA-03.md). Compact groups have discrete duals and discrete groups have compact duals by Theorem 2.1 of Characters and the dual group; its Proposition 4.1 and Theorem 4.3 give finite-product and arbitrary compact-product/discrete-sum duality. Evaluation identifies \(H\) with \(\widehat{\widehat H}\) by Theorem 2.1 of The Pontryagin duality theorem, whose Corollary 4.4 gives the compact/discrete converse implications.
- For closed \(K\leq H\), pullback identifies \(\widehat{H/K}\) with \(K^\perp\), and restriction identifies \(\widehat H/K^\perp\) with \(\widehat K\), topologically. These are Theorem 2.1 of Subgroups, quotients and annihilators. Its Corollary 2.2 proves that annihilation exchanges compact and open subgroups. In particular, the annihilator of a compact open subgroup is compact and open.
- For a surjective inverse system of compact abelian groups, every character of the limit factors through a coordinate group, and its discrete dual is the direct limit of the coordinate duals under pullback. This is Proposition 4.2 of Totally disconnected groups, the p-adic numbers and the adèles. We use its independent general proof for finite cyclic groups, with the explicit pullback maps given above; its later adelic examples are not needed.
- The construction of \(\mathbb Q_p\), its valuation and the compact open ring \(\mathbb Z_p\) are Theorem 2.1 and Proposition 2.2 of Completions, the p-adic numbers and complete discretely valued fields. Proposition 2.3 gives the corresponding inverse-limit description for a complete discrete valuation ring. The elementary residue and unit calculations needed for (6)–(9) were proved here.

The self-duality of \(\mathbb Q_p\) and of the adèles, the diagonal lattice in the full adèle ring, and Poisson summation are treated in *The adèle ring of a number field* and *Additive characters, self-dual measures and Poisson summation on the adèles*.

## References

- [Getz–Hahn] J. R. Getz and H. Hahn, *An Introduction to Automorphic Representations: With a View toward Trace Formulae*, [author-hosted draft dated 22 April 2022](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), §2.3, pp.46–48. These locators refer to that draft.
- [Bost–Connes] J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica (N.S.) 1 (1995), 411–457, §3, pp.422–423, the finite-adèle definition (a)–(c). [Author-hosted scan](https://alainconnes.org/wp-content/uploads/bostconnesscan.pdf).
- [Sutherland 25] A. V. Sutherland, *The ring of adeles, strong approximation*, MIT 18.785, Lecture 25 (29 November 2021), [MIT OpenCourseWare notes](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/resources/mit18_785f21_lec25/), §§25.1–25.4, pp.1–10.
- [Lenstra] H. Lenstra, *Profinite Groups*, [Leiden-hosted notes](https://websites.math.leidenuniv.nl/algebra/Lenstra-Profinite.pdf), §2, Example 2.2, p.3, for the inverse-limit, prime-product and factorial presentations of \(\widehat{\mathbb Z}\). The residue and character proofs used here are given above.
