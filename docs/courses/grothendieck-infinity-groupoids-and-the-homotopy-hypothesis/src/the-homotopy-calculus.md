# The homotopy calculus

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson develops the homotopy theory of a single model \(X\) of the fixed coherator \(\mathcal C\): composition, units and inverses, the homotopy relation between parallel cells, components and homotopy groups. Weak equivalences are the morphisms inducing bijections on components and isomorphisms on all homotopy groups. The main results are a test for weak equivalences with exactly prescribed boundaries (Proposition 3.1), their closure properties (Lemma 3.2), and the identification of the morphisms with the right lifting property against all boundary inclusions (Lemma 4.2). No model structure is used.

**Prerequisites.** [*Globular theories and their models*](globular-theories-and-their-models.md): coherators, models, the operations of a model (Proposition 3.2), free models \(D_j\), \(\partial D_j\) and the maps \(I_j\), \(J_j\) (Section 5).

## 1. Units, compositions and inverses

Contractibility of \(\mathcal C\) provides the following operations, chosen once and for all. Each is constructed dimension by dimension: in its lowest dimension its faces are prescribed directly, and in each higher dimension its faces are the operations already constructed applied to faces. Every pair to be filled has an arity of height at most the output dimension, so it is admissible.

- *Units.* For an \(r\)-cell \(a\), the unit \(e(a):a\to a\) is an \((r+1)\)-cell, a filler of the pair consisting twice of the identity of \(d_r\). Write \(e_p^q(a)\) for the iterated unit of a \(p\)-cell \(a\), of dimension \(q\), with \(e_p^p(a)=a\).
- *Compositions.* For \(r\)-cells \(\alpha,\gamma\) and \(i<r\) with \(s_i\gamma=t_i\alpha\), the composite \(\gamma*_i\alpha\) is an \(r\)-cell with \(s_i(\gamma*_i\alpha)=s_i\alpha\) and \(t_i(\gamma*_i\alpha)=t_i\gamma\), and with \(k\)-faces \(s_k\gamma*_is_k\alpha\) and \(t_k\gamma*_it_k\alpha\) for \(i<k<r\). Its arity is \(d_r\amalg_{d_i}d_r\).
- *Inverses.* For an \(r\)-cell \(\alpha\) and \(i<r\), the \(i\)-inverse \(w_i(\alpha)\) is an \(r\)-cell with \(s_iw_i(\alpha)=t_i\alpha\) and \(t_iw_i(\alpha)=s_i\alpha\), and with \(k\)-faces \(w_i(s_k\alpha)\), \(w_i(t_k\alpha)\) for \(i<k<r\).

Morphisms of models preserve these operations. Let \(r\ge1\) and let \(\alpha,\beta\) be parallel \(r\)-cells, or \(r=0\) and \(\alpha,\beta\) vertices. Write \(\alpha\sim\beta\) if there is an \((r+1)\)-cell \(\alpha\to\beta\). This is an equivalence relation: units give reflexivity, \(w_r\) turns \(H:\alpha\to\beta\) into a cell \(\beta\to\alpha\), and \(*_r\) composes \(\alpha\to\beta\) and \(\beta\to\gamma\). Put
\[
\begin{gathered}
\pi_0(X)=X_0/{\sim},\\
\pi_r(X;u,v)=\{\alpha:u\to v\}/{\sim}\quad(r\ge1),
\end{gathered}
\]
for parallel \((r-1)\)-cells \(u,v\); these *homotopy sets* may be empty.

**Lemma 1.1.** Composition at any level respects homotopy. For fixed \(r\ge1\), composition \(*_{r-1}\) makes the homotopy sets \(\pi_r(X;u,v)\), for \(u,v\) ranging over the \((r-1)\)-cells with a fixed boundary, the hom-sets of a groupoid.

**Proof.** If \(H:\alpha\to\alpha'\) and \(\gamma*_i\alpha\) is defined, then \(e(\gamma)*_iH\) is an \((r+1)\)-cell from \(\gamma*_i\alpha\) to \(\gamma*_i\alpha'\), by the face equations of compositions and units; similarly on the other side. Associativity: \((\gamma*_{r-1}\beta)*_{r-1}\alpha\) and \(\gamma*_{r-1}(\beta*_{r-1}\alpha)\) are values of two operations on the arity \(d_r\amalg_{d_{r-1}}d_r\amalg_{d_{r-1}}d_r\) of height \(r\) with the same faces; they form an admissible pair with \(j=r+1\), and a filler is a homotopy between them. The unit and inverse laws follow in the same way, from operations on \(d_r\). \(\square\)

For a vertex \(x\) and \(r\ge1\), the *homotopy group* is
\[
\pi_r(X,x)=\pi_r\bigl(X;e_0^{r-1}(x),e_0^{r-1}(x)\bigr),
\]
with composition \(*_{r-1}\). Morphisms of models induce maps of homotopy sets and homomorphisms of homotopy groups.

## 2. Division with prescribed boundaries

Multiplication below the top level changes the whole boundary of a cell. The following division calculus controls this.

**Lemma 2.1 (division).** Let \(\gamma\) be an \(r\)-cell and \(i<r\). Fix a boundary \(b\) of dimension \(r\) — a pair of parallel \((r-1)\)-cells, or nothing if \(r=0\) — such that \(r\)-cells \(\alpha\) with boundary \(b\) satisfy \(t_i\alpha=s_i\gamma\). Left multiplication \(\alpha\mapsto\gamma*_i\alpha\) induces a bijection from the homotopy set at \(b\) to the homotopy set at the boundary \(b'\) of the composites. The same holds for right multiplication. The sets may be empty.

**Proof.** *Universal normalizations.* Let \((g,a)\) be the generic pair of \(i\)-composable \(k\)-cells, the pair of top cells of \(d_k\amalg_{d_i}d_k\), for \(k>i\). Put \(U^k_{i+1}(g,a)=w_i(g)*_i(g*_ia)\). We construct operations \(U^k_h(g,a)\) for \(k\ge h>i\) such that

- (a) the faces of \(U^k_h(g,a)\) of dimension less than \(h\) are those of \(a\);
- (b) for \(h\le l<k\), the \(l\)-faces of \(U^k_h(g,a)\) are \(U^l_h\) applied to the \(l\)-faces of \((g,a)\).

For \(h=i+1\) this follows from the face equations: the \(i\)-faces of \(w_i(g)*_i(g*_ia)\) are \(s_ia\) and \(s_ig=t_ia\). In particular \(U^h_h(g,a)\) and \(a\) are parallel as operations on \(d_h\amalg_{d_i}d_h\), an arity of height \(h\). Choose fillers
\[
\begin{gathered}
c_h(g,a):a\to U^h_h(g,a),\\
\delta_h(g,a):U^h_h(g,a)\to a ,
\end{gathered}
\]
and for \(k>h\) put
\[
\begin{aligned}
&U^k_{h+1}(g,a)\\
&=e^k_{h+1}\delta_h(t_hg,t_ha)\\
&\quad*_h\Bigl(U^k_h(g,a)*_he^k_{h+1}c_h(s_hg,s_ha)\Bigr).
\end{aligned}
\]
By (b) the \(h\)-faces of \(U^k_h(g,a)\) are \(U^h_h(s_hg,s_ha)\) and \(U^h_h(t_hg,t_ha)\), so both compositions are defined, and the new \(h\)-faces are \(s_ha\) and \(t_ha\); lower faces are unchanged. In dimensions above \(h\) the faces obey the same formula, by the face equations of compositions and units. This proves (a) and (b) for \(h+1\).

*A left inverse.* Let \(\beta\) be an \(r\)-cell with boundary \(b'\). Start with \(z=w_i(\gamma)*_i\beta\), and for \(h=i+1,\ldots,r-1\) replace \(z\) by
\[
\begin{aligned}
&e^r_{h+1}\delta_h(t_h\gamma,t_hb)\\
&\quad*_h\bigl(z*_he^r_{h+1}c_h(s_h\gamma,s_hb)\bigr),
\end{aligned}
\]
where \(s_hb,t_hb\) denote the \(h\)-faces of the cells with boundary \(b\), determined by \(b\). The faces of \(z\) at each stage are those of \(U^r_h(\gamma,\alpha)\) for any \(\alpha\) with boundary \(b\), since they are computed from the faces of \(\beta\), which are those of \(\gamma*_i\alpha\). So every composition is defined, and the result \(K_\gamma(\beta)\) is an \(r\)-cell with boundary exactly \(b\). It depends on \(\beta\) through multiplications by fixed cells, so by Lemma 1.1 it induces a map \(K_\gamma\) of homotopy sets. If \(\beta=\gamma*_i\alpha\), then \(K_\gamma(\beta)=U^r_r(\gamma,\alpha)\), which is parallel to \(\alpha\) as an operation on \(d_r\amalg_{d_i}d_r\); a filler of this admissible pair is a homotopy. Hence \(K_\gamma L_\gamma=\mathrm{id}\), where \(L_\gamma\) is left multiplication.

*Bijectivity.* Interchanging left and right gives a left inverse for right multiplication. So every left or right multiplication by a fixed cell is injective on homotopy sets. \(K_\gamma\) is a composite of such multiplications, hence injective, and \(K_\gamma L_\gamma K_\gamma=K_\gamma\) gives \(L_\gamma K_\gamma=\mathrm{id}\). \(\square\)

**Lemma 2.2 (change of boundary and vertex).** Let \(r\ge1\).

1. For an \((r-1)\)-cell \(u\) with source vertex \(x\) and target vertex \(y\), the set \(\pi_r(X;u,u)\) is in natural bijection with \(\pi_r(X,x)\) and with \(\pi_r(X,y)\).
2. An arrow \(x\to y\) gives a bijection \(\pi_r(X,x)\to\pi_r(X,y)\), natural in morphisms of models.
3. If \(\pi_r(X;u,v)\) is nonempty, a cell \(u\to v\) gives a bijection \(\pi_r(X;u,u)\to\pi_r(X;u,v)\).

**Proof.** (3) is composition in the groupoid of Lemma 1.1. For \(r=1\), (1) is the definition and (2) is conjugation in the fundamental groupoid. Let \(r\ge2\), \(a=e^{r-1}_0(x)\) and \(w=u*_0a\). By Lemma 2.1 the maps
\[
\begin{gathered}
\pi_r(X;u,u)\xrightarrow{[\alpha]\mapsto[\alpha*_0e(a)]}\pi_r(X;w,w),\\
\pi_r(X;a,a)\xrightarrow{[\beta]\mapsto[e(u)*_0\beta]}\pi_r(X;w,w)
\end{gathered}
\]
are bijections, and \(\pi_r(X;a,a)=\pi_r(X,x)\). For \(y\) use \(b=e^{r-1}_0(y)\), \(w'=b*_0u\) and the maps \([\alpha]\mapsto[e(b)*_0\alpha]\), \([\beta]\mapsto[\beta*_0e(u)]\). For (2) apply (1) to \(u=e^{r-1}_1(p)\) for the arrow \(p:x\to y\), whose source and target vertices are \(x\) and \(y\). The fixed choice of operations makes all these bijections natural. \(\square\)

## 3. Weak equivalences

A morphism of models \(f:X\to Y\) is a *weak equivalence* if it induces a bijection \(\pi_0(X)\to\pi_0(Y)\) and isomorphisms \(\pi_r(X,x)\to\pi_r(Y,fx)\) for all \(r\ge1\) and all vertices \(x\). The class of weak equivalences is \(\mathcal W\).

**Proposition 3.1 (the exact-boundary test).** For a morphism \(f:X\to Y\) the following are equivalent.

1. \(f\in\mathcal W\).
2. \(f\) induces a bijection on \(\pi_0\) and bijections \(\pi_r(X;u,v)\to\pi_r(Y;fu,fv)\) for all \(r\ge1\) and all parallel \((r-1)\)-cells \(u,v\) of \(X\).
3. For every \(r\ge0\), every boundary \(b\colon\partial D_r\to X\) and every \(r\)-cell \(y\) of \(Y\) with boundary \(fb\), there are an \(r\)-cell \(x\) of \(X\) with boundary exactly \(b\) and an \((r+1)\)-cell \(fx\to y\) in \(Y\).

In particular a weak equivalence reflects homotopy between parallel cells.

**Proof.** (1)⇒(2). By Lemma 2.2(1), \(f\) is bijective on all homotopy sets \(\pi_r(X;u,u)\). We prove (2) by induction on \(r\). If \(\pi_r(Y;fu,fv)\) is nonempty, then \(fu\sim fv\); by injectivity on \(\pi_0\) (for \(r=1\)) or on \(\pi_{r-1}\) (for \(r\ge2\), by the induction hypothesis), \(u\sim v\), so \(\pi_r(X;u,v)\) is nonempty. Choose a cell \(u\to v\); by Lemma 2.2(3), composition with it and with its image identifies the map \(\pi_r(X;u,v)\to\pi_r(Y;fu,fv)\) with the map on \(\pi_r(-;u,u)\), which is bijective. If the set for \(Y\) is empty, so is the set for \(X\).

(2)⇒(3). For \(r=0\) use surjectivity on \(\pi_0\); for \(r\ge1\), surjectivity on \(\pi_r(X;u,v)\), where \(b=(u,v)\).

(3)⇒(2). (3) gives surjectivity on \(\pi_0\) and on every \(\pi_r(X;u,v)\). If parallel \(r\)-cells \(x_1,x_2\) of \(X\) (or vertices, for \(r=0\)) have homotopic images, apply (3) in dimension \(r+1\) to the boundary \((x_1,x_2)\) and a cell \(fx_1\to fx_2\): it produces a cell \(x_1\to x_2\). This is injectivity.

(2)⇒(1) is the special case of based homotopy groups. \(\square\)

**Lemma 3.2 (closure).** The class \(\mathcal W\) has the two-out-of-three property, is closed under retracts, and is closed under filtered colimits of morphisms. Hence a transfinite composite of weak equivalences is a weak equivalence.

**Proof.** *Two-out-of-three.* Let \(f:X\to Y\), \(g:Y\to Z\). If \(f,g\in\mathcal W\), then \(gf\in\mathcal W\). If \(g,gf\in\mathcal W\), the maps of \(f\) on components and homotopy groups are composites of bijections. If \(f,gf\in\mathcal W\), \(g\) is bijective on \(\pi_0\), and on homotopy groups at vertices \(f(x)\); every vertex of \(Y\) is joined by an arrow to some \(f(x)\), and Lemma 2.2(2) transfers bijectivity to it.

*Retracts.* Let \(f\) be a retract of \(f'\in\mathcal W\). Given the data of Proposition 3.1(3) for \(f\), map them into the corresponding data for \(f'\), apply the test there, and map the resulting cells back by the retraction. The boundary is preserved exactly because the composite of the two maps of arrows is the identity.

*Filtered colimits.* In Proposition 3.1(3) for the colimit, the boundary, the target cell and their finitely many face equations all occur at some stage, because filtered colimits are computed on cells (Theorem 4.3 of the previous lesson). Apply the test there and map its witnesses to the colimit.

*Transfinite composites.* By induction: successor stages are compositions, and at a limit stage the map from the initial object is the filtered colimit of the maps to the earlier stages. \(\square\)

A model \(X\) is *contractible* if \(X\to1\) is a weak equivalence. By Proposition 3.1(3) applied to \(X\to1\), whose target has one cell in each dimension, this means: \(X\) is nonempty, and every pair of parallel cells is joined by a cell.

## 4. Lifting tests

For a set \(K\) of morphisms, \(K\)-\(\mathrm{inj}\) denotes the morphisms with the right lifting property against every member of \(K\).

**Lemma 4.1.** A morphism \(f\) has the right lifting property against \(I_j\) exactly when every boundary \(b\) of dimension \(j\) in its domain, and every \(j\)-cell \(y\) of its codomain with boundary \(fb\), admit a \(j\)-cell \(x\) with boundary \(b\) and \(fx=y\). It has the right lifting property against \(J_j\) exactly when every \(j\)-cell \(x\) of its domain, and every \((j+1)\)-cell \(H\) of its codomain with source \(fx\), admit a \((j+1)\)-cell \(\tilde H\) with source \(x\) and \(f\tilde H=H\).

**Proof.** Morphisms out of \(D_j\), \(\partial D_j\) and \(D_{j+1}\) are cells and boundaries, and \(J_j\) is induced by \(\sigma_j:d_j\to d_{j+1}\). \(\square\)

**Lemma 4.2 (lifting tests).** If \(f\in\mathcal W\) has the right lifting property against \(J_j\), it has the right lifting property against \(I_j\). Moreover
\[
I\text{-}\mathrm{inj}=\mathcal W\cap J\text{-}\mathrm{inj}.
\]
Every morphism \(X\to1\) has the right lifting property against every \(J_j\).

**Proof.** Given \(b\) and \(y\) as in Lemma 4.1, Proposition 3.1(3) gives \(x\) with boundary \(b\) and a cell \(H:fx\to y\). Lifting \(H\) against \(J_j\) with source \(x\) gives \(\tilde H\) with \(f\tilde H=H\); its target is a \(j\)-cell with the same boundary as \(x\), namely \(b\), and with image \(y\).

An \(I\)-injective morphism satisfies Proposition 3.1(3) exactly, with the unit of the target cell as homotopy, so it is a weak equivalence. Each \(J_j\) is a composite of a pushout of \(I_j\), adjoining the new parallel cell, and a pushout of \(I_{j+1}\), adjoining the joining cell; so \(I\)-injective morphisms are \(J\)-injective. The first paragraph gives the reverse inclusion. Finally, a lifting problem of \(J_j\) against \(X\to1\) is solved by the unit of the prescribed source cell. \(\square\)

The unit \(e\) also gives a retraction \(D_{j+1}\to D_j\) of \(J_j\), sending the top cell to the unit of the \(j\)-cell. Hence every elementary expansion \(X\to X\amalg_{D_j}D_{j+1}\) has a retraction, and so has every transfinite composite of elementary expansions: choose the retractions at successor stages and take the induced map at limit stages. The existence of these retractions does not show that elementary expansions are weak equivalences; that is the main theorem of the course.

## 5. Exercises

**5.1** (easy). Show that \(\pi_1(X,x)\) is a group under \(*_0\), with neutral element the class of \(e(x)\).

**5.2** (medium). Let \(f:X\to Y\) induce a bijection on \(\pi_0\), and isomorphisms on all \(\pi_r\), \(r\ge1\), at one vertex of each component of \(X\). Show that \(f\) is a weak equivalence.

**5.3** (easy). Show that a contractible model is nonempty and that any two of its vertices are joined by an arrow.

**5.4** (medium). Let \(f:X\to Y\) be a weak equivalence and \(u,v\) parallel \((r-1)\)-cells of \(X\) with \(fu\sim fv\). Show that \(u\sim v\).

**5.5** (medium). Show that a morphism with the right lifting property against every \(I_j\) is surjective on cells in every dimension.

## 6. Solutions

**5.1.** By Lemma 1.1 the classes of arrows \(x\to x\) form the hom-set at \(x\) of a groupoid, which is a group. The unit law of Lemma 1.1 makes \([e(x)]\) neutral.

**5.2.** Let \(x'\) be a vertex of \(X\) and \(x\) the chosen vertex of its component, with an arrow \(p:x\to x'\). Lemma 2.2(2) gives bijections \(\pi_r(X,x)\to\pi_r(X,x')\) and \(\pi_r(Y,fx)\to\pi_r(Y,fx')\), the second for the arrow \(fp\), and naturality says that they intertwine the maps induced by \(f\). So the map at \(x'\) is bijective, and it is a homomorphism.

**5.3.** \(X\to1\) is surjective on \(\pi_0\), so \(X_0\ne\varnothing\); injectivity on \(\pi_0\), or Proposition 3.1(3) with \(r=1\), gives an arrow between any two vertices.

**5.4.** This is the injectivity in Proposition 3.1(2) one dimension lower: for \(r=1\) on \(\pi_0\), and for \(r\ge2\) on \(\pi_{r-1}(X;s u,t u)\).

**5.5.** By induction on \(j\). For \(j=0\), lifting against \(I_0:\varnothing\to D_0\) gives a preimage of every vertex. Let \(j\ge1\) and \(y\) a \(j\)-cell of the codomain. By the induction hypothesis \(sy\) has a preimage \(x_1\). If \(j=1\), choose any preimage \(x_2\) of \(ty\). If \(j\ge2\), the boundary of \(x_1\) maps to the common boundary of \(sy\) and \(ty\), and lifting \(ty\) against \(I_{j-1}\) with this boundary gives \(x_2\) parallel to \(x_1\) with \(fx_2=ty\). Lifting \(y\) against \(I_j\) with the boundary \((x_1,x_2)\) gives a preimage of \(y\).

## Sources

- [OpenAI-312] OpenAI, *The Grothendieck homotopy hypothesis via elementary expansions*, OpenAI Math Release preprint, 24 September 2026, Sections 1.2 and 1.3. https://github.com/openai/math/tree/main/preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026
- D. Ara, [*On the homotopy theory of Grothendieck \(\infty\)-groupoids*](https://arxiv.org/abs/1206.2941), J. Pure Appl. Algebra 217 (2013), Section 4: homotopy groups, division (Lemma 4.12) and the characterization of weak equivalences (Theorem 4.18).
