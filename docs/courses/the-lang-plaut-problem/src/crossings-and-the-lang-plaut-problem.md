# Crossings and the Lang–Plaut problem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves OpenAI's negative answer to the question of Lang and Plaut [OpenAI-L, Section 5]:

**Theorem 3.1** (OpenAI). The subset \(S\) of the Hilbert space \(\ell^2\) constructed in [Doubling spaces and coloured strips](doubling-spaces-and-coloured-strips.md) is doubling with constant at most \(76800\) and admits no bi-Lipschitz embedding into \(\mathbb R^k\), for any \(k\) and any distortion.

The preceding lesson, [Two energy estimates](two-energy-estimates.md), produced sheets \(F,F_1,\dots,F_N\) of a supposed embedding whose derivatives agree with that of \(F\) in mean square on a rectangle \(Q\), with the factor \(n^2\) on the horizontal side. Here we pick one period block \(P\) of \(Q\), a horizontal line in the row of each colour and a vertical line in the column of each colour, along which the normalized offsets \(h_i=(F_i-F)/r\) are nearly constant. Where the row of colour \(i\) crosses the column of colour \(m\neq i\), both offsets are defined, and the embedding keeps them at distance at least \(\sqrt2\). Transporting along the lines, the \(N\) values \(h_i(x_i,y_i)\) are more than \(1\) apart and lie in a ball of radius \(D\) in \(\mathbb R^k\), which is impossible for \(N>(1+2D)^k\).

We use the choices (1.1)–(1.7) and Proposition 2.1 of [Two energy estimates](two-energy-estimates.md); Lemma 1.2 and (2.1) of [Lipschitz sheets and a lexicographic maximum](lipschitz-sheets-and-a-lexicographic-maximum.md); Lemma 1.1 and Proposition 3.1 of [Doubling spaces and coloured strips](doubling-spaces-and-coloured-strips.md); and, for Corollary 3.2, that the Euclidean unit sphere of \(\mathbb R^k\) is compact and a continuous real function on a compact set attains its minimum (core course [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20)).

## 1. Lines with small energy

Keep the notation of [Two energy estimates](two-energy-estimates.md) for a fixed \(n\). Let
\[
\mathcal E=n^2\|G_H^x-F_x\|^2+\|G_V^y-F_y\|^2\ge0
\]
on \(Q\). The rectangle \(Q\) is a union of congruent period blocks, so some period block \(P\subseteq Q\) satisfies \(\varepsilon_n:=\langle\mathcal E\rangle_P\le\langle\mathcal E\rangle_Q\). By Proposition 2.1 there, \(\varepsilon_n\to0\) as \(n\to\infty\). The block \(P\) has width \(Nnr\) and height \(Nr\), and contains one row and one column of each colour.

**Lemma 1.1** (lines). For each colour \(i\) there are a height \(y_i\) inside the row of colour \(i\) in \(P\) and an abscissa \(x_i\) inside the column of colour \(i\) in \(P\) such that, with \(h_i=(F_i-F)/r\) and
\[
\omega_n=N\sqrt{2N\varepsilon_n},
\]
the values of \(h_i\) on the horizontal segment of \(P\) at height \(y_i\) lie within \(\omega_n\) of each other, and so do the values of \(h_i\) on the vertical segment of \(P\) at abscissa \(x_i\).

**Proof.** In the row of colour \(i\), \(G_H^x-F_x=(F_i-F)_x\) almost everywhere, so \(\mathcal E\ge n^2\|(F_i-F)_x\|^2\) there. The row has area \(|P|/N\), so the average of \(n^2\|(F_i-F)_x\|^2\) over it is at most \(N\varepsilon_n\). By Fubini's theorem this average is the average over the heights \(y\) in the row of
\[
\Phi(y)=\frac1{Nnr}\int n^2\|(F_i-F)_x(x,y)\|^2\,dx,
\]
the integral along the horizontal segment of \(P\) at height \(y\). By Markov's inequality, \(\Phi(y)\le2N\varepsilon_n\) on a set of heights of positive measure (of full measure if \(\varepsilon_n=0\)). Choose \(y_i\) in it for which Lemma 1.2 of [Lipschitz sheets and a lexicographic maximum](lipschitz-sheets-and-a-lexicographic-maximum.md) applies to \(F_i-F\) at height \(y_i\); this excludes a null set of heights. The segment lies in the open row, inside \(\Omega_w\cap U_{j,i}\). For two points of it, at distance at most \(Nnr\), (1.2) of that lesson gives
\[
\|h_i(b)-h_i(a)\|\le\frac1r(Nnr)^{1/2}\Bigl(\frac{Nnr\cdot2N\varepsilon_n}{n^2}\Bigr)^{1/2}=N\sqrt{2N\varepsilon_n}.
\]
In the column of colour \(i\), \(G_V^y-F_y=(F_i-F)_y\) almost everywhere and \(\mathcal E\ge\|(F_i-F)_y\|^2\); in the same way there is \(x_i\) with \(\frac1{Nr}\int\|(F_i-F)_y(x_i,y)\|^2dy\le2N\varepsilon_n\) along the vertical segment of \(P\), whose length is \(Nr\), and then \(\|h_i(b)-h_i(a)\|\le\frac1r(Nr)^{1/2}(Nr\cdot2N\varepsilon_n)^{1/2}=N\sqrt{2N\varepsilon_n}\) for two of its points. \(\square\)

The factor \(n^2\) in the horizontal energy is exactly what compensates for the horizontal segments being \(n\) times longer than the vertical ones.

## 2. Crossings

Let \(z_i=h_i(x_i,y_i)\), the value at the point where the chosen lines of colour \(i\) meet; that point lies in the row and in the column of colour \(i\), so \(F_i\) is defined there, and \(\|z_i\|\le D\) by (1.6) of [Two energy estimates](two-energy-estimates.md).

**Lemma 2.1** (crossings). For \(i\neq m\), \(\|z_i-z_m\|\ge\sqrt2-2\omega_n\).

**Proof.** The point \(c=(x_m,y_i)\) lies in the row of colour \(i\) and in the column of colour \(m\), so both \(F_i\) and \(F_m\) are defined at \(c\). The points \((c,w+re_{j,i})\) and \((c,w+re_{j,m})\) of \(S\) are at distance \(\sqrt2\,r\), so by the lower bound in (2.1) of [Lipschitz sheets and a lexicographic maximum](lipschitz-sheets-and-a-lexicographic-maximum.md), \(\|F_i(c)-F_m(c)\|\ge\sqrt2\,r\), that is \(\|h_i(c)-h_m(c)\|\ge\sqrt2\). The points \(c\) and \((x_i,y_i)\) lie on the chosen horizontal segment of colour \(i\), so \(\|h_i(c)-z_i\|\le\omega_n\) by Lemma 1.1; the points \(c\) and \((x_m,y_m)\) lie on the chosen vertical segment of colour \(m\), so \(\|h_m(c)-z_m\|\le\omega_n\). \(\square\)

Nothing is assumed about differentiability at the crossing points: the lines control the values of \(h_i\) everywhere on them.

## 3. The theorem

**Proof of Theorem 3.1.** The doubling bound is Proposition 3.1 of [Doubling spaces and coloured strips](doubling-spaces-and-coloured-strips.md). The set \(S\) has more than one point, so it does not embed into \(\mathbb R^0\). Suppose \(f\) were a bi-Lipschitz embedding of \(S\) into \(\mathbb R^k\), \(k\ge1\), normalized as in (2.1) of [Lipschitz sheets and a lexicographic maximum](lipschitz-sheets-and-a-lexicographic-maximum.md), and make the choices of [Two energy estimates](two-energy-estimates.md) with \(N>(1+2D)^k\). Since \(\varepsilon_n\to0\), \(\omega_n\to0\), so for \(n\) large \(\sqrt2-2\omega_n\ge1\). Then by Lemma 2.1 the \(N\) points \(z_1,\dots,z_N\) lie in the closed ball of radius \(D\) about \(0\) in \(\mathbb R^k\) and have pairwise distances at least \(1\). Lemma 1.1 of [Doubling spaces and coloured strips](doubling-spaces-and-coloured-strips.md) gives \(N\le(1+2D)^k\), a contradiction. \(\square\)

**Corollary 3.2.** \(S\) admits no bi-Lipschitz embedding into any finite-dimensional real normed space.

**Proof.** Let \(Y\) be a real normed space of dimension \(k\ge1\) with basis \(b_1,\dots,b_k\), and \(T:\mathbb R^k\to Y\), \(T(c)=\sum_ic_ib_i\). By the triangle and Cauchy–Schwarz inequalities, \(\|Tc\|\le M\|c\|\) with \(M=(\sum_i\|b_i\|^2)^{1/2}\). Hence \(c\mapsto\|Tc\|\) is continuous, and it is positive on the Euclidean unit sphere because \(T\) is injective; as the sphere is compact, its minimum \(m\) there is positive, and \(\|Tc\|\ge m\|c\|\) for all \(c\). So \(T^{-1}:Y\to\mathbb R^k\) is bi-Lipschitz, and composing it with an embedding of \(S\) into \(Y\) would give an embedding of \(S\) into \(\mathbb R^k\), contradicting Theorem 3.1. For \(k=0\), \(Y\) is a single point, and \(S\) has more than one point. \(\square\)

**Remarks.** (1) The doubling constant of \(S\) is a fixed number, and \(S\) is a single set: the contradiction is reached for every \(k\) and \(D\) by levels \(j\) that come later and later in the fixed sequence \((N_j,W_j)\). Only the pair \((N,n)\) and the near-extremal sheet change with \(n\).

(2) The OpenAI preprint also shows that \(S\) is isometric to a subset of \(L_p[0,1]\) for every \(1\le p<\infty\), by a series of independent Gaussian variables, which answers the corresponding question for \(1<p<2\) left open by Lafforgue and Naor; and, using Dvoretzky's theorem on almost Euclidean finite-dimensional subspaces, that every infinite-dimensional Banach space contains a compact doubling subset, with a universal doubling bound, that admits no bi-Lipschitz embedding into a finite-dimensional normed space [OpenAI-L, Sections 6 and 7]. These two results are not proved in this course.

## 4. Exercises

**Exercise 4.1** (easy). Show that some period block \(P\subseteq Q\) satisfies \(\langle\mathcal E\rangle_P\le\langle\mathcal E\rangle_Q\).

**Exercise 4.2** (easy). In Lemma 2.1, check that the point \(c=(x_m,y_i)\) lies in the row of colour \(i\) and the column of colour \(m\), and that the two points of \(S\) used there are at distance \(\sqrt2\,r\).

**Exercise 4.3** (medium). Suppose the vertical strips at every level had the same width as the horizontal ones (\(W_j=1\) for all \(j\)). Which step of the proof of Proposition 2.1 of [Two energy estimates](two-energy-estimates.md) fails?

**Exercise 4.4** (medium). Show that, for a fixed finite subset of \(S\), an embedding into some \(\mathbb R^k\) always exists. Deduce that the obstruction of Theorem 3.1 cannot come from a single finite subset with a bounded number of points independent of \(k\) and \(D\).

## 5. Solutions

**4.1.** \(\langle\mathcal E\rangle_Q\) is the average of the block averages \(\langle\mathcal E\rangle_P\) over the blocks of \(Q\), which all have the same area; an average is at least the smallest of the averaged numbers.

**4.2.** \(y_i\) lies inside the row of colour \(i\) and \(x_m\) inside the column of colour \(m\), so \(c\) lies in both. The two points have the same base point and the same coordinates except at level \(j\), where they are \(re_{j,i}\) and \(re_{j,m}\), at distance \(\sqrt2\,r\).

**4.3.** The bound (2.4) there for the mean of the first column of the column field comes from integrating across single columns: an error of \(2Dr\) per column of width \(W_jr\), that is \(2D/W_j\) after averaging. With \(W_j=1\) this error does not tend to \(0\), so \(\eta_n\) need not tend to \(0\), Lemma 3.1(b) of [Lipschitz sheets and a lexicographic maximum](lipschitz-sheets-and-a-lexicographic-maximum.md) cannot be applied, and the vertical estimate (2.2) is lost. Wide columns force the first derivative column of the column sheets towards the largest squared length \(A\); the factor \(n^2\) in the horizontal estimate then compensates for the rows being \(n\) times longer than the columns are high.

**4.4.** A finite subset \(\{z_1,\dots,z_m\}\) of \(\mathcal H\) lies in the finite-dimensional span of its points, a Euclidean space of dimension at most \(m\); the inclusion is an isometric embedding. So any obstruction must use finite subsets whose number of points grows with \(k\) and \(D\), as the \(N\) points of the proof do.

## References

- [OpenAI-L] OpenAI, *A doubling Hilbert subset with no finite-dimensional bi-Lipschitz embedding*, OpenAI Math Release preprint, 25 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026
