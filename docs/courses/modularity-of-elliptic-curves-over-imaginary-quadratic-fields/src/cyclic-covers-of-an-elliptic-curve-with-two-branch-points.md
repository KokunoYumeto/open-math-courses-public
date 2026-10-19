# Cyclic covers of an elliptic curve with two branch points

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson constructs the curves that carry the congruences of the course. Starting from an elliptic curve \(E\colon y^2=h(x)\), a parameter \(t\) gives a quadratic twist \(B_t\) of \(E\) with a rational point \(R_t\). A rational function on \(B_t\) with zeros and poles at \(\pm R_t\) and \(\pm[n]R_t\) defines cyclic covers \(C_{m,t}\to B_t\) of every degree \(m\mid n\). They have genus \(m\), they are branched at exactly two points, and they carry an involution that inverts the deck transformations. As \(t\) varies, the covers form a smooth proper family over an open subset of the affine line, and the same family can be written with the fixed curve \(E\) and a moving point \(R\in E\).

**Prerequisites.** [*Elliptic curves over imaginary quadratic fields and their automorphy*](elliptic-curves-over-imaginary-quadratic-fields-and-their-automorphy.md). From *Galois representations*: [*The ℓ-adic Tate module of an elliptic curve*](course:LG-GAL/the-adic-tate-module-of-an-elliptic-curve), Section 1.1, in particular the criterion (G4) for principal divisors. From *The étale fundamental group*: [*The étale fundamental group*](course:AG-DFG/etale-fundamental-group), the Riemann–Hurwitz formula (5.5) in characteristic zero.

**Conventions.** Throughout, \(k\) is a field of characteristic zero and \(n\ge3\) is an odd integer. Curves are smooth, projective and geometrically integral unless stated otherwise. For a point \(P\) of an elliptic curve, \((P)\) denotes the corresponding prime divisor, and sums of points are taken in the group law.

## 1. Twists and the parameter set

Let \(h\in k[x]\) be a separable cubic polynomial and \(E\colon y^2=h(x)\), with origin the point \(O\) at infinity. For \(t\in k\) with \(h(t)\neq0\) put
\[
\begin{gathered}
B_t\colon\ h(t)\,y^2=h(x),\\
R_t=(t,1),\qquad S_t=[n]R_t .\quad(1.1)
\end{gathered}
\]
The curve \(B_t\) is an elliptic curve with origin \(O\). Over \(k\bigl(\sqrt{h(t)}\bigr)\) the map \((x,y)\mapsto\bigl(x,\sqrt{h(t)}\,y\bigr)\) is an isomorphism \(B_t\to E\) of elliptic curves, so \(B_t\) is the quadratic twist of \(E\) by \(h(t)\); it is isomorphic to \(E\) over \(k\) when \(h(t)\) is a square.

**Lemma 1.1.** Let \(U\subset\mathbb A^1_k\) be the set of \(t\) with \(h(t)\ne0\) for which the five points \(O,R_t,-R_t,S_t,-S_t\) of \(B_t\) are pairwise distinct. Then the complement of \(U\) in \(\mathbb A^1_{\bar k}\) is finite, and \(U\) is a nonempty open subset of \(\mathbb A^1_k\).

**Proof.** Write \(R=R_t\). The point \(R\) is affine, so \(R\ne O\), and \(-R=(t,-1)\ne R\). The remaining conditions say that \([m]R\ne O\) for \(m=n\) (for \(S_t\ne O\)), \(m=n-1\) and \(m=n+1\) (for \(S_t\ne\pm R\)) and \(m=2n\) (for \(S_t\ne-S_t\)). Under the isomorphism \(B_t\to E\) over \(\bar k\), the point \(R\) goes to \(\bigl(t,\sqrt{h(t)}\bigr)\), and the isomorphism respects multiplication by \(m\). The torsion subgroup \(E[m](\bar k)\) is finite, so the set of \(x\)-coordinates of its points is finite. Hence \(t\notin U\) exactly when \(h(t)=0\) or \(t\) is the \(x\)-coordinate of a point of \(E[m]\) for one of the four values of \(m\). This finite set is stable under \(\operatorname{Gal}(\bar k/k)\), so its complement is open and defined over \(k\). \(\square\)

## 2. The Kummer function

**Lemma 2.1.** Let \(t\in U(k)\). There is a unique \(f_t\in k(B_t)^\times\) with
\[
\begin{aligned}
\operatorname{div}(f_t)&=(S_t)-(-S_t)\\
&\quad-n(R_t)+n(-R_t),\\
f_t(O)&=1,\quad(2.1)
\end{aligned}
\]
and it satisfies
\[
f_t\circ[-1]=f_t^{-1}.
\tag{2.2}
\]

**Proof.** The divisor \(D\) on the right of (2.1) has degree \(1-1-n+n=0\). Its sum in the group law is
\[
\begin{aligned}
&S_t+S_t-[n]R_t-[n]R_t\\
&\quad=2[n]R_t-2[n]R_t=O .
\end{aligned}
\]
By the criterion (G4) for principal divisors, \(D=\operatorname{div}(g)\) for some \(g\in\bar k(B_t)^\times\). The point \(O\) is not in the support of \(D\), so \(g(O)\in\bar k^\times\), and \(f=g/g(O)\) has divisor \(D\) and value \(1\) at \(O\). Any two functions with the same divisor differ by a nonzero constant, so \(f\) is unique among functions in \(\bar k(B_t)\) with these properties. For \(\sigma\in\operatorname{Gal}(\bar k/k)\), the function \(\sigma(f)\) has divisor \(\sigma(D)=D\), because the four points are \(k\)-rational, and value \(\sigma(1)=1\) at \(O\). By uniqueness \(\sigma(f)=f\) for all \(\sigma\), so \(f\in k(B_t)\).

The function \(f\circ[-1]\) has divisor \([-1]^*D\)\(=(-S_t)-(S_t)-n(-R_t)+n(R_t)\)\(=-D\), so \(f\circ[-1]=c/f\) for a constant \(c\). Evaluating at \(O=-O\) gives \(1=c\). \(\square\)

**Remark 2.2.** The normalization \(f_t(O)=1\) matters. Any other choice \(cf_t\) gives the cover \(Y^m=cf_t\), which differs from \(Y^m=f_t\) by the twist by the class of \(c\) in \(k^\times/k^{\times m}\). The normalized function is the one compatible with base change and with the identifications of Section 6.

## 3. The cyclic covers

Let \(m>1\) be a divisor of \(n\); it is odd. For \(t\in U(k)\) let \(C_{m,t}\) be the curve with function field
\[
k(C_{m,t})=k(B_t)[Y]/(Y^m-f_t),\quad(3.1)
\]
that is, the normalization of \(B_t\) in this field. We write \(Z\) for a point of \(B_t\), so that the cover is "\(Y^m=f_t(Z)\)".

**Proposition 3.1.** Let \(t\in U(k)\).

1. The polynomial \(Y^m-f_t\) is irreducible over \(\bar k(B_t)\). Hence \(C_{m,t}\) is geometrically integral and \(C_{m,t}\to B_t\) has degree \(m\).
2. The cover is totally ramified over \(S_t\) and \(-S_t\) and unramified over every other point of \(B_t\).
3. \(C_{m,t}\) has genus \(m\).

**Proof.** (1) Let \(K=\bar k(B_t)\) and \(v\) the valuation of \(K\) at \(S_t\), so \(v(f_t)=1\). Let \(L=K(y)\) with \(y^m=f_t\), and let \(w\) be an extension of \(v\) to \(L\), with ramification index \(e\), normalized by \(w|_K=e\,v\). Then \(m\,w(y)=w(f_t)=e\). So \(m\) divides \(e\), and \(m\le e\le[L:K]\le m\). Hence \([L:K]=m\), the polynomial is irreducible, and \(S_t\) is totally ramified.

(2) The same argument applies at \(-S_t\), where \(v(f_t)=-1\). Let \(P\in B_t(\bar k)\) be any other point and \(\pi\) a uniformizer at \(P\). Then \(f_t=\pi^{a}\varepsilon\) with \(\varepsilon\) a unit at \(P\) and \(a\in\{0,n,-n\}\), so \(m\mid a\). Put \(y'=y\pi^{-a/m}\); then \(y'^m=\varepsilon\). In the completed local ring \(\bar k[[\pi]]\) the unit \(\varepsilon\) has \(m\) distinct \(m\)-th roots, by Hensel's lemma, because \(\varepsilon(P)\ne0\) and \(m\) is invertible in \(\bar k\). So \(Y^m-\varepsilon\) splits into \(m\) distinct linear factors over the completion, and \(P\) has \(m\) distinct preimages, each unramified.

(3) By (2) the two branch points contribute ramification index \(m\) each, and every other point is unramified. The Riemann–Hurwitz formula (5.5) of [*The étale fundamental group*](course:AG-DFG/etale-fundamental-group), applied over \(\bar k\), with \(g(B_t)=1\), gives
\[
2g(C_{m,t})-2=m\cdot0+2(m-1),
\]
so \(g(C_{m,t})=m\). The genus does not change under extension of the ground field, because the curve is geometrically integral. \(\square\)

## 4. The family over \(U\)

The covers vary in a smooth proper family. Let
\[
\begin{gathered}
\mathcal B\subset\mathbb P^2_U,\\
\mathcal B\colon\ h(t)Y_0^{\,2}Y_2=h^{\mathrm{hom}}(Y_1,Y_2)
\end{gathered}
\]
be the projective closure of \(h(t)y^2=h(x)\) over \(U\), where \(h^{\mathrm{hom}}\) is the homogenization of \(h\) and \(x=Y_1/Y_2\), \(y=Y_0/Y_2\). Since \(h(t)\) is invertible on \(U\) and \(h\) is separable, \(\mathcal B\to U\) is an elliptic curve over \(U\): smooth and proper with geometrically connected fibres of genus one and the zero section \(O\) at infinity. The points \(R=(t,1)\), \(-R\), \(S=[n]R\) and \(-S\) are sections \(U\to\mathcal B\), and by the definition of \(U\) the five sections \(O,\pm R,\pm S\) are pairwise disjoint.

**Lemma 4.1.** There is a rational function \(f\) on \(\mathcal B\) whose divisor is
\[
\begin{aligned}
\operatorname{div}(f)&=S(U)-(-S)(U)\\
&\quad-n\,R(U)+n\,(-R)(U),\quad(4.1)
\end{aligned}
\]
which is regular and equal to \(1\) along \(O(U)\), and whose restriction to every fibre \(\mathcal B_t\), \(t\in U\), is the function \(f_t\) of Lemma 2.1.

**Proof.** Apply Lemma 2.1 over the field \(k(t)\) to the generic fibre of \(\mathcal B\), with the point \(R\). This gives \(f\in k(\mathcal B)^\times\) whose divisor on the generic fibre is the generic fibre of (4.1), with \(f=1\) at the generic point of \(O(U)\). The surface \(\mathcal B\) is regular, so \(\operatorname{div}(f)\) is defined, and it equals the right side of (4.1) plus a vertical divisor \(\sum_ua_u\mathcal B_u\) over finitely many closed points \(u\in U\). The automorphism \([-1]\) of \(\mathcal B\) over \(U\) maps each fibre \(\mathcal B_u\) to itself, and \(f\circ[-1]=f^{-1}\) by (2.2) on the generic fibre. Comparing the multiplicity of \(\mathcal B_u\) in the divisors of both sides gives \(a_u=-a_u\), so \(a_u=0\). Thus (4.1) holds. The section \(O(U)\) is disjoint from the four sections in (4.1), so \(f\) is regular and invertible near it, and its restriction to \(O(U)\cong U\) is a function on \(U\) that equals \(1\) at the generic point, hence everywhere. Finally, the sections meet each fibre transversally in one point, so the restriction of \(f\) to \(\mathcal B_t\) has the divisor (2.1) and value \(1\) at \(O\); by uniqueness it is \(f_t\). \(\square\)

**Proposition 4.2.** For each divisor \(m>1\) of \(n\), let \(\mathcal C_m\) be the normalization of \(\mathcal B\) in \(k(\mathcal B)[Y]/(Y^m-f)\). Then \(\mathcal C_m\to U\) is smooth and proper, and its fibre over \(t\in U\) is the curve \(C_{m,t}\) of Section 3.

**Proof.** Normalization of a scheme of finite type over a field in a finite extension of its function field is finite, so \(\mathcal C_m\to\mathcal B\) is finite and \(\mathcal C_m\to U\) is proper. Smoothness is local on \(\mathcal B\). Let \(P\in\mathcal B\) be a closed point over \(u\in U\), and let \(\tau\) be a local parameter of \(U\) at \(u\).

*If \(P\) lies on none of the four sections,* \(f\) is a unit at \(P\). The algebra \(\mathcal O_{\mathcal B,P}[Y]/(Y^m-f)\) is finite étale over \(\mathcal O_{\mathcal B,P}\), since the derivative \(mY^{m-1}\) is invertible (\(Y^m=f\) is a unit and \(m\) is invertible). An étale algebra over a regular local ring is regular, hence normal, so it is the local ring of the normalization, and it is smooth over \(U\) because \(\mathcal B\) is.

*If \(P\) lies on \(\pm R(U)\),* let \(\pi\) be a local equation of that section near \(P\); the section is a Cartier divisor on the regular surface. Then \(f=\pi^{a}\varepsilon\) with \(a=\mp n\) and \(\varepsilon\) a unit, and \(Y'=Y\pi^{-a/m}\) satisfies \(Y'^m=\varepsilon\). The previous case applies to \(Y'\), which generates the same field.

*If \(P\) lies on \(\pm S(U)\),* let \(\pi\) be a local equation of the section. Because the section is a section of a smooth morphism of relative dimension one, \((\tau,\pi)\) is a regular system of parameters at \(P\), and \(\pi\) restricts to a uniformizer on the fibre \(\mathcal B_u\) at \(P\). Write \(f^{\pm1}=\pi\varepsilon\) with \(\varepsilon\) a unit. After the étale base change that adjoins \(e=\varepsilon^{1/m}\), the element \(Y''=Y^{\pm1}/e\) satisfies \(Y''^m=\pi\). The algebra \(\mathcal O[Y'']/(Y''^m-\pi)\) is regular with parameters \((\tau,Y'')\), and étale locally over \(U\) it is the relative affine line with coordinate \(Y''\), mapping to the relative affine line with coordinate \(\pi\) by \(Y''\mapsto Y''^m\). It is therefore normal and smooth over \(U\). Smoothness and normality descend along the étale base change.

So \(\mathcal C_m\) is smooth over \(U\). In each of the three local models the fibre over \(u\) is the normalization of \(\mathcal B_u\) in the field (3.1), by the same computations as in Proposition 3.1. Hence the fibre of \(\mathcal C_m\) over \(t\) is \(C_{m,t}\). \(\square\)

By Proposition 3.1 the fibres are geometrically connected of genus \(m\). The open set \(U\) may be shrunk by finitely many points whenever this is convenient; this changes none of the statements of the course.

## 5. The involution and the rotations

**Proposition 5.1.** For every \(t\in U(k)\) and every divisor \(m>1\) of \(n\):

1. there is an involution \(w\) of \(C_{m,t}\), defined over \(k\), given by
\[
w(Z,Y)=(-Z,\,Y^{-1});\quad(5.1)
\]
2. if \(k\) contains the group \(\mu_m\) of \(m\)-th roots of unity, the maps \(u_\zeta(Z,Y)=(Z,\zeta Y)\), \(\zeta\in\mu_m\), are automorphisms of \(C_{m,t}\) over \(B_t\), they form the full group of deck transformations, and
\[
w\,u_\zeta\,w=u_{\zeta^{-1}};
\tag{5.2}
\]
3. for \(d\mid m\), the inclusion \(k(B_t)(Y^{m/d})\subset k(C_{m,t})\) defines a map \(C_{m,t}\to C_{d,t}\), \(Y\mapsto Y^{m/d}\), which is the quotient by the subgroup \(\mu_{m/d}\) of rotations; for \(d=1\) it is \(C_{m,t}\to B_t\).

All these maps extend to the family \(\mathcal C_m\to U\).

**Proof.** (1) On function fields, define \(w^*\) by \(w^*(g)=g\circ[-1]\) for \(g\in k(B_t)\) and \(w^*(Y)=Y^{-1}\). This is compatible with the relation \(Y^m=f_t\), because \((Y^{-1})^m=f_t^{-1}=f_t\circ[-1]\) by (2.2). So \(w^*\) is a field automorphism of \(k(C_{m,t})\) over \(k\) with \((w^*)^2=1\), and it induces an involution of the curve.

(2) If \(\mu_m\subset k\), the extension (3.1) is a Kummer extension of degree \(m\) with Galois group \(\{Y\mapsto\zeta Y\}\cong\mu_m\). The automorphisms of the curve over \(B_t\) are the automorphisms of its function field over \(k(B_t)\), so they are the \(u_\zeta\). For (5.2), compute on points:
\[
\begin{aligned}
w\,u_\zeta\,w(Z,Y)&=w\,u_\zeta(-Z,Y^{-1})\\
&=w(-Z,\zeta Y^{-1})\\
&=(Z,\zeta^{-1}Y).
\end{aligned}
\]

(3) The element \(Y^{m/d}\) satisfies \((Y^{m/d})^d=f_t\), so \(k(B_t)(Y^{m/d})\) is the function field of \(C_{d,t}\), and it is the fixed field of the rotations by \(\zeta\) with \(\zeta^{m/d}=1\).

The same formulas define automorphisms and maps of the generic fibres of the families, and they extend to the normal schemes \(\mathcal C_m\), \(\mathcal C_d\) and \(\mathcal B\), which are the normalizations of \(\mathcal B\) in the respective fields. \(\square\)

The involution has a small fixed-point set, which already shows how it pairs the rotation characters.

**Proposition 5.2.** The involution \(w\) of \(C_{m,t}\) has exactly four fixed points over \(\bar k\), one above each point of \(B_t[2](\bar k)\). The quotient \(C_{m,t}/\langle w\rangle\) has genus \((m-1)/2\).

**Proof.** A fixed point of \(w\) lies over a point \(Z\) with \(-Z=Z\), that is, over \(Z\in B_t[2]\), which consists of \(O\) and the three points with \(y=0\). None of these is in the support of \(\operatorname{div}(f_t)\), because \(\pm R_t\) and \(\pm S_t\) are not \(2\)-torsion: \(R_t\ne-R_t\), and \(S_t\ne-S_t\) by the definition of \(U\). So \(f_t\) is a unit at \(Z\), and (2.2) at \(Z=-Z\) gives \(f_t(Z)^2=1\). The \(m\) points above \(Z\) are the solutions of \(Y^m=f_t(Z)\), and such a point is fixed by \(w\) exactly when \(Y=Y^{-1}\), that is, \(Y=\pm1\). Since \(m\) is odd, \((\pm1)^m=\pm1\), so exactly one of \(Y=1\), \(Y=-1\) satisfies \(Y^m=f_t(Z)\), namely \(Y=f_t(Z)\). This gives exactly one fixed point above each of the four points of \(B_t[2]\).

The quotient map \(C_{m,t}\to C_{m,t}/\langle w\rangle\) has degree two and is ramified exactly at the four fixed points, each with index two. Riemann–Hurwitz gives \(2m-2=2(2g'-2)+4\), so \(g'=(m-1)/2\). \(\square\)

For \(m=3\) the quotient \(D_t=C_{3,t}/\langle w\rangle\) has genus one. Its Jacobian is the elliptic curve \(A_t\) that starts the chain of congruences; Lesson 5 identifies its cohomology with a character piece of \(H^1(C_{n,t})\).

## 6. The moving-point family

For the geometry of Lessons 3 and 4 it is convenient to keep the elliptic curve fixed and move the point. Let
\[
\begin{aligned}
&E^\circ=\{R\in E:\ O,\,R,\,-R,\,[n]R,\,-[n]R\\
&\qquad\qquad\text{pairwise distinct}\},
\end{aligned}
\]
an open subset of \(E\) whose complement is finite. On the constant surface \(E\times E^\circ\to E^\circ\), with the parameter \(R\) in the second factor, the graphs of \(Z=\pm R\) and \(Z=\pm[n]R\) are disjoint sections. Lemma 4.1 and Proposition 4.2 apply verbatim: there is a rational function \(f_R(Z)\), normalized by \(f_R(O)=1\), with divisor \(([n]R)-(-[n]R)-n(R)+n(-R)\) on every fibre, and the normalization of \(E\times E^\circ\) in \(Y^m=f_R(Z)\) is a smooth proper family \(\mathcal C^E_m\to E^\circ\) with fibres \(C_{m,R}\).

**Proposition 6.1.** The map \(x\colon E^\circ\to\mathbb A^1\) takes values in \(U\) and is finite étale of degree two onto \(U\), and \(E^\circ=x^{-1}(U)\). For \(R\in E^\circ\) with \(t=x(R)\), the map
\[
\begin{gathered}
\phi_R\colon B_t\longrightarrow E,\\
(x,y)\longmapsto\bigl(x,\,y(R)\,y\bigr),\quad(6.1)
\end{gathered}
\]
is an isomorphism of elliptic curves with \(\phi_R(R_t)=R\), and it identifies \(f_t\) with \(f_R\) and \(C_{m,t}\) with \(C_{m,R}\). These identifications form an isomorphism over \(E^\circ\) between \(\mathcal C^E_m\) and the pullback of \(\mathcal C_m\) along \(x\).

**Proof.** A point \(R=(x_0,y_0)\in E^\circ\) is not \(2\)-torsion, because \(R\ne-R\), so \(y_0\ne0\) and \(h(x_0)=y_0^2\ne0\). For \((x,y)\in B_t\), \((y_0y)^2=h(t)y^2=h(x)\), so \(\phi_R\) maps \(B_t\) to \(E\); it is an isomorphism with inverse \((x,y)\mapsto(x,y/y_0)\), it fixes the point at infinity, and \(\phi_R(t,1)=(x_0,y_0)=R\). An isomorphism of elliptic curves preserving the origins is a group isomorphism, so \(\phi_R([m]R_t)=[m]R\) for every \(m\). Hence the five points \(O,\pm R_t,\pm S_t\) are pairwise distinct exactly when \(O,\pm R,\pm[n]R\) are, which gives \(E^\circ=x^{-1}(U)\). The map \(x\colon E\to\mathbb P^1\) has degree two and is ramified exactly at the points of \(E[2]\), none of which lies in \(E^\circ\); so it is finite étale of degree two over \(U\).

The function \(f_R\circ\phi_R\) on \(B_t\) has the divisor (2.1) and value \(1\) at \(O\), so it equals \(f_t\) by Lemma 2.1. Therefore \(\phi_R\) extends to an isomorphism \(C_{m,t}\to C_{m,R}\) with \(Y\mapsto Y\). The coefficient \(y(R)\) is a regular invertible function on \(E^\circ\), so the same formula defines the isomorphism of families. \(\square\)

The normalization \(f(O)=1\) is what makes this identification exact: no constant appears in the equation \(Y^m=f\), so no twist of the cover appears either (Remark 2.2).

## 7. Exercises

**7.1.** Let \(E\colon y^2=x^3-x\) over \(\mathbb Q\) and \(n=3\). Show that \(t=2\) lies in \(U\), and write down the five points \(O,\pm R_2,\pm S_2\) of \(B_2\colon6y^2=x^3-x\).

**7.2.** Show that the function \(f_t\) of Lemma 2.1 satisfies \(f_t(Q)\in\{1,-1\}\) for every \(Q\in B_t[2](\bar k)\), and that \(f_t(O)=1\) is consistent with this.

**7.3.** Let \(m\mid n\), \(m>1\), and suppose \(\mu_m\subset k\). Show that the fixed points of \(u_\zeta\) for \(\zeta\ne1\) are exactly the two points above \(S_t\) and \(-S_t\), and deduce the genus formula of Proposition 3.1 from the Lefschetz-free count: the cover \(C_{m,t}\setminus\{\text{2 points}\}\to B_t\setminus\{\pm S_t\}\) is a connected étale cover of degree \(m\).

**7.4.** Show that \(w\,u_\zeta\) is an involution for every \(\zeta\in\mu_m\), and count its fixed points.

## 8. Solutions

**7.1.** Here \(h(2)=6\ne0\), and \(R_2=(2,1)\) lies on \(6y^2=x^3-x\) since \(6=8-2\). On \(B_2\) the tangent line at \(R_2\) has slope \(\lambda\) with \(12y\lambda=3x^2-1\), so \(\lambda=11/12\). For \(6y^2=x^3-x\), the third intersection of a line \(y=\lambda x+c\) with the curve satisfies \(x_1+x_2+x_3=6\lambda^2\). So \(x([2]R_2)=6\cdot\frac{121}{144}-4=\frac{121}{24}-4=\frac{25}{24}\), and \(y([2]R_2)\)\(=-\bigl(1+\frac{11}{12}(\frac{25}{24}-2)\bigr)\)\(=-\bigl(1-\frac{253}{288}\bigr)\)\(=-\frac{35}{288}\). Then \(S_2=[3]R_2=[2]R_2+R_2\): the chord through \((2,1)\) and \((\frac{25}{24},-\frac{35}{288})\) has slope \(\lambda'=\frac{1+35/288}{2-25/24}=\frac{323/288}{23/24}=\frac{323}{276}\). Hence
\[
\begin{gathered}
x(S_2)=6\lambda'^2-2-\tfrac{25}{24}=\tfrac{2738}{529},\\
y(S_2)=-\tfrac{57387}{12167},
\end{gathered}
\]
with \(529=23^2\) and \(12167=23^3\). These points are affine with \(y\ne0\) (the \(2\)-torsion points of \(B_2\) are \(O\) and \((0,0),(\pm1,0)\)), so \(\pm R_2\) and \(\pm S_2\) are not \(2\)-torsion and \(R_2\), \(S_2\) are different from \(O\). Since \(x(S_2)\ne2\), also \(S_2\ne\pm R_2\). Hence the five points \(O\), \((2,\pm1)\) and \(\bigl(\frac{2738}{529},\pm\frac{57387}{12167}\bigr)\) are distinct and \(2\in U\).

**7.2.** A point \(Q\in B_t[2]\) satisfies \(Q=-Q\) and is not in the support of \(\operatorname{div}(f_t)\) (see the proof of Proposition 5.2), so (2.2) gives \(f_t(Q)=f_t(-Q)=f_t(Q)^{-1}\), that is, \(f_t(Q)^2=1\). For \(Q=O\) the normalization chooses the value \(+1\).

**7.3.** A point \((Z,Y)\) is fixed by \(u_\zeta\), \(\zeta\ne1\), exactly when \(\zeta Y=Y\) in the local description, which happens only where the fibre of the cover over \(Z\) has fewer than \(m\) points, that is, over the totally ramified points \(\pm S_t\) (Proposition 3.1(2)); the unique point above each is fixed by every rotation. Removing the two branch points, the cover is a connected étale cover of degree \(m\) of the twice-punctured torus \(B_t\setminus\{\pm S_t\}\), whose Euler characteristic over \(\mathbb C\) is \(0-2=-2\). The cover has Euler characteristic \(-2m\), and adding back the two points gives \(2-2g=-2m+2\), so \(g=m\). (This is the topological form of the same Riemann–Hurwitz count, valid after a complex embedding of \(k\).)

**7.4.** By (5.2), \((wu_\zeta)^2=w u_\zeta w u_\zeta=u_{\zeta^{-1}}u_\zeta=1\). The involution \(wu_\zeta\) acts by \((Z,Y)\mapsto(-Z,\zeta^{-1}Y^{-1})\), so its fixed points lie over \(B_t[2]\) and satisfy \(Y^2=\zeta^{-1}\), together with \(Y^m=f_t(Z)=\pm1\). Since \(m\) is odd, \(\zeta^{-1}\) has a unique square root \(\eta_0\) in \(\mu_m\), and the solutions are \(Y=\pm\eta_0\). Exactly one of them satisfies \(Y^m=f_t(Z)\), because \((\pm\eta_0)^m=\pm1\). So \(wu_\zeta\) also has exactly four fixed points, one above each point of \(B_t[2]\). The \(m\) involutions \(wu_\zeta\) are the reflections of the dihedral group generated by \(w\) and the rotations.

## Sources

- [OpenAI-030] OpenAI, *Modularity of elliptic curves over imaginary quadratic fields*, OpenAI Math Release preprint, 4 October 2026, Section 3.1 (the family and its dihedral action). https://github.com/openai/math/tree/main/preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026
