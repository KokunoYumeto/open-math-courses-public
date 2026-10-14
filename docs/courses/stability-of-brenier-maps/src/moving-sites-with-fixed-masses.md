# Moving sites with fixed masses

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Two finite targets are compared by moving the sites of one to the sites of the other along an optimal coupling, keeping the masses carried by the moving sites fixed. Along the way, the intercepts that realize these masses, constructed in [Laguerre cells and prescribed masses](laguerre-cells-and-prescribed-masses.md), move too. This lesson shows that they move slowly: their weighted speed is at most a constant times the speed of the sites, by the moment estimate of [A uniform estimate for cell moments](a-uniform-estimate-for-cell-moments.md). As a consequence the affine potentials of two finite targets differ by at most \(C\,W_2\) in \(L^2(\rho)\), linearly in the distance of the targets.

- The potential estimate for finite targets (Proposition 1.1).
- The estimate on the cube example (Section 2).

The lesson follows [OpenAI-BS, Section 5]. Throughout, \(K\subseteq B(0,R)\) is a compact convex set with nonempty interior and \(\rho\) its uniform probability measure; \(C_0=162\).

## 1. The potential estimate

**Proposition 1.1** ([OpenAI-BS, Proposition 5.1]). Let \(\mu\) and \(\nu\) be finitely supported probability measures in the ball \(B(0,L)\). There are finite affine maxima \(u_0\) and \(u_1\) with slopes in \(B(0,L)\), hence convex and \(L\)-Lipschitz, such that \(\nabla u_0=T_\mu\) and \(\nabla u_1=T_\nu\) almost everywhere and
\[
\|u_0-u_1\|_{L^2(\rho)}\le(1+\sqrt{C_0})RW_2(\mu,\nu) .
\]

*Proof.* *An optimal coupling.* The couplings of \(\mu\) and \(\nu\) are the nonnegative matrices with prescribed row and column sums on the finite supports, a compact set on which the cost is linear, so an optimal coupling exists. Deleting zero weights and combining identical pairs, write it as
\[
\begin{gathered}
\pi=\sum_{i=1}^Nm_i\,\delta_{(y_i^0,y_i^1)},\\
m_i>0,\quad\sum_im_i=1 ,
\end{gathered}
\]
with distinct pairs. Put \(w=W_2(\mu,\nu)\) and
\[
\begin{gathered}
v_i=y_i^1-y_i^0,\\
y_i(t)=(1-t)y_i^0+ty_i^1,\\
\sum_im_i|v_i|^2=w^2 .
\end{gathered}
\]

*The moving sites stay distinct.* Optimality implies
\[
(y_i^0-y_j^0)\cdot(y_i^1-y_j^1)\ge0 .
\]
Indeed, moving a mass \(\varepsilon\le\min(m_i,m_j)\) from the pairs \((y_i^0,y_i^1)\), \((y_j^0,y_j^1)\) to the pairs \((y_i^0,y_j^1)\), \((y_j^0,y_i^1)\) changes the cost by \(2\varepsilon(y_i^0-y_j^0)\cdot(y_i^1-y_j^1)\), which must not be negative. With \(a=y_i^0-y_j^0\) and \(b=y_i^1-y_j^1\), not both zero, and \(0<t<1\),
\[
\begin{aligned}
|y_i(t)-y_j(t)|^2&=(1-t)^2|a|^2+t^2|b|^2\\
&\quad+2t(1-t)\,a\cdot b>0 .
\end{aligned}
\]
So the sites \(y_i(t)\) are distinct for \(0<t<1\), even when some endpoint sites coincide. They lie in \(B(0,L)\).

*Intercepts and their speed.* By Proposition 2.1 of the lesson on Laguerre cells, for \(0<t<1\) there are unique intercepts \(c_i(t)\) with \(\sum_im_ic_i(t)=0\) whose cells have masses \(M_i(t)=m_i\), and they are continuously differentiable in \(t\). Fix \(t\) and let \(r_i=c_i'(t)\); then \(\sum_im_ir_i=0\). Differentiating \(M_i(c(t),y(t))=m_i\) gives \(DM_i[r,v]=0\) for every \(i\). For any intercept vector \(q\), the formulas of Proposition 1.1 of the lesson on Laguerre cells give
\[
\begin{aligned}
0&=\sum_iq_i\,DM_i[r,v]\\
&=\sum_{i<j}g_{ij}(q_i-q_j)(r_i-r_j)\\
&\quad+\sum_{i<j}(q_i-q_j)\,b_{ij}\cdot(v_i-v_j) ,
\end{aligned}
\]
and the two sums are \(\sum_ir_i\,DM_i[q,0]\) and \(\sum_iv_i\cdot DB_i[q,0]\). Hence
\[
\sum_ir_i\,DM_i[q,0]=-\sum_iv_i\cdot DB_i[q,0] .
\]
Since \(\sum_im_ir_i=0\), the range statement of that proposition gives a \(q\) with \(DM_i[q,0]=m_ir_i\) for all \(i\); no bound on \(q\) is needed. Put \(E_r=\sum_im_ir_i^2\). By the duality, weighted Cauchy–Schwarz and Proposition 2.1 of the lesson on cell moments, with \(M_i=m_i\),
\[
\begin{aligned}
E_r&\le\Bigl(\sum_im_i|v_i|^2\Bigr)^{1/2}\\
&\quad\times\Bigl(\sum_i\frac{|DB_i[q,0]|^2}{m_i}\Bigr)^{1/2}\\
&\le w\,\sqrt{C_0}R\Bigl(\sum_i\frac{|m_ir_i|^2}{m_i}\Bigr)^{1/2}\\
&=\sqrt{C_0}Rw\sqrt{E_r} .
\end{aligned}
\]
Hence
\[
\Bigl(\sum_im_ir_i^2\Bigr)^{1/2}\le\sqrt{C_0}\,R\,w ,
\]
also when \(E_r=0\); for \(N=1\) the normalization gives \(r_1=0\).

*The potentials.* Let \(u_t(x)=\max_i\bigl(x\cdot y_i(t)+c_i(t)\bigr)\). On compact subintervals of \((0,1)\), \(t\mapsto u_t(x)\) is Lipschitz uniformly in \(x\in K\), and at a strict maximum its derivative is \(x\cdot v_i+r_i\). For each \(t\) the ties are null, so by Fubini's theorem this formula holds for almost every \((t,x)\). The cell of index \(i\) has mass \(m_i\), so
\[
\begin{aligned}
\|\partial_tu_t\|_{L^2(\rho)}&\le R\Bigl(\sum_im_i|v_i|^2\Bigr)^{1/2}\\
&\quad+\Bigl(\sum_im_ir_i^2\Bigr)^{1/2}\\
&\le(1+\sqrt{C_0})\,R\,w .
\end{aligned}
\]
The fundamental theorem of calculus in \(t\), for each \(x\), and Minkowski's integral inequality give, for \(0<t,t'<1\),
\[
\begin{aligned}
&\|u_t-u_{t'}\|_{L^2(\rho)}\\
&\qquad\le(1+\sqrt{C_0})\,R\,w\,|t-t'| .
\end{aligned}
\]

*The endpoints.* For each \(i\), \(|c_i'(t)|\le\sqrt{C_0}Rw/\sqrt{m_i}\), so \(c_i(t)\) has limits at \(t=0\) and \(t=1\); this bound, which depends on the masses, is used only here. The maxima \(u_t\) converge uniformly on \(K\) to the maxima \(u_0\) and \(u_1\) of the limit affine functions, so the last inequality extends to \(t=0\), \(t'=1\). At \(t=0\), merge repeated slopes, keeping the largest intercept. Outside finitely many hyperplanes the maximizing slope of \(u_0\) is unique, and every maximizing slope of \(u_t\) at \(x\) converges to it as \(t\to0\): otherwise a sequence of times with one fixed maximizing index would contradict the strict gap at \(t=0\). For \(0<t<1\), the slope law is \((\nabla u_t)_\#\rho=\sum_im_i\delta_{y_i(t)}\); against a continuous test function, bounded convergence gives \((\nabla u_0)_\#\rho=\sum_im_i\delta_{y_i^0}=\mu\), and likewise \((\nabla u_1)_\#\rho=\nu\). By Lemma 2.1 of [Optimal maps of finite affine maxima](optimal-maps-of-finite-affine-maxima.md), these gradients are the optimal maps \(T_\mu\) and \(T_\nu\). \(\blacksquare\)

The argument never inverts the graph Laplacian quantitatively. It tests the constraint equation against the one direction \(q\) whose mass derivative is the weighted intercept velocity, and the moment estimate converts that test into a bound on the velocity itself.

## 2. The cube example

Return to \(K=Y=[-1,1]^d\) and the potentials \(u_a=\max\{-x_1,x_1,a\}\) and \(\tilde u_a=\max\{-x_1,x_1,a+bx_2\}\) of Proposition 4.1 of the first lesson, with \(0<a<\frac12\) and \(b=a/2\). The path \(\max\{-x_1,x_1,a+sbx_2\}\), \(0\le s\le1\), keeps the three cell masses fixed. Both potentials have weighted intercept mean \(a\cdot a=a^2\), and subtracting \(a^2\) from both normalizes them without changing their difference \(f=\tilde u_a-u_a\).

Let \(q=b|t|\) on the slice \(x_2=t\). For \(t\ge0\), \(f=q\) on the old central interval \(|x_1|<a\) and \(f=a+q-|x_1|\) on the added part \(a\le|x_1|<a+q\); for \(t<0\), \(f=-q\) on \(|x_1|<a-q\) and \(f=|x_1|-a\) on the removed part \(a-q\le|x_1|<a\). Integrating over \(x_1\) with density \(\frac12\),
\[
\mathbb E[f^2\mid x_2=t]=\begin{cases}aq^2+q^3/3,&t\ge0,\\ aq^2-2q^3/3,&t<0,\end{cases}
\]
and averaging over \(t\),
\[
\begin{aligned}
\|u_a-\tilde u_a\|_{L^2(\rho)}^2&=\frac{ab^2}3-\frac{b^3}{24}=\frac{5a^3}{64}\\
&=\frac5{16}\,W_2(\mu_a,\nu_a)^2 .
\end{aligned}
\]
So on this example the potentials are at distance exactly \(\sqrt{5/16}\,W_2\), while the maps are at distance of order \(W_2^{1/3}\). The next lesson shows that the passage from potentials to gradients always costs at most the exponent \(\frac13\).

## 3. Exercises

**3.1.** Verify the formula \(2\varepsilon(y_i^0-y_j^0)\cdot(y_i^1-y_j^1)\) for the change of cost under the swap in the proof of Proposition 1.1.

**3.2.** Give an example of an optimal coupling with two pairs whose first sites coincide, and check that the moving sites are distinct for \(0<t<1\).

**3.3.** Check the two cases of \(\mathbb E[f^2\mid x_2=t]\) and the average \(\frac{ab^2}3-\frac{b^3}{24}\) in Section 2.

**3.4.** Show that \(\sum_iv_i\cdot DB_i[q,0]\) equals \(\sum_{i<j}(q_i-q_j)\,b_{ij}\cdot(v_i-v_j)\).

**3.5.** Why does the proof need the intercept speed in the weighted norm \(\bigl(\sum_im_ir_i^2\bigr)^{1/2}\), and not the bound \(|c_i'|\le\sqrt{C_0}Rw/\sqrt{m_i}\) of the individual intercepts?

## 4. Solutions

**3.1.** The new cost minus the old one is \(\varepsilon\) times
\[
\begin{aligned}
&|y_i^0-y_j^1|^2+|y_j^0-y_i^1|^2\\
&\quad-|y_i^0-y_i^1|^2-|y_j^0-y_j^1|^2 .
\end{aligned}
\]
The squares \(|y|^2\) cancel, and the mixed terms give \(2\varepsilon\) times \(y_i^0\cdot y_i^1+y_j^0\cdot y_j^1-y_i^0\cdot y_j^1-y_j^0\cdot y_i^1\), which is \(2\varepsilon(y_i^0-y_j^0)\cdot(y_i^1-y_j^1)\).

**3.2.** \(\mu=\delta_0\), \(\nu=\frac12(\delta_{e_1}+\delta_{-e_1})\): the only coupling has pairs \((0,e_1)\) and \((0,-e_1)\), and \(y_1(t)=te_1\ne-te_1=y_2(t)\) for \(t>0\).

**3.3.** For \(t\ge0\) the conditional expectation is \(\frac12\bigl(2a\,q^2+2\int_0^q(q-s)^2ds\bigr)\), that is \(aq^2+q^3/3\). For \(t<0\) it is \(\frac12\bigl(2(a-q)q^2+2\int_0^q s^2ds\bigr)\), that is \(aq^2-2q^3/3\). Average with \(t\) uniform on \([-1,1]\) and \(q=b|t|\): the half \(t\ge0\) contributes \(\frac12\int_0^1(ab^2t^2+b^3t^3/3)\,dt\), which is \(\frac{ab^2}6+\frac{b^3}{24}\), and the half \(t<0\) contributes \(\frac12\int_0^1(ab^2t^2-2b^3t^3/3)\,dt\), which is \(\frac{ab^2}6-\frac{b^3}{12}\). The sum is \(\frac{ab^2}3-\frac{b^3}{24}\). With \(b=a/2\) this is \(\frac{a^3}{12}-\frac{a^3}{192}=\frac{5a^3}{64}\), and \(W_2^2=ab^2=\frac{a^3}4\).

**3.4.** \(DB_i[q,0]=\sum_{j\ne i}b_{ij}(q_i-q_j)\), so the left side is \(\sum_i\sum_{j\ne i}(q_i-q_j)\,b_{ij}\cdot v_i\); pairing the terms \((i,j)\) and \((j,i)\), with \(b_{ij}=b_{ji}\), gives \((q_i-q_j)\,b_{ij}\cdot(v_i-v_j)\).

**3.5.** The weighted norm is what bounds \(\|\partial_tu_t\|_{L^2(\rho)}\), because the cell of index \(i\) has mass \(m_i\). The individual bound blows up as \(m_i\to0\) and would give a constant depending on the smallest mass; it is used only to show that the intercepts have limits at the endpoints.

## References

- [OpenAI-BS] OpenAI, *Sharp one-third stability of Brenier maps*, OpenAI Math Release preprint, 25 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026
