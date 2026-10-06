# Dual balls and compact convexity

**Programme reading HA-LCA-PRE-DUAL-CONVEX.** Self-checked by the writing AI. The measure statements use the full completed, locally determined Haar domain on an arbitrary locally compact Hausdorff group. The convexity statements apply to weak-star compact subsets of the dual of any complex normed space, without a separability assumption.

The freely accessible readings are D. H. Fremlin's *Measure Theory*, [§243, version of 30 April 2004 in the volume 2 source collection of 2016](https://www1.essex.ac.uk/maths/people/fremlin/mt2.2016/mt243.tex), 243F–G, and Günther Hörmann's [*Advanced Functional Analysis*, summer semester 2023, corrected 13 September 2024](https://www.mat.univie.ac.at/~gue/lehre/23AFA/AFA.pdf), §5.11 on printed pages 71–73 and §§6.5–6.6. The local duality proof uses finite-measure Hilbert representation and explicit gluing. The separation proof uses finitely many coordinates and Euclidean minimization. Thus none of the source's external Radon–Nikodým, gluing or Hahn–Banach references is an unproved dependency.

This adapted component is distributed under the [Design Science License](../../assets/fremlin/DESIGN-SCIENCE-LICENSE.txt). The unchanged volume 2 source package, with its original notices, is retained. The other reading's prose and figures are not reproduced.

## 1. The full Haar domain and its duality

Throughout this section, \((G,\Sigma,\mu)\) is the space constructed in [the general Haar domain theorem](nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-theorem-3-1). In particular, choose an open, closed, sigma-compact subgroup \(H\), representatives \(r\) for the left cosets, and an increasing compact exhaustion \(K_n\) of \(H\). A set is in \(\Sigma\) precisely when its section in each \(rH\) is measurable for the completed Haar measure on that coset. Its measure is the sum of those section measures, where an arbitrary sum of nonnegative numbers means the supremum of its finite subsums. We write
\[
 \langle f,q\rangle_\mu=\int_G f(x)q(x)\,d\mu(x)
       \quad(f\in L^1(\mu),\ q\in L^\infty(\mu)).          \tag{1}
\]
This pairing is complex bilinear; a bar is not implicit in it.

<a id="ha-lca-pre-dual-convex-lemma-1-1"></a>
### Lemma 1.1. Finite pieces and arbitrary gluing

There is a partition \(G=\bigsqcup_{i\in I}E_i\) into measurable sets of finite measure with these properties:

1. A subset \(A\) belongs to \(\Sigma\) if and only if \(A\cap E_i\) is measurable in every piece.
2. For every \(A\in\Sigma\), \(\mu(A)=\sum_i\mu(A\cap E_i)\).
3. Functions measurable on the pieces glue to a \(\Sigma\)-measurable function; null sets on the pieces glue to a null set.
4. If \(h\ge0\) is measurable, then
\[
 \int_G h\,d\mu=\sum_i\int_{E_i}h\,d\mu.                  \tag{2}
\]
For \(f\in L^1\), only countably many pieces have a nonzero integral of \(|f|\), \(f\) is zero almost everywhere off their union, and its restrictions to finite subcollections approximate it in \(L^1\).

**Proof.** Put \(K_0=\varnothing\), \(D_n=K_n\setminus K_{n-1}\), and \(E_{(r,n)}=rD_n\). These are disjoint Borel sets covering \(G\), and \(\mu(E_{(r,n)})\le\mu(rK_n)<\infty\). Within a fixed coset, measurability of all intersections with \(E_{(r,n)}\) is equivalent to measurability of their countable union, by the sigma-algebra property. The defining coset criterion then proves assertion 1. Countable additivity inside each coset, followed by the arbitrary coset sum, proves assertion 2: both iterated sums equal the supremum of sums over finite sets of pairs \((r,n)\). Indeed a finite set of pairs is contained in finitely many rows with finite selections in each, and conversely every such finite selection is a finite set of pairs.

For a glued function, the inverse image of any Borel set has measurable intersection with every piece, so assertion 1 proves its measurability. Assertion 2 shows that the union of null piece sets has measure zero. This proves assertion 3 even when \(I\) is uncountable.

For a nonnegative simple function, (2) follows from assertion 2 and finite distributivity of nonnegative sums. For a general \(h\), the earlier [definition of the integral and monotone convergence](integration-and-l1.md#ha-lca-pre-integral-theorem-1-2) show that every simple \(s\le h\) has integral at most the right side of (2), giving the upper bound. For the reverse bound, on any finite collection of pieces choose simple lower approximations to \(h\), extend them by zero and add them. Taking their integral suprema gives the sum of the integrals on that finite collection. Taking the supremum over finite collections gives the reverse inequality, including infinite values.

If the sum in (2) for \(|f|\) is finite, for each integer \(m\ge1\) there are only finitely many indices with \(\int_{E_i}|f|\ge1/m\); otherwise finite subsums would be arbitrarily large. Every positive summand lies in one of these finite sets. Hence there are only countably many positive summands. On each other piece \(f=0\) almost everywhere by the earlier [zero-integral criterion](integration-and-l1.md#ha-lca-pre-integral-corollary-1-3); assertion 3 glues the exceptional sets to a null set. Enumerating the positive summands and using their convergent sum shows that the \(L^1\) norm of the omitted tail tends to zero. If there are no positive summands, \(f=0\) in \(L^1\). \(\square\)

<a id="ha-lca-pre-dual-convex-theorem-1-2"></a>
### Theorem 1.2. \(L^\infty=(L^1)^*\), with the exact norm

Every bounded complex linear functional \(\Lambda:L^1(\mu)\to\mathbb C\) has a unique representing class \(q\in L^\infty(\mu)\) such that
\[
 \Lambda(f)=\int_G fq\,d\mu\quad(f\in L^1),\qquad
 \|\Lambda\|=\|q\|_\infty.                               \tag{3}
\]
Conversely, every \(q\in L^\infty\) defines such a functional. This is a complex linear isometric bijection.

**Proof.** The bound \(\int|fq|\le\|q\|_\infty\int|f|\) follows by choosing a representative bounded by \(\|q\|_\infty\) off a null set and using monotonicity of the integral. Such a representative exists: intersect the full-measure bounds \(|q|\le\|q\|_\infty+1/n\). Thus (1) is well-defined on classes and defines a bounded complex linear functional of norm at most \(\|q\|_\infty\).

For the converse set \(C=\|\Lambda\|\) and use Lemma 1.1. On a piece \(E_i\) of positive finite measure, extend its functions by zero to \(G\). The earlier [Cauchy–Schwarz inequality](hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-lemma-1-1), applied in the [complete \(L^2(E_i)\) space](hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-theorem-6-1), gives
\[
 \|f\|_1\le\mu(E_i)^{1/2}\|f\|_2.
\]
Therefore the restriction of \(\Lambda\) to \(L^2(E_i)\) is bounded. The earlier [Hilbert representation theorem](hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-theorem-2-3), with the inner product linear in the first variable, supplies \(v_i\in L^2(E_i)\) such that
\[
 \Lambda(f)=\int_{E_i} f\,\overline{v_i}\,d\mu
                  \quad(f\in L^2(E_i)).                 \tag{4}
\]
For \(\varepsilon>0\), let \(A=\{x\in E_i:|v_i(x)|>C+\varepsilon\}\). The function
\[
 f=1_A\,v_i/|v_i|,
\]
defined as zero when its numerator vanishes, is in \(L^2(E_i)\). If \(\mu(A)>0\), (4) gives
\[
 |\Lambda(f)|=\int_A|v_i|\,d\mu
       \ge(C+\varepsilon)\mu(A)>C\|f\|_1,
\]
contradicting the definition of \(C\). Thus \(\mu(A)=0\). Taking \(\varepsilon=1/n\) proves \(|v_i|\le C\) almost everywhere.

Put \(q_i=\overline{v_i}\) and modify it on its null exceptional set to have \(|q_i|\le C\) everywhere on \(E_i\). On a zero-measure piece take \(q_i=0\). The bounded simple functions on a finite-measure piece are in \(L^2\) and are dense in \(L^1\) by the earlier [simple approximation theorem](integration-and-l1.md#ha-lca-pre-integral-lemma-2-3). Consequently continuity extends (4) to all \(L^1\) functions on that piece. Choice selects representatives on all pieces; Lemma 1.1 glues them to a measurable \(q\) bounded everywhere by \(C\). Finite sums of piece restrictions of an arbitrary \(f\in L^1\) converge to \(f\) in \(L^1\). Both \(\Lambda\) and integration against \(q\) are continuous, so their equality on those finite sums gives (3) without its norm equality yet.

To obtain the exact norm, let \(0<a<\|q\|_\infty\). Then \(A=\{|q|>a\}\) has positive measure. By Lemma 1.1 some \(A\cap E_i=F\) has \(0<\mu(F)<\infty\). Set
\[
 f(x)=\frac{1_F(x)\overline{q(x)}}{\mu(F)|q(x)|},
\]
with value zero outside \(F\). It has \(L^1\) norm one and
\(\int fq=\mu(F)^{-1}\int_F|q|\ge a\). Hence \(\|\Lambda_q\|\ge a\). Letting \(a\) increase to \(\|q\|_\infty\), and also treating \(q=0\), proves the norm equality. Applied to a difference of two representatives of the same functional, this equality proves uniqueness. Linearity of the correspondence is the bilinearity of (1). \(\square\)

<a id="ha-lca-pre-dual-convex-corollary-1-3"></a>
### Corollary 1.3. Continuous representatives and dense tests

A bounded continuous function has essential-supremum norm equal to its uniform norm. Two bounded continuous functions representing the same \(L^\infty\) class are identical.

Let \(q_d,q\in L^\infty\), with \(\sup_d\|q_d\|_\infty\le R\) and \(\|q\|_\infty\le R<\infty\). Then
\[
 \int fq_d\longrightarrow\int fq\quad(f\in L^1)
 \quad\Longleftrightarrow\quad
 \int hq_d\longrightarrow\int hq\quad(h\in C_c(G)).       \tag{5}
\]

**Proof.** If \(|h(x_0)|>a\) for a continuous \(h\), the set \(\{|h|>a\}\) contains a nonempty open neighbourhood of \(x_0\). It has positive Haar measure by the earlier [full-support theorem](nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-theorem-3-1). Thus every \(a<\|h\|_\infty\) is at most \(\|h\|_{\mathrm{ess}\,\infty}\). The reverse inequality is immediate. Applying this equality to a difference proves the uniqueness assertion.

The forward implication in (5) uses \(C_c\subseteq L^1\), because compact sets have finite measure. Conversely, the earlier [\(C_c\) density theorem on the full Haar domain](nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-lemma-5-1) allows an \(h\in C_c\) with \(\|f-h\|_1\) arbitrarily small. Then
\[
 \left|\int f(q_d-q)\right|
 \le 2R\|f-h\|_1+\left|\int h(q_d-q)\right|.
\]
First choose \(h\) and then a sufficiently late \(d\). This proves convergence for every \(f\). If \(R=0\), all classes vanish and the assertion is immediate. \(\square\)

## 2. Weak-star topology, compactness and separation

Let \(E\) be a complex normed space. Its dual \(E^*\) consists of bounded complex linear maps \(\ell:E\to\mathbb C\), with norm
\(\|\ell\|=\sup_{\|x\|\le1}|\ell(x)|\). The **weak-star topology** \(\sigma(E^*,E)\) is the topology generated by the evaluations \(\ell\mapsto\ell(x)\). A neighbourhood basis at \(\ell_0\) consists of
\[
 U(\ell_0;x_1,\ldots,x_n;\varepsilon)
 =\{\ell:|(\ell-\ell_0)(x_j)|<\varepsilon,\ 1\le j\le n\},
 \qquad \varepsilon>0.                                 \tag{6}
\]
Evaluations separate points of \(E^*\) by the definition of different functions. Hence this topology is Hausdorff. Addition and scalar multiplication are continuous: after fixing finitely many \(x_j\), the necessary estimates are the corresponding finite scalar estimates. In particular, sums, scalar multiples and finite convex combinations of convergent nets have the corresponding limits. A net converges weak-star exactly when all its evaluations converge.

<a id="ha-lca-pre-dual-convex-theorem-2-1"></a>
### Theorem 2.1. Compact dual balls

For \(R\ge0\), the ball
\[
 B_R(E^*)=\{\ell:\|\ell\|\le R\}
\]
is weak-star compact and closed. The dual norm is weak-star lower semicontinuous. Every net in a weak-star compact set has a convergent subnet whose limit belongs to that set.

In particular, under Theorem 1.2, every closed norm ball of \(L^\infty(G,\Sigma,\mu)\) is compact for the topology of the pairings (1).

**Proof.** For each \(x\in E\) the closed complex disk
\(D_x=\{z:|z|\le R\|x\|\}\) is compact by the earlier [finite-dimensional compactness theorem](banach-spectrum.md#ha-lca-pre-banach-lemma-1-1). Thus
\[
 P=\prod_{x\in E}D_x
\]
is compact by the earlier [arbitrary product theorem](banach-spectrum.md#ha-lca-pre-banach-lemma-4-1). A point \(a=(a_x)\) represents an element of \(B_R(E^*)\) exactly when
\[
 a_{x+y}=a_x+a_y,\qquad a_{\alpha x}=\alpha a_x
             \quad(x,y\in E,\ \alpha\in\mathbb C).       \tag{7}
\]
These are closed coordinate conditions. If they hold, \(x\mapsto a_x\) is complex linear and satisfies \(|a_x|\le R\|x\|\), which proves boundedness and the claimed norm bound. Conversely every element of the ball satisfies (7). The evaluation map therefore identifies the ball with a closed subset of \(P\), and its induced product topology is exactly (6). This proves compactness, including \(E=\{0\}\) and \(R=0\).

For any \(R\ge0\), inside the whole dual the same ball is the intersection of the closed sets
\[
 \{\ell:|\ell(x)|\le R\|x\|\}\qquad(x\in E).
\]
Thus every sublevel set of the norm is closed, which is lower semicontinuity. More explicitly, if \(\|\ell\|>a\ge0\), some unit vector \(x\) has \(|\ell(x)|>a\); a weak-star neighbourhood of \(\ell\) retains this strict inequality. It follows in particular that if \(\ell_d\to\ell\) and \(\|\ell\|=1\), then eventually \(\|\ell_d\|>a\) for each \(a<1\).

The earlier [compact-net argument](hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-theorem-5-1) was proved for an arbitrary compact space: intersect closures of tails and index a subnet by triples consisting of a tail index, a neighbourhood of the resulting cluster point, and a later index whose point belongs to that neighbourhood. Its index map is both increasing and cofinal. Applying that proved argument to the compact set here gives the asserted subnet, with no countability condition.

Finally the linear bijection in Theorem 1.2 preserves norms and sends evaluation at \(f\in L^1\) precisely to the pairing (1). It therefore transports both the balls and their stated topologies, proving the \(L^\infty\) assertion. \(\square\)

<a id="ha-lca-pre-dual-convex-lemma-2-2"></a>
### Lemma 2.2. Separating a point from a compact convex set

Let \(C\subset E^*\) be nonempty, weak-star compact and convex, and let \(\ell_0\notin C\). There is \(x\in E\) such that
\[
 \operatorname{Re}\ell_0(x)>
       \sup_{\ell\in C}\operatorname{Re}\ell(x).         \tag{8}
\]
The supremum is finite and attained.

**Proof.** A compact subset of a Hausdorff space is closed. For the precise elementary argument used here, for each \(c\in C\) choose disjoint neighbourhoods of \(c\) and \(\ell_0\); finitely many of the former cover \(C\), and the intersection of the latter is a neighbourhood of \(\ell_0\) disjoint from \(C\). By (6) there are \(x_1,\ldots,x_n\) and \(\varepsilon>0\) for which that basic neighbourhood misses \(C\). Necessarily \(n\ge1\). Define
\[
 T:E^*\longrightarrow\mathbb R^{2n},\qquad
 T\ell=(\operatorname{Re}\ell(x_1),\operatorname{Im}\ell(x_1),
                    \ldots,\operatorname{Re}\ell(x_n),\operatorname{Im}\ell(x_n)).
\]
This map is continuous and real linear. Its image \(D=T(C)\) is nonempty, compact and convex. The point \(b=T\ell_0\) is not in \(D\), since equality with a point of \(D\) would give all the coordinate differences zero and hence a point of \(C\) in the forbidden neighbourhood.

The continuous function \(z\mapsto|b-z|^2\) attains its minimum on \(D\), by the earlier [compact-extrema theorem](banach-spectrum.md#ha-lca-pre-banach-lemma-1-1). Let \(z_0\) be a minimizer and \(v=b-z_0\ne0\). For \(z\in D\) and \(0<t\le1\), convexity and minimality give
\[
 |v-t(z-z_0)|^2\ge|v|^2.
\]
Expanding and dividing by \(2t\) yields
\[
 v\cdot(z-z_0)\le\tfrac12t|z-z_0|^2.
\]
Letting \(t\downarrow0\) proves \(v\cdot z\le v\cdot z_0\). Consequently
\[
 v\cdot b=v\cdot z_0+|v|^2>\sup_{z\in D}v\cdot z.       \tag{9}
\]
Write \(v=(a_1,b_1,\ldots,a_n,b_n)\) and set
\(x=\sum_{j=1}^n(a_j-i b_j)x_j\). Complex linearity gives
\[
 \operatorname{Re}\ell(x)
  =\sum_j\big(a_j\operatorname{Re}\ell(x_j)
                         +b_j\operatorname{Im}\ell(x_j)\big)
  =v\cdot T\ell.
\]
Thus (9) is (8). This functional is continuous, so its real image of \(C\) is compact and has a maximum, as asserted. \(\square\)

## 3. Extreme points

For a convex set \(K\) in a real or complex vector space, a nonempty convex subset \(F\subseteq K\) is a **face** if
\[
 0<t<1,\quad a,b\in K,\quad ta+(1-t)b\in F
                      \quad\Longrightarrow\quad a,b\in F.       \tag{10}
\]
A point is **extreme** if its singleton is a face. Denote the set of extreme points by \(\operatorname{Ext}K\). Convexity always uses real coefficients in \([0,1]\).

<a id="ha-lca-pre-dual-convex-lemma-3-1"></a>
### Lemma 3.1. Compact faces have extreme points

Every nonempty weak-star compact convex \(K\subset E^*\) has an extreme point. More generally, each nonempty compact face \(F_0\) of \(K\) contains an extreme point of \(K\). If \(x\in E\), the functional \(\ell\mapsto\operatorname{Re}\ell(x)\) attains its maximum over \(K\) at an extreme point.

**Proof.** Intersections of faces, when nonempty, are faces: convexity and implication (10) hold in every constituent set and therefore in their intersection. A face of a face of \(K\) is a face of \(K\): if a strict convex combination in \(K\) lies in the smaller face, first apply (10) for the larger face to place its endpoints there, and then apply (10) for the smaller face. Singletons are compact in any topology.

The set \(K\) itself is a face of \(K\). Given a compact face \(F_0\), order all nonempty compact faces of \(K\) contained in \(F_0\) by reverse inclusion. Every nonempty chain has an upper bound given by its intersection. Indeed, its members are closed subsets of the compact Hausdorff set \(F_0\); a finite subcollection has intersection equal to its smallest member, which is nonempty. Compactness, or equivalently the finite-intersection property obtained by taking complements of open covers, makes the entire intersection nonempty. It is compact and is a face by the first paragraph. An empty chain has upper bound \(F_0\). The maximal principle for sets therefore supplies a face \(F\) minimal by inclusion.

Suppose \(\ell_1,\ell_2\in F\) are distinct. Choose \(x\in E\) with \((\ell_1-\ell_2)(x)\ne0\). Multiplying \(x\) by the conjugate phase of this nonzero number makes
\(\operatorname{Re}\ell_1(x)\ne\operatorname{Re}\ell_2(x)\). Let
\[
 c=\max_{\ell\in F}\operatorname{Re}\ell(x),\qquad
 F'=\{\ell\in F:\operatorname{Re}\ell(x)=c\}.
\]
The maximum exists because \(F\) is compact. Its level set is nonempty, closed and convex, and is a proper subset of \(F\), since the displayed functional takes two different values there. It is a face of \(F\): a strict weighted average of two numbers at most \(c\) equals \(c\) only when both numbers equal \(c\). By face transitivity it is a compact face of \(K\), contradicting minimality. Thus \(F\) is a singleton; its point is extreme in \(K\). Taking \(F_0=K\) proves the first assertion.

Finally the same maximum-level construction applied directly to \(K\) gives a nonempty compact face of maximizers for any fixed \(x\in E\). The result just proved gives an extreme point of \(K\) in that face. \(\square\)

<a id="ha-lca-pre-dual-convex-theorem-3-2"></a>
### Theorem 3.2. The compact-convex extreme-point theorem

For every nonempty weak-star compact convex \(K\subset E^*\),
\[
 K=\overline{\operatorname{conv}(\operatorname{Ext}K)}^{\,w^*}.   \tag{11}
\]
The convex hull here consists of finite convex combinations.

**Proof.** Finite convex combinations form a convex set: a convex combination of two finite convex combinations is another such combination, by multiplying their nonnegative coefficients and retaining their total sum one. Every convex set containing \(\operatorname{Ext}K\) contains those combinations by induction on the number of terms.

The closure of a convex subset \(A\) is convex in this topology. To see this directly, if \(a,b\in\bar A\), \(0<t<1\), and a finite-coordinate neighbourhood of \(ta+(1-t)b\) with radius \(\varepsilon\) is prescribed, choose \(a',b'\in A\) approximating \(a,b\) on those coordinates within \(\varepsilon\). Then the same coordinates of \(ta'+(1-t)b'\) differ from those of \(ta+(1-t)b\) by less than \(t\varepsilon+(1-t)\varepsilon=\varepsilon\). The cases \(t=0,1\) are immediate.

Set \(C=\overline{\operatorname{conv}(\operatorname{Ext}K)}^{\,w^*}\). By Lemma 3.1 it is nonempty. Since \(K\) is compact and Hausdorff, it is closed by the argument in Lemma 2.2, so \(C\subseteq K\). The set \(C\) is closed, compact and convex. If some \(\ell_0\in K\) were outside \(C\), Lemma 2.2 would give an \(x\in E\) such that
\[
 \operatorname{Re}\ell_0(x)>
                \sup_{\ell\in C}\operatorname{Re}\ell(x).
\]
But Lemma 3.1 supplies a point \(p\in\operatorname{Ext}K\subseteq C\) maximizing this functional over \(K\). Then
\(\operatorname{Re}p(x)\ge\operatorname{Re}\ell_0(x)\), contradicting the strict inequality. Hence \(K=C\). \(\square\)

<a id="ha-lca-pre-dual-convex-corollary-3-3"></a>
### Corollary 3.3. Recovering a normalized boundary

Let \(K\) be a nonempty weak-star compact convex subset of \(B_1(E^*)\), with \(0\in K\). Suppose that every nonzero extreme point of \(K\) has norm one. Put
\[
 A=\operatorname{Ext}K\setminus\{0\}.
\]
Every \(q\in K\) of norm one is a weak-star limit of finite convex combinations of points of \(A\).

This assertion does not require the norm-one subset of \(K\) to be closed, compact or convex.

**Proof.** Fix \(q\in K\) with \(\|q\|=1\). By Theorem 3.2, every weak-star neighbourhood \(U\) of \(q\) contains a finite convex combination \(s_U\) of points of \(\operatorname{Ext}K\). Direct these neighbourhoods by reverse inclusion and choose one such combination for each. For every neighbourhood \(V\), all later \(U\subseteq V\) have \(s_U\in V\). Thus \(s_U\to q\).

In the selected expression for \(s_U\), omit any zero extreme points and let \(t_U\in[0,1]\) be the sum of the remaining coefficients. By the triangle inequality and the assumed norms of the remaining points,
\[
 \|s_U\|\le t_U\le1.
\]
The lower semicontinuity conclusion of Theorem 2.1 shows that, for every \(a<1\), eventually \(\|s_U\|>a\). Consequently \(t_U\to1\), and \(t_U>0\) on a tail of the directed set. On that tail set \(r_U=s_U/t_U\). Dividing the remaining coefficients by \(t_U\) makes \(r_U\) a finite convex combination of points of \(A\).

For every \(x\in E\),
\[
 |r_U(x)-s_U(x)|
 =\frac{1-t_U}{t_U}|s_U(x)|
 \le(1-t_U)\|x\|\longrightarrow0.
\]
Together with \(s_U(x)\to q(x)\), this proves \(r_U\to q\) weak-star. In particular, \(A\) is nonempty whenever \(K\) has a norm-one point. \(\square\)

## Source reading and scope

Fremlin 243F–G motivates the duality problem and its dependence on the measure domain. The full Haar domain has been partitioned and glued explicitly above, so no general localizability or Radon–Nikodým theorem is silently invoked. Hörmann §5.11 supplies the compact-face argument; the required strict separation is proved in Lemma 2.2 in the exact weak-star setting used here. His §§6.5–6.6 supply the product-compactness approach to dual balls; the product theorem itself is already proved in the earlier programme.

The reading establishes these eight source and proof obligations only. It does not yet identify positive-type functions, prove their GNS theorem, or classify the extreme points of their ball. Those are separate statements in the positive-type lesson.
