# The full left Hilbert algebra obtained by dualizing twice

**Self-checked by the writing AI.**

Starting with an arbitrary left Hilbert algebra, the right-bounded vectors form a right Hilbert algebra. Dualizing once more produces the left-bounded vectors and the full left completion. This lesson proves the left-ideal covariance, the closed unbounded left multipliers, the adjoint-intersection formula, and the exact meanings of fullness and equivalence. No separability, identity element, faithful state, or modular commutant theorem is assumed.

Free comparisons are Brent Nelson, [*Tomita–Takesaki Theory*, pages 7–8](https://users.math.msu.edu/users/banelson/files/Tomita-Takesaki%20Theory.pdf), especially the primed left-bounded-vector lemmas and Definition 1.18, and François Combes, [*Poids associé à une algèbre hilbertienne à gauche*, Definition 2.1 and Lemmas 2.2–2.4, printed page 51](https://www.numdam.org/item/CM_1971__23_1_49_0.pdf). Here the multiplier pairings and graph closures are proved explicitly, using the preceding programme proofs rather than an appeal to duality without checking its hypotheses.

The exact inputs are HA04, graph involutions, HA05 and HA08 for multiplication, HA07 for graph affiliation, RD04 for the right algebra and its product core, RD05 for its generated commutant, and RD06–07 for the product-core adjoint test. BK01–02 supplies bounded extensions, adjoints and bicommutants; TC03 supplies closure and adjoint-domain tests. Only the graph-involution part of HA04 is needed, not its later polar conclusions.

## Left-bounded vectors form a covariant left ideal

Let \(\mathcal A\subseteq H\) be an arbitrary left Hilbert algebra. Write

\[
M=L(\mathcal A)'',\qquad S=\overline{(a\mapsto a^\sharp)},\qquad F=S^*.
\tag{FL.1}
\]

Use the right Hilbert algebra proved in RD04 and its commutant identity from RD05:

\[
\mathcal A_r=\mathcal B_r\cap D(F),\qquad
R(\mathcal A_r)''=M'.
\tag{FL.2}
\]

Its product and involution satisfy

\[
\eta\zeta=R_\zeta\eta,\qquad
\eta^\flat=F\eta,\qquad
R_{\eta^\flat}=R_\eta^*.
\tag{FL.3}
\]

The product span is Hilbert dense, so the representation \(R(\mathcal A_r)\) is nondegenerate. Define the left-bounded vectors relative to this right algebra by

\[
\mathcal B_l=\left\{\xi\in H:\ \exists C<\infty\ \forall\eta\in\mathcal A_r,
\ \|R_\eta\xi\|\leq C\|\eta\|\right\}.
\tag{FL.4}
\]

For \(\xi\in\mathcal B_l\), let \(\lambda_\xi\) be the bounded extension determined on the dense subspace \(\mathcal A_r\) by

\[
\lambda_\xi\eta=R_\eta\xi.
\tag{FL.5}
\]

Then \(\lambda_\xi\in M\), the assignment \(\xi\mapsto\lambda_\xi\) is linear and injective, and

\[
x\xi\in\mathcal B_l,\qquad
\lambda_{x\xi}=x\lambda_\xi
\quad(x\in M,\ \xi\in\mathcal B_l).
\tag{FL.6}
\]

Consequently \(\mathcal B_l\) is invariant under \(M\), and
\(\mathfrak n_l=\{\lambda_\xi:\xi\in\mathcal B_l\}\) is a left ideal of \(M\).

**Proof.** For \(\xi\in\mathcal B_l\), \(\eta,\zeta\in\mathcal A_r\), associativity in the right Hilbert algebra gives

\[
\lambda_\xi R_\eta\zeta
=R_{R_\eta\zeta}\xi
=R_\eta R_\zeta\xi
=R_\eta\lambda_\xi\zeta.
\]

Both sides are bounded operators and \(\mathcal A_r\) is dense, so \(\lambda_\xi\) commutes with every \(R_\eta\). Equation (FL.2) yields
\(\lambda_\xi\in R(\mathcal A_r)'=(M')'=M\).

If \(\lambda_\xi=0\), every operator in \(R(\mathcal A_r)\) kills \(\xi\). Nondegeneracy, or the positive contraction net in \(R(\mathcal A_r)\) converging strongly to the identity, gives \(\xi=0\). Thus the assignment is injective.

For \(x\in M\), every \(R_\eta\in M'\) commutes with \(x\). Hence

\[
R_\eta(x\xi)=xR_\eta\xi=x\lambda_\xi\eta,\qquad
\|R_\eta(x\xi)\|\leq\|x\lambda_\xi\|\,\|\eta\|.
\]

This proves (FL.6), and the left-ideal assertion follows immediately. Finally, if \(a\in\mathcal A\), then
\(R_\eta a=L_a\eta\); hence \(a\in\mathcal B_l\) and \(\lambda_a=L_a\). \(\square\)

## Closed left multipliers from the involution domain

Fix \(\xi\in D(S)\). On the common dense domain \(\mathcal A_r\), define

\[
A_\xi^0\eta=R_\eta\xi,\qquad
B_\xi^0\eta=R_\eta S\xi.
\tag{FL.7}
\]

Both operators are closable, and

\[
A_\xi^0\subseteq(B_\xi^0)^*,\qquad
B_\xi^0\subseteq(A_\xi^0)^*.
\tag{FL.8}
\]

Their closures

\[
\Lambda_\xi=\overline{A_\xi^0},\qquad
\Lambda_{S\xi}=\overline{B_\xi^0}
\tag{FL.9}
\]

are affiliated with \(M\). When \(\xi\) is left bounded, \(\Lambda_\xi\) is the bounded operator \(\lambda_\xi\).

**Proof.** Choose \(a_n\in\mathcal A\) with \(a_n\to\xi\) and \(a_n^\sharp\to S\xi\); \(\mathcal A\) is a graph core for \(S\). For \(\eta,\zeta\in\mathcal A_r\), boundedness of the right multipliers and the mixed product identity give

\[
\begin{aligned}
\langle R_\eta\xi,\zeta\rangle
&=\lim_n\langle R_\eta a_n,\zeta\rangle
=\lim_n\langle L_{a_n}\eta,\zeta\rangle\\
&=\lim_n\langle\eta,L_{a_n^\sharp}\zeta\rangle
=\langle\eta,R_\zeta S\xi\rangle.
\end{aligned}
\tag{FL.10}
\]

Thus each operator in (FL.7) is contained in the adjoint of the other. Each adjoint has a domain containing the dense subspace \(\mathcal A_r\), proving closability and (FL.8).

For \(\theta,\eta\in\mathcal A_r\), the right-algebra multiplication rule gives

\[
A_\xi^0(R_\theta\eta)
=R_{R_\theta\eta}\xi
=R_\theta R_\eta\xi
=R_\theta A_\xi^0\eta.
\tag{FL.11}
\]

The domain is invariant under \(R_\theta\) and under
\(R_\theta^*=R_{F\theta}\). Hence the closed graph of \(\Lambda_\xi\) is invariant under the diagonal actions of the star algebra \(R(\mathcal A_r)\). Its bicommutant is \(M'\), so the graph-projection criterion in HA07 proves that every unitary in \(M'\) preserves \(D(\Lambda_\xi)\) and commutes there with \(\Lambda_\xi\). This is affiliation with \(M\). The same proof applies to \(S\xi\). If \(\xi\in\mathcal B_l\), the bounded operator \(\lambda_\xi\) extends \(A_\xi^0\). Closedness of its graph gives one inclusion. For the reverse inclusion, choose \(\eta_n\in\mathcal A_r\) converging to any \(\eta\in H\). Boundedness gives

\[
 \eta_n\longrightarrow\eta,
 \qquad
 A_\xi^0\eta_n=\lambda_\xi\eta_n
 \longrightarrow\lambda_\xi\eta.
\]

Thus every vector in the graph of the bounded extension is a limit of vectors in the initial graph. The two closed graphs coincide. \(\square\)

## The adjoint intersection and the double algebra

Set

\[
\mathcal A^{\prime\prime}=\mathcal B_l\cap D(S).
\tag{FL.12}
\]

Then

\[
\lambda(\mathcal A^{\prime\prime})
=\mathfrak n_l\cap\mathfrak n_l^*.
\tag{FL.13}
\]

More precisely, for \(\xi,\zeta\in\mathcal B_l\),

\[
\lambda_\xi^*=\lambda_\zeta
\quad\Longleftrightarrow\quad
\xi\in D(S)\ \text{and}\ S\xi=\zeta.
\tag{FL.14}
\]

With product \(\xi\zeta=\lambda_\xi\zeta\) and involution
\(\xi^\sharp=S\xi\), the space \(\mathcal A^{\prime\prime}\) is a left Hilbert algebra containing \(\mathcal A\). Its closed involution is \(S\), and

\[
\lambda(\mathcal A^{\prime\prime})''=M.
\tag{FL.15}
\]

**Proof.** If \(\xi\in\mathcal A^{\prime\prime}\), equation (FL.10) and boundedness of \(\lambda_\xi\) show, for every \(\zeta\in\mathcal A_r\),

\[
R_\zeta S\xi=\lambda_\xi^*\zeta.
\]

Thus \(S\xi\in\mathcal B_l\) and
\(\lambda_{S\xi}=\lambda_\xi^*\). Since \(S(D(S))=D(S)\), this proves one implication in (FL.14) and the inclusion from left to right in (FL.13).

Conversely suppose \(\lambda_\xi^*=\lambda_\zeta\). For
\(\eta_1,\eta_2\in\mathcal A_r\),

\[
\begin{aligned}
\langle R_{\eta_1}^*\eta_2,\xi\rangle
&=\langle\eta_2,R_{\eta_1}\xi\rangle
=\langle\eta_2,\lambda_\xi\eta_1\rangle\\
&=\langle\lambda_\xi^*\eta_2,\eta_1\rangle
=\langle R_{\eta_2}\zeta,\eta_1\rangle
=\langle\zeta,R_{\eta_2}^*\eta_1\rangle.
\end{aligned}
\tag{FL.16}
\]

View the right Hilbert algebra \(\mathcal A_r\) as the left Hilbert algebra with opposite product
\(\eta\circ\theta=\theta\eta=R_\eta\theta\). Its closed involution is \(F\), whose adjoint is \(S\). In that opposite algebra,

\[
\eta_1^\flat\circ\eta_2=R_{\eta_1}^*\eta_2,\qquad
\eta_2^\flat\circ\eta_1=R_{\eta_2}^*\eta_1.
\]

Its product span is a graph core for \(F\) by RD04. Equivalently, the general adjoint test of RD06 applies to this opposite algebra: its left multiplication is the original right multiplication, its involution is the original right involution, and its four axioms are exactly the right-algebra axioms of RD04 with the product reversed. Therefore that test applied to (FL.16) gives
\(\xi\in D(S)\) and \(S\xi=\zeta\). This proves (FL.14), and then every operator in
\(\mathfrak n_l\cap\mathfrak n_l^*\) has the form required in (FL.13).

Apply the right-algebra construction to the opposite left Hilbert algebra just used. Its right-bounded space is precisely \(\mathcal B_l\), and its adjoint-domain algebra is (FL.12). Taking the opposite of the resulting right algebra gives the displayed product on \(\mathcal A^{\prime\prime}\). RD04 applied to this opposite algebra supplies all four Hilbert-algebra axioms and the graph-core assertion for \(S\). RD05 applied in the same dualized setting gives
\(\lambda(\mathcal A^{\prime\prime})''=(M')'=M\). The inclusion
\(\mathcal A\subseteq\mathcal A^{\prime\prime}\) follows from FL-01 and \(\mathcal A\subseteq D(S)\). \(\square\)

## Fullness and equivalence

The algebra \(\mathcal A^{\prime\prime}\) in (FL.12) is the **full left completion** of \(\mathcal A\). A left Hilbert algebra is **full** when

\[
\mathcal A=\mathcal A^{\prime\prime}.
\tag{FL.17}
\]

Two left Hilbert algebras \(\mathcal A_1\subseteq H_1\) and
\(\mathcal A_2\subseteq H_2\) are **equivalent** when their full completions
\(\mathcal A_1^{\prime\prime}\) and \(\mathcal A_2^{\prime\prime}\) are isometrically star-isomorphic. Here isometric refers to the Hilbert norms; the isomorphism consequently extends uniquely to a unitary between the Hilbert completions.

The completion is idempotent:

\[
(\mathcal A^{\prime\prime})^{\prime\prime}=\mathcal A^{\prime\prime}.
\tag{FL.18}
\]

It does not change the two generated von Neumann algebras:

\[
\lambda(\mathcal A^{\prime\prime})''=M,\qquad
R(\mathcal A_r)''=M'.
\tag{FL.19}
\]

**Proof of (FL.18).** The right algebra obtained from
\(\mathcal A^{\prime\prime}\) is exactly \(\mathcal A_r\). Indeed, if
\(\eta\in\mathcal A_r\) and \(\xi\in\mathcal A^{\prime\prime}\), then

\[
\|\lambda_\xi\eta\|=\|R_\eta\xi\|\leq\|R_\eta\|\,\|\xi\|.
\]

Thus \(\eta\) is right bounded for \(\mathcal A^{\prime\prime}\), it already belongs to \(D(F)\), and its right operator is \(R_\eta\). Conversely, a vector in the right algebra of
\(\mathcal A^{\prime\prime}\) is right bounded after restriction to
\(\mathcal A\subseteq\mathcal A^{\prime\prime}\) and lies in \(D(F)\); hence it belongs to \(\mathcal A_r\). Dualizing this same right algebra again gives exactly
\(\mathcal B_l\cap D(S)=\mathcal A^{\prime\prime}\). Equation (FL.19) is (FL.2) together with (FL.15). \(\square\)

**Why the isomorphism extends to a unitary.** Let \(U_0\) be a complex-linear, isometric star-isomorphism from the first full completion onto the second. Given \(\xi\in H_1\), choose \(\xi_n\) in the first algebra with \(\xi_n\to\xi\). The sequence \(U_0\xi_n\) is Cauchy because distances are preserved. Define \(U\xi\) to be its limit in \(H_2\). If another approximating sequence is chosen, the distance between the two image sequences tends to zero, so the value is independent of the choice. Taking limits proves linearity and norm preservation. Polarization, as in BK01, gives preservation of the inner product. The range is closed: a Cauchy sequence of image vectors has Cauchy preimages, whose limit maps to its limit. The range also contains the dense second algebra, so it is all of \(H_2\). This proves that \(U\) is unitary; density proves uniqueness.

The extension also respects the bounded left actions. For algebra vectors \(\xi,\eta\), multiplicativity gives

\[
 U\lambda_\xi\eta
 =U_0(\xi\eta)
 =\lambda_{U_0\xi}U\eta.
\]

Both operators are bounded, so density extends this identity to every \(\eta\in H_1\). Likewise, preserving the algebra involution identifies the two initial involution graphs. Each algebra is a graph core by FL03. Taking closures, and then applying the same argument to \(U^{-1}\), gives the exact domain and operator identities

\[
 \begin{aligned}
 U D(S_1)&=D(S_2),\\
 S_2 U\xi&=U S_1\xi
 \qquad(\xi\in D(S_1)).
 \end{aligned}
\]

The identity, inverse and composition of such algebra isomorphisms have the same properties. Thus the stated relation is an equivalence relation, and (FL.18) makes an algebra equivalent to its full completion.

## Exported conclusions

FL01 proves the covariant left ideal; FL02 constructs the closed affiliated left multipliers; FL03 proves the adjoint intersection and the left Hilbert algebra obtained by dualizing twice; FL04 proves idempotence and the unitary meaning of equivalence. The preceding linked proofs apply in arbitrary dimension. The construction does not assert a modular commutant theorem or a correspondence with general weights; those require their own proofs.
