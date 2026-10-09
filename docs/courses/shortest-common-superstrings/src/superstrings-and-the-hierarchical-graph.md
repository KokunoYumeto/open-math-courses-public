# Superstrings and the hierarchical graph

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Given finitely many strings, a *common superstring* is a string that contains each of them as a contiguous substring. Finding a shortest one is NP-hard, and the question is how close a polynomial-time algorithm can come. Tarhio and Ukkonen conjectured in 1988 that the greedy algorithm, which repeatedly merges two strings of largest overlap, is always within a factor \(2\). Approximation algorithms with guarantees \(3\) (Blum, Jiang, Li, Tromp and Yannakakis, 1994), \(2\tfrac12\) (Sweedyk), \(2\tfrac{11}{23}\) (Mucha [Mu]), about \(2.466\) (Englert, Matsakis and Veselý [EMV]) and \(\tfrac73\) (Chukhin, Kulikov, Mihajlin and Smal [CKMS]) followed, and Shibata showed that the greedy algorithm itself can be worse than \(2\) [Sh]. This course presents OpenAI's algorithm with factor \(2\) [OpenAI-SCS]:

**Theorem 4.1** (OpenAI 2026). There is a deterministic algorithm, running in time polynomial in the total encoded length of the input, that outputs for every finite family \(\mathcal S\) of strings a common superstring \(T\) with \(|T|\le2\,\mathrm{OPT}(\mathcal S)\), where \(\mathrm{OPT}(\mathcal S)\) is the length of a shortest common superstring.

The proof works in the *hierarchical graph* of the input, introduced by Golovnev, Kulikov and Mihajlin [GKM] and developed in the collapsing-superstring framework [GKLMN]: its vertices are the substrings of the input strings, an edge either appends a letter at the end (cost \(1\)) or deletes the first letter (cost \(0\)), and closed walks through the empty word spell common superstrings. This lesson sets up the graph and proves that balanced edge multisets with connected support give superstrings (Corollary 3.2). The next lessons construct such a multiset of cost at most \(2\,\mathrm{OPT}\).

## 1. Strings and superstrings

An *alphabet* \(\Sigma\) is a finite set with a total order (in the algorithm, the order of the codes of the letters). A string \(s\) of length \(|s|\) is a sequence \(s(0)s(1)\cdots s(|s|-1)\) of letters; \(\varepsilon\) is the empty string. For \(0\le i\le j\le|s|\), \(s[i:j)\) is the substring \(s(i)\cdots s(j-1)\). A string \(s\) *occurs* in \(T\) at position \(i\) if \(T[i:i+|s|)=s\); a *common superstring* of a family \(\mathcal S\) is a string in which every member of \(\mathcal S\) occurs. For nonempty \(s\), \(\operatorname{pref}(s)\) deletes the last letter of \(s\) and \(\operatorname{suf}(s)\) deletes the first.

**Lemma 1.1** (preprocessing). Deleting from \(\mathcal S\) the empty string, repeated strings, and every string that occurs in another member of \(\mathcal S\) does not change the set of common superstrings. After this deletion, let \(V\) be the set of all substrings of members of \(\mathcal S\), including \(\varepsilon\). Then \(V\) is closed under taking substrings, \(|V|\le1+L(L+1)/2\) where \(L=\sum_{s\in\mathcal S}|s|\), and no element of \(V\) other than \(s\) itself contains a remaining member \(s\in\mathcal S\).

**Proof.** A string containing \(t\) contains every substring of \(t\); so a string containing all remaining members contains all deleted ones. A string \(s\) of length \(\ell\) has at most \(\ell(\ell+1)/2\) nonempty substrings, and \(\sum\ell(\ell+1)/2\le L(L+1)/2\). If \(r\in V\) contains a remaining member \(s\), then \(r\) is a substring of some remaining member \(t\), so \(s\) occurs in \(t\); after the deletion this forces \(t=s\), and then \(r=s\). \(\square\)

We call the remaining members of \(\mathcal S\) the *required* strings. If none remains, \(\varepsilon\) is a shortest common superstring. Otherwise all letters of the required strings form the alphabet \(\Sigma\), so every single letter belongs to \(V\).

## 2. The hierarchical graph

The *hierarchical graph* has vertex set \(V\) and, for every nonempty \(s\in V\), an *up edge* \(\operatorname{pref}(s)\to s\) of cost \(1\) and a *down edge* \(s\to\operatorname{suf}(s)\) of cost \(0\). Both endpoints lie in \(V\), because \(V\) is closed under substrings. An up step appends a letter at the end of the current word; a down step deletes its first letter. The *cost* of a walk is its number of up steps.

**Lemma 2.1** (reading a walk). Let a walk start at \(\varepsilon\), and let \(T\) be the string of letters appended at its up steps, in order. At every moment the current vertex word is a suffix of the letters written so far. Consequently, if the walk is closed and visits every required string, then \(T\) is a common superstring of length equal to the cost of the walk.

**Proof.** Initially both are empty. An up step \(\operatorname{pref}(s)\to s\) appends the last letter of \(s\) to both the written string and the vertex word, so a suffix stays a suffix. A down step shortens the vertex word at the front, and a suffix of a suffix is a suffix. When the walk visits a required string \(s\), it is a suffix of a prefix of \(T\), so it occurs in \(T\). \(\square\)

Conversely, every common superstring gives such a walk (Exercise 5.3), so \(\mathrm{OPT}(\mathcal S)\) is the least cost of a closed walk from \(\varepsilon\) visiting all required strings.

## 3. Balanced edge multisets

A finite multiset \(E\) of edges of the hierarchical graph is *balanced* if at every vertex the number of edges of \(E\) entering it equals the number leaving it, counted with multiplicity. Its *support* is the set of vertices incident to an edge of \(E\); it is *connected* if any two vertices of the support are joined by a path of edges of \(E\), directions ignored. The union (sum) of balanced multisets is balanced, and so is the edge multiset of any closed walk.

**Lemma 3.1** (Euler tours). Let \(E\) be a nonempty balanced finite multiset of directed edges, on any vertex set, with connected support, and let \(v\) be a vertex of the support. There is a closed walk from \(v\) that uses every edge of \(E\) exactly once.

**Proof.** Starting at a vertex \(u\), follow unused edges as long as possible. Whenever the walk enters a vertex \(w\neq u\), it has used one more edge into \(w\) than out of \(w\), so by balance an unused edge leaves \(w\); hence the walk can stop only at \(u\), and it produces a closed walk using each edge at most once. Start this way at \(v\). If some edges remain unused, then some vertex \(u\) of the closed walk so far has an unused incident edge: otherwise the vertices of the walk and those of the unused edges would be two nonempty sets of support vertices with no edge of \(E\) between them, against connectivity. The unused edges still form a balanced multiset, since a closed walk uses as many edges into each vertex as out of it. Run the procedure from \(u\) on the unused edges, and insert the resulting closed walk into the previous one at a visit of \(u\). Repeat until no edges remain. \(\square\)

**Corollary 3.2.** Let \(E\) be a balanced multiset of edges of the hierarchical graph whose support is connected and contains \(\varepsilon\) and every required string. Then the letters appended along an Euler tour of \(E\) from \(\varepsilon\) form a common superstring whose length is the number of up edges in \(E\).

**Proof.** An Euler tour uses every edge, so it visits every support vertex. Apply Lemma 2.1. \(\square\)

## 4. The plan

**Theorem 4.1** (OpenAI 2026). There is a deterministic algorithm, polynomial in the total encoded length of the input, that outputs for every finite family \(\mathcal S\) of strings a common superstring \(T\) with \(|T|\le2\,\mathrm{OPT}(\mathcal S)\).

The proof is completed in Section 5 of [Connecting the layers](connecting-the-layers.md). It builds the multiset of Corollary 3.2 in two halves.

1. [Forced occurrence counts](forced-occurrence-counts.md) assigns to every nonempty \(s\in V\) a number \(m(s)\) that is at most the number of occurrences of \(s\) in every common superstring. From these numbers it builds a balanced *base graph* that contains every required string, with \(W=\sum_{c\in\Sigma}m(c)\le\mathrm{OPT}(\mathcal S)\) up edges. The base graph need not be connected. Besides the obvious inequalities between the occurrence counts of a word and of its one-letter extensions, the counts satisfy a rule for periodic words, which records repetitions that the extension inequalities miss.
2. [Periodic layers](periodic-layers.md) rearranges the base graph into *layers*: closed walks along periodic texts, each of cost equal to the least period of its text. Each layer of period \(p\) receives a budget \(p\); the budgets add up to \(W\).
3. [Connecting the layers](connecting-the-layers.md) adds closed walks that connect every layer to \(\varepsilon\), spending each budget at most once, so the added cost is at most \(W\). The periodic count rule guarantees that whenever the layers of a text cannot be connected cheaply among themselves, a shorter word occurs on a layer with a different text, where a connection can be attached.

The total cost is at most \(2W\le2\,\mathrm{OPT}(\mathcal S)\).

## 5. Exercises

**Exercise 5.1** (easy). List \(V\) and draw the hierarchical graph for \(\mathcal S=\{ab,ba\}\). Find a closed walk from \(\varepsilon\) of cost \(3\) through both required strings, and read off the superstring.

**Exercise 5.2** (easy). Show that the walk \(\varepsilon\to a\to ab\to b\to ba\to a\to\varepsilon\) is closed, and compute its cost and the string it spells. Is its edge multiset balanced?

**Exercise 5.3** (medium). Let \(T\) be a common superstring. For \(0\le i\le|T|\), let \(u_i\) be the longest suffix of \(T[0:i)\) that belongs to \(V\). Show that \(u_{i+1}\) is obtained from \(u_i\) by down steps followed by one up step, that the resulting walk \(u_0\to\dots\to u_{|T|}\to\dots\to\varepsilon\) visits every required string, and that its cost is \(|T|\). Deduce that \(\mathrm{OPT}(\mathcal S)\) is the least cost of a closed walk from \(\varepsilon\) visiting all required strings.

**Exercise 5.4** (easy). Show that Lemma 3.1 fails without connectivity and without balance.

## 6. Solutions

**5.1.** \(V=\{\varepsilon,a,b,ab,ba\}\). The walk \(\varepsilon\to a\to ab\to b\to ba\to a\to\varepsilon\) has up steps appending \(a\), \(b\), \(a\), so it costs \(3\) and spells \(aba\).

**5.2.** It returns to \(\varepsilon\), so it is closed and its edge multiset is balanced. Its up steps are \(\varepsilon\to a\), \(a\to ab\) and \(b\to ba\); its cost is \(3\) and it spells \(aba\), which contains \(ab\) and \(ba\).

**5.3.** Let \(c=T(i)\). Every suffix of \(T[0:i+1)\) in \(V\) has the form \(xc\), where \(x\) is a suffix of \(T[0:i)\) in \(V\), since \(V\) is closed under substrings; so \(x\) is a suffix of \(u_i\). Hence \(u_{i+1}=x c\) for the longest suffix \(x\) of \(u_i\) with \(xc\in V\) (the empty suffix qualifies since \(c\in V\)): delete letters from the front of \(u_i\) down to \(x\), then append \(c\). If a required string \(s\) occurs at \(T[j:j+|s|)\), then \(s\) is a suffix of \(T[0:j+|s|)\) in \(V\), and by Lemma 1.1 no element of \(V\) longer than \(s\) has \(s\) as a suffix; so \(u_{j+|s|}=s\). The walk makes exactly one up step per letter of \(T\), and finally deletes letters down to \(\varepsilon\). With Lemma 2.1, the least cost of such a closed walk equals \(\mathrm{OPT}(\mathcal S)\).

**5.4.** Two disjoint directed cycles form a balanced multiset with disconnected support and no Euler tour. A single edge \(u\to w\) is connected but not balanced, and no closed walk uses it exactly once.

## References

- [OpenAI-SCS] OpenAI, *A polynomial-time 2-approximation for shortest common superstring*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026
- [GKM] A. Golovnev, A. S. Kulikov and I. Mihajlin, *Solving SCS for bounded length strings in fewer than 2^n steps*, Information Processing Letters 114 (2014), 421–425. https://golovnev.org/papers/scs_exact.pdf
- [GKLMN] A. Golovnev, A. S. Kulikov, A. Logunov, I. Mihajlin and M. Nikolaev, *Collapsing superstring conjecture*, APPROX/RANDOM 2019. https://arxiv.org/abs/1809.08669
- [Mu] M. Mucha, *Lyndon words and short superstrings*, Proceedings of SODA 2013, 958–972. https://arxiv.org/abs/1205.6787
- [EMV] M. Englert, N. Matsakis and P. Veselý, *Approximation guarantees for shortest superstrings: simpler and better*, ISAAC 2023, LIPIcs 283, 29:1–29:17. https://doi.org/10.4230/LIPIcs.ISAAC.2023.29
- [CKMS] N. Chukhin, A. S. Kulikov, I. Mihajlin and A. Smal, *A tight cycle-cover inequality for shortest common superstring*, 2026. https://arxiv.org/abs/2609.27921
- [Sh] H. Shibata, *Disproving the greedy superstring conjecture*, 2026. https://arxiv.org/abs/2609.01365
