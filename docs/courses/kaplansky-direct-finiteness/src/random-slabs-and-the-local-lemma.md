# Random slabs and the local lemma

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

With the holes fixed in [Direction spaces and compatible holes](direction-spaces-and-compatible-holes.md), the rest of the space must be covered by lines, once in each of \(D\) partitions, without creating cycles of length less than \(12\) in the incidence graph. Such a cycle is a closed polygon with at most five sides. This lesson chooses, for each index \(j\) and each coset of the space \(U_j\), a random two-dimensional subspace of \(E_j\); the lines of partition \(j\) will lie in the three-dimensional *slabs* it determines. A short polygon can only close up if its steps happen to lie in the chosen slabs, which is unlikely, and a classification of the possible polygons bounds the probabilities. The Lovász local lemma then shows that all bad events can be avoided at once.

- Random slabs (Section 1).
- The bad events (Section 2).
- Short polygons (Section 3).
- Event bounds (Section 4).
- The local lemma (Section 5).

Notation is that of [Direction spaces and compatible holes](direction-spaces-and-compatible-holes.md): \(q=2^h\), \(D=\ell+1\), \(s\), \(b=s+20\), \(n=10b\), the planes \(W_r\) with directions \(e_r\), the directions \(d_j\), the spaces \(E_j\) and \(U_j=d_j\oplus E_j\), the holes \(O\) with properties 1 to 3 of Lemma 4.1, and \(T_r=\bigcup_{o\in O}(o+W_r)\). For \(u\in U_j\) write \(u^{(E_j)}\) for its component in \(E_j\).

## 1. Random slabs

Independently for each index \(j\) and each coset \(C\) of \(U_j\) in \(\mathcal A\), choose a two-dimensional subspace \(P_{j,C}\subseteq E_j\) uniformly at random. The translates of \(d_j\oplus P_{j,C}\) contained in \(C\) partition \(C\) into three-dimensional affine *slabs*. Two points \(x,y\in C\) lie in the same slab exactly when \((y-x)^{(E_j)}\in P_{j,C}\).

**Lemma 1.1.** A fixed nonzero vector of \(E_j\) lies in \(P_{j,C}\) with probability
\[
p_*=\frac{q^2-1}{q^{b-1}-1}\le2q^{3-b} .
\]

*Proof.* Count the pairs \((y,P)\) of a nonzero vector \(y\) and a two-dimensional subspace \(P\ni y\) of \(E_j\). Each \(P\) contains \(q^2-1\) nonzero vectors. The invertible linear maps of \(E_j\) act transitively on nonzero vectors and permute the two-dimensional subspaces, so every nonzero vector lies in the same number of subspaces \(P\). Hence this number is \((q^2-1)/(q^{b-1}-1)\) times the number of all \(P\), which is the probability. Finally \(q^{b-1}-1\ge q^{b-1}/2\). \(\square\)

## 2. The bad events

The bad events are defined before any line is chosen.

*Hole pairs.* For each coset \(C\) of some \(U_j\) and each pair of distinct holes \(o,o'\in C\), the event that they lie in the same slab. Their difference \(u=o'-o\in U_j\) has \(u^{(E_j)}\ne0\): otherwise \(u\in d_j\subseteq W_{\rho(j)}\), and the two holes would lie in one translate of \(W_{\rho(j)}\), contradicting property 1. So the event is \(u^{(E_j)}\in P_{j,C}\), of probability \(p_*\).

*Candidate polygons.* A *candidate polygon* is a closed sequence of \(k\in\{3,4,5\}\) nonzero steps \(x_0\to x_1\to\cdots\to x_k=x_0\) in \(\mathcal A\), each step labelled by a type:

- a *generic* step of label \(G_j\): \(x_{i+1}-x_i\in U_j\) with nonzero \(E_j\)-component;
- a *replacement* step of label \(R_r\): \(x_{i+1}-x_i\in e_r\setminus\{0\}\), with both endpoints in \(T_r\).

At least one step is generic, and cyclically adjacent steps have different labels; repeated vertices are allowed. The event of a candidate polygon is that every generic step, of label \(G_j\), has its \(E_j\)-component in \(P_{j,C}\), where \(C\) is the coset of \(U_j\) containing that step. All choices are finite, so the list of events is finite.

A replacement step need not lie on an actual replacement line; the condition on its endpoints only makes the list longer, which does no harm. The three properties of the holes have separate roles: property 1 makes each hole-pair event test a nonzero vector, property 2 bounds the number of holes that enter the counts of Section 4, and property 3 was used in Lemma 4.2 of the previous lesson to exclude rectangles made only of replacement lines.

## 3. Short polygons

**Lemma 3.1** (classification; [OpenAI-DF2, Lemma 5.5]). Every candidate polygon has one of the following forms.

1. A rectangle with labels \(G_j,R_r,G_j,R_r\), opposite steps being opposite vectors.
2. A rectangle with labels \(G_j,G_{j'},G_j,G_{j'}\), \(j\ne j'\), opposite steps being opposite vectors.
3. A pentagon with two steps of label \(G_j\), two of label \(G_{j'}\), \(j\ne j'\), and one of label \(R_r\), where \(\rho(j)=\rho(j')=r\).

If \(g\in\{1,2\}\) is the number of distinct generic labels, the event uses \(2g\) distinct slab variables \(P_{j,C}\) and has probability \(p_*^{2g}\). In case 3, the replacement vector and one vector of each generic label determine the other two vectors, once the order of the steps is fixed.

*Proof.* Each step lies in a space of the form \(W_{\rho(j)}\oplus E_j\) or in a plane \(W_r\), so it involves at most two members of the list of Lemma 2.1 of the previous lesson, and a polygon with \(k\le5\) steps involves at most ten. These form a direct sum, so the closure equation \(\sum_i(x_{i+1}-x_i)=0\) holds componentwise.

The \(E_j\)-component of the sum comes only from the steps of label \(G_j\), each contributing a nonzero vector; so each generic label occurs at least twice. A label occurring three times in a cyclic sequence of at most five steps would occupy two adjacent positions, so each label occurs at most twice. Hence each generic label occurs exactly twice, and \(g\in\{1,2\}\).

If \(g=1\), with label \(G_j\): in the plane \(W_{\rho(j)}\) the components lie in the two distinct directions \(d_j\) and \(e_{\rho(j)}\), and other planes \(W_r\) receive only replacement steps of label \(R_r\). Componentwise closure forces the replacement vectors of each label to sum to zero, so each replacement label occurring at all occurs twice. With \(k\le5\) this leaves \(k=4\), labels alternating \(G_j,R_r,G_j,R_r\), and since \(U_j+e_r\) is direct, closure gives opposite vectors in opposite positions: case 1.

If \(g=2\) and \(k=4\), the labels alternate, and since \(U_j+U_{j'}\) is direct, opposite vectors are paired: case 2. If \(g=2\) and \(k=5\), there is one replacement step, of label \(R_r\), and its nonzero vector in \(e_r\) must be cancelled in the plane \(W_r\) by components of the generic steps. These components lie in \(d_j\) if \(\rho(j)=r\) and in \(d_{j'}\) if \(\rho(j')=r\). If neither label is in bundle \(r\), nothing cancels; if only one is, two vectors in the distinct directions \(e_r\) and \(d_j\) cannot cancel. So \(\rho(j)=\rho(j')=r\): case 3. Given the replacement vector and one vector of each generic label, closure prescribes the sum of the remaining vector in \(U_j\) and the remaining vector in \(U_{j'}\), and these are unique because \(U_j+U_{j'}\) is direct.

For the probability: between the two steps of label \(G_j\), in one cyclic direction there is exactly one other step. Its vector \(v\) is nonzero and lies in \(U_{j'}\) or in some \(e_r\), so \(v\notin U_j\) by Lemma 2.2 of the previous lesson. If the first \(G_j\) step starts at \(x\) with vector \(u\in U_j\), the second starts at \(x+u+v\notin x+U_j\). So the two steps lie in different cosets of \(U_j\) and use different variables; variables of different labels are different too. The \(2g\) variables are independent, and each condition has probability \(p_*\) by Lemma 1.1, because each tested \(E_j\)-component is a fixed nonzero vector. \(\square\)

## 4. Event bounds

For a slab variable \(P_{j,C}\), let \(\mu(P_{j,C})\) be the sum of the probabilities of the bad events that use it, and \(\mu\) the largest of these sums.

**Lemma 4.1** (event bounds; [OpenAI-DF2, Lemma 5.6]). Every bad event uses at most four variables, and \(\mu=O(q^{-7})\).

*Proof.* A hole-pair event uses one variable, and a polygon event \(2g\le4\). Fix \(P_{j,C}\).

*Hole pairs.* Since \(C\subseteq C+W_r\), property 2 gives at most \(100\) holes in \(C\), so the hole-pair events contribute at most \(100^2p_*\).

For polygons, rotate the cyclic sequence so that it starts with a generic step of label \(G_j\) in \(C\); rotations and orders of at most five labels change the counts below by an absolute constant factor.

*Rectangles of case 2.* Choose the other label \(j'\) (at most \(D\) ways), the starting point in \(C\) (\(q^b\) ways) and one vector of each label (at most \(q^{2b}\) ways); closure determines the rest. The contribution is \(O(Dq^{3b}p_*^4)\).

*Rectangles of case 1.* Both endpoints of the first step lie in \(C\cap T_r\). A hole \(o\) contributes to this set only if \(o\in C+W_r\), which allows at most \(100\) holes, and each nonempty \(C\cap(o+W_r)\) is a coset of \(U_j\cap W_r\), with \(q\) points if \(r=\rho(j)\) and one point otherwise (Lemma 2.2 of the previous lesson). Choosing the two endpoints and the replacement vector (at most \(q\) ways) gives at most \(100^2q^3\) rectangles for \(r=\rho(j)\) and \(100^2q\) for each of the other \(D/q\) bundles, in total \(O(100^2(q^3+D))\) rectangles, contributing \(O\bigl((q^3+D)p_*^2\bigr)\). This counts also choices that fail the conditions, which only increases the bound.

*Pentagons of case 3.* The other label lies in the bundle \(\rho(j)\), at most \(q\) choices. Choose the starting point in \(C\), one vector of each generic label and the replacement vector: at most \(q\cdot q^b\cdot q^{2b}\cdot q\) choices, the rest being determined by Lemma 3.1. The contribution is \(O(q^{3b+2}p_*^4)\).

With \(p_*\le2q^{3-b}\), \(b=s+20\) and \(q^s\le D<q^{s+1}\),
\[
\begin{aligned}
\mu&\le100^2p_*+O\bigl(Dq^{3b}p_*^4\bigr)\\
&\quad+O\bigl((D+q^3)p_*^2+q^{3b+2}p_*^4\bigr)\\
&=O\bigl(q^{-s-17}+q^{-7}+q^{-s-33}\\
&\qquad+q^{-2s-31}+q^{-s-6}\bigr)\\
&=O(q^{-7}),
\end{aligned}
\]
with constants that do not depend on the variable. \(\square\)

## 5. The local lemma

**Lemma 5.1** (a special case of the local lemma; [OpenAI-DF2, Lemma 5.7]; [Erdős–Lovász]). Let a finite list of events be determined by independent random variables, each event by a nonempty set of at most four of them. If, for every variable, the probabilities of the events using it add up to at most \(1/16\), then with positive probability no event occurs.

*Proof.* Call two distinct events *neighbours* if their sets of variables meet, and write \(\mathcal N(A)\) for the set of neighbours of \(A\). An event is independent of the family of all its non-neighbours jointly, since they are determined by disjoint sets of independent variables. Put \(x_A=2\Pr(A)\). Each event uses some variable, so \(\Pr(A)\le1/16\) and \(x_A\le1/8\). Summing over the at most four variables of \(A\),
\[
\sum_{B\in\mathcal N(A)}x_B\le4\cdot2\cdot\frac1{16}=\frac12 ,
\]
and since \(\prod(1-y_i)\ge1-\sum y_i\) for \(y_i\in[0,1]\),
\[
\begin{aligned}
&\Pr(A)=\frac{x_A}2\\
&\le x_A\prod_{B\in\mathcal N(A)}(1-x_B).
\end{aligned}\tag{5.1}
\]

We show by induction on \(|\mathcal S|\) that for every event \(A\) and every set \(\mathcal S\) of events not containing \(A\), the event \(\bigcap_{B\in\mathcal S}B^c\) has positive probability and
\[
\Pr\Bigl(A\Bigm|\bigcap_{B\in\mathcal S}B^c\Bigr)\le x_A .
\]
For \(\mathcal S=\emptyset\) this is (5.1). Otherwise, write \(\mathcal S_1\) for the neighbours of \(A\) in \(\mathcal S\), \(\mathcal S_2\) for the rest, and \(D_i=\bigcap_{B\in\mathcal S_i}B^c\). Listing \(\mathcal S=\{B_1,\ldots,B_k\}\), the chain rule gives \(\Pr(D_1\cap D_2)=\prod_i\bigl(1-\Pr(B_i\mid\bigcap_{i'<i}B_{i'}^c)\bigr)\ge\prod_i(1-x_{B_i})>0\) by the induction hypothesis for smaller sets. If \(\mathcal S_1=\emptyset\), independence gives \(\Pr(A\mid D_2)=\Pr(A)\le x_A\). Otherwise
\[
\begin{aligned}
&\Pr(A\mid D_1\cap D_2)\\
&\quad\le\frac{\Pr(A\cap D_2)/\Pr(D_2)}{\Pr(D_1\mid D_2)}\\
&\quad=\frac{\Pr(A)}{\Pr(D_1\mid D_2)} ,
\end{aligned}
\]
using independence of \(A\) from \(D_2\). The chain rule over \(\mathcal S_1\), with the induction hypothesis for the smaller conditioning sets, gives \(\Pr(D_1\mid D_2)\ge\prod_{B\in\mathcal S_1}(1-x_B)\ge\prod_{B\in\mathcal N(A)}(1-x_B)\), and (5.1) gives the bound \(x_A\). Finally, for the whole list \(A_1,\ldots,A_N\),
\[
\begin{aligned}
&\Pr\Bigl(\bigcap_iA_i^c\Bigr)\\
&\quad=\prod_i\Bigl(1-\Pr\bigl(A_i\bigm|\textstyle\bigcap_{i'<i}A_{i'}^c\bigr)\Bigr)\\
&\quad\ge\prod_i(1-x_{A_i})>0 .\qquad\square
\end{aligned}
\]

**Corollary 5.2.** For all sufficiently large \(h\), the subspaces \(P_{j,C}\) can be chosen so that every slab contains at most one hole and no candidate polygon event occurs.

*Proof.* By Lemma 4.1, \(\mu=O(q^{-7})\le1/16\) for large \(h\), and every event uses at most four variables; Lemma 5.1 applies. \(\square\)

The general form of the local lemma with weights \(x_A\) is due to Erdős and Lovász and was developed further by many authors; Moser and Tardos gave an algorithmic proof [Moser–Tardos]. Only the existence of a good choice is needed here.

## 6. Exercises

**6.1** (easy). Show that the number of two-dimensional subspaces of a \(d\)-dimensional \(Q\)-space is \(\frac{(q^d-1)(q^d-q)}{(q^2-1)(q^2-q)}\), and recover \(p_*\) for \(d=b-1\) by counting directly.

**6.2** (easy). Check the five exponents in the proof of Lemma 4.1.

**6.3** (medium). Show that a candidate polygon cannot have \(k=3\).

**6.4** (medium). In Lemma 5.1, show that the hypothesis can be weakened to: each event uses at most \(a\) variables and the sums are at most \(1/(4a)\).

## 7. Solutions

**6.1.** An ordered basis of a two-dimensional subspace is a pair \((y_1,y_2)\) with \(y_1\ne0\) and \(y_2\notin Qy_1\): \((q^d-1)(q^d-q)\) pairs, and each subspace has \((q^2-1)(q^2-q)\) ordered bases. The subspaces containing a fixed \(y\ne0\) correspond to the directions of \(Q^d/Qy\), of which there are \((q^{d-1}-1)/(q-1)\). The quotient of the two counts is \(\frac{(q^{d-1}-1)(q^2-1)(q^2-q)}{(q-1)(q^d-1)(q^d-q)}=\frac{q^2-1}{q^d-1}\), which is \(p_*\) for \(d=b-1\).

**6.2.** Using \(p_*\le2q^{3-b}\), \(D<q^{s+1}\) and \(b=s+20\): \(p_*=O(q^{3-b})=O(q^{-s-17})\); \(Dq^{3b}p_*^4=O(q^{s+1+3b+12-4b})=O(q^{s+13-b})=O(q^{-7})\); \(Dp_*^2=O(q^{s+1+6-2b})=O(q^{-s-33})\); \(q^3p_*^2=O(q^{9-2b})=O(q^{-2s-31})\); \(q^{3b+2}p_*^4=O(q^{14-b})=O(q^{-s-6})\).

**6.3.** Each generic label occurs exactly twice and its two occurrences are not adjacent; in a cycle of three steps any two positions are adjacent.

**6.4.** With \(x_A=2\Pr(A)\), the sum over neighbours is at most \(a\cdot2\cdot\frac1{4a}=\frac12\), and each \(x_A\le\frac1{2a}<1\); the proof is unchanged.

## References

- [OpenAI-DF2] OpenAI, *A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two*, OpenAI Math Release preprint, 23 September 2026, Sections 5.3 and 5.4 (Lemmas 5.5 to 5.7). https://github.com/openai/math/tree/main/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026
- [Erdős–Lovász] P. Erdős and L. Lovász, *Problems and results on 3-chromatic hypergraphs and some related questions*, in: Infinite and Finite Sets, Vol. II, Colloquia Mathematica Societatis János Bolyai 10, North-Holland, 1975, 609–627; free on the Erdős papers page of the Rényi Institute. https://www.renyi.hu/~p_erdos/1975-34.pdf
- [Moser–Tardos] R. A. Moser and G. Tardos, *A constructive proof of the general Lovász Local Lemma*, arXiv:0903.0544 (2009). https://arxiv.org/abs/0903.0544
