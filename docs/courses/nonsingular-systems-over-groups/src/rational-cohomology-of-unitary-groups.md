# Rational cohomology of unitary groups

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The fixed-space theorem of the next lesson is a statement about unitary matrices proved with cohomology: a class that detects matrices with a large fixed space is pulled back along block-diagonal maps, and its top-degree part is computed from the exponent sums. This lesson collects what is needed. The rational cohomology of the unitary group \(\mathrm U(d)\) is an exterior algebra on generators of degrees \(1,3,\ldots,2d-1\), and the generators can be chosen to restrict correctly to smaller blocks, to add under matrix multiplication and to change sign under inversion. The underlying facts of algebraic topology are stated with free references; the properties of the generators are proved here [OpenAI-NS, Section 2].

- Statements from algebraic topology (Section 1).
- Primitive generators (Section 2).
- Block-diagonal maps (Section 3).
- Incidence manifolds (Section 4).

All cohomology has coefficients in \(\mathbb Q\). For a space \(X\) write \(H^*(X)=H^*(X;\mathbb Q)\), with the cup product written as juxtaposition.

## 1. Statements from algebraic topology

The unitary group \(\mathrm U(d)\) is a compact connected Lie group of real dimension \(d^2\) (Lemma 1.1 of [A unitary with a large fixed space](course:the-kervaire-conjecture/a-unitary-with-a-large-fixed-space)); as a compact connected smooth manifold it is orientable, since translations by group elements carry an orientation of the tangent space at \(I\) to every point. Let \(\iota:\mathrm U(d-1)\to\mathrm U(d)\), \(X\mapsto X\oplus1\), be the standard inclusion and \(\pi:\mathrm U(d)\to S^{2d-1}\), \(W\mapsto We_d\), the last-column map; \(\pi\circ\iota\) is constant.

The following statements are used without proof in the programme; each is a standard result with a free reference.

**(UC) The cohomology of \(\mathrm U(d)\).** There are classes \(x_{a,d}\in H^{2a-1}(\mathrm U(d))\), \(1\le a\le d\), such that the products \(x_{a_1,d}\cdots x_{a_u,d}\) with \(a_1<\cdots<a_u\) form a basis of \(H^*(\mathrm U(d))\) (the empty product being \(1\)), and
\[
\iota^*x_{a,d}=x_{a,d-1}\ (a<d),\qquad x_{d,d}=\pi^*\sigma ,
\]
where \(\sigma\) generates \(H^{2d-1}(S^{2d-1})\). [Hatcher, Corollary 4D.3(a) and its proof: the bundle \(\mathrm U(d-1)\to\mathrm U(d)\to S^{2d-1}\) and the Leray–Hirsch theorem; the proof with integer coefficients gives the statement with rational coefficients.]

**(KU) Künneth formula.** For compact manifolds \(X\), \(Y\), the cross product \(H^*(X)\otimes H^*(Y)\to H^*(X\times Y)\), \(u\otimes v\mapsto\operatorname{pr}_X^*u\,\operatorname{pr}_Y^*v\), is an isomorphism of graded rings, with the sign \((-1)^{|v||u'|}\) in \((u\otimes v)(u'\otimes v')\). [Hatcher, Theorem 3.15 and the remarks after it.]

**(INT) Intersection numbers.** Let \(N\) be a closed connected oriented smooth manifold, \(R\) and \(M\) closed oriented smooth manifolds with \(\dim M+\dim R=\dim N\), and \(p:R\to N\), \(f:M\to N\) smooth. Let \(\alpha\in H^{\dim M}(N)\) be the Poincaré dual of \(p_*[R]\).

1. If the pairs \((x,y)\) with \(f(x)=p(y)\) are finitely many and at each of them \(df(T_xM)+dp(T_yR)=T_{f(x)}N\), then \(\langle f^*\alpha,[M]\rangle\) is a sum of one sign \(\pm1\) for each pair. In particular \(\langle f^*\alpha,[M]\rangle=0\) if \(f(M)\cap p(R)=\varnothing\).
2. For products: if \(N=\prod_jN_j\), \(R=\prod_jR_j\) and \(p=\prod_jp_j\) with \(p_j:R_j\to N_j\), then \(\alpha=\pm\operatorname{pr}_1^*\alpha_1\cdots\operatorname{pr}_n^*\alpha_n\), where \(\alpha_j\) is the Poincaré dual of \((p_j)_*[R_j]\).

[Hatcher, Theorem 3.30, for Poincaré duality; Hutchings, Theorem 1.1 (cup product is Poincaré dual to transverse intersection), applied to the submanifolds \(\{(x,y,f(x))\}\) and \(\{(x,y,p(y))\}\) of \(M\times R\times N\), which meet transversely exactly at the pairs of 1, and to products of graphs for 2.] Poincaré duality itself is proved in the programme ([Poincaré duality, Corollary 2.1](course:poincare-duality-on-manifolds/poincare-duality)); what (INT) assumes is the description of the dual classes by transverse intersections.

Two consequences of (UC) are used repeatedly. First, a product of \(u\) distinct generators has degree at least \(1+3+\cdots+(2u-1)=u^2\), and the top degree \(d^2\) is spanned by \(x_{1,d}x_{2,d}\cdots x_{d,d}\). Second, \(\iota^*\) is an isomorphism \(H^i(\mathrm U(d))\to H^i(\mathrm U(d-1))\) for \(i\le2d-2\): in these degrees the basis monomials do not involve \(x_{d,d}\), of degree \(2d-1\), and \(\iota^*\) maps them bijectively onto the basis monomials of \(H^i(\mathrm U(d-1))\).

## 2. Primitive generators

Let \(\mu:\mathrm U(d)\times\mathrm U(d)\to\mathrm U(d)\) be multiplication and \(\nu(W)=W^{-1}\) inversion. By (KU), a class \(e\in H^n(\mathrm U(d))\) is *primitive* if \(\mu^*e=e\otimes1+1\otimes e\).

**Lemma 2.1** ([OpenAI-NS, Section 2]). The generators of (UC) can be chosen, for all \(d\) at once, so that:

1. \(\mu^*x_{a,d}=x_{a,d}\otimes1+1\otimes x_{a,d}\);
2. \(\nu^*x_{a,d}=-x_{a,d}\);
3. for every coordinate block inclusion \(\iota_{k,d}:\mathrm U(k)\to\mathrm U(d)\), which puts \(X\) on a set of \(k\) coordinates and the identity on the others, \(\iota_{k,d}^*x_{a,d}=x_{a,k}\) for \(a\le k\) and \(=0\) for \(a>k\).

We write \(e_{a,d}\) for these generators.

*Proof.* Choose the generators of (UC) inductively in \(d\), with \(e_{d,d}=\pi^*\sigma\). For \(d=1\), \(\mathrm U(1)\) is the circle, \(H^1\) is spanned by \(e_{1,1}\), and the restrictions of \(\mu\) to \(\mathrm U(1)\times\{1\}\) and \(\{1\}\times\mathrm U(1)\) are the identity, so \(\mu^*e_{1,1}=e_{1,1}\otimes1+1\otimes e_{1,1}\), there being no other terms of degree \(1\).

(1) For \(d\ge2\) and \(a\le d\), put \(\Delta=\mu^*e_{a,d}-e_{a,d}\otimes1-1\otimes e_{a,d}\). Restricting \(\mu\) to \(\mathrm U(d)\times\{I\}\) or \(\{I\}\times\mathrm U(d)\) gives the identity, so in the Künneth decomposition \(\Delta\) has no component in bidegrees \((2a-1,0)\) and \((0,2a-1)\): it lies in the sum of \(H^p\otimes H^q\) with \(p,q\ge1\) and \(p+q=2a-1\), so \(p,q\le2d-2\). On these bidegrees \(\iota^*\otimes\iota^*\) is injective, by the second consequence of (UC). Since \(\mu\circ(\iota\times\iota)=\iota\circ\mu\), the restriction of \(\Delta\) to \(\mathrm U(d-1)\times\mathrm U(d-1)\) is the class \(\Delta\) formed for \(\iota^*e_{a,d}\). For \(a<d\) this is \(e_{a,d-1}\), primitive by induction, and for \(a=d\) it is \(\iota^*\pi^*\sigma=0\). In both cases the restriction of \(\Delta\) vanishes, so \(\Delta=0\).

(2) The map \(W\mapsto(W,W^{-1})\) followed by \(\mu\) is constant, so it pulls \(e_{a,d}\) back to \(0\). By (1), it pulls \(e_{a,d}\) back to \(e_{a,d}+\nu^*e_{a,d}\).

(3) For the standard inclusion of the first \(k\) coordinates, iterate \(\iota^*e_{a,j}=e_{a,j-1}\) for \(a<j\) and \(\iota^*e_{j,j}=0\). Any other coordinate block inclusion is \(\iota_{k,d}\) followed by conjugation by a permutation matrix \(g\). Conjugation \(W\mapsto gWg^{-1}\) is homotopic to the identity, because \(\mathrm U(d)\) is connected (join \(g\) to \(I\) by a path \(g_s\) and use \(W\mapsto g_sWg_s^{-1}\)), so it acts trivially on cohomology. \(\square\)

Primitive classes behave like degree-one classes on a torus: for maps \(\phi,\psi:Z\to\mathrm U(d)\) and their pointwise product \(\phi\psi=\mu\circ(\phi,\psi)\),
\[
\begin{aligned}
(\phi\psi)^*e_{a,d}&=\phi^*e_{a,d}\\
&\quad+\psi^*e_{a,d},
\end{aligned}
\tag{2.1}
\]
by (1) applied to \((\phi,\psi)^*(e\otimes1+1\otimes e)=\phi^*e+\psi^*e\).

## 3. Block-diagonal maps

Let \(k_1,\ldots,k_r\ge1\) and put
\[
\begin{gathered}
D=\prod_{i=1}^r\mathrm U(k_i),\\
e^{(i)}_{a}=\operatorname{pr}_i^*e_{a,k_i}\in H^{2a-1}(D)\\
(a\le k_i).
\end{gathered}
\]
By (KU) and (UC), \(H^*(D)\) is the exterior algebra on the \(\sum_ik_i\) classes \(e^{(i)}_a\), its top degree is \(\sum_ik_i^2=\dim D\), and the top degree is spanned by the product of all generators.

**Lemma 3.1** ([OpenAI-NS, (2.8)]). Let \(\mathcal B\) be a finite ordered list of pairs \((i,s)\), \(1\le i\le r\), \(s=\pm1\), put \(d=\sum_{(i,s)\in\mathcal B}k_i\) and \(b_i=\sum_{(i,s)\in\mathcal B}s\), and let \(P\in\mathrm U(d)\). The map
\[
\begin{gathered}
F:D\to\mathrm U(d),\\
F(X)=\operatorname{diag}_{(i,s)\in\mathcal B}\bigl(X_i^{\,s}\bigr)\,P,
\end{gathered}
\]
with one diagonal block of size \(k_i\) for each entry \((i,s)\) of \(\mathcal B\), satisfies, for \(1\le a\le d\),
\[
F^*e_{a,d}=\sum_{i:\ k_i\ge a}b_i\,e^{(i)}_a .
\]

*Proof.* Right multiplication by \(P\) is homotopic to the identity, since \(\mathrm U(d)\) is connected, so we may take \(P=I\). The block-diagonal matrix is the product of the matrices that equal \(X_i^{\,s}\) on one block and the identity elsewhere, one for each entry of \(\mathcal B\). By (2.1), \(F^*e_{a,d}\) is the sum of the pullbacks along these factors. The factor for \((i,s)\) is \(\operatorname{pr}_i\), followed by \(\nu\) if \(s=-1\), followed by a coordinate block inclusion of \(\mathrm U(k_i)\); by Lemma 2.1(2) and (3) it pulls \(e_{a,d}\) back to \(s\,e^{(i)}_a\) if \(a\le k_i\), and to \(0\) otherwise. \(\square\)

So only the signed numbers of occurrences \(b_i\) matter, not the order or positions of the blocks, nor \(P\).

## 4. Incidence manifolds

For \(0\le l\le d\) let
\[
\begin{gathered}
R(d,l)=\{(W,E):\ W\in\mathrm U(d),\\
E\in\operatorname{Gr}_l(\mathbb C^d),\ W|_E=\mathrm{id}_E\},\\
p(W,E)=W ,
\end{gathered}
\]
where \(\operatorname{Gr}_l(\mathbb C^d)\) is the Grassmannian of \(l\)-dimensional complex subspaces. For \(l\ge1\) this is the incidence manifold of Lemma 2.1 of [A unitary with a large fixed space](course:the-kervaire-conjecture/a-unitary-with-a-large-fixed-space), a compact smooth manifold of dimension \(d^2-l^2\); for \(l=0\) it is \(\mathrm U(d)\), with \(p\) the identity. The image of \(p\) consists of the unitaries with \(\dim\ker(W-I)\ge l\).

**Lemma 4.1.** \(R(d,l)\) is orientable.

*Proof.* The projection \((W,E)\mapsto E\) makes \(R(d,l)\) a smooth fibre bundle over the Grassmannian with fibre \(\mathrm U(d-l)\): over \(E\), the possible \(W\) are the unitaries of \(E^\perp\) extended by the identity on \(E\), and the charts of that lemma, \(\chi(Z,B)\), are local trivializations. Two trivializations over the same subspace differ on the fibre by \(Y\mapsto bYb^{-1}\) for a unitary \(b\) of \(E^\perp\), which depends continuously on the base point; conjugation by an element of the connected group \(\mathrm U(d-l)\) is isotopic to the identity, so it preserves an orientation of the fibre. The Grassmannian is a complex manifold, hence oriented. Orienting each local product by the base orientation followed by the fibre orientation gives orientations that agree on overlaps, so \(R(d,l)\) is orientable. \(\square\)

Fix orientations of all \(R(d,l)\) and \(\mathrm U(d)\), and let
\[
\alpha(d,l)\in H^{l^2}(\mathrm U(d))
\]
be the Poincaré dual of \(p_*[R(d,l)]\); it has degree \(d^2-(d^2-l^2)=l^2\). For \(l=0\), \(\alpha(d,0)=1\). By (INT), if \(f:M\to\mathrm U(d)\) is a smooth map from a closed oriented manifold of dimension \(l^2\) whose image contains no unitary with an \(l\)-dimensional fixed space, then \(\langle f^*\alpha(d,l),[M]\rangle=0\). The next lesson computes the part of \(\alpha(d,l)\) that matters.

## 5. Exercises

**5.1** (easy). Show that \(H^*(\mathrm U(2))\) has dimension \(4\) and that its top class has degree \(4=\dim\mathrm U(2)\).

**5.2** (easy). Let \(F:\mathrm U(k)\to\mathrm U(2k)\), \(F(X)=\operatorname{diag}(X,X^{-1})\). Show that \(F^*\) vanishes in positive degrees.

**5.3** (medium). Let \(F:\mathrm U(1)\times\mathrm U(1)\to\mathrm U(3)\), \(F(X_1,X_2)=\operatorname{diag}(X_1,X_1,X_2^{-1})\). Compute \(F^*e_{1,3}\), \(F^*e_{2,3}\), \(F^*e_{3,3}\).

**5.4** (medium). Show that \(\dim R(d,l)=d^2-l^2\) by counting: \(\dim_{\mathbb R}\operatorname{Gr}_l(\mathbb C^d)=2l(d-l)\) and \(\dim\mathrm U(d-l)=(d-l)^2\).

## 6. Solutions

**5.1.** The basis is \(1\), \(e_{1,2}\), \(e_{2,2}\), \(e_{1,2}e_{2,2}\), of degrees \(0,1,3,4\).

**5.2.** By Lemma 3.1 with \(\mathcal B=((1,1),(1,-1))\), \(b_1=1-1=0\), so \(F^*e_{a,2k}=0\) for all \(a\); every positive-degree class is a sum of products of generators.

**5.3.** Here \(\mathcal B=((1,1),(1,1),(2,-1))\), \(k_1=k_2=1\), \(b_1=2\), \(b_2=-1\). By Lemma 3.1, \(F^*e_{1,3}=2e^{(1)}_1-e^{(2)}_1\), and \(F^*e_{2,3}=F^*e_{3,3}=0\), since no \(k_i\ge2\).

**5.4.**
\[
\begin{aligned}
&2l(d-l)+(d-l)^2\\
&\quad=(d-l)(2l+d-l)\\
&\quad=(d-l)(d+l)=d^2-l^2 .
\end{aligned}
\]

## References

- [OpenAI-NS] OpenAI, *Nonsingular systems of equations over arbitrary groups*, OpenAI Math Release preprint, 5 October 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002; free edition on the author's page, Theorem 3.15, Theorem 3.30 and Corollary 4D.3. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
- [Hutchings] M. Hutchings, *Cup product and intersections*, lecture notes, University of California, Berkeley; on the author's page, Theorem 1.1. https://math.berkeley.edu/~hutching/teach/215b-2011/cup.pdf
