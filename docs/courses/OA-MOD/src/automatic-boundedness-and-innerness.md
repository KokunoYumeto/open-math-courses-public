# Why an everywhere-defined derivation is bounded

The domain hypothesis separates two different uses of derivations. A derivative on a dense smooth algebra can be unbounded. A complex-linear derivation defined on an entire C*-algebra is automatically bounded, even when continuity was not assumed. Together with the spectral-tail construction, this supplies the unrestricted von Neumann innerness theorem and its full Lie-algebra interpretation.

The decomposition and automatic-boundedness arguments below are the existing OA-FLOW programme proof in *Derivatives of actions: domains, perturbations, and implementation*, in the section *Complex derivations and bounded generators*. Canonical ownership remains OA-FLOW. The current October repairs were written and checked by GPT-6.1 Sol (OpenAI), Ultra; the earlier record identifies Codex, September 2026, without an exact model. Exact prerequisite binding, local selection and the final innerness consequence were prepared by GPT-6 Astra (OpenAI), Ultra, 5 October 2026. Original programme expression is CC0.

The mathematical antecedent for automatic boundedness is Shôichirô Sakai, [*On a conjecture of Kaplansky*](https://www.jstage.jst.go.jp/article/tmj1949/12/1/12_1_31/_article/-char/en), Tohoku Mathematical Journal 12 (1960), pages 31–33, with the theorem and proof on pages 31–32. The complete programme argument is reproduced below, rather than replacing it with a citation. The resulting unrestricted innerness theorem is Sakai, [*Derivations of W\*-Algebras*](https://www.math.uci.edu/~brusso/sakai66.pdf) (1966), Theorem 1; the alternate spectral-tail construction used here is the preceding programme reading, with its approved Takesaki II antecedent.

## The algebraic and analytic preparation

The forced unitization, with its positive-cone identification in the same reading, embeds any C*-algebra as a closed ideal of a unital C*-algebra. State Cauchy–Schwarz, norming states and compactness of the unital state set are proved at arbitrary-algebra scope. Their self-adjoint calculus and real and complex Hahn–Banach proofs are linked there. The real and complex closed graph theorem supplies the last step. No faithful or normal state is required, and no weak-star metrizability is assumed.

Compactness supplies a convergent subnet of the sequence of states used below. Explicitly, the closures of the tails have the finite-intersection property, so their intersection contains a point \(\varphi\). For each original index \(n\) and neighborhood \(U\) of \(\varphi\), some \(m\ge n\) lies in \(U\). Direct triples \((n,U,m)\) by increasing both integer indices and shrinking \(U\). The tail property supplies a common successor, and projection to \(m\) is increasing and cofinal. The corresponding subnet converges to \(\varphi\). This uses the compactness proved in the linked state and Banach lessons, not a sequential compactness assertion.

**Decomposition lemma.** For any derivation \(d\) of a complex star algebra, define \(d^\dagger(x)=d(x^*)^*\). Then \(d^\dagger\) is a complex-linear derivation and

\[
\begin{gathered}
d_1=\frac{d+d^\dagger}{2}, \\
d_2=\frac{d-d^\dagger}{2i}, \\
d=d_1+i d_2.
\end{gathered}
\tag{AU.1}
\]

is its unique decomposition into two star derivations.

**Proof.** The two conjugations make \(d^\dagger\) complex linear. Reversing the product twice gives

\[
d^\dagger(xy)=d(y^*x^*)^*=x d^\dagger(y)+d^\dagger(x)y.
\]

Also \((d^\dagger)^\dagger=d\) and \((\lambda d)^\dagger=\bar\lambda d^\dagger\). These identities make both \(d_1\) and \(d_2\) fixed by \(\dagger\), and direct addition gives (AU.1). If \(d=r+is\) with \(r^\dagger=r\) and \(s^\dagger=s\), then \(d^\dagger=r-is\), forcing the two formulas. \(\square\)

For an inner derivation \(d=[b,\cdot]\), one has \(d^\dagger=[-b^*,\cdot]\). Thus \(d\) is star preserving exactly when \(b+b^*\) is central. In that case the same derivation has the form \(i[h,\cdot]\) with \(h=(b-b^*)/(2i)\) selfadjoint. Two selfadjoint implementers give the same derivation exactly when their difference is central. For a general complex derivation the formula \(i[h,\cdot]\) with selfadjoint \(h\) is not asserted.

## The closed-graph argument

**Automatic boundedness theorem.** An everywhere-defined derivation on a C*-algebra is bounded.

**Proof.** By (AU.1) it suffices to treat a star derivation \(d\). Extend to the unitization by \(d(1)=0\); the product rule verifies this extension algebraically, without assuming continuity. Suppose \(z\geq0\) and a state \(\varphi\) satisfies \(\varphi(z)=\|z\|\). Then \(\varphi(dz)=0\). For \(z=0\) this is immediate. Otherwise normalize \(z\) to norm one and let \(q=(1-z)^{1/2}\). Since \(\varphi(q^2)=0\), state Cauchy–Schwarz gives

\[
\varphi((dq)q)=\varphi(q(dq))=0.
\]

The identity \(d(z)=-d(q^2)\) proves the claim. This step is algebraic; the value \(dq\) is an element of the algebra even though \(d\) has not yet been shown bounded.

To prove the graph closed on the real Banach space \(A_{\rm sa}\), let \(x_n\to0\) and \(d x_n\to y\) in norm, with all \(x_n\) selfadjoint. Then \(y\) is selfadjoint. If \(y\ne0\), scale the sequence and, if necessary, change its sign so that \(\|y\|=1\) and \(1\in\operatorname{Sp}(y)\). Replace \(x_n\) by \(x_n+\|x_n\|1\). It still tends to zero, has the same derivative, and is positive. Write \(y=y_+-y_-\) and choose a state \(\varphi_n\) norming the positive element \(y_++x_n\). Pass to a weak-star convergent subnet in the unital state space; denote its limit by \(\varphi\).

Because \(x_n\to0\), norming implies \(\varphi(y_+)=\|y_+\|=1\). Applying the preceding claim to \(y_++x_n\) and taking the subnet limit yields \(\varphi(dy_++y)=0\). The same claim applied to \(y_+\) and \(\varphi\) gives \(\varphi(dy_+)=0\). Therefore \(\varphi(y)=0\), and hence \(\varphi(y_-)=1\). But \(\|y_++y_-\|=\||y|\|=1\), whereas \(\varphi(y_++y_-)=2\), contradicting the state norm. Thus \(y=0\).

The real closed graph theorem, with the completeness and complete-metric Baire premises stated above, makes \(d\) bounded on \(A_{\rm sa}\). Writing every \(x\) as its selfadjoint real and imaginary parts proves boundedness on \(A\). Restrict from the unitization in the nonunital case, and combine the two bounded star derivations in (AU.1) for the general case. \(\square\)

Completeness and an everywhere-defined domain are essential here. A smooth subalgebra of a von Neumann algebra is generally not complete in the C*-norm, so this theorem gives no boundedness conclusion for its action generator.

## All von Neumann derivations are inner

Let \(M\) be an arbitrary von Neumann algebra and \(d:M\to M\) any everywhere-defined complex-linear derivation. The preceding theorem makes \(d\) bounded. Apply the complete spectral-tail proof, with its exact input bridge, to obtain

\[
\begin{gathered}
d=[k,\cdot],\\
k\in M, \\
\|k\|\le\|d\|.
\end{gathered}
\tag{AU.2}
\]

For a star derivation, the same proof supplies a self-adjoint implementer in the convention \(d=i[h,\cdot]\), both a positive choice \(0\le h\le\|d\|1\) and a centered choice of norm at most \(\|d\|/2\). These claims retain arbitrary algebras and arbitrary Hilbert representations. They use no trace, factor decomposition, semifiniteness or separability.

The map \(\operatorname{ad}:M\to\operatorname{Der}(M)\) is therefore onto. Its kernel is the center \(Z(M)\) by the definition of a commutator. A direct four-term expansion on each \(x\in M\) gives

\[
\begin{gathered}
{}[\operatorname{ad}a,\operatorname{ad}b] \\
=\operatorname{ad}[a,b].
\end{gathered}
\tag{AU.3}
\]

Thus it identifies the complex Lie algebra \(M/Z(M)\) with all complex-linear derivations of \(M\). The Jacobi identity follows by expanding the three double commutators and canceling ordered products in pairs. The general commutator of two derivations is again a derivation: in its expansion on a product, the two mixed terms from the two compositions cancel. This verifies the Lie structure without a further continuity premise.

The bounded contract used by the earlier modular and cone-generator lessons is a consequence of this full theorem; its statement remains unchanged. Conversely, bounded innerness alone would not prove this unrestricted statement. The automatic-boundedness argument supplies exactly the missing step.
