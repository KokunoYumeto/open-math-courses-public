# Zero avoidance and the finite sieve

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson completes the proof of the uniform component bound for Gaussian primes. Suppose that an infinite walk with steps of length at most \(D\) avoids the zero class of every conjugate factor of every prime in a large finite union of batches. Sample a time with the schedule of [A common sampling schedule](a-common-sampling-schedule.md). Because the walk never meets those zero classes, a short word of increments after the sampled time rules out every starting residue that would lead into one of them. Coverage, proved in that lesson, makes many residues likely starting points, and self-avoidance makes the different steps of a short word test disjoint possibilities; so repeated tests reveal a positive proportion of the residue entropy. We show that each batch near \(T\) forces at least \(c_1/\log T\) units of conditional information per increment. On the other hand, an increment takes at most \(K_D\) values, and a telescoping argument shows that all batches together can extract at most \(\log K_D\) units per increment from the common final time. Since \(\sum_T1/\log T\) diverges as the number of windows grows, a large enough finite sieve admits no infinite walk.

We use [Entropy of finite random variables](entropy-of-finite-random-variables.md) throughout, the arithmetic of [Walks through Gaussian primes](walks-through-gaussian-primes.md), and the notation and results of [A common sampling schedule](a-common-sampling-schedule.md).

Basic references are [OpenAI-moat] and [Tao 2016].

## 1. The setting

Fix \(D\ge1\) and the constants of Section 1 of [A common sampling schedule](a-common-sampling-schedule.md), with the batches of the windows \(\lceil M/2\rceil\le m\le M\) and their union \(\mathcal P_M\). "For large \(M\)" has the meaning fixed there. Let \(z_0,z_1,\dots\) be an infinite \(D\)-walk with every point in \(\mathcal A(\mathcal P_M)\): no point is divisible by either conjugate factor of any prime of \(\mathcal P_M\). Run the schedule from time \(0\), with final time \(t_*\).

**Auxiliary choices.** For each batch \(T\), let \(\mathcal C_T\) be a uniform signed subset of size \(q_T\) (Proposition 4.2 of the schedule lesson): \(q_T\) distinct primes of the batch, chosen uniformly, each with one of its two conjugate factors chosen by a fair coin. The choices for different batches are independent of each other and of the sampling. Write \(\mathcal C\) for all of them. Entropies and informations are always computed with \(\mathcal C\) fixed and then averaged, as in Convention 7.1 of the entropy lesson; we write \(\mathbb E_{\mathcal C}\) for this average.

For a time \(t\), let \(X'_T(t)=F_{\mathcal C_T}(z_t)\) be the vector of residues of \(z_t\) modulo the factors selected for the batch \(T\), and \(O'_T(t)\) the vector of residues modulo the factors selected for all smaller batches. Write \(X'_T=X'_T(t_*)\) and \(O'_T=O'_T(t_*)\). For an integer \(L\ge1\), the **increment word** of length \(L\) at time \(t\) is

\[
W_L(t)=\bigl(z_{t+1}-z_t,\ z_{t+2}-z_{t+1},\ \dots,\ z_{t+L}-z_{t+L-1}\bigr).
\]

Each letter is a nonzero lattice vector of length at most \(D\), so it takes at most \(K_D\) values. We use the dyadic lengths

\[
L_T=2^{\lfloor\log_2(T^{2/5})\rfloor},\qquad \tfrac12T^{2/5}<L_T\le T^{2/5}.
\]

## 2. The information cost of one batch

**Proposition 2.1** (cost of a batch). Put \(K_0=128\) and \(c_1=\beta_0c_0/(12K_0)\). For large \(M\), every batch \(T\) satisfies

\[
\frac1{L_T}\,\mathbb E_{\mathcal C}\,I\bigl(X'_T;W_{L_T}(t_*)\mid O'_T\bigr)\ge\frac{c_1}{\log T}.
\]

**Proof.** Fix the batch and write \(L=L_T\), \(q=q_T\), \(p\) for primes of the batch, and \(A_0=A_0(T)\) for the first checkpoint of Section 5 of the schedule lesson. Put

\[
X=X'_T(A_0),\qquad O=O'_T(A_0),\qquad s=z_{t_*}-z_{A_0},\qquad W=W_L(t_*).
\]

*Step 1: the residues at \(A_0\) are uncertain.* For fixed \(\mathcal C\), Corollary 2.4(3) of the entropy lesson gives \(H(X\mid O)\ge H(X)-H(O)\). The variable \(O\) takes at most \(\prod_{T'<T}(2T')^{q_{T'}}\) values, and \(q_{T'}\le k_{T'}\), so Proposition 4.3 of the schedule lesson gives \(H(O)\le e_0c_0T\le e_0qL_*\). The average of \(H(X)\) over \(\mathcal C_T\) is the profile \(f_{z_{A_0}}(q)\), which is at least \((1-e_0)qL_*\) by Proposition 4.2 there, since \(A_0\) comes after the top band of the batch's window. Hence

\[
\mathbb E_{\mathcal C}\,H(X\mid O)\ge(1-2e_0)\,qL_*.
\tag{2.1}
\]

By Lemma 5.1 of the schedule lesson, \(s\) lies in the set \(\mathcal D_0\), so

\[
H(s)\le\log|\mathcal D_0|\le T^{1/4}.
\tag{2.2}
\]

The time-0 run, and with it the law of \(s\), does not depend on \(\mathcal C\).

*Step 2: repeated tests.* Fix \(\mathcal C\). Put \(m=\lceil K_0(T/L)\log T\rceil\). In an auxiliary experiment, draw \((O,X)\) with its law, and then, conditionally on the values of \((O,X)\), draw \(m\) independent **packages** \(P_1,\dots,P_m\), each with the conditional law of \((s,W)\) given those values. Thus each triple \((O,X,P_a)\) has the law of \((O,X,(s,W))\), and the packages are conditionally independent given \((O,X)\). Write \(P=(P_1,\dots,P_m)\) and \(P_a=(s_a,W^{(a)})\).

For a selected factor \(\pi\) (one of the factors in \(\mathcal C_T\)), say that a residue \(x\in\mathbb Z[i]/(\pi)\) **passes** the package \(P_a\) if

\[
x+s_a+\sum_{h<l}W^{(a)}_h\not\equiv0\pmod\pi\qquad\text{for }l=0,1,\dots,L-1,
\]

where \(W^{(a)}_h\) is the \(h\)-th letter, counted from \(0\). Let \(\mathcal L_\pi(P)\) be the set of residues that pass every package. In the original experiment, \(X_\pi+s+\sum_{h<l}W_h\) is the residue of \(z_{t_*+l}\), which is nonzero because the walk avoids the zero class of \(\pi\). Since \((X,P_a)\) has the law of \((X,(s,W))\), the true coordinate \(X_\pi\) passes every package almost surely: \(X_\pi\in\mathcal L_\pi(P)\). For each value of \((O,P)\), the conditional values of \(X\) therefore lie in the product of the sets \(\mathcal L_\pi(P)\), and

\[
H(X\mid O,P)\le\mathbb E\sum_{\pi\in\mathcal C_T}\log|\mathcal L_\pi(P)|.
\tag{2.3}
\]

*Step 3: the packages are mixtures of continuations.* For an integer \(a\ge0\), let \(\kappa_a\) be the law of \((z_{t_*}-z_a,W_L(t_*))\) in the continuation experiment from the exact start \(A_0=a\). The variables \(O\) and \(X\) are functions of the walk position at time \(A_0\), and after \(A_0\) the schedule uses fresh randomness. Hence, for every value \(\omega\) of \((O,X)\) of positive probability,

\[
\mathbb P\bigl((s,W)\in\cdot\mid(O,X)=\omega\bigr)=\sum_a\mathbb P\bigl(A_0=a\mid(O,X)=\omega\bigr)\,\kappa_a.
\tag{2.4}
\]

Call a selected factor \(\pi\) **favorable** for the value \(\omega\) if, for the posterior law \(\mu_\omega=\mathbb P(A_0=\cdot\mid(O,X)=\omega)\), the set \(G\) of exact starts \(a\) at which the terminal residue law \(b_{0,a,\pi}\) has \((\tau_0,\beta_0)\)-coverage has \(\mu_\omega(G)\ge\frac12\). Let \(\chi(a,\pi)\) indicate that \(b_{0,a,\pi}\) fails this coverage. An unfavorable factor has posterior failure probability above \(\frac12\), so its indicator is at most twice that probability. By the tower property and Proposition 6.1 of the schedule lesson (at most a fraction \(\eta_0\) of the signed coordinates fail at each exact start),

\[
\mathbb E_{\mathcal C}\,\mathbb E\,\#\{\text{unfavorable }\pi\in\mathcal C_T\}
\le2\,\mathbb E_{\mathcal C}\,\mathbb E\sum_{\pi\in\mathcal C_T}\chi(A_0,\pi)
=2\,\mathbb E_{A_0}\,\mathbb E_{\mathcal C}\sum_{\pi\in\mathcal C_T}\chi(A_0,\pi)\le2\eta_0q.
\tag{2.5}
\]

Here we used that \(A_0\) is independent of \(\mathcal C\), and that a uniform signed subset of size \(q\) contains each signed coordinate with probability \(q/(2k_T)\).

*Step 4: most candidates are likely starting points.* Fix \(\omega\) and a favorable \(\pi\), of norm \(p\). For \(a\in G\), at most \(p^{1-\beta_0}\) residues \(u\) have \(b_{0,a,\pi}(u)<\tau_0/p\). The event \(s\equiv-x\pmod\pi\) means \(z_{t_*}\equiv z_a-x\), so in the continuation experiment from \(A_0=a\),

\[
\mathbb P\bigl(s\equiv-x\pmod\pi\bigr)\ge\frac{\tau_0}p
\]

for all but fewer than \(p^{1-\beta_0}\) candidates \(x\). Let \(u_x\) be the \(\mu_\omega\)-measure of the set of \(a\in G\) at which this inequality holds for \(x\). Summing the exceptional counts over \(a\in G\),

\[
\sum_{x\in\mathbb Z[i]/(\pi)}\bigl(\mu_\omega(G)-u_x\bigr)<p^{1-\beta_0}.
\]

All summands are nonnegative, and \(u_x<\frac14\) makes the summand larger than \(\frac14\). So fewer than \(4p^{1-\beta_0}\) candidates have \(u_x<\frac14\).

*Step 5: a short word tests \(L\) disjoint possibilities.* Fix a candidate \(x\) with \(u_x\ge\frac14\), and an offset \(0\le l<L\). Say that a package **hits** \(x\) at \(l\) if \(x+s_a+\sum_{h<l}W^{(a)}_h\equiv0\pmod\pi\). For \((s,W)\) drawn from \(\kappa_a\), this means \(z_{t_*+l}-z_a\equiv-x\pmod\pi\), an event about the time \(t_*+l\). By Lemma 3.2 of the schedule lesson, at every \(a\in G\) counted by \(u_x\),

\[
\kappa_a(\text{hit at }l)\ge\kappa_a(\text{hit at }0)-T_+^{-9}\ge\frac{\tau_0}p-T_+^{-9}\ge\frac{\tau_0}{2p},
\]

since \(l<L\le T_+\) and \(p\le2T\le2T_+\). By (2.4), a package hits \(x\) at \(l\) with conditional probability at least \(u_x\tau_0/(2p)\ge\tau_0/(8p)\), given \((O,X)=\omega\).

For one package, the hits at different offsets are disjoint events. Indeed, every realized package has the form \((z_t-z_{a'},W_L(t))\) for some times \(a'\) and \(t\), and then a hit at \(l\) means \(z_{t+l}\equiv z_{a'}-x\pmod\pi\). Hits at \(l\ne l'\) would make \(\pi\) divide \(z_{t+l}-z_{t+l'}\), which is nonzero because the walk has distinct points, and has length at most \(DL\le DT^{2/5}<\sqrt T\le\sqrt p\) for large \(M\); this contradicts Proposition 2.4(2) of the first lesson. Hence one package rejects \(x\) (hits it at some offset) with conditional probability at least \(L\tau_0/(8p)=L/(32p)\).

*Step 6: the lists are short.* The packages are conditionally independent given \((O,X)=\omega\). So for a favorable \(\pi\),

\[
\mathbb E\bigl[|\mathcal L_\pi(P)|\ \big|\ (O,X)=\omega\bigr]\le4p^{1-\beta_0}+p\Bigl(1-\frac L{32p}\Bigr)^m\le4p^{1-\beta_0}+p\exp\Bigl(-\frac{Lm}{32p}\Bigr)\le5p^{1-\beta_0}.
\]

For the last inequality, \(Lm/(32p)\ge K_0T\log T/(64T)=2\log T\), so \(p\exp(-Lm/(32p))\le2T\cdot T^{-2}\le p^{1-\beta_0}\). By Jensen's inequality, the conditional expectation of \(\log|\mathcal L_\pi(P)|\) is at most \((1-\beta_0)\log p+\log5\) for a favorable \(\pi\), and it is at most \(\log p\) in any case. With (2.3) and (2.5), and \(\mathbb E_{\mathcal C}\sum_{\pi\in\mathcal C_T}\log p=qL_*\),

\[
\mathbb E_{\mathcal C}\,H(X\mid O,P)\le(1-\beta_0)qL_*+q\log5+2\eta_0q\,\beta_0\log(2T)\le\Bigl(1-\frac{\beta_0}2\Bigr)qL_*,
\]

for large \(M\), because \(\eta_0=\frac1{100}\), \(\log(2T)\le2L_*\) and \(\log5/L_*\to0\). Together with (2.1) and \(e_0=\beta_0/50\),

\[
\mathbb E_{\mathcal C}\,I(X;P\mid O)\ge\Bigl(\frac{\beta_0}2-2e_0\Bigr)qL_*\ge\frac{\beta_0}3\,qL_*.
\tag{2.6}
\]

*Step 7: moving the information to the final time.* Fix \(\mathcal C\). By Lemma 3.4 of the entropy lesson, \(I(X;P\mid O)\le m\,I(X;s,W\mid O)\). By the chain rule for information,

\[
I(X;s,W\mid O)=I(X;s\mid O)+I(X;W\mid O,s),\qquad I(X;s\mid O)\le H(s).
\]

Given \(s\), the residue vectors at \(A_0\) and at \(t_*\) determine each other: \(X'_T=X+F_{\mathcal C_T}(s)\) and \(O'_T=O+(\text{residues of }s)\). By Corollary 2.4(4) of the entropy lesson, \(I(X;W\mid O,s)=I(X'_T;W\mid O'_T,s)\), and Lemma 3.3 there gives \(I(X'_T;W\mid O'_T,s)\le I(X'_T;W\mid O'_T)+H(s)\). Hence

\[
I(X;P\mid O)\le m\bigl(I(X'_T;W\mid O'_T)+2H(s)\bigr).
\]

Average over \(\mathcal C\), and use (2.6), (2.2), \(qL_*\ge c_0T\) and \(m\le2K_0(T/L)\log T\):

\[
\mathbb E_{\mathcal C}\,I(X'_T;W\mid O'_T)\ge\frac{\beta_0c_0}{6K_0}\cdot\frac L{\log T}-2T^{1/4}\ge\frac{\beta_0c_0}{12K_0}\cdot\frac L{\log T},
\]

the last step for large \(M\), because \(L/\log T\ge T^{2/5}/(2\log T)\) is much larger than \(T^{1/4}\). Divide by \(L\). \(\square\)

The variables on the left of Proposition 2.1 are those of the run from time \(0\), observed at the common final time \(t_*\). This is what allows the costs of different batches to be compared.

## 3. The entropy budget

**Lemma 3.1** (telescoping budget). For large \(M\) and every value of \(\mathcal C\),

\[
\sum_T\frac{I\bigl(X'_T;W_{L_T}(t_*)\mid O'_T\bigr)}{L_T}\le\log K_D+\frac1M,
\]

the sum running over all batches.

**Proof.** List the batches as \(T_1<T_2<\dots<T_n\), and write \(L_j=L_{T_j}\). These lengths are powers of \(2\) and increase with \(j\), so \(L_j\) divides \(L_{j+1}\). For a time \(t\), let \(Q_j(t)\) be the vector of residues of \(z_t\) modulo the factors selected for the batches \(T_1,\dots,T_j\), with \(Q_0\) empty. Then \(O'_{T_j}=Q_{j-1}(t_*)\) and \((O'_{T_j},X'_{T_j})=Q_j(t_*)\). Put

\[
a_j=\frac{H\bigl(W_{L_j}(t_*)\mid Q_{j-1}(t_*)\bigr)}{L_j},\qquad b_j=\frac{H\bigl(W_{L_j}(t_*)\mid Q_j(t_*)\bigr)}{L_j},
\]

so that the \(j\)-th term of the sum is \(a_j-b_j\).

*Blocks.* Split \(W_{L_{j+1}}(t_*)\) into the \(r=L_{j+1}/L_j\) consecutive blocks \(W_{L_j}(t_*+iL_j)\), \(0\le i<r\). The residue vector \(Q_j(t_*+iL_j)\) is determined by \(Q_j(t_*)\) and the earlier blocks, since \(z_{t_*+iL_j}-z_{t_*}\) is the sum of their letters. The chain rule and Corollary 2.4(4) of the entropy lesson give

\[
H\bigl(W_{L_{j+1}}(t_*)\mid Q_j(t_*)\bigr)\le\sum_{i=0}^{r-1}H\bigl(W_{L_j}(t_*+iL_j)\mid Q_j(t_*+iL_j)\bigr).
\]

*Almost invariance.* The pair \((W_{L_j}(t),Q_j(t))\) is a fixed function of the time \(t\). Since \(iL_j<L_{j+1}\le T_+^{2/5}\le T_+\), Lemma 3.2 of the schedule lesson shows that its laws at \(t_*+iL_j\) and at \(t_*\) differ by at most \(T_+^{-9}\) in total variation. The pair takes at most \(K_D^{L_j}\prod_T(2T)^{q_T}\) values, and by Lemma 5.2 of the first lesson the logarithm of this number is at most \(T_+\log K_D+(16\log2)T_+\). Corollary 5.6 of the entropy lesson, with \(h(u)\le u\log(e/u)\), gives

\[
H\bigl(W_{L_j}(t_*+iL_j)\mid Q_j(t_*+iL_j)\bigr)\le H\bigl(W_{L_j}(t_*)\mid Q_j(t_*)\bigr)+\epsilon_M,\qquad \epsilon_M=T_+^{-7},
\]

for large \(M\). Dividing by \(L_{j+1}=rL_j\), we get \(a_{j+1}\le b_j+\epsilon_M\).

*Telescoping.* Hence

\[
\sum_{j=1}^n(a_j-b_j)=a_1-b_n+\sum_{j=1}^{n-1}(a_{j+1}-b_j)\le a_1+n\epsilon_M.
\]

Each letter takes at most \(K_D\) values, so \(a_1\le\log K_D\). The number of batches is \(n\le X_M\le T_+\), so \(n\epsilon_M\le T_+^{-6}\le1/M\). \(\square\)

The telescoping argument is related to Tao's entropy decrement argument [Tao 2016, Section 3]: approximate invariance of the sampled time under small shifts, together with subadditivity over blocks, limits the total information that nested families of residues can extract from the increments.

## 4. The finite sieve theorem

**Theorem 4.1** (finite sieve obstruction). For every \(D\ge1\) there is a finite set \(\mathcal P_D\) of rational primes congruent to \(1\) modulo \(4\) such that \(\mathcal A(\mathcal P_D)\) contains no infinite \(D\)-walk.

**Proof.** Let \(M\) be large, and suppose that an infinite \(D\)-walk lies in \(\mathcal A(\mathcal P_M)\). Average Lemma 3.1 over \(\mathcal C\) and apply Proposition 2.1 to each batch:

\[
c_1\sum_T\frac1{\log T}\le\log K_D+1.
\tag{4.1}
\]

The window \([X_m,1.05X_m]\) contains at least \(0.05X_m/\log B-1\ge0.04X_m/\log B\) batches for large \(M\) (Exercise 7.3 of the schedule lesson), and each contributes \(1/\log T\ge1/(1.05X_m)\). So each window contributes at least \(0.038/\log B\), and the at least \(M/2\) windows contribute at least \(0.019M/\log B\). For

\[
M>\frac{(\log K_D+1)\log B}{0.019\,c_1}
\]

this contradicts (4.1). All the thresholds are uniform over the walks. Choosing one such large \(M\), depending only on \(D\), and putting \(\mathcal P_D=\mathcal P_M\), no infinite \(D\)-walk lies in \(\mathcal A(\mathcal P_D)\). \(\square\)

**Corollary 4.2** (the Gaussian moat theorem). For every real \(D\) there is \(B_D\) such that every connected component of the graph joining Gaussian primes at distance at most \(D\) has at most \(B_D\) vertices. In particular there is no infinite walk through distinct Gaussian primes with steps of length at most \(D\).

**Proof.** This is Theorem 1.1 of [Walks through Gaussian primes](walks-through-gaussian-primes.md), which was deduced there from Theorem 4.1 above by the periodic reduction (Theorem 4.1 of that lesson). \(\square\)

The auxiliary signed subsets \(\mathcal C\) were used only to average the information inequalities; the sieve \(\mathcal P_D\) itself is a fixed finite set, and it excludes both conjugate factors of each of its primes. The bound \(B_D\) given by the periodic reduction is \(8|\mathcal P_D|\bigl(1+(K_D-1)Q^2\bigr)\), where \(Q\) is the product of the primes of \(\mathcal P_D\); with the scales used here it is astronomically large, and the proof does not aim at a good bound.

The theorem concerns a fixed step bound. It says nothing about walks whose permitted step length grows with the distance from the origin, as in the percolation model of [Vardi], and it gives no useful estimate for \(B_D\) or for the distance from the origin that a walk with steps at most \(D\) can reach.

## 5. Exercises

**Exercise 5.1 (easy).** Show that \(DL_T<\sqrt T\) as soon as \(T>D^{10}\). Where is this inequality used?

**Exercise 5.2 (easy).** Let \(\Phi\) and \(\Psi\) be finite random variables and \(s\) a random element of \(\mathbb Z[i]\). Show directly that if \(\Phi'=\Phi+g(s)\) for a function \(g\) with values in a group, then \(H(W\mid\Phi,s)=H(W\mid\Phi',s)\) for every finite \(W\).

**Exercise 5.3 (medium).** Show that the walk must avoid the zero classes of *both* conjugate factors of each prime of the sieve for the proof of Proposition 2.1 to apply, by locating the step that uses this.

**Exercise 5.4 (medium).** Let \(\tau_0,\tau_1,\dots\) be a Markov chain on the nonnegative integers with finitely supported transitions, and let \(Y=f(\tau_0)\) for a function \(f\). Prove the analogue of (2.4): the conditional law of \(\tau_1\) given \(Y=y\) is the mixture of the transition laws from \(\tau_0=a\), with weights \(\mathbb P(\tau_0=a\mid Y=y)\).

**Exercise 5.5 (medium).** Verify the lower bound for the sum in (4.1): with \(X_m=100^m\), show that \(\sum_T1/\log T\ge0.019M/\log B\) for large \(M\).

## 6. Solutions

**5.1.** \(L_T\le T^{2/5}\), so \(DL_T\le DT^{2/5}<T^{1/2}\) when \(T^{1/10}>D\). It is used in Step 5 of the proof of Proposition 2.1, to show that two positions of one increment word are never congruent modulo a factor of norm \(p\ge T\).

**5.2.** The pairs \((\Phi,s)\) and \((\Phi',s)\) determine each other, since \(\Phi=\Phi'-g(s)\). So the events \(\{\Phi=\varphi,s=\sigma\}\) and \(\{\Phi'=\varphi+g(\sigma),s=\sigma\}\) coincide, the conditional laws of \(W\) agree, and so do the conditional entropies.

**5.3.** In Step 2, the true coordinate \(X_\pi\) passes every package because \(z_{t_*+l}\not\equiv0\pmod\pi\) for the selected factor \(\pi\). The selected factor of each prime is chosen by a fair coin, so either factor can be selected; the argument needs zero avoidance for both. (The averaging over signs is essential elsewhere: the coverage of Proposition 6.1 of the schedule lesson and the entropy profiles are statements about random signed coordinates.)

**5.4.** For a value \(y\) with \(\mathbb P(Y=y)>0\) and a set \(E\),

\[
\mathbb P(\tau_1\in E,Y=y)=\sum_{a:f(a)=y}\mathbb P(\tau_0=a)\,\mathbb P(\tau_1\in E\mid\tau_0=a),
\]

because the event \(\{Y=y\}\) is the union of the events \(\{\tau_0=a\}\) with \(f(a)=y\). Divide by \(\mathbb P(Y=y)\), and note that \(\mathbb P(\tau_0=a)/\mathbb P(Y=y)=\mathbb P(\tau_0=a\mid Y=y)\) for these \(a\) and vanishes for the others.

**5.5.** For \(m\) in \([\lceil M/2\rceil,M]\) there are at least \(M/2\) windows. The window \(m\) contains at least \(0.05X_m/\log B-1\) batches, which is at least \(0.04X_m/\log B\) once \(X_m\ge100\log B\); each has \(\log T\le1.05X_m\). So the window contributes at least \(0.04/(1.05\log B)\ge0.038/\log B\), and the total is at least \((M/2)(0.038/\log B)=0.019M/\log B\).

## References

- [OpenAI-moat] OpenAI, Bounded-step walks on Gaussian primes, preprint, 26 September 2026. https://github.com/openai/math/blob/main/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf
- [Tao 2016] T. Tao, The logarithmically averaged Chowla and Elliott conjectures for two-point correlations, Forum of Mathematics, Pi 4 (2016), e8. https://doi.org/10.1017/fmp.2016.6
- [Vardi] I. Vardi, Prime percolation, Experimental Mathematics 7 (1998), 275–289. https://projecteuclid.org/euclid.em/1047674208
