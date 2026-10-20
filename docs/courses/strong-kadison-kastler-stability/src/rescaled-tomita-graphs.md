# Rescaled Tomita graphs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a prepared pair \(M,N\) with common vector \(\Omega\), each algebra has its Tomita operator \(S_P\), the closure of \(x\Omega\mapsto x^*\Omega\), and its modular operator \(\Delta_P=S_P^*S_P\). This lesson shows that a small completely bounded distance between \(M\) and \(N\) forces the graphs of the rescaled operators \(cS_P\) to be close, uniformly in \(c>0\) (Proposition 2.1). Bounding a single element in operator norm would lose this uniformity as \(c\to0\) or \(c\to\infty\). Instead a graph vector is first flattened by random signs and Haar unitaries, then replicated into a row, where closeness at one matrix level supplies the estimate. A consequence is that the spectral projections of \(\log\Delta_M\) and \(\log\Delta_N\) for separated half-lines are almost orthogonal (Corollary 3.1). This is the comparison of the two modular actions on which the next lessons build [OpenAI-289, Section 6].

We use: [Close operator algebras](close-operator-algebras.md) (Exercise 5.4 and Lemma 1.4); [Preparing infinite factors](preparing-infinite-factors.md) (Definition 5.1 and the identity (5.1)); the Tomita–Takesaki theorem for a faithful normal state, [Modular time from a faithful normal state](course:OA-MOD/OA-MOD-FS); and the [fixed-point criterion](course:OA-MOD/OA-MOD-CZ#recognize-exactly-the-fixed-observations) for centralizers.

## 1. Graphs and their symmetries

Fix a prepared pair \(M,N\subseteq B(H)\) with vector \(\Omega\), state \(\varphi=\langle\cdot\,\Omega,\Omega\rangle\) and subfactor \(R=(\bigcup_jR_j)''\). Let \(\overline H\) be the conjugate Hilbert space, with vectors \(\bar\xi\) and \(\alpha\bar\xi=\overline{\bar\alpha\xi}\); an operator \(T\) on \(H\) gives the operator \(\bar T\bar\xi=\overline{T\xi}\) on \(\overline H\). For \(P\in\{M,N\}\), \(c>0\) and any \(x\in B(H)\) put
\[
g_c(x)=\bigl(x\Omega,\;c\,\overline{x^*\Omega}\bigr)\in H\oplus\overline H .
\]
This is complex linear in \(x\). Let \(E_c^P\) be the orthogonal projection onto the closure of \(\{g_c(x):x\in P\}\), which is the graph of the closed linear operator \(cS_P\), followed by \(\xi\mapsto\bar\xi\), from \(H\) to \(\overline H\). Also \(\|g_c(x)\|^2=\varphi(x^*x)+c^2\varphi(xx^*)\).

**Lemma 1.1** (common symmetries). For unitaries \(r,s\in R\) let \(\rho_s=J_Ms^*J_M=J_Ns^*J_N\), right multiplication by \(s\), and
\[
U_{r,s}=r\rho_s\oplus\overline{s^*\rho_{r^*}} .
\]
Then \(U_{r,s}\) is unitary, \(g_c(rxs)=U_{r,s}g_c(x)\) for every \(x\in B(H)\) commuting with \(\rho_s\) and \(\rho_{r^*}\), and both projections \(E_c^M,E_c^N\) commute with every \(U_{r,s}\). Moreover, for \(x\in M\) or \(x\in N\), the Haar averages \(E_j(x)=\int_{\mathcal U(R_j)}uxu^*\,du\) converge weakly to \(\varphi(x)1\).

**Proof.** The two expressions for \(\rho_s\) agree by Definition 5.1(3) of the preparation lesson, and \(\rho_s\) commutes with \(M\) and \(N\). For \(x\in P\), \(rxs\Omega=r\rho_sx\Omega\) and \((rxs)^*\Omega=s^*x^*r^*\Omega=s^*\rho_{r^*}x^*\Omega\), which gives the formula; the same computation applies to any \(x\) commuting with \(\rho_s\) and \(\rho_{r^*}\). The adjoint of \(U_{r,s}\) is \(U_{r^*,s^*}\), so each graph closure is invariant under a self-adjoint group of unitaries and reduces it. For the averages: every weak operator cluster point of \(E_j(x)\) commutes with all \(R_j\), hence lies in \(R'\cap P=\mathbb C1\), and \(\varphi(E_j(x))=\varphi(x)\) because \(R\) lies in the centralizer of \(\varphi\). \(\square\)

## 2. Uniform comparison of the graphs

**Proposition 2.1** (uniform graph comparison). Every prepared pair with \(d_{\rm cb}(M,N)\le\gamma\) satisfies
\[
\sup_{c>0}\|E_c^M-E_c^N\|\le5\cdot10^5\,\gamma .
\]

**Proof.** Put \(T=(1-E_c^N)E_c^M\). By Lemma 1.1, \(T\) commutes with every \(U_{r,s}\). We first treat \(c=\sqrt k\) with \(k\in\mathbb N\), and we may suppose \(T\ne0\).

*A flattened element with the signal.* Choose \(x\in M\) with \(\|g_c(x)\|=1\) and \(\|Tg_c(x)\|\ge\frac12\|T\|\); this is possible since the vectors \(g_c(x)\), \(x\in M\), are dense in the range of \(E_c^M\). Write \(\alpha=\varphi(x^*x)\) and \(\beta=\varphi(xx^*)\), so \(\alpha+k\beta=1\). Choose independent Haar unitaries \(u_i,v_i\) of \(R_j\) and independent fair signs \(\epsilon_i\), \(i\le m\), and put
\[
x_i=u_ixv_i,\qquad y=m^{-1/2}\textstyle\sum_{i=1}^m\epsilon_ix_i .
\]
By Lemma 1.1, \(Tg_c(x_i)=U_{u_i,v_i}Tg_c(x)\), so all the vectors \(w_i=Tg_c(x_i)\) have norm \(s_0=\|Tg_c(x)\|\). For Hilbert space vectors, \(\mathbb E_\epsilon\|\sum_i\epsilon_iw_i\|^2=\sum_i\|w_i\|^2\) and, expanding the fourth power over the three pairings of indices, \(\mathbb E_\epsilon\|\sum_i\epsilon_iw_i\|^4\le3(\sum_i\|w_i\|^2)^2\). So \(Z=\|Tg_c(y)\|^2\) has \(\mathbb E_\epsilon Z=s_0^2\) and \(\mathbb E_\epsilon Z^2\le3s_0^4\). The Cauchy–Schwarz inequality applied to \(Z1_{\{Z\ge\mathbb EZ/2\}}\) gives \(\mathbb P(Z\ge\mathbb EZ/2)\ge(\mathbb EZ)^2/(4\,\mathbb EZ^2)\ge1/12\). Hence, for every choice of the unitaries, with sign probability at least \(1/12\),
\[
\|Tg_c(y)\|\ge\frac{\|T\|}{2\sqrt2}.
\tag{2.1}
\]

*Fourth moments of the element.* The unitaries of \(R\) preserve \(\varphi\), so \(\mathbb E\varphi(y^*y)=\alpha\), \(\mathbb E\varphi(yy^*)=\beta\) and \(\mathbb E\|g_c(y)\|^2=1\). Expand \(\varphi((y^*y)^2)\) and take the sign expectation. The terms with all four indices equal contribute \(m^{-1}\varphi((x^*x)^2)\). For distinct \(i,l\), use that elements of \(R\) can be moved cyclically under \(\varphi\), and that \(v_iv_l^*\) and \(u_i^*u_l\) are Haar distributed:
\[
\begin{aligned}
\mathbb E\varphi(x_i^*x_ix_l^*x_l)&=\varphi\bigl(x^*x\,E_j(x^*x)\bigr)\to\alpha^2,\\
\mathbb E\varphi(x_i^*x_lx_l^*x_i)&=\varphi\bigl(x^*E_j(xx^*)x\bigr)\to\alpha\beta,
\end{aligned}
\]
as \(j\to\infty\), by Lemma 1.1 applied to \(\langle E_j(x^*x)\Omega,x^*x\Omega\rangle\) and \(\langle E_j(xx^*)x\Omega,x\Omega\rangle\). The third pairing is bounded by the second: \(|\varphi(a^2)|\le\varphi(aa^*)^{1/2}\varphi(a^*a)^{1/2}\) with \(a=x_i^*x_l\), and the two factors have equal expectations after exchanging \(i\) and \(l\). The same computation for \(yy^*\) exchanges \(\alpha\) and \(\beta\). Since \(\alpha\le1\), \(k\beta\le1\) and \(k\ge1\), the weighted off-diagonal limit satisfies
\[
\alpha^2+2\alpha\beta+k\beta^2+2k\alpha\beta\le6 .
\]
Choose \(m\) with \(m^{-1}(\varphi((x^*x)^2)+k\varphi((xx^*)^2))\le1\), and then \(j\) so large that the off-diagonal contribution is at most \(7\). Then
\[
\begin{aligned}
&\mathbb E\bigl[\|g_c(y)\|^2+\varphi((y^*y)^2)+k\varphi((yy^*)^2)\bigr]\\
&\quad \le10 .\quad(2.2)
\end{aligned}
\]
By Markov's inequality the bracket exceeds \(240\) with probability at most \(1/24<1/12\). So some realization satisfies both (2.1) and the bound \(240\) for the bracket.

*Clipping.* For \(b>0\) let \(f_b(t)=\min(1,b/t)\) and \(f_b(0)=1\). Put \(z=y\,f_{K_1}(|y|)\) with \(K_1=4\sqrt{480}\). With the polar decomposition \(y=w|y|\), \((y-z)^*(y-z)\)\(=|y|^2(1-f_{K_1}(|y|))^2\le|y|^4/K_1^2\) and \((y-z)(y-z)^*\le w|y|^4w^*/K_1^2\)\(=(yy^*)^2/K_1^2\), because \(t(1-f_b(t))\le t^2/b\). Hence
\[
\begin{aligned}
&\|g_c(y-z)\|^2\\
&\quad\le K_1^{-2}\bigl[\varphi((y^*y)^2)+k\varphi((yy^*)^2)\bigr]\\
&\quad\le\frac{240}{K_1^2},
\end{aligned}
\]
and with \(a_0=1/(4\sqrt2)\), since \(\sqrt{240}/K_1=a_0\),
\[
\begin{aligned}
\|Tg_c(z)\|&\ge\Bigl(\frac1{2\sqrt2}-\frac{\sqrt{240}}{K_1}\Bigr)\|T\|\\
&=a_0\|T\|.
\end{aligned}
\]
Also \(\|z\|\le K_1\), \(\alpha_z:=\varphi(z^*z)\le\varphi(y^*y)\le240\) and \(\beta_z:=\varphi(zz^*)\le\varphi(yy^*)\le240/k\).

*A row.* A single element of norm \(K_1\) would still cost \(\sqrt k\,K_1\gamma\) on the second leg of the graph. To avoid this, let \(r_1,\dots,r_k\) be independent Haar unitaries of a large \(R_{j'}\) and form the row and its square
\[
\begin{gathered}
Y=[\,r_1z\ \cdots\ r_kz\,]\in M_{1,k}(M),\\
A=YY^*=\textstyle\sum_ir_izz^*r_i^* .
\end{gathered}
\]
For rows of vectors use the normalized norm \(\|(\eta_i)\|_{\rm av}^2=k^{-1}\sum_i\|\eta_i\|^2\). Since \(Tg_c(r_iz)=U_{r_i,1}Tg_c(z)\), the row \((Tg_c(Y_i))_i\) has normalized norm at least \(a_0\|T\|\) for every choice of the \(r_i\). As before, as \(j'\to\infty\),
\[
\begin{aligned}
&\mathbb E\varphi(A^2)\to k\varphi((zz^*)^2)+k(k-1)\beta_z^2,\\
&\mathbb E\,k^{-1}\textstyle\sum_i\varphi(Y_i^*AY_i)\\
&\qquad\to\varphi((z^*z)^2)+(k-1)\alpha_z\beta_z .
\end{aligned}
\]
With \(\varphi((zz^*)^2)\le K_1^2\beta_z\) and \(\varphi((z^*z)^2)\le K_1^2\alpha_z\), both limits are at most \(240K_1^2+240^2\). Choose \(j'\) and a realization with
\[
\begin{aligned}
&\varphi(A^2)+k^{-1}\textstyle\sum_i\varphi(Y_i^*AY_i)\le C_1:\\
&\quad =3.81\cdot10^6 .
\end{aligned}
\]

*Clipping the row.* Put \(X=f_{K_2}(A^{1/2})Y\), so \(\|X\|\le K_2\), and \(Q=1-f_{K_2}(A^{1/2})\), so \(Q^2\le A/K_2^2\) and \(Y-X=QY\). Since \(c^2=k\),
\[
\begin{aligned}
&k^{-1}\textstyle\sum_i\|g_c(Y_i-X_i)\|^2\\
&\quad =k^{-1}\sum_i\varphi(Y_i^*Q^2Y_i)\\
&\qquad +\varphi(QAQ)\le C_1/K_2^2 .
\end{aligned}
\]
Choose \(K_2=2\sqrt{C_1}/a_0\). Then
\[
\begin{aligned}
\|(Tg_c(X_i))_i\|_{\rm av}&\ge\Bigl(a_0-\frac{\sqrt{C_1}}{K_2}\Bigr)\|T\|\\
&=\frac{a_0}2\|T\| .\quad(2.3)
\end{aligned}
\]

*Comparison at one matrix level.* Since \(d_{\rm cb}(M,N)\le\gamma\), there is a row \(Z\in M_{1,k}(N)\) with \(\|X-Z\|\le K_2\gamma\), up to an arbitrarily small slack (Exercise 5.4 of [Close operator algebras](close-operator-algebras.md) and compression to the first row). For any row \([e_i]\) of operators with norm at most \(\eta\),
\[
\begin{aligned}
&k^{-1}\textstyle\sum_i\|g_c(e_i)\|^2\\
&\quad =k^{-1}\sum_i\varphi(e_i^*e_i)+\varphi\bigl(\sum_ie_ie_i^*\bigr)\\
&\quad \le2\eta^2 .
\end{aligned}
\]
Since \(g_c(X_i)\) lies in the range of \(E_c^M\) and \(g_c(Z_i)\) in that of \(E_c^N\),
\[
\begin{aligned}
&\|(Tg_c(X_i))_i\|_{\rm av}\\
&\quad =\|((1-E_c^N)g_c(X_i-Z_i))_i\|_{\rm av}\\
&\quad \le\sqrt2K_2\gamma .
\end{aligned}
\]
With (2.3), \(\|(1-E_c^N)E_c^M\|\le(2\sqrt2K_2/a_0)\gamma\)\(=16K_2\gamma\le3.534\cdot10^5\gamma\). The same holds with \(M\) and \(N\) exchanged, and for orthogonal projections \(\|E-F\|\) is the larger of \(\|(1-F)E\|\) and \(\|(1-E)F\|\).

*All rescalings.* The antiunitary flip \(\Theta(\xi,\bar\eta)=(\eta,\bar\xi)\) of \(H\oplus\overline H\) satisfies \(\Theta g_c(x)=c\,g_{1/c}(x^*)\), so it carries the graph for \(c\) onto the graph for \(1/c\), for both algebras, and the bound holds for \(c=1/\sqrt k\). For \(c\ge1\) let \(k=\lfloor c^2\rfloor\); then \(r=c/\sqrt k\in[1,\sqrt2)\), and \(1\oplus r\) maps the graphs for \(\sqrt k\) onto those for \(c\). An invertible operator \(V\) multiplies the one-sided gap \(\|(1-F)E\|\) between subspaces by at most \(\|V\|\|V^{-1}\|\), here at most \(\sqrt2\). For \(0<c<1\) use \(1/c\) and the flip. Hence \(\sup_c\|E_c^M-E_c^N\|\)\(\le\sqrt2\cdot3.534\cdot10^5\gamma\le5\cdot10^5\gamma\). \(\square\)

## 3. Separated spectral cuts

**Corollary 3.1** (logarithmic modular cuts). For a prepared pair with \(d_{\rm cb}(M,N)\le\gamma\), put \(L_P=\log\Delta_P\). For every \(a\in\mathbb R\),
\[
\begin{aligned}
&\bigl\|1_{(-\infty,a-1/2]}(L_N)\,1_{[a+1/2,\infty)}(L_M)\bigr\|\\
&\quad \le2.1\cdot10^6\,\gamma ,
\end{aligned}
\]
and the same holds with \(M\) and \(N\) exchanged.

**Proof.** The projection onto the graph of a closed operator \(A\) has upper left entry \((1+A^*A)^{-1}\). For the graph of \(cS_P\) followed by conjugation, \(A^*A=c^2\Delta_P\), so the upper left entry of \(E_c^P\) is \((1+c^2\Delta_P)^{-1}=g(L_P+2\log c)\) with \(g(s)=(1+e^s)^{-1}\). Taking \(c=e^{-a/2}\), Proposition 2.1 gives
\[
\|g(L_M-a)-g(L_N-a)\|\le5\cdot10^5\gamma .
\]
Let \(p=1_{(-\infty,a-1/2]}(L_N)\), \(q=1_{[a+1/2,\infty)}(L_M)\), and regard \(X=pq\) as an operator from \(qH\) to \(pH\). Let \(A_0\) and \(B_0\) be the restrictions of \(g(L_N-a)\) to \(pH\) and of \(g(L_M-a)\) to \(qH\); since \(g\) is decreasing, \(A_0\ge g(-1/2)\) and \(B_0\le g(1/2)\). As \(p\) commutes with \(g(L_N-a)\) and \(q\) with \(g(L_M-a)\),
\[
\begin{aligned}
&A_0X-XB_0\\
&\quad=p\bigl(g(L_N-a)-g(L_M-a)\bigr)q\\
&\quad=:D_0,\qquad\|D_0\|\le5\cdot10^5\gamma .
\end{aligned}
\]
Differentiating \(t\mapsto e^{-tA_0}Xe^{tB_0}\), which tends to \(0\) since \(\|e^{-tA_0}\|\|e^{tB_0}\|\le e^{-t(g(-1/2)-g(1/2))}\), gives
\[
\begin{gathered}
X=\int_0^\infty e^{-tA_0}D_0e^{tB_0}\,dt,\\
\|X\|\le\frac{\|D_0\|}{g(-1/2)-g(1/2)} .
\end{gathered}
\]
Here \(g(-1/2)-g(1/2)=\tanh(1/4)>0.24\). Exchanging the algebras gives the other estimate. \(\square\)

## 4. Exercises

**Exercise 4.1.** Let \(w_1,\dots,w_m\) be vectors in a Hilbert space and \(\epsilon_i\) independent fair signs. Prove \(\mathbb E\|\sum_i\epsilon_iw_i\|^4\le3(\sum_i\|w_i\|^2)^2\).

**Exercise 4.2.** Prove the Paley–Zygmund bound used above: for a random variable \(Z\ge0\) with \(0<\mathbb EZ^2<\infty\), \(\mathbb P(Z\ge\mathbb EZ/2)\ge(\mathbb EZ)^2/(4\,\mathbb EZ^2)\).

**Exercise 4.3.** Let \(A\) be a closed densely defined operator from \(H\) to \(K\). Show that the orthogonal projection onto its graph has upper left entry \((1+A^*A)^{-1}\).

**Exercise 4.4.** For two orthogonal projections \(E,F\), show that \(\|E-F\|\) is the larger of \(\|(1-F)E\|\) and \(\|(1-E)F\|\).

**Exercise 4.5.** In the matrix example \(M=M_2(\mathbb C)\) with the state of density \(h=\operatorname{diag}(\frac23,\frac13)\), compute \(\log\Delta\) on the matrix units and its spectrum.

## 5. Solutions

**Solution 4.1.** Expanding, \(\mathbb E\|\sum\epsilon_iw_i\|^4\)\(=\sum_{i,j,k,l}\mathbb E[\epsilon_i\epsilon_j\epsilon_k\epsilon_l]\langle w_i,w_j\rangle\langle w_k,\)\(w_l\rangle\). Only the pairings \(i=j,k=l\), \(i=k,j=l\) and \(i=l,j=k\) survive, with the all-equal terms counted once. Each pairing is at most \((\sum\|w_i\|^2)^2\) by \(|\langle w_i,w_j\rangle|\le\|w_i\|\|w_j\|\).

**Solution 4.2.** \(\mathbb EZ\le\mathbb E[Z1_{\{Z<\mathbb EZ/2\}}]\)\(+\mathbb E[Z1_{\{Z\ge\mathbb EZ/2\}}]\le\frac12\mathbb EZ\)\(+(\mathbb EZ^2)^{1/2}\mathbb P(Z\ge\mathbb EZ/2)^{1/2}\).

**Solution 4.3.** The graph is the range of the injective operator \(\xi\mapsto(\xi,A\xi)\) on the domain. The vector \((\eta,0)\) decomposes as \(((1+A^*A)^{-1}\eta,A(1+A^*A)^{-1}\eta)\) plus \((\eta-(1+A^*A)^{-1}\eta,-A(1+A^*A)^{-1}\eta)\), and the second vector is orthogonal to every \((\xi,A\xi)\) because \(A^*A(1+A^*A)^{-1}\eta=\eta-(1+A^*A)^{-1}\eta\).

**Solution 4.4.** \(E-F=E(1-F)-(1-E)F\), and the two terms map into orthogonal subspaces from orthogonal subspaces, so the norm of their sum is the maximum of their norms; and \(\|E(1-F)\|=\|(1-F)E\|\).

**Solution 4.5.** \(\Delta x=hxh^{-1}\), so \(\Delta e_{12}=2e_{12}\), \(\Delta e_{21}=\frac12e_{21}\) and \(\Delta e_{ii}=e_{ii}\). The spectrum of \(\log\Delta\) is \(\{-\log2,0,\log2\}\).

## References

- [OpenAI-289] OpenAI, Universal strong Kadison–Kastler stability, preprint, 23 September 2026, Section 6. https://github.com/openai/math/tree/main/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026
