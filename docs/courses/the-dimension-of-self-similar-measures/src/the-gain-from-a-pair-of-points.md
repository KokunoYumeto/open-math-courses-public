# The gain from a pair of points

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Replace every point of a law on the line by two points at the distance \(v\), each with half the mass. At scales much larger than \(v\) the two points are rarely separated by a grid, and the entropy hardly changes. At the scale \(v\) the entropy grows by exactly the one-bit deficit \(\Delta_v\) of the law, and at a smaller scale \(s\) it grows by at least \(\Delta_v-s/v\). So the entropy between a small scale \(s\) and a large scale \(t\) grows by at least the one-bit deficit at the scale \(v\), up to the errors \(s/v\) and \(v/t\). The lesson proves this. It then defines how much mass of a finite law can be arranged in such pairs of a given size, the *pair capacity*, and proves the form in which the proof of [OpenAI-S] uses the gain: every unit of pair capacity of a factor of a convolution yields a definite gain of entropy.

- The two-point gain (Theorem 1.2).
- Pair capacities of a finite law (Definition 2.1).
- The gain of a convolution from the pairs of one factor (Theorem 2.3).

The lesson follows [OpenAI-S, Section 2, the lemma on the two-point gain; Section 3, the definition of pair capacity; Section 5, the proof of the lemma on the conditional pair gain]. According to [OpenAI-S], the comparison of fair pairs follows a method of P. Varjú. The lesson continues [Entropy at a scale](entropy-at-a-scale.md), whose notation it uses: \(\mathcal H_s\), \(G_{s,t}=\mathcal H_s-\mathcal H_t\) and \(\Delta_v=1-G_{v,2v}\). It uses the rules for mutual information from [Entropy of finite random variables](entropy-of-finite-random-variables.md).

## 1. The two-point gain

Let \(X\) be a bounded random variable, \(v>0\), and \(J\) a fair bit with the values \(0,1\), independent of \(X\). Let \(Y=X+vJ\). For a scale \(a>0\) put
\[
D_a=\mathcal H_a(Y)-\mathcal H_a(X).
\]

**Lemma 1.1.**

1. \(D_a=\int_0^1I\bigl(J;\lfloor Y/a+u\rfloor\bigr)\,du\) for every \(a>0\); in particular \(D_a\ge0\).
2. \(D_v=\Delta_v(X)\).
3. \(D_s\ge D_v-\tfrac sv\) for \(0<s<v\).
4. \(D_t\le\tfrac vt\) for \(t>v\).

**Proof.** All the integrands below are bounded Borel functions of the shifts, for the reason given in Section 1 of the lesson on entropy at a scale: the probabilities of the cells of a grid, and of the intersection of a cell of one grid with a cell of another, are differences of values of a distribution function at points that depend continuously on the shifts.

(1) Fix \(u\) and let \(Z=\lfloor Y/a+u\rfloor\). Given \(J=0\), \(Z\) is the label of \(X\); given \(J=1\), it is the label of \(X+v\). So \(H(Z\mid J)\) is \(\tfrac12H_{a,u}(X)+\tfrac12H_{a,u}(X+v)\). Its integral over \(u\) is \(\tfrac12\mathcal H_a(X)+\tfrac12\mathcal H_a(X+v)\), which is \(\mathcal H_a(X)\) by Lemma 1.1 of the lesson on entropy at a scale. Hence the integral of \(I(J;Z)=H(Z)-H(Z\mid J)\) is \(\mathcal H_a(Y)-\mathcal H_a(X)\).

(2) is Corollary 3.2 of the lesson on entropy at a scale.

(3) Take a grid of length \(s\) with the shift \(u\) and a grid of length \(v\) with the shift \(u'\), and let \(Z_s,Z_v\) be the labels of \(Y\) in the two grids. By Proposition 3.1 of the lesson on entropy of finite random variables,
\[
\begin{aligned}
I(J;Z_v)&\le I(J;(Z_s,Z_v))\\
&=I(J;Z_s)+I(J;Z_v\mid Z_s)\\
&\le I(J;Z_s)+H(Z_v\mid Z_s).
\end{aligned}
\]
A cell of the grid of length \(s\) is an interval of length \(s<v\). If no boundary of the other grid lies in its interior, \(Z_v\) is constant on the event that \(Y\) is in this cell; otherwise \(Z_v\) takes at most two values there. For a fixed cell, the set of the shifts \(u'\) for which a boundary lies in its interior has the measure \(s/v\). So for every \(u\)
\[
\begin{aligned}
\int_0^1H(Z_v\mid Z_s)\,du'&\le\sum_c\mathbb P(Z_s=c)\,\frac sv\\
&=\frac sv .
\end{aligned}
\]
Integrating the first display over \(u\) and \(u'\) and using (1) gives \(D_v\le D_s+s/v\).

(4) Fix \(u\), and let \(A=\lfloor X/t+u\rfloor\) and \(A'=\lfloor(X+v)/t+u\rfloor\), the labels of \(X\) and of \(X+v\). The label \(Z\) of \(Y\) is \(A\) if \(J=0\) and \(A'\) if \(J=1\). Since \(J\) is independent of \((A,A')\), we have \(I(J;(A,A'))=0\), and
\[
\begin{aligned}
I(J;Z)&\le I(J;(Z,A,A'))\\
&=I(J;Z\mid A,A').
\end{aligned}
\]
On the event \(A=A'\) the label \(Z\) is determined by \((A,A')\), and on the event \(A\ne A'\) the conditional information is at most \(H(J)=1\). So \(I(J;Z)\le\mathbb P(A\ne A')\). For a fixed value \(x\) of \(X\), the labels of \(x\) and \(x+v\) differ exactly if a boundary of the grid lies in \((x,x+v]\), which happens for a set of shifts of the measure \(v/t\). Integrating over \(u\) and exchanging the integral with the expectation gives \(D_t\le v/t\). \(\blacksquare\)

**Theorem 1.2 (two-point gain).** Let \(X\) be bounded, \(J\) an independent fair bit, and \(0<s<v<t\). Then
\[
\begin{aligned}
&G_{s,t}(X+vJ)-G_{s,t}(X)\\
&\quad\ge\ \Delta_v(X)-\frac sv-\frac vt .
\end{aligned}
\]
The same holds for \(X+B\) in place of \(X+vJ\), where \(B\) is independent of \(X\) and takes two values at the distance \(v\) with probability \(\tfrac12\) each.

**Proof.** The left side is \(D_s-D_t\). By Lemma 1.1, \(D_s-D_t\ge D_v-\tfrac sv-\tfrac vt\), and \(D_v=\Delta_v(X)\). A variable \(B\) as in the last statement is \(c+vJ\) with a constant \(c\) and a fair bit \(J\), and \(G_{s,t}\) does not change under translations. \(\blacksquare\)

No integer ratio of the scales is needed in Theorem 1.2. The theorem is useful when \(s\) is much smaller and \(t\) much larger than \(v\), and when the deficit \(\Delta_v(X)\) is not small. By Theorem 3.5 of the lesson [The one-bit deficit of a self-similar measure](the-one-bit-deficit.md), a self-similar measure that is exact dimensional with a dimension less than one has \(\Delta_v\ge\delta\) at every scale \(v\), with a constant \(\delta>0\).

## 2. Pairs inside a finite law

A *fair pair* is a law that gives the mass \(\tfrac12\) to each of two different points; its *size* is their distance.

**Definition 2.1.** Let \(\nu\) be a law with a finite support \(F\subset\mathbb R\), and \(\ell\) an integer. Let \(\mathcal E_\ell(F)\) be the set of the pairs \(e=\{x,y\}\) of points of \(F\) with \(2^{-\ell}\le|x-y|<2^{1-\ell}\). A family of numbers \(w_e\ge0\), \(e\in\mathcal E_\ell(F)\), is *feasible* if
\[
\frac12\sum_{e\ni x}w_e\le\nu(\{x\})\qquad\text{for every }x\in F .
\]
The *pair capacity* \(c_\ell(\nu)\) is the largest value of \(\sum_ew_e\) over the feasible families; it is \(0\) if \(\mathcal E_\ell(F)\) is empty.

If \(\beta_e\) denotes the fair pair on the two points of \(e\), feasibility says that the measure \(\sum_ew_e\beta_e\) is at most \(\nu\) at every point. So \(c_\ell(\nu)\) is the largest mass of \(\nu\) that can be written as a combination of fair pairs with sizes in \([2^{-\ell},2^{1-\ell})\). Summing the conditions over \(x\) gives \(\sum_ew_e\le1\). The maximum exists, because the feasible families form a closed bounded set in a space of finite dimension. For a fixed finite law only finitely many \(c_\ell(\nu)\) are different from \(0\).

**Example 2.2.** If \(\nu\) gives the masses \(q\) and \(1-q\) to two points at the distance \(1\), then \(c_0(\nu)=2\min\{q,1-q\}\) and all other capacities vanish. If \(\nu\) is uniform on the four points \(0,1,10,11\), then \(c_0(\nu)=1\), with the pairs \(\{0,1\}\) and \(\{10,11\}\) of weight \(\tfrac12\) each; and \(c_{-3}(\nu)=1\) as well, since \(8\le|x-y|<16\) for the pairs \(\{0,10\}\), \(\{0,11\}\), \(\{1,10\}\), \(\{1,11\}\).

**Theorem 2.3 (gain from pairs).** Let \(s>0\), \(N\ge2\) an integer and \(t=Ns\). Let \(\nu\) be a law with finite support, and \(w_e\ge0\) numbers, indexed by finitely many pairs \(e\) of points of the support, such that \(\tfrac12\sum_{e\ni x}w_e\le\nu(\{x\})\) for all \(x\), and such that the size \(v_e\) of every pair with \(w_e>0\) satisfies \(s<v_e<t\). Let \(\lambda\) be a bounded law. Then the convolution \(\nu*\lambda\), the law of the sum of independent variables with the laws \(\nu\) and \(\lambda\), satisfies
\[
\begin{aligned}
&G_{s,t}(\nu*\lambda)\ \ge\ G_{s,t}(\lambda)\\
&\quad+\sum_ew_e\Bigl(\Delta_{v_e}(\lambda)-\frac s{v_e}-\frac{v_e}t\Bigr).
\end{aligned}
\]

**Proof.** Let \(\beta_e\) be the fair pair of \(e\), and \(\nu_0=\nu-\sum_ew_e\beta_e\). By the assumption \(\nu_0\) is a measure with a mass \(\varrho_0=1-\sum_ew_e\ge0\) at finitely many points. So \(\nu\) is the mixture of the laws \(\beta_e\) with the weights \(w_e\) and, if \(\varrho_0>0\), of the law \(\nu_0/\varrho_0\) with the weight \(\varrho_0\). Convolution with \(\lambda\) turns this into a mixture of the laws \(\beta_e*\lambda\) and \((\nu_0/\varrho_0)*\lambda\) with the same weights. The ratio \(t/s\) is an integer, so by Proposition 2.4 of the lesson on entropy at a scale
\[
\begin{aligned}
G_{s,t}(\nu*\lambda)&\ge\sum_ew_e\,G_{s,t}(\beta_e*\lambda)\\
&\quad+\varrho_0\,G_{s,t}\bigl((\nu_0/\varrho_0)*\lambda\bigr).
\end{aligned}
\]
By the same proposition, part (2), the last term is at least \(\varrho_0G_{s,t}(\lambda)\). By Theorem 1.2, \(G_{s,t}(\beta_e*\lambda)\) is at least \(G_{s,t}(\lambda)+\Delta_{v_e}(\lambda)-s/v_e-v_e/t\). The weights \(w_e\) and \(\varrho_0\) add up to \(1\), and the stated inequality follows. \(\blacksquare\)

The theorem is applied with weights that realize a pair capacity \(c_\ell(\nu)\): if all the sizes lie in \([2^{-\ell},2^{1-\ell})\), strictly between \(s\) and \(t\), and \(\Delta_v(\lambda)\ge\delta\) for all these sizes, the gain is at least \(c_\ell(\nu)\) times \(\delta\) minus the two error terms.

## 3. Exercises

**3.1.** Let \(X\) be constant. Compute \(D_a\) for all \(a\), and check the four statements of Lemma 1.1 and Theorem 1.2.

**3.2.** Show that \(D_t\le1\) and \(D_s\le1\) for all scales, and that \(G_{s,t}(X+vJ)-G_{s,t}(X)\le1\).

**3.3.** Let \(\nu\) be uniform on the three points \(0,1,2\). Compute \(c_0(\nu)\) and \(c_{-1}(\nu)\).

**3.4.** Show that \(c_\ell(\nu)\le1\), and that \(c_\ell(\nu)=1\) if \(\nu\) is the law of \(x+2^{-\ell}J\), where \(x\) is distributed according to a law with a finite support whose points have pairwise distances that are not equal to \(2^{-\ell}\), and \(J\) is an independent fair bit.

## 4. Solutions

**3.1.** \(Y\) is a fair pair of the size \(v\), and by Exercise 4.1 of the lesson on entropy at a scale \(\mathcal H_a(Y)=\min\{1,v/a\}\), while \(\mathcal H_a(X)=0\). So \(D_a=\min\{1,v/a\}\). Then \(D_v=1=\Delta_v(X)\); for \(s<v\), \(D_s=1\ge1-s/v\); for \(t>v\), \(D_t=v/t\). The gain is \(1-v/t\ge1-s/v-v/t\).

**3.2.** By Lemma 1.1 (1), \(D_a\) is a mean of mutual informations with the fair bit \(J\), which are at most \(H(J)=1\). The gain is \(D_s-D_t\le D_s\le1\).

**3.3.** The pairs with \(1\le|x-y|<2\) are \(\{0,1\}\) and \(\{1,2\}\), with weights \(w,w'\). Feasibility: \(\tfrac w2\le\tfrac13\), \(\tfrac{w'}2\le\tfrac13\) and \(\tfrac{w+w'}2\le\tfrac13\). So \(c_0=\tfrac23\). The only pair with \(2\le|x-y|<4\) is \(\{0,2\}\), and \(c_{-1}=\tfrac23\).

**3.4.** The first statement was shown after Definition 2.1. For the second, the support of \(\nu\) consists of the points \(x\) and \(x+2^{-\ell}\); the assumption on the distances says that these are all different. Give the pair \(\{x,x+2^{-\ell}\}\) the weight of \(x\) in the law of the first variable. Then \(\sum_ew_e\beta_e=\nu\), the family is feasible, and its sum is \(1\).

## References

- [OpenAI-S] OpenAI, *The entropy-rate dimension formula for self-similar measures on the line*, OpenAI Math Release preprint, 24 September 2026, Sections 2, 3 and 5. https://github.com/openai/math/tree/main/preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026
