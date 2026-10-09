# Biased Fourier analysis and hypercontractivity

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(\mathcal P\) be a property of graphs on the vertex set \([n]=\{1,\dots,n\}\): a set of graphs, closed under relabelling the vertices. Let \(\mu_p(\mathcal P)\) be the probability that the random graph \(G(n,p)\), in which each of the \(\binom n2\) possible edges is present independently with probability \(p\), has the property. If \(\mathcal P\) is *increasing* (adding edges keeps it) and nontrivial, \(\mu_p(\mathcal P)\) increases from \(0\) to \(1\) as \(p\) runs from \(0\) to \(1\), and the *threshold width* \(p_{1-\varepsilon}-p_\varepsilon\) measures how fast, where \(p_a\) is the value of \(p\) at which \(\mu_p=a\). Friedgut and Kalai proved in 1996 that the width is \(O(\log(1/\varepsilon)/\log n)\) for every such property and conjectured the bound \(O(\log(1/\varepsilon)/(\log n)^2)\), which would be optimal [FK]. Bourgain and Kalai came within any power \((\log n)^{\eta}\) of it. OpenAI proved the conjecture in 2026, together with its analogue for \(r\)-uniform hypergraphs with exponent \(r/(r-1)\) [OpenAI-T1, OpenAI-T2].

This course proves both results. The method compares two quantities of a Boolean function \(f\) under the biased product measure: its variance and its *total influence*, the expected number of coordinates whose change changes \(f\). The present lesson develops Fourier analysis for the biased measure, proves a hypercontractive inequality with explicit dependence on the bias (Theorem 3.1), and deduces that a Boolean function all of whose influences are small compared with its total influence has little Fourier mass at low degrees (Lemma 4.1), an estimate in the tradition of Kahn, Kalai and Linial. It also proves the Margulis–Russo formula, which turns influence bounds into threshold widths (Lemma 2.2). The lessons [Vertex blocks and graph properties](vertex-blocks-and-graph-properties.md) and [Hypergraph properties](hypergraph-properties.md) use the symmetry of graph and hypergraph properties.

We use finite probability, Hölder's inequality, and the duality \(\|w\|_2=\sup\{|\mathbb E[vw]|:\|v\|_2=1\}\) in a finite-dimensional inner product space.

## 1. The biased Fourier basis

Let \(J\) be a finite set, \(0<p<1\), \(\sigma=\sqrt{p(1-p)}\le\frac12\), and give \(\{0,1\}^J\) the product measure in which each coordinate is \(1\) with probability \(p\). Write \(\mathbb E\) for expectation and \(\|g\|_q=(\mathbb E|g|^q)^{1/q}\). Put
\[
\chi_i(x)=\frac{x_i-p}\sigma,\qquad\chi_S=\prod_{i\in S}\chi_i,\qquad\chi_\varnothing=1.
\]
Each \(\chi_i\) has mean \(0\) and second moment \(1\), so by independence the \(2^{|J|}\) functions \(\chi_S\) are orthonormal, and they form a basis of the real functions on \(\{0,1\}^J\). With \(\widehat g(S)=\mathbb E[g\chi_S]\),
\[
g=\sum_S\widehat g(S)\chi_S,\qquad\mathbb Eg^2=\sum_S\widehat g(S)^2,\qquad\operatorname{Var}(g)=\sum_{S\neq\varnothing}\widehat g(S)^2.\tag{1.1}
\]
The *degree* of \(\chi_S\) is \(|S|\). For \(i\in J\), let \(\Delta_ig(x)=g(x_{i\leftarrow1})-g(x_{i\leftarrow0})\), where \(x_{i\leftarrow b}\) is \(x\) with coordinate \(i\) set to \(b\); it does not depend on \(x_i\). Integrating coordinate \(i\) alone, \(\mathbb E_i[g\chi_i]=\frac{p(1-p)}\sigma\Delta_ig=\sigma\Delta_ig\), so
\[
\widehat g(A\cup\{i\})=\sigma\,\widehat{\Delta_ig}(A)\qquad(A\subseteq J\setminus\{i\}),\tag{1.2}
\]
the right-hand coefficient being taken on \(J\setminus\{i\}\).

## 2. Influences

For a Boolean function \(h:\{0,1\}^J\to\{0,1\}\), the *influence* of \(i\) is \(I_i(h)=\mathbb P(\Delta_ih\neq0)\), the probability that \(i\) is *pivotal*, and the *total influence* is \(I(h)=\sum_iI_i(h)\).

**Lemma 2.1** (influence and Fourier weights). \(\sum_{S\ni i}\widehat h(S)^2=\sigma^2I_i(h)\) and \(\sum_S|S|\,\widehat h(S)^2=\sigma^2I(h)\). In particular \(\operatorname{Var}(h)\le\sigma^2I(h)\).

**Proof.** By (1.2) and Parseval on \(J\setminus\{i\}\), \(\sum_{S\ni i}\widehat h(S)^2=\sigma^2\mathbb E(\Delta_ih)^2=\sigma^2I_i(h)\), as \(\Delta_ih\in\{-1,0,1\}\). Sum over \(i\); each \(S\) is counted \(|S|\) times. \(\square\)

**Lemma 2.2** (Margulis–Russo). Let \(h\) be increasing (\(h(x)\le h(y)\) when \(x\le y\) coordinatewise) and \(\mu(p)=\mathbb E_ph\). Then \(\mu\) is a polynomial in \(p\) and \(\mu'(p)=I_p(h)\), the total influence under the bias \(p\).

**Proof.** Give each coordinate its own bias \(p_i\). Then \(\mathbb Eh\) is a polynomial, affine in each \(p_i\) separately, and its partial derivative in \(p_i\) is \(\mathbb E\,\Delta_ih\). For increasing \(h\), \(\Delta_ih\in\{0,1\}\), so this is \(I_i(h)\). Differentiate along \(p_i=p\) for all \(i\). \(\square\)

## 3. A biased hypercontractive inequality

For \(0<\rho\le1\), let \(T_\rho\) be the linear operator with \(T_\rho\chi_S=\rho^{|S|}\chi_S\).

**Theorem 3.1** (Bonami–Beckner, biased form). With \(\rho=\sigma/4\), \(\|T_\rho g\|_4\le\|g\|_2\) for every real function \(g\) on \(\{0,1\}^J\).

**Proof.** *One coordinate.* Since \(|\chi_i|\le\max\{p,1-p\}/\sigma\le\sigma^{-1}\) and \(\mathbb E\chi_i^2=1\), \(\mathbb E|\chi_i|^3\le\sigma^{-1}\) and \(\mathbb E\chi_i^4\le\sigma^{-2}\). For real \(a,b\), expanding and using \(\mathbb E\chi_i=0\) and \(2|ab^3|\le a^2b^2+b^4\),
\[
\mathbb E(a+\rho b\chi_i)^4\le a^4+6\rho^2a^2b^2+\frac{4\rho^3}\sigma|ab^3|+\frac{\rho^4}{\sigma^2}b^4\le a^4+\frac{13\sigma^2}{32}a^2b^2+\frac{9\sigma^2}{256}b^4\le(a^2+b^2)^2,
\]
the last step because \(\sigma^2\le\frac14\).

*Tensorization.* Induct on \(|J|\); for \(J=\varnothing\) there is nothing to prove. Pick \(i\in J\) and write \(g=a+b\chi_i\) with \(a,b\) functions of the other coordinates. Then \(T_\rho g=A+\rho B\chi_i\) with \(A=T_\rho a\), \(B=T_\rho b\) (the operator on the other coordinates). Applying the one-coordinate inequality for fixed values of the other coordinates, then the triangle inequality in \(L^2\), then the induction hypothesis,
\[
\|T_\rho g\|_4^2\le\|A^2+B^2\|_2\le\|A\|_4^2+\|B\|_4^2\le\|a\|_2^2+\|b\|_2^2=\|g\|_2^2.\qquad\square
\]

For \(d\ge0\), let \(P_{\le d}\) be the orthogonal projection onto the span of the \(\chi_S\) with \(|S|\le d\).

**Corollary 3.2.** For every real function \(v\), \(\|P_{\le d}v\|_2\le\rho^{-d}\|v\|_{4/3}\), with \(\rho=\sigma/4\).

**Proof.** If \(u=P_{\le d}u\), then \(\|T_\rho^{-1}u\|_2^2=\sum_{|S|\le d}\rho^{-2|S|}\widehat u(S)^2\le\rho^{-2d}\|u\|_2^2\), so by Theorem 3.1 applied to \(T_\rho^{-1}u\), \(\|u\|_4\le\rho^{-d}\|u\|_2\). Hence, by Hölder's inequality,
\[
\|P_{\le d}v\|_2=\sup_{u=P_{\le d}u,\ \|u\|_2=1}|\mathbb E[vu]|\le\sup\|v\|_{4/3}\|u\|_4\le\rho^{-d}\|v\|_{4/3}.\qquad\square
\]

## 4. A low-degree estimate

**Lemma 4.1** (OpenAI). Let \(m\ge2\) be real and \(h:\{0,1\}^J\to\{0,1\}\) with \(I_i(h)\le I(h)/m\) for every \(i\). For \(k=\frac{\sigma\log m}{64}\),
\[
\sum_{1\le|S|\le k}\widehat h(S)^2\le m^{-1/4}I(h).\tag{4.1}
\]

**Proof.** If \(k<1\) the sum is empty. Otherwise, counting every nonempty \(S\) at least once through one of its elements, and using (1.2) and Corollary 3.2 on \(J\setminus\{i\}\) with \(d=k-1\),
\[
\sum_{1\le|S|\le k}\widehat h(S)^2\le\sum_i\sum_{S\ni i,\,|S|\le k}\widehat h(S)^2=\sigma^2\sum_i\|P_{\le k-1}\Delta_ih\|_2^2\le\sigma^2\rho^{-2k}\sum_i\|\Delta_ih\|_{4/3}^2,
\]
and \(\|\Delta_ih\|_{4/3}^2=I_i(h)^{3/2}\) since \(|\Delta_ih|\) is an indicator. Now \(\rho^{-2k}=m^{\sigma\log(4/\sigma)/32}\le m^{1/16}\), because \(s\mapsto s\log(4/s)\) is increasing on \((0,\frac12]\) (its derivative is \(\log(4/s)-1>0\)), so \(\sigma\log(4/\sigma)\le\frac12\log8<2\).

If \(I(h)\le m^{1/4}\), then \(\sum_iI_i(h)^{3/2}\le\max_iI_i(h)^{1/2}\,I(h)\le(I(h)/m)^{1/2}I(h)\le m^{-3/8}I(h)\), and the sum in (4.1) is at most \(\sigma^2m^{1/16-3/8}I(h)\le m^{-1/4}I(h)\). If \(I(h)>m^{1/4}\), the sum is at most \(\mathbb Eh^2\le1<m^{-1/4}I(h)\). \(\square\)

The bound is linear in \(I(h)\); this allows averaging it over random restrictions in the next lesson. The constant \(64\) and the exponent \(\frac14\) are not optimized.

## 5. Exercises

**Exercise 5.1** (easy). Show that the \(\chi_S\) are orthonormal and that \(\mathbb E_i[g\chi_i]=\sigma\Delta_ig\).

**Exercise 5.2** (easy). Compute \(I(h)\) and \(\operatorname{Var}(h)\) for the dictator \(h(x)=x_1\) and for the AND of all coordinates, and check \(\operatorname{Var}(h)\le\sigma^2I(h)\).

**Exercise 5.3** (medium). Check the arithmetic of the one-coordinate inequality in the proof of Theorem 3.1: the coefficients \(\frac{13}{32}\) and \(\frac9{256}\), and the final inequality for \(\sigma^2\le\frac14\).

**Exercise 5.4** (medium). For the majority function on \(n\) (odd) coordinates at \(p=\frac12\), show that each influence is \(I(h)/n\), and compare the bound of Lemma 4.1 with \(m=n\) to the actual weight \(\sum_{|S|=1}\widehat h(S)^2\).

## 6. Solutions

**5.1.** For \(S\neq T\), take \(i\in S\triangle T\); the factor \(\chi_i\) appears once and is independent of the rest, with mean \(0\). \(\mathbb E\chi_S^2=\prod\mathbb E\chi_i^2=1\). For the second identity, \(\mathbb E_i[g\chi_i]=p\,g(x_{i\leftarrow1})\frac{1-p}\sigma+(1-p)\,g(x_{i\leftarrow0})\frac{-p}\sigma\).

**5.2.** Dictator: \(I=1\), \(\operatorname{Var}=p(1-p)=\sigma^2\), equality. AND of \(N\) coordinates: \(I_i=p^{N-1}\), \(I=Np^{N-1}\), \(\operatorname{Var}=p^N(1-p^N)\le Np^{N-1}\cdot p(1-p)\), since \(1-p^N\le N(1-p)\).

**5.3.** \(6\rho^2=\frac{6\sigma^2}{16}=\frac{12\sigma^2}{32}\); \(\frac{4\rho^3}\sigma=\frac{\sigma^2}{16}\), and \(\frac{\sigma^2}{16}|ab^3|\le\frac{\sigma^2}{32}(a^2b^2+b^4)\); \(\frac{\rho^4}{\sigma^2}=\frac{\sigma^2}{256}\). So the coefficients are \(\frac{12+1}{32}\sigma^2\) and \(\frac{1+8}{256}\sigma^2\). With \(\sigma^2\le\frac14\) they are at most \(\frac{13}{128}\le2\) and \(\frac9{1024}\le1\).

**5.4.** By symmetry all influences are equal. At \(p=\frac12\), \(\sigma=\frac12\) and \(\widehat h(\{i\})=\sigma\,\mathbb E\Delta_ih=\frac12I_i(h)\) for increasing \(h\) taking values in \(\{0,1\}\). With \(I_i\approx\sqrt{2/(\pi n)}\), the degree-one weight is \(\frac n4I_i^2\approx\frac1{2\pi}\), a constant, while Lemma 4.1 with \(m=n\) bounds the weight up to degree \(k=\frac{\log n}{128}\) by \(n^{-1/4}I(h)\approx n^{1/4}\): consistent, and far from sharp for this function.

## References

- [FK] E. Friedgut and G. Kalai, *Every monotone graph property has a sharp threshold*, Proc. Amer. Math. Soc. 124 (1996), 2993–3002.
- [OpenAI-T1] OpenAI, *A sharp threshold bound for monotone graph properties*, OpenAI Math Release preprint, 25 September 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026
- [OpenAI-T2] OpenAI, *A uniform influence bound for hypergraph properties*, OpenAI Math Release preprint, 5 October 2026. https://github.com/openai/math/tree/main/preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026
