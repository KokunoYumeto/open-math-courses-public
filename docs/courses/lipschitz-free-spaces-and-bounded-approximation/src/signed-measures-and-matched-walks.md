# Signed measures and matched walks

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson begins the proof of the theorem on blocks: no operator of finite rank and norm at most \(p\) on the free space of the block \(M_p\) is close to the identity at all anchors. Suppose there is such an operator. After a small change its range is spanned by the evaluations at finitely many points, the *support* \(S\). Then the operator assigns to every point \(x\) of the block a signed measure \(\mu_x\) on \(S\), of total mass \(1\) and of bounded total variation. Because the operator is close to the identity at the anchors, the measure \(\mu_x\) of a graph vertex \(x\) is concentrated, in a weak sense, on the points of \(S\) whose labels are close to the label of \(x\).

The second half of the lesson is about the graphs alone. It studies walks in a graph that can be followed by points of \(S\) with close labels, the *matched walks*. Long matched walks start at few vertices. At the other vertices, each point of \(S\) singles out at most one direction, and of two neighbouring vertices with nearby followers, one singles out the direction to the other. The next lesson combines the two halves.

- The setting (Section 1) and a common finite support (Lemma 2.1).
- Bumps and signed measures (Lemmas 3.1 and 3.2).
- Compatible pairs and matched walks (Section 4).
- Long matched walks are rare (Proposition 5.1).
- Records and exceptional directions (Lemma 6.1).

The lesson follows [OpenAI-LF, Sections 4 and 5]. It uses the free space of [Lipschitz-free spaces and approximation properties](lipschitz-free-spaces-and-approximation-properties.md) (Lemma 1.1 there) and the block of [Colored graphs with a tree limit](colored-graphs-with-a-tree-limit.md): Corollary 2.5, Lemma 3.1 and Proposition 5.1 there. It uses that linear functionals on a normed space of finite dimension are bounded (core course [Functional Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D20)).

## 1. The setting

Fix an integer \(p\ge1\). The lesson on colored graphs fixed numbers
\[
L,\ R,\ K,\ D,\ B,\ V,\ \Delta,\ Q,\ H,\ k ,
\]
a sequence \(G_1,G_2,\dots\) of finite \(\Delta\)-regular multigraphs with vertex colors in \(\{1,\dots,k\}\), and the block \((M_p,d_p,o)\): its points are the vertices of the graphs \(G_m\) (the *source vertices*) and finitely many *anchors*, which form the set \(A_p\). Every point \(t\) has a label \(h(t)\in\{0,\dots,D\}^k\), and every source vertex \(x\) has an anchor \(a(x)\). We use the following facts.

- (G1) \(d_p(u,u')\ge1\) for \(u\ne u'\); the diameter is at most \(B\); the ends of a source edge have a distance of at most \(1\).
- (G2) \(\|h(u)-h(u')\|_\infty\le d_p(u,u')\); a source vertex of color \(i\) has \(h_i(x)=0\); \(h(a(x))=h(x)\).
- (G3) \(d_p(x,a(x))=R\) for every source vertex \(x\).
- (G4) Every closed ball of radius \(2L\) has at most \(Q\) points; every label has at most \(H\) coordinates less than \(D\).
- (N) \(L=10p\); \(L\le K\); \((2pR+1)/K\le\tfrac15\); \(K+2L+1=D-4\); \(V=1+4pB\); \(V/\Delta<\tfrac1{20}\); \(\Delta QH/k<\tfrac12\).
- (T) For every property of a vertex that can be read off from its colored ball of radius \(n\), the fraction of the vertices of \(G_m\) with this property converges, as \(m\to\infty\), to the probability that the root of the \(\Delta\)-regular tree with independent uniform colors has it.

In the free space \(\mathcal F(M_p)\) we use \(\|\delta_x-\delta_y\|=d_p(x,y)\), so \(\|\delta_x\|\le B\), and that the evaluation combinations are dense.

## 2. A common finite support

An operator of finite rank need not have a range that is spanned by finitely many evaluations. A small change achieves this.

**Lemma 2.1.** Let \(T_0\) be a bounded linear operator of finite rank on \(\mathcal F(M_p)\) with \(\|T_0\|\le p\) and
\[
\|T_0\delta_a-\delta_a\|<\tfrac12\qquad(a\in A_p) .
\]
Then there are a finite set \(S\subseteq M_p\) with \(o\in S\) and a bounded linear operator \(T\) on \(\mathcal F(M_p)\) such that:

1. the range of \(T\) lies in the span of the \(\delta_j\), \(j\in S\);
2. \(\|T\|\le2p\);
3. \(\|T\delta_a-\delta_a\|<1\) for all \(a\in A_p\).

**Proof.** If \(T_0=0\), take \(T=0\) and \(S=\{o\}\). Otherwise let \(v_1,\dots,v_r\) be a basis of the range of \(T_0\). The coordinates of a vector of the range in this basis are linear functionals on a space of finite dimension, so they are bounded. Composing them with \(T_0\) gives bounded functionals \(\phi_1,\dots,\phi_r\) on \(\mathcal F(M_p)\) with
\[
T_0u=\sum_{i=1}^r\phi_i(u)\,v_i .
\]
Let \(0<\eta<\min\{p,\ 1/(2B)\}\). Choose evaluation combinations \(w_i\) so close to \(v_i\) that \(\sum_i\|\phi_i\|\,\|w_i-v_i\|<\eta\), and put \(Tu=\sum_i\phi_i(u)\,w_i\). Then \(\|T-T_0\|<\eta\). Let \(S\) consist of \(o\) and of the finitely many points that occur in the \(w_i\). Then \(\|T\|<p+\eta<2p\), and for an anchor \(a\)
\[
\begin{aligned}
\|T\delta_a-\delta_a\|&\le\|T_0\delta_a-\delta_a\|\\
&\quad+\|T-T_0\|\,\|\delta_a\|\\
&<\tfrac12+\eta B<1 .
\end{aligned}
\]
\(\blacksquare\)

## 3. Bumps and signed measures

For a source vertex \(x\) define a function \(b_x\) on \(M_p\) by
\[
b_x(t)=L\,\Bigl(1-\frac{\|h(x)-h(t)\|_\infty}{K}\Bigr)_+ ,
\]
where \(s_+=\max\{s,0\}\). It depends on \(x\) only through the label of \(x\).

**Lemma 3.1.** The function \(b_x\) has values in \([0,L]\), satisfies \(|b_x(t)-b_x(t')|\le\frac LK\,d_p(t,t')\le d_p(t,t')\), and \(b_x(a(x))=L\). Further \(b_x(t)>0\) exactly if \(\|h(x)-h(t)\|_\infty<K\).

**Proof.** By (G2), \(t\mapsto\|h(x)-h(t)\|_\infty\) changes by at most \(d_p(t,t')\) between \(t\) and \(t'\); multiplying by \(L/K\), subtracting from \(L\) and taking the positive part does not increase differences. \(L/K\le1\) by (N), and \(h(a(x))=h(x)\) by (G2). \(\blacksquare\)

A *signed measure* \(\nu\) on a finite set \(S\) is a family of real numbers \(\nu(\{j\})\), \(j\in S\). For a function \(g\) on \(S\) and a set \(E\subseteq S\) write
\[
\begin{gathered}
\int g\,d\nu=\sum_{j\in S}g(j)\,\nu(\{j\}),\\
|\nu|(E)=\sum_{j\in E}|\nu(\{j\})|,\\
\|\nu\|_{\mathrm{TV}}=|\nu|(S) .
\end{gathered}
\]
The number \(\sum_j\nu(\{j\})\) is the *total mass* and \(\|\nu\|_{\mathrm{TV}}\) the *total variation*. If \(g=0\) outside \(E\) and \(|g|\le c\) on \(E\), then \(|\int g\,d\nu|\le c\,|\nu|(E)\).

**Lemma 3.2** (the measures of an operator). Let \(S\subseteq M_p\) be finite with \(o\in S\), and let \(T\) be a bounded linear operator on \(\mathcal F(M_p)\) with the three properties of Lemma 2.1. Then there are signed measures \(\mu_x\) on \(S\), for \(x\in M_p\), each of total mass \(1\), with the following three properties.

(1) For every Lipschitz function \(g\) on \(M_p\) and all \(x\),
\[
\int g\,d\mu_x=(T\delta_x)\bigl(g-g(o)\bigr)+g(o) .
\]

(2) \(\|\mu_x\|_{\mathrm{TV}}\le V\) for all \(x\).

(3) \(\int b_x\,d\mu_x\ge\frac34L\) for every source vertex \(x\).

In (1), \(g-g(o)\) lies in \(\operatorname{Lip}_0(M_p)\), so the element \(T\delta_x\) of the free space can be applied to it.

**Proof.** Since \(\delta_o=0\), we can write \(T\delta_x=\sum_{j\in S\setminus\{o\}}c_x(j)\,\delta_j\) with real numbers \(c_x(j)\). Put
\[
\begin{aligned}
\mu_x(\{j\})&=c_x(j)\qquad(j\in S,\ j\ne o),\\
\mu_x(\{o\})&=1-\sum_{j\ne o}c_x(j) .
\end{aligned}
\]
The total mass is \(1\), and
\[
\begin{aligned}
\int g\,d\mu_x&=\sum_{j\ne o}c_x(j)\bigl(g(j)-g(o)\bigr)\\
&\quad+g(o) ,
\end{aligned}
\]
which is (1).

*Proof of (2).* Let \(g(j)\) be \(1\), \(-1\) or \(0\) according to whether \(\mu_x(\{j\})\) is positive, negative or zero, for \(j\in S\), and \(g=0\) outside \(S\). Two values of \(g\) differ by at most \(2\), and two different points have a distance of at least \(1\). So \(g-g(o)\) has a Lipschitz constant of at most \(2\), and by (1)
\[
\begin{aligned}
\|\mu_x\|_{\mathrm{TV}}=\int g\,d\mu_x&\le2\,\|T\delta_x\|+1\\
&\le2\cdot2p\cdot B+1=V .
\end{aligned}
\]

*Proof of (3).* Let \(x\) be a source vertex and \(a=a(x)\). By (G3) and the properties of \(T\),
\[
\begin{aligned}
\|T\delta_x-\delta_a\|&\le\|T(\delta_x-\delta_a)\|\\
&\quad+\|T\delta_a-\delta_a\|\\
&\le2pR+1 .
\end{aligned}
\]
The function \(b_x-b_x(o)\) has a Lipschitz constant of at most \(L/K\), and \(\delta_a(b_x-b_x(o))=L-b_x(o)\). So by (1)
\[
\begin{aligned}
&\int b_x\,d\mu_x-L\\
&\quad=(T\delta_x-\delta_a)\bigl(b_x-b_x(o)\bigr)\\
&\quad\ge-\frac LK\,(2pR+1)\ \ge\ -\frac L5 ,
\end{aligned}
\]
by (N). \(\blacksquare\)

The measures \(\mu_x\) may have negative parts; no positivity is available. All of them have the total mass \(1\), so \(\mu_x-\mu_y\) gives the value \(0\) to constant functions, and (1) gives
\[
\begin{aligned}
&\int g\,d(\mu_x-\mu_y)\\
&\qquad=\bigl(T(\delta_x-\delta_y)\bigr)\bigl(g-g(o)\bigr) .
\end{aligned}
\]
If \(x\) and \(y\) are the ends of a source edge and \(g\) has a Lipschitz constant of at most \(1\), the right side is at most \(\|T\|\,d_p(x,y)\le2p\) in absolute value. On the other hand \(\mu_x\) gives a large value to \(b_x\), and \(\mu_y\) to \(b_y\). The plan is to find, for many edges, a function \(g\) with a Lipschitz constant of at most \(1\) that is close to \(b_x\) where \(\mu_x\) lives and close to \(-b_y\) where \(\mu_y\) lives. Then the left side is about \(\frac34L+\frac34L\), which is much larger than \(2p\). The obstacle is that \(b_x\) and \(-b_y\) are far apart at points of \(S\) where both are large. The rest of this lesson shows how to give up few points of \(S\) so that the remaining requirements are consistent.

## 4. Compatible pairs and matched walks

From here on \(S\subseteq M_p\) is a fixed finite set with \(o\in S\). Its points are called *states*. Nothing else is assumed about \(S\): it may contain anchors and vertices of several graphs.

**Definition.** A source vertex \(x\) and a state \(j\) are *compatible* if
\[
\|h(x)-h(j)\|_\infty\le K+2L+1 .
\]
A nonbacktracking walk \(x_0,e_1,x_1,\dots,e_t,x_t\) in one of the graphs \(G_m\) is *matched* if there are states \(j_0,\dots,j_t\) such that \(x_s\) and \(j_s\) are compatible for \(0\le s\le t\) and
\[
d_p(j_{s-1},j_s)\le2L\qquad(1\le s\le t) .
\]
We then say that the walk is matched *with the initial state* \(j_0\). It *starts at* \(x_0\) and *starts through* the incidence \(e_1\).

The states may repeat, and so may the vertices. A part \(x_0,e_1,\dots,x_s\) of a matched walk is matched, with the same initial state.

The bound \(K+2L+1\) is the sum of three numbers: a label distance below \(K\), at which a bump is positive; one step along a source edge, which changes the label by at most \(1\); and one step between states of distance at most \(2L\). By (N) it is \(D-4\), less than the height \(D\) at which labels are cut off. This is used in the following way.

**Lemma 4.1.** For a state \(j\) let \(C_j\) be the set of the colors \(i\) with \(h_i(j)<D\). Then \(|C_j|\le H\), and if a source vertex \(x\) is compatible with \(j\), then the color of \(x\) lies in \(C_j\).

**Proof.** \(|C_j|\le H\) by (G4). If \(x\) has the color \(i\), then \(h_i(x)=0\) by (G2), so \(h_i(j)\le K+2L+1<D\). \(\blacksquare\)

So a state admits few of the \(k\) colors for the vertices that it can follow.

## 5. Long matched walks are rare

**Proposition 5.1.** Let \(n\ge1\), and let \(\beta_m\) be the fraction of the vertices of \(G_m\) at which a matched walk of length \(n\) starts. Then
\[
\limsup_{m\to\infty}\beta_m\le|S|\,\frac Hk\,\Bigl(\frac{\Delta QH}{k}\Bigr)^n .
\]
Consequently there are \(n\ge2\) and \(m\) with \(\beta_m<\dfrac1{20V}\).

**Proof.** *A weaker property.* Say that a vertex \(x\) of a colored \(\Delta\)-regular multigraph has the property \((\mathrm W)\) if there are a nonbacktracking walk \(x=x_0,e_1,x_1,\dots,e_n,x_n\) and states \(j_0,\dots,j_n\) with \(d_p(j_{s-1},j_s)\le2L\) for \(1\le s\le n\) and with the color of \(x_s\) in \(C_{j_s}\) for \(0\le s\le n\). By Lemma 4.1 every vertex of \(G_m\) at which a matched walk of length \(n\) starts has the property \((\mathrm W)\).

The property \((\mathrm W)\) of \(x\) can be read off from the colored ball of radius \(n\) around \(x\): a walk of length \(n\) from \(x\) uses only vertices and edge instances of this ball, and the property mentions only their colors. The set \(S\), the sets \(C_j\) and the pairs of states at a distance of at most \(2L\) are fixed. By (T) the fraction of the vertices of \(G_m\) with \((\mathrm W)\) converges to the probability \(\varrho\) that the root of the \(\Delta\)-regular tree with independent uniform colors has \((\mathrm W)\). So \(\limsup\beta_m\le\varrho\).

*The tree.* In the tree, a nonbacktracking walk from the root goes one level down at every step: after the first step it is at a child of the root, and a step that does not reverse the step before cannot go to the parent. So it visits \(n+1\) different vertices, and there are at most \(\Delta^n\) such walks. A sequence of states \(j_0,\dots,j_n\) as in \((\mathrm W)\) is given by one of \(|S|\) states \(j_0\) and, at each step, one of the at most \(Q\) states in the closed ball of radius \(2L\) around the state before, by (G4). So there are at most \(|S|\,Q^n\) such sequences. For a fixed walk and a fixed sequence of states, the colors of the \(n+1\) different vertices are independent and uniform, so the probability that the color of \(x_s\) lies in \(C_{j_s}\) for all \(s\) is at most \((H/k)^{n+1}\). Summing over the walks and the sequences,
\[
\varrho\le\Delta^n\cdot|S|\,Q^n\cdot\Bigl(\frac Hk\Bigr)^{n+1} ,
\]
which is the bound of the proposition.

*The choice.* By (N), \(\Delta QH/k<\tfrac12\). Choose \(n\ge2\) so large that \(|S|\,\frac Hk\,2^{-n}<\frac1{40V}\). Then \(\beta_m<\frac1{20V}\) for all large \(m\). \(\blacksquare\)

The proof replaced compatibility by the weaker condition on the colors, because the colors of different vertices of the tree are independent, while the labels are not. The set \(S\) may have been chosen with knowledge of the whole sequence of graphs. This does no harm: the graphs are fixed objects, and once \(S\) is fixed, \((\mathrm W)\) is one fixed property of colored balls, to which (T) applies.

## 6. Records and exceptional directions

Fix \(n\ge2\) and one of the graphs, \(G=G_m\). Call a vertex of \(G\) *bad* if a matched walk of length \(n\) starts at it, and *good* otherwise.

Let \(x\) be a good vertex, \(e\in\mathcal D(x)\) an incidence that starts at \(x\), and \(j\) a state. A matched walk that starts at \(x\) has a length of at most \(n-1\), because its first \(n\) steps would be a matched walk of length \(n\). The *record* \(r_x(e,j)\) is the largest length of a matched walk that starts through \(e\) with the initial state \(j\); it is \(0\) if there is no such walk of positive length. So \(0\le r_x(e,j)\le n-1\).

**Definition.** Let \(x\) be a good vertex and \(j\) a state. An incidence \(e\in\mathcal D(x)\) is *exceptional at* \((x,j)\) if
\[
r_x(e,j)>r_x(e',j)
\]
for all \(e'\in\mathcal D(x)\) with \(e'\ne e\). At a bad vertex \(x\), every incidence in \(\mathcal D(x)\) is called exceptional at \((x,j)\) for every state \(j\). For an incidence \(e\colon x\to y\) let \(E_e\) be the set of the states \(j\in S\) for which \(e\) is exceptional at \((x,j)\).

At a good vertex and for a fixed state there is at most one exceptional incidence: the one with the strictly largest record, if the largest record is not attained twice. So at a good vertex \(x\) every state lies in at most one of the \(\Delta\) sets \(E_e\), \(e\in\mathcal D(x)\).

**Lemma 6.1** (exceptional directions). Let \(e\colon x\to y\) be an incidence of \(G\), and let \(j,j'\) be states such that \(x\) and \(j\) are compatible, \(y\) and \(j'\) are compatible, and \(d_p(j,j')\le2L\). Then \(j\in E_e\) or \(j'\in E_{\bar e}\).

**Proof.** If \(x\) is bad, then \(j\in E_e\); if \(y\) is bad, then \(j'\in E_{\bar e}\). Let both be good, and put
\[
\begin{aligned}
\alpha_x&=\max_{e'\in\mathcal D(x),\ e'\ne e}r_x(e',j),\\
\alpha_y&=\max_{f\in\mathcal D(y),\ f\ne\bar e}r_y(f,j') .
\end{aligned}
\]
The maxima are over \(\Delta-1\ge3\) incidences.

We claim that \(r_x(e,j)\ge1+\alpha_y\). If \(\alpha_y>0\), there is a matched walk of length \(\alpha_y\) that starts at \(y\) through an incidence \(f\ne\bar e\) with the initial state \(j'\). Put the step \(e\) in front of it, with the state \(j\) in front of its states. The result is a walk from \(x\); it is nonbacktracking because \(f\ne\bar e\); and it is matched because \(x\) and \(j\) are compatible and \(d_p(j,j')\le2L\). It starts through \(e\) with the initial state \(j\) and has the length \(1+\alpha_y\). If \(\alpha_y=0\), the walk \(x,e,y\) with the states \(j,j'\) is matched and has the length \(1\).

The same argument with the roles of \(x\) and \(y\) exchanged, for the incidence \(\bar e\colon y\to x\), gives \(r_y(\bar e,j')\ge1+\alpha_x\).

Suppose \(e\) is not exceptional at \((x,j)\) and \(\bar e\) is not exceptional at \((y,j')\). Then \(r_x(e,j)\le\alpha_x\) and \(r_y(\bar e,j')\le\alpha_y\). Together with the two inequalities,
\[
\begin{aligned}
\alpha_x\ge r_x(e,j)&\ge1+\alpha_y\\
&\ge1+r_y(\bar e,j')\ge2+\alpha_x ,
\end{aligned}
\]
which is impossible. \(\blacksquare\)

The proof speaks about incidences only, so it covers loops and parallel edges; for a loop, \(x=y\) and \(\bar e\) is the other incidence of the loop. In words: if two neighbouring good vertices have compatible states that are close to each other, then for at least one of the two the direction to the other vertex is the direction in which its state can be followed strictly longest. Each state has at most one such direction at each good vertex. The next lesson gives up, for the incidence \(e\colon x\to y\), the states in \(E_e\) for the measure \(\mu_x\) and the states in \(E_{\bar e}\) for the measure \(\mu_y\). Averaged over the \(\Delta\) directions this costs a fraction \(1/\Delta\) of the total variation of the measures.

## 7. Exercises

**7.1.** Let \(T\) be as in Lemma 3.2 and let \(x\in S\) with \(T\delta_x=\delta_x\). Show that one can take for \(\mu_x\) the measure with \(\mu_x(\{x\})=1\) and \(\mu_x(\{j\})=0\) for \(j\ne x\).

**7.2.** Show that the numbers \(c_x(j)\) in the proof of Lemma 3.2 are determined by \(T\delta_x\).

**7.3.** How many nonbacktracking walks of length \(n\ge1\) start at the root of the \(\Delta\)-regular tree?

**7.4.** Let \(x\) be a good vertex and \(j\) a state such that no matched walk of positive length starts at \(x\) with the initial state \(j\). Show that no incidence is exceptional at \((x,j)\).

**7.5.** Let \(x\) be a source vertex and \(j\) a state with \(b_x(j)>0\). Show that \(x\) and \(j\) are compatible, and that every source vertex \(y\) joined to \(x\) by a source edge is compatible with every state \(j'\) with \(d_p(j,j')\le2L\).

## 8. Solutions

**7.1.** If \(x\ne o\), then \(c_x(x)=1\) and \(c_x(j)=0\) otherwise is a representation of \(T\delta_x\), and \(\mu_x(\{o\})=1-1=0\). If \(x=o\), then \(T\delta_o=0\), all \(c_o(j)\) can be taken as \(0\), and \(\mu_o(\{o\})=1\).

**7.2.** The evaluations \(\delta_j\), \(j\in S\setminus\{o\}\), are linearly independent: the function that is \(1\) at \(j\) and \(0\) at all other points of \(M_p\) vanishes at \(o\) and has a Lipschitz constant of at most \(1\), because different points have distances at least \(1\); a vanishing combination applied to it gives that the coefficient of \(\delta_j\) is \(0\).

**7.3.** \(\Delta\) choices for the first step and \(\Delta-1\) for each further step: \(\Delta(\Delta-1)^{n-1}\).

**7.4.** All records \(r_x(e,j)\), \(e\in\mathcal D(x)\), are \(0\). No record is strictly larger than the others, since there are \(\Delta\ge4\) incidences.

**7.5.** By Lemma 3.1, \(\|h(x)-h(j)\|_\infty<K\le K+2L+1\). By (G1) and (G2), \(\|h(y)-h(x)\|_\infty\le1\) and \(\|h(j)-h(j')\|_\infty\le2L\). So \(\|h(y)-h(j')\|_\infty<1+K+2L\).

## References

- [OpenAI-LF] OpenAI, *A uniformly discrete counterexample to bounded approximation in Lipschitz-free spaces*, OpenAI Math Release preprint, 26 September 2026, Sections 4 and 5. https://github.com/openai/math/tree/main/preprints/Failure-of-Bounded-Approximation-in-a-Lipschitz-Free-Space-over-a-Uniformly-Discrete-Metric-Space-September-26-2026
