# Nonunital algebras: unitization, relative classes and half-exactness

This lesson was written with GPT-6.1 Sol (OpenAI), in Codex, at the Ultra setting. Self-checked by the writing AI.

A projection in a matrix algebra over \(C_0(\mathbb R^2)\) must vanish. Nevertheless, the projection describing the tautological line on the compactified plane determines a nonzero K-theory class. The missing information is a comparison with a projection at infinity. Unitization makes that comparison available and makes exactness for ideals possible.

We use the group completion, identity stabilization and functoriality proved in [The Grothendieck group and \(K_0\) of a unital algebra](KT-OPK-03.md). The elementary projection and idempotent results are those of [Idempotents, projections and their equivalences](KT-OPK-01.md). The sphere coordinates and winding convention are those of [Vector bundles and finitely generated projective modules](KT-OPK-02.md). All algebras are complex. Banach-algebra homomorphisms are bounded, and C*-algebra homomorphisms are *-homomorphisms. Ideals are closed and two-sided. Matrices act on columns and modules are right modules.

## 1. Recording the scalar part

For any Banach algebra \(A\), including a unital one, its external unitization is

\[
A^+=A\oplus\mathbb C,\qquad
(a,\lambda)(b,\mu)=(ab+\lambda b+\mu a,\lambda\mu).
\]

Its identity is \((0,1)\). A compatible complete algebra norm, for example \(\|a\|+|\lambda|\), suffices in the Banach case. The complete norm constructions are [Banach algebras, Construction 3.2 and Proposition 3.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#OA-FND-BN-04), [Proposition 3.4](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#OA-FND-BN-05) and [Exercise 5 for an already unital C*-algebra](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html#exercises). Write \(a+\lambda1\) for \((a,\lambda)\), and let \(\epsilon_A:A^+\to\mathbb C\) be \(a+\lambda1\mapsto\lambda\). A homomorphism \(\phi:A\to B\) has the unital extension \(\phi^+(a+\lambda1)=\phi(a)+\lambda1\).

To distinguish two constructions while proving their agreement, put

\[
K_0^{\mathrm{alg}}(D)=G(V_{\mathrm{id}}(D))
\]

for a unital Banach algebra \(D\). This is the preceding lesson's group, not algebraic higher K-theory. Define

\[
\boxed{K_0(A)=\ker\bigl((\epsilon_A)_*:K_0^{\mathrm{alg}}(A^+)\to
K_0^{\mathrm{alg}}(\mathbb C)=\mathbb Z\bigr).}
\]

On a scalar idempotent the last map is its rank. Since \(\epsilon_B\phi^+=\epsilon_A\), the extension induces \(\phi_*:K_0(A)\to K_0(B)\). Identity and composition follow entrywise from their unital versions. Homotopies also extend, so the same argument proves homotopy invariance. In a C*-algebra we may use projections throughout, by the [projection–idempotent correspondence (Lesson 1, Theorems 4.1–4.2)](KT-OPK-01.md#4-replacing-idempotents-by-projections).

**Theorem 1.1 (normal form).** Every \(x\in K_0(A)\) has the form

\[
x=[e]-[P],\qquad e\in M_l(A^+),\qquad
P=\operatorname{diag}(1_n,0_{l-n}),\qquad \epsilon_A(e)=P.
\]

Here \(0\leq n\leq l\); in the C*-case \(e\) can be a projection. Thus \(e-P\in M_l(A)\). More generally, differences of idempotents with equal scalar matrices represent elements of \(K_0(A)\).

*Proof.* The [identity-denominator theorem (Lesson 3, Theorem 3.2)](KT-OPK-03.md#3-differences-complements-and-equality) writes \(x=[g]-[1_n]\) in the unital algebra \(A^+\), after allowing zero padding. Augmentation zero says that \(\epsilon_A(g)\) has rank \(n\). A scalar change of basis carries this idempotent to \(P\). Conjugate \(g\) by that same constant invertible matrix. This leaves its class unchanged and gives the required equality of scalar matrices. In the C*-case start with projections and use a scalar unitary change of basis. Conversely, equal scalar matrices have equal ranks and hence their difference is in the kernel. \(\square\)

In particular, subtraction of \([P]\) is part of the definition even when \(P\) does not belong to \(M_l(A)\). If \(e\in M_l(A)\), its scalar matrix is zero and its class already belongs to the kernel.

## 2. Unital consistency and finite direct sums

**Theorem 2.1.** For unital \(A\), the inclusion \(A\hookrightarrow A^+\) induces an isomorphism from the preceding lesson's \(K_0^{\mathrm{alg}}(A)\) to the kernel defining \(K_0(A)\).

*Proof.* The algebra isomorphism

\[
A^+\longrightarrow A\oplus\mathbb C,\qquad
a+\lambda1\longmapsto(a+\lambda1_A,\lambda)
\]

has inverse \((b,\lambda)\mapsto(b-\lambda1_A)+\lambda1\). Matrix idempotents over a direct sum are pairs of matrix idempotents. Rectangular equivalence witnesses are pairs as well; zero padding puts two given representatives in a common size. Consequently

\[
V_{\mathrm{id}}(A\oplus\mathbb C)=V_{\mathrm{id}}(A)\oplus
V_{\mathrm{id}}(\mathbb C).
\]

Group completion of this finite product is the product of the group completions: take differences componentwise, and use a pair of stabilization witnesses for equality. Augmentation is projection onto the second factor \(\mathbb Z\). The inclusion \(a\mapsto a+0\) corresponds to \(a\mapsto(a,0)\), so its image is exactly the kernel and it is injective. \(\square\)

We can henceforth write \(K_0(A)\) without ambiguity for a unital algebra. Notice that the isomorphism uses \(A^+\cong A\oplus\mathbb C\), not an identification of \(A^+\) with \(A\).

For a possibly nonunital \(A\), let \(V(A)\) mean stable algebraic idempotent classes, or equivalently stable Murray–von Neumann projection classes in the C*-case. Entrywise inclusion into \(A^+\) defines a homomorphism

\[
\omega_A:G(V(A))\longrightarrow K_0(A),\qquad
[p]-[q]\longmapsto[p]-[q].
\]

The formula is meaningful because both scalar parts vanish. Section 5 will prove when this map is an isomorphism and exhibit an important failure of surjectivity.

## 3. Lifting a stabilized invertible and proving half-exactness

For \(z\in GL_r(D)\), an elementary block factorization is

\[
\begin{pmatrix}z&0\\0&z^{-1}\end{pmatrix}
=\begin{pmatrix}1&z\\0&1\end{pmatrix}
\begin{pmatrix}1&0\\-z^{-1}&1\end{pmatrix}
\begin{pmatrix}1&z\\0&1\end{pmatrix}
\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\tag{3.1}
\]

Multiplying the first three factors gives \(\begin{psmallmatrix}0&z\\-z^{-1}&0\end{psmallmatrix}\), which proves the identity. If \(D=C/I\) for a unital Banach algebra \(C\), choose arbitrary matrix lifts \(Z,W\) of \(z,z^{-1}\). Substitution into the right side of (3.1) gives an invertible matrix over \(C\): each triangular factor is invertible with the opposite off-diagonal entry. Its image is \(\operatorname{diag}(z,z^{-1})\). The individual lift \(Z\) need not be invertible.

**Theorem 3.1 (half-exactness).** For every closed ideal \(J\subset A\),

\[
K_0(J)\xrightarrow{\iota_*}K_0(A)\xrightarrow{\pi_*}K_0(A/J)
\]

is exact at \(K_0(A)\).

*Proof.* Identify \(J^+\) with \(J+\mathbb C1\subset A^+\). Under \(\pi^+:A^+\to(A/J)^+\), a normal-form representative \(e\in M_l(J^+)\) goes to its scalar matrix \(P\). Therefore \(\pi_*\iota_*([e]-[P])=0\).

Conversely let \(x=[e]-[P]\in K_0(A)\) map to zero. In the unital group of \((A/J)^+\), the two classes \([\pi^+(e)]\) and \([P]\) agree. The [identity-stabilization criterion (Lesson 3, Theorem 3.2)](KT-OPK-03.md#3-differences-complements-and-equality) gives equivalence after adding the same identity block. The [stabilized-similarity theorem (Lesson 1, Theorem 3.1)](KT-OPK-01.md#3-why-an-extra-block-removes-the-difference) then supplies an invertible \(z\) over \((A/J)^+\) and matrices

\[
E=\operatorname{diag}(e,1_k,0),\qquad
F=\operatorname{diag}(P,1_k,0),\qquad
z\pi^+(E)z^{-1}=F.
\]

The zero blocks may be enlarged to obtain one common size \(r\). The matrix \(F\) is scalar. By (3.1), \(\operatorname{diag}(z,z^{-1})\) lifts to \(w\in GL_{2r}(A^+)\). Put

\[
f=w\operatorname{diag}(E,0_r)w^{-1}.
\]

Then \(\pi^+(f)=\operatorname{diag}(F,0_r)\), so \(f-\operatorname{diag}(F,0_r)\) has entries in \(J\). In particular \(f\in M_{2r}(J^+)\). Its relative class maps to

\[
[f]-[\operatorname{diag}(F,0_r)]
=[E]-[F]=[e]-[P]=x
\]

in \(K_0(A)\). Conjugation and zero padding preserve classes, while the common \(1_k\) cancels only in the group. This proves the reverse inclusion. The proof works for Banach algebras; for C*-algebras the isomorphism with projection K-theory gives the same result. \(\square\)

This is exactness in the middle. No lifting assertion for all quotient idempotents, and no injectivity assertion for \(\iota_*\), has been proved or assumed.

## 4. A splitting makes the entire short sequence exact

**Theorem 4.1 (split exactness).** Suppose

\[
0\longrightarrow J\xrightarrow{\iota} A\xrightarrow{\pi}B
\longrightarrow0
\]

has a bounded algebra-homomorphism section \(s:B\to A\), so \(\pi s=1_B\). Then

\[
0\longrightarrow K_0(J)\xrightarrow{\iota_*}K_0(A)
\xrightarrow{\pi_*}K_0(B)\longrightarrow0
\]

is split exact, with section \(s_*\).

*Proof.* Functoriality gives \(\pi_*s_*=1\), hence surjectivity and a section. Half-exactness gives the middle equality. It remains to prove injectivity, which is not a consequence of half-exactness alone.

Take \(x=[e]-[P]\in K_0(J)\) whose image in \(K_0(A)\) vanishes. [Identity stabilization (Lesson 3, Theorem 3.2)](KT-OPK-03.md#3-differences-complements-and-equality) and [stabilized similarity (Lesson 1, Theorem 3.1)](KT-OPK-01.md#3-why-an-extra-block-removes-the-difference) in \(A^+\) give

\[
UEU^{-1}=F,
\qquad E=\operatorname{diag}(e,1_k,0),\quad
F=\operatorname{diag}(P,1_k,0),
\]

with \(U\) invertible and \(F\) scalar. Now \(\pi^+(E)=F\), so \(v=\pi^+(U)\) commutes with \(F\). The unital extension \(s^+\) carries \(v\) to an invertible \(S=s^+(v)\). Since it fixes every scalar entry, \(SF=FS\). Thus

\[
W=S^{-1}U,\qquad \pi^+(W)=1,\qquad WEW^{-1}=F.
\]

Both \(W\) and \(W^{-1}\) are the identity plus a matrix over \(J\), so they are invertibles over \(J^+\). Hence \([E]=[F]\) already in its unital group, giving \(x=0\) in \(K_0(J)\). \(\square\)

Every \(x\in K_0(A)\) now has a unique decomposition

\[
x=\iota_*y+s_*z,\qquad z=\pi_*x.
\]

Existence follows because \(x-s_*\pi_*x\) is in the kernel; uniqueness follows from applying \(\pi_*\) and then injectivity of \(\iota_*\). This is a group decomposition. An algebra splitting need not make \(A\) an algebra direct sum because the two factors can multiply nontrivially.

**Corollary 4.2.** For arbitrary Banach algebras \(A,B\), the two inclusions induce

\[
K_0(A)\oplus K_0(B)\ \cong\ K_0(A\oplus B).
\]

*Proof.* Apply Theorem 4.1 to the ideal \(A\oplus0\) and the quotient onto \(B\), with section \(b\mapsto(0,b)\). The decomposition has exactly the indicated two inclusions. Induction gives finite direct sums. \(\square\)

## 5. When projections inside the algebra suffice

We give the projection approximate-unit statement for arbitrary C*-algebras, without separability or a sequential approximate-unit assumption. Equip \(M_\infty(A)=\bigcup_N M_N(A)\) with its norm in \(A\otimes\mathcal K\), using upper-left zero corner inclusions. Here \(\mathcal K=\mathcal K(\ell^2(\mathbb N))\) only specifies the stabilization norm.

The hypothesis is: for every finite subset \(T\subset M_\infty(A)\) and \(\delta>0\), some projection \(r\in M_\infty(A)\) satisfies

\[
\|ra-a\|<\delta,\qquad \|ar-a\|<\delta\quad(a\in T).
\tag{5.1}
\]

This is the approximate-unit-of-projections condition, with a net allowed. It is equivalent to saying \(A\otimes\mathcal K\) has an approximate unit of projections. Indeed, (5.1) extends from finite matrices to its completion by density and \(\|r\|\leq1\). Conversely a projection in that completion can be approximated by a finite self-adjoint matrix and corrected by the spectral cutoff near 0 and 1; the correction is a finite-matrix projection and is arbitrarily close. Applying this to a projection that already approximates the given finite set yields (5.1). The correction has value zero at 0 and so lies in the finite nonunital matrix algebra. This uses the [spectral correction (Lesson 1, Theorem 6.1)](KT-OPK-01.md#6-repairing-an-approximate-idempotent), not K-theory continuity.

**Theorem 5.1.** Under (5.1), \(\omega_A:G(V(A))\to K_0(A)\) is an isomorphism.

We first describe the compression used for both directions. Let \(h(t)\in M_m(A^+)\) be a continuous path of projections, with constant scalar part

\[
P=\operatorname{diag}(1_n,0),\qquad h(t)=P+X(t).
\]

A single projection is the same construction with no parameter. Regard every entry of \(X(t)\) as an element of the first corner of \(M_\infty(A)\). Its image as \(t\) varies is a compact norm set. Finite nets in these finitely many compact sets, together with (5.1) and the bound \(\|r\|\leq1\), give a common \(r\in M_N(A)\) approximating them on both sides uniformly to any specified tolerance. Enlarge its finite support if necessary. Set

\[
\widetilde P=P\otimes1_N,\quad
\widetilde X(t)=X(t)\otimes e_{11},\quad
\widetilde h(t)=\widetilde P+\widetilde X(t),\quad
R=1_m\otimes r.
\]

The tilde notation uses scalar matrix tensor products; it is a finite matrix construction. A coordinate permutation identifies \(\widetilde h(t)\) with \(h(t)\oplus P^{\oplus(N-1)}\). Thus it is a projection, and

\[
[\widetilde h(t)]-[\widetilde P]=[h(t)]-[P].
\tag{5.2}
\]

The projection \(R\) commutes with \(\widetilde P\). The self-adjoint compression

\[
a(t)=\widetilde P+R\widetilde X(t)R
=R\widetilde h(t)R+(1-R)\widetilde P
\]

is uniformly as close as desired to \(\widetilde h(t)\). For example, the norm of a matrix of \(m^2\) blocks is at most \(m\) times the maximum block norm, and each compressed block differs by at most the sum of its two approximation errors. This bound is independent of \(N\).

Choose the error small enough, say less than \(1/4\). The spectra of \(a(t)\), and of the line segments from \(\widetilde h(t)\) to \(a(t)\), lie in disjoint neighborhoods of 0 and 1. The cutoff \(\chi\), zero on the first neighborhood and one on the second, gives a continuous projection path from \(\widetilde h(t)\) to \(c(t)=\chi(a(t))\). Functional calculus commutes with augmentation, so this path retains scalar part \(\widetilde P\). Since \(a(t)\) commutes with \(R\),

\[
c(t)=d(t)+(1-R)\widetilde P,\qquad
d(t)=\chi\bigl(R\widetilde h(t)R\bigr)
\in R M_{mN}(A)R.
\tag{5.3}
\]

The cutoff defining \(d(t)\) is taken in the unital corner with identity \(R\); the zero corner is harmless. In particular \(d(t)\) is a projection in a finite matrix algebra over \(A\). Both \(R\widetilde P\) and \((1-R)\widetilde P\) are projections, and their sum is \(\widetilde P\). Equation (5.3) therefore gives

\[
[h(t)]-[P]=[d(t)]-[R\widetilde P].
\tag{5.4}
\]

*Surjectivity.* Apply this construction to the projection normal form of Theorem 1.1. Both projections on the right of (5.4) belong to \(M_\infty(A)\), so the class is in the image of \(\omega_A\).

*Injectivity.* Suppose \([p]-[q]\in G(V(A))\) maps to zero. In the unital group of \(A^+\), identity stabilization gives equivalence between \(p\oplus1_k\) and \(q\oplus1_k\). After zero padding, projection equivalence gives a continuous projection path \(h(t)\) between them. Write both endpoints as \(P+p'\) and \(P+q'\), with \(P\) scalar and \(p',q'\in M_m(A)\) orthogonal to \(P\). Their scalar images agree, but the scalar path need not be constant.

The [close-projection transport (Lesson 2, proof of Theorem 4.2)](KT-OPK-02.md#4-transport-along-a-cylinder), applied to the finite-dimensional scalar path, gives a continuous scalar unitary \(u(t)\), with \(u(0)=1\), such that

\[
\epsilon_A(h(t))=u(t)Pu(t)^*.
\]

Replace \(h(t)\) by \(u(t)^*h(t)u(t)\). Its scalar part is now constantly \(P\); its endpoints are \(P+p'\) and \(P+q''\). Here \(u(1)\) commutes with \(P\), and \(q''=u(1)^*q'u(1)\) is equivalent to \(q'\) in \(V(A)\), since the partial isometry \(u(1)^*q'\) has entries in \(A\).

Apply the common compression to this path. At its initial endpoint the projection \(d(0)\) of (5.3) is

\[
d(0)=p_R+R\widetilde P,
\]

where \(p_R=\chi(R(p'\otimes e_{11})R)\) is orthogonal to \(\widetilde P\) and is as close as desired to \(p'\otimes e_{11}\). Continuity of the cutoff at a projection justifies the last assertion as the compression error tends to zero. Choose the tolerance so this distance is less than one. The close-projection equivalence then gives \([p_R]=[p]\) in \(V(A)\). Although its implementing unitary is in the unitization, its partial isometry is the unitary times a projection in \(A\), and thus has entries in \(A\). At the final endpoint the same argument gives

\[
d(1)=q_R+R\widetilde P,\qquad [q_R]=[q].
\]

The path \(d(t)\) consists entirely of projections over \(A\). Its endpoints have the same class in \(V(A)\): subdivide into close pairs, using the same partial-isometry observation. Orthogonal sums agree with block sums. Consequently

\[
[p]+[R\widetilde P]=[q]+[R\widetilde P]
\quad\hbox{in }V(A).
\]

This is exactly a group-completion witness for \([p]-[q]=0\). It proves injectivity without assuming cancellation of \(V(A)\). \(\square\)

This proof explains why the projection approximate unit matters: it moves the nonscalar part into a genuinely unital finite corner and leaves an unchanged scalar projection outside that corner. The theorem includes every unital C*-algebra and every C*-algebra with a projection approximate unit, as well as the more general stably unital case. The corresponding nonunital AF-algebra agreement was already established in [AF-algebras, Proposition 7.7](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/af-algebras.html#OA-FND-AF-06).

**Example 5.2 (compact operators).** Let \(H\) be any nonzero Hilbert space. The net of orthogonal projections onto finite-dimensional subspaces is an approximate unit for \(\mathcal K(H)\). To see norm approximation, cover the compact image of the unit ball under a compact operator by finitely many small balls and include their centers in the subspace. This makes \(\|(1-r)T\|\) small; apply the same argument to \(T^*\) for \(\|T(1-r)\|\). Larger subspaces retain both estimates.

A compact projection has finite-dimensional range: otherwise an orthonormal sequence in its range contradicts compactness. Projections in matrices over \(\mathcal K(H)\) are thus finite-rank projections on finite sums of \(H\). They are equivalent exactly when their ranks agree. An isometry between finite-dimensional ranges extends by zero to a finite-rank partial isometry, which proves the sufficient direction; a partial isometry proves necessity. All nonnegative ranks occur after finite matrix amplification, including when \(H\) is finite-dimensional. Therefore

\[
V(\mathcal K(H))\cong\mathbb N_0,\qquad
K_0(\mathcal K(H))\cong\mathbb Z,
\]

with a rank-one projection as positive generator. No separability of \(H\) is required. For \(H=0\), both algebra and group are zero.

## 6. Compact supports and the determinant at the equator

Let \(X\) be locally compact Hausdorff and let \(X^+=X\cup\{\infty\}\) be its one-point compactification. If \(X\) is already compact, add an isolated point. Extension by the limiting scalar identifies

\[
C_0(X)^+\cong C(X^+),\qquad
\epsilon(f)=f(\infty).
\]

Hence the definition of compactly supported K-theory is

\[
K_c^0(X):=K_0(C_0(X))
=\ker\bigl(K_0(C(X^+))\xrightarrow{\mathrm{ev}_\infty}\mathbb Z\bigr).
\tag{6.1}
\]

No countability assumption on \(X\) is involved.

**Proposition 6.1.** \(K_0(C_0(\mathbb R))=0\).

*Proof.* The one-point compactification is a circle. Every complex vector bundle on the circle is trivial, by the [endpoint-gluing proof (Lesson 2, Proposition 5.1)](KT-OPK-02.md#5-gluing-around-a-circle-and-across-a-sphere). Its bundle monoid is \(\mathbb N_0\), and the third lesson identifies its group completion with \(K_0(C(S^1))=\mathbb Z\). Evaluation at any point is the rank isomorphism. Its kernel is zero. \(\square\)

For the sphere use the second lesson's coordinates: a finite point \(z\) represents \([1:z]\in\mathbb{CP}^1\), the coordinate at infinity is \(w=1/z\), and the equator is parametrized counterclockwise by \(z=e^{i\theta}\). A clutching matrix \(g:S^1\to GL_r(\mathbb C)\) transfers coefficients from the finite disc to the infinity disc:

\[
a_\infty=g(z)a_0.
\]

For a bundle \(E\), trivialize it on both discs and define

\[
d(E)=\operatorname{wind}(\det g).
\]

The zero bundle has \(d=0\).

**Theorem 6.2.** This gives a well-defined homomorphism

\[
d:K_0(C(S^2))\longrightarrow\mathbb Z
\]

which vanishes on the class of every trivial bundle. The Bott relative class specified below has value \(+1\).

*Proof.* The two disc trivializations exist by the [triviality theorem for contractible compact spaces (Lesson 2, Corollary 4.3)](KT-OPK-02.md#4-transport-along-a-cylinder). A change of trivialization replaces \(g\) by \(a_\infty g a_0^{-1}\), where \(a_0,a_\infty\) extend invertibly across their respective discs. The winding of each determinant is zero: its boundary loop extends to a disc, whose radial contraction supplies a null-homotopy. Both conclusions hold with the chosen equator parametrization. Product winding is additive and inversion changes the sign, so \(d(E)\) is independent of the trivializations. A bundle isomorphism has the same frame-change equation, proving invariance under isomorphism.

For a direct sum the transition is block diagonal and its determinant is the product of the two determinants. Thus \(d\) is additive on the bundle monoid. The [Serre–Swan and projection correspondence (Lesson 2, Theorems 3.1–3.2)](KT-OPK-02.md#3-recovering-bundles-and-all-their-maps), followed by the [universal property of group completion (Lesson 3, Theorem 1.1)](KT-OPK-03.md#1-additive-measurements-and-formal-subtraction), gives the asserted homomorphism on \(K_0(C(S^2))\). A trivial bundle admits identical global frames on both discs and has transition 1, so its degree is zero.

The rank-one projection

\[
q(z)=\frac{1}{1+|z|^2}
\begin{pmatrix}1&\overline z\\z&|z|^2\end{pmatrix},
\qquad
q(\infty)=\begin{pmatrix}0&0\\0&1\end{pmatrix}=P
\tag{6.2}
\]

is the range projection onto the line spanned by \((1,z)^T\). Near infinity that line is spanned by \((w,1)^T\), and on the equator

\[
(1,z)^T=z(1/z,1)^T.
\]

Thus its finite-to-infinity coefficient transfer is \(g(z)=z\), of winding \(+1\). Since \(q-P\) vanishes at infinity,

\[
\beta=[q]-[P]\in K_0(C_0(\mathbb R^2)),\qquad d(\beta)=1.
\]

Here \(d\) on the relative group means its restriction to the subgroup (6.1). The constant projection \(P\) represents the trivial line and is equivalent to \(\operatorname{diag}(1,0)\). Thus one may also write \([q]-[1]\) as a difference of rank-one classes. The sign is determined by the stated transfer convention; no identification with a separately signed Chern-number convention is being made. \(\square\)

If \(k\beta=0\), applying \(d\) gives \(k=0\). Therefore \(\beta\) is nonzero and has infinite order. We have proved this without computing the entire sphere K-group or using Bott periodicity.

**Proposition 6.3.** If \(X\) is connected, noncompact and locally compact Hausdorff, then \(V(C_0(X))=0\).

*Proof.* A projection \(p\in M_n(C_0(X))\) has continuous, integer-valued rank \(\operatorname{Tr}(p(x))\), hence constant rank. Since \(p\) vanishes at infinity, \(\|p(x)\|<1\) off a compact set. There is a point outside that set because \(X\) is noncompact. A projection of norm less than one is zero, so the constant rank is zero everywhere. Thus \(p=0\). Idempotent classes have the same conclusion by the range-projection correspondence; alternatively an idempotent's rank is its trace and a nonzero idempotent has norm at least one. \(\square\)

For \(X=\mathbb R^2\), this gives \(G(V(C_0(\mathbb R^2)))=0\), whereas \(K_0(C_0(\mathbb R^2))\) contains \(\beta\). The zero map from the first group cannot be surjective. In particular \(C_0(\mathbb R^2)\) fails condition (5.1).

## 7. Relative terminology and two failures of short exactness

The equal-scalar differences of Theorem 1.1 are relative classes: they compare two finite projective objects whose scalar fibers agree. In relative algebra K-theory this special group is denoted \(K_0(A^+,A)\). For this pair the comparison is exactly the augmentation kernel, as verified in [Blackadar 1998, Proposition 5.4.1]. Our definition and normal-form proof already supply this kernel picture.

For a unital complex Banach algebra \(D\) and a closed two-sided ideal \(J\), the relative group \(K_0(D,J)\) also records a chosen isomorphism between the two objects over \(D/J\). A kernel alone can lose this comparison information. The strong excision statement is

\[
K_0(J^+,J)\ \cong\ K_0(D,J)
\]

under the map induced by \(J^+\to D\). Blackadar [1998, Theorem 5.4.2] states this theorem. The complete relative comparison construction, explicit inverse and all choice and relation checks are [The six-term sequence, §§5–6, Theorem 6.1 and Corollary 6.2](KT-OPK-11.md#6-strong-excision-including-injectivity). The corollary supplies the general complex Banach-algebra case; the theorem supplies the C*-algebra case, including nonunital ambient algebras through external unitization. Here the relative group means that comparison-triple group. The preceding half-exactness and split-exactness proofs use their explicit scalar normal forms.

**Example 7.1 (failure of injectivity).** For infinite-dimensional \(H\),

\[
0\to\mathcal K(H)\to B(H)\to Q(H)\to0
\]

is the compact-operator extension. Section 5 gives \(K_0(\mathcal K(H))=\mathbb Z\), while [Lesson 3, Theorem 5.3, proves](KT-OPK-03.md#5-calculations-dimensions-absorption-and-bundles) \(K_0(B(H))=0\) for every infinite-dimensional Hilbert space. The inclusion therefore sends a rank-one generator to zero and is not injective. This is compatible with exactness at the zero middle group. It also shows this extension admits no bounded algebra-homomorphism section: Theorem 4.1 would force injectivity.

**Example 7.2 (failure of surjectivity).** Endpoint evaluation gives

\[
0\to C_0((0,1))\to C([0,1])
\xrightarrow{f\mapsto(f(0),f(1))}\mathbb C\oplus\mathbb C\to0.
\]

The map is onto, since \((a,b)\) is the endpoint pair of \((1-t)a+tb\). Its kernel consists precisely of the functions vanishing at both endpoints and identifies with \(C_0((0,1))\). Every bundle on the interval is trivial, so \(K_0(C([0,1]))=\mathbb Z\). Corollary 4.2 gives \(K_0(\mathbb C\oplus\mathbb C)=\mathbb Z^2\). Endpoint evaluation on a trivial rank-\(n\) bundle is \((n,n)\), and therefore the induced homomorphism is

\[
\mathbb Z\longrightarrow\mathbb Z^2,\qquad k\longmapsto(k,k).
\]

Its image omits \((1,0)\). A continuous matrix projection on the interval cannot have different endpoint ranks, which also explains the obstruction to lifting this quotient projection. The linear interpolation used to prove surjectivity of the algebra map is not a multiplicative section.

## 8. Exercises with solutions

**Exercise 8.1 (basic).** Identify the external unitization of \(C_0((0,1))\) and compute its \(K_0\).

*Solution.* Identify the two endpoints of \([0,1]\). The quotient is a circle. A function on this quotient is a continuous function on the interval with equal endpoint values. Subtracting that common value leaves a function vanishing at both endpoints. Thus

\[
C_0((0,1))^+\cong C(S^1),
\]

and augmentation is evaluation at the identified point. The circle bundle calculation gives \(K_0(C(S^1))=\mathbb Z\), and evaluation is rank, an isomorphism. Its kernel, \(K_0(C_0((0,1)))\), is zero. A homeomorphism \((0,1)\cong\mathbb R\) gives the same result as Proposition 6.1.

**Exercise 8.2 (basic).** Give the canonical maps implementing finite direct-sum compatibility of \(K_0\).

*Solution.* For \(A=A_1\oplus\cdots\oplus A_r\), let \(i_j\) and \(p_j\) be coordinate inclusion and projection. The maps are

\[
(x_1,\ldots,x_r)\longmapsto\sum_j(i_j)_*x_j,
\qquad x\longmapsto\bigl((p_1)_*x,\ldots,(p_r)_*x\bigr).
\]

Corollary 4.2 and induction prove the first map is an isomorphism. Since \(p_ji_k\) is identity for \(j=k\) and the zero homomorphism otherwise, functoriality proves the displayed second map is its inverse. The zero homomorphism induces zero because a relative normal form maps to \([P]-[P]\). This includes zero algebras and does not require identities in the summands.

**Exercise 8.3 (intermediate).** Verify the two failure examples, including exactness in the middle, and determine whether either extension can have a homomorphic section.

*Solution.* In Example 7.1 the compact-operator ideal is closed and the Calkin algebra is its Banach quotient. The computed first group is \(\mathbb Z\) and the middle group is zero, so the first map is zero and its kernel is all of \(\mathbb Z\). Both the kernel of the next map and the image of the first map are the zero subgroup of \(K_0(B(H))\); middle exactness holds. Injectivity would follow from a section, so no such section exists.

In Example 7.2 the preceding endpoint-interpolation and kernel checks prove exactness at the algebra level. Exercise 8.1 gives zero for the ideal K-group, while the next map \(k\mapsto(k,k)\) has zero kernel. Its image is the diagonal subgroup, with cokernel \(\mathbb Z\) detected by \((a,b)\mapsto a-b\). It is not onto, so a homomorphic section would contradict Theorem 4.1. Both examples satisfy half-exactness and fail one of the additional assertions needed for a short exact K-group sequence.

**Exercise 8.4 (intermediate).** For compact Hausdorff \(X\), a point \(x_0\in X\), and any Banach algebra \(A\), prove

\[
K_0(C(X,A))\cong K_0(A)\oplus
K_0(C_0(X\setminus\{x_0\},A)).
\]

*Solution.* Evaluation \(\mathrm{ev}_{x_0}:C(X,A)\to A\) has the bounded multiplicative section \(a\mapsto(x\mapsto a)\). Its kernel consists of functions vanishing at \(x_0\). Restriction identifies this kernel with \(C_0(X\setminus\{x_0\},A)\). To verify vanishing at infinity, for \(\varepsilon>0\) the set \(\{x\mid\|f(x)\|\geq\varepsilon\}\) is closed in compact \(X\) and misses a neighborhood of \(x_0\), hence is compact in the complement. Conversely a continuous function vanishing at infinity on the complement extends continuously by zero at \(x_0\): each such compact superlevel set is closed in \(X\) and misses \(x_0\), so its complement is a neighborhood on which the extended function is smaller than \(\varepsilon\). The identification respects multiplication and the supremum norm.

Apply Theorem 4.1. Explicitly the isomorphism sends \((z,y)\) to the constant-section image of \(z\) plus the ideal-inclusion image of \(y\). Evaluation recovers \(z\), and injectivity of the ideal map gives uniqueness of \(y\). The argument permits nonunital \(A\), arbitrary compact Hausdorff \(X\), and the case \(X=\{x_0\}\), when the ideal is zero.

**Exercise 8.5 (advanced).** Explain why projections over \(C_0(\mathbb R^2)\) miss a nonzero class. Locate the unitization step, and show that replacing \(K_0\) everywhere by \(G(V(\cdot))\) would destroy half-exactness.

*Solution.* Proposition 6.3 makes every finite matrix projection over \(C_0(\mathbb R^2)\) zero, so its projection monoid and group completion are zero. The matrix \(q\) of (6.2) does not vanish at infinity and is not a projection over this algebra. It lies over its unitization \(C(S^2)\). Subtracting its scalar projection \(P=q(\infty)\) creates the legitimate relative class \(\beta\), even though neither \(q\) nor \(P\) lies in \(M_2(C_0(\mathbb R^2))\). The determinant homomorphism gives \(d(\beta)=1\), hence it is nonzero and of infinite order. The subtraction in the unitized group is exactly the step unavailable to \(G(V(C_0(\mathbb R^2)))\).

In the extension

\[
0\to C_0(\mathbb R^2)\to C(S^2)\xrightarrow{\mathrm{ev}_\infty}
\mathbb C\to0,
\]

the alternative ideal group would be zero. The alternative groups for the two unital algebras are their ordinary \(K_0\)-groups, and the kernel of evaluation contains \(\beta\). Thus the alternative sequence would have zero image but nonzero kernel at the middle. By contrast our relative definition and Theorem 3.1 give exactness. The algebra extension even splits by constants, so Theorem 4.1 identifies its true ideal group with the whole evaluation kernel.

## Prerequisite and later results

We used the first lesson's stabilized equivalence, range projection, close-projection equivalence and spectral correction; the second lesson's bundle–projection correspondence, cylinder transport, winding lemma and triviality over contractible spaces and the circle; and the third lesson's group completion, identity stabilization, functoriality and \(K_0(B(H))=0\). Continuous functional calculus and its continuity are the verified results of *C*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients*, Theorems 5.1 and 6.1. The exact proofs are [Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-07) and [Theorem 6.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-11); they supply the cutoff continuity in Section 5.

The complete general relative comparison and strong excision proofs are the exact owned results in Lesson 11, §§5–6, with the Banach version in Corollary 6.2. Bott periodicity will eventually compute \(K_0(C_0(\mathbb R^2))\); the present determinant argument establishes only the explicitly proved infinite-order class.

## References

- Bruce Blackadar, *K-Theory for Operator Algebras*, second edition, Cambridge University Press, 1998, §§5.4–5.6, especially Propositions 5.4.1 and 5.5.5 and Theorem 5.6.1; Proposition 8.3.6 for split exactness. Strong excision is Theorem 5.4.2. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- Bruce Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Springer, 2006; author's revised 2017 text, V.1.1.15–V.1.1.21, especially V.1.1.17–V.1.1.19 for unitization and stable unitality.
- Heath Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser, 2024, §8.1.
- [AF-algebras, Proposition 7.7](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/af-algebras.html#OA-FND-AF-06), in *Foundations of von Neumann algebras*, for the nonunital AF case.
- *Cyclic forms that survive norm completion*, in *Cyclic cohomology, connections and transverse geometry*, for the same scalar-relative convention.
