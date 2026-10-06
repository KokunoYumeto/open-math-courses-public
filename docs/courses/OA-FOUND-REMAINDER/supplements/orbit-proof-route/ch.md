<span id="changing-reference-for-a-weight-cocycle"></span>
# Changing reference for a weight cocycle

<span id="the-ordered-chain-rule"></span>
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

<span id="reversal-and-paths-of-reference-changes"></span>
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

