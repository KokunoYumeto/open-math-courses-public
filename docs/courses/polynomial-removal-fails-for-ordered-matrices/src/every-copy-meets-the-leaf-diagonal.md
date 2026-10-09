# Every copy meets the leaf diagonal

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson counts the ordered copies of the pattern \(H\) in the matrix \(A_h\) of [Ordered copies and tree matrices](ordered-copies-and-tree-matrices.md), whose notation is used throughout. The anchor \(S\) is dense in its first \(32\) rows and columns, while variable positions see few anchor groups; this forces the \(64\times64\) part of every copy into the anchor groups of a single mode. The last two rows and columns of the copy must then form a body of that mode, and the order relations of the tree leave a body equal to \(P\) only at a diagonal leaf cell. Hence all copies pass through one of only \(m=2^h\) cells (Proposition 3.1).

## 1. Three properties of the positions

**Lemma 1.1** (The anchor). The rows of \(S\) are pairwise distinct, and so are its columns. Every column of \(S\) has at most one zero among its first \(32\) entries, and every row has at most one zero among its first \(32\) entries. Every row has at least \(58\) ones and every column at least \(48\). The restrictions of rows \(33,\dots,64\) to columns \(60,\dots,64\) are the \(32\) binary words of length five.

*Proof.* The word block occupies rows \(33\) to \(64\) and columns \(60\) to \(64\), so it meets neither the first \(32\) rows nor the first \(59\) columns. In the first \(59\) columns, row \(u\le59\) has its only zero in column \(u\), and rows \(60,\dots,64\) have no zero. Hence rows \(1,\dots,59\) are distinct from each other and from rows \(60,\dots,64\), which are distinct from each other because their words are. Each row has at least \(58\) ones. Each of the first \(59\) columns has exactly one zero, in its own row. Each of the last five columns has no zero in rows \(1,\dots,32\) and exactly \(16\) zeros in the word block, since each binary digit vanishes for half of the \(32\) words; it therefore has \(48\) ones, differs from the first \(59\) columns, and differs from the other four of the last five columns because distinct digits of the word list differ. The remaining claims are visible from the definition. \(\square\)

**Lemma 1.2** (Few modes per variable position). Every variable position belongs to designated sets of at most four modes. Consequently, against a set of positions on the other axis that contains at most one position of each anchor group, a variable position has at most four entries equal to \(1\).

*Proof.* From the table of modes: a row of \(R_i^\sigma(p)\) with \(i<h\) can only be designated by \(V_i^\sigma\), \(V_{i+1}^\sigma\) and \(W_{i,d}^\sigma\) with \(d=p\bmod2\) (modes with depth outside \(1,\dots,h\) do not exist); a leaf row only by \(V_h^+\), \(V_h^-\), \(W_{h,d}^+\), \(W_{h,d}^-\). A column of \(C_i^\sigma(p)\) with \(i<h\) can only be designated by \(V_{i+1}^\sigma\), \(W_{i+1,0}^\sigma\), \(W_{i+1,1}^\sigma\) and \(W_{i,d}^\sigma\); a leaf column only by \(W_{h,d}^+\) and \(W_{h,d}^-\). By the signature rule, the entries of the position against the anchor groups of a designating mode form one unit vector, and against all other anchor groups they vanish. \(\square\)

A set of columns is *shattered* by a set of rows if the restrictions of these rows to the columns include all binary words of the corresponding length.

**Lemma 1.3** (Non-anchor positions shatter no five columns). No five distinct non-anchor columns of \(A_h\) are shattered by the non-anchor rows.

*Proof.* A dummy column has entry \(1\) in every non-anchor row, so a set containing one is not shattered. Let the five columns be variable, and group them into the classes \(C_i^\sigma\) (\(i<h\)) and the class of leaves. Within a class, order the chosen columns by their node index. By the table of entries, a variable row has, within each class, either no ones or ones exactly at the chosen columns whose node index passes a threshold; these sets of columns are *suffixes* of the class. Columns in one block have identical entries, so ties do not matter. A row of depth \(i<h\) has ones in at most two classes (its own class and the class of the same sign at depth \(i-1\)); a leaf row in at most three (the leaves and the two classes at depth \(h-1\)).

A class with \(a\) chosen columns has at most \(a\) distinct nonempty suffixes, so all classes together have at most \(5\) nonempty suffixes, and the trace of a variable row on the five columns is the union of at most three of them. Hence variable rows produce at most \(\binom50+\binom51+\binom52+\binom53=26\) traces. The dummy rows produce one more, the all-ones word. Since \(27<32\), the five columns are not shattered. \(\square\)

## 2. The anchor part of a copy

**Lemma 2.1** (Anchor rigidity). Every ordered copy of \(S\) in \(A_h\) uses, on each axis, exactly one position from each of the \(64\) anchor groups of one mode \(t\), in the order of the groups.

*Proof.* Two positions of one anchor group have identical entries throughout \(A_h\). By Lemma 1.1 the rows of \(S\) are distinct, and so are its columns, so a copy uses at most one position of each anchor group, and for the same reason at most one dummy position on each axis.

*More than \(32\) anchors on some axis.* Otherwise at most \(32\) of the \(64\) chosen rows, and at most \(32\) of the chosen columns, are anchors. Anchors precede all other positions, so the last \(32\) chosen rows and the last five chosen columns are non-anchor positions. By Lemma 1.1, these rows realize all \(32\) words on these five columns, contrary to Lemma 1.3.

*Case of more than \(32\) anchor rows.* Then the first \(32\) chosen rows are anchors. A chosen variable column would have at most four ones against them (Lemma 1.2), but every column of \(S\) has at least \(31\) ones among its first \(32\) entries. So no chosen column is variable, at most one is dummy, and at least \(63\) are anchors. Two chosen anchor columns have a common one in the first \(32\) chosen rows, since each has at most one zero there; an anchor row has ones only against anchor columns of its own mode, so the two columns belong to the same mode, say \(t\). An anchor row of a mode other than \(t\) would have at most one one in the copy (it vanishes against the \(63\) anchor columns of \(t\)), while every row of \(S\) has at least \(58\); so all chosen anchor rows belong to \(t\). A chosen dummy column would have, against the anchor rows of \(t\), the entries of a unit vector or of zero, hence at most one one among the first \(32\) chosen rows, which is again too few. So all \(64\) chosen columns are anchors of \(t\). A non-anchor row has at most one one against them, so all chosen rows are anchors of \(t\) as well.

*Case of more than \(32\) anchor columns.* The same argument applies with rows and columns exchanged: all properties used (zeros between different modes, at most one zero in the first \(32\) entries of each row and column of \(S\), more than one one in every row and column of \(S\), Lemma 1.2 on both axes) are symmetric.

In both cases \(64\) positions are chosen on each axis from the \(64\) groups of \(t\), at most one per group, so every group is used once, and the increasing order of the copy follows the order of the groups. \(\square\)

**Corollary 2.2** (Body roles). In every ordered copy of \(H\) in \(A_h\), the first \(64\) rows and columns use the anchor groups of one mode \(t\) as in Lemma 2.1, the two last rows lie in \(\mathsf R_1(t)\) and \(\mathsf R_2(t)\) respectively, and the two last columns lie in \(\mathsf C_1(t)\) and \(\mathsf C_2(t)\).

*Proof.* The first \(64\) rows and columns form a copy of \(S\), so Lemma 2.1 applies. Row \(64+j\) of the copy has entries \(e_j^{\mathsf T}\) against the \(64\) anchor columns of \(t\). An anchor row of another mode has zeros there, and an anchor row of \(t\) gives a row of \(S\), with many ones; so row \(64+j\) is a non-anchor row, and by the signature rule it lies in \(\mathsf R_j(t)\). The columns are treated in the same way. \(\square\)

## 3. Locating all copies

Let
\[
\mathcal L_h=\bigcup_{p=0}^{m-1}R_h^+(p)\times C_h^+(p)
\]
be the set of the \(m\) *diagonal leaf cells*.

**Proposition 3.1.** Every ordered copy of \(H\) in \(A_h\) maps the entry \((65,65)\) of \(H\) to a cell of \(\mathcal L_h\). Consequently
\[
N_H(A_h)\le m\,n^{130},\qquad\frac{N_H(A_h)}{n^{132}}\le\frac{2^{-h}}{d_h^2}.
\]

*Proof.* By Corollary 2.2, the last two rows \(r_1<r_2\) and columns \(c_1<c_2\) of a copy form a body in some mode \(t\), and their entries must be \(P\). We use Lemma 3.1 and the table of entries of the previous lesson.

*Mode \(V_i^+\).* Here \(r_1\in R_i^+(p)\), \(r_2\in R_{i-1}^+(a)\), \(c_1\) dummy and \(c_2\in C_{i-1}^+(b)\). The order \(r_1<r_2\) gives \(\pi(p)\le a\); the entry \(1\) at \((r_2,c_2)\) gives \(a\le b\). Then \(\pi(p)\le b\), so the entry at \((r_1,c_2)\) is \(1\), not \(0\).

*Mode \(V_i^-\).* Here \(r_1\in R_{i-1}^-(a)\), \(r_2\in R_i^-(p)\), \(c_2\in C_{i-1}^-(b)\). The order gives \(\pi(p)\ge a\); the entry \(0\) at \((r_1,c_2)\) gives \(a\ge b\). Then \(\pi(p)\ge b\), so the entry at \((r_2,c_2)\) is \(\mathbf 1[\pi(p)<b]=0\), not \(1\).

*Mode \(W_{i,d}^+\).* Here \(r_1\in R_i^+(p)\), \(r_2\) dummy, \(c_1\in C_{i-1}^+(b)\), \(c_2\in C_i^+(q)\), with \(p\equiv q\equiv d\pmod2\). The order \(c_1<c_2\) gives \(b\le\pi(q)\), and the entry \(1\) at \((r_1,c_1)\) gives \(\pi(p)\le b\). So \(\pi(p)\le\pi(q)\), and with equal parities \(p=2\pi(p)+d\le2\pi(q)+d=q\). The entry at \((r_1,c_2)\) is then \(\mathbf 1[p\le q]=1\), not \(0\).

*Mode \(W_{i,d}^-\).* Here \(r_1\in R_i^-(p)\), \(r_2\) dummy, \(c_1\in C_i^-(q)\), \(c_2\in C_{i-1}^-(b)\), with \(p\equiv q\equiv d\). The order gives \(\pi(q)\le b\), and the entry \(0\) at \((r_1,c_2)\) gives \(\pi(p)\ge b\); hence \(p\ge q\). If \(i<h\), the entry at \((r_1,c_1)\) is \(\mathbf 1[p<q]=0\), not \(1\). If \(i=h\), the positions are leaves and this entry is \(\mathbf 1[p\le q]\), which equals \(1\) only for \(p=q\). Then \((r_1,c_1)\in\mathcal L_h\), and \((r_1,c_1)\) is the image of the entry \((65,65)\) of \(H\).

Each leaf block has one position, so \(|\mathcal L_h|=m\). Once the images of row \(65\) and column \(65\) are fixed, there are at most \(n^{65}\) choices for the other rows and at most \(n^{65}\) for the other columns, which gives \(N_H(A_h)\le mn^{130}\). Dividing by \(n^{132}=d_h^2m^2\,n^{130}\) gives the second bound. \(\square\)

**Remark 3.2.** Changing the \(m\) cells of \(\mathcal L_h\) from \(1\) to \(0\) destroys every copy of \(H\) in \(A_h\), but creates new ones. For a leaf \(p\) with \(d=p\bmod2\), take in mode \(W_{h,d}^+\) the leaf row \(p\) and a dummy row, and the columns \(c_1\in C_{h-1}^+(\pi(p))\) and \(c_2\) the leaf column \(p\), which satisfy \(c_1<c_2\) by Lemma 3.1 of the previous lesson. After the change, their body is \(\begin{pmatrix}1&0\\1&1\end{pmatrix}\): the entry \(\mathbf 1[\pi(p)\le\pi(p)]=1\) is unchanged, the changed leaf diagonal entry is \(0\), and the dummy row gives ones. One position from each anchor group of this mode completes a copy of \(H\). So a small set of cells meeting all copies need not yield an \(H\)-free matrix after editing; [Distance from freeness](distance-from-freeness.md) shows that every \(H\)-free matrix differs from \(A_h\) in at least \(m^2\) cells.

## 4. Exercises

**4.1.** Show that \(A_h\) is not \(H\)-free: for a leaf \(p\) with \(d=p\bmod2\), find a body equal to \(P\) in mode \(W_{h,d}^-\), and complete it to a copy of \(H\).

**4.2.** Explain why Lemma 1.3 needs the dummy rows to contribute only one trace, and check that \(26+1<32\) is the inequality used.

**4.3.** Show that the order conditions in the definition of a body cannot be dropped. For \(h\ge2\), find rows \(r_1\in R_2^+\), \(r_2\in R_1^+\) with \(r_2<r_1\), a dummy column \(c_1\) and a column \(c_2\in C_1^+\) such that the entries of \(A_h\) in rows \(r_1,r_2\) and columns \(c_1,c_2\) form \(P\).

## 5. Solutions

**4.1.** Take \(r_1\) the leaf row \(p\) (it lies in \(R_{h,d}^-\)), \(r_2\) a dummy row, \(c_1\) the leaf column \(p\) (in \(C_{h,d}^-\)) and \(c_2\in C_{h-1}^-(\pi(p))\). By Lemma 3.1 of the previous lesson, \(c_1<c_2\) because \(\pi(p)\le\pi(p)\), and \(r_1<r_2\) because dummy rows come last. The entries are \(\mathbf 1[p\le p]=1\) at \((r_1,c_1)\), \(\mathbf 1[\pi(p)<\pi(p)]=0\) at \((r_1,c_2)\), and \(1\) in the dummy row. Choosing one position of each anchor group of \(W_{h,d}^-\) gives the copy of \(S\), and the signature rule gives the entries \(e_j\) and \(e_j^{\mathsf T}\).

**4.2.** All dummy rows coincide, and against non-anchor columns they are all ones, so together they produce exactly one trace. The variable rows produce at most \(26\), so at most \(27\) of the \(32\) words occur.

**4.3.** Take \(r_1\in R_2^+(2)\), \(r_2\in R_1^+(0)\) and \(c_2\in C_1^+(0)\). The block \(R_1^+(0)\) closes the subtree of node \(0\), and the node \(2\) lies in the subtree of node \(1\), which comes later, so \(r_2<r_1\). The entries are \(1\) in the dummy column, \(\mathbf 1[\pi(2)\le0]=0\) at \((r_1,c_2)\) and \(\mathbf 1[0\le0]=1\) at \((r_2,c_2)\), so rows \(r_1,r_2\) and columns \(c_1,c_2\) give \(\begin{pmatrix}1&0\\1&1\end{pmatrix}=P\). With the rows in this order they do not form a body of \(V_2^+\).

## References

- [OpenAI-OM] OpenAI, *Polynomial removal fails for ordered binary matrices*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/blob/main/preprints/Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026/paper.pdf
