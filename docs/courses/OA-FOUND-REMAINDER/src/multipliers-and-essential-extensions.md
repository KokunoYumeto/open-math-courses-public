# Multipliers and essential extensions

*Written by GPT-6.1 Sol (OpenAI), Ultra, September–October 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

A nonunital C*-algebra can sit as an ideal in a larger algebra that supplies an identity and additional operators. The multiplier algebra is the largest such extension in which the original ideal detects every operator. Its self-adjoint elements also have a semicontinuity description: they admit bounded monotone approximation from both sides after adjoining the bidual identity.

We prove that description and the extension property. The norm convergence needed in the first proof comes from compactness of the quasi-state space. In the second proof, multiplication on the ideal determines an operator on the universal representation.

Use the [quasi-state evaluation model](../reader/affine-approximation-and-quasi-state-spaces.html#3-the-compact-space-of-positive-functionals), Theorem 3.1, and the monotone-limit notation from [Monotone approximation and semicontinuous operators](../reader/monotone-approximation-and-semicontinuous-operators.html). Positive increasing approximate identities and continuous functional calculus are supplied by [Continuous functional calculus](../../foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-19), Theorem 11.4. The universal representation and its bidual closure are [The universal enveloping von Neumann algebra](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-03), Theorem 3.3; its Proposition 5.7 supplies the complete extension proof in the nondegenerate case used here. Blackadar’s freely readable *Operator Algebras* also treats idealizers, essential extensions and the strict topology. The bounded-monotone intersection criterion is proved here by quasi-state compactness and the explicit estimates (2.2)–(2.5).

## 1. Operators that preserve the algebra

Let \(A\) be a C*-algebra and \(M=A^{**}\), with its canonical identity \(1\). We realize \(M\) faithfully and normally on the universal representation space. The zero algebra has zero multiplier algebra; the remaining discussion permits \(A\ne0\).

Define
\[
\begin{aligned}
\operatorname{LM}(A)&=\{x\in M:xA\subset A\},\\
\operatorname{RM}(A)&=\{x\in M:Ax\subset A\},\\
\operatorname{Mult}(A)&=\operatorname{LM}(A)\cap\operatorname{RM}(A).
\end{aligned}
\tag{1.1}
\]
These are left multipliers, right multipliers and two-sided multipliers, respectively. We write \(\operatorname{Mult}(A)\) to distinguish this algebra from the bidual \(M\).

**Proposition 1.1.** The multiplier algebra is a unital C*-subalgebra of \(M\). It contains \(A\) as a closed two-sided ideal. If \(A\) is unital, then \(\operatorname{Mult}(A)=A\).

**Proof.** Left multipliers are closed under addition, scalar multiplication and multiplication: \(xy a=x(ya)\in A\) for \(x,y\in\operatorname{LM}(A)\). They are norm closed, since \(x_n\to x\) implies \(x_na\to xa\) in norm for every \(a\in A\). Right multipliers have the analogous properties. Taking adjoints interchanges the two classes, because \(xa\in A\) implies \(a^*x^*\in A\). Their intersection is consequently a norm-closed self-adjoint subalgebra, hence a C*-algebra. It contains \(1\) and \(A\), and (1.1) says precisely that multiplication on either side by its elements preserves \(A\).

If \(A\) is unital, its identity is also the bidual identity. A multiplier \(x\) then satisfies \(x=x1\in A\). The converse inclusion always holds. \(\square\)

An ideal \(J\) in a C*-algebra \(B\) is called essential, or thick, if every nonzero two-sided ideal of \(B\) has nonzero intersection with \(J\). In what follows \(J\) is closed. The definition is unchanged if one tests only closed ideals.

**Lemma 1.2 — detection by the ideal.** For a closed two-sided ideal \(J\subset B\), the following are equivalent:

1. \(J\) is essential.
2. \(bJ=0\) implies \(b=0\), for \(b\in B\).
3. \(Jb=0\) implies \(b=0\), for \(b\in B\).

**Proof.** Let
\[
\operatorname{Ann}(J)=\{b\in B:bJ=Jb=0\}.
\]
This is a closed self-adjoint two-sided ideal. For example, if \(b\) annihilates \(J\) and \(c\in B\), then \((cb)J=0\) and \(J(cb)=(Jc)b=0\), since \(Jc\subset J\); the other products and adjoints are similar. Also \(\operatorname{Ann}(J)\cap J=0\): an approximate identity \(u_i\) of \(J\) satisfies \(bu_i\to b\) in norm for \(b\in J\), whereas \(bu_i=0\) for an annihilator element.

If \(J\) is essential, it follows that \(\operatorname{Ann}(J)=0\). If \(bJ=0\), then \((b^*b)J=0\); self-adjointness also gives \(J(b^*b)=0\). Thus \(b^*b\in\operatorname{Ann}(J)\), and \(b=0\). This proves 1 implies 2. Adjoint symmetry gives condition 3.

Conversely, if an ideal \(K\subset B\) satisfies \(K\cap J=0\), then \(bJ\subset K\cap J=0\) for every \(b\in K\). Condition 2 forces \(K=0\). This proves essentiality even when \(K\) is not closed. The same annihilator argument shows that testing closed ideals suffices. \(\square\)

**Corollary 1.3.** The ideal \(A\) is essential in \(\operatorname{Mult}(A)\).

**Proof.** Let \(u_i\in A_+\) be an increasing contractive approximate identity. It converges strongly to \(1\) in the universal representation. If \(xA=0\) for a multiplier \(x\), then \(xu_i=0\) and strong convergence gives \(x=0\). Apply Lemma 1.2. \(\square\)

## 2. Monotone approximation from both sides

Put \(A_1=A+\mathbb C1\subset M\). For a self-adjoint subset \(V\subset M\), let \(V^\uparrow\) denote its bounded increasing strong limits and let \(V^\downarrow=-(-V)^\uparrow\). The bounds refer to the whole approximating family.

We will use a compactness argument for nets. If continuous nonnegative functions \(h_i\) on a compact space decrease pointwise to zero, then they converge uniformly. Indeed, for any \(\varepsilon>0\) the open sets \(\{h_i<\varepsilon\}\) increase and cover the space. A finite subcover and one common upper index give \(h_i<\varepsilon\) everywhere from that index onward. This proves the required net version of Dini's theorem.

**Theorem 2.1 — the self-adjoint multiplier criterion.** For every C*-algebra,
\[
\operatorname{Mult}(A)_{\mathrm{sa}}
=(A_1)_{\mathrm{sa}}^\uparrow\cap(A_1)_{\mathrm{sa}}^\downarrow.
\tag{2.1}
\]
The right side consists of actual bounded monotone limits; no norm closure is added to either class in this formula.

**Proof.** Suppose
\[
y_i\uparrow x,\qquad z_j\downarrow x,
\qquad y_i,z_j\in(A_1)_{\mathrm{sa}},
\]
with both families norm bounded. Fix \(a\in A\). The positive elements
\[
d_{i,j}=a^*(z_j-y_i)a\in A_+
\]
decrease to zero on the product directed set. They belong to \(A\) because \(A\) is an ideal in \(A_1\). Their evaluations are continuous nonnegative functions on the compact quasi-state space \(Q(A)\). Every \(\varphi\in Q(A)\) has a normal extension to \(M\), so these evaluations decrease pointwise to zero. Dini's argument and the quasi-state norm formula give
\[
\|a^*(z_j-y_i)a\|
=\sup_{\varphi\in Q(A)}\varphi(d_{i,j})\longrightarrow0.
\tag{2.2}
\]
Choose a bound \(L\) for all \(\|x-y_i\|\). Since \(0\le x-y_i\le z_j-y_i\), positive functional calculus gives
\[
\begin{aligned}
\|(x-y_i)a\|^2
&=\|a^*(x-y_i)^2a\|\\
&\le L\|a^*(x-y_i)a\|\\
&\le L\|a^*(z_j-y_i)a\|.
\end{aligned}
\tag{2.3}
\]
It follows that \(y_i a\to xa\) in norm. To read this directly as convergence of the \(i\)-net, take a product index \((i_0,j_0)\) after which (2.2) is small, then use the fixed \(j_0\) in (2.3) for all \(i\ge i_0\). Since \(y_i a\in A\) and \(A\) is norm closed, \(xa\in A\). Self-adjointness gives \(ax=(xa^*)^*\in A\). Thus \(x\) is a multiplier.

Conversely suppose \(x=x^*\in\operatorname{Mult}(A)\). An affine change with positive slope reduces to \(0\le x\le1\); the two monotone-limit classes are preserved under this change and its inverse. Since \(\operatorname{Mult}(A)\) is a unital C*-algebra, it contains \(x^{1/2}\) and \((1-x)^{1/2}\). With the approximate identity \(u_i\) from Corollary 1.3,
\[
x^{1/2}u_i x^{1/2}\in A_+,
\qquad x^{1/2}u_i x^{1/2}\uparrow x,
\tag{2.4}
\]
and
\[
1-(1-x)^{1/2}u_i(1-x)^{1/2}\in(A_1)_{\mathrm{sa}},
\qquad
1-(1-x)^{1/2}u_i(1-x)^{1/2}\downarrow x.
\tag{2.5}
\]
Both nets are uniformly bounded. Undoing the affine change proves membership in both classes. \(\square\)

Theorem 4.1 of the monotone-approximation lesson also writes the two classes as \(\mathbb R1+C\) and \(\mathbb R1-C\), where \(C=\overline{A_{\mathrm{sa}}^\uparrow}^{\|\cdot\|}\). Thus (2.1) can equivalently be written
\[
\operatorname{Mult}(A)_{\mathrm{sa}}
=(\mathbb R1+C)\cap(\mathbb R1-C).
\tag{2.6}
\]
Formula (2.6) uses that exact identification of the monotone-limit class. The separate state-semicontinuity cone in the open-projection lesson is its norm closure and is not substituted in the proof.

## 3. The maximal essential extension

**Theorem 3.1.** Let \(J\) be a closed essential ideal of a C*-algebra \(B\), and let \(\theta:J\to A\) be a *-isomorphism. There is a unique *-isomorphism onto its image
\[
\widetilde\theta:B\longrightarrow\operatorname{Mult}(A)
\tag{3.1}
\]
whose restriction to \(J\) is \(\theta\). If \(B\) is unital, this embedding preserves the identity. Consequently every essential extension of \(A\) embeds into its multiplier algebra while fixing \(A\).

**Proof.** Act on the universal representation space \(H\) of \(A\), and identify \(A\) with its represented copy. Then \(\theta\), viewed as a representation of \(J\), is nondegenerate. The complete ideal-extension theorem WA Proposition 5.7 gives its unique extension \(\rho:B\to B(H)\), with \(\rho(B)\subset\theta(J)''=M\) and
\[
\rho(b)\theta(j)=\theta(bj)\quad(b\in B,\ j\in J).
\tag{3.2}
\]
Taking adjoints gives the other ideal action:
\[
\theta(j)\rho(b)=\theta(jb).
\tag{3.3}
\]
Equations (3.2)–(3.3) show that \(\rho(b)\in\operatorname{Mult}(A)\). If \(\rho(b)=0\), then \(\theta(bj)=0\) for every \(j\in J\), so \(bJ=0\). Essentiality and Lemma 1.2 imply \(b=0\). This proves injectivity; an injective C*-homomorphism is isometric, and its image is a C*-subalgebra.

For uniqueness, any extension \(S\) satisfies \(S(b)\theta(j)=\theta(bj)\). The difference \(S(b)-\rho(b)\) annihilates \(A\), and Corollary 1.3 forces it to be zero. If \(B\) is unital, (3.2) gives \(\rho(1)a=a\) for every \(a\in A\); nondegeneracy gives \(\rho(1)=1\). \(\square\)

Essentiality is the faithfulness condition. If it is omitted, the same construction still gives a homomorphism into \(\operatorname{Mult}(A)\), but an ideal of \(B\) invisible to \(J\) can lie in its kernel.

## 4. Approximation after multiplication

The strict topology on \(\operatorname{Mult}(A)\) is specified by the seminorms
\[
x\longmapsto\|xa\|+\|ax\|\quad(a\in A).
\tag{4.1}
\]
It records norm convergence after multiplication by any fixed algebra element. It is Hausdorff because \(A\) detects multipliers.

For every multiplier \(x\), the elements \(xu_i\in A\) converge strictly to \(x\). Indeed,
\[
\|(x-xu_i)a\|\le\|x\|\|a-u_i a\|\longrightarrow0,
\qquad
\|a(x-xu_i)\|=\|ax-(ax)u_i\|\longrightarrow0.
\tag{4.2}
\]
The second convergence uses \(ax\in A\). They also converge strongly to \(x\) in the universal representation and have norms at most \(\|x\|\). Norm convergence to the identity, however, would place that identity inside the closed algebra \(A\).

## 5. Graded exercises with solutions

**Exercise 5.1 — introductory: an invisible summand.** Let \(B=M_2(\mathbb C)\oplus\mathbb C\), \(J=M_2(\mathbb C)\oplus0\), and \(\theta(a,0)=a\). Determine the homomorphism constructed in Theorem 3.1, and explain the role of essentiality.

**Solution.** The target algebra \(A=M_2(\mathbb C)\) is unital, so \(\operatorname{Mult}(A)=A\). The ideal \(J\) has identity \((I_2,0)\), giving
\[
\rho(a,\lambda)=\theta((a,\lambda)(I_2,0))=a.
\]
The kernel is \(0\oplus\mathbb C\), a nonzero ideal disjoint from \(J\). Thus the constructed map preserves the action on \(J\) and fails to be injective exactly because that action cannot detect the second summand.

**Exercise 5.2 — intermediate: strict convergence without norm convergence.** For \(A=c_0(\mathbb N)\), identify \(\operatorname{Mult}(A)\), and let \(u_F\) be the indicator of a finite subset \(F\), directed by inclusion. Prove that \(u_F\to1\) strictly and strongly in the universal representation, but never in norm. Show that \(xu_F\to x\) strictly for every multiplier \(x\).

**Solution.** The bidual is \(\ell^\infty\), with pointwise products. Every bounded sequence multiplies a null sequence into a null sequence on both sides, so
\(\operatorname{Mult}(c_0)=\ell^\infty\). For \(a\in c_0\),
\[
\|(1-u_F)a\|=\sup_{n\notin F}|a_n|\longrightarrow0.
\]
The algebra is commutative, so this is both strict seminorm terms. The finite indicators form an increasing contractive approximate identity, hence converge strongly to \(1\) in the universal representation. For every finite \(F\), the complement is nonempty and \(\|1-u_F\|=1\), excluding norm convergence. Finally
\[
\|(x-xu_F)a\|\le\|x\|\sup_{n\notin F}|a_n|\longrightarrow0,
\]
on both sides. This also illustrates why a multiplier may be approximated by algebra elements after multiplication even when it has no norm approximation from the algebra.

**Exercise 5.3 — advanced: three matrix-sequence extensions.** Let
\[
A=c_0(\mathbb N,M_2(\mathbb C)),
\qquad
B=\{x=(x_n):x_n\text{ converges in norm to a diagonal matrix}\}.
\]
With the supremum norm, show that \(B\) is a unital C*-algebra having \(A\) as an essential ideal. Identify its quotient by \(A\), its embedding in \(\operatorname{Mult}(A)\), and the position of \(A_1\) inside it. Give a multiplier outside \(B\).

**Solution.** Norm convergence and the fact that diagonal matrices form a closed C*-subalgebra show that \(B\) is closed under products and adjoints, is norm closed, and contains the constant identity sequence. Pointwise multiplication preserves null sequences, so \(A\) is an ideal. If \(xA=0\), multiply by a sequence supported at one index and having value \(I_2\) there. This gives \(x_n=0\) at each index, so the ideal is essential.

The dual of \(A\) consists of summable sequences of linear functionals on \(M_2\), with norm the sum of their norms: restriction to each coordinate gives the sequence, finite supported tests give the sum bound, and absolute convergence reconstructs the functional. Since \(M_2\) is finite dimensional, dualizing gives
\[
A^{**}=\ell^\infty(\mathbb N,M_2),
\]
with coordinatewise operations. Every such bounded matrix sequence preserves \(A\) on both sides. Hence it is the multiplier algebra, and the embedding of \(B\) in Theorem 3.1 is its ordinary inclusion.

Taking the norm limit is an onto *-homomorphism \(B\to D_2\), the diagonal two-by-two algebra, with kernel \(A\). Thus \(B/A\cong D_2\cong\mathbb C^2\). The unitization \(A_1\) consists exactly of sequences whose limits are scalar matrices. Consequently
\[
A_1\subsetneq B\subsetneq\operatorname{Mult}(A).
\]
A constant nonscalar diagonal sequence proves the first strict inclusion. The bounded sequence \(x_n=\operatorname{diag}((-1)^n,0)\) is a multiplier and has no norm limit, proving the second. The extension property permits both intermediate algebras, while the multiplier algebra contains every bounded coordinate action.

## References

[Blackadar] Bruce Blackadar, [*Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*](https://bruceblackadar.com/Mathematics/Cycr.pdf), author’s revised and corrected online version of the 2005 book, accessed 3 October 2026.
