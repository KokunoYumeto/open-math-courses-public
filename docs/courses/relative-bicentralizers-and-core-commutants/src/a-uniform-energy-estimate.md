# A uniform energy estimate

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The previous lesson defined the comparison contraction \(U=L^*R\) and the unitary \(D=\exp(iX\otimes Y)\) on \(L^2(N)\otimes L^2(\mathrm B)\), and words
\[
C=W_{d_n}U_nW_{d_{n-1}}\cdots W_{d_1}U_1W_{d_0},\qquad D_{\mathrm{all}}=W_d\exp(iS_n\otimes Y),
\]
on \(L^2(N)^{\otimes n}\otimes L^2(\mathrm B)\). This lesson proves that \(C\) and \(D_{\mathrm{all}}\) almost agree on vectors whose total modular energy \(S_n\) is concentrated in a short interval, with an error that depends on the length of the interval and on the vector in \(L^2(\mathrm B)\), but not on the number \(n\) of tensor factors, the shifts \(d_j\) or the position of the interval (Proposition 1.1) [OAI, Proposition 5.1]. The proof feeds the states \(T\mapsto\langle Z(T)\xi,\xi\rangle\) of the iterated kernel into the binormal identity; all of them live on the single algebra \(B(L^2(M))\), and compactness of its state space turns pointwise convergence into uniformity.

Two consequences are prepared for the next lesson: the same estimate for words in which some \(U_j\) are replaced by \(D_j\), or all of them by the averages \(G_j=(U_j+D_j)/2\) (Lemma 2.1), and a time-averaged version without any spectral restriction (Lemma 3.1) [OAI, Lemma 6.1].

We use: Theorem 5.1 of [Binormal states and the relative bicentralizer](binormal-states-and-the-relative-bicentralizer.md); the setting, Lemma 1.1, Lemma 3.1 and Proposition 4.1 of [The two relative products](the-two-relative-products.md); Theorem 2.3 of [The relative bicentralizer](the-relative-bicentralizer.md); (B6) of [Ultraproducts and the asymptotic centralizer](course:type-iii-factors/ultraproducts-and-the-asymptotic-centralizer#results-used-from-other-lessons); Theorem 9.1(3) of [Analytic elements and strip arguments](course:analytic-elements-strips-and-kms/analytic-elements-and-strip-arguments#9-entire-elements-of-automorphism-groups-of-von-neumann-algebras); the Banach–Alaoglu theorem, [Weak topologies, Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian); and the unitary Fourier transform and vector Plancherel identity, FF-2 and FF-3 of [Fourier and closed-form foundations for the state core](course:OA-FLOW/OA-FLOW-FF#OA-FLOW.FF.2).

## 1. The estimate

We keep the setting and notation of the previous lesson: \(N\) a factor of type III₁ with separable predual, \(N\subset M\) with expectation, \(M\) with separable predual, \(\mathcal H=L^2(M,\bar\varphi)\), \(\Omega\), \(\mathcal X=\log\Delta\), \(H\), \(K\), \(X\), \(W_s=e^{isY}\), \(U\), \(D\), the words \(C\) and \(D_{\mathrm{all}}\), and the kernel maps \(Z\). Functions of finitely many commuting self-adjoint operators are defined by their joint spectral measure; in particular \(D_{\mathrm{all}}=\exp(i(S_n+d)\otimes Y)\). For a vector \(\xi\) and a self-adjoint operator \(S\), the *\(S\)-spectral support* of \(\xi\) lies in a Borel set \(I\) if \(E_S(I)\xi=\xi\).

**Proposition 1.1** (uniform energy estimate). For every \(\eta\in K\) there is a nondecreasing function \(\epsilon_\eta\colon(0,\infty)\to[0,\infty)\), continuous from the right, with \(\epsilon_\eta(\delta)\to0\) as \(\delta\downarrow0\), such that
\[
\|(C-D_{\mathrm{all}})(\xi\otimes\eta)\|\le\epsilon_\eta(\delta)\,\|\xi\|
\tag{1.1}
\]
for every \(n\ge1\), all \(d_0,\ldots,d_n\in\mathbb R\), and every \(\xi\in H^{\otimes n}\) whose \(S_n\)-spectral support lies in an interval of length \(\delta\).

**Proof.** *Step 1: centred tests with analytic vectors.* Let \(a\in\mathrm B\) be entire analytic for \(\sigma=\sigma^{\bar\varphi}\) and \(a_+=\sigma_{i/2}(a)\). For \(\delta>0\) let \(g_a(\delta)\) be the supremum of
\[
\big|\langle C(\xi\otimes a\Omega),\xi\otimes a\Omega\rangle-\|a\Omega\|^2\big|
\]
over all \(n\), all \(d_0,\ldots,d_n\), and all unit vectors \(\xi\in H^{\otimes n}\) whose \((S_n+d)\)-spectral support lies in \([-\delta,\delta]\). We claim \(g_a(\delta)\to0\) as \(\delta\downarrow0\). Otherwise there are \(\varepsilon_0>0\), \(\delta_k\downarrow0\) and data \((n_k,d^{(k)},\xi_k)\) admissible for \(\delta_k\) with the displayed quantity at least \(\varepsilon_0\). Let \(Z_k\) be the kernel maps of these data and \(\Phi_k(T)=\langle Z_k(T)\xi_k,\xi_k\rangle\), states of \(B(\mathcal H)\). By Proposition 4.1(1) of the previous lesson, \(\Phi_k(y)=\Phi_k(\rho(y))=\bar\varphi(y)\) for \(y\in M\) and \(\Phi_k(e_N)=1\). By Proposition 4.1(3) there, for \(f\in C_0(\mathbb R)\),
\[
|\Phi_k(f(\mathcal X))-f(0)|=|\langle(f(S_{n_k}+d^{(k)})-f(0))\xi_k,\xi_k\rangle|\le\sup_{|u|\le\delta_k}|f(u)-f(0)|\to0 .
\]
The state space of \(B(\mathcal H)\) is weak\(^*\) compact, so a subnet of \((\Phi_k)\) converges weak\(^*\) to a state \(\Phi\) with \(\Phi(y)=\Phi(\rho(y))=\bar\varphi(y)\), \(\Phi(e_N)=1\) and \(\Phi(f(\mathcal X))=f(0)\) for \(f\in C_0(\mathbb R)\). By Theorem 5.1 of the lesson on binormal states, applied to \(a^*\in\mathrm B\) and \(a_+\in M\),
\[
\Phi(a^*\rho(a_+))=\langle a^*\Omega a_+,\Omega\rangle=\langle a^*\rho(a_+)\Omega,\Omega\rangle=\langle a^*a\Omega,\Omega\rangle=\|a\Omega\|^2 .
\]
But \(\Phi_k(a^*\rho(a_+))=\langle C_k(\xi_k\otimes a\Omega),\xi_k\otimes a\Omega\rangle\) by Proposition 4.1(4) of the previous lesson, and these numbers stay at distance at least \(\varepsilon_0\) from \(\|a\Omega\|^2\), a contradiction.

Since \(C\) is a contraction and \(\xi\) is a unit vector,
\[
\|C(\xi\otimes a\Omega)-\xi\otimes a\Omega\|^2\le2\|a\Omega\|^2-2\operatorname{Re}\langle C(\xi\otimes a\Omega),\xi\otimes a\Omega\rangle\le2g_a(\delta).
\]
For the ideal word, the product spectral measure of \(S_n+d\) and \(Y\) gives, with \(\nu_\xi\) the spectral measure of \(S_n+d\) at \(\xi\),
\[
\|D_{\mathrm{all}}(\xi\otimes\eta)-\xi\otimes\eta\|^2=\iint|e^{iuv}-1|^2\,d\nu_\xi(u)\,d\nu_\eta(v)=\int\|W_u\eta-\eta\|^2\,d\nu_\xi(u)\le\sup_{|u|\le\delta}\|W_u\eta-\eta\|^2 .
\]
Hence \(\|(C-D_{\mathrm{all}})(\xi\otimes a\Omega)\|\le e_a(\delta):=(2g_a(\delta))^{1/2}+\sup_{|u|\le\delta}\|W_ua\Omega-a\Omega\|\), and \(e_a(\delta)\to0\) as \(\delta\downarrow0\) by Step 1 and the strong continuity of \(W\).

*Step 2: general vectors of \(K\).* The vectors \(a\Omega\) with \(a\in\mathrm B\) entire analytic are dense in \(K\): for \(a\in\mathrm B\) the Gaussian averages \(a_k=\int\sqrt{k/\pi}\,e^{-kt^2}\sigma_t(a)\,dt\) lie in \(\mathrm B\), because \(\mathrm B\) is \(\sigma\)-weakly closed and \(\sigma\)-invariant (Theorem 2.3 of the first lesson), are entire analytic by Theorem 9.1(3) of the analytic elements lesson, and \(a_k\Omega=e^{-\mathcal X^2/4k}a\Omega\to a\Omega\) by (B6) and the spectral theorem. For \(\eta\in K\) put
\[
\epsilon'_\eta(\delta)=\inf\big\{2\|\eta-a\Omega\|+e_a(\delta):\ a\in\mathrm B\text{ entire analytic}\big\}.
\]
As \(C\) is a contraction and \(D_{\mathrm{all}}\) unitary, \(\|(C-D_{\mathrm{all}})(\xi\otimes\eta)\|\le\epsilon'_\eta(\delta)\) for unit \(\xi\) whose \((S_n+d)\)-spectral support lies in \([-\delta,\delta]\). Given \(\varepsilon>0\), choose \(a\) with \(2\|\eta-a\Omega\|<\varepsilon/2\); then \(\epsilon'_\eta(\delta)<\varepsilon\) for small \(\delta\). So \(\epsilon'_\eta(\delta)\to0\).

*Step 3: arbitrary intervals.* Let \(\xi\) be a unit vector whose \(S_n\)-spectral support lies in \([\alpha,\alpha+\delta]\). Put \(q=-\alpha-\delta/2-d\) and replace the last shift \(d_n\) by \(d_n+q\). This replaces \(C\) and \(D_{\mathrm{all}}\) by \(W_qC\) and \(W_qD_{\mathrm{all}}\), whose difference has the same norm on every vector, and the new total shift \(d+q\) centres the support of \(S_n+d+q\) on \(\xi\) in \([-\delta/2,\delta/2]\). Step 2 gives \(\|(C-D_{\mathrm{all}})(\xi\otimes\eta)\|\le\epsilon'_\eta(\delta)\), and homogeneity gives the bound \(\epsilon'_\eta(\delta)\|\xi\|\) for all \(\xi\). Finally let \(m(\delta)=\sup_{0<\delta'\le\delta}\epsilon'_\eta(\delta')\) and \(\epsilon_\eta(\delta)=\lim_{\delta'\downarrow\delta}m(\delta')\). Then \(\epsilon_\eta\ge\epsilon'_\eta\) is nondecreasing, continuous from the right, and tends to \(0\) at \(0\). \(\square\)

The uniformity is the point: the function \(\epsilon_\eta\) does not depend on \(n\), on the shifts or on \(\xi\), because a failure of uniformity would produce a limit state on the single algebra \(B(\mathcal H)\) contradicting the binormal identity.

## 2. Hybrid and averaged words

For a set \(P\subset\{1,\ldots,n\}\) let \(C_P\) be the word (3.1) of the previous lesson with \(U_j\) replaced by \(D_j\) for \(j\in P\). Let \(G_j=(U_j+D_j)/2\) and \(C_G\) the word with every \(U_j\) replaced by \(G_j\).

**Lemma 2.1** (hybrid words). The estimate (1.1), with the same function \(\epsilon_\eta\), holds for every \(C_P\) and for \(C_G\) in place of \(C\).

**Proof.** We prove the statement for \(C_P\) by induction on \(p=|P|\), for all \(n\), all shifts and all \(P\) of size \(p\) simultaneously. For \(p=0\) it is Proposition 1.1. If \(P=\{1,\ldots,n\}\), then \(C_P=D_{\mathrm{all}}\) by Lemma 3.1 of the previous lesson. So let \(1\le p<n\), assume the statement for \(p-1\), and fix \(j_0\in P\), \(\eta\), and \(\xi\) with \(S_n\)-spectral support in an interval \(I\) of length \(\delta\).

*Discretization.* Let \(\tau>0\), \(I_k=[k\tau,(k+1)\tau)\) and \(u_k=k\tau\) for \(k\in\mathbb Z\), and let \(E_k\) be the spectral projection of \(X_{j_0}\) for \(I_k\). Every factor of \(C_P\) and of \(D_{\mathrm{all}}\) either acts on positions other than \(j_0\) or is a function of \(X_{j_0}\) and \(Y\), so it commutes with every \(E_k\). Write \(C_P=A_{\mathrm{after}}D_{j_0}A_{\mathrm{before}}\) and let \(C^{(k)}=A_{\mathrm{after}}W_{u_k}A_{\mathrm{before}}\). Similarly \(D_{\mathrm{all}}=D_{j_0}D'\) with \(D'=W_d\exp(iS'\otimes Y)\), \(S'=S_n-X_{j_0}\), and let \(D^{(k)}=W_{u_k}D'\). The operator \(C^{(k)}\) acts as the identity on the \(j_0\)-th copy of \(H\), and on the remaining \(n-1\) copies and \(K\) it is a word \(C'_k\) of the same kind with the set \(P\setminus\{j_0\}\) of replaced positions and with the two shifts adjacent to position \(j_0\) merged into \(d_{j_0-1}+u_k+d_{j_0}\). Its ideal word is \(D^{(k)}\), since the shifts now add up to \(d+u_k\).

*The discretization error.* Put \(\chi=A_{\mathrm{before}}(\xi\otimes\eta)\) and \(u_\tau(x)=\sum_ku_k1_{I_k}(x)\). Since \(A_{\mathrm{after}}\) is a contraction and the ranges of the \(E_k\) are orthogonal,
\[
\sum_k\|(C_P-C^{(k)})E_k(\xi\otimes\eta)\|^2\le\sum_k\|(D_{j_0}-W_{u_k})E_k\chi\|^2=\big\|\big(e^{iX_{j_0}\otimes Y}-e^{iu_\tau(X_{j_0})\otimes Y}\big)\chi\big\|^2 .
\]
The function \((x,y)\mapsto e^{ixy}-e^{iu_\tau(x)y}\) is bounded by \(2\) and tends to \(0\) pointwise as \(\tau\to0\), so the right side tends to \(0\) by dominated convergence for the joint spectral measure. The same holds for \(\sum_k\|(D_{\mathrm{all}}-D^{(k)})E_k(\xi\otimes\eta)\|^2\), with \(\xi\otimes\eta\) in place of \(\chi\).

*The fibres.* The joint spectral measure of \(X_{j_0}\) and \(S'\) at \(E_k\xi\) lives on \(\{(x,s):x\in I_k,\ x+s\in I\}\), so the \(S'\)-spectral support of \(E_k\xi\) lies in the interval \(I-I_k\), of length \(\delta+\tau\). Expanding \(E_k\xi=\sum_le_l\otimes\xi_{k,l}\) along an orthonormal basis \((e_l)\) of the \(j_0\)-th copy of \(H\), every \(\xi_{k,l}\) has \(S'\)-spectral support in \(I-I_k\). The inductive hypothesis, applied to the words \(C'_k\) on \(n-1\) positions with \(p-1\) replaced positions, gives
\[
\|(C^{(k)}-D^{(k)})E_k(\xi\otimes\eta)\|^2=\sum_l\|(C'_k-D^{(k)})(\xi_{k,l}\otimes\eta)\|^2\le\epsilon_\eta(\delta+\tau)^2\,\|E_k\xi\|^2 .
\]

*Conclusion.* \(C_P-D_{\mathrm{all}}\) commutes with the \(E_k\), so \(\|(C_P-D_{\mathrm{all}})(\xi\otimes\eta)\|^2=\sum_k\|(C_P-D_{\mathrm{all}})E_k(\xi\otimes\eta)\|^2\). Writing each term as a sum of three and using the triangle inequality in \(\ell^2\),
\[
\|(C_P-D_{\mathrm{all}})(\xi\otimes\eta)\|\le\epsilon_\eta(\delta+\tau)\|\xi\|+\Big(\sum_k\|(C_P-C^{(k)})E_k(\xi\otimes\eta)\|^2\Big)^{1/2}+\Big(\sum_k\|(D_{\mathrm{all}}-D^{(k)})E_k(\xi\otimes\eta)\|^2\Big)^{1/2}.
\]
Let \(\tau\downarrow0\) and use the right continuity of \(\epsilon_\eta\).

For \(C_G\), expanding the product gives \(C_G=2^{-n}\sum_PC_P\), the sum over all subsets \(P\), so \(\|(C_G-D_{\mathrm{all}})(\xi\otimes\eta)\|\le2^{-n}\sum_P\|(C_P-D_{\mathrm{all}})(\xi\otimes\eta)\|\le\epsilon_\eta(\delta)\|\xi\|\). \(\square\)

## 3. Time averaging

**Lemma 3.1** (time averaging). For every \(\delta>0\) there is a continuous probability density \(p_\delta\) on \(\mathbb R\) such that, for every \(\eta\in K\), every \(n\), all shifts, every word \(C\), \(C_P\) or \(C_G\) as above (written \(C\)), and every \(\xi\in H^{\otimes n}\),
\[
\int_{\mathbb R}\big\|(C-D_{\mathrm{all}})(e^{itS_n}\xi\otimes\eta)\big\|^2p_\delta(t)\,dt\le\epsilon_\eta(\delta)^2\|\xi\|^2 .
\]

**Proof.** Choose a real \(g\in C_c^\infty(\mathbb R)\) vanishing outside \([-\delta/2,\delta/2]\) with \(\|g\|_2=1\), let \(\hat g(t)=(2\pi)^{-1/2}\int e^{itx}g(x)\,dx\) and \(p_\delta=|\hat g|^2\). It is continuous, and \(\int p_\delta=1\) by Plancherel's theorem (FF-2). Since \(g\) is real, \(|\hat g(-t)|=|\hat g(t)|\).

Let \(A\colon H^{\otimes n}\to H^{\otimes n}\otimes K\), \(A\xi'=(C-D_{\mathrm{all}})(\xi'\otimes\eta)\), a bounded operator. The function \(F(t)=\hat g(t)e^{-itS_n}\xi\) is continuous with \(\|F(t)\|=|\hat g(t)|\,\|\xi\|\), so it is integrable and square integrable, \(\hat g\) being a Schwartz function. By Fourier inversion for \(g\), \(g(x)=(2\pi)^{-1/2}\int\hat g(t)e^{-itx}dt\), and the spectral theorem,
\[
(2\pi)^{-1/2}\int e^{itz}F(t)\,dt=(2\pi)^{-1/2}\int\hat g(t)e^{-it(S_n-z)}\xi\,dt=g(S_n-z)\xi .
\]
The bounded operator \(A\) commutes with the vector integral, so \(z\mapsto Ag(S_n-z)\xi\) is the Fourier transform of the integrable and square-integrable function \(AF\). The vector Plancherel identity (FF-3) gives
\[
\int\|Ag(S_n-z)\xi\|^2dz=\int\|AF(t)\|^2dt=\int|\hat g(t)|^2\|Ae^{-itS_n}\xi\|^2dt=\int p_\delta(t)\,\|Ae^{itS_n}\xi\|^2dt .
\]
Each vector \(g(S_n-z)\xi\) has \(S_n\)-spectral support in \([z-\delta/2,z+\delta/2]\), an interval of length \(\delta\), so by Proposition 1.1 and Lemma 2.1, \(\|Ag(S_n-z)\xi\|\le\epsilon_\eta(\delta)\|g(S_n-z)\xi\|\). Finally, with \(\nu_\xi\) the spectral measure of \(S_n\) at \(\xi\) and Tonelli's theorem, \(\int\|g(S_n-z)\xi\|^2dz=\iint|g(s-z)|^2dz\,d\nu_\xi(s)=\|\xi\|^2\). \(\square\)

## 4. Exercises

**Exercise 4.1.** Show that for \(n=1\) and a vector \(\xi=x\Omega\) with \(x\in N\) an exact eigenoperator of frequency \(h\), \(C\) and \(D_{\mathrm{all}}\) agree on \(\xi\otimes\eta\) for every \(\eta\in K\), without using Proposition 1.1.

**Exercise 4.2.** Show that the function \(\epsilon_\eta\) of Proposition 1.1 can be chosen so that \(\epsilon_{c\eta}=|c|\epsilon_\eta\) for scalars \(c\), and \(\epsilon_{\eta_1+\eta_2}\le\epsilon_{\eta_1}+\epsilon_{\eta_2}\).

**Exercise 4.3.** In Lemma 3.1 take \(g=\delta^{-1/2}1_{[-\delta/2,\delta/2]}\) instead of a smooth function. Compute \(p_\delta\), and check that the proof still works when the Fourier transform of \(F\) is identified through the \(L^2\) Fourier transform.

## 5. Solutions

**4.1.** By Proposition 2.3 of the previous lesson, \(U(x\Omega\otimes\zeta)=x\Omega\otimes W_h\zeta\) for every \(\zeta\in K\). Hence \(C(x\Omega\otimes\eta)=W_{d_1}U(x\Omega\otimes W_{d_0}\eta)=x\Omega\otimes W_{d_1+h+d_0}\eta\). Since \(X\) acts on \(x\Omega\) as the scalar \(h\), \(D_{\mathrm{all}}(x\Omega\otimes\eta)=x\Omega\otimes W_{d+h}\eta\) with \(d=d_0+d_1\).

**4.2.** The left side of (1.1) is linear in \(\eta\). Define \(\tilde\epsilon_\eta(\delta)\) as the supremum of \(\|(C-D_{\mathrm{all}})(\xi\otimes\eta)\|\) over all admissible data with \(\|\xi\|=1\) and support length at most \(\delta\). It is the smallest admissible nondecreasing function, it is bounded by \(\epsilon_\eta\), it tends to \(0\), and it is homogeneous and subadditive in \(\eta\) because the left side is. Its right-continuous regularization, as at the end of the proof of Proposition 1.1, keeps these properties.

**4.3.** \(\hat g(t)=(2\pi)^{-1/2}\delta^{-1/2}\int_{-\delta/2}^{\delta/2}e^{itx}dx=(2\pi\delta)^{-1/2}\,\frac{2\sin(t\delta/2)}{t}\), so \(p_\delta(t)=\frac{2\sin^2(t\delta/2)}{\pi\delta t^2}\). The function \(F(t)=\hat g(t)e^{-itS_n}\xi\) is square integrable but not integrable. Its \(L^2\) Fourier transform is the \(L^2\) limit of the transforms of \(1_{[-T,T]}F\), which are \(g_T(S_n-z)\xi\) with \(g_T\) the truncated inverse transforms of \(\hat g\); these converge in \(L^2(\mathbb R,H^{\otimes n})\) to \(z\mapsto g(S_n-z)\xi\) by the spectral theorem and the scalar Plancherel identity. The rest of the proof is unchanged.

## References

- [OAI] OpenAI, Expected amenable subalgebras preserving core commutants (September 23, 2026), OpenAI Math Release preprint. https://github.com/openai/math/blob/main/preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026.pdf
