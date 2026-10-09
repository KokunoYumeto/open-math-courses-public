# A common sampling schedule

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson builds one random procedure that samples a time on a fixed walk with bounded steps, and proves everything the final argument of the Gaussian moat course needs to know about it. The procedure applies the entropy enrichment transition of [Entropy enrichment](entropy-enrichment.md) at a decreasing sequence of scales, arranged in bands, and ends with a uniformly random time offset. We prove four kinds of estimates, uniformly over all walks: the time shift after any stage is controlled, and small translates of the final time have almost the same law; each batch of primes acquires a joint residue entropy of order \(T\) that survives to the end; at a sequence of checkpoints the residue entropy is almost maximal; and the final residues have coverage seen from every checkpoint. The last estimate is proved by backward induction with the transfer theorem of [Coverage from shared continuations](coverage-from-shared-continuations.md).

We use the prime counts of Section 5 of [Walks through Gaussian primes](walks-through-gaussian-primes.md), the displacement bounds of [Differences of a walk and separating products](differences-of-a-walk-and-separating-products.md), Pinsker's inequality from [Entropy of finite random variables](entropy-of-finite-random-variables.md), and the two preceding lessons.

A basic reference is [OpenAI-moat].

## 1. Constants, windows and batches

Fix \(D\ge1\) and an infinite \(D\)-walk \(z_0,z_1,\dots\); no congruence condition is assumed in this lesson. The following absolute constants are fixed once and for all, in this order:

| Constant | Value | Role |
|---|---|---|
| \(\beta_0\) | \(1/200\) | coverage exponent at the first checkpoint |
| \(e_0\) | \(\beta_0/50=10^{-4}\) | allowed entropy deficit of each batch |
| \(l_0\) | \(15\) | number of transitions that create batch entropy |
| \(g_0\) | \(10^{-6}\) | transition parameter of the top bands |
| \(a_0\) | \(1/4\) | where the batch entropy is created |
| \(c_0\) | \(a_0g_0^{2(l_0+1)}/2\) | size of the batch entropy, in units of \(T\) |
| \(B\) | \(2+(8\log2)/(e_0c_0)\) | ratio between consecutive batches |

They satisfy \(2^{-l_0}+40g_0<e_0\). Let \(M\) be a positive integer, the only parameter that will tend to infinity. Put

\[
X_m=100^m\quad\Bigl(\Bigl\lceil\frac M2\Bigr\rceil\le m\le M\Bigr),\qquad g_1=e^{-M^3},\qquad g_2=e^{-100M^{20}},\qquad T_+=e^{1.05X_M}.
\]

The interval \([X_m,1.05X_m]\) is the \(m\)-th **window**. The **batches** used are the sets \(\mathcal B_T\) of Section 5 of the first lesson for all

\[
T=B^j\ (j\in\mathbb Z)\qquad\text{with}\qquad X_m\le\log T\le1.05X_m\ \text{for some}\ \Bigl\lceil\frac M2\Bigr\rceil\le m\le M.
\]

They are pairwise disjoint (Lemma 5.2 of the first lesson). Their union \(\mathcal P_M\) is a finite set of primes congruent to \(1\) modulo \(4\). For a batch we write \(k=k_T\) and \(L_*=L^*_T\), and the signed coordinates and residue entropy profiles \(f_Z\) of [Entropy enrichment](entropy-enrichment.md) refer to that batch.

**Convention.** "For large \(M\)" means "for all \(M\ge M_D\)", where \(M_D\) depends only on \(D\). Each lemma below may enlarge \(M_D\), finitely many times. Every estimate is uniform over the walk, the batches, and the starting times.

For example, for large \(M\) every batch satisfies \(T\ge5\), \(k_T\ge a_0T/L_*\) and \(k_T\ge T^{1/2}\), by Proposition 5.1 of the first lesson, since \(\log T\ge X_{\lceil M/2\rceil}\ge10^M\).

## 2. The schedule

**Definition 2.1** (bands). For each window \(m\) there are three **bands** of scales \(U\), given by intervals for \(\log U\) and a transition parameter:

| Band | \(\log U\) in | parameter |
|---|---|---|
| top | \([0.8X_m,\ 1.3X_m]\) | \(g_0\) |
| middle | \([0.20X_m,\ 0.30X_m]\) | \(g_1=e^{-M^3}\) |
| bottom | \([0.05X_m,\ 0.10X_m]\) | \(g_2=e^{-100M^{20}}\) |

The **scheduled scales** of a band with parameter \(g\) are the numbers \(U\) with \(\log U=u_{\max}-2i\log(1/g)\), \(i=0,1,2,\dots\), that lie in the band, where \(u_{\max}\) is its upper end. Consecutive scheduled scales in a band have ratio \(g^2\).

The bands are disjoint and ordered: within a window, the top band lies above the middle band, which lies above the bottom band; and the top band of window \(m-1\) lies below the bottom band of window \(m\), since \(1.3X_{m-1}=0.013X_m<0.05X_m\).

**Definition 2.2** (the schedule). The **schedule** is the following finite list of operations. Go through the windows \(m=M,M-1,\dots,\lceil M/2\rceil\); in each, go through the top, middle and bottom bands; in each band, go through its scheduled scales in decreasing order. For each scheduled scale \(U\), with the parameter \(g\) of its band, the operation is the transition of Definition 2.1 of [Entropy enrichment](entropy-enrichment.md) with parameters \(U,g\). The last operation adds to the current time an independent uniformly random integer in \(\{0,1,\dots,N-1\}\), where \(N=\lceil T_+^{10}\rceil\).

A **checkpoint** is a position in this list: the stage just before a given operation, or the final stage. Running the schedule from time \(0\), with fresh randomness for each operation, gives a random time at each checkpoint; we use the same letter for the checkpoint and its random time. The final random time is denoted \(t_*\).

Every operation acts on the current time only: given the current time, its randomness is fresh. So for a checkpoint \(A\) and an integer \(a\ge0\), we may run the remaining operations from the deterministic time \(a\). We call this the **continuation experiment from the exact start \(A=a\)**. It is defined for every \(a\), whether or not \(a\) is a possible value of \(A\) in the run from time \(0\); and when \(\mathbb P(A=a)>0\), the conditional law of the remaining run given \(A=a\) is the law of this continuation experiment. Every random time in such an experiment takes finitely many values.

## 3. Future shifts and smoothing

**Lemma 3.1** (future shifts). For large \(M\) the following holds. Let \(V\) be a scheduled scale, with parameter \(g\). There is a number \(S_V\), depending only on the schedule, such that in every continuation experiment from the checkpoint before \(V\), every later checkpoint is at most \(S_V\) steps later, and

\[
\log(1+S_V)\le2gV.
\]

Consequently, for random times \(A\le A'\) at that checkpoint and a later one, \(H(z_{A'}-z_A)\le4gV+\log(\pi D^2)\).

**Proof.** A transition with parameters \(U,g_U\) advances time by at most \(\lfloor e^{g_UU}\rfloor\), and the final offset by at most \(N-1\). Let \(S_V\) be \(N-1\) plus the sum of \(\lfloor e^{g_UU}\rfloor\) over \(V\) and all later scheduled scales \(U\).

The number of operations is at most the sum, over windows and bands, of \(1+(\text{band length})/(2\log(1/g))\), which is at most \(4X_M\) for large \(M\). For a later scale \(U\) in the band of \(V\), \(g_UU\le gV\). For a scale \(U\) in a later band, \(\log U\le\log V-0.037X_{\lceil M/2\rceil}\), as the gaps between consecutive bands are at least \(0.037X_m\); and \(\log(g_U/g)\le\log(1/g_2)=100M^{20}\). Since \(0.037X_{\lceil M/2\rceil}\ge0.037\cdot10^M>100M^{20}\) for large \(M\), again \(g_UU\le gV\). Hence

\[
1+S_V\le N+4X_Me^{gV}\le2\max\{N,4X_Me^{gV}\}.
\]

Now \(\log N\le10.5X_M+1\) and \(\log(4X_M)\le5M\), while \(gV\ge g_2e^{0.05X_{\lceil M/2\rceil}}\ge\exp(0.05\cdot10^M-100M^{20})\), which exceeds \(11X_M+5M+1\) for large \(M\). So \(\log(1+S_V)\le\log2+gV+\max\{11X_M,5M\}\le2gV\). The entropy bound follows from Lemma 1.2 of [Differences of a walk and separating products](differences-of-a-walk-and-separating-products.md). \(\square\)

**Lemma 3.2** (smoothing). In every continuation experiment, from any exact start at any checkpoint before the final offset,

\[
\operatorname{TV}\bigl(\mathcal L(t_*),\mathcal L(t_*+a)\bigr)\le T_+^{-9}\qquad(0\le a\le T_+),
\]

where \(\mathcal L\) denotes the law. The same bound holds for the laws of \(\Phi(t_*)\) and \(\Phi(t_*+a)\), for every function \(\Phi\) of the time.

**Proof.** Write \(t_*=\tilde t+O\), where \(O\) is the final offset, uniform on \(\{0,\dots,N-1\}\) and independent of \(\tilde t\). The laws of \(O\) and \(O+a\) differ by \(a/N\) in total variation. Since \(\mathcal L(t_*)=\sum_t\mathbb P(\tilde t=t)\,\mathcal L(t+O)\) and similarly for \(t_*+a\), and translations and mixtures do not increase total variation (Section 5 of the entropy lesson), the distance is at most \(a/N\le T_+/T_+^{10}\). Images under \(\Phi\) do not increase it either. \(\square\)

## 4. Entropy that survives

**Lemma 4.1** (a run in one band). For large \(M\) the following holds. Let \(T\) be a batch, and let \(U_0>U_1>\dots>U_l\) be consecutive scheduled scales of one band, with parameter \(g\), such that \(\lfloor U_0/L_*\rfloor\le k_T\). Run the schedule, in any experiment that starts at or before the checkpoint before \(U_0\). Then at the checkpoint before \(U_l\), and at every later checkpoint, the point \(Z\) satisfies

\[
\operatorname{def}_Z\bigl(\lfloor U_l/L_*\rfloor\bigr)\le2^{-l}+40g+\frac{2\log(\pi D^2)}{U_l}.
\]

**Proof.** The hypotheses of Theorem 3.1 of [Entropy enrichment](entropy-enrichment.md) hold for each \((U_j,g)\), \(j<l\): the subset sizes are at most \(k_T\), and \(g^5U_j\ge g^3U_l\ge g_2^3e^{0.05X_{\lceil M/2\rceil}}\), which exceeds \(K_D\log T\le K_D\cdot1.05X_M\) for large \(M\). Corollary 4.1 there gives deficit at most \(2^{-l}+32g\) at the checkpoint before \(U_l\), at the size \(s=\lfloor U_l/L_*\rfloor\); the starting law plays no role. For a later checkpoint, Proposition 1.1(3) of that lesson and Lemma 3.1 lower the profile at \(s\) by at most \(4gU_l+\log(\pi D^2)\), while \(sL_*\ge U_l-L_*\ge U_l/2\). \(\square\)

For a batch \(T\) in window \(m\), let \(U^{(T)}\) be the first scheduled scale of the top band of window \(m\) with \(U^{(T)}\le a_0T\). It exists and satisfies \(g_0^2a_0T<U^{(T)}\le a_0T\), because \(\log(a_0T)\) lies in \([X_m-\log4,\ 1.05X_m]\), well inside the band. Let \(V_T=g_0^{2l_0}U^{(T)}\), again a scheduled top-band scale, and put

\[
q_T=\Bigl\lfloor\frac{V_T}{L_*}\Bigr\rfloor.
\]

**Proposition 4.2** (batch entropy). For large \(M\), every batch \(T\) satisfies \(q_TL_*\ge c_0T\) and \(q_T\le k_T\). In the run from time \(0\), at the checkpoint before \(V_T\) and at every later checkpoint, the point \(Z\) satisfies

\[
f_Z(q_T)\ge(1-e_0)\,q_TL_*.
\]

**Proof.** Since \(\lfloor U^{(T)}/L_*\rfloor\le a_0T/L_*\le k_T\), Lemma 4.1 applies with \(l=l_0\), \(g=g_0\) and \(U_l=V_T\). The deficit is at most \(2^{-l_0}+40g_0+2\log(\pi D^2)/V_T<e_0\) for large \(M\), by the choice of \(l_0\) and \(g_0\). Finally \(q_TL_*\ge V_T-L_*\ge V_T/2>a_0g_0^{2(l_0+1)}T/2=c_0T\), and \(q_T\le U^{(T)}/L_*\le k_T\). \(\square\)

**Proposition 4.3** (smaller batches are cheap). Every batch \(T\) satisfies

\[
\sum_{\text{batches }T'<T}k_{T'}\log(2T')\le e_0c_0T.
\]

**Proof.** The batches are powers of \(B\), so Lemma 5.2 of the first lesson bounds the sum by \((8\log2)T/(B-1)\le e_0c_0T\), by the choice of \(B\). \(\square\)

The top bands thus give every batch near \(T\) an entropy of order \(T\), and the geometric spacing of the batches makes all residues of the smaller batches together cost only a small fraction of it.

## 5. Checkpoints for the coverage induction

Fix a batch \(T\) in window \(m\). Define

\[
\beta_i=2^{-i}\beta_0,\qquad r_0=\tfrac14,\qquad r_{i+1}=r_i-2\beta_i,
\]

so that \(r_i=\frac14-4\beta_0(1-2^{-i})\in(0.23,0.25]\). Let \(J=J(T)\) be the least index with \(\beta_J\log T\le M^{20}\). For large \(M\), \(\beta_0\log T>M^{20}\), so \(J\ge1\), and by minimality

\[
\frac{M^{20}}2<\beta_J\log T\le M^{20},\qquad J\le7M.
\tag{5.1}
\]

The bound on \(J\) holds because \(2^{-J}\ge M^{20}/(2\beta_0\log T)\ge1/(2\cdot1.05\cdot100^M)\) for \(M\ge1\).

Let \(A_i\) be the checkpoint just before the first scheduled operation with scale \(U\le T^{r_i}\), for \(0\le i\le J\). Since \(0.23X_m<r_i\log T\le0.2625X_m\), this scale lies in the middle band of window \(m\), and it lies in \((g_1^2T^{r_i},T^{r_i}]\). Let \(S_i\) be the number \(S_V\) of Lemma 3.1 for this scale, and

\[
\mathcal D_i=\{v\in\mathbb Z[i]:\ |v|\le DS_i\}.
\]

**Lemma 5.1** (common support of later displacements). For large \(M\): in every continuation experiment from an exact start at \(A_i\), every displacement from \(A_i\) to a later checkpoint lies in \(\mathcal D_i\), and \(\log|\mathcal D_i|\le T^{r_i}\).

**Proof.** The time shift is at most \(S_i\), and each step has length at most \(D\). By Lemma 1.1 of the geometric lesson and Lemma 3.1, \(\log|\mathcal D_i|\le\log\pi+2\log(DS_i+1)\le\log(\pi D^2)+4g_1T^{r_i}\le T^{r_i}\). \(\square\)

The set \(\mathcal D_i\) does not depend on the exact start. This common support bound will control the entropy of displacements from a random checkpoint, without conditioning on its value.

**Proposition 5.2** (entropy between checkpoints). For large \(M\) and \(0\le i<J\), there is a number \(s_i\le k_T\), depending only on the batch and the schedule, such that in the continuation experiment from every exact start at \(A_i\), the point \(Y=z_{A_{i+1}}\) satisfies

\[
f_Y(s_i)\ge\bigl(1-e^{-M^3/2}\bigr)s_iL_*,\qquad s_iL_*\ge\exp\bigl(r_i\log T-4M^6\bigr).
\]

**Proof.** Let \(U_0\) be the scale at \(A_i\), and \(U_0>\dots>U_l\) the next scheduled scales, with \(l=\lceil M^3\rceil\); put \(s_i=\lfloor U_l/L_*\rfloor\). They lie in the middle band and before \(A_{i+1}\): they use at most \((l+1)\cdot2M^3\le3M^6\) units of \(\log U\), whereas \((r_i-r_{i+1})\log T=2\beta_i\log T>2M^{20}\) because \(i<J\). Also \(U_0/L_*\le T^{1/4}\le k_T\). Lemma 4.1 gives, at \(A_{i+1}\), deficit at most \(2^{-M^3}+40e^{-M^3}+2\log(\pi D^2)/U_l\le e^{-M^3/2}\). Finally \(U_l\ge g_1^{2l+2}T^{r_i}\ge\exp(r_i\log T-3M^6)\) and \(s_iL_*\ge U_l/2\). \(\square\)

**Proposition 5.3** (terminal entropy). For large \(M\), in the continuation experiment from every exact start at \(A_J\),

\[
\operatorname{av}_c\bigl[\log p_c-H(z_{t_*}\bmod\pi_c)\bigr]\le e^{-90M^{20}}L_*,
\]

the mean being over the \(2k_T\) signed coordinates of the batch.

**Proof.** After \(A_J\) the schedule reaches the bottom band of window \(m\). Let \(U_0\) be its first scale and \(U_0>\dots>U_l\) the following ones, with \(l=\lceil200M^{20}\rceil\). They use at most \((l+1)\cdot200M^{20}\le5\cdot10^4M^{40}\) units of \(\log U\), less than the band length \(0.05X_m\) for large \(M\), and \(U_0/L_*\le e^{0.1X_m}\le k_T\). Lemma 4.1 gives, at the final checkpoint, deficit at most \(2^{-200M^{20}}+40e^{-100M^{20}}+2\log(\pi D^2)/U_l\le e^{-90M^{20}}\) at \(s=\lfloor U_l/L_*\rfloor\). By concavity (Proposition 1.1(2) of [Entropy enrichment](entropy-enrichment.md)), \(f_{z_{t_*}}(1)\ge f_{z_{t_*}}(s)/s\ge(1-e^{-90M^{20}})L_*\). Since the first index of a random signed ordering is uniform on the signed coordinates, \(f_{z_{t_*}}(1)=\operatorname{av}_cH(z_{t_*}\bmod\pi_c)\), and \(\operatorname{av}_c\log p_c=L_*\). \(\square\)

## 6. Coverage at every checkpoint

For a signed coordinate \(c\) of the batch, with prime \(p=p_c\), a checkpoint \(A_i\) and an integer \(a\ge0\), let \(b_{i,a,c}\) be the law of \(z_{t_*}\bmod\pi_c\) in the continuation experiment from the exact start \(A_i=a\). Define

\[
\tau_0=\tfrac14,\quad\delta_i=2^{-i-6},\quad\tau_{i+1}=\tau_i+4\delta_i,\qquad \eta_0=\tfrac1{100},\quad\eta_{i+1}=\frac{\eta_i\delta_i}{100}.
\]

Then \(\tau_i=\frac38-2^{-i-3}<\frac38\) and \(\eta_i=100^{-(i+1)}2^{-i(i-1)/2-6i}\). By (5.1), \(\log(1/\delta_i)\le8M\), and for an absolute constant \(C\),

\[
\eta_i\ge e^{-CM^2},\qquad \eta_i\delta_i\beta_{i+1}\ge e^{-CM^2}\qquad(0\le i\le J).
\tag{6.1}
\]

**Proposition 6.1** (terminal coverage). For large \(M\), for every batch \(T\), every \(0\le i\le J(T)\) and every integer \(a\ge0\), all but at most \(2k_T\eta_i\) signed coordinates \(c\) of the batch satisfy

\[
\#\Bigl\{u\in\mathbb Z[i]/(\pi_c):\ b_{i,a,c}(u)<\frac{\tau_i}{p_c}\Bigr\}<p_c^{1-\beta_i},
\]

that is, \(b_{i,a,c}\) has \((\tau_i,\beta_i)\)-coverage.

**Proof.** We proceed by downward induction on \(i\).

*The base \(i=J\).* Fix an exact start at \(A_J\). For each coordinate, \(\log p_c-H(z_{t_*}\bmod\pi_c)\) is the relative entropy of \(b_{J,a,c}\) from the uniform law, by (5.1) of the entropy lesson. If a coordinate fails \((\tau_J,\beta_J)\)-coverage, its set \(K\) of residues of probability below \(\tau_J/p\) has at least \(p^{1-\beta_J}\) elements, and the uniform law gives \(K\) at least \((1-\tau_J)|K|/p\ge\frac58p^{-\beta_J}\) more mass than \(b_{J,a,c}\). Since \(p\le2T\) and \(\beta_J\log T\le M^{20}\), this total variation is at least \(\frac5{16}e^{-M^{20}}\), and Pinsker's inequality gives relative entropy at least \(2(\frac5{16})^2e^{-2M^{20}}\ge\frac16e^{-2M^{20}}\). By Proposition 5.3, the fraction of failing coordinates is at most

\[
6e^{-88M^{20}}L_*\le6e^{-88M^{20}}\cdot2.1\cdot100^M<e^{-CM^2}\le\eta_J
\]

for large \(M\).

*The step from \(i+1\) to \(i\).* Assume the assertion for \(i+1\), and fix an exact start \(A_i=a\). Apply Theorem 3.1 of [Coverage from shared continuations](coverage-from-shared-continuations.md) with \(\Lambda=\mathbb Z[i]\), the signed coordinates of the batch, the mixing variable \(A=A_{i+1}\) in this experiment, \(y(a')=z_{a'}\), and \(\nu_{a'}\) the law of \(z_{t_*}-z_{a'}\) in the continuation experiment from the exact start \(A_{i+1}=a'\). Given \(A_{i+1}\), draw \(n=n_i=\lceil T^{6\beta_i/5}\rceil\) independent continuations to the final time, and let \(h_1,\dots,h_n\) be their displacements from \(Y=z_{A_{i+1}}\). Then \(Z=Y+h_1\) has the law of \(z_{t_*}\) in the experiment from \(A_i=a\), so the conclusion of the theorem is the assertion for \(i\) at the start \(a\). We check its hypotheses with

\[
(\tau,\delta,\tau',\beta,\beta',\eta,\eta')=(\tau_i,\delta_i,\tau_{i+1},\beta_i,\beta_{i+1},\eta_i,\eta_{i+1}),\qquad s=s_i.
\]

1. *Coverage at the later checkpoint:* this is the induction hypothesis at every exact start \(a'\) of \(A_{i+1}\).
2. *Entropy:* Proposition 5.2 gives \(f_Y(s_i)\ge(1-\varepsilon)s_iL_*\) with \(\varepsilon=e^{-M^3/2}\). Every \(h_l\) lies in \(\mathcal D_{i+1}\), whatever the value of \(A_{i+1}\), by Lemma 5.1. Hence \(H(\mathcal H)\le n\log|\mathcal D_{i+1}|\le2T^{6\beta_i/5}T^{r_{i+1}}\), and since \(r_i-r_{i+1}=2\beta_i\) and \(\beta_i\log T>M^{20}\),
\[
\kappa=\frac{H(\mathcal H)}{s_iL_*}\le2\exp\Bigl(-\frac45\beta_i\log T+4M^6\Bigr)\le e^{-M^3}.
\]
3. *Budget:* \(\eta_{i+1}=\eta_i\delta_i/100\), and \(\varepsilon+\kappa\le2e^{-M^3/2}\le\eta_i\delta_i\beta_{i+1}/16\) by (6.1), for large \(M\).
4. *Many trials:* for every prime \(p\) of the batch, \(T\le p\le2T\) gives \(np^{-\beta_i}\ge2^{-\beta_i}T^{\beta_i/5}\ge\frac12e^{M^{20}/5}\), so \(\delta_i^2np^{-\beta_i}/2\ge e^{M^{20}/5-17M}\), which exceeds \(\log p+\log(100/\delta_i)\le2.1\cdot100^M+9M\) for large \(M\); this gives \(p\exp(-\delta_i^2np^{-\beta_i}/2)\le\delta_i/100\). Also \(\log(1/\delta_i)\le8M<M^{20}/4<\frac{\beta_{i+1}}2\log p\), by (5.1).
5. *Size:* \(\log(2e/\delta_i)\le8M+2<M^{20}/8<\frac{\beta_{i+1}}4\log T\).

The theorem gives the assertion for \(i\) at the start \(a\), which was arbitrary. \(\square\)

At the first checkpoint, the conclusion reads: from every exact start at \(A_0\), for at least \(99\%\) of the signed coordinates, the final residue takes every value with probability at least \(1/(4p)\), apart from fewer than \(p^{199/200}\) exceptional values.

## 7. Exercises

**Exercise 7.1 (easy).** Check that \(2^{-15}+40\cdot10^{-6}<10^{-4}\), while \(2^{-14}+40\cdot10^{-6}>10^{-4}\). Which inequality between the constants does the proof of Proposition 4.2 need?

**Exercise 7.2 (easy).** Verify the formulas \(r_i=\frac14-4\beta_0(1-2^{-i})\), \(\tau_i=\frac38-2^{-i-3}\) and \(\eta_i=100^{-(i+1)}2^{-i(i-1)/2-6i}\) by induction.

**Exercise 7.3 (medium).** Show that the number of batches \(T=B^j\) in the window \([X_m,1.05X_m]\) is at least \(0.05X_m/\log B-1\).

**Exercise 7.4 (medium).** Explain why Lemma 5.1 bounds \(H(\mathcal H)\) without conditioning on \(A_{i+1}\), although the displacements \(h_l\) are independent only given \(A_{i+1}\).

**Exercise 7.5 (medium).** Show that in Lemma 3.2 the offset length \(N\) cannot be much smaller: if the final offset were uniform on \(\{0,\dots,N-1\}\), then the total variation between the laws of \(O\) and \(O+a\) equals \(a/N\) for \(0\le a\le N\).

## 8. Solutions

**7.1.** \(2^{-15}\approx3.05\cdot10^{-5}\) and \(2^{-14}\approx6.10\cdot10^{-5}\); with \(4\cdot10^{-5}\) added, the sums are about \(7.05\cdot10^{-5}\) and \(1.01\cdot10^{-4}\). The proof needs the strict inequality \(2^{-l_0}+40g_0<e_0\), which leaves room for the term \(2\log(\pi D^2)/V_T\); that term tends to \(0\) as \(M\) grows. So \(l_0=15\) is the least admissible value with \(g_0=10^{-6}\).

**7.2.** For \(r_i\): \(r_{i+1}=\frac14-4\beta_0(1-2^{-i})-2^{1-i}\beta_0=\frac14-4\beta_0(1-2^{-i-1})\). For \(\tau_i\): \(\frac38-2^{-i-3}+4\cdot2^{-i-6}=\frac38-2^{-i-4}\). For \(\eta_i\): multiplying by \(\delta_i/100=2^{-i-6}/100\) raises the power of \(100\) by one and adds \(i+6\) to the exponent of \(2\), and \(\frac{i(i-1)}2+6i+i+6=\frac{(i+1)i}2+6(i+1)\).

**7.3.** The numbers \(j\log B\) with \(X_m\le j\log B\le1.05X_m\) are the integers \(j\) in an interval of length \(0.05X_m/\log B\), and such an interval contains at least its length minus one integers.

**7.4.** For each value \(a'\) of \(A_{i+1}\), every \(h_l\) lies in \(\mathcal D_{i+1}\), a set that does not depend on \(a'\). So the vector \(\mathcal H\) takes values in \(\mathcal D_{i+1}^n\), and \(H(\mathcal H)\le n\log|\mathcal D_{i+1}|\) by Corollary 1.3 of the entropy lesson, with no independence needed.

**7.5.** The laws of \(O\) and \(O+a\) are uniform on \(\{0,\dots,N-1\}\) and \(\{a,\dots,a+N-1\}\); they agree on the overlap of \(N-a\) points and differ on \(a\) points at each end, each of mass \(1/N\). So the distance is \(a/N\). To make it at most \(T_+^{-9}\) for shifts up to \(T_+\), one needs \(N\ge T_+^{10}\).

## References

- [OpenAI-moat] OpenAI, Bounded-step walks on Gaussian primes, preprint, 26 September 2026. https://github.com/openai/math/blob/main/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf
