# Hypersurfaces of maximal contact

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

To reduce the order of an ideal \(\mathcal I\) of maximal order \(m\), we must blow up centres inside the set of points of order \(m\). The induction on dimension rests on one observation: near any point, this set lies in a smooth hypersurface \(H\), and it keeps lying in the strict transforms of \(H\) whatever blow-ups of order \(m\) we perform. Such an \(H\) is a hypersurface of maximal contact. Every blow-up sequence of order \(m\) for \(\mathcal I\) then restricts to a blow-up sequence for the marked ideal \((\mathcal I|_H,m)\) on the smaller-dimensional \(H\). This lesson constructs these hypersurfaces from derivatives, proves the "going-down" property, and shows by examples why the converse direction needs more work.

We use [Smooth blow-ups and transforms of ideals](smooth-blowups-and-transforms-of-ideals.md), [Blow-up sequences and the main theorems](blow-up-sequences-and-the-main-theorems.md) and [Derivative ideals under blowing up](derivative-ideals-under-blowing-up.md).

## 1. The ideal of maximal contact

**Definition 1.1.** Let \(\mathcal I\) be an ideal sheaf on a smooth scheme \(X\) with \(m=\operatorname{maxord}\mathcal I\ge1\). The *ideal of maximal contact* is

\[
MC(\mathcal I)=D^{m-1}(\mathcal I).
\]

**Lemma 1.2.** \(\operatorname{cosupp}(MC(\mathcal I),1)=\operatorname{cosupp}(\mathcal I,m)\). At a point \(x\) with \(\operatorname{ord}_x\mathcal I=m\), \(\operatorname{ord}_xMC(\mathcal I)=1\); at a point with \(\operatorname{ord}_x\mathcal I<m\), \(MC(\mathcal I)_x=\mathcal O_{X,x}\).

**Proof.** The first claim is [Derivative ideals under blowing up, Lemma 1.2](derivative-ideals-under-blowing-up.md#1-marked-derivative-ideals) with \(j=m-1\). Since \(\operatorname{maxord}\mathcal I=m\), \(D(MC(\mathcal I))=D^m(\mathcal I)=\mathcal O_X\) ([Smooth blow-ups and transforms of ideals, Proposition 2.6(3)](smooth-blowups-and-transforms-of-ideals.md#2-order-of-vanishing-and-derivative-ideals)). So at every point some element of \(MC(\mathcal I)\) or some first derivative of one is a unit, which means \(\operatorname{ord}_xMC(\mathcal I)\le1\) by the Taylor criterion. If \(\operatorname{ord}_x\mathcal I=m\), then \(x\in\operatorname{cosupp}(MC(\mathcal I),1)\) and the order is exactly \(1\). If \(\operatorname{ord}_x\mathcal I<m\), then \(x\notin\operatorname{cosupp}(MC(\mathcal I),1)\), so \(MC(\mathcal I)_x\) contains a unit. \(\square\)

## 2. Maximal contact

**Definition 2.1.** Let \(\mathcal I\) be an ideal sheaf on a smooth scheme \(X\), nonzero on every component, with \(m=\operatorname{maxord}\mathcal I\ge1\). A smooth closed hypersurface \(H\subset X\) (a smooth effective Cartier divisor, possibly reducible or empty) is a *hypersurface of maximal contact* for \(\mathcal I\) if for every open \(X^0\subset X\) and every blow-up sequence of order \(m\) starting with \((X^0,\mathcal I|_{X^0})\), every centre \(Z_i\) lies in the strict transform \(H_i\) of \(H\cap X^0\).

The divisors \(E\) play no role in this definition. A blow-up sequence of order \(m\) for a triple \((X^0,\mathcal I|_{X^0},E^0)\) is in particular one for \((X^0,\mathcal I|_{X^0},\emptyset)\), since the snc conditions only restrict the allowed centres.

**Definition 2.2.** A smooth closed hypersurface \(H\) is an *MC-hypersurface* for \(\mathcal I\) if it is locally defined by sections of \(MC(\mathcal I)\): every point has a neighbourhood \(U\) and \(h\in MC(\mathcal I)(U)\) with \(H\cap U=V(h)\).

**Theorem 2.3 (maximal contact).** Let \(\mathcal I\) be nonzero on every component of \(X\), with \(m=\operatorname{maxord}\mathcal I\ge1\).

1. *Local existence.* Every point \(x\in X\) has an open neighbourhood \(U\) carrying an MC-hypersurface for \(\mathcal I|_U\), which passes through \(x\) when \(\operatorname{ord}_x\mathcal I=m\).
2. *Maximal contact.* Every MC-hypersurface \(H\) is a hypersurface of maximal contact. Along every blow-up sequence of order \(m\) starting with \((X^0,\mathcal I|_{X^0})\), the strict transforms \(H_i\) are smooth hypersurfaces with \(\mathcal O(-H_i)\subset\mathcal J_i\), where \(\mathcal J_i\) is the transform of \((MC(\mathcal I),1)\); a component of \(H_i\) that is a component of the centre \(Z_i\) has empty strict transform.
3. *Going down.* If moreover \(\mathcal I|_H\) is nonzero on every component of \(H\), then along every such sequence no centre \(Z_i\) contains a component of \(H_i\), \(\mathcal I_i|_{H_i}\) is nonzero on every component of \(H_i\), and the restriction to \(H\cap X^0\) is a blow-up sequence of order \(\ge m\) starting with \((H\cap X^0,\mathcal I|_{H\cap X^0},m)\), with transforms \(\mathcal I_i|_{H_i}\).
4. *Persistence.* In the situation of (2), if \(\operatorname{maxord}\mathcal I_i=m\), then \(H_i\) is an MC-hypersurface for \(\mathcal I_i\), and \(\operatorname{cosupp}(\mathcal I_i,m)\subset H_i\). In the situation of (3), \(\mathcal I_i|_{H_i}\) is nonzero on every component.
5. *Pull-back.* If \(h:Y\to X\) is smooth and \(h(Y)\) meets \(\operatorname{cosupp}(\mathcal I,m)\), then \(\operatorname{maxord}h^*\mathcal I=m\), \(h^{-1}(H)\) is an MC-hypersurface for \(h^*\mathcal I\), and \(h^*\mathcal I|_{h^{-1}H}\) is nonzero on every component when \(\mathcal I|_H\) is.

**Proof.** (1) If \(\operatorname{ord}_x\mathcal I<m\), then by Lemma 1.2 some \(h\in MC(\mathcal I)\) is a unit near \(x\), and \(V(h)=\emptyset\) on a neighbourhood. If \(\operatorname{ord}_x\mathcal I=m\), Lemma 1.2 gives \(h\in MC(\mathcal I)_x\) with \(\operatorname{ord}_xh=1\): \(h(x)=0\) and \(dh(x)\ne0\). Then \(V(h)\) is smooth near \(x\) ([Smooth morphisms](course:AG-FSE/AG-FSE-05), Lemma 5.1).

(2) Restricting \(h\) to opens, we may take \(X^0=X\). Let \((X_i,\mathcal I_i)\) be a blow-up sequence of order \(m\) with centres \(Z_i\). Apply [Derivative ideals under blowing up, Theorem 3.1](derivative-ideals-under-blowing-up.md#3-the-basic-inclusion) with \(j=m-1\): the sequence is of order \(\ge1\) for \((\mathcal J_0,1)=(MC(\mathcal I),1)\), and the transforms satisfy \(\mathcal J_i\subset D^{m-1}(\mathcal I_i)\) and \(\operatorname{ord}_{Z_i}\mathcal J_i\ge1\). We prove by induction on \(i\) that \(H_i\) is smooth, \(\mathcal O_{X_i}(-H_i)\subset\mathcal J_i\) and \(Z_i\subset H_i\).

For \(i=0\), \(\mathcal O(-H)\subset MC(\mathcal I)=\mathcal J_0\) because the local equations of \(H\) are sections of \(MC(\mathcal I)\). Suppose \(H_i\) is smooth and \(\mathcal O(-H_i)\subset\mathcal J_i\). The order of \(\mathcal O(-H_i)\) along \(Z_i\) is at least that of \(\mathcal J_i\), hence \(\ge1\): \(Z_i\subset H_i\). The local equation of the smooth hypersurface \(H_i\) has order exactly \(1\) along each component of \(Z_i\). Over a component of \(Z_i\) of codimension \(\ge2\), the strict transform \(B_{Z_i}H_i\) is smooth and \(\pi_i^*\mathcal O(-H_i)=\mathcal O(-H_{i+1}-F_{i+1})\) there. A component of \(Z_i\) that equals a component \(H''\) of \(H_i\) is blown up trivially, its strict transform is empty, and \(\pi_i^*\mathcal O(-H_i)=\mathcal O(-H_i)=\mathcal O(-(H_i-H'')-F_{i+1})\) near it. In both cases \(H_{i+1}\) is smooth and

\[
\mathcal O(-H_{i+1})=(\pi_i)^{-1}_*\bigl(\mathcal O(-H_i),1\bigr)\subset(\pi_i)^{-1}_*(\mathcal J_i,1)=\mathcal J_{i+1}.
\]

This proves (2).

(3) We add to the induction the claim that \(\mathcal I_i|_{H_i}\) is nonzero on every component of \(H_i\); it holds for \(i=0\) by assumption. The centre contains no component \(H'\) of \(H_i\): otherwise \(\operatorname{ord}_{H'}\mathcal I_i\ge m\ge1\), so every section of \(\mathcal I_i\) vanishes on \(H'\) and \(\mathcal I_i|_{H'}=0\). By [Smooth blow-ups and transforms of ideals, Lemma 4.4](smooth-blowups-and-transforms-of-ideals.md#4-transforms-of-ideals-and-of-marked-ideals), applied to the hypersurface \(H_i\) and the centre \(Z_i\), we get \(\operatorname{ord}_{Z_i}(\mathcal I_i|_{H_i})\ge m\) and

\[
(\pi_i|_{H_{i+1}})^{-1}_*\bigl(\mathcal I_i|_{H_i},m\bigr)=\bigl((\pi_i)^{-1}_*(\mathcal I_i,m)\bigr)\big|_{H_{i+1}}=\mathcal I_{i+1}|_{H_{i+1}},
\]

using that the order-\(m\) transform of \(\mathcal I_i\) is the marked transform (Lemma 2.3 of [Blow-up sequences and the main theorems](blow-up-sequences-and-the-main-theorems.md#2-triples-and-the-blow-ups-they-allow)). The transform of an ideal that is nonzero on every component of \(H_i\), under the blow-up of a centre containing no component, is nonzero on every component of \(H_{i+1}\). This completes the induction and proves (3).

(4) If \(\operatorname{maxord}\mathcal I_i=m\), then \(D^{m-1}(\mathcal I_i)=MC(\mathcal I_i)\), and by (2), \(\mathcal O(-H_i)\subset\mathcal J_i\subset MC(\mathcal I_i)\). So the local equations of \(H_i\) are sections of \(MC(\mathcal I_i)\), and \(\operatorname{cosupp}(\mathcal I_i,m)=V(MC(\mathcal I_i))\subset H_i\) by Lemma 1.2. The last claim is part of the induction in (3).

(5) By [Smooth blow-ups and transforms of ideals, Proposition 2.6(4)](smooth-blowups-and-transforms-of-ideals.md#2-order-of-vanishing-and-derivative-ideals), orders are preserved by smooth pull-back and \(D^{m-1}(h^*\mathcal I)=h^*D^{m-1}(\mathcal I)\). Since \(h(Y)\) meets \(\operatorname{cosupp}(\mathcal I,m)\), \(\operatorname{maxord}h^*\mathcal I=m\), so \(D^{m-1}(h^*\mathcal I)=MC(h^*\mathcal I)\), which contains the pulled-back local equations of \(H\). The hypersurface \(h^{-1}(H)\) is smooth, being smooth over \(H\). The restriction \(h^*\mathcal I|_{h^{-1}H}\) is the pull-back of \(\mathcal I|_H\) under the smooth map \(h^{-1}H\to H\), which is open, so it is nonzero on every component. \(\square\)

**Corollary 2.4 (going down).** Let \(H\) be as in Theorem 2.3(3). Restriction to \(H\) maps blow-up sequences of order \(m\) for \((X,\mathcal I)\) injectively to blow-up sequences of order \(\ge m\) for \((H,\mathcal I|_H,m)\).

**Proof.** Theorem 2.3(3) gives the map. It is injective because the centres \(Z_i\subset H_i\) are the same in both sequences. \(\square\)

In positive characteristic this fails in general: there are hypersurface singularities of order \(2\) in characteristic \(2\) whose locus of order \(2\) is a curve contained in no smooth hypersurface. Kollár reproduces such an example of Narasimhan. Characteristic zero enters through Lemma 1.2, which rests on the Taylor criterion.

## 3. The converse fails

Going down says that every allowed blow-up for \(\mathcal I\) is allowed for \((\mathcal I|_H,m)\). The converse is false: the restriction can demand blow-ups that are not of order \(m\) for \(\mathcal I\).

**Example 3.1.** Let \(\mathcal I=(xy-z^n)\) on \(\mathbf A^3\), \(n\ge2\). The order is \(2\) at the origin and \(\le1\) elsewhere, since at \((a,b,c)\ne0\) on the surface one of \(x,y\) has a nonzero coefficient \(b\) or \(a\) in the linear part. Here \(MC(\mathcal I)=D(\mathcal I)=(xy-z^n,y,x,nz^{n-1})=(x,y,z^{n-1})\), so \(H=V(x)\) is an MC-hypersurface. But \(\mathcal I|_H=(z^n)\) on \(H\cong\mathbf A^2_{y,z}\) has order \(n\ge2\) along the whole line \(z=0\), and blowing up that line is not a blow-up of order \(2\) for \(\mathcal I\), whose order along the line is \(1\). For the MC-hypersurface \(H_g=V(x-y)\), however, \(\mathcal I|_{H_g}=(x^2-z^n)\) on \(H_g\cong\mathbf A^2_{x,z}\), which again has an isolated point of order \(2\).

**Example 3.2.** Even a well-chosen hypersurface can fail after blow-ups. Let \(\mathcal I=(x^3+xy^5+z^4)\) on \(\mathbf A^3\), of order \(3\) at the origin. Then \(D(\mathcal I)\ni3x^2+y^5,\ 5xy^4,\ 4z^3\), and \(D^2(\mathcal I)\ni6x,\ 5y^4,\ 12z^2\), so \(h=x+y^4+z^2\in MC(\mathcal I)\) has order \(1\), and \(H=V(h)\) is an MC-hypersurface. Blow up the origin and use the chart \(x=x_1y,\ z=z_1y\):

\[
\pi^*(x^3+xy^5+z^4)=y^3\bigl(x_1^3+x_1y^3+yz_1^4\bigr),\qquad \pi^*h=y\bigl(x_1+y^3+yz_1^2\bigr).
\]

The transform \(\mathcal I_1=(x_1^3+x_1y^3+yz_1^4)\) still has order \(3\) at the origin of the chart. Blow it up, chart \(x_1=x_2y,\ z_1=z_2y\):

\[
\mathcal I_2=(x_2^3+x_2y+y^2z_2^4),\qquad H_2=V\bigl(x_2+y^2+y^2z_2^2\bigr).
\]

Now \(\mathcal I_2\) has order \(2\) at the origin (from \(x_2y\)), and \(\operatorname{maxord}\mathcal I_2\le2\) on this chart: the order of reduction is complete there. But on \(H_2\), where \(x_2=-y^2(1+z_2^2)\),

\[
\mathcal I_2|_{H_2}=\bigl(-y^6(1+z_2^2)^3-y^3(1+z_2^2)+y^2z_2^4\bigr),
\]

which has order \(3\) at the origin. So the marked restriction \((H_2,\mathcal I_2|_{H_2},3)\) still has a point of order \(\ge3\), and order reduction for it would require further blow-ups that are not blow-ups of order \(3\) for \(\mathcal I_2\).

The next lesson identifies ideals for which the converse holds: the restriction of a suitably "balanced" ideal to any smooth hypersurface predicts its blow-ups exactly.

## 4. Exercises

**Exercise 4.1.** For \(\mathcal I=(x^2+y^2+z^2)\) on \(\mathbf A^3\), compute \(MC(\mathcal I)\) and determine the MC-hypersurfaces through the origin. Check that Theorem 2.3(3) applies to each of them.

*Solution.* The order is \(2\) at the origin and \(\le1\) elsewhere, so \(m=2\) and \(MC(\mathcal I)=D(\mathcal I)=(x^2+y^2+z^2,2x,2y,2z)=(x,y,z)\), the ideal of the origin. Every function vanishing at the origin lies in it, so every smooth surface through the origin is, near the origin, an MC-hypersurface. The restriction of \(\mathcal I\) to such a surface \(H\) is nonzero: otherwise \(H\) would be contained in the cone \(V(x^2+y^2+z^2)\), which is irreducible of dimension \(2\) and singular at the origin, so \(H\) would equal the cone near the origin, contradicting smoothness of \(H\).

**Exercise 4.2.** Let \(\mathcal I=(x^m)\) on \(\mathbf A^2\). Show that \(H=V(x)\) is a hypersurface of maximal contact in the sense of Definition 2.1, as Theorem 2.3(2) predicts, but that the going-down statement Theorem 2.3(3) does not apply. What does the restriction \((H,\mathcal I|_H,m)\) look like?

*Solution.* \(MC(\mathcal I)=D^{m-1}(x^m)=(x)\). The points of order \(m\) form the line \(H\), and the only possible centre of order \(m\) through them is \(H\) itself or a union of points on it; after blowing up \(H\) (a trivial blow-up) the transform is \(\mathcal O\). So every centre lies in \(H\) and its transforms, in accordance with Theorem 2.3(2). Theorem 2.3(3) does not apply because \(\mathcal I|_H=0\). The restriction is the zero ideal, so going down gives no information; such codimension-one parts of the cosupport are removed first by trivial blow-ups in the order reduction lessons.

**Exercise 4.3.** In Example 3.2, verify that \(\pi^*h=y(x_1+y^3+yz_1^2)\) and that the strict transform \(H_1\) passes through the centre of the second blow-up, as Theorem 2.3(2) predicts.

*Solution.* \(\pi^*(x+y^4+z^2)=x_1y+y^4+z_1^2y^2=y(x_1+y^3+yz_1^2)\). The second centre is the origin of the chart, where \(x_1+y^3+yz_1^2\) vanishes.

## References

- [Kollár] J. Kollár, *Resolution of singularities — Seattle lecture*, arXiv:math/0508332, section "Maximal contact and going down", Examples of bad restrictions. <https://arxiv.org/abs/math/0508332>
- [Włodarczyk] J. Włodarczyk, *Simple Hironaka resolution in characteristic zero*, arXiv:math/0401401, Giraud's lemma on maximal contact. <https://arxiv.org/abs/math/0401401>
