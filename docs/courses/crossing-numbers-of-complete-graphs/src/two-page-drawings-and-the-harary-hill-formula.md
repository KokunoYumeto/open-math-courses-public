# Two-page drawings and the Harary–Hill formula

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In a *two-page drawing* the vertices lie on a line, the *spine*, and every edge is drawn in one of the two half-planes it bounds. Two-page drawings of \(K_n\) with \(Z(n)\) crossings go back to Blažek and Koman [Schaefer, entry "Book crossing number"], and the construction used here, in which an edge goes up or down according to the sum of its endpoints modulo \(n\), follows [OpenAI-C, Section 5]. This lesson draws the edges as semicircles, proves that the drawing is admissible and has exactly \(Z(n)\) crossings, and combines this with [The lower bound for complete graphs](the-lower-bound-for-complete-graphs.md) to prove the Harary–Hill formula [OpenAI-C, Theorem 1.1].

- Semicircles (Section 1).
- The drawing (Section 2).
- Counting the crossings (Section 3).
- The formula (Section 4).

## 1. Semicircles

For real numbers \(a<b\), the *upper semicircle* over \([a,b]\) is the set of points \((x,y)\) with \(y\ge0\) and
\[
y^2=(x-a)(b-x),
\]
the upper half of the circle with diameter \([a,b]\) on the horizontal axis; the *lower semicircle* is its mirror image. It is a simple arc from \((a,0)\) to \((b,0)\) whose interior lies in the open half-plane.

**Lemma 1.1** (two semicircles; [OpenAI-C, Section 5]). Let two upper semicircles have diameters \([a,b]\) and \([c,d]\).

1. If \(a,b,c,d\) are distinct, the interiors meet exactly when the endpoints alternate along the axis, \(a<c<b<d\) or \(c<a<d<b\), and then in exactly one point.
2. If they have exactly one common endpoint, they meet only there.
3. Where two semicircles meet at a point off the axis, they cross properly.

*Proof.* (1) A common point of the interiors has \(y>0\), lies over both intervals, and satisfies \(\ell(x)=0\) for
\[
\begin{aligned}
\ell(x)&=(x-a)(b-x)-(x-c)(d-x)\\
&=(a+b-c-d)\,x-ab+cd,
\end{aligned}
\]
an affine function of \(x\). Conversely, a root \(x\) of \(\ell\) inside both intervals gives a common point, with \(y=\sqrt{(x-a)(b-x)}>0\). The function \(\ell\) is not identically zero, as that would force \(a+b=c+d\) and \(ab=cd\), that is \(\{a,b\}=\{c,d\}\). If \(a<c<b<d\), the overlap of the intervals is \((c,b)\), where \(\ell(c)=(c-a)(b-c)>0\) and \(\ell(b)=-(b-c)(d-b)<0\); so \(\ell\) has exactly one root there. If \(a<c<d<b\), the overlap is \((c,d)\) with \(\ell(c)=(c-a)(b-c)>0\) and \(\ell(d)=(d-a)(b-d)>0\), and the affine \(\ell\) is positive on the whole overlap. Disjoint intervals do not overlap. The remaining orders are the same with the roles exchanged.

(2) With \(a=c\) and \(b<d\), \(\ell(x)=(x-a)(b-d)<0\) on the overlap \((a,b)\); with \(b=d\) and \(a<c\), \(\ell(x)=(b-x)(c-a)>0\) on the overlap \((c,b)\). If \(b=c\) or \(a=d\), the two intervals overlap only in the common endpoint.

(3) The semicircles lie on the circles \(f_1=0\) and \(f_2=0\) with \(f_j(x,y)=(x-m_j)^2+y^2-\rho_j^2\), centres \((m_j,0)\) on the axis. At a common point \(z=(x_0,y_0)\) with \(y_0\ne0\) the gradients \(2(x_0-m_1,y_0)\) and \(2(x_0-m_2,y_0)\) are linearly independent, because \(m_1\ne m_2\) (circles with a common point and a common centre coincide). By the inverse function theorem [Lebl, Theorem 8.5.1], \(\Psi=(f_2,f_1)\) maps a neighbourhood of \(z\) homeomorphically onto an open set containing \(0\); choose \(\epsilon>0\) such that the open square \((-\epsilon,\epsilon)^2\) lies in that set and its preimage \(U\) lies in the open half-plane. Then \(\Psi\) maps \(U\) onto the square, the first semicircle (where \(f_1=0\)) onto the horizontal axis of the square, and the second onto the vertical axis. The map \((p,q)\mapsto(p,q)\max(|p|,|q|)/\sqrt{p^2+q^2}\), extended by \(0\mapsto0\), is a homeomorphism of the open square of side \(2\) onto the open unit disc preserving the two axes; after rescaling, it gives the homeomorphism required in Definition 1.1 of [Drawings and crossing numbers](drawings-and-crossing-numbers.md). \(\square\)

## 2. The drawing

Let \(n\ge3\) and \(m=\lfloor n/2\rfloor\). Label the vertices of \(K_n\) by the residues \(0,1,\ldots,n-1\) modulo \(n\), and call the residues \(0,\ldots,m-1\) *low* and \(m,\ldots,n-1\) *high*. Place vertex \(i\) at \((a_i,0)\) with \(a_0<a_1<\cdots<a_{n-1}\), and draw the edge \(\{i,j\}\) as the upper semicircle over the interval between its endpoints if \(i+j\bmod n\) is low, and as the lower semicircle if it is high.

**Proposition 2.1.** The positions \(a_0<\cdots<a_{n-1}\) can be chosen so that this is a drawing of \(K_n\) in the sense of Definition 1.1 of [Drawings and crossing numbers](drawings-and-crossing-numbers.md). Its crossing points are in bijection with the pairs of edges of the same colour whose endpoints alternate along the spine; each such pair crosses once.

*Proof.* Edge interiors lie in the open half-planes, so they contain no vertex, and edges of different colours do not meet except at common endpoints. By Lemma 1.1, two edges of the same colour meet in their interiors exactly when their endpoints alternate, once and properly, and two edges with a common endpoint meet only there. It remains to choose the positions so that no point lies on three edges. Three edges through one interior point have the same colour and pairwise alternating endpoints, so their six endpoints are distinct. Choose \(a_0,a_1,\ldots\) in turn, each in its own interval, the intervals pairwise disjoint and increasing. When \(a_j\) is chosen, consider each pair of edges with endpoints among the earlier vertices that cross, at a point \((x,y)\) with \(y\ne0\), and each earlier vertex \(i\). The semicircle over \([a_i,a_j]\) passes through \((x,y)\) only if \((x-a_i)(a_j-x)=y^2\), which for \(x\ne a_i\) determines \(a_j=x+y^2/(x-a_i)\), and for \(x=a_i\) is impossible. So finitely many values are excluded, and \(a_j\) can be chosen. Three edges through one point would have been excluded when the last of their six endpoints was placed. \(\square\)

## 3. Counting the crossings

**Proposition 3.1** (the count; [OpenAI-C, Proposition 5.1]). The drawing of Proposition 2.1 has exactly \(Z(n)\) crossing points.

*Proof.* *Four vertices.* Every set of four vertices \(\alpha<\beta<\gamma<\delta\) (in the order of the spine) contains exactly one pair of disjoint edges with alternating endpoints, \(\{\alpha,\gamma\}\) and \(\{\beta,\delta\}\). By Proposition 2.1, \(c(D)\) is the number of four-sets for which these two edges have the same colour. Alternation of two disjoint pairs along the spine is the same as alternation in the cyclic order of the residues modulo \(n\).

*Cyclic gaps.* Describe a four-set by one of its elements \(a\) and the gaps \(g_1,g_2,g_3,g_4\ge1\), \(g_1+g_2+g_3+g_4=n\), to the following elements in the cyclic order: the elements are \(a\), \(a+g_1\), \(a+g_1+g_2\), \(a+g_1+g_2+g_3\) modulo \(n\). Every four-set arises from exactly four such descriptions, one for each starting element. The alternating pairs are the first with the third and the second with the fourth element, with endpoint sums
\[
\begin{gathered}
r=2a+g_1+g_2\quad\text{and}\quad r+k,\\
k=g_1+g_3 .
\end{gathered}
\]
Here \(2\le k\le n-2\), and for given \(k\) there are \((k-1)(n-k-1)\) choices of the gaps: \(1\le g_1\le k-1\) and \(1\le g_2\le n-k-1\), the other two then being determined. Hence \(4c(D)\) is the number of descriptions for which \(r\) and \(r+k\) have the same colour.

*The set \(R_k\).* For \(1\le k\le n-1\) let \(R_k\) be the set of residues \(r\) such that \(r\) and \(r+k\) have the same colour, and \(\ell=\min(k,n-k)\le m\). Then \(|R_k|=n-2\ell\). Indeed, if \(k\le n/2\), the colour changes from \(r\) to \(r+k\) exactly for the \(k\) residues \(m-k\le r\le m-1\) (low to high) and the \(k\) residues \(n-k\le r\le n-1\) (high to low, since \(r+k\) wraps around to a residue below \(k\le m\)), so
\[
\begin{gathered}
R_k=\{0,\ldots,m-k-1\}\\
\cup\{m,\ldots,n-k-1\};
\end{gathered}
\]
and \(R_k=R_{n-k}-k\) in general, since \(r\) and \(r+k\) have the same colour exactly when \(r+k\) and \((r+k)+(n-k)\) do.

*Counting over the starting element.* Fix \(k\) and the gaps, and let \(a\) run over all residues. If \(n\) is odd, \(a\mapsto2a+g_1+g_2\) is a bijection of the residues, so exactly \(|R_k|\) values of \(a\) qualify. Let \(n=2m\) be even. Then \(2a+g_1+g_2\) runs twice over the residues of the parity of \(g_1+g_2\), so the number of qualifying \(a\) is twice the number of elements of \(R_k\) of that parity. We show that, summed over the gaps, this still gives \((k-1)(n-k-1)|R_k|\).

- If \(m\) is odd, adding \(m\) exchanges the low and the high residues, so \(R_k+m=R_k\), and it changes parity; so \(R_k\) has as many even as odd elements, and each choice of gaps gives \(|R_k|\).
- If \(m\) and \(k\) are even, then \(R_k\), for \(k\le m\), consists of two intervals of the even length \(m-k\), each with as many even as odd elements; for \(k>m\), \(R_k=R_{n-k}-k\) is the translate of such a set by the even number \(k\). Again each choice of gaps gives \(|R_k|\).
- If \(m\) is even and \(k\) is odd, then for fixed \(g_2\) the \(k-1\) values of \(g_1\), an even number of consecutive integers, give \(g_1+g_2\) each parity equally often. Each parity occurs for \(\frac{k-1}2\) values of \(g_1\) and contributes twice the elements of \(R_k\) of that parity, so the sum over \(g_1\) is \((k-1)|R_k|\), and summing over \(g_2\) gives \((k-1)(n-k-1)|R_k|\).

*Summation.* Therefore
\[
\begin{gathered}
4\,c(D)=\sum_{k=2}^{n-2}f(k),\\
f(k)=(k-1)(n-k-1)\\
\cdot\bigl(n-2\min(k,n-k)\bigr).
\end{gathered}
\]
The function \(f\) satisfies \(f(k)=f(n-k)\), \(f(1)=0\), and \(f(n/2)=0\) if \(n\) is even. Pairing \(k\) with \(n-k\),
\[
\begin{gathered}
c(D)=\frac12\sum_{k=1}^{m}(k-1)(n-k-1)\\
\cdot(n-2k).
\end{gathered}
\]
Put \(B_k=k(k-1)(n-k-1)(n-k-2)\). Then
\[
\begin{gathered}
B_k-B_{k-1}=(k-1)(n-k-1)\\
\cdot\bigl(k(n-k-2)-(k-2)(n-k)\bigr)\\
=2(k-1)(n-k-1)(n-2k),
\end{gathered}
\]
so the sum telescopes to \(c(D)=\frac14(B_m-B_0)=\frac14B_m\). For \(n=2m+1\), \(B_m=m^2(m-1)^2\) and \(c(D)=\binom m2^2=Z(n)\); for \(n=2m\), \(B_m=m(m-1)^2(m-2)\) and \(c(D)=Z(n)\), by (2.2) of [Drawings and crossing numbers](drawings-and-crossing-numbers.md). \(\square\)

## 4. The formula

**Theorem 4.1** (the Harary–Hill formula; [OpenAI-C, Theorem 1.1]). For every integer \(n\ge3\),
\[
\begin{gathered}
\operatorname{cr}(K_n)\\
=\frac14\Bigl\lfloor\frac n2\Bigr\rfloor\Bigl\lfloor\frac{n-1}2\Bigr\rfloor\Bigl\lfloor\frac{n-2}2\Bigr\rfloor\Bigl\lfloor\frac{n-3}2\Bigr\rfloor .
\end{gathered}
\]

*Proof.* The right side is \(Z(n)\). Proposition 3.1 gives \(\operatorname{cr}(K_n)\le Z(n)\), and Theorem 5.1 of [The lower bound for complete graphs](the-lower-bound-for-complete-graphs.md) gives \(\operatorname{cr}(K_n)\ge Z(n)\). \(\square\)

Together with Theorem 5.2 of [The Zarankiewicz formula](the-zarankiewicz-formula.md) this proves both theorems stated in [Drawings and crossing numbers](drawings-and-crossing-numbers.md). For \(n=5,\ldots,12\) the values \(1,3,9,18,36,60,100,150\) agree with the values known before 2026 [Schaefer, entry "Crossing number"].

## 5. Exercises

**5.1.** For \(n=5\) (\(m=2\)), list the low edges (endpoint sum \(0\) or \(1\) modulo \(5\)) and the high edges, and find the unique crossing of the drawing.

**5.2.** For \(n=6\) (\(m=3\)), compute \(|R_k|\) for \(k=2,3,4\) and the sum \(\sum_kf(k)\), and check that it equals \(4Z(6)=12\).

**5.3.** Show that if all edges of \(K_n\) are drawn as upper semicircles, the drawing has \(\binom n4\) crossings, and compare with \(Z(n)\) for \(n=5,6\).

## 6. Solutions

**5.1.** The low edges, with endpoint sum \(0\) or \(1\) modulo \(5\), are \(\{0,1\}\), \(\{1,4\}\), \(\{2,3\}\), \(\{2,4\}\); the other six edges are high. The five four-sets have the alternating pairs \((\{0,2\},\{1,3\})\), \((\{0,2\},\{1,4\})\), \((\{0,3\},\{1,4\})\), \((\{0,3\},\{2,4\})\) and \((\{1,3\},\{2,4\})\). Only the first consists of two edges of the same colour, both high. So the only crossing is between \(\{0,2\}\) and \(\{1,3\}\), and \(c(D)=1=Z(5)\).

**5.2.** \(m=3\), so \(|R_k|=6-2\min(k,6-k)\): \(|R_2|=2\), \(|R_3|=0\), \(|R_4|=2\). Then \(f(2)=1\cdot3\cdot2=6\), \(f(3)=2\cdot2\cdot0=0\), \(f(4)=3\cdot1\cdot2=6\), and \(\sum_kf(k)=12=4\cdot3\).

**5.3.** By Lemma 1.1 two upper semicircles cross exactly when their endpoints alternate, and every four-set has exactly one alternating pair, so there are \(\binom n4\) crossings (after choosing positions as in Proposition 2.1). For \(n=5\) this is \(5>1\), and for \(n=6\) it is \(15>3\).

## References

- [Lebl] J. Lebl, *Basic Analysis I & II*, version 6.3, Theorem 8.5.1 (inverse function theorem); the text of the core course [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20). https://www.jirka.org/ra/html/sec_svinvfuncthm.html#thm_inverse
- [OpenAI-C] OpenAI, *The crossing number of complete graphs*, OpenAI Math Release preprint, 23 September 2026, Theorem 1.1 and Section 5, Proposition 5.1. https://github.com/openai/math/tree/main/preprints/The-crossing-number-of-complete-graphs-September-23-2026
- [Schaefer] M. Schaefer, *The graph crossing number and its variants: a survey*, Electron. J. Combin., Dynamic Survey DS21, ninth edition, 17 July 2026, entries "Book crossing number" and "Crossing number". https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS21
