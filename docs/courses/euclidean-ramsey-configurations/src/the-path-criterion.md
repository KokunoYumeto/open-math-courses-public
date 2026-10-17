# The path criterion

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson gives a sufficient condition for the Ramsey property in terms of products of scaled copies of the set in a free group. Combined with the two-scale configurations of [Two-scale configurations](two-scale-configurations.md), it proves the hard half of the classification in the next lesson. The proof colours words, applies [the Hales–Jewett theorem](the-hales-jewett-theorem.md), and evaluates free group products by strings through the group of [Ultrafilters and idempotents](ultrafilters-and-idempotents.md). The words of a monochromatic line differ only in their variable positions, and the number \(t\) of these positions is not known before the colouring is fixed; the construction therefore prepares, in advance, products of every weight \(1/t\) with \(t\) up to the length of the words. The group and word methods of Leader, Russell and Walters [LRW-T, Sections 2–3] are the model for this approach.

Throughout, \(A=\{a_1,\dots,a_s\}\) is a finite set in a Euclidean space with \(s\ge2\).

## 1. Paths in a free group

Let \(\mathcal E=\mathbb R^{(\mathbb N)}\) be the Euclidean space of real sequences with finitely many nonzero terms, and let \(K\) be the free group on symbols \(\xi_z\), one for each \(z\in\mathcal E\). For \(g\in K\) write \(\Delta g=(g,\dots,g)\in K^s\). A *path* is a finite sequence of factors in \(K^s\) of two kinds:

1. a *diagonal factor* \(\Delta g\), of weight \(0\);
2. a *copy factor* \(X_b=(\xi_{b_1},\dots,\xi_{b_s})\), where \(b_1,\dots,b_s\in\mathcal E\) and, for some \(u\ge0\), \(\|b_i-b_j\|^2=u\|a_i-a_j\|^2\) for all \(i,j\); its weight is \(u\).

The *endpoint* of a path is the product of its factors in \(K^s\), in their order, and its *weight* is the sum of the weights of its factors. The weight belongs to the path, not to the endpoint: two paths with the same endpoint can have different weights.

**Proposition 1.1** (path criterion). Suppose that for every integer \(n\ge1\) there are two paths with the same endpoint and weights \(\lambda>0\) and \(\mu\ge0\) with \(\mu/\lambda<1/n\). Then \(A\) is Ramsey.

## 2. Two reductions

**Lemma 2.1** (a finite dimension). Fix \(r\ge2\). If every \(r\)-colouring of \(\mathcal E\) is constant on some congruent copy of \(A\), then there is \(D\) such that every \(r\)-colouring of \(\mathbb R^D\) is constant on some congruent copy of \(A\).

*Proof.* Suppose instead that for every \(D\) there is an \(r\)-colouring \(c_D\) of \(\mathbb R^D\) constant on no copy; view \(\mathbb R^D\) as the sequences supported in the first \(D\) coordinates. Let \(\mathcal U\) be a nonprincipal ultrafilter on \(\mathbb N\) containing all cofinite sets (Section 1 of the previous lesson). A point \(z\in\mathcal E\) lies in \(\mathbb R^D\) for all \(D\ge D(z)\). The sets \(\{D\ge D(z):c_D(z)=j\}\), for \(j=1,\dots,r\), together with the finite set \(\{D<D(z)\}\), partition \(\mathbb N\); the finite set is not in \(\mathcal U\), so exactly one of the others is (Lemma 1.1(c) of the previous lesson). Let \(c(z)\) be that \(j\). For a copy \(b_1,\dots,b_s\) in \(\mathcal E\), the set of \(D\) with \(c_D(b_i)=c(b_i)\) for every \(i\) belongs to \(\mathcal U\), so it contains some \(D\ge\max_iD(b_i)\). Since \(c_D\) is not constant on the copy, neither is \(c\). So \(c\) is constant on no copy of \(A\) in \(\mathcal E\), a contradiction. \(\square\)

**Lemma 2.2** (synchronized weights). Fix \(n\ge1\). If two paths have the same endpoint and weights \(\lambda>0\) and \(\mu\ge0\) with \(\rho=\mu/\lambda<1/n\), then there is \(w\in K^s\) such that for every \(t=1,\dots,n\) some path of weight \(1/t\) has endpoint \(w\).

*Proof.* For \(\kappa>0\), the endomorphism of \(K\) with \(\xi_z\mapsto\xi_{\kappa z}\), applied in every coordinate of \(K^s\), sends diagonal factors to diagonal factors and a copy factor of weight \(u\) to a copy factor of weight \(\kappa^2u\), since \(\|\kappa b_i-\kappa b_j\|^2=\kappa^2u\|a_i-a_j\|^2\). It is a homomorphism, so two paths with equal endpoints keep equal endpoints. Put
\[
\alpha_t=\frac{1/t-\rho}{1-\rho}\qquad(1\le t\le n).
\]
Then \(0<\alpha_n<\alpha_{n-1}<\dots<\alpha_1=1\), because \(1/t\ge1/n>\rho\). These points divide \([0,1]\) into \(n\) intervals of positive length. For an interval of length \(l\), apply the endomorphism with \(\kappa=\sqrt{l/\lambda}\) to both paths; this gives two paths with a common endpoint and weights \(l\) and \(\rho l\). Concatenate, in the order of the intervals from left to right, one of the two paths for each interval. The endpoint \(w\) of the concatenation does not depend on these choices. For a given \(t\), choose the heavier path on the intervals inside \([0,\alpha_t]\) and the lighter one on the others; the weight is
\[
\alpha_t+\rho(1-\alpha_t)=\frac1t .\qquad\square
\]

## 3. Strings of points

Let \(\mathcal S\) be the monoid of finite strings of points of \(\mathcal E\), with concatenation; a one-letter string is written \((z)\). Choose linear isometric embeddings \(J_1,J_2,\dots:\mathcal E\to\mathcal E\) onto pairwise orthogonal coordinate blocks, for instance by sending the \(m\)th coordinate to the coordinate numbered \(2^{j-1}(2m-1)\). For a string \(x=(x_1,\dots,x_L)\) put
\[
\Phi(x)=\sum_{j=1}^LJ_jx_j\in\mathcal E .
\]
For two strings of the same length, orthogonality of the blocks gives
\[
\|\Phi(x)-\Phi(x')\|^2=\sum_{j=1}^L\|x_j-x'_j\|^2 .
\]

## 4. Proof of Proposition 1.1

Fix \(r\ge2\) and an \(r\)-colouring \(c\) of \(\mathcal E\). By Lemma 2.1 it suffices to find a congruent copy of \(A\) in \(\mathcal E\) on which \(c\) is constant.

*Preparation.* Let \(n=\mathrm{HJ}(s,r)\) be the length given by the Hales–Jewett theorem for the alphabet \([s]\) and \(r\) colours. By the hypothesis and Lemma 2.2, there is \(w=(w_1,\dots,w_s)\in K^s\) and, for every \(t\le n\), a path \(\Pi_t\) of weight \(1/t\) ending at \(w\). These choices are made before anything else.

*A group homomorphism.* Colour \(\mathcal S\) by \(c\circ\Phi\), with colour classes \(B_1,\dots,B_r\). Take the idempotent \(p\) and the group \(G=p(\beta\mathcal S)p\) of Proposition 2.2 of the previous lesson. Since \(K\) is free, there is a homomorphism
\[
\psi:K\to G,\qquad\psi(\xi_z)=p\,\delta_{(z)}\,p .
\]

*Colouring words.* Colour a word \(i_1\cdots i_n\in[s]^n\) by the unique \(k\) with
\[
B_k\in\psi(w_{i_1})\,\psi(w_{i_2})\cdots\psi(w_{i_n}),
\]
which exists by Lemma 1.1(c) of the previous lesson. By the choice of \(n\) there is a monochromatic combinatorial line, with variable word \(v\) and colour \(k\); let \(t\ge1\) be its number of variable positions. Its \(i\)th word \(v(i)\) has the letter \(i\) in every variable position.

*Expanding the products.* For the word \(v(i)\), the factor at a variable position is \(\psi(w_i)\). Write \(w_i\) as the product of the \(i\)th entries of the factors of \(\Pi_t\), and apply \(\psi\). A diagonal factor \(\Delta g\) contributes \(\psi(g)\), the same for every \(i\). A copy factor \(X_b\) contributes \(p\,\delta_{(b_i)}\,p\): two factors \(p\), the same for every \(i\), around the principal ultrafilter of the one-letter string \((b_i)\). The factor at a fixed position, with letter \(x\), is \(\psi(w_x)\), the same for every \(i\). Expanding every variable position in this way, the product for \(v(i)\) becomes a product of ultrafilters arranged in columns, the same arrangement for every \(i\), in which each column is either common to all \(i\) or principal at a one-letter string. Each of these products contains \(B_k\).

*Realization.* Lemma 3.1 of the previous lesson gives strings \(z^{(1)},\dots,z^{(s)}\in B_k\) obtained by concatenating, column by column, one common string in each common column and the letter \((b_i)\) in each principal column. So the strings have equal lengths and their entries align, and they differ only at the principal columns. There are \(t\) expanded variable positions, each contributing the copy factors of \(\Pi_t\), whose weights add up to \(1/t\). By Section 3,
\[
\begin{aligned}
&\|\Phi(z^{(i)})-\Phi(z^{(j)})\|^2\\
&\quad=t\cdot\frac1t\,\|a_i-a_j\|^2\\
&\quad=\|a_i-a_j\|^2 .
\end{aligned}
\]
So the points \(\Phi(z^{(1)}),\dots,\Phi(z^{(s)})\) form a congruent copy of \(A\), and all of them have colour \(k\) under \(c\), because every \(z^{(i)}\) lies in \(B_k\). \(\square\)

The proof uses the Hales–Jewett theorem only for the existence of the length \(n\), and the free group only through its universal property. The idempotent \(p\) is needed because \(\psi\) must be a homomorphism into a group, while strings can only be concatenated.

## 5. Exercises

**5.1** (easy). For \(n=2\) and \(\rho=1/4\), compute \(\alpha_1,\alpha_2\) and the weights of the two concatenated paths of Lemma 2.2.

**5.2** (medium). Explain why the proof cannot use a single path of weight one at every variable position.

**5.3** (medium). Let \(A\) consist of two points at distance one. Show directly that every \(r\)-colouring of \(\mathcal E\) is constant on a copy of \(A\), find an explicit \(D\) as in Lemma 2.1, and explain why Lemma 2.1 is needed in the proof of Proposition 1.1.

**5.4** (easy). Show that the map \(\Phi\) is injective on strings of a fixed length, and give two strings of different lengths with the same image.

## 6. Solutions

**5.1.** \(\alpha_1=1\) and \(\alpha_2=(1/2-1/4)/(3/4)=1/3\). The intervals are \([0,1/3]\) and \([1/3,1]\), of lengths \(1/3\) and \(2/3\). For \(t=1\) both heavier paths are used: weight \(1/3+2/3=1\). For \(t=2\) the heavier path is used on \([0,1/3]\) and the lighter one on \([1/3,1]\): weight \(1/3+\frac14\cdot\frac23=\frac12\).

**5.2.** The \(t\) variable positions each contribute the weight of the path used there, so the squared distances of the resulting copy are \(t\) times the weight times those of \(A\). With weight one, the copy would be \(A\) scaled by \(\sqrt t\), and \(t\) is only known after the colouring is fixed. Weight \(1/t\) gives scale one.

**5.3.** The \(r+1\) vertices of a regular simplex of side one in \(\mathbb R^r\subset\mathcal E\) receive \(r\) colours, so two of them have the same colour; \(D=r\) works. Lemma 2.1 is needed because the definition of a Ramsey set asks for one finite dimension \(D\) for each number of colours, while the construction of Section 4 produces a copy somewhere in \(\mathcal E\), in coordinates that depend on the colouring.

**5.4.** For equal lengths, \(\Phi(x)=\Phi(x')\) gives \(\sum\|x_j-x'_j\|^2=0\). The strings \((0)\) and \((0,0)\) both map to \(0\).

## References

- [OpenAI-ER] OpenAI, *A classification of finite Euclidean Ramsey configurations*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026
- [LRW-T] I. Leader, P. A. Russell and M. Walters, *Transitive sets in Euclidean Ramsey theory*, Journal of Combinatorial Theory, Series A 119 (2012), 382–396; arXiv:1012.1350. https://arxiv.org/abs/1012.1350
