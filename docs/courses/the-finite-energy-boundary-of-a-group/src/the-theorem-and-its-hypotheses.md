# The theorem and its hypotheses

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The lessons of this course start from a finitely presented group \(\Gamma\) that has a finite-energy function whose gradient is not a limit of gradients of finitely supported functions. From such a function they build a compact boundary \(B\) of \(\Gamma\), study the action of \(\Gamma\) on it, and arrive at a contradiction when three further conditions on the group hold. This lesson states the result as one theorem about the group (Theorem 1.1) and goes through its proof step by step, naming the lesson that supplies each step (Section 2). It then describes how the theorem is used in OpenAI's proof of the Singer conjecture in dimension four outside the middle degree, and which statements of that proof are not proved in this programme (Section 3). Section 4 is about the role of the dimension.

No new argument is given in this lesson. Its purpose is to make visible what has been proved and under which hypotheses.

## 1. The statement

We recall the notions that occur in the statement.

- A *triangular presentation* \(\langle S\mid R\rangle\) has a finite set \(S\) of generators and finitely many relators, each of length at most three. Every finitely presented group has one. Its *Cayley graph* \(G\) has the vertex set \(\Gamma\) and joins \(g\) to \(gs\) for every generator \(s\). It is *one-ended* if for every finite set \(A\) of vertices, \(G\setminus A\) has exactly one infinite component. ([Finite-energy functions on a Cayley complex](finite-energy-functions-on-a-cayley-complex.md), [The compact space and its boundary](the-compact-space-and-its-boundary.md).)
- \(\mathcal D\) is the Hilbert space of the gradients \(dF\) of the real functions \(F\) on \(\Gamma\) of finite energy, and \(\mathcal D_0\) is the closure in it of the gradients of the functions with finite support.
- Assumption \((\mathrm C_k)\), for an abelian group \(k\): for every \(1\)-cochain \(\alpha\) on the Cayley complex with values in \(k\) whose coboundary is nonzero on finitely many cells only, there is a \(1\)-cochain \(\eta\), nonzero on finitely many edges only, with \(d\eta=d\alpha\). ([Dimension and cohomology of the boundary](dimension-and-cohomology-of-the-boundary.md).)
- If \(\mathcal D_0\ne\mathcal D\) and \(G\) is one-ended, a function \(f\) as in Theorem 4.1 of the first lesson gives a compact metric space \(X=\Gamma\cup B\) with an action of \(\Gamma\); the *boundary* \(B\) is compact and connected and has more than one point.
- A *cut point* of \(B\) is a point whose complement in \(B\) is not connected. If the set \(P\) of cut points is not empty, the *dendrite quotient* \(D_P(B)\) is the quotient of \(B\) constructed in [The dendrite quotient of a continuum](course:pretrees/the-dendrite-quotient-of-a-continuum); the group \(\Gamma\) acts on it.

**Theorem 1.1.** Let \(\Gamma=\langle S\mid R\rangle\) be a triangular presentation. Assume:

- (H1) the Cayley graph \(G\) is one-ended;
- (H2) \(\Gamma\) has no element of finite order other than the identity;
- (H3) assumption \((\mathrm C_k)\) holds for the group \(k\) with two elements;
- (H4) if \(\mathcal D_0\ne\mathcal D\), and \(B\) is the boundary given by a function \(f\) as above, and \(B\) has a cut point, then \(\Gamma\) fixes a point of the dendrite quotient \(D_P(B)\).

Then \(\mathcal D_0=\mathcal D\): the gradient of every function of finite energy on \(\Gamma\) is a limit, in the space of square summable functions on the edges, of gradients of functions with finite support.

Hypothesis (H4) speaks about a space that exists only when the conclusion fails. It is a condition on all actions of a certain kind that \(\Gamma\) could have. In the application of Section 3 it follows from a general theorem on groups acting on dendrites.

## 2. The proof, step by step

Suppose \(\mathcal D_0\ne\mathcal D\).

*Step 1: the boundary.* By (H1) the standing assumptions of the lesson on the compact space and its boundary hold. Fix a function \(f\) as in Theorem 4.1 of the lesson on finite-energy functions. That lesson constructs the compact metric space \(X=\Gamma\cup B\), in which the points of \(\Gamma\) are isolated and dense, with an action of \(\Gamma\) by homeomorphisms; \(B\) is compact and connected and has more than one point (Theorem 5.1 there), and vertices near a point of \(B\) are joined by paths of \(G\) near that point (Theorem 6.2 there).

*Step 2: the action.* \(\Gamma\) acts on \(B\) as a convergence group (Corollary 3.2 of [The convergence action](the-convergence-action.md)), and by (H2) every orbit in \(B\) is dense (Theorem 5.2 there).

*Step 3: dimension and cohomology.* \(\dim B\le1\) (Theorem 2.3 of the lesson on dimension and cohomology), and \(\check H^1(B;k)=0\) by (H3) (Theorem 3.2 there).

*Step 4: a continuum without cut points.* Either \(B\) has no cut point (Case A of [A continuum without cut points and its graph](a-continuum-without-cut-points-and-its-graph.md)), or it has one (Case B). Case A needs (H2). Case B needs in addition the two hypotheses (b) and (z) of [The tree of cut points](course:convergence-groups/the-tree-of-cut-points):

- (b), the fixed-point property for trees with finite edge stabilizers, holds because \(S\) is a finite generating set with a one-ended Cayley graph (Theorem 5.1 of [The fixed-point property for groups with one end](course:convergence-groups/the-fixed-point-property-for-groups-with-one-end));
- (z), that \(\Gamma\) fixes a point of \(D_P(B)\), is (H4).

The two other hypotheses of the theorem on the tree of cut points hold as well: \(\Gamma\) is finitely generated, and by (H2) every element other than the identity has infinite order. In Case B that theorem gives a tree whose vertices include the cut points, and [A block of the boundary](a-block-of-the-boundary.md) cuts out of \(B\) a compact connected set \(L\) with more than one point and without cut points.

In both cases Theorem 2.1 of the lesson on a continuum without cut points gives a group \(H\), a continuum \(L\) without cut points with \(\dim L\le1\) and \(\check H^1(L;k)=0\), and a graph \(K\), with the properties (S1) to (S7) of [Component labels and annular depth](component-labels-and-annular-depth.md).

*Step 5: local connectedness.* By Theorem 7.1 of [The continuum is locally connected](the-continuum-is-locally-connected.md), \(L\) is locally connected. This uses the two lessons before it.

*Step 6: the contradiction.* A locally connected continuum with more than one point, of dimension at most one and with vanishing first Čech cohomology, has a cut point (Corollary 3.2 of [Dendrites and cut points](course:continua-arcs-and-cut-points/dendrites-and-cut-points)). But \(L\) has none. In the form of Corollary 7.3 of the lesson on local connectedness: \(\check H^1(B;k)\ne0\), against Step 3. \(\blacksquare\)

The hypotheses enter as follows.

- \(\mathcal D_0\ne\mathcal D\), the assumption to be refuted: the function \(f\) with connected level sides, from which the space \(X\) is built.
- (H1): the construction of \(X\), the connectedness of \(B\), the paths near boundary points; and hypothesis (b) on trees.
- (H2): the density of the orbits; elements of infinite order in the stabilizers of cut points; the description of the block.
- (H3): the vanishing of \(\check H^1(B;k)\), which is used twice, for the component labels at a deleted vertex and for the final contradiction.
- (H4): the tree of cut points, in Case B only.

## 3. The use in the proof of the Singer conjecture in dimension four

For a finite connected complex \(Q\) with fundamental group \(\Gamma\) there are numbers \(b_p^{(2)}(\widetilde Q)\ge0\), the \(L^2\)-Betti numbers of the universal cover, defined with the von Neumann algebra of \(\Gamma\). The theorem of [OpenAI-S] is:

> Let \(Q\) be a finite connected aspherical Poincaré complex of formal dimension four. Then \(b_p^{(2)}(\widetilde Q)=0\) for all \(p\ne2\). In particular this holds for every closed connected aspherical topological manifold of dimension four.

Its proof assumes \(b_1^{(2)}(\widetilde Q)>0\) and derives a contradiction; the other degrees then follow by duality. Theorem 1.1 is the part of the proof that takes place on the group. The following statements connect it with the complex \(Q\). They are proved or quoted in [OpenAI-S], in its Sections 2, 5 and 6. They are *not* proved in this programme, and neither \(L^2\)-Betti numbers nor Poincaré complexes are defined in it.

- (R1) \(\Gamma\) is infinite and finitely presented, and has no element of finite order other than the identity. This gives (H2), and a triangular presentation.
- (R2) Poincaré duality with coefficients in modules over the group ring gives, for the group \(k\) with two elements, \(H^i(\Gamma;k\Gamma)=0\) for \(i=1,2\), and \(H^1(\Gamma;k[\Gamma/J])=0\) for every subgroup \(J\) that is trivial or infinite cyclic.
- (R3) Cochains of finite support on the Cayley complex are cochains with values in the group ring. With this, \(H^1(\Gamma;k\Gamma)=0\) gives (H1), and \(H^2(\Gamma;k\Gamma)=0\) gives (H3).
- (R4) By (R2), \(\Gamma\) is not a nontrivial amalgamated product and not an HNN extension over a subgroup that is finite or infinite cyclic. A theorem on convergence groups acting on dendrites ([Bowditch 2], Lemma 1.4) then says that the dendrite quotient \(D_P(B)\) is a single point. This gives (H4). The proof of that theorem uses the theory of group actions on real trees.
- (R5) If \(b_1^{(2)}(\widetilde Q)>0\), then \(\mathcal D_0\ne\mathcal D\) for the Cayley complex of a triangular presentation of \(\Gamma\).
- (R6) \(b_0^{(2)}=b_4^{(2)}=0\), \(b_3^{(2)}=b_1^{(2)}\), and \(b_p^{(2)}=0\) for \(p>4\).

Given (R1) to (R5), Theorem 1.1 contradicts \(b_1^{(2)}(\widetilde Q)>0\); with (R6) the theorem follows.

So the state in this programme is: Theorem 1.1 has a complete proof in the lessons named in Section 2 and the lessons they use, from the core courses [Point-Set Topology (C90)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C90), [Measure and Integration (D10)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) and [Functional Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D20). The reductions (R1) to (R6) and the theorem on dendrites in (R4) are taken from the literature. The theorem on dendrites is the deepest of them.

Two remarks on the comparison with [OpenAI-S]. There the fixed-point property for trees, hypothesis (b) above, is obtained from (R2); here it is obtained from (H1) alone. And there the conclusion of (R4) is that \(D_P(B)\) is a point, while Theorem 1.1 needs only that \(\Gamma\) fixes a point of it.

## 4. The role of the dimension

Theorem 1.1 is a statement about a group; no dimension occurs in it. In the proof of [OpenAI-S] the dimension four enters only through the reductions (R2) and (R6).

For a finite connected aspherical Poincaré complex of formal dimension \(n\), duality reads \(H^i(\Gamma;V)\cong H_{n-i}(\Gamma;V)\) for modules \(V\) over \(k\Gamma\). The homology of \(\Gamma\) with coefficients in \(k[\Gamma/J]\) is the homology of \(J\) with coefficients in \(k\). So
\[
\begin{gathered}
H^i(\Gamma;k\Gamma)\cong H_{n-i}(\{1\};k),\\
H^1(\Gamma;k[\Gamma/J])\cong H_{n-1}(J;k).
\end{gathered}
\]
The first group is zero when \(n-i\ge1\), which for \(i=1,2\) means \(n\ge3\). The second is zero for \(J\) trivial or infinite cyclic when \(n-1\ge2\), again \(n\ge3\). So the two vanishing statements of (R2), the place where the proof uses the number four, hold in every formal dimension at least three. If the other reductions are carried over to formal dimension \(n\ge3\), the argument gives \(b_1^{(2)}(\widetilde Q)=0\) for every finite connected aspherical Poincaré complex of formal dimension at least three. This consequence of the proof was pointed out by the Reddit user u/Apprehensive_Sand951 [Sand].

It is not stated in [OpenAI-S], and it is not proved in this programme: like the theorem in dimension four it depends on the reductions of Section 3, and these have not been examined here in other dimensions beyond the count above. For \(n=2\) the count fails, as it must: \(H^2(\Gamma;k\Gamma)\cong H_0(\{1\};k)=k\) is not zero.

The Singer conjecture is also studied for special families of groups. Avramidi, Okun and Schreve consider right-angled Coxeter groups \(W_L\) of flag complexes \(L\) and their \(L^2\)-Betti numbers over the field with two elements. Contracting an edge \(e\) of \(L\) gives a branched double cover of the associated cube complexes, and with it an inequality between these numbers for \(W_L\) and \(W_{L/e}\) [AOS, Theorem 1.1]. This gives a new proof of the Singer conjecture for the groups \(W_L\) of flag triangulations \(L\) of the 2-sphere, whose cube complexes are closed aspherical manifolds of dimension three, and reduces the version over the field with two elements for right-angled Coxeter groups to minimal flag triangulations of even-dimensional spheres [AOS, Section 1].

## 5. Exercises

**5.1.** Let \(\Gamma=\langle s,t\mid\ \rangle\) be the free group on two generators. By Exercise 5.3 of the lesson on finite-energy functions, \(\mathcal D_0\ne\mathcal D\). Which hypothesis of Theorem 1.1 fails?

**5.2.** Let \(\Gamma=\mathbb Z^2\) with the triangular presentation \(\langle s,t,y\mid y^{-1}st,\ y^{-1}ts\rangle\). Which of (H2) and (H3) hold?

**5.3.** In Step 4, the theorem on the tree of cut points is applied. It has four hypotheses (a), (b), (c), (z). Say for each from which of (H1) to (H4) it follows.

**5.4.** Let \(\Gamma\) satisfy (H1), (H2) and (H3), and suppose \(\mathcal D_0\ne\mathcal D\). Show that the boundary \(B\) has cut points.

## 6. Solutions

**5.1.** (H1). The Cayley graph is the tree in which every vertex has four neighbours; removing one vertex leaves four infinite components (Exercise 6.4 of the lesson on the fixed-point property for groups with one end).

**5.2.** (H2) holds: an element \(s^at^b\) with \((a,b)\ne(0,0)\) has infinite order. (H3) fails, by Exercise 4.4 of the lesson on dimension and cohomology.

**5.3.** (a), finitely generated: \(S\) is finite. (b): from (H1), by the theorem on groups with one end. (c), every infinite subgroup contains an element of infinite order: from (H2), since every element other than the identity has infinite order. (z): this is (H4).

**5.4.** If \(B\) had no cut point, Case A of the lesson on a continuum without cut points would apply, which needs (H2) only, and Corollary 7.3 of the lesson on local connectedness would give \(\check H^1(B;k)\ne0\), against (H3) and Theorem 3.2 of the lesson on dimension and cohomology. So \(B\) has cut points. Hypothesis (H4) is not needed for this; it is needed to exclude the case with cut points.

## References

- [OpenAI-S] OpenAI, *The Singer conjecture in dimension four*, OpenAI Math Release preprint, 25 September 2026, Sections 1, 2 and 10. https://github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026
- [Bowditch 2] B. H. Bowditch, *Connectedness properties of limit sets*, Transactions of the American Mathematical Society 351 (1999). Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-connected.pdf
- [Sand] u/Apprehensive_Sand951, comment in the thread *AI in mathematics, October 10, 2026*, r/math, Reddit, October 2026. https://www.reddit.com/r/math/comments/1x2iy00/comment/pf4k77i/
- [AOS] G. Avramidi, B. Okun and K. Schreve, *Reflections on branched covers*, arXiv:2610.02723 (October 2026). https://arxiv.org/abs/2610.02723
