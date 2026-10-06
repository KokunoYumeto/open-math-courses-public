# Uniform approximation on locally compact spaces

**Programme reading HA-LCA-PRE-APPROX.** The result needed for Fourier analysis is uniform density in \(C_0(X)\), with no countability assumption on the locally compact Hausdorff space \(X\). We prove it from a polynomial estimate, and include the compactification argument.

The earlier proofs used here are [Lemma 1.1 of the Banach-algebra reading](banach-spectrum.md#ha-lca-pre-banach-lemma-1-1), for compact intervals and uniform continuity, and [Lemmas 1.1 and 1.5 of the finite-Radon reading](finite-radon-representation.md), for compact closed sets and the uniform function spaces. In particular, uniform limits are continuous and \(C_0\) is complete; those statements were proved in the earlier reading.

The free sources are the faculty-hosted [*The Weierstrass and Stone Approximation Theorems*](https://web.math.utk.edu/~freire/teaching/m561f22/Stone_Weierstrass_proof.pdf), pages 1–5 through the complex-valued reduction, and D. H. Fremlin's [*Measure Theory*, Volume 4, 4A6B](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt4a6.tex), the 8 December 2010 version in the 2013 collection, for the \(C_0\) reduction. The source's invoked compact approximation theorem is proved below.

Adaptation and additional proofs: GPT-6 Astra (OpenAI), Ultra, 4 October 2026. This combined reading is under the [Design Science License](../../assets/fremlin/DESIGN-SCIENCE-LICENSE.txt), including its warranty disclaimer. The unchanged Fremlin source package preserves the original copyright and source.

## 1. Polynomial approximation and lattice operations

<a id="ha-lca-pre-approx-lemma-1-1"></a>
**Lemma 1.1 (polynomial approximation).** Every continuous real function on a compact interval is a uniform limit of real polynomials.

**Proof.** First work on \([0,1]\). For \(n\ge1\) put
\[
w_{n,k}(x)=\binom nk x^k(1-x)^{n-k},\qquad
B_nf(x)=\sum_{k=0}^n f(k/n)w_{n,k}(x).
\]
Powers with exponent zero are one, including at the endpoints, so these are polynomials defined on the closed interval. The finite binomial expansion gives
\(\sum_k w_{n,k}(x)=1\). For \(k\ge1\),
\[
k\binom nk=n\binom{n-1}{k-1},
\]
so summing after taking out \(nx\) gives
\[
\sum_{k=0}^n k\,w_{n,k}(x)=nx.
\]
For \(n\ge2\), the identity
\(k(k-1)\binom nk=n(n-1)\binom{n-2}{k-2}\)
similarly gives
\(\sum_k k(k-1)w_{n,k}(x)=n(n-1)x^2\).
For \(n=1\) both sides of this last identity are zero. Adding the first-moment identity and expanding the square now gives
\[
\sum_{k=0}^n(k/n-x)^2w_{n,k}(x)
=\frac{x(1-x)}n\le\frac1{4n}.                         \tag{1}
\]
All these are finite algebraic identities; no probability limit theorem is used.

Let \(M=\|f\|_\infty\). Given \(\varepsilon>0\), uniform continuity supplies \(\delta>0\) such that
\(|f(s)-f(t)|<\varepsilon\) whenever \(|s-t|<\delta\).
The part of
\[
|B_nf(x)-f(x)|\le\sum_{k=0}^n|f(k/n)-f(x)|w_{n,k}(x)
\]
with \(|k/n-x|<\delta\) is at most \(\varepsilon\), because the weights are nonnegative and sum to one. On the remaining indices,
\[
\sum_{|k/n-x|\ge\delta}w_{n,k}(x)
\le\delta^{-2}\sum_k(k/n-x)^2w_{n,k}(x)
\le\frac1{4n\delta^2}.
\]
Their contribution is at most \(M/(2n\delta^2)\). Hence
\[
\|B_nf-f\|_\infty\le\varepsilon+\frac{M}{2n\delta^2},
\]
which tends to at most \(\varepsilon\), uniformly in \(x\). As \(\varepsilon\) is arbitrary, uniform convergence follows.

For a nondegenerate interval \([a,b]\), apply the result to \(f(a+(b-a)x)\) and replace \(x\) by \((t-a)/(b-a)\) in the approximating polynomials. On a one-point interval a constant polynomial suffices. \(\square\)

<a id="ha-lca-pre-approx-lemma-1-2"></a>
**Lemma 1.2 (closed algebras are lattices).** Let \(K\) be compact Hausdorff and \(A\) a real subalgebra of \(C(K;\mathbb R)\) containing the constant functions. Its uniform closure \(\overline A\) is again an algebra containing constants. It is closed under absolute values, maxima and minima of finitely many functions.

**Proof.** Addition and scalar multiplication pass to uniform limits. If \(f_n\to f\) and \(g_n\to g\) uniformly, then
\[
\|f_ng_n-fg\|_\infty
\le\|f_n-f\|_\infty\|g_n\|_\infty
   +\|f\|_\infty\|g_n-g\|_\infty\longrightarrow0,
\]
since a uniformly convergent sequence is uniformly bounded. This proves the algebra assertion.

For \(f\in\overline A\), take \(M>\|f\|_\infty\). Lemma 1.1 supplies polynomials \(p_n\) converging to \(|t|\) uniformly on \([-M,M]\). Since \(\overline A\) is an algebra containing constants, \(p_n(f)\in\overline A\), and
\[
\|p_n(f)-|f|\|_\infty
\le\sup_{|t|\le M}|p_n(t)-|t||\longrightarrow0.
\]
Thus \(|f|\in\overline A\). The identities
\[
\max(f,g)=\frac{f+g+|f-g|}{2},\qquad
\min(f,g)=\frac{f+g-|f-g|}{2}
\]
prove closure under two-function maxima and minima, and induction gives any finite number. Here a closure is closed in the uniform metric: if a limit of its elements were outside it, a positive-radius ball about that limit disjoint from \(A\) would also exclude all sufficiently close elements, a contradiction. This also justifies the limit passages within \(\overline A\). \(\square\)

## 2. Approximation on a compact space

<a id="ha-lca-pre-approx-theorem-2-1"></a>
**Theorem 2.1 (real compact approximation).** If a real subalgebra \(A\subseteq C(K;\mathbb R)\) contains constants and separates points of the compact Hausdorff space \(K\), then it is uniformly dense in \(C(K;\mathbb R)\).

**Proof.** If \(K\) is empty there is only the zero function and the assertion is immediate. Put \(B=\overline A\). It is a lattice by Lemma 1.2. Fix \(h\in C(K;\mathbb R)\) and \(\varepsilon>0\).

For distinct \(x,y\), choose \(a\in A\) with \(a(x)\ne a(y)\). The function
\[
a_{x,y}(z)=h(x)+
 \frac{h(y)-h(x)}{a(y)-a(x)}\bigl(a(z)-a(x)\bigr)
\]
belongs to \(A\) and equals \(h\) at \(x,y\). For \(y=x\), use the constant function \(h(x)\).

Hold \(x\) fixed. The open sets
\(\{z:a_{x,y}(z)>h(z)-\varepsilon\}\), as \(y\) varies, cover \(K\), because the set indexed by \(y\) contains \(y\). Choose finitely many covering indices and take the maximum of their functions, calling it \(b_x\in B\). It satisfies
\[
b_x(z)>h(z)-\varepsilon\quad(z\in K),\qquad b_x(x)=h(x).
\]
The sets \(\{z:b_x(z)<h(z)+\varepsilon\}\), as \(x\) varies, also form an open cover. Choose a finite subcover and let \(b\) be the minimum of its \(b_x\)'s. Then \(b\in B\) and
\[
h(z)-\varepsilon<b(z)<h(z)+\varepsilon\quad(z\in K).
\]
In particular \(\|b-h\|_\infty\le\varepsilon\). Repeating with \(\varepsilon\downarrow0\) puts \(h\) in the closed set \(B\). This is exactly the uniform density of \(A\). \(\square\)

<a id="ha-lca-pre-approx-corollary-2-2"></a>
**Corollary 2.2 (complex compact approximation).** A complex subalgebra \(A\subseteq C(K;\mathbb C)\) is uniformly dense if it contains constants, separates points and contains \(\overline f\) whenever it contains \(f\).

**Proof.** Its real-valued members form a real algebra \(A_{\mathbb R}\) containing real constants. If \(f\in A\), then
\[
\operatorname{Re}f=\tfrac12(f+\overline f),\qquad
\operatorname{Im}f=\tfrac1{2i}(f-\overline f)
\]
belong to \(A_{\mathbb R}\). When \(f(x)\ne f(y)\), at least one of these two real functions differs at \(x,y\), so \(A_{\mathbb R}\) separates points. Apply Theorem 2.1 to the real and imaginary parts of any continuous \(h\). If their uniform approximation errors are less than \(\varepsilon/2\), the sum of the two approximants, with the second multiplied by \(i\), lies in \(A\) and approximates \(h\) within \(\varepsilon\). \(\square\)

## 3. The version for functions vanishing at infinity

<a id="ha-lca-pre-approx-lemma-3-1"></a>
**Lemma 3.1 (adjoining a point at infinity).** For a locally compact Hausdorff space \(X\), adjoin a new point \(\infty\). On \(X^\infty=X\cup\{\infty\}\), take as a basis the open subsets of \(X\) and the sets
\[
N_K=\{\infty\}\cup(X\setminus K),\qquad K\subseteq X\ \text{compact}.
\]
This gives a compact Hausdorff space in which \(X\) is an open subspace with its original topology. A function \(f:X\to\mathbb C\) lies in \(C_0(X)\) if and only if its extension \(f^\infty\), defined to be zero at \(\infty\), is continuous on \(X^\infty\).

**Proof.** Compact subsets of \(X\) are closed, by the earlier finite-Radon Lemma 1.1. Thus an intersection of an open subset of \(X\) with \(N_K\) is open in \(X\), and
\(N_K\cap N_L=N_{K\cup L}\), where a finite union of compact sets is compact by taking finite subcovers for each member. These facts verify the basis intersection condition and the subspace assertion.

For compactness, any open cover has a member containing \(\infty\), hence containing some \(N_K\). Finitely many further members cover the compact remainder \(K\). Two points of \(X\) are separated as before. To separate \(x\in X\) from \(\infty\), choose a compact neighbourhood \(K\) of \(x\); its interior at \(x\) and \(N_K\) are disjoint neighbourhoods. This proves the Hausdorff assertion. The construction also works when \(X\) is compact: then \(\infty\) is isolated.

If \(f\in C_0(X)\), the compact set \(\{|f|\ge\varepsilon\}\) shows that \(|f^\infty|<\varepsilon\) on a neighbourhood \(N_K\) of \(\infty\), for every \(\varepsilon>0\). Thus the extension is continuous there, and it is already continuous on \(X\). Conversely, continuity at \(\infty\) supplies a compact \(K\) outside which \(|f|<\varepsilon\). The level set \(\{|f|\ge\varepsilon\}\) is closed in \(X\) and contained in \(K\), so it is compact by the earlier finite-Radon Lemma 1.1. Continuity on \(X\) is inherited from the extension. These are exactly the defining properties of \(C_0(X)\). \(\square\)

<a id="ha-lca-pre-approx-theorem-3-2"></a>
**Theorem 3.2 (locally compact Stone–Weierstrass).** Suppose \(A\subseteq C_0(X;\mathbb C)\) is a complex linear subspace satisfying:

1. \(fg\in A\) and \(\overline f\in A\) for \(f,g\in A\);
2. for each \(x\in X\), some \(f\in A\) has \(f(x)\ne0\);
3. for distinct \(x,y\), some \(f\in A\) has \(f(x)\ne f(y)\).

Then \(A\) is uniformly dense in \(C_0(X;\mathbb C)\).

**Proof.** On the compact space \(X^\infty\) of Lemma 3.1, consider
\[
\widetilde A=\{f^\infty+c:f\in A,\ c\in\mathbb C\}.
\]
It is a complex subalgebra containing constants and conjugates: expanding a product gives \((fg+df+cg)^\infty+cd\). It separates points of \(X\) by condition 3. It separates \(x\in X\) from \(\infty\) by condition 2, because \(f^\infty(\infty)=0\). Corollary 2.2 makes \(\widetilde A\) dense in \(C(X^\infty;\mathbb C)\).

Given \(h\in C_0(X)\) and \(\varepsilon>0\), choose \(f^\infty+c\) within \(\varepsilon/2\) of \(h^\infty\). At \(\infty\) this gives \(|c|<\varepsilon/2\), so on \(X\)
\[
\|f-h\|_\infty
\le\|f^\infty+c-h^\infty\|_\infty+|c|<\varepsilon.
\]
This proves density. No constant function on a noncompact \(X\) has been inserted into \(A\); constants are used only on the compact space. \(\square\)
