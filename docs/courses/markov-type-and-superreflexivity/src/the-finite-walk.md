# The finite walk

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the second main statement of the course. Let \(N\) be a norm on finite sequences that does not change when zeros are inserted and does not increase when neighbouring entries are added. For every \(n\) there is a reversible stationary walk whose steps carry labels of norm \(1\), with opposite labels for a step and its reverse, such that the sum of the first \(n\) labels has a norm of at least \(n/24\) with a probability of at least \(\tfrac3{20}\). Together with the reduction of the first lesson this proves that a space with nontrivial Markov type is superreflexive.

The states of the walk are charts: increasing maps from a finite set of points of the line to positions of a sequence. A step applies one of four homeomorphisms to the points and changes the chart so that the moved points keep their positions. The label of a step is a sum of differences of basis vectors at the positions of the ends of the arcs of its letter. The partial sums of the sum of all labels, read at suitable positions, are the values of the function \(c_w\) of the lesson on reduced words; they alternate between two levels.

- The landmarks, the chain and the labels (Section 1).
- Along good steps the positions of the orbit points do not change (Lemma 2.1).
- The partial sums of the total label (Lemma 3.1).
- From the two levels to the norm (Lemma 4.1).
- The walk with linear displacement (Theorem 5.1), and the theorem of the course (Theorem 5.2).

The lesson follows [OpenAI-M, Section 5]. It uses marked chains and the notions of spreading invariance and contractive merging from [Markov type and the reduction to a finite walk](markov-type-and-the-reduction-to-a-finite-walk.md), the chain of charts from [Charts and reversible transport](charts-and-reversible-transport.md), and the homeomorphisms \(h_s\), the arcs \(\mathcal A_s\) and the function \(c_w\) from [Two levels from reduced words](two-levels-from-reduced-words.md).

## 1. The chain and the labels

Throughout, \(N\) is a spreading invariant norm on \(c_{00}\) with contractive merging, and \(b_i\) is the sequence with \(1\) at the position \(i\). For \(k\ge1\) let
\[
D_k=N(1,-1,1,-1,\dots,1,-1),
\]
the norm of the array with \(k\) pairs \(1,-1\).
Then \(D_k>0\), and \(D_{k+l}\le D_k+D_l\): the array with \(k+l\) pairs is the sum of the array with the first \(k\) pairs followed by zeros and the array with zeros followed by the last \(l\) pairs, and \(N\) does not see zeros.

Fix \(n\ge1\), and put
\[
L=8(n+1),\qquad\varepsilon=\frac1{10n}.
\]
Let \(\mathcal S\), the numbers \(\alpha_s<\beta_s\), the arcs and the maps \(h_s\) be as in the lesson on reduced words.

**The landmarks.** Let \(\Lambda\) be the finite set of real numbers that consists of

- the points \(\alpha_s+j\) and \(\beta_s+j\) for the four letters \(s\) and the integers \(0\le j<L\);
- the points \(h_w(0)+j\) for all words \(w\) of a length of at most \(n\), the empty word included, and all integers \(-2n\le j\le L+2n\).

**The chain.** For every letter \(s\) let \(D_s=\{a\in\Lambda:h_s(a)\in\Lambda\}\) and \(T_s=h_s|_{D_s}\). These are order-preserving bijections \(D_s\to D_{s^{-1}}\) with \(T_{s^{-1}}=T_s^{-1}\). By the proposition on reversible transport there are a bound \(B\) and a finite stationary reversible marked chain on charts \(C\colon\Lambda\to\{1,\dots,B\}\), with edges \((C,s,C')\), whose letters are independent and uniform in \(\mathcal S\), and in which every edge is *good*,
\[
C'(a)=C(h_s(a))
\]
for all \(a\in\Lambda\) with \(h_s(a)\in\Lambda\), with a probability of at least \(1-\varepsilon\).

**The labels.** For an edge \((C,s,C')\) with a positive letter \(s\) put
\[
g(C,s,C')=\sum_{j=0}^{L-1}\bigl(b_{C(\alpha_s+j)}-b_{C(\beta_s+j)}\bigr),
\]
and for a negative letter \(s\) put \(g(C,s,C')=-g(C',s^{-1},C)\). So \(g\) is an odd labeling with values in \(c_{00}\). The label of an edge with a positive letter is read in the chart at its source; the label of an edge with a negative letter is read in the chart at its target.

Since a chart is strictly increasing, the positions
\[
\begin{aligned}
&C(\alpha_s)<C(\beta_s)<C(\alpha_s+1)\\
&\quad<C(\beta_s+1)<C(\alpha_s+2)<\dots
\end{aligned}
\]
are increasing, and the label has the entries \(1,-1,1,-1,\dots\) at them. By the spreading invariance,
\[
N(g(e))=D_L\qquad\text{for every edge }e .
\]

A label is a sum of differences \(b_{C(\alpha)}-b_{C(\beta)}\). The partial sums of such a difference are simple. For points \(\alpha<\beta\) and \(y\) of \(\Lambda\) and a chart \(C\), the sum of the entries of \(b_{C(\alpha)}-b_{C(\beta)}\) at the positions \(\le C(y)\) is
\[
\mathbf 1[\alpha\le y]-\mathbf 1[\beta\le y]=\mathbf 1_{[\alpha,\beta)}(y).
\]
We refer to this formula as (1.1).

## 2. Good steps

Let \((C_{i-1},s_i,C_i)\), \(i=1,\dots,n\), be successive edges of the chain, all of them good, and \(w=s_1\cdots s_n\). Suppose that the reduced form of \(w\) has the length \(\ell>0\), with \(n_+\) positive and \(n_-\) negative letters. Put
\[
m=\lfloor h_w(0)\rfloor,\qquad z=h_w(0)-m .
\]
Since \(h_w(0)\) is not an integer, \(0<z<1\); and \(|h_w(0)|<2n\) gives \(-2n\le m\le2n-1\).

We consider the starting points \(y_0=j\) and \(y_0=z+j\) for the integers \(j\) with \(\tfrac L4\le j\le\tfrac{3L}4\), and their backward orbits \(y_i=h_{s_i}^{-1}(y_{i-1})\).

**Lemma 2.1.** For each of these starting points and all \(0\le i\le n\):

1. \(y_i\in\Lambda\);
2. \(0<y_i<L\);
3. \(C_i(y_i)=C_0(y_0)\).

**Proof.** 1. For \(y_0=j\): \(y_i=h_{s_i^{-1}\cdots s_1^{-1}}(0)+j\), a point \(h_{w'}(0)+j\) with a word \(w'\) of the length \(i\le n\) and \(0\le j\le L\). For \(y_0=z+j=h_w(0)+j-m\): \(y_i=h_{s_{i+1}\cdots s_n}(0)+j-m\), with a word of the length \(n-i\) and \(-2n\le j-m\le L+2n\).

2. Every \(h_s^{-1}\) moves a point by less than \(2\), and \(j\le y_0<j+1\). So \(j-2n<y_i<j+1+2n\). With \(j\ge\tfrac L4=2n+2\) and \(j\le\tfrac{3L}4=6n+6\) this gives \(2<y_i<8n+7<L\).

3. Since \(h_{s_i}(y_i)=y_{i-1}\in\Lambda\) and the edge number \(i\) is good, \(C_i(y_i)=C_{i-1}(h_{s_i}(y_i))\), which is \(C_{i-1}(y_{i-1})\). \(\blacksquare\)

So the position \(C_0(y_0)\) is the position of the point \(y_i\) in the chart \(C_i\), for every \(i\): the charts follow the backward orbit. Put
\[
r_j=C_0(j),\qquad t_j=C_0(z+j)
\]
for \(\tfrac L4\le j\le\tfrac{3L}4\).
Since \(j<z+j<j+1\) and \(C_0\) is increasing, \(r_j<t_j<r_{j+1}\).

## 3. The partial sums of the total label

Let
\[
\begin{gathered}
G=\sum_{i=1}^ng(C_{i-1},s_i,C_i)\in c_{00},\\
F(k)=\sum_{a\le k}G_a\quad\text{for }0\le k\le B.
\end{gathered}
\]
Every label has the sum of its entries equal to \(0\), so \(F(0)=F(B)=0\).

**Lemma 3.1.** In the situation of Section 2, for each of the starting points \(y_0\),
\[
F\bigl(C_0(y_0)\bigr)=c_w(y_0).
\]
Consequently \(F(r_j)=-n_-\) and \(F(t_j)=n_+\) for all \(\tfrac L4\le j\le\tfrac{3L}4\).

**Proof.** Let \(k=C_0(y_0)\). We compute the sum of the entries at the positions \(\le k\) of the label number \(i\), and show that it is \(\chi_{s_i}(y_{i-1})\).

*A positive letter \(s_i\).* The label is read in the chart \(C_{i-1}\), and \(k=C_{i-1}(y_{i-1})\) by Lemma 2.1. By (1.1) the sum is \(\sum_{j'=0}^{L-1}\mathbf 1_{[\alpha_{s_i}+j',\beta_{s_i}+j')}(y_{i-1})\). Since \(0<y_{i-1}<L\), this is \(\mathbf 1_{\mathcal A_{s_i}}(y_{i-1})=\chi_{s_i}(y_{i-1})\).

*A negative letter \(s_i\).* The label is \(-g(C_i,s_i^{-1},C_{i-1})\), read in the chart \(C_i\), and \(k=C_i(y_i)\). In the same way, with \(0<y_i<L\), the sum is \(-\mathbf 1_{\mathcal A_{s_i^{-1}}}(y_i)\). By property 2 of the lemma on the homeomorphisms, \(y_i=h_{s_i}^{-1}(y_{i-1})\) lies in \(\mathcal A_{s_i^{-1}}\) if and only if \(y_{i-1}\notin\mathcal A_{s_i}\). So the sum is \(\mathbf 1_{\mathcal A_{s_i}}(y_{i-1})-1=\chi_{s_i}(y_{i-1})\).

Adding over \(i\) gives \(F(k)=c_w(y_0)\). The last statement is the lemma on the two levels, for the points \(j\) and \(z+j=h_w(0)+(j-m)\). \(\blacksquare\)

The vector \(G\) is the sum of all \(n\) labels; nothing is cancelled in it. The reduction of the word enters only through the numbers \(c_w(y_0)\), which do not change when \(w\) is reduced.

## 4. From two levels to the norm

**Lemma 4.1.** In the situation of Section 2,
\[
N(G)\ge\frac\ell6\,D_L .
\]

**Proof.** Write \(V=-n_-\) and \(U=n_+\), so that \(U-V=\ell\), and \(a=\tfrac L4\), \(b=\tfrac{3L}4\).

*Blocks.* Cut the positions \(1,\dots,B\) at
\[
r_a<t_a<r_{a+1}<\dots<t_{b-1}<r_b .
\]
By Lemma 3.1 the partial sums \(F\) at these cuts are \(V,U,V,U,\dots,U,V\), and \(F(0)=F(B)=0\). So the sums of the entries of \(G\) over the blocks between the cuts are
\[
V,\ \ \ell,\,-\ell,\ \ell,\,-\ell,\ \dots,\ \ell,\,-\ell,\ \ -V,
\]
with \(b-a=\tfrac L2\) pairs \(\ell,-\ell\). No block is empty; the last one is not, because \(r_b<t_b\le B\). By the contractive merging, \(N(G)\) is at least the norm of this array. The array is \(\ell\) times the array with \(\tfrac L2\) pairs \(1,-1\) between two zeros, plus the array \((V,0,\dots,0,-V)\). So
\[
\begin{aligned}
N(G)&\ge\ell\,D_{L/2}-|V|\,D_1\\
&\ge\ell\,(D_{L/2}-D_1),
\end{aligned}
\]
because \(|V|=n_-\le\ell\).

*One cut.* Cutting only at \(r_a\) gives the array \((V,-V)\), and cutting only at \(t_a\) gives \((U,-U)\). So \(N(G)\ge\max\{|V|,U\}\,D_1\ge\tfrac\ell2D_1\).

*Together.* For numbers \(A,A'\ge0\) we have \(\max\{A-A',A'/2\}\ge A/3\): if \(A'\le\tfrac23A\) the first number is at least \(A/3\), and otherwise the second. With \(A=\ell D_{L/2}\) and \(A'=\ell D_1\) this gives \(N(G)\ge\tfrac\ell3D_{L/2}\). Finally \(D_L\le2D_{L/2}\). \(\blacksquare\)

The first estimate uses all \(L\) oscillations between the two levels; it is good when \(D_{L/2}\) is large compared with \(D_1\). The second uses one oscillation; it covers the case that \(D_{L/2}\) is not larger than \(D_1\). In both cases the result is measured in units of \(D_L\), the norm of one label.

## 5. The walk and the theorem

**Theorem 5.1** (a walk with linear displacement; [OpenAI-M]). Let \(N\) be a spreading invariant norm on \(c_{00}\) with contractive merging. For every integer \(n\ge1\) there are a finite stationary reversible marked chain and an odd labeling \(g\) with values in \(c_{00}\) such that \(N(g(e))=1\) for every edge \(e\) and
\[
\Pr\Bigl(N\Bigl(\sum_{i=1}^ng(E_i)\Bigr)\ge\frac n{24}\Bigr)\ge\frac3{20}.
\]

This is Proposition 4.2 of the first lesson.

**Proof.** Take the chain and the labels of Section 1, and let \(E_i=(C_{i-1},s_i,C_i)\) be the first \(n\) edges of the chain.

*Good steps.* Each \(E_i\) fails to be good with a probability of at most \(\varepsilon\). So all \(n\) are good with a probability of at least \(1-n\varepsilon=\tfrac9{10}\).

*The word.* The letters \(s_1,\dots,s_n\) are independent and uniform in \(\mathcal S\). By the lemma on random words, \(\ell\ge\tfrac n4\) with a probability of at least \(\tfrac14\).

*Both.* With a probability of at least \(\tfrac14-\tfrac1{10}=\tfrac3{20}\), all steps are good and \(\ell\ge\tfrac n4\); then \(\ell>0\), and by Lemma 4.1
\[
N\Bigl(\sum_{i=1}^ng(E_i)\Bigr)\ge\frac\ell6\,D_L\ge\frac n{24}\,D_L .
\]
Every label has the norm \(D_L\). Dividing all labels by \(D_L\) gives the theorem. \(\blacksquare\)

**Theorem 5.2** ([OpenAI-M]). Assume the hypothesis (JE) of the first lesson. Every real Banach space that has Markov type \(p\) for some \(p>1\) is superreflexive.

**Proof.** In the first lesson the theorem was derived from the ordered norm and the walk with linear displacement. The first is Theorem 5.3 of the lesson on the spreading norm, the second is Theorem 5.1. \(\blacksquare\)

**The parts of the proof.** A space that is not superreflexive contains, in arbitrarily good finite approximation, sequences in which the order of the terms is visible in the norm: partial sums are controlled, zeros do not matter, merging does not increase the norm. On such sequences one can write vectors whose partial sums oscillate \(L\) times between two levels. The oscillation is produced by words in a free group acting on the line, and its size is the reduced length of the word. A random word has a reduced length proportional to its length. The chain of charts makes the words into the steps of a reversible stationary walk. So the walk reaches, in \(n\) steps of length \(1\), a distance proportional to \(n\); a space with Markov type \(p>1\) does not allow this.

**What is assumed.** The course proves the theorem from the hypothesis (JE), the theorem of James and Enflo that a space without an equivalent uniformly convex norm has a space finitely representable in it that is not reflexive. The Hahn–Banach theorem is taken from the core course on functional analysis, and Ramsey's theorem and the minimax theorem from an earlier course of the programme. Everything else is proved in the five lessons.

**What is not in the course.** The converse, that a superreflexive space has Markov type \(p\) for some \(p>1\), is quoted in the first lesson from [OpenAI-M] and not proved. The theorem is for real Banach spaces.

## 6. Exercises

**6.1.** Let \(N(a)=\max_j|a_1+\dots+a_j|\) (Exercise 5.5 of the first lesson). Compute \(D_k\), and say what Lemma 4.1 gives. Which of the two estimates in its proof is the better one here?

**6.2.** Let \(N(a)=\sum_i|a_i|\). Compute \(D_k\) and the two estimates of the proof of Lemma 4.1.

**6.3.** Check the inequalities \(2<y_i<8n+7\) of Lemma 2.1 for \(n=1\) and the two extreme values of \(j\).

**6.4.** Why is the label of an edge with a negative letter read in the chart at its target, and not at its source?

**6.5.** Let a space have Markov type \(p>1\) with the constant \(K\). Which bound for \(n\) follows from the two theorems of this lesson, and what is it for \(p=2\), \(K=1\)?

## 7. Solutions

**6.1.** The partial sums of \((1,-1,\dots)\) are \(1,0,1,0,\dots\): \(D_k=1\) for all \(k\). Lemma 4.1 gives \(N(G)\ge\ell/6\). The first estimate gives \(\ell(D_{L/2}-D_1)=0\), the second \(\tfrac\ell2\). In fact \(N(G)\ge\max\{|V|,U\}\ge\tfrac\ell2\) directly, since \(V\) and \(U\) are partial sums of \(G\).

**6.2.** \(D_k=2k\). The first estimate gives \(\ell(L-2)\), the second \(\ell\). The lemma gives \(\tfrac\ell6\cdot2L=\tfrac{\ell L}3\), which is smaller than \(\ell(L-2)\) for \(L\ge3\).

**6.3.** \(n=1\): \(L=16\), \(j\) from \(4\) to \(12\). The points \(y_i\) lie in \((j-2,j+3)\). For \(j=4\) this is \((2,7)\), for \(j=12\) it is \((10,15)\), and \(15=8n+7<16\).

**6.4.** The labeling must be odd: the label of \((C,s,C')\) is minus the label of the reverse edge \((C',s^{-1},C)\), whose letter is positive and whose source is \(C'\). In the proof this is what makes the term of a negative letter equal to \(\chi_{s_i}(y_{i-1})\): the point \(y_i\) is looked at in the chart \(C_i\), where it has the position \(C_0(y_0)\).

**6.5.** By the proof of the theorem in the first lesson, \(\tfrac3{20}(n/24)^p\le K^pn\), that is \(n^{p-1}\le\tfrac{20}3(24K)^p\). For \(p=2\), \(K=1\): \(n\le\tfrac{20}3\cdot576=3840\). So for \(n>3840\) the walk of Theorem 5.1 cannot exist in a space with these constants; a Hilbert space has no norm \(N\) of the kind of this lesson finitely represented in it.

## References

- [OpenAI-M] OpenAI, *Nontrivial Markov Type Forces Superreflexivity*, OpenAI Math Release preprint, 23 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026
