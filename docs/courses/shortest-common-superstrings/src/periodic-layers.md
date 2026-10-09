# Periodic layers

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The base graph of [Forced occurrence counts](forced-occurrence-counts.md) is a balanced multiset of edges of cost \(W\), possibly disconnected. This lesson rewrites it, without changing a single edge, as a union of *layers*: closed walks that run once along a periodic text of least period \(p\) and cost exactly \(p\) (Lemma 3.1). Each layer receives a *budget* equal to its period; the budgets add up to \(W\), and [Connecting the layers](connecting-the-layers.md) spends them to connect everything to the empty word. The lesson also shows how the counts \(m\) are visible on the layers (Lemmas 2.1 and 4.1) and proves two facts about periodic texts (Section 5). The construction follows OpenAI [OpenAI-SCS].

We use the hierarchical graph and Lemma 3.1 of [Superstrings and the hierarchical graph](superstrings-and-the-hierarchical-graph.md), and the periodic texts, the blocking functionals \(B_A\), the counts \(m\) and the base graph of [Forced occurrence counts](forced-occurrence-counts.md).

## 1. Closed walks and their texts

**Lemma 1.1.** The base graph is the union of the edge multisets of finitely many nonempty closed walks.

**Proof.** As in the proof of Lemma 3.1 of [Superstrings and the hierarchical graph](superstrings-and-the-hierarchical-graph.md), following unused edges from a vertex with an unused outgoing edge produces a closed walk, and the remaining edges are again balanced. Repeat until no edges remain. \(\square\)

Fix a nonempty closed walk \(\Gamma\) starting at a word \(w_0\). Each step changes the length of the current word by \(\pm1\) and the walk returns to its start, so it has as many up steps as down steps, say \(P\ge1\) of each; \(P\) is its *turn length*. Let \(c_1,\dots,c_P\) be the letters appended by its up steps in order, and define the periodic text
\[
A_\Gamma(i)=c_{(i\bmod P)+1}\qquad(i\in\mathbb Z).
\]
Run \(\Gamma\) repeatedly, forward and backward in time. Give the moment \(0\) the coordinates \(x=-|w_0|\), \(e=0\); let each up step increase \(e\) by \(1\) and each down step increase \(x\) by \(1\). The interval \([x,e)\) at a moment is the *window* of that moment.

**Lemma 1.2.** At every moment, the current word is \(A_\Gamma[x,e)\).

**Proof.** The current word behaves like a queue: an up step appends a letter at the back, a down step removes the letter at the front. Run \(M\) turns from moment \(0\), with \(MP\ge|w_0|\). The word returns to \(w_0\), and since at least \(|w_0|\) letters were removed from the front, none of the original letters remains: \(w_0\) consists of the last \(|w_0|\) appended letters, \(A_\Gamma[MP-|w_0|,MP)=A_\Gamma[-|w_0|,0)\). So the claim holds at moment \(0\). An up step at a window \([x,e)\) appends the letter of the \((e+1)\)-th up step counted from moment \(0\), which is \(A_\Gamma(e)\); a down step removes \(A_\Gamma(x)\). So the claim propagates forward, and by periodicity (one turn shifts both coordinates by \(P\)) it holds at every moment. \(\square\)

So the walk is a staircase in the plane of pairs (start, end): it moves up at fixed start and right at fixed end, and its windows spell words of \(V\).

## 2. Recorded occurrences

An *occurrence* of a nonempty word \(s\) in \(A_\Gamma\) is an interval \([u,u+|s|)\) with \(A_\Gamma[u,u+|s|)=s\). It is *recorded* on \(\Gamma\) if some window of \(\Gamma\) contains it. Translation by \(P\) maps windows to windows, and we count recorded occurrences modulo \(P\).

**Lemma 2.1** (recorded occurrences; OpenAI). For every decomposition of the base graph into closed walks and every nonempty \(s\in V\), the total number of recorded occurrences of \(s\), over all the walks, is \(m(s)\).

**Proof.** Fix a walk and an occurrence \([u,v)\), \(v=u+|s|\). Exactly one up step of the lift reaches the end \(v\); let \([x,v)\) be its window. A window containing \([u,v)\) has end at least \(v\), so it occurs at or after this step, and starts only increase; hence the occurrence is recorded exactly when \(x\le u\), that is, when the word \(A_\Gamma[x,v)\) created by this up step ends with \(s\). So the recorded occurrences of \(s\), modulo \(P\), correspond to the up steps of one turn whose target word ends with \(s\). Over all walks these are all up edges of the base graph with such targets, counted with multiplicity, and by (3.1) of [Forced occurrence counts](forced-occurrence-counts.md)
\[
\sum_{y:\,ys\in V}u(ys)=\sum_{y:\,ys\in V}\Bigl(m(ys)-\sum_cm(cys)\Bigr)=m(s),
\]
because the sum telescopes over the length of \(y\). \(\square\)

## 3. Ordered layers

Two closed walks belong to the same *group* if their texts are translates of each other. Within a group, fix one text \(A\) and translate the coordinates of every walk of the group so that its text is \(A\). Let \(p\) be the least period of \(A\). The shifts \(\delta\) with \(A(i+\delta)=A(i)\) for all \(i\) form the subgroup \(p\mathbb Z\), so every turn length in the group is a multiple of \(p\).

Since starts increase by one at each down step, the lift of a walk passes every start \(x\) once: it arrives at start \(x\) by a down step, takes up steps, and leaves by a down step at some end \(Z(x)\), the *exit end* at \(x\). Then the windows at start \(x\) are exactly \([x,e)\) with \(Z(x-1)\le e\le Z(x)\), and
\[
Z(x-1)\le Z(x),\qquad Z(x-1)\ge x,\qquad Z(x+P)=Z(x)+P.\tag{3.1}
\]
Conversely, a function \(Z\colon\mathbb Z\to\mathbb Z\) with (3.1) for some multiple \(P\) of \(p\) describes a staircase in the text \(A\) that returns to the same word after each turn; it is a closed walk of the hierarchical graph when the words \(A[x,e)\) of its windows lie in \(V\).

**Lemma 3.1** (ordered layers; OpenAI). The walks of a group can be replaced by closed walks with the same multiset of edges, called *layers*, each with turn length \(p\), such that their exit-end functions \(z_1\le z_2\le\dots\le z_h\) are pointwise ordered and satisfy (3.1) with \(P=p\). Each layer costs \(p\) per turn, and the layers of all groups together cost \(W\).

**Proof.** Let walk \(j\) of the group have turn length \(d_jp\) and exit ends \(Z_j\). For each start \(x\), let \(\mathcal E_x\) be the multiset of the numbers \(Z_j(x+rp)-rp\) for all \(j\) and \(0\le r<d_j\): the passages of the walks through the starts \(x+rp\), translated to start \(x\). Translation by multiples of \(p\) does not change words, because \(A\) has period \(p\). Let \(z_1(x)\le\dots\le z_h(x)\), \(h=\sum_jd_j\), be the elements of \(\mathcal E_x\) in increasing order.

The passage \((j,r)\) at start \(x\) enters at \(Z_j(x+rp-1)-rp\), an element of \(\mathcal E_{x-1}\), and exits at \(Z_j(x+rp)-rp\in\mathcal E_x\); this pairs \(\mathcal E_{x-1}\) with \(\mathcal E_x\) so that each entry is at most its exit and at least \(x\). If two multisets of equal size are paired so that each element of the first is at most its partner, then their \(i\)-th smallest elements satisfy the same inequality (Exercise 6.2). So \(z_i(x-1)\le z_i(x)\) and \(z_i(x-1)\ge x\). Replacing \(x\) by \(x+p\) permutes the passages of each walk and adds \(p\) to every value, so \(\mathcal E_{x+p}=\mathcal E_x+p\) and \(z_i(x+p)=z_i(x)+p\). Thus each \(z_i\) defines a staircase of turn length \(p\) in the text \(A\).

The edges are unchanged. At start \(x\), the down edges are those from the windows \([x,e)\), one for each \(e\in\mathcal E_x\), for the old walks and the new staircases alike. The up edge from \([x,e)\) to \([x,e+1)\) is used by as many passages as there are entries at most \(e\) minus exits at most \(e\), since each entry is at most its exit; this number depends only on \(\mathcal E_{x-1}\) and \(\mathcal E_x\). So the staircases use exactly the edges of the original walks; in particular their windows are vertices of the base graph, and they are closed walks of the hierarchical graph. Each layer has \(p\) up steps per turn and \(\sum_jd_jp\) is the total number of up steps of the group, so the layers of all groups cost \(W\). \(\square\)

We fix such layers for the rest of the course. A layer of period \(p\) receives the *budget* \(p\); the budgets add up to \(W\). For a layer \(i\) write
\[
f_i(x)=z_i(x-1),\qquad l_i(x)=z_i(x)
\]
for its *first* and *last end* at start \(x\): at start \(x\) its windows are \([x,e)\) with \(f_i(x)\le e\le l_i(x)\). Within a group, a higher layer has larger first and last ends. Every window of a layer is a vertex of the base graph, and two windows spelling the same word are the same vertex.

## 4. Unblocked occurrences on layers

Let \(s\) be nonempty and let \(A'\) be a periodic text with \(A'[0:|s|)=s\), the *template*. A recorded occurrence \([u,u+|s|)\) of \(s\) on a layer with text \(A\) is aligned with \(A'\) by comparing \(A(u+x)\) with \(A'(x)\). It is *blocked* if a nearest left mismatch \(x_L<0\) and a nearest right mismatch \(x_R\ge|s|\) both exist and the interval \([u+x_L,u+x_R+1)\) is recorded on the same layer; otherwise it is *unblocked*.

**Lemma 4.1** (matching window; OpenAI). Over all layers, the number of blocked recorded occurrences of \(s\) is \(B_{A'}(s;m)\), so \(m(s)-B_{A'}(s;m)\) recorded occurrences are unblocked. Every unblocked recorded occurrence lies in a window of its layer that agrees with the aligned template throughout.

**Proof.** A blocked occurrence determines the recorded occurrence of its bracketing word \(r\) and the offset of \(s\) in it, counted in \(b_{A',s}(r)\); conversely, such a pair gives a blocked occurrence, as in Lemma 1.1 of [Forced occurrence counts](forced-occurrence-counts.md). The correspondence commutes with translation by a turn, and Lemma 2.1 applied to the layers counts the recorded occurrences of each \(r\) as \(m(r)\). This gives \(B_{A'}(s;m)\).

Let \([u,v)\) be an unblocked recorded occurrence on a layer. The first window containing it is created by the up step reaching end \(v\); it contains no right mismatch. If it contains no left mismatch either, it agrees with the template throughout. Otherwise let \(\ell<u\) be the nearest left mismatch. Follow the layer until a down step removes \(\ell\); until then the starts stay at most \(\ell<u\), so the windows still contain \([u,v)\). No right mismatch enters a window before that step: a window containing \(\ell\) and the nearest right mismatch would record the bracketing interval, and the occurrence would be blocked. Immediately after the down step, the window starts at \(\ell+1\), contains \([u,v)\), and contains no mismatch. \(\square\)

In particular, if the text of a layer is the aligned template itself, none of its recorded occurrences is blocked.

## 5. Two facts about periodic texts

**Lemma 5.1** (agreement bounds). Two different periodic texts with periods \(p\) and \(q\) agree on fewer than \(p+q\) consecutive positions. If both have period \(p\), they agree on fewer than \(p\) consecutive positions.

**Proof.** Two texts of period \(p\) that agree on \(p\) consecutive positions agree everywhere. Suppose a text \(X\) of period \(p\) and a text \(Y\) of period \(q\) agree on an interval \(I\) of length \(p+q\). For the first \(q\) positions \(i\) of \(I\), both \(i\) and \(i+p\) lie in \(I\), so \(Y(i)=X(i)=X(i+p)=Y(i+p)\). These \(i\) represent all residues modulo \(q\), so \(Y(i)=Y(i+p)\) for all \(i\), by the period \(q\) of \(Y\). Then \(X\) and \(Y\) both have period \(p\) and agree on \(p\) consecutive positions, so \(X=Y\). \(\square\)

This is a weak form of the theorem of Fine and Wilf, which replaces \(p+q\) by \(p+q-\gcd(p,q)\). Order infinite *forward words* \(A(t)A(t+1)\cdots\) lexicographically, using the order of \(\Sigma\). A position \(t\) of a periodic text \(A\) is *distinguished* if its forward word is the largest among the forward words of \(A\); such positions exist, since a text of least period \(p\) has at most \(p\) different forward words.

**Lemma 5.2** (maximal rotation). Let \(A\) have least period \(p\) and a distinguished position \(t\). Let \(D\neq A\) be a periodic text of period \(q\) all of whose forward words are at most the forward word of \(A\) at \(t\). Then \(D\) and \(A\) do not agree on all \(q\) positions \(t,\dots,t+q-1\).

**Proof.** Translate so that \(t=0\), and let \(S\) be the forward word of \(A\) at \(0\). The forward word at \(q\), \(S'(i)=S(i+q)\), satisfies \(S'\le S\). If \(S'=S\), then \(A(i)=A(i+q)\) for all \(i\ge0\), hence for all \(i\) by periodicity; so \(A\) has period \(q\), and a text of period \(q\) agreeing with \(A\) on \(q\) consecutive positions equals \(A\). So \(D\) cannot agree there. Otherwise let \(j\) be the first index with \(S(j)\neq S(j+q)\); then \(S(j)>S(j+q)\). Let \(U\) be the word with period \(q\) whose first \(q\) letters are those of \(S\). By induction \(U(i)=S(i)\) for \(i<j+q\): for \(i<q\) by definition, and for \(q\le i<j+q\), \(U(i)=U(i-q)=S(i-q)=S(i)\) because \(i-q<j\). At \(i=j+q\), \(U(j+q)=U(j)=S(j)>S(j+q)\), so \(U>S\). If \(D\) agreed with \(A\) on \(0,\dots,q-1\), its forward word at \(0\) would be \(U\), larger than \(S\), contrary to the hypothesis. \(\square\)

## 6. Exercises

**Exercise 6.1** (easy). For the base graph of \(\{ab,ba\}\), the closed walk \(a\to ab\to b\to ba\to a\), started at \(a\) (Exercise 4.1 of [Forced occurrence counts](forced-occurrence-counts.md)), compute \(P\), the text \(A_\Gamma\), the windows of one turn and the exit ends \(Z(x)\).

**Exercise 6.2** (medium). Let \(a_1,\dots,a_h\) and \(b_1,\dots,b_h\) be real numbers with \(a_i\le b_i\) for all \(i\). Show that the \(k\)-th smallest of the \(a_i\) is at most the \(k\)-th smallest of the \(b_i\), for every \(k\).

**Exercise 6.3** (easy). Let \(X\) have period \(2\) with \(X(0)X(1)=ab\), and \(Y\) period \(3\) with \(Y(0)Y(1)Y(2)=aba\). Show that \(X\) and \(Y\) agree on positions \(0,1,2\) and differ at \(3\). Compare with Lemma 5.1.

**Exercise 6.4** (easy). Let \(a<b\) and let \(A\) have period \(3\) with \(A(0)A(1)A(2)=aab\). Find the distinguished positions of \(A\).

## 7. Solutions

**6.1.** \(P=2\), the up steps append \(c_1=b\) and \(c_2=a\), so \(A_\Gamma(i)=b\) for even \(i\) and \(a\) for odd \(i\). Starting from \([-1,0)=a\), the windows are \([-1,1)=ab\), \([0,1)=b\), \([0,2)=ba\), \([1,2)=a\). The exit ends are \(Z(-1)=1\) and \(Z(0)=2\), and \(Z(x+2)=Z(x)+2\).

**6.2.** Let \(a_{(k)}\) and \(b_{(k)}\) be the \(k\)-th smallest values. At least \(k\) of the \(b_i\) are at most \(b_{(k)}\), and their partners \(a_i\) are also at most \(b_{(k)}\). So at least \(k\) of the \(a_i\) are at most \(b_{(k)}\), which means \(a_{(k)}\le b_{(k)}\).

**6.3.** \(X=\dots ababab\dots\) and \(Y=\dots abaaba\dots\) from position \(0\): both start with \(aba\), and \(X(3)=b\neq a=Y(3)\). They agree on \(3<2+3\) consecutive positions, as Lemma 5.1 requires; the theorem of Fine and Wilf gives the sharp bound \(2+3-1=4\).

**6.4.** The forward words at positions \(0,1,2\) begin with \(aab\), \(aba\) and \(baa\). The largest is the one starting with \(b\), so the distinguished positions are those \(t\) with \(t\equiv2\pmod3\).

## References

- [OpenAI-SCS] OpenAI, *A polynomial-time 2-approximation for shortest common superstring*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026
