# Lower semicontinuous weights on a C*-algebra

*Codex writing thread, September 2026. New original prose: CC0. Written prerequisite bindings, hereditary-corner details, the matrix example and exact-edition source checks: GPT-6 Astra (OpenAI), Ultra, October 2026.*

A weight may be infinite on most positive elements. Norm lower semicontinuity nevertheless has two strong consequences: its GNS representation acts nondegenerately on the Hilbert space actually constructed from finite elements, and the entire weight can be recovered from bounded positive functionals. Neither assertion requires the finite domain to be norm dense in the algebra. We use the finite-domain GNS construction and the positive contractive approximate identity. Inner products are linear in the first variable.

The order and square-root arguments use the written abstract C*-calculus, AC1–4 and forced unitization, UZ07. Point separation is NP2; norm-preserving extension is NP1. For the operator arguments, BK01–07 supplies Hilbert-space completion, topology, bounded monotone limits, inverse order and polar decomposition; BG03 supplies a cyclic vector for every bounded positive functional. AB04–05 proves the compactness facts, and CP07 proves normality of vector functionals. The universal-bidual construction, UB02–09 supplies canonical normal extensions and bidual inclusions. These are proof providers, not external proof citations.

## Nondegeneracy on the finite-weight GNS space

Let \(A\) be any complex C*-algebra, possibly nonunital or zero, and let \(\varphi:A_+\to[0,\infty]\) be an additive, positively homogeneous, norm-lower-semicontinuous weight. Its semicyclic representation \((H_\varphi,\pi_\varphi,\Lambda_\varphi)\) has the GNS formulas (CS.6). We claim that

\[
\overline{\pi_\varphi(A)H_\varphi}=H_\varphi.
\tag{LW.1}
\]

Choose a positive contractive approximate identity \((e_i)\) for \(A\). For \(x\in\mathfrak n_\varphi\), both \(x^*e_i x\) and \(x^*e_i^2x\) lie between zero and \(x^*x\). Their weights are therefore finite and at most \(\varphi(x^*x)\). They converge in norm to \(x^*x\): the first assertion follows from \(e_ix\to x\), and the second from \((e_ix)^*(e_ix)\to x^*x\). Lower semicontinuity now forces

\[
\begin{aligned}
\varphi(x^*e_i x)&\longrightarrow\varphi(x^*x),\\
\varphi(x^*e_i^2x)&\longrightarrow\varphi(x^*x).
\end{aligned}
\tag{LW.2}
\]

Indeed, each liminf is at least the weight of the norm limit, while monotonicity supplies the opposite bound.

Put \(r_i=x-e_ix\), \(w=\varphi(x^*x)\), \(p_i=\varphi(x^*e_ix)\), and \(q_i=\varphi(x^*e_i^2x)\). The GNS norm gives \(\|\Lambda_\varphi(r_i)\|^2=\varphi(r_i^*r_i)\). The linear extension of \(\varphi\) to its finite *-algebra expands the square without subtracting infinite quantities:

\[
\varphi(r_i^*r_i)=w-2p_i+q_i\to0.
\tag{LW.3}
\]

Here \(\Lambda_\varphi(r_i)=\Lambda_\varphi(x)-\pi_\varphi(e_i)\Lambda_\varphi(x)\).
Every \(\pi_\varphi(e_i)\) is a contraction. Since \(\Lambda_\varphi(\mathfrak n_\varphi)\) is dense, (LW.3) extends to strong convergence \(\pi_\varphi(e_i)\to I_{H_\varphi}\), proving (LW.1). This also covers \(H_\varphi=0\), where nondegeneracy has its usual vacuous meaning. It does **not** say that \(\mathfrak n_\varphi\) is norm dense in \(A\); the faithful weight on \(\mathbb C^2\) in the preceding lesson illustrates the distinction.

## A closed hereditary set absorbs approximate order bounds

We need a separation statement that respects positivity in a noncommutative algebra. Let \(C\subseteq A_+\) be norm closed, convex, hereditary, and contain zero. In the real Banach space \(A_{\rm sa}\), set \(D=\overline{C-A_+}^{\|\cdot\|}\). Then

\[
D\cap A_+=C.
\tag{LW.4}
\]

The inclusion \(C\subseteq D\cap A_+\) is immediate. For the reverse, take \(a\in D\cap A_+\). There are \(b_n\in C\), \(c_n\in A_+\), and \(\varepsilon_n>0\) with \(\varepsilon_n\to0\) and \(\|a-b_n+c_n\|\leq\varepsilon_n\). Consequently \(a\leq b_n+\varepsilon_n1\) in the forced unitization.

For one such pair \((b,\varepsilon)\), put

\[
k=b^{1/2}(b+\varepsilon1)^{-1/2}.
\tag{LW.5}
\]

Set \(d=kak\).
Continuous functional calculus gives \(k\in A\), even when \(A\) has no unit, because the defining scalar function vanishes at zero. It also gives \(0\leq k\leq1\) and \(0\leq d\leq k(b+\varepsilon1)k=b\), so heredity places \(d\) in \(C\). Let \(h=(b+\varepsilon1)^{1/2}-b^{1/2}\). Since \((1-k)(b+\varepsilon1)(1-k)=h^2\), the approximate bound on \(a\) and scalar functional calculus give

\[
(1-k)a(1-k)\leq h^2\leq\varepsilon1.
\tag{LW.6}
\]

We have \(\|(1-k)a^{1/2}\|\leq\sqrt\varepsilon\). Decomposing \(a-kak=(1-k)a+ka(1-k)\) yields

\[
\|a-d\|\leq2\sqrt{\|a\|\varepsilon}.
\tag{LW.7}
\]

Apply this estimate to \((b_n,\varepsilon_n)\). Then \(d_n\in C\) and \(d_n\to a\) in norm, so closedness gives \(a\in C\). The construction proves (LW.4) without moving to the bidual. Its contraction \(k\) changes the approximate inequality \(a\leq b+\varepsilon1\) into an exact inequality \(kak\leq b\) while controlling the norm error.

## Recovery from bounded positive functionals

For the weight in LW-01, define

\[
\mathcal F_\varphi=\{\omega\in A^*_+:\omega\leq\varphi\}.
\tag{LW.8}
\]

The order in (LW.8) compares values on every \(b\in A_+\). The zero functional belongs to this set. For each \(a\in A_+\), we will prove

\[
\boxed{\displaystyle
\varphi(a)=\sup_{\omega\in\mathcal F_\varphi}\omega(a).}
\tag{LW.9}
\]

This assertion concerns all positive elements, including those of infinite weight, without a density, faithfulness, separability, or semifiniteness hypothesis.

The sublevel set \(C=\{b\in A_+: \varphi(b)\leq1\}\) is hereditary by monotonicity, convex by additivity and homogeneity, and norm closed by lower semicontinuity. Let \(D=\overline{C-A_+}\); LW-02 gives \(D\cap A_+=C\). Fix \(a\in A_+\) and a finite \(t\) with \(0<t<\varphi(a)\). Then \(y=a/t\) lies in \(A_+\setminus D\). Strict Hahn–Banach separation in \(A_{\rm sa}\) supplies a bounded real-linear \(g\) with

\[
\begin{aligned}
g(y)&>\alpha,\\
\alpha&:=\sup_{z\in D}g(z)\in[0,\infty).
\end{aligned}
\tag{LW.10}
\]

The lower bound uses \(0\in D\). For every \(b\in A_+\) and \(s\geq0\), we have \(-sb\in D\); hence finiteness of \(\alpha\) implies \(g(b)\geq0\). Complexification therefore turns \(g\) into a bounded positive functional. Explicitly, for self-adjoint \(u,v\), extend by \(g(u+iv)=g(u)+ig(v)\). The decomposition into real and imaginary parts is unique, their norms are at most the norm of \(u+iv\), and therefore this extension has norm at most twice the real-functional norm. Positivity was just proved on the unchanged positive cone. As subtracting a positive element cannot increase \(g\), we also have \(\alpha=\sup_{b\in C}g(b)\).

When \(\alpha>0\), set \(\omega=g/\alpha\). If \(0<\varphi(b)<\infty\), scale \(b\) into \(C\) to obtain \(\omega(b)\leq\varphi(b)\). If \(\varphi(b)=0\), every positive multiple of \(b\) belongs to \(C\), so \(g(b)=0\). An infinite weight imposes no further bound. Thus \(\omega\in\mathcal F_\varphi\), and (LW.10) gives \(\omega(a)>t\).

When \(\alpha=0\), the same scaling argument shows that \(g\) vanishes on every finite-weight positive element. Every positive multiple \(Mg\) therefore belongs to \(\mathcal F_\varphi\). Since \(g(y)>0\), choose \(M\) with \(Mg(a)>t\). We have found a dominated bounded positive functional above every finite \(t<\varphi(a)\). The reverse inequality in (LW.9) is built into (LW.8). If \(\varphi(a)=0\), both sides vanish; if \(\varphi(a)=\infty\), the arbitrary choice of finite \(t\) gives an infinite supremum.

The positive functionals alone establish recovery. If one uses the wider convention in which a self-adjoint bounded functional \(\rho\) may satisfy \(\rho\leq\varphi\) on \(A_+\), adjoining such functionals does not change the supremum: each is bounded above by \(\varphi\), while the positive subfamily already attains the supremum. For example, if \(\varphi(b)=\infty\) for every nonzero \(b\in A_+\), then \(\mathfrak n_\varphi=0\), yet all bounded positive functionals are dominated and their values have supremum \(+\infty\) at each nonzero positive \(b\). Nondegeneracy on the zero GNS space and recovery of the weight are distinct conclusions.

## The finite part is a hereditary algebra

Write, with complex linear span and norm closure,

\[
\begin{aligned}
P&=\{a\geq0:\varphi(a)<\infty\},\\
\mathfrak m&=\operatorname{span}P,\\
B&=\overline{\mathfrak m}^{\,\|\cdot\|}.
\end{aligned}
\tag{LW.11}
\]

The finite-domain calculation gives
\(\mathfrak m=\operatorname{span}\{x^*y:x,y\in\mathfrak n_\varphi\}\);
it is a *-algebra contained in \(\mathfrak n_\varphi\). If
\(a\in\mathfrak m\cap A_+\), take the real part of a finite expression for
\(a\) in elements of \(P\), then separate positive and negative real
coefficients. This writes \(a=p-q\) with \(p,q\in P\). Since
\(0\leq a\leq p\), monotonicity gives \(a\in P\). Thus

\[
\begin{aligned}
\mathfrak m\cap A_+&=P,\\
\overline P^{\,\|\cdot\|}&=B_+.
\end{aligned}
\tag{LW.12}
\]

For the second equality, approximate \(b^{1/2}\), \(b\in B_+\), by
\(z_n\in\mathfrak m\), and use \(z_n^*z_n\in P\). The positive cone of the closed *-subalgebra agrees with the inherited cone: for a positive element of \(A\) lying in \(B\), AC3–4 approximates its square root by polynomials with zero constant term, all in \(B\). Thus it is a square in \(B\) as well.

The algebra \(B\) is hereditary in \(A\). Indeed, if \(0\leq a\leq b\in B_+\),
choose \(b_n\in P\) with \(b_n\to b\), and
\(\varepsilon_n>\|b-b_n\|\) tending to zero. The contraction from (LW.5),
formed with \(b_n,\varepsilon_n\), gives \(d_n\in P\) with
\(0\leq d_n\leq b_n\) and
\(\|a-d_n\|\leq2\sqrt{\|a\|\varepsilon_n}\). Hence \(a\in B\).
The restricted weight \(\psi=\varphi|_{B_+}\) is norm lower semicontinuous
and densely defined: its finite linear domain is \(\mathfrak m\), dense
in \(B\).

We need the exact bidual corner, including when \(B=0\). Direct \(P\)
by positive order and set \(u_h=h(1+h)^{-1}\) for \(h\in P\), using the
forced unitization. Inverse-order reversal makes \(u_h\) increasing;
\(0\leq u_h\leq h\) puts it in \(P\). For \(b\in P\), \(t>0\), and \(h\geq tb\),

\[
\begin{gathered}
\|(1-u_h)b^{1/2}\|^2\\
\leq\|b^{1/2}(1+h)^{-1}b^{1/2}\|\\
\leq\|b(1+tb)^{-1}\|
\leq t^{-1}.
\end{gathered}
\tag{LW.13}
\]

For each \(b\in P\), multiplying (LW.13) by \(b^{1/2}\) gives

\[
 \|(1-u_h)b\|\leq\sqrt{\|b\|/t}
 \quad(h\geq tb).
\]

Taking adjoints gives the same bound for \(b(1-u_h)\). Finite linear combinations give both limits on \(\mathfrak m\). For \(a\in B\), choose \(m\in\mathfrak m\) close to \(a\); the error off this dense subalgebra is at most \(2\|a-m\|\), uniformly in \(h\). Thus \(u_h\) is a positive contractive approximate identity of \(B\);
the constant zero net covers \(B=0\).

Let \(j:B\hookrightarrow A\). Hahn–Banach makes restriction
\(j^*:A^*\to B^*\) onto, so the normal *-homomorphism \(j^{**}\) is
isometric and has ultraweakly closed range
\(N=(B^\perp)^\perp=\overline B^{\,\sigma(A^{**},A^*)}\). Put
\(e=j^{**}(1_{B^{**}})\). An ultraweak cluster point of \(u_h\) acts as
the identity on \(B\) and hence on \(B^{**}\); uniqueness and weak*
compactness give \(u_h\to e\) ultraweakly. Bounded monotone convergence
also gives strong convergence in the universal representation, so
\(e\) is an open projection, meaning a strong limit of an increasing net of positive elements of \(A\). Heredity gives \(BAB\subseteq B\):
\(0\leq xax^*\leq\|a\|xx^*\) for \(x\in B,a\in A_+\), followed by
polarization. To spell out that step, for \(x,y\in B\) and \(a\in A_+\), expansion gives

\[
 \begin{aligned}
 4xay^*&=\sum_{k=0}^{3}i^k z_kaz_k^*,\\
 z_k&=x+i^ky.
 \end{aligned}
\]

Every summand lies in \(B\). Every element of \(A\) is a linear combination of four positives by AC4, so this proves the assertion for arbitrary middle factors and both outside factors in \(B\). Passing separately to the two ultraweak limits in
\(u_hau_k\in B\) gives \(eae\in N\) for \(a\in A\); ultraweak density of
\(A\) then gives \(eA^{**}e\subseteq N\). Since \(e\) is the identity of
\(N\), the opposite inclusion holds. Finally a functional annihilating
\(B\) separates any \(a\in A\setminus B\) from \(N\). We have proved

\[
\begin{aligned}
B^{**}&\cong eA^{**}e,\\
B&=A\cap eA^{**}e.
\end{aligned}
\tag{LW.14}
\]

The projection \(e\) need not be central or the support of \(\varphi\).
This use of the bidual follows the universal-bidual construction.

## Directed functionals in the dense case

First work with a norm-lower-semicontinuous weight \(\psi\) on a
C*-algebra \(C\) for which \(\mathfrak n_\psi\) is norm dense. Set

\[
\begin{gathered}
\mathcal G_\psi=
 \{\gamma\in C^*_+:\gamma\leq r\psi\\
 \text{for some }0\leq r<1\}.
\end{gathered}
\tag{LW.15}
\]

We prove that two members have a common upper bound in this same
strict family. This assertion is stronger than pointwise recovery
(LW.9).

Here is the bounded-functional representation needed for the proof.
If \(\rho\in C^*_+\) and \(\rho\leq c\psi\), \(c>0\), let
\((H_\rho,\pi_\rho,\xi_\rho)\) be its cyclic bounded-functional GNS
representation. On the weight GNS core define

\[
\begin{gathered}
T_\rho\Lambda_\psi(a)=\pi_\rho(a)\xi_\rho,\\
a\in\mathfrak n_\psi.
\end{gathered}
\tag{LW.16}
\]

Domination makes this well-defined and bounded by \(\sqrt c\).
Norm density of \(\mathfrak n_\psi\), boundedness of \(\rho\), and
cyclicity give dense range. The intertwining identity for \(T_\rho\)
and its adjoint puts

\[
\begin{gathered}
D_\rho=T_\rho^*T_\rho,\\
D_\rho\in\pi_\psi(C)',\\
0\leq D_\rho\leq cI,\\
\langle D_\rho\Lambda_\psi(a),
 \Lambda_\psi(a)\rangle\\
=\rho(a^*a).
\end{gathered}
\tag{LW.17}
\]

Quadratic polarization on the dense core makes \(D_\rho\) unique and
additive in \(\rho\). In the polar decomposition
\(T_\rho=V_\rho D_\rho^{1/2}\), dense range gives
\(V_\rho V_\rho^*=I_{H_\rho}\). The partial isometry intertwines:
this follows by taking the strong limit of
\(T_\rho(D_\rho+\delta I)^{-1/2}\) as \(\delta\downarrow0\).
For \(\eta_\rho=V_\rho^*\xi_\rho\),

\[
\begin{gathered}
D_\rho^{1/2}\Lambda_\psi(a)
 =\pi_\psi(a)\eta_\rho,\\
\rho(b)=
 \langle\pi_\psi(b)\eta_\rho,\eta_\rho\rangle.
\end{gathered}
\tag{LW.18}
\]

In particular, dominated bounded functionals factor normally
through \(\pi_\psi(C)''\) in this dense case. The second identity in (LW.18) follows from the intertwining relation and \(V_\rho V_\rho^*=I\); CP07 makes its vector functional normal on the bicommutant. The dense-range step used norm density of the finite left ideal in \(C\), not just density of its image in the weight GNS space.

Take \(\gamma_i\in\mathcal G_\psi\), \(i=1,2\). Choose
\(0<\lambda_i<1\) and \(\rho_i\leq\psi\) with
\(\gamma_i=\lambda_i\rho_i\); zero functionals pose no exception.
Put \(D=D_{\rho_1+\rho_2}=D_{\rho_1}+D_{\rho_2}\leq2I\), and let
\(\eta=\eta_{\rho_1+\rho_2}\). Choose \(s>0\) with
\(s/(1+s)\geq\max_i\lambda_i\), and set

\[
\begin{gathered}
h=\bigl(s(I+sD)^{-1}\bigr)^{1/2},\\
h\in\pi_\psi(C)',\\
\gamma(b)=
 \langle\pi_\psi(b)h\eta,h\eta\rangle.
\end{gathered}
\tag{LW.19}
\]

For \(a\in\mathfrak n_\psi\), write \(\zeta=\Lambda_\psi(a)\). Then (LW.18) gives

\[
\begin{gathered}
\gamma(a^*a)=
 \langle f_s(D)\zeta,\zeta\rangle,\\
f_s(D)=sD(I+sD)^{-1}.
\end{gathered}
\tag{LW.20}
\]

Inversion reverses positive-operator order: from \(0<P\leq Q\),
write \(Q=P^{1/2}(I+R)P^{1/2}\) with \(R\geq0\), and compare the
inverses. Hence \(f_s\) is operator monotone. Since \(D_{\rho_i}\leq I\),

\[
\begin{aligned}
\lambda_iD_{\rho_i}
 &\leq \frac{s}{1+s}D_{\rho_i}\\
 &\leq f_s(D_{\rho_i})\\
 &\leq f_s(D)\\
 &\leq \frac{2s}{1+2s}I.
\end{aligned}
\tag{LW.21}
\]

The last bound proves
\(\gamma\leq \frac{2s}{1+2s}\psi\) on finite-weight positives,
and trivially on infinite-weight positives. The first bound proves
\(\gamma\geq\gamma_i\) on squares from \(\mathfrak n_\psi\).
Approximate every \(b^{1/2}\), \(b\in C_+\), in norm from that dense
left ideal; boundedness of both functionals extends the inequality
to all \(b\). This is upward directedness with a strict constant.

The canonical normal extensions of this directed family to
\(C^{**}\) form an increasing net. Write \(E(x)=\sup_\gamma\gamma^{**}(x)\). This pointwise supremum is
additive: to combine lower bounds for two positive arguments, pass
to a common upper functional. It is normal because for every
bounded increasing net \(x_j\uparrow x\), the two independent
suprema commute:

\[
\begin{aligned}
E(x)
 &=\sup_{\gamma,j}\gamma^{**}(x_j)\\
 &=\sup_j E(x_j).
\end{aligned}
\tag{LW.22}
\]

Scalar attenuation of each \(\rho\leq\psi\), together with (LW.9),
recovers \(\psi\) on \(C_+\). The finite linear domain is norm dense
in \(C\), so this normal envelope is semifinite in the ultraweak
finite-domain-density sense: that finite linear domain lies in the finite linear domain of \(E\), and its ultraweak closure contains \(C\), hence all of \(C^{**}\) by UB05.

## The normal envelope without a density hypothesis

Return to arbitrary \(A,\varphi\). Apply LW-05 to the densely
defined restriction \(\psi\) on \(B\) from LW-04. Denote its normal
semifinite envelope on \(B^{**}=eA^{**}e\) by \(\Psi\). Define

\[
\begin{gathered}
\Phi(x)=\Psi(x)\quad(x=exe),\\
\Phi(x)=\infty\quad(x\ne exe).
\end{gathered}
\tag{LW.23}
\]

For \(f=1-e\) and \(x\geq0\), \(x=exe\) exactly when \(fxf=0\):
if \(fxf=(x^{1/2}f)^*(x^{1/2}f)=0\), then \(xf=fx=0\).
Consequently a positive sum lies in the corner exactly when both
summands do. This proves additivity of (LW.23), including the
infinite case. Positive homogeneity uses \(0\cdot\infty=0\).
If \(x_j\uparrow x\) is a bounded increasing positive net and
\(x\) is in the corner, normality follows from \(\Psi\). If \(x\)
is outside, some \(x_j\) must be outside the ultraweakly closed
corner; its value is already infinite. Thus \(\Phi\) is a normal
weight. On \(A_+\cap eA^{**}e=B_+\), it agrees with \(\psi\).
Every finite-weight positive element of \(A\) belongs to \(B\);
therefore \(\Phi|_{A_+}=\varphi\) also outside the corner.

This \(\Phi\) is precisely the canonical functional envelope.
Write \(\mathcal F_\varphi\) as in (LW.8) and
\(\mathcal G_\varphi\) as in (LW.15), with \(\varphi\) in place of
\(\psi\). If \(\omega\leq\varphi\), its restriction to \(B\) is
dominated by \(\psi\); the normal restriction of \(\omega^{**}\)
to \(eA^{**}e\) is consequently bounded above by \(\Psi\).
Outside the corner, \(\Phi\) is infinite. This proves that the
functional envelope is at most \(\Phi\).

Conversely, if \(\delta\in B^*_+\) is dominated by \(\psi\), the
bounded normal functional
\(\Omega_\delta(x)=\delta^{**}(exe)\) on \(A^{**}\) restricts to a
member of \(\mathcal F_\varphi\). On finite positives this follows
from their membership in \(B\); infinite values impose no bound.
UB05 makes each such normal functional the unique normal extension of its restriction to \(A\). These functionals recover \(\Psi\) on the corner. For
\(x\geq0\) outside, \(fxf\ne0\). Choose a positive normal
functional \(\rho\) with \(\rho(fxf)>0\): in the faithful universal representation choose a vector on which the nonzero positive operator \(fxf\) has positive quadratic form, and use its normal vector functional from CP07. For each \(L>0\),
\(y\mapsto L\rho(fyf)\) is bounded normal positive and its
restriction to \(A\) vanishes on every finite-weight positive
element, hence belongs to \(\mathcal F_\varphi\). Its value at
\(x\) grows without bound. Therefore

\[
\begin{aligned}
\Phi(x)
 &=\sup_{\omega\in\mathcal F_\varphi}
     \omega^{**}(x)\\
 &=\sup_{\gamma\in\mathcal G_\varphi}
     \gamma^{**}(x).
\end{aligned}
\tag{LW.24}
\]

The second equality follows by taking \(r\omega\), \(r\uparrow1\),
for each \(\omega\leq\varphi\). Scalar attenuation proves equality
of the suprema; it does not by itself prove directedness.

## Global directedness and the off-diagonal block

The family \(\mathcal G_\varphi\) is upward directed even when
\(B\ne A\). Let \(\gamma_i\leq\lambda_i\varphi\), \(i=1,2\),
with \(0<\lambda_i<1\). Choose \(\varepsilon>0\) so that
\((1+\varepsilon)\max_i\lambda_i<1\).
By LW-05 on \(B\), a \(\delta\in B^*_+\) and \(0<r<1\) satisfy, for \(i=1,2\),

\[
\begin{aligned}
\delta&\geq(1+\varepsilon)\gamma_i|_B,\\
\delta&\leq r\psi.
\end{aligned}
\tag{LW.25}
\]

Their normal extensions preserve order on \(eA^{**}e\).
The upper bound there is \(\delta^{**}\leq r\Psi\).

A cross term cannot be dropped just because \(e\) is a corner
projection. For every bounded positive normal functional \(\omega\)
on \(A^{**}\), \(x\geq0\), and \(f=1-e\), its cyclic GNS vectors
\(v=\pi_\omega(x)^{1/2}\pi_\omega(e)\xi_\omega\) and
\(w=\pi_\omega(x)^{1/2}\pi_\omega(f)\xi_\omega\) give

\[
\begin{aligned}
\omega(x)
 &\leq(1+\varepsilon)\omega(exe)\\
 &\quad+(1+\varepsilon^{-1})\omega(fxf).
\end{aligned}
\tag{LW.26}
\]

Indeed, this is
\(\|v+w\|^2\leq(1+\varepsilon)\|v\|^2+
(1+\varepsilon^{-1})\|w\|^2\).
The inequality follows by expanding the squared norm, using Cauchy–Schwarz and then \(2ab\leq\varepsilon a^2+\varepsilon^{-1}b^2\), which is the nonnegativity of \((\sqrt\varepsilon a-b/\sqrt\varepsilon)^2\). No centrality of \(e\) is used.

Put \(c=1+\varepsilon^{-1}\) and set

\[
\begin{aligned}
\Gamma(x)
 &=\delta^{**}(exe)\\
 &\quad+c\gamma_1^{**}(fxf)\\
 &\quad+c\gamma_2^{**}(fxf).
\end{aligned}
\tag{LW.27}
\]

This is bounded normal positive. Equations (LW.25)–(LW.26)
give \(\Gamma\geq\gamma_1^{**},\gamma_2^{**}\) on *all*
positive \(x\), including off-diagonal blocks. On the corner,
\(\Gamma\leq r\Psi=r\Phi\); outside it, \(r\Phi=\infty\).
The restriction of \(\Gamma\) to \(A\) therefore belongs to
\(\mathcal G_\varphi\) and dominates both \(\gamma_i\).
Equation (LW.24) is consequently an increasing-normal-functional
limit, providing a second direct proof of additivity and normality.

## Semifiniteness and the GNS boundary

The finite positive domain of \(\Phi\) lies in \(eA^{**}e\);
inside that corner it is the finite positive domain of \(\Psi\).
Since \(\Psi\) is semifinite there,

\[
\overline{\mathfrak m_\Phi}^{\,\mathrm{uw}}=eA^{**}e.
\tag{LW.28}
\]

Thus \(\Phi\) is semifinite on all of \(A^{**}\) exactly when
\(e=1\), equivalently \(B=A\), equivalently
\(\mathfrak n_\varphi\) is norm dense. The last equivalence uses
\(\mathfrak m\subseteq\mathfrak n_\varphi\) in one direction;
in the other, squares of norm approximants to \(a^{1/2}\)
from \(\mathfrak n_\varphi\) approach every \(a\in A_+\)
through \(P\). This is finite-domain density, not an assertion
that finite elements increase below each given positive element.

The universal envelope must not be identified unconditionally with
a pullback from the original semicyclic GNS algebra. In the
faithful example
\(A=\mathbb C^2\), let
\(\varphi(a,b)=a\) when \(b=0\) and
\(\varphi(a,b)=\infty\) when \(b>0\), for \((a,b)\geq0\).
The GNS space is \(\mathbb C\), and
\(\bar\pi_\varphi(a,b)=a\). But

\[
\begin{gathered}
\bar\pi_\varphi(0,1)=0,\\
\Phi(0,1)=\infty.
\end{gathered}
\tag{LW.29}
\]

Every weight on \(\pi_\varphi(A)''=\mathbb C\) sends zero to
zero. Hence no weight \(\Theta\) there can satisfy
\(\Phi=\Theta\circ\bar\pi_\varphi\). The dense case in LW-05
does permit normal factorization of dominated bounded functionals;
this example shows exactly why its density hypothesis cannot be
discarded. The source's final sentence uses the GNS representation of the
*normal envelope* on \(A^{**}\). That representation has its own
precise bridge below. No unitary identification with the original
C*-semicyclic GNS representation is assumed here.

**A noncentral finite-domain corner.** Let \(A=M_2(\mathbb C)\), with standard column vectors \(e_1,e_2\), and put

\[
 p=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

Define a weight on positive matrices by

\[
 \varphi(x)=
 \begin{cases}
 t,&x=tp,\ t\geq0,\\
 \infty,&x\notin pAp.
 \end{cases}
\]

For positive \(x\), the condition \(x_{22}=0\) implies \(x^{1/2}e_2=0\), since its squared norm is \(x_{22}\). Hence the second row and column vanish, and \(x=pxp\). A positive sum therefore belongs to the corner precisely when both summands do. This proves additivity, and positive homogeneity follows directly, with the usual convention at zero. Each finite sublevel set is the closed interval \(\{tp:0\leq t\leq c\}\), so the weight is norm lower semicontinuous. It is faithful because its only zero is the zero matrix.

For an increasing net \(x_j\uparrow x\), if \(x\) is in the corner, every \(x_j\) is there and the first diagonal entries increase to that of \(x\). If \(x\) is outside, some \(x_j\) must be outside the closed corner, so the supremum of the weights is already infinite. This also proves normality. Coordinate functionals identify the bidual of this finite-dimensional matrix space with itself; the corner-envelope formula in LW06 consequently gives \(\Phi=\varphi\).

The finite left ideal and its GNS map are

\[
 \begin{aligned}
 \mathfrak n_\varphi&=Ap=\{a:a=ap\},\\
 \Lambda_\varphi(a)&=ae_1\in\mathbb C^2.
 \end{aligned}
\]

Indeed, \((a^*a)_{22}=\|ae_2\|^2\); finiteness is exactly the vanishing of the second column, and then \(\varphi(a^*a)=\|ae_1\|^2\). Every first column occurs, so this map already has range all of \(\mathbb C^2\), with no null vectors in \(Ap\). Left multiplication becomes the usual faithful matrix action. Its kernel is zero, whereas the finite positive domain spans only \(pAp\). This corner is proper and noncentral: multiplying \(p\) on the two sides of the matrix unit with its sole nonzero entry in position \((1,2)\) gives different answers. Thus faithfulness of the weight and of its GNS representation does not make its finite-domain projection central or equal to one. In the transfer below the central projection is \(z=1\), but the finite-domain projection remains \(p\).

## Transfer to the normal-envelope GNS algebra

Let \(N=A^{**}\), and form the semicyclic GNS triple
\((H_\Phi,\pi_\Phi,\Lambda_\Phi)\) of the normal weight from LW-06.
The normal GNS theorem proves that
\(\pi_\Phi:N\to B(H_\Phi)\) is normal, without requiring semifiniteness.
It is unital on its GNS space, including the zero-space convention.
Set \(M_\Phi=\pi_\Phi(N)''\). The kernel of \(\pi_\Phi\) is an
ultraweakly closed two-sided ideal, hence \(N(1-z)\) for a central
projection \(z\in N\), by the central-ideal theorem.
The restriction \(q=\pi_\Phi|_{zN}\) is an isometric normal
*-homomorphism. Its unit-ball image is ultraweakly compact, hence
closed, and is exactly the unit ball of \(\pi_\Phi(N)\).
Kaplansky density
puts the unit ball of the bicommutant in the ultraweak closure of
that represented ball. Hence the image ball is already the unit
ball of \(M_\Phi\), and \(\pi_\Phi(N)=M_\Phi\).
The predual argument in Surjectivity uses a compact ball and the exact density theorem
makes \(q^{-1}\) normal. Thus

\[
\begin{gathered}
M_\Phi=\pi_\Phi(N),\\
q:zN\xrightarrow{\ \cong\ }M_\Phi.
\end{gathered}
\tag{LW.30}
\]

For \(y\in(M_\Phi)_+\), there is now a well-defined normal weight:

\[
\Theta(y)=\Phi(q^{-1}(y)).
\tag{LW.31}
\]

It is the restriction of \(\Phi\) to the represented central
summand, transported by a normal isomorphism. The crucial point is
that this transport preserves the *GNS data*, even if it does not
preserve every infinite value of \(\Phi\).

For \(x\in\mathfrak n_\Phi\), the GNS module relation gives
\(\Lambda_\Phi((1-z)x)=\pi_\Phi(1-z)\Lambda_\Phi(x)\).
Since \(\pi_\Phi(1-z)=0\),

\[
\begin{gathered}
\Lambda_\Phi((1-z)x)=0,\\
\Phi((1-z)x^*x)=0.
\end{gathered}
\tag{LW.32}
\]

For \(y=\pi_\Phi(x)\), centrality of \(z\) and additivity of \(\Phi\) imply

\[
\begin{gathered}
\Theta(y^*y)=\Phi(zx^*x)\\
=\Phi(x^*x).
\end{gathered}
\tag{LW.33}
\]

Consequently \(\pi_\Phi(x)\in\mathfrak n_\Theta\), and

\[
U\Lambda_\Phi(x)
 =\Lambda_\Theta(\pi_\Phi(x))
\tag{LW.34}
\]

is well-defined and isometric by polarization. It is onto:
every \(y\in\mathfrak n_\Theta\) has a unique lift
\(x=q^{-1}(y)\in zN\) with \(\Phi(x^*x)<\infty\), hence is in the
displayed range after completion. On GNS vectors the module
identities give
\(U\pi_\Phi(a)U^*=\pi_\Theta(\pi_\Phi(a))\).
Thus the GNS representation of \(\Theta\) is exactly the concrete
inclusion of \(M_\Phi\) on \(H_\Phi\), up to \(U\); their commutants
are conjugate by \(U\).

For \(a\in N_+\) with \(\Phi(a)<\infty\), take
\(x=a^{1/2}\) in (LW.32). Then
\(\Phi((1-z)a)=0\), so

\[
\Phi(a)=\Theta(\pi_\Phi(a)).
\tag{LW.35}
\]

This equality need not hold at an infinite value. In the
\(\mathbb C^2\) example of LW-08, \(z=(1,0)\),
\(M_\Phi=\mathbb C\), and \(\Theta(t)=t\) for \(t\geq0\).
The projection \((0,1)\) has \(\Phi(0,1)=\infty\) but is sent
to zero. The central-summand transfer is therefore a precise
meaning for viewing the envelope on its GNS algebra, while the
unrestricted pullback identity remains false.

## The opposite weight on the correct commutant

The weight \(\Theta\) is normal on the von Neumann algebra
\(M_\Phi\). Its GNS representation is unitarily the concrete
inclusion just proved. Apply the arbitrary-normal opposite-weight
construction to this exact
normal input, including its finite-domain projection. It gives
a faithful semifinite normal weight \(\Theta^{\mathrm{opp}}\)
on \(\pi_\Theta(M_\Phi)'\). Transporting it along \(U\) defines

\[
\begin{gathered}
\Phi_{\mathrm{env}}^{\mathrm{opp}}(h)\\
=\Theta^{\mathrm{opp}}(UhU^*).
\end{gathered}
\tag{LW.36}
\]

Unitary transport preserves the weight axioms, normality,
faithfulness, and semifiniteness. This includes a zero GNS
space: the opposite algebra is then zero and its unique weight
has all three properties.

The commutant in (LW.36) is that of the **envelope GNS algebra**
\(M_\Phi=\pi_\Phi(A^{**})''\), as in the final sentence of the
source passage. The construction makes no equality claim
\(\Phi=\Theta\circ\pi_\Phi\) on all positive elements, and it
does not silently identify this GNS space with the GNS space
built earlier directly from \(\varphi\) on \(A\).
For a proper noncentral finite-domain corner such as the
\(M_2(\mathbb C)\) example proved in LW-08, the
arbitrary-normal form of OW-14 is needed: its finite value uses
the finite-domain projection rather than an unrestricted norm
of a representing functional.

## Source and scope

The mathematical antecedents are Takesaki, *Theory of Operator Algebras II*, Chapter VII, §4, Lemma 4.1, Proposition 4.2, and the unnumbered continuation (printed pp. 88–90; PDF pp. 109–111 in the checked receipt-backed copy). LW-01–03 cover the numbered results. LW-04–07 give an original dense-case and hereditary-corner proof of the strict family and universal normal envelope at arbitrary C*-algebra generality. LW-08 records the exact semifiniteness boundary and the false unrestricted GNS pullback. LW-09–10 make the source's final envelope-GNS viewpoint precise through a normal central-summand transfer and the exact existing arbitrary-normal opposite-weight theorem. They do not claim equality of infinite values across the GNS quotient or identify the envelope GNS space with the original C*-weight GNS space. For freely accessible comparisons, Johan Kustermans, [*KMS-weights on C*-algebras*](https://arxiv.org/abs/funct-an/9704008), §3, pp. 19–21, proves strict-family directedness under the dense-left-ideal setup stated on p. 19 (Lemmas 3.3–3.4 and Proposition 3.5). LW05 retains the local resolvent proof; LW04 and LW06–07 supply the additional hereditary-corner and off-diagonal arguments needed without density. Johan Kustermans and Stefaan Vaes, [*Weight theory for C*-algebraic quantum groups*](https://arxiv.org/abs/math/9901063), Definitions 1.3 and 1.5, Theorem 1.6 and Proposition 1.7, pp. 4–5, provide a further comparison for the functional families, lower semicontinuity and GNS properties. Their recovery theorem is stated there with an external reference; its complete proof here is LW02–03. Neither reference replaces a course proof.
