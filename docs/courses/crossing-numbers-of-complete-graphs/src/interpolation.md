# Interpolation

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The lower bounds of the course turn the cycle relations of a drawing into statements about polynomials evaluated at chosen real numbers, one for each vertex. This lesson proves the facts about such evaluations that are needed: Lagrange interpolation and the vanishing of weighted sums of low-degree polynomials [OpenAI-B, Section 4], [OpenAI-C, Lemma 3.1], and two interpolation problems in two variables whose nodes form two triangles of a grid [OpenAI-B, Lemma 4.1], [OpenAI-C, Lemma 3.2]. Everything is elementary algebra of polynomials with real coefficients.

- Interpolation in one variable (Section 1).
- Polynomials in two variables (Section 2).
- The odd pattern (Section 3).
- The even pattern (Section 4).

## 1. Interpolation in one variable

We use three facts about polynomials with real coefficients: a nonzero polynomial \(A\) in one variable of degree at most \(d\) has at most \(d\) roots, \(A(c)=0\) exactly when \(t-c\) divides \(A\) [Judson, Corollaries 17.2.3 and 17.2.4], and polynomials in several variables form an integral domain in which degrees in each variable add under multiplication [Judson, Proposition 17.1.4, applied one variable at a time]. Let \(u_1,\ldots,u_N\) be distinct real numbers, the *nodes*, and put
\[
\begin{gathered}
G(t)=\prod_{p=1}^N(t-u_p),\\
G'(u_p)=\prod_{q\ne p}(u_p-u_q)\ne0 .
\end{gathered}
\]

**Lemma 1.1** (Lagrange interpolation). For every polynomial \(A\) of degree at most \(N-1\),
\[
A(t)=\sum_{p=1}^NA(u_p)\,\frac{G(t)}{(t-u_p)\,G'(u_p)} .
\]
Consequently, for any values \(c_1,\ldots,c_N\) there is exactly one polynomial of degree at most \(N-1\) taking the value \(c_p\) at \(u_p\) for every \(p\).

*Proof.* The polynomial \(L_p(t)=\prod_{q\ne p}(t-u_q)/(u_p-u_q)\), which is \(G(t)/\bigl((t-u_p)G'(u_p)\bigr)\), has degree \(N-1\), value \(1\) at \(u_p\) and \(0\) at the other nodes. Both sides of the formula have degree at most \(N-1\) and agree at the \(N\) nodes, so their difference, having \(N\) roots, is zero. For the second statement, \(\sum_pc_pL_p\) takes the prescribed values, and two such polynomials differ by one of degree at most \(N-1\) with \(N\) roots. \(\square\)

**Corollary 1.2** (weights; [OpenAI-B, Section 4], [OpenAI-C, Lemma 3.1]). For every polynomial \(A\) of degree at most \(N-1\), the sum \(\sum_pA(u_p)/G'(u_p)\) is the coefficient of \(t^{N-1}\) in \(A\). In particular
\[
\sum_{p=1}^N\frac{A(u_p)}{G'(u_p)}=0\qquad\text{if }\deg A\le N-2 .
\]
The same holds for polynomials whose coefficients are vectors or matrices, coordinate by coordinate.

*Proof.* Each \(L_p\) has leading coefficient \(1/G'(u_p)\) in degree \(N-1\); compare the coefficients of \(t^{N-1}\) in Lemma 1.1. \(\square\)

The numbers \(1/G'(u_p)\) are the *barycentric weights* of the nodes; they are the weights of the barycentric form of Lagrange interpolation in numerical analysis.

## 2. Polynomials in two variables

For integers \(a,b\ge0\), let \(\mathcal P_{a,b}\) be the space of real polynomials \(P(u,v)\) of degree at most \(a\) in \(u\) and at most \(b\) in \(v\); it has the basis \(u^iv^j\), \(0\le i\le a\), \(0\le j\le b\), and dimension \((a+1)(b+1)\). Put \(\mathcal P_{a,b}=0\) if \(a<0\) or \(b<0\).

**Lemma 2.1.** Let \(P\in\mathcal P_{a,b}\) and \(c\in\mathbb R\).

1. If \(P(c,v)=0\) for all \(v\), then \(P=(u-c)R\) with \(R\in\mathcal P_{a-1,b}\).
2. If \(P(u,c)=0\) for all \(u\), then \(P=(v-c)R\) with \(R\in\mathcal P_{a,b-1}\).
3. If \(P(c,v)\), as a polynomial in \(v\), has more than \(b\) roots, then \(P(c,v)=0\) for all \(v\); similarly in the other variable.

*Proof.* (1) Write \(P=\sum_ip_i(v)u^i\). Since \(u^i-c^i=(u-c)\sum_{j=0}^{i-1}c^ju^{i-1-j}\), we get \(P=(u-c)R+S\) with \(S(v)=\sum_ip_i(v)c^i=P(c,v)\) and \(R\) of degree at most \(a-1\) in \(u\) and at most \(b\) in \(v\). By assumption \(S=0\). (2) is the same with the variables exchanged, and (3) is the root bound in one variable. \(\square\)

For points \((x,y)\) of the plane, evaluation \(P\mapsto P(x,y)\) is the linear functional on \(\mathcal P_{a,b}\) with coordinates \(x^iy^j\) in the monomial basis. Interpolation on a set \(S\) of points asks whether the evaluation map \(\mathcal P_{a,b}\to\mathbb R^S\) is bijective; when \(|S|=(a+1)(b+1)\), it suffices that only the zero polynomial vanishes on \(S\).

## 3. The odd pattern

Let \(s\ge1\) and let \(x_1,\ldots,x_{2s+1}\) be distinct real numbers. The *odd pattern* is the set of index pairs
\[
\begin{gathered}
Q_s=\{(p,q):1\le q<p\le s+1\}\\
\cup\ \{(p,q):s+1<p<q\le 2s+1\},
\end{gathered}
\]
a lower triangle with \(\frac{s(s+1)}2\) pairs and an upper triangle with \(\frac{s(s-1)}2\) pairs, \(s^2\) pairs in all.

**Lemma 3.1** (the odd pattern; [OpenAI-B, Lemma 4.1]). Evaluation at the points \((x_p,x_q)\), \((p,q)\in Q_s\), is a bijection \(\mathcal P_{s-1,s-1}\to\mathbb R^{Q_s}\). Equivalently, the \(s^2\) vectors \(h_{pq}=(x_p^ix_q^j)_{0\le i,j<s}\), \((p,q)\in Q_s\), form a basis of \(\mathbb R^{s^2}\).

*Proof.* Both spaces have dimension \(s^2\), so it suffices to show that a polynomial \(P\in\mathcal P_{s-1,s-1}\) vanishing at all the points is zero. We induct on \(s\). For \(s=1\), \(P\) is a constant and vanishes at the point indexed by \((2,1)\).

Let \(s\ge2\). The lower triangle contains the \(s\) points \((x_{s+1},x_q)\), \(1\le q\le s\). So \(P(x_{s+1},v)\), of degree at most \(s-1\) in \(v\), has \(s\) roots and vanishes identically, and Lemma 2.1 gives \(P=(u-x_{s+1})P_1\) with \(P_1\in\mathcal P_{s-2,s-1}\). The lower triangle also contains the \(s-1\) points \((x_p,x_1)\), \(2\le p\le s\), at which \(u-x_{s+1}\ne0\); so \(P_1(u,x_1)\), of degree at most \(s-2\) in \(u\), has \(s-1\) roots and vanishes identically, and \(P_1=(v-x_1)R\) with \(R\in\mathcal P_{s-2,s-2}\). Thus
\[
P(u,v)=(u-x_{s+1})(v-x_1)R(u,v).
\]
At the remaining points of the pattern both factors are nonzero, so \(R\) vanishes at \((x_p,x_q)\) for \(2\le q<p\le s\) and for \(s+2\le p<q\le2s+1\).

Put
\[
\begin{gathered}
(y_1,\ldots,y_{2s-1})\\
=(x_{s+2},\ldots,x_{2s+1},x_2,\ldots,x_s),
\end{gathered}
\]
distinct numbers, and \(S(u,v)=R(v,u)\in\mathcal P_{s-2,s-2}\). A pair \((p',q')\) of the lower triangle of \(Q_{s-1}\), \(1\le q'<p'\le s\), gives \(S(y_{p'},y_{q'})=R(x_{s+1+q'},x_{s+1+p'})\), a value of \(R\) on the second family, as \(s+2\le s+1+q'\) and \(s+1+p'\le2s+1\). A pair of the upper triangle, \(s<p'<q'\le2s-1\), gives \(S(y_{p'},y_{q'})=R(x_{q'-s+1},x_{p'-s+1})\), a value of \(R\) on the first family, as \(2\le p'-s+1<q'-s+1\le s\). So \(S\) vanishes on the odd pattern for \(y_1,\ldots,y_{2s-1}\), and by induction \(S=0\). Hence \(R=0\) and \(P=0\). \(\square\)

## 4. The even pattern

Let \(s\ge2\) and let \(u_1,\ldots,u_{2s}\) be distinct real numbers. The *even pattern* is
\[
\begin{gathered}
L_s=\{(p,q):1\le q<p\le s\}\\
\cup\ \{(p,q):s<p<q\le 2s\},
\end{gathered}
\]
two triangles with \(\frac{s(s-1)}2\) pairs each, \(s(s-1)\) pairs in all.

**Lemma 4.1** (the even pattern; [OpenAI-C, Lemma 3.2]). Evaluation at the points \((u_p,u_q)\), \((p,q)\in L_s\), is a bijection from \(\mathcal P_{s-1,s-2}\) onto \(\mathbb R^{L_s}\), and also from \(\mathcal P_{s-2,s-1}\) onto \(\mathbb R^{L_s}\).

*Proof.* All three spaces have dimension \(s(s-1)\), so it suffices to prove injectivity; we do so for both spaces together, by induction on \(s\). For \(s=2\) the pattern consists of \((u_2,u_1)\) and \((u_3,u_4)\); a polynomial in \(\mathcal P_{1,0}\) is \(\alpha+\beta u\), which vanishes at the distinct values \(u_2\) and \(u_3\) only if it is zero, and similarly for \(\mathcal P_{0,1}\) with \(u_1\ne u_4\).

Let \(s\ge3\) and let \(P\in\mathcal P_{s-1,s-2}\) vanish on the pattern. Row \(p=s\) of the lower triangle contains the \(s-1\) points \((u_s,u_q)\), \(q<s\), and row \(p=s+1\) of the upper triangle the \(s-1\) points \((u_{s+1},u_q)\), \(s+1<q\le2s\). So \(P(u_s,v)\) and \(P(u_{s+1},v)\), of degree at most \(s-2\) in \(v\), vanish identically, and by Lemma 2.1 twice (the second time after dividing by \(u-u_s\), which is nonzero at \(u=u_{s+1}\)),
\[
\begin{gathered}
P=(u-u_s)(u-u_{s+1})R,\\
R\in\mathcal P_{s-3,s-2}.
\end{gathered}
\]
Delete the indices \(s\) and \(s+1\) and renumber the remaining nodes \(u_1,\ldots,u_{s-1},u_{s+2},\ldots,u_{2s}\) as \(u'_1,\ldots,u'_{2s-2}\). The remaining points of the lower triangle, \(1\le q<p\le s-1\), form the lower triangle of \(L_{s-1}\), and those of the upper triangle, \(s+2\le p<q\le2s\), become \(s-1<p-2<q-2\le2s-2\), the upper triangle of \(L_{s-1}\). The two factors do not vanish there, so \(R\) vanishes on \(L_{s-1}\) for the nodes \(u'\). As \(\mathcal P_{s-3,s-2}=\mathcal P_{(s-1)-2,(s-1)-1}\), the induction hypothesis for the second space gives \(R=0\).

For \(P\in\mathcal P_{s-2,s-1}\) use columns instead: column \(q=1\) of the lower triangle contains the \(s-1\) points \((u_p,u_1)\), \(1<p\le s\), and column \(q=2s\) of the upper triangle the \(s-1\) points \((u_p,u_{2s})\), \(s<p<2s\). Hence \(P=(v-u_1)(v-u_{2s})R\) with \(R\in\mathcal P_{s-2,s-3}\). Deleting the indices \(1\) and \(2s\) and renumbering \(u_2,\ldots,u_{2s-1}\) as \(u'_1,\ldots,u'_{2s-2}\), the remaining points become the pattern \(L_{s-1}\), and the induction hypothesis for the first space, \(\mathcal P_{(s-1)-1,(s-1)-2}\), gives \(R=0\). \(\square\)

## 5. Exercises

**5.1.** For \(N=3\) nodes \(0,1,2\), compute the weights \(1/G'(u_p)\) and check Corollary 1.2 for \(A(t)=1\), \(A(t)=t\) and \(A(t)=t^2\).

**5.2.** Draw the odd pattern \(Q_2\) on the \(5\times5\) grid of index pairs and verify Lemma 3.1 for \(s=2\) directly: a polynomial \(\alpha+\beta u+\gamma v+\delta uv\) vanishing at the four points is zero.

**5.3.** For \(s=2\), show that evaluation at the four points \((x_1,x_2)\), \((x_1,x_3)\), \((x_1,x_4)\), \((x_1,x_5)\) is not injective on \(\mathcal P_{1,1}\), and that evaluation at \((x_2,x_1)\), \((x_3,x_1)\), \((x_2,x_3)\), \((x_3,x_2)\) is injective. The shape of a pattern matters, not only its size.

## 6. Solutions

**5.1.** \(G'(0)=(0-1)(0-2)=2\), \(G'(1)=(1-0)(1-2)=-1\), \(G'(2)=(2-0)(2-1)=2\); the weights are \(\frac12,-1,\frac12\). Then \(\frac12-1+\frac12=0\), \(0-1+1=0\) and \(0-1+2=1\), the leading coefficient of \(t^2\).

**5.2.** \(Q_2=\{(2,1),(3,1),(3,2),(4,5)\}\), the points \((x_2,x_1),(x_3,x_1),(x_3,x_2),(x_4,x_5)\). From \(P(x_3,x_1)=P(x_3,x_2)=0\) and \(x_1\ne x_2\), the linear function \(P(x_3,v)\) vanishes, so \(P=(u-x_3)(\beta+\delta v)\). From \(P(x_2,x_1)=0\) and \(x_2\ne x_3\), \(\beta+\delta x_1=0\), so \(P=\delta(u-x_3)(v-x_1)\). Finally \(P(x_4,x_5)=\delta(x_4-x_3)(x_5-x_1)=0\) forces \(\delta=0\).

**5.3.** The nonzero polynomial \(u-x_1\) vanishes at the first four points. For the second set, let \(P=\alpha+\beta u+\gamma v+\delta uv\) vanish there. Then \(P(x_2,x_1)-P(x_3,x_1)\) is \((x_2-x_3)(\beta+\delta x_1)=0\), and \(P(x_2,x_3)-P(x_3,x_2)\) is \((x_2-x_3)(\beta-\gamma)=0\), so \(\beta=\gamma=-\delta x_1\). With these values, \(P(x_2,x_3)-P(x_2,x_1)\) is \(\delta(x_1-x_2)(x_1-x_3)\), and both values are \(0\); hence \(\delta=0\), then \(\beta=\gamma=0\), and \(\alpha=P(x_2,x_1)=0\).

## References

- [Judson] T. W. Judson, *Abstract Algebra: Theory and Applications*, online edition, Proposition 17.1.4 and Corollaries 17.2.3 and 17.2.4; the text of the core course [Abstract Algebra I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C30). https://judsonbooks.org/aata-files/aata-html/poly-section-division-algorithm.html
- [OpenAI-B] OpenAI, *The crossing number of complete bipartite graphs*, OpenAI Math Release preprint, 23 September 2026, Section 4, Lemma 4.1. https://github.com/openai/math/tree/main/preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026
- [OpenAI-C] OpenAI, *The crossing number of complete graphs*, OpenAI Math Release preprint, 23 September 2026, Section 3, Lemmas 3.1 and 3.2. https://github.com/openai/math/tree/main/preprints/The-crossing-number-of-complete-graphs-September-23-2026
