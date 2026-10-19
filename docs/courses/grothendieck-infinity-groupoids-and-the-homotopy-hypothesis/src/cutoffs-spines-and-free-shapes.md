# Cutoffs, spines and free shapes

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The main theorem of the course says that every elementary expansion of a cellular model is a weak equivalence. The proof is by descending induction on the dimension of the expansion. Descending induction needs a top dimension, which is supplied by a *cutoff*: the models in which every boundary above a fixed dimension \(q\) has exactly one filler (Section 1). This lesson also proves two facts that do not depend on the main theorem: cell attachments in high dimensions do not change low-dimensional cells, and free models on pasting schemes are contractible (Section 2). Section 3 sets up the descending induction, proves its first case, and derives a splitting lemma for upper cell attachments that the later lessons use.

**Prerequisites.** [*Globular theories and their models*](globular-theories-and-their-models.md) (models, Theorem 4.3, the small object argument Proposition 5.1) and [*The homotopy calculus*](the-homotopy-calculus.md) (weak equivalences, Proposition 3.1, Lemmas 3.2, 4.1 and 4.2).

## 1. The cutoff reflector

Fix \(q\ge0\). A model \(Y\) is *\(q\)-coskeletal* if every boundary of dimension \(j>q\) in \(Y\) has exactly one filler: the restriction
\[
\operatorname{Hom}(D_j,Y)\longrightarrow\operatorname{Hom}(\partial D_j,Y)
\]
is bijective for every \(j>q\). Distinct parallel \(q\)-cells are allowed. Let \(\mathcal A_q\subseteq\mathcal A\) be the full subcategory of \(q\)-coskeletal models. For \(k<q\), \(\mathcal A_k\subseteq\mathcal A_q\).

**Lemma 1.1 (cutoff reflector).** The inclusion \(\mathcal A_q\subseteq\mathcal A\) has a left adjoint \(R_q\), whose unit \(\eta:X\to R_qX\) is bijective on the cells of every dimension at most \(q\). For \(k<q\), \(R_kR_q\cong R_k\).

**Proof.** Let \(Z\) be the globular set that agrees with \(X\) through dimension \(q\) and has, in each dimension \(j>q\), exactly one cell over each pair of parallel \((j-1)\)-cells, with that pair as boundary. Let \(\eta:X\to Z\) be the identity through dimension \(q\) and send a cell of dimension \(j>q\) to the unique cell with the image boundary.

We interpret the generating operations on \(Z\) along the defining tower, keeping \(\eta\) compatible with the operations already interpreted (Proposition 3.2 of the first lesson). Let \(\theta:d_j\to S\) be a generating operation, adjoined for the pair \((\sigma,\tau)\). If \(j\le q\), then \(\dim S\le j\le q\), so \(Z(S)=X(S)\); put \(\theta_Z=\theta_X\). Its face equations hold in \(Z\) because \(\eta\) is compatible with \(\sigma\) and \(\tau\), and \(\eta\) is compatible with \(\theta\) because it is the identity in dimension \(j\). If \(j>q\), the pair \((\sigma_Z(z),\tau_Z(z))\) is a pair of parallel \((j-1)\)-cells; let \(\theta_Z(z)\) be the unique \(j\)-cell over it. Then \(\eta\theta_X(x)\) and \(\theta_Z(\eta x)\) are \(j\)-cells with the same boundary, hence equal. This makes \(Z\) a \(q\)-coskeletal model and \(\eta\) a morphism of models.

If \(Y\) is \(q\)-coskeletal and \(f:X\to Y\) a morphism, a globular map \(g:Z\to Y\) with \(g\eta=f\) must equal \(f\) through dimension \(q\) and send each higher cell to the unique filler of the image boundary; this defines \(g\), and it preserves every generating operation — of output dimension at most \(q\) because its inputs come from \(X\), and above \(q\) by uniqueness of fillers in \(Y\). So \(Z=R_qX\). Finally \(R_k\) and \(R_k|_{\mathcal A_q}\circ R_q\) are both left adjoint to the inclusion \(\mathcal A_k\subseteq\mathcal A\). \(\square\)

Write \(F_q=R_qF\) for the free \(q\)-coskeletal model, and \(D_j\), \(\partial D_j\), \(I_j\), \(J_j\) also for their images under \(R_q\) when working in \(\mathcal A_q\). Since \(R_q\) is a left adjoint, it preserves pushouts and cellular presentations. In \(\mathcal A_q\):

- \(I_j\) and \(J_j\) are isomorphisms for \(j>q\): for \(Y\) in \(\mathcal A_q\), a \(j\)-cell is determined by its boundary, and a \((j+1)\)-cell by its source, because its target is the unique \(j\)-cell parallel to its source;
- the image of \(J_q\) adjoins a \(q\)-cell parallel to a given one, and the joining \((q+1)\)-cell is forced;
- filtered colimits are computed in \(\mathcal A\): a filtered colimit of \(q\)-coskeletal models is \(q\)-coskeletal, since \(D_j\) and \(\partial D_j\) are finitely presentable;
- \(\mathcal A_q\) is cocomplete (colimits are reflections of colimits in \(\mathcal A\)), \(F_q(K)\) is finitely presentable for finite \(K\) (as in Theorem 4.3(2) of the first lesson), and the small object argument holds in \(\mathcal A_q\), with the same proof.

Weak equivalences, homotopy sets and the results of the previous lesson apply to the models in \(\mathcal A_q\), which are models of \(\mathcal C\); closure under filtered colimits holds in \(\mathcal A_q\) because these colimits are computed in \(\mathcal A\).

**Lemma 1.2 (high attachments preserve low cells).** Let \(k\ge0\). In \(\mathcal A\), every relative cellular extension that uses only \(I_j\) with \(j>k\) is bijective on the cells of every dimension at most \(k\). The same holds in \(\mathcal A_q\) when \(k<q\), and for extensions that use only \(J_j\) with \(j>k\).

**Proof.** \(R_k(I_j)\) is an isomorphism for \(j>k\), and \(R_k\) preserves colimits, so \(R_k\) sends such an extension \(X\to Y\) to an isomorphism. In the naturality square of the units \(X\to R_kX\) and \(Y\to R_kY\), both units are bijective on cells of dimension at most \(k\), and so is \(R_kX\to R_kY\); hence so is \(X\to Y\). In \(\mathcal A_q\) use the reflection of \(\mathcal A_q\) onto \(\mathcal A_k\). Each \(J_j\) is a pushout of \(I_j\) followed by a pushout of \(I_{j+1}\). \(\square\)

## 2. Spines and free shapes

The *suspension* \(\Sigma S\) of a pasting scheme \(S\) with table \((h_1,b_1,\ldots,h_l)\) is the pasting scheme with table \((h_1+1,b_1+1,\ldots,h_l+1)\): two new vertices, the *poles*, and the cells of \(S\) raised by one dimension, its vertices becoming arrows between the poles. For nonempty pasting schemes \(S_1,\ldots,S_p\) let
\[
\begin{aligned}
[S_1,\ldots,S_p]&=\Sigma S_1\amalg_{d_0}\Sigma S_2\\
&\qquad\amalg_{d_0}\cdots\amalg_{d_0}\Sigma S_p ,
\end{aligned}
\]
with vertices \(v_0,\ldots,v_p\), the suspension of \(S_i\) sitting between \(v_{i-1}\) and \(v_i\). Every pasting scheme is a single vertex or of this form: split its table at the gluings with \(b_a=0\) and lower all dimensions of each block by one. Let \(v(S)\) be the first vertex of \(S\).

Define subschemes \(T_m(S)\), \(m\ge0\): a vertex is its own \(T_m\), and for \(S=[S_1,\ldots,S_p]\),
\[
\begin{aligned}
T_0(S)&=[v(S_1),\ldots,v(S_p)],\\
T_m(S)&=[T_{m-1}(S_1),\ldots,\\
&\qquad T_{m-1}(S_p)]\quad(m\ge1).
\end{aligned}
\]
Thus \(T_0(S)\) is the string of arrows \(v_0\to v_1\to\cdots\to v_p\) given by the first arrow of each slot, and \(T_m(S)\) keeps everything up to depth \(m\) and one arrow per slot at depth \(m\).

**Lemma 2.1 (spines).** For every pasting scheme \(S\) and \(m\ge0\), \(T_m(S)\) has height at most \(m+1\) and contains all cells of \(S\) of dimension at most \(m\). The inclusion \(T_m(S)\to S\) is a finite composite of pushouts, in \(\mathbf{Glob}\), of the inclusions \(\sigma_j:d_j\to d_{j+1}\) with \(j>m\).

**Proof.** The height and cell claims follow from the recursion. First, every pasting scheme \(S\) is obtained from \(v(S)\) by finitely many pushouts of source inclusions \(\sigma_j\), \(j\ge0\). This is induction on the recursion: for \(S=[S_1,\ldots,S_p]\), attach the outer string of arrows by pushouts of \(\sigma_0\), using in the \(i\)-th slot the arrow \(\Sigma v(S_i)\); then build each \(S_i\) from \(v(S_i)\) by the induction hypothesis and suspend these attachments into the \(i\)-th slot. Suspension turns a pushout of \(\sigma_j\) into a pushout of \(\sigma_{j+1}\), the two added cells acquiring the poles as their outermost faces.

For \(m=0\), rebuild each \(S_i\) from \(v(S_i)\) in its slot; all these attachments are suspended once, so they use \(\sigma_j\) with \(j\ge1\). For \(m\ge1\), the induction hypothesis builds \(S_i\) from \(T_{m-1}(S_i)\) with \(\sigma_j\), \(j>m-1\), and suspension raises the indices above \(m\). \(\square\)

**Proposition 2.2 (free shapes are contractible).** For every pasting scheme \(S\) and every \(q\ge0\), the models \(F(S)\) and \(F_q(S)\) are contractible.

**Proof.** Let \(a,b\) be parallel \(m\)-cells of \(F(S)\) (any two vertices if \(m=0\)). By Lemma 2.1, \(F(T_m(S))\to F(S)\) is a composite of pushouts of \(J_j\) with \(j>m\), since \(F\) preserves pushouts; by Lemma 1.2 it is bijective on cells of dimension at most \(m\). So \(a,b\) lift to parallel cells \(a',b'\) of \(F(T_m(S))\). By Theorem 4.3(1) of the first lesson these are operations \(d_m\to T_m(S)\) of \(\mathcal C\), and they form an admissible pair because \(\dim T_m(S)\le m+1\). A filler is an \((m+1)\)-cell \(a'\to b'\), whose image joins \(a\) to \(b\). As \(S\) has a vertex, \(F(S)\) is nonempty, hence contractible.

For \(F_q(S)\): parallel \(m\)-cells with \(m<q\) come from \(F(S)\) by Lemma 1.1, and the image of the filler just constructed joins them; for \(m\ge q\) the filler exists in the \(q\)-coskeletal model. \(\square\)

This argument uses no statement about elementary expansions.

## 3. The descending induction

Fix \(q\ge0\). For \(0\le n\le q\) consider the statement:

> \(\mathsf E(q,n)\): for every cellular object \(X\) of \(\mathcal A_q\) and every morphism \(a:D_n\to X\), the pushout \(X\to X\amalg_{D_n}D_{n+1}\) of \(J_n\) along \(a\) is a weak equivalence.

Here cellular objects may have arbitrary transfinite presentations, and \(a\) is any \(n\)-cell, not necessarily a generator of the presentation. The statements are proved by descending induction on \(n\), for each \(q\); the main theorem follows by letting \(q\) grow (lesson 5).

**Lemma 3.1 (the top case).** \(\mathsf E(q,q)\) holds for every \(q\ge0\).

**Proof.** Let \(i:X\to Y\) be the pushout of \(J_q\) along \(a\). It has a retraction \(r:Y\to X\) sending the new \(q\)-cell to \(a\) and the joining cell to the unit of \(a\). For \(q>0\), \(i\) is bijective on cells of dimension less than \(q\) by Lemma 1.2. We check Proposition 3.1(3) of the previous lesson in dimension \(d\). If \(d<q\), the given \(d\)-cell of \(Y\) comes from a \(d\)-cell of \(X\) with the prescribed boundary, and its unit is the homotopy. If \(d=q\), apply \(r\) to the given cell \(y\): \(r(y)\) has the prescribed boundary since \(ri=\mathrm{id}\), and \(ir(y)\) is parallel to \(y\), so the two are joined by the unique \((q+1)\)-cell over them. If \(d>q\), the prescribed boundary has a unique filler in \(X\), whose image is the given cell. For \(q=0\) only the last two cases occur. \(\square\)

For the rest of this section and in the next two lessons, fix \(0\le n<q\) and assume \(\mathsf E(q,j)\) for all \(n<j\le q\). An index \(j\) is *upper* if \(j>n\); an *upper* \(I\)- or \(J\)-cellular extension uses only \(I_j\) or \(J_j\) with \(j\) upper.

A morphism with the right lifting property against every member of a set \(K\) has it against every relative \(K\)-cellular extension: lifting properties pass to pushouts, coproducts and transfinite composites, the last by choosing lifts stage by stage. Since \(J_j\) is a composite of two boundary attachments, every stage of a \(J\)-cellular extension of a cellular object is cellular. Hence every upper \(J\)-cellular extension with cellular source is a weak equivalence: a pushout of a coproduct of upper \(J_j\) is a transfinite composite of single pushouts, each a weak equivalence by \(\mathsf E(q,j)\) for \(j\le q\) and an isomorphism for \(j>q\), and Lemma 3.2 of the previous lesson handles transfinite composites.

**Lemma 3.2 (upper splitting).** Let \(i:U\to V\) be an upper \(I\)-cellular extension with \(U\) cellular and \(i\in\mathcal W\). Then \(i\) has a retraction, and for every morphism \(U\to U'\) with \(U'\) cellular, the pushout \(U'\to U'\amalg_UV\) is a weak equivalence.

**Proof.** The small object argument for the upper \(J_j\) factors \(i=pa\) with \(a:U\to Z\) an upper \(J\)-cellular extension and \(p:Z\to V\) with the right lifting property against every upper \(J_j\). By the preceding paragraph \(a\in\mathcal W\), so \(p\in\mathcal W\) by two-out-of-three, and by Lemma 4.2 of the previous lesson \(p\) has the right lifting property against every upper \(I_j\). As \(i\) is an upper \(I\)-cellular extension, the square \(pa=i\cdot\mathrm{id}\) has a diagonal \(s:V\to Z\) with \(si=a\) and \(ps=\mathrm{id}_V\). So \(i\) is a retract of \(a\) in the category of objects under \(U\).

Every elementary expansion has a retraction, and so has every \(J\)-cellular extension (end of the previous lesson); let \(t:Z\to U\) be a retraction of \(a\). Then \(tsi=ta=\mathrm{id}_U\), so \(ts\) retracts \(i\). Pushing the retract diagram out along \(U\to U'\) exhibits the pushout of \(i\) as a retract of the pushout of \(a\). The latter is an upper \(J\)-cellular extension of the cellular object \(U'\), hence a weak equivalence, and Lemma 3.2 of the previous lesson gives the claim. \(\square\)

## 4. Exercises

**4.1** (easy). Show that \(T_0(S)\) for \(S=d_2\amalg_{d_0}d_1\) is the string of two arrows, and that \(T_1(S)=S\).

**4.2** (easy). Show that the \(0\)-coskeletal reflection of a model \(X\) has the vertices of \(X\) and exactly one cell over every boundary of positive dimension.

**4.3** (medium). Show that a \(q\)-coskeletal model \(Y\) has \(\pi_r(Y,x)\) trivial for \(r>q\).

**4.4** (medium). Show that the pushout in \(\mathcal A_q\) of \(J_j\) along a \(j\)-cell is an isomorphism when \(j>q\).

## 5. Solutions

**4.1.** \(S=[\,d_1,\,d_0\,]\): a \(2\)-cell between two arrows from \(v_0\) to \(v_1\), followed by an arrow \(v_1\to v_2\). \(T_0(S)=[v(d_1),v(d_0)]\) is the string \(v_0\to v_1\to v_2\), using the lower arrow of the first slot. \(T_1(S)=[T_0(d_1),T_0(d_0)]=[d_1,d_0]=S\), since \(d_1=[d_0]\) and \(T_0([d_0])=[v(d_0)]=[d_0]\).

**4.2.** By Lemma 1.1, the reflection keeps the vertices and has one cell over each boundary in every dimension \(j\ge1\).

**4.3.** Let \(r>q\) and \(\alpha,\beta\) be \(r\)-cells with the boundary of iterated units at \(x\). They are parallel cells of dimension \(r>q\) with the same boundary, so \(\alpha=\beta\) by uniqueness of fillers. So \(\pi_r(Y,x)\) has one element.

**4.4.** By Section 1, \(J_j\) is an isomorphism in \(\mathcal A_q\) for \(j>q\), and pushouts of isomorphisms are isomorphisms.

## Sources

- [OpenAI-312] OpenAI, *The Grothendieck homotopy hypothesis via elementary expansions*, OpenAI Math Release preprint, 24 September 2026, Section 2.1–2.3. https://github.com/openai/math/tree/main/preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026
- S. Henry and E. Lanari, [*On the homotopy hypothesis for 3-groupoids*](https://tac.mta.ca/tac/volumes/39/26/39-26abs.html), Theory Appl. Categ. 39 (2023), Section 2: coskeletal and truncated globular models.
- E. Lanari, [*Towards a globular path object for weak \(\infty\)-groupoids*](https://arxiv.org/abs/1805.00156), J. Pure Appl. Algebra (2020), Proposition 3.8: contractibility of free globular sums.
