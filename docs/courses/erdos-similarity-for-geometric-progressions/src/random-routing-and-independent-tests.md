# Random routing and independent tests

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson builds a random \(1\)-periodic set \(B\) of expected density \(p\) from independent random tables on the grids of [Dyadic grids and windows on a tree](dyadic-grids-and-windows-on-a-tree.md) [OpenAI-ES, Section 4]. Each point \(z\) is routed from the root of the tree to a leaf: at each vertex it takes the first child whose table entry at its key is \(1\), and the last child, the *default*, if there is none. Whether \(z\) belongs to \(B\) is then decided by a table at the leaf. If the route of a center \(x\) makes a default choice, the first vertex where it does so offers many tests, one for each index \(n\) in the windows of its non-default children, each of which puts a point \(x+tq^n\) into \(B\) when it succeeds. At a stable center these tests are independent, and at a fixed scale \(t\) all of them fail only with probability \((1-p/2)^{(M-1)r}\).

- The random tables and the random set (Section 1).
- The route of a center (Section 2).
- Local tests (Section 3).
- Independent tests at a fixed scale (Section 4).

We keep the notation of [Dyadic grids and windows on a tree](dyadic-grids-and-windows-on-a-tree.md): \(q\), \(c\), the grids \(\Gamma_b\) and keys \(J_b\), the ordered \(M\)-ary tree of height \(d\), its windows \(W_e=\{a_e,\ldots,b_e\}\), the lengths \(r_h\), the set \(\mathcal N\) of all window indices and the set \(\mathcal S\) of stable centers. All probability spaces in this lesson are finite: a probability is a finite sum, and conditioning on an event of positive probability is division by its probability.

## 1. The random tables and the random set

Fix \(p\in(0,1)\). For each edge \(e=(P,i)\) with \(i<M\) take a *selector table*
\[
S_e:\{0,\ldots,N_{b_e}-1\}\to\{0,1\}
\]
of fair bits; the last child \(P_M\) is the *default child* and its edge has no table. For each leaf \(L\), let \(b(L)\) be the right endpoint of the window of its incoming edge, and take a *terminal table*
\[
T_L:\{0,\ldots,N_{b(L)}-1\}\to\{0,1\}
\]
of bits equal to \(1\) with probability \(p\). All entries of all tables are independent. This defines a finite product probability space \(\Omega\) with probability \(\mathbb P\) and expectation \(\mathbb E\). We write \(\mathcal A\) for the family of events determined by the selector tables alone.

*Routing.* For an outcome and a point \(z\in\mathbb R\), start at the root. At an internal vertex \(P\), go to the first child \(P_i\) with \(i<M\) and \(S_{(P,i)}(J_{b_{(P,i)}}(z))=1\), or to \(P_M\) if there is no such \(i\). Let \(L(z)\) be the leaf reached, and put
\[
B=\bigl\{z\in\mathbb R:\ T_{L(z)}\bigl(J_{b(L(z))}(z)\bigr)=1\bigr\}.
\]
All keys are \(1\)-periodic and determined by the key at the finest grid of the construction, by Lemma 1.1 of [Dyadic grids and windows on a tree](dyadic-grids-and-windows-on-a-tree.md). So each realization of \(B\) is \(1\)-periodic and, in each period, a union of finitely many cells of that grid, which are half-open intervals.

**Lemma 1.1** (mean density; [OpenAI-ES, Lemma 4.1]). \(\mathbb E\rho(B)=p\).

*Proof.* Fix \(z\). The selector tables determine the leaf \(L(z)\) and the address \(J_{b(L(z))}(z)\); the terminal entry at that address is independent of the selectors and equals \(1\) with probability \(p\). So \(\mathbb P(z\in B)=p\). Since \(\Omega\) is finite,
\[
\begin{aligned}\mathbb E\rho(B)&=\sum_{\omega\in\Omega}\mathbb P(\omega)\int_0^1\mathbf 1_{B(\omega)}(z)\,dz\\&=\int_0^1\mathbb P(z\in B)\,dz=p .\qquad\square\end{aligned}
\]

## 2. The route of a center

Fix a center \(x\in\mathbb R\). The *exposure* of \(x\) is the list of all selector entries at the keys of \(x\),
\[
\bigl(S_e(J_{b_e}(x))\bigr)_{e=(P,i),\ i<M},
\]
including entries on edges off the route of \(x\). An *atom* \(\xi\) of the exposure is one possible value of this list; it has positive probability. The addresses \(J_{b_e}(x)\) do not depend on the outcome. So, conditionally on \(\xi\), the selector entries at all other addresses are still independent fair bits, and the terminal entries are still independent with probability \(p\) of being \(1\).

The exposure determines the whole route of \(x\). We say the route makes a *default choice* at a vertex where it goes to the default child.

**Lemma 2.1** (no default; [OpenAI-ES, Section 4.2]). The probability that the route of \(x\) makes no default choice is \((1-2^{1-M})^d\).

*Proof.* For an internal vertex \(P\) and \(i<M\), the event that the route, if it reaches \(P\), goes to \(P_i\) is
\[
\begin{aligned}D_{P,i}=\bigl\{&S_{(P,j)}(J_{b_{(P,j)}}(x))=0\text{ for }j<i,\\&S_{(P,i)}(J_{b_{(P,i)}}(x))=1\bigr\},\end{aligned}
\]
of probability \(2^{-i}\). Events for different vertices depend on disjoint sets of independent entries, so they are independent. The route makes no default choice exactly when, for some path \(P^0,P^1,\ldots,P^d\) from the root to a leaf with \(P^{j+1}=P^j_{i_j}\) and all \(i_j<M\), all events \(D_{P^j,i_j}\) occur; different paths give disjoint events. Hence the probability is
\[
\begin{aligned}&\sum_{i_0,\ldots,i_{d-1}<M}\ \prod_{j=0}^{d-1}2^{-i_j}\\&\quad=\Bigl(\sum_{i=1}^{M-1}2^{-i}\Bigr)^d=(1-2^{1-M})^d .\qquad\square\end{aligned}
\]

## 3. Local tests

Now let \(x\) be a stable center and \(\xi\) an atom of its exposure on which the route of \(x\) makes a default choice. Let \(U\) be the first vertex of the route where this happens, \(h\) its height and \(r=r_h\). Put
\[
\begin{gathered}e_i=(U,i)\quad(1\le i<M),\\ y_n(t)=x+tq^n\quad(t\in[1,2]).\end{gathered}
\]
On \(\xi\), all selector entries of \(x\) on the edges \(e_i\) are \(0\). For \(i<M\) and a point \(z\), let \(L_i(z)\) be the leaf reached by routing \(z\) from the child \(U_i\) (so \(L_i(z)=U_i\) if \(U_i\) is a leaf), and define the *local test*
\[
\begin{aligned}&Q_i(z)=S_{e_i}\bigl(J_{b_{e_i}}(z)\bigr)\\&\quad\cdot T_{L_i(z)}\bigl(J_{b(L_i(z))}(z)\bigr).\end{aligned}\tag{3.1}
\]
It reads only the table of \(e_i\) and the tables below \(U_i\).

**Lemma 3.1** (the route is preserved; [OpenAI-ES, Lemma 4.2]). On \(\xi\), for every outcome, every \(i<M\), every \(n\in W_{e_i}\) and every \(t\in[1,2]\), the route of \(y_n(t)\) reaches \(U\) and does not take the children \(U_1,\ldots,U_{i-1}\). Consequently
\[
\begin{gathered}Q_i\bigl(y_n(t)\bigr)=1\\ \Longrightarrow\ y_n(t)\in B .\end{gathered}\tag{3.2}
\]

*Proof.* Let \(P\) be a vertex of the route of \(x\) above \(U\), and let \(a\) be the child chosen there by \(x\); then \(a<M\), since \(U\) is the first default. The choice at \(P\) reads the entries on the edges \((P,1),\ldots,(P,a)\). These edges come before \(e_i\) in preorder, because \(e_i\) lies in the subtree of \(P_a\), and preorder lists \((P,j)\) for \(j\le a\) before that subtree. By Lemma 3.2 of [Dyadic grids and windows on a tree](dyadic-grids-and-windows-on-a-tree.md), the keys of \(y_n(t)\) and \(x\) on these edges agree, so \(y_n(t)\) reads the same entries and also goes to \(P_a\). Starting from the root, \(y_n(t)\) therefore follows the route of \(x\) down to \(U\). At \(U\), the edges \((U,j)\) with \(j<i\) also come before \(e_i\); so \(y_n(t)\) reads the entries of \(x\) on them, which are \(0\).

If \(Q_i(y_n(t))=1\), the selector of \(y_n(t)\) on \(e_i\) is \(1\), so its route goes to \(U_i\), continues to the leaf \(L_i(y_n(t))\), and finds the terminal entry \(1\) there. By the definition of \(B\), \(y_n(t)\in B\). \(\square\)

## 4. Independent tests at a fixed scale

**Lemma 4.1** (independent tests; [OpenAI-ES, Lemma 4.3]). Let \(x\in\mathcal S\) and \(\xi\) be as in Section 3, with \(U\), \(h\) and \(r=r_h\). For every fixed \(t\in[1,2]\),
\[
\begin{aligned}&\mathbb P\Bigl(Q_i\bigl(y_n(t)\bigr)=0\\&\qquad\text{for all }i<M\\&\qquad\text{and all }n\in W_{e_i}\Bigm|\xi\Bigr)\\&\quad=\Bigl(1-\frac p2\Bigr)^{(M-1)r}.\end{aligned}\tag{4.1}
\]

*Proof.* On \(\xi\) the set \(\mathcal I=\{(i,n):1\le i<M,\ n\in W_{e_i}\}\) is fixed and has \((M-1)r\) elements. Put \(A_{i,n}=S_{e_i}\bigl(J_{b_{e_i}}(y_n(t))\bigr)\).

*The selector bits.* For fixed \(i\), the points \(x\) and \(y_n(t)\), \(n\in W_{e_i}\), have pairwise distinct keys at resolution \(b_{e_i}\) by Lemma 4.1 of [Dyadic grids and windows on a tree](dyadic-grids-and-windows-on-a-tree.md). So the \(A_{i,n}\) read distinct entries of the table \(S_{e_i}\), none of them the entry exposed at \(x\). Different \(i\) use different tables. Conditionally on \(\xi\), the \(A_{i,n}\) are therefore independent fair bits.

*The terminal bits.* Condition further on all selector tables. Then the leaf \(L_{i,n}=L_i(y_n(t))\) and the address
\[
\kappa_{i,n}=\bigl(L_{i,n},\ J_{b(L_{i,n})}(y_n(t))\bigr)
\]
are fixed for every pair, and these addresses are distinct. For different \(i\), the leaves lie in the disjoint subtrees below \(U_i\). For equal \(i\) and different leaves, the tables differ. For equal \(i\), equal leaves \(L\) and \(n\ne n'\): the incoming edge of \(L\) is \(e_i\) or an edge below \(U_i\), whose window comes after \(W_{e_i}\), so \(b(L)\ge b_{e_i}\), and the keys of \(y_n(t)\) and \(y_{n'}(t)\) at resolution \(b(L)\) differ by Lemma 4.1 of [Dyadic grids and windows on a tree](dyadic-grids-and-windows-on-a-tree.md). So the terminal entries at the addresses \(\kappa_{i,n}\) are independent and equal \(1\) with probability \(p\), whatever the selector tables are. A pair with \(A_{i,n}=0\) fails; a pair with \(A_{i,n}=1\) fails exactly when its terminal entry is \(0\). Hence, given the selector tables (on \(\xi\)), all tests fail with probability \((1-p)^{\sum_{\mathcal I}A_{i,n}}\).

*Averaging.* Taking the conditional expectation given \(\xi\) and using the independence of the \(A_{i,n}\),
\[
\begin{aligned}&\mathbb E\Bigl[(1-p)^{\sum_{\mathcal I}A_{i,n}}\Bigm|\xi\Bigr]\\&\quad=\prod_{(i,n)\in\mathcal I}\Bigl(\frac12+\frac{1-p}2\Bigr)\\&\quad=\Bigl(1-\frac p2\Bigr)^{(M-1)r}.\qquad\square\end{aligned}
\]

The tests at one scale \(t\) are independent. In [Every scale and every center](every-scale-and-every-center.md), finitely many scales, fixed in advance on the atom \(\xi\), represent all \(t\in[1,2]\), and a union bound over them handles every scale at once.

## 5. Exercises

**5.1.** For \(M=2\), compute the probability in Lemma 2.1 and describe the event of no default choice.

**5.2.** Show that \(\mathbb E\rho(B)=p\) also follows from the formula \(\mathbb P(z\in B)=p\) for each \(z\) by the theorem of Fubini on \(\Omega\times[0,1)\), and explain why the finite form used in the proof of Lemma 1.1 suffices.

**5.3.** Suppose that in Lemma 4.1 two points \(y_n(t)\), \(y_{n'}(t)\) with \(n\ne n'\) had the same key at resolution \(b_{e_i}\). Show that the probability in (4.1) could then be larger than \((1-p/2)^{(M-1)r}\), by computing it for \(M=2\), \(r=2\) and two points with the same key and the same leaf.

**5.4.** Show that \((1-p/2)^{k}\le e^{-pk/2}\) for all integers \(k\ge0\).

**5.5.** Show that if the route of \(x\) makes no default choice, the leaf \(L(x)\) is determined by the exposure, and explain why Lemma 3.1 needs \(x\) to be stable.

## 6. Solutions

**5.1.** \((1-2^{-1})^d=2^{-d}\): at every vertex of the route the single selector entry of \(x\) must be \(1\), so the route goes to the first child at every step and ends at the leftmost leaf.

**5.2.** The function \((\omega,z)\mapsto\mathbf 1_{B(\omega)}(z)\) is measurable on \(\Omega\times[0,1)\), and its integral computed in the two orders gives \(\mathbb E\rho(B)\) and \(\int_0^1\mathbb P(z\in B)\,dz\). Since \(\Omega\) is finite, the integral over \(\Omega\) is a finite weighted sum, and exchanging a finite sum with an integral is linearity of the integral.

**5.3.** Let the two points read the same selector entry \(A\) and the same terminal entry \(T\). Both tests fail exactly when \(AT=0\), an event of probability \(1-\frac p2\), instead of \((1-\frac p2)^2\) for two independent tests.

**5.4.** \(1-u\le e^{-u}\) for real \(u\), by convexity of the exponential; take \(u=p/2\) and raise to the power \(k\).

**5.5.** The route reads only entries at the keys of \(x\), which form the exposure. In Lemma 3.1 the point \(y_n(t)\) must read the same entries as \(x\) above \(U\); this holds when its keys on the earlier edges equal those of \(x\), which is Lemma 3.2 of [Dyadic grids and windows on a tree](dyadic-grids-and-windows-on-a-tree.md) for stable \(x\). At an unstable center a translation can cross a cell boundary of an earlier grid, and \(y_n(t)\) may then leave the route of \(x\).

## References

- [OpenAI-ES] OpenAI, *The geometric case of the Erdős similarity conjecture*, OpenAI Math Release preprint, 5 October 2026, Section 4. https://github.com/openai/math/tree/main/preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026
