# The fundamental theorem for an integrable derivative

*Written and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, 4 October 2026. Original exposition is CC0. Independent review remains separate.*

Suppose that \(F:[a,b]\to\mathbb C\) is continuous, differentiable at every point of \((a,b)\), and that \(F'\) is Lebesgue integrable. We will prove
\[
 F(b)-F(a)=\int_a^b F'(x)\,dx.
 \tag{FT0.1}
\]
The derivative need not be continuous or bounded. Differentiability merely almost everywhere would not suffice, as the last example shows.

Our measure prerequisites are the written proofs in [Scalar measure and integration](scalar-integration-programme.md): its Section 0 proves compact-interval compactness and extrema; Section 1 constructs Lebesgue measure from open interval covers; Section 2 constructs scalar integrals and proves monotone and dominated convergence. We prove the approximation and comparison steps needed here rather than assume a general differentiation theorem for integrals. All intervals below are finite unless stated otherwise, and integrals ignore endpoint values.

## FT1. Small sets and open supersets

**Small-set bound.** If \(h\) is integrable on \(I=[a,b]\), then for each \(\varepsilon>0\) there is \(\delta>0\) such that
\[
 m(E)<\delta\quad\Longrightarrow\quad
 \int_E|h|<\varepsilon
 \tag{FT1.1}
\]
for every measurable \(E\subseteq I\).

*Proof.* By dominated convergence, \(\int_I |h|1_{\{|h|>M\}}\to0\) as \(M\to\infty\). Choose \(M>0\) making this integral less than \(\varepsilon/2\), and choose \(\delta=\varepsilon/(2M)\). Splitting \(E\) according to whether \(|h|\leq M\) gives
\(\int_E|h|\leq M m(E)+\int_I|h|1_{\{|h|>M\}}<\varepsilon\).
\(\square\)

Consequently \(H(x)=\int_a^x h(t)\,dt\) is continuous on \(I\), since
\( |H(y)-H(x)|\leq\int_{[x,y]}|h|\) for \(x\leq y\). This conclusion uses no assertion about the derivative of \(H\).

**Open approximation.** If \(E\subseteq I\) is Lebesgue measurable and \(\eta>0\), there is an open set \(O\subseteq\mathbb R\) containing every point of \(E\) such that \(m(O\setminus E)<\eta\).

*Proof.* The interval-cover definition of Lebesgue outer measure supplies countably many open intervals covering \(E\), whose total length is less than \(m(E)+\eta\). Their union \(O\) is open and has measure at most that sum, by countable subadditivity and the interval-length formula. Since \(E\) is measurable and has finite measure, \(m(O\setminus E)=m(O)-m(E)<\eta\). The same argument works for the completion of Borel measure because a Lebesgue-measurable set has its outer measure as its measure. \(\square\)

## FT2. A pointwise lower-semicontinuous majorant

A function \(g:I\to(-\infty,\infty]\) is lower semicontinuous if \(\{x:g(x)>c\}\) is relatively open for every real \(c\). Such a function is measurable. Values \(+\infty\) are allowed on a null set; an integrable such function means that its almost-everywhere finite representative is integrable.

**Lemma.** For every finite-valued integrable real function \(f\) on \(I=[a,b]\), \(a<b\), and every \(\varepsilon>0\), there is a lower-semicontinuous function \(g\), bounded below, such that
\[
 g(x)\geq f(x)\quad(x\in I),\qquad
 \int_I|g|<\infty,\qquad
 \int_I g<\int_I f+\varepsilon.
 \tag{FT2.1}
\]
The first inequality is pointwise, including on every null exceptional set of \(f\).

*Proof for \(f=h\geq0\).* Choose \(d>0\) so small that \(d(b-a)<\varepsilon/2\). For each integer \(k\geq0\), let
\[
 E_k=\{x\in I:h(x)>kd\}.
 \tag{FT2.2}
\]
By FT1 choose open \(O_k\supseteq E_k\) with
\(m(O_k\setminus E_k)<\varepsilon 2^{-k-2}/d\). On \(I\) put
\[
 q(x)=d\sum_{k=0}^{\infty}1_{E_k}(x),\qquad
 g(x)=d\sum_{k=0}^{\infty}1_{O_k}(x).
 \tag{FT2.3}
\]
For a finite nonnegative number \(h(x)\), counting the multiples \(kd<h(x)\) shows
\(h(x)\leq q(x)<h(x)+d\); this also holds when \(h(x)=0\). Therefore \(g\geq q\geq h\) at every point. Each \(1_{O_k}\) is lower semicontinuous. A finite sum of such nonnegative functions is lower semicontinuous: if its value exceeds a number, finitely many strict lower bounds at that point, valid on a common neighbourhood, already make the sum exceed that number. The supremum of the increasing partial sums is lower semicontinuous because its strict superlevel set is the union of their strict superlevel sets. Thus \(g\) is lower semicontinuous.

Monotone convergence and \(O_k\supseteq E_k\) give
\[
 \begin{aligned}
 \int_I g
 &=d\sum_{k=0}^{\infty}m(I\cap O_k)\\
 &\leq d\sum_{k=0}^{\infty}m(E_k)
       +d\sum_{k=0}^{\infty}m(O_k\setminus E_k)\\
 &<\int_I q+\frac{\varepsilon}{2}
 \leq\int_I h+d(b-a)+\frac{\varepsilon}{2}
 <\int_I h+\varepsilon.
 \end{aligned}
 \tag{FT2.4}
\]
In particular \(g\) is integrable and finite almost everywhere. Its possible infinite point values will be retained for the pointwise comparison.

*Reduction of a signed \(f\) to this case.* Put \(f_N=\max(f,-N)\). Then \(0\leq f_N-f\leq |f|\), and \(f_N-f\to0\) pointwise. Dominated convergence gives \(\int_I(f_N-f)\to0\). Choose \(N\geq1\) for which this integral is less than \(\varepsilon/2\). The function \(h=f_N+N\) is finite, nonnegative and integrable. Apply the nonnegative case with error \(\varepsilon/2\) to obtain \(g_0\). Set \(g=g_0-N\). It is lower semicontinuous, bounded below by \(-N\), and satisfies \(g\geq f_N\geq f\). It is integrable since \(|g|\leq g_0+N\) on the finite interval. Its integral is less than \(\int_I f_N+\varepsilon/2<\int_I f+\varepsilon\). \(\square\)

## FT3. Comparing an increment with an integral

**Lemma.** Let \(F:[a,b]\to\mathbb R\) be continuous. Suppose its finite right derivative \(D_+F(x)\) exists at every \(x\in(a,b)\). If a finite-valued integrable \(f\) satisfies \(D_+F(x)\leq f(x)\) at every such \(x\), then
\[
 F(b)-F(a)\leq\int_a^b f(x)\,dx.
 \tag{FT3.1}
\]
No derivative is required at either endpoint.

*Proof.* Choose the majorant \(g\) from FT2 with error \(\varepsilon>0\), and put \(G(x)=\int_a^x g(t)\,dt\). By FT1 this is a continuous real function even if the chosen representative of \(g\) has infinite values at some points. Fix \(\tau>0\) and set
\[
 H(x)=F(x)-G(x)-\tau x.
 \tag{FT3.2}
\]
We claim \(H(v)\leq H(u)\) whenever \(a<u<v<b\). If instead \(H(v)>H(u)\), continuity on \([u,v]\) gives a minimum at some \(c\in[u,v)\). In particular \(a<c<b\), so the right derivative \(d_c=D_+F(c)\) exists. Choose \(q=d_c-\tau/4\). Since \(g(c)\geq f(c)\geq d_c>q\), lower semicontinuity gives \(g(t)>q\) on a neighbourhood of \(c\), including a sufficiently short right interval. This remains valid if \(g(c)=+\infty\).

The definition of the right derivative gives, for sufficiently small \(h>0\),
\[
 F(c+h)-F(c)\leq(d_c+\tau/4)h.
 \tag{FT3.3}
\]
Choose such an \(h\) with \(c+h\leq v\) and with \([c,c+h]\) in the neighbourhood just chosen. Integral monotonicity gives \(G(c+h)-G(c)\geq qh\). Consequently
\[
 H(c+h)-H(c)
 \leq(d_c+\tau/4-q-\tau)h=-\frac{\tau h}{2}<0,
 \tag{FT3.4}
\]
contrary to the minimum property. This proves the claim. Let \(u\downarrow a\), \(v\uparrow b\), using continuity, to get
\[
 F(b)-F(a)\leq\int_a^b g+\tau(b-a)
 <\int_a^b f+\varepsilon+\tau(b-a).
 \tag{FT3.5}
\]
Since \(\varepsilon\) and \(\tau\) are arbitrary positive numbers, (FT3.1) follows. \(\square\)

The pointwise majorization in FT2 is essential to this proof: the minimizing point \(c\) cannot be chosen to avoid an unspecified null exceptional set.

## FT4. The real and complex fundamental theorem

**Theorem.** If \(F:[a,b]\to\mathbb R\) or \(\mathbb C\) is continuous, differentiable at every interior point, and has integrable derivative, then
\[
 \int_a^b F'(x)\,dx=F(b)-F(a).
 \tag{FT4.1}
\]
The same statement holds for a finite right derivative at every interior point. It holds on every closed subinterval as well. In particular \(F\) is absolutely continuous: for every \(\varepsilon>0\) there is \(\delta>0\) such that any finite family of intervals with disjoint interiors and total length less than \(\delta\) satisfies
\[
 \sum_j|F(v_j)-F(u_j)|<\varepsilon.
 \tag{FT4.2}
\]

*Proof.* Assign arbitrary finite values to the derivative at the two endpoints. In the real case, FT3 applied to \(F\), then to \(-F\), with their respective integrable derivatives gives both inequalities in (FT4.1). Two-sided differentiability implies the right-derivative hypothesis. For complex \(F\), apply the real conclusion to its real and imaginary parts; both derivatives are integrable since their absolute values are bounded by \(|F'|\), and scalar integration is componentwise. When \(a=b\), both sides of (FT4.1) are zero.

The assumptions restrict to every closed subinterval, so the same equality holds there. The absolute integral bound gives
\( |F(v_j)-F(u_j)|\leq\int_{u_j}^{v_j}|F'|\).
Add these inequalities. Overlaps can only be endpoints, whose measures are zero, so the sum of the integrals is the integral over the union. Its measure is at most the total interval length. FT1 gives (FT4.2). \(\square\)

There is no hidden measurability assumption about derivatives beyond the stated integral. Indeed, the finite right derivative of a continuous function is Borel measurable on \((a,b)\). Extend \(F\) constantly to the left and right of \([a,b]\), obtaining a continuous \(\widetilde F\) on \(\mathbb R\). Each
\( n(\widetilde F(x+1/n)-\widetilde F(x))\) is continuous, and their pointwise limit on \((a,b)\) is the right derivative. Pointwise limits of measurable scalar functions are measurable, as proved in the preceding programme lesson. Thus assigning endpoint values gives a measurable derivative representative; integrability is still a separate hypothesis.

## FT5. Products, oriented substitution and infinite endpoints

Let \(u,v\) be continuous on \([a,b]\), differentiable at every interior point, and suppose the products \(u'v\) and \(uv'\) are integrable. The elementary product rule gives \((uv)'=u'v+uv'\), an integrable derivative. Applying FT4 to \(uv\) proves
\[
 \int_a^b u'v=u(b)v(b)-u(a)v(a)-\int_a^b uv'.
 \tag{FT5.1}
\]
The product rule is proved directly by splitting the increment into
\( [u(x+h)-u(x)]v(x+h)+u(x)[v(x+h)-v(x)]\), dividing by \(h\), and taking the limit. Thus no continuity of the derivatives is used. In particular continuously differentiable factors satisfy the finite-interval formula, because their derivatives and the factors are bounded on a compact interval and hence the products are integrable.

For oriented substitution, let \(\phi\in C^1([a,b])\), and let \(h\) be continuous on an interval containing the image of \(\phi\). Put \(A(s)=\int_{s_0}^s h(t)\,dt\), with reversed endpoints interpreted by a minus sign. The difference quotient of \(A\) is an interval average of \(h\); its difference from \(h(s)\) is bounded by the supremum of \(|h(t)-h(s)|\) on the shrinking interval. Hence \(A'=h\). The chain rule, obtained by composing the first-order difference expansions, gives \((A\circ\phi)'=(h\circ\phi)\phi'\). FT4, or the earlier C1 Lemma 6.1, now yields
\[
 \int_{\phi(a)}^{\phi(b)}h(t)\,dt
 =\int_a^b h(\phi(x))\phi'(x)\,dx.
 \tag{FT5.2}
\]
There is no monotonicity requirement on \(\phi\), and the signed derivative is retained.

If \(F\) is differentiable on \(\mathbb R\), \(F'\in L^1(\mathbb R)\), and \(F(t)\to L_\pm\) as \(t\to\pm\infty\), apply FT4 on \([-A,B]\). Dominated convergence for \(F'1_{[-A,B]}\), with majorant \(|F'|\), and the assumed endpoint limits give
\[
 \int_{\mathbb R}F'=L_+-L_-.
 \tag{FT5.3}
\]
The endpoints may tend independently to infinity: the absolute integrals on either omitted tail tend to zero. The same argument on \([a,B]\) gives the half-line formula with its finite endpoint value. Finally, if \(u,v\) are differentiable on \(\mathbb R\), \(u'v,uv'\in L^1\), and \(u(t)v(t)\to L_\pm\), apply (FT5.3) to their product to obtain
\[
 \int_{\mathbb R}u'v=L_+-L_--\int_{\mathbb R}uv'.
 \tag{FT5.4}
\]
Zero endpoint products therefore give the negative transposed integral. Each endpoint limit must be checked; boundedness alone does not supply it.

## FT6. Two distinctions in the hypotheses

**An integrable derivative that is not continuous.** On \([-1,1]\), put \(F(0)=0\) and \(F(x)=x^2\sin(1/x)\) for \(x\ne0\). At zero, \(F(x)/x=x\sin(1/x)\to0\), so \(F'(0)=0\). Away from zero, direct differentiation gives
\[
 F'(x)=2x\sin(1/x)-\cos(1/x).
 \tag{FT6.1}
\]
This derivative is bounded in absolute value by three and is measurable by FT4, hence is integrable. Along \(x_n=1/(2\pi n)\) its value is \(-1\); along \(y_n=1/((2n+1)\pi)\) it is \(1\). Thus it is not continuous at zero. Nevertheless FT4 gives \(\int_{-1}^1F'=2\sin1\). This case lies outside the C1 version of the theorem.

**Almost-everywhere differentiability is insufficient.** A direct construction makes the distinction explicit. Set \(C_0(x)=x\) on \([0,1]\) and recursively set
\[
 C_{n+1}(x)=
 \begin{cases}
 \tfrac12 C_n(3x),&0\leq x\leq\tfrac13,\\
 \tfrac12,&\tfrac13\leq x\leq\tfrac23,\\
 \tfrac12+\tfrac12 C_n(3x-2),&\tfrac23\leq x\leq1.
 \end{cases}
 \tag{FT6.2}
\]
Induction shows each \(C_n\) is continuous and nondecreasing, with endpoint values zero and one; the formulas agree at the two joints. The recursion gives
\(\|C_{n+1}-C_n\|_\infty\leq\tfrac12\|C_n-C_{n-1}\|_\infty\) for \(n\geq1\). The geometric-series bound makes \(C_n\) uniformly Cauchy. Real completeness gives a pointwise limit \(C\), and the same uniform bound proves uniform convergence. The limit is continuous: approximate it uniformly by one \(C_n\), then use continuity of that \(C_n\) at the point in question. It still has \(C(0)=0\), \(C(1)=1\).

Let \(K_n\) be the union of the \(2^n\) closed intervals remaining after \(n\) successive removals of open middle thirds, and let \(K=\bigcap_n K_n\). Its measure is at most \(2^n3^{-n}\) for every \(n\), hence zero. Every point outside \(K\) lies in an open interval deleted at some finite stage. On a middle interval the recursion is constant; composing the two outer affine branches shows that on each later deleted interval all subsequent \(C_n\) have the same constant value. Therefore \(C\) is locally constant outside \(K\) and has derivative zero there.

Thus \(C\) is continuous, differentiable almost everywhere, and its almost-everywhere derivative has the integrable representative zero, but \(C(1)-C(0)=1\ne0=\int_0^1 0\). This does not contradict FT4: that theorem requires the finite derivative at every interior point. The example also shows why that condition cannot be silently replaced by an almost-everywhere assertion.

## Free source and proof scope

[D. H. Fremlin, *Measure Theory*, Chapter 22](https://www1.essex.ac.uk/maths/people/fremlin/chap22.pdf), 225I and 225L, is a free human reference for the semicontinuous majorant and the integrable-derivative FTC. The local source comparison read pages 31–34, including 225I–225L, and inspected those page images. FT1–FT4 above give the complete compact-interval argument with its own rounding construction and minimum argument; no general Vitali covering, differentiation-of-integrals or absolute-continuity characterization is imported. FT5 supplies every remaining clause of the declared scalar FTC interface. The separate general multidimensional Jacobian prerequisite is proved in [The Jacobian theorem on a measurable source set](relative-jacobian.md), with its [geometric measure foundations](euclidean-volume-foundations.md).
