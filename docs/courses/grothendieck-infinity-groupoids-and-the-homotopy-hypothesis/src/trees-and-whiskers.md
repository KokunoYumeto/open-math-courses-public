# Trees and whiskers

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The inductive step of the main theorem builds, for each model, an object of partial paths: cells moving along cells of one dimension higher. Its representing objects are glued from free models on finite globular sets that are not pasting schemes: pasting schemes with extra *whiskers*, a new cell attached to each cell of one dimension. This lesson proves that these free models are contractible, using only the expansions of higher index already available in the descending induction. The key case is a *tree diagram*: in one dimension, the arrows form a tree instead of a string. Comparing a tree with a string on the same vertices gives maps in both directions whose composite is homotopic to the identity on generators; duplicating the generators by expansions of higher index turns these homotopies on generators into a statement about the whole model.

**Prerequisites.** [*Cutoffs, spines and free shapes*](cutoffs-spines-and-free-shapes.md): the category \(\mathcal A_q\) of \(q\)-coskeletal models, free shapes (Proposition 2.2), the induction hypotheses and Lemma 3.2. [*The homotopy calculus*](the-homotopy-calculus.md): the groupoid of Lemma 1.1, Lemma 3.2.

Throughout, \(q\ge0\) and \(0\le n<q\) are fixed, \(\mathsf E(q,j)\) is assumed for \(n<j\le q\), all constructions take place in \(\mathcal A_q\), and \(F\) stands for the free \(q\)-coskeletal model \(F_q\).

## 1. Tree diagrams

A *tree diagram at depth \(0\)* is a finite nonempty oriented tree, viewed as a globular set of dimensions \(0\) and \(1\); a single vertex is allowed. A *tree diagram at depth \(n>0\)* is either a vertex or a string \([K_1,\ldots,K_p]\) of suspended tree diagrams \(K_i\) at depth \(n-1\), glued at vertices as for pasting schemes. A tree diagram \(K\) at depth \(n\) is a finite globular set of height at most \(n+1\). Its *slots* at depth \(n\) are the places where the recursion reaches depth \(0\); in each slot, the tree vertices are \(n\)-cells with a common boundary and the tree edges are \((n+1)\)-cells, with arbitrary orientations. The free model \(F(K)\) is cellular: attach the finitely many cells of \(K\) along their boundaries in increasing dimension. It has many more cells than \(K\), created by the operations of \(\mathcal C\).

**Proposition 1.1 (trees are contractible).** For every tree diagram \(K\) at depth \(n\), the model \(F(K)\) is contractible.

**Proof.** In each slot, order the tree vertices and replace the tree by the string \(x_1\to x_2\to\cdots\) on the same vertices. The result \(K^{\mathrm{lin}}\) is a pasting scheme with the same cells as \(K\) through dimension \(n\). Put \(A=F(K)\) and \(L=F(K^{\mathrm{lin}})\); \(L\) is contractible by Proposition 2.2 of the previous lesson.

Define morphisms \(f:A\to L\) and \(g:L\to A\) fixing the generating cells through dimension \(n\). The morphism \(f\) sends each tree edge to the composite, at level \(n\), of the string edges along the path between its endpoints, using \(n\)-inverses for edges traversed backwards; \(g\) sends each string edge to the composite along the path in the tree. Within one slot the vertices are parallel \(n\)-cells, so these assignments have the required faces, and they extend to morphisms of models by the universal property of free models.

For each tree edge \(e\), an \((n+1)\)-cell of \(K\), the cell \(gf(e)\) is the composite along a walk in the tree with the same endpoints as \(e\). In the groupoid of \((n+1)\)-cells modulo homotopy (Lemma 1.1 of the lesson on the homotopy calculus), inverses of composites expand, and deleting backtracking pairs reduces the walk to the unique path between the endpoints of \(e\) in the tree, which is \(e\) itself. So there is an \((n+2)\)-cell
\[
\alpha_e:e\longrightarrow gf(e)\quad\text{in }A .
\]

Duplicate the generators. Let \(Q\) be obtained from \(A\) by adjoining, for each tree edge \(e\), a new \((n+1)\)-cell \(e'\) parallel to \(e\) and an \((n+2)\)-cell \(\delta_e:e\to e'\). Let \(a_0:A\to Q\) be the inclusion; it is a finite composite of pushouts of \(J_{n+1}\) with cellular sources, hence a weak equivalence by \(\mathsf E(q,n+1)\), which is assumed since \(n<n+1\le q\). Let \(a_1:A\to Q\) fix the generators through dimension \(n\) and send each \(e\) to \(e'\); this is a morphism because \(K\) has no generators above dimension \(n+1\). Let \(r:Q\to A\) keep the old generators, send \(e'\) to \(e\) and \(\delta_e\) to the unit of \(e\). Then \(ra_0=ra_1=\mathrm{id}_A\), so two-out-of-three gives \(r\in\mathcal W\) and then \(a_1\in\mathcal W\). Let \(h:Q\to A\) be the identity on \(A\), send \(e'\) to \(gf(e)\) and \(\delta_e\) to \(\alpha_e\). Then
\[
ha_0=\mathrm{id}_A,\qquad ha_1=gf ,
\]
so \(h\in\mathcal W\) and \(gf\in\mathcal W\). Only \(J_{n+1}\) was used.

The weak equivalence \(gf\) factors through the contractible model \(L\). So its map on components factors through a point and its maps on homotopy groups through trivial groups; since these maps are bijective, \(A\) has one component and trivial homotopy groups. \(A\) is nonempty, hence contractible. When \(q=n+1\), the attachments of \(J_q\) used above are covered by Lemma 3.1 of the previous lesson. \(\square\)

## 2. Whiskered shapes

Let \(S\) be a pasting scheme with \(\dim S\le q\), and \(\epsilon\in\{0,1\}\). Let \(H_\epsilon(S)\) be obtained from \(F(S)\) by adjoining, for each \(n\)-cell \(x\) of the globular set \(S\), a new \(n\)-cell \(x'\) parallel to \(x\) and an \((n+1)\)-cell joining them, oriented \(x\to x'\) if \(\epsilon=0\) and \(x'\to x\) if \(\epsilon=1\). The higher cells of \(S\) keep their boundaries. If \(S\) has no \(n\)-cells, \(H_\epsilon(S)=F(S)\). This is a cellular construction: attach each \(x'\) along its boundary, then the joining cell.

**Proposition 2.1 (whiskered shapes are contractible).** \(H_\epsilon(S)\) is contractible, for both values of \(\epsilon\), and also when the orientation is chosen separately for each \(n\)-cell of \(S\).

**Proof.** Put \(S'=T_n(S)\), the spine of Lemma 2.1 of the previous lesson. It has the same \(n\)-cells as \(S\), so the same whiskers can be adjoined. In \(S'\) every slot at depth \(n\) is a string of \((n+1)\)-cells or a single \(n\)-cell; adjoining a leaf with its edge at every vertex of the slot turns it into a finite oriented tree. So \(H_\epsilon(S')\) is the free model on a tree diagram at depth \(n\), and is contractible by Proposition 1.1; any orientations are allowed.

By Lemma 2.1 of the previous lesson, \(S'\to S\) is a finite composite of pushouts of \(\sigma_j\) with \(j>n\). These add no \(n\)-cells, so performing them after the whiskers gives \(H_\epsilon(S)\), by the universal properties of the pushouts. Hence \(H_\epsilon(S')\to H_\epsilon(S)\) is an upper \(J\)-cellular extension of a cellular object, and a weak equivalence by Section 3 of the previous lesson. So \(H_\epsilon(S)\) is contractible. Branches of \(S\) that end before depth \(n\) carry no whiskers and are unchanged. \(\square\)

The statement \(\mathsf E(q,n)\) itself has not been used; it is proved in the next lesson.

## 3. Exercises

**3.1** (easy). Draw the tree diagram at depth \(0\) obtained from the string \(x_0\to x_1\to x_2\) by adjoining a leaf at each vertex, and the string used in the proof of Proposition 1.1.

**3.2** (easy). Show that for the tree \(x_0\leftarrow x_1\to x_2\), the maps \(f\) and \(g\) of the proof of Proposition 1.1, with the order \(x_0,x_1,x_2\), send the edge \(x_1\to x_0\) to the inverse of the string edge \(x_0\to x_1\) and back.

**3.3** (medium). Explain why the duplication argument in the proof of Proposition 1.1 needs only \(J_{n+1}\) and not \(J_n\).

**3.4** (medium). Let \(K\) be a tree diagram at depth \(0\) with two vertices and one edge. Show directly that \(F(K)=D_1\) is contractible.

## 4. Solutions

**3.1.** The tree has the path \(x_0\to x_1\to x_2\) and three leaves \(y_i\), with edges \(x_i\to y_i\) (or \(y_i\to x_i\)). With the order \(x_0,y_0,x_1,y_1,x_2,y_2\), the string is \(x_0\to y_0\to x_1\to y_1\to x_2\to y_2\).

**3.2.** The tree edge \(x_1\to x_0\) has endpoints \(x_1,x_0\); the path in the string goes backwards along \(x_0\to x_1\), so \(f\) sends it to \(w_0\) of that string edge. The string edge \(x_0\to x_1\) goes backwards along the tree edge \(x_1\to x_0\), so \(g\) sends it to the inverse of the tree edge, and \(gf\) of the tree edge is a double inverse, homotopic to it.

**3.3.** The homotopies \(\alpha_e\) are \((n+2)\)-cells between \((n+1)\)-cells. Adjoining a duplicate \(e'\) of an \((n+1)\)-cell and a cell \(e\to e'\) is a pushout of \(J_{n+1}\). The \(n\)-cells of \(K\) are never duplicated, since \(f\) and \(g\) fix them.

**3.4.** \(D_1=F(d_1)\) is the free model on a pasting scheme, so Proposition 2.2 of the previous lesson applies; this is also the case \(K=K^{\mathrm{lin}}\) of Proposition 1.1, where \(f\) and \(g\) are identities.

## Sources

- [OpenAI-312] OpenAI, *The Grothendieck homotopy hypothesis via elementary expansions*, OpenAI Math Release preprint, 24 September 2026, Sections 2.4 and 2.5. https://github.com/openai/math/tree/main/preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026
