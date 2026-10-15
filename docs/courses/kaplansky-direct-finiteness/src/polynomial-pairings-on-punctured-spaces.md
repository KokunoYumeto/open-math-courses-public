# Polynomial pairings on punctured spaces

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The incidence criterion of [The glued group and planar balance](the-glued-group-and-planar-balance.md) asks for vectors \(x_v\in K^m\) on the points of an incidence system with
\[
\begin{gathered}
\sum_{v\in f}x_vx_v^{\mathsf T}=0\ \text{ on every line }f,\\
\sum_{v\in V}x_vx_v^{\mathsf T}=-I_m ,
\end{gathered}
\]
and with \(m<|V|\). This lesson constructs such vectors from low-degree polynomials on an affine space \(Q^n\) over a field of characteristic two. Products of two polynomials of degree at most \((q-2)/2\) have degree at most \(q-2\), and such polynomials sum to zero over every full affine line and over the whole space. The interpolation polynomials of a set \(O\) of removed points, the *holes*, have unit vectors as values at the holes, so removing the holes leaves the total \(-I_m\). The lines themselves only have to avoid the holes; their arrangement is the subject of the next three lessons.

- Interpolation on an index simplex (Section 1).
- Sums over affine lines (Section 2).
- The pairing supplied by holes (Section 3).

Let \(Q\) be a finite field with \(q\) elements. Its multiplicative group is cyclic ([Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40): Judson, *Abstract Algebra: Theory and Applications*, Corollary 22.11). Polynomials in \(n\) variables are formal polynomials with coefficients in \(Q\); the *total degree* of a monomial \(X_1^{k_1}\cdots X_n^{k_n}\) is \(k_1+\cdots+k_n\).

## 1. Interpolation on an index simplex

Enumerate \(Q\) as \(a_0,a_1,\ldots,a_{q-1}\). For \(0\le d<q\) and \(n\ge1\) put
\[
\begin{aligned}
S_d=\Bigl\{&(a_{k_1},\ldots,a_{k_n}):\\
&k_i\ge0,\ \sum_ik_i\le d\Bigr\}\subseteq Q^n .
\end{aligned}
\]
Since \(d<q\), every index \(k_i\le d\) is a valid index, distinct index tuples give distinct points, and \(|S_d|=\binom{d+n}{n}\), which is also the number of monomials of total degree at most \(d\).

**Lemma 1.1** (interpolation; [OpenAI-DF2, Lemma 2.1]). Evaluation on \(S_d\) is a linear isomorphism from the space of polynomials of total degree at most \(d\) to the space \(Q^{S_d}\) of functions on \(S_d\).

*Proof.* For an index tuple \(k=(k_1,\ldots,k_n)\) with \(\sum_ik_i\le d\) let
\[
N_k=\prod_{i=1}^n\prod_{0\le u<k_i}(X_i-a_u),
\]
a polynomial of total degree \(\sum_ik_i\le d\). At the point with index tuple \(j\), \(N_k\) vanishes if \(j_i<k_i\) for some \(i\), because the factor with \(u=j_i\) is zero. Order the tuples lexicographically. If \(N_k\) is nonzero at the point \(j\), then \(j_i\ge k_i\) for all \(i\), so \(j\) comes after or equals \(k\). The square matrix of values \(N_k(\text{point }j)\) is therefore triangular, with diagonal entries
\[
N_k(\text{point }k)=\prod_{i=1}^n\prod_{0\le u<k_i}(a_{k_i}-a_u)\ne0 .
\]
So the \(\binom{d+n}{n}\) polynomials \(N_k\) have linearly independent evaluations on \(S_d\). They lie in the polynomial space, which has the same dimension, so they form a basis of it, and evaluation is an isomorphism. \(\square\)

In particular, for each point \(o\in S_d\) there is a unique polynomial \(f_o\) of total degree at most \(d\) that equals \(1\) at \(o\) and \(0\) at the other points of \(S_d\).

## 2. Sums over affine lines

An *affine line* in \(Q^n\) is a translate \(p+Qw\), \(w\ne0\), of a one-dimensional subspace; it has \(q\) points, parametrized by \(z\mapsto p+zw\).

**Lemma 2.1** (line sums; [OpenAI-DF2, Lemma 2.2]). Let \(g\) be a polynomial on \(Q^n\) of total degree at most \(q-2\). Then the sum of the values of \(g\) over every affine line is zero, and so is the sum over \(Q^n\).

*Proof.* Restricted to a line \(z\mapsto p+zw\), \(g\) becomes a polynomial in \(z\) of degree at most \(q-2\). It suffices to show \(\sum_{z\in Q}z^k=0\) for \(0\le k\le q-2\), with \(z^0=1\). For \(k=0\) the sum is \(q\cdot1=0\) in \(Q\). For \(1\le k\le q-2\), choose \(c\in Q^\times\) with \(c^k\ne1\); it exists because \(Q^\times\) is cyclic of order \(q-1>k\). Multiplication by \(c\) permutes \(Q\), so \(\sum_zz^k=\sum_z(cz)^k=c^k\sum_zz^k\), and \((1-c^k)\sum_zz^k=0\) forces the sum to vanish. Finally, \(Q^n\) is a disjoint union of parallel lines. \(\square\)

The bound \(q-2\) is sharp: \(\sum_{z\in Q}z^{q-1}=q-1=-1\) (Exercise 4.2).

## 3. The pairing supplied by holes

**Proposition 3.1** (the pairing supplied by holes; [OpenAI-DF2, Proposition 2.3]). Let \(q\ge4\) be a power of two, \(Q\) a field with \(q\) elements, \(n\ge1\), \(d_0=(q-2)/2\), \(S=S_{d_0}\subseteq\mathcal A=Q^n\) and \(N_{\rm pt}=q^n\). Let \(\ell\) be an odd prime and \(D=\ell+1\). Let \(O\subseteq S\) be a set of *holes* with
\[
\frac{2N_{\rm pt}}{D^2}\le|O|\le\frac{7N_{\rm pt}}{D^2},
\]
and \(\mathcal F\) a family of affine lines contained in \(V=\mathcal A\setminus O\). Let \(K\) be a finite field containing \(Q\). Put \(m=|O|\), \(t=|V|\), and for \(v\in\mathcal A\)
\[
x_v=\bigl(f_o(v)\bigr)_{o\in O}\in Q^m\subseteq K^m ,
\]
with the interpolation polynomials \(f_o\) of total degree at most \(d_0\) of Section 1. Then
\[
\begin{gathered}
0<m<t\le m\ell^2,\\
\sum_{v\in V}x_vx_v^{\mathsf T}=-I_m,\\
\sum_{v\in f}x_vx_v^{\mathsf T}=0\quad(f\in\mathcal F).
\end{gathered}
\]

*Proof.* The entry \((o,o')\) of \(W_v=x_vx_v^{\mathsf T}\) is \(f_o(v)f_{o'}(v)\), the value at \(v\) of a polynomial of total degree at most \(2d_0=q-2\). By Lemma 2.1,
\[
\sum_{v\in f}W_v=0\quad(f\in\mathcal F),\qquad\sum_{v\in\mathcal A}W_v=0 .
\]
For a hole \(o\), the vector \(x_o\) is the unit vector of the coordinate \(o\), because \(f_{o'}(o)=1\) exactly when \(o'=o\) (both lie in \(S\)). Hence \(\sum_{o\in O}W_o=I_m\), and
\[
\sum_{v\in V}W_v=\sum_{v\in\mathcal A}W_v-\sum_{o\in O}W_o=-I_m .
\]
The lines lie in \(V\), so their sums are not affected by the removal.

For the sizes: \(m\ge2N_{\rm pt}/D^2>0\). Since \(\ell\ge3\), \(D\ge4\), and \(m\le7N_{\rm pt}/16<N_{\rm pt}/2\), so \(t=N_{\rm pt}-m>m\). Finally
\[
\begin{aligned}
\frac tm=\frac{N_{\rm pt}}m-1&\le\frac{D^2}2-1\\
&\le(D-1)^2=\ell^2 ,
\end{aligned}
\]
where the last inequality is equivalent to \((D-2)^2\ge0\). \(\square\)

**Remark 3.2.** The identities are consistent with a regular line system only in suitable characteristic. If every point of \(V\) lies on exactly \(D\) lines of \(\mathcal F\), summing the line identities gives \(D\sum_{v\in V}W_v=0\), that is \(-D\,I_m=0\), so the characteristic of \(K\) must divide \(D=\ell+1\) (Exercise 4.4). This is where the characteristic enters the construction: characteristic two divides \(\ell+1\) for every odd prime \(\ell\).

The vectors \(x_v\) are computed by finite-field linear algebra: \(f_o\) is obtained by inverting the triangular matrix of Lemma 1.1.

## 4. Exercises

**4.1** (easy). Let \(q=4\), \(Q=\{0,1,\omega,\omega^2\}\) with \(\omega^2=\omega+1\), \(n=1\), and enumerate \(a_0=0\), \(a_1=1\). Find \(S_1\) and the interpolation polynomials \(f_0\), \(f_1\) of degree at most \(1\), and check \(\sum_{z\in Q}f_0(z)f_1(z)=0\).

**4.2** (easy). Show that \(\sum_{z\in Q}z^{q-1}=-1\), so Lemma 2.1 fails for degree \(q-1\).

**4.3** (medium). Show that the number of affine lines through a point of \(Q^n\) is \((q^n-1)/(q-1)\), and that two distinct affine lines meet in at most one point.

**4.4** (medium). Let \(K\) be any field, \((V,\mathcal F)\) an incidence system in which every point lies on exactly \(D\) lines, and \(W_v\in\operatorname{Mat}_m(K)\) with \(\sum_{v\in f}W_v=0\) for all lines and \(\sum_vW_v=-I_m\), \(m\ge1\). Show that the characteristic of \(K\) divides \(D\).

## 5. Solutions

**4.1.** \(S_1=\{a_0,a_1\}=\{0,1\}\). The polynomials of degree at most one with the prescribed values are \(f_0(z)=1+z\) and \(f_1(z)=z\) (in characteristic two \(-1=1\)). Then \(f_0f_1=z+z^2\), and \(\sum_zz=0+1+\omega+\omega^2=0\), \(\sum_zz^2=\sum_zz=0\), since squaring permutes \(Q\). The degree of \(f_0f_1\) is \(2=q-2\), as Lemma 2.1 requires.

**4.2.** For \(z\ne0\), \(z^{q-1}=1\) because \(Q^\times\) has order \(q-1\), and \(0^{q-1}=0\). So the sum is \((q-1)\cdot1=-1\) in \(Q\).

**4.3.** A line through \(p\) is \(p+Qw\); two nonzero vectors give the same line exactly when they are proportional, so the lines through \(p\) correspond to the \((q^n-1)/(q-1)\) one-dimensional subspaces. If two lines share two points \(p\ne p'\), both are \(p+Q(p'-p)\).

**4.4.** Each point lies on \(D\) lines, so \(\sum_f\sum_{v\in f}W_v=D\sum_vW_v=-D\,I_m\). The left side is zero, so \(D\cdot1=0\) in \(K\).

## References

- [OpenAI-DF2] OpenAI, *A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two*, OpenAI Math Release preprint, 23 September 2026, Section 2 (Lemmas 2.1, 2.2, Proposition 2.3, Remark 2.4). https://github.com/openai/math/tree/main/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026
- [Dyn–Floater] N. Dyn and M. S. Floater, *Multivariate polynomial interpolation on lower sets*, Journal of Approximation Theory 177 (2014), 34–42, on the lower-set interpolation used in Lemma 1.1; free in the publisher's open archive. https://doi.org/10.1016/j.jat.2013.09.008
