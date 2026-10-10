# Every orbit is attracted

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves that every orbit of the map \(f:M\to M\) of [A clock with registers](a-clock-with-registers.md) approaches one of two small invariant sets: either the clock stops at \(50\) and the main coordinate tends to \(0\), or the main coordinate tends to \(\infty\) and the registers become zero. The second case is the heart of the construction. In every complete period of the clock, the registers are first erased, then loaded with predictions, and then read out in phase with the square of the main coordinate; the readouts never decrease the modulus of \(z^2\), and one of them adds at least \(2\) to it unless \(|z|\) was already larger than one at a preparation step. The proofs only use the formulas of the previous lesson; we refer to its displays as (2.1), (3.1), (5.1), (5.2) and to its Lemma 2.1 as the clock barrier lemma.

## 1. Two invariant sets

Write \(\mathbf v=(v_1,\ldots,v_q)\) and
\[
Z_0=\{(50\bmod100,\,0,\,\mathbf v):\mathbf v\in\Sigma^q\},\qquad
Z_\infty=\{(t,\,\infty,\,0,\ldots,0):t\in\mathbb R/100\mathbb Z\}.\tag{1.1}
\]
Both are compact. They are forward invariant: on \(Z_0\) we have \(h(50,0)=b(50)=0\), the readout coefficients \(\bar\beta_\ell(50)\) and the inputs (which contain the factor \(\alpha(50)=0\)) vanish, and \(a(50)=L\), so \(f(50,0,\mathbf v)=(50,0,LS(v_1),\ldots,LS(v_q))\). On \(Z_\infty\) the main coordinate stays at \(\infty\), the clock advances by \(h(t,\infty)=1\) (as \(e(\infty)=1\)), and the inputs vanish because \(\Phi_k(\infty)=0\), so zero registers stay zero.

For an orbit we write \(f^n(x)=(t_n\bmod100,z_n,v_{n,1},\ldots,v_{n,q})\), where \(t_0\in\mathbb R\) is any lift of the initial clock and \(t_{n+1}=t_n+h(t_n,z_n)\). Then
\[
0\leq t_{n+1}-t_n\leq1,\tag{1.2}
\]
and \(t_{n+1}-t_n=1\) whenever \(t_n\bmod100\in[0,48]\cup[52,100)\), because \(b=1\) there.

**Theorem 1.1 (attraction).** For every \(x\in M\), \(\operatorname{dist}(f^nx,Z_0\cup Z_\infty)\to0\) as \(n\to\infty\), for every compatible metric on \(M\). More precisely: if the lifted clock \((t_n)\) is bounded, then \(t_n\to50+100k\) for some integer \(k\) and \(z_n\to0\); if it is unbounded, then \(z_n\to\infty\) and all registers are zero from some time on.

All compatible metrics on the compact space \(M\) are uniformly equivalent ([Topological entropy and attraction](topological-entropy-and-attraction.md), Section 1 and Exercise 5.4), so it suffices to prove the theorem for one product metric.

## 2. Bounded clocks

**Lemma 2.1.** If \((t_n)\) is bounded, then \(t_n\to50+100k\) for some integer \(k\), and \(z_n\to0\). No assumption is made on the registers.

*Proof.* The sequence \((t_n)\) is nondecreasing and bounded, so it converges to some \(t_*\), and \(h(t_n,z_n)=t_{n+1}-t_n\to0\). Since \(0\leq b(t_n)\leq h(t_n,z_n)\), continuity gives \(b(t_*)=0\), so \(t_*=50+100k\) by the clock barrier lemma. For large \(n\) the clock reading is near \(50\) modulo \(100\), far from the readout windows in \((74,80)\); so \(z_{n+1}=z_n^2\) for finite \(z_n\), and \(z_n=\infty\) would force \(h=1\) from then on, which is impossible. Also \(h(t_n,z_n)<1\) for large \(n\), so \(e(z_n)<1\), that is \(|z_n|<\tfrac34\). From such a time \(N\) on, \(|z_{N+r}|=|z_N|^{2^r}\to0\). \(\square\)

## 3. Complete passages

From now until the end of Section 5 we assume that \((t_n)\) is unbounded, so \(t_n\to\infty\), and that \(z_0\) is finite. Then every \(z_n\) is finite, since (5.2) adds finite numbers to \(z^2\). For an integer \(k\) with \(100k>t_0\) put
\[
N_k=\min\{n\geq0:t_n\geq100k\},\qquad N_{k+1}=\min\{n\geq0:t_n\geq100(k+1)\}.
\]
By (1.2), \(0\leq t_{N_k}-100k<1\). The indices \(N_k\leq n<N_{k+1}\) form a **complete passage**. Within it we use the translated readings \(s_n=t_n-100k\in[0,100)\), at which the periodic data of (5.2) may be evaluated directly; for instance \(\bar\beta_\ell(t_n)=\beta_\ell(s_n)\). Put
\[
I=\{n:\ N_k\leq n<N_{k+1},\ \alpha(s_n)>0\},
\]
the **preparation indices** of the passage. Every period after the first one met by the orbit is a complete passage.

**Lemma 3.1 (preparation).** In a complete passage:

(a) all registers are zero at the first index of \(I\);

(b) \(I\) is nonempty, has at most four elements, and contains an index \(i\) with \(\alpha(s_i)=1\);

(c) some index \(j\) of the passage has \(s_j\in[76,77)\) and \(\beta_\ell(s_j)=1\) for at least one \(\ell\);

(d) \(|z_i|>\tfrac12\) for every \(i\in I\).

*Proof.* (a) Let \(r\) be the first index of the passage with \(s_r\geq2\). The previous reading is below \(2\) (the first reading of the passage is below \(1\)), so \(2\leq s_r<3\) by (1.2). At time \(r\) the gain \(a(s_r)\) and the input (which contains \(\alpha(s_r)\)) vanish, so \(v_{r+1,\ell}=0\) for every \(\ell\), even if some \(v_{r,\ell}\) was \(\infty\). Until the clock reaches \(8\) the inputs remain zero, and \(S(0)=0\) keeps the registers at zero; preparation indices have \(s>8\).

(b) On \([0,48]\) the clock advances by exactly one per step, so its readings there form an arithmetic progression with difference one. An open interval of length four contains at most four of them; hence \(|I|\leq4\). The first reading at least \(9\) lies in \([9,10)\), where \(\alpha=1\); it occurs in the passage because the readings eventually reach \(100\).

(c) Similarly the clock advances by one on \([52,100)\), so the first reading at least \(76\) lies in \([76,77)\), and (3.1) of the previous lesson supplies \(\ell\) with \(\beta_\ell(s_j)=1\).

(d) Suppose \(i\in I\) and \(|z_i|\leq\tfrac12\). We show by induction that \(8\leq s_n\leq50\) and \(|z_n|\leq\tfrac12\) for all \(n\geq i\). If this holds at \(n\), there is no readout (the readout windows lie in \((74,80)\)), \(e(z_n)=0\), and therefore \(z_{n+1}=z_n^2\) and \(s_{n+1}=s_n+b(s_n)\leq50\) by the clock barrier lemma (iii); also \(s_{n+1}\geq s_n\geq8\) and \(|z_{n+1}|\leq\tfrac14\). So the readings never exceed \(50\), contradicting the completeness of the passage. \(\square\)

## 4. Predictions and linear registers

Fix a complete passage. The predictions of (5.1) are computed with the map \(G\), which ignores the readouts; after a readout the actual main coordinate differs from the predicted one. Only the clocks have to agree, and they do, because the clock moves by exactly one throughout the readout region.

**Lemma 4.1 (clock prediction).** For each \(\ell\) there is at most one index \(j\) in the passage with \(\beta_\ell(s_j)>0\). If there is one, then for every \(i\in I\) and every \(m\geq1\),
\[
\beta_\ell\bigl(T_m(s_i,z_i)\bigr)=\begin{cases}\beta_\ell(s_j),&m=j-i,\\0,&m\neq j-i.\end{cases}\tag{4.1}
\]
Here \(\beta_\ell\) is the function on \(\mathbb R\), not its periodization.

*Proof.* Fix \(i\in I\); then \(s_i\in(8,12)\). Let \(r_{70}\) and \(r_{82}\) be the first indices after \(i\) with \(s\geq70\) and \(s\geq82\); they lie in the passage. For \(i\leq n<r_{70}\) the readings are below \(70\), so no readout occurs and \((s_{n+1},z_{n+1})=G(s_n,z_n)\). Hence \(G^{n-i}(s_i,z_i)=(s_n,z_n)\) and \(T_{n-i}(s_i,z_i)=s_n\) for \(i<n\leq r_{70}\). From \(r_{70}\) on, both the actual and the predicted clocks lie in \([70,82)\) until they reach \(82\), and there both advance by exactly one per step, whatever their main coordinates are. Starting from equal values at \(r_{70}\), they stay equal:
\[
T_{n-i}(s_i,z_i)=s_n\qquad(i<n\leq r_{82}).\tag{4.2}
\]
After that the predicted clock is at least \(82\) and nondecreasing, so it never returns to the support of \(\beta_\ell\), which lies in \((74,80)\). Before \(r_{70}\) the predictions are below \(70\). So \(\beta_\ell(T_m(s_i,z_i))\) can be nonzero only for \(r_{70}\leq i+m<r_{82}\), and there it equals \(\beta_\ell(s_{i+m})\).

The support of \(\beta_\ell\) lies in an interval \(J_\ell\) of length less than one. If \(\beta_\ell(s_j)>0\), then \(s_j\in J_\ell\) and \(s_{j+1}=s_j+1\) lies beyond \(J_\ell\); by monotonicity no later reading meets \(J_\ell\). Hence at most one index \(j\) has \(\beta_\ell(s_j)>0\), and (4.1) follows from the previous paragraph. \(\square\)

**Lemma 4.2 (registers are linear until read).** Let \(j\) be an index of the passage and \(\ell\) a channel with \(\beta_\ell(s_j)>0\). Then \(|v_{j,\ell}|\leq\tfrac12\), so \(S(v_{j,\ell})=v_{j,\ell}\), and
\[
v_{j,\ell}=\frac{\beta_\ell(s_j)}{10}\sum_{i\in I}\alpha(s_i)\,\chi(z_i)\Bigl(\frac{z_i}{|z_i|}\Bigr)^{2^{j-i+1}}.\tag{4.3}
\]
No alignment of the phases of the summands is assumed.

*Proof.* The phases are defined because \(z_i\neq0,\infty\) for \(i\in I\) (Lemma 3.1(d)). For \(i\in I\) put
\[
c_i=\frac{\beta_\ell(s_j)}{10}\,\alpha(s_i)\,\chi(z_i)\Bigl(\frac{z_i}{|z_i|}\Bigr)^{2^{j-i+1}},\qquad|c_i|\leq\tfrac1{10}.
\]
By Lemma 4.1, only the term \(m=j-i\) survives in (5.1), so the input at a preparation index is exactly
\[
U_\ell(s_i,z_i)=L^{1+i-j}c_i\qquad(i\in I).\tag{4.4}
\]
Let \(i_0=\min I\), and for \(i_0\leq u\leq j\) define the candidate values
\[
w_u=L^{u-j}\sum_{i\in I,\ i<u}c_i,\qquad\text{so that}\qquad|w_u|\leq\frac{|I|}{10}L^{u-j}\leq\frac4{10}<\frac12.\tag{4.5}
\]
By Lemma 3.1(a), \(v_{i_0,\ell}=0=w_{i_0}\). For \(i_0\leq u<j\) the reading \(s_u\) lies in \((8,80)\subseteq[7,90]\), so the gain is \(a(s_u)=L\); the input is zero unless \(u\in I\), and then it is given by (4.4). Hence
\[
w_{u+1}=L\,w_u+U_\ell(s_u,z_u).
\]
If \(v_{u,\ell}=w_u\), then (4.5) gives \(S(v_{u,\ell})=w_u\), and the register update of (5.2) gives \(v_{u+1,\ell}=w_{u+1}\). By induction \(v_{j,\ell}=w_j=\sum_{i\in I}c_i\), since every preparation index precedes \(j\). This is (4.3), and (4.5) gives the bound. \(\square\)

The induction concerns only the register read at \(j\). Another register may already have been read earlier in the passage and may have left the unit disc since; by Lemma 4.1 its readout coefficient is zero for the rest of the passage, and registers do not enter one another's updates.

## 5. Phase alignment and escape

**Lemma 5.1 (escape in one passage).** In a complete passage with finite main coordinate, let \(i_0=\min I\). For \(i_0\leq n<N_{k+1}\),
\[
z_n\neq0,\qquad|z_{n+1}|\geq|z_n|^2,\qquad\frac{z_{n+1}}{|z_{n+1}|}=\Bigl(\frac{z_n}{|z_n|}\Bigr)^2.\tag{5.1}
\]
Moreover some index \(N\) with \(i_0\leq N<N_{k+1}\) has \(|z_N|>1\).

*Proof.* Put \(\theta=z_{i_0}/|z_{i_0}|\). Before the first readout of the passage the main coordinate squares exactly, so it stays nonzero and its phase at time \(n\) is \(\theta^{2^{n-i_0}}\); this includes all preparation indices, which precede all readouts.

We go through the readout indices in order. Let \(j\) be one, and suppose \(z_j\neq0\) has phase \(\theta^{2^{j-i_0}}\). For each \(i\in I\) the phase in (4.3) is
\[
\Bigl(\frac{z_i}{|z_i|}\Bigr)^{2^{j-i+1}}=\bigl(\theta^{2^{i-i_0}}\bigr)^{2^{j-i+1}}=\theta^{2^{j-i_0+1}},
\]
the phase of \(z_j^2\). Lemma 4.2 applies to each channel \(\ell\) with \(\beta_\ell(s_j)>0\); the other channels have coefficient \(\beta_\ell(s_j)=0\) in the main update. Therefore the main update at \(j\) is exactly
\[
z_{j+1}=\Bigl(|z_j|^2+2\sum_{\ell=1}^q\beta_\ell(s_j)^2\sum_{i\in I}\alpha(s_i)\chi(z_i)\Bigr)\theta^{2^{j-i_0+1}}.\tag{5.2}
\]
(One factor \(\beta_\ell(s_j)\) comes from the readout in the main update and the other from the input; \(20\cdot\frac1{10}=2\).) All added coefficients are nonnegative and \(|z_j|^2>0\). This gives (5.1) at \(j\), with phase \(\theta^{2^{j+1-i_0}}\). Between readouts the coordinate squares exactly. Induction proves (5.1) throughout the passage, including steps at which several channels are read at once and successive readouts of different channels.

If some \(i\in I\) has \(|z_i|>1\), take \(N=i\). Otherwise \(\tfrac12<|z_i|\leq1\) for all \(i\in I\) (Lemma 3.1(d)). Choose \(i_*\in I\) with \(\alpha(s_{i_*})=1\) (Lemma 3.1(b)); then \(\chi(z_{i_*})=1\), because \(\chi=1\) on \(\{\tfrac12\leq|z|\leq1\}\). Choose \(j_*\) and \(\ell_*\) with \(s_{j_*}\in[76,77)\) and \(\beta_{\ell_*}(s_{j_*})=1\) (Lemma 3.1(c)). In (5.2) at \(j=j_*\) the single pair \((\ell_*,i_*)\) contributes \(2\), and all other terms have the same phase, so
\[
|z_{j_*+1}|\geq|z_{j_*}|^2+2>2.
\]
Take \(N=j_*+1\); it lies in the passage because \(s_{j_*+1}<78\). \(\square\)

## 6. Proof of the attraction theorem

*Bounded clock.* Lemma 2.1 gives \(t_n\to50\) modulo \(100\) and \(z_n\to0\); in a product metric the distance to \(Z_0\) tends to zero, whatever the registers do.

*\(z_0=\infty\).* The main coordinate stays at \(\infty\), the inputs vanish, and the clock advances by one at every step. Within \(100\) steps its reading meets \([2,5]\) modulo \(100\); at that step \(a=0\) and every register becomes zero, and it stays zero. From then on the orbit lies in \(Z_\infty\).

*Unbounded clock, finite \(z_0\).* Choose a complete passage and \(N\) with \(|z_N|>1\) as in Lemma 5.1. We claim \(|z_{n+1}|\geq|z_n|^2\) for all \(n\geq N\). Within that passage this is (5.1). After its readout region no readout occurs until the readout region of the next period, so the main coordinate squares exactly across the end of the period, the reset and the next preparation; old registers, however large, cannot affect \(z\) there, and they are erased by the reset before new inputs arrive. The next period is again a complete passage, and Lemma 5.1 applies from its first preparation index to its end. These stretches cover all times after \(N\). Hence
\[
|z_{N+r}|\geq|z_N|^{2^r}\longrightarrow\infty.\tag{6.1}
\]
The argument does not need the inputs to stop: as long as \(\chi(z_n)\neq0\), the new inputs have nonnegative weights and aligned phases, as in Lemma 5.1. Now \(z_n\to\infty\) in \(\Sigma\), and \(\chi\) vanishes near \(\infty\), so from some time on all inputs vanish. The next reset makes every register zero, and they stay zero. So the distance to \(Z_\infty\) tends to zero. This proves Theorem 1.1. \(\square\)

The convergence is pointwise in the initial point; no uniform time of approach is asserted, and none exists (Exercise 7.2).

## 7. Exercises

**7.1.** Compute \(f\) on \(Z_0\) and on \(Z_\infty\), and check that both sets are forward invariant.

**7.2.** Show that the convergence in Theorem 1.1 is not uniform in the initial point. Use the metric \(d=\max\{d_{\mathrm{clock}},d_\Sigma(z,z'),d_\Sigma(v_1,v_1'),\ldots,d_\Sigma(v_q,v_q')\}\), where \(d_{\mathrm{clock}}\) is the distance in \(\mathbb R/100\mathbb Z\) and \(d_\Sigma\) is a compatible metric on \(\Sigma\), and put \(\varepsilon=\min\{\tfrac1{10},d_\Sigma(0,\infty)\}\). Show that for every \(N\) there are \(x\in M\) and \(n\geq N\) with \(d(f^nx,Z_0\cup Z_\infty)\geq\varepsilon\). (Start with the clock at \(50+\delta\), the main coordinate \(0\) and zero registers.)

**7.3.** In (5.2), why can a readout never decrease \(|z|\)? Which two properties of the construction are used?

**7.4.** Suppose two readout windows \(\beta_1\) and \(\beta_2\) are both positive at the same reading \(s_j\). Show that Lemma 4.2 still applies to both channels, and write the main update at \(j\).

## 8. Solutions

**7.1.** See Section 1: \(f(50,0,\mathbf v)=(50,0,LS(v_1),\ldots,LS(v_q))\) and \(f(t,\infty,0,\ldots,0)=(t+1,\infty,0,\ldots,0)\).

**7.2.** Let \(0<\delta<\tfrac1{10}\) and \(x_\delta=(50+\delta,0,0,\ldots,0)\). Along its orbit the main coordinate and the registers stay zero: the inputs contain the factor \(\chi(0)=0\), the registers are updated to \(a(t)S(0)=0\), and the main coordinate to \(0^2+20\sum_\ell\bar\beta_\ell(t)S(0)=0\). Since \(e(0)=0\), the lifted clock satisfies \(t_{n+1}=t_n+b(t_n)\), so it is nondecreasing and stays at least \(50+\delta\). The function \(b\) is smooth and periodic, so \(K=\max|b'|\) is finite, and \(b(50)=0\) gives \(b(t)\leq K(t-50)\) for \(t\geq50\) (mean value theorem). Hence \(t_{n+1}-50\leq(1+K)(t_n-50)\) and \(t_n-50\leq(1+K)^n\delta\): the clock is at most \(50.1\) for all \(n\leq n(\delta)=\log(0.1/\delta)/\log(1+K)\), and \(n(\delta)\to\infty\) as \(\delta\to0\). The clock does pass \(50.1\): \(b\) has a positive minimum \(c\) on \([50+\delta,50.1]\) (it vanishes only at \(50\) modulo \(100\); extreme value theorem), so the clock gains at least \(c\) per step while it lies there. Let \(n'\) be the first time with \(t_{n'}>50.1\). Then \(n'>n(\delta)\), and \(t_{n'}\leq51.1\) because the clock moves by at most one per step. At time \(n'\) the clock distance from \(50\) is more than \(\tfrac1{10}\), so the distance to \(Z_0\) is more than \(\tfrac1{10}\); the main coordinate is \(0\), so the distance to \(Z_\infty\) is at least \(d_\Sigma(0,\infty)\). Given \(N\), choose \(\delta\) with \(n(\delta)\geq N\) and take \(n=n'\). Theorem 3.1 of [Topological entropy and attraction](topological-entropy-and-attraction.md) uses only pointwise attraction, and Exercise 5.5 there shows the same phenomenon in a simpler map.

**7.3.** At a readout the added term has the same phase as \(z_j^2\) (phase alignment, Lemma 5.1) and a nonnegative coefficient (the weights \(\beta_\ell^2\), \(\alpha\) and \(\chi\) are nonnegative). A sum of two complex numbers with the same phase has modulus equal to the sum of the moduli.

**7.4.** The proof of Lemma 4.2 concerns one channel at a time and uses only Lemma 4.1 for that channel, so it applies to both. The main update is (5.2) with the sum over \(\ell\) containing the two positive terms \(\beta_1(s_j)^2\) and \(\beta_2(s_j)^2\).

## References

- [OpenAI-C1] OpenAI, *A \(C^1\) counterexample to the entropy conjecture*, OpenAI Math Release preprint, 25 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026
