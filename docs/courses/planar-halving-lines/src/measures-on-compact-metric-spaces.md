# Measures on compact metric spaces

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The limit argument of this course replaces sequences of finite point configurations by limiting measures and limiting sets. This lesson collects the tools, with proofs, on a compact metric space \(K\): regularity of finite Borel measures; weak convergence and its inequalities for open and closed sets; compactness of bounded sequences of measures; Hausdorff limits of closed sets; and conditional measures of a measure on a product \(Z\times[0,1]\) given the first coordinate. Two results are taken from other courses: the Riesz representation theorem, Theorem 2.2 of the programme's lesson [Haar measure on locally compact groups](course:AN-01/prerequisites/riesz/positive-riesz), and the monotone class theorem, 136B of [Fremlin], the text of the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10). Later lessons also use the Radon–Nikodym theorem [Fremlin, 232E] and the Lebesgue decomposition [Fremlin, 232I] from that course.

All measures are nonnegative, finite and defined on the Borel sets. The *closed \(\rho\)-neighbourhood* of a set \(F\) is \(F^{[\rho]}=\{x:d(x,F)\le\rho\}\), and the open one is \(\{x:d(x,F)<\rho\}\).

## 1. Regularity

**Lemma 1.1.** Let \(\mu\) be a finite Borel measure on a metric space \(X\). For every Borel set \(A\) and every \(\epsilon>0\) there are a closed \(F\) and an open \(U\) with \(F\subseteq A\subseteq U\) and \(\mu(U\setminus F)<\epsilon\). If \(X\) is compact, \(F\) is compact.

*Proof.* Let \(\mathcal A\) be the family of Borel sets with this property. It contains every closed set \(F\): the open sets \(\{x:d(x,F)<1/m\}\) decrease to \(F\), so their measures decrease to \(\mu(F)\). It is closed under complements, exchanging the roles of \(F\) and \(U\). For a sequence \(A_i\in\mathcal A\), choose \(F_i\subseteq A_i\subseteq U_i\) with \(\mu(U_i\setminus F_i)<\epsilon2^{-i-1}\); then \(U=\bigcup U_i\) is open, and for \(m\) large the closed set \(F=F_1\cup\dots\cup F_m\) satisfies \(\mu(\bigcup A_i\setminus F)<\epsilon/2\), so \(\mu(U\setminus F)<\epsilon\). Thus \(\mathcal A\) is a \(\sigma\)-algebra containing the closed sets, hence all Borel sets. In a compact space closed sets are compact. \(\square\)

## 2. Weak convergence

Measures \(\mu_n\) on a compact metric space \(K\) *converge weakly* to \(\mu\) if \(\int f\,d\mu_n\to\int f\,d\mu\) for every continuous \(f:K\to\mathbb R\). The limit is unique, by Lemma 1.1 and Urysohn functions: for closed \(F\), the functions \(\max(0,1-m\,d(\cdot,F))\) decrease to the indicator of \(F\).

**Lemma 2.1.** Let \(\mu_n\to\mu\) weakly on \(K\).

(a) \(\mu_n(K)\to\mu(K)\); \(\liminf\mu_n(U)\ge\mu(U)\) for open \(U\); \(\limsup\mu_n(F)\le\mu(F)\) for closed \(F\).

(b) If \(A\) is Borel and \(\mu(\partial A)=0\), then \(\mu_n(A)\to\mu(A)\), and the restrictions \(\mu_n|_A\) converge weakly to \(\mu|_A\).

(c) If \(\pi:K\to K'\) is a continuous map into a compact metric space, the image measures \(\pi_*\mu_n\) converge weakly to \(\pi_*\mu\).

*Proof.* (a) Take \(f=1\). For open \(U\) and closed \(F=K\setminus U\), the continuous functions \(f_m=\min(1,m\,d(\cdot,F))\) increase to the indicator of \(U\); so \(\liminf_n\mu_n(U)\) is at least \(\lim_n\int f_m\,d\mu_n=\int f_m\,d\mu\) for every \(m\), and the right side tends to \(\mu(U)\). The closed case follows by complements and the convergence of total masses.

(b) The interior \(A^\circ\) and closure \(\bar A\) satisfy \(\mu(A^\circ)=\mu(\bar A)=\mu(A)\), and (a) squeezes \(\mu_n(A)\) between \(\mu_n(A^\circ)\) and \(\mu_n(\bar A)\). For a continuous \(f\ge0\) and \(t\ge0\), the boundary of \(A\cap\{f>t\}\) lies in \(\partial A\cup\{f=t\}\), which is \(\mu\)-null for all but countably many \(t\); so \(\mu_n(A\cap\{f>t\})\to\mu(A\cap\{f>t\})\) for almost every \(t\), and \(\int_Af\,d\mu_n=\int_0^{\max f}\mu_n(A\cap\{f>t\})\,dt\) converges by dominated convergence. Signed \(f\) is a difference of two nonnegative ones.

(c) \(\int f\,d\pi_*\mu_n=\int f\circ\pi\,d\mu_n\), and \(f\circ\pi\) is continuous. \(\square\)

## 3. Compactness

**Lemma 3.1.** For a compact metric space \(K\), the space \(C(K)\) of continuous functions with the supremum norm has a countable dense subset.

*Proof.* For \(m\ge1\) choose a finite set \(x_1,\dots,x_r\) such that every point is within \(1/m\) of one of them, put \(\psi_i(x)=\max(0,2/m-d(x,x_i))\) and \(\Psi=\sum_i\psi_i\ge1/m\). For \(f\in C(K)\) with modulus of continuity \(\omega\), and rational numbers \(q_i\) with \(|q_i-f(x_i)|\le1/m\),
\[
\Bigl|f(x)-\sum_iq_i\,\frac{\psi_i(x)}{\Psi(x)}\Bigr|\le\omega(2/m)+\frac1m ,
\]
because only the \(x_i\) with \(d(x,x_i)<2/m\) contribute and the weights \(\psi_i/\Psi\) add up to one. The functions \(\sum_iq_i\psi_i/\Psi\), over all \(m\) and rational \(q_i\), form a countable dense set. \(\square\)

**Theorem 3.2** (compactness). Let \(K\) be a compact metric space. Every sequence of measures \(\mu_n\) on \(K\) with \(\sup_n\mu_n(K)<\infty\) has a weakly convergent subsequence. For countably many such sequences, one subsequence of indices can be chosen along which all of them converge.

*Proof.* Let \(f_1,f_2,\dots\) be dense in \(C(K)\) (Lemma 3.1). The numbers \(\int f_j\,d\mu_n\) are bounded by \(\|f_j\|\sup_n\mu_n(K)\), so a diagonal subsequence makes all of them converge. For any \(f\in C(K)\) and \(\epsilon>0\), some \(f_j\) has \(\|f-f_j\|<\epsilon\), so \(\int f\,d\mu_n\) is a Cauchy sequence; let \(\Lambda(f)\) be its limit. Then \(\Lambda\) is a positive linear functional on \(C(K)=C_c(K)\), and the Riesz representation theorem [Haar measure on locally compact groups](course:AN-01/prerequisites/riesz/positive-riesz) (Theorem 2.2) gives a measure \(\mu\) with \(\int f\,d\mu=\Lambda(f)\); it is finite, with \(\mu(K)=\Lambda(1)\). For countably many sequences, apply the diagonal argument to all the countably many sequences of numbers \(\int f_j\,d\mu^{(i)}_n\) at once. \(\square\)

## 4. Hausdorff limits

For nonempty closed subsets \(A,B\) of a compact metric space \(K\) put
\[
\begin{aligned}
d_H(A,B)=\max\Bigl({}&\sup_{a\in A}d(a,B),\\
&\sup_{b\in B}d(b,A)\Bigr).
\end{aligned}
\]
This is a metric on the nonempty closed subsets of \(K\), the *Hausdorff distance*.

**Theorem 4.1** (Blaschke selection). Every sequence of nonempty closed subsets of \(K\) has a subsequence that converges in Hausdorff distance to a nonempty closed set.

*Proof.* *A Cauchy subsequence.* For \(m\ge1\) fix a finite \(1/m\)-net \(F_m\) of \(K\), and for a closed set \(A\) let \(T_m(A)=\{x\in F_m:d(x,A)\le1/m\}\). Every point of \(A\) is within \(1/m\) of a point of \(F_m\), which then lies in \(T_m(A)\); and every point of \(T_m(A)\) is within \(1/m\) of \(A\). So \(d_H(A,T_m(A))\le1/m\). There are finitely many possible sets \(T_m(A)\); a diagonal subsequence \((A_n)\) has \(T_m(A_n)\) constant for \(n\ge n_m\), for every \(m\). Then \(d_H(A_n,A_{n'})\le2/m\) for \(n,n'\ge n_m\).

*The limit.* Passing to a further subsequence, \(d_H(A_n,A_{n+1})<2^{-n}\) for all \(n\ge1\). Call a sequence \((x_m)_{m\ge1}\) *admissible* if \(x_m\in A_m\) and \(d(x_m,x_{m+1})<2^{-m}\) for all \(m\); it is Cauchy and converges in the compact space \(K\), and its limit \(y\) satisfies \(d(x_n,y)<2^{1-n}\). Every \(x\in A_n\) is the \(n\)th term of an admissible sequence: choose \(x_{m+1}\in A_{m+1}\) within \(2^{-m}\) of \(x_m\) for \(m\ge n\), and \(x_{m-1}\in A_{m-1}\) within \(2^{-(m-1)}\) of \(x_m\) for \(m\le n\), both possible since \(d_H(A_m,A_{m+1})<2^{-m}\). Let \(A\) be the closure of the set of limits of admissible sequences; it is nonempty. Each \(x\in A_n\) is within \(2^{1-n}\) of such a limit, and each limit \(y\), with its sequence \((x_m)\), is within \(2^{1-n}\) of \(x_n\in A_n\); passing to the closure, \(d_H(A_n,A)\le2^{1-n}\). \(\square\)

**Lemma 4.2.** Let \(\Gamma_n\to\Gamma\) in Hausdorff distance.

(a) Every point of \(\Gamma\) is the limit of points \(x_n\in\Gamma_n\), and every limit of a subsequence of points \(x_n\in\Gamma_n\) lies in \(\Gamma\).

(b) If a compact set \(L\) is disjoint from \(\Gamma\), then \(L\) is disjoint from \(\Gamma_n\) for all large \(n\).

(c) If measures \(\mu_n\) are concentrated on \(\Gamma_n\), that is \(\mu_n(K\setminus\Gamma_n)=0\), and converge weakly to \(\mu\), then \(\mu(K\setminus\Gamma)=0\).

*Proof.* (a) For \(y\in\Gamma\) choose \(x_n\in\Gamma_n\) nearest to \(y\); \(d(x_n,y)\le d_H(\Gamma_n,\Gamma)\). If \(x_n\in\Gamma_n\) and \(x_{n_i}\to x\), then \(d(x,\Gamma)\le d(x,x_{n_i})+d_H(\Gamma_{n_i},\Gamma)\to0\), and \(\Gamma\) is closed. (b) \(L\) has positive distance \(\rho\) from \(\Gamma\), and \(\Gamma_n\) lies in the open \(\rho\)-neighbourhood of \(\Gamma\) once \(d_H(\Gamma_n,\Gamma)<\rho\). (c) The set \(K\setminus\Gamma\) is the union of the compact sets \(L_m=\{x:d(x,\Gamma)\ge1/m\}\). By (b) and Lemma 2.1(a), applied to the open set \(\{d(\cdot,\Gamma)>1/(2m)\}\supseteq L_m\), which misses \(\Gamma_n\) for large \(n\), its \(\mu\)-measure is at most \(\liminf\mu_n=0\). \(\square\)

## 5. Conditional measures

**Proposition 5.1** (conditional measures). Let \(Z\) be a compact metric space, \(\nu\) a finite measure on \(Z\times[0,1]\), and \(\lambda=\pi_*\nu\) its image on \(Z\) under \(\pi(z,t)=z\). There are probability measures \(h_z\) on \([0,1]\), \(z\in Z\), such that for every Borel \(J\subseteq[0,1]\) the function \(z\mapsto h_z(J)\) is Borel and
\[
\nu(F\times J)=\int_Fh_z(J)\,d\lambda(z)
\]
for every Borel \(F\subseteq Z\).

*Proof.* *Distribution functions at dyadic points.* Let \(D\) be the set of dyadic rationals in \([0,1]\). For \(t\in D\), the measure \(F\mapsto\nu(F\times[0,t])\) is at most \(\lambda\), so by the Radon–Nikodym theorem [Fremlin, 232E] it has a Borel density \(G_t\) with respect to \(\lambda\), and one may take \(0\le G_t\le1\) and \(G_1=1\). For \(t<t'\) in \(D\), \(\int_F(G_{t'}-G_t)\,d\lambda=\nu(F\times(t,t'])\ge0\) for all \(F\), so \(G_t\le G_{t'}\) \(\lambda\)-almost everywhere. For \(t\in D\), \(t<1\), and \(t_m\in D\) decreasing to \(t\), the functions \(G_{t_m}\) decrease almost everywhere to a limit \(G'\ge G_t\) with \(\int_FG'\,d\lambda\) equal to \(\lim\nu(F\times[0,t_m])=\nu(F\times[0,t])\), by monotone convergence; so \(G'=G_t\) almost everywhere. These are countably many conditions, so outside a Borel \(\lambda\)-null set \(N_0\) the function \(t\mapsto G_t(z)\) on \(D\) is nondecreasing, takes the value \(1\) at \(t=1\), and satisfies \(G_t(z)=\lim G_{t_m}(z)\) along every dyadic sequence \(t_m\downarrow t\).

*The measures.* For \(z\notin N_0\) and \(x\in[0,1)\) let \(\Phi_z(x)=\inf\{G_t(z):t\in D,\,t>x\}\), and \(\Phi_z(1)=1\). This function is nondecreasing, right-continuous, and equal to \(G_t(z)\) at dyadic \(t\). For a continuous \(f\) on \([0,1]\) the sums
\[
\begin{aligned}
\Lambda_z^{(m)}(f)={}&f(0)\Phi_z(0)\\
&+\sum_{i=1}^{2^m}f(i2^{-m})\bigl(\Phi_z(i2^{-m})\\
&\qquad-\Phi_z((i-1)2^{-m})\bigr)
\end{aligned}
\]
form a Cauchy sequence, by uniform continuity of \(f\) and \(\Phi_z(1)=1\); their limit \(\Lambda_z(f)\) is a positive linear functional with \(\Lambda_z(1)=1\). By the Riesz representation theorem there is a probability measure \(h_z\) with \(\int f\,dh_z=\Lambda_z(f)\). For dyadic \(t<1\), take continuous \(f_j\) equal to \(1\) on \([0,t]\), \(0\) on \([t+2^{-j},1]\), and affine in between: then \(\Lambda_z(f_j)\) lies between \(\Phi_z(t)\) and \(\Phi_z(t+2^{-j})\), and letting \(j\to\infty\) gives \(h_z([0,t])=\Phi_z(t)=G_t(z)\) by right-continuity. For \(z\in N_0\) let \(h_z\) be the unit mass at \(0\).

*All Borel sets.* Let \(\mathcal J\) be the family of Borel \(J\subseteq[0,1]\) for which \(z\mapsto h_z(J)\) is Borel and the displayed formula holds for every Borel \(F\). It contains \([0,1]\), since \(\nu(F\times[0,1])=\lambda(F)\), and the intervals \([0,t]\), \(t\in D\), since \(h_z([0,t])=G_t(z)\) off the null set \(N_0\). It is closed under differences \(J'\setminus J\) with \(J\subseteq J'\), and under increasing countable unions by monotone convergence; so it is a Dynkin class. The intervals \([0,t]\), \(t\in D\), are closed under intersection and generate the Borel \(\sigma\)-algebra of \([0,1]\). By the monotone class theorem [Fremlin, 136B], \(\mathcal J\) contains all Borel sets. \(\square\)

The measure \(h_z\) is the *conditional distribution of the second coordinate given the first*. Two families with the property agree for \(\lambda\)-almost every \(z\) on every dyadic interval, hence as measures; this uniqueness is not used.

## 6. Exercises

**6.1** (easy). Show that the unit masses \(\delta_{1/n}\) on \([0,1]\) converge weakly to \(\delta_0\), and that \(\delta_{1/n}((0,1])=1\) does not converge to \(\delta_0((0,1])\). Which part of Lemma 2.1 explains this?

**6.2** (easy). Show that the sets \(\{0,1/n,2/n,\dots,1\}\) converge in Hausdorff distance to \([0,1]\), and that the measures \(\frac1{n+1}\sum_{i=0}^n\delta_{i/n}\) converge weakly to Lebesgue measure on \([0,1]\).

**6.3** (medium). In Proposition 5.1 let \(\nu\) be the image of Lebesgue measure on \([0,1]\) under \(t\mapsto(t,t)\), with \(Z=[0,1]\). Find \(h_z\).

## 7. Solutions

**6.1.** For continuous \(f\), \(f(1/n)\to f(0)\). The set \((0,1]\) has boundary \(\{0\}\), which carries the full mass of \(\delta_0\), so Lemma 2.1(b) does not apply; (a) gives only \(\liminf\delta_{1/n}((0,1])\ge\delta_0((0,1])=0\).

**6.2.** Every point of \([0,1]\) is within \(1/(2n)\) of the finite set, which lies in \([0,1]\). For continuous \(f\), \(\frac1{n+1}\sum f(i/n)\) is a Riemann sum up to a term \(O(\|f\|/n)\), and converges to \(\int_0^1f\).

**6.3.** \(\lambda\) is Lebesgue measure on \(Z=[0,1]\), and \(\nu(F\times J)=|F\cap J|=\int_F\mathbf1_J(z)\,dz\). So \(h_z=\delta_z\) for almost every \(z\): the second coordinate is determined by the first.

## References

- [Fremlin] D. H. Fremlin, *Measure Theory*, Volumes 1 and 2, 136B (monotone class theorem), 232E (Radon–Nikodym theorem), 232I (Lebesgue decomposition); the text of the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10). https://www1.essex.ac.uk/maths/people/fremlin/mt.htm
- [OpenAI-HL] OpenAI, *A power saving for planar halving lines*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/A-power-saving-for-planar-halving-lines-September-25-2026
