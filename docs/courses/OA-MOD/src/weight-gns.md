# General weights: finite domains, GNS spaces, and normal representations

Course: OA-MOD. Self-checked by the writing AI. The proofs below do not assert completion of the weight-to-Hilbert-algebra correspondence or of modular theory.

This unit constructs the Hilbert space on which relative weight theory will act. Its organizing question is which conclusions use algebraic positivity, which use normality, and which use semifiniteness. Keeping these hypotheses separate prevents an argument for a state from being applied to an infinite weight without its missing domain justification.

## Conventions and precise prerequisite contract

Throughout, \(M\) is a unital von Neumann algebra, represented faithfully and normally on some Hilbert space \(K\). Neither \(K\) nor the predual of \(M\) is assumed separable. All unqualified inner products are linear in their first variable. A bounded increasing net of positive operators has a supremum in \(M_+\); the notation \(a_i\uparrow a\) includes the assertion that \(a\) is that supremum. Its convergence is strong and ultraweak. A sum over an arbitrary index set of nonnegative numbers means the supremum of its finite partial sums.

The bounded prerequisites have the following written programme proofs. The bounded prerequisite boundary proves Hilbert completion, extension from dense subspaces, complex Riesz representation, bounded adjoints, positivity, positive square roots and the continuous calculus for bounded self-adjoint operators. Inversion reverses order proves inverse-order reversal; Bounded increasing positive nets have strong suprema proves monotone convergence for arbitrary bounded positive nets; The ultraweak convergence needed by finite cutoffs proves bounded strong-to-ultraweak convergence and separate ultraweak continuity of fixed multiplication; Supports from bounded resolvent cutoffs constructs support projections and the resolvent cutoffs used below.

The final step of WG-007 also uses the bounded positive-map equivalence in The positive-map equivalence: preserving bounded increasing positive-net suprema is equivalent to ultraweak continuity. Its scalar converse is proved in The scalar normality criterion from The full characterization, using norm approximation by dominated predual functionals. NW-11 uses only the algebraic GNS construction WG-003–006, so this route does not assume the representation normality being proved. The algebraic GNS construction in WG-002–006 and the bounded weight comparison in DW do not use it.

For the models, SS1 proves \(L^2\) completeness on every measure space, including weighted counting measure on an arbitrary set. If \(\sum_j w_j|\xi_j|^2<\infty\), a finite partial sum within \(\varepsilon^2\) of its supremum gives a finite-coordinate approximation with norm error at most \(\varepsilon\). This proves the finite-support density used below without countability of the whole index set. To realize \(\ell^\infty(I)\) as a von Neumann algebra on \(\ell^2(I)\), note that an operator commuting with every coordinate projection is diagonal: its value on \(e_i\) is a scalar multiple of \(e_i\), and these scalars are bounded by its norm. Finite-support density gives the same formula on all vectors. Every bounded diagonal family is a multiplier, so this multiplication algebra is its own commutant.

The exponential in the final shift example is constructed in Logarithms and imaginary powers. The series estimates can be checked directly. For \(n\ge2\), \(n^{-2}\le(n-1)^{-1}-n^{-1}\), so the reciprocal-square series converges. If \(0<r<1\), the finite geometric sum is \(r(1-r^N)/(1-r)\); writing \(r=(1+\delta)^{-1}\) gives \(r^N\le(1+N\delta)^{-1}\to0\). In particular \(e^{-n^2}\le e^{-n}\) is summable, whereas \(e^{2n+1}\) is unbounded since the positive-term exponential series gives \(e^{2n+1}\ge 1+2n+1\).

No closability theorem or lower-semicontinuity theorem for extended-valued weights is included in these bounded inputs.

## The finite part of an extended-valued weight

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

## Domain algebra and its positive cone

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

## Linear extension without infinite subtraction

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

## Cauchy-Schwarz and the null ideal

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

## The GNS construction for an arbitrary weight

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

## Normality is a net argument

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

proves \(D_i\xi\to0\). Therefore \(\pi_\varphi(a_i)\uparrow\pi_\varphi(a)\) strongly. The proved positive-map equivalence The positive-map equivalence now gives ultraweak continuity, hence normality. ∎

No sequence was extracted from the given net. The proof does not require a faithful normal state, a countable approximate unit, or a dominated-convergence theorem for the unbounded function \(\varphi\).

## Finite positive cutoffs characterize semifiniteness

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

## Density of the two-sided finite domain in the GNS space

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

## Faithfulness and the finite-weight specialization

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

## An uncountable model with no cyclic vector

Let \(I\) be an uncountable set and choose real numbers \(0<w_j<\infty\) for \(j\in I\). On \(M=\ell^\infty(I)\), set

\[
\varphi(f)=\sum_{j\in I}w_j f(j),\qquad f\geq0.
\]

This is a faithful normal semifinite weight. Additivity follows by taking finite partial sums: to approximate two suprema simultaneously, take the union of two finite index sets. For normality, a bounded increasing net in \(\ell^\infty(I)_+\) has pointwise supremum, and

\[
\sup_\alpha\sup_{F\subset I\text{ finite}}
\sum_{j\in F}w_jf_\alpha(j)
=\sup_{F\subset I\text{ finite}}\sup_\alpha
\sum_{j\in F}w_jf_\alpha(j).
\]

For a fixed finite \(F\), an increasing net commutes with the finite sum; this proves normality. Faithfulness follows because each \(w_j\) is positive. The finite-support projections \(1_F\) have finite weight and increase strongly to \(1\) in the diagonal representation on \(\ell^2(I)\); OA-MOD-WG-008 proves semifiniteness.

Directly from the definitions,

\[
\mathfrak n_\varphi
=\left\{f\in\ell^\infty(I):\sum_jw_j|f(j)|^2<\infty\right\},
\qquad
H_\varphi=\ell^2(I,w),
\]

with \(\Lambda_\varphi\) the inclusion and \(\pi_\varphi\) multiplication. Finite-support functions lie in the domain and are dense in the weighted Hilbert space, proving this identification.

Every vector \(\xi\in\ell^2(I,w)\) has countable support. Indeed, for each positive integer \(n\), the set where \(w_j|\xi(j)|^2\geq1/n\) is finite, and their union contains its support. Multiplication cannot enlarge support. Choose an index outside this countable set; the vector supported there is orthogonal to the whole orbit of \(\xi\). No vector is cyclic. The semicyclic construction nevertheless gives the faithful normal representation proved above.

## Nonfaithful weights and an undefined quotient involution

For \(M=M_2(\mathbb C)\), let \(\varphi(a)=a_{11}\) on positive matrices. Then \(\mathfrak n_\varphi=M\) and

\[
N_\varphi=\{x:xe_1=0\},\qquad
H_\varphi\cong\mathbb C^2,\qquad
\Lambda_\varphi(x)=xe_1.
\]

The inner-product identity follows from
\(\varphi(y^*x)=\langle xe_1,ye_1\rangle\); every vector is the first column of a matrix, giving surjectivity. Under this identification \(\pi_\varphi(a)\) is the usual matrix action, so the representation is faithful although the weight is not.

Let \(E_{ij}\) denote the matrix units. Then

\[
\Lambda_\varphi(E_{12})=0,
\qquad
\|\Lambda_\varphi(E_{12}^*)\|^2
=\varphi(E_{12}E_{21})=1.
\]

Consequently the expression
\(\Lambda_\varphi(x)\mapsto\Lambda_\varphi(x^*)\)
does not define an operator on this quotient, even though all matrices and their adjoints lie in the GNS domain. Nonfaithful weights require a support reduction or an appropriately formulated relative construction before introducing a Tomita operator.

## Semifiniteness does not supply finite subelements in each corner

Let \((u_n)_{n\geq1}\) be the usual orthonormal basis of \(\ell^2(\mathbb N)\), and define on \(B(\ell^2)_+\)

\[
\varphi(a)=\sum_{n\geq1}n^2\langle a u_n,u_n\rangle.
\]

This is a normal weight: additivity follows from nonnegative sums, and for a bounded increasing positive net, each diagonal coefficient increases to its limiting value; interchanging the supremum over that net with the supremum of finite sums proves normality. It is faithful, since vanishing of every positive diagonal coefficient implies \(a^{1/2}u_n=0\) for every \(n\), and hence \(a=0\). The projections onto the first \(N\) basis vectors have finite weight and increase strongly to \(1\), proving semifiniteness by OA-MOD-WG-008.

Choose \(c>0\) so that \(v=\sum_{n\geq1}(c/n)u_n\) is a unit vector, and let \(q\) be its rank-one projection. Then

\[
\varphi(q)=\sum_{n\geq1}n^2(c^2/n^2)=\infty.
\]

If \(0\leq b\leq q\), then \(b\) annihilates \((1-q)\ell^2\), because \(\|b^{1/2}\xi\|^2\leq\langle q\xi,\xi\rangle=0\) there. Thus \(b=q b q=tq\), with \(0\leq t\leq1\). Every nonzero such \(b\) has infinite weight. The weight is nonetheless faithful, normal, and semifinite.

The finite-domain density in this unit is density in the entire algebra. It is not an assertion about the finite-weight part below each prescribed positive element.

## Problems and solutions

**Problem 1: normal and faithful can still give a zero GNS space.** On a nonzero von Neumann algebra, define \(\psi(0)=0\) and \(\psi(a)=\infty\) for every nonzero \(a\geq0\). Determine which hypotheses above it satisfies and compute its GNS triple.

**Solution.** The sum of two positive operators is zero exactly when both are zero, so additivity holds in the extended nonnegative reals; homogeneity holds with the stated convention. The weight is faithful. If \(a_i\uparrow a\neq0\), at least one \(a_i\neq0\), and hence \(\sup_i\psi(a_i)=\infty=\psi(a)\); if \(a=0\), all terms are zero. Thus it is normal. Its finite cone and both finite domains are \(\{0\}\), so it is not semifinite. Its GNS Hilbert space is zero and its representation is zero. This shows exactly why faithfulness of the weight alone does not make the representation faithful.

**Problem 2: a dense-range GNS map need not be injective.** On \(\ell^\infty(I)\), for an arbitrary set \(I\), put \(\chi(f)=0\) for every \(f\geq0\). Compute the domains and distinguish density of the GNS map from injectivity.

**Solution.** Both domains are all of \(M\), while \(N_\chi=M\) and \(H_\chi=\{0\}\). The GNS map has dense range and is bounded, but is not injective if \(M\neq0\). The weight is finite, normal, and semifinite, and is faithful only for the zero algebra. Compare this full-domain example with Problem 1, where the same zero Hilbert space arises from the domain \(\{0\}\). Density of a map's range alone therefore supplies neither injectivity nor a substantial domain.

**Problem 3: right multiplication need not be bounded in GNS norm.** On \(B(\ell^2(\mathbb N))\), let

\[
\rho(a)=\sum_{n\geq1}e^{-n^2}\langle a u_n,u_n\rangle,
\]

and let \(S u_n=u_{n+1}\). Show that \(x\mapsto xS\), though defined on all of \(\mathfrak n_\rho=M\), has no bounded extension to \(H_\rho\).

**Solution.** The same positive-sum argument as in OA-MOD-WG-013 proves normality and faithfulness. Since \(\rho(1)=\sum_ne^{-n^2}<\infty\), its domain is all of \(M\). Write \(p_n\) for the projection onto \(\mathbb C u_n\). Then

\[
\|\Lambda_\rho(p_{n+1})\|^2=e^{-(n+1)^2},
\qquad
\|\Lambda_\rho(p_{n+1}S)\|^2=e^{-n^2}.
\]

The squared ratio is \(e^{2n+1}\), unbounded in \(n\). A bounded extension would bound all these ratios by its squared norm, a contradiction. Faithfulness makes the algebraic map well-defined on \(\Lambda_\rho(M)\), but does not make it bounded. The bounded action proved in OA-MOD-WG-006 is the left action.

**Problem 4: cutoff convergence for coefficients.** Assume \(\varphi\) is normal and semifinite. For \(x,y\in\mathfrak n_\varphi\), \(a\in M\), and the cutoffs of OA-MOD-WG-008, prove

\[
\widetilde\varphi(y^*a e_i x)
\longrightarrow\widetilde\varphi(y^*a x).
\]

Identify why all displayed arguments belong to the linear extension's domain.

**Solution.** Both \(e_i x\) and \(x\) lie in \(\mathfrak n_\varphi\), and the left ideal property puts \(a e_i x\) and \(a x\) there as well. Pairing with \(y\in\mathfrak n_\varphi\) therefore produces members of \(\mathfrak m_\varphi\). Cauchy-Schwarz, the left-action estimate, and OA-MOD-WG-009 give

\[
\begin{aligned}
|\widetilde\varphi(y^*a(e_i x-x))|
&\leq\|\Lambda_\varphi(y)\|
\|\Lambda_\varphi(a(e_i x-x))\|\\
&\leq\|\Lambda_\varphi(y)\|\,\|a\|\,
\|\Lambda_\varphi(e_i x-x)\|\longrightarrow0.
\end{aligned}
\]

This proves the convergence without claiming that an extended-valued weight is an ultraweakly continuous scalar functional.

## Exported facts and remaining analytic boundary

The unit exports the ideals \(\mathfrak n_\varphi,N_\varphi,\mathfrak m_\varphi\), the finite linear extension, its Cauchy-Schwarz inequality, the semicyclic triple and its unitary uniqueness, normality of \(\pi_\varphi\), finite positive cutoffs, density of the two-sided finite domain in GNS norm, and the faithful-representation criterion. All claims retain the hypotheses stated at their own anchors.

For a faithful normal semifinite weight, injectivity of \(\Lambda_\varphi\) and OA-MOD-WG-009 make

\[
S_0:\Lambda_\varphi(\mathfrak n_\varphi\cap\mathfrak n_\varphi^*)
\longrightarrow H_\varphi,
\qquad S_0\Lambda_\varphi(x)=\Lambda_\varphi(x^*)
\]

a well-defined densely defined conjugate-linear operator. To check that it is conjugate-linear, use conjugate-linearity of the adjoint and linearity of \(\Lambda_\varphi\); faithfulness removes representative ambiguity. The present unit stops at that assertion. Closability of \(S_0\), the closedness properties of \(\Lambda_\varphi\), weight lower semicontinuity, Hilbert-algebra axioms, and the modular polar decomposition require further theorems. In particular no modular automorphism, standard form, relative modular operator, or spatial derivative is constructed by the preceding domain argument alone.

**Free source comparisons.** Brent Nelson's [*Tomita–Takesaki Theory*](https://users.math.msu.edu/users/banelson/files/Tomita-Takesaki%20Theory.pdf), Definition 3.1 and Lemma 3.2, printed pp. 19–20, treat the hereditary finite cone and its algebraic domains. The discussion before Proposition 3.4 and Definition 3.5, p. 20, describes the semicyclic representation. Those passages leave parts of the GNS argument brief; WG-004–006 supplies the finite linear extension, null-ideal quotient, bounded left action, adjoint identity and unitary uniqueness in full. Proposition 3.4 is not a substitute for WG-007's net argument or its bounded-map prerequisite.

Jacob Lurie's [2011 Math 261y, Lecture 34](https://people.math.harvard.edu/~lurie/261ynotes/lecture34.pdf), Construction 5, p. 3, is a second free comparison for the weight GNS construction. For nonfaithful weights the quotient by the null space must be explicit, as it is here. The stronger finite-subelement convention in that lecture is not substituted for finite-domain density; WG-013 proves why those conditions differ. These references are comparisons with freely readable work, not replacements for the proofs above.
