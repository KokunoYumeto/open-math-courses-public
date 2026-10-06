# Kasparov modules and the groups KK(A, B)

*Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A Kasparov module replaces the Hilbert space of a Fredholm module by a Hilbert module over a second algebra. Its operator is an odd involution up to defects that become compact after the first algebra acts. This gives a bivariant group: the first algebra describes the represented geometry, and the second algebra contains the coefficient-valued index.

The preceding lesson proves the tensor constructions in Lemmas 3.0a and 6.0a, the interior grading in Proposition 6.1, and graded stabilization in Theorem 6.2. Its exact earlier programme proofs supply the C\*-algebra and adjointable-operator foundations. The present construction is based on the actual free Blackadar author text and Rosenberg author notes listed below, and its group and countability arguments are proved here. All commutators below are graded. In particular an odd \(F\) satisfies
\[
\begin{gathered}
{}[F,\phi(a)]_{\mathrm{gr}}\\
=F\phi(a)-(-1)^{|a|}\phi(a)F
\end{gathered}
\tag{0.1}
\]
for homogeneous \(a\). The Hilbert-space Fredholm and polar facts are proved in the earlier Lesson 1, Lemma 1.1; Lemma 1.2 supplies the index and compact-perturbation invariance. The compression convention is the one in *Fredholm modules and analytic K-homology*. We prove below the additional index invariance required for homotopies over varying Hilbert modules.

Until a hypothesis is explicitly added, \(A,B\) may be arbitrary graded complex C\*-algebras. We use countably generated modules in the definition. Consequently a canonical cycle on the module \(B\) itself requires \(B\) to be \(\sigma\)-unital; this condition matters for homomorphism and identity classes.

## 1. Cycles and locally compact defects

A cycle for the pair \((A,B)\), also called a **Kasparov module**, consists of a triple \((E,\phi,F)\), where \(E\) is a countably generated graded Hilbert \(B\)-module, \(\phi:A\to\mathcal L(E)\) is graded, and \(F\in\mathcal L(E)\) is odd, such that for every homogeneous \(a\in A\),
\[
\begin{aligned}
\left[F,\phi(a)\right]_{\mathrm{gr}}&\in\mathcal K(E),\\
(F^2-1)\phi(a)&\in\mathcal K(E),\\
(F-F^*)\phi(a)&\in\mathcal K(E).
\end{aligned}
\tag{1.1}
\]
Checking homogeneous entries suffices by linearity. It is **degenerate** if all three expressions are zero. No nondegeneracy of \(\phi\) is required. In particular \((E,0,F)\) is degenerate for every odd adjointable \(F\).

The word compact means a norm limit of module rank-one operators. It does not mean finite-dimensional range. Nor does (1.1) require \(F^2-1\) to be globally compact when \(A\) is nonunital.

For a fixed graded representation, let \(\mathcal D_\phi^r\) be the degree-\(r\) operators \(T\) with
\([T,\phi(a)]_{\mathrm{gr}}\in\mathcal K(E)\)
for all homogeneous \(a\), and put
\[
\begin{gathered}
\mathcal D_\phi=\mathcal D_\phi^0+\mathcal D_\phi^1,\\
\mathcal J_\phi=\{T\in\mathcal D_\phi\mid\\
T\phi(a),\phi(a)T\in\mathcal K(E)\\
\text{ for all }a\}.
\end{gathered}
\tag{1.2}
\]

### Lemma 1.1. The defect quotient

\(\mathcal D_\phi\) is a graded unital C\*-algebra, and \(\mathcal J_\phi\) is a graded closed ideal in it. A cycle operator belongs to \(\mathcal D_\phi^1\), with
\[
F-F^*,\ F^2-1\in\mathcal J_\phi.
\tag{1.3}
\]

**Proof.** If homogeneous \(S,T\) pseudocommute, the graded Leibniz identity expresses the commutator of \(ST\) as the sum of two bounded multiples of compact commutators. For adjoints, direct reversal of the two terms gives
\[
[T,\phi(a^*)]_{\mathrm{gr}}^*
=-(-1)^{|T||a|}[T^*,\phi(a)]_{\mathrm{gr}}.
\]
Thus the homogeneous spaces are closed under the required products and adjoints. Their finite parity sum is norm closed: the parity projections are bounded, and the defining compact-commutator conditions are closed. The identity is even, so this is a graded unital C\*-algebra.

If \(K\) is two-sided locally compact and \(S\) pseudocommutes, then \(SK\phi(a)\) and \(\phi(a)KS\) are compact immediately. In the other two products, move \(S\) across \(\phi(a)\), leaving a compact commutator plus a bounded multiple of \(\phi(a)K\) or \(K\phi(a)\). This proves the two-sided ideal property first on homogeneous entries and then by addition. Taking adjoints exchanges the two compactness conditions, and norm limits preserve both. Hence \(\mathcal J_\phi\) is a closed graded ideal.

For a cycle, \(K=F-F^*\) belongs to \(\mathcal D_\phi\). Since \(K^*=-K\), its right local compactness implies left local compactness by adjoints, so \(K\in\mathcal J_\phi\). The element \(F^2-1\) also lies in \(\mathcal D_\phi\), and
\[
F^2-F^{*2}=F(F-F^*)+(F-F^*)F^*
\]
lies in this ideal. The right compactness of \((F^2-1)\phi(a)\), together with this identity and adjoints, gives its left compactness. This proves (1.3) with no unitality assumption on the represented algebra. \(\square\)

Thus in \(\mathcal D_\phi/\mathcal J_\phi\) a cycle operator is an odd self-adjoint unitary. The zero quotient, which occurs for compact representations, is allowed.

### Lemma 1.2. Testing commutators after multiplication

In (1.1), it suffices to require
\([F,\phi(a)]_{\mathrm{gr}}\phi(b)\in\mathcal K(E)\)
for all homogeneous \(a,b\), while retaining the two stated local defects.

**Proof.** The adjoint defect \(K=F-F^*\) is two-sided locally compact, since \(K^*=-K\). Taking the adjoint of
\([F,\phi(b^*)]_{\mathrm{gr}}\phi(a^*)\)
shows that \(\phi(a)[F^*,\phi(b)]_{\mathrm{gr}}\) is compact. Also
\(\phi(a)[K,\phi(b)]_{\mathrm{gr}}\) is compact: in its first term use \(K\phi(b)\), and in its second use \(\phi(ab)K\). Hence
\(\phi(a)[F,\phi(b)]_{\mathrm{gr}}\) is compact. The graded Leibniz identity now makes
\([F,\phi(ab)]_{\mathrm{gr}}\) compact.

An even approximate identity of \(A\) is obtained by averaging any positive contractive approximate identity with its grading image. For homogeneous \(a\), its products with these even elements converge in norm to \(a\). The corresponding commutators converge in norm as well, proving the required compactness for \(a\). The converse implication is immediate. \(\square\)

## 2. Homotopies and gluing

Let \(IB=C([0,1],B)\), graded pointwise. A **homotopy** is a cycle over \((A,IB)\). Its endpoint at \(t\) is
\[
(E_t,\phi_t,F_t),\qquad
E_t=E\otimes_{\mathrm{ev}_t}B,
\tag{2.1}
\]
with representation and operator induced by interior tensor product. Compact operators descend to compact operators in a fiber: a rank-one operator descends to the corresponding rank-one operator on the images of its two vectors, and norm limits descend as well. A countable generating family also descends. Endpoints are understood up to a degree-zero unitary intertwining both the representation and operator.

An **operator homotopy** keeps \(E,\phi\) fixed and varies \(F\) in norm. This is a homotopy on \(C([0,1],E)\): its compact operators are exactly \(C([0,1],\mathcal K(E))\). One direction follows from rank-one sections; for the converse, approximate a continuous compact-valued field at finitely many points by finite-rank operators and use a finite scalar partition of unity. Constant vector sections express those finite-rank approximations on the interval.

Strong-* continuity of operators alone is not sufficient to declare a homotopy. Its defects must belong to the compact operators of the interval module, a condition imposed by the definition.

### Lemma 2.1. Fibers and gluing of Hilbert modules

The evaluation map \(E\to E_t\) for a Hilbert \(IB\)-module is onto, and
\[
\|x_t\|^2=\|\langle x,x\rangle(t)\|.
\tag{2.2}
\]
If countably generated modules over two intervals have degree-preservingly identified junction fibers, their fiberwise gluing is countably generated. Compatible adjointable operators glue; compatible compact operators glue to compact operators.

**Proof.** The kernel of evaluation consists of vectors with \(\langle x,x\rangle(t)=0\), equivalently the closure of \(E\) times the coefficient ideal vanishing at \(t\). To see the last description, multiply such an \(x\) by scalar cutoffs that vanish near \(t\) and tend to one away from \(t\). Continuity of \(\|\langle x,x\rangle(s)\|\) proves convergence in norm. These scalar multipliers act on the Hilbert module by the central multiplier action; if needed, insert a coefficient approximate identity to express their values as elements of that closed product ideal.

The quotient norm is (2.2). Its lower bound follows from contractivity of evaluation. For the upper bound, multiply \(x\) by a scalar cutoff equal to one at \(t\) and supported in an arbitrarily small neighborhood; its norm tends to \(\|x_t\|\). The quotient is complete and maps isometrically to the interior-tensor fiber, with dense image, so that map is onto.

Write the two modules as \(E_1,E_2\), and let \(U:(E_1)_1\to(E_2)_0\) be their junction unitary. Over the pullback algebra
\[
C([0,1],B)\mathbin{\times_B}C([0,1],B)
\cong C([0,2],B),
\]
form the closed module
\[
G=\{(x,y):Ux_1=y_0\}.
\tag{2.3}
\]
Its inner product is the pair of inner products, whose junction values match. It is complete with norm \(\max(\|x\|,\|y\|)\). The component gradings preserve the matching relation.

For countable generation, the kernel of junction evaluation is generated by scalar cutoffs times generating vectors of each half, extended by zero to the other half. Choose countably many cutoffs increasing to one away from the junction; they approximate every kernel vector. Next take a countable generating family of the first junction fiber, obtained by evaluating generators of \(E_1\). Lift each member to both halves using surjectivity and \(U\), giving countably many vectors in \(G\). Together with the kernel generators these generate \(G\): approximate an arbitrary junction value by their coefficient span, subtract the corresponding lifted combination, and remove the remaining small junction value with a cutoff in a sufficiently small neighborhood. Continuity of the vector norm makes that removal arbitrarily small. Coefficients on one half extend to the other by their constant junction value.

Compatible adjointable operators and their adjoints preserve (2.3), so they give an adjointable operator on \(G\). Its fiber norm controls its module norm: for any adjointable \(T\),
\(\|Tx\|=\sup_s\|(Tx)_s\|\), hence \(\|T\|=\sup_s\|T_s\|\).

Here is the compactness assertion. The finite Gram norm identity used here is proved in [Ordinary Hilbert C\*-module foundations, MF.6](supporting/hilbert-c-star-modules-and-morita-equivalence/hilbert-module-foundations.html#mf-006), equation (MF.18a) and its adjoint form. A compact operator on either half has continuous fiber norm. For a finite sum \(K=R_XR_Y^*\) of rank-one operators,
\[
\begin{gathered}
G_X(s)=X_s^*X_s,\\
G_Y(s)=Y_s^*Y_s,\quad P_s=G_Y(s)^{1/2},\\
\|K_s\|^2=\|P_sG_X(s)P_s\|.
\end{gathered}
\tag{2.4}
\]
where \(R_X,R_Y\) are the finite columns of its vectors. Their Gram matrices are continuous \(B\)-valued matrices, so (2.4) is continuous; uniform finite-rank approximation proves the general assertion.

Approximate the common junction value of two matching compact operators by a finite sum of rank-one operators on that fiber. Lift both vectors of each rank-one term to \(G\); their sum is a compact operator \(L\) on \(G\). On a sufficiently small neighborhood of the junction its discrepancy from the desired operators has norm less than \(2\varepsilon\), by the preceding continuity. Choose a scalar partition into a function supported in this neighborhood and two functions supported away from the junction, one on each half. Multiply \(L\) by the first function. On the other pieces multiply the given compact half-operators by the respective cutoff; their finite-rank approximations extend by zero to compact operators on \(G\). The resulting global compact approximates the matching operator within \(2\varepsilon\). Let \(\varepsilon\) tend to zero. \(\square\)

### Theorem 2.2. Homotopy is an equivalence relation

Homotopy on cycles, with endpoint unitary equivalence, is reflexive, symmetric and transitive. It respects direct sums.

**Proof.** A constant interval cycle proves reflexivity. Pulling back by \(t\mapsto1-t\) proves symmetry. For transitivity, glue the two interval modules along their identified endpoint by Lemma 2.1. The representations and cycle operators glue because the junction unitary intertwines them. Each defect in (1.1) is a matching pair of compact operators, so is compact on the glued module by the lemma. Rescale \([0,2]\) to \([0,1]\). Its endpoints are the required outer endpoints. Direct sums of interval cycles give the last assertion. \(\square\)

### Proposition 2.3. Degenerate cycles vanish

A degenerate cycle is homotopic to the zero module.

**Proof.** Use \(C_0([0,1),E)\) as a Hilbert \(IB\)-module, with pointwise representation and constant operator \(F\). It is countably generated: take scalar functions from a countable dense family in \(C_0([0,1))\), multiply them by generating vectors of \(E\), and then by coefficient functions. All defects are exactly zero, so this is a cycle. Its fiber at zero is \(E\); its fiber at one is zero. \(\square\)

The exact vanishing in this proof is essential. A constant nonzero compact defect on a module that disappears at an endpoint need not be a compact interval-module operator.

## 3. Perturbation and normalization

### Proposition 3.1. Locally compact perturbations

Suppose \((E,\phi,F)\) and \((E,\phi,F')\) are cycles and
\[
(F'-F)\phi(a)\in\mathcal K(E)
\quad\text{for all }a.
\tag{3.1}
\]
The straight segment \(F_t=F+t(F'-F)\) is an operator homotopy.

**Proof.** Put \(K=F'-F\). Both operators pseudocommute, so \(K\in\mathcal D_\phi^1\). Their self-adjointness defects imply \(K-K^*\) is right locally compact; (3.1) then implies that \(K^*\) is right locally compact too. Taking adjoints gives left local compactness of \(K\), so \(K\in\mathcal J_\phi\). In the quotient of Lemma 1.1 every \(F_t\) equals \(F\), hence has the same self-adjointness and square defects. Its graded commutators are compact by linearity. These compact fields are norm-continuous in \(t\), proving the interval compactness condition. \(\square\)

### Theorem 3.2. Odd self-adjoint normalization

Every cycle is operator homotopic, by locally compact perturbations, to one with \(F=F^*\) and \(\|F\|\leq1\). After adding a zero-representation degenerate cycle, it is homotopic to a cycle whose operator is an exact odd self-adjoint unitary.

**Proof.** Work first in the graded quotient of Lemma 1.1. There the image of \(F\) is an odd self-adjoint involution. Replacing \(F\) by \(f=(F+F^*)/2\) leaves that image unchanged; Proposition 3.1 supplies the operator path. Apply the continuous odd function
\(g(t)=\max(-1,\min(t,1))\)
to \(f\) inside \(\mathcal D_\phi\). Grading compatibility of functional calculus follows by polynomial approximation: applying the grading to \(g(f)\) gives \(g(-f)=-g(f)\). Since \(g(1)=1\) and \(g(-1)=-1\), the image of \(g(f)\) remains the same involution. The change belongs to \(\mathcal J_\phi\), so again gives the path of Proposition 3.1. We can now assume \(f=f^*\) and \(\|f\|\leq1\).

Set \(s=(1-f^2)^{1/2}\). It is even, commutes with \(f\), and belongs to \(\mathcal J_\phi\) because its quotient image is zero. On \(E\oplus E^{\mathrm{op}}\) use \(\rho=\phi\oplus0\) and
\[
G_t=\begin{pmatrix}f&ts\\ts&-f\end{pmatrix},
\qquad 0\leq t\leq1.
\tag{3.2}
\]
The grading on the two summands is opposite. Consequently even underlying maps in the off-diagonal positions, and odd underlying maps in the diagonal positions, give an odd block operator. It is self-adjoint. Multiplication gives zero off-diagonal entries in its square and
\[
G_t^2-1=(1-t^2)\operatorname{diag}(f^2-1,f^2-1).
\]
After multiplication by \(\rho(a)\), this is compact. For homogeneous \(a\), the graded commutator has top-left block \([f,\phi(a)]_{\mathrm{gr}}\), top-right block \(-(-1)^{|a|}t\phi(a)s\), bottom-left block \(ts\phi(a)\), and zero bottom-right block. All are compact. Their dependence on \(t\) is norm continuous, so they are compact on the interval module. The path starts at the normalized cycle plus the zero-representation cycle \((E^{\mathrm{op}},0,-f)\), which is degenerate. At its other end \(G_1^2=1\) exactly. No complementary even identity has been inserted into an odd operator. \(\square\)

If \(B\) is \(\sigma\)-unital, every class can also be represented on \(\widehat H_B\). Add \((\widehat H_B,0,0)\), a countably generated degenerate module, and use graded stabilization. The countability condition is why this formulation includes \(\sigma\)-unitality. An even identity on an unrepresented summand cannot simply be inserted into an odd operator; the doubled construction (3.2) preserves the required parity.

### Proposition 3.3. The positive comparison criterion

Let \((E,\phi,F)\) and \((E,\phi,F')\) be cycles. Suppose that for every homogeneous \(a\),
\[
\begin{gathered}
\phi(a)(FF'+F'F)\phi(a)^*
\\
\text{is positive modulo }\mathcal K(E).
\end{gathered}
\tag{3.3}
\]
Then the cycles are operator homotopic.

**Proof.** In the defect quotient \(\mathcal D_\phi/\mathcal J_\phi\), both \(F,F'\) are self-adjoint unitaries. Put \(L=FF'+F'F\), an even pseudocommuting operator, and \(h=(L+L^*)/2\). Then \(L-h\in\mathcal J_\phi\). We first show that the negative part \(h_-\) belongs to \(\mathcal J_\phi\).

Pass temporarily to \(\mathcal L(E)/\mathcal K(E)\). The image of \(h\) commutes with the image of \(\phi(a)\), because \(h\) is even. Put \(b=\phi(aa^*)\), in this quotient. It is positive, commutes with \(h\), and \(hb=\phi(a)h\phi(a)^*\) is positive by (3.3). Commuting functional calculus gives \(h_-b=0\): on a negative spectral interval \(h\leq-\varepsilon\), a positive cutoff \(f(h)\) satisfies
\(0\leq f(h)hb f(h)\leq-\varepsilon f(h)^2b\), so \(f(h)b=0\); cutoffs exhausting the negative spectrum give the claim. It follows that
\[
(h_-\phi(a))(h_-\phi(a))^*=h_-bh_-=0
\]
in that quotient. Thus \(h_-\phi(a)\) is compact; its commutation modulo compacts gives the other side too. Functional calculus keeps \(h_-\) in \(\mathcal D_\phi\), proving it belongs to \(\mathcal J_\phi\).

Consequently \(P=h_+\) is a positive even lift of \(L\) modulo \(\mathcal J_\phi\). Its image commutes with those of \(F,F'\). For example
\[
[L,F]=F'F^2-F^2F'=0
\quad\text{modulo }\mathcal J_\phi,
\]
and similarly for \(F'\); functional calculus then preserves this commutation.

For \(c=\cos\theta,s=\sin\theta\), \(0\leq\theta\leq\pi/2\), put
\[
F_\theta=(1+csP)^{-1/2}(cF+sF').
\tag{3.4}
\]
The first factor is even, norm-continuous and well defined since \(1+csP\geq1\). In the defect quotient the second factor is self-adjoint, commutes with the first, and has square \(1+csP\). Hence \(F_\theta\) is an odd self-adjoint unitary there. It remains in \(\mathcal D_\phi\), so it satisfies all cycle conditions, with norm-continuous compact defects. Its endpoints are \(F,F'\). \(\square\)

For example, if \(\|F-F'\|<1\), the criterion holds in the defect quotient, since
\[
FF'+F'F=2-(F-F')^2\geq1
\]
there. This comparison will control choices of product operators in the later Kasparov-product construction.

## 4. The abelian group

Define \(KK(A,B)\) as the set of homotopy classes of cycles. Direct sum is the addition. Define
\[
\begin{gathered}
KK^n(A,B)=KK(A,B\widehat\otimes C_n),\\
 n\geq0.
\end{gathered}
\tag{4.1}
\]
The notation \(KK^0=KK\) is immediate; identifying all degrees modulo two is a later periodicity theorem.

### Theorem 4.1. Group law and inverse

\(KK(A,B)\) is an abelian group. An inverse of \((E,\phi,F)\) is
\[
\begin{gathered}
(E^{\mathrm{op}},\widetilde\phi,-F),\\
\widetilde\phi(a)=\phi(\alpha(a)).
\end{gathered}
\tag{4.2}
\]
The zero module is the identity, and every degenerate module has that class.

**Proof.** Theorem 2.2 makes direct sum well defined on homotopy classes. Rebracketing and exchanging summands are even unitaries intertwining the full triples, giving associativity and commutativity. The zero module is the additive identity, and Proposition 2.3 identifies every degenerate cycle with it.

On \(E^{\mathrm{op}}\), the induced grading of operators is unchanged. If \(a\) has degree \(p\), the twisted representation in (4.2) is \((-1)^p\phi(a)\). It is graded, and the three defects of its operator \(-F\) are scalar sign multiples of the corresponding original defects. Thus (4.2) is a cycle. Its twist is needed to obtain the following homotopy on \(E\oplus E^{\mathrm{op}}\):
\[
\begin{gathered}
\rho=\phi\oplus\widetilde\phi,\\
H_\theta=
\begin{pmatrix}
\cos\theta\,F&\sin\theta\\
\sin\theta&-\cos\theta\,F
\end{pmatrix},
\\
0\leq\theta\leq\pi/2.
\end{gathered}
\tag{4.3}
\]
Put \(D=\operatorname{diag}(F,-F)\) and let \(J\) be the flip. Both are odd, \(DJ+JD=0\), and \(J=J^*=J^{-1}\). Hence the square and adjoint defects of \(H_\theta\) are respectively \(\cos^2\theta(D^2-1)\) and \(\cos\theta(D-D^*)\), locally compact for \(\rho\). For degree \(p\), its flip commutator has blocks
\[
\begin{gathered}
\widetilde\phi(a)-(-1)^p\phi(a)=0,
\\
 \phi(a)-(-1)^p\widetilde\phi(a)=0.
\end{gathered}
\]
The diagonal commutators are scalar sign multiples of \([F,\phi(a)]_{\mathrm{gr}}\). All defects form norm-continuous compact fields. At \(\theta=0\) the path is the original cycle plus (4.2); at \(\theta=\pi/2\) it is the degenerate flip. Their classes therefore sum to zero. This constructs an inverse for every class, completing the group proof. \(\square\)

When \(A\) is trivially graded, the twist disappears. With nontrivially graded \(A\), omitting it generally destroys the cancellation of the off-diagonal graded commutators.

We have not identified arbitrary interval homotopy with stable operator homotopy. The known comparison theorem assumes separable \(A\) and \(\sigma\)-unital \(B\): cycles define the same class exactly when, after adding suitable degenerate cycles and applying unitary equivalence, they are operator homotopic. Its full proof remains an obligation in *Homotopy, associativity, the index pairing and KK-equivalence*. None of the group arguments above uses that comparison theorem.

## 5. Homomorphisms, splitting morphisms and Morita modules

### Proposition 5.1. Compact representations give cycles

If \(E\) is a countably generated graded Hilbert \(B\)-module and
\(\phi:A\to\mathcal K(E)\) is graded, then \((E,\phi,0)\) is a cycle. For any bounded odd adjointable \(T\), \((E,\phi,T)\) is a cycle, and the segment from zero to \(T\) identifies their classes.

**Proof.** Every expression in (1.1) is a finite sum of a compact operator multiplied by bounded adjointable operators. These are compact. The same calculation holds along the norm-continuous segment \(tT\). \(\square\)

For \(\sigma\)-unital \(B\), a graded homomorphism \(\phi:A\to B=\mathcal K(B)\) therefore gives
\[
[\phi]=[(B,\phi,0)]\in KK(A,B).
\tag{5.1}
\]
Indeed \(B\) is countably generated as its own right module by a countable approximate identity. Conversely countable generation of \(B\) implies \(\sigma\)-unitality: for generators \(b_j\), the positive norm-convergent sum
\(h=\sum 2^{-j}b_jb_j^*/(1+\|b_j\|^2)\)
has a functional-calculus approximate identity \(u_n=h(h+1/n)^{-1}\) acting in norm on every \(b_jB\). In fact \(h\geq c_jb_jb_j^*\), with \(c_j=2^{-j}/(1+\|b_j\|^2)>0\), so
\[
\begin{gathered}
\|(1-u_n)b_j\|^2
\\\leq c_j^{-1}\|(1-u_n)h(1-u_n)\|
\\\longrightarrow0.
\end{gathered}
\]
Density of the generating span gives \(u_nb\to b\) for every \(b\in B\); taking adjoints gives convergence on the right too. Thus this hypothesis cannot be omitted from the canonical module in (5.1).

In particular \(1_B=[(B,\mathrm{id},0)]\) is the identity class for \(\sigma\)-unital \(B\); its identity property for the Kasparov product is proved later, when the product is defined.

There is also a useful arbitrary-coefficient version when \(A\) is \(\sigma\)-unital. Let
\[
E_\phi=\overline{\phi(A)B}\subset B.
\tag{5.2}
\]
A countable approximate identity \(e_j\) of \(A\) makes the vectors \(\phi(e_j)\) generate this right Hilbert \(B\)-module: \(\phi(e_j)\phi(a)b\to\phi(a)b\). The module is graded, and \(\phi(a)\) acts compactly on it. Indeed
\(\mathcal K(E_\phi)\) consists of the closure of left multiplications by \(xy^*\), \(x,y\in E_\phi\), and
\(\phi(e_j)\phi(a)\phi(e_j)\to\phi(a)\).
To verify membership in that closure, let \(v_\nu\) be a positive contractive approximate identity in \(B\). With \(x=\phi(e_j)\phi(a)v_\nu\) and \(y=\phi(e_j)v_\nu\), both vectors lie in \(E_\phi\), and
\[
xy^*=\phi(e_j)\phi(a)v_\nu^2\phi(e_j)
\longrightarrow\phi(e_j)\phi(a)\phi(e_j).
\]
The generators \(\phi(e_j)\) themselves belong to \(E_\phi\): multiplying them by a coefficient approximate identity approximates them, and \(\phi(e_i)\phi(e_j)\to\phi(e_j)\). Hence \((E_\phi,\phi,0)\) defines a class even if \(B\) is not \(\sigma\)-unital. When \(B\) is \(\sigma\)-unital, this is the same homomorphism class as (5.1), as shown below.

### Lemma 5.2. Removing an essential submodule for a compact representation

Let \(E\) and \(E_\phi=\overline{\phi(A)E}\) both be countably generated, and let \(\phi:A\to\mathcal K(E)\) be graded. The cycle \((E,\phi,0)\) has the same class as its restriction to \(E_\phi\).

**Proof.** Over \(IB\), take the closed submodule
\[
\begin{gathered}
M=\{\xi\in C([0,1],E)\mid\\\xi(1)\in E_\phi\},
\end{gathered}
\tag{5.3}
\]
with pointwise \(\phi\) and operator zero. It is countably generated if both \(E\) and \(E_\phi\) are: use cutoff multiples of generators of \(E\), vanishing at one, and constant sections of generators of \(E_\phi\). Evaluation at one is onto, and the same cutoff argument as Lemma 2.1 shows these generate. The representation is compact on \(M\). To verify this last point without assuming a complement, approximate \(\phi(a)\) by operators of the form \(\phi(e_i)\phi(a)\phi(e_i)\), using an approximate identity of \(A\). Each is a norm limit of finite-rank operators whose two vectors belong to \(E_\phi\): sandwich a finite-rank approximation of \(\phi(a)\) by \(\phi(e_i)\). Their constant vector sections belong to \(M\), proving compactness. Thus (5.3) gives the required homotopy.

In the application to (5.2), \(A\) is \(\sigma\)-unital and \(E_\phi\) is countably generated by the images of its countable approximate identity. Thus the countability hypothesis of this lemma is satisfied. \(\square\)

For clarity, that countability is part of Lemma 5.2's hypothesis. No general claim that every closed submodule of a countably generated module is countably generated is intended.

For arbitrary \(A,B\) without those countability assumptions, there is no automatic canonical cycle on \(B\). For example, \(B=c_0(J)\) for uncountable \(J\) is not countably generated as a right module: countably many vectors have support in a countable subset of \(J\). Its identity homomorphism cannot be represented by the canonical module \(B\) in our definition. Other definitions allowing larger standard modules require a separate convention.

### Proposition 5.3. A splitting morphism, with its grading

Let
\[
0\longrightarrow B\longrightarrow D
\mathop{\longrightarrow}^{q}A\longrightarrow0
\]
be a graded extension with graded homomorphic section \(s\), and assume \(B\) is \(\sigma\)-unital. Let \(\omega:D\to M(B)\) be the multiplication action on its ideal. Then its splitting cycle over \((D,B)\) is
\[
\begin{gathered}
(B\oplus B^{\mathrm{op}},\ \omega\oplus\omega sq\alpha_D,\ J),\\
J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\end{gathered}
\tag{5.4}
\]

**Proof.** The ideal grading extends to its multipliers by
\((L,R)\mapsto(\beta L\beta,\beta R\beta)\)
in the double-centralizer construction of Lesson 1, Lemma 2.0. Multiplication by \(d\) then shows that \(\omega\) intertwines this grading with \(\alpha_D\). Thus both diagonal actions in (5.4) are graded homomorphisms. The module is countably generated by \(\sigma\)-unitality of \(B\), and the opposite second grading makes \(J\) odd. It is an exact self-adjoint involution, so only its commutator needs checking.

For degree \(p\), the second action is \((-1)^p\omega(sq(d))\). The top-right and bottom-left blocks of \([J,\rho(d)]_{\mathrm{gr}}\) are therefore
\[
(-1)^p\bigl(\omega(sq(d))-\omega(d)\bigr),
\qquad\omega(d)-\omega(sq(d)).
\]
Exactness gives \(d-sq(d)\in B\). Lemma 2.0 identifies its multiplier action with left multiplication by that element of the ideal. Such left multiplications are precisely \(\mathcal K(B)=B\): rank-one operators multiply by \(xy^*\), and a coefficient approximate identity makes their span dense in \(B\). Thus the blocks are compact, proving every cycle condition. \(\square\)

The grading twist in (5.4) is essential. If the action of an odd quotient element is the same in both summands, an untwisted flip has its sum, rather than its difference, as graded commutator. For a direct-sum extension \(D=B\oplus A\), \(\omega sq=0\); (5.4) then agrees with the doubled homomorphism cycle for the projection onto \(B\). The class may depend on the chosen section.

### Proposition 5.4. Morita correspondences

A graded \(A\)-\(B\) imprimitivity module gives a class \([(E,\phi,0)]\in KK(A,B)\) if \(A\) and \(B\) are \(\sigma\)-unital.

**Proof.** By the definition of imprimitivity, its left action identifies \(A\) with \(\mathcal K(E)\). This action is graded. Since \(\mathcal K(E)\) has a countable approximate identity, \(E\) is countably generated: approximate its approximate-identity operators by finite sums of rank-one operators, and collect the first vectors of those sums. Their span times \(B\) is dense, because \(\mathcal K(E)\) acts nondegenerately on \(E\). To verify nondegeneracy directly for a vector \(x\), apply continuous cutoffs to \(\langle x,x\rangle\) and approximate \(x\) by \(x\langle x,x\rangle(\langle x,x\rangle+\varepsilon)^{-1}\), which lies in the closed span of \(\theta_{u,v}E\). Proposition 5.1 proves the assertion. The inverse-product claim making this class a KK-equivalence is a later product theorem, not part of its construction here. \(\square\)

For a concrete example, let \(B\) be trivially graded and \(\sigma\)-unital. The column module \(B^n\) has
\[
\langle x,y\rangle_B=\sum_jx_j^*y_j,\qquad
{}_{M_n(B)}\langle x,y\rangle=xy^*.
\]
Matrix multiplication is the left action, and
\((xy^*)z=x\langle y,z\rangle_B\) verifies compatibility. The spans of both inner products are dense in their coefficient algebras, by a coefficient approximate identity, and \(\mathcal K(B^n)=M_n(B)\). Its zero-operator cycle is the standard Morita class from \(M_n(B)\) to \(B\).

## 6. The scalar group and interval indices

We now compute \(KK(\mathbb C,\mathbb C)\) for trivially graded scalars, using the actual homotopy relation. The next finite-dimensional reduction prevents any appeal to an unproved identification of homotopy relations.

### Lemma 6.1. An index for a varying interval module

Let \(X,Y\) be Hilbert \(C([0,1])\)-modules and \(T:X\to Y\) adjointable, with
\[
\begin{gathered}
T^*T-1_X\in\mathcal K(X),\\
TT^*-1_Y\in\mathcal K(Y).
\end{gathered}
\tag{6.1}
\]
Every fiber \(T_t\) is Fredholm, and \(\operatorname{index}T_t\) is independent of \(t\).

**Proof.** Evaluation preserves the two compact defects, so the Hilbert-space Fredholm criterion proves the first assertion.

Put \(A_0=TT^*\). Choose a continuous nonnegative function \(g\) on its spectrum, supported near zero, with \(g(1)=0\), such that
\(A_0+g(A_0)\geq c1_Y\) for some \(c>0\); for example extend \(g(s)=\max(0,c-s)\) for \(0<c<1\). The image of \(A_0\) in the compact-operator quotient is \(1\), so \(g(A_0)\) is compact. Approximate this positive compact operator by \(RR^*\), with an adjointable finite column \(R:C([0,1])^N\to Y\), closely enough that
\[
TT^*+RR^*\geq(c/2)1_Y.
\tag{6.2}
\]
Such positive finite-column approximations follow from the definition of compacts: approximate the square root by a finite-rank \(L=R_UR_V^*\); then
\(LL^*=R_U(R_V^*R_V)R_U^*=RR^*\), using the finite positive matrix square root.

The augmented map
\[
\widetilde T=(T,R):X\oplus C([0,1])^N\to Y
\tag{6.3}
\]
is surjective and has adjointable right inverse
\(\widetilde T^*(\widetilde T\widetilde T^*)^{-1}\).
Its kernel projection is
\[
P=1-\widetilde T^*
(\widetilde T\widetilde T^*)^{-1}\widetilde T.
\tag{6.4}
\]
It is compact. Indeed
\(\widetilde T^*\widetilde T-1\) is compact by (6.1) and the finite free summand, while
\(\widetilde T\widetilde T^*-1\) is compact. In the adjointable-operator quotient on
\((X\oplus C([0,1])^N)\oplus Y\), the off-diagonal map \(\widetilde T\) is therefore a unitary between the two corners, so (6.4) has zero image.

The range of a compact projection over a unital coefficient algebra is finite projective. Here is the needed constructive argument. Approximate \(P\) by \(SS^*\), a finite column, so that \(PSS^*P\) is invertible on \(P(X\oplus C([0,1])^N)\). Then
\[
V=(PSS^*P)^{-1/2}PS
\]
is a coisometry from a finite free module onto that range. Thus \(V^*V\) is a finite matrix projection over \(C([0,1])\), with range isomorphic to \(\operatorname{ran}P\). Its endpoint ranks, and indeed all its fiber ranks, agree: continuous finite matrix projections have locally constant rank, since projections less than distance one apart have isomorphic ranges. For the rank assertion, if finite-dimensional projections \(p,q\) satisfy \(\|p-q\|<1\), the map \(q:\operatorname{ran}p\to\operatorname{ran}q\) is injective: a vector in its kernel has norm at most \(\|p-q\|\) times its norm. Exchanging \(p,q\) gives the reverse dimension inequality, hence equal ranks. Continuity makes this apply locally along the interval, and connectedness makes the rank constant.

The fiber of (6.3) is surjective, with kernel the fiber of \(P\), because its right inverse evaluates to a right inverse. At every \(t\), adding the finite-dimensional domain summand changes the Hilbert-space Fredholm index by \(N\); its off-diagonal finite-rank column does not change that index. Therefore
\[
\operatorname{index}T_t=\operatorname{rank}P_t-N.
\tag{6.5}
\]
The right side is constant. \(\square\)

### Theorem 6.2. The scalar KK-group is the integers

For a scalar cycle let \(P=\phi(1)\), and let \(T\) be the positive-to-negative block of \(PFP\) on \(PH\). Then
\[
\begin{aligned}
KK(\mathbb C,\mathbb C)&\longrightarrow\mathbb Z,\\
[(H,\phi,F)]&\longmapsto\operatorname{index}T
\end{aligned}
\tag{6.6}
\]
is an isomorphism. It sends the homomorphism class \(1_{\mathbb C}\) to \(1\).

**Proof.** First normalize to \(F=F^*\). Compression by the even projection \(P\) is a locally compact perturbation, since
\((F-PFP)P=(1-P)FP\) is compact by \([F,P]\in\mathcal K\). Its represented part is a cycle on \(PH\), and its remaining part has zero representation, hence vanishes. On the represented part \(\phi\) is unital and
\[
F=\begin{pmatrix}0&T^*\\T&0\end{pmatrix},
\qquad T^*T-1,\ TT^*-1\in\mathcal K.
\]
Thus \(T\) is Fredholm. Normalization and compression do not alter the compression index, by the compact-perturbation facts proved in the index-pairing lesson.

Perform the same operations on an arbitrary interval cycle over \(C([0,1])\). The projection \(P=\phi(1)\) splits its module into represented and unrepresented parts; in the represented part the grading gives two Hilbert \(C([0,1])\)-submodules. Its off-diagonal operator satisfies (6.1), so Lemma 6.1 proves equality of its two endpoint indices. Hence (6.6) is well defined for the full homotopy relation. It is additive by direct sums.

For injectivity and surjectivity, work now on a single Hilbert space. The polar decomposition \(T=V|T|\) gives a partial isometry \(V\) with finite-dimensional kernel and cokernel. The difference \(T-V\) is compact: \(|T|-1\) is compact by continuous functional calculus from \(T^*T-1\), and \(T-V=V(|T|-1)\). Replace \(T\) by \(V\), a compact perturbation. The represented cycle splits orthogonally into its finite-dimensional even kernel, its finite-dimensional odd cokernel, and the complements joined by the unitary \(V\). The last part is degenerate. Thus its class is
\[
\begin{gathered}
(\dim\ker T-\dim\ker T^*)\\\cdot[(\mathbb C,\mathrm{id},0)],
\end{gathered}
\tag{6.7}
\]
because an odd one-dimensional zero-operator cycle is the inverse of the even one by Theorem 4.1. Every integer occurs in this way. The even one-dimensional cycle has index \(1\); thus (6.6) and integer multiples of that cycle are inverse maps. \(\square\)

For finite-dimensional \(H^+,H^-\), every operator is compact and the index is \(\dim H^+-\dim H^-\). Balanced finite-dimensional modules consequently represent zero, independently of their particular odd operator.

## 7. Fredholm modules and the odd circle class

An even Fredholm module from *Fredholm modules and analytic K-homology*, on a separable graded Hilbert space, is exactly a cycle over \((A,\mathbb C)\) when \(A\) has trivial grading. Its homotopies there used operator paths and degenerate summands. Those operations define the same KK-class by the results above. The converse comparison, giving the full identification with analytic K-homology, is proved later using the precise stable operator-homotopy theorem.

An ungraded odd Fredholm module \((H,\pi,F)\) over trivially graded \(A\) supplies a cycle for \(KK^1(A,\mathbb C)=KK(A,C_1)\). Regard
\[
\begin{gathered}
E=H\otimes C_1,\\
\phi(a)=\pi(a)\otimes1,\\
G=F\otimes L_\varepsilon,
\end{gathered}
\tag{7.1}
\]
with grading on the coefficient factor and trivial grading on \(H\). Left multiplication \(L_\varepsilon\) is odd, so \(G\) is odd. The square, adjoint and commutator defects are the original compact Hilbert-space defects tensored with \(1\) or \(L_\varepsilon\). The exterior compact-operator formula of the preceding lesson makes them compact module operators. Separability of \(H\) makes \(E\) countably generated.

For the circle, use \(H=L^2(S^1)\), multiplication representation of \(C(S^1)\), and the exact involution \(F=2P-1\), where \(P\) projects onto the Fourier modes \(n\geq0\). The preceding Fredholm-module lesson proves all cycle conditions from finite-rank Fourier commutators and uniform approximation. Formula (7.1) gives its odd KK-class. Equivalently, the circle Dirac operator \(D=-i\,d/d\theta\) has bounded transform \(D(1+D^2)^{-1/2}\), differing from \(F\) by a compact diagonal operator: its Fourier eigenvalue difference tends to zero in both directions. Tensored with \(L_\varepsilon\) this is a compact module perturbation, so Proposition 3.1 identifies the two KK-classes. This is the circle Dirac class. Its analytic compression pairing with the coordinate \(z\) is \(-1\), computed in the index-pairing lesson; identifying that pairing as a Kasparov product is the later product theorem.

## 8. Exercises

**8.1. Exact degeneracy.** Show that an odd self-adjoint involution \(F\) graded-commuting with \(\phi(A)\) gives a degenerate cycle. Explain why ordinary commutation with odd represented elements would not suffice.

**8.2. The inverse rotation.** Verify every defect of (4.3), including its off-diagonal graded commutators, for a homogeneous element of either degree.

**8.3. Scalar classes.** Reduce a scalar cycle to its finite kernel and cokernel, and prove that its integer is unchanged under arbitrary interval-module homotopy, rather than only operator homotopy.

**8.4. Two homomorphism cycles.** For a graded \(\phi:A\to B\) with \(B\) \(\sigma\)-unital, show that
\[
(B,\phi,0),\qquad
\left(B\oplus B^{\mathrm{op}},\phi\oplus0,
\begin{pmatrix}0&1\\1&0\end{pmatrix}\right)
\]
give the same class.

## 9. Solutions

**Solution to 8.1.** The square and adjoint defects are zero by hypothesis, and the first defect is the assumed graded commutator. Thus all three expressions (1.1) vanish. If \(a\) is odd, ordinary commutation says \(F\phi(a)=\phi(a)F\), while the graded condition requires their sum to be zero. For example \(\phi(\varepsilon)=F=\sigma_1\) on \(\mathbb C^2\), graded by \(\sigma_3\), gives an odd self-adjoint involution commuting ordinarily with the represented odd generator, but its graded commutator is \(2I\), which is not zero. The finite-dimensional example is a cycle, since its defects are compact, but is not degenerate.

**Solution to 8.2.** Put \(c=\cos\theta,s=\sin\theta\), \(D=\operatorname{diag}(F,-F)\) and \(J\) equal to the flip. Since \(DJ+JD=0\),
\((cD+sJ)^2-1=c^2(D^2-1)\).
The adjoint defect is \(c(D-D^*)\). Multiplying their diagonal entries by the corresponding representation gives compact operators. If \(|a|=p\), write \(\rho(a)=\operatorname{diag}(\phi(a),(-1)^p\phi(a))\). The top-right graded commutator of \(J\) is
\((-1)^p\phi(a)-(-1)^p\phi(a)=0\);
the bottom-left one is
\(\phi(a)-(-1)^{2p}\phi(a)=0\).
The diagonal commutator of \(D\) is a sign multiple of \([F,\phi(a)]_{\mathrm{gr}}\) in each block. This verifies the full homotopy and its degenerate endpoint for both parities.

**Solution to 8.3.** Normalize and compress to the range of \(\phi(1)\), removing the zero-representation summand by Proposition 2.3. The represented off-diagonal \(T\) has both square-modulus defects compact, so is Fredholm. Its polar partial isometry differs from it compactly; its complements are related by a unitary and form a degenerate cycle. The remaining finite cycle has even dimension \(\dim\ker T\) and odd dimension \(\dim\ker T^*\), hence represents their difference. For an interval homotopy do the normalization and compression on the interval module. Apply Lemma 6.1 to its off-diagonal map: the finite augmentation has compact kernel projection \(P\), represented by a continuous finite matrix projection, and gives endpoint indices \(\operatorname{rank}P_t-N\). That rank is constant on the interval. This proves the required invariance for varying modules and finishes both directions of the scalar group computation.

**Solution to 8.4.** Add the degenerate cycle \((B^{\mathrm{op}},0,0)\) to the first cycle. On the resulting module keep \(\rho=\phi\oplus0\) and put \(F_t=tJ\). The image of \(\rho\) is compact because \(\phi(a)\in B=\mathcal K(B)\). Every defect is therefore compact, either by direct multiplication or by Proposition 5.1. This norm-continuous odd path joins the sum to the second cycle. Countable generation follows from \(\sigma\)-unitality.

## What this lesson does not prove

The ordinary Hilbert-module tensor product and functional calculus are the exact prerequisites identified in the preceding lesson. That lesson supplies graded stabilization. The Hilbert-space Fredholm facts and compact index invariance are the exact prerequisites used in *Fredholm modules and analytic K-homology* and *The index pairing between K-theory and K-homology*. The additional interval-module index invariance, homotopy gluing, group law and scalar computation were proved here.

The full equivalence between homotopy and stable operator homotopy, under separability of \(A\) and \(\sigma\)-unitality of \(B\), remains a proof obligation in *Homotopy, associativity, the index pairing and KK-equivalence*. The full identification of analytic K-homology with \(KK(A,\mathbb C)\), the odd Fredholm picture and the identity/inverse-product statements for homomorphisms and Morita classes are proved in the later picture and product lessons. They have not been used as premises in this lesson.

## References

- B. Blackadar, *K-Theory for Operator Algebras*, second edition, 1998. [Actual freely readable author text](https://www.bruceblackadar.com/Mathematics/book6.pdf), Sections 17.1–17.4, especially the homotopy relations, inverse rotation, and positive comparison criterion. The parity, countability and interval-index details required here are proved in the lesson.

- J. Rosenberg, *Examples and applications of noncommutative geometry and K-theory*, author lecture notes, 2010. [Actual freely readable author version](https://math.umd.edu/~jmr/BuenosAires/NCGexamples.pdf), Section 1.2, pages 3–7, for Hilbert-module cycles, degeneracy and Morita examples. This reference is to the free lecture notes.

- *Kasparov's KK-theory*, [Graded C\*-algebras, Clifford algebras and graded Hilbert modules](KT-KK-05.html), Lemmas 3.0a and 6.0a, Proposition 6.1, Theorem 6.2 and Proposition 6.3; and [Extensions of C\*-algebras and the Busby invariant](KT-KK-01.html), Lemmas 1.1–1.2 and 2.0, for the earlier programme proofs identified above.
