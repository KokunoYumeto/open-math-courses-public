# Projective planes and prescribed types

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The two graphs of [Group algebras and zero divisors](group-algebras-and-zero-divisors.md) are random, but the sets of letters at their vertices are prescribed in advance. This lesson fixes the alphabet and the prescriptions [OpenAI-KZ, Section 2.1–2.2]. The letters are the points of the projective plane over the field with \(128\) elements and three further letters; the outgoing letters of a vertex are a line of the plane together with some of the extra letters. Two lines meet in one point or coincide, so they share an odd number of points, and the extra letters are arranged so that they add an even number. This gives the odd intersections that Proposition 3.2 of that lesson needs, before any random choice is made. The same prescriptions control how often a word of letters can be read along a random path, through a decay estimate for squared word weights proved at the end of the lesson.

- Finite projective planes (Section 1).
- The alphabet and the prescribed types (Section 2).
- Turn weights (Section 3).
- The squared-word estimate (Section 4).

Signed alphabets, outgoing letters and immersed labelled graphs are as in Section 3 of [Group algebras and zero divisors](group-algebras-and-zero-divisors.md). From the core course [Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40) (Judson, *Abstract Algebra: Theory and Applications*) we use that there is a field with \(2^7=128\) elements ([Theorem 22.1.6](https://judsonbooks.org/aata-files/aata-html/finite-section-field.html)), and that in a vector space over a field coordinates in a basis are unique and any two bases have the same number of elements ([Propositions 20.3.1 and 20.3.6](https://judsonbooks.org/aata-files/aata-html/vect-section-linear-independence.html)).

## 1. Finite projective planes

Let \(\mathbb F_q\) be a finite field with \(q\) elements and \(V=\mathbb F_q^3\). A subspace of \(V\) of dimension \(k\) has exactly \(q^k\) elements, since its elements are the combinations of a basis with unique coefficients. The *points* of the projective plane over \(\mathbb F_q\) are the subspaces of dimension \(1\) and its *lines* are the subspaces of dimension \(2\); a point *lies on* a line if it is contained in it.

**Lemma 1.1** (projective planes). Put \(v=q^2+q+1\).

1. There are \(v\) points and \(v\) lines.
2. Every line contains \(q+1\) points, and every point lies on \(q+1\) lines.
3. Two distinct points lie on exactly one common line, and two distinct lines meet in exactly one point.

*Proof.* A point contains \(q-1\) nonzero vectors and every nonzero vector lies in exactly one point, so there are \((q^3-1)/(q-1)=v\) points. In the same way a line contains \((q^2-1)/(q-1)=q+1\) points.

Two distinct points \(\langle x\rangle,\langle y\rangle\) have linearly independent generators, so \(W=\langle x,y\rangle\) is a line containing both. A line \(W'\) containing both contains \(W\), and both have \(q^2\) elements, so \(W'=W\).

Two distinct lines \(W,W'\) meet in a subspace. If \(W\cap W'=\{0\}\), the map \(W\times W'\to V\), \((w,w')\mapsto w+w'\), would be injective, because \(w_1+w_1'=w_2+w_2'\) gives \(w_1-w_2=w_2'-w_1'\in W\cap W'\); but \(q^4>q^3\). If \(W\cap W'=W\), then \(W\subseteq W'\) and the two have the same number of elements, so \(W=W'\). Hence \(W\cap W'\) is a subspace of \(W\) of dimension \(1\): exactly one point.

Every pair of distinct points lies on exactly one line, and every line contains \(\binom{q+1}2\) pairs, so the number of lines is \(\binom v2/\binom{q+1}2=\frac{v(v-1)}{(q+1)q}=v\), using \(v-1=q(q+1)\). Finally, the lines through a point \(\langle x\rangle\) are the lines through \(\langle x\rangle\) and one of the other \(v-1\) points, and each such line contains \(q\) of these points, so there are \((v-1)/q=q+1\) of them. \(\square\)

## 2. The alphabet and the prescribed types

From now on
\[
\begin{aligned}q&=128,\\v&=q^2+q+1=16513,\\p&=\frac{q+1}v=\frac{129}{16513}.\end{aligned}
\]
The *ordinary letters* are the \(v\) points of the projective plane over \(\mathbb F_{128}\), and there are three further *extra letters*. The alphabet \(T\) consists of these \(v+3=16516\) letters, with a fixed-point-free involution \(t\mapsto\bar t\) defined as follows: each extra letter is paired with one of three distinct ordinary letters, and the remaining \(v-3=16510\) ordinary letters are paired arbitrarily in twos. The rose over \(T\) has \(8258\) loops, one for each pair.

Let \(A\) and \(B\) be disjoint sets of \(n\) vertices each, where \(n\) is a multiple of \(2v^2\). To every vertex \(x\) we assign its *type*, a set \(S_x\subseteq T\) that will be its set of outgoing letters:

1. On either side, the ordinary part of \(S_x\) is the set of points of a line, and every line occurs for exactly \(n/v\) vertices of the side; these vertices form the *line class* of the line.
2. In each line class on \(A\), the extra part of \(S_x\) is each of the three two-element sets of extra letters for exactly \(\frac p2\cdot\frac nv\) vertices, and is empty for the others.
3. In each line class on \(B\), the extra part of \(S_x\) is the set of all three extra letters for exactly \(p\cdot\frac nv\) vertices, and is empty for the others.

These numbers are integers because \(n/v\) is a multiple of \(2v\) and \(pv=129\): a line class has \(n/v=2vk\) vertices for \(n=2v^2k\), of which \(129k\) have each two-element extra set on \(A\) and \(258k\) have the three extras on \(B\). For \(n=2v^2\), a line class has \(33026\) vertices: on \(A\), \(129\) of each double type and \(32639\) without extras; on \(B\), \(258\) with three extras and \(32768\) without. Every type has between \(q+1=129\) and \(d_*=q+4=132\) letters.

For a letter \(t\) and a side \(Y\in\{A,B\}\) put \(Y_t=\{x\in Y:t\in S_x\}\).

**Lemma 2.1** (types; [OpenAI-KZ, Section 2.1]).

1. Every letter \(t\) has \(\#Y_t=np\) on each side \(Y\).
2. For every \(x\in A\) and \(y\in B\), the number \(\#(S_x\cap S_y)\) is odd.

*Proof.* (1) An ordinary letter lies on \(q+1\) of the \(v\) lines, so \(\#Y_t=(q+1)\frac nv=np\). An extra letter lies in two of the three two-element sets, so on \(A\) each line class contributes \(2\cdot\frac p2\cdot\frac nv\) vertices and \(\#A_t=np\); on \(B\) each line class contributes \(p\frac nv\) vertices, and \(\#B_t=np\).

(2) The ordinary parts of \(S_x\) and \(S_y\) are lines; they share one point if they are distinct and \(q+1=129\) points if they are equal, an odd number in both cases. The extra part of \(S_x\) has \(0\) or \(2\) elements, and that of \(S_y\) has \(0\) or \(3\), so they share \(0\) or \(2\) letters. The sum is odd. \(\square\)

So whatever the edges of the graphs turn out to be, the condition of Proposition 3.2 of [Group algebras and zero divisors](group-algebras-and-zero-divisors.md) holds, provided every vertex has exactly its type as set of outgoing letters. The random choice in [Random matchings with large girth](random-matchings-with-large-girth.md) is used only to control the geometry of the graphs.

## 3. Turn weights

A *turn* is a pair of consecutive letters \(t,u\) of a path; it is *cancelling* if \(u=\bar t\). At the vertex between the two edges, the outgoing letters include \(\bar t\), the first edge read backwards, and \(u\). For a non-cancelling turn \(t,u\) let \(w(t,u)\) be the proportion of vertices of \(B\) containing \(u\) among those containing \(\bar t\):
\[
w(t,u)=\frac{\#\{y\in B:\bar t,u\in S_y\}}{\#B_{\bar t}},
\]
and put \(w(t,\bar t)=0\).

**Lemma 3.1** (turn weights; [OpenAI-KZ, Section 2.2]).

1. For distinct \(\bar t\) and \(u\), \(w(t,u)\) is \(1/(q+1)\) if both are ordinary, \(p\) if exactly one is extra, and \(1\) if both are extra. Every positive turn weight lies in \([1/129,1]\).
2. The corresponding proportion on \(A\), the share of vertices of \(A\) containing \(u\) among those containing \(\bar t\), is at most \(w(t,u)\).
3. \(w(t,u)=w(\bar u,\bar t)\) for all letters \(t,u\).

*Proof.* (1) If \(\bar t\) and \(u\) are distinct points, the vertices of \(B\) containing \(\bar t\) are those whose line passes through \(\bar t\), in \(q+1\) equally large line classes, and exactly one of these lines passes through \(u\); the proportion is \(1/(q+1)\). If \(\bar t\) is a point and \(u\) extra, the vertices containing \(u\) are those with all three extras, a proportion \(p\) of every line class. If \(\bar t\) is extra and \(u\) a point, the vertices containing \(\bar t\) form the same proportion of every line class, and the line classes through \(u\) make up \((q+1)/v=p\) of all line classes. If both are extra, every vertex of \(B\) with one extra letter has all three. Finally \(p=129/16513>1/129\).

(2) On \(A\) the proportions are the same, except when \(\bar t\) and \(u\) are both extra: the vertices containing \(\bar t\) have one of the two two-element sets containing \(\bar t\), equally often, and half of them contain \(u\); and \(\frac12\le1\).

(3) By Lemma 2.1(1), \(\#B_{\bar t}=\#B_u=np\), so for a non-cancelling turn both sides equal \(\#\{y\in B:\bar t,u\in S_y\}/(np)\). The turn \(t,\bar t\) corresponds to the turn \(t,\bar t\) again, and both weights are \(0\). \(\square\)

For a word \(W=t_1t_2\cdots t_h\) of letters put
\[
P(W)=\prod_{i=1}^{h-1}w(t_i,t_{i+1}),
\]
and let \(W^{-1}=\bar t_h\cdots\bar t_1\) be the inverse word. By Lemma 3.1(3), \(w(\bar t_{i+1},\bar t_i)=w(t_i,t_{i+1})\), so
\[
P(W^{-1})=P(W).\tag{3.1}
\]
In [The bounded-pattern estimate](the-bounded-pattern-estimate.md), \(P(W)\) bounds the proportion of choices of a vertex path that can carry the word \(W\).

## 4. The squared-word estimate

**Lemma 4.1** (squared words; [OpenAI-KZ, Lemma 2.1]). For every \(h\ge3002\),
\[
\sum_{W\in T^h}P(W)^2\le e^{-h/300}.
\]
So the estimate \(\sum_{W\in T^h}P(W)^2\le e^{-2\delta h}\) holds with \(\delta=1/600\) for all large \(h\).

*Proof.* Let \(M\) be the matrix indexed by \(T\times T\) with entries \(M_{t,u}=w(t,u)^2\), and let \(f(t)=5\) if \(\bar t\) is extra and \(f(t)=1\) otherwise. Exactly three letters \(t\) have \(f(t)=5\), namely the ordinary letters paired with the extras. We show
\[
\begin{aligned}(Mf)(t)&=\sum_{u\in T}w(t,u)^2f(u)\\&\le\tfrac{149}{150}f(t)\qquad(t\in T).\end{aligned}
\]

If \(\bar t\) is ordinary, the \(v-1\) ordinary letters \(u\ne\bar t\) have \(w(t,u)=1/(q+1)\), and at most three of them have \(f(u)=5\); the three extra letters have \(w(t,u)=p\) and \(f(u)=1\). Hence
\[
\begin{aligned}
(Mf)(t)&\le\frac{v-1}{(q+1)^2}+\frac{3\cdot4}{(q+1)^2}+3p^2\\
&=\frac q{q+1}+\frac{12}{(q+1)^2}+3p^2,
\end{aligned}
\]
since \(v-1=q(q+1)\). This number equals \(\frac{500731261911}{504183783481}<\frac{149}{150}\). If \(\bar t\) is extra, then \(f(t)=5\); the two other extra letters have weight \(1\) and \(f=1\), and the \(v\) ordinary letters have weight \(p\), at most three of them with \(f=5\). Hence
\[
\begin{aligned}\frac{(Mf)(t)}{f(t)}&\le\frac{2+vp^2+12p^2}5\\&=\frac{820350863}{1363395845}<\frac{149}{150}.\end{aligned}
\]

Now \(\sum_{W\in T^h}P(W)^2=\mathbf 1^{\mathsf T}M^{h-1}\mathbf 1\), where \(\mathbf 1\) is the vector of ones: expanding the matrix product gives the sum over all words of the products of the squared turn weights. Since \(M\) has nonnegative entries and \(\mathbf 1\le f\) entrywise, \(Mf\le\frac{149}{150}f\) gives by induction \(M^{h-1}f\le(\frac{149}{150})^{h-1}f\), and
\[
\begin{aligned}
\sum_{W\in T^h}P(W)^2&\le\mathbf 1^{\mathsf T}M^{h-1}f\\
&\le\Bigl(\frac{149}{150}\Bigr)^{h-1}\sum_tf(t).
\end{aligned}
\]
Here \(\sum_tf(t)=16516+12=16528<e^{10}\). Since \(\log\frac{150}{149}>\frac1{150}\),
\[
\Bigl(\frac{149}{150}\Bigr)^{h-1}e^{10}\le e^{10-(h-1)/150}\le e^{-h/300}
\]
as soon as \(h/300\ge10+1/150\), that is, for \(h\ge3002\). \(\square\)

The point of squaring is that the weights \(P(W)\) of the words of length \(h\) need not have a small sum, but their squares do: the squared turn weights from an ordinary letter add up to about \(q/(q+1)\), less than one, while the plain weights add up to more than one.

## 5. Exercises

**5.1.** Check the numbers of Section 2 for \(n=2v^2\): the size of a line class, the numbers of vertices of each type, and \(\#Y_t=np\) for an ordinary and an extra letter.

**5.2.** Show that \(\sum_uw(t,u)\ge1\) for every letter \(t\) whose inverse \(\bar t\) is ordinary, so that the unsquared weights do not decay.

**5.3.** Let \(q=2\). Draw the projective plane over \(\mathbb F_2\) (the Fano plane) and check Lemma 1.1 for it.

**5.4.** Show that if the extra part of every type on \(A\) had one element instead of two, Lemma 2.1(2) would fail.

**5.5.** Show that \(\mathbf 1^{\mathsf T}M^{h-1}\mathbf 1=\sum_{W\in T^h}P(W)^2\), including the role of the cancelling turns.

## 6. Solutions

**5.1.** \(n/v=2v=33026\). On \(A\): \(\frac p2\cdot33026=\frac{129}{2\cdot16513}\cdot33026=129\) for each of the three double types, and \(33026-387=32639\) without extras. On \(B\): \(p\cdot33026=258\) and \(33026-258=32768\). An ordinary letter lies on \(129\) lines, so \(\#Y_t=129\cdot33026=4260354\); and \(np=2v^2\cdot\frac{129}{v}=258v=4260354\). An extra letter on \(A\) lies in \(2\cdot129=258\) vertices of each of the \(v\) line classes, again \(258v\).

**5.2.** If \(\bar t\) is ordinary, the \(v-1\) other ordinary letters contribute \((v-1)/(q+1)=q\), so the sum is at least \(q=128\).

**5.3.** The Fano plane has \(7\) points and \(7\) lines, three points on every line and three lines through every point; any two points lie on one line and any two lines meet in one point. With \(q=2\): \(v=7\) and \(q+1=3\).

**5.4.** Two vertices with the same line and extra parts \(\{e\}\) on \(A\) and all three extras on \(B\) would share \(129+1=130\) letters, an even number.

**5.5.** \((M^{h-1})_{t_1,t_h}\) is the sum over all words \(t_1t_2\cdots t_h\) with these ends of \(\prod_iM_{t_i,t_{i+1}}=P(W)^2\). A word with a cancelling turn has \(P(W)=0\) and contributes nothing, consistent with \(M_{t,\bar t}=0\).

## References

- [OpenAI-KZ] OpenAI, *A Torsion-Free Group Algebra with Zero Divisors*, OpenAI Math Release preprint, 23 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026
