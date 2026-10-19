# Recovering a supported weight from a partial cocycle

*Written with OpenAI Codex (GPT-6 Sol and GPT-6 Astra). Original prose: CC0.*

A faithful weight gives a unitary Connes cocycle. When the weight to be recovered has support smaller than \(1\), the comparison instead has a moving initial projection and a fixed final projection. The trick is to fill the complementary corner, reconstruct a faithful weight from the resulting unitary cocycle, and then restrict back to the desired support. The antecedent is Takesaki, *Theory of Operator Algebras II*, Chapter VIII, §3, Theorem 3.21. Here “n.s.f.” means normal, semifinite and faithful.

## The supported inverse problem

Let \(\varphi\) be n.s.f. on a von Neumann algebra \(M\). Suppose \(u:\mathbb R\to M\) is a sigma-strong* continuous family and \(e\in M\) is a projection such that

\[
u_{s+t}=u_s\sigma_s^\varphi(u_t),\qquad
u_tu_t^*=e,\qquad u_t^*u_t=\sigma_t^\varphi(e).
\tag{PL.1}
\]

Thus each \(u_t\) is a partial isometry from \(\sigma_t^\varphi(e)H\) onto \(eH\) in a faithful representation. The case \(e=0\) is allowed.

**Theorem.** There is exactly one normal semifinite weight \(\theta\) with support \(e\) whose supported spatial cocycle satisfies

\[
[D\theta:D\varphi]_t=u_t.
\tag{PL.2}
\]

For an n.s.f. commutant reference \(\kappa\), this cocycle means \(A_\theta^{it}A_\varphi^{-it}\), where \(A_\theta^{it}\) is unitary on the support of \(A_\theta\) and zero on its orthogonal complement. We will prove that the expression is independent of \(\kappa\). It does not define a modular automorphism group for \(\theta\) on all of \(M\).

## Filling the complementary corner

Choose an n.s.f. weight \(\eta\) on \((1-e)M(1-e)\) by the weight existence theorem. Its lift \(\eta^\uparrow(x)=\eta((1-e)x(1-e))\) has support \(1-e\), by corner lifting. Compare it spatially with \(\varphi\) and put \(v_t=[D\eta^\uparrow:D\varphi]_t\). The support formula gives sigma-strong* continuity and

\[
v_tv_t^*=1-e,\qquad
v_t^*v_t=\sigma_t^\varphi(1-e),\qquad
v_{s+t}=v_s\sigma_s^\varphi(v_t).
\tag{PL.3}
\]

For clarity, the last law follows directly from spatial powers. If \(B=d\eta^\uparrow/d\kappa\) and \(C=d\varphi/d\kappa\), take \(B^{it}\) to be zero off its support. Then \(v_t=B^{it}C^{-it}\) lies in \(M\) by the commutant covariance of both spatial operators. Since \(C^{is}\) implements \(\sigma_s^\varphi\),

\[
\begin{aligned}
v_s\sigma_s^\varphi(v_t)
&=B^{is}C^{-is}C^{is}v_tC^{-is}\\
&=B^{is}B^{it}C^{-it}C^{-is}\\
&=v_{s+t}.
\end{aligned}
\tag{PL.3a}
\]

The powers of \(B\) obey the group law on its support, so their zero extensions introduce no extra term.

The final projections of \(u_t,v_t\) are \(e,1-e\), and their initial projections are \(\sigma_t^\varphi(e),\sigma_t^\varphi(1-e)\). Hence \(w_t=u_t+v_t\) is unitary. In \(w_s\sigma_s^\varphi(w_t)\), the two cross terms vanish: the initial projection of \(u_s\) is orthogonal to the final projection of \(\sigma_s^\varphi(v_t)\), and conversely. The two remaining terms obey their respective cocycle laws. Thus \(w_{s+t}=w_s\sigma_s^\varphi(w_t)\). The sum is strongly* continuous.

## Cutting the faithful reconstruction back to its support

The faithful inverse-cocycle theorem gives a unique n.s.f. weight \(\rho\) with \([D\rho:D\varphi]_t=w_t\). Its modular covariance implies

\[
\sigma_t^\rho(e)
=w_t\sigma_t^\varphi(e)w_t^*
=u_tu_t^*=e.
\tag{PL.4}
\]

Thus \(e\) is in the centralizer of \(\rho\). The centralizer-corner theorem makes \(\rho|_{eMe}\) n.s.f.; lift it to \(M\) by

\[
\theta(x)=\rho(exe),\qquad x\in M_+.
\tag{PL.5}
\]

This is normal semifinite and has support exactly \(e\).

We still have to recover \(u\), rather than merely construct a weight on the correct corner. Fix a faithful concrete representation and an n.s.f. weight \(\kappa\) on its commutant. Let \(A_\rho=d\rho/d\kappa\) and \(A_\varphi=d\varphi/d\kappa\). Because \(A_\rho^{it}\) implements \(\sigma^\rho_t\), equation (PL.4) implies that \(e\) commutes with every \(A_\rho^{it}\), hence reduces \(A_\rho\) and its spectral projections.

For a bounded \(\kappa\)-vector \(\xi\), the coefficient map obeys \(R_\kappa(e\xi)=eR_\kappa(\xi)\). Therefore the spatial energies satisfy

\[
Q_\theta[\xi]
=\rho\!\left(eR_\kappa(\xi)R_\kappa(\xi)^*e\right)
=Q_\rho[e\xi].
\tag{PL.6}
\]

We verify the core needed to identify the full operator. Set

\[
B=A_\rho|_{eH}\oplus0_{(1-e)H},\qquad
D(B^{1/2})=\bigl(D(A_\rho^{1/2})\cap eH\bigr)\oplus(1-e)H.
\tag{PL.6a}
\]

Let \(D_\kappa\) be the bounded-vector space for the commutant reference, and let
\(E_\rho=\{\xi\in D_\kappa:Q_\rho[\xi]<\infty\}\).
The spatial form-core theorem makes \(E_\rho\) a core for \(A_\rho^{1/2}\). The coefficient identity above shows that \(eD_\kappa\subseteq D_\kappa\). Since \(e\) reduces \(A_\rho\), it also preserves \(E_\rho\) and commutes with \(A_\rho^{1/2}\) on its domain. For any \(\xi\in D(A_\rho^{1/2})\cap eH\), choose \(\xi_n\in E_\rho\) converging to \(\xi\) in that graph norm. Then \(e\xi_n\to\xi\) and \(A_\rho^{1/2}e\xi_n=eA_\rho^{1/2}\xi_n\to A_\rho^{1/2}\xi\). Hence \(eE_\rho\) is a core for the restricted square-root operator.

The space \((1-e)D_\kappa\) is dense in \((1-e)H\): the space \(D_\kappa\) contains \(E_\rho\), which is Hilbert-norm dense because it is a form core for the densely defined operator \(A_\rho^{1/2}\). The operator \(B^{1/2}\) vanishes there, so

\[
\mathcal C=eE_\rho+(1-e)D_\kappa
\quad\text{is a core for }B^{1/2}.
\tag{PL.6b}
\]

For every \(\xi\in D_\kappa\), (PL.6) and the full bounded-vector energy identity give \(Q_\theta[\xi]=\|B^{1/2}\xi\|^2\), with both sides interpreted as infinity off \(D(B^{1/2})\). Thus the finite bounded-vector domain of \(\theta\) is exactly \(D_\kappa\cap D(B^{1/2})\), and it contains \(\mathcal C\). Closing its initial spatial form therefore gives precisely the closed square-root form of \(B\). The spatial form-core theorem and uniqueness of the represented closed form now prove \(A_\theta=B\), including its full operator and square-root domains. Consequently the supported imaginary powers give

\[
A_\theta^{it}=eA_\rho^{it},\qquad
[D\theta:D\varphi]_t
=eA_\rho^{it}A_\varphi^{-it}
=ew_t=u_t.
\tag{PL.7}
\]

The equality \(ew_t=u_t\) follows from the complementary final projections.

## Why the answer is intrinsic and unique

Let \(\beta\) be any normal semifinite weight supported by \(e\). Fill \(1-e\) with an n.s.f. corner weight \(\zeta\), and set \(\gamma=\beta+\zeta^\uparrow\). The corner sum is n.s.f. and has \(e\) in its centralizer. The same coefficient-form calculation as (PL.6) yields \(A_\beta^{it}=eA_\gamma^{it}\) for every commutant reference. Hence

\[
[D\beta:D\varphi]_t=e[D\gamma:D\varphi]_t.
\tag{PL.8}
\]

The cocycle on the right is independent of the reference by the balanced-weight construction. So the supported expression in (PL.2) is intrinsic, including when \(\beta=\theta\).

If another supported normal semifinite weight has cocycle \(u\), its supported imaginary powers are \(u_tA_\varphi^{it}\) on \(eH\) and zero elsewhere. This strongly continuous unitary group on \(eH\) determines the positive operator there through its logarithm and the spectral uniqueness theorem. The spatial recovery theorem then determines the weight, including its infinite values. This proves uniqueness. \(\square\)

For \(e=1\), the complementary corner vanishes and the theorem reduces to faithful cocycle reconstruction. For \(e=0\), it yields the zero weight. The analytic half-strip characterization and general operator-valued-weight existence are distinct results and are not proved here.

## References

- Takesaki, *Theory of Operator Algebras II*, Springer, 2003, Chapter VIII, §3, Theorem 3.21. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-10451-4).
