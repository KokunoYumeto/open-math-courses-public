# The lower bound for complete graphs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves \(\operatorname{cr}(K_n)\ge Z(n)\) [OpenAI-C, Corollary 4.4], the lower half of the Harary–Hill formula. For odd \(n=2s+1\), a real number \(t_i\) is attached to every vertex, and a polynomial in four variables, symmetric in the two endpoints of each of two edges, is evaluated at the pairs of independent edges whose signed crossing count is not zero. The cycle pairing of [Signed crossings and cycles](signed-crossings-and-cycles.md), applied to cycles whose coefficients are weighted powers of the \(t_i\), gives two facts: the evaluation determines the polynomial, and the evaluations of any two polynomials are orthogonal for a nondegenerate diagonal form. An isotropic subspace has at most half the dimension of the space, so there are at least twice as many crossing pairs as the dimension \(\binom s2^2\) of the space of polynomials. Even \(n\) follows by deleting vertices.

- Cycles with polynomial coefficients (Section 1).
- The order pairing (Section 2).
- The evaluation map (Section 3).
- The odd lower bound (Section 4).
- All \(n\) (Section 5).

## 1. Cycles with polynomial coefficients

Let \(n\ge3\) and let \(D\) be a normal drawing of \(K_n\) (Definition 1.1 of [Polygonal drawings](polygonal-drawings.md)) with vertices \(1,\ldots,n\). Orient the edges in any way, choose cuts, and let \(J\) be the form of Definition 1.2 of [Signed crossings and cycles](signed-crossings-and-cycles.md). For distinct \(i,p\) let \([ip]\) be the edge \(\{i,p\}\) as an element of the edge space with the sign of the direction from \(i\) to \(p\): it is the basis vector if the edge is oriented from \(i\) to \(p\), and its negative otherwise; put \([ii]=0\). Then \([pi]=-[ip]\) and \(\partial[ip]=p-i\). As \(J\) does not depend on the orientations (Section 1 of [Signed crossings and cycles](signed-crossings-and-cycles.md)), we may compute \(J([ip],[kq])\) with the edges oriented from \(i\) to \(p\) and from \(k\) to \(q\):

- for \(\{i,p\}\cap\{k,q\}=\varnothing\), \(J([ip],[kq])=I\), the signed number of crossings of the two edges in these directions;
- for \(p\ne q\), both different from \(i\), \(J([ip],[iq])=\frac12T_i(ip,iq)\), because adjacent edges do not cross and both point out of \(i\).

Choose distinct real numbers \(t_1,\ldots,t_n\), put \(F(t)=\prod_i(t-t_i)\) and \(w_i=1/F'(t_i)\).

**Lemma 1.1** (polynomial cycle tests; [OpenAI-C, Lemma 4.1]). For every polynomial \(H(x,u,y,v)\) of degree at most \(n-2\) in each of its four variables,
\[
\begin{gathered}
\sum_{i,p,k,q=1}^nJ([ip],[kq])\,w_iw_pw_kw_q\\
\cdot H(t_i,t_p,t_k,t_q)=0 .
\end{gathered}
\]

*Proof.* Both sides are linear in \(H\), so let \(H=x^au^by^cv^e\) with \(a,b,c,e\le n-2\). For \(a,b\le n-2\) put
\[
z_{a,b}=\sum_{i,p=1}^nw_iw_p\,t_i^at_p^b\,[ip] .
\]
Its boundary is
\[
\begin{aligned}
\partial z_{a,b}&=\sum_{i,p}w_iw_pt_i^at_p^b\,(p-i)\\
&=\Bigl(\sum_iw_it_i^a\Bigr)\sum_pw_pt_p^b\,p\\
&\quad-\Bigl(\sum_pw_pt_p^b\Bigr)\sum_iw_it_i^a\,i=0,
\end{aligned}
\]
because \(\sum_iw_it_i^a=0\) for \(a\le n-2\) by Corollary 1.2 of [Interpolation](interpolation.md). So \(z_{a,b}\) and \(z_{c,e}\) are cycles, and Theorem 1.3 of [Signed crossings and cycles](signed-crossings-and-cycles.md) gives \(J(z_{a,b},z_{c,e})=0\); expanded by bilinearity, this is the stated identity for \(H=x^au^by^cv^e\). \(\square\)

## 2. The order pairing

For integers \(a,b\) let \(\mathcal P_{a,b}\) be the polynomials in two variables of degree at most \(a\) in the first and \(b\) in the second (Section 2 of [Interpolation](interpolation.md)).

**Lemma 2.1** (order pairing; [OpenAI-C, Lemma 3.3]). Let \(s\ge2\), let \(u_1,\ldots,u_{2s}\) be distinct real numbers, \(G(t)=\prod_p(t-u_p)\), and \(\prec\) a linear order of \(\{1,\ldots,2s\}\). Let \(S(p,q)=\frac12\) if \(p\prec q\), \(S(p,q)=-\frac12\) if \(q\prec p\), \(S(p,p)=0\), and for polynomials \(A,B\) in two variables put
\[
\begin{gathered}
\kappa_{pq}=\frac{u_p-u_q}{G'(u_p)\,G'(u_q)},\\
M(A,B)=\sum_{p,q=1}^{2s}S(p,q)\,\kappa_{pq}\\
\cdot A(u_p,u_q)\,B(u_p,u_q).
\end{gathered}
\]

1. The bilinear form \(M\) on \(\mathcal P_{s-1,s-2}\times\mathcal P_{s-2,s-1}\) is nondegenerate: only \(A=0\) pairs to zero with all \(B\), and only \(B=0\) with all \(A\).
2. If \(A\in\mathcal P_{s-2,s-2}\) and \(M(A,B)=0\) for every \(B\in\mathcal P_{s-1,s-1}\), then \(A=0\).

*Proof.* (1) Let \(A\in\mathcal P_{s-1,s-2}\) and \(B\in\mathcal P_{s-2,s-1}\). The polynomial \((u-v)A(u,v)B(u,v)\) has degree at most \(2s-2\) in each variable. Hence, by Corollary 1.2 of [Interpolation](interpolation.md) with \(2s\) nodes, replacing \(S(p,q)\) by \(S(p,q)+r_p+c_q\) does not change \(M(A,B)\): for fixed \(p\) the sum over \(q\) of \((u_p-u_q)A(u_p,u_q)B(u_p,u_q)/G'(u_q)\) vanishes, and likewise for fixed \(q\). The diagonal values of \(S\) do not matter, because of the factor \(u_p-u_q\).

Renumber the indices so that \(\prec\) becomes the natural order; the nodes remain arbitrary distinct numbers and \(G\) does not change. Off the diagonal \(S(p,q)=\frac12-\mathbf 1_{q<p}\), and
\[
\begin{gathered}
K(p,q)=S(p,q)-\tfrac12+\mathbf1_{p>s}\\
=\begin{cases}-1,&1\le q<p\le s,\\ \ 1,&s<p<q\le2s,\\ \ 0,&\text{otherwise, }p\ne q,\end{cases}
\end{gathered}
\]
differs from \(S\) by a row term. So
\[
\begin{gathered}
M(A,B)=\sum_{(p,q)\in L_s}K(p,q)\,\kappa_{pq}\\
\cdot A(u_p,u_q)\,B(u_p,u_q),
\end{gathered}
\]
the sum over the even pattern \(L_s\) of Section 4 of [Interpolation](interpolation.md). By Lemma 4.1 there, evaluation on \(L_s\) identifies both \(\mathcal P_{s-1,s-2}\) and \(\mathcal P_{s-2,s-1}\) with \(\mathbb R^{L_s}\). In these coordinates \(M\) is the diagonal form with the nonzero coefficients \(K(p,q)\,\kappa_{pq}\), which is nondegenerate.

(2) \(\mathcal P_{s-2,s-2}\subseteq\mathcal P_{s-1,s-2}\) and \(\mathcal P_{s-2,s-1}\subseteq\mathcal P_{s-1,s-1}\); apply (1). \(\square\)

The lemma is a counterpart of Lemma 3.1 of [The Zarankiewicz formula](the-zarankiewicz-formula.md) for an even number of nodes: the weighted pairing detects the linear order of the nodes, whatever it is.

## 3. The evaluation map

From here on \(n=2s+1\) with \(s\ge2\). Let \(\mathcal T\) be the set of ordered pairs \((\{i,p\},\{k,q\})\) of disjoint edges with \(J([ip],[kq])\ne0\); this condition does not depend on the orientations. Each such pair crosses at least once, different unordered pairs cross at different points, and every unordered pair gives two ordered ones, so
\[
|\mathcal T|\le2\,c(D).\tag{3.1}
\]

Let \(\mathcal S\) be the space of polynomials \(P(x,u,y,v)\) of degree at most \(s-2\) in each variable that are symmetric under exchanging \(x\) and \(u\) and under exchanging \(y\) and \(v\) (not necessarily under exchanging the pairs). The symmetric polynomials in two variables of degree at most \(s-2\) in each have the basis \(x^au^b+x^bu^a\) (\(a<b\)) and \(x^au^a\), with \(0\le a\le b\le s-2\), so they form a space of dimension \(\binom s2\), and
\[
\dim\mathcal S=\binom s2^2 .\tag{3.2}
\]
The *evaluation map* \(E:\mathcal S\to\mathbb R^{\mathcal T}\) is
\[
E(P)_{(\{i,p\},\{k,q\})}=P(t_i,t_p,t_k,t_q),
\]
well defined by the two symmetries.

**Lemma 3.1** (injectivity; [OpenAI-C, Lemma 4.2]). The map \(E\) is injective.

*Proof.* Let \(P\in\mathcal S\) with \(E(P)=0\).

*Step 1: vanishing at a common endpoint.* Let \(U,V\) be polynomials in one variable of degree at most \(s\), and \(B\in\mathcal P_{s-1,s-1}\). Apply Lemma 1.1 to
\[
\begin{gathered}
H(x,u,y,v)=P(x,u,y,v)\\
\cdot(u-v)(u-y)(v-x)\\
\cdot U(x)\,V(y)\,B(u,v),
\end{gathered}
\]
whose degrees in \(x,u,y,v\) are at most \((s-2)+1+s\), \((s-2)+2+(s-1)\), \((s-2)+1+s\) and \((s-2)+2+(s-1)\), all equal to \(2s-1=n-2\). Consider the terms \((i,p,k,q)\). If the two edges are disjoint, either \(J([ip],[kq])=0\) or the pair lies in \(\mathcal T\) and \(P(t_i,t_p,t_k,t_q)=0\). If \(i=p\) or \(k=q\), the edge vector is \(0\). The factor \((u-v)(u-y)(v-x)\) vanishes when \(p=q\), \(p=k\) or \(q=i\). The only remaining terms have \(i=k\) and \(p,q\) distinct and different from \(i\), where \(J([ip],[iq])=\frac12T_i(ip,iq)=:S_i(p,q)\). Writing \(F_i(t)=\prod_{p\ne i}(t-t_p)\), we have \((t_p-t_i)w_p=1/F_i'(t_p)\) for \(p\ne i\), and the identity of Lemma 1.1 becomes
\[
\sum_{i=1}^nw_i^2\,U(t_i)V(t_i)\,\Psi_i(B)=0,
\]
where, with \(\kappa^{(i)}_{pq}=(t_p-t_q)/\bigl(F_i'(t_p)F_i'(t_q)\bigr)\),
\[
\begin{gathered}
\Psi_i(B)=\sum_{p,q\ne i}S_i(p,q)\,\kappa^{(i)}_{pq}\\
\cdot P(t_i,t_p,t_i,t_q)\,B(t_p,t_q).
\end{gathered}
\]
Every polynomial of degree at most \(2s=n-1\) is a sum of products \(U(t)V(t)\) with \(\deg U,\deg V\le s\), one monomial at a time. Taking for this polynomial the Lagrange polynomial that is \(1\) at \(t_i\) and \(0\) at the other nodes (Lemma 1.1 of [Interpolation](interpolation.md)), linearity gives \(w_i^2\Psi_i(B)=0\), so \(\Psi_i(B)=0\) for every \(i\) and every \(B\in\mathcal P_{s-1,s-1}\).

For fixed \(i\), \(\Psi_i(B)\) is the order pairing of Lemma 2.1 for the \(2s\) nodes \(t_p\), \(p\ne i\), with \(G=F_i\), the order of the edges at \(i\) given by the cut, and \(A_i(u,v)=P(t_i,u,t_i,v)\in\mathcal P_{s-2,s-2}\). By Lemma 2.1(2), \(P(t_i,u,t_i,v)=0\) for every \(i\).

*Step 2: division by the differences.* As a polynomial in \(x\), with coefficients polynomials in \(u,v\), \(P(x,u,x,v)\) has degree at most \(2s-4\) and vanishes at the \(n=2s+1\) numbers \(t_i\), so it is zero. Divide \(P\), as a polynomial in \(y\) with coefficients in the polynomials in \(x,u,v\), by the monic \(y-x\): the remainder is \(P(x,u,x,v)=0\), so \(P=(y-x)P_1\). By the symmetries, \(P\) also vanishes when \(v=x\), when \(y=u\) and when \(v=u\): for instance \(P(x,u,y,x)=P(x,u,x,y)=0\), and \(P(x,u,y,u)=P(u,x,u,y)=0\). Substituting \(v=x\) in \(P=(y-x)P_1\) gives \((y-x)P_1(x,u,y,x)=0\), and as polynomials form an integral domain (Section 1 of [Interpolation](interpolation.md)), \(P_1(x,u,y,x)=0\), so \(P_1=(v-x)P_2\). In the same way, substituting \(y=u\) gives \(P_2=(y-u)P_3\), and substituting \(v=u\) gives \(P_3=(v-u)R\). Thus
\[
\begin{gathered}
P=C\,R,\\
C=(x-y)(x-v)(u-y)(u-v).
\end{gathered}
\]
The polynomial \(C\) has degree exactly two in each variable and is invariant under both exchanges; as degrees in each variable add under multiplication, \(R\) has degree at most \(s-4\) in each variable and the same two symmetries: \(R\in\mathcal S\). At every pair in \(\mathcal T\) the four numbers \(t_i,t_p,t_k,t_q\) are distinct, so \(C\ne0\) there and \(E(R)=0\).

*Step 3: descent.* If \(E\) had a nonzero kernel, take a nonzero \(P\) in it of least degree in \(x\). Step 2 gives a nonzero \(R\) in the kernel of smaller degree in \(x\), a contradiction. \(\square\)

## 4. The odd lower bound

**Proposition 4.1** (odd \(n\); [OpenAI-C, Proposition 4.3]). Let \(n=2s+1\) with \(s\ge2\). For every normal drawing \(D\) of \(K_n\),
\[
c(D)\ \ge\ \frac{|\mathcal T|}2\ \ge\ \binom s2^{\!2}=Z(n).
\]

*Proof.* Let
\[
\begin{gathered}
\Delta(x,u,y,v)=(x-u)(y-v)\\
\cdot(x-y)(x-v)(u-y)(u-v).
\end{gathered}
\]
For \(P,Q\in\mathcal S\) the polynomial \(PQ\Delta\) has degree at most \(2(s-2)+3=n-2\) in each variable, since each variable occurs in three of the six factors of \(\Delta\). Apply Lemma 1.1 to \(H=PQ\Delta\). The terms with two equal indices among \(i,p,k,q\) vanish, because \(\Delta\) does. The terms with four distinct indices come in groups of four, \((i,p,k,q)\), \((p,i,k,q)\), \((i,p,q,k)\), \((p,i,q,k)\), belonging to the same ordered pair of disjoint edges: exchanging \(i\) and \(p\) changes the signs of \([ip]\) and of the factor \(x-u\) of \(\Delta\), and leaves \(P\), \(Q\), the other factors of \(\Delta\) and the weights unchanged; similarly for \(k\) and \(q\). So the four terms are equal, and with fixed representatives \((i,p,k,q)\),
\[
\begin{gathered}
\sum_{\alpha\in\mathcal T}a_\alpha\,E(P)_\alpha\,E(Q)_\alpha=0,\\
a_\alpha=J([ip],[kq])\,w_iw_pw_kw_q\\
\cdot\Delta(t_i,t_p,t_k,t_q),
\end{gathered}
\]
the ordered pairs of disjoint edges outside \(\mathcal T\) contributing nothing. Every \(a_\alpha\) is nonzero, so \(\langle\xi,\zeta\rangle=\sum_{\alpha\in\mathcal T}a_\alpha\xi_\alpha\zeta_\alpha\) is a nondegenerate symmetric bilinear form on \(\mathbb R^{\mathcal T}\), and the image \(W=E(\mathcal S)\) is *isotropic*: \(\langle w,w'\rangle=0\) for all \(w,w'\in W\).

An isotropic subspace has at most half the dimension of the space. Indeed, let \(w_1,\ldots,w_r\) be a basis of \(W\). The orthogonal space \(W^\perp=\{\xi:\langle\xi,w_j\rangle=0\text{ for all }j\}\) is the kernel of the linear map \(\xi\mapsto(\langle\xi,w_j\rangle)_j\), whose matrix has the rows \((a_\alpha w_j(\alpha))_\alpha\); these rows are linearly independent, being the images of the independent \(w_j\) under the invertible diagonal matrix of the \(a_\alpha\). So \(\dim W^\perp=|\mathcal T|-r\), and \(W\subseteq W^\perp\) gives \(2r\le|\mathcal T|\).

By Lemma 3.1, \(r=\dim\mathcal S\), and with (3.1) and (3.2), \(2\binom s2^2\le|\mathcal T|\le2c(D)\). Finally \(\binom s2^2=Z(2s+1)\) by (2.2) of [Drawings and crossing numbers](drawings-and-crossing-numbers.md). \(\square\)

**Remark 4.2.** As for complete bipartite graphs, the proof bounds the number of pairs of independent edges with a nonzero signed number of crossings, \(|\mathcal T|/2\), in every normal drawing of \(K_{2s+1}\), minimal or not. In a drawing with exactly \(Z(n)\) crossings, such as the two-page drawing of [Two-page drawings and the Harary–Hill formula](two-page-drawings-and-the-harary-hill-formula.md), equality holds throughout: \(|\mathcal T|=2\dim\mathcal S\), and the image of \(E\) is a maximal isotropic subspace.

## 5. All \(n\)

**Theorem 5.1** (the lower bound; [OpenAI-C, Corollary 4.4]). For every \(n\ge3\), \(\operatorname{cr}(K_n)\ge Z(n)\).

*Proof.* For \(n=3,4\), \(Z(n)=0\). For odd \(n\ge5\), apply Proposition 4.1 to a normal drawing attaining \(\operatorname{cr}(K_n)\) (Theorem 1.2 of [Polygonal drawings](polygonal-drawings.md)). Let \(n=2s\ge6\) and let \(D\) be such a normal drawing. Deleting a vertex \(r\) and its edges gives a drawing \(D_r\) of \(K_{n-1}\), with at least \(\operatorname{cr}(K_{n-1})\ge Z(n-1)\) crossings by the odd case. A crossing point lies on two edges with four distinct endpoints (Corollary 4.2 of [Polygonal drawings](polygonal-drawings.md)), so it survives in exactly \(n-4\) of the drawings \(D_r\). Hence \((n-4)c(D)\ge nZ(n-1)\), and by Exercise 7.4 of [Drawings and crossing numbers](drawings-and-crossing-numbers.md), \(nZ(n-1)\) equals \((2s-4)Z(2s)\), so \(c(D)\ge Z(n)\). \(\square\)

## 6. Exercises

**6.1.** For \(n=5\) (\(s=2\)) the space \(\mathcal S\) consists of the constants. Show that Lemma 3.1 says \(\mathcal T\ne\varnothing\), and conclude \(\operatorname{cr}(K_5)\ge1\).

**6.2.** For \(s=2\), check Lemma 2.1(1) directly with nodes \(u=(0,1,2,3)\) and the natural order: \(\mathcal P_{1,0}\) and \(\mathcal P_{0,1}\) are two-dimensional, and the pairing is a \(2\times2\) matrix. Compute its determinant.

**6.3.** Show that \(C=(x-y)(x-v)(u-y)(u-v)\) is invariant under exchanging \(x\) and \(u\) and under exchanging \(y\) and \(v\), while \(\Delta=(x-u)(y-v)C\) changes sign under each exchange.

## 7. Solutions

**6.1.** \(\dim\mathcal S=\binom22^2=1\), spanned by the constant \(1\), and \(E(1)\) is the all-ones vector on \(\mathcal T\); it is nonzero exactly when \(\mathcal T\ne\varnothing\). A pair in \(\mathcal T\) crosses, so every normal drawing of \(K_5\) has a crossing, and by Theorem 1.2 of the polygonal lesson so does every drawing.

**6.2.** \(G'(0)=-6\), \(G'(1)=2\), \(G'(2)=-2\), \(G'(3)=6\). The pattern \(L_2\) is \(\{(2,1),(3,4)\}\) with \(K(2,1)=-1\), \(K(3,4)=1\). With bases \(1,u\) of \(\mathcal P_{1,0}\) and \(1,v\) of \(\mathcal P_{0,1}\): the two coefficients are \(K(2,1)\kappa_{21}=-\frac{1-0}{2\cdot(-6)}=\frac1{12}\) and \(K(3,4)\kappa_{34}=\frac{2-3}{(-2)\cdot6}=\frac1{12}\), so
\[
\begin{gathered}
M(A,B)=\tfrac1{12}\bigl(A(u_2,u_1)B(u_2,u_1)\\
+A(u_3,u_4)B(u_3,u_4)\bigr).
\end{gathered}
\] The evaluation matrices are \(\begin{pmatrix}1&1\\1&2\end{pmatrix}\) (values of \(1,u\) at \(u_2=1,u_3=2\)) and \(\begin{pmatrix}1&0\\1&3\end{pmatrix}\) (values of \(1,v\) at \(u_1=0,u_4=3\)); the pairing matrix is \(\begin{pmatrix}1&1\\1&2\end{pmatrix}^{\mathsf T}\operatorname{diag}(\tfrac1{12},\tfrac1{12})\begin{pmatrix}1&0\\1&3\end{pmatrix}\), with determinant \(1\cdot\frac1{144}\cdot3=\frac1{48}\ne0\).

**6.3.** Exchanging \(x\) and \(u\) maps \((x-y)(x-v)(u-y)(u-v)\) to \((u-y)(u-v)(x-y)(x-v)\), the same product; similarly for \(y\) and \(v\). The factor \(x-u\) changes sign under the first exchange and \(y-v\) under the second.

## References

- [OpenAI-C] OpenAI, *The crossing number of complete graphs*, OpenAI Math Release preprint, 23 September 2026, Sections 3 and 4: Lemma 3.3, Lemma 4.1, Lemma 4.2, Proposition 4.3 and Corollary 4.4. https://github.com/openai/math/tree/main/preprints/The-crossing-number-of-complete-graphs-September-23-2026
