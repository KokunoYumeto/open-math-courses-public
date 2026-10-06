# Fredholm operators and the K₀ index

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

For Hilbert spaces, a Fredholm operator has closed range and finite-dimensional kernel and cokernel. A Hilbert-module Fredholm operator can have nonclosed range. Its index therefore needs a definition that remains meaningful before kernels become finite projective modules. We construct that definition through the quotient by compact operators, compare it with the kernel formula whenever that formula applies, and determine when a compact perturbation can supply closed range.

The prerequisites are Adjointable operators, Compact operators, multipliers and the strict topology, Finite projective modules, frames and K₀, and Kasparov's stabilization theorem. We also use the basic operator K-theory of stable projections and invertibles, its homotopy invariance and matrix stability, and its index boundary map, with the exact locators collected below. Inner products are linear in the second variable. Our sign convention is kernel minus cokernel.

## 1. Fredholmness without closed range

**Definition 1.1.** An adjointable \(T:E\to F\) is Fredholm when an adjointable \(S:F\to E\) satisfies
\[
ST-1_E\in\mathcal K(E),\qquad TS-1_F\in\mathcal K(F).
\tag{1.1}
\]
Such an \(S\) is a parametrix. For \(E=F\), this says precisely that the image of \(T\) in \(\mathcal L(E)/\mathcal K(E)\) is invertible: a lift of the inverse is a parametrix, and (1.1) proves the converse.

Products and adjoints of Fredholm operators are Fredholm. For a product \(T_2T_1\), compose the parametrices in the reverse order and expand the two defects. The rank-one composition formulas make every term compact. Taking adjoints gives a parametrix for \(T^*\). Compact perturbations preserve (1.1), and Fredholm endomorphisms form a norm-open set because invertibility is open in the quotient.

**Proposition 1.2 (Closed-range defects).** If a Fredholm \(T:E\to F\) has closed range, then \(\ker T\) and \(\ker T^*\) have compact identity operators. They admit finite Parseval frames and are finite projective Hilbert modules.

*Proof.* The closed-range theorem gives adjointable orthogonal projections \(P,Q\) onto the two kernels. Since \(TP=0\), compressing (1.1) gives
\[
P(ST-1_E)P=-P.
\]
Thus \(P\in\mathcal K(E)\). Similarly \(QT=0\) gives \(Q(TS-1_F)Q=-Q\), so \(Q\in\mathcal K(F)\). Compression identifies \(P\mathcal K(E)P\) with \(\mathcal K(PE)\), by \(P\theta_{x,y}P=\theta_{Px,Py}\). Its identity is \(P\), hence compact. The finite-frame theorem of the preceding lesson on projective modules applies; the same argument applies to \(QF\). ∎

For nonunital \(A\), these modules are represented by projections with entries in \(A\), and determine classes in the relative group \(K_0(A)\). The assertion does not say that every relative K₀ class has such an individual projection representative.

## 2. The quotient definition of the index

Write
\[
D=\mathcal K(H_A)\cong\mathbb K\otimes_{\min}A,\qquad
M=\mathcal L(H_A)=M(D),\qquad Q_A=M/D.
\tag{2.1}
\]
The case \(A=0\) is trivial; the following constructions concern \(A\ne0\). Let \(\pi:M\to Q_A\) be the quotient map.

For an extension \(0\to J\to B\to B/J\to0\) with \(B\) unital, its index boundary map has the following convention. Given an invertible \(u\in M_n(B/J)\), take an invertible lift \(W\in M_{2n}(B)\) of \(\operatorname{diag}(u,u^{-1})\). With \(e=\operatorname{diag}(1_n,0_n)\), set
\[
\partial[u]=[WeW^{-1}]-[e]\in K_0(J).
\tag{2.2}
\]
The difference of idempotents is relative: \(WeW^{-1}-e\in M_{2n}(J)\). Similarity to projections gives its usual C*-algebra K₀ interpretation. The well-definedness, independence and naturality of this homomorphism are proved in The index map and the exact sequence at K₀, Theorem 2.2; Proposition 5.1 there gives its normalized unitary version. Blackadar, Definition 8.3.1 and Propositions 8.3.3–8.3.4, are the classical references.

The required invertible lift can be built directly. If \(t,s\) lift \(u,u^{-1}\), respectively, the product
\[
W=
\begin{pmatrix}1&t\\0&1\end{pmatrix}
\begin{pmatrix}1&0\\-s&1\end{pmatrix}
\begin{pmatrix}1&t\\0&1\end{pmatrix}
\begin{pmatrix}0&-1\\1&0\end{pmatrix}
\tag{2.3}
\]
is invertible, since every factor is. Multiplication in the quotient gives \(\operatorname{diag}(u,u^{-1})\). No invertible lift of \(u\) alone is assumed.

For a general extension, use the forced unitizations \(B^\dagger=B\oplus\mathbb C\) and \((B/J)^\dagger\), adjoining a new unit even if an algebra already has one. The quotient extends to the unital extension
\[
0\longrightarrow J\longrightarrow B^\dagger
\longrightarrow(B/J)^\dagger\longrightarrow0.
\]
Represent a \(K_1(B/J)\) class by an invertible \(u\) in a matrix algebra over \((B/J)^\dagger\) with scalar part \(1_n\). Take \(t,s\) over \(B^\dagger\) lifting \(u,u^{-1}\); their scalar parts are \(1_n\). Construction (2.3) now takes place over \(B^\dagger\), with its adjoined unit, and the scalar part of \(W\) is \(1_{2n}\). Consequently \(WeW^{-1}-e\) lies in \(M_{2n}(J)\), and (2.2) is a relative class in \(K_0(J)\). This is the unitized convention proved in Nonunital algebras: unitization, relative classes and half-exactness, Theorem 1.1, and The index map and the exact sequence at K₀, Section 2. In our Fredholm application \(B=M(D)\) is already unital, so the first displayed construction applies directly.

**Definition 2.1.** For Fredholm \(T\in M\), define
\[
\operatorname{Ind}_A(T)=\partial[\pi(T)]\in K_0(D)\cong K_0(A).
\tag{2.4}
\]
The last identification is basic matrix stability of K-theory, with the coordinate corner \(a\mapsto e_{11}\otimes a\). This defines an index for every coefficient algebra \(A\), even when \(H_A\) is not countably generated.

Here is a projection formula useful in the nonunital case. Multiply \(T\) on the right by a positive invertible function of \(T^*T\) to obtain a contraction \(t\) whose quotient is the unitary polar part of \(\pi(T)\). Explicitly, choose \(c>0\) smaller than the lower bound of the spectrum of \(\pi(T^*T)\), and put
\[
t=Tg(T^*T),\qquad g(s)=(\max(s,c))^{-1/2}.
\]
Then \(t^*t\leq1\), and \(\pi(t)\) is unitary. The positive invertible interpolation between \(1\) and \(g(T^*T)\) shows \([\pi(t)]=[\pi(T)]\) in \(K_1(Q_A)\).

Set \(d=(1-t^*t)^{1/2}\), \(d'=(1-tt^*)^{1/2}\). Both are compact. The matrix
\[
W_t=\begin{pmatrix}t&-d'\\d&t^*\end{pmatrix}
\]
is unitary: \(td=d't\) follows first for polynomials from \(t(t^*t)=(tt^*)t\), then for the square-root function by uniform approximation. This identity and the two defect identities give \(W_t^*W_t=W_tW_t^*=1\). Its quotient is \(\operatorname{diag}(\pi(t),\pi(t)^*)\). Thus (2.2) gives
\[
\operatorname{Ind}_A(T)=[p_t]-[e],\qquad
p_t=\begin{pmatrix}
tt^*&td\\dt^*&1-t^*t
\end{pmatrix},\quad e=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\tag{2.5}
\]
Here \(p_t-e\in M_2(D)\), so this is an actual relative projection class, rather than a difference of presumed finite kernels.

**Theorem 2.2 (Kernel comparison).** If a Fredholm endomorphism \(T\) of \(H_A\) has closed range, then
\[
\operatorname{Ind}_A(T)=[\ker T]-[\ker T^*].
\tag{2.6}
\]

*Proof.* The closed-range theorem supplies the polar partial isometry \(v\) of \(T\), with \(v^*v=1-P\), \(vv^*=1-Q\), where \(P,Q\) are the kernel projections. Its quotient is the unitary polar part of \(\pi(T)\), so their K₁ classes agree. Proposition 1.2 makes \(P,Q\) compact. Substituting \(v\) for \(t\) in (2.5), \(d=P\) and \(vP=0\), hence \(p_v=\operatorname{diag}(1-Q,P)\). Relative addition gives
\([p_v]-[e]=[P]-[Q]\).
Under the coordinate stability identification, these projection classes are exactly the classes of the two finite-frame modules. ∎

**Theorem 2.3 (Index laws).** The index is unchanged by compact perturbation or a norm-continuous Fredholm path. It vanishes on invertible operators and satisfies
\[
\begin{aligned}
\operatorname{Ind}(T\oplus S)&=\operatorname{Ind}(T)+\operatorname{Ind}(S),\\
\operatorname{Ind}(ST)&=\operatorname{Ind}(S)+\operatorname{Ind}(T),\\
\operatorname{Ind}(T^*)&=-\operatorname{Ind}(T).
\end{aligned}
\tag{2.7}
\]
Finite standard sums are identified with \(H_A\) by coordinate reindexing.

*Proof.* Compact perturbations have identical quotient images. A Fredholm path gives a path of invertibles in the quotient, whose stable K₁ class is constant. For an invertible lift, use \(W=\operatorname{diag}(T,T^{-1})\) in (2.2); it commutes with \(e\), giving zero. Direct sum is addition in both K₁ and K₀, and \(\partial\) is a homomorphism. The basic K₁ identity \([uv]=[u]+[v]\) gives the composition law. The adjoint of an invertible has the K₁ class of its inverse, by polar deformation, giving the last law. These arguments use no closed-range perturbation. ∎

## 3. Stable multipliers have zero K-theory

**Theorem 3.1.** For every C*-algebra \(A\),
\[
K_0(M(\mathbb K\otimes A))=K_1(M(\mathbb K\otimes A))=0.
\tag{3.1}
\]

*Proof.* Choose a bijection \(\mathbb N^2\to\mathbb N\). It identifies the countable orthogonal sum of copies of \(H_A\) with \(H_A\), giving isometries \(v_j\in M\) with orthogonal ranges spanning the module. Define
\[
\alpha(x)=\sum_{j\geq1}v_jxv_j^*.
\tag{3.2}
\]
This is the bounded adjointable diagonal operator consisting of copies of \(x\); its adjoint consists of copies of \(x^*\). Consequently \(\alpha\) is a unital *-homomorphism. The series converges strictly, since its tails tend pointwise to zero on vectors and on adjoints, hence on compact operators by the strict-topology criterion.

Let \(w\) shift the summands: \(wv_j=v_{j+1}\). It is an isometry, and
\[
\alpha(x)=v_1xv_1^*+w\alpha(x)w^*,\qquad
v_1v_1^*+ww^*=1.
\tag{3.3}
\]
An isometric corner \(x\mapsto vxv^*\) induces the identity on both K-groups. For projections this follows from the rectangular partial isometry \(vp\). For a unitary \(u\), its image under the unitized corner map is \(vuv^*+1-vv^*\). The unitary
\[
Z=\begin{pmatrix}v&1-vv^*\\0&v^*\end{pmatrix}
\]
conjugates \(\operatorname{diag}(u,1)\) to
\(\operatorname{diag}(vuv^*+1-vv^*,1)\).
Stable K₁ classes are unchanged by conjugation, so the same conclusion holds. These arguments apply in every matrix algebra.

The two ranges in (3.3) are orthogonal. Their sum therefore induces the sum of their K-theory maps, as is seen on block projections and block unitaries. Hence
\[
\alpha_*=\mathrm{id}_*+\alpha_*.
\]
Cancellation in either abelian K-group gives \(\mathrm{id}_*=0\), proving (3.1). ∎

**Corollary 3.2.** The boundary maps give isomorphisms
\[
K_i(A)\cong K_{1-i}(Q_A),\qquad i=0,1.
\tag{3.4}
\]
Every element of \(K_0(A)\) is the index of a Fredholm operator on \(H_A\).

*Proof.* Apply the six-term exact sequence to \(0\to D\to M\to Q_A\to0\). Both K-groups of \(M\) vanish by Theorem 3.1, so the two boundary maps are injective and surjective. Basic matrix stability identifies \(K_i(D)\) with \(K_i(A)\).

For the final assertion, represent a preimage under \(\partial\) by an invertible matrix \(u\) over \(Q_A\). Lift its entries to a matrix \(T\) over \(M\); its quotient is invertible, so \(T\) is Fredholm on \(H_A^n\). Coordinate reindexing gives a Fredholm on \(H_A\), with the same class under matrix stability and therefore the prescribed index. No unstabilized representability assertion about \(K_1(Q_A)\) is needed. ∎

There is also a complete stable classification. Fredholm operators on finite sums of \(H_A\), modulo norm-continuous Fredholm paths and addition of invertible summands, form \(K_0(A)\) through the index. To verify injectivity, equal indices give equal stable K₁ classes of the quotient invertibles, by Corollary 3.2. After adding identity matrices, there is a quotient path between them. Approximate that path by a sufficiently fine polygonal path with the same endpoints. Its segments remain invertible because the original path and its inverses are uniformly bounded. Choose lifts of its finitely many vertices, fixing the prescribed endpoint lifts, and interpolate linearly. Their images are the invertible polygonal path, so the lifted path is Fredholm. Conversely every permitted equivalence preserves the index by Theorem 2.3. Surjectivity is the last part of Corollary 3.2.

## 4. Closed-range perturbations and their limitation

**Theorem 4.1 (Unital coefficients).** If \(A\) is unital, every Fredholm operator on \(H_A\) has an \(A\)-compact perturbation with closed range.

*Proof.* First normalize \(T\) to the essentially unitary contraction \(t=TD\) used in Section 2, where \(D=g(T^*T)\) is positive invertible. It suffices to perturb \(t\), since multiplication on the right by \(D^{-1}\) preserves closed range and compactness of a perturbation.

Because \(\pi(tt^*)=1\), the positive compact
\[
k=(\tfrac12-tt^*)_+
\]
satisfies \(tt^*+k\geq\tfrac12\,1\). Let \(P_N\) be the first \(N\)-coordinate projection on \(H_A\). It is compact here because \(A\) is unital. Choose \(N\) with
\(\|k-P_NkP_N\|<1/4\), using strict convergence of the coordinate projections on compacts. Since \(P_NkP_N\leq\|k\|P_N\), choose \(c\geq\max(1,\|k\|)\); then
\[
tt^*+cP_N\geq\tfrac14\,1.
\]
For the coordinate inclusion \(J:A^N\to H_A\), form
\[
R=(t,\sqrt c\,J):H_A\oplus A^N\to H_A.
\]
Its \(RR^*=tt^*+cP_N\) is invertible. Thus
\[
V=(RR^*)^{-1/2}R
\]
is a coisometry. The difference \(V-R\) is compact, because \(RR^*-1\) is compact and functional calculus gives \((RR^*)^{-1/2}-1\) compact. In the domain \(H_A\oplus A^N\), \(R^*R-1\) is also compact: its upper-left block is \(t^*t-1\); the other blocks factor through the finite free summand. Therefore
\[
q=1-V^*V
\]
is a compact projection onto \(\ker R\).

We need to move \(q\) into finitely many coordinates. Let \(M_0\) be projection onto the added \(A^N\), and let \(P_L\) be a finite-coordinate projection containing \(M_0\). For sufficiently large \(L\), \(\|(1-P_L)q\|\) is small. The positive operator \(qP_Lq\) is then invertible in the corner with identity \(q\). The partial isometry
\[
b=P_Lq(qP_Lq)^{-1/2}
\]
has \(b^*b=q\) and \(r=bb^*\leq P_L\). As \(\|(1-P_L)q\|\to0\), \(b\to q\) in norm, so \(r\to q\); arrange \(\|r-q\|<1\).

There is a unitary \(u=1+\text{compact}\) with \(uqu^*=r\). To verify this, put
\[
a=rq+(1-r)(1-q).
\]
Then \(aq=ra\), \(a-1\) is compact, and
\(a^*a=1-(r-q)^2\), which is invertible. The same computation for \(aa^*\) makes \(a\) invertible. Its polar unitary \(u=a(a^*a)^{-1/2}\) has the asserted properties.

Set \(W=Vu^*\). It is a coisometry with \(W^*W=1-r\) and differs compactly from \(R\). With \(i:H_A\to H_A\oplus A^N\) the original-summand inclusion, define
\[
t_1=W(1-P_L)i.
\tag{4.1}
\]
The difference \(t_1-t=(W-R)i-WP_Li\) is compact. Since \(r\leq P_L\), \(W\) is isometric on \((1-P_L)(H_A\oplus A^N)\). Thus \(t_1\) has closed range. Its kernel is the finite-coordinate module \((P_L-M_0)(H_A\oplus A^N)\); its cokernel is the finite projective module
\(W(P_L-r)(H_A\oplus A^N)\).
Indeed these two target subspaces are orthogonal and exhaust the target, by \(WW^*=1\). Finally \(t_1D^{-1}\) is the required compact perturbation of \(T\). ∎

The argument retains finitely many coordinates in order to discard all finite-dimensional interactions at once. It does not assume that the sum of two finite projective submodules is closed.

**Example 4.2 (A nonunital obstruction).** Let \(A=C_0(\mathbb C)\), and let
\[
f(z)=\frac{z}{\sqrt{1+|z|^2}},\qquad
T=\operatorname{diag}(f,1,1,\ldots)\in\mathcal L(H_A).
\]
The defect \(1-T^*T=1-TT^*\) is the first-coordinate operator with entry \((1+|z|^2)^{-1}\), hence compact. Thus \(T\) is Fredholm. Its relative index projection (2.5), after removing the unchanged coordinates, is
\[
p(z)=\frac1{1+|z|^2}
\begin{pmatrix}|z|^2&z\\\overline z&1\end{pmatrix},
\qquad
\operatorname{Ind}_A(T)=[p]-[e_{11}].
\tag{4.2}
\]
This class is nonzero. The projection extends to the one-point compactification \(S^2\) with value \(e_{11}\) at infinity. Its range is the line spanned by \((z,1)\) on the finite chart; on the other chart use \((1,1/z)\). On the circle \(|z|=1\), the unit-vector transition is multiplication by \(z\), of winding number one. The winding argument in the preceding projective-module lesson proves that this line bundle \(L\) is nontrivial.

It also proves that \([L]-[1]\) is not merely zero after stable addition. Otherwise \(L\oplus V\cong1\oplus V\) for some bundle \(V\), by the Grothendieck construction and the bundle/module correspondence. Taking top exterior powers gives \(L\otimes\det V\cong\det V\); tensoring with the dual determinant line would make \(L\) trivial, a contradiction. Thus (4.2) is a nonzero relative class.

On the other hand, \(D=C_0(\mathbb C,\mathbb K)\) has no nonzero projections. A continuous projection has norm zero or one at each point; connectedness makes that norm constant, and vanishing at infinity forces it to be zero. If any compact perturbation of \(T\) had closed range, Proposition 1.2 would make its kernel projections compact and therefore zero. The closed-range decomposition would then make it invertible, and Theorem 2.3 would give index zero, contradicting (4.2).

Consequently the unital hypothesis in Theorem 4.1 cannot be removed. The quotient index and the stable-multiplier computation, however, remain valid for arbitrary \(A\). Nonunital relative classes are precisely why defining every index by finite kernels would lose information.

## 5. Fredholm triples and arbitrary coefficient algebras

A Fredholm triple is \((E,F,T)\), with \(E,F\) countably generated Hilbert \(A\)-modules and \(T:E\to F\) Fredholm. We impose unitary equivalence, norm-continuous Fredholm homotopy on fixed modules, and addition or removal of triples whose operator is invertible. Addition is orthogonal direct sum. This describes the even Fredholm model; it does not include the additional left action needed for a general Kasparov bimodule.

**Lemma 5.1 (The \(\sigma\)-unital case).** If \(B\) is \(\sigma\)-unital, these triples are classified by \(K_0(B)\).

*Proof.* The module \(H_B\) is countably generated, so one may add its degenerate identity triple. Stabilization identifies both \(E\oplus H_B\) and \(F\oplus H_B\) with \(H_B\). The resulting operator is a standard-module Fredholm, and Section 3 classifies it by its index. Changing either stabilization unitary multiplies its quotient on one side by the image of an actual unitary. That unitary's quotient K₁ class is zero because \(K_1(\mathcal L(H_B))=0\). Thus the index and the classified triple are independent of the choices. Stable matrix additions in Section 3 are additions of countably generated invertible triples here. Conversely every standard Fredholm is such a triple. ∎

For arbitrary \(A\), adding the identity on \(H_A\) would leave this collection if \(A\) were not \(\sigma\)-unital. We instead reduce the data of each triple to a separable subalgebra and check that extension of coefficients respects its index.

**Lemma 5.2 (Naturality under coefficient extension).** Let \(B\subseteq C\) be \(\sigma\)-unital C*-algebras. Tensoring a countably generated \(B\)-triple with the correspondence \(C_C\) preserves Fredholmness and carries its index to the image under \(K_0(B)\to K_0(C)\). Nondegeneracy of the inclusion is not required.

*Proof.* The left action of \(B\) on \(C_C\) is compact, since \(\mathcal K(C)=C\). The tensor-compactness theorem therefore carries both parametrix defects to compacts. If \(x_j\) generates a module and \(u_n\) is a sequential approximate identity of \(B\), the vectors \(x_j\otimes u_n\) generate the extended module: \(x_ju_n\to x_j\), and balancing approximates every tensor in the generating span by their \(C\)-span. Thus countable generation is preserved.

It remains to verify the coefficient map on the index. After the \(B\)-stabilization in Lemma 5.1, tensoring gives a Fredholm on
\[
L=H_B\otimes_B C\cong\ell^2\boxtimes J,\qquad
J=\overline{\operatorname{span}}BC.
\]
Stabilize \(L\) over \(C\). The tensor homomorphism from \(\mathcal L(H_B)\), acting on the \(L\) summand and by zero on its complement, sends \(\mathcal K(H_B)\) into \(\mathcal K(H_C)\). It gives a possibly nonunital homomorphism of the two compact extensions. Unitizing and adding the identity on the complementary summand carries an invertible quotient representative to the stabilized extended Fredholm. Applying this homomorphism to the lift in (2.2) proves naturality of the boundary map. We must identify its compact K₀ map with coefficient inclusion.

The right ideal \(J\) has \(\mathcal K(J)=\overline{JJ^*}\subseteq C\), acting by left multiplication. Indeed the rank-one map for \(x,y\in J\) is multiplication by \(xy^*\), and that representation is faithful: an element of \(\overline{JJ^*}\) annihilating \(J\) annihilates its own dense product span and hence is zero. Notice \(B\subseteq J\) and \(B\subseteq\overline{JJ^*}\), by its own approximate identity and positive square roots.

Inside \(\mathcal K_C(J\oplus C)\), the formulas
\[
\rho_t(b)=
\begin{pmatrix}
\cos^2(t)b&\cos(t)\sin(t)b\\
\cos(t)\sin(t)b&\sin^2(t)b
\end{pmatrix},
\qquad 0\leq t\leq\pi/2,
\tag{5.1}
\]
give a norm-continuous homotopy of *-homomorphisms. The off-diagonal multiplication maps are compact because \(b\in J\); the diagonal entries belong to \(\mathcal K(J)\) and \(C\), respectively. Matrix multiplication, using \(\cos^2t+\sin^2t=1\), proves multiplicativity. The endpoints are the upper \(B\)-corner and its ordinary inclusion in the lower \(C\)-corner.

After stabilization of \(J\oplus C\), this homotopy proves equality of their maps into \(K_0(\mathcal K(H_C))\). The lower corner gives the usual coordinate coefficient map. More explicitly, any adjointable isometric embedding \(C\to H_C\) gives the same map as the first-coordinate embedding. If \(i,j\) are two such embeddings, \(v=ij^*\) has initial and final projections \(P_j,P_i\), and
\[
\begin{pmatrix}v&1-P_i\\1-P_j&-v^*\end{pmatrix}
\]
is a unitary on \(H_C\oplus H_C\) conjugating their two compact corner homomorphisms after adjoining a zero summand. This is valid for relative K₀ classes as well, by unitization. Matrix amplification of (5.1) identifies the tensor compact map with \(K_0(B)\to K_0(C)\). Boundary naturality now gives the asserted index identity. The degenerate summand used in the initial stabilization remains invertible after tensoring, so removing it does not change the index. ∎

**Lemma 5.3 (Separable reduction).** Every countably generated Fredholm \(A\)-triple is obtained by tensoring a Fredholm triple over some separable C*-subalgebra \(B\subseteq A\) with \(A_A\).

*Proof.* Choose countable generating sets \(X\subseteq E\), \(Y\subseteq F\), and a parametrix \(S\). Add the vectors occurring in finite-rank approximations of \(ST-1_E\) and \(TS-1_F\), choosing one approximation within \(1/n\) for every \(n\). Enlarge the two countable sets repeatedly so that
\[
TX\subseteq Y,\quad T^*Y\subseteq X,\quad
SY\subseteq X,\quad S^*X\subseteq Y.
\]
Let \(B\) be generated by all inner products within \(X\) and within \(Y\). It is separable. It is \(\sigma\)-unital: a countable norm-dense sequence generates \(B_B\) as a module, using its nondegenerate action, so the earlier countability criterion applies to \(\mathcal K(B)=B\).

Let \(E_B=\overline{\operatorname{span}}XB\), and define \(F_B\) similarly, with closure in the original module norm. Their inner products lie in \(B\), making them complete Hilbert \(B\)-modules. Each \(x\in X\) actually belongs to \(E_B\): if \(u_n\) is a \(B\) approximate identity, then
\[
\|x-xu_n\|^2
=\|(1-u_n)\langle x,x\rangle(1-u_n)\|\longrightarrow0.
\]
The analogous assertion holds for \(Y\). The operator and adjoint inclusions therefore restrict \(T,S,T^*,S^*\) to these modules. The chosen finite-rank approximations restrict to compacts, proving that the restricted \(T_B\) is Fredholm.

Multiplication gives a unitary
\[
E_B\otimes_B A\longrightarrow E,\qquad x\otimes a\longmapsto xa.
\tag{5.2}
\]
It preserves inner products since both are \(a^*\langle x,y\rangle b\). Its image contains \(XA\), dense in \(E\). The analogous unitary for \(F\) identifies the extended \(T_B\) with \(T\). ∎

**Theorem 5.4 (Fredholm-triple presentation).** For every C*-algebra \(A\), the equivalence classes of countably generated Fredholm triples form an abelian group naturally identified with \(K_0(A)\). For \(\sigma\)-unital \(A\), this identification is the standard-module index after stabilization.

*Proof.* Descend a triple to \(B\) as in Lemma 5.3 and define its index to be the image of its \(B\)-index in \(K_0(A)\). This definition is independent of the reduction. Given two reductions, take a separable subalgebra \(C\subseteq A\) containing both coefficient algebras and their countable vector inner products. Also include coefficients in countable approximations expressing each reduction's generating vectors in the other's generating \(A\)-span. Such approximations exist since both \(A\)-extensions are the original modules. Over this enlarged \(C\), the closures of the two generating spans coincide; their operators coincide by restriction. Lemma 5.2 identifies both index images with this common \(C\)-index, proving independence.

Direct sums can be reduced simultaneously, so the index is additive. An invertible triple reduces with its inverse and has zero index. Unitary equivalence can likewise be included in the countable data, so it preserves the index.

For a norm-continuous Fredholm path, the reduction can be made simultaneously for the whole path. Locally there are norm-continuous parametrices: near \(T_0\), if \(S_0\) is a parametrix and \(\delta=T_t-T_0\) is small, use
\[
S_t=(1+S_0\delta)^{-1}S_0
=S_0(1+\delta S_0)^{-1}.
\]
Multiplication shows that its two defects are compact. Patch finitely many local choices by a scalar partition of unity; the defects remain compact since the weights sum to one. Include the operators, their adjoints and finite-rank defect approximations at rational parameter values in Lemma 5.3. Norm continuity makes the resulting restricted modules invariant and the defects compact for every parameter. The reduced path has constant \(B\)-index, hence the original path has constant \(A\)-index.

Every \(K_0(A)\) class comes from a separable subalgebra \(B\): its finite matrix projections over \(A^+\) have only finitely many coefficient entries after subtracting scalar parts. Generate \(B\) by those entries. Corollary 3.2 represents the resulting \(B\)-class by a standard \(B\)-Fredholm. Tensor with \(A_A\); compactness and countable generation are preserved by the argument of Lemma 5.2, giving an \(A\)-triple with the prescribed index. This proves surjectivity.

If a descended \(B\)-index has zero image in \(K_0(A)\), its equality to zero has a finite stable projection-equivalence witness in matrices over \(A^+\). Include that witness's coefficient entries in a separable \(C\subseteq A\) containing \(B\). If the witness is expressed by a homotopy, include its values at rational parameters; norm closure includes the whole homotopy. The index is then already zero in \(K_0(C)\). Lemmas 5.1 and 5.2 make the extended \(C\)-triple equivalent to a degenerate triple. Tensoring that equivalence with \(A_A\) preserves compactness, norm homotopies, unitary equivalence and invertibility. It also preserves countable generation: use generators tensored with a sequential approximate identity of \(C\), exactly as in Lemma 5.2. Thus the original \(A\)-triple is zero.

Finally \((F,E,T^*)\) has the negative index of \((E,F,T)\), as is seen after a common separable reduction and Lemma 5.1. The preceding zero-index argument makes their sum zero as a triple class. Therefore every class has an inverse. Additivity, surjectivity and the zero-index argument now prove injectivity as well, completing the group identification. ∎

The same reduction compares this index with the finite-kernel formula when a countably generated triple has closed range. The spectral-gap functional calculus supplying its kernel projections restricts to the reduced modules. The restricted projections are compact by the parametrix-compression proof, and tensoring them back gives the original kernels and their finite projective classes. Thus the kernel-minus-cokernel convention is preserved throughout, including nonunital coefficient extension.

## 6. Numerical, family and geometric indices

**Example 6.1 (Complex coefficients).** For \(A=\mathbb C\), \(H_A=\ell^2\) and module compacts are ordinary compact operators. The Hilbert-space Fredholm theorem makes the range closed and the two kernels finite-dimensional. Their projection classes in \(K_0(\mathbb C)=\mathbb Z\) are their dimensions, so
\[
\operatorname{Ind}_{\mathbb C}(T)
=\dim\ker T-\dim\ker T^*.
\]
In particular the unilateral shift has index \(-1\). This sign agrees with the boundary computation (2.5).

**Example 6.2 (A family index bundle).** Let \(X\) be compact Hausdorff and let \(x\mapsto T_x\) be a norm-continuous family of Fredholm operators on a fixed separable infinite-dimensional Hilbert space \(H\). The module \(C(X,H)\) is \(H_{C(X)}\) after choosing an orthonormal basis: finite-coordinate approximation is uniform on the compact image of a continuous section, so the completed column norm is exactly its supremum norm. The family gives an adjointable operator \(T\); the adjoint family is norm continuous too.

This operator is module Fredholm. Near each \(x_0\), the parametrix formula used in Theorem 5.4 supplies a norm-continuous parametrix family from one at \(x_0\). A finite subordinate partition of unity patches these to \(S_x\). The two defects are norm-continuous families of compact operators, hence belong to \(\mathcal K(C(X,H))\). Indeed a compact subset of \(\mathbb K(H)\) is uniformly approximated by finite-coordinate compressions, giving finite matrices of continuous functions.

There is a uniform finite augmentation without normalizing \(T\). Choose \(\varepsilon>0\) below the spectrum of the positive invertible \(\pi(TT^*)\) in the module quotient. Then \(k=(\varepsilon-TT^*)_+\) is compact and \(TT^*+k\geq\varepsilon\,1\). Uniform finite-coordinate compression of \(k\), as in Theorem 4.1, gives \(N\) and \(c>0\) with \(TT^*+cP_N\geq(\varepsilon/2)1\). Thus
\[
R_x:H\oplus\mathbb C^N\to H,\qquad
R_x(h,a)=T_xh+\sqrt c\,Ja
\]
is onto for every \(x\). Its kernel projection
\(1-R_x^*(R_xR_x^*)^{-1}R_x\)
is norm continuous. It is module compact: in the quotient the finite summand disappears, and \(\pi(T)^*(\pi(T)\pi(T)^*)^{-1}\pi(T)=1\), so the projection has zero quotient image. Its fibres therefore have finite rank. The projective-module/bundle correspondence gives a vector bundle \(V=\ker R\), and the family index is
\[
\operatorname{Ind}(T)=[V]-[X\times\mathbb C^N]\in K^0(X).
\tag{6.1}
\]
To check the formula against the module index, join \(R\) to \((T,0)\) by scaling the finite-column term. Every operator on this path is Fredholm, because that term is compact. The closed-range kernel formula gives \(\operatorname{Ind}(R)=[V]\), while direct sum with the finite-module triple \((C(X)^N,0,0)\) gives
\(\operatorname{Ind}(T,0)=\operatorname{Ind}(T)+[C(X)^N]\).
Equation (6.1) follows. The construction makes no assumption that the kernels of the original family form bundles.

Every class is realized by such a norm-continuous family. If it is \([p]-[q]\) for finite continuous matrix projections, on \(\ell^2\otimes\mathbb C^n\) use
\[
T_p=S^*\otimes p+1\otimes(1-p),
\]
whose kernel is \(p\mathbb C^n\) and cokernel is zero. For \(q\), use \(S\otimes q+1\otimes(1-q)\), with the reverse defects. Their direct sum varies in norm continuously with \(x\) and has the prescribed index bundle. This is the realization direction of the family-index picture; no contractibility theorem for the whole Hilbert-space unitary group is used.

**Example 6.3 (A Mishchenko-Fomenko index).** Let \(G\) be a countable discrete group, let \(M\) be a closed even-dimensional spin\(^{c}\) manifold, and let \(f:M\to BG\). The associated flat module bundle
\[
\mathcal L_f=\widehat M\times_G C^*G
\]
has rank-one free right \(C^*G\)-module fibres; \(G\) acts on them by left multiplication by its canonical unitaries. If \(E\) is a Hermitian bundle on \(M\), the Dirac operator twisted by \(E\otimes\mathcal L_f\) has a Mishchenko-Fomenko index in \(K_0(C^*G)\). The exact assigned programme dependency is *The Baum–Connes assembly map and the conjecture*, Section 2, in *Kasparov’s KK-theory*: the Mishchenko–Fomenko construction and its comparison with assembly for the Dirac class of a proper cocompact action. Specializing to the covering classified by \(f\) gives the index map on \([M,f,E]\). This assigned proof is planned; Land, Definitions 3.3–3.4 and Proposition 3.5, credits the geometric statement.

The required content of that planned section includes the coefficient Sobolev construction, the compact-remainder elliptic parametrix and its bounded Fredholm realization, followed by the Dirac-index comparison, for this countable discrete covering and unital coefficient algebra. These analytic requirements are not claimed to be written merely by naming the index. Our bounded module results describe its index and its invariance, and unitality of \(C^*G\) permits the finite-projective kernel description after compact perturbation. The preceding bounded index theory is proved without this geometric application; the later assembly comparison uses that bounded index, so it supplies no circular proof of it.

## 7. Exercises with solutions

**Exercise 7.1 (Basic: the numerical index).** Recover the ordinary Fredholm index for \(A=\mathbb C\).

*Solution.* Module rank-one operators on \(\ell^2\) are ordinary rank-one operators, so their norm closure is the usual compact ideal. The Hilbert-space Fredholm theorem gives closed range and finite-dimensional kernels. Theorem 2.2 identifies the boundary index with their projection-class difference. Under the rank isomorphism \(K_0(\mathbb C)\cong\mathbb Z\), this is \(\dim\ker T-\dim\ker T^*\). The shift has zero kernel and one-dimensional cokernel, so its value is \(-1\). ∎

**Exercise 7.2 (Intermediate: compact kernel identity).** Prove finite generation of the two kernels for a closed-range Fredholm \(T:E\to F\).

*Solution.* The closed-range theorem makes the kernel projections \(P,Q\) adjointable. Compression of the two parametrix identities gives
\(P=-P(ST-1)P\) and \(Q=-Q(TS-1)Q\), so they are compact. The rank-one compression formula identifies their corner algebras with the compact algebras on their ranges. Hence each kernel has compact identity. The finite-frame theorem constructs vectors \(x_i\) with \(\sum_i\theta_{x_i,x_i}=1\), giving \(x=\sum_i x_i\langle x_i,x\rangle\). This is algebraic finite generation; the Gram projection identifies the kernel with a projection module. No assertion about arbitrary nonclosed-range kernels is used. ∎

**Exercise 7.3 (Intermediate: both multiplier K-groups).** Prove (3.1) by an infinite direct-sum argument.

*Solution.* Reindex \(H_A^\infty\) as \(H_A\) and take the diagonal amplification \(\alpha\). Separating its first summand gives
\(\alpha(x)=v_1xv_1^*+w\alpha(x)w^*\),
where the two range projections are orthogonal and sum to one. A corner made by an isometry induces the identity on K₀, using the partial isometry \(vp\), and on K₁, using the explicit unitary \(Z\) in Theorem 3.1 after unitization. Orthogonal direct sum is addition of the induced K-theory maps, so \(\alpha_*=\mathrm{id}_*+\alpha_*\) on each group. Cancellation proves both groups zero. The infinite sums are bounded adjointable diagonal operators and converge strictly, which is sufficient; no norm convergence of their finite partial sums is claimed. ∎

**Exercise 7.4 (Intermediate: the coefficient shift).** For unital \(A\), compute the index of \(S_A(a_1,a_2,\ldots)=(0,a_1,a_2,\ldots)\).

*Solution.* It is an adjointable isometry with
\(S_A^*S_A=1\) and \(1-S_AS_A^*=P_1\), projection onto the first \(A\)-coordinate. Since \(A\) is unital, \(P_1=\theta_{e_1,e_1}\) is compact. Thus \(S_A\) is Fredholm with closed range, kernel zero and cokernel \(A_A\). Its index is \(-[1_A]\in K_0(A)\). The unital condition matters: for nonunital \(A\ne0\), \(P_1\) need not be compact, since the identity on \(A_A\) is a multiplier rather than an element of \(\mathcal K(A)=A\). ∎

**Exercise 7.5 (Advanced: compare the family index).** Construct the index bundle of a norm-continuous Fredholm family over compact \(X\) and compare it with the \(C(X)\)-module index.

*Solution.* Use \(C(X,H)=H_{C(X)}\). Local continuous parametrices patch by a finite partition of unity, with compact operator defects; their compact-image uniform finite-coordinate approximations prove module Fredholmness. Choose a finite coordinate space \(\mathbb C^N\) and \(c>0\) so that \([T_x,\sqrt c\,J]\) is onto everywhere, using a positive compact correction of \(TT^*\) and uniform finite-coordinate approximation. The continuous projection
\(1-R_x^*(R_xR_x^*)^{-1}R_x\)
defines its finite-rank kernel bundle \(V\). Set the index bundle to \([V]-[\mathbb C^N]\).

Scaling \(J\) supplies a Fredholm path from \(R\) to \((T,0)\). Theorem 2.3 and the triple presentation give
\([V]=\operatorname{Ind}(R)=\operatorname{Ind}(T)+[\mathbb C^N]\).
Thus the bundle class equals the module index. Changing the augmentation yields the same class by that equality, and norm-continuous family homotopies preserve it. Pointwise kernel dimensions of \(T_x\) may jump; they are not used to form the bundle. ∎

## What this lesson does not prove

We use the preceding course proofs of closed-range decompositions, compact composition and compression, finite frames and relative K₀, stabilization, and tensor compactness. The relevant locators are the closed-range theorem in *Adjointable operators*, the finite-frame equivalences in *Finite projective modules, frames and K₀*, Theorem 3.1 of *Kasparov's stabilization theorem*, and Theorem 2.4 of *Tensor products and C*-correspondences*.

The written programme proofs supplying operator K-theory are Idempotents, projections and their equivalences, Theorems 4.2–4.3; The Grothendieck group and K₀ of a unital algebra, Theorems 3.2 and 4.2; Nonunital algebras: unitization, relative classes and half-exactness, Theorem 1.1; Matrix stability, stability and continuity of K₀, Theorems 1.1 and 4.1; and Invertibles, unitaries and K₁, Theorems 2.2 and 3.1 and Corollary 4.2. These supply the equivalence relations, relative classes, homotopy invariance, both stability maps and the product/direct-sum law. The boundary map is The index map and the exact sequence at K₀, Theorem 2.2, and exactness is The six-term exact sequence and the exponential map, Theorem 2.1, for arbitrary C*-algebra extensions. Blackadar, Sections 5.1–5.5, 8.1, 8.3 and 9.3, credits their classical formulations. We prove the closed-range comparison, multiplier computation, quotient isomorphisms and Fredholm-triple classification here. Naturality is also visible directly by applying coefficient maps to the lifts.

For complex coefficients we use Theorem 1.1 of *Fredholm operators and the stable index*: invertibility modulo Hilbert-space compacts is equivalent to closed range and finite-dimensional kernel and cokernel. That lesson denotes cokernel minus kernel by \(\kappa\), so our index is \(-\kappa\). The family example uses the finite-rank bundle correspondence proved earlier and the cutoff and finite-partition lemma proved in Section 5 of *Finite projective modules, frames and K₀*. Its realization argument is explicit; we do not prove the full Atiyah–Jänich classifying-space theorem.

The geometric application has the exact planned provider *The Baum–Connes assembly map and the conjecture*, Section 2, in *Kasparov’s KK-theory*, with the coefficient analytic and comparison requirements stated in Example 6.3. Land, Proposition 3.5, remains the source credit. No completed elliptic or assembly proof is claimed before that assigned provider is written. The Fredholm-triple presentation describes even coefficient K-theory; the full definition and product of Kasparov groups belong to a separate course.

## References

[Blackadar 1998] Bruce Blackadar, *K-Theory for Operator Algebras*, second edition, Cambridge University Press, 1998, Sections 5.2, 5.5, 8.1, 8.3, 9.3 and 12.2; Section 17.5 for the Fredholm picture of Kasparov theory. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).

[Blackadar 2006] Bruce Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Springer, 2006, II.7.2.9 for the closed-range theorem. [Author's revised edition](https://www.bruceblackadar.com/Mathematics/Cycr.pdf).

[Connes 1982] Alain Connes, “A survey of foliations and operator algebras,” *Operator Algebras and Applications*, Part I, Proceedings of Symposia in Pure Mathematics 38, American Mathematical Society, 1982, 521–628, the section on C*-modules and continuous fields over the leaf space. [Author's text](https://alainconnes.org/wp-content/uploads/foliationsfine.pdf).

[Land] Markus Land, “The analytical assembly map and index theory,” *Journal of Noncommutative Geometry* 9 (2015), 603–619; Section 3, especially Proposition 3.5. [Author's preprint, version 2](https://arxiv.org/abs/1306.5657v2).
