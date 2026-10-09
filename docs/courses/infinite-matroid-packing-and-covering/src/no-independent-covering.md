# No independent covering

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson completes the counterexample. Copies of the self-dual matroid \(Q\) of [Assembling a self-dual matroid](assembling-a-self-dual-matroid.md) are placed at the vertices of a doubly infinite path whose edges are copies of \(D\); the copies at even vertices form \(M_0\), those at odd vertices \(M_1\) (Section 1). If an independent set of \(M_0\) and one of \(M_1\) covered the ground set, the inequality (4.1) of that lesson would produce an infinite strictly decreasing sequence of ordinals along the path (Section 2). The reduction of [Infinite matroids and the packing/covering conjecture](infinite-matroids-and-the-conjecture.md) then excludes every packing/covering partition. Section 3 records consequences.

## 1. Two matroids on a double ray

For \(n\in\mathbb Z\), let the *bundle* \(e_n=\{n\}\times D\) join the vertices \(v_n\) and \(v_{n+1}\) of a doubly infinite path, and let \(E=\mathbb Z\times D=\bigcup_ne_n\), a countably infinite set. The *central bundle* is \(e_{-1}\), joining \(v_{-1}\) and \(v_0\). The vertex \(v_n\) is incident with \(e_{n-1}\) and \(e_n\); call the one closer to the central bundle its *inward* bundle and the other its *outward* bundle:
\[
\text{inward}(v_n)=e_{n-1},\ \text{outward}(v_n)=e_n\ \ (n\ge0);\qquad\text{inward}(v_n)=e_n,\ \text{outward}(v_n)=e_{n-1}\ \ (n\le-1).
\]
So both \(v_{-1}\) and \(v_0\) have the central bundle as inward bundle. Let \(Q_n\) be the copy of \(Q\) on \(e_{n-1}\cup e_n\) obtained by sending the element \(d\) of the copy \(L\) to \((\text{inward},d)\) and the element \(d\) of \(R\) to \((\text{outward},d)\). Put
\[
M_0=\bigoplus_{n\text{ even}}Q_n,\qquad M_1=\bigoplus_{n\text{ odd}}Q_n .
\]
Each bundle \(e_k\) has exactly one endpoint of each parity, so for each \(i\) the supports \(e_{n-1}\cup e_n\) of the summands partition \(E\). By Proposition 3.1 of [Infinite matroids and the packing/covering conjecture](infinite-matroids-and-the-conjecture.md), \(M_0\) and \(M_1\) are matroids on \(E\), and they are self-dual because \(Q\) is.

**Lemma 1.1** (Spanning property). For \(i=0,1\) and \(X\subseteq E\), every set spanning \(M_i\!\upharpoonright\!X\) contains a maximal independent subset of \(X\).

*Proof.* For \(S\subseteq X\), the restriction's closure of \(S\) is \(\operatorname{cl}_{M_i}(S)\cap X\), since independence of subsets of \(X\) is the same in \(M_i\) and in \(M_i\!\upharpoonright\!X\). By Proposition 3.1 there, \(x\) in the support \(F_n\) of \(Q_n\) lies in \(\operatorname{cl}_{M_i}(S)\) exactly when it lies in \(\operatorname{cl}_{Q_n}(S\cap F_n)\). So if \(S\) spans \(M_i\!\upharpoonright\!X\), each \(S\cap F_n\) spans \(Q_n\!\upharpoonright\!(X\cap F_n)\), and by Proposition 4.2(c) of [Assembling a self-dual matroid](assembling-a-self-dual-matroid.md) it contains a maximal independent subset \(J_n\) of \(X\cap F_n\). Independence in \(M_i\) is componentwise, so \(\bigcup_nJ_n\subseteq S\) is a maximal independent subset of \(X\). \(\square\)

**Lemma 1.2.** Every finite subset of \(E\) is independent in \(M_0\) and in \(M_1\), and \(E\) is dependent in both; so neither is finitary or cofinitary. Neither has a nonempty finitary or cofinitary direct summand.

*Proof.* The parts of a finite set in the summands are finite, hence independent by Proposition 4.2(b) of [Assembling a self-dual matroid](assembling-a-self-dual-matroid.md); \(E\) meets every support in the dependent ground set of a copy of \(Q\). For the last claim, let \(M_i=N\oplus N'\), with \(N\) on a nonempty set \(F\) and \(N'\) on \(E\setminus F\); the independent sets of \(N\) are the independent sets of \(M_i\) inside \(F\), and the bases of \(M_i\) are the unions of a basis of \(N\) and one of \(N'\) (Proposition 3.1 of [Infinite matroids and the packing/covering conjecture](infinite-matroids-and-the-conjecture.md)). Since the complement of a basis of \(M_i\) is a basis, the complement in \(F\) of a basis of \(N\) is a basis of \(N\), so \(N^*=N\). If \(N\) is finitary, then \(F\), all of whose finite subsets are independent, is independent; it is the only basis of \(N\), while its complement \(\varnothing\) in \(F\) must also be a basis, which is impossible for \(F\ne\varnothing\). If \(N\) is cofinitary, then \(N=N^*\) is finitary, and the same contradiction applies. \(\square\)

## 2. The descending ranks

**Theorem 2.1** (OpenAI 2026). There are no independent sets \(J_0\) of \(M_0\) and \(J_1\) of \(M_1\) with \(J_0\cup J_1=E\). Consequently the pair \((M_0,M_1)\) of self-dual matroids on the countable set \(E\) has no packing/covering partition, and the infinite matroid packing/covering conjecture is false in ZFC.

*Proof.* Suppose \(J_0\cup J_1=E\). Replacing \(J_1\) by its subset \(E\setminus J_0\), we may assume that \(E=J_0\mathbin{\dot\cup}J_1\). Assign every element of a bundle to the endpoint of the bundle whose parity is that of the part \(J_0\) or \(J_1\) containing it. The elements assigned to \(v_n\) form the set \(J_{n\bmod2}\cap(e_{n-1}\cup e_n)\), which is independent in \(Q_n\).

The labels of the central bundle are split into those assigned to \(v_{-1}\) and those assigned to \(v_0\), two complementary subsets of \(D\). Exactly one of them is large. Let \(w_0\) be the vertex receiving the large one, and let \(w_0,w_1,w_2,\dots\) be the vertices from \(w_0\) outward (\(w_k=v_k\) if \(w_0=v_0\), and \(w_k=v_{-1-k}\) if \(w_0=v_{-1}\)). The outward bundle of \(w_k\) is the inward bundle of \(w_{k+1}\). Let \(x_k\subseteq D\) be the labels assigned to \(w_k\) on its inward bundle and \(z_k\) those assigned on its outward bundle. Each element of a bundle is assigned to exactly one endpoint, so
\[
x_{k+1}=D\setminus z_k .
\]

We show by induction that every \(x_k\) is large and \(\rho(x_k)>\rho(x_{k+1})\). Let \(x_k\) be large. The set assigned to \(w_k\) is independent in its copy of \(Q\), so it lies in a basis, which in the coordinates of \(Q\) is a basis \(B_k\) with \(x_k\subseteq(B_k)_L\) and \(z_k\subseteq(B_k)_R\). Put \(u_k=(B_k)_L\) and \(y_k=D\setminus(B_k)_R\). Then \(u_k\supseteq x_k\) is large, and (4.1) of [Assembling a self-dual matroid](assembling-a-self-dual-matroid.md) gives that \(y_k\) is large with \(\rho(u_k)>\rho(y_k)\). Since \(y_k\subseteq D\setminus z_k=x_{k+1}\), the set \(x_{k+1}\) is large. By the monotonicity of \(\rho\) (Lemma 4.1 of [Ideals, ultrafilters and an ordinal rank](ideals-ultrafilters-and-an-ordinal-rank.md)),
\[
\rho(x_k)\ge\rho(u_k)>\rho(y_k)\ge\rho(x_{k+1}).
\]
The set \(\{\rho(x_k):k\ge0\}\) of ordinals has a least element \(\rho(x_k)\) (Proposition 10.2 of the core course text), but \(\rho(x_{k+1})<\rho(x_k)\). This contradiction shows that no independent covering exists.

\(M_0\) and \(M_1\) are self-dual and have the spanning property of Lemma 1.1, so by Lemma 4.2 of [Infinite matroids and the packing/covering conjecture](infinite-matroids-and-the-conjecture.md) a packing/covering partition would give an independent covering. \(\square\)

## 3. Consequences

**Corollary 3.1.** In ZFC there is a self-dual matroid on a countable set in which every subset is independent or spanning and every basis and every complement of a basis is infinite.

*Proof.* \(Q\), by Theorem 4.1 and Proposition 4.2 of [Assembling a self-dual matroid](assembling-a-self-dual-matroid.md), with Lemma 1.2(2) of [Infinite matroids and the packing/covering conjecture](infinite-matroids-and-the-conjecture.md). \(\square\)

Such matroids are called *uniform*. Bowler and Geschke had constructed countable self-dual uniform matroids under Martin's axiom for countable partial orders, hence under the continuum hypothesis, and asked for a construction in ZFC [BG]; Gollin and Joó record the existence in ZFC of a uniform matroid of infinite rank and corank as open [GJ, Section 1]. Corollary 3.1 answers both.

The following consequences use equivalences proved by Bowler and Carmesin, which this course does not reprove.

- *Matroid intersection.* By [BC, Proposition 3.6], \((M,N)\) satisfies the intersection property if and only if \((M,N^*)\) has a packing/covering partition. With \(M=M_0\), \(N=M_1=M_1^*\), Theorem 2.1 shows that \((M_0,M_1)\) fails the intersection property: for every set \(J\) independent in both and every partition \(J=J_0\mathbin{\dot\cup}J_1\), \(\operatorname{cl}_{M_0}(J_0)\cup\operatorname{cl}_{M_1}(J_1)\ne E\). So the unrestricted infinite matroid intersection conjecture is false. Both matroids are direct sums of uniform matroids, *partitional* in Joó's terminology, on a common countable set, which answers Joó's question for this class negatively [Joó2, Question 1.5]. Joó proved the intersection conjecture for finitary matroids on a countable set [Joó1], and a packing/covering theorem for families of direct sums of finitary and cofinitary matroids on a countable set [Joó3]; by Lemma 1.2, \(M_0\) and \(M_1\) lie outside these classes.
- *Separate covering and packing conjectures.* Bowler and Carmesin also formulated separate Covering and Packing Conjectures and proved that, as universal statements, they are equivalent to the packing/covering conjecture [BC, Section 7]; so they are false as well.

## 4. Exercises

**4.1.** Draw the double ray with the bundles \(e_{-3},\dots,e_2\) and mark, for each vertex, which bundle is its \(L\)- and which its \(R\)-coordinate. Check that \(e_{-1}\) is the \(L\)-coordinate of both of its endpoints and every other bundle is the \(L\)-coordinate of exactly one endpoint.

**4.2.** Where does the proof of Theorem 2.1 use that the ultrafilter contains exactly one of a set and its complement? Where does it use that \(Q\) is self-dual?

**4.3.** Show that for every self-dual matroid \(N\) on a set \(F\), \(F\) is the union of two independent sets of \(N\). So Theorem 2.1 depends on the interplay of the two matroids \(M_0\) and \(M_1\).

## 5. Solutions

**4.1.** For \(n\ge0\), \(v_n\) has \(L=e_{n-1}\), \(R=e_n\); for \(n\le-1\), \(L=e_n\), \(R=e_{n-1}\). So \(e_{-1}\) is \(L\) at \(v_{-1}\) and at \(v_0\); a bundle \(e_k\) with \(k\ge0\) is \(L\) at \(v_{k+1}\) and \(R\) at \(v_k\); a bundle \(e_k\) with \(k\le-2\) is \(L\) at \(v_k\) and \(R\) at \(v_{k+1}\).

**4.2.** Exactly one of the two complementary label sets of the central bundle is large, which starts the induction, and \(x_{k+1}=D\setminus z_k\) contains the large set \(y_k\). Self-duality of \(Q\) is used for the second conclusion, through Lemma 4.2 of the first lesson; the absence of an independent covering uses only the bases of \(Q\) and the inequality (4.1).

**4.3.** Take a basis \(B\) of \(N\). Its complement \(F\setminus B\) is a basis, and \(B\cup(F\setminus B)=F\).

## References

- [OpenAI-IM] OpenAI, *A counterexample to the infinite matroid packing/covering conjecture*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026/paper.pdf
- [BC] N. Bowler and J. Carmesin, *Matroid intersection, base packing and base covering for infinite matroids*, Combinatorica 35 (2015). https://arxiv.org/abs/1202.3409
- [BG] N. Bowler and S. Geschke, *Self-dual uniform matroids on infinite sets*, Proceedings of the AMS 144 (2016); author version on the author's page. https://www.math.uni-hamburg.de/home/geschke/papers/UniformMatroid7.pdf
- [GJ] J. P. Gollin and A. Joó, *Wild generalised truncation of infinite matroids*, 2025. https://arxiv.org/abs/2504.05064
- [Joó1] A. Joó, *Proof of Nash-Williams' intersection conjecture for countable matroids*, Advances in Mathematics 380 (2021). https://arxiv.org/abs/1912.13253
- [Joó2] A. Joó, *Intersection of a partitional and a general infinite matroid*, Discrete Mathematics 344 (2021). https://arxiv.org/abs/2009.07205
- [Joó3] A. Joó, *On the packing/covering conjecture of infinite matroids*, Israel Journal of Mathematics 261 (2024). https://arxiv.org/abs/2103.14881
