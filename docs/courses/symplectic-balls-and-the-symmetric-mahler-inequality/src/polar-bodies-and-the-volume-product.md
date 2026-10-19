# Polar bodies and the volume product

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For an origin-symmetric convex body \(K\subset\mathbf R^n\), the *volume product* \(\operatorname{vol}(K)\operatorname{vol}(K^\circ)\) does not change under invertible linear maps. Mahler conjectured that it is at least \(4^n/n!\), the value for the cube. Iriyeh and Shibata proved this for \(n=3\) [IS]. In every dimension the inequality was known up to a factor \(c^n\) (Bourgain and Milman; see [Ku]), and Kuperberg proved it up to the factor \((\pi/4)^n\gamma_n\), where \(\gamma_1=4/\pi\) and \(\gamma_n\to\sqrt2\) [Ku]. Artstein-Avidan, Karasev and Ostrover computed a symplectic capacity of \(K\times K^\circ\) to be \(4\) and observed that Viterbo's volume–capacity conjecture would therefore give the inequality, because symplectic maps preserve volume [AKO]. Viterbo's conjecture fails for some convex domains [HKO]; a ball of capacity close to \(4\) inside \(K\times K^\circ\) still suffices. OpenAI proved that every ball of capacity less than \(4\) embeds symplectically into \(\operatorname{int}K\times\operatorname{int}K^\circ\) [OpenAI-SB]. This course proves that theorem (Theorem B) and the symmetric Mahler inequality (Theorem A).

## The theorems

A *convex body* is a compact convex subset of \(\mathbf R^n\) with nonempty interior. It is *origin-symmetric* if \(K=-K\). Its *polar* is
\[
K^\circ=\{p\in\mathbf R^n:\langle q,p\rangle\le1\ \forall q\in K\}.
\]

**Theorem A** (symmetric Mahler inequality). For every \(n\ge1\) and every origin-symmetric convex body \(K\subset\mathbf R^n\),
\[
\operatorname{vol}_n(K)\,\operatorname{vol}_n(K^\circ)\ge\frac{4^n}{n!}.
\]
Equality holds for the cube \([-1,1]^n\) (Example 1.7).

Write the points of \(\mathbf R^{2n}=\mathbf R^n_q\times\mathbf R^n_p\) as \((q,p)\), and let \(J\) be the matrix of the standard symplectic form \(\omega_0=\sum_jdq_j\wedge dp_j\), that is, \(\omega_0(X,Y)=X^{\mathsf T}JY\) with
\[
J=\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix}.
\]
A smooth map \(e\) from an open set \(U\subseteq\mathbf R^{2n}\) to \(\mathbf R^{2n}\) is *symplectic* if \(De(z)^{\mathsf T}J\,De(z)=J\) for every \(z\in U\). For \(c>0\), the *ball of capacity* \(c\) is
\[
B^{2n}(c)=\{(q,p):\ \pi(|q|^2+|p|^2)<c\},
\]
the open Euclidean ball of radius \(\sqrt{c/\pi}\); its volume is \(c^n/n!\).

**Theorem B** (OpenAI). Let \(n\ge2\), let \(K\subset\mathbf R^n\) be an origin-symmetric convex body and \(U_K=\operatorname{int}K\times\operatorname{int}K^\circ\). For every \(0<c<4\) there is an injective symplectic map \(B^{2n}(c)\to U_K\), which is a diffeomorphism onto an open subset of \(U_K\).

Theorem B gives Theorem A for \(n\ge2\) because symplectic maps preserve volume (Lemma 2.4); the deduction is in the last lesson. The capacity \(4\) cannot be exceeded: a linear symplectic change of coordinates maps \(U_K\) into \((-1,1)^2\times\mathbf R^{2n-2}\) [AKO, Remark 4.2], and Gromov's nonsqueezing theorem then bounds the capacity of every embedded ball by \(4\). This upper bound is not used in the course and nonsqueezing is not proved here.

## 1. Polar bodies and support functions

The *support function* of a compact set \(C\subset\mathbf R^n\) is \(h_C(p)=\max_{y\in C}\langle p,y\rangle\). Thus \(K^\circ=\{p:h_K(p)\le1\}\). We write \(B(x,r)\) for the open Euclidean ball.

**Lemma 1.1.** Let \(K\) be an origin-symmetric convex body. There are \(0<r\le R\) with \(B(0,r)\subseteq K\subseteq\overline{B(0,R)}\). Then \(B(0,1/R)\subseteq K^\circ\subseteq\overline{B(0,1/r)}\), \(K^\circ\) is an origin-symmetric convex body, and
\[
\operatorname{int}K^\circ=\{p:\ h_K(p)<1\}.
\]

**Proof.** Let \(B(y,r)\subseteq K\). By symmetry \(B(-y,r)\subseteq K\), and by convexity the midpoints \(\frac12(a+b)\) with \(a\in B(y,r)\), \(b\in B(-y,r)\) fill \(B(0,r)\), which therefore lies in \(K\). Boundedness gives \(R\). If \(|p|<1/R\), then \(\langle q,p\rangle\le|q||p|<1\) for \(q\in K\). If \(p\ne0\) lies in \(K^\circ\), the point \(q=tp/|p|\) with \(t<r\) lies in \(K\), so \(t|p|\le1\) for all \(t<r\), and \(|p|\le1/r\). The set \(K^\circ\) is an intersection of closed half-spaces, hence closed and convex, and it is symmetric because \(K\) is.

The support function satisfies \(|h_K(p)-h_K(p')|\le R|p-p'|\), so \(\{h_K<1\}\) is open; it lies in \(K^\circ\) and hence in the interior. If \(h_K(p)=1\), the points \((1+\varepsilon)p\) have \(h_K=1+\varepsilon>1\) and lie outside \(K^\circ\), so \(p\) is not an interior point. \(\square\)

**Lemma 1.2** (separation). Let \(C\subset\mathbf R^n\) be a nonempty compact convex set and \(x\notin C\). There is a vector \(v\) with \(\langle v,x\rangle>h_C(v)\).

**Proof.** Let \(c_0\) be a point of \(C\) nearest to \(x\), and \(v=x-c_0\ne0\). For \(y\in C\) and \(0<s\le1\), the point \(c_0+s(y-c_0)\) lies in \(C\), so \(|v-s(y-c_0)|^2\ge|v|^2\); dividing by \(s\) and letting \(s\to0\) gives \(\langle v,y-c_0\rangle\le0\). Hence \(\langle v,y\rangle\le\langle v,c_0\rangle=\langle v,x\rangle-|v|^2\) for all \(y\in C\). \(\square\)

**Lemma 1.3.** (a) For nonempty compact convex sets \(C\) and \(C'\), \(C\subseteq C'\) if and only if \(h_C\le h_{C'}\).

Let \(C\) and \(C'\) be convex bodies containing \(0\) in their interiors.

(b) \(C^{\circ\circ}=C\).

(c) If \(C\subseteq C'\), then \(C'^\circ\subseteq C^\circ\).

**Proof.** (a) Inclusion gives the inequality of maxima. Conversely, if \(x\in C\setminus C'\), Lemma 1.2 gives \(v\) with \(\langle v,x\rangle>h_{C'}(v)\), while \(\langle v,x\rangle\le h_C(v)\).

(b) If \(x\in C\), then \(\langle x,p\rangle\le1\) for every \(p\in C^\circ\), so \(x\in C^{\circ\circ}\). If \(x\notin C\), Lemma 1.2 gives \(v\) with \(\langle v,x\rangle>h_C(v)\); here \(h_C(v)>0\) because \(C\) contains a ball about \(0\). The vector \(v/h_C(v)\) lies in \(C^\circ\) and pairs with \(x\) to a value greater than \(1\), so \(x\notin C^{\circ\circ}\).

(c) follows from the definition. \(\square\)

**Lemma 1.4** (strip bodies). Let \(b_1,\dots,b_m\in\mathbf R^n\) span \(\mathbf R^n\), let \(P\) be the convex hull of \(\pm b_1,\dots,\pm b_m\), and put
\[
K'=\bigcap_{j=1}^m\{x\in\mathbf R^n:|\langle b_j,x\rangle|\le1\}.
\]
Then \(K'\) is an origin-symmetric convex body, \(K'=P^\circ\) and \((K')^\circ=P\).

**Proof.** A linear functional attains its maximum over \(P\) at one of the points \(\pm b_j\), so \(P^\circ=K'\). Since the \(b_j\) span \(\mathbf R^n\), the linear map \(x\mapsto(\langle b_j,x\rangle)_j\) is injective, so there is \(C_b\) with \(|x|\le C_b\max_j|\langle b_j,x\rangle|\); thus \(K'\) is bounded, and it contains the ball \(B(0,1/\max_j|b_j|)\). It is closed, convex and symmetric. The set \(P\) contains a basis of vectors together with their negatives, hence a neighbourhood of \(0\), so Lemma 1.3(b) gives \((K')^\circ=P^{\circ\circ}=P\). \(\square\)

We call \(K'\) the *strip body* of \(b_1,\dots,b_m\).

**Lemma 1.5** (finite polar approximation). Let \(K\) be an origin-symmetric convex body and \(\alpha>0\). There are vectors \(b_1,\dots,b_m\) spanning \(\mathbf R^n\) whose strip body \(K'\) satisfies
\[
K\subseteq K'\subseteq(1+\alpha)K,\qquad(K')^\circ\subseteq K^\circ.
\]

**Proof.** Put \(\lambda=1+\alpha\). By Lemma 1.1, \(K^\circ\) is an origin-symmetric convex body, so \(\rho=\min_{|v|=1}h_{K^\circ}(v)>0\). Let \(d=\alpha\rho/\lambda\), and choose finitely many points \(b_1,\dots,b_m\in K^\circ\) such that every point of the compact set \(K^\circ\) lies within distance \(d\) of one of them. Let \(P\) be the convex hull of the \(\pm b_j\); then \(P\subseteq K^\circ\). For a unit vector \(v\), a point of \(K^\circ\) where \(\langle v,\cdot\rangle\) is largest lies within \(d\) of some \(b_j\), so
\[
\begin{aligned}
h_P(v)&\ge h_{K^\circ}(v)-d\\
&\ge h_{K^\circ}(v)-\tfrac\alpha\lambda h_{K^\circ}(v)\\
&=\lambda^{-1}h_{K^\circ}(v).
\end{aligned}
\]
Both sides are positively homogeneous, so \(h_P\ge h_{\lambda^{-1}K^\circ}\) everywhere, and Lemma 1.3(a) gives \(\lambda^{-1}K^\circ\subseteq P\subseteq K^\circ\). In particular \(P\) has interior points, so the \(b_j\) span \(\mathbf R^n\). Taking polars (Lemma 1.3(b), (c)), with \((\lambda^{-1}K^\circ)^\circ=\lambda K\), gives \(K\subseteq P^\circ\subseteq\lambda K\), and \(P^\circ=K'\), \((K')^\circ=P\subseteq K^\circ\) by Lemma 1.4. \(\square\)

**Lemma 1.6.** If \(C\) is a convex body with \(B(0,r)\subseteq C\), then \(tC\subseteq\operatorname{int}C\) for \(0<t<1\), and \(\operatorname{vol}(\operatorname{int}C)=\operatorname{vol}(C)\).

**Proof.** For \(x\in C\) and \(|y|<(1-t)r\), the point \(tx+y=tx+(1-t)\frac{y}{1-t}\) lies in \(C\) by convexity; so \(tx\) is an interior point. Hence \(t^n\operatorname{vol}(C)\le\operatorname{vol}(\operatorname{int}C)\le\operatorname{vol}(C)\) for all \(t<1\). \(\square\)

**Example 1.7.** The cube \([-1,1]^n\) has volume \(2^n\). Its polar is the cross-polytope \(\{p:\sum_j|p_j|\le1\}\), whose intersection with each of the \(2^n\) closed coordinate orthants is a simplex of volume \(1/n!\); these simplices overlap only in sets of measure zero. So the volume product of the cube is \(2^n\cdot2^n/n!=4^n/n!\).

## 2. Plan of the course

The proof of Theorem B combines two scales. For a strip body \(K\) and a large integer \(k\), the functions \(f_j(z)=g(\langle b_j,z\rangle)^k\) on a domain in \(\mathbf C^n\), with a fixed conformal map \(g\), vanish to order \(k\) at the origin. Lesson 4 shows that the domain \(\{\sum_j|f_j|^2<1\}\), with the symplectic form of the potential \(|z|^2+\sum_j|f_j|^2\), contains balls of every capacity below \(\pi k\). Lessons 5 and 6 study the conformal map and prove a uniform estimate for integrals along horizontal slices. Lesson 7 maps the domain symplectically into \(\operatorname{int}K\times S\operatorname{int}K^\circ\) with \(S\approx\pi k/4\), rescales, and passes to general \(K\) by Lemma 1.5. Lessons 2 and 3 supply the tools: forms, symplectic maps and Moser's method; and plurisubharmonic potentials.

## 3. Exercises

**1.1** (easy). Show that \(([-1,1]^n)^\circ\) is the cross-polytope, and that the polar of the ellipsoid \(\{x:\sum_jx_j^2/a_j^2\le1\}\) is \(\{p:\sum_ja_j^2p_j^2\le1\}\).

**1.2** (easy). Show that \((AK)^\circ=A^{-\mathsf T}K^\circ\) for an invertible matrix \(A\), and deduce that the volume product is invariant under invertible linear maps.

**1.3** (medium). Compute the volume product of the regular hexagon with vertices at distance \(1\) from the centre, and compare it with \(4^2/2!=8\).

**1.4** (easy). Show that the volume product of the Euclidean unit ball in \(\mathbf R^n\) is \(\kappa_n^2\), with \(\kappa_n=\operatorname{vol}(B(0,1))\), and check \(\kappa_2^2=\pi^2>8\).

## 4. Solutions

**1.1.** \(h_{[-1,1]^n}(p)=\sum_j|p_j|\), so the polar is \(\{\sum_j|p_j|\le1\}\). For the ellipsoid \(E\), the substitution \(x_j=a_jy_j\) gives \(h_E(p)=\max_{|y|\le1}\sum_ja_jp_jy_j\), and this maximum is \((\sum_ja_j^2p_j^2)^{1/2}\).

**1.2.** \(\langle Aq,p\rangle=\langle q,A^{\mathsf T}p\rangle\), so \(p\in(AK)^\circ\) if and only if \(A^{\mathsf T}p\in K^\circ\). The volumes change by the factors \(|\det A|\) and \(|\det A|^{-1}\).

**1.3.** The hexagon \(H\) is the union of six equilateral triangles of side \(1\), of area \(\frac{3\sqrt3}2\). Its polar is the regular hexagon whose sides lie on the lines \(\langle v,p\rangle=1\) for the six vertices \(v\); its inradius is \(1\), its circumradius \(2/\sqrt3\), and its area \(\frac{3\sqrt3}2\cdot\frac43=2\sqrt3\). The product is \(9>8\).

**1.4.** The unit ball is its own polar. \(\kappa_2=\pi\) and \(\pi^2\approx9.87\).

## References

- [OpenAI-SB] OpenAI, *Symplectic balls in symmetric polar products*, OpenAI Math Release preprint, 22 September 2026. https://github.com/openai/math/tree/main/preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026
- [AKO] S. Artstein-Avidan, R. Karasev and Y. Ostrover, *From symplectic measurements to the Mahler conjecture*, Duke Mathematical Journal 163 (2014), 2003–2022; arXiv:1303.4197. https://arxiv.org/abs/1303.4197
- [IS] H. Iriyeh and M. Shibata, *Symmetric Mahler's conjecture for the volume product in the three dimensional case*, Duke Mathematical Journal 169 (2020), 1077–1134; arXiv:1706.01749. https://arxiv.org/abs/1706.01749
- [Ku] G. Kuperberg, *From the Mahler conjecture to Gauss linking integrals*, Geometric and Functional Analysis 18 (2008), 870–892; arXiv:math/0610904. https://arxiv.org/abs/math/0610904
- [HKO] P. Haim-Kislev and Y. Ostrover, *A counterexample to Viterbo's conjecture*, arXiv:2405.16513 (2024). https://arxiv.org/abs/2405.16513
