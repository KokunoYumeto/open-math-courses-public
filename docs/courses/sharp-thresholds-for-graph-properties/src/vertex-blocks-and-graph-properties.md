# Vertex blocks and graph properties

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the two graph theorems of [OpenAI-T1]:

**Theorem 4.1** (OpenAI). For every \(n\ge2\), every \(0<p<1\) and every function \(f:\{0,1\}^{E_n}\to\{0,1\}\) on the edge set \(E_n=\binom{[n]}2\) that is invariant under the permutations of the vertices,
\[
\operatorname{Var}_p(f)\le\frac{2^{17}}{(\log n)^2}\,I_p(f).
\]

**Theorem 5.1** (OpenAI; the Friedgut–Kalai conjecture). For every nontrivial increasing graph property \(\mathcal P\) on \(n\ge2\) vertices and every \(0<\varepsilon<\frac12\),
\[
p_{1-\varepsilon}(\mathcal P)-p_\varepsilon(\mathcal P)\le\frac{2^{19}}{(\log n)^2}\log\frac1{2\varepsilon}.
\]

Here \(\log\) is the natural logarithm, \(p_a=\inf\{p:\mu_p(\mathcal P)\ge a\}\), and variance and influences are taken under the bias \(p\), as in [Biased Fourier analysis and hypercontractivity](biased-fourier-analysis-and-hypercontractivity.md). The idea is to restrict \(f\) to the edges that touch a random block \(B\) of about \(\sqrt n\) vertices, fixing all other edges. Every permutation of \(B\) fixes each of the fixed edges, so the restricted function is still symmetric under the permutations of \(B\), and all its influences are small compared with its total influence; Lemma 4.1 of the preceding lesson then bounds its low-degree Fourier mass (Proposition 2.1). A Fourier coefficient \(\widehat f(S)\) is indexed by a set \(S\) of edges, that is, by a graph; a graph with \(s\) edges has a vertex of degree between \(1\) and \(\sqrt{2s}\), and with probability about \(|B|/n\) the block meets the vertices of \(S\) only there. So restricted degrees up to \(k\) control original degrees up to \(k^2/2\) (Lemma 3.1), and \(k\) of order \(\log n\) gives the factor \((\log n)^2\).

We use Lemmas 2.1, 2.2 and 4.1 and the notation of [Biased Fourier analysis and hypercontractivity](biased-fourier-analysis-and-hypercontractivity.md), with \(J=E_n\). Monotonicity is needed only for Theorem 5.1.

## 1. Restrictions

**Lemma 1.1** (averaging over a restriction). Let \(F\subseteq E_n\), \(H=E_n\setminus F\), and for \(y\in\{0,1\}^H\) let \(f_y(x)=f(x,y)\) on \(\{0,1\}^F\). If \(y\) has the product law, then for every \(k>0\)
\[
\mathbb E_y\sum_{A\subseteq F,\ 1\le|A|\le k}\widehat{f_y}(A)^2=\sum_{S\subseteq E_n,\ 1\le|S\cap F|\le k}\widehat f(S)^2,\qquad\mathbb E_yI(f_y)=\sum_{e\in F}I_e(f).
\]

**Proof.** Integrating the expansion of \(f\) over \(x\) against \(\chi_A\) gives \(\widehat{f_y}(A)=\sum_{D\subseteq H}\widehat f(A\cup D)\chi_D(y)\), and orthonormality in \(y\) gives \(\mathbb E_y\widehat{f_y}(A)^2=\sum_D\widehat f(A\cup D)^2\); sum over \(A\). For \(e\in F\), the pivotal event of \(f_y\) at \(e\) is that of \(f\) with the coordinates in \(H\) fixed to \(y\), so \(\mathbb E_yI_e(f_y)=I_e(f)\). \(\square\)

## 2. A random vertex block

From now on \(f\) is invariant under vertex permutations. For \(B\subseteq[n]\), let \(F_B=\{e\in E_n:e\cap B\neq\varnothing\}\).

**Proposition 2.1** (the block estimate). Let \(3\le m\le n\), \(B\) uniform among the \(m\)-element subsets of \([n]\), and \(k=\frac{\sigma\log m}{64}\). Then
\[
\sum_{S\subseteq E_n}\mathbb P_B\bigl(1\le|S\cap F_B|\le k\bigr)\,\widehat f(S)^2\le\frac{2m}n\,m^{-1/4}I(f).
\]

**Proof.** Fix \(B\) and \(y\in\{0,1\}^{E_n\setminus F_B}\). A permutation of \([n]\) supported on \(B\) fixes every edge disjoint from \(B\), hence fixes \(y\), so \(f_y\) is invariant under all such permutations; the product measure is invariant too, so influences of \(f_y\) are constant on orbits. The orbits on \(F_B\) are the \(\binom m2\) edges inside \(B\), and for each \(w\notin B\) the \(m\) edges \(\{u,w\}\), \(u\in B\); all have at least \(m\) elements since \(m\ge3\). Hence \(I_e(f_y)\le I(f_y)/m\) for \(e\in F_B\), and Lemma 4.1 of [Biased Fourier analysis and hypercontractivity](biased-fourier-analysis-and-hypercontractivity.md) gives \(\sum_{1\le|A|\le k}\widehat{f_y}(A)^2\le m^{-1/4}I(f_y)\). Averaging over \(y\) with Lemma 1.1,
\[
\sum_{1\le|S\cap F_B|\le k}\widehat f(S)^2\le m^{-1/4}\sum_{e\in F_B}I_e(f).
\]
Average over \(B\): each endpoint of an edge lies in \(B\) with probability \(m/n\), so \(\mathbb P(e\in F_B)\le2m/n\). \(\square\)

## 3. Capturing a support at one vertex

**Lemma 3.1.** Let \(t=\log n\ge16\), \(m=\lfloor\sqrt n\rfloor\) and \(k=\frac{\sigma\log m}{64}\). Then
\[
\sum_{1\le|S|\le k^2/2}\widehat f(S)^2\le4m^{-1/4}I(f).
\]

**Proof.** If \(k^2/2<1\), the sum is empty. Fix \(S\) with \(1\le s=|S|\le k^2/2\), regarded as a graph; let \(V\) be the set of vertices it touches, \(v=|V|\). Since \(s\le\binom v2<v^2/2\), the average degree on \(V\) is \(2s/v<\sqrt{2s}\le k\); choose \(u\in V\) of degree \(d_S(u)\le2s/v\), so \(1\le d_S(u)\le k\), and note \(v\le2s\le k^2\). For uniform \(B\), \(\mathbb P(u\in B)=m/n\), and given \(u\in B\) each other vertex lies in \(B\) with probability \(\frac{m-1}{n-1}\); so
\[
\mathbb P\bigl(B\cap V=\{u\}\bigr)\ge\frac mn\Bigl(1-(v-1)\frac{m-1}{n-1}\Bigr).
\]
On this event \(S\cap F_B\) consists of the \(d_S(u)\) edges of \(S\) at \(u\), so \(1\le|S\cap F_B|\le k\). Now \(k\le t\), \(\frac{m-1}{n-1}\le\frac1{\sqrt n+1}\le n^{-1/2}\), and \((v-1)n^{-1/2}\le t^2e^{-t/2}\le256e^{-8}<\frac12\), since \(t^2e^{-t/2}\) decreases for \(t\ge4\). Hence \(\mathbb P_B(1\le|S\cap F_B|\le k)\ge\frac m{2n}\) for each such \(S\). Inserting this in Proposition 2.1 (the vertex \(u\) may depend on \(S\), as the probability bound is used for each nonnegative term separately) gives the claim. \(\square\)

## 4. The variance bound

**Proof of Theorem 4.1.** If \(n<e^{16}\), Lemma 2.1 of [Biased Fourier analysis and hypercontractivity](biased-fourier-analysis-and-hypercontractivity.md) gives \(\operatorname{Var}(f)\le\sigma^2I(f)\le\frac14I(f)\le\frac{64}{(\log n)^2}I(f)\). Let \(t=\log n\ge16\), with \(m\) and \(k\) as in Lemma 3.1. By the same Lemma 2.1,
\[
\sum_{|S|>k^2/2}\widehat f(S)^2\le\frac2{k^2}\sum_S|S|\widehat f(S)^2=\frac{2\sigma^2}{k^2}I(f),
\]
so with Lemma 3.1 and (1.1) of that lesson, \(\operatorname{Var}(f)\le\bigl(4m^{-1/4}+\frac{2\sigma^2}{k^2}\bigr)I(f)\). The bias cancels: \(\frac{2\sigma^2}{k^2}=\frac{8192}{(\log m)^2}\). Since \(m\ge\sqrt n-1\ge\sqrt n/2\), \(\log m\ge\frac t2-\log2\ge\frac t3\), so \(\frac{2\sigma^2}{k^2}\le\frac{73728}{t^2}\). Also \(4m^{-1/4}\le4\cdot2^{1/4}e^{-t/8}\), and \(t^2e^{-t/8}\) decreases for \(t\ge16\), so \(4m^{-1/4}t^2\le4\cdot2^{1/4}\cdot256e^{-2}<256\). Altogether \(\operatorname{Var}(f)\le\frac{73728+256}{t^2}I(f)\le\frac{2^{17}}{t^2}I(f)\). \(\square\)

No monotonicity was used, and the bound holds uniformly in \(p\), including \(p\) close to \(0\) or \(1\).

## 5. Threshold widths

**Proof of Theorem 5.1.** Let \(f=\mathbf 1_{\mathcal P}\) and \(\mu(p)=\mathbb E_pf\). By Lemma 2.2 of [Biased Fourier analysis and hypercontractivity](biased-fourier-analysis-and-hypercontractivity.md), \(\mu'(p)=I_p(f)\), and \(\operatorname{Var}_p(f)=\mu(1-\mu)\) since \(f\) is Boolean. Theorem 4.1 gives, with \(C_0=2^{17}\),
\[
\mu'(p)\ge\frac{(\log n)^2}{C_0}\,\mu(p)\bigl(1-\mu(p)\bigr)\qquad(0<p<1).
\]
As \(\mathcal P\) is increasing and nontrivial, it contains the complete graph and not the empty graph, so \(0<\mu(p)<1\) for \(0<p<1\), with \(\mu(0)=0\) and \(\mu(1)=1\); so \(\mu\) is strictly increasing and each \(p_a\) is the unique solution of \(\mu(p_a)=a\). Dividing,
\[
\frac d{dp}\log\frac{\mu}{1-\mu}=\frac{\mu'}{\mu(1-\mu)}\ge\frac{(\log n)^2}{C_0},
\]
and integrating over \([p_\varepsilon,p_{1-\varepsilon}]\), \(p_{1-\varepsilon}-p_\varepsilon\le\frac{C_0}{(\log n)^2}\cdot2\log\frac{1-\varepsilon}\varepsilon\). Finally \(\frac{1-\varepsilon}\varepsilon\le\frac1{4\varepsilon^2}\), because \(4\varepsilon(1-\varepsilon)\le1\), so \(\log\frac{1-\varepsilon}\varepsilon\le2\log\frac1{2\varepsilon}\), and \(4C_0=2^{19}\). \(\square\)

Integrating from the median \(p_*=p_{1/2}\) instead gives \(\mu(p_*-s)\le\bigl(1+e^{s(\log n)^2/C_0}\bigr)^{-1}\) and the same bound for \(1-\mu(p_*+s)\). Friedgut and Kalai pointed out that containing a clique whose order is proportional to \(\log n\) can have a transition of width of order \((\log n)^{-2}\), so for fixed \(\varepsilon\) the exponent \(2\) cannot be improved; this example is not treated here.

## 6. Exercises

**Exercise 6.1** (easy). Describe the orbits of the permutations supported on \(B\) acting on \(F_B\), and show that each has at least \(m\) elements when \(m\ge3\).

**Exercise 6.2** (easy). Show that a graph with \(s\ge1\) edges has a vertex of degree between \(1\) and \(\sqrt{2s}\).

**Exercise 6.3** (easy). Show that symmetry is essential in Theorem 4.1: for \(f(x)=x_e\) (one fixed edge), compute \(\operatorname{Var}_p(f)\) and \(I_p(f)\), and the threshold width of the property "the edge \(e\) is present", which is not a graph property.

**Exercise 6.4** (medium). Show that \(\mathbb P\bigl(B\cap V=\{u\}\bigr)\ge\frac mn\bigl(1-(v-1)\frac{m-1}{n-1}\bigr)\).

## 7. Solutions

**6.1.** The edges inside \(B\) form one orbit of size \(\binom m2\ge m\) for \(m\ge3\); for \(w\notin B\), the edges \(\{u,w\}\) with \(u\in B\) form one orbit of size \(m\), since the permutations of \(B\) act transitively on \(B\) and fix \(w\).

**6.2.** Let \(V\) be the set of vertices of positive degree, \(v=|V|\). Then \(s\le\binom v2<v^2/2\), and the average degree \(2s/v\) is less than \(\sqrt{2s}\); some vertex of \(V\) has degree at most the average and at least \(1\).

**6.3.** \(\operatorname{Var}_p=p(1-p)\) and \(I_p=1\), so the ratio is \(\sigma^2\), not small. \(\mu_p=p\), so \(p_{1-\varepsilon}-p_\varepsilon=1-2\varepsilon\).

**6.4.** \(\mathbb P(B\cap V=\{u\})=\mathbb P(u\in B)\,\mathbb P(\text{no other vertex of }V\text{ in }B\mid u\in B)\), and by the union bound the last probability is at least \(1-(v-1)\frac{m-1}{n-1}\).

## References

- [OpenAI-T1] OpenAI, *A sharp threshold bound for monotone graph properties*, OpenAI Math Release preprint, 25 September 2026, Sections 3 and 4. https://github.com/openai/math/tree/main/preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026
