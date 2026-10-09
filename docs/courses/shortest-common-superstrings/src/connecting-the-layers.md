# Connecting the layers

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[Periodic layers](periodic-layers.md) rewrote the base graph as layers: closed walks, each running once along a periodic text of least period \(p\), with cost \(p\) and a budget \(p\); the budgets add up to \(W\). This lesson adds closed walks of total cost at most \(W\) that connect every layer to the empty word \(\varepsilon\) (Theorem 4.3), and with it proves the factor-\(2\) theorem (Section 5), following OpenAI [OpenAI-SCS]. The construction processes the layers group by group in increasing order of period. Layers of one text that are close together are joined cheaply among themselves. When they are not, the periodic count rule of [Forced occurrence counts](forced-occurrence-counts.md) forces a shorter word to occur on a layer with a different text, which provides a place to attach a connection (Section 3). Some connections may form directed cycles; opening each cycle at a lexicographically extremal place frees exactly the budget needed (Section 4).

We use the windows, layers, first and last ends \(f_i,l_i\), budgets, Lemmas 4.1, 5.1 and 5.2 of [Periodic layers](periodic-layers.md), the counts \(m\), the functionals \(B_A\) and Definition 2.1 of [Forced occurrence counts](forced-occurrence-counts.md), and Corollary 3.2 of [Superstrings and the hierarchical graph](superstrings-and-the-hierarchical-graph.md). A collection of layers and added walks is *rooted* if its support is connected to \(\varepsilon\), directions ignored. To *touch* a layer means to share one of its vertices; since all base edges stay, touching a layer connects to all of it.

## 1. Following ordered windows

**Lemma 1.1** (ordered windows). Let \([a,b)\) and \([c,d)\) be windows in a common text, each spelling a word in \(V\), with \(a\le c\) and \(b\le d\). There is a walk in the hierarchical graph from the first word to the second of cost \(d-b\), which visits a word of length at most \(\max(0,b-c)\). Consequently a list of windows whose starts and ends are both nondecreasing can be followed at a cost equal to the total increase of the ends; if the last window is the first one translated by \(h\), in a text with a period dividing \(h\), this gives a closed walk of cost \(h\).

**Proof.** If \(c\le b\), delete the first \(c-a\) letters to reach \([c,b)\), of length \(b-c\), and append letters up to \(d\). The words on the way are suffixes of the first word or prefixes of the second, so they lie in \(V\), and the cost is \(d-b\). If \(c>b\), delete down to \(\varepsilon\); for each letter of the gap \([b,c)\) take an up step to that one-letter word and a down step back; then append the letters of \([c,d)\). One-letter words lie in \(V\), and the cost is \((c-b)+(d-c)=d-b\). \(\square\)

In particular, a *round trip* from a word \(s\) to \(\varepsilon\) and back costs \(|s|\).

## 2. Three joining operations

**Lemma 2.1** (joining an ordered band). Let \(k\) layers of one group, of period \(p\), be given, and let \(t\) be a start. Let \(H\) be the first end of the highest of them and \(E\) the last end of the lowest at \(t\). If \(h\) is a nonnegative multiple of \(p\) with \(H-E\le h\), the \(k\) layers can be joined by a closed walk of cost at most \(h\).

**Proof.** If \(E\ge H\), every layer \(i\) has \(f_i(t)\le H\le E\le l_i(t)\), so all contain the window \([t,E)\) and are already joined. Otherwise go up at start \(t\) from \([t,E)\) to \([t,H)\): every layer has a window at start \(t\) with end in \([E,H]\), so this path touches all of them, and its words are prefixes of the vertex \([t,H)\). Then follow to \([t+h,E+h)\), a translate of \([t,E)\); since \(E+h\ge H\), Lemma 1.1 gives a closed walk of cost \(h\). \(\square\)

A *record* is a window of a layer together with a periodic text, its *alignment*, that agrees with the layer's text throughout the window. A record on a layer provides a vertex at which layers following the other text can be attached.

**Lemma 2.2** (collective link). Let \(k\) layers of one group have the common text \(A\) of period \(p\), and let \(K=kp\). Let \(R=[a,b)\) be a window spelling a word of \(V\) that agrees with \(A\). Let \(r_H=f_H(a)\) be the first end of the highest and \(r_L=l_L(a)\) the last end of the lowest of these layers. If
\[
r_H\le b+K,\qquad r_H-r_L\le K,\qquad r_L+K\ge b,\tag{2.1}
\]
there is a closed walk of cost \(K\), through the word of \(R\), that touches all \(k\) layers.

**Proof.** Let \(Y=\max(b,r_H)\), so \(b\le Y\le b+K\). For each layer \(i\), \(f_i(a)\le r_H\le Y\) and \(Y\le r_L+K\le l_i(a)+K=l_i(a+K)\). Let \(x_i\) be the least start \(x\ge a\) with \(z_i(x)\ge Y\); then \(x_i\le a+K\), and \(z_i(x_i-1)\le Y\) (for \(x_i=a\) because \(z_i(a-1)=f_i(a)\), otherwise by minimality). So \([x_i,Y)\) is a window of layer \(i\). Higher layers have larger \(z\), hence smaller \(x_i\). The list \(R\), the windows \([x_i,Y)\) from the highest layer to the lowest, and \(R+K=[a+K,b+K)\), has nondecreasing starts and ends, and \(R+K\) spells the word of \(R\) since \(K\) is a multiple of \(p\). Lemma 1.1 gives the walk. \(\square\)

A *request* reserves the budget of a layer for an operation at another layer, its *host*, which may also spend the host's budget.

**Lemma 2.3** (host requests). Let a host layer have period \(q\). On it choose windows \(R_i=[a_i,b_i)\), indexed by finitely many groups \(i\), the *child groups*. The text of child group \(i\) has period \(p_i\), differs up to translation from the host's text and from the texts of the other child groups, and, in a chosen alignment, agrees with the host's text throughout \(R_i\). For each \(i\), one or more layers of child group \(i\) request a connection at \(R_i\), each with a window \([a_i,e)\) satisfying
\[
a_i+p_i<e\le b_i-p_i.\tag{2.2}
\]
Then the host and all requesting layers can be rooted with closed walks costing at most the host's budget \(q\) plus the budgets of the requesting layers.

**Proof.** By Lemma 5.1 of [Periodic layers](periodic-layers.md),
\[
b_i-a_i<p_i+q.\tag{2.3}
\]
Take the windows \(R_i\) on one lift of the host. If \(R_i\) comes before \(R_l\), their starts and ends are ordered, and where they overlap the two different child texts agree, so
\[
b_i-a_l<p_i+p_l,\tag{2.4}
\]
which is trivial without overlap. Choose \(j\) with \(p_j\) minimal. Translating the windows \(R_i\) by multiples of \(q\), together with the coordinates of their child groups (which changes no word, period or budget), we may assume \(a_j\le a_i\le T:=a_j+q\) and \(b_j\le b_i\le b_j+q\) for all \(i\). The next copy of \(R_j\) is \(R_j+q=[T,b_j+q)\), a window of the same host, and (2.4) applies to it as well.

*The host excursion.* At start \(a_j\), visit the windows \([a_j,e)\) of the requesters of group \(j\) in increasing order of \(e\), then \(R_j\). Then, for each other \(i\) in the order of the \(R_i\), and within \(i\) in increasing order of \(e\), visit
\[
Q_{i,e}=[s_i,h_{i,e})=\bigl[\min(a_i+p_i,T),\ \max(e,b_j)\bigr).\tag{2.5}
\]
Finally visit \([T,e_0+q)\), where \(e_0\) is the first requester end at \(j\). For \(R_i\) before \(R_l\), (2.2) and (2.4) give \(a_i+p_i<e_i\le b_i-p_i<a_l+p_l<e_l\), so the raw windows \([a_i+p_i,e)\) have increasing starts and ends, and so do the \(Q_{i,e}\). Each \(Q_{i,e}\) lies in \(R_i\) (as \(a_i\le T\) and \(b_j\le b_i\)) and is nonempty, so it spells a word of \(V\) that also agrees with child text \(i\). Applying (2.4) to \(R_i\) and \(R_j+q\) gives \(b_i-T<p_i+p_j\), and with (2.3) for \(j\),
\[
e\le b_i-p_i<T+p_j,\qquad b_j<T+p_j,\qquad h_{i,e}<T+p_j.\tag{2.6}
\]
Since \(e_0>a_j+p_j\), the last window ends after \(T+p_j\); so the whole list is ordered. The last window is \([a_j,e_0)\) translated by \(q\), so Lemma 1.1 gives a closed walk of cost \(q\), the host's budget. Its last transition starts at a window ending before \(T+p_j\) and reaches start \(T\), so it visits a word of length less than \(p_j\).

*Attaching the other requesters.* For a requester of group \(i\neq j\) with window \([a_i,e)\),
\[
a_i\le s_i\le a_i+p_i,\qquad e\le h_{i,e}\le e+p_i.\tag{2.7}
\]
Only the last inequality needs comment: if \(h_{i,e}=b_j\), then (2.4) for \(R_j\) before \(R_i\) and the minimality of \(p_j\) give \(b_j<a_i+p_j+p_i\le a_i+2p_i<e+p_i\). In child text \(i\), the list \(Q_{i,e}\), \([a_i+p_i,e+p_i)\), \(Q_{i,e}+p_i\) is ordered by (2.7); its middle window is a translate of the requester's window, hence the same vertex, and its last window spells the same word as the first. Lemma 1.1 gives a closed walk of cost \(p_i\), the requester's budget, through the requester and the host excursion.

*The requesters of group \(j\)* were visited by the host excursion. The budget \(p_j\) of one of them pays for a round trip from the word of length less than \(p_j\) found above to \(\varepsilon\). Then the host and all requesting layers are rooted. \(\square\)

## 3. Processing the period groups

Process the groups in increasing order of their least period, breaking ties by a fixed order (for instance by the least rotation of the text). Requests are sent to layers of groups processed later and fulfilled when that group is processed; *links* are only planned here and carried out in Section 4. A layer is *marked rooted* when an operation below roots it.

### 3.1 Incoming requests and a baseline

At the start of the processing of a group of period \(p\), every layer of the group that has received requests is a host: apply Lemma 2.3 to it and all its requesters. We show below (in Section 3.4) that every requester has a smaller period, so its group was processed earlier, and that each child group sends its requests to one window of one host; these are the hypotheses of Lemma 2.3, and the host's budget is still unused.

A host has a window of length less than \(2p\): its window \(R_i\) for a child of period \(p_i<p\) has length less than \(p+p_i\) by (2.3). If there are hosts, call the highest one the *baseline*; the hosts are rooted by Lemma 2.3. Each layer below the baseline is rooted with its own budget \(p\). If it has a window of length at most \(p\), use a round trip through \(\varepsilon\). Otherwise let \(S=[a,h)\) be a window of the baseline of length less than \(2p\). The lower layer has \(f_i(a)\le h\), so it has the window \([a,e)\) with \(e=\min(l_i(a),h)\), and \(p<e-a\le h-a<2p\). The list \([a,h)\), \([a+p,e+p)\), \([a+p,h+p)\) is ordered, since \(h<a+2p<e+p\), so Lemma 1.1 gives a closed walk of cost \(p\) through the baseline and the lower layer.

Let \(n\) be the number of layers above the baseline, or of all layers of the group if there are no hosts. Their budgets are unused. If \(n=0\), go to the next group.

### 3.2 Easy connections

Let \(A\) be the text of the group and \(t\) a distinguished position of \(A\) (Section 5 of [Periodic layers](periodic-layers.md)). Let \(H=f_H(t)\) be the first end at \(t\) of the highest layer. If \(H-t\le np\), a round trip from \(\varepsilon\) through \([t,H)\) costs at most \(np\); its up path passes all windows \([t,e)\), \(t\le e\le H\), and so touches every upper layer. If a baseline exists and its last end at \(t\) is at least \(H-np\), Lemma 2.1, with the baseline as lowest layer and \(h=np\), joins the baseline and the upper layers. In both cases the upper layers are rooted within their budgets. It remains to treat the case
\[
H>t+np,\qquad\text{and }l_{\mathrm{base}}(t)<H-np\text{ if a baseline exists}.\tag{3.1}
\]

### 3.3 Forcing a record on another text

Starting with \(k=1\), increase \(k\) as long as more than \(k\) layers \(i\) of the group satisfy \(l_i(t)\ge H-kp\); stop at the first \(k\) for which this fails, and put \(K=kp\).

**Lemma 3.1.** The search stops with \(1\le k\le n\). Let \(L_*\) be the lowest of the \(k\) highest layers. Then
\[
l_{L_*}(t)\ge H-(k-1)p,\tag{3.2}
\]
\[
f_H(x)-l_{L_*}(x)\le K\qquad\text{for all }x.\tag{3.3}
\]
At most \(k\) recorded occurrences of \(w=A[t:H-K)\) on layers have, as their whole text, the text \(A\) aligned at the occurrence.

**Proof.** For \(k\le n\), by (3.1), the baseline and the layers below it do not satisfy \(l_i(t)\ge H-kp\), so at most \(n\) layers do and the search stops by \(k=n\). If \(k=1\), the highest layer has \(l_H(t)\ge f_H(t)=H\). If \(k>1\), the test passed at \(k-1\), so at least \(k\) layers satisfy \(l_i(t)\ge H-(k-1)p\); by the order of the layers these include the \(k\) highest, which gives (3.2). For any \(x\), take \(x'\equiv x\pmod p\) with \(t-p<x'\le t\); then \(f_H(x')\le H\) and \(l_{L_*}(x')\ge l_{L_*}(t-p)=l_{L_*}(t)-p\), so (3.2) gives (3.3) at \(x'\), and the difference is invariant under translation by \(p\).

By (3.1), \(H-K>t\), so \(w\) is nonempty. Another group has no text equal to a translate of \(A\). A layer of this group has text \(A\), and the translates of \(A\) equal to \(A\) are those by multiples of \(p\); so among its recorded occurrences of \(w\), modulo its turn, only the one at position \(t\) has \(A\) as its aligned text, and it is recorded exactly when \(l_i(t)\ge H-K\). When the search stops, at most \(k\) layers satisfy this. \(\square\)

Apply the periodic rule of Definition 2.1 of [Forced occurrence counts](forced-occurrence-counts.md), with the origin moved to \(t\), to
\[
v=A[t:H),\qquad w=A[t:H-K),\qquad|v|=|w|+kp.
\]
The window \([t,H)\) of the highest layer is a recorded occurrence of \(v\) on a layer whose whole text is the template, so it is unblocked, and Lemma 4.1 of [Periodic layers](periodic-layers.md) gives \(m(v)>B_A(v;m)\). The rule gives \(m(w)\ge B_A(w;m)+k+1\), so \(w\) has at least \(k+1\) unblocked recorded occurrences. By Lemma 3.1 one of them lies on a layer \(D\) whose aligned text differs from \(A\); \(D\) may belong to this group with a different phase. By Lemma 4.1 of [Periodic layers](periodic-layers.md), \(D\) has a window \(R=[a,b)\) that agrees with \(A\) throughout and contains \([t,H-K)\). Let \(q\) be the period of \(D\). By Lemma 5.1 there,
\[
a\le t,\qquad b\ge H-K,\qquad b-a<p+q,\qquad\text{and }b-a<p\text{ if }D\text{ is in this group}.\tag{3.4}
\]
This one record is used for all connections from this group.

### 3.4 Distributing the remaining budgets

At start \(a\) put \(r_H=f_H(a)\) and \(r_L=l_{L_*}(a)\). By monotonicity, (3.3) and (3.4),
\[
r_H-r_L\le K,\qquad r_H\le H\le b+K.\tag{3.5}
\]

*The collective case.* If \(r_L+K\ge b\), the conditions (2.1) hold for the \(k\) highest layers and \(R\). They form a *collective block*, with a planned link to \(D\) at \(R\) as in Lemma 2.2, which reserves their combined budget \(K\). Otherwise \(r_H\le r_L+K<b\).

*The individual cases.* Every upper layer \(i\) not in the collective block has \(f_i(a)\le b\): if the collective test failed, \(f_i(a)\le r_H<b\); and a layer below the \(k\) highest has \(f_i(a)\le l_i(t)<H-K\le b\), by the stopping rule and \(a\le t\). For such a layer, do exactly one of the following.

1. If it has a window of length at most \(p\), root it by a round trip through \(\varepsilon\).
2. If all its windows are longer than \(p\) and \(l_i(a)+p\ge b\), it forms an *individual block* with a planned link to \(D\) at \(R\): at start \(a+p\) its ends range over \([f_i(a)+p,l_i(a)+p]\), which meets \([b,b+p]\), so it has a window \([a+p,e')\) with \(b\le e'\le b+p\). The list
\[
[a,b),\qquad[a+p,e'),\qquad[a+p,b+p)
\]
is ordered and gives a closed walk of cost \(p\) in \(A\) through \(R\) and the layer. Its transition into start \(a+p\) visits a word of length at most \(\max(0,b-a-p)<q\), by Lemma 1.1 and (3.4). The layer's budget is reserved for this link.
3. Otherwise its first end \(e=f_i(a)\) satisfies
\[
a+p<e\le l_i(a)<b-p,\tag{3.6}
\]
since its windows are longer than \(p\). Reserve its budget and send a request to \(D\) at \(R\). Then \(b-a>2p\), and with \(b-a<p+q\) this gives \(q>p\).

This proves the promised facts about requests: they go to layers of larger period, whose groups are processed later, and all requests from one group go to the single record \(R\) on the single layer \(D\), with windows satisfying (2.2). Planned links spend no budget of their target.

**Proposition 3.2** (OpenAI). After all groups are processed, every layer is either marked rooted or belongs to exactly one *block*, and not both. A block consists of layers of one group, has one target layer, and keeps its whole budget reserved for its planned link; a collective block of \(k\) layers satisfies (3.2) at its distinguished position, and an individual block consists of one layer.

**Proof.** Requests use disjoint budgets of the requesters, and a host's budget is spent only when its group is processed, which happens after all its requesters. The baseline step uses budgets of the layers below the baseline, and the easy branches use the budgets of the upper layers and root them. In the remaining branch, the collective case and the individual cases split the upper layers. Every request is fulfilled. The layers not rooted by these operations are exactly those in blocks, whose links are only planned. \(\square\)

## 4. Opening cycles

Regard each block as a node, with an arrow to the block containing its target layer, or to a *rooted sink* if the target layer is marked rooted. Every block has exactly one outgoing arrow, so following arrows from any block leads either to a sink or into a directed cycle.

**Lemma 4.1** (one free period). A block of \(k\) layers of period \(p\) can be joined internally for cost at most \((k-1)p\), leaving \(p\) of its budget free.

**Proof.** For an individual block nothing is needed. For a collective block, (3.2) gives \(f_H(t)-l_{L_*}(t)\le(k-1)p\), and Lemma 2.1 with \(h=(k-1)p\) joins it. \(\square\)

**Lemma 4.2** (a short contact on a maximal link; OpenAI). On a directed cycle of blocks, choose a block whose group has the lexicographically largest forward word at its distinguished position, and let \(q\) be the period of its target layer. Its planned link can be carried out within its reserved budget so that the resulting connected piece contains a word of length at most \(q\).

**Proof.** For an individual block, item 2 of Section 3.4 already gives such a word. Let the block be collective, with \(k\) layers of period \(p\), \(K=kp\), distinguished position \(t\), \(H=f_H(t)\) and record \(R=[a,b)\) on the target, so that \(a\le t<H-K\le b\) and \(b-a<p+q\). If some layer of the block has a window of length at most \(q\), the collective link of Lemma 2.2 suffices. Otherwise every window of every layer of the block is longer than \(q\).

The target layer belongs to a block of the cycle, so every forward word of its text is at most the forward word of its own group at its distinguished position, and hence at most that of \(A\) at \(t\). Its aligned text differs from \(A\). By Lemma 5.2 of [Periodic layers](periodic-layers.md), it does not agree with \(A\) on all of \([t,t+q)\); since it agrees with \(A\) on \(R\supseteq[t,\min(b,t+q))\), we get \(b-t<q\). Let \(x=\min(t,a+K)\). Then \(a\le x\le a+K\) and \(x\le t<b\); if \(x=t\), then \(b-x<q\), and if \(x=a+K<t\), then \(b-x=b-a-K<p+q-K\le q\). So \([x,b)\) is a suffix of \(R\) of length less than \(q\).

At start \(x\), each layer of the block has its first window \([x,f_i(x))\) longer than \(q>b-x\), so \(f_i(x)>b\); and \(f_i(x)\le f_H(x)\le f_H(t)=H\). Let \(F=f_H(x)\), so \(b<F\le H\le b+K\). Follow the list
\[
[a,b),\qquad[x,b),\qquad[x,F),\qquad[a+K,b+K).\tag{4.1}
\]
Its starts and ends are nondecreasing, its words lie in \(V\) (a suffix of \(R\), a window of the highest layer, and a translate of \(R\)), and the last spells the word of \(R\) in the text \(A\) of period \(p\mid K\). By Lemma 1.1 it is a closed walk of cost \(K\). The vertical part at start \(x\) passes every first end \(f_i(x)\in(b,F]\), so it touches every layer of the block, and \([x,b)\) is the short word. \(\square\)

**Theorem 4.3** (connecting the base graph; OpenAI). Closed walks of total cost at most \(W\) can be added to the base graph so that every layer is rooted.

**Proof.** After the processing of Section 3, the layers outside blocks are rooted within their budgets. Consider a directed cycle of blocks.

If the cycle consists of one block, its target layer belongs to the block, hence to its group, and the record has a different phase, so \(|R|<p\) by (3.4). Join the block internally (Lemma 4.1) instead of carrying out its link; \(R\) is a window of one of its layers, and the free budget \(p\) pays for a round trip from \(R\) to \(\varepsilon\).

If the cycle has at least two blocks, choose the block of Lemma 4.2 and carry out its link with a short word of length at most \(q\), where \(q\) is the period of its target block. Do not carry out the link of that target block; join the target block internally instead (Lemma 4.1), which frees \(q\), and spend it on a round trip from the short word to \(\varepsilon\). Carry out all other links of the cycle. The two special links are different because the cycle has at least two blocks, and the cycle becomes one rooted piece.

Different cycles have disjoint blocks, so these choices do not compete for budgets. Finally carry out the remaining links in order of increasing distance from a rooted sink or an opened cycle; each attaches its block to a rooted piece using its own reserved budget. Every budget is used at most once, so the added cost is at most the sum of the budgets, \(W\). \(\square\)

## 5. The algorithm

**Proof of Theorem 4.1 of [Superstrings and the hierarchical graph](superstrings-and-the-hierarchical-graph.md).** Preprocess the input (Lemma 1.1 there); if no string remains, output \(\varepsilon\). Otherwise compute the counts \(m\) and the base graph; by Lemma 2.2 and Lemma 3.1 of [Forced occurrence counts](forced-occurrence-counts.md), it is balanced, contains every required string and costs \(W\le\mathrm{OPT}(\mathcal S)\). Add the closed walks of Theorem 4.3. The resulting multiset is balanced, its support is connected and contains \(\varepsilon\), and its cost is at most \(2W\). By Corollary 3.2 of [Superstrings and the hierarchical graph](superstrings-and-the-hierarchical-graph.md), an Euler tour from \(\varepsilon\) spells a common superstring of length at most \(2W\le2\,\mathrm{OPT}(\mathcal S)\).

*Running time.* Let \(N\) be the encoded length of the input; then \(L\le N\) and \(|V|=O(L^2)\). Every choice above is made by taking the first admissible item in a fixed order of the explicit data, so the algorithm is deterministic. The periodic rules are the triples \((v,p,k)\) with \(kp<|v|\) and \(v\) of period \(p\), polynomially many; each \(b_{A,s}(r)\) is computed by checking the at most \(|r|\) offsets, and the counts are at most \(L\) (Lemma 2.2 there), so they have polynomially many bits. The base graph has \(2W\le2L\) edges with multiplicity. The decomposition into closed walks, the texts, their least periods and alignments, and the sorted layers of Lemma 3.1 of [Periodic layers](periodic-layers.md) are found by finite traversals, string comparisons and sorting; a layer is stored by one period of its text and one period of its function \(z\). Two periodic texts of periods \(p\) and \(q\) are compared on \(p+q\) positions (Lemma 5.1 there). The search for the record in Section 3.3 scans the at most \(2W\) windows of one turn of all layers and the placements of \(w\) in them, keeping one whose whole window agrees with \(A\) and whose aligned text differs from \(A\); the argument after Lemma 3.1 shows that it succeeds. The operations of Sections 2 to 4 are lists of windows of polynomial length, turned into walks by Lemma 1.1, and the cycles of the block graph are found by following arrows. The final multiset has at most \(4W\le4L\) edges, and its Euler tour (Lemma 3.1 of [Superstrings and the hierarchical graph](superstrings-and-the-hierarchical-graph.md)) is found in polynomial time. \(\square\)

## 6. Exercises

**Exercise 6.1** (easy). For \(\mathcal S=\{ab,ba\}\), the base graph is one layer of period \(2\) with text \(\dots abab\dots\) (Exercise 6.1 of [Periodic layers](periodic-layers.md)). Carry out the processing of Section 3 and find the walk that connects it to \(\varepsilon\). What is the total cost?

**Exercise 6.2** (easy). Show that in Lemma 2.1 the walk can be chosen with cost exactly \(h\) when \(E<H\), and with no added walk when \(E\ge H\).

**Exercise 6.3** (medium). In Lemma 2.3, show that the requesters of group \(j\) need no budget of their own, except one, and explain why \(j\) is chosen with the smallest period.

**Exercise 6.4** (medium). Explain why opening a cycle of at least two blocks frees the period \(q\) of the target of the chosen block, and why the chosen link needs a contact of length at most \(q\) rather than at most the period \(p\) of its own block.

## 7. Solutions

**6.1.** There are no hosts and no baseline, \(n=1\), \(p=2\). With \(a<b\), the forward words of \(A=\dots abab\dots\) start with \(ab\) or \(ba\), so \(t\) is a position of \(b\), say \(A(0)=b\), \(t=0\). The windows of the layer at start \(0\) are \([0,1)=b\) and \([0,2)=ba\), so \(H=f_H(0)=1\) and \(H-t=1\le np=2\): the easy case applies. The round trip \(\varepsilon\to b\to\varepsilon\) costs \(1\) and touches the layer. The total cost is \(2+1=3=\mathrm{OPT}\), and an Euler tour from \(\varepsilon\) spells, for instance, \(bab\).

**6.2.** If \(E<H\), the walk built in the proof goes up from \(E\) to \(H\) and then to \(E+h\), so its cost is exactly \((H-E)+(E+h-H)=h\). If \(E\ge H\), the layers share the window \([t,E)\).

**6.3.** The host excursion visits their windows at start \(a_j\), so they are attached; the budget \(p_j\) of one of them pays for the round trip from the short word, of length less than \(p_j\), to \(\varepsilon\). The minimality of \(p_j\) is used to show \(h_{i,e}\le e+p_i\) when \(h_{i,e}=b_j\), so that every other requester can attach at cost exactly its own budget.

**6.4.** The target block's link is replaced by its internal joining, which by Lemma 4.1 costs one period of that block less than its budget; this frees \(q\). The round trip from the contact to \(\varepsilon\) must be paid from the freed amount, so the contact must have length at most \(q\). Lemma 4.2 obtains such a contact from the maximality of the chosen block's forward word, through Lemma 5.2 of [Periodic layers](periodic-layers.md).

## References

- [OpenAI-SCS] OpenAI, *A polynomial-time 2-approximation for shortest common superstring*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026
