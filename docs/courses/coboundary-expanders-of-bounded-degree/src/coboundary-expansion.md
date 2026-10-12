# Coboundary expansion

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A graph is an expander if every set of vertices has many edges leaving it, in proportion to its size. Coboundary expansion is the corresponding property of simplicial complexes of higher dimension: it compares the size of a set of faces with the size of the set of faces of the next dimension that contain an odd number of them. In September 2026 OpenAI released a proof that for every dimension \(d\ge3\) there are arbitrarily large complexes that are coboundary expanders with a common constant, and in which every vertex lies in a bounded number of faces [OpenAI-C]. This lesson gives the definitions, proves the basic properties, and states the theorem.

- Cochains with coefficients in the field \(\mathbb F_2\), the coboundary map, cocycles and coboundaries (Section 1).
- The weights of the faces form a probability distribution in every dimension, and \(\|\delta f\|\le(i+2)\|f\|\) (Lemmas 2.1 and 2.2).
- A coboundary expander has no cohomology below its dimension. Conversely an inequality relative to the cocycles, together with the vanishing of cohomology, gives coboundary expansion (Proposition 3.2).
- For graphs the definition is edge expansion. The full simplex of dimension \(s\) is a coboundary expander with the constants \((s+1)/(s-i)\) (Section 4).
- Passing to a skeleton changes the weights by controlled factors and keeps an expansion inequality (Lemma 5.1, Corollary 5.2).

The lesson follows [OpenAI-C, Section 1 and the part of Section 5 on weights]. It uses only finite sets, counting, and vector spaces over \(\mathbb F_2\) (core course [Linear Algebra](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B40)).

## 1. Cochains and coboundaries

A *simplicial complex* \(Y\) is here a finite collection of finite sets, its *faces*, such that every subset of a face is a face. For \(i\ge-1\) let \(Y(i)\) be the set of the faces with \(i+1\) elements; such a face has *dimension* \(i\). So \(Y(-1)\) consists of the empty face, the elements of \(Y(0)\) are the *vertices*, and those of \(Y(1)\) the *edges*. The dimension of \(Y\) is the largest dimension of a face. The complex is *pure of dimension \(s\)* if every face is contained in a face of dimension \(s\).

Let \(\mathbb F_2=\{0,1\}\) be the field with two elements. A *cochain of degree \(i\)* is a function \(f\colon Y(i)\to\mathbb F_2\); these functions form the vector space \(C^i(Y)\). A cochain is determined by its *support*, the set of the faces on which it is \(1\), and the sum of two cochains has as support the symmetric difference of the supports. The *coboundary map* \(\delta_i\colon C^i(Y)\to C^{i+1}(Y)\) is
\[
(\delta_if)(\tau)=\sum_{\sigma\in Y(i),\ \sigma\subset\tau}f(\sigma).
\]
So the support of \(\delta_if\) consists of the faces of dimension \(i+1\) that contain an odd number of faces of the support of \(f\). For \(i=-1\), \(\delta_{-1}\) sends the value at the empty face to the constant function on the vertices.

**Lemma 1.1.** \(\delta_{i+1}\delta_i=0\).

**Proof.** For \(\rho\in Y(i+2)\), \((\delta\delta f)(\rho)\) is the sum of \(f(\sigma)\) over the pairs \(\sigma\subset\tau\subset\rho\) with \(\sigma\in Y(i)\), \(\tau\in Y(i+1)\). A face \(\sigma\subset\rho\) of dimension \(i\) misses two elements of \(\rho\), so it lies in exactly two such \(\tau\). Every term occurs twice, and the sum is \(0\) in \(\mathbb F_2\). \(\blacksquare\)

Let \(Z^i(Y)\) be the kernel of \(\delta_i\), the *cocycles*, and \(B^i(Y)\) the image of \(\delta_{i-1}\), the *coboundaries*. By Lemma 1.1, \(B^i\subseteq Z^i\); the quotient \(H^i(Y)=Z^i/B^i\) is the *cohomology* of \(Y\) with coefficients in \(\mathbb F_2\), reduced in degree \(0\). In degree \(0\), \(B^0\) consists of the two constant functions on the vertices, and \(Z^0\) of the functions that take the same value at the two ends of every edge. So \(H^0(Y)=0\) exactly when the graph of the vertices and edges of \(Y\) is connected (Exercise 7.1).

## 2. Weights

Let \(Y\) be pure of dimension \(s\). For a face \(\sigma\) let \(c(\sigma)\) be the number of faces of dimension \(s\) that contain \(\sigma\). The *weight* of \(\sigma\in Y(i)\), for \(0\le i\le s\), is
\[
w_i(\sigma)=\frac{c(\sigma)}{\binom{s+1}{i+1}\,|Y(s)|},
\]
and the *norm* of a cochain \(f\in C^i(Y)\) is the total weight of its support,
\[
\|f\|=\sum_{\sigma:\ f(\sigma)=1}w_i(\sigma).
\]
When the complex or the degree has to be named we write \(w_i^Y\) and \(\|f\|_{Y,i}\).

**Lemma 2.1.**

1. \(w_i(\sigma)>0\) for every \(\sigma\in Y(i)\), and \(\sum_{\sigma\in Y(i)}w_i(\sigma)=1\).
2. \(\|f+g\|\le\|f\|+\|g\|\), and \(\|f\|=0\) only for \(f=0\).
3. For \(i<s\) and \(\sigma\in Y(i)\), the sum over the faces \(\tau\in Y(i+1)\) that contain \(\sigma\) satisfies
\[
\sum_{\tau\supset\sigma}w_{i+1}(\tau)=(i+2)\,w_i(\sigma).
\]

**Proof.** (1) Positivity holds because \(Y\) is pure. Count the pairs \((\sigma,\rho)\) with \(\sigma\in Y(i)\), \(\rho\in Y(s)\) and \(\sigma\subset\rho\): grouped by \(\sigma\) the number is \(\sum_\sigma c(\sigma)\), and grouped by \(\rho\) it is \(\binom{s+1}{i+1}|Y(s)|\).

(2) The support of \(f+g\) is contained in the union of the supports, and all weights are positive.

(3) Count the pairs \((\tau,\rho)\) with \(\sigma\subset\tau\subset\rho\), \(\tau\in Y(i+1)\), \(\rho\in Y(s)\). Grouped by \(\tau\) the number is \(\sum_\tau c(\tau)\). Grouped by \(\rho\) it is \((s-i)\,c(\sigma)\), because \(\tau\) is obtained from \(\sigma\) by adding one of the \(s-i\) elements of \(\rho\) outside \(\sigma\). Since \(\binom{s+1}{i+2}=\binom{s+1}{i+1}\tfrac{s-i}{i+2}\), division by \(\binom{s+1}{i+2}|Y(s)|\) gives the claim. \(\blacksquare\)

By (1) the weights are a probability distribution on \(Y(i)\): choose a face of dimension \(s\) uniformly at random, and then one of its faces of dimension \(i\) uniformly at random. The norm \(\|f\|\) is the probability that \(f\) is \(1\) at the face so chosen.

**Lemma 2.2.** For \(f\in C^i(Y)\) with \(0\le i<s\), \(\|\delta_if\|\le(i+2)\,\|f\|\).

**Proof.** Every face in the support of \(\delta_if\) contains a face of the support of \(f\). So \(\|\delta_if\|\) is at most the sum, over the faces \(\sigma\) of the support of \(f\), of the total weight of the faces \(\tau\in Y(i+1)\) containing \(\sigma\), which is \((i+2)w_i(\sigma)\) by Lemma 2.1(3). \(\blacksquare\)

For a subspace \(A\subseteq C^i(Y)\) and \(f\in C^i(Y)\) let
\[
\operatorname{dist}(f,A)=\min_{a\in A}\|f-a\| .
\]
The minimum exists because \(A\) is finite. By Lemma 2.1(2), \(\operatorname{dist}(f,A)=0\) exactly when \(f\in A\).

## 3. Expansion

**Definition 3.1.** Let \(\varepsilon>0\). A pure complex \(Y\) of dimension \(s\) is an *\(\varepsilon\)-coboundary expander* if for every \(i\) with \(0\le i<s\) and every \(f\in C^i(Y)\)
\[
\|\delta_if\|\ge\varepsilon\,\operatorname{dist}(f,B^i(Y)).
\]

A cochain close to a coboundary can have a small coboundary; the definition asks that this is the only way to have a small coboundary.

**Proposition 3.2.** Let \(Y\) be pure of dimension \(s\) and \(0\le i<s\).

1. For every \(f\in C^i(Y)\), \(\|\delta_if\|\le(i+2)\operatorname{dist}(f,Z^i)\).
2. If \(\|\delta_if\|\ge\varepsilon\operatorname{dist}(f,B^i)\) for all \(f\in C^i(Y)\), with some \(\varepsilon>0\), then \(H^i(Y)=0\).
3. If \(H^i(Y)=0\) and \(\|\delta_if\|\ge\eta\operatorname{dist}(f,Z^i)\) for all \(f\in C^i(Y)\), then \(\|\delta_if\|\ge\eta\operatorname{dist}(f,B^i)\) for all \(f\).

**Proof.** (1) For \(z\in Z^i\), \(\delta_if=\delta_i(f-z)\), and Lemma 2.2 gives \(\|\delta_if\|\le(i+2)\|f-z\|\). (2) For \(f\in Z^i\) the left side is \(0\), so \(\operatorname{dist}(f,B^i)=0\) and \(f\in B^i\). (3) \(Z^i=B^i\). \(\blacksquare\)

So a coboundary expander is connected and has no cohomology in the degrees below its dimension, and coboundary expansion consists of two parts: an inequality relative to the cocycles, and the vanishing of cohomology. By (1) the constants \(\varepsilon\) and \(\eta\) cannot be larger than \(i+2\), unless every cochain of degree \(i\) is a cocycle.

## 4. Two examples

**Example 4.1 (graphs).** Let \(Y\) be a graph in which every vertex lies on an edge, with vertex set \(V\) and edge set \(E\); it is pure of dimension \(1\). An edge has the weight \(1/|E|\), and a vertex \(v\) the weight \(\deg(v)/(2|E|)\). Let \(f\) be the function that is \(1\) on a set \(A\subseteq V\) and \(0\) outside. The support of \(\delta_0f\) is the set \(E(A,V\setminus A)\) of the edges with exactly one end in \(A\), and \(B^0\) consists of \(0\) and the constant \(1\). Let \(\operatorname{vol}(A)=\sum_{v\in A}\deg(v)\), and let \(\nu(A)\) be the smaller of \(\operatorname{vol}(A)\) and \(\operatorname{vol}(V\setminus A)\). Then
\[
\begin{gathered}
\|\delta_0f\|=\frac{|E(A,V\setminus A)|}{|E|},\\
\operatorname{dist}(f,B^0)=\frac{\nu(A)}{2|E|}.
\end{gathered}
\]
So \(Y\) is an \(\varepsilon\)-coboundary expander exactly when every set \(A\) of vertices satisfies
\[
|E(A,V\setminus A)|\ge\frac\varepsilon2\,\nu(A).
\]
This is the edge expansion of graphs.

**Example 4.2 (the full simplex).** Let \(Y\) consist of all subsets of a set \(V\) with \(s+1\) elements. It is pure of dimension \(s\) with one face of dimension \(s\), and every face of dimension \(i\) has the weight \(1/\binom{s+1}{i+1}\).

**Proposition 4.3.** For the full simplex of dimension \(s\), for \(0\le i<s\) and \(f\in C^i(Y)\),
\[
\|\delta_if\|\ge\frac{s+1}{s-i}\,\operatorname{dist}(f,B^i(Y)).
\]

**Proof.** Write \(\sigma+v\) for \(\sigma\cup\{v\}\) and \(\sigma-u\) for \(\sigma\setminus\{u\}\). For a vertex \(v\) and \(j\ge0\) define \(c_v\colon C^j(Y)\to C^{j-1}(Y)\) by \((c_vg)(\sigma)=g(\sigma+v)\) if \(v\notin\sigma\), and \((c_vg)(\sigma)=0\) if \(v\in\sigma\). This is possible because every subset of \(V\) is a face. We claim that for \(f\in C^i(Y)\)
\[
f=c_v\delta_if+\delta_{i-1}c_vf .
\]
Let \(\sigma\in Y(i)\). If \(v\notin\sigma\), then \((c_v\delta_if)(\sigma)=(\delta_if)(\sigma+v)\) is \(f(\sigma)\) plus the sum of \(f(\sigma+v-u)\) over \(u\in\sigma\), and \((\delta_{i-1}c_vf)(\sigma)\) is the sum of \((c_vf)(\sigma-u)=f(\sigma-u+v)\) over \(u\in\sigma\); the two sums cancel. If \(v\in\sigma\), then \((c_v\delta_if)(\sigma)=0\), and in \((\delta_{i-1}c_vf)(\sigma)\) only the term with \(u=v\) is different from zero, and it is \(f(\sigma)\).

By the claim \(f-c_v\delta_if\in B^i\), so \(\operatorname{dist}(f,B^i)\le\|c_v\delta_if\|\) for every vertex \(v\). Let \(g=\delta_if\) and let \(G\) be its support. The support of \(c_vg\) consists of the sets \(\tau-v\) with \(\tau\in G\) and \(v\in\tau\). Summing over the \(s+1\) vertices, each \(\tau\in G\) is counted \(i+2\) times, so
\[
\begin{gathered}
\sum_{v\in V}\|c_vg\|=\frac{(i+2)\,|G|}{\binom{s+1}{i+1}},\\
\|g\|=\frac{|G|}{\binom{s+1}{i+2}} .
\end{gathered}
\]
Since \(\binom{s+1}{i+2}=\binom{s+1}{i+1}\tfrac{s-i}{i+2}\), the average of \(\|c_vg\|\) over the vertices is \(\tfrac{s-i}{s+1}\|g\|\). The smallest of the numbers \(\|c_vg\|\) is at most the average. \(\blacksquare\)

So a single simplex is a coboundary expander, with constants larger than \(1\). The same holds for the complex of all subsets with at most \(s+1\) elements of a larger set (Corollary 5.3). In such a complex the number of faces at a vertex grows with the number of vertices. The problem solved in [OpenAI-C] is to find large coboundary expanders in which every vertex lies in a bounded number of faces.

## 5. Skeletons

Let \(T\) be a pure complex of dimension \(n\) and \(0\le s\le n\). The *\(s\)-skeleton* \(X=\operatorname{skel}_sT\) consists of the faces of \(T\) of dimension at most \(s\). It is pure of dimension \(s\). For \(i\le s\) the cochains of degree \(i\) of \(X\) and of \(T\) are the same, and so are the maps \(\delta_i\) for \(i<s\). Hence \(Z^i(X)=Z^i(T)\) for \(i<s\) and \(B^i(X)=B^i(T)\) for \(i\le s\). The weights are different, because those of \(X\) count faces of dimension \(s\) and those of \(T\) faces of dimension \(n\).

**Lemma 5.1.** Let \(T\) be pure of dimension \(n\), \(X=\operatorname{skel}_sT\), and for \(\tau\in T(s)\) let \(c(\tau)\) be the number of faces of dimension \(n\) containing \(\tau\). Suppose \(a\le c(\tau)\le b\) for all \(\tau\in T(s)\), with \(a>0\), and let
\[
\Lambda=\frac{\binom{n+1}{s+1}\,|T(n)|}{|T(s)|}.
\]
Then for \(0\le i\le s\) and every \(\sigma\in T(i)\)
\[
\frac\Lambda b\,w_i^T(\sigma)\le w_i^X(\sigma)\le\frac\Lambda a\,w_i^T(\sigma).
\]
Consequently \(\tfrac\Lambda b\|f\|_{T,i}\le\|f\|_{X,i}\le\tfrac\Lambda a\|f\|_{T,i}\) for every cochain \(f\) of degree \(i\le s\), and the same inequalities hold for the distances from a subspace.

**Proof.** For \(i=s\): \(w_s^X(\tau)=1/|T(s)|\) and \(w_s^T(\tau)=c(\tau)/(\binom{n+1}{s+1}|T(n)|)\), so \(w_s^X(\tau)=\Lambda\,w_s^T(\tau)/c(\tau)\).

For \(i<s\) we show that both weights of \(\sigma\in T(i)\) are averages of the weights in degree \(s\):
\[
w_i(\sigma)=\binom{s+1}{i+1}^{-1}\sum_{\tau\supset\sigma}w_s(\tau),
\]
the sum over the faces \(\tau\in T(s)\) that contain \(\sigma\), for \(w=w^X\) and for \(w=w^T\). For \(w^X\) this is the definition, since \(w_s^X\) is constant. For \(w^T\), count the pairs \((\tau,\rho)\) with \(\sigma\subset\tau\subset\rho\), \(\tau\in T(s)\), \(\rho\in T(n)\): the sum of \(c(\tau)\) over \(\tau\supset\sigma\) is \(\binom{n-i}{s-i}\) times the number \(c_n(\sigma)\) of faces of dimension \(n\) containing \(\sigma\). So the right side for \(w^T\) is
\[
\frac{\binom{n-i}{s-i}\,c_n(\sigma)}{\binom{s+1}{i+1}\binom{n+1}{s+1}\,|T(n)|},
\]
and
\[
\binom{n+1}{s+1}\binom{s+1}{i+1}=\binom{n+1}{i+1}\binom{n-i}{s-i},
\]
because both count the pairs of a subset with \(s+1\) elements and a subset of it with \(i+1\) elements in a set with \(n+1\) elements. Summing the inequalities of degree \(s\) over \(\tau\supset\sigma\) gives the inequalities of degree \(i\). The statements about norms and distances follow by summing over supports. \(\blacksquare\)

**Corollary 5.2.** In the situation of Lemma 5.1 let \(i<s\), let \(A\) be a subspace of \(C^i(T)\), and suppose \(\|\delta_if\|_{T,i+1}\ge\eta\operatorname{dist}_{T,i}(f,A)\) for all \(f\in C^i(T)\). Then for all \(f\)
\[
\|\delta_if\|_{X,i+1}\ge\frac{a\,\eta}b\,\operatorname{dist}_{X,i}(f,A).
\]

**Proof.** By Lemma 5.1,
\[
\begin{gathered}
\|\delta_if\|_{X,i+1}\ge\frac\Lambda b\,\|\delta_if\|_{T,i+1},\\
\operatorname{dist}_{T,i}(f,A)\ge\frac a\Lambda\,\operatorname{dist}_{X,i}(f,A).
\end{gathered}
\]
The factor \(\Lambda\) cancels. \(\blacksquare\)

The factor \(\Lambda\) can be very large or very small; what matters is that it is the same in the two consecutive degrees.

**Corollary 5.3.** Let \(X\) be the complex of all subsets with at most \(s+1\) elements of a set with \(n+1\) elements, where \(1\le s\le n\). Then for \(0\le i<s\) and \(f\in C^i(X)\)
\[
\|\delta_if\|\ge\frac{n+1}{n-i}\,\operatorname{dist}(f,B^i(X)).
\]

**Proof.** \(X\) is the \(s\)-skeleton of the full simplex \(T\) of dimension \(n\). Every face of dimension \(s\) lies in the one face of dimension \(n\), so \(a=b=1\) in Lemma 5.1, and \(\Lambda=1\) because \(|T(s)|=\binom{n+1}{s+1}\). So the weights of \(X\) and \(T\) agree in the degrees up to \(s\). The cochains, the maps \(\delta_i\) and the spaces \(B^i\) agree as well, and the inequality is Proposition 4.3 for \(T\). \(\blacksquare\)

In this complex every vertex lies in \(\binom ns\) faces of dimension \(s\).

## 6. The theorem

**Theorem 6.1** ([OpenAI-C, Theorem 1.1]). For every integer \(d\ge3\) there are numbers \(D\) and \(\varepsilon>0\) and connected pure simplicial complexes \(X_m\) of dimension \(d\), for \(m=2,3,\dots\), such that the number of vertices of \(X_m\) tends to infinity, every vertex of every \(X_m\) lies in at most \(D\) faces of dimension \(d\), and every \(X_m\) is an \(\varepsilon\)-coboundary expander.

This lesson does not prove the theorem. The proof in [OpenAI-C] has three parts.

- The complexes are given explicitly: \(X_m\) is the \(d\)-skeleton of a complex \(T_m\) of dimension \(2d\) built from cosets of subgroups of a finite group of matrices over the ring \(\mathbb F_q[t]/(t^m)\). The bound for the number of faces at a vertex and the growth of the number of vertices are elementary.
- An inequality relative to the cocycles for the skeleton of dimension \(2d-1\) of \(T_m\), with a constant independent of \(m\), is taken from a theorem of I. Oppenheim and I. Valentiner-Branth on a class of complexes that contains the \(T_m\). Corollary 5.2 carries it to \(X_m\).
- The vanishing of \(H^i(T_m)\) for \(1\le i\le d-1\) is the new part. Its proof uses an infinite complex inside a building and the homology of groups.

By Proposition 3.2(3) the second and third part together give the theorem. According to [OpenAI-C, Section 1], graphs give the case \(d=1\), and the case \(d=2\) is a theorem of M. Chapman and A. Lubotzky; the notion of coboundary expansion goes back to the work of N. Linial, R. Meshulam and N. Wallach on random complexes and of M. Gromov.

## 7. Exercises

**7.1.** Show that \(Z^0(Y)\) consists of the functions on the vertices that are constant on every connected component of the graph of vertices and edges, and that \(H^0(Y)=0\) exactly when this graph is connected.

**7.2.** Let \(Y\) be the triangle graph, with three vertices and three edges. Find the largest \(\varepsilon\) for which \(Y\) is an \(\varepsilon\)-coboundary expander.

**7.3.** Show that for the full simplex and \(i=s-1\) the constant \(s+1\) of Proposition 4.3 cannot be improved.

**7.4.** Let \(T\) be a pure complex of dimension \(n\) in which every face of dimension \(n-1\) lies in exactly \(q\) faces of dimension \(n\), and \(X\) its skeleton of dimension \(n-1\). Show that the weights of \(X\) and \(T\) agree in all degrees \(i\le n-1\).

## 8. Solutions

**7.1.** \((\delta_0f)(\{u,v\})=f(u)+f(v)\), which is \(0\) exactly when \(f(u)=f(v)\). So \(f\in Z^0\) exactly when \(f\) takes equal values at the ends of every edge, that is, when \(f\) is constant along every path. \(B^0\) consists of the two constant functions. They are all of \(Z^0\) exactly when there is one component.

**7.2.** Up to symmetry and exchange of \(A\) with its complement, the only set to consider is a single vertex \(A\). Then \(|E(A,V\setminus A)|=2\), \(\operatorname{vol}A=2\) and \(\operatorname{vol}(V\setminus A)=4\). By Example 4.1 the condition is \(2\ge\tfrac\varepsilon2\cdot2\), so the largest \(\varepsilon\) is \(2\). This is the largest value that Proposition 3.2(1) allows in degree \(0\).

**7.3.** Let \(f\) be \(1\) on one face \(\sigma_0\) of dimension \(s-1\) and \(0\) elsewhere. Then \(\delta f\) is \(1\) on the face of dimension \(s\), so \(\|\delta f\|=1\). Every cochain \(f-b\) with \(b\in B^{s-1}\) has the same coboundary, so it is not zero and has norm at least \(1/(s+1)\), the weight of one face. So \(\operatorname{dist}(f,B^{s-1})=1/(s+1)\), and \(\|\delta f\|=(s+1)\operatorname{dist}(f,B^{s-1})\).

**7.4.** In Lemma 5.1 with \(s=n-1\) we have \(a=b=q\). Counting the pairs of a face of dimension \(n-1\) and a face of dimension \(n\) containing it gives \(q\,|T(n-1)|=(n+1)\,|T(n)|\), so \(\Lambda=\binom{n+1}n|T(n)|/|T(n-1)|=q\). Hence \(\Lambda/a=\Lambda/b=1\), and Lemma 5.1 gives \(w_i^X=w_i^T\) for \(i\le n-1\).

## References

- [OpenAI-C] OpenAI, *Bounded-degree coboundary expanders in every dimension*, OpenAI Math Release preprint, 24 September 2026, Sections 1 and 5. https://github.com/openai/math/tree/main/preprints/Bounded-degree-coboundary-expanders-in-every-dimension-September-24-2026
