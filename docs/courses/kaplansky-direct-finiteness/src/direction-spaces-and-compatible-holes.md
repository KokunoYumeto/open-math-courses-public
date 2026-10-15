# Direction spaces and compatible holes

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The pairing of [Polynomial pairings on punctured spaces](polynomial-pairings-on-punctured-spaces.md) needs a family of full affine lines in \(Q^n\) that avoids a set \(O\) of holes, covers every other point exactly \(D=\ell+1\) times, and has incidence girth at least \(12\). Partitions of the space into parallel lines give regularity easily, but every partition has lines through the holes, and simply deleting them lowers the degree of other points as well. The construction instead arranges the lines through each hole in planar bundles: inside a plane through the hole, the \(q\) lines through the hole in all directions but one can be traded for the \(q-1\) parallel lines of the remaining direction that miss the hole. This trade removes the hole and changes no other degree. This lesson fixes the parameters and the direction spaces, describes the trade, and chooses the holes so that the trades are compatible. The next two lessons choose the remaining lines and prove the girth bound.

- The theorem and the parameters (Section 1).
- Direction spaces (Section 2).
- The local trade (Section 3).
- Choosing compatible holes (Section 4).

## 1. The theorem and the parameters

Let \(q=2^h\) with \(h\ge2\), and let \(\ell\) be the least prime with \(\ell\equiv-1\pmod{q^{100}}\). It exists by Dirichlet's theorem, and its size is controlled by the following theorem, which is not proved in the programme.

**(LIN)** (Linnik's theorem; [Linnik 1944]; [Xylouris, abstract]). There are absolute constants \(c,L>0\) such that for all coprime natural numbers \(a\) and \(k\) there is a prime \(p\equiv a\pmod k\) with \(p\le c\,k^L\).

Put
\[
\begin{gathered}
D=\ell+1,\quad s=\lfloor\log_qD\rfloor,\\
b=s+20,\quad n=10b,\quad N_{\rm pt}=q^n .
\end{gathered}
\]
Then \(q^{100}\) divides \(D\), so \(D\ge q^{100}\) and \(s\ge100\), and
\[
q^s\le D<q^{s+1}. \tag{1.1}
\]
By (LIN) with \(a=q^{100}-1\) and \(k=q^{100}\), \(D\le c\,q^{100L}+1\le(c+1)q^{100L}\), so
\[
\begin{aligned}
s&\le100L+\log_q(c+1)\\
&\le100L+\log_2(c+1) .
\end{aligned}
\]
So \(s\), \(b\) and \(n\) are bounded independently of \(h\). In this lesson and the next two, asymptotic statements refer to \(h\to\infty\); the constants implicit in \(O(\cdot)\) may depend on this fixed bound for \(s\), but not on \(h\). This is the only use of (LIN): without a bound on \(s\), the dimension \(n\) could grow with \(q\), and the estimates below would fail.

Let \(Q\) be a field with \(q\) elements, with an enumeration \(a_0,\ldots,a_{q-1}\), and \(\mathcal A=Q^n\). Put \(d_0=(q-2)/2\) and
\[
S=\Bigl\{(a_{k_1},\ldots,a_{k_n}):\sum_ik_i\le d_0\Bigr\}\subseteq\mathcal A ,
\]
the index simplex of [Polynomial pairings on punctured spaces](polynomial-pairings-on-punctured-spaces.md). An *affine line* is a translate of a one-dimensional \(Q\)-subspace, a *direction* is a one-dimensional subspace, and a *plane* is a translate of a two-dimensional subspace.

**Theorem 1.1** ([OpenAI-DF2, Theorem 5.1]). For all sufficiently large \(h\), for every field \(Q\) with \(q=2^h\) elements and every enumeration of \(Q\), there are a set \(O\subseteq S\) and a set \(\mathcal F\) of affine lines contained in \(V=\mathcal A\setminus O\) such that
\[
\frac{2N_{\rm pt}}{D^2}\le|O|\le\frac{7N_{\rm pt}}{D^2},
\]
every point of \(V\) lies on exactly \(D\) lines of \(\mathcal F\), and the incidence graph of \(V\) and \(\mathcal F\) has girth at least \(12\).

The proof occupies this lesson, [Random slabs and the local lemma](random-slabs-and-the-local-lemma.md) and [Line partitions, girth and the counterexample](line-partitions-girth-and-the-counterexample.md).

## 2. Direction spaces

Divide the index set \(\{1,\ldots,D\}\) into \(D/q\) *bundles* of \(q\) indices each; this is possible because \(q\) divides \(D\). Write \(\rho(j)\) for the bundle of the index \(j\).

**Lemma 2.1** (direction spaces; [OpenAI-DF2, Lemma 5.2]). There are two-dimensional subspaces \(W_r\subseteq\mathcal A\), one for each bundle \(r\), and \((b-1)\)-dimensional subspaces \(E_j\subseteq\mathcal A\), one for each index \(j\), such that any at most ten distinct members of this list form a direct sum.

*Proof.* A field \(Q'\) with \(q^b\) elements exists and contains a subfield with \(q\) elements, which is isomorphic to \(Q\) ([Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40): Judson, Theorems 22.6 and 22.7); so \(Q'\) is a \(Q\)-vector space of dimension \(b\), and \(\mathcal A=Q^{10b}\) can be identified with \((Q')^{10}\) as a \(Q\)-vector space. For distinct \(\xi\in Q'\), the vectors \(\nu(\xi)=(1,\xi,\xi^2,\ldots,\xi^9)\) have the property that any \(k\le10\) of them are linearly independent over \(Q'\): their first \(k\) coordinates form an invertible Vandermonde matrix. We need \(D/q+D\) distinct parameters, and \(D/q+D<q^{s+2}\le q^b\) by (1.1). Give each \(W_r\) and each \(E_j\) its own parameter \(\xi\), and choose it as a \(Q\)-subspace of the prescribed dimension, \(2\) or \(b-1\), of the one-dimensional \(Q'\)-subspace \(Q'\nu(\xi)\), which has \(Q\)-dimension \(b\ge2\). Distinct members lie in distinct lines \(Q'\nu(\xi)\); at most ten of these lines form a direct sum over \(Q'\), hence over \(Q\), and so do any subspaces of them. \(\square\)

Fix these spaces. In each plane \(W_r\), choose one direction \(e_r\); the other \(q\) directions of \(W_r\) are assigned bijectively to the \(q\) indices of the bundle \(r\), and the direction assigned to \(j\) is called \(d_j\). Put
\[
U_j=d_j\oplus E_j ,
\]
a subspace of dimension \(b\).

**Lemma 2.2.** For indices \(j\ne j'\) and bundles \(r\),
\[
\begin{gathered}
U_j\cap U_{j'}=0,\qquad U_j\cap e_r=0,\\
U_j\cap W_r=\begin{cases}d_j,&r=\rho(j),\\0,&r\ne\rho(j).\end{cases}
\end{gathered}
\]
Moreover \(U_j+U_{j'}\), \(U_j+e_r\) and \(e_r+e_{r'}\) (\(r\ne r'\)) are direct sums.

*Proof.* Consider a relation \(d+e=d'+e'\) with \(d\in d_j\), \(e\in E_j\), \(d'\in d_{j'}\), \(e'\in E_{j'}\). It involves at most four spaces of the list, \(E_j\), \(E_{j'}\), \(W_{\rho(j)}\), \(W_{\rho(j')}\), which form a direct sum. So \(e=e'=0\), and \(d=d'\). If \(\rho(j)\ne\rho(j')\), the components in different planes vanish; if \(\rho(j)=\rho(j')\), then \(d\) and \(d'\) lie in the two distinct directions \(d_j\ne d_{j'}\) of one plane, so again \(d=d'=0\). The other statements follow in the same way: within the plane \(W_{\rho(j)}\), the directions \(d_j\) and \(e_{\rho(j)}\) are distinct, and different planes and the spaces \(E_j\) are independent. \(\square\)

The partitions used later have, for each index \(j\), lines with directions in \(U_j\); the line through a hole \(o\) in partition \(j\) will be \(o+d_j\). The spaces \(E_j\) supply the other directions.

## 3. The local trade

Let \(o\) be a point and \(r\) a bundle. The plane \(o+W_r\) contains the \(q\) lines \(o+d_j\), \(\rho(j)=r\), through \(o\) (the *fan*), and the \(q\) lines of direction \(e_r\), one of which, \(o+e_r\), passes through \(o\).

**Lemma 3.1** (the local trade). Remove from a family of lines the fan of \(o\) in \(o+W_r\), and insert the \(q-1\) lines of direction \(e_r\) in \(o+W_r\) other than \(o+e_r\). Then each point of \(o+W_r\) not on \(o+e_r\) loses one incidence and gains one, the point \(o\) loses \(q\) incidences, the other points of \(o+e_r\) lose and gain none, and points outside \(o+W_r\) are unaffected.

*Proof.* The fan uses every direction of \(W_r\) except \(e_r\), so each point \(y\ne o\) of the plane lies on exactly one fan line if \(y-o\notin e_r\), and on none otherwise; \(o\) lies on all \(q\). The inserted lines partition the points of the plane off \(o+e_r\). \(\square\)

So the trade removes the hole from all lines of the bundle without changing any other degree. The holes and the remaining lines must be chosen so that all these trades can be carried out together and create no short cycles; the holes are chosen now.

## 4. Choosing compatible holes

Lines from two different bundles could form a rectangle. An *exceptional rectangle* has corners \(x\), \(x+u\), \(x+u+v\), \(x+v\) with \(0\ne u\in e_r\), \(0\ne v\in e_{r'}\) and \(r\ne r'\). Each of its four sides lies on an affine line; for a side of direction \(e_r\), a *witness* is a point of the plane through that side parallel to \(W_r\) that is not on the side's line, and similarly for \(e_{r'}\). If a side is a line inserted by a trade, the hole of that trade is a witness.

**Lemma 4.1** (compatible holes; [OpenAI-DF2, Lemma 5.3]). For all sufficiently large \(h\) there is a set \(O\subseteq S\) with
\[
\frac{2N_{\rm pt}}{D^2}\le|O|\le\frac{7N_{\rm pt}}{D^2}
\]
and the following properties.

1. Every translate of every \(W_r\) contains at most one point of \(O\).
2. For every index \(j\), every coset \(C\) of \(U_j\) and every bundle \(r\), \(|O\cap(C+W_r)|\le100\).
3. No exceptional rectangle has four distinct witnesses in \(O\), one for each side.

*Proof.* Put \(M=N_{\rm pt}/D^2\). Counting index tuples, \(|S|=\binom{d_0+n}{n}\ge d_0^n/n!\). For \(q\ge6\), \(d_0\ge q/3\), so \(|S|\ge c_SN_{\rm pt}\) with \(c_S=1/(3^nn!)\), a positive constant because \(n\) is bounded. Choose each point of \(S\) independently with probability \(\theta=5M/|S|\), and let \(X\) be the set of chosen points. Then \(\theta\le5/(c_SD^2)\), so \(\theta=O(D^{-2})\) and \(\theta\le1\) for large \(h\).

*Size.* \(\mathbb E|X|=5M\) and \(\operatorname{Var}|X|=|S|\theta(1-\theta)\le5M\). Since \(D<q^{s+1}\), \(M>q^{n-2s-2}=q^{8s+198}\to\infty\). By Chebyshev's inequality ([Probability](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B90): Grinstead–Snell, *Introduction to Probability*, Theorem 8.1),
\[
\Pr\bigl(\bigl||X|-5M\bigr|\ge M\bigr)\le\frac{5M}{M^2}\to0 .
\]

*Occupancy.* There are at most \(D\cdot(D/q)\cdot N_{\rm pt}\le D^2N_{\rm pt}\) triples \((j,r,C)\), and each set \(C+W_r\) has at most \(q^{b+2}\) points. The probability that a given set of at most \(q^{b+2}\) points contains \(100\) chosen points is at most \(\binom{q^{b+2}}{100}\theta^{100}\le(\theta q^{b+2})^{100}\). Since \(\theta=O(q^{-2s})\) and \(q^{b+2}=q^{s+22}\), the probability that some \(C+W_r\) contains more than \(100\) chosen points is at most
\[
\begin{aligned}
&D^2N_{\rm pt}\,(\theta q^{b+2})^{100}\\
&\quad=O\bigl(q^{12s+202}\,q^{100(22-s)}\bigr)\\
&\quad=O\bigl(q^{2402-88s}\bigr),
\end{aligned}
\]
which tends to zero because \(s\ge100\).

*Collisions and rectangles.* Mark every chosen point that, together with another chosen point, lies in one translate of some \(W_r\), and every chosen point that belongs to four distinct chosen witnesses of one exceptional rectangle. The expected number of pairs of distinct chosen points in a common translate of some \(W_r\) is at most \((D/q)\cdot N_{\rm pt}q^2\cdot\theta^2\). The rectangle data \((x,r,r',u,v)\) number at most \(N_{\rm pt}(D/q)^2(q-1)^2\le N_{\rm pt}D^2\), each rectangle has fewer than \(q^8\) quadruples of witnesses, and a quadruple of distinct points is chosen with probability at most \(\theta^4\) (zero if a point lies outside \(S\)). So the number \(Z\) of marked points has \(\mathbb EZ\le2N_{\rm pt}(D/q)q^2\theta^2+4N_{\rm pt}D^2q^8\theta^4\), and since \(M=N_{\rm pt}/D^2\),
\[
\begin{aligned}
\frac{\mathbb EZ}M&\le2D^3q\,\theta^2+4D^4q^8\theta^4\\
&=O\Bigl(\frac qD+\frac{q^8}{D^4}\Bigr),
\end{aligned}
\]
which tends to zero since \(D\ge q^{100}\). Since \(Z\ge0\), \(\mathbb EZ\ge M\Pr(Z>M)\) (Markov's inequality), so \(\Pr(Z>M)\to0\).

For large \(h\), some outcome has \(4M\le|X|\le6M\), no set \(C+W_r\) with more than \(100\) chosen points, and \(Z\le M\). Delete the marked points and let \(O\) be the rest. Then \(3M\le|O|\le6M\), which gives the size bounds; deletion keeps property 2; every pair in property 1 and every quadruple in property 3 consists of marked points, so properties 1 and 3 hold for \(O\). \(\square\)

Fix such a set \(O\) and put \(T_r=\bigcup_{o\in O}(o+W_r)\). The *replacement lines of label \(R_r\)* are the lines of direction \(e_r\) in the planes \(o+W_r\), \(o\in O\), other than \(o+e_r\).

**Lemma 4.2** (replacement lines; [OpenAI-DF2, Lemma 5.4]). The replacement lines avoid \(O\), the replacement lines of one label are pairwise disjoint, and no exceptional rectangle has all four sides on replacement lines.

*Proof.* By property 1, distinct holes lie in disjoint translates of \(W_r\), and each such plane contains one hole; the replacement lines of label \(R_r\) in one plane are parallel and miss its hole. This gives the first two statements.

Suppose an exceptional rectangle, with sides of directions \(e_r\) and \(e_{r'}\), has its four sides on replacement lines. The hole of the trade that produced each side is a witness for that side. The two sides of direction \(e_r\) lie in translates of \(W_r\) that differ by the nonzero vector \(v\in e_{r'}\), which is not in \(W_r\) by Lemma 2.1; so these planes are disjoint, and their witnesses differ. The planes of two adjacent sides, of directions \(e_r\) and \(e_{r'}\), meet only in the common corner, because \(W_r\cap W_{r'}=0\); the corner lies on both sides, so it is neither witness. So the four witnesses are distinct holes, contradicting property 3. \(\square\)

## 5. Exercises

**5.1** (easy). Show that a two-dimensional \(Q\)-space has exactly \(q+1\) directions, and that the fan of Lemma 3.1 together with the line \(o+e_r\) covers the plane \(o+W_r\), meeting only at \(o\).

**5.2** (easy). Check the exponent \(12s+202+100(22-s)=2402-88s\) and that it is negative for \(s\ge100\).

**5.3** (medium). Show that \(\binom{d_0+n}{n}\ge d_0^n/n!\), and that \(d_0=(q-2)/2\ge q/3\) for \(q\ge6\).

**5.4** (medium). Explain why the bound \(D/q+D<q^{s+2}\le q^b\) suffices in Lemma 2.1, and why ten Vandermonde vectors are needed: a short polygon in the next lesson has at most five steps, and each step involves at most two of the spaces \(W_r\), \(E_j\).

## 6. Solutions

**5.1.** The nonzero vectors of a two-dimensional space number \(q^2-1\), and each direction contains \(q-1\) of them, giving \((q^2-1)/(q-1)=q+1\) directions. Each point \(y\ne o\) of the plane lies on the unique line \(o+Q(y-o)\), which is a fan line or \(o+e_r\); distinct lines through \(o\) meet only at \(o\).

**5.2.** \(12s+202+2200-100s=2402-88s\), and \(88\cdot100=8800>2402\).

**5.3.** \(\binom{d_0+n}{n}=\prod_{i=1}^n\frac{d_0+i}{i}\ge\prod_{i=1}^n\frac{d_0}{i}=\frac{d_0^n}{n!}\). And \((q-2)/2\ge q/3\) is equivalent to \(q\ge6\).

**5.4.** One parameter is needed for each of the \(D/q\) planes and \(D\) spaces \(E_j\), and \(Q'\) has \(q^b\) elements; \(D/q+D<2D<2q^{s+1}\le q^{s+2}\). A polygon with at most five steps, each in a space \(U_j=d_j\oplus E_j\subseteq W_{\rho(j)}\oplus E_j\) or a direction \(e_r\subseteq W_r\), involves at most \(2\cdot5=10\) members of the list, and its closure equation is then decided componentwise.

## References

- [OpenAI-DF2] OpenAI, *A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two*, OpenAI Math Release preprint, 23 September 2026, Sections 5.1 and 5.2 (Theorem 5.1, Lemmas 5.2 to 5.4). https://github.com/openai/math/tree/main/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026
- [Linnik 1944] U. V. Linnik, *On the least prime in an arithmetic progression. I. The basic theorem*, Recueil Mathématique (Matematicheskii Sbornik), Nouvelle série 15(57) (1944), 139–178; free on Math-Net.Ru. https://www.mathnet.ru/eng/sm6196
- [Xylouris] T. Xylouris, *On Linnik's constant*, arXiv:0906.2749 (2009). https://arxiv.org/abs/0906.2749
