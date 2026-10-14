# Output entropy of damping blocks

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A pure input of one qubit with excited population \(p\) leaves the generalized amplitude-damping channel \(\mathcal A=\mathcal A_{\gamma,\nu}\) with entropy \(e(p)=g(v(p))\) ([Quantum channels and Holevo information](quantum-channels-and-holevo-information.md), Lemma 5.2). This lesson proves that the same bound holds site by site for every input of \(n\) qubits, however entangled:
\[
S\bigl(\mathcal A^{\otimes n}(\rho)\bigr)\ge\sum_{j=1}^ne(p_j),
\]
where \(p_j\) is the excited population of the input at site \(j\) (Proposition 3.1 and Corollary 3.2). Together with an upper bound for the entropy of a mean output, this proves that the Holevo information of \(n\) uses is \(n\) times that of one use (Theorem 4.1).

- Convexity of \(e\) (Lemma 1.1).
- One damping use next to an arbitrary channel (Lemma 2.1).
- Many uses, pure and mixed inputs (Proposition 3.1, Corollary 3.2).
- The Holevo information of \(n\) uses (Theorem 4.1) and the capacity (Corollary 4.2).

The lesson follows [OpenAI-GAD, Sections 4 and 5]. It uses the thermal block inequality of [Block entropy inequalities](block-entropy-inequalities.md) (Theorem 2.1 there), the convexity of \(s\mapsto g(s^2)\) from [Entropy differences and log-determinants](entropy-differences-and-log-determinants.md) (Lemma 5.2 there), and the framework of the first lesson.

Throughout, \(\gamma,\nu\in[0,1]\) are fixed, \(\mathcal A=\mathcal A_{\gamma,\nu}\), and \(k,a,b,c,d\) are as in Section 5 of the first lesson: \(a+c=b+d=1\) and \(ad-bc=k^2\). A lower bound for the entropy of each output is needed, and it must depend on the input populations: the entropy of a mean output is controlled by the mean populations (Section 4), and a bound for the minimum output entropy alone would lose this information.

## 1. Convexity of the one-qubit output entropy

**Lemma 1.1** ([OpenAI-GAD, Lemma 4.1]). The function
\[
e(p)=g\bigl(\gamma\nu(1-\nu)+\gamma(1-\gamma)(p-\nu)^2\bigr)
\]
is convex on \([0,1]\).

*Proof.* By the completed square of Lemma 5.2 of the first lesson,
\[
\sqrt{v(p)}=\left\|\begin{pmatrix}\sqrt{\gamma\nu(1-\nu)}\\\sqrt{\gamma(1-\gamma)}\,(p-\nu)\end{pmatrix}\right\|,
\]
the Euclidean norm of a vector that depends affinely on \(p\). So \(p\mapsto\sqrt{v(p)}\) is convex, also when a coefficient vanishes. Its values lie in \([0,\frac12]\), where \(s\mapsto g(s^2)\) is nondecreasing and convex (Lemma 5.2 of the second lesson). A nondecreasing convex function of a convex function is convex: for \(0\le\theta\le1\),
\[
\begin{aligned}
&g\bigl(v(\theta p+(1-\theta)p')\bigr)\\
&\quad\le g\Bigl(\bigl(\theta\sqrt{v(p)}+(1-\theta)\sqrt{v(p')}\bigr)^2\Bigr)\\
&\quad\le\theta e(p)+(1-\theta)e(p'),
\end{aligned}
\]
by convexity of \(\sqrt v\) and monotonicity, then convexity of \(s\mapsto g(s^2)\). \(\blacksquare\)

## 2. One damping use next to an arbitrary channel

**Lemma 2.1** ([OpenAI-GAD, Lemma 4.2]). Let \(\mathcal N\colon\mathcal B(\mathcal H_{\mathrm{in}})\to\mathcal B(\mathcal H_{\mathrm{out}})\) be a channel between nonzero finite-dimensional spaces. For a unit vector \(\psi\in\mathbb C^2\otimes\mathcal H_{\mathrm{in}}\), write
\[
\psi=\sqrt{1-p}\,|0\rangle\otimes\psi_0+\sqrt p\,|1\rangle\otimes\psi_1,
\]
with \(0\le p\le1\) and unit vectors \(\psi_0,\psi_1\); a branch of weight zero may be chosen arbitrarily. Then
\[
\begin{aligned}
&S\bigl((\mathcal A\otimes\mathcal N)(\psi\psi^*)\bigr)\\
&\quad\ge e(p)+(1-p)\,S\bigl(\mathcal N(\psi_0\psi_0^*)\bigr)\\
&\qquad+p\,S\bigl(\mathcal N(\psi_1\psi_1^*)\bigr).
\end{aligned}
\]

The branch vectors need not be orthogonal, and each may be entangled across the factors of \(\mathcal H_{\mathrm{in}}\) when \(\mathcal N\) is itself a tensor product.

*Proof.* Choose a Kraus representation \(\mathcal N(P)=\sum_{\ell=1}^rV_\ell PV_\ell^*\) with \(\sum_\ell V_\ell^*V_\ell=I\) (Theorem 1.2 of the first lesson). Let \(X\) and \(Y\) be the matrices of size \(\dim\mathcal H_{\mathrm{out}}\times r\) whose \(\ell\)-th columns are \(V_\ell\psi_0\) and \(V_\ell\psi_1\). The common column index gives
\[
\begin{gathered}
XX^*=\mathcal N(\psi_0\psi_0^*),\\
YY^*=\mathcal N(\psi_1\psi_1^*),\\
XY^*=\mathcal N(\psi_0\psi_1^*),\\
\operatorname{Tr}XX^*=\operatorname{Tr}YY^*=1 .
\end{gathered}
\]
No relation between \(\dim\mathcal H_{\mathrm{out}}\), \(r\) and \(\dim\mathcal H_{\mathrm{in}}\) is needed.

Put \(x=1-p\) and \(y=p\). Then \(\psi\psi^*=\sum_{i,j\in\{0,1\}}\sqrt{x_ix_j}\,|i\rangle\langle j|\otimes\psi_i\psi_j^*\) with \(x_0=x\), \(x_1=y\). The channel \(\mathcal A\) maps \(|0\rangle\langle0|\mapsto\operatorname{diag}(a,c)\), \(|1\rangle\langle1|\mapsto\operatorname{diag}(b,d)\), \(|0\rangle\langle1|\mapsto k|0\rangle\langle1|\) and \(|1\rangle\langle0|\mapsto k|1\rangle\langle0|\). In block form with respect to the first factor, \((\mathcal A\otimes\mathcal N)(\psi\psi^*)\) has the diagonal blocks \(axXX^*+byYY^*\) and \(cxXX^*+dyYY^*\) and the off-diagonal blocks \(k\sqrt{xy}\,XY^*\) and \(k\sqrt{xy}\,YX^*\). This is the matrix \(T\) of Theorem 2.1 of the third lesson, with
\[
\begin{gathered}
\alpha=ax,\quad\beta=by,\quad\eta=cx,\\
\delta=dy,\quad K=k\sqrt{xy}.
\end{gathered}
\]
These coefficients are nonnegative with sum \((a+c)x+(b+d)y=1\), and \(\alpha\delta-\beta\eta=(ad-bc)xy=K^2\). Moreover \(\alpha+\eta=x\), \(\beta+\delta=y\), and since \(ax+by=1-t(p)\) and \(cx+dy=t(p)\) are the output populations of Lemma 5.2 of the first lesson,
\[
u=t(p)\bigl(1-t(p)\bigr)-k^2xy=v(p)
\]
by the first form of \(v\) there. Theorem 2.1 of the third lesson gives the claim; it includes \(u=0\), and the terms of a branch of weight zero vanish, so \(p=0\), \(p=1\) and all boundary values of \(\gamma,\nu\) are covered. \(\blacksquare\)

## 3. Many uses

For a state \(\rho\) on \((\mathbb C^2)^{\otimes n}\), the *excited population at site \(j\)* is the probability of the outcome \(1\) at site \(j\) in the standard basis: \(p_j=\langle1|\rho_j|1\rangle\) for the marginal \(\rho_j\) of \(\rho\) on site \(j\).

**Proposition 3.1** ([OpenAI-GAD, Proposition 4.3]). For every \(n\ge1\) and every unit vector \(\psi\in(\mathbb C^2)^{\otimes n}\), with site populations \(p_1,\dots,p_n\),
\[
S\bigl(\mathcal A^{\otimes n}(\psi\psi^*)\bigr)\ge\sum_{j=1}^ne(p_j).
\]

*Proof.* For \(n=1\) this is an equality by Lemma 5.2 of the first lesson. Let \(n\ge2\), assume the claim for \(n-1\), and write
\[
\begin{gathered}
\psi=\sqrt x\,|0\rangle\otimes\psi_0+\sqrt y\,|1\rangle\otimes\psi_1,\\
x=1-p_1,\qquad y=p_1 ,
\end{gathered}
\]
with unit vectors \(\psi_0,\psi_1\) on the remaining \(n-1\) sites; a branch of weight zero is chosen arbitrarily. The branch vectors need not be orthogonal and may be entangled across the remaining sites. Lemma 2.1 with \(\mathcal N=\mathcal A^{\otimes(n-1)}\), and \(\sigma_i=\mathcal A^{\otimes(n-1)}(\psi_i\psi_i^*)\), gives
\[
\begin{aligned}
&S\bigl(\mathcal A^{\otimes n}(\psi\psi^*)\bigr)\\
&\quad\ge e(p_1)+x\,S(\sigma_0)+y\,S(\sigma_1).
\end{aligned}
\]
Let \(p_{j|i}\) be the excited population of site \(j\ge2\) in \(\psi_i\). Tracing out the first site removes the cross terms, because \(\langle1|0\rangle=0\): the marginal of \(\psi\psi^*\) on the remaining sites is \(x\,\psi_0\psi_0^*+y\,\psi_1\psi_1^*\). Hence
\[
p_j=x\,p_{j|0}+y\,p_{j|1}\qquad(j\ge2),
\]
whether or not \(\psi_0\perp\psi_1\). By the induction hypothesis for both branches and the convexity of \(e\) (Lemma 1.1),
\[
\begin{aligned}
&xS(\sigma_0)+yS(\sigma_1)\\
&\quad\ge\sum_{j=2}^n\bigl(x\,e(p_{j|0})+y\,e(p_{j|1})\bigr)\\
&\quad\ge\sum_{j=2}^ne(p_j).
\end{aligned}
\]
Terms of a branch of weight zero have coefficient zero, so \(p_1\in\{0,1\}\) is included. \(\blacksquare\)

**Corollary 3.2** ([OpenAI-GAD, Corollary 4.4]). For every \(n\ge1\) and every state \(\rho\) on \((\mathbb C^2)^{\otimes n}\) with site populations \(p_1,\dots,p_n\),
\[
S\bigl(\mathcal A^{\otimes n}(\rho)\bigr)\ge\sum_{j=1}^ne(p_j).
\]

*Proof.* Write \(\rho=\sum_aq_a\psi_a\psi_a^*\) with unit vectors \(\psi_a\), and let \(p_{a,j}\) be their site populations; then \(p_j=\sum_aq_ap_{a,j}\). Concavity of entropy, Proposition 3.1 and convexity of \(e\) give
\[
\begin{aligned}
&S\bigl(\mathcal A^{\otimes n}(\rho)\bigr)\ge\sum_aq_a\sum_je(p_{a,j})\\
&\quad\ge\sum_je\Bigl(\sum_aq_ap_{a,j}\Bigr)=\sum_je(p_j).
\end{aligned}
\]
\(\blacksquare\)

## 4. The Holevo information of many uses

Recall from the first lesson the function
\[
f(p)=h\bigl(t(p)\bigr)-e(p),
\]
where \(t(p)=(1-\gamma)p+\gamma\nu\) and \(0\le p\le1\).
It is continuous on \([0,1]\) and attains its maximum.

**Theorem 4.1** ([OpenAI-GAD, Theorem 1.1]; Theorem 5.3(1) of the first lesson). For every \(n\ge1\),
\[
\chi(\mathcal A^{\otimes n})=n\,\chi(\mathcal A)=\frac n{\ln2}\max_{0\le p\le1}f(p).
\]
If \(p\) maximizes \(f\), the \(2^n\) tensor products of \(\phi_\pm=\sqrt{1-p}\,|0\rangle\pm\sqrt p\,|1\rangle\), with probabilities \(2^{-n}\), form an ensemble that attains \(\chi(\mathcal A^{\otimes n})\).

*Proof.* *Upper bound.* Let \(\{q_a,\rho_a\}\) be an ensemble of states on \((\mathbb C^2)^{\otimes n}\); the \(\rho_a\) may be mixed and entangled across the sites. Let \(p_{a,j}\) be the population of \(\rho_a\) at site \(j\), and \(\bar p_j=\sum_aq_ap_{a,j}\). Corollary 3.2 and the convexity of \(e\) give
\[
\begin{aligned}
\sum_aq_aS\bigl(\mathcal A^{\otimes n}(\rho_a)\bigr)&\ge\sum_{j=1}^n\sum_aq_ae(p_{a,j})\\
&\ge\sum_{j=1}^ne(\bar p_j).
\end{aligned}
\]
The mean output \(\bar\sigma=\sum_aq_a\mathcal A^{\otimes n}(\rho_a)\) has, at site \(j\), the marginal \(\mathcal A(\bar\rho_j)\), where \(\bar\rho_j\) is the marginal of the mean input \(\sum_aq_a\rho_a\) at site \(j\); this follows from Lemma 1.3 of the first lesson, because the channels at the other sites preserve traces. So the excited population of \(\bar\sigma\) at site \(j\) is \(t_j=(1-\gamma)\bar p_j+\gamma\nu\). Corollary 2.2 of the first lesson, in the standard basis at every site, gives
\[
S(\bar\sigma)\le\sum_{j=1}^nh\bigl((1-\gamma)\bar p_j+\gamma\nu\bigr).
\]
Subtracting,
\[
\chi_{\mathcal A^{\otimes n}}\{q_a,\rho_a\}\le\sum_{j=1}^nf(\bar p_j)\le n\max_{[0,1]}f .
\]
Taking the supremum over ensembles, \((\ln2)\,\chi(\mathcal A^{\otimes n})\le n\max f\).

*Attainment.* Let \(p\) maximize \(f\). The states \(\phi_\pm\phi_\pm^*\) have the population \(p\) and the coherences \(\pm\sqrt{p(1-p)}\), so each output has entropy \(e(p)\), and the mean input \(\operatorname{diag}(1-p,p)\) has the mean output \(\operatorname{diag}(1-t,t)\) with \(t=(1-\gamma)p+\gamma\nu\), whose entropy is \(h(t)\). So the pair with probabilities \(\frac12\) has Holevo quantity \(f(p)\). For \(n\) uses, take the \(2^n\) tensor products with probabilities \(2^{-n}\). Each output and the mean output are tensor products of one-site outputs and of the one-site mean output, and entropy is additive on tensor products, so the Holevo quantity is \(nf(p)\). For \(p\in\{0,1\}\) the two states coincide, and repeated members of the ensemble may be merged. So \((\ln2)\,\chi(\mathcal A^{\otimes n})\ge nf(p)=n\max f\).

The case \(n=1\) gives \(\chi(\mathcal A)=\max f/\ln2\), and the general case gives \(\chi(\mathcal A^{\otimes n})=n\chi(\mathcal A)\). \(\blacksquare\)

**Corollary 4.2** (the capacity; Theorem 5.3(3) of the first lesson). Under Hypothesis (CT) of the first lesson,
\[
\begin{aligned}
C(\mathcal A_{\gamma,\nu})&=\chi(\mathcal A_{\gamma,\nu})\\
&=\frac1{\ln2}\max_{0\le p\le1}f(p)
\end{aligned}
\]
bits per use.

*Proof.* By Theorem 4.1, \(\sup_n\frac1n\chi(\mathcal A^{\otimes n})=\chi(\mathcal A)\), and (CT) identifies the left side with \(C(\mathcal A)\). \(\blacksquare\)

Theorem 4.1 is a statement about all inputs of \(n\) uses and all measurements of their outputs; Corollary 4.2 turns it into a statement about codes. Entangled inputs are allowed in the codes, and the theorem shows that they do not increase the Holevo information per use. The codes of the coding theorem that achieve the capacity use product inputs and a measurement on whole blocks of outputs.

## 5. Exercises

**5.1.** Show that equality holds in Proposition 3.1 for product inputs \(\psi=\psi_1\otimes\dots\otimes\psi_n\).

**5.2.** Show that \(h(t)=g\bigl(t(1-t)\bigr)\) for \(t\in[0,1]\), and deduce that \(f(p)=g\bigl(t(1-t)\bigr)-g\bigl(v(p)\bigr)\) with \(t=t(p)\) and \(v(p)=t(1-t)-(1-\gamma)p(1-p)\). Conclude that \(f(0)=f(1)=0\), and that \(\chi(\mathcal A_{\gamma,\nu})>0\) for \(\gamma<1\).

**5.3.** Let \(p\in(0,1)\) and \(m\ge2\). Show that the ensemble of the \(m\) states \(\sqrt{1-p}\,|0\rangle+e^{2\pi ik/m}\sqrt p\,|1\rangle\), \(k=1,\dots,m\), with equal probabilities, also has Holevo quantity \(f(p)\).

**5.4.** Show that Proposition 3.1 implies \(S_{\min}(\mathcal A^{\otimes n})=n\,S_{\min}(\mathcal A)\).

**5.5.** In the proof of Proposition 3.1, why is it necessary to keep the populations \(p_{j|i}\) of the branches, instead of bounding \(S(\sigma_i)\) below by \((n-1)S_{\min}(\mathcal A)\)?

## 6. Solutions

**5.1.** For a product input, the output is the tensor product of the one-site outputs, whose entropies are \(e(p_j)\) by Lemma 5.2 of the first lesson; entropy is additive on tensor products.

**5.2.** A state \(\operatorname{diag}(1-t,t)\) has determinant \(t(1-t)\), so its entropy is both \(h(t)\) and \(g(t(1-t))\). By Lemma 5.2 of the first lesson, \(e(p)=g(v(p))\) with \(v(p)=t(1-t)-(1-\gamma)p(1-p)\). At \(p\in\{0,1\}\) the two arguments of \(g\) agree, so \(f=0\). For \(0<p<1\) and \(\gamma<1\), the second argument is smaller, and \(g\) is strictly increasing (its derivative \(2L\) is positive, Lemma 5.1 of the second lesson), so \(f(p)>0\).

**5.3.** Each state has population \(p\) and output entropy \(e(p)\). The mean of the coherences \(e^{2\pi ik/m}\sqrt{p(1-p)}\) over \(k\) is \(0\), so the mean input is \(\operatorname{diag}(1-p,p)\) and the mean output has entropy \(h(t)\).

**5.4.** By Lemma 3.1(4) of the first lesson, \(S_{\min}(\mathcal A^{\otimes n})\le nS_{\min}(\mathcal A)\). Conversely, by Lemma 3.1(2) there a pure input attains \(S_{\min}(\mathcal A^{\otimes n})\), and by Proposition 3.1 its output entropy is at least \(\sum_je(p_j)\ge n\min_pe(p)=nS_{\min}(\mathcal A)\).

**5.5.** The induction must reproduce the bound \(\sum_{j\ge2}e(p_j)\) in terms of the populations of \(\psi\). A bound by \((n-1)S_{\min}(\mathcal A)\) would give only \(S\ge e(p_1)+(n-1)S_{\min}(\mathcal A)\), which loses the dependence on \(p_2,\dots,p_n\); but the Holevo bound in Section 4 needs \(\sum_je(\bar p_j)\) to compare with \(\sum_jh(t_j)\).

## References

- [OpenAI-GAD] OpenAI, *Classical capacity and entropy inequalities for generalized amplitude damping*, OpenAI Math Release preprint, 24 September 2026, Sections 4 and 5. https://github.com/openai/math/tree/main/preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026
