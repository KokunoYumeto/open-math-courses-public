# Random sets, covers and expectation thresholds

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Fix a graph \(H\), and let the random graph \(G(n,p)\) on the vertex set \([n]=\{1,\dots,n\}\) contain each possible edge independently with probability \(p\). How large must \(p\) be for \(G(n,p)\) to contain a copy of \(H\) with probability at least \(\frac12\)? There is an easy lower bound. If some subgraph \(F\) of \(H\) has fewer than \(\frac12\) copies in expectation, then \(F\), and with it \(H\), appears with probability less than \(\frac12\). The least \(p\) at which no subgraph is excluded in this way is the *expectation threshold* \(p_{\mathrm E}(n,H)\). In 2006 Kahn and Kalai conjectured that this first-moment obstruction is the only one up to a logarithmic factor: the containment threshold \(p_{\mathrm c}(n,H)\) is at most \(Kp_{\mathrm E}(n,H)\log n\) for a universal constant \(K\), whatever the graph \(H\) [KK]. This course presents the proof of the conjecture by OpenAI (2026) [OpenAI-KK2], in the sharper form \(p_{\mathrm c}(n,H)\le2048\,\mathrm e^{50}p_{\mathrm E}(n,H)\,(1+\log_2e(H))\), and three further results of OpenAI on expectation thresholds: integral and fractional expectation thresholds agree up to a constant factor, Talagrand's discrete convexity conjecture holds, and every graph splits into a bounded number of pieces that appear at a constant multiple of its integral expectation threshold.

This lesson sets up the language: random subsets of a finite set, increasing families and their thresholds, covers and expectation thresholds, the counting of copies of graphs, and the example of perfect matchings, which shows that a logarithmic factor cannot be avoided. Section 5 states the second Kahn–Kalai conjecture and describes the plan of the course.

Throughout, \(\log\) is the natural logarithm, \(\log_2\) the logarithm to base \(2\), and \(\mathrm e\) the base of the natural logarithm.

## 1. Random subsets and increasing families

Let \(X\) be a finite set. For \(0\le p\le1\), \(\mu_p\) denotes the law of a random subset \(W\subseteq X\) that contains each element independently with probability \(p\):
\[
\mu_p(W=Y)=p^{|Y|}(1-p)^{|X\setminus Y|}\qquad(Y\subseteq X).
\]
A family \(\mathcal F\) of subsets of \(X\) is *increasing* if \(A\in\mathcal F\) and \(A\subseteq A'\subseteq X\) imply \(A'\in\mathcal F\). It is *nontrivial* if \(\varnothing\neq\mathcal F\neq2^X\); an increasing family is nontrivial exactly when \(X\in\mathcal F\) and \(\varnothing\notin\mathcal F\). Write \(\mu_p(\mathcal F)=\mathbb P_{W\sim\mu_p}(W\in\mathcal F)\).

**Lemma 1.1** (monotone coupling). Let \((U_x)_{x\in X}\) be independent random variables, each uniform on \([0,1]\), and let \(W_p=\{x:U_x\le p\}\). Then \(W_p\) has law \(\mu_p\), and \(W_p\subseteq W_{p'}\) for \(p\le p'\). Consequently, for an increasing family \(\mathcal F\), the function \(p\mapsto\mu_p(\mathcal F)\) is a nondecreasing polynomial; if \(\mathcal F\) is nontrivial, it is strictly increasing on \([0,1]\), with \(\mu_0(\mathcal F)=0\) and \(\mu_1(\mathcal F)=1\).

**Proof.** The events \(\{x\in W_p\}=\{U_x\le p\}\) are independent and have probability \(p\), and \(U_x\le p\le p'\) gives \(W_p\subseteq W_{p'}\). For increasing \(\mathcal F\) this gives \(\{W_p\in\mathcal F\}\subseteq\{W_{p'}\in\mathcal F\}\), and \(\mu_p(\mathcal F)=\sum_{Y\in\mathcal F}p^{|Y|}(1-p)^{|X\setminus Y|}\) is a polynomial. Let \(\mathcal F\) be nontrivial and \(0\le p<p'\le1\). The event that \(p<U_x\le p'\) for every \(x\) has probability \((p'-p)^{|X|}>0\), and on it \(W_p=\varnothing\notin\mathcal F\) and \(W_{p'}=X\in\mathcal F\). Hence \(\mu_{p'}(\mathcal F)-\mu_p(\mathcal F)=\mathbb P(W_p\notin\mathcal F,\ W_{p'}\in\mathcal F)>0\). Finally \(\mu_0\) and \(\mu_1\) are concentrated on \(\varnothing\) and \(X\). \(\square\)

By continuity and Lemma 1.1, a nontrivial increasing family has a unique number \(p_{\mathrm c}(\mathcal F)\in(0,1)\) with \(\mu_{p_{\mathrm c}(\mathcal F)}(\mathcal F)=\frac12\), its *threshold*. Equivalently \(p_{\mathrm c}(\mathcal F)=\min\{p:\mu_p(\mathcal F)\ge\frac12\}\), and \(\mu_p(\mathcal F)>\frac12\) for every \(p>p_{\mathrm c}(\mathcal F)\).

**Lemma 1.2** (unions of independent product sets). If \(W_1,\dots,W_N\) are independent and \(W_i\) has law \(\mu_{p_i}\), then \(W_1\cup\dots\cup W_N\) has law \(\mu_{p_*}\) with \(1-p_*=\prod_i(1-p_i)\), and \(p_*\le\sum_ip_i\).

**Proof.** An element \(x\) lies outside \(\bigcup_iW_i\) exactly when \(x\notin W_i\) for every \(i\), which has probability \(\prod_i(1-p_i)\); these events for different \(x\) depend on disjoint collections of independent indicators, so they are independent. The inequality \(1-\prod_i(1-p_i)\le\sum_ip_i\) is the union bound for the events \(\{x\in W_i\}\). \(\square\)

## 2. Covers and expectation thresholds

Let \(\mathcal F\) be a nontrivial increasing family on \(X\). A *cover* of \(\mathcal F\) is a family \(\mathcal G\subseteq2^X\) such that every \(A\in\mathcal F\) contains some \(S\in\mathcal G\); its *cost* at density \(p\) is \(c_p(\mathcal G)=\sum_{S\in\mathcal G}p^{|S|}\). A *fractional cover* is a function \(g\colon2^X\to[0,\infty)\) with \(\sum_{S\subseteq A}g(S)\ge1\) for every \(A\in\mathcal F\); its cost is \(c_p(g)=\sum_Sg(S)p^{|S|}\). A cover \(\mathcal G\) is the same as the fractional cover \(g=\mathbf 1_{\mathcal G}\), with the same cost.

**Lemma 2.1** (first-moment bound). For every fractional cover \(g\) and every \(p\), \(\mu_p(\mathcal F)\le c_p(g)\). For a cover \(\mathcal G\), \(c_p(\mathcal G)\) is the expected number of members of \(\mathcal G\) contained in \(W\sim\mu_p\).

**Proof.** If \(W\in\mathcal F\) then \(\sum_{S\subseteq W}g(S)\ge1\). So \(\mathbf 1\{W\in\mathcal F\}\le\sum_Sg(S)\mathbf 1\{S\subseteq W\}\); take expectations, using \(\mathbb P(S\subseteq W)=p^{|S|}\). \(\square\)

The *expectation threshold* and the *fractional expectation threshold* of \(\mathcal F\) are
\[
q(\mathcal F)=\sup\{p\in[0,1]:c_p(\mathcal G)\le\tfrac12\text{ for some cover }\mathcal G\},\qquad q_f(\mathcal F)=\sup\{p\in[0,1]:c_p(g)\le\tfrac12\text{ for some fractional cover }g\}.
\]
Both sets contain \(p=0\): the family \(\mathcal F\) is a cover of itself, and \(c_0(\mathcal F)=0\) because \(\varnothing\notin\mathcal F\). Costs are nondecreasing in \(p\), so both sets are intervals starting at \(0\); Exercise 6.4 shows that they are closed.

**Proposition 2.2.** \(q(\mathcal F)\le q_f(\mathcal F)\le p_{\mathrm c}(\mathcal F)\).

**Proof.** Every cover is a fractional cover with the same cost, which gives the first inequality. If \(c_p(g)\le\frac12\) for a fractional cover \(g\), Lemma 2.1 gives \(\mu_p(\mathcal F)\le\frac12\), so \(p\le p_{\mathrm c}(\mathcal F)\) by Lemma 1.1. \(\square\)

Upper bounds for the expectation thresholds come from *spread* random members of \(\mathcal F\):

**Proposition 2.3** (spread members). Let \(\sigma>0\), and let \(A\) be a random member of \(\mathcal F\) such that \(\mathbb P(J\subseteq A)\le\sigma^{|J|}\) for every nonempty \(J\subseteq X\). Then \(q(\mathcal F)\le q_f(\mathcal F)\le\sigma\).

**Proof.** Let \(g\) be a fractional cover with \(c_p(g)\le\frac12\). Since \(A\in\mathcal F\), \(\sum_{S\subseteq A}g(S)\ge1\); taking expectations, \(1\le\sum_Sg(S)\,\mathbb P(S\subseteq A)\le\sum_Sg(S)\,\sigma^{|S|}\), where the term \(S=\varnothing\) is \(g(\varnothing)\) on both sides. If \(p\ge\sigma\), the right side is at most \(c_p(g)\le\frac12\), a contradiction. So \(p<\sigma\), and \(q_f(\mathcal F)\le\sigma\). \(\square\)

The *Kahn–Kalai conjecture* in its abstract form asserted that \(p_{\mathrm c}(\mathcal F)\le Kq(\mathcal F)\log\ell(\mathcal F)\) for a universal constant \(K\), where \(\ell(\mathcal F)\) is the maximum of \(2\) and the largest size of a minimal member of \(\mathcal F\) [KK]. Talagrand introduced the fractional version [Tal]. Frankston, Kahn, Narayanan and Park proved \(p_{\mathrm c}(\mathcal F)\le Kq_f(\mathcal F)\log\ell(\mathcal F)\) [FKNP], and Park and Pham proved the abstract conjecture itself [PP]. These theorems are background and are not used in this course.

## 3. Copies of graphs

All graphs are finite and simple. For graphs \(G\) and \(F\), \(N(G,F)\) is the number of subgraphs of \(G\) isomorphic to \(F\). These are *ordinary* copies: the vertices of a copy may span further edges of \(G\). The random graph \(G(n,p)\) has vertex set \([n]\), and its edge set has law \(\mu_p\) on \(X=\binom{[n]}2\), the set of \(2\)-element subsets of \([n]\). For a graph \(H\) with at least one edge and at most \(n\) vertices, the *containment threshold* and the *expectation threshold* are
\[
p_{\mathrm c}(n,H)=\inf\bigl\{p\in[0,1]:\mathbb P\bigl(N(G(n,p),H)>0\bigr)\ge\tfrac12\bigr\},
\]
\[
p_{\mathrm E}(n,H)=\inf\bigl\{p\in[0,1]:\mathbb E\,N(G(n,p),F)\ge\tfrac12\text{ for every subgraph }F\text{ of }H\bigr\}.
\]

A graph without isolated vertices is determined by its edge set, and we identify the two. A *copy* of such a graph \(F\) *on* \([n]\) is a set \(S\subseteq X\) of edges whose graph, on the vertices covered by \(S\), is isomorphic to \(F\). Write \(M(F)=N(K_n,F)\) for the number of copies of \(F\) on \([n]\), and \(M(I,F)=N(I,F)\); for the empty graph, \(M(\varnothing)=M(I,\varnothing)=1\). For integers \(0\le v\le n\), \((n)_v=n(n-1)\cdots(n-v+1)\).

**Lemma 3.1** (counting copies). Let \(F\) and \(I\) be graphs without isolated vertices and with at most \(n\) vertices.

1. \(M(F)=(n)_{v(F)}/|\operatorname{Aut}F|\), where \(\operatorname{Aut}F\) is the group of permutations of \(V(F)\) preserving adjacency.
2. For every graph \(F'\) with at most \(n\) vertices, isolated vertices allowed, \(\mathbb E\,N(G(n,p),F')=N(K_n,F')\,p^{e(F')}\).
3. Suppose \(I\) has a subgraph isomorphic to \(F\), let \(\mathbf I\) be a uniformly random copy of \(I\) on \([n]\), and let \(F_0\) be a copy of \(F\) on \([n]\). Then \(\mathbb P(F_0\subseteq\mathbf I)=M(I,F)/M(F)\); in particular this probability does not depend on the choice of \(F_0\).

**Proof.** (1) Each of the \((n)_{v(F)}\) injective maps \(\varphi\colon V(F)\to[n]\) gives the copy \(\varphi(F)=\{\varphi(x)\varphi(y):xy\in E(F)\}\), and every copy arises in this way. Since \(F\) has no isolated vertices, the edge set \(\varphi(F)\) determines the vertex set \(\varphi(V(F))\). So if \(\varphi(F)=\psi(F)\), then \(\alpha=\psi^{-1}\circ\varphi\) is a bijection of \(V(F)\) mapping edges to edges, hence an automorphism, and \(\varphi=\psi\circ\alpha\); conversely every \(\psi\circ\alpha\) with \(\alpha\in\operatorname{Aut}F\) gives the copy \(\psi(F)\). Each copy therefore arises from exactly \(|\operatorname{Aut}F|\) maps.

(2) Each of the \(N(K_n,F')\) copies of \(F'\) in \(K_n\) has \(e(F')\) edges and lies in \(G(n,p)\) with probability \(p^{e(F')}\); use linearity of expectation.

(3) A permutation \(\pi\) of \([n]\) maps copies to copies, and the uniform law of \(\mathbf I\) is invariant under \(\pi\). Any two copies of \(F\) are related by a permutation of \([n]\): compose an isomorphism between them with any bijection between the complements of their vertex sets. Hence \(\mathbb P(\pi F_0\subseteq\mathbf I)=\mathbb P(F_0\subseteq\pi^{-1}\mathbf I)=\mathbb P(F_0\subseteq\mathbf I)\) is the same for all copies \(F_0\). The sum of these \(M(F)\) equal probabilities is the expected number of copies of \(F\) contained in \(\mathbf I\), which is \(M(I,F)\) because \(\mathbf I\) is isomorphic to \(I\). \(\square\)

**Lemma 3.2** (basic properties). Let \(H\) have at least one edge and at most \(n\) vertices.

1. The infima defining \(p_{\mathrm c}(n,H)\) and \(p_{\mathrm E}(n,H)\) are attained, and the defining conditions hold for every larger \(p\).
2. \(p_{\mathrm E}(n,H)\) is the least \(p\in[0,1]\) such that \(M(S)\,p^{|S|}\ge\frac12\) for every nonempty set \(S\subseteq E(H)\), where \(S\) is regarded as a graph without isolated vertices.
3. \(0<p_{\mathrm E}(n,H)\le p_{\mathrm c}(n,H)\).
4. Deleting the isolated vertices of \(H\) changes neither \(p_{\mathrm c}(n,H)\) nor \(p_{\mathrm E}(n,H)\).

**Proof.** (1) The edge sets containing a copy of \(H\) form an increasing family \(\mathcal F_H\) on \(X\), nontrivial because \(H\) has an edge and at most \(n\) vertices; so \(p_{\mathrm c}(n,H)=p_{\mathrm c}(\mathcal F_H)\) by Lemma 1.1. Each \(\mathbb E\,N(G(n,p),F)\) is a nondecreasing polynomial in \(p\) by Lemma 3.1(2). So the finitely many conditions \(\mathbb E\,N(G(n,p),F)\ge\frac12\) define a closed set of numbers \(p\); with each \(p\) it contains every \(p'\in[p,1]\), and it contains \(p=1\) because \(N(K_n,F)\ge1\).

(2) Each nonempty \(S\subseteq E(H)\) is the edge set of the subgraph of \(H\) formed by \(S\) and the vertices it covers, and \(\mathbb E\,N(G(n,p),S)=M(S)p^{|S|}\); so the conditions in (2) are among those defining \(p_{\mathrm E}(n,H)\). Conversely, let \(F\) be a subgraph of \(H\) with edge set \(S\). If \(S=\varnothing\), then \(N(G,F)=\binom n{v(F)}\ge1\) for every graph \(G\) on \([n]\). If \(S\neq\varnothing\), every copy of \(S\) on \([n]\) extends to at least one copy of \(F\) in \(K_n\) by adding \(v(F)-v(S)\) further vertices, and different copies of \(S\) give different copies of \(F\); so \(N(K_n,F)\ge M(S)\), and the condition for \(F\) follows from that for \(S\).

(3) The condition for a single edge reads \(\binom n2p\ge\frac12\), which fails at \(p=0\). At \(p=p_{\mathrm c}(n,H)\), the graph \(G(n,p)\) contains a copy of \(H\), and hence of every subgraph \(F\) of \(H\), with probability at least \(\frac12\); since \(N(G,F)\ge\mathbf 1\{N(G,F)>0\}\), \(\mathbb E\,N(G(n,p),F)\ge\frac12\).

(4) Let \(H'\) be \(H\) without its isolated vertices. A graph on \([n]\) contains a copy of \(H\) exactly when it contains a copy of \(H'\), since a copy of \(H'\) can be completed by \(v(H)-v(H')\) further vertices of \([n]\). The graphs \(H\) and \(H'\) have the same edge set, so (2) gives the same expectation threshold. \(\square\)

Kahn and Kalai normalize with expected count \(1\) instead of \(\frac12\). By Lemma 3.2(2), each condition has the form \(p\ge(2M(S))^{-1/|S|}\), and replacing \(\frac12\) by \(1\) multiplies the right side by \(2^{1/|S|}\in(1,2]\); so the two normalizations give thresholds within a factor \(2\) of each other.

**Proposition 3.3.** With \(\mathcal F_H\) as in the proof of Lemma 3.2,
\[
p_{\mathrm E}(n,H)\le q(\mathcal F_H)\le q_f(\mathcal F_H)\le p_{\mathrm c}(n,H).
\]

**Proof.** Let \(p<p_{\mathrm E}(n,H)\). By Lemma 3.2(2) there is a nonempty \(S\subseteq E(H)\) with \(M(S)p^{|S|}<\frac12\). The copies of \(S\) on \([n]\) form a cover of \(\mathcal F_H\), since every copy of \(H\) contains a copy of \(S\), and the cost of this cover at \(p\) is \(M(S)p^{|S|}<\frac12\). Hence \(q(\mathcal F_H)\ge p\). The remaining inequalities are Proposition 2.2. \(\square\)

So the theorem of Park and Pham bounds \(p_{\mathrm c}(n,H)\) in terms of \(q(\mathcal F_H)\), which can be larger than \(p_{\mathrm E}(n,H)\); the graph conjecture of Kahn and Kalai asks for a bound in terms of the smaller quantity. Kahn and Kalai stated both conjectures in [KK], and the graph version became known as the *second* Kahn–Kalai conjecture.

## 4. Perfect matchings

**Lemma 4.1.** \((n)_m\ge(n/\mathrm e)^m\) for all integers \(0\le m\le n\).

**Proof.** Since \(\log\) is increasing, \(\log(n-i)\ge\int_{n-i-1}^{n-i}\log x\,dx\) for \(0\le i\le m-1\). Hence \(\log\,(n)_m\ge\int_{n-m}^n\log x\,dx=n\log n-(n-m)\log(n-m)-m\ge m\log n-m\), where \(0\log0=0\). \(\square\)

Let \(n\) be even and \(\mathrm{PM}_n\) the perfect matching on \(n\) vertices: \(n/2\) disjoint edges.

**Proposition 4.2.** For every even \(n\ge2\), \(\dfrac1{2n}\le p_{\mathrm E}(n,\mathrm{PM}_n)\le\dfrac{\mathrm e^2}n\).

**Proof.** The nonempty edge subsets of \(\mathrm{PM}_n\) are matchings \(jK_2\) with \(1\le j\le n/2\) edges, and \(|\operatorname{Aut}(jK_2)|=2^jj!\), so \(M(jK_2)=(n)_{2j}/(2^jj!)\) by Lemma 3.1. By Lemma 4.1 and \(j!\le j^j\le(n/2)^j\),
\[
M(jK_2)\Bigl(\frac{\mathrm e^2}n\Bigr)^j\ge\frac{(n/\mathrm e)^{2j}\,\mathrm e^{2j}}{2^j\,(n/2)^j\,n^j}=1,
\]
so every condition of Lemma 3.2(2) holds at \(p=\mathrm e^2/n\) when \(\mathrm e^2/n\le1\); when \(\mathrm e^2/n>1\) the upper bound is trivial. For the lower bound take \(j=n/2\): \(M(\mathrm{PM}_n)=(n-1)(n-3)\cdots3\cdot1\le n^{n/2}\), and \(M(\mathrm{PM}_n)\,p^{n/2}\ge\frac12\) forces \(p\ge(2n^{n/2})^{-2/n}=2^{-2/n}/n\ge1/(2n)\). \(\square\)

**Proposition 4.3** (isolated vertices). For every \(n\ge16\), the graph \(G(n,\frac{\log n}{3n})\) has an isolated vertex with probability greater than \(\frac12\). Consequently \(p_{\mathrm c}(n,\mathrm{PM}_n)>\frac{\log n}{3n}\) for every even \(n\ge16\).

**Proof.** Let \(p=\frac{\log n}{3n}\) and let \(Z\) be the number of isolated vertices of \(G(n,p)\). A vertex is isolated when its \(n-1\) potential edges are absent, and two given vertices are both isolated when \(2n-3\) potential edges are absent. Hence \(\mathbb EZ=n(1-p)^{n-1}\) and \(\mathbb E[Z(Z-1)]=n(n-1)(1-p)^{2n-3}\), so
\[
\operatorname{Var}Z=\mathbb EZ+n(n-1)(1-p)^{2n-3}-n^2(1-p)^{2n-2}\le\mathbb EZ+n^2(1-p)^{2n-3}p=\mathbb EZ+(\mathbb EZ)^2\,\frac p{1-p}.
\]
By Chebyshev's inequality, \(\mathbb P(Z=0)\le\mathbb P(|Z-\mathbb EZ|\ge\mathbb EZ)\le\frac1{\mathbb EZ}+\frac p{1-p}\). For \(0\le p\le\frac12\), \(\log(1-p)\ge-p-p^2\): the difference vanishes at \(0\) and has derivative \(\frac{p(1-2p)}{1-p}\ge0\). Hence \((1-p)^{n-1}\ge\mathrm e^{-n(p+p^2)}=n^{-(1+p)/3}\ge n^{-1/2}\), so \(\mathbb EZ\ge\sqrt n\). With \(\frac p{1-p}\le2p\) and \(n\ge16\),
\[
\mathbb P(Z=0)\le\frac1{\sqrt n}+\frac{2\log n}{3n}\le\frac14+\frac{2\log16}{48}<\frac12,
\]
because \(\frac{\log x}x\) decreases for \(x\ge\mathrm e\).

A graph containing a perfect matching on \([n]\) has no isolated vertex, so \(\mathbb P(N(G(n,p'),\mathrm{PM}_n)>0)<\frac12\) for \(p'=p\), and by Lemma 1.1 for every \(p'\le p\). Since the infimum defining \(p_{\mathrm c}(n,\mathrm{PM}_n)\) is attained (Lemma 3.2), \(p_{\mathrm c}(n,\mathrm{PM}_n)>p\). \(\square\)

The logarithm persists even if \(p_{\mathrm E}\) is replaced by the larger thresholds of Proposition 3.3:

**Proposition 4.4.** For every even \(n\ge2\), \(q(\mathcal F_{\mathrm{PM}_n})\le q_f(\mathcal F_{\mathrm{PM}_n})\le\mathrm e^2/n\).

**Proof.** Let \(A\) be a uniformly random perfect matching on \([n]\), a random member of \(\mathcal F_{\mathrm{PM}_n}\). A nonempty set \(J\) of edges lies in \(A\) only if \(J\) is a matching, say with \(j\) edges, and then \(\mathbb P(J\subseteq A)=1/((n-1)(n-3)\cdots(n-2j+1))\), the number of perfect matchings of the other \(n-2j\) vertices divided by the number of all perfect matchings. The product of all \(n/2\) factors \(n-1,n-3,\dots,1\) is \(n!/(2^{n/2}(n/2)!)\ge(n/\mathrm e)^n/(2^{n/2}(n/2)^{n/2})=(n/\mathrm e^2)^{n/2}\), by Lemma 4.1 with \(m=n\) and \((n/2)!\le(n/2)^{n/2}\). The \(j\) largest factors have geometric mean at least the geometric mean of all of them, so \(\mathbb P(J\subseteq A)\le(\mathrm e^2/n)^j\). Proposition 2.3 gives the claim. \(\square\)

Together, Propositions 3.3, 4.2, 4.3 and 4.4 give, for even \(n\ge16\),
\[
\frac{p_{\mathrm c}(n,\mathrm{PM}_n)}{p_{\mathrm E}(n,\mathrm{PM}_n)}\ge\frac{p_{\mathrm c}(n,\mathrm{PM}_n)}{q_f(\mathcal F_{\mathrm{PM}_n})}>\frac{\log n}{3\mathrm e^2}:
\]
a comparison of the containment threshold with any of the three expectation thresholds, valid for all graphs, must allow a logarithmic factor. Corollary 3.2 of [The second Kahn–Kalai conjecture](the-second-kahn-kalai-conjecture.md) shows that \(p_{\mathrm c}(n,\mathrm{PM}_n)\) is of order \(\frac{\log n}n\); Erdős and Rényi determined its asymptotic value \(\frac{\log n}n\) in 1966.

## 5. The second Kahn–Kalai conjecture

**Theorem 5.1** (OpenAI 2026; the second Kahn–Kalai conjecture). For every \(n\ge2\) and every graph \(H\) with \(h\ge1\) edges and at most \(n\) vertices,
\[
p_{\mathrm c}(n,H)\le\min\bigl\{1,\ 2048\,\mathrm e^{50}\,p_{\mathrm E}(n,H)\,(1+\log_2h)\bigr\},
\]
and consequently \(p_{\mathrm c}(n,H)\le6144\,\mathrm e^{50}\,p_{\mathrm E}(n,H)\log_2n\).

The constant is enormous but universal: the graph \(H\) may depend on \(n\) in any way. The proof is Theorem 3.1 of [The second Kahn–Kalai conjecture](the-second-kahn-kalai-conjecture.md). Before it, Mossel, Niles-Weed, Sun and Zadik obtained a single logarithm for a modified expectation threshold [MNSZ-1], Dubroff, Kahn and Park proved \(p_{\mathrm c}(n,H)=O(p_{\mathrm E}(n,H)\log^3n)\) [DKP], and Tran reduced the loss to \(O(\log^2(2e(H)))\) [Tran].

The proof of Theorem 5.1 has three parts, one per lesson.

1. [Resampling a spread family](resampling-a-spread-family.md). A probability law on subsets of \(X\) is *\(a\)-spread* if it gives mass at most \(a^{|J|}\) to the sets containing any given nonempty set \(J\). One random set \(W\) of density \(\rho=\mathrm e^{50}a\) typically allows a set drawn from such a law to be traded for a *fragment*, the part outside \(W\) of a related set, of at most half the size; the fragments are again nearly spread. This step is the planted posterior sampling of Mossel, Niles-Weed, Sun and Zadik [MNSZ-2].
2. [Covering a probability tree](covering-a-probability-tree.md). The trade is made simultaneously at every node of a tree of successive extensions, whose labels are disjoint along each branch and whose sizes grow by a factor of at least \(16\) from level to level. Disjointness controls the dependence created by reusing one random set at all levels, and about \(\log_2\) of the largest label size rounds place a whole branch inside the union of the random sets.
3. [The second Kahn–Kalai conjecture](the-second-kahn-kalai-conjecture.md). For a graph \(H\), maximizing a ratio over subgraphs, as in Tran's construction [Tran], gives a chain of subgraphs whose conditional extensions are \(128\,p_{\mathrm E}(n,H)\)-spread; the tree of all histories of this chain has copies of \(H\) as branch unions.

The remaining lessons treat the two expectation thresholds of Section 2 and the integral threshold of graphs.

4. [Integral and fractional expectation thresholds](integral-and-fractional-expectation-thresholds.md) proves Talagrand's conjecture \(q_f(\mathcal F)\le25\cdot512^4\,q(\mathcal F)\) through a multiscale selector estimate.
5. [The discrete convexity conjecture](the-discrete-convexity-conjecture.md) proves that if \(\mu_p(\mathcal D)\ge1-2^{-75}\), the sets not covered by \(2^{75}\) members of \(\mathcal D\) form a \(p\)-small family, and a version with two unions at density \(p/(50\cdot512^4)\).
6. [Embedding sparse graphs in random graphs](embedding-sparse-graphs-in-random-graphs.md) and [Graph decompositions at the expectation threshold](graph-decompositions-at-the-expectation-threshold.md) prove that every graph splits into a bounded number of pieces, each appearing in \(G(n,p)\) once \(p\) is a constant multiple of the integral expectation threshold of the whole graph.

## 6. Exercises

**Exercise 6.1** (easy). Let \(S_0\subseteq X\) have \(s\ge1\) elements and \(\mathcal F=\{A\subseteq X:S_0\subseteq A\}\). Show that \(q(\mathcal F)=q_f(\mathcal F)=p_{\mathrm c}(\mathcal F)=2^{-1/s}\).

**Exercise 6.2** (easy). Let \(|X|=N\ge1\) and \(\mathcal F=\{A\subseteq X:A\neq\varnothing\}\). Show that \(q(\mathcal F)=\frac1{2N}\), \(p_{\mathrm c}(\mathcal F)=1-2^{-1/N}\) and \(p_{\mathrm c}(\mathcal F)\le2\log2\cdot q(\mathcal F)\).

**Exercise 6.3** (easy). Show that \(p_{\mathrm E}(n,K_3)=\bigl(3/(n)_3\bigr)^{1/3}\) for every \(n\ge3\).

**Exercise 6.4** (medium). Show that the suprema defining \(q(\mathcal F)\) and \(q_f(\mathcal F)\) are attained. For \(q_f\), show first that replacing a fractional cover \(g\) by \(\min\{g,1\}\) gives a fractional cover of no larger cost.

**Exercise 6.5** (medium). Let \(H\) have \(h\ge1\) edges, at most \(n\) vertices and no isolated vertices, let \(q=p_{\mathrm E}(n,H)\), and let \(\mathbf H\) be a uniformly random copy of \(H\) on \([n]\). Show that \(\mathbb P(J\subseteq\mathbf H)\le2\binom h{|J|}q^{|J|}\le(2\mathrm ehq)^{|J|}\) for every nonempty \(J\subseteq X\).

## 7. Solutions

**6.1.** The cover \(\{S_0\}\) costs \(p^s\), so \(q(\mathcal F)\ge2^{-1/s}\). Every fractional cover \(g\) satisfies \(\sum_{S\subseteq S_0}g(S)\ge1\) because \(S_0\in\mathcal F\), so \(c_p(g)\ge\sum_{S\subseteq S_0}g(S)p^{|S|}\ge p^s\); a cost at most \(\frac12\) forces \(p\le2^{-1/s}\), so \(q_f(\mathcal F)\le2^{-1/s}\). Finally \(\mu_p(\mathcal F)=p^s\) equals \(\frac12\) at \(p=2^{-1/s}\). Proposition 2.2 gives the chain of equalities.

**6.2.** Each singleton \(\{x\}\) lies in \(\mathcal F\), and the only sets contained in it are \(\varnothing\) and \(\{x\}\). A cover containing \(\varnothing\) costs at least \(1\); otherwise it contains every singleton and costs at least \(Np\). The cover by all singletons costs exactly \(Np\), so \(q(\mathcal F)=\frac1{2N}\). Next \(\mu_p(\mathcal F)=1-(1-p)^N\), which equals \(\frac12\) at \(p=1-2^{-1/N}\). Since \(1-\mathrm e^{-y}\le y\) with \(y=\frac{\log2}N\), \(p_{\mathrm c}(\mathcal F)\le\frac{\log2}N=2\log2\cdot q(\mathcal F)\).

**6.3.** The nonempty edge subsets of \(K_3\) are an edge, a path with two edges and the triangle, with \(M=\binom n2\), \((n)_3/2\) and \((n)_3/6\) respectively, by Lemma 3.1(1). By Lemma 3.2(2), \(p_{\mathrm E}(n,K_3)\) is the largest of \((n(n-1))^{-1}\), \(((n)_3)^{-1/2}\) and \((3/(n)_3)^{1/3}\). Write \(t=(n)_3\ge6\). Then \((3/t)^{1/3}\ge t^{-1/2}\) because \(9t\ge1\), and \((3/t)^{1/3}\ge(n(n-1))^{-1}\) because \(3n^3(n-1)^3\ge t=n(n-1)(n-2)\).

**6.4.** There are finitely many covers, and each cost is a continuous nondecreasing function of \(p\); so \(\{p:\min_{\mathcal G}c_p(\mathcal G)\le\frac12\}\) is closed and \(q(\mathcal F)\) belongs to it. For a fractional cover \(g\) and \(A\in\mathcal F\): if \(g(S)\ge1\) for some \(S\subseteq A\), then \(\min\{g,1\}\) gives \(S\) weight \(1\); otherwise \(\min\{g,1\}=g\) on the subsets of \(A\). In both cases \(\sum_{S\subseteq A}\min\{g(S),1\}\ge1\), and the cost does not increase. The fractional covers with values in \([0,1]\) form a compact set \(K\subseteq[0,1]^{2^X}\), and \((p,g)\mapsto c_p(g)\) is continuous. Hence \(\{p:\min_{g\in K}c_p(g)\le\frac12\}\) is closed, and by the first observation it is the set defining \(q_f(\mathcal F)\).

**6.5.** If \(J\) is not a copy of a subset of \(E(H)\), the probability is \(0\). Otherwise \(J\) is a copy of a nonempty \(S\subseteq E(H)\) with \(|S|=|J|=j\), and by Lemma 3.1(3), \(\mathbb P(J\subseteq\mathbf H)=M(H,S)/M(S)\). The copies of \(S\) in \(H\) are \(j\)-element subsets of \(E(H)\), so \(M(H,S)\le\binom hj\), and \(M(S)\ge\frac12q^{-j}\) by Lemma 3.2(2). Finally \(2\binom hj\le2\frac{h^j}{j!}\le2\bigl(\frac{\mathrm eh}j\bigr)^j\le(2\mathrm eh)^j\), using \(j!\ge(j/\mathrm e)^j\).

## References

- [OpenAI-KK2] OpenAI, *The second Kahn–Kalai conjecture*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-second-Kahn-Kalai-conjecture-September-24-2026
- [KK] J. Kahn and G. Kalai, *Thresholds and expectation thresholds*, Combinatorics, Probability and Computing 16 (2007), 495–502. https://arxiv.org/abs/math/0603218
- [FKNP] K. Frankston, J. Kahn, B. Narayanan and J. Park, *Thresholds versus fractional expectation-thresholds*, Annals of Mathematics 194 (2021), 475–495. https://arxiv.org/abs/1910.13433
- [PP] J. Park and H. T. Pham, *A proof of the Kahn–Kalai conjecture*, Journal of the American Mathematical Society 37 (2024), 235–243. https://arxiv.org/abs/2203.17207
- [Tal] M. Talagrand, *Are many small sets explicitly small?*, Proceedings of STOC 2010, 13–36. https://michel.talagrand.net/preprints/small.pdf
- [MNSZ-1] E. Mossel, J. Niles-Weed, N. Sun and I. Zadik, *On the second Kahn–Kalai conjecture*, 2022. https://arxiv.org/abs/2209.03326
- [MNSZ-2] E. Mossel, J. Niles-Weed, N. Sun and I. Zadik, *A second moment proof of the spread lemma*, 2022; published as *A Bayesian proof of the spread lemma*, Random Structures & Algorithms 66 (2025). https://arxiv.org/abs/2209.11347
- [DKP] Q. Dubroff, J. Kahn and J. Park, *On the "second" Kahn–Kalai conjecture*, 2025. https://arxiv.org/abs/2508.14269
- [Tran] T. Tran, *Fractional expectation thresholds and the "second" Kahn–Kalai conjecture*, 2026. https://arxiv.org/abs/2609.20546
