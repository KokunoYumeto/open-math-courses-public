# Suspension, higher K-groups and the long exact sequence

*Written by GPT-6.1 Sol (OpenAI) in Codex, at Ultra. Independently authored CC0 lesson. Mathematical revisions by GPT-6 Astra (OpenAI), at Ultra.*

An invertible matrix can be doubled with its inverse and joined to the identity. Conjugating a fixed projection along that path produces an idempotent loop. This turns an invertible component into a relative projective class over a suspension. The cone extension explains why every such class occurs and why the construction is injective.

We use [The index map and the exact sequence at \(K_0\)](KT-OPK-07.md), especially [its Theorem 4.1](KT-OPK-07.md#4-exactness-at-the-four-interior-groups), [normalized boundary construction (Theorem 2.2)](KT-OPK-07.md#2-the-idempotent-associated-to-a-doubled-lift), and [Lemmas 3.1–3.2 on finite stabilization](KT-OPK-07.md#3-what-a-zero-k_0--difference-provides). [Homotopy invariance for nonunital algebras (Lesson 7, Section 6)](KT-OPK-07.md#6-the-fredholm-sign-and-a-cone-extension), normalized \(K_1\), and matrix stability come from [Lesson 3, Section 4](KT-OPK-03.md#4-changing-the-algebra), [Lesson 6, Proposition 1.2](KT-OPK-06.md#1-a-definition-that-keeps-the-scalar-part-fixed) and [Lesson 6, Section 3](KT-OPK-06.md#3-functoriality-and-finite-matrix-properties). Unless explicitly stated otherwise, algebras below are arbitrary complex C*-algebras, maps are *-homomorphisms, and unitizations are external. The suspension isomorphism itself also holds for complex Banach algebras, with bounded homomorphisms.

## 1. Cones, suspensions, and lifting continuous functions

Define

\[
\begin{aligned}
SA&=\{f\in C([0,1],A):\\
&\qquad f(0)=f(1)=0\},\\
CA&=\{f\in C([0,1],A):\\
&\qquad f(0)=0\}.
\end{aligned}
\tag{1.1}
\]

Both have pointwise operations and the supremum norm. They are closed ideals in \(C([0,1],A)\), hence C*-algebras. Restriction identifies them with \(C_0((0,1),A)\) and \(C_0((0,1],A)\), respectively. A fixed homeomorphism from \((0,1)\) onto \(\mathbb R\) gives the usual real-line suspension. Matrices commute with these constructions by taking entries. A homomorphism \(\phi:A\to B\) induces \(S\phi\) and \(C\phi\) pointwise, and both constructions preserve composition.

Evaluation at the nonvanishing endpoint gives

\[
0\longrightarrow SA\longrightarrow CA
\xrightarrow{\operatorname{ev}_1}A\longrightarrow0.
\tag{1.2}
\]

It is onto: \(a\) is the value at 1 of \(t\mapsto ta\). This is a linear lift; multiplicativity is not needed for surjectivity.

**Proposition 1.1 (cone contraction).** The identity homomorphism of \(CA\) is homotopic to the zero homomorphism. Consequently \(K_0(CA)=K_1(CA)=0\).

*Proof.* For \(0\leq r\leq1\), put

\[
(H_r f)(t)=f(rt).
\tag{1.3}
\]

This is a *-homomorphism into \(CA\); its norm is at most one. Uniform continuity of each \(f\) on the compact interval makes \(r\mapsto H_r f\) norm continuous. At \(r=1\) it is the identity, and at \(r=0\) it is zero because \(f(0)=0\). Homotopy invariance makes the identity map of either K-group equal to its zero map. A group whose identity homomorphism is zero is the zero group. The same proof applies to Banach algebras. \(\square\)

To suspend a general extension, surjectivity on continuous functions must be proved. A quotient map need not have a bounded linear section.

**Lemma 1.2 (endpoint-preserving lifts).** Let \(q:E\to F\) be a surjective bounded linear map between Banach spaces. Every continuous \(F\)-valued function on \([0,1]\) has a continuous lift. If it vanishes at either or both endpoints, the lift can be chosen to vanish at those endpoints.

*Proof.* [The open mapping theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#OA-FND-HB-05) gives a constant \(M\) such that every \(b\in F\) has a lift \(a\) with \(\|a\|\leq M\|b\|\); enlarge the constant if necessary to avoid an attained-infimum assertion. Begin with a residual \(r_0=f\). Choose a partition fine enough that its piecewise linear interpolant \(v_0\), formed from the values of \(r_0\) at the nodes, satisfies

\[
\|r_0-v_0\|_\infty\leq\tfrac12\|r_0\|_\infty.
\]

If the residual is zero, stop. Lift every node value with the stated bound and interpolate the lifts on the same partition. Choose the zero lift at each endpoint where the original function vanishes. The resulting function \(a_0\) has \(qa_0=v_0\) and \(\|a_0\|_\infty\leq M\|r_0\|_\infty\).

Repeat this construction for \(r_{m+1}=r_m-qa_m\). The prescribed zero endpoints remain zero, and

\[
\begin{aligned}
\|r_m\|_\infty&\leq2^{-m}\|f\|_\infty,\\
\|a_m\|_\infty&\leq M2^{-m}\|f\|_\infty.
\end{aligned}
\]

Completeness gives uniform convergence of \(\sum_m a_m\) to a continuous function \(a\) with the required endpoints. Boundedness of \(q\) gives \(qa=f\), since the residual tends uniformly to zero. \(\square\)

**Corollary 1.3 (suspending extensions).** Every C*-algebra extension

\[
E:\quad 0\longrightarrow J\xrightarrow{\iota}A
\xrightarrow{\pi}B\longrightarrow0
\tag{1.4}
\]

induces an extension \(0\to SJ\to SA\to SB\to0\). Thus \(SA/SJ\cong SB\), and the same assertion holds after any finite number of suspensions.

*Proof.* The pointwise kernel is precisely the continuous functions taking values in \(J\) and vanishing at both endpoints. Lemma 1.2 proves surjectivity, with both endpoints fixed at zero. The induced bijective *-homomorphism from the C*-quotient is an isometric isomorphism by [C*-algebras, Theorem 15.1 and Corollary 15.4](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-25); [Corollary 4.6](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-12) gives the isometry of an injective *-homomorphism. Repeating the argument proves the last assertion. \(\square\)

## 2. The idempotent loop of an invertible

Write \(G_n^1(A)=\{u\in GL_n(A^+):\epsilon_A(u)=I_n\}\), as in [Invertibles, unitaries and \(K_1\)](KT-OPK-06.md), and set \(P_n=\operatorname{diag}(I_n,0_n)\). For \(u\in G_n^1(A)\), choose a path

\[
\begin{gathered}
z:[0,1]\longrightarrow G_{2n}^1(A),\\
z(0)=I_{2n},\\
z(1)=\operatorname{diag}(u,u^{-1}).
\end{gathered}
\tag{2.1}
\]

Here is a path available without making any choice of logarithm of \(u\). Let

\[
\begin{gathered}
R_a=\begin{pmatrix}\cos a\,I_n&-\sin a\,I_n\\
\sin a\,I_n&\cos a\,I_n\end{pmatrix},\\
a(t)=\tfrac\pi2(1-t),
\end{gathered}
\]

and take

\[
\begin{aligned}
z(t)&=\operatorname{diag}(u,I_n)R_{a(t)}\\
&\quad\cdot\operatorname{diag}(I_n,u^{-1})R_{a(t)}^{-1}.
\end{aligned}
\tag{2.2}
\]

At \(t=0\), the rotation exchanges the two blocks and the product is identity. At \(t=1\), the rotation is identity and the product is the required doubled matrix. Augmentation makes the two diagonal factors identity, so the scalar part of the product is identity for every \(t\). Each factor is invertible, and if \(u\) is unitary the path is unitary.

Put \(e(t)=z(t)P_nz(t)^{-1}\). It is an idempotent, with scalar part \(P_n\) and with \(e(0)=e(1)=P_n\). Hence \(e-P_n\in M_{2n}(SA)\), so

\[
\theta_A[u]=[e]-[P_n]\in K_0(SA).
\tag{2.3}
\]

An element of \((CA)^+\) can be viewed as an \(A^+\)-valued continuous function whose scalar part is constant and whose value at 0 is that scalar. The path \(z\) is therefore a normalized invertible over \((CA)^+\). Its endpoint is exactly the doubled quotient representative in the boundary formula of Lesson 7.

**Theorem 2.1 (suspension isomorphism).** Formula (2.3) is independent of the path, representative, and finite matrix size. It defines a natural group isomorphism

\[
\theta_A:K_1(A)\xrightarrow{\cong}K_0(SA).
\tag{2.4}
\]

With the endpoint convention (1.1), it equals the index boundary of (1.2), with coefficient \(+1\).

*Proof.* Formula (2.3) is literally the normalized invertible-lift formula for that boundary. [Lesson 7, Theorem 2.2](KT-OPK-07.md#2-the-idempotent-associated-to-a-doubled-lift), proves independence of doubled lifts, invariance under stabilized homotopy, and additivity. These apply to any choice of the path in (2.1), since every such path is a doubled lift over \((CA)^+\). Thus they prove all the well-definedness assertions here.

The four-interior exact sequence of [Lesson 7, Theorem 4.1](KT-OPK-07.md#4-exactness-at-the-four-interior-groups), applied to (1.2), contains

\[
\begin{gathered}
K_1(CA)\longrightarrow K_1(A)
\xrightarrow{\theta_A}K_0(SA)\\
\longrightarrow K_0(CA).
\end{gathered}
\]

Proposition 1.1 makes both outside groups zero. Exactness at the two middle groups proves injectivity and surjectivity of \(\theta_A\). The sign follows from the equality of formulas, not from exactness alone.

For \(\phi:A\to B\), pointwise application gives a morphism of the two cone extensions with ideal map \(S\phi\) and quotient map \(\phi\). Boundary naturality yields

\[
(S\phi)_*\theta_A=\theta_B\phi_*.
\tag{2.5}
\]

This includes nonunital maps: their external extensions fix \(P_n\) and preserve the normalized path. Every step also works for Banach algebras, using their norm-continuous invertibles and the Banach version of Lesson 7. \(\square\)

## 3. Higher groups and the long sequence

For \(n\geq0\) define

\[
\begin{gathered}
K_n(A)=K_0(S^nA),\\
S^0A=A.
\end{gathered}
\tag{3.1}
\]

At \(n=1\), this is identified with the already defined invertible-component group by \(\theta_A\). We use that identification whenever \(K_1\) appears in a sequence. In general

\[
K_n(A)\cong K_1(S^{n-1}A)\quad(n\geq1)
\tag{3.2}
\]

by \(\theta_{S^{n-1}A}^{-1}\). There is no periodicity claim at this stage.

For the extension \(E\) in (1.4), let \(\partial_{S^{n-1}E}\) be the index boundary of its \((n-1)\)-fold suspension. Define

\[
\begin{aligned}
\partial_n &:K_n(B)\longrightarrow K_{n-1}(J),\\
\partial_n&=\partial_{S^{n-1}E}\theta_{S^{n-1}B}^{-1}.
\end{aligned}
\tag{3.3}
\]

In particular \(\partial_1\) is exactly the index boundary already fixed.

**Theorem 3.1 (long exact sequence).** Every extension (1.4) gives a natural sequence

\[
\begin{gathered}
\cdots\longrightarrow K_{n+1}(B)\\
\xrightarrow{\partial_{n+1}}K_n(J)
\xrightarrow{\iota_*}K_n(A)\\
\xrightarrow{\pi_*}K_n(B)
\xrightarrow{\partial_n}K_{n-1}(J)\\
\longrightarrow\cdots\longrightarrow K_1(B)\\
\xrightarrow{\partial_1}K_0(J)
\longrightarrow K_0(A)\\
\longrightarrow K_0(B).
\end{gathered}
\tag{3.4}
\]

It is exact at every displayed group except the final \(K_0(B)\), where no surjectivity is asserted.

*Proof.* Exactness at \(K_n(A)\) is \(K_0\)-half-exactness for the \(n\)-fold suspended extension. For exactness at \(K_n(B)\), use (3.2). Naturality (2.5) transports the map from \(K_n(A)\) to the map on \(K_1(S^{n-1}A)\). The assertion then becomes exactness at the quotient \(K_1\)-group in Lesson 7. Its outgoing map transports to (3.3).

Exactness at \(K_{n-1}(J)\) is exactness at the ideal \(K_0\)-group of the \((n-1)\)-fold suspended extension, again Lesson 7. These arguments cover all interior groups. At \(K_0(J)\) and \(K_0(A)\) they are precisely the two already proved exactness statements, and there is no appended zero at the right. Corollary 1.3 ensures that every extension used in this argument actually exists.

A morphism of extensions induces morphisms of all their suspensions. Naturality of the index boundaries and of \(\theta^{-1}\) proves naturality of (3.3); functoriality proves it for the other arrows. Thus the entire long sequence is natural. \(\square\)

Every \(K_n\) is homotopy invariant: suspend a point-norm homotopy and apply \(K_0\)-homotopy invariance. For completeness, point-norm continuity on suspension-valued functions is uniform on their compact range, by a finite approximation of that range and the norm bound one for *-homomorphisms. This proves the needed suspended point-norm continuity. Consequently homotopy-equivalent C*-algebras have isomorphic groups in every degree: the two induced compositions are identities because the original compositions are homotopic to identities. Cone contraction, applied in the cone coordinate after any number of suspensions, also gives \(K_n(CA)=0\) for every \(n\).

## 4. The line and plane before periodicity

Here \(K_*\) means the two groups \(K_0,K_1\), not a claim about every higher degree. The first computations are

\[
\begin{array}{c|cc}
A&K_0(A)&K_1(A)\\\hline
\mathbb C&\mathbb Z&0\\
C_0(\mathbb R)&0&\mathbb Z\\
C_0(\mathbb R^2)&\mathbb Z&0.
\end{array}
\tag{4.1}
\]

The first row was proved in [Lesson 3, Example 5.1](KT-OPK-03.md#5-calculations-dimensions-absorption-and-bundles) and [Lesson 6, Theorem 5.1, applied to the scalar von Neumann algebra](KT-OPK-06.md#5-components-detected-by-spectra-winding-and-index). For the second, [Lesson 4, Proposition 6.1](KT-OPK-04.md#6-compact-supports-and-the-determinant-at-the-equator), gives \(K_0=0\); [Lesson 6, Theorem 5.2](KT-OPK-06.md#winding-detects-the-circle-group) computes \(K_1\) by counterclockwise winding. In interval coordinates a generator is

\[
\omega(s)=e^{2\pi is},\qquad 0\leq s\leq1.
\tag{4.2}
\]

Its endpoint values are identity, so it is a normalized unitary over \((S\mathbb C)^+\). Theorem 2.1 applied to \(S\mathbb C\) proves

\[
K_0(S^2\mathbb C)=\mathbb Z\,
\theta_{S\mathbb C}[\omega].
\tag{4.3}
\]

For the plane's \(K_1\), use [Invertibles, unitaries and \(K_1\)](KT-OPK-06.md), [Section 5, “Sphere maps and unitary transport,” Proposition “The determinant and the second homotopy group”](KT-OPK-06.md#sphere-maps-and-unitary-transport). It proves \(\pi_2(U(n),I_n)=0\) at every finite matrix size: based sphere contractions and the explicit compact-family unitary lift reduce a two-sphere map to a scalar map, whose continuous argument contracts it. A normalized unitary over \(C_0(\mathbb R^2)^+=C(S^2)\) is precisely a map \(S^2\to U(n)\) taking infinity to \(I_n\), so that proposition gives a homotopy with the same value at infinity. Every stage remains a normalized unitary in the function algebra. The based polar deformation treats normalized invertibles as well. Consequently every representative is zero in \(K_1\), proving the plane's \(K_1=0\). This uses no periodicity theorem.

### Fixing the generator's sign

Write the two suspension coordinates in the order \((t,s)\): \(t\) is the new, outer suspension coordinate, and \(s\) is the coordinate of \(S\mathbb C\). Identify the open square with the oriented plane by

\[
\begin{aligned}
x&=-\cot(\pi t),\\
y&=-\cot(\pi s),\\
z&=x+iy.
\end{aligned}
\tag{4.4}
\]

Both derivatives are positive, so \(dt\wedge ds\) corresponds to \(dx\wedge dy\). Collapsing the square's boundary gives its one-point compactification, which is the sphere.

Apply (2.2) to \(u=\omega(s)\). Put \(c=\cos a(t)\), \(r=\sin a(t)\). The first column of this unitary path is

\[
\begin{aligned}
\xi(t,s)&=\begin{pmatrix}
c^2\omega(s)+r^2\\
cr(1-\omega(s)^{-1})
\end{pmatrix},\\
e(t,s)&=\xi(t,s)\xi(t,s)^*.
\end{aligned}
\tag{4.5}
\]

Because the matrix path is unitary, \(\xi^*\xi=1\). The vector \(\xi\) is therefore a nonvanishing frame on the entire square before its boundary is collapsed. On that boundary,

\[
\begin{array}{c|c}
\text{edge}&\xi\\\hline
t=0&(1,0)^T\\
t=1&(\omega(s),0)^T\\
s=0\text{ or }s=1&(1,0)^T.
\end{array}
\tag{4.6}
\]

Thus \(e\) equals \(P=\operatorname{diag}(1,0)\) everywhere on the boundary and descends to a line bundle on the sphere.

Use a small boundary collar for the disc about infinity. There \(e\) is close to \(P\), so

\[
\eta=\frac{e(1,0)^T}{\|e(1,0)^T\|}
\]

is a continuous unit frame and descends across the collapsed boundary, where it is \((1,0)^T\). If \(\xi_1\) denotes the first entry of \(\xi\), then on the collar

\[
\eta=\xi\frac{\overline{\xi_1}}{|\xi_1|},
\qquad
\xi=\eta\frac{\xi_1}{|\xi_1|}.
\tag{4.7}
\]

Choose a central closed rectangle whose boundary lies in this collar. Its interior and the infinity disc give the two trivializations. The coefficient transfer from the central frame to the infinity frame is therefore \(g=\xi_1/|\xi_1|\) on the rectangle's positively oriented boundary. It has the same winding as the limiting outer-boundary function: uniform continuity, together with \(|\xi_1|=1\) on the outer boundary, gives a nonvanishing homotopy between the two sufficiently close boundary functions.

For the orientation \(dt\wedge ds\), the outer boundary travels along \(s=0\) with \(t\) increasing, then along \(t=1\) with \(s\) increasing, then back along \(s=1\) and \(t=0\). Formula (4.6) shows that only the second edge contributes: it is the positive loop \(\omega(s)\). Consequently the finite-to-infinity clutching degree of \(e\) is \(+1\).

Let \(\mathfrak b\) denote the relative class in [Lesson 4, Theorem 6.2](KT-OPK-04.md#6-compact-supports-and-the-determinant-at-the-equator):

\[
\begin{gathered}
q(z)=\frac1{1+|z|^2}
\begin{pmatrix}1&\overline z\\z&|z|^2\end{pmatrix},\\
q(\infty)=\operatorname{diag}(0,1),\\
\mathfrak b=[q]-[q(\infty)].
\end{gathered}
\tag{4.8}
\]

That lesson proves \(d(\mathfrak b)=1\), using the same finite-to-infinity coefficient-transfer convention. We have just proved \(d(\theta_{S\mathbb C}[\omega])=1\). By (4.3) the latter is a generator of the whole relative group. Hence \(d\) is an isomorphism on that group, and

\[
\begin{gathered}
\boxed{\theta_{S\mathbb C}[\omega]=\mathfrak b}\\
\text{in the coordinate order }(t,s).
\end{gathered}
\tag{4.9}
\]

Interchanging the two plane coordinates reverses the boundary orientation and changes the clutching degree to \(-1\). With that reversed identification the same suspension construction represents \(-\mathfrak b\). Thus a sign comparison must state its coordinate order.

The “positive loop” convention in *Frequency calculus for an action of Euclidean space*, Lemma 7.4, concerns a different typed map:

\[
\begin{aligned}
\beta_A:K_0(A)&\longrightarrow K_1(SA),\\
[p]-[P]&\longmapsto[u],\\
u(t)&=\exp(2\pi itp)\\
&\quad\cdot\exp(-2\pi itP).
\end{aligned}
\tag{4.10}
\]

Its scalar generator is \(\omega\). Its general isomorphism assertion is Bott periodicity, proved in the later lesson of that title. Formula (4.9) compares that positive scalar loop with our \(\theta\) without using the general assertion. The two maps (2.4) and (4.10) have different domains and codomains; a blanket equation \(\theta=-\beta\) would be ill-typed. Their composition \(\theta_{SA}\beta_A\) has target \(K_0(S^2A)\). The initial convention block of *K-theory of the leaf space* likewise distinguishes the two maps and uses the positive exponential loop in (4.10).

## 5. Mapping cones and the map they encode

For any \(\phi:A\to B\), define

\[
\begin{aligned}
C_\phi&=\{(a,f)\in A\oplus CB:\\
&\qquad f(1)=\phi(a)\}.
\end{aligned}
\tag{5.1}
\]

This is a closed C*-subalgebra. The projection \(q(a,f)=a\) gives an extension

\[
\begin{gathered}
0\longrightarrow SB\xrightarrow{j}C_\phi\\
\xrightarrow{q}A\longrightarrow0,\\
j(f)=(0,f).
\end{gathered}
\tag{5.2}
\]

It is onto because \((a,t\mapsto t\phi(a))\) is a lift of \(a\). Its kernel is exactly \(SB\).

For the shifted ideal term, fix its coordinate identification explicitly. An element of \(S^{n-1}(SB)\) has coordinates \((r_1,\ldots,r_{n-1},t)\), where \(t\) is the original mapping-cone coordinate. Let

\[
\begin{gathered}
(T_n f)(t,r_1,\ldots,r_{n-1})=\\
f(r_1,\ldots,r_{n-1},t).
\end{gathered}
\tag{5.3}
\]

Thus \(T_n:S^{n-1}(SB)\to S^nB\) brings that coordinate to the first position, and \(T_1\) is identity. It is a natural *-isomorphism. Use its induced map when identifying \(K_{n-1}(SB)\) with \(K_n(B)\).

**Theorem 5.1 (mapping-cone sequence).** Under (3.2) and this ideal-coordinate identification, the connecting homomorphism of (5.2) is \(\phi_*\). In particular there is an exact sequence

\[
\begin{gathered}
\cdots\longrightarrow K_{n+1}(B)\\
\longrightarrow K_n(C_\phi)\xrightarrow{q_*}K_n(A)\\
\xrightarrow{\phi_*}K_n(B)\longrightarrow\cdots.
\end{gathered}
\tag{5.4}
\]

ending in \(K_0(C_\phi)\to K_0(A)\xrightarrow{\phi_*}K_0(B)\). Exactness is asserted at every interior term, including \(K_0(A)\), but not surjectivity onto the final \(K_0(B)\).

*Proof.* The map \(F:C_\phi\to CB\), \(F(a,f)=f\), gives a morphism from (5.2) to the cone extension of \(B\). Its ideal map is the identity on \(SB\), and its quotient map is \(\phi\). Boundary naturality gives

\[
\begin{aligned}
\partial_{C_\phi}&=\theta_B\phi_*,\\
\partial_{C_\phi}&:K_1(A)\longrightarrow K_0(SB).
\end{aligned}
\tag{5.5}
\]

After \(n-1\) suspensions, the doubled path for a representative \(u(r_1,\ldots,r_{n-1})\) conjugates \(P\) in the cone variable \(t\). The boundary therefore has coordinates \((r_1,\ldots,r_{n-1},t)\), whereas \(\theta_{S^{n-1}B}\) places the path variable first. Applying \(T_n\) makes these two formulas identical. With \(\partial_n\) defined by (3.3), the resulting equality is

\[
\begin{aligned}
(T_n)_*\partial_n^{C_\phi}&=\phi_*,\\
\phi_*&:K_n(A)\longrightarrow K_n(B).
\end{aligned}
\tag{5.6}
\]

Naturality handles all representatives and nonunital maps. Identify the other ideal term \(K_n(SB)\) with \(K_{n+1}(B)\) using \((T_{n+1})_*\) as well. Transporting Theorem 3.1 by these isomorphisms proves (5.4) down to \(K_0(C_\phi)\to K_0(A)\). Explicit coordinate transport prevents an unrecorded permutation from becoming a sign convention.

We prove its additional exactness assertion at \(K_0(A)\) directly. The homomorphisms \((a,f)\mapsto f(r)\), \(0\leq r\leq1\), form a point-norm homotopy from zero to \(\phi q\). Hence \(\phi_*q_*=0\).

Conversely let \(x\in K_0(A)\) with \(\phi_*x=0\). Use [Lesson 4's normal form](KT-OPK-04.md#1-recording-the-scalar-part) \(x=[e]-[P]\), where \(e\) is an idempotent over \(A^+\), with scalar part the scalar projection \(P\). Its image has \([\phi^+(e)]=[P]\) over \(B^+\). [Lesson 7, Lemma 3.1](KT-OPK-07.md#3-what-a-zero-k_0--difference-provides), adds common identity and zero blocks to produce padded idempotents \(e'\), \(P'\), and an invertible path \(w(r)\), starting at identity, such that

\[
w(1)P'w(1)^{-1}=\phi^+(e').
\]

At its endpoint the scalar matrix of \(w(1)\) commutes with \(P'\). Normalize the entire path by

\[
y(r)=w(r)\epsilon_B(w(r))^{-1}.
\]

It starts at identity, has scalar part identity throughout, and its final conjugation still gives \(\phi^+(e')\). Thus \(h(r)=y(r)P'y(r)^{-1}\) is an idempotent path with scalar part \(P'\), starting at \(P'\) and ending at \(\phi^+(e')\). The pair \((e',h)\) is an idempotent over \((C_\phi)^+\): subtracting its scalar reference gives an element of the mapping cone, since the function starts at zero and ends at \(\phi^+(e')-P'\). The class

\[
[(e',h)]-[P']\in K_0(C_\phi)
\]

maps to \([e']-[P']=x\). This proves \(\ker\phi_*\subset\operatorname{im}q_*\) and finishes the proof. \(\square\)

**Example 5.2 (scalar inclusion into two-by-two matrices).** Take \(\phi:\mathbb C\to M_2(\mathbb C)\), \(\phi(\lambda)=\lambda I_2\). Rank gives \(\phi_*:K_0(\mathbb C)\to K_0(M_2(\mathbb C))\) as multiplication by 2. Since both \(K_1\)-groups vanish, the bottom of (5.4) gives

\[
K_0(C_\phi)=0.
\tag{5.7}
\]

For degree 1, use \(K_2(\mathbb C)=\mathbb Z\) from (4.3), and \(K_2(M_2(\mathbb C))=\mathbb Z\) by matrix stability. Naturality of \(\theta\) identifies the degree-2 map \(\phi_*\) with the suspended \(K_1\)-map. The determinant of \(\omega I_2\) is \(\omega^2\), so that map is again multiplication by 2. Exactness therefore gives

\[
\begin{aligned}
K_1(C_\phi)&=\operatorname{coker}(2:\mathbb Z\to\mathbb Z)\\
&=\mathbb Z/2.
\end{aligned}
\tag{5.8}
\]

Its generator is the image from the ideal \(SM_2(\mathbb C)\) of the based loop \(g(t)=\operatorname{diag}(e^{2\pi it},1)\): explicitly the normalized unitary is \(1+j(g-I_2)\). This class has order exactly 2 by the cokernel computation. All inputs to (5.7)–(5.8) were proved before general Bott periodicity.

## 6. Exercises with complete solutions

**Exercise 8.1 — Contracting the cone (basic).** Construct a homotopy contracting \(CA\), and prove that all its higher groups vanish.

*Solution.* Use \(H_r\) in (1.3). Evaluation at \(rt\) preserves products, adjoints and addition, and \(f(0)=0\) makes \(H_0=0\). Uniform continuity gives the required point-norm homotopy to \(H_1=\mathrm{id}\). After any finite number of suspensions apply this same homotopy in the cone variable. Equivalently, suspended functions have compact range in \(CA\), so point-norm continuity is uniform on that range as explained after Theorem 3.1. The identity on \(K_0(S^nCA)\) is thus its zero map. Therefore \(K_n(CA)=0\) for every \(n\geq0\).

**Exercise 8.2 — The suspended quotient (basic).** Prove \(S(A/J)\cong SA/SJ\) for an arbitrary closed ideal of a C*-algebra.

*Solution.* Pointwise quotient sends \(SA\) into \(S(A/J)\). Its kernel is \(SJ\), because a function is in that kernel precisely when all its values lie in \(J\). For a target function vanishing at both endpoints, apply Lemma 1.2 to the Banach-space quotient \(A\to A/J\). Each polygonal approximate lift is zero at both endpoints; the uniformly convergent sum remains zero there and has the exact target image. This proves surjectivity without a linear section. The induced bijective *-homomorphism of the C*-quotient is an isometric isomorphism.

**Exercise 8.3 — The cone boundary and its sign (intermediate).** Identify \(\theta_A\) with the boundary of the cone extension, including nonunital algebras.

*Solution.* Represent a class by \(u\in G_n^1(A)\) and choose (2.2). Its value at 0 is identity and its scalar part is constantly identity, so \(z\) is a normalized invertible over \((CA)^+\). Evaluation at 1 gives \(\operatorname{diag}(u,u^{-1})\). The boundary formula of Lesson 7 is \([zP_nz^{-1}]-[P_n]\), exactly (2.3). Their equality has sign \(+1\). Since the scalar part of the conjugated projection is \(P_n\) and both endpoint values equal \(P_n\), its difference from \(P_n\) lies in \(M_{2n}(SA)\). No ordinary unit of \(A\) is needed; every identity used here is the external unit. Theorem 2.1 proves that this equality descends to all K-classes and is an isomorphism.

**Exercise 8.4 — The mapping-cone sequence (intermediate).** Derive the sequence for \(C_\phi\) and identify its connecting maps.

*Solution.* Projection onto \(A\) is onto via \((a,t\phi(a))\), and its kernel is \(SB\). Map this extension to \(0\to SB\to CB\to B\to0\) by \((a,f)\mapsto f\), identity on the ideal and \(\phi\) on the quotient. Boundary naturality gives (5.5). Suspend this diagram \(n-1\) times and use \(\theta^{-1}\), bringing the mapping-cone variable to the first position with \(T_n\). Formula (5.6) gives exactly \(\phi_*:K_n(A)\to K_n(B)\). Transport the adjacent ideal term using \(T_{n+1}\); the long extension sequence becomes (5.4). At \(K_0(A)\), the evaluation homotopy gives zero composite and the padded, scalar-normalized idempotent path in Theorem 5.1 lifts every kernel class into \(C_\phi\). These establish all claimed exactness statements, including that final interior one.

**Exercise 8.5 — The two-plane generator (advanced).** Compare the suspension of the positive winding generator with the relative Bott class (4.8).

*Solution.* Distinguish the winding unitary \(\omega\in K_1(S\mathbb C)\) from the idempotent class \(\mathfrak b\in K_0(S^2\mathbb C)\). Substitute \(\omega(s)\) into the doubled path (2.2); its unit first column is (4.5). The resulting rank-one projection equals \(P\) on the square's boundary. On a collar its infinity frame is \(\eta\), and the transfer from \(\xi\) to \(\eta\) is (4.7). With the outer coordinate \(t\) first and inner coordinate \(s\) second, the positive boundary travels upward along \(t=1\). There the transfer is \(\omega(s)\); on the other three edges it is 1. Its winding is therefore \(+1\). The collar argument makes this the actual clutching degree on a finite interior boundary, not merely a limiting formal loop.

The class \(\theta_{S\mathbb C}[\omega]\) generates the whole relative group by Theorem 2.1 and the line's \(K_1\) computation. Its degree is 1, so degree is injective on that cyclic group. Lesson 4 gives \(d(\mathfrak b)=1\), proving equality (4.9). Reversing the coordinate order changes the boundary orientation and gives the negative class. This determines the sign with the stated course coordinates and explains which change would reverse it.

## What this lesson does not prove

The finite unitary-group topology used in the plane's \(K_1\) computation is proved in the preceding lesson *Invertibles, unitaries and \(K_1\)*, Section 5, as specified in Section 4 here. General Bott periodicity, including the isomorphism assertion for (4.10), is proved in the subsequent Bott-periodicity lesson. No computation in this lesson assumes it. The long sequence (3.4) has no degree-zero boundary continuing it cyclically yet; that requires periodicity and the exponential map.

## References and convention checks

The path-conjugation suspension map is [B98, Theorem 8.2.2]. The cone argument identifies it with the same index boundary already proved in the preceding lesson, and the long sequence uses [B98, §8.3]. The proof of suspended surjectivity and the finite-witness proof at the bottom of the mapping-cone sequence are included explicitly.

The positive exponential loop in *Frequency calculus for an action of Euclidean space*, Lemma 7.4, has the type (4.10). The section “Suspension, Bott periodicity and extension boundaries” of *K-theory of the leaf space* uses that loop and cites the separate suspension isomorphism. Their comparison here is the typed scalar calculation (4.9), with ordered coordinates (4.4).

- [B98] B. Blackadar, *K-Theory for Operator Algebras*, second edition, Cambridge University Press, 1998, §§8.2–8.3, printed pp. 61–64, especially Theorem 8.2.2 and Definition 8.3.1. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- [B06] B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Springer, 2006, revised author version 2017, V.1.2.8–V.1.2.9 for suspension, V.1.2.12 for the boundary, and V.1.2.15 for the higher sequence.
- [E24] H. Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser, 2024, §§8.3–8.5. Its suspension-defined \(K_1\) and mapping-cone viewpoint are compared with the invertible-component definition used here.
- [H] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002, Proposition 4.1, Corollary 4.9, Theorem 4.41 and the unitary bundle in Example 4.55, for comparison with the standard topology route. The exact proof provider used here is Lesson 6, Section 5. [Author’s text](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf)
