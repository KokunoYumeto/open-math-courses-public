# Vector bundles and their constructions

*Public domain (CC0).*

A family of vector spaces can look like a product near each point without admitting one choice of coordinates everywhere. The failure to choose global coordinates is what characteristic classes will measure. We first establish the constructions that allow us to compare such families: sections, pullbacks, complements and stabilization.

This lesson assumes finite-dimensional real and complex linear algebra, continuous maps, and the definitions of compactness, Hausdorffness and local finiteness. The topological facts about partitions of unity needed below are proved here. The final geometric examples also use smooth coordinate charts and the chain rule. Hatcher's *Vector Bundles and K-Theory* [H], Sections 1.1–1.2, treats sections, pullbacks, metrics and complements; Proposition 1.4 proves compact-base stabilization. The proofs below include the locally finite partition construction and the real and complex cases.

## 1. Local coordinates and global sections

Let \(\mathbb F\) be \(\mathbb R\) or \(\mathbb C\). A **rank \(r\) vector bundle** over a space \(B\) is a map \(\pi:E\to B\), a vector-space structure on every fibre \(E_b=\pi^{-1}(b)\), and local homeomorphisms

\[
\phi_U:E|_U\longrightarrow U\times\mathbb F^r
\]

over \(U\), linear on fibres. Rank may instead be locally constant; every assertion then applies separately on the subsets of each rank. A bundle map over \(f:B\to C\) is a continuous map \(E\to F\) carrying \(E_b\) linearly into \(F_{f(b)}\). We distinguish a general bundle map from a fibrewise isomorphism.

On an overlap, coordinate changes have the form

\[
(b,v)\longmapsto (b,g_{UV}(b)v),\qquad
g_{UV}:U\cap V\longrightarrow\mathrm{GL}_r(\mathbb F).
\]

Continuity follows by evaluating the coordinate change on each coordinate vector. Conversely, continuous matrices satisfying \(g_{UW}=g_{UV}g_{VW}\) glue the local products into a bundle. To see the topology explicitly, declare a subset open when its inverse image in each local product is open. The cocycle identity makes the identifications consistent; the continuous invertible changes identify each local product with an open part of the glued space.

A section is a continuous map \(s:B\to E\) with \(\pi s=\mathrm{id}\). The zero section, fibrewise addition and scalar multiplication are continuous because they are continuous in every local coordinate system. Write \(\varepsilon^r=B\times\mathbb F^r\) for the trivial bundle.

**Lemma 1.1 (continuous inverse).** A fibrewise isomorphism of equal-rank bundles over the same base is a bundle isomorphism.

**Proof.** In local coordinates it is multiplication by a continuous matrix \(A(b)\) with nonzero determinant. The formula
\(A^{-1}=\operatorname{adj}(A)/\det A\) proves continuity of its inverse. To verify this formula, each entry of the adjugate is a signed minor and hence a polynomial in the entries of \(A\). Cofactor expansion gives \(A\operatorname{adj}(A)=(\det A)I\): the diagonal entries are determinant expansions, while each off-diagonal entry is the determinant of a matrix with two equal rows and is zero. The column expansion gives \(\operatorname{adj}(A)A=(\det A)I\) as well. These identities hold over both stated fields. These local inverses agree, so they form the global continuous inverse. The same argument proves smoothness of the inverse for smooth bundles. \(\square\)

**Theorem 1.2 (frame criterion).** A rank \(r\) bundle is trivial if and only if it has sections \(s_1,\ldots,s_r\) forming a basis of each fibre.

**Proof.** A trivialization gives the sections corresponding to the coordinate vectors. Conversely, the map
\((b,t_1,\ldots,t_r)\mapsto\sum_i t_i s_i(b)\)
is continuous and a linear isomorphism on every fibre. Lemma 1.1 gives a trivialization. \(\square\)

The criterion makes nontriviality visible without cohomology. The tautological real line bundle \(\gamma\) on \(\mathbb{RP}^n\) has fibre the line represented by the base point. Its total space is
\(\{(\ell,v):v\in\ell\}\subset\mathbb{RP}^n\times\mathbb R^{n+1}\).
On the open set where coordinate \(i\) of the line is nonzero, choose its representative with coordinate \(i\) equal to one. This is a continuous nonzero local frame and proves local triviality.

**Proposition 1.3.** For \(n\geq1\), this tautological line bundle is nontrivial.

**Proof.** If a nowhere-zero section existed, its pullback along \(q:S^n\to\mathbb{RP}^n\) would have the form \(s(q(x))=t(x)x\). Here \(t(x)=\langle s(q(x)),x\rangle\) is continuous and \(t(-x)=-t(x)\). A path in \(S^n\) from \(x\) to \(-x\) and the intermediate value theorem give a zero of \(t\), a contradiction. A trivial line bundle would have a nowhere-zero section by Theorem 1.2. \(\square\)

For \(n=1\), writing the line as \(\mathbb R(\cos\theta,\sin\theta)\), with \(0\leq\theta\leq\pi\), identifies the total space with

\[
([0,\pi]\times\mathbb R)/((0,t)\sim(\pi,-t)).
\]

This is the Möbius line bundle. The sign at the seam prevents a nonzero section from closing up.

## 2. The partition of unity we will use

A family of sets is locally finite if every point has a neighbourhood meeting only finitely many members. A Hausdorff space is **paracompact** if every open cover has a locally finite open refinement. From now on, topological bases requiring a metric or a complement are paracompact Hausdorff. The first section did not require those assumptions.

**Lemma 2.1.** A paracompact Hausdorff space is regular and normal.

**Proof.** First fix \(x\) and an open neighbourhood \(O\). For each \(y\notin O\), Hausdorffness gives disjoint open sets \(U_y\ni x\) and \(V_y\ni y\). Take a locally finite open refinement \(\{W_a\}\) of the cover consisting of \(O\) and all \(V_y\). Let \(C\) be the union of the closures of the \(W_a\) meeting \(B\setminus O\). Each such \(W_a\) lies in a \(V_y\), since it cannot lie in \(O\). Thus its closure does not contain \(x\). The closures of a locally finite family are locally finite: shrink a neighbourhood witnessing local finiteness, and any open set missing that neighbourhood has closure missing its smaller interior neighbourhood. A locally finite union of closed sets is closed, as can be checked in a neighbourhood meeting only finitely many. Consequently \(C\) is closed and misses \(x\). The union \(W\) of the selected open sets contains \(B\setminus O\) and lies in \(C\). The neighbourhood \(B\setminus C\) of \(x\) has closure contained in \(B\setminus W\subset O\). This proves regularity.

To prove normality, let \(A\subset O\), with \(A\) closed and \(O\) open. Regularity gives for each \(x\in A\) an open \(U_x\) with \(x\in U_x\subset\overline U_x\subset O\). Refine the cover \(\{U_x:x\in A\}\cup\{B\setminus A\}\) locally finitely. Let \(V\) be the union of refinement members meeting \(A\). Each is contained in some \(U_x\). Local finiteness gives \(\overline V\subset\bigcup\overline W_a\subset O\). Hence \(A\subset V\subset\overline V\subset O\). For disjoint closed sets \(A\) and \(C\), apply this to \(O=B\setminus C\); then \(V\) and \(B\setminus\overline V\) separate them. \(\square\)

**Lemma 2.2 (continuous separator).** In a normal space, if \(A\) is closed and \(A\subset O\) with \(O\) open, there is a continuous \(f:B\to[0,1]\) equal to one on \(A\) and zero outside \(O\).

**Proof.** The neighbourhood conclusion in Lemma 2.1 uses only normality once it is available: separate a closed set from the closed complement of its prescribed open neighbourhood. Choose open sets \(U_t\), indexed by dyadic rational numbers \(t\in[0,1]\), with \(A\subset U_0\), \(U_1=O\), and \(\overline U_s\subset U_t\) for \(s<t\). Start with \(U_0\) whose closure lies in \(O\); insert the intermediate dyadics one finite level at a time by the neighbourhood conclusion. Define
\(g(x)=\inf\{t:x\in U_t\}\), taking the infimum to be one for an empty set. Then
\(\{g<a\}=\bigcup_{t<a}U_t\).
Also \(\{g>a\}=\bigcup_{t>a}(B\setminus\overline U_t)\): membership on the right forces \(g\geq t>a\); if \(g>a\), choose dyadics \(a<t<s<g\), so \(x\notin U_s\) and therefore \(x\notin\overline U_t\). Both sets are open. Thus \(g\) is continuous, zero on \(A\), and one outside \(O\). Take \(f=1-g\). \(\square\)

**Theorem 2.3 (subordinate partition).** For every open cover of a paracompact Hausdorff space, there is a locally finite family of continuous functions \(\rho_a:B\to[0,1]\) with \(\sum_a\rho_a=1\) and each support contained in a member of the cover.

**Proof.** By regularity, choose an open cover \(\{V_x\}\) such that each \(\overline V_x\) lies in a member of the original cover. Take a locally finite refinement \(\{W_a\}\), assigning \(W_a\) to some \(V_x\). Its closure still lies in the assigned original member. Apply the same procedure to \(\{W_a\}\), obtaining a locally finite cover \(\{Z_b\}\), with \(\overline Z_b\subset W_{a(b)}\). For each \(a\), put
\(F_a=\bigcup_{a(b)=a}\overline Z_b\).
The family of closures is locally finite, so \(F_a\) is closed, \(F_a\subset W_a\), and the \(F_a\) cover \(B\). Lemma 2.2 gives \(f_a=1\) on \(F_a\) and \(f_a=0\) outside \(W_a\). The supports are contained in \(\overline W_a\), a locally finite family. Thus \(f=\sum_a f_a\) is continuous and positive. Set \(\rho_a=f_a/f\). The functions have the claimed properties. \(\square\)

This proof matters for bundles: extension by zero of a local construction multiplied by \(\rho_a\) is continuous because its support stays inside the chart where it was defined. Local finiteness turns an apparently infinite sum into a finite sum near every point.

## 3. Pulling back and combining fibres

Given \(f:C\to B\), define

\[
f^*E=\{(c,v)\in C\times E:f(c)=\pi(v)\}.
\]

Its fibre at \(c\) is \(E_{f(c)}\). Pulling back a chart on \(U\) gives a chart on \(f^{-1}U\), so it is a bundle. The maps
\((d,(c,v))\mapsto(d,v)\) when \(c=g(d)\) give canonical isomorphisms \(g^*f^*E\cong(fg)^*E\); the identity pullback is canonically \(E\). Restriction to a subset is the pullback along its inclusion. A fibrewise isomorphism over \(f\) identifies its domain with \(f^*E\) by sending \(v\) to \((\pi(v),F(v))\), and Lemma 1.1 proves this is an isomorphism.

For bundles \(E,F\) over \(B\), their Whitney sum \(E\oplus F\) has fibre \(E_b\oplus F_b\). Local products with transition matrices \(\operatorname{diag}(g,h)\) prove local triviality. The analogous transition matrices are

\[
g\otimes h\quad\text{for }E\otimes F,\qquad
(g^{-1})^{\mathsf T}\quad\text{for }E^*,\qquad
T\longmapsto hTg^{-1}\quad\text{for }\operatorname{Hom}(E,F).
\]

Every formula is continuous and satisfies the cocycle identity. Exterior powers use \(\Lambda^k g\); their entries are minors of \(g\). In particular, \(\det E=\Lambda^rE\) is a line bundle. These operations commute with pullback, since the fibre identifications and transition matrices on both sides are identical.

More generally, any construction on finite-dimensional vector spaces whose induced maps on invertible matrices are continuous and preserve compositions gives a bundle construction by this gluing procedure. To check independence of charts, insert the old-to-new coordinate matrix into the same construction; functoriality supplies the compatible change of coordinates. This proves the assertion, rather than assuming that a disjoint union of fibres already has a suitable topology.

## 4. Metrics, projections and complements

A metric is a continuous positive-definite symmetric bilinear form on each real fibre, or a Hermitian form on each complex fibre. For complex fibres we take the inner product conjugate-linear in its first variable.

The finite-dimensional preparation is available in the programme's B40 source [B40]: basis uniqueness, Gram–Schmidt with its full induction in the solved exercise, and the real orthogonal-projection formula. Its accompanying lessons [B40-B] and [B40-H] give full proofs of basis extension over any field and orthogonal decomposition over both fields. The latter uses an inner product linear in the first variable; exchanging its two arguments gives our convention. Orthogonality and the projection map are unchanged. The calculation below supplies the positive-Gram argument and the metric-weighted formula over both fields.

**Theorem 4.1.** Every finite-rank vector bundle over a paracompact Hausdorff base has a metric.

**Proof.** Take a partition subordinate to trivializing charts. On each chart let \(h_a\) be the coordinate Euclidean or Hermitian metric and set
\(h(v,w)=\sum_a\rho_a(b)h_a(v,w)\)
for \(v,w\in E_b\), interpreting each summand as zero outside its chart. Support containment proves continuity there, and local finiteness proves continuity of the sum. For \(v\ne0\), some \(\rho_a(b)>0\), so the corresponding summand is positive and every other summand nonnegative. Thus \(h\) is positive definite. \(\square\)

**Theorem 4.2 (complement and splitting).** Let \(S\subset E\) be a rank \(k\) subbundle and give \(E\) a metric. Its orthogonal complement \(S^\perp\) is a rank \(r-k\) subbundle and addition gives \(S\oplus S^\perp\cong E\).

**Proof.** On an open set where \(S\) has a frame, write its columns in a frame of \(E\) as a matrix \(A(b)\) and write the metric matrix as \(H(b)\). The Gram matrix \(A^*HA\) is invertible. Indeed, for \(z\ne0\), the frame columns give \(Az\ne0\), and positive definiteness gives \(z^*A^*HAz=(Az)^*H(Az)>0\). Its kernel is therefore zero, which proves invertibility in finite dimension. The projection onto \(S\) is

\[
P=A(A^*HA)^{-1}A^*H.
\]

This is continuous, has image \(S_b\), satisfies \(P^2=P\), and has kernel \(S_b^\perp\). For \(G=A^*HA\), multiplication gives \(PA=A\) and \(P^2=AG^{-1}GG^{-1}A^*H=P\). Since \(A\) is injective and \(G\) invertible, \(Pv=0\) is equivalent to \(A^*Hv=0\); this is precisely orthogonality to every frame column. At a fixed point \(b_0\), choose a basis \(z_1,\ldots,z_{r-k}\) of that kernel in the ambient coordinates. The vectors \((I-P(b))z_j\) remain independent near \(b_0\), since a nonzero minor at \(b_0\) stays nonzero. They form a local frame of the kernel. Hence \(S^\perp\) is a bundle. Addition is a fibrewise isomorphism; Lemma 1.1 proves the splitting. \(\square\)

This argument also proves that the image and kernel of a continuous bundle map of constant rank are subbundles. A nonzero rank minor stays nonzero near a point. Its columns frame the image there, and solving the corresponding pivot equations gives a frame of the kernel. Without constant rank, the assertion fails: multiplication by \(x\) on the trivial line over \(\mathbb R\) has a one-dimensional kernel at zero and a zero-dimensional kernel elsewhere.

If \(0\to S\to E\to Q\to0\) is an exact sequence of finite-rank bundles, the map \(S^\perp\to Q\) is a fibrewise isomorphism, so \(E\cong S\oplus Q\). The splitting depends on a metric; the existence statement does not choose a canonical splitting.

## 5. Stabilization and geometric examples

**Theorem 5.1 (finite ambient bundle).** Every rank \(r\) bundle on a compact Hausdorff base embeds as a subbundle of \(\varepsilon^N\) for some finite \(N\), and has a complementary bundle \(F\) with \(E\oplus F\cong\varepsilon^N\).

**Proof.** A compact Hausdorff space is paracompact: every open cover has a finite subcover, which is a locally finite refinement. Use Theorem 2.3 for a finite trivializing cover, retaining a finite partition by summing all functions assigned to each member. In each chart let \(\phi_a(v)\in\mathbb F^r\) be the fibre coordinate. Define

\[
J(v)=(\rho_1(b)\phi_1(v),\ldots,\rho_m(b)\phi_m(v))
\in\mathbb F^{mr}.
\]

The extension of each component by zero is continuous. For \(v\ne0\), a chart with \(\rho_a(b)>0\) gives a nonzero component, so \(J_b\) is injective. Its rank is constantly \(r\); the constant-rank argument following Theorem 4.2 makes its image a subbundle. Lemma 1.1 identifies \(E\) with its image. Take the orthogonal complement in the trivial bundle and apply Theorem 4.2. \(\square\)

For a smooth \(n\)-manifold \(M\), a chart identifies a tangent vector with its \(n\) velocity coordinates. Chart changes act by the Jacobian, and the chain rule gives the cocycle identity. This constructs the smooth rank \(n\) bundle \(TM\) directly from the smooth atlas.

For an immersion \(f:M\to N\), \(df:TM\to f^*TN\) is an injective bundle map. Give \(N\) a smooth Riemannian metric. The smooth version of the projection proof gives the normal bundle \(\nu_f\) and

\[
f^*TN\cong TM\oplus\nu_f.
\]

For an embedding this is the restriction \(TN|_M\). This assertion only needs the already specified smooth metric; the continuous metric existence proof did not itself assert smoothness.

Here is the smooth existence argument. A second-countable smooth manifold has a countable cover by coordinate balls with compact closures: each point has such a ball, and second countability gives a countable subcover by choosing one covering ball for each basic open set contained in a covering ball. These closures yield a compact exhaustion \(K_n\), which can be chosen with \(K_n\subset\operatorname{int}K_{n+1}\). Indeed, start with a finite union of the first closures; at each step include the next closure and finitely many precompact coordinate balls covering the preceding compact set. Their closures form the next compact set, with the required interior containment.

For each compact shell \(K_n\setminus\operatorname{int}K_{n-1}\), choose finitely many coordinate balls whose closures lie in \(\operatorname{int}K_{n+1}\setminus K_{n-2}\) and in prescribed trivializing charts, and choose smaller concentric balls covering that shell. Take \(K_{-1}=K_0=\varnothing\) at the initial stages, shifting the exhaustion indices if necessary. The larger balls support smooth functions positive on the smaller balls. An explicit function on a coordinate ball of radius \(R\) is \(\exp(-1/(R^2-|x|^2))\) inside and zero outside. Every derivative tends to zero at the boundary, since an exponential decay dominates each inverse power of \(R^2-|x|^2\), so extension by zero is smooth. The shell construction makes the entire family locally finite: a neighbourhood inside \(\operatorname{int}K_m\) misses the supports from shells \(n\geq m+2\). The sum is positive everywhere, and dividing each function by that sum gives a smooth subordinate partition. Summing the chart metrics with this partition produces a smooth metric by the same positivity proof as Theorem 4.1.

On the unit sphere, \(T_xS^n=x^\perp\) and the normal line has global section \(x\). Thus

\[
TS^n\oplus\varepsilon^1\cong\varepsilon^{n+1},\qquad
(v,t)\longmapsto v+tx.
\]

Stable triviality does not say that \(TS^n\) is trivial. For odd \(n=2m-1\), identify \(\mathbb R^{2m}\) with \(\mathbb C^m\); the vector \(ix\) is tangent and never zero. This provides one section, not an entire frame in general.

For a product, the differential of its two projections gives
\(T(M\times N)\cong\operatorname{pr}_M^*TM\oplus\operatorname{pr}_N^*TN\).
In product coordinates this is precisely the decomposition of velocity coordinates. Its inverse combines those coordinates, so it is a bundle isomorphism.

## 6. Exercises with solutions

**Exercise 6.1 (easy).** Let \(L\) be the Möbius line bundle. Give an explicit nonzero section of \(L\otimes L\). Does this trivialize \(L\)?

**Solution.** In the interval description let \(e_\theta=(\cos\theta,\sin\theta)\) be the local frame. The tensor \(e_\theta\otimes e_\theta\) has identical values at the seam because both factors change sign. It descends to a nowhere-zero section and trivializes \(L\otimes L\). It does not supply a section of \(L\); Proposition 1.3 proves that \(L\) remains nontrivial.

**Exercise 6.2 (medium).** Suppose \(s_1,\ldots,s_k\) are independent sections of a metric rank \(r\) bundle. Construct the trivial rank \(k\) summand and the projection onto it.

**Solution.** The map \(A:\varepsilon^k\to E\) with columns \(s_i\) is fibrewise injective of constant rank, so its image is a subbundle isomorphic to \(\varepsilon^k\). Its orthogonal projection in ambient local coordinates is \(A(A^*HA)^{-1}A^*H\). The formula agrees on chart overlaps because it is characterized by image equal to the span of the sections and orthogonal kernel. The complement theorem gives \(E\cong\varepsilon^k\oplus F\).

**Exercise 6.3 (medium).** A metric makes \(E\) isomorphic to \(E^*\) when \(E\) is real. What changes over \(\mathbb C\)?

**Solution.** In the real case \(v\mapsto(w\mapsto h(v,w))\) is a continuous fibrewise linear isomorphism. In the complex convention fixed above, the same map is conjugate-linear in \(v\), so it defines a linear isomorphism \(\overline E\cong E^*\), where scalar multiplication in \(\overline E\) is conjugated. Its inverse is continuous by Lemma 1.1. Confusing these two statements would later give the wrong sign for first Chern classes.

**Exercise 6.4 (hard).** If \(E\) is a bundle on a compact Hausdorff space, prove that finitely many global sections span every fibre, and derive its finite stabilization from those sections.

**Solution.** Multiply each vector of each local frame in a finite trivializing cover by its subordinate partition function and extend by zero. At every point at least one function is positive, so the corresponding \(r\) sections span the fibre. These finitely many sections give a surjective bundle map \(A:\varepsilon^N\to E\). Its kernel has constant rank and is a subbundle. Give \(\varepsilon^N\) its usual metric; restriction of \(A\) to \((\ker A)^\perp\) is a fibrewise isomorphism onto \(E\), so \(\varepsilon^N\cong\ker A\oplus E\). This proves stabilization by a surjection as well as by the injection in Theorem 5.1.

**Exercise 6.5 (hard).** Let \(P,Q\) be orthogonal projections of the same rank in \(\mathbb F^N\), with \(\|P-Q\|<1\). Prove that \(Q:\operatorname{im}P\to\operatorname{im}Q\) is invertible. Explain its bundle version.

**Solution.** For \(v\in\operatorname{im}P\), if \(Qv=0\), then \(v=(P-Q)v\), so \(\|v\|\leq\|P-Q\|\|v\|\) forces \(v=0\). Equal finite dimensions imply surjectivity. A continuous pair of projection fields satisfying the strict inequality therefore gives a fibrewise isomorphism between their image bundles. Lemma 1.1 proves that its inverse is continuous. The strict inequality is needed: projections onto perpendicular lines have norm difference one and their restriction map is zero.

## References

[H] Allen Hatcher, *Vector Bundles and K-Theory*, version 2.2, 2017, [author's text](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf). Copyrighted reference; no text or figures reproduced here.

[B40] Jim Hefferon, *Linear Algebra*, [original English text with solved exercises](https://kokunoyumeto.github.io/program-matematika-indonesia/en/readers/hefferon-linear-algebra/sources/00-linear-algebra-cumulative.tex). The relevant topics are bases and unique representation, Gram–Schmidt, orthogonal projections and the adjugate identity. The source is available under CC BY-SA 2.5, with its notices in the linked source archive.

[B40-B] [*From bases to projections*](https://kokunoyumeto.github.io/program-matematika-indonesia/en/readers/basis-projection-bridge/#extending-a-basis-and-choosing-a-complement), revision 2, especially the basis-extension theorem and projection corollary. Adapted from Hefferon by OpenAI GPT-6 Astra in Codex, at Ultra, October 2026; CC BY-SA 2.5. The finite-dimensional argument applies over every field.

[B40-H] [*Orthonormal bases and orthogonal projections*](https://kokunoyumeto.github.io/program-matematika-indonesia/en/readers/finite-hermitian-spaces/#orthogonal-projection-and-decomposition), Theorems 1–2. Proofs and exposition by OpenAI GPT-6 Astra in Codex, at Ultra, October 2026; CC BY-SA 4.0. The projected subspace is finite-dimensional; the ambient real or complex inner-product space need not be complete.
