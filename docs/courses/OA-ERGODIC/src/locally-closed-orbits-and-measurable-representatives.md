# Locally closed orbits and measurable representatives

An orbit space may distinguish every orbit topologically and still fail to be Hausdorff. The useful question for measure theory is whether its Borel sets have a countable description and whether one can choose an orbit representative measurably. This lesson proves the Glimm criterion, including its ergodic-measure converse and its representative construction, for a continuous action of a Polish group.

Read [Polish orbits and their quotient topology](polish-orbits-and-their-quotient-topology.md) first. We use its complete Effros equivalence and countable invariant-open orbit code. The exact written programme prerequisites are *Polish and standard Borel spaces*, Theorems 1.1, 2.4 and 4.3, Theorem 5.6 (Blackwell), and Proposition 7.4, in *Operator algebra foundations*. They supply a continuous Baire-space parametrization, analytic separation and injective Borel images, the countably generated atom theorem, and standard Borel coset spaces. Their proofs are present in that programme lesson. The category, Cantor construction, probability argument and measurable selector needed below are proved here.

Throughout, \(G\) is Polish, \(X\) is a nonempty Polish space, and \(G\times X\to X\) is continuous. Write \(\pi:X\to Y=X/G\), and equip \(Y\) with both its quotient topology \(\tau_q\) and its quotient Borel structure

\[
\mathcal B_q=\{A\subset Y:\pi^{-1}(A)\in\mathcal B(X)\}.
\tag{1.1}
\]

An orbit is **locally closed** if it is open in its closure in \(X\). This is equivalent to being the intersection of an open and a closed subset of \(X\). Ergodic means that every invariant Borel set has either zero measure or conull complement. We do not require quasi-invariance.

## 1. The criterion and the closure conditions

**Condition C.** Every identity neighborhood \(N\) contains an identity neighborhood \(M\) such that, simultaneously for all \(x\in X\),

\[
\overline{Mx}^{\,X}\subset Nx.
\tag{1.2}
\]

**Condition D.** Every identity neighborhood \(N\) contains an identity neighborhood \(M\) such that, for every \(x\) and every open neighborhood base \((Q_n)\) at \(x\),

\[
\bigcap_n\overline{M Q_n}^{\,X}\subset Nx.
\tag{1.3}
\]

The bars are ambient closures, and the neighborhoods in the base need not be nested. D implies C: \(Mx\subset M Q_n\) for each \(n\), so its closure is contained in the intersection in (1.3). Locally compact Polish groups satisfy both conditions for every continuous action, by the compact-neighborhood proof in the preceding lesson, Proposition 6.1.

**Theorem 1.1 (Glimm criterion).** Assume C. The following six conditions are equivalent:

1. Every orbit is locally closed.
2. \(\mathcal B_q=\sigma(\tau_q)\).
3. \((Y,\mathcal B_q)\) is countably separated.
4. Every nonzero ergodic sigma-finite Borel measure on \(X\) is concentrated on one orbit.
5. \((Y,\mathcal B_q)\) is standard Borel.
6. There is a Borel subset of \(X\) meeting every orbit exactly once.

Thus, in particular, all six are equivalent under D, as in the source exercise. The proof of the representative implication actually requires only a \(T_0\) quotient. Under C the first four conditions imply that property. Burgess's general selection theorem is broader: it handles countably separated orbit relations on invariant Borel subsets without C or a \(T_0\) quotient.

The elementary forward implications come in Section 2. Sections 3–5 construct the measure needed for the converse. Section 6 constructs the representative and closes the proof.

## 2. Category and countable orbit descriptions

**Lemma 2.1.** Under C, an orbit that is nonmeagre in a closed invariant subspace \(F\subset X\) is open in \(F\).

*Proof.* Choose a neighborhood \(N\) and then \(M\) as in C, shrinking \(M\) to an open identity neighborhood if necessary. Separability of \(G\) gives \(G=\bigcup_j g_jM\): a countable dense set meets every open set \(gM^{-1}\). Hence \(Gx=\bigcup_j g_jMx\). If this orbit is nonmeagre in \(F\), one of these pieces, and therefore \(Mx\), is nonmeagre in \(F\). Its closure in \(F\) has nonempty interior, since a closed set with empty interior is nowhere dense. That closure is contained in \(\overline{Mx}^{\,X}\subset Nx\subset Gx\). Thus the orbit contains a nonempty relatively open subset of \(F\). Translates of this subset give an open neighborhood of each orbit point, because \(F\) is invariant. Their union is the orbit. \(\square\)

**Lemma 2.2.** Suppose a continuous action on a nonempty Polish space \(F\) has a dense orbit. Every invariant Borel subset of \(F\) is meagre or comeagre.

*Proof.* The sets with the Baire property form a sigma-algebra: complements are handled by replacing the complement of an open set by its interior, whose omitted boundary is nowhere dense; countable unions differ from the corresponding union of open sets by a meagre set. Thus every Borel set has that property. If an invariant Borel set \(A\) is nonmeagre, some nonempty open \(W\subset F\) has \(W\setminus A\) meagre.

The dense orbit implies topological transitivity: for nonempty open \(U,V\), choose \(gx\in U\) and \(hx\in V\); then \(hg^{-1}U\) meets \(V\). Consequently \(GW\) is dense and open. It has a countable subcover by translates of \(W\), since \(F\) is second countable. Invariance makes \(A\) comeagre in every translate and hence in \(GW\). The complement of \(GW\) is nowhere dense. Therefore \(A\) is comeagre in \(F\). \(\square\)

**Proposition 2.3.** Under C, condition 3 implies condition 1.

*Proof.* Fix \(x\), and put \(F=\overline{Gx}\). This is a nonempty closed invariant Polish space with a dense orbit. Pull a countable separating family in \(Y\) back to invariant Borel sets \(A_n\subset X\). By Lemma 2.2, one of \(A_n\cap F\) and \(F\setminus A_n\) is comeagre in \(F\). Intersect these comeagre choices over all \(n\). The resulting set \(H\) is comeagre and nonempty, by the Baire theorem.

All points of \(H\) have the same orbit code, so they lie in a single orbit \(O\). This orbit is nonmeagre in \(F\), hence open there by Lemma 2.1. The dense orbit \(Gx\) meets \(O\), so it equals \(O\). Thus \(Gx\) is open in \(F\). \(\square\)

We next verify the other simple implications.

**\(1\Rightarrow2\).** A locally closed subset of a metric space is \(G_\delta\): closed sets are \(G_\delta\), and an open set is already a countable intersection of open sets. The complete Effros theorem in the preceding lesson therefore makes \(Y\) a \(T_0\) space. Let \((U_n)\) be a countable base of \(X\), and set \(Z_n=GU_n\). These are invariant open sets. The code

\[
c(x)=(1_{Z_n}(x))_{n\geq1}
\tag{2.1}
\]

has precisely the orbits as its fibers. Indeed, the sets \(\pi(U_n)\) form a quotient base and separate points of a \(T_0\) quotient. An invariant Borel subset of \(X\) is a union of these code fibers. The exact written Blackwell theorem, Theorem 5.6 of the prerequisite lesson, therefore puts it in \(\sigma(Z_n)\). Pullback by the surjective \(\pi\) is injective on subsets of \(Y\), so this says precisely \(\mathcal B_q=\sigma(\tau_q)\). The reverse inclusion always holds, since \(\pi\) is continuous.

**\(2\Rightarrow3\).** Every individual orbit is Borel, even before C is used. Its stabilizer \(G_x\) is closed. The written coset-space Proposition 7.4 makes \(G/G_x\) standard Borel, and the canonical map \(G/G_x\to X\) is an injective Borel map. The written injective-image theorem, Theorem 4.3, makes its image \(Gx\) Borel. Consequently every singleton of \(Y\) belongs to \(\mathcal B_q\). A countable quotient base generates \(\sigma(\tau_q)\). If two quotient points had identical memberships in this base, they would have identical memberships in every set of the generated sigma-algebra: the sets containing both or neither form a sigma-algebra. This would contradict their Borel singletons. The base therefore separates points.

**\(3\Rightarrow4\).** Pull back a countable separating family to invariant Borel sets \(A_n\). Ergodicity chooses a conull side of each \(A_n\). Their intersection is conull and nonempty for a nonzero measure, and all its points have the same code. It lies in one orbit. This argument works for every nonzero ergodic measure; sigma-finiteness is unnecessary in this direction.

## 3. Analytic sets and a category argument in a product

For the converse we need to know that the orbit relation has the Baire property. We supply that bridge rather than assuming analytic sets are Borel.

**Lemma 3.1 (Souslin's Baire-property theorem).** Every analytic subset of a Polish space has the Baire property.

*Proof.* First construct a Baire-property envelope of an arbitrary \(E\subset X\). Let \(U\) be the union of all basic open sets whose intersection with \(E\) is meagre. Countability of the base makes \(E\cap U\) meagre. Then

\[
H(E)=(X\setminus U)\cup(E\cap U)
\tag{3.1}
\]

contains \(E\) and has the Baire property. It is minimal modulo meagre sets among such supersets. To see this, let \(B\supset E\) have the Baire property. The difference \(H(E)\setminus B\) lies in \(X\setminus U\). If it were nonmeagre, it would be comeagre in some nonempty open \(W\). Since it is disjoint from \(E\), the set \(E\cap W\) would be meagre. Every basic open subset of \(W\) would then occur in the definition of \(U\), giving \(W\subset U\), a contradiction.

Let \(A\) be nonempty analytic. By the written continuous-parametrization theorem, there is a continuous surjection \(f:\mathbb N^{\mathbb N}\to A\). For a finite sequence \(s\), let \([s]\) denote its cylinder and put \(F_s=\overline{f([s])}\), with \(F_\varnothing=X\). These closed sets decrease along extensions, and

\[
A=\bigcup_{a\in\mathbb N^{\mathbb N}}\ \bigcap_{n\geq1}F_{a|n}.
\tag{3.2}
\]

For the nontrivial inclusion, continuity at \(a\) implies that \(f([a|n])\) eventually lies in every prescribed ball about \(f(a)\), so the intersection of its closures is exactly \(\{f(a)\}\).

For each \(s\), let \(E_s\) be the union of the branch intersections in (3.2) over branches extending \(s\). Then \(E_\varnothing=A\), \(E_s=\bigcup_j E_{sj}\), and \(E_s\subset F_s\). Take the envelopes \(H(E_s)\) and intersect each with \(F_s\) and all its ancestral envelopes. Call the resulting Baire-property superset \(H_s\). It still has the same minimality property, and is contained in \(F_s\). The union \(\bigcup_jH_{sj}\) contains \(E_s\), so \(H_s\setminus\bigcup_jH_{sj}\) is meagre. The union \(L\) of these exceptional sets over the countable tree is meagre. If \(z\in H_\varnothing\setminus L\), repeatedly choose a child \(H_{sj}\) containing \(z\). This produces a branch with \(z\in F_{a|n}\) for every \(n\), hence \(z\in A\). Thus \(A\subset H_\varnothing\) and \(H_\varnothing\setminus A\subset L\). The empty analytic set is immediate. \(\square\)

**Lemma 3.2 (category in a product).** Let \(F\) be Polish. If \(R\subset F\times F\) has the Baire property and every section \(R_x=\{y:(x,y)\in R\}\) is meagre, then \(R\) is meagre.

*Proof.* For a closed nowhere dense \(K\subset F\times F\) and a nonempty basic open \(V\subset F\), the set

\[
D_V=\{x:\{x\}\times V\subset K\}
\tag{3.3}
\]

is closed, as an intersection of closed sections. It has empty interior: otherwise an open rectangle would lie in \(K\). Outside the meagre union of these \(D_V\), the closed section \(K_x\) has empty interior and is nowhere dense. Apply this argument to countably many closed nowhere dense sets covering any given meagre subset \(L\subset F\times F\). For comeagre many \(x\), its section \(L_x\) is meagre.

Now write \(R\mathbin\triangle W\subset L\), where \(W\) is open and \(L\) meagre. If \(W\) is nonempty, it contains a nonempty rectangle \(U\times V\). Choose \(x\in U\) with \(L_x\) meagre. Then \(R_x\) contains \(V\setminus L_x\), which is nonmeagre by the Baire theorem. This is impossible. Thus \(W\) is empty and \(R\subset L\). \(\square\)

**Proposition 3.3.** Under C, if \(Gx\) is not locally closed and \(F=\overline{Gx}\), every orbit in \(F\) is meagre in \(F\), and the orbit relation restricted to \(F\times F\) is meagre.

*Proof.* A nonmeagre orbit in \(F\) would be open by Lemma 2.1; it would meet the dense orbit \(Gx\), making that orbit open in \(F\), contrary to the hypothesis. The relation

\[
E_G|_F=\{(z,gz):z\in F,\ g\in G\}
\tag{3.4}
\]

is the continuous image of the Polish space \(F\times G\), so Lemma 3.1 gives its Baire property. Its sections are the meagre orbits. Lemma 3.2 now applies. Also \(F\) has no isolated point, since an orbit containing an isolated point would be nonmeagre in \(F\). \(\square\)

## 4. A Cantor space inside the orbit relation

Write \(aE_0b\) for eventual equality of binary sequences: they differ at only finitely many coordinates.

**Theorem 4.1.** Suppose a continuous Polish action on a nonempty Polish space \(F\) has a dense orbit and its orbit relation \(E\) is meagre in \(F\times F\). There is a continuous injection \(f:2^{\mathbb N}\to F\) such that

\[
aE_0b\quad\Longleftrightarrow\quad f(a)E f(b).
\tag{4.1}
\]

*Proof.* Choose a complete compatible metric \(d\) on \(F\). Cover \(E\) by closed nowhere dense sets \(R_1,R_2,\ldots\), replacing each by its union with its transpose if desired. Let \(O\) be the dense orbit. We construct nonempty open sets \(V_n\subset F\) and elements \(h_s\in G\), indexed by binary words \(s\) of length \(n\). Start with \(V_0=F\) and \(h_\varnothing=1\). At each positive level require:

- the closed sets \(h_s\overline{V_n}\) are pairwise disjoint and have diameter at most \(2^{-n}\);
- \(h_{si}\overline{V_{n+1}}\subset h_sV_n\);
- if the last bits of distinct words \(s,t\) of length \(n\) differ, then \((h_s\overline{V_n})\times(h_t\overline{V_n})\) misses \(R_j\) for every \(j\leq n\).

Here is the full induction. Suppose level \(n-1\) is fixed. For all words \(s,t\) at that level and all \(j\leq n\), the conditions

\[
(h_su,h_tv)\notin R_j,\qquad(h_sv,h_tu)\notin R_j
\tag{4.2}
\]

define an open dense subset of \(V_{n-1}\times V_{n-1}\), because product translations are homeomorphisms and \(R_j\) is nowhere dense. Intersect these finitely many conditions and also require \(u\ne v\). The latter is open dense: \(F\) has no isolated point, since an isolated point would make \(E\) contain an open singleton rectangle. Since \(O\times O\) is dense, choose \((u,v)\) in this intersection with both points in \(O\). Choose \(\gamma_n\in G\) such that \(\gamma_nu=v\), and set

\[
h_{s0}=h_s,\qquad h_{s1}=h_s\gamma_n.
\tag{4.3}
\]

The finitely many child centers \(h_su,h_sv\) are distinct: different parent centers lie in the disjoint parent regions, and siblings are distinct by \(u\ne v\). Their cross products in (4.2) avoid the required closed sets. By continuity, choose a sufficiently small open neighborhood \(V_n\) of \(u\) whose closure lies in \(V_{n-1}\), whose image \(\gamma_n\overline{V_n}\) lies in \(V_{n-1}\), and whose finitely many translated closures have all three properties above. One can first choose the finitely many required open neighborhoods and then a metric ball with closure inside their inverse images. This completes the induction.

For \(a\in2^{\mathbb N}\), the nested nonempty closed sets \(h_{a|n}\overline{V_n}\) have diameters tending to zero. Completeness gives a unique common point \(f(a)\). Agreement of two prefixes of length \(n\) gives image distance at most \(2^{-n}\); disjoint sibling closures give injectivity.

If \(a\) and \(b\) have the same tail after coordinate \(m\), choose \(v_n\in V_n\), for \(n>m\). Their group words have the form

\[
h_{a|n}=h_{a|m}k_n,\qquad h_{b|n}=h_{b|m}k_n,
\tag{4.4}
\]

with exactly the same suffix \(k_n=\gamma_{m+1}^{a_{m+1}}\cdots\gamma_n^{a_n}\). The points \(h_{a|n}v_n\) and \(h_{b|n}v_n\) converge to their branch limits. Apply the fixed inverse prefix translations: both resulting sequences equal \(k_nv_n\). Therefore \(h_{a|m}^{-1}f(a)=h_{b|m}^{-1}f(b)\), proving that the images are in one orbit.

If \(a,b\) differ infinitely often, fix \(j\) and choose \(n\geq j\) at which their bits differ. The image pair lies in the corresponding child-closure product, which misses \(R_j\). This holds for each \(j\), so the pair lies outside \(E\). Both directions of (4.1) are proved. \(\square\)

The construction is a proof of a familiar Glimm–Effros mechanism. Its role here is precise: infinite disagreement cannot be repaired by any group element, while finite disagreement is repaired by a fixed prefix translation. The intermediate centers all belong to the same dense orbit; their limits need not belong to it.

## 5. An ergodic probability spread across orbits

**Lemma 5.1.** On \(2^{\mathbb N}\) there is a Borel probability \(\eta\) giving every cylinder of length \(n\) mass \(2^{-n}\). Every \(E_0\)-invariant Borel set has mass zero or one, and every \(E_0\)-class has mass zero.

*Proof.* For existence, send \(t\in[0,1)\), with Lebesgue measure, to its binary digits, choosing the terminating expansion at dyadic numbers. Each digit is Borel, and the inverse image of a length-\(n\) cylinder is a half-open interval of length \(2^{-n}\). The pushforward is the required Borel probability. The cylinder masses give independence of finite blocks of digits. They also imply independence of the first \(n\) coordinates and the entire tail after \(n\): establish the assertion for tail cylinders and then close under complements and countable disjoint unions. This is the elementary pi-lambda argument.

If \(A\) is Borel and \(E_0\)-invariant, its membership is unaffected by changing the first \(n\) coordinates. The set of tails obtained by prepending \(n\) zeros is Borel and pulls back exactly to \(A\). Thus \(A\) is measurable in every tail sigma-algebra. It is independent of every finite-coordinate cylinder. The Borel sets \(B\) satisfying \(\eta(A\cap B)=\eta(A)\eta(B)\) form a lambda-system containing the cylinder pi-system, so they include every Borel set. Take \(B=A\) to get \(\eta(A)=\eta(A)^2\).

A singleton is contained in a cylinder of mass \(2^{-n}\) for every \(n\), so has mass zero. An \(E_0\)-class is countable: for each \(n\) there are only \(2^n\) sequences agreeing with its fixed tail after \(n\), and the class is their countable union. Hence it has mass zero.

For completeness, the pi-lambda argument used above is as follows. A lambda-system contains the whole space and is closed under complements and countable disjoint unions; these rules also give differences of nested members. Let \(\mathcal D\) be the smallest lambda-system containing a pi-system \(\mathcal P\) that contains the whole space. For fixed \(P\in\mathcal P\), the members \(B\in\mathcal D\) with \(P\cap B\in\mathcal D\) form a lambda-system containing \(\mathcal P\), so include \(\mathcal D\). Now fix \(B\in\mathcal D\) and repeat the argument with the members \(A\in\mathcal D\) satisfying \(A\cap B\in\mathcal D\). This proves that \(\mathcal D\) is closed under intersections. Complements and intersections give finite unions; expressing a countable union as a disjoint union gives countable unions. Hence \(\mathcal D\) is a sigma-algebra and equals \(\sigma(\mathcal P)\). This proves the assertion about the independence lambda-system, and also uniqueness of finite measures agreeing on a generating pi-system. \(\square\)

**Proposition 5.2.** Under C, condition 4 implies condition 1.

*Proof.* If an orbit is not locally closed, Proposition 3.3 supplies a closed invariant \(F\) with a dense orbit and meagre orbit relation. Apply Theorem 4.1 and push \(\eta\) forward by \(f\), viewing the resulting probability \(\mu=f_*\eta\) on \(X\). For any invariant Borel \(B\subset X\), the set \(f^{-1}(B)\) is \(E_0\)-invariant by (4.1), so Lemma 5.1 gives \(\mu(B)=0\) or \(1\). Thus \(\mu\) is ergodic and sigma-finite.

Each orbit is Borel by the coset and injective-image argument in Section 2. Its inverse image under \(f\), if nonempty, is exactly one \(E_0\)-class, by both directions of (4.1). Every orbit therefore has \(\mu\)-mass zero. This contradicts condition 4. No quasi-invariance of \(\mu\) is asserted or used. \(\square\)

## 6. Choosing one representative by nested closed sets

We now prove \(1\Rightarrow5,6\). In fact a \(T_0\) quotient suffices.

**Lemma 6.1 (the closed-set category test).** If \(A\subset X\) is closed, then

\[
A^\Delta=\{x:\{g:gx\in A\}\text{ is nonmeagre in }G\}
\tag{6.1}
\]

is invariant and Borel.

*Proof.* The group set in (6.1) is closed. Since \(G\) is Baire, a closed subset is nonmeagre exactly when it has nonempty interior. Fix a countable base \((W_i)\) of nonempty open subsets of \(G\) and a countable dense set \(D\subset G\). Closedness therefore gives the explicit formula

\[
A^\Delta=\bigcup_i\ \bigcap_{g\in D\cap W_i}g^{-1}A.
\tag{6.2}
\]

Each intersection is closed, so \(A^\Delta\) is \(F_\sigma\). Replacing \(x\) by \(hx\) right-translates the group set by \(h^{-1}\); homeomorphisms preserve meagreness. Hence the test is invariant. \(\square\)

**Proposition 6.2.** If the quotient is \(T_0\), there is a Borel map \(s:X\to X\) which is constant on each orbit and satisfies \(s(x)\in Gx\).

*Proof.* Use the invariant open code \((Z_n)\) in (2.1), whose fibers are exactly the orbits. Choose a complete metric \(d\) and a countable dense sequence \((p_j)\) in \(X\). For each \(n\), enumerate all closed balls of radius \(2^{-n-2}\) about the \(p_j\); these cover \(X\). Also exhaust each \(Z_n\) by the closed sets

\[
H_{n,k}=\{z:d(z,X\setminus Z_n)\geq1/k\},\qquad k\geq1.
\tag{6.3}
\]

If \(Z_n=X\), use \(H_{n,k}=X\); if \(Z_n=\varnothing\), the positive case never occurs.

Begin with \(A_0(x)=X\). Inductively \(A_{n-1}(x)\) is a closed set chosen from a countable collection by invariant Borel decisions, and \(x\in A_{n-1}(x)^\Delta\). If \(x\in Z_n\), enumerate the intersections

\[
A_{n-1}(x)\cap H_{n,k}\cap\overline B(p_j,2^{-n-2}).
\tag{6.4}
\]

Choose the first whose closed-set category test contains \(x\), in a fixed enumeration of \((k,j)\). Such a choice exists. Indeed the nonmeagre group preimage of \(A_{n-1}(x)\) is covered by the preimages of (6.4), because every group translate of \(x\) lies in \(Z_n\). A countable union of meagre sets would be meagre. If \(x\notin Z_n\), make the same first-choice construction with intersections of \(A_{n-1}(x)\), \(X\setminus Z_n\), and these closed balls. Again the group preimages cover the preceding nonmeagre group set.

Call the chosen closed set \(A_n(x)\) and the chosen center \(p_{j_n(x)}\). Lemma 6.1 makes each first-choice test Borel and invariant. Induction over the countably many possible previous choices makes \(j_n\) Borel and orbit-constant. The sets \(A_n(x)\) are nonempty and nested, their diameters tend to zero, and their intersection is a singleton \(s(x)\). It satisfies every positive and negative code decision: the corresponding closed condition was imposed at step \(n\) and remains imposed at all later steps. Its code equals that of \(x\), so \(s(x)\in Gx\).

Finally \(d(p_{j_n(x)},s(x))\leq2^{-n-2}\), so \(s\) is a pointwise limit of Borel maps with countable range. Explicitly, for any nonempty closed \(K\subset X\), the real Borel functions \(d(p_{j_n(x)},K)\) converge to \(d(s(x),K)\); the zero set is \(s^{-1}(K)\). The empty set has empty preimage. Thus \(s\) is Borel. Orbit-constancy follows from the invariant decisions at every step. \(\square\)

Set \(T=\{x:s(x)=x\}\). This is Borel, since the diagonal of \(X\times X\) is closed and \(x\mapsto(x,s(x))\) is Borel. Each orbit meets \(T\) in its unique selected point, so \(1\Rightarrow6\). Being a Borel subset of a Polish space, \(T\) is standard Borel. The bijection \(\pi|_T:T\to Y\) is a Borel isomorphism: it is measurable by (1.1), and a Borel set \(B\subset T\) corresponds to a quotient set whose inverse image is \(s^{-1}(B)\), which is Borel. Thus \(1\Rightarrow5\).

**\(5\Rightarrow3\).** A standard Borel space has a countable separating family, transported from a countable base of a Polish realization.

**\(6\Rightarrow3\).** Let \(T\) be a Borel transversal and \(B\subset T\) Borel. Both \(GB\) and \(G(T\setminus B)\) are analytic: they are continuous images under the action of Borel subsets of \(G\times X\), as in the written prerequisite Theorem 4.3(1). They partition \(X\), because every orbit meets \(T\) exactly once. The written separation theorem, Theorem 2.4, therefore makes \(GB\) Borel. Take the saturations of a countable relative base of \(T\); they are invariant Borel sets separating orbits. These descend to the required family in \(\mathcal B_q\). This closes every implication of Theorem 1.1. \(\square\)

## 7. Two contrasting models

**Scaling.** The group \(\mathbb R_{>0}\) acts on \(\mathbb R\) by multiplication. Its three orbits are \(P=(0,\infty)\), \(N=(-\infty,0)\), and \(Z=\{0\}\). They are locally closed. The quotient is \(T_0\), but not Hausdorff, since every neighborhood of \(Z\) in the quotient is the whole quotient. It is nevertheless a three-point standard Borel space. A Borel selector is

\[
s(x)=
\begin{cases}
1,&x>0,\\
-1,&x<0,\\
0,&x=0.
\end{cases}
\tag{7.1}
\]

Theorem 1.1 makes every nonzero ergodic Borel measure concentrate on one of these three orbits. The measure can fail to be quasi-invariant, as \(\delta_1\) does.

**Rational translations.** Give \(\mathbb Q\) the discrete topology and let it translate \(\mathbb R\). This is a continuous Polish action, satisfying C and D because \(\{0\}\) is an identity neighborhood; for D, \(\bigcap_n\overline{Q_n}=\{x\}\). Each orbit is countable, dense and meagre, so no orbit is locally closed. Theorem 1.1 therefore denies countable Borel separation and a Borel transversal. Lebesgue measure is an explicit ergodic sigma-finite witness.

Here is its full ergodicity check, using only finite-measure uniqueness. Let \(A\) be a Borel set invariant under rational translations, and set \(c=\lambda(A\cap[0,1))\). Translation invariance gives equal \(A\)-measure to all \(2^n\) dyadic cells partitioning \([0,1)\); each has mass \(c2^{-n}\). Integer translations give the same assertion in every unit interval. The finite measures \(\lambda|_A\) and \(c\lambda\) therefore agree on the dyadic interval pi-system in each unit interval, and hence on all its Borel sets, by the pi-lambda proof in Lemma 5.1. Apply that equality to \(A\) itself in \([0,1)\): it gives \(c=c^2\). Thus \(c\) is zero or one, and the equality of measures in every unit interval makes \(A\) null or conull in \(\mathbb R\). Its countable orbits all have measure zero. Alternatively, Sections 3–5 construct an ergodic probability with the same zero-orbit-mass property.

## 8. Graded exercises with complete solutions

**Exercise 8.1.** *Level 1.* Prove D implies C without assuming the point neighborhoods are nested.

*Solution.* Fix \(N\) and its witness \(M\) in D. For any \(x\), every base member contains \(x\), so \(Mx\subset M Q_n\). Taking closures and then intersecting gives \(\overline{Mx}\subset\bigcap_n\overline{M Q_n}\subset Nx\). The same \(M\) works for every point. No nesting was used.

**Exercise 8.2.** *Level 2.* In Proposition 2.3, why can the comeagre code fiber not be an orbit different from the original dense orbit?

*Solution.* C and Lemma 2.1 make the comeagre fiber's orbit open in \(F\). Every nonempty relatively open set meets the original dense orbit. Orbits that meet are equal, so this open orbit is the original orbit. Merely knowing that the fiber is nonmeagre, without the closure condition, would not yield this conclusion.

**Exercise 8.3.** *Level 2.* Derive formula (6.2), including the direction that uses density.

*Solution.* If the closed group preimage of \(A\) has interior, it contains a nonempty basic open \(W_i\), so \(gx\in A\) for every \(g\in D\cap W_i\). Conversely, this condition puts the dense subset \(D\cap W_i\) into the closed group preimage, and hence puts all of \(W_i\) into it. Such a nonempty open subset of a Polish group is nonmeagre. Right translation gives invariance, and the countable union of closed intersections gives Borelness.

**Exercise 8.4.** *Level 3.* In the Cantor construction, repair a finite change in the first \(m\) binary coordinates by an explicit group element. Explain why no convergence of the varying suffix group elements is needed.

*Solution.* Formula (4.4) and continuity of the two fixed inverse translations give \(h_{a|m}^{-1}f(a)=h_{b|m}^{-1}f(b)\). Hence \(f(b)=h_{b|m}h_{a|m}^{-1}f(a)\). The common points \(k_nv_n\) converge after applying those fixed translations. The group elements \(k_n\) themselves need not converge; the proof asserts no such limit.

**Exercise 8.5.** *Level 3.* Show that the probability in Proposition 5.2 has no atoms and gives every orbit mass zero, even when the original acting group is uncountable.

*Solution.* Since \(f\) is injective, the inverse image of a singleton has at most one point and hence zero Bernoulli mass. For an orbit meeting \(f(2^{\mathbb N})\), choose one preimage \(a\). The exact equivalence (4.1) makes its entire preimage \([a]_{E_0}\), a countable set of measure zero. An orbit missing the image has empty preimage. This argument controls orbit preimages and requires no countability of the acting group.

**Exercise 8.6.** *Level 2.* Why do nested small closed balls alone fail to prove that the selected limit lies in the required orbit? Identify the extra constraint in Proposition 6.2.

*Solution.* A nonclosed orbit can approach a point of a different orbit, so a limit of points in the first orbit can lie only in its closure. At step \(n\), Proposition 6.2 also imposes a closed inner part of \(Z_n\) when its code bit is one, and \(X\setminus Z_n\) when its bit is zero. These closed constraints survive the limit. Every code bit is imposed at a finite stage, so the final point has exactly the orbit code of the initial point.

**Exercise 8.7.** *Level 2.* Compute the quotient sigma-algebra and a transversal for the scaling model. Give an ergodic Borel measure of infinite total mass.

*Solution.* Each of \(P,N,Z\) is Borel, so every subset of the three-point quotient is quotient Borel. The transversal is \(\{-1,0,1\}\). The measure \(dx/x\) on \(P\), extended by zero to the other orbits, is sigma-finite and infinite. Any invariant Borel subset of \(P\) is empty or all of \(P\), since the scaling action is transitive there. Thus this measure is ergodic and concentrated on \(P\), as the theorem requires.

**Exercise 8.8.** *Level 3.* Let \(S_\infty\) act by permuting values on the Polish space \(I\) of injective sequences in \(\mathbb N^{\mathbb N}\). Prove that its quotient is countably separated but is not \(T_0\), and deduce that C fails. This tests the necessity of C in \(3\Rightarrow1\).

*Solution.* The space \(I\) is closed in \(\mathbb N^{\mathbb N}\), since every coordinate-inequality condition is clopen. The permutation group is Polish in its usual topology, and the value action is continuous. Two injective sequences are in one orbit exactly when their omitted ranges have the same cardinality in \(\mathbb N\cup\{\infty\}\): the coordinatewise bijection of their ranges extends to a permutation precisely when the complements have equal cardinality. The condition of omitting at least \(k\) values is Borel: take the countable union, over distinct \(m_1,\ldots,m_k\), of the closed conditions that no coordinate equals any \(m_j\). Exact finite defect and infinite defect are therefore Borel, giving a countable separating family.

Every defect orbit is dense in \(I\), since any finite injective prefix extends to an infinite injective sequence with any prescribed complement cardinality. Every nonempty invariant open set consequently meets every orbit and then contains every orbit. The quotient is indiscrete with more than one point, so fails \(T_0\).

One can also see the failure of C directly. Choose \(x\) whose range is \(\mathbb N\setminus\{0\}\), and let \(N\) be the subgroup fixing \(0\). Given any identity neighborhood \(M\), choose a finite set \(K\) containing \(0\) whose pointwise fixer lies in \(M\), and choose \(b\notin K\). There is an injective \(y\) with range \(\mathbb N\setminus\{0,b\}\) which agrees with \(x\) at the coordinates whose values lie in \(K\). Every finite prefix of \(y\) is obtained from the corresponding prefix of \(x\) by a finite partial permutation compatible with fixing \(K\); extend it to a permutation fixing \(K\). Thus \(y\in\overline{Mx}\). But \(Nx\) consists of sequences with complement exactly \(\{0\}\), so \(y\notin Nx\). No \(M\) witnesses C for this \(N\).

## References and provenance

Masamichi Takesaki, *Theory of Operator Algebras III* (2003), Exercise XIII.2(2) supplied PDF page 51, specifies C, D and the Glimm equivalences. Its bibliography entry [508] identifies Edward G. Effros, *Transformation Groups and C\*-Algebras*, *Annals of Mathematics* 81 (1965), 38–55, [publisher record](https://doi.org/10.2307/1970381). The full arguments here are newly written course exposition of known mathematics; a complete comparison of wording and distinctive arrangement against all cited sources remains in progress.

David Marker, [*Descriptive Set Theory*](https://www.math.uic.edu/~marker/math512/dst.pdf), Lemma 4.21, Theorem 4.22 and Corollary 4.23 provides the Baire-envelope and Souslin-operation treatment used to check Lemma 3.1. That public draft is a reference source; no copying or translation permission is inferred from access. Lemmas 3.1–3.2 give the required complete course arguments.

John P. Burgess, [*A Selection Theorem for Group Actions*](https://msp.org/pjm/1979/80-2/pjm-v80-n2-p05-s.pdf), *Pacific Journal of Mathematics* 80 (1979), 333–336, proves the broader selector theorem discussed after Theorem 1.1. The complete four-stage proof was checked; it uses Borel-rank refinement and general Vaught transforms. Section 6 instead treats the invariant-open code available here and proves only the needed closed-set category test, so no general Vaught-transform theorem or Burgess proof is left as an external prerequisite. The Cantor argument is credited to the classical Glimm–Effros construction; its entire induction is supplied in Section 4.

The exact programme prerequisites named at the beginning are actual written proofs, used at their stated scope. AI writing and mathematical self-checking do not constitute independent human review or formal verification. This lesson and its eight solved exercises have original expression dedicated under CC0 1.0; cited sources retain their own rights. The course's remaining general measured-groupoid and source-validation obligations are separate from this completed orbit-space criterion.
