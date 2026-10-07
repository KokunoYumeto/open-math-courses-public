# A finite regular measure from positive function covers

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Original exposition and embedded diagram: public domain (CC0).*

Let \(K\) be a compact metric space and let \(I:C(K,\mathbb R)\to\mathbb R\) be positive and real linear. We construct the unique finite regular Borel measure representing \(I\). The starting point is a countable cover by nonnegative continuous functions: its cost is the sum of their functional values. Metric separation makes the resulting outer measure additive on separated sets. Compactness then recovers the functional from the measure.

This is a local construction in the classical Daniell–Stone viewpoint. An authorized free primary treatment of positive functionals and their representing measures is D. H. Fremlin, [*Measure Theory*, Chapter 43, 436A–D, 436H–K and Exercise 436X(c), author-supplied TeX](https://www1.essex.ac.uk/maths/people/fremlin/chap43.tex). Fremlin proves broader representation results for truncated Riesz spaces and locally compact Hausdorff spaces; Exercise 436X(c) also formulates an outer-measure construction from increasing continuous approximants. The construction below gives a complete positive-cover outer measure, metric measurability argument, compact-metric regularity proof and integral comparison. Its mathematical inputs are the complete [scalar integration proofs, Sections 0–2](../../OA-MOD/notes/analytic-programme/scalar-integration-programme.html), the elementary compact-metric facts [SS2](../../OA-MOD/notes/analytic-programme/spectral-scalar-prerequisites.html#ss2-the-topology-needed-on-a-compact-metric-space), the complete ordered real field and choice. No representation theorem is an input.

<a id="rm01"></a>
## RM01. The outer measure and its total mass

If \(K\) is empty, its function space, functional and measure are zero. Henceforth \(K\ne\varnothing\). Put \(M=I(1)\). Positivity gives \(M\ge0\), monotonicity and
\[
 |I(f)|\le M\|f\|_\infty\qquad(f\in C(K,\mathbb R)).
 \tag{RM1}
\]
Indeed \(-\|f\|_\infty1\le f\le\|f\|_\infty1\). In particular no boundedness hypothesis on \(I\) has been added.

For any \(A\subset K\), define
\[
 \mu^*(A)=\inf\left\{\sum_{j=1}^{\infty}I(f_j):
 f_j\in C(K,\mathbb R),\ f_j\ge0,
 \sum_{j=1}^{\infty}f_j(x)\ge1\text{ for }x\in A\right\}.
 \tag{RM2}
\]
Each nonnegative sum is the supremum of its finite partial sums. Finite covers are included by adjoining zeros. The constant function one gives a cover of every set, so \(0\le\mu^*(A)\le M<\infty\). The zero sequence covers the empty set. Enlarging a set restricts its admissible covers, proving monotonicity.

To prove countable subadditivity, consider \(A_j\subset K\). If \(\sum_j\mu^*(A_j)=\infty\), the desired inequality is immediate. Otherwise, for \(\varepsilon>0\), choose a function cover for each \(A_j\) of cost less than \(\mu^*(A_j)+\varepsilon2^{-j}\). Enumerate all its functions by a single sequence, using diagonal enumeration of pairs of positive integers. The resulting sequence covers \(\bigcup_jA_j\); its total cost is the sum of the individual costs, by equality of the suprema over finite subsums of nonnegative numbers. Hence
\[
 \mu^*\left(\bigcup_jA_j\right)
 \le\sum_j\mu^*(A_j)+\varepsilon.
\]
Let \(\varepsilon\downarrow0\). Thus \(\mu^*\) is an outer measure.

Its total mass is exactly \(M\). Given a function cover \((f_j)\) of \(K\) and \(0<\varepsilon<1\), the increasing open sets
\(\{x:\sum_{j\le n}f_j(x)>1-\varepsilon\}\) cover \(K\). Compactness gives one index \(n\) for which that partial sum exceeds \(1-\varepsilon\) everywhere. Positivity and linearity imply
\[
 \sum_jI(f_j)\ge\sum_{j\le n}I(f_j)\ge(1-\varepsilon)M.
\]
Let \(\varepsilon\downarrow0\) and take the infimum over covers. The opposite bound was given by the constant cover, so
\[
 \mu^*(K)=M.
 \tag{RM3}
\]
This proof also applies when \(M=0\).

<a id="rm02"></a>
## RM02. Metric separation makes every Borel set measurable

If nonempty sets \(A,B\subset K\) have distance \(\delta>0\), their distance functions are continuous and
\(d(x,A)+d(x,B)\ge\delta\). Consequently
\[
 h(x)=\frac{d(x,B)}{d(x,A)+d(x,B)}
\]
is continuous, lies in \([0,1]\), is one on \(A\), and is zero on \(B\). Any function cover \((f_j)\) of \(A\cup B\) splits into covers \((hf_j)\) of \(A\) and \(((1-h)f_j)\) of \(B\). Linearity and nonnegative sums give
\[
 \mu^*(A)+\mu^*(B)\le\sum_jI(f_j).
\]
Take the infimum over covers and use subadditivity for the reverse inequality. Empty sets cause no change. We have proved
\[
 \mu^*(A\cup B)=\mu^*(A)+\mu^*(B)
 \quad\text{if }d(A,B)>0.
 \tag{RM4}
\]

Here is the complete Borel-measurability argument, including the limiting step for an outer measure. Let \(F\subset K\) be closed; the empty case is immediate. For an arbitrary \(A\subset K\), set
\[
 A_n=\{x\in A:d(x,F)\ge1/n\},\qquad
 C_k=\{x\in A:1/(k+1)\le d(x,F)<1/k\}.
\]
Any finite collection of the \(C_k\) with indices of one parity consists of mutually separated sets. For indices differing by at least two, the distance-value ranges have a positive gap; the distance function is 1-Lipschitz, so this also separates the sets themselves. Taking a minimum over the finitely many gaps lets (RM4) be applied repeatedly to their union. Therefore each parity's finite sum of outer measures is at most \(\mu^*(K)=M\), and
\[
 \sum_{k\ge1}\mu^*(C_k)\le2M.
\]
The tails of this nonnegative scalar series tend to zero by real completeness. Also
\[
 A\setminus F\subset A_n\cup\bigcup_{k\ge n}C_k,
 \qquad
 \mu^*(A)\ge\mu^*(A\cap F)+\mu^*(A_n),
\]
where the second inequality uses the separation of \(F\) from \(A_n\). Subadditivity now gives
\[
 \mu^*(A\cap F)+\mu^*(A\setminus F)
 \le\mu^*(A)+\sum_{k\ge n}\mu^*(C_k).
\]
Let \(n\to\infty\). The reverse inequality is subadditivity, so \(F\) satisfies the Carathéodory condition. The complete Carathéodory proof in scalar integration, Section 1, says that the measurable sets form a sigma-algebra and that the outer measure restricts to a measure there. This sigma-algebra contains the closed sets, hence all Borel sets. Write
\[
 \mu=\mu^*|_{\mathcal B(K)}.
 \tag{RM5}
\]
It is a finite Borel measure with mass \(M\). In particular, the preceding argument has not assumed continuity from below for arbitrary outer-measurable subsets before proving their measurability.

<a id="rm03"></a>
## RM03. Regularity on every Borel set

A finite Borel measure on this compact metric space has both required approximations. If \(F\) is closed, the open sets \(U_n=\{d(x,F)<1/n\}\) decrease to \(F\); continuity from above gives \(\mu(U_n\setminus F)\to0\). For \(F=\varnothing\), use the empty open set. If \(U\) is open with nonempty complement, the closed sets
\(F_n=\{d(x,K\setminus U)\ge1/n\}\) increase to \(U\), so continuity from below gives \(\mu(U\setminus F_n)\to0\). For \(U=K\), use \(F_n=K\). All the closed sets are compact.

To include every Borel set, let \(\mathcal R\) consist of the Borel sets \(E\) such that for every \(\varepsilon>0\) there are closed \(F\) and open \(U\) with
\(F\subset E\subset U\) and \(\mu(U\setminus F)<\varepsilon\). It contains closed sets by the preceding paragraph and is closed under complements: replace \(F,U\) by \(K\setminus U,K\setminus F\).

For \(E=\bigcup_jE_j\) with \(E_j\in\mathcal R\), choose \(F_j\subset E_j\subset U_j\) with \(\mu(U_j\setminus F_j)<\varepsilon2^{-j}/4\), and put \(U=\bigcup_jU_j\). Then \(\mu(U\setminus E)<\varepsilon/4\). Since \(\mu(E)\le M<\infty\), continuity from below supplies \(N\) with
\(\mu(E\setminus\bigcup_{j\le N}E_j)<\varepsilon/4\). The compact set \(F=\bigcup_{j\le N}F_j\subset E\) then has \(\mu(E\setminus F)<\varepsilon/2\). Combining the two errors gives \(\mu(U\setminus F)<\varepsilon\). Thus \(\mathcal R\) is a sigma-algebra containing the closed sets, and contains every Borel set. We have proved
\[
 \mu(E)=\inf_{U\supset E\text{ open}}\mu(U)
       =\sup_{F\subset E\text{ compact}}\mu(F)
 \qquad(E\in\mathcal B(K)).
 \tag{RM6}
\]
Finiteness is used in the continuity-from-above and finite-union approximation steps. This argument asserts full Borel regularity on compact metric \(K\); it makes no stronger regularity assertion on an arbitrary noncompact space.

<a id="rm04"></a>
## RM04. Recovering the functional

For a closed \(F\subset K\), the cover definition gives the exact compact-majorant identity
\[
 \mu(F)=\inf\{I(g):g\in C(K,\mathbb R),\ g\ge0,\ g\ge1_F\}.
 \tag{RM7}
\]
The measure is at most each displayed cost, since one function is an admissible cover. Conversely, for any function cover \((f_j)\) of \(F\) and \(0<\varepsilon<1\), compactness of \(F\) supplies a finite partial sum at least \(1-\varepsilon\) on \(F\). Dividing it by \(1-\varepsilon\) gives a displayed majorant of cost at most \((1-\varepsilon)^{-1}\sum_jI(f_j)\). Take the infimum over covers and let \(\varepsilon\downarrow0\). This proves (RM7), including \(F=\varnothing\). Clipping a majorant to \([0,1]\) preserves its value one on \(F\) and only decreases its functional value. Thus, for \(U=K\setminus F\), (RM3) and (RM7) give
\[
 \mu(U)=\sup\{I(h):h\in C(K,\mathbb R),\ 0\le h\le1,\ h|_F=0\}.
 \tag{RM8}
\]

If a continuous \(r\ge0\) has zero set \(F\), put \(h_k=\min(1,kr)\). These functions increase, lie in the set in (RM8), and
\[
 I(h_k)\longrightarrow\mu(U).
 \tag{RM9}
\]
Indeed, for any \(h\) in that set and \(\eta>0\), the compact set \(\{h\ge\eta\}\) lies in \(U\). On a nonempty such set, \(r\) has a positive minimum, so eventually \(h_k=1\) there. Elsewhere \(h<\eta\); hence \(h\le h_k+\eta\) everywhere. Positivity gives \(I(h)\le I(h_k)+\eta M\). Take the supremum over \(h\), then let \(\eta\downarrow0\), to prove (RM9). For the empty compact set the same bound is immediate. If \(F=\varnothing\), positivity of the minimum of \(r\) makes \(h_k=1\) eventually; if \(F=K\), all functions are zero.

Now fix continuous \(0\le f\le1\). For \(n\ge1\), define the Borel simple function and continuous approximants
\[
 s_n=\frac1n\sum_{j=1}^{n}1_{\{f>j/n\}},\qquad
 H_{n,k}=\frac1n\sum_{j=1}^{n}\min\bigl(1,k(f-j/n)_+\bigr).
 \tag{RM10}
\]
At every point, including exact subdivision endpoints,
\(0\le H_{n,k}\le s_n\le f\) and \(0\le f-s_n\le1/n\). Apply (RM9) to each continuous function \((f-j/n)_+\), keeping \(n\) fixed. Finite linearity and the simple-integral formula give
\[
 \int s_n\,d\mu
 =\frac1n\sum_{j=1}^{n}\mu(\{f>j/n\})
 =\lim_{k\to\infty}I(H_{n,k})\le I(f).
\]
Since \(\mu(K)=M\), the uniform bound on \(f-s_n\) implies
\(\int f\,d\mu\le I(f)+M/n\). Let \(n\to\infty\). Applying this same inequality to \(1-f\), and using \(\int1\,d\mu=I(1)=M\), gives the reverse inequality. Thus
\[
 I(f)=\int_K f\,d\mu.
 \tag{RM11}
\]
Scaling treats every continuous nonnegative function, because it is bounded on \(K\). Positive and negative parts treat every real continuous function. For complex continuous \(f=u+iv\), the complexification \(I_{\mathbb C}(f)=I(u)+iI(v)\) is consequently its complex integral.

### An exact two-point example

Take \(K=\{0,1\}\), with distance one, and \(I(f)=f(0)/3+2f(1)/3\). The separator in (RM4) has \(h(0)=1,h(1)=0\), splitting every function cover into its two costs. Thus \(\mu(\{0\})=1/3\), \(\mu(\{1\})=2/3\) and \(M=1\). For \(f(0)=1/4,f(1)=3/4\), the strict lower step in (RM10) at \(n=4\) has \(s_4(0)=0,s_4(1)=1/2\). Consequently \(\int f=7/12\), \(\int s_4=1/3\), and their difference is exactly \(M/n=1/4\). The following diagram shows this example, including the strict-endpoint convention; it does not assert that a general representing measure is atomic.

<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="620" viewBox="0 0 1080 620" role="img" aria-labelledby="title desc">
<title id="title">Positive function covers on two points</title>
<desc id="desc">For K equals zero and one, separated by distance one, weights are one third and two thirds. A continuous separator splits cover costs. The lower step s4 of f with values one quarter and three quarters has values zero and one half. The weighted integral difference is exactly one quarter.</desc>
<rect width="1080" height="620" rx="18" fill="#f7f9fc"/>
<g font-family="Arial, sans-serif" fill="#152b44">
<text x="38" y="44" font-size="25" font-weight="bold">A cover splits; lower steps recover its functional</text>
<text x="38" y="76" font-size="18">Exact example: K = {0, 1}, d(0, 1) = 1, I(f) = f(0)/3 + 2f(1)/3</text>
<rect x="28" y="100" width="450" height="390" rx="12" fill="white" stroke="#ccd6e2"/>
<text x="52" y="134" font-size="21" font-weight="bold">RM4 · metric separation</text>
<line x1="126" y1="216" x2="377" y2="216" stroke="#62778e" stroke-width="2"/>
<circle cx="126" cy="216" r="12" fill="#217bb8"/>
<circle cx="377" cy="216" r="12" fill="#d18522"/>
<text x="98" y="187" font-size="18">x = 0</text>
<text x="348" y="187" font-size="18">x = 1</text>
<text x="234" y="202" font-size="18">d = 1</text>
<text x="91" y="257" font-size="18">h = 1</text>
<text x="344" y="257" font-size="18">h = 0</text>
<text x="72" y="291" font-size="18">μ({0}) = 1/3</text>
<text x="313" y="291" font-size="18">μ({1}) = 2/3</text>
<text x="52" y="340" font-size="19">For every nonnegative cover (f_j):</text>
<text x="52" y="373" font-size="19">Σ I(f_j) = Σ I(hf_j) + Σ I((1−h)f_j)</text>
<text x="52" y="420" font-size="18">The two sets have separate cover costs.</text>
<text x="52" y="451" font-size="18">Their outer measures therefore add.</text>
<rect x="496" y="100" width="556" height="390" rx="12" fill="white" stroke="#ccd6e2"/>
<text x="520" y="134" font-size="21" font-weight="bold">RM10 · strict lower steps, n = 4</text>
<g stroke="#e1e7ef" stroke-width="1">
<line x1="566" y1="365" x2="1005" y2="365"/><line x1="566" y1="316" x2="1005" y2="316"/>
<line x1="566" y1="267" x2="1005" y2="267"/><line x1="566" y1="218" x2="1005" y2="218"/>
<line x1="566" y1="169" x2="1005" y2="169"/>
</g>
<g font-size="16" text-anchor="end"><text x="554" y="371">0</text><text x="554" y="322">1/4</text><text x="554" y="273">1/2</text><text x="554" y="224">3/4</text><text x="554" y="175">1</text></g>
<g stroke="#62778e" stroke-width="2"><line x1="566" y1="163" x2="566" y2="365"/><line x1="566" y1="365" x2="1005" y2="365"/></g>
<rect x="652" y="316" width="45" height="49" fill="#217bb8"/>
<rect x="873" y="218" width="45" height="147" fill="#217bb8"/>
<rect x="932" y="267" width="45" height="98" fill="#d18522"/>
<line x1="711" y1="365" x2="756" y2="365" stroke="#d18522" stroke-width="6"/>
<g font-size="16" text-anchor="middle"><text x="674" y="304">1/4</text><text x="734" y="348">0</text><text x="895" y="206">3/4</text><text x="954" y="255">1/2</text></g>
<text x="704" y="398" text-anchor="middle" font-size="18">x = 0</text><text x="924" y="398" text-anchor="middle" font-size="18">x = 1</text>
<rect x="584" y="426" width="16" height="16" fill="#217bb8"/><text x="610" y="440" font-size="17">f</text>
<rect x="666" y="426" width="16" height="16" fill="#d18522"/><text x="692" y="440" font-size="17">s₄ = (1/4) Σⱼ₌₁⁴ 1{f &gt; j/4}</text>
<text x="38" y="536" font-size="22" font-weight="bold">∫ f dμ = 7/12,     ∫ s₄ dμ = 1/3,     ∫(f − s₄) dμ = 1/4 = M/n</text>
<text x="38" y="576" font-size="18">Equality is possible at subdivision endpoints. RM10–RM11 prove the bound for every compact metric K.</text>
</g></svg>


<a id="rm05"></a>
## RM05. Uniqueness and the exact supplied contract

Let \(\nu\) be another finite regular Borel measure representing \(I\). For a nonempty closed \(F\subset K\), the continuous functions
\(g_n=(1-nd(x,F))_+\) lie between zero and one and converge pointwise to \(1_F\). Scalar dominated convergence, with the constant majorant one integrable for both finite measures, gives
\[
 \nu(F)=\lim_n I(g_n)=\mu(F).
\]
The empty set agrees as well. Both total masses equal \(I(1)\), so complements give agreement on open sets. Outer regularity then gives agreement on every Borel set. This proves uniqueness.

The supplied theorem is exactly: every positive real-linear functional on \(C(K,\mathbb R)\), for every compact metric space \(K\), has a unique finite Borel measure representing it, outer regular and compact-inner-regular on every Borel set, with total mass \(I(1)\); complexification gives the complex integral identity. There is no countability condition on an ambient operator Hilbert space. Scalar \(L^2\) completeness on arbitrary, possibly non-sigma-finite or noncomplete measure spaces is supplied separately by SS1 and its stated measurable-representative convention. The construction here does not replace the general locally compact Hausdorff theorem.
