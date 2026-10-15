# Averaging within a cell

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In the proof of the main theorem of [PSD factorizations and semidefinite lifts](psd-factorizations-and-semidefinite-lifts.md), the vertices of \(K_n\) are grouped into cells of a fixed even size \(k\). An odd cut of \(K_n\) is then restricted to each cell: its values at \(d\) chosen vertices of the cell, the terminals, are prescribed, and it takes equal values at the two ends of each edge of a perfect matching of the other vertices. This lesson studies the average of a function over such restrictions, when the terminals and the matching are chosen at random. The average has the uniform distribution as its marginal, and its variance over the random choice tends to zero as \(k\) grows, by a factor that does not depend on the function or, for matrix-valued functions, on their dimensions [OpenAI-PSD, Section 2].

- The restrictions and the averaging operators (Section 1).
- Estimates for binomial coefficients (Section 2).
- The two-sample kernel and its trace (Section 3).
- Invariant subspaces of large dimension (Section 4).
- The local averaging theorem (Section 5).

## 1. Restrictions of a cut to one cell

Fix an even integer \(d\ge2\) and an even integer \(k\), large in terms of \(d\) as specified in Section 5. A cell has the vertex set \([k]\). For \(b\in\{0,1\}\), let \(w\) be the unique integer in \(\{k/2,k/2+1\}\) with \(w\equiv b\pmod2\), and put
\[
\begin{gathered}X=\binom{[k]}{w},\qquad L=2^{d-1},\\ Y_b=\Bigl\{y\in\{0,1\}^d\mid\\ \textstyle\sum_\ell y_\ell\equiv b\pmod2\Bigr\}.\end{gathered}
\]
Thus \(X\) is the set of subsets of \([k]\) with \(w\) elements, and \(|Y_b|=L\). We identify a subset \(a\in X\) with its indicator function \(\mathbf 1_a\).

*Local column data* \(m\) consist of an ordered list \((v_1,\ldots,v_d)\) of distinct vertices, the *terminals*, and a perfect matching of the remaining \(k-d\) vertices, whose edges are the *internal pairs*. Let \(\mathcal M\) be the finite set of local column data. For \(y\in Y_b\), let \(\pi^m_y\) be the uniform probability measure on the set of \(a\in X\) with
\[
\begin{gathered}\mathbf 1_a(v_\ell)=y_\ell\quad(1\le\ell\le d),\\ \mathbf 1_a(u)=\mathbf 1_a(v)\ \text{ for each}\\ \text{internal pair }\{u,v\}.\end{gathered}\tag{1.1}
\]
To see that this set is nonempty, put
\[
\begin{gathered}s=|y|=\sum_\ell y_\ell,\\ h=\frac{k-d}2,\\ g=\frac{w-s}2 .\end{gathered}\tag{1.2}
\]
Since \(w\equiv b\equiv s\pmod2\), the number \(g\) is an integer. A set satisfying (1.1) consists of the \(s\) terminals with \(y_\ell=1\) and of \(g\) whole internal pairs among the \(h\) internal pairs. With \(\varepsilon=w-k/2\in\{0,1\}\),
\[
\begin{gathered}g=\frac h2+\frac d4+\frac\varepsilon2-\frac s2,\\ \Bigl|g-\frac h2\Bigr|\le\kappa,\\ \kappa=\frac d4+\frac12 ,\end{gathered}\tag{1.3}
\]
because \(0\le s\le d\). So \(0\le g\le h\) as soon as \(h\ge2\kappa\), and then the support of \(\pi^m_y\) has \(\binom hg\) elements.

For a real function \(B\) on \(X\), put
\[
\begin{gathered}(T_yB)(m)=\sum_{a\in X}\pi^m_y(a)B(a)\\ (m\in\mathcal M).\end{gathered}
\]
The same formula applies entrywise to matrix-valued functions. Expectations over \(a\) and over \(m\) refer to the uniform probability measures on \(X\) and on \(\mathcal M\), and \(\mathbb E_aB=\mathbb E_aB(a)\).

## 2. Estimates for binomial coefficients

For \(v\ge0\) put \(\alpha_v=\binom{2v}v4^{-v}\).

**Lemma 2.1.** For every integer \(v\ge0\),
\[
\frac1{2\sqrt{v+1}}\le\alpha_v\le\frac1{\sqrt{v+1}} .
\]

*Proof.* We have \(\alpha_0=1\) and \(\alpha_{v+1}/\alpha_v=(2v+1)/(2v+2)\), so \(\alpha_v=\prod_{i=1}^v\frac{2i-1}{2i}\). Then
\[
(2v+1)\alpha_v^2=\prod_{i=1}^v\frac{(2i-1)(2i+1)}{(2i)^2}\le1,
\]
since \((2i-1)(2i+1)=4i^2-1\). This gives \(\alpha_v\le(2v+1)^{-1/2}\le(v+1)^{-1/2}\). For the lower bound, \(4v\alpha_v^2\) equals \(1\) at \(v=1\) and does not decrease, since
\[
\frac{4(v+1)\alpha_{v+1}^2}{4v\alpha_v^2}=\frac{(2v+1)^2}{4v(v+1)}\ge1 .
\]
So \(\alpha_v\ge(4v)^{-1/2}\ge\frac12(v+1)^{-1/2}\) for \(v\ge1\), and the bound holds at \(v=0\) as well. \(\square\)

**Lemma 2.2.** For integers \(0\le j\le u\),
\[
\begin{aligned}\frac{\binom uj^2}{\binom{2u}{2j}}&=\frac{\binom{2j}j\binom{2u-2j}{u-j}}{\binom{2u}u}\\&\le2\sqrt{\frac{u+1}{(j+1)(u-j+1)}} .\end{aligned}
\]

*Proof.* Writing all binomial coefficients with factorials, both sides of the identity equal
\[
\frac{u!^2\,(2j)!\,(2u-2j)!}{j!^2\,(u-j)!^2\,(2u)!}.
\]
In terms of Lemma 2.1, the middle expression is \(\alpha_j\alpha_{u-j}/\alpha_u\), and the bounds of that lemma give the inequality. \(\square\)

**Lemma 2.3.** Let \(h\ge8\kappa(\kappa+1)\), where \(\kappa\ge1\), and let \(g\) be an integer with \(|g-h/2|\le\kappa\). Then
\[
\binom hg\ge\frac{2^h}{4\sqrt{h+2}} .
\]

*Proof.* Let \(m=\lfloor h/2\rfloor\). If \(h=2v\), Lemma 2.1 gives \(\binom hm=4^v\alpha_v\ge2^h/(2\sqrt{v+1})\). If \(h=2v+1\), then \(\binom{2v+2}{v+1}=2\binom{2v+1}v\), and Lemma 2.1 gives \(\binom hm\ge2^h/(2\sqrt{v+2})\). In both cases \(\binom hm\ge2^h/(2\sqrt{h+2})\).

Put \(q=(h/2-\kappa)/(h/2+\kappa)\in(0,1)\). If \(g>m\), then \(\binom hg/\binom hm\) is the product of the factors \((h-i)/(i+1)\), \(m\le i\le g-1\); there are \(g-m\le\kappa+1\) of them, and each is at least \((h/2-\kappa+1)/(h/2+\kappa)\ge q\). If \(g<m\), the ratio is the product of the factors \((i+1)/(h-i)\), \(g\le i\le m-1\); there are \(m-g\le\kappa\) of them, and each is at least \(q\), because \(i\ge h/2-\kappa\) and \(h-i\le h-g\le h/2+\kappa\). By Bernoulli's inequality, in all cases
\[
\frac{\binom hg}{\binom hm}\ge q^{\kappa+1}\ge1-\frac{2\kappa(\kappa+1)}{h/2+\kappa}\ge\frac12 ,
\]
the last step by \(h\ge8\kappa(\kappa+1)\). \(\square\)

## 3. The two-sample kernel and its trace

Fix \(b\) and \(y\in Y_b\), write \(T=T_y\), and suppose \(h\ge8\kappa(\kappa+1)\). Equip the real functions on \(X\) and on \(\mathcal M\) with the inner products for the uniform probability measures, and put \(K=T^*T\), a positive semidefinite self-adjoint operator on functions on \(X\). Let \(N=|X|\).

Sample \(m\) uniformly, and then \(a,a'\in X\) independently from \(\pi^m_y\). Let \(J(a,a')\) be the probability of the outcome \((a,a')\), and put \(D(a,a')=N^2J(a,a')\), the density of this law relative to two independent uniform elements of \(X\).

**Lemma 3.1.** The operator \(K\) satisfies:

1. \((KB)(a)=N^{-1}\sum_{a'}D(a,a')B(a')\); in particular \(K\) has the matrix entries \(D(a,a')/N\), and \(K1=1\) if \(\mathbb E_m\pi^m_y(a)=1/N\) for every \(a\).
2. \(D(a,a')\) depends only on \(|a\cap a'|\). It vanishes unless \(|a\cap a'|=w-2j\) for some \(0\le j\le g_*\), where \(g_*=\min(g,h-g)\), and in that case \(D(a,a')=P_j/Q_j\) with
\[
\begin{gathered}P_j=\frac{\binom gj\binom{h-g}j}{\binom hg},\\ Q_j=\frac{\binom w{2j}\binom{k-w}{2j}}{\binom kw}.\end{gathered}
\]
3. The trace of \(K^2\) is given by the formula (3.1) below.

\[
\begin{gathered}\operatorname{tr}(K^2)=\sum_{j=0}^{g_*}\frac{P_j^2}{Q_j}=\frac{\binom kw}{\binom hg^2}\\ \cdot\sum_{j=0}^{g_*}\frac{\binom gj^2\binom{h-g}j^2}{\binom w{2j}\binom{k-w}{2j}} .\end{gathered}\tag{3.1}
\]

*Proof.* (1) For real functions \(B_1,B_2\) on \(X\), by the definition of \(J\),
\[
\begin{aligned}\langle B_1,KB_2\rangle&=\langle TB_1,TB_2\rangle\\&=\mathbb E_m\bigl[(TB_1)(m)\,(TB_2)(m)\bigr]\\&=\sum_{a,a'}J(a,a')B_1(a)B_2(a'),\end{aligned}
\]
and \(\langle B_1,KB_2\rangle=N^{-1}\sum_aB_1(a)(KB_2)(a)\). Comparing gives the formula for \(KB_2\). For \(B=1\) it gives \((K1)(a)=N\sum_{a'}J(a,a')\), which is \(N\,\mathbb E_m\pi^m_y(a)\).

(2) A permutation \(\sigma\) of \([k]\) acts on local column data by relabeling, and \(\pi^{\sigma m}_y(\sigma a)=\pi^m_y(a)\). Since \(m\mapsto\sigma m\) preserves the uniform measure, \(J(\sigma a,\sigma a')=J(a,a')\). The permutations act transitively on the pairs \((a,a')\) with a given \(|a\cap a'|\), so \(D\) depends only on \(|a\cap a'|\). Conditional on \(m\), the sets \(a,a'\) contain the same \(s\) terminals and two independent uniform choices of \(g\) of the \(h\) internal pairs. If the second choice keeps exactly \(g-j\) pairs of the first, then \(|a\cap a'|=s+2(g-j)=w-2j\); this happens with probability \(P_j\), since one chooses the \(g-j\) kept pairs and \(j\) of the \(h-g\) other pairs. For two independent uniform elements of \(X\), the intersection has \(w-2j\) elements with probability \(Q_j\). Both laws are invariant, hence uniform on the pairs with a given intersection size, so the density on that class is \(P_j/Q_j\). Here \(Q_j>0\), because \(w=2g+s\ge2j\) and \(k-w=2(h-g)+(d-s)\ge2j\). On the classes with other intersection sizes the joint law vanishes.

(3) Since \(D\) is symmetric, \(\operatorname{tr}(K^2)=N^{-2}\sum_{a,a'}D(a,a')^2\). The class of pairs with \(|a\cap a'|=w-2j\) has \(N^2Q_j\) elements, so this equals \(\sum_jQ_j(P_j/Q_j)^2\). \(\square\)

**Proposition 3.2** (the trace estimate). If \(h\ge8\kappa(\kappa+1)\), then
\[
\operatorname{tr}(K^2)\le2^{d+9}\sqrt{h+1}\,\bigl(1+\log(h+1)\bigr).
\]

*Proof.* *The prefactor.* The largest binomial coefficient \(\binom k{k/2}\) is at most \(2^k/\sqrt{k/2+1}\le2^k/\sqrt{h+1}\) by Lemma 2.1, and Lemma 2.3, with (1.3), gives \(\binom hg^2\ge4^h/(16(h+2))\). Since \(k=2h+d\) and \(h+2\le2(h+1)\),
\[
\begin{aligned}\frac{\binom kw}{\binom hg^2}&\le\frac{2^{2h+d}}{\sqrt{h+1}}\cdot\frac{16(h+2)}{4^h}\\&\le2^{d+5}\sqrt{h+1} .\end{aligned}
\]

*The sum.* Since \(w\ge2g\) and \(k-w\ge2(h-g)\), we have \(\binom w{2j}\ge\binom{2g}{2j}\) and \(\binom{k-w}{2j}\ge\binom{2(h-g)}{2j}\). Lemma 2.2 with \(u=g\) and with \(u=h-g\) bounds the \(j\)-th term of the sum in (3.1) by
\[
\begin{aligned}&\frac{4\sqrt{(g+1)(h-g+1)}}{(j+1)\sqrt{(g-j+1)(h-g-j+1)}}\\&\quad\le\frac{2(h+2)}{(j+1)(g_*-j+1)} ,\end{aligned}
\]
using \(\sqrt{(g+1)(h-g+1)}\le(h+2)/2\) and \(g-j+1,\ h-g-j+1\ge g_*-j+1\). The partial fractions
\[
\begin{aligned}&\frac1{(j+1)(g_*-j+1)}\\&\quad=\frac1{g_*+2}\Bigl(\frac1{j+1}+\frac1{g_*-j+1}\Bigr)\end{aligned}
\]
give
\[
\begin{aligned}&\sum_{j=0}^{g_*}\frac1{(j+1)(g_*-j+1)}\\&\quad=\frac2{g_*+2}\sum_{i=1}^{g_*+1}\frac1i\\&\quad\le\frac{2(1+\log(h+1))}{g_*+2} .\end{aligned}
\]
By (1.3), \(g_*\ge h/2-\kappa\ge h/4\), so \(2(h+2)\cdot2/(g_*+2)\le16\), and the sum in (3.1) is at most \(16(1+\log(h+1))\). Multiplying by the prefactor proves the estimate. \(\square\)

## 4. Invariant subspaces of large dimension

The symmetric group \(S_k\) acts on \(X\) and, by \((\sigma B)(a)=B(\sigma^{-1}a)\), by orthogonal operators on the real functions on \(X\).

**Lemma 4.1.** Let \(k\ge6\) be even and \(w\in\{k/2,k/2+1\}\). Every nonzero \(S_k\)-invariant subspace \(V\) of real functions on \(X\) that is orthogonal to the constants has dimension at least \(k/2\).

*Proof.* Choose \(k/2\) disjoint transpositions \(\tau_1,\ldots,\tau_{k/2}\), the swaps of the two vertices of \(k/2\) disjoint pairs. They act on \(V\) as commuting orthogonal involutions, so \(V\) is the orthogonal direct sum of their joint eigenspaces \(V_\epsilon\), \(\epsilon\in\{1,-1\}^{k/2}\). A permutation \(\sigma\) that maps the pairs to the pairs, with \(\sigma\tau_i\sigma^{-1}=\tau_{\beta(i)}\) for a permutation \(\beta\) of \(\{1,\ldots,k/2\}\), maps \(V_\epsilon\) into \(V_{\epsilon'}\) with \(\epsilon'_{\beta(i)}=\epsilon_i\), and it maps \(V\) into itself.

Suppose that some \(V_\epsilon\ne0\) has exactly \(j\) entries \(-1\), with \(0<j<k/2\). Every pattern with \(j\) entries \(-1\) is of the form \(\epsilon'\) above, so all \(\binom{k/2}j\) of these joint eigenspaces are nonzero, and they are mutually orthogonal. Hence \(\dim V\ge\binom{k/2}j\ge k/2\).

Otherwise every nonzero \(V_\epsilon\) has a constant pattern, all entries \(1\) or all entries \(-1\), and the product of any two of the \(\tau_i\) acts as the identity on \(V\). Any product of two disjoint transpositions is \(\sigma\tau_1\tau_2\sigma^{-1}\) for some \(\sigma\in S_k\), and since \(\sigma^{-1}\) maps \(V\) into itself, it also acts as the identity on \(V\). For five distinct labels \(p,q,r,x,z\),
\[
\bigl[(p\,q)(x\,z)\bigr]\bigl[(q\,r)(x\,z)\bigr]=(p\,q)(q\,r),
\]
a cycle of length three. So every cycle of length three, and with them the alternating group \(A_k\), acts as the identity on \(V\). The group \(A_k\) acts transitively on \(X\): if \(\sigma a=a'\) with \(\sigma\) odd, then \(\sigma\) composed with a transposition of two elements of \(a\) is even and also maps \(a\) to \(a'\), and \(a\) has \(w\ge3\) elements. So every function in \(V\) is constant, and as it is orthogonal to the constants, it vanishes. This contradicts \(V\ne0\). \(\square\)

## 5. The local averaging theorem

**Theorem 5.1** (local averaging; [OpenAI-PSD, Lemma 2.1]). Let \(d\ge2\) be even, put \(\kappa=d/4+1/2\), and let \(k\ge d+16\kappa(\kappa+1)\) be even. Put
\[
\theta_d(k)=2^{(d+10)/2}\,k^{-1/4}\bigl(1+\log k\bigr)^{1/2}.
\]
For both \(b\in\{0,1\}\) and every \(y\in Y_b\):

1. \(\mathbb E_m\pi^m_y(a)=1/|X|\) for every \(a\in X\).
2. Every real function \(B\) on \(X\) satisfies
\[
\begin{aligned}&\mathbb E_m\bigl|(T_yB)(m)-\mathbb E_aB\bigr|^2\\&\quad\le\theta_d(k)\,\mathbb E_a\bigl|B(a)-\mathbb E_aB\bigr|^2 .\end{aligned}
\]
3. For all positive integers \(p,q\), every \(B\colon X\to\mathbb R^{p\times q}\) satisfies
\[
\begin{aligned}&\mathbb E_m\|(T_yB)(m)-\mathbb E_aB\|_{\mathrm F}^2\\&\quad\le\theta_d(k)\,\mathbb E_a\|B(a)-\mathbb E_aB\|_{\mathrm F}^2\\&\quad\le\theta_d(k)\,\mathbb E_a\|B(a)\|_{\mathrm F}^2 .\end{aligned}
\]

In particular \(\theta_d(k)\to0\) as \(k\to\infty\).

*Proof.* The bound on \(k\) gives \(h=(k-d)/2\ge8\kappa(\kappa+1)\ge16\), so \(0\le g\le h\) and \(k\ge6\).

(1) The law of \(a\) obtained by sampling \(m\) uniformly and then \(a\sim\pi^m_y\) is invariant under all permutations of \([k]\), by the equivariance in the proof of Lemma 3.1(2). Since \(S_k\) acts transitively on \(X\), this law is uniform.

(2) By part 1 and Lemma 3.1(1), \(K1=1\). As \(K\) is self-adjoint, it maps the orthogonal complement \(1^\perp\) of the constants into itself, and \(\operatorname{tr}(K^2)\) is \(1\) plus the sum of the squares of the eigenvalues of \(K\) on \(1^\perp\). Let \(\mu\) be the largest eigenvalue of \(K\) on \(1^\perp\), with eigenspace \(V\subseteq1^\perp\) (if \(1^\perp=0\), there is nothing to prove). Since \(J\) is invariant under permutations, \(K\) commutes with the action of \(S_k\), so \(V\) is invariant, and Lemma 4.1 gives \(\dim V\ge k/2\). Therefore, by Proposition 3.2 and \(h+1\le k\),
\[
\begin{aligned}\frac k2\mu^2&\le\operatorname{tr}(K^2)-1\\&\le2^{d+9}\sqrt k\,(1+\log k),\end{aligned}
\]
so \(0\le\mu\le\theta_d(k)\). For \(B_0=B-\mathbb E_aB\in1^\perp\) we have \(T_yB-\mathbb E_aB=T_yB_0\) (as \(T_y1=1\)), and
\[
\mathbb E_m|T_yB_0|^2=\langle B_0,KB_0\rangle\le\mu\,\mathbb E_a|B_0|^2 .
\]

(3) Apply part 2 to each entry and sum over the entries; then use \(\mathbb E_a\|B-\mathbb E_aB\|_{\mathrm F}^2=\mathbb E_a\|B\|_{\mathrm F}^2-\|\mathbb E_aB\|_{\mathrm F}^2\). \(\square\)

The constant in part 3 is the same in every matrix dimension. The theorem also applies after fixing auxiliary data, as long as the fixed data determine the whole function \(B\) on \(X\) before \(m\) is sampled and \(m\) remains uniform: the inequality then holds for each fixing, and averaging over the fixings introduces no factor that depends on \(B\) or on its dimensions. This is how the theorem is used in [Fourier smoothing of matrix squares](fourier-smoothing-of-matrix-squares.md), where conditioning on other cells selects an arbitrary function on the present cell.

The proof combines an upper bound for \(\operatorname{tr}(K^2)\) with a lower bound for the multiplicity of every nonconstant eigenvalue; a similar use of multiplicities appears in Gowers's work on quasirandom groups [Gowers 2008].

## 6. Exercises

**6.1.** Let \(k=8\), \(d=2\), \(b=0\) and \(y=(0,0)\). Compute \(w\), \(h\), \(g\), the numbers \(P_j\) and \(Q_j\), and \(\operatorname{tr}(K^2)\) from (3.1).

**6.2.** Show that \(\binom mj\ge m\) for integers \(1\le j\le m-1\).

**6.3.** In the setting of Section 1, suppose that the terminals \(v_1,\ldots,v_d\) are fixed and only the matching of the other vertices is random. Show that the marginal of \(a\) is not uniform on \(X\).

**6.4.** Show that \(\mathbb E_m\pi^m_y(a)\pi^m_y(a')\), as a function of \((a,a')\), is invariant under every permutation of \([k]\) applied to both arguments.

**6.5.** Let \(T\colon V_1\to V_2\) be a linear map between finite-dimensional inner product spaces, and \(K=T^*T\). Show that \(\|T\|_{\mathrm{op}}^2\) equals the largest eigenvalue of \(K\).

## 7. Solutions

**6.1.** Here \(k/2=4\) is even, so \(w=4\); \(s=0\), \(h=3\) and \(g=2\), with \(g_*=1\). Then \(P_0=\binom20\binom10/\binom32=\frac13\) and \(P_1=\binom21\binom11/\binom32=\frac23\), while \(\binom84=70\), \(Q_0=\binom40^2/70=\frac1{70}\) and \(Q_1=\binom42^2/70=\frac{36}{70}\). Hence
\[
\begin{aligned}\operatorname{tr}(K^2)&=\frac{1/9}{1/70}+\frac{4/9}{36/70}\\&=\frac{70}9+\frac{70}{81}=\frac{700}{81}.\end{aligned}
\]

**6.2.** For \(1\le j\le m-1\), \(\binom mj=\binom m{j-1}\frac{m-j+1}j\), and the sequence \(\binom mj\) increases up to the middle and is symmetric; its smallest value on \(1\le j\le m-1\) is \(\binom m1=m\).

**6.3.** The vertex \(v_1\) lies in \(a\) exactly when \(y_1=1\). So the probability that \(v_1\in a\) is \(0\) or \(1\), whereas under the uniform law on \(X\) it equals \(w/k\in(0,1)\).

**6.4.** For a permutation \(\sigma\), \(\pi^{\sigma m}_y(\sigma a)=\pi^m_y(a)\), since \(\sigma\) maps the sets satisfying (1.1) for \(m\) onto those for \(\sigma m\). As \(m\mapsto\sigma m\) is a bijection of \(\mathcal M\), averaging over \(m\) gives the claim.

**6.5.** For a unit vector \(B\), \(\|TB\|^2=\langle B,KB\rangle\). Expanding \(B\) in an orthonormal eigenbasis of the positive semidefinite operator \(K\) shows that this is at most the largest eigenvalue, with equality for a corresponding eigenvector.

## References

- [OpenAI-PSD] OpenAI, *Exponential PSD rank of positively shifted matching matrices*, OpenAI Math Release preprint, 5 October 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026
- [Gowers 2008] W. T. Gowers, *Quasirandom groups*, Combin. Probab. Comput. 17 (2008). https://arxiv.org/abs/0710.3877
