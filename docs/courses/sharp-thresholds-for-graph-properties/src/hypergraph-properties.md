# Hypergraph properties

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For \(r\ge3\) and \(n\ge r\), let \(E_{n,r}=\binom{[n]}r\); an element of \(\{0,1\}^{E_{n,r}}\) is an \(r\)-uniform hypergraph on \([n]\), and a *hypergraph property* is a function on this space invariant under the permutations of \([n]\). Friedgut and Kalai conjectured that increasing \(r\)-uniform hypergraph properties have threshold width \(O_{r,\varepsilon}((\log n)^{-r/(r-1)})\), and Bourgain and Kalai came within any power \((\log n)^\eta\) of it. This lesson proves the conjecture [OpenAI-T2]:

**Theorem 3.1** (OpenAI). For every \(r\ge3\) there is a constant \(C_r\) such that for every \(n\ge r\), every \(0<p<1\) and every hypergraph property \(f:\{0,1\}^{E_{n,r}}\to\{0,1\}\),
\[
\operatorname{Var}_p(f)\le\frac{C_r}{(\log n)^{r/(r-1)}}\,I_p(f).
\]

**Corollary 3.2** (OpenAI). For a nontrivial increasing property of \(r\)-uniform hypergraphs on \(n\ge r\) vertices and \(0<\varepsilon<\frac12\), \(p_{1-\varepsilon}-p_\varepsilon\le\frac{2C_r}{(\log n)^{r/(r-1)}}\log\frac{1-\varepsilon}\varepsilon\).

The proof follows [Vertex blocks and graph properties](vertex-blocks-and-graph-properties.md): restrict to the edges meeting a random block \(B\) of about \(\sqrt n\) vertices, bound the restricted low-degree mass by the hypercontractive estimate, and transfer it to the original Fourier degrees. The one change is combinatorial: an \(r\)-uniform hypergraph with \(s\) edges has a vertex of degree between \(1\) and \(rs^{(r-1)/r}\), so restricted degrees up to \(k\) control original degrees up to \((k/r)^{r/(r-1)}\). With \(k\) of order \(\sigma\log n\), the exponent becomes \(r/(r-1)\), and the factor \(\sigma^{2-r/(r-1)}\), with a positive exponent, makes the bound uniform in the bias.

We use Lemmas 2.1, 2.2 and 4.1 of [Biased Fourier analysis and hypercontractivity](biased-fourier-analysis-and-hypercontractivity.md) and Lemma 1.1 of [Vertex blocks and graph properties](vertex-blocks-and-graph-properties.md), whose statement and proof hold verbatim for any finite coordinate set and any subset \(F\) of it. Throughout \(\alpha=\frac r{r-1}\in(1,2)\), \(\sigma=\sqrt{p(1-p)}\), and \(F_B=\{e\in E_{n,r}:e\cap B\neq\varnothing\}\).

## 1. The block estimate

**Lemma 1.1.** Let \(r+1\le m\le n\), \(B\) uniform among the \(m\)-subsets of \([n]\), and \(k=\frac{\sigma\log m}{64}\). For every hypergraph property \(f\),
\[
\sum_{S\subseteq E_{n,r}}\mathbb P_B\bigl(1\le|S\cap F_B|\le k\bigr)\,\widehat f(S)^2\le m^{-1/4}\,\frac{rm}n\,I_p(f).
\]

**Proof.** Fix \(B\) and an assignment \(y\) of the edges disjoint from \(B\). The permutations supported on \(B\) fix every such edge, so \(f_y\) is invariant under them. An edge with \(j\ge1\) vertices in \(B\) has an orbit of size \(\binom mj\ge m\), since \(1\le j\le r<m\): its part outside \(B\) is fixed and its part inside can be any \(j\)-subset of \(B\). So \(I_e(f_y)\le I(f_y)/m\) on \(F_B\), and Lemma 4.1 of [Biased Fourier analysis and hypercontractivity](biased-fourier-analysis-and-hypercontractivity.md) applies to \(f_y\). Average over \(y\) with Lemma 1.1 of [Vertex blocks and graph properties](vertex-blocks-and-graph-properties.md), and then over \(B\), using \(\mathbb P(e\in F_B)\le rm/n\) by a union bound over the \(r\) vertices of \(e\). \(\square\)

## 2. Capturing a support

**Lemma 2.1.** Let \(1\le m\le n\), \(k>0\), \(L=(k/r)^\alpha\), and suppose \(rL\frac{m-1}{n-1}\le\frac12\). For a uniform \(m\)-subset \(B\) and every \(S\subseteq E_{n,r}\) with \(1\le|S|\le L\),
\[
\mathbb P_B\bigl(1\le|S\cap F_B|\le k\bigr)\ge\frac m{2n}.
\]

**Proof.** Let \(s=|S|\), \(V=\bigcup_{e\in S}e\) and \(v=|V|\). Since \(s\le\binom vr\le v^r\), the average degree is \(\frac{rs}v\le rs^{(r-1)/r}\le rL^{(r-1)/r}=k\); choose \(u\in V\) with \(1\le d_S(u)\le k\). As in Lemma 3.1 of [Vertex blocks and graph properties](vertex-blocks-and-graph-properties.md), \(\mathbb P(B\cap V=\{u\})\ge\frac mn\bigl(1-(v-1)\frac{m-1}{n-1}\bigr)\ge\frac m{2n}\), using \(v\le rs\le rL\). On this event the edges of \(S\) meeting \(B\) are those containing \(u\), so \(|S\cap F_B|=d_S(u)\in[1,k]\). \(\square\)

Combining the two lemmas, whenever both apply,
\[
\sum_{1\le|S|\le L}\widehat f(S)^2\le2r\,m^{-1/4}I_p(f).\tag{2.1}
\]

## 3. The theorem

**Proof of Theorem 3.1.** Choose an integer \(N_r>r\) such that for all \(n\ge N_r\) and \(m=\lfloor\sqrt n\rfloor\):
\[
m\ge r+1,\qquad\log m\ge\tfrac13\log n,\qquad r(\log n)^\alpha n^{-1/2}\le\tfrac12,\qquad m^{-1/4}(\log n)^\alpha\le1;
\]
this is possible because every power of \(\log n\) grows more slowly than every positive power of \(n\). Let \(n\ge N_r\), \(k=\frac{\sigma\log m}{64}\) and \(L=(k/r)^\alpha\). Since \(k/r\le\log n\) and \(\frac{m-1}{n-1}\le n^{-1/2}\), Lemma 2.1 applies, and (2.1) gives
\[
\sum_{1\le|S|\le L}\widehat f(S)^2\le\frac{2r}{(\log n)^\alpha}I_p(f).
\]
By Lemma 2.1 of [Biased Fourier analysis and hypercontractivity](biased-fourier-analysis-and-hypercontractivity.md),
\[
\sum_{|S|>L}\widehat f(S)^2\le\frac1L\sum_S|S|\widehat f(S)^2=\frac{\sigma^2}LI_p(f),\qquad\frac{\sigma^2}L=\frac{(64r)^\alpha\sigma^{2-\alpha}}{(\log m)^\alpha}\le\frac{(192r)^\alpha}{(\log n)^\alpha},
\]
because \(2-\alpha=\frac{r-2}{r-1}>0\) and \(\sigma\le1\). Adding, \(\operatorname{Var}_p(f)\le\frac{2r+(192r)^\alpha}{(\log n)^\alpha}I_p(f)\). For \(r\le n<N_r\), \(\operatorname{Var}_p(f)\le\sigma^2I_p(f)\le\frac14I_p(f)\le\frac{(\log N_r)^\alpha}{4(\log n)^\alpha}I_p(f)\). So \(C_r=\max\{2r+(192r)^\alpha,\frac14(\log N_r)^\alpha\}\) works. \(\square\)

**Proof of Corollary 3.2.** Let \(q(p)=\mathbb E_pf\). By the Margulis–Russo formula (Lemma 2.2 of [Biased Fourier analysis and hypercontractivity](biased-fourier-analysis-and-hypercontractivity.md)), \(q'(p)=I_p(f)\). The complete hypergraph has the property and the empty one does not, so \(0<q(p)<1\) for \(0<p<1\). By Theorem 3.1, \(\frac{d}{dp}\log\frac q{1-q}=\frac{q'}{q(1-q)}\ge\frac{(\log n)^\alpha}{C_r}\), so \(q\) is strictly increasing, the quantiles are unique, and integrating from \(p_\varepsilon\) to \(p_{1-\varepsilon}\) gives \(2\log\frac{1-\varepsilon}\varepsilon\ge\frac{(\log n)^\alpha}{C_r}(p_{1-\varepsilon}-p_\varepsilon)\). \(\square\)

For \(r=2\) the same argument gives exponent \(2\), as in [Vertex blocks and graph properties](vertex-blocks-and-graph-properties.md), where the sharper count \(s<v^2/2\) improves the constants. The bound in Theorem 3.1 holds for every hypergraph property, monotone or not, and at every bias \(p\).

## 4. Exercises

**Exercise 4.1** (easy). Show that the orbit of an edge with \(j\) vertices in \(B\), under the permutations supported on \(B\), has \(\binom mj\) elements, and that \(\binom mj\ge m\) for \(1\le j\le r<m\).

**Exercise 4.2** (easy). Show that an \(r\)-uniform hypergraph with \(s\ge1\) edges has a vertex of degree between \(1\) and \(rs^{(r-1)/r}\).

**Exercise 4.3** (medium). Show that \(\frac{\sigma^2}L\le\frac{(64r)^\alpha}{(\log m)^\alpha}\) for every \(0<p<1\), and explain why the argument would fail as \(p\to0\) if the exponent \(\alpha\) were larger than \(2\).

**Exercise 4.4** (easy). Show that the denominators \((\log n)^\alpha\) and \((\log\binom nr)^\alpha\) are comparable for fixed \(r\): \(\frac12\log n\le\log\binom nr\le r\log n\) for \(n>r\).

## 5. Solutions

**4.1.** A permutation supported on \(B\) maps \(e=e_{\rm in}\cup e_{\rm out}\), \(e_{\rm in}\subseteq B\), to \(\pi(e_{\rm in})\cup e_{\rm out}\), and these permutations act transitively on the \(j\)-subsets of \(B\). For \(1\le j\le m-1\), \(\binom mj\ge\binom m1=m\).

**4.2.** With \(v\) vertices of positive degree, \(s\le\binom vr\le v^r\), so \(v\ge s^{1/r}\), and the average degree \(rs/v\le rs^{1-1/r}\); some vertex has degree at most the average and at least \(1\).

**4.3.** \(\frac{\sigma^2}L=\frac{\sigma^2(64r)^\alpha}{(\sigma\log m)^\alpha}=\frac{(64r)^\alpha\sigma^{2-\alpha}}{(\log m)^\alpha}\), and \(\sigma^{2-\alpha}\le1\) because \(\sigma\le1\) and \(2-\alpha>0\). For \(\alpha>2\) the factor \(\sigma^{2-\alpha}\) would be unbounded as \(p\to0\); for graphs (\(\alpha=2\)) the powers of \(\sigma\) cancel exactly.

**4.4.** \(\binom nr\le n^r\) gives the upper bound. For \(1\le r\le n-1\), \(\binom nr\ge n\), and \(n>\sqrt n\); so \(\log\binom nr\ge\frac12\log n\) (indeed for all \(n>r\)).

## References

- [OpenAI-T2] OpenAI, *A uniform influence bound for hypergraph properties*, OpenAI Math Release preprint, 5 October 2026. https://github.com/openai/math/tree/main/preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026
