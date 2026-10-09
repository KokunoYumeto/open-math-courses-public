# Coordinates and the Abhyankar–Sathaye problem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A polynomial \(f\) in \(n\) variables is a coordinate if it is one component of a polynomial automorphism of affine space. Every fibre \(f=c\) of a coordinate is then a copy of affine \((n-1)\)-space, and the gradient of \(f\) vanishes nowhere. Abhyankar and Sathaye asked for the converse: if the single hypersurface \(f=0\) is isomorphic to affine \((n-1)\)-space, must \(f\) be a coordinate? This lesson constructs a polynomial in four variables, of degree \(17\), whose zero set is isomorphic to affine three-space, although its gradient vanishes at a point of the fibre \(f=-1\). So the answer is no in every dimension \(n\geq4\). The proof is elementary: one lemma about solving two compatible linear equations, a change of variables in a cusp equation, and one derivative.

We use [Keller maps and the Jacobian conjecture](keller-maps-and-the-jacobian-conjecture.md) for the chain rule and Proposition 1.1, and the embedding dimension of a local ring from [Dimension theory of Noetherian local rings](course:AG-CA/dimension-theory-of-noetherian-local-rings#4-parameters-and-embedding-dimension).

Basic references are [OpenAI-AS] and [Kraft].

## 1. Coordinates

Let \(k\) be a field and \(R=k[z_1,\ldots,z_n]\). Write \(k^{[m]}\) for a polynomial ring over \(k\) in \(m\) variables, and \(\nabla f=(\partial f/\partial z_1,\ldots,\partial f/\partial z_n)\) for the gradient of \(f\in R\).

**Definition 1.1.** A polynomial \(f\in R\) is a **coordinate** if there are \(f_2,\ldots,f_n\in R\) such that \((f,f_2,\ldots,f_n)\) is a polynomial automorphism of \(k^n\).

For example \(z_1+z_2^2\) is a coordinate of \(k[z_1,z_2,z_3]\), with complement \((z_2,z_3)\): after renumbering the variables, the map \((z_1+z_2^2,z_2,z_3)\) is triangular, so it is an automorphism by Proposition 5.1 of the first lesson.

**Proposition 1.2.** Let \(f\) be a coordinate of \(R\).

1. For every \(c\in k\), the algebra \(R/(f-c)\) is isomorphic to \(k^{[n-1]}\).
2. For every field \(K\supseteq k\), the gradient \(\nabla f\) has no zero in \(K^n\).

**Proof.** Let \(\Phi=(f,f_2,\ldots,f_n)\) be an automorphism, and let \(\varphi:k[y_1,\ldots,y_n]\to R\) be the homomorphism with \(\varphi(y_i)=\Phi_i\). As in the proof of Theorem 4.1 of the first lesson, \(\varphi\) is an isomorphism. It carries the ideal \((y_1-c)\) onto \((f-c)\), so \(R/(f-c)\cong k[y_1,\ldots,y_n]/(y_1-c)\cong k[y_2,\ldots,y_n]\). This proves the first part. For the second, \(\Phi\) is still an automorphism over \(K\), so \(\det J\Phi\) is a nonzero constant by Proposition 1.1 of the first lesson. At every point \(p\in K^n\) the matrix \(J\Phi(p)\) is therefore invertible, and its first row \(\nabla f(p)\) is not zero. \(\square\)

**The Abhyankar–Sathaye problem.** Suppose \(R/(f)\cong k^{[n-1]}\) as \(k\)-algebras. Is \(f\) a coordinate? Geometrically: can every closed embedding of affine \((n-1)\)-space as a hypersurface in affine \(n\)-space be moved onto a coordinate hyperplane by an automorphism of the ambient space?

For \(n=2\) and \(k\) of characteristic zero, the answer is yes, by the theorem of Abhyankar and Moh, proved independently by Suzuki [Abhyankar–Moh], [Suzuki]. In higher dimensions the answer was known to be yes for special shapes of the equation. Sathaye proved it in three variables for polynomials linear in one variable, and Russell extended this to arbitrary fields [Sathaye], [Russell]. In four variables, Kaliman, Vénéreau and Zaidenberg treated polynomials of the form \(a(x)y+b(x,z,t)\) [KVZ]. We do not use these results.

Proposition 1.2 gives two invariants that every coordinate has and an isomorphism of the single fibre \(f=0\) does not provide: all the other fibres, and the zeros of the gradient on the whole space. Shpilrain and Yu used the zeros of the gradient to distinguish embeddings of isomorphic hypersurfaces, and asked whether the gradient of \(f\) must vanish nowhere when \(R/(f)\cong k^{[n-1]}\) [Shpilrain–Yu]. The example below, found in 2026 [OpenAI-AS], answers both questions negatively.

## 2. Solving two compatible linear equations

The construction is built around the cuspidal cubic \(X^2+Y^3=0\), parametrized by \((U^3,-U^2)\). Perturb the parametrization by multiples of a parameter \(H\): put \(X=U^3+HV\) and \(Y=-U^2+HW\). Then \(X^2+Y^3\) vanishes modulo \(H\), and it is in fact divisible by \(H\):

\[
(U^3+HV)^2+(-U^2+HW)^3=H\,S(H,U,V,W),
\tag{2.1}
\]
\[
S(H,U,V,W)=2U^3V+3U^4W+H\bigl(V^2-3U^2W^2\bigr)+H^2W^3 .
\]

Indeed, the terms \(U^6\) cancel and every remaining term contains \(H\). All rings below are commutative with identity.

**Lemma 2.1.** Let \(B\) be a ring and \(h,x,y,s\in B\) with

\[
x^2+y^3=hs\qquad\text{and}\qquad hB+yB=B .
\tag{2.2}
\]

Then the \(B\)-algebra

\[
C=B[U,V,W]\big/\bigl(U^3+hV-x,\ \ -U^2+hW-y,\ \ S(h,U,V,W)-s\bigr)
\]

is isomorphic to the polynomial ring \(B[T]\).

**Proof.** Choose \(\alpha,\beta\in B\) with \(\alpha h+\beta y=1\).

*Step 1: a linear change of variables.* Substitute \(V=G-UW\), an automorphism of \(B[U,V,W]\) over \(B[U,W]\) with inverse \(G=V+UW\). Modulo the second relation \(hW=y+U^2\), the first relation becomes

\[
U^3+hG-U\cdot hW-x\equiv U^3+hG-U(y+U^2)-x=hG-yU-x ,
\]

and expanding \(S(h,U,G-UW,W)\), then replacing \(hW\) by \(y+U^2\) wherever it occurs, gives

\[
S(h,U,G-UW,W)\equiv hG^2-2yUG+y^2W .
\]

Hence

\[
C\cong B[U,G,W]\big/\bigl(hG-yU-x,\ \ hW-(y+U^2),\ \ y^2W-(s-hG^2+2yUG)\bigr).
\tag{2.3}
\]

*Step 2: eliminating \(W\).* Let \(A=B[U,G]/(hG-yU-x)\), and in \(A\) put \(a=y+U^2\) and \(b=s-hG^2+2yUG\). By (2.3), \(C\cong A[W]/(hW-a,\ y^2W-b)\). The two linear equations are compatible:

\[
y^2a-hb=y^2U^2+y^3-hs+h^2G^2-2hyUG=(hG-yU)^2+y^3-hs=x^2+y^3-hs=0 .
\]

Put \(r=\alpha(1+\beta y)\) and \(q=\beta^2\). Then \(rh+qy^2=(1-\beta y)(1+\beta y)+\beta^2y^2=1\). Let \(W_0=ra+qb\in A\). Using \(hb=y^2a\),

\[
hW_0=rha+qy^2a=a,\qquad y^2W_0=ry^2a+qy^2b=rhb+qy^2b=b .
\]

So \(hW-a=h(W-W_0)\) and \(y^2W-b=y^2(W-W_0)\), while \(W-W_0=r(hW-a)+q(y^2W-b)\). The ideal generated by the two equations in \(A[W]\) is therefore the principal ideal \((W-W_0)\), and \(C\cong A[W]/(W-W_0)\cong A\).

*Step 3: \(A\) is a polynomial ring.* Define \(B\)-algebra homomorphisms

\[
A\to B[T],\quad U\mapsto hT-\beta x,\ \ G\mapsto yT+\alpha x;\qquad
B[T]\to A,\quad T\mapsto\alpha U+\beta G .
\]

The first is well defined because \(h(yT+\alpha x)-y(hT-\beta x)=(\alpha h+\beta y)x=x\). The composite \(B[T]\to A\to B[T]\) sends \(T\) to \(\alpha(hT-\beta x)+\beta(yT+\alpha x)=T\). For the other composite, in \(A\) we have \(hG=yU+x\), hence

\[
h(\alpha U+\beta G)-\beta x=(\alpha h+\beta y)U=U,\qquad
y(\alpha U+\beta G)+\alpha x=(\alpha h+\beta y)G=G .
\]

Both composites are identities, so \(A\cong B[T]\), and \(C\cong B[T]\). \(\square\)

The proof never divides by \(h\) or \(y\), and \(B\) may have zero divisors. The isomorphism is explicit: \(T=\alpha U+\beta(V+UW)\), and conversely \(U,G\) come from Step 3, then \(W=W_0\) and \(V=G-UW\).

## 3. A hypersurface isomorphic to affine three-space

From now on \(k\) has characteristic zero. In \(R=k[h,u,v,w]\), define

\[
x=u^3+hv,\qquad y=-u^2+hw,\qquad s=S(h,u,v,w),
\tag{3.1}
\]

so that \(x^2+y^3=hs\) by (2.1). For independent variables \(x,y,s\), put

\[
p(x,y,s)=-2s^2x+3sy^2-3s^3y .
\]

This polynomial measures the effect of a translation along the cuspidal cubic:

\[
(x+s^3)^2+(y-s^2)^3=x^2+y^3-s\,p(x,y,s),
\tag{3.2}
\]

as one checks by expanding; the terms \(s^6\) cancel. Define

\[
F=h-1-p(x,y,s)\in R ,
\tag{3.3}
\]

with \(x,y,s\) given by (3.1). It is a polynomial of degree \(17\) in \(h,u,v,w\), with \(69\) terms.

**Theorem 3.1.** The algebra \(R/(F)\) is isomorphic to \(k^{[3]}\).

**Proof.** Introduce an auxiliary algebra in which \(x,y,s\) are independent variables:

\[
B=k[h,x,y,s]\big/\bigl(h-1-p(x,y,s),\ \ x^2+y^3-sh\bigr).
\]

*\(B\) is a polynomial ring in two variables.* Eliminating \(h\) with the first relation gives \(B\cong k[x,y,s]/\bigl(x^2+y^3-s-s\,p(x,y,s)\bigr)\). The substitution \(X=x+s^3\), \(Y=y-s^2\) is an automorphism of \(k[x,y,s]\) over \(k[s]\), and by (3.2) it turns the relation into \(X^2+Y^3-s\). Hence

\[
B\cong k[X,Y,s]/(X^2+Y^3-s)\cong k[X,Y].
\]

*The unit ideal condition.* Modulo \(h\) and \(y\), the relation \(x^2+y^3=sh\) gives \(x^2=0\), and the relation \(h=1+p\) gives \(0=1-2s^2x\). So \(2s^2x=1\), and squaring, \(1=4s^4x^2=0\). Thus \(B/(hB+yB)=0\), that is, \(hB+yB=B\).

*Applying the lemma.* Since \(x^2+y^3=sh\) holds in \(B\), Lemma 2.1 applies to \(B\) and its elements \(h,x,y,s\). Write \(u,v,w\) for the three new variables. Then

\[
C=k[h,x,y,s,u,v,w]\big/\bigl(h-1-p,\ x^2+y^3-sh,\ u^3+hv-x,\ -u^2+hw-y,\ S(h,u,v,w)-s\bigr)\cong B[T]\cong k^{[3]} .
\]

The last three relations express \(x\), \(y\) and \(s\) as the polynomials (3.1), so dividing by them identifies \(k[h,x,y,s,u,v,w]\) with \(R\). Under this identification the relation \(x^2+y^3-sh\) becomes zero, by (2.1), and \(h-1-p\) becomes \(F\). So \(C\cong R/(F)\), and \(R/(F)\cong k^{[3]}\). \(\square\)

The isomorphism is defined over \(\mathbb Q\) and can be written down; see Section 5.

## 4. A critical point

**Theorem 4.1.** The polynomial \(F\) is not a coordinate of \(k[h,u,v,w]\). Its gradient vanishes at the point

\[
P=(h,u,v,w)=\bigl(2,\ 0,\ -\tfrac12,\ \tfrac12\bigr),
\]

which lies on the fibre \(F=-1\).

**Proof.** In \(R\), with \(x,y,s\) as in (3.1), put \(X=x+s^3\) and \(Y=y-s^2\). By (3.2), \(x^2+y^3=hs\) and (3.3),

\[
X^2+Y^3=hs-s\,p=s\,(h-p)=s\,(1+F).
\tag{4.1}
\]

At \(P\): \(x=2\cdot(-\tfrac12)=-1\), \(y=2\cdot\tfrac12=1\), and \(s=2\cdot\tfrac14+4\cdot\tfrac18=1\). Hence \(X=-1+1=0\), \(Y=1-1=0\), \(p=2+3-3=2\) and \(F=2-1-2=-1\). Differentiate (4.1) with respect to any of the four variables:

\[
2X\,\partial X+3Y^2\,\partial Y=(1+F)\,\partial s+s\,\partial F .
\]

At \(P\) the left side vanishes and so does \(1+F\), while \(s=1\). Hence every partial derivative of \(F\) vanishes at \(P\). By Proposition 1.2, \(F\) is not a coordinate. \(\square\)

*Reference:* [OpenAI-AS, Theorem 1.1].

**Corollary 4.2.** For every \(n\geq4\) there is a polynomial \(f\in k[z_1,\ldots,z_n]\) with \(k[z_1,\ldots,z_n]/(f)\cong k^{[n-1]}\) that is not a coordinate.

**Proof.** Take \(f=F\) in \(R[z_5,\ldots,z_n]\). Then \(R[z_5,\ldots,z_n]/(F)\cong(R/(F))[z_5,\ldots,z_n]\cong k^{[n-1]}\) by Theorem 3.1. The derivatives of \(F\) in the new variables are zero, and its other derivatives vanish at \(P\), so the gradient vanishes at \((P,0,\ldots,0)\). \(\square\)

The critical point also shows that the fibre through it is not an affine space, so \(F\) fails the first condition of Proposition 1.2 as well.

**Proposition 4.3.** The algebra \(R/(F+1)\) is not isomorphic to \(k^{[3]}\).

**Proof.** Let \(\mathfrak m=(h-2,u,v+\tfrac12,w-\tfrac12)\), the maximal ideal of \(P\) in \(R\). Since \(F+1\) and all its first derivatives vanish at \(P\), its Taylor expansion at \(P\) starts in degree two, so \(F+1\in\mathfrak m^2\). The local ring \(\mathcal O=(R/(F+1))_{\mathfrak m}\) therefore has

\[
\mathfrak m\mathcal O\big/(\mathfrak m\mathcal O)^2\cong\mathfrak m/\bigl(\mathfrak m^2+(F+1)\bigr)=\mathfrak m/\mathfrak m^2\cong k^4,
\]

so its embedding dimension is four. Suppose \(\psi:R/(F+1)\to k[X,Y,T]\) were an isomorphism of \(k\)-algebras. It carries \(\mathfrak m/(F+1)\), whose residue field is \(k\), to a maximal ideal \(\mathfrak n\) of \(k[X,Y,T]\) with residue field \(k\). If \(X,Y,T\) have images \(a,b,c\in k\) in that residue field, then \(\mathfrak n\) contains the maximal ideal \((X-a,Y-b,T-c)\), hence equals it. So the maximal ideal of \(k[X,Y,T]_{\mathfrak n}\) is generated by three elements, and its embedding dimension is at most three [Dimension theory of Noetherian local rings, Proposition 4.2](course:AG-CA/dimension-theory-of-noetherian-local-rings#4-parameters-and-embedding-dimension). But \(\psi\) induces an isomorphism of these local rings, which preserves the embedding dimension. This is a contradiction. \(\square\)

So the zero fibre of \(F\) is affine three-space while the fibre over \(-1\) is singular. An isomorphism of one hypersurface with affine space says nothing about its neighbours.

## 5. Explicit coordinates on the zero fibre

The proofs of Lemma 2.1 and Theorem 3.1 give explicit formulas once \(\alpha\) and \(\beta\) with \(\alpha h+\beta y=1\) in \(B\) are known. Put

\[
\alpha=1+2s^2x+4s^5,\qquad \beta=(3s^3-3sy)(1+2s^2x)-4s^4y^2 .
\]

**Proposition 5.1.** In \(k[h,x,y,s]\),

\[
\alpha h+\beta y-1=(1+2s^2x)\bigl(h-1-p(x,y,s)\bigr)-4s^4\bigl(x^2+y^3-sh\bigr).
\tag{5.1}
\]

Consequently \(\alpha h+\beta y=1\) in \(B\), and the polynomials

\[
X=x+s^3,\qquad Y=y-s^2,\qquad T=\alpha u+\beta(v+uw),
\tag{5.2}
\]

with \(x,y,s\) given by (3.1), define an isomorphism \(k[X,Y,T]\to R/(F)\). The inverse isomorphism sends \(h,u,v,w\) to the polynomials in \(X,Y,T\) computed in this order:

\[
\begin{aligned}
&s=X^2+Y^3,\quad x=X-s^3,\quad y=Y+s^2,\quad h=1+p(x,y,s),\\
&u=hT-\beta x,\quad g=yT+\alpha x,\quad w=\alpha(1+\beta y)(y+u^2)+\beta^2\bigl(s-hg^2+2uyg\bigr),\quad v=g-uw .
\end{aligned}
\]

**Proof.** Identity (5.1) is checked by expanding both sides. The rest is the chain of isomorphisms in the proofs of Theorem 3.1 and Lemma 2.1, with \(r=\alpha(1+\beta y)\), \(q=\beta^2\) and \(W_0=ra+qb\). \(\square\)

## 6. Exercises

**Exercise 6.1 (easy).** Show that \(z_1+z_2^2+z_3^3z_2\) is a coordinate of \(k[z_1,z_2,z_3]\).

**Exercise 6.2 (easy).** Verify the identity (2.1) and the identity (3.2).

**Exercise 6.3 (medium).** Let \(D=h\,\partial_u-3u^2\,\partial_v+2u\,\partial_w\), a derivation of \(R\). Show that \(D\) kills \(h\), \(x\), \(y\) and \(s\), and hence \(F\).

**Exercise 6.4 (medium).** Show that a polynomial \(f\in k[z_1,\ldots,z_n]\) with a critical point on the fibre \(f=c\) cannot satisfy \(k[z_1,\ldots,z_n]/(f-c)\cong k^{[n-1]}\). (Adapt the proof of Proposition 4.3.)

## 7. Solutions

**6.1.** The map \((z_1+z_2^2+z_3^3z_2,\ z_2,\ z_3)\) is triangular in the order \(z_3,z_2,z_1\): its inverse is \((y_1-y_2^2-y_3^3y_2,\ y_2,\ y_3)\). So the given polynomial is a coordinate, with complement \((z_2,z_3)\).

**6.2.** For (2.1): \((U^3+HV)^2=U^6+2HU^3V+H^2V^2\) and \((-U^2+HW)^3=-U^6+3HU^4W-3H^2U^2W^2+H^3W^3\). The sum is \(H\) times \(2U^3V+3U^4W+H(V^2-3U^2W^2)+H^2W^3\). For (3.2): \((x+s^3)^2+(y-s^2)^3=x^2+y^3+2s^3x-3s^2y^2+3s^4y\), and \(-s\,p=2s^3x-3s^2y^2+3s^4y\).

**6.3.** \(D(h)=0\). \(D(x)=h\cdot3u^2+h\cdot(-3u^2)=0\) and \(D(y)=h\cdot(-2u)+h\cdot2u=0\). Applying \(D\) to \(hs=x^2+y^3\) gives \(h\,D(s)=0\), and \(h\) is not a zero divisor in the domain \(R\), so \(D(s)=0\). A derivation that kills \(h,x,y,s\) kills every polynomial in them, in particular \(F\).

**6.4.** Let \(P\) be a point of \(k^n\) with \(f(P)=c\) and \(\nabla f(P)=0\), and \(\mathfrak m\) its maximal ideal. Then \(f-c\in\mathfrak m^2\), so the local ring of \(k[z]/(f-c)\) at \(\mathfrak m\) has embedding dimension \(n\). Every local ring of \(k^{[n-1]}\) at a maximal ideal with residue field \(k\) has embedding dimension at most \(n-1\). As in Proposition 4.3, an isomorphism would carry one to the other.

## References

- [OpenAI-AS] OpenAI, An explicit noncoordinate polynomial with affine three-space zero fibre, preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026/paper.pdf
- [Kraft] H. Kraft, Challenging problems on affine n-space, Séminaire Bourbaki, Exposé 802, Astérisque 237 (1996), 295–317. https://numdam.org/item/SB_1994-1995__37__295_0/
- [KVZ] S. Kaliman, S. Vénéreau, M. Zaidenberg, Simple birational extensions of the polynomial algebra C^[3], Trans. Amer. Math. Soc. 356 (2004), 509–555. https://arxiv.org/abs/math/0104204
- [Shpilrain–Yu] V. Shpilrain, J.-T. Yu, Embeddings of hypersurfaces in affine spaces, J. Algebra 239 (2001), 161–173. https://arxiv.org/abs/math/0010211
- [Russell] P. Russell, Simple birational extensions of two dimensional affine rational domains, Compositio Math. 33 (1976), 197–208. https://www.numdam.org/item/CM_1976__33_2_197_0/
- [Sathaye] A. Sathaye, On linear planes, Proc. Amer. Math. Soc. 56 (1976), 1–7. https://doi.org/10.1090/S0002-9939-1976-0409472-6
- [Suzuki] M. Suzuki, Propriétés topologiques des polynômes de deux variables complexes, et automorphismes algébriques de l'espace C², J. Math. Soc. Japan 26 (1974), 241–257. https://doi.org/10.2969/jmsj/02620241
- [Abhyankar–Moh] S. S. Abhyankar, T. T. Moh, Embeddings of the line in the plane, J. Reine Angew. Math. 276 (1975), 148–166. https://doi.org/10.1515/crll.1975.276.148
