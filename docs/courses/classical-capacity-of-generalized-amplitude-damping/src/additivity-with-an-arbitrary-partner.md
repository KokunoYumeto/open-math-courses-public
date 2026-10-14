# Additivity with an arbitrary partner

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The one-use estimate of the previous lesson, Lemma 2.1 of [Output entropy of damping blocks](output-entropy-of-damping-blocks.md), holds next to an arbitrary finite-dimensional channel \(\mathcal N\). This lesson uses it to prove that the generalized amplitude-damping channel \(\mathcal A=\mathcal A_{\gamma,\nu}\) is additive with every such partner, for the Holevo information (Theorem 1.1), for the minimum output entropy (Theorem 2.1), and for the regularized Holevo information, hence, under the coding theorem, for the classical capacity (Theorem 3.1). The partner is arbitrary: its own Holevo information need not be additive. The last section computes special cases: ordinary amplitude damping, the symmetry \(\nu\leftrightarrow1-\nu\), the unital channel \(\nu=\frac12\), and the endpoints.

- Holevo information (Theorem 1.1).
- Minimum output entropy (Theorem 2.1).
- Regularized Holevo information and capacity (Theorem 3.1).
- Special cases (Section 4).

The lesson follows [OpenAI-GAD, Sections 6 and 7]. Notation is that of [Quantum channels and Holevo information](quantum-channels-and-holevo-information.md): Holevo quantities \(\chi_{\mathcal N}\{q_a,\rho_a\}\) in nats, Holevo information \(\chi\) in bits, \(S_{\min}\) in nats, \(t(p)=(1-\gamma)p+\gamma\nu\), \(e(p)=g(v(p))\) and \(f(p)=h(t(p))-e(p)\). Throughout, \(\mathcal N\colon\mathcal B(\mathcal H_{\mathrm{in}})\to\mathcal B(\mathcal H_{\mathrm{out}})\) is a channel between nonzero finite-dimensional spaces.

## 1. Holevo information

**Theorem 1.1** ([OpenAI-GAD, Corollary 1.2]). \(\chi(\mathcal A\otimes\mathcal N)=\chi(\mathcal A)+\chi(\mathcal N)\).

*Proof.* The inequality \(\ge\) is Lemma 3.1(4) of the first lesson. For \(\le\), by Lemma 3.1(1) there it suffices to bound the Holevo quantity of an ensemble \(\{q_a,\psi_a\psi_a^*\}\) of pure states on \(\mathbb C^2\otimes\mathcal H_{\mathrm{in}}\); the vectors \(\psi_a\) may be entangled between the two factors. Decompose each of them as in Lemma 2.1 of the previous lesson,
\[
\begin{aligned}
\psi_a&=\sqrt{1-p_a}\,|0\rangle\otimes\psi_{a,0}\\
&\quad+\sqrt{p_a}\,|1\rangle\otimes\psi_{a,1},
\end{aligned}
\]
and put, for \(i\in\{0,1\}\),
\[
\begin{gathered}
\bar p=\sum_aq_ap_a,\\
w_{a,0}=q_a(1-p_a),\quad w_{a,1}=q_ap_a,\\
\tau_{a,i}=\mathcal N(\psi_{a,i}\psi_{a,i}^*).
\end{gathered}
\]
The weights \(w_{a,i}\) are nonnegative with sum \(1\).

*The branch ensemble.* Let \(\bar\rho=\sum_aq_a\psi_a\psi_a^*\) and let \(\bar\rho_2\) be its marginal on \(\mathcal H_{\mathrm{in}}\). The cross terms vanish under the partial trace over the qubit, because \(\langle1|0\rangle=0\), whatever the overlaps of the branch vectors; so
\[
\bar\rho_2=\sum_{a,i}w_{a,i}\,\psi_{a,i}\psi_{a,i}^* ,
\]
and, by Lemma 1.3 of the first lesson, since \(\mathcal A\) preserves traces,
\[
\begin{aligned}
\bar\tau:=\sum_{a,i}w_{a,i}\tau_{a,i}&=\mathcal N(\bar\rho_2)\\
&=\operatorname{Tr}_1\bigl((\mathcal A\otimes\mathcal N)(\bar\rho)\bigr).
\end{aligned}
\]
So the branch ensemble \(\{w_{a,i},\psi_{a,i}\psi_{a,i}^*\}\) for \(\mathcal N\) has as mean output exactly the second marginal of the mean output of the given ensemble.

*Upper bound for the mean output.* Let \(\sigma_a=(\mathcal A\otimes\mathcal N)(\psi_a\psi_a^*)\) and \(\bar\sigma=\sum_aq_a\sigma_a\). Since \(\mathcal N\) preserves traces, the first marginal of \(\bar\sigma\) is \(\mathcal A\) applied to the first marginal of \(\bar\rho\), whose excited population is \(\bar p\); so the first marginal of \(\bar\sigma\) has the excited population \(t(\bar p)\). Corollary 2.2 of the first lesson, with the standard basis of the qubit and an eigenbasis of \(\bar\tau\), gives
\[
S(\bar\sigma)\le h\bigl(t(\bar p)\bigr)+S(\bar\tau).
\]

*Lower bound for the outputs.* Lemma 2.1 of the previous lesson and the convexity of \(e\) (Lemma 1.1 there) give
\[
\begin{aligned}
&\sum_aq_aS(\sigma_a)\\
&\quad\ge\sum_aq_ae(p_a)+\sum_{a,i}w_{a,i}S(\tau_{a,i})\\
&\quad\ge e(\bar p)+\sum_{a,i}w_{a,i}S(\tau_{a,i}).
\end{aligned}
\]

*Conclusion.* Subtracting,
\[
\begin{aligned}
&\chi_{\mathcal A\otimes\mathcal N}\{q_a,\psi_a\psi_a^*\}\\
&\quad\le f(\bar p)\\
&\qquad+\chi_{\mathcal N}\{w_{a,i},\psi_{a,i}\psi_{a,i}^*\}\\
&\quad\le(\ln2)\bigl(\chi(\mathcal A)+\chi(\mathcal N)\bigr),
\end{aligned}
\]
by Theorem 4.1 of the previous lesson for the first term and the definition of \(\chi(\mathcal N)\) for the second. Taking the supremum over ensembles proves \(\le\). \(\blacksquare\)

## 2. Minimum output entropy

**Theorem 2.1** ([OpenAI-GAD, Corollary 1.2]). \(S_{\min}(\mathcal A)=g\bigl(\gamma\nu(1-\nu)\bigr)\), and
\[
S_{\min}(\mathcal A\otimes\mathcal N)=S_{\min}(\mathcal A)+S_{\min}(\mathcal N).
\]

*Proof.* By Lemma 3.1(2) of the first lesson, a pure input attains \(S_{\min}(\mathcal A)\), so \(S_{\min}(\mathcal A)=\min_pe(p)\) by Lemma 5.2 there. Since \(v(p)=\gamma\nu(1-\nu)+\gamma(1-\gamma)(p-\nu)^2\) is smallest at \(p=\nu\) and \(g\) is nondecreasing, \(\min_pe(p)=g(\gamma\nu(1-\nu))\), attained by every pure state with population \(\nu\), also at the endpoints of the parameters.

For the product, \(\le\) is Lemma 3.1(4) of the first lesson. For \(\ge\), a pure input attains \(S_{\min}(\mathcal A\otimes\mathcal N)\), and for a pure input \(\psi\) Lemma 2.1 of the previous lesson, with \(S(\mathcal N(\psi_i\psi_i^*))\ge S_{\min}(\mathcal N)\) for both branches, gives
\[
\begin{aligned}
&S\bigl((\mathcal A\otimes\mathcal N)(\psi\psi^*)\bigr)\\
&\quad\ge e(p)+S_{\min}(\mathcal N)\\
&\quad\ge S_{\min}(\mathcal A)+S_{\min}(\mathcal N).
\end{aligned}
\]
\(\blacksquare\)

## 3. Regularized Holevo information and capacity

**Theorem 3.1** ([OpenAI-GAD, Corollary 1.2]). For every \(n\ge1\),
\[
\chi\bigl((\mathcal A\otimes\mathcal N)^{\otimes n}\bigr)=n\chi(\mathcal A)+\chi(\mathcal N^{\otimes n}),
\]
hence
\[
\begin{aligned}
&\sup_n\frac1n\chi\bigl((\mathcal A\otimes\mathcal N)^{\otimes n}\bigr)\\
&\qquad=\chi(\mathcal A)+\sup_n\frac1n\chi(\mathcal N^{\otimes n}).
\end{aligned}
\]
Under Hypothesis (CT) of the first lesson, \(C(\mathcal A\otimes\mathcal N)=C(\mathcal A)+C(\mathcal N)\).

*Proof.* Reordering the tensor factors of the inputs and of the outputs identifies \((\mathcal A\otimes\mathcal N)^{\otimes n}\) with \(X\mapsto U\bigl(\mathcal A^{\otimes n}\otimes\mathcal N^{\otimes n}\bigr)(VXV^*)U^*\) for permutation unitaries \(U\) and \(V\), and such unitaries do not change the Holevo information (Lemma 3.1(3) of the first lesson). Apply Theorem 1.1 to \(\mathcal A\) and the partner \(\mathcal A^{\otimes(n-1)}\otimes\mathcal N^{\otimes n}\), which is again a channel between nonzero finite-dimensional spaces, then to \(\mathcal A\) and \(\mathcal A^{\otimes(n-2)}\otimes\mathcal N^{\otimes n}\), and so on:
\[
\chi\bigl(\mathcal A^{\otimes n}\otimes\mathcal N^{\otimes n}\bigr)=n\chi(\mathcal A)+\chi(\mathcal N^{\otimes n}).
\]
Dividing by \(n\) and taking suprema gives the second formula. Under (CT), its left side is \(C(\mathcal A\otimes\mathcal N)\) and its right side is \(\chi(\mathcal A)+C(\mathcal N)\), and \(\chi(\mathcal A)=C(\mathcal A)\) by Corollary 4.2 of the previous lesson. \(\blacksquare\)

No restriction was placed on entanglement among the inputs of the copies of \(\mathcal N\): the regularization of the partner remains, and only the damping channel is peeled off.

## 4. Special cases

**Corollary 4.1** (ordinary amplitude damping; [OpenAI-GAD, Corollary 7.1]). For \(\gamma\in[0,1]\), let \(\mathcal A_\gamma\) have the Kraus operators \(K_0=\operatorname{diag}(1,\sqrt{1-\gamma})\) and \(K_1=\sqrt\gamma\,|0\rangle\langle1|\). For every \(n\ge1\),
\[
\begin{aligned}
\chi(\mathcal A_\gamma^{\otimes n})&=n\chi(\mathcal A_\gamma)\\
&=\frac n{\ln2}\max_{0\le p\le1}f_0(p),\\
f_0(p)&=h\bigl((1-\gamma)p\bigr)\\
&\quad-g\bigl(\gamma(1-\gamma)p^2\bigr),
\end{aligned}
\]
and under (CT) the capacity of \(\mathcal A_\gamma\) is \(\chi(\mathcal A_\gamma)\).

*Proof.* The channel with these Kraus operators maps \(\bigl(\begin{smallmatrix}1-q&z\\\bar z&q\end{smallmatrix}\bigr)\) to \(\bigl(\begin{smallmatrix}1-(1-\gamma)q&\sqrt{1-\gamma}z\\\sqrt{1-\gamma}\bar z&(1-\gamma)q\end{smallmatrix}\bigr)\), which is \(\mathcal A_{\gamma,0}\); and \(v_{\gamma,0}(p)=\gamma(1-\gamma)p^2\). Theorem 4.1 and Corollary 4.2 of the previous lesson apply. \(\blacksquare\)

This one-use maximum, with the ensemble of two states of opposite phases, agrees with Giovannetti and Fazio [GF, Section III A], whose transmissivity is \(1-\gamma\).

**Lemma 4.2** (the symmetry \(\nu\leftrightarrow1-\nu\)). Let \(\mathsf X=|0\rangle\langle1|+|1\rangle\langle0|\). Then
\[
\mathcal A_{\gamma,1-\nu}(\rho)=\mathsf X\,\mathcal A_{\gamma,\nu}(\mathsf X\rho\mathsf X)\,\mathsf X ,
\]
so \(\mathcal A_{\gamma,1-\nu}\) and \(\mathcal A_{\gamma,\nu}\) have the same Holevo information, minimum output entropy and capacity.

*Proof.* Conjugation by \(\mathsf X\) exchanges the populations and conjugates the coherence. For \(\rho\) with population \(q\) and coherence \(z\), \(\mathsf X\rho\mathsf X\) has population \(1-q\) and coherence \(\bar z\); \(\mathcal A_{\gamma,\nu}\) maps it to population \((1-\gamma)(1-q)+\gamma\nu\) and coherence \(k\bar z\); conjugating back gives population \(1-(1-\gamma)(1-q)-\gamma\nu\), that is \((1-\gamma)q+\gamma(1-\nu)\), and coherence \(kz\), which is \(\mathcal A_{\gamma,1-\nu}(\rho)\). Unitary conjugations change neither the Holevo information nor the minimum output entropy (Lemma 3.1(3) of the first lesson). Conjugating the states and the measurement operators of a code by \(\mathsf X^{\otimes n}\) turns every code for one channel into a code for the other with the same error probabilities, so the capacities agree as well. \(\blacksquare\)

In particular \(\nu=1\) has the capacity of ordinary amplitude damping, with the population \(p\) replaced by \(1-p\).

**Corollary 4.3** (the unital channel; [OpenAI-GAD, Corollary 7.2]). For every \(\gamma\in[0,1]\),
\[
\begin{aligned}
\chi(\mathcal A_{\gamma,1/2})&=1-\frac{g(\gamma/4)}{\ln2}\\
&=1-\frac1{\ln2}h\Bigl(\frac{1+\sqrt{1-\gamma}}2\Bigr),
\end{aligned}
\]
the states \((|0\rangle\pm|1\rangle)/\sqrt2\) with probabilities \(\frac12\) attain it, and their tensor products attain \(\chi(\mathcal A_{\gamma,1/2}^{\otimes n})\) for every \(n\). Under (CT) this is the capacity.

*Proof.* For \(\nu=\frac12\),
\[
\begin{aligned}
f(p)&=h\Bigl((1-\gamma)p+\frac\gamma2\Bigr)\\
&\quad-g\Bigl(\frac\gamma4+\gamma(1-\gamma)\bigl(p-\tfrac12\bigr)^2\Bigr).
\end{aligned}
\]
The first term is concave in \(p\), as \(h\) composed with an affine function, and the second is the negative of the convex function \(e\) of Lemma 1.1 of the previous lesson; so \(f\) is concave. Moreover \(f(1-p)=f(p)\), because \((1-\gamma)(1-p)+\frac\gamma2\) equals \(1-\bigl((1-\gamma)p+\frac\gamma2\bigr)\) and \(h(1-s)=h(s)\). Hence \(f(\frac12)\ge\frac12\bigl(f(p)+f(1-p)\bigr)=f(p)\) for all \(p\), and the maximum is \(f(\frac12)=\ln2-g(\gamma/4)\). Finally \(g(\gamma/4)=h\bigl((1+\sqrt{1-\gamma})/2\bigr)\) by the definition of \(g\). Theorem 4.1 of the previous lesson gives the rest. \(\blacksquare\)

*The endpoints.* For \(\gamma=0\) the channel is the identity, \(v\equiv0\), and \(\chi=1\) bit per use. For \(\gamma=1\) it replaces every input by \(\operatorname{diag}(1-\nu,\nu)\), so \(\chi=0\); in the formula, both terms of \(f\) equal \(h(\nu)\), because \(g(\nu(1-\nu))=h(\nu)\). These cases include the four corners of the parameter square.

## 5. Exercises

**5.1.** Let \(\mathcal N\) be the identity channel of \(\mathbb C^m\). Show directly that \(\chi(\mathcal A\otimes\mathcal N)=\chi(\mathcal A)+\log_2m\).

**5.2.** Show that Theorem 2.1 implies that \(S_{\min}\bigl(\mathcal A_{\gamma_1,\nu_1}\otimes\dots\otimes\mathcal A_{\gamma_n,\nu_n}\bigr)\) equals \(\sum_jg\bigl(\gamma_j\nu_j(1-\nu_j)\bigr)\).

**5.3.** Show that \(\chi(\mathcal A_{\gamma_1,\nu_1}\otimes\dots\otimes\mathcal A_{\gamma_n,\nu_n})\) equals \(\sum_j\chi(\mathcal A_{\gamma_j,\nu_j})\), for damping channels with different parameters.

**5.4.** For \(\gamma\in(0,1)\) and \(\nu\in(0,1)\), show that the maximizer of \(f\) lies strictly between \(0\) and \(1\).

**5.5.** Show that the function \(\gamma\mapsto\chi(\mathcal A_{\gamma,1/2})\) decreases from \(1\) to \(0\) on \([0,1]\).

## 6. Solutions

**5.1.** For the identity channel of \(\mathbb C^m\), every Holevo quantity is at most the entropy of the mean output, hence at most \(\ln m\), and an orthonormal basis with uniform probabilities attains \(\ln m\); so \(\chi(\mathcal N)=\log_2m\). Theorem 1.1 applies.

**5.2.** Induction on \(n\), with the partner \(\mathcal A_{\gamma_2,\nu_2}\otimes\dots\otimes\mathcal A_{\gamma_n,\nu_n}\) and Theorem 2.1 for the first factor, whose minimum output entropy is \(g(\gamma_1\nu_1(1-\nu_1))\).

**5.3.** Induction on \(n\) with Theorem 1.1, the partner being the product of the remaining channels.

**5.4.** By Exercise 5.2 of the previous lesson, \(f(0)=f(1)=0\) and \(f(p)>0\) for \(0<p<1\) when \(\gamma<1\); so no maximizer lies at an endpoint.

**5.5.** By Corollary 4.3 the value is \(1-h\bigl((1+\sqrt{1-\gamma})/2\bigr)/\ln2\). As \(\gamma\) increases from \(0\) to \(1\), \((1+\sqrt{1-\gamma})/2\) decreases from \(1\) to \(\frac12\), where \(h\) increases from \(0\) to \(\ln2\); so the value decreases from \(1\) to \(0\).

## References

- [OpenAI-GAD] OpenAI, *Classical capacity and entropy inequalities for generalized amplitude damping*, OpenAI Math Release preprint, 24 September 2026, Sections 6 and 7. https://github.com/openai/math/tree/main/preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026
- [GF] V. Giovannetti and R. Fazio, *Information-capacity description of spin-chain correlations*, Physical Review A 71 (2005); preprint arXiv:quant-ph/0405110. https://arxiv.org/abs/quant-ph/0405110
