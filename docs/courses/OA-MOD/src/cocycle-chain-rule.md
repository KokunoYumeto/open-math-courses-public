# Changing reference for a weight cocycle

*GPT-6 Sol (OpenAI), Codex writing thread, Ultra effort, September 2026. New original prose: CC0. This lesson is a draft awaiting course-level mathematical review.*

A weight cocycle compares two modular actions. If the reference weight changes twice, the two comparisons must be multiplied in a definite order. We prove that rule for faithful normal semifinite weights, then test the order in a two-by-two matrix algebra. The spatial construction supplies the cocycle and its normalization; the existence of a faithful normal semifinite weight supplies a common weight on the commutant. For the classical antecedents, see Connes, *Une classification des facteurs de type III*, and Takesaki, *Theory of Operator Algebras II*, Chapter VIII, §3.

Throughout, \([D\beta:D\alpha]_t\) means the cocycle defined by the modular action of the balanced weight \(\alpha\oplus\beta\) on the off-diagonal matrix unit. The cocycle identity alone would not specify this family: multiplying one cocycle by \(e^{ict}\), for real \(c\), preserves that identity and its modular intertwining action. The mixed KMS characterization and the converse reconstruction of a weight from an arbitrary cocycle are separate results; neither is proved here.

## The ordered chain rule

**Theorem.** Let \(\alpha,\beta,\gamma\) be faithful normal semifinite weights on a von Neumann algebra \(M\). For every real \(t\),

\[
[D\gamma:D\alpha]_t
=[D\gamma:D\beta]_t[D\beta:D\alpha]_t.
\tag{CH.1}
\]

The factors need not commute.

**Proof.** Represent \(M\) faithfully and nondegenerately on a Hilbert space \(H\), and put \(N=M'\). Choose a faithful normal semifinite weight \(\omega\) on \(N\). All three spatial derivatives can then be taken on the same \(H\):

\[
A=\frac{d\alpha}{d\omega},\qquad
B=\frac{d\beta}{d\omega},\qquad
C=\frac{d\gamma}{d\omega}.
\]

They are positive, injective, self-adjoint operators. Their imaginary powers are bounded unitaries on all of \(H\), even if the derivatives and their inverses are unbounded. The spatial formula for the balanced-weight cocycle gives

\[
\begin{aligned}
[D\gamma:D\beta]_t[D\beta:D\alpha]_t
&=(C^{it}B^{-it})(B^{it}A^{-it})\\
&=C^{it}A^{-it}\\
&=[D\gamma:D\alpha]_t.
\end{aligned}
\]

Only the adjacent factors involving \(B\) cancel. No unbounded operators are moved across one another, and no common domain for their products is needed. Each cocycle in this computation lies in \(M\) and is independent of the commutant weight and of the faithful representation. Faithfulness of the representation proves the identity in \(M\). The zero algebra has the same identity in its zero-dimensional representation. \(\square\)

## Reversal and paths of reference changes

Taking all three weights equal in the theorem gives the identity cocycle. Taking \(\gamma=\alpha\) then gives the reverse comparison:

\[
[D\alpha:D\alpha]_t=1,\qquad
[D\alpha:D\beta]_t=[D\beta:D\alpha]_t^*.
\tag{CH.2}
\]

Indeed, the spatial formula yields \(A^{it}A^{-it}=1\), and each cocycle is unitary.

For faithful normal semifinite weights \(\varphi_0,\ldots,\varphi_n\), apply the chain rule repeatedly:

\[
[D\varphi_n:D\varphi_0]_t
=[D\varphi_n:D\varphi_{n-1}]_t
\cdots[D\varphi_1:D\varphi_0]_t.
\tag{CH.3}
\]

Induction gives this product in precisely the displayed order. If \(n=0\), it is the empty product \(1\). Thus an intermediate reference can be inserted or removed without changing the total comparison.

The same order appears in modular covariance. Set \(u_t=[D\beta:D\alpha]_t\) and \(v_t=[D\gamma:D\beta]_t\). The spatial construction gives \(\sigma_t^\beta=\operatorname{Ad}(u_t)\circ\sigma_t^\alpha\). Using the cocycle laws for \(u\) and \(v\),

\[
\begin{aligned}
v_{s+t}u_{s+t}
&=v_s\sigma_s^\beta(v_t)\,u_s\sigma_s^\alpha(u_t)\\
&=v_su_s\sigma_s^\alpha(v_t)u_s^*u_s\sigma_s^\alpha(u_t)\\
&=(v_su_s)\sigma_s^\alpha(v_tu_t).
\end{aligned}
\]

Hence \(vu\) is a \(\sigma^\alpha\)-cocycle. Both factors are strongly* continuous unitary families, so their product is strongly* continuous as well.

## A two-by-two test of the order

Use the usual trace for \(\alpha\) on \(M_2(\mathbb C)\). Define \(\beta\) and \(\gamma\) by the positive density matrices

\[
b=\begin{pmatrix}1&0\\0&e\end{pmatrix},\qquad
c=QbQ^*,\qquad
Q=2^{-1/2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}.
\]

All three weights are faithful normal semifinite. The matrix spatial formula gives

\[
u_t=[D\beta:D\alpha]_t=b^{it},\qquad
v_t=[D\gamma:D\beta]_t=c^{it}b^{-it}.
\]

Thus \(v_tu_t=c^{it}\). At \(t=\pi\), let
\(U=b^{i\pi}=\operatorname{diag}(1,-1)\) and
\(C=c^{i\pi}=QUQ^*=\begin{pmatrix}0&1\\1&0\end{pmatrix}\).
Then \(u_\pi=U\), \(v_\pi=CU\), and

\[
v_\pi u_\pi=C,\qquad u_\pi v_\pi=UCU=-C.
\]

The reversed product is already wrong for two-by-two matrices.

## What changes when a weight has smaller support

**Exercise.** Suppose the intermediate weight \(\beta\) is normal semifinite but not faithful. Why does the preceding proof no longer give a whole-algebra unitary chain rule? What can still be said when all three weights are faithful on one common corner \(pMp\)?

**Solution.** The support calculation shows that \(B=d\beta/d\omega\) has a nonzero kernel when the support of \(\beta\) is proper. Its imaginary powers on the support, extended by zero, are partial unitaries. Their adjacent product is
\(B^{-it}B^{it}=s(B)\), rather than \(1\). Moreover, the balanced-weight cocycles used above were defined as whole-algebra unitaries for faithful weights. A nonfaithful intermediate weight cannot simply be inserted into that definition.

If \(\alpha,\beta,\gamma\) are faithful normal semifinite weights on the *same* corner \(pMp\), the theorem applies there, with identity \(p\). Different supports require a separate cocycle definition and compatible support and domain identities; the argument above does not supply them.

## Balanced sums and componentwise transport

Let \(\alpha\) be a normal automorphism of \(M\), let \(\varphi\) and \(\psi\) be faithful normal semifinite weights, and put

\[
\begin{aligned}
N&=M_2(M), &
\beta&=\alpha\otimes\operatorname{id}_{M_2},\\
\chi([x_{ij}])&=\varphi(x_{11})+\psi(x_{22}).
\end{aligned}
\]

For \(t\in\mathbb R\), abbreviate

\[
\begin{aligned}
w_t&=[D(\chi\circ\beta):D\chi]_t,\\
u_t&=[D(\varphi\circ\alpha):D\varphi]_t,\\
v_t&=[D(\psi\circ\alpha):D\psi]_t.
\end{aligned}
\]

Then

\[
w_t=u_t\otimes e_{11}+v_t\otimes e_{22}
=\begin{pmatrix}u_t&0\\0&v_t\end{pmatrix}.
\tag{CH.4}
\]

**Proof.** Choose a faithful nondegenerate representation \(M\subseteq B(H)\) and a faithful normal semifinite reference weight \(\eta\) on \(M'\). Write

\[
\begin{aligned}
A_\varphi&=\frac{d\varphi}{d\eta}, &
A_\psi&=\frac{d\psi}{d\eta},\\
B_\varphi&=\frac{d(\varphi\circ\alpha)}{d\eta}, &
B_\psi&=\frac{d(\psi\circ\alpha)}{d\eta}.
\end{aligned}
\]

Represent \(N\) on \(H\oplus H\). Its commutant is the diagonal copy \(\{y\oplus y:y\in M'\}\), on which we use \(\eta\). The balanced direct-sum calculation, first for \(\chi\) and then for

\[
\chi\circ\beta=(\varphi\circ\alpha)\oplus(\psi\circ\alpha),
\]

gives

\[
\frac{d\chi}{d\eta}=A_\varphi\oplus A_\psi,
\qquad
\frac{d(\chi\circ\beta)}{d\eta}=B_\varphi\oplus B_\psi.
\]

Functional calculus commutes with orthogonal direct sums. Hence the spatial cocycle formula gives

\[
\begin{aligned}
w_t
&=(B_\varphi\oplus B_\psi)^{it}
  (A_\varphi\oplus A_\psi)^{-it}\\
&=(B_\varphi^{it}A_\varphi^{-it})
  \oplus(B_\psi^{it}A_\psi^{-it})\\
&=u_t\oplus v_t.
\end{aligned}
\]

All imaginary powers here are bounded unitaries, so no common domain for products of unbounded operators is being assumed. This is exactly (CH.4). \(\square\)

If \((\alpha_s)_{s\in G}\) is an action and \(\beta_s=\alpha_s\otimes\operatorname{id}_{M_2}\), applying (CH.4) to each \(s\) gives the componentwise transport formula for the action. This statement concerns modular transport of the balanced weight; action cohomology and crossed-product consequences belong to OA-FLOW.

## References

- Connes, “Une classification des facteurs de type III,” *Annales scientifiques de l’École Normale Supérieure* 6 (1973), 133–252. [Open article](https://numdam.org/articles/10.24033/asens.1247/).
- Takesaki, *Theory of Operator Algebras II*, Springer, 2003, Chapter VIII, §3. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-10451-4).
