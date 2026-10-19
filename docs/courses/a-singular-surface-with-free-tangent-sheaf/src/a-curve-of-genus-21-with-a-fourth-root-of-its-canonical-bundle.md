# A curve of genus 21 with a fourth root of its canonical bundle

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson constructs a smooth curve \(C\subset\Sigma=\mathbb P^1\times\mathbb P^1\) of bidegree \((8,4)\) through the six points \(q_1,\ldots,q_6\) of the elliptic curve \(\Gamma\) of the preceding lesson, with contact of order exactly four with \(\Gamma\) at each of them. The curve has genus \(21\), and the line bundle \(L=H+Z\), where \(H\) is the restriction of \(\mathcal O(1,0)\) and \(Z=q_1+\cdots+q_6\), satisfies \(4L\cong K_C\) through a normalized isomorphism. Contact of order four makes the subschemes of length at most four at the marked points the same on \(C\) and on \(\Gamma\); this reduces the dimension counts on \(C\) to counts on the curve of genus one. Proposition 3.3 collects the output used in the rest of the course.

**Prerequisites.** [*An elliptic curve on the quadric*](an-elliptic-curve-on-the-quadric.md): its notation, Lemmas 1.1–1.3 and 2.2, the identifications (2.2) and (2.3), Proposition 3.3 and Section 4. From *Commutative algebra for geometry* (AG-CA): [*Krull dimension and Noether normalization*](course:AG-CA/krull-dimension-and-noether-normalization), Theorem 4.2; [*Smooth algebras over a field and the Jacobian criterion*](course:AG-CA/smooth-algebras-over-a-field-and-the-jacobian-criterion), Corollary 2.2. Riemann–Roch and Serre duality on curves as recalled at the start of the preceding lesson. [*Serre's comparison theorems and Chow's theorem*](course:AG-QC/serres-comparison-theorems-and-chows-theorem), Theorem 3.1, for the remark on holomorphic sections.

Notation from the preceding lesson: \(G\) is the equation of \(\Gamma\), of bidegree \((2,2)\); \(F=\mathcal O(1,0)\) and \(\Gamma=\mathcal O(2,2)\) also denote line bundles on \(\Sigma\); on \(\Gamma\) there are the line bundles \(\Delta,\Phi,M\), the divisor \(Z=q_1+\cdots+q_6\) of \(M\) cut out by the section \(\beta\), and the identifications (2.2) induced by \(\zeta\). For a section \(s\) of a line bundle, \(V(s)\) is its zero scheme.

## 1. Fourth-order contact

By (2.3) of the preceding lesson, \(\zeta^{-5}\) identifies \(4M\) with \((2\Gamma+4F)|_\Gamma=\mathcal O(8,4)|_\Gamma\), so \(\beta^4\) is a section of \(\mathcal O(8,4)|_\Gamma\) with divisor \(4Z\).

**Lemma 1.1 (lifts).** Restriction \(H^0(\Sigma,\mathcal O(8,4))\to H^0(\Gamma,\mathcal O(8,4)|_\Gamma)\) is surjective. If \(K_0\) restricts to \(\beta^4\), the sections restricting to \(\beta^4\) are exactly
\[
\begin{gathered}
K_s=K_0+G\,s,\\
s\in V=H^0(\Sigma,\mathcal O(6,2)),\quad \dim V=21 .
\end{gathered}
\]

**Proof.** Multiplication by \(G\) gives the exact sequence \(0\to\mathcal O(6,2)\to\mathcal O(8,4)\to\mathcal O(8,4)|_\Gamma\to0\), and \(H^1(\Sigma,\mathcal O(6,2))=0\) by Lemma 1.1 of the preceding lesson. The kernel of restriction is \(G\cdot V\), and \(\dim V=7\cdot3\). \(\square\)

Each \(K_s\) is nonzero on \(\Gamma\setminus Z\), so \(V(K_s)\cap\Gamma=\{q_1,\ldots,q_6\}\) as sets. By the Jacobian criterion (Corollary 2.2 of the lesson on smooth algebras), the curve \(V(K_s)\) is smooth at a point \(p\) exactly when the differential of a local equation of \(V(K_s)\) is nonzero at \(p\), that is, when the class of \(K_s\) in \(\mathfrak m_p/\mathfrak m_p^2\) is nonzero after trivializing \(\mathcal O(8,4)\) near \(p\).

**Lemma 1.2 (the marked points).** For each \(j\) there is a proper affine hyperplane \(H_j\subset V\) such that \(V(K_s)\) is smooth at \(q_j\) for \(s\notin H_j\).

**Proof.** Work in the local ring \(\mathcal O=\mathcal O_{\Sigma,q_j}\), with all line bundles trivialized near \(q_j\), and write \(\mathfrak m\) for its maximal ideal. The class \([G]\) of \(G\) in \(\mathfrak m/\mathfrak m^2\) is nonzero, since \(\Gamma\) is smooth. The restriction of \(K_0\) to \(\Gamma\) is \(\beta^4\), which lies in \(\mathfrak m_\Gamma^4\); hence \(K_0=h_0G+m_4\) with \(h_0\in\mathcal O\) and \(m_4\in\mathfrak m^4\), so \([K_0]=h_0(q_j)[G]\). Then \([K_s]=(h_0(q_j)+s(q_j))[G]\), which is nonzero unless \(s(q_j)=-h_0(q_j)\). The linear functional \(s\mapsto s(q_j)\) on \(V\) is nonzero, because \(\mathcal O(6,2)\) has a section not vanishing at \(q_j\) (a product of powers of linear forms not vanishing there). So \(H_j=\{s:\ s(q_j)=-h_0(q_j)\}\) is a proper affine hyperplane. \(\square\)

**Lemma 1.3 (away from \(\Gamma\)).** There is a proper Zariski-closed subset \(Y\subsetneq V\) such that for \(s\notin Y\), the curve \(V(K_s)\) is smooth at every point outside \(\Gamma\).

**Proof.** Consider the chart \(X_0Y_0\ne0\) with coordinates \((x,y)\), and lower-case letters for dehomogenizations; there \(\Sigma\setminus\Gamma\) is the principal open set \(D(g)\) of the plane, an irreducible affine variety of dimension two. On \(D(g)\), \(k_s=g\,(f+s)\) with the regular function \(f=k_0/g\). At a zero of \(f+s\), \(dk_s=g\,d(f+s)\). So \(V(K_s)\) is singular at \(p\in D(g)\) exactly when
\[
\begin{aligned}
(f+s)(p)&=\partial_x(f+s)(p)\\
&=\partial_y(f+s)(p)=0 .
\end{aligned}
\]
Let \(B\subset D(g)\times V\) be the set of pairs \((p,s)\) satisfying these equations. Expand \(s=c_0+c_1x+c_2y+\sum_{i\ge3}c_im_i\), where \(m_3,\ldots,m_{20}\) are the remaining monomials \(x^ay^b\), \(a\le6\), \(b\le2\). For \(p=(a,b)\) the three equations read
\[
\begin{gathered}
c_1=-f_x(p)-\sum_{i\ge3}c_i\,\partial_xm_i(p),\\
c_2=-f_y(p)-\sum_{i\ge3}c_i\,\partial_ym_i(p),
\end{gathered}
\]
\[
c_0=-f(p)-c_1a-c_2b-\sum_{i\ge3}c_im_i(p).
\]
They express \(c_0,c_1,c_2\) as regular functions of \(p\in D(g)\) and \(c_3,\ldots,c_{20}\), so \((p,c_3,\ldots,c_{20})\mapsto(p,s)\) is an isomorphism of \(D(g)\times\mathbb A^{18}\) onto \(B\). Hence \(B\) is an irreducible affine variety of dimension \(20\) (Theorem 4.2 of the lesson on Krull dimension: dimension equals transcendence degree). Let \(Y_0\) be the closure of the projection of \(B\) to \(V\). It is irreducible, and the projection \(B\to Y_0\) is dominant, so it induces an injection of function fields \(\mathbb C(Y_0)\hookrightarrow\mathbb C(B)\); thus \(\dim Y_0\le20<21\), and \(Y_0\ne V\). The three other charts, with the coordinates \((x',y)\), \((x,y')\), \((x',y')\) where \(x'=1/x\) and \(y'=1/y\), give \(Y_1,Y_2,Y_3\) in the same way, because in each chart the monomials \(1\), \(x\) or \(x'\), and \(y\) or \(y'\) are dehomogenizations of sections in \(V\). Put \(Y=Y_0\cup Y_1\cup Y_2\cup Y_3\), a proper closed subset of the irreducible variety \(V\cong\mathbb A^{21}\). \(\square\)

**Proposition 1.4.** Choose \(s\in V\) outside \(Y\cup H_1\cup\cdots\cup H_6\), possible because \(V\) is irreducible, and put \(K=K_s\), \(C=V(K)\). Then:

1. \(C\) is a smooth connected curve of bidegree \((8,4)\) and genus \(21\), and \(C\cap\Gamma=\{q_1,\ldots,q_6\}\).
2. At each \(q_j\), choose \(z\in\mathfrak m=\mathfrak m_{\Sigma,q_j}\) restricting to a uniformizer of \(\Gamma\) at \(q_j\). Then \(z\) restricts to a uniformizer of \(C\) at \(q_j\), and
\[
\begin{gathered}
(K,z^\ell)=(G,z^\ell)\quad\text{in }\mathcal O_{\Sigma,q_j}\\
(1\le\ell\le4),
\end{gathered}
\]
while \((K,z^5)\ne(G,z^5)\). In particular \(\operatorname{div}_C(G|_C)=4Z\).

**Proof.** (1) By Lemmas 1.2 and 1.3, \(C\) is smooth at every point; by Lemma 1.2 of the preceding lesson it is connected and irreducible of genus \((8-1)(4-1)=21\). The intersection with \(\Gamma\) was computed before Lemma 1.2.

(2) In \(\mathcal O=\mathcal O_{\Sigma,q_j}\) the elements \(G,z\) form a regular system of parameters, and \(\mathcal O/(G)=\mathcal O_{\Gamma,q_j}\) is a discrete valuation ring with uniformizer \(z\). The restriction of \(K\) to \(\Gamma\) is \(\beta^4\), and \(\beta\) has a simple zero at \(q_j\), so \(K\equiv uz^4\pmod G\) for a unit \(u\): \(K=uz^4+hG\) with \(h\in\mathcal O\). Since \(C\) is smooth at \(q_j\), \(K\notin\mathfrak m^2\), which forces \(h(q_j)\ne0\). So \(h\) is a unit and \((K)=(G+vz^4)\) with \(v=u/h\) a unit. Then \((K,z)=(G,z)=\mathfrak m\), so \(z\) is a uniformizer of \(\mathcal O_{C,q_j}=\mathcal O/(K)\); and \((K,z^\ell)=(G+vz^4,z^\ell)=(G,z^\ell)\) for \(\ell\le4\). If \((K,z^5)=(G,z^5)\), then \(vz^4\in(G,z^5)\), so \(z^4\in(z^5)\) in the discrete valuation ring \(\mathcal O/(G)\), which is false. Finally
\[
\begin{aligned}
\mathcal O_{C,q_j}/(G)&=\mathcal O/(K,G)\\
&=\mathcal O/(G,uz^4)=\mathcal O_{\Gamma,q_j}/(z^4)
\end{aligned}
\]
has length four, so \(G|_C\) vanishes to order four at \(q_j\). It has no other zeros on \(C\), by (1). \(\square\)

In analytic local coordinates \((y,z)\) at \(q_j\) with \(\Gamma=\{y=0\}\), and frames in which \(K\) and \(\beta\) have coefficients \(k(y,z)\) and \(b(z)\) with \(k(0,z)=b(z)^4\), the curve \(C\) is the graph \(y=\varphi(z)\) with \(\varphi(z)=-b'(0)^4z^4/k_y(0,0)+O(z^5)\); this is the same statement in coordinates.

## 2. The line bundles on \(C\)

Put
\[
\begin{gathered}
H=F|_C=\mathcal O(1,0)|_C,\\
L=H+Z,\qquad \theta=2L,
\end{gathered}
\tag{2.1}
\]
where \(Z=q_1+\cdots+q_6\) is regarded as a divisor on \(C\), and let \(\xi\) be the canonical section of \(\mathcal O_C(Z)\), with divisor \(Z\). By Lemma 1.2(2) of the preceding lesson, \(\deg H=1\cdot4+0\cdot8=4\), so \(\deg L=10\), and \(\deg K_C=6\cdot4+2\cdot8=40=2\cdot21-2\).

The sections \(\xi^4\) of \(4\mathcal O_C(Z)\) and \(G|_C\) of \(\Gamma|_C=\mathcal O(2,2)|_C\) have the same divisor \(4Z\) (Proposition 1.4), so
\[
4\mathcal O_C(Z)\xrightarrow{\ \sim\ }\Gamma|_C,\qquad \xi^4\mapsto G|_C .
\]
By Lemma 1.3 of the preceding lesson with \((c,d)=(8,4)\), the residue gives an isomorphism \(\mathcal O(6,2)|_C=(\Gamma+4F)|_C\to K_C\). Together,
\[
\begin{aligned}
4L&=4H+4Z\\
&\cong(4F+\Gamma)|_C\cong K_C,
\end{aligned}
\tag{2.2}
\]
and we fix this isomorphism: for a local section \(\sigma\) of \(\Gamma+4F=\mathcal O(6,2)\),
\[
\begin{aligned}
\sigma|_C&\longmapsto\operatorname{Res}_C\Bigl(\frac{\sigma\,\varepsilon}{K}\Bigr)\\
&=\operatorname{Res}_C\Bigl(\frac{\sigma\,G\,\Omega}{K}\Bigr),
\end{aligned}
\tag{2.3}
\]
with the normal differential first; here \(\Omega=\varepsilon/G\) is the logarithmic form of the preceding lesson. In the chart \(X_0Y_0\ne0\) this is \(\sigma\mapsto-\sigma\,dx/k_y=\sigma\,dy/k_x\) by (1.2) there. The normalization (2.3) fixes the scalar in (2.2), which matters in the residue computations of later lessons.

The section spaces below are algebraic. By Serre's comparison theorem (Theorem 3.1 of the lesson on Serre's comparison theorems), they coincide with the spaces of holomorphic sections of the associated holomorphic line bundles, and the same holds for all cohomology groups of coherent sheaves on \(C\), \(\Gamma\) and \(\Sigma\). The analytic constructions of later lessons use this.

## 3. Section counts and evaluation maps

**Lemma 3.1 (dimension formula).** For a line bundle \(B\) and an effective divisor \(D\) on a curve \(X\),
\[
\begin{aligned}
&h^0(B+D)-h^0(B)=\deg D\\
&\quad-\operatorname{rank}\Bigl(H^0(X,K_X-B)\\
&\qquad\longrightarrow H^0\bigl(D,(K_X-B)|_D\bigr)\Bigr),
\end{aligned}
\]
where \(D\) is regarded as a finite subscheme and the map is restriction.

**Proof.** Riemann–Roch for \(B\) and for \(B+D\) gives
\[
\begin{aligned}
&h^0(B+D)-h^0(B)=\deg D\\
&\quad+h^0(K_X-B-D)-h^0(K_X-B).
\end{aligned}
\]
A section of \(K_X-B\) restricts to zero on \(D\) exactly when it is a section of \(K_X-B-D\). So \(h^0(K_X-B)-h^0(K_X-B-D)\) is the rank of the restriction. \(\square\)

For a point \(q_j\) and \(\ell\ge1\), write \(\ell q_j\) for the subscheme of length \(\ell\) of \(C\), or of \(\Gamma\), supported at \(q_j\), and \(\ell Z=\sum_j\ell q_j\). By Proposition 1.4(2), for \(\ell\le4\) the subschemes \(\ell q_j\) of \(C\) and of \(\Gamma\) are the same subscheme of \(\Sigma\), with ideal \((G,z^\ell)=(K,z^\ell)\).

**Lemma 3.2 (adjoint jets).** For \(0\le j\le3\) put
\[
\begin{gathered}
\mathcal A_j=\Gamma+(4-j)F=\mathcal O(6-j,2),\\
N_j=\mathcal A_j|_\Gamma=(8-j)F+\Delta .
\end{gathered}
\]
Restriction is an isomorphism \(H^0(\Sigma,\mathcal A_j)\cong H^0(C,K_C-jH)\), where \(\mathcal A_j|_C\cong K_C-jH\) by the adjunction isomorphism (2.3), and it maps \(H^0(\Sigma,\mathcal A_j)\) onto \(H^0(\Gamma,N_j)\). For \(1\le\ell\le4\), restriction to the subscheme \(\ell Z\) has the same rank on \(H^0(C,K_C-jH)\) as on \(H^0(\Gamma,N_j)\). The ranks needed are, with all \(h^0\) taken on \(\Gamma\):
\[
\begin{array}{c|cccc}
j&0&1&2&3\\\hline
\ell&1&2&2&2\\
h^0(N_j)&16&14&12&10\\
N_j-\ell Z&5F&\Phi&\Delta&-F+\Delta\\
h^0(N_j-\ell Z)&10&2&0&0\\
\text{rank}&6&12&12&10
\end{array}
\]

**Proof.** The kernels of restriction to \(C\) and to \(\Gamma\) are
\[
\begin{gathered}
\mathcal A_j-C=\mathcal O(-2-j,-2),\\
\mathcal A_j-\Gamma=\mathcal O(4-j,0).
\end{gathered}
\]
By Lemma 1.1 of the preceding lesson, the first has \(H^0=H^1=0\) and the second has \(H^1=0\), which gives the two assertions about restriction. For \(\ell\le4\), restriction from \(\Sigma\) to the common subscheme \(\ell Z\) factors through \(H^0(C,\mathcal A_j|_C)\) and through \(H^0(\Gamma,N_j)\). Restriction from \(\Sigma\) maps onto both of these spaces, so the restrictions from \(C\) and from \(\Gamma\) to \(\ell Z\) have the same image as the restriction from \(\Sigma\).

On \(\Gamma\), \(\deg F=2\), \(Z\) is a divisor of \(M\cong3F+\Delta\), \(2\Delta\cong\mathcal O_\Gamma\), and \(2Z\sim6F\) by (2.3) of the preceding lesson. Hence the residual bundles \(N_j-\ell Z\) are \(8F+\Delta-(3F+\Delta)=5F\), \(7F+\Delta-6F\cong F+\Delta=\Phi\), \(6F+\Delta-6F=\Delta\) and \(5F+\Delta-6F=-F+\Delta\). By Lemma 2.2 of the preceding lesson, a line bundle of positive degree on \(\Gamma\) has as many sections as its degree, the nontrivial degree-zero bundle \(\Delta\) has none, and a bundle of negative degree has none. The kernel of restriction to \(\ell Z\) on \(H^0(\Gamma,N_j)\) is \(H^0(\Gamma,N_j-\ell Z)\), and subtracting gives the ranks. \(\square\)

For \(j=3\), the twelve-dimensional space \(H^0(\Sigma,\mathcal O(3,2))\) has a two-dimensional kernel on restriction to \(\Gamma\), and the resulting ten-dimensional space injects into the twelve-dimensional space of sections on \(2Z\).

**Proposition 3.3 (the curve data).** The curve \(C\), the divisor \(Z=q_1+\cdots+q_6\), the line bundles \(H,L,\theta\), and a basis \(u=(u_1,u_2)\) of \(H^0(C,H)\) chosen below have the following properties.

1. \(g(C)=21\), \(\deg H=4\), \(\deg L=10\), \(L=H+Z\), \(\theta=2L\), and \(K_C\cong4L\) through (2.2) and (2.3). The curve \(C\) has contact of order exactly four with \(\Gamma\) at every \(q_j\) (Proposition 1.4).
2. The pencil \(u\) defines a finite morphism \(f:C\to\mathbb P^1\) of degree four, unramified at every \(q_j\), and the values \(f(q_j)\) are not all equal. The zero divisor of \(u_1\) is a reduced fibre of \(f\) disjoint from \(Z\).
3. The section dimensions are
\[
\begin{gathered}
h^0(C,jH)=j+1\ (0\le j\le3),\\
h^0(C,L)=h^0(C,H+2Z)=2,\\
h^0(C,\theta)=3,\quad h^0(C,\mathcal O_C(Z))=1,\\
h^0(C,\theta+H)=6,
\end{gathered}
\]
and more precisely
\[
\begin{gathered}
H^0(C,L)=\xi\,H^0(C,H),\\
H^0(C,H+2Z)=\xi^2H^0(C,H),\\
H^0(C,\theta)=\xi^2H^0(C,2H).\quad(3.1)
\end{gathered}
\]
In particular \(r=\xi u\) is a basis of \(H^0(C,L)\) whose common zero divisor is exactly \(Z\), with simple zeros, and every section of \(\theta\) vanishes to order at least two at each \(q_j\).
4. For every \(k\ge2\), restriction
\[
\begin{aligned}
&H^0\bigl(C,(k+1)L\bigr)\\
&\quad\longrightarrow H^0\bigl(Z,(k+1)L|_Z\bigr)\qquad(3.2)
\end{aligned}
\]
is surjective.
5. On \(\Gamma\) there are the data of the preceding lesson: the identifications (2.2) and (2.3) there, the logarithmic form \(\Omega\), the quadratic form \(Q\) on \(H^0(\Gamma,\Phi)^*\), the divisor \(Z\) of \(M\), and nonzero vectors \(w_j\in H^0(\Gamma,\Phi)^*\) with \([w_j]=[\mathrm{ev}_{q_j}]\), using three distinct directions, satisfying \(w^2=90=9\deg L\) and \(w_j^2+w_j\cdot w=1\).

**Proof.** (1) The degrees were computed in Section 2.

(2) The projection \(\mathrm{pr}_1\) restricted to the irreducible curve \(C\) is nonconstant, hence finite, and \(H\) is the pullback of \(\mathcal O(1)\), of degree four; so \(f=\mathrm{pr}_1|_C\) has degree four for every basis \(u\) of \(H^0(\Sigma,\mathcal O(1,0))\). Restriction \(H^0(\Sigma,\mathcal O(1,0))\to H^0(C,H)\) is an isomorphism by (3) below, so \(u\) may be taken there. At \(q_j\) the curves \(C\) and \(\Gamma\) are tangent, since their subschemes of length two coincide (Proposition 1.4); the differential of \(\mathrm{pr}_1\) on their common tangent line is nonzero because \(q_j\) is not a ramification point of \(\mathrm{pr}_1|_\Gamma\) (Section 4 of the preceding lesson). So \(f\) is unramified at \(q_j\), and \(f(q_j)\) is the first coordinate of \(q_j\); these are not all equal. Choose a point \(x_\infty\in\mathbb P^1\) that is neither a branch value of \(f\) nor one of the \(f(q_j)\). Let \(u_1\in H^0(\Sigma,\mathcal O(1,0))\) be a nonzero linear form vanishing at \(x_\infty\), and choose \(u_2\) so that \((u_1,u_2)\) is obtained from \((X_0,X_1)\) by a matrix of determinant one, which is possible after scaling \(u_2\). The zero divisor of \(u_1\) is the fibre of \(f\) over \(x_\infty\), reduced and disjoint from \(Z\). A change of basis of determinant one preserves the section \(\eta_\Gamma=u_1\,du_2-u_2\,du_1\) of the preceding lesson, so the quadratic form \(Q\) and all normalizations made there are unchanged.

(3) For \(0\le j\le3\), restriction of \(\mathcal O(j,0)\) to \(C\) has kernel \(\mathcal O(j-8,-4)\), with \(H^0=H^1=0\) by Lemma 1.1 of the preceding lesson. So \(h^0(C,jH)=h^0(\Sigma,\mathcal O(j,0))=j+1\). Apply Lemma 3.1 with \(B=jH\) and \(D=\ell Z\), using \(K_C-jH\) and the ranks of Lemma 3.2:
\[
\begin{gathered}
h^0(\mathcal O_C(Z))=1+6-6=1,\\
h^0(H+2Z)=2+12-12=2,\\
h^0(2H+2Z)=3+12-12=3,
\end{gathered}
\]
\[
h^0(3H+2Z)=4+12-10=6 .
\]
Since \(H^0(C,H)\subset H^0(C,H+Z)\) and \(H^0(C,H+Z)\subset H^0(C,H+2Z)\) by multiplication with \(\xi\), and the outer spaces have dimension two, \(h^0(C,L)=2\). Here \(\theta=2H+2Z\) and \(\theta+H=3H+2Z\). Multiplication by \(\xi\) or \(\xi^2\) is injective, and the dimensions of source and target agree in each case of (3.1), which proves (3.1). The sections \(u_1,u_2\) have no common zero, because \(H\) is pulled back from \(\mathcal O(1)\) on \(\mathbb P^1\); so the common zeros of \(\xi u_1,\xi u_2\) are the zeros of \(\xi\), the reduced divisor \(Z\).

(4) Let \(N=(k+1)L\). Restriction \(H^0(C,N)\to H^0(Z,N|_Z)\) has kernel \(H^0(C,N-Z)\), so its rank is \(h^0(N)-h^0(N-Z)\). Riemann–Roch gives
\[
\begin{gathered}
h^0(N)-h^0(N-Z)\\
=6+h^0(K_C-N)-h^0(K_C-N+Z),\\
K_C-N=(3-k)L .
\end{gathered}
\]
So (3.2) is surjective, of rank six, exactly when the inclusion of \(H^0(C,(3-k)L)\) in \(H^0(C,(3-k)L+Z)\) is an equality. For \(k=2\) this is \(H^0(L)\subset H^0(L+Z)=H^0(H+2Z)\), both of dimension two. For \(k=3\) it is \(H^0(\mathcal O_C)\subset H^0(\mathcal O_C(Z))\), both of dimension one. For \(k\ge4\), the degree of \((3-k)L+Z\) is \(10(3-k)+6\le-4\), and both spaces vanish.

(5) This is Section 4 of the preceding lesson, with \(\deg L=10\). \(\square\)

**Corollary 3.4.** (1) \(h^1(C,L)=h^0(C,3L)=12\) and \(h^0(C,4L)=21\).

(2) At \(q_j\), take frames of \(H\) and \(\mathcal O_C(Z)\) and a local parameter \(z\) at \(q_j\) in which \(\xi\) is represented by \(z\). Then the row of coefficients of \(r=\xi u\) is \(z\,u(z)\), and its derivative at \(q_j\) is the row \(r'(q_j)=u(q_j)\in\mathbb C^2\). These six rows are nonzero and span \(\mathbb C^2\). Changing the frames or the parameter multiplies each row by a nonzero scalar.

**Proof.** (1) Riemann–Roch gives \(h^0(L)-h^1(L)=10+1-21=-10\), so \(h^1(L)=12\), and \(h^1(L)=h^0(K_C-L)=h^0(3L)\). Also \(h^0(4L)=h^0(K_C)=g(C)=21\). (2) \(u(q_j)\ne0\) since \(u\) has no base point, and the projective direction of \(u(q_j)\) is \(f(q_j)\); these are not all equal, so the rows span \(\mathbb C^2\). A change of frames multiplies \(z\,u(z)\) by a unit, and a change of parameter replaces \(z\) by a unit multiple; at \(z=0\) the derivative of a unit times \(z\,u(z)\) is that unit's value times \(u(0)\). \(\square\)

## 4. Exercises

**4.1** (easy). Show that \(h^0(C,jH)=j+1\) for \(0\le j\le7\), and \(h^0(C,8H)=12\).

**4.2** (easy). Show that multiplication \(\operatorname{Sym}^2H^0(C,L)\to H^0(C,\theta)\) is an isomorphism.

**4.3** (medium). Show that for \(k=1\) the restriction (3.2), \(H^0(C,2L)\to H^0(Z,2L|_Z)\), is the zero map.

**4.4** (medium). Show that \(\theta\) is a theta characteristic, \(2\theta\cong K_C\), with \(h^0(C,\theta)=h^1(C,\theta)=3\).

**4.5** (medium). Using Lemma 3.1 and the ranks of Lemma 3.2 for \(j=0\), show that the six points \(q_1,\ldots,q_6\) impose independent conditions on \(H^0(C,K_C)\), and compute \(h^0(C,K_C-Z)\).

## 5. Solutions

**4.1.** The kernel of restriction of \(\mathcal O(j,0)\) to \(C\) is \(\mathcal O(j-8,-4)\). For \(j\le7\) its \(H^0\) and \(H^1\) vanish by Lemma 1.1 of the preceding lesson, since both entries are negative, so \(h^0(C,jH)=j+1\). For \(j=8\) the kernel is \(\mathcal O(0,-4)\), with \(H^0=0\) and \(h^1=1\cdot3=3\), while \(H^1(\Sigma,\mathcal O(8,0))=0\); the cohomology sequence gives \(h^0(C,8H)=9+3=12\). As a check, Riemann–Roch gives that \(h^0(8H)-h^0(K_C-8H)\) is \(32-20=12\), and \(K_C-8H\cong\mathcal O(-2,2)|_C\) has no sections, since \(H^0(\Sigma,\mathcal O(-2,2))=0\) and \(H^1(\Sigma,\mathcal O(-10,-2))=0\).

**4.2.** By (3.1), \(H^0(C,L)=\xi H^0(C,H)\) and \(H^0(C,\theta)=\xi^2H^0(C,2H)\). Multiplication \(\operatorname{Sym}^2H^0(C,H)\to H^0(C,2H)\) is the restriction from \(\Sigma\) of the isomorphism \(\operatorname{Sym}^2H^0(\mathbb P^1,\mathcal O(1))\to H^0(\mathbb P^1,\mathcal O(2))\), followed by the isomorphism \(H^0(\Sigma,\mathcal O(2,0))\to H^0(C,2H)\) of 4.1. Multiplying by \(\xi^2\) gives the claim.

**4.3.** By (3.1) every section of \(2L=\theta\) is \(\xi^2\) times a section of \(2H\), so it vanishes at every \(q_j\), and its restriction to the reduced subscheme \(Z\) is zero.

**4.4.** \(2\theta=4L\cong K_C\). Serre duality gives \(h^1(\theta)=h^0(K_C-\theta)=h^0(\theta)=3\), consistent with Riemann–Roch: \(h^0(\theta)-h^1(\theta)=20+1-21=0\).

**4.5.** By Lemma 3.2 with \(j=0\), \(\ell=1\), restriction \(H^0(C,K_C)\to H^0(Z,K_C|_Z)\cong\mathbb C^6\) has rank six, so the six points impose independent conditions and \(h^0(C,K_C-Z)=21-6=15\). Equivalently, Lemma 3.1 with \(B=\mathcal O_C\), \(D=Z\) gives \(h^0(\mathcal O_C(Z))=1\): no nonconstant rational function on \(C\) has poles only at \(Z\), each simple.

## Sources

- [OpenAI-048] OpenAI, *A singular normal affine surface with free tangent sheaf* (manuscript, 23 September 2026), in the release github.com/openai/math, family 048. Section 2: fourth-order contact on the quadric, the adjoint-jet ranks and the curve data. The smoothness of the general lift is proved there by Bertini's theorem; Lemmas 1.2 and 1.3 give a direct dimension count for this linear system.
