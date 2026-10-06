# Homotopy, associativity, the index pairing and KK-equivalence

*Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The product constructed in the preceding lesson makes cycles composable. Three further facts give the composition its force: an arbitrary module homotopy can be replaced by an operator homotopy, products associate, and composition with an odd Fredholm class is the familiar compression index. We prove these facts with their signs and countability conditions.

We use the graded cycle, tensor and compact-operator conventions of the preceding lessons. Products are written in execution order:
\(x\widehat\otimes_D y\) first applies \(x\), then \(y\).
The connection calculus, product existence and operator-homotopy uniqueness used below are Lemmas 1.1–1.2 and Theorems 3.1–4.2 of *Connections and the existence of the Kasparov product*. The graded technical theorem is Theorem 3.1 of *Kasparov's technical theorem*.

## 1. Moving an evaluation by an operator homotopy

Let \(I=[0,1]\), and let \(e_t:C(I)\to\mathbb C\) be evaluation. The usual homotopy \(t\mapsto e_t\) changes the representation. We need a homotopy that keeps a representation fixed and changes only its operator.

**Lemma 1.1 (the evaluation bridge).** The cycles of \(e_0,e_1\) have the same operator-homotopy class.

**Proof.** On \(H=L^2([0,2\pi])\), use the periodic Fourier basis and the bounded skew-adjoint operator
\[
De_n=i\,\operatorname{sign}(n)e_n,\qquad De_0=0.
\]
Thus \(D^*=-D\) and \(D^2=-1+p_0\), with \(p_0\) rank one. The commutator of \(D\) with multiplication by a periodic continuous function is compact. For a monomial it is finite rank, because a fixed shift crosses the sign change at only finitely many Fourier coordinates; uniform trigonometric approximation proves the assertion.

Choose a continuous function \(h:[0,2\pi]\to[-1,1]\) with
\(h(0)=1,h(2\pi)=-1\), and put \(k=(1-h^2)^{1/2}\).
Define
\[
T_h=M_h-M_kD.
\tag{1.1}
\]
The function \(k\) is periodic, with endpoint value zero. For any continuous interval function \(g\), both \(k\) and \(kg\) are periodic. The identity
\[
\begin{aligned}
M_k[D,M_g]&=[D,M_{kg}]\\
&\quad-[D,M_k]M_g
\end{aligned}
\tag{1.2}
\]
therefore proves its left side compact, even when \(g\) has different endpoint values.

The operator \(T_h\) is essentially unitary. Indeed, using \([D,M_k]\) compact,
\[
T_h^*T_h\equiv M_{h^2}+M_k[D,M_h]-M_{k^2}D^2\equiv1
\pmod{\mathcal K(H)}.
\]
The analogous expansion gives \(T_hT_h^*\equiv1\). Also
\([T_h,M_g]=-M_k[D,M_g]\) is compact by (1.2). The assignment \(h\mapsto T_h\) is norm-continuous in the uniform norm.

Its index is one. The space of the allowed \(h\)'s is convex, so all these indices agree. For \(h(\theta)=\cos(\theta/2)\), \(k=\sin(\theta/2)\), direct computation gives
\[
\begin{aligned}
T_h1&=\cos(\theta/2),\\
T_h\cos(n\theta)&=\cos((n-\tfrac12)\theta),\\
T_h\sin(n\theta)&=\sin((n-\tfrac12)\theta)\quad(n\geq1).
\end{aligned}
\tag{1.3}
\]
The half-integer sine and cosine functions form an orthogonal complete system, since their complex combinations are the Fourier basis multiplied by \(e^{i\theta/2}\). All noninitial modes in (1.3) map isometrically after normalization. The constant and first cosine have the same image, giving kernel \(\mathbb C(1-\cos\theta)\); their image spans the first half-integer cosine. Hence \(T_h\) is onto and has exactly that one-dimensional kernel.

Choose \(r:[0,2\pi]\to I\) constant zero on \([0,\pi/3]\), constant one on \([5\pi/3,2\pi]\), and affine between them. On \(H\oplus H^{\mathrm{op}}\) use the fixed representation
\[
\rho(g)=\operatorname{diag}(M_{g\circ r},M_{g\circ r}).
\]
The odd self-adjoint operator with bottom-left part \(T_h\) is a cycle by the preceding calculations.

Choose \(h_0=-1\) on \([\pi/3,2\pi]\), and \(h_1=1\) on \([0,5\pi/3]\), with the stipulated endpoint values. Let \(P,Q\) be the multiplication projections of the two constant end intervals. The functions \(k_0,k_1\) are supported in these intervals. Since \([M_{k_i},D]\) is compact, replacing the endpoint operators by
\[
T'_0=PT_{h_0}P-(1-P),\qquad
T'_1=QT_{h_1}Q+(1-Q)
\tag{1.4}
\]
is a compact perturbation. For example
\(M_{k_0}D(1-P)=M_{k_0},D\) is compact, and the other off-diagonal block vanishes. Thus these are valid endpoint perturbation paths.

The complementary cycles in (1.4) are exactly degenerate. The corner at \(P\) has scalar representation \(e_0\) and Fredholm index one; that at \(Q\) has scalar representation \(e_1\) and the same index. A Hilbert-space Fredholm operator in a scalar represented cycle is compactly perturbable to its polar partial isometry. Its invertible complement is a degenerate cycle, and its finite kernel/cokernel cycle reduces, by cancellation of opposite parity pairs, to its index times the one-dimensional evaluation cycle. Thus the two corners represent \(e_0,e_1\).

The path \(h_t=(1-t)h_0+th_1\), with the compact endpoint perturbations just described, is an operator homotopy on the fixed \(\rho\). It proves the result after addition of the displayed degenerate cycles. \(\square\)

The endpoint block corrections in (1.4) matter: the original \(T_{h_i}\) need not commute exactly with \(P,Q\). Compact commutation supplies the correction; exact block invariance is then true.

## 2. Homotopy and operator homotopy

**Lemma 2.1 (products of operator paths).** Suppose two input cycles vary by norm-continuous operator paths on fixed represented modules, with separable first source and \(\sigma\)-unital intermediate algebra. Their endpoint products are operator homotopic.

**Proof.** Normalize the two operator paths by the pointwise self-adjoint contraction construction. Continuous functional calculus preserves norm continuity. The fixed stabilization in the connection-existence proof gives a norm-continuous family \(G_t\) of connections. In the product-existence construction, generate \(A_2\) using all the defects
\[
G_t^2-1,\quad G_t-G_t^*,\quad
[G_t,\phi(a)]_{\mathrm{gr}},\quad
[F_{1,t}\widehat\otimes1,G_t]_{\mathrm{gr}}.
\]
Their norm-continuous dependence allows \(t\) and \(a\) to be restricted to countable dense sets in forming the algebra. Add the compact ideal as before. The separable derivating space includes the full two operator families and \(\phi(A)\). Every product and derivation hypothesis is exactly the one checked in the preceding lesson.

A single technical-theorem partition \(M,N\) now works for all \(t\). The operators
\[
F_t=M^{1/4}(F_{1,t}\widehat\otimes1)M^{1/4}
+N^{1/4}G_tN^{1/4}
\tag{2.1}
\]
are norm-continuous and satisfy the product axioms for each \(t\). Their endpoints give the required products; product uniqueness takes care of any originally chosen endpoint representatives. \(\square\)

**Lemma 2.2 (a degenerate right factor).** A product with a degenerate second cycle is operator homotopic to a degenerate cycle.

**Proof.** Exact graded commutation of its second operator with the intermediate algebra defines \(1\widehat\otimes F_2\), as in Solution 10.1 of the preceding lesson. Its adjoint and square defects vanish on the tensor module: multiplying those defects by any creation operator reduces them to the exact localized defects of the degenerate second cycle. The creation ranges span the tensor module. It also graded commutes exactly with the first representation and with \(F_1\widehat\otimes1\). Thus it is both a degenerate cycle and a product operator, whose positivity bracket is zero. Product uniqueness proves the assertion. \(\square\)

**Theorem 2.3 (comparison of homotopies).** For separable graded \(A\) and \(\sigma\)-unital graded \(B\), the map
\[
KK_{\mathrm{oh}}(A,B)\longrightarrow KK_h(A,B)
\tag{2.2}
\]
is an isomorphism.

**Proof.** An operator path is an interval-module cycle, so the map is defined and onto. For injectivity let \(\alpha\) be a cycle over \((A,C(I,B))\), with endpoint cycles \(\alpha_0,\alpha_1\).

Tensor the evaluation bridge of Lemma 1.1 externally with \(B\). The resulting fixed represented module is the graded Hilbert module
\((H\oplus H^{\mathrm{op}})\widehat\otimes B\), countably generated because \(B\) is \(\sigma\)-unital. Its operator path has endpoint classes
\[
[\operatorname{ev}_0]\oplus d_0,\qquad
[\operatorname{ev}_1]\oplus d_1
\]
under operator homotopy, where \(d_i\) are degenerate.
All compact-defect assertions survive tensoring after source multiplication: approximate an element of \(C(I,B)\) by finite sums \(g(t)b\), and use a Hilbert-space compact tensor multiplication by \(b\).

Apply Lemma 2.1 to the fixed first cycle \(\alpha\) and this second operator path. Its endpoint products are operator homotopic. By Lemma 2.2 their degenerate summands contribute zero. Products with evaluations are the coefficient pushforward cycles, by Theorem 5.2 of the preceding lesson; uniqueness identifies their operator-homotopy classes with \(\alpha_0,\alpha_1\). Hence the endpoints of every module homotopy are equal in \(KK_{\mathrm{oh}}\). This proves injectivity. \(\square\)

**Corollary 2.4 (the scalar and extension identifications).** For trivially graded \(\sigma\)-unital \(B\),
\[
KK^i(\mathbb C,B)\cong K_i(B),\qquad i=0,1.
\tag{2.3}
\]
For trivially graded separable \(A\) and \(\sigma\)-unital \(B\),
\[
KK^1(A,B)\cong\operatorname{Ext}(A,B)^{-1}.
\tag{2.4}
\]

**Proof.** The even and odd scalar computations in Theorems 2.2 and 3.2 of *Pictures of KK* compute \(KK_{\mathrm{oh}}\) by the stable Calkin boundary maps. Theorem 2.3 transfers them to \(KK_h\). The odd map sends a self-adjoint \(T\) to the projection \(q((1+T)/2)\), then uses the positive exponential boundary. The second boundary isomorphism uses the ordinary K-theory periodicity in the stated stable-Calkin prerequisite.

For extensions, Theorem 5.2 of *Pictures of KK* proves the full separable comparison with \(KK_c\), and its Theorem 9.4 proves \(KK_c=KK_{\mathrm{oh}}\). Apply Theorem 2.3. These are precisely the separability hypotheses used here; no nonseparable compact-homology identification is inferred. \(\square\)

## 3. The connection calculation for three factors

For three cycles \((E_i,\phi_i,F_i)\), write
\[
E_{12}=E_1\widehat\otimes_{\phi_2}E_2,\quad
E_{23}=E_2\widehat\otimes_{\phi_3}E_3,\quad
E=E_{12}\widehat\otimes_{\phi_3}E_3
\cong E_1\widehat\otimes E_{23}.
\]
The identification is the inner-product-preserving map on elementary tensors. Let \(F_{12}\) be an \(F_2\)-connection, \(F_{23}\) an \(F_3\)-connection and \(F\) an \(F_{23}\)-connection, all odd and self-adjoint. By composition of connections, \(F\) is also an \(F_3\)-connection for \(E_{12}\).

**Lemma 3.1 (the bracket is a connection).** Put
\[
S_{12}=F_{12}\widehat\otimes1,\quad S_2=F_2\widehat\otimes1.
\]
Then \([S_{12},F]_{\mathrm{gr}}\) is a
\([S_2,F_{23}]_{\mathrm{gr}}\)-connection for \(E_1\).

**Proof.** For homogeneous \(x\in E_1\), degree \(p\), the \(F_{12}\)-connection condition gives
\[
S_{12}T_x=(-1)^pT_xS_2+C_x\widehat\otimes1,
\]
where \(C_x\in\mathcal K(E_2,E_{12})\) has degree \(p+1\). The other connection gives
\(FT_x=(-1)^pT_xF_{23}+K_x\), with \(K_x\) compact on the final modules. Expanding the anticommutator using these two identities gives
\[
\begin{aligned}
\left[S_{12},F\right]_{\mathrm{gr}}T_x
-T_x[S_2,F_{23}]_{\mathrm{gr}}
&\equiv F(C_x\widehat\otimes1)\\
&\quad+(-1)^p(C_x\widehat\otimes1)F_{23}
\end{aligned}
\tag{3.1}
\]
modulo final compact operators.

Regard \(F_{23}\oplus F\) as an \(F_3\)-connection on
\((E_2\oplus E_{12})\widehat\otimes E_3\). Lemma 1.1 of the preceding lesson says it graded commutes modulo compacts with every first-factor compact matrix, including the off-diagonal \(C_x\). Its degree \(p+1\) gives exactly the plus sign on the right of (3.1). That side is compact. Taking adjoints proves the second creation condition. \(\square\)

We also need a localized positivity fact.

**Lemma 3.2 (the negative part).** If \(F_{23}\) is a product of \(F_2,F_3\), the negative part of
\[
K=[S_2,F_{23}]_{\mathrm{gr}}
\]
is locally compact for the source action of \(D_1\). Consequently the negative part of
\(H=[S_{12},F]_{\mathrm{gr}}\) is a \(0\)-connection for \(E_1\). It is also a \(0\)-connection for \(E_{12}\).

**Proof.** The even self-adjoint \(K\) commutes with the source modulo compacts. Expand its commutator with \(\phi_2(d)\): the term involving \([F_{23},\phi_2(d)]_{\mathrm{gr}}\) is compact; the other is the graded commutator of \(F_{23}\) with
\([F_2,\phi_2(d)]_{\mathrm{gr}}\widehat\otimes1\), also compact by its connection property.
The product positivity says
\(\phi_2(d)K\phi_2(d)^*\geq0\) modulo compacts. The negative-part calculation of Proposition 3.3 in the cycle lesson therefore gives \(K_-\phi_2(d)\) and \(\phi_2(d)K_-\) compact.

By Lemma 3.1 and continuous functional calculus, \(H_-\) is a \(K_-\)-connection. Local compactness of \(K_-\) makes its creation products compact, by the creation compactness test; hence this is a \(0\)-connection for \(E_1\).
Since \(F\) is an \(F_3\)-connection for \(E_{12}\), its graded commutator with the first-factor \(F_{12}\) is a \(0\)-connection for \(E_{12}\). Thus \(H\) annihilates its compact first-factor ideal modulo final compacts. Continuous functional calculus with \(t\mapsto t_-\), which vanishes at zero, keeps that annihilation property. This proves the second assertion. \(\square\)

## 4. Full associativity

**Theorem 4.1 (associativity).** Let \(A,D_1\) be separable graded C\*-algebras, let \(D_2\) be \(\sigma\)-unital, and let \(B\) be a graded C\*-algebra. For
\[
x\in KK(A,D_1),\quad y\in KK(D_1,D_2),\quad
z\in KK(D_2,B),
\]
one has
\[
x\widehat\otimes_{D_1}(y\widehat\otimes_{D_2}z)
=(x\widehat\otimes_{D_1}y)\widehat\otimes_{D_2}z.
\tag{4.1}
\]

**Proof.** Choose normalized cycles and self-adjoint product operators
\(F_{12},F_{23},F\), where \(F\) represents the left side. On \(E\) set
\[
S_1=F_1\widehat\otimes1\widehat\otimes1,\qquad
S_{12}=F_{12}\widehat\otimes1,\qquad J=\mathcal K(E).
\]
Let \(I_1,I_{12}\) be the images of \(\mathcal K(E_1)\) and \(\mathcal K(E_{12})\), each tensored with identity on the remaining factors. The algebra
\[
A_1=C^*(J,I_1,I_{12})
\]
is \(\sigma\)-unital. Indeed \(I_1\) normalizes \(I_{12}\), since it comes from an adjointable operator on \(E_{12}\), so \(I_{12}+I_1\) is a closed C\*-algebra; adding the ideal \(J\) retains closedness. A sum of strictly positive elements of these three images is strictly positive in \(A_1\).

Put \(H=[S_{12},F]_{\mathrm{gr}}\) and
\[
A_2=C^*(J,H_-,[S_1,F]_{\mathrm{gr}}).
\]
Both extra generators annihilate \(I_1\) and \(I_{12}\) modulo \(J\). For \(H_-\) this is Lemma 3.2. For \([S_1,F]_{\mathrm{gr}}\), apply the first-factor commutator rule once to the \(F_{23}\)-connection and once to the \(F_3\)-connection. Hence \(A_1A_2\subset J\), and \(A_2\) is \(\sigma\)-unital by adjoining its finite generating set to \(J\).

The space spanned by \(F,S_1,S_{12},\phi(A)\) derives \(A_1\).
The operator \(F\) commutes graded with both compact images modulo \(J\). The operators \(S_1,\phi(A)\) act adjointably on both first modules. The operator \(S_{12}\) normalizes \(I_{12}\) and has graded commutators with \(I_1\) in \(I_{12}\), by the \(F_{12}\)-connection property before the last tensoring. These facts verify the full derivation condition.

Apply the technical theorem and form
\[
F'=M^{1/2}S_1+N^{1/2}F,\qquad M+N=1.
\tag{4.2}
\]
Use the globally compact self-adjoint sandwich correction if necessary.
The product-existence calculation makes \((E,\phi,F')\) a cycle: \(M\) kills the localized first-input defects in \(I_1\), \(N\) kills the cross bracket, and the defects of \(F\) were already source-localized compacts.
Moreover
\[
\begin{aligned}
\phi(a)[F,F']_{\mathrm{gr}}\phi(a)^*
&\equiv\phi(a)M^{1/2}[F,S_1]_{\mathrm{gr}}\phi(a)^*\\
&\quad+2\phi(a)N^{1/2}\phi(a)^*\geq0\pmod J.
\end{aligned}
\]
The first term is positive by the original product alignment of \(F\), since \(M\) commutes with the sandwich modulo \(J\). Thus \(F'\) is operator homotopic to \(F\).

It remains to show that \(F'\) is a product of \(F_{12},F_3\). The \(M^{1/2}S_1\) term is a \(0\)-connection for \(E_{12}\), since \(M\) annihilates \(I_{12}\). The other term differs from \(F\), an \(F_3\)-connection for \(E_{12}\), by a \(0\)-connection. This proves the creation conditions.

For positivity the actual expression is
\[
\begin{aligned}
\phi(a)[S_{12},F']_{\mathrm{gr}}\phi(a)^*
&\equiv\phi(a)M^{1/2}[S_{12},S_1]_{\mathrm{gr}}\phi(a)^*\\
&\quad+\phi(a)N^{1/2}H\phi(a)^*.
\end{aligned}
\tag{4.3}
\]
Both terms are positive modulo \(J\). For the second, \(N^{1/2}H_-\in J\), so only the positive part remains, commuting with the cutoff modulo \(J\).

For the first, before tensoring with the final identity, the product positivity of \(F_{12}\) says that
\(\phi_1(a)[F_{12},F_1\widehat\otimes1]_{\mathrm{gr}}\phi_1(a)^*\)
is positive modulo \(\mathcal K(E_{12})\). Write that localized bracket as \(P-C\), where \(P\geq0\) is its positive part and \(C\in\mathcal K(E_{12})\) is its negative part. Under the final tensor homomorphism, \(C\) lands in \(I_{12}\), so \(M^{1/2}\) kills this error modulo \(J\). The first term of (4.3) is consequently the class of the actual positive operator \(M^{1/4}(P\widehat\otimes1)M^{1/4}\): commutation of \(M\) with the localized bracket modulo \(J\) passes to its positive part by continuous functional calculus. This proves positivity of that term. It need not vanish: annihilating the compact negative part gives no reason to annihilate the positive part. Both terms of (4.3) are retained in the associativity argument.

Thus \(F'\) is a product of \(F_{12},F_3\), while representing the same class as \(F\). Uniqueness proves (4.1). \(\square\)

In particular the theorem includes the cases where any factor is a homomorphism or an imprimitivity bimodule. Its proof uses the three-module compact ideals; it does not assume the tensor of an arbitrary first-factor compact operator is a compact operator on the final module.

In fact the same proof works for \(\sigma\)-unital \(D_1\) whenever the requisite binary product operators exist. Separability of \(D_1\) in the theorem guarantees existence of the inner product \(y\widehat\otimes_{D_2}z\); no other step uses it. In particular the explicit compact-left correspondence products give this existence for the Morita reductions used below, even with a nonseparable intermediate algebra.

## 5. Naturality, composition and rings

**Proposition 5.1 (naturality).** Whenever the displayed products satisfy the preceding separability and countability hypotheses, graded homomorphisms \(f:A'\to A\), \(g:B\to B'\), \(h:D\to D'\) give
\[
\begin{aligned}
f^*(x\widehat\otimes_D y)&=f^*x\widehat\otimes_D y,\\
g_*(x\widehat\otimes_D y)&=x\widehat\otimes_D g_*y,\\
h_*x\widehat\otimes_{D'}z&=x\widehat\otimes_D h^*z.
\end{aligned}
\tag{5.1}
\]

**Proof.** A product operator remains a product after precomposing its representation with \(f\). Its source conditions and positivity are tested on the represented elements \(f(a')\).

For the second identity tensor the product module and operator with \(B'\) along \(g\). Compact operators descend to compact operators: a rank-one operator becomes the product of two compact creation operators from \(B'\). The associating tensor unitary identifies this module with \(E_1\widehat\otimes(E_2\widehat\otimes_g B')\). The creation errors are the original errors tensored with \(1\), still compact. The induced homomorphism on adjointable operators preserves the positive quotient sandwich. Thus it is the desired product.

For the third identity the unitary is
\[
(E_1\widehat\otimes_h D')\widehat\otimes_{\psi'}E_2'
\longrightarrow E_1\widehat\otimes_{\psi'h}E_2',\qquad
(x\widehat\otimes d')\widehat\otimes y
\longmapsto x\widehat\otimes\psi'(d')y.
\tag{5.2}
\]
It preserves the defining inner products. Its range is dense even for a degenerate \(\psi'\): approximate \(x\) by \(xu_n\), with \(u_n\) an approximate identity of \(D\), and move \(h(u_n)\) to the second vector. A creation operator on the left corresponds to \(T_x\psi'(d')\) on the right. The connection error is the original error multiplied by \(\psi'(d')\), plus \(T_x\) times the compact graded commutator of \(F_2'\) with \(\psi'(d')\), with its Koszul sign. Both are compact. Taking adjoints proves the second creation condition. The first operator and representation coincide under (5.2), so positivity is unchanged. Uniqueness proves all three identities. \(\square\)

**Theorem 5.2 (the category and its endomorphism rings).** Separable graded C\*-algebras, with morphism groups \(KK(A,B)\) and composition the Kasparov product, form an additive category. The identity at \(A\) is \((A,\operatorname{id},0)\). For every such \(A\), \(KK(A,A)\) is a unital ring. In particular
\[
KK(\mathbb C,\mathbb C)\cong\mathbb Z
\quad\text{as unital rings}.
\tag{5.3}
\]
For homomorphisms \(f:A\to D\), \(g:D\to B\), composition gives
\([f]\widehat\otimes_D[g]=[g f]\).

**Proof.** The previous lesson proves bilinearity and both identity actions; Theorem 4.1 proves associativity. These are the category axioms and the distributive ring axioms. The identity assertion for homomorphisms follows directly by tensoring the two homomorphism cycles. The tensor \(D\widehat\otimes_g B\) identifies with \(B_g=\overline{g(D)B}\), with source action \(g f\) and zero operator. Its essential source submodule is \(\overline{g f(A)B}\), the same as for the homomorphism cycle of \(g f\). Proposition 5.1 of the preceding lesson joins each cycle to that common support cycle. Thus their homotopy classes agree; no orthogonal complement of the support module is assumed.

The scalar additive calculation identifies the class of
\((\mathbb C,\operatorname{id},0)\) with \(1\in\mathbb Z\). Every scalar class is an integer multiple of this class. Bilinearity and its identity action make their product \(m n\), proving (5.3).

To see additivity on objects, \(A\oplus D\) has the evident inclusion and projection homomorphisms. The two cross compositions are zero and the two diagonal compositions are identities. The sum of the two inclusion-projection endomorphisms is the identity: its homomorphism cycle decomposes as the direct sum on the right module \(A\oplus D\). These identities exhibit \(A\oplus D\) as a biproduct. The zero algebra is a zero object. \(\square\)

For completeness, the general product is obtained from ordinary products by dilation:
\[
\begin{aligned}
KK(A_1,B_1\widehat\otimes D)\times
KK(D\widehat\otimes A_2,B_2)\\
\longrightarrow KK(A_1\widehat\otimes A_2,B_1\widehat\otimes B_2).
\end{aligned}
\tag{5.4}
\]
Explicitly dilate the first class by \(A_2\), the second on the left by \(B_1\), and compose over \(B_1\widehat\otimes D\widehat\otimes A_2\). For separable \(A_1,A_2\) and \(\sigma\)-unital \(B_1,D\), all displayed modules and the intermediate algebra meet the countability hypotheses. Theorem 4.1 and Proposition 5.1 give its associativity and naturality by the canonical tensor-associating and signed-flip maps. This includes the external product of the preceding lesson.

Here dilation respects product operators by a direct check. Under its canonical tensor unitary, the creation operator for \(x\widehat\otimes c\) is \(T_x\widehat\otimes L_c\). A compact creation error becomes the original compact tensored with \(L_c\in\mathcal K(C)\), hence is compact; the adjoint error is the same calculation. Source multiplication likewise inserts a compact \(C\)-factor in each cycle defect.

For positivity, the even bracket \([S,F]_{\mathrm{gr}}\) commutes with the source modulo compacts. Expand that commutator: the term involving the compact source commutator of \(F\) is compact, and the other is the graded commutator of \(F\) with the compact first-factor operator \([F_1,\phi_1(a)]_{\mathrm{gr}}\widehat\otimes1\). Lemma 3.2's negative-part argument consequently makes the bracket's negative part locally compact for the source. After dilation its product with a finite source sum \(\sum_i a_i\widehat\otimes c_i\) is compact, because each term is a source-localized compact tensored with \(L_{c_i}\). Its positive part, tensored with identity, is positive in the faithful graded matrix model. Thus every finite source sum has a positive quotient sandwich; norm closure gives all source tests. Dilation therefore carries binary products to binary products. The canonical regrouping of a triple dilation reduces its two composition orders exactly to (4.1), proving the asserted associativity of (5.4); precomposition, coefficient pushforward and the balancing identity reduce its naturality to (5.1).

**Theorem 5.3 (symmetry of the external product).** For graded cycles the external product is preserved by the signed flips of the source and coefficient factors. For trivially graded algebras and parity classes this becomes
\[
\begin{gathered}
x\boxtimes y=(-1)^{pq}\,\sigma^*\tau_*(y\boxtimes x),\\
x\in KK^p(A_1,B_1),\\
y\in KK^q(A_2,B_2),
\end{gathered}
\tag{5.5}
\]
where \(\sigma:A_1\otimes A_2\to A_2\otimes A_1\) and
\(\tau:B_2\otimes B_1\to B_1\otimes B_2\) are the ordinary flips.

**Proof.** On \(E=E_1\widehat\otimes E_2\) put
\(S_1=F_1\widehat\otimes1\), \(S_2=1\widehat\otimes F_2\).
Normalize the inputs. These operators anticommute exactly. Let \(J=\mathcal K(E)\), and let
\[
I_1=\mathcal K(E_1)\widehat\otimes\phi_2(A_2),\qquad
I_2=\phi_1(A_1)\widehat\otimes\mathcal K(E_2)
\]
denote their represented closed images. They are \(\sigma\)-unital under the external-product hypotheses, and \(I_1I_2\subset J\), by the exterior compact-operator formula.

Apply the technical theorem to \(I_1+J,I_2+J\), including
\(S_1,S_2,\phi(A_1\widehat\otimes A_2)\) in its derivating space. The first operators preserve the corresponding compact first-factor ideals; a crossed derivation produces an original compact source commutator tensored with a compact operator, hence lands in \(J\). The source representation preserves each ideal. These observations verify every hypothesis. Obtain \(M,N\) with \(M I_1,N I_2\subset J\), \(M+N=1\), and the stipulated compact commutators.

The operator
\[
F=M^{1/2}S_1+N^{1/2}S_2
\]
is a cycle. For a source tensor, its weighted square and commutator defects lie respectively in \(MI_1\) and \(NI_2\); the cross square term is zero by exact anticommutation. The self-adjoint sandwich correction is globally compact.

It is a product for either ordering. For the first ordering the compact first-factor algebra is \(I_1\). The operator \(S_2\) is a connection: its creation error for \(x\widehat\otimes a_2\) is, with the Koszul sign, \(R_x\widehat\otimes[F_2,\phi_2(a_2)]_{\mathrm{gr}}\), where \(R_x:B_1\to E_1\) is compact because \(R_x^*R_x=\langle x,x\rangle\in\mathcal K(B_1)\). The error is thus compact. The \(M^{1/2}S_1\) term is a \(0\)-connection since \(M\) kills \(I_1\); \(N^{1/2}-1\) is a \(0\)-connection, so the second term retains the connection. The positivity bracket is \(2M^{1/2}S_1^2\); after a source sandwich it equals \(2\phi(a)M^{1/2}\phi(a)^*\) modulo \(J\), hence is positive. For the reverse ordering use \(I_2,N,S_2\) in the same computation. The signed module flip carries its operators and representations to this very module. Uniqueness therefore proves symmetry for the graded cycles.

For parity classes dilate their coefficient Cliffords and then use the matrix Morita reduction. When \(p=q=1\), exchanging the two Clifford generators in \(C_2\) is implemented by the odd unitary \((\sigma_1+\sigma_2)/\sqrt2\). It reverses the spinor grading, because it conjugates \(\sigma_3\) to \(-\sigma_3\). Reversing the grading of an even cycle with trivially graded source gives its negative: conjugating its operator by the original grading changes \(F\) to \(-F\) and leaves the representation fixed, giving the inverse-cycle formula. Thus this exchange contributes \(-1\). If either parity is zero there is no odd Clifford exchange and the sign is \(+1\). These four parity cases prove (5.5). \(\square\)

## 6. The odd product is the compression index

We fix the scalar odd identification by the **positive exponential boundary**:
a quotient projection \(p\) with self-adjoint lift \(a\) gives
\([\exp(2\pi i a)]\in K_1(B)\).
The even scalar index is kernel minus cokernel. These are the conventions of *Pictures of KK* and *The index pairing between K-theory and K-homology*.

The odd-by-odd product uses right Clifford dilation of the second factor and then the ordered \(C_2\)-matrix Morita correspondence. Before an even unitary rotation, the second cycle's original Clifford generator is \(\sigma_1\), and the auxiliary first cycle's generator is \(\sigma_2\), with grading \(\sigma_3\). After the even rotation they become \(-\sigma_2,\sigma_1\), the convention used for the two-circle example in the preceding lesson.

**Lemma 6.1 (an essential odd Hilbert-space representative).** An odd Fredholm class has a representative \((H,\pi,r)\) with \(\pi\) essential and \(r=r^*=r^{-1}\).

**Proof.** Let \(Q_0\) project onto \(\overline{\pi(B)H}\). It commutes with \(\pi(B)\). The off-diagonal operator is source-locally compact, because
\[
(1-Q_0)F\pi(b)=(1-Q_0)[F,\pi(b)]
\]
is compact; taking adjoints gives the other block. Thus removing the zero-representation complement and compressing gives a cycle with essential representation. Normalize its operator to a self-adjoint contraction \(f\).

Here the coefficient is \(\mathbb C\), so Hilbert-space range projections are available. They can be constructed without discontinuous norm functional calculus: for \(f_+=\max(f,0)\), the increasing contractions
\(f_+(f_++1/n)^{-1}\) converge strongly to the projection \(P_+\) onto \(\overline{\operatorname{Ran}f_+}\). Indeed bounded monotone positive operators converge strongly, since
\(\|(a_n-a_m)\xi\|^2\leq2\langle(a_n-a_m)\xi,\xi\rangle\); their action tends to the identity on \(\operatorname{Ran}f_+\) and is zero on its orthogonal complement. Construct \(P_-\) similarly from \(f_-=\max(-f,0)\). They are orthogonal and commute with \(f\).

Put \(P_0=1-P_+-P_-\) and \(r=P_+-P_-+P_0\). Then \(r\) is a self-adjoint involution, and
\[
(r-f)^2\leq1-f^2.
\]
For every \(b\), sandwich this inequality by \(\pi(b)\). Its right side is compact. In a compact-operator quotient a positive element dominated by zero is zero, so
\((r-f)\pi(b)\) is compact; adjoints give the other side. The locally compact perturbation rule therefore replaces \(f\) by \(r\) on the same essential representation. \(\square\)

**Theorem 6.2 (the odd index formula).** Let \(B\) be trivially graded and \(\sigma\)-unital. For an odd scalar class \(x\in KK^1(\mathbb C,B)\) and an odd Hilbert-space class \(y\in KK^1(B,\mathbb C)\), let \(u\) be the K-theory class corresponding to \(x\). Then
\[
x\widehat\otimes_B y
=\operatorname{index}\bigl(P\pi(u)P\bigr)
\in KK(\mathbb C,\mathbb C)=\mathbb Z,
\tag{6.1}
\]
where \(P=(1+r)/2\) for an involution representative of \(y\), with matrix amplification and unitization understood. The right side has kernel-minus-cokernel sign.

**Proof.** First work in the stable algebra \(J=B\otimes\mathcal K\). The scalar odd Calkin picture supplies a projection \(p\in M(J)/J\) and a self-adjoint contraction \(s\in M(J)\) with \(q(s)=2p-1\). Put
\[
a=(1+s)/2,\qquad t=(1-s^2)^{1/2}\in J,\qquad v=t+is\in M(J).
\tag{6.2}
\]
The element \(v\) is unitary, since \(s,t\) commute and \(s^2+t^2=1\). Its square has scalar quotient \(-1\), so \(-v^2\in1+J\).

Represent the odd class on \(J\) by an essential \(\Phi:J\to\mathcal L(H)\) and involution \(r=2P-1\), using Lemma 6.1. Extend \(\Phi\) to \(M(J)\) by [Lesson 05, Lemma 2.0](KT-KK-05.html#lemma-2-0-compact-module-operators-and-their-multipliers). In the decomposition \(H=PH\oplus(1-P)H\), write its multiplier blocks as
\[
\Phi(m)=
\begin{pmatrix}\alpha(m)&\beta(m)\\
\gamma(m)&\delta(m)\end{pmatrix}.
\]
The off-diagonal blocks are compact for \(m\in J\), because \([r,\Phi(m)]\) is compact. They need not be compact for arbitrary multipliers.

In the ordered Clifford model the first operator is \(\Phi(s)\sigma_2\), the second connection is \(r\sigma_1\), and the special formula of Theorem 6.1 in the preceding lesson gives
\[
F=\Phi(s)\sigma_2+\Phi(t)r\sigma_1.
\tag{6.3}
\]
Its scalar source commutator is zero. The second operator is a connection: under the essential identification
\((J\widehat\otimes C_1)\widehat\otimes_\psi E_2\cong E_2\),
its creation errors are exactly its compact commutators with \(\psi(J\widehat\otimes C_1)\). Thus that theorem identifies (6.3) with the product class, even though the special formula itself need not be a product connection.

The bottom-left part from even to odd is
\[
T=\Phi(t)r+i\Phi(s)
=\begin{pmatrix}
\alpha(v)&-\beta(v^*)\\
\gamma(v)&-\delta(v^*)
\end{pmatrix}.
\tag{6.4}
\]
It is Fredholm because (6.3) is a scalar cycle. Multiplication on the left by the actual unitary \(\Phi(v)\) does not change its index. The identities \(\Phi(v)\Phi(v^*)=1\) give the exact calculation
\[
\Phi(v)T=
\begin{pmatrix}\alpha(v^2)&0\\
\gamma(v^2)&-1\end{pmatrix}.
\tag{6.5}
\]
Since \(v^2\in J^+\), its lower-left block is compact. Therefore
\[
\operatorname{index}T=\operatorname{index}\alpha(v^2)
=\operatorname{index}\alpha(-v^2).
\tag{6.6}
\]

The K-class of \(-v^2\) is the positive exponential class of \(p\). On the spectrum \([-1,1]\) of \(s\),
\[
-v^2=\exp\bigl(i(2\arcsin s+\pi)\bigr).
\]
Interpolate its real phase with \(\pi(s+1)\). At \(s=-1\) both phases are zero, and at \(s=1\) both are \(2\pi\). Thus throughout the interpolation the quotient unitary is one, giving a norm-continuous path in \(1+J\) to
\(\exp(2\pi i a)\). The compressed operators along it are Fredholm, since their quotient images are unitaries and the compression commutators are compact. Their indices agree. This proves (6.1) for that exponential representative.

Every K-class \(u\in K_1(J)\) is such a boundary class by the scalar Calkin boundary isomorphism used in Corollary 2.4. Equality in \(K_1(J)\) is a matrix-stabilized norm unitary homotopy; compression along it is again a Fredholm path. Hence the formula holds for every representative \(u\), including formal stabilization and unitization.

Finally pass from \(J\) to \(B\) through the standard matrix Morita equivalence. Its inverse classes and product identities were proved in the preceding lesson; associativity shows that the scalar product is unchanged. The stabilized representation and projection give precisely the usual matrix amplification of \(P\pi(u)P\). This proves the general formula and its sign. \(\square\)

For the positive coordinate unitary on the circle, the Hardy compression is the unilateral shift, so the formula gives \(-1\), in agreement with the earlier odd index pairing. The Fourier circle representative with \(r=2P-1\), \(P\) projecting onto nonnegative modes, differs locally compactly from its bounded Dirac transform. Thus the examples have the same sign convention.

## 7. KK-equivalences

Two algebras \(A,B\) are **KK-equivalent** if there are
\[
x\in KK(A,B),\quad y\in KK(B,A),\qquad
x\widehat\otimes_B y=1_A,\quad
y\widehat\otimes_A x=1_B.
\tag{7.1}
\]

**Proposition 7.1 (consequences and examples).** A KK-equivalence induces isomorphisms of all KK groups in either variable, and hence of K-theory and K-homology. Morita equivalent \(\sigma\)-unital algebras are KK-equivalent. In particular \(A,M_n(A)\) and \(A\otimes\mathcal K\) are KK-equivalent. Homotopy-equivalent separable algebras are KK-equivalent.

**Proof.** Right multiplication by \(x\) has inverse right multiplication by \(y\), by associativity and (7.1). Left multiplication similarly has its stated inverse. Apply these statements to scalar K-theory and K-homology, with the Clifford dilation for degree one.

For a Morita equivalence take the bimodule cycle and its conjugate. The two inner-product tensor unitaries in Proposition 7.1 of the preceding lesson give exactly (7.1). The finite column module \(A^n\) and the standard module \(H_A\) give the matrix and compact-operator cases: their compact left algebras are \(M_n(A)\) and \(A\otimes\mathcal K\), and their dual row modules have the required inverse tensor products.

This Morita assertion also covers \(\sigma\)-unital algebras beyond the separable category. The two inverse products have explicit zero-operator representatives with compact left action, so they exist without a general product-existence theorem for nonseparable sources. Tensoring cycles with the bimodules and their duals gives inverse homotopy functors by the same two tensor unitaries. Thus the resulting KK and K-group isomorphisms retain that full \(\sigma\)-unital generality.

For homotopy equivalence use the two homomorphism classes. Their products are the classes of the composed maps by Theorem 5.2, and homotopy of homomorphisms gives equality of KK classes by the interval construction. Thus the two compositions have the identity classes. \(\square\)

**Proposition 7.2 (cones are K-contractible).** For a separable \(A\), the cone \(CA=C_0((0,1],A)\) has identity class zero. Consequently
\[
KK(CA,D)=0,\qquad KK(D,CA)=0
\]
whenever the products used to express the identity actions are defined.

**Proof.** Extend \(f\in CA\) continuously by \(f(0)=0\). The homomorphisms
\[
(\rho_t f)(s)=f(ts),\quad0\leq t\leq1,
\]
join zero to the identity in pointwise norm. Uniform continuity of \(f\) on \([0,1]\) proves this continuity in the cone norm. Their classes therefore agree, so \(1_{CA}=0\). Every class with source or target \(CA\) is its product with this identity; bilinearity makes it zero. \(\square\)

The Bott and Dirac constructions in the lesson *Bott periodicity in KK: the Bott and Dirac elements* provide classes between \(\mathbb C\) and \(C_0(\mathbb R^2)\) satisfying (7.1). That lesson must supply the construction and the two explicit product identities. The present proposition supplies their consequences once those identities are established.

## 8. Exercises

**8.1. Composed homomorphisms.** Prove directly on tensor cycles that
\([f]\widehat\otimes_D[g]=[g f]\), including nonunital maps.

**8.2. A homomorphism in the middle.** For \(h:D\to D'\), prove
\[
(x\widehat\otimes_D[h])\widehat\otimes_{D'}z
=x\widehat\otimes_D([h]\widehat\otimes_{D'}z)
\]
by the tensor unitary and connection conditions.

**8.3. Isomorphisms from equivalence.** For \(x,y\) satisfying (7.1), write the induced K-theory and K-homology maps and verify the two inverse compositions, in both parities.

**8.4. The odd unitary test.** Let \(B\) be unital, \(u\in M_n(B)\) unitary and \((H,\pi,r)\) an odd Fredholm representative with \(r^2=1\). Prove that the product of the K-class of \(u\) with this odd class is
\(\operatorname{index}(P_n\pi_n(u)P_n)\), where \(P_n\) is the matrix amplification of \((1+r)/2\). Fix the sign by the circle coordinate.

## 9. Solutions

**Solution to 8.1.** The tensor map
\(d\widehat\otimes b\mapsto g(d)b\) is an inner-product isometry from
\(D\widehat\otimes_g B\) onto \(B_g=\overline{g(D)B}\). The first source acts there by \(g f\). Both operators are zero, so the product conditions reduce to compact left action. The image of \(g(d)\) is compact on \(B_g\), using the rank-one approximations \(g(u_k)g(d)g(u_k)\) from the homomorphism theorem. The tensor cycle and the cycle of \(g f\) have the common essential source submodule \(\overline{g f(A)B}\). The essential-replacement interval construction, with zero connection, joins both to its zero-operator cycle. They therefore give \([g f]\), even when that support has no adjointable complement.

**Solution to 8.2.** Represent \(x\) on \(E_1\) and \(z\) on \(E_2'\). The two tensor modules are identified by (5.2), with the same first operator and first source representation. For a dense elementary first vector \(x\widehat\otimes d'\), its creation operator is \(T_x\psi'(d')\). Move the second operator first across \(\psi'(d')\), giving its compact graded source commutator, and then across \(T_x\), giving the product's compact creation error. The combined sign is \((-1)^{|x|+|d'|}\). Taking adjoints proves the other condition. Positivity is identical under the module unitary. Thus the same final operator is a product in both constructions, and uniqueness proves the equality. Countable generation and range density hold as in Proposition 5.1, including degenerate homomorphisms.

**Solution to 8.3.** On K-theory use \(v\mapsto v\widehat\otimes_A x\); its inverse is \(w\mapsto w\widehat\otimes_B y\). Associativity makes their composition
\(v\mapsto v\widehat\otimes_A(x\widehat\otimes_B y)=v\).
The other composition uses \(y\widehat\otimes_A x=1_B\). On K-homology from \(A\) to \(B\), use \(q\mapsto y\widehat\otimes_A q\), whose inverse is \(r\mapsto x\widehat\otimes_B r\). The same identities prove both inverse compositions. For degree one dilate the equivalence classes by \(C_1\) on the coefficient or insert the corresponding source Clifford factor; the tensor unitary and the identity correspondence preserve the product equations. Thus both parity maps are isomorphisms.

**Solution to 8.4.** Stabilize \(B\) and choose a quotient projection \(p\) whose positive exponential boundary is \([u]\), using the stable Calkin scalar identification. Lift \(2p-1\) to a self-adjoint contraction \(s\). With \(t=(1-s^2)^{1/2}\), \(v=t+is\), Theorem 6.2 constructs the product operator with bottom-left Fredholm map (6.4). The exact unitary multiplication (6.5) reduces its index to the compression of \(-v^2\).

The phase interpolation
\[
(1-\lambda)(2\arcsin s+\pi)+\lambda\pi(s+1)
\]
keeps the quotient exponential equal to one and joins \(-v^2\) to the positive boundary unitary. The latter and \(u\), after finite matrix stabilization, are unitary homotopic by equality of their K-classes. Compress every unitary along these norm paths by \(P_n\); all compressed operators are Fredholm because the off-diagonal blocks are compact. Their indices are constant. This gives exactly
\(\operatorname{index}(P_n\pi_n(u)P_n)\).
For \(B=C(\mathbb T)\), the coordinate \(u(z)=z\), and nonnegative-mode \(P\), the compression is the unilateral shift with zero kernel and one-dimensional cokernel. The product is therefore \(-1\), fixing the kernel-minus-cokernel sign.

## What this lesson does not prove

The scalar Calkin boundary isomorphisms are the precise Hilbert-module prerequisite already stated in *Pictures of KK*: vanishing of the two K-groups of the stable multiplier algebra and the resulting index and positive exponential boundary isomorphisms. The odd isomorphism uses the programme's ordinary K-theory Bott theorem. The nondegenerate multiplier extension is proved in [Lesson 05, Lemma 2.0](KT-KK-05.html#lemma-2-0-compact-module-operators-and-their-multipliers). These are prerequisites in *Hilbert C\*-modules and Morita equivalence*.

The separable scalar and extension computations used in Corollary 2.4 are proved in *Pictures of KK*, at Theorems 2.2, 3.2 and 5.2. Its compact-homology comparison is Theorem 9.4. Their exact separable scope is sufficient here; the arbitrary-source compact-homology extension comparison remains a separate obligation of that lesson.

Bott and Dirac inverses, the Thom isomorphism and the universal coefficient theorem are treated in the following lessons. No one of them is used to prove associativity or the index formula here.

## References and source credit

- B. Blackadar, [*K-Theory for Operator Algebras*, author-posted corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf). The [author identifies this freely downloadable version](https://www.bruceblackadar.com/mathpubs.html) as a slightly corrected second edition. The source retains its author copyright and the usage terms stated on that page. Sections 18.5–18.8 and 18.11, printed pp. 175–179 and 181–184, for homotopy comparison, associativity, naturality and the index pairing. The required proofs and all exercise solutions are given in this lesson and its exact preceding programme prerequisites.
