# Smooth blow-ups and transforms of ideals

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Resolution of singularities in characteristic zero replaces a singular variety by a smooth one through a sequence of blow-ups along smooth centres. The proof in this course works with ideal sheaves on smooth varieties: an ideal is improved by blowing up smooth subvarieties along which it vanishes to the highest order, until its pull-back defines a divisor with simple normal crossings. This first lesson sets up the objects that every later lesson uses: coordinates, the order of vanishing of an ideal and its description by derivatives, blow-ups along smooth centres, simple normal crossing divisors, and the transforms of ideals and marked ideals under a blow-up.

Throughout the course \(k\) is a field of characteristic zero. A *smooth scheme* is a scheme smooth and of finite type over \(k\). Points are scheme-theoretic points; closed points are named as such. A smooth scheme is regular, so its local rings are domains, its irreducible components are disjoint, and each component is an integral smooth scheme.

The prerequisites are commutative algebra and the basic theory of smooth morphisms: [Regular local rings](course:AG-CA/AG-CA-14), [Kähler differentials](course:AG-CA/AG-CA-16), [Smooth algebras over a field and the Jacobian criterion](course:AG-CA/AG-CA-18), [Completion](course:AG-CA/AG-CA-19), [Coefficient rings and the Cohen structure theorem](course:AG-CA/AG-CA-19S) and [Smooth morphisms](course:AG-FSE/AG-FSE-05). Blow-ups are defined in the AI Integrated Stacks Project, Section [01OF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-section-blowing-up).

## 1. Coordinates and derivations

**Definition 1.1.** Let \(X\) be a smooth scheme and \(U\subset X\) open. A *coordinate system* on \(U\) is a tuple \(z=(z_1,\ldots,z_N)\) of regular functions on \(U\) whose differentials \(dz_1,\ldots,dz_N\) form a basis of \(\Omega_{U/k}\). The *coordinate derivations* \(\partial_1,\ldots,\partial_N\) are the dual basis of \(\operatorname{Der}_k(\mathcal O_U)=\operatorname{Hom}(\Omega_{U/k},\mathcal O_U)\): \(\partial_i(z_j)=\delta_{ij}\). A coordinate system is *centred* at a point \(p\) if every \(z_i\) vanishes at \(p\).

Since \(\Omega_{X/k}\) is locally free of rank \(\dim_xX\) at \(x\) ([Stacks, Tag 02G1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-smooth-omega-finite-locally-free)), \(N\) is the local dimension. The map \(z:U\to\mathbf A^N_k\) is étale: its differentials give an isomorphism \(z^*\Omega_{\mathbf A^N}\to\Omega_U\), and this is the inverse-function criterion of [Poincaré duality for smooth varieties, Section 2](course:ag-etale-cohomology/poincare-duality-for-smooth-varieties#2-the-trace-and-its-derived-comparison) (also [Stacks, Tag 02GU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-at-point)). The coordinate derivations commute: \(\partial_i\partial_j-\partial_j\partial_i\) is a derivation vanishing on every \(z_l\), hence vanishing on \(\Omega_U\), hence zero. For a multi-index \(\alpha\in\mathbf N^N\) write \(\partial^\alpha=\partial_1^{\alpha_1}\cdots\partial_N^{\alpha_N}\), \(|\alpha|=\sum\alpha_i\) and \(\alpha!=\prod\alpha_i!\).

**Lemma 1.2 (adapted coordinates).** Let \(X\) be a smooth scheme, \(Y\subset X\) a closed subscheme smooth over \(k\), and \(p\in Y\) a closed point, with \(r=\dim_pX-\dim_pY\). There are an open neighbourhood \(U\) of \(p\) and a coordinate system on \(U\), centred at \(p\), with \(Y\cap U=V(z_1,\ldots,z_r)\).

**Proof.** The local rings \(R=\mathcal O_{X,p}\) and \(R/I=\mathcal O_{Y,p}\) are regular, of dimensions \(N=\dim_pX\) and \(N-r\). By [Regular local rings](course:AG-CA/AG-CA-14), Proposition 1.4, there is a regular system of parameters \(t_1,\ldots,t_N\) of \(R\) with \(I=(t_1,\ldots,t_r)\). The second fundamental exact sequence ([Kähler differentials](course:AG-CA/AG-CA-16), Theorem 3.3, applied to \(R\to\kappa(p)=R/\mathfrak m\)) gives an exact sequence \(\mathfrak m/\mathfrak m^2\to\Omega_{X/k}\otimes\kappa(p)\to\Omega_{\kappa(p)/k}\to0\). The residue field is finite and separable over \(k\), since \(k\) has characteristic zero, so \(\Omega_{\kappa(p)/k}=0\) ([Kähler differentials](course:AG-CA/AG-CA-16), Theorem 6.2). Both outer spaces have dimension \(N\), so \(dt_1,\ldots,dt_N\) form a basis of \(\Omega_{X/k}\otimes\kappa(p)\). Represent the \(t_i\) by functions on an open \(U\ni p\). By Nakayama's lemma their differentials form a basis of \(\Omega_U\) after shrinking \(U\). The ideal sheaves of \(Y\cap U\) and of \(V(t_1,\ldots,t_r)\) are coherent and have the same stalk at \(p\), so they agree after shrinking \(U\). \(\square\)

Every point \(x\) of \(Y\) has a closed point \(p\) of \(Y\) in its closure, and every open neighbourhood of \(p\) contains \(x\). So Lemma 1.2 provides coordinates adapted to \(Y\) near every point of \(Y\), centred at a closed point of \(Y\). The proof also shows that coordinates centred at a closed point \(p\) generate \(\mathfrak m_p\): their images form a basis of \(\mathfrak m_p/\mathfrak m_p^2\cong\Omega_{X/k}\otimes\kappa(p)\).

**Lemma 1.3 (a smooth subscheme inside a smooth hypersurface).** Let \(H\subset X\) be a smooth hypersurface, \(Y\subset H\) a smooth closed subscheme and \(p\in Y\) a closed point. There are coordinates near \(p\), centred at \(p\), with \(H=V(z_1)\) and \(Y=V(z_1,\ldots,z_r)\).

**Proof.** By Lemma 1.2 applied in \(H\), choose coordinates \(w_1,\ldots,w_{N-1}\) on a neighbourhood of \(p\) in \(H\), centred at \(p\), with \(Y=V(w_1,\ldots,w_{r-1})\). Lift them to functions \(z_2,\ldots,z_N\) near \(p\) in \(X\) vanishing at \(p\), and let \(z_1\) be a local equation of \(H\). The conormal sequence \(0\to\mathcal I_H/\mathcal I_H^2\to\Omega_X|_H\to\Omega_H\to0\) is exact, with \(\mathcal I_H/\mathcal I_H^2\) free on the class of \(z_1\) ([Kähler differentials](course:AG-CA/AG-CA-16), Theorem 3.3 and Proposition 5.2; injectivity holds because both outer terms are locally free of the ranks \(1\) and \(N-1\) and \(\Omega_X|_H\) has rank \(N\)). So \(dz_1,\ldots,dz_N\) form a basis of \(\Omega_X\otimes\kappa(p)\), hence of \(\Omega_X\) near \(p\). Near \(p\), \(Y=V(z_1,z_2,\ldots,z_r)\). \(\square\)

## 2. Order of vanishing and derivative ideals

**Definition 2.1.** Let \(X\) be a smooth scheme, \(\mathcal I\subset\mathcal O_X\) an ideal sheaf and \(x\in X\). The *order* of \(\mathcal I\) at \(x\) is

\[
\operatorname{ord}_x\mathcal I=\max\{r\ge0:\ \mathcal I_x\subset\mathfrak m_x^r\},
\]

with \(\operatorname{ord}_x\mathcal I=\infty\) when \(\mathcal I_x=0\). For a function \(f\), \(\operatorname{ord}_xf=\operatorname{ord}_x(f)\). For an irreducible closed subset \(Z\) with generic point \(\eta\), \(\operatorname{ord}_Z\mathcal I=\operatorname{ord}_\eta\mathcal I\). For a closed subset \(Z\) with several irreducible components we write \(\operatorname{ord}_Z\mathcal I\ge m\), or \(=m\), when this holds at every generic point of \(Z\). The *maximal order* is \(\operatorname{maxord}\mathcal I=\sup_x\operatorname{ord}_x\mathcal I\).

By Krull's intersection theorem ([Stacks, Tag 00IQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-intersection-powers-ideal-module)), \(\operatorname{ord}_xf<\infty\) for \(f\ne0\) in the domain \(\mathcal O_{X,x}\).

**Lemma 2.2.** Every \(k\)-derivation \(\delta\) of \(\mathcal O_{X,x}\) maps \(\mathfrak m_x^r\) into \(\mathfrak m_x^{r-1}\) for \(r\ge1\).

**Proof.** A product of \(r\) elements of \(\mathfrak m_x\) is mapped by the Leibniz rule to a sum of products of \(r-1\) elements of \(\mathfrak m_x\) with one other factor. \(\square\)

**Proposition 2.3 (Taylor criterion).** Let \(z\) be a coordinate system on an open set containing \(x\), with derivations \(\partial_i\). For \(f\in\mathcal O_{X,x}\),

\[
\operatorname{ord}_xf=\min\{|\alpha|:\ \partial^\alpha f\notin\mathfrak m_x\}.
\]

If the coordinates are centred at a closed point \(p\) of the closure \(W\) of \(x\) and \(W=V(z_1,\ldots,z_c)\) near \(p\), the minimum is attained by some \(\alpha\) supported in \(\{1,\ldots,c\}\).

**Proof.** If \(\operatorname{ord}_xf\ge r\) then \(\partial^\alpha f\in\mathfrak m_x\) for \(|\alpha|<r\), by Lemma 2.2. Conversely suppose \(\operatorname{ord}_xf=d<\infty\). We find \(\alpha\) with \(|\alpha|=d\) and \(\partial^\alpha f\notin\mathfrak m_x\).

*A closed point with centred coordinates.* Assume first that \(x\) is closed and \(z\) is centred at \(x\); this is the case \(c=N\) below. Write \(K\) for the residue field and \(\widehat R\) for the completion of \(R=\mathcal O_{X,x}\). The \(z_i\) generate \(\mathfrak m\) (remark after Lemma 1.2). By [Completion](course:AG-CA/AG-CA-19), Theorem 4.1, \(\widehat R\) is a regular local ring of dimension \(N\) with maximal ideal \((z_1,\ldots,z_N)\widehat R\), and by [Coefficient rings and the Cohen structure theorem](course:AG-CA/AG-CA-19S), Theorem 5.1, it has coefficient fields. We use one containing \(k\): the field \(K\) is generated over \(k\) by one element with separable minimal polynomial \(g\), and Hensel's lemma ([Completion](course:AG-CA/AG-CA-19), Theorem 5.1) gives a root \(a\) of \(g\) in \(\widehat R\) lifting the generator; then the field \(k(a)\subset\widehat R\) maps isomorphically onto \(K\). The continuous homomorphism \(k(a)[[X_1,\ldots,X_N]]\to\widehat R\), \(X_i\mapsto z_i\), is surjective, by successive approximation using \(\widehat R=k(a)+\mathfrak m\widehat R\) and \(\mathfrak m\widehat R=(z)\). It is injective, because a proper quotient of the \(N\)-dimensional domain \(k(a)[[X]]\) has dimension \(<N\). So \(\widehat R=k(a)[[z_1,\ldots,z_N]]\) (compare [Coefficient rings and the Cohen structure theorem](course:AG-CA/AG-CA-19S), Corollary 6.2). Each \(\partial_i\) extends continuously to \(\widehat R\) by Lemma 2.2. It vanishes on \(k(a)\), because \(0=\partial_i(g(a))=g'(a)\partial_i(a)\) with \(g'(a)\) a unit. A continuous \(k(a)\)-linear derivation of \(k(a)[[z]]\) is determined by its values on the \(z_j\), so \(\partial_i\) is the formal partial derivative. Write \(f=\sum_\beta c_\beta z^\beta\). Since \(\operatorname{ord}f=d\), some \(c_\beta\ne0\) with \(|\beta|=d\), and \(\partial^\beta f\) has constant term \(\beta!\,c_\beta\ne0\), using characteristic zero. So \(\partial^\beta f\) is a unit of \(\widehat R\), hence of \(R\).

*General points.* Let \(W\) be the closure of \(x\), with its reduced structure. Its smooth locus is a dense open subset ([Smooth algebras over a field and the Jacobian criterion](course:AG-CA/AG-CA-18), Corollary 3.3). Choose a closed point \(p\) of \(W\) in it and, by Lemma 1.2, coordinates \(w\) near \(p\), centred at \(p\), with \(W=V(w_1,\ldots,w_c)\) near \(p\), where \(c=\dim\mathcal O_{X,x}\). The derivations of \(w\) and of \(z\) are related by an invertible matrix of functions near \(x\), so the set of ideals \((\partial^\alpha f:|\alpha|\le j)\) does not depend on the coordinate system; it suffices to prove the claim for \(w\). If \(z\) itself is centred at a closed point of \(W\) and adapted to \(W\), take \(w=z\); this gives the final assertion. The ring \(\mathcal O_{X,x}\) is regular with maximal ideal \((w_1,\ldots,w_c)\). The restrictions of \(w_{c+1},\ldots,w_N\) to \(W\) form a coordinate system on \(W\) near \(p\), so the function field \(\kappa(x)\) of \(W\) is finite and separable over \(F=k(w_{c+1},\ldots,w_N)\). The subfield \(F\) lies in \(\mathcal O_{X,x}\), because a nonzero polynomial in \(w_{c+1},\ldots,w_N\) restricts to a nonzero function on \(W\) and is therefore a unit at \(x\). As in the first case, the completion of \(\mathcal O_{X,x}\) is \(L[[w_1,\ldots,w_c]]\) for a coefficient field \(L\supset F\) obtained by Hensel's lemma from a primitive element of \(\kappa(x)/F\). The derivations \(\partial/\partial w_i\) with \(i\le c\) vanish on \(F\) and hence on \(L\), and act as formal partial derivatives in \(w_1,\ldots,w_c\). The argument of the first case, with monomials in \(w_1,\ldots,w_c\), gives \(\alpha\) supported in \(\{1,\ldots,c\}\) with \(|\alpha|=d\) and \(\partial^\alpha f\notin\mathfrak m_x\). \(\square\)

**Definition 2.4 (derivative ideals).** For an ideal sheaf \(\mathcal I\) on a smooth scheme, \(D(\mathcal I)\) is the ideal sheaf generated by \(\mathcal I\) and by \(\delta(f)\) for all local derivations \(\delta\) and local sections \(f\) of \(\mathcal I\); set \(D^0(\mathcal I)=\mathcal I\) and \(D^{r+1}(\mathcal I)=D(D^r(\mathcal I))\).

On an open set with a coordinate system, \(D^r(\mathcal I)\) is generated by the \(\partial^\alpha f\) with \(f\in\mathcal I\) and \(|\alpha|\le r\). Indeed this holds for \(r=1\) because every derivation is an \(\mathcal O\)-linear combination of the \(\partial_i\), and if \(g=\sum a_\beta\partial^\beta f_\beta\) then \(\partial_i g=\sum(\partial_ia_\beta)\partial^\beta f_\beta+\sum a_\beta\partial_i\partial^\beta f_\beta\). Including \(\mathcal I\) in \(D(\mathcal I)\) is harmless: \(f=\partial_i(z_if)-z_i\partial_if\) always lies in the ideal generated by derivatives.

**Corollary 2.5 (cosupport).** For \(m\ge1\) put \(\operatorname{cosupp}(\mathcal I,m)=\{x:\operatorname{ord}_x\mathcal I\ge m\}\). Then

\[
\operatorname{cosupp}(\mathcal I,m)=V\bigl(D^{m-1}(\mathcal I)\bigr).
\]

In particular \(\operatorname{cosupp}(\mathcal I,m)\) is closed, \(x\mapsto\operatorname{ord}_x\mathcal I\) is upper semicontinuous, and for an irreducible closed \(Z\), \(\operatorname{ord}_Z\mathcal I\ge m\) if and only if \(Z\subset\operatorname{cosupp}(\mathcal I,m)\).

**Proof.** The point \(x\) lies in \(V(D^{m-1}\mathcal I)\) if and only if \(\partial^\alpha f\in\mathfrak m_x\) for all \(f\in\mathcal I_x\) and \(|\alpha|\le m-1\). By Proposition 2.3 this says \(\operatorname{ord}_xf\ge m\) for every \(f\in\mathcal I_x\), that is, \(\mathcal I_x\subset\mathfrak m_x^m\). The last claim holds because a closed set containing the generic point of \(Z\) contains \(Z\). \(\square\)

If \(\mathcal I\) is nonzero on every irreducible component of \(X\) and \(X\) is quasi-compact, then \(\operatorname{maxord}\mathcal I<\infty\): each \(\operatorname{cosupp}(\mathcal I,m)\) is closed, they decrease with \(m\), and their intersection is empty, so by quasi-compactness of the Noetherian space \(X\) one of them is empty.

**Proposition 2.6 (properties of derivative ideals).** Let \(\mathcal I,\mathcal J\) be ideal sheaves on a smooth scheme \(X\).

1. \(D^r(D^s(\mathcal I))=D^{r+s}(\mathcal I)\), and \(\mathcal I\subset D(\mathcal I)\subset D^2(\mathcal I)\subset\cdots\).
2. \(D^r(\mathcal I\mathcal J)\subset\sum_{i=0}^rD^i(\mathcal I)D^{r-i}(\mathcal J)\).
3. If \(m=\operatorname{maxord}\mathcal I<\infty\), then \(D^m(\mathcal I)=\mathcal O_X\), and for \(r<m\), \(\operatorname{cosupp}(D^r\mathcal I,m-r)=\operatorname{cosupp}(\mathcal I,m)\).
4. If \(h:Y\to X\) is smooth, then \(D(h^{-1}\mathcal I\cdot\mathcal O_Y)=h^{-1}D(\mathcal I)\cdot\mathcal O_Y\), and \(\operatorname{ord}_y(h^{-1}\mathcal I\cdot\mathcal O_Y)=\operatorname{ord}_{h(y)}\mathcal I\) for every \(y\in Y\).
5. If \(k\subset k'\) is a field extension and \(\mathcal I'\) is the pull-back of \(\mathcal I\) to \(X'=X\times_kk'\), then \(D(\mathcal I')\) is the pull-back of \(D(\mathcal I)\), and \(\operatorname{ord}_{x'}\mathcal I'=\operatorname{ord}_x\mathcal I\) for \(x'\) over \(x\).

**Proof.** (1) is the definition; the inclusions were noted after Definition 2.4. (2) follows from the Leibniz rule by induction on \(r\). (3) At every point some element of \(\mathcal I\) has order \(\le m\), so by Proposition 2.3 some \(\partial^\alpha f\) with \(|\alpha|\le m\) is a unit there. For the cosupports, \(\operatorname{cosupp}(D^r\mathcal I,m-r)=V(D^{m-r-1}D^r\mathcal I)=V(D^{m-1}\mathcal I)\) by Corollary 2.5 and (1).

(4) The question is local. By [Smooth morphisms](course:AG-FSE/AG-FSE-05), Theorem 4.1, near any point \(Y\) has an étale map to \(\mathbf A^d_X\) over \(X\); together with a coordinate system \(z\) on \(X\), the pulled-back functions \(h^*z_i\) and the \(d\) affine coordinates \(u_l\) form a coordinate system on \(Y\). For \(f\) on \(X\), the corresponding derivations satisfy \(\partial_{h^*z_i}(h^*f)=h^*(\partial_if)\) and \(\partial_{u_l}(h^*f)=0\). This gives the first claim. For the second, \(\operatorname{cosupp}(h^{-1}\mathcal I\cdot\mathcal O_Y,m)=V(D^{m-1}(h^{-1}\mathcal I\cdot\mathcal O_Y))=h^{-1}V(D^{m-1}\mathcal I)\) for every \(m\).

(5) A coordinate system on \(X\) remains one on \(X'\), and its derivations are the base changes, so the generators \(\partial^\alpha f\) correspond. The orders agree by Corollary 2.5, since \(V(D^{m-1}\mathcal I')\) is the inverse image of \(V(D^{m-1}\mathcal I)\). \(\square\)

Characteristic zero is used in Proposition 2.3 through \(\beta!\ne0\). In characteristic \(p\) the function \(x^p\) has order \(p\) at the origin but all its first derivatives vanish, and (3) fails.

## 3. Blowing up a smooth centre

A closed subscheme \(Z\) of a smooth scheme \(X\) is a *smooth centre* if it is smooth over \(k\); its components may have different dimensions. The blow-up \(\pi:B_ZX\to X\) ([Stacks, Tag 01OG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-definition-blow-up)) is an isomorphism over \(X\setminus Z\), and \(F=\pi^{-1}(Z)\) is an effective Cartier divisor, the *exceptional divisor* ([Stacks, Tag 02OS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-blowing-up-gives-effective-Cartier-divisor)). We allow \(Z=\emptyset\) (*empty blow-up*, \(\pi=\mathrm{id}\), \(F=\emptyset\)).

**Proposition 3.1 (charts).** Let \(Z\subset X\) be a smooth centre, \(p\) a closed point of \(Z\), and \(z\) a coordinate system on \(U\ni p\) with \(Z\cap U=V(z_1,\ldots,z_r)\), as in Lemma 1.2.

1. If \(r\ge2\), then \(\pi^{-1}(U)\) is covered by the opens \(U_j\), \(1\le j\le r\), where \(z_j\) generates the pulled-back ideal of \(Z\). On \(U_j\) the functions
\[
y_i=z_i/z_j\ (i\le r,\ i\ne j),\qquad y_j=z_j,\qquad y_i=z_i\ (i>r)
\]
form a coordinate system, and \(F\cap U_j=V(y_j)\).
2. If \(r=1\), then \(\pi\) is an isomorphism over \(U\) and \(F\cap U=Z\cap U\).

In particular \(B_ZX\) is smooth and \(F\) is a smooth divisor whose components lie over the components of \(Z\).

**Proof.** Since \(z:U\to\mathbf A^N\) is étale, hence flat, and \(Z\cap U\) is the inverse image of the linear subspace \(L=V(z_1,\ldots,z_r)\), blowing up commutes with this base change: \(B_{Z\cap U}U=U\times_{\mathbf A^N}B_L\mathbf A^N\) ([Stacks, Tag 0805](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-flat-base-change-blowing-up)). By [Stacks, Tags 0804](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-blowing-up-affine) and [0BIQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-blowup-regular-sequence), \(B_L\mathbf A^N\) is covered by the spectra of \(k[z_1,\ldots,z_N][y_i:i\le r,i\ne j]/(z_jy_i-z_i)\), which are polynomial rings in the variables listed in (1), with the pulled-back ideal of \(L\) generated by \(z_j=y_j\). The base change of these charts to \(U\) is étale over them, so the pulled-back functions form coordinate systems. For \(r=1\), \(Z\cap U\) is an effective Cartier divisor and the blow-up is an isomorphism ([Stacks, Tag 0807](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-blow-up-effective-Cartier-divisor)). \(\square\)

A blow-up whose centre is a union of components of codimension one is *trivial*: \(\pi\) is an isomorphism, but the exceptional divisor is \(F=Z\). The morphism \(\pi\) of a trivial blow-up does not determine \(Z\), and every later construction records the centre together with the morphism.

**Definition 3.2 (simple normal crossings).** An *ordered divisor* \(E=(E^1,\ldots,E^s)\) on a smooth scheme \(X\) is a finite sequence of smooth divisors, each possibly reducible or empty. It has *simple normal crossings* (snc) if every point \(x\) has a coordinate system on a neighbourhood such that each \(E^i\) through \(x\) equals \(V(z_{c(i)})\) near \(x\), with \(c(i)\ne c(i')\) for \(i\ne i'\). A smooth centre \(Z\) has *snc with* \(E\) if moreover the coordinates can be chosen with \(Z=V(z_{j_1},\ldots,z_{j_t})\) near \(x\). Some \(E^i\) may contain \(Z\).

**Lemma 3.3 (total transform).** Let \(E\) be snc and let the smooth centre \(Z\) have snc with \(E\). Let \(\pi:B_ZX\to X\) be the blow-up. Define \(\pi^{-1}_{\rm tot}(E)\) as the ordered divisor consisting of the strict transforms \(\pi^{-1}_*E^1,\ldots,\pi^{-1}_*E^s\) followed by \(F\). It has simple normal crossings. If \(Z\) is a component of some \(E^i\), the strict transform of that component is empty, and \(F\) contains it again.

**Proof.** Work in the charts of Proposition 3.1 with coordinates adapted to both \(E\) and \(Z\), say \(Z=V(z_1,\ldots,z_r)\) and \(E^i=V(z_{c(i)})\). If \(c(i)>r\), the strict transform of \(E^i\) is \(V(y_{c(i)})\) on every chart. If \(c(i)\le r\) and \(r\ge2\), then on \(U_j\) with \(j\ne c(i)\) the total transform \(V(y_{c(i)}y_j)\) is the strict transform \(V(y_{c(i)})\) plus \(F=V(y_j)\), and on \(U_{c(i)}\) the strict transform is empty. On every chart the divisors are distinct coordinate hyperplanes. If \(r=1\) the blow-up is the identity, the strict transform of \(V(z_1)\) is empty, and \(F=V(z_1)\). Strict transforms are defined in [Stacks, Tag 080D](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-definition-strict-transform); for a closed subscheme \(S\subset X\) the strict transform is the blow-up \(B_{Z\cap S}S\) ([Stacks, Tag 080E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-strict-transform)). \(\square\)

## 4. Transforms of ideals and of marked ideals

**Lemma 4.1 (multiplicity along the exceptional divisor).** Let \(Z\subset X\) be a smooth centre that is irreducible near a closed point \(p\), with coordinates centred at \(p\) and \(Z=V(z_1,\ldots,z_r)\) near \(p\), \(r\ge1\). Let \(f\) be a function near \(p\) with \(\operatorname{ord}_Zf\ge m\).

1. Near \(p\), \(f\in(z_1,\ldots,z_r)^m\).
2. On each chart \(U_j\) of Proposition 3.1 (or on \(U\) if \(r=1\)), \(\pi^*f=y_j^m f'\) for a function \(f'\).
3. If \(\operatorname{ord}_Zf=m\), then \(f'\) does not vanish identically on any component of \(F\cap U_j\).

Consequently the multiplicity of \(\pi^{-1}\mathcal I\cdot\mathcal O_{B_ZX}\) along the component of \(F\) over a component \(Z_j\) of \(Z\) equals \(\operatorname{ord}_{Z_j}\mathcal I\).

**Proof.** (1) Let \(\eta\) be the generic point of \(Z\). For \(\alpha\) supported in \(\{1,\ldots,r\}\) with \(|\alpha|<m\), Lemma 2.2 gives \(\partial^\alpha f\in\mathfrak m_\eta\cap\mathcal O_{X,p}=(z_1,\ldots,z_r)\mathcal O_{X,p}\); the last equality holds because \(\mathcal O_{X,p}/(z_1,\ldots,z_r)=\mathcal O_{Z,p}\) is a domain. In the completion \(k(a)[[z_1,\ldots,z_N]]\) of the proof of Proposition 2.3, write \(f=\sum c_\beta z^\beta\). For \(\gamma\) supported in \(\{r+1,\ldots,N\}\), the coefficient of \(z^\gamma\) in \(\partial^\alpha f\) is \(\alpha!\,c_{\alpha+\gamma}\). It must vanish because \(\partial^\alpha f\in(z_1,\ldots,z_r)\). So \(c_\beta=0\) whenever \(\beta\) has degree \(<m\) in \(z_1,\ldots,z_r\), that is, \(f\in(z_1,\ldots,z_r)^m\widehat{\mathcal O}_{X,p}\). The completion is faithfully flat over \(\mathcal O_{X,p}\) ([Completion](course:AG-CA/AG-CA-19), Theorem 3.2), so \(f\in(z_1,\ldots,z_r)^m\mathcal O_{X,p}\), and this persists on a neighbourhood of \(p\).

(2) Write \(f=\sum_{|\beta|=m}z^\beta a_\beta\) with \(\beta\) supported in \(\{1,\ldots,r\}\). On \(U_j\), \(\pi^*z^\beta=y_j^m\prod_{i\ne j}y_i^{\beta_i}\), so \(f'=\sum_\beta\bigl(\prod_{i\ne j}y_i^{\beta_i}\bigr)\pi^*a_\beta\).

(3) The restriction of \(f'\) to \(F\cap U_j\cong(Z\cap U)\times\mathbf A^{r-1}\) is the polynomial \(\sum_\beta(\prod_{i\ne j}y_i^{\beta_i})\,a_\beta|_Z\) in the fibre variables. Distinct \(\beta\) of degree \(m\) give distinct monomials, because \(\beta_j=m-\sum_{i\ne j}\beta_i\). So the restriction vanishes only if every \(a_\beta|_Z=0\). Now for \(|\alpha|=m\) supported in \(\{1,\ldots,r\}\), every term of \(\partial^\alpha(z^\beta a_\beta)\) in which a derivative falls on \(a_\beta\) keeps a positive power of some \(z_i\), \(i\le r\), and the remaining term is nonzero on \(Z\) only for \(\beta=\alpha\). Hence \((\partial^\alpha f)|_Z=\alpha!\,a_\alpha|_Z\). If \(\operatorname{ord}_Zf=m\), Proposition 2.3 at \(\eta\), applied with coordinates adapted to \(Z\), gives such an \(\alpha\) with \(\partial^\alpha f\notin\mathfrak m_\eta\), so \(a_\alpha|_Z\ne0\). \(\square\)

**Definition 4.2 (birational transform).** Let \(\pi:B_ZX\to X\) be the blow-up of a smooth centre with components \(Z_j\) and exceptional components \(F_j\) over them. For an ideal sheaf \(\mathcal I\) with \(m_j=\operatorname{ord}_{Z_j}\mathcal I<\infty\), the *birational transform* is

\[
\pi^{-1}_*\mathcal I=\mathcal O_{B_ZX}\Bigl(\sum_jm_jF_j\Bigr)\cdot\pi^{-1}\mathcal I\cdot\mathcal O_{B_ZX}.
\]

A *marked ideal* is a pair \((\mathcal I,m)\) with \(m\in\mathbf N\). Its *cosupport* is \(\operatorname{cosupp}(\mathcal I,m)\), as in Corollary 2.5. If \(\operatorname{ord}_Z\mathcal I\ge m\), the *birational transform* of \((\mathcal I,m)\) is

\[
\pi^{-1}_*(\mathcal I,m)=\bigl(\mathcal O_{B_ZX}(mF)\cdot\pi^{-1}\mathcal I\cdot\mathcal O_{B_ZX},\ m\bigr).
\]

By Lemma 4.1 both are ideal sheaves, and the unmarked transform does not contain any \(F_j\) in its cosupport \(\operatorname{cosupp}(\cdot,1)\). In a chart, \(\pi^{-1}_*(f,m)=y_j^{-m}f(y_1y_j,\ldots,y_j,\ldots,y_ry_j,y_{r+1},\ldots,y_N)\). This formula depends on the coordinates only up to a unit, so it computes ideals but not individual functions. For a trivial blow-up (\(r=1\)) the scheme does not change, but \(\pi^{-1}_*(\mathcal I,m)=\mathcal O_X(mZ)\mathcal I\) has order \(m\) less along \(Z\).

Marked ideals multiply by \((\mathcal I_1,m_1)(\mathcal I_2,m_2)=(\mathcal I_1\mathcal I_2,m_1+m_2)\) and add, for equal markings, by \((\mathcal I_1,m)+(\mathcal I_2,m)=(\mathcal I_1+\mathcal I_2,m)\). Birational transforms respect both operations whenever they are defined. The cosupports satisfy \(\operatorname{cosupp}(\mathcal I_1+\mathcal I_2,m)=\operatorname{cosupp}(\mathcal I_1,m)\cap\operatorname{cosupp}(\mathcal I_2,m)\), \(\operatorname{cosupp}(\mathcal I^c,mc)=\operatorname{cosupp}(\mathcal I,m)\), and \(\operatorname{cosupp}(\mathcal I_1\mathcal I_2,m_1+m_2)\supset\operatorname{cosupp}(\mathcal I_1,m_1)\cap\operatorname{cosupp}(\mathcal I_2,m_2)\). These follow from \(\operatorname{ord}_x(\mathcal I_1+\mathcal I_2)=\min(\operatorname{ord}_x\mathcal I_1,\operatorname{ord}_x\mathcal I_2)\) and \(\operatorname{ord}_x(\mathcal I_1\mathcal I_2)=\operatorname{ord}_x\mathcal I_1+\operatorname{ord}_x\mathcal I_2\); the latter holds because \(\operatorname{ord}_x(fg)=\operatorname{ord}_xf+\operatorname{ord}_xg\) in the regular local ring \(\mathcal O_{X,x}\), whose graded ring is a polynomial ring ([Regular local rings](course:AG-CA/AG-CA-14), Theorem 1.1).

**Lemma 4.3 (the maximal order does not increase).** If \(\operatorname{ord}_Z\mathcal I=\operatorname{maxord}\mathcal I=m<\infty\), then \(\operatorname{maxord}\pi^{-1}_*\mathcal I\le m\).

**Proof.** Away from \(F\) the blow-up is an isomorphism. Every point of \(B_ZX\) specializes to a closed point, and the order can only increase under specialization (Corollary 2.5). So it suffices to show \(\operatorname{ord}_q\pi^{-1}_*\mathcal I\le m\) for a closed point \(q\in F\). Its image \(p\) is a closed point of \(Z\). Choose coordinates centred at \(p\) adapted to the component of \(Z\) through \(p\), \(Z=V(z_1,\ldots,z_r)\), and choose \(f\in\mathcal I_p\) with \(\operatorname{ord}_pf=m\), possible since \(m=\operatorname{ord}_Z\mathcal I\le\operatorname{ord}_p\mathcal I\le m\). By Lemma 4.1, \(f=\sum_{|\beta|=m}z^\beta a_\beta\) near \(p\), with \(\beta\) supported in \(\{1,\ldots,r\}\).

First, some \(a_\alpha\) is a unit at \(p\). Proposition 2.3 gives \(\alpha\) with \(|\alpha|=m\) and \(\partial^\alpha f(p)\ne0\). If \(\alpha\) involved an index \(i>r\), every term of \(\partial^\alpha(z^\beta a_\beta)\) would apply at most \(m-1\) derivatives to \(z^\beta\) and so would vanish at \(p\). So \(\alpha\) is supported in \(\{1,\ldots,r\}\), and as in the proof of Lemma 4.1(3), \(\partial^\alpha f(p)=\alpha!\,a_\alpha(p)\). Hence \(a_\alpha(p)\ne0\).

Let \(q\in U_j\) (for \(r=1\) read \(U_1=U\) and ignore the fibre variables). Write \(y'=(y_i)_{i\le r,\,i\ne j}\) for the fibre coordinates. Then \(f'=y_j^{-m}\pi^*f=\sum_\beta y'^{\beta'}\pi^*a_\beta\), where \(\beta'\) is \(\beta\) with its \(j\)-th entry removed; \(\beta\mapsto\beta'\) is injective on \(\{|\beta|=m\}\). Among the \(\beta\) with \(a_\beta(p)\ne0\), choose one, \(\gamma\), with \(|\gamma'|\) maximal. The derivations \(\partial/\partial y_i\) with \(i\ne j\) preserve the ideal \((y_j)\) of \(F\cap U_j\) and induce the coordinate derivations of \(F\cap U_j\cong(Z\cap U)\times\mathbf A^{r-1}\) for the coordinates \(y'\) and \(z_{r+1},\ldots,z_N\). Functions pulled back from \(Z\) are killed by the \(\partial/\partial y_i\), \(i\le r\), \(i\ne j\). Therefore

\[
\bigl(\partial_{y'}^{\gamma'}f'\bigr)\big|_F=\gamma'!\,a_\gamma|_Z+\sum_{\beta'>\gamma'}\frac{\beta'!}{(\beta'-\gamma')!}\,y'^{\beta'-\gamma'}a_\beta|_Z,
\]

where \(\beta'>\gamma'\) means \(\beta'\ge\gamma'\) componentwise and \(\beta'\ne\gamma'\). Each such \(\beta\) has \(|\beta'|>|\gamma'|\), so \(a_\beta(p)=0\) by the choice of \(\gamma\). Evaluating at \(q\), which lies over \(p\), gives \(\gamma'!\,a_\gamma(p)\ne0\). So \(\partial_{y'}^{\gamma'}f'\) is a unit at \(q\), and by Lemma 2.2, \(\operatorname{ord}_qf'\le|\gamma'|\le m\). Since \(f'\in\pi^{-1}_*\mathcal I\), the claim follows. \(\square\)

**Lemma 4.4 (transforms commute with restriction).** Let \(H\subset X\) be a smooth hypersurface and \(Z\subset H\) a smooth centre containing no component of \(H\). Let \(B_ZH\subset B_ZX\) be the strict transform, with \(\pi_H:B_ZH\to H\). If \(\operatorname{ord}_Z\mathcal I\ge m\) and \(\mathcal I|_H\) is nonzero on every component of \(H\), then \(\operatorname{ord}_Z(\mathcal I|_H)\ge m\) and

\[
(\pi_H)^{-1}_*(\mathcal I|_H,m)=\bigl(\pi^{-1}_*(\mathcal I,m)\bigr)\big|_{B_ZH}.
\]

**Proof.** Restriction to \(H\) maps \(\mathfrak m_{X,\eta}\) into \(\mathfrak m_{H,\eta}\), so orders do not decrease. Locally choose coordinates with \(H=V(z_1)\) and \(Z=V(z_1,\ldots,z_r)\); here \(r\ge2\) because \(Z\) contains no component of \(H\). The strict transform \(B_ZH\) is \(V(y_1)\) on the charts \(U_j\), \(2\le j\le r\), and does not meet \(U_1\), where the pull-back of \(z_1\) generates the ideal of \(F\). On \(U_j\), setting \(y_1=0\) in \(y_j^{-m}f(y_1y_j,y_2y_j,\ldots)\) gives \(y_j^{-m}f(0,y_2y_j,\ldots)\), the chart formula for the transform of \((f|_H,m)\) on \(B_ZH\). \(\square\)

The hypothesis that \(Z\) contains no component of \(H\) cannot be dropped. If \(Z=H\), the restriction \(\mathcal I|_H\) of an ideal with \(\operatorname{ord}_H\mathcal I\ge m\ge1\) is zero, and only the chart \(U_1\) exists.

**Example 4.5 (the transform depends on the sequence of centres).** Let \(C\) be a smooth curve through a closed point \(p\) in a smooth threefold \(X_0\), and \(\mathcal I=\mathcal I_C\), marked with \(1\). Blowing up \(p\) and then the strict transform of \(C\) gives exceptional divisors \(E_0,E_1\) on \(X_2\) and the transform \(\mathcal O(E_0+E_1)\Pi^{-1}\mathcal I\). Blowing up \(C\) and then the fibre \(D\) of the first exceptional divisor over \(p\) gives \(X_2'\cong X_2\) with \(E_0'\leftrightarrow E_1\), \(E_1'\leftrightarrow E_0\). The transform is \(\mathcal O(E_0'+2E_1')\Sigma^{-1}\mathcal I\), because the pull-back of \(E_0'\) under the second blow-up is \(E_0'+E_1'\). The two composite morphisms agree, but the transforms of \((\mathcal I,1)\) differ. Transforms of marked ideals are therefore always taken along a specified sequence of blow-ups.

## 5. Exercises

**Exercise 5.1.** Let \(\mathcal I=(x^2+y^3)\) on \(\mathbf A^2\). Compute \(\operatorname{ord}_x\mathcal I\) at every point, \(D(\mathcal I)\), \(D^2(\mathcal I)\), and \(\operatorname{cosupp}(\mathcal I,2)\).

*Solution.* The order is \(2\) at the origin, \(1\) at the other points of the curve, and \(0\) elsewhere. \(D(\mathcal I)=(x^2+y^3,2x,3y^2)=(x,y^2)\) and \(D^2(\mathcal I)=(1)\). By Corollary 2.5, \(\operatorname{cosupp}(\mathcal I,2)=V(x,y^2)\) as a set, the origin.

**Exercise 5.2.** Blow up the origin of \(\mathbf A^2\) for \(\mathcal I=(x^2+y^3)\). Compute \(\pi^{-1}_*\mathcal I\) and \(\pi^{-1}_*(\mathcal I,1)\) in both charts, and check Lemma 4.3.

*Solution.* The order along the origin is \(2\). On the chart \(x=x_1y,\ y=y\): \(\pi^*(x^2+y^3)=y^2(x_1^2+y)\), so \(\pi^{-1}_*\mathcal I=(x_1^2+y)\), of maximal order \(1\). On the chart \(x=x,\ y=y_1x\): \(\pi^*=x^2(1+y_1^3x)\), so \(\pi^{-1}_*\mathcal I=(1+y_1^3x)\), which has order \(0\) at every point of \(F=V(x)\). The marked transform \(\pi^{-1}_*(\mathcal I,1)=\mathcal O(F)\pi^{-1}\mathcal I\) is \((y(x_1^2+y))\), respectively \((x(1+y_1^3x))\); it still contains \(F\) in its cosupport \(\operatorname{cosupp}(\cdot,1)\).

**Exercise 5.3.** Show that \(\operatorname{ord}_x\) is not upper semicontinuous for a general ideal on a singular scheme if one defines it by the same formula: take \(X=V(xy)\subset\mathbf A^2\), \(\mathcal I=(x)\cdot\mathcal O_X\).

*Solution.* At the origin \(\mathfrak m=(x,y)\) and \(x\notin\mathfrak m^2\) in \(\mathcal O_{X,0}\), so the order is \(1\). At the generic point of the line \(V(x)\) the image of \(x\) is \(0\), so the order is \(\infty\). The set where the order is \(\ge2\) is the line \(V(x)\) minus the origin, which is not closed. On smooth schemes Corollary 2.5 rules this out.

**Exercise 5.4.** Let \(k\) have characteristic \(p>0\) and let \(\mathcal I=(x^p)\) on \(\mathbf A^1_k\). Show that \(D^r(\mathcal I)=\mathcal I\) for every \(r\), so that \(V(D^{m-1}\mathcal I)=\{0\}\) for every \(m\ge1\), while \(\operatorname{cosupp}(\mathcal I,m)=\emptyset\) for \(m>p\). Which step of Proposition 2.3 fails?

*Solution.* \(\partial_x(x^p)=px^{p-1}=0\), so \(D(\mathcal I)=(x^p)\), and by induction \(D^r(\mathcal I)=(x^p)\). The order of \(\mathcal I\) at the origin is \(p\) and at every other point \(0\), so \(\operatorname{cosupp}(\mathcal I,m)\) is empty for \(m>p\), while \(V(D^{m-1}\mathcal I)=V(x^p)\) is the origin. In Proposition 2.3 the monomial \(x^p\) has \(\partial^p(x^p)=p!=0\): the constant term \(\beta!\,c_\beta\) vanishes. Corollary 2.5 and Proposition 2.6(3) fail accordingly.

## References

- [Kollár] J. Kollár, *Resolution of singularities — Seattle lecture* (2005, revised 2007), arXiv:math/0508332, sections on blow-ups, birational transforms and marked ideals. <https://arxiv.org/abs/math/0508332>
- [Włodarczyk] J. Włodarczyk, *Simple Hironaka resolution in characteristic zero*, J. Amer. Math. Soc. 18 (2005); free preprint arXiv:math/0401401. <https://arxiv.org/abs/math/0401401>
- [Hauser] H. Hauser, *The Hironaka theorem on resolution of singularities (Or: A proof we always wanted to understand)*, Bull. Amer. Math. Soc. 40 (2003), 323–403, free from the AMS. <https://www.ams.org/journals/bull/2003-40-03/S0273-0979-03-00982-0/>
