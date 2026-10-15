# The regular trace and spectral phase

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The proof of the Kervaire conjecture in this course measures words in a group \(A\) by operators on the Hilbert space \(\ell^2(A)\). Every group, finite or not, countable or not, acts on \(\ell^2(A)\) by left translations, and the operators commuting with the right translations carry a trace that vanishes on no nonzero positive operator. This lesson constructs that trace on matrices over the right-translation commutant, and with it a number \(\ell(U)\) attached to every unitary matrix \(U\): the trace of its spectral phase, with every spectral angle measured in \([0,1)\) turns. The main result is that \(\ell\) is subadditive, \(\ell(UV)\le\ell(U)+\ell(V)\), and vanishes only at the identity [OpenAI-K, Section 2]. The next lessons use it twice: an upper bound for \(\ell\) of a product comes from subadditivity, and a lower bound from a direct calculation, and the gap between them is the trace of the phase of a single group element.

- The right-translation commutant and its trace (Section 1).
- Functional calculus inside the commutant (Section 2).
- Spectral phase (Section 3).
- Subadditivity (Section 4).

We use the Borel functional calculus of normal operators, Theorems 3.1 and 8.1 and Remark 4.5 of [The spectral theorem for bounded self-adjoint operators](course:foundations-of-von-neumann-algebras/the-spectral-theorem-for-bounded-self-adjoint-operators), and the continuous functional calculus, Theorem 5.1 of [C\*-algebras, the continuous functional calculus, automatic continuity and positive cones](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones).

## 1. The right-translation commutant and its trace

Let \(A\) be a group with identity \(1\). The Hilbert space \(\ell^2(A)\) has the orthonormal basis \((\delta_x)_{x\in A}\). For \(a\in A\) define unitary operators by
\[
\begin{gathered}
L(a)\delta_x=\delta_{ax},\\
R(a)\delta_x=\delta_{xa^{-1}} .
\end{gathered}
\]
Then \(L(ab)=L(a)L(b)\), \(R(ab)=R(a)R(b)\), \(L(a)^*=L(a^{-1})\), \(R(a)^*=R(a^{-1})\), and every \(L(a)\) commutes with every \(R(b)\). Let
\[
\begin{gathered}
\mathcal M=\{T\in B(\ell^2(A)):\\
TR(a)=R(a)T\text{ for all }a\in A\}
\end{gathered}
\]
be the commutant of the right translations. It is a unital algebra containing every \(L(a)\), and it is closed under adjoints, since \(TR(a)=R(a)T\) for all \(a\) gives \(R(a)^*T^*=T^*R(a)^*\), that is \(R(a^{-1})T^*=T^*R(a^{-1})\), for all \(a\). It is the group von Neumann algebra of \(A\), described through the right translations [Jones, Sections 3.3 and 3.4]; this lesson uses only the definition. For \(T\in\mathcal M\) put
\[
\tau(T)=\langle T\delta_1,\delta_1\rangle .
\]

**Lemma 1.1** (matrix coefficients). Let \(T\in\mathcal M\) and \(t_x=\langle T\delta_1,\delta_x\rangle\). Then \(\langle T\delta_y,\delta_x\rangle=t_{xy^{-1}}\) for all \(x,y\in A\), and \(\sum_x|t_x|^2=\|T\delta_1\|^2<\infty\).

*Proof.* Since \(R(y^{-1})\delta_1=\delta_y\), we have \(T\delta_y=TR(y^{-1})\delta_1=R(y^{-1})T\delta_1\), so
\[
\begin{aligned}
\langle T\delta_y,\delta_x\rangle&=\langle T\delta_1,R(y^{-1})^*\delta_x\rangle\\
&=\langle T\delta_1,R(y)\delta_x\rangle\\
&=\langle T\delta_1,\delta_{xy^{-1}}\rangle\\
&=t_{xy^{-1}} .
\end{aligned}
\]
The second statement is Parseval's identity for the vector \(T\delta_1\). \(\square\)

A square-summable family has at most countably many nonzero terms, so the sums below are ordinary absolutely convergent series even when \(A\) is uncountable.

**Lemma 1.2** (the trace). For \(S,T\in\mathcal M\):

1. \(\tau(ST)=\tau(TS)\);
2. if \(T\ge0\), then \(\tau(T)\ge0\), and \(\tau(T)=0\) only for \(T=0\).

*Proof.* (1) Write \(s_x=\langle S\delta_1,\delta_x\rangle\) and \(t_x=\langle T\delta_1,\delta_x\rangle\). Expanding \(T\delta_1\) in the basis,
\[
\begin{aligned}
\tau(ST)&=\sum_x t_x\langle S\delta_x,\delta_1\rangle\\
&=\sum_xt_xs_{x^{-1}} ,
\end{aligned}
\]
by Lemma 1.1 with \(y=x\) and \(1\) in place of \(x\). The series converges absolutely by the Cauchy–Schwarz inequality, because \((t_x)\) and \((s_{x^{-1}})\) are square-summable. Exchanging the roles of \(S\) and \(T\) and substituting \(x\mapsto x^{-1}\) gives the same sum for \(\tau(TS)\).

(2) For \(T\ge0\), the positive square root \(T^{1/2}\) commutes with every operator commuting with \(T\) (Theorem 3.1(5) of the spectral theorem lesson), so \(T^{1/2}\in\mathcal M\). Now \(\tau(T)=\|T^{1/2}\delta_1\|^2\ge0\). If \(\tau(T)=0\), then \(T^{1/2}\delta_1=0\), and \(T^{1/2}\delta_y=T^{1/2}R(y^{-1})\delta_1\), which is \(R(y^{-1})T^{1/2}\delta_1=0\), for every \(y\); so \(T^{1/2}=0\) and \(T=0\). \(\square\)

**Matrices.** Fix \(b\ge1\) and let \(H_b=\mathbb C^b\otimes\ell^2(A)\), the direct sum of \(b\) copies of \(\ell^2(A)\), with basis vectors \(e_j\otimes\delta_x\). An operator on \(H_b\) is a \(b\times b\) matrix \((T_{jl})\) of operators on \(\ell^2(A)\). It commutes with every \(I\otimes R(a)\) exactly when every entry commutes with every \(R(a)\), so the algebra \(M_b(\mathcal M)\) of matrices with entries in \(\mathcal M\) is the commutant of the operators \(I\otimes R(a)\). For \(T=(T_{jl})\in M_b(\mathcal M)\) put
\[
\begin{aligned}
\tau_b(T)&=\sum_{j=1}^b\tau(T_{jj})\\
&=\sum_{j=1}^b\langle T(e_j\otimes\delta_1),e_j\otimes\delta_1\rangle .
\end{aligned}
\]
The trace is unnormalized: \(\tau_b(I)=b\). A scalar matrix \(Q\in M_b(\mathbb C)\) acts on \(H_b\) as \(Q\otimes I\), which lies in \(M_b(\mathcal M)\), and \(\tau_b(Q\otimes I)=\operatorname{Tr}Q\) because \(\tau(I)=1\). We write \(Q\) for \(Q\otimes I\).

**Lemma 1.3.** For \(S,T\in M_b(\mathcal M)\): \(\tau_b(ST)=\tau_b(TS)\); \(|\tau_b(T)|\le b\|T\|\) and \(\tau_b(T^*)=\overline{\tau_b(T)}\); if \(T\ge0\), then \(\tau_b(T)\ge0\), with equality only for \(T=0\).

*Proof.* By Lemma 1.2(1), \(\tau_b(ST)=\sum_{j,l}\tau(S_{jl}T_{lj})\) equals \(\sum_{j,l}\tau(T_{lj}S_{jl})=\tau_b(TS)\). The bound and the adjoint formula hold for each of the \(b\) vector functionals in the definition. If \(T\ge0\), each term \(\langle T(e_j\otimes\delta_1),e_j\otimes\delta_1\rangle=\|T^{1/2}(e_j\otimes\delta_1)\|^2\) is nonnegative; if they all vanish, then \(T^{1/2}\), which lies in \(M_b(\mathcal M)\) as in Lemma 1.2, kills every \(e_j\otimes\delta_1\) and hence every \(e_j\otimes\delta_y=(I\otimes R(y^{-1}))(e_j\otimes\delta_1)\). \(\square\)

In particular, conjugation by a unitary \(V\in M_b(\mathcal M)\) does not change the trace: \(\tau_b(VTV^*)=\tau_b(TV^*V)=\tau_b(T)\).

The same trace, together with the integrality of the trace of an idempotent proved in [Idempotents and integral traces](course:bass-trace-conjecture/idempotents-and-integral-traces), shows that the group ring of a torsion-free group over a field of characteristic zero has no idempotents other than \(0\) and \(1\) (Theorem 2.1 there). The same trace proves Kaplansky's theorem that the matrix rings over \(\mathbb C[A]\) are directly finite: if \(XY=I\), the idempotent \(YX\) and its range projection both have trace \(b\), which forces \(YX=I\) ([Directly finite group algebras](course:kaplansky-direct-finiteness/directly-finite-group-algebras), Theorem 3.1).

## 2. Functional calculus inside the commutant

Let \(\mathbb T=\{z\in\mathbb C:|z|=1\}\) and let \(B_b(\mathbb T)\) be the bounded Borel functions on \(\mathbb T\). A unitary operator \(U\) is normal with spectrum in \(\mathbb T\). For \(f\in B_b(\mathbb T)\) let \(f(U)\) be the Borel functional calculus of \(U\) applied to the restriction of \(f\) to the spectrum (Theorems 3.1 and 8.1 of the spectral theorem lesson). We use its properties: \(f\mapsto f(U)\) is a unital \(*\)-homomorphism, agrees with the continuous calculus on continuous functions, satisfies \(\|f(U)\|\le\sup|f|\), maps nonnegative functions to positive operators and real functions to self-adjoint ones; if \(f_r\to f\) pointwise with \(\sup_r\sup|f_r|<\infty\), then \(f_r(U)\xi\to f(U)\xi\) for every vector \(\xi\); and \(f(U)\) commutes with every operator that commutes with \(U\) and \(U^*\). We also use that \(\langle f(U)\xi,\xi\rangle=\int f\,d\mu_\xi\) for a finite measure \(\mu_\xi\) on the spectrum, which is determined by the integrals of continuous functions.

**Lemma 2.1.** Let \(U\in M_b(\mathcal M)\) be unitary and \(f\in B_b(\mathbb T)\).

1. \(f(U)\in M_b(\mathcal M)\).
2. If \(f_r\to f\) pointwise on \(\mathbb T\) with \(\sup_r\sup|f_r|<\infty\), then \(\tau_b(f_r(U))\to\tau_b(f(U))\).
3. If \(V\) is a unitary operator on \(H_b\), then \(f(VUV^*)=Vf(U)V^*\). If moreover \(V\in M_b(\mathcal M)\), then \(\tau_b(f(VUV^*))=\tau_b(f(U))\).
4. If \(f\) is real, then \(e^{2\pi if(U)}=(e^{2\pi if})(U)\), where the left side is the exponential of the self-adjoint operator \(f(U)\).
5. With \(c(z)=\bar z\), \(f(U^*)=(f\circ c)(U)\).

*Proof.* (1) \(U\) and \(U^*\) lie in \(M_b(\mathcal M)\), so they commute with every \(I\otimes R(a)\); hence so does \(f(U)\).

(2) The operators \(f_r(U)\) converge to \(f(U)\) on each of the \(b\) vectors \(e_j\otimes\delta_1\), and \(\tau_b\) is the sum of the corresponding vector functionals.

(3) The unitary \(VUV^*\) has the same spectrum \(S\) as \(U\). The map \(g\mapsto Vg(U)V^*\) is a unital \(*\)-homomorphism from \(C(S)\) to \(B(H_b)\) sending \(\iota(z)=z\) to \(VUV^*\); by the uniqueness in Theorem 5.1(1) of the C\*-algebra lesson it is the continuous calculus of \(VUV^*\). Thus for each vector \(\xi\) the measures of \(VUV^*\) at \(\xi\) and of \(U\) at \(V^*\xi\) have the same integrals of continuous functions, so they are equal, and
\[
\begin{aligned}
\langle f(VUV^*)\xi,\xi\rangle&=\langle f(U)V^*\xi,V^*\xi\rangle\\
&=\langle Vf(U)V^*\xi,\xi\rangle
\end{aligned}
\]
for every \(\xi\). An operator is determined by these numbers, so \(f(VUV^*)=Vf(U)V^*\). The trace statement follows from Lemma 1.3.

(4) By Remark 4.5 of the spectral theorem lesson, \(e^{2\pi if(U)}=\sum_{n\ge0}(2\pi i)^nf(U)^n/n!\) in norm. Since the calculus is a homomorphism, \(f(U)^n=(f^n)(U)\), so the partial sums equal \(s_N(U)\) for the partial sums \(s_N=\sum_{n\le N}(2\pi i)^nf^n/n!\). These converge to \(e^{2\pi if}\) uniformly on \(\mathbb T\), because \(f\) is bounded, and \(\|s_N(U)-(e^{2\pi if})(U)\|\le\sup|s_N-e^{2\pi if}|\).

(5) \(U^*\) is a unitary with spectrum \(c(S)\). The map \(g\mapsto(g\circ c)(U)\) is a unital \(*\)-homomorphism from \(C(c(S))\) to \(B(H_b)\) sending \(\iota\) to \(\bar\iota(U)=U^*\), so it is the continuous calculus of \(U^*\), by the same uniqueness. As in (3), the measure of \(U^*\) at \(\xi\) is the image under \(c\) of the measure of \(U\) at \(\xi\), and \(\langle f(U^*)\xi,\xi\rangle=\langle(f\circ c)(U)\xi,\xi\rangle\) for all \(\xi\). \(\square\)

## 3. Spectral phase

Define the Borel function \(h:\mathbb T\to[0,1)\) by
\[
\begin{gathered}
h(e^{2\pi ix})=x-\lfloor x\rfloor\\
(x\in\mathbb R) ,
\end{gathered}
\]
so \(h(1)=0\), and \(h(z)\) is the angle of \(z\) in turns, taken in \([0,1)\). It is continuous except at \(1\), where it jumps from values near \(1\) to \(0\). For a unitary \(U\in M_b(\mathcal M)\) put
\[
\ell(U)=\tau_b(h(U)) ,
\]
the *spectral phase* of \(U\).

**Lemma 3.1.** Let \(U\in M_b(\mathcal M)\) be unitary.

1. \(0\le h(U)\le I\) and \(e^{2\pi ih(U)}=U\).
2. \(0\le\ell(U)\le b\), and \(\ell(U)=0\) exactly when \(U=I\).
3. If \(V\in M_b(\mathcal M)\) is unitary, then \(\ell(VUV^*)=\ell(U)\).
4. If \(U=Q\) is a scalar unitary matrix with eigenvalues \(\lambda_1,\ldots,\lambda_b\), listed with multiplicity, then \(\ell(Q)=\sum_jh(\lambda_j)\).

*Proof.* (1) \(0\le h\le1\) gives \(0\le h(U)\le I\). Since \(e^{2\pi ih(z)}=z\) for all \(z\in\mathbb T\), Lemma 2.1(4) gives \(e^{2\pi ih(U)}=\iota(U)=U\), where \(\iota(z)=z\).

(2) The bounds follow from (1) and Lemma 1.3. If \(\ell(U)=0\), then \(h(U)=0\) by faithfulness, and \(U=e^{0}=I\) by (1). Conversely \(h(I)=h(1)I=0\).

(3) is Lemma 2.1(3).

(4) Diagonalize \(Q=VDV^*\) with a scalar unitary \(V\) and \(D=\operatorname{diag}(\lambda_j)\). For a vector \(\xi=\sum_je_j\otimes\xi_j\), the measure of \(D\) at \(\xi\) is \(\sum_j\|\xi_j\|^2\delta_{\lambda_j}\), so \(h(D)=\operatorname{diag}(h(\lambda_j))\). Then \(h(Q)=Vh(D)V^*\) by Lemma 2.1(3), and \(\ell(Q)=\operatorname{Tr}h(Q)=\sum_jh(\lambda_j)\). \(\square\)

The value \(h(1)=0\) at the cut makes \(\ell\) faithful. It also makes \(\ell\) discontinuous: the scalar unitary \(e^{-2\pi i\epsilon}\) has phase \(1-\epsilon\), close to \(1\), while its limit \(1\) has phase \(0\). The next lessons use this deliberately, approaching the cut from below on some boundary words and from above on another.

## 4. Subadditivity

**Lemma 4.1** (subadditivity of spectral phase; [OpenAI-K, Lemma 2.1]). For all unitaries \(U,V\in M_b(\mathcal M)\),
\[
\ell(UV)\le\ell(U)+\ell(V).
\]

*Proof.* Put \(B=h(V)\), so \(0\le B\le I\) and \(e^{2\pi iB}=V\) by Lemma 3.1, and put
\[
W_u=Ue^{2\pi iuB}\qquad(0\le u\le1).
\]
Each \(W_u\) is a unitary in \(M_b(\mathcal M)\), \(W_0=U\), \(W_1=UV\), and \(u\mapsto W_u\) is differentiable in norm with \(\frac{d}{du}W_u=2\pi iW_uB\), from the exponential series. For a function \(f\) on \(\mathbb T\) write \(f'\) for its derivative in turns: \(f'(e^{2\pi ix})=\frac{d}{dx}f(e^{2\pi ix})\).

*Step 1: a derivative formula.* For \(f(z)=z^r\) with an integer \(r\ge1\), the product rule and Lemma 1.3 give
\[
\begin{aligned}
\frac{d}{du}\tau_b(W_u^r)&=2\pi i\sum_{j=0}^{r-1}\tau_b\bigl(W_u^{j+1}BW_u^{r-1-j}\bigr)\\
&=2\pi ir\,\tau_b(W_u^rB)\\
&=\tau_b\bigl(f'(W_u)B\bigr) ,
\end{aligned}
\]
since \(\tau_b(W_u^{j+1}BW_u^{r-1-j})=\tau_b(W_u^{r-1-j}W_u^{j+1}B)\) and \(f'(z)=2\pi irz^r\). For \(r\le-1\) the same calculation with \(\frac{d}{du}W_u^{-1}=-2\pi iBW_u^{-1}\) gives the same formula, and for \(r=0\) both sides vanish. Now let \(f\) be a smooth function on \(\mathbb T\) with Fourier series \(f(e^{2\pi ix})=\sum_ra_re^{2\pi irx}\). Integrating by parts three times gives \(|a_r|\le C/|r|^3\) for \(r\ne0\), so \(\sum_r(1+|r|)|a_r|<\infty\). Hence \(f(W)=\sum_ra_rW^r\) and \(f'(W)=\sum_r2\pi ira_rW^r\), with norm-convergent series, for every unitary \(W\), and the derivatives \(2\pi ira_r\tau_b(W_u^rB)\) of the terms of \(\tau_b(f(W_u))\) are bounded by \(2\pi b|r||a_r|\), uniformly in \(u\). So the series may be differentiated term by term:
\[
\begin{aligned}
&\frac{d}{du}\tau_b\bigl(f(W_u)\bigr)\\
&\qquad=\tau_b\bigl(f'(W_u)B\bigr).
\end{aligned}\tag{4.1}
\]

*Step 2: smooth functions with slope at most one.* Let \(f\) be smooth and real with \(f'\le1\). Then \(f'(W_u)\) is self-adjoint with \(f'(W_u)\le I\), and \(B^{1/2}\in M_b(\mathcal M)\). By Lemma 1.3,
\[
\begin{aligned}
\tau_b\bigl(f'(W_u)B\bigr)&=\tau_b\bigl(B^{1/2}f'(W_u)B^{1/2}\bigr)\\
&\le\tau_b(B^{1/2}B^{1/2})\\
&=\tau_b(B) ,
\end{aligned}
\]
because \(B^{1/2}(I-f'(W_u))B^{1/2}\ge0\). The right side of (4.1) is continuous in \(u\), so integrating from \(0\) to \(1\) gives
\[
\begin{aligned}
&\tau_b\bigl(f(UV)\bigr)\\
&\qquad\le\tau_b\bigl(f(U)\bigr)+\tau_b\bigl(h(V)\bigr).
\end{aligned}\tag{4.2}
\]

*Step 3: passing to \(h\).* Let \(g(x)=x-\lfloor x\rfloor\). For \(0<\epsilon<1\) choose a smooth function \(\rho_\epsilon\ge0\) on \(\mathbb R\), supported in \((0,\epsilon)\), with integral \(1\), and put
\[
\begin{aligned}
f_\epsilon(e^{2\pi ix})&=\int_0^\epsilon\rho_\epsilon(s)\,g(x+s)\,ds\\
&=\int_{\mathbb R}\rho_\epsilon(y-x)\,g(y)\,dy .
\end{aligned}
\]
The second form shows that \(f_\epsilon\) is smooth, and it is periodic because \(g\) is. Its values lie in \([0,1)\). For \(\delta\ge0\), \(g(x+\delta)-g(x)=\delta-(\lfloor x+\delta\rfloor-\lfloor x\rfloor)\le\delta\), and averaging gives \(f_\epsilon(x+\delta)-f_\epsilon(x)\le\delta\); so \(f_\epsilon'\le1\). Finally, \(g\) is continuous from the right at every point, including the integers, where \(g(n+s)=s\to0=g(n)\); so \(\sup_{0<s<\epsilon}|g(x+s)-g(x)|\to0\) as \(\epsilon\to0\), and \(f_\epsilon\to h\) pointwise on \(\mathbb T\), including \(f_\epsilon(1)\to0=h(1)\). Apply (4.2) to \(f_\epsilon\) and let \(\epsilon\to0\), using Lemma 2.1(2) for the fixed unitaries \(U\) and \(UV\). \(\square\)

The smoothing approaches every angle from the right, so that the limit takes the value \(0\), not \(1\), at the cut. With the left-continuous choice \(h(1)=1\), the trace of the phase would not detect the identity.

For finite matrices, that is, for the trivial group \(A\), Lemma 4.1 also follows from a theorem of R. C. Thompson: for Hermitian matrices \(X,Y\) there are unitaries \(V_1,V_2\) with \(e^{iX}e^{iY}=e^{i(V_1XV_1^*+V_2YV_2^*)}\); see [ALV, Section 2] for this formula and its extensions. Applied to \(X=2\pi h(U)\) and \(Y=2\pi h(V)\), it writes \(UV=e^{2\pi iC}\) with \(C\ge0\) and \(\operatorname{Tr}C=\ell(U)+\ell(V)\), and \(h(e^{2\pi iC})\le C\) gives the inequality. The proof above needs no approximation of \(A\) by matrices, and this is what makes it work for every group.

## 5. Exercises

**5.1** (easy). Let \(A\) be finite. Show that \(\tau(T)=\frac1{|A|}\operatorname{Tr}(T)\) for \(T\in\mathcal M\), where \(\operatorname{Tr}\) is the trace of operators on the finite-dimensional space \(\ell^2(A)\).

**5.2** (easy). Show that \(\tau(L(a))=0\) for \(a\ne1\), and that \(\tau_b\) of a matrix whose diagonal entries are left translations by elements other than \(1\) is zero.

**5.3** (medium). Let \(a\in A\). Show that \(\ell(L(a))=\frac{m-1}{2m}\) if \(a\) has finite order \(m\), and \(\ell(L(a))=\frac12\) if \(a\) has infinite order. (Compute \(\langle L(a)^n\delta_1,\delta_1\rangle\) and identify the measure \(\mu_{\delta_1}\) of \(L(a)\).)

**5.4** (easy). Let \(P\) be the spectral projection \(1_{\{1\}}(U)\) of a unitary \(U\in M_b(\mathcal M)\). Show that \(h(\bar z)=1-h(z)\) for \(z\ne1\), and deduce \(\ell(U^*)=\tau_b(I-P)-\ell(U)\).

**5.5** (easy). Find scalar \(1\times1\) unitaries \(U,V\) with \(\ell(UV)=\ell(U)+\ell(V)\), and others with \(\ell(UV)<\ell(U)+\ell(V)\).

**5.6** (medium). Show that \(\ell(U)+\ell(V)\le b+\ell(VU)\) for all unitaries \(U,V\in M_b(\mathcal M)\). (Write \(V=(VU)U^*\) and use Lemma 4.1 and Exercise 5.4.)

## 6. Solutions

**5.1.** By Lemma 1.1,
\[
\begin{aligned}
\operatorname{Tr}T&=\sum_x\langle T\delta_x,\delta_x\rangle=\sum_xt_{xx^{-1}}\\
&=|A|\,t_1=|A|\,\tau(T).
\end{aligned}
\]

**5.2.** \(\tau(L(a))=\langle\delta_a,\delta_1\rangle=0\) for \(a\ne1\). The trace \(\tau_b\) only sees the diagonal entries.

**5.3.** \(\langle L(a)^n\delta_1,\delta_1\rangle=\langle\delta_{a^n},\delta_1\rangle\) is \(1\) if \(a^n=1\) and \(0\) otherwise. These are the integrals of \(z^n\) against \(\mu=\mu_{\delta_1}\). If \(a\) has infinite order, \(\int z^n\,d\mu=0\) for \(n\ne0\), the same as for the normalized arc length, and since trigonometric polynomials are dense in \(C(\mathbb T)\), \(\mu\) is the normalized arc length; then \(\ell(L(a))=\int h\,d\mu=\int_0^1x\,dx=\frac12\). If \(a\) has order \(m\), the moments are those of the uniform measure on the \(m\)-th roots of unity, so \(\ell(L(a))=\frac1m\sum_{j=0}^{m-1}\frac jm=\frac{m-1}{2m}\).

**5.4.** For \(z=e^{2\pi ix}\) with \(x\in(0,1)\), \(\bar z=e^{2\pi i(1-x)}\) and \(h(\bar z)=1-x\); and \(h(\bar1)=0\). So \(h\circ c=1_{\{z\ne1\}}-h\) on \(\mathbb T\). By Lemma 2.1(5), \(h(U^*)=(h\circ c)(U)=(I-P)-h(U)\). Take traces.

**5.5.** \(U=V=e^{2\pi i\cdot0.3}\): \(\ell(UV)=0.6=0.3+0.3\). \(U=V=e^{2\pi i\cdot0.6}\): \(UV=e^{2\pi i\cdot0.2}\), so \(\ell(UV)=0.2<1.2\).

**5.6.** By Lemma 4.1 and Exercise 5.4, with \(P=1_{\{1\}}(U)\),
\[
\begin{aligned}
\ell(V)&=\ell((VU)U^*)\le\ell(VU)+\ell(U^*)\\
&=\ell(VU)+\tau_b(I-P)-\ell(U)\\
&\le\ell(VU)+b-\ell(U).
\end{aligned}
\] For scalars the inequality is \(x+y\le1+(x+y-\lfloor x+y\rfloor)\) for \(x,y\in[0,1)\), with equality when \(x+y\ge1\).

## References

- [OpenAI-K] OpenAI, *The Kervaire theorem for groups*, OpenAI Math Release preprint, 24 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/The-Kervaire-Theorem-for-Groups-September-24-2026
- [ALV] J. Antezana, G. Larotonda and A. Varela, *Thompson-type formulae*, Journal of Functional Analysis 262 (2012), 1515–1528; arXiv:1107.0348, Section 2. https://arxiv.org/abs/1107.0348
- [Jones] V. F. R. Jones, *Von Neumann algebras*, lecture notes, 1 October 2009, Sections 3.3 and 3.4, on the author's page. https://math.berkeley.edu/~vfr/VonNeumann2009.pdf
