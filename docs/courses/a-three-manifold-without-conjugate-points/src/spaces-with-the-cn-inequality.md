# Spaces with the CN inequality

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The obstruction to nonpositive curvature takes place in the space on which the fundamental group acts: the universal cover of a nonpositively curved manifold, or more generally a CAT(0) space. This lesson develops, from a single inequality, the part of the geometry of such spaces that the obstruction needs. The inequality, a quadratic comparison with the Euclidean plane for a point and a geodesic segment, goes back to Bruhat and Tits [BT, (3.2.1)]; it holds in every CAT(0) space and in every Hadamard manifold. From it we derive uniqueness and convexity of geodesics, a four-point inequality, nearest-point projections onto convex sets, and an exact Pythagorean identity for parallel lines, together with the shifts between parallel lines measured by Busemann functions.

- Geodesic spaces and the CN inequality (Section 1).
- Geodesics and convexity (Section 2).
- Projections onto convex sets (Section 3).
- Parallel lines and Busemann functions (Section 4).

## 1. Geodesic spaces and the CN inequality

Let \((X,d)\) be a metric space. A *geodesic segment* from \(y\) to \(z\) is a map \(c\colon[0,L]\to X\) with \(L=d(y,z)\), \(c(0)=y\), \(c(L)=z\) and \(d(c(s),c(s'))=|s-s'|\) for all \(s,s'\). For \(t\in[0,1]\) we write \(c_t=c(tL)\), the point at fraction \(t\) of the segment; \(c_{1/2}\) is its *midpoint*. A *geodesic line* is a map \(c\colon\mathbb R\to X\) with \(d(c(s),c(s'))=|s-s'|\). The space is *geodesic* if any two points are joined by a geodesic segment.

**Definition 1.1.** A geodesic space \(X\) is a *CN space* if for every \(x\in X\), every geodesic segment \(c\) from \(y\) to \(z\) and every \(t\in[0,1]\),
\[
\begin{aligned}
&d(x,c_t)^2\le(1-t)\,d(x,y)^2\\
&\quad+t\,d(x,z)^2\\
&\quad-t(1-t)\,d(y,z)^2 .
\end{aligned} \tag{1.1}
\]

**Lemma 1.2.** In a real inner product space, for all vectors \(x,y,z\) and \(t\in[0,1]\),
\[
\begin{aligned}
&|x-(1-t)y-tz|^2\\
&\quad=(1-t)|x-y|^2+t|x-z|^2\\
&\qquad-t(1-t)|y-z|^2 .
\end{aligned}
\]

*Proof.* Put \(u=x-y\), \(w=x-z\); then \(x-(1-t)y-tz=(1-t)u+tw\) and \(y-z=w-u\). Expand both sides: each equals \((1-t)^2|u|^2+t^2|w|^2+2t(1-t)\langle u,w\rangle\). \(\square\)

So (1.1) is an equality in Euclidean space. A *geodesic triangle* in a geodesic space consists of three points and a choice of geodesic segments joining them in pairs. Its *comparison triangle* is a triangle in the Euclidean plane with the same side lengths; each point \(p\) of a side has a *comparison point* \(\bar p\) on the corresponding side, at the same distances from the two ends. The space is *CAT(0)* if for every geodesic triangle and all points \(p,q\) of it, \(d(p,q)\le|\bar p-\bar q|\) ([Davis, Appendix I.2]).

**Proposition 1.3.** Every CAT(0) space is a CN space.

*Proof.* Given \(x\) and a geodesic segment \(c\) from \(y\) to \(z\), form a geodesic triangle with vertices \(x,y,z\) and side \(c\). The comparison point of \(c_t\) is \((1-t)\bar y+t\bar z\), so \(d(x,c_t)\le|\bar x-(1-t)\bar y-t\bar z|\), and Lemma 1.2 gives (1.1). \(\square\)

**Proposition 1.4.** Let \(X\) be a Hadamard manifold, that is, a complete connected simply connected Riemannian manifold with nonpositive sectional curvature, with its Riemannian distance. Then \(X\) is a CN space, closed bounded subsets of \(X\) are compact, and the geodesic segments of \(X\) are its Riemannian geodesics from one point to another, parametrized by arc length.

*Proof.* By the Cartan–Hadamard theorem ([Comparison theorems, cut loci and curvature and topology, Theorem C.1](course:DG-FND/comparison-theorems-cut-loci-and-curvature-and-topology)), any two points \(y,z\) are joined by exactly one Riemannian geodesic \(\eta\colon[0,1]\to X\). By the Hopf–Rinow theorem ([Completeness and the Hopf–Rinow theorem](course:DG-FND/completeness-and-the-hopf-rinow-theorem)) some geodesic from \(y\) to \(z\) has length \(d(y,z)\), so \(\eta\) has this length, and closed bounded sets are compact. Hence \(s\mapsto\eta(s/L)\), \(L=d(y,z)\), is a geodesic segment, and the inequality (C.4) of Theorem C.2 there is (1.1) for it. If \(c\) is any geodesic segment from \(y\) to \(z\) and \(m=c_t\), then \(d(y,m)=tL\) and \(d(m,z)=(1-t)L\), and (C.4) with \(q=m\) gives
\[
\begin{aligned}
&d(m,\eta(t))^2\le(1-t)t^2L^2\\
&\quad+t(1-t)^2L^2-t(1-t)L^2=0 .
\end{aligned}
\]
So \(c\) is the reparametrized \(\eta\), and (1.1) holds for every geodesic segment. \(\square\)

From now on \(X\) is a CN space.

## 2. Geodesics and convexity

**Lemma 2.1** (uniqueness). Any two points \(y,z\) are joined by exactly one geodesic segment \(c\). For \(t\in[0,1]\), \(c_t\) is the only point \(m\) with \(d(y,m)=t\,d(y,z)\) and \(d(m,z)=(1-t)\,d(y,z)\).

*Proof.* Let \(L=d(y,z)\) and let \(m\) be such a point. Then (1.1) with \(x=m\) gives
\[
\begin{aligned}
&d(m,c_t)^2\le(1-t)t^2L^2\\
&\quad+t(1-t)^2L^2-t(1-t)L^2=0 .
\end{aligned}
\]
Applied to the points of a second geodesic segment, this shows that it coincides with \(c\). \(\square\)

We write \([y,z]\) for the image of the geodesic segment from \(y\) to \(z\). A restriction of a geodesic segment to a subinterval is a geodesic segment, so by uniqueness the segment between two points of \([y,z]\) is contained in \([y,z]\). If \(d(x,z)=d(x,y)+d(y,z)\), the concatenation of the segments from \(x\) to \(y\) and from \(y\) to \(z\), parametrized by arc length, is a geodesic segment: it has length \(d(x,z)\), so no two of its points are farther apart than their parameter difference, and the triangle inequality through the end points gives the reverse inequality.

**Lemma 2.2** (two segments from one point). Let \(x,y,z\in X\), let \(m\) be the midpoint of \([x,y]\) and \(m'\) the midpoint of \([x,z]\). Then \(d(m,m')\le\frac12d(y,z)\).

*Proof.* Apply (1.1) with \(t=\frac12\) to the segment \([x,y]\) and the point \(m'\), and to the segment \([x,z]\) and the point \(y\):
\[
\begin{aligned}
d(m',m)^2&\le\tfrac12d(m',x)^2+\tfrac12d(m',y)^2\\
&\quad-\tfrac14d(x,y)^2,\\
d(y,m')^2&\le\tfrac12d(y,x)^2+\tfrac12d(y,z)^2\\
&\quad-\tfrac14d(x,z)^2 .
\end{aligned}
\]
Since \(d(m',x)=\frac12d(x,z)\), inserting the second inequality into the first leaves \(d(m,m')^2\le\frac14d(y,z)^2\). \(\square\)

**Proposition 2.3** (convexity of the metric). Let \(c,c'\colon[0,1]\to X\) be geodesic segments parametrized proportionally to arc length (constant maps allowed). Then \(t\mapsto d(c(t),c'(t))\) is convex.

*Proof.* The function \(\phi(t)=d(c(t),c'(t))\) is continuous. Let \(t_1<t_2\) and \(t=\frac12(t_1+t_2)\). The points \(c(t)\) and \(c'(t)\) are the midpoints of \([c(t_1),c(t_2)]\) and \([c'(t_1),c'(t_2)]\). Let \(\mu\) be the midpoint of \([c(t_1),c'(t_2)]\). Lemma 2.2, applied from the point \(c(t_1)\) and from the point \(c'(t_2)\), gives
\[
\begin{aligned}
d(c(t),\mu)&\le\tfrac12d(c(t_2),c'(t_2)),\\
d(\mu,c'(t))&\le\tfrac12d(c(t_1),c'(t_1)),
\end{aligned}
\]
so \(\phi(t)\le\frac12\phi(t_1)+\frac12\phi(t_2)\). A continuous function with this midpoint property is convex: by induction on \(n\) it satisfies \(\phi(t_\lambda)\le(1-\lambda)\phi(t_1)+\lambda\phi(t_2)\), where \(t_\lambda=(1-\lambda)t_1+\lambda t_2\), for \(\lambda=k/2^n\), \(0\le k\le2^n\) (write \(\lambda\) as the midpoint of two neighbouring fractions with denominator \(2^{n-1}\)), and dyadic \(\lambda\) are dense. \(\square\)

**Lemma 2.4** (four points). For all \(x_1,x_2,x_3,x_4\in X\), with \(d_{ij}=d(x_i,x_j)\),
\[
\begin{aligned}
&d_{13}^2+d_{24}^2\\
&\quad\le d_{12}^2+d_{23}^2+d_{34}^2+d_{41}^2 .
\end{aligned} \tag{2.1}
\]

*Proof.* Let \(m\) be the midpoint of \([x_1,x_3]\). By (1.1) with \(t=\frac12\), applied to the points \(x_2\) and \(x_4\),
\[
\begin{aligned}
&d(x_2,m)^2+d(x_4,m)^2\\
&\quad\le\tfrac12\bigl(d_{12}^2+d_{23}^2+d_{34}^2+d_{41}^2\bigr)-\tfrac12d_{13}^2 .
\end{aligned}
\]
Since \(d_{24}^2\le(d(x_2,m)+d(m,x_4))^2\), which is at most \(2d(x_2,m)^2+2d(m,x_4)^2\), (2.1) follows. \(\square\)

## 3. Projections onto convex sets

A subset \(C\subseteq X\) is *convex* if \([y,z]\subseteq C\) for all \(y,z\in C\). For \(x\in X\) put \(d(x,C)=\inf_{p\in C}d(x,p)\).

**Proposition 3.1** (nearest points). Let \(C\subseteq X\) be nonempty, convex and complete for the restricted metric.

1. Every \(x\in X\) has exactly one point \(\pi_C(x)\in C\) with \(d(x,\pi_C(x))=d(x,C)\).
2. For every \(p\in C\), \(d(x,p)^2\ge d(x,a)^2+d(a,p)^2\), where \(a=\pi_C(x)\).
3. \(d(\pi_C(x),\pi_C(y))\le d(x,y)\) for all \(x,y\).
4. If \(y\in[x,\pi_C(x)]\), then \(\pi_C(y)=\pi_C(x)\).
5. If \(g\) is an isometry of \(X\) with \(g(C)=C\), then \(\pi_C(gx)=g\,\pi_C(x)\).

*Proof.* (1) Let \(D=d(x,C)\) and \(p_n\in C\) with \(d(x,p_n)\to D\). The midpoint \(m\) of \([p_n,p_k]\) lies in \(C\), so (1.1) gives
\[
\begin{aligned}
&D^2\le d(x,m)^2\le\tfrac12d(x,p_n)^2\\
&\quad+\tfrac12d(x,p_k)^2-\tfrac14d(p_n,p_k)^2 .
\end{aligned}
\]
Hence \(d(p_n,p_k)^2\) is at most \(2d(x,p_n)^2+2d(x,p_k)^2-4D^2\), which tends to \(0\); the sequence is Cauchy, and its limit in \(C\) has distance \(D\) from \(x\). The same inequality applied to two points at distance \(D\) shows that they coincide.

(2) Let \(a=\pi_C(x)\) and \(p\in C\). The point \(q_t\) at fraction \(t\) of \([a,p]\) lies in \(C\), so \(d(x,q_t)\ge d(x,a)\), and (1.1) gives
\[
\begin{aligned}
&d(x,a)^2\le(1-t)d(x,a)^2\\
&\quad+t\,d(x,p)^2-t(1-t)d(a,p)^2 .
\end{aligned}
\]
For \(0<t\le1\), dividing by \(t\) gives \(d(x,a)^2+(1-t)d(a,p)^2\le d(x,p)^2\); let \(t\to0\).

(3) Put \(a=\pi_C(x)\), \(b=\pi_C(y)\). By (2), \(d(x,b)^2\ge d(x,a)^2+d(a,b)^2\) and \(d(y,a)^2\ge d(y,b)^2+d(a,b)^2\). Lemma 2.4 for the points \(x,a,b,y\) gives
\[
\begin{aligned}
&d(x,b)^2+d(a,y)^2\\
&\quad\le d(x,a)^2+d(a,b)^2\\
&\qquad+d(b,y)^2+d(y,x)^2 .
\end{aligned}
\]
Combining, \(d(a,b)^2\le d(x,y)^2\).

(4) Let \(a=\pi_C(x)\) and \(D=d(x,a)\). Then \(d(y,a)=D-d(x,y)\), while every \(p\in C\) has \(d(y,p)\ge d(x,p)-d(x,y)\ge D-d(x,y)\). So \(a\) is a nearest point of \(C\) to \(y\), and it is the only one.

(5) \(g\) maps \(C\) onto \(C\) and preserves distances, so it maps the nearest point of \(x\) to the nearest point of \(gx\). \(\square\)

**Lemma 3.2.** Let \(C\) be as in Proposition 3.1 and \(c\colon[0,1]\to X\) a geodesic segment parametrized proportionally to arc length. Then \(t\mapsto d(c(t),C)\) is convex.

*Proof.* Let \(t_1<t_2\), \(0\le\lambda\le1\), \(t_\lambda=(1-\lambda)t_1+\lambda t_2\), and let \(\sigma\colon[0,1]\to C\) be the segment from \(\pi_C(c(t_1))\) to \(\pi_C(c(t_2))\), parametrized proportionally to arc length; it lies in \(C\) by convexity. Proposition 2.3, applied to \(\sigma\) and to \(\lambda\mapsto c(t_\lambda)\), gives
\[
\begin{aligned}
d(c(t_\lambda),C)&\le d\bigl(c(t_\lambda),\sigma(\lambda)\bigr)\\
&\le(1-\lambda)\,d(c(t_1),C)\\
&\quad+\lambda\,d(c(t_2),C).\qquad\square
\end{aligned}
\]

**Lemma 3.3.** A bounded convex function \(\phi\colon\mathbb R\to\mathbb R\) is constant.

*Proof.* If \(\phi(a)<\phi(b)\) for some \(a<b\), convexity gives \(\phi(s)\ge\phi(b)+(s-b)\frac{\phi(b)-\phi(a)}{b-a}\) for \(s>b\), which is unbounded; if \(\phi(a)>\phi(b)\), the same holds for \(s<a\). \(\square\)

## 4. Parallel lines and Busemann functions

The image of a geodesic line \(c\) is convex, by uniqueness of segments, and complete, being isometric to \(\mathbb R\). So Proposition 3.1 applies to \(C=c(\mathbb R)\); we write \(\pi_c\) for the projection.

Two geodesic lines \(c,c'\) are *parallel* if \(d(c(s),c'(s))\) is bounded on \(\mathbb R\). This is an equivalence relation, by the triangle inequality. It depends on the direction of the parametrizations, and it is not changed by a shift of parameter \(s\mapsto c'(s+r)\).

**Proposition 4.1** (the Pythagorean identity for parallel lines). Let \(c,c'\) be parallel geodesic lines. There are unique numbers \(D\ge0\) and \(\sigma\in\mathbb R\) such that for all \(s,u\in\mathbb R\)
\[
\begin{aligned}
&d(c(s),c'(u))^2\\
&\quad=D^2+(s-u+\sigma)^2 .
\end{aligned} \tag{4.1}
\]
Moreover \(\pi_{c'}(c(s))=c'(s+\sigma)\) and \(\pi_c(c'(u))=c(u-\sigma)\).

*Proof.* By Lemma 3.2 the function \(s\mapsto d(c(s),c'(\mathbb R))\) is convex; it is bounded by hypothesis, hence constant by Lemma 3.3, say equal to \(D\). Similarly \(u\mapsto d(c'(u),c(\mathbb R))\) is constant, and both constants equal \(\inf_{s,u}d(c(s),c'(u))\), so the second is also \(D\).

Write \(\pi_{c'}(c(s))=c'(\varphi(s))\) and \(\pi_c(c'(u))=c(\psi(u))\). The point \(c'(\varphi(s))\) has distance \(D\) from \(c(s)\) and distance \(D\) from the line \(c\), so \(c(s)\) is a nearest point of \(c(\mathbb R)\) to it, and \(\psi(\varphi(s))=s\) by uniqueness; likewise \(\varphi(\psi(u))=u\). By Proposition 3.1(3), \(\varphi\) and \(\psi\) are \(1\)-Lipschitz, and they are inverse to each other, so \(|\varphi(s)-\varphi(s')|=|s-s'|\) and \(\varphi(s)=\pm s+\sigma\). The sign is \(+\): if \(\varphi(s)=-s+\sigma\), Proposition 3.1(2) with \(p=c'(s)\) would give \(d(c(s),c'(s))^2\ge D^2+(2s-\sigma)^2\), which is unbounded.

Lower bound: Proposition 3.1(2) with \(x=c(s)\), \(p=c'(u)\) gives \(d(c(s),c'(u))^2\ge D^2+(s+\sigma-u)^2\). Upper bound: apply Lemma 2.4 to \(x_1=c(s)\), \(x_2=c(u-\sigma)\), \(x_3=c'(u)\), \(x_4=c'(s+\sigma)\). Here \(d(x_2,x_3)=d(x_4,x_1)=D\), because \(x_3\) and \(x_4\) are the projections of \(x_2\) and \(x_1\), and \(d(x_1,x_2)=d(x_3,x_4)=|s-u+\sigma|\). So
\[
\begin{aligned}
&d(x_1,x_3)^2+d(x_2,x_4)^2\\
&\quad\le2D^2+2(s-u+\sigma)^2 .
\end{aligned}
\]
By the lower bound, each term on the left is at least \(D^2+(s-u+\sigma)^2\); hence both are equal to it, which is (4.1). For fixed \(s\), the right side of (4.1) is minimal exactly at \(u=s+\sigma\), with minimum \(D^2\); so \(D\) and \(\sigma\) are determined by the two lines. \(\square\)

We call \(\sigma=\sigma(c,c')\) the *shift* of \(c'\) relative to \(c\). From (4.1), \(\sigma(c',c)=-\sigma(c,c')\), \(\sigma(c,c)=0\), and replacing \(c'\) by \(s\mapsto c'(s+r)\) changes the shift to \(\sigma(c,c')-r\). Shift \(0\) means that \(c(s)\) and \(c'(s)\) are nearest points of the two lines for every \(s\).

For a geodesic line \(c\) and \(x\in X\), the function \(s\mapsto d(x,c(s))-s\) is nonincreasing, since \(d(x,c(s+r))\le d(x,c(s))+r\), and bounded below by \(-d(x,c(0))\). The *Busemann function* of \(c\) is
\[
b_c(x)=\lim_{s\to\infty}\bigl(d(x,c(s))-s\bigr).
\]

**Lemma 4.2.** (1) \(|b_c(x)-b_c(y)|\le d(x,y)\), and \(b_c(c(u))=-u\). (2) For an isometry \(g\) of \(X\), \(b_c(gx)=b_{g^{-1}\circ c}(x)\). (3) If \(c'\) is parallel to \(c\), then \(b_c(c'(u))=\sigma(c,c')-u\).

*Proof.* (1) Each function \(x\mapsto d(x,c(s))-s\) is \(1\)-Lipschitz, and \(d(c(u),c(s))-s=-u\) for \(s\ge u\). (2) \(d(gx,c(s))=d(x,g^{-1}c(s))\). (3) By (4.1), \(d(c'(u),c(s))-s\) equals \(\sqrt{D^2+(s-u+\sigma)^2}-s\), which tends to \(\sigma-u\). \(\square\)

**Proposition 4.3** (shifts add). If \(c_1,c_2,c_3\) are pairwise parallel geodesic lines, then
\[
\begin{aligned}
&\sigma(c_1,c_3)\\
&\quad=\sigma(c_1,c_2)+\sigma(c_2,c_3).
\end{aligned} \tag{4.2}
\]

*Proof.* Write \(\sigma_{jk}=\sigma(c_j,c_k)\) and let \(D_{23}\) be the constant of (4.1) for \(c_2,c_3\). By Lemma 4.2, \(b=b_{c_1}\) takes the values \(\sigma_{12}-v\) at \(c_2(v)\) and \(\sigma_{13}-w\) at \(c_3(w)\), and it is \(1\)-Lipschitz, so by (4.1) for \(c_2,c_3\), for all \(v,w\in\mathbb R\),
\[
\begin{aligned}
&|\sigma_{12}-\sigma_{13}+w-v|\\
&\quad\le\sqrt{D_{23}^2+(v-w+\sigma_{23})^2} .
\end{aligned}
\]
With \(x=w-v\), squaring gives
\[
\begin{aligned}
&2x(\sigma_{12}-\sigma_{13}+\sigma_{23})\\
&\quad\le D_{23}^2+\sigma_{23}^2-(\sigma_{12}-\sigma_{13})^2
\end{aligned}
\]
for every real \(x\), which forces \(\sigma_{12}-\sigma_{13}+\sigma_{23}=0\). \(\square\)

**Corollary 4.4.** Let \(c,c'\) be parallel geodesic lines and let \(Y\) be the union of the images of all geodesic lines parallel to \(c\). Then \(b_{c'}-b_c\) is constant on \(Y\), equal to \(-\sigma(c,c')\).

*Proof.* For \(c''\) parallel to \(c\), Lemma 4.2(3) and (4.2) give
\[
\begin{aligned}
&b_{c'}(c''(u))-b_c(c''(u))\\
&\quad=\sigma(c',c'')-\sigma(c,c'')\\
&\quad=-\sigma(c,c') .\qquad\square
\end{aligned}
\]

In a CAT(0) space more is true: two parallel lines bound a flat strip, isometric to a strip in the Euclidean plane, and a free abelian group of rank \(n\) acting by semisimple isometries has a minimal set that splits isometrically as a product with \(\mathbb R^n\) (the flat torus theorem, [Davis, Appendix I.4, Theorem I.4.2]); [OpenAI-NC, Section 2] uses these results. The identity (4.1) and the additivity (4.2) are the parts of this flat geometry that the obstruction needs, and they hold in every CN space.

## 5. Exercises

**5.1.** Show that \(\mathbb R^2\) with the norm \(\|x\|_\infty=\max(|x_1|,|x_2|)\) is a geodesic space that is not a CN space.

**5.2.** Show that closed balls in a CN space are convex, and that for every point \(p\) and every geodesic segment \(c\) from \(y\) to \(z\) the function \(t\mapsto d(p,c_t)^2-t^2d(y,z)^2\) is convex on \([0,1]\).

**5.3.** Let \(c\) be a geodesic line. Show that \(\pi_c\) maps \(b_c^{-1}(\beta)\cap Y\) to the single point \(c(-\beta)\), where \(Y\) is as in Corollary 4.4.

**5.4.** In the hyperbolic plane, let \(c,c'\) be two distinct geodesic lines that are asymptotic as \(s\to+\infty\). Explain which hypothesis of Proposition 4.1 fails and what Lemma 3.2 says about \(s\mapsto d(c(s),c'(\mathbb R))\).

**5.5.** Check (4.1) and (4.2) directly for three parallel lines in \(\mathbb R^3\).

## 6. Solutions

**5.1.** Straight segments are geodesic, so the space is geodesic. The points \(y=(0,0)\), \(z=(2,0)\) are joined by the straight segment and by the broken path through \((1,1)\), both of length \(2\); by Lemma 2.1 this cannot happen in a CN space. Directly, (1.1) fails for \(x=(1,1)\) and the straight segment at \(t=\frac12\): the left side is \(1\), the right side \(\frac12+\frac12-1=0\).

**5.2.** If \(d(p,y),d(p,z)\le r\), then (1.1) gives \(d(p,c_t)^2\le r^2\). For the second claim, apply (1.1) on subsegments: for \(t=(1-\lambda)t_1+\lambda t_2\) and the subsegment from \(c_{t_1}\) to \(c_{t_2}\), of length \(|t_2-t_1|L\), it reads
\[
\begin{aligned}
&d(p,c_t)^2\\
&\quad\le(1-\lambda)d(p,c_{t_1})^2+\lambda d(p,c_{t_2})^2\\
&\qquad-\lambda(1-\lambda)(t_2-t_1)^2L^2 ,
\end{aligned}
\]
and the subtracted quantity \(\lambda(1-\lambda)(t_2-t_1)^2L^2\) equals \((1-\lambda)t_1^2L^2+\lambda t_2^2L^2-t^2L^2\). Subtracting \(t^2L^2\) from both sides gives the convexity inequality for \(t\mapsto d(p,c_t)^2-t^2L^2\).

**5.3.** For \(c''\) parallel to \(c\), the point \(c''(u)\) has \(b_c=\sigma(c,c'')-u\) and projection \(c(u-\sigma(c,c''))\) by Proposition 4.1; if \(b_c=\beta\), this is \(c(-\beta)\).

**5.4.** The distance \(d(c(s),c'(s))\) tends to \(0\) or stays bounded as \(s\to+\infty\) but is unbounded as \(s\to-\infty\), so the lines are not parallel. The function \(s\mapsto d(c(s),c'(\mathbb R))\) is still convex; it is positive, tends to \(0\) at \(+\infty\) and is unbounded at \(-\infty\), so it is strictly decreasing.

**5.5.** For lines \(c_j(s)=p_j+sv\) with a common unit vector \(v\), the nearest point of \(c_k\) to \(c_j(s)\) is \(c_k(u)\) with \(u=s-\langle p_k-p_j,v\rangle\). So (4.1) holds with \(D_{jk}\) the length of the component of \(p_k-p_j\) orthogonal to \(v\) and \(\sigma_{jk}=\langle p_j-p_k,v\rangle\), and \(\sigma_{12}+\sigma_{23}=\langle p_1-p_3,v\rangle=\sigma_{13}\).

## References

- [OpenAI-NC] OpenAI, *A Three-Manifold Without Conjugate Points and Without a Nonpositively Curved Metric*, OpenAI Math Release preprint, 24 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026
- [BT] F. Bruhat and J. Tits, *Groupes réductifs sur un corps local*, Publications Mathématiques de l'IHÉS 41 (1972), 5–251, (3.2.1). https://www.numdam.org/item/PMIHES_1972__41__5_0/
- [Davis] M. W. Davis, *The Geometry and Topology of Coxeter Groups*, first edition, Princeton University Press, 2008, Appendix I.2 and I.4. https://people.math.osu.edu/davis.12/davisbook.pdf
