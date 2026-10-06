# Finite domains and the GNS space of a C*-weight

*GPT-6 Sol (OpenAI), Codex writing thread, Ultra effort, September 2026. New original prose: CC0. This lesson is a draft awaiting course-level mathematical review.*

A positive functional is finite everywhere, but a weight can take the value \(+\infty\). Its GNS construction must therefore begin with the elements whose squares have finite weight. We work with any complex \(C^*\)-algebra, including the zero and nonunital cases, and use inner products linear in the first variable. The free comparison is [Kustermans–Vaes, *Weight theory for C*-algebraic quantum groups*, §1.1, Definitions 1.1–1.2 and the intervening finite-domain discussion, page 4](https://arxiv.org/abs/math/9901063). The elementary construction below applies to every weight; it does not assume the proper-weight hypotheses used later in that paper. The order and square-root inputs are proved in AC1–4 and UZ06–07. BK01 constructs the Hilbert completion, bounded extensions and adjoints. The current reconstruction and additional details are by GPT-6 Astra (OpenAI), Ultra, October 2026, CC0; the earlier credit is retained.

## The algebra of finite elements

A weight \(\varphi:A_+\to[0,\infty]\) is additive and homogeneous for nonnegative scalars, with \(0\cdot\infty=0\). Define

\[
F_\varphi=\{a\in A_+:\varphi(a)<\infty\},\qquad
\mathfrak n_\varphi=\{x\in A:x^*x\in F_\varphi\},\qquad
\mathfrak m_\varphi=\operatorname{span}_{\mathbb C}F_\varphi.
\tag{CS.1}
\]

Additivity makes \(\varphi\) monotone: if \(0\leq b\leq a\), then
\(\varphi(a)=\varphi(b)+\varphi(a-b)\).
Consequently \(F_\varphi\) is a hereditary cone, stable under finite positive sums. The operator inequalities

\[
(x+y)^*(x+y)\leq2x^*x+2y^*y,\qquad
x^*a^*ax\leq\|a\|^2x^*x
\tag{CS.2}
\]

show that \(\mathfrak n_\varphi\) is a linear left ideal. To justify the inequalities in the abstract algebra, the difference in the first is \((x-y)^*(x-y)\geq0\). For the second, AC4 gives \(a^*a\leq\|a\|^2 1\) in the forced unitization, and conjugation by \(x\) preserves order. Both resulting elements lie in the original algebra, whose cone is inherited by UZ07. Scalar multiplication preserves the finite domain because \((\lambda x)^*(\lambda x)=|\lambda|^2x^*x\), including the zero scalar.

There is a unique positive complex-linear extension \(\varphi_0\) of \(\varphi\) to \(\mathfrak m_\varphi\). On the real span of \(F_\varphi\), set
\(\varphi_0(a-b)=\varphi(a)-\varphi(b)\).
If \(a-b=c-d\), then \(a+d=c+b\), so additivity gives the same value from both presentations. Complexification gives a linear functional. If \(a-b\geq0\), then \(0\leq a-b\leq a\), making \(a-b\) finite and \(\varphi_0(a-b)=\varphi(a-b)\geq0\). This proves positivity, not just well-definedness. Every self-adjoint element in the complex span of the finite cone is in its real span: take the real part of any finite complex linear combination. Combining its nonnegative and negative real coefficients writes it as \(a-b\) with \(a,b\in F_\varphi\). The argument just given therefore proves the exact identity \(\mathfrak m_\varphi\cap A_+=F_\varphi\), and also verifies that the complex extension has the unique required values on every positive element of its domain.

Finite squares and polarization yield

\[
\mathfrak m_\varphi
=\operatorname{span}_{\mathbb C}
\{y^*x:x,y\in\mathfrak n_\varphi\}.
\tag{CS.3}
\]

One inclusion follows by polarizing \((x+\lambda y)^*(x+\lambda y)\). For the other, \(a\in F_\varphi\) has \(a^{1/2}\in\mathfrak n_\varphi\) and \(a=(a^{1/2})^*a^{1/2}\). The product
\((x^*y)(u^*v)=x^*(yu^*v)\)
is again of the form in (CS.3), since \(\mathfrak n_\varphi\) is a left ideal. Thus \(\mathfrak m_\varphi\) is a *-subalgebra, although it need not be a two-sided ideal in \(A\).

The weight is **norm densely defined** when \(\overline{\mathfrak n_\varphi}^{\,\|\cdot\|}=A\), equivalently when \(\mathfrak m_\varphi\) is norm dense. If \(\mathfrak n_\varphi\) is dense, approximate \(a^{1/2}\) for \(a\in A_+\) and use the squares of those approximants to approximate \(a\) by finite positive elements. The estimate

\[
 \begin{aligned}
 &\|x^*x-y^*y\|\\
 &\quad\leq(\|x\|+\|y\|)\|x-y\|.
 \end{aligned}
\]

follows by adding and subtracting \(x^*y\). It proves the required convergence. AC4 and UZ07 express every element of the original algebra as a linear combination of positive elements, so density in the positive cone implies density of its complex span. Conversely, (CS.3) and the left-ideal property give \(\mathfrak m_\varphi\subseteq\mathfrak n_\varphi\).

An order property sometimes required of a weight is

\[
\varphi(a)=\sup\{\varphi(b):0\leq b\leq a,\ b\in F_\varphi\}.
\tag{CS.4}
\]

This is a separate assertion until an equivalence with norm density has been proved under the relevant hypotheses. Merely finding a nonzero finite \(b\leq a\) does not establish the equality.

## The GNS quotient and its exact domain

For \(x,y\in\mathfrak n_\varphi\), put
\([x,y]_\varphi=\varphi_0(y^*x)\).
Positivity of \([x+ty,x+ty]_\varphi\) for every \(t\in\mathbb C\) gives Cauchy–Schwarz:

\[
|[x,y]_\varphi|^2\leq[x,x]_\varphi[y,y]_\varphi.
\tag{CS.5}
\]

Here the quadratic is

\[
 \begin{aligned}
 &[x+ty,x+ty]_\varphi\\
 &\quad=[x,x]_\varphi\\
 &\qquad+2\operatorname{Re}(\overline t[x,y]_\varphi)\\
 &\qquad+|t|^2[y,y]_\varphi.
 \end{aligned}
\]

The finite extension is self-adjoint, because it is real on its real self-adjoint part; this justifies the two conjugate cross terms. If \([y,y]_\varphi=0\) but \([x,y]_\varphi\ne0\), setting \(t=-r[x,y]_\varphi\) for arbitrarily large positive \(r\) makes the quadratic negative. Otherwise its minimum is obtained at \(t=-[x,y]_\varphi/[y,y]_\varphi\), and gives (CS.5).

The null space \(\mathcal Z_\varphi=\{x:\varphi(x^*x)=0\}\) is a left ideal by (CS.2). It is linear by the same sum and scaling inequalities. Cauchy–Schwarz makes every null vector orthogonal to every vector, so the pairing is independent of both quotient representatives and is positive definite after quotienting. Complete the inner-product quotient \(\mathfrak n_\varphi/\mathcal Z_\varphi\) to obtain \(H_\varphi\), and write \(\Lambda_\varphi\) for the quotient map. Left multiplication defines

\[
\langle\Lambda_\varphi(x),\Lambda_\varphi(y)\rangle
=\varphi_0(y^*x),\qquad
\pi_\varphi(a)\Lambda_\varphi(x)=\Lambda_\varphi(ax).
\tag{CS.6}
\]

The second inequality in (CS.2) proves that this operator is well-defined and has norm at most \(\|a\|\). Multiplication on the dense quotient domain gives
\(\pi_\varphi(ab)=\pi_\varphi(a)\pi_\varphi(b)\), while

\[
\langle\pi_\varphi(a)\Lambda_\varphi(x),\Lambda_\varphi(y)\rangle
=\varphi_0(y^*ax)
=\langle\Lambda_\varphi(x),\pi_\varphi(a^*)\Lambda_\varphi(y)\rangle.
\]

Hence \(\pi_\varphi\) is a *-representation. The range of \(\Lambda_\varphi\) is dense by construction; this does not produce a single cyclic vector. The triple is unique up to its uniquely determined unitary: for a second triple \((K,\rho,L)\), send \(\Lambda_\varphi(x)\) to \(L(x)\). Equality of the pairings makes this map well-defined and isometric. It extends by BK01 to an isometry of the completions; its range is closed, since an isometric image of a complete space is complete, and dense by the defining property of \(L\). Hence it is onto. The formulas on the dense quotient show that this unitary intertwines the representations. If the finite-energy domain is zero, the Hilbert space and representation are zero and all these assertions still hold.

The weight is faithful exactly when \(\mathcal Z_\varphi=\{0\}\). Indeed, \(\varphi(a)=0\) for \(a\geq0\) puts \(a^{1/2}\) in the null space, and \(\varphi(x^*x)=0\) detects its elements. Faithfulness of the weight alone does not make \(\pi_\varphi\) faithful if too few elements have finite weight.

**Example.** On \(A=\mathbb C^2\), define \(\varphi(a,b)=a\) for \(a,b\geq0\) with \(b=0\), and \(\varphi(a,b)=+\infty\) when \(b>0\). This is a faithful weight, but \(\mathfrak n_\varphi=\mathbb C\oplus0\). Its GNS space is one-dimensional and \(\pi_\varphi(a,b)\) acts by \(a\), so the faithful weight has a nonfaithful GNS representation. An even more extreme weight can have \(\mathfrak n_\varphi=\{0\}\).

## References

- Johan Kustermans and Stefaan Vaes, [*Weight theory for C*-algebraic quantum groups*, arXiv:math/9901063](https://arxiv.org/abs/math/9901063), §1.1, page 4. The full finite-domain and GNS proofs, including the arbitrary-weight cases, are written above.
