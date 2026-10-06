# Contractive retractions and the algebraic structure of expectations

Course: OA-MOD. English course draft. The scalar Tomiyama theorem retains its existing programme owner. This course supplies the assigned shorter proof and matrix-strengthening arguments, now with exact written prerequisites and an explicit bidual comparison. Current revision by GPT-6 Astra (OpenAI), Ultra, October 2026, CC0; earlier authorship and alternative proofs are retained.

An expectation is useful in weight theory because multiplication by an element of the smaller algebra can pass through it. The exact programme Tomiyama theorem supplies this compatibility and positivity from a single norm condition. The retained shorter proof and matrix arguments explain the mechanism and establish all matrix positivity inequalities. The domain and range may be nonunital C*-algebras. No separability, countability, normality, or faithful state is assumed.

## Objects and dependency contracts

A C*-subalgebra is norm closed and closed under the inherited product and involution. An inclusion \(B\subseteq A\) need not preserve an identity, even when both algebras have identities. A **contractive retraction** is a complex-linear map

\[
\begin{gathered}
E:A\longrightarrow B,\\ E(b)=b\quad(b\in B),\\
\|E(a)\|\leq\|a\|\quad(a\in A).
\end{gathered}
\]

In particular, the composite map \(A\to B\hookrightarrow A\) is idempotent. The word projection in this context refers to that bounded linear map, not to an element \(p=p^*=p^2\) of an algebra.

The precise prerequisite contracts are:

1. **Continuous functional calculus.** Continuous functional calculus, positive square roots and positive and negative parts of a self-adjoint element; the C*-identity; positivity of \(x^*x\); and the order inequalities \(0\leq x^*x\leq\|x\|^2 1\) in a unitization. These facts also apply to matrix algebras. A faithful representation identifies the intrinsic order with operator order.
2. **States and positivity.** On a nonzero unital C*-algebra, a state is a positive linear functional taking value one at the identity. States have norm one and determine the positive cone: an element is positive if all its state evaluations are nonnegative real numbers. This contract includes existence of enough states, not just existence of a particular faithful state. No faithful state is required here.
3. **The C*-algebra bidual.** For every C*-algebra \(C\), the bidual \(C^{**}\), with its canonical product and involution, is a von Neumann algebra and the canonical embedding is an isometric *-homomorphism. If \(C\) is unital, its canonical embedding sends \(1_C\) to the identity of \(C^{**}\). An isometric inclusion \(i:B\hookrightarrow A\) induces an isometric normal *-homomorphism \(i^{**}:B^{**}\hookrightarrow A^{**}\). Its image is a von Neumann subalgebra which can have a different identity. Every bounded map \(T:A\to B\) has a weak-star continuous second adjoint \(T^{**}:A^{**}\to B^{**}\) of the same norm. Second adjoints preserve compositions and extend the original maps. The weak-star topologies here are \(\sigma(A^{**},A^*)\) and \(\sigma(B^{**},B^*)\).
4. **Spectral projections.** In a von Neumann algebra, each bounded self-adjoint element is a norm limit of finite real linear combinations of its spectral projections, all lying in that algebra. This follows by uniform approximation of the identity function on its bounded spectrum by step functions in the bounded Borel spectral calculus.
5. **Normal positive maps.** A bounded positive linear map between von Neumann algebras is normal, equivalently ultraweakly continuous, if and only if it preserves the suprema of bounded increasing nets of positive elements. This contract is used in the nonnormal example and in the last exercise, not in the retraction theorem itself.

These inputs have the following exact written providers. AC1–4 proves abstract unital calculus and order, and UZ06–07 supplies the nonunital calculus and inherited cone. ST02–03 proves the state norm and the positivity test, including its application to initially nonself-adjoint elements. UB03–05 constructs the universal representation and identifies the Banach bidual as a von Neumann algebra. UB09 proves the inclusion and its weak-star closed range; AB01 proves second-adjoint norm equality, naturality and composition. SK04 and SK08 constructs the spectral projections and their algebra membership. NP04 proves the normal-map equivalence used in the examples. The earlier programme route below retains its ownership and historical status; the local argument uses these written providers rather than an external proof citation.

## A scalar norm test for positivity

**Lemma.** Let \(C\) be a nonzero unital C*-algebra. If a complex-linear functional \(f:C\to\mathbb C\) satisfies \(\|f\|\leq1\) and \(f(1)=1\), then \(f\) is positive.

**Proof in the present coordinates.** If \(h=h^*\) and \(t\in\mathbb R\), contractivity and the C*-identity give

\[
 \begin{gathered}|1+itf(h)|^2\leq\|1+ith\|^2\\
 \leq1+t^2\|h\|^2.\end{gathered}
\]

Write \(f(h)=a+ib\), with \(a,b\) real. After expansion and subtraction of one, the inequality becomes

\[
 -2tb+t^2|f(h)|^2\leq t^2\|h\|^2.
\]

Divide by positive \(t\) and let it decrease to zero to get \(b\geq0\); use negative \(t\) to get \(b\leq0\). Thus \(f(h)\) is real. If \(0\leq h\leq1\), AC4 gives \(\|1-h\|\leq1\), so \(f(h)=1-f(1-h)\geq0\). Scaling proves positivity for every positive element, including zero. This proves the asserted norm test without a representation or a faithful state.

**Earlier programme route.** **Lemma 8.1** of [The universal enveloping von Neumann algebra and W*-algebras](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-20), by Claude Opus 5.5 (Anthropic), September 2026, CC0, proves positivity from a norming net. Its unital specialization takes the constant net at the identity. The preceding argument is a local alternative; it neither replaces that more general lemma nor changes its canonical ownership.

Consequently, a contractive linear map between nonzero unital C*-algebras which sends identity to identity is positive: compose it with each state of the range and apply the lemma and the state-order contract. The identities in this assertion are the respective identities of the domain and range.

## The norm estimate that excludes a wrong corner

**Lemma.** Suppose \(M\) is a unital C*-algebra, \(N\subseteq M\) is a C*-subalgebra, and \(P:M\to N\) is a contractive retraction. For every projection \(p\in N\) and every \(x\in M\),

\[
pP((1-p)x)=0.
\]

Neither positivity of \(P\) nor an identity for \(N\) is a hypothesis.

The programme **Remark 8.6** explicitly assigns the shorter orthogonal-support route to OA-MOD. The following retained estimate supplies that route; the general scalar theorem keeps its programme owner.

**Proof.** Put \(z=(1-p)x\) and \(y=pP(z)\in N\). Then \(z^*y=y^*z=0\). For \(t>0\), retraction, contractivity, and the C*-identity give

\[
\begin{gathered}(1+t)\|y\|=\|pP(z+ty)\|\\
\leq\|z+ty\|\\
\leq\bigl(\|z\|^2+t^2\|y\|^2\bigr)^{1/2}.\end{gathered}
\]

After squaring and cancelling \(t^2\|y\|^2\), this becomes

\[
(1+2t)\|y\|^2\leq\|z\|^2.
\]

Letting \(t\) tend to infinity yields \(y=0\). ∎

The estimate uses orthogonal **left** supports: it gives \(z^*y=0\). One must not replace this by the generally false assertion \(zy^*=0\). This distinction fixes which side of the expectation is being controlled.

## Full nonunital retraction theorem

**Theorem (Tomiyama).** Let \(A\) be a C*-algebra, let \(B\subseteq A\) be a C*-subalgebra, and let \(E:A\to B\) be a contractive retraction. Then

\[
E(A_+)\subseteq B_+,\qquad E(x^*)=E(x)^*,
\]

and

\[
\begin{gathered}E(bxc)=bE(x)c\\
(x\in A,\ b,c\in B).\end{gathered}
\]

If \(B\neq\{0\}\), then \(\|E\|=1\). If \(B=\{0\}\), then \(E=0\) and \(\|E\|=0\). If \(A\) is unital and \(B\neq\{0\}\), the range is automatically unital and \(E(1_A)\) is its identity; this identity need not be \(1_A\).

**Exact written programme owner.** Read **Definition 8.4 and Theorem 8.5(1)–(4)** of [The universal enveloping von Neumann algebra and W*-algebras](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-21), by Claude Opus 5.5 (Anthropic), September 2026, CC0. Definition 8.4 includes contractive retractions and the zero range; the full theorem proof treats nonunital algebras, a range identity different from the ambient identity, both module identities and scalar Schwarz. That existing theorem owns the general scalar result.

**Remark 8.6** of that lesson explicitly assigns the shorter orthogonal-support proof and complete positivity to OA-MOD. The entire shorter proof below is retained at its stated contracts. This local proof route does not create duplicate canonical ownership of Tomiyama's theorem.

**Retained shorter proof.** The zero range case is immediate, so assume \(B\neq\{0\}\). We first prove the assertion for a contractive retraction \(P:M\to N\) with \(M\) a von Neumann algebra and \(N\) a von Neumann subalgebra. Write \(1\) for the identity of \(M\) and \(e\) for that of \(N\). Then \(e\) is a nonzero projection in \(M\), and \(n=ene\) for \(n\in N\).

For a projection \(p\in N\), put \(r=e-p\), which is also a projection in \(N\). The preceding lemma gives

\[
pP((1-p)x)=0.
\]

Apply the same lemma to \(r\) and the element \(px\). Since \((1-r)p=p\), it gives \(rP(px)=0\). Because \(eP(px)=P(px)\), this implies \(P(px)=pP(px)\). Decomposing \(x=px+(1-p)x\) therefore proves

\[
P(px)=pP(x).
\tag{CE1}
\]

This calculation allows \(p=0\), \(p=e\), and \(r=0\). In particular, setting \(p=e\) and \(x=1\) in (CE1) gives

\[
P(1)=eP(1)=P(e)=e.
\]

The scalar norm test, applied after composition with each state of \(N\), now proves that \(P\) is positive. A positive linear map preserves the involution: write a self-adjoint element as the difference of its positive and negative parts, then decompose an arbitrary element into real and imaginary self-adjoint parts.

Taking adjoints in (CE1), with \(x^*\) in place of \(x\), gives \(P(xp)=P(x)p\). For \(b=b^*\in N\), choose finite real linear combinations \(b_k\) of spectral projections of \(b\) with \(\|b_k-b\|\to0\). Contractivity gives

\[
\begin{gathered}\|P(b_kx)-P(bx)\|\\\leq\|b_k-b\|\|x\|\to0,\end{gathered}
\]

and \(b_kP(x)\to bP(x)\) in norm. Thus \(P(bx)=bP(x)\); the same argument proves the right-module identity. Splitting an arbitrary \(b\in N\) into self-adjoint real and imaginary parts proves both identities for every \(b\). Applying them successively yields \(P(bxc)=bP(x)c\). No normality assumption on \(P\) was needed in this von Neumann algebra argument: the approximation used was in norm.

For the original C*-algebras, let \(i:B\hookrightarrow A\) denote the inclusion and \(j_A:A\to A^{**}\), \(j_B:B\to B^{**}\) the evaluation embeddings. UB05 and UB09 prove that

\[
 i^{**}:B^{**}\longrightarrow A^{**}
\]

is an isometric normal *-homomorphism, with weak-star closed range \(N=i^{**}(B^{**})\). In particular \(N\) is a von Neumann subalgebra; its identity is \(e=i^{**}(1_{B^{**}})\), which need not be the ambient identity. The Banach second adjoint of the original retraction is the complex-linear normal contraction

\[
 E^{**}:A^{**}\longrightarrow B^{**}.
\]

Here normality means weak-star continuity; positivity has not yet been proved or assumed. Because \(Ei=\operatorname{id}_B\), the composition identity in AB01 gives \(E^{**}i^{**}=\operatorname{id}_{B^{**}}\). Consequently the well-typed map

\[
 P=i^{**}E^{**}:A^{**}\longrightarrow N
\]

is a contractive retraction. The von Neumann argument applies to \(P\).

We spell out the return to the original algebras. Naturality in AB01 gives \(E^{**}j_A=j_BE\) and \(i^{**}j_B=j_Ai\), hence \(Pj_A=j_AiE\). If \(a\geq0\) in \(A\), then \(Pj_A(a)\geq0\). Injectivity first makes \(E(a)\) self-adjoint, because its image equals its adjoint. It also makes \(E(a)\) positive: continuous calculus sends its negative part to the negative part of its positive image, hence to zero, and an injective map cannot annihilate a nonzero element. This is the same \(f(0)=0\) calculus used in UB02 and UZ07. Taking adjoints and using injectivity similarly returns preservation of the involution. For \(b,c\in B\) and \(x\in A\), apply bimodularity of \(P\) to \(j_A(b)j_A(x)j_A(c)\); both outer factors lie in \(N\). Naturality and injectivity of \(j_Ai\) give exactly \(E(bxc)=bE(x)c\). No claim that a nonunital algebra equals its bidual has been made.

If \(b\in B\) has norm one, then \(\|E\|\geq\|E(b)\|=1\), proving the norm assertion. Finally suppose \(A\) is unital. The element \(E(1_A)\in B\), viewed in \(B^{**}\), is the identity of \(B^{**}\) by the von Neumann algebra argument. It therefore multiplies every element of \(B\) to itself on both sides. Thus it is the identity of \(B\). ∎

A positive \(B\)-bimodule retraction is called a **conditional expectation** here. The theorem establishes that every contractive retraction has this structure. Later units impose normality, faithfulness, or compatibility with a specified weight as additional properties. They are not part of this theorem's hypotheses or automatic conclusions.

## Detecting matrix positivity using algebra-valued columns

The next lemma gives a direct route to complete positivity without a dilation of \(E\). Matrix C*-algebras may be realized using the faithful isometric representation in UB03: \(M_n(C)\) acts on the finite Hilbert sum with the usual matrix product and adjoint. Its operator norm is complete because it lies between the maximum entry norm and \(n\) times that norm. Thus AC1–4 and UZ06–07 apply to this C*-algebra too, including its nonunital case.

**Lemma.** Let \(C\) be a possibly nonunital C*-algebra and let \(H=[h_{ij}]\in M_n(C)\) be self-adjoint. Then \(H\geq0\) if and only if

\[
\sum_{i,j=1}^n c_i^*h_{ij}c_j\geq0.
\tag{CE2}
\]

The inequality is required for every column \((c_1,\ldots,c_n)\in C^n\).

**Proof.** If \(H\geq0\), write \(H=K^*K\), with \(K\in M_n(C)\). The expression in (CE2) is

\[
\sum_{k=1}^n\left(\sum_i k_{ki}c_i\right)^*
\left(\sum_j k_{kj}c_j\right),
\]

and is positive.

Conversely, suppose (CE2) holds. Let \(D=H_-\), the negative part of \(H\), and set \(Y=D^{1/2}\). These elements lie in \(M_n(C)\), even when \(C\) has no identity: the continuous functions defining them vanish at zero. Functional calculus gives

\[
YHY=-D^2.
\]

Use each column of \(Y\) as the column \((c_i)\) in (CE2). Every diagonal entry of \(-D^2\) is then positive. Every diagonal entry of \(D^2=D^*D\) is also positive, so these diagonal entries all vanish. For each column index \(k\),

\[
0=(D^*D)_{kk}=\sum_i d_{ik}^*d_{ik}.
\]

Each summand is positive and dominated by zero, hence each \(d_{ik}=0\). Consequently \(D=0\), and \(H\geq0\). ∎

## Schwarz inequalities, complete positivity, and matrix norms

**Theorem.** Under the hypotheses of OA-MOD-CE-004,

\[
\begin{gathered}E(x)^*E(x)\\\leq E(x^*x),\\
E(x)E(x)^*\\\leq E(xx^*)\end{gathered}
\tag{CE3}
\]

for every \(x\in A\).
For every positive integer \(n\), the entrywise map

\[
\begin{gathered}E_n:M_n(A)\longrightarrow M_n(B),\\
E_n([x_{ij}])=[E(x_{ij})]\end{gathered}
\]

is positive and contractive. Thus \(E\) is completely positive and completely contractive. If \(B\neq\{0\}\), every \(E_n\) has norm one.

The scalar inequalities (CE3) are the existing programme **Theorem 8.5(3)**, also applied to \(x^*\). The retained residual identity explains that imported inequality and extends it to the matrix arguments assigned here by **Remark 8.6**. The matrix-column criterion, complete positivity, complete contractivity and matrix defect proofs remain local course work.

**Proof.** Set \(r=x-E(x)\). Positivity and bimodularity give the identity

\[
\begin{gathered}0\leq E(r^*r)\\=E(x^*x)\\-E(x)^*E(x).\end{gathered}
\tag{CE4}
\]

In detail, the two mixed terms in the expansion of \(r^*r\) both map to \(E(x)^*E(x)\), and its last term is fixed by \(E\). This proves the first inequality in (CE3); applying it to \(x^*\) proves the second.

To prove matrix positivity, let \(X=[x_{ij}]\geq0\) in \(M_n(A)\). For a column \((b_i)\in B^n\), the element \(\sum_{ij}b_i^*x_{ij}b_j\) is positive in \(A\). Therefore

\[
\begin{gathered}\sum_{ij}b_i^*E(x_{ij})b_j\\
=E\left(\sum_{ij}b_i^*x_{ij}b_j\right)\geq0.\end{gathered}
\]

The matrix \([E(x_{ij})]\) is self-adjoint because \(E\) preserves the involution. OA-MOD-CE-005 proves that it is positive. This works for all \(n\) and for nonunital \(B\).

For the norm assertion, first use the extension \(P:A^{**}\to B^{**}\) from OA-MOD-CE-004, with respective identities \(1\) and \(e\). The same matrix-positivity proof applies to \(P\). Matrix multiplication and bimodularity show that \(P_n\) is a bimodule map over \(M_n(B^{**})\). Expanding the residual \(X-P_n(X)\) just as in (CE4) gives

\[
\begin{gathered}P_n(X)^*P_n(X)\leq P_n(X^*X)\\
\leq\|X\|^2\operatorname{diag}(e,\ldots,e).\end{gathered}
\]

The last inequality uses positivity and \(P_n(1_n)=\operatorname{diag}(e,\ldots,e)\). Hence \(\|P_n(X)\|\leq\|X\|\). Restrict to \(M_n(A)\) to obtain contractivity of \(E_n\). If the range is nonzero, it contains an element of norm one fixed by \(E_n\), so \(\|E_n\|=1\). If the range is zero, \(E_n=0\). ∎

Notice the order of the proof. Positivity of a map alone would not justify the general Schwarz inequality \(E(x)^*E(x)\leq E(x^*x)\). Here bimodularity and retraction supply the residual identity that proves it.

## The positive defect of forgetting information

For any \(x_1,\ldots,x_n\in A\), define a matrix in \(M_n(B)\) by

\[
D_{ij}=E(x_i^*x_j)-E(x_i)^*E(x_j).
\]

Then \([D_{ij}]\geq0\).

**Proof.** Put \(r_i=x_i-E(x_i)\). Bimodularity and retraction give \(D_{ij}=E(r_i^*r_j)\). The Gram matrix \([r_i^*r_j]\) is positive: it equals \(R^*R\), where \(R\) is the row matrix \((r_1,\ldots,r_n)\). Complete positivity now gives the claim. ∎

The scalar defect in (CE4) is the one-element case. The full matrix statement keeps all cross terms, which is the form needed when an expectation is used to construct a Hilbert module or a correspondence. It is a bounded-algebra input to those constructions; it does not assert a theorem about unbounded operator-valued weights.

If \(E\) is faithful in the sense that \(a\in A_+\) and \(E(a)=0\) imply \(a=0\), then equality in the first inequality of (CE3) holds exactly when \(x\in B\). Indeed, (CE4) and faithfulness imply \(r^*r=0\), hence \(r=0\). Without faithfulness this conclusion fails, as the next example shows.

## Worked example: an infinite corner and its exact defect

Let \(H=K\oplus L\) be an orthogonal decomposition of an arbitrary Hilbert space, and let \(p\) be the orthogonal projection onto \(K\). Neither summand is assumed separable. Put

\[
\begin{gathered}A=\mathcal K(H),\\ B=p\mathcal K(H)p,\\ E(x)=pxp.\end{gathered}
\]

Here \(\mathcal K(H)\) denotes the norm closure of the finite-rank operators. Compression preserves finite rank and is norm continuous, so \(E(x)\in B\). The formula \(E(b)=b\) for \(b\in B\) and the estimate \(\|pxp\|\leq\|x\|\) verify the hypotheses of the theorem. Thus \(E\) is completely positive and completely contractive.

If \(K\) is infinite dimensional, \(B\cong\mathcal K(K)\) is nonunital. If also \(H\) is infinite dimensional, this is a genuinely nonunital instance of the theorem. The projection \(p\) is then an element of \(B(H)\) used for compression, not an asserted element of \(B\). For \(K=\{0\}\), the map and its range are zero; for \(L=\{0\}\), it is the identity map.

Its Schwarz defect can be calculated without invoking an abstract dilation:

\[
\begin{gathered}E(x^*x)-E(x)^*E(x)\\=px^*(1-p)xp\\
=\bigl((1-p)xp\bigr)^*\bigl((1-p)xp\bigr).\end{gathered}
\]

The defect vanishes exactly when \((1-p)xp=0\). If \(L\neq\{0\}\), this does not force \(x\in B\): choose a nonzero compact operator supported on \(L\), which has zero defect and zero expectation. A rank-one positive operator supported on \(L\) also shows directly that \(E\) is not faithful in this case. Thus the equality conclusion of OA-MOD-CE-007 needs its faithfulness hypothesis.

## Worked example: norm one does not imply normality

Let \(\mathcal U\) be a free ultrafilter on \(\mathbb N\). It exists by extending the cofinite filter using AB03; no finite set can belong to the extension because its cofinite complement already does. The compactness and ultrafilter criterion proved in AB03–04 justify the limits below. The bounded diagonal algebra on \(\ell^2(\mathbb N)\) is a von Neumann algebra by CY05. For a bounded complex sequence \(a=(a_n)\), set

\[
\ell(a)=\lim_{n\to\mathcal U}a_n.
\]

The limit exists and is unique because the closure of the sequence's range is compact in a closed bounded disk. Continuity of addition and scalar multiplication shows that \(\ell\) is complex linear. Limits of nonnegative sequences are nonnegative, \(\ell(1)=1\), and \(|\ell(a)|\leq\|a\|_\infty\). Hence

\[
E:\ell^\infty(\mathbb N)\longrightarrow\mathbb C1,
\qquad E(a)=\ell(a)1
\]

is a contractive retraction.

Let \(q_k\) be the indicator sequence of \(\{1,\ldots,k\}\). Then \(q_k\uparrow1\) in the von Neumann algebra \(\ell^\infty(\mathbb N)\), but \(\ell(q_k)=0\) because the ultrafilter contains no finite set. Consequently \(E(q_k)=0\) for every \(k\), whereas \(E(1)=1\). The map fails to preserve this bounded increasing supremum and is not normal.

The bidual extension used in the proof does not contradict this example. Its weak-star continuity concerns the canonical bidual topologies with preduals \(A^*\) and \(B^*\). For an algebra which is already a von Neumann algebra, that construction need not identify the canonical copy of \(A\) in \(A^{**}\) with all of \(A^{**}\), nor does it change a nonnormal map on \(A\) into a normal one on \(A\).

## Exercises

1. **A proper identity.** Let \(A=M_3(\mathbb C)\), let \(e=\operatorname{diag}(1,1,0)\), and let \(B=eAe\). Compute \(E(1_A)\), \(\|E\|\), and the Schwarz defect for \(E(x)=exe\). Determine whether \(E\) is faithful.
2. **The norm hypothesis is sharp.** For \(t>0\), define a retraction from \(\mathbb C^2\) onto its diagonal subalgebra by

   \[
   \begin{gathered}\alpha=(1+t)z-tw,\\ F_t(z,w)=(\alpha,\alpha).\end{gathered}
   \]

   Compute its norm for the supremum norm, and show that it is not positive.
3. **An expected ideal must split off.** Let \(I\) be a closed two-sided ideal in a C*-algebra \(A\). Suppose there is a contractive retraction \(E:A\to I\). Prove that

   \[
   \begin{gathered}A=I\oplus I^\perp,\\
   I^\perp=\{a\in A:aI=Ia=0\},\\
   \ker E=I^\perp.\end{gathered}
   \]

   Prove that \(E\) is the unique contractive retraction onto \(I\), and that it is a *-homomorphism. Conclude that a proper essential ideal admits no contractive retraction; here essential means \(I^\perp=\{0\}\).
4. **Faithful equality.** If \(E\) is faithful, prove that \(E(x^*x)=E(x)^*E(x)\) forces \(x\in B\). Exhibit the failure without faithfulness using the infinite-corner example.
5. **Composing expectations.** Suppose \(C\subseteq B\subseteq A\), with contractive retractions \(E:A\to B\) and \(F:B\to C\). Prove that \(F\circ E\) is a completely positive contractive \(C\)-bimodule retraction. If \(A,B,C\) are von Neumann algebras and both maps are normal, prove that the composite is normal.

## Solutions

**1.** Since \(E(1_A)=e\), the map is unital as a map into the unital algebra \(B\), whose identity is \(e\). Its norm is one because it fixes the norm-one element \(e\). Direct multiplication gives

\[
E(x^*x)-E(x)^*E(x)=ex^*(1-e)xe.
\]

The positive nonzero matrix \(1-e\) has expectation zero, so \(E\) is not faithful. This example separates an identity for the range from the identity of the ambient algebra.

**2.** For \(\max\{|z|,|w|\}\leq1\), the common coordinate has absolute value at most \(1+2t\). At \((z,w)=(1,-1)\), it equals \(1+2t\), so \(\|F_t\|=1+2t\). The positive element \((0,1)\) maps to \((-t,-t)\), which is not positive. Fixing a C*-subalgebra by an idempotent bounded map therefore does not suffice without the contractivity requirement.

**3.** If \(a\in\ker E\) and \(b\in I\), then \(ab,ba\in I\), because \(I\) is an ideal. Retraction and bimodularity give

\[
\begin{gathered}ab=E(ab)=E(a)b=0,\\
ba=E(ba)=bE(a)=0.\end{gathered}
\]

Thus \(\ker E\subseteq I^\perp\). Conversely, if \(a\in I^\perp\), then \(E(a)b=E(ab)=0\) for every \(b\in I\). Choose \(b=E(a)^*\in I\). Then \(E(a)E(a)^*=0\), so the C*-identity gives \(E(a)=0\). Thus \(\ker E=I^\perp\).

Every \(a\in A\) decomposes as \(E(a)+(a-E(a))\), with the terms in \(I\) and \(I^\perp\). Their intersection is zero: if \(b\in I\cap I^\perp\), then \(b^*\in I\) and \(bb^*=0\), hence \(b=0\). The annihilator \(I^\perp\) is a closed two-sided *-ideal. To verify the ideal property, for \(a\in I^\perp\), \(c\in A\), and \(b\in I\), one has \((ca)b=c(ab)=0\) and \(b(ca)=(bc)a=0\), since \(bc\in I\); the calculation for \(ac\) is the same. Taking adjoints preserves both annihilation conditions. This proves the asserted direct sum of ideals.

If \(a=b+k\) and \(a'=b'+k'\) are the decompositions, the mixed products vanish and \(kk'\in I^\perp\). Hence \(E(aa')=bb'=E(a)E(a')\). Preservation of the involution was proved in OA-MOD-CE-004, so \(E\) is a *-homomorphism. Any other contractive retraction has kernel \(I^\perp\) by the same argument and must be the coordinate projection of this decomposition; it equals \(E\). If \(I\) is essential, the decomposition forces \(A=I\).

**4.** Identity (CE4) says that the assumed equality is \(E(r^*r)=0\), where \(r=x-E(x)\). Faithfulness gives \(r^*r=0\), and the C*-identity gives \(r=0\). For failure without faithfulness, take \(L\neq\{0\}\) and choose a nonzero compact \(x\) supported on \(L\) in OA-MOD-CE-008. Then \(E(x)=E(x^*x)=0\), although \(x\notin B\).

**5.** Contractivity follows from \(\|F(E(a))\|\leq\|E(a)\|\leq\|a\|\). If \(c\in C\), then \(F(E(c))=F(c)=c\), so the composite is a retraction. For \(c,d\in C\),

\[
\begin{gathered}F(E(cad))=F(cE(a)d)\\=cF(E(a))d.\end{gathered}
\]

Its matrix amplifications are \(F_n\circ E_n\), so it is completely positive. For normality, let \(0\leq a_\alpha\uparrow a\) be a bounded increasing net in \(A\). Normality of \(E\) gives \(E(a_\alpha)\uparrow E(a)\), and then normality of \(F\) gives \(F(E(a_\alpha))\uparrow F(E(a))\). The normality assertion uses the standard equivalence between normality and preservation of bounded increasing positive suprema; it does not follow from contractivity alone.

## Antecedents, proof status, and the next questions

The norm-one retraction theorem is due to Jun Tomiyama, [“On the Projection of Norm One in W*-algebras,” *Proceedings of the Japan Academy* 33 (1957), 608–612](https://doi.org/10.3792/pja/1195524885). The assigned source is Masamichi Takesaki, *Theory of Operator Algebras I*, III.3, Definition 3.3 and Theorem 3.4, printed pp. 131–133 in the exact approved receipt-backed edition. Its full proof, including the final removal of identity assumptions, has been compared with the argument here. Jesse Peterson's [*Notes on operator algebras*, 27 April 2020, Theorem 8.3.1, pp. 143–144](https://math.vanderbilt.edu/peters10/teaching/spring2020/OperatorAlgebras.pdf) gives the short orthogonal-support route under a unital inclusion hypothesis. CE003–004 retains that norm mechanism with the range identity distinguished from the ambient identity and the nonunital comparison proved explicitly. The programme Lemma 8.1 and Theorem 8.5 retain their CC0 attribution and canonical ownership; Remark 8.6 assigns the shorter proof and complete positivity to this course. The lesson has its own exposition, matrix-defect treatment and examples. Source-book copies, prose and figures are not reproduced.

The lesson supplies positivity, bimodularity and scalar Schwarz through its retained shorter argument and exact written prerequisites, together with complete positivity, complete contractivity and matrix defects for arbitrary C*-algebras.

The following B9 questions are not answered by a contractive retraction theorem: existence of normal expectations preserving a prescribed normal semifinite faithful weight; the modular invariance criterion for that existence; the domains and extended positive values of general operator-valued weights; and the construction of correspondences and relative tensor products from such data. Those obligations remain in the course, with their full hypotheses. This unit supplies bounded expectation machinery to them.
