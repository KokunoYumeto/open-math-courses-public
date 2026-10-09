# Completely bounded homomorphisms and similarity

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Kadison asked in 1955 whether every bounded unital homomorphism \(\pi\) of a unital C\*-algebra \(A\) into \(B(H)\) is similar to a \(*\)-homomorphism: whether some invertible \(S\in B(H)\) makes \(S\pi(\cdot)S^{-1}\) preserve adjoints. This course proves that the answer is yes, following OpenAI's solution [OpenAI-288]. The present lesson sets up the framework. Matrix amplifications measure how far a homomorphism is from a \(*\)-homomorphism. Paulsen's theorem says that \(\pi\) is similar to a \(*\)-homomorphism exactly when it is completely bounded, and that the smallest condition number \(\|S\|\|S^{-1}\|\) of a similarity equals the completely bounded norm. Applied to upper triangular homomorphisms, the same theorem shows that a derivation is implemented by an operator as soon as it is completely bounded, by an operator of norm at most half its completely bounded norm. For inner derivations this is Arveson's distance formula.

We use Theorem 4.1 of [Completely bounded extension and factorization](course:OA-APPROX/completely-bounded-extension#theorem-4-1), which factors a completely bounded map on a C\*-algebra through a representation; and, from [C\*-algebras, continuous functional calculus, automatic continuity and positive cones](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-14), Theorem 4.2 (\(*\)-homomorphisms are contractive), [Proposition 7.3](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-10) (every element of a unital C\*-algebra is a combination of four unitaries) and [Corollary 15.4](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-26) (the range of a \(*\)-homomorphism is closed and the induced map on the quotient is isometric).

## 1. Matrix amplifications

All Hilbert spaces and algebras are complex, and inner products are linear in the first variable. Throughout, \(A\) is a unital C\*-algebra. A *homomorphism* is a complex linear multiplicative map; it is not assumed to preserve adjoints. A *representation* of \(A\) on a Hilbert space \(K\) is a unital \(*\)-homomorphism \(\sigma:A\to B(K)\).

For integers \(p,q\ge1\), \(M_{p,q}(A)\) is the space of \(p\times q\) matrices over \(A\), and \(M_n(A)=M_{n,n}(A)\). The algebra \(M_n(A)\) is a C\*-algebra, and \(M_{p,q}(A)\) carries the norm of the corner of \(M_n(A)\), \(n=\max(p,q)\), into which it embeds by adding zero rows or columns. Thus \(\|x\|^2=\|x^*x\|=\|xx^*\|\) for \(x\in M_{p,q}(A)\), where \(x^*\in M_{q,p}(A)\). In particular, for a row \(x=(x_1,\dots,x_h)\) and a column \(y=(y_1,\dots,y_h)^{T}\),
\[
\|x\|=\Big\|\sum_jx_jx_j^*\Big\|^{1/2},\qquad \|y\|=\Big\|\sum_jy_j^*y_j\Big\|^{1/2}.
\tag{1.1}
\]

Let \(K,F\) be Hilbert spaces and \(u:A\to B(K,F)\) linear. Its amplification \(u_{p,q}:M_{p,q}(A)\to B(K^q,F^p)\) applies \(u\) to every entry, and \(u_n=u_{n,n}\). Put
\[
\|u\|_{\rm cb}=\sup_n\|u_n\|,\qquad \|u\|_{\rm row}=\sup_h\|u_{1,h}\|,\qquad \|u\|_{\rm col}=\sup_h\|u_{h,1}\|,
\tag{1.2}
\]
with values in \([0,\infty]\). The map \(u\) is *completely bounded* if \(\|u\|_{\rm cb}<\infty\). Since \(u_{p,q}(x)\) is a corner of \(u_n\) applied to the padded matrix, \(\|u_{p,q}\|\le\|u_n\|\) for \(n\ge p,q\); in particular \(\|u\|_{\rm row},\|u\|_{\rm col}\le\|u\|_{\rm cb}\). For an operator \(T\), \(T^{(n)}\) denotes the diagonal operator with \(n\) copies of \(T\).

**Lemma 1.1.** Let \(\pi:A\to B(H)\) be a homomorphism and \(\sigma:A\to B(K)\) a representation.

1. \(\pi_{p,q}(xy)=\pi_{p,r}(x)\pi_{r,q}(y)\) for \(x\in M_{p,r}(A)\) and \(y\in M_{r,q}(A)\).
2. Each \(\sigma_n\) is a \(*\)-homomorphism of \(M_n(A)\) into \(B(K^n)\). Hence \(\|\sigma_{p,q}(x)\|\le\|x\|\) for all \(p,q\), and \(\|\sigma\|_{\rm cb}\le1\).
3. If \(\pi(a)=T^{-1}\sigma(a)T\) for an invertible \(T\in B(H,K)\), then \(\|\pi\|_{\rm cb}\le\|T\|\|T^{-1}\|\).

**Proof.** (1) The \((i,j)\) entry of both sides is \(\sum_k\pi(x_{ik})\pi(y_{kj})=\pi\big(\sum_kx_{ik}y_{kj}\big)\). (2) By (1), \(\sigma_n\) is multiplicative; it preserves adjoints entrywise, so it is contractive by Theorem 4.2 of the C\*-algebra lesson. Rectangular matrices are corners of square ones. (3) \(\pi_n(x)=(T^{-1})^{(n)}\sigma_n(x)T^{(n)}\), and \(\|T^{(n)}\|=\|T\|\). \(\square\)

## 2. Contractive homomorphisms and similar representations

**Lemma 2.1.** A unital homomorphism \(\pi:A\to B(H)\) with \(\|\pi\|\le1\) is a \(*\)-homomorphism.

**Proof.** Let \(u\in A\) be unitary. Then \(\pi(u)\pi(u^*)=\pi(u^*)\pi(u)=\pi(1)=1\), so \(\pi(u)\) is invertible with inverse \(\pi(u^*)\). For \(\xi\in H\), \(\|\xi\|=\|\pi(u^*)\pi(u)\xi\|\le\|\pi(u)\xi\|\le\|\xi\|\), so \(\pi(u)\) is an invertible isometry, that is, a unitary, and \(\pi(u)^*=\pi(u)^{-1}=\pi(u^*)\). By Proposition 7.3 of the C\*-algebra lesson every \(a\in A\) is a combination \(\sum_jc_ju_j\) of unitaries; then \(\pi(a^*)=\sum_j\bar c_j\pi(u_j^*)=\big(\sum_jc_j\pi(u_j)\big)^*=\pi(a)^*\). \(\square\)

**Lemma 2.2** (unitary absorption). Let \(\sigma:A\to B(K)\) and \(\rho:A\to B(H)\) be representations and \(V:K\to H\) a bounded invertible operator with \(\rho(a)V=V\sigma(a)\) for all \(a\in A\). Then \(|V|=(V^*V)^{1/2}\) commutes with \(\sigma(A)\), \(W=V|V|^{-1}\) is a unitary of \(K\) onto \(H\), and \(\rho(a)=W\sigma(a)W^*\) for all \(a\).

**Proof.** Apply the identity to \(a^*\) and take adjoints: \(V^*\rho(a)=\sigma(a)V^*\). Hence \(V^*V\sigma(a)=V^*\rho(a)V=\sigma(a)V^*V\). Since \(V\) is invertible, the spectrum of \(V^*V\) lies in \([\|V^{-1}\|^{-2},\|V\|^2]\), so \(|V|\) and \(|V|^{-1}\) are norm limits of polynomials in \(V^*V\) and commute with \(\sigma(A)\). Now \(W^*W=|V|^{-1}V^*V|V|^{-1}=1\) and \(W\) is invertible, so \(W\) is unitary, and \(\rho(a)=V\sigma(a)V^{-1}=W|V|\sigma(a)|V|^{-1}W^*=W\sigma(a)W^*\). \(\square\)

## 3. Paulsen's similarity theorem

**Theorem 3.1** (Paulsen). Let \(\pi:A\to B(H)\) be a unital homomorphism. Then \(\pi\) is completely bounded if and only if \(S\pi(\cdot)S^{-1}\) is a \(*\)-homomorphism for some invertible \(S\in B(H)\). Every such \(S\) satisfies \(\|S\|\|S^{-1}\|\ge\|\pi\|_{\rm cb}\), and if \(\pi\) is completely bounded, \(S\) can be chosen positive with \(\|S\|\|S^{-1}\|=\|\pi\|_{\rm cb}\).

**Proof.** If \(S\pi(\cdot)S^{-1}=\rho\) is a \(*\)-homomorphism, then \(\pi(a)=S^{-1}\rho(a)S\), and Lemma 1.1(3) gives \(\|\pi\|_{\rm cb}\le\|S\|\|S^{-1}\|\).

Conversely let \(\pi\) be completely bounded; we may assume \(H\ne0\). Theorem 4.1 of the factorization lesson, applied with \(V=A\), gives a \(*\)-representation \(\Pi:A\to B(K)\), possibly degenerate, and operators \(V_1,V_2:H\to K\) with
\[
\pi(a)=V_1^*\Pi(a)V_2\quad(a\in A),\qquad \|V_1\|\|V_2\|=\|\pi\|_{\rm cb}.
\]
The operator \(e=\Pi(1)\) is a projection with \(\Pi(a)=e\Pi(a)e\). Replacing \(K\) by \(eK\), \(\Pi\) by its restriction to \(eK\) and \(V_i\) by \(eV_i\), we keep the factorization, do not increase \(\|V_1\|\|V_2\|\), and obtain a unital \(\Pi\).

Let \(K_0\) be the closed linear span of the vectors \(\Pi(a)V_2\xi\) (\(a\in A\), \(\xi\in H\)), and
\[
N=\{k\in K_0:\ V_1^*\Pi(b)k=0\ \text{for all }b\in A\}.
\]
Both subspaces are closed and invariant under \(\Pi(A)\): for \(N\), because \(V_1^*\Pi(b)\Pi(c)k=V_1^*\Pi(bc)k\). Invariant subspaces of a \(*\)-representation reduce it, so \(L=K_0\ominus N\) reduces \(\Pi\), and \(\rho(a)=\Pi(a)|_L\) is a representation of \(A\) on \(L\). Write \(P\) for the projection onto \(L\); it commutes with \(\Pi(A)\).

*Claim.* For \(a\in A\) and \(\xi\in H\), \(\Pi(a)V_2\xi-V_2\pi(a)\xi\in N\). Both terms lie in \(K_0\), since \(V_2\xi=\Pi(1)V_2\xi\). For \(b\in A\), \(V_1^*\Pi(b)\big(\Pi(a)V_2\xi-V_2\pi(a)\xi\big)=\pi(ba)\xi-\pi(b)\pi(a)\xi=0\).

Define \(S_0:H\to L\) by \(S_0\xi=PV_2\xi\); then \(\|S_0\|\le\|V_2\|\). By the claim, since \(P\) kills \(N\) and commutes with \(\Pi(a)\),
\[
\rho(a)S_0\xi=P\Pi(a)V_2\xi=PV_2\pi(a)\xi=S_0\pi(a)\xi .
\tag{3.1}
\]
Taking \(b=1\) in the definition of \(N\) shows that \(V_1^*\) vanishes on \(N\). As \(V_2\xi\in K_0=L\oplus N\), we get \(\xi=\pi(1)\xi=V_1^*V_2\xi=V_1^*S_0\xi\), so \(\|\xi\|\le\|V_1\|\|S_0\xi\|\): \(S_0\) is injective with closed range. By the claim, \(P\Pi(a)V_2\xi=S_0\pi(a)\xi\) lies in the range of \(S_0\); these vectors span a dense subspace of \(PK_0=L\). Hence \(S_0\) is a bounded bijection of \(H\) onto \(L\), with \(\|S_0^{-1}\|\le\|V_1\|\).

Let \(S=|S_0|\in B(H)\), positive and invertible, and \(U=S_0S^{-1}\), a unitary of \(H\) onto \(L\) (as in Lemma 2.2). By (3.1),
\[
S\pi(a)S^{-1}=U^*S_0\pi(a)S_0^{-1}U=U^*\rho(a)U,
\]
a \(*\)-homomorphism, and \(\|S\|\|S^{-1}\|=\|S_0\|\|S_0^{-1}\|\le\|V_1\|\|V_2\|\le\|\pi\|_{\rm cb}\). With the first paragraph, equality holds. \(\square\)

In particular a unital homomorphism with \(\|\pi\|_{\rm cb}=1\) is a \(*\)-homomorphism, since then \(\|S\|\|S^{-1}\|=1\) forces \(S\) to be a positive scalar.

## 4. Rectangular derivations

**Definition 4.1.** Let \(\sigma:A\to B(K)\) and \(\lambda:A\to B(F)\) be representations. A *rectangular derivation* for \(\sigma,\lambda\) is a linear map \(\Delta:A\to B(K,F)\) with
\[
\Delta(ab)=\Delta(a)\sigma(b)+\lambda(a)\Delta(b)\qquad(a,b\in A).
\tag{4.1}
\]
It is *implemented* by \(V\in B(K,F)\) if
\[
\Delta(a)=V\sigma(a)-\lambda(a)V\qquad(a\in A).
\tag{4.2}
\]
When \(F=K\) and \(\lambda=\sigma\), \(\Delta\) is a *\(\sigma\)-derivation*. For a C\*-algebra \(A\subseteq B(H)\) with \(1_H\in A\) and \(x\in B(H)\), the map \(\operatorname{ad}(x)|_A(a)=xa-ax\) is the derivation implemented by \(x\) for the inclusion representation.

Putting \(a=b=1\) in (4.1) gives \(\Delta(1)=0\). Every \(V\) defines through (4.2) a rectangular derivation, and \(\Delta_n(x)=V^{(n)}\sigma_n(x)-\lambda_n(x)V^{(n)}\) shows \(\|\Delta\|_{\rm cb}\le2\|V\|\). For \(s\ge0\) put
\[
\beta(s)=\left\|\begin{pmatrix}1&s\\0&1\end{pmatrix}\right\|=\frac{s+\sqrt{s^2+4}}2\le1+s .
\tag{4.3}
\]
The value follows from the characteristic polynomial \(\mu^2-(2+s^2)\mu+1\) of \(\left(\begin{smallmatrix}1&s\\0&1\end{smallmatrix}\right)^{T}\left(\begin{smallmatrix}1&s\\0&1\end{smallmatrix}\right)=\left(\begin{smallmatrix}1&s\\s&1+s^2\end{smallmatrix}\right)\), whose larger root is \(\beta(s)^2\); the inequality is \(\sqrt{s^2+4}\le s+2\).

**Lemma 4.2** (triangular homomorphisms). Let \(\Delta\) be a rectangular derivation for \(\sigma,\lambda\), and \(c>0\). Then
\[
\Phi_c(a)=\begin{pmatrix}\lambda(a)&c\Delta(a)\\0&\sigma(a)\end{pmatrix}\in B(F\oplus K)
\]
is a unital homomorphism. After reordering \((F\oplus K)^q\) as \(F^q\oplus K^q\), the amplification \((\Phi_c)_{p,q}(x)\) has diagonal blocks \(\lambda_{p,q}(x)\), \(\sigma_{p,q}(x)\), lower left block \(0\), and upper right block \(c\Delta_{p,q}(x):K^q\to F^p\). Consequently \(\|\Phi_c\|\le\beta(c\|\Delta\|)\) and \(\|\Phi_c\|_{\rm cb}\le\beta(c\|\Delta\|_{\rm cb})\).

**Proof.** Multiplicativity is (4.1), and \(\Phi_c(1)=1\) because \(\Delta(1)=0\). The block description is the entrywise definition. For an operator \(T=\left(\begin{smallmatrix}X&Y\\0&Z\end{smallmatrix}\right)\) with \(\|X\|,\|Z\|\le1\) and \(\|Y\|\le s\),
\[
\|T(\xi,\eta)\|^2\le(\|\xi\|+s\|\eta\|)^2+\|\eta\|^2=\left\|\begin{pmatrix}1&s\\0&1\end{pmatrix}\begin{pmatrix}\|\xi\|\\\|\eta\|\end{pmatrix}\right\|^2\le\beta(s)^2\big(\|\xi\|^2+\|\eta\|^2\big).
\]
Apply this to \(x\) in the unit ball of \(M_n(A)\), with \(X=\lambda_n(x)\), \(Z=\sigma_n(x)\) (contractions by Lemma 1.1(2)) and \(Y=c\Delta_n(x)\). \(\square\)

**Theorem 4.3** (implementation). Let \(\Delta\) be a completely bounded rectangular derivation for \(\sigma,\lambda\). Then \(\Delta\) is implemented by some \(V\in B(K,F)\) with \(\|V\|\le\frac12\|\Delta\|_{\rm cb}\).

**Proof.** For \(\Delta=0\) take \(V=0\). Let \(D=\|\Delta\|_{\rm cb}>0\) and \(c>0\). By Lemma 4.2 and Theorem 3.1 there is a positive invertible \(S\) on \(F\oplus K\) with \(\|S\|\|S^{-1}\|\le\beta(cD)\) such that \(S\Phi_c(\cdot)S^{-1}\) preserves adjoints. Put \(Q=S^2\), \(m=\|Q^{-1}\|^{-1}\) and \(M=\|Q\|\), so that \(m\le Q\le M\) and \(M/m=(\|S\|\|S^{-1}\|)^2\le\beta(cD)^2\). The identity \(S\Phi_c(a^*)S^{-1}=(S\Phi_c(a)S^{-1})^*=S^{-1}\Phi_c(a)^*S\) says \(Q\Phi_c(a^*)=\Phi_c(a)^*Q\); with \(a^*\) in place of \(a\),
\[
Q\Phi_c(a)=\Phi_c(a^*)^*Q,\qquad \Phi_c(a^*)^*=\begin{pmatrix}\lambda(a)&0\\ c\Delta(a^*)^*&\sigma(a)\end{pmatrix}.
\tag{4.4}
\]
Write \(Q=(Q_{ij})\) relative to \(F\oplus K\). The upper row of (4.4) reads
\[
Q_{11}\lambda(a)=\lambda(a)Q_{11},\qquad cQ_{11}\Delta(a)+Q_{12}\sigma(a)=\lambda(a)Q_{12}.
\tag{4.5}
\]
The compression \(Q_{11}\) satisfies \(Q_{11}\ge m\), so it is invertible with \(\|Q_{11}^{-1}\|\le1/m\), and \(Q_{11}^{-1}\) commutes with \(\lambda(A)\). The block \(Q_{12}\) is the off-diagonal block of \(Q-\frac{M+m}2\cdot1\), whose norm is at most \(\frac{M-m}2\); so \(\|Q_{12}\|\le\frac{M-m}2\). Put \(V_c=-c^{-1}Q_{11}^{-1}Q_{12}\). By (4.5), \(\Delta(a)=c^{-1}Q_{11}^{-1}\big(\lambda(a)Q_{12}-Q_{12}\sigma(a)\big)=V_c\sigma(a)-\lambda(a)V_c\), and
\[
\|V_c\|\le\frac{M-m}{2cm}\le\frac{\beta(cD)^2-1}{2c}=\frac{cD^2+D\sqrt{c^2D^2+4}}4 ,
\tag{4.6}
\]
using \(\beta(s)^2-1=\frac12\big(s^2+s\sqrt{s^2+4}\big)\). The right side of (4.6) tends to \(D/2\) as \(c\to0\). The operators implementing \(\Delta\) form a set that is closed in the weak operator topology, because (4.2) is linear in \(V\). Its intersections with the closed balls of radius \(D/2+1/j\) are nonempty, compact in the weak operator topology and decreasing in \(j\), so they have a common point \(V\), with \(\|V\|\le D/2\). \(\square\)

**Corollary 4.4** (Christensen's criterion). A rectangular derivation is implemented by a bounded operator if and only if it is completely bounded.

**Proof.** Combine Theorem 4.3 with \(\|\Delta\|_{\rm cb}\le2\|V\|\). \(\square\)

**Corollary 4.5** (Arveson's distance formula). Let \(A\subseteq B(H)\) be a C\*-algebra with \(1_H\in A\), and \(x\in B(H)\). Then
\[
2\operatorname{dist}(x,A')=\|\operatorname{ad}(x)|_A\|_{\rm cb},
\]
and the distance to the commutant \(A'\) is attained.

**Proof.** For \(y\in A'\), \(\operatorname{ad}(x)|_A=\operatorname{ad}(x-y)|_A\), whose completely bounded norm is at most \(2\|x-y\|\). Conversely, \(\Delta=\operatorname{ad}(x)|_A\) is a completely bounded derivation for the inclusion representation, so Theorem 4.3 gives \(V\) with \(\|V\|\le\frac12\|\Delta\|_{\rm cb}\) and \(Va-aV=xa-ax\) for \(a\in A\). Then \(x-V\in A'\) and \(\operatorname{dist}(x,A')\le\|V\|\). The function \(y\mapsto\|x-y\|\) is lower semicontinuous for the weak operator topology, and the bounded parts of \(A'\) are compact in it, so the infimum is attained. \(\square\)

The formula involves the completely bounded norm. Whether the norm \(\|\operatorname{ad}(x)|_A\|\) alone controls \(\operatorname{dist}(x,A')\) with a constant independent of \(A\) and \(x\) is a form of the derivation problem; the last lesson of the course proves that it does.

## 5. Exercises

**Exercise 5.1.** Prove (1.1), and show that \(\|u\|_{\rm row}\le\|u\|_{\rm cb}\) for every linear \(u:A\to B(K,F)\).

**Exercise 5.2.** Let \(A=\mathbb C^2\) with \(p=(1,0)\), let \(s\ge0\), and \(P_s=\left(\begin{smallmatrix}1&s\\0&0\end{smallmatrix}\right)\in M_2(\mathbb C)\). Show that \(\pi_s(\alpha,\beta)=\alpha P_s+\beta(1-P_s)\) is a unital homomorphism of \(A\) into \(M_2(\mathbb C)\), and that
\[
\beta(2s)\le\|\pi_s\|\le\|\pi_s\|_{\rm cb}\le\beta(s)^2 .
\]
Deduce that \(\pi_s\) is not a \(*\)-homomorphism for \(s>0\).

**Exercise 5.3.** Let \(p\in B(H)\) be a projection and \(A=\{\alpha p+\beta(1-p):\alpha,\beta\in\mathbb C\}\). Write \(x\in B(H)\) as \(\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) relative to \(H=pH\oplus(1-p)H\). Show directly that \(\operatorname{dist}(x,A')=\max(\|b\|,\|c\|)=\frac12\|\operatorname{ad}(x)|_A\|\), and conclude from Corollary 4.5 that here \(\|\operatorname{ad}(x)|_A\|=\|\operatorname{ad}(x)|_A\|_{\rm cb}\).

**Exercise 5.4.** Let \(A=\mathbb C^2\) act on \(\mathbb C^2\) by diagonal matrices, and \(\Delta=\operatorname{ad}(e_{12})|_A\), where \(e_{12}\) is the matrix unit. Show that \(\|\Delta\|_{\rm cb}=2\) and that every operator implementing \(\Delta\) has norm at least \(1\). So the bound of Theorem 4.3 is attained.

**Exercise 5.5.** Let \(\sigma,\rho\) be representations of \(A\) on \(K\) and \(H\), and \(V:K\to H\) a bounded operator, not necessarily invertible, with \(\rho(a)V=V\sigma(a)\). Show that \(V^*V\in\sigma(A)'\) and \(VV^*\in\rho(A)'\), and that the partial isometry of the polar decomposition of \(V\) also intertwines \(\sigma\) and \(\rho\).

## 6. Solutions

**Solution 5.1.** \(x\) is the first row of the square matrix \(\tilde x\) with zero other rows, and \(\tilde x\tilde x^*\) has \(\sum_jx_jx_j^*\) in its \((1,1)\) entry and zeros elsewhere; so \(\|x\|^2=\|\tilde x\tilde x^*\|=\|\sum_jx_jx_j^*\|\). The column case uses \(\tilde y^*\tilde y\). Finally \(u_{1,h}(x)\) is the first row of \(u_h(\tilde x)\), so \(\|u_{1,h}(x)\|\le\|u_h(\tilde x)\|\le\|u\|_{\rm cb}\|x\|\).

**Solution 5.2.** \(P_s^2=P_s\), so \(P_s\) and \(1-P_s\) are complementary idempotents and \(\pi_s\) is a unital homomorphism. With \(S=\left(\begin{smallmatrix}1&s\\0&1\end{smallmatrix}\right)\), \(SP_sS^{-1}=\left(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\right)\) (check \(SP_s=\left(\begin{smallmatrix}1&s\\0&0\end{smallmatrix}\right)=\left(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\right)S\)), so \(S\pi_s(\cdot)S^{-1}\) is a \(*\)-homomorphism and Lemma 1.1(3) gives \(\|\pi_s\|_{\rm cb}\le\|S\|\|S^{-1}\|=\beta(s)^2\) (\(S^{-1}\) is \(S\) with \(-s\), of the same norm). The unit vector \((1,-1)\) of \(A\) gives \(\pi_s(1,-1)=2P_s-1=\left(\begin{smallmatrix}1&2s\\0&-1\end{smallmatrix}\right)\), whose norm is \(\beta(2s)\) (multiply on the right by the unitary \(\operatorname{diag}(1,-1)\)). For \(s>0\), \(\beta(2s)>1\), so \(\pi_s\) is not contractive, whereas \(*\)-homomorphisms are.

**Solution 5.3.** \(A'\) consists of the operators commuting with \(p\), the block diagonal ones. For block diagonal \(y\), the off-diagonal blocks of \(x-y\) are \(b\) and \(c\), so \(\|x-y\|\ge\max(\|b\|,\|c\|)\), with equality for \(y=\operatorname{diag}(a,d)\). Next, \(\operatorname{ad}(x)(\alpha p+\beta(1-p))=(\alpha-\beta)[x,p]\) and \([x,p]=\left(\begin{smallmatrix}0&-b\\c&0\end{smallmatrix}\right)\) has norm \(\max(\|b\|,\|c\|)\). On the unit ball \(|\alpha|,|\beta|\le1\) the factor \(|\alpha-\beta|\) reaches \(2\). Hence \(\|\operatorname{ad}(x)|_A\|=2\max(\|b\|,\|c\|)=2\operatorname{dist}(x,A')\), which equals \(\|\operatorname{ad}(x)|_A\|_{\rm cb}\) by Corollary 4.5.

**Solution 5.4.** \(\Delta(\alpha,\beta)=e_{12}\operatorname{diag}(\alpha,\beta)-\operatorname{diag}(\alpha,\beta)e_{12}=(\beta-\alpha)e_{12}\), so \(\|\Delta\|=2\), attained at \((-1,1)\); and \(\|\Delta\|_{\rm cb}\le2\|e_{12}\|=2\). An operator \(V\) implements \(\Delta\) exactly when \(V-e_{12}\) commutes with the diagonal matrices, that is, is diagonal. Its \((1,2)\) entry is then \(1\), so \(\|V\|\ge1=\frac12\|\Delta\|_{\rm cb}\).

**Solution 5.5.** As in Lemma 2.2, \(V^*\rho(a)=\sigma(a)V^*\), so \(V^*V\sigma(a)=V^*\rho(a)V=\sigma(a)V^*V\) and \(VV^*\rho(a)=V\sigma(a)V^*=\rho(a)VV^*\). Write \(V=W|V|\). Then \(|V|\) commutes with \(\sigma(A)\), and \(W\sigma(a)|V|=W|V|\sigma(a)=V\sigma(a)=\rho(a)V=\rho(a)W|V|\). So \(W\sigma(a)\) and \(\rho(a)W\) agree on the closure of the range of \(|V|\), which is the initial space \(W^*WK\) of \(W\). This space reduces \(\sigma\) (its projection \(W^*W\) is the support of \(V^*V\in\sigma(A)'\)); on its orthogonal complement both \(W\sigma(a)\) and \(\rho(a)W\) vanish, the first because \(\sigma(a)\) preserves the complement and \(W\) kills it. Hence \(W\sigma(a)=\rho(a)W\).

## References

- [OpenAI-288] OpenAI, Kadison's similarity theorem through uniform derivation estimates, preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026
- [Ozawa] N. Ozawa, An invitation to the similarity problems (after Pisier), lecture notes, RIMS, 2006: Theorem 3.1 (similarity and complete boundedness), Lemma 1.2 (the triangular homomorphism of a derivation), Corollary 3.2. https://www.kurims.kyoto-u.ac.jp/~narutaka/notes/similarity.pdf
- [CSSW] E. Christensen, A. M. Sinclair, R. R. Smith, S. A. White, Perturbations of C\*-algebraic invariants, Geometric and Functional Analysis 20 (2010), 368–397, formula (2.1) (Arveson's distance formula). https://arxiv.org/abs/0910.1368
