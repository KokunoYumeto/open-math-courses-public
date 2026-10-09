# Nested predicates on a labelled tournament

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson builds the Boolean functions of OpenAI's separation of block sensitivity from the square of sensitivity [OpenAI-S, Section 2]. They come in levels \(0,1,\dots,d\), and each level is a nested family of predicates: \(P_{\ell,1}\ge P_{\ell,2}\ge\dots\), so a predicate with a larger index accepts fewer inputs. Level \(0\) consists of indicators of unions of Hamming balls of radii \(d,d-1,\dots,0\) around well separated centres. At level \(\ell\), the input is cut into \(kr\) children arranged in \(k\) rows of \(r\). A *clause* for row \(i\) asks the strongest child predicate to accept every child in row \(i\), and a weaker child predicate to reject one selected child in each row \(j\) that \(i\) points to in a tournament on the rows; the selected position is a label \(a(i,j)\). The parent predicate accepts when some clause holds, and varying the weaker predicate gives the nested family.

All predicates vanish at the all-zero input, and the number of disjoint sensitive blocks there is multiplied by \(k\) at each level (Lemma 4.1). The point of the construction is that sensitivity grows much more slowly; the lesson [Sensitivity recurrences and a superquadratic separation](sensitivity-recurrences-and-a-superquadratic-separation.md) proves this using the quantities of Section 5. The labels are chosen at random so that one configuration of nearly satisfied clauses cannot occur (Lemma 1.1). The rows of a tournament with one selected blocking position in each outgoing row adapt a construction of Meiburg, who used it for spectral sensitivity [Meiburg].

We use the notation of [Sensitivity, block sensitivity and composition](sensitivity-block-sensitivity-and-composition.md): \(x^a\) is \(x\) with coordinate \(a\) flipped, and a sensitive block at \(x\) is a nonempty set of coordinates whose flip changes the value.

## 1. The tournament and the labels

Fix integers \(d\ge1\) and \(M\ge3\), and put
\[
L=d+2,\qquad k=2M^2+1,\qquad r=\lceil\sqrt M\,\rceil,\qquad t=16.
\]
A *tournament* on \([k]\) orients each pair of distinct vertices: exactly one of \(i\to j\) and \(j\to i\) holds. We use the cyclic tournament: \(i\to j\) when \(j-i\) is congruent to one of \(1,\dots,M^2\) modulo \(k\). Every vertex has exactly \(M^2\) outgoing edges (Exercise 6.1).

**Lemma 1.1** (labels). The edges can be labelled by numbers \(a(i,j)\in[r]\) so that there is no set \(I\subseteq[k]\) with \(|I|=t\) and numbers \(m_j\in[r]\), \(j\in I\), such that
\[
a(i,j)=m_j\qquad\text{for every edge }i\to j\text{ with }i,j\in I.
\]

**Proof.** Choose the labels independently and uniformly in \([r]\). For a fixed \(I\) and fixed \((m_j)_{j\in I}\), the \(\binom t2=120\) edges inside \(I\) have their labels prescribed, each with probability \(1/r\), independently; so the event has probability \(r^{-120}\). There are at most \(k^t\) sets \(I\) and \(r^t\) choices of the \(m_j\), so the probability that some \((I,(m_j))\) occurs is at most
\[
k^{16}r^{16}r^{-120}=k^{16}r^{-104}\le(3M^2)^{16}M^{-52}=3^{16}M^{-20}\le3^{-4}<1,
\]
using \(k\le3M^2\), \(r\ge\sqrt M\) and \(M\ge3\). Hence some labelling has the property. \(\square\)

Fix such a labelling from now on.

## 2. Hamming balls

For \(0\le\ell\le d\) put
\[
H_\ell=d+1-\ell,\qquad N_\ell=LM(kr)^\ell.
\]
The predicates of level \(\ell\) are \(P_{\ell,q}:\{0,1\}^{N_\ell}\to\{0,1\}\), \(q\in[H_\ell]\).

At level \(0\), split the \(LM\) coordinates into \(M\) blocks \(E_1,\dots,E_M\) of size \(L\), let \(z_j\in\{0,1\}^{LM}\) be the indicator of \(E_j\), let \(\operatorname{dist}\) be the Hamming distance (the number of differing coordinates), and put
\[
D(x)=\min_{j\in[M]}\operatorname{dist}(x,z_j),\qquad P_{0,q}(x)=\mathbf 1\{D(x)\le H_0-q\}\quad(q\in[d+1]).
\]
These are the indicators of the unions of the balls of radius \(d+1-q\) around the centres, for the radii \(d,d-1,\dots,0\), so they are nested. Distinct centres have distance \(2L=2d+4\).

## 3. Clauses

Let \(1\le\ell\le d\), and put \(H=H_\ell\) and \(Q=H+1=H_{\ell-1}\). Split an input \(x\in\{0,1\}^{N_\ell}\) into \(kr\) *children* \(x_{j,c}\in\{0,1\}^{N_{\ell-1}}\), \(j\in[k]\) (the *row*) and \(c\in[r]\) (the *position*). For \(q\in[H]\) and \(i\in[k]\), the clause \(C_{i,q}\) holds at \(x\) if
\[
\begin{aligned}
P_{\ell-1,Q}(x_{i,c})&=1\quad\text{for all }c\in[r]&&\text{(the targets of }C_{i,q}),\\
P_{\ell-1,Q-q}(x_{j,a(i,j)})&=0\quad\text{for all }j\text{ with }i\to j&&\text{(the gates of }C_{i,q}),
\end{aligned}
\]
and \(P_{\ell,q}(x)=1\) if some clause \(C_{i,q}\), \(i\in[k]\), holds. Since \(1\le Q-q\le H<Q\), the indices are those of predicates of level \(\ell-1\), and the targets always use the predicate with the largest index \(Q\).

**Lemma 3.1** (structure). (a) The \(r+M^2\) conditions of a clause concern \(r+M^2\) distinct children. Consequently, flipping one input coordinate changes the truth value of at most one condition of a given clause.

(b) For each \(\ell\), the predicates are nested: \(P_{\ell,1}\ge P_{\ell,2}\ge\dots\ge P_{\ell,H_\ell}\). More precisely, for \(q<q'\) every clause satisfies \(C_{i,q'}\le C_{i,q}\).

**Proof.** (a) The targets concern the \(r\) children of row \(i\); each gate concerns one child of a row \(j\neq i\), and distinct gates concern distinct rows because there is one edge from \(i\) to each \(j\) with \(i\to j\). A coordinate of the input belongs to exactly one child, and a flip changes only the predicates of that child.

(b) Induction on \(\ell\); level \(0\) was noted above. Let \(q<q'\) and suppose level \(\ell-1\) is nested. Since \(Q-q'<Q-q\), \(P_{\ell-1,Q-q}\le P_{\ell-1,Q-q'}\), so a gate condition for \(q'\) (the child predicate of index \(Q-q'\) rejects) implies the one for \(q\). The targets do not depend on \(q\). Hence \(C_{i,q'}\le C_{i,q}\) and \(P_{\ell,q'}\le P_{\ell,q}\). \(\square\)

A flip may change several predicates of its child, and it may affect several clauses that use that child; Lemma 3.1(a) concerns one clause at a time. By construction \(N_\ell=krN_{\ell-1}\), as claimed in Section 2.

## 4. Disjoint sensitive blocks at zero

**Lemma 4.1** (blocks at zero). Let \(0\le\ell\le d\). Every \(P_{\ell,q}\) vanishes at the all-zero input, and there are \(Mk^\ell\) pairwise disjoint sets of coordinates, each of size \(Lr^\ell\), such that flipping any one of them at the all-zero input makes every \(P_{\ell,q}\) equal to \(1\).

**Proof.** At level \(0\), \(D(0)=L>d\), so all \(P_{0,q}(0)=0\), and flipping \(E_j\) gives \(z_j\), with \(D=0\). Let \(\ell\ge1\) and assume the lemma at level \(\ell-1\), with blocks \(B_1,\dots,B_{Mk^{\ell-1}}\). At the all-zero input every child is zero, so every target fails and every clause fails: \(P_{\ell,q}(0)=0\). For a row \(i\) and an index \(h\), let \(B_{i,h}\) be the union of the copies of \(B_h\) in the \(r\) children of row \(i\). Flipping \(B_{i,h}\) makes every child of row \(i\) equal to \(0^{B_h}\), where every predicate of level \(\ell-1\) accepts, so the targets of \(C_{i,q}\) hold; the children of the other rows remain zero, where every predicate of level \(\ell-1\) rejects, so the gates of \(C_{i,q}\) hold. So \(C_{i,q}\) and \(P_{\ell,q}\) hold for every \(q\). The sets \(B_{i,h}\) are pairwise disjoint (different rows use different children; in one child the \(B_h\) are disjoint), there are \(k\cdot Mk^{\ell-1}\) of them, and each has size \(r\cdot Lr^{\ell-1}\). \(\square\)

## 5. Sensitivity profiles

For \(0\le\ell\le d\) and \(b\in\{0,1\}\) let
\[
S_{\ell,b}=\max_{q\in[H_\ell]}s_b(P_{\ell,q}),
\]
the largest number of coordinates whose flip changes some predicate of level \(\ell\) from the value \(b\). For simultaneous changes of two predicates of the same level, let \(J_{\ell,b}\) be the largest value of
\[
\bigl|\{a\in[N_\ell]:P_{\ell,q}(x^a)=P_{\ell,q'}(x^a)=1-b\}\bigr|
\]
over all \(q<q'\) in \([H_\ell]\) and all \(x\) with \(P_{\ell,q}(x)=P_{\ell,q'}(x)=b\); a maximum over no cases is \(0\). In particular \(J_{d,0}=J_{d,1}=0\), since \(H_d=1\).

**Lemma 5.1** (level zero). \(S_{0,0}\le L\), \(S_{0,1}\le LM\) and \(J_{0,0}=J_{0,1}=0\).

**Proof.** Let \(P_{0,q}\) have radius \(\rho=H_0-q\in\{0,\dots,d\}\) and let \(P_{0,q}(x)=0\), so \(D(x)\ge\rho+1\). If a flip of coordinate \(a\) makes it accept, then \(D(x^a)\le\rho\), and since one flip changes each distance by exactly \(1\), some centre \(z\) has \(\operatorname{dist}(x,z)=\rho+1\le d+1\) and \(\operatorname{dist}(x^a,z)=\rho\). At most one centre lies within distance \(d+1\) of \(x\), since two such centres would be at distance at most \(2d+2<2L\). So \(a\) is one of the \(\rho+1\) coordinates where \(x\) and that centre differ, and \(S_{0,0}\le d+1\le L\). The bound on \(S_{0,1}\) is the number of coordinates.

For adjacent inputs \(x,y\), \(\operatorname{dist}(x,z_j)\le\operatorname{dist}(y,z_j)+1\) for every \(j\), so \(D(x)\le D(y)+1\), and symmetrically; thus \(|D(x)-D(y)|\le1\). Two predicates of level \(0\) with radii \(\rho<\rho'\) can both change from \(0\) to \(1\) under one flip only if \(D\) drops from at least \(\rho'+1\) to at most \(\rho\), and both change from \(1\) to \(0\) only if \(D\) rises from at most \(\rho\) to at least \(\rho'+1\); either way \(D\) changes by at least \(2\). \(\square\)

## 6. Exercises

**Exercise 6.1** (easy). Show that the cyclic orientation of Section 1 is a tournament on \([k]\) in which every vertex has exactly \(M^2\) outgoing and \(M^2\) incoming edges.

**Exercise 6.2** (easy). Show that for \(\ell\ge1\) the \(Mk^\ell\) blocks of Lemma 4.1 partition the set of all \(N_\ell\) coordinates.

**Exercise 6.3** (easy). Show that the property of Lemma 1.1 fails whenever \(r=1\), and explain where the proof uses \(r\ge\sqrt M\).

**Exercise 6.4** (medium). Show that \(S_{0,0}=d+1\) exactly.

**Exercise 6.5** (easy). For \(d=1\) and \(M=3\), compute \(L,k,r,H_0,H_1,N_0,N_1\), and the number and size of the blocks of Lemma 4.1 at level \(1\).

## 7. Solutions

**6.1.** For distinct \(i,j\) the residues \(j-i\) and \(i-j\) are nonzero and sum to \(0\) modulo \(k=2M^2+1\), so exactly one of them lies in \(\{1,\dots,M^2\}\). The outgoing neighbours of \(i\) are \(i+1,\dots,i+M^2\) and the incoming ones \(i-1,\dots,i-M^2\), modulo \(k\).

**6.2.** The blocks are disjoint, and their sizes add up to \(Mk^\ell\cdot Lr^\ell=LM(kr)^\ell=N_\ell\).

**6.3.** If \(r=1\), all labels equal \(1\), and any set \(I\) of size \(t\le k\) with all \(m_j=1\) violates the property. The proof needs \(k^{16}r^{-104}<1\), and \(r\ge\sqrt M\) makes \(r^{104}\) beat \(k^{16}\le(3M^2)^{16}\).

**6.4.** The proof of Lemma 5.1 gives \(S_{0,0}\le d+1\). For equality, let \(x\) be \(1\) on exactly one coordinate of \(E_1\). Then \(\operatorname{dist}(x,z_1)=L-1=d+1\), and \(\operatorname{dist}(x,z_j)=L+1\) for \(j\neq1\), so \(D(x)=d+1\) and \(P_{0,1}(x)=0\). Flipping any of the \(d+1\) other coordinates of \(E_1\) gives \(D=d\) and \(P_{0,1}=1\).

**6.5.** \(L=3\), \(k=19\), \(r=2\), \(H_0=2\), \(H_1=1\), \(N_0=9\), \(N_1=342\); at level \(1\) there are \(Mk=57\) blocks of size \(Lr=6\).

## References

- [Meiburg] A. Meiburg, *Block sensitivity can exceed spectral sensitivity squared*, arXiv:2608.00851 (2026), Sections 3.1 and 5.2–5.5. https://arxiv.org/abs/2608.00851
- [OpenAI-S] OpenAI, *A superquadratic separation between sensitivity and block sensitivity*, OpenAI Math Release preprint, 25 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026
