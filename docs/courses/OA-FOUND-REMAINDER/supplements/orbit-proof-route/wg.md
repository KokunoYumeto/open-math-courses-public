<span id="general-weights-finite-domains-gns-spaces-and-normal-representations"></span>
# General weights: finite domains, GNS spaces, and normal representations

<span id="oa-mod-wg-001-conventions-and-precise-prerequisite-contract"></span>
<span id="OA-MOD-WG-001"></span>
<span id="oa-mod-wg-001"></span>
## OA-MOD-WG-001. Conventions and precise prerequisite contract

Throughout, \(M\) is a unital von Neumann algebra, represented faithfully and normally on some Hilbert space \(K\). Neither \(K\) nor the predual of \(M\) is assumed separable. All unqualified inner products are linear in their first variable. A bounded increasing net of positive operators has a supremum in \(M_+\); the notation \(a_i\uparrow a\) includes the assertion that \(a\) is that supremum. Its convergence is strong and ultraweak. A sum over an arbitrary index set of nonnegative numbers means the supremum of its finite partial sums.

The bounded operator-algebra prerequisites used here are:

1. Positivity and continuous functional calculus in a unital C*-algebra, including \(x^*x\leq\|x\|^2 1\), positive square roots, and order reversal under inversion of strictly positive invertible operators.
2. The spectral theorem for a bounded positive operator \(b\), including its support projection \(s(b)\), and monotone convergence for bounded increasing nets of positive operators.
3. On a norm-bounded set of operators, strong convergence implies ultraweak convergence. Multiplication by a fixed bounded operator is separately ultraweakly continuous.
4. A positive map between von Neumann algebras is normal precisely when it preserves the suprema of bounded increasing positive nets. Equivalently, for such a map, normality is ultraweak continuity. This equivalence is a bounded-map theorem; it is not being asserted here for extended-valued weights.

These are exact prerequisite statements, not claims that an open-text import has already been admitted. The course dependency audit records their import status. None is a theorem about closability of an unbounded operator or lower semicontinuity of a weight.

<a id="OA-MOD-WG-002"></a>
<span id="oa-mod-wg-002-the-finite-part-of-an-extended-valued-weight"></span>
<span id="oa-mod-wg-002"></span>
## OA-MOD-WG-002. The finite part of an extended-valued weight

A **weight** is a map \(\varphi:M_+\to[0,\infty]\) satisfying
\[
\varphi(0)=0,\qquad
\varphi(a+b)=\varphi(a)+\varphi(b),\qquad
\varphi(t a)=t\varphi(a)\quad(t\geq0).
\]
We use \(0\cdot\infty=0\). It follows immediately that \(0\leq a\leq b\) implies \(\varphi(a)\leq\varphi(b)\), since \(b=a+(b-a)\).

Define three subsets with different purposes:
\[
F_\varphi=\{a\in M_+:\varphi(a)<\infty\},\qquad
\mathfrak n_\varphi=\{x\in M:\varphi(x^*x)<\infty\},
\]
\[
\mathfrak m_\varphi
=\operatorname{span}_{\mathbb C}
\{y^*x:x,y\in\mathfrak n_\varphi\}.
\]
The first is a positive cone, the second will be the domain of the GNS map, and the third will be the domain of a finite-valued linear extension. In particular, the original weight is not a complex-linear function on all of \(M\).

We call \(\varphi\) **faithful** if \(a\in M_+\) and \(\varphi(a)=0\) imply \(a=0\). We call it **normal** if
\[
\varphi(a)=\sup_i\varphi(a_i)
\quad\text{whenever }0\leq a_i\uparrow a\text{ is bounded in }M.
\]
We call it **semifinite** if \(\mathfrak m_\varphi\) is ultraweakly dense in \(M\). This definition is essential: for general weights it is not replaced by a requirement that every nonzero positive element dominate a nonzero element of finite weight. Item OA-MOD-WG-013 gives a counterexample to that replacement.

<a id="OA-MOD-WG-003"></a>
<span id="oa-mod-wg-003-domain-algebra-and-its-positive-cone"></span>
<span id="oa-mod-wg-003"></span>
## OA-MOD-WG-003. Domain algebra and its positive cone

**Proposition.** For every weight, \(F_\varphi\) is an additive hereditary cone, \(\mathfrak n_\varphi\) is a left ideal, and \(\mathfrak m_\varphi\) is a possibly nonunital *-subalgebra. More precisely,
\[
\mathfrak m_\varphi=\operatorname{span}_{\mathbb C}F_\varphi,
\qquad
\mathfrak m_\varphi\cap M_+=F_\varphi,
\qquad
\mathfrak m_\varphi\subseteq
\mathfrak n_\varphi\cap\mathfrak n_\varphi^*.
\]
Every element of \(\mathfrak m_\varphi\) has the form \((a-b)+i(c-d)\), where \(a,b,c,d\in F_\varphi\).

**Proof.** Additivity and homogeneity preserve finite values, and monotonicity makes \(F_\varphi\) hereditary. For \(x,y\in\mathfrak n_\varphi\),
\[
(x+y)^*(x+y)\leq2x^*x+2y^*y;
\]
this follows by expanding \((x-y)^*(x-y)\geq0\). Consequently \(x+y\in\mathfrak n_\varphi\). Scalar multiplication is immediate. For \(a\in M\),
\[
(ax)^*(ax)=x^*a^*ax\leq\|a\|^2x^*x,
\]
so \(ax\in\mathfrak n_\varphi\). This proves the left ideal assertion.

Taking adjoints preserves the span defining \(\mathfrak m_\varphi\). Products of its spanning elements remain in that span because
\[
(y^*x)(v^*u)=y^*(xv^*u),
\]
and \(xv^*u\in\mathfrak n_\varphi\). Each \(y^*x\) itself belongs to \(\mathfrak n_\varphi\), by the left ideal property, and so does its adjoint. This proves the subalgebra and inclusion statements.

The polarization identity
\[
4y^*x=\sum_{k=0}^{3}i^k(x+i^k y)^*(x+i^k y)
\]
puts every spanning element in \(\operatorname{span}_{\mathbb C}F_\varphi\). Conversely, for \(a\in F_\varphi\), the square root \(a^{1/2}\) lies in \(\mathfrak n_\varphi\), and \(a=(a^{1/2})^*a^{1/2}\). The two spans therefore coincide.

Grouping the positive and negative real and imaginary coefficients of a finite linear combination of members of \(F_\varphi\) gives the four-term decomposition. If an element \(h\) of that span is self-adjoint, averaging a decomposition with its adjoint removes the imaginary part and expresses \(h=a-b\), with \(a,b\in F_\varphi\). If also \(h\geq0\), then \(0\leq h\leq a\), so heredity gives \(h\in F_\varphi\). The reverse inclusion was already established. ∎

Here “hereditary” for the subalgebra refers to its positive cone: if \(0\leq b\leq a\in(\mathfrak m_\varphi)_+\), then \(b\in\mathfrak m_\varphi\). No norm-closedness is asserted.

**Corollary for arbitrary hereditary cones.** Let \(P\subseteq M_+\) be a nonempty cone closed under addition and multiplication by nonnegative scalars, and suppose \(0\leq a\leq b\in P\) implies \(a\in P\). Set
\[
\mathfrak n_P=\{x:x^*x\in P\},\qquad
\mathfrak m_P=\operatorname{span}_{\mathbb C}
\{y^*x:x,y\in\mathfrak n_P\}.
\]
Then \(\mathfrak n_P\) is a left ideal, \(\mathfrak m_P\) is a hereditary *-subalgebra,
\[
\mathfrak m_P=\operatorname{span}_{\mathbb C}P,\qquad
\mathfrak m_P\cap M_+=P,\qquad
\mathfrak m_P\subseteq\mathfrak n_P\cap\mathfrak n_P^*,
\]
and every element of \(\mathfrak m_P\) is a complex linear combination of four members of \(P\).

**Proof.** Define \(\varphi_P(a)=0\) for \(a\in P\) and \(\varphi_P(a)=+\infty\) otherwise. Nonemptiness and the cone property give \(0\in P\). For positive \(a,b\), heredity gives
\[
a+b\in P\quad\Longleftrightarrow\quad a\in P\text{ and }b\in P.
\]
It follows that \(\varphi_P(a+b)=\varphi_P(a)+\varphi_P(b)\), with the extended-value conventions of WG-002. For \(t>0\), \(ta\in P\) is equivalent to \(a\in P\), by applying the cone property also to \(t^{-1}\). This proves homogeneity for \(t>0\); for \(t=0\) it follows from \(0\cdot\infty=0\). Thus \(\varphi_P\) is a weight with \(F_{\varphi_P}=P\). The proposition applied to this weight gives all the stated conclusions. Neither normality nor semifiniteness of this auxiliary weight is claimed. ∎


<a id="OA-MOD-WG-004"></a>
<span id="oa-mod-wg-004-linear-extension-without-infinite-subtraction"></span>
<span id="oa-mod-wg-004"></span>
## OA-MOD-WG-004. Linear extension without infinite subtraction

**Proposition.** There is a unique positive complex-linear functional
\[
\widetilde\varphi:\mathfrak m_\varphi\longrightarrow\mathbb C
\]
whose restriction to \(F_\varphi\) equals \(\varphi\). It satisfies
\(\widetilde\varphi(z^*)=\overline{\widetilde\varphi(z)}\).

**Proof.** For a self-adjoint element \(h=a-b\), with \(a,b\in F_\varphi\), set
\(\widetilde\varphi(h)=\varphi(a)-\varphi(b)\).
If also \(h=c-d\), then \(a+d=c+b\), and additivity gives
\[
\varphi(a)+\varphi(d)=\varphi(c)+\varphi(b).
\]
Every number here is finite. Subtracting proves independence of the decomposition. Addition of decompositions proves additivity on the self-adjoint part; positive scalar multiplication follows from homogeneity, and negative scalar multiplication follows by swapping the two terms. Thus this is a real-linear functional.

Every \(z\in\mathfrak m_\varphi\) has the unique self-adjoint decomposition
\[
z=h+ik,\qquad h=(z+z^*)/2,\quad k=(z-z^*)/(2i).
\]
Define \(\widetilde\varphi(z)=\widetilde\varphi(h)+i\widetilde\varphi(k)\). Real linearity and the transformation \((h,k)\mapsto(-k,h)\) under multiplication by \(i\) prove complex linearity. Positivity follows from OA-MOD-WG-003, because the positive elements of the domain are exactly \(F_\varphi\). The formula for adjoints and uniqueness follow from the same decomposition. ∎

We retain the tilde when a complex argument is present, making the domain visible. A formula such as \(\widetilde\varphi(y^*a x)\) is legitimate for \(x,y\in\mathfrak n_\varphi\), \(a\in M\), because \(ax\in\mathfrak n_\varphi\). It is not legitimate for arbitrary \(x,y\in M\) merely because the product exists.

<a id="OA-MOD-WG-005"></a>
<span id="oa-mod-wg-005-cauchy-schwarz-and-the-null-ideal"></span>
<span id="oa-mod-wg-005"></span>
## OA-MOD-WG-005. Cauchy-Schwarz and the null ideal

**Lemma.** On \(\mathfrak n_\varphi\), the formula
\[
B_\varphi(x,y)=\widetilde\varphi(y^*x)
\]
defines a positive semidefinite sesquilinear form, linear in \(x\), and
\[
|B_\varphi(x,y)|^2
\leq\varphi(x^*x)\varphi(y^*y).
\]
Its null space is the left ideal
\[
N_\varphi=\{x\in M:\varphi(x^*x)=0\}\subseteq\mathfrak n_\varphi.
\]

**Proof.** Sesquilinearity and conjugate symmetry follow from OA-MOD-WG-004; positivity follows from the definition. Put \(A=B_\varphi(x,x)\), \(C=B_\varphi(y,y)\), and \(b=B_\varphi(x,y)\). For every \(t\in\mathbb C\),
\[
0\leq B_\varphi(x+ty,x+ty)
=A+t\overline b+\overline t b+|t|^2C.
\]
If \(C>0\), choose \(t=-b/C\) to obtain \(|b|^2\leq AC\). If \(C=0\) and \(b\neq0\), choosing \(t=-r b\), with \(r>0\), would make the right side \(A-2r|b|^2\), which is eventually negative. Thus \(b=0\) when \(C=0\), proving the inequality in every case.

The inequality shows that a null vector is orthogonal to every element of \(\mathfrak n_\varphi\). Hence sums and scalar multiples of null vectors are null. The estimate from OA-MOD-WG-003 gives
\[
\varphi((ax)^*(ax))\leq\|a\|^2\varphi(x^*x)=0
\quad(x\in N_\varphi),
\]
so \(N_\varphi\) is a left ideal. ∎

<a id="OA-MOD-WG-006"></a>
<span id="oa-mod-wg-006-the-gns-construction-for-an-arbitrary-weight"></span>
<span id="oa-mod-wg-006"></span>
## OA-MOD-WG-006. The GNS construction for an arbitrary weight

Let \(H_\varphi\) be the Hilbert completion of \(\mathfrak n_\varphi/N_\varphi\). Write
\[
\Lambda_\varphi:\mathfrak n_\varphi\to H_\varphi,
\qquad x\mapsto[x].
\]
The preceding lemma proves that the quotient inner product
\[
\langle\Lambda_\varphi(x),\Lambda_\varphi(y)\rangle
=\widetilde\varphi(y^*x)
\]
is well-defined and positive definite. By construction, the range of \(\Lambda_\varphi\) is dense. For \(a\in M\), define initially
\[
\pi_\varphi(a)\Lambda_\varphi(x)=\Lambda_\varphi(ax).
\]
This is well-defined because both domain ideals are left ideals, and
\[
\|\Lambda_\varphi(ax)\|^2
\leq\|a\|^2\|\Lambda_\varphi(x)\|^2.
\]
It therefore extends uniquely to a bounded operator on \(H_\varphi\), with norm at most \(\|a\|\).

**Theorem.** This construction gives a unital *-representation \(\pi_\varphi:M\to B(H_\varphi)\), for every weight. Neither normality, faithfulness, nor semifiniteness is needed for this assertion. The triple \((H_\varphi,\pi_\varphi,\Lambda_\varphi)\) is the GNS semicyclic triple.

**Proof.** Linearity and multiplication hold on the dense range of \(\Lambda_\varphi\), because the left action of \(M\) has these properties. Boundedness extends these identities to all of \(H_\varphi\). For \(x,y\in\mathfrak n_\varphi\),
\[
\begin{aligned}
\langle\pi_\varphi(a)\Lambda_\varphi(x),\Lambda_\varphi(y)\rangle
&=\widetilde\varphi(y^*a x)\\
&=\langle\Lambda_\varphi(x),\pi_\varphi(a^*)\Lambda_\varphi(y)\rangle.
\end{aligned}
\]
Density yields \(\pi_\varphi(a)^*=\pi_\varphi(a^*)\). Finally,
\(\pi_\varphi(1)\Lambda_\varphi(x)=\Lambda_\varphi(x)\), so \(\pi_\varphi(1)=I\). In particular the representation is nondegenerate: \(\overline{\pi_\varphi(M)H_\varphi}=H_\varphi\). When \(H_\varphi=\{0\}\), its identity operator is the zero operator and these statements retain their usual meaning. ∎

**Uniqueness.** Suppose \((H',\pi',\Lambda')\) has a linear map \(\Lambda':\mathfrak n_\varphi\to H'\) with dense range, the same inner-product formula, and \(\pi'(a)\Lambda'(x)=\Lambda'(ax)\), with \(\pi'\) a bounded-operator representation. Then
\(U\Lambda_\varphi(x)=\Lambda'(x)\) defines an isometry on a dense subspace: its well-definedness and norm preservation follow from the shared quadratic form. Its range is dense, so it extends to a unitary. The action identity gives \(U\pi_\varphi(a)=\pi'(a)U\) first on GNS vectors and then everywhere. Density also proves uniqueness of \(U\).

Here “semicyclic” means this representation together with its dense-range module map. Some treatments impose additional closedness conditions when defining an abstract semicyclic object. No such closedness is included silently in the present terminology.

<a id="OA-MOD-WG-007"></a>
<span id="oa-mod-wg-007-normality-is-a-net-argument"></span>
<span id="oa-mod-wg-007"></span>
## OA-MOD-WG-007. Normality is a net argument

**Theorem.** If \(\varphi\) is normal, then \(\pi_\varphi\) is normal. Semifiniteness is not required.

**Proof.** Let \(0\leq a_i\uparrow a\) in \(M\). Strong convergence gives \(x^*a_i x\uparrow x^*a x\) for each fixed \(x\in\mathfrak n_\varphi\). All their weights are finite, since
\[
0\leq x^*a_i x\leq x^*a x\leq\|a\|x^*x.
\]
By normality,
\[
\varphi(x^*a_i x)\uparrow\varphi(x^*a x).
\]
Set \(D_i=\pi_\varphi(a-a_i)\). This is positive, \(0\leq D_i\leq\|a\|I\), and additivity with finite values gives
\[
\langle D_i\Lambda_\varphi(x),\Lambda_\varphi(x)\rangle
=\varphi(x^*a x)-\varphi(x^*a_i x)\longrightarrow0.
\]
Functional calculus gives \(D_i^2\leq\|a\|D_i\). Thus
\[
\|D_i\Lambda_\varphi(x)\|^2
\leq\|a\|\langle D_i\Lambda_\varphi(x),\Lambda_\varphi(x)\rangle
\longrightarrow0.
\]
For an arbitrary \(\xi\in H_\varphi\), approximate \(\xi\) by a GNS vector \(\eta\). The bound
\[
\|D_i\xi\|\leq\|a\|\|\xi-\eta\|+\|D_i\eta\|
\]
proves \(D_i\xi\to0\). Therefore \(\pi_\varphi(a_i)\uparrow\pi_\varphi(a)\) strongly. The bounded-map normality criterion in OA-MOD-WG-001 proves normality. ∎

No sequence was extracted from the given net. The proof does not require a faithful normal state, a countable approximate unit, or a dominated-convergence theorem for the unbounded function \(\varphi\).

<a id="OA-MOD-WG-008"></a>
<span id="oa-mod-wg-008-finite-positive-cutoffs-characterize-semifiniteness"></span>
<span id="oa-mod-wg-008"></span>
## OA-MOD-WG-008. Finite positive cutoffs characterize semifiniteness

**Theorem.** For an arbitrary weight, semifiniteness is equivalent to the existence of an increasing net \((e_i)\) of positive contractions in \(F_\varphi\) with \(e_i\uparrow1\). No normality assumption is needed for this equivalence.

**Proof.** Suppose \(\mathfrak m_\varphi\) is ultraweakly dense. Order \(F_\varphi\) by the operator order; it is directed because \(a+b\) is a common upper bound. For \(a\in F_\varphi\), put
\[
e_a=a(1+a)^{-1}=1-(1+a)^{-1}.
\]
The inverse-order inequality shows that \(a\leq b\) implies \(e_a\leq e_b\). Functional calculus gives \(0\leq e_a\leq1\) and \(e_a\leq a\), so \(e_a\in F_\varphi\). The increasing net has a strong supremum \(e\leq1\).

Fix \(b\in F_\varphi\). Every \(t b\), \(t>0\), is also an index. Spectral calculus gives
\[
e_{tb}=tb(1+tb)^{-1}\uparrow s(b)
\quad(t\to\infty),
\]
because the scalar functions increase to the indicator of \((0,\infty)\). Hence \(e\geq s(b)\). For a positive contraction dominating a projection \(p\), one has \(ep=p\): indeed \(p(1-e)p=0\), so \((1-e)^{1/2}p=0\). Applying this with \(p=s(b)\) gives \(eb=b\). Linearity gives \(ez=z\) for every \(z\in\mathfrak m_\varphi\). Separate ultraweak continuity of multiplication and density give this identity for every \(z\in M\). Setting \(z=1\) proves \(e=1\).

Conversely, suppose finite positive contractions \(e_i\uparrow1\) are given. Since \(e_i^2\leq e_i\), each \(e_i\in\mathfrak n_\varphi\). For \(a\in M\), the left ideal property gives \(a e_i\in\mathfrak n_\varphi\), so
\[
e_i a e_i=e_i^*(a e_i)\in\mathfrak m_\varphi.
\]
These operators converge strongly to \(a\): for \(\xi\in K\),
\[
\|(e_i a e_i-a)\xi\|
\leq\|a\|\|(e_i-1)\xi\|+\|(e_i-1)a\xi\|.
\]
Their norms are bounded by \(\|a\|\), so the convergence is also ultraweak. Thus \(\mathfrak m_\varphi\) is ultraweakly dense. ∎

These cutoffs are generally positive contractions, not projections. The set of all finite-weight projections must not be assumed directed under inclusion.

<a id="OA-MOD-WG-009"></a>
<span id="oa-mod-wg-009-density-of-the-two-sided-finite-domain-in-the-gns-space"></span>
<span id="oa-mod-wg-009"></span>
## OA-MOD-WG-009. Density of the two-sided finite domain in the GNS space

**Theorem.** If \(\varphi\) is normal and semifinite, then
\[
\overline{\Lambda_\varphi(\mathfrak m_\varphi)}
=\overline{\Lambda_\varphi(\mathfrak n_\varphi\cap\mathfrak n_\varphi^*)}
=H_\varphi.
\]
More explicitly, for the cutoffs in OA-MOD-WG-008 and every \(x\in\mathfrak n_\varphi\),
\[
e_a x\in\mathfrak m_\varphi,\qquad
\Lambda_\varphi(e_a x)\longrightarrow\Lambda_\varphi(x)
\quad\text{in Hilbert norm}.
\]

**Proof.** Both \(e_a\) and \(x\) belong to \(\mathfrak n_\varphi\), and \(e_a x=e_a^*x\), proving membership in \(\mathfrak m_\varphi\). Since \(0\leq1-e_a\leq1\),
\[
\begin{aligned}
\|\Lambda_\varphi(x-e_a x)\|^2
&=\varphi\bigl(x^*(1-e_a)^2x\bigr)\\
&\leq\varphi\bigl(x^*(1-e_a)x\bigr)\\
&=\varphi(x^*x)-\varphi(x^*e_a x).
\end{aligned}
\]
The last equality subtracts finite numbers. The operators \(x^*e_a x\) increase strongly to \(x^*x\), so normality makes the final difference tend to zero. Density of \(\Lambda_\varphi(\mathfrak n_\varphi)\) now proves the first assertion, and the inclusion in OA-MOD-WG-003 proves the second. ∎

This proves a dense domain for a prospective involution when the weight is faithful. It does not prove that the involution is closable.

<a id="OA-MOD-WG-010"></a>
<span id="oa-mod-wg-010-faithfulness-and-the-finite-weight-specialization"></span>
<span id="oa-mod-wg-010"></span>
## OA-MOD-WG-010. Faithfulness and the finite-weight specialization

**Proposition.** If \(\varphi\) is faithful and semifinite, then \(\pi_\varphi\) is faithful. Normality is not needed for this particular conclusion.

**Proof.** If \(\pi_\varphi(a)=0\), then for each finite cutoff \(e_i\),
\[
0=\|\pi_\varphi(a)\Lambda_\varphi(e_i)\|^2
=\varphi((a e_i)^*(a e_i)).
\]
Faithfulness gives \(a e_i=0\). Since \(e_i\to1\) strongly in the faithful concrete realization of \(M\), we get \(a=0\). ∎

If \(\varphi(1)<\infty\), then \(\varphi(a)\leq\|a\|\varphi(1)\) for all \(a\in M_+\). Thus \(\mathfrak n_\varphi=\mathfrak m_\varphi=M\), and \(\Omega_\varphi=\Lambda_\varphi(1)\) exists. Its orbit is dense because
\(\pi_\varphi(a)\Omega_\varphi=\Lambda_\varphi(a)\). If the finite weight is also faithful, \(\pi_\varphi\) is faithful and \(\Omega_\varphi\) is separating for \(\pi_\varphi(M)\), since
\[
\pi_\varphi(a)\Omega_\varphi=0
\Longrightarrow\varphi(a^*a)=0
\Longrightarrow a=0.
\]
For an infinite weight, the symbol \(\Lambda_\varphi(1)\) need not be defined. The dense family \(\Lambda_\varphi(\mathfrak n_\varphi)\) is the replacement, and a cyclic vector may not exist at all.

<a id="OA-MOD-WG-011"></a>
