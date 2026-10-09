# Distance from freeness

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[Every copy meets the leaf diagonal](every-copy-meets-the-leaf-diagonal.md) showed that the matrix \(A_h\) of [Ordered copies and tree matrices](ordered-copies-and-tree-matrices.md) has few ordered copies of \(H\). This lesson shows that \(A_h\) is nevertheless far from \(H\)-free: every \(H\)-free binary matrix differs from \(A_h\) in at least \(m^2\) cells (Proposition 1.1). The idea is to choose at random one root-to-leaf path of the tree, the same on both axes, together with one position in each anchor group and in each dummy block. If fewer than \(m^2\) cells were changed, some choice would leave every chosen anchor, dummy and root entry unchanged. Then the anchors and dummies of each mode, through the facts (2.1) of the first lesson, force the plus entries along the path to stay \(1\) and the minus entries to stay \(0\), down to a leaf where plus and minus are the same cell. Notation is that of the first lesson; \(m=2^h\) and \(n=d_hm\) with \(d_h=386h+2\).

## 1. The distance bound

**Proposition 1.1.** Every \(H\)-free binary \(n\times n\) matrix \(B\) differs from \(A=A_h\) in at least \(m^2\) cells. Hence \(\operatorname{dist}_H(A_h)\ge m^2/n^2=d_h^{-2}\).

*Proof.* Let \(B\) be a binary matrix differing from \(A\) on a set \(E\) of fewer than \(m^2\) cells. We show that \(B\) contains an ordered copy of \(H\).

*A random choice of positions.* On each axis, the positions are partitioned into *classes* of \(m\) positions: the \(6hs\) anchor groups, the dummy block, the classes \(R_i^\sigma\) (or \(C_i^\sigma\)) for \(i<h\) and \(\sigma=\pm\), and the class of leaves, counted once. Choose \(z\in\{0,\dots,m-1\}\) uniformly, and let \(a_i=\lfloor z/2^{h-i}\rfloor\) for \(0\le i\le h\); thus \(a_i\) is the ancestor of the leaf \(z\) at depth \(i\), and \(\pi(a_i)=a_{i-1}\). Given \(z\), choose independently and uniformly
\[
x_i^\sigma\in R_i^\sigma(a_i),\qquad y_i^\sigma\in C_i^\sigma(a_i)\qquad(0\le i<h,\ \sigma=\pm),
\]
let \(x_h=x_h^+=x_h^-\) and \(y_h=y_h^+=y_h^-\) be the leaf positions of \(z\), and choose, independently of everything else, one uniform position in every anchor group and \(x_*\in R_*\), \(y_*\in C_*\).

Every position \(r\) of a class is chosen with probability \(1/m\): for a variable position of depth \(i\), the node \(a_i\) equals the node of \(r\) with probability \(2^{-i}\), and then \(r\) is chosen with probability \(2^i/m\). Call a cell \((r,c)\) *protected* if \(r\) or \(c\) is an anchor or dummy position, or if both lie in blocks of depth \(0\). For a protected cell, the events "\(r\) is chosen" and "\(c\) is chosen" are independent: an anchor or dummy choice is independent of all choices on the other axis, and the depth-\(0\) choices are independent uniform choices in fixed blocks, since \(a_0=0\). Hence a protected cell has both its row and its column chosen with probability \(1/m^2\). Each class contributes exactly one chosen position, so by the union bound
\[
\Pr\bigl(\text{some protected cell with chosen row and column lies in }E\bigr)\le\frac{|E|}{m^2}<1 .
\]
Fix a choice for which no protected cell with chosen row and column lies in \(E\). On all such cells \(B\) agrees with \(A\); all other cells are unrestricted.

*What a mode forbids.* Fix a mode \(t\). Its chosen anchor rows and columns, one per group, give a copy of \(S\) in \(B\), because their entries are protected and equal \(S(u,v)\) in \(A\). They precede all non-anchor positions. A chosen non-anchor row in \(\mathsf R_j(t)\) has, against the chosen anchor columns of \(t\), the protected entries \(e_j^{\mathsf T}\), and symmetrically for columns in \(\mathsf C_j(t)\). Hence every body of mode \(t\) formed by chosen positions whose four entries in \(B\) are \(P\) completes these anchors to an ordered copy of \(H\) in \(B\). Assume, for a contradiction, that \(B\) is \(H\)-free; then no such body is \(P\).

*Propagation along the path.* The depth-\(0\) entries are protected, so
\[
B(x_0^+,y_0^+)=A(x_0^+,y_0^+)=\mathbf 1[0\le0]=1,\qquad B(x_0^-,y_0^-)=\mathbf 1[0<0]=0 .
\]
We show by induction on \(i\) that
\[
B(x_i^+,y_i^+)=1\qquad\text{and}\qquad B(x_i^-,y_i^-)=0\qquad(0\le i\le h). \tag{1.1}
\]
Let \(1\le i\le h\) and assume (1.1) at depth \(i-1\). Entries in the dummy row \(x_*\) or the dummy column \(y_*\) against chosen non-anchor positions are protected and equal \(1\). By Lemma 3.1 of the first lesson, with \(\pi(a_i)=a_{i-1}\), all the following quadruples are bodies of the stated modes.

- Mode \(V_i^+\), rows \(x_i^+<x_{i-1}^+\), columns \(y_*<y_{i-1}^+\): the entries are \(\begin{pmatrix}1&B(x_i^+,y_{i-1}^+)\\1&1\end{pmatrix}\). By (2.1) of the first lesson, avoiding \(P\) forces \(B(x_i^+,y_{i-1}^+)=1\).
- Mode \(V_i^-\), rows \(x_{i-1}^-<x_i^-\), columns \(y_*<y_{i-1}^-\): the entries are \(\begin{pmatrix}1&0\\1&B(x_i^-,y_{i-1}^-)\end{pmatrix}\), which forces \(B(x_i^-,y_{i-1}^-)=0\).
- Mode \(W_{i,d}^+\) with \(d=a_i\bmod2\), rows \(x_i^+<x_*\), columns \(y_{i-1}^+<y_i^+\): the entries are \(\begin{pmatrix}1&B(x_i^+,y_i^+)\\1&1\end{pmatrix}\), using the value just obtained, which forces \(B(x_i^+,y_i^+)=1\).
- Mode \(W_{i,d}^-\), rows \(x_i^-<x_*\), columns \(y_i^-<y_{i-1}^-\): the entries are \(\begin{pmatrix}B(x_i^-,y_i^-)&0\\1&1\end{pmatrix}\), which forces \(B(x_i^-,y_i^-)=0\).

This proves (1.1). At depth \(h\), the two statements of (1.1) concern the single cell \((x_h,y_h)\), which cannot be both \(1\) and \(0\). Hence \(B\) contains a copy of \(H\). \(\square\)

## 2. The theorem

**Theorem 2.1** (OpenAI 2026). Let \(H\) be the \(66\times66\) pattern of the first lesson. For every \(h\ge1\), with \(n_h=(386h+2)2^h\) and \(\epsilon_h=(386h+2)^{-2}\), the matrix \(A_h\) is \(\epsilon_h\)-far from \(H\)-freeness and satisfies \(N_H(A_h)\le\epsilon_h2^{-h}n_h^{132}\).

*Proof.* Proposition 1.1 gives the distance, and Proposition 3.1 of [Every copy meets the leaf diagonal](every-copy-meets-the-leaf-diagonal.md) gives \(N_H(A_h)/n_h^{132}\le2^{-h}d_h^{-2}=\epsilon_h2^{-h}\). \(\square\)

**Corollary 2.2.** Conjecture 1.1 of the first lesson fails for this \(H\): for all \(c,C>0\) there are \(n\), \(0<\epsilon<1\) and an \(n\times n\) binary matrix \(A\), \(\epsilon\)-far from \(H\)-freeness, with \(N_H(A)<c\,\epsilon^Cn^{132}\).

*Proof.* For \(A=A_h\), \(\epsilon=\epsilon_h\), Theorem 2.1 gives \(N_H(A_h)/(\epsilon_h^Cn_h^{132})\le(386h+2)^{2C-2}2^{-h}\), which tends to \(0\) as \(h\to\infty\). Choose \(h\) with this quantity below \(c\). \(\square\)

**Corollary 2.3** (Sampling rows and columns). Fix \(h\ge1\) and \(0\le q\le n_h\). Choose a uniformly random \(q\)-element set \(R\) of rows and, independently, a uniformly random \(q\)-element set \(C\) of columns. The probability that the submatrix \(A_h[R,C]\), with the inherited orders, contains an ordered copy of \(H\) is at most \(\epsilon_h2^{-h}q^2\), and it is \(0\) when \(q<66\). In particular, a probability at least \(\rho>0\) requires \(q\ge\sqrt\rho\,(386h+2)2^{h/2}\), which grows exponentially in \(\epsilon_h^{-1/2}=386h+2\).

*Proof.* A copy in \(A_h[R,C]\) is a copy in \(A_h\), so by Proposition 3.1 of the previous lesson \(R\times C\) contains a cell of \(\mathcal L_h\). A fixed cell lies in \(R\times C\) with probability \((q/n_h)^2\), and \(|\mathcal L_h|=2^h\), so the probability is at most \(2^h(q/n_h)^2=\epsilon_h2^{-h}q^2\). For \(q<66\) the submatrix is too small. Rearranging gives the bound on \(q\). \(\square\)

Fischer and Rozenberg, and Alon and Ben-Eliezer [AB], had earlier constructed super-polynomial examples for matrices over three symbols. In contrast, Alon and Ben-Eliezer proved polynomial bounds when \(A\) contains many copies of \(H\) with pairwise disjoint sets of entries [AB]. Remark 3.2 of the previous lesson shows how both statements fit with Theorem 2.1: the copies of \(H\) in \(A_h\) all meet a set of only \(2^h\) cells, while every \(H\)-free repair changes at least \(4^h\) cells.

## 3. Exercises

**3.1.** Check that each of the four quadruples in the propagation step is a body of the stated mode: identify the designated sets and verify the two order conditions with Lemma 3.1 of the first lesson.

**3.2.** Show that a protected cell is needed in the union bound: give a cell \((r,c)\) of two variable positions of depth \(1\) for which the probability that both \(r\) and \(c\) are chosen exceeds \(1/m^2\), and explain why such cells may be changed freely in the proof.

**3.3.** Show that Theorem 2.1 already gives, for \(h=1\), a matrix of order \(776\) at distance at least \(388^{-2}\) from \(H\)-freeness with at most \(388^{-2}2^{-1}\cdot776^{132}\) copies of \(H\), and compare with the trivial bound \(\binom{776}{66}^2\).

## 4. Solutions

**3.1.** \(V_i^+\): \(x_i^+\in R_i^+=\mathsf R_1\), \(x_{i-1}^+\in R_{i-1}^+=\mathsf R_2\), and \(x_i^+<x_{i-1}^+\) because \(\pi(a_i)\le a_{i-1}\); \(y_*\in C_*\) precedes all variable columns. \(V_i^-\): \(x_{i-1}^-<x_i^-\) because \(\pi(a_i)\ge a_{i-1}\). \(W_{i,d}^+\): \(x_i^+\in R_{i,d}^+\) since \(a_i\equiv d\), dummy rows come last, and \(y_{i-1}^+<y_i^+\) because \(\pi(a_i)\ge a_{i-1}\). \(W_{i,d}^-\): \(y_i^-\in C_{i,d}^-\) and \(y_i^-<y_{i-1}^-\) because \(\pi(a_i)\le a_{i-1}\).

**3.2.** Let \(r\in R_1^+(0)\) and \(c\in C_1^+(0)\). Both are chosen exactly when \(a_1=0\), which has probability \(1/2\), and the two positions are then chosen with probability \((2/m)^2\); the product is \(2/m^2>1/m^2\). The two choices are dependent through \(z\). The proof never uses the original value of such a cell: the propagation determines the needed values from the protected cells and from the assumption that \(B\) is \(H\)-free.

**3.3.** For \(h=1\): \(d_1=388\), \(m=2\), \(n_1=776\), \(\epsilon_1=388^{-2}\), and \(N_H(A_1)\le388^{-2}2^{-1}776^{132}\). The trivial bound \(\binom{776}{66}^2\) is smaller than \(776^{132}/(66!)^2\), so for \(h=1\) Theorem 2.1 says little; its force lies in the factor \(2^{-h}\) as \(h\) grows, against the polynomial factor \(\epsilon_h^{C}=(386h+2)^{-2C}\).

## References

- [OpenAI-OM] OpenAI, *Polynomial removal fails for ordered binary matrices*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/blob/main/preprints/Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026/paper.pdf
- [AB] N. Alon and O. Ben-Eliezer, *Efficient removal lemmas for matrices*, Order (2020); preprint 2016. https://arxiv.org/abs/1609.04235
