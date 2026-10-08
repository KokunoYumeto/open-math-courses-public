# Vector bundles and finitely generated projective modules

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A continuous projection chooses a vector subspace continuously at each point of a space. Its range is a vector bundle; its range on continuous functions is a projective module. Over a compact Hausdorff space, these descriptions capture every complex vector bundle and every finitely generated projective module. This lesson proves that correspondence, including all morphisms, then uses matrices to transport bundles along homotopies and to study a nontrivial line bundle on the sphere.

We assume [Idempotents, projections and their equivalences](KT-OPK-01.md) and *Point-Set Topology*. We prove the finite partition of unity needed below from the core topology course's normality and Urysohn proofs, and use the close-projection lemma. Exact statements used without proof are collected below. Freely accessible comparisons are [Hatcher 2017], [Blackadar 1998] and [Connes 1994]; the additional sources consulted are credited in the references.

Throughout, \(X\) is compact Hausdorff and \(A=C(X,\mathbb C)\). Modules are right modules, represented by columns. Hermitian inner products are conjugate-linear in the first variable and linear in the second. Bundle morphisms cover the identity unless another base map is specified. We allow the finite fibre dimension to vary between components.

## 1. Reading geometry from a matrix

A complex vector bundle \(\pi:E\to X\) consists of finite-dimensional complex vector spaces \(E_x=\pi^{-1}(x)\), with a topology locally described by fibrewise linear homeomorphisms

\[
E|_U\longrightarrow U\times\mathbb C^r.
\]

The integer \(r\) is constant on each such neighbourhood. These homeomorphisms are *local trivializations*. A continuous fibrewise linear map is a bundle morphism. In local trivializations it is multiplication by a continuous matrix. Consequently a fibrewise bijective morphism has continuous inverse: invert its local matrix. A bundle is *trivial of rank \(r\)* if it is isomorphic to \(X\times\mathbb C^r\).

A section \(s\) satisfies \(\pi(s(x))=x\). The continuous sections form an \(A\)-module \(\Gamma(E)\), with \((sf)(x)=s(x)f(x)\). The Whitney sum \(E\oplus F\) has fibre \(E_x\oplus F_x\); product trivializations give its topology. Taking the two coordinates identifies

\[
\Gamma(E\oplus F)=\Gamma(E)\oplus\Gamma(F),\qquad
\Gamma(X\times\mathbb C^r)=A^r.
\]

For \(f:Z\to X\), the *pullback* is

\[
f^*E=\{(z,e)\in Z\times E:f(z)=\pi(e)\}.
\]

A trivialization on \(U\) pulls back to one on \(f^{-1}(U)\). This is a bundle with fibre \(E_{f(z)}\). Pullback respects direct sums, and successive pullbacks agree with pullback along the composite, by the displayed fibre description and its topology.

**Lemma 1.1 (Range bundles).** If \(p:X\to M_N(\mathbb C)\) is continuous and \(p(x)^2=p(x)=p(x)^*\), then

\[
E_p=\{(x,v):p(x)v=v\}\subseteq X\times\mathbb C^N
\]

is a vector bundle. Its section module is \(pA^N\), and

\[
E_p\oplus E_{1-p}\cong X\times\mathbb C^N.
\]

*Proof.* The trace of \(p(x)\) equals its rank: a projection is the identity on its range and zero on its kernel. Thus its rank is a continuous integer-valued function and is locally constant. Fix \(x_0\) of rank \(r\), and put an orthonormal basis of its range in the columns of \(V\). The columns of \(B(x)=p(x)V\) remain independent near \(x_0\), since \(B(x)^*B(x)\) remains invertible. Shrink the neighbourhood so that the rank remains \(r\). These columns then span the range. The maps

\[
(x,a)\longmapsto(x,B(x)a),\qquad
(x,v)\longmapsto\bigl(x,(B(x)^*B(x))^{-1}B(x)^*v\bigr)
\]

are inverse continuous trivializations. Rank zero uses the empty frame.

A section is a continuous column \(s\in A^N\) with \(ps=s\), equivalent to \(s\in pA^N\). Addition maps the two range bundles to the trivial bundle, with inverse \(v\mapsto(pv,(1-p)v)\). \(\square\)

The columns \(pe_1,\ldots,pe_N\) generate \(pA^N\), even when no subset is a global basis. Moreover

\[
A^N=pA^N\oplus(1-p)A^N.
\]

A module is *projective* if maps from it lift through surjective module maps. A finitely generated module \(P\) is projective exactly when it is a direct summand of some \(A^N\). Indeed, finite generators give a surjection \(A^N\to P\); lifting the identity splits it. Conversely, a map from a summand extends to the free module by the summand projection, lifts by choosing preimages of the standard basis, and restricts back. This proves the characterization we use.

## 2. Finitely many coordinates suffice

**Lemma 2.0 (Finite partitions with closed supports).** For any finite open cover \(U_1,\ldots,U_J\) of a compact Hausdorff space \(X\), there are continuous functions \(\rho_j:X\to[0,1]\) such that \(\sum_j\rho_j=1\) and \(\operatorname{supp}\rho_j\subset U_j\).

*Proof.* The empty base is immediate. The core topology course proves [compact Hausdorff normality](https://kokunoyumeto.github.io/topology-an-inquiry-based-approach-id/reader/complete/o003-c90-ch17-exercise-guides-d.html#o003-c90-ch17-exer-c-03) and [Urysohn's lemma, including normal-space shrinking](https://kokunoyumeto.github.io/topology-an-inquiry-based-approach-id/reader/complete/o003-c90-completion-separation.html#o003-c90-thm-urysohn-bridge). These results apply without metrizability or countability assumptions.

For each \(x\in X\), choose \(j(x)\) with \(x\in U_{j(x)}\). Shrinking gives an open \(V_x\) with \(x\in V_x\) and \(\overline{V_x}\subset U_{j(x)}\). Urysohn's lemma applied to the disjoint closed sets \(\{x\}\) and \(X\setminus V_x\) gives \(f_x:X\to[0,1]\) with \(f_x(x)=1\) and \(f_x=0\) outside \(V_x\). Thus

\[
\operatorname{supp}f_x\subseteq\overline{V_x}\subset U_{j(x)}.
\]

The open sets \(\{f_x>0\}\) cover \(X\). Select a finite subcover with functions \(f_1,\ldots,f_L\), and write \(j_\ell=j(x_\ell)\). Their sum \(S=\sum_{\ell=1}^L f_\ell\) is continuous and strictly positive. Set

\[
\rho_j=S^{-1}\sum_{\{\ell:j_\ell=j\}}f_\ell.
\]

These functions are nonnegative and sum to one. Each support is contained in the finite union of the closed sets \(\operatorname{supp}f_\ell\) assigned to \(j\), which lies inside \(U_j\). This proves the stronger closed-support condition required for zero extension. \(\square\)

Choose a finite trivializing cover \(U_1,\ldots,U_J\), with fibre-coordinate maps \(\tau_j:E|_{U_j}\to\mathbb C^{r_j}\). Choose continuous functions \(\rho_j\geq0\) with

\[
\sum_j\rho_j=1,\qquad \operatorname{supp}\rho_j\subset U_j.
\]

Lemma 2.0 supplies these functions. The support condition is stronger than merely vanishing outside the chart: it makes the following zero extensions continuous. Hatcher's freely available treatment proves the metric and complement constructions [Hatcher 2017, Propositions 1.2–1.4]. We retain the explicit projection formula below and allow the rank to vary between components.

**Theorem 2.1 (Metrics and finite complements).** Every complex vector bundle over \(X\) admits a continuous Hermitian metric and is isomorphic to \(E_p\) for a projection \(p\in M_N(A)\). It has a bundle complement \(F\) with \(E\oplus F\cong X\times\mathbb C^N\).

*Proof.* For \(v,w\in E_x\), define

\[
h_x(v,w)=\sum_j\rho_j(x)\langle\tau_j(v),\tau_j(w)\rangle,
\]

interpreting a term as zero off \(U_j\). Each term is continuous by the support condition. The form is Hermitian and positive definite because some \(\rho_j(x)>0\) and \(\tau_j\) is a fibre isomorphism.

Put \(N=\sum_jr_j\) and define

\[
J_xv=\bigl(\sqrt{\rho_1(x)}\,\tau_1(v),\ldots,
\sqrt{\rho_J(x)}\,\tau_J(v)\bigr)\in\mathbb C^N,
\]

again using zero extensions. This continuous bundle map satisfies \(\|J_xv\|^2=h_x(v,v)\), so it is injective on each fibre.

On a neighbourhood with a local frame of \(E\), let \(B(x)\) have as columns the images of that frame. Its columns are independent. The projection onto their span is

\[
p(x)=B(x)(B(x)^*B(x))^{-1}B(x)^*.
\]

This formula is continuous, self-adjoint and idempotent. It is independent of the frame because it is the orthogonal projection onto \(J_xE_x\). The local formulas define \(p\in M_N(A)\). The map \(J:E\to E_p\) has continuous inverse in these frames, given by the coefficient formula in Lemma 1.1. That lemma supplies \(F=E_{1-p}\). \(\square\)

The metric is auxiliary; the bundle and its section module do not include it as structure. The theorem represents any failure of global triviality inside a larger trivial bundle. It does not say that adding only trivial summands makes a bundle trivial.

The smooth complement statement is already proved in [The Bott operator, suspension, and reduction of the index to Euclidean space, Lemma 12.5](https://kokunoyumeto.github.io/open-math-courses-public/courses/bott-and-weyl-traces/bott-suspension.html#12-embeddings-tubular-neighbourhoods-and-stable-complements). Theorem 2.1 addresses continuous bundles on arbitrary compact Hausdorff bases. The algebraic projection-module description is used in [Connections and curvature from symmetries of an algebra, §1](https://kokunoyumeto.github.io/open-math-courses-public/courses/NCG-CYCLIC/public/reader/connections-and-curvature.html#1-smooth-elements-retain-projective-modules). Here we identify its geometric meaning.

## 3. Recovering bundles and all their maps

The section functor sends \(T:E\to F\) to \(s\mapsto T\circ s\). An equivalence of categories requires more than matching isomorphism classes: every module map must arise from exactly one bundle map.

**Theorem 3.1 (Serre–Swan).** The functor

\[
\Gamma:\{\text{complex vector bundles over }X\}\longrightarrow
\{\text{finitely generated projective }A\text{-modules}\}
\]

is an equivalence of categories, with continuous bundle morphisms on the left and algebraic \(A\)-linear maps on the right.

*Proof on objects.* Theorem 2.1 and Lemma 1.1 give \(\Gamma(E)\cong pA^N\), hence finite projectivity. Conversely, express a finite projective module as a summand of \(A^N\). Its summand projection is an idempotent \(e\in M_N(A)\), so \(P\cong eA^N\). The idempotent-to-projection result from *Idempotents, projections and their equivalences* supplies \(p\) with \(eA^N\cong pA^N\); its full internal proof is [Lesson 1, Theorem 4.1](KT-OPK-01.md#4-replacing-idempotents-by-projections) [Blackadar 1998, Proposition 4.6.2]. Thus \(P\cong\Gamma(E_p)\).

*Proof on morphisms.* It suffices to use range bundles. Let

\[
\alpha:pA^m\longrightarrow qA^n
\]

be \(A\)-linear. Extend it to \(A^m\) by composing with \(p\). A map out of \(A^m\) is determined by the images of its standard basis. Put these columns in \(a\in M_{n,m}(A)\). Then

\[
a=qap,\qquad \alpha(s)=as\quad(s\in pA^m).
\]

Hence \((x,v)\mapsto(x,a(x)v)\) is a continuous map \(E_p\to E_q\) inducing \(\alpha\). No continuity assumption on \(\alpha\) is needed: its finitely many columns are continuous sections.

For uniqueness, the sections \(pe_j\) span every fibre. A bundle map is determined by its action on them. Conversely, any bundle map \(T:E_p\to E_q\) yields the continuous columns \(T_x(p(x)e_j)\); their matrix satisfies \(a=qap\) and induces \(\Gamma(T)\). This proves fullness and faithfulness. Identities and compositions agree under the constructions, proving the equivalence. \(\square\)

One can recognize a fibre without choosing matrices. Let \(I_x=\{f\in A:f(x)=0\}\), and let \(\mathbb C_x\) be \(\mathbb C\) with \(A\)-action by evaluation. Then

\[
P_x=P/PI_x\cong P\otimes_A\mathbb C_x.
\]

The isomorphism sends \([s]\) to \(s\otimes1\); its inverse sends \(s\otimes\lambda\) to \([s\lambda]\), and the balancing relation makes it well-defined.

For \(P=pA^N\), evaluation identifies this quotient with \(p(x)\mathbb C^N\). It is onto since \(pc\), for a constant column \(c\), takes the value \(p(x)c\). If \(s(x)=0\), every coordinate of \(s\) belongs to \(I_x\), and
\(s=ps=\sum_j(pe_j)s_j\) lies in \(PI_x\). This proves injectivity. Thus rank is intrinsic to the module. Transporting the range-bundle topology gives a bundle for any \(P\); the morphism proof shows that different presentations give isomorphic realizations, acting as the identity on these intrinsic fibres.

**Theorem 3.2 (Isomorphism and projection equivalence).** For projections \(p\in M_m(A)\) and \(q\in M_n(A)\), the following are equivalent:

1. \(E_p\cong E_q\).
2. \(pA^m\cong qA^n\).
3. There is \(v\in M_{n,m}(A)\) with \(v^*v=p\) and \(vv^*=q\).

The last condition is Murray–von Neumann equivalence in \(M_\infty(A)\), where stabilization adjoins zero blocks.

*Proof.* Theorem 3.1 gives the first equivalence. An isomorphism in the second condition and its inverse have matrices \(a=qap\) and \(b=pbq\), with \(ba=p\), \(ab=q\). The algebraic-equivalence-to-partial-isometry result from *Idempotents, projections and their equivalences*, proved in [Lesson 1, Theorem 4.2](KT-OPK-01.md#4-replacing-idempotents-by-projections) [Blackadar 1998, Proposition 4.6.4], gives the third condition after embedding the matrices in a common square algebra. The support identities \(v=qvp\) recover a rectangular \(n\)-by-\(m\) matrix. Conversely, such a \(v\) induces a bundle isomorphism with inverse \(v^*\), or a module isomorphism by multiplication. \(\square\)

Zero stabilization adds no nonzero fibres. Adding identity blocks instead adds trivial bundles. These are different operations: the latter can weaken the notion of bundle equivalence.

## 4. Transport along a cylinder

For a continuous \(p:X\times[0,1]\to M_N(\mathbb C)\), put \(p_t(x)=p(x,t)\).

**Lemma 4.1.** The map \(t\mapsto p_t\) is norm-continuous in \(M_N(A)\).

*Proof.* Fix \(t_0\) and \(\varepsilon>0\). The continuous function \(p(x,t)-p(x,t_0)\) vanishes on \(X\times\{t_0\}\). At each \(x\), its norm is less than \(\varepsilon\) on a product neighbourhood \(U_x\times J_x\). Finitely many \(U_x\) cover \(X\); intersecting their intervals gives a neighbourhood of \(t_0\) on which \(\sup_x\|p(x,t)-p(x,t_0)\|<\varepsilon\). \(\square\)

We use the close-projection result without repeating its proof. For projections \(P,Q\) in a unital C*-algebra with \(\|P-Q\|<1\), a unitary carrying \(P\) to \(Q\) is

\[
u(Q,P)=\bigl(QP+(1-Q)(1-P)\bigr)
\bigl(1-(P-Q)^2\bigr)^{-1/2}.
\]

This is [AF-algebras, Lemma 7.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/af-algebras.html#OA-FND-AF-06). Its formula is continuous in \(P,Q\) on this domain, by [Continuous functional calculus, Theorem 6.1(4)](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-11), and \(u(P,P)=1\).

**Theorem 4.2 (Cylinder trivialization).** For a bundle \(E\) over \(X\times[0,1]\), let \(E_0=E|_{X\times\{0\}}\). There is an isomorphism \(\operatorname{pr}_X^*E_0\to E\) equal to the identity at \(t=0\). In particular \(E_0\cong E_1\).

*Proof.* Represent \(E\) by a projection \(p(x,t)\), using Theorem 2.1 on the compact Hausdorff product. Lemma 4.1 and uniform continuity on the interval give a subdivision \(0=t_0<\cdots<t_L=1\) with \(\|p_t-p_{t_i}\|<1\) throughout each \([t_i,t_{i+1}]\).

Start with \(U_0=1\), and on that interval set

\[
U_t=u(p_t,p_{t_i})U_{t_i}.
\]

At \(t_i\), the new factor is \(1\), so the formulas join continuously. Induction gives \(U_tp_0U_t^*=p_t\). The matrix \(U(x,t)\) is jointly continuous: norm-continuity in \(t\) and continuity in \(x\) imply this by the triangle inequality. Thus

\[
(x,t,v)\longmapsto(x,t,U(x,t)v),\qquad
v\in\operatorname{ran}p(x,0),
\]

is the required isomorphism; its inverse uses \(U(x,t)^*\). Transport it back to \(E\). \(\square\)

**Corollary 4.3 (Homotopic pullbacks).** For homotopic maps \(f_0,f_1:X\to Y\) between compact Hausdorff spaces, \(f_0^*E\cong f_1^*E\) for every complex vector bundle \(E\to Y\). Every bundle over a nonempty contractible compact Hausdorff space is trivial.

*Proof.* Pull \(E\) back along the homotopy \(F:X\times[0,1]\to Y\) and apply Theorem 4.2. If \(X\) is contractible, its identity is homotopic to a constant map at some \(x_*\). Their pullbacks are \(E\) and \(X\times E_{x_*}\). \(\square\)

In particular, bundles on closed discs and cubes are trivial. No smoothness of the contraction is needed. Over the empty base there is only the empty bundle.

**Theorem 4.4 (Compact-base classifying maps).** Fix \(n\geq0\). For \(N\geq\max(n,1)\), put

\[
\begin{gathered}
G_n(\mathbb C^N)=\{p\in M_N(\mathbb C):\\
p=p^*=p^2,\ \operatorname{Tr}p=n\}.
\end{gathered}
\tag{4.1}
\]

Give each stage its matrix norm topology, include it in the next by \(p\mapsto\operatorname{diag}(p,0)\), and give the union \(G_n(\mathbb C^\infty)\) its final topology: a subset is open exactly when its intersection with each stage is open. If \(\operatorname{Vect}_n(X)\) denotes the isomorphism classes of rank-\(n\) complex bundles over a compact Hausdorff space, there is a natural bijection

\[
\begin{gathered}
{[X,G_n(\mathbb C^\infty)]}
\longrightarrow\operatorname{Vect}_n(X),\\
{[p]}\longmapsto[E_p].
\end{gathered}
\tag{4.2}
\]

Here brackets on the left mean unbased homotopy classes. Each map and each homotopy factors through a finite stage, so its range bundle is the finite-dimensional range construction of Lemma 1.1.

*Proof.* Each stage is compact Hausdorff: it is a closed bounded subset of a finite-dimensional matrix space. The inclusions are closed topological embeddings. The final union induces the original topology on each stage. Indeed, an open set in a fixed stage extends to an open set in the next stage with precisely that intersection, by the subspace topology; iterate this extension and use the prescribed intersections at earlier stages. Their compatible union is final-open. Conversely a final-open set has an open intersection with every stage by definition.

Every compact subset \(K\) of the final union is contained in a finite stage. Otherwise choose strictly increasing \(N_j\geq j\) containing all previously chosen points, and choose \(x_j\in K\) outside stage \(N_j\). The set \(S=\{x_j:j\geq1\}\) meets each fixed stage in finitely many points. Thus every subset of \(S\) meets each stage in a closed subset and is closed in the final union. In particular \(S\) is closed in \(K\), and every subset of \(S\) is closed in its subspace topology. It is therefore an infinite discrete compact space, which is impossible: its singleton cover has no finite subcover.

The image of a continuous map from \(X\), or from \(X\times[0,1]\), is compact. It lies in a finite stage and factors continuously through it because that stage has its original subspace topology. Lemma 1.1 constructs its range bundle. Theorem 4.2 makes the endpoint bundles of a homotopy isomorphic, and zero padding leaves a range bundle unchanged. Hence (4.2) is well-defined. Theorem 2.1 proves surjectivity.

For injectivity, let \(E_p\cong E_q\), with stages \(N,M\), and regard both as one bundle \(E\). Their coordinate inclusions give fibrewise injections \(j_0:E\to X\times\mathbb C^N\) and \(j_1:E\to X\times\mathbb C^M\). For \(0\leq t\leq\pi/2\), the fibre map

\[
j_t(v)=(\cos t\,j_0(v),\sin t\,j_1(v))
\tag{4.3}
\]

is injective, since at least one coefficient is nonzero. In a local frame let \(B_t\) have these images as columns. The matrix

\[
p_t=B_t(B_t^*B_t)^{-1}B_t^*
\tag{4.4}
\]

is the orthogonal range projection, independent of the frame, and continuous in \((x,t)\). It joins \(p\oplus0_M\) to \(0_N\oplus q\). A scalar coordinate permutation takes the latter to \(q\oplus0_N\). The unitary path argument in Proposition 5.1 joins that permutation to the identity; conjugation along the path completes a homotopy to the padded \(q\). Thus the maps have the same class in the union. For \(n=0\) all projections are zero and both sets are singletons, so no empty-frame inverse is needed. The empty base is immediate. Finally pullback of a projection range is the range of the pulled-back projection, proving naturality. \(\square\)

For variable rank, compactness and local constancy give finitely many clopen rank strata. Apply the theorem separately on those strata. This compact statement supplies the classifying-map treatment of [Hatcher 2017, Theorem 1.16] without importing its additional noncompact-base argument.

## 5. Gluing around a circle and across a sphere

Cutting the circle at \(1\) produces an interval. A bundle pulled back to that interval is trivial by Corollary 4.3. Its endpoint fibres are identified by an invertible matrix \(a\), giving a model

\[
([0,1]\times\mathbb C^r)/\bigl((1,v)\sim(0,av)\bigr).
\]

This model is locally trivial near the seam: use \(v\) near \(0\) and \(av\) near \(1\) as one common coordinate. The interval trivialization identifies its quotient with the original bundle, including these seam neighbourhoods.

**Proposition 5.1.** Every complex vector bundle over \(S^1\) is trivial.

*Proof.* The group \(GL_r(\mathbb C)\) is path-connected. Put \(h=(a^*a)^{1/2}\) and \(u=ah^{-1}\). Then \(u^*u=1\); invertibility gives \(uu^*=1\). The path \(u((1-s)h+s1)\) joins \(a\) to \(u\) through invertibles. A unitary has a complex eigenvector; its orthogonal complement is invariant, since its adjoint is its inverse. Induction gives an orthonormal eigenbasis, with all eigenvalues of modulus one. Choose an argument for each eigenvalue and interpolate these arguments to zero to join \(u\) to \(1\).

Choose \(b:[0,1]\to GL_r(\mathbb C)\) with \(b(0)=1\), \(b(1)=a\). The map \((t,v)\mapsto(e^{2\pi it},b(t)v)\) descends to an isomorphism to the trivial bundle, because its endpoint values agree on the prescribed equivalence; its inverse in the local seam coordinates is continuous. Rank zero is immediate. \(\square\)

For the sphere, use the Riemann-sphere coordinate \(z\in\mathbb C\cup\{\infty\}\), identified with \([1:z]\in\mathbb{CP}^1\). Give it the complex orientation. The two closed discs are \(D_0=\{|z|\leq1\}\) and \(D_\infty=\{|z|\geq1\}\cup\{\infty\}\). Parametrize their equator by \(z=e^{i\theta}\), counterclockwise in the \(z\)-plane. The infinity chart has coordinate \(w=1/z\).

For \(g:S^1\to GL_r(\mathbb C)\), identify

\[
(z,a)_0\sim(z,g(z)a)_\infty
\]

to define the clutched bundle \(E_g\). Thus \(g\) transfers the *coordinate column* from the finite disc to the infinity disc. Extend \(g\) radially into a collar of the equator. On that collar, the finite-disc column \(a_0\), or \(g(z/|z|)^{-1}a_\infty\) on the other side, is a common coordinate, proving local triviality. Away from the equator use the disc coordinates. Conversely, every bundle on \(S^2\) has this form: both disc restrictions are trivial, and their frames determine \(g\) on the equator.

**Lemma 5.2 (Winding).** A continuous \(g:S^1\to\mathbb C^\times\) has an integer \(\operatorname{wind}(g)\), additive under multiplication and invariant under homotopy. A loop extending to a nonvanishing function on a disc has winding zero; \(z\mapsto z^k\) has winding \(k\).

*Proof.* Normalize \(g\) to modulus one. Subdivide \([0,2\pi]\) into intervals on which the normalized values lie in open arcs admitting an argument. Adding multiples of \(2\pi\) at the subdivision points joins the arguments to a continuous real function \(\phi(\theta)\). Its endpoint difference is \(2\pi k\), since the endpoint values of \(g\) agree. Any two argument lifts differ by a constant multiple of \(2\pi\), so \(k\) is well-defined.

Arguments add for products. If two normalized loops are uniformly close enough that their quotient avoids \(-1\), the quotient has a single continuous argument in \((-\pi,\pi)\), with equal endpoint values. Their windings agree. Uniform continuity of a homotopy and a finite subdivision of its parameter prove homotopy invariance. A disc extension contracts radially to its centre; a constant loop has winding zero. The argument \(k\theta\) proves the last assertion. \(\square\)

**Theorem 5.3 (Distinct line bundles).** The line bundles \(L_k=E_{z^k}\), \(k\in\mathbb Z\), are pairwise non-isomorphic. \(L_0\) is trivial.

*Proof.* An isomorphism \(E_g\cong E_h\) is multiplication in the disc coordinates by nonvanishing functions \(a_0:D_0\to\mathbb C^\times\) and \(a_\infty:D_\infty\to\mathbb C^\times\). Compatibility at the seam says

\[
a_\infty(z)g(z)=h(z)a_0(z).
\]

Both \(a_0\) and \(a_\infty\), restricted to the equator parametrized by \(z\), have winding zero. Each extends over a disc, whose radial contraction gives a null-homotopy regardless of boundary parametrization. Lemma 5.2 yields \(\operatorname{wind}(g)=\operatorname{wind}(h)\). Hence \(L_k\cong L_l\) forces \(k=l\). For \(g=1\), the coordinates glue to a global trivialization. \(\square\)

We now identify one of these bundles as a projection range. The convention for the rest of the course is this single formula:

\[
\boxed{\displaystyle
q(z)=\frac{1}{1+|z|^2}
\begin{pmatrix}1&\overline z\\ z&|z|^2\end{pmatrix}
\quad(z\in\mathbb C),\qquad
q(\infty)=\begin{pmatrix}0&0\\0&1\end{pmatrix}.}
\]

With \(c(z)=(1,z)^T\), this is \(c(z)c(z)^*/(c(z)^*c(z))\). Thus \(q=q^*=q^2\) and has rank one. Its entries converge to those of \(q(\infty)\). In the chart \(w=1/z\), it is the orthogonal projection onto \((w,1)^T\), so it is continuous at infinity.

The range \(H=E_q\) is the tautological line: its fibre at \([1:z]\) is that line in \(\mathbb C^2\). Frames on the two discs are

\[
c_0(z)=(1,z)^T,\qquad c_\infty(w)=(w,1)^T.
\]

On the equator, \(c_0(z)=z\,c_\infty(1/z)\). A vector of finite-disc coefficient \(a\) therefore has infinity-disc coefficient \(za\). With our coordinate-transfer convention, \(H=L_1\), with clutching winding \(+1\). Theorem 5.3 proves its nontriviality. This winding convention is fixed separately from any definition of a first Chern number.

By Theorem 3.1, \(\Gamma(H)=qA^2\) is projective. It is not free: a finitely generated free module has a finite basis, since finitely many generators use only finitely many basis coordinates. Evaluation forces that basis to have one element, and Serre–Swan would then make \(H\) trivial. The columns of \(q\) nevertheless give two explicit generators. A finite generating set is weaker than a global basis.

The dual line bundle \(H^*\) has reciprocal transition \(z^{-1}\), so \(H\oplus H^*\) has transition \(\operatorname{diag}(z,z^{-1})\). Exercise 7.4 proves that this sum is trivial. Applying sections gives

\[
\Gamma(H)\oplus\Gamma(H^*)\cong C(S^2)^2.
\]

In this rank-two trivial module, the nonfree projective module \(\Gamma(H)\) has a nonfree complement: \(H^*=L_{-1}\) is also nontrivial by Theorem 5.3.

**Theorem 5.4 (Clutching in every sphere dimension).** For \(k\geq1\) and \(n\geq0\), clutching the two closed hemispheres along their equator induces a bijection

\[
\begin{gathered}
{[S^{k-1},GL_n(\mathbb C)]}\\
\longrightarrow\operatorname{Vect}_n(S^k),\\
{[g]}\longmapsto[E_g].
\end{gathered}
\tag{5.1}
\]

The homotopies are unbased. We take \(GL_0(\mathbb C)\) to be the one-element group. The convention is the coordinate transfer \(a_+=g(x)a_-\) on the equator.

*Proof.* Extend this transfer constantly in the transverse coordinate of an equatorial collar \(S^{k-1}\times(-\varepsilon,\varepsilon)\). The column \(a_-\), or \(g(x)^{-1}a_+\) on the other side, gives a common coordinate there. Together with the hemisphere coordinates this proves local triviality. This works also for \(k=1\), when the equator has two points.

A homotopy of transfers gives these same collar charts over \(S^k\times[0,1]\), so Theorem 4.2 identifies the endpoint bundles. Conversely, Corollary 4.3 trivializes every bundle on each closed hemisphere. The two trivializations determine its transfer \(g\), and reconstruct the bundle by the seam charts just described.

Changing a hemisphere trivialization multiplies the transfer on the corresponding side by the restriction of a map from a closed disc to \(GL_n(\mathbb C)\), or by its inverse. Contracting the disc makes that map homotopic to a constant. Proposition 5.1 joins the constant to the identity. These homotopies show that the transfer class is independent of both choices. A bundle isomorphism transports the two trivializations, so the class depends only on the isomorphism class. Clutching then recovers the original bundle, while the evident hemisphere trivializations of \(E_g\) recover \(g\). These two constructions are inverse. Rank zero is immediate. \(\square\)

**Corollary 5.5 (Products of transfers and direct sums).** For continuous \(f,g:S^{k-1}\to GL_n(\mathbb C)\),

\[
E_{fg}\oplus\underline{\mathbb C}^{\,n}
\cong E_f\oplus E_g.
\tag{5.2}
\]

In particular \(E_g\oplus E_{g^{-1}}\) is trivial of rank \(2n\).

*Proof.* The direct sum has transfer \(f\oplus g\). Set

\[
\begin{gathered}
R_t=\begin{pmatrix}
\cos t\,I_n&-\sin t\,I_n\\
\sin t\,I_n&\cos t\,I_n
\end{pmatrix},\\
0\leq t\leq\pi/2.
\end{gathered}
\tag{5.3}
\]

The invertible transfer \((f\oplus I_n)R_t(I_n\oplus g)R_t^{-1}\) starts at \(f\oplus g\) and ends at \(fg\oplus I_n\). Theorem 5.4 proves (5.2). Taking \(f=g\) and the second transfer \(g^{-1}\) makes their product the identity. The identity transfer yields a global trivialization. \(\square\)

These are the complex clutching bijection and product relation of [Hatcher 2017, Proposition 1.11 and Example 1.13]. No stable-range homotopy-group computation is needed.

## 6. The next algebraic step

Let \(V_{\mathrm{bun}}(X)\) be the commutative monoid of bundle isomorphism classes, with addition by Whitney sum and zero the zero bundle. Theorems 3.1 and 3.2 identify it with the monoid of Murray–von Neumann projection classes over \(C(X)\), with addition by block sum. This follows from the section identity in §1 and the equivalence of isomorphism classes in §3.

The Grothendieck group allows formal differences and imposes \([E\oplus F]=[E]+[F]\). Taking this construction on the two identified monoids gives

\[
K^0(X)\cong K_0(C(X)).
\]

The group formulation is [Blackadar 1998, §§1.7.1–1.7.2]. This announces the construction developed in *The Grothendieck group and \(K_0\) of a unital algebra*. *Topological K-theory of spaces, pairs and vector bundles* develops functoriality and noncompact versions. We have proved the underlying bundle–module–projection correspondence, including direct sums, before taking formal differences. Neither periodicity nor a computation of \(K^0(S^2)\) is needed to prove \(H\) nontrivial.

## 7. Exercises with solutions

**Exercise 7.1 (Basic: rank).** For a finite projective \(C(X)\)-module \(P\), define its rank at \(x\) using \(P\otimes_A\mathbb C_x\). Prove it is locally constant. Give an example where it is not constant.

*Solution.* Write \(P\cong pA^N\). The fibre calculation identifies \(P\otimes_A\mathbb C_x\) with \(p(x)\mathbb C^N\); its dimension is \(\operatorname{Tr}p(x)\). This is continuous and integer-valued, hence locally constant. The tensor-product fibre makes it independent of presentation. On \(X=\{a,b\}\), take \(p(a)=\operatorname{diag}(1,0)\) and \(p(b)=1_2\). The ranks are one and two. Compactness does not force connectedness.

**Exercise 7.2 (Basic: the Bott transition).** With the boxed projection and coordinate-transfer convention, compute the clutching function of \(H\), its winding, and the transition for \(H^*\).

*Solution.* The frames \(c_0=(1,z)^T\) and \(c_\infty=(1/z,1)^T\) satisfy \(c_0=z c_\infty\). Hence \(a_\infty=za_0\), so the clutching map is \(z\). Its argument is \(\theta\) on \(e^{i\theta}\), giving winding \(+1\). The dual frames \(\ell_0,\ell_\infty\), each taking value one on its corresponding original frame, satisfy \(\ell_0=z^{-1}\ell_\infty\). Thus the dual coordinate transfer is \(z^{-1}\), with winding \(-1\).

**Exercise 7.3 (Intermediate: a cube).** Prove directly through projections that every complex vector bundle over \([0,1]^k\) is trivial, and describe a global frame.

*Solution.* For \(k=0\) the base is a point. Otherwise represent the bundle by \(p(x)\). The projections \(P_t(x)=p(tx)\) form a norm-continuous path by Lemma 4.1. It starts with the constant projection \(p(0)\) and ends with \(p(x)\). The subdivision construction of Theorem 4.2 supplies \(U(x)\) with \(U(x)p(0)U(x)^*=p(x)\). A basis \(v_1,\ldots,v_r\) of \(\operatorname{ran}p(0)\) gives the continuous fibre bases \(U(x)v_j\). They trivialize the range bundle; the isomorphism representing the original bundle transfers the frame back.

**Exercise 7.4 (Intermediate: a trivial sum).** Prove that a loop in \(GL_2(\mathbb C)\) is null-homotopic if its determinant has winding zero. Deduce that \(H\oplus H^*\) is trivial, while \(H\) is not, and obtain the section-module identity.

*Solution.* Polar decomposition deforms the loop to a unitary loop \(u\) by the positive interpolation in Proposition 5.1. Its determinant has the same winding because the positive polar factor has positive determinant. For winding zero, Lemma 5.2 gives a continuous periodic argument \(\phi\) for \(\det u\). The loop \(d=\operatorname{diag}(\det u,1)\) contracts through \(\operatorname{diag}(e^{i(1-s)\phi},1)\). The loop \(d^{-1}u\) lies in \(SU(2)\).

Every \(SU(2)\) matrix has the form

\[
\begin{pmatrix}a&-\overline b\\b&\overline a\end{pmatrix},
\qquad |a|^2+|b|^2=1,
\]

which identifies \(SU(2)\) with \(S^3\). Its loops contract by the following elementary argument. Uniform continuity allows approximation of a loop by finitely many short great-circle arcs joining sampled points. Choose the sampling fine enough that corresponding points of the two loops have Euclidean distance less than one. Normalized straight interpolation gives a homotopy between them.

The finite union of arcs misses a point of \(S^3\): each arc lies in a real linear subspace of dimension at most two, and a finite union of proper linear subspaces cannot cover \(\mathbb R^4\). For the latter assertion, choose a nonzero linear functional vanishing on each subspace. The product of these functionals is a nonzero polynomial, so it cannot vanish on all of \(\mathbb R^4\). Stereographic projection from a missed point identifies its complement with \(\mathbb R^3\), where straight interpolation contracts the approximating loop. Thus \(d^{-1}u\), and then \(u=d(d^{-1}u)\), are null-homotopic. Any constant value can be joined to the identity by Proposition 5.1.

Apply this to \(g(z)=\operatorname{diag}(z,z^{-1})\), whose determinant is \(1\). A null-homotopy gives an extension \(G:D_0\to GL_2(\mathbb C)\) with boundary \(g\): use the homotopy on concentric circles, with its constant endpoint at the centre. In the clutched bundle use \(G(x)a_0\) as coordinate on \(D_0\) and \(a_\infty\) on \(D_\infty\). They agree because \(a_\infty=ga_0\) at the seam. This trivializes \(H\oplus H^*\). Theorem 5.3 gives nontriviality of \(H\), and taking sections gives \(\Gamma(H)\oplus\Gamma(H^*)\cong C(S^2)^2\).

**Exercise 7.5 (Advanced: \(X\times S^1\)).** Let \(E\) be a complex vector bundle over \(X\times S^1\), and set \(F=E|_{X\times\{1\}}\). Show that \(E\) is obtained by identifying the ends of \(F\times[0,1]\) with an automorphism of \(F\). Describe it and its dependence on the cylinder trivialization.

*Solution.* Pull \(E\) back along \(c(x,t)=(x,e^{2\pi it})\). Theorem 4.2 gives maps \(T_t:F\to E|_{X\times\{e^{2\pi it}\}}\), continuous in \(x,t\), with \(T_0=1_F\). Both endpoint targets are \(F\), so

\[
a=T_0^{-1}T_1=T_1:F\longrightarrow F
\]

is a bundle automorphism. Identify \((x,1,v)\sim(x,0,a_xv)\) in \(\operatorname{pr}_X^*F\). The map \((x,t,v)\mapsto T_t(v)\) descends to \(E\) since \(T_1(v)=T_0(a_xv)\).

It is a bundle isomorphism. Away from the seam this follows from \(T_t\). Near the seam choose a local frame of \(F\), using \(v\) near \(0\) and \(a_xv\) near \(1\) as quotient coordinates. In a local trivialization of \(E\), the descended map has continuous invertible matrices agreeing at the seam; matrix inversion proves its inverse continuous there too. This argument works locally around every \(x\), without a global frame of \(F\).

For another cylinder trivialization \(T'_t=T_tb_t\), with \(b_t\) a continuous path of automorphisms of \(F\), the resulting automorphism is \(a'=b_0^{-1}ab_1\). If both trivializations start at the identity, \(b_0=1\); then \(a'\) differs by right multiplication by the endpoint of a path starting at the identity. This gives an automorphism after a choice of trivialization, not a distinguished automorphism determined by \(E\). It makes no claim that \(F\) is trivial.

## What this lesson does not prove

- **Normality and Urysohn's lemma.** The exact core-course proofs are [compact Hausdorff normality, self-study exercise Q.55](https://kokunoyumeto.github.io/topology-an-inquiry-based-approach-id/reader/complete/o003-c90-ch17-exercise-guides-d.html#o003-c90-ch17-exer-c-03) and [Urysohn's lemma, Theorem U.12](https://kokunoyumeto.github.io/topology-an-inquiry-based-approach-id/reader/complete/o003-c90-completion-separation.html#o003-c90-thm-urysohn-bridge). Lemma 2.0 proves the finite closed-support partition used here from those results.
- **Projection algebra.** An idempotent over a unital C*-algebra has a projection with isomorphic range module ([Lesson 1, Theorem 4.1](KT-OPK-01.md#4-replacing-idempotents-by-projections); [Blackadar 1998, Proposition 4.6.2]). Algebraically equivalent projections admit a partial isometry ([Lesson 1, Theorem 4.2](KT-OPK-01.md#4-replacing-idempotents-by-projections); [Blackadar 1998, Proposition 4.6.4]). Projections at norm distance less than one admit the displayed continuous unitary formula [AF-algebras, Lemma 7.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/af-algebras.html#OA-FND-AF-06). These are the results used from the preceding lesson.
- **Continuous functional calculus.** For a normal element \(a\) of a unital C*-algebra and a continuous function \(f\) on its spectrum, \(f(a)\) respects products, adjoints and spectral mapping [Continuous functional calculus, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-07). For continuous \(f\) on an open set \(U\), the map \(a\mapsto f(a)\) is continuous on normal elements with spectrum in \(U\) [ibid., Theorem 6.1(4)](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-11). In particular, positive invertible elements have positive square roots and inverse square roots varying continuously. These are the exact functional-calculus facts used here.
- **Smooth complements.** The smooth result is [The Bott operator, suspension, and reduction of the index to Euclidean space, Lemma 12.5](https://kokunoyumeto.github.io/open-math-courses-public/courses/bott-and-weyl-traces/bott-suspension.html#12-embeddings-tubular-neighbourhoods-and-stable-complements), cited only to relate the two settings.
- **Later K-theory.** The group-completion formulation is [Blackadar 1998, §§1.7.1–1.7.2]. Pairs, compactly supported K-theory and Bott periodicity are developed in later lessons. The identification in §6 records the common group completion of the monoids proved equivalent here.

## References

- [Hatcher 2017] Allen Hatcher, *Vector Bundles & K-Theory*, version 2.2, November 2017, Propositions 1.2–1.4, 1.7, 1.11 and 1.18; Theorems 1.6 and 1.16; Example 1.13. [Author's free edition](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf). The matrix construction and cylinder proof here are independently written.
- [Point-Set Topology] *Topologi: Pendekatan Berbasis Inkuiri*, complete programme edition, core topology self-study supplement, [compact Hausdorff normality](https://kokunoyumeto.github.io/topology-an-inquiry-based-approach-id/reader/complete/o003-c90-ch17-exercise-guides-d.html#o003-c90-ch17-exer-c-03) and [Urysohn's lemma](https://kokunoyumeto.github.io/topology-an-inquiry-based-approach-id/reader/complete/o003-c90-completion-separation.html#o003-c90-thm-urysohn-bridge). These supplement proofs are credited as programme work, rather than as the original textbook author's solutions.
- [AF-algebras](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/af-algebras.html#OA-FND-AF-06) *AF-algebras*, Lemma 7.1, in *Foundations of von Neumann algebras*.
- [The Bott operator, suspension, and reduction of the index to Euclidean space](https://kokunoyumeto.github.io/open-math-courses-public/courses/bott-and-weyl-traces/bott-suspension.html#12-embeddings-tubular-neighbourhoods-and-stable-complements) *The Bott operator, suspension, and reduction of the index to Euclidean space*, Lemma 12.5 and Example 12.6, in *Index theory of elliptic operators*.
- [Connections and curvature from symmetries of an algebra](https://kokunoyumeto.github.io/open-math-courses-public/courses/NCG-CYCLIC/public/reader/connections-and-curvature.html#1-smooth-elements-retain-projective-modules) *Connections and curvature from symmetries of an algebra*, §1, in *Cyclic cohomology and noncommutative geometry*.
- [Continuous functional calculus](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-07) *Order, local units and quotients of C\*-algebras*, Theorems 5.1 and 6.1, in *Foundations of von Neumann algebras*.
- [Connes 1994] Alain Connes, *Noncommutative Geometry*, Academic Press, 1994, Chapter II, §1. [Author's electronic edition](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).
- [Blackadar 1998] Bruce Blackadar, *K-Theory for Operator Algebras*, second edition, MSRI Publications 5, Cambridge University Press, 1998, §§1.1, 1.7 and 4.6. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- [Roe 2017] John Roe, *Lectures on K-Theory and Operator Algebras*, Math 582, Spring 2017, Lecture 1, Propositions 1.10 and 1.12, printed/PDF pp. 5–6. [Freely readable lecture notes](https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/1/4020/files/2017/12/KTheoryNotes-1uvuwyz.pdf#page=5). This gives the finite-coordinate route to projective section modules. Lemma 2.0 and Theorems 2.1, 3.1 and 3.2 here prove the closed-support, variable-rank, converse and all-morphism details.
- [Emerson 2024] Heath Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser, 2024, §§5.1–5.2.
