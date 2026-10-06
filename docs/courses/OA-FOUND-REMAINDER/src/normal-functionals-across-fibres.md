# Normal functionals across fibres

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

A normal functional on a direct integral can be evaluated separately on its fibres and then integrated. Its norm is the integral of the fibre norms. The fibres need not be copies of one algebra, and their dimensions may vary. Two countable families make the proof possible: operators that detect the norm of every fibre functional, and finite vector functionals that approximate every fibre predual.

Prerequisites are [Measurable fields and direct integrals](../reader/supplements/measurable-fields-direct-integrals.html), [Direct integrals of von Neumann algebras](../reader/supplements/direct-integrals-of-von-neumann-algebras-commutants-and-centres-takesa.html), and [Compact and trace-class operators, preduals and operator topologies](../../foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.html). We use Theorem 9.1(ii) of the last lesson: a normal functional on an operator subspace has a normal extension to \(B(H)\), and is a sum of vector functionals with square-summable vector sequences. For positive functionals we use Theorem 10.1 of [The double commutation theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html). The constant-fibre version is already treated in [Vector-valued functions and preduals](../reader/normal-functionals-across-fibres.html#4-every-normal-functional-has-a-unique-field), Theorem 9.1; here the algebra and its predual can vary with the point. Basic measure-theoretic tools are Tonelli, dominated convergence and Cauchy–Schwarz. The linked programme proofs and the selection construction in Section 1 supply the prerequisites. Effros’s freely readable paper treats Borel selectors, and Takesaki’s book provides further context for direct integrals.

Let \((X,\Sigma,\mu)\) be a sigma-finite measure space, let \(H(x)\) be a measurable field of separable Hilbert spaces, and let \(M(x)\subseteq B(H(x))\) be a measurable field of von Neumann algebras. Put
\[
\mathcal H=\int_X^\oplus H(x)\,d\mu(x),
\qquad M=\int_X^\oplus M(x)\,d\mu(x).
\]
Neither standardness of the base nor separability of \(\mathcal H\) is needed in this lesson. Zero fibres are allowed. All functional fields are taken modulo equality almost everywhere.

## 1. Measurable fields in the preduals

A field \(\varphi(x)\in M(x)_*\) is **measurable** if
\[
x\longmapsto\varphi(x)(a(x))
\]
is measurable for every measurable operator field \(a(x)\in M(x)\). The operator field may have unbounded norm; each \(a(x)\) is nevertheless a bounded operator on its own fibre.

Choose measurable contractions \(a_n(x)\in M(x)\) whose values are ultraweakly dense in \(M(x)_1\) at every retained point. Here is the precise provider and treatment of the null set. [Proposition 1.3(1)–(2)](../reader/supplements/direct-integrals-of-von-neumann-algebras-commutants-and-centres-takesa.html#1-measurable-fields-of-von-neumann-algebras) repairs the given field on one measurable null set to a family generated at every point. [Theorem 10.3(1)–(2)](../reader/supplements/effros-borel-structure.html#oa-fnd-ef-10) constructs its unit-ball selectors by embedding each fibre isometrically in one separable Hilbert space, adjoining scalars on the orthogonal complement, choosing from that fixed-space algebra and compressing back. Compression maps its unit ball onto the fibre unit ball. The actual fixed-space choice proof is [Lemma 5.1 and Theorem 5.3](../reader/supplements/effros-borel-structure.html#oa-fnd-ef-04): extend a functional one real dimension at a time, approximate \(sg\), \(0<s<1\), by rational choice parameters using the interior estimate, and then let \(s\uparrow1\); realification handles complex scalars. Thus the density argument does not assume continuity at boundary functionals. Replace every selector by zero on the one original measurable null set. Its values then belong to the original \(M(x)\) everywhere, and are dense at every point outside that set. This works over the stated arbitrary sigma-finite base and includes variable and zero fibre dimensions; it does not require a selector of a general analytic relation. In particular,
\[
\|\varphi(x)\|=\sup_n|\varphi(x)(a_n(x))|.
\tag{1.1}
\]
Thus the norm function of a measurable normal-functional field is measurable. We call the field **integrable** if
\[
\|\varphi\|_1=\int_X\|\varphi(x)\|\,d\mu(x)<\infty.
\tag{1.2}
\]
Write \(L^1(X;M(x)_*)\) for the resulting space. This notation describes varying Banach spaces, rather than a Bochner space with one fixed target.

**Lemma 1.1.** This is a Banach space. If \(\varphi,\psi\) are measurable fields, the function \(x\mapsto\|\varphi(x)-\psi(x)\|\) is measurable.

**Proof.** The distance assertion follows from (1.1) applied to the difference field. For completeness, take a Cauchy sequence and a subsequence \(\varphi_j\) satisfying
\[
\sum_j\|\varphi_{j+1}-\varphi_j\|_1<\infty.
\]
Tonelli shows that the sum of the pointwise norms of these differences is finite almost everywhere. At every such point the sequence converges in the Banach space \(M(x)_*\), to a functional \(\varphi(x)\). Set it equal to zero on the exceptional set. For any measurable operator field \(a(x)\), the evaluations \(\varphi_j(x)(a(x))\) converge pointwise to \(\varphi(x)(a(x))\), so the limit field is measurable. Furthermore,
\[
\|\varphi(x)\|\leq\|\varphi_1(x)\|
+\sum_j\|\varphi_{j+1}(x)-\varphi_j(x)\|,
\]
an integrable bound. The tails of this sum give convergence of the subsequence in the norm (1.2). The original Cauchy sequence then converges to the same limit. \(\square\)

## 2. Integration and the exact norm

For an integrable field define
\[
J\varphi(a)=\int_X\varphi(x)(a(x))\,d\mu(x),
\qquad a=\int_X^\oplus a(x)\,d\mu(x)\in M.
\tag{2.1}
\]
The choice of representative does not affect this number.

**Proposition 2.1.** The map \(J:L^1(X;M(x)_*)\to M^*\) is linear and isometric:
\[
\|J\varphi\|=\int_X\|\varphi(x)\|\,d\mu(x).
\tag{2.2}
\]

**Proof.** The integrand is measurable and absolutely integrable, since almost everywhere
\[
|\varphi(x)(a(x))|\leq\|\varphi(x)\|\|a(x)\|
\leq\|\varphi(x)\|\|a\|.
\]
This proves well-definedness, linearity and the inequality \(\|J\varphi\|\leq\|\varphi\|_1\).

For the reverse inequality, choose a strictly positive measurable weight \(w\) with \(\int_Xw\,d\mu<\infty\); the sigma-finite weight construction is Lemma 3.1 of [Decomposable operators and the diagonal algebra](../reader/supplements/decomposable-operators-diagonal-algebra.html). Fix \(\varepsilon>0\). At each point let \(n(x)\) be the first integer satisfying
\[
|\varphi(x)(a_{n(x)}(x))|>\|\varphi(x)\|-\varepsilon w(x).
\]
It exists by (1.1), and its level sets are measurable. Put \(z(x)=\varphi(x)(a_{n(x)}(x))\), and define a scalar
\[
c(x)=
\begin{cases}\overline{z(x)}/|z(x)|,&z(x)\neq0,\\
1,&z(x)=0.
\end{cases}
\]
The operator field \(b(x)=c(x)a_{n(x)}(x)\) is measurable: it is formed from countably many measurable pieces and a measurable scalar multiplier. It belongs to \(M(x)_1\), so its direct integral \(b\) belongs to \(M_1\). Its evaluation is real and nonnegative, and
\[
J\varphi(b)=\int_X|z(x)|\,d\mu(x)
\geq\|\varphi\|_1-\varepsilon\int_Xw\,d\mu.
\]
Let \(\varepsilon\downarrow0\). This proves (2.2). No assertion about a measurable polar decomposition was needed. \(\square\)

In particular, a field whose integral functional is zero is zero almost everywhere. Cancellation of its evaluation on the identity alone would not give that conclusion.

## 3. Why the integrated functional is normal

We first identify a countable stock of approximating fields. Choose a measurable orthonormal basis sequence \(e_k(x)\), allowing \(e_k(x)=0\) where the fibre dimension is less than \(k\). Enumerate all finite sums
\[
\psi_m(x)=\sum_{i,j\leq N_m}c^{(m)}_{ij}
\omega_{e_i(x),e_j(x)}|_{M(x)},
\qquad c^{(m)}_{ij}\in\mathbb Q+i\mathbb Q,
\tag{3.1}
\]
including zero. Here \(\omega_{\xi,\eta}(a)=\langle a\xi,\eta\rangle\), with inner products linear in the first variable. Every \(\psi_m\) is a measurable normal-functional field.

**Lemma 3.1.** For every \(x\), the values \(\{\psi_m(x):m\geq1\}\) are norm dense in \(M(x)_*\).

**Proof.** A normal functional on \(M(x)\) extends normally to \(B(H(x))\), by Theorem 9.1(ii) of the operator-topology lesson. On \(B(H(x))\) it is represented by a trace-class operator. Compressing that operator to the first \(N\) basis vectors converges in trace norm: this holds first for finite-rank operators, by convergence on their finitely many defining vectors, and then for arbitrary trace-class operators by finite-rank approximation and contractivity of compression. Finite matrix coefficients can be approximated by rational complex coefficients in trace norm. Under trace duality these give finite rational sums of the matrix vector functionals in (3.1). Restriction to \(M(x)\) is contractive, so the restricted sums converge in its predual norm as well. \(\square\)

**Theorem 3.2.** Every functional \(J\varphi\) in (2.1) is normal.

**Proof.** Fix \(\varepsilon>0\) and a positive integrable weight \(w\) as above. By Lemma 3.1, at each point there is an \(m\) with
\[
\|\varphi(x)-\psi_m(x)\|<\varepsilon w(x).
\]
The norm on the left is measurable by (1.1), because it is the supremum of countably many measurable evaluations. Thus we can choose the first such \(m=m(x)\) measurably, and define \(\varphi_\varepsilon(x)=\psi_{m(x)}(x)\). Then
\[
\|\varphi-\varphi_\varepsilon\|_1
\leq\varepsilon\int_Xw\,d\mu,\qquad
\|\varphi_\varepsilon(x)\|\leq\|\varphi(x)\|+\varepsilon w(x).
\tag{3.2}
\]
It remains to prove \(J\varphi_\varepsilon\) is normal.

Let \(F_N\uparrow X\) be measurable sets of finite measure. Truncate the selected field to
\[
\varphi_{\varepsilon,N}(x)
=1_{F_N}(x)1_{\{m(x)\leq N\}}\,\varphi_\varepsilon(x).
\]
This is a finite sum of fields \(1_E\psi_m\), where \(\mu(E)<\infty\). Each such field integrates to a finite sum of vector functionals on \(\mathcal H\), because \(1_Ee_i\in\mathcal H\) and
\[
\int_E\langle a(x)e_i(x),e_j(x)\rangle\,d\mu(x)
=\langle a(1_Ee_i),1_Ee_j\rangle.
\]
Hence \(J\varphi_{\varepsilon,N}\) is normal. Dominated convergence applied to the integrable bound in (3.2) gives \(\|\varphi_{\varepsilon,N}-\varphi_\varepsilon\|_1\to0\). By Proposition 2.1 their integral functionals converge in norm. The normal functionals form a norm-closed subspace of \(M^*\), so \(J\varphi_\varepsilon\) is normal. Finally (3.2) and \(\varepsilon\downarrow0\) give \(J\varphi\) as a norm limit of normal functionals. \(\square\)

The finite-measure truncation matters. The basis fields are pointwise bounded, but need not be square integrable on an infinite-measure base. Restricting them to finite-measure sets turns the fibre vector expressions into vector functionals on the integral Hilbert space.

## 4. Every normal functional has a unique field

**Theorem 4.1.** Integration is an isometric isomorphism
\[
J:L^1(X;M(x)_*)\longrightarrow M_*.
\tag{4.1}
\]
Equivalently, every \(\omega\in M_*\) has a unique integrable measurable field \(\omega_x\in M(x)_*\) such that
\[
\omega(a)=\int_X\omega_x(a(x))\,d\mu(x),\qquad
\|\omega\|=\int_X\|\omega_x\|\,d\mu(x).
\tag{4.2}
\]

**Proof.** Only surjectivity remains. By the normal-functional representation theorem, there are vectors \(\xi_k,\eta_k\in\mathcal H\) with
\[
\omega(a)=\sum_k\langle a\xi_k,\eta_k\rangle,\qquad
\sum_k\|\xi_k\|^2<\infty,\quad
\sum_k\|\eta_k\|^2<\infty.
\]
Choose measurable representatives. Tonelli implies that the sums of their squared pointwise norms are finite almost everywhere. At every such point define
\[
\omega_x=\sum_k\omega_{\xi_k(x),\eta_k(x)}|_{M(x)}.
\tag{4.3}
\]
Cauchy–Schwarz makes this series absolutely convergent in the predual norm, and
\[
\int_X\|\omega_x\|\,d\mu(x)
\leq\sum_k\int_X\|\xi_k(x)\|\|\eta_k(x)\|\,d\mu(x)
\leq
\Big(\sum_k\|\xi_k\|^2\Big)^{1/2}
\Big(\sum_k\|\eta_k\|^2\Big)^{1/2}<\infty.
\]
The finite partial sums of (4.3) evaluate measurably on every measurable operator field. Their pointwise norm convergence shows the same for the limit, including on operator fields with unbounded norm. Thus the field is measurable. For \(a\in M\), the displayed integrable bound times \(\|a\|\) permits interchange of the sum and the integral, giving \(\omega=J(\omega_x)\). The norm identity and uniqueness follow from Proposition 2.1. \(\square\)

**Corollary 4.2.** A normal functional on \(M\) is positive if and only if its field is positive almost everywhere. In that case
\[
\|\omega\|=\omega(1)=\int_X\omega_x(1_{H(x)})\,d\mu(x).
\]

**Proof.** A positive field integrates to a positive functional. Conversely, a positive normal functional is a sum of positive vector functionals with square-summable vectors, by Theorem 10.1 of the double-commutation lesson. Constructing its field as in (4.3), now with \(\eta_k=\xi_k\), produces a positive field. Uniqueness in Theorem 4.1 identifies it with the original field. The last identity uses the norm formula for positive functionals on unital C*-algebras. \(\square\)

**Corollary 4.3.** Replace \(\mu\) by an equivalent sigma-finite measure \(\nu=h\mu\), with \(0<h<\infty\) almost everywhere, and identify the two integral algebras by the scalar change-of-measure unitary. If \(\omega_x\) represents a normal functional using \(\mu\), its field using \(\nu\) is \(h(x)^{-1}\omega_x\). Its integrated norm is unchanged.

**Proof.** Scalar change of measure leaves the fibre algebra actions unchanged. For every bounded measurable algebra field,
\[
\int_Xh^{-1}\omega_x(a(x))\,d\nu
=\int_X\omega_x(a(x))\,d\mu.
\]
The new field is measurable and integrable, with \(\int\|h^{-1}\omega_x\|\,d\nu=\int\|\omega_x\|\,d\mu\). Uniqueness gives the claim. \(\square\)

## 5. Exercises with complete solutions

**Exercise 5.1 — A norming field with varying dimensions (intermediate).** On \([0,1]\) with Lebesgue measure take \(M(x)=\mathbb C\) for \(0\leq x<1/2\) and \(M(x)=M_2(\mathbb C)\) for \(1/2\leq x\leq1\). Define
\[
\varphi_x(a)=
\begin{cases}
e^{2\pi ix}a,&x<1/2,\\
\operatorname{Tr}\!\left(\operatorname{diag}(2x-1,-(1-x))a\right),&x\geq1/2.
\end{cases}
\]
Compute the norm of its integral functional and its evaluation on \(1\). Give a unitary field attaining the norm. Is the functional positive?

**Solution.** On the scalar part the fibre norm is one. On the matrix part trace duality gives the norm as the sum of the absolute diagonal entries, namely \(x\). Therefore
\[
\|J\varphi\|=\frac12+\int_{1/2}^1x\,dx=\frac78.
\]
Its identity evaluation is
\[
\int_0^{1/2}e^{2\pi ix}\,dx+\int_{1/2}^1(3x-2)\,dx
=\frac{i}{\pi}+\frac18.
\]
The field \(u(x)=e^{-2\pi ix}\) on the first part and \(u(x)=\operatorname{diag}(1,-1)\) on the second is measurable and unitary; \(\varphi_x(u(x))=\|\varphi_x\|\), so \(J\varphi(u)=7/8\). The functional is not positive: its identity evaluation is not real, and the second diagonal direction also has negative density on the interior of the matrix interval.

**Exercise 5.2 — Reweighting a finite base (basic).** On \(X=\{0,1\}\), give the points masses \(2,3\). Let \(M(0)=M_2(\mathbb C)\), \(M(1)=\mathbb C\), and take \(\varphi_0(a)=\operatorname{Tr}(\operatorname{diag}(1,-4)a)\), \(\varphi_1(z)=2iz\). Compute the integrated norm. Find the representing field when the masses are changed to \(5,1\).

**Solution.** The two fibre norms are \(5,2\); the integrated norm is \(2\cdot5+3\cdot2=16\). The new-to-old density is \(h(0)=5/2,h(1)=1/3\). The new field is \((2/5)\varphi_0\) at \(0\), and \(3\varphi_1\), or \(z\mapsto6iz\), at \(1\). Its norm integral is \(5\cdot2+1\cdot6=16\), as required.

**Exercise 5.3 — Local tests and uniqueness (advanced).** Let \(a_n\) be the measurable norm-detecting sequence in (1.1). Show that two integrable fields are equal almost everywhere if their integral functionals agree on every \(1_Ea_n\), for measurable \(E\subseteq X\) and every \(n\). Explain why testing only the identity cannot replace these tests.

**Solution.** Let \(\delta_x\) be the difference. For each \(n\), the scalar function \(g_n(x)=\delta_x(a_n(x))\) is integrable. The assumption gives \(\int_Eg_n\,d\mu=0\) for every measurable \(E\), hence \(g_n=0\) almost everywhere; apply this to real and imaginary parts, or to their positive and negative level sets. Discard the union of the exceptional sets for all \(n\). Equation (1.1) gives \(\|\delta_x\|=\sup_n|g_n(x)|=0\) there. For a scalar counterexample to the identity-only test, take density \(1\) on \([0,1/2)\) and \(-1\) on \([1/2,1]\). Its integral evaluation on \(1\) is zero, while its field has norm one almost everywhere and its integral functional has norm one.

## References

[Effros] E. G. Effros, *The Borel space of von Neumann algebras on a separable Hilbert space*, Pacific Journal of Mathematics 15 (1965), 1153–1164. [Freely accessible paper](https://msp.org/pjm/1965/15-4/pjm-v15-n4-p07-s.pdf).

[Takesaki] M. Takesaki, *Theory of Operator Algebras I*, Springer, 1979.
