# Split faces and semicontinuous quotient lifts

*Written by GPT-6.1 Sol (OpenAI), Ultra, September–October 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

A quotient of a C*-algebra is visible in the positive functionals that vanish on its kernel. Those functionals form a closed split face of the quasi-state space. Extending affine functions from that face gives lifts of semicontinuous operators in the quotient bidual.

We prove the face description and all three lifting statements: the norm-closed upper cone, the actual upper-limit class after adjoining the identity, and its norm closure. An explicit central lift preserves the norm and preserves positivity when the element is positive. The state-space argument keeps track of the norm of both positive components at a convergent state.

Use the split-face and affine evaluation models in [Affine approximation and quasi-state spaces](../reader/affine-approximation-and-quasi-state-spaces.html), Sections 2–4; the quasi-state characterization and unitized class in [Monotone approximation and semicontinuous operators](../reader/monotone-approximation-and-semicontinuous-operators.html), Theorems 2.1 and 4.1; and the [state and resolvent criterion](../reader/open-projections-and-closed-one-sided-ideals.html#the-state-and-resolvent-criterion), Theorem 1.1, and [central ideal restriction](../reader/open-projections-and-closed-one-sided-ideals.html#changing-the-algebra-changes-its-identity), Proposition 4.1. For bidual quotient summands, [The universal enveloping von Neumann algebra](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-06) supplies Lemma 4.2, together with Lemma 2.1 and the faithful nondegenerate case of Theorem 3.3, using its stated background on normal extensions. The freely readable [Brown] gives a broader closed-face framework. Our norm-preserving quotient lift uses the central ideal decomposition proved below; its hypotheses allow every C*-algebra.

## 1. Extending from a closed split face

Let \(K\) be a nonempty compact convex subset of a Hausdorff locally convex real space. Suppose \(F\) is a nonempty closed split face, with complementary face \(G\). Thus each point has a unique splitting
\[
k=\lambda y+(1-\lambda)v,
\quad y\in F,\quad v\in G,\quad 0\le\lambda\le1,
\tag{1.1}
\]
with unused endpoint components ignored. The weight \(\lambda\) is affine; the positive-weight components combine by the corresponding normalized convex combinations. The complementary face need not be closed. If \(F=K\), the extension below is simply the original function.

**Lemma 1.1 — a bounded semicontinuous extension.** Let \(f:F\to\mathbb R\) be bounded, affine and lower semicontinuous. For any \(c\ge\sup_F f\), define
\[
\widetilde f(k)=\lambda f(y)+(1-\lambda)c.
\tag{1.2}
\]
This is a bounded lower semicontinuous affine extension of \(f\) to \(K\). If \(f\ge0\) and \(c\ge0\), it is positive. An upper semicontinuous bounded affine function has an upper semicontinuous bounded affine extension, obtained using a constant below its infimum.

**Proof.** The split decomposition makes (1.2) well defined and affine. Its values lie between the lower bound of \(f\) and \(c\), and it agrees with \(f\) on \(F\). Positivity is immediate under the stated assumptions.

Consider the two compact convex sets
\[
E_F=\{(y,t):y\in F,\ f(y)\le t\le c\},
\qquad E_K=K\times\{c\}.
\]
The first is compact because \(F\) is compact, \(f\) is bounded and lower semicontinuous, and its displayed upper strip is closed. The convex hull of these two sets is compact: it is the continuous image of
\([0,1]\times E_F\times E_K\) under the convex-combination map. We claim that this hull is precisely
\[
E=\{(k,t):k\in K,\ \widetilde f(k)\le t\le c\}.
\tag{1.3}
\]
Every point of the hull lies in \(E\), by affinity and the inequality \(\widetilde f\le c\). Conversely, for the splitting (1.1),
\[
(k,\widetilde f(k))
=\lambda(y,f(y))+(1-\lambda)(v,c)
\]
belongs to the hull. The point \((k,c)\) belongs to \(E_K\). Taking the segment between these points gives every allowed \(t\) in (1.3). Thus \(E\) is compact and closed, which proves lower semicontinuity. This argument uses \(K\times\{c\}\), whose compactness is available even if \(G\) is not closed. Applying the result to \(-f\) proves the upper semicontinuous version. \(\square\)

## 2. The faces attached to an ideal

Let \(I\) be a closed two-sided ideal of a C*-algebra \(A\), let \(B=A/I\), and let \(q:A\to B\) be the quotient map. Put \(M=A^{**}\). The increasing approximate identity of \(I\) has an open central supremum \(z\in M\). The canonical identifications are
\[
I^{**}=Mz,\qquad B^{**}=M(1-z),\qquad
q^{**}(x)=(1-z)x.
\tag{2.1}
\]
The identity of the quotient summand is \(1-z\), also denoted \(1_B\). Functionals are identified with their normal bidual extensions. Restriction to \(I\) identifies \(I^*\) with \(A^*z\); pullback by \(q\) identifies \(B^*\) with \(A^*(1-z)\). The second identification is a weak* homeomorphism onto its image, since evaluations at elements of \(B\) are exactly evaluations at any chosen preimages in \(A\).

**Proposition 2.1.** Inside \(Q(A)=\{\varphi\in A^*_+:\|\varphi\|\le1\}\), the face
\[
F=\{\varphi\in Q(A):\varphi(z)=0\}
\tag{2.2}
\]
is closed and split, and identifies with \(Q(B)\). Its complementary face is
\[
G=\{\varphi\in Q(A):\varphi(z)=1\},
\tag{2.3}
\]
which identifies with \(S(I)\). Inside \(S(A)\), the same two conditions identify \(S(B)\) and \(S(I)\) as complementary split faces; \(S(B)\) is closed for the relative weak* topology.

**Proof.** Since \(z\) is open, its evaluation is lower semicontinuous on \(Q(A)\). It is nonnegative, so its zero set \(F\) is closed. Positivity of the evaluation makes the zero set a face. The upper bound \(\varphi(z)\le\|\varphi\|\le1\) makes its level set at one a face as well.

For \(\varphi\in Q(A)\), let
\[
t=\varphi(z),\qquad
\eta=z\varphi,\qquad \rho=(1-z)\varphi.
\tag{2.4}
\]
Centrality makes \(\eta,\rho\) positive, and their norms are \(t\) and \(\|\varphi\|-t\). If \(0<t<1\), then
\[
\varphi=(1-t)\frac{\rho}{1-t}+t\frac{\eta}{t},
\qquad
\frac{\rho}{1-t}\in F,\quad \frac{\eta}{t}\in G.
\tag{2.5}
\]
The endpoint cases use just the nonzero component. Conversely, evaluating any split decomposition at \(z\) determines the weight \(t\), and multiplication by the two central projections determines both components. This proves uniqueness.

The condition \(\varphi(z)=0\) is equivalent to vanishing on \(I\). In one direction use a positive approximate identity of \(I\) and normality. In the other, \(z\varphi\) is a positive functional of norm zero, so \(\varphi\) vanishes on \(Mz\). Thus \(F=q^*Q(B)\). A positive functional satisfying \(\varphi(z)=1\) has norm one and is supported on \(z\), giving the stated identification with \(S(I)\).

If \(\varphi\) is a state, then \(\|\rho\|=1-t\). Hence the quotient component in (2.5) is also a state. Intersecting (2.2) with \(S(A)\) gives a relatively closed face. This proves the state-space assertion. If a quotient or ideal is zero, its state face is empty and the corresponding weight is always zero; the remaining splitting is trivial. \(\square\)

The ideal states need not form a closed face. For \(A=C([0,1])\) and \(I\) the functions vanishing at zero, evaluation states at positive points belong to \(S(I)\), while their weak* limit at zero is a quotient state.

## 3. The quotient lifting theorem

For any C*-algebra \(E\), use its own bidual identity to define
\[
\begin{aligned}
C_E&=\overline{E_{\mathrm{sa}}^\uparrow}^{\|\cdot\|},\\
T_E&=(E+\mathbb C1_E)_{\mathrm{sa}}^\uparrow
=\mathbb R1_E+C_E,\\
D_E&=\overline{T_E}^{\|\cdot\|}.
\end{aligned}
\tag{3.1}
\]
The equality in the middle is the exact unitized-class theorem. The two norm-closed classes are characterized by lower semicontinuous evaluation on \(Q(E)\) and on \(S(E)\), respectively.

**Theorem 3.1 — all three classes lift.** For every onto C*-homomorphism \(q:A\to B\),
\[
q^{**}(C_A)=C_B,\qquad
q^{**}(T_A)=T_B,\qquad
q^{**}(D_A)=D_B.
\tag{3.2}
\]
For \(x\in C_B\) or \(x\in D_B\), an explicit lift in the corresponding class is
\[
L(x)=x+\|x\|z\in M_{\mathrm{sa}},
\tag{3.3}
\]
where \(x\) is viewed in \(M(1-z)\). This lift has norm \(\|x\|\); it is positive if \(x\) is positive. The zero quotient has only zero classes, so its assertions are immediate.

**Proof for \(C\).** Normality sends a bounded increasing net in \(A_{\mathrm{sa}}\) to one in \(B_{\mathrm{sa}}\), preserving its supremum. Contractivity then gives \(q^{**}(C_A)\subset C_B\).

Conversely let \(x\in C_B\) and \(c=\|x\|\). Its evaluation \(f\) on \(Q(B)=F\) is bounded, affine and lower semicontinuous, and \(f\le c\). Lemma 1.1 extends it using the constant \(c\) on the complementary face \(S(I)\). For the splitting (2.5), the extension is
\[
\widetilde f(\varphi)=\rho(x)+ct
=\varphi(x+cz).
\tag{3.4}
\]
It is lower semicontinuous on \(Q(A)\), so the quasi-state characterization gives \(x+cz\in C_A\). Multiplication by \(1-z\) recovers \(x\). Since its two central blocks are \(x\) and \(cz\), its norm is \(c\) when \(x\ne0\), and is zero otherwise. If \(x\ge0\), both blocks are positive. This proves the first equality and its extra assertions. \(\square\)

**Proof for \(T\).** Normality gives \(q^{**}(T_A)\subset T_B\), since \(q^{**}(A+\mathbb C1)=B+\mathbb C1_B\). For \(y\in T_B\), write \(y=\alpha1_B+x\) with \(x\in C_B\). A lift \(a\in C_A\) from the first part gives
\[
\alpha1+a\in\mathbb R1+C_A=T_A,
\qquad q^{**}(\alpha1+a)=y.
\]
This proves the second equality. \(\square\)

**Proof for \(D\).** Continuity and the second equality give \(q^{**}(D_A)\subset D_B\). For the reverse inclusion, let \(x\in D_B\), and again put \(c=\|x\|\). We prove directly that the evaluation of \(a=x+cz\) is lower semicontinuous on \(S(A)\).

Write \(g(\varphi)=\varphi(a)\). On the closed quotient state face \(S(B)\), the function \(f(\rho)=\rho(x)\) is lower semicontinuous and lies between \(-c\) and \(c\). On any state of \(A\),
\[
g(\varphi)=\rho(x)+c\|\eta\|,
\qquad \rho=(1-z)\varphi,\quad \eta=z\varphi.
\tag{3.5}
\]
These two components need not be weak* continuous as functions of \(\varphi\). We use compactness and preservation of total state norm instead.

Suppose \(\varphi_i\to\varphi\) weak* within \(S(A)\), and a subnet satisfies \(g(\varphi_i)\le r<g(\varphi)\). Decompose \(\varphi_i=\rho_i+\eta_i\), and put \(\lambda_i=\|\rho_i\|\). Both positive components belong to \(Q(A)\). Compactness allows a further subnet such that
\[
\rho_i\to\rho,\quad\eta_i\to\eta\quad\text{weak*},
\qquad \lambda_i\to\lambda\in[0,1].
\tag{3.6}
\]
Then \(\rho+\eta=\varphi\), and \(\rho\) vanishes on \(I\). Lower semicontinuity of the dual norm gives
\[
\|\rho\|\le\lambda,\qquad\|\eta\|\le1-\lambda.
\]
Norm additivity for positive functionals and the fact that the limit is a state force equality in both bounds:
\[
1=\|\varphi\|=\|\rho\|+\|\eta\|,
\qquad \|\rho\|=\lambda,\quad\|\eta\|=1-\lambda.
\tag{3.7}
\]
If \(\lambda>0\), the normalized quotient states \(\rho_i/\lambda_i\) converge weak* to the quotient state \(\rho/\lambda\). Lower semicontinuity of \(f\) therefore gives
\[
\liminf_i\rho_i(x)\ge\rho(x).
\tag{3.8}
\]
If \(\lambda=0\), the same conclusion follows from \(|\rho_i(x)|\le c\lambda_i\to0\) and \(\rho=0\). Consequently
\[
\liminf_i g(\varphi_i)\ge\rho(x)+c\|\eta\|.
\tag{3.9}
\]
Although \(\eta\) need not remain supported on the ideal, its quotient component satisfies
\(\eta(1-z)(x)\le c\|\eta(1-z)\|\). Since \(\rho\) is supported on \(1-z\),
\[
\begin{aligned}
g(\varphi)
&=\rho(x)+\eta(1-z)(x)+c\eta(z)\\
&\le\rho(x)+c\bigl(\|\eta(1-z)\|+\eta(z)\bigr)\\
&=\rho(x)+c\|\eta\|.
\end{aligned}
\tag{3.10}
\]
This contradicts \(g(\varphi_i)\le r<g(\varphi)\). Thus \(g\) is lower semicontinuous on states. The state characterization gives \(a\in D_A\). Its image, norm and positivity have the same properties as in the first part. This proves the third equality. \(\square\)

Applying the theorem to \(-x\) gives corresponding statements for the lower classes. The assertions are relative to the quotient's own identity and topology; they are not consequences of treating its central summand as the original algebra.

## 4. Graded exercises with solutions

**Exercise 4.1 — introductory: the ideal and quotient components.** Let \(A=M_2(\mathbb C)\oplus\mathbb C\), \(I=0\oplus\mathbb C\), and \(B=M_2(\mathbb C)\). Describe the closed quasi-state face and its complement. For a self-adjoint \(x\in B\), compute the lift (3.3) and its norm.

**Solution.** A positive functional on \(A\) has the form
\[
\varphi(a,\alpha)=\operatorname{Tr}(ha)+t\alpha,
\qquad h\ge0,\quad t\ge0,
\]
with norm \(\operatorname{Tr}(h)+t\). The quasi-state space imposes that this sum is at most one. The closed quotient face consists of \(t=0\), and its complement is the singleton \(h=0,t=1\), the state of the scalar ideal. The split weight is \(t\). Here \(z=(0,1)\), and
\[
L(x)=(x,\|x\|),\qquad\|L(x)\|=\max\{\|x\|,\|x\|\}=\|x\|.
\]
All self-adjoint elements of these finite-dimensional algebras belong to their semicontinuity classes, since constant nets suffice. The formula makes the norm and positivity of the lift explicit.

**Exercise 4.2 — intermediate: a discontinuous central lift.** Let \(A=C([0,1])\), let \(I\) be the functions vanishing at both endpoints, and identify \(B=A/I\cong\mathbb C^2\) by endpoint evaluation. Put \(b=(1,0)\). Show that its zero-on-the-ideal central lift \(b\in M(1-z)\) does not belong to \(C_A\). Determine the lift \(b+z\) from Theorem 3.1 and exhibit positive increasing continuous approximants.

**Solution.** The ideal support \(z\) evaluates to one at interior point states and to zero at either endpoint. The quotient element \(b\), viewed in the complementary summand, evaluates to one at zero and zero at every interior point. Thus \(\delta_{1/n}\to\delta_0\), whereas their values on \(b\) are zero and the limit state's value is one. Its evaluation is not lower semicontinuous, so \(b\notin C_A\).

The norm-preserving positive lift \(a=b+z\) evaluates to one on \([0,1)\) and zero at one. Its continuous approximants are
\[
a_n(t)=\min\{1,n(1-t)\}\quad(0\le t\le1).
\]
They are positive contractions and increase. Every positive functional on \(A\) is integration against a finite positive measure. Monotone convergence gives their limiting evaluation as the measure of \([0,1)\). This is also the evaluation of \(b+z\): its quotient component selects the atom at zero and its ideal component selects \((0,1)\). Positive functionals separate the bidual, so \(a_n\uparrow b+z\). The endpoint quotient is \((1,0)\), and the lift has norm one.

**Exercise 4.3 — advanced: why closedness needs a lifting argument.** In the real vector space of symmetric two-by-two matrices, consider the closed positive cone
\[
\mathcal P=\left\{\begin{pmatrix}u&v\\v&w\end{pmatrix}:u,w\ge0,\ uw\ge v^2\right\}.
\]
Let \(P\) send the matrix to \((u,v)\in\mathbb R^2\). Show that \(P\) is an open continuous surjective linear map but \(P(\mathcal P)\) is not closed. Explain which part of Theorem 3.1 supplies the extra fact required for \(D\).

**Solution.** The map is coordinate projection, so it is continuous, onto and open: the projection of a Euclidean ball contains the ball of the same radius in its two coordinate directions. If \(u>0\), any \(v\) is permitted by choosing \(w\ge v^2/u\). If \(u=0\), positivity forces \(v=0\). Therefore
\[
P(\mathcal P)=\{(u,v):u>0\}\cup\{(0,0)\}.
\]
The positive matrices
\[
\begin{pmatrix}1/n&1\\1&n\end{pmatrix}
\]
have determinant zero and images tending to \((0,1)\), which is absent from the image. The cone is closed, while its image is not. Continuity and openness alone therefore do not establish that an image of a norm-closed cone is closed. In Theorem 3.1, the explicit central lift and the state-space argument (3.6)–(3.10) prove that every element of \(D_B\) has a preimage in \(D_A\); that is the additional lifting fact.

## References

[Brown] Lawrence G. Brown, [*Semicontinuity and closed faces of C*-algebras*](https://arxiv.org/abs/1312.3624v2), arXiv:1312.3624v2, 11 July 2014. This is contextual reading on closed faces and semicontinuity. Lemma 1.1 and the central quotient lifting proof above supply the required arguments.
