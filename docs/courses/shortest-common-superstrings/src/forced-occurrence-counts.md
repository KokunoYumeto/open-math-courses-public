# Forced occurrence counts

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Every letter of a common superstring \(T\) is an occurrence of a one-letter word, so \(|T|=\sum_{c\in\Sigma}N_T(c)\), where \(N_T(s)\) is the number of positions at which \(s\) occurs in \(T\). This lesson constructs numbers \(m(s)\), one for each nonempty substring \(s\) of the input, with \(m(s)\le N_T(s)\) for *every* common superstring \(T\) (Lemma 2.2), following OpenAI [OpenAI-SCS]. Then \(W=\sum_cm(c)\) is a lower bound for the optimum. The numbers satisfy the inequalities that relate occurrences of a word to occurrences of its one-letter extensions, and a further rule for periodic words. From them we build a balanced *base graph* with exactly \(W\) up edges that contains every required string (Lemma 3.1).

We use the notation of [Superstrings and the hierarchical graph](superstrings-and-the-hierarchical-graph.md): the required strings after preprocessing (Lemma 1.1 there), assumed to be at least one, the set \(V\) of their substrings, the alphabet \(\Sigma\), and \(L\), the sum of the lengths of the required strings. Words not in \(V\) have count \(0\) throughout.

## 1. Periodic texts and blocked occurrences

A *periodic text* is a map \(A\colon\mathbb Z\to\Sigma\) with \(A(i+p)=A(i)\) for all \(i\) and some integer \(p\ge1\), a *period* of \(A\). We write \(A[i:j)\) for the string \(A(i)A(i+1)\cdots A(j-1)\).

Fix a periodic text \(A\) and a nonempty string \(s\) with \(A[0:|s|)=s\). For \(r\in V\), let \(b_{A,s}(r)\) be the number of integers \(j\) with \(1\le j\) and \(j+|s|\le|r|-1\) such that
\[
r(h)=A(h-j)\quad(1\le h\le|r|-2),\qquad r(0)\neq A(-j),\qquad r(|r|-1)\neq A(|r|-1-j).\tag{1.1}
\]
Placing position \(j\) of \(r\) at position \(0\) of \(A\), the word \(r\) agrees with \(A\) except at its two end letters, and \(s=r[j:j+|s|)\) lies strictly inside. For a function \(m\) on the nonempty words, let
\[
B_A(s;m)=\sum_{r\in V\setminus\{\varepsilon\}}b_{A,s}(r)\,m(r).\tag{1.2}
\]
Only words with \(|r|\ge|s|+2\) contribute.

Let \(T\) be a finite string with an occurrence of \(s\) at position \(i\). *Align* it with \(A\) by comparing \(T(i+x)\) with \(A(x)\) for \(0\le i+x<|T|\). The *nearest left mismatch* is the largest \(x<0\) with \(T(i+x)\neq A(x)\), and the *nearest right mismatch* the smallest \(x\ge|s|\) with \(T(i+x)\neq A(x)\), if they exist. When both exist at \(x_L\) and \(x_R\), the *bracketing word* of the occurrence is \(T[i+x_L:i+x_R+1)\). The occurrence is *blocked* if both mismatches exist and its bracketing word belongs to \(V\), and *unblocked* otherwise.

**Lemma 1.1.** \(B_A(s;N_T)\) is the number of blocked occurrences of \(s\) in \(T\); in particular \(B_A(s;N_T)\le N_T(s)\).

**Proof.** Consider pairs consisting of an occurrence of some \(r\in V\) in \(T\), at position \(i'\), and an integer \(j\) counted in \(b_{A,s}(r)\); there are \(B_A(s;N_T)\) of them. The pair gives the occurrence of \(s\) at \(i'+j\): by (1.1), aligned with \(A\) it agrees at the interior positions of \(r\) and disagrees at the two ends, so its nearest mismatches are the ends of \(r\), its bracketing word is \(r\in V\), and it is blocked. Conversely, a blocked occurrence determines its bracketing word \(r\), the position \(i'\) of that word and the offset \(j\) of the occurrence inside it. So the pairs correspond exactly to the blocked occurrences. \(\square\)

A single occurrence of \(r\) can bracket several occurrences of \(s\) (Exercise 4.3); this is why \(b_{A,s}(r)\) counts placements.

## 2. The counts

**Lemma 2.1.** For every string \(T\) and every nonempty \(s\),
\[
N_T(s)\ge\sum_{c\in\Sigma}N_T(cs),\qquad N_T(s)\ge\sum_{c\in\Sigma}N_T(sc).\tag{2.1}
\]
If \(T\) is a common superstring, then \(N_T(s)\ge1\) for every required string \(s\).

**Proof.** An occurrence of \(cs\) at position \(i\) gives an occurrence of \(s\) at \(i+1\), and different pairs \((c,i)\) give different positions \(i+1\). The same holds for right extensions. \(\square\)

**Definition 2.1** (forced counts). Define integers \(m(s)\ge0\) for the nonempty \(s\in V\), in order of decreasing length, as follows: \(m(s)\) is the least integer that satisfies

1. \(m(s)\ge\sum_cm(cs)\) and \(m(s)\ge\sum_cm(sc)\);
2. \(m(s)\ge1\) if \(s\) is required;
3. the *periodic rules*: for every \(v\in V\), every integer \(p\ge1\) such that \(v\) has period \(p\) (that is, \(v(i)=v(i+p)\) for \(0\le i<|v|-p\)), and every \(k\ge1\) with \(|v|=|s|+kp\) and \(s=v[0:|s|)\): let \(A\) be the periodic text with period \(p\) and \(A[0:p)=v[0:p)\), so that \(A[0:|v|)=v\). If
\[
m(v)>B_A(v;m),\tag{2.2}
\]
then \(m(s)\ge B_A(s;m)+k+1\).

The right sides only involve words longer than \(s\): \(v\) is longer than \(s\), and every word contributing to \(B_A(v;m)\) or \(B_A(s;m)\) is longer than \(v\) or \(s\). So the counts are well defined. A rule is determined by the triple \((v,p,k)\) with \(kp<|v|\), so there are finitely many rules.

**Lemma 2.2** (occurrence lower bound; OpenAI). For every common superstring \(T\) and every nonempty \(s\in V\), \(m(s)\le N_T(s)\). Consequently
\[
W:=\sum_{c\in\Sigma}m(c)\le\mathrm{OPT}(\mathcal S),\qquad m(s)\le L.
\]

**Proof.** Write \(N=N_T\). We prove \(m(s)\le N(s)\) by induction on decreasing length; it suffices to show that \(N(s)\) satisfies every lower bound used in Definition 2.1. Conditions 1 and 2 hold for \(N\) by Lemma 2.1 and induction. Consider a periodic rule \((v,p,k)\) whose trigger (2.2) holds; we show \(N(s)\ge B_A(s;N)+k+1\), which is at least \(B_A(s;m)+k+1\), since every word in \(B_A(s;\cdot)\) is longer than \(s\) and has \(N\ge m\) by induction.

*Case \(N(v)>B_A(v;N)\).* By Lemma 1.1, \(v\) has an unblocked occurrence in \(T\), say at position \(i\). Since \(v=A[0:|v|)\) has period \(p\), the word \(s\) occurs at positions \(i,i+p,\dots,i+kp\), all inside this occurrence of \(v\). Aligned with \(A\) at its own position \(i+lp\), each of these occurrences compares \(T(i+lp+x)\) with \(A(x)=A(lp+x)\), so it uses the same alignment as the occurrence of \(v\). All positions inside the occurrence of \(v\) agree with \(A\), so the nearest mismatches of each occurrence of \(s\) are those of the occurrence of \(v\), and so are its bracketing words. Hence these \(k+1\) occurrences are unblocked, and by Lemma 1.1, \(N(s)-B_A(s;N)\ge k+1\).

*Case \(N(v)\le B_A(v;N)\).* By Lemma 1.1 equality holds, and with the induction hypothesis and (2.2),
\[
\sum_rb_{A,v}(r)\bigl(N(r)-m(r)\bigr)=B_A(v;N)-B_A(v;m)=N(v)-B_A(v;m)\ge m(v)-B_A(v;m)>0,
\]
where every difference \(N(r)-m(r)\) is nonnegative. Choose \(r\) with \(b_{A,v}(r)\ge1\) and \(N(r)\ge m(r)+1\), and an offset \(j\) counted in \(b_{A,v}(r)\). The offsets \(j,j+p,\dots,j+kp\) are counted in \(b_{A,s}(r)\): by periodicity, \(A(h-j-lp)=A(h-j)\), so (1.1) holds with the same values, and \(j+lp+|s|\le j+|v|\le|r|-1\). Hence \(b_{A,s}(r)\ge k+1\), and since all terms are nonnegative,
\[
N(s)\ge B_A(s;N)\ge B_A(s;m)+b_{A,s}(r)\bigl(N(r)-m(r)\bigr)\ge B_A(s;m)+k+1.
\]
In both cases the rule holds for \(N\). For an optimal \(T\), \(W=\sum_cm(c)\le\sum_cN_T(c)=|T|=\mathrm{OPT}(\mathcal S)\). For \(T\) the concatenation of the required strings, \(m(s)\le N_T(s)\le|T|=L\). \(\square\)

The periodic rule records forced repetitions. For example, if the only required string is \(a^h\) with \(h\ge2\), the extension inequalities alone allow \(m(a^j)=1\) for all \(j\), with \(W=1\). The constant text \(A=aaa\cdots\) has period \(1\), every word \(r\in V\) agrees with it, so all blocking functionals vanish; the rule for \(v=a^h\), \(p=1\), \(k=h-j\) forces \(m(a^j)\ge h-j+1\), and indeed \(m(a^j)=h-j+1=N_{a^h}(a^j)\) and \(W=h=\mathrm{OPT}\).

## 3. The base graph

Give the up edge \(\operatorname{pref}(s)\to s\) and the down edge \(s\to\operatorname{suf}(s)\) at each nonempty \(s\in V\) the multiplicities
\[
u(s)=m(s)-\sum_cm(cs),\qquad d(s)=m(s)-\sum_cm(sc),\tag{3.1}
\]
both nonnegative by Definition 2.1. The *base graph* \(G\) is this multiset of edges.

**Lemma 3.1** (OpenAI). The base graph is balanced, its support contains every required string, and it has \(W\) up edges and \(W\) down edges, counted with multiplicity.

**Proof.** At a nonempty \(s\), the edges entering \(s\) are the up edge into \(s\) and the down edges from the words \(cs\); those leaving \(s\) are its down edge and the up edges into the words \(sc\). So
\[
\text{in}(s)=u(s)+\sum_cd(cs)=m(s)-\sum_{c,c'}m(csc'),\qquad\text{out}(s)=d(s)+\sum_cu(sc)=m(s)-\sum_{c,c'}m(c'sc),
\]
and the two agree. Since the numbers of edges entering and leaving all vertices have equal sums, the vertex \(\varepsilon\) is balanced too. Every word of length at least \(2\) is \(cs\) for exactly one letter \(c\) and one nonempty \(s\), so \(\sum_su(s)=\sum_sm(s)-\sum_{|s'|\ge2}m(s')=\sum_cm(c)=W\), and likewise for \(d\). A required string has no proper extension in \(V\) (Lemma 1.1 of [Superstrings and the hierarchical graph](superstrings-and-the-hierarchical-graph.md)), so both its edges have multiplicity \(m(s)\ge1\). \(\square\)

By Corollary 3.2 of [Superstrings and the hierarchical graph](superstrings-and-the-hierarchical-graph.md), it suffices to add closed walks, of total cost at most \(W\), that connect the support of \(G\) to \(\varepsilon\). For \(a^h\), the base graph already contains the path from \(\varepsilon\) to \(a^h\) in both directions and is connected. In general it is not (Exercise 4.1).

## 4. Exercises

**Exercise 4.1** (easy). For \(\mathcal S=\{ab,ba\}\), compute the counts \(m\), the number \(W\), and the base graph. Show that the base graph is a closed walk of cost \(2\) that does not contain \(\varepsilon\), and that \(W=2<\mathrm{OPT}=3\).

**Exercise 4.2** (easy). For the single required string \(a^h\), check directly that \(N_T(a^j)\ge h-j+1\) for every string \(T\) containing \(a^h\), and describe the base graph.

**Exercise 4.3** (medium). Let \(A\) have period \(2\) with \(A(0)=a\), \(A(1)=b\), let \(s=a\), and let \(r=cababc\in V\), where \(c\neq a,b\). Show that \(b_{A,s}(r)=2\), and find the two occurrences of \(a\) in \(r\) that \(r\) brackets.

**Exercise 4.4** (medium). In the proof of Lemma 2.2, why must the occurrences of \(s\) at positions \(i+lp\) be aligned at their own positions rather than at \(i\)? Show that with \(p\ge1\) arbitrary the alignments agree.

## 5. Solutions

**4.1.** \(V=\{\varepsilon,a,b,ab,ba\}\). The required words get \(m(ab)=m(ba)=1\). Neither \(ab\) nor \(ba\) has a period smaller than its length, so no periodic rule applies. Then \(m(a)=\max(m(ba),m(ab))=1\) and \(m(b)=1\), so \(W=2\). By (3.1), \(u(ab)=d(ab)=u(ba)=d(ba)=1\) and all other multiplicities are \(0\): the edges are \(a\to ab\to b\to ba\to a\), a closed walk of cost \(2\) avoiding \(\varepsilon\). A shortest superstring is \(aba\), so \(\mathrm{OPT}=3\).

**4.2.** An occurrence of \(a^h\) at position \(i\) contains occurrences of \(a^j\) at the \(h-j+1\) positions \(i,\dots,i+h-j\). With \(m(a^j)=h-j+1\), (3.1) gives \(u(a^j)=m(a^j)-m(a^{j+1})=1\) and \(d(a^j)=1\) for \(1\le j\le h\): the base graph is the path \(\varepsilon\to a\to\dots\to a^h\) of up edges together with the down edges back.

**4.3.** Both \(j=1\) and \(j=3\) satisfy (1.1): the letters \(r(1)\dots r(4)=abab\) agree with \(A(h-j)\), and \(r(0)=r(5)=c\) differ from the letters of \(A\) there. For \(j=2,4\), \(r(j)=b\neq a\). The bracketed occurrences are those of \(a\) at positions \(1\) and \(3\) of \(r\).

**4.4.** Blocking is defined with the alignment of each occurrence at its own position. For the occurrence at \(i+lp\), position \(i+lp+x\) is compared with \(A(x)=A(x+lp)\), which is the letter compared with \(T(i+(x+lp))\) in the alignment of the occurrence of \(v\) at \(i\); so the two alignments compare the same pairs of letters.

## References

- [OpenAI-SCS] OpenAI, *A polynomial-time 2-approximation for shortest common superstring*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026
