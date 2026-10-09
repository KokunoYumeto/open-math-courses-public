# Symmetric forms over finite fields

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves OpenAI's counterexample to the duality conjecture for metric entropy [OpenAI-E, Sections 4 and 5], with the two preceding lessons:

**Theorem 4.1** (OpenAI). For all \(a,b\ge1\) there are \(n\ge1\) and a symmetric convex body \(K\subseteq\mathbb R^n\) such that, for \(L=[-1,1]^n\),
\[
\log N(K,L)>b\log N(L^\circ,a^{-1}K^\circ).
\]

By Corollary 2.2 of [Covering numbers and polar bodies](covering-numbers-and-polar-bodies.md), it suffices to find a matrix with many separated rows whose column combinations have a short approximation list. [Compression by partitions](compression-by-partitions.md) gives the approximation list from partitions with few classes. Here the row set is the space of symmetric \(h\)-linear forms on \(\mathbb F_p^r\), with \(p^{D_h}\) elements, and the partitions are given by contracting a form with a vector \(t_i\), which takes only \(p^{D_{h-1}}\) values. The vectors \(t_i\) are chosen at random so that every nonzero form survives, after deleting a few of the \(t_i\), on all tuples of the remaining ones (Proposition 2.1). A short path between two forms in a partition graph would write their difference as a sum of forms killed by the \(t_i\) along the path, so distinct forms are far apart, and the rows are separated (Proposition 3.1). As \(D_{h-1}/D_h=h/(r+h-1)\) is small, the approximation list is short compared with the number of rows.

We use Lemma 1.1, Lemma 2.1, Theorem 3.2, Lemma 3.3 and Exercise 4.1 of [Covering numbers and polar bodies](covering-numbers-and-polar-bodies.md), and the columns, Proposition 2.1 and Corollary 2.2 of [Compression by partitions](compression-by-partitions.md). Probabilities are uniform probabilities on finite sets.

## 1. Zeros of polynomials over a finite field

Let \(p\) be a prime and \(\mathbb F_p\) the field with \(p\) elements. A nonzero polynomial in one variable of degree \(e\) over \(\mathbb F_p\) has at most \(e\) roots: if \(c\) is a root, division gives \(P=(z-c)P_1\) with \(\deg P_1=e-1\), and a root of \(P\) other than \(c\) is a root of \(P_1\).

**Lemma 1.1** (zero bound, named after Schwartz and Zippel). Let \(P\in\mathbb F_p[z_1,\dots,z_k]\) be a nonzero polynomial of total degree at most \(d\). If \(U_1,\dots,U_k\) are independent and uniform in \(\mathbb F_p\), then \(\Pr(P(U_1,\dots,U_k)=0)\le d/p\).

**Proof.** Induction on \(k\); for \(k=0\), \(P\) is a nonzero constant. For \(k\ge1\) write \(P=\sum_{j=0}^eP_j(z_1,\dots,z_{k-1})z_k^j\) with \(P_e\neq0\), of total degree at most \(d-e\). The probability that \(P_e(U_1,\dots,U_{k-1})=0\) is at most \((d-e)/p\). For each value of \((U_1,\dots,U_{k-1})\) with \(P_e\neq0\), \(P\) becomes a nonzero polynomial of degree \(e\) in \(z_k\), which vanishes at no more than \(e\) of the \(p\) values of \(U_k\). Adding, \(\Pr(P=0)\le(d-e)/p+e/p\). \(\square\)

## 2. Symmetric forms and robust directions

Let \(r,h\) be positive integers, \(E=\mathbb F_p^r\) with basis \(e_1,\dots,e_r\), and \(D_j=\binom{r+j-1}j\). Let \(\operatorname{Sym}^j(E^*)\) be the space of maps \(E^j\to\mathbb F_p\) that are linear in each argument and invariant under permutations of the arguments, with \(\operatorname{Sym}^0(E^*)=\mathbb F_p\).

A symmetric \(j\)-linear form \(Z\) is determined by its values on tuples of basis vectors, and these depend only on the multiset of indices; conversely, any function \(c\) on multisets of \(j\) elements of \([r]\) defines the symmetric form
\[
Z(x^{(1)},\dots,x^{(j)})=\sum_{a_1,\dots,a_j\in[r]}x^{(1)}_{a_1}\cdots x^{(j)}_{a_j}\,c(\{a_1,\dots,a_j\}).
\]
There are \(D_j\) such multisets, so \(\operatorname{Sym}^j(E^*)\) is a vector space of dimension \(D_j\) with \(p^{D_j}\) elements. For \(x\in\operatorname{Sym}^h(E^*)\) and \(t\in E\), the contraction \(x(t,\cdot,\dots,\cdot)\) lies in \(\operatorname{Sym}^{h-1}(E^*)\).

**Proposition 2.1** (robust directions). Let \(0<\theta<1\), put \(w=2D_h\) and \(u=\lceil hw/\theta\rceil\), and let \(p\) be a prime with \(p>h^2u^{2h}\); in particular \(p>h\). There are \(t_1,\dots,t_u\in E\) such that for every nonzero \(Z\in\operatorname{Sym}^h(E^*)\) some \(T\subseteq[u]\) with \(|[u]\setminus T|\le\theta u\) satisfies
\[
Z(t_{i_1},\dots,t_{i_h})\neq0\qquad\text{for all }(i_1,\dots,i_h)\in T^h,\tag{2.1}
\]
repeated indices included.

**Proof.** Choose \(t_1,\dots,t_u\) independently and uniformly in \(E\), so their \(ur\) coordinates are independent and uniform in \(\mathbb F_p\). Fix a nonzero \(Z\), given by \(c\neq0\) as above. Its *diagonal* is
\[
Z(z,\dots,z)=\sum_{\alpha}\frac{h!}{\alpha_1!\cdots\alpha_r!}\,c(\alpha)\,z_1^{\alpha_1}\cdots z_r^{\alpha_r},
\]
the sum over multisets \(\alpha\) of size \(h\), written by multiplicities, since \(\frac{h!}{\alpha!}\) ordered tuples have multiset \(\alpha\). Each coefficient \(\frac{h!}{\alpha!}\) is an integer dividing \(h!\), which is not divisible by the prime \(p>h\), so it is nonzero in \(\mathbb F_p\); and distinct multisets give distinct monomials; so the diagonal is a nonzero polynomial of degree \(h\). For a tuple \(\mathbf i=(i_1,\dots,i_h)\), \(Z(t_{i_1},\dots,t_{i_h})\) is a polynomial of total degree \(h\) in the coordinates of the vectors \(t_i\), \(i\in\{i_1,\dots,i_h\}\); substituting the same variables \(z\) for all these vectors gives the diagonal, so this polynomial is nonzero. By Lemma 1.1,
\[
\Pr\bigl(Z(t_{i_1},\dots,t_{i_h})=0\bigr)\le\frac hp.
\]
Values of \(Z\) on tuples with pairwise disjoint index sets depend on disjoint sets of independent coordinates, so their vanishing events are independent. There are at most \(u^{hw}\) lists of \(w\) tuples and fewer than \(p^{D_h}\) nonzero forms, so the probability that some nonzero \(Z\) vanishes on \(w\) tuples with pairwise disjoint index sets is at most
\[
p^{D_h}u^{hw}\Bigl(\frac hp\Bigr)^w=\Bigl(\frac{h^2u^{2h}}p\Bigr)^{D_h}<1.
\]
Fix vectors for which this does not happen. For a nonzero \(Z\), take a maximal family of tuples on which \(Z\) vanishes with pairwise disjoint index sets; it has at most \(w-1\) members. Let \(T\) be the complement of the union of their index sets, so \(|[u]\setminus T|\le h(w-1)<hw\le\theta u\). A tuple in \(T^h\) on which \(Z\) vanished would have index set disjoint from all those in the family, contradicting maximality. \(\square\)

## 3. Separated rows

**Proposition 3.1** (separated rows). With the parameters and vectors of Proposition 2.1, let \(X=\operatorname{Sym}^h(E^*)\), \(L_i(x)=x(t_i,\cdot,\dots,\cdot)\) for \(i\in[u]\), and \(\mathcal T=\{T\subseteq[u]:|[u]\setminus T|\le\theta u\}\). Then \(|X|=p^{D_h}\), each \(L_i\) takes at most \(q=p^{D_{h-1}}\) values, and every two distinct \(x,y\in X\) have some \(T\in\mathcal T\) with \(d_T(x,y)>h\). Consequently the rows \(R_x=(g_{(v,T)}(x))_{(v,T)\in X\times\mathcal T}\) formed from the columns \(g_{(v,T)}(x)=\phi_h(d_T(x,v))\) of [Compression by partitions](compression-by-partitions.md) satisfy \(\|R_x-R_y\|_\infty=1\) for \(x\neq y\).

**Proof.** The counts were shown in Section 2. Let \(x\neq y\), let \(Z=y-x\neq0\) and let \(T\in\mathcal T\) be given by Proposition 2.1; \(T\) is nonempty because \(|[u]\setminus T|\le\theta u<u\). Suppose there were a path \(x=x_0,x_1,\dots,x_k=y\) with \(1\le k\le h\) in the graph of \(T\). For each step choose \(i_j\in T\) with \(L_{i_j}(x_j)=L_{i_j}(x_{j-1})\); then \(\Delta_j=x_j-x_{j-1}\) satisfies \(\Delta_j(t_{i_j},\cdot,\dots,\cdot)=0\). Take any \(i_*\in T\) and the tuple \((t_{i_1},\dots,t_{i_k},t_{i_*},\dots,t_{i_*})\) of length \(h\). Each \(\Delta_j\) vanishes on it, being symmetric with \(t_{i_j}\) among the arguments, so \(Z=\sum_j\Delta_j\) vanishes on it, contradicting (2.1). Hence \(d_T(x,y)>h\). In the column \((x,T)\), \(g_{(x,T)}(x)=\phi_h(0)=1\) and \(g_{(x,T)}(y)=\phi_h(d_T(y,x))=0\); all values lie in \([0,1]\). \(\square\)

## 4. The counterexample

**Proof of Theorem 4.1.** Fix \(a,b\ge1\). Choose, in this order:

1. \(\theta=\frac1{1000a}\) and \(s=\lceil1/\theta\rceil\);
2. a positive integer \(h\) with \(\frac{\log3}{\log(h+1)}\le\theta\);
3. a positive integer \(r\) with \(r+h-1>8bh^2s\);
4. \(D_j\), \(w=2D_h\), \(u=\lceil hw/\theta\rceil\), and \(C=\log u+hs2^u\log(1+\frac{s2^u}\theta)\);
5. a prime \(p>\max\{h^2u^{2h},\ \exp(8bC/D_h)\}\).

Every bound in step 5 is already determined. Proposition 3.1 gives \(X\) with \(m=|X|=p^{D_h}>1\), labels with at most \(q=p^{D_{h-1}}\) values, and separated rows. Proposition 2.1 of [Compression by partitions](compression-by-partitions.md), with these partitions and the family \(\mathcal T\) (which satisfies (1.1) there by definition), gives an approximation list for the nonnegative combinations with
\[
\log Q\le hs\log q+C=hsD_{h-1}\log p+C,
\]
and Corollary 2.2 of the same lesson gives a list of at most \(Q^2\) functions approximating every signed combination of \(\ell^1\)-norm at most \(1\) within \(6\theta\). Lemma 2.1 of [Covering numbers and polar bodies](covering-numbers-and-polar-bodies.md) with \(\varepsilon=6\theta\) and \(t=\theta\) gives symmetric convex bodies \(K\) and \(L=B_\infty^Y\) in \(\mathbb R^Y\), \(Y=X\times\mathcal T\), with
\[
N(K,L)\ge m,\qquad N(L^\circ,38\theta K^\circ)\le Q^2,
\]
and \(38\theta<a^{-1}\), so \(N(L^\circ,a^{-1}K^\circ)\le Q^2\). Finally \(\frac{D_{h-1}}{D_h}=\frac h{r+h-1}\) gives
\[
\frac{\log(Q^2)}{\log m}\le\frac{2hsD_{h-1}}{D_h}+\frac{2C}{D_h\log p}=\frac{2h^2s}{r+h-1}+\frac{2C}{D_h\log p}<\frac1{4b}+\frac1{4b}
\]
by the choices of \(r\) and \(p\). Hence \(b\log N(L^\circ,a^{-1}K^\circ)\le b\log(Q^2)<\frac12\log m<\log N(K,L)\). Identifying \(\mathbb R^Y\) with \(\mathbb R^n\), \(L=[-1,1]^n\). \(\square\)

**Remark 4.2.** For fixed \(a\), taking \(p>\max\{h^2u^{2h},\exp(rC/D_h)\}\) instead, the bodies \(K_r,L_r\) obtained for \(r=1,2,\dots\) satisfy \(\log N(L_r^\circ,a^{-1}K_r^\circ)/\log N(K_r,L_r)\le\frac{2h^2s}{r+h-1}+\frac2r\to0\). The dimensions of these examples grow very fast.

The two inequalities of the conjecture are exchanged by passing to a polar pair, so the left-hand inequality fails as well:

**Corollary 4.3** (the left-hand inequality). For all \(a,b\ge1\) there are \(n\) and a symmetric convex body \(L\subseteq\mathbb R^n\) such that, for the cross-polytope \(K=B_1^n\), \(\log N(K,L)<\frac1b\log N(L^\circ,aK^\circ)\).

**Proof.** Take \(K_0\) and \(L_0=[-1,1]^n\) from Theorem 4.1, and put \(K=L_0^\circ=B_1^n\) and \(L=a^{-1}K_0^\circ\). By Lemma 1.1 and Exercise 4.1 of [Covering numbers and polar bodies](covering-numbers-and-polar-bodies.md), \(L^\circ=aK_0\) and \(K^\circ=L_0\). Hence \(N(L^\circ,aK^\circ)=N(aK_0,aL_0)=N(K_0,L_0)\) and \(N(K,L)=N(L_0^\circ,a^{-1}K_0^\circ)\), and Theorem 4.1 states that \(\log N(K_0,L_0)>b\log N(L_0^\circ,a^{-1}K_0^\circ)\). \(\square\)

Convexified packing does satisfy a universal duality (Theorem 3.2 of [Covering numbers and polar bodies](covering-numbers-and-polar-bodies.md)), so the theorem also separates it from covering numbers:

**Corollary 4.4** (covering against convexified packing). For all \(\alpha,\beta\ge1\) there are \(n\) and a symmetric convex body \(K\subseteq\mathbb R^n\) such that, for \(L=[-1,1]^n\), \(\log N(K,L)>\beta\log\widehat M(K,\alpha^{-1}L)\).

**Proof.** \(\widehat M\) is unchanged when both arguments are multiplied by the same positive factor, since convex separation is. By Theorem 3.2 and Lemma 3.3 of [Covering numbers and polar bodies](covering-numbers-and-polar-bodies.md), and since \((\alpha^{-1}L)^\circ=\alpha L^\circ\),
\[
\widehat M\bigl(K,\alpha^{-1}L\bigr)\le\widehat M\bigl(\alpha L^\circ,\tfrac12K^\circ\bigr)^2=\widehat M\bigl(L^\circ,\tfrac1{2\alpha}K^\circ\bigr)^2\le N\bigl(L^\circ,\tfrac1{8\alpha}K^\circ\bigr)^2.
\]
Take \(K,L\) from Theorem 4.1 with \(a=8\alpha\) and \(b=2\beta\): then \(\log N(K,L)>2\beta\log N(L^\circ,\frac1{8\alpha}K^\circ)\ge\beta\log\widehat M(K,\alpha^{-1}L)\). \(\square\)

## 5. Exercises

**Exercise 5.1** (easy). Prove \(\frac{D_{h-1}}{D_h}=\frac h{r+h-1}\).

**Exercise 5.2** (medium). The proof of Proposition 2.1 uses \(p>h\) to make the diagonal of a nonzero form nonzero. Show that the conclusion fails when \(p\le h\): for \(p=2\), \(h=2\), \(r=2\), give a nonzero symmetric bilinear form \(Z\) on \(\mathbb F_2^2\) with \(Z(z,z)=0\) for all \(z\), and show that no vectors \(t_1,\dots,t_u\) and no nonempty \(T\) satisfy (2.1) for it.

**Exercise 5.3** (easy). Show that in Proposition 3.1 the contraction \(L_i\) is a linear map \(\operatorname{Sym}^h(E^*)\to\operatorname{Sym}^{h-1}(E^*)\), so that its classes are the cosets of its kernel, and that \(x\) and \(y\) are adjacent in the graph of \(T\) exactly when \(y-x\) is killed by some \(t_i\), \(i\in T\).

## 6. Solutions

**5.1.** \(\binom{r+h-2}{h-1}\big/\binom{r+h-1}h=\frac{(r+h-2)!\,h!\,(r-1)!}{(h-1)!\,(r-1)!\,(r+h-1)!}=\frac h{r+h-1}\).

**5.2.** \(Z(x,y)=x_1y_2+x_2y_1\) is symmetric, bilinear and nonzero, and \(Z(z,z)=2z_1z_2=0\) in characteristic \(2\). A nonempty \(T\) contains some \(i\), and \(Z(t_i,t_i)=0\), so (2.1) fails on the tuple \((i,i)\in T^2\) whatever the vectors are.

**5.3.** \(x\mapsto x(t_i,\cdot,\dots,\cdot)\) is linear in \(x\), so \(L_i(x)=L_i(y)\) iff \(L_i(y-x)=0\), that is, iff \((y-x)(t_i,\cdot,\dots,\cdot)=0\).

## References

- [OpenAI-E] OpenAI, *Counterexamples to the duality conjecture for metric entropy*, OpenAI Math Release preprint, 24 September 2026, Sections 4 and 5. https://github.com/openai/math/blob/main/preprints/Counterexamples-to-the-duality-conjecture-for-metric-entropy-September-24-2026
