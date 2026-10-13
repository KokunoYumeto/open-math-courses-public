# Label Cover and the graph of the reduction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A graph with a proper coloring by three colors has an independent set that contains at least a third of its vertices: the largest of the three color classes. [OpenAI-I] proves that it is NP-hard to find, in such a graph, an independent set that contains even a small fixed fraction of the vertices. More exactly: for every \(\delta>0\) it is NP-hard to tell graphs with a proper coloring by three colors from graphs in which every independent set has fewer than \(\delta\,|V|\) vertices.

This lesson states the theorem, constructs the graph of the proof from a Label Cover instance, and proves that the graph has a proper coloring by three colors if all tests of the instance can be satisfied. The other five lessons of the course prove that the graph has no large independent set if only a small fraction of the tests can be satisfied.

- The theorem and its consequence for colorings (Section 1).
- Label Cover instances with value one or with small value (Theorem 2.1).
- Phases, links and the link distance (Section 3).
- The vertices and the edges of the graph (Section 4).
- The three colors (Theorem 5.2).

The lesson follows [OpenAI-I, Sections 1 to 3]. It needs finite probability, and for Theorem 2.1 the lesson [Projection games and the base game](course:two-to-one-games-with-perfect-completeness/projection-games-and-the-base-game) (Two-to-one games with perfect completeness).

## 1. The theorem

A *graph* is finite, has at least one vertex, and has no loops and no multiple edges. A set of vertices is *independent* if no two of its vertices are joined by an edge. A *proper coloring* with \(k\) colors gives every vertex one of \(k\) colors so that the two ends of every edge have different colors; each of its color classes is an independent set. A *formula* is a Boolean formula in conjunctive normal form with three literals per clause.

**Theorem 1.1** ([OpenAI-I]). Assume the hypotheses (PCP) and (PR) that are named below. For every real number \(\delta\) with \(0<\delta<\tfrac13\) there is a map, computable in polynomial time, from formulas \(\varphi\) to graphs \(G_\varphi\) such that

- if \(\varphi\) is satisfiable, then \(G_\varphi\) has a proper coloring with three colors;
- if \(\varphi\) is not satisfiable, then every independent set of \(G_\varphi\) has fewer than \(\delta\,|V(G_\varphi)|\) vertices.

The two hypotheses are theorems of the literature that this course does not prove: the PCP theorem and the parallel repetition theorem, in the forms stated in [Projection games and the base game](course:two-to-one-games-with-perfect-completeness/projection-games-and-the-base-game) (Two-to-one games with perfect completeness). They are used only in Theorem 2.1 below. The proof also uses a theorem of T. Austin on Lipschitz functions of many variables. It is stated as Theorem (J) in the second lesson, [Lipschitz functions on a torus: extension, juntas and influences](lipschitz-functions-on-a-torus-extension-juntas-and-influences.md), and it is proved in [Lipschitz functions are close to juntas](course:hypercontractivity-on-a-torus-and-juntas/lipschitz-functions-are-close-to-juntas) (Hypercontractivity on a torus and juntas for Lipschitz functions).

The course proves Theorem 1.1 in its last lesson, [The coefficient test and the theorem](the-coefficient-test-and-the-theorem.md). It is enough to prove it for rational \(\delta\): for a real \(\delta\) choose a rational \(\delta_0\) with \(0<\delta_0<\delta\) and take the map for \(\delta_0\).

**Corollary 1.2.** Assume (PCP) and (PR). Let \(3\le k\le c\) be integers. There is a map, computable in polynomial time, from formulas to graphs such that a satisfiable formula gives a graph with a proper coloring with \(k\) colors, and a formula that is not satisfiable gives a graph without a proper coloring with \(c\) colors.

**Proof.** Take the map of Theorem 1.1 for a \(\delta\) with \(0<\delta<\min\{\tfrac13,\tfrac1c\}\). A proper coloring with three colors is one with \(k\) colors, since \(k\ge3\). If a graph with \(n\) vertices has a proper coloring with \(c\) colors, one of the color classes has at least \(n/c>\delta n\) vertices, and it is independent. So the graph of a formula that is not satisfiable has no such coloring. \(\blacksquare\)

An algorithm that tells, in polynomial time, the graphs with a proper coloring by \(k\) colors from the graphs without a proper coloring by \(c\) colors would therefore decide in polynomial time whether a formula is satisfiable. The same holds for the two kinds of graphs of Theorem 1.1. This is the meaning of "NP-hard" in this course. Theorem 1.1 says more than Corollary 1.2 (Exercise 6.3).

## 2. Label Cover

**Definition.** A *Label Cover instance* \(\mathcal C\) consists of

- two finite sets \(U\) and \(V\) of *questions*;
- two nonempty finite sets \(\Sigma_L\) and \(\Sigma_R\) of *answers*;
- a nonempty finite list of *tests*; a test \(c\) has a question \(u_c\in U\), a question \(v_c\in V\) and a map \(\pi_c:\Sigma_L\to\Sigma_R\).

Several tests may have the same two questions and different maps. Every question occurs in at least one test. A *labeling* is a pair of maps \(\ell:U\to\Sigma_L\) and \(\rho:V\to\Sigma_R\). It *satisfies* the test \(c\) if
\[
\pi_c(\ell(u_c))=\rho(v_c).
\]
The *value* \(\operatorname{val}(\mathcal C)\) is the largest fraction of the tests of the list that one labeling satisfies. Equivalently, it is the largest probability, over the labelings, that a test drawn uniformly from the list is satisfied.

In the words of [Projection games and the base game](course:two-to-one-games-with-perfect-completeness/projection-games-and-the-base-game) (Two-to-one games with perfect completeness), a Label Cover instance is a projection game with the uniform law on a list of edges in which all questions of one player have the same set of answers.

**Theorem 2.1.** Assume (PCP) and (PR). For every \(\sigma>0\) there are finite sets \(\Sigma_L\), \(\Sigma_R\) and a map, computable in polynomial time, from formulas \(\varphi\) to Label Cover instances \(\mathcal C_\varphi\) with these sets of answers, such that \(\operatorname{val}(\mathcal C_\varphi)=1\) if \(\varphi\) is satisfiable and \(\operatorname{val}(\mathcal C_\varphi)\le\sigma\) if it is not.

**Proof.** Theorem 5.1 of the lesson on the base game gives, for a suitable integer \(t\ge1\) that depends only on \(\sigma\), a projection game computed from \(\varphi\) in polynomial time, with value \(1\) or at most \(\sigma\) in the two cases. Its edges are the \(t\)-tuples of pairs (clause, position) of a formula \(\Psi\), with the uniform law. The first player gets \(t\) clauses \(C_1,\dots,C_t\) and answers with an element of \(\mathcal A_{C_1}\times\dots\times\mathcal A_{C_t}\), where \(\mathcal A_C\subset\{0,1\}^3\) is the set of the seven triples that do not violate \(C\). The second player gets \(t\) variables and answers with an element of \(\{0,1\}^t\).

For every clause \(C\) number the seven triples of \(\mathcal A_C\) from \(1\) to \(7\) in their lexicographic order. This identifies every set of answers of the first player with \(\Sigma_L=\{1,\dots,7\}^t\), and it turns the map of every edge into a map from \(\Sigma_L\) to \(\Sigma_R=\{0,1\}^t\). Renaming the answers of a question by a bijection changes neither the satisfied edges of a labeling nor the value. Questions that occur in no edge are left out; this does not change the value either. \(\blacksquare\)

From here on the course works with one Label Cover instance \(\mathcal C\). The graph is constructed from \(\mathcal C\) and from a few numbers, which are chosen in the last lesson and depend only on \(\delta\).

## 3. Phases, links and the link distance

### The circle

Let \(\mathbb T=\mathbb R/\mathbb Z\). Its elements are called *phases*. For a phase \(x\) let \(\|x\|\) be the distance of a representative of \(x\) to the nearest integer. Then
\[
\begin{gathered}
0\le\|x\|\le\tfrac12,\qquad \|{-x}\|=\|x\|,\\
\|x+y\|\le\|x\|+\|y\|,
\end{gathered}
\]
and \(\|x-y\|\) is the *circle distance* of \(x\) and \(y\).

For a finite nonempty set \(M\) let \(\mathbb T^M\) be the set of the families \(x=(x_\kappa)_{\kappa\in M}\) of phases, one for each element of \(M\), with the *sup distance*
\[
d_\infty(x,y)=\max_{\kappa\in M}\|x_\kappa-y_\kappa\|.
\]
A map \(\pi:M\to M'\) between finite sets turns a family \(x\in\mathbb T^{M'}\) into the family \(x\circ\pi\in\mathbb T^{M}\) with \((x\circ\pi)_\kappa=x_{\pi(\kappa)}\), the *pullback* of \(x\). The *half shift* \(T\) adds \(\tfrac12\) to every phase of a family: \((Tx)_\kappa=x_\kappa+\tfrac12\).

**Lemma 3.1.** Let \(\pi:M\to M'\) be a map of finite nonempty sets, and \(x,y\in\mathbb T^{M'}\).

1. \(d_\infty(x\circ\pi,y\circ\pi)\le d_\infty(x,y)\).
2. \(T(x\circ\pi)=(Tx)\circ\pi\), \(T(Tx)=x\), \(d_\infty(Tx,Ty)=d_\infty(x,y)\) and \(d_\infty(x,Tx)=\tfrac12\).

**Proof.** (1) The left side is the maximum of \(\|x_\lambda-y_\lambda\|\) over the elements \(\lambda\) of the image of \(\pi\). (2) Both families of the first equation have the phase \(x_{\pi(\kappa)}+\tfrac12\) at \(\kappa\). The rest follows from \(\tfrac12+\tfrac12=0\) in \(\mathbb T\), from \((x_\kappa+\tfrac12)-(y_\kappa+\tfrac12)=x_\kappa-y_\kappa\) and from \(\|\tfrac12\|=\tfrac12\). \(\blacksquare\)

### The numbers of the construction

Fix integers \(r\ge s\ge2\) and \(m\ge1\), an even integer \(P\ge2\), a rational number \(\lambda\) with \(0<\lambda<1\), and a probability law \(\mu\) with rational values on the set of the subsets of \([r]=\{1,\dots,r\}\) with \(s\) elements. Put
\[
\begin{gathered}
D=mP,\\
\Gamma=\bigl\{0,\tfrac1D,\tfrac2D,\dots,\tfrac{D-1}D\bigr\}\subset\mathbb T .
\end{gathered}
\]
\(\Gamma\) is a subgroup of \(\mathbb T\), and it contains \(\tfrac12\) because \(D\) is even. So \(T\) maps \(\Gamma^M\) to itself.

### Tuples and their answers

The construction has \(r\) *layers*. A *tuple of the layer* \(i\in[r]\) is a sequence of \(r-1\) questions
\[
\mathbf q=(v_1,\dots,v_{i-1},u_i,\dots,u_{r-1}),
\]
with \(v_1,\dots,v_{i-1}\in V\) and \(u_i,\dots,u_{r-1}\in U\). So a tuple has the *positions* \(1,\dots,r-1\); in the layer \(i\) the positions before \(i\) hold questions of \(V\), the others questions of \(U\). The *set of answers* of the layer \(i\) is
\[
M_i=\Sigma_R^{\,i-1}\times\Sigma_L^{\,r-i},
\]
one answer for every position. All tuples of a layer have the same set of answers.

For \(i<r\) and a test \(c\) let
\[
\pi_c^{(i)}:M_i\to M_{i+1}
\]
be the map that applies \(\pi_c\) to the answer at the position \(i\) and leaves the other answers unchanged. A tuple \(\mathbf q\) of the layer \(i\) and a tuple \(\mathbf q'\) of the layer \(i+1\) are *joined by \(c\)* if they have the same questions at all positions other than \(i\), and \(\mathbf q\) has \(u_c\) and \(\mathbf q'\) has \(v_c\) at the position \(i\).

### The space of the points

A *point* is a pair \(\xi=(\mathbf q,x)\) of a tuple \(\mathbf q\) of some layer \(i\) and a family \(x\in\Gamma^{M_i}\). Let \(\mathscr X\) be the finite set of all points. The points with a given tuple \(\mathbf q\) form the *copy* of \(\mathbf q\). Put \(T(\mathbf q,x)=(\mathbf q,Tx)\).

There are two kinds of *links* between points:

- two points \((\mathbf q,x)\), \((\mathbf q,y)\) of one copy are joined by a link of the length \(d_\infty(x,y)\);
- if \(\mathbf q\) (layer \(i\)) and \(\mathbf q'\) (layer \(i+1\)) are joined by a test \(c\), then for every \(x\in\Gamma^{M_{i+1}}\) the points \((\mathbf q',x)\) and \((\mathbf q,x\circ\pi_c^{(i)})\) are joined by a link of the length \(0\).

The *link distance* \(\operatorname{dist}(\xi,\eta)\) of two points is the least sum of the lengths of a sequence of links that leads from \(\xi\) to \(\eta\); it is \(0\) for \(\xi=\eta\) and \(\infty\) if there is no such sequence.

**Lemma 3.2.** For all points \(\xi,\eta,\zeta\):

1. \(\operatorname{dist}(\xi,\eta)=\operatorname{dist}(\eta,\xi)\) and \(\operatorname{dist}(\xi,\zeta)\le\operatorname{dist}(\xi,\eta)+\operatorname{dist}(\eta,\zeta)\);
2. \(\operatorname{dist}((\mathbf q,x),(\mathbf q,y))\le d_\infty(x,y)\);
3. \(\operatorname{dist}(T\xi,T\eta)=\operatorname{dist}(\xi,\eta)\).

**Proof.** (1) A sequence of links can be reversed, and two sequences can be put one after the other. (2) is the link inside the copy. (3) By Lemma 3.1(2), \(T\) maps a link inside a copy to a link of the same length inside that copy, and it maps the link of length \(0\) between \((\mathbf q',x)\) and \((\mathbf q,x\circ\pi_c^{(i)})\) to the link of length \(0\) between \((\mathbf q',Tx)\) and \((\mathbf q,(Tx)\circ\pi_c^{(i)})\). So \(T\) maps sequences of links to sequences of the same length, and \(T\) is its own inverse. \(\blacksquare\)

Two different points can have the link distance \(0\). The link distance is finite or infinite, and all finite values are multiples of \(\tfrac1D\).

**Example 3.3** (\(r=2\)). The tuples of the layer \(1\) are the questions \(u\in U\), with the set of answers \(\Sigma_L\); those of the layer \(2\) are the questions \(v\in V\), with \(\Sigma_R\). For every test \(c\) and every \(x\in\Gamma^{\Sigma_R}\) there is a link of length \(0\) between \((v_c,x)\) and \((u_c,x\circ\pi_c)\).

Let \(U=\{u\}\), \(V=\{v\}\), \(\Sigma_L=\Sigma_R=\{0,1\}\), with two tests: one with the identity map and one with the map that exchanges \(0\) and \(1\). A labeling satisfies exactly one of them, so the value is \(\tfrac12\). The point \((v,(x_0,x_1))\) has links of length \(0\) to \((u,(x_0,x_1))\) and to \((u,(x_1,x_0))\). So the points \(\xi=(u,(0,\tfrac12))\) and \((u,(\tfrac12,0))=T\xi\) have the link distance \(0\), although their sup distance is \(\tfrac12\).

### The first branch

If there is a point \(\xi\in\mathscr X\) with
\[
\operatorname{dist}(\xi,T\xi)\le\tfrac18,
\]
the graph of the construction is the complete graph on \(k_\delta=\lfloor1/\delta\rfloor+1\) vertices. Its independent sets have one vertex, and \(1<\delta k_\delta\). This case is called the *first branch*. Theorem 5.2 shows that it does not occur when the value of \(\mathcal C\) is \(1\).

## 4. The vertices and the edges

Suppose that \(\operatorname{dist}(\xi,T\xi)>\tfrac18\) for every point \(\xi\). The vertices of the graph are the outcomes of a random experiment.

A *coefficient* is one of the numbers \(0,\tfrac1m,\tfrac2m,\dots,1\). The *law of the coefficients* gives \(\tfrac km\), for \(0\le k\le m\), the probability
\[
p_k=\frac{\lambda^k}{1+\lambda+\dots+\lambda^m},
\]
so that \(p_k=\lambda\,p_{k-1}\).

**The experiment.**

1. Draw tests \(c_1,\dots,c_{r-1}\) independently and uniformly from the list. This is a *chain*. Write \(u_h=u_{c_h}\) and \(v_h=v_{c_h}\). The chain has, for every \(i\in[r]\), the tuple
\[
\mathbf q_i=(v_1,\dots,v_{i-1},u_i,\dots,u_{r-1}),
\]
one in every layer, and \(\mathbf q_i\), \(\mathbf q_{i+1}\) are joined by \(c_i\). For \(i\le j\) let
\[
\pi_{ij}=\pi_{c_{j-1}}^{(j-1)}\circ\dots\circ\pi_{c_i}^{(i)}:M_i\to M_j ,
\]
the map that applies \(\pi_{c_h}\) at every position \(h\) with \(i\le h<j\); \(\pi_{ii}\) is the identity.
2. Independently, draw a set \(B\) with the law \(\mu\). For every \(j\in B\) draw a coefficient \(t_j\) with the law of the coefficients, and for every \(j\in B\) and every \(\ell\in M_j\) a *rotation* \(\widehat\theta_{j,\ell}\), uniform in \(\{0,\tfrac1P,\dots,\tfrac{P-1}P\}\). All these are independent.
3. Let \(b=\min B\). The *location* of the outcome is the point \((\mathbf q_b,x)\) with
\[
x_\kappa=\sum_{j\in B}t_j\,\widehat\theta_{j,\pi_{bj}(\kappa)}\quad(\kappa\in M_b),
\]
read as a phase.

**Lemma 4.1.** (1) \(\pi_{jk}\circ\pi_{ij}=\pi_{ik}\) for \(i\le j\le k\). (2) For \(i\le j\) and \(x\in\Gamma^{M_j}\), the points \((\mathbf q_j,x)\) and \((\mathbf q_i,x\circ\pi_{ij})\) have the link distance \(0\). (3) The location of an outcome is a point of \(\mathscr X\).

**Proof.** (1) is clear from the definition. (2) For \(j=i+1\) this is a link of length \(0\), because \(\mathbf q_i\) and \(\mathbf q_{i+1}\) are joined by \(c_i\). In general, the points \((\mathbf q_h,x\circ\pi_{hj})\) for \(h=j,j-1,\dots,i\) are joined in turn by links of length \(0\), since \(x\circ\pi_{hj}=(x\circ\pi_{h+1,j})\circ\pi_{c_h}^{(h)}\). (3) Every product \(t_j\widehat\theta_{j,\ell}\) is a multiple of \(\tfrac1{mP}=\tfrac1D\). \(\blacksquare\)

**The vertices.** An outcome consists of the chain, the set \(B\), the coefficients and the rotations. Let \(N\) be the number of the tests. The chain has the probability \(N^{-(r-1)}\), and for a given chain the rest of the outcome has the probability
\[
\mu(B)\prod_{j\in B}p_{k_j}\cdot P^{-\sum_{j\in B}|M_j|},
\]
where \(t_j=k_j/m\). These are finitely many rational numbers that do not depend on the instance, only on the numbers of the construction and on \(|\Sigma_L|\), \(|\Sigma_R|\). Let \(C_0\) be a common denominator of them. The graph has, for every outcome \(\omega\) of positive probability, exactly \(C_0N^{r-1}\Pr(\omega)\) vertices; they are called the *copies* of \(\omega\), and their *location* is the location of \(\omega\). So the graph has \(C_0N^{r-1}\) vertices, and a vertex drawn uniformly is a copy of an outcome that has the law of the experiment.

**The edges.** Two different vertices with the locations \(\xi\) and \(\eta\) are joined by an edge if and only if
\[
\operatorname{dist}(\xi,T\eta)\le\tfrac18 .
\]
The condition is symmetric in the two vertices: by Lemma 3.2, \(\operatorname{dist}(\xi,T\eta)=\operatorname{dist}(T\xi,TT\eta)\), and this is \(\operatorname{dist}(\eta,T\xi)\). Two different vertices with the same location \(\xi\) are not joined, because \(\operatorname{dist}(\xi,T\xi)>\tfrac18\) in this branch.

This defines the graph \(G(\mathcal C)\) of the instance; in the first branch \(G(\mathcal C)\) is the complete graph on \(k_\delta\) vertices.

**Proposition 4.2.** For fixed numbers \(r,s,m,P,\lambda,\mu,k_\delta\) and fixed sets of answers, the graph \(G(\mathcal C)\) can be computed from the list of the tests of \(\mathcal C\) in a time that is polynomial in the number \(N\) of the tests.

**Proof.** Every question occurs in a test, so \(|U|,|V|\le N\). A layer has at most \(N^{r-1}\) tuples, and a copy has at most \(D^a\) points, where \(a=\max\{|\Sigma_L|,|\Sigma_R|\}^{r-1}\) is a constant. So \(\mathscr X\) has at most \(rN^{r-1}D^a\) points. The links of length \(0\) are listed by running through the layers \(i<r\), the tests, the tuples of the layer \(i\) with \(u_c\) at the position \(i\), and the families \(x\). All lengths are integers after multiplication by \(D\), and the link distances of all pairs of points are computed by an algorithm for shortest paths in a time polynomial in the number of the points. This decides the first branch. Otherwise the \(C_0N^{r-1}\) vertices and their locations are listed by running through the chains and, for each chain, through the finitely many sets \(B\), coefficients and rotations; the edges are found by looking up the link distance for every pair of vertices. \(\blacksquare\)

## 5. The three colors

**Lemma 5.1.** Let \((\ell,\rho)\) be a labeling that satisfies all tests of \(\mathcal C\). For a tuple \(\mathbf q=(v_1,\dots,v_{i-1},u_i,\dots,u_{r-1})\) let
\[
\begin{aligned}
\kappa(\mathbf q)=\bigl(&\rho(v_1),\dots,\rho(v_{i-1}),\\
&\ell(u_i),\dots,\ell(u_{r-1})\bigr)\in M_i
\end{aligned}
\]
be the tuple of its answers, and let
\[
\phi(\mathbf q,x)=x_{\kappa(\mathbf q)}\in\mathbb T
\]
be the phase of a point at these answers. Then for all points \(\xi,\eta\)
\[
\begin{gathered}
\|\phi(\xi)-\phi(\eta)\|\le\operatorname{dist}(\xi,\eta),\\
\phi(T\xi)=\phi(\xi)+\tfrac12 .
\end{gathered}
\]

**Proof.** The second statement is the definition of \(T\). For the first it is enough to consider one link, by the triangle inequality for the circle distance. For a link inside a copy, \(\|x_\kappa-y_\kappa\|\le d_\infty(x,y)\) for every \(\kappa\). For a link of length \(0\) between \((\mathbf q',x)\) and \((\mathbf q,x\circ\pi_c^{(i)})\), where \(\mathbf q\) and \(\mathbf q'\) are joined by \(c\): the tuples \(\kappa(\mathbf q)\) and \(\kappa(\mathbf q')\) agree outside the position \(i\), where the first has \(\ell(u_c)\) and the second has \(\rho(v_c)=\pi_c(\ell(u_c))\), because the labeling satisfies \(c\). So \(\pi_c^{(i)}(\kappa(\mathbf q))=\kappa(\mathbf q')\), and
\[
\begin{aligned}
\phi(\mathbf q,x\circ\pi_c^{(i)})&=x_{\pi_c^{(i)}(\kappa(\mathbf q))}\\
&=x_{\kappa(\mathbf q')}=\phi(\mathbf q',x).
\end{aligned}
\]
The two ends of the link have the same phase. \(\blacksquare\)

**Theorem 5.2.** If \(\operatorname{val}(\mathcal C)=1\), then the first branch does not occur, and the graph \(G(\mathcal C)\) has a proper coloring with three colors.

**Proof.** Take a labeling that satisfies all tests, and \(\phi\) as in Lemma 5.1. For every point \(\xi\),
\[
\begin{aligned}
\operatorname{dist}(\xi,T\xi)&\ge\|\phi(\xi)-\phi(T\xi)\|\\
&=\|\tfrac12\|=\tfrac12>\tfrac18,
\end{aligned}
\]
so the first branch does not occur. Color a vertex with the location \(\xi\) by the one of the three sets
\[
[0,\tfrac13),\qquad[\tfrac13,\tfrac23),\qquad[\tfrac23,1)
\]
that contains the representative of \(\phi(\xi)\) in \([0,1)\). Let two vertices with the locations \(\xi\), \(\eta\) be joined by an edge. Then
\[
\begin{aligned}
\|\phi(\xi)-\phi(\eta)-\tfrac12\|&=\|\phi(\xi)-\phi(T\eta)\|\\
&\le\operatorname{dist}(\xi,T\eta)\le\tfrac18 ,
\end{aligned}
\]
and so, by the triangle inequality,
\[
\|\phi(\xi)-\phi(\eta)\|\ge\|\tfrac12\|-\tfrac18=\tfrac38>\tfrac13 .
\]
Two phases with representatives in the same one of the three sets have a circle distance of less than \(\tfrac13\). So the two vertices have different colors. \(\blacksquare\)

In the coloring all copies of an outcome, and all vertices with the same location, have the same color. The links of length \(0\) are what makes the coloring possible: they force the phase at the chosen answers to be the same along a chain, and this needs a labeling that satisfies every test.

**What remains.** Suppose that \(\operatorname{val}(\mathcal C)\le\sigma\) for a small \(\sigma\), and that the first branch does not occur. The following lessons show that, for suitable numbers of the construction, every independent set of \(G(\mathcal C)\) has fewer than \(\delta\,|V(G(\mathcal C))|\) vertices. The proof starts from an independent set \(\mathcal A\) and turns it into Lipschitz functions on the sets \(\mathbb T^{M_i}\) ([From an independent set to lists of answers](from-an-independent-set-to-lists-of-answers.md)); a labeling that satisfies many tests is found from the few answers on which these functions depend.

## 6. Exercises

**6.1.** In the instance of Example 3.3 show that \(\operatorname{dist}(\xi,T\xi)\le\tfrac12-\|x_0-x_1\|\) for the point \(\xi=(u,(x_0,x_1))\). For which \(D\) is there a point with \(\operatorname{dist}(\xi,T\xi)=0\)?

**6.2.** Let \(r=3\) and let \(c_1,c_2\) be a chain. Write the three tuples, the three sets of answers and the map \(\pi_{13}\). For \(B=\{1,3\}\) write the phase of the location at an answer \(\kappa=(a_1,a_2)\), and say which rotations of the layer \(3\) occur in the location.

**6.3.** Let \(G\) be a graph with \(n\) vertices and at least one edge, and let \(G^+\) be \(G\) together with \(n'\) further vertices that are joined to no vertex. Show that \(G\) and \(G^+\) have proper colorings with the same numbers of colors, and that \(G^+\) has an independent set with at least \(n'\) of its \(n+n'\) vertices. Conclude that the second statement of Corollary 1.2 does not imply the second statement of Theorem 1.1.

**6.4.** Let \(r=s=2\), \(m=1\), \(P=2\), \(\lambda=\tfrac12\) and \(|\Sigma_L|=|\Sigma_R|=2\). Find the law of the coefficients, a common denominator \(C_0\), the number of the vertices, and the number of the copies of an outcome with the coefficients \(t_1=0\), \(t_2=1\).

**6.5.** Show that Theorem 5.2 remains true if the number \(\tfrac18\) in the rule for the edges and in the first branch is replaced by any number \(\eta\) with \(0\le\eta<\tfrac16\).

## 7. Solutions

**6.1.** The points \((u,(x_0,x_1))\) and \((u,(x_1,x_0))\) have the link distance \(0\): both have a link of length \(0\) to \((v,(x_0,x_1))\), the first by the test with the identity and the second by the test with the exchange. Inside the copy of \(u\), the points \((u,(x_1,x_0))\) and \(T\xi=(u,(x_0+\tfrac12,x_1+\tfrac12))\) have the sup distance
\[
\|x_0-x_1-\tfrac12\|=\tfrac12-\|x_0-x_1\| ,
\]
since the two phases of their difference are \(x_1-x_0-\tfrac12\) and its negative, and \(\|y-\tfrac12\|=\tfrac12-\|y\|\) for every phase \(y\). The triangle inequality gives the claim. The bound is \(0\) for \(x_1=x_0+\tfrac12\), and \(\tfrac12\in\Gamma\) for every even \(D\): for every \(D\) of the construction the point \((u,(0,\tfrac12))\) has \(\operatorname{dist}(\xi,T\xi)=0\), and the first branch occurs.

**6.2.** \(\mathbf q_1=(u_1,u_2)\), \(\mathbf q_2=(v_1,u_2)\), \(\mathbf q_3=(v_1,v_2)\); \(M_1=\Sigma_L^2\), \(M_2=\Sigma_R\times\Sigma_L\), \(M_3=\Sigma_R^2\); \(\pi_{13}(a_1,a_2)=(\pi_{c_1}(a_1),\pi_{c_2}(a_2))\). For \(B=\{1,3\}\), \(b=1\) and
\[
x_{(a_1,a_2)}=t_1\widehat\theta_{1,(a_1,a_2)}+t_3\,\widehat\theta_{3,(\pi_{c_1}(a_1),\pi_{c_2}(a_2))} .
\]
Only the rotations \(\widehat\theta_{3,\ell}\) with \(\ell\) in the image of \(\pi_{13}\) occur, and two answers with the same image under \(\pi_{13}\) get the same second term.

**6.3.** A proper coloring of \(G^+\) gives one of \(G\) by restriction. A proper coloring of \(G\) with \(k\) colors is extended to \(G^+\) by giving the new vertices any of the colors. The new vertices form an independent set of \(G^+\). So if \(G\) has no proper coloring with \(c\) colors, neither has \(G^+\), although the largest independent set of \(G^+\) contains the fraction \(n'/(n+n')\) of the vertices, which is close to \(1\) for large \(n'\). A map to graphs without proper colorings by \(c\) colors does therefore not bound the size of the independent sets, while the proof of Corollary 1.2 shows the converse implication.

**6.4.** \(p_0=\frac{1}{1+1/2}=\tfrac23\) and \(p_1=\tfrac13\). Here \(B=\{1,2\}\) with probability \(1\), and there are \(|M_1|+|M_2|=4\) rotations, each with two values. For a given chain an outcome has the probability \(p_{k_1}p_{k_2}/16\), one of \(\tfrac{4}{144},\tfrac{2}{144},\tfrac{1}{144}\). So \(C_0=144\) is a common denominator, the graph has \(144\,N\) vertices, and an outcome with \(t_1=0\), \(t_2=1\) has \(144\cdot\tfrac23\cdot\tfrac13\cdot\tfrac1{16}=2\) copies.

**6.5.** The proof of Theorem 5.2 uses the number only twice. First, \(\operatorname{dist}(\xi,T\xi)\ge\tfrac12>\eta\), so the first branch does not occur. Second, for an edge, \(\|\phi(\xi)-\phi(\eta)\|\ge\tfrac12-\eta>\tfrac13\) exactly because \(\eta<\tfrac16\), and this is all that the three sets of length \(\tfrac13\) need.

## References

- [OpenAI-I] OpenAI, *Hardness of finding large independent sets in three-colorable graphs*, OpenAI Math Release preprint, 24 September 2026, Sections 1 to 3. https://github.com/openai/math/tree/main/preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026
