# Projection bodies of polytopes

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(K\subseteq\mathbb R^d\), \(d\ge2\), be a *convex body*: a compact convex set with nonempty interior. For a unit vector \(u\), project \(K\) orthogonally onto the hyperplane \(u^\perp\) and measure the \((d-1)\)-dimensional volume of the shadow. This function of \(u\) is the support function of a second convex body, the *projection body* \(\Pi K\) (Proposition 3.2). The quantity
\[
R_d(K)=\frac{|\Pi K|}{|K|^{d-1}},
\]
where \(|\cdot|\) is \(d\)-dimensional volume, does not change under invertible affine maps (Proposition 3.1). Its smallest value is the subject of Petty's conjecture; this course is about its largest value. For a simplex,
\[
R_d=c_d=\frac{(d+1)\,d^d}{d!}
\]
([The simplex value](the-simplex-value.md)), and Brannen conjectured in 1996 that simplices maximize \(R_d\) among all convex bodies [FHLX, (1.3)]. The bound \(R_d\le c_d\) holds in dimensions two and three [FHLX, Section 1]; in dimension three it is a theorem of Chen, Feng, Li, Xi and Xu [CFLXX, Theorem 1.2]. Feng, Hu, Liu and Xu showed that it fails in every dimension \(d\ge9\), with polytopes that have at most \(d+2\) facets [FHLX, Theorem 1.3].

## The theorems

This course proves two theorems of OpenAI [OpenAI-PB]. Let \(T_n\) be the standard simplex, the set of \(x\in\mathbb R^n\) with all \(x_i\ge0\) and \(x_1+\dots+x_n\le1\).

**Theorem A** (OpenAI). The product \(K=T_{10}\times T_{10}\subseteq\mathbb R^{20}\) satisfies
\[
\frac{R_{20}(K)}{c_{20}}=\frac{121\binom{20}{10}}{21\cdot2^{20}}=\frac{22\,355\,476}{22\,020\,096}>1 .
\]

**Theorem B** (OpenAI). There are \(\lambda>1\) and \(N\) such that for every \(n\ge N\) some Cartesian product \(K_n\subseteq\mathbb R^n\) of simplices satisfies \(R_n(K_n)\ge\lambda^nc_n\).

So simplices are not maximizers in dimension twenty, and the largest value of \(R_n\) exceeds the simplex value by an exponential factor. The mechanism is that \(R\) is multiplicative on products (Proposition 4.1). [A product of two simplices](a-product-of-two-simplices.md) also shows that no product of simplices beats the simplex below dimension twenty.

**The course.**

1. This lesson: support functions, Cauchy's formula for the projection body of a polytope, affine invariance, convex bodies, and products.
2. [The simplex value](the-simplex-value.md): the projection body of a simplex is a cube plus one segment, and \(R_d(T_d)=c_d\).
3. [A product of two simplices](a-product-of-two-simplices.md): Theorems A and B, and the first dimension in which products of simplices exceed \(c_n\).

**What the course assumes.** Lebesgue measure from the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10), in the text of Fremlin [Fremlin], cited by number: translation invariance (134A), Lebesgue measure on \(\mathbb R^{r+s}\) as a product measure (251N), Fubini's theorem (252B), and the effect of a linear map, \(\mu(T[E])=|\det T|\,\mu(E)\) (263A). Compactness in \(\mathbb R^d\) and the extreme value theorem from the core course [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20) [Lebl, Theorem 7.5.6]. Linear algebra: determinants and orthonormal bases.

## 1. Support functions

For a nonempty compact convex set \(C\subseteq\mathbb R^d\) the *support function* is \(h_C(x)=\max_{y\in C}\langle x,y\rangle\). It satisfies \(h_C(tx)=t\,h_C(x)\) for \(t\ge0\), and for compact convex \(C,D\), a matrix \(M\) and \(t\ge0\),
\[
\begin{gathered}
h_{C+D}=h_C+h_D,\qquad h_{tC}=t\,h_C,\\
h_{MC}(x)=h_C(M^{\mathsf T}x),
\end{gathered}
\]
where \(C+D=\{c+e:c\in C,\ e\in D\}\) is the Minkowski sum. For a vector \(v\), the segment \([-\frac v2,\frac v2]\) has support function \(x\mapsto\frac12|\langle v,x\rangle|\).

**Lemma 1.1.** For nonempty compact convex \(C,D\subseteq\mathbb R^d\), \(C\subseteq D\) if and only if \(h_C\le h_D\). In particular \(C=D\) if and only if \(h_C=h_D\).

*Proof.* If \(C\subseteq D\), then \(h_C\le h_D\) by the definition. Suppose \(x\in C\setminus D\). The distance from \(x\) to the points of \(D\) attains its minimum at some \(y\in D\) [Lebl, Theorem 7.5.6]. For \(z\in D\) and \(t\in[0,1]\), \(y+t(z-y)\in D\), so \(t\mapsto|x-y-t(z-y)|^2\) is minimal at \(t=0\) and its derivative there is \(\ge0\): \(\langle x-y,z-y\rangle\le0\). With \(v=x-y\ne0\) this gives
\[
\begin{aligned}
h_D(v)&=\langle v,y\rangle<\langle v,y\rangle+|v|^2\\
&=\langle v,x\rangle\le h_C(v).
\end{aligned}
\] \(\square\)

A *zonotope* is a finite Minkowski sum of segments. The zonotope \(\sum_j[-\frac{v_j}2,\frac{v_j}2]\) has support function \(\frac12\sum_j|\langle v_j,x\rangle|\).

## 2. Polytopes and Cauchy's formula

A *polytope* in this course is a set
\[
P=\{x\in\mathbb R^d:\langle a_j,x\rangle\le b_j,\ 1\le j\le k\}
\]
that is bounded and has nonempty interior, where the \(a_j\) are unit vectors and no inequality can be omitted without changing \(P\). The sets \(F_j=P\cap H_j\), with \(H_j=\{\langle a_j,x\rangle=b_j\}\), are its *facets*, and \(a_j\) is the outward unit normal of \(F_j\).

Volume on an affine hyperplane \(H\) is defined through an isometry \(\iota(z)=x_0+\sum_iz_iv_i\) from \(\mathbb R^{d-1}\) onto \(H\), with \(v_1,\dots,v_{d-1}\) orthonormal: \(\operatorname{vol}_{d-1}(E)=\mu_{d-1}(\iota^{-1}[E])\). Two such isometries differ by a translation and an orthogonal map of \(\mathbb R^{d-1}\), so the value does not depend on the choice [Fremlin, 134A and 263A]. Write \(s_j=\operatorname{vol}_{d-1}(F_j)\).

**Lemma 2.1** (facets). Every facet \(F_j\) contains a point at which all other inequalities are strict; so \(F_j\) contains a relatively open subset of \(H_j\) and \(s_j>0\). A point of \(P\) at which all inequalities are strict is an interior point, and the boundary of \(P\) is the union of the facets. The hyperplanes \(H_j\) are distinct.

*Proof.* Since inequality \(j\) cannot be omitted, some \(z\) satisfies all other inequalities and \(\langle a_j,z\rangle>b_j\). Let \(p\) be an interior point of \(P\), where every inequality is strict. On the segment from \(p\) to \(z\) the function \(\langle a_j,\cdot\rangle\) takes the value \(b_j\) at some \(q\ne z\), and at \(q\), a convex combination of \(p\) and \(z\) with positive weight on \(p\), the other inequalities are strict. By continuity a neighbourhood of \(q\) in \(H_j\) lies in \(F_j\). The second statement holds because each strict inequality persists in a neighbourhood, and a point with \(\langle a_j,x\rangle=b_j\) is a limit of points \(x+ta_j\notin P\). If \(H_i=H_j\) with \(i\ne j\), then either \(a_i=a_j\) and \(b_i=b_j\), so one inequality could be omitted, or \(a_i=-a_j\), \(b_i=-b_j\), and \(P\) would lie in \(H_j\). \(\square\)

For a unit vector \(u\) let \(\pi_u\) be the orthogonal projection onto \(u^\perp\), and use on \(u^\perp\) the volume just defined.

**Lemma 2.2** (projection of a facet). \(\operatorname{vol}_{d-1}(\pi_u[F_j])=s_j\,|\langle a_j,u\rangle|\).

*Proof.* Let \(v_1,\dots,v_{d-1}\) be an orthonormal basis of the directions of \(H_j\), and \(w_1,\dots,w_{d-1}\) one of \(u^\perp\). In these coordinates \(\pi_u\) restricted to \(H_j\) is an affine map \(z\mapsto Mz+c\) of \(\mathbb R^{d-1}\) with \(M_{ik}=\langle v_k,w_i\rangle\), so \(\operatorname{vol}_{d-1}(\pi_u[F_j])=|\det M|\,s_j\) [Fremlin, 263A and 134A]. In the orthonormal basis \(w_1,\dots,w_{d-1},u\) of \(\mathbb R^d\) the vectors \(v_1,\dots,v_{d-1},u\) have the coordinate matrix with blocks \(M\) and \(0\) above, and \(\langle v_k,u\rangle\) and \(1\) below, so \(|\det(v_1,\dots,v_{d-1},u)|=|\det M|\). Writing \(u=\langle u,a_j\rangle a_j+t\) with \(t\) in the span of the \(v_k\) gives
\[
\begin{aligned}
&|\det(v_1,\dots,v_{d-1},u)|\\
&\quad=|\langle u,a_j\rangle|\,|\det(v_1,\dots,v_{d-1},a_j)|\\
&\quad=|\langle u,a_j\rangle| .
\end{aligned}
\] \(\square\)

**Proposition 2.3** (Cauchy's formula for polytopes). For every unit vector \(u\),
\[
\operatorname{vol}_{d-1}(\pi_u[P])=\frac12\sum_{j=1}^ks_j\,|\langle a_j,u\rangle| .
\]
Consequently the zonotope
\[
\Pi P=\sum_{j=1}^k\Bigl[-\frac{s_ja_j}2,\frac{s_ja_j}2\Bigr]
\]
has support function \(h_{\Pi P}(u)=\operatorname{vol}_{d-1}(\pi_u[P])\) for unit \(u\). It is the *projection body* of \(P\).

*Proof.* Let \(\mathcal N\subseteq u^\perp\) be the union of the sets \(\pi_u[F_i\cap F_j]\), \(i\ne j\), and \(\pi_u[F_j]\) for the \(j\) with \(\langle a_j,u\rangle=0\). Each of these lies in the projection of an affine subspace of dimension at most \(d-2\) (\(H_i\cap H_j\), or \(H_j\) when it contains the direction \(u\)), so in an affine subspace of \(u^\perp\) of dimension at most \(d-2\). Such a subspace is a countable union of images of cubes under a singular affine map of \(\mathbb R^{d-1}\), hence null [Fremlin, 263A], and so is \(\mathcal N\).

Fix \(y\in\pi_u[P]\setminus\mathcal N\), and let \(\ell=\{y+tu:t\in\mathbb R\}\), so that \(\ell\cap P\) is a nonempty segment \([p,q]\). Every facet \(F_j\) with \(y\in\pi_u[F_j]\) meets \(\ell\) in a boundary point of \(P\). We show that \(\ell\) meets the boundary exactly in \(p\) and \(q\), that \(p\ne q\), and that \(p\) and \(q\) lie in exactly one facet each, and in different ones. A boundary point \(c\in\ell\) lies in some facet \(F_j\) (Lemma 2.1), in only one because \(y\notin\mathcal N\), and \(\langle a_j,u\rangle\ne0\). Along \(\ell\) the function \(\langle a_j,\cdot\rangle\) is strictly monotone and equals \(b_j\) at \(c\); as it is \(\le b_j\) on \([p,q]\), \(c\) is an endpoint of \([p,q]\). If \(p=q\), then \(p\) is a boundary point, the inequalities other than \(j\) are strict near \(p\), and moving from \(p\) along \(\ell\) in the direction where \(\langle a_j,\cdot\rangle\) decreases stays in \(P\), a contradiction. Finally, if \(p\) and \(q\) lay in the same facet \(F_j\), then \(\langle a_j,p\rangle=\langle a_j,q\rangle\) would force \(\langle a_j,u\rangle=0\).

Hence \(\sum_j\mathbf 1_{\pi_u[F_j]}=2\cdot\mathbf 1_{\pi_u[P]}\) outside \(\mathcal N\); both sides vanish off \(\pi_u[P]\). The sets are compact, hence measurable, and integrating over \(u^\perp\) with Lemma 2.2 gives the formula. The last statement is the formula for the support function of a zonotope. \(\square\)

## 3. Affine invariance and convex bodies

For a polytope put \(R_d(P)=|\Pi P|/|P|^{d-1}\).

**Proposition 3.1** (OpenAI; affine covariance). Let \(P\) be a polytope, \(L\) an invertible \(d\times d\) matrix and \(x_0\in\mathbb R^d\). Then \(LP+x_0\) is a polytope,
\[
\Pi(LP+x_0)=|\det L|\,L^{-\mathsf T}\,\Pi P,
\]
and \(R_d(LP+x_0)=R_d(P)\).

*Proof.* \(LP+x_0\) is described by the inequalities \(\langle L^{-\mathsf T}a_j,y\rangle\le b_j+\langle L^{-\mathsf T}a_j,x_0\rangle\), none of which can be omitted. Its facets are \(LF_j+x_0\), with outward unit normals \(a'_j=L^{-\mathsf T}a_j/|L^{-\mathsf T}a_j|\).

*Facet areas.* The prism \(F_j+[0,a_j]\) has volume \(s_j\): in orthonormal coordinates with last basis vector \(a_j\) it is a translate of a product of a set of measure \(s_j\) and an interval of length \(1\) [Fremlin, 251N, 263A, 134A]. Its image \(LF_j+x_0+[0,La_j]\) has volume \(|\det L|s_j\) [Fremlin, 263A]. A prism \(G+[0,v]\) over a set \(G\) in a hyperplane with unit normal \(n\) has volume \(\operatorname{vol}_{d-1}(G)\,|\langle v,n\rangle|\): the shear \(x\mapsto x-\langle x,n\rangle\,(v-\langle v,n\rangle n)/\langle v,n\rangle\), of determinant \(1\), carries it onto a prism over \(G\) with the perpendicular edge \(\langle v,n\rangle n\). Here \(\langle La_j,a'_j\rangle=1/|L^{-\mathsf T}a_j|\), so the area of \(LF_j+x_0\) is \(s'_j=|\det L|\,|L^{-\mathsf T}a_j|\,s_j\), and
\[
s'_ja'_j=|\det L|\,L^{-\mathsf T}(s_ja_j).
\]
By Proposition 2.3, \(\Pi(LP+x_0)\) is the Minkowski sum of the images of the segments of \(\Pi P\) under \(|\det L|L^{-\mathsf T}\), which is the image of \(\Pi P\). Volumes: \(|\Pi(LP+x_0)|=|\det L|^d|\det L|^{-1}|\Pi P|\) and \(|LP+x_0|^{d-1}=|\det L|^{d-1}|P|^{d-1}\). \(\square\)

**Proposition 3.2** (OpenAI; convex bodies). For every convex body \(K\subseteq\mathbb R^d\) there is a unique convex body \(\Pi K\) with \(h_{\Pi K}(u)=\operatorname{vol}_{d-1}(\pi_u[K])\) for all unit vectors \(u\). There are polytopes \(P_m\supseteq K\) with \(R_d(P_m)\to R_d(K)=|\Pi K|/|K|^{d-1}\). For polytopes \(\Pi K\) is the body of Proposition 2.3, and \(R_d(LK+x_0)=R_d(K)\) for invertible \(L\) and all \(x_0\).

*Proof.* Uniqueness is Lemma 1.1. Translate so that \(aB\subseteq K\subseteq RB\) with \(0<a<R\), \(B\) the closed unit ball, and write \(F(u)=\operatorname{vol}_{d-1}(\pi_u[K])\) for unit \(u\).

*Circumscribed polytopes.* For a finite set \(\mathcal U\) of unit vectors such that every unit vector lies within \(\delta<\frac12\) of \(\mathcal U\), let \(P_{\mathcal U}\) be the set of \(x\) with \(\langle u,x\rangle\le h_K(u)\) for all \(u\in\mathcal U\); it contains \(K\). For \(x\in P_{\mathcal U}\) and a unit vector \(v\), choose \(u\in\mathcal U\) with \(|u-v|\le\delta\); as \(h_K\) is \(R\)-Lipschitz on unit vectors,
\[
\begin{aligned}
\langle v,x\rangle&\le h_K(u)+\delta|x|\\
&\le h_K(v)+\delta R+\delta|x| .
\end{aligned}
\]
With \(v=x/|x|\) this gives \(|x|\le R(1+\delta)/(1-\delta)\le3R\), and then \(\langle v,x\rangle\le h_K(v)+4\delta R\) for all \(v\). By Lemma 1.1, \(P_{\mathcal U}\subseteq K+4\delta RB\subseteq\lambda K\) with \(\lambda=1+4\delta R/a\), because \(K+tB\subseteq K+\frac taK=(1+\frac ta)K\). So \(P_{\mathcal U}\) is bounded with nonempty interior; omitting superfluous inequalities one at a time makes it a polytope in the sense of Section 2. Choose increasing sets \(\mathcal U_m\) with \(\delta_m\to0\), and let \(P_m=P_{\mathcal U_m}\), \(\lambda_m=1+4\delta_mR/a\); then \(P_{m+1}\subseteq P_m\) and \(K\subseteq P_m\subseteq\lambda_mK\).

*The limit body.* Projection preserves these inclusions, so for unit \(u\), \(F(u)\le h_{\Pi P_m}(u)\le\lambda_m^{d-1}F(u)\), and \(h_{\Pi P_m}\) decreases in \(m\). By Lemma 1.1 the zonotopes \(\Pi P_m\) decrease. Let \(\Pi K=\bigcap_m\Pi P_m\), a compact convex set. For each \(u\), points \(x_m\in\Pi P_m\) with \(\langle u,x_m\rangle=h_{\Pi P_m}(u)\) have a limit point in every \(\Pi P_m\), hence in \(\Pi K\); so \(h_{\Pi K}(u)=\lim_mh_{\Pi P_m}(u)=F(u)\). Since \(F(u)\ge\operatorname{vol}_{d-1}(\pi_u[aB])=:r>0\), \(\Pi K\) contains the ball \(rB\) by Lemma 1.1, and it is a convex body.

*Volumes.* \(|K|\le|P_m|\le\lambda_m^d|K|\), and \(\Pi K\subseteq\Pi P_m\subseteq\lambda_m^{d-1}\Pi K\) by Lemma 1.1, so \(|\Pi K|\le|\Pi P_m|\le\lambda_m^{d(d-1)}|\Pi K|\). Hence \(R_d(P_m)\to R_d(K)\). If \(K\) is a polytope, Proposition 2.3 and uniqueness show that the two definitions agree.

*Invariance.* The polytopes \(LP_m+x_0\) satisfy \(LK+x_0\subseteq LP_m+x_0\subseteq\lambda_m(LK)+x_0\), and the argument above, centred at \(x_0\), gives \(R_d(LP_m+x_0)\to R_d(LK+x_0)\). By Proposition 3.1, \(R_d(LP_m+x_0)=R_d(P_m)\to R_d(K)\). \(\square\)

In particular \(\sup_KR_d(K)\) over convex bodies equals the supremum over polytopes, and Brannen's question asks whether it equals \(c_d\).

## 4. Products

**Proposition 4.1** (OpenAI; products). Let \(A\subseteq\mathbb R^r\) and \(B\subseteq\mathbb R^s\) be polytopes, \(r,s\ge2\). In \(\mathbb R^{r+s}=\mathbb R^r\times\mathbb R^s\),
\[
\Pi(A\times B)=(|B|\,\Pi A)\times(|A|\,\Pi B),
\]
and
\[
R_{r+s}(A\times B)=R_r(A)\,R_s(B).
\]

*Proof.* If \(A=\{\langle a_i,x\rangle\le\alpha_i\}\) and \(B=\{\langle b_j,y\rangle\le\beta_j\}\), then \(A\times B\) is described by both families of inequalities, none of which can be omitted. Its facets are \(F_i\times B\), with unit normal \((a_i,0)\) and area \(s_i|B|\), and \(A\times G_j\), with unit normal \((0,b_j)\) and area \(|A|t_j\), where \(s_i,t_j\) are the facet areas of \(A\) and \(B\) [Fremlin, 251N]. By Proposition 2.3,
\[
\begin{aligned}
&h_{\Pi(A\times B)}(u,v)\\
&\quad=|B|\,h_{\Pi A}(u)+|A|\,h_{\Pi B}(v)\\
&\quad=h_{(|B|\Pi A)\times(|A|\Pi B)}(u,v),
\end{aligned}
\]
since the support function of a product \(C\times D\) is \(h_C(u)+h_D(v)\). Lemma 1.1 gives the first identity. Then \(|\Pi(A\times B)|=|B|^r|\Pi A|\,|A|^s|\Pi B|\) and \(|A\times B|^{r+s-1}=|A|^{r+s-1}|B|^{r+s-1}\), whose quotient is \(R_r(A)R_s(B)\). \(\square\)

## 5. Exercises

**5.1** (easy). Show that the cube \(Q=[0,1]^d\) has \(\Pi Q=[-1,1]^d\) and \(R_d(Q)=2^d\).

**5.2** (medium). For a polytope, show that \(\sum_js_ja_j=0\). (Hint: in the proof of Proposition 2.3, one of the two facets over \(y\) has \(\langle a_j,u\rangle>0\) and the other \(\langle a_j,u\rangle<0\).)

**5.3** (medium). Let \(d=2\) and let \(J\) be the rotation by a right angle. Show that \(\Pi P=J(P+(-P))\) for every polygon \(P\), so that \(R_2(P)=|P-P|/|P|\).

## 6. Solutions

**5.1.** The facets are \(\{x_i=0\}\cap Q\) and \(\{x_i=1\}\cap Q\), with normals \(\mp e_i\) and area \(1\). Proposition 2.3 gives \(\Pi Q=\sum_i2[-\frac{e_i}2,\frac{e_i}2]=[-1,1]^d\), of volume \(2^d\), and \(|Q|=1\).

**5.2.** For \(y\in\pi_u[P]\setminus\mathcal N\) the line \(\ell\) enters \(P\) at \(p\) and leaves it at \(q\) (with \(q-p\) a positive multiple of \(u\)); the facet at \(q\) has \(\langle a_j,u\rangle>0\), since \(\langle a_j,\cdot\rangle\) increases to \(b_j\), and the facet at \(p\) has \(\langle a_j,u\rangle<0\). So the facets with \(\langle a_j,u\rangle>0\) cover \(\pi_u[P]\) once up to a null set, as do those with \(\langle a_j,u\rangle<0\). By Lemma 2.2,
\[
\begin{aligned}
\sum_{\langle a_j,u\rangle>0}s_j\langle a_j,u\rangle&=\operatorname{vol}_{d-1}(\pi_u[P])\\
&=\sum_{\langle a_j,u\rangle<0}s_j|\langle a_j,u\rangle|,
\end{aligned}
\]
so \(\langle\sum_js_ja_j,u\rangle=0\) for every \(u\).

**5.3.** For a unit vector \(u\), \(\pi_u[P]\) is a segment whose length is the width of \(P\) in the direction \(Ju\), namely \(h_P(Ju)+h_P(-Ju)\), which equals \(h_{P+(-P)}(Ju)=h_{J^{\mathsf T}(P+(-P))}(u)\). As \(J^{\mathsf T}=J^{-1}=-J\) and \(P+(-P)\) is symmetric, \(J^{\mathsf T}(P+(-P))=J(P+(-P))\). Lemma 1.1 gives the identity, and \(|J(P-P)|=|P-P|\).

## References

- [OpenAI-PB] OpenAI, *A product counterexample to the simplex maximum for projection-body volume*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026
- [FHLX] Y. Feng, S. Hu, W. Liu and L. Xu, *On the reverse projection inequality*, preprint, 2026, MathSciDoc 2608.23002; Section 1. https://archive.ymsc.tsinghua.edu.cn/pacm_download/743/12781--2026.8.26.pdf
- [CFLXX] S. Chen, Y. Feng, Y. Li, D. Xi and L. Xu, *Petty's conjectured projection inequality in dimension three*, preprint, 2026, MathSciDoc 2608.23001. https://archive.ymsc.tsinghua.edu.cn/pacm_download/741/12780-pettyinequality.pdf
- [Fremlin] D. H. Fremlin, *Measure Theory*, Volumes 1 and 2, 134A, 251N, 252B, 263A; the text of the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10). https://www1.essex.ac.uk/maths/people/fremlin/mt.htm
- [Lebl] J. Lebl, *Basic Analysis I and II*, version 6.3; the text of the core courses [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10) and [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20). https://www.jirka.org/ra/
