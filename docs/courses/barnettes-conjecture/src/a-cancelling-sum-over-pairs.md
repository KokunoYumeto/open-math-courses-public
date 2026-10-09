# A cancelling sum over pairs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a pair \((r,s)\) of states, let \(Q_s\) consist of the edge opposite \(s(t)\) in every black face \(t\). [Two induced trees and a Hamiltonian cycle](two-induced-trees-and-a-hamiltonian-cycle.md) turns a pair for which \(Q_s\) is a forest into the two induced trees that give a Hamiltonian cycle. This lesson proves that such a pair exists whenever any pair exists (Proposition 4.2). The argument evaluates one finite exponential sum over all pairs in two ways. Fixing \(s\), the pairs with a cycle in \(Q_s\) cancel in sign-reversed couples (Lemma 2.2). Grouping the pairs instead by the edges joining \(r(t)\) to \(s(t)\), the sum has a nonzero Taylor coefficient (Proposition 4.2). Both computations rest on a *disk identity*: a directed cycle of chosen edges encloses a fixed signed number of black and white triangles (Lemma 1.1). The regrouping by union cycles resembles the double-dimer expansion of Kenyon [Ken], and the passage between face–vertex matchings and plane trees is related to Temperley's correspondence as extended by Kenyon, Propp and Wilson [KPW]; neither is used as an input.

The setting is that of [Pairs of states](pairs-of-states.md): \(T\) is a sphere triangulation with a face colouring, \(t_0\) a black face whose vertices are the roots, \(\mathcal T\) the other black faces and \(X\) the non-root vertices. Separating triangles are allowed in Sections 1 to 3. The face on the left of a dart \(d\) is \(\operatorname{face}(d)\), and \(\delta(d)=\pm1\) according as this face is black or white (Section 3 of [Triangulations from cubic bipartite graphs](triangulations-from-cubic-bipartite-graphs.md)). For a cycle \(\Gamma\) of \(T\), the side not containing \(t_0\) is its *inner side*, and \(\Gamma\) is traversed *counterclockwise* when its inner side lies on the left of its darts (Lemma 3.3 of [Sphere maps](sphere-maps.md)).

## 1. The disk identity

**Lemma 1.1** (Disk identity). Let \(r\) be a state, and choose in every \(t\in\mathcal T\) a dart of an edge of \(t\) leaving \(r(t)\). Every cycle of \(T\) traversed along chosen darts avoids the roots, and the sum of \(\delta\) over its darts is \(-3\) if it is traversed counterclockwise and \(3\) if clockwise.

*Proof.* A non-root vertex \(v\) is left by exactly one chosen dart, the one chosen in \(r^{-1}(v)\), and the roots are left by none. So a cycle \(\Gamma\) traversed along chosen darts contains no root, and its dart leaving a vertex \(v\) is the dart chosen in \(t_v=r^{-1}(v)\); this edge lies in \(t_v\), so \(t_v\) is the black face of that edge.

Let \(h\) be the length of \(\Gamma\), \(\mathcal A\) its inner side, \(I\) the number of vertices strictly inside \(\mathcal A\), \(B\) and \(W\) the numbers of black and white faces in \(\mathcal A\), and \(l\) the number of edges of \(\Gamma\) whose black face lies in \(\mathcal A\). We show \(B=I+l\). The black faces in \(\mathcal A\) belong to \(\mathcal T\), because \(t_0\) is on the other side. The vertices of a face in \(\mathcal A\) lie on \(\Gamma\) or strictly inside \(\mathcal A\) (Lemma 3.4(a) of [Sphere maps](sphere-maps.md)), so \(r\) maps the black faces of \(\mathcal A\) injectively into this set of vertices. Every vertex \(v\) strictly inside \(\mathcal A\) is a non-root, since the roots are not on \(\Gamma\) and the face \(t_0\) at each of them lies outside \(\mathcal A\), and \(r^{-1}(v)\) is a black face at \(v\), hence in \(\mathcal A\). A vertex \(v\) of \(\Gamma\) is in the image exactly when \(t_v\in\mathcal A\), that is, when the edge of \(\Gamma\) leaving \(v\) has its black face in \(\mathcal A\); every edge of \(\Gamma\) leaves exactly one of its vertices, so there are \(l\) such vertices. Hence \(B=I+l\).

By Corollary 3.1 of [Triangulations from cubic bipartite graphs](triangulations-from-cubic-bipartite-graphs.md), \(B+W=2I+h-2\), so \(W=I+h-2-l\) and \(B-W=2l-h+2\). By Lemma 3.2 there, applied with \(\Gamma\) traversed counterclockwise, \(3(B-W)=2l-h\), the sum of \(\delta\) over the counterclockwise darts. Therefore \(3(2l-h+2)=2l-h\), that is, \(2l-h=-3\). The clockwise darts are the reverses, on which \(\delta\) changes sign. \(\square\)

**Corollary 1.2.** For a pair \((r,s)\), direct the edge joining \(r(t)\) and \(s(t)\) in each \(t\in\mathcal T\) from \(r(t)\) to \(s(t)\). These darts belong to distinct edges and form vertex-disjoint directed cycles covering \(X\), each of length at least \(3\), and
\[
J(r,s)=\frac13\sum_{t\in\mathcal T}\delta\bigl(r(t),s(t)\bigr)
\]
is an integer: each counterclockwise cycle contributes \(-1\) and each clockwise cycle \(+1\).

*Proof.* Each edge of \(T\) lies in exactly one black face, so the darts belong to distinct edges. Every vertex of \(X\) is left by one of them (in \(r^{-1}(v)\)) and entered by one (in \(s^{-1}(v)\)), and the roots by none, so they form disjoint directed cycles covering \(X\). A cycle of length \(2\) would need two parallel edges. Lemma 1.1 applies with these chosen darts. \(\square\)

## 2. The sum and its cancellation

For a state \(s\), let \(Q_s\) be the spanning subgraph of \(T\) whose edges are, for each \(t\in\mathcal T\), the edge of \(t\) opposite \(s(t)\), that is, the edge joining the two other vertices of \(t\). These \(|\mathcal T|\) edges are distinct, since each edge lies in one black face.

Assign a real number \(a(t,v)\) to every \(t\in\mathcal T\) and every vertex \(v\) of \(t\), to be chosen in Section 3, and let \(\omega(s)=\sum_{t\in\mathcal T}a(t,s(t))\). With \(\mathrm i^2=-1\), put
\[
Z(x)=\sum_{(r,s)\text{ a pair}}\mathrm i^{J(r,s)}\exp\bigl(x\,\omega(s)\bigr)\qquad(x\in\mathbb R).
\]

**Lemma 2.1.** For a black face \(t\) with three distinct vertices \(p,q,u\),
\[
\delta(u,q)-\delta(p,q)=2\,\delta(p,u).
\]

*Proof.* The three darts of the face \(t\) have \(t\) on their left, so \(\delta=+1\) on them and \(-1\) on their reverses. If the face visits \(p,q,u\) in this cyclic order, then \(\delta(p,q)=1\), \(\delta(u,q)=-1\) and \(\delta(p,u)=-1\); if it visits \(p,u,q\), then \(\delta(p,q)=-1\), \(\delta(u,q)=1\) and \(\delta(p,u)=1\). \(\square\)

**Lemma 2.2** (Cancellation). If \(Q_s\) contains a cycle, then \(\sum_r\mathrm i^{J(r,s)}=0\), the sum running over the states \(r\) for which \((r,s)\) is a pair.

*Proof.* Choose a cycle \(\Gamma_0\) of \(Q_s\); the choice depends on \(s\) alone. For a partner \(r\) of \(s\), let \(u(t)\) be the third vertex of \(t\), so that the edge of \(t\) in \(Q_s\) joins \(r(t)\) and \(u(t)\), and direct it from \(r(t)\) to \(u(t)\). Each vertex is left by at most one of these darts, so the \(h\) edges of \(\Gamma_0\) have distinct tails among its \(h\) vertices, and \(\Gamma_0\) is a directed cycle. Define \(\tilde r(t)=u(t)\) if the edge of \(t\) in \(Q_s\) lies in \(\Gamma_0\), and \(\tilde r(t)=r(t)\) otherwise. Along \(\Gamma_0\) the tails and the heads are the same set of vertices, so \(\tilde r\) is a bijection onto \(X\); it is a state, and a partner of \(s\) because \(u(t)\ne s(t)\). For \(\tilde r\), the same construction directs \(\Gamma_0\) the other way and returns \(r\). So \(r\mapsto\tilde r\) is an involution without fixed points on the partners of \(s\).

By Lemma 2.1, the faces changed contribute
\[
3\bigl(J(\tilde r,s)-J(r,s)\bigr)=\sum_t\bigl(\delta(u(t),s(t))-\delta(r(t),s(t))\bigr)=2\sum_t\delta\bigl(r(t),u(t)\bigr),
\]
the sums running over the faces whose edge lies in \(\Gamma_0\). The last sum is the \(\delta\)-sum of the directed cycle \(\Gamma_0\), which is \(\pm3\) by Lemma 1.1 (choose in every \(t\in\mathcal T\) the dart from \(r(t)\) to \(u(t)\)). Hence \(J(\tilde r,s)=J(r,s)\pm2\) and \(\mathrm i^{J(\tilde r,s)}=-\mathrm i^{J(r,s)}\). The terms cancel in couples. \(\square\)

## 3. Positive weights on spokes

**Lemma 3.1** (Face potentials). Let \(K\) be a sphere map with at least one edge and \(f_\infty\) one of its faces. There is a function \(a\) on the darts of \(K\) with \(a(\theta d)=-a(d)\) whose sum over the darts of every face other than \(f_\infty\) equals \(1\). For every cycle \(\Gamma\) of \(K\), traversed so that \(f_\infty\) is not on the left of its darts, \(\sum_{d\in\Gamma}a(d)\) is the number of faces on the left side of \(\Gamma\), hence positive.

*Proof.* For a function \(a\) with \(a(\theta d)=-a(d)\), let \(\partial a(f)=\sum_{d\in f}a(d)\). Then \(\sum_f\partial a(f)=\sum_da(d)=0\). For an edge \(\{d,\theta d\}\) whose darts lie in different faces, the function equal to \(1\) on \(d\), \(-1\) on \(\theta d\) and \(0\) elsewhere has \(\partial\)-values \(+1\) on \(\operatorname{face}(d)\), \(-1\) on \(\operatorname{face}(\theta d)\) and \(0\) elsewhere. These pairs of faces are the ends of the non-loop edges of the connected dual \(K^*\), so, adding such functions along paths in \(K^*\), every function on faces with total sum \(0\) is a value of \(\partial\). Take \(\partial a\) equal to \(1\) on every face other than \(f_\infty\) and to \(1-F\) on \(f_\infty\).

Let \(\mathcal L\) be the left side of \(\Gamma\), so \(f_\infty\notin\mathcal L\). In \(\sum_{f\in\mathcal L}\partial a(f)\), an edge with both darts in faces of \(\mathcal L\) contributes \(a(d)+a(\theta d)=0\), an edge of \(\Gamma\) contributes its dart with \(\mathcal L\) on the left, which is the dart of the traversal, and no other edge contributes (Theorem 3.2 of [Sphere maps](sphere-maps.md)). Hence \(\sum_{d\in\Gamma}a(d)=\sum_{f\in\mathcal L}\partial a(f)=|\mathcal L|\ge1\). \(\square\)

**The spoke map.** Let \(T^+\) be obtained from \(T\) by adding, inside every \(t\in\mathcal T\), a *centre* \(c_t\) joined to the three vertices of \(t\) by three *spokes*. Precisely, if the face \(t\) consists of the darts \(\alpha\) from \(p\) to \(q\), \(\beta\) from \(q\) to \(w\) and \(\gamma\) from \(w\) to \(p\), add the darts \(pc,cp,qc,cq,wc,cw\) (with \(c=c_t\) and \(xy\) the dart from \(x\) to \(y\)), give \(c\) the rotation \((cp,cw,cq)\), and insert \(pc\) after \(\theta\gamma\) in the rotation at \(p\), \(qc\) after \(\theta\alpha\) at \(q\), and \(wc\) after \(\theta\beta\) at \(w\).

**Lemma 3.2.** \(T^+\) is a sphere map. Its faces are the faces of \(T\) not in \(\mathcal T\) and, for each \(t\in\mathcal T\), three *sectors* \((\alpha,qc,cp)\), \((\beta,wc,cq)\), \((\gamma,pc,cw)\), one for each edge of \(t\).

*Proof.* With the new rotations, \(\varphi(\alpha)=\sigma(\theta\alpha)=qc\), \(\varphi(qc)=\sigma(cq)=cp\) and \(\varphi(cp)=\sigma(pc)=\alpha\), since \(\alpha\) followed \(\theta\gamma\) at \(p\) before the insertion. The other two sectors are checked in the same way. For any other dart \(x\), \(\sigma(\theta x)\) is unchanged, because the insertions only change the successors of \(\theta\alpha\), \(\theta\beta\), \(\theta\gamma\). Each \(t\) adds one vertex, three edges and, replacing one face by three, two faces, so \(\chi\) is unchanged; the map is connected. \(\square\)

Let \(H_0\) be the spanning subgraph of \(T^+\) consisting of all spokes. By Proposition 1.6(e) of [Sphere maps](sphere-maps.md), each component \(K\) of \(H_0\), with the rotations restricted, is a sphere map. For a component with at least one edge, let \(f_\infty(K)\) be the face of \(K\) whose region, in the sense of Proposition 4.1 of [Sphere maps](sphere-maps.md) applied in \(T^+\), contains \(t_0\). Fix on each such component a function \(a_K\) as in Lemma 3.1 with respect to \(f_\infty(K)\), and put
\[
a(t,v)=a_K(\text{dart from }c_t\text{ to }v),
\]
where \(K\) is the component containing \(c_t\). The dart from \(v\) to \(c_t\) then has weight \(-a(t,v)\).

## 4. The sum does not vanish

**Lemma 4.1.** Let \(\Gamma\) be a cycle of \(T\) containing at most one edge of each face of \(\mathcal T\) and none of \(t_0\). Let \(L_+\) be the sum of \(a(t,\text{head})\) over the darts of \(\Gamma\) traversed counterclockwise, \(t\) being the black face of the edge of the dart, and \(L_-\) the same sum for the clockwise traversal. Then \(L_+-L_->0\).

*Proof.* Replace every counterclockwise dart from \(u\) to \(v\), with black face \(t\), by the two spoke darts from \(u\) to \(c_t\) and from \(c_t\) to \(v\). The centres are distinct, so this gives a cycle \(\Gamma^+\) of \(H_0\), and its weight is \(\sum(a(t,v)-a(t,u))=L_+-L_-\), because the tails of the counterclockwise darts are the heads of the clockwise ones. By Lemma 3.1 it suffices to show that \(f_\infty(K)\) is not on the left of \(\Gamma^+\) in the component \(K\) of \(H_0\) containing it.

*Sides in \(T^+\).* \(\Gamma\) is also a cycle of \(T^+\); let \(\mathcal A\) be its side in \(T^+\) not containing \(t_0\). For an edge \(e\) of \(\Gamma\), let \(s_e\) be its sector; its three edges are \(e\) and the two spokes of the detour. Over \(\mathbb F_2\), \(\Gamma^+=\Gamma+\sum_{e\in\Gamma}b_{s_e}\), and \(\Gamma=\sum_{f\in\mathcal A}b_f\), so by Lemma 3.1(c) of [Sphere maps](sphere-maps.md) the sides of \(\Gamma^+\) in \(T^+\) are \(\mathcal A\mathbin\triangle\mathcal S\) and its complement, where \(\mathcal S=\{s_e:e\in\Gamma\}\). Since \(t_0\) is not a sector, \(t_0\notin\mathcal A\mathbin\triangle\mathcal S\). We check that \(\mathcal A\mathbin\triangle\mathcal S\) lies on the left of the detour, using the dart from \(u\) to \(c_t\) of the detour of a counterclockwise dart from \(u\) to \(v\). If this dart is the dart \(\alpha\) of the face \(t\) (notation of Lemma 3.2, with \(p=u\), \(q=v\)), the face on the left of \(pc\) is the sector of the edge \(wp\), which is not in \(\mathcal S\) because \(t\) has only one edge in \(\Gamma\); it lies in \(\mathcal A\), because the sector of \(\alpha\) does (it is on the left of a counterclockwise dart) and the spoke \(pc\) between the two sectors is not in \(\Gamma\). If instead the face \(t\) contains the reverse dart, from \(v\) to \(u\), then (with \(p=v\), \(q=u\)) the face on the left of \(qc\) is the sector of the edge \(e=uv\) itself, which lies in \(\mathcal S\) and not in \(\mathcal A\), since it is on the left of the reverse of a counterclockwise dart. In both cases the face on the left is in \(\mathcal A\mathbin\triangle\mathcal S\), so by Lemma 3.3 of [Sphere maps](sphere-maps.md) the left side of \(\Gamma^+\) in \(T^+\) is \(\mathcal A\mathbin\triangle\mathcal S\).

*Sides in \(K\).* Faces of \(T^+\) that are \(K\)-adjacent share an edge outside \(K\), hence outside \(\Gamma^+\), so every region of \(K\) lies on one side of \(\Gamma^+\) in \(T^+\). Assign to each face of \(K\) the side of its region. An edge of \(K\) lies in \(\Gamma^+\) exactly when its two darts have their faces of \(T^+\) on different sides, that is, when its two faces of \(K\) (Proposition 4.1 of [Sphere maps](sphere-maps.md)) are assigned different sides. By the uniqueness in Theorem 3.2 there, this assignment is the partition of the faces of \(K\) into the two sides of \(\Gamma^+\), and the left side consists of the faces whose region lies in \(\mathcal A\mathbin\triangle\mathcal S\). The region of \(f_\infty(K)\) contains \(t_0\), so \(f_\infty(K)\) is on the right. \(\square\)

**Proposition 4.2** (A forest state). If a pair exists, then some pair \((r,s)\) has \(Q_s\) a forest.

*Proof.* Group the pairs according to the set \(D\) of edges joining \(r(t)\) and \(s(t)\). By Corollary 1.2, \(D\) is a disjoint union of cycles covering \(X\), with one edge in each \(t\in\mathcal T\), and the pairs with a given \(D\) correspond exactly to the independent choices of a direction on each cycle (tails give \(r\), heads give \(s\)). Each cycle \(C\) of \(D\) satisfies the hypothesis of Lemma 4.1. Writing \(L_\pm(C)\) as there, a counterclockwise cycle contributes \(-1\) to \(J\) and \(L_+(C)\) to \(\omega(s)\), and a clockwise one \(+1\) and \(L_-(C)\). The pairs with edge set \(D\) therefore contribute
\[
\prod_{C\subseteq D}\Bigl(-\mathrm i\,e^{xL_+(C)}+\mathrm i\,e^{xL_-(C)}\Bigr)
\]
to \(Z(x)\). Each factor vanishes at \(x=0\) with derivative \(-\mathrm i(L_+(C)-L_-(C))\ne0\), so if \(D\) has \(c(D)\) cycles, the Taylor expansion of the product at \(0\) begins with
\[
(-\mathrm i)^{c(D)}\prod_{C\subseteq D}\bigl(L_+(C)-L_-(C)\bigr)\,x^{c(D)} .
\]
Since a pair exists, some \(D\) occurs; let \(c_{\min}\) be the least number of cycles. The coefficient of \(x^{c_{\min}}\) in \(Z\) is \((-\mathrm i)^{c_{\min}}\) times a sum of positive numbers, one for each \(D\) with \(c_{\min}\) cycles; groups with more cycles contribute no such term. So \(Z\) is not identically zero.

On the other hand, \(Z(x)=\sum_s e^{x\omega(s)}\sum_r\mathrm i^{J(r,s)}\), and by Lemma 2.2 the inner sum vanishes whenever \(Q_s\) contains a cycle. Hence some \(s\) with a partner has \(Q_s\) a forest. \(\square\)

The sum \(Z\) is finite and serves only to prove existence; the argument gives no bound on the work needed to find the pair.

## 5. Exercises

**5.1.** In the octahedron of Exercise 4.1 of [Pairs of states](pairs-of-states.md), with the pairs \((r_1,r_2)\) and \((r_2,r_1)\), show that \(D\) is the boundary of the white face opposite \(t_0\), and that \(Q_{r_1}\) and \(Q_{r_2}\) are forests.

**5.2.** Show that the values \(J(r_1,r_2)\) and \(J(r_2,r_1)\) in Exercise 5.1 are \(-1\) and \(1\) in some order, and that \(Z(x)=-\mathrm i\,e^{xL_+}+\mathrm i\,e^{xL_-}\) for the single cycle \(D\).

**5.3.** Show by an example that the conclusion of Lemma 1.1 fails for a cycle of \(T\) that is not traversed along the chosen darts of a state: take the boundary of a single black face of \(\mathcal T\).

## 6. Solutions

**5.1.** From the solution of Exercise 4.1 there, the edges \(r_1(t)r_2(t)\) are \((-e_2)(-e_3)\), \((-e_3)(-e_1)\) and \((-e_1)(-e_2)\), the boundary of the face \((-e_1)(-e_2)(-e_3)\), which is white. For \(s=r_2\), the edges opposite \(s(t)\) are \(e_1(-e_2)\), \(e_2(-e_3)\) and \(e_3(-e_1)\), three disjoint edges; for \(s=r_1\) they are \(e_1(-e_3)\), \(e_2(-e_1)\) and \(e_3(-e_2)\). Both are forests.

**5.2.** The inner side of the cycle \(D\) is the white face \(w\) it bounds (its other side contains \(t_0\)), so \(I=0\), \(B=0\), \(W=1\) and \(l=0\): the black faces of the three edges are \(t_1,t_2,t_3\), on the other side. The counterclockwise \(\delta\)-sum is \(2l-h=-3\). The pair whose darts \(r(t)\to s(t)\) run counterclockwise has \(J=-1\), the other \(J=1\), and \(\mathrm i^{-1}=-\mathrm i\). Since \(s\) is the head state, \(\omega(s)\) is \(L_+\) for the counterclockwise pair and \(L_-\) for the other.

**5.3.** For the boundary of a black face \(t\in\mathcal T\), traversed so that \(t\) is on the left, every dart has \(\delta=+1\), so the sum is \(3\), although \(t\) is the inner side, so that this traversal is counterclockwise. Such a cycle never consists of chosen darts: all three of its edges have \(t\) as their black face, and \(t\) has only one chosen dart. Lemma 1.1 depends on the matching identity \(B=I+l\).

## References

- [OpenAI-B] OpenAI, *Paired states and Hamiltonian cycles in cubic bipartite planar graphs*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/Paired-states-and-Hamiltonian-cycles-in-cubic-bipartite-planar-graphs-September-24-2026/paper.pdf
- [Ken] R. Kenyon, *Conformal invariance of loops in the double-dimer model*, Communications in Mathematical Physics 326 (2014), 477–497; preprint 2011. https://arxiv.org/abs/1105.4158
- [KPW] R. W. Kenyon, J. G. Propp and D. B. Wilson, *Trees and matchings*, Electronic Journal of Combinatorics 7 (2000), R25. https://arxiv.org/abs/math/9903025
