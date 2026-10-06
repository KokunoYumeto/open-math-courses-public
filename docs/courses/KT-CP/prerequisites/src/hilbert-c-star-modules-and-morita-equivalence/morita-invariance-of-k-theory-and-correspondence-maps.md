# Morita invariance of K-theory and maps induced by correspondences

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An imprimitivity bimodule carries K-theory classes between equivalent algebras. A correspondence with compact left action does something more general: it carries classes forward even when the module is not full and the resulting map is not invertible. Stabilization turns that correspondence into an actual homomorphism of algebras. We will prove that its induced map depends on the correspondence, composes under tensor products and respects extension boundaries.

The Morita-invariance and full-corner theorems hold for arbitrary C*-algebras. We first prove the σ-unital case by stabilization, then remove countability by a local construction that retains fullness. The compact-correspondence construction allows arbitrary coefficient algebras, provided the right module is countably generated. We allow degenerate left actions, as in *Tensor products and C*-correspondences*, Definition 1.1.

## 1. Relative classes and canonical stability

Write \(D^\dagger\) for the forced unitization, with augmentation \(\varepsilon:D^\dagger\to\mathbb C\). This convention applies even to a unital \(D\), when \(D^\dagger\cong D\oplus\mathbb C\). Let \(\varepsilon_*:K_0(D^\dagger)\to K_0(\mathbb C)\) be the augmentation map. The definitions are
\[
\begin{gathered}
K_0(D)=\ker\varepsilon_*,\\
K_1(D)=\pi_0 U_\infty(D),\\
\begin{aligned}
U_n(D)&=\{u\in U(M_n(D^\dagger)):\\
&\hspace{2em}\varepsilon(u)=1_n\}.
\end{aligned}
\end{gathered}
\tag{1.1}
\]
After stabilization, a \(K_0\)-class can be written \([p]-[P]\), where \(P\) is a scalar projection and \(\varepsilon(p)=P\). These pictures and their agreement with stable projection classes are proved in [Nonunital algebras: unitization, relative classes and half-exactness](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/nonunital-algebras-unitization-relative-classes-and-half-exactness.html), Theorems 1.1–2.1, and [Invertibles, unitaries and K₁](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/invertibles-unitaries-and-k1.html), Section 1. Blackadar, V.1.1.17 and V.1.2.1–2, gives the classical conventions. For unital algebras, they agree with the projection and finitely generated projective-module picture proved in *Finite projective modules, frames and K₀*.

Actual projections in a nonunital \(D\) need not generate \(K_0(D)\). For instance \(C_0(\mathbb R^2)\) has no nonzero matrix projections: their ranks are locally constant, hence constant on the connected plane, and vanishing at infinity forces rank zero. Its nonzero Bott class is represented by a projection in the unitization minus its scalar projection. The Bott computation is proved in [Bott periodicity](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/bott-periodicity.html), Theorem 4.1 and Corollary 6.1. Blackadar, V.1.2.20–21, is the classical reference. Thus a formula involving only projective modules over \(D\) cannot define every nonunital class.

Let
\[
\begin{gathered}
s_D:D\longrightarrow D\otimes\mathcal K,\\
s_D(d)=d\otimes e_{11}.
\end{gathered}
\tag{1.2}
\]
We use its canonical K-theory isomorphism \(s_{D*}\). In degree zero this is [Matrix stability, stability and continuity of K₀](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/matrix-stability-stability-and-continuity-of-k0.html), Theorem 4.1. In degree one it follows from [Invertibles, unitaries and K₁](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/invertibles-unitaries-and-k1.html), Corollary 4.2, or from the natural identification \(K_1(D)=K_0(SD)\), proved in [Suspension, higher K-groups and the long exact sequence](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/suspension-higher-k-groups-and-the-long-exact-sequence.html), Theorem 2.1, and degree-zero stability, since \(S(D\otimes\mathcal K)=SD\otimes\mathcal K\). The same argument supplies matrix stability in both degrees. Homotopic homomorphisms give homotopic image projections and unitaries, hence identical K-maps; for degree zero use [Idempotents, projections and their equivalences](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/idempotents-projections-and-their-equivalences.html), Theorems 4.2–4.3, and [The Grothendieck group and K₀ of a unital algebra](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/the-grothendieck-group-and-k0-of-a-unital-algebra.html), Theorem 4.2. The stability maps are natural because the corner homomorphisms commute with every homomorphism of coefficient algebras.

## 2. Full multiplier corners

**Theorem 2.1.** If \(C\) is σ-unital and \(p\in M(C)\) is a full projection, then the inclusion
\[
i:pCp\longrightarrow C
\tag{2.1}
\]
induces isomorphisms on \(K_0\) and \(K_1\).

*Proof.* Put \(B=pCp\). The full-corner module \(pC\) is a \(B\)–\(C\) imprimitivity bimodule. If \((e_n)\) is a countable approximate identity of \(C\), then \((pe_n)\) generates \(pC\): \(pe_nc\to pc\). Since \(\mathcal K(pC)=B\), the countable-generation criterion makes \(B\) σ-unital too.

The two-absorption lemma from *Stable isomorphism and the Brown–Green–Rieffel theorem*, Lemma 1.2, identifies \((pC)^\infty\) with \(H_C\). Refine that unitary by keeping its first copy of \(pC\). The source tail is another \((pC)^\infty\), hence isomorphic to the standard tail. The target decomposes as
\[
\begin{aligned}
H_C&=pC\oplus G,\\
G&=(1-p)C\oplus H_{C,\mathrm{tail}}.
\end{aligned}
\tag{2.2}
\]
The complement \((1-p)C\) is countably generated by \((1-p)e_n\). Kasparov stabilization absorbs it into the standard tail. As in the preceding lesson’s Theorem 3.1, choose a unitary \(W:(pC)^\infty\to H_C\) equal to identity on the first \(pC\). Compact conjugation gives
\[
\begin{gathered}
\Phi:B\otimes\mathcal K\longrightarrow C\otimes\mathcal K,\\
\Phi(b\otimes e_{11})=b\otimes e_{11}.
\end{gathered}
\tag{2.3}
\]
Left multiplication by \(b\) kills \((1-p)C\), so the second equality holds even though \(p\) need not belong to \(C\). Hence \(\Phi s_B=s_C i\). On K-theory,
\[
i_*=(s_{C*})^{-1}\Phi_*s_{B*},
\tag{2.4}
\]
a composition of three isomorphisms. ∎

This proof constructs the map needed for the corner inclusion. An abstract stable isomorphism alone would not establish (2.4) for that particular inclusion.

**Lemma 2.2 (Full separable subalgebras).** Let \(p\in M(C)\) be a full projection. Every countable subset of \(C\) is contained in a separable C*-subalgebra \(D\subset C\) such that \(pD,Dp\subset D\) and \(\overline{DpD}=D\). These subalgebras form a directed family with union \(C\).

*Proof.* Start with the algebra generated by the given set, and repeatedly adjoin \(px,xp\) for a countable dense set of its elements. Continuity makes the resulting separable algebra invariant under both operations. Suppose such an algebra \(D_n\) has been chosen. For each element of a countable dense subset of \(D_n\), and each positive integer \(m\), fullness in \(C\) supplies a finite sum \(\sum_j a_jpb_j\), with \(a_j,b_j\in C\), within \(1/m\) of that element. Adjoin all these factors and again close under multiplication by \(p\), obtaining \(D_{n+1}\). Put \(D=\overline{\bigcup_nD_n}\). Every element of every \(D_n\) is in \(\overline{DpD}\), so this ideal is all of \(D\). The restricted left and right multiplication maps define a multiplier projection of \(D\).

Every element of \(C\) lies in one such algebra by starting with its singleton. To dominate two such algebras, start with the union of their countable dense subsets. The construction contains both. This proves directedness and the union assertion. ∎

**Lemma 2.3 (Continuity for directed inclusions).** If \(C\) is the closure of a directed union of C*-subalgebras \(D_\lambda\), then
\[
\begin{gathered}
\varinjlim_\lambda K_i(D_\lambda)\cong K_i(C),\\
i=0,1.
\end{gathered}
\tag{2.5a}
\]
No countability of the directed set is required.

*Proof.* Use forced unitizations with their common scalar coordinate. Approximate a matrix projection over \(C^\dagger\) by a self-adjoint matrix over one \(D_\lambda^\dagger\), keeping its scalar part unchanged. Within distance less than \(1/4\) of the projection, its spectrum avoids \(1/2\). The spectral cut \(\chi_{(1/2,\infty)}\), continuous on this spectrum, gives a projection in the same matrix algebra with the same scalar part, as close to the original projection as desired. Nearby projections are homotopic by cutting their straight-line interpolation. Thus every relative K₀-class comes from a stage.

A relation between two classes is witnessed, after adding a common auxiliary projection and stabilizing, by a projection homotopy. Approximate that auxiliary projection and a finite mesh of the homotopy in a common stage. Keep their scalar matrices exact. Linear interpolation followed by the spectral cut produces a projection path in that stage: uniform closeness to the original path keeps the spectrum away from \(1/2\). Endpoints already in the stage are kept exact, and nearby auxiliary projections give the same class. This supplies the equality witness at a later stage. The finite stabilized projection-homotopy description of K₀ is the equivalence developed in *Idempotents, projections and their equivalences* and *The Grothendieck group and K₀ of a unital algebra*; unitization gives its relative version.

For K₁ approximate a normalized unitary \(u=1+x\) by \(v=1+y\) in a stage within distance less than one. It is invertible, and \(v(v^*v)^{-1/2}\) is a normalized unitary approaching \(u\). Polar parts of the short straight-line interpolation connect the nearby unitaries. A stabilized unitary homotopy is approximated using a finite mesh in a common stage. Polygonal interpolation remains invertible by uniform closeness to the unitary path; its polar parts give a normalized unitary path with exact endpoints. Thus representatives and equality witnesses occur at stages, proving surjectivity and injectivity in both degrees. ∎

**Theorem 2.4 (Arbitrary full multiplier corners).** For every C*-algebra \(C\) and full projection \(p\in M(C)\), the inclusion \(pCp\to C\) induces isomorphisms on both K-groups.

*Proof.* Use the directed family from Lemma 2.2. Every \(D\) is separable, hence σ-unital. Explicitly, rescale a dense sequence \((d_n)\) to make \(h=\sum_n2^{-n}(d_n^*d_n+d_nd_n^*)\) norm convergent. The inequalities \(d_n^*d_n,d_nd_n^*\leq c_n h\) show that \(e_m=h(h+1/m)^{-1}\) satisfies \(e_md_n,d_ne_m\to d_n\): sandwich those inequalities by \(1-e_m\) and use \(\|(1-e_m)h(1-e_m)\|\to0\). Density makes \((e_m)\) an approximate identity. Theorem 2.1 therefore applies to \(pDp\to D\).

These corner maps commute with inclusions. Also \(\bigcup_DpDp=pCp\), since a \(D\) containing a given corner element contains it in \(pDp\). Apply Lemma 2.3 to both unions. The directed limit of the corner isomorphisms is exactly the K-map of \(pCp\to C\), so it is an isomorphism. The extra factors in Lemma 2.2 are essential: an arbitrary separable subalgebra need not retain fullness. ∎

**Corollary 2.5 (Linking-algebra invariance).** Let \(X\) be an \(A\)–\(B\) imprimitivity bimodule, without countability assumptions. Let \(L=\mathcal K(X\oplus B)\), and let \(i_A,i_B\) be its two diagonal corner inclusions. Then
\[
\begin{gathered}
\mu_X:K_*(A)\longrightarrow K_*(B),\\
\mu_X=(i_{B*})^{-1}i_{A*}.
\end{gathered}
\tag{2.5}
\]
is an isomorphism.

*Proof.* Both diagonal multiplier projections are full by the linking theorem in *Imprimitivity bimodules and Morita equivalence*, Theorem 5.1. Apply Theorem 2.4 to both corners. ∎

## 3. Compact transport through an embedding

The next lemma allows embeddings which are not adjointable. This matters when a left action is degenerate or when a module is restricted to an ideal.

**Lemma 3.1.** An inner-product-preserving right-module isometry \(j:E\to F\) induces an isometric homomorphism
\[
\begin{gathered}
j_{\mathcal K}:\mathcal K(E)\longrightarrow\mathcal K(F),\\
j_{\mathcal K}(\theta_{x,y})=\theta_{jx,jy}.
\end{gathered}
\tag{3.1}
\]

*Proof.* The rank-one product and adjoint identities are preserved. To check norm and well-definedness, write a finite-rank operator as \(XY^*\), with columns \(X,Y:D^n\to E\). Its norm satisfies
\[
\begin{aligned}
\|XY^*\|^2&=\|Y(X^*X)Y^*\|\\
&=\|(X^*X)^{1/2}(Y^*Y)\,\\
&\hspace{2em}(X^*X)^{1/2}\|.
\end{aligned}
\tag{3.2}
\]
Indeed \(\|XY^*\|^2=\|Y(X^*X)Y^*\|\), and apply \(\|ZZ^*\|=\|Z^*Z\|\) to \(Z=Y(X^*X)^{1/2}\). The coefficient Gram matrices \(X^*X,Y^*Y\) do not change when the column vectors are embedded by \(j\). Thus every finite-rank operator has the same norm after transport; a zero expression stays zero. Completion proves the claim. The identical argument transports compact operators between two embedded modules. ∎

**Lemma 3.2 (Embedding independence).** If \(j,k:E\to H_B\) are such isometries, then \(j_{\mathcal K*}=k_{\mathcal K*}\) after the canonical stable identifications.

*Proof.* For \(0\leq t\leq\pi/2\), put
\[
\begin{gathered}
r_t x\in H_B\oplus H_B,\\
r_t x=(\cos t\,jx,\sin t\,kx).
\end{gathered}
\tag{3.3}
\]
Each \(r_t\) preserves inner products. Transport a rank-one operator by Lemma 3.1; its four blocks are norm-continuous in \(t\). Approximation by finite rank, with the common isometry bound, proves pointwise norm continuity on all compacts. These homomorphisms form a homotopy from \(j_{\mathcal K}\) in the first corner to \(k_{\mathcal K}\) in the second. Scalar two-by-two rotation connects the two corner placements on K-theory. Homotopy invariance and stability identify the endpoint maps. ∎

Now let \(E_B\) be countably generated and let
\[
\varphi:A\longrightarrow\mathcal K(E)
\tag{3.4}
\]
be a homomorphism. Stabilization gives an adjointable isometric embedding \(j:E\to H_B\), obtained by restricting a unitary \(E\oplus H_B\to H_B\). With \(\mathcal K(H_B)=B\otimes\mathcal K\), define
\[
\begin{gathered}
h_E=j_{\mathcal K}\varphi:A\to B\otimes\mathcal K,\\
T_E:K_*(A)\to K_*(B),\\
T_E=(s_{B*})^{-1}(h_E)_*.
\end{gathered}
\tag{3.5}
\]

**Theorem 3.3.** Formula (3.5) is well defined, independent of stabilization and invariant under unitary equivalence of correspondences. Direct sums induce sums of maps. Neither fullness nor nondegeneracy of \(\varphi\) is required.

*Proof.* Lemma 3.1 makes \(h_E\) an actual homomorphism. Lemma 3.2 makes its K-map independent of the chosen embedding. A module unitary intertwining the left actions just changes that embedding by composition, so gives the same map. For a direct sum, put the two embeddings in orthogonal standard summands. The transported left action is the block sum of the two homomorphisms, whose K-map is their sum. ∎

For clarity, its relative-class formulas are
\[
\begin{aligned}
h_E^\dagger(p)&=P\otimes1+(h_E)_n(p-P),\\
h_E^\dagger(u)&=1+(h_E)_n(u-1).
\end{aligned}
\tag{3.6}
\]
The first line has scalar projection \(P\); the second has scalar identity. The symbol \(1\) denotes the identity of the target unitization. Apply the stable inverse to \([h_E^\dagger(p)]-[P]\) or \([h_E^\dagger(u)]\). This is the explicit map on arbitrary nonunital classes. It does not assume that \(p\) lies over \(A\) itself or that \(E\) has a compact identity.

The construction only needs an isometric embedding into \(H_B\); countable generation guarantees one. In particular, the first-coordinate embedding of \(B_B\) defines the identity map even when that module is not countably generated. For a homomorphism \(f:A\to B\), that embedding with left action \(f\) recovers exactly \(f_*\).

## 4. Tensor composition

Let \((E,\varphi)\) be an \(A\)–\(B\) compact correspondence and \((F,\psi)\) a \(B\)–\(C\) compact correspondence, with both right modules countably generated. The tensor module is countably generated: if \((x_n)\) generates \(E\) and \((y_m)\) generates \(F\), tensors \(x_n\otimes y_m\) generate it. To see density, approximate the first factor by sums \(x_nb\), move \(b\) to the second factor, then approximate that factor by sums \(y_mc\). Its left action is compact by *Tensor products and C*-correspondences*, Theorem 2.4.

**Theorem 4.1.** With that left action,
\[
T_{E\otimes_B F}=T_F T_E.
\tag{4.1}
\]

*Proof.* Choose adjointable stabilization embeddings \(v:E\to H_B\) and \(w:F\to H_C\). If \(v(x)=(b_j)\), define
\[
J(x\otimes y)=(w\psi(b_j)y)_j\in H_C^\infty.
\tag{4.2}
\]
Balancing is respected. The sum of inner products is
\[
\begin{aligned}
&\langle y,\psi(\sum_j b_j^*c_j)z\rangle_C\\
&\quad=\langle y,\psi(\langle x,x'\rangle_B)z\rangle_C,
\end{aligned}
\tag{4.3}
\]
where \(v(x')=(c_j)\). Thus \(J\) extends isometrically to the completed tensor product. Reindex the two countable coordinates to identify \(H_C^\infty\) with \(H_C\). Lemma 3.2 lets us compute the tensor map with this embedding, whether or not \(J\) is adjointable.

For \(x\in E\), the creation operator \(C_x:F\to E\otimes_B F\), \(y\mapsto x\otimes y\), is compact. In fact the factorization \(E\cdot B=E\), proved in the first module lesson, Theorem 5.3, writes \(x=x'b\); then
\[
C_x=C_{x'}\psi(b).
\tag{4.4}
\]
Creation is adjointable, with \(C_x^*(x'\otimes y)=\psi(\langle x,x'\rangle)y\); composing it with the compact \(\psi(b)\) proves the claim. Transporting compact maps through the embeddings gives a compact operator \(S_x:F\to H_C^\infty\), whose coordinates are \(w\psi(b_j)\). Its tail norms tend to zero by \(\|\psi(\sum_{j>N}b_j^*b_j)\|\to0\).

The operator \(\theta_{x,x'}\otimes1\) equals \(C_xC_{x'}^*\). Its transported compact image is therefore \(S_xS_{x'}^*\). On the other hand, the matrix of \(v_{\mathcal K}(\theta_{x,x'})\) has entries \(b_i c_j^*\). Applying \(h_F=w_{\mathcal K}\psi\) entrywise gives
\[
\big(w\psi(b_i c_j^*)w^*\big)_{i,j}
=S_xS_{x'}^*.
\tag{4.5}
\]
The equality follows from \(w^*w=1_F\). Density extends it to every compact operator on \(E\), and hence to every \(\varphi(a)\). Thus the tensor homomorphism, up to the countable reindexing, is
\[
(h_F\otimes1_{\mathcal K})h_E.
\tag{4.6}
\]
The canonical stability maps commute with homomorphisms. Applying that naturality twice to (4.6) proves (4.1). Reindexing the two compact matrix coordinates is compatible with these maps: on any finite corner it is a finite change of matrix placement, implemented by a scalar unitary and a rotation homotopy after enlargement. Every K-class and every relation reaches a finite corner by stability. ∎

In particular, the proof never replaces \(H_B\otimes_B F\) by \(F^\infty\) for a degenerate \(\psi\). Formula (4.2) directly embeds the part detected by the tensor product.

## 5. The Morita map and projective modules

**Theorem 5.1.** For any \(A\)–\(B\) imprimitivity module \(X\), formula (2.5) defines its Morita isomorphism, with inverse \(\mu_{X^*}\). If \(X_B\) is countably generated, \(T_X=\mu_X\). Whenever \(X^*\) also admits a standard-module embedding, its map \(T_{X^*}\) is the inverse; this holds in particular for σ-unital algebras. If both algebras are unital, then
\[
\begin{aligned}
&T_X([P]-[Q])\\
&\quad=[P\otimes_A X]-[Q\otimes_A X]
\end{aligned}
\tag{5.1}
\]
for finitely generated projective right modules \(P,Q\).

*Proof.* Corollary 2.5 makes (2.5) an isomorphism. The linking algebra for the conjugate module is the same linking algebra with corners exchanged, by the conjugation and rank-one identifications of the imprimitivity lesson. Its formula is consequently the inverse.

When \(X_B\) is countably generated, embed \(X\) adjointably in the tail of \(H_B\), and place \(B_B\) in the first coordinate. This embeds \(M=X\oplus B\) isometrically even if \(B_B\) is not countably generated. Lemma 3.1 transports \(L=\mathcal K(M)\) into \(\mathcal K(H_B)\), so (3.5) defines \(T_M\) using this supplied embedding. On the \(B\)-corner its homomorphism is exactly \(s_B\), hence \(T_M i_{B*}=1\). Since \(i_{B*}\) is an isomorphism, \(T_M=(i_{B*})^{-1}\). Restriction to the \(A\)-corner gives compact transport for \(X\), and Lemma 3.2 identifies it with \(T_X\). Thus \(T_X=T_M i_{A*}=\mu_X\). The same argument applies to any supplied embedding of \(X^*\). For σ-unital algebras both modules are countably generated, and the inverse evaluations together with Theorem 4.1 also give the inverse identities.

When \(A,B\) are unital, \(1_X\) is compact because it is the image of \(1_A\). The compact-identity criterion in the finite-projective lesson makes \(X_B\) finitely generated projective. Write \(P=pA^n\). Tensor balancing identifies
\[
P\otimes_A X\cong\varphi_n(p)X^n.
\tag{5.2}
\]
The map sends \((a_i)\otimes x\) to \((a_ix)_i\); its inner-product computation is the tensor formula, and nondegeneracy gives onto the projected range. This range is a finitely generated projective summand of \(X^n\). Compact transport and stability identify the class of \(\varphi_n(p)\) with the class of that range, by the projection-module theorem. Additivity gives (5.1). ∎

More generally, for a compact correspondence between unital algebras the image of \([1_A]\) is \([\varphi(1_A)E]\). The range of a compact projection is finitely generated projective, by the same criterion. This class need not be \([1_B]\). Formula (3.6), rather than (5.1) alone, remains the definition for general nonunital algebras.

## 6. Ideals, quotients and boundary maps

For a closed ideal \(J\subset B\), put \(E_J=\overline{EJ}\) and \(\bar E=E/E_J\), a Hilbert \(B/J\)-module. The coefficient-quotient construction and its norm are those of the preceding Rieffel lesson, Lemma 1.1 and Proposition 2.2; their right-module proofs do not require a left inner product.

**Lemma 6.1.** Quotienting vectors induces the exact sequence
\[
\begin{aligned}
0\to\mathcal K(E_J)&\to\mathcal K(E)\\
&\to\mathcal K(\bar E)\to0.
\end{aligned}
\tag{6.1}
\]

*Proof.* Transport compacts from the closed submodule by Lemma 3.1. They form an ideal: for example \(\theta_{x,y}\theta_{za,wb}\) has both vectors in \(E_J\) when \(a,b\in J\), since \(J\) is two-sided; taking adjoints and approximating proves the assertion. Every adjointable operator and its adjoint preserve \(E_J\). Its induced operator on the Banach quotient has norm at most its original norm and retains the adjoint identity. This defines the compact quotient homomorphism. Rank-one quotient operators lift, so its range contains the dense finite ranks; the closed-range property of C*-homomorphisms makes it onto.

If a compact \(T\) induces zero on \(\bar E\), its range lies in \(E_J\). Approximate \(T\) by \(T f_\lambda\), with \(f_\lambda\) an approximate identity of \(\mathcal K(E)\), and then by finite sums \(\theta_{Tx_i,y_i}\). An approximate identity \(u_\alpha\) of \(\mathcal K(E_J)\) converges on the finitely many vectors \(Tx_i\in E_J\). Consequently \(u_\alpha T\to T\) in norm, first for these sums and then for \(T\). Since \(u_\alpha T\) belongs to that ideal, \(T\in\mathcal K(E_J)\). The reverse kernel inclusion is immediate. ∎

Suppose \(I\subset A\) is an ideal with \(\varphi(I)\subset\mathcal K(E_J)\). Restrict the action to \(E_J\) and descend it to \(\bar E\). A stabilization unitary \(E\oplus H_B\to H_B\) respects multiplication by \(J\). It restricts and descends to unitaries
\[
\begin{gathered}
E_J\oplus H_J\cong H_J,\\
\bar E\oplus H_{B/J}\cong H_{B/J}.
\end{gathered}
\tag{6.2}
\]
The quotient statement follows from the coefficient quotient on each coordinate. Thus \(h_E\) maps the extension \(0\to I\to A\to A/I\to0\) into the stabilized extension of \(B\) by \(J\). Write \(i,k\) for the two ideal inclusions and \(\pi,q\) for the quotient maps. The three vertical maps and commuting squares are
\[
\begin{gathered}
h_I:I\to J\otimes\mathcal K,\\
h_E:A\to B\otimes\mathcal K,\\
h_Q:A/I\to(B/J)\otimes\mathcal K,\\
k h_I=h_E i,\qquad q h_E=h_Q\pi.
\end{gathered}
\tag{6.3}
\]
The target extension is exact: compact matrix corners show that the kernel of \(q\) consists precisely of \(J\otimes\mathcal K\). Rank-one matrix coefficients lift, so the image is dense; its C*-homomorphism range is closed, hence onto. Independence follows from the embedding-rotation argument restricted and quotiented in the same way.

If \(J\) is σ-unital, \(E_J\) is countably generated over \(J\): generators are \(x_n e_m\), for generators \(x_n\) of \(E\) and an approximate identity \((e_m)\) of \(J\). The restricted map is then precisely Theorem 3.3’s correspondence map. For arbitrary \(J\), (6.2) still supplies the embedding needed to define the restricted map. This avoids claiming that ideals of σ-unital algebras must themselves be σ-unital.

**Theorem 6.2.** The three maps obtained from (6.3), after canonical stability, commute with both boundary maps and therefore with the six-term K-theory sequence.

*Proof.* The six-term theorem is [The six-term exact sequence and the exponential map](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/six-term-exact-sequence-and-exponential-map.html), Theorem 2.1, proved for arbitrary C*-algebra extensions. Its boundary formulas make the relevant naturality explicit. For the index map, take a normalized unitary \(u\) in a matrix quotient, lift \(\operatorname{diag}(u,u^*)\) to a unitary \(W\) over the forced unitization, and write
\[
\partial_1[u]=[WPW^*]-[P].
\tag{6.4}
\]
The scalar part of \(W\) is chosen identity and \(P\) is the standard first-block projection. Such a lift exists: the elementary-matrix lift in *Fredholm operators and the K₀ index*, Section 2, equation (2.3), is normalized and invertible; taking its unitary polar part retains its unitary quotient and scalar identity. The positive polar interpolation gives the same relative K-class. Apply the unitized homomorphism \(h_E^\dagger\) to \(W\). It is a normalized lift of the corresponding quotient unitary; it preserves \(P\), products and adjoints. Formula (6.4) therefore gives the commuting index square.

For the exponential boundary, let \(p\) be a quotient projection with scalar part \(P\), and choose a self-adjoint lift \(a\) with that scalar part. [The six-term exact sequence and the exponential map](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/six-term-exact-sequence-and-exponential-map.html), Theorem 1.1, proves
\[
\partial_0([p]-[P])=[\exp(2\pi i a)].
\tag{6.5}
\]
The exponential has scalar part identity. A homomorphism commutes with continuous functional calculus, so applying \(h_E^\dagger\) gives exactly the exponential for the image lift. This proves the second boundary square. The algebra maps in (6.3) commute by construction; their other K-squares commute by functoriality. The canonical stability homomorphisms also form a diagram of extensions, so the same argument allows their inverse K-isomorphisms in every square. ∎

For an arbitrary imprimitivity module, the Rieffel correspondence pairs ideals \(I,J\). The submodule \(X_J\) and quotient \(X/X_J\) give their equivalences without countability assumptions. There is an exact linking-algebra extension
\[
\begin{gathered}
0\longrightarrow L(X_J)\longrightarrow L(X)\\
\longrightarrow L(X/X_J)\longrightarrow0.
\end{gathered}
\tag{6.6}
\]
Its corner maps are the coefficient and vector quotient maps. Lemma 6.1 proves exactness by applying its rank-one argument to the direct-sum linking module. The diagonal corners are respectively \(I,J\), then \(A,B\), then \(A/I,B/J\). Thus both coefficient extensions map into this linking extension by diagonal inclusions. Theorem 2.4 makes all six inclusion maps K-isomorphisms. Naturality of the index and exponential formulas, proved above for diagrams of algebra extensions, identifies the two six-term sequences through \(\mu_{X_J},\mu_X,\mu_{X/X_J}\). This proves Morita naturality of both boundaries for arbitrary algebras and corresponding ideals, without a countable standard-module embedding.

## 7. Examples: units, bundles and traces

**Example 7.1 (Stability and matrix corners).** The standard module \(H_A\), with compact left algebra \(A\otimes\mathcal K\), implements the canonical inverse to \(s_{A*}\). Indeed use its identity embedding in itself in (3.5). The module \(e_{11}M_n(A)\), from \(A\) to \(M_n(A)\), gives the corner homomorphism on K-theory: embed this row module in the first copy of \(M_n(A)\) inside its standard module. Left multiplication by \(a\) is exactly multiplication by \(aE_{11}\). Composition with the corner of the standard module yields the stabilized algebra map, hence the usual matrix-corner map, including its relative formulas.

**Example 7.2 (A bundle correspondence).** For a finite-rank Hermitian vector bundle \(V\) over compact Hausdorff \(X\), take \(E=\Gamma(V)\) with scalar left action from \(\mathbb C\). Its identity is compact by a finite Parseval frame. Then
\[
\begin{gathered}
T_E:\mathbb Z\to K_0(C(X)),\\
T_E(m)=m[V].
\end{gathered}
\tag{7.1}
\]
This follows from the compact projection for \(E\), and additivity. It sends the scalar unit to the bundle class, not necessarily the trivial line class. The degree-one map has zero domain, since finite complex unitary matrices are path connected, giving \(K_1(\mathbb C)=0\).

**Example 7.3 (Free proper actions).** Let a locally compact Hausdorff group \(G\) act continuously, freely and properly on a locally compact Hausdorff space \(X\). Then the free proper-action imprimitivity module gives
\[
\begin{aligned}
&K_i(C_0(X)\rtimes G)\\
&\quad\cong K_i(C_0(G\backslash X)).
\end{aligned}
\tag{7.2}
\]
The crossed product is full. The right side is the topological K-theory with compact supports of the orbit space, with degree convention \(K_i(C_0(Y))=K^{-i}(Y)\). The analytic imprimitivity theorem is [Proper actions, free actions and the orbit space](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/KT-CP-09.html), Proposition 9.2 and Theorem 9.5; the K-isomorphism is Corollary 2.5 here and itself requires no σ-unitality.

For a finite free action on compact \(X\), its equivalence module is \(C(X)\) over \(C(G\backslash X)\), with coefficient inner product given by summing over an orbit. Combining its map with the inclusion of \(C(X)\) defines a transfer. If \(\pi:X\to Y=G\backslash X\), the transfer of \(\pi^*V\) is
\[
[V]\,[\pi_*\mathbf1],
\tag{7.3}
\]
where \(\pi_*\mathbf1\) has fibre \(\bigoplus_{x\in\pi^{-1}(y)}\mathbb C\). Indeed the tensor module has fibre \(\bigoplus_{x\in\pi^{-1}(y)}V_y\), canonically \(V_y\otimes(\pi_*\mathbf1)_y\); this respects local covering trivializations. Finite freeness gives those trivializations by choosing a neighborhood disjoint from its nontrivial translates. The coefficient module is the section module of this direct-image bundle. Its rank is \(|G|\), but its K-class need not be \(|G|[\mathbf1]\).

For the antipodal cover \(S^2\to\mathbb RP^2\), the bundle \(\pi_*\mathbf1\) splits as \(\mathbf1\oplus L\), where \(L\) is the complex sign line. The line is nontrivial. Otherwise there is an odd nowhere-zero complex function on \(S^2\). Normalize it to a map to the circle and lift its phase to a real function \(f\), using simple connectivity of the sphere. Oddness makes \(f(-x)-f(x)\) a constant odd multiple of \(\pi\). Applying the antipode twice negates that same constant, a contradiction. Also \([\mathbf1\oplus L]\ne2[\mathbf1]\) in K-theory: equality would give a stable bundle isomorphism after adding a common bundle, and taking determinants and canceling its determinant would trivialize \(L\). Thus (7.3) is the appropriate transfer formula even in a two-sheeted example.

**Example 7.4 (The equivariant bundle map \(T_H\)).** In *A fundamental class for an action on a manifold*, §8, Lemma 8.3 constructs the countably generated module \(\mathcal E_H\), its compact left action \(\lambda_H\), and a frame embedding \(J\) into the standard module of the reduced crossed product \(A\). Its homomorphism is \(\rho_H=J\lambda_H(\cdot)J^*\). Thus its \(T_H\) is precisely (3.5). The frame construction and compactness there are prerequisites; the independence and tensor-composition mechanism are Theorems 3.3 and 4.1 here. The explicit coefficient identification of bundle tensor products in that lesson’s Proposition 8.4 gives
\[
\begin{gathered}
T_{H\oplus L}=T_H+T_L,\\
T_L T_H=T_{H\otimes L}.
\end{gathered}
\tag{7.4}
\]
That construction uses a countable spatial frame and allows an arbitrary discrete acting group; no countability of the group is added here.

**Proposition 7.5 (Trace normalization).** Let \(A,B\) be unital and \(X\) an imprimitivity module. Let \(\tau_B\) be a tracial state. For a finite Parseval frame \((\eta_j)\) of \(X_B\), define
\[
\tau_X(a)=\sum_j\tau_B(\langle\eta_j,a\eta_j\rangle_B).
\tag{7.5}
\]
This trace is independent of the frame. If \(\tau_X=c\tau_A\), then
\[
\begin{gathered}
\tau_{B*}(T_X z)=c\tau_{A*}(z),\\
z\in K_0(A).
\end{gathered}
\tag{7.6}
\]

*Proof.* For a rank-one operator, the frame identity and the tracial property give
\[
\begin{aligned}
&\sum_j\tau_B(\langle\eta_j,x\rangle\langle y,\eta_j\rangle)\\
&\quad=\tau_B(\langle y,x\rangle).
\end{aligned}
\tag{7.7}
\]
Thus (7.5) on compact operators is frame independent. The rank-one product identity and cyclicity of \(\tau_B\) show \(\tau_X(kl)=\tau_X(lk)\) for finite ranks; continuity extends this to compacts. It is positive by (7.5). The left algebra is that compact algebra, so this is a trace on \(A\). For a projection \(p\in M_n(A)\), the trace dimension of \(pX^n\) is the matrix trace of \(\tau_X\) on \(p\), by using the frame in each coordinate and projecting it. If \(\tau_X=c\tau_A\), this is \(c\tau_A^{(n)}(p)\). Apply Theorem 5.1 and take differences to prove (7.6). ∎

The factor depends on the chosen direction: \(c=\tau_X(1_A)\) is the right \(B\)-trace dimension of \(X\). For a torus equivalence whose right trace dimension is \(\theta>0\), with the induced trace equal to \(\theta\) times the normalized left trace, (7.6) gives multiplication by \(\theta\); the inverse map scales by \(\theta^{-1}\). The noncommutative-torus lesson fixes the module, direction and generator convention. No sign-independent or direction-independent trace factor is implicit in (7.6).

## 8. Exercises with complete solutions

**Exercise 14.1.** Show that the corner inclusion \(A\to M_n(A)\) and its Morita map agree.

*Solution.* Put \(D=M_n(A)\) and \(E=e_{11}D\). The right inner product is \(x^*y\), and the left compact algebra is \(e_{11}De_{11}=A\). The inclusion \(j:E\to D\to H_D\) preserves inner products. Its compact transport sends left multiplication by \(a\) to first-standard-coordinate multiplication by \(aE_{11}\). Hence \(h_E=s_D i\), where \(i(a)=aE_{11}\). Formula (3.5) gives \(T_E=i_*\). For arbitrary \(A\), Theorem 5.1 identifies this supplied-embedding map with the Morita isomorphism. On a nonunital relative class \([p]-[P]\), the image projection in \(M_m(D^\dagger)\) is \(P\otimes1_{D^\dagger}+i_m(p-P)\), with scalar part \(P\). Under the canonical embedding \(D^\dagger\to M_n(A^\dagger)\), this becomes \(P\otimes1_n+i_m(p-P)\); the subtracted scalar projection becomes \(P\otimes1_n\). The full scalar identity in these formulas is essential.

**Exercise 14.2.** Prove independence from the stabilization isomorphism.

*Solution.* Restrict two stabilization unitaries to isometries \(j,k:E\to H_B\). The isometries \(r_t\) of (3.3) preserve the coefficient inner product because \(\cos^2t+\sin^2t=1\). Lemma 3.1 transports \(\varphi(a)\) to compacts. For a finite sum of rank ones its four blocks are polynomial expressions in \(\sin t,\cos t\), hence norm continuous; uniform contractivity and compact approximation extend this to every \(\varphi(a)\). This is a homotopy of algebra homomorphisms. Their forced-unitization maps have the same scalar part, so the homotopy applies to both relative projections and normalized unitaries. Its endpoints are the two maps in opposite matrix corners; scalar rotation identifies these corners on K-theory. Applying the same canonical stable inverse gives equal maps. No path connecting the original stabilization unitaries is required.

**Exercise 14.3.** Compute the map \(K_0(\mathbb C)\to K_0(C(X))\) for \(\Gamma(V)\), where \(X\) is compact and \(V\) is a finite-rank bundle.

*Solution.* Choose a finite Parseval frame and its projection \(p\in M_N(C(X))\), so \(\Gamma(V)=pC(X)^N\). The scalar homomorphism on this module is \(\lambda\mapsto\lambda1_E\). Under its frame embedding the compact identity is \(p\); thus the positive generator of \(K_0(\mathbb C)=\mathbb Z\) maps to \([p]=[V]\). A rank-\(m\) scalar projection maps to the direct sum of \(m\) copies of \(V\). Passing to differences proves \(m\mapsto m[V]\) for every integer. If \(V\) is a nontrivial line, this retains its bundle class rather than replacing it by its fibre rank.

**Exercise 14.4.** Show that correspondence maps commute with the index boundary for an extension of the right algebra and its induced module extension.

*Solution.* Take \(0\to J\to B\to B/J\to0\), and an ideal \(I\subset A\) with \(\varphi(I)\subset\mathcal K(E_J)\). The induced modules are \(E_J\) and \(\bar E\). Restrict and quotient one stabilization unitary as in (6.2); Lemma 6.1 ensures that its compact algebra maps give (6.3). For a normalized unitary \(u\) over \(A/I\), choose a normalized unitary lift \(W\) of \(\operatorname{diag}(u,u^*)\) in the matrix unitization of \(A\). Then \(WPW^*-P\) has entries in \(I\). Applying \(h_E^\dagger\) yields a normalized lift of the image quotient unitary; its projection difference has entries in \(J\otimes\mathcal K\). Consequently
\[
(h_I)_*\partial_1[u]=\partial_1(h_Q)_*[u].
\tag{8.1}
\]
Canonical stability also satisfies this equality because its corner maps form a diagram of extensions. Taking their inverse K-isomorphisms proves \(T_I\partial_1=\partial_1T_Q\). For arbitrary \(J\), the restricted map is defined by the supplied embedding in (6.2); if \(J\) is σ-unital it is a countably generated correspondence map in the original sense. This states exactly the induced-extension hypothesis, rather than assigning a boundary compatibility to unrelated correspondences.

## What this lesson does not prove

We use the written programme proofs [Matrix stability, stability and continuity of K₀](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/matrix-stability-stability-and-continuity-of-k0.html), Theorem 4.1; [Invertibles, unitaries and K₁](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/invertibles-unitaries-and-k1.html), Corollary 4.2; [Idempotents, projections and their equivalences](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/idempotents-projections-and-their-equivalences.html), Theorems 4.2–4.3; [Suspension, higher K-groups and the long exact sequence](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/suspension-higher-k-groups-and-the-long-exact-sequence.html), Theorem 2.1; [Bott periodicity](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/bott-periodicity.html), Theorem 4.1; and [The six-term exact sequence and the exponential map](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/six-term-exact-sequence-and-exponential-map.html), Theorems 1.1–2.1. They supply stability, homotopy, suspension, Bott periodicity and the two boundary formulas, with no countability or unitality restriction on the algebras. Blackadar, V.1, credits the classical results. Module stabilization, compact identities, tensor compactness, inverse evaluations and linking fullness are proved in the earlier Hilbert-module lessons. Arbitrary-algebra Morita invariance and full-corner invariance are proved in Section 2, including the directed-continuity argument that removes σ-unitality. Free proper-action analysis and the equivariant bundle module are the precisely identified prerequisites in Examples 7.3–7.4. General Kasparov products and their technical theorem are not used to prove Theorem 4.1; Rosenberg §1 explains the broader bivariant setting. Torus-module existence and its trace normalization are developed in the next lesson.

## References

- H. Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, §8.2, especially Definition 8.2.1, Theorem 8.2.2 and Corollary 8.2.4.
- B. Blackadar, *Operator Algebras*, II.7.6.9–13 and V.1, with the specific K-theory locators above.
- J. Rosenberg, *Examples and applications of noncommutative geometry and K-theory*, §1.2–1.3, pp.96–99, for compact-action Kasparov bimodules and the larger product theory.
- A. Connes, *Noncommutative Geometry*, Chapter II, Appendix A, Definition 7 and Theorem 8, and its concluding K-theory discussion.
- *Matrix stability, stability and continuity of K₀*, Theorems 1.1, 3.3 and 4.1.
- *A fundamental class for an action on a manifold*, §8, Lemma 8.3 and Proposition 8.4.
