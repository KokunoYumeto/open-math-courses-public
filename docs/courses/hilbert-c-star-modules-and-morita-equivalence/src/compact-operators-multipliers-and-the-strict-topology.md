# Compact operators, multipliers and the strict topology

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An identity operator can be compact on a Hilbert module even when the module is an infinite-dimensional Banach space. For example, on a unital C*-algebra regarded as a module over itself, the identity is a single rank-one module operator. This observation changes the question we ask: which operators are built from the module's inner product, and which operators act as multipliers of that collection?

We answer both questions. We compute compact operators on the basic modules, prove that every adjointable operator is a multiplier of the compact operators, and describe the topology in which compact operators approximate all adjointable operators. We also explain exactly what compactness says about Hilbert-space fibres.

The prerequisites are Adjointable operators and the basic multiplier terminology of *Multipliers and essential extensions*. We assume the Hilbert-module Cauchy–Schwarz inequality, the C*-algebra structure of adjointable operators, and ordinary C*-algebra functional calculus and approximate identities. No fullness, separability, unitality, or countable generation is assumed unless stated. Basic references are [Blackadar 1998], [Blackadar 2006], and [Emerson 2024].

Throughout, \(E\) is a right Hilbert \(A\)-module, the inner product is linear in its second variable, and \(\mathcal L(E)\) denotes its adjointable operators. Write \(\mathbb K=\mathcal K(\ell^2)\) for Hilbert-space compact operators and use the spatial tensor product.

## 1. Operators made from vectors

For \(x,y\in E\), define

\[
\theta_{x,y}(z)=x\langle y,z\rangle.
\]

This is a module map, and Cauchy–Schwarz gives \(\|\theta_{x,y}\|\leq\|x\|\|y\|\). The word “rank” here refers to the module expression: the range lies in \(xA\), which may be infinite-dimensional over \(\mathbb C\).

**Proposition 1.1.** For \(T\in\mathcal L(E)\),

\[
\theta_{x,y}^*=\theta_{y,x},\qquad
T\theta_{x,y}=\theta_{Tx,y},\qquad
\theta_{x,y}T=\theta_{x,T^*y}.
\]

Moreover,

\[
\theta_{x,y}\theta_{u,v}
=\theta_{x\langle y,u\rangle,v},\qquad
\theta_{x,x}\geq0,\qquad
\|\theta_{x,x}\|=\|x\|^2.
\]

*Proof.* For \(z,w\in E\),

\[
\langle\theta_{x,y}z,w\rangle
=\langle y,z\rangle^*\langle x,w\rangle
=\langle z,\theta_{y,x}w\rangle.
\]

The two formulas involving \(T\) follow from module linearity and the adjoint identity. Substituting the definition twice gives the product formula.

For positivity, the map \(R_x:A\to E\), \(a\mapsto xa\), is adjointable, with \(R_x^*z=\langle x,z\rangle\). Thus \(\theta_{x,x}=R_xR_x^*\) is positive; these operators can be viewed in \(\mathcal L(E\oplus A)\). To obtain the lower norm bound, put \(a=\langle x,x\rangle\). If \(x\ne0\),

\[
\|\theta_{x,x}x\|^2=\|\langle xa,xa\rangle\|
=\|a^3\|=\|a\|^3.
\]

Divide by \(\|x\|^2=\|a\|\). The upper bound was already established. The case \(x=0\) is immediate. \(\square\)

Define the **compact module operators** by

\[
\mathcal K(E)=
\overline{\operatorname{span}}\{\theta_{x,y}:x,y\in E\}
\subseteq\mathcal L(E),
\]

where the closure is in operator norm.

**Theorem 1.2.** \(\mathcal K(E)\) is a closed two-sided ideal of \(\mathcal L(E)\), and it is essential: every nonzero closed two-sided ideal of \(\mathcal L(E)\) meets \(\mathcal K(E)\) nontrivially.

*Proof.* Proposition 1.1 makes the finite span a two-sided, involution-stable ideal. Its norm closure is therefore a closed ideal. If \(T\mathcal K(E)=0\), then for every \(x\in E\),

\[
0=T\theta_{x,Tx}=\theta_{Tx,Tx}.
\]

The norm formula implies \(Tx=0\), hence \(T=0\). If an ideal \(J\) had zero intersection with \(\mathcal K(E)\), then \(Tk\in J\cap\mathcal K(E)\) for \(T\in J\), \(k\in\mathcal K(E)\); the preceding argument gives \(J=0\). \(\square\)

Essentiality says that the compact operators detect every adjointable operator. Their action also reaches every vector, a fact we need before constructing multipliers.

**Lemma 1.3.** The linear span \(\mathcal K(E)E\) is dense in \(E\). Every positive contractive approximate identity \((e_\lambda)\) of \(\mathcal K(E)\) satisfies \(e_\lambda x\to x\) for every \(x\in E\).

*Proof.* For \(a=\langle x,x\rangle\) and \(t>0\), form inverses in the unitization of \(A\). The vector

\[
\theta_{x,x}\bigl(x(a+t)^{-1}\bigr)
=xa(a+t)^{-1}
\]

belongs to \(\mathcal K(E)E\). Its difference from \(x\) has squared norm at most

\[
\sup_{s\geq0}s\left(\frac{t}{s+t}\right)^2=\frac t4.
\]

Hence these vectors converge to \(x\). On a vector \(ky\), approximate identity convergence gives \(e_\lambda ky\to ky\). Finite sums are dense, and \(\|e_\lambda\|\leq1\) extends convergence to all vectors. \(\square\)

## 2. Three calculations, including nonunital coefficients

The basic modules are \(A\), \(A^n\), and

\[
H_A=\left\{(a_j)_{j\geq1}:
\sum_j a_j^*a_j\text{ converges in norm}\right\},
\qquad
\langle(a_j),(b_j)\rangle=\sum_j a_j^*b_j.
\]

Finite coordinate truncations approximate every vector of \(H_A\). When \(A\) is nonunital, a coordinate vector with entry \(1\) need not exist; we use vectors whose entries belong to \(A\).

**Theorem 2.1.** There are canonical C*-algebra isomorphisms

\[
\mathcal K(A)\cong A,\qquad
\mathcal K(A^n)\cong M_n(A),\qquad
\mathcal K(H_A)\cong A\otimes\mathbb K.
\]

*Proof.* On \(A\), \(\theta_{a,b}\) is left multiplication by \(ab^*\). Left multiplication \(\lambda_c\) has norm \(\|c\|\): the upper estimate is immediate, and \(cu_\lambda\to c\) for a contractive approximate identity of \(A\) gives the lower estimate. Products \(ab^*\) have dense linear span, since \(cu_\lambda=c(u_\lambda)^*\to c\). Thus left multiplication identifies \(A\) with \(\mathcal K(A)\).

For \(A^n\), matrix multiplication defines a faithful *-homomorphism \(M_n(A)\to\mathcal L(A^n)\). Faithfulness follows by testing vectors supported in a single coordinate and using an approximate identity of \(A\). A faithful C*-homomorphism is isometric. The matrix of \(\theta_{x,y}\) is \((x_i y_j^*)_{ij}\). Conversely, vectors supported in coordinates \(i\) and \(j\) give a matrix with the single entry \(ab^*\) in position \((i,j)\). Density of these products proves the second assertion.

On \(H_A\), let \(V_{ij}(a)\) have only the \(i\)-th output coordinate nonzero, equal to \(az_j\). Its adjoint is \(V_{ji}(a^*)\), and

\[
V_{ij}(a)V_{kl}(b)=\delta_{jk}V_{il}(ab).
\]

Writing \(\delta_i a\) for the vector with entry \(a\) in coordinate \(i\), we have

\[
\theta_{\delta_i a,\delta_j b}=V_{ij}(ab^*).
\]

Thus all \(V_{ij}(a)\) are compact. The finite upper-left matrix algebras \(M_n(A)\) act faithfully, hence isometrically, on \(H_A\). Their increasing norm closure is the spatial stabilization \(A\otimes\mathbb K\): on each finite matrix corner the spatial tensor norm is precisely the C*-norm of \(M_n(A)\).

It remains to show that this closure contains every compact operator. If \(P_n\) truncates to the first \(n\) coordinates, then

\[
\|\theta_{x,y}-\theta_{P_nx,P_ny}\|
\leq\|x-P_nx\|\|y\|
+\|P_nx\|\|y-P_ny\|\longrightarrow0.
\]

The truncated operator lies in a finite matrix corner. This proves the final assertion. \(\square\)

For \(A=\mathbb C\), the last calculation is \(\mathcal K(\ell^2)=\mathbb K\). In contrast, the coordinate truncation \(P_n\) for general \(A\) has entries in \(M(A)\); it need not itself be compact. For example, if \(A\) is nonunital, its nonzero diagonal entries are identity multipliers outside \(A\).

## 3. When a sequence can replace a net

A module is **countably generated** if it is the closed linear span of \(x_jA\) for some countable family \((x_j)\). A C*-algebra is **\(\sigma\)-unital** if it has a sequential positive contractive approximate identity.

**Theorem 3.1.** \(E\) is countably generated if and only if \(\mathcal K(E)\) is \(\sigma\)-unital.

*Proof.* Suppose \((x_j)\) generates \(E\). Rescale each nonzero generator so that \(\|x_j\|\leq1\), without changing the generated module, and put

\[
h=\sum_{j\geq1}2^{-j}\theta_{x_j,x_j}\in\mathcal K(E),
\qquad e_m=h(h+m^{-1})^{-1}.
\]

The series converges in norm. Functional calculus gives positive contractions \(e_m\in\mathcal K(E)\). With \(r_m=1-e_m\), the inequality \(h\geq2^{-j}\theta_{x_j,x_j}\) implies

\[
\|r_mx_j\|^2
=\|r_m\theta_{x_j,x_j}r_m\|
\leq2^j\|r_mhr_m\|
\leq\frac{2^j}{4m}.
\]

The last estimate uses \(\sup_{s\geq0}s/(1+ms)^2=1/(4m)\). Hence \(e_mx\to x\) on all generators, their \(A\)-linear span, and then all of \(E\). Proposition 1.1 now gives

\[
e_m\theta_{x,y}=\theta_{e_mx,y}\to\theta_{x,y},
\qquad
\theta_{x,y}e_m=\theta_{x,e_my}\to\theta_{x,y}.
\]

Density and contractivity make \((e_m)\) an approximate identity for \(\mathcal K(E)\).

Conversely, let \((e_m)\) be such an approximate identity. Choose finite sums

\[
f_m=\sum_{j=1}^{N_m}\theta_{v_{mj},w_{mj}},
\qquad\|f_m-e_m\|<m^{-1}.
\]

Lemma 1.3 gives \(f_mx\to x\) for every \(x\). Each \(f_mx\) belongs to the module span of the finitely many \(v_{mj}\). The countable union of these vectors generates \(E\). The zero module also satisfies both assertions. \(\square\)

This proof does not require \(A\) to be \(\sigma\)-unital. Applied to \(E=A\), it shows that \(A\) is countably generated over itself exactly when \(A\) is \(\sigma\)-unital. Merely writing a module as \(A\) or \(A^n\) does not provide finitely many generators when the coefficient algebra lacks a unit.

## 4. Recovering all adjointable operators

For a C*-algebra \(B\), a multiplier can be represented by a pair of bounded linear maps \((L,R):B\to B\), with

\[
L(ab)=L(a)b,\quad R(ab)=aR(b),\quad
aL(b)=R(a)b.
\]

Think of \(L(b)=mb\) and \(R(b)=bm\). With ordinary composition of maps, the product and involution are

\[
(L_1,R_1)(L_2,R_2)=(L_1\circ L_2,R_2\circ R_1),
\]

\[
(L,R)^*=(L^{\#},R^{\#}),\quad
L^{\#}(b)=R(b^*)^*,\quad R^{\#}(b)=L(b^*)^*.
\]

**Lemma (The double-centralizer algebra).** These pairs form a unital C*-algebra \(M(B)\), with \(\|(L,R)\|=\|L\|=\|R\|\). The algebra \(B\) embeds isometrically as an essential ideal. Every C*-algebra extension containing \(B\) as an ideal has a unique homomorphism into \(M(B)\) restricting to identity on \(B\); its kernel is the annihilator of \(B\).

*Proof.* The identities defining a pair are closed in the product of the two bounded-map spaces, so the pairs are complete. The displayed product and involution preserve the identities and satisfy the *-algebra laws by substitution; the identity pair is \((\operatorname{id},\operatorname{id})\). For a positive contractive approximate identity \((e_\lambda)\), compatibility gives
\[
R(a)e_\lambda=aL(e_\lambda),\qquad
e_\lambda L(a)=R(e_\lambda)a.
\]
Taking norm limits bounds \(\|R\|\leq\|L\|\) and conversely. The involution therefore preserves this common norm. Its compatibility also gives
\[
L(b)^*c=b^*L^{\#}(c),\qquad
L(b)^*L(b)=b^*L^{\#}L(b).
\]
Hence \(\|L\|^2\leq\|L^{\#}L\|\); composition gives the reverse bound. This proves the C*-identity. Completeness of the bounded-map spaces is proved in the opening lemma of *Adjointable operators*, Section 2.

Send \(b\in B\) to left and right multiplication by \(b\). Approximate identities show that the operator norms equal \(\|b\|\). Multiplying a pair by this embedded element gives the embedded element \(L(b)\), and multiplication on the other side gives \(R(b)\), by the three compatibility identities. Thus \(B\) is an ideal. A pair annihilating this ideal has \(L=0\), hence \(R=0\), proving essentiality.

If \(B\) is an ideal in \(D\), send \(d\) to \((b\mapsto db,b\mapsto bd)\). These maps are bounded, form a pair, and preserve products and adjoints. The kernel is exactly \(\{d:dB=Bd=0\}\). Any homomorphism fixing \(B\) must have these same products with every embedded \(b\), so its two centralizers are forced and it equals this one. In particular an essential extension embeds faithfully. For \(B=0\), the algebra of pairs is zero and the same assertions have their evident zero-algebra interpretation. ∎

We next identify this algebra with all adjointable operators on a module whose compact algebra is \(B\).

**Theorem 4.1.** The map

\[
\Phi:\mathcal L(E)\longrightarrow M(\mathcal K(E)),
\qquad T\longmapsto(k\mapsto Tk,\ k\mapsto kT)
\]

is a canonical C*-algebra isomorphism.

*Proof.* Set \(B=\mathcal K(E)\). The ideal property shows that both maps take values in \(B\), and their multiplier identities follow from associativity. Their product and involution agree with those in \(\mathcal L(E)\). Essentiality proves injectivity.

For surjectivity, take \(m=(L,R)\in M(B)\). On the dense linear span \(D=BE\), try to define

\[
T_m\left(\sum_{i=1}^r b_ix_i\right)
=\sum_{i=1}^r L(b_i)x_i.
\]

We must show that the formula is independent of the chosen sum and bounded. Let \((e_\lambda)\) be a positive contractive approximate identity of \(B\). Since \(L\) is bounded and \(e_\lambda b_i\to b_i\),

\[
\sum_i L(b_i)x_i
=\lim_\lambda L(e_\lambda)\left(\sum_i b_ix_i\right).
\]

Here \(L(e_\lambda)\in B\subseteq\mathcal L(E)\) has norm at most \(\|L\|\). Therefore

\[
\left\|\sum_i L(b_i)x_i\right\|
\leq\|L\|\left\|\sum_i b_ix_i\right\|.
\]

This proves well-definedness and yields a bounded \(A\)-linear extension to \(E\).

Apply the same construction to \(m^*\), obtaining \(T_{m^*}\). Multiplier compatibility, followed by taking adjoints, gives

\[
L(b)^*c=b^*L^{\#}(c).
\]

Consequently, for \(bx,cy\in D\),

\[
\langle T_m(bx),cy\rangle
=\langle x,L(b)^*cy\rangle
=\langle bx,T_{m^*}(cy)\rangle.
\]

Linearity and continuity give \(T_m^*=T_{m^*}\) on all of \(E\). Finally, the construction gives \(T_mb=L(b)\). On a dense vector \(cx\),

\[
bT_m(cx)=bL(c)x=R(b)cx,
\]

so \(bT_m=R(b)\). Thus \(\Phi(T_m)=m\). A bijective C*-homomorphism is isometric, completing the proof. \(\square\)

**Corollary 4.2.** Canonically,

\[
M(A)=\mathcal L(A),\qquad
\mathcal L(A^n)=M_n(M(A)),\qquad
M(A\otimes\mathbb K)=\mathcal L(H_A).
\]

*Proof.* Apply Theorem 4.1 to the calculations of Theorem 2.1. For the middle equality, the coordinate inclusions and projections of \(A^n\) identify its adjointable operators with matrices of operators in \(\mathcal L(A)\), including the adjoint matrix. \(\square\)

In particular, the action of \(\mathcal K(\ell^2)\) on \(\ell^2\) realizes its multiplier algebra as \(\mathcal B(\ell^2)\). More generally, for a faithful nondegenerate representation \(\rho:B\to\mathcal B(H)\), Exercise 5 identifies \(M(B)\) with the idealizer

\[
\{S\in\mathcal B(H):S\rho(B)\subseteq\rho(B),\quad
\rho(B)S\subseteq\rho(B)\}.
\]

Indeed, an idealizing \(S\) defines \(L,R\) through the isometric map \(\rho\); Exercise 5 implements that pair, and nondegeneracy forces the implementing operator to equal \(S\). Thus the double-centralizer, concrete, and module descriptions have the same multiplication and the same action on the original algebra.

**Corollary 4.3.** If \(p\) is a projection in \(M(B)\), then \(M(pBp)\cong pM(B)p\).

*Proof.* Regard \(B\) as a Hilbert module over itself. The complemented submodule \(pB\) has compact algebra \(pBp\): its rank-one operators are left multiplications by \(pab^*p\), whose span is dense in \(pBp\). Its adjointable operators identify with \(p\mathcal L(B)p\), by extending them as zero on \((1-p)B\). Apply Theorem 4.1 and Corollary 4.2. \(\square\)

## 5. Convergence tested against compact operators

The **strict topology** on \(\mathcal L(E)=M(\mathcal K(E))\) is generated by

\[
T\longmapsto\|Tk\|,\qquad T\longmapsto\|kT\|,
\qquad k\in\mathcal K(E).
\]

Thus \(T_i\to T\) strictly means norm convergence after multiplying on either side by each fixed compact module operator. Essentiality makes this topology Hausdorff.

**Proposition 5.1.** On norm-bounded subsets of \(\mathcal L(E)\), strict convergence is equivalent to

\[
T_ix\to Tx,\qquad T_i^*x\to T^*x
\quad\text{for every }x\in E.
\]

Every positive contractive approximate identity of \(\mathcal K(E)\) converges strictly to the identity of \(\mathcal L(E)\), and \(\mathcal K(E)\) is strictly dense in \(\mathcal L(E)\).

*Proof.* For a uniformly bounded net with the displayed vector convergence,

\[
(T_i-T)\theta_{x,y}=\theta_{(T_i-T)x,y},\qquad
\theta_{x,y}(T_i-T)=\theta_{x,(T_i^*-T^*)y}
\]

converge in norm to zero. Approximation by finite sums, using the uniform bound, proves strict convergence against every compact.

Conversely, strict convergence gives convergence on every vector \(ky\). Lemma 1.3 and the uniform operator bound extend this to every vector. The adjoint net is strictly convergent because taking adjoints interchanges the two seminorm families; the same argument applies to it.

For an approximate identity \((e_\lambda)\), strict convergence to \(1\) is its defining two-sided approximation property. For any \(T\), the operators \(Te_\lambda\) are compact, and

\[
(Te_\lambda-T)k=T(e_\lambda k-k),\qquad
k(Te_\lambda-T)=(kT)e_\lambda-kT
\]

converge in norm to zero. \(\square\)

For infinite-dimensional \(\ell^2\), its finite-coordinate projections satisfy \(P_n\to1\) strictly but \(\|1-P_n\|=1\). This is the topology in which an infinite system is recovered from finite matrix pieces.

**Theorem 5.2.** \(M(B)\) is complete in the strict topology for every C*-algebra \(B\). Consequently, \(\mathcal L(E)\) is strictly complete and is the strict completion of \(\mathcal K(E)\).

*Proof.* Let \((m_i)\) be a strict Cauchy net. For every \(b\in B\), both \(m_ib\) and \(bm_i\) are norm-Cauchy in \(B\). Define

\[
L(b)=\lim_i m_ib,\qquad R(b)=\lim_i bm_i.
\]

Passing to limits gives linearity and all three double-centralizer identities. We still need boundedness; a general Cauchy net need not come with a common operator-norm bound.

Suppose \(b_n\to0\) and \(L(b_n)\to c\) in norm. For every \(a\in B\),

\[
ac=\lim_n aL(b_n)=\lim_n R(a)b_n=0.
\]

Taking \(a=c^*\) gives \(c=0\). This proves the graph of \(L\) is closed, hence \(L\) is bounded by the closed graph theorem. For \(R\), if \(b_n\to0\) and \(R(b_n)\to c\), then \(ca=\lim_n b_nL(a)=0\) for every \(a\), again implying \(c=0\). Thus \(R\) is bounded too. The pair is a multiplier \(m\), and the defining limits say precisely that \(m_i\to m\) strictly. The last conclusion follows from Proposition 5.1 and Theorem 4.1. \(\square\)

Involution is strictly continuous. Multiplication is separately strictly continuous and jointly strictly continuous on bounded sets. For example, if bounded nets satisfy \(S_i\to S\), \(T_i\to T\) strictly, then

\[
\|(S_iT_i-ST)k\|
\leq\|S_i\|\|(T_i-T)k\|+\|(S_i-S)Tk\|\to0.
\]

On the other side use
\(k(S_iT_i-ST)=k(S_i-S)T_i+kS(T_i-T)\).
The separate continuity assertions follow by holding one factor fixed.

**Example 5.3: a continuous unitary group.** A representation \(g\mapsto U_g\) of a topological group by unitaries in \(\mathcal L(E)\) is strictly continuous exactly when \(g\mapsto U_gx\) is norm-continuous for every \(x\in E\). Indeed, \(U_g^*=U_{g^{-1}}\), and unitaries have a common norm bound, so Proposition 5.1 applies.

On \(\ell^2\), define \(U_te_n=e^{int}e_n\), \(t\in\mathbb R\). For a fixed vector, its finite-coordinate part varies continuously and its tail contributes at most twice the tail norm. This proves strong, hence strict, continuity. But \(\|(U_{\pi/n}-1)e_n\|=2\), so the group is not norm-continuous at zero. For each \(k\in\mathbb K\), the induced conjugation \(t\mapsto U_tkU_t^*\) is norm-continuous, by splitting its difference into terms using \(U_tk-U_sk\) and \(kU_t^*-kU_s^*\). This is the continuity needed for actions on compact operators in crossed-product constructions.

## 6. Fields, bundles, and the meaning of a fibre

First consider the commutative coefficient algebra. For a locally compact Hausdorff space \(X\),

\[
M(C_0(X))=C_b(X).
\]

Here is a direct module proof. If \(T\in\mathcal L(C_0(X))\), choose a function \(u\) of norm one that equals \(1\) near a given point \(t\), and set \(f(t)=(Tu)(t)\). The identity \(T(uv)=(Tu)v=(Tv)u\) makes this independent of \(u\). Locally \(f=Tu\), so it is continuous, and \(|f(t)|\leq\|T\|\). The same identity gives \(Tg=fg\) for every \(g\in C_0(X)\). Conversely, multiplication by a bounded continuous \(f\) is adjointable, with adjoint multiplication by \(\overline f\).

On bounded subsets of \(C_b(X)\), the strict topology is uniform convergence on compact subsets. To see the forward implication, test against a cutoff equal to \(1\) on a given compact set. For the reverse implication, split a test function \(a\in C_0(X)\) into a compact region and a tail where \(|a|\) is small; the common bound controls the tail. Boundedness matters: on \(X=\mathbb N\), the functions \(f_n=n\,1_{\{n\}}\) converge to zero uniformly on every compact set, whereas

\[
\|f_na\|=1\quad\text{for }a(j)=1/j.
\]

Thus they do not converge strictly.

**Proposition 6.1: a vector bundle.** If \(V\to X\) is a finite-rank Hermitian vector bundle over a locally compact Hausdorff space, and \(E=\Gamma_0(V)\), then

\[
\mathcal K(E)\cong\Gamma_0(\operatorname{End}(V)),
\]

with fibrewise operator norm and composition.

*Proof.* A rank-one operator acts at \(t\) by
\(v\mapsto x(t)\langle y(t),v\rangle\). This is a continuous endomorphism section vanishing at infinity, since its norm is at most \(\|x(t)\|\|y(t)\|\). Multiplication by an endomorphism section \(F\) has operator norm \(\sup_t\|F(t)\|\): the upper bound is immediate, and a local unit vector extended using a cutoff tests the lower bound at any point.

Conversely, approximate a vanishing section \(F\) uniformly by compactly supported sections. A finite partition subordinate to trivializing neighborhoods on its compact support reduces to one section supported compactly inside one chart. In a local orthonormal frame, write its entries as \(f_{ij}\). Choose a scalar cutoff \(\chi\) equal to \(1\) on that support and supported in the chart. The sections \(x=f_{ij}e_i\) and \(y=\chi e_j\), extended as zero, are global elements of \(E\), and \(\theta_{x,y}\) gives the \((i,j)\) entry. Summing over the entries proves density of finite-rank module operators. \(\square\)

**Example 6.2: operator fields on a compact base.** Let \(X\) be compact Hausdorff and \(A=C(X)\). Then

\[
H_A\cong C(X,\ell^2),\qquad
\mathcal K(H_A)\cong C(X,\mathbb K).
\]

For the first equality, square summability in \(C(X)\) means uniform convergence of the coordinate tails. Conversely, a continuous \(\ell^2\)-valued function has compact image, on which finite-coordinate truncations converge uniformly. For the second equality, finite matrix fields act as in Theorem 2.1. Every continuous compact-operator field is uniformly approximated by its finite-coordinate compressions: pointwise approximation is uniform on its compact image in \(\mathbb K\). These compressions are finite matrix fields.

In this description, \(\mathcal L(H_A)\) consists precisely of bounded fields

\[
t\longmapsto B(t)\in\mathcal B(\ell^2)
\]

such that \(B(t)\xi\) and \(B(t)^*\xi\) are continuous for every \(\xi\in\ell^2\). Equivalently, these are bounded fields continuous for the strict topology of \(M(\mathbb K)\).

To verify the assertion, an adjointable module operator induces bounded operators at every point, using the inequality
\(\langle Tz,Tz\rangle\leq\|T\|^2\langle z,z\rangle\).
Apply it to the constant sections \(\xi\) and to \(T^*\) to get the two continuity conditions. Conversely, such a bounded field sends continuous sections to continuous sections: near \(t_0\), split
\(B(t)z(t)-B(t_0)z(t_0)\)
into \(B(t)(z(t)-z(t_0))\) and
\((B(t)-B(t_0))z(t_0)\).
The adjoint field does the same and satisfies the pointwise adjoint identity. This constructs the adjointable operator, of norm \(\sup_t\|B(t)\|\). Proposition 5.1 on \(\ell^2\) proves the strict-topology formulation.

Fibrewise compactness alone still does not characterize \(\mathcal K(H_A)\). Take
\(X=\{0\}\cup\{1/n:n\geq1\}\), and let \(B(0)=0\), \(B(1/n)=p_n\), the projection onto \(\mathbb Ce_n\). For each fixed \(\xi\), \(\|p_n\xi\|\to0\), so both field conditions hold. Every \(B(t)\) is compact. But \(\|B(1/n)\|=1\) prevents norm continuity at zero, so the module operator is not compact.

**Proposition 6.3: genuine point fibres.** Let \(E\) be a Hilbert \(C_0(X)\)-module. Its Hilbert-space fibre \(E_t\) is the completion of \(E\) after dividing out vectors with \(\langle x,x\rangle(t)=0\). Every \(k\in\mathcal K(E)\) induces a compact Hilbert-space operator \(k_t\) on \(E_t\).

*Proof.* The operator inequality used above gives
\(\|(Tx)_t\|\leq\|T\|\|x_t\|\), so an adjointable \(T\) descends and extends with norm at most \(\|T\|\). Rank-one module operators descend to

\[
(\theta_{x,y})_t=\theta_{x_t,y_t},
\]

which has Hilbert-space rank at most one. Norm approximation by finite sums passes to fibres contractively, proving compactness. \(\square\)

There are two other comparisons to keep separate. First, a compact module operator need not be compact as an operator on the module's underlying Banach space. On \(E=C([0,1])\), the identity is \(\theta_{1,1}\), but disjoint continuous bumps of norm one show that its unit ball is not relatively compact.

Second, a representation of a noncommutative coefficient algebra can produce a Hilbert space with an additional infinite-dimensional coefficient factor. For instance, take \(A=\mathcal B(\ell^2)\), \(E=A\), and represent \(A\) on \(\ell^2\) by its defining action. The Hilbert-space completion of balanced vectors \(a\otimes\xi\) identifies with \(\ell^2\) through \(a\otimes\xi\mapsto a\xi\): this map preserves the inner product \(\langle\xi,a^*b\eta\rangle\) and is onto because \(A\) is unital. The module compact \(\theta_{1,1}\) induces the identity on \(\ell^2\), which is not Hilbert-space compact. Thus compactness after a general coefficient representation differs from compactness at a \(C_0(X)\) point. Geometric representations attached to leaves must be interpreted through their actual coefficient algebra; point-fibre terminology cannot be transferred without that distinction.

## 7. Exercises and complete solutions

**Exercise 1 (basic).** Verify \(\theta_{x,y}^*=\theta_{y,x}\) and \(T\theta_{x,y}=\theta_{Tx,y}\).

*Solution.* For \(z,w\in E\),

\[
\langle x\langle y,z\rangle,w\rangle
=\langle y,z\rangle^*\langle x,w\rangle
=\langle z,y\langle x,w\rangle\rangle.
\]

This proves the adjoint identity. Module linearity gives
\(T(x\langle y,z\rangle)=(Tx)\langle y,z\rangle\), which is the second identity.

**Exercise 2 (basic).** Prove \(\mathcal K(A)\cong A\) without assuming that \(A\) is unital.

*Solution.* The map \(c\mapsto\lambda_c\) is an isometric *-homomorphism, since a contractive approximate identity satisfies \(cu_\lambda\to c\). Rank-one operators are \(\lambda_{ab^*}\). The image of the isometric map is closed, and the span of \(ab^*\) is dense in \(A\), because \(cu_\lambda\) is such a product. Therefore its image is exactly \(\mathcal K(A)\).

**Exercise 3 (intermediate).** Use matrix units to prove \(\mathcal K(H_A)\cong A\otimes\mathbb K\).

*Solution.* Let \(e_{ij}\) be the scalar matrix units. Send \(a\otimes e_{ij}\) to \(V_{ij}(a)\). The relations
\(V_{ij}(a)V_{kl}(b)=\delta_{jk}V_{il}(ab)\)
and \(V_{ij}(a)^*=V_{ji}(a^*)\) make this a *-homomorphism on finite matrix corners. Each corner is faithful by testing single-coordinate vectors, hence isometric. Its extension from the increasing union therefore embeds \(A\otimes\mathbb K\) isometrically. Its image is contained in \(\mathcal K(H_A)\), since \(\theta_{\delta_i b,\delta_j c}=V_{ij}(bc^*)\) and products \(bc^*\) span a dense subspace of \(A\). Conversely, truncate the two vectors in every \(\theta_{x,y}\); the estimate in Theorem 2.1 shows norm convergence to finite matrix operators. The image is closed and contains all compact operators.

**Exercise 4 (intermediate).** The identity of \(C_0(\mathbb N)\), viewed as a Hilbert module over itself, is a multiplier but is not compact. Prove both assertions, and examine its point fibres.

*Solution.* The identity is adjointable and belongs to \(M(C_0(\mathbb N))=\ell^\infty(\mathbb N)\) as the constant sequence \(1\). By Exercise 2, compact module operators correspond to \(c_0(\mathbb N)\), which does not contain this sequence. Each point fibre is \(\mathbb C\), where the induced identity is rank one and compact. The missing condition is vanishing at infinity, not pointwise compactness.

**Exercise 5 (advanced).** Let \(\pi:A\to\mathcal L(E)\) be a nondegenerate *-homomorphism, meaning that the linear span \(\pi(A)E\) is dense. Prove that it extends uniquely to a unital *-homomorphism
\(\widetilde\pi:M(A)\to\mathcal L(E)\), strictly continuous on bounded sets. Deduce the corresponding extension from any C*-algebra containing \(A\) as a closed ideal.

*Solution.* Let \((u_\lambda)\) be a positive contractive approximate identity of \(A\). On \(\pi(a)x\),
\(\pi(u_\lambda)\pi(a)x\to\pi(a)x\).
Density and contractivity give \(\pi(u_\lambda)x\to x\) on all of \(E\).

For \(m\in M(A)\), consider \(\pi(mu_\lambda)\), whose norms are at most \(\|m\|\). On a dense vector \(v=\sum_i\pi(a_i)x_i\),

\[
\pi(mu_\lambda)v
\longrightarrow\sum_i\pi(ma_i)x_i.
\]

The common bound makes this limit independent of the expression for \(v\) and defines a bounded module map \(T_m\) on \(E\). Applying the construction to \(m^*\) produces its adjoint. In fact,

\[
\langle \pi(ma)x,\pi(b)y\rangle
=\langle x,\pi(a^*m^*b)y\rangle
=\langle\pi(a)x,T_{m^*}\pi(b)y\rangle.
\]

Thus \(T_m\in\mathcal L(E)\), with \(T_m^*=T_{m^*}\) and
\(T_m\pi(a)x=\pi(ma)x\).
On these same dense vectors, \(T_mT_n=T_{mn}\), linearity holds, \(T_1=1\), and \(T_a=\pi(a)\). This proves the unital *-homomorphism assertion. If another extension existed, its value at \(m\) would have the identical action on every \(\pi(a)x\); density proves uniqueness.

Suppose \(m_i\to m\) strictly and \(\sup_i\|m_i\|<\infty\). Then

\[
\|(T_{m_i}-T_m)\pi(a)x\|
\leq\|(m_i-m)a\|\|x\|\to0.
\]

Uniform boundedness of these operators extends convergence to all vectors. Since \(m_i^*\to m^*\) strictly, the adjoints converge on all vectors too. Proposition 5.1 proves strict convergence in \(\mathcal L(E)\).

Finally, if \(A\) is a closed ideal in \(D\), each \(d\in D\) gives the multiplier \((a\mapsto da,a\mapsto ad)\). Compose this homomorphism with \(\widetilde\pi\). Uniqueness follows on \(\pi(A)E\) just as above. If \(\pi\) is faithful, the extension has kernel

\[
A^\perp=\{d\in D:dA=Ad=0\}.
\]

Indeed, a zero image forces \(\pi(da)=\pi(ad)=0\) for all \(a\); faithfulness gives both annihilation conditions. Conversely, these conditions make its action zero on the dense subspace. This also explains why nondegeneracy is needed: the dense subspace is what determines the action of each multiplier.

## What this lesson does not prove

The norm Cauchy–Schwarz inequality is *Hilbert C*-modules*, Theorem 2.1. Automatic boundedness, the adjointable C*-algebra and its order estimate are *Adjointable operators*, Theorems 2.1–2.2 and Section 3. The complete-graph and bounded-map arguments are the opening lemma of that lesson's Section 2. The double-centralizer C*-algebra and its maximal essential-extension property are proved in the opening lemma of Section 4 here; Exercise 5 extends nondegenerate module representations.

Functional calculus, positive contractive approximate identities and isometry of injective C*-homomorphisms are the exact foundational programme results identified in the first Hilbert-module lesson. Blackadar's II.7.3 and the other references below credit the classical multiplier theory. Foliation algebras, general continuous-field theory and crossed products require their own geometric hypotheses and are not used to prove these operator results.

## References

- **[Blackadar 1998]** B. Blackadar, *K-Theory for Operator Algebras*, second edition, MSRI Publications 5, Cambridge University Press, 1998. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf). Multiplier algebras and compact module operators are treated in §§12.1, 13.2, and 13.4.
- **[Blackadar 2006]** B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Encyclopaedia of Mathematical Sciences 122, Springer, 2006; [author's revised text, 2017](https://www.bruceblackadar.com/Mathematics/Cycr.pdf). Relevant discussions are II.7.2 and II.7.3.
- **[Emerson 2024]** H. Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser Advanced Texts, 2024. See §§5.3 and 5.5 for multiplier and module viewpoints.
