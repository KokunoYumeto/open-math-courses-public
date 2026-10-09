# Two energy estimates

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

We continue the proof by contradiction of [Lipschitz sheets and a lexicographic maximum](lipschitz-sheets-and-a-lexicographic-maximum.md): \(f:S\to\mathbb R^k\) satisfies (2.1) there, and \(K\), \(A\), \(B\) are defined by its sheets. Near a good point where the derivative columns of a sheet \(F\) have squared lengths close to \((A,B)\), we add one coordinate \(re_{j,i}\) at a fresh fine level \(j\) and obtain new sheets \(F_1,\dots,F_N\), each within \(Dr\) of \(F\) on its strips. This lesson shows that their derivatives are close to that of \(F\) in mean square, in a rectangle \(Q\) tiled by period blocks of the strips at level \(j\) (Proposition 2.1) [OpenAI-L, Section 4]. Two features of the strips are used: a horizontal strip of colour \(i\) crosses the whole rectangle, so \(F_i-F\) can be integrated along its full width; and the vertical strips of level \(j\) are \(n\) times wider than the horizontal ones, so that integrating across one of them already gives an error of order \(1/n\). The horizontal estimate comes with the factor \(n^2\), which the lesson [Crossings and the Lang–Plaut problem](crossings-and-the-lang-plaut-problem.md) needs because the horizontal lines it uses are \(n\) times longer than the vertical ones.

We use Lemmas 1.1, 1.2, 3.1 and 4.1 of [Lipschitz sheets and a lexicographic maximum](lipschitz-sheets-and-a-lexicographic-maximum.md), the set \(S\), the strips and the sheets of [Doubling spaces and coloured strips](doubling-spaces-and-coloured-strips.md), and Fubini's theorem for bounded measurable functions on rectangles (core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10), Fremlin, *Measure Theory*, Volume 2, 251N and 252B).

## 1. Choices

The map \(f\), the numbers \(k\), \(D\), \(A\), \(B\) and the set \(K\) are fixed. Fix an integer
\[
N>(1+2D)^k.\tag{1.1}
\]
Let \(n\) be a positive integer. All the following choices depend on \(n\).

*A near-extremal sheet.* Since \((A,B)\in K\) lies in the closure of the pairs given by good points, there are a sheet \(F=F_w\) and a good point \(p_0\) of \(F\) with \(u=F_x(p_0)\), \(v=F_y(p_0)\) and
\[
0\le A-\|u\|^2<n^{-4},\qquad\bigl|B-\|v\|^2\bigr|<n^{-4};\tag{1.2}
\]
the first difference is nonnegative by the definition of \(A\). Since \(p_0\) is good and \(\Omega_w\) is open, there is a closed square \(Q^0\) of side \(l\), centred at \(p_0\) and contained in \(\Omega_w\), with
\[
\bigl\langle\|F_x-u\|^2+\|F_y-v\|^2\bigr\rangle_{Q^0}<n^{-8}.\tag{1.3}
\]

*A fresh level.* Every pair of positive integers occurs infinitely often in the sequence \((N_j,W_j)\), so there is a level \(j\), larger than every level where \(w\) is nonzero, with
\[
(N_j,W_j)=(N,n),\qquad Nnr_j<\tfrac1{100}\,l\,n^{-8}.\tag{1.4}
\]
Put \(r=r_j\). The horizontal strips of level \(j\) have height \(r\) and their colours repeat with period \(Nr\); the vertical strips have width \(nr\) and their colours repeat with period \(Nnr\). A *period block* is a rectangle \([aNnr,(a+1)Nnr]\times[bNr,(b+1)Nr]\), \(a,b\in\mathbb Z\). It contains exactly one horizontal strip (a *row*) and one vertical strip (a *column*) of each colour.

*The rectangle.* Let \(Q\) be the union of the period blocks contained in \(Q^0\), a closed rectangle with sides \(L_x\) and \(L_y\). Trimming \(Q^0\) to the grid of blocks loses less than one period at each end, so \(L_x\ge l-2Nnr\ge l/2\) and \(L_y\ge l/2\). Hence \(|Q|\ge|Q^0|/4\), and with (1.3) and (1.4),
\[
\bigl\langle\|F_x-u\|^2+\|F_y-v\|^2\bigr\rangle_Q<4n^{-8},\qquad\frac r{L_x},\ \frac r{L_y}<\frac{n^{-9}}{50N}.\tag{1.5}
\]

*The new sheets.* For \(1\le i\le N\), let \(F_i\) be the sheet of the sequence obtained from \(w\) by putting \(re_{j,i}\) at level \(j\). Its domain is \(\Omega_w\cap U_{j,i}\), which contains the rows and the columns of colour \(i\) inside \(Q^0\). The two points of \(S\) behind \(F_i(p)\) and \(F(p)\) are at distance \(r\), so by (2.1) of [Lipschitz sheets and a lexicographic maximum](lipschitz-sheets-and-a-lexicographic-maximum.md)
\[
\|F_i-F\|\le Dr\qquad\text{on }\Omega_w\cap U_{j,i}.\tag{1.6}
\]

*The selected fields.* Off the boundaries of the strips (a null set), define on \(Q\): \(G_H^x=(F_i)_x\), where \(i\) is the colour of the row containing the point; and \(G_V^x=(F_i)_x\), \(G_V^y=(F_i)_y\), where \(i\) is the colour of the column containing the point. Good points of the finitely many sheets \(F,F_1,\dots,F_N\) have full measure, so almost everywhere on \(Q\)
\[
\|G_H^x\|^2\le A,\qquad\bigl(\|G_V^x\|^2,\|G_V^y\|^2\bigr)\in K.\tag{1.7}
\]

## 2. The estimates

**Proposition 2.1** (two energy estimates; OpenAI). With the choices of Section 1, averages over \(Q\) satisfy
\[
n^2\bigl\langle\|G_H^x-F_x\|^2\bigr\rangle\le2(1+4D)n^{-2}+\frac{4D^2}{25N}\,n^{-7}+8n^{-6},\tag{2.1}
\]
\[
\bigl\langle\|G_V^y-F_y\|^2\bigr\rangle\longrightarrow0\qquad(n\to\infty).\tag{2.2}
\]

**Proof.** *The row field.* A row of colour \(i\) meets \(Q\) in a horizontal band across the whole width of \(Q\). By Lemma 1.2 of [Lipschitz sheets and a lexicographic maximum](lipschitz-sheets-and-a-lexicographic-maximum.md), applied to the Lipschitz map \(F_i-F\) on \(\Omega_w\cap U_{j,i}\), for almost every height \(y\) in the band,
\[
\Bigl\|\int_{x_L}^{x_R}\bigl((F_i)_x-F_x\bigr)(x,y)\,dx\Bigr\|=\|(F_i-F)(x_R,y)-(F_i-F)(x_L,y)\|\le2Dr,
\]
where \(x_L,x_R\) are the ends of \(Q\); the end points lie in the domain because \(Q\subseteq\Omega_w\) and \(y\) lies in the open row, and (1.6) applies. The integrand is \(G_H^x-F_x\) almost everywhere in the band. Integrating over the heights and dividing by \(|Q|=L_xL_y\), \(\|\langle G_H^x-F_x\rangle\|\le2Dr/L_x\). By the Cauchy–Schwarz inequality and (1.5), \(\|\langle F_x\rangle-u\|\le\langle\|F_x-u\|^2\rangle^{1/2}<2n^{-4}\), so
\[
\|\langle G_H^x\rangle-u\|\le\frac{2Dr}{L_x}+2n^{-4}.\tag{2.3}
\]
Lemma 4.1 of that lesson, with \(\langle\|G_H^x\|^2\rangle\le A\) from (1.7), (1.2) and \(\|u\|\le D\), gives
\[
\bigl\langle\|G_H^x-u\|^2\bigr\rangle\le A-\|u\|^2+2D\|\langle G_H^x\rangle-u\|\le(1+4D)n^{-4}+\frac{4D^2r}{L_x}.
\]
Since \(\|G_H^x-F_x\|^2\le2\|G_H^x-u\|^2+2\|F_x-u\|^2\), (1.5) gives
\[
\bigl\langle\|G_H^x-F_x\|^2\bigr\rangle\le2(1+4D)n^{-4}+\frac{8D^2r}{L_x}+8n^{-8},
\]
and multiplying by \(n^2\) and using \(r/L_x<n^{-9}/(50N)\) gives (2.1).

*The column field, first column.* A column of colour \(i\) meets \(Q\) in a vertical band of width \(nr\), and \(Q\) is the union of \(L_x/(nr)\) such bands. For almost every height \(y\), Lemma 1.2 of that lesson applies to \(F_i-F\) on the open segment crossing the band at height \(y\), whose end points lie on the edges of the band; the continuous extension to the end points still satisfies (1.6), by continuity. So the integral of \(G_V^x-F_x\) across each band at height \(y\) has norm at most \(2Dr\). Adding over the \(L_x/(nr)\) bands and dividing by \(L_x\) gives at most \(2D/n\) for almost every \(y\). Hence, as above,
\[
\|\langle G_V^x\rangle-u\|\le\frac{2D}n+2n^{-4}.\tag{2.4}
\]
Let \(\eta_n=\langle A-\|G_V^x\|^2\rangle\), which is nonnegative by (1.7). By Lemma 4.1 of that lesson, whose left-hand side is nonnegative, \(\langle\|G_V^x\|^2\rangle\ge\|u\|^2-2\|u\|\,\|\langle G_V^x\rangle-u\|\), so
\[
0\le\eta_n\le A-\|u\|^2+2D\|\langle G_V^x\rangle-u\|\le(1+4D)n^{-4}+\frac{4D^2}n\longrightarrow0.
\]
Apply Lemma 3.1(b) of that lesson to the pairs \((\|G_V^x\|^2,\|G_V^y\|^2)\), which lie in \(K\) almost everywhere by (1.7), on \(Q\) with the normalized area measure:
\[
\limsup_{n\to\infty}\bigl\langle\|G_V^y\|^2\bigr\rangle\le B.\tag{2.5}
\]

*The column field, second column.* A column of colour \(i\) crosses \(Q\) from bottom to top. As for the rows, for almost every \(x\) in it the integral of \((F_i)_y-F_y\) along the vertical segment through \(Q\) has norm at most \(2Dr\), so \(\|\langle G_V^y-F_y\rangle\|\le2Dr/L_y\) and
\[
\|\langle G_V^y\rangle-v\|\le\frac{2Dr}{L_y}+2n^{-4}\longrightarrow0.\tag{2.6}
\]
By Lemma 4.1 of that lesson and \(\|v\|\le D\),
\[
0\le\bigl\langle\|G_V^y-v\|^2\bigr\rangle\le\bigl\langle\|G_V^y\|^2\bigr\rangle-\|v\|^2+2D\|\langle G_V^y\rangle-v\|.
\]
By (2.5), (1.2) and (2.6), the right-hand side has \(\limsup\) at most \(B-B+0=0\). So \(\langle\|G_V^y-v\|^2\rangle\to0\), and with \(\langle\|F_y-v\|^2\rangle<4n^{-8}\) this gives (2.2). \(\square\)

The vertical estimate has no rate: it comes from the compactness argument of Lemma 3.1 of [Lipschitz sheets and a lexicographic maximum](lipschitz-sheets-and-a-lexicographic-maximum.md), and it does not need the vectors \(v\) to converge. The order of the maximization in the definition of \((A,B)\) is what makes it work: the first column of the column field is forced towards the largest possible squared length \(A\), and then its second column cannot have a larger mean squared length than \(B\).

## 3. Exercises

**Exercise 3.1** (easy). Derive the inequalities \(L_x,L_y\ge l/2\) and \(r/L_x<n^{-9}/(50N)\) from (1.4).

**Exercise 3.2** (easy). Show that a period block contains exactly one row and one column of each colour, and that \(Q\) contains at least one period block.

**Exercise 3.3** (medium). Show that (2.1) remains true, with a right-hand side tending to \(0\), when \(n^2\) is replaced by \(n^{2+\gamma}\) for a fixed \(0\le\gamma<2\). Which term limits \(\gamma\)?

**Exercise 3.4** (medium). In the estimate (2.4), the integral was taken across each column separately. Explain why integrating \(G_V^x-F_x\) along the whole width of \(Q\) at once would not give a useful bound.

## 4. Solutions

**3.1.** \(2Nnr<\frac1{50}ln^{-8}\le l/2\), so \(L_x\ge l-2Nnr\ge l/2\), and likewise \(L_y\ge l-2Nr\ge l/2\). Then \(r/L_x\le2r/l<\frac2{100}\,n^{-8}/(Nn)=n^{-9}/(50N)\), and the same for \(L_y\).

**3.2.** The rows of level \(j\) in \([bNr,(b+1)Nr]\) are those with \(q=bN,\dots,bN+N-1\), whose colours run through all residues; similarly for columns. \(Q^0\) has side \(l>2Nnr\), so it contains a full period of the grid in each direction.

**3.3.** Multiplying the bound before (2.1) by \(n^{2+\gamma}\) gives \(2(1+4D)n^{\gamma-2}+\frac{4D^2}{25N}n^{\gamma-7}+8n^{\gamma-6}\). The first term, which comes from \(A-\|u\|^2<n^{-4}\) and \(\|\langle F_x\rangle-u\|<2n^{-4}\), needs \(\gamma<2\).

**3.4.** Along a horizontal line, \(G_V^x\) switches between the derivatives of different sheets \(F_i\) at the edges of the columns. Only within one column is it the derivative of a single map \(F_i-F\), whose increments are bounded by \(2Dr\) through (1.6).

## References

- [OpenAI-L] OpenAI, *A doubling Hilbert subset with no finite-dimensional bi-Lipschitz embedding*, OpenAI Math Release preprint, 25 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026
