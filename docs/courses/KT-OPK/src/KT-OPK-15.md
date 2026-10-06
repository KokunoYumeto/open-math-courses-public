# Smooth subalgebras and the density theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

*Independently authored CC0 lesson; self-checked by the writing AI.*

A differential formula requires derivatives of its coefficients. A projection or invertible supplied by a C*-algebra need not have those derivatives. The density theorem explains when one can replace it by a smooth representative without changing its K-class, and when equivalences between smooth representatives can themselves be made smooth.

The decisive properties concern inverses, spectral projections and matrices. Norm density supplies approximations. Functional calculus turns those approximations into exact representatives. We will keep these two operations separate, including the completeness assumption needed when contour integration is used inside a finer topology.

We use stable idempotent equivalence from [Idempotents, projections and their equivalences](KT-OPK-01.md), the Grothendieck construction from [K_0 of a unital algebra](KT-OPK-03.md), and stable invertible homotopy from [Invertibles, unitaries and K_1](KT-OPK-06.md). The contour calculus, its algebra property and spectral mapping are [Banach algebras, spectrum, holomorphic functional calculus and Gelfand theory, §6, Definition 6.4 and Theorems 6.7 and 6.10](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#6-the-holomorphic-functional-calculus).

## 1. What stability means

Let \(A\) be a complex C*-algebra and \(B\subset A\) a norm-dense complex subalgebra. Unless another topology is specified, \(B\) carries the norm inherited from \(A\); it need not be complete. Use the external unitizations \(B^+=B\oplus\mathbb C\) and \(A^+=A\oplus\mathbb C\), even when \(A\) already has a unit.

**Definition 1.1.** Scalar holomorphic stability means that

\[
\begin{gathered}
a\in B^+,\\
f\text{ holomorphic near }\sigma_{A^+}(a)\\
\Longrightarrow\quad f(a)\in B^+.
\end{gathered}
\tag{1.1}
\]

Matrix holomorphic stability means the corresponding assertion for every \(M_n(B^+)\subset M_n(A^+)\). For an element of \(B\) and a function vanishing at zero, the scalar quotient shows that \(f(a)\in B\). In a matrix unitization with scalar part \(C\in M_n(\mathbb C)\), the scalar part of \(f(a)\) is \(f(C)\).

An inclusion is **inverse closed**, or **spectrally invariant**, if an element of the smaller unital algebra invertible in the larger one has its inverse in the smaller one. Holomorphic stability implies this by taking \(f(z)=z^{-1}\). Inverse closure says the two spectra agree.

A **local Banach algebra**, in the sense of Blackadar, Definition 3.1.1, is a normed algebra with holomorphic stability also required at every matrix level. A local C*-algebra additionally has an involution and an inherited C*-norm. This terminology permits incomplete algebras.

Here is the precise scalar-to-matrix result we will prove. A Fréchet algebra is a complete metrizable locally convex algebra with continuous multiplication. A **continuous inverse algebra** has an open set of units and continuous inversion. These are separate hypotheses in the following theorem.

**Theorem 1.2 (matrix inheritance).** Suppose \(B\) is dense in \(A\).

1. Scalar inverse closure of \(B^+\) implies inverse closure at every matrix level, without a completeness assumption.
2. If \(B^+\) is also a Fréchet continuous inverse algebra whose inclusion into \(A^+\) is continuous, scalar holomorphic stability implies matrix holomorphic stability. In fact scalar inverse closure suffices under these additional hypotheses.

*Proof.* Write \(D=B^+\), \(E=A^+\). Suppose \(M\in M_n(D)\) is invertible in \(M_n(E)\). Choose \(N\in M_n(D)\) so close to \(M^{-1}\) that \(T=NM\) is near the identity. We prove by induction that such a \(T\) has inverse in \(M_n(D)\). The case \(n=1\) is scalar inverse closure.

Write

\[
\begin{gathered}
T=\begin{pmatrix}a&b\\c&d\end{pmatrix},\\
S=d-ca^{-1}b.
\end{gathered}
\tag{1.2}
\]

The scalar entry \(a\) is near \(1\), so is invertible in \(E\), with \(a^{-1}\in D\). Multiplication gives the factorization

\[
\begin{gathered}
T=L\operatorname{diag}(a,S)U,\\
L=\begin{pmatrix}1&0\\ca^{-1}&1\end{pmatrix},\\
U=\begin{pmatrix}1&a^{-1}b\\0&1\end{pmatrix}.
\end{gathered}
\tag{1.3}
\]

The outer factors are invertible. Since \(T\) is invertible, \(S\) is invertible in \(M_{n-1}(E)\). Its entries belong to \(D\), so induction gives \(S^{-1}\in M_{n-1}(D)\). Reversing the factors produces \(T^{-1}\in M_n(D)\). Now

\[
M^{-1}=T^{-1}N\in M_n(D).
\tag{1.4}
\]

For the second assertion, \(GL_n(D)=M_n(D)\cap GL_n(E)\) is open in the Fréchet topology. Matrix inversion is continuous there. To see this, near any fixed matrix \(M\), retain a fixed \(N\) chosen above. The scalar pivot stays invertible, and the Schur formula and induction express the inverse by continuous operations. These neighborhoods cover the group.

For \(X\in M_n(D)\) and a suitable surrounding cycle \(\Gamma\), the function \(z\mapsto(z-X)^{-1}\) is continuous with values in \(M_n(D)\). Its contour integral exists in this complete Fréchet space: Riemann sums are Cauchy for every continuous seminorm, and completeness gives their limit. The continuous inclusion takes that limit to the ambient contour integral. Consequently

\[
\begin{gathered}
f(X)=\int_\Gamma\frac{f(z)}{2\pi i}(z-X)^{-1}\,dz,\\
f(X)\in M_n(D).
\end{gathered}
\tag{1.5}
\]

This proves holomorphic stability at every level. \(\square\)

The Schur formula alone proves inverse closure. It does not justify taking the limit of Riemann sums in an incomplete subalgebra. The Fréchet form above is the matrix-calculus theorem of Schweitzer, §§1–2, with the integration hypotheses made explicit. For an arbitrary normed algebra we will assume matrix holomorphic stability, as in Blackadar's definition, or prove it directly for the particular algebra.

**Lemma 1.3 (Complete metrizability forces continuous inversion).** Let \(G\) be a group with a completely metrizable topology and jointly continuous multiplication. Then inversion is continuous.

*Proof.* Choose a compatible complete metric \(d\), and denote the identity by \(e\). Every fixed left or right translation is a homeomorphism: its inverse function is another fixed translation. This uses algebraic inverses of constants, without assuming continuity of the variable inverse map. It suffices to prove inversion continuous at \(e\).

Suppose there is an open identity neighbourhood \(U_0\) such that every identity neighbourhood contains an \(x\) with \(x^{-1}\notin U_0\). Construct nested open identity neighbourhoods of shrinking diameter with

\[
\overline{U_{j+1}}\ \overline{U_{j+1}}\subset U_j.
\tag{1.6}
\]

Indeed multiplication continuity gives an open \(W\ni e\) with \(WW\subset U_j\). A sufficiently small open metric ball has closure in \(W\cap U_j\); make its diameter at most \(2^{-j}\). No symmetry of these neighbourhoods is required. Choose \(x_j\in U_j\) with \(x_j^{-1}\notin U_0\). Then \(x_j\to e\).

Choose successively an increasing subsequence \(z_k=x_{m_k}\), with \(m_k\geq k\), so that, for \(y_0=e\) and \(y_k=y_{k-1}z_k\),

\[
d(y_k,y_{k-1})<2^{-k}.
\tag{1.7}
\]

Each choice is possible because the fixed translation by \(y_{k-1}\) is continuous and \(x_j\to e\). The products form a Cauchy sequence, so \(y_k\to y\in G\). The metric need not be invariant under translations.

For \(j>k\), the ordered tail \(z_{k+1}\cdots z_j\) belongs to \(U_k\). To verify this, start with \(z_j\in U_j\subset U_{j-1}\). If \(z_{l+1}\cdots z_j\in U_l\), then \(z_l\in U_l\), so their product is in \(U_lU_l\subset U_{l-1}\). Induction backwards proves the assertion, without commuting any factors. For each fixed \(k\), translation by \(y_k^{-1}\) now gives

\[
y_k^{-1}y\in\overline{U_k}\subset U_1,
\qquad k\geq2.
\tag{1.8}
\]

Here \(\overline{U_k}\subset U_{k-1}\) follows from (1.6) and \(e\in\overline{U_k}\). Since \(y_{k-1}\to y\), eventually \(y_{k-1}\in yU_1\). For such \(k\geq2\),

\[
\begin{gathered}
z_k^{-1}=y_k^{-1}y_{k-1}\\
=(y_k^{-1}y)(y^{-1}y_{k-1})\in U_1U_1\subset U_0.
\end{gathered}
\tag{1.9}
\]

This contradicts the choice of \(z_k\). Inversion is continuous at the identity. At a general \(g\), write \(x=gh\); fixed translations and \(x^{-1}=h^{-1}g^{-1}\) give continuity there as well. \(\square\)

**Corollary 1.4 (Fréchet density from inverse closure).** Suppose \(B\subset A\) is a dense complex subalgebra, \(B\) is a Fréchet algebra, its inclusion in the C*-algebra \(A\) is continuous, and \(B^+\) is inverse closed in \(A^+\). Then \(B^+\) is a continuous inverse algebra, matrix holomorphically stable in \(A^+\), and Theorem 2.1 gives both K-isomorphisms. Its finer Fréchet topology gives the same \(K_1\) group. No involution on \(B\) is required.

*Proof.* The external unitization is again a complete metrizable locally convex algebra with continuous multiplication. Inverse closure gives the exact equality

\[
GL_1(B^+)=\iota^{-1}(GL_1(A^+)),
\tag{1.10}
\]

so the unit group is open in \(B^+\). It is completely metrizable, although the restriction of the original complete metric need not be complete. To check this explicitly, let \(d\) be a compatible complete metric on \(B^+\) and \(F\) the closed complement of its unit group. If \(F\ne\varnothing\), use on the unit group

\[
\begin{gathered}
d'(x,y)=d(x,y)\\
\quad+\left|d(x,F)^{-1}-d(y,F)^{-1}\right|.
\end{gathered}
\tag{1.11}
\]

Distance to \(F\) is positive there and continuous. Thus \(d'\) is a metric with the same topology. A \(d'\)-Cauchy sequence is \(d\)-Cauchy and has bounded reciprocal distance to \(F\). Its ambient limit therefore stays a positive distance from \(F\), hence is a unit. Continuity of that reciprocal distance at the limit proves \(d'\)-convergence. If \(F\) is empty, use \(d\) itself.

Lemma 1.3 supplies continuous scalar inversion. Theorem 1.2's actual Schur-complement proof gives matrix inverse closure and continuous matrix inversion. Complete Fréchet contour integration then gives matrix holomorphic stability. Theorem 2.1 applies. Its finitely many affine path segments are continuous in the finer locally convex topology; conversely that topology's continuous paths are ambient norm continuous. Its two injectivity and surjectivity arguments therefore also identify the finer-topology \(K_1\). \(\square\)

Thus the additional continuous-inverse condition in Theorem 1.2 is automatic in this complete Fréchet setting. Density alone remains insufficient, and the incomplete-algebra contour limitation stated above remains in force. The group argument is the proof attributed to Pfister in [Roe, Proposition 16.5 and Remark 16.7, pp. 77–78], with the limiting tail kept in its closure. The matrix step uses our proved Schur formula rather than the module argument of that source.

## 2. The density theorem, including injectivity

Define \(K_0(B^+)\) from stable algebraic equivalence classes of idempotents, and \(K_1(B^+)\) from stable norm homotopy classes of invertibles. As in [Nonunital algebras](KT-OPK-04.md), \(K_0(B)\) is the kernel of the scalar map to \(\mathbb Z\); scalar normalization gives the relative description of \(K_1(B)\).

**Theorem 2.1 (density).** If \(B\subset A\) is dense and matrix holomorphically stable, then inclusion induces isomorphisms

\[
K_j(B)\ \xrightarrow{\ \cong\ }\ K_j(A),
\qquad j=0,1.
\tag{2.1}
\]

*Proof for \(K_0\).* First treat \(D=B^+\subset E=A^+\). Let \(e\in M_n(E)\) be an idempotent. On \(\Gamma=\{|z-1|=1/2\}\), put

\[
R=\max_{z\in\Gamma}\|(z-e)^{-1}\|.
\]

Choose \(b\in M_n(D)\) with \(\|b-e\|=\varepsilon\) small enough that \(R\varepsilon<1\), and that the spectrum of \(b\) remains in the disjoint disks around \(0\) and \(1\). Bound the resolvent of \(e\) uniformly on the compact set outside those disks inside a sufficiently large circle; the Neumann estimate preserves invertibility there. The large-\(|z|\) resolvent estimate handles the remaining exterior. Matrix holomorphic stability gives an idempotent

\[
\begin{gathered}
q=\frac{1}{2\pi i}\int_\Gamma(z-b)^{-1}\,dz,\\
q\in M_n(D).
\end{gathered}
\tag{2.2}
\]

Indeed this is the calculus of the function equal to zero on the component near zero and one on the component near one. The resolvent identity gives

\[
\|q-e\|
\leq\frac{R^2\varepsilon}{2(1-R\varepsilon)}.
\tag{2.3}
\]

Thus \(q\) can be arbitrarily close to \(e\). For close idempotents define

\[
\begin{aligned}
w&=qe+(1-q)(1-e)\\
 &=1+(q-e)(2e-1),\\
we&=qw.
\end{aligned}
\tag{2.4}
\]

If \(\|q-e\|\|2e-1\|<1\), \(w\) is invertible by the ambient Neumann estimate. Hence \(e\) and \(q\) represent the same stable class. This proves surjectivity on the semigroup of idempotent classes.

For injectivity, suppose two idempotents \(h,k\) over \(D\) become stably equivalent over \(E\). After adding zero blocks, the equivalence results of Lesson 1 give an invertible \(w\) over \(E\) with \(whw^{-1}=k\). Approximate \(w\) by \(v\) over \(D\). For a sufficiently close approximation, \(v\) is invertible in \(E\), hence has its inverse in \(D\). Then \(k'=vhv^{-1}\) is arbitrarily close to \(k\). Formula (2.4), applied to \(k'\) and \(k\), gives an invertible \(z\) over \(D\) with \(zk'z^{-1}=k\). Therefore \(zv\) implements the equivalence already over \(D\). The idempotent semigroups are isomorphic, so their Grothendieck groups are isomorphic.

If \(B\) is a *-subalgebra, \(b\) can be chosen selfadjoint when \(e\) is a projection. Then (2.2) is an orthogonal projection. For example \(\varepsilon<1/8\) gives \(R=2\) and \(\|q-e\|\leq(8/3)\varepsilon<1/3\). This is the smooth-projection mechanism used for projective modules.

*Proof for \(K_1\).* Given an invertible \(u\) over \(E\), approximate it by \(v\) over \(D\) with

\[
\|u^{-1}\|\|v-u\|<1.
\tag{2.5}
\]

The straight segment from \(u\) to \(v\) is invertible in \(E\), and \(v^{-1}\) belongs to \(D\). Thus every class has a representative over \(D\).

For injectivity, let an ambient path \(u(t)\) join two stabilized invertibles over \(D\). Its inverse norm has a finite maximum \(L\). Subdivide the interval so that oscillations on each segment are small, approximate its finitely many vertex values in \(D\), and keep the two endpoints exactly. The resulting affine polygonal path \(v(t)\) can be chosen with

\[
\sup_t\|v(t)-u(t)\|<L^{-1}.
\tag{2.6}
\]

Every \(v(t)\) is ambient invertible, so matrix inverse closure makes it invertible over \(D\). It is a norm-continuous path in \(D\) with the prescribed endpoints. Hence the original two classes agree over \(D\).

The external scalar maps on \(D\) and \(E\) commute with inclusion and have the same scalar splitting. The \(K_0\) isomorphism therefore restricts to their kernels. The relative \(K_1\) identification from Lesson 6 likewise gives (2.1) for \(B\) and \(A\). \(\square\)

This proof also covers a finer Fréchet continuous-inverse topology on \(B\). The polygonal path is continuous in that topology, and stable similarities implement the algebraic \(K_0\) equivalence. Conversely every path continuous in the finer topology is norm continuous. Thus the \(K_1\) group defined using that topology has the same answer.

The same approximation method handles families with any finite number of parameters. This strengthens the component calculation to all homotopy groups, with the topology specified.

**Theorem 2.2 (families of invertibles).** Suppose \(B\subset A\) is dense and matrix inverse closed. With the induced norm topology, inclusion

\[
GL_n(B^+)\longrightarrow GL_n(A^+)
\tag{2.7}
\]

induces a bijection of components and isomorphisms on every higher homotopy group, based at any invertible over \(B^+\). The same holds for the unions under identity padding, equipped with their matrix operator norm topology.

*Proof.* Translate the base point to the identity by multiplication by its inverse, which belongs to \(M_n(B^+)\). Represent a based sphere map by a map \(F\) on the cube \(I^k\) that equals the identity on its boundary. Compactness and continuity of inversion give a finite bound \(L\) on \(\|F(x)^{-1}\|\).

Subdivide the cube into small cubes, then divide each small cube into simplices according to the ordering of its coordinates. Uniform continuity makes the oscillation of \(F\) on each simplex arbitrarily small. Approximate its finitely many vertex values by matrices over \(B^+\), keeping boundary vertices equal to the identity. Affine interpolation gives a continuous piecewise affine map \(V\) over \(B^+\), equal to the identity on the boundary. Choose the oscillation and vertex errors so that

\[
\sup_x\|V(x)-F(x)\|<L^{-1}.
\tag{2.8}
\]

The Neumann estimate makes every point of the straight homotopy from \(F\) to \(V\) invertible in \(A^+\). Matrix inverse closure makes \(V\) invertible over \(B^+\). This proves surjectivity on every higher homotopy group. The component assertion is the same argument with one point and with an interval for a path.

For injectivity, start with a based map \(f\) over \(B^+\) that has an ambient nullhomotopy. First replace \(f\), by the construction above, with a piecewise affine map \(f'\) over \(B^+\). Both endpoints and their straight homotopy have entries in \(B^+\); inverse closure makes that homotopy invertible there. Follow the reversed homotopy from \(f'\) to \(f\) by the given nullhomotopy. This produces an ambient cube homotopy with bottom face \(f'\), top face the identity and all side faces the identity. Its boundary is piecewise affine over \(B^+\).

Use a sufficiently fine product subdivision extending the bottom-face subdivision, and interpolate vertex approximations on its simplices. Keep every boundary vertex exactly. The interpolation then agrees with the given piecewise affine map on the whole boundary. The uniform inverse bound for the ambient homotopy makes the interpolated homotopy invertible everywhere, by the same estimate (2.8). Inverse closure puts it in \(GL_n(B^+)\). Thus \(f'\), and hence \(f\), is nullhomotopic there. For \(k\geq1\), the induced maps are homomorphisms, so this kernel calculation proves injectivity.

For the norm topology on the stable union, realize its matrices as finite blocks acting on the standard stabilized module, with identity on the remaining coordinates. Inversion is continuous in the unital completion of these finite blocks. Consequently compact parameter sets still have the uniform inverse bounds used above. Each vertex approximation has finite size, and the finitely many vertices fit in one common size. Affine interpolation therefore has a common finite size. A straight segment between an original finite block and such an approximation lies in a finite matrix algebra at each parameter value; the ambient invertibility estimate makes it invertible in that algebra. The homotopy is norm continuous even if the original map does not factor through one fixed size. After its piecewise affine replacement the boundary has a common finite size, so the relative nullhomotopy argument also applies. This proves the stable assertion without assuming that every compact family originally lies at a finite stage. \(\square\)

This proves the higher homotopy conclusion recorded in Connes, III, Appendix C, Proposition 3(b). Matrix holomorphic stability implies the inverse-closure hypothesis; the proof uses only inverse closure for this particular conclusion. The statement concerns the induced norm topology, rather than an unspecified finer topology.

### 2.3. The final topology of the stable stages

Connes, III, Appendix C, Proposition 3(b), p.292, phrases the stable density result using an inductive limit. We now specify a final topology of spaces and give the finite-stage argument for that topology. It also proves that changing from the stable norm topology to this final topology preserves the homotopy groups.

**Theorem 2.3 (two stable topologies).** Assume the matrix inverse-closure and density hypotheses of Theorem 2.2. Every finite invertible group with its induced norm topology is locally contractible. For either \(B\) or \(A\), the final union and the stable norm union both have homotopy groups equal to the colimits of those of their finite stages. The continuous identity from the final union to the norm union induces a component bijection and all higher homotopy isomorphisms. Inclusion from \(B\) to \(A\) has the same property for either stable topology. Higher homotopy groups are based at the identity; the component statement is a statement about sets.

Let \(B\subset A\) be a dense complex subalgebra of a C*-algebra, as in Lesson 15, and suppose that \(M_n(B^+)\subset M_n(A^+)\) is inverse closed for every \(n\). Give

\[
\begin{gathered}
G_n(B)=GL_n(B^+),
\\ G_n(A)=GL_n(A^+).
\end{gathered}
\tag{2.9}
\]

their induced norm topologies and embed them by \(X\mapsto\operatorname{diag}(X,1)\). Their unions have two relevant topologies. The **stable norm topology** uses the matrix operator norm after identity padding. The **final topology of the stages** declares \(U\) open exactly when \(U\cap G_n\) is open in \(G_n\) for every \(n\). In this paragraph and the following proof, “final” refers to this explicit topology of spaces.

*Proof.* First, every \(G_n(B)\) is a locally contractible topological group. Inversion is the restriction of continuous ambient inversion, since inverse closure puts its values in \(M_n(B^+)\). For \(X\in G_n(B)\), choose \(r>0\) with \(r\|X^{-1}\|<1\). The relative ball

\[
V_r(X)=\{Y\in M_n(B^+):\|Y-X\|<r\}
\]

consists entirely of invertibles: apply the ambient Neumann estimate, then inverse closure. The contraction

\[
H(Y,t)=X+(1-t)(Y-X)
\tag{2.10}
\]

stays in that ball. Such balls give a contractible neighborhood basis.

For either algebra, a compact subset of the union with the final topology lies in one finite stage. To prove this, suppose a compact set \(K\) did not. Choose distinct \(x_j\in K\) and increasing integers \(n_j\geq j\) so that every previously chosen point lies in \(G_{n_j}\) and \(x_j\notin G_{n_j}\). This is possible because finitely many points fit in one stage and \(K\) does not. For each fixed \(m\), the set \(S=\{x_j:j\geq1\}\) meets \(G_m\) in a finite set. Every subset \(C\subset S\) therefore has \(C\cap G_m\) closed in \(G_m\). The definition of the final topology makes every such \(C\) closed in the union. Thus \(S\) is closed in \(K\) and is an infinite discrete space. It would be compact as a closed subset of \(K\), whereas its singleton open cover has no finite subcover. This contradiction proves the claim.

Each stage retains its original topology inside the final union. Indeed each identity-padding inclusion is a closed topological embedding. Starting with an open set in \(G_n\), extend it successively to open sets in \(G_{n+1},G_{n+2},\ldots\) with the prescribed intersections, using the subspace topology at each step; on earlier stages take its intersections. The union of these compatible sets is final-open and restricts to the original open set. Consequently a continuous map from a compact space to the final union, whose image lies in \(G_n\), is continuous as a map to \(G_n\).

It follows for every \(k\geq0\) that

\[
\pi_k(G_\infty^{\mathrm{final}})
 =\underset{n}{\operatorname{colim}}\ \pi_k(G_n).
\tag{2.11}
\]

Every sphere map and every homotopy has compact image and hence factors continuously through a finite stage. These two facts give respectively surjectivity and injectivity of the canonical map in (2.11). For \(k=0\), use points and paths and interpret the formula as the corresponding statement about components.

The same colimit formula holds for the stable norm union, although its compact subsets need not lie in a finite stage. To see the distinction explicitly, let \(e_{jj}\) be the \(j\)-th diagonal matrix unit and consider the identity-padded invertibles

\[
X_j=I+j^{-1}e_{jj}\otimes1_{A^+}.
\tag{2.12}
\]

They converge in norm to \(I\), so \(\{I,X_1,X_2,\ldots\}\) is norm compact. They do not all belong to any one stage, so the proved compact-stage property prevents this set from being compact in the final topology.
 Here is the necessary replacement argument. For a based sphere map, use a cube with constant boundary. Its compact image has a uniform inverse bound \(L\). Triangulate the cube finely enough that its oscillation on each simplex is less than \(L^{-1}\). The finitely many vertex values have a common matrix size. Interpolate them affinely, keeping boundary values the identity. The resulting map has that common size and is uniformly within \(L^{-1}\) of the original map. The straight homotopy is ambient invertible by the Neumann estimate. For \(B\), every point of this homotopy lies in a finite matrix algebra over \(B^+\): an original value and the affine replacement each have finite size, although a common size for all original values has not been assumed. The ambient inverse estimate makes that finite block invertible, and inverse closure puts its inverse over \(B^+\). It is continuous in the stable norm topology. This gives a finite-stage representative.

For a nullhomotopy of a finite-stage map, first replace the boundary map by a piecewise affine one in that same stage. Follow the straight homotopy from this replacement back to the original map by the given nullhomotopy. Triangulate the resulting cube compatibly with its piecewise affine boundary, keep all boundary vertex values, and interpolate the remaining vertices. The same uniform inverse bound puts the interpolated nullhomotopy in one finite stage and fixes its entire boundary. Combining with the first boundary replacement proves the finite-stage injectivity assertion. The component case uses the identical argument for an interval. This proves the stable norm analogue of (2.11).

The identity from the final union to the norm union is continuous, since every stage inclusion into the norm union is continuous. The two colimit calculations show that it induces bijections on components and isomorphisms on every higher homotopy group.

Finally, the finite-stage density argument of Lesson 15, Theorem 2.2, applies to \(G_n(B)\to G_n(A)\). It uses finite affine approximations with error less than a uniform inverse bound, and requires only matrix inverse closure. Its finite-stage isomorphisms pass to the colimits in (2.11). Hence inclusion induces the same homotopy-group isomorphisms for both stable topologies. This supplies the explicit final-topology version of Connes's density conclusion without identifying the two topological spaces or asserting a result for an unspecified finer topology on \(B\). \(\square\)

## 3. Closed derivations supply complete calculus domains

Let \(\delta:\mathcal D\to A\) be a densely defined closed derivation, where \(\mathcal D\) is a subalgebra and

\[
\delta(ab)=\delta(a)b+a\delta(b).
\tag{3.1}
\]

For a *-derivation also assume \(\mathcal D\) is *-closed and \(\delta(a^*)=\delta(a)^*\). Adjoin an external unit with \(\delta(1)=0\).

**Theorem 3.1.** The graph domain \(\mathcal D\), with norm

\[
\|a\|_\delta=\|a\|+\|\delta(a)\|,
\tag{3.2}
\]

is a Banach algebra, and is holomorphically stable in every matrix algebra over \(A\).

*Proof.* A graph-norm Cauchy sequence gives norm limits for both \(a_j\) and \(\delta(a_j)\); closedness puts the limit in the graph. The product rule gives

\[
\|ab\|_\delta\leq\|a\|_\delta\|b\|_\delta.
\]

Completeness does not yet prove ambient inverse closure. For that, if \(x\in\mathcal D^+\) satisfies \(\|x\|<1\), the Neumann series belongs to the graph domain, since

\[
\begin{aligned}
\delta(x^m)&=\sum_{r=0}^{m-1}x^r\delta(x)x^{m-1-r},\\
\|\delta(x^m)\|&\leq m\|x\|^{m-1}\|\delta(x)\|.
\end{aligned}
\tag{3.3}
\]

The right-hand bound is summable in \(m\). Thus \((1-x)^{-1}\in\mathcal D^+\).

Now take \(a\in\mathcal D^+\) invertible in \(A^+\), and approximate \(a^{-1}\) in norm by \(b\in\mathcal D^+\) so that \(\|1-ab\|<1\). The preceding argument gives \((ab)^{-1}\in\mathcal D^+\), hence \(a^{-1}=b(ab)^{-1}\in\mathcal D^+\). Differentiating \(aa^{-1}=1\) yields

\[
\delta(a^{-1})=-a^{-1}\delta(a)a^{-1}.
\tag{3.4}
\]

For the resolvent \(R(z)=(z-a)^{-1}\), this becomes

\[
\delta(R(z))=R(z)\delta(a)R(z).
\tag{3.5}
\]

Both expressions are norm continuous on a surrounding cycle. The resolvent is therefore graph-norm continuous there, and its contour integral belongs to the complete graph domain. This proves holomorphic stability. Entrywise amplification is a closed derivation on each matrix algebra: convergence of a matrix and its derivative is convergence in each of finitely many entries. The same argument proves every matrix assertion. \(\square\)

This theorem also holds for a derivation with values in a Banach algebra containing \(A\), using the inherited left and right multiplication, provided its graph is closed. The preceding estimates and the graph integral are unchanged.

For example \(C^1[0,1]\), with derivative and graph norm, has the same K-theory as \(C[0,1]\). Completeness of the derivative graph follows by integrating the limiting derivative; polynomial approximation makes the domain norm dense.

### A differential norm gives a checkable criterion

The graph-domain argument above is a special case of a useful Banach-algebra test. It converts an estimate on products into matrix holomorphic stability; compare [Roe, Corollary 14.7].

**Proposition 3.2 (differential norm criterion).** Let \(B\) be a norm-dense *-subalgebra of a C*-algebra \(A\). Suppose \(B\) has a complete submultiplicative norm \(N\), with continuous involution and \(N(b)\geq\|b\|_A\), and for some \(C>0\),

\[
\begin{aligned}
N(bc)&\leq C\bigl(\|b\|_A N(c)\\
&\hspace{4em}+N(b)\|c\|_A\bigr).
\end{aligned}
\tag{3.6}
\]

Then \(B\) is inverse closed and holomorphically stable at every matrix level, with external unitizations when needed. Inclusion induces both K-isomorphisms of Theorem 2.1, also when \(K_1(B)\) uses its Banach norm topology.

*Proof.* First suppose the two algebras have the same identity. Write \(\rho_B,\rho_A\) for their spectral radii. Applying (3.6) to \(b^m,b^m\), taking \(m\)-th roots, and using the Banach spectral-radius formula gives

\[
\rho_B(b)^2\leq\rho_B(b)\rho_A(b).
\tag{3.7}
\]

Indeed the constant \(2C\) has \(m\)-th root tending to one, and \(N(b^{2m})^{1/m}\) tends to \(\rho_B(b)^2\). If \(\rho_B(b)>0\), divide by it; if it is zero the resulting inequality already holds. The reverse inequality follows from \(\|b^m\|_A\leq N(b^m)\). Thus the two radii agree for every \(b\in B\).

Equality of radii alone is not used as an assertion of equality of spectra. Let \(b\in B\) be invertible in \(A\). Positivity and invertibility of \(b^*b\) give, for \(\lambda>\|b^*b\|_A\),

\[
\begin{gathered}
h=1-\lambda^{-1}b^*b,\\
\rho_B(h)=\rho_A(h)<1.
\end{gathered}
\tag{3.8}
\]

Choose \(q\) strictly between this radius and one. The spectral-radius formula gives \(N(h^k)\leq q^k\) for all sufficiently large \(k\). Consequently \(\lambda^{-1}\sum_{k\geq0}h^k\) converges in the complete algebra \(B\) and, by multiplication of its partial sums, is the inverse of \(b^*b\). It gives a left inverse for \(b\). The same argument for \(bb^*\) gives a right inverse. A left and a right inverse coincide, since \(l=l(br)=(lb)r=r\); hence \(b^{-1}\in B\).

For an algebra without a common identity, pass to the forced unitizations. Put \(N^+(b+\mu1)=N(b)+|\mu|\). This is a complete submultiplicative norm dominating the ambient unitized C*-norm. The scalar quotient gives \(|\mu|\leq\|b+\mu1\|\), and therefore \(\|b\|\leq2\|b+\mu1\|\). Expanding the product, applying (3.6) to its \(bc\) term, and bounding the other three terms yields

\[
\begin{aligned}
N^+(xy)&\leq(2C+2)\bigl(\|x\|N^+(y)\\
&\quad+N^+(x)\|y\|\bigr).
\end{aligned}
\tag{3.9}
\]

This also applies if \(B\) was already unital but its identity was not the ambient one. The preceding inverse argument now applies to the unitizations, with no missing scalar normalization.

For matrices set \(N_k(X)=\sum_{i,j}N^+(x_{ij})\). This is a complete submultiplicative norm and dominates the ambient matrix norm. Each entry satisfies \(\|x_{ij}\|\leq\|X\|\). Summing (3.9) over the matrix product entries gives

\[
\begin{aligned}
N_k(XY)&\leq k(2C+2)\\
&\quad\cdot\bigl(\|X\|N_k(Y)\\
&\qquad+N_k(X)\|Y\|\bigr).
\end{aligned}
\tag{3.10}
\]

The factor \(k\) comes from summing over a row or column of the other matrix. Applying the same spectral-radius and positive-product argument proves inverse closure at every matrix level.

Inversion in each complete Banach matrix algebra is continuous: near an invertible \(X\), the series for \((1+X^{-1}H)^{-1}X^{-1}\) converges in its Banach norm. On a compact contour outside the common spectrum, the resolvent is therefore continuous in that norm and can be integrated there. Its ambient image is precisely the ambient holomorphic functional calculus. Subtracting its scalar part leaves a matrix over \(B\), so this proves matrix holomorphic stability. Theorem 2.1 supplies the K-isomorphisms. Its finite polygonal paths are continuous also for \(N\), while an \(N\)-continuous path is ambient continuous; this proves the final topology assertion. \(\square\)

For a closed *-derivation, the graph norm \(N(b)=\|b\|+\|\delta(b)\|\) satisfies (3.6) with \(C=1\), directly from the Leibniz rule and the product norm bound. More generally the same test applies to any complete normed *-subalgebra for which the displayed estimate has been proved. Completeness and that estimate are actual hypotheses; a dense algebra supplied only with the ambient norm acquires neither from density.

## 4. Smooth actions and regular spectral triples

Let a finite-dimensional Lie group \(G\) act on \(A\) by automorphisms, continuously in norm on each element. Its smooth algebra \(A^\infty\) consists of the elements \(a\in A\) whose orbit map is smooth in norm:

\[
\begin{gathered}
\mathcal O_a:G\longrightarrow A,\\
\mathcal O_a(g)=\alpha_g(a).
\end{gathered}
\tag{4.1}
\]

**Theorem 4.1.** \(A^\infty\) is norm dense and holomorphically stable at every matrix level. Its inclusion induces the two K-theory isomorphisms of Theorem 2.1.

*Proof.* For nonnegative \(f\in C_c^\infty(G)\) with Haar integral one, set \(a_f=\int f(g)\alpha_g(a)\,dg\). Applying \(\alpha_h\) changes the coefficient to \(f(h^{-1}g)\). All derivatives in \(h\), on a fixed small neighborhood, are supported in one compact set and uniformly bounded there. Differentiation under the norm integral proves \(a_f\in A^\infty\). Concentrating the support at the identity gives \(a_f\to a\).

If a smooth \(a\) is ambient invertible, \(\alpha_g(a^{-1})=\alpha_g(a)^{-1}\) is smooth. Indeed Banach-algebra inversion is smooth by its local Neumann expansion, with first derivative \(h\mapsto-a^{-1}ha^{-1}\). For holomorphic \(f\), apply the contour formula to \(\alpha_g(a)\) on a fixed surrounding cycle. Its resolvents and every derivative in \(g\) are uniformly bounded on that cycle locally in \(g\). Differentiating the integral proves that \(f(a)\) is smooth. The entrywise action on matrices proves matrix stability; external unitization treats a nonunital algebra. Theorem 2.1 now applies. \(\square\)

For a basis \(X_1,\ldots,X_d\) of the Lie algebra, the seminorms

\[
p_m(a)=\sum_{r=0}^m
\sum_{i_1,\ldots,i_r}
\|\delta_{X_{i_1}}\cdots\delta_{X_{i_r}}a\|
\tag{4.2}
\]

give the usual smooth Fréchet topology. Completeness follows by closedness of the infinitesimal generators and induction on derivative order; convergence of orbit maps and their derivatives in local coordinates then recovers smoothness. The Leibniz rule bounds each product seminorm by a finite sum of products of lower seminorms. The inverse formulas just proved give continuous inversion in this topology. The finer-topology conclusion following Theorem 2.1 therefore applies.

For the rotation algebra \(A_\theta\), generated by unitaries with \(VU=e^{2\pi i\theta}UV\), the action

\[
\begin{gathered}
\alpha_{s,t}(U)=e^{is}U,\\
\alpha_{s,t}(V)=e^{it}V.
\end{gathered}
\tag{4.3}
\]

defines \(A_\theta^\infty\) by (4.1), with \(G=\mathbb T^2\). The relations are preserved, and the inverse action is \(\alpha_{-s,-t}\). Continuity holds first on finite words in the generators and then on their norm closure. Theorem 4.1 applies for rational and irrational \(\theta\). We need no K-group computation of \(A_\theta\) to conclude that its smooth algebra has the same groups. This is the algebra used in [Connections and curvature from symmetries of an algebra, §1](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/prerequisites/NCG-CYCLIC/connections-and-curvature-for-c-star-dynamical-systems.html#1-smooth-elements-retain-projective-modules).

For a compact smooth manifold \(M\), \(C^\infty(M)\subset C(M)\) is another example. In a finite coordinate cover, multiply a continuous function by a smooth partition of unity, approximate each compactly supported coordinate function by convolution, and sum; this proves uniform density. For a matrix of smooth functions, pointwise inversion is smooth wherever the determinant is nonzero. The contour formula then preserves smoothness, by differentiating under its compact integral. Thus Theorem 2.1 applies.

Here is a careful spectral-triple version. Let \(\Lambda\) be selfadjoint on \(H\), and let \(\delta(T)=[\Lambda,T]\) on bounded operators preserving \(\operatorname{Dom}\Lambda\) with bounded commutator. This derivation has the adjoint rule \(\delta(T^*)=-\delta(T)^*\). It is closed: if \(T_j\to T\) and \(\delta(T_j)\to C\), then for \(\xi\in\operatorname{Dom}\Lambda\),

\[
\begin{aligned}
\Lambda T_j\xi&=T_j\Lambda\xi+\delta(T_j)\xi\\
&\longrightarrow\ T\Lambda\xi+C\xi.
\end{aligned}
\tag{4.4}
\]

Closedness of \(\Lambda\) proves \(T\xi\in\operatorname{Dom}\Lambda\) and the desired commutator identity. Taking adjoints in its sesquilinear form proves preservation of the domain by \(T^*\) and the stated adjoint rule.

Suppose a unital C*-algebra \(A\subset B(H)\) contains a norm-dense *-algebra \(\mathcal A_0\) lying in every \(\operatorname{Dom}\delta^k\). Then

\[
\mathcal A_\Lambda=A\cap\bigcap_{k\geq0}\operatorname{Dom}\delta^k
\tag{4.5}
\]

is a dense Fréchet *-algebra with seminorms \(\sum_{j\leq k}\|\delta^j(a)\|\). Completeness follows successively from closedness of \(\delta\). For \(a\) invertible in \(A\), approximate \(a^{-1}\) by \(b\in\mathcal A_0\); the derivative-summable Neumann argument (3.3) puts \(b(ab)^{-1}=a^{-1}\) in the first commutator domain. No norm density in all of \(B(H)\) is needed. Formula (3.4) and the Leibniz rule then inductively put that inverse in every iterated domain. The same formulas give (3.5) and its higher derivatives. Repeated differentiation of the contour formula, in these complete graph seminorms, proves matrix holomorphic stability.

For a **regular** spectral triple take \(\Lambda=|D|\). The required dense algebra is the represented spectral-triple algebra; regularity places both its elements and their \(D\)-commutators in all these domains. These are exactly the hypotheses in [Spectral triples and dimension spectrum, §1](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/preparation.html#dependency-f1d9b2ae7966). A spectral triple without regularity does not supply this conclusion automatically. Derivatives may take values in \(B(H)\), rather than in \(A\), which is why the containing-algebra version of Theorem 3.1 matters.

## 5. Incomplete ideals still admit matrix calculus

Not every useful smooth or local algebra carries the Fréchet topology of Theorem 1.2.

**Proposition 5.1.** Any algebraic two-sided ideal \(I\) of a C*-algebra \(A\) is holomorphically stable in all matrix unitizations.

*Proof.* Work in \(A^+\), in which \(I\) is still an ideal. Let \(X\in M_n(I^+)\) have scalar part \(C\in M_n(\mathbb C)\). The scalar quotient implies \(\sigma(C)\subseteq\sigma(X)\). Let \(m_C\) be the minimal polynomial of \(C\). Choose a polynomial \(r\) having the same derivatives as \(f\) at each root of \(m_C\), through one less than its multiplicity. Such an \(r\) exists by the polynomial Chinese remainder theorem for the pairwise coprime powers of \(z-\lambda\).

The function \(g=(f-r)/m_C\) has removable singularities at these roots and is holomorphic near \(\sigma(X)\). Since \(m_C(C)=0\), \(m_C(X)\in M_n(I)\). Moreover \(r(X)-r(C)\in M_n(I)\). Consequently

\[
\begin{aligned}
f(X)-f(C)
 &=r(X)-r(C)\\
 &\quad +m_C(X)g(X)\\
 &\in M_n(I).
\end{aligned}
\tag{5.1}
\]

Here \(r(C)=f(C)\) by the finite-dimensional holomorphic calculus, and the ideal property permits multiplication by the ambient \(g(X)\). This proves the assertion without completing \(I\). \(\square\)

There is a canonical smallest dense ideal to which this proposition applies. Its construction needs only positive functional calculus and the Neumann criterion.

**Theorem 5.2 (the Pedersen ideal).** Let \(K(A)\) be the algebraic two-sided ideal generated by

\[
\begin{gathered}
(a-\varepsilon)_+,\\
a\in A_+,\quad\varepsilon>0.
\end{gathered}
\tag{5.2}
\]

Then \(K(A)\) is a dense *-ideal contained in every dense algebraic two-sided ideal of \(A\). In particular it is the unique smallest dense ideal.

*Proof.* Positive functional calculus puts each generator in \(A\), since the scalar function vanishes at zero. The generators are selfadjoint, so the two-sided ideal they generate is invariant under adjoints. Moreover

\[
\|a-(a-\varepsilon)_+\|\leq\varepsilon.
\tag{5.3}
\]

Thus its closure contains every positive element. A selfadjoint element is the difference of its positive and negative parts, and every element is the sum of a selfadjoint element and \(i\) times one. Hence the ideal is dense.

Let \(I\) be any dense algebraic two-sided ideal, with no closure or adjoint assumption. Fix \(c=(a-\varepsilon)_+\), and set \(e=h(a)\), where \(h(t)=\min(1,t/\varepsilon)\) for \(t\geq0\). Then \(e\in A\) and \(ce=c\). Choose \(y\in I\) with \(\|y-e\|<1\). In the external unitization,

\[
\begin{gathered}
x=1-e+y=1+(y-e),\\
cx=cy,\qquad c=cyx^{-1}.
\end{gathered}
\tag{5.4}
\]

The Neumann criterion supplies \(x^{-1}\). Since an ideal of \(A\) is also an ideal under multiplication by \(A^+\), the last expression belongs to \(I\). Every generator of \(K(A)\) therefore lies in \(I\), proving minimality and uniqueness. \(\square\)

This is the Pedersen ideal described in Blackadar, Example 3.1.2(a), with the reference there to Pedersen, §5.6. Its existence, density and defining minimality have now been proved, and Proposition 5.1 supplies its matrix calculus. Theorem 2.1 therefore identifies its K-theory with that of \(A\). Likewise \(C_c(X)\) is a dense ideal of \(C_0(X)\) for locally compact Hausdorff \(X\); Exercise 15.5 proves its density and support checks explicitly.

## 6. Why density alone is insufficient

Analytic polynomials \(\mathbb C[z]\) on \(\mathbb T\) are **not** norm dense in \(C(\mathbb T)\). The continuous functional

\[
\ell(f)=\frac{1}{2\pi}\int_0^{2\pi}
f(e^{it})e^{it}\,dt
\tag{6.1}
\]

vanishes on every analytic polynomial but takes value \(1\) on \(z^{-1}\). Also \(z\) is ambient invertible but has no inverse in that polynomial algebra. This example illustrates failed inverse closure, but cannot demonstrate failure of a theorem whose density hypothesis it does not satisfy.

A genuine dense example is \(B=\mathbb C[x,y]\subset C(\mathbb T)\), where

\[
\begin{aligned}
x(e^{it})&=\cos t,\\
y(e^{it})&=\sin t\,e^{\cos t}.
\end{aligned}
\tag{6.2}
\]

Both generators are real, so \(B\) is a *-algebra. Polynomials in \(x\) approximate \(e^{-x}\) uniformly by the exponential series. Their products with \(y\) therefore approximate \(\sin t\). The closure of \(B\) contains \(\cos t,\sin t\), hence \(z,z^{-1}\). Laurent polynomials are uniformly dense by the Fejér approximation proved in [Bott periodicity, §5](KT-OPK-10.md#5-the-polynomial-loop-route-an-outline-with-explicit-reductions); thus \(B\) is dense.

These two functions are algebraically independent. Write a hypothetical relation as \(P(X,Y)=\sum_jp_j(X)Y^j\). On the upper and lower semicircles, \(X=u\in(-1,1)\) and \(Y=\pm\sqrt{1-u^2}e^u\). Adding and subtracting the two relations, and dividing the odd relation by \(Y\), gives

\[
\begin{aligned}
\sum_k p_{2k}(u)(1-u^2)^ke^{2ku}&=0,\\
\sum_k p_{2k+1}(u)(1-u^2)^ke^{2ku}&=0.
\end{aligned}
\tag{6.3}
\]

Each left side is an entire exponential polynomial, so vanishing on the interval makes it identically zero. For the largest exponent, divide by its exponential and let real \(u\to+\infty\). Its polynomial coefficient tends to zero because every lower exponential dominates its polynomial factor in decay. A polynomial tending to zero there is zero. Induction proves all coefficients zero, and hence every \(p_j=0\).

Thus \(B\) is isomorphic to \(\mathbb C[X,Y]\). The only units of this polynomial ring are nonzero constants: total degrees add in a product of nonzero polynomials. Every matrix invertible over \(B\) consequently has constant determinant. Its circle winding pairing

\[
\begin{aligned}
&\frac{1}{2\pi i}\int_0^{2\pi}
\operatorname{Tr}(v(t)^{-1}v'(t))\,dt\\
&\hspace{1em}=\operatorname{wind}(\det v)
\end{aligned}
\tag{6.4}
\]

is zero, by the determinant derivative formula. This pairing is invariant under ambient stable homotopy by [Determinants of traces and the pairing with K_1, §5](KT-OPK-14.md#5-an-invariant-derivation-gives-an-odd-pairing). For the scalar \(z=e^{it}\) it equals \(1\). Therefore \([z]\) is not in the image of \(K_1(B)\to K_1(C(\mathbb T))\), despite norm density and smooth generators.

In this example \(x-2\) is ambient invertible but is not a unit of \(B\). The inverse-closure step in the density proof fails precisely.

## 7. Exercises with complete solutions

**Exercise 15.1.** Prove spectral invariance and holomorphic stability of \(C^1[0,1]\subset C[0,1]\).

*Solution.* If \(f\) has no zero, compactness gives \(\min|f|>0\), and

\[
(f^{-1})'=-f^{-2}f'
\]

is continuous. Thus its inverse is \(C^1\). The norm \(\|f\|_\infty+\|f'\|_\infty\) is complete: for graph limits \(f,g\), the identity \(f_j(t)-f_j(0)=\int_0^tf'_j(s)\,ds\) passes to the limit and gives \(f'=g\). Multiplication satisfies the graph-norm product estimate. If \(F\) is holomorphic near the range of \(f\), \(F(f)\) has derivative \(F'(f)f'\), so is \(C^1\). For a matrix function the inverse is \(C^1\) by differentiating the matrix product; the contour formula has a continuous derivative uniformly on its compact cycle. This proves matrix holomorphic stability as well. Polynomials are uniformly dense, so Theorem 2.1 applies.

**Exercise 15.2.** Prove the \(2\times2\) Schur inverse formula and explain its precise inheritance consequence.

*Solution.* For \(T\) in (1.2) with scalar entries and invertible \(a,S\), direct multiplication of (1.3) gives

\[
\begin{aligned}
(T^{-1})_{11}&=a^{-1}+a^{-1}bS^{-1}ca^{-1},\\
(T^{-1})_{12}&=-a^{-1}bS^{-1},\\
(T^{-1})_{21}&=-S^{-1}ca^{-1},\\
(T^{-1})_{22}&=S^{-1}.
\end{aligned}
\tag{7.1}
\]

If \(T\) is near the identity, \(a\) is ambient invertible; (1.3) then forces \(S\) ambient invertible. Scalar inverse closure puts both inverses in the smaller algebra, so all four entries in (7.1) belong to it. For an arbitrary invertible matrix first replace \(T\) by \(NM\) as in Theorem 1.2. This proves matrix inverse closure. With the complete continuous-inverse Fréchet hypotheses, these formulas also give continuous matrix inversion, and the Fréchet contour integral proves matrix holomorphic stability. Without those hypotheses the contour step needs a separate justification or a direct matrix-stability assumption.

**Exercise 15.3.** Prove the inverse and holomorphic-calculus assertions for a closed derivation, including the domain issue.

*Solution.* Approximate an ambient inverse \(a^{-1}\) by \(b\) in the domain with \(\|1-ab\|<1\). Formula (3.3) shows convergence of the Neumann series for \((ab)^{-1}\) in graph norm, rather than just ambient norm. Hence \(a^{-1}=b(ab)^{-1}\) is in the domain. Applying the derivation to \(aa^{-1}=1\) gives (3.4), and substituting \(z-a\) gives the positive sign in (3.5). The derivative of the resolvent is continuous on the contour by that formula. Completeness of the graph domain therefore permits integration there; its ambient image is \(f(a)\). Closedness entry by entry and the amplified product rule prove the same argument for every matrix. Each operation has been performed in its stated domain.

**Exercise 15.4.** Explain the analytic-polynomial example, give a genuinely dense counterexample, and identify the failed proof step.

*Solution.* Formula (6.1) separates \(z^{-1}\) from the closure of \(\mathbb C[z]\), so the analytic-polynomial example lacks density. Its invertible matrices have nonzero constant polynomial determinant and hence cannot represent the winding-one class \([z]\). For the actual dense example use (6.2). Approximation of \(e^{-x}\) gives \(\sin t\), then Laurent density gives all of \(C(\mathbb T)\). The even and odd decomposition (6.3), followed by the entire-function identity and largest-exponent argument, proves \(B\cong\mathbb C[X,Y]\). Its matrix determinants are constant units, so (6.4) vanishes for every class in the image, whereas it is one on \(z\). Norm approximation can make a matrix ambient invertible without making it invertible over \(B\). This invalidates (2.5)'s transfer of the inverse and is exactly the missing stability property.

**Exercise 15.5.** For locally compact Hausdorff \(X\), verify density and matrix holomorphic stability of \(C_c(X)\subset C_0(X)\), including scalar parts.

*Solution.* Given \(f\in C_0(X)\) and \(\varepsilon>0\), the set where \(|f|\geq\varepsilon\) is compact. A compactly supported continuous cutoff \(0\leq h\leq1\), equal to one on this set, exists by the compact-cutoff construction in [Topological K-theory, §1](KT-OPK-12.md#1-compact-supports-and-the-exact-sequence-of-a-pair). Then \(hf\in C_c(X)\) and \(\|f-hf\|\leq\varepsilon\).

For \(F=C+G\in M_n(C_c(X)^+)\), the support of all entries of \(G\) lies in one compact set \(K\). Outside \(K\), \(F(x)=C\), so \(f(F(x))-f(C)=0\). The surrounding-cycle formula makes this matrix function continuous everywhere: the resolvents are continuous and uniformly bounded on the cycle. Thus \(f(F)-f(C)\) has compact support and belongs to \(M_n(C_c(X))\). Its scalar part is exactly \(f(C)\), as required. Theorem 2.1 gives both K-isomorphisms, with external-unitization kernels retained.

## What this lesson does not prove

The ambient contour calculus and spectral mapping are imported from the foundation lesson, §6, at the precise locators given above. Stable idempotent equivalence, external-unitization K-theory, invertible homotopy, Fejér approximation and the circle winding pairing are imported from Lessons 1, 3, 4, 6, 10 and 14 at the stated sections. The two K-isomorphisms, all higher norm homotopy groups of invertibles, and the existence, density and minimality of the Pedersen ideal are proved here. No irrational-rotation K-group computation, local index formula or assertion of automatic spectral-triple regularity is used.

## References

- B. Blackadar, *K-Theory for Operator Algebras*, second edition, 1998, complete §3.1, especially Definition 3.1.1 and Examples 3.1.2, and §4.5, especially Proposition 4.5.1. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- A. Connes, *Noncommutative Geometry*, 1994, [III, Appendix C, Definitions and Propositions 1–3, pp. 291–292](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). We distinguish the matrix-calculus integration hypothesis from matrix inverse closure.
- L. B. Schweitzer, [*A Short Proof that \(M_n(A)\) is local if \(A\) is local and Fréchet*](https://arxiv.org/abs/funct-an/9211005), *International Journal of Mathematics* 3 (1992), 581–589, §§1–2, especially Lemma 1.2, Theorem 2.1, Corollary 2.3 and Remark 2.4.

- J. Roe, *Lectures on K-Theory and Operator Algebras*, Math 582, Spring 2017, Corollary 14.7 and its proof, pp. 66–67. [Freely readable author notes](https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/1/4020/files/2017/12/KTheoryNotes-1uvuwyz.pdf#page=66). Proposition 3.2 supplies the complete norm criterion, including unitizations, matrix estimates and contour integration. No source expression is adapted.

[Connes1994, stable topology] A. Connes, *Noncommutative Geometry*, III, complete AppendixC, pp.291–292, especially Proposition3(b). [Freely readable author edition](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Theorem2.3 gives a full independent proof for the explicitly defined final topology of spaces, including compact-stage reduction, stage topology, relative finite approximation and comparison with the norm union. It does not assume that an unspecified categorical group-limit has this topology or that scalar contour integrals in an incomplete algebra automatically stay in that algebra.
