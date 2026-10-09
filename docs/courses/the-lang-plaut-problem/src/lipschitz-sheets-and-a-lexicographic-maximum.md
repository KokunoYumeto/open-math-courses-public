# Lipschitz sheets and a lexicographic maximum

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Suppose that the set \(S\) of [Doubling spaces and coloured strips](doubling-spaces-and-coloured-strips.md) had a bi-Lipschitz embedding \(f\) into \(\mathbb R^k\). Restricted to the copy of an open subset of the plane formed by the points \((p,w)\) with \(w\) fixed, \(f\) gives a Lipschitz map of that open set into \(\mathbb R^k\), a *sheet*. Lipschitz maps of the plane are differentiable almost everywhere. This lesson collects the facts about such maps that the argument uses: good points, where the derivative is approached in mean square (Lemma 1.1); integration of the derivative along lines (Lemma 1.2); and a compact set \(K\) recording the squared lengths of the two derivative columns of all sheets at all good points. Maximizing first one coordinate and then the other over \(K\) gives two numbers \(A,B\), and Lemma 3.1 says what happens near this lexicographic maximum. The proof of the theorem, in [Two energy estimates](two-energy-estimates.md) and [Crossings and the Lang–Plaut problem](crossings-and-the-lang-plaut-problem.md), works near the point \((A,B)\) [OpenAI-L, Section 3].

We use from the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10), in Fremlin's *Measure Theory*, Volume 2: Rademacher's theorem, that a Lipschitz map from a subset of \(\mathbb R^r\) to \(\mathbb R^s\) is differentiable (relative to its domain) at almost every point of its domain (262Q); that a Lipschitz function on a closed bounded interval is absolutely continuous (262Bc), and an absolutely continuous function is the integral of its derivative (225E); Lebesgue's differentiation theorem, that a locally integrable function \(g\) on \(\mathbb R^r\) satisfies \(\mu(B(p,\delta))^{-1}\int_{B(p,\delta)}|g-g(p)|\to0\) as \(\delta\to0\) for almost every \(p\) (261E); that Lebesgue measure on \(\mathbb R^2\) is the product of Lebesgue measures on \(\mathbb R\) (251N), so that almost every horizontal or vertical section of a null set is null (252D); and Markov's inequality. Integrals of \(\mathbb R^k\)-valued functions are taken coordinatewise, and \(\|\int g\|\le\int\|g\|\).

## 1. Lipschitz maps of plane domains

Let \(\Omega\subseteq\mathbb R^2\) be open and \(F:\Omega\to\mathbb R^k\) Lipschitz with constant \(D\). Write \(F_x=\partial F/\partial x\) and \(F_y=\partial F/\partial y\), the two columns of the derivative where \(F\) is differentiable. At such a point the difference quotients \((F(p+he_1)-F(p))/h\) have norm at most \(D\), so \(\|F_x\|,\|F_y\|\le D\). The columns are measurable, as pointwise limits of difference quotients on the conegligible set of differentiability points. For a set \(E\) of finite positive area and an integrable \(h\) on it, write \(\langle h\rangle_E=|E|^{-1}\int_Eh\), where \(|E|\) is the area. Let \(Q(p,l)\) be the closed square of side \(l\) centred at \(p\).

**Lemma 1.1** (good points). For almost every \(p\in\Omega\), \(F\) is differentiable at \(p\) and, with \(u=F_x(p)\) and \(v=F_y(p)\),
\[
\lim_{l\to0}\bigl\langle\|F_x-u\|^2+\|F_y-v\|^2\bigr\rangle_{Q(p,l)}=0.\tag{1.1}
\]
We call such points *good*.

**Proof.** By Rademacher's theorem, \(F\) is differentiable almost everywhere in \(\Omega\). Extend the \(2k\) coordinates of \(F_x\) and \(F_y\) by \(0\) to the rest of \(\mathbb R^2\); they are bounded and measurable, hence locally integrable. By Lebesgue's differentiation theorem, applied to each coordinate, almost every \(p\in\Omega\) satisfies \(\mu(B(p,\delta))^{-1}\int_{B(p,\delta)}\|F_x-u\|\to0\) and the same for \(F_y\) and \(v\). Since \(\|F_x-u\|\le2D\), \(\|F_x-u\|^2\le2D\|F_x-u\|\). Finally \(Q(p,l)\subseteq B(p,l)\), whose area is \(\pi l^2=\pi|Q(p,l)|\), so averages of a nonnegative function over \(Q(p,l)\) are at most \(\pi\) times its averages over \(B(p,l)\). \(\square\)

**Lemma 1.2** (line integrals). For almost every \(y\), the following holds. Let \(I\) be a bounded open interval with \(I\times\{y\}\subseteq\Omega\), with closure \([a,b]\). Then \(x\mapsto F(x,y)\) extends continuously to \([a,b]\), the extension is \(D\)-Lipschitz, and
\[
F(b,y)-F(a,y)=\int_a^bF_x(x,y)\,dx,\qquad\|F(b,y)-F(a,y)\|\le(b-a)^{1/2}\Bigl(\int_a^b\|F_x(x,y)\|^2dx\Bigr)^{1/2}.\tag{1.2}
\]
The same holds for vertical segments, with \(F_y\).

**Proof.** The points of \(\Omega\) where \(F\) is not differentiable form a null set, so for almost every \(y\) they meet the line at height \(y\) in a null set. Fix such a \(y\). The map \(\varphi(x)=F(x,y)\) on \(I\) is \(D\)-Lipschitz, so \(\varphi(x_n)\) is a Cauchy sequence whenever \(x_n\) converges in \([a,b]\); this gives the Lipschitz extension. Each coordinate of the extension is absolutely continuous on \([a,b]\), and at every \(x\in I\) where \(F\) is differentiable at \((x,y)\) its derivative is the corresponding coordinate of \(F_x(x,y)\). That is almost every \(x\), so the integral formula holds. The inequality follows from \(\|\int g\|\le\int\|g\|\) and the Cauchy–Schwarz inequality. \(\square\)

## 2. Sheets of an embedding

Suppose that \(f:S\to\mathbb R^k\) is a bi-Lipschitz embedding. Dividing \(f\) by its scale, we may assume that for some \(D\ge1\)
\[
\|z-z'\|\le\|f(z)-f(z')\|\le D\|z-z'\|\qquad(z,z'\in S).\tag{2.1}
\]
For a finitely supported sequence \(w\) as in Section 2 of [Doubling spaces and coloured strips](doubling-spaces-and-coloured-strips.md) with nonempty \(\Omega_w\), the *sheet* \(F_w:\Omega_w\to\mathbb R^k\), \(F_w(p)=f(p,w)\), is \(D\)-Lipschitz, because \(\|(p,w)-(p',w)\|=\|p-p'\|\). Let \(K\) be the closure in \([0,D^2]^2\) of the set of pairs
\[
\bigl(\|F_x(p)\|^2,\|F_y(p)\|^2\bigr),
\]
where \(F\) runs over all sheets and \(p\) over the good points of \(F\) (Lemma 1.1). The sheet of \(w=0\) is defined on the whole plane and has good points, so \(K\) is a nonempty compact set. Put
\[
A=\max\{s:(s,t)\in K\},\qquad B=\max\{t:(A,t)\in K\}.\tag{2.2}
\]
So \((A,B)\in K\), and \(\|F_x(p)\|^2\le A\) at every good point of every sheet. The numbers \(A,B\) and the set \(K\) depend only on \(f\).

## 3. Near the lexicographic maximum

**Lemma 3.1** (lexicographic maximum). Let \(K\subseteq[0,D^2]^2\) be nonempty and compact, and define \(A,B\) by (2.2).

(a) For every \(\varepsilon>0\) there is \(\delta>0\) such that every \((s,t)\in K\) with \(s>A-\delta\) has \(t\le B+\varepsilon\).

(b) Let \((s_n,t_n)\) be measurable functions on probability spaces with values in \(K\), and suppose \(\mathbb E(A-s_n)\to0\). Then \(\limsup_n\mathbb Et_n\le B\).

**Proof.** (a) Otherwise there are \((s_m,t_m)\in K\) with \(s_m\to A\) and \(t_m>B+\varepsilon\); a convergent subsequence has a limit \((A,t)\in K\) with \(t\ge B+\varepsilon\), contradicting the definition of \(B\).

(b) Let \(\varepsilon>0\) and \(\delta\) as in (a). Since \(A-s_n\ge0\), Markov's inequality gives \(\mathbb P(A-s_n\ge\delta)\le\mathbb E(A-s_n)/\delta\). On the complement \(t_n\le B+\varepsilon\), and everywhere \(t_n\le D^2\), so \(\mathbb Et_n\le B+\varepsilon+D^2\,\mathbb E(A-s_n)/\delta\). Let \(n\to\infty\) and then \(\varepsilon\to0\). \(\square\)

Part (b) is the form used: if the mean of the first coordinate approaches its largest possible value \(A\), the mean of the second coordinate cannot exceed \(B\) in the limit. No rate is involved.

## 4. Mean and variance

**Lemma 4.1** (variance). Let \(G\) be a bounded measurable \(\mathbb R^k\)-valued function on a set \(E\) of finite positive area, and \(a\in\mathbb R^k\). Then, with averages over \(E\),
\[
\bigl\langle\|G-a\|^2\bigr\rangle=\bigl\langle\|G\|^2\bigr\rangle-\|a\|^2-2\bigl\langle a,\langle G\rangle-a\bigr\rangle\le\bigl\langle\|G\|^2\bigr\rangle-\|a\|^2+2\|a\|\,\|\langle G\rangle-a\|.
\]

**Proof.** Average \(\|G-a\|^2=\|G\|^2-2\langle G,a\rangle+\|a\|^2\) and write \(-2\langle\langle G\rangle,a\rangle+\|a\|^2=-\|a\|^2-2\langle a,\langle G\rangle-a\rangle\). The inequality is Cauchy–Schwarz. \(\square\)

So a field whose mean squared length is at most about \(\|a\|^2\), and whose mean is close to \(a\), is close to \(a\) in mean square. In the next lesson the bound on the mean squared length comes from the maximality of \(A\), or from Lemma 3.1(b), and the closeness of the mean comes from Lemma 1.2.

## 5. Exercises

**Exercise 5.1** (easy). Let \(F\) be differentiable at \(p\). Show that \(\|F_x(p)\|\le D\), and more generally that \(\|dF_p(h)\|\le D\|h\|\) for every \(h\in\mathbb R^2\).

**Exercise 5.2** (easy). Let \(K=\{(1-\frac1n,1):n\ge1\}\cup\{(1,0)\}\), which is not closed. Define \(A\) and \(B\) by (2.2) and show that Lemma 3.1(a) fails. What are \(A\) and \(B\) for the closure of \(K\)?

**Exercise 5.3** (easy). Give a compact \(K\subseteq[0,1]^2\) for which maximizing the second coordinate first, and then the first coordinate, gives a different point of \(K\) than (2.2).

**Exercise 5.4** (medium). Let \(G\) take values in a set where \(\|G\|^2\le A\), and let \(\|a\|^2\ge A-\eta\) and \(\|\langle G\rangle-a\|\le\gamma\). Show that \(\langle\|G-a\|^2\rangle\le\eta+2\|a\|\gamma\).

## 6. Solutions

**5.1.** \(dF_p(h)=\lim_{s\downarrow0}(F(p+sh)-F(p))/s\), and the difference quotients have norm at most \(D\|h\|\) for small \(s\). Take \(h=e_1\).

**5.2.** \(A=1\) (attained only at \((1,0)\)) and \(B=0\), but the points \((1-\frac1n,1)\) have first coordinates tending to \(A\) and second coordinate \(1>B+\frac12\). The closure adds \((1,1)\), and then \(A=B=1\).

**5.3.** \(K=\{(1,0),(0,1)\}\): (2.2) gives \((1,0)\), while maximizing the second coordinate first gives \((0,1)\).

**5.4.** By Lemma 4.1, \(\langle\|G-a\|^2\rangle\le A-\|a\|^2+2\|a\|\gamma\le\eta+2\|a\|\gamma\).

## References

- [OpenAI-L] OpenAI, *A doubling Hilbert subset with no finite-dimensional bi-Lipschitz embedding*, OpenAI Math Release preprint, 25 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026
