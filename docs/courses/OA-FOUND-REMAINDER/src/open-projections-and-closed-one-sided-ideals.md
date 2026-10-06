# Open projections and closed one-sided ideals

*Self-checked by the writing AI. Original text: CC0 1.0. The credited Kaneda–Schick example retains CC BY 4.0.*

Suppose a collection of operators is meant to act only on part of a system. A projection in the bidual describes such a part, but it need not be recoverable from the original algebra. This lesson asks how to recognize the parts that can be recovered: through positive approximations, through closed one-sided ideals, or through what states fail to see.

The three descriptions require different tests. A matrix calculation identifies the correct side of an ideal. A discrete example shows why the supporting projection may lie outside the algebra. An endpoint example shows how continuity can obstruct a support, even when all fibres have the same dimension. We will then prove the complete dictionary for an arbitrary C*-algebra, including the distinction between the algebra's identity and an ideal's relative identity.

Use [Monotone approximation and semicontinuous operators](../reader/monotone-approximation-and-semicontinuous-operators.html), especially its quasi-state criterion, positive approximants, unitized-cone identity and one-sided resolvent estimate. The affine approximation needed for the state criterion is [Affine approximation and quasi-state spaces](../reader/affine-approximation-and-quasi-state-spaces.html#2-approximation-on-a-split-face), Corollary 2.2. The complete polar decomposition and Cauchy–Schwarz estimate are [Polar decomposition and absolute value of functionals](../../foundations-of-von-neumann-algebras/polar-decomposition-of-functionals-and-weak-compactness-in-preduals.html#oa-fnd-pd-03), Theorem 2.7; its [invariant-subspace proof and subspace Krein–Šmulian proof](../../foundations-of-von-neumann-algebras/polar-decomposition-of-functionals-and-weak-compactness-in-preduals.html#oa-fnd-pd-09) are Theorem 6.1 and Lemma 6.4. [Kaplansky density](../../foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences.html#oa-fnd-kd-07), Theorem 7.1, supplies bounded strong* approximation. [Continuous functional calculus](../../foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-19), Theorem 11.4, supplies positive approximate identities for one-sided ideals. [The universal enveloping von Neumann algebra](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-06), Lemma 4.2, supplies central ideal summands, with its stated bidual and normal-extension prerequisites. Brown’s freely readable paper also treats open and closed projections and state semicontinuity. The proofs below give the full state-to-ideal reconstruction and resolvent steps.

Let \(A\ne0\) and \(M=A^{**}\). Evaluations of a bidual element use the unique normal extensions of functionals in \(A^*\). Write \(Q(A)=\{\varphi\in A^*_+:\|\varphi\|\le1\}\) and \(S(A)=\{\varphi\in A^*_+:\|\varphi\|=1\}\), with their relative \(\sigma(A^*,A)\) topologies. For a bounded increasing net of self-adjoint elements, \(a_i\uparrow x\) means that its supremum in \(M\) is \(x\); this is also its strong and ultraweak limit in the universal representation.

A projection \(p\in M\) is **open relative to \(A\)** when \(u_i\uparrow p\) for an increasing net in \(A_+\). A projection is **closed** when its complement is open. The positive terms automatically satisfy \(0\le u_i\le p\le1\). These words concern the fixed inclusion \(A\subset M\).

## What a support keeps and what states miss

For a projection \(p\), the right ideal \(pM\cap A\) consists of operators whose ranges lie in \(pH\); the left ideal \(Mp\cap A\) consists of operators that vanish on \((1-p)H\). A matrix is a useful first test because confusing range with initial space reverses the two ideals.

**Exercise 5.1 — introductory: a matrix projection and its ideals.** For \(A=M_2(\mathbb C)\) and \(p=\operatorname{diag}(1,0)\), compute the right ideal \(pA\), the left ideal \(Ap\), and \(A^*(1-p)\) in the trace-density model \(f_d(X)=\operatorname{Tr}(dX)\). Determine whether \(p\) is open and closed.

**Solution.** The right ideal consists of matrices with second row zero; the left ideal consists of matrices with second column zero. The condition \(f_d(pX)=0\) for all \(X\) is \(dp=0\), so \(d\) has first column zero. Its positive unit ball has densities \(d=\operatorname{diag}(0,t)\), \(0\le t\le1\). All these spaces are closed in finite dimension.

The constant net with value \(p\) is a positive increasing net in \(A\), so \(p\) is open. The same applies to \(1-p\), so \(p\) is closed too. Their evaluation functions are continuous because both projections already belong to \(A\).

The positive densities in the matrix calculation live on the complementary coordinate. This suggests recording the states that assign zero to \(p\), rather than testing all entries of the ideal independently. In infinite dimensions, both closure and approximation matter.

**Exercise 5.2 — intermediate: every subset of a discrete space.** Let \(A=c_0(\mathbb N)\) and \(p=1_S\in\ell^\infty(\mathbb N)=A^{**}\) for any subset \(S\). Find an increasing positive net from \(A\) with supremum \(p\), the right ideal it supports, and the weak* closed annihilator in \(\ell^1\). Is \(p\) closed as well?

**Solution.** Direct the finite subsets \(F\subset S\) by inclusion. Their indicators \(1_F\in c_0\) are positive contractions increasing to \(1_S\) strongly. The supported ideal is
\[
\mathfrak r=\{a\in c_0:a_n=0\text{ for }n\notin S\}.
\]
Its annihilator consists of \(\ell^1\) sequences vanishing on \(S\). It is weak* closed because it is the intersection of the zero sets of the continuous coordinate evaluations at \(1_{\{n\}}\), \(n\in S\). The complement \(1_{\mathbb N\setminus S}\) has the same type of approximation, so \(p\) is also closed. This includes infinite \(S\), for which \(p\) need not belong to \(c_0\).

Here openness and closedness coexist without membership in \(A\): an infinite subset has an indicator in the bidual, and finite-subset indicators approximate it strongly. General elements of \(c_0\) can have infinite support, as the sequence \((1/n)\) shows. Finite-support functions are norm-dense in \(c_0\), since their truncations discard tails that tend uniformly to zero. The test must allow nets and bidual limits.

Now compare a nondiscrete base. In \(C([0,1])\), set \(h(t)=t\) and let \(z=s(h)\) be its support projection in the bidual. Functional calculus gives positive contractions
\[
u_n(t)=\frac{t}{t+1/n},\qquad u_n\uparrow z.
\]
The evaluations satisfy \(\delta_t(z)=1\) for \(t>0\) and \(\delta_0(z)=0\). The net constructs an open part, namely the part seen away from the endpoint. Its complement cannot be obtained in the same way: \(\delta_{1/n}\to\delta_0\) on continuous functions, but their evaluations at \(1-z\) are zero and the limiting evaluation is one. An increasing limit of continuous positive evaluations is lower semicontinuous, so this jump rules out openness of \(1-z\).

The final worked problem will prove the ideal identification and explain why passing to that ideal changes the admissible scalar identity. Before building the general criterion, the following human-authored example combines this endpoint jump with the matrix calculation.

### Equivalent projections can see different open pieces

*Adapted from Masayoshi Kaneda and Thomas Schick, [Open projections and Murray–von Neumann equivalence](https://doi.org/10.1112/blms.12820), published version, 2023, Example 1.1. © 2023 The Authors. This entire subsection is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). GPT-6.1 Sol (OpenAI) replaces indicator notation by \(z=s(h)\) and supplies the evaluation-state proof of nonopenness.*

For \(B=C([0,1])\otimes M_2\), use the central projection \(z\) above and put
\[
v=(1-z)\otimes e_{11}+z\otimes e_{12}.
\]
Orthogonality of \(z,1-z\) gives
\[
\begin{aligned}
p=vv^*&=1\otimes e_{11},\\
q=v^*v&=(1-z)\otimes e_{11}+z\otimes e_{22}.
\end{aligned}
\]
Thus \(v\) implements Murray–von Neumann equivalence. The constant approximation makes \(p\) open. The states \(\psi_t(b)=\langle b(t)e_1,e_1\rangle\) satisfy \(\psi_{1/n}\to\psi_0\), but \(\psi_{1/n}(q)=0\) and \(\psi_0(q)=1\). If \(q\) were an increasing limit from \(B_+\), its state evaluation would be a supremum of continuous functions and hence lower semicontinuous. The jump contradicts that conclusion, so \(q\) is not open.

## The dictionary we want to prove

The examples ask whether a projection can be reconstructed from observations in \(A\), rather than merely compared with another projection in \(M\). The full answer is the following equivalence. Its proof follows the states-to-ideal route below; none of its unproved implications is needed in that route.

**Theorem 3.1 — recovering a support from observations.** For a projection \(p\in M\), the following are equivalent:

1. \(p\) is open.
2. \(pM\) is the ultraweak closure of a closed right ideal of \(A\).
3. \(A^*(1-p)\) is \(\sigma(A^*,A)\)-closed.
4. A norm-bounded increasing net in \(A_{\mathrm{sa}}\) converges to \(p\).
5. \(\widehat p\) is lower semicontinuous on \(S(A)\).

Equivalently in condition 2, \(Mp\) is the ultraweak closure of a closed left ideal. Equivalently in condition 3, \((1-p)A^*\) is weak* closed. When these hold the right and left ideals can be chosen as
\[
\mathfrak r=pM\cap A,\qquad \mathfrak l=Mp\cap A.
\tag{3.1}
\]

## From zero observations to an actual ideal

The module convention fixes which side is being recovered:
\[
(a f)(X)=f(Xa),\qquad (f a)(X)=f(aX)
\quad(a,X\in M,\ f\in A^*).
\tag{2.1}
\]
If a positive functional \(\rho\) assigns zero to \(p\), positivity and Cauchy–Schwarz make it vanish on \(pM\). The matrix calculation is the finite-dimensional instance of this fact. To reconstruct a closed ideal, we need these observations to be closed in the topology that tests only elements of \(A\).

### Closing all witnesses, not only the positive ones

**Lemma 2.1.** If \(p\in M\) is a projection and \(\widehat p\) is lower semicontinuous on \(Q(A)\), then
\[
V=A^*(1-p)=\{f\in A^*:f(pX)=0\text{ for all }X\in M\}
\tag{2.2}
\]
is weak* closed for \(\sigma(A^*,A)\).

**Proof.** The space \(V\) is norm closed and invariant under the left action of \(M\). Its positive unit ball is
\[
Q_p=\{\rho\in Q(A):\rho(p)=0\}.
\tag{2.3}
\]
For positive \(\rho\), \(\rho(p)=0\) implies \(\rho(pX)=0\) by Cauchy–Schwarz; the reverse implication follows at \(X=1\). Lower semicontinuity makes (2.3) weak* closed, and \(Q(A)\) is weak* compact, so \(Q_p\) is compact.

Positive witnesses alone do not describe the whole annihilator. Let \(f_i\in V\), \(\|f_i\|\le1\), and \(f_i\to f\) weak*. The polar-decomposition and invariant-subspace theorems place \(|f_i|\) in \(Q_p\). Passing to a subnet gives \(|f_i|\to\rho\in Q_p\) weak*. Their Cauchy–Schwarz bounds pass to the limit on \(A\):
\[
|f(a)|^2\le\rho(aa^*)\quad(a\in A).
\tag{2.4}
\]
To test the bidual corner, approximate \(X\in M\) strongly* by a bounded net from \(A\), using Kaplansky density. The products \(aa^*\) converge strongly and stay bounded. Normality of \(f,\rho\) therefore extends (2.4) to
\[
|f(X)|^2\le\rho(XX^*)\quad(X\in M).
\tag{2.5}
\]
At \(X=pY\), \(0\le pYY^*p\le\|Y\|^2p\), so the right side is zero. Thus \(f(pY)=0\), or \(f\in V\). The unit ball of \(V\) is weak* closed. The supplied subspace Krein–Šmulian lemma upgrades this bounded-ball statement to weak* closedness of \(V\) itself. \(\square\)

### Recovering the support by multiplication

**Lemma 2.2.** If the subspace \(V\) in (2.2) is weak* closed, there is a closed right ideal \(\mathfrak r\subset A\) with
\[
\overline{\mathfrak r}^{\mathrm{uw}}=pM,
\tag{2.6}
\]
where the closure is taken in \(M\). A bounded increasing net in \(\mathfrak r_+\) converges to \(p\).

**Proof.** Recover the operators that all the witnesses annihilate:
\[
\mathfrak r=\{a\in A:f(a)=0\text{ for every }f\in V\}.
\]
This preannihilator is norm closed. For \(a\in\mathfrak r\), \(b\in A\) and \(f\in V\), left invariance gives \(bf\in V\), so \(f(ab)=(bf)(a)=0\). Hence it is a right ideal. Hahn–Banach and weak* closedness give \(\mathfrak r^\perp=V\), and its ultraweak closure is \(V^\perp\). This is exactly \(pM\): its elements are annihilated by every \(f\in V\); if \((1-p)X\ne0\), a normal \(h\) detects it and \(h(1-p)\in V\) detects \(X\).

The ideal has been recovered, but its approximate identity must recover the *specified* projection \(p\). The positive strict contractions in \(\mathfrak r\) form an increasing contractive left approximate identity \((u_i)\), by the supplied one-sided-ideal theorem. Let \(q=\sup_i u_i\). Since \(u_i\in pM\) and \(u_i=u_i^*\), \(u_i=pu_ip\), so \(q\le p\). For \(a\in\mathfrak r\), \(u_i a\to a\) in norm and \(u_i a\to qa\) strongly. Thus \(qa=a\). In particular \(qu_i=u_i\); passing to the strong limit gives \(q^2=q\). The positive contraction \(q\) is therefore a projection, and \(qM\) is ultraweakly closed. Since \(\mathfrak r\subset qM\), taking ultraweak closures yields \(pM\subset qM\), hence \(qp=p\), or \(p\le q\). Therefore \(q=p\). \(\square\)

These lemmas recover an open support when its evaluation is lower semicontinuous on the **quasi-state** space. We still need to justify the **state** test in the dictionary. States omit the zero functional, so adjoining a scalar identity matters.

## Turning state information into positive approximations

Set \(A_1=A+\mathbb C1\subset M\), using the bidual identity, and retain
\[
C=\overline{A_{\mathrm{sa}}^\uparrow}^{\|\cdot\|},\qquad
D=\overline{(A_1)_{\mathrm{sa}}^\uparrow}^{\|\cdot\|}.
\tag{1.1}
\]
The earlier quasi-state criterion identifies \(C\) with lower semicontinuous evaluations on \(Q(A)\). The next criterion identifies \(D\) using states. Its resolvent clauses remove a small scalar error from a projection and remain useful for positive elements that are not projections.

### The state and resolvent criterion

**Theorem 1.1.** For \(x\in M_{\mathrm{sa}}\), the following are equivalent:

1. \(x\in D\).
2. \(\widehat x\) is lower semicontinuous on \(S(A)\).
3. For every \(\alpha>0\) such that \(1-\alpha x\) is positive and invertible,
\[
(1-\alpha x)^{-1}\in C.
\tag{1.2}
\]
4. For every such \(\alpha\),
\[
(1-\alpha x)^{-1}x\in(A_1)_{\mathrm{sa}}^\uparrow.
\tag{1.3}
\]

**Proof.** Evaluations of elements of \((A_1)_{\mathrm{sa}}\) are continuous on states: the scalar part becomes a constant. A bounded increasing limit is represented there by a supremum of these continuous functions. Uniform limits preserve lower semicontinuity, so 1 implies 2.

Assume 2. Extend \(\widehat x|_{S(A)}\) homogeneously to \(Q(A)\), assigning zero at zero. The result is exactly \(\widehat x\), a bounded affine function. The states and zero form complementary split faces, with lower semicontinuous weight \(e(\varphi)=\|\varphi\|\). The singleton-complement approximation gives continuous affine functions \(c_i\) vanishing at zero and scalars \(\beta_i\le0\) such that
\[
c_i+\beta_i e\le\widehat x,
\qquad c_i(\varphi)+\beta_i e(\varphi)\longrightarrow\widehat x(\varphi).
\]
The continuous affine model writes \(c_i=\widehat{a_i}\), \(a_i\in A_{\mathrm{sa}}\). Thus
\[
x_i=a_i+\beta_i1\le x
\]
converges to \(x\) on all positive normal functionals, and hence weakly as operators in the universal representation, by polarization. Its norms need not be uniformly bounded.

Fix an admissible \(\alpha\). The [one-sided resolvent estimate](../reader/monotone-approximation-and-semicontinuous-operators.html#5-strong-resolvent-estimates) nevertheless gives
\[
B_i=(1-\alpha x_i)^{-1}\longrightarrow
B=(1-\alpha x)^{-1}\quad\text{strongly},
\qquad 0\le B_i\le B.
\tag{1.4}
\]
Each \(B_i\) lies in \(A_1\). It has a decomposition \(B_i=d_i+\lambda_i1\), \(d_i\in A_{\mathrm{sa}}\), with
\[
\lambda_i=(1-\alpha\beta_i)^{-1}>0.
\]
For nonunital \(A\) this follows by applying the quotient character of \(A_1\); for unital \(A\) it follows by subtracting this scalar multiple of the identity from \(B_i\). Consequently
\[
\widehat{B_i}(\varphi)=\varphi(d_i)+\lambda_i\|\varphi\|
\]
is lower semicontinuous on \(Q(A)\). The family \((B_i)\) is bounded by \(B\), so (1.4) gives convergence on every normal functional. Since each \(B_i\le B\),
\[
\widehat B(\varphi)=\sup_i\widehat{B_i}(\varphi)
\quad(\varphi\in Q(A)).
\]
No increasingness of \((B_i)\) is needed for this supremum identity. It proves lower semicontinuity of \(\widehat B\). The preceding quasi-state characterization gives \(B\in C\), establishing 3.

By the exact identity \((A_1)_{\mathrm{sa}}^\uparrow=\mathbb R1+C\), condition 3 gives
\[
(1-\alpha x)^{-1}x=\alpha^{-1}(B-1)
\in(A_1)_{\mathrm{sa}}^\uparrow,
\]
proving 4. Finally these elements converge in norm to \(x\) as \(\alpha\downarrow0\), proving 1. \(\square\)

### Passing to an increasing limit

The criterion survives the monotone limit needed to construct a support.

**Corollary 1.2.** The cones \(C\) and \(D\) are closed under bounded increasing limits:
\[
C^\uparrow=C,\qquad D^\uparrow=D.
\tag{1.5}
\]

**Proof.** A bounded increasing limit is represented on positive functionals by the pointwise supremum. The supremum of lower semicontinuous functions is lower semicontinuous, both on \(Q(A)\) and on \(S(A)\). Apply the two characterizations. Constant nets give the reverse inclusions. \(\square\)

### Moving the scalar error out of a projection

For a general self-adjoint element, state and quasi-state semicontinuity differ. This transform controls that difference for positive elements.

**Proposition 1.3 — the positive bounded transform.** For \(x\in M_+\) and \(\alpha>0\),
\[
\alpha1+x\in C
\quad\Longleftrightarrow\quad
(\alpha1+x)^{-1}x\in D.
\tag{1.6}
\]

**Proof.** Put \(b=(\alpha1+x)^{-1}x\). If \(b\in D\), then \(0\le b<1\) with a strict uniform bound below one. Theorem 1.1 gives
\((1-b)^{-1}=1+\alpha^{-1}x\in C\), and positive scaling proves the left side.

Conversely, suppose \(\alpha1+x\in C\). Its positive scalar shifts have bounded positive increasing approximants, by [Proposition 3.1 on positive approximants](../reader/monotone-approximation-and-semicontinuous-operators.html#3-positive-approximants). For \(\delta>0\), take
\[
y_i\in A_+,\qquad y_i\uparrow x+(\alpha+\delta)1.
\]
The elements \(1-\alpha(\delta1+y_i)^{-1}\) lie in \((A_1)_{\mathrm{sa}}\), increase, and are bounded between \((1-\alpha/\delta)1\) and \(1\). Their limit is
\[
1-\alpha((\alpha+2\delta)1+x)^{-1}
\in(A_1)_{\mathrm{sa}}^\uparrow.
\]
Letting \(\delta\downarrow0\) in norm gives \(b\in D\). \(\square\)

## Finishing the recovery and returning to the models

### A projection has no approximation gap

**Theorem 2.3 — a projection has no norm-closure gap.** For a projection \(p\in M\),
\[
p\in D\quad\Longleftrightarrow\quad p\in A_+^\uparrow.
\tag{2.7}
\]

**Proof.** The reverse implication is immediate. Suppose \(p\in D\). For every \(\delta>0\),
\[
(\delta1+p)^{-1}p=\frac{p}{1+\delta}\in D,
\]
since \(D\) is invariant under positive scaling. Proposition 1.3 gives \(p+\delta1\in C\). Norm closure gives \(p\in C\), so \(\widehat p\) is lower semicontinuous on \(Q(A)\). Lemmas 2.1 and 2.2 provide a bounded increasing net in \(A_+\) with supremum \(p\). \(\square\)

### Completing the support dictionary

**Proof of Theorem 3.1.** Condition 1 gives a positive net \(u_i\uparrow p\). Since \(0\le u_i\le p\), each \(u_i=pu_ip\) belongs to \(\mathfrak r\). Its ultraweak closure is a right ideal of \(M\): right multiplication by any \(b\in A\) preserves it, then the ultraweak density of \(A\) and separate continuity extend this to all \(b\in M\). It contains \(p\), and is contained in \(pM\). Hence it is \(pM\), proving 2.

Condition 2 gives condition 3 by taking annihilators: \(\mathfrak r^\perp=A^*(1-p)\), which is weak* closed. Lemma 2.2 proves 3 implies 1. Conditions 1 and 4 are equivalent by Theorem 2.3, since any limit in condition 4 belongs to \(C\subset D\). Conditions 1 and 5 are equivalent by Theorems 1.1 and 2.3. Taking adjoints of ideals, and taking \(f\mapsto f^*\) for functionals, proves the left-handed versions. Formula (3.1) follows from the construction. If a closed right ideal has ultraweak closure \(pM\), its annihilator is \(A^*(1-p)\). Hahn–Banach recovers the ideal as the preannihilator of that space, hence as \(pM\cap A\). Thus a support determines its closed ideal uniquely. \(\square\)

On states the identity has constant evaluation one. Thus a projection \(q\) is closed exactly when \(\widehat q\) is upper semicontinuous on \(S(A)\). For a nonunital algebra this assertion should not be transferred to \(Q(A)\): the bidual identity has evaluation \(\|\varphi\|\) there, which may be discontinuous.

The matrix and discrete problems now have a common explanation. Their complementary positive observations are closed, so the annihilator determines a closed ideal; its approximate identity recovers the same projection. At the endpoint, a new complementary observation appears as a limit. This is why openness is sensitive to \(A\), whereas Murray–von Neumann equivalence takes place entirely in \(M\).

## Changing the algebra changes its identity

A supported right ideal need not be a C*-algebra. For a **two-sided** ideal \(I\), its support is central and its bidual is a direct summand. Compression transports semicontinuity, but the summand's scalar identity is its central support \(z\), rather than the ambient \(1\).

Let \(I\) be a closed two-sided ideal of \(A\). Its ultraweak closure is \(Mz\) for a central projection \(z\). Its increasing positive approximate identity converges to \(z\), so \(z\) is open. The canonical bidual inclusion identifies \(I^{**}\) with \(Mz\), whose identity is \(z\). Put
\[
\begin{aligned}
I_1&=I+\mathbb Cz\subset Mz,\\
C_I&=\overline{I_{\mathrm{sa}}^\uparrow}^{\|\cdot\|},\\
D_I&=\overline{(I_1)_{\mathrm{sa}}^\uparrow}^{\|\cdot\|}.
\end{aligned}
\]

**Proposition 4.1.** Under this identification,
\[
D_I=\overline{z(A_1)_{\mathrm{sa}}^\uparrow}^{\|\cdot\|}
=\overline{zD}^{\|\cdot\|}.
\tag{4.1}
\]
The closures on the right are in \(Mz\).

**Proof.** Let \(u_j\in I_+\) be an increasing contractive approximate identity with limit \(z\). For \(a\in(A_1)_+\),
\[
a^{1/2}u_j a^{1/2}\in I_+,
\qquad a^{1/2}u_j a^{1/2}\uparrow a^{1/2}za^{1/2}=za.
\tag{4.2}
\]
The ideal property places the products in \(I\); centrality gives the last equality. For general \(a\in(A_1)_{\mathrm{sa}}\), add a scalar to make it positive and then subtract the corresponding scalar multiple of \(z\). Hence \(za\in(I_1)_{\mathrm{sa}}^\uparrow\subset D_I\).

If \(a_i\uparrow x\) is a bounded net in \((A_1)_{\mathrm{sa}}\), centrality makes \(za_i\) a bounded increasing net in \(D_I\) with limit \(zx\). Corollary 1.2 for \(I\) gives \(zx\in D_I\). This proves the inclusion into \(D_I\) of both right-hand closures in (4.1).

Conversely the exact unitized-cone identity for \(I\) gives
\[
(I_1)_{\mathrm{sa}}^\uparrow=\mathbb Rz+C_I.
\]
An increasing net from \(I\) is also one from \(A\); thus \(C_I\subset C\cap Mz\). Therefore every \(\alpha z+y\) in this exact cone is
\[
z(\alpha1+y),\qquad \alpha1+y\in\mathbb R1+C
=(A_1)_{\mathrm{sa}}^\uparrow.
\]
Taking norm closures proves the reverse inclusion for the first equality. Since multiplying by \(z\) is contractive and \(D\) is the norm closure of \((A_1)_{\mathrm{sa}}^\uparrow\), the two right-hand closures agree. \(\square\)

The relative scalar identity is \(z\). It may have different semicontinuity properties when viewed in the whole bidual with identity \(1\); the last exercise makes this distinction concrete.

**Exercise 5.3 — advanced: the relative identity at an endpoint.** Let \(A=C([0,1])\), \(I=\{a:a(0)=0\}\), and \(h(t)=t\). Let \(z=s(h)\in A^{**}\), the support projection of \(h\). Show that \(I^{**}=A^{**}z\), that \(z\) is open and not closed, and that \(-z\in D_I\) but \(-z\notin D\). Explain how this is consistent with Proposition 4.1.

**Solution.** The functions
\[
u_n(t)=\frac{t}{t+1/n}\in I_+
\]
increase to \(s(h)=z\) in the bidual. They are an approximate identity for \(I\): for any \(a\in I\), small \(t\) makes \(|a(t)|\) uniformly small, while on \(t\ge\eta>0\), \(1-u_n(t)\) tends uniformly to zero. Thus \(u_na\to a\) in norm. The ideal's central supporting projection is \(z\), giving the stated bidual identification. In particular \(z\) is open.

For evaluation states at positive points, normality gives \(\delta_t(z)=\lim_nu_n(t)=1\); at zero, \(\delta_0(z)=0\). Since \(\delta_{1/n}\to\delta_0\) weak*, the evaluation of \(1-z\) has value zero along the sequence and value one at its limit. It is not lower semicontinuous on states. Theorem 3.1 says \(1-z\) is not open, so \(z\) is not closed.

The projection \(z\) is the identity of \(I^{**}\), so \(-z\in(I_1)_{\mathrm{sa}}\subset D_I\). On the state space of \(A\), however, \(\widehat{-z}\) has value \(-1\) at every \(\delta_{1/n}\) and zero at \(\delta_0\). It is not lower semicontinuous, so \(-z\notin D\). There is no conflict with (4.1): \(-z=z(-1)\), and \(-1\in(A_1)_{\mathrm{sa}}\). Compression by \(z\), followed by the relative interpretation in \(I^{**}\), is exactly what that proposition uses.

## References

[Kaneda–Schick] Masayoshi Kaneda and Thomas Schick, [“Open projections and Murray–von Neumann equivalence”](https://doi.org/10.1112/blms.12820), *Bulletin of the London Mathematical Society* **55** (2023), 1808–1816. The marked subsection adapts Example 1.1 of the published HTML version under CC BY 4.0.

[Brown] Lawrence G. Brown, [Semicontinuity and closed faces of C*-algebras](https://arxiv.org/abs/1312.3624v2), arXiv:1312.3624v2, 11 July 2014.
