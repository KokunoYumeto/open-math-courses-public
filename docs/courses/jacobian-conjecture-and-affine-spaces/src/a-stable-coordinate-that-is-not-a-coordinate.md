# A stable coordinate that is not a coordinate

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A polynomial \(f\in k[x_1,\ldots,x_n]\) is a **one-stable coordinate** if it becomes a coordinate after adjoining one variable: it is a coordinate of \(k[x_1,\ldots,x_n,w]\). The stable coordinate conjecture asked whether every such polynomial is already a coordinate of \(k[x_1,\ldots,x_n]\). This lesson proves that the answer is no in four variables, for the explicit polynomial

\[
f=x_1-2Q\bigl(Q(x_2+x_4)+x_1x_4\bigr),\qquad Q=x_2^2-x_4^2+x_1x_3,
\]

of degree five. Every fibre \(f=\lambda\) of this polynomial is isomorphic to affine three-space, and still none of these hypersurfaces can be moved onto a coordinate hyperplane by an automorphism of \(\mathbb A^4\). The proof follows the pattern of [Cancellation fails in dimension four](cancellation-fails-in-dimension-four.md), with one simplification at the end.

We use [Coordinates and the Abhyankar–Sathaye problem](coordinates-and-the-abhyankar-sathaye-problem.md), [Locally nilpotent derivations](locally-nilpotent-derivations.md), [Additive actions on line bundles](additive-actions-on-line-bundles.md) and the line bundle of Section 4 of [Cancellation fails in dimension four](cancellation-fails-in-dimension-four.md). The field \(k\) has characteristic zero.

Basic references are [OpenAI-stable] and [Shpilrain–Yu].

## 1. Stable coordinates

Coordinates were defined in [Coordinates and the Abhyankar–Sathaye problem](coordinates-and-the-abhyankar-sathaye-problem.md). If \(f\) is a coordinate of \(k[x_1,\ldots,x_n]\), it is a coordinate of \(k[x_1,\ldots,x_n,w]\), with \(w\) added to its complement. The **stable coordinate conjecture** [Shpilrain–Yu, Conjecture 3] asserts the converse. Over the complex numbers it holds in at most three variables [Shpilrain–Yu, Proposition 1.1]: in two variables by cancellation for curves and the theorem of Abhyankar and Moh, and in three variables by cancellation for affine surfaces together with Kaliman's theorem that a polynomial on \(\mathbb C^3\) whose general fibre is \(\mathbb C^2\) is a coordinate. The counterexample of this lesson was found in 2026 [OpenAI-stable]. A counterexample in five variables, the polynomial \(H\) of the cancellation lessons, is proved in [A stable coordinate in five variables](a-stable-coordinate-in-five-variables.md); the present example has four variables.

## 2. A presentation by a hypersurface

Let \(P=k[p,s,u,F,J]\) and put

\[
x=s^2-u^2+pF,\qquad H=x^2F-(1+2sx)J-pJ^2-u,\qquad A=P/(H).
\tag{2.1}
\]

**Proposition 2.1.** There are polynomial coordinates \(p',s',F',J\) of \(A\), so \(A\cong k^{[4]}\), in which

\[
x=s'^2-J^2+p'F',\qquad p=p'-2x\bigl(x(s'+J)+p'J\bigr).
\]

Under the identification \((p',s',F',J)=(x_1,x_2,x_3,x_4)\), the element \(p\in A\) becomes the polynomial \(f\).

**Proof.** Consider

\[
M=\begin{pmatrix}F&s-u\\ s+u&-p\end{pmatrix},\qquad e=\begin{pmatrix}x\\-J\end{pmatrix},\qquad n=\begin{pmatrix}J\\x\end{pmatrix}.
\]

Then \(x=-\det M\), \(e^{\mathsf T}n=0\), and expanding gives \(H=e^{\mathsf T}Me-J-u\). Define \(F',s',u',p'\), keeping \(J\), by

\[
M'=(I_2-2ne^{\mathsf T})M=\begin{pmatrix}F'&s'-u'\\ s'+u'&-p'\end{pmatrix}.
\]

Since \((ne^{\mathsf T})^2=n(e^{\mathsf T}n)e^{\mathsf T}=0\), the matrix \(I_2-2ne^{\mathsf T}\) has determinant one and inverse \(I_2+2ne^{\mathsf T}\). So \(\det M'=\det M=-x\): the element \(x\), hence also \(e\) and \(n\), is the same polynomial when written through \(M'\) and \(J\). The substitution is therefore invertible, with inverse \(M=(I_2+2ne^{\mathsf T})M'\), and \(p',s',u',F',J\) are coordinates of \(P\). Half the difference of the off-diagonal entries of \(M'\) is \(u'=u-e^{\mathsf T}Me\), so \(H=-J-u'\). Eliminating \(u'=-J\) gives \(A=k[p',s',F',J]\). In this quotient, \(x=-\det M'=s'^2-u'^2+p'F'=s'^2-J^2+p'F'\), and the lower right entry of \(M=(I_2+2ne^{\mathsf T})M'\) gives \(p=p'-2x\bigl(x(s'-u')+p'J\bigr)=p'-2x\bigl(x(s'+J)+p'J\bigr)\). \(\square\)

The polynomial \(f\) takes the values \(0\) and \(1\) at \((0,0,0,0)\) and \((1,0,0,0)\), so \(p\) is a nonzero nonunit of \(A\).

## 3. The polynomial becomes a coordinate after one more variable

Put

\[
y=s+x(x+u^2),\qquad z=sx+pJ .
\]

Expanding, as in Lemma 2.1 of [A fourfold whose cylinder is affine space](a-fourfold-whose-cylinder-is-affine-space.md),

\[
xy-z(z+1)=p\,(H+u).
\tag{3.1}
\]

Over \(k[p,p^{-1}]\), the elements \(x,y,z,u\) are coordinates of \(P[p^{-1}]\), with inverse formulas \(s=y-x(x+u^2)\), \(F=p^{-1}(x-s^2+u^2)\), \(J=p^{-1}(z-sx)\). Let \(\Delta=-p\,\partial/\partial u\) on \(P[p^{-1}]=k[p^{\pm1}][x,y,z,u]\). Differentiating the inverse formulas gives

\[
\Delta(p)=0,\quad\Delta(u)=-p,\quad\Delta(s)=2pxu,\quad\Delta(F)=-4sxu-2u,\quad\Delta(J)=-2x^2u,
\tag{3.2}
\]

so \(\Delta\) is a locally nilpotent derivation of \(P\). By (3.1), \(H=p^{-1}(xy-z(z+1))-u\), so \(\Delta(H)=p\) and \(\Delta^2(H)=0\).

**Proposition 3.1.** \(A[w]\) is a polynomial ring in five variables in which \(p\) is a coordinate. Consequently \(f\) is a coordinate of \(k[x_1,x_2,x_3,x_4,w]\).

**Proof.** Extend \(\Delta\) by \(\Delta(w)=0\). The automorphism \(\exp(w\Delta)\) of \(P[w]\) fixes \(p\) and sends \(H\) to \(H+pw\), so \(A[w]\cong P[w]/(H+pw)\) by an isomorphism fixing \(p\). Put \(x_0=s^2-u^2\) and

\[
L=x_0^2F-(1+2sx_0)J,\qquad N=(1-2sx_0)F+4s^2J,
\]

a linear change of \(F,J\) over \(k[p,s,u]\) of determinant \(4s^2x_0^2+(1+2sx_0)(1-2sx_0)=1\), with inverse \(F=4s^2L+(1+2sx_0)N\), \(J=-(1-2sx_0)L+x_0^2N\). Expanding \(x=x_0+pF\) in \(H\) gives

\[
H=L-u+pQ_0,\qquad Q_0=2x_0F^2+pF^3-2sFJ-J^2\in P .
\]

So \(H+pw=L-u+pw'\) with \(w'=w+Q_0\), and \(p,s,u,L,N,w'\) are coordinates of \(P[w]\). The relation lets us eliminate \(L=u-pw'\), and

\[
P[w]/(H+pw)\cong k[p,s,u,N,w'],
\]

a polynomial ring with \(p\) among its coordinates. By Proposition 2.1, \(A=k[x_1,\ldots,x_4]\) with \(p=f\), so \(f\) is a coordinate of \(k[x_1,\ldots,x_4,w]\). \(\square\)

**Proposition 3.2.** For every \(\lambda\in k\), \(A/(p-\lambda)\cong k^{[3]}\). So every fibre \(f=\lambda\) is isomorphic to affine three-space.

**Proof.** For \(\lambda=0\): modulo \(p\), \(H\equiv L-u\), and \(P/pP=k[s,u,L,N]\), so \(A/pA\cong k[s,u,N]\). For \(\lambda\ne0\): by (3.1) and the coordinates \(x,y,z,u\), \(A/(p-\lambda)=k[x,y,z,u]/\bigl(xy-z(z+1)-\lambda u\bigr)\), and eliminating \(u\) gives \(k[x,y,z]\). \(\square\)

## 4. A filtration and its graded ring

Give the generators of \(P\) the **weights** \(\omega(p,s,u,F,J)=(-1,0,0,1,1)\), and let \(\mathcal F_dA\) be the image in \(A\) of the span of the monomials of weight at most \(d\). Then \(x\) has weight zero, and

\[
H=H_*-u,\qquad H_*=x^2F-(1+2sx)J-pJ^2,
\tag{4.1}
\]

where \(H_*\) is homogeneous of weight one and \(u\) has weight zero.

**Proposition 4.1.** The filtration is exhaustive and separated, and its associated graded ring is the domain

\[
G=\operatorname{gr}A\cong P/(H_*),
\]

graded by the weights; the classes of \(p,s,u,F,J\) are nonzero, of degrees \(-1,0,0,1,1\). For \(0\ne a\in A\) put \(\deg a=\min\{d:a\in\mathcal F_dA\}\). This is a degree function on \(A\), and the generators \(p,s,u,F,J\) are exact for it.

**Proof.** Every element has a polynomial representative, so the filtration is exhaustive. A monomial of weight at most \(-r\) contains \(p\) at least \(r\) times, so \(\mathcal F_{-r}A\subset p^rA\). In the factorial ring \(A\cong k^{[4]}\), a nonzero element is divisible by only finitely many powers of the nonzero nonunit \(p\), so \(\bigcap_rp^rA=0\) and the filtration is separated.

The natural map \(P\to\operatorname{gr}A\) sends a homogeneous polynomial of weight \(d\) to its class in \(\mathcal F_dA/\mathcal F_{d-1}A\); it is surjective. A homogeneous \(Q_d\) of weight \(d\) lies in its kernel exactly when \(Q_d-R=qH\) for some \(R\) of weight less than \(d\) and some \(q\in P\). If \(q\ne0\), the top-weight part of \(qH\) is \((\operatorname{top}q)H_*\), because \(P\) is a graded domain, and it must equal \(Q_d\). So the kernel is \((H_*)\); conversely \(H_*=H+u\equiv u\) has class zero in degree one.

To see that \(H_*\) is prime, use the coordinates \(x,y,z,u\) of \(P[p^{-1}]\): there \(pH_*=xy-z(z+1)\) by (3.1) and (4.1), an irreducible polynomial, and \(p\) is a unit. Modulo \(p\), \(H_*\equiv x_0^2F-(1+2sx_0)J\ne0\). As in Lemma 1.1 of [Cancellation fails in dimension four](cancellation-fails-in-dimension-four.md), \(H_*\) is irreducible in \(P\), hence prime. It is not associated to any of the five variables, so their classes are nonzero.

Since \(G\) is a domain, the classes of nonzero elements multiply to nonzero classes, so \(\deg(ab)=\deg a+\deg b\); the other properties of a degree function are clear. Exactness of the generators is the definition of \(\mathcal F_dA\). \(\square\)

Write \(\tau\) for the class of \(p\) in \(G\). Let \(B=k[x,y,z,u]/(xy-z(z+1))\), the ring called \(R\) in [Cancellation fails in dimension four](cancellation-fails-in-dimension-four.md). In \(G\), the elements \(x=s^2-u^2+\tau F\), \(y=s+x(x+u^2)\), \(z=sx+\tau J\) and \(u\) satisfy \(xy-z(z+1)=\tau H_*=0\), so they define a homomorphism \(B\to G\) into degree zero. After inverting \(\tau\), the inverse formulas of Section 3 give

\[
G[\tau^{-1}]=B[\tau,\tau^{-1}],\qquad\deg B=0,\ \deg\tau=-1 .
\]

So \(B\to G\) is injective. In \(B\) put

\[
s_B=y-x(x+u^2),\qquad f_0=x-s_B^2+u^2,\qquad g_0=z-s_Bx,\qquad I=(f_0,g_0)\subset B .
\]

Inside \(B[\tau^{\pm1}]\), \(s=s_B\), \(F=f_0/\tau\) and \(J=g_0/\tau\), so

\[
G=B[\tau,f_0/\tau,g_0/\tau]=B[\tau,I/\tau].
\]

**Lemma 4.2.** For every \(\ell>0\), the degree-\(\ell\) component of \(G\) is \(G_\ell=\tau^{-\ell}I^\ell\).

**Proof.** \(G\) is spanned by the elements \(b\tau^r(f_0/\tau)^i(g_0/\tau)^j\) with \(b\in B\) and \(r,i,j\ge0\), of degree \(i+j-r\). If this degree is \(\ell\), the element is \(\tau^{-\ell}bf_0^ig_0^j\) with \(bf_0^ig_0^j\in I^{\ell+r}\subset I^\ell\). Conversely \(\tau^{-\ell}f_0^ig_0^j\in G\) for \(i+j=\ell\). \(\square\)

## 5. A coordinate would give a derivation of the quadric

**Proposition 5.1.** If \(p\) is a coordinate of \(A\), there are a nonzero locally nilpotent derivation \(E\) of \(B\) and an element \(0\ne h\in I\) with \(E(h)=0\).

**Proof.** Let \(A=k[p,q_1,q_2,q_3]\). Some \(q_i\) has positive degree: otherwise \(p\) and the \(q_i\) would all lie in the subalgebra \(\mathcal F_0A\), which does not contain \(F\). Renumber so that \(\deg q_1=\ell>0\), and let \(D=\partial/\partial q_2\), a nonzero locally nilpotent derivation of \(A\) with \(D(p)=D(q_1)=0\). By Propositions 6.1 and 6.2 of [Locally nilpotent derivations](locally-nilpotent-derivations.md), \(D\) induces a nonzero homogeneous locally nilpotent derivation \(D_0\) of \(G\), of some degree shift \(m\), with \(D_0(\tau)=0\) and \(D_0(\eta)=0\) for the class \(\eta\) of \(q_1\), which is homogeneous of degree \(\ell\).

Since \(D_0(\tau)=0\), \(D_0\) extends to a locally nilpotent derivation of \(G[\tau^{-1}]=B[\tau^{\pm1}]\). For \(b\in B\), \(D_0(b)\) has degree \(m\), and the degree-\(m\) component of \(B[\tau^{\pm1}]\) is \(\tau^{-m}B\); so \(D_0(b)=\tau^{-m}E(b)\) for a unique \(E(b)\in B\). Then \(E\) is a derivation of \(B\), with \(E^r(b)=\tau^{rm}D_0^r(b)\), so it is locally nilpotent. It is nonzero, since otherwise \(D_0\) would kill \(B\) and \(\tau\), hence \(G\). By Lemma 4.2, \(\eta=\tau^{-\ell}h\) with \(0\ne h\in I^\ell\subset I\), and \(0=D_0(\eta)=\tau^{-\ell-m}E(h)\). \(\square\)

## 6. The line bundle and the obstruction

Let \(C=k[a,d,b,c,u]/(ac-bd-1)\), with \(x=ab\), \(y=dc\), \(z=db\), and fibre weights \(\operatorname{wt}(a)=\operatorname{wt}(d)=1\), \(\operatorname{wt}(b)=\operatorname{wt}(c)=-1\), \(\operatorname{wt}(u)=0\). This is the ring \(\widetilde R\) of [Cancellation fails in dimension four, Proposition 4.1](cancellation-fails-in-dimension-four.md), a Laurent bundle algebra over \(B\); and \(B\) is a smooth domain by Lemma 1.1 there, hence a regular Noetherian domain. Put

\[
v=a^2(x+u^2)-d^2=a^3b+a^2u^2-d^2 .
\]

**Lemma 6.1.** \(IC=vC\).

**Proof.** In \(C[a^{-1}]\) put \(\xi=d/a\) and \(j=x+u^2-\xi^2\). The relation \(ac-bd=1\) gives \(z=\xi x\) and \(y=\xi+\xi^2x\), hence \(s_B=\xi-xj\), and then

\[
f_0=(1+2\xi x-x^2j)\,j,\qquad g_0=x^2j,\qquad v=a^2j .
\]

Since \((1-2\xi x)(1+2\xi x-x^2j)+x^2(4\xi^2+j-2\xi xj)=1\), the two coefficients of \(j\) generate the unit ideal, so \(IC[a^{-1}]=jC[a^{-1}]=vC[a^{-1}]\). At a prime of \(C\) containing \(a\), we have \(bd=-1\), \(x=0\) and \(z=-1\), so \(g_0\equiv-1\) and \(v\equiv-d^2\) are units of the local ring, and both ideals are the unit ideal there. Two ideals that agree after localizing at every prime are equal. \(\square\)

**Proposition 6.2.** If \(E\) is a nonzero locally nilpotent derivation of \(B\) killing some \(0\ne h\in I\), then there is a nonzero locally nilpotent derivation \(\widetilde E\) of \(C\) that preserves the fibre weights and kills \(v\).

**Proof.** Theorem 3.2 of [Additive actions on line bundles](additive-actions-on-line-bundles.md) gives a weight-preserving locally nilpotent \(\widetilde E\) extending \(E\), nonzero because \(E\) is. By Lemma 6.1, \(h=vq\) in \(C\) with \(q\ne0\). Since \(\widetilde E(h)=E(h)=0\) and kernels are factorially closed (Proposition 3.2 of [Locally nilpotent derivations](locally-nilpotent-derivations.md)), \(\widetilde E(v)=0\). \(\square\)

**Proposition 6.3.** No nonzero locally nilpotent derivation of \(C\) preserves the fibre weights and kills \(v\).

**Proof.** Suppose \(\widetilde E\) is one. Grade \(C\) by the auxiliary degrees \((a,d,b,c,u)\mapsto(0,1,-1,0,1)\); the relation is homogeneous of degree zero, and this grading commutes with the fibre weights. Let \(E'\) be the component of \(\widetilde E\) of largest auxiliary shift \(\lambda\), a nonzero locally nilpotent derivation preserving fibre weights (Proposition 5.1 of [Locally nilpotent derivations](locally-nilpotent-derivations.md)). In \(v=a^3b+(a^2u^2-d^2)\), the first term has auxiliary degree \(-1\) and the second degree \(2\). So the component of degree \(2+\lambda\) of \(\widetilde E(v)=0\) is \(E'(a^2u^2-d^2)=0\).

Now \(a^2u^2-d^2=(au-d)(au+d)\), and both factors are nonzero. By factorial closure, \(E'\) kills \(au-d\) and \(au+d\), hence \(d\) and \(au\), and then \(a\) and \(u\):

\[
E'(a)=E'(d)=E'(u)=0 .
\]

As in Proposition 8.1 of [Cancellation fails in dimension four](cancellation-fails-in-dimension-four.md), the element \(h=cE'(b)-bE'(c)\) satisfies \(ah=E'(b)\), \(dh=E'(c)\), lies in \(k[a,d,u]\), and is nonzero. Since \(E'\) preserves fibre weights, \(E'(b)\) has weight \(-1\) and \(h\) has weight \(-2\). But every nonzero homogeneous element of \(k[a,d,u]\) has nonnegative weight. \(\square\)

## 7. Conclusion

**Theorem 7.1.** The polynomial \(f=x_1-2Q(Q(x_2+x_4)+x_1x_4)\), with \(Q=x_2^2-x_4^2+x_1x_3\), is a coordinate of \(k[x_1,x_2,x_3,x_4,w]\) but not of \(k[x_1,x_2,x_3,x_4]\).

**Proof.** The first assertion is Proposition 3.1. If \(f\) were a coordinate, then by Proposition 2.1 so would be \(p\in A\); Proposition 5.1 would give a derivation \(E\) of \(B\) killing a nonzero element of \(I\), Proposition 6.2 would give a derivation of \(C\) that Proposition 6.3 excludes. \(\square\)

*Reference:* [OpenAI-stable, Theorem 1.1].

**Corollary 7.2.** For every \(\lambda\in k\), the hypersurface \(f=\lambda\) in \(\mathbb A^4\) is isomorphic to \(\mathbb A^3\), but no automorphism of \(\mathbb A^4\) carries it onto a coordinate hyperplane.

**Proof.** The first part is Proposition 3.2; in particular \((f-\lambda)\) is a prime ideal. If an automorphism carried the hypersurface onto a coordinate hyperplane, it would carry its prime ideal \((f-\lambda)\) onto the ideal of a coordinate \(g\); two generators of the same principal ideal differ by a nonzero constant, so \(f-\lambda\), and hence \(f\), would be a coordinate. \(\square\)

So this polynomial is a counterexample to the Abhyankar–Sathaye question of [Coordinates and the Abhyankar–Sathaye problem](coordinates-and-the-abhyankar-sathaye-problem.md) of a different kind from the one constructed there: all of its fibres are affine spaces, and its gradient vanishes nowhere on them, since a critical point would make the fibre through it singular.

## 8. Exercises

**Exercise 8.1 (easy).** Check that \(f\) has degree five and compute \(f(1,0,0,0)\) and \(f(0,0,0,0)\).

**Exercise 8.2 (medium).** Verify the values (3.2) by differentiating the inverse formulas, and check that \(\Delta(H)=p\).

**Exercise 8.3 (medium).** Show that \(f\) has no critical point: \(\nabla f\) vanishes nowhere on \(k^4\), even over an algebraic closure of \(k\).

## 9. Solutions

**8.1.** \(Q\) has degree two and \(Q(x_2+x_4)+x_1x_4\) has degree three, so \(2Q(\cdots)\) has degree five, with leading part \(2(x_2^2-x_4^2+x_1x_3)^2(x_2+x_4)\neq0\). At \((1,0,0,0)\), \(Q=0\), so \(f=1\); at the origin \(f=0\).

**8.2.** From \(s=y-x(x+u^2)\): \(\Delta(s)=-2xu\,\Delta(u)=2pxu\). From \(pF=x-s^2+u^2\): \(p\Delta(F)=-2s\Delta(s)+2u\Delta(u)=-4psxu-2pu\). From \(pJ=z-sx\): \(p\Delta(J)=-x\Delta(s)=-2px^2u\). Finally \(H=p^{-1}(xy-z(z+1))-u\) gives \(\Delta(H)=-\Delta(u)=p\).

**8.3.** By Proposition 3.2 over an algebraic closure \(\bar k\), every fibre \(f=\lambda\) with \(\lambda\in\bar k\) is isomorphic to \(\mathbb A^3\), hence smooth, with every local ring of embedding dimension three. If \(\nabla f(P_0)=0\) at a point with \(f(P_0)=\lambda\), then \(f-\lambda\) lies in the square of the maximal ideal of \(P_0\), and the local ring of the fibre at \(P_0\) would have embedding dimension four, as in Proposition 4.3 of [Coordinates and the Abhyankar–Sathaye problem](coordinates-and-the-abhyankar-sathaye-problem.md).

## References

- [OpenAI-stable] OpenAI, A stable coordinate that is not a coordinate in four variables, preprint, 5 October 2026. https://github.com/openai/math/blob/main/preprints/A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026/stable-coordinate-four-variables.pdf
- [Shpilrain–Yu] V. Shpilrain, J.-T. Yu, Affine varieties with equivalent cylinders, J. Algebra 251 (2002), 295–307. https://doi.org/10.1006/jabr.2001.9124
- [OpenAI-cancellation] OpenAI, An explicit failure of complex affine-space cancellation, preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/paper.pdf
