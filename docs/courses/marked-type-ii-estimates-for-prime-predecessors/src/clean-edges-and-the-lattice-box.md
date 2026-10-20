# Clean edges and the lattice box

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An edge operation is **clean** if it stores no label and promotes no particle: the memory passes through unchanged, and every new label is drawn freshly. This lesson proves that the clean part of every edge has operator norm at most \(L^{-G}\), for any prescribed \(G\), once the major arcs are defined with a large enough exponent \(A_0\). The source of cancellation is the minor-arc kernel: after the shared labels are fixed, the positions of an edge lie in a two-dimensional lattice, the edge sees them only through a determinant, and on a balanced box the matrix \(e(\vartheta\det(\mathbf h,\mathbf l))\) has small norm when \(\vartheta\) is far from fractions with small denominators. Test (G1) of the good positions is what keeps the box balanced.

**Prerequisites.** [*Truncation, adjoints and absolute bounds*](truncation-adjoints-and-absolute-bounds.md), Sections 2 and 4; [*Physical states and good positions*](physical-states-and-good-positions.md), Definition 3.1; [*Cauchy's inequality and the determinant equation*](cauchys-inequality-and-the-determinant-equation.md), Section 5; [*From the moment to the pairing*](from-the-moment-to-the-pairing.md), Lemma 2.1.

The archimedean root is fixed, positions are written in root coordinates \(z\), and \(\tau(z)\in[\frac1{16},16]\) on the box. For a vector \(z\) we fix \(w_z\) with \(\det(z,w_z)=1\) and put \(r_z^*=\tau(w_z)/\tau(z)\), a real lift of the ratio of the position \(gz\).

## 1. Removing the cross-edge ban

The clean piece \(\mathcal E_j^{\rm cl}\) of \(\mathcal E_j\) is the piece \(S=I=\varnothing\) of Lemma 2.4 of Lesson 13. In it, the cross-edge ban couples the new labels with the dropped ones; its other restrictions are conditions on the source state or on the target state alone. Let \(\mathcal E_j^{\rm cl,0}\) be the operation obtained by replacing the ban with the condition that the target's full lists have distinct entries.

**Lemma 1.1.** \(\|\mathcal E_j^{\rm cl}-\mathcal E_j^{\rm cl,0}\|\le4KL^{C_e}e^{-L^{0.1}}\) on \(\mathscr H_B\).

**Proof.** The difference consists of the choices in which, in some group \(i\), the fresh label equals the dropped source label \(p_{i,M}\). For each group this prescribes one fresh prime value, whose measure is at most \(\max\nu_i\le4e^{-L^{0.1}}\) by Lemma 2.1 of Lesson 12. The crude bound with fixed fresh values (Lemma 4.1 of Lesson 13) bounds the weighted row sums by \(L^{C_e}\cdot4e^{-L^{0.1}}\) for each group, and the same holds for the column sums, since the adjoint is the same kind of piece with the roles of the two labels exchanged. Lemma 2.1 of Lesson 13 finishes the proof. \(\square\)

## 2. Cells, line tuples and blocks

In \(\mathcal E_j^{\rm cl,0}\) the shared labels and the memory are copied unchanged. Fix them; in particular the shared product \(D\in[d_0,2d_0)\) is fixed. The operation acts on the remaining variables: the position and the last slot of each list, which together are an ordered tuple of one prime per group, determined by its product. Write \(b\) for the product at the source and \(a\) at the target.

For two vectors \(z,z'\),

\[
\begin{gathered}
\frac{z'_2}{\tau(z')}-\frac{z_2}{\tau(z)}=\frac{\det(z,z')}{\tau(z)\tau(z')}.\quad(2.1)
\end{gathered}
\]

Divide the vectors into **cells** according to the integer part of \(z_2/(\tau(z)H)\). On the support of the multiplier \(|\det(z,z')|\le10H\) (Lemma 2.1 of Lesson 9), so by (2.1) an edge changes the cell index by at most \(2561\). An edge also preserves the **line tuple** \(([z]_p)_{p\mid D}\): if \(p\mid D\), then \(p\mid\det(z,z')\), and two primitive vectors with determinant divisible by \(p\) have the same line modulo \(p\). Hence \(\mathcal E_j^{\rm cl,0}\), with \(D\) and the memory fixed, is a sum over at most \(5123\) cell shifts of operators that are direct sums of **blocks**: a block maps the vectors of one cell with one line tuple to those of a shifted cell with the same tuple. It suffices to bound every block.

**Lemma 2.1 (the lattice).** Let \(z_*\) be a vector in the source cell of a block and \(w_*=w_{z_*}\). Every primitive vector with the line tuple of \(z_*\) lies in \(\Lambda=\mathbb Zz_*+\mathbb ZDw_*\). Writing such a vector as \(z=hz_*+lDw_*\),

\[
\begin{gathered}
\det(z,z')=D\,(hl'-lh'),\\
\frac{\tau(z)}{\tau(z_*)}=h+l\alpha,\quad\alpha=Dr^*_{z_*},\quad(2.2)
\end{gathered}
\]

and the vectors of the block satisfy \(|l|\le7\cdot10^5\,Y\) and \(|h+l\alpha|\le16\).

**Proof.** Write \(z=hz_*+jw_*\). For \(p\mid D\), \([z]_p=[z_*]_p\) means that \(z\) is a multiple of \(z_*\) modulo \(p\), that is \(p\mid j\); since \(D\) is squarefree, \(D\mid j\). The determinant formula follows from \(\det(z_*,w_*)=1\), and the formula for \(\tau\) from linearity. The vectors of the block lie in cells at most \(2562\) apart from that of \(z_*\), so \(|\det(z_*,z)|\le256\cdot2563H\) by (2.1); and \(\det(z_*,z)=lD\) with \(D\ge d_0\), \(H=d_0Y\). Finally \(\tau(z)/\tau(z_*)\in[\frac1{16},16]\), because the first coordinates \(u\tau(z)\) and \(u\tau(z_*)\) of the two positions lie in \([U,16U]\). \(\square\)

## 3. A balanced box

**Lemma 3.1.** Suppose some source state of the block is good. Then there are integer coordinates \((c_1,c_2)\) on \(\Lambda\), related to \((h,l)\) by a matrix in \(\mathrm{SL}_2(\mathbb Z)\), such that \(\det(z,z')=D(c_1c'_2-c_2c'_1)\) and all vectors of the block satisfy \(|c_1|\le A'\), \(|c_2|\le B'\), where

\[
\begin{gathered}
A'B'\le C_0Y,\\
Y^{0.1}\le A',B'\le Y^{0.9},\quad(3.1)
\end{gathered}
\]

with an absolute constant \(C_0\), for large \(x\).

**Proof.** Let \(z_*\) be the position of a good source state. Consider the lattice

\[
\begin{gathered}
\Gamma=\{(h+l\alpha,\ l/Y):\ (h,l)\in\mathbb Z^2\}\subset\mathbb R^2,
\end{gathered}
\]

of covolume \(1/Y\). By Lemma 2.1 the vectors of the block correspond to points of \(\Gamma\) in the box \(\mathcal R_0=[-16,16]\times[-7\cdot10^5,7\cdot10^5]\). Let \(\lambda\) be the length of a shortest nonzero vector of \(\Gamma\).

*Lower bound.* If \(\lambda<Y^{-0.8}\), a vector \((h+l\alpha,l/Y)\) of that length has \(|l|<Y^{0.2}\), and \(l\ne0\), since otherwise \(|h|<1\) forces \(h=0\). Then \(\|l\alpha\|\le|h+l\alpha|<Y^{-0.7}\). Since \(\alpha=Dr_{z_*}^*\) and \(r^*_{z_*}\) is a lift of the ratio of the position, \(\|l\alpha\|=\|lDr_{gz_*}\|\). The source states of the block have \(D\) as an omission product (omit the last slots), so test (G1) at the good state forbids this, with \(|l|\) in place of \(l\). Hence \(\lambda\ge Y^{-0.8}\).

*Upper bound.* By Dirichlet's approximation theorem there is \(1\le l\le Q=\lceil Y^{1/2}\rceil\) with \(\|l\alpha\|\le1/Q\). Taking \(h\) with \(|h+l\alpha|=\|l\alpha\|\) gives a vector of length at most \((Q^{-2}+Q^2Y^{-2})^{1/2}\le\sqrt5\,Y^{-1/2}\). So \(\lambda\le\sqrt5\,Y^{-1/2}\).

*The basis.* A shortest vector \(v_1\) is primitive in \(\Gamma\); complete it to a basis \(v_1,v_2\), replace \(v_2\) by \(v_2-mv_1\) so that its component along \(v_1\) has modulus at most \(\lambda/2\), and replace \(v_2\) by \(-v_2\) if needed so that the change of coordinates from \((h,l)\) has determinant \(+1\). The component of \(v_2\) orthogonal to \(v_1\) has length \(\gamma=1/(Y\lambda)\), since the covolume is \(1/Y\). A point \(c_1v_1+c_2v_2\) of \(\mathcal R_0\) has length at most \(R_0=8\cdot10^5\); its orthogonal component gives \(|c_2|\le R_0/\gamma=R_0Y\lambda\), and its component along \(v_1\) gives \(|c_1|\lambda\le R_0+|c_2|\lambda/2\), so \(|c_1|\le R_0/\lambda+R_0Y\lambda\le6R_0/\lambda\), because \(Y\lambda^2\le5\). Take \(A'=6R_0/\lambda\) and \(B'=R_0Y\lambda\). Then \(A'B'=6R_0^2Y\), and the bounds on \(\lambda\) give \(A'\in[R_0Y^{0.5},6R_0Y^{0.8}]\) and \(B'\in[R_0Y^{0.2},3R_0Y^{0.5}]\), which implies (3.1) for large \(Y\). The determinant identity holds because the coordinate change is unimodular, by (2.2). \(\square\)

If no source state of the block is good, the block vanishes, since the edge requires a good source.

## 4. The determinant matrix on a box

For real \(\vartheta\) and \(A',B'\ge1\) let \(T(\vartheta)\) be the matrix \((e(\vartheta hk))\) with rows \(|h|\le A'\) and columns \(|k|\le B'\).

**Lemma 4.1.** If \(|\vartheta-c/d|\le1/d^2\) with \((c,d)=1\) and \(d\ge1\), then

\[
\begin{aligned}
\|T(\vartheta)\|^2&\le C\Bigl(\frac{A'}d+1\Bigr)\\
&\quad\times\bigl(B'+d\log(2d)\bigr).\quad(4.1)
\end{aligned}
\]

**Proof.** The entries of \(TT^*\) are \(\sum_{|k|\le B'}e(\vartheta(h-h')k)\), of modulus at most \(\min(2B'+1,1/\|(h-h')\vartheta\|)\). By the Schur test for this Hermitian matrix,
\[
\begin{aligned}
\|T\|^2&\le\max_h\sum_{h'}|(TT^*)_{hh'}|\\
&\le\sum_{|n|\le2A'}\min(2B'+1,1/\|n\vartheta\|).
\end{aligned}
\]
Split the range of \(n\) into at most \(8A'/d+3\) intervals of length at most \(d/2\). Two different \(n,n'\) in one interval satisfy \(0<|n-n'|<d\), so \((n-n')c/d\) is a nonzero multiple of \(1/d\) modulo \(1\), and \(|(n-n')(\vartheta-c/d)|\le\frac d2\cdot\frac1{d^2}=\frac1{2d}\); hence \(\|n\vartheta-n'\vartheta\|\ge\frac1{2d}\). The points \(n\vartheta\bmod1\) of one interval are thus \(\frac1{2d}\)-separated. An arc of length \(\frac1{4d}\) contains at most one of them, so for every \(k\ge0\) at most two of them satisfy \(k/(4d)\le\|n\vartheta\|<(k+1)/(4d)\). The two possible terms with \(k=0\) contribute at most \(2(2B'+1)\), and the others at most \(\sum_{1\le k\le2d}2\cdot4d/k\le8d(1+\log2d)\). So each interval contributes \(O(B'+d\log2d)\). \(\square\)

The determinant matrix \(e(\vartheta(h_1l_2-h_2l_1))\), with rows \((h_1,h_2)\) and columns \((l_1,l_2)\) in the box \(|\cdot_1|\le A'\), \(|\cdot_2|\le B'\), is the tensor product of \(T(\vartheta)\) (indices \(h_1,l_2\)) and the transpose of \(\overline{T(\vartheta)}\) (indices \(h_2,l_1\)), up to a reordering of the columns. Its norm is therefore \(\|T(\vartheta)\|^2\).

## 5. The clean bound

**Theorem 5.1.** For every fixed \(G>0\), if \(A_0\ge G+2\), then for large \(x\) and every \(j\),

\[
\begin{gathered}
\|\mathcal E_j^{\rm cl}\|_{\mathscr H_B\to\mathscr H_B}\le L^{-G}.\quad(5.1)
\end{gathered}
\]

**Proof.** By Lemma 1.1 it suffices to bound \(\mathcal E_j^{\rm cl,0}\), and by Section 2 to bound one block, with \(D\) and the memory fixed. We treat a forward edge; a reversed edge has the conjugate transposed kernel and the same bound.

*Reduction to counting measure.* The last slots carry the measure \(m(b)=\prod_i\nu_i(p_i)\). Since \(\nu_i(p)\le1.01\mu_i(p)\), \(V_i\ge\frac12\) and \(b\ge Y\) on the support of \(\eta(b/Y)\), \(m(b)\le C_K/Y\). Conjugating by multiplication with \(\sqrt m\) maps the block isometrically to an operator on counting measure with kernel \(\sqrt{m(b)m(a)}\) times the original kernel, and \(\sqrt{m(b)m(a)}=(C_K/Y)\theta(b)\theta(a)\) with \(0\le\theta\le1\). The original kernel is

\[
\begin{gathered}
\rho^{h(z)}\rho^{h(z')}\frac{d_0}D\eta\Bigl(\frac bY\Bigr)\eta\Bigl(\frac aY\Bigr)\psi\Bigl(\frac tY\Bigr)\\
\times\int_{\mathbb T\setminus\mathfrak M}e\bigl(\theta(t-b+a)\bigr)d\theta,
\end{gathered}
\]

times the indicators of the source and target restrictions, with \(t=c_1c_2'-c_2c_1'\) by Lemma 3.1. Every factor other than \(\psi(t/Y)\int_{\mathbb T\setminus\mathfrak M}\cdots\) is a function of the source or of the target alone, of modulus at most \(1\). Extending the positions to all integer points of the box of Lemma 3.1 and the products \(a,b\) to all integers can only increase the norm. So the block has norm at most \(C_K\|\mathcal O\|\), where \(\mathcal O\) acts on functions of \((\mathbf l,a)\) in the box times \(\mathbb Z\) with kernel

\[
\begin{gathered}
\frac1Y\psi\Bigl(\frac{\det(\mathbf h,\mathbf l)}Y\Bigr)\\
\times\int_{\mathbb T\setminus\mathfrak M}e\bigl(\theta(\det(\mathbf h,\mathbf l)-b+a)\bigr)d\theta .
\end{gathered}
\]

*Diagonalization in the labels.* The kernel depends on \(a\) and \(b\) only through \(e(\theta(a-b))\). Under the unitary map \(\phi\mapsto\sum_ae(\theta a)\phi(\cdot,a)\) from \(\ell^2(\mathbb Z)\) to \(L^2(\mathbb T)\), \(\mathcal O\) becomes multiplication, in \(\theta\in\mathbb T\setminus\mathfrak M\), by the matrices \(\mathcal O_\theta=\frac1Y\psi(\det/Y)e(\theta\det)\) on the box. Hence \(\|\mathcal O\|\le\sup_{\theta\notin\mathfrak M}\|\mathcal O_\theta\|\).

*The cutoff.* Write \(\psi(y)=\int_{\mathbb R}\widehat\psi(u)e(uy)\,du\) with \(\widehat\psi\) rapidly decreasing. Then \(\mathcal O_\theta=\int\widehat\psi(u)\frac1Y(e(\vartheta\det(\mathbf h,\mathbf l)))\,du\) with \(\vartheta=\theta+u/Y\). For \(|u|>L^{A_0}/2\), use the trivial bound \((2A'+1)(2B'+1)\le9C_0Y\) for the norm (the maximal row sum); these \(u\) contribute \(O_k(L^{-kA_0})\) for every \(k\).

*Minor arcs.* Let \(|u|\le L^{A_0}/2\) and \(Q=\lceil Y/L^{A_0}\rceil\). Dirichlet's theorem gives a reduced fraction \(c/d\) with \(1\le d\le Q\) and \(|\vartheta-c/d|\le1/(dQ)\le1/d^2\). If \(d\le L^{A_0}\), then \(\|\theta-c/d\|\le1/(dQ)+|u|/Y\)\(\le\frac32L^{A_0}/Y\), so \(\theta\in\mathfrak M\), which is excluded. Hence \(L^{A_0}<d\le Q\). By Lemma 4.1 and the tensor structure,

\[
\begin{aligned}
&\frac1Y\bigl\|e(\vartheta\det)\bigr\|\\
&\quad\le\frac CY\Bigl(\frac{A'}d+1\Bigr)\bigl(B'+d\log2d\bigr)\\
&\quad\le C\Bigl(\frac{C_0}d+\frac{\log2Y}{Y^{0.1}}\\
&\qquad+\frac{2\log2Y}{L^{A_0}}\Bigr),
\end{aligned}
\]

using \(A'B'\le C_0Y\), \(A',B'\le Y^{0.9}\) and \(d\log2d\le Q\log2Q\le2YL^{-A_0}\log2Y\). Since \(1/d<L^{-A_0}\) and \(\log2Y\le3KL^{0.2}\), this is \(O_K(L^{0.2-A_0})\).

Collecting the factors \(C_K\), the \(5123\) cell shifts and Lemma 1.1, \(\|\mathcal E_j^{\rm cl}\|\le C_KL^{0.2-A_0}+O(L^{-A_0k})\le L^{-G}\) for large \(x\) when \(A_0\ge G+2\). The clean piece does not change the memory, so it commutes with \(\Pi_B\). \(\square\)

The constant \(C_K\) depends on \(K\), but the exponent \(0.2-A_0\) does not: the clean bound buys any power of \(L\) by enlarging \(A_0\), before \(K\) is chosen.

## 6. Exercises

**14.1.** Prove the identity (2.1).

**14.2.** Show that for a squarefree \(D\) and a primitive \(z_*\), the primitive vectors \(z\) with \([z]_p=[z_*]_p\) for all \(p\mid D\) are exactly the primitive vectors of \(\mathbb Zz_*+\mathbb ZDw_*\).

**14.3.** State and prove Dirichlet's approximation theorem: for real \(\alpha\) and an integer \(Q\ge1\) there is \(1\le l\le Q\) with \(\|l\alpha\|\le1/(Q+1)\).

**14.4.** Show that \(\|A\otimes B\|=\|A\|\,\|B\|\) for matrices \(A,B\).

**14.5.** Compute \(\|T(0)\|\) and explain why the clean bound fails at \(\theta=0\), which lies in \(\mathfrak M\).

## 7. Solutions

**14.1.** \(z_2'\tau(z)-z_2\tau(z')\)\(=z_2'z_1+rz_2'z_2-z_2z_1'-rz_2z_2'\)\(=\det(z,z')\). Divide by \(\tau(z)\tau(z')\).

**14.2.** Lemma 2.1 gives one inclusion. Conversely, if \(z=hz_*+lDw_*\) is primitive, then modulo \(p\mid D\) it is \(hz_*\) with \(p\nmid h\) (otherwise \(p\) divides \(z\)), so \([z]_p=[z_*]_p\).

**14.3.** The \(Q+2\) numbers \(0,1\) and the fractional parts of \(l\alpha\), \(1\le l\le Q\), lie in \([0,1]\); divide it into \(Q+1\) intervals of length \(1/(Q+1)\). Two of the numbers lie in one interval. Their difference is \(\pm(l-l')\alpha\) or \(l\alpha\) minus an integer, with \(1\le|l-l'|\le Q\) (or \(1\le l\le Q\)), at distance at most \(1/(Q+1)\) from an integer.

**14.4.** \((A\otimes B)^*(A\otimes B)=A^*A\otimes B^*B\), whose largest eigenvalue is the product of the largest eigenvalues of \(A^*A\) and \(B^*B\).

**14.5.** \(T(0)\) is the all-ones matrix of size \((2\lfloor A'\rfloor+1)\times(2\lfloor B'\rfloor+1)\), of norm \(\sqrt{(2\lfloor A'\rfloor+1)(2\lfloor B'\rfloor+1)}\asymp\sqrt Y\). The determinant matrix then has norm of order \(Y\), and after division by \(Y\) there is no saving. On the major arcs the kernel has no cancellation of this kind; Lesson 17 treats them by a different argument.

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Section 4.5. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
