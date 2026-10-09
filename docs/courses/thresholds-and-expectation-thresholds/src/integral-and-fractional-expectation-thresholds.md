# Integral and fractional expectation thresholds

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A nontrivial increasing family \(\mathcal F\) on a finite set \(X\) has two expectation thresholds, defined in Section 2 of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md). The integral threshold \(q(\mathcal F)\) uses covers: families \(\mathcal G\) such that every member of \(\mathcal F\) contains a member of \(\mathcal G\). The fractional threshold \(q_f(\mathcal F)\) uses fractional covers: weights on subsets of \(X\) summing to at least \(1\) below every member of \(\mathcal F\). Every cover is a fractional cover, so \(q(\mathcal F)\le q_f(\mathcal F)\). In 2010 Talagrand conjectured that the two thresholds agree up to a universal constant factor [Tal]. This lesson presents OpenAI's proof of the conjecture [OpenAI-IF]:

**Theorem 4.1** (OpenAI 2026; Talagrand's conjecture). For every finite set \(X\) and every nontrivial increasing family \(\mathcal F\subseteq2^X\),
\[
q_f(\mathcal F)\le25\cdot512^4\,q(\mathcal F).
\]
More precisely, if some fractional cover of \(\mathcal F\) has cost at most \(\frac12\) at density \(r\in(0,1]\), then some cover of \(\mathcal F\) has cost at most \(\frac12\) at density \(r/(25\cdot512^4)\).

The constant does not depend on \(X\), on the sizes of the members of \(\mathcal F\), or on the sets carrying the fractional weights. Earlier results proved the comparison for special weights: Talagrand for weights on single elements, DeMarco and Kahn for clique-counting weights, Frankston, Kahn and Park for weights on pairs, and Fischer and Person for further classes. Dubroff, Kahn and Park, and then Pham, rounded fractional covers supported on sets of size at most \(t\) with a loss depending on \(t\), and Park obtained a loss of order \(\log\log(1/q(\mathcal F))\) [Park]. None of these results is used below.

The proof has two parts. Section 3 proves a *multiscale selector estimate* (Theorem 3.1): if \(\mathcal F\) admits no cheap cover, then a random colouring of \(X\) by \(1,2,\dots,s+1\), with colour \(i\) of probability \(256^ip\), typically has a single member \(H\in\mathcal F\) that captures most of a prescribed probability mass on \(H\) at every scale at once. Its proof develops the minimum-fragment method of Park and Pham [PP-S], Pham's towers of fragments [Pham] and the maximal truncations of Bednorz, Martynek and Meller [BMM]; the truncation lemma is Section 2. Section 4 turns a fractional cover into such masses, as Pham did [Pham], and compares two estimates of one expectation.

We use the notation of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md): \(\mu_p\), covers, the cost \(c_p\), and the thresholds \(q\) and \(q_f\). Empty sums are \(0\), empty products are \(1\), and \(p^0=1\) also for \(p=0\).

## 1. Small families

A family \(\mathcal F\subseteq2^X\), increasing or not, is *\(p\)-small* if it has a cover \(\mathcal G\) with \(c_p(\mathcal G)=\sum_{S\in\mathcal G}p^{|S|}\le\frac12\). If \(\mathcal F\) is \(p\)-small, it is \(p'\)-small for every \(p'\le p\), since costs are nondecreasing in \(p\); and any subfamily of a \(p\)-small family is \(p\)-small. For a nontrivial increasing family, \(q(\mathcal F)\) is the supremum of the \(p\) for which \(\mathcal F\) is \(p\)-small, and by Lemma 2.1 of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md), a \(p\)-small family has \(\mu_p(\mathcal F)\le\frac12\).

## 2. Maximal truncation

**Lemma 2.1** (maximal truncation). Let \(\lambda\) be a probability mass function on a finite set \(X\), let \(A\subseteq X\), \(m\ge0\) and \(0<d<1\). Call \(u\in[0,1]\) *admissible* if
\[
\{x:\lambda(x)>u\}\subseteq A\qquad\text{and}\qquad\sum_{x\in X}\min\{\lambda(x),u\}\bigl(\mathbf 1_A(x)-(1-d)\bigr)\ge mu.\tag{2.1}
\]
If an admissible \(u\) exists, there is a largest one, \(\varepsilon\), and \(|\{x:\lambda(x)>\varepsilon\}|\le m/d\).

**Proof.** The inclusion in (2.1) holds exactly when \(u\ge u_0=\max(\{\lambda(x):x\notin A\}\cup\{0\})\). Both sides of the inequality in (2.1) are continuous in \(u\). So the admissible set is a closed subset of \([u_0,1]\), compact and by assumption nonempty, and it has a largest element \(\varepsilon\). Let \(R=\{x:\lambda(x)>\varepsilon\}\). If \(\varepsilon=1\), then \(R=\varnothing\). Otherwise let
\[
f(u)=\sum_{x\in X}\min\{\lambda(x),u\}\bigl(\mathbf 1_A(x)-(1-d)\bigr)-mu.
\]
For \(u\) slightly larger than \(\varepsilon\), namely \(\varepsilon<u<\min(\{1\}\cup\{\lambda(x):x\in R\})\), the terms with \(\lambda(x)\le\varepsilon\) do not change, and each \(x\in R\) contributes \(u(\mathbf 1_A(x)-(1-d))=du\), because \(R\subseteq A\) by admissibility of \(\varepsilon\). So \(f\) has slope \(d|R|-m\) there. If \(d|R|>m\), then \(f(u)>f(\varepsilon)\ge0\) for such \(u\), and \(\{\lambda>u\}\subseteq R\subseteq A\); so \(u\) is admissible, contradicting the maximality of \(\varepsilon\). Hence \(d|R|\le m\). \(\square\)

## 3. A multiscale selector estimate

**Theorem 3.1** (multiscale selector estimate; OpenAI). Let \(X\) be finite, let \(\mathcal F\) be a nonempty family of nonempty subsets of \(X\), and suppose that \(\mathcal F\) is not \(p\)-small, where \(0<p\le1\). For each \(H\in\mathcal F\) let \(\lambda_H\) be a probability mass function on \(X\) vanishing outside \(H\). Let \(D=256\) and let \(s\ge0\) be an integer with \(p\sum_{i=1}^sD^i\le\frac12\). Colour the elements of \(X\) independently by a random map \(a\colon X\to\{1,\dots,s+1\}\) with
\[
\pi_i=\mathbb P(a(x)=i)=D^ip\quad(1\le i\le s),\qquad\pi_{s+1}=1-p\sum_{i=1}^sD^i\ge\tfrac12.\tag{3.1}
\]
For a colouring \(v\) let \(A_i(v)=\{x:v(x)\le i\}\). Then with probability at least \(\frac9{10}\) there is \(H\in\mathcal F\) with
\[
\lambda_H\bigl(A_i(a)\bigr)\ge1-2^{-i}\qquad(1\le i\le s),\tag{3.2}
\]
where \(\lambda_H(A)=\sum_{x\in A}\lambda_H(x)\); for such an \(H\),
\[
\sum_{x\in X}a(x)\,\lambda_H(x)\le2.\tag{3.3}
\]

The point of (3.2) is that one member \(H\) works at all scales \(i\) simultaneously. The bound (3.3) follows from (3.2): since \(a(x)=\sum_{i=0}^s\mathbf 1\{a(x)>i\}\),
\[
\sum_xa(x)\lambda_H(x)=\sum_{i=0}^s\lambda_H\bigl(X\setminus A_i(a)\bigr)=1+\sum_{i=1}^s\bigl(1-\lambda_H(A_i(a))\bigr)\le1+\sum_{i=1}^s2^{-i}\le2.
\]

**Proof.** If \(s=0\), every element has colour \(1\), (3.2) is empty, and any \(H\in\mathcal F\) works. Let \(s\ge1\) and \(d_i=2^{-i}\). A colouring is *bad* if no \(H\in\mathcal F\) satisfies (3.2); we show \(\mathbb P(a\text{ bad})\le\frac1{10}\).

*Moves.* A *move* of a colouring \(a\) is a colouring \(z\le a\) (pointwise): some elements receive earlier colours. Write
\[
U(a,z)=\{x:z(x)<a(x)\},\qquad m_i(a,z)=|A_i(z)\setminus A_i(a)|=|\{x:z(x)\le i<a(x)\}|,\qquad L(a,z)=\sum_x\bigl(a(x)-z(x)\bigr).
\]
The move is *feasible* if there are \(H\in\mathcal F\) and \(\varepsilon_1,\dots,\varepsilon_s\in[0,1]\) such that for every \(i\), with \(R_i=\{x:\lambda_H(x)>\varepsilon_i\}\),
\[
R_i\subseteq A_i(z)\qquad\text{and}\qquad\sum_{x\in X}\min\{\lambda_H(x),\varepsilon_i\}\bigl(\mathbf 1_{A_i(z)}(x)-(1-d_i)\bigr)\ge m_i(a,z)\,\varepsilon_i.\tag{3.4}
\]
That is, \(\varepsilon_i\) is admissible in the sense of Lemma 2.1 for \(\lambda=\lambda_H\), \(A=A_i(z)\), \(m=m_i(a,z)\) and \(d=d_i\). We say that \(H\) and the \(\varepsilon_i\) *witness* the feasibility.

*If the trivial move is feasible, \(a\) is not bad.* For \(z=a\), \(m_i=0\). Replacing \(\min\{\lambda_H(x),\varepsilon_i\}\) by \(\lambda_H(x)\) in (3.4) adds \((\lambda_H(x)-\varepsilon_i)d_i\ge0\) for each \(x\in R_i\subseteq A_i(a)\), and nothing for other \(x\). So \(\sum_x\lambda_H(x)(\mathbf 1_{A_i(a)}(x)-(1-d_i))\ge0\), that is, \(\lambda_H(A_i(a))\ge1-d_i\), for every \(i\) and the same \(H\).

*Minimal moves cover \(\mathcal F\).* Fix orders on the finite sets of colourings and of members of \(\mathcal F\). For every colouring \(a\) and every \(H_0\in\mathcal F\), choose, among the feasible moves \(z\) of \(a\) with \(U(a,z)\subseteq H_0\), one with \(L(a,z)\) as small as possible, the first in the order among these. Such moves exist: the move that gives colour \(1\) to the elements of \(H_0\) and keeps the other colours is feasible, witnessed by \(H=H_0\) and all \(\varepsilon_i=0\), because \(\{\lambda_{H_0}>0\}\subseteq H_0\subseteq A_i(z)\). The witness of a chosen move need not be \(H_0\). Let \(\mathcal Z(a)\) be the set of chosen moves. Each \(H_0\) contains the changed set of its chosen move, so \(\{U(a,z):z\in\mathcal Z(a)\}\) covers \(\mathcal F\); as \(\mathcal F\) is not \(p\)-small, \(\sum_{z\in\mathcal Z(a)}p^{|U(a,z)|}>\frac12\). Writing \(P(v)=\prod_x\pi_{v(x)}\) for the probability of a colouring \(v\),
\[
\tfrac12\,\mathbb P(a\text{ bad})\le\sum_{a\text{ bad}}P(a)\sum_{z\in\mathcal Z(a)}p^{|U(a,z)|}.\tag{3.5}
\]
For bad \(a\), every \(z\in\mathcal Z(a)\) has \(U(a,z)\neq\varnothing\), because the trivial move is not feasible.

*Profiles.* For a pair \((a,z)\) with \(z\le a\), its *profile* is the array \(n_{ih}=|\{x:z(x)=i,\ a(x)=h\}|\), \(1\le i<h\le s+1\). Put \(t_i=\sum_{h>i}n_{ih}\), the number of elements moved to colour \(i\), and \(t=\sum_{i=1}^st_i=|U(a,z)|\). The profile determines the numbers \(m_i(a,z)=\sum_{j\le i<h}n_{jh}\), so for fixed \(z\) the feasibility conditions (3.4) depend on \(a\) only through the profile.

Group the pairs \((a,z)\) occurring in (3.5) by \(z\) and the profile. In a group, take the first \(H\in\mathcal F\) that witnesses feasibility for these data, and for every \(i\) let \(\varepsilon_i\) be the largest admissible value for \(\lambda_H\), \(A_i(z)\), \(m_i\) and \(d_i\), which exists by Lemma 2.1. Then \(H\) and these \(\varepsilon_i\) witness the feasibility of \(z\) for every \(a\) of the group, and Lemma 2.1 gives
\[
|R_i|\le\frac{m_i(a,z)}{d_i}\le2^it.\tag{3.6}
\]

*Moved elements lie in the sets \(R_i\).* We claim that for every \((a,z)\) of the group,
\[
\{x:z(x)=i<a(x)\}\subseteq R_i\qquad(1\le i\le s).\tag{3.7}
\]
Suppose that \(z(x)=i<a(x)\) and \(x\notin R_i\). Let \(z'\) agree with \(z\) except that \(z'(x)=i+1\). Then \(z'\le a\), and \(U(a,z')\subseteq U(a,z)\subseteq H_0\), where \(z\) was chosen for \(H_0\). The set \(A_i(z')=A_i(z)\setminus\{x\}\), all other \(A_j\) are unchanged, \(m_i(a,z')=m_i(a,z)-1\) and the other \(m_j\) are unchanged. In test \(i\) of (3.4), the inclusion still holds because \(x\notin R_i\); the left side decreases by \(\min\{\lambda_H(x),\varepsilon_i\}\,(d_i+(1-d_i))\le\varepsilon_i\), and the right side decreases by exactly \(\varepsilon_i\). So \(H\) and the same \(\varepsilon_i\) witness the feasibility of \(z'\). But \(L(a,z')=L(a,z)-1\), contradicting the choice of \(z\).

*Counting.* Given \(z\) and the profile, the colouring \(a\) is determined by the sets \(\{x:z(x)=i<a(x)\}\), of sizes \(t_i\), and the original colours of their elements. By (3.7), the number of colourings \(a\) in the group is at most
\[
\prod_{i=1}^s\binom{|R_i|}{t_i}\binom{t_i}{(n_{ih})_{h>i}},\tag{3.8}
\]
where the second factor is a multinomial coefficient. Since \(\binom nk\le(\mathrm en/k)^k\) and by (3.6),
\[
\prod_{i=1}^s\binom{|R_i|}{t_i}\le\prod_{i:t_i>0}\Bigl(\frac{\mathrm e\,2^it}{t_i}\Bigr)^{t_i}\le\prod_{i=1}^s\bigl(\mathrm e\,4^i\bigr)^{t_i}.\tag{3.9}
\]
For the second inequality, put \(\alpha_i=t_i/t\). The weighted arithmetic–geometric mean inequality gives \(\prod_{i:t_i>0}(2^{-i}/\alpha_i)^{\alpha_i}\le\sum_{i:t_i>0}\alpha_i\cdot2^{-i}/\alpha_i\le1\); raising to the power \(t\) gives \(\prod_{i:t_i>0}(t/t_i)^{t_i}\le\prod_i2^{it_i}\).

Every pair of the group has the same value of \(p^tP(a)\): the colourings \(a\) and \(z\) differ exactly on the moved elements, so
\[
p^tP(a)=P(z)\prod_{i=1}^s\Bigl(\frac p{\pi_i}\Bigr)^{t_i}\prod_{i<h}\pi_h^{n_{ih}}.\tag{3.10}
\]
By (3.8)–(3.10), the pairs with given \(z\) and profile contribute at most
\[
P(z)\prod_{i=1}^s\Bigl[\Bigl(\frac{\mathrm e\,4^ip}{\pi_i}\Bigr)^{t_i}\binom{t_i}{(n_{ih})_{h>i}}\prod_{h>i}\pi_h^{n_{ih}}\Bigr]
\]
to the right side of (3.5). Sum this bound over all profiles with given row sums \(t_1,\dots,t_s\), occurring or not: by the multinomial theorem, row \(i\) gives \((\sum_{h>i}\pi_h)^{t_i}\le1\). Then sum over all colourings \(z\), using \(\sum_zP(z)=1\). Since \(\mathrm e\,4^ip/\pi_i=\mathrm e/64^i\), the right side of (3.5) is at most
\[
\sum_{\substack{t_1,\dots,t_s\ge0\\t_1+\dots+t_s>0}}\ \prod_{i=1}^s\Bigl(\frac{\mathrm e}{64^i}\Bigr)^{t_i}\le\sum_{\ell\ge1}\varrho^\ell=\frac\varrho{1-\varrho}<\frac1{20},\qquad\varrho=\sum_{i=1}^s\frac{\mathrm e}{64^i}<\frac{\mathrm e}{63}<\frac1{21},
\]
because every product with \(t_1+\dots+t_s=\ell\) appears, with a multinomial coefficient at least \(1\), in the expansion of \(\varrho^\ell\). With (3.5), \(\mathbb P(a\text{ bad})<\frac1{10}\). \(\square\)

## 4. Rounding a fractional cover

**Proof of Theorem 4.1.** Let \(D=256\), \(B=512\) and \(C=25B^4\). Let \(r\in(0,1]\), and let \(g\colon2^X\to[0,\infty)\) satisfy
\[
\sum_{S\subseteq H}g(S)\ge1\quad(H\in\mathcal F),\qquad\sum_{S\subseteq X}g(S)\,r^{|S|}\le\tfrac12.\tag{4.1}
\]
Let \(p=r/C\). We show that \(\mathcal F\) is \(p\)-small. This gives the second statement; since every \(r<q_f(\mathcal F)\) admits such a \(g\), it gives \(q(\mathcal F)\ge q_f(\mathcal F)/C\) (if \(q_f(\mathcal F)=0\) there is nothing to prove).

*Masses from the fractional cover.* The cost in (4.1) contains the term \(g(\varnothing)\), so \(g(\varnothing)\le\frac12\). For \(H\in\mathcal F\) put
\[
M_H=\sum_{\varnothing\neq S\subseteq H}g(S)\ge1-g(\varnothing)\ge\tfrac12,\qquad\lambda_H(x)=\frac1{M_H}\sum_{\substack{\varnothing\neq S\subseteq H\\x\in S}}\frac{g(S)}{|S|}.
\]
Each nonempty \(S\subseteq H\) spreads its weight \(g(S)\) equally over its elements, so \(\lambda_H\) is a probability mass function vanishing outside \(H\). The members of \(\mathcal F\) are nonempty, since \(\varnothing\notin\mathcal F\).

*The selector event.* Suppose that \(\mathcal F\) is not \(p\)-small. Let \(s\) be the largest integer \(\ge0\) with \(p\sum_{i=1}^sD^i\le\frac12\); it exists because the sums are unbounded. Theorem 3.1 gives an event \(\mathcal E\), of probability at least \(\frac9{10}\), on which some \(H\in\mathcal F\) satisfies \(\sum_xa(x)\lambda_H(x)\le2\). Put
\[
Y_x=B^{4-a(x)},\qquad Z=\sum_{\varnothing\neq S\subseteq X}g(S)\prod_{x\in S}Y_x\ge0.
\]

*Lower bound.* On \(\mathcal E\), with \(H\) as above and \(\bar a(S)=|S|^{-1}\sum_{x\in S}a(x)\),
\[
\frac1{M_H}\sum_{\varnothing\neq S\subseteq H}g(S)\,\bar a(S)=\sum_xa(x)\lambda_H(x)\le2.
\]
Markov's inequality for the probability distribution \(g(S)/M_H\) on the nonempty subsets of \(H\) shows that the sets with \(\bar a(S)\le4\) carry \(g\)-weight at least \(M_H/2\). For each of them \(\prod_{x\in S}Y_x=B^{|S|(4-\bar a(S))}\ge1\). Hence \(Z\ge M_H/2\ge\frac14\) on \(\mathcal E\), and
\[
\mathbb EZ\ge\tfrac14\,\mathbb P(\mathcal E)\ge\tfrac9{40}.\tag{4.2}
\]

*Upper bound.* By maximality of \(s\), \(\frac12<p\sum_{i=1}^{s+1}D^i\le2pD^{s+1}\), so \(B^{-(s+1)}\le D^{-(s+1)}<4p\). The \(Y_x\) are independent with common mean
\[
\mathbb EY_x=B^4\Bigl(p\sum_{i=1}^s\Bigl(\frac DB\Bigr)^i+\pi_{s+1}B^{-(s+1)}\Bigr)\le B^4\Bigl(p\sum_{i\ge1}2^{-i}+4p\Bigr)\le5B^4p=\frac r5,
\]
also when \(s=0\). A product over a nonempty set \(S\) of distinct independent variables has mean \((\mathbb EY_x)^{|S|}\), and \((r/5)^{|S|}\le r^{|S|}/5\) for \(|S|\ge1\). So
\[
\mathbb EZ=\sum_{\varnothing\neq S}g(S)\,(\mathbb EY_x)^{|S|}\le\frac15\sum_{\varnothing\neq S}g(S)\,r^{|S|}\le\frac1{10},\tag{4.3}
\]
which contradicts (4.2). Hence \(\mathcal F\) is \(p\)-small. \(\square\)

Combined with Proposition 2.2 of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md), \(q(\mathcal F)\le q_f(\mathcal F)\le25\cdot512^4\,q(\mathcal F)\). In particular, the theorem of Frankston, Kahn, Narayanan and Park, \(p_{\mathrm c}(\mathcal F)=O(q_f(\mathcal F)\log\ell(\mathcal F))\), and the theorem of Park and Pham, \(p_{\mathrm c}(\mathcal F)=O(q(\mathcal F)\log\ell(\mathcal F))\), are equivalent up to the value of the constant.

## 5. Exercises

**Exercise 5.1** (easy). Show that the hypothesis "\(\mathcal F\) is not \(p\)-small" cannot be dropped in Theorem 3.1: give \(X\), \(\mathcal F\), \(\lambda_H\), \(p\) and \(s\ge1\) for which the probability that some \(H\) satisfies (3.2) is less than \(\frac9{10}\).

**Exercise 5.2** (easy). Check that \(\varrho=\sum_{i\ge1}\mathrm e/64^i=\mathrm e/63\) and that \(\varrho/(1-\varrho)<\frac1{20}\). Which property of the colour probabilities \(\pi_i=256^ip\) makes the ratio \(\mathrm e\,4^ip/\pi_i\) summable, and what is the role of the factor \(4^i\)?

**Exercise 5.3** (medium). Let \(1\le k\le N=|X|\) and \(\mathcal F=\{H\subseteq X:|H|\ge k\}\). Show that \(g(\{x\})=\frac1k\) defines a fractional cover with cost \(Nr/k\), so that \(q_f(\mathcal F)\ge k/(2N)\), and that \(q(\mathcal F)\ge\frac1{\mathrm e}\cdot\frac kN\cdot2^{-1/k}\) by the cover of all \(k\)-element sets. (The fractional cover is supported on single elements while the minimal members of \(\mathcal F\) have \(k\) elements.)

**Exercise 5.4** (medium). In the proof of Theorem 4.1, where are the following used: (a) \(B\ge2D\); (b) the factor \(4\) in the exponent \(4-a(x)\); (c) the bound \(\pi_{s+1}\le1\)? Show that with \(B=D\) the mean \(\mathbb EY_x\) would not be bounded by a constant multiple of \(p\) uniformly in \(s\).

## 6. Solutions

**5.1.** Let \(X=\{x\}\), \(\mathcal F=\{\{x\}\}\), \(\lambda_{\{x\}}(x)=1\), and \(p=2^{-20}\), \(s=1\). Then (3.2) says \(a(x)=1\), which has probability \(\pi_1=256p<\frac9{10}\). Here \(\mathcal F\) is \(p\)-small: the cover \(\{\{x\}\}\) costs \(p\le\frac12\).

**5.2.** \(\sum_{i\ge1}64^{-i}=\frac1{63}\), and \(\varrho/(1-\varrho)=\mathrm e/(63-\mathrm e)<0.046<0.05\). The ratio is \(\mathrm e\,4^ip/(256^ip)=\mathrm e\,64^{-i}\): the colour probabilities grow faster than the factors \(4^i\), which come from \(|R_i|\le2^it\) and the arithmetic–geometric mean step. Those factors in turn come from the capture targets \(1-2^{-i}\) through \(d_i=2^{-i}\) in Lemma 2.1.

**5.3.** A set \(H\) with \(|H|\ge k\) has \(\sum_{x\in H}g(\{x\})\ge1\), and the cost is \(\sum_xr/k=Nr/k\), at most \(\frac12\) for \(r\le k/(2N)\). The \(k\)-element sets form a cover of cost \(\binom Nkp^k\le(\mathrm eNp/k)^k\), at most \(\frac12\) when \(p\le\frac{k}{\mathrm eN}2^{-1/k}\).

**5.4.** (a) It gives \((D/B)^i\le2^{-i}\), so the first sum in \(\mathbb EY_x\) is at most \(p\). (b) Markov's inequality gives sets with average colour at most \(4\), where \(\prod Y_x\ge1\). (c) It bounds the last term by \(B^4B^{-(s+1)}<4B^4p\). With \(B=D\), the first sum would be \(B^4ps\), and \(s\) grows like \(\log_{256}(1/p)\).

## References

- [OpenAI-IF] OpenAI, *Integral and fractional expectation thresholds are equivalent*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/Integral-and-fractional-expectation-thresholds-are-equivalent-September-23-2026
- [PP-S] J. Park and H. T. Pham, *On a conjecture of Talagrand on selector processes and a consequence on positive empirical processes*, Annals of Mathematics 199 (2024), 1293–1321. https://arxiv.org/abs/2204.10309
- [Pham] H. T. Pham, *A sharp version of Talagrand's selector process conjecture and an application to rounding fractional covers*, Proceedings of STOC 2025, 322–328; expanded version *A sharp version of Talagrand's selector process conjecture, with applications to rounding fractional covers and Bernoulli Sudakov minoration*. https://arxiv.org/abs/2412.03540
- [BMM] W. Bednorz, R. Martynek and R. Meller, *The suprema of selector processes with the application to positive infinitely divisible processes*, 2022–2026. https://arxiv.org/abs/2212.14636
- [Park] J. Park, *A dimension-free comparison between expectation thresholds and fractional expectation thresholds*, 2026. https://arxiv.org/abs/2609.14681
- [Tal] M. Talagrand, *Are many small sets explicitly small?*, Proceedings of STOC 2010, 13–36. https://michel.talagrand.net/preprints/small.pdf
