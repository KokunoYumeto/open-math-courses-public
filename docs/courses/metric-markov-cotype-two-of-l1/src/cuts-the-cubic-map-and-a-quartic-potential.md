# Cuts, the cubic map and a quartic potential

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson prepares the two tools of the proof that \(\ell_1\) has metric Markov cotype two. The first tool replaces finitely many points of \(\ell_1\) by vertices of a cube \([0,1]^{\mathcal B}\) with weighted coordinates, in such a way that the distance in \(\ell_1\) becomes the *square* of a Hilbert distance, and gives a map from the whole cube back into \(\ell_1\) that does not increase distances. The second tool is an inequality for the map \(\Phi\) of the cube that applies the cubic \(\phi(r)=3r^2-2r^3\) to every coordinate. The squared change of \(\Phi\) between two points of the cube is bounded by the change of the fourth power of the Hilbert distance to a vertex, up to a term that is linear in the displacement. For a random displacement with mean zero the linear term disappears.

- The cut representation of finitely many points of \(\ell_1\) (Proposition 1.2).
- The cube, its two norms and the cubic map (Section 2).
- The flat inequality with the constant \(108\) (Proposition 3.3).
- Displacements with mean zero (Corollary 4.1), and why the identity map would not do (Example 4.2).

The lesson follows [OpenAI-MC, Sections 2 and 3]. It uses only finite sums, absolutely convergent series and the Cauchy–Schwarz inequality. The definitions of [Metric Markov cotype two](metric-markov-cotype-two.md) are not needed here.

## 1. Cuts

The space \(\ell_1\) consists of the real sequences \(x=(x(k))_{k\ge1}\) with \(\|x\|_1=\sum_k|x(k)|<\infty\). Let \(x_1,\dots,x_n\in\ell_1\) with \(n\ge2\). A *cut* is a subset \(B\) of \([n]=\{1,\dots,n\}\) that is neither empty nor all of \([n]\). Write \(r_+=\max\{r,0\}\). For a cut \(B\) and a coordinate \(k\) put
\[
b_B(k)=\Bigl(\min_{i\in B}x_i(k)-\max_{i\notin B}x_i(k)\Bigr)_+ ,
\]
and put \(v(k)=\min_ix_i(k)\). So \(b_B(k)>0\) exactly if in the coordinate \(k\) all points with index in \(B\) lie strictly above all other points, and then \(b_B(k)\) is the gap between the two groups.

The sequences \(v\) and \(b_B\) lie in \(\ell_1\): \(|v(k)|\le\sum_i|x_i(k)|\), and for \(i_0\in B\) and \(j_0\notin B\),
\[
0\le b_B(k)\le|x_{i_0}(k)|+|x_{j_0}(k)| .
\]
The *weight* of a cut is \(w_B=\|b_B\|_1\). Let \(\mathcal B\) be the set of the cuts with \(w_B>0\). It has at most \(2^n-2\) elements.

**Lemma 1.1** (one coordinate). Fix \(k\), and let \(\alpha_1<\alpha_2<\dots<\alpha_m\) be the different values among \(x_1(k),\dots,x_n(k)\). For \(1\le r<m\) let
\[
B_r=\{\,i:\ x_i(k)\ge\alpha_{r+1}\,\} .
\]
Then \(B_r\) is a cut with \(b_{B_r}(k)=\alpha_{r+1}-\alpha_r\), and \(b_B(k)=0\) for every other cut \(B\).

**Proof.** The set \(B_r\) contains an index with the value \(\alpha_m\) and no index with the value \(\alpha_1\), so it is a cut. The smallest value on \(B_r\) is \(\alpha_{r+1}\) and the largest value outside is \(\alpha_r\). Conversely let \(b_B(k)>0\), and let \(\alpha_{r+1}\) be the smallest value on \(B\) and \(\alpha'\) the largest value outside \(B\); then \(\alpha'<\alpha_{r+1}\). Every index with a value \(\ge\alpha_{r+1}\) lies in \(B\), because its value exceeds \(\alpha'\); every index in \(B\) has a value \(\ge\alpha_{r+1}\). So \(B=\{i:x_i(k)\ge\alpha_{r+1}\}\), and \(r\ge1\) because \(B\) is not all of \([n]\). \(\blacksquare\)

So in one coordinate the cuts that matter are nested: \(B_1\supset B_2\supset\dots\supset B_{m-1}\). The index \(i\) lies in \(B_r\) exactly if \(\alpha_{r+1}\le x_i(k)\).

Let \(z_i\in\{0,1\}^{\mathcal B}\) be the vector that records which cuts contain \(i\):
\[
z_i(B)=\begin{cases}1&\text{if }i\in B,\\0&\text{if }i\notin B.\end{cases}
\]
Define the map \(T\) from \(\mathbb R^{\mathcal B}\) to \(\ell_1\) by
\[
T(u)=v+\sum_{B\in\mathcal B}u_B\,b_B .
\]
It is affine, and its values lie in \(\ell_1\) because the sum is finite.

**Proposition 1.2** (cut representation). Let \(x_1,\dots,x_n\in\ell_1\). If the points are not all equal, then \(\mathcal B\) is not empty, and for all \(i,j\in[n]\) and all \(u,u'\in\mathbb R^{\mathcal B}\), with sums over \(B\in\mathcal B\):
\[
\begin{gathered}
T(z_i)=x_i,\\
\|x_i-x_j\|_1=\sum_Bw_B\,|z_i(B)-z_j(B)|,\\
\|T(u)-T(u')\|_1\le\sum_Bw_B\,|u_B-u'_B| .
\end{gathered}
\]
The second equation also holds with \((z_i(B)-z_j(B))^2\) in place of the absolute value. The three statements are called parts 1, 2 and 3.

**Proof.** Cuts outside \(\mathcal B\) have \(b_B=0\), so in every coordinate sums over \(\mathcal B\) of terms with a factor \(b_B(k)\) can be taken over all cuts. Fix \(k\) and use the notation of Lemma 1.1.

*Part 1.* By Lemma 1.1,
\[
T(z_i)(k)=\alpha_1+\sum_{r:\ i\in B_r}(\alpha_{r+1}-\alpha_r) .
\]
The index \(i\) lies in \(B_r\) exactly if \(\alpha_{r+1}\le x_i(k)\). So the sum runs over the gaps below \(x_i(k)\), and their total is \(x_i(k)-\alpha_1\).

*Part 2.* Let \(x_i(k)\ge x_j(k)\). No cut \(B_r\) contains \(j\) without containing \(i\), and \(B_r\) contains \(i\) without \(j\) exactly if \(x_j(k)<\alpha_{r+1}\le x_i(k)\). The gaps of these \(r\) add up to \(x_i(k)-x_j(k)\). So
\[
\begin{aligned}
&|x_i(k)-x_j(k)|\\
&\qquad=\sum_B|z_i(B)-z_j(B)|\,b_B(k) ,
\end{aligned}
\]
and the same holds if \(x_i(k)<x_j(k)\), by symmetry. Sum over \(k\); the sum over the finitely many \(B\) can be exchanged with the sum over \(k\), and \(\sum_kb_B(k)=w_B\). The numbers \(z_i(B)-z_j(B)\) are \(0\) or \(\pm1\), so their absolute values are their squares.

If \(\mathcal B\) were empty, part 2 would give \(\|x_i-x_j\|_1=0\) for all \(i,j\). So \(\mathcal B\) is not empty if the points are not all equal.

*Part 3.* \(T(u)-T(u')=\sum_B(u_B-u'_B)\,b_B\), and \(\|b_B\|_1=w_B\). \(\blacksquare\)

**Example 1.3.** Let \(x_1=(0,0)\), \(x_2=(1,0)\), \(x_3=(1,2)\) (all further coordinates \(0\)). In the first coordinate the values are \(0<1\), with the cut \(\{2,3\}\) and the gap \(1\). In the second coordinate the values are \(0<2\), with the cut \(\{3\}\) and the gap \(2\). So \(\mathcal B=\{\{2,3\},\{3\}\}\) with the weights \(1\) and \(2\), \(v=0\), \(b_{\{2,3\}}=(1,0)\), \(b_{\{3\}}=(0,2)\), and
\[
z_1=(0,0),\quad z_2=(1,0),\quad z_3=(1,1) .
\]
For instance \(\|x_1-x_3\|_1=3=1\cdot1+2\cdot1\).

**Example 1.4** (the map \(T\) leaves the span of the points). Let \(x_1,x_2,x_3\) be the first three unit vectors of \(\ell_1\). In the coordinate \(k\le3\) the values are \(0<1\), with the cut \(\{k\}\) and the gap \(1\). So \(\mathcal B=\{\{1\},\{2\},\{3\}\}\) with weights \(1\), \(v=0\), and \(T(u)=(u_1,u_2,u_3,0,0,\dots)\). The points \(x_i\) lie in the plane of the vectors with coordinate sum \(1\), but \(T\) maps the cube onto the cube \([0,1]^3\). For instance \(T(0)=0\) is the coordinatewise median of the three points. The new points of the cotype inequality will be of the form \(T(u)\), and this is where they can leave a subspace that contains the old points.

## 2. The cube and the cubic map

From here to the end of the lesson \(\mathcal B\) is any finite nonempty set and \((w_B)_{B\in\mathcal B}\) are positive numbers. On \(\mathbb R^{\mathcal B}\) use the norm
\[
\|u\|_{1,w}=\sum_Bw_B\,|u_B|
\]
and the inner product and norm
\[
\begin{gathered}
\langle u,u'\rangle_H=\sum_Bw_B\,u_Bu'_B,\\
\|u\|_H=\sqrt{\langle u,u\rangle_H} .
\end{gathered}
\]
Write \(H\) for \(\mathbb R^{\mathcal B}\) with this inner product. The Cauchy–Schwarz inequality gives, for \(a,\delta\in\mathbb R^{\mathcal B}\),
\[
\sum_Bw_B\,|a_B|\,|\delta_B|\le\|a\|_H\,\|\delta\|_H .
\]
Let \(Q=[0,1]^{\mathcal B}\) be the cube. Its *vertices* are the vectors in \(\{0,1\}^{\mathcal B}\). For two vertices \(e,e'\) the differences \(e_B-e'_B\) are \(0\) or \(\pm1\), so
\[
\|e-e'\|_{1,w}=\|e-e'\|_H^2 .
\]
With the weights and vertices \(z_i\) of Proposition 1.2 this reads
\[
\|x_i-x_j\|_1=\|z_i-z_j\|_{1,w}=\|z_i-z_j\|_H^2 .
\]
So the *squared* distances in \(\ell_1\), which occur in the cotype inequality, are *fourth* powers of distances in \(H\). Part 3 of Proposition 1.2 says that \(T\) does not increase distances from \(\|\cdot\|_{1,w}\) to \(\|\cdot\|_1\).

**Definition.** Let \(\phi(r)=3r^2-2r^3\) for \(0\le r\le1\), and let \(\Phi\) be the map of \(Q\) that applies \(\phi\) to every coordinate: \(\Phi(u)_B=\phi(u_B)\).

**Lemma 2.1.** 1. \(\phi'(r)=6r(1-r)\). The function \(\phi\) is increasing on \([0,1]\) with \(\phi(0)=0\) and \(\phi(1)=1\). So \(\Phi\) maps \(Q\) into \(Q\) and fixes every vertex.

2. For \(r\in[0,1]\) and \(d\in\{0,1\}\): \(|\phi'(r)|\le6\,|r-d|\).

3. \(\phi(r)=r^3+3r^2(1-r)\), and \(\phi(1-r)=1-\phi(r)\).

**Proof.** 1 is a computation. 2: \(6r(1-r)\le6r\) and \(6r(1-r)\le6(1-r)\). 3: \(r^3+3r^2-3r^3=\phi(r)\); and \(\phi(r)+\phi(1-r)\) is the sum of the four terms \(r^3\), \(3r^2(1-r)\), \(3r(1-r)^2\), \((1-r)^3\) of the expansion of \((r+(1-r))^3=1\). \(\blacksquare\)

Part 3 has a reading in terms of chance: if three independent events have the probability \(r\) each, then \(\phi(r)\) is the probability that at least two of them occur. Part 2 is the property that matters: the derivative of \(\phi\) vanishes at both ends of the interval, to first order. The map \(\Phi\) is *flat* at the vertices of the cube.

## 3. The flat inequality

Fix a vertex \(e\) of the cube. For \(u\in Q\) put
\[
F_e(u)=\|u-e\|_H^4 .
\]

**Lemma 3.1** (increments of \(\Phi\)). Let \(u,u'\in Q\), and put \(a=u-e\) and \(\delta=u'-u\). Then
\[
\begin{aligned}
&\|\Phi(u')-\Phi(u)\|_{1,w}\\
&\qquad\le6\,\|a\|_H\|\delta\|_H+3\,\|\delta\|_H^2 .
\end{aligned}
\]

**Proof.** Fix \(B\). The points \(u_B+\sigma\delta_B\), \(0\le\sigma\le1\), lie in \([0,1]\), and
\[
\begin{aligned}
&\phi(u'_B)-\phi(u_B)\\
&\qquad=\delta_B\int_0^1\phi'(u_B+\sigma\delta_B)\,d\sigma .
\end{aligned}
\]
By Lemma 2.1 with \(d=e_B\),
\[
\begin{aligned}
|\phi'(u_B+\sigma\delta_B)|&\le6\,|u_B+\sigma\delta_B-e_B|\\
&\le6\,|a_B|+6\sigma\,|\delta_B| .
\end{aligned}
\]
Integrating over \(\sigma\) gives
\[
|\phi(u'_B)-\phi(u_B)|\le6\,|a_B|\,|\delta_B|+3\,\delta_B^2 .
\]
Multiply by \(w_B\), sum over \(B\), and use the Cauchy–Schwarz inequality for the first term. \(\blacksquare\)

**Lemma 3.2** (the remainder of the fourth power). For \(a,\delta\in H\) let
\[
R=\|a+\delta\|_H^4-\|a\|_H^4-4\,\|a\|_H^2\langle a,\delta\rangle_H .
\]
Then
\[
R=2\,\|a\|_H^2\|\delta\|_H^2+\bigl(2\langle a,\delta\rangle_H+\|\delta\|_H^2\bigr)^2 .
\]
In particular \(R\ge0\), \(\|a\|_H^2\|\delta\|_H^2\le\tfrac12R\) and \(\|\delta\|_H^4\le4R\).

**Proof.** Write \(\alpha=\|a\|_H^2\) and \(\gamma=2\langle a,\delta\rangle_H+\|\delta\|_H^2\), so that \(\|a+\delta\|_H^2=\alpha+\gamma\). Then
\[
\begin{aligned}
R&=(\alpha+\gamma)^2-\alpha^2-4\alpha\langle a,\delta\rangle_H\\
&=2\alpha\bigl(\gamma-2\langle a,\delta\rangle_H\bigr)+\gamma^2\\
&=2\alpha\,\|\delta\|_H^2+\gamma^2 .
\end{aligned}
\]
Both terms are \(\ge0\), which gives the first two consequences. For the third, \(\|\delta\|_H^2=\gamma-2\langle a,\delta\rangle_H\), so
\[
\begin{aligned}
\|\delta\|_H^4&\le2\gamma^2+8\langle a,\delta\rangle_H^2\\
&\le2\gamma^2+8\,\alpha\,\|\delta\|_H^2\\
&\le4R .
\end{aligned}
\]
\(\blacksquare\)

The term \(4\|a\|_H^2\langle a,\delta\rangle_H\) is the derivative of \(a\mapsto\|a\|_H^4\) in the direction \(\delta\). So \(R\) is the error of the linear approximation of the fourth power, and the lemma bounds it from below.

**Proposition 3.3** (the flat inequality). Let \(u,u'\in Q\) and let \(e\) be a vertex of \(Q\). With \(a=u-e\) and \(\delta=u'-u\),
\[
\begin{aligned}
&\|\Phi(u')-\Phi(u)\|_{1,w}^2\\
&\quad\le108\,\bigl(F_e(u')-F_e(u)\\
&\qquad\qquad-4\,\|a\|_H^2\langle a,\delta\rangle_H\bigr) .
\end{aligned}
\]

**Proof.** The expression in the bracket is the number \(R\) of Lemma 3.2, because \(u'-e=a+\delta\). Square the inequality of Lemma 3.1 and use \((\alpha+\beta)^2\le2\alpha^2+2\beta^2\):
\[
\begin{aligned}
&\|\Phi(u')-\Phi(u)\|_{1,w}^2\\
&\qquad\le72\,\|a\|_H^2\|\delta\|_H^2+18\,\|\delta\|_H^4\\
&\qquad\le36R+72R .
\end{aligned}
\]
\(\blacksquare\)

## 4. Displacements with mean zero

**Corollary 4.1.** Let \(u\in Q\) and let \(e\) be a vertex of \(Q\). Let \(u^1,\dots,u^m\in Q\) and \(\rho_1,\dots,\rho_m\ge0\) with \(\sum_l\rho_l=1\) and
\[
\sum_l\rho_l\,u^l=u .
\]
Then
\[
\begin{aligned}
&\sum_l\rho_l\,\|\Phi(u^l)-\Phi(u)\|_{1,w}^2\\
&\qquad\le108\,\Bigl(\sum_l\rho_l\,F_e(u^l)-F_e(u)\Bigr) .
\end{aligned}
\]

**Proof.** Apply Proposition 3.3 to \(u\) and \(u^l\), with \(\delta^l=u^l-u\), multiply by \(\rho_l\) and sum. The linear terms add up to \(4\|a\|_H^2\langle a,\sum_l\rho_l\delta^l\rangle_H=0\). \(\blacksquare\)

In words: let a random point of the cube have the mean \(u\). Then the mean squared distance, in the norm \(\|\cdot\|_{1,w}\), between the images under \(\Phi\) of the random point and of its mean is at most \(108\) times the mean increase of the potential \(F_e\). The vertex \(e\) is arbitrary. In the next lesson the corollary is applied to every step of a walk, and the increases of the potential add up to a telescoping sum.

**Example 4.2** (the identity map does not satisfy such an inequality). Take one coordinate with the weight \(1\), the vertex \(e=0\), a number \(0<\varepsilon\le\tfrac12\), the point \(u=\varepsilon\) and the two points \(u^1=0\), \(u^2=2\varepsilon\) with \(\rho_1=\rho_2=\tfrac12\). The potential is \(F_0(u)=u^4\), and
\[
\begin{aligned}
\sum_l\rho_lF_0(u^l)-F_0(u)&=\tfrac12(2\varepsilon)^4-\varepsilon^4\\
&=7\varepsilon^4 .
\end{aligned}
\]
Without the map \(\Phi\), the mean squared distance of the two points from \(u\) is \(\varepsilon^2\), which is not bounded by a constant times \(\varepsilon^4\). With the map: \(\phi(\varepsilon)-\phi(0)=3\varepsilon^2-2\varepsilon^3\) and \(\phi(2\varepsilon)-\phi(\varepsilon)=9\varepsilon^2-14\varepsilon^3\), so the mean squared distance of the images is at most \(\tfrac12(9+81)\varepsilon^4=45\varepsilon^4\). Near a vertex the potential is of the fourth order, and a map of the cube can obey the inequality only if its changes are of the second order there. This is the reason for the cubic: \(\phi'\) vanishes at \(0\) and at \(1\).

## 5. Exercises

**5.1.** Compute \(\mathcal B\), the weights, \(v\) and the vectors \(z_i\) for \(x_1=(0,3)\), \(x_2=(2,1)\), \(x_3=(5,1)\), and check part 2 of Proposition 1.2 for the three pairs.

**5.2.** In the setting of Section 1 show that \(\sum_Bb_B(k)=\max_ix_i(k)-\min_ix_i(k)\) for every \(k\), and conclude that for \(u\in Q\) every coordinate of \(T(u)\) lies between the smallest and the largest value of the points in this coordinate.

**5.3.** Let \(n=3\) and let \(\mu\in\{0,1\}^{\mathcal B}\) be the vertex with \(\mu_B=1\) exactly if \(B\) has at least two elements. Show that \(T(\mu)\) is the coordinatewise median of \(x_1,x_2,x_3\).

**5.4.** Show that \(\|\Phi(u')-\Phi(u)\|_{1,w}\le\tfrac32\,\|u'-u\|_{1,w}\) for \(u,u'\in Q\), and that the constant \(\tfrac32\) cannot be replaced by a smaller one.

**5.5.** Take one coordinate with the weight \(w\), the vertex \(e=0\), the point \(u=\tfrac12\) and the two points \(\tfrac12\pm\eta\) with probabilities \(\tfrac12\), where \(0<\eta\le\tfrac12\). Compute both sides of Corollary 4.1.

## 6. Solutions

**5.1.** First coordinate: the values are \(0<2<5\), with the cuts \(\{2,3\}\) (gap \(2\)) and \(\{3\}\) (gap \(3\)). Second coordinate: the values are \(1<3\), with the cut \(\{1\}\) (gap \(2\)). So \(\mathcal B=\{\{2,3\},\{3\},\{1\}\}\) with the weights \(2,3,2\), and \(v=(0,1)\). In this order of the cuts, \(z_1=(0,0,1)\), \(z_2=(1,0,0)\), \(z_3=(1,1,0)\). Distances: \(\|x_1-x_2\|_1=4=2+2\); \(\|x_1-x_3\|_1=7=2+3+2\); \(\|x_2-x_3\|_1=3\).

**5.2.** By Lemma 1.1 the sum is \(\sum_{r=1}^{m-1}(\alpha_{r+1}-\alpha_r)=\alpha_m-\alpha_1\). For \(u\in Q\), \(T(u)(k)=v(k)+\sum_Bu_Bb_B(k)\) with \(0\le u_B\le1\) and \(b_B(k)\ge0\), so \(\alpha_1\le T(u)(k)\le\alpha_1+(\alpha_m-\alpha_1)\).

**5.3.** Fix \(k\). By Lemma 1.1, \(T(\mu)(k)\) is \(\alpha_1\) plus the gaps \(\alpha_{r+1}-\alpha_r\) of those \(r\) for which \(B_r\) has at least two elements, that is, for which at least two of the three points have a value \(\ge\alpha_{r+1}\) in the coordinate \(k\). This holds exactly if the median of the three values is \(\ge\alpha_{r+1}\). So the sum of these gaps is the median minus \(\alpha_1\).

**5.4.** \(\phi'(r)=6r(1-r)\) has the largest value \(\tfrac32\) on \([0,1]\), at \(r=\tfrac12\). So \(|\phi(r')-\phi(r)|\le\tfrac32|r'-r|\) for \(r,r'\in[0,1]\); multiply by \(w_B\) and sum. For one coordinate and \(u=\tfrac12\), \(u'=\tfrac12+\eta\), the quotient of the two sides is \(\tfrac32-2\eta^2\) (see the next solution), which tends to \(\tfrac32\) as \(\eta\to0\).

**5.5.** \(\phi(\tfrac12\pm\eta)=\tfrac12\pm(\tfrac32\eta-2\eta^3)\), and \(\|\cdot\|_{1,w}\) is \(w\) times the absolute value. So the left side is \(w^2(\tfrac32\eta-2\eta^3)^2\). The potential is \(F_0(u)=(wu^2)^2\), and
\[
\begin{aligned}
&\tfrac12\bigl(\tfrac12+\eta\bigr)^4+\tfrac12\bigl(\tfrac12-\eta\bigr)^4-\tfrac1{16}\\
&\qquad=\tfrac32\eta^2+\eta^4 .
\end{aligned}
\]
So the right side is \(108\,w^2(\tfrac32\eta^2+\eta^4)\). The left side is at most \(\tfrac94w^2\eta^2\), so in this example the inequality holds with \(\tfrac32\) in place of \(108\).

## References

- [OpenAI-MC] OpenAI, *Metric Markov Cotype Two of \(\ell_1\)*, OpenAI Math Release preprint, 5 October 2026, Sections 2 and 3. https://github.com/openai/math/tree/main/preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026
