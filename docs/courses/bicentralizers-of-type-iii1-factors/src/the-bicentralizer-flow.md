# The bicentralizer flow

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(M\) be a type III₁ factor with separable predual. Connes observed that the bicentralizers of two faithful normal states \(\varphi,\psi\) are canonically isomorphic: conjugating by unitaries \(u_n\) that move \(\varphi\) closer and closer to \(\psi\) carries \(\mathrm B(M,\varphi)\) onto \(\mathrm B(M,\psi)\). Haagerup, and independently Marrakchi, found that the same idea, with partial isometries that scale \(\varphi\) by a factor \(\lambda\) instead of unitaries, gives a canonical action \(\beta^\varphi\) of the multiplicative group \(\mathbb R_+^*\) on \(\mathrm B(M,\varphi)\), the *bicentralizer flow* of Ando, Haagerup, Houdayer and Marrakchi [AHHM]. This lesson constructs both. Every element of \(\mathrm B(M,\varphi)\) commutes in the ultrapower with the asymptotic centralizer, and the conjugating unitaries or partial isometries are unique up to elements of the asymptotic centralizer; the remaining point, that the result lies in \(M\) itself, follows from a reparametrization argument.

We use [Asymptotic centralizers of type III₁ factors](asymptotic-centralizers-of-type-iii1-factors.md) (Lemmas 1.1–1.3, Theorem 3.1, Proposition 4.1, Corollary 4.2) and [The bicentralizer](the-bicentralizer.md) (Proposition 1.3, Theorem 2.1, Lemma 2.3); Lemmas 1.3 and 1.4 and the result (B8) of [Ultraproducts and the asymptotic centralizer](course:type-iii-factors/ultraproducts-and-the-asymptotic-centralizer#results-used-from-other-lessons); and the uniqueness of the decomposition of a self-adjoint normal functional into positive parts of minimal total norm, Corollary 2.8 of [Polar decomposition of functionals and weak compactness in preduals](course:foundations-of-von-neumann-algebras/polar-decomposition-of-functionals-and-weak-compactness-in-preduals). Throughout, \(M\) is a type III₁ factor with separable predual, \(\varphi,\psi,\chi\) are faithful normal states on \(M\), and \(\omega\) is a free ultrafilter on \(\mathbb N\).

## 1. Three lemmas

**Lemma 1.1** (reparametrization). Let \((y_n)\) be a bounded sequence in \(M\). Suppose that for every free ultrafilter \(\omega\) and every map \(s:\mathbb N\to\mathbb N\) with \(s(n)\to\infty\), the sequences \((y_n)\) and \((y_{s(n)})\) belong to \(N_\omega\) and have the same class in \(M^\omega\). Then \((y_n)\) converges \(*\)-strongly to some \(y\in M\), and its class is the constant \(y\) in every \(M^\omega\).

**Proof.** Suppose \((y_n)\) is not Cauchy for \(d(a,b)=\|a-b\|^\sharp_\varphi\). Then there are \(c>0\) and indices \(n_1<n_2<\cdots\) and \(m_k>n_k\) with \(d(y_{n_k},y_{m_k})\ge c\). Let \(\omega\) be a free ultrafilter containing \(\{n_k:k\ge1\}\), and \(s(n_k)=m_k\), \(s(n)=n\) otherwise. Then \(s(n)\to\infty\) and \(\lim_\omega d(y_n,y_{s(n)})\ge c\), so the difference of the two sequences is not in \(I_\omega\), against the hypothesis. Hence \((y_n)\) is \(d\)-Cauchy; it is bounded, so by Lemma 1.4 of the ultraproduct lesson (after rescaling into the unit ball) it converges \(*\)-strongly to some \(y\in M\), and \(y_n-y\in I_\omega\) for every \(\omega\). \(\square\)

**Lemma 1.2** (products land in the asymptotic centralizer). Let \(\lambda>0\).

1. If \((v_n),(w_n)\) are bounded with \(\|v_n\varphi-\lambda\varphi v_n\|\to_\omega0\) and \(\|w_n\varphi-\lambda\varphi w_n\|\to_\omega0\), then \((w_n^*v_n)\in A_{\varphi,\omega}\).
2. If \(u_n,w_n\) are unitaries with \(\|u_n\varphi u_n^*-\psi\|\to_\omega0\) and \(\|w_n\varphi w_n^*-\psi\|\to_\omega0\), then \((w_n^*u_n)\in A_{\varphi,\omega}\).
3. If \(u_n\) are unitaries with \(\|u_n\varphi u_n^*-\psi\|\to_\omega0\) and \((y_n)\in A_{\psi,\omega}\), then \((u_n^*y_nu_n)\in A_{\varphi,\omega}\).

**Proof.** (1) Taking adjoints in the bimodule \(M_*\), \((w\varphi)^*=\varphi w^*\) and \((\lambda\varphi w)^*=\lambda w^*\varphi\), so \(\|\varphi w_n^*-\lambda w_n^*\varphi\|=\|w_n\varphi-\lambda\varphi w_n\|\). Then
\[
w_n^*v_n\varphi-\varphi w_n^*v_n=w_n^*(v_n\varphi-\lambda\varphi v_n)+(\lambda w_n^*\varphi-\varphi w_n^*)v_n ,
\]
whose norm tends to \(0\) along \(\omega\).

(2) By (1.1) of the first lesson, \(\|[w_n^*u_n,\varphi]\|=\|w_n^*u_n\varphi u_n^*w_n-\varphi\|=\|u_n\varphi u_n^*-w_n\varphi w_n^*\|\to_\omega0\).

(3) Conjugation by a unitary is isometric on \(M_*\), and \(u_n(u_n^*y_nu_n\varphi-\varphi u_n^*y_nu_n)u_n^*=y_n(u_n\varphi u_n^*)-(u_n\varphi u_n^*)y_n\), whose norm is at most \(\|[y_n,\psi]\|+2\|y_n\|\,\|u_n\varphi u_n^*-\psi\|\). \(\square\)

Write \(\tau\) for the trace of the II₁ factor \(M_{\varphi,\omega}\) (Theorem 3.1 of the first lesson); it is the restriction of \(\varphi^\omega\).

**Lemma 1.3.** For \(x\in\mathrm B(M,\varphi)\) and \(Z\in M_{\varphi,\omega}\), \(\varphi^\omega(xZ)=\varphi(x)\tau(Z)\).

**Proof.** The inclusion \(M_{\varphi,\omega}\subset M^\omega\) is a unital \(*\)-homomorphism carrying the faithful normal state \(\tau\) to \(\varphi^\omega\), so it is normal: if \(a_i\uparrow a\), then \(Z=\sup_ia_i\) in \(M^\omega\) satisfies \(Z\le a\) and \(\varphi^\omega(a-Z)=\tau(a)-\lim_i\tau(a_i)=0\). Hence \(\rho(Z)=\varphi^\omega(xZ)\) is a normal functional on \(M_{\varphi,\omega}\). It is tracial: for \(Z_1,Z_2\in M_{\varphi,\omega}\), using \(Z_2\varphi^\omega=\varphi^\omega Z_2\) (Lemma 1.1(2) of the first lesson) and \(xZ_2=Z_2x\) (Proposition 1.3 of the bicentralizer lesson),
\[
\rho(Z_1Z_2)=(Z_2\varphi^\omega)(xZ_1)=(\varphi^\omega Z_2)(xZ_1)=\varphi^\omega(Z_2xZ_1)=\varphi^\omega(xZ_2Z_1)=\rho(Z_2Z_1).
\]
Writing \(x\) as a combination of self-adjoint elements of \(\mathrm B(M,\varphi)\), we may assume \(x=x^*\); then \(\rho\) is self-adjoint. Let \(\rho=\rho_+-\rho_-\) be its decomposition into normal positive functionals with \(\|\rho\|=\|\rho_+\|+\|\rho_-\|\). For a unitary \(U\in M_{\varphi,\omega}\), \(\rho\circ\operatorname{Ad}U=\rho\), and \(\rho_\pm\circ\operatorname{Ad}U\) is another such decomposition; by uniqueness, \(\rho_\pm\circ\operatorname{Ad}U=\rho_\pm\). Since unitaries span \(M_{\varphi,\omega}\), \(\rho_\pm\) are tracial, so by uniqueness of the normal tracial state of a II₁ factor (B8), \(\rho_\pm=\rho_\pm(1)\tau\). Hence \(\rho=\rho(1)\tau=\varphi(x)\tau\). \(\square\)

## 2. Connes' isomorphism

By Corollary 4.2 of the first lesson there are unitaries \(u_n\in M\) with \(\|u_n\varphi u_n^*-\psi\|\to0\). Call such a sequence a *\((\psi,\varphi)\)-sequence*.

**Theorem 2.1.** Let \((u_n)\) be a \((\psi,\varphi)\)-sequence. For every \(x\in\mathrm B(M,\varphi)\), \(u_nxu_n^*\) converges \(*\)-strongly to an element \(\beta_{\psi,\varphi}(x)\in\mathrm B(M,\psi)\), which does not depend on the choice of \((u_n)\). The map \(\beta_{\psi,\varphi}\colon\mathrm B(M,\varphi)\to\mathrm B(M,\psi)\) is a \(*\)-isomorphism with \(\psi\circ\beta_{\psi,\varphi}=\varphi\),
\[
\beta_{\varphi,\varphi}=\mathrm{id},\qquad\beta_{\chi,\psi}\circ\beta_{\psi,\varphi}=\beta_{\chi,\varphi},
\]
and for every bounded sequence \((a_n)\) with \(\|a_n\varphi-\psi a_n\|\to0\) and every \(x\in\mathrm B(M,\varphi)\),
\[
a_nx-\beta_{\psi,\varphi}(x)a_n\to0\quad*\text{-strongly}.
\tag{2.1}
\]
If \(y\in M\) satisfies \(u_nx-yu_n\to0\) \(*\)-strongly for one \((\psi,\varphi)\)-sequence, then \(y=\beta_{\psi,\varphi}(x)\).

**Proof.** Fix \(\omega\). By Lemma 1.3 of the first lesson, \(U=[u_n]\) is a unitary of \(M^\omega\) with \(U\varphi^\omega U^*=\psi^\omega\). If \((w_n)\) is another \((\psi,\varphi)\)-sequence, with class \(W\), then \(W^*U\in M_{\varphi,\omega}\) by Lemma 1.2(2), so \(W^*Ux=xW^*U\) for \(x\in\mathrm B(M,\varphi)\), that is
\[
UxU^*=WxW^* .
\tag{2.2}
\]
For \(s(n)\to\infty\), \((u_{s(n)})\) is again a \((\psi,\varphi)\)-sequence. So (2.2), for every \(\omega\), gives the hypothesis of Lemma 1.1 for \(y_n=u_nxu_n^*\), which lies in \(N_\omega\) as a product of multipliers. Hence \(u_nxu_n^*\) converges \(*\)-strongly to some \(\beta_{\psi,\varphi}(x)\in M\), equal to \(UxU^*\) in every \(M^\omega\); by (2.2) it does not depend on the sequence.

*Values in \(\mathrm B(M,\psi)\).* Let \(Y=[y_n]\in M_{\psi,\omega}\). By Lemma 1.2(3), \(U^*YU\in M_{\varphi,\omega}\), so it commutes with \(x\), and \(Y\) commutes with \(UxU^*=\beta_{\psi,\varphi}(x)\). By Proposition 1.3 of the bicentralizer lesson, \(\beta_{\psi,\varphi}(x)\in\mathrm B(M,\psi)\).

*Algebraic properties.* \(x\mapsto UxU^*\) is an injective \(*\)-homomorphism, so \(\beta_{\psi,\varphi}\) is one. With \(u_n=1\), \(\beta_{\varphi,\varphi}=\mathrm{id}\). If \((v_n)\) is a \((\chi,\psi)\)-sequence, then \(\|v_nu_n\varphi u_n^*v_n^*-\chi\|\le\|u_n\varphi u_n^*-\psi\|+\|v_n\psi v_n^*-\chi\|\to0\), so \((v_nu_n)\) is a \((\chi,\varphi)\)-sequence, and in \(M^\omega\)
\[
\beta_{\chi,\varphi}(x)=VUxU^*V^*=V\beta_{\psi,\varphi}(x)V^*=\beta_{\chi,\psi}(\beta_{\psi,\varphi}(x)).
\]
So \(\beta_{\varphi,\psi}\) inverts \(\beta_{\psi,\varphi}\). Since \(U^*\psi^\omega U=\varphi^\omega\), \(\psi(\beta_{\psi,\varphi}(x))=\psi^\omega(UxU^*)=\varphi^\omega(x)=\varphi(x)\).

*Intertwining (2.1).* Let \(c_n=u_n^*a_n\). Since \(u_n^*\psi-\varphi u_n^*=u_n^*(\psi-u_n\varphi u_n^*)\),
\[
\|[c_n,\varphi]\|\le\|a_n\varphi-\psi a_n\|+\|a_n\|\,\|\psi-u_n\varphi u_n^*\|\to0,
\]
so \((c_n)\in\mathrm{AC}(M,\varphi)\). Write \(a_nx-\beta_{\psi,\varphi}(x)a_n=u_nz_n\) with
\[
z_n=(c_nx-xc_n)+(x-u_n^*\beta_{\psi,\varphi}(x)u_n)c_n .
\]
The first term tends to \(0\) \(*\)-strongly because \(x\) and \(x^*\) lie in \(\mathrm B(M,\varphi)\). For the second, \(e_n=\beta_{\psi,\varphi}(x)-u_nxu_n^*\to0\) \(*\)-strongly, and \(\|u_n^*e_nu_n\|_\varphi^2=(u_n\varphi u_n^*)(e_n^*e_n)\le\psi(e_n^*e_n)+\|e_n\|^2\|u_n\varphi u_n^*-\psi\|\to0\); likewise for the adjoint. So \(u_n^*e_nu_n=u_n^*\beta_{\psi,\varphi}(x)u_n-x\to0\) \(*\)-strongly, and its product with the asymptotically centralizing \((c_n)\) tends to \(0\) along every \(\omega\), because \(I_\omega\) is an ideal of \(A_{\varphi,\omega}\). Hence \(z_n\to0\) \(*\)-strongly along every \(\omega\), so \(z_n\to0\) \(*\)-strongly. Finally \(\|u_nz_n\|_\varphi=\|z_n\|_\varphi\), and \(\|(u_nz_n)^*\|_\varphi\to0\) as in the proof of Lemma 1.3 of the first lesson.

*Uniqueness.* If \(u_nx-yu_n\to0\) \(*\)-strongly, then, as for \(e_n\) above with the roles of \(\varphi\) and \(\psi\) exchanged, \((u_nx-yu_n)u_n^*=u_nxu_n^*-y\to0\) strongly, so \(y=\beta_{\psi,\varphi}(x)\). \(\square\)

## 3. The flow

Let \(\lambda>0\). A finite family of bounded sequences \((v_{k,n})_n\), \(1\le k\le m\), is an *admissible \(\lambda\)-family along \(\omega\)* if
\[
\lim_\omega\|v_{k,n}\varphi-\lambda\varphi v_{k,n}\|=0\quad(1\le k\le m),\qquad\lim_\omega\Big\|1-\sum_kv_{k,n}v_{k,n}^*\Big\|^\sharp_\varphi=0 .
\]
By Lemma 1.2 of the first lesson the classes \(V_k\) belong to \(M^\omega\), with \(V_k\varphi^\omega=\lambda\varphi^\omega V_k\) and \(\sum_kV_kV_k^*=1\). By Proposition 4.1 there, admissible \(\lambda\)-families exist, with ordinary convergence; for \(\lambda\le1\) one sequence suffices.

**Theorem 3.1.** For every \(\lambda>0\) there is a unital \(*\)-automorphism \(\beta^\varphi_\lambda\) of \(\mathrm B(M,\varphi)\) such that:

1. for every free ultrafilter \(\omega\), every admissible \(\lambda\)-family along \(\omega\), and every \(x\in\mathrm B(M,\varphi)\), \(\sum_kV_kxV_k^*=\beta^\varphi_\lambda(x)\) in \(M^\omega\); in particular, for the family of Proposition 4.1 of the first lesson, \(\sum_kv_{k,n}xv_{k,n}^*\to\beta_\lambda^\varphi(x)\) \(*\)-strongly;
2. for every bounded sequence \((w_n)\) with \(\|w_n\varphi-\lambda\varphi w_n\|\to0\) and every \(x\in\mathrm B(M,\varphi)\), \(w_nx-\beta^\varphi_\lambda(x)w_n\to0\) \(*\)-strongly;
3. \(\beta^\varphi_1=\mathrm{id}\), \(\beta^\varphi_\lambda\beta^\varphi_\mu=\beta^\varphi_{\lambda\mu}\), and \(\varphi\circ\beta_\lambda^\varphi=\varphi\) on \(\mathrm B(M,\varphi)\);
4. \(\lambda\mapsto\beta^\varphi_\lambda\) is continuous for the \(u\)-topology: \(\beta^\varphi_\lambda(x)\to x\) strongly as \(\lambda\to1\), for every \(x\);
5. \(\beta^\psi_\lambda\circ\beta_{\psi,\varphi}=\beta_{\psi,\varphi}\circ\beta^\varphi_\lambda\).

**Proof.** (1) Let \((v_{k,n})\) and \((w_{l,n})\) be admissible \(\lambda\)-families along \(\omega\), with classes \(V_k,W_l\). By Lemma 1.2(1), \(W_l^*V_k\in M_{\varphi,\omega}\), so it commutes with \(x\in\mathrm B(M,\varphi)\), and
\[
\sum_kV_kxV_k^*=\sum_{k,l}W_lW_l^*V_kxV_k^*=\sum_{k,l}W_lxW_l^*V_kV_k^*=\sum_lW_lxW_l^* .
\tag{3.1}
\]
For the family of Proposition 4.1 of the first lesson and \(s(n)\to\infty\), the reparametrized family \((v_{k,s(n)})\) is admissible along every \(\omega\); by (3.1) and Lemma 1.1, \(y_n=\sum_kv_{k,n}xv_{k,n}^*\) converges \(*\)-strongly to an element \(\beta^\varphi_\lambda(x)\in M\), equal to \(\sum_kV_kxV_k^*\) in every \(M^\omega\). By (3.1) again, every admissible family gives the same element.

*Values in the bicentralizer, multiplicativity.* Let \(Y=[y_n]\in M_{\varphi,\omega}\). The class of \((v_{k,n}^*y_nv_{l,n})_n\) lies in \(M_{\varphi,\omega}\): writing \(v_k,y,v_l\) for the \(n\)-th terms,
\[
v_k^*yv_l\varphi\approx\lambda\,v_k^*y\varphi v_l\approx\lambda\,v_k^*\varphi yv_l\approx\varphi v_k^*yv_l ,
\]
where the three errors are bounded by \(\|v_k\|\|y\|\,\|v_l\varphi-\lambda\varphi v_l\|\), \(\lambda\|v_k\|\|v_l\|\,\|[y,\varphi]\|\) and \(\|y\|\|v_l\|\,\|\lambda v_k^*\varphi-\varphi v_k^*\|\), all tending to \(0\) along \(\omega\) (the last by the adjoint identity in the proof of Lemma 1.2(1)). So \(x\) commutes with \(V_k^*YV_l\), and
\[
\beta^\varphi_\lambda(x)Y=\sum_{k,l}V_kxV_k^*YV_lV_l^*=\sum_{k,l}V_kV_k^*YV_lxV_l^*=Y\beta^\varphi_\lambda(x).
\]
Thus \(\beta_\lambda^\varphi(x)\in\mathrm B(M,\varphi)\). With \(Y=1\), \(V_k^*V_l\in M_{\varphi,\omega}\) commutes with \(x\), so
\[
\beta^\varphi_\lambda(x)\beta^\varphi_\lambda(y)=\sum_{k,l}V_kx(V_k^*V_l)yV_l^*=\sum_{k,l}V_kV_k^*V_lxyV_l^*=\beta^\varphi_\lambda(xy).
\]
It is linear, \(*\)-preserving and unital since \(\sum_kV_kV_k^*=1\).

(3) The family consisting of the constant sequence \(1\) is admissible for \(\lambda=1\), so \(\beta^\varphi_1=\mathrm{id}\). If \((v_{k,n})\) is admissible for \(\lambda\) and \((w_{l,n})\) for \(\mu\), then \((v_{k,n}w_{l,n})\) is admissible for \(\lambda\mu\): \(\|vw\varphi-\lambda\mu\varphi vw\|\le\|v\|\,\|w\varphi-\mu\varphi w\|+\mu\|v\varphi-\lambda\varphi v\|\,\|w\|\), and \(\sum_{k,l}V_kW_lW_l^*V_k^*=1\). Hence
\[
\beta^\varphi_{\lambda\mu}(x)=\sum_{k,l}V_kW_lxW_l^*V_k^*=\sum_kV_k\beta^\varphi_\mu(x)V_k^*=\beta^\varphi_\lambda(\beta^\varphi_\mu(x)).
\]
So \(\beta^\varphi_\lambda\) is an automorphism with inverse \(\beta^\varphi_{1/\lambda}\). For state preservation, \(V_k^*V_k\in M_{\varphi,\omega}\), so Lemma 1.3 gives
\[
\varphi^\omega(V_kxV_k^*)=(\varphi^\omega V_k)(xV_k^*)=\lambda^{-1}\varphi^\omega(xV_k^*V_k)=\lambda^{-1}\varphi(x)\tau(V_k^*V_k)=\varphi(x)\varphi^\omega(V_kV_k^*),
\]
using \(\varphi^\omega(V_k^*V_k)=(V_k\varphi^\omega)(V_k^*)=\lambda\varphi^\omega(V_kV_k^*)\). Summing over \(k\), \(\varphi(\beta^\varphi_\lambda(x))=\varphi(x)\).

(2) Let \(W=[w_n]\in M^\omega\) (Lemma 1.2 of the first lesson). By Lemma 1.2(1), \(V_k^*W\in M_{\varphi,\omega}\), so \(Wx=\sum_kV_kV_k^*Wx=\sum_kV_kxV_k^*W=\beta^\varphi_\lambda(x)W\). Thus \(w_nx-\beta^\varphi_\lambda(x)w_n\to0\) \(*\)-strongly along every \(\omega\), hence \(*\)-strongly.

(4) Let \(\lambda_j\to1\) with \(\lambda_j\le1\). For each \(j\) take a single sequence \((v_{j,n})_n\) as in Proposition 4.1 of the first lesson (with \(m=1\)), and choose \(n(j)\) so large that \(w_j=v_{j,n(j)}\) satisfies \(\|w_j\varphi-\lambda_j\varphi w_j\|<1/j\), \(\|1-w_jw_j^*\|^\sharp_\varphi<1/j\) and \(\|w_jxw_j^*-\beta^\varphi_{\lambda_j}(x)\|^\sharp_\varphi<1/j\). Then \(\|[w_j,\varphi]\|\le1/j+(1-\lambda_j)\|w_j\|\to0\), so along every \(\omega\) the class \(W\) lies in \(M_{\varphi,\omega}\) with \(WW^*=1\), and \(WxW^*=xWW^*=x\). Hence \(w_jxw_j^*\to x\), and \(\beta^\varphi_{\lambda_j}(x)\to x\), \(*\)-strongly. For \(\lambda_j\ge1\), \(\|\beta^\varphi_{\lambda_j}(x)-x\|_\varphi=\|x-\beta^\varphi_{1/\lambda_j}(x)\|_\varphi\to0\), since \(\varphi\)-preserving automorphisms preserve \(\|\cdot\|_\varphi\). For \(\varphi\)-preserving automorphisms, pointwise strong convergence is convergence in the \(u\)-topology: they are implemented on \(L^2(\mathrm B(M,\varphi),\varphi_{\mathrm B})\) by unitaries \(U_\lambda\) with \(U_\lambda x\xi=\beta^\varphi_\lambda(x)\xi\), these converge strongly to \(1\), and every normal functional is a sum of vector functionals.

(5) If \((v_{k,n})\) is admissible for \(\varphi\) and \((u_n)\) is a \((\psi,\varphi)\)-sequence, then \((u_nv_{k,n}u_n^*)\) is admissible for \(\psi\): \(\|uvu^*\psi-\lambda\psi uvu^*\|\le\|v\varphi-\lambda\varphi v\|+(1+\lambda)\|v\|\,\|u\varphi u^*-\psi\|\). So for \(x\in\mathrm B(M,\varphi)\), in \(M^\omega\),
\[
\beta^\psi_\lambda(\beta_{\psi,\varphi}(x))=\sum_kUV_kU^*\,UxU^*\,UV_k^*U^*=U\beta^\varphi_\lambda(x)U^*=\beta_{\psi,\varphi}(\beta^\varphi_\lambda(x)).\qquad\square
\]

**Corollary 3.2.** Let \(\mathrm B=\mathrm B(M,\varphi)\), \(\varphi_{\mathrm B}=\varphi|_{\mathrm B}\), \(\lambda>0\). If \((w_n)\) is a bounded sequence in \(\mathrm B\) with \(\|w_n\varphi_{\mathrm B}-\lambda\varphi_{\mathrm B}w_n\|_{\mathrm B_*}\to0\), then \(w_na-\beta^\varphi_\lambda(a)w_n\to0\) \(*\)-strongly for every \(a\in\mathrm B\).

**Proof.** By (2.1) of the bicentralizer lesson, \((w_n\varphi-\lambda\varphi w_n)(y)=(w_n\varphi_{\mathrm B}-\lambda\varphi_{\mathrm B}w_n)(E(y))\) for \(y\in M\), where \(E\) is the \(\varphi\)-preserving expectation onto \(\mathrm B\). So \(\|w_n\varphi-\lambda\varphi w_n\|\to0\), and Theorem 3.1(2) applies. \(\square\)

In the notation \(b_s=\beta^\varphi_{e^{-s}}\), Corollary 3.2 says: for bounded \((w_n)\) in \(\mathrm B\) and \(a\in\mathrm B\), \(\|\varphi_{\mathrm B}w_n-e^sw_n\varphi_{\mathrm B}\|\to0\) implies \(w_na-b_s(a)w_n\to0\) \(*\)-strongly. Together with Theorem 3.1(3), (4) this is the input that the spectral rigidity theorem of a later lesson requires.

## 4. Exercises

**Exercise 4.1.** Show that \(\beta_{\psi,\varphi}\) maps the centre of \(M\), that is \(\mathbb C1\), identically, and that \(\beta^\varphi_\lambda(1)=1\).

**Exercise 4.2.** Let \(u\in M\) be a unitary and \(\psi=u\varphi u^*\). Show that \(\beta_{\psi,\varphi}(x)=uxu^*\) for \(x\in\mathrm B(M,\varphi)\).

**Exercise 4.3.** Show that if \(\mathrm B(M,\varphi)=\mathbb C1\) for one faithful normal state \(\varphi\), then \(\mathrm B(M,\psi)=\mathbb C1\) for every faithful normal state \(\psi\).

**Exercise 4.4.** Let \(x\in\mathrm B(M,\varphi)\) and let \((w_n)\) be a bounded sequence with \(\|w_n\varphi-\lambda\varphi w_n\|\to0\) and \(w_nw_n^*\to1\) \(*\)-strongly. Show that \(w_nxw_n^*\to\beta^\varphi_\lambda(x)\) \(*\)-strongly.

## 5. Solutions

**4.1.** \(u_n1u_n^*=1\), and \(\sum_kV_kV_k^*=1\).

**4.2.** The constant sequence \(u_n=u\) is a \((\psi,\varphi)\)-sequence, and \(u_nxu_n^*=uxu^*\).

**4.3.** \(\beta_{\psi,\varphi}\) is a bijection of \(\mathrm B(M,\varphi)\) onto \(\mathrm B(M,\psi)\).

**4.4.** Fix \(\omega\). By Lemma 1.2 of the first lesson, \(W=[w_n]\in M^\omega\), and \(WW^*=1\). By Theorem 3.1(2), \(Wx=\beta^\varphi_\lambda(x)W\) in \(M^\omega\), so \(WxW^*=\beta^\varphi_\lambda(x)WW^*=\beta^\varphi_\lambda(x)\). Thus \(w_nxw_n^*-\beta^\varphi_\lambda(x)\to0\) \(*\)-strongly along every \(\omega\), hence \(*\)-strongly.

## References

- [AHHM] H. Ando, U. Haagerup, C. Houdayer, A. Marrakchi, Structure of bicentralizer algebras and inclusions of type III factors, Mathematische Annalen 376 (2020), 1145–1194. https://arxiv.org/abs/1804.05706
- [Marrakchi] A. Marrakchi, Full factors, bicentralizer flow and approximately inner automorphisms, Inventiones Mathematicae 222 (2020), 375–398. https://arxiv.org/abs/1811.10253
