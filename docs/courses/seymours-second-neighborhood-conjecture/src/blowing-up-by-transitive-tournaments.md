# Blowing up by transitive tournaments

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[Second out-neighborhoods and minimal counterexamples](second-out-neighborhoods-and-minimal-counterexamples.md) showed that a minimal counterexample \(D\) to the second neighborhood conjecture satisfies the *subset deficit*
\[
\bigl|F^2(S)\setminus F(S)\bigr|<\bigl|F(S)\setminus S\bigr|\qquad(\varnothing\ne S\subsetneq V(D)) \tag{0.1}
\]
(Proposition 3.3 there), and that every vertex of \(D\) has an in-neighbor. This lesson converts (0.1) into a cleaner inequality that involves \(U\), \(F(U)\) and \(F^2(U)\) symmetrically:
\[
|U|+|F^2(U)|<2|F(U)|\qquad(\varnothing\ne U\subsetneq V(G)). \tag{0.2}
\]
In words, the three numbers \(|U|\), \(|F(U)|\), \(|F^2(U)|\) form a strictly concave sequence. The graph \(G\) is obtained from \(D\) by replacing every vertex with a large transitive tournament. The point of the construction is that a deficit of one unit in (0.1) is multiplied by the block size \(m\), while the transitive tournaments cost at most one unit per vertex of \(D\). OpenAI notes that the same product appears in the work of Brantner, Brockman, Kay and Snively [BBKS]; here it is needed for all nonempty proper sets of vertices.

Notation: \(D\) is an oriented graph on \(n\ge1\) vertices, \(F=F_D\) is its image operator, and \([m]=\{1,\dots,m\}\).

## 1. The product with a transitive tournament

**Definition 1.1.** For an integer \(m\ge1\), the oriented graph \(G=D[T_m]\) has vertex set \(V(D)\times[m]\), and \((v,a)\to(w,b)\) is an arc of \(G\) if either \(v\to w\) in \(D\), or \(v=w\) and \(a<b\). The set \(\{v\}\times[m]\) is the *block* of \(v\). An arc of \(G\) is *external* if its ends lie in different blocks and *internal* otherwise.

**Lemma 1.2.** \(G\) is an oriented graph. If every vertex of \(D\) has an in-neighbor, then every vertex of \(G\) has an in-neighbor, and \(F_G(V(G))=V(G)\).

*Proof.* There are no loops. Two opposite arcs between \((v,a)\) and \((w,b)\) would require either \(v\to w\) and \(w\to v\) in \(D\), or \(v=w\), \(a<b\) and \(b<a\). If \(u\to v\) in \(D\), then \((u,1)\to(v,a)\) for every \(a\in[m]\). \(\square\)

Inside one block, the arcs form the transitive tournament on \([m]\). Its image operator is
\[
f(T)=\{b\in[m]:a<b\text{ for some }a\in T\}\qquad(T\subseteq[m]).
\]

**Lemma 1.3.** For every \(T\subseteq[m]\),
\[
|T|-|f(T)|\le1,\qquad f^2(T)\subseteq f(T),\qquad |T|-2|f(T)|+|f^2(T)|\le1 .
\]

*Proof.* For \(T=\varnothing\) all three quantities vanish. Otherwise let \(a\) be the least element of \(T\). Then \(f(T)=\{a+1,\dots,m\}\) and \(T\subseteq\{a,\dots,m\}\), so \(|T|\le m-a+1=|f(T)|+1\). Next, \(f^2(T)=f(\{a+1,\dots,m\})\) equals \(\{a+2,\dots,m\}\) if \(a<m\) and is empty if \(a=m\); in both cases it lies in \(f(T)\). If \(a<m\), then \(|T|-2|f(T)|+|f^2(T)|\le(m-a+1)-2(m-a)+(m-a-1)=0\). If \(a=m\), then \(T=\{m\}\) and the quantity equals \(1\). \(\square\)

## 2. Images in the product

Fix \(U\subseteq V(G)\). For \(v\in V(D)\) let \(T_v=\{a\in[m]:(v,a)\in U\}\), and let
\[
S=\{v\in V(D):T_v\ne\varnothing\}
\]
be the *support* of \(U\). Thus \(|U|=\sum_{v\in S}|T_v|\).

**Lemma 2.1.** The first and second images of \(U\) in \(G\) satisfy
\[
F_G(U)=\bigl(F(S)\times[m]\bigr)\cup\bigcup_{v\in S\setminus F(S)}\{v\}\times f(T_v),
\]
\[
F_G^2(U)\subseteq\bigl((F(S)\cup F^2(S))\times[m]\bigr)\cup\bigcup_{v\in S}\{v\}\times f^2(T_v).
\]

*Proof.* An arc leaving \((v,a)\in U\) is either external, ending in a block of \(F(\{v\})\subseteq F(S)\), or internal, ending in \(\{v\}\times f(\{a\})\). Conversely, every vertex of a block of \(w\in F(S)\) is the head of an external arc from \(U\): if \(v\in S\) and \(v\to w\), then \((v,a)\to(w,b)\) for \(a\in T_v\) and every \(b\). Hence \(F_G(U)\) is the union of the blocks of \(F(S)\) and of the sets \(\{v\}\times f(T_v)\), \(v\in S\); those with \(v\in F(S)\) lie in full blocks already.

For the second image, consider a walk \(x\to y\to z\) in \(G\) with \(x\in U\) in the block of \(v\in S\). If both arcs are external, the blocks of \(x,y,z\) form a walk \(v\to w\to u\) in \(D\), so \(u\in F^2(S)\). If exactly one arc is external, then either the first arc moves to a block \(w\in F(\{v\})\) and the second stays in \(w\), or the first stays in the block of \(v\) and the second moves to a block of \(F(\{v\})\); in both cases \(z\) lies in a block of \(F(S)\). If both arcs are internal, then \(z\in\{v\}\times f(f(T_v))\). \(\square\)

**Proposition 2.2.** For every \(U\subseteq V(G)\) with support \(S\),
\[
|U|-2|F_G(U)|+|F_G^2(U)|\le m\Bigl(\bigl|F^2(S)\setminus F(S)\bigr|-\bigl|F(S)\setminus S\bigr|\Bigr)+|S\setminus F(S)| .
\]

*Proof.* Put \(H_0=F(S)\cup F^2(S)\), so \(|H_0|=|F(S)|+|F^2(S)\setminus F(S)|\). By Lemma 2.1, the sets \(F(S)\times[m]\) and \(\{v\}\times f(T_v)\) for \(v\in S\setminus F(S)\) are disjoint, so
\[
|F_G(U)|=m|F(S)|+\sum_{v\in S\setminus F(S)}|f(T_v)| .
\]
In the bound for \(F_G^2(U)\) in Lemma 2.1, the sets \(\{v\}\times f^2(T_v)\) with \(v\in H_0\) lie inside \(H_0\times[m]\). The remaining ones have \(v\in S\setminus H_0\subseteq S\setminus F(S)\), and adding the terms for the other \(v\in S\setminus F(S)\) only increases the bound:
\[
|F_G^2(U)|\le m|H_0|+\sum_{v\in S\setminus F(S)}|f^2(T_v)| .
\]
Finally \(|T_v|\le m\) gives \(|U|\le m|S\cap F(S)|+\sum_{v\in S\setminus F(S)}|T_v|\). Adding the three estimates, with the second multiplied by \(-2\),
\[
|U|-2|F_G(U)|+|F_G^2(U)|\le m\bigl(|H_0|-2|F(S)|+|S\cap F(S)|\bigr)+\sum_{v\in S\setminus F(S)}\bigl(|T_v|-2|f(T_v)|+|f^2(T_v)|\bigr).
\]
Each term of the last sum is at most \(1\) by Lemma 1.3. The bracket equals \(|F^2(S)\setminus F(S)|-|F(S)|+|S\cap F(S)|=|F^2(S)\setminus F(S)|-|F(S)\setminus S|\). \(\square\)

## 3. Strictly concave growth

**Theorem 3.1.** Let \(D\) be an oriented graph on \(n\ge1\) vertices in which every vertex has an in-neighbor and which satisfies the subset deficit (0.1). Let \(m>n\) be an integer and \(G=D[T_m]\). Then \(G\) is a nonempty oriented graph in which every vertex has an in-neighbor, and
\[
|U|+|F_G^2(U)|<2|F_G(U)|\qquad\text{for every }\varnothing\ne U\subsetneq V(G).
\]

*Proof.* The first claims are Lemma 1.2. Let \(\varnothing\ne U\subsetneq V(G)\) have support \(S\ne\varnothing\).

If \(S\ne V(D)\), then (0.1) says that \(|F^2(S)\setminus F(S)|-|F(S)\setminus S|\) is a negative integer, hence at most \(-1\). Proposition 2.2 and \(|S\setminus F(S)|\le n\) give
\[
|U|-2|F_G(U)|+|F_G^2(U)|\le-m+n<0 .
\]

If \(S=V(D)\), then \(F(S)=V(D)\) because every vertex of \(D\) has an in-neighbor, so \(F_G(U)\) contains every block by Lemma 2.1, that is, \(F_G(U)=V(G)\). Then \(F_G^2(U)=F_G(V(G))=V(G)\) by Lemma 1.2, and
\[
|U|-2|F_G(U)|+|F_G^2(U)|=|U|-|V(G)|<0
\]
because \(U\) is a proper subset. \(\square\)

**Corollary 3.2** (Reduction). If some nonempty finite oriented graph has no vertex \(v\) with \(|N_1^+(v)|\le|N_2^+(v)|\), then there is a nonempty finite oriented graph \(G\) in which every vertex has an in-neighbor and
\[
|U|+|F_G^2(U)|<2|F_G(U)|\qquad\text{for every }\varnothing\ne U\subsetneq V(G). \tag{3.1}
\]

*Proof.* Take a minimal counterexample \(D\). By Proposition 3.3 of [Second out-neighborhoods and minimal counterexamples](second-out-neighborhoods-and-minimal-counterexamples.md), every vertex of \(D\) has an in-neighbor and \(D\) satisfies (0.1). Apply Theorem 3.1 with \(m=|V(D)|+1\). \(\square\)

[The extremal argument and its consequences](the-extremal-argument-and-its-consequences.md) shows that no graph satisfies (3.1), which proves the conjecture.

For \(U=V(G)\) in a graph in which every vertex has an in-neighbor, all three numbers \(|U|,|F_G(U)|,|F_G^2(U)|\) equal \(|V(G)|\), so (3.1) can only be required for proper subsets. The next example shows that (3.1) is a strong condition even in small graphs.

**Example 3.3.** Let \(D\) be the directed triangle on \(\mathbb Z/3\), \(m\ge2\), \(G=D[T_m]\), and \(U=\{0\}\times[m]\). By Lemma 2.1, \(F_G(U)=(\{0\}\times\{2,\dots,m\})\cup(\{1\}\times[m])\) has \(2m-1\) elements. The formula for \(F_G\) in Lemma 2.1, applied to the set \(F_G(U)\), whose support is \(\{0,1\}\) with \(F(\{0,1\})=\{1,2\}\) and \(T_0=\{2,\dots,m\}\), gives
\[
F_G^2(U)=(\{0\}\times\{3,\dots,m\})\cup(\{1,2\}\times[m]),
\]
with \(3m-2\) elements. Hence \(|U|+|F_G^2(U)|=4m-2=2|F_G(U)|\), and (3.1) fails. This is consistent with Theorem 3.1, because the directed triangle does not satisfy (0.1) (Exercise 4.2 of the previous lesson).

## 4. Exercises

**4.1.** Show that equality \(|T|-2|f(T)|+|f^2(T)|=1\) in Lemma 1.3 holds only for \(T=\{m\}\), and that the quantity is at most \(0\) for every other \(T\).

**4.2.** In \(G=D[T_m]\), show that \(|N_1^+((v,a))|=m\,d^+(v)+(m-a)\) and \(N_2^+((v,a))=N_2^+(v)\times[m]\). Deduce that \(D[T_m]\) is a counterexample to the conjecture if and only if \(D\) is.

**4.3.** In Example 3.3, show that the single vertex \(U=\{(0,1)\}\) satisfies the strict inequality \(|U|+|F_G^2(U)|<2|F_G(U)|\).

**4.4.** Show that an oriented graph \(D\) satisfying the hypotheses of Theorem 3.1 has at least two vertices and is itself a counterexample to the conjecture. (Together with [The extremal argument and its consequences](the-extremal-argument-and-its-consequences.md), this shows that no oriented graph satisfies these hypotheses.)

## 5. Solutions

**4.1.** From the proof of Lemma 1.3, if the least element \(a\) of \(T\) satisfies \(a<m\), the quantity is at most \(|T|-(m-a)-1\le0\), and for \(T=\varnothing\) it is \(0\). The only remaining case is \(T=\{m\}\), where it equals \(1\).

**4.2.** The out-neighbors of \((v,a)\) are the blocks of \(N_1^+(v)\) and \(\{v\}\times\{a+1,\dots,m\}\). A walk of length two from \((v,a)\) ends in a block of \(F^2(\{v\})\) (two external arcs), in a block of \(N_1^+(v)\) (one external arc), or in \(\{v\}\times\{a+2,\dots,m\}\) (no external arc). The last two sets consist of out-neighbors of \((v,a)\), and every vertex of a block of \(F^2(\{v\})\) is reached by two external arcs. Since \(v\notin F^2(\{v\})\) (Lemma 1.1 of the previous lesson), \(N_2^+((v,a))=(F^2(\{v\})\setminus N_1^+(v))\times[m]=N_2^+(v)\times[m]\). Hence
\[
|N_1^+((v,a))|-|N_2^+((v,a))|=m\bigl(d^+(v)-|N_2^+(v)|\bigr)+(m-a).
\]
If \(D\) is a counterexample, the bracket is at least \(1\) and the difference is positive for every \((v,a)\). If some \(v\) has \(d^+(v)\le|N_2^+(v)|\), the vertex \((v,m)\) has a difference at most \(0\).

**4.3.** \(F_G(\{(0,1)\})=(\{0\}\times\{2,\dots,m\})\cup(\{1\}\times[m])\) has \(2m-1\) elements, and \(F_G^2(\{(0,1)\})=F_G(F_G(U))\) is the set computed in Example 3.3, with \(3m-2\) elements. Then \(1+(3m-2)=3m-1<4m-2\) because \(m\ge2\).

**4.4.** An oriented graph has no loops, so a graph with one vertex has a vertex without in-neighbors; hence \(n\ge2\). For a vertex \(v\), the set \(S=\{v\}\) is nonempty and proper. Since \(v\notin F(\{v\})\), we have \(|F(S)\setminus S|=|N_1^+(v)|\), and \(F^2(S)\setminus F(S)=N_2^+(v)\) by Lemma 1.1 of [Second out-neighborhoods and minimal counterexamples](second-out-neighborhoods-and-minimal-counterexamples.md). Thus (0.1) for \(S=\{v\}\) says \(|N_2^+(v)|<|N_1^+(v)|\), for every vertex \(v\).

## References

- [OpenAI-SN] OpenAI, *A proof of Seymour's second-neighborhood conjecture*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/paper.pdf
- [BBKS] J. N. Brantner, G. Brockman, B. Kay and E. E. Snively, *Contributions to Seymour's second neighborhood conjecture*, Involve 2 (2009); preprint 2008. https://arxiv.org/abs/0808.0946
