# The Zarankiewicz formula

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves Zarankiewicz's formula \(\operatorname{cr}(K_{m,n})=d_md_n\) [OpenAI-B, Theorem 1.1]. The upper bound is Zarankiewicz's drawing, Proposition 4.1 of [Drawings and crossing numbers](drawings-and-crossing-numbers.md). For the lower bound with \(n=2s+1\) odd, the form \(J\) of a normal drawing is cut into \(n\times n\) blocks, one for each pair of vertices of the first class. A linear map built from interpolation weights sends each block to an \(s^2\times s^2\) matrix: diagonal blocks become invertible, an off-diagonal block becomes a matrix whose rank is at most the number of crossings between two stars, and the cycle pairing of [Signed crossings and cycles](signed-crossings-and-cycles.md) gives the images the form \(X_i-Y_k\). The rank inequality of [An intersection inequality for subspaces](an-intersection-inequality-for-subspaces.md) then counts the crossings. Even \(n\) follows by deleting vertices.

- The blocks of a drawing of \(K_{m,n}\) (Section 1).
- The block relation (Section 2).
- The detector (Section 3).
- The lower bound for odd \(n\) (Section 4).
- Even \(n\) and the formula (Section 5).

Throughout, the vertex classes of \(K_{m,n}\) are \(\{a_1,\ldots,a_m\}\) and \(\{b_1,\ldots,b_n\}\), and \(d_r=\lfloor r/2\rfloor\lfloor(r-1)/2\rfloor\).

## 1. The blocks of a drawing of \(K_{m,n}\)

Let \(D\) be a normal drawing of \(K_{m,n}\) (Definition 1.1 of [Polygonal drawings](polygonal-drawings.md)). Orient every edge \(a_ib_p\) from \(a_i\) to \(b_p\), choose a cut at every vertex, and let \(J\) be the form of Definition 1.2 of [Signed crossings and cycles](signed-crossings-and-cycles.md). For \(1\le i,k\le m\) let \(J^{ik}\) be the \(n\times n\) matrix
\[
J^{ik}(p,q)=J(a_ib_p,\,a_kb_q).
\]

**Lemma 1.1.** Let \(\prec_i\) be the order of the edges at \(a_i\) given by the cut there, read as an order of their second endpoints \(b_1,\ldots,b_n\).

1. \(J^{ii}\) is the matrix \(S_{\prec_i}\) with entries \(\frac12\) at \((p,q)\) if \(b_p\prec_ib_q\), \(-\frac12\) if \(b_q\prec_ib_p\), and \(0\) on the diagonal.
2. For \(i\ne k\) and \(p\ne q\), \(J^{ik}(p,q)=I(a_ib_p,a_kb_q)\), the signed number of crossings of the two edges.

*Proof.* (1) For \(p\ne q\) the edges \(a_ib_p\) and \(a_ib_q\) have the common endpoint \(a_i\) only; they do not cross, the drawing being normal, and both point out of \(a_i\), so \(J(a_ib_p,a_ib_q)=\frac12T_{a_i}(a_ib_p,a_ib_q)\). The diagonal of \(J\) vanishes. (2) The edges have no common endpoint, so there is no local term. \(\square\)

Let \(c_{ik}\) be the number of crossing points of \(D\) on an edge at \(a_i\) and an edge at \(a_k\). By Corollary 4.2 of [Polygonal drawings](polygonal-drawings.md), the two edges through a crossing point have four distinct endpoints, so they belong to the stars of two different vertices \(a_i\ne a_k\), and
\[
\sum_{i\ne k}c_{ik}=2\,c(D),\tag{1.1}
\]
the sum over ordered pairs, each crossing point being counted for \((i,k)\) and for \((k,i)\).

## 2. The block relation

Let \(\mathcal L\) be the space of *additive* \(n\times n\) matrices, those of the form \(H(p,q)=r_p+c_q\) for some \(r,c\in\mathbb R^n\).

**Lemma 2.1** (block relation; [OpenAI-B, Lemma 3.2]). For all \(1\le i,k\le m\),
\[
J^{ik}-J^{i1}-J^{1k}+J^{11}\in\mathcal L .
\]

*Proof.* Call the left side \(H\). For a matrix \(K\) and indices \(p,p',q,q'\), the *rectangle sum* is
\[
\begin{gathered}
\rho(K)=K(p,q)-K(p,q')\\
-K(p',q)+K(p',q').
\end{gathered}
\]
A matrix \(H\) is additive exactly when all its rectangle sums vanish: then, for fixed \(p_0,q_0\), \(H(p,q)\) is \(H(p,q_0)+H(p_0,q)-H(p_0,q_0)\), and conversely. If \(i=1\) or \(k=1\), then \(H=0\). If \(p=p'\) or \(q=q'\), the rectangle sum vanishes trivially. Otherwise \(i,k\ne1\), and the closed walks
\[
\begin{gathered}
a_i\to b_p\to a_1\to b_{p'}\to a_i,\\
a_k\to b_q\to a_1\to b_{q'}\to a_k
\end{gathered}
\]
are simple cycles with signed edge vectors
\[
\begin{gathered}
z=a_ib_p-a_1b_p+a_1b_{p'}-a_ib_{p'},\\
y=a_kb_q-a_1b_q+a_1b_{q'}-a_kb_{q'} .
\end{gathered}
\]
By Theorem 1.3 of [Signed crossings and cycles](signed-crossings-and-cycles.md), \(J(z,y)=0\). Expand \(J(z,y)\) by bilinearity into sixteen terms and group them by the first-class endpoints of the two edges. The four terms with an edge at \(a_i\) from \(z\) and an edge at \(a_k\) from \(y\) add up to \(\rho(J^{ik})\). The terms with edges at \(a_i\) and \(a_1\) give \(-\rho(J^{i1})\), because the edges at \(a_1\) enter \(y\) with the opposite signs; likewise those at \(a_1\) and \(a_k\) give \(-\rho(J^{1k})\), and those at \(a_1\) and \(a_1\) give \(+\rho(J^{11})\). Hence
\[
\begin{aligned}
0=J(z,y)&=\rho(J^{ik})-\rho(J^{i1})\\
&\quad-\rho(J^{1k})+\rho(J^{11})\\
&=\rho(H),
\end{aligned}
\]
and every rectangle sum of \(H\) vanishes. \(\square\)

## 3. The detector

Fix \(n=2s+1\) with \(s\ge1\), put \(d=s^2\), and choose distinct real numbers \(x_1,\ldots,x_n\). Let \(F(t)=\prod_p(t-x_p)\), let \(h_{pq}\in\mathbb R^d\) be the vector with coordinates \(x_p^ix_q^j\), \(0\le i,j<s\), in a fixed order, and put
\[
\begin{gathered}
\omega_{pq}=\frac{x_p-x_q}{F'(x_p)\,F'(x_q)},\\
B_{pq}=\omega_{pq}\,h_{pq}h_{pq}^{\mathsf T},\\
\Phi(H)=\sum_{p,q=1}^nH(p,q)\,B_{pq}
\end{gathered}
\]
for an \(n\times n\) matrix \(H\). For a linear order \(\prec\) of \(\{1,\ldots,n\}\) let \(S_\prec\) be the matrix with entries \(\frac12\) at \((p,q)\) if \(p\prec q\), \(-\frac12\) if \(q\prec p\), and \(0\) on the diagonal.

**Lemma 3.1** (the detector; [OpenAI-B, Lemma 4.2]). The linear map \(\Phi:\mathbb R^{n\times n}\to\mathbb R^{d\times d}\) has the following properties.

1. \(\Phi(H)=0\) for every additive matrix \(H\) and every diagonal matrix \(H\).
2. \(B_{pp}=0\), and \(B_{pq}\) has rank one for \(p\ne q\). Hence \(\operatorname{rank}\Phi(H)\) is at most the number of off-diagonal entries of \(H\) that are not zero.
3. \(\Phi(S_\prec)\) is invertible for every linear order \(\prec\).

*Proof.* (2) The factor \(x_p-x_q\) vanishes for \(p=q\) and not otherwise, and \(h_{pq}\ne0\) since its coordinate for \(i=j=0\) is \(1\); a nonzero multiple of \(hh^{\mathsf T}\) with \(h\ne0\) has rank one. A sum of matrices has rank at most the sum of their ranks.

(1) Diagonal matrices are killed by (2). The entry of \(B_{pq}\) in row \((i,j)\) and column \((i',j')\) is
\[
\frac{x_p^{\,i+i'}}{F'(x_p)}\cdot\frac{(x_p-x_q)\,x_q^{\,j+j'}}{F'(x_q)} .
\]
For fixed \(p\), the polynomial \(t\mapsto(x_p-t)t^{\,j+j'}\) has degree at most \(2s-1=n-2\), so by Corollary 1.2 of [Interpolation](interpolation.md) the sum over \(q\) vanishes: \(\sum_qB_{pq}=0\). In the same way \(\sum_pB_{pq}=0\) for fixed \(q\). Hence, for \(H(p,q)=r_p+c_q\),
\[
\begin{aligned}
\Phi(H)&=\sum_pr_p\sum_qB_{pq}+\sum_qc_q\sum_pB_{pq}\\
&=0 .
\end{aligned}
\]

(3) First let \(\prec\) be the natural order. Let \(H_<(p,q)=1\) if \(q<p\) and \(0\) otherwise, and let \(\mathbf 1\) be the all-ones vector; then \(S_\prec=\frac12\mathbf1\mathbf1^{\mathsf T}-H_<-\frac12I\), and by (1), \(\Phi(S_\prec)=-\Phi(H_<)\). Subtracting \(1\) from every entry in the rows \(p>s+1\) changes \(H_<\) by an additive matrix, giving \(H'\) with \(\Phi(H')=\Phi(H_<)\). Off the diagonal, \(H'\) is \(+1\) on the pairs \(1\le q<p\le s+1\), \(-1\) on the pairs \(s+1<p<q\le2s+1\), and \(0\) elsewhere: its off-diagonal support is the odd pattern \(Q_s\) of Section 3 of [Interpolation](interpolation.md). Its diagonal does not matter. Therefore
\[
\begin{aligned}
\Phi(S_\prec)&=-\sum_{(p,q)\in Q_s}H'(p,q)\,\omega_{pq}\,h_{pq}h_{pq}^{\mathsf T}\\
&=-A\,\Lambda\,A^{\mathsf T},
\end{aligned}
\]
where \(A\) is the \(d\times d\) matrix with the columns \(h_{pq}\), \((p,q)\in Q_s\), and \(\Lambda\) is diagonal with the nonzero entries \(H'(p,q)\,\omega_{pq}\). By Lemma 3.1 of [Interpolation](interpolation.md) the columns of \(A\) form a basis, so \(A\) is invertible, and so is \(\Phi(S_\prec)\).

For an arbitrary order \(\pi(1)\prec\pi(2)\prec\cdots\prec\pi(n)\), put \(x'_a=x_{\pi(a)}\), distinct numbers. The polynomial \(F\) is the same for the nodes \(x'\), and the vectors and matrices built from them are \(h'_{ab}=h_{\pi(a)\pi(b)}\) and \(B'_{ab}=B_{\pi(a)\pi(b)}\). Since \(S_\prec(\pi(a),\pi(b))\) is the entry of the natural order at \((a,b)\), \(\Phi(S_\prec)=\sum_{a,b}S_{\text{nat}}(a,b)B'_{ab}\), which is invertible by the first case applied to the nodes \(x'\). \(\square\)

So \(\Phi\) forgets exactly what the cycle relations leave undetermined (additive terms and diagonal entries), it costs at most one unit of rank per nonzero off-diagonal entry, and it recognizes every linear order of the spokes, all at once.

## 4. The lower bound for odd \(n\)

For a normal drawing \(D\) of \(K_{m,n}\), let \(N_I(D)\) be the number of unordered pairs of independent edges whose signed number of crossings \(I\) is not zero. Each such pair crosses at least once, and different pairs cross at different points, so \(N_I(D)\le c(D)\).

**Proposition 4.1** (odd \(n\); [OpenAI-B, Section 5.2]). Let \(m\ge1\) and \(n=2s+1\ge3\). For every normal drawing \(D\) of \(K_{m,n}\),
\[
c(D)\ \ge\ N_I(D)\ \ge\ d_m\,d_n .
\]

*Proof.* Let \(R_{ik}=\Phi(J^{ik})\) and
\[
X_i=R_{i1},\qquad Y_k=R_{11}-R_{1k}.
\]
By Lemma 2.1 and Lemma 3.1(1), \(R_{ik}=R_{i1}+R_{1k}-R_{11}=X_i-Y_k\) for all \(i,k\). By Lemma 1.1(1) and Lemma 3.1(3), \(X_i-Y_i=R_{ii}=\Phi(S_{\prec_i})\) is invertible. For \(i\ne k\), Lemma 1.1(2) and Lemma 3.1(2) give
\[
\begin{gathered}
\operatorname{rank}R_{ik}\le\#\{(p,q):p\ne q,\\
I(a_ib_p,a_kb_q)\ne0\},
\end{gathered}
\]
because the diagonal entries of \(J^{ik}\), which may carry a local term at a common endpoint \(b_p\), do not affect \(\Phi\). Summing over the ordered pairs \(i\ne k\), every unordered pair of independent edges with \(I\ne0\) is counted twice, so the right sides add up to \(2N_I(D)\). Corollary 3.1 of [An intersection inequality for subspaces](an-intersection-inequality-for-subspaces.md), with \(d=s^2=d_n\), gives
\[
\begin{aligned}
2\,d_md_n&\le\sum_{i\ne k}\operatorname{rank}(X_i-Y_k)\\
&\le2N_I(D)\le2\,c(D). \qquad\square
\end{aligned}
\]

**Remark 4.2.** In Zarankiewicz's drawing with \(n\) odd, \(c(D)=d_md_n\) (Proposition 4.1 of [Drawings and crossing numbers](drawings-and-crossing-numbers.md)), so every inequality in the proof is an equality: two independent edges cross at most once, no crossing pair has signed count zero, and the ranks of the matrices \(X_i-Y_k\) add up exactly to \(2d_md_n\).

## 5. Even \(n\) and the formula

**Proposition 5.1** (even \(n\); [OpenAI-B, Section 5.3]). For \(m\ge1\) and even \(n\ge2\), \(\operatorname{cr}(K_{m,n})\ge d_md_n\).

*Proof.* For \(n=2\), \(d_2=0\). Let \(n=2t\ge4\) and let \(D\) be a normal drawing attaining \(\operatorname{cr}(K_{m,n})\) (Theorem 1.2 of [Polygonal drawings](polygonal-drawings.md)). Deleting \(b_r\) and its edges gives a drawing \(D_r\) of \(K_{m,n-1}\), and \(n-1\) is odd. A crossing point of \(D\) lies on edges \(a_ib_p\) and \(a_kb_q\) with \(p\ne q\) (Corollary 4.2 of [Polygonal drawings](polygonal-drawings.md)), so it is a crossing point of \(D_r\) exactly for the \(n-2\) values \(r\ne p,q\). By Proposition 4.1, applied to a normal drawing with no more crossings than \(D_r\) (Theorem 1.2 of [Polygonal drawings](polygonal-drawings.md)), each \(D_r\) has at least \(d_md_{n-1}\) crossings. Hence
\[
\begin{gathered}
(n-2)\,c(D)=\sum_{r=1}^nc(D_r)\ge n\,d_md_{n-1},\\
c(D)\ge\frac{2t}{2t-2}\,d_m\,(t-1)^2\\
=d_m\,t(t-1)=d_md_n . \qquad\square
\end{gathered}
\]

**Theorem 5.2** (Zarankiewicz's formula; [OpenAI-B, Theorem 1.1]). For all integers \(m,n\ge1\),
\[
\begin{gathered}
\operatorname{cr}(K_{m,n})\\
=\Bigl\lfloor\frac m2\Bigr\rfloor\Bigl\lfloor\frac{m-1}2\Bigr\rfloor\Bigl\lfloor\frac n2\Bigr\rfloor\Bigl\lfloor\frac{n-1}2\Bigr\rfloor .
\end{gathered}
\]

*Proof.* The upper bound is Proposition 4.1 of [Drawings and crossing numbers](drawings-and-crossing-numbers.md). For the lower bound, if \(n=1\) the right side is \(0\); if \(n\ge3\) is odd, apply Proposition 4.1 to a normal drawing attaining \(\operatorname{cr}(K_{m,n})\); if \(n\) is even, apply Proposition 5.1. \(\square\)

**Remark 5.3.** The proof gives more than the crossing number. In every normal drawing of \(K_{m,n}\) with \(n\) odd, minimal or not, at least \(d_md_n\) pairs of independent edges have a nonzero signed number of crossings (Proposition 4.1): pairs that cross an even number of times with cancelling signs never help.

## 6. Exercises

**6.1.** Take \(n=3\), so \(s=1\) and \(d=1\), with nodes \(x=(0,1,2)\). Compute the numbers \(B_{pq}\), check that their row and column sums vanish, and compute \(\Phi(S_\prec)\) for the natural order.

**6.2.** For \(K_{3,3}\) (\(m=n=3\)) follow the proof of Proposition 4.1: the \(R_{ik}\) are numbers with \(R_{ik}=X_i-Y_k\) and \(X_i\ne Y_i\). Conclude with Exercise 4.2 of [An intersection inequality for subspaces](an-intersection-inequality-for-subspaces.md) that some two independent edges have nonzero signed crossing number, and hence \(\operatorname{cr}(K_{3,3})\ge1\).

**6.3.** Show that in Proposition 5.1 the number of crossings that survive the deletion of \(b_r\) is \(c(D)-\sum_{\text{edges }e\text{ at }b_r}(\text{crossings on }e)\), and use this to give a second proof of \(\sum_rc(D_r)=(n-2)c(D)\).

## 7. Solutions

**6.1.** \(F'(0)=2\), \(F'(1)=-1\), \(F'(2)=2\), and \(B_{pq}=(x_p-x_q)/(F'(x_p)F'(x_q))\): \(B_{12}=\frac12\), \(B_{13}=-\frac12\), \(B_{21}=-\frac12\), \(B_{23}=\frac12\), \(B_{31}=\frac12\), \(B_{32}=-\frac12\), and \(B_{pp}=0\). Every row and every column sums to \(0\). For the natural order, \(\Phi(S)\) is \(\frac12(B_{12}+B_{13}+B_{23})\) minus \(\frac12(B_{21}+B_{31}+B_{32})\), that is \(\frac14+\frac14=\frac12\ne0\).

**6.2.** Here \(R_{ik}=\Phi(J^{ik})\) are real numbers, \(R_{ik}=X_i-Y_k\), and \(R_{ii}\ne0\). By Exercise 4.2 of the subspace lesson, at least two of the six numbers \(R_{ik}\), \(i\ne k\), are nonzero. A nonzero \(R_{ik}\) requires a nonzero off-diagonal entry of \(J^{ik}\), that is, two independent edges at \(a_i\) and \(a_k\) with \(I\ne0\), which cross. So \(c(D)\ge1\).

**6.3.** The crossings lost by deleting \(b_r\) are those on edges at \(b_r\); a crossing lies on two edges with distinct ends \(b_p\ne b_q\), so it is lost for exactly two values of \(r\). Summing over \(r\), \(\sum_rc(D_r)=nc(D)-2c(D)\).

## References

- [OpenAI-B] OpenAI, *The crossing number of complete bipartite graphs*, OpenAI Math Release preprint, 23 September 2026, Theorem 1.1, Lemma 3.2, Lemma 4.2 and Section 5. https://github.com/openai/math/tree/main/preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026
