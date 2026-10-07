# Integration and duality for Cauchy evolution

This companion supplies the complete norm, extension and integration arguments used by the first-order existence proof. It retains the full AN-03 Hahn–Banach argument, all-exponent integral inequalities, and the complete construction of the Bochner integral and its spaces. The final sections connect those proofs to the original time interval, Sobolev dual pairing and distributional trace.

This is a modified selection from *Elliptic Operators & Boundary Problems: Renewed 2026 Course Draft*. Original principal author: AN-03 course-writing task. Original publisher: AN-03 local course project. The AN-03 course-writing task and OpenAI Codex are responsible for the renewed edition. Selection, current prerequisite bindings and explicitly identified connecting proofs: GPT-6 Astra (OpenAI), Ultra, 5 October 2026; publisher: AN-04 local course project.

Original text: CC0.

## H0. Earlier proofs and notation

The retained selections below are from AN03-P004, *Banach estimates, quotient spaces and compact parameter arguments*: Section 5 before its unrelated editorial addendum, Section 15.2, and Sections 17.1–17.3. Their mathematical bodies and original labels are unchanged. Section references inside those extracts identify their AN-03 source; the exact included replacements are specified here.

The [measure proof M0–M8](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) proves the chosen Zorn axiom's selection consequence, real and complex integration, completed Lebesgue measure, monotone and dominated convergence, product integration, affine Jacobians, completeness and compact smooth density. LP4 in the retained text is exactly M4's product formula; LP5 is its already proved affine change of variables. General-measure statements below assume a measure and its defining countable additivity; the same simple-function supremum proof in M3 supplies convergence on that measure. The Cauchy receiver uses only Lebesgue measure on a finite real interval.

The [Hilbert-space proof T1](../20261004-free-canonical-composition/compactness-and-essential-norms.md#t1-the-hilbert-space-facts-with-proofs) proves representation and adjoints from completeness by the parallelogram identity, with no separability assumption. The [global Sobolev isometries G1](sharp-lower-bound.md#g1-global-sobolev-bounds-with-the-original-norms) and [Fourier L1–L3](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md) identify all pairings and dense subspaces. [U001's real-variable and compact calculus](../20261004-free-stationary-phase/proof-map.html) supplies real powers, derivatives, finite-dimensional compactness and scalar fundamental theorems. The inner product is linear in the first entry. Every dependency has an exact locator in the [proof map](proof-map.json).

## 5. Hahn–Banach and scalar norm tests

Let \(M\subset X\) be a linear subspace of a real normed space and \(f:M\to\mathbb R\) bounded and linear, with \(C=\|f\|\). We first prove an extension by one vector. For \(v\notin M\), consider the real intervals with endpoints
\[
f(m)-C\|m-v\|,\qquad f(m)+C\|m-v\|\quad(m\in M).
\]
Every lower endpoint is at most every upper endpoint: for \(m,n\in M\),
\[
f(m)-f(n)\leq C\|m-n\|\leq C\|m-v\|+C\|n-v\|.
\]
The endpoints from \(m=0\) show that the lower endpoints are bounded above and the upper endpoints bounded below. Real completeness supplies a real \(c\) between their supremum and infimum. Consequently
\[
|c-f(m)|\leq C\|v-m\|\quad(m\in M).
\tag{B4}
\]
Define \(F(m+tv)=f(m)+tc\). The representation is unique because \(v\notin M\), so \(F\) is real-linear and extends \(f\). For \(t\ne0\), apply (B4) to \(-m/t\) and multiply by \(|t|\); it gives \(|F(m+tv)|\leq C\|m+tv\|\). For \(t=0\) use the original bound. Restriction supplies the reverse inequality for the norms, so \(\|F\|=C\). This also handles \(C=0\).

For extension to all of \(X\), order the pairs consisting of a subspace containing \(M\) and an extension of \(f\) bounded by \(C\), by extension. The original pair makes this a nonempty partially ordered set. For a nonempty chain, the union of its subspaces is a subspace: any finite list of vectors belongs to one member of the chain. The functionals agree on overlaps, giving a well-defined linear functional on that union with the same bound. This is an upper bound; the original pair bounds an empty chain. Zorn's explicitly assumed maximality principle gives a maximal pair. The one-vector construction shows that its domain cannot omit any vector of \(X\). Thus the real extension exists on all of \(X\), with norm \(C\).

Now let \(X\) and \(M\) be complex and \(f:M\to\mathbb C\) bounded and complex-linear. Its real part \(h=\operatorname{Re}f\) is a real-linear functional on the underlying real subspace. Its real operator norm equals \(\|f\|\): one inequality is \(|h(m)|\leq|f(m)|\); for the other, when \(f(m)\ne0\), multiply \(m\) by \(\theta=\overline{f(m)}/|f(m)|\), so \(h(\theta m)=|f(m)|\) and \(\|\theta m\|=\|m\|\). Extend \(h\) by the real result to \(a:X\to\mathbb R\), with norm \(\|f\|\), and put
\[
F(x)=a(x)-i\,a(ix).
\tag{B5}
\]
Real-linearity gives additivity and \(F(ix)=iF(x)\); together these prove complex-linearity. On \(M\), \(\operatorname{Re}f(im)=-\operatorname{Im}f(m)\), so \(F(m)=f(m)\). For any \(x\) with \(F(x)\ne0\), choose a unit scalar \(\theta\) making \(\theta F(x)=|F(x)|\). Complex-linearity gives
\[
|F(x)|=\operatorname{Re}F(\theta x)=a(\theta x)
\leq\|a\|\|x\|.
\]
The zero value is harmless. Thus \(\|F\|\leq\|a\|=\|f\|\), while restriction proves equality. Neither the closedness of \(M\) nor the completeness of \(X\) was required.

For any complex normed space \(E\), this implies the exact norm identity
\[
\|v\|=\sup_{\ell\in E',\ \|\ell\|\leq1}|\ell(v)|.
\tag{B6}
\]
The right side is at most the left by the operator bound. If \(v\ne0\), define \(f(zv)=z\|v\|\) on the complex line it spans. Its norm is one, and (B5) extends it with the same norm, attaining \(\ell(v)=\|v\|\). If \(v=0\), every value is zero and the dual ball contains the zero functional. Thus the identity holds also for the zero space. It applies in particular to \(E=\mathcal L(B_1,B_2)\); Section 3 separately proves that this operator space is Banach when \(B_2\) is Banach.

The practical consequence is precise. If \(|\ell(v)|\leq K\|\ell\|\) for every continuous complex-linear \(\ell\), with the same \(K\), then \(\|v\|\leq K\). A bound depending arbitrarily on \(\ell\) cannot be substituted for that uniform estimate.

### 15.2. Hölder, Minkowski and all Young endpoints

For \(1<p<\infty\), put \(p'=p/(p-1)\). The scalar inequality \(ab\leq a^p/p+b^{p'}/p'\), \(a,b\geq0\), follows by maximizing \(ab-a^p/p\) as a function of \(a\): its derivative is \(b-a^{p-1}\), with maximum at \(a=b^{1/(p-1)}\); the zero case follows directly. Apply it to \(|f|/\|f\|_p\) and \(|g|/\|g\|_{p'}\) when both norms are nonzero and finite. The original functions and norms are retained, and multiplication restores both norm factors. If a norm is zero, its function vanishes almost everywhere and the conclusion follows directly. This proves
\[
 \int|fg|\leq\|f\|_p\|g\|_{p'},\qquad
 \int|fg|\leq\|f\|_1\|g\|_\infty.
 \tag{LP6}
\]
The second inequality is the pointwise essential bound. It also covers its reversed ordering. The first inequality includes integral Cauchy–Schwarz at \(p=p'=2\). Repeated application proves Hölder for any finite number of factors whose reciprocal exponents sum to one, including infinite exponents by their essential bounds.

For \(1<p<\infty\), the convexity of \(t^p\) gives \(|f+g|^p\leq2^{p-1}(|f|^p+|g|^p)\), so the sum is integrable. Using \(|f+g|^p\leq(|f|+|g|)|f+g|^{p-1}\) and (LP6) gives \(\|f+g\|_p^p\leq(\|f\|_p+\|g\|_p)\|f+g\|_p^{p-1}\). Divide when that norm is positive; if it is zero the result is immediate. The integral triangle inequality gives the case \(p=1\), and the essential-supremum triangle inequality gives \(p=\infty\). Thus every original \(L^p\) norm satisfies Minkowski.

Let \(1\leq p,q,r\leq\infty\) satisfy \(1+1/r=1/p+1/q\). Convolution uses the original density \(dy\). When \(r<\infty\), the relation forces \(p,q<\infty\) and \(r\geq p,q\). Split the absolute integrand into the three factors
\[
 |f(y)g(x-y)|
 =\bigl(|f(y)|^{p/r}|g(x-y)|^{q/r}\bigr)
        |f(y)|^{1-p/r}|g(x-y)|^{1-q/r}.
 \tag{LP7}
\]
If an exponent is zero, its factor is omitted; this convention also applies where its base vanishes. Hölder uses exponents \(r\), \(pr/(r-p)\) and \(qr/(r-q)\) for the retained factors. A factor with zero exponent requires no division by zero. Their reciprocal sum is \(1/r+(1/p-1/r)+(1/q-1/r)=1\). Hence, outside any exceptional set where the first integral is infinite,
\[
 |f*g(x)|^r
 \leq\left(\int|f(y)|^p|g(x-y)|^q\,dy\right)
         \|f\|_p^{r-p}\|g\|_q^{r-q}.
 \tag{LP8}
\]
Zero input norms give zero convolution. For positive norms, integrating (LP8), using (LP4) and the translation case of (LP5), shows that the first integral is finite for almost every \(x\), and proves
\[
 \|f*g\|_r\leq\|f\|_p\|g\|_q.
 \tag{LP9}
\]
If \(r=\infty\), then \(1/p+1/q=1\), so (LP6) proves (LP9) directly for each defined section and its essential supremum. This includes \(p=1,q=\infty\) and \(p=\infty,q=1\). For \(p=q=r=1\), (LP8) is simply the integrated triangle bound; the two omitted factors have exponent zero. These cases exhaust the displayed exponent relation, and no strong estimate with an invalid exponent is being asserted.

### 17.1. Strong measurability and finite-valued approximation

Let \((\Omega,\mathcal A,\mu)\) be a positive measure space. It need not be sigma-finite or complete. Let \(B\) be the original real or complex Banach space. Equality almost everywhere means equality outside a measurable null set. We replace values on that set by zero when constructing representatives. A finite-valued measurable function is
\[
 s=\sum_{j=1}^J b_j1_{E_j},\qquad
 E_j\in\mathcal A,\quad E_j\cap E_k=\varnothing\ (j\ne k),
 \quad b_j\in B.
 \tag{BI1}
\]
The value off their union is zero. A function \(f:\Omega\to B\) is strongly measurable when it is the pointwise limit almost everywhere of such functions. The union of the finitely many values in a countable approximating sequence, together with zero, is countable. Its closure \(S\) is separable, and \(f\) takes values in \(S\) off one measurable null set. For each \(b\in B\), the real function \(\|f-b\|_B\) is measurable there, since it is the pointwise limit of the corresponding measurable distances. Its extension by the distance from zero on the null set is measurable.

Conversely suppose, after this null-set replacement, that \(f\) takes values in a separable subset \(S\subset B\) and every distance \(\|f-b\|_B\) is measurable. Choose a countable dense family \(b_1,b_2,\ldots\) in \(S\cup\{0\}\), with \(b_1=0\). For each \(N\geq1\), choose the least index among the minimizers of the first \(N\) distances. The measurable cells are explicitly
\[
 E_{N,j}=
 \{\|f-b_j\|_B<\|f-b_k\|_B\text{ for every }k<j\}
 \cap
 \{\|f-b_j\|_B\leq\|f-b_k\|_B\text{ for every }j<k\leq N\},
 \quad 1\leq j\leq N,
 \qquad
 q_N=\sum_{j=1}^N b_j1_{E_{N,j}}.
 \tag{BI2}
\]
An intersection over no indices imposes no condition. These disjoint cells cover \(\Omega\), including ties and zero distances. Density proves \(q_N(x)\to f(x)\) at every point of this representative. Since zero is always one of the candidates,
\[
 \|q_N(x)-f(x)\|_B\leq\|f(x)\|_B,\qquad
 \|q_N(x)\|_B\leq2\|f(x)\|_B.
 \tag{BI3}
\]
This proves the converse without a sigma-finiteness assumption. It also proves closure of strong measurability under pointwise almost-everywhere limits: take the closure of the countable union of the separable ranges of all functions in the sequence. The limit has its range in that closure, and every distance to a fixed vector is a measurable pointwise limit. Finite sums and continuous linear images are covered by the same argument; their ranges lie in the separable closure of the appropriate countable sums or images.

If \(1\leq p<\infty\) and \(\int\|f\|_B^p\,d\mu<\infty\), dominated convergence applied to (BI3) gives
\[
 \|q_N-f\|_{L^p(\mu;B)}^p
  =\int_\Omega\|q_N-f\|_B^p\,d\mu\longrightarrow0.
 \tag{BI4}
\]
Each nonzero value \(b_j\) of \(q_N\) has a support of finite measure: on its cell, (BI3) gives \(\|f\|_B\geq\|b_j\|_B/2\), hence
\[
 \mu(E_{N,j})
 \leq {2^p\over\|b_j\|_B^p}
          \int_{E_{N,j}}\|f(x)\|_B^p\,d\mu(x)<\infty
 \quad(b_j\ne0).
 \tag{BI5}
\]
The zero cell can have infinite measure and contributes the zero vector; no expression \(0\cdot\infty\) is used to define its integral. Thus finite-valued functions with finite-measure nonzero cells are dense in every finite-\(p\) Bochner space, on the original arbitrary measure space.

### 17.2. The actual vector integral, norm bound and continuous maps

For (BI1) with finite-measure nonzero cells, set
\[
 I(s)=\sum_{\{j:b_j\ne0\}}\mu(E_j)b_j,\qquad
 \|I(s)\|_B\leq\sum_{\{j:b_j\ne0\}}\mu(E_j)\|b_j\|_B
                 =\int_\Omega\|s\|_B\,d\mu.
 \tag{BI6}
\]
The sums on the right also omit zero cells. Refining any two finite representations by their intersections proves independence: the measure of each finite-measure cell is the sum of its refined pieces, and every original vector coefficient remains. A common refinement proves linearity for finite-valued integrable functions and the difference bound
\(\|I(s)-I(t)\|_B\leq\int\|s-t\|_B\,d\mu\).

Let \(f\) be strongly measurable and norm-integrable. Choose any finite-valued integrable sequence \(s_k\) tending to \(f\) in \(L^1(\mu;B)\), supplied by (BI4). Its integrals are Cauchy by the difference bound, so completeness of the original \(B\) supplies a vector limit. Define
\[
 \int_\Omega f\,d\mu=\lim_{k\to\infty}I(s_k),\qquad
 \left\|\int_\Omega f\,d\mu\right\|_B
       \leq\int_\Omega\|f\|_B\,d\mu.
 \tag{BI7}
\]
Indeed
\(\int\|s_k\|_B\leq\int\|f\|_B+\int\|s_k-f\|_B\).
Any second approximating sequence \(t_k\) gives the same limit because
\(\|I(s_k)-I(t_k)\|_B\leq\|s_k-f\|_1+\|t_k-f\|_1\).
This proves existence, independence, linearity, almost-everywhere invariance and the exact norm inequality. It is the Bochner integral; its definition retains the original vector space and its norm.

If \(T:B\to C\) is bounded linear between the original Banach spaces, then \(Tf\) is strongly measurable and
\[
 \int_\Omega Tf\,d\mu
       =T\!\left(\int_\Omega f\,d\mu\right),\qquad
 \|Tf\|_{L^1(\mu;C)}\leq\|T\|_{\mathcal L(B,C)}\|f\|_{L^1(\mu;B)}.
 \tag{BI8}
\]
Both statements hold first for each finite sum, with its original coefficient order, and then follow by the displayed operator norm and (BI7). In particular every real or complex continuous linear functional commutes with integration. Complex Banach duality here is complex linear, with no conjugation inserted in that identity.

Suppose \(f_k\) are strongly measurable, \(f_k\to f\) almost everywhere, and \(\|f_k(x)\|_B\leq g(x)\) for one nonnegative integrable \(g\). The closure argument in Section 17.1 proves strong measurability of the limit; continuity of the norm gives \(\|f\|_B\leq g\). Scalar dominated convergence applied to the exact bound \(\|f_k-f\|_B\leq2g\) gives
\[
 \int_\Omega\|f_k-f\|_B\,d\mu\longrightarrow0,\qquad
 \left\|\int_\Omega f_k\,d\mu-\int_\Omega f\,d\mu\right\|_B
       \leq\int_\Omega\|f_k-f\|_B\,d\mu\longrightarrow0.
 \tag{BI9}
\]
The majorant hypothesis and the pointwise limit are explicit; a weak scalar limit alone cannot be substituted.

### 17.3. Complete Bochner spaces, including nonseparable Hilbert spaces

For \(1\leq p<\infty\), the space \(L^p(\mu;B)\) consists of almost-everywhere classes of strongly measurable functions with norm
\[
 \|f\|_{L^p(\mu;B)}
     =\left(\int_\Omega\|f(x)\|_B^p\,d\mu(x)\right)^{1/p}.
 \tag{BI10}
\]
At \(p=\infty\) use the essential supremum of the same original pointwise norm. Scalar Minkowski and the pointwise Banach triangle inequality give the norm triangle inequality; vanishing norm is exactly almost-everywhere vanishing.

Let \(f_j\) be Cauchy. Choose a subsequence with
\(\|f_{j_{k+1}}-f_{j_k}\|_p\leq2^{-k}\).
For finite \(p\), the increasing functions
\[
 G_M(x)=\|f_{j_1}(x)\|_B+
          \sum_{k=1}^M\|f_{j_{k+1}}(x)-f_{j_k}(x)\|_B
\]
have \(L^p\) norms at most \(\|f_{j_1}\|_p+\sum_{k=1}^M2^{-k}\).
Scalar monotone convergence applied to \(G_M^p\) shows that their limit is finite almost everywhere and has that same finite bound. Completeness of \(B\) therefore gives the pointwise vector sum
\[
 f(x)=f_{j_1}(x)+
           \sum_{k=1}^\infty(f_{j_{k+1}}(x)-f_{j_k}(x))
 \quad\text{almost everywhere},\qquad
 \|f-f_{j_k}\|_p
       \leq\sum_{\nu=k}^\infty
                   \|f_{j_{\nu+1}}-f_{j_\nu}\|_p
       \leq\sum_{\nu=k}^\infty2^{-\nu}.
 \tag{BI11}
\]
The first inequality follows by bounding the pointwise difference by the entire nonnegative tail and passing its finite sums through monotone convergence. Strong measurability of \(f\) follows from Section 17.1. The bound on \(G\) puts \(f\) in \(L^p\); the Cauchy property and the triangle inequality give convergence of the entire original sequence. For \(p=\infty\), remove the countable union of measurable null sets for the initial essential bound and every displayed difference bound. The same series converges uniformly in \(B\) on the complement and satisfies (BI11) in the essential-supremum norm. This proves completeness at every \(1\leq p\leq\infty\) on the original measure space.

Finite-valued density (BI4) has only been proved for finite \(p\). It is false in general at infinity. On \(\Omega=\mathbb N\) with counting measure and \(B=\ell^2(\mathbb N)\), let \(f(k)=e_k\), the original unit coordinate vectors. The truncations are finite-valued and converge pointwise, so \(f\) is strongly measurable, with essential-supremum norm one. If \(s\) has any finite set of values \(v_1,\ldots,v_J\), then
\[
 \|e_k-v_j\|_{\ell^2}^2
      =1+\|v_j\|_{\ell^2}^2
                -2\operatorname{Re}(v_{j,k})\longrightarrow
                       1+\|v_j\|_{\ell^2}^2.
 \tag{BI12}
\]
Each coordinate \(v_{j,k}\) tends to zero, because its square sum is finite. Taking the minimum over this finite family shows
\(\liminf_{k\to\infty}\|e_k-s(k)\|_{\ell^2}\geq1\).
Thus the exact original essential-supremum distance is at least one.

For an arbitrary complex Hilbert space \(H\), finite or infinite dimensional and possibly nonseparable, define
\[
 (f,g)_{L^2(\mu;H)}
       =\int_\Omega(f(x),g(x))_H\,d\mu(x).
 \tag{BI13}
\]
The inner product is linear in its first variable. Scalar Cauchy--Schwarz proves absolute integrability of this scalar pairing and its continuity. Strong measurability of the pair is inherited from finite-valued approximations. The pointwise Hilbert identities give linearity, conjugate symmetry and positivity after integration, with \((f,f)=\|f\|_2^2\). Completeness is (BI11), so this is a Hilbert space. No countable basis of the ambient \(H\) was used.

**The full pointwise Hilbert inequality used in (BI13).** For the original possibly nonseparable \(H\), let \(v\ne0\) and \(c=(u,v)_H/(v,v)_H\). Positivity of its original norm gives the complete expansion
\[
 0\leq\|u-cv\|_H^2
 =\|u\|_H^2-\overline c(u,v)_H-c(v,u)_H+|c|^2\|v\|_H^2
 =\|u\|_H^2-\frac{|(u,v)_H|^2}{\|v\|_H^2}.
 \tag{BI13a}
\]
Every term uses the original inner product, linear in its first variable. For \(v=0\), the pairing is zero. Thus \(|(u,v)_H|\leq\|u\|_H\|v\|_H\), including all zero cases. Applying the separately proved scalar integral Cauchy--Schwarz to these two original pointwise norms proves the absolute-integrability clause of (BI13). No basis or separability of \(H\) is used.

## H4. Time approximation and bounded measurable operator families

On \(I=(0,T)\), \(T<\infty\), a finite-valued measurable function with values in \(H^s\) is a finite sum \(1_E v\). Approximate \(v\) in \(H^s\) by a Schwartz vector using G2. Approximate \(1_E\) in scalar \(L^1(I)\) by smooth functions, using M7 in dimension one after extension by zero; finite sums and BI4 therefore prove density of finite sums of smooth time functions times Schwartz vectors in \(L^1(I;H^s)\). The same construction proves density of compact smooth scalar functions in \(L^p(\mathbb R)\) for finite \(p\): first truncate the value and support; for an indicator, choose the compact smooth approximation between zero and one by the M7 cutoff construction, so its \(L^p\) error to that indicator is bounded by its \(L^1\) error. The finite bounded simple approximations and LP6–LP9 finish the proof.

Let \(A(t):H^s\to H^{s-1}\) be uniformly bounded and strongly continuous. If \(u(t)\) is strongly measurable, take its almost-everywhere finite-valued approximations. For each fixed vector \(v\), the continuous map \(t\mapsto A(t)v\) is strongly measurable: uniform continuity on compact time intervals gives finite step approximations there. Hence \(A(t)u_j(t)\) is strongly measurable, and the uniform bound gives pointwise convergence to \(A(t)u(t)\). BI2–BI3 imply strong measurability of the limit. The bound
\[
 \|A(\cdot)u(\cdot)\|_{L^p(I;H^{s-1})}
       \le \sup_{t\in I}\|A(t)\|\,\|u\|_{L^p(I;H^s)}
 \tag{H1}
\]
holds also at infinity by its essential-supremum definition.

## H5. The actual primitive and its weak and almost-everywhere derivative

For \(g\in L^1(I;B)\) in the original Banach space, define \(w(t)=\int_0^t g(r)\,dr\) by BI7. For finitely many disjoint intervals,
\[
 \sum_j\|w(b_j)-w(a_j)\|_B
       \le\int_{\bigcup_j(a_j,b_j)}\|g(r)\|_B\,dr.
 \tag{H2}
\]
The scalar integral on the right is absolutely continuous with respect to interval length: truncate \(\|g\|\) above a large number to make the tail integral small, then bound the truncated part by that number times the total length. Thus \(w\) is absolutely continuous, in particular continuous. For any scalar compact smooth test \(\theta\), scalarization by a bounded functional, followed by scalar Fubini, gives
\[
 \int_I w(t)\theta'(t)\,dt=-\int_I g(t)\theta(t)\,dt.
 \tag{H3}
\]
Both vector integrals exist by BI7. Every functional commutes with them by BI8; Hahn–Banach's B6 separates their difference, so the identity is a vector identity. There is no unproved vector Fubini assertion in this argument.

For completeness the derivative is also \(g(t)\) in norm almost everywhere. Extend \(g\) by zero and approximate it in \(L^1(\mathbb R;B)\) by finite sums of continuous compact smooth scalar functions times vectors, using BI4 and the indicator approximation in H4. Here is the required scalar maximal bound. For nonnegative \(h\in L^1(\mathbb R)\), set
\[
 Mh(t)=\sup_{r>0}\frac1{2r}\int_{t-r}^{t+r}h(s)\,ds,\qquad
 |\{Mh>\lambda\}|\le \frac3\lambda\|h\|_1\quad(\lambda>0).
 \tag{H4}
\]
Each fixed-radius average is continuous, since its primitive is continuous by the scalar case of H2, so this superlevel set is open. Cover any compact subset by finitely many witnessing centered intervals. Select a longest interval, discard all intervals meeting it, and repeat. The selected intervals are disjoint. Every discarded interval has at most the selected length and meets its selector, so it lies in the interval with that same center and three times that length. Their union therefore has length at most three times the sum of the selected lengths. On each selected interval the integral of \(h\) exceeds \(\lambda\) times its length. Summing proves H4 for the compact subset. An open subset of the line is the increasing union of its compact truncations at positive distance from its complement; monotone convergence of measures proves H4 for the whole set.

For a continuous approximant \(v\), the upper limit as \(r\downarrow0\) of the average of \(\|g(s)-g(t)\|\) is at most
\[
 M(\|g-v\|)(t)+\|g(t)-v(t)\|.
 \tag{H5}
\]
Continuity makes the missing average of \(\|v(s)-v(t)\|\) tend to zero. H4 and the elementary bound \(|\{h>\lambda\}|\le\lambda^{-1}\int h\) show that the set where H5's left side exceeds any fixed \(\epsilon>0\) has measure at most \(8\epsilon^{-1}\|g-v\|_1\). Let the approximation error tend to zero, then take countably many positive rational \(\epsilon\). Almost everywhere the average norm difference tends to zero. A one-sided difference quotient for \(w\) is bounded by twice the corresponding centered average, so \((w(t+h)-w(t))/h\to g(t)\) in \(B\) at every such point.

If \(u\in L^1(I;H)\) has distributional derivative \(g\in L^1(I;H)\), then \(u-w\) is a single constant vector almost everywhere. For a scalar distribution of derivative zero, choose a compact test \(\beta\) of integral one. Every test \(\theta-(\int\theta)\beta\) has integral zero and a compact smooth primitive in \(I\); its pairing with the distribution is zero. The distribution therefore is constant. Apply this to all coordinate functionals from a countable dense subset of the separable closed linear span of the essential ranges of \(u,w\). Those ranges are separable by BI1–BI3; rational finite linear combinations make that span separable. All scalar constants hold simultaneously off a single null set. Evaluating at one point of that full-measure set supplies a vector \(c\), and the separating coordinates give \(u=w+c\) almost everywhere. It follows that \(u\) has an absolutely continuous representative and a well-defined trace. If \(g\) is continuous, the norm estimate for the integral difference quotient gives \(w'=g\) at every point, including the one-sided endpoint derivatives.

## H6. The exact Hilbert-valued duality used for existence

Let \(F\) be a bounded conjugate-linear functional on \(L^1(I;H)\), with \(|F(v)|\le K\|v\|_1\). It may be obtained by applying the retained complex Hahn–Banach theorem to the conjugate of a functional on a nonclosed subspace. LP6 gives \(\|v\|_1\le\sqrt T\|v\|_2\), so its restriction to the complete Hilbert space BI13 is bounded. T1 applied after conjugation gives \(u\in L^2(I;H)\) such that
\[
 F(v)=\int_I (u(t),v(t))_H\,dt.
 \tag{H6}
\]
If \(B=\{t:\|u(t)\|_H>K+\epsilon\}\) has positive measure, the strongly measurable vector \(v=1_Bu/\|u\|_H\), zero off \(B\), lies in \(L^2\), has \(L^1\) norm \(|B|\), and makes H6's right side \(\int_B\|u\|_H>K|B|\). This contradicts the bound. Thus \(u\in L^\infty(I;H)\), with norm at most \(K\). Bounded finite-valued functions lie in \(L^2\) on the finite interval and are dense in \(L^1\) by BI4, so H6 extends to every \(L^1\) vector. This proves precisely the required representation, without a general Banach dual formula.

For the Sobolev duality, apply this result after the isometry \(E_{-s}:H^{-s}\to L^2_x\) and use G2's inverse. The representative belongs to \(L^\infty_tH^s\). The exact norm-attaining test in the original variables is \(1_BE_{2s}u/\|u\|_s\), since \(E_{2s}:H^s\to H^{-s}\) is an isometry and its dual pairing with \(u\) equals \(\|u\|_s\) after normalization. This fixes the signs, conjugation and powers in the weak Cauchy construction.

## Source and receiving status

The unchanged extracts retain their AN-03 labels. H4–H6 are connecting programme proofs, including the actual primitive, trace and norm derivative, and the complete finite-interval Hilbert duality. These are standard results; no original research claim is made. Together with the sharp-lower-bound companion they close the functional-analytic inputs of U030. Its full restoration still requires the spacetime symbol and pullback dependencies and a review of the receiving proof.
