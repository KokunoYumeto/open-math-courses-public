# Near normalizers at every time

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(M,N\) be a prepared pair with common vector \(\Omega\) and modular groups \(U_M(t)=\Delta_M^{it}\), \(U_N(t)=\Delta_N^{it}\). The unitaries \(W(t)=U_N(t)U_M(t)^*\) nearly normalize \(M\): conjugation by \(W(t)\) moves \(M\) by at most twice the completely bounded distance. This lesson proves that each \(W(t)\) is close to an exact normalizer of \(M\), with a bound uniform in \(t\) (Theorem 1.1). The proof makes the comparison of modular cuts into a statement about the frequency nest, replaces the field \(W\) by analytic multipliers, and smooths them into a norm-continuous path of approximate normalizers. The path is then factored by the infinitesimal estimates for type III factors, and a completely positive limit recovers an exact normalizer at each time [OpenAI-289, Section 7].

We use: [Close operator algebras](close-operator-algebras.md) (Lemmas 1.4 and 1.5); [Averaging and the completely positive criterion](averaging-and-the-completely-positive-criterion.md) (Lemma 1.1 and Proposition 4.1); [Preparing infinite factors](preparing-infinite-factors.md) (Definition 5.1); [Rescaled Tomita graphs](rescaled-tomita-graphs.md) (Corollary 3.1, with its constant \(C_{\rm cut}=2.1\cdot10^6\)); [Infinitesimal normalizers of type III factors](infinitesimal-normalizers-of-type-iii-factors.md) (Lemma 3.1 and the group \(\mathcal G_M\)); [Frequency nests and analytic multipliers](frequency-nests-and-analytic-multipliers.md) (the notation \(\mathcal K,P_a,C_s,M_F\), Lemmas 3.1 and 4.1 and Proposition 4.2); [Stone's theorem](course:analytic-elements-strips-and-kms/holomorphy-in-banach-spaces-stone-s-theorem-and-resolvent-convergence#4-stone-s-theorem) (a strongly continuous unitary group \(s\mapsto e^{isA}\) determines the spectral measure of its generator); and the [weak compactness of the unit ball of \(B(H)\)](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies#OA-FND-LT-10).

## 1. The statement

In this lesson \(C\) denotes absolute constants, whose values may change from one occurrence to the next, and \(\gamma_0>0\) an absolute threshold; all smallness conditions below are met by decreasing \(\gamma_0\).

**Theorem 1.1** (near normalizers). There are absolute constants \(\gamma_0>0\) and \(C\) such that, for every prepared pair \(M,N\subseteq B(H)\) with \(d_{\rm cb}(M,N)\le\gamma<\gamma_0\), and every \(t\in\mathbb R\), there is a unitary \(n_t\) with
\[
n_tMn_t^*=M,\qquad\|n_t-W(t)\|\le C\gamma .
\]

No measurability or continuity of \(t\mapsto n_t\) is claimed. Throughout the proof write \(L_P=\log\Delta_P\), so \(U_P(t)=e^{itL_P}\).

## 2. Initial approximate normalizers

**Lemma 2.1.** For every \(t\), \(k\ge1\) and \(x\in M_k(M)_1\),
\[
\begin{gathered}
\begin{aligned}
&\operatorname{dist}\bigl(W(t)^{(k)}xW(t)^{(k)*},M_k(M)_1\bigr)\\
&\quad \le2\gamma,
\end{aligned}\\
\begin{aligned}
&\operatorname{dist}\bigl(W(t)^{(k)*}xW(t)^{(k)},M_k(M)_1\bigr)\\
&\quad \le2\gamma .
\end{aligned}
\end{gathered}
\]
Consequently \(d_{\rm cb}(W(t)MW(t)^*,M)\le2\gamma\).

**Proof.** \(U_M(t)\) normalizes \(M\) and \(U_N(t)\) normalizes \(N\). Given \(x\), the element \(U_M(t)^*xU_M(t)\) lies in \(M_k(M)_1\); approximate it by \(y\in M_k(N)_1\) within \(\gamma\) plus a small slack; then \(U_N(t)yU_N(t)^*\in M_k(N)_1\) is within \(\gamma\) plus slack of some \(z\in M_k(M)_1\). So \(W(t)xW(t)^*\) is within \(2\gamma\) plus slack of \(z\). The second estimate approximates \(x\) by \(y\in M_k(N)_1\), then \(U_N(t)^*yU_N(t)\) by \(z\in M_k(M)_1\), and uses \(U_M(t)zU_M(t)^*\in M_k(M)_1\). The two estimates give the two directed distances between the unit balls of \(M_k(W(t)MW(t)^*)\) and \(M_k(M)\). \(\square\)

## 3. The frequency nest sees the modular comparison

On \(\mathcal K=L^2(\mathbb R,H)\) let \(\mathcal U_P\) be multiplication by the field \(t\mapsto U_P(t)\), for \(P=M,N\), and \(\mathcal W=\mathcal U_N\mathcal U_M^*\), multiplication by \(W\). Let \(T_s\) be the translation \((T_sf)(t)=f(t+s)\), so that \(P_a\) is the spectral projection of the generator of \(s\mapsto T_s\) for \((a,\infty)\).

**Lemma 3.1.** For every \(a\in\mathbb R\),
\[
\begin{gathered}
\|(1-P_a)C_1\mathcal WP_a\|\le C_{\rm cut}\gamma,\\
\|(1-P_a)C_1\mathcal W^*P_a\|\le C_{\rm cut}\gamma .
\end{gathered}
\]

**Proof.** A direct computation gives \(\mathcal U_P^*T_s\mathcal U_P=T_s\otimes U_P(s)\), because \(U_P(t)^*U_P(t+s)=U_P(s)\). So conjugation by \(\mathcal U_P\) carries the spectral projections of the generator of \(s\mapsto T_s\) to those of the generator of \(V_P(s)=T_s\otimes e^{isL_P}\). Under the Fourier transform in \(t\), \(T_s\) becomes multiplication by \(e^{is\xi}\), so \(V_P(s)\) becomes the decomposable unitary field \(\xi\mapsto e^{is(\xi+L_P)}\). The decomposable field of spectral projections \(\xi\mapsto1_B(\xi+L_P)\), \(B\) a Borel set, is a projection-valued measure whose unitary group is \(V_P\). By Stone's theorem it is the spectral measure of the generator of \(V_P\). Hence
\[
\begin{gathered}
\mathcal U_P^*P_a\mathcal U_P\ \text{has fibers}\\
1_{(a,\infty)}(\xi+L_P)=1_{(a-\xi,\infty)}(L_P).
\end{gathered}
\]
By (3.1) of the analytic multiplier lesson, \(C_1^*(1-P_a)C_1=1-P_{a-1}\), and so
\[
\begin{aligned}
&(1-P_a)C_1\mathcal WP_a\\
&\quad=C_1\mathcal U_N\bigl[\mathcal U_N^*(1-P_{a-1})\mathcal U_N\bigr]\\
&\qquad\cdot\bigl[\mathcal U_M^*P_a\mathcal U_M\bigr]\mathcal U_M^* .
\end{aligned}
\]
The bracketed product is decomposable with fibers \(1_{(-\infty,a-1-\xi]}(L_N)\,1_{(a-\xi,\infty)}(L_M)\). With \(b=a-\frac12-\xi\), this is a product of the cuts of Corollary 3.1 of [Rescaled Tomita graphs](rescaled-tomita-graphs.md) at \(b\mp\frac12\) (the open half-line gives a smaller projection), so each fiber has norm at most \(C_{\rm cut}\gamma\). By Lemma 4.1 of the analytic multiplier lesson the norm of a decomposable operator is the essential supremum of the norms of its fibers. The second estimate is the same with \(M\) and \(N\) exchanged, since \(\mathcal W^*=\mathcal U_M\mathcal U_N^*\). \(\square\)

## 4. Analytic multipliers and their extensions

Put \(\delta=C_{\rm cut}\gamma\), \(F(s)=e^{is}W(s)\) and \(\tilde F(s)=e^{is}W(s)^*\); then \(C_1\mathcal W=M_F\) and \(C_1\mathcal W^*=M_{\tilde F}\). By Lemma 3.1 and Proposition 4.2 of the analytic multiplier lesson there are analytic bounded fields \(B\) and \(S\) with
\[
\begin{gathered}
\|B-F\|_\infty\le\delta,\\
\|S-\tilde F\|_\infty\le\delta .\quad(4.1)
\end{gathered}
\]
Let \(B(z)\) and \(S(z)\), \(\operatorname{Im}z>0\), be their extensions (Lemma 3.1 there).

**Lemma 4.1.** For \(\operatorname{Im}z>0\), every \(k\) and every \(x\in M_k(M)_1\),
\[
\begin{aligned}
&\|B(z)S(z)-e^{2iz}\|\le2\delta+\delta^2,\\
&\|S(z)B(z)-e^{2iz}\|\le2\delta+\delta^2,\\
&\operatorname{dist}\bigl(B(z)^{(k)}xS(z)^{(k)},M_k(M)\bigr)\le\beta,\\
&\operatorname{dist}\bigl(S(z)^{(k)}xB(z)^{(k)},M_k(M)\bigr)\le\beta,
\end{aligned}
\]
where \(\beta=2\gamma+2\delta+\delta^2\).

**Proof.** On the boundary, \(F\tilde F=e^{2is}\), \(\|S\|_\infty\le1+\delta\), and \(BS-e^{2is}=(B-F)S+F(S-\tilde F)\) has norm at most \(2\delta+\delta^2\) almost everywhere. The scalar \(e^{2is}\) is an analytic field with extension \(e^{2iz}\), so by the product rule of Lemma 3.1 of the analytic multiplier lesson the extension of the analytic field \(BS-e^{2is}\) is \(B(z)S(z)-e^{2iz}\), and its norm is bounded by the boundary bound. The same holds for \(SB\).

For the second estimate, \(F^{(k)}x\tilde F^{(k)}=e^{2is}W(s)^{(k)}xW(s)^{(k)*}\) is within \(2\gamma\) of \(M_k(M)\) by Lemma 2.1, and \(\|B^{(k)}xS^{(k)}-F^{(k)}x\tilde F^{(k)}\|\le2\delta+\delta^2\); so on the boundary the distance is at most \(\beta\) almost everywhere. Let \(\omega\) be a normal functional on \(B(H^k)\) of norm at most \(1\) vanishing on \(M_k(M)\). The fields \(B^{(k)},S^{(k)}\) are analytic on \(L^2(\mathbb R,H^k)\), so the extension of \(B^{(k)}xS^{(k)}\) is \(B(z)^{(k)}xS(z)^{(k)}\), the Poisson integral of its boundary values; testing \(\omega\), a norm-convergent sum of vector functionals, gives
\[
\begin{aligned}
&|\omega(B(z)^{(k)}xS(z)^{(k)})|\\
&\quad \le\int\frac{r\,|\omega(B(s)^{(k)}xS(s)^{(k)})|}{\pi((t-s)^2+r^2)}\,ds\le\beta
\end{aligned}
\]
for \(z=t+ir\), since \(|\omega(y)|\le\operatorname{dist}(y,M_k(M))\). As \(M_k(M)\) is weak\* closed, the distance to it is the supremum of \(|\omega(y)|\) over such \(\omega\), by the Hahn–Banach theorem applied in the predual. The case \(S\,x\,B\) is the same. \(\square\)

## 5. A norm-continuous path

For \(z=t+ir\) with \(0<r\le\gamma\) put
\[
\begin{gathered}
A_r(t)=e^{-iz}B(z),\\
C_r(t)=e^{-iz}S(z).
\end{gathered}
\]
Since \(|e^{-iz}|=e^r\le e^\gamma\), Lemma 4.1 gives, uniformly in \(r,t,k\) and \(x\in M_k(M)_1\),
\[
\begin{aligned}
&\|A_r(t)\|,\ \|C_r(t)\|\le1+C\gamma,\\
&\|A_r(t)C_r(t)-1\|\le C\gamma,\\
&\|C_r(t)A_r(t)-1\|\le C\gamma,\\
&\operatorname{dist}\bigl(A_r(t)^{(k)}xC_r(t)^{(k)},M_k(M)\bigr)\\
&\qquad\le C\gamma,\quad(5.1)
\end{aligned}
\]
and the same with \(A_r\) and \(C_r\) exchanged in the last line.

*Polar parts.* For small \(\gamma\), \(A_rC_r\) and \(C_rA_r\) are invertible, so \(A_r(t)\) has a right and a left inverse, which agree, and \(\|A_r(t)^{-1}\|\le1+C\gamma\). With \(\|A_r(t)\|\le1+C\gamma\), the spectrum of \(|A_r(t)|\) lies in \([1-C\gamma,1+C\gamma]\), and the unitary polar part
\[
V_r(t)=A_r(t)\bigl(A_r(t)^*A_r(t)\bigr)^{-1/2}
\]
satisfies \(\|V_r(t)-A_r(t)\|=\|1-|A_r(t)|\|\le C\gamma\) and, comparing \(A_r(t)^{-1}=|A_r(t)|^{-1}V_r(t)^*\) with \(C_r(t)=A_r(t)^{-1}A_r(t)C_r(t)\), \(\|V_r(t)^*-C_r(t)\|\le C\gamma\). By (5.1), at every matrix level, \(V_r(t)xV_r(t)^*\) and \(V_r(t)^*xV_r(t)\) lie within \(C\gamma\) of \(M_k(M)\) for \(x\in M_k(M)_1\).

*Continuity.* For fixed \(r\), \(t\mapsto A_r(t)\) is norm continuous, by holomorphy of \(B\), and its inverses are bounded, so \(V_r\) is norm continuous by the continuous functional calculus. Put
\[
E_r(t)=V_r(t)V_r(0)^*,
\]
a norm-continuous unitary path with \(E_r(0)=1\). For \(x\in M_1\), \(V_r(0)^*xV_r(0)\) is within \(C\gamma\) of some \(m\in M\) with \(\|m\|\le1+C\gamma\), and \(V_r(t)mV_r(t)^*\) is within \(C\gamma\|m\|\) of \(M\); so
\[
\sup_{x\in M_1}\operatorname{dist}\bigl(E_r(t)xE_r(t)^*,M\bigr)\le C\gamma .
\]
\(M\) is a separably acting type III factor. Lemma 3.1 of [Infinitesimal normalizers of type III factors](infinitesimal-normalizers-of-type-iii-factors.md), applied to the path on the interval between \(0\) and \(t\), gives \(a_r(t)\in\mathcal U(M)\) and \(b_r'(t)\in\mathcal U(M')\) with
\[
\begin{aligned}
&\|E_r(t)-a_r(t)b_r'(t)\|\\
&\quad \le C\gamma ,\quad(5.2)
\end{aligned}
\]
where a slack of \(\gamma\) allows for an infimum that is not attained. No continuous choice of the factors is needed.

## 6. Back to the real axis

The field \(F_0(s)=e^{is}W(s)\) is strongly\* continuous, since modular groups are strongly continuous. Put
\[
D_r(t)=e^{-i(t+ir)}\int_{\mathbb R}\frac{r\,F_0(s)}{\pi((t-s)^2+r^2)}\,ds .
\]
By (3.2) of the analytic multiplier lesson and (4.1), \(\|A_r(t)-D_r(t)\|\le e^r\delta\), so
\[
\begin{gathered}
\|V_r(t)-D_r(t)\|\le C\gamma,\\
\|D_r(t)\|\le e^r .\quad(6.1)
\end{gathered}
\]
At every fixed \(t\), \(D_r(t)\to W(t)\) strongly\* as \(r\downarrow0\): on a fixed vector, split the integral into \(|s-t|<\eta\), where strong continuity controls \(F_0(s)\xi-F_0(t)\xi\), and the complement, whose Poisson mass tends to \(0\); the same holds for the adjoint field, and \(e^{-i(t+ir)}\to e^{-it}\). Since \(W(0)=1\) and all the operators are uniformly bounded,
\[
\begin{gathered}
Q_r(t)=D_r(t)D_r(0)^*\longrightarrow W(t)\\
\text{strongly}^*,
\end{gathered}
\]
and by (6.1), \(\|E_r(t)-Q_r(t)\|\le C\gamma\). This compares \(E_r(t)\) with a convergent family; it does not assert convergence of \(E_r(t)\).

## 7. A completely positive limit

**Proof of Theorem 1.1.** Fix \(t\) and a sequence \(r\downarrow0\). The maps \(\Phi_r(x)=a_r(t)xa_r(t)^*\) are UCP from \(M\) to \(M\), and \(\Phi_r\) is the restriction of \(\operatorname{Ad}(a_r(t)b_r'(t))\) because \(b_r'(t)\) commutes with \(M\). For operators \(T_1,T_2\), the maps \(x\mapsto T_1xT_1^*\) and \(x\mapsto T_2xT_2^*\) differ in completely bounded norm by at most \((\|T_1\|+\|T_2\|)\|T_1-T_2\|\). With (5.2) and Section 6,
\[
\begin{gathered}
\begin{aligned}
&\|\Phi_r^{(k)}(x)\\
&\qquad -Q_r(t)^{(k)}xQ_r(t)^{(k)*}\|\\
&\quad \le C\gamma\|x\|
\end{aligned}\\
(x\in M_k(M)).
\end{gathered}
\]
By Lemma 1.1 of the averaging lesson, a subnet of \((\Phi_r)\) converges pointwise in the weak operator topology to a UCP map \(\Phi:M\to M\); it need not be normal. For fixed \(x\), \(Q_r(t)xQ_r(t)^*\to W(t)xW(t)^*\) strongly, also at every matrix level, and norm balls are weakly closed, so
\[
\begin{gathered}
\|\Phi-\rho_t\|_{\rm cb}\le C\gamma,\\
\rho_t(x)=W(t)xW(t)^* .
\end{gathered}
\]
The representation \(\rho_t\) of \(M\) is faithful and normal, and by Lemma 2.1 every element of \(M_1\) is within \(2\gamma\) of \(\rho_t(M)_1\). For small \(\gamma\), Proposition 4.1 of the averaging lesson, with \(Q=M\), gives a unitary \(q_t\) with \(q_t\rho_t(M)q_t^*=M\) and \(\|q_t-1\|\le C\gamma\). Then \(n_t=q_tW(t)\) satisfies \(n_tMn_t^*=M\) and \(\|n_t-W(t)\|=\|q_t-1\|\le C\gamma\). All thresholds and constants were absolute. \(\square\)

## 8. Exercises

**Exercise 8.1.** Verify \(\mathcal U_P^*T_s\mathcal U_P=T_s\otimes U_P(s)\).

**Exercise 8.2.** Show that, for bounded operators \(T_1,T_2\), \(\|T_1xT_1^*-T_2xT_2^*\|\)\(\le(\|T_1\|+\|T_2\|)\|T_1-T_2\|\|x\|\), at every matrix level.

**Exercise 8.3.** Let \(V\subseteq B(K)\) be a weak\* closed subspace. Show that \(\operatorname{dist}(y,V)=\sup\{|\omega(y)|\}\) over normal functionals \(\omega\) of norm at most \(1\) vanishing on \(V\).

**Exercise 8.4.** Show that an invertible \(A\) with \(\|A\|\le1+\epsilon\) and \(\|A^{-1}\|\le1+\epsilon\) has polar part \(V\) with \(\|V-A\|\le\epsilon\).

**Exercise 8.5.** Explain why the proof does not use a continuous or measurable choice of \(t\mapsto n_t\), and where Section 2 of the next lesson removes the need for one.

## 9. Solutions

**Solution 8.1.** \((\mathcal U_P^*T_s\mathcal U_Pf)(t)\)\(=U_P(t)^*U_P(t+s)f(t+s)\)\(=U_P(s)f(t+s)\).

**Solution 8.2.** \(T_1xT_1^*-T_2xT_2^*\)\(=(T_1-T_2)xT_1^*+T_2x(T_1-T_2)^*\); amplification preserves norms.

**Solution 8.3.** \(V\) is the annihilator of its preannihilator \(V_\perp\) in the predual, by the Hahn–Banach theorem in the predual, and the quotient \(B(K)/V\) is isometrically the dual of \(V_\perp\). So the quotient norm of \(y\) is the norm of the functional \(\omega\mapsto\omega(y)\) on \(V_\perp\).

**Solution 8.4.** The spectrum of \(|A|\) lies in \([(1+\epsilon)^{-1},1+\epsilon]\subseteq[1-\epsilon,1+\epsilon]\), and \(V-A=V(1-|A|)\).

**Solution 8.5.** Each \(n_t\) is produced separately, through a cluster point of a sequence in \(r\) at that \(t\). The next lesson averages the family \(t\mapsto n_t\) with an invariant mean on \(\mathbb R_d\), which needs no measurability, and recovers continuity at the end from an intertwining relation with the modular group of \(N\).

## References

- [OpenAI-289] OpenAI, Universal strong Kadison–Kastler stability, preprint, 23 September 2026, Section 7. https://github.com/openai/math/tree/main/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026
