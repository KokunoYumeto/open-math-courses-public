# The exterior resolution needed for odd primary bordism

<a id="DG-CHAR-13F-resolution.proof"></a>

We give an explicit free resolution over an exterior algebra, induce it on the correct module side, and compute the possible Ext degrees. The [Thom-module calculation](odd-primary-thom-module.md) supplies the actual module to which it will be applied.

## A free resolution over an exterior algebra

Let \(k\) be a field of odd characteristic. Let

\[
E=\Lambda_k(Q_0,Q_1,\ldots),\qquad |Q_i|=d_i,
\]

where every \(d_i\) is a positive odd integer. Thus \(Q_i^2=0\) and \(Q_iQ_j=-Q_jQ_i\) for \(i\ne j\). Let \(k\) be the trivial graded left \(E\)-module, by the augmentation sending every \(Q_i\) to zero. Infinite exterior algebras and direct sums below are algebraic: each element has finite support.

For every finitely supported sequence \(\alpha=(\alpha_0,\alpha_1,\ldots)\) of nonnegative integers, introduce a symbol \(g_\alpha\) of homological degree \(\|\alpha\|=\sum_i\alpha_i\) and internal degree \(\sum_i\alpha_i d_i\). Define the free graded left \(E\)-modules

\[
P_s=\bigoplus_{\|\alpha\|=s}E g_\alpha,
\qquad
d(g_\alpha)=\sum_{i:\alpha_i>0}Q_i g_{\alpha-e_i}.
\tag{1}
\]

Extend \(d\) by left \(E\)-linearity. The map has homological degree \(-1\) and internal degree zero. There is **one summand per distinct index** \(i\), not \(\alpha_i\) summands. In particular, \(g_{n e_i}\) is a divided-power symbol for purposes of this resolution, not an ordinary monomial to which a polynomial derivative is applied. No multiplication on the symbols is required.

The augmentation \(P_0\to k\) sends \(a g_0\) to the augmentation of \(a\). Equation (1) defines a complex: terms with the same index in \(d^2\) contain \(Q_i^2=0\), and the two terms with distinct indices \(i,j\) have coefficient \(Q_iQ_j+Q_jQ_i=0\). This argument also covers repeated entries of \(\alpha\).

Here is an explicit contraction of its positive-weight part. Write \(Q_I=Q_{i_1}\cdots Q_{i_m}\), where \(I=\{i_1<\cdots<i_m\}\) is a finite set. These elements form the exterior basis. For the basis element \(Q_I g_\alpha\), put

\[
\beta=\alpha+\mathbf1_I.
\]

The differential preserves \(\beta\). For fixed \(\beta\ne0\), let \(S=\{i:\beta_i>0\}\) and \(j=\min S\). The basis elements of this weight space are exactly

\[
Q_I g_{\beta-\mathbf1_I},\qquad I\subseteq S.
\]

Right multiplication by \(Q_i\), followed by increasing-order rewriting, gives

\[
d\bigl(Q_I g_{\beta-\mathbf1_I}\bigr)
=\sum_{i\in S\setminus I}
(-1)^{\#\{u\in I:u>i\}}
Q_{I\cup\{i\}}g_{\beta-\mathbf1_{I\cup\{i\}}}.
\tag{2}
\]

Define the \(k\)-linear map of homological degree \(+1\)

\[
h\bigl(Q_I g_{\beta-\mathbf1_I}\bigr)=
\begin{cases}
(-1)^{\#\{u\in I:u>j\}}
Q_{I\setminus\{j\}}g_{\beta-\mathbf1_{I\setminus\{j\}}},&j\in I,\\
0,&j\notin I.
\end{cases}
\tag{3}
\]

The internal degree is unchanged. The map \(h\) is not asserted to be \(E\)-linear; a \(k\)-linear contraction suffices for exactness of a complex of \(E\)-modules.

We check \(dh+hd=1\), including the signs. If \(j\notin I\), then \(h\) first is zero, and after \(d\) only its \(i=j\) term survives under \(h\). The two signs are both \((-1)^{\#\{u\in I:u>j\}}\), so their product is (1). If \(j\in I\), the \(i=j\) term of \(dh\) gives the original element with coefficient (1). For each \(i\ne j\), adding \(i\) and removing \(j\) in the two orders gives opposite signs: the sign exponents differ by

\[
\mathbf1_{i>j}+\mathbf1_{j>i}=1\pmod2.
\]

Thus all off-diagonal terms cancel. The choice \(j\in S\) is fixed on the entire weight subcomplex; neither operation changes \(\beta\). This also proves the identity when some \(\beta_i>1\).

Weight zero consists only of \(k g_0\) in degree zero and maps isomorphically to the augmented \(k\). Give this two-term complex the inverse augmentation as its contraction. Consequently

\[
\cdots\longrightarrow P_2\longrightarrow P_1\longrightarrow P_0
\longrightarrow k\longrightarrow0
\tag{4}
\]

is exact. Every chain is a finite sum of weight components, so the proof remains valid for infinitely many generators. Each \(P_s\) is free over \(E\); (4) is a free graded \(E\)-resolution of \(k\).

The absence of multiplicities in (1) is necessary. In characteristic \(p\), the alternative rule \(d(g_{n e_0})=nQ_0g_{(n-1)e_0}\) gives \(d(g_{p e_0})=0\). In the one-generator complex, no boundary has a nonzero \(g_{p e_0}\) coefficient, since every differential has coefficient divisible by \(Q_0\). It therefore introduces a false positive-degree homology class.

## Induction to a larger graded algebra

Let \(A\) be an augmented graded \(k\)-algebra containing \(E\), and suppose \(A\) is free as a graded **right** \(E\)-module. This side matters because \(P_s\) is a left \(E\)-module. A direct sum of shifted copies of \(E\) preserves exact sequences when tensored over \(E\): tensoring each copy is a grading shift of the original sequence, and exactness of a direct sum is checked component by component. Thus

\[
A\otimes_E P_\bullet\longrightarrow A\otimes_E k
\tag{5}
\]

is an exact complex of free graded **left** \(A\)-modules. Its differential on the free generators is again (1), now with \(Q_i\in A\). The target is the quotient left module \(A/AE_+\). Nothing here identifies that left ideal with a two-sided ideal without further hypotheses.

Suppose a graded left \(A\)-module \(M\) is actually given with an isomorphism

\[
M\cong\bigoplus_{\lambda}\Sigma^{m_\lambda}(A\otimes_E k).
\tag{6}
\]

Taking the corresponding direct sum of shifts of (5) is a free resolution of \(M\). Applying graded \(A\)-linear maps into the trivial module \(k\) gives zero cochain differential: each differential entry is one of the \(Q_i\), and every \(Q_i\) acts by zero on \(k\). Under the convention that a free generator of internal degree \(t\) contributes to \(\operatorname{Ext}^{s,t}_A(M,k)\), the possible bidegrees are exactly those of the resolution generators:

\[
s=\sum_i\alpha_i,
\qquad
t=m_\lambda+\sum_i\alpha_i d_i.
\tag{7}
\]

If the index sets are infinite, Hom of a direct sum is a product; this does not introduce a class in an absent bidegree. No finite-dimensionality assumption is needed for the vanishing conclusion below.

## The odd prime degree calculation

Let \(p\) be odd, set \(d_i=2p^i-1\), and assume every \(m_\lambda\) is divisible by four. The index \(i=0\) is included: \(d_0=1\), and this generator accounts for the degree-one Bockstein. From (7),

\[
t-s=m_\lambda+\sum_i2\alpha_i(p^i-1)\equiv0\pmod4.
\tag{8}
\]

Hence the hypotheses (5)–(6) imply

\[
\operatorname{Ext}^{s,t}_A(M,k)=0
\quad\text{whenever }t-s\not\equiv0\pmod4.
\tag{9}
\]

In particular the entire stem \(t-s=7\) vanishes. This is an algebraic conclusion about the stated module \(M\), not yet a calculation of a bordism group.

## Application to the actual Thom module

The [full operation-algebra computation](odd-primary-one-group-cohomology.md), Section 9, and the [Thom-module calculation](odd-primary-thom-module.md), Sections 2–5, supply the hypotheses of (5)–(6) for \(M=H^*(MSO;\mathbb F_p)\). Consequently (9) applies. [Finite Adams-tower detection](finite-adams-tower-detection.md) gives the required homotopy divisibility, and the [bounding theorem](oriented-seven-manifold-bounding.md) eliminates the remaining finite primary groups.

René Thom, [*Travaux de Milnor sur le cobordisme*](https://www.numdam.org/item/SB_1958-1960__5__169_0.pdf), p. 173, describes this exterior-generator resolution. Equations (2)–(3) specify its contraction and signs.
