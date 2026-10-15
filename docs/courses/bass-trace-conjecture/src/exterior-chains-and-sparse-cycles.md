# Exterior chains and sparse cycles

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The path sums of [Path sums of an idempotent](path-sums-of-an-idempotent.md) are weighted lists of group elements. Projecting every entry to the coset space \(Y=\langle g\rangle\backslash G\) turns them into chains of the full simplex on \(Y\), taken modulo the action of the group \(H=C_G(g)/\langle g\rangle\). In every even dimension these chains are cycles, and their simplices have connected vertex sets in the graph \(Y\). This lesson sets up the exterior algebra on a set, the chain complex of the full simplex and its coinvariants, constructs the cycles, and states the vanishing theorem for sparse cycles on which the proof of the trace theorem rests [OpenAI-BT, Sections 2 and 7].

- The exterior algebra on an ordered set (Section 1).
- The chain complex of the full simplex (Section 2).
- Group actions and coinvariants (Section 3).
- Cycles from path sums (Section 4).
- The sparse-chain vanishing theorem (Section 5).

## 1. The exterior algebra on an ordered set

Let \(Y\) be a set with a total order; for a countable set, take the order of an enumeration. Let \(\Lambda(Y)\) be the complex vector space with basis \(\varepsilon_S\), one for each finite subset \(S\subseteq Y\). For finite subsets \(S\), \(T\) put
\[
\operatorname{inv}(S,T)=\#\{(s,t)\in S\times T:\ s>t\},
\]
and define the product on basis vectors by
\[
\begin{aligned}
&\varepsilon_S\wedge\varepsilon_T=(-1)^{\operatorname{inv}(S,T)}\varepsilon_{S\cup T}\\
&\qquad\text{if }S\cap T=\varnothing,\\
&\varepsilon_S\wedge\varepsilon_T=0\quad\text{if }S\cap T\ne\varnothing,
\end{aligned}
\]
extended bilinearly. Let \(\Lambda^k(Y)\) be the span of the \(\varepsilon_S\) with \(|S|=k\), and identify \(\Lambda^1(Y)\) with the space \(\mathbb C^{(Y)}\) of finitely supported functions on \(Y\), writing \(\varepsilon_y=\varepsilon_{\{y\}}\).

**Lemma 1.1.** (a) The product is associative, with identity \(\varepsilon_\varnothing\).
(b) For finite \(S\), \(T\), \(\varepsilon_S\wedge\varepsilon_T=(-1)^{|S||T|}\varepsilon_T\wedge\varepsilon_S\). Hence elements of \(\Lambda^1(Y)\) anticommute, \(u\wedge u=0\) for \(u\in\Lambda^1(Y)\), and elements of even degree commute with all elements.
(c) If \(y_1<\cdots<y_k\), then \(\varepsilon_{y_1}\wedge\cdots\wedge\varepsilon_{y_k}=\varepsilon_{\{y_1,\ldots,y_k\}}\).

*Proof.* (a) If \(S\), \(T\), \(U\) are pairwise disjoint, both \((\varepsilon_S\wedge\varepsilon_T)\wedge\varepsilon_U\) and \(\varepsilon_S\wedge(\varepsilon_T\wedge\varepsilon_U)\) equal \(\pm\varepsilon_{S\cup T\cup U}\) with the sign \((-1)^{\operatorname{inv}(S,T)+\operatorname{inv}(S,U)+\operatorname{inv}(T,U)}\), since \(\operatorname{inv}(S\cup T,U)=\operatorname{inv}(S,U)+\operatorname{inv}(T,U)\) and \(\operatorname{inv}(S,T\cup U)=\operatorname{inv}(S,T)+\operatorname{inv}(S,U)\). Otherwise both sides are \(0\).
(b) If \(S\cap T=\varnothing\), every pair \((s,t)\) is counted in exactly one of \(\operatorname{inv}(S,T)\), \(\operatorname{inv}(T,S)\), so their sum is \(|S||T|\); otherwise both sides vanish. For \(u=\sum_yc_y\varepsilon_y\), the terms of \(u\wedge u=\sum_{y,y'}c_yc_{y'}\varepsilon_y\wedge\varepsilon_{y'}\) cancel in pairs, and \(\varepsilon_y\wedge\varepsilon_y=0\).
(c) By induction on \(k\): \(\operatorname{inv}(\{y_1,\ldots,y_{k-1}\},\{y_k\})=0\). \(\square\)

For \(u_1,\ldots,u_k\in\Lambda^1(Y)\), the product \(u_1\wedge\cdots\wedge u_k\) lies in \(\Lambda^k(Y)\); by (b) it is multilinear and changes sign when two factors are exchanged. It vanishes when two factors are equal.

**Lemma 1.2.** (a) Let \(V\) be a vector space and \(\Phi:\Lambda^1(Y)^k\to V\) a multilinear map that vanishes whenever two arguments are equal. There is exactly one linear map \(\bar\Phi:\Lambda^k(Y)\to V\) with \(\bar\Phi(u_1\wedge\cdots\wedge u_k)=\Phi(u_1,\ldots,u_k)\) for all \(u_i\).
(b) Let \(L:\Lambda^1(Y)\to\Lambda^1(Y')\) be linear, where \(Y'\) is another ordered set. The linear map \(\Lambda(L)\) with \(\Lambda(L)\varepsilon_S=L\varepsilon_{y_1}\wedge\cdots\wedge L\varepsilon_{y_k}\), for \(S=\{y_1<\cdots<y_k\}\), satisfies \(\Lambda(L)(x\wedge x')=\Lambda(L)x\wedge\Lambda(L)x'\).
(c) For a permutation \(\sigma\) of \(\{0,\ldots,N-1\}\), \(\varepsilon_{\sigma(0)}\wedge\cdots\wedge\varepsilon_{\sigma(N-1)}=\operatorname{sgn}(\sigma)\,\varepsilon_{\{0,\ldots,N-1\}}\).

*Proof.* (a) A multilinear map vanishing on equal arguments changes sign when two arguments are exchanged: expand \(\Phi(\ldots,u+u',\ldots,u+u',\ldots)=0\). Define \(\bar\Phi(\varepsilon_S)=\Phi(\varepsilon_{y_1},\ldots,\varepsilon_{y_k})\) for \(S=\{y_1<\cdots<y_k\}\). The maps \((u_1,\ldots,u_k)\mapsto\bar\Phi(u_1\wedge\cdots\wedge u_k)\) and \(\Phi\) are multilinear and change sign under exchanges, and they agree on basis vectors in increasing order by Lemma 1.1(c); hence on all lists of basis vectors, and by multilinearity everywhere. Uniqueness holds because the \(\varepsilon_S\) span.
(b) For disjoint \(S\), \(T\), the product \(\Lambda(L)\varepsilon_S\wedge\Lambda(L)\varepsilon_T\) is a product of the factors \(L\varepsilon_u\), \(u\in S\cup T\), with the elements of \(S\) first. Moving them into increasing order takes \(\operatorname{inv}(S,T)\) exchanges of adjacent factors of degree one, each contributing \(-1\). This gives \(\Lambda(L)(\varepsilon_S\wedge\varepsilon_T)\). If \(S\cap T\ne\varnothing\), the product contains a repeated factor and vanishes, like \(\varepsilon_S\wedge\varepsilon_T\).
(c) Sort the factors by exchanges of adjacent factors; each exchange contributes \(-1\), and the number of exchanges has the parity of \(\sigma\). \(\square\)

## 2. The chain complex of the full simplex

Put
\[
\begin{gathered}
E_j=\Lambda^{j+1}(Y)\quad(j\ge0),\\
E_{-1}=\Lambda^0(Y)=\mathbb C .
\end{gathered}
\]
For vertices \(y_0,\ldots,y_j\) write \([y_0,\ldots,y_j]=\varepsilon_{y_0}\wedge\cdots\wedge\varepsilon_{y_j}\): this is zero if two vertices coincide, and changes sign when two vertices are exchanged. Let \(\alpha:\Lambda^1(Y)\to\mathbb C\) be the coefficient sum, \(\alpha(\sum c_y\varepsilon_y)=\sum c_y\). By Lemma 1.2(a) there is a linear map \(\partial:E_j\to E_{j-1}\) with
\[
\begin{aligned}
&\partial(u_0\wedge\cdots\wedge u_j)\\
&\ =\sum_{i=0}^j(-1)^i\alpha(u_i)\\
&\ \ \cdot u_0\wedge\cdots\widehat{u_i}\cdots\wedge u_j :
\end{aligned}
\tag{2.1}
\]
the right side is multilinear, and if \(u_a=u_{a+1}\) its terms with \(i\ne a,a+1\) vanish while the two terms \(i=a\), \(i=a+1\) cancel. A multilinear map that vanishes when two adjacent arguments are equal changes sign when two adjacent arguments are exchanged (expand it at \(u+u'\) in both places), and therefore vanishes whenever any two arguments are equal. In particular
\[
\begin{aligned}
&\partial[y_0,\ldots,y_j]\\
&\quad=\sum_{i=0}^j(-1)^i[y_0,\ldots,\widehat{y_i},\ldots,y_j],
\end{aligned}
\]
and \(\partial[y]=1\) in degree \(0\).

**Lemma 2.1.** (a) \(\partial\partial=0\).
(b) For every vertex \(v\) and \(x\in E_j\), \(j\ge-1\), \(\partial(\varepsilon_v\wedge x)+\varepsilon_v\wedge\partial x=x\), where \(\partial x=0\) for \(x\in E_{-1}\). Consequently every \(x\) with \(\partial x=0\) is a boundary, \(x=\partial(\varepsilon_v\wedge x)\), and the complex \(E_*\) is acyclic.

*Proof.* (a) In \(\partial\partial[y_0,\ldots,y_j]\) the list with \(y_a\) and \(y_b\) removed, \(a<b\), occurs twice: removing \(y_a\) first contributes \((-1)^a(-1)^{b-1}\), removing \(y_b\) first contributes \((-1)^b(-1)^a\). The two cancel.
(b) For \(x=u_0\wedge\cdots\wedge u_j\), (2.1) applied to \(\varepsilon_v\wedge u_0\wedge\cdots\wedge u_j\) gives \(\alpha(\varepsilon_v)x-\varepsilon_v\wedge\partial x\), and \(\alpha(\varepsilon_v)=1\). Both sides are linear in \(x\). For \(x\in E_{-1}=\mathbb C\), \(\partial(\varepsilon_v x)=x\). \(\square\)

A *simplicial complex* \(K\) on \(Y\) is a set of nonempty finite subsets of \(Y\), its *simplices*, containing every nonempty subset of each of its members. A simplex with \(j+1\) elements is a \(j\)-simplex. The *augmented oriented chains* of \(K\) are the subspaces
\[
\begin{gathered}
C_j(K)=\operatorname{span}\{\varepsilon_S:\ S\in K,\\
|S|=j+1\}\subseteq E_j ,
\end{gathered}
\]
with \(C_{-1}(K)=\mathbb C\) when \(K\ne\varnothing\). The boundary of \(\varepsilon_S\) is a combination of \(\varepsilon_T\) with \(T\subseteq S\), so \(C_*(K)\) is a subcomplex. The full simplex, consisting of all nonempty finite subsets, has chain complex \(E_*\).

## 3. Group actions and coinvariants

Let a group \(H\) act on \(Y\). Each \(h\in H\) defines a linear map \(\varepsilon_y\mapsto\varepsilon_{hy}\) of \(\Lambda^1(Y)\), and by Lemma 1.2(b) the map \(\Lambda(h)\) is an automorphism of the algebra \(\Lambda(Y)\), with \(\Lambda(h)[y_0,\ldots,y_j]=[hy_0,\ldots,hy_j]\); we write \(hx\) for \(\Lambda(h)x\). This is an action of \(H\) on every \(E_j\). It commutes with \(\partial\), since \(\alpha(hu)=\alpha(u)\). When \(hS=S\), the vector \(h\varepsilon_S\) is \(\pm\varepsilon_S\), with the sign of the permutation of \(S\) induced by \(h\).

For a vector space \(V\) with an action of \(H\), the *coinvariants* are
\[
V_H=V/\operatorname{span}\{hv-v:\ h\in H,\ v\in V\}.
\]
The boundary induces maps \(\partial:(E_j)_H\to(E_{j-1})_H\) with \(\partial\partial=0\). A class \(\bar c\in(E_j)_H\) is a *cycle* if \(\partial\bar c=0\) in \((E_{j-1})_H\); a chain representing it need not have zero boundary in \(E_{j-1}\). A linear functional \(\psi:E_n\to\mathbb C\) is *invariant* if \(\psi(hx)=\psi(x)\); it then defines a functional on \((E_n)_H\), again written \(\psi\). An invariant \(\psi\) is a *cocycle* if \(\psi\circ\partial=0\) on \(E_{n+1}\).

**Lemma 3.1.** Let \(K\) be an \(H\)-invariant simplicial complex on \(Y\) and \(W_j\) the span of the \(\varepsilon_S\) with \(|S|=j+1\) and \(S\notin K\). Then \(E_j=C_j(K)\oplus W_j\) with both summands \(H\)-invariant, and \((E_j)_H=C_j(K)_H\oplus(W_j)_H\). In particular \(C_j(K)_H\to(E_j)_H\) is injective, and a class of \(C_j(K)_H\) whose image in \((E_j)_H\) is a cycle is a cycle in \(C_*(K)_H\).

*Proof.* Every \(h\in H\) maps \(\varepsilon_S\) to \(\pm\varepsilon_{hS}\), and \(hS\in K\) exactly when \(S\in K\). So both summands are invariant, and the subspace spanned by the \(hv-v\) splits accordingly. The last assertion follows because \(\partial\) maps \(C_j(K)\) into \(C_{j-1}(K)\) and the map on coinvariants in degree \(j-1\) is injective. \(\square\)

When \(H\) acts freely on \(Y\), the stabilizer of a finite set \(S\) acts faithfully on \(S\), so it is finite; the complex \(E_*\) is then a resolution of \(\mathbb C\) by modules induced from finite subgroups, and the homology of \((E_*)_H\) is the group homology of \(H\) with complex coefficients (see [Cohomological and geometric dimension](course:eilenberg-ganea-counterexample/cohomological-and-geometric-dimension) for group homology). This interpretation is not used below; the course works directly with the complexes \(E_*\) and \((E_*)_H\).

## 4. Cycles from path sums

Return to the data of [Path sums of an idempotent](path-sums-of-an-idempotent.md): a finitely generated group \(G\), an idempotent \(e\in\operatorname{Mat}_r(\mathbb CG)\), an element \(g\) of infinite order, \(J=C_G(g)\), \(H=J/\langle g\rangle\) acting freely on the graph \(Y=\langle g\rangle\backslash G\) of degree at most \(D\), the sets \(Q_k=J\backslash G^k\) and the path sums \(v_k\). Fix a total order on the countable set \(Y\). For \(k\ge1\) define
\[
\begin{gathered}
\pi_k:\mathbb C^{(Q_k)}\to(E_{k-1})_H,\\
J(h_0,\ldots,h_{k-1})\mapsto\bigl[\,[\bar h_0,\ldots,\bar h_{k-1}]\,\bigr],
\end{gathered}
\]
where the outer bracket is the class in coinvariants. It is well defined: replacing the tuple by \(c\) times it, \(c\in J\), replaces the chain by its translate under \(\bar c\in H\). Put \(b_k=\pi_k(v_k)\) and
\[
z_n=b_{n+1}\in(E_n)_H\qquad(n\ge2\text{ even}).
\]

**Proposition 4.1** ([OpenAI-BT, Proposition 7.3]). Let \(n\ge2\) be even.

1. \(z_n\) is a cycle.
2. Either \(z_n=0\), or \(z_n\) is the image of a cycle of \(C_n(K)_H\) for an \(H\)-invariant simplicial complex \(K\) on \(Y\) with the following properties: every simplex of \(K\) is a face of an \(n\)-simplex of \(K\); \(K\) has finitely many \(H\)-orbits of simplices; and the vertices of every \(n\)-simplex of \(K\) span a connected subgraph of \(Y\).

The graph \(Y\) and its degree bound \(D\) do not depend on \(n\).

*Proof.* (1) The twisted shift \(T\) of Lemma 4.1 in [Path sums of an idempotent](path-sums-of-an-idempotent.md) satisfies \(\overline{gh_0}=\bar h_0\), so it moves the vertex \(\bar h_0\) from the front of the list to the back. This cyclic permutation of \(k\) vertices has sign \((-1)^{k-1}\), so \(\pi_kT=(-1)^{k-1}\pi_k\), and with \(T_*v_k=v_k\),
\[
b_k=\pi_k(T_*v_k)=(-1)^{k-1}b_k .
\]
Hence \(b_k=0\) for even \(k\). Deleting the entry \(i\) of a tuple and then projecting gives the \(i\)-th face of the projected simplex, so by the deletion identities
\[
\begin{aligned}
\partial b_k&=\sum_{i=0}^{k-1}(-1)^i\pi_{k-1}\bigl((d_i)_*v_k\bigr)\\
&=\sum_{i=0}^{k-1}(-1)^ib_{k-1}\qquad(k\ge2).
\end{aligned}
\]
For \(k=n+1\) odd, \(\sum_{i=0}^n(-1)^i=1\), so \(\partial z_n=b_n=0\), as \(n\) is even.

(2) A tuple whose projected vertices are not distinct contributes \(0\). If no tuple with nonzero weight has distinct projected vertices, \(z_n=0\). Otherwise consider a tuple \((h_0,\ldots,h_n)\) with nonzero weight and distinct projected vertices. Its increments \(s_i=h_i^{-1}h_{i+1}\), \(i<n\), lie in \(S_0\), and \(s_i\ne1\) because \(\bar h_{i+1}\ne\bar h_i\); so \(s_i\in S\) and \(\bar h_i\), \(\bar h_{i+1}\) are adjacent. The path \(\bar h_0,\ldots,\bar h_n\) visits all \(n+1\) vertices, so they span a connected subgraph. Let \(K\) consist of the vertex sets of these tuples, their \(H\)-translates, and all their nonempty subsets. Translates of connected vertex sets are connected, since \(H\) acts by graph automorphisms. The finitely many orbits of \(Q_{n+1}\) with nonzero weight give finitely many \(H\)-orbits of \(n\)-simplices, hence of simplices. The defining sum of \(z_n\) is a chain of \(C_n(K)\), and by Lemma 3.1 its class in \(C_n(K)_H\) is a cycle. \(\square\)

## 5. The sparse-chain vanishing theorem

**Theorem 5.1** (sparse-chain vanishing [OpenAI-BT, Theorem 2.1]). For every integer \(D\ge2\) there is an integer \(n_0(D)\) with the following property. Let \(Y\) be the vertex set of a countable connected simple graph in which every vertex has at most \(D\) neighbours, and let a countable group \(H\) act on the graph by automorphisms, freely on vertices. Let \(n\ge n_0(D)\), and let \(K\) be an \(H\)-invariant simplicial complex on \(Y\) such that

1. every simplex of \(K\) is a face of an \(n\)-simplex of \(K\), and \(K\) has finitely many \(H\)-orbits of simplices;
2. the vertices of every \(n\)-simplex of \(K\) span a connected subgraph of \(Y\).

Then every invariant cocycle \(\psi:E_n\to\mathbb C\) vanishes on the image in \((E_n)_H\) of every cycle of \(C_n(K)_H\).

The bound \(n_0(D)\) depends only on \(D\): not on \(H\), \(K\) or \(\psi\). No boundedness of \(\psi\) is assumed; the cocycles that occur need not be bounded, as the signed area of Example 5.2 shows. The proof bounds \(\psi\) only on finitely many basis vectors attached to each simplex of \(K\). The proof occupies [A transport metric with small balls](a-transport-metric-with-small-balls.md), [Separating filtrations](separating-filtrations.md), [Near-minimal separators](near-minimal-separators.md) and [From filtrations to chains](from-filtrations-to-chains.md). Its method develops the separating-set argument of Papasoglu [Papasoglu, Section 2], the separating filtrations of Alpert [Alpert, Lemmas 4, 6, 7] and the use of a parameter space with a free action by Braun and Sauer [Braun–Sauer, Sections 2, 4, 5], which prove bounds for simplicial volume and macroscopic dimension of Riemannian manifolds whose balls have small volume.

The theorem is false in low dimension, and the following example shows why the dimension must grow with \(D\).

**Example 5.2.** Let \(Y=\mathbb Z^2\) with edges between points at distance \(1\), so \(D=4\), and let \(H=\mathbb Z^2\) act by translations. Put \(o=(0,0)\), \(a=(1,0)\), \(b=(0,1)\) and
\[
c=[o,a,a+b]-[o,b,a+b]\in E_2 .
\]
The two triangles have connected vertex sets. Let \(K\) be the complex of their translates and faces. In \(E_1\),
\[
\begin{aligned}
\partial c&=[a,a+b]+[o,a]\\
&\quad-[b,a+b]-[o,b],
\end{aligned}
\]
and in coinvariants \([a,a+b]\) equals \([o,b]\) and \([b,a+b]\) equals \([o,a]\), so the class of \(c\) is a cycle. Its two triangles form the standard triangulation of the torus \(\mathbb R^2/\mathbb Z^2\). The signed area
\[
\psi[y_0,y_1,y_2]=\tfrac12\det(y_1-y_0,\,y_2-y_0)
\]
is alternating, so by Lemma 1.2(a) it defines a functional on \(E_2\). It is invariant under translations, and it is a cocycle (Exercise 6.3). Its value on \(c\) is \(\tfrac12-(-\tfrac12)=1\). So the conclusion of Theorem 5.1 fails for \(D=4\) and \(n=2\): the theorem is a statement about high dimensions, and [A transport metric with small balls](a-transport-metric-with-small-balls.md) gives an explicit admissible value of \(n_0(D)\).

In the application, \(K\) and \(\psi\) come from an idempotent: [A Pfaffian cocycle](a-pfaffian-cocycle.md) constructs, for every \(m\ge1\), an invariant cocycle \(\psi_m\) on \(E_{2m}\) with \(\psi_m(z_{2m})=2^{-m}\lambda\). Choosing \(2m\ge n_0(D)\), Theorem 5.1 and Proposition 4.1 give \(\lambda=0\).

## 6. Exercises

**6.1** (easy). With the order \(1<2<3<4\), compute \(\varepsilon_{\{1,3\}}\wedge\varepsilon_{\{2,4\}}\) and \(\varepsilon_3\wedge\varepsilon_1\wedge\varepsilon_2\).

**6.2** (easy). Let \(H\) act freely on \(Y\) and let \(S\subseteq Y\) be finite and nonempty. Show that the stabilizer \(\{h:hS=S\}\) has at most \(|S|\) elements.

**6.3** (medium). Show that the signed area of Example 5.2 is a cocycle: for any four points \(y_0,\ldots,y_3\) of \(\mathbb Z^2\), \(\sum_{i=0}^3(-1)^i\psi[y_0,\ldots,\widehat{y_i},\ldots,y_3]=0\).

**6.4** (easy). Let \(K\) be an \(H\)-invariant simplicial complex and \(x\in C_j(K)\) a chain whose class in \(C_j(K)_H\) is a cycle. Show that \(\partial x\) is a finite sum of terms \(hw-w\) with \(h\in H\) and \(w\in C_{j-1}(K)\).

**6.5** (medium). Show that the boundary map (2.1) on \(E_0\to E_{-1}\) is the coefficient sum, and that for \(Y\ne\varnothing\) the homology of the augmented complex \(E_*\) vanishes in every degree \(j\ge-1\), including \(j=-1\).

## 7. Solutions

**6.1.** \(\operatorname{inv}(\{1,3\},\{2,4\})=1\), from the pair \((3,2)\), so the product is \(-\varepsilon_{\{1,2,3,4\}}\). For the second, \(\varepsilon_3\wedge\varepsilon_1=-\varepsilon_{\{1,3\}}\), and \(\varepsilon_{\{1,3\}}\wedge\varepsilon_2=-\varepsilon_{\{1,2,3\}}\), so the product is \(\varepsilon_{\{1,2,3\}}\); this agrees with Lemma 1.2(c), since the permutation \((3,1,2)\) is even.

**6.2.** Fix \(y\in S\). If \(hS=S\), then \(hy\in S\). If \(hy=h'y\), then \(h^{-1}h'\) fixes \(y\), so \(h=h'\) by freeness. So \(h\mapsto hy\) is injective from the stabilizer into \(S\).

**6.3.** Put \(u\times v=u_1v_2-u_2v_1\) for \(u,v\in\mathbb Z^2\). Expanding the determinant,
\[
\begin{aligned}
&\det(y_1-y_0,\,y_2-y_0)\\
&\quad=y_1\times y_2-y_0\times y_2+y_0\times y_1 .
\end{aligned}
\]
The function \(\beta[y,y']=\tfrac12\,y\times y'\) is alternating, so it defines a functional on \(E_1\) by Lemma 1.2(a), and the display says \(\psi=\beta\circ\partial\) on \(E_2\). Hence \(\psi\circ\partial=\beta\circ\partial\circ\partial=0\) by Lemma 2.1(a). The functional \(\beta\) is not invariant under translations, although \(\psi\) is.

**6.4.** The class of \(\partial x\) in \(C_{j-1}(K)_H\) is zero, so \(\partial x\) is a finite linear combination \(\sum_i\mu_i(h_iw_i-w_i)\) with \(w_i\in C_{j-1}(K)\), and \(\mu_i(h_iw_i-w_i)=h_i(\mu_iw_i)-\mu_iw_i\).

**6.5.** For \(u_0\in E_0=\Lambda^1(Y)\), (2.1) gives \(\partial u_0=\alpha(u_0)\). Lemma 2.1(b) shows that every cycle in \(E_j\), \(j\ge0\), is a boundary. In degree \(-1\), every element of \(E_{-1}=\mathbb C\) is a cycle, and \(x=\partial(x\,\varepsilon_v)\) for any \(v\in Y\).

## References

- [OpenAI-BT] OpenAI, *The Bass trace conjecture for complex group rings*, OpenAI Math Release preprint, 24 September 2026, Theorem 2.1, Section 7 and Proposition 7.3. https://github.com/openai/math/tree/main/preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026
- [Papasoglu] P. Papasoglu, *Uryson width and volume*, Geometric and Functional Analysis 30 (2020), 574–587; arXiv:1909.03738, Section 2. https://arxiv.org/abs/1909.03738
- [Alpert] H. Alpert, *Simplicial volume and 0-strata of separating filtrations*, arXiv:2211.06362v3. https://arxiv.org/abs/2211.06362
- [Braun–Sauer] S. Braun and R. Sauer, *Volume and macroscopic scalar curvature*, Geometric and Functional Analysis 31 (2021), 1321–1376; arXiv:2012.08999. https://arxiv.org/abs/2012.08999
