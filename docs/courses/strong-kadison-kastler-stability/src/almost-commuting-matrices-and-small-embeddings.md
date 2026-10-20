# Almost commuting matrices and small embeddings

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves Theorem 2.4 of [Close operator algebras](close-operator-algebras.md): one-sided gaps between von Neumann algebras can tend to \(0\) while every unitary implementing a spatial embedding stays a fixed distance from \(I\) [OpenAI-289c, Section 4]. The algebras are those of [A circle family and a near inclusion](a-circle-family-and-a-near-inclusion.md), built from Voiculescu's almost commuting clock and shift matrices \(U_n,V_n\). Three steps remain.

1. The commutator of \(U_n\) and \(V_n\) has norm \(\nu_n\to0\), but every commuting pair of unitaries is at total distance at least \(1-\nu_n/2\) from \((U_n,V_n)\) (Lemma 1.2). The proof is the winding-number argument of Exel and Loring [EL], in its trace-logarithm form [Exel, Lemma 3.1].
2. Two commuting von Neumann algebras that contain operators close to \(E_1\tilde R_1\) and \(E_2\tilde R_2\), for suitable projections \(E_i\) and unitaries \(\tilde R_i\), yield commuting unitaries close to \(\tilde R_1\) and \(\tilde R_2\) on the finite-dimensional range of \(E_1E_2\) (Lemma 2.2).
3. A unitary \(u\) close to \(I\) with \(uM_nu^*\subseteq N_n\) turns the conjugated left regular representation into a representation commuting with the right regular one. Weak limits along the free generators then recover \(U_n\) and \(V_n\) inside two commuting algebras, which steps 1 and 2 forbid (Theorem 3.1).

The argument gives the explicit value \(\varepsilon_0=1/20000\) in Theorem 2.4.

We use: [Close operator algebras](close-operator-algebras.md) (Definition 1.2 and Lemma 1.5(1)); [A circle family and a near inclusion](a-circle-family-and-a-near-inclusion.md) (Lemmas 2.1 and 3.1 and Proposition 3.2); and from the foundations course, [Corollary 9.7(a)](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies#OA-FND-LT-10) (the unit ball of \(B(H)\) is weakly compact), the [continuous functional calculus](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-07) (Theorem 5.1) and its [continuity](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-11) (Theorem 6.1).

## 1. The clock and shift matrices

**Lemma 1.1** (the winding number). For a unitary matrix \(C\) with \(\det C=1\) and without eigenvalue \(-1\), put
\[
\kappa(C)=\frac1{2\pi i}\operatorname{Tr}\log C,
\]
with the principal logarithm on the circle minus \(-1\). Then \(\kappa(C)\) is an integer. If \(s\mapsto C(s)\), \(0\le s\le1\), is a continuous path of unitary matrices with \(\det C(s)=1\) and \(\|C(s)-I\|<2\) for all \(s\), then \(\kappa(C(s))\) does not depend on \(s\).

**Proof.** Let \(e^{i\theta_1},\dots,e^{i\theta_n}\) be the eigenvalues of \(C\), with \(\theta_j\in(-\pi,\pi)\). Then \(\operatorname{Tr}\log C=i\sum_j\theta_j\) and \(e^{i\sum_j\theta_j}=\det C=1\), so \(\sum_j\theta_j\in2\pi\mathbb Z\) and \(\kappa(C)=\sum_j\theta_j/2\pi\) is an integer. For the path, \(c=\max_s\|C(s)-I\|<2\), and every spectrum \(\sigma(C(s))\) lies in the closed arc \(\Gamma=\{z\in\mathbb T:|z-1|\le c\}\), which does not contain \(-1\). The principal logarithm is continuous on \(\Gamma\), so by Theorem 6.1(1) of the foundations lesson on C\*-algebras, applied to the normal elements \(C(s)\) of the matrix algebra, \(s\mapsto\log C(s)\) is continuous. So \(\kappa(C(s))\) is a continuous integer-valued function on \([0,1]\), hence constant. \(\square\)

For \(n\ge3\) let \(\omega=e^{2\pi i/n}\), let \(e_0,\dots,e_{n-1}\) be the standard basis of \(\mathbb C^n\), with indices modulo \(n\), and define unitaries
\[
U_ne_j=\omega^je_j,\qquad V_ne_j=e_{j+1}.
\]

**Lemma 1.2** (Voiculescu's matrices). For \(n\ge3\), \(\nu_n=\|U_nV_n-V_nU_n\|=2\sin(\pi/n)\). Every pair of commuting unitaries \(\hat U,\hat V\) on \(\mathbb C^n\) satisfies
\[
\|\hat U-U_n\|+\|\hat V-V_n\|\ge1-\frac{\nu_n}2 .
\]

**Proof.** \(U_nV_ne_j=\omega^{j+1}e_{j+1}=\omega V_nU_ne_j\), so \(U_nV_n=\omega V_nU_n\) and \(\nu_n=|\omega-1|=2\sin(\pi/n)\). Write \(U=U_n\), \(V=V_n\), and suppose that \(\mu=\|\hat U-U\|+\|\hat V-V\|<1-\nu_n/2\). Since \(\|U^*\hat U-I\|=\|\hat U-U\|<2\), the unitary \(U^*\hat U\) has no eigenvalue \(-1\), so \(U^*\hat U=e^{iA}\) for a self-adjoint \(A\) with spectrum in \((-\pi,\pi)\); similarly \(V^*\hat V=e^{iB}\). The paths
\[
\begin{gathered}
U(s)=Ue^{isA},\\
V(s)=Ve^{isB}\\
(0\le s\le1)
\end{gathered}
\]
consist of unitaries and join \((U,V)\) to \((\hat U,\hat V)\). For \(|\theta|<\pi\) and \(0\le s\le1\),
\[
\begin{aligned}
|e^{is\theta}-1|&=2|\sin(s\theta/2)|\\
&\le2|\sin(\theta/2)|\\
&=|e^{i\theta}-1|,
\end{aligned}
\]
so \(\|U(s)-U\|\le\|e^{iA}-I\|=\|\hat U-U\|\), and likewise \(\|V(s)-V\|\le\|\hat V-V\|\). Let \(C(s)=U(s)V(s)U(s)^*V(s)^*\), a unitary with determinant \(1\). Then \(\|C(s)-I\|=\|U(s)V(s)-V(s)U(s)\|\), and replacing \(U(s),V(s)\) by \(U,V\) in both products changes this norm by at most \(2\|U(s)-U\|+2\|V(s)-V\|\). Hence
\[
\|C(s)-I\|\le\nu_n+2\mu<2 .
\]
By Lemma 1.1, \(\kappa(C(0))=\kappa(C(1))\). But \(C(0)=UVU^*V^*=\omega I\), whose principal logarithm is \((2\pi i/n)I\) because \(0<2\pi/n<\pi\); so \(\kappa(C(0))=1\). And \(C(1)=\hat U\hat V\hat U^*\hat V^*=I\), so \(\kappa(C(1))=0\). This contradiction proves the bound. \(\square\)

So \(\nu_n\to0\) while the distance from \((U_n,V_n)\) to commuting pairs stays near \(1\). That almost commuting unitary matrices need not be close to commuting ones was found by Voiculescu; the integer \(\kappa\) is the obstruction that survives small perturbations.

## 2. A finite-dimensional corner

Commuting operators need not have commuting compressions to a subspace. The next lemma moves the subspace slightly, so that compression preserves commutation.

**Lemma 2.1** (polar parts). Let \(R\) be a unitary and \(C\) an operator on a Hilbert space with \(\eta=\|C-R\|\le1/5\). Then \(C\) is invertible, \(C_u=C(C^*C)^{-1/2}\) is a unitary with \(\|C_u-R\|\le5\eta\), and \(C_u\) is a norm limit of polynomials in \(C\) and \(C^*\). On a finite-dimensional space, \(C_u=C\,p(C^*C)\) for a polynomial \(p\).

**Proof.** \(C=R\bigl(I+R^*(C-R)\bigr)\) is invertible because \(\|R^*(C-R)\|<1\). From \(C^*C-I=C^*(C-R)+(C-R)^*R\), \(\|C^*C-I\|\le(1+\eta)\eta+\eta\le3\eta\le3/5\), so the spectrum of \(C^*C\) lies in \([1-3\eta,1+3\eta]\). By the continuous functional calculus, \((C^*C)^{-1/2}\) is a norm limit of polynomials in \(C^*C\), and
\[
\begin{aligned}
&\|(C^*C)^{-1/2}-I\|\\
&\quad \le\max_{|\mu-1|\le3\eta}|\mu^{-1/2}-1|\le3\eta,
\end{aligned}
\]
because \((1-x)^{-1/2}\le1+x\) for \(0\le x\le3/5\) (equivalently \(x+x^2\le1\)), and \(1-(1+x)^{-1/2}\le x/2\). Then \(C_u^*C_u=I\) and \(C_u\) is invertible, so it is unitary, and
\[
\begin{aligned}
\|C_u-R\|&\le\|C\|\,\|(C^*C)^{-1/2}\\
&\quad -I\|+\|C-R\|\\
&\le(1+\eta)3\eta+\eta\\
&\le5\eta .
\end{aligned}
\]
In finite dimension, any function of the self-adjoint matrix \(C^*C\) agrees with a polynomial that interpolates it on the finite spectrum. \(\square\)

**Lemma 2.2** (a commuting corner). Let \(E_1,E_2\) be commuting projections on a Hilbert space \(H\) such that \(E=E_1E_2\) has nonzero finite-dimensional range \(\mathcal D\). Let \(\tilde R_1,\tilde R_2\) be unitaries commuting with \(E_1\) and \(E_2\), and let \(R_i\) be the restriction of \(\tilde R_i\) to \(\mathcal D\). Let \(\mathcal A_1,\mathcal A_2\subseteq B(H)\) be von Neumann algebras such that every element of \(\mathcal A_1\) commutes with every element of \(\mathcal A_2\). Suppose \(T_i\in\mathcal A_i\) and
\[
\begin{gathered}
\delta_i=\|T_i-E_i\tilde R_i\|,\\
\delta=\delta_1+\delta_2\le\frac1{400}.
\end{gathered}
\]
Then there are commuting unitaries \(\hat R_1,\hat R_2\) on \(\mathcal D\) with \(\|\hat R_i-R_i\|\le305\,\delta\).

**Proof.** *Projections in the algebras.* Since \(\tilde R_i\) commutes with \(E_i\), \((E_i\tilde R_i)^*(E_i\tilde R_i)=E_i\), so
\[
\begin{aligned}
d_i&=\|T_i^*T_i-E_i\|\\
&\le(1+\delta_i)\delta_i+\delta_i\le3\delta_i .
\end{aligned}
\]
If a real number \(\lambda\) has distance more than \(d_i\) from \(\{0,1\}\), then \(\lambda-E_i\) is invertible with \(\|(\lambda-E_i)^{-1}\|<1/d_i\), so \(Z=(\lambda-E_i)^{-1}(T_i^*T_i-E_i)\) has norm less than \(1\) and \(\lambda-T_i^*T_i=(\lambda-E_i)(I-Z)\) is invertible. Hence \(\sigma(T_i^*T_i)\subseteq[-d_i,d_i]\cup[1-d_i,1+d_i]\), and \(d_i<1/4\). Let \(\varphi\) be continuous, \(0\) on \((-\infty,1/4]\), \(1\) on \([3/4,\infty)\), and linear in between. Then \(Q_i=\varphi(T_i^*T_i)\) is a projection in \(\mathcal A_i\), since \(\varphi^2=\varphi\) on the spectrum and \(Q_i\) is a norm limit of polynomials in \(T_i^*T_i\in\mathcal A_i\). As \(|\varphi(\lambda)-\lambda|\le d_i\) on the spectrum, \(\|Q_i-T_i^*T_i\|\le d_i\) and \(\|Q_i-E_i\|\le2d_i\le6\delta_i\).

*A nearby corner.* \(Q_1\) and \(Q_2\) commute, so \(P=Q_1Q_2\) is a projection, and
\[
\begin{aligned}
\|P-E\|&\le\|Q_1-E_1\|+\|Q_2-E_2\|\\
&\le6\delta .
\end{aligned}
\]
Let \(S=PE+(I-P)(I-E)\)\(=I+(P-E)(2E-I)\). Since \(2E-I\) is unitary, \(\|S-I\|\le6\delta\le1/5\). Also \(SE=PE=PS\), and \(S^*S=EPE+(I-E)(I-P)(I-E)\) commutes with \(E\). Lemma 2.1 with \(R=I\) makes \(J=S(S^*S)^{-1/2}\) a unitary with \(\|J-I\|\le30\delta\). The factor \((S^*S)^{-1/2}\) is a norm limit of polynomials in \(S^*S\), so it commutes with \(E\), and
\[
\begin{aligned}
JE&=SE(S^*S)^{-1/2}\\
&=PS(S^*S)^{-1/2}=PJ .
\end{aligned}
\]
So \(J\) maps \(\mathcal D\) onto the range of \(P\), and \(EJ^*=J^*P\).

*Commuting compressions.* Put \(A=Q_1T_1Q_1\in\mathcal A_1\) and \(B=Q_2T_2Q_2\in\mathcal A_2\). Since \(Q_2\) commutes with \(T_1\) and \(Q_1\), \(PT_1P=Q_2AQ_2=AQ_2\); likewise \(PT_2P=Q_1B\). Using \(AQ_1=Q_1A=A\), \(BQ_2=Q_2B=B\) and \(AB=BA\),
\[
\begin{gathered}
(AQ_2)(Q_1B)=AQ_1Q_2B=AB,\\
(Q_1B)(AQ_2)=Q_1ABQ_2=AB .
\end{gathered}
\]
So \(PT_1P\) and \(PT_2P\) commute; the same computation with \(A^*\) or \(B^*\) shows that each commutes with the adjoint of the other.

*Transport to \(\mathcal D\).* Let \(C_i\) be the restriction to \(\mathcal D\) of \(J^*PT_iPJ=EJ^*T_iJE\). Conjugation by the unitary \(J\) from \(\mathcal D\) onto the range of \(P\) carries the relations of the previous step to \(C_1,C_2\): they commute, and each commutes with the adjoint of the other. Since \(EE_i=E\), the restriction \(R_i\) of \(\tilde R_i\) is also the restriction of \(E(E_i\tilde R_i)E\). By Lemma 1.5(1) of [Close operator algebras](close-operator-algebras.md),
\[
\begin{aligned}
\|C_i-R_i\|&\le\|J^*T_iJ-E_i\tilde R_i\|\\
&\le\delta_i+2\|J-I\|\\
&\le61\delta\le\frac15 .
\end{aligned}
\]
*Polar parts.* Lemma 2.1 on \(\mathcal D\) gives unitaries \(\hat R_i=C_i\,p_i(C_i^*C_i)\) with \(\|\hat R_i-R_i\|\le5\cdot61\delta=305\delta\). Since \(C_1\) and \(C_1^*\) commute with \(C_2\) and \(C_2^*\), \(\hat R_1\) commutes with \(\hat R_2\). \(\square\)

## 3. Proof of Theorem 2.4

For \(n\ge6\), apply the construction of [A circle family and a near inclusion](a-circle-family-and-a-near-inclusion.md) with \(t=1/2\), \(d=n\), \(U=U_n\) and \(V=V_n\). Write \(L_n=K\otimes K\otimes\mathbb C^n\), \(H_n=S\otimes L_n\), and \(a_n,b_n,f_n,W_n,M_n,N_n\) for the resulting objects; all these Hilbert spaces are separable. Let \(C=61952\) be the constant of Proposition 3.2 there.

**Theorem 3.1.** For \(n\ge6\):

1. \(\gamma(M_n,N_n)\le C\nu_n\), and \(W_n^*M_nW_n\subseteq N_n\).
2. Every unitary \(u\) of \(H_n\) with \(uM_nu^*\subseteq N_n\) satisfies
\[
\|u-I\|\ge\frac1{9760}-\frac{C\nu_n}2 .
\]

In particular \(\gamma(M_n,N_n)\to0\), every \(M_n\) embeds spatially in \(N_n\), and once \(C\nu_n\le10^{-4}\), every implementing unitary has \(\|u-I\|\ge1/20000\). This proves Theorem 2.4 of [Close operator algebras](close-operator-algebras.md) with \(\varepsilon_0=1/20000\).

**Proof.** Part 1 is Lemma 3.1 and Proposition 3.2 of [A circle family and a near inclusion](a-circle-family-and-a-near-inclusion.md), with \(\nu=\nu_n\).

*A representation commuting with the right regular one.* Let \(u\) be a unitary with \(uM_nu^*\subseteq N_n\), put \(\eta=\|u-I\|\) and \(\beta=C\nu_n+2\eta\). For \(g\in G\) let \(Z(g)=W_n(\lambda(g)\otimes I)W_n^*\in M_n\) and
\[
\Sigma(g)=uZ(g)u^*\,(\rho(g)\otimes I).
\]
Since \(uZ(g)u^*\in N_n\) commutes with every \(\rho(h)\otimes I\), and \(Z\) and \(\rho\otimes I\) are representations, \(\Sigma\) is a unitary representation of \(G\). By Lemma 1.5(1) of [Close operator algebras](close-operator-algebras.md) and Proposition 3.2 of [A circle family and a near inclusion](a-circle-family-and-a-near-inclusion.md), and since \(\lambda(g)\) commutes with \(\rho(g)\),
\[
\begin{aligned}
&\bigl\|\Sigma(g)-\lambda(g)\rho(g)\otimes f_n(g)\bigr\|\\
&\quad \le\|uZ(g)u^*-Z(g)\|+\|Z(g)\\
&\qquad -\lambda(g)\otimes f_n(g)\|\le\beta .
\end{aligned}
\]
Let \(\mathcal A_1\) and \(\mathcal A_2\) be the von Neumann algebras generated by the \(\Sigma(g,e)\) and by the \(\Sigma(e,g)\), \(g\in F\). These are self-adjoint sets of commuting operators, since \((g,e)\) and \((e,h)\) commute in \(G\); so every element of \(\mathcal A_1\) commutes with every element of \(\mathcal A_2\).

*The corner data.* Identify \(S=\ell^2(F\times F)\) with \(K\otimes K\) by \(\delta_{(x_1,x_2)}=\delta_{x_1}\otimes\delta_{x_2}\), so that
\[
H_n=K\otimes K\otimes K\otimes K\otimes\mathbb C^n .
\]
Let \(E_1\) be \(p_e\) in the first and third factors and the identity in the others, and \(E_2\) be \(p_e\) in the second and fourth factors and the identity in the others. They commute, and \(E=E_1E_2\) has range \(\mathcal D=\delta_e\otimes\delta_e\otimes\delta_e\otimes\delta_e\otimes\mathbb C^n\), identified with \(\mathbb C^n\). Let \(\tilde R_1\) and \(\tilde R_2\) act as \(U_n\), respectively \(V_n\), on the last factor and as the identity on the others; they commute with \(E_1\) and \(E_2\), and their restrictions to \(\mathcal D\) are \(U_n\) and \(V_n\).

*Weak limits along the generators.* Let \(g_{1j}=(s_j,e)\) and \(g_{2j}=(e,s_j)\). The operator \(\lambda_F(s_j)\rho_F(s_j)\) sends \(\delta_x\) to \(\delta_{s_jxs_j^{-1}}\). It fixes \(\delta_e\); for \(x\ne e\) and all \(j\) such that \(s_j^{\pm1}\) does not occur in \(x\), the word \(s_jxs_j^{-1}\) is reduced and begins with \(s_j\), so for fixed \(y\) it differs from \(y\) when \(j\) is large. Hence \(\lambda_F(s_j)\rho_F(s_j)\to p_e\) weakly. In the identification above, \(\lambda(g_{1j})\rho(g_{1j})=\lambda_F(s_j)\rho_F(s_j)\otimes I\), and \(f_n(g_{1j})=a_n(s_j)\to\frac12p_e\otimes I\otimes U_n\) weakly by Lemma 2.1 of [A circle family and a near inclusion](a-circle-family-and-a-near-inclusion.md). Weakly convergent bounded sequences acting in separate tensor factors have weakly convergent tensor products (check the matrix entries between elementary tensors), so
\[
\lambda(g_{ij})\rho(g_{ij})\otimes f_n(g_{ij})\longrightarrow\tfrac12E_i\tilde R_i
\]
weakly as \(j\to\infty\), for \(i=1\) and similarly for \(i=2\).

By weak compactness of the unit ball, the sequence \(\Sigma(g_{ij})\), \(j\ge1\), has a weak cluster point \(B_i\), which lies in the weakly closed algebra \(\mathcal A_i\). Along a subnet converging to \(B_i\), the differences \(\Sigma(g_{ij})-\lambda(g_{ij})\rho(g_{ij})\otimes f_n(g_{ij})\) converge weakly to \(B_i-\frac12E_i\tilde R_i\); they lie in the ball of radius \(\beta\), which is weakly closed. Hence \(\|B_i-\frac12E_i\tilde R_i\|\le\beta\), and \(T_i=2B_i\in\mathcal A_i\) satisfies \(\|T_i-E_i\tilde R_i\|\le2\beta\).

*The contradiction.* Let \(\delta=\|T_1-E_1\tilde R_1\|+\|T_2-E_2\tilde R_2\|\le4\beta\). If \(\delta>1/400\), then certainly \(\delta\ge1/1220\). If \(\delta\le1/400\), Lemma 2.2 gives commuting unitaries \(\hat R_1,\hat R_2\) on \(\mathbb C^n\) with
\[
\|\hat R_1-U_n\|+\|\hat R_2-V_n\|\le610\,\delta .
\]
For \(n\ge6\), \(\nu_n\le2\sin(\pi/6)=1\), so Lemma 1.2 bounds the left side below by \(1/2\), and again \(\delta\ge1/1220\). In both cases \(\beta\ge\delta/4\ge1/4880\), and
\[
\|u-I\|=\frac{\beta-C\nu_n}2\ge\frac1{9760}-\frac{C\nu_n}2 .
\]
Finally, if \(C\nu_n\le10^{-4}\), the right side is at least \(1/9760-1/20000>1/20000\). \(\square\)

Christensen's theorem implements small near inclusions of injective algebras by unitaries close to \(I\) (Theorem 3.1 of [Averaging and the completely positive criterion](averaging-and-the-completely-positive-criterion.md)). Theorem 3.1 shows that this one-sided statement fails without injectivity (Exercise 4.4), while Theorem 2.1 of [Close operator algebras](close-operator-algebras.md) shows that it holds without injectivity when the near inclusion goes both ways.

## 4. Exercises

**Exercise 4.1.** Show that \(\nu_n=2\sin(\pi/n)\le1\) for \(n\ge6\), and that \(C\nu_n\le10^{-4}\) once \(n\ge4\cdot10^9\).

**Exercise 4.2.** For \(1\le m<n/2\), show that \(U_n^mV_nU_n^{-m}V_n^*=\omega^mI\) and \(\kappa(\omega^mI)=m\). Deduce that every commuting pair \(\hat U,\hat V\) satisfies \(\|\hat U-U_n^m\|+\|\hat V-V_n\|\)\(\ge1-|\omega^m-1|/2\).

**Exercise 4.3.** Let \(n=2\), so \(U_2=\operatorname{diag}(1,-1)\) and \(V_2\) exchanges \(e_0\) and \(e_1\). Compute \(U_2V_2U_2^*V_2^*\) and \(\|U_2V_2-V_2U_2\|\), and explain why Lemma 1.1 does not apply.

**Exercise 4.4.** Use Christensen's theorem (Theorem 3.1 of [Averaging and the completely positive criterion](averaging-and-the-completely-positive-criterion.md)) and Theorem 3.1 to show that \(M_n\) is not injective for all large \(n\).

**Exercise 4.5.** Show that \(\gamma(N_n,M_n)\ge1\) for every \(n\). (Compare the diagonal blocks of \(W_n^*(I\otimes Y)W_n\), for a self-adjoint unitary \(Y\ne\pm I\) on \(L_n\), with those of the operators \(X\otimes I\), \(X\in\lambda(G)''\).)

## 5. Solutions

**Solution 4.1.** \(\sin\) is increasing on \([0,\pi/2]\) and \(\pi/n\le\pi/6\), so \(\nu_n\le2\sin(\pi/6)=1\). Also \(\nu_n\le2\pi/n\), so \(C\nu_n\le2\pi\cdot61952/n\le10^{-4}\) when \(n\ge4\cdot10^9\).

**Solution 4.2.** \(U_n^mV_ne_j=\omega^{m(j+1)}e_{j+1}=\omega^mV_nU_n^me_j\), so \(U_n^mV_nU_n^{-m}V_n^*=\omega^mI\). Since \(0<2\pi m/n<\pi\), the principal logarithm of \(\omega^mI\) is \((2\pi im/n)I\), with trace \(2\pi im\). The proof of Lemma 1.2 applies verbatim to the pair \((U_n^m,V_n)\), whose commutator has norm \(|\omega^m-1|\), and with \(\kappa=m\ne0\) at the starting point.

**Solution 4.3.** \(V_2U_2V_2^*=\operatorname{diag}(-1,1)=-U_2\), so \(U_2V_2=-V_2U_2\), \(U_2V_2U_2^*V_2^*=-I\) and \(\|U_2V_2-V_2U_2\|=\|2U_2V_2\|=2\). The matrix \(-I\) has the eigenvalue \(-1\), where the principal logarithm is not defined, so \(\kappa\) is not defined at the starting point.

**Solution 4.4.** Suppose \(M_n\) is injective for infinitely many \(n\). For those \(n\) with \(C\nu_n<1/200\), take \(\gamma=2C\nu_n\), so \(\gamma(M_n,N_n)\le C\nu_n<\gamma<1/100\) and \(M_n\subset_\gamma N_n\). Christensen's theorem gives a unitary \(u\) with \(uM_nu^*\subseteq N_n\) and \(\|u-I\|\le150\gamma=300C\nu_n\), which tends to \(0\). This contradicts Theorem 3.1(2), which bounds \(\|u-I\|\) below by \(1/20000\) for large \(n\).

**Solution 4.5.** \(N_n\) contains \(I\otimes Y\) for every \(Y\in B(L_n)\). Every operator of \(M_n\) has the form \(W_n(X\otimes I)W_n^*\) with \(X\in\lambda(G)''\), and
\[
\begin{aligned}
&\|I\otimes Y-W_n(X\otimes I)W_n^*\|\\
&\quad =\|W_n^*(I\otimes Y)W_n-X\otimes I\|.
\end{aligned}
\]
Here \(W_n^*(I\otimes Y)W_n\) is block diagonal with blocks \(f_n(x)^*Yf_n(x)\), while the diagonal blocks of \(X\otimes I\) are \(X_{x,x}I=X_{e,e}I\), by right invariance of the matrix of \(X\). The norm of an operator is at least that of each diagonal block, so the distance is at least the distance from the unitary conjugate \(f_n(e)^*Yf_n(e)=Y\) to \(\mathbb CI\). For a self-adjoint unitary \(Y\ne\pm I\) with eigenvalues \(1\) and \(-1\), \(\|Y-cI\|\ge\max(|1-c|,|1+c|)\ge1\) for every \(c\in\mathbb C\). So the contraction \(I\otimes Y\) of \(N_n\) has distance at least \(1\) from \(M_n\).

## References

- [OpenAI-289c] OpenAI, Near inclusions of von Neumann algebras without small spatial embeddings, preprint, 5 October 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Near-Inclusions-of-von-Neumann-Algebras-Without-Small-Spatial-Embeddings-October-5-2026
- [EL] R. Exel, T. A. Loring, Almost commuting unitary matrices, Proceedings of the American Mathematical Society 106 (1989), 913–915. https://doi.org/10.1090/S0002-9939-1989-0975641-9
- [Exel] R. Exel, The soft torus and applications to almost commuting matrices, Pacific Journal of Mathematics 160 (1993), 207–217. https://msp.org/pjm/1993/160-2/p02.xhtml
