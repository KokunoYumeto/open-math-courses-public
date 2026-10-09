# Transition isomorphisms and the relative flow

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(N\subset M\) be an inclusion with a faithful normal conditional expectation \(E\), and suppose that \(N\) is a factor of type III₁ with separable predual. Conjugation by unitaries of \(N\) that move one faithful normal state \(\varphi\) of \(N\) closer and closer to another one \(\psi\) carries the relative bicentralizer of \(\varphi\) onto that of \(\psi\); partial isometries of \(N\) that scale \(\varphi\) by a factor \(\lambda\) define an action of \(\mathbb R_+^*\) on \(\mathrm B(N\subset M,\varphi)\), the *relative bicentralizer flow* of Ando, Haagerup, Houdayer and Marrakchi [AHHM, Theorem A]. This lesson constructs both, following the absolute case of [The bicentralizer flow](course:bicentralizers-of-type-iii1-factors/the-bicentralizer-flow#2-connes-isomorphism). Two facts specific to inclusions are added: the flow commutes with the modular group of \(\bar\varphi=\varphi\circ E\) (Theorem 3.1(6)), and the von Neumann algebra \(\mathrm B^\sharp=N\vee\mathrm B(N\subset M,\varphi)\) does not depend on \(\varphi\) (Theorem 4.1). The last section computes the relative bicentralizer of a matrix amplification.

We use: [The relative bicentralizer](the-relative-bicentralizer.md) (all of Sections 1 and 2); Lemmas 1.1 (reparametrization) and 1.2 (products of eigen-sequences) of [The bicentralizer flow](course:bicentralizers-of-type-iii1-factors/the-bicentralizer-flow#1-three-lemmas), which concern bounded sequences in a single algebra and are applied below in \(N\) and in \(M\); Lemma 1.2 (asymptotic eigenoperators), Lemma 1.3 (unitaries conjugating states), Proposition 4.1 (rows of approximate eigenoperators) and Corollary 4.2 (Connes–Størmer unitaries) of [Asymptotic centralizers of type III₁ factors](course:bicentralizers-of-type-iii1-factors/asymptotic-centralizers-of-type-iii1-factors#4-approximate-eigenoperators), applied to \(N\); Lemmas 1.1, 1.3 and 1.4 and (B8) of [Ultraproducts and the asymptotic centralizer](course:type-iii-factors/ultraproducts-and-the-asymptotic-centralizer#results-used-from-other-lessons); the modular expectation theorem (ME.1)–(ME.3) of [Conditional expectations from modular invariance](course:OA-MOD/OA-MOD-ME#OA-MOD-ME-01); the uniqueness of the decomposition of a self-adjoint normal functional into positive parts of minimal total norm, [Corollary 2.8 of the polar decomposition lesson](course:foundations-of-von-neumann-algebras/polar-decomposition-of-functionals-and-weak-compactness-in-preduals#OA-FND-PD-07); and the theorem that any two infinite projections of a countably decomposable factor are equivalent, [Proposition 15.2(4) of the projections lesson](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras#OA-FND-TY-20).

## 1. Setting and a trace lemma

Throughout this lesson \(N\) is a factor of type III₁ with separable predual, \(N\subset M\) with the same unit, \(M\) countably decomposable, \(E\colon M\to N\) a faithful normal conditional expectation, and \(\omega\) a free ultrafilter. For faithful normal states \(\varphi,\psi,\chi\) on \(N\) we write \(\bar\varphi=\varphi\circ E\), and so on, and \(\mathrm B(\varphi)=\mathrm B(N\subset M,\varphi)\). The notation \(M^\omega\), \(\pi\), \(N_{\varphi,\omega}\subset M^\omega\), \(\mathcal G_\varphi\), \(\mathcal U_\delta\) is that of the previous lesson. For a unitary \(u\in N\), \(u\bar\varphi u^*=(u\varphi u^*)\circ E\) because \(E\) is \(N\)-bimodular, so
\[
\|u\bar\varphi u^*-\bar\psi\|_{M_*}=\|u\varphi u^*-\psi\|_{N_*}
\tag{1.1}
\]
by the argument of Lemma 1.1 of the previous lesson. Likewise \(\|v\bar\varphi-\lambda\bar\varphi v\|_{M_*}=\|v\varphi-\lambda\varphi v\|_{N_*}\) for \(v\in N\) and \(\lambda>0\). In particular, by Lemma 1.2 of the asymptotic centralizer lesson applied in \(M\) to \(\bar\varphi\), a bounded sequence \((v_n)\) in \(N\) with \(\lim_\omega\|v_n\varphi-\lambda\varphi v_n\|=0\) lies in \(N_\omega\) and its class \(V\) satisfies \(V\bar\varphi^\omega=\lambda\bar\varphi^\omega V\).

Write \(\tau\) for the trace of the II₁ factor \(N_{\varphi,\omega}\); it is the restriction of \(\bar\varphi^\omega\) (Lemma 1.2 of the previous lesson).

**Lemma 1.1.** For \(x\in\mathrm B(\varphi)\) and \(Z\in N_{\varphi,\omega}\), \(\bar\varphi^\omega(xZ)=\bar\varphi(x)\tau(Z)\).

**Proof.** The inclusion \(N_{\varphi,\omega}\subset M^\omega\) is normal, so \(\rho(Z)=\bar\varphi^\omega(xZ)\) is a normal functional on \(N_{\varphi,\omega}\). For \(Z_1,Z_2\in N_{\varphi,\omega}\), \(Z_2\) commutes with \(\bar\varphi^\omega\) and with \(x\) (Lemma 1.2 and Proposition 2.2 of the previous lesson), so
\[
\rho(Z_1Z_2)=(Z_2\bar\varphi^\omega)(xZ_1)=(\bar\varphi^\omega Z_2)(xZ_1)=\bar\varphi^\omega(Z_2xZ_1)=\bar\varphi^\omega(xZ_2Z_1)=\rho(Z_2Z_1).
\]
We may assume \(x=x^*\), so \(\rho\) is self-adjoint. Let \(\rho=\rho_+-\rho_-\) be its decomposition into normal positive functionals with \(\|\rho\|=\|\rho_+\|+\|\rho_-\|\). For a unitary \(U\in N_{\varphi,\omega}\), \(\rho_\pm\circ\operatorname{Ad}U\) is another such decomposition of \(\rho\circ\operatorname{Ad}U=\rho\), so by uniqueness \(\rho_\pm\) are invariant under \(\operatorname{Ad}U\), hence tracial. By (B8) a normal tracial positive functional on a II₁ factor is a multiple of \(\tau\), so \(\rho=\rho(1)\tau=\bar\varphi(x)\tau\). \(\square\)

## 2. Transition isomorphisms

A sequence of unitaries \(u_n\in N\) with \(\|u_n\varphi u_n^*-\psi\|\to0\) is a *\((\psi,\varphi)\)-sequence*; such sequences exist by Corollary 4.2 of the asymptotic centralizer lesson.

**Theorem 2.1.** Let \((u_n)\) be a \((\psi,\varphi)\)-sequence. For every \(x\in\mathrm B(\varphi)\), \(u_nxu_n^*\) converges \(*\)-strongly to an element \(\beta_{\psi,\varphi}(x)\in\mathrm B(\psi)\), which does not depend on the choice of \((u_n)\). The map \(\beta_{\psi,\varphi}\colon\mathrm B(\varphi)\to\mathrm B(\psi)\) is a \(*\)-isomorphism with \(\bar\psi\circ\beta_{\psi,\varphi}=\bar\varphi\), it is the identity on \(N'\cap M\), and
\[
\beta_{\varphi,\varphi}=\mathrm{id},\qquad\beta_{\chi,\psi}\circ\beta_{\psi,\varphi}=\beta_{\chi,\varphi}.
\]
For every bounded sequence \((a_n)\) in \(N\) with \(\|a_n\varphi-\psi a_n\|\to0\) and every \(x\in\mathrm B(\varphi)\),
\[
a_nx-\beta_{\psi,\varphi}(x)a_n\to0\quad*\text{-strongly}.
\tag{2.1}
\]

**Proof.** Fix \(\omega\). By (1.1) and Lemma 1.3 of the asymptotic centralizer lesson (in \(M\), for the states \(\bar\varphi,\bar\psi\)), \(U=\pi(u_n)\) is a unitary of \(M^\omega\) with \(U\bar\varphi^\omega U^*=\bar\psi^\omega\). If \((w_n)\) is another \((\psi,\varphi)\)-sequence with class \(W\), then \((w_n^*u_n)\in A_{\varphi,\omega}(N)\) by Lemma 1.2(2) of the flow lesson applied in \(N\), so \(W^*U\in N_{\varphi,\omega}\) commutes with \(x\in\mathrm B(\varphi)\) (Proposition 2.2 of the previous lesson), that is,
\[
UxU^*=WxW^* .
\tag{2.2}
\]
For \(s(n)\to\infty\), \((u_{s(n)})\) is again a \((\psi,\varphi)\)-sequence. Hence (2.2), for every \(\omega\), is the hypothesis of Lemma 1.1 of the flow lesson for \(y_n=u_nxu_n^*\) in \(M\): this sequence converges \(*\)-strongly to some \(\beta_{\psi,\varphi}(x)\in M\), equal to \(UxU^*\) in every \(M^\omega\), and by (2.2) independent of the sequence.

*Values in \(\mathrm B(\psi)\).* For \(Y=\pi(y_n)\) with \((y_n)\in A_{\psi,\omega}(N)\), Lemma 1.2(3) of the flow lesson in \(N\) gives \((u_n^*y_nu_n)\in A_{\varphi,\omega}(N)\), so \(U^*YU\in N_{\varphi,\omega}\) commutes with \(x\); hence \(Y\) commutes with \(UxU^*=\beta_{\psi,\varphi}(x)\). By Proposition 2.2 of the previous lesson, \(\beta_{\psi,\varphi}(x)\in\mathrm B(\psi)\).

*Algebraic properties.* \(x\mapsto UxU^*\) is an injective \(*\)-homomorphism; with \(u_n=1\), \(\beta_{\varphi,\varphi}=\mathrm{id}\). If \((v_n)\) is a \((\chi,\psi)\)-sequence, then \((v_nu_n)\) is a \((\chi,\varphi)\)-sequence and, with \(V=\pi(v_n)\), \(\beta_{\chi,\varphi}(x)=VUxU^*V^*=\beta_{\chi,\psi}(\beta_{\psi,\varphi}(x))\). So \(\beta_{\varphi,\psi}\) inverts \(\beta_{\psi,\varphi}\). Since \(U^*\bar\psi^\omega U=\bar\varphi^\omega\), \(\bar\psi(\beta_{\psi,\varphi}(x))=\bar\psi^\omega(UxU^*)=\bar\varphi(x)\). If \(x\in N'\cap M\), then \(u_nxu_n^*=x\).

*Intertwining.* Put \(c_n=u_n^*a_n\). Since \(u_n^*\psi-\varphi u_n^*=u_n^*(\psi-u_n\varphi u_n^*)\),
\[
\|[c_n,\varphi]\|\le\|a_n\varphi-\psi a_n\|+\|a_n\|\,\|\psi-u_n\varphi u_n^*\|\to0 ,
\]
so \((c_n)\in\mathrm{AC}(N,\varphi)\). Write \(a_nx-\beta_{\psi,\varphi}(x)a_n=u_nz_n\) with
\[
z_n=(c_nx-xc_n)+(x-u_n^*\beta_{\psi,\varphi}(x)u_n)c_n .
\]
The first term tends to \(0\) \(*\)-strongly, because \(x,x^*\in\mathrm B(\varphi)\). For the second, \(e_n=\beta_{\psi,\varphi}(x)-u_nxu_n^*\to0\) \(*\)-strongly, and by (1.1)
\[
\|u_n^*e_nu_n\|^2_{\bar\varphi}=(u_n\bar\varphi u_n^*)(e_n^*e_n)\le\bar\psi(e_n^*e_n)+\|e_n\|^2\|u_n\varphi u_n^*-\psi\|\to0 ,
\]
likewise for the adjoint; so \(u_n^*e_nu_n\to0\) \(*\)-strongly, and its product with \((c_n)\in A_{\bar\varphi,\omega}(M)\) tends to \(0\) \(*\)-strongly along every \(\omega\), because \(I_\omega\) is an ideal of \(A_{\bar\varphi,\omega}(M)\) (Theorem 5.1(5) of the ultraproduct lesson). Hence \(z_n\to0\) \(*\)-strongly. Finally, \((u_n)\in N_\omega\) for every \(\omega\) (Lemma 1.3 of the asymptotic centralizer lesson, with (1.1)), so \((u_nz_n)\in I_\omega\) for every \(\omega\), that is, \(u_nz_n\to0\) \(*\)-strongly. \(\square\)

**Corollary 2.2.** If \(\psi=v\varphi v^*\) for a unitary \(v\in N\), then \(\beta_{\psi,\varphi}(x)=vxv^*\).

**Proof.** The constant sequence \(v\) is a \((\psi,\varphi)\)-sequence. \(\square\)

## 3. The flow

Let \(\lambda>0\). A finite family of bounded sequences \((v_{k,n})_n\) in \(N\), \(1\le k\le m\), is an *admissible \(\lambda\)-family along \(\omega\)* for \(\varphi\) if
\[
\lim_\omega\|v_{k,n}\varphi-\lambda\varphi v_{k,n}\|=0\quad(1\le k\le m),\qquad\lim_\omega\Big\|1-\sum_kv_{k,n}v_{k,n}^*\Big\|^\sharp_{\varphi}=0 .
\]
The classes \(V_k\in M^\omega\) satisfy \(V_k\bar\varphi^\omega=\lambda\bar\varphi^\omega V_k\) and \(\sum_kV_kV_k^*=1\) (Section 1 and Lemma 1.1 of the previous lesson). By Proposition 4.1 of the asymptotic centralizer lesson applied to \((N,\varphi)\), admissible \(\lambda\)-families exist with ordinary convergence; for \(\lambda\le1\) one sequence suffices.

**Theorem 3.1.** For every \(\lambda>0\) there is a unital \(*\)-automorphism \(\beta^\varphi_\lambda\) of \(\mathrm B(\varphi)\) such that:

1. for every \(\omega\), every admissible \(\lambda\)-family along \(\omega\) and every \(x\in\mathrm B(\varphi)\), \(\sum_kV_kxV_k^*=\beta^\varphi_\lambda(x)\) in \(M^\omega\); for an admissible family with ordinary convergence, \(\sum_kv_{k,n}xv_{k,n}^*\to\beta^\varphi_\lambda(x)\) \(*\)-strongly;
2. for every bounded sequence \((w_n)\) in \(N\) with \(\|w_n\varphi-\lambda\varphi w_n\|\to0\) and every \(x\in\mathrm B(\varphi)\), \(w_nx-\beta^\varphi_\lambda(x)w_n\to0\) \(*\)-strongly; in particular \(wx=\beta^\varphi_\lambda(x)w\) for every \(w\in N\) with \(w\varphi=\lambda\varphi w\);
3. \(\beta^\varphi_1=\mathrm{id}\), \(\beta^\varphi_\lambda\beta^\varphi_\mu=\beta^\varphi_{\lambda\mu}\), and \(\bar\varphi\circ\beta^\varphi_\lambda=\bar\varphi\) on \(\mathrm B(\varphi)\);
4. \(\beta^\varphi_\lambda(x)\to x\) strongly as \(\lambda\to1\), for every \(x\in\mathrm B(\varphi)\); the action is continuous for the \(u\)-topology;
5. \(\beta^\psi_\lambda\circ\beta_{\psi,\varphi}=\beta_{\psi,\varphi}\circ\beta^\varphi_\lambda\);
6. \(\beta^\varphi_\lambda\circ\sigma^{\bar\varphi}_t=\sigma^{\bar\varphi}_t\circ\beta^\varphi_\lambda\) on \(\mathrm B(\varphi)\) for all \(t\in\mathbb R\);
7. \(\beta^\varphi_\lambda(x)=x\) for \(x\in N'\cap M\).

**Proof.** (1) Let \((v_{k,n})\), \((w_{l,n})\) be admissible \(\lambda\)-families along \(\omega\), with classes \(V_k,W_l\). By Lemma 1.2(1) of the flow lesson in \(N\), \((w_{l,n}^*v_{k,n})_n\in A_{\varphi,\omega}(N)\), so \(W_l^*V_k\in N_{\varphi,\omega}\) commutes with \(x\in\mathrm B(\varphi)\), and
\[
\sum_kV_kxV_k^*=\sum_{k,l}W_lW_l^*V_kxV_k^*=\sum_{k,l}W_lxW_l^*V_kV_k^*=\sum_lW_lxW_l^* .
\tag{3.1}
\]
For a family with ordinary convergence and \(s(n)\to\infty\), the reparametrized family is admissible along every \(\omega\); by (3.1) and Lemma 1.1 of the flow lesson, \(\sum_kv_{k,n}xv_{k,n}^*\) converges \(*\)-strongly to an element \(\beta^\varphi_\lambda(x)\in M\), equal to \(\sum_kV_kxV_k^*\) in every \(M^\omega\); by (3.1) every admissible family gives the same element.

*Values in \(\mathrm B(\varphi)\), multiplicativity.* Let \(Y=\pi(y_n)\) with \((y_n)\in A_{\varphi,\omega}(N)\). The sequence \((v_{k,n}^*y_nv_{l,n})_n\) lies in \(A_{\varphi,\omega}(N)\): writing \(v_k,y,v_l\) for the \(n\)-th terms,
\[
v_k^*yv_l\varphi\approx\lambda v_k^*y\varphi v_l\approx\lambda v_k^*\varphi yv_l\approx\varphi v_k^*yv_l ,
\]
with errors at most \(\|v_k\|\|y\|\,\|v_l\varphi-\lambda\varphi v_l\|\), \(\lambda\|v_k\|\|v_l\|\,\|[y,\varphi]\|\) and \(\|y\|\|v_l\|\,\|\lambda v_k^*\varphi-\varphi v_k^*\|\), where \(\|\lambda v_k^*\varphi-\varphi v_k^*\|=\|v_k\varphi-\lambda\varphi v_k\|\) by taking adjoints in \(N_*\). So \(x\) commutes with \(V_k^*YV_l\), and
\[
\beta^\varphi_\lambda(x)Y=\sum_{k,l}V_kxV_k^*YV_lV_l^*=\sum_{k,l}V_kV_k^*YV_lxV_l^*=Y\beta^\varphi_\lambda(x).
\]
By Proposition 2.2 of the previous lesson, \(\beta_\lambda^\varphi(x)\in\mathrm B(\varphi)\). With \(Y=1\), \(V_k^*V_l\in N_{\varphi,\omega}\) commutes with \(x\), so \(\beta^\varphi_\lambda(x)\beta^\varphi_\lambda(y)=\sum_{k,l}V_kxV_k^*V_lyV_l^*=\sum_{k,l}V_kV_k^*V_lxyV_l^*=\beta^\varphi_\lambda(xy)\). The map is linear, \(*\)-preserving, and unital since \(\sum_kV_kV_k^*=1\).

(3) The constant sequence \(1\) is an admissible \(1\)-family, so \(\beta^\varphi_1=\mathrm{id}\). If \((v_{k,n})\) is admissible for \(\lambda\) and \((w_{l,n})\) for \(\mu\), then \((v_{k,n}w_{l,n})\) is admissible for \(\lambda\mu\), since \(\|vw\varphi-\lambda\mu\varphi vw\|\le\|v\|\,\|w\varphi-\mu\varphi w\|+\mu\|v\varphi-\lambda\varphi v\|\,\|w\|\) and \(\sum_{k,l}V_kW_lW_l^*V_k^*=1\); hence \(\beta^\varphi_{\lambda\mu}=\beta^\varphi_\lambda\beta^\varphi_\mu\), and \(\beta^\varphi_\lambda\) is an automorphism with inverse \(\beta^\varphi_{1/\lambda}\). For state preservation, \(V_k^*V_k\in N_{\varphi,\omega}\) and Lemma 1.1 give
\[
\bar\varphi^\omega(V_kxV_k^*)=(\bar\varphi^\omega V_k)(xV_k^*)=\lambda^{-1}\bar\varphi^\omega(xV_k^*V_k)=\lambda^{-1}\bar\varphi(x)\tau(V_k^*V_k)=\bar\varphi(x)\bar\varphi^\omega(V_kV_k^*),
\]
using \(\bar\varphi^\omega(V_k^*V_k)=(V_k\bar\varphi^\omega)(V_k^*)=\lambda\bar\varphi^\omega(V_kV_k^*)\). Summing over \(k\), \(\bar\varphi(\beta^\varphi_\lambda(x))=\bar\varphi(x)\).

(2) Let \(W=\pi(w_n)\). By Lemma 1.2(1) of the flow lesson in \(N\), \(V_k^*W\in N_{\varphi,\omega}\), so \(Wx=\sum_kV_kV_k^*Wx=\sum_kV_kxV_k^*W=\beta^\varphi_\lambda(x)W\) in every \(M^\omega\); hence \(w_nx-\beta^\varphi_\lambda(x)w_n\to0\) \(*\)-strongly along every \(\omega\), so \(*\)-strongly. The last assertion is the case of a constant sequence.

(4) Let \(\lambda_j\to1\), \(\lambda_j\le1\). For each \(j\) take a single sequence \((v_{j,n})_n\) from Proposition 4.1 of the asymptotic centralizer lesson (with \(m=1\)) and choose \(n(j)\) so that \(w_j=v_{j,n(j)}\) satisfies \(\|w_j\varphi-\lambda_j\varphi w_j\|<1/j\), \(\|1-w_jw_j^*\|^\sharp_\varphi<1/j\) and \(\|w_jxw_j^*-\beta^\varphi_{\lambda_j}(x)\|^\sharp_{\bar\varphi}<1/j\). Then \(\|[w_j,\varphi]\|\le1/j+(1-\lambda_j)\|w_j\|\to0\), so along every \(\omega\) the class \(W\) lies in \(N_{\varphi,\omega}\) with \(WW^*=1\), and \(WxW^*=xWW^*=x\). Hence \(\beta^\varphi_{\lambda_j}(x)\to x\) \(*\)-strongly. For \(\lambda_j\ge1\), \(\|\beta^\varphi_{\lambda_j}(x)-x\|_{\bar\varphi}=\|x-\beta^\varphi_{1/\lambda_j}(x)\|_{\bar\varphi}\to0\), because \(\bar\varphi\)-preserving automorphisms preserve \(\|\cdot\|_{\bar\varphi}\). The \(\bar\varphi\)-preserving automorphisms \(\beta^\varphi_\lambda\) are implemented on \(L^2(\mathrm B(\varphi),\bar\varphi)\) by unitaries \(U_\lambda\) with \(U_\lambda x\bar\xi=\beta^\varphi_\lambda(x)\bar\xi\); these converge strongly to \(1\), which is continuity in the \(u\)-topology.

(5) If \((v_{k,n})\) is admissible for \(\varphi\) and \((u_n)\) is a \((\psi,\varphi)\)-sequence, then \((u_nv_{k,n}u_n^*)\) is admissible for \(\psi\), because \(\|uvu^*\psi-\lambda\psi uvu^*\|\le\|v\varphi-\lambda\varphi v\|+(1+\lambda)\|v\|\,\|u\varphi u^*-\psi\|\). In \(M^\omega\),
\[
\beta^\psi_\lambda(\beta_{\psi,\varphi}(x))=\sum_kUV_kU^*\,UxU^*\,UV_k^*U^*=U\beta^\varphi_\lambda(x)U^*=\beta_{\psi,\varphi}(\beta^\varphi_\lambda(x)).
\]

(6) By (1.1) of the previous lesson, \(\sigma^{\bar\varphi}_t\) restricts to \(\sigma^\varphi_t\) on \(N\), and \(\varphi\circ\sigma_t^\varphi=\varphi\) gives \(\|\sigma^\varphi_t(v)\varphi-\lambda\varphi\sigma^\varphi_t(v)\|=\|v\varphi-\lambda\varphi v\|\) and \(\|\sigma^\varphi_t(y)\|^\sharp_\varphi=\|y\|^\sharp_\varphi\). So if \((v_{k,n})\) is admissible with ordinary convergence, so is \((\sigma^\varphi_t(v_{k,n}))\). The normal automorphism \(\sigma^{\bar\varphi}_t\) preserves \(*\)-strong convergence of bounded sequences (it preserves \(\|\cdot\|^\sharp_{\bar\varphi}\)), so applying it to the convergence in (1),
\[
\sum_k\sigma^\varphi_t(v_{k,n})\,\sigma^{\bar\varphi}_t(x)\,\sigma^\varphi_t(v_{k,n})^*\to\sigma^{\bar\varphi}_t(\beta^\varphi_\lambda(x))\quad*\text{-strongly}.
\]
Since \(\sigma^{\bar\varphi}_t(x)\in\mathrm B(\varphi)\) (Theorem 2.3 of the previous lesson), the left side converges to \(\beta^\varphi_\lambda(\sigma^{\bar\varphi}_t(x))\) by (1).

(7) For \(x\in N'\cap M\), \(\sum_kv_{k,n}xv_{k,n}^*=x\sum_kv_{k,n}v_{k,n}^*\to x\). \(\square\)

We also use the logarithmic parametrization
\[
\gamma^\varphi_s=\beta^\varphi_{e^{-s}}\qquad(s\in\mathbb R).
\tag{3.2}
\]
An element \(v\in N\) with \(v\varphi=e^{-s}\varphi v\) is said to have *modular frequency* \(s\); Theorem 3.1(2) says that \(vx=\gamma^\varphi_s(x)v\) for \(x\in\mathrm B(\varphi)\). Corollary 1.3 of [Spectral shift maps](spectral-shift-maps.md) shows that this condition on \(v\) is equivalent to \(\sigma^\varphi_t(v)=e^{its}v\) for all \(t\). By Theorem 3.1, \(s\mapsto\gamma^\varphi_s\) is a continuous action of \(\mathbb R\) on \(\mathrm B(\varphi)\) by \(\bar\varphi\)-preserving automorphisms commuting with \(\sigma^{\bar\varphi}\) and fixing \(N'\cap M\).

## 4. A von Neumann algebra independent of the state

**Theorem 4.1.** For faithful normal states \(\varphi,\psi\) on \(N\),
\[
N\vee\mathrm B(\varphi)=N\vee\mathrm B(\psi).
\]
We denote this von Neumann algebra by \(\mathrm B^\sharp=\mathrm B^\sharp(N\subset M)\).

**Proof.** Let \(y\in\mathrm B(\psi)\) and \(x=\beta_{\varphi,\psi}(y)\in\mathrm B(\varphi)\), so \(y=\beta_{\psi,\varphi}(x)\). For a \((\psi,\varphi)\)-sequence \((u_n)\), Theorem 2.1 gives \(y=\lim u_nxu_n^*\) \(*\)-strongly, and \(u_nxu_n^*\in N\vee\mathrm B(\varphi)\), which is strongly closed. So \(\mathrm B(\psi)\subset N\vee\mathrm B(\varphi)\), and by symmetry the two algebras agree. \(\square\)

Both \(N\) and \(\mathrm B(\varphi)\) are globally invariant under \(\sigma^{\bar\varphi}\) (by (1.1) and Theorem 2.3 of the previous lesson), so \(\mathrm B^\sharp\) is, and the modular expectation theorem gives a \(\bar\varphi\)-preserving faithful normal conditional expectation \(E^\sharp\colon M\to\mathrm B^\sharp\).

**Proposition 4.2.** \(E\circ E^\sharp=E\). Consequently \(\bar\chi\circ E^\sharp=\bar\chi\) for every faithful normal state \(\chi\) on \(N\), and \(E^{\chi}_{\mathrm B}\circ E^\sharp=E^\chi_{\mathrm B}\), where \(E^\chi_{\mathrm B}\) is the \(\bar\chi\)-preserving expectation onto \(\mathrm B(\chi)\). In particular, if \(z\in M\) and \(E^\sharp(z)=0\), then \(E^\chi_{\mathrm B}(z)=0\) for every \(\chi\).

**Proof.** \(E\circ E^\sharp\) is a contractive retraction of \(M\) onto \(N\subset\mathrm B^\sharp\), and \(\varphi\circ E\circ E^\sharp=\bar\varphi\circ E^\sharp=\bar\varphi\). By uniqueness in the modular expectation theorem, \(E\circ E^\sharp=E\). Then \(\bar\chi\circ E^\sharp=\chi\circ E\circ E^\sharp=\bar\chi\). Finally \(E^\chi_{\mathrm B}\circ E^\sharp\) is a contractive retraction onto \(\mathrm B(\chi)\subset\mathrm B^\sharp\) preserving \(\bar\chi\), so it equals \(E^\chi_{\mathrm B}\). \(\square\)

## 5. Matrix amplifications

Let \(R\subset N\) be a subfactor isomorphic to \(M_k(\mathbb C)\), with matrix units \((e_{ij})\) and the same unit as \(N\). Put \(N_1=R'\cap N\) and \(M_1=R'\cap M\). The maps \(x\mapsto\sum_{i,j}e_{ij}\otimes e_{1i}xe_{j1}\) identify \(M\) with \(R\otimes M_1\) and \(N\) with \(R\otimes N_1\) (here \(e_{1i}xe_{j1}\) is read as an element of \(M_1\) through the isomorphism \(e_{11}Me_{11}\cong M_1\), \(y\mapsto\sum_ie_{i1}ye_{1i}\)). Since \(E\) is \(R\)-bimodular, it maps \(M_1\) into \(N_1\) and corresponds to \(\mathrm{id}_R\otimes E_1\) with \(E_1=E|_{M_1}\). The algebra \(N_1\cong e_{11}Ne_{11}\cong N\) is a factor of type III₁ with separable predual, since \(e_{11}\sim1\) in \(N\). Let \(\tau_R\) be the normalized trace of \(R\).

**Proposition 5.1.** For every faithful normal state \(\chi_1\) on \(N_1\),
\[
\mathrm B(N\subset M,\tau_R\otimes\chi_1)=1\otimes\mathrm B(N_1\subset M_1,\chi_1),
\qquad
\mathrm B^\sharp(N\subset M)=R\otimes\mathrm B^\sharp(N_1\subset M_1).
\]

**Proof.** Write \(\chi=\tau_R\otimes\chi_1\). For \(x=\sum_{i,j}e_{ij}\otimes x_{ij}\in N\) and \(z=\sum_{a,b}e_{ab}\otimes z_{ab}\),
\[
[x,\chi](z)=\frac1k\sum_{i,j}\big(\chi_1(z_{ji}x_{ij})-\chi_1(x_{ij}z_{ji})\big)=\frac1k\sum_{i,j}[x_{ij},\chi_1](z_{ji}),
\]
so \(\frac1k\max_{i,j}\|[x_{ij},\chi_1]\|\le\|[x,\chi]\|\le\frac1k\sum_{i,j}\|[x_{ij},\chi_1]\|\). Hence a bounded sequence in \(N\) lies in \(\mathrm{AC}(N,\chi)\) exactly when all its matrix entries lie in \(\mathrm{AC}(N_1,\chi_1)\). In particular the constant sequences \(e_{ij}\otimes1\) lie in \(\mathrm{AC}(N,\chi)\), so every \(a\in\mathrm B(N\subset M,\chi)\) commutes with \(R\) and has the form \(1\otimes a_1\), \(a_1\in M_1\). For such \(a\) and \(x_n=\sum e_{ij}\otimes x_{ij,n}\),
\[
\|[1\otimes a_1,x_n]\|^2_{\bar\chi}=\frac1k\sum_{i,j}\|[a_1,x_{ij,n}]\|^2_{\bar\chi_1},
\]
which tends to \(0\) for every \((x_n)\in\mathrm{AC}(N,\chi)\) exactly when \(a_1\in\mathrm B(N_1\subset M_1,\chi_1)\). This proves the first identity. By Theorem 4.1, applied to both inclusions,
\[
\mathrm B^\sharp(N\subset M)=N\vee(1\otimes\mathrm B(N_1\subset M_1,\chi_1))=R\otimes\big(N_1\vee\mathrm B(N_1\subset M_1,\chi_1)\big)=R\otimes\mathrm B^\sharp(N_1\subset M_1).\qquad\square
\]

## 6. Exercises

**Exercise 6.1.** Show that \(\beta_{\psi,\varphi}\) maps \(N'\cap M\) identically and that \(E^{\psi}_{N'\cap M}\circ\beta_{\psi,\varphi}=E^\varphi_{N'\cap M}\), where \(E^\varphi_{N'\cap M}\) is the \(\bar\varphi\)-preserving expectation onto \(N'\cap M\).

**Exercise 6.2.** In the situation of Exercise 4.2 of the previous lesson, \(N\otimes1\subset N\bar\otimes Q\), show that \(\beta^\varphi_\lambda=\mathrm{id}\) on \(1\otimes Q\) and that \(\mathrm B^\sharp=N\bar\otimes Q\).

**Exercise 6.3.** Let \(v\in N\) with \(v\varphi=\lambda\varphi v\) and \(x\in\mathrm B(\varphi)\). Show that \(xv^*=v^*\beta^\varphi_\lambda(x)\) and \(v^*vx=v^*\beta^\varphi_\lambda(x)v\).

**Exercise 6.4.** Show that \(\beta^\varphi_\lambda(E^\varphi_{N'\cap M}(x))=E^\varphi_{N'\cap M}(x)\) and \(E^\varphi_{N'\cap M}(\beta^\varphi_\lambda(x))=E^\varphi_{N'\cap M}(x)\) for \(x\in\mathrm B(\varphi)\).

## 7. Solutions

**6.1.** The first statement is in Theorem 2.1. Both \(E^\psi_{N'\cap M}\circ\beta_{\psi,\varphi}\) and \(E^\varphi_{N'\cap M}\) are maps \(\mathrm B(\varphi)\to N'\cap M\) fixing \(N'\cap M\) and \(N'\cap M\)-bimodular. For \(y\in N'\cap M\) and \(x\in\mathrm B(\varphi)\), \(\bar\psi(y^*\beta_{\psi,\varphi}(x))=\bar\psi(\beta_{\psi,\varphi}(y^*x))=\bar\varphi(y^*x)\), using \(\beta_{\psi,\varphi}(y)=y\), multiplicativity and state transport. On the other hand \(\bar\varphi(y^*z)=\bar\psi(y^*z)\) for \(y,z\in N'\cap M\): indeed \(E(y^*z)\in N'\cap N=\mathbb C1\), so \(\bar\varphi(y^*z)=E(y^*z)=\bar\psi(y^*z)\). Hence \(E^\psi_{N'\cap M}(\beta_{\psi,\varphi}(x))\) and \(E^\varphi_{N'\cap M}(x)\) have the same inner products with every \(y\in N'\cap M\) for the common state \(\bar\varphi|_{N'\cap M}=\bar\psi|_{N'\cap M}\), and they are equal.

**6.2.** By Exercise 4.2 of the previous lesson, \(\mathrm B(\varphi)=1\otimes Q\subset N'\cap(N\bar\otimes Q)\), and Theorem 3.1(7) applies. Then \(\mathrm B^\sharp=N\vee(1\otimes Q)=N\bar\otimes Q\).

**6.3.** By Theorem 3.1(2), \(vx=\beta^\varphi_\lambda(x)v\) for every \(x\in\mathrm B(\varphi)\); applied to \(x^*\) and taking adjoints, \(xv^*=v^*\beta^\varphi_\lambda(x)\). Multiplying \(vx=\beta^\varphi_\lambda(x)v\) on the left by \(v^*\) gives the second identity.

**6.4.** \(E^\varphi_{N'\cap M}(x)\in N'\cap M\) is fixed by Theorem 3.1(7). For the second identity recall that \(w\bar\xi\mapsto E^\varphi_{N'\cap M}(w)\bar\xi\) is the orthogonal projection onto the closure of \((N'\cap M)\bar\xi\), so it suffices that \(\beta^\varphi_\lambda(x)\) and \(x\) have the same inner products with every \(y\in N'\cap M\). Since \(N'\cap M\subset\mathrm B(\varphi)\) and \(\beta^\varphi_\lambda(y^*)=y^*\), Theorem 3.1(3) gives \(\bar\varphi(y^*\beta^\varphi_\lambda(x))=\bar\varphi(\beta^\varphi_\lambda(y^*x))=\bar\varphi(y^*x)\).

## References

- [AHHM] H. Ando, U. Haagerup, C. Houdayer, A. Marrakchi, Structure of bicentralizer algebras and inclusions of type III factors, Mathematische Annalen 376 (2020), 1145–1194. https://arxiv.org/abs/1804.05706
- [M1] A. Marrakchi, Kadison's problem for type III subfactors and the bicentralizer conjecture, Inventiones Mathematicae 239 (2025), 79–163. https://arxiv.org/abs/2308.15163
