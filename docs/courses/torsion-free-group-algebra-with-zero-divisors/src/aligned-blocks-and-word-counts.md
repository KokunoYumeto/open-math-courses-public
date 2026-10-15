# Aligned blocks and word counts

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson continues the proof of the bounded-pattern estimate, Proposition 1.2 of [Image graphs and multiplicity stages](image-graphs-and-multiplicity-stages.md) [OpenAI-KZ, Section 3]. The pairing of a system compares words along the chains of its image graph, but the comparisons shift positions by arbitrary amounts. Cutting every chain into blocks of a common length \(s\), chosen by simultaneous approximation of all shifts, makes almost every block match a single partner block letter for letter. The words on all blocks of a connected cluster of matched blocks are then determined by one of them, up to few letters, and the squared-word estimate of [Projective planes and prescribed types](projective-planes-and-prescribed-types.md) bounds the number of words in each weight range. These are the counting inputs for [The bounded-pattern estimate](the-bounded-pattern-estimate.md).

- Subcomparisons and a common grid (Section 1).
- Blocks and alignment (Section 2).
- Joins and unmatched blocks (Section 3).
- Links, propagation and self-links (Section 4).
- Binning the word weights (Section 5).

We keep a system with a pairing as in Definition 1.1 of [Image graphs and multiplicity stages](image-graphs-and-multiplicity-stages.md), with at most \(K\) paths, total length \(L\le H\le CL\), at most \(I\) interval pairs, \(b\) unpaired occurrences, and the reduction condition (1.1) there; its image graph \(\Delta\), marks, chains and multiplicities \(m_e\) are as in Sections 2 and 3 of that lesson. Constants may depend on \(K,C,I\), and \(o(\cdot)\) refers to \(L\to\infty\) uniformly over such systems.

## 1. Subcomparisons and a common grid

Orient every chain and identify it with the real interval \([0,\ell]\), where \(\ell\) is its length; its edges sit at the *positions* \(\frac12,\frac32,\ldots,\ell-\frac12\), and every edge carries a letter read in the chain's orientation. Since every path traverses whole chains, each interval pair of the pairing, cut at the ends of the chain traversals on both sides, splits into boundedly many *subcomparisons*, each between one traversal of a chain and one traversal of a chain. In chain coordinates a subcomparison is a map
\[
x\longmapsto\sigma x+a,\qquad\sigma\in\{1,-1\},\ a\in\mathbb Z,
\]
on a set of consecutive positions: \(a\) is an integer because positions are half-integers. Reading the letters in the chain orientations, a subcomparison with \(\sigma=1\) relates equal letters and one with \(\sigma=-1\) inverse letters; reversing the reading direction of a traversal both reverses the order and inverts the letters, so this holds in all cases. The *cuts* are the ends of the subcomparison domains in path positions.

Let \(a_1,\ldots,a_d\) be the shifts of all subcomparisons, padded with zeros to a fixed length \(d\ge1\) depending only on \(K,C,I\). Put
\[
N=\bigl\lfloor L^{1/(2(d+1))}\bigr\rfloor,\qquad R=\lfloor\sqrt N\rfloor .
\]

**Lemma 1.1** (a common grid). There is an integer \(1\le u\le N^d\) with \(\operatorname{dist}(ua_i/L,\mathbb Z)\le1/N\) for every \(i\). With the least such \(u\) and \(s=L/(uR)\), for \(1\le i\le d\),
\[
\begin{aligned}&\frac L{N^{d+1/2}}\le s\le\frac LR,\\&\operatorname{dist}\Bigl(\frac{a_i}s,\mathbb Z\Bigr)\le\frac RN,\end{aligned}\tag{1.1}
\]

*Proof.* Divide \([0,1)^d\) into \(N^d\) cubes of side \(1/N\). Among the \(N^d+1\) points whose coordinates are the fractional parts of \(ka_1/L,\ldots,ka_d/L\), \(0\le k\le N^d\), two lie in one cube, say for \(k<k'\); then \(u=k'-k\) works. The bounds on \(s\) follow from \(1\le u\le N^d\) and \(\sqrt N/2\le R\le\sqrt N\) for large \(N\). Finally, if \(ua_i/L=m+\theta\) with \(m\in\mathbb Z\) and \(|\theta|\le1/N\), then \(a_i/s=ua_iR/L=Rm+R\theta\), at distance at most \(R/N\) from \(\mathbb Z\). \(\square\)

The choice of \(u\), hence of \(s\), is determined by the unlabelled pattern. Since \(N\) is a positive power of \(L\), \(s\ge L^{(2d+3)/(4d+4)}\) tends to infinity as a positive power of \(L\), while \(s/L\le1/R\) and \(R/N\le N^{-1/2}\) tend to \(0\).

## 2. Blocks and alignment

On each chain \([0,\ell]\), consider the intervals \([ks,(k+1)s)\), \(k=0,1,2,\ldots\), contained in \([0,\ell]\). The positions in such an interval form a *full block*. A full block has \(h_i=s+O(1)\) positions, the positions after the last full block form an *end fragment* of fewer than \(s+1\) positions, and all traversals of a chain use the same blocks. We index the full blocks of \(\Delta\) by \(i\) and write \(m_i\) for the multiplicity of their chain. A *block occurrence* is a full block on a particular traversal; there are \(O(L/s)\) of them.

**Lemma 2.1** (alignment). Let \(x\mapsto\sigma x+a\) be a subcomparison, and write \(a=\nu s+r\) with \(\nu\in\mathbb Z\) and \(|r|\le sR/N\). The image of the grid interval \([ks,(k+1)s)\) meets the grid interval \([(k+\nu)s,(k+\nu+1)s)\) if \(\sigma=1\), or \([(\nu-k-1)s,(\nu-k)s)\) if \(\sigma=-1\), in an interval of length \(s-|r|\) containing at least \(s-|r|-2\) positions.

*Proof.* For \(\sigma=1\) the image is \([(k+\nu)s+r,(k+\nu+1)s+r)\); for \(\sigma=-1\) it is \(((\nu-k-1)s+r,(\nu-k)s+r]\). In both cases it is the indicated grid interval moved by \(r\), and an interval of length \(s-|r|\) contains at least \(s-|r|-2\) half-integers. \(\square\)

By (1.1), \(|r|\le sR/N=o(s)\), so aligned blocks share \(s-o(s)\) positions.

## 3. Joins and unmatched blocks

Fix \(\kappa=\kappa(L)\to0\), depending only on \(L\), with \(\kappa s\ge2sR/N+4\) and \(\kappa<\frac13\); for instance \(\kappa=2R/N+4/s\) for large \(L\). Two block occurrences are *joined* if some subcomparison maps a run of at least \((1-\kappa)s\) consecutive positions of one of them onto positions of the other. We record one such subcomparison for each join.

**Lemma 3.1** (joins). Every block occurrence takes part in at most one join. The number \(b_*\) of block occurrences in no join satisfies
\[
\begin{aligned}sb_*&\le b+O\Bigl(s+\frac Ls\Bigr)\\&=b+o(L).\end{aligned}\tag{3.1}
\]

*Proof.* A join occupies more than half of each of its two block occurrences, since \((1-\kappa)s>(s+O(1))/2\) for large \(L\). The intervals of the pairing are disjoint, so the runs used by two joins at the same block occurrence would overlap in occurrences belonging to two different intervals, or to one interval compared twice. So a block occurrence takes part in at most one join.

A block occurrence is *central* if it is at distance more than \(3s+3\) from all cuts and from the ends of its chain. Only boundedly many block occurrences are not central. A central block occurrence lies either inside one subcomparison domain or outside all of them. If it lies inside one, Lemma 2.1 gives a full partner block on the other side, sharing at least \(s-|r|-2\ge(1-\kappa)s\) consecutive positions with its image, and the partner is again away from the chain ends; so it is joined. If it lies outside all domains, all its \(s-O(1)\) positions are unpaired. Therefore the central unjoined block occurrences number at most \(b/(s-O(1))\), and adding the boundedly many others,
\[
\begin{aligned}sb_*&\le b+O(1)\cdot\frac{b}{s}+O(s)\\&\le b+O\Bigl(\frac Ls+s\Bigr),\end{aligned}
\]
using \(b\le H\le CL\). Both \(L/s\) and \(s\) are \(o(L)\). \(\square\)

## 4. Links, propagation and self-links

Forgetting which traversal a block occurrence belongs to turns every join into a *link* between two full blocks. The *link graph* has the full blocks as vertices and the links as edges, possibly with loops (*self-links*) and parallel links. For a component \(\mathcal U\) of the link graph put
\[
S_{\mathcal U}=\sum_{i\in\mathcal U}m_i,\qquad z_{\mathcal U}=\max_{i\in\mathcal U}m_i,
\]
and let \(b_{\mathcal U}\) be the number of unjoined occurrences of blocks of \(\mathcal U\). A *word assignment* gives every position of \(\Delta\) a letter, in the chain orientation, such that consecutive positions inside a chain never carry a cancelling turn and every recorded subcomparison relates equal or inverse letters as it should. The letters of an actual realization form a word assignment: consecutive edges of a chain meet at a vertex of degree \(2\) of \(\Delta\), where they are two distinct edges of the immersed graph \(\Gamma\).

**Lemma 4.1** (propagation). For a component \(\mathcal U\) and a block \(i_0\in\mathcal U\), the number of ways to extend a given word on \(i_0\) to words on all blocks of \(\mathcal U\) compatible with the recorded links is at most \(\exp(o(s)\,\#\mathcal U)\).

*Proof.* Choose a spanning tree of \(\mathcal U\) rooted at \(i_0\). A link from a block to its child fixes at least \((1-\kappa)s\) letters of the child's word, possibly read backwards and inverted, so at most \(\kappa s+O(1)\) letters remain free, with at most \((\#T)^{\kappa s+O(1)}=\exp(o(s))\) choices. Multiply along the tree. \(\square\)

**Lemma 4.2** (self-links). If \(\mathcal U\) contains a self-link of a block \(i\), then either no word assignment exists, or the word on \(i\) has at most \(\exp(o(s))\) possibilities.

*Proof.* A self-link joins two occurrences of the same block, so its recorded subcomparison relates positions \(x\in D\) of the block to positions \(\sigma x+a\) of the same block, where \(D\) is a run of at least \((1-\kappa)s\) positions.

If \(\sigma=1\), the constraint is \(W(x)=W(x+a)\) for \(x\in D\), where \(W\) is the word on the block. The shift \(a\) is not \(0\): otherwise two paired occurrences would traverse the same edge, contrary to the reduction condition (1.1) of [Image graphs and multiplicity stages](image-graphs-and-multiplicity-stages.md). Joining \(x\) to \(x+a\) for \(x\in D\) gives a graph on the \(h_i\) positions of the block whose components are arithmetic progressions with difference \(|a|\); it is a forest with \(\#D\) edges, so it has \(h_i-\#D\le\kappa s+O(1)\) components. A word satisfying the constraints is constant on components, so there are at most \((\#T)^{\kappa s+O(1)}=\exp(o(s))\) of them.

If \(\sigma=-1\), the constraint is \(W(a-x)=\overline{W(x)}\) for \(x\in D\). The set \(J=D\cap(a-D)\) is a run of positions symmetric about \(a/2\) with \(\#J\ge2\#D-h_i>0\). If \(a\) is odd, \(a/2\) is a position in \(J\), and its letter would equal its own inverse, which is impossible since the involution has no fixed points. If \(a\) is even, the positions \(a/2-\frac12\) and \(a/2+\frac12\) lie in \(J\) and are consecutive, and their letters would be inverse, a cancelling turn inside a chain. So no word assignment exists. \(\square\)

**Lemma 4.3** (link balance). If \(\mathcal U\) has no self-link, then
\[
2z_{\mathcal U}\le S_{\mathcal U}+b_{\mathcal U}.\tag{4.1}
\]

*Proof.* Let \(i\in\mathcal U\) have \(m_i=z_{\mathcal U}\). At least \(z_{\mathcal U}-b_{\mathcal U}\) of its occurrences are joined, each to an occurrence of a different block of \(\mathcal U\), since there are no self-links, and different joins use different occurrences by Lemma 3.1. The other blocks of \(\mathcal U\) have \(S_{\mathcal U}-z_{\mathcal U}\) occurrences in all. \(\square\)

## 5. Binning the word weights

For a word \(W_i\) on a full block \(i\), read in the chain orientation and without cancelling turns, every turn weight is positive by Lemma 3.1 of [Projective planes and prescribed types](projective-planes-and-prescribed-types.md), so \(P(W_i)>0\). Its *bin* is the integer \(d_i=\lfloor-\log P(W_i)\rfloor\).

**Lemma 5.1** (bins; [OpenAI-KZ, Section 3]). Put \(a_0=2\log129\) and \(\delta=1/600\). For all sufficiently large \(L\), every block word without cancelling turns has
\[
\frac{\delta s}2\le d_i\le a_0s,
\]
and for every integer \(d\) the number of words of length \(h_i\) with bin \(d\) is at most \(\exp(2d-\delta s)\).

*Proof.* By Lemma 4.1 of that lesson, \(P(W)^2\le\sum_{W'\in T^{h}}P(W')^2\le e^{-2\delta h}\) for words of length \(h\ge3002\), so \(-\log P(W_i)\ge\delta h_i\ge\delta s/2+1\) for large \(s\), and \(d_i\ge\delta s/2\). Every positive turn weight is at least \(1/129\), so \(-\log P(W_i)\le(h_i-1)\log129\le a_0s\). Every word with bin \(d\) has \(P(W)>e^{-d-1}\), so \(P(W)^2>e^{-2d-2}\), and the number of such words is at most \(e^{2d+2}e^{-2\delta h_i}\le e^{2d-\delta s}\) for large \(s\). \(\square\)

The upper bound uses the squared weights: the number of words in a bin is controlled because their squared weights cannot add up to more than \(e^{-2\delta h}\).

An *enlarged pattern* is an unlabelled pattern, as in Section 4 of [Image graphs and multiplicity stages](image-graphs-and-multiplicity-stages.md), together with the bins \(d_i\) of all full blocks.

**Lemma 5.2** (few enlarged patterns). The number of enlarged patterns is \(\exp(o(L))\).

*Proof.* By Lemma 4.1 of that lesson, the unlabelled patterns number at most a polynomial in \(L\). There are \(O(L/s)\) full blocks, each with at most \(a_0s+1\) possible bins, so the bins add a factor \(\exp(O((L/s)\log s))\), which is \(\exp(o(L))\) because \(s\to\infty\). \(\square\)

## 6. Exercises

**6.1.** Take \(d=1\) and \(L=10^{12}\). Compute \(N\), \(R\), and the range (1.1) of \(s\).

**6.2.** Show that in Lemma 2.1 the image of a grid interval under a reflection \(x\mapsto a-x\) is a half-open interval of the form \((\cdot,\cdot]\), and explain why this costs at most one position compared with a translation.

**6.3.** In the proof of Lemma 4.2, check that the graph joining \(x\) to \(x+a\) for \(x\in D\) has no cycles.

**6.4.** Show that a word \(W\) of length \(h\) on which a translation self-link with shift \(a\ne0\) acts on all of \(D=\{\frac12,\ldots,h-|a|-\frac12\}\) is periodic with period \(|a|\), and count the words of length \(h\) with this property.

**6.5.** Show that a component of the link graph without self-links, consisting of two blocks of multiplicities \(2\) and \(1\), has at least one unjoined occurrence, and check (4.1) for it.

## 7. Solutions

**6.1.** \(L^{1/4}=1000\), so \(N=1000\) and \(R=31\). Then \(L/N^{3/2}\approx3.16\cdot10^7\le s\) and \(s\le L/R\approx3.2\cdot10^{10}\), and the shifts are within \(R/N=0.031\) of multiples of \(s\), relative to \(s\).

**6.2.** \(x\mapsto a-x\) maps \([ks,(k+1)s)\) onto \((a-(k+1)s,a-ks]\). Its intersection with a half-open grid interval differs from that of the corresponding half-open interval at most at one endpoint, which is at most one position.

**6.3.** Every edge joins \(x\) to \(x+a\), and following edges in the direction of increasing position moves by \(|a|\) at each step; a cycle would have to return to its start, which is impossible when every step increases the position.

**6.4.** The constraint \(W(x)=W(x+a)\) for all \(x\) with \(x,x+a\) in the block says \(W\) has period \(|a|\); such a word is determined by its first \(|a|\) letters, so there are at most \((\#T)^{|a|}\) of them.

**6.5.** Let block \(1\) have multiplicity \(2\) and block \(2\) multiplicity \(1\). Without self-links, an occurrence of block \(1\) can only be joined to the single occurrence of block \(2\), and that occurrence takes part in at most one join by Lemma 3.1. So at least one occurrence of block \(1\) is unjoined, \(b_{\mathcal U}\ge1\), and (4.1) reads \(4\le3+b_{\mathcal U}\).

## References

- [OpenAI-KZ] OpenAI, *A Torsion-Free Group Algebra with Zero Divisors*, OpenAI Math Release preprint, 23 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026
