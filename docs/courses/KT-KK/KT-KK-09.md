# Connections and the existence of the Kasparov product

*Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A tensor product of represented Hilbert modules gives the right space for composing two cycles. It does not give an operator automatically. The second operator usually fails to respect the relation used to form the interior tensor product. A connection replaces that nonexistent operator by one that respects elementary tensors up to compact errors. Kasparov's technical theorem then combines this connection with the first operator.

We prove existence and uniqueness, including the compactness and positivity calculations. We also calculate products with homomorphisms, Morita equivalences, two circle classes and a vector bundle. Associativity and comparison of the two homotopy relations are proved in the next lesson; neither is used to construct the product here.

All tensor products and commutators are graded. For homogeneous operators,
\[
[R,T]_{\mathrm{gr}}=RT-(-1)^{|R||T|}TR.
\]
In particular the commutator of two odd operators is their anticommutator. We write \(\mathcal L(E)\) and \(\mathcal K(E)\) for adjointable and compact module operators, and use the analogous notation between different modules. The stabilization and compact-operator rules were proved in *Graded C\*-algebras, Clifford algebras and graded Hilbert modules*. The square-root partition is Theorem 3.1 and Corollary 3.2 of *Kasparov's technical theorem*.

## 1. The connection conditions

Let \(E_1\) be a countably generated graded Hilbert \(D\)-module, let \(E_2\) be a graded Hilbert \(B\)-module, and let
\(\psi:D\to\mathcal L(E_2)\) be a graded homomorphism. Set
\[
E=E_1\widehat\otimes_\psi E_2.
\]
For homogeneous \(x\in E_1\) define the creation operator
\[
T_x y=x\widehat\otimes y,\qquad
T_x^*(z\widehat\otimes y)=\psi(\langle x,z\rangle)y.
\tag{1.1}
\]
These formulas give \(\|T_x\|\leq\|x\|\) and degree \(|x|\). In particular
\[
T_x^*T_z=\psi(\langle x,z\rangle),\qquad
T_xT_z^*=\theta_{x,z}\widehat\otimes1.
\tag{1.2}
\]

Let \(F_2\) have degree \(p\), with
\([F_2,\psi(d)]_{\mathrm{gr}}\) compact for every \(d\in D\).
An **\(F_2\)-connection** is an operator \(G\) of degree \(p\) such that
\[
\begin{aligned}
T_xF_2-(-1)^{p|x|}GT_x&\in\mathcal K(E_2,E),\\
F_2T_x^*-(-1)^{p|x|}T_x^*G&\in\mathcal K(E,E_2)
\end{aligned}
\tag{1.3}
\]
for every homogeneous \(x\). The two conditions are both imposed; for self-adjoint \(F_2,G\), either one implies the other by taking adjoints.

**Lemma 1.1 (the compactness test).** Put
\[
I_0=\mathcal K(E_1)\widehat\otimes1\subset\mathcal L(E).
\]
An operator \(Z\) is a \(0\)-connection if and only if
\[
ZI_0\subset\mathcal K(E),\qquad I_0Z\subset\mathcal K(E).
\tag{1.4}
\]
Every connection graded commutes with \(I_0\) modulo \(\mathcal K(E)\).

**Proof.** If \(ZT_x\) and \(T_x^*Z\) are compact, multiplication by \(T_y^*,T_y\) and (1.2) prove (1.4) first on rank-one generators and then on their norm closure. Conversely take an approximate identity \(u_\lambda\) of \(\mathcal K(E_1)\). It acts in norm on every vector of \(E_1\); this follows first on the range of rank-one operators and then by density. Thus
\[
\|(u_\lambda\widehat\otimes1)T_x-T_x\|
\leq\|u_\lambda x-x\|\longrightarrow0.
\]
Under (1.4), \(Z(u_\lambda\widehat\otimes1)T_x\) is compact and converges in norm to \(ZT_x\). Applying the same argument to \(Z^*\) proves the other condition.

For a connection \(G\), move it across the two creation operators in \(T_xT_y^*\), using (1.3). The two resulting errors are compact; the remaining terms have the sign \((-1)^{p(|x|+|y|)}\). This is precisely the graded commutator with \(\theta_{x,y}\widehat\otimes1\). Norm approximation proves the assertion for \(I_0\). \(\square\)

The following elementary rules will make the later calculations shorter.

**Lemma 1.2 (connection calculus).** Adjoints of connections are connections of the adjoints. Sums and products of homogeneous connections correspond to sums and products of the second operators, with the usual degree bookkeeping. Two connections of the same operator differ by a \(0\)-connection. For self-adjoint connections, continuous functional calculus has the same property; even and odd functions have the corresponding parity.

If \(S=R\widehat\otimes1\), for homogeneous \(R\in\mathcal L(E_1)\), then
\[
[S,G]_{\mathrm{gr}}\text{ is a }0\text{-connection}.
\tag{1.5}
\]
Finally, connections compose on a triple interior tensor product.

**Proof.** Taking adjoints in (1.3) gives the first assertion. For products use, modulo compact operators,
\[
GH T_x
\equiv(-1)^{(|G|+|H|)|x|}T_xF_2F'_2.
\]
This follows by moving \(H\), then \(G\), past \(T_x\); the errors remain compact after multiplication by bounded operators. The adjoint-side calculation is the same. The sum and difference assertions follow directly from (1.3). Polynomial approximation on a compact spectral interval proves the assertion about continuous functions, since the connection conditions are norm closed.

For (1.5), \(ST_x=T_{Rx}\). Moving \(G\) across \(T_x\) and \(T_{Rx}\) shows
\[
SGT_x\equiv(-1)^{p|x|}T_{Rx}F_2,\qquad
GST_x\equiv(-1)^{p(|R|+|x|)}T_{Rx}F_2.
\]
Their graded difference vanishes modulo compacts. The second creation condition follows by the adjoint calculation.

For the last assertion write a creation operator for an elementary vector \(x\widehat\otimes y\) as \(T_xU_y\), where \(U_y\) is the creation operator for the second tensor product. Move the final connection past \(T_x\), then the intermediate connection past \(U_y\). The total sign is the sum of the two vector degrees. Each error is compact. Taking adjoints proves the second condition. Finite sums of elementary vectors are dense and the creation operators depend continuously in norm on their vectors, completing the proof. \(\square\)

Here and below, an operator on the first factor really does tensor with \(1\): it is \(D\)-linear and adjointable. An operator on the second factor generally does not tensor with \(1\).

**Theorem 1.3 (existence of connections).** An \(F_2\)-connection exists. It can be chosen self-adjoint when \(F_2\) is self-adjoint, of the same degree, and with norm at most \(\|F_2\|\). A norm-continuous path \(F_{2,t}\) admits a norm-continuous path of such connections.

**Proof.** Regard \(E_1\) as a module over the forced unitization \(D^+\), and extend \(\psi\) to the unital homomorphism
\(\psi^+(d+\lambda1)=\psi(d)+\lambda1\).
Countable generation is retained. The natural map
\[
E_1\widehat\otimes_\psi E_2
\longrightarrow E_1\widehat\otimes_{\psi^+}E_2
\]
is unitary: both inner products agree, and the unitization balancing relations already hold by linearity and the scalar action. Graded stabilization realizes \(E_1=P\widehat H_{D^+}\) for an even projection \(P\).

On \(\widehat H_{D^+}\widehat\otimes_{\psi^+}E_2
\cong\widehat\ell^2\widehat\otimes E_2\), define
\[
C(e_j\widehat\otimes y)
=(-1)^{p|e_j|}e_j\widehat\otimes F_2y.
\tag{1.6}
\]
For a homogeneous vector \(x=\sum_j e_jx_j\) supported on finitely many coordinates, \(|x_j|=|x|-|e_j|\). The \(j\)-th entry of its creation error is consequently
\[
\begin{aligned}
&(CT_x-(-1)^{p|x|}T_xF_2)_j\\
&\quad=(-1)^{p|e_j|}
 \bigl(F_2\psi^+(x_j)-(-1)^{p|x_j|}\psi^+(x_j)F_2\bigr).
\end{aligned}
\]
Every entry is compact by the input commutator condition; the added scalar coordinates have zero commutator. A finite column of compact operators is compact, by approximating each entry by finite-rank operators. Applying the same calculation to \(F_2^*\) and taking adjoints gives the other creation error. The bound \(\|T_x\|\leq\|x\|\) extends both errors by norm approximation to every vector. This proves the full connection condition for \(C\).

Tensor \(P\) with \(1\), and compress:
\[
G=(P\widehat\otimes1)C(P\widehat\otimes1).
\tag{1.7}
\]
For \(x\in PE_1^{\mathrm{standard}}\), one has
\((P\widehat\otimes1)T_x=T_x\). Thus the first creation error for \(G\) is the projection times the corresponding error for \(C\); the second is obtained on the other side. This proves the connection property. Compression retains the degree, norm bound and self-adjointness. Apply the same fixed compression to \(C_t\) for a path \(F_{2,t}\); (1.6) shows norm continuity. \(\square\)

The construction is called a **Grassmann connection**. It uses the unitization of the intermediate algebra, so it does not require that \(\psi(D)E_2\) be all of \(E_2\).

## 2. The product axioms and normalization

Take cycles
\[
\alpha=(E_1,\phi_1,F_1)\in\mathcal E(A,D),\qquad
\beta=(E_2,\psi,F_2)\in\mathcal E(D,B).
\]
On \(E=E_1\widehat\otimes_\psi E_2\) put
\[
\phi=\phi_1\widehat\otimes1,\qquad S=F_1\widehat\otimes1.
\]
A **product operator** is an odd \(F\in\mathcal L(E)\) satisfying:

1. \((E,\phi,F)\) is a Kasparov cycle.
2. \(F\) is an \(F_2\)-connection.
3. For every \(a\in A\),
\[
\phi(a)[S,F]_{\mathrm{gr}}\phi(a)^*\geq0
\quad\text{in }\mathcal L(E)/\mathcal K(E).
\tag{2.1}
\]

We can normalize \(F_1,F_2\) to odd self-adjoint contractions by Theorem 3.2 of *Kasparov modules and the groups \(KK(A,B)\)*. These normalizations preserve the product axioms in the following precise sense.

**Lemma 2.1 (locally compact changes of the inputs).** Replacing either input operator by a locally compact perturbation does not change the connection and localized positivity requirements, modulo compacts. A product-operator perturbation retains the product axioms if it is both a \(0\)-connection and two-sided locally compact for \(\phi(A)\). Self-adjoint normalization and clipping of a product operator have these properties.

**Proof.** Suppose \(R\) and \(R^*\) are locally compact for \(\psi(D)\). Then
\[
(T_xR)^*(T_xR)=R^*\psi(\langle x,x\rangle)R
\]
is compact. An adjointable operator \(T\) with \(T^*T\) compact is compact: use \(T(T^*T+\varepsilon)^{-1}T^*T\) and the scalar bound on its error to approximate \(T\) by compact operators. Thus \(T_xR\) is compact; the adjoint version proves \(RT_x^*\) compact. This proves the assertion for the second input.

For a first-input perturbation \(R_1\), write \(R=R_1\widehat\otimes1\). Each \(R\phi(a)\) and \(\phi(a)R\) lies in \(I_0\). Use Lemma 1.1 to move the connection \(F\) across these operators, and use its cycle commutator to move it across \(\phi(a)\). The two terms in
\(\phi(a)[R,F]_{\mathrm{gr}}\phi(a)^*\) then cancel modulo compacts. Thus (2.1) is unchanged.

For the stated product-operator perturbation \(Z\), both terms of
\(\phi(a)[S,Z]_{\mathrm{gr}}\phi(a)^*\) are compact: one contains \(Z\phi(a)^*\), the other contains \(\phi(a)Z\). The connection assertion is its assumed \(0\)-connection condition. In self-adjoint normalization this condition holds automatically, since \(F-F^*\) is a \(0\)-connection when \(F_2\) is self-adjoint. A clipping function then changes \(F\) by a function vanishing at \(\pm1\). Since \(F_2^2-1\) is locally compact for \(\psi(D)\), that function of \(F_2\) has compact creation products by the first part. Lemma 1.2 makes the clipping change a \(0\)-connection. The cycle perturbation rule supplies its local compactness. \(\square\)

## 3. Existence from the technical theorem

**Theorem 3.1 (existence of the product).** If \(A\) is separable, \(D\) is \(\sigma\)-unital and both input modules are countably generated, there is a product operator. For self-adjoint input operators it can be chosen self-adjoint. No \(\sigma\)-unitality hypothesis on \(B\) is needed.

**Proof.** Normalize the inputs as above and choose a self-adjoint odd \(F_2\)-connection \(G\). The module \(E\) is countably generated: products \(x_i\widehat\otimes y_j\) of two countable generating families have dense \(B\)-span, using the balancing relation to move the \(D\)-coefficients into \(\psi(D)y_j\).
Put \(J=\mathcal K(E)\), a \(\sigma\)-unital algebra, and
\[
A_1=C^*(I_0,J)=I_0+J.
\]
Its two summands are \(\sigma\)-unital, so a sum of their strictly positive elements is strictly positive in \(A_1\). Set
\[
\begin{aligned}
A_2&=C^*(J\cup\mathcal Z),\\
\mathcal Z&=\{G^2-1,[S,G]_{\mathrm{gr}}\}\\
&\quad\cup\{[G,\phi(a)]_{\mathrm{gr}}:a\in A\}.
\end{aligned}
\tag{3.1}
\]
All generators can be selected from a countable dense subset of \(A\). Adjoining them to the \(\sigma\)-unital ideal \(J\) gives a \(\sigma\)-unital algebra: if \(h_J\) is strictly positive in \(J\), add a convergent positive sum of suitably weighted \(z_j^*z_j+z_jz_j^*\). The resulting \(h\) has \(f_n(h)z_j\to z_j\) and \(z_jf_n(h)\to z_j\), since \(h\) dominates a positive multiple of both \(z_j^*z_j\) and \(z_jz_j^*\); it also acts as an approximate identity on \(J\). Thus \(f_n(h)\) approximates every element of the generated algebra.

Each generator in (3.1), other than \(J\), is a \(0\)-connection. For \(G^2-1\), Lemma 1.2 gives a connection of \(F_2^2-1\), whose creation errors are compact by Lemma 2.1. The commutators are \(0\)-connections by (1.5). They and their adjoints therefore annihilate \(I_0\) modulo \(J\). This proves
\[
A_1A_2\subset J.
\tag{3.2}
\]
The separable graded space spanned by \(S,G,\phi(A)\) derives \(A_1\). For \(S,\phi(A)\) this is the adjointable ideal property on the first module; for \(G\) it is Lemma 1.1.

The graded technical theorem supplies even positive contractions \(M,N\) with
\[
M+N=1,\quad MA_1\subset J,\quad NA_2\subset J,
\tag{3.3}
\]
and compact commutators with \(S,G,\phi(A)\). Its square-root corollary gives the same annihilation and commutation properties for the needed roots.
First define
\[
F_0=M^{1/2}S+N^{1/2}G.
\tag{3.4}
\]
The operator \(M^{1/2}\) is a \(0\)-connection by Lemma 1.1. Hence its product with \(S\) is a \(0\)-connection. Since \(N-1=-M\) is a \(0\)-connection, functional calculus gives \(N^{1/2}-1\) a \(0\)-connection as well. Consequently the second term in (3.4) is an \(F_2\)-connection. Their sum is the required connection.

All the following equalities are modulo \(J\). Move the cutoffs past \(S,G,\phi(a)\) to obtain
\[
\begin{aligned}
(F_0^2-1)\phi(a)
&=M(S^2-1)\phi(a)\\
&\quad+N(G^2-1)\phi(a)\\
&\quad+M^{1/2}N^{1/2}[S,G]_{\mathrm{gr}}\phi(a)\\
&=0.
\end{aligned}
\tag{3.5}
\]
Here \((S^2-1)\phi(a)\in I_0\), while the other two defects belong to \(A_2\). Also
\[
\begin{aligned}
\left[F_0,\phi(a)\right]_{\mathrm{gr}}
&\equiv M^{1/2}[S,\phi(a)]_{\mathrm{gr}}\\
&\quad+N^{1/2}[G,\phi(a)]_{\mathrm{gr}}=0.
\end{aligned}
\tag{3.6}
\]
The first commutator is in \(I_0\), and the second is in \(A_2\).
The adjoint defect is compact because the two cutoffs commute with the self-adjoint \(S,G\) modulo \(J\).

Finally,
\[
\begin{aligned}
\phi(a)[S,F_0]_{\mathrm{gr}}\phi(a)^*
&\equiv2\phi(a)M^{1/2}S^2\phi(a)^*\\
&\equiv2\phi(a)M^{1/2}\phi(a)^*\geq0.
\end{aligned}
\tag{3.7}
\]
The omitted commutator with \(G\) is killed by \(N^{1/2}\). The second equality uses
\((S^2-1)\phi(a)^*\in I_0\) and the cutoff commutators. This proves all three product conditions.

For an exactly self-adjoint operator use
\[
F=M^{1/4}SM^{1/4}+N^{1/4}GN^{1/4}.
\tag{3.8}
\]
It differs from \(F_0\) by a globally compact operator, so all the verified conditions persist. Undoing the input normalizations with Lemma 2.1 proves the stated generality. \(\square\)

Notice the localization in (3.5). For a nonunital source one only knows
\((F_1^2-1)\phi_1(a)\) is compact. One cannot replace this by a global assertion \(F_1^2-1\in\mathcal K(E_1)\).

## 4. Uniqueness and descent to homotopy classes

**Theorem 4.1 (uniqueness up to operator homotopy).** Under the hypotheses of Theorem 3.1, any two product operators on the given tensor module represent the same operator-homotopy class.

**Proof.** Normalize \(F_1\) and the two product operators \(F,F'\) to self-adjoint contractions. Lemma 2.1 preserves their product conditions. This time apply the technical theorem with the same \(A_1\) and
\[
A_2=C^*(J,\ [S,F]_{\mathrm{gr}},\
[S,F']_{\mathrm{gr}},\ F-F').
\tag{4.1}
\]
These generators are \(0\)-connections by Lemma 1.2. Include \(S,F,F',\phi(A)\) in the separable derivating space. As in Section 3 all hypotheses are satisfied. Let \(M,N\) be the resulting partition and put
\[
H=M^{1/2}S+N^{1/2}F.
\tag{4.2}
\]
Use its self-adjoint sandwich version if desired. The existence calculation shows that \(H\) is a product operator: the defects of \(F\) are already locally compact, while \(M\) kills the first-module defects and \(N\) kills \([S,F]_{\mathrm{gr}}\).

We compare \(H\) to both original operators. Fix \(a\), put \(b=\phi(a)\), and take \(T=F\) or \(T=F'\). Modulo \(J\) the comparison is
\[
\begin{aligned}
b[T,H]_{\mathrm{gr}}b^*
&=bM^{1/2}[T,S]_{\mathrm{gr}}b^*\\
&\quad+2bN^{1/2}b^*.
\end{aligned}
\tag{4.3}
\]
For \(T=F\), use the cycle equation for \(F\). For \(T=F'\), use
\(N^{1/2}(F-F')=0\) modulo \(J\) to replace the term
\(N^{1/2}[F',F]_{\mathrm{gr}}\) by \(2N^{1/2}F^2\), then uses the same localized cycle equation.

These sums are positive. Indeed \(M^{1/2}\) commutes modulo \(J\) with all operators in the sandwich, so its product with the positive localized anticommutator is positive. Proposition 3.3 of *Kasparov modules and the groups \(KK(A,B)\)* supplies an operator homotopy from \(F\) to \(H\), and one from \(F'\) to \(H\). Reverse and concatenate the latter to prove the assertion. \(\square\)

The proof needs positivity, rather than smallness of the ordinary commutator. Both \(S\) and \(F\) are odd, so their relevant bracket is \(SF+FS\).

**Theorem 4.2 (the bilinear product).** The construction gives a well-defined bilinear map
\[
KK(A,D)\times KK(D,B)\longrightarrow KK(A,B),\qquad
(x,y)\longmapsto x\widehat\otimes_D y.
\tag{4.4}
\]

**Proof.** A homotopy of the second cycle is a cycle over \(C([0,1],B)\). Apply Theorem 3.1 with that coefficient algebra. The tensor module evaluates to the two endpoint tensor modules; creation conditions, compact defects and quotient positivity descend under evaluation. Its endpoints are products of the endpoint input cycles and hence have the required classes by Theorem 4.1.

For a homotopy of the first cycle, its intermediate algebra is \(C([0,1],D)\), still \(\sigma\)-unital. Tensor the second cycle externally with \(C([0,1])\), using the pointwise representation and constant operator. Compact defects are continuous compact-valued fields. Apply the same theorem and evaluate. The canonical map identifying the evaluated interior tensor product with the tensor product of the evaluated modules is unitary by its inner-product formula and density of elementary tensors. This proves invariance in both variables.

Direct sums of product operators satisfy every axiom for a direct sum in either input, by the two block creation conditions and block positivity. Theorem 4.1 then proves additivity. Degenerate cycles have zero homotopy class by Proposition 2.3 of the cycle lesson, so the preceding homotopy invariance also covers their addition. Thus (4.4) is well-defined on the groups. \(\square\)

## 5. Essential representations and homomorphisms

A representation is **essential** if \(\overline{\psi(D)E_2}=E_2\). This is useful when identifying \(D\widehat\otimes_\psi E_2\) with \(E_2\). An arbitrary representation need not be essential, and its essential submodule need not have an adjointable orthogonal projection.

**Proposition 5.1 (essential replacement).** If \(D\) is \(\sigma\)-unital, every cycle \((E_2,\psi,F_2)\) is homotopic to a cycle on
\(E_2^0=\overline{\psi(D)E_2}\), with its essential representation.

**Proof.** Normalize \(F_2\) to be self-adjoint. Set
\[
L=\{f\in C([0,1],D^+):f(1)\in D\}.
\]
It is a countably generated Hilbert ideal of \(C([0,1],D^+)\). For example, if \(h\) is strictly positive in \(D\), the function
\(\ell(t)=(1-t)1+th\) is strictly positive in \(L\): its standard functional-calculus approximate identity converges on every fiber, and uniformly on a given continuous section by compactness of the interval and a finite-neighborhood argument. Thus \(L\) is \(\sigma\)-unital and generated as a Hilbert ideal by a countable approximate identity.

Tensor \(L\) with the constant interval module
\(\overline E_2=C([0,1],E_2)\), using the pointwise unital extension \(\psi^+\). The map
\[
f\widehat\otimes \xi\longmapsto
\bigl(t\mapsto\psi^+(f(t))\xi(t)\bigr)
\]
identifies this tensor module with
\[
\mathcal M=\{\xi\in C([0,1],E_2):\xi(1)\in E_2^0\}.
\tag{5.1}
\]
It preserves inner products. Its image is dense: first approximate the endpoint value by finite sums \(\psi(d)y\), subtract their constant sections, and approximate the remaining section by sections vanishing near \(1\). Those sections are obtained with scalar cutoffs supported away from \(1\), which belong to \(L\). The approximation is uniform. Products of countable generating families show countable generation of \(\mathcal M\).

Choose a self-adjoint Grassmann \(F_2\)-connection \(G\) on this tensor module. Let \(D\) act through its constant embedding in \(L\), followed by the left action on the tensor product. Left multiplication by an element of \(L\) is compact on the Hilbert ideal \(L\): rank-one operators are multiplication by \(fg^*\), and their closed span is \(L\). Lemma 1.1 therefore gives compact representation commutators.

For the square defect one must retain localization to \(D\), since \(F_2\) need not be a cycle for the unitization \(D^+\). Approximate \(d\in D\) by finite sums \(d_1d_2^*\) with \(d_i\in D\), regarded as constant vectors in \(L\). Its represented left multiplication on the tensor module is then approximated by \(T_{d_1}T_{d_2}^*\). The connection identities give
\[
(G^2-1)T_{d_1}T_{d_2}^*
\equiv T_{d_1}(F_2^2-1)T_{d_2}^*
\pmod{\mathcal K(\mathcal M)}.
\]
The right side is compact by the creation compactness test of Lemma 2.1, because the original square defect is locally compact for \(\psi(D)\). Its interval field is compact in \(C([0,1],\mathcal K(E_2))\). Taking the finite-sum limit proves the localized square condition. Self-adjointness supplies the adjoint condition. Thus \((\mathcal M,\psi,G)\) is an interval cycle.

Its fiber at \(0\) is \(D^+\widehat\otimes_{\psi^+}E_2\cong E_2\). The creation operator for \(1\in D^+\) is this unitary identification, so the connection condition gives \(G_0-F_2\) compact. At \(1\) the fiber is \(D\widehat\otimes_\psi E_2\cong E_2^0\), with essential representation. Combining the interval cycle with the initial compact perturbation proves the assertion. \(\square\)

The same construction supplies the explicit multiplication connections used later. For homogeneous \(d\in D\), let \(A_d:E_2\to E_2^0\) send \(y\) to \(\psi(d)y\). Its adjoint is multiplication by \(d^*\), followed by inclusion in \(E_2\); the inner-product identity verifies this without an orthogonal projection onto \(E_2^0\). At the final fiber, the creation operator for the constant vector \(d\in L\) is exactly \(A_d\). Therefore the Grassmann connection gives
\[
F_2^0A_d-(-1)^{|d|}A_dF_2
\in\mathcal K(E_2,E_2^0),
\tag{5.1a}
\]
and its adjoint condition. At the initial fiber the creation for \(1\) identifies \(G_0\) with \(F_2\) modulo compacts, as above. Self-adjoint normalization and clipping preserve (5.1a): a two-sided locally compact change \(K\) of the final operator has compact \(KA_d\), by approximating \(d\) by sums of products and writing \(A_{rs}=\psi^0(r)A_s\). The changes of the initial operator have compact \(A_dK\) by the analogous adjoint-side argument. Hence the replacement can be normalized while retaining both multiplication-connection conditions.

**Theorem 5.2 (products with homomorphisms).** For graded homomorphisms
\(f:A\to D\) and \(g:D\to B\), under the countability hypotheses for their homomorphism cycles,
\[
[f]\widehat\otimes_D y=f^*(y),\qquad
x\widehat\otimes_D[g]=g_*(x).
\tag{5.2}
\]
Consequently \(1_A=[\operatorname{id}_A]\) is a two-sided identity whenever the indicated products are defined.

**Proof.** The homomorphism cycle for \(f\) is \((D,f,0)\). Replace the representation of \(y\) by an essential one using Proposition 5.1. The unitary
\[
D\widehat\otimes_\psi E_2\longrightarrow E_2,\qquad
d\widehat\otimes y\longmapsto\psi(d)y
\tag{5.3}
\]
intertwines the representation with \(\psi f\). Its creation errors for \(F_2\) are the original compact commutators with \(\psi(d)\). It is a cycle, and its positivity condition is zero because the first operator is zero. This gives \(f^*(y)\).

For \(g\), write \(E_g=\overline{g(D)B}\). Since the intermediate algebra \(D\) is \(\sigma\)-unital, a countable approximate identity makes this module countably generated, and \(g(d)|_{E_g}\) is compact by the support-module proof in Lesson 06, Section 5. Thus \((E_g,g,0)\) is the homomorphism cycle even for arbitrary \(B\). If \(B\) is \(\sigma\)-unital, Lemma 5.2 there identifies it with the canonical cycle \((B,g,0)\).

The inclusion of \(E_g\) into \(B\) gives a unitary
\(E_1\widehat\otimes_gE_g\to E_1\widehat\otimes_gB\): it preserves inner products, and its range is dense because
\(x\widehat\otimes b=\lim_j xe_j\widehat\otimes b=\lim_jx\widehat\otimes g(e_j)b\).
The tensor module is countably generated by the vectors \(x_i\widehat\otimes g(e_j)\), for generating vectors \(x_i\) of \(E_1\). Under this unitary the proposed tensor cycle is
\[
(E_1\widehat\otimes_g B,\ \phi_1\widehat\otimes1,\
F_1\widehat\otimes1).
\]
Each creation operator \(T_x:E_g\to E_1\widehat\otimes_g E_g\) is compact. Indeed \(T_x^*T_x\) is the compact action of \(g(\langle x,x\rangle)\) on \(E_g\), and the compactness test used in Lemma 2.1 applies. Hence \(S=F_1\widehat\otimes1\) is a \(0\)-connection. Compact input defects tensor to compact operators here: a rank-one operator \(\theta_{x,z}\) becomes \(T_xT_z^*\). Finally
\[
\phi(a)[S,S]_{\mathrm{gr}}\phi(a)^*
=2\phi(a)S^2\phi(a)^*\geq0
\]
already as an operator, since \(S\) is self-adjoint. This is exactly the coefficient pushforward. Choosing \(f\) or \(g\) to be the identity proves the last statement. \(\square\)

If \(B\) is not \(\sigma\)-unital, the full Hilbert module \(B\) need not be countably generated, so \((B,g,0)\) is not automatically an allowed cycle. For separable \(D\), use instead the countably generated ideal module
\[
B_g=\overline{g(D)B}\subset B.
\]
A countable approximate identity of \(D\) acts in norm on this module, so \(g(u_n)\) generate it as a right module. The left action of \(g(d)\) is compact: the multipliers
\(g(u_n)g(d)g(u_n)\) converge to \(g(d)\) in norm, and each is multiplication by \(xy^*\) for \(x=g(u_n)g(d)\), \(y=g(u_n)\) in \(B_g\), hence a rank-one operator on \(B_g\). The tensor product with \(E_1\) is unchanged, since \(E_1D\) is dense in \(E_1\). The proof of (5.2) then applies with \(B_g\). For \(\sigma\)-unital \(B\), the simpler full-module cycle suffices.

## 6. A useful formula which need not be a connection

Suppose \(F_1\) is a self-adjoint contraction and \(G\) is an odd \(F_2\)-connection, without requiring \(G\) to be self-adjoint. Put
\[
R=(1-S^2)^{1/2},\qquad H=S+RG.
\tag{6.1}
\]
This formula is useful when its representation commutators are compact. It does not generally satisfy the connection condition itself.

**Theorem 6.1 (the special formula).** Under the product hypotheses, if
\([H,\phi(a)]_{\mathrm{gr}}\) is compact for all \(a\in A\), then \((E,\phi,H)\) is a cycle operator homotopic to a product operator.

**Proof.** We first prove the cycle assertion without assuming that \(S\) graded commutes with \(G\) globally modulo compacts.
Let
\[
C=C^*(1,J,I_0,S,G,\phi(A)),\qquad Q=C/J,
\]
Let \(I\) be the closed two-sided ideal of \(Q\) generated by the image of \(I_0\). This image need not itself be an ideal. A \(0\)-connection \(D\in C\) annihilates \(I\), as follows. Suppress quotient symbols for this calculation. First-factor generators \(S,\phi(a)\), and generators from \(I_0\), multiply \(I_0\) into itself on either side. The generators \(G,G^*\) graded commute with \(I_0\) in \(Q\), by Lemma 1.1. Generators from \(J\) have zero image. The identity has the first property.

For a homogeneous word \(c=a_1\cdots a_n\) in these generators and \(i\in I_0\), prove \(Dci=0\) by induction on \(n\). The empty word is Lemma 1.1. If the last generator is a first-factor generator, combine \(a_ni\in I_0\) and apply the induction hypothesis to the shorter word. If it is \(G\) or \(G^*\), write \(c=u a_n\) and move \(i\) past that last generator:
\[
\begin{aligned}
Du a_ni
&=(-1)^{|a_n||i|}Du i a_n\\
&=0.
\end{aligned}
\]
The remaining zero-image and identity cases are immediate. Thus \(Dci=0\) for all words, then for their linear span and norm closure. Multiplication on the right proves that \(D\) kills every generator \(ci c'\) of \(I\). Apply the same argument to the \(0\)-connection \(D^*\), and take adjoints, to obtain \(ID=0\). This proves annihilation without asserting that arbitrary products of derivating operators still derive \(I_0+J\). Write
\[
Z=\operatorname{Ann}(I)
=\{z\in Q:zI=Iz=0\}.
\]
This is a closed two-sided ideal, and \(I\cap Z=0\): an element \(z\) in the intersection has \(zz^*=0\). In these quotient calculations we suppress the quotient symbols.

The operators \(G^2-1\), \(G-G^*\) and \([S,G]_{\mathrm{gr}}\) belong to \(Z\), by the connection calculus and the second input's localized defects. In \(Q/Z\), \(G\) is self-adjoint and anticommutes with \(S\), so it commutes with \(S^2\) and with \(R\). Thus \([G,R],[G^*,R]\in Z\). Direct multiplication gives
\[
\begin{aligned}
H-H^*&=R(G-G^*)+[R,G^*]\in Z,\\
H^2-1&=R^2(G^2-1)+R[S,G]_{\mathrm{gr}}\\
&\quad+R[G,R]G\in Z.
\end{aligned}
\tag{6.2}
\]

The first input cycle implies
\[
R\phi(a),\ \phi(a)R,\ [S,\phi(a)]_{\mathrm{gr}}\in I.
\tag{6.3}
\]
For the roots in (6.3), pass first to
\(\mathcal L(E_1)/\mathcal K(E_1)\): \(F_1\) commutes graded with the source, and \((1-F_1^2)\phi_1(a)=0\); commuting functional calculus gives the square-root assertion there. Tensor the resulting compact operators with \(1\).

Now pass to \(Q/I\). There \(R\phi(a)=0\), \(S\) commutes graded with \(\phi(a)\), and \(S^2\phi(a)=\phi(a)\). By the assumed pseudolocality of \(H\),
\[
RH\phi(a)=(-1)^{|a|}R\phi(a)H=0
\]
for homogeneous \(a\). Since \(R\) commutes with \(S\), this says \(R^2G\phi(a)=0\). Positivity of \(R\) gives \(RG\phi(a)=0\): the square of its norm is the norm of
\(\phi(a)^*G^*R^2G\phi(a)\), which is zero. Hence
\[
H\phi(a)=H^*\phi(a)=S\phi(a)
\quad\text{in }Q/I.
\]
For the square, graded commutation of \(S\) with the source gives
\[
\begin{aligned}
H^2\phi(a)&=HS\phi(a)\\
&=(-1)^{|a|}H\phi(a)S\\
&=(-1)^{|a|}S\phi(a)S\\
&=S^2\phi(a)=\phi(a).
\end{aligned}
\]
The localized defects therefore belong to \(I\), as well as to \(Z\) by (6.2). Their intersection is zero. This proves all cycle defects compact in the original algebra.

To compare with a product, use the Section 3 technical-theorem construction, adding \([G,R]\) and \(G-G^*\) to \(A_2\), and \(R\) to the derivating space already containing \(S,G,\phi(A)\). These additions are permitted: the added defects are \(0\)-connections by the quotient calculation above, and \(R\) is an even first-factor operator, so it normalizes \(I_0\) and derives \(I_0+J\). The cutoffs commute with \(H\) modulo \(J\) because, for \(P=M,N\),
\[
\begin{aligned}
\left[P,H\right]&=[P,S]+[P,R]G\\
&\quad+R[P,G]\in J.
\end{aligned}
\]
Functional calculus gives the same compact commutator for their required roots. No derivation condition on \(H\) is needed. The second input may first be normalized without changing which operators are its connections, by Lemma 2.1. Let
\[
F=M^{1/2}S+N^{1/2}G
\]
be the resulting product operator. Its self-adjoint version differs globally compactly, since \(N^{1/2}(G-G^*)\) is compact; equivalently the construction may use \((G+G^*)/2\). The extra cutoff conditions and (6.3) give
\[
\begin{aligned}
\phi(a)[H,F]_{\mathrm{gr}}\phi(a)^*
&\equiv2\phi(a)M^{1/2}S^2\phi(a)^*\\
&\quad+2\phi(a)N^{1/2}R\phi(a)^*\geq0
\quad\pmod J.
\end{aligned}
\tag{6.4}
\]
Here \([H,S]_{\mathrm{gr}}=2S^2+R[S,G]_{\mathrm{gr}}\); the second term disappears after sandwiching, because \(\phi(a)R\in I\) and the bracket annihilates \(I\). Also
\([H,G]_{\mathrm{gr}}=[S,G]_{\mathrm{gr}}+2RG^2+[G,R]G\); the \(N^{1/2}\) cutoff kills its two bracket terms and the square defect. The remaining two summands in (6.4) are positive because the cutoffs commute modulo \(J\) with \(S\) and \(R\).

The positive comparison criterion proves the operator homotopy to \(F\). This proves the formula without an unverified interpolation path. \(\square\)

## 7. Morita and external products

**Proposition 7.1 (imprimitivity bimodules).** Let \(X\) be an imprimitivity \(A\)-\(D\) bimodule, with \(A,D\) \(\sigma\)-unital. Its cycle \((X,\lambda,0)\) has an inverse represented by the conjugate \(D\)-\(A\) bimodule \(X^*\). Products with this cycle are the usual Morita tensor constructions.

**Proof.** Compact left action makes the zero operator a valid cycle; \(\sigma\)-unitality of \(\mathcal K(X)=A\) gives countable generation. For a cycle on \(E_2\), every \(F_2\)-connection on \(X\widehat\otimes_D E_2\) is a cycle: its defects are \(0\)-connections and the source action lies in \(\mathcal K(X)\widehat\otimes1\). Positivity is zero because the first operator is zero. Thus it computes the indicated Morita construction.

For two zero-operator bimodule cycles use the zero product operator. The inner-product maps
\[
\begin{aligned}
X^*\widehat\otimes_A X&\longrightarrow D,
&\bar x\widehat\otimes y&\longmapsto\langle x,y\rangle_D,\\
X\widehat\otimes_D X^*&\longrightarrow A,
&x\widehat\otimes\bar y&\longmapsto{}_A\langle x,y\rangle
\end{aligned}
\tag{7.1}
\]
are well-defined bimodule isometries. For example the squared inner-product calculation for the first uses
\[
\langle y_1,{}_A\langle x_1,x_2\rangle y_2\rangle_D
=\langle y_1,x_1\rangle_D\langle x_2,y_2\rangle_D.
\]
Fullness makes their ranges dense and hence surjective. The corresponding product cycles are \((D,\operatorname{id},0)\) and \((A,\operatorname{id},0)\), the identities of Theorem 5.2. This proves the assertion. \(\square\)

For separable source algebras and \(\sigma\)-unital coefficient algebras, dilation by an auxiliary algebra \(C\) is
\[
\tau_C(E,\phi,F)
=(E\widehat\otimes C,\ \phi\widehat\otimes1,\
F\widehat\otimes1).
\]
The auxiliary algebra must be \(\sigma\)-unital to guarantee countable generation of this displayed module. Compact defects are checked after multiplying by \(a\widehat\otimes c\): they are original compact operators tensored with multiplication by \(c\in\mathcal K(C)\). The same construction over an interval shows homotopy invariance.

Thus for \(x\in KK(A_1,B_1)\) and \(y\in KK(A_2,B_2)\) we define the **external product**
\[
x\boxtimes y
=\tau_{A_2}(x)\widehat\otimes_{B_1\widehat\otimes A_2}
\tau_{B_1}(y)
\in KK(A_1\widehat\otimes A_2,B_1\widehat\otimes B_2).
\tag{7.2}
\]
The second dilation places \(B_1\) on the left, with the graded flip used to order its factors. Countable generation and the intermediate \(\sigma\)-unitality hold under the stated hypotheses. Theorem 4.2 makes (7.2) bilinear and well-defined. Its associativity and graded symmetry will follow in the next lesson from the internal product.

Coefficient Morita reduction is compatible with this construction directly, without invoking associativity. If \(Y\) is a compact-left correspondence and \(F\) is a product operator, \(F\widehat\otimes1\) satisfies the same product axioms after tensoring the coefficient modules with \(Y\). Compact creation errors remain compact by the compact-left tensor rule, the canonical tensor-associating unitary identifies the creation operators, and the induced homomorphism on adjointable operators preserves quotient positivity. This also justifies using the \(C_2\)-\(\mathbb C\) matrix correspondence to express the product of two odd classes as an even cycle.

## 8. The two circle classes

Let \(e_n(z)=z^n\) be the Fourier basis of \(L^2(\mathbb T)\), and let the odd circle cycle have operator
\[
F_{\mathbb T}e_n=f(n)e_n,\qquad
f(n)=\frac{n}{\sqrt{1+n^2}}.
\tag{8.1}
\]
This is the bounded transform of \(-i\,d/d\theta\). Multiplication by \(z\) is the bilateral shift, and its commutator with (8.1) is compact because \(f(n+1)-f(n)\to0\) at both ends. Laurent-polynomial approximation gives compact commutators for all continuous functions.

**Proposition 8.1 (the torus product).** With the order of the two circle factors fixed, their external product is the even cycle on
\[
H=\ell^2(\mathbb Z^2)\otimes\mathbb C^2,\qquad
\Gamma=\sigma_3,
\]
with multiplication representation of \(C(\mathbb T^2)\) and
\[
F e_{n,m}
=\frac{n\sigma_1-m\sigma_2}{\sqrt{1+n^2+m^2}}e_{n,m}.
\tag{8.2}
\]
Here
\[
\begin{gathered}
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\\
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\end{gathered}
\]

**Proof.** In the Clifford model for the product, take
\[
E_1=\ell^2(\mathbb Z)\widehat\otimes C(\mathbb T)
\widehat\otimes C_1,\qquad
F_1=f(n)\varepsilon.
\]
The first source circle acts by shifting \(n\); the second acts on the coefficient \(C(\mathbb T)\). After the \(C_2\) matrix correspondence, the second cycle is on
\(\ell^2(\mathbb Z)\otimes\mathbb C^2\), with
\[
\psi(g\widehat\otimes\varepsilon^r)=M_g\sigma_1^r,
\qquad F_2=-f(m)\sigma_2,\quad r=0,1.
\tag{8.3}
\]
Here the odd product uses right Clifford dilation of the second cycle. Its coefficient generators are ordered as the second cycle's original generator, followed by the auxiliary generator supplied by the first cycle. We represent these by \(-\sigma_2,\sigma_1\), respectively. Their chirality is
\((-i)(-\sigma_2)\sigma_1=\sigma_3\), agreeing with the chosen grading. This identification is an even unitary conjugate of the usual ordered pair \(\sigma_1,\sigma_2\). It fixes the minus sign in (8.2) and (8.3), and hence the orientation of the product.

These are valid graded cycles by the circle compactness calculation and
\(\sigma_1\sigma_2=-\sigma_2\sigma_1\). Their tensor module is \(H\), and
\(S=F_1\widehat\otimes1=f(n)\sigma_1\).

The operator (8.2) is odd and self-adjoint. Its square defect is
\[
F^2-1=-\frac{1}{1+n^2+m^2}1_2,
\]
a compact diagonal operator: outside any finite lattice set its entries tend uniformly to zero. The two coordinate shifts have compact commutators with \(F\). Indeed the gradient of
\((x,y)\mapsto(x\sigma_1-y\sigma_2)/\sqrt{1+x^2+y^2}\)
has norm bounded by \(C/\sqrt{1+x^2+y^2}\); finite differences in either coordinate tend to zero at infinity. Laurent-polynomial approximation again proves all source commutators compact.

For the connection condition first take a vector
\(x=e_n\widehat\otimes g\widehat\otimes\varepsilon^r\).
Its creation operator is \(J_nM_g\sigma_1^r\), where \(J_n\) embeds the second Fourier space at the fixed first coordinate \(n\). At this fixed coordinate,
\[
\left\|
\frac{n\sigma_1-m\sigma_2}{\sqrt{1+n^2+m^2}}
+f(m)\sigma_2
\right\|\longrightarrow0
\quad(|m|\longrightarrow\infty).
\tag{8.4}
\]
Thus the difference times \(J_n\) is compact. Move \(\sigma_2\) across \(\sigma_1^r\), giving the sign \((-1)^r\), and move \(f(m)\) across \(M_g\), giving the already proved compact circle commutator. These are exactly the two terms of the first creation error. Self-adjointness gives the adjoint condition. Finite sums of these vectors are dense in \(E_1\), so the norm-closed connection condition holds for every vector.

Finally the positivity is particularly simple:
\[
[S,F]_{\mathrm{gr}}
=\frac{2n^2}{\sqrt{1+n^2}\sqrt{1+n^2+m^2}}1_2\geq0.
\tag{8.5}
\]
Sandwiching this positive operator by any \(\phi(a)\) stays positive. All three product axioms hold, and uniqueness proves the assertion. \(\square\)

The untwisted scalar index of (8.2) is zero: only the zero Fourier mode lies in the kernel, with one vector in each parity. This does not make its \(C(\mathbb T^2)\)-homology class zero. A bundle test supplies more information than the scalar test.

The simpler expression \(f(n)\sigma_1-
\sqrt{1-f(n)^2}\,f(m)\sigma_2\) illustrates the hypothesis in Theorem 6.1. Its commutator with the first coordinate shift does not tend to zero when \(n\) is fixed and \(|m|\to\infty\). Hence it cannot simply replace (8.2). A formula for the operator still needs the representation-commutator test.

## 9. Bundles and twisted Dirac operators

Let \(M\) be a closed even-dimensional spin\(^{c}\) manifold with graded spinor bundle \(S_M\), and let \(D_M\) be its self-adjoint Dirac operator with domain \(H^1(M,S_M)\). Let \(V\) be a smooth Hermitian vector bundle with a Hermitian connection. The section module \(\Gamma(V)\) is a finitely generated projective \(C(M)\)-module, concentrated in even degree. Pointwise multiplication gives the cycle
\[
[[V]]=[(\Gamma(V),\lambda,0)]\in KK(C(M),C(M)).
\]
Its scalar pullback is the K-theory class \([V]\in KK(\mathbb C,C(M))\).

We will use the compact-resolvent and self-adjointness assertions for closed-manifold Dirac operators proved in Corollary 4.2 of *Fredholm modules and analytic K-homology*. The analytic index of the bounded transform is the Sobolev Dirac index, by Theorem 5.2 of *The index pairing between K-theory and K-homology*.

**Lemma 9.1 (bounded intertwining and transforms).** Suppose \(D,D'\) are self-adjoint operators with compact resolvents on two Hilbert spaces. Let \(T\) be bounded, map the domain of \(D\) into that of \(D'\), and satisfy
\[
D'T-TD=C
\]
there, for a bounded operator \(C\). Then, for \(b(t)=t/\sqrt{1+t^2}\),
\[
b(D')T-Tb(D)\text{ is compact}.
\tag{9.1}
\]

**Proof.** For \(\alpha=\sqrt{1+s^2}\), the domain assumption gives the resolvent identity
\[
(D'\pm i\alpha)^{-1}T-T(D\pm i\alpha)^{-1}
=-(D'\pm i\alpha)^{-1}C(D\pm i\alpha)^{-1}.
\tag{9.2}
\]
Every right side is compact and has norm at most \(\|C\|/(1+s^2)\). Use
\[
\begin{gathered}
b(D)=\frac2\pi\int_0^\infty D(D^2+1+s^2)^{-1}\,ds,\\
D(D^2+\alpha^2)^{-1}
=\frac12\bigl((D-i\alpha)^{-1}+(D+i\alpha)^{-1}\bigr).
\end{gathered}
\tag{9.3}
\]
The individual truncated integrals converge strongly, as follows from the scalar integral and bounded spectral calculus. Their intertwined difference, by (9.2), converges in norm to a compact operator, since
\(\int_0^\infty(1+s^2)^{-1}ds<\infty\). Its strong limit is the difference in (9.1). \(\square\)

**Theorem 9.2 (twisting is the Kasparov product).** If \(D_V\) is the Dirac operator on \(S_M\otimes V\) for the tensor connection, then
\[
[[V]]\widehat\otimes_{C(M)}[D_M]=[D_V].
\tag{9.4}
\]
Also
\[
[V]\widehat\otimes_{C(M)}[D_M]
=\operatorname{index}D_V^+\in KK(\mathbb C,\mathbb C)=\mathbb Z.
\tag{9.5}
\]

**Proof.** The map
\[
\Gamma(V)\widehat\otimes_{C(M)}L^2(M,S_M)
\longrightarrow L^2(M,S_M\otimes V)
\]
given by pointwise tensoring is an isometry by integration of the fiber inner products. Its range is dense: use finitely many local frames, a partition of unity and density of smooth spinor sections. Hence it is unitary.

For a smooth section \(v\) of \(V\), creation \(T_v\) maps \(H^1\) to \(H^1\), and the tensor connection formula gives
\[
D_VT_v-T_vD_M
=\sum_j c(e_j)\otimes\nabla^V_{e_j}v.
\tag{9.6}
\]
The right side is a smooth bundle homomorphism on a compact manifold, hence bounded on \(L^2\). Lemma 9.1 proves that \(b(D_V)\) is a \(b(D_M)\)-connection for every smooth \(v\). Smooth sections are dense in \(\Gamma(V)\) in the uniform norm; creation is norm-continuous in that norm. Thus the connection property holds for all sections, and self-adjointness gives its second condition.

Ellipticity supplies the remaining cycle conditions for \(b(D_V)\). Positivity is zero because the first operator is zero. Theorem 4.1 proves (9.4).

For (9.5) use the same tensor product and operator, with scalar first representation. It is a product by the same connection proof. The scalar Fredholm calculation of the cycle lesson makes its class the even-kernel dimension minus the odd-kernel dimension. The bounded-transform domain calculation in the index-pairing lesson identifies this with \(\operatorname{index}D_V^+\). This proves the integer formula without an associativity argument or a topological index theorem. \(\square\)

A Grassmann connection gives a second concrete representative. Choose a smooth isometric embedding \(V\subset M\times\mathbb C^N\), with smooth projection \(p\). The operator
\[
p\,b(D_M)^{\oplus N}p
\quad\text{on }pL^2(M,S_M)^{\oplus N}
\tag{9.7}
\]
is a connection and a cycle. Its representation is compact on the first projective module, and its positivity condition is again zero. It has the same class as the twisted Dirac transform by the product uniqueness theorem. Thus the choice of embedding and the choice of connection on \(V\) do not change the class.

## 10. Exercises

**10.1. Exact tensoring.** Suppose a homogeneous \(F_2\) graded commutes exactly with \(\psi(D)\). Prove that \(1\widehat\otimes F_2\) is well-defined on the interior tensor product and is an \(F_2\)-connection.

**10.2. A projective Grassmann connection.** Let \(E_1=pD^N\), for an even projection \(p\) in the graded matrix algebra over \(D\). Write the Grassmann connection explicitly and prove both creation conditions. If the first representation is compact, prove that it is already a product operator with first operator zero.

**10.3. A homomorphism on the right.** Verify the connection, cycle and positivity conditions for
\(F_1\widehat\otimes1\) in the product with \((B,g,0)\). Explain the countability qualification when \(B\) is not \(\sigma\)-unital.

**10.4. Two odd circle classes.** Construct their product as an even cycle using \(C_1\widehat\otimes C_1\cong M_2\). Prove compactness of its source commutators, both connection conditions and positivity, with the signs fixed. Compute its scalar index.

## 11. Solutions

**Solution to 10.1.** On homogeneous elementary tensors set
\[
K(x\widehat\otimes y)=(-1)^{|F_2||x|}
x\widehat\otimes F_2y.
\]
For homogeneous \(d\), applying the formula to \(xd\widehat\otimes y\) gives the sign \((-1)^{|F_2|(|x|+|d|)}\). Applying it to \(x\widehat\otimes\psi(d)y\) gives the same result because
\(F_2\psi(d)=(-1)^{|F_2||d|}\psi(d)F_2\). Thus it respects balancing.

To see boundedness without a formal manipulation of null vectors, extend \(\psi\) to \(D^+\) and use the standard-module operator (1.6). Exact commutation implies that operator commutes with the even stabilized projection \(P\), by first checking finite matrix coefficients and then strong convergence of the matrix truncations on vectors. Its restriction is the formula above, has norm at most \(\|F_2\|\), and has adjoint given by the same formula with \(F_2^*\). Finally
\[
KT_x=(-1)^{|F_2||x|}T_xF_2
\]
exactly; the adjoint-side identity is also exact. Thus both creation errors are zero.

**Solution to 10.2.** Let \(C\) be the signed diagonal amplification (1.6) on the finite free module tensor \(E_2\), and let \(\Pi=p\widehat\otimes1\). Set \(G=\Pi C\Pi\) on \(\Pi(E_2^{\oplus N})\), with the appropriate coordinate parities. For a homogeneous \(x=(x_j)\) in \(pD^N\), \(T_x\) is the column of the represented coordinates, and \(\Pi T_x=T_x\). Hence
\[
GT_x-(-1)^{|F_2||x|}T_xF_2
=\Pi\bigl(CT_x-(-1)^{|F_2||x|}T_xF_2\bigr).
\]
Its entries are compact commutators of \(F_2\) with \(\psi(x_j)\). This is a finite compact column. Taking adjoints proves the second condition when \(F_2\) is self-adjoint; in general apply the same finite row computation using the second connection condition for \(C\).

For a compact first representation, every \(\phi(a)\) lies in the image of \(\mathcal K(pD^N)\). The defect \(G^2-1\) is a \(0\)-connection, so its product with that image is compact. Lemma 1.1 gives the compact representation commutators; the adjoint defect is handled by adjoints or by choosing self-adjoint \(G\). The first operator is zero, making the positivity sandwich zero. Thus this connection is a product without an additional cutoff partition.

**Solution to 10.3.** On \(E=E_1\widehat\otimes_g B\), the creation operator from \(B\) has
\(T_x^*T_x=g(\langle x,x\rangle)\in\mathcal K(B)\). The \(T^*T\) compactness test makes \(T_x\) compact. Therefore \(ST_x\) and \(T_x^*S\) are compact for \(S=F_1\widehat\otimes1\), proving the \(0\)-connection condition. Tensoring a compact rank-one operator on \(E_1\) gives \(T_xT_z^*\), so all three input defects descend to compact defects. With normalized self-adjoint \(F_1\), the positivity expression is \(2\phi(a)S^2\phi(a)^*\), positive already before quotienting.

The full module \(B\) is countably generated exactly when it is \(\sigma\)-unital. If this fails and \(D\) is separable, replace it by \(B_g=\overline{g(D)B}\), as in Section 5. On this module
\(g(\langle x,x\rangle)\) still acts compactly, and the approximate identity of \(D\) makes it countably generated. The tensor product and resulting pushforward class agree with the usual coefficient tensor construction.

**Solution to 10.4.** Use the Pauli matrices in Section 8 as the two odd Clifford generators and \(\sigma_3\) as the grading. The tensor module is
\(\ell^2(\mathbb Z^2)\otimes\mathbb C^2\), with operator (8.2). Its square is \((n^2+m^2)/(1+n^2+m^2)\), so the defect tends to zero outside finite lattice sets. Each source coordinate shift has a commutator whose entries are finite differences of the coefficient vector in (8.2), bounded by \(C/\sqrt{1+n^2+m^2}\) at infinity. They are compact; uniform Laurent-polynomial approximation handles all source functions.

For the dense creation vectors \(e_n\widehat\otimes g\widehat\otimes\varepsilon^r\), the operators are \(J_nM_g\sigma_1^r\). Equation (8.4) supplies the compact fixed-coordinate error, the original circle commutator supplies the compact error from \(M_g\), and
\(\sigma_2\sigma_1^r=(-1)^r\sigma_1^r\sigma_2\) supplies exactly the creation sign. Taking adjoints gives the second condition. Norm approximation handles arbitrary creation vectors. The positivity bracket is (8.5), positive at every lattice point. The zero mode has one even and one odd vector, while no other mode has a kernel. Hence the scalar index is \(1-1=0\). This completes every product axiom and the scalar calculation.

## What this lesson does not prove

The product's associativity, its naturality for general changes of the intermediate algebra, graded symmetry of external products and the comparison \(KK_h=KK_{\mathrm{oh}}\) are theorems of *Homotopy, associativity, the index pairing and KK-equivalence*. The present construction and examples do not assume them.

The elementary module calculus uses the programme's Hilbert-module prerequisites: *Tensor products of Hilbert modules and C\*-correspondences* in *Hilbert C\*-modules and Morita equivalence* gives positivity and completion of the interior tensor product; [Lesson 05, Lemma 2.0](KT-KK-05.html#lemma-2-0-compact-module-operators-and-their-multipliers) proves \(\mathcal L(E)=M(\mathcal K(E))\) and the equivalence of countable generation with \(\sigma\)-unitality of \(\mathcal K(E)\). Graded stabilization and the compact-left tensor rules also have complete proofs in the preceding graded lesson of this course. The closed-manifold analytic input is precisely Corollary 4.2 of the Fredholm-module lesson and Theorem 5.2 of the index-pairing lesson, both already proved there.

No characteristic-class index formula, Bott equivalence, Thom isomorphism or universal coefficient theorem is used here.

## References and source credit

- B. Blackadar, [*K-Theory for Operator Algebras*, author-posted corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf). The [author identifies this freely downloadable version](https://www.bruceblackadar.com/mathpubs.html) as a slightly corrected second edition. The source retains its author copyright and the usage terms stated on that page. Sections 18.3–18.4, printed pp. 169–175, for connections, existence, uniqueness and homomorphism cycles. The required proofs and all exercise solutions are given in this lesson and its exact preceding programme prerequisites.
