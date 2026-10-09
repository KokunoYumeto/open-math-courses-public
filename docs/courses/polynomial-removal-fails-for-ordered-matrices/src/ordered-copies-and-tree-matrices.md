# Ordered copies and tree matrices

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Removal lemmas say that an object far from having a property contains many small witnesses against it. For binary matrices whose rows and columns carry a fixed order, the witnesses are ordered copies of a fixed pattern. Alon, Fischer and Newman raised the question of efficient bounds for ordered matrices after treating the unordered case; Alon and Ben-Eliezer asked whether polynomial bounds always hold [AB, Problem 1.4]; and Gishboliner and Shapira stated the polynomial removal conjecture for a single ordered pattern in their survey [GS]. Alon, Ben-Eliezer and Fischer proved that some bound exists for every fixed distance [ABF]. This course presents OpenAI's construction showing that no polynomial bound exists, already for one fixed \(66\times66\) pattern [OpenAI-OM]:

**Theorem** (OpenAI 2026; Theorem 2.1 of [Distance from freeness](distance-from-freeness.md)). There is a binary \(66\times66\) matrix \(H\) such that for every integer \(h\ge1\), with \(n_h=(386h+2)2^h\) and \(\epsilon_h=(386h+2)^{-2}\), some binary \(n_h\times n_h\) matrix \(A_h\) is \(\epsilon_h\)-far from being \(H\)-free and has at most \(\epsilon_h2^{-h}n_h^{132}\) ordered copies of \(H\).

This lesson defines the pattern and the matrices \(A_h\). [Every copy meets the leaf diagonal](every-copy-meets-the-leaf-diagonal.md) locates all copies of \(H\) in \(A_h\), and [Distance from freeness](distance-from-freeness.md) shows that every \(H\)-free matrix differs from \(A_h\) in many entries.

## 1. Ordered copies and the conjecture

For \(k\ge1\) write \([k]=\{1,\dots,k\}\). Let \(H\) be a binary \(k\times k\) matrix and \(A\) a binary \(n\times n\) matrix. An *ordered copy* of \(H\) in \(A\) is a pair of increasing sequences \(r_1<\dots<r_k\) and \(c_1<\dots<c_k\) in \([n]\) with \(A(r_i,c_j)=H(i,j)\) for all \(i,j\in[k]\); zeros must match as well as ones. Let \(N_H(A)\) be the number of ordered copies, and call \(A\) *\(H\)-free* if \(N_H(A)=0\). The *distance* of \(A\) from \(H\)-freeness is
\[
\operatorname{dist}_H(A)=\frac1{n^2}\min\bigl\{|\{(r,c):A(r,c)\ne B(r,c)\}|:B\text{ binary and }H\text{-free}\bigr\},
\]
and \(A\) is *\(\epsilon\)-far* from \(H\)-freeness if \(\operatorname{dist}_H(A)\ge\epsilon\). Changes are allowed in both directions.

**Conjecture 1.1** (polynomial ordered matrix removal). For every binary square matrix \(H\), of size \(k\), there are \(c_H,C_H>0\) such that \(N_H(A)\ge c_H\epsilon^{C_H}n^{2k}\) for every \(n\ge1\), every \(0<\epsilon<1\) and every binary \(n\times n\) matrix \(A\) that is \(\epsilon\)-far from \(H\)-freeness.

The theorem above shows that Conjecture 1.1 fails (Corollary 2.2 of the third lesson).

## 2. The pattern

Let \(s=64\). For \(0\le a<32\) and \(1\le b\le5\), let \(\eta_b(a)=\lfloor a/2^{5-b}\rfloor\bmod2\) be the \(b\)-th binary digit of \(a\), written with five digits; so \((\eta_1(a),\dots,\eta_5(a))\), \(a=0,\dots,31\), lists all binary words of length five. The *anchor* \(S\in\{0,1\}^{s\times s}\) is
\[
S(u,v)=\begin{cases}\eta_{v-59}(u-33),&33\le u\le64\text{ and }60\le v\le64,\\ 1&\text{otherwise, if }u\ne v,\\ 0&\text{otherwise, if }u=v.\end{cases}
\]
So \(S\) is the all-ones matrix with zeros on the diagonal, except that its lower right \(32\times5\) corner lists the binary words of length five. With \(e_1,e_2\) the first two standard basis vectors of \(\mathbb R^s\), the pattern and its *body* are
\[
H=\begin{pmatrix}S&e_1&e_2\\ e_1^{\mathsf T}&1&0\\ e_2^{\mathsf T}&1&1\end{pmatrix},\qquad P=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad k=66 .
\]

The body is used through two facts about \(2\times2\) binary matrices: for binary \(a,b\),
\[
\begin{pmatrix}1&a\\1&b\end{pmatrix}\ne P\iff b\le a,\qquad\begin{pmatrix}a&b\\1&1\end{pmatrix}\ne P\iff a\le b. \tag{2.1}
\]
Indeed, the first matrix equals \(P\) exactly when \(a=0\) and \(b=1\), and the second exactly when \(a=1\) and \(b=0\). In both cases, if the smaller side is known to be \(1\), the other entry is forced to be \(1\); if the larger side is \(0\), the other is forced to be \(0\).

## 3. Positions indexed by a binary tree

Fix \(h\ge1\) and \(m=2^h\). The nodes of depth \(i\in\{0,\dots,h\}\) of the full binary tree are the integers \(0\le p<2^i\); the children of \(p\) are \(2p\) and \(2p+1\), and the parent of \(p\ge0\) at depth \(i\ge1\) is \(\pi(p)=\lfloor p/2\rfloor\).

*Variable positions.* For depth \(i<h\), each node \(p\) has two row blocks \(R_i^-(p),R_i^+(p)\) and two column blocks \(C_i^-(p),C_i^+(p)\), each of \(m/2^i\) positions. A leaf \(p\) (depth \(h\)) has a single row position and a single column position, each with two names:
\[
R_h^-(p)=R_h^+(p),\qquad C_h^-(p)=C_h^+(p).
\]
All other blocks are disjoint. For \(\sigma\in\{-,+\}\) let \(R_i^\sigma\) and \(C_i^\sigma\) be the unions over \(p\) of the blocks at depth \(i\) (each has \(m\) positions), and for \(1\le i\le h\) and \(d\in\{0,1\}\) let \(R_{i,d}^\sigma\), \(C_{i,d}^\sigma\) be the unions over the nodes \(p\equiv d\pmod2\).

*Order of variable positions.* Rows are ordered recursively: for an internal node, first its minus block, then the positions of the subtree of child \(2p\), then those of child \(2p+1\), then its plus block; a leaf contributes its single position. Columns use the same recursion with the signs exchanged: plus block, the two subtrees, minus block. Within a block any fixed order is used. For disjoint sets \(X,Y\) on the same axis, \(X<Y\) means that every position of \(X\) precedes every position of \(Y\).

**Lemma 3.1.** For \(1\le i\le h\), nodes \(p,q\) at depth \(i\) and nodes \(a,b\) at depth \(i-1\):
\[
R_i^+(p)<R_{i-1}^+(a)\iff\pi(p)\le a,\qquad R_{i-1}^-(a)<R_i^-(p)\iff\pi(p)\ge a,
\]
\[
C_{i-1}^+(b)<C_i^+(q)\iff\pi(q)\ge b,\qquad C_i^-(q)<C_{i-1}^-(b)\iff\pi(q)\le b .
\]

*Proof.* The recursion places the subtrees of the nodes at depth \(i-1\) consecutively, in increasing order of the node, each subtree occupying an interval of positions that begins with the minus row block (plus column block) of its root and ends with its plus row block (minus column block). A block of the child \(p\) lies inside the interval of its parent \(\pi(p)\), strictly between the parent's two blocks; this holds also for a leaf. Hence \(R_i^+(p)\) precedes \(R_{i-1}^+(a)\) exactly when the subtree of \(\pi(p)\) does not come after that of \(a\), that is, \(\pi(p)\le a\); and \(R_{i-1}^-(a)\) precedes \(R_i^-(p)\) exactly when \(a\le\pi(p)\). The column statements are the same with the signs exchanged. \(\square\)

*Dummy positions.* A dummy row block \(R_*\) and a dummy column block \(C_*\) of \(m\) positions each are placed after all variable rows and before all variable columns, respectively.

*Modes.* For \(1\le i\le h\) and \(d\in\{0,1\}\) there are six *modes* \(V_i^+,V_i^-,W_{i,0}^+,W_{i,1}^+,W_{i,0}^-,W_{i,1}^-\), \(6h\) in all. Each mode \(t\) designates two row sets \(\mathsf R_1(t),\mathsf R_2(t)\) and two column sets \(\mathsf C_1(t),\mathsf C_2(t)\):

| mode \(t\) | \(\mathsf R_1(t)\) | \(\mathsf R_2(t)\) | \(\mathsf C_1(t)\) | \(\mathsf C_2(t)\) |
|---|---|---|---|---|
| \(V_i^+\) | \(R_i^+\) | \(R_{i-1}^+\) | \(C_*\) | \(C_{i-1}^+\) |
| \(V_i^-\) | \(R_{i-1}^-\) | \(R_i^-\) | \(C_*\) | \(C_{i-1}^-\) |
| \(W_{i,d}^+\) | \(R_{i,d}^+\) | \(R_*\) | \(C_{i-1}^+\) | \(C_{i,d}^+\) |
| \(W_{i,d}^-\) | \(R_{i,d}^-\) | \(R_*\) | \(C_{i,d}^-\) | \(C_{i-1}^-\) |

In each mode the two row sets are disjoint, and so are the two column sets. A *body in mode \(t\)* consists of rows \(r_1<r_2\) and columns \(c_1<c_2\) with \(r_j\in\mathsf R_j(t)\) and \(c_j\in\mathsf C_j(t)\).

*Anchor positions.* Order the modes by increasing \(i\), and at each depth as listed above. Before all other positions on each axis, place for each mode \(t\), in this order, \(s\) consecutive *anchor groups* \(\widehat R_t(1),\dots,\widehat R_t(s)\) of rows and \(\widehat C_t(1),\dots,\widehat C_t(s)\) of columns, each of \(m\) positions.

Each axis thus consists of \(6hs\) anchor groups, the dummy block, \(2h\) classes \(R_i^\sigma\) (or \(C_i^\sigma\)) with \(i<h\), and one class of leaves, each of size \(m\). Hence each axis has
\[
n=d_hm\quad\text{positions},\qquad d_h=6hs+2h+2=386h+2 ,
\]
identified with \([n]\) in the order just described.

## 4. The host matrices

The entries of \(A_h\in\{0,1\}^{n\times n}\) are given by three rules.

1. *Anchor against anchor.* Between \(\widehat R_t(u)\) and \(\widehat C_{t'}(v)\) the entry is \(S(u,v)\) if \(t=t'\) and \(0\) if \(t\ne t'\).
2. *Signatures.* A non-anchor row \(r\) has, against the groups \(\widehat C_t(1),\dots,\widehat C_t(s)\) of a mode \(t\), the values of \(e_j^{\mathsf T}\) if \(r\in\mathsf R_j(t)\) (\(j=1,2\)), and zeros if \(r\) lies in neither set. Symmetrically, a non-anchor column \(c\) has, against \(\widehat R_t(1),\dots,\widehat R_t(s)\), the values of \(e_j\) if \(c\in\mathsf C_j(t)\), and zeros otherwise.
3. *Non-anchor entries.* An entry in a dummy row or a dummy column, between non-anchor positions, is \(1\). Between variable positions the entries are
\[
\begin{array}{ccc|c}
\text{row}&\text{column}&\text{depths}&\text{entry}\\ \hline
R_i^+(p)&C_i^+(q)&0\le i\le h&\mathbf 1[p\le q]\\
R_i^-(p)&C_i^-(q)&0\le i<h&\mathbf 1[p<q]\\
R_i^+(p)&C_{i-1}^+(q)&1\le i\le h&\mathbf 1[\pi(p)\le q]\\
R_i^-(p)&C_{i-1}^-(q)&1\le i\le h&\mathbf 1[\pi(p)<q]
\end{array}
\]
and \(0\) in every other case.

The rules are consistent: the first two table lines concern different pairs of blocks because the second excludes the leaves, and in the last two lines the column is not a leaf, so its sign is determined. Thus the entry between leaves \(p,q\) is \(\mathbf 1[p\le q]\). Every rule depends only on the blocks or groups containing the row and the column, so two positions of one anchor group, or of one dummy block, have identical entries throughout \(A_h\).

The design can be read as follows. At the root, \(A_h(R_0^+,C_0^+)=1\) and \(A_h(R_0^-,C_0^-)=0\). The \(V\) modes compare consecutive row depths through (2.1), with dummy columns supplying the ones in the first column of the body; the \(W\) modes compare consecutive column depths, with dummy rows supplying the second row of the body. At the leaves the plus and minus positions coincide, so a matrix that respected all these comparisons along one path from the root would need the value \(1\) and the value \(0\) in the same cell. The third lesson turns this into a lower bound for the distance, and the second shows that the only copies of \(H\) in \(A_h\) itself sit at the leaves.

## 5. Exercises

**5.1.** Show that the rows of \(H\) are pairwise distinct and that \(H\) is not \(H'\)-free for \(H'=P\), that is, \(H\) contains an ordered copy of \(P\).

**5.2.** For \(h=1\), list the variable rows and the variable columns of \(A_1\) in their order, and write down the \(4\times4\) matrix of entries between the variable blocks \(R_0^-(0),R_1(0),R_1(1),R_0^+(0)\) (rows) and \(C_0^+(0),C_1(0),C_1(1),C_0^-(0)\) (columns), where \(R_1(p)\) and \(C_1(p)\) are the leaves.

**5.3.** Check the four equivalences of Lemma 3.1 for \(h=2\), \(i=2\), \(p=3\) and \(a\in\{0,1\}\).

## 6. Solutions

**5.1.** The rows of \(S\) are distinct (Lemma 1.1 of [Every copy meets the leaf diagonal](every-copy-meets-the-leaf-diagonal.md)); the last two rows of \(H\) begin with \(e_1^{\mathsf T}\) and \(e_2^{\mathsf T}\), which differ from each other and from the rows of \(S\), each of which has at least \(58\) ones. The last two rows and columns of \(H\) form \(P\).

**5.2.** For \(h=1\), \(m=2\): the variable rows are \(R_0^-(0)\) (two positions), the leaves \(R_1(0)\), \(R_1(1)\), and \(R_0^+(0)\) (two positions); the variable columns are \(C_0^+(0)\), the leaves \(C_1(0)\), \(C_1(1)\), and \(C_0^-(0)\). By the table: \(R_0^-\) against \(C_0^-\) gives \(\mathbf 1[0<0]=0\), and \(0\) against \(C_0^+\) and the leaves. The leaf \(R_1(p)\) against \(C_0^+(0)\) gives \(\mathbf 1[0\le0]=1\), against \(C_1(q)\) gives \(\mathbf 1[p\le q]\), and against \(C_0^-(0)\) gives \(\mathbf 1[0<0]=0\). \(R_0^+\) against \(C_0^+\) gives \(1\), and \(0\) against the leaves and \(C_0^-\). In block form, with rows \(R_0^-,R_1(0),R_1(1),R_0^+\) and columns \(C_0^+,C_1(0),C_1(1),C_0^-\):
\[
\begin{pmatrix}0&0&0&0\\1&1&1&0\\1&0&1&0\\1&0&0&0\end{pmatrix}.
\]

**5.3.** Here \(\pi(3)=1\). The leaf \(3\) lies in the subtree of node \(1\), after the subtree of node \(0\). For \(a=0\): \(R_2^+(3)\) comes after \(R_1^+(0)\), consistent with \(\pi(3)=1>0\); and \(R_1^-(0)<R_2^-(3)\), consistent with \(1\ge0\). For \(a=1\): \(R_2^+(3)<R_1^+(1)\) because the plus block of node \(1\) closes its subtree, consistent with \(1\le1\); and \(R_1^-(1)<R_2^-(3)\), consistent with \(1\ge1\). The column statements follow in the same way with the signs exchanged.

## References

- [OpenAI-OM] OpenAI, *Polynomial removal fails for ordered binary matrices*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/blob/main/preprints/Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026/paper.pdf
- [AB] N. Alon and O. Ben-Eliezer, *Efficient removal lemmas for matrices*, Order (2020); preprint 2016. https://arxiv.org/abs/1609.04235
- [ABF] N. Alon, O. Ben-Eliezer and E. Fischer, *Testing hereditary properties of ordered graphs and matrices*, FOCS 2017; full version. https://arxiv.org/abs/1704.02367
- [GS] L. Gishboliner and A. Shapira, *Polynomial property testing*, 2025. https://arxiv.org/abs/2508.16878
