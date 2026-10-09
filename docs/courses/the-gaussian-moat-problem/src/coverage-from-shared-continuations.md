# Coverage from shared continuations

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Entropy measures how spread out a distribution is on average, but the Gaussian moat argument needs a pointwise statement: for most prime factors \(\pi\) of norm \(p\), the sampled walk position lies in each residue class modulo \(\pi\) with probability at least a constant times \(1/p\), apart from fewer than \(p^{1-\beta}\) exceptional classes. We call this *coverage*. Almost maximal entropy implies coverage only for very accurate entropy bounds, and such bounds are available only late in the sampling procedure. This lesson proves a transfer principle that moves coverage backwards in time at a small cost: if every continuation from a later checkpoint has coverage, and the position at that checkpoint has nearly maximal joint residue entropy, then the final position has coverage with a smaller exceptional set, seen from the earlier checkpoint.

The proof uses one vector of repeated continuations, shared by all residue coordinates. If coverage failed for many coordinates, this vector would place the true residue on a short list of candidates for each of them, and the total entropy saved would exceed what the vector can carry. The principle uses only finite abelian groups, and applies beyond Gaussian arithmetic.

We use [Entropy of finite random variables](entropy-of-finite-random-variables.md), in particular Propositions 7.2 and 7.3 and Lemma 6.1, and the binomial tail bounds of [Concentration and the discrete cube](concentration-and-the-discrete-cube.md). The lesson continues [Entropy enrichment](entropy-enrichment.md).

A basic reference is [OpenAI-moat].

## 1. Coverage

**Definition 1.1.** Let \(X\) be a random variable with values in a set \(G\) of \(p\) elements, and let \(\tau>0\) and \(0<\beta<1\). We say that \(X\) has **\((\tau,\beta)\)-coverage** if

\[
\#\{u\in G:\ \mathbb P(X=u)<\tau/p\}<p^{1-\beta}.
\]

The residues counted on the left are the **exceptional** residues. Coverage allows exceptional residues, but fewer than \(p^{1-\beta}\) of them; larger \(\beta\) means fewer exceptions, and larger \(\tau\) a higher floor. A uniformly distributed variable has \((\tau,\beta)\)-coverage for every \(\tau\le1\). Coverage depends only on the law, and is unchanged by translating \(X\) in a group \(G\).

Coverage of the conditional laws of a variable, with an exponent \(\beta'\), does not give the variable itself coverage with a larger exponent \(\beta\); Exercise 5.3 gives an example. The theorem below obtains such an improvement from entropy.

## 2. Signed coordinates on a lattice

Let \(\Lambda\) be a free abelian group of finite rank, and let \(k\ge1\). For \(1\le j\le k\) and each sign \(\pm\), let

\[
\phi_{j,\pm}:\Lambda\longrightarrow G_{j,\pm}
\]

be a homomorphism onto a finite abelian group of order \(p_j\). Assume \(T\le p_j\le2T\) for some \(T\ge2\). As in [Entropy enrichment](entropy-enrichment.md), a **signed coordinate** is a pair \(c=(j,\pm)\); write \(p_c\), \(G_c\), \(\phi_c\) accordingly. There are \(2k\) signed coordinates. Write \(\operatorname{av}_c\) for the mean over all of them, and

\[
\overline L=\frac1k\sum_{j=1}^k\log p_j=\operatorname{av}_c\log p_c,\qquad \log T\le\overline L\le\log(2T)\le2\log T.
\]

Let \(c_1,\dots,c_k\) be a random signed ordering, independent of everything else: a uniformly random ordering of \(\{1,\dots,k\}\) with independent fair signs. For a random element \(Y\) of \(\Lambda\) taking finitely many values, put

\[
F_s(Y)=\bigl(\phi_{c_1}(Y),\dots,\phi_{c_s}(Y)\bigr),\qquad f_Y(s)=\mathbb E\,H\bigl(F_s(Y)\bigr),
\]

entropies being computed with the ordering fixed and then averaged. The ordering is exchangeable and each \(c_i\) is uniform on the signed coordinates, so Propositions 7.2 and 7.3 of [Entropy of finite random variables](entropy-of-finite-random-variables.md) apply. In the Gaussian case, \(\Lambda=\mathbb Z[i]\), the indices \(j\) run through a batch of split primes, and \(\phi_{j,\pm}\) is reduction modulo the two conjugate factors of \(p_j\).

## 3. The transfer theorem

The experiment is as follows. Let \(A\) be a random variable taking finitely many values, let \(y\) be a map from these values to \(\Lambda\), and \(Y=y(A)\). For each value \(a\) of \(A\), let \(\nu_a\) be a probability law on \(\Lambda\) with finite support. Given \(A\), let \(h_1,\dots,h_n\) be independent with law \(\nu_A\), and put

\[
\mathcal H=(h_1,\dots,h_n),\qquad Z=Y+h_1.
\]

In the application, \(A\) is an exact intermediate time of the sampling procedure, \(Y\) the walk position at that time, \(\nu_a\) the law of the displacement from time \(a\) to the final time, and \(h_1,\dots,h_n\) are displacements of \(n\) independent continuations from that time. The variable \(A\) influences both \(Y\) and \(\mathcal H\); no independence between \(Y\) and \(\mathcal H\) is assumed. Every \(Y+h_l\) has the same law as \(Z\), because given \(A=a\) each \(h_l\) has law \(\nu_a\).

**Theorem 3.1** (one-step coverage transfer). Let \(1\le s\le k\) and \(n\ge1\) be integers, and let

\[
0<\tau\le\tfrac38,\quad 0<\delta\le\tfrac1{64},\quad \tau'=\tau+4\delta,\quad 0<\beta'\le\beta<1,\quad 0<\eta\le1,\quad 0\le\eta'\le1,\quad\varepsilon,\kappa\ge0.
\]

Assume:

1. *(coverage at the later checkpoint)* for every value \(a\) of \(A\), all but at most \(2k\eta'\) signed coordinates \(c\) have the property that \(\phi_c(y(a)+h_1)\), under the conditional law given \(A=a\), has \((\tau',\beta')\)-coverage;
2. *(entropy)* \(f_Y(s)\ge(1-\varepsilon)s\overline L\) and \(H(\mathcal H)\le\kappa s\overline L\);
3. *(budget)* \(\eta'\le\eta\delta/100\) and \(\varepsilon+\kappa\le\eta\delta\beta'/16\);
4. *(many trials)* for every \(j\), \(p_j\exp(-\delta^2np_j^{-\beta}/2)\le\delta/100\) and \(\delta^{-1}<p_j^{\beta'/2}\);
5. *(size)* \(\log(2e/\delta)\le(\beta'/4)\log T\).

Then all but at most \(2k\eta\) signed coordinates \(c\) have the property that \(\phi_c(Z)\) has \((\tau,\beta)\)-coverage.

**Proof.** Call a signed coordinate **deficient** if \(\phi_c(Z)\) fails \((\tau,\beta)\)-coverage, and suppose, for a contradiction, that the fraction \(\theta\) of deficient coordinates exceeds \(\eta\).

*Lists of candidates.* For a deficient coordinate \(c\), write \(p=p_c\) and \(u_p=\lceil p^{1-\beta}\rceil\), so that \(1\le u_p\le p\). There are at least \(p^{1-\beta}\), hence at least \(u_p\), residues \(u\) with \(\mathbb P(\phi_c(Z)=u)<\tau/p\); choose a set \(K_c\) of exactly \(u_p\) of them. Using the same data \(\mathcal H\) for every coordinate, define the list

\[
\mathcal L_c(\mathcal H)=\Bigl\{x\in G_c:\ \#\{l\le n:\ x+\phi_c(h_l)\in K_c\}\le n(\tau+\delta)\frac{u_p}p\Bigr\}.
\]

*The true residue is often on the list.* The number of \(l\) with \(\phi_c(Y)+\phi_c(h_l)\in K_c\) has expectation \(n\,\mathbb P(\phi_c(Z)\in K_c)<n\tau u_p/p\), because each \(Y+h_l\) has the law of \(Z\). By Markov's inequality,

\[
\mathbb P\bigl(\phi_c(Y)\in\mathcal L_c(\mathcal H)\bigr)\ge1-\frac\tau{\tau+\delta}=\frac\delta{\tau+\delta}\ge\delta.
\tag{3.1}
\]

This step uses only the common law of the \(Y+h_l\), not the independence of the trials.

*The list is usually short.* Fix a value \(a\) of \(A\) and a deficient coordinate \(c\) for which \(\phi_c(y(a)+h_1)\) has \((\tau',\beta')\)-coverage given \(A=a\). Translating by \(\phi_c(y(a))\), the conditional law of \(\phi_c(h_1)\) gives probability at least \(\tau'/p\) to every residue outside a set \(E_{a,c}\) with fewer than \(p^{1-\beta'}\) elements. In the group \(G_c\),

\[
\sum_{x\in G_c}\bigl|(K_c-x)\cap E_{a,c}\bigr|=u_p\,|E_{a,c}|,
\]

since each pair \((k,e)\in K_c\times E_{a,c}\) is counted exactly for \(x=k-e\). Hence at most \(|E_{a,c}|/\delta\) candidates \(x\) have \(|(K_c-x)\cap E_{a,c}|>\delta u_p\). Every other candidate \(x\) has at least \((1-\delta)u_p\) residues of \(K_c-x\) outside \(E_{a,c}\), so each trial satisfies

\[
\mathbb P\bigl(x+\phi_c(h_l)\in K_c\mid A=a\bigr)\ge(1-\delta)u_p\frac{\tau'}p\ge(\tau+2\delta)\frac{u_p}p=:\lambda,
\]

because \((\tau+4\delta)(1-\delta)-(\tau+2\delta)=\delta(2-\tau-4\delta)>0\). Given \(A=a\), the trials are independent, so the count for \(x\) is a sum of \(n\) independent indicators with success probability at least \(\lambda\). The candidate \(x\) is on the list only if this count is at most \(n(\lambda-\delta u_p/p)=(1-v)n\lambda\), with \(v=\delta/(\tau+2\delta)\). By Lemma 3.2 and Proposition 3.1 of [Concentration and the discrete cube](concentration-and-the-discrete-cube.md), this has conditional probability at most

\[
\exp\Bigl(-\frac{n\lambda v^2}2\Bigr)=\exp\Bigl(-\frac{n(\delta u_p/p)^2}{2\lambda}\Bigr)\le\exp\Bigl(-\frac{\delta^2n}2\cdot\frac{u_p}p\Bigr)\le\exp\Bigl(-\frac{\delta^2np^{-\beta}}2\Bigr),
\]

using \(\lambda\le u_p/p\) (as \(\tau+2\delta<1\)) and \(u_p/p\ge p^{-\beta}\). A union bound over at most \(p\) candidates and hypothesis 4 show that, with conditional probability at least \(1-\delta/100\), the list contains only candidates of the first kind; there are fewer than \(p^{1-\beta'}/\delta<p^{1-\beta'/2}\) of them, again by hypothesis 4. Thus

\[
\mathbb P\bigl(|\mathcal L_c(\mathcal H)|>p^{1-\beta'/2}\ \big|\ A=a\bigr)\le\frac\delta{100}
\tag{3.2}
\]

whenever \(c\) has the required coverage at \(a\).

*Averaging over the later checkpoint.* For a deficient \(c\), let \(\chi_c\) be the probability of the event that \(c\) lacks \((\tau',\beta')\)-coverage at the value of \(A\). By hypothesis 1, for each value \(a\) at most a fraction \(\eta'\) of all signed coordinates lack it, so the sum of \(\chi_c\) over all coordinates is at most \(2k\eta'\), and the mean of \(\chi_c\) over the deficient coordinates is at most \(\eta'/\theta<\eta'/\eta\le\delta/100\). For a deficient \(c\) put

\[
\rho_c=\mathbb P\bigl(\phi_c(Y)\in\mathcal L_c(\mathcal H)\text{ and }|\mathcal L_c(\mathcal H)|\le p_c^{1-\beta'/2}\bigr).
\]

By (3.1), (3.2) and the bound for \(\chi_c\), \(\rho_c\ge\delta-\chi_c-\delta/100\), so the mean \(\bar\rho\) of \(\rho_c\) over the deficient coordinates satisfies \(\bar\rho\ge\delta-\delta/50\ge\delta/2\).

*Too much information.* Lemma 6.1 of [Entropy of finite random variables](entropy-of-finite-random-variables.md), with \(a=p_c\) and \(b=p_c^{1-\beta'/2}\), gives for each deficient coordinate

\[
\log p_c-H\bigl(\phi_c(Y)\mid\mathcal H\bigr)\ge\rho_c\frac{\beta'}2\log p_c-h(\rho_c)\ge\rho_c\frac{\beta'}2\log T-h(\rho_c).
\]

The binary entropy \(h\) is concave, and \(h(u)\le u\log(e/u)\) by (4.1) of that lesson, so the mean of \(h(\rho_c)\) over the deficient coordinates is at most \(h(\bar\rho)\le\bar\rho\log(e/\bar\rho)\le\bar\rho\log(2e/\delta)\le\bar\rho\frac{\beta'}4\log T\), by hypothesis 5. Hence the mean over the deficient coordinates of \(\log p_c-H(\phi_c(Y)\mid\mathcal H)\) is at least

\[
\bar\rho\frac{\beta'}4\log T\ge\frac{\delta\beta'}8\log T.
\]

For every other coordinate this quantity is nonnegative, since \(\phi_c(Y)\) takes at most \(p_c\) values. Averaging over all \(2k\) signed coordinates, and using \(\theta>\eta\) and \(\overline L\le2\log T\),

\[
\operatorname{av}_c\bigl[\log p_c-H(\phi_c(Y)\mid\mathcal H)\bigr]>\frac{\eta\delta\beta'}8\log T\ge\frac{\eta\delta\beta'}{16}\overline L.
\]

But Proposition 7.3 of the entropy lesson, with hypothesis 2, bounds the left side by \((\varepsilon+\kappa)\overline L\le\frac{\eta\delta\beta'}{16}\overline L\), by hypothesis 3. This contradiction shows \(\theta\le\eta\). \(\square\)

The theorem lowers the probability floor from \(\tau'\) to \(\tau=\tau'-4\delta\), and improves the exponent from \(\beta'\) to \(\beta\). The only price is the entropy of the shared vector \(\mathcal H\), paid once for all coordinates. The independence of the trials is used only conditionally on the exact value of \(A\).

## 4. Iterating the transfer

The next lesson applies Theorem 3.1 backwards along a sequence of checkpoints \(A_J,A_{J-1},\dots,A_0\). At the last checkpoint, coverage comes from an extremely accurate entropy bound for single coordinates, through Pinsker's inequality. At each earlier checkpoint, the theorem is applied with \(A\) the next checkpoint, and with parameters arranged as follows:

\[
\tau_{i+1}=\tau_i+4\delta_i,\qquad \beta_{i+1}=\beta_i/2,\qquad \eta_{i+1}=\eta_i\delta_i/100.
\]

Thus the floor rises and the exponent halves when moving forward, so that going backwards the floor falls slightly and the exponent doubles at each step. The entropy hypothesis comes from Theorem 3.1 of [Entropy enrichment](entropy-enrichment.md), and the size of \(\mathcal H\) is controlled by the maximal length of the remaining displacements.

## 5. Exercises

**Exercise 5.1 (easy).** Show that if \(X\) has \((\tau,\beta)\)-coverage on a set of \(p\) elements, then \(X\) takes at least \(p-p^{1-\beta}\) values, and that \(\mathbb P(X\in S)\ge\tau(|S|-p^{1-\beta})/p\) for every set \(S\).

**Exercise 5.2 (easy).** Verify the identity \((\tau+4\delta)(1-\delta)-(\tau+2\delta)=\delta(2-\tau-4\delta)\), and show that it is positive in the range of Theorem 3.1.

**Exercise 5.3 (medium).** Show that hypothesis 2 of Theorem 3.1 cannot be dropped. Work in the Gaussian case with one split prime \(p\), so \(k=1\) and the two signed coordinates are reduction modulo \(\pi\) and \(\bar\pi\). Let \(m=\lceil p^{1-\beta}\rceil\) and assume \(m<p^{1-\beta'}\). Let \(A\) take a single value, and construct \(\nu_a\) so that both reductions of \(Z\) have exactly \(m\) residues of probability zero, while hypothesis 1 holds with \(\eta'=0\).

**Exercise 5.4 (medium).** Suppose that separate data \(\mathcal H_c\) were used for each coordinate, each with \(H(\mathcal H_c)\le\kappa s\overline L\). Show that the bound \(H(\phi_c(Y)\mid\mathcal H_c)\ge H(\phi_c(Y))-H(\mathcal H_c)\) only gives
\(\operatorname{av}_c[\log p_c-H(\phi_c(Y)\mid\mathcal H_c)]\le\varepsilon_1\overline L+\kappa s\overline L\), where \(\varepsilon_1\overline L=\operatorname{av}_c[\log p_c-H(\phi_c(Y))]\). Compare with Proposition 7.3 of the entropy lesson.

**Exercise 5.5 (medium).** In the last step of the proof, the individual probabilities \(\rho_c\) may be close to \(0\), and then \(\rho_c\frac{\beta'}2\log p_c-h(\rho_c)\) may be negative. Explain how the proof deals with this.

## 6. Solutions

**5.1.** At most \(p^{1-\beta}\) residues have probability below \(\tau/p\), so the others have positive probability; and \(S\) contains at least \(|S|-p^{1-\beta}\) residues of probability at least \(\tau/p\).

**5.2.** Expanding, \((\tau+4\delta)(1-\delta)=\tau+4\delta-\tau\delta-4\delta^2\); subtracting \(\tau+2\delta\) leaves \(2\delta-\tau\delta-4\delta^2\). For \(\tau\le\frac38\) and \(\delta\le\frac1{64}\), the factor \(2-\tau-4\delta\) is positive.

**5.3.** Let \(M_+\) and \(M_-\) be sets of \(m\) residues modulo \(\pi\) and modulo \(\bar\pi\). By Exercise 7.4 of [Walks through Gaussian primes](walks-through-gaussian-primes.md), reduction gives a bijection from \(\mathbb Z[i]/p\mathbb Z[i]\) onto \(\mathbb Z[i]/(\pi)\times\mathbb Z[i]/(\bar\pi)\). Let \(\nu_a\) be uniform on a set of representatives of the pairs outside \(M_+\times\mathbb Z[i]/(\bar\pi)\) and \(\mathbb Z[i]/(\pi)\times M_-\). Then each reduction of \(h_1\) is uniform on the \(p-m\) residues outside \(M_\pm\), each of probability \(1/(p-m)\ge\tau'/p\), and \(Z=y(a)+h_1\) is a translate. Each reduction has exactly \(m<p^{1-\beta'}\) exceptional residues, so hypothesis 1 holds with \(\eta'=0\); but \(m\ge p^{1-\beta}\), so neither reduction of \(Z\) has \((\tau,\beta)\)-coverage. Here \(Y\) is constant, \(f_Y\equiv0\), so hypothesis 2 forces \(\varepsilon\ge1\), and hypothesis 3 fails.

**5.4.** For each coordinate, \(\log p_c-H(\phi_c(Y)\mid\mathcal H_c)\le\bigl(\log p_c-H(\phi_c(Y))\bigr)+H(\mathcal H_c)\); averaging gives the stated bound. The data cost now appears as \(\kappa s\overline L\) for each coordinate, a factor \(s\) larger than the charge \(\kappa\overline L\) of Proposition 7.3 of the entropy lesson, where one shared vector is paid for once against the joint entropy of \(s\) coordinates. In the application \(s\) is very large, and a cost of \(\kappa s\overline L\) per coordinate would exceed the maximal possible deficit \(\log p_c\) unless \(\kappa<1/s\).

**5.5.** The proof never bounds a single \(h(\rho_c)\). It averages over the deficient coordinates: the gain terms average to \(\bar\rho\frac{\beta'}2\) times at least \(\log T\), while concavity of \(h\) bounds the mean of \(h(\rho_c)\) by \(h(\bar\rho)\), and \(\bar\rho\ge\delta/2\) with hypothesis 5 makes \(h(\bar\rho)\) at most half of the mean gain. Individual coordinates with small \(\rho_c\) are thereby absorbed.

## References

- [OpenAI-moat] OpenAI, Bounded-step walks on Gaussian primes, preprint, 26 September 2026. https://github.com/openai/math/blob/main/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf
