# A clock with registers

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson builds the map of the counterexample and proves that it is continuously differentiable. The map has three kinds of coordinates. A circle coordinate \(t\) is a *clock*: it advances by at most one per step, and it can slow down only near one reading. A sphere coordinate \(z\), the *main coordinate*, usually squares: \(z\mapsto z^2\). Further sphere coordinates \(v_1,\ldots,v_q\), the *registers*, store small complex signals. Early in each clock period the map writes into the registers predictions of the phase that \(z\) will have at a later readout; registers multiply their contents by a large gain \(L\) at every step; at the readout the map adds the amplified signals to \(z^2\). The signals are aligned with \(z^2\), so they push \(|z|\) up instead of disturbing it. The difficulty is regularity: a prediction \(m\) steps ahead involves the phase \((z/|z|)^{2^{m+1}}\), whose derivative is of order \(2^m\), and \(m\) is unbounded. Weighting the \(m\)-th prediction by \(L^{1-m}\) makes the series continuously differentiable; the gains restore its size before the readout. The next lesson analyses the orbits.

We use from the core course [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20) (Lebl, *Basic Analysis*): the extreme value theorem ([Theorem 7.5.6](https://www.jirka.org/ra/html/sec_metcont.html)), differentiation of uniformly convergent sequences ([Theorem 6.2.10](https://www.jirka.org/ra/html/sec_liminter.html#thm_dersconverge)), the chain rule ([Theorem 8.3.7](https://www.jirka.org/ra/html/sec_svtheder.html)) and the criterion that a map is continuously differentiable when its partial derivatives exist and are continuous ([Proposition 8.4.6](https://www.jirka.org/ra/html/sec_svthedercont.html#mv_prop_contdiffpartials)). From [Local tools for bundles and transport](course:DG-FND/local-tools-for-bundles-and-transport) we use Theorem 3.1: for a closed set \(K\) in a smooth manifold and an open neighbourhood \(U\) of \(K\) there is a smooth function with values in \([0,1]\), equal to one near \(K\) and with support in \(U\). We call such a function a *cutoff for \((K,U)\)*.

## 1. The Riemann sphere and the manifold

The Riemann sphere \(\Sigma=\mathbb C\cup\{\infty\}\) has two charts: the coordinate \(z\) on \(\mathbb C\), and the coordinate \(w=1/z\) on \(\Sigma\setminus\{0\}\), with \(w(\infty)=0\). On their overlap \(\mathbb C\setminus\{0\}\) the transition \(w=1/z\) is smooth with smooth inverse, so \(\Sigma\) is a compact smooth surface. A map of \(\Sigma\) is smooth at \(\infty\) when its expression in \(w\) is smooth at \(w=0\); for example \(z\mapsto z^2\), with \(\infty\mapsto\infty\), reads \(w\mapsto w^2\) there.

We measure tangent vectors of \(\Sigma\) by the **round metric**: a tangent vector with coordinate velocity \(\dot z\) at a finite point \(z\) has length \(2|\dot z|/(1+|z|^2)\). In the chart \(w\) the same vector has velocity \(\dot w=-\dot z/z^2\) and
\[
\frac{2|\dot w|}{1+|w|^2}=\frac{2|\dot z|/|z|^2}{(|z|^2+1)/|z|^2}=\frac{2|\dot z|}{1+|z|^2},
\]
so the formula is the same in both charts and defines a continuous norm on every tangent space, including at \(\infty\). On \(\mathbb R\times\Sigma\) we use the product norm \(\|(\dot t,\xi)\|=(\dot t^2+\|\xi\|^2)^{1/2}\). For a \(C^1\) map \(\Psi\) between such spaces, \(\|D\Psi(x)\|\) denotes the operator norm of its derivative at \(x\) with respect to these norms. By the chain rule (Lebl, Theorem 8.3.7, applied in charts) \(D(\Psi_2\circ\Psi_1)(x)=D\Psi_2(\Psi_1x)\,D\Psi_1(x)\), hence
\[
\|D(\Psi_2\circ\Psi_1)(x)\|\leq\|D\Psi_2(\Psi_1x)\|\,\|D\Psi_1(x)\|.\tag{1.1}
\]
On a compact subset of a chart domain these norms are comparable with the Euclidean norms of coordinate velocities: the factor \(2/(1+|z|^2)\) is bounded above and below by positive constants there.

Fix an integer \(q\geq2\) (the construction below works with \(q=2\)). The manifold of the counterexample is
\[
M=(\mathbb R/100\mathbb Z)\times\Sigma\times\Sigma^q,\qquad\text{coordinates }(t,z,v_1,\ldots,v_q),
\]
a compact smooth manifold of dimension \(2q+3\). We use \(t\) also for a real lift of the clock.

## 2. The clock

**Lemma 2.1 (the clock barrier).** There is a smooth \(100\)-periodic function \(b:\mathbb R\to[0,1]\) such that

(i) \(b(t)=0\) exactly when \(t\equiv50\pmod{100}\);

(ii) \(b(t)=1\) when \(|t-50|\geq2\), for \(t\in[0,100]\);

(iii) \(t+b(t)\leq50\) for \(0\leq t\leq50\).

*Proof.* Let \(\eta\) be a cutoff for \(([-1,1],(-2,2))\) on \(\mathbb R\), and on \([0,100]\) put
\[
b(t)=\eta(t-50)\,\frac{(t-50)^2}4+1-\eta(t-50).
\]
Near \(t=0\) and \(t=100\) we have \(\eta(t-50)=0\), so \(b=1\) there and the \(100\)-periodic extension is smooth. Write \(x=t-50\). If \(|x|\geq2\), then \(\eta(x)=0\) and \(b=1\); this is (ii). If \(|x|\leq2\), then \(b\) is a convex combination of \(x^2/4\in[0,1]\) and \(1\), so \(b\in[0,1]\). If \(\eta(x)<1\) then \(b\geq1-\eta(x)>0\); if \(\eta(x)=1\) then \(b=x^2/4\), which vanishes only at \(x=0\); this gives (i). For (iii) put \(y=50-t\in[0,50]\); we need \(b\leq y\). If \(y\leq1\), then \(\eta=1\) and \(b=y^2/4\leq y\). If \(1\leq y\leq2\), then \(b\leq\max\{y^2/4,1\}\leq y\). If \(y\geq2\), then \(b=1\leq y\). \(\square\)

Let \(e:\Sigma\to[0,1]\) be a cutoff for \((\{|z|\geq\tfrac34\}\cup\{\infty\},\ \{|z|>\tfrac12\}\cup\{\infty\})\); thus \(e=0\) on \(\{|z|\leq\tfrac12\}\) and \(e=1\) on \(\{|z|\geq\tfrac34\}\cup\{\infty\}\). The **clock increment** is
\[
h(t,z)=b(t)+(1-b(t))\,e(z).\tag{2.1}
\]
It is smooth and \(100\)-periodic in \(t\), and \(0\leq h\leq1\), \(h\geq b\), with \(h=1\) whenever \(b(t)=1\) or \(e(z)=1\). The clock can therefore slow down only near \(t\equiv50\), and only while \(|z|<\tfrac34\).

## 3. Cutoffs and register saturation

Fix the following smooth functions.

1. \(\alpha:\mathbb R\to[0,1]\), a cutoff for \(([9,11],(8,12))\): the **preparation** window.
2. \(\beta_1,\ldots,\beta_q:\mathbb R\to[0,1]\), the **readout** windows, with supports in open intervals \(J_\ell\subset(74,80)\) of length less than one, such that
\[
\text{for every }t\in[76,77]\text{ some }\ell\text{ has }\beta_\ell(t)=1.\tag{3.1}
\]
For \(q=2\) take \(J_1=(75.9,76.6)\), \(J_2=(76.4,77.1)\) and let \(\beta_\ell\) be a cutoff for \(([76,76.5],J_1)\), respectively \(([76.5,77],J_2)\). For larger \(q\) put \(\beta_\ell=0\) for \(\ell\geq3\) (or use a finer cover). Write \(\bar\beta_\ell(t)=\sum_{k\in\mathbb Z}\beta_\ell(t-100k)\) for the \(100\)-periodization; its translates have disjoint supports, so \(0\leq\bar\beta_\ell\leq1\).
3. \(\chi:\Sigma\to[0,1]\), a cutoff for \((\{\tfrac12\leq|z|\leq1\},\{\tfrac14<|z|<2\})\); it vanishes near \(0\) and near \(\infty\).

In the formulas below the functions \(\beta_\ell\) on the real line, and not their periodizations, are used for predictions: only predicted readings in \(J_\ell\subset(74,80)\) count.

The constant \(L\) is chosen in Section 4, depending only on \(h\). Once it is fixed, choose:

4. A smooth \(p:[0,\infty)\to[0,3]\) with \(p(r)=r\) for \(0\leq r\leq1\), \(p\) nondecreasing on \([0,3L]\), and \(p(r)=0\) for all large \(r\). To construct it, let \(\psi\) be a cutoff on \(\mathbb R\) for \(((-\infty,1],(-\infty,2))\), put \(p_0(r)=\int_0^r\psi\), which equals \(r\) on \([0,1]\), is nondecreasing and is at most \(2\); let \(\phi\) be a cutoff for \(([0,3L],(-1,3L+1))\) and put \(p=\phi\,p_0\).
5. The **saturation** \(S:\Sigma\to\mathbb C\),
\[
S(v)=p(|v|)\frac v{|v|}\quad(0<|v|<\infty),\qquad S(0)=S(\infty)=0.\tag{3.2}
\]
It equals \(v\) on the closed unit disc (so it is smooth near \(0\)), it is smooth where \(0<|v|<\infty\), and it vanishes for \(|v|\geq3L+1\) (so it is smooth near \(\infty\)). Moreover \(|S|\leq3\).
6. A smooth \(100\)-periodic **gain** \(a:\mathbb R\to[0,L]\) with \(a=0\) on \([2,5]\) and \(a=L\) on \([7,90]\): \(L\) times the periodization of a cutoff for \(([7,90],(6,96))\).

## 4. The prediction map and the gain

To predict later clock readings, we drop the readout additions and use the smooth map
\[
G:\mathbb R\times\Sigma\to\mathbb R\times\Sigma,\qquad G(t,z)=(t+h(t,z),\,z^2),\qquad T_m=\mathrm{pr}_1\circ G^m\quad(m\geq1).\tag{4.1}
\]
Here the clock is a real number, not a reading modulo \(100\). Since \(h\) is \(100\)-periodic, \(G\) commutes with \((t,z)\mapsto(t+100,z)\), and so does the continuous function \(x\mapsto\|DG(x)\|\). On the compact set \([0,100]\times\Sigma\) it is bounded (Lebl, Theorem 7.5.6); hence there is \(B\geq1\) with \(\|DG\|\leq B\) everywhere. By (1.1), and because the projection \(\mathrm{pr}_1\) has derivative of norm at most one,
\[
\|D(G^m)\|\leq B^m,\qquad\|DT_m\|\leq B^m\qquad(m\geq1).\tag{4.2}
\]
Fix the **gain**
\[
L>\max\{B,2\}.\tag{4.3}
\]
The bound \(L>B\) will control the derivatives of the predicted clock readings and \(L>2\) those of the predicted phases.

## 5. The inputs and the map

For \(k\geq1\) let \(\Phi_k(z)=\chi(z)\,(z/|z|)^k\) for \(z\in\mathbb C\setminus\{0\}\), and \(\Phi_k(0)=\Phi_k(\infty)=0\); these are smooth complex functions on \(\Sigma\), vanishing near both poles. For \(1\leq\ell\leq q\), \(t\in\mathbb R\) and \(z\in\Sigma\) define the **input**
\[
U^\circ_\ell(t,z)=\frac{\alpha(t)}{10}\sum_{m=1}^{\infty}L^{1-m}\,\beta_\ell\bigl(T_m(t,z)\bigr)\,\Phi_{2^{m+1}}(z),\tag{5.1}
\]
and let \(U_\ell(t,z)=\sum_{k\in\mathbb Z}U^\circ_\ell(t-100k,z)\) be its \(100\)-periodization. Since \(\alpha\) is supported in \((8,12)\), at most one translate is nonzero at any \(t\), and \(U_\ell=U^\circ_\ell\) for \(0\leq t<100\). The index \(m\) counts iterates of \(G\), not clock units.

**Definition 5.1 (the map).** Define \(f:M\to M\), \(f(t,z,v_1,\ldots,v_q)=(t',z',v_1',\ldots,v_q')\), by
\[
\begin{aligned}
t'&=t+h(t,z)\pmod{100},\\
z'&=z^2+20\sum_{\ell=1}^q\bar\beta_\ell(t)\,S(v_\ell)\quad(z\neq\infty),\qquad z'=\infty\quad(z=\infty),\\
v_\ell'&=a(t)\,S(v_\ell)+U_\ell(t,z)\qquad(1\leq\ell\leq q).
\end{aligned}\tag{5.2}
\]
All right-hand sides use the old state. Every register output is a complex number, in the affine chart. When the clock reading lies in \([2,5]\) modulo \(100\), both \(a(t)\) and \(U_\ell(t,z)\) vanish, so **every register is reset to zero**, whatever its value was.

*How the timing is meant to work.* Write \(z_i\) for the main coordinate at step \(i\). An input computed at step \(i\) enters its register at step \(i+1\). If it is read out at step \(i+m\), it has received \(m-1\) gains in between. If the gain is \(L\) throughout and the register stays in the unit disc, where \(S\) is the identity, the factor \(L^{1-m}\) is exactly cancelled. If moreover \(z\) squares exactly in between, its phase at step \(i+m\) is \((z_i/|z_i|)^{2^m}\), so the phase of \(z_{i+m}^2\) is \((z_i/|z_i|)^{2^{m+1}}\): the phase written into the input. Finally the clock moves by exactly one on \([70,82]\), which contains every readout support, whatever \(z\) does. These are explanations, not proofs: the next lesson proves that the predicted and actual clocks agree, that each register stays in the unit disc until it is read, and only then uses the phase.

## 6. Continuous differentiability

**Proposition 6.1.** The inputs \(U_\ell:(\mathbb R/100\mathbb Z)\times\Sigma\to\mathbb C\) are continuously differentiable, \(|U_\ell|\leq L/(10(L-1))<\tfrac15\), and \(f\) is a \(C^1\) self-map of \(M\).

*Proof.* *Angular factors.* The support of \(\chi\) lies in the compact annulus \(A=\{\tfrac14\leq|z|\leq2\}\), on which \(u(z)=z/|z|\) is smooth; let \(c_u\) and \(c_\chi\) be the maxima of \(\|Du\|\) and \(\|D\chi\|\) on \(A\) (norms from the round metric on the source and the modulus on \(\mathbb C\)). Since \(D(u^k)=k\,u^{k-1}Du\) and \(|u|=1\),
\[
|\Phi_k|\leq1,\qquad\|D\Phi_k\|\leq c_\chi+k\,c_u\leq C_\chi(1+k)\tag{6.1}
\]
with \(C_\chi=\max\{c_\chi,c_u\}\), independent of \(k\).

*Summands.* The \(m\)-th summand of (5.1),
\[
F_{\ell,m}(t,z)=\frac{L^{1-m}}{10}\,\alpha(t)\,\beta_\ell\bigl(T_m(t,z)\bigr)\,\Phi_{2^{m+1}}(z),
\]
is smooth on \(\mathbb R\times\Sigma\). By the product rule its derivative is the sum of three terms, in which respectively \(\alpha\), \(\beta_\ell\circ T_m\) and \(\Phi_{2^{m+1}}\) are differentiated. With \(c_\alpha=\max|\alpha'|\), \(c_\beta=\max_\ell\max|\beta_\ell'|\), (4.2) and (6.1),
\[
|F_{\ell,m}|+\|DF_{\ell,m}\|\leq C\,L^{1-m}\bigl(1+B^m+2^{m+1}\bigr)\tag{6.2}
\]
for a constant \(C\) independent of \(\ell\) and \(m\). By (4.3) the three series \(\sum L^{1-m}\), \(\sum L(B/L)^m\) and \(\sum 2L(2/L)^m\) converge. Hence the series \(\sum_mF_{\ell,m}\) and \(\sum_mDF_{\ell,m}\) converge uniformly on \(\mathbb R\times\Sigma\): their tails are bounded by tails of a convergent numerical series.

*Differentiability of the sum.* Let \(K\) be a compact coordinate box inside a chart \((t,x_1,x_2)\) of \(\mathbb R\times\Sigma\) (with \(x_1+ix_2=z\) or \(=w\)). On \(K\) the coordinate partial derivatives of a function are bounded by a constant \(c_K\) times the norm of its derivative, so the series of partial derivatives \(\sum_m\partial_jF_{\ell,m}\) converge uniformly on \(K\). On each coordinate segment in \(K\), Lebl's Theorem 6.2.10 shows that the partial derivative \(\partial_jU^\circ_\ell\) exists and equals \(\sum_m\partial_jF_{\ell,m}\). This limit is continuous: if \(g_N\to g\) uniformly with \(g_N\) continuous, then \(|g(x)-g(y)|\leq|g(x)-g_N(x)|+|g_N(x)-g_N(y)|+|g_N(y)-g(y)|\), and the outer terms are uniformly small. By Lebl's Proposition 8.4.6, \(U^\circ_\ell\) is continuously differentiable on the interior of \(K\). Such boxes cover \(\mathbb R\times\Sigma\), so \(U^\circ_\ell\) is \(C^1\).

Nothing in this argument depends on a *selected* prediction time: at a point where \(\beta_\ell(T_m)=0\) for all \(m\), every summand and its derivative vanish, and uniform convergence of the tails gives continuity even if nearby points have nonzero summands with indices tending to infinity.

*Periodization and bound.* \(U^\circ_\ell\) vanishes, with its derivative, unless \(t\in(8,12)\). The translates \(U^\circ_\ell(\cdot-100k,\cdot)\) have disjoint supports and only one of them is nonzero near any point, so \(U_\ell\) is \(C^1\) and descends to \((\mathbb R/100\mathbb Z)\times\Sigma\). Since \(\alpha,\beta_\ell,|\Phi_k|\leq1\),
\[
|U_\ell|\leq\frac1{10}\sum_{m\geq1}L^{1-m}=\frac{L}{10(L-1)}<\frac15,\tag{6.3}
\]
using \(L>2\).

*The map.* The clock component of (5.2) is smooth and well defined modulo \(100\). Each register component is \(C^1\), with values in the disc of radius \(3L+\tfrac15\) of the affine chart; this includes source values \(v_\ell=\infty\), because \(S\) is smooth and vanishes near \(\infty\). The main component is smooth at every finite \(z\). Near \(z=\infty\) put \(C_0(t,\mathbf v)=20\sum_\ell\bar\beta_\ell(t)S(v_\ell)\), a smooth function with \(|C_0|\leq60q\). In the coordinate \(w=1/z\) at the source and \(w'=1/z'\) at the target,
\[
w'=\frac1{w^{-2}+C_0}=\frac{w^2}{1+C_0\,w^2}.\tag{6.4}
\]
For \(|w|<(120q)^{-1/2}\) the denominator has modulus at least \(1-60q|w|^2>\tfrac12\), uniformly in \(t\) and the registers, so (6.4) extends smoothly to \(w=0\) with value \(0\), which is \(z'=\infty\). Hence \(f\) is \(C^1\). \(\square\)

**Remark 6.2 (why the series is infinite).** The number of steps between preparation (clock near \(10\)) and a readout (clock near \(76\)) is not bounded: the clock passes \(50\), where its increment \(h\) can be as small as \(b(t)\), when \(|z|<\tfrac34\). An input built from finitely many predictions \(m\leq m_0\) would miss every readout more than \(m_0\) steps after preparation, and the main coordinate would then square without help. The weights \(L^{1-m}\) let the series run over all delays while keeping its first derivatives summable. Nothing better than \(C^1\) is claimed: the second derivatives of the summands grow like \(L^{-m}(B^{2m}+4^m)\), and \(L\) was only chosen larger than \(B\) and \(2\).

## 7. Exercises

**7.1.** Verify (6.4), and show that the denominator is at least \(\tfrac12\) in modulus for \(|w|<(120q)^{-1/2}\).

**7.2.** Why is the saturation \(S\) needed in (5.2)? What would go wrong with the formulas \(v_\ell'=a(t)v_\ell+U_\ell\) and \(z'=z^2+20\sum_\ell\bar\beta_\ell(t)v_\ell\) on the sphere?

**7.3.** Show that \(f\) is not injective. (Use that \(S\) vanishes near \(\infty\).)

**7.4.** Show that a register is reset to zero at the first step at which the clock reading lies in \([2,5]\) modulo \(100\), and that it then stays zero until the clock reaches \(8\).

**7.5.** Compute \(\|DG\|\) at a point \((t,z)\) with \(b(t)=1\) and \(z\) finite, in terms of \(|z|\), for the map \(z\mapsto z^2\) in the round metric. Show that \(\|D(z\mapsto z^2)\|\) is at most \(2\) on the whole sphere (so that \(B\) is governed by the clock part of \(G\)).

## 8. Solutions

**7.1.** \(z'=z^2+C_0\) with \(z=1/w\) gives \(1/w'=1/w^2+C_0=(1+C_0w^2)/w^2\), hence (6.4). For \(|w|^2<1/(120q)\), \(|C_0w^2|\leq60q|w|^2<\tfrac12\).

**7.2.** On the sphere, \(a(t)v_\ell\) is undefined at \(v_\ell=\infty\) when \(a(t)=0\) (it would be \(0\cdot\infty\)), and \(z^2+20\bar\beta_\ell(t)v_\ell\) is undefined when \(z\) is finite and \(v_\ell=\infty\), or makes \(z'\) depend discontinuously on \(v_\ell\). The saturation makes every term bounded, equal to the identity on the unit disc (where the registers will be shown to live until they are read), and zero near \(\infty\).

**7.3.** Fix all coordinates except \(v_1\), and let \(v_1\) vary in \(\{|v_1|>3L+1\}\cup\{\infty\}\). There \(S(v_1)=0\), and \(v_1\) enters (5.2) only through \(S(v_1)\); so all these points have the same image.

**7.4.** At such a step \(a(t)=0\) and \(\alpha(t)=0\), so \(U_\ell=0\) and \(v_\ell'=0\). While the clock stays below \(8\) (modulo \(100\)) the input remains zero, and \(S(0)=0\) keeps the register at zero, whatever the gain.

**7.5.** For \(g(z)=z^2\) at finite \(z\), a tangent vector of round length \(2|\dot z|/(1+|z|^2)\) is sent to \(2z\dot z\), of round length \(2|2z\dot z|/(1+|z|^4)\). The ratio is \(2|z|(1+|z|^2)/(1+|z|^4)\), which is at most \(2\) (it equals \(2\) at \(|z|=1\)), since \(2|z|(1+|z|^2)\leq2(1+|z|^4)\) is equivalent to \(|z|+|z|^3\leq1+|z|^4\), that is \((1-|z|)(1-|z|^3)\geq0\). By symmetry in the chart \(w\) the same bound holds near \(\infty\). When \(b(t)=1\) the clock component is \(t+1\), whose derivative has norm one; so at such points \(\|DG\|\leq2\), and larger values of \(\|DG\|\) come from the variation of \(b\) and \(e\) in the clock increment.

## References

- [OpenAI-C1] OpenAI, *A \(C^1\) counterexample to the entropy conjecture*, OpenAI Math Release preprint, 25 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026
- [Lebl] J. Lebl, *Basic Analysis I* and *II*, version 6.3; the texts of the core courses Real Analysis I and II. https://www.jirka.org/ra/
