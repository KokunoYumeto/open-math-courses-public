# Covering a probability tree

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The transition of [Resampling a spread family](resampling-a-spread-family.md) trades one random label for a fragment of at most half its size. The graph argument needs more: a whole *chain* of extensions, a small set first, then an extension of it, then an extension of that, each drawn from a law that is spread conditionally on what came before, with sizes \(\ell_1,\ell_2,\dots\) growing geometrically. All possible histories of such a chain form a tree. This lesson proves OpenAI's tree covering theorem (Theorem 3.2) [OpenAI-KK2]: a random set of density of order \(\sigma\log\ell_k\) contains all the labels along some branch of the tree with probability at least \(\frac23\), where every node has \(\sigma\)-spread children and \(\ell_k\) is the largest label size. One random set is used at all nodes of the tree simultaneously; the labels along each branch are disjoint, and this disjointness keeps the resulting dependence under control. For a tree with one level, the theorem is a form of the spread lemma (Corollary 4.1).

We use the product laws \(\mu_\rho\) and Lemmas 1.1 and 1.2 of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md), and the indexed families, the transition, local failures and Theorem 3.1 of [Resampling a spread family](resampling-a-spread-family.md).

## 1. Probability trees

**Definition 1.1.** Let \(k\ge0\). A *probability tree with \(k\) levels* on a finite set \(X\) is a finite rooted tree whose leaves all have depth \(k\), together with, for each non-leaf node \(v\), a probability law \(\nu_v\) on the set \(\operatorname{Ch}(v)\) of children of \(v\), with \(\nu_v(b)>0\) for every child \(b\), and a *label* \(A_v(b)\subseteq X\) on each arc from \(v\) to a child \(b\). The arcs from depth \(j-1\) to depth \(j\) form *level* \(j\). A *path* is a sequence \(P=(v_0,v_1,\dots,v_k)\) from the root \(v_0\) to a leaf \(v_k\) with \(v_j\in\operatorname{Ch}(v_{j-1})\), and its *union* is
\[
\mathcal U(P)=\bigcup_{j=1}^kA_{v_{j-1}}(v_j).
\]
A tree with \(0\) levels is a single node; it has one path, whose union is empty.

Different arcs may carry equal labels, and labels may be empty; nodes are distinct even when the labels leading to them agree. The tree is *disjoint* if the labels along each path are pairwise disjoint. Level \(j\) has *capacity* \(m\) if \(|A_v(b)|\le m\) for all its arcs, and it is *\(a\)-spread* if, for every node \(v\) at depth \(j-1\), the indexed family \((A_v(b))_{b\in\operatorname{Ch}(v)}\) with the weights \(\nu_v\) is \(a\)-spread. These conditions concern the children of one node at a time; nothing is assumed about the law of a whole path.

Every arc lies on some path, since every non-leaf node has a child and all leaves have depth \(k\).

**Lemma 1.2** (labels below an arc). In a disjoint probability tree, let \(b\) be a child of \(v\). Every arc of the subtree rooted at \(b\) has a label disjoint from \(A_v(b)\).

**Proof.** Let \((u,b')\) be an arc with \(u\) in the subtree rooted at \(b\). The path from the root to \(u\) passes through the arc \((v,b)\); continue it through \(b'\) to a leaf. Both labels lie on this path. \(\square\)

## 2. One simultaneous reduction

**Lemma 2.1** (reduction; OpenAI). Let \(\mathcal T\) be a disjoint probability tree on \(X\) with \(k\ge1\) levels. Suppose that level \(j\) has capacity \(m_j\) and is \(\alpha_j\)-spread, where the \(m_j\) are positive integers with \(m_{j+1}\ge16m_j\), and \(0<\alpha_j\le a\) for a number \(a\) with \(\rho=\mathrm e^{50}a<1\). Then there are a family \(\mathcal S\) of subsets of \(X\) with \(\mu_\rho(\mathcal S)\ge\frac34\) and, for each \(W\in\mathcal S\), a disjoint probability tree \(\mathcal T'_W\) with \(k\) levels such that:

1. level \(j\) of \(\mathcal T'_W\) has capacity \(\lfloor m_j/2\rfloor\) and is \(\alpha_j/(1-\mathrm e^{-m_j})\)-spread;
2. for every path \(Q\) of \(\mathcal T'_W\) there is a path \(P\) of \(\mathcal T\) with \(\mathcal U(P)\subseteq W\cup\mathcal U(Q)\).

**Proof.** *Local quantities.* Let \(v\) be a non-leaf node at depth \(s-1\), so that its arcs belong to level \(s\). Apply the transition of [Resampling a spread family](resampling-a-spread-family.md) to the family \((A_v(b))_{b\in\operatorname{Ch}(v)}\) with weights \(\nu_v\), parameter \(\rho\) and capacity \(m_s\); since \(\alpha_s\le a=\mathrm e^{-50}\rho\), Theorem 3.1 there applies. For a fixed set \(W\subseteq X\), let
\[
d_v(W)=\mathbb P(\text{local failure}\mid W),\qquad t_{vb}(W)=\mathbb P(\text{no local failure and target }b\mid W),
\]
probabilities over the source and the target only. Then
\[
d_v(W)+\sum_{b\in\operatorname{Ch}(v)}t_{vb}(W)=1,\tag{2.1}
\]
and by Lemma 2.1(2) there, \(d_v(W)\) and \(t_{vb}(W)\) depend only on \(W\cap\bigcup_bA_v(b)\).

*Good nodes.* Fix \(W\) and put \(\varepsilon_s=\mathrm e^{-m_s}\). Call every leaf good, and, proceeding upward, call a non-leaf node \(v\) at depth \(s-1\) *good* if
\[
\sum_{b\text{ good}}t_{vb}(W)\ge1-\varepsilon_s.\tag{2.2}
\]
Let \(\mathcal S\) be the family of sets \(W\) for which the root is good.

*A potential.* Define \(D_v(W)\ge0\) by \(D_v(W)=0\) at the leaves and
\[
D_v(W)=\varepsilon_s^{-1}\Bigl(d_v(W)+\sum_{b\in\operatorname{Ch}(v)}t_{vb}(W)\,D_b(W)\Bigr)\tag{2.3}
\]
at a non-leaf node \(v\) at depth \(s-1\). Every bad node \(v\) has \(D_v(W)>1\). Indeed, assume this for the children of \(v\). If \(v\) is bad, then (2.1) and the failure of (2.2) give \(d_v+\sum_{b\text{ bad}}t_{vb}=1-\sum_{b\text{ good}}t_{vb}>\varepsilon_s\); since \(D_b>1\) for the bad children, the bracket in (2.3) exceeds \(\varepsilon_s\).

*The potential below an arc.* Let \(b\) be a child of \(v\). By its recursive definition, \(D_b(W)\) is a function of the quantities \(d_u(W)\) and \(t_{ub'}(W)\) at the nodes \(u\) of the subtree rooted at \(b\), and each of these depends only on the intersection of \(W\) with labels of arcs in that subtree. By Lemma 1.2, all these labels are disjoint from \(A_v(b)\). Hence \(D_b(W)\) depends only on \(W\setminus A_v(b)\). This holds at every node of \(\mathcal T\), good or bad.

*The expected potential.* Let \(W\sim\mu_\rho\), and let \(v\) be a non-leaf node at depth \(s-1\). Theorem 3.1(1) of [Resampling a spread family](resampling-a-spread-family.md) gives \(\mathbb Ed_v(W)\le\mathrm e^{-9m_s}\). A transition without local failure has \(Z(Y)\ge\mathrm e^{-10m_s}\), so \(t_{vb}(W)\le\mathbb P(\text{target }b,\ Z(Y)\ge\mathrm e^{-10m_s}\mid W)\), and Theorem 3.1(2) there, applied to \(f=D_b\), gives \(\mathbb E[t_{vb}(W)D_b(W)]\le\mathrm e^{11m_s}\nu_v(b)\,\mathbb ED_b(W)\). With \(\varepsilon_s^{-1}=\mathrm e^{m_s}\), (2.3) yields
\[
\mathbb ED_v(W)\le\mathrm e^{-8m_s}+\mathrm e^{12m_s}\sum_b\nu_v(b)\,\mathbb ED_b(W).\tag{2.4}
\]
Since \(\sum_b\nu_v(b)=1\), induction from the leaves upward gives, for every \(v\) at depth \(s-1\),
\[
\mathbb ED_v(W)\le\sum_{j=s}^k\exp\Bigl(12\sum_{h=s}^{j-1}m_h-8m_j\Bigr).
\]
For the root \(o\), take \(s=1\). Since \(m_h\le16^{h-j}m_j\) for \(h<j\), \(\sum_{h<j}m_h\le m_j\sum_{i\ge1}16^{-i}=m_j/15\), and each exponent is at most \(\frac{12}{15}m_j-8m_j\le-7m_j\). The \(m_j\) are distinct positive integers, so
\[
1-\mu_\rho(\mathcal S)=\mu_\rho(\text{root bad})\le\mathbb P\bigl(D_o(W)>1\bigr)\le\mathbb ED_o(W)\le\sum_{m\ge1}\mathrm e^{-7m}=\frac1{\mathrm e^7-1}<\frac14.
\]

*The reduced tree.* Let \(W\in\mathcal S\), and build \(\mathcal T'_W\) from the root downward. At a retained good non-leaf node \(v\) at depth \(j-1\), put \(\gamma_v=\sum_{b\text{ good}}t_{vb}(W)\ge1-\varepsilon_j>0\); retain the good children \(b\) with \(t_{vb}(W)>0\), and give them the weights \(\nu'_v(b)=t_{vb}(W)/\gamma_v\) and the labels \(A'_v(b)=A_v(b)\setminus W\). These weights are positive and sum to \(1\), every retained non-leaf node has a retained child, and the retained nodes form a probability tree with \(k\) levels. Its labels are subsets of labels of \(\mathcal T\), so it is disjoint. Every path \(Q\) of \(\mathcal T'_W\) is a path \(P\) of \(\mathcal T\), and \(A_v(b)\subseteq W\cup A'_v(b)\) on every arc gives \(\mathcal U(P)\subseteq W\cup\mathcal U(Q)\).

If \(t_{vb}(W)>0\), some outcome of the transition at \(v\) has target \(b\) and no local failure, so its fragment \(A_v(b)\setminus W\) has at most \(m_j/2\) elements. Thus level \(j\) has capacity \(\lfloor m_j/2\rfloor\).

For the spread, let \(J\subseteq X\) be nonempty, and run the transition at \(v\) with the fixed set \(W\). The retained children \(b\) with \(J\subseteq A'_v(b)\) are targets of outcomes with no local failure, a good target and \(J\subseteq T\). By Lemma 2.1(1) of [Resampling a spread family](resampling-a-spread-family.md), \(T\subseteq A_v(c)\) for the source \(c\), whose law is \(\nu_v\) whatever \(W\) is. Hence
\[
\sum_{\substack{b\text{ retained}\\J\subseteq A'_v(b)}}\nu'_v(b)=\frac{\mathbb P(\text{no local failure, good target, }J\subseteq T\mid W)}{\gamma_v}\le\frac{\mathbb P_{c\sim\nu_v}\bigl(J\subseteq A_v(c)\bigr)}{1-\varepsilon_j}\le\frac{\alpha_j^{|J|}}{1-\varepsilon_j}\le\Bigl(\frac{\alpha_j}{1-\varepsilon_j}\Bigr)^{|J|}.
\]
\(\square\)

The sources and targets are auxiliary: for each \(W\), the tree \(\mathcal T'_W\) is determined by the numbers \(t_{vb}(W)\).

## 3. The tree covering theorem

**Lemma 3.1.** \(\prod_{m=1}^\infty(1-\mathrm e^{-m})^{-1}<4\).

**Proof.** For \(0<y<1\), \(-\log(1-y)=\sum_{i\ge1}y^i/i\le y/(1-y)\). Hence
\[
\sum_{m\ge1}-\log(1-\mathrm e^{-m})\le\frac1{1-\mathrm e^{-1}}\sum_{m\ge1}\mathrm e^{-m}=\frac{\mathrm e^{-1}}{(1-\mathrm e^{-1})^2}<0.93<\log4.\qquad\square
\]

**Theorem 3.2** (tree covering; OpenAI). Let \(\mathcal T\) be a disjoint probability tree on \(X\) with \(k\ge1\) levels. Suppose that every level is \(\sigma\)-spread, where \(\sigma>0\), and that level \(i\) has capacity \(\ell_i\), where the \(\ell_i\) are positive integers with \(\ell_{i+1}\ge16\ell_i\). Let
\[
r=\min\bigl\{1,\ 16\,\mathrm e^{50}\sigma\,(1+\log_2\ell_k)\bigr\}.
\]
Then a random set \(W\sim\mu_r\) contains \(\mathcal U(P)\) for some path \(P\) of \(\mathcal T\) with probability at least \(\frac23\).

**Proof.** If \(r=1\), then \(W=X\) and every path works. Let \(r<1\), and put
\[
a=4\sigma,\qquad\rho=\mathrm e^{50}a,\qquad s=\lfloor\log_2\ell_k\rfloor+1.
\]
Then \(\rho=r/(4(1+\log_2\ell_k))<1\), and \(2^{s-1}\le\ell_k<2^s\).

*The procedure.* Let \(W_1,W_2,\dots\) be independent with law \(\mu_\rho\). We process them in order, keeping a current disjoint probability tree, initially \(\mathcal T\), and a number \(t\) of successes, initially \(0\). After \(t\) successes, produced by the sets \(W^{(1)},\dots,W^{(t)}\), the current tree \(\mathcal T_t\) has the following two properties.

(a) For every path \(Q\) of \(\mathcal T_t\) there is a path \(P\) of \(\mathcal T\) with \(\mathcal U(P)\subseteq W^{(1)}\cup\dots\cup W^{(t)}\cup\mathcal U(Q)\).

(b) The levels of \(\mathcal T_t\) correspond, in order, to the original levels \(i\) with \(m_i(t)=\lfloor\ell_i/2^t\rfloor\ge1\); such a level has capacity \(m_i(t)\) and is \(\alpha_i(t)\)-spread, where
\[
\alpha_i(t)=\sigma\prod_{u=0}^{t-1}\bigl(1-\mathrm e^{-\lfloor\ell_i/2^u\rfloor}\bigr)^{-1}.
\]

Both hold for \(t=0\). Suppose that they hold after \(t\) successes and that \(\mathcal T_t\) has at least one level. For a remaining level \(i\), the numbers \(\lfloor\ell_i/2^u\rfloor\) with \(0\le u<t\) are distinct positive integers, since each is at least \(m_i(t)\ge1\) and halving a positive integer decreases it; so Lemma 3.1 gives \(\alpha_i(t)<4\sigma=a\). For consecutive remaining levels \(i<i'\), \(m_{i'}(t)=\lfloor\ell_{i'}/2^t\rfloor\ge\lfloor16\ell_i/2^t\rfloor\ge16\,m_i(t)\). So Lemma 2.1 applies to \(\mathcal T_t\) and the next set \(W\) of the sequence. If \(W\notin\mathcal S\), the attempt *fails* and the current tree is kept. If \(W\in\mathcal S\), the attempt *succeeds*, and \(\mathcal T'_W\) has level capacities \(\lfloor m_i(t)/2\rfloor=m_i(t+1)\), because \(\lfloor\lfloor x\rfloor/2\rfloor=\lfloor x/2\rfloor\), and spread parameters \(\alpha_i(t)/(1-\mathrm e^{-m_i(t)})=\alpha_i(t+1)\). The levels of \(\mathcal T'_W\) with \(m_i(t+1)=0\) form an initial segment, since \(\ell_i\) increases with \(i\), and all their labels are empty. Follow a path of \(\mathcal T'_W\) through this segment, chosen by a fixed rule, to a node \(u\), and let \(\mathcal T_{t+1}\) be the subtree rooted at \(u\). A path of \(\mathcal T_{t+1}\), preceded by the chosen segment, is a path of \(\mathcal T'_W\) with the same union; so Lemma 2.1(2) and (a) for \(\mathcal T_t\) give (a) for \(\mathcal T_{t+1}\) with \(W^{(t+1)}=W\), and (b) holds by construction.

*Completion.* Since \(\ell_i\le\ell_k<2^s\), every \(m_i(s)\) is \(0\), while \(m_k(t)\ge1\) for \(t<s\). So the current tree keeps at least one level until the \(s\)-th success and has no levels after it. Then (a), applied to the single path of \(\mathcal T_s\), whose union is empty, gives a path \(P\) of \(\mathcal T\) with \(\mathcal U(P)\subseteq W^{(1)}\cup\dots\cup W^{(s)}\).

*Number of attempts.* The current tree is determined by the sets already processed, and the next set is independent of them. So, before completion, each attempt succeeds with conditional probability at least \(\frac34\) given the past. Let \(G_t\) be the number of attempts after the \((t-1)\)-th success up to and including the \(t\)-th, and \(N=G_1+\dots+G_s\). Given the past up to the \((t-1)\)-th success, the next \(g\) attempts all fail with probability at most \(4^{-g}\); so \(\mathbb EG_t\le\sum_{g\ge0}4^{-g}=\frac43\) and \(\mathbb EN\le\frac{4s}3\). By Markov's inequality, \(\mathbb P(N>4s)\le\frac13\).

*The union.* Let \(W_*=W_1\cup\dots\cup W_{4s}\). On the event \(N\le4s\), \(W_*\) contains \(\mathcal U(P)\) for some path \(P\) of \(\mathcal T\). By Lemma 1.2 of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md), \(W_*\) has law \(\mu_{r_*}\) with \(r_*\le4s\rho=16\,\mathrm e^{50}\sigma s\le r\), since \(s\le1+\log_2\ell_k\). So \(\mu_{r_*}\) gives probability at least \(\frac23\) to the increasing family of sets that contain the union of some path, and by Lemma 1.1 there, so does \(\mu_r\). \(\square\)

## 4. One level: the spread lemma

**Corollary 4.1** (spread lemma). Let \((A_b)_{b\in B}\) with weights \(\nu\) be a \(\sigma\)-spread indexed family on \(X\) with \(|A_b|\le\ell\) for all \(b\), where \(\ell\) is a positive integer. For \(r=\min\{1,16\,\mathrm e^{50}\sigma(1+\log_2\ell)\}\), a random set \(W\sim\mu_r\) contains some \(A_b\) with probability at least \(\frac23\).

**Proof.** The tree consisting of a root with children \(b\in B\), weights \(\nu_b\) and labels \(A_b\) has one level, of capacity \(\ell\); it is disjoint and \(\sigma\)-spread. Apply Theorem 3.2. \(\square\)

Statements of this type were proved by Alweiss, Lovett, Wu and Zhang in their work on the sunflower conjecture [ALWZ] and by Frankston, Kahn, Narayanan and Park [FKNP], who combined such a statement with linear programming duality to bound thresholds by fractional expectation thresholds. Mossel, Niles-Weed, Sun and Zadik gave the planted proof [MNSZ-2] that Lemma 2.1 carries out simultaneously along a tree. The factor \(\log\ell\) cannot be removed (Exercise 5.4).

## 5. Exercises

**Exercise 5.1** (easy). Let \(m_1,\dots,m_k\) be positive integers with \(m_{j+1}\ge16m_j\). Show that \(\sum_{j=1}^k\exp\bigl(12\sum_{h<j}m_h-8m_j\bigr)<\frac1{1000}\).

**Exercise 5.2** (easy). Show that \(\lfloor\lfloor x\rfloor/2\rfloor=\lfloor x/2\rfloor\) and \(\lfloor16x\rfloor\ge16\lfloor x\rfloor\) for real \(x\ge0\), and that \(\lfloor\ell/2^s\rfloor=0\) for \(s=\lfloor\log_2\ell\rfloor+1\).

**Exercise 5.3** (medium). Disregarding the conditions on capacities, give a probability tree with two levels that is not disjoint, in which the potential \(D_b\) at the child \(b\) of the root depends on \(W\cap A_{\text{root}}(b)\). At which step does the proof of Lemma 2.1 use disjointness?

**Exercise 5.4** (medium). Let \(\ell\ge2\) and \(M\ge1\) be integers, \(X=[\ell]\times[M]\), and let \(\nu\) be the uniform law on the \(M^\ell\) sets \(\{(i,g(i)):i\in[\ell]\}\), where \(g\colon[\ell]\to[M]\). Show that \(\nu\) is \(\frac1M\)-spread. Show that if \(r<1\) and \(W\sim\mu_r\) contains one of these sets with probability at least \(\frac23\), then \(\frac r{1-r}\ge\frac1M\log\frac\ell{\log(3/2)}\ge\frac{\log\ell}M\). Conclude that Corollary 4.1 fails if \(\log_2\ell\) is replaced by a function \(\phi(\ell)\) with \(\phi(\ell)/\log\ell\to0\).

## 6. Solutions

**5.1.** As in the proof of Lemma 2.1, each exponent is at most \(-7m_j\), and the \(m_j\) are distinct positive integers, so the sum is at most \(\sum_{m\ge1}\mathrm e^{-7m}=(\mathrm e^7-1)^{-1}<0.001\).

**5.2.** Let \(n=\lfloor x\rfloor\). Since \(n\le x\), \(\lfloor n/2\rfloor\le\lfloor x/2\rfloor\). Conversely, \(2\lfloor x/2\rfloor\) is an integer at most \(x\), hence at most \(n\), so \(\lfloor x/2\rfloor\le\lfloor n/2\rfloor\). Next, \(16\lfloor x\rfloor\) is an integer at most \(16x\). Finally \(\log_2\ell<\lfloor\log_2\ell\rfloor+1=s\), so \(\ell<2^s\).

**5.3.** Let \(X=\{x\}\), let the root have a single child \(b\) with label \(\{x\}\), and let \(b\) have a single child with label \(\{x\}\), both levels of capacity \(1\). At \(b\), the transition has one label \(A=\{x\}\), so \(Z(Y)=\rho^{-1}\) and \(T=\{x\}\setminus W\). The outcome is a local failure exactly when \(|T|>\frac12\), that is, when \(x\notin W\). So \(D_b(W)=\mathrm e\,\mathbf 1\{x\notin W\}\) depends on \(W\cap\{x\}=W\cap A_{\text{root}}(b)\). Disjointness is used to show that \(D_b\) depends only on \(W\setminus A_v(b)\), which allows Theorem 3.1(2) of [Resampling a spread family](resampling-a-spread-family.md) to be applied with \(f=D_b\).

**5.4.** A nonempty set \(J\) lies in \(\{(i,g(i))\}\) only if its elements have distinct first coordinates, and then for \(M^{-|J|}\) of the functions \(g\); so \(\nu\) is \(\frac1M\)-spread. The set \(W\) contains one of the sets exactly when every row \(\{i\}\times[M]\) meets \(W\), which has probability \(\bigl(1-(1-r)^M\bigr)^\ell\). If this is at least \(\frac23\), then \((1-r)^M\le1-(2/3)^{1/\ell}\le\frac{\log(3/2)}\ell\), using \(1-\mathrm e^{-y}\le y\). Since \(\log(1-r)\ge-\frac r{1-r}\), \((1-r)^M\ge\exp\bigl(-\frac{Mr}{1-r}\bigr)\), and therefore \(\frac{Mr}{1-r}\ge\log\frac\ell{\log(3/2)}\ge\log\ell\). If Corollary 4.1 held with \(\phi(\ell)\) in place of \(\log_2\ell\), then taking \(\sigma=\frac1M\) and \(M\) large, \(r=16\,\mathrm e^{50}\frac{1+\phi(\ell)}M<1\) would satisfy \(\frac r{1-r}\ge\frac{\log\ell}M\), that is, \(16\,\mathrm e^{50}(1+\phi(\ell))\ge(1-r)\log\ell\), which fails for large \(\ell\) and correspondingly large \(M\).

## References

- [OpenAI-KK2] OpenAI, *The second Kahn–Kalai conjecture*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-second-Kahn-Kalai-conjecture-September-24-2026
- [MNSZ-2] E. Mossel, J. Niles-Weed, N. Sun and I. Zadik, *A second moment proof of the spread lemma*, 2022; published as *A Bayesian proof of the spread lemma*, Random Structures & Algorithms 66 (2025). https://arxiv.org/abs/2209.11347
- [ALWZ] R. Alweiss, S. Lovett, K. Wu and J. Zhang, *Improved bounds for the sunflower lemma*, Annals of Mathematics 194 (2021), 795–815. https://arxiv.org/abs/1908.08483
- [FKNP] K. Frankston, J. Kahn, B. Narayanan and J. Park, *Thresholds versus fractional expectation-thresholds*, Annals of Mathematics 194 (2021), 475–495. https://arxiv.org/abs/1910.13433
