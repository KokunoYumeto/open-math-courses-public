# Topological K-theory of spaces, pairs and vector bundles

*Written by GPT-6.1 Sol (OpenAI), October 2026, at Ultra. Public domain (CC0).*

Independently authored CC0 lesson; self-checked by the writing AI.

A bundle difference over a space becomes relative data when we specify how its two bundles agree on a closed subspace. That specified agreement can carry information even when the bundles themselves are trivial. We connect this description to operator K-theory, then compute integral groups with their actual generators.

All spaces are Hausdorff. We import the bundle–projection correspondence and transport along a cylinder from [Lesson 2, §§2–4](KT-OPK-02.md#2-finitely-many-coordinates-suffice), the natural suspension map \(\theta_A:K_1(A)\to K_0(SA)\) from [Lesson 8, Theorem 2.1](KT-OPK-08.md#2-the-idempotent-loop-of-an-invertible), Bott periodicity from [Lesson 10, Theorem 4.1 and §6](KT-OPK-10.md#4-the-boundary-proves-periodicity-and-fixes-its-sign), and the six-term sequence, Mayer–Vietoris and strong relative excision from [Lesson 11, Theorems 2.1, 4.1 and 6.1](KT-OPK-11.md). Tensor products are minimal, and all K-groups are complex.

## 1. Compact supports and the exact sequence of a pair

For compact \(X\), set \(K^{-n}(X)=K_n(C(X))\). For locally compact \(X\), use

\[
\begin{gathered}
K_c^{-n}(X)=K_n(C_0(X)),\\
n\geq0.
\end{gathered}
\tag{1.1}
\]

Here \(C_0(X)\) consists of continuous functions vanishing at infinity. If \(Y\subset X\) is closed, define

\[
K^{-n}(X,Y)=K_n(C_0(X\setminus Y)).
\tag{1.2}
\]

For noncompact \(X\), this relative notation includes compact supports. Two-periodicity extends the degrees to all integers; we write \(K^1=K^{-1}\). For compact \(X\), Lesson 2 and group completion identify \(K^0(X)\) with differences \([E]-[F]\) of finite-rank vector bundles. Its degree-one counterpart is the stable homotopy group of maps \(X\to U(N)\), by polar decomposition from Lesson 6.

**Lemma 1.1 (restriction).** For a locally compact \(X\) and closed \(Y\), restriction gives an exact sequence

\[
\begin{aligned}
0&\longrightarrow C_0(X\setminus Y)\xrightarrow{j}C_0(X)\\
&\xrightarrow{r}C_0(Y)\longrightarrow0.
\end{aligned}
\tag{1.3}
\]

The map \(j\) extends functions by zero.

*Proof.* Write \(X^+\) for the one-point compactification, adding a disjoint point if \(X\) is compact. The subspace \(Y\cup\{\infty\}\) is closed in \(X^+\). A function in \(C_0(Y)\), set equal to zero at infinity, is continuous there.

We recall the extension argument to avoid imposing normality on \(X\). A compact Hausdorff space is normal: separate each pair of points in two disjoint closed sets by disjoint open neighborhoods, and use compactness twice to obtain neighborhoods of the whole sets with disjoint closures. Normality gives a function separating two closed sets: choose open sets indexed by dyadic rationals with \(\overline{U_a}\subset U_b\) for \(a<b\), and take the infimum of the indices of the sets containing a point. The nested-closure condition proves continuity of this function and its prescribed values zero and one.

For a real function \(f\) on a closed subset, \(|f|\leq M\), apply this separation to the sets where \(f\leq-M/3\) and \(f\geq M/3\). It gives a function \(h\) on the compact ambient space with \(|h|\leq M/3\) and \(|f-h|\leq2M/3\) on the closed subset. Repeat for the residual. The successive extensions have norms at most \(M(2/3)^k/3\); their uniformly convergent sum extends \(f\). Apply this separately to real and imaginary parts on \(Y\cup\{\infty\}\). The resulting extension has value zero at infinity and belongs to \(C_0(X)\). Thus \(r\) is onto.

Its kernel consists of functions vanishing on \(Y\). Such a function restricts to an element of \(C_0(X\setminus Y)\): each set where its absolute value is at least \(\varepsilon>0\) is compact and disjoint from \(Y\). Conversely these compact level sets show that zero extension is continuous across \(Y\) and vanishes at infinity. They prove the kernel assertion and injectivity of \(j\). \(\square\)

The same normality construction gives the compact cutoffs used later in the course. If \(F\subset X\) is compact, local compactness gives finitely many open neighborhoods covering \(F\) whose closures in \(X\) are compact; let \(U\) be their union. Separate the disjoint closed sets \(F\) and \(X^+\setminus U\) in the compact space \(X^+\) by the dyadic construction above. Its function \(h\) satisfies \(0\leq h\leq1\), is one on \(F\), and is zero off \(U\). Its support is contained in the compact closure of \(U\) in \(X\), so \(h\in C_c(X)\). No normality of the noncompact space is assumed.

**Theorem 1.2 (pair sequence).** There is a natural exact cycle

\[
\begin{gathered}
K^0(X,Y)\xrightarrow{j_*}K_c^0(X)\\
\xrightarrow{r_*}K_c^0(Y)\xrightarrow{\varepsilon}K^1(X,Y)\\
\xrightarrow{j_*}K_c^1(X)\xrightarrow{r_*}K_c^1(Y)\\
\xrightarrow{\delta}K^0(X,Y).
\end{gathered}
\tag{1.4}
\]

Repeating it using periodicity gives, in every degree,

\[
\begin{gathered}
\cdots\longrightarrow K^{-n}(X,Y)\\
\longrightarrow K_c^{-n}(X)\longrightarrow K_c^{-n}(Y)\\
\longrightarrow K^{-n+1}(X,Y)\longrightarrow\cdots.
\end{gathered}
\tag{1.5}
\]

*Proof.* Apply Lesson 11, Theorem 2.1, to (1.3); it proves exactness at all six positions. The index boundary is \(\delta\); \(\varepsilon\) uses the positive formula \([e]\mapsto[\exp(2\pi ix)]\) with its normalized self-adjoint lift. Apply the natural periodicity identifications of Lesson 10 to repeat the cycle. This proves (1.5), including its boundary degrees. \(\square\)

A proper map \(f:X\to X'\) gives \(f^*:C_0(X')\to C_0(X)\), since inverse images of compact level sets are compact. If \(f(Y)\subset Y'\), it takes the relative ideal into the relative ideal and gives a morphism of (1.3); hence (1.4) is contravariantly natural for proper maps of pairs. A proper homotopy \(H:X\times[0,1]\to X'\) gives a norm-continuous homotopy of these algebra maps. Indeed its compact level sets control all tails uniformly, and continuity is uniform on the remaining compact set. Thus it induces homotopy invariance. Compact spaces require no extra properness condition.

For a nonempty compact pointed space \((X,x_0)\), evaluation at \(x_0\) splits by constants. Consequently

\[
\begin{aligned}
K^0(X)&=\mathbb Z[1]\oplus\widetilde K^0(X),\\
\widetilde K^0(X)&=\ker(\operatorname{ev}_{x_0})_*,\\
\widetilde K^1(X)&=K^1(X).
\end{aligned}
\tag{1.6}
\]

The first coordinate is the rank at the chosen point. On a disconnected space it is not the complete rank function. Likewise \(K_c^0(X)\) is the kernel of evaluation at infinity on \(K^0(X^+)\). Using bounded functions instead would give a different group; for example \(K_c^0(\mathbb R)=0\), whereas the constant unit in \(C_b(\mathbb R)\) has nonzero K-class, detected by evaluation at any point.

## 2. Specified bundle comparisons

Let \(X\) be compact and \(Y\) closed. Form a group \(\mathcal D(X,Y)\) generated by triples

\[
(E,F,\sigma),\qquad \sigma:E|_Y\xrightarrow{\cong}F|_Y.
\tag{2.1}
\]

Identify isomorphic triples, impose direct-sum addition, and identify the endpoints of a triple over \((X\times[0,1],Y\times[0,1])\). A triple is zero if its specified comparison extends to a bundle isomorphism over \(X\). These are the difference-bundle relations. The comparison is part of the data: it is not merely the statement that the restrictions have equal K-classes.

**Theorem 2.1 (difference bundles).** There is a natural isomorphism

\[
\mathcal D(X,Y)\xrightarrow{\cong}K^0(X,Y).
\tag{2.2}
\]

Its composite with \(j_*\) in (1.4) sends \((E,F,\sigma)\) to \([E]-[F]\).

*Proof.* Put \(A=C(X)\), \(J=C_0(X\setminus Y)\). Choose Hermitian metrics and finite isometric embeddings of \(E,F\) in trivial bundles, as in Lesson 2, §2. Pad with zero coordinates to a common size. Their range projections are \(p,q\in M_N(A)\). Replace \(\sigma\) by its polar isometry

\[
u=\sigma(\sigma^*\sigma)^{-1/2}.
\tag{2.3}
\]

The positive operator on \(E|_Y\) is uniformly bounded below on the compact base; its inverse square root is continuous. Interpolating the positive factor to identity homotopes \(\sigma\) to \(u\). Between the embedded ranges, \(u\) is a matrix \(v\) over \(C(Y)\) with

\[
v^*v=r(p),\qquad vv^*=r(q).
\tag{2.4}
\]

It gives a triple in \(R(A,J)\), the relative group defined in Lesson 11, §5.

Here are all the choice and relation checks. For two isometric embeddings \(i_0,i_1\) of a fixed bundle, place their targets in orthogonal free summands and use

\[
\begin{gathered}
i_t=\cos t\,i_0\oplus\sin t\,i_1,\\
0\leq t\leq\pi/2.
\end{gathered}
\tag{2.5}
\]

Since \(i_t^*i_t=I\), their projections and transported comparisons form a continuous relative-triple path. Zero padding and a scalar unitary path rearrange endpoint coordinates. Isomorphic geometric triples therefore give the same class. Metrics can be joined by convex interpolation; normalizing the embeddings and (2.3) continuously gives the same conclusion for metric choices. A geometric homotopy has finite embeddings over the compact cylinder, giving a relative projection homotopy. If \(\sigma\) extends, its global polar isometry gives an actual partial-isometry lift of \(v\), so the algebraic triple is degenerate. Direct sums are block sums. We obtain a homomorphism \(\mathcal D(X,Y)\to R(A,J)\).

Conversely, from \((p,q,v)\) take the range bundles of \(p,q\) and the isomorphism \(v\) on \(Y\). Lesson 2, §1, proves their local triviality. An algebraic homotopy gives these bundles over the cylinder; block addition gives direct sum; an actual partial-isometry lift extends the comparison over \(X\). Thus this reverse map respects every relation. Its composite on geometric triples recovers the original bundles and the polar comparison, homotopic to \(\sigma\). Its composite on algebraic triples recovers precisely \(p,q,v\). The two maps are inverse.

Finally Lesson 11, Theorem 6.1, supplies the choice-independent isomorphism \(\kappa:R(A,J)\to K_0(J)\), including injectivity. This proves (2.2). It also proves naturality, since projection pullbacks, polar parts and relative excision are natural. \(\square\)

The map can be computed in finite matrices. Set \(p'=p\oplus0\), \(q'=q\oplus0\). Lift to a unitary \(U\) over \(A\) the quotient completion

\[
W(v)=\begin{pmatrix}v&1-r(q)\\r(p)-1&v^*\end{pmatrix}.
\tag{2.6}
\]

Its identity-component path is given in Lesson 11, equation (5.5). Define

\[
\begin{gathered}
L=\begin{pmatrix}p'&-(1-p')\\1-p'&p'\end{pmatrix},\\
h=L\bigl(U^*q'U\oplus(1-p')\bigr)L^*,\\
P_0=\operatorname{diag}(I_{2N},0_{2N}).
\end{gathered}
\tag{2.7}
\]

Then \(h-P_0\in M_{4N}(J)\), and (2.2) is \([P_0]-[h]\) over the external \(J^+\). This formula remains valid for \(Y=\varnothing\); no embedding of \(J^+\) into \(A\) is presumed. In \(K_0(A)\) it equals \([p]-[q]\), proving the asserted forgetful formula.

**Lemma 2.2 (a boundary comparison).** For a unitary map \(u:Y\to U(N)\), the triple \((\mathbf1^N,\mathbf1^N,u)\) maps to \(\delta[u]\).

*Proof.* Choose a doubled unitary lift \(U\) of \(\operatorname{diag}(u,u^*)\), and let \(Q=\operatorname{diag}(I_N,0_N)\). The reduction (2.7), whose remaining complementary rotation is scalar in this case, gives \([Q]-[U^*QU]\). The matrix \(U^*\) is a doubled lift for \(u^*\), so the index formula of Lesson 7 gives \([U^*QU]-[Q]=\delta[u^*]\). Since \([u^*]=-[u]\), the claimed class is \(\delta[u]\). \(\square\)

**Theorem 2.3 (Collapsing a contractible closed subspace).** Let \(X\) be compact Hausdorff and let \(Y\subset X\) be nonempty, closed and contractible. For every \(n\geq0\), the quotient map \(q:X\to X/Y\) induces a bijection

\[
\begin{gathered}
q^*:\operatorname{Vect}_n(X/Y)\\
\longrightarrow\operatorname{Vect}_n(X).
\end{gathered}
\tag{2.8}
\]

These are isomorphism classes of complex bundles. The bijections preserve direct sums and pullbacks along maps of such pairs. In both degrees, \(q^*:K^i(X/Y)\to K^i(X)\) is an isomorphism. No neighborhood retraction or cofibration assumption is needed.

*Proof.* The quotient is compact Hausdorff: points outside \(Y\) have disjoint neighborhoods from \(Y\) by normality, and two distinct outside points have disjoint neighborhoods avoiding \(Y\). These give the required separated quotient neighborhoods. The case \(n=0\) is immediate; assume \(n>0\).

Every rank-\(n\) bundle \(E\to X\) is trivial on \(Y\), by [Lesson 2, Corollary 4.3](KT-OPK-02.md#4-transport-along-a-cylinder). Choose a frame there, equivalently a trivialization \(h:E|_Y\to Y\times\mathbb C^n\). This frame extends to a frame on a neighborhood \(U\) of \(Y\). Indeed embed \(E\) as the range of a finite continuous projection \(p:X\to M_N(\mathbb C)\), by Lesson 2, Theorem 2.1. Extend each coordinate of each frame vector from \(Y\) to \(X\), using the extension proof in Lemma 1.1, and multiply by \(p(x)\). These are sections of \(E\) that retain the prescribed frame on \(Y\). Their Gram determinant is positive on \(Y\), hence on an open neighborhood \(U\); since the fiber rank is \(n\), they are a basis there. The resulting trivialization extends exactly \(h\).

Form \(E/h\) by identifying two vectors over \(Y\) when \(h\) assigns them the same vector in \(\mathbb C^n\). It is a bundle over \(X/Y\). Outside the collapsed point its charts are those of \(E\); over \(U/Y\), the extended frame gives the chart \((U/Y)\times\mathbb C^n\). Here is the quotient-topology check for that chart. The map \(U\to U/Y\) is closed: the saturation of a closed subset is either that subset or its union with the closed compact set \(Y\). Its fibers are compact. Its product with the identity on \(\mathbb C^n\) is therefore also closed. To see this directly, for a point outside the image of a closed subset of \(U\times\mathbb C^n\), cover the compact fiber by finitely many product neighborhoods disjoint from that subset, intersect their neighborhoods in \(\mathbb C^n\), and use closedness of \(U\to U/Y\) to shrink the base neighborhood whose inverse image lies in their union. Thus the product map is a quotient map, proving the asserted chart homeomorphism. Charts over \(U\) and outside \(Y\) agree by the original transition maps. The quotient construction yields an isomorphism

\[
q^*(E/h)\cong E.
\tag{2.9}
\]

It is the fiberwise quotient map, which in the extended-frame chart is the identity on the vector coordinate.

The isomorphism class of \(E/h\) is independent of the frame. For two trivializations \(h_0,h_1\), their ratio is a continuous map \(g:Y\to\operatorname{GL}_n(\mathbb C)\). A contraction of \(Y\) homotopes \(g\) to a constant matrix. Every invertible complex matrix has a path to the identity: polar deformation reduces it to a unitary, and a finite-dimensional self-adjoint logarithm gives that path. Thus \(g\) is homotopic to the identity. Multiplying \(h_0\) by this homotopy gives a continuous family of trivializations \(h_s\) joining \(h_0\) and \(h_1\). Apply the preceding frame-extension and quotient construction to \(E\times[0,1]\) over \(X\times[0,1]\), with its frame on the closed subset \(Y\times[0,1]\), collapsing each \(Y\times\{s\}\) separately. The resulting bundle lies over \((X/Y)\times[0,1]\). The base map \(q\times\operatorname{id}\) is a closed quotient map with precisely these fibers, by the same compact-fiber argument. Its endpoint bundles are \(E/h_0\) and \(E/h_1\). Lesson 2, Theorem 4.2, makes them isomorphic.

Isomorphic bundles give isomorphic quotients after transporting the frame, so \(E\mapsto E/h\) is well defined on isomorphism classes. Equation (2.9) proves one inverse identity. If \(F\to X/Y\) is a bundle, \(q^*F\) has its canonical frame over \(Y\), obtained by choosing a basis of the fiber at the collapsed point. Quotienting with that frame recovers \(F\), chart by chart. This proves the other inverse identity and hence (2.8). Block frames give direct-sum compatibility. Pullback compatibility follows from the commuting quotient square and the bijections just proved: pullbacks of bundles along the two routes agree before and after applying the injective quotient pullback.

For \(K^0\), an arbitrary finite-rank bundle has finitely many clopen rank strata. Since the nonempty contractible space \(Y\) is connected, it lies in one stratum. Apply (2.8) there and leave all other strata unchanged; their quotient images remain clopen. Group completion therefore gives the asserted \(K^0\) isomorphism.

For \(K^1\), contractibility and homotopy invariance give \(K^1(Y)=0\) and \(K^0(Y)=\mathbb Z\). Restriction \(K^0(X)\to K^0(Y)\) is onto, since the trivial line maps to its generator. The exact cycle (1.4) consequently gives \(K^1(X,Y)\cong K^1(X)\). Evaluation at the collapsed point of \(X/Y\) has kernel \(C_0(X\setminus Y)\) and a scalar section. Its degree-one sequence gives \(K^1(X/Y)\cong K^1(X,Y)\), because the scalar degree-one group is zero and the degree-zero evaluation is onto. The composite is exactly \(q^*\), by the commuting ideal inclusions. This proves the second-degree assertion. \(\square\)

This is the unstable quotient result of [Hatcher, Lemma 2.10, printed p. 53](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf#page=57), with its compact Hausdorff and closed-subspace hypotheses explicit. The frame-extension and quotient-topology details also justify its use without a neighborhood deformation retraction.

## 3. Disc bundles, sphere bundles and a trivial Thom class

Let \(V\to X\) be a finite-rank Hermitian vector bundle over compact \(X\), and write \(B(V),S(V)\) for its closed unit disc and unit sphere bundles. They are compact: finite trivializations over compact closed subsets of the base reduce this to compact Euclidean discs. The radial map

\[
\begin{aligned}
V&\longrightarrow B(V)\setminus S(V),\\
v&\longmapsto\frac{v}{\sqrt{1+\|v\|^2}}
\end{aligned}
\tag{3.1}
\]

is a homeomorphism, with inverse \(w\mapsto w/\sqrt{1-\|w\|^2}\). A homeomorphism is proper, since its inverse takes compact sets to compact sets. Function pullback therefore proves, in both degrees,

\[
\begin{gathered}
\boxed{K_c^i(V)=K^i(B(V),S(V))},\\
i=0,1.
\end{gathered}
\tag{3.2}
\]

For rank zero, \(S(V)\) is empty and (3.2) is just \(K^i(X)=K^i(X,\varnothing)\). Together with Theorem 2.1, this is the disc/sphere difference-bundle definition used in [Hilbert modules and fields on the leaf space, Theorem 6.6](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/preparation.html#dependency-8c424e02f290). The homeomorphism proves the identification without an analytic index argument.

For a trivial real bundle of dimension \(d\), the relative ideal is \(C_0(\mathbb R^d,C(X))\). The suspension isomorphisms already proved give

\[
\begin{gathered}
K^i(X\times D^d,X\times S^{d-1})\\
\cong K^{i+d}(X).
\end{gathered}
\tag{3.3}
\]

with degrees modulo two. For \(d=0\), take \(S^{-1}=\varnothing\). In particular \(K^0(D^{2r},S^{2r-1})=\mathbb Z\) and \(K^1(D^{2r},S^{2r-1})=0\).

**Theorem 3.1 (the trivial complex line).** For compact \(X\), let \(\pi:X\times D^2\to X\) and let \(z\) be the complex coordinate on its boundary. The assignment

\[
E\longmapsto(\pi^*E,\pi^*E,z\,\mathrm{id}_E)
\tag{3.4}
\]

extends by bundle differences to an isomorphism \(K^0(X)\to K_c^0(X\times\mathbb C)\). For a point its value on the trivial line is the positive planar Bott class.

*Proof.* For a point, Lemma 2.2 identifies the triple with the disc-extension boundary \(\delta[z]\). Lesson 11, Example 3.3, computes this boundary as the positive class

\[
\begin{gathered}
q(\zeta)=\frac1{1+|\zeta|^2}
\begin{pmatrix}1&\overline\zeta\\\zeta&|\zeta|^2\end{pmatrix},\\
\mathfrak b=[q]-[P],\qquad P=\operatorname{diag}(0,1).
\end{gathered}
\tag{3.5}
\]

The disc interior is identified with the plane by (3.1), preserving its complex orientation. Lesson 10, equation (6.4), identifies \(\mathfrak b\) with \(\theta_{S\mathbb C}\beta_{\mathbb C}[1]\).

For \(E\) represented by a projection \(e\in M_N(C(X))\), use the possibly nonunital *-homomorphism \(\lambda\mapsto\lambda e\) from \(\mathbb C\) to \(M_N(C(X))\). Applied pointwise to the scalar disc pair, it sends the scalar comparison triple to (3.4) on the range bundle of \(e\). Naturality of \(\kappa,\theta,\beta\), followed by matrix stability, identifies its class with

\[
\mathsf B_{C(X)}[e]=\theta_{SC(X)}\beta_{C(X)}[e].
\tag{3.6}
\]

Both constituent maps are natural isomorphisms. Direct sums of (3.4) agree with sums of classes, so group completion extends the assignment; (3.6) proves that extension is well-defined and bijective on all bundle differences. This proves the theorem, including its sign. \(\square\)

Iterating (3.6) computes trivial complex bundles of any rank. Formula (3.2) applies also to nontrivial \(V\); a general Thom isomorphism for those bundles requires a further theorem, which is not asserted here.

## 4. Spheres and concrete generators

Put \(D_d=C_0(\mathbb R^d)\). Lesson 10, Corollary 6.1, proves \(K_i(D_d)=\mathbb Z\) when \(i\equiv d\pmod2\) and zero otherwise. Here is a finite-matrix specification of generators in every dimension. Begin with \(b_0=[1]\). Recursively set

\[
\begin{aligned}
b_{2m+2}&=\theta_{SD_{2m}}\beta_{D_{2m}}(b_{2m}),\\
b_{2m+1}&=\beta_{D_{2m}}(b_{2m}).
\end{aligned}
\tag{4.1}
\]

Use \(SD_d=D_{d+1}\), with each new real coordinate first and \(x=-\cot(\pi t)\). These are generators because each displayed map is an isomorphism.

For clarity, (4.1) supplies actual representatives, rather than only an unnamed generator. If \(b_{2m}=[e]-[P]\), the odd representative is

\[
\begin{aligned}
u(t)&=\bigl(z(t)e+I-e\bigr)\\
&\qquad\cdot\bigl(\overline{z(t)}P+I-P\bigr),\\
z(t)&=e^{2\pi it}.
\end{aligned}
\tag{4.2}
\]

It has scalar part and endpoint values identity. To make the next even representative, set \(Q=\operatorname{diag}(I,0)\) and

\[
\begin{gathered}
Z_a=\operatorname{diag}(u,I)R_a
\operatorname{diag}(I,u^*)R_a^*,\\
R_a=\begin{pmatrix}\cos a\,I&-\sin a\,I\\
\sin a\,I&\cos a\,I\end{pmatrix},\\
a=\tfrac\pi2(1-s).
\end{gathered}
\tag{4.3}
\]

Then \([Z_aQZ_a^*]-[Q]\) is the first line of (4.1), by Lesson 8, equations (2.2)–(2.3). All operations are in finite matrices; both boundary values are \(Q\). In dimension two this is the class (3.5).

**Theorem 4.1.** For \(n\geq0\),

\[
\begin{array}{c|cc}
&K^0(S^n)&K^1(S^n)\\\hline
n\text{ even}&\mathbb Z^2&0\\
n\text{ odd}&\mathbb Z&\mathbb Z
\end{array}
\tag{4.4}
\]

For positive even \(n\), a basis of \(K^0\) is \([1]\) and the extension of \(b_n\); for odd \(n\), the degree-one generator is the extension of the normalized unitary representing \(b_n\).

*Proof.* Regard \(S^n\) as \((\mathbb R^n)^+\), with point \(\infty\). Evaluation there gives the split extension

\[
\begin{aligned}
0&\longrightarrow D_n\longrightarrow C(S^n)\\
&\xrightarrow{\operatorname{ev}_\infty}\mathbb C\longrightarrow0.
\end{aligned}
\tag{4.5}
\]

Split exactness identifies its K-groups with those of \(D_n\) plus \(K_*(\mathbb C)\). The latter are \(\mathbb Z[1]\) and zero. The parity calculation for \(D_n\) proves (4.4). In even degree the equal-scalar projection difference extends over infinity; in odd degree (4.2) extends by identity. Injectivity of the ideal map and the constant splitting prove that the stated classes are bases. For \(n=0\), the two points instead have the basis of their characteristic projections; equivalently use \([1]\) and the characteristic projection of the point different from \(\infty\). \(\square\)

For \(S^1\), the unitary is the positive winding coordinate. For \(S^2\), the reduced generator is \([q]-[P]\). For \(S^3\), take (4.2) with \(e=q(\zeta)\) and \(P\) from (3.5). This gives an explicit two-by-two unitary over the one-point compactification of \(\mathbb R\times\mathbb C\); its behavior at infinity follows from \(q(\zeta)-P\to0\) uniformly in the loop variable, together with its identity limits at the two loop endpoints. Its class generates \(K^1(S^3)\).

### An explicit unstable projection example

For this example we also use the continuous projection retraction and stable projection homotopy from [Lesson 1, Theorems 4.1 and 4.3](KT-OPK-01.md).

**Proposition 4.2.** There are unitarily equivalent rank-one projections in \(M_2(C(S^3))\) which cannot be joined by a projection homotopy in that same algebra. They cannot be joined by an idempotent homotopy there either.

*Proof.* Take the two-by-two unitary \(U\) just constructed, whose class generates \(K^1(S^3)\). Put

\[
e=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad p=UeU^*.
\tag{4.6}
\]

Both are rank-one projections, and their unitary equivalence is explicit. Suppose there were a norm-continuous projection path \(p_t\) from \(e\) to \(p\). We first lift it to a unitary path with initial value the identity. For projections \(a,b\) of distance less than one, set

\[
\begin{gathered}
x=ba+(1-b)(1-a),\\
v(b,a)=x(x^*x)^{-1/2}.
\end{gathered}
\tag{4.7}
\]

Indeed \(x-1=(b-a)(2a-1)\), so \(x\) is invertible by the Neumann criterion. The equation \(xa=bx\) makes \(x^*x\) commute with \(a\). Thus its polar unitary satisfies \(v(b,a)av(b,a)^*=b\), depends continuously on \(b\), and equals one when \(b=a\). Subdivide the path into intervals on which \(\|p_t-p_{t_j}\|<1\). Starting with \(W_0=1\), define \(W_t=v(p_t,p_{t_j})W_{t_j}\) on each interval. These formulas agree at endpoints and give a continuous unitary path with \(W_t eW_t^*=p_t\).

At the final endpoint, \(D=U^*W_1\) commutes with \(e\). Therefore

\[
\begin{gathered}
D=\operatorname{diag}(f,g),\\
f,g:S^3\longrightarrow\mathbb T.
\end{gathered}
\tag{4.8}
\]

Each scalar map has a continuous real logarithm. Here is the elementary topological justification. Every loop in \(S^3\) is homotopic, by normalized straight interpolation, to a sufficiently close finite geodesic polygon. That polygon misses some point of the sphere: its finitely many arcs lie in finitely many proper two-dimensional linear subspaces of \(\mathbb R^4\). The complement of a point is homeomorphic to \(\mathbb R^3\), so the polygon contracts. Hence \(S^3\) is simply connected. Fix an argument at one base point and extend it along a path using local circle arguments. Two paths give the same endpoint argument because their concatenation is a contractible loop, whose image has winding zero. Local arguments then prove that the resulting logarithm is continuous. This applies to both \(f\) and \(g\).

Write \(f=\exp(2\pi ih)\) and \(g=\exp(2\pi ik)\), with continuous real \(h,k\). Scaling both logarithms to zero contracts \(D\) to the identity. The path \(W_t\) already contracts \(W_1\) to the identity. Since \(U=W_1D^*\), multiplying these two paths would contract \(U\), giving \([U]=0\) in \(K^1(S^3)\). This contradicts its generating property.

Finally a path of idempotents with these projection endpoints would become a path of projections under the continuous projection retraction of Lesson 1, Theorem 4.1. That retraction fixes projections, so the contradiction applies to idempotent paths as well. \(\square\)

This gives the explicit construction behind the similar, nonhomotopic idempotents mentioned early in the course. The obstruction is unstable: stabilizing the projections makes their algebraic equivalence into a projection homotopy by the rotation construction of Lesson 1, Theorem 4.3. Their \(K_0\) classes are already equal; the nonzero class used to obstruct the two-by-two homotopy is a \(K_1\) class.

## 5. Adding circles, with arbitrary coefficients

Let \(A\) be any C*-algebra, including nonunital. Evaluation at \(1\in\mathbb T\) in

\[
\begin{aligned}
0&\longrightarrow SA\xrightarrow{j}C(\mathbb T,A)\\
&\xrightarrow{r}A\longrightarrow0
\end{aligned}
\tag{5.1}
\]

splits by the constant map \(c\). The suspension is identified using \(z(t)=e^{2\pi it}\). The usual identification \(C(\mathbb T)\otimes A=C(\mathbb T,A)\) follows by finite partitions of unity and approximation by finite sums of scalar functions times elements of \(A\); the minimal norm is their supremum norm in a faithful representation.

**Theorem 5.1 (circle with coefficients).** Set

\[
\begin{aligned}
\alpha_0&=\theta_A:K_1(A)\to K_0(SA),\\
\alpha_1&=\beta_A:K_0(A)\to K_1(SA).
\end{aligned}
\tag{5.2}
\]

For \(i=0,1\), the natural isomorphism is

\[
\begin{gathered}
K_i(A)\oplus K_{1-i}(A)\\
\xrightarrow{\cong}K_i(C(\mathbb T,A)),\\
(a,b)\longmapsto c_*a+j_*\alpha_i b.
\end{gathered}
\tag{5.3}
\]

*Proof.* The split extension (5.1) gives \(K_i(C(\mathbb T,A))=c_*K_i(A)\oplus j_*K_i(SA)\). Both maps in (5.2) are isomorphisms, proving (5.3). Explicitly the inverse first takes \(r_*x\); the remainder \(x-c_*r_*x\) has zero evaluation and has a unique antecedent under the injective \(j_*\). Apply \(\alpha_i^{-1}\) to that antecedent. Constants, evaluation, ideal inclusion and \(\alpha_i\) all commute with arbitrary *-homomorphisms. This proves naturality and the nonunital case. \(\square\)

**Corollary 5.2 (tori).** For \(n\geq1\),

\[
K^0(\mathbb T^n)\cong K^1(\mathbb T^n)
\cong\mathbb Z^{2^{n-1}}.
\tag{5.4}
\]

*Proof with generators.* Start with the basis \([1]\) in degree zero on a point and the empty degree-one basis. Add the circle coordinates in the order \(1,\ldots,n\). For each subset \(I\subset\{1,\ldots,n\}\), construct \(g_I\) recursively: if \(n\notin I\), take the constant extension of its preceding class; if \(n\in I\), take \(j_*\alpha_i\) of \(g_{I\setminus\{n\}}\), where \(i\equiv|I|\pmod2\). Theorem 5.1 says these classes form a basis, partitioned by even and odd cardinality. There are \(2^{n-1}\) subsets of each parity: toggling the first element is a bijection between them, and together they exhaust the \(2^n\) subsets. This proves both the ranks and the specified basis. Each step has the finite projection or unitary formulas (4.2)–(4.3). For \(n=0\) the groups are those of a point, so (5.4) is not meant in that case. \(\square\)

On the two-torus, the degree-one basis is \([z_1],[z_2]\), and the degree-zero basis is \([1],g_{\{1,2\}}\). A concrete projection for the latter is \(q(x_2+ix_1)\), where

\[
\begin{gathered}
z_k=e^{2\pi it_k},\\
x_k=-\cot(\pi t_k),\qquad 0<t_k<1.
\end{gathered}
\tag{5.5}
\]

Extend it by \(P\) when either \(z_k=1\), and subtract \([P]\). The extension is continuous, since \(q-P\to0\) when either real coordinate tends to infinity. The coordinate order in (5.5) is new outer coordinate \(2\), then inner coordinate \(1\). Naturality of \(\theta\) and the inclusion of the first circle's ideal identifies this class with \(j_*\theta_{C(\mathbb T)}[z_1]\), exactly the recursive \(g_{\{1,2\}}\). Reversing the real-coordinate order would negate this generator. The computation used a split extension at each stage and does not require a Künneth theorem or a calculation of the ring structure.

## 6. What rational information sees

Write \(H^{\mathrm{ev}}(X;\mathbb Q)=\bigoplus_{k\geq0}H^{2k}(X;\mathbb Q)\), and use \(H^{\mathrm{odd}}\) for the analogous odd sum. Here cohomology is ordinary cohomology. For a finite CW complex these sums have finitely many nonzero terms.

**Theorem 6.1 (rational Chern character).** There are natural isomorphisms

\[
\begin{aligned}
\operatorname{ch}_0:K^0(X)\otimes\mathbb Q
&\xrightarrow{\cong}H^{\mathrm{ev}}(X;\mathbb Q),\\
\operatorname{ch}_1:K^1(X)\otimes\mathbb Q
&\xrightarrow{\cong}H^{\mathrm{odd}}(X;\mathbb Q)
\end{aligned}
\tag{6.1}
\]

for every finite CW complex \(X\). They also give reduced and relative isomorphisms for finite CW pairs. The even character is a ring homomorphism for tensor products of bundles. We construct both maps and prove the theorem below, including the signs relating them to this course's boundaries. See [Blackadar 1998, Theorem 1.6.6, printed p. 7] for the statement; [Hatcher, §3.1, Theorem 3.2, Proposition 3.3 and Proposition 3.10](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf#page=82) for the projective-bundle construction, splitting and line arithmetic; and [Hatcher, §4.1, Propositions 4.2–4.5](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf#page=113) for the rational character and finite-cell proof. The characteristic-class axioms are also compared in [Weibel, Chern axioms].

### Line classes and projective spaces

We recall the cohomological conventions used in the construction. Relative cochains are cochains vanishing on the subspace; lifting a cocycle and taking its coboundary defines the connecting map \(\delta_H\). Cup products have the usual graded sign. The relative cup product lands in the relative group for the union of the two subspaces when those subspaces form an excisive pair, in particular for two open sets. This follows by subdividing singular simplices into that open cover before using the cup formula. For CW pairs, cohomology of the quotient is reduced relative cohomology. The cellular cochain groups have one generator per cell, with differential given by the incidence degrees. These descriptions give the pair sequence and the cell computations used here directly from cochain complexes.

Let \(\eta_2\) evaluate to one on the complex-oriented sphere \(\mathbb{CP}^1\). Complex projective space has one cell in each dimension \(0,2,\ldots,2m\): filter by the coordinate subspaces, whose successive complements are \(\mathbb C^j\). Thus its integral cohomology is \(\mathbb Z\) in these even degrees and zero elsewhere. If \(h\) restricts to \(\eta_2\), then

\[
\begin{gathered}
H^*(\mathbb{CP}^m;\mathbb Z)
=\mathbb Z[h]/(h^{m+1}),\\
|h|=2.
\end{gathered}
\tag{6.2}
\]

Here is the product check in (6.2). A coordinate hyperplane has an oriented normal complex disc. Its relative normal-disc class extends by zero to a class in projective space. To see that this disc class exists with integral coefficients, filter the normal disc bundle by the cells of the hyperplane. After its sphere boundary is collapsed, there is one relative cell two dimensions above each base cell. Its incidence number is the base incidence number: a complex linear change of normal coordinate preserves the oriented disc generator. The resulting relative cochain complex is the base cochain complex shifted by two, and the constant degree-zero class gives the normal-disc class. In a neighborhood of the hyperplane the normal coordinate is the omitted homogeneous coordinate divided by a nonzero coordinate; these neighborhoods give the normal bundle just used.

The hyperplane class restricts to a projective line as one positive transverse point, so it is \(h\). Choose \(j\) transverse coordinate hyperplanes. The cup product of their disc classes is the class of their intersection, since in local normal coordinates it is the product of \(j\) positively oriented two-disc generators. Restricting to a transverse \(\mathbb{CP}^j\) gives one positive point. Consequently \(h^j\) evaluates to one on that \(\mathbb{CP}^j\), proving it generates the degree \(2j\) group. This proves the ring assertion and its orientation, including compatibility under the standard inclusions of projective spaces.

For a line bundle \(L\) over a compact base, choose a finite isometric embedding into a trivial bundle, as in Lesson 2. Its range lines define \(f:X\to\mathbb{CP}^{N-1}\). Define

\[
c_1(L)=f^*(-h).
\tag{6.3}
\]

Two embeddings, placed in orthogonal coordinate blocks, are joined by the isometric path (2.5). Their line maps are therefore homotopic after zero padding. The compatibility just proved for \(h\) makes (6.3) independent of the embedding. Isomorphic bundles give the same class, and pullback embeddings prove naturality. A bundle on a cylinder has a finite embedding on that cylinder, so endpoint restrictions prove homotopy invariance as well.

**Lemma 6.2 (line arithmetic).** For line bundles,

\[
\begin{aligned}
c_1(L\otimes M)&=c_1(L)+c_1(M),\\
c_1(L^*)&=-c_1(L).
\end{aligned}
\tag{6.4}
\]

*Proof.* The Segre map takes two lines to their tensor-product line in the tensor product of their coordinate spaces. In degree two, the cellular cohomology of the product of two projective spaces is the direct sum of the degree-two groups of its factors; all its cells have even dimension. The pullback of \(-h\) by the Segre map restricts to \(-h\) on each factor, since fixing the other line gives a complex linear projective inclusion. It is therefore the sum of those two classes. Apply the classifying maps from the chosen embeddings. The trivial line has a constant map and class zero. Finally \(L\otimes L^*\) is trivial, giving the second assertion. \(\square\)

In particular, the range of the planar projection (3.5) is the tautological line with fibre \(\mathbb C(1,\zeta)\) on \(\mathbb{CP}^1\). With \(\zeta=x+iy\), its first Chern class is \(-\eta_2\). Thus the positive Bott class fixed by our boundary formulas has first Chern number \(-1\). The word “positive” in that convention specifies its clutching and boundary sign.

### Higher classes from one polynomial relation

Let \(E\) have constant rank \(r>0\), let \(\pi:P(E)\to X\) be its bundle of lines, and let \(S\subset\pi^*E\) be its tautological line. Put \(u=c_1(S)\).

**Lemma 6.3 (projective bundle and splitting).** The map

\[
\begin{gathered}
\bigoplus_{j=0}^{r-1}H^{n-2j}(X;\mathbb Z)\\
\longrightarrow H^n(P(E);\mathbb Z),\\
(a_j)_j\longmapsto\sum_j\pi^*a_j\,u^j.
\end{gathered}
\tag{6.5}
\]

is an isomorphism for a finite CW base, and for a compact Hausdorff base of finite CW homotopy type. In particular \(\pi^*\) is injective. Iterated projective bundles give a map \(F(E)\to X\) injective on cohomology under which \(E\) becomes a sum of line bundles.

*Proof.* Filter the base by its cells. A bundle on a characteristic disc is trivial: contract that disc and apply the cylinder transport of Lesson 2. Over a newly attached \(d\)-cell, the relative quotient of the total projective bundle by its preceding part is

\[
(D^d\times\mathbb{CP}^{r-1})/
(\partial D^d\times\mathbb{CP}^{r-1}).
\tag{6.6}
\]

Its relative cellular cochains are the fibre cochains shifted by \(d\). The restriction of \(u\) is \(-h\), so multiplication by \(1,u,\ldots,u^{r-1}\) identifies the direct sum of the base relative groups with these relative groups, integrally, by (6.2). For several cells the quotients and the relative groups are finite wedges and direct sums of these pieces.

Now compare the cohomology sequences of the base filtration pair and the total-space filtration pair, using (6.5) in every degree and the analogous relative maps. Multiplication by a globally defined even-degree class commutes with their connecting maps, by the cochain coboundary formula. The relative maps are isomorphisms as just computed. Beginning with a finite set of vertices, induction and the five lemma give (6.5) at each finite stage. The five lemma here is the elementary exact-row diagram chase: surjectivity at the middle follows by lifting its image on the right and then its residual on the left; injectivity follows by first representing a kernel element from the left and then subtracting the image of the preceding term. The isomorphisms at the four other positions justify those two corrections.

The total space has finite CW homotopy type. Indeed it is obtained by finitely many gluings of the products in (6.6) before quotienting. Both fibre and disc are finite CW spaces, their boundary inclusions are cofibrations, and replacing their attaching maps by homotopic cellular maps gives finite CW models of the same homotopy type. Cylinder transport identifies bundles pulled back along homotopy inverses, so the argument also applies to compact Hausdorff bases of finite CW homotopy type.

The coefficient of the basis element \(1\) proves injectivity of \(\pi^*\). Choose a Hermitian metric and split \(\pi^*E=S\oplus S^\perp\). Repeat the construction with \(S^\perp\), whose rank is smaller. Each pullback is injective by the first part; after finitely many steps the bundle splits into lines. Pulling back one such construction after another splits any prescribed finite collection of bundles while preserving injectivity. \(\square\)

There are therefore unique classes \(c_j(E)\in H^{2j}(X;\mathbb Z)\) defined by

\[
\begin{gathered}
u^r+\sum_{j=1}^r(-1)^j a_j u^{r-j}=0,\\
a_j=\pi^*c_j(E).
\end{gathered}
\tag{6.7}
\]

Set \(c_0=1\), and set \(c_j=0\) for \(j>r\); the rank-zero bundle has total class one. The degree and uniqueness in (6.5) prove existence and uniqueness of these coefficients. Pulling back (6.7) proves naturality by that same uniqueness. For rank one, \(P(E)=X\) and the relation gives exactly (6.3).

We check the sum formula rather than assume it. Write the left polynomial of (6.7) as \(w_E(u)\). In \(P(E\oplus F)\) the open complement of \(P(F)\) retracts onto \(P(E)\) by

\[
\begin{gathered}
\bigl[(e,f)\bigr]\longmapsto\bigl[(e,(1-t)f)\bigr],\\
e\ne0.
\end{gathered}
\tag{6.8}
\]

This homotopy stays over \(X\). Its endpoint factors through the retraction onto \(P(E)\), so ordinary cohomological homotopy invariance identifies the restricted class \(u\) with the pullback of its restriction to \(P(E)\). The classes \(\pi^*c_j(E)\) also stay fixed, since the homotopy stays over the base. Consequently \(w_E(u)\) restricts to zero on that open set, by its defining relation on \(P(E)\). Likewise \(w_F(u)\) vanishes on the open complement of \(P(E)\). Lift the two classes to the relative groups for their respective open sets. Their relative cup product lies in the group relative to the union, which is the whole space, and is zero. Hence \(w_E(u)w_F(u)=0\). It is a monic polynomial of the correct degree, so uniqueness of (6.7) gives

\[
\begin{gathered}
c(E\oplus F)=c(E)c(F),\\
c(E)=\sum_{j=0}^r c_j(E).
\end{gathered}
\tag{6.9}
\]

Zero ranks cause no exception, since their polynomial is one. On the splitting space in Lemma 6.3, if \(E=\bigoplus L_i\) and \(x_i=c_1(L_i)\), (6.9) identifies \(c_j(E)\) with the elementary symmetric polynomial in the \(x_i\).

### The even character and its Bott normalization

Define polynomials \(p_k\) recursively by

\[
\begin{aligned}
p_k&=\sum_{j=1}^{k-1}(-1)^{j-1}c_jp_{k-j}\\
&\quad+(-1)^{k-1}k c_k,\qquad k\geq1.
\end{aligned}
\tag{6.10}
\]

For a bundle of rank \(r\), substitute its classes and define

\[
\begin{gathered}
\operatorname{ch}_0(E)
=r+\sum_{k\geq1}\frac{p_k(E)}{k!},\\
p_k(E)=p_k(c_1(E),\ldots,c_k(E)).
\end{gathered}
\tag{6.11}
\]

The sum is finite in cohomology, since the base has finite CW homotopy type. On a splitting space, these polynomials are \(p_k=\sum_i x_i^k\). To verify the recursion, differentiate \(\prod_i(1+x_i t)\), divide by that product as a formal power series, and compare coefficients with \(\sum_{k\geq1}(-1)^{k-1}(\sum_i x_i^k)t^{k-1}\). This proves the identity over the integers, so

\[
\begin{gathered}
\operatorname{ch}_0(E)=\sum_i e^{x_i}\\
\text{after splitting}.
\end{gathered}
\tag{6.12}
\]

The exponentials are truncated by cohomological degree. A common splitting space for \(E,F\) shows that (6.11) is additive on direct sums. For tensor products, Lemma 6.2 gives roots \(x_i+y_j\), and
\(\sum_{i,j}e^{x_i+y_j}=(\sum_i e^{x_i})(\sum_j e^{y_j})\). Cohomological injectivity of the splitting map brings both identities back to the original base. Therefore
\(\operatorname{ch}_0([E]-[F])=\operatorname{ch}_0(E)-\operatorname{ch}_0(F)\)
is a well-defined natural ring homomorphism on the bundle Grothendieck group, hence on \(K^0(X)\) by Lesson 2. Rank functions handle disconnected bases component by component. Pullback and cylinder embeddings prove homotopy invariance. Restriction to a point is rank, so the map restricts to reduced groups.

For a pointed space \(T\), let \(\Sigma T=S^1\wedge T\); orient the suspension coordinate increasingly, and put it first. Write \(\sigma\) for the ordinary reduced cohomological suspension. It can be constructed by taking the relative product with the positive class of \(([0,1],\{0,1\})\) and collapsing the boundary. Its cochain construction gives a natural isomorphism, with degrees shifted by one. Relative groups of \((X,Y)\) are those of \(T=X/Y\); if \(Y\) is empty use \(T=X_+\). The ideal defining (1.2) is exactly the kernel at the quotient base point, so this reduced interpretation agrees with operator K-theory.

For the planar Bott class \(\mathfrak b\), (6.3) and (6.11) give

\[
\begin{aligned}
\operatorname{ch}_0(\mathfrak b)&=-\eta_2,\\
\operatorname{ch}_0(\mathsf B x)&=-\sigma^2\operatorname{ch}_0(x).
\end{aligned}
\tag{6.13}
\]

To justify the second formula for every reduced class, first work on \(S^2\times T\). Theorem 3.1 and its nonunital projection-corner proof identify \(\mathsf B[E]\) with the external bundle difference \(\mathfrak b\otimes E\). Subtracting bundles gives the same identity for every virtual class. Multiplicativity just proved computes its character as \(-\eta_2\) times the character of that class. If the class is reduced, both this K-class and its cohomology class vanish on the two base-point faces. They determine unique classes on \(S^2\wedge T\): in both pair sequences the restriction to \(S^2\vee T\) is surjective, since its reduced summands extend by the two projections from the product. Consequently the quotient pullbacks are injective. This proves (6.13) on the smash product, including its sign. It uses an external product with this particular Bott difference, rather than a Künneth theorem.

### Odd classes and both connecting maps

On \(\widetilde K^1(T)\) define

\[
\operatorname{ch}_1=-\sigma^{-1}\operatorname{ch}_0\theta.
\tag{6.14}
\]

Here \(\theta\) is the explicit natural isomorphism of Lesson 8 for the ideal of the base point, with target \(\widetilde K^0(\Sigma T)\). On unpointed \(X\), use \(T=X_+\). This defines a natural additive odd character on absolute, reduced and relative groups. Equations (6.13)–(6.14) give

\[
\begin{aligned}
\operatorname{ch}_0\theta&=-\sigma\operatorname{ch}_1,\\
\operatorname{ch}_1\beta&=\sigma\operatorname{ch}_0.
\end{aligned}
\tag{6.15}
\]

The second identity follows by applying (6.14) to \(\beta x\) and using \(\theta\beta=\mathsf B\). In particular the positive winding unitary on a circle has character the positive degree-one generator.

**Lemma 6.4 (boundary comparison).** For a finite CW pair, the positive exponential boundary \(\varepsilon\) and the index boundary \(\delta\) of (1.4) satisfy

\[
\begin{aligned}
\operatorname{ch}_1\varepsilon&=\delta_H\operatorname{ch}_0,\\
\operatorname{ch}_0\delta&=-\delta_H\operatorname{ch}_1.
\end{aligned}
\tag{6.16}
\]

*Proof.* The case of an empty subspace has zero boundaries. Otherwise work with \(Y_+\subset X_+\), including the disjoint base points, and form the reduced mapping cone
\(D=X_+\cup_{Y_+}CY_+\). The cone parameter has apex at \(t=0\) and attaches to \(Y_+\) at \(t=1\), matching the cone convention of Lesson 8. There are maps

\[
\begin{aligned}
q:D&\longrightarrow X_+/Y_+,\\
d:D&\longrightarrow\Sigma Y_+,
\end{aligned}
\tag{6.17}
\]

collapsing respectively the cone and \(X_+\). The map \(q\) is a homotopy equivalence. Indeed the cone is a contractible subcomplex. Extend its contraction to \(D\) by the CW homotopy extension property. The terminal map factors through its collapse to give an inverse; the extended homotopy and its quotient give both inverse homotopies. The extension property follows cell by cell from the retraction of \(D^n\times[0,1]\) onto its bottom and lateral boundary. Thus \(q^*\) is an isomorphism in both theories.

We establish the actual boundary formulas on \(D\). Given a projection \(p\) on \(Y\), choose a self-adjoint matrix lift \(a\) on \(X\), using Lemma 1.1 entrywise and then symmetrizing. Join it on the cone to \(tp\), with value zero at the apex. This gives a self-adjoint matrix function \(A\) on \(D\). The unitary \(\exp(2\pi iA)\) is nullhomotopic by scaling \(A\) to zero. It is the product of the exponential-boundary unitary on the \(X\) piece and the positive loop \(\exp(2\pi itp)\) on the cone piece, extended by identity on the other piece. Those two factors agree at their common boundary and have disjoint varying pieces. The class of their product is their K-theory sum, by Lesson 6. Hence

\[
q^*\varepsilon[p]=-d^*\beta[p].
\tag{6.18}
\]

Differences of projections give the full even group. At a disjoint base point the lift and its exponential are zero and identity respectively; thus this calculation also uses the required normalized representatives.

For a unitary \(v:Y\to U(N)\), Lemma 2.2 represents \(\delta[v]\) by \((\mathbf1^N,\mathbf1^N,v)\). Glue the trivial \(X\) bundle to the trivial cone bundle, with coefficient transfer \(v\) from the \(X\) frame to the cone frame, and call the resulting bundle \(G(v)\). This gluing is locally trivial at the seam: extend the matrix entries of \(v\) to \(X\) by Lemma 1.1 and take the polar part on the open neighborhood of \(Y\) where that extension is invertible. It supplies compatible local frames there. On the pair \((D,CY_+)\), its cone frame specifies a comparison of \(G(v)\) with the trivial bundle. Restriction to \((X_+,Y_+)\) gives exactly the triple of Lemma 2.2. This restriction induces an isomorphism of relative groups by strong excision from Lesson 11: it is identity on the ideal of the common complement \(X\setminus Y\). Naturality of (2.2) therefore identifies \([G(v)]-[\mathbf1^N]\) with \(q^*\delta[v]\) in the absolute group of \(D\).

By contrast, the projection loop defining \(\theta[v]\) has cone frame \(z(t)e_j\), where \(z(0)=I\) and \(z(1)=\operatorname{diag}(v,v^*)\), as in (4.3). At the attaching end that frame is \(ve_j\); its coefficient transfer from the fixed \(X\) frame is \(v^{-1}\). Thus \(d^*\theta[v]\) is the glued difference with the inverse comparison. Their sum is zero: \(\operatorname{diag}(v,v^{-1})\) is contracted to identity by the scalar-rotation path (2.2), so the direct sum of the two glued bundles is trivial. Therefore

\[
q^*\delta[v]=-d^*\theta[v].
\tag{6.19}
\]

Finally the relative cochain construction, with this same cone parameter, gives

\[
q^*\delta_H a=-d^*\sigma a.
\tag{6.20}
\]

For clarity, lift a cellular cocycle on \(Y\) to \(X\) and to the cone, zero at the apex. For a cell \(e\) of \(Y\), orient its cone cell with the interval direction first. Its boundary is \(e-c(\partial e)\), where \(c\) denotes this oriented cone operation. The relative coboundary of the cone lift consequently represents the positive interval product \(\sigma a\). The two lifts agree on \(Y\), and form a cochain on \(D\). Its coboundary is the sum of the relative coboundary on \(X\) and that positive cone coboundary; its absolute class is zero. Collapsing the two pieces gives exactly (6.20).

Apply the natural characters to (6.18) and (6.19), then use (6.15) and (6.20). The first gives \(-d^*\sigma\operatorname{ch}_0\), which is \(q^*\delta_H\operatorname{ch}_0\). The second gives \(+d^*\sigma\operatorname{ch}_1\), which is \(-q^*\delta_H\operatorname{ch}_1\). Cancel the isomorphism \(q^*\). These are precisely (6.16). \(\square\)

### The finite-cell argument

Let \(\eta_d\) be the generator of \(\widetilde H^d(S^d;\mathbb Z)\) fixed by increasing real coordinates, with each new suspension coordinate first; in dimension two this is the complex orientation of \(x+iy\). Equations (6.13)–(6.15), starting with the rank-one class on a point, give for the generators (4.1)

\[
\begin{aligned}
\operatorname{ch}_0(b_{2m})&=(-1)^m\eta_{2m},\\
\operatorname{ch}_1(b_{2m+1})&=(-1)^m\eta_{2m+1}.
\end{aligned}
\tag{6.21}
\]

For \(d=0\), \(\eta_0\) is the characteristic degree-zero class of the nonbase point of \(S^0\). Every relative sphere character is therefore an isomorphism after tensoring with \(\mathbb Q\), in its nonzero parity; in the other parity both groups are zero. This verifies the normalization in every dimension, rather than just on a two-sphere.

*Proof of Theorem 6.1.* On a finite zero-skeleton, \(K^0\) and \(H^0\) are the groups of integral and rational rank functions, respectively; \(K^1\) and odd cohomology vanish. The characters are the asserted isomorphisms there. Suppose the result holds on a subcomplex \(Y\), and attach one \(d\)-cell to obtain \(X\). The quotient \(X/Y\) is \(S^d\), so the relative characters in both parities are rational isomorphisms by (6.21) and Theorem 4.1. Attachments of additional zero-cells are already covered by the rank computation.

Tensor the pair sequence (1.4) with \(\mathbb Q\). This preserves exactness: tensoring is localization by nonzero integers, and clearing a common denominator reduces any kernel or image question to the original exact sequence. Group the ordinary cohomology sequence into even and odd direct sums. It remains exact since the sums are finite. Use \(\delta_H\) from even to odd and \(-\delta_H\) from odd to even; changing that arrow's sign preserves its kernel and image. Lemma 6.4 now makes the two exact rows commute under the characters. In the five consecutive positions

\[
\begin{gathered}
K^{i-1}(Y)\otimes\mathbb Q\\
\longrightarrow K^i(X,Y)\otimes\mathbb Q\\
\longrightarrow K^i(X)\otimes\mathbb Q\\
\longrightarrow K^i(Y)\otimes\mathbb Q\\
\longrightarrow K^{i+1}(X,Y)\otimes\mathbb Q,\\
i=0,1,
\end{gathered}
\tag{6.22}
\]

the four nonmiddle vertical maps are isomorphisms by induction and the relative sphere calculation. The diagram chase described in Lemma 6.3 proves that the middle character is an isomorphism. Induct over the finitely many cells, in increasing dimension, to prove (6.1) for arbitrary finite CW complexes, including disconnected ones and the empty complex. Its maps are natural because each part of the construction was natural. Applying the proved reduced assertion to \(X/Y\) proves the relative assertion for every finite CW pair. \(\square\)

The theorem does not replace integral computations. A finite-order K-class maps to zero because rational cohomology is a rational vector space: if \(nx=0\), then \(n\operatorname{ch}(x)=0\) and hence \(\operatorname{ch}(x)=0\). In particular the nonzero projective-plane class computed below is invisible to (6.1), although its rank is already zero. The character cannot be used to decide its integral order. The integral projective-space and projective-bundle calculations that follow establish their lattices and bases separately, and then use the character to normalize a generator.

### Integral projective-space K-theory

The rational character can help identify an integral generator once the integral group and its lattice have been established separately. It does not by itself determine that lattice. The following calculation adds the K-theory counterpart of (6.2); compare [Hatcher, Proposition 2.24]. Let \(L\) be the tautological complex line on \(\mathbb{CP}^m\) and set \(x=[L]-[1]\).

**Theorem 6.5.** For every \(m\geq0\),

\[
\begin{aligned}
K^0(\mathbb{CP}^m)&=\mathbb Z[x]/(x^{m+1}),\\
K^1(\mathbb{CP}^m)&=0.
\end{aligned}
\tag{6.23}
\]

Both \(1,x,\ldots,x^m\) and \(1,[L],\ldots,[L]^m\) are integral additive bases. The character is \(\operatorname{ch}(x)=e^{-h}-1\), with the sign fixed in (6.3).

*Proof.* Filter projective space by its coordinate subspaces. The quotient of the successive pair \((\mathbb{CP}^j,\mathbb{CP}^{j-1})\) is the complex-oriented \(S^{2j}\). Beginning with a point, the pair sequence and the sphere groups of §4 show inductively that \(K^1\) is zero and give

\[
\begin{gathered}
0\longrightarrow\mathbb Z\xrightarrow{\iota_j}K^0(\mathbb{CP}^j)\\
\longrightarrow K^0(\mathbb{CP}^{j-1})\longrightarrow0.
\end{gathered}
\tag{6.24}
\]

The group on the right is free by induction, so lift its basis to split this sequence as groups. Hence \(K^0(\mathbb{CP}^j)\) is free of rank \(j+1\). In particular its rational character is injective even before tensoring: a class with zero character is torsion by Theorem 6.1, and this group has no torsion.

The line-class construction gives \(\operatorname{ch}(L)=e^{-h}\). Since \(h^{j+1}=0\), injectivity just proved implies \(x^{j+1}=0\). Inductively \(x^j\) restricts to zero on \(\mathbb{CP}^{j-1}\), so \(x^j=a\iota_j(b_{2j})\) for some integer \(a\), using the relative sphere generator of (6.21). Naturality of the relative character and the complex cell orientation give

\[
\begin{aligned}
\operatorname{ch}(\iota_j(b_{2j}))&=(-1)^j h^j,\\
\operatorname{ch}(x^j)&=(e^{-h}-1)^j\\
&=(-1)^j h^j.
\end{aligned}
\tag{6.25}
\]

Here the quotient's top cohomology generator pulls back to \(h^j\), since it evaluates to one on the oriented top cell; this is the hyperplane normalization proved in (6.2). Thus \(a=1\): the top power is an *integral* relative generator. Lift the lower powers through (6.24) and add this top power. They form an integral basis, giving precisely (6.23) and no additional relation. Finally the binomial identities \([L]^j=(1+x)^j\) give an upper triangular change of basis with diagonal entries one; its integer inverse proves the second basis assertion. For \(m=0\), the line is trivial and the statement is \(K^0(\mathrm{point})=\mathbb Z\). \(\square\)

For instance \(K^0(\mathbb{CP}^2)\) has basis \(1,x,x^2\), and
\(\operatorname{ch}(x)=-h+h^2/2\), \(\operatorname{ch}(x^2)=h^2\). The factor \(1/2\) explains why a rational cohomology basis cannot simply be read as an integral K-basis.

### Projective bundles over arbitrary compact bases

We next need a degree-zero bundle action, rather than a general Künneth theorem. For a bundle represented by a projection \(s\), multiplication of \([p]\) by \([s]\) is represented by \(p\otimes s\). For an odd class represented by a unitary \(u\), it is represented by

\[
u\otimes s+1\otimes(1-s).
\tag{6.26}
\]

Pull back both representatives to the same space before using these formulas. Direct sums, stable equivalence and homotopies show that they define an action of virtual bundles in both degrees, including relative groups when the other factor is relative. They preserve both boundary maps: the exponential of a lifted self-adjoint corner is its exponential on the \(s\)-corner and identity on the complement; the doubled-lift index formula likewise becomes its original formula on that corner plus a constant complementary projection. Subtracting the scalar projection cancels that complement. These same corner identities preserve \(\beta\) and \(\theta\). Thus the action commutes with pair sequences, suspension and Bott maps. These checks use the actual formulas of Lessons 7–11 and do not assume a general product theorem.

**Lemma 6.6 (a projective-space factor).** If \(T\) is any compact Hausdorff space, the map

\[
\begin{gathered}
\bigoplus_{j=0}^{m}K^i(T)\\
\longrightarrow K^i(T\times\mathbb{CP}^m),\\
(a_j)\longmapsto\sum_j\pi_T^*a_j\,x^j,\\
i=0,1,
\end{gathered}
\tag{6.27}
\]

is an isomorphism. Replacing the powers of \(x\) by powers of \([L]\) gives the same conclusion.

*Proof.* The case \(m=0\) is identity. In the pair with the preceding projective subspace, the relative ideal is \(C_0(T\times\mathbb C^m)\). Its two groups identify with \(K^i(T)\) by the iterated coefficient Bott maps of §3. The scalar relative generator maps to \(x^m\) by (6.25). Multiplying its relative representative by a coefficient class realizes precisely the coefficient Bott isomorphism: for even classes this is the projection-corner calculation (3.6), iterated \(m\) times, and for odd classes it is the same calculation after suspension, or (6.26) and the corner compatibility with \(\theta\).

Assume (6.27) for \(m-1\), in both degrees. Each class on \(T\times\mathbb{CP}^{m-1}\) is a sum of coefficient classes times the first \(m\) powers; those powers extend to \(T\times\mathbb{CP}^m\). Restriction is therefore onto in both degrees, so both adjacent boundary maps in the pair sequence vanish. The relative group injects, and its entire image is exactly the coefficient classes times \(x^m\). Exactness now proves that the first \(m\) powers together with this final summand give both surjectivity and injectivity in (6.27). The integer binomial change of basis of Theorem 6.5 remains invertible on every coefficient group, including groups with torsion. \(\square\)

**Theorem 6.7 (the K-theory projective-bundle theorem).** Let \(E\to X\) be a complex vector bundle of constant rank \(r\geq1\), with \(X\) compact Hausdorff. Let \(\pi:P(E)\to X\) be its bundle of lines, and let \(S\subset\pi^*E\) be the tautological line. In both degrees,

\[
\begin{gathered}
\bigoplus_{j=0}^{r-1}K^i(X)\\
\xrightarrow{\cong}K^i(P(E)),\\
(a_j)\longmapsto\sum_j\pi^*a_j[S]^j,\\
i=0,1.
\end{gathered}
\tag{6.28}
\]

In particular \(\pi^*\) is injective. No finite CW hypothesis is required. In degree zero this gives the ring presentation

\[
\begin{gathered}
K^0(P(E))\\
\cong K^0(X)[s]/(f_E(s)),\\
f_E(s)=\sum_{j=0}^{r}(-1)^j[\Lambda^j E]s^{r-j},\\
s\longmapsto[S].
\end{gathered}
\tag{6.29}
\]

The coefficient \([\Lambda^0E]\) is the unit, so this is a monic polynomial.

*Proof.* A finite embedding of \(E\) into a trivial bundle identifies \(P(E)\) with the closed set of lines fixed by the associated range projection in \(X\times\mathbb{CP}^{N-1}\). Thus its total space is compact Hausdorff. The finite shrinking argument of Lesson 2, Lemma 2.0, supplies compact closed sets \(K_1,\ldots,K_N\) covering \(X\), each lying in a trivializing open set for \(E\). For every closed subset \(V\subset K_j\), the projective bundle is \(V\times\mathbb{CP}^{r-1}\), and its tautological line is the pullback of \(L\). Lemma 6.6 proves (6.28) over \(V\).

We show that the property “(6.28) holds over every closed subset” is preserved under a union of two compact closed sets. Let \(V\) be closed in that union and put \(V_1=V\cap K\), \(V_2=V\cap K'\). Functions on \(V\) form the pullback of functions on \(V_1,V_2\) over \(V_1\cap V_2\). The restriction maps are onto by Lemma 1.1. The same holds on their projective-bundle preimages, so Lesson 11, Theorem 4.1, gives Mayer–Vietoris sequences in both degrees. Compare the latter sequence with \(r\) copies of the former sequence, using the powers of the *global* line \(S\). The maps commute by the corner boundary checks preceding Lemma 6.6. On \(V_1,V_2\) and their intersection the comparison is an isomorphism by the assumed property. In each five consecutive exact positions surrounding \(K^i(V)\), the other four comparison maps are therefore isomorphisms. The exact diagram chase used in Lemma 6.3 proves the remaining one is an isomorphism. If the intersection is empty, these pullbacks and sequences reduce to direct sums and the same assertion follows directly.

Induct over the finite closed cover to prove (6.28) on \(X\). Under its explicit isomorphism, \(\pi^*a\) is the vector \((a,0,\ldots,0)\), proving injectivity.

For the ring relation, write \(\pi^*E=S\oplus E'\), with \(E'\) the rank-\(r-1\) orthogonal complement. The exterior algebra of a direct sum is the graded tensor product of its exterior algebras: expanding an alternating tensor according to which factors lie in each summand gives the bundle isomorphisms in every degree. Therefore, in the polynomial ring over \(K^0(P(E))\),
\(\sum_j[\pi^*\Lambda^jE]t^j=(1+[S]t)\sum_j[\Lambda^jE']t^j\).
Multiply formally by \(\sum_{k\geq0}(-[S]t)^k\) and take the coefficient of \(t^r\). The left side is \((-1)^r f_E([S])\), and the right side is \([\Lambda^rE']=0\). This proves the relation. Division by a monic polynomial works over any commutative coefficient ring by successively subtracting its leading term; it gives a unique remainder of degree below \(r\). Hence the quotient in (6.29) is free over \(K^0(X)\) on \(1,s,\ldots,s^{r-1}\). The map to the bundle ring carries these to the basis already proved in (6.28), so it is both injective and surjective. This proves the complete ring presentation, including coefficient rings with torsion. \(\square\)

**Corollary 6.8 (integral K-theory splitting).** A constant finite-rank complex bundle over any compact Hausdorff base splits into lines after pullback along a finite sequence of projective bundles, and that pullback is injective on both K-groups.

*Proof.* Choose a Hermitian metric. On \(P(E)\), the bundle \(\pi^*E\) is \(S\oplus S^\perp\); the orthogonal complement is a continuous bundle of rank \(r-1\). Apply the same construction to that complement until the rank is one. Each pullback is injective by Theorem 6.7, so their composite is injective. Rank zero needs no construction. A bundle of nonconstant finite rank has finitely many clopen rank strata on a compact base; apply the construction separately on each stratum, taking identity on the rank-zero stratum, and then their disjoint union. The K-groups are finite direct sums on those strata, so injectivity is preserved. \(\square\)

This is the integral K-theory version of the earlier cohomological splitting, with a larger class of bases. It gives actual coefficient bases and injective maps before rationalization, while leaving the projective-plane torsion of Exercise 12.4 intact.

## Graded products and boundary signs

Let \(T\) be compact Hausdorff with a base point. Write \(\widetilde K^i(T)=K_i(C_0(T\setminus\{*\}))\), for \(i=0,1\). Put \(\Sigma T=S^1\wedge T\), with the increasing real suspension coordinate first. In this section the degrees are modulo two. Retain the actual maps

\[
\begin{gathered}
\beta_T:\widetilde K^0(T)\longrightarrow\widetilde K^1(\Sigma T),\\
\theta_T:\widetilde K^1(T)\longrightarrow\widetilde K^0(\Sigma T).
\end{gathered}
\]

and the ordered positive Bott isomorphism

\[
\begin{gathered}
\mathsf B_T=\theta_{\Sigma T}\beta_T,\\
\mathsf B_T:\widetilde K^0(T)
\longrightarrow\widetilde K^0(\Sigma^2T).
\end{gathered}
\tag{GP.1}
\]

The map \(\beta\) is the positive projection loop; \(\theta\) is the forward doubled-path map. They have different types. The positive winding class \(\eta\in\widetilde K^1(S^1)\) satisfies \(\theta_{S^1}\eta=\mathfrak b\), where \(\mathfrak b\) is the positive planar Bott class of Lessons 8 and 10, with outer coordinate first.

### An even external product without a Künneth assumption

**Lemma GP.1.** There is a natural bilinear product

\[
\begin{gathered}
\boxtimes:\widetilde K^0(T)\times\widetilde K^0(U)\\
\longrightarrow\widetilde K^0(T\wedge U).
\end{gathered}
\tag{GP.2}
\]

It pulls back to the ordinary external tensor product of virtual bundles on \(T\times U\). It is associative, and the interchange of \(T,U\) carries it to the reversed product.

*Proof.* Tensor products of finite bundle representatives define a bilinear external product on the ordinary groups. The fibrewise tensor flip gives commutativity under interchange. Associativity comes from the fibrewise association isomorphism. Direct-sum distribution, bundle isomorphisms and bundle homotopies establish all these assertions in their Grothendieck groups.

Let \(W=T\times\{*\}\cup\{*\}\times U\). The ordinary external product of two reduced classes restricts to zero on W: on each face one factor is its zero virtual fibre at the base point. We check that this has a unique relative lift.

Restriction to T splits on W by collapsing the U arm. Its kernel is \(C_0(U\setminus\{*\})\). The split exact sequence gives

\[
K^i(W)\cong K^i(T)\oplus\widetilde K^i(U),\qquad i=0,1.
\]

Every such class extends to \(T\times U\): extend the T class by the first projection and the reduced U class by the second. Thus restriction to W is onto in both degrees. Exactness of the pair sequence makes

\[
\begin{gathered}
\widetilde K^i(T\wedge U)\\
=K^i(T\times U,W)\\
\longrightarrow K^i(T\times U).
\end{gathered}
\tag{GP.3}
\]

injective, with image the kernel of restriction. The quotient homeomorphism and the identical relative ideal give the equality in (GP.3). Define (GP.2) as that unique lift. Uniqueness proves bilinearity and pointed naturality, including homotopy invariance. It also proves the interchange assertion.

Here is the additional injectivity needed for associativity, so a three-factor quotient does not hide an assumption. For any compact V, \(W\times V\) is the union of \(T\times V\) and \(U\times V\) along V. Restriction to \(T\times V\) splits by collapsing the U arm, with kernel \(C_0((U\setminus\{*\})\times V)\). The latter group's inclusion into \(K^i(U\times V)\) identifies it with the kernel of restriction to V, since that evaluation also splits. It follows that every \(K^i(W\times V)\) class extends to \(T\times U\times V\): extend the first class by its projection and the kernel class by the other projection. This holds in both degrees.

Consequently the relative group for \((T\times U\times V,W\times V)\) injects into its absolute group. The quotient map \((T\times U)\times V\to(T\wedge U)\times V\) is also injective on absolute K-groups: decompose the latter group into its split V summand and the relative kernel at \(\{*\}\times V\). It is injective on the V summand by evaluating at both base points, and on the kernel by the preceding relative injection and the identical complement ideal.

Now pull either association of three reduced products to \(T\times U\times V\). They are the two associations of the ordinary bundle tensor product and hence agree. The pullback from \(T\wedge U\wedge V\) is injective: factor it through (GP.3) for \((T\wedge U,V)\) and the just proved coefficient-V injection. Thus the reduced products agree. This proves associativity. The same finite-factor argument proves the coherence used below. \(\square\)

### Every permutation sign, integrally

**Lemma GP.2.** A permutation \(\pi\) of the n real suspension coordinates acts on
\(\widetilde K^0(\Sigma^nT)\) as multiplication by \(\operatorname{sgn}(\pi)\). Reversal of any one real suspension coordinate acts as \(-1\). These statements hold for every compact pointed T, including torsion classes.

*Proof.* First reverse the coordinate in \(\theta_A[u]\). With the existing doubled path \(z(0)=1\), \(z(1)=D=\operatorname{diag}(u,u^{-1})\), its representative is \([z(t)Pz(t)^{-1}]-[P]\). Put

\[
w(t)=z(1-t)D^{-1}.
\]

Then \(w(0)=1\), \(w(1)=\operatorname{diag}(u^{-1},u)\), and D commutes with P. Hence

\[
w(t)Pw(t)^{-1}=z(1-t)Pz(1-t)^{-1}.
\]

The reversed projection loop is precisely a permitted representative of \(\theta_A[u^{-1}]=-\theta_A[u]\). Since \(\theta_A\) is onto, reflection of the first coordinate acts as \(-1\) on \(K_0(SA)\). Apply this with \(A=C_0(\mathbb R^{n-1},C_0(T\setminus\{*\}))\). Reflection in another coordinate is conjugate by a coordinate permutation to this reflection, and a conjugate of \(-\mathrm{id}\) is still \(-\mathrm{id}\).

The interchange of two adjacent real coordinates is the composition of a reflection in one of those coordinates and a quarter-turn in their plane: the matrices \(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\) and \(R_{\pi/2}\operatorname{diag}(1,-1)\) are equal. The quarter-turn is homotopic to the identity through rotations. These rotations give a proper homotopy on \(\mathbb R^n\times(T\setminus\{*\})\): inverse images of a fixed compact set lie in a fixed closed ball in the real variables and a fixed compact set in the remaining variables. Its pullbacks are therefore norm-continuously homotopic. Thus every adjacent interchange acts as \(-1\). Decompose any permutation into adjacent interchanges. The parity of their number is \(\operatorname{sgn}(\pi)\), proving the assertion. All witnesses are actual integral K-classes. \(\square\)

For \(x\in\widetilde K^0(\Sigma^mT)\), \(y\in\widetilde K^0(\Sigma^nU)\), define \(E_{m,n}(x,y)\) by (GP.2), then gather the suspension coordinates in the order

\[
\begin{gathered}
(s_1,\ldots,s_m,\\
t_1,\ldots,t_n;\,T,U).
\end{gathered}
\tag{GP.4}
\]

The underlying homeomorphism sends this word to \((s;T,t;U)\). It specifies the product on the nose; no sign is suppressed when gathering the variables. Lemma GP.1 and the identical coordinate words prove associativity of the E maps. Swapping the two input blocks requires exactly mn adjacent interchanges of real suspension variables. Lemma GP.2 therefore gives the factor \((-1)^{mn}\) under interchange of T and U.

The coefficient Bott formula already proved in Lesson 12, Theorem 3.1, and Lesson 10 identifies

\[
\mathsf B_{\Sigma^mT}x=E_{2,m}(\mathfrak b,x).
\tag{GP.5}
\]

For reduced classes it follows either by subtracting bundle representatives on the compactification, or by (GP.3); for all higher suspended classes those same arguments apply to \(\Sigma^mT\). Thus E commutes with adding a Bott block on its first factor. It commutes with adding one on its second factor as well: use associativity and move that two-coordinate block past the m coordinates of the first factor. This uses 2m interchanges and has sign \(+1\). This proves both periodicity compatibilities explicitly.

### The two-degree product and its suspension normalization

**Theorem GP.3.** There are natural, bilinear, associative external products

\[
\begin{gathered}
\widetilde K^i(T)\times\widetilde K^j(U)\\
\longrightarrow\widetilde K^{i+j}(T\wedge U),\\
i,j\in\{0,1\}.
\end{gathered}
\tag{GP.6}
\]

with

\[
\tau^*(y\boxtimes x)=(-1)^{ij}x\boxtimes y,
\tag{GP.7}
\]

where \(\tau:T\wedge U\to U\wedge T\) interchanges the factors. They agree with the existing even bundle action in both degrees.

*Proof.* Put \(\Phi_0=\mathrm{id}\), \(\Phi_1=\theta\). Apply \(E_{i,j}\) to \(\Phi_i x,\Phi_j y\). If i+j is zero, leave its value alone; if it is one, apply \(\theta^{-1}\); if it is two, apply \(\mathsf B^{-1}\). This is an explicit definition of all four products in (GP.6), with exactly the ordered coordinates (GP.4).

Here is full periodic coherence rather than a separate associativity assumption. For each parity i, take the direct limit of \(\widetilde K^0(\Sigma^{i+2r}T)\) under the isomorphisms adding the first two-coordinate Bott block. It is identified with \(\widetilde K^i(T)\) by \(\Phi_i\) at r=0. The two compatibilities after (GP.5) make E descend to the products of these direct limits, independently of r and of both representatives. Associativity of E then proves associativity of these products: choose representatives for three classes, apply the identical total coordinate word, and use the ordinary even associativity in Lemma GP.1; all changes of even stage are accounted for by those two Bott compatibilities. Returning to the r=0 identifications gives exactly the four-case definition above. Since \((i+2r)(j+2s)\equiv ij\pmod2\), the coordinate-block interchange formula gives (GP.7).

For an even bundle class represented by s and an odd unitary represented by u, the existing formula \(u\otimes s+1\otimes(1-s)\) is sent by \(\theta\) to the even corner product with \(\theta[u]\). This follows directly by putting the doubled path on the s corner and the constant path on its complement; the constant projection cancels in its relative class. It is exactly the (1,0) product above; the tensor flip gives the (0,1) case. Subtract virtual bundles. The even-even case is the original bundle tensor product. These checks also apply after quotienting a closed subspace. Thus no existing even action is changed. \(\square\)

The positive winding class has the following important normalization:

\[
\boxed{\begin{gathered}
\eta\boxtimes x=\beta x\quad(i=0),\\
\eta\boxtimes x=-\theta x\quad(i=1).
\end{gathered}}
\tag{GP.8}
\]

To prove the first identity, apply \(\theta\) to the product. The (1,0) definition and (GP.5) give \(\theta(\eta\boxtimes x)=\mathfrak b\boxtimes x=\mathsf Bx=\theta\beta x\); cancel \(\theta\).

For the second, write \(k=\theta x\), with its suspension variable b. The (1,1) product is defined using \(\theta\eta=\mathfrak b\), whose coordinates are (a,r), where a is the added \(\theta\) coordinate and r is the original winding coordinate. Before gathering, the even product has word (a,r,b;T). Gathering the two added coordinates first gives (a,b,r;T). This is exactly one adjacent interchange. Before that interchange the class is \(\mathsf Bk\), by (GP.5); afterwards it is its negative by Lemma GP.2. The inverse Bott map on the first two coordinates therefore gives \(-k\) on the remaining r coordinate. This proves \(\eta\boxtimes x=-\theta x\), integrally. In particular

\[
\eta\boxtimes\eta=-\mathfrak b.
\tag{GP.9}
\]

Let \(s_i\) denote \(\beta\) for i=0 and \(\theta\) for i=1. Then (GP.8) reads \(s_i x=(-1)^i\eta\boxtimes x\). It implies two distinct suspension rules. With the suspended coordinate placed first,

\[
\begin{gathered}
s_{i+j}(a\boxtimes b)\\
=a\boxtimes s_jb,\\[3pt]
s_{i+j}(a\boxtimes b)\\
=(-1)^j(s_i a)\boxtimes b.
\end{gathered}
\tag{GP.10}
\]

In the first identity, the target on the right is first gathered from \(T\wedge\Sigma U\) to \(\Sigma(T\wedge U)\); in the second identity it is already in \(\Sigma T\wedge U\) order. For the first line, move the odd \(\eta\) past a, which contributes \((-1)^i\); this cancels the change from \((-1)^{i+j}\) to \((-1)^j\). For the second there is no move past a, leaving the factor \((-1)^j\). Thus (GP.10) derives, rather than assumes, every needed suspension sign.

### Absolute and relative products

Let X,Y be compact Hausdorff and A⊂X, B⊂Y closed. Define \(T_{X,A}=X_+/A_+\), so that when A is empty it is X with a disjoint base point. Its complement of the quotient point is \(X\setminus A\), hence its reduced operator K-groups are precisely \(K^i(X,A)\). There is a canonical pointed homeomorphism

\[
T_{X,A}\wedge T_{Y,B}
\cong T_{X\times Y,\,A\times Y\cup X\times B}.
\]

Indeed both sides are compact Hausdorff quotient spaces with complement \((X\setminus A)\times(Y\setminus B)\), and the product quotient induces a continuous bijection. It is a homeomorphism by compactness. The description also covers empty A or B with the disjoint-base-point convention.

Put \(F_{A,B}=A\times Y\cup X\times B\). Consequently (GP.6) gives the typed external product

\[
\begin{gathered}
K^i(X,A)\times K^j(Y,B)\\
\longrightarrow K^{i+j}(X\times Y,F_{A,B}).
\end{gathered}
\tag{GP.11}
\]

If both factors have base X, the relative diagonal

\[
T_{X,A\cup B}\longrightarrow T_{X,A}\wedge T_{X,B},
\qquad [x]\longmapsto([x],[x]),
\]

is continuous and well-defined: every point of A∪B is sent to the smash base point. Pulling (GP.11) back gives

\[
\begin{gathered}
K^i(X,A)\times K^j(X,B)\\
\longrightarrow K^{i+j}(X,A\cup B).
\end{gathered}
\tag{GP.12}
\]

These products are associative and graded commutative by (GP.7), natural under maps of compact pairs, and agree with bundle tensor products in even degree. Taking A=B=∅ gives a unital graded ring \(K^*(X)\), whose identity is the trivial line. Taking A=∅ gives its left and right actions on relative K-groups. The actions on Y are obtained by restriction. Every formula has specified absolute/relative target; no pullback along an undefined map \(\Sigma Y\to Y\) is used.

**Corollary GP.5 (a contractible cover).** Let a compact pointed Hausdorff space \(X\) be the union of \(n\geq1\) closed contractible subspaces \(A_1,\ldots,A_n\), each containing the base point. Every product of \(n\) homogeneous reduced \(K\)-classes on \(X\) is zero. In particular the product of any two reduced classes on a suspension is zero.

*Proof.* The split point-evaluation sequence (1.6) identifies reduced classes with the evaluation kernel in \(K^*(X)\). Naturality of (GP.12) respects that inclusion and the relative products. For \(x_k\in\widetilde K^{i_k}(X)\), restriction to \(A_k\) is zero. In even degree, homotopy invariance identifies \(K^0(A_k)\) with the rank group \(\mathbb Z\), and the reduced class has rank zero at the base point. In odd degree \(K^1(A_k)=0\). Exactness of the pair sequence therefore lifts \(x_k\) to \(K^{i_k}(X,A_k)\). Iterate (GP.12), and put \(d=i_1+\cdots+i_n\) modulo two and \(F=A_1\cup\cdots\cup A_n=X\). Their product lies in

\[
\begin{gathered}
K^d(X,F)\\
=K^d(X,X)=0.
\end{gathered}
\tag{GP.22}
\]

For \(\Sigma T=S^1\wedge T\), take the images of the two closed semicircles times \(T\). Each image is a closed reduced cone containing the suspension base point. Its contraction is the map moving its interval coordinate linearly toward the collapsed endpoint while keeping the \(T\)-coordinate fixed. This descends through the collapsed base-point interval, so each cone is contractible for every compact pointed Hausdorff \(T\). Their union is \(\Sigma T\); apply the first assertion with \(n=2\). \(\square\)

### The cone comparison for every compact Hausdorff pair

Fix Y⊂X closed. If Y is empty the connecting maps are zero, so all module identities below are immediate. Otherwise form the reduced cone space

\[
D=X_+\cup_{Y_+}CY_+.
\]

The cone has apex at t=0 and attaches at t=1. The disjoint base point and its cone interval are collapsed to the common base point. The finite gluing quotient is compact Hausdorff. Let

\[
\begin{gathered}
q:D\to T_{X,Y},\\
d:D\to\Sigma Y_+.
\end{gathered}
\tag{GP.13}
\]

collapse, respectively, the whole cone and X₊. The quotient function extension of Lesson 12, Lemma 1.1, gives the exact sequence

\[
\begin{gathered}
0\to C_0(X\setminus Y)\\
\to C_0(D\setminus\{*\})\\
\to C_0((0,1],C(Y))\to0.
\end{gathered}
\tag{GP.14}
\]

The first map is q pullback. Restriction to the cone gives the last map; its surjectivity follows by extending its function from that compact closed cone, with zero value at the common base point. The kernel is the zero-extended ideal of the common complement X\Y. The quotient is exactly the existing cone algebra of C(Y), whose two K-groups vanish by the contraction f(t)↦f(rt). Thus the six-term sequence proves

\[
\begin{gathered}
q^*:K^i(X,Y)\xrightarrow{\cong}\widetilde K^i(D),\\
i=0,1.
\end{gathered}
\tag{GP.15}
\]

This group isomorphism needs no CW assumption and no assertion that q is a homotopy equivalence.

The actual boundary formulas are

\[
\boxed{\begin{gathered}
q^*\varepsilon=-d^*\beta,\\
q^*\delta=-d^*\theta.
\end{gathered}}
\tag{GP.16}
\]

Here \(\varepsilon:K^0(Y)\to K^1(X,Y)\) is the positive exponential, and \(\delta:K^1(Y)\to K^0(X,Y)\) is the existing index boundary.

For the first formula take a projection p on Y, with zero value at the disjoint base point, and a selfadjoint matrix lift a on X₊. On the cone use tp. The two pieces agree at t=1 and give a selfadjoint matrix function A on D. The class of \(\exp(2\pi iA)\) is zero, since scaling A to zero contracts it. It is exactly the product of the exponential-boundary unitary on the X piece, extended by identity on the cone, and the positive projection loop on the cone, extended by identity on X. Those normalized factors have disjoint varying pieces. The unitary product gives the sum of their K₁ classes. Hence \(q^*\varepsilon[p]+d^*\beta[p]=0\). Projection differences prove the first formula in full.

For the second formula let v be a unitary map on Y, with identity value at the added base point. Glue the trivial X₊ bundle to the trivial cone bundle with coefficient transfer v from the X frame to the cone frame, obtaining G(v). This is a bundle: extend the entries of v to X, polar-correct on the open neighborhood of Y where the extension is invertible, and use those frames at the seam. The cone frame specifies its relative comparison with the trivial bundle. Restriction to (X₊,Y₊) is the triple \((\mathbf1^N,\mathbf1^N,v)\), which current Lemma 2.2 identifies with \(\delta[v]\). Strong relative excision identifies the groups, because their complement ideals are literally the same C₀(X\Y). Forgetting that comparison therefore gives

\[
[G(v)]-[\mathbf1^N]=q^*\delta[v].
\]

The doubled path defining \(\theta[v]\) has terminal cone frame \(ve_j\). Coefficient transfer from the fixed X frame to this cone frame is \(v^{-1}\). Thus \(d^*\theta[v]\) is the glued difference for the inverse transfer. The two differences sum to zero: the doubled comparison \(\operatorname{diag}(v,v^{-1})\) contracts to identity by the existing scalar-rotation path. Gluing this homotopy gives a bundle over the compact cylinder of D, whose endpoint with identity transfer is trivial; bundle cylinder transport identifies its endpoints. Hence \(q^*\delta[v]+d^*\theta[v]=0\). All normalized maps and finite matrices are those of the existing index/triple constructions. This proves the second formula and (GP.16) for all compact pairs.

### The exact left- and right-module formulas

**Theorem GP.4.** For homogeneous \(a\in K^i(X)\), \(b\in K^j(Y)\), write \(r^*a\) for its restriction and set \(\partial_0=\varepsilon\), \(\partial_1=\delta\). The actual course boundaries obey

\[
\boxed{\partial_{i+j}(r^*a\,b)=a\,\partial_jb.}
\tag{GP.17}
\]

Thus the pair exact cycle is a cycle of left K*(X)-modules with unsigned linearity, including odd a. The four typed formulas are

\[
\begin{gathered}
(i,j)=(0,0):\\
\varepsilon(r^*a\,b)=a\,\varepsilon b,\\[3pt]
(i,j)=(0,1):\\
\delta(r^*a\,b)=a\,\delta b,\\[3pt]
(i,j)=(1,0):\\
\delta(r^*a\,b)=a\,\varepsilon b,\\[3pt]
(i,j)=(1,1):\\
\varepsilon(r^*a\,b)=a\,\delta b.
\end{gathered}
\tag{GP.18}
\]

For right multiplication the exact rule is

\[
\begin{gathered}
\partial_{j+i}(b\,r^*a)\\
=(-1)^i(\partial_jb)\,a.
\end{gathered}
\tag{GP.19}
\]

If instead one wants the usual Koszul convention for a homogeneous degree-one connecting map, define \(\overline\partial_0=\varepsilon\), \(\overline\partial_1=-\delta\). Then

\[
\begin{gathered}
\overline\partial_{i+j}(r^*a\,b)
=(-1)^i a\,\overline\partial_jb,\\
\overline\partial_{j+i}(b\,r^*a)
=(\overline\partial_jb)\,a.
\end{gathered}
\tag{GP.20}
\]

Changing that arrow's sign preserves exactness; it does not change the actual positive exponential or index maps in the course.

*Proof.* The inclusion and restriction arrows are left-linear by naturality of (GP.11)–(GP.12). We prove the nontrivial connecting identity with actual maps, rather than relying on that observation.

There is a continuous pointed map \(\rho:D\to X_+\wedge D\). On X₊ it sends x to (x,x); on the cone it sends (y,t) to (y,(y,t)). At the cone apex the second factor is the base point, so continuity does not require a map from the apex to a chosen point of Y. At the seam its two definitions agree. Let \(\kappa:T_{X,Y}\to X_+\wedge T_{X,Y}\) be the relative diagonal and let

\[
\begin{gathered}
\Gamma:\Sigma Y_+\to X_+\wedge\Sigma Y_+,\\
(t,y)\longmapsto(y,(t,y)).
\end{gathered}
\]

On the base point both maps take the base-point value. They have the exact identities

\[
\begin{gathered}
(\mathrm{id}\wedge q)\rho=\kappa q,\\
(\mathrm{id}\wedge d)\rho=\Gamma d.
\end{gathered}
\tag{GP.21}
\]

The first follows on X by the diagonal and on the cone by its collapse. The second follows on the cone by the displayed formulas and on X by its collapse. These are equalities of continuous maps, not merely homotopy claims.

Naturality of the product and (GP.21) first give

\[
\begin{aligned}
q^*(a\,\partial_jb)
&=\rho^*(a\boxtimes q^*\partial_jb)\\
&=-d^*\Gamma^*(a\boxtimes s_jb),
\end{aligned}
\]

using (GP.16). Apply the first suspension rule (GP.10), followed by the diagonal of Y: it says precisely

\[
\Gamma^*(a\boxtimes s_jb)=s_{i+j}(r^*a\,b).
\]

This diagonal statement is legitimate on the suspension because it uses Γ, not a nonexistent projection ΣY→Y. The two scalar factors involved are explicitly \((-1)^{i+j}\) from \(s_{i+j}\) and \((-1)^i(-1)^j\) from moving the odd η past a; they agree. Formula (GP.16) now shows that the previous expression is \(q^*\partial_{i+j}(r^*a\,b)\). Cancel the isomorphism (GP.15). This proves (GP.17) and every entry of (GP.18).

For (GP.19), graded commutativity first moves a past b with sign \((-1)^{ij}\). After applying (GP.17), moving a past \(\partial_jb\), of parity j+1, gives \((-1)^{i(j+1)}\). Their product is \((-1)^i\). Finally multiply (GP.17) by \((-1)^{i+j}\) and use \(\overline\partial_j=(-1)^j\partial_j\); the factor remaining on the left-module action is \((-1)^i\). The right formula follows from (GP.19) by the same calculation. This proves (GP.20). \(\square\)

The unsigned left-module assertion is therefore valid with this course's actual two different degree-one boundary formulas. It would be incorrect to replace δ by −δ and retain unsigned left-linearity for odd coefficients. Conversely it would be incorrect to insert an extra Koszul sign in (GP.17) while keeping the actual ε and δ.

Source credit: [Hatcher, *Vector Bundles and K-Theory*](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf#page=59), Example 2.13 and Propositions 2.14–2.15, printed pp. 55–57, develops the relative products, graded interchange and exact-sequence module structure. The proofs above specify all integral coordinate and boundary signs using the positive \(\beta,\varepsilon\) and forward \(\theta,\delta\) of Lessons 8, 10 and 11. In particular (GP.17) gives the module formula for those actual arrows; (GP.20) records the effect of changing the odd connecting arrow. The required inputs are the finite bundle and cylinder proofs of Lesson 2, the matrix block-product laws, coefficient Bott periodicity, and the relative-bundle identification and exact pair sequence proved earlier in this lesson.

## 7. Exercises with complete solutions

**Exercise 12.1 — The three-sphere (basic).** Compute both groups of \(S^3\) and give generators.

*Solution.* The ideal in (4.5) is \(D_3\), whose groups are zero in degree zero and \(\mathbb Z\) in degree one. Split exactness therefore gives \(K^0(S^3)=\mathbb Z[1]\), \(K^1(S^3)=\mathbb Z[U]\). Here, on \(\mathbb R\times\mathbb C\),

\[
\begin{aligned}
U(t,\zeta)&=\bigl(z(t)q(\zeta)+I-q(\zeta)\bigr)\\
&\qquad\cdot\bigl(\overline{z(t)}P+I-P\bigr).
\end{aligned}
\tag{7.1}
\]

and \(U(\infty)=I\). Its class is \(\beta_{D_2}(\mathfrak b)\); Bott periodicity and injectivity of the split ideal map prove that it is a generator. Thus the formula and its generating property are both determined, without an unproved unstable homotopy calculation.

**Exercise 12.2 — The two-torus (basic).** List integral bases of both groups of \(\mathbb T^2\).

*Solution.* Theorem 5.1 with \(A=C(\mathbb T)\) gives two copies of \(\mathbb Z\) in each degree. Constants carry the first circle's rank and winding classes to \([1]\) and \([z_1]\). In degree one the ideal map takes \(\beta_A[1]\) to \([z_2]\). In degree zero it takes \(\theta_A[z_1]\) to the Bott-type difference \([q(x_2+ix_1)]-[P]\), extended by zero difference on the two collapsed circles as in (5.5). These are respectively the constant and ideal summands, so \([1],[q]-[P]\) and \([z_1],[z_2]\) are bases. In particular the Bott difference has zero evaluation at the distinguished point; it is not another rank generator.

**Exercise 12.3 — Two circles meeting at a point (intermediate).** Use Mayer–Vietoris to compute \(K^*(S^1\vee S^1)\).

*Solution.* A function on the wedge is a pair of circle functions with the same value at the meeting point. Thus its algebra is the pullback of two evaluations \(C(\mathbb T)\to\mathbb C\). These are onto, so Lesson 11, Theorem 4.1, applies. The difference map in degree zero is

\[
\mathbb Z^2\longrightarrow\mathbb Z,\qquad (a,b)\longmapsto a-b;
\tag{7.2}
\]

it is onto with diagonal kernel. In degree one its target \(K_1(\mathbb C)\) is zero. Exactness then makes \(K^0\) the diagonal \(\mathbb Z\), generated by the common unit, and makes restriction an isomorphism \(K^1\to\mathbb Z^2\). Explicit generators are the unitary equal to the positive circle coordinate on the first circle and one on the second, and the unitary with those roles interchanged. Their values agree at the common point, so they are actual continuous wedge unitaries.

**Exercise 12.4 — Integral torsion on the projective plane (intermediate).** Compute \(K^0(\mathbb{RP}^2)\) and \(K^1(\mathbb{RP}^2)\), and identify a nonzero torsion bundle difference.

*Solution.* Let \(X=\mathbb{RP}^2\), \(Y=\mathbb{RP}^1\). The closed upper hemisphere of \(S^2\), identified with a disc, gives the characteristic map \(\chi:D^2\to X\). Its interior maps homeomorphically to \(X\setminus Y\). On the equator a point \((\cos\theta,\sin\theta,0)\) maps to its real line. Identify \(Y\) with a circle by sending that line to \(e^{2i\theta}\). Thus the boundary restriction of \(\chi\) is the degree-two map.

Restriction along \(\chi\) gives a morphism from the extension for \((X,Y)\) to the disc/boundary extension. The ideal map is the homeomorphism of the interiors, and \(\chi^*[z]=[z^2]=2[z]\) on \(K^1(Y)\). Naturality and the positive disc computation of Lesson 11 give

\[
\begin{gathered}
\delta:K^1(Y)\longrightarrow K^0(X,Y),\\
\mathbb Z\longrightarrow\mathbb Z,\qquad \delta(1)=2\mathfrak b.
\end{gathered}
\tag{7.3}
\]

The other relative group is zero. The six-term sequence now says \(K^1(X)\) injects into \(\mathbb Z\) with image the kernel of multiplication by two, hence \(K^1(X)=0\). Its degree-zero part gives

\[
\begin{gathered}
0\longrightarrow\mathbb Z/2\xrightarrow{j_*}K^0(X)\\
\xrightarrow{r_*}\mathbb Z\longrightarrow0,\\
K^0(X)=\mathbb Z[1]\oplus(\mathbb Z/2)j_*(\mathfrak b).
\end{gathered}
\tag{7.4}
\]

The unit splits \(r_*\), and exactness makes the indicated torsion class nonzero.

To identify it geometrically, let \(L\) be the complexification of the tautological real line on \(X\). On \(Y\) the section

\[
\begin{gathered}
x_\theta=(\cos\theta,\sin\theta,0),\\
s([x_\theta])=e^{i\theta}x_\theta.
\end{gathered}
\tag{7.5}
\]

is well-defined: replacing \(\theta\) by \(\theta+\pi\) changes both factors' signs. It is a nonvanishing unit section, so define \(\sigma:L|_Y\to\mathbf1\) by \(\sigma(s)=1\). The triple \((L,\mathbf1,\sigma)\) maps, on forgetting its comparison, to \([L]-[1]\).

Over the upper hemisphere, \(\chi^*L\) has the unit frame \(x\), the point of the hemisphere itself. At its boundary, \(s=e^{i\theta}x\), so \(\sigma(x)=e^{-i\theta}\). Hence the pulled-back triple is the trivial disc comparison of winding minus one. Lemma 2.2 identifies its relative class with \(-\mathfrak b\). Since the ideal pullback is an isomorphism, the original relative triple has this class also. Therefore

\[
\begin{gathered}
{}[L]-[1]=-j_*(\mathfrak b)=j_*(\mathfrak b)\ne0,\\
2([L]-[1])=0.
\end{gathered}
\tag{7.6}
\]

Finally evaluation at any chosen point splits by the unit. The point-pair sequence (1.4) identifies \(K^0(X,\{x_0\})\) with the reduced group \(\mathbb Z/2\), generated by (7.6), and \(K^1(X,\{x_0\})=0\). Indeed evaluation is onto in degree zero, so its exponential boundary is zero; degree-one groups of the point are zero, so the relative degree-zero map is injective and has exactly the evaluation kernel. The cell pair supplied the degree-two boundary needed to compute that kernel; the point pair then gives the requested reduced description.

**Exercise 12.5 — A difference-bundle Thom representative (advanced).** Prove the trivial-line isomorphism for compact \(X\) and describe its value on a virtual bundle.

*Solution.* Under (3.1), its target is the relative group of \((X\times D^2,X\times S^1)\). For \([E]-[F]\), take the difference of the triples (3.4) for \(E\) and \(F\). Equivalently a single representative is

\[
\begin{gathered}
\bigl(\pi^*E\oplus\pi^*F,\ \pi^*E\oplus\pi^*F,\ \tau\bigr),\\
\tau=\operatorname{diag}(z\,\mathrm{id}_E,
\overline z\,\mathrm{id}_F).
\end{gathered}
\tag{7.7}
\]

The inverse-comparison relation makes the second block the negative of the \(F\) triple. If \(E,F\) are represented by projections \(e,f\), naturality with respect to \(\lambda\mapsto\lambda e\) and \(\lambda\mapsto\lambda f\) identifies (7.7) with \(\mathsf B_{C(X)}([e]-[f])\), as proved in Theorem 3.1. It therefore respects every group-completion relation. The inverse exists because \(\mathsf B=\theta\beta\) is an isomorphism; this proves both injectivity and surjectivity. For \(X\) a point, the triple \((\mathbf1,\mathbf1,z)\) is \(+\mathfrak b\), fixing the Thom sign. For general \(X\), the image of \([1_X]\) is the corresponding trivial-line Thom class; the entire target need not be cyclic.

## What this lesson imports and does not prove

The projection retraction and stable projection homotopy are imported from Lesson 1; the bundle–projection correspondence and cylinder transport from Lesson 2; stable unitary K-theory from Lesson 6; suspension and ordered Bott periodicity from Lessons 8 and 10; exactness, the disc boundary and full algebraic relative excision from Lesson 11. The rational Chern character (6.1), its construction, both boundary comparisons and the finite-cell argument are proved in §6. Theorems 6.5–6.7 also prove the integral projective-space ring and the projective-bundle basis over every compact Hausdorff base, in both K-degrees. Corollary 6.8 gives the integral K-theory splitting principle. A Thom isomorphism for a nontrivial complex vector bundle, the general Künneth theorem with torsion terms and the full torus ring structure are outside this lesson's claims; Lemma 6.6 proves the specific projective-space product needed here. Its relative-bundle identification, all group computations, unstable projection example and trivial-line Thom theorem are proved here using the specified imports.

## References

- **[Blackadar 1998]** B. Blackadar, *K-Theory for Operator Algebras*, second edition, MSRI Publications 5, Cambridge University Press, 1998, §§1.5–1.7; Theorem 1.6.6, printed p. 7; Exercise 9.4.1. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- **[Emerson 2024]** H. Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser Advanced Texts, 2024, §§7.1–7.6. The relative comparison is specified on the bundles themselves, and the projective-plane computation includes its attaching map.
- **[Weibel, Chern axioms]** Charles A. Weibel, *The K-book: An Introduction to Algebraic K-theory*, author-hosted Chapter I, §4, especially Chern-class axioms 4.13, chapter pp. 35–36, and Exercises 4.10–4.12, chapter p. 37. [Freely readable Chapter I](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.I.pdf#page=35). This is an axiomatic comparison: its splitting and Swan passages include exercises and external references. The complete constructions used here remain Lemmas 6.2–6.4 and the proof of Theorem 6.1, compared with Hatcher’s fully written projective-bundle and character arguments. Chapter pagination differs from the AMS printed book.
- **[Connes 1994]** A. Connes, *Noncommutative Geometry*, Academic Press, 1994, Chapter II, §1, printed pp. 86–90. [Author's electronic edition](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf#page=86).

- **[Hatcher]** A. Hatcher, *Vector Bundles and K-Theory*, version 2.2, November 2017, §3.1, Theorem 3.2 and Proposition 3.3 with their proofs, printed pp. 78–81 (PDF pp. 82–85), and Proposition 3.10, printed p. 86 (PDF p. 90); §4.1, Chern-character construction and Propositions 4.2–4.5, printed pp. 109–111 (PDF pp. 113–115). [Freely readable author edition](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf#page=82). Theorem 3.2 permits either specified generator for the line normalization; this lesson fixes c₁ of the tautological line as minus the complex-oriented hyperplane generator. Its alternating projective relation and explicit boundary signs are preserved.

- **[Hatcher, projective bundles]** A. Hatcher, *Vector Bundles and K-Theory*, version 2.2, November 2017, Proposition 2.23, Proposition 2.24, Theorem 2.25(b), Example 2.26, the splitting-principle proof and Proposition 2.27, printed pp. 66–71. [Freely available author draft](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf#page=70). The argument here independently proves the integral projective-space normalization using the already established character, proves the arbitrary compact-base theorem by coefficient Bott maps and a finite closed cover, and derives the full ring relation from exterior powers. No source expression is adapted.
