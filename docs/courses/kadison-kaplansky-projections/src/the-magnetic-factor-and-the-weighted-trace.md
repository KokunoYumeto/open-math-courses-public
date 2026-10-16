# The magnetic factor and the weighted trace

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A projection \(p_t\) of the previous lesson has trace about \(t^{n_{\mathrm f}}\), small near the end \(t=0\) of the interval \((0,\delta)\) of central characters but not near \(t=\delta\). In the model operator the supporting layers move to one end of the tower as \(t\to0\) and to the other as \(t\to\delta\), and the trace must be small at both ends, even after multiplication by the large geometric weights \(\mathfrak w_i=2^{C_\bullet H_i}\) that pay for overlaps of copies. A finite *magnetic* representation of the second factor shifts its effective parameter from \(t\) to \(t-\delta\), at the price of a matrix multiplicity \(N\); the product projection then has trace of order \(Nt^{n_{\mathrm f}}(\delta-t)^{n_{\mathrm f}}\), and suitable choices of the scales make it small at both ends, uniformly in the layers [OpenAI-KK, Sections 8.5 and 8.6].

- Parameters (Section 1).
- A finite magnetic representation (Section 2).
- Absorption (Section 3).
- The projection field (Section 4).
- Smooth layer windows (Section 5).
- The weighted trace (Section 6).

The notation of [An affine nilpotent group](an-affine-nilpotent-group.md) and [Schwartz idempotents and lattice projections](schwartz-idempotents-and-lattice-projections.md) is in force, with \(L=\bar E_{\mathbb Z}\), the twisted representations \(u_t\), the projections \(p_\theta\) and the constant \(\theta_0\).

## 1. Parameters

The constants \(m\), \(C_*\), \(C_\bullet\) are fixed, and \(h_*=5003\) bounds \(H_0\le h_*\log_2d\). Choose fixed constants
\[
\begin{gathered}
E_0>10(C_*+C_\bullet+1),\\
A_*\in\mathbb N,\ \frac{A_*}m>10E_0h_*,\\
\kappa>0,\ \frac\kappa m>10(E_0+A_*+C_\bullet+1),
\end{gathered}
\]
and put
\[
\begin{gathered}
q=d^{A_*},\qquad\delta=q^{-1},\\
N=q^{n_{\mathrm f}},\qquad I=H_0 .
\end{gathered}
\]
These are integers except \(\delta\), and \(\ell\) is taken so large that \(\delta<\theta_0\).

## 2. A finite magnetic representation

Let \(\mathfrak n_q\) be the strictly upper triangular matrices over \(\mathbb Z/q\mathbb Z\), a set of \(q^{n_{\mathrm f}}=N\) elements. On \(\mathbb C^N=\ell^2(\mathfrak n_q)\) define, for \((\lambda,b,z)\in E_{\mathbb Z}\),
\[
\begin{aligned}
&(R(\lambda,b,z)\psi)(x)\\
&\quad=\mathbf e\Bigl(-\frac{z+\lambda(x)}q\Bigr)\,\psi\bigl(b^{-1}(1+x)-1\bigr),
\end{aligned}
\]
with all arguments reduced modulo \(q\); the phase depends only on the residue of the integer \(z+\lambda(x)\). The affine map is a permutation of \(\mathfrak n_q\) and the phase has modulus one, so \(R(\lambda,b,z)\) is unitary. The identity \(\mu(A_{b^{-1}}x)=c(\gamma,\eta)+(\mu\circ L_{b^{-1}})(x)\) used in the proof of Lemma 1.1 of the previous lesson is an identity of integer polynomials, so it holds modulo \(q\), and the computation given there, with the phase \(-1/q\) in place of \(\epsilon\), gives that \(R(\lambda,b,0)R(\mu,b',0)\) equals \(\mathbf e(-c(\gamma,\eta)/q)R(\gamma\eta,0)\) for \(\gamma=(\lambda,b)\), \(\eta=(\mu,b')\). Since \(R(\lambda,b,z)=\mathbf e(-z/q)R(\lambda,b,0)\) and the law (1.1) of [An affine nilpotent group](an-affine-nilpotent-group.md) adds \(c(\gamma,\eta)\) to the central coordinates, \(R\) is a representation of \(E_{\mathbb Z}\). Its central character is \(R(0,1,z)=\mathbf e(-\delta z)\). Write \(R_\gamma=R(\sigma(\gamma))\) for \(\gamma\in L\).

Reduction modulo \(q\) is a surjective homomorphism \(L\to\bar E_{\mathbb Z/q\mathbb Z}\), because the group law has integer coefficients. Its kernel is
\[
\begin{gathered}
\Lambda_q=\bigl\{(\lambda,b)\in L:\\
\lambda_{ij}\equiv(b-1)_{ij}\equiv0\pmod q\bigr\},
\end{gathered}
\]
of index \(q^{2n_{\mathrm f}}\), and
\[
R_y=1_N\qquad(y\in\Lambda_q),\tag{2.1}
\]
because then \(\lambda(x)\in q\mathbb Z\) and \(b\equiv1\) modulo \(q\).

## 3. Absorption

**Lemma 3.1** (absorption of the finite factor; [OpenAI-KK, Lemma 8.9]). On \(\ell^2(L)\otimes\mathbb C^N\) put \(V_t(\gamma)=u_t(\gamma)\otimes R_\gamma\). Then \(V_t(\gamma)V_t(\eta)=\mathbf e((t-\delta)c(\gamma,\eta))V_t(\gamma\eta)\), and the unitary \(W(\delta_\eta\otimes v)=\delta_\eta\otimes R_\eta v\) satisfies
\[
W^*V_t(\gamma)W=u_{t-\delta}(\gamma)\otimes1_N .
\]
It fixes \(\delta_1\otimes\mathbb C^N\) pointwise. Consequently every coefficient sum in the \(V_t(\gamma)\), and every continuous function of a self-adjoint one, has the same norm as the corresponding element for \(u_{t-\delta}\), and its identity trace, summed over the \(N\) matrix indices, is \(N\) times the identity trace of that element.

*Proof.* The section law and the central character give \(R_\gamma R_\eta=R((0,1,c(\gamma,\eta))\sigma(\gamma\eta))\), which is \(\mathbf e(-\delta c(\gamma,\eta))R_{\gamma\eta}\); with the multiplier of \(u_t\) this gives the multiplier of \(V_t\). Then
\[
\begin{aligned}
&V_t(\gamma)W(\delta_\eta\otimes v)\\
&\quad=\mathbf e(tc(\gamma,\eta))\delta_{\gamma\eta}\otimes R_\gamma R_\eta v\\
&\quad=\mathbf e((t-\delta)c(\gamma,\eta))\delta_{\gamma\eta}\otimes R_{\gamma\eta}v ,
\end{aligned}
\]
which is \(W(u_{t-\delta}(\gamma)\otimes1)(\delta_\eta\otimes v)\). Since \(R_1=1\), \(W\) fixes \(\delta_1\otimes v\). Conjugation by \(W\) carries a coefficient sum \(x\) in the \(V_t(\gamma)\) to \(y\otimes1_N\), with \(y\) the same sum in the \(u_{t-\delta}(\gamma)\), and
\[
\begin{aligned}
&\sum_j\langle x(\delta_1\otimes e_j),\delta_1\otimes e_j\rangle\\
&\quad=\sum_j\langle(y\otimes1)(\delta_1\otimes e_j),\delta_1\otimes e_j\rangle\\
&\quad=N\langle y\delta_1,\delta_1\rangle .
\end{aligned}
\]
Both statements pass to norm limits and to continuous functions. \(\square\)

The operators \(V_t(\gamma)\) commute with the right operators \(v_t(k)\otimes1_N\), so the identity trace above is the one of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md), Section 2.

## 4. The projection field

Every element of \(F\) is uniquely \(\sigma_X(\gamma)\sigma_Y(\gamma')z_0^n\), and by Lemma 5.1 of [An affine nilpotent group](an-affine-nilpotent-group.md), \(\lambda(\sigma_X(\gamma)\sigma_Y(\gamma')z_0^n)\otimes W\), with \(W\in M_N(\mathbb C)\), acts in the fiber at \(t\) of (5.1) there, amplified by \(\mathbb C^N\), by
\[
\mathbf e(nt)\,u_t(\gamma)\otimes u_t(\gamma')\otimes W .
\]
For \(W=R_{\gamma'}\) the second factor acts by \(V_t(\gamma')\). So in the fibers of sums of the elements \(\lambda(\sigma_X(\gamma)\sigma_Y(\gamma')z_0^n)\otimes R_{\gamma'}\), the first factor acts through \(u_t\) and the second through \(V_t\); the two commute, and both commute with the right operators \(v_t(k)\otimes v_t(k')\otimes1_N\).

For \(0<t<\delta\), both \(t\) and \(t-\delta\) lie in \((-\theta_0,\theta_0)\setminus\{0\}\). Put
\[
p(t)=p_t\otimes p_{t-\delta}[V_t] ,
\]
where \(p_{t-\delta}[V_t]\) is obtained by evaluating the coefficients of \(K_{t-\delta}\) on the \(V_t(\gamma)\) and applying the same continuous function; by Lemma 3.1 it is conjugate by \(W\) to \(p_{t-\delta}\otimes1_N\). Put \(p(t)=0\) for \(t\notin(0,\delta)\). This is a measurable field of equivariant projections, and its identity trace \(s_p(t)\), summed over the matrix indices, satisfies, for \(0<t<\delta\), by Proposition 3.1 of the previous lesson and Lemma 3.1,
\[
\begin{aligned}
&0<s_p(t)\\
&\quad=N\operatorname{tr}_t(p_t)\operatorname{tr}_{t-\delta}(p_{t-\delta})\\
&\quad\le C\,N\,t^{n_{\mathrm f}}(\delta-t)^{n_{\mathrm f}} .
\end{aligned}\tag{4.1}
\]

## 5. Smooth layer windows

**Lemma 5.1** (smooth layer windows; [OpenAI-KK, Lemma 8.10]). There is a smooth function \(h\ge0\), supported in \((-1,1)\) and positive on \([-0.7,0.7]\), with \(\sum_{i\in\mathbb Z}h(v-i)^2=1\) for all \(v\in\mathbb R\). For \(0<t<\delta\) put
\[
\begin{gathered}
b(t)=\kappa^{-1}\log_2\frac t{\delta-t},\\
h_i(t)=h(b(t)-i),
\end{gathered}
\]
and \(h_i=0\) outside \((0,\delta)\). Each \(h_i\) is smooth on the circle; the set \(J(t)=\{i:h_i(t)\ne0\}\) has one element or two adjacent elements, and \(\sum_ih_i(t)^2=1\) on \((0,\delta)\). With \(w_i=q^{-1}2^{-\kappa|i|}\), the support of \(h_i\) has length at most \(C_\kappa w_i\), and \(\|\partial_t^jh_i\|_\infty\le C_{\kappa,j}w_i^{-j}\). For \(i\in J(t)\),
\[
\begin{aligned}
\log_2t^{-1}&=\log_2q+\kappa\max(-i,0)\\
&\quad+O_\kappa(1),\\
\log_2(\delta-t)^{-1}&=\log_2q+\kappa\max(i,0)\\
&\quad+O_\kappa(1),\\
t(\delta-t)&\le2^\kappa q^{-2}2^{-\kappa|i|} .
\end{aligned}
\]

*Proof.* Take a smooth \(\beta\ge0\) supported in \((-0.9,0.9)\) and positive on \([-0.7,0.7]\), and \(h=\beta\bigl(\sum_j\beta(\cdot-j)^2\bigr)^{-1/2}\); the sum is smooth, periodic and positive, because some translate of every \(v\) lies in \([-\frac12,\frac12]\). An interval of length \(1.8\) contains at most two integers, adjacent. The support of \(h_i\) corresponds to \(|b-i|<0.9\), a compact subset of \((0,\delta)\), so \(h_i\) extends smoothly by zero.

The inverse of \(b\) is \(t(b)=\delta\frac{2^{\kappa b}}{1+2^{\kappa b}}\), with \(\delta-t(b)=\frac\delta{1+2^{\kappa b}}\) and \(t'(b)=\kappa\ln2\,\frac{t(\delta-t)}\delta\). For \(|b-i|\le0.9\), \(t'(b)\) lies between two positive multiples of \(w_i\), depending on \(\kappa\), and all higher derivatives in \(b\) are at most a multiple of \(w_i\). The chain rule for the inverse function gives the derivative bounds, and integrating \(t'\) the support bound. Finally \(\log_2t(b)^{-1}=\log_2q+\log_2(1+2^{-\kappa b})\) and \(\log_2(\delta-t(b))^{-1}\) equals \(\log_2q+\log_2(1+2^{\kappa b})\), where \(\log_2(1+2^x)-\max(x,0)\in[0,1]\), and \(|b-i|<1\); and \(\frac{2^{\kappa b}}{(1+2^{\kappa b})^2}\le2^{-\kappa|b|}\le2^\kappa2^{-\kappa|i|}\). \(\square\)

## 6. The weighted trace

**Proposition 6.1** (uniform weighted trace bound; [OpenAI-KK, Proposition 8.11]). Let \(\mathfrak w_i=2^{C_\bullet H_i}\) and
\[
\begin{aligned}
\mu_\ell=\sup\bigl\{&\mathfrak w_i\,s_p(t):\\
&0<t<\delta,\ i\in J(t)\bigr\} .
\end{aligned}
\]
Then \(\mu_\ell\to0\) as \(\ell\to\infty\). More precisely, for \(i\in J(t)\),
\[
\begin{aligned}
&\mathfrak w_iNt^{n_{\mathrm f}}(\delta-t)^{n_{\mathrm f}}\\
&\quad\le2^{\kappa n_{\mathrm f}}d^{-(A_*n_{\mathrm f}-C_\bullet h_*)}2^{-(\kappa n_{\mathrm f}-C_\bullet)|i|},
\end{aligned}
\]
and both exponents subtracted on the right are positive.

*Proof.* With \(H_i=H_0+|i|\), \(H_0\le h_*\log_2d\), \(N=q^{n_{\mathrm f}}\) and Lemma 5.1,
\[
\begin{aligned}
&\mathfrak w_iN\bigl(t(\delta-t)\bigr)^{n_{\mathrm f}}\\
&\quad\le2^{C_\bullet H_0}2^{C_\bullet|i|}q^{n_{\mathrm f}}\bigl(2^\kappa q^{-2}2^{-\kappa|i|}\bigr)^{n_{\mathrm f}}\\
&\quad\le2^{\kappa n_{\mathrm f}}d^{C_\bullet h_*}d^{-A_*n_{\mathrm f}}2^{-(\kappa n_{\mathrm f}-C_\bullet)|i|} .
\end{aligned}
\]
The choices of Section 1 give \(A_*n_{\mathrm f}\ge A_*>10mE_0h_*>C_\bullet h_*\) and \(\kappa n_{\mathrm f}\ge\kappa>C_\bullet\). By (4.1), \(\mu_\ell\le C2^{\kappa n_{\mathrm f}}d^{-(A_*n_{\mathrm f}-C_\bullet h_*)}\), which tends to zero. \(\square\)

The constants are fixed in this order: the geometry fixes \(C_*\) and \(C_\bullet\); then \(m\), and the functions \(J_\pm\); then \(E_0\), \(A_*\), \(\kappa\); later, all accuracies of the approximation in the next lessons; only then is \(\ell\) increased.

## 7. Exercises

**7.1** (easy). For \(q=2\) and \(m=2\), write elements of \(L\) as \((\lambda,\beta)\) with \(b=1+\beta\), as in the exercises of [An affine nilpotent group](an-affine-nilpotent-group.md). Write the four matrices \(R_{(\lambda,\beta)}\), \(\lambda,\beta\in\{0,1\}\), on \(\mathbb C^2=\ell^2(\mathbb Z/2)\), and check \(R_\gamma R_\eta=\mathbf e(-c(\gamma,\eta)/2)R_{\gamma\eta}\) for \(\gamma=(0,1)\), \(\eta=(1,0)\).

**7.2** (easy). Show that \(\Lambda_q\) has index \(q^{2n_{\mathrm f}}\) in \(L\).

**7.3** (medium). In Lemma 5.1, show that as \(t\to0\) the active layers tend to \(-\infty\), and as \(t\to\delta\) to \(+\infty\).

**7.4** (medium). Show that \(\operatorname{tr}_\theta(p_\theta)\ge c|\theta|^{n_{\mathrm f}}\) for \(0<|\theta|<\theta_0\), with \(c>0\) depending only on \(m\) and \(J_\pm\), after decreasing \(\theta_0\) if necessary. Deduce that without the magnetic factor, that is with \(p_t\otimes p_t\) in place of \(p(t)\), the supremum \(\mu_\ell\) of Proposition 6.1 would be infinite for every \(\ell\).

## 8. Solutions

**7.1.** For \(m=2\) and \(q=2\), \((R_{(\lambda,\beta)}\psi)(x)=(-1)^{\lambda x}\psi(x-\beta)\), \(x\in\mathbb Z/2\): the identity, the diagonal matrix \(\operatorname{diag}(1,-1)\), the swap of the two coordinates, and their product. For \(\gamma=(0,1)\), \(\eta=(1,0)\): \(c(\gamma,\eta)=-\mu\beta=-1\) and \(\gamma\eta=(1,1)\), so the claim is \(R_\gamma R_\eta=-R_{\gamma\eta}\). Indeed \(R_\gamma R_\eta\psi(x)=(-1)^{x-1}\psi(x-1)\) and \(R_{(1,1)}\psi(x)=(-1)^x\psi(x-1)\).

**7.2.** Reduction modulo \(q\) is surjective onto a group of \(q^{2n_{\mathrm f}}\) elements, the pairs of a functional and a unitriangular matrix modulo \(q\), and \(\Lambda_q\) is its kernel.

**7.3.** \(b(t)=\kappa^{-1}\log_2\frac t{\delta-t}\) tends to \(-\infty\) as \(t\to0\) and to \(+\infty\) as \(t\to\delta\), and \(J(t)\) consists of integers within distance one of \(b(t)\).

**7.4.** In the proof of Proposition 3.1 of the previous lesson, \(p_\theta-K_\theta=f(K_\theta)(K_\theta^2-K_\theta)\) with \(\|f(K_\theta)\|\le2\), so
\[
\begin{aligned}
\|p_\theta\delta_1\|&\ge\|K_\theta\delta_1\|-2\|(K_\theta^2-K_\theta)\delta_1\|\\
&\ge C^{-1}\sqrt\nu-2Cy\sqrt\nu\\
&\ge(2C)^{-1}\sqrt\nu
\end{aligned}
\]
for small \(y\), and \(\operatorname{tr}_\theta(p_\theta)=\|p_\theta\delta_1\|^2\ge(4C^2)^{-1}|\theta|^{n_{\mathrm f}}\). For \(\delta/2<t<\delta\) the trace of \(p_t\otimes p_t\) is then at least \(c^2(\delta/2)^{2n_{\mathrm f}}>0\), a bound independent of \(t\), while \(J(t)\) contains integers \(i\to+\infty\) as \(t\to\delta\) (Exercise 7.3) and \(\mathfrak w_i=2^{C_\bullet(H_0+|i|)}\) is unbounded.

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Sections 8.5 and 8.6, Lemmas 8.9 and 8.10, Proposition 8.11. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026
