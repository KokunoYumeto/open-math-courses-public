# Denominators at the prime two

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Suppose that Catalan's constant \(G\) is rational. Then every determinant \(\Delta_N\) of [Chebyshev rows and mixed moments](chebyshev-rows-and-mixed-moments.md) is a rational number, and for a nonzero rational number the product formula \(\log|x|=\sum_pv_p(x)\log p\) expresses its size through its valuations. A lower bound for every \(v_p(\Delta_N)\) therefore gives a lower bound for \(|\Delta_N|\). This lesson sets up the tools for such bounds (valuations, the Cauchy–Binet formula, binomial coefficients) and proves the bound at the prime \(2\):

\[
v_2(\Delta_N)\ge-\frac{505}{4608}\,n^2-O_G\bigl(n\log(n+2)\bigr),\qquad n=48N.
\]

The difficulty is that individual moments have large powers of \(2\) in their denominators. The proof compares the moments with a \(2\)-adically convergent version of their defining series, whose valuations are excellent, and charges the two fixed discrepancies to a few columns at a time. The count of how many columns can carry large denominators becomes a quadratic optimization.

We use the \(p\)-adic numbers from [Completions, the p-adic numbers and complete discretely valued fields](course:NT-LOC/NT-LOC-02#digits-in-any-complete-discrete-valuation): \(\mathbb Q_p\) is complete for the \(p\)-adic absolute value, it satisfies the ultrametric inequality, and a series converges in \(\mathbb Q_p\) as soon as its terms tend to zero (Proposition 2.3 there). A basic reference is [OpenAI-Catalan].

## 1. Valuations, products and minors

For a prime \(p\) and a nonzero rational number \(x\), \(v_p(x)\) is the exponent of \(p\) in \(x\); we put \(v_p(0)=+\infty\). It extends to \(\mathbb Q_p\), and

\[
v_p(xy)=v_p(x)+v_p(y),\qquad v_p(x+y)\ge\min\{v_p(x),v_p(y)\}.
\]

For a nonzero rational number, unique factorization gives the **product formula**

\[
\log|x|=\sum_pv_p(x)\log p,
\tag{1.1}
\]

a finite sum. All lower bounds below are of the form \(v_p(\cdot)\ge\) something, and sums of any finite number of terms obey the same bound as their terms.

**Lemma 1.1** (Legendre). For \(m\ge0\), \(v_p(m!)=\sum_{k\ge1}\lfloor m/p^k\rfloor\). Consequently

\[
0\le v_p\binom{2l}l=\sum_{k\ge1}\Bigl(\Bigl\lfloor\frac{2l}{p^k}\Bigr\rfloor-2\Bigl\lfloor\frac l{p^k}\Bigr\rfloor\Bigr)\le\#\{k\ge1:p^k\le2l\}\le\frac{\log(2l)}{\log p}.
\]

**Proof.** The number of multiples of \(p^k\) up to \(m\) is \(\lfloor m/p^k\rfloor\), and a number divisible by exactly \(p^e\) is counted for \(k=1,\dots,e\). For the binomial coefficient, each bracket is \(0\) or \(1\) (since \(\lfloor2y\rfloor-2\lfloor y\rfloor\in\{0,1\}\)) and vanishes when \(p^k>2l\). \(\square\)

**Lemma 1.2** (Cauchy–Binet). Let \(F\) be an \(n\times m\) matrix and \(T\) an \(m\times n\) matrix over a commutative ring, \(m\ge n\). Then

\[
\det(FT)=\sum_{S}\det(F_S)\det(T^S),
\]

the sum running over \(n\)-element subsets \(S\subseteq\{1,\dots,m\}\), where \(F_S\) consists of the columns of \(F\) in \(S\) and \(T^S\) of the rows of \(T\) in \(S\), both in increasing order.

**Proof.** The \(k\)-th column of \(FT\) is \(\sum_jT_{jk}F_j\). By multilinearity, \(\det(FT)=\sum_{j_1,\dots,j_n}\prod_kT_{j_kk}\,\det(F_{j_1},\dots,F_{j_n})\). Terms with a repeated index vanish. Group the others by the set \(S=\{j_1,\dots,j_n\}\): writing \(j_k=s_{\sigma(k)}\) with \(s_1<\dots<s_n\) the elements of \(S\), the determinant is \(\operatorname{sgn}(\sigma)\det F_S\), and \(\sum_\sigma\operatorname{sgn}(\sigma)\prod_kT_{s_{\sigma(k)}k}=\det T^S\). \(\square\)

A **full minor** of an \(n\times m\) matrix is the determinant of \(n\) of its columns.

**Lemma 1.3.** Let \(X\) be an \(n\times n\) matrix over \(\mathbb Q_p\) whose \(k\)-th column has all entries of valuation at least \(\gamma_k\). Then \(v_p(\det X)\ge\sum_k\gamma_k\).

**Proof.** Each term of the Leibniz expansion is a product of one entry from each column. \(\square\)

**Lemma 1.4** (transfer of minor bounds). Let \(F\) be an \(n\times m\) matrix over \(\mathbb Q_p\) and suppose every full minor of \(F\) has valuation at least \(-\Theta\).

1. For every \(m\times n\) matrix \(T\) with entries in \(\mathbb Z_p\), \(v_p(\det(FT))\ge-\Theta\).
2. If \(U\) is an \(m\times m\) matrix with entries in \(\mathbb Z_p\) and \(\det U\) is a unit of \(\mathbb Z_p\), then every full minor of \(FU^{-1}\) has valuation at least \(-\Theta\). Equivalently: if all full minors of \(FU\) are bounded below by \(-\Theta\), so are those of \(F\).

**Proof.** (1) is Lemma 1.2, since the minors of \(T\) lie in \(\mathbb Z_p\). (2) The inverse \(U^{-1}=\operatorname{adj}(U)/\det U\) has entries in \(\mathbb Z_p\), and a full minor of \(FU^{-1}\) is \(\det(F\,(U^{-1})_{\text{cols}})\), to which (1) applies. \(\square\)

In this lesson and the next one, \(F\) is the \(n\times(n+q)\) matrix of raw columns \(F_j\), \(b\le j<L\), of [Chebyshev rows and mixed moments](chebyshev-rows-and-mixed-moments.md), and \(\Delta_N=\det(\mathcal F\mathcal T)\) with the integer matrix \(\mathcal T\) defined there. By Lemma 1.4(1), it suffices to bound all full minors of \(\mathcal F\).

## 2. A 2-adic version of the moments

From now on assume that \(G\) is rational, and regard it also as an element of \(\mathbb Q_2\). Constants that may depend on this rational number carry a subscript \(G\). Recall \(m_u=2/((u+1)c_{u/2})\) for even \(u\) and \(m_u=0\) for odd \(u\), with \(c_l=4^{-l}\binom{2l}l\).

**Lemma 2.1.** For even \(u\ge0\), \(v_2(m_u)=u+1-v_2\binom u{u/2}\ge u+1-\log_2(u+1)\).

**Proof.** \(m_u=2^{u+1}/\bigl((u+1)\binom u{u/2}\bigr)\) with \(u+1\) odd. Apply Lemma 1.1 with \(2l=u\). \(\square\)

For \(0\le i,j<H\) define, in \(\mathbb Q_2\),

\[
M_{\mathrm s}(i,j)=\sum_{k\ge0}\frac{m_{i+k}}{j+k+1}.
\tag{2.1}
\]

**Lemma 2.2.** The series (2.1) converges in \(\mathbb Q_2\), and \(v_2(M_{\mathrm s}(i,j))\ge i-2\log_2H-1\) for \(0\le i,j<H\).

**Proof.** By Lemma 2.1 a nonzero term has valuation at least \((i+k+1)-\log_2(i+k+1)-\log_2(j+k+1)\ge i+k+1-2\log_2(H+k)\). Since \(H+k\le H(k+1)\), this is at least \(i+1-2\log_2H+\bigl(k-2\log_2(k+1)\bigr)\), and \(k-2\log_2(k+1)\ge-2\) for every \(k\ge0\). The terms tend to zero, so the series converges, and the bound passes to the sum. \(\square\)

The same algebra that proved the recurrences of the real moments proves them for \(M_{\mathrm s}\): the diagonal identity \(M_{\mathrm s}(i,j)-M_{\mathrm s}(i+1,j+1)=m_i/(j+1)\) holds term by term, and the telescoping computations of Lemma 5.2 of [Chebyshev rows and mixed moments](chebyshev-rows-and-mixed-moments.md) go through because \(m_v\to0\) in \(\mathbb Q_2\) as well (Lemma 2.1). In particular the boundary values \(M_{\mathrm s}(d,0)\) and \(M_{\mathrm s}(0,d)\) satisfy the two boundary recurrences, and \(M_{\mathrm s}(1,0)=2\). Put

\[
e_1=4G-M_{\mathrm s}(0,0),\qquad e_2=-M_{\mathrm s}(0,1),
\]

two fixed elements of \(\mathbb Q_2\), independent of \(N\).

**Lemma 2.3.** For \(0\le i,j<H\),

\[
M^0(i,j)+4G\,c_{(i-j)/2}=M_{\mathrm s}(i,j)+e_1c_{(i-j)/2}+e_2c_{(j-i-1)/2}.
\]

**Proof.** Both sides satisfy the diagonal recurrence and, on the two boundary lines, the two boundary recurrences. For \(M^0\) this holds by its definition (5.1) of the previous lesson and the recurrences defining \(k^\pm\); for \(M_{\mathrm s}\) it was noted above; and the two kernels \(c_{(i-j)/2}\) and \(c_{(j-i-1)/2}\) depend only on \(i-j\) and solve the homogeneous boundary recurrences (proof of Proposition 5.4 there). They agree at the three starting values: at \((0,0)\) both equal \(4G\); at \((1,0)\) both equal \(2\); at \((0,1)\) the left side is \(k^+_1=0\) and the right side is \(M_{\mathrm s}(0,1)+e_2=0\). Diagonal reduction then gives agreement everywhere. \(\square\)

## 3. Three kinds of columns

Recall the raw columns \(F_j(r)=M(P_r,j)-\frac32Z(D_r,j)\) and their rational form from Proposition 6.1 of the previous lesson. Combining it with Lemma 2.3, and using the contact identity \(\sum_i[t^i]P_r\,c_{(j-i-1)/2}=[t^j]{}(tP_r/f)=[t^j]D_r\) for \(j<L\) to move the \(e_2\) term to the \(D\) side, we obtain for \(b\le j<L\)

\[
F_j=S_j+E_j+B_j,
\tag{3.1}
\]

with the column vectors

\[
S_j(r)=M_{\mathrm s}(P_r,j),\qquad E_j(r)=e_1\sum_i[t^i]P_r\,c_{(i-j)/2},\qquad B_j(r)=\sum_i[t^i]D_r\Bigl(e_2[i=j]-\frac32Z^0(i,j)\Bigr).
\]

If \(e_1=0\) or \(e_2=0\), the corresponding terms simply vanish.

**Coefficients of the rows.** Write

\[
\frac{P_r(t)}{(1-t)^h}=t^{C-1}T_d(1/t)=\sum_{u\ge0}p_{r,u}t^{C-1-u},\qquad \frac{D_r(t)}{(1-t)^h}=\sum_{u\ge0}d_{r,u}t^{C-1-u}.
\]

So \(p_{r,u}=[x^u]T_d\) and \(d_{r,u}=\pm[x^u]U_{d-1}\), with \(d=|r-g|\).

**Lemma 3.1.** \(v_2([x^u]T_d)\ge u-1\) and \(v_2([x^u]U_d)\ge u\) for all \(d,u\ge0\). Hence \(v_2(p_{r,u})\ge u-1\) and \(v_2(d_{r,u})\ge u-1\).

**Proof.** Induction on \(d\) with \([x^u]S_{d+1}=2[x^{u-1}]S_d-[x^u]S_{d-1}\): if the coefficients of \(S_d\) and \(S_{d-1}\) in degree \(u\) have valuation at least \(u-\epsilon\) (with \(\epsilon=1\) for \(T\) and \(0\) for \(U\)), so do those of \(S_{d+1}\). The initial cases \(T_0=1\), \(T_1=x\), \(U_0=1\), \(U_1=2x\) satisfy the bounds; in degree \(0\) only integrality is needed. \(\square\)

**Lemma 3.2.** Put \(L_2=\lfloor\log_2H\rfloor\). For \(0\le i,j<H\), \(v_2(Z^0(i,j))\ge-2L_2\). Every entry of every column \(S_j\) has valuation at least \(C-2\log_2H-3\).

**Proof.** The sums \(\sum_{k\le i}k^{-d}\) have valuation at least \(-dL_2\) term by term; dividing by \(i-j\) costs at most \(L_2\) more. For \(S_j\): the coefficient \([t^i]P_r\) is an integer combination of the \(p_{r,u}\) with \(u\ge C-1-i\), because \((1-t)^h\) only raises degrees; so \(v_2([t^i]P_r)\ge C-2-i\). Lemma 2.2 adds \(i-2\log_2H-1\). \(\square\)

**The exceptional columns.** Let \(\mathbf p_u=(p_{r,u})_{0\le r<n}\) and \(\mathbf d_u=(d_{r,u})_r\). Expanding \((1-t)^h\),

\[
E_j=\sum_u\mathbf p_u\,a_{u,j},\qquad B_j=\sum_u\mathbf d_u\,b_{u,j},
\]

\[
a_{u,j}=e_1\sum_{v=0}^h(-1)^v\binom hv\,c_{(C-1-u+v-j)/2},\qquad
b_{u,j}=\sum_{v=0}^h(-1)^v\binom hv\Bigl(e_2\,[C-1-u+v=j]-\frac32Z^0(C-1-u+v,j)\Bigr).
\]

Only \(u\) with \(\mathbf p_u\ne0\) or \(\mathbf d_u\ne0\) occur, and for them the indices \(C-1-u+v\) lie in \(\{0,\dots,H-1-u\}\). Fix an integer \(K_G\ge0\) with \(v_2(e_1),v_2(e_2)\ge-K_G\) (or ignore a vanishing \(e_i\)). Since \(v_2(c_l)\ge-2l\),

\[
v_2(a_{u,j})\ge u+j-H+1-K_G,\qquad v_2(b_{u,j})\ge-2L_2-1-K_G.
\tag{3.2}
\]

Indeed, in \(a_{u,j}\) the index \(l=(C-1-u+v-j)/2\) satisfies \(2l\le H-1-u-j\).

## 4. The estimate

**Proposition 4.1** (the prime two). Assume \(G\) rational. Put \(\delta=(q+g+h)/n=5/24\). For every \(N\ge1\),

\[
v_2(\Delta_N)\ge-\Bigl(\frac\delta2+\frac{\delta^2}8\Bigr)n^2-O_G\bigl(n\log(n+2)\bigr)=-\frac{505}{4608}n^2-O_G\bigl(n\log(n+2)\bigr),
\]

and the same bound holds for every full minor of the raw matrix \(\mathcal F\).

**Proof.** By Lemma 1.4(1) it suffices to treat a full minor of \(\mathcal F\), with distinct raw column indices \(j_1,\dots,j_n\in[b,L)\). Expand each column by (3.1), and expand the resulting determinant by multilinearity. Consider a term in which \(m\) columns are of type \(E\), \(l\) of type \(B\), and \(n-m-l\) of type \(S\). Expand the \(E\) columns through the vectors \(\mathbf p_u\) and the \(B\) columns through the vectors \(\mathbf d_u\). If two \(E\) columns use the same \(u\), the determinant has two proportional columns and vanishes; the same holds within the \(B\) group. So in a nonzero term the \(E\) columns use distinct values of \(u\), whose sum is at least \(0+1+\dots+(m-1)=m(m-1)/2\), and likewise the \(B\) columns have \(\sum u\ge l(l-1)/2\). The \(E\) columns also have distinct raw indices \(j\ge b\), so \(\sum j\ge mb+m(m-1)/2\).

By Lemma 1.3 and the bounds of Section 3, such a term has valuation at least

\[
\sum_{E}\bigl((u-1)+(u+j-H+1-K_G)\bigr)+\sum_{B}\bigl((u-1)-2L_2-1-K_G\bigr)+(n-m-l)\bigl(C-2\log_2H-3\bigr).
\]

Inserting the lower bounds for the sums, this is at least

\[
\Phi(m,l)-O_G\bigl(n\log(n+2)\bigr),\qquad \Phi(m,l)=\frac32m^2-(H-b)m+\frac12l^2+C(n-m-l),
\]

since all remaining terms are linear in \(m\) and \(l\) with coefficients \(O_G(\log(n+2))\). A finite sum of such terms obeys the same lower bound, so every full minor satisfies \(v_2\ge\min\Phi-O_G(n\log(n+2))\), the minimum over integers \(m,l\ge0\) with \(m+l\le n\). We bound this from below by the minimum over real \((m,l)\) in the same triangle.

For fixed \(m\), \(\partial\Phi/\partial l=l-C<0\) because \(l\le n<C\), so the minimum is at \(l=n-m\). There, using \(H-b=58N=(1+\delta)n\),

\[
\Phi(m,n-m)=2m^2-(2+\delta)nm+\frac{n^2}2=2\Bigl(m-\frac{(2+\delta)n}4\Bigr)^2-\Bigl(\frac\delta2+\frac{\delta^2}8\Bigr)n^2.
\]

With \(\delta=5/24\), \(\frac\delta2+\frac{\delta^2}8=\frac{480+25}{4608}=\frac{505}{4608}\). \(\square\)

The value \(\delta=(q+g+h)/n\) records how far the row degrees reach beyond the columns: \(H-b-n=q+g+h\). The quadratic term is the cost of the two transcendental starting values, paid through at most a few columns at a time. The next lesson treats the odd primes, where a different mechanism controls the denominators.

## 5. Exercises

**Exercise 5.1 (easy).** Compute \(v_2(m_u)\) for \(u=0,2,4,6,8\), and compare with Lemma 2.1.

**Exercise 5.2 (easy).** Verify Lemma 3.1 for \(T_4=8x^4-8x^2+1\) and \(U_4=16x^4-12x^2+1\).

**Exercise 5.3 (medium).** Prove the identity \(\Phi(m,n-m)=2m^2-(2+\delta)nm+n^2/2\) and locate the minimizing \(m\). Is it an admissible number of columns?

**Exercise 5.4 (medium).** Show that \(k-2\log_2(k+1)\ge-2\) for every integer \(k\ge0\), as used in Lemma 2.2.

**Exercise 5.5 (medium).** Show that \(v_2(c_l)=1-2l\) when \(l\) is a power of \(2\). Deduce from Lemma 2.3 that the difference \(M^0(i,j)+4G\,c_{(i-j)/2}-M_{\mathrm s}(i,j)\) has valuation about \(-|i-j|\) for suitable \(i,j\) when \(e_1\ne0\), whereas \(v_2(M_{\mathrm s}(i,j))\ge i-2\log_2H-1\). Explain the role of the columns of types \(E\) and \(B\).

## 6. Solutions

**5.1.** \(m_0=2\), \(m_2=4/3\), \(m_4=16/15\), \(m_6=32/35\), \(m_8=256/315\): valuations \(1,2,4,5,8\). Lemma 2.1: \(v_2\binom u{u/2}\) is \(0,1,1,2,1\), so \(u+1-v_2\binom u{u/2}\) is \(1,2,4,5,8\).

**5.2.** \(T_4\): coefficients \(1,-8,8\) in degrees \(0,2,4\), valuations \(0,3,3\ge-1,1,3\). \(U_4\): \(1,-12,16\), valuations \(0,2,4\ge0,2,4\).

**5.3.** \(\frac32m^2+\frac12(n-m)^2=2m^2-nm+\frac{n^2}2\), and \(-(H-b)m=-(1+\delta)nm\). The minimum is at \(m=(2+\delta)n/4=\frac{53}{96}n\), which lies in \([0,n]\); for the lower bound it does not matter whether it is an integer.

**5.4.** For \(k\le7\) check directly (the minimum is about \(-1.17\), near \(k=2\)). For \(k\ge7\), \(2\log_2(k+1)\le k\), because \(2^{k/2}\ge k+1\) there, by induction.

**5.5.** \(v_2(c_l)=v_2\binom{2l}l-2l\). For \(l=2^e\), in Lemma 1.1 the bracket \(\lfloor2l/2^k\rfloor-2\lfloor l/2^k\rfloor\) is \(1\) for \(k=e+1\) and \(0\) otherwise, so \(v_2(c_l)=1-2l\). By Lemma 2.3 the difference equals \(e_1c_{(i-j)/2}+e_2c_{(j-i-1)/2}\); for \(i-j=2^{e+1}\) only the first kernel is present, with valuation \(v_2(e_1)+1-(i-j)\). So individual entries can have denominators of order \(2^{|i-j|}\), while \(M_{\mathrm s}\) is \(2\)-adically small. The decomposition (3.1) puts these large denominators into the columns \(E_j\) and \(B_j\), whose expansions through the fixed vectors \(\mathbf p_u\) and \(\mathbf d_u\) show that a nonzero term of a minor can use only a few of them with large denominators; this is what the quadratic function \(\Phi\) counts.

## References

- [OpenAI-Catalan] OpenAI, Catalan's constant is irrational, preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf
