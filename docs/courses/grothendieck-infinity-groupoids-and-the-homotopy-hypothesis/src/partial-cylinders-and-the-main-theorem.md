# Partial cylinders and the main theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson completes the descending induction and proves the main theorem of the course.

**Theorem 0.1 (OpenAI, 2026; Henry's pushout conjecture).** Let \(X\) be a cellular model of the coherator \(\mathcal C\), \(n\ge0\), and \(a:D_n\to X\) an \(n\)-cell. The pushout
\[
i:X\longrightarrow X^+=X\amalg_{D_n}D_{n+1}
\]
of \(J_n:D_n\to D_{n+1}\), the inclusion of the first face, along \(a\) is a weak equivalence.

The cell \(a\) may be any composite or coherence cell; the free construction of \(X^+\) creates many new cells besides the two adjoined ones, and the theorem controls all of them. The idea of the inductive step is a *partial path object*: a functor \(\mathcal P\) on \(q\)-coskeletal models with two natural endpoint morphisms \(p_0,p_1:\mathcal PY\to Y\). A cell of \(\mathcal PY\) is a cylinder in \(Y\): below dimension \(n\) it is stationary, in dimension \(n\) it is a single \((n+1)\)-cell moving one \(n\)-cell to another, and in higher dimensions it consists of cells filling the resulting shapes. Each endpoint has the right lifting property against all boundary inclusions, and the pair \((p_0,p_1)\) has it against \(J_n\). Section 4 shows that these properties prove the inductive step.

**Prerequisites.** [*Cutoffs, spines and free shapes*](cutoffs-spines-and-free-shapes.md) (Lemmas 1.1, 1.2, 3.1 and 3.2, the statements \(\mathsf E(q,n)\)), [*Trees and whiskers*](trees-and-whiskers.md) (Propositions 1.1 and 2.1), [*The homotopy calculus*](the-homotopy-calculus.md) (Proposition 3.1, Lemmas 3.2 and 4.2), [*Globular theories and their models*](globular-theories-and-their-models.md) (Proposition 3.2, Theorem 4.3, Proposition 5.1).

In Sections 1–4, \(q\ge0\) and \(0\le n<q\) are fixed, \(\mathsf E(q,j)\) is assumed for \(n<j\le q\), all constructions take place in \(\mathcal A_q\), \(F\) denotes \(F_q\), and \(D_j,\partial D_j,I_j,J_j\) denote their images in \(\mathcal A_q\). An index is *upper* if it exceeds \(n\).

## 1. The cylinder objects

We construct models \(P_0,\ldots,P_q\) forming a coglobular diagram — maps \(\sigma,\tau:P_{j-1}\to P_j\) satisfying the coglobular identities — together with two maps of coglobular diagrams \(e_0,e_1:D_\bullet\to P_\bullet\), the *endpoints*. A morphism \(P_j\to Y\) will be a cylinder on a \(j\)-cell of \(Y\), and \(e_\epsilon\) picks its two ends. For a globular set \(S\) of height at most \(q\) put
\[
P(S)=\operatorname{colim}_{(d_j\to S)}P_j ,
\]
the colimit over the category of cells of \(S\) and their faces. The endpoints induce \(e_\epsilon(S):F(S)\to P(S)\), and \(P(-)\) preserves the colimits by which globular sets are built from globes. Given \(P_0,\ldots,P_{j-1}\), put
\[
\begin{aligned}
A_j^\epsilon&=P(\partial d_j)\amalg_{\partial D_j}D_j,\\
A_j^{01}&=P(\partial d_j)\\
&\qquad\amalg_{\partial D_j\amalg\partial D_j}(D_j\amalg D_j),
\end{aligned}
\]
where \(\partial D_j\) maps to \(P(\partial d_j)\) by \(e_\epsilon(\partial d_j)\), respectively by both endpoints. A morphism \(A_j^{01}\to Y\) is the boundary of a cylinder together with both of its end cells; \(A_j^\epsilon\to Y\) prescribes only end \(\epsilon\).

*Stationary levels.* For \(j<n\) put \(P_j=D_j\) with \(e_0=e_1=\mathrm{id}\). Put \(P_n=D_{n+1}\), with \(e_0,e_1:D_n\to D_{n+1}\) the inclusions of the two faces; its coglobular maps from \(P_{n-1}=D_{n-1}\) are those of \(D_n\), so the cylinder is stationary below dimension \(n\). Then
\[
\begin{gathered}
P(\partial d_n)=\partial D_n,\qquad A_n^\epsilon=D_n,\\
A_n^{01}=\partial D_{n+1},
\end{gathered}
\]
and \(A_n^{01}\to P_n\) is \(I_{n+1}\).

*Upper levels.* For \(n<j\le q\), apply the small object argument to the set of upper \(I_k\) and the morphism \(A_j^{01}\to1\):
\[
A_j^{01}\longrightarrow P_j\longrightarrow1 ,
\]
the first map an upper \(I\)-cellular extension, the second with the right lifting property against every upper \(I_k\). The coglobular maps \(P_{j-1}\to P_j\) and the endpoints \(D_j\to P_j\) are the composites through \(A_j^{01}\); the coglobular identities hold because these maps agree on boundaries.

*Cellularity.* By induction on \(j\), \(P(\partial d_j)\) is cellular, using the skeletal filtration of \(\partial d_j\) and the maps \(P(\partial d_k)\to P_k\) for \(k<j\): for \(k<n\) this map is \(I_k\); for \(k=n\) it attaches the two end \(n\)-cells to \(\partial D_n\) and then the joining \((n+1)\)-cell; for \(k>n\) it attaches the two end \(k\)-cells and then the completion. Hence \(A_j^\epsilon\), \(A_j^{01}\) and \(P_j\) are cellular. For \(j>n\), the map \(A_j^\epsilon\to P_j\) is an upper \(I\)-cellular extension: it attaches the missing end \(j\)-cell, then the completion. For \(n\le j\le q\), \(A_j^{01}\to P_j\) is \(I\)-cellular.

## 2. Gluing along skeleta

**Lemma 2.1 (skeletal gluing).** Fix \(\epsilon\). For a finite globular set \(S\) of height at most \(q\) and \(\ell\ge0\), put
\[
C_\ell(S)=F(S)\amalg_{F(\operatorname{sk}_\ell S)}P(\operatorname{sk}_\ell S),
\]
glued by \(e_\epsilon\). For \(\ell>n\) there is a pushout square
\[
\begin{array}{ccc}
\coprod_{s\in S_\ell}A_\ell^\epsilon&\longrightarrow&C_{\ell-1}(S)\\
\big\downarrow&&\big\downarrow\\
\coprod_{s\in S_\ell}P_\ell&\longrightarrow&C_\ell(S)
\end{array}
\]
where \(S_\ell\) is the set of \(\ell\)-cells of \(S\). If \(S\) is a pasting scheme, then
\[
\begin{gathered}
C_n(S)=H_\epsilon(S),\\
C_{j-1}(d_j)=A_j^\epsilon\ \ (j>n),\\
C_{\dim S}(S)=P(S),
\end{gathered}
\]
with the whiskers oriented so that the retained copy of each \(n\)-cell is end \(\epsilon\).

**Proof.** \(\operatorname{sk}_\ell S\) is obtained from \(\operatorname{sk}_{\ell-1}S\) by attaching one globe along its boundary for each \(s\in S_\ell\), and \(F\) and \(P(-)\) preserve these colimits. A morphism \(C_\ell(S)\to T\) is a morphism \(F(S)\to T\) together with cylinder maps on the cells through level \(\ell\), compatible with faces and with end \(\epsilon\). Given these data through level \(\ell-1\), extending them at an \(\ell\)-cell \(s\) means choosing \(P_\ell\to T\) with prescribed values on \(P(\partial d_\ell)\) and on the retained end \(D_\ell\), that is, extending a map \(A_\ell^\epsilon\to T\). This is the universal property of the square; shared faces use the same maps, so no face is duplicated. Through dimension \(n-1\) the cylinders are stationary; in dimension \(n\) each cell acquires a second end and one joining cell, and higher cells keep their boundaries. This is \(C_n(S)=H_\epsilon(S)\). The other two identities follow from \(\operatorname{sk}_{j-1}d_j=\partial d_j\) and \(\operatorname{sk}_{\dim S}S=S\). \(\square\)

**Proposition 2.2 (cylinders are contractible).** Every \(P_j\) is contractible. For \(n<j\le q\), both \(A_j^\epsilon\) are contractible, and \(A_j^\epsilon\to P_j\) is an upper \(I\)-cellular weak equivalence. For every pasting scheme \(S\) of height at most \(q\), \(P(S)\) is cellular and contractible.

**Proof.** For \(j\le n\), \(P_j\) is a free globe, contractible by Proposition 2.2 of the lesson on cutoffs. Let \(j>n\), and assume the claims below \(j\). By Lemma 2.1, \(A_j^\epsilon=C_{j-1}(d_j)\) is obtained from \(C_n(d_j)=H_\epsilon(d_j)\) by pushouts of the maps \(A_\ell^\epsilon\to P_\ell\), \(n<\ell<j\), along the boundary cells, attached one at a time in increasing \(\ell\). The starting object is cellular and contractible by Proposition 2.1 of the lesson on trees. Each map pushed out is an upper \(I\)-cellular weak equivalence with cellular source, by the induction hypothesis, so each pushout is a weak equivalence by Lemma 3.2 of the lesson on cutoffs; all intermediate objects are cellular. Hence \(A_j^\epsilon\) is contractible. (For \(j=n+1\), \(A_{n+1}^\epsilon=H_\epsilon(d_{n+1})\).)

The upper extension \(A_j^\epsilon\to P_j\) is bijective on cells through dimension \(n\) (Lemma 1.2 of the lesson on cutoffs), so \(P_j\) is nonempty and has joining cells for parallel cells of dimension less than \(n\), inherited from \(A_j^\epsilon\). Since \(P_j\to1\) lifts every upper boundary inclusion, every boundary of dimension greater than \(n\) has a filler in \(P_j\). So \(P_j\) is contractible, and \(A_j^\epsilon\to P_j\), a map between contractible objects, is a weak equivalence.

For a pasting scheme \(S\) with \(\dim S\ge n\), start from \(C_n(S)=H_\epsilon(S)\) and apply the same filtration up to \(\ell=\dim S\); it ends at \(P(S)\), every step is a weak equivalence of cellular objects, and the start is contractible. If \(\dim S<n\), then \(P(S)=F(S)\), contractible by Proposition 2.2 of the lesson on cutoffs. \(\square\)

## 3. The partial path object

For \(Y\) in \(\mathcal A_q\), let \(\mathcal PY\) be the globular set with
\[
(\mathcal PY)_j=\operatorname{Hom}_{\mathcal A_q}(P_j,Y)\qquad(0\le j\le q),
\]
faces given by the coglobular maps, and exactly one cell over each boundary in dimensions above \(q\). Precomposition with \(e_\epsilon\) gives globular maps \(p_\epsilon:\mathcal PY\to Y\) through dimension \(q\), extended uniquely above. By the definition of \(P(S)\), for \(\dim S\le q\),
\[
\begin{aligned}
&\{\text{globular maps }S\to\mathcal PY\}\\
&\quad\cong\operatorname{Hom}_{\mathcal A_q}(P(S),Y).\qquad(3.1)
\end{aligned}
\]

**Proposition 3.1.** The globular set \(\mathcal PY\) carries interpretations of all operations of \(\mathcal C\) making \(\mathcal P:\mathcal A_q\to\mathcal A_q\) a functor and \(p_0,p_1\) natural morphisms of models. Each \(p_\epsilon\) has the right lifting property against every \(I_j\), and so is a weak equivalence. The morphism \((p_0,p_1):\mathcal PY\to Y\times Y\) has the right lifting property against \(J_n\).

**Proof.** *The operations.* We interpret the generating operations in the order of the defining tower, naturally in \(Y\), so that \(p_0,p_1\) preserve the operations interpreted so far (Proposition 3.2 of the first lesson). Let \(\theta:d_j\to S\) be a generating operation of output dimension \(j\). If \(j>q\), let \(\theta\) act by the unique filler of the boundary given by its faces; the endpoints preserve it by uniqueness of fillers in \(Y\). If \(j<n\), all cells involved are stationary: \(P(S)=F(S)\) and \(P_j=D_j\), and \(\theta\) acts as in \(Y\).

Let \(n\le j\le q\); then \(\dim S\le j\le q\), so (3.1) applies. The operation \(\theta\) is a morphism of free models \(D_j\to F(S)\), and the required ends of its action on cylinders are the morphisms \(e_\epsilon(S)\theta:D_j\to P(S)\). Its two faces are operations of the earlier theory, already interpreted on \(\mathcal PY\); by (3.1) and the Yoneda lemma, their actions \(\operatorname{Hom}(P(S),Y)\to\operatorname{Hom}(P_{j-1},Y)\), natural in \(Y\), are represented by morphisms \(P_{j-1}\to P(S)\). They agree on common faces, because the two faces of \(\theta\) are parallel, and so define \(b_\theta:P(\partial d_j)\to P(S)\). Compatibility of the endpoints with the earlier operations says that \(b_\theta\) restricted along \(e_\epsilon(\partial d_j)\) equals \(e_\epsilon(S)\theta\) restricted to \(\partial D_j\). So \(b_\theta\) and the two ends glue to a morphism \(A_j^{01}\to P(S)\). As \(A_j^{01}\to P_j\) is \(I\)-cellular and \(P(S)\) is contractible (Proposition 2.2), so that \(P(S)\to1\) has the right lifting property against all \(I_k\) (Lemma 4.2 of the lesson on the homotopy calculus), this morphism extends to \(P_j\to P(S)\). Choose such an extension once, independently of \(Y\); precomposition with it is the action of \(\theta\) on \(\mathcal PY\). Its faces and ends are the prescribed ones by construction. Because all choices are made on the representing objects, postcomposition with a morphism \(Y\to Z\) preserves every operation, so \(\mathcal P\) is a functor, and \(p_0,p_1\) are natural morphisms of models. The globular set is unchanged, so \(\mathcal PY\) is \(q\)-coskeletal.

*Each endpoint.* An \(I_j\)-lifting problem against \(p_\epsilon\), for \(j\le q\), is a boundary of a cylinder together with a cell of \(Y\) at end \(\epsilon\), that is, a morphism \(A_j^\epsilon\to Y\); a solution is an extension to \(P_j\to Y\). For \(j<n\), \(A_j^\epsilon\to P_j\) is the identity. For \(j=n\) it is a face inclusion \(D_n\to D_{n+1}\), which has a retraction by a unit. For \(j>n\) it is an upper \(I\)-cellular weak equivalence with cellular source (Proposition 2.2) and has a retraction by Lemma 3.2 of the lesson on cutoffs. Composing with the retractions solves the problem. For \(j>q\), \(I_j\) is an isomorphism in \(\mathcal A_q\). So \(p_\epsilon\) has the right lifting property against all \(I_j\), and \(p_\epsilon\in\mathcal W\) by Lemma 4.2 of the lesson on the homotopy calculus.

*Both endpoints.* A \(J_n\)-lifting problem against \((p_0,p_1)\) is a cylinder \(h:P_n\to Y\) together with \((n+1)\)-cells \(a_0,a_1\) of \(Y\) starting at its two ends; it is a morphism from
\[
B=P_n\amalg_{D_n\amalg D_n}(D_{n+1}\amalg D_{n+1}).
\]
As \(P_n=D_{n+1}\), \(B\) is the free model on a tree diagram at depth \(n\): four \(n\)-cells \(x_0,x_1,y_0,y_1\) with a common boundary and three \((n+1)\)-cells \(h:x_0\to x_1\), \(a_0:x_0\to y_0\), \(a_1:x_1\to y_1\), forming the tree \(y_0-x_0-x_1-y_1\). So \(B\) is cellular and contractible by Proposition 1.1 of the lesson on trees. Attaching one \((n+1)\)-cell \(y_0\to y_1\), the cylinder on the target face, gives exactly \(A^{01}_{n+1}\), so the natural map \(B\to P_{n+1}\) factors as an \(I_{n+1}\)-attachment followed by the completion \(A^{01}_{n+1}\to P_{n+1}\). It is an upper \(I\)-cellular map between cellular contractible objects, hence a weak equivalence with a retraction \(P_{n+1}\to B\) (Lemma 3.2 of the lesson on cutoffs). Composing the retraction with the given \(B\to Y\) is a cylinder \(P_{n+1}\to Y\) solving the lifting problem; its source is \(h\) and its ends are \(a_0,a_1\) because it restricts to the given map on \(B\). For \(q=n+1\) the added cell is an attachment of \(I_q\), and the same argument applies. \(\square\)

## 4. The inductive step

**Proposition 4.1.** Under the standing hypotheses, \(\mathsf E(q,n)\) holds. Consequently \(\mathsf E(q,n)\) holds for all \(0\le n\le q\).

**Proof.** Let \(X\) be cellular in \(\mathcal A_q\), \(a:D_n\to X\), and \(i:X\to Y=X\amalg_{D_n}D_{n+1}\). The unit on \(a\) gives a retraction \(r:Y\to X\) with \(ri=\mathrm{id}_X\). Since \(p_0:\mathcal PX\to X\) has the right lifting property against all \(I_j\) and \(X\) is cellular, there is \(h:X\to\mathcal PX\) with \(p_0h=\mathrm{id}_X\). Put
\[
u=p_1h:X\to X,\quad\bar u=ur:Y\to X .
\]
As \(p_0,p_1\in\mathcal W\), two-out-of-three gives \(h\in\mathcal W\) and \(u\in\mathcal W\); also \(\bar ui=u\).

The square with top \(\mathcal P(i)h:X\to\mathcal PY\), left \(i\), right \((p_0,p_1):\mathcal PY\to Y\times Y\) and bottom \((\mathrm{id}_Y,i\bar u):Y\to Y\times Y\) commutes:
\[
\begin{aligned}
(p_0,p_1)\,\mathcal P(i)\,h&=(ip_0h,\,ip_1h)\\
&=(i,\,iu)\\
&=(\mathrm{id}_Y,\,i\bar u)\,i .
\end{aligned}
\]
The right map has the right lifting property against \(J_n\), hence against its pushout \(i\): restrict the top map along \(a\) and the bottom map along the new cell \(D_{n+1}\to Y\), solve the resulting \(J_n\)-square, and glue by the universal property of the pushout. This gives \(f:Y\to\mathcal PY\) with \(p_0f=\mathrm{id}_Y\) and \(p_1f=i\bar u\). Two-out-of-three gives \(f\in\mathcal W\), and then \(v=i\bar u=iur\in\mathcal W\).

Finally \(iu:X\to Y\) is a retract of \(v:Y\to Y\) in the category of arrows: the maps of arrows \((i,\mathrm{id}_Y):iu\to v\) and \((r,\mathrm{id}_Y):v\to iu\) commute with the arrows because \(vi=iuri=iu\) and \(iur=v\), and they compose to the identity because \(ri=\mathrm{id}_X\). By retract closure \(iu\in\mathcal W\), and two-out-of-three with \(u\in\mathcal W\) gives \(i\in\mathcal W\).

With the top case \(\mathsf E(q,q)\) (Lemma 3.1 of the lesson on cutoffs), descending induction on \(n\) proves \(\mathsf E(q,n)\) for all \(n\le q\). \(\square\)

The argument places no condition on the cell \(a\), and all maps are morphisms of models, so the conclusion includes all cells that the free construction of \(Y\) creates.

## 5. The main theorem

**Proof of Theorem 0.1.** Let \(i:X\to X^+\) be as in the theorem, in \(\mathcal A\). We check Proposition 3.1(3) of the lesson on the homotopy calculus in a fixed dimension \(k\). Choose \(q\ge\max(n+1,k+1)\). The reflector \(R_q\) preserves colimits, so \(R_qX\) is cellular in \(\mathcal A_q\) and \(R_q(i)\) is the pushout of \(J_n\) along \(R_q(a)\); by Proposition 4.1 it is a weak equivalence. The units \(X\to R_qX\) and \(X^+\to R_qX^+\) are bijective on cells of dimension at most \(q\) (Lemma 1.1 of the lesson on cutoffs). The data of the test in dimension \(k\) — a boundary in \(X\) and a \(k\)-cell of \(X^+\) — and the witnesses that the test provides for \(R_q(i)\) — a \(k\)-cell and a \((k+1)\)-cell — all lie in dimensions at most \(q\). So they correspond to cells of \(X\) and \(X^+\) with the same faces, and these are witnesses for \(i\). As \(k\) is arbitrary, \(i\in\mathcal W\). \(\square\)

## 6. Exercises

**6.1** (easy). Show that for \(n=0\) the expansion of Theorem 0.1 adjoins a new vertex \(a'\) and an arrow \(a\to a'\), and that its retraction sends \(a'\) to \(a\).

**6.2** (medium). Show that a transfinite composite of pushouts of coproducts of the maps \(J_n\), \(n\ge0\), starting from a cellular model, is a weak equivalence.

**6.3** (medium). In the proof of Proposition 4.1, verify that \((i,\mathrm{id}_Y)\) and \((r,\mathrm{id}_Y)\) are maps of arrows \(iu\to v\) and \(v\to iu\).

**6.4** (medium). Show that the endpoint morphism \(p_0:\mathcal PY\to Y\) has a section for every cellular \(Y\) in \(\mathcal A_q\).

## 7. Solutions

**6.1.** \(D_0\to D_1\) includes the free vertex as the first vertex of the free arrow. Its pushout along \(a\) adjoins the target vertex \(a'\) and the arrow \(a\to a'\), together with all cells that the operations create. The retraction \(D_1\to D_0\) sends the arrow to the unit \(e(x)\), hence \(a'\) to \(a\).

**6.2.** Each pushout of a coproduct is a transfinite composite of single pushouts of some \(J_n\) along cells; every intermediate object is cellular, since \(J_n\) is a composite of two boundary attachments. Each single pushout is a weak equivalence by Theorem 0.1, and Lemma 3.2 of the lesson on the homotopy calculus handles transfinite composites.

**6.3.** A map of arrows from \(iu:X\to Y\) to \(v:Y\to Y\) given by \((i,\mathrm{id}_Y)\) requires \(\mathrm{id}_Y\circ iu=v\circ i\); indeed \(vi=iuri=iu\). A map \((r,\mathrm{id}_Y)\) from \(v\) to \(iu\) requires \(\mathrm{id}_Y\circ v=iu\circ r\), which is the definition \(v=iur\). The composite \((ri,\mathrm{id}_Y)=(\mathrm{id}_X,\mathrm{id}_Y)\).

**6.4.** The morphism \(\varnothing\to Y\) is \(I\)-cellular and \(p_0\) has the right lifting property against all \(I_j\), hence against \(\varnothing\to Y\) (lifting passes to cellular extensions). Lifting the square with \(\mathrm{id}_Y\) at the bottom gives a section.

## Sources

- [OpenAI-312] OpenAI, *The Grothendieck homotopy hypothesis via elementary expansions*, OpenAI Math Release preprint, 24 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026
- E. Lanari, [*Towards a globular path object for weak \(\infty\)-groupoids*](https://arxiv.org/abs/1805.00156), J. Pure Appl. Algebra (2020), Definitions 5.2, 5.3 and 6.1: cylinder objects representing path cells.
- S. Henry, [*Algebraic models of homotopy types and the homotopy hypothesis*](https://arxiv.org/abs/1609.04622) (2016), Conjecture 5.3.3: the pushout conjecture.
