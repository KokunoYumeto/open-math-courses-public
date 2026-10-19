# An elliptic curve on the quadric

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The curve of genus 21 at the centre of the construction lies on the quadric surface \(\Sigma=\mathbb P^1\times\mathbb P^1\), where it has contact of order four with an elliptic curve \(\Gamma\) at six points. This lesson builds \(\Gamma\) and the data carried by the six points. Section 1 collects the facts about curves on \(\Sigma\) used throughout the course: cohomology, degrees, and the residue description of the canonical bundle. Section 2 constructs an explicit smooth curve \(\Gamma\) of bidegree \((2,2)\) on which the two rulings differ by a line bundle of exact order four. Section 3 attaches to \(\Gamma\) a nondegenerate quadratic form on a two-dimensional space of sections. Section 4 chooses six points of \(\Gamma\) and six vectors in that quadratic space with two normalizations that the gluing of vector fields in a later lesson requires.

**Prerequisites.** [*Derivations and the Lipman–Zariski problem*](derivations-and-the-lipman-zariski-problem.md) for the overall plan. From the course *Cohomology of quasi-coherent sheaves* (AG-QC): [*Cohomology of projective space*](course:AG-QC/cohomology-of-projective-space), Exercise 7.5 with its solution (cohomology of \(\mathcal O(a,b)\) on \(\mathbb P^1\times\mathbb P^1\) over any ring); [*Dualizing sheaves and Serre duality for projective schemes*](course:AG-QC/dualizing-sheaves-and-serre-duality-for-projective-schemes), Theorem 4.2 and Proposition 8.2. From the course *The abstract theory of ideals* (NOE-ABS): [*Algebraic functions of one variable: conductors and adjoints*](course:NOE-ABS/NOE-ABS-06), Theorem 4.3 (Riemann–Roch). From *Commutative algebra for geometry* (AG-CA): [*Kähler differentials*](course:AG-CA/kahler-differentials), Theorem 5.1; [*Smooth algebras over a field and the Jacobian criterion*](course:AG-CA/smooth-algebras-over-a-field-and-the-jacobian-criterion), Corollary 2.2.

Throughout, the ground field is \(\mathbb C\). A *curve* is a smooth connected projective curve. Line bundles on a curve are written additively: \(B+D\) means \(B\otimes\mathcal O(D)\) for a divisor \(D\), and \(mB\) means \(B^{\otimes m}\). For a line bundle \(B\), \(h^i(B)=\dim H^i(B)\). The canonical bundle of a curve \(X\) is \(K_X=\Omega^1_X\); by Proposition 8.2 of the lesson on dualizing sheaves it is the dualizing sheaf, so Theorem 4.2 there gives \(h^1(B)=h^0(K_X-B)\), and Riemann–Roch reads
\[
\begin{gathered}
h^0(B)-h^0(K_X-B)\\
=\deg B+1-g(X),\\
g(X)=h^1(\mathcal O_X)=h^0(K_X).
\end{gathered}
\]
Taking \(B=K_X\) gives \(\deg K_X=2g(X)-2\).

## 1. Curves on the quadric

Write \(\Sigma=\mathbb P^1\times\mathbb P^1\) with homogeneous coordinates \([X_0:X_1]\) and \([Y_0:Y_1]\), affine coordinates \(x=X_1/X_0\), \(y=Y_1/Y_0\), and \(\mathcal O(a,b)=\mathrm{pr}_1^*\mathcal O(a)\otimes\mathrm{pr}_2^*\mathcal O(b)\). For \(a,b\ge0\), the global sections of \(\mathcal O(a,b)\) are the bihomogeneous polynomials of bidegree \((a,b)\). In the chart \(X_0Y_0\ne0\) a section \(S\) is represented by its dehomogenization \(s(x,y)=S(1,x;1,y)\), a polynomial of degree at most \(a\) in \(x\) and at most \(b\) in \(y\).

Put \(V_0(d)=H^0(\mathbb P^1,\mathcal O(d))\) and \(V_1(d)=H^1(\mathbb P^1,\mathcal O(d))\), of dimensions \(\max(d+1,0)\) and \(\max(-d-1,0)\). Exercise 7.5 of the lesson on cohomology of projective space proves
\[
\begin{aligned}
&H^i(\Sigma,\mathcal O(a,b))\\
&\quad\cong\bigoplus_{p+q=i}V_p(a)\otimes V_q(b).
\end{aligned}
\tag{1.1}
\]

**Lemma 1.1 (vanishing on the quadric).** (a) \(H^0(\Sigma,\mathcal O(a,b))=0\) if \(a<0\) or \(b<0\). (b) \(H^1(\Sigma,\mathcal O(a,b))=0\) unless one of \(a,b\) is at least \(0\) and the other at most \(-2\); in particular it vanishes when \(a,b\ge-1\) and when \(a,b\le-1\). (c) \(H^2(\Sigma,\mathcal O(a,b))\) has dimension \((a+1)(b+1)\) if \(a,b\le-2\), and vanishes otherwise.

**Proof.** Read off (1.1): \(V_0(d)\ne0\) exactly when \(d\ge0\), and \(V_1(d)\ne0\) exactly when \(d\le-2\). \(\square\)

**Lemma 1.2 (curves on the quadric).** Let \(K\) be a section of \(\mathcal O(c,d)\), \(c,d\ge1\), whose zero scheme \(C=V(K)\) is smooth of dimension one. Then:

1. \(H^0(C,\mathcal O_C)=\mathbb C\) and \(h^1(\mathcal O_C)=(c-1)(d-1)\); in particular \(C\) is connected, hence irreducible, and \(g(C)=(c-1)(d-1)\).
2. \(\deg\bigl(\mathcal O(a,b)|_C\bigr)=ad+bc\).

**Proof.** (1) Multiplication by \(K\) gives the exact sequence \(0\to\mathcal O(-c,-d)\to\mathcal O_\Sigma\to\mathcal O_C\to0\). By Lemma 1.1, \(\mathcal O(-c,-d)\) has \(H^0=H^1=0\) and \(h^2=(c-1)(d-1)\), while \(\mathcal O_\Sigma\) has \(h^0=1\), \(H^1=H^2=0\). The cohomology sequence gives \(H^0(\mathcal O_C)\cong H^0(\mathcal O_\Sigma)=\mathbb C\) and \(H^1(\mathcal O_C)\cong H^2(\mathcal O(-c,-d))\). A decomposition of \(C\) into two disjoint nonempty closed subsets would give a nonconstant idempotent in \(H^0(\mathcal O_C)\), so \(C\) is connected. Its local rings are regular, hence domains, so two irreducible components cannot meet; being connected, \(C\) is irreducible.

(2) Both sides are additive in \((a,b)\), so it suffices to treat \((1,0)\) and \((0,1)\). The line \(\ell=V(X_0)\cong\mathbb P^1\) is not contained in \(C\): otherwise the irreducible curve \(C\) would equal \(\ell\), and \(K\) would be a unit multiple of a power of \(X_0\), of bidegree \((m,0)\), while \(d\ge1\). So \(K|_\ell\) is a nonzero binary form of degree \(d\) in \(Y_0,Y_1\), and \(X_0|_C\) is a nonzero section of \(\mathcal O(1,0)|_C\). At each point the order of vanishing of a section of a line bundle on the curve \(C\) is the length of the quotient of the local ring by it, so the degree of the divisor of \(X_0|_C\) is the length of
\[
\mathcal O_C/(X_0)=\mathcal O_\Sigma/(K,X_0)=\mathcal O_\ell/(K|_\ell),
\]
which is the number \(d\) of zeros of \(K|_\ell\) counted with multiplicity. The same argument with \(V(Y_0)\) gives \(\deg\mathcal O(0,1)|_C=c\). \(\square\)

**Residues.** For sections \(S\) of \(\mathcal O(c-2,d-2)\) and \(K\neq0\) of \(\mathcal O(c,d)\), let \(S\varepsilon/K\) denote the rational two-form on \(\Sigma\) equal to \(s\,dx\wedge dy/k\) in the chart \(X_0Y_0\ne0\), where \(s,k\) are the dehomogenizations. In the chart with coordinates \(x'=1/x\) and \(y\), the dehomogenizations are \(s'=x'^{c-2}s\) and \(k'=x'^{c}k\), and \(dx=-x'^{-2}dx'\), so
\[
\frac{s\,dx\wedge dy}{k}=-\frac{s'\,dx'\wedge dy}{k'} ;
\]
the charts with \(y'=1/y\) behave in the same way. Hence the poles of \(S\varepsilon/K\) lie on \(V(K)\). The notation records that the two-form \(\varepsilon\), equal to \(dx\wedge dy\) in the first chart, has no zeros and has poles of order two along \(V(X_0)\) and \(V(Y_0)\); in particular \(K_\Sigma\cong\mathcal O(-2,-2)\).

Let \(C\) be a smooth curve on a smooth surface and \(\psi\) a rational two-form near a point of \(C\) such that \(k\psi\) is regular, where \(k\) is a local equation of \(C\) with \(dk\ne0\) along \(C\). Writing \(k\psi=dk\wedge\alpha+k\beta\) with regular forms \(\alpha,\beta\) (possible because \(dk\) is part of a local basis of one-forms), the *residue* \(\operatorname{Res}_C\psi\) is the restriction of \(\alpha\) to \(C\). The normal differential stands first: \(\operatorname{Res}_{y=0}\bigl((dy/y)\wedge dz\bigr)=dz\).

The residue is well defined. If \(dk\wedge\alpha=k\beta'\) for regular \(\alpha,\beta'\), then at each point of \(C\) the two-form \(dk\wedge\alpha\) vanishes, so \(\alpha\) is a multiple of \(dk\) pointwise along \(C\), and its restriction to \(C\) is zero. If \(k\) is replaced by \(uk\) with \(u\) a unit, then
\[
\begin{aligned}
uk\psi&=u\,dk\wedge\alpha+uk\beta\\
&=d(uk)\wedge\alpha\\
&\quad+uk\bigl(\beta-u^{-1}du\wedge\alpha\bigr),
\end{aligned}
\]
so the same \(\alpha\) serves for the new equation.

**Lemma 1.3 (adjunction).** In the situation of Lemma 1.2, the map \(S|_C\mapsto\operatorname{Res}_C(S\varepsilon/K)\) is an isomorphism of line bundles
\[
\mathcal O(c-2,d-2)|_C\xrightarrow{\ \sim\ }K_C .
\]
In the chart \(X_0Y_0\ne0\) it is given by
\[
\begin{aligned}
&\operatorname{Res}_C\Bigl(\frac{s\,dx\wedge dy}{k}\Bigr)\\
&\quad=-\frac{s\,dx}{k_y}=\frac{s\,dy}{k_x},
\end{aligned}
\tag{1.2}
\]
the first expression where \(k_y\ne0\) and the second where \(k_x\ne0\). In particular \(\deg K_C=(c-2)d+(d-2)c\), which agrees with \(2g(C)-2\).

**Proof.** If \(S\) vanishes on \(C\), then \(S=KS'\) locally and \(S\varepsilon/K=S'\varepsilon\) is regular, with residue zero; so the map is defined on \(\mathcal O(c-2,d-2)|_C\). In the chart, \(dk\wedge dx=k_y\,dy\wedge dx\), so where \(k_y\ne0\),
\[
\frac{s\,dx\wedge dy}{k}=\frac{dk}{k}\wedge\Bigl(-\frac{s\,dx}{k_y}\Bigr),
\]
which gives the first expression; the second follows in the same way from \(dk\wedge dy=k_x\,dx\wedge dy\). On \(C\) the relation \(k_x\,dx+k_y\,dy=0\) holds in \(\Omega^1_C\) (Theorem 5.1 of the lesson on Kähler differentials), so the two expressions agree where both are defined. By the Jacobian criterion (Corollary 2.2 of the lesson on smooth algebras), \(k_x\) and \(k_y\) have no common zero on the smooth curve \(C\). Where \(k_y\ne0\), the same Jacobian presentation shows that \(\Omega^1_C\) is free on \(dx\), so \(-s\,dx/k_y\) generates \(\Omega^1_C\) exactly where \(s\ne0\); similarly where \(k_x\ne0\). In the other charts the same computation applies to \(\pm s'\,dx'\wedge dy/k'\). Hence the map is an isomorphism of line bundles. The degree follows from Lemma 1.2(2). \(\square\)

## 2. A curve of bidegree (2,2) with a torsion line bundle

**Lemma 2.1 (smoothness of a (2,2) curve).** Let \(G\) be a section of \(\mathcal O(2,2)\), written
\[
G=\alpha(X)\,Y_0^2+\beta(X)\,Y_0Y_1+\gamma(X)\,Y_1^2
\]
with binary quadratic forms \(\alpha,\beta,\gamma\) in \(X=(X_0,X_1)\), and let \(\delta=\beta^2-4\alpha\gamma\), a binary quartic form. If \(\delta\) has four distinct zeros on \(\mathbb P^1\), then \(V(G)\) is smooth. Moreover, \(V(G)\) meets the fibre \(\{x\}\times\mathbb P^1\) in one point if \(\delta(x)=0\) and in two points otherwise.

**Proof.** Fix \(x\in\mathbb P^1\) and let \(q_x(Y)=\alpha(x)Y_0^2+\beta(x)Y_0Y_1+\gamma(x)Y_1^2\), defined up to a nonzero factor. If \(q_x\) were identically zero, then \(\alpha,\beta,\gamma\) would all vanish at \(x\), and \(\delta\) would vanish to order at least two there; so \(q_x\ne0\), and \(V(G)\cap(\{x\}\times\mathbb P^1)\) is the zero set of the binary quadratic \(q_x\), with discriminant \(\delta(x)\).

If \(\delta(x)\ne0\), \(q_x\) has two simple zeros, and at each of them the derivative of \(G\) along the fibre is nonzero, so \(V(G)\) is smooth there.

If \(\delta(x)=0\), \(q_x\) has a double zero \(y_0\). Choose a local coordinate \(t\) on the first factor with \(t(x)=0\), and an affine coordinate \(s\) on the second factor with \(s(y_0)=0\) and \(s=\infty\) not a zero of \(q_x\). Near \((x,y_0)\), in a trivialization, \(G=a(t)+b(t)s+c(t)s^2\) with \(a(0)=b(0)=0\) and \(c(0)\ne0\). The discriminant \(b^2-4ac\) equals \(\delta\) times a nowhere vanishing function, because changing the fibre coordinate by a Möbius transformation and the trivialization by a unit multiplies the discriminant of a binary quadratic by a nonzero factor. Differentiating at \(t=0\),
\[
\frac{d}{dt}\bigl(b^2-4ac\bigr)\Big|_{t=0}=-4a'(0)c(0).
\]
Since \(x\) is a simple zero of \(\delta\), \(a'(0)\ne0\), so \(\partial G/\partial t\ne0\) at \((x,y_0)\), and \(V(G)\) is smooth there. \(\square\)

The fibres over the four zeros of \(\delta\) are the four points where the projection \(V(G)\to\mathbb P^1\) to the first factor is ramified: at such a point, \(s\) is a local coordinate on the curve and \(t=-c(0)s^2/a'(0)+O(s^3)\).

**The zigzag curve.** Consider the eight points
\[
\begin{gathered}
(0,0),\ (0,1),\ (1,1),\ (1,2),\\
(2,2),\ (2,3),\ (3,3),\ (3,0)
\end{gathered}
\]
of the chart \(X_0Y_0\ne0\): a closed path on the grid \(\{0,1,2,3\}^2\) that alternates vertical and horizontal steps. They lie on the curve \(\Gamma=V(G)\), where \(G\) has dehomogenization
\[
\begin{aligned}
g(x,y)={}&x^2y^2-5x^2y\\
&+3x^2-xy^2\\
&+11xy-9x\\
&-3y^2+3y .
\end{aligned}
\tag{2.1}
\]
On the grid lines,
\[
\begin{aligned}
g(0,y)&=-3y(y-1),\\
g(1,y)&=-3(y-1)(y-2),\\
g(2,y)&=-(y-2)(y-3),\\
g(3,y)&=3y(y-3),\\
g(x,0)&=3x(x-3),\\
g(x,1)&=-x(x-1),\\
g(x,2)&=-3(x-1)(x-2),\\
g(x,3)&=-3(x-2)(x-3).
\end{aligned}
\]
Each of these has degree exactly two, so it has no zero at infinity, and each grid line meets \(\Gamma\) exactly in the two marked points on it. Writing \(g=A(x)y^2+B(x)y+C(x)\) with \(A=x^2-x-3\), \(B=-5x^2+11x+3\), \(C=3x^2-9x\), the quartic \(\delta\) of Lemma 2.1 has dehomogenization
\[
\begin{gathered}
\delta(x)=B^2-4AC\\
=13x^4-62x^3+91x^2-42x+9 .
\end{gathered}
\]
Its leading coefficient is \(13\ne0\), so \(\delta\) does not vanish at \(x=\infty\), and its discriminant is \(2^8\cdot3^8\cdot7\ne0\), so its four zeros in \(\mathbb C\) are distinct. By Lemma 2.1, \(\Gamma\) is smooth. By Lemma 1.2, \(\Gamma\) is irreducible of genus \((2-1)(2-1)=1\). (The factorizations and the discriminant are finite exact computations; the check script of this course verifies them and, independently, that \(g,g_x,g_y\) generate the unit ideal in each of the four charts.)

**Switches.** Put \(F=\mathcal O(1,0)|_\Gamma\) and \(S=\mathcal O(0,1)|_\Gamma\), both of degree two by Lemma 1.2(2). For \(p\in\Gamma\), the vertical line through \(p\) is the zero set of a section of \(\mathcal O(1,0)\); its restriction to \(\Gamma\) has a divisor of degree two containing \(p\), which we write \(p+\iota_F(p)\). This defines a map \(\iota_F\) on the points of \(\Gamma\) with \(\iota_F^2=\mathrm{id}\); its fixed points are the four ramification points of the first projection. Define \(\iota_S\) in the same way with horizontal lines, and put
\[
T=\iota_S\circ\iota_F .
\]
By construction \(p+\iota_F(p)\) is a divisor of \(F\) and \(p+\iota_S(p)\) a divisor of \(S\) for every \(p\).

**Lemma 2.2.** On a curve \(X\) of genus one, \(K_X\cong\mathcal O_X\), and for points \(p,q\) one has \(\mathcal O_X(p)\cong\mathcal O_X(q)\) only if \(p=q\). A line bundle of degree \(e>0\) has \(h^0=e\); a line bundle of degree \(0\) has \(h^0=1\) if it is trivial and \(h^0=0\) otherwise; a line bundle of negative degree has \(h^0=0\).

**Proof.** \(\deg K_X=0\) and \(h^0(K_X)=1\); a nonzero section of a degree-zero line bundle has no zeros, so it trivializes the bundle. Hence \(K_X\cong\mathcal O_X\). A line bundle of negative degree has no nonzero section, since the divisor of a section is effective. For \(\deg B=e>0\), Riemann–Roch gives \(h^0(B)=e+h^0(-B)=e\). For \(\deg B=0\), a nonzero section trivializes \(B\). Finally \(h^0(\mathcal O_X(p))=1\), so if \(p\ne q\) and \(\mathcal O_X(p)\cong\mathcal O_X(q)\), a rational function with divisor \(q-p\) would be a nonconstant section of \(\mathcal O_X(p)\), a contradiction. \(\square\)

**Lemma 2.3 (switches and torsion).** Let \(D_0=S-F\). For every \(p\in\Gamma\):

1. \(\mathcal O_\Gamma(T(p)-p)\cong D_0\), and \(\mathcal O_\Gamma(T^k(p)-p)\cong kD_0\) for \(k\ge1\).
2. \(kD_0\cong\mathcal O_\Gamma\) if and only if \(T^k(p)=p\); in particular, whether \(T^k(p)=p\) does not depend on \(p\).
3. \(\iota_FT\iota_F=T^{-1}\).

**Proof.** (1) \(p+\iota_F(p)\) is a divisor of \(F\) and \(\iota_F(p)+\iota_S(\iota_F(p))\) a divisor of \(S\); subtracting, \(T(p)-p\) is a divisor of \(S-F\). Summing over \(T^i(p)\), \(0\le i<k\), gives the second statement. (2) If \(T^k(p)=p\), then \(kD_0\cong\mathcal O_\Gamma(0)\). If \(T^k(p)\ne p\) and \(kD_0\) were trivial, then \(\mathcal O_\Gamma(T^k(p))\cong\mathcal O_\Gamma(p)\), contradicting Lemma 2.2. (3) Since \(\iota_F^2=\iota_S^2=\mathrm{id}\), \(\iota_FT\iota_F=\iota_F\iota_S=T^{-1}\). \(\square\)

**Proposition 2.4.** On the zigzag curve, \(D_0=S-F\) has exact order four. Explicitly, the sections
\[
\begin{gathered}
P_X=\prod_{i=0}^3(X_1-iX_0),\\
P_Y=\prod_{i=0}^3(Y_1-iY_0)
\end{gathered}
\]
of \(\mathcal O(4,0)\) and \(\mathcal O(0,4)\) restrict to sections of \(4F\) and \(4S\) with the same divisor, the eight zigzag points, each simple, and
\[
\zeta:4F\xrightarrow{\ \sim\ }4S,\qquad \zeta(P_X|_\Gamma)=P_Y|_\Gamma,
\]
is an isomorphism.

**Proof.** From the factorizations on the grid lines,
\[
\begin{gathered}
\iota_F(0,0)=(0,1),\ \iota_S(0,1)=(1,1),\\
\iota_F(1,1)=(1,2),\ \iota_S(1,2)=(2,2),
\end{gathered}
\]
\[
\begin{gathered}
\iota_F(2,2)=(2,3),\ \iota_S(2,3)=(3,3),\\
\iota_F(3,3)=(3,0),\ \iota_S(3,0)=(0,0).
\end{gathered}
\]
So \(T\) moves \((0,0)\) to \((1,1)\), \((2,2)\), \((3,3)\) and back to \((0,0)\): \(T^4(0,0)=(0,0)\) and \(T^2(0,0)=(2,2)\ne(0,0)\). By Lemma 2.3(2), \(4D_0\) is trivial and \(2D_0\) is not, so \(D_0\) has order exactly four. The section \(P_X|_\Gamma\) vanishes on the four vertical grid lines, hence at the eight zigzag points; since \(\deg4F=8\), these are all its zeros and each is simple. The same holds for \(P_Y|_\Gamma\). Two sections of line bundles with the same divisor determine an isomorphism carrying one to the other. \(\square\)

**The bundle identities.** Define on \(\Gamma\)
\[
\Delta=2D_0,\quad \Phi=F+\Delta,\quad M=3\Phi .
\]
Thus \(\Delta\) is nontrivial with \(2\Delta\cong\mathcal O_\Gamma\). Every line bundle in this list, and every restriction \(\mathcal O(a,b)|_\Gamma=aF+bS\), is of the form \(aF+bS\) with \(a,b\in\mathbb Z\): \(\Delta=-2F+2S\), \(\Phi=-F+2S\), \(M=-3F+6S\). We fix once and for all the isomorphisms
\[
\begin{aligned}
&\zeta^m:\ aF+bS\\
&\quad\xrightarrow{\ \sim\ }(a-4m)F\\
&\quad+(b+4m)S\quad(m\in\mathbb Z)
\end{aligned}
\tag{2.2}
\]
induced by \(\zeta\). They are compatible with tensor products and with composition, \(\zeta^m\zeta^{m'}=\zeta^{m+m'}\). Every identification below between bundles of this form is one of them. With \(\Gamma|_\Gamma=\mathcal O(2,2)|_\Gamma=2F+2S\), they give
\[
\begin{gathered}
\Gamma|_\Gamma=4F+\Delta,\qquad M=3F+\Delta,\\
2M=6F,\qquad 2\Phi=2F,
\end{gathered}
\]
\[
\begin{gathered}
4M=(2\Gamma+4F)|_\Gamma,\\
2M-(\Gamma+F)|_\Gamma=\Phi,\\
(\Gamma+2F)|_\Gamma-2M=\Delta .
\end{gathered}
\tag{2.3}
\]
For instance \(4M=-12F+24S\) and \((2\Gamma+4F)|_\Gamma=8F+4S\) are identified by \(\zeta^{-5}\). In (2.3), \(\Gamma\) and \(F\) also denote the line bundles \(\mathcal O(2,2)\) and \(\mathcal O(1,0)\) on \(\Sigma\), a notation used from here on.

## 3. The quadratic form

**The logarithmic form.** Put
\[
\begin{gathered}
\Omega=\frac{\varepsilon}{G},\qquad \Omega=\frac{dx\wedge dy}{g}\\
\text{in the chart }X_0Y_0\ne0 .
\end{gathered}
\]
By Section 1, \(\Omega\) is a rational two-form on \(\Sigma\) without zeros and with a simple pole exactly along \(\Gamma\) (the case \((c,d)=(2,2)\), \(S=1\) of the discussion before Lemma 1.3). Its residue
\[
\omega=\operatorname{Res}_\Gamma\Omega=-\frac{dx}{g_y}=\frac{dy}{g_x}
\]
is a nowhere vanishing differential on \(\Gamma\), by Lemma 1.3 with \(\mathcal O(0,0)|_\Gamma=\mathcal O_\Gamma\).

**The Wronskian section.** Let \(u=(u_1,u_2)\) be a basis of \(H^0(\Sigma,\mathcal O(1,0))\) obtained from \((X_0,X_1)\) by a matrix of determinant one; the next lesson fixes a convenient choice. Restricting to \(\Gamma\), put
\[
\begin{aligned}
\eta_\Gamma&=u_1\,du_2-u_2\,du_1\\
&\in H^0(\Gamma,K_\Gamma+2F).
\end{aligned}
\]
This means: in a local frame \(e\) of \(F\), with \(u_i=f_ie\), the section is \((f_1\,df_2-f_2\,df_1)\,e^2\). It does not depend on the frame, since replacing \(e\) by \(he\) replaces \(f_i\) by \(f_i/h\), and
\[
\begin{aligned}
&(f_1/h)\,d(f_2/h)-(f_2/h)\,d(f_1/h)\\
&\qquad=h^{-2}(f_1\,df_2-f_2\,df_1).
\end{aligned}
\]
Replacing \(u\) by \(Au\), \(A\in GL_2(\mathbb C)\), multiplies \(\eta_\Gamma\) by \(\det A\), so \(\eta_\Gamma\) is the same for all admissible \(u\) and may be computed with \(u=(X_0,X_1)\): in the frame \(X_0\), \(f=(1,x)\) and \(\eta_\Gamma=dx\cdot X_0^2\).

**Lemma 3.1.** The section \(\eta_\Gamma\) vanishes exactly at the four ramification points \(r_1,\ldots,r_4\) of the first projection \(\Gamma\to\mathbb P^1\), each simply. In the chart \(X_0Y_0\ne0\),
\[
-\frac{\eta_\Gamma}{\omega}=g_y\cdot X_0^2 .
\]

**Proof.** By Lemma 1.3, \(\omega=-dx/g_y\) where \(g_y\ne0\), so \(\eta_\Gamma/\omega=-g_yX_0^2\) on that set, and by continuity on the whole chart. Its zeros in the chart are the points of \(\Gamma\) with \(g_y=0\), which are the ramification points of the first projection lying in the chart. At such a point, in the coordinates of the proof of Lemma 2.1, \(g\) is a unit times \(G=a(t)+b(t)s+c(t)s^2\) and \(s\) is a Möbius function of \(y\), so along \(\Gamma\), where \(G=0\), the derivative \(g_y\) is a unit times \(\partial G/\partial s\). There \(s\) is a local coordinate on \(\Gamma\), \(t=O(s^2)\) along \(\Gamma\), and \(\partial G/\partial s=b(t)+2c(t)s\), which is \(2c(0)s+O(s^2)\), a simple zero. The section \(\eta_\Gamma\) does not depend on a chart, and the same computation in the charts with \(x'=1/x\) or \(y'=1/y\), where \(\eta_\Gamma/\omega\) is \(\pm\) the derivative of the local equation along the fibre times a frame, covers the remaining ramification points. The total number of zeros is \(\deg(K_\Gamma+2F)=4\), so these are all. \(\square\)

**The Φ-map.** By Lemma 2.2, \(h^0(\Gamma,\Phi)=2\), and for each \(q\in\Gamma\) the sections of \(\Phi\) vanishing at \(q\) form a line, since \(h^0(\Phi-q)=1\). The divisor of such a section is \(q+\iota_\Phi(q)\) for a unique point \(\iota_\Phi(q)\). In particular \(\Phi\) has no base point, and it defines a morphism of degree two
\[
\begin{gathered}
\varphi_\Phi:\Gamma\to\mathbb P\bigl(H^0(\Gamma,\Phi)^*\bigr)\cong\mathbb P^1,\\
q\mapsto[\mathrm{ev}_q],
\end{gathered}
\]
where \(\mathrm{ev}_q(\sigma)=\sigma(q)/e(q)\) for a local frame \(e\) of \(\Phi\) at \(q\); changing \(e\) rescales \(\mathrm{ev}_q\). The fibre through \(q\) is \(\{q,\iota_\Phi(q)\}\). The ramification points of \(\varphi_\Phi\), where \(\iota_\Phi(q)=q\), are finite in number, being the zeros of the nonzero differential of \(\varphi_\Phi\); their images are the *branch values*.

**Lemma 3.2.** \(\iota_\Phi=T^2\circ\iota_F\). The four ramification points of the first projection form two fibres \(\{r,T^2(r)\}\) of \(\varphi_\Phi\), and \(\varphi_\Phi\) is unramified at them.

**Proof.** By Lemma 2.3(1), \(p+T^2\iota_F(p)\) is a divisor of \(F+2D_0=\Phi\), since \(p+\iota_F(p)\) is a divisor of \(F\). By uniqueness of the residual point, \(\iota_\Phi(p)=T^2\iota_F(p)\). For a fixed point \(r\) of \(\iota_F\), \(\iota_\Phi(r)=T^2(r)\), which differs from \(r\) because \(2D_0\) is nontrivial (Lemma 2.3(2)). By Lemma 2.3(3), \(\iota_FT^2\iota_F=T^{-2}\), and \(T^{-2}=T^2\) because \(T^4=\mathrm{id}\); hence \(\iota_F(T^2r)=T^2\iota_F(r)=T^2(r)\), so \(T^2(r)\) is again a fixed point of \(\iota_F\). \(\square\)

An element \(\sigma=\sum_i\sigma_i\otimes\tau_i\) of \(\operatorname{Sym}^2H^0(\Gamma,\Phi)\) defines the quadratic form \(Q_\sigma(\lambda)=\sum_i\lambda(\sigma_i)\lambda(\tau_i)\) on \(H^0(\Gamma,\Phi)^*\), and has the image \(m(\sigma)=\sum_i\sigma_i\tau_i\in H^0(\Gamma,2\Phi)\) under multiplication. For every \(q\) and every local frame \(e\) of \(\Phi\) at \(q\),
\[
Q_\sigma(\mathrm{ev}_q)=\frac{m(\sigma)(q)}{e(q)^2}.
\tag{3.1}
\]

**Proposition 3.3 (the quadratic form).** There is a unique \(\sigma\in\operatorname{Sym}^2H^0(\Gamma,\Phi)\) with
\[
\begin{aligned}
m(\sigma)&=-\frac{\eta_\Gamma}{\omega}\\
&\in H^0(\Gamma,2F)\\
&=H^0(\Gamma,2\Phi),
\end{aligned}
\tag{3.2}
\]
the equality of section spaces being \(\zeta\) from (2.3). The quadratic form \(Q=Q_\sigma\) on \(H^0(\Gamma,\Phi)^*\) is nondegenerate, and a direction \([\mathrm{ev}_q]\) is isotropic exactly when \(q\) is one of the ramification points \(r_1,\ldots,r_4\) of the first projection.

**Proof.** The map \(m\) is injective: identifying \(\operatorname{Sym}^2H^0(\Gamma,\Phi)\) with the binary quadratic forms on \(H^0(\Gamma,\Phi)^*\), \(m(\sigma)\) is the pullback of \(Q_\sigma\) along \(\varphi_\Phi\), and \(\varphi_\Phi\) is surjective onto \(\mathbb P^1\), being a nonconstant morphism from an irreducible projective curve. By Lemma 3.2, the divisor \(r_1+r_2+r_3+r_4\) of \(-\eta_\Gamma/\omega\) (Lemma 3.1) is the pullback along \(\varphi_\Phi\) of \(a+b\), where \(a\ne b\) are the images of the two fibres, and each fibre is reduced. Let \(\sigma_0\) correspond to a binary quadratic form with simple zeros at \(a\) and \(b\). Then \(m(\sigma_0)\) and \(-\eta_\Gamma/\omega\) are sections of \(2\Phi\) with the same divisor, so their ratio is a nowhere vanishing regular function on the connected projective curve \(\Gamma\), a nonzero constant \(c\). Then \(\sigma=c\sigma_0\) satisfies (3.2), and it is unique by injectivity. Its binary quadratic form has two distinct zeros, so \(Q\) is nondegenerate. By (3.1), \(Q(\mathrm{ev}_q)=0\) exactly when \(-\eta_\Gamma/\omega\) vanishes at \(q\). \(\square\)

The polar form of \(Q\) is written
\[
\begin{gathered}
v\cdot w=\tfrac12\bigl(Q(v+w)-Q(v)-Q(w)\bigr),\\
v^2=Q(v).
\end{gathered}
\]

## 4. Six points with prescribed data

Suppose six vectors \(w_1,\ldots,w_6\) and their sum \(w\) satisfy \(w_j^2+w_j\cdot w=1\) for each \(j\). Summing over \(j\),
\[
\sum_{j=1}^6\bigl(w_j^2-1\bigr)=-\sum_jw_j\cdot w=-w^2 .
\]
The curve of the next lesson carries a line bundle \(L\) of degree \(10\); the choice \(w^2=90=9\deg L\) will make this total equal to \(-9\deg L\), the value that a later obstruction computation requires, while all six pointwise normalizations are kept.

**Lemma 4.1 (six vectors).** In a two-dimensional nondegenerate quadratic space over \(\mathbb C\) one can choose three distinct nonisotropic directions, avoiding any prescribed finite set of directions, and nonzero vectors \(w_1,\ldots,w_6\), using each of the three directions twice with the two vectors in each pair equal, such that
\[
\begin{gathered}
w=\sum_{j=1}^6w_j,\quad w^2=90,\\
w_j^2+w_j\cdot w=1\\
(1\le j\le6).
\end{gathered}
\tag{4.1}
\]

**Proof.** Choose coordinates with \(Q(x,y)=xy\), so that \((x,y)\cdot(x',y')=(xy'+yx')/2\). Put
\[
\begin{gathered}
h=\sqrt{90},\quad R=\sqrt{1+h^2/4},\quad b=\frac{2h}{R},\\
d(z)=\Bigl(Rz-\frac h2,\ \frac Rz-\frac h2\Bigr)\quad(z\ne0).
\end{gathered}
\]
Expanding,
\[
\begin{aligned}
&d(z)^2+d(z)\cdot(h,h)\\
&=\Bigl(R^2-\frac{hR}2\bigl(z+z^{-1}\bigr)+\frac{h^2}4\Bigr)\\
&\quad+\Bigl(\frac{hR}2\bigl(z+z^{-1}\bigr)-\frac{h^2}2\Bigr)\\
&=R^2-\frac{h^2}4=1 .
\end{aligned}
\]
For a nonzero complex number \(\lambda\), let \(z_1,z_2,z_3\) be the roots of
\[
X^3-bX^2+b\lambda X-\lambda=0 .
\]
By Vieta's formulas, \(\sum_iz_i=b\), \(\sum_{i<j}z_iz_j=b\lambda\) and \(z_1z_2z_3=\lambda\), so \(\sum_iz_i^{-1}=b\lambda/\lambda=b\). Hence
\[
\begin{aligned}
\sum_{i=1}^3d(z_i)&=\Bigl(Rb-\frac{3h}2,\ Rb-\frac{3h}2\Bigr)\\
&=\Bigl(\frac h2,\ \frac h2\Bigr),
\end{aligned}
\]
because \(Rb=2h\). Take \(w_{2i-1}=w_{2i}=d(z_i)\). Then \(w=(h,h)\), \(w^2=h^2=90\), and \(w_j^2+w_j\cdot w=1\) by the expansion.

It remains to choose \(\lambda\) so that the three directions are distinct and nonisotropic. As \(\lambda\to0\) the cubic tends to \(X^2(X-b)\): two roots tend to \(0\) and one to \(b\). The discriminant of the cubic, a polynomial in \(\lambda\), has no constant term and linear coefficient \(-4b^3\ne0\), so the roots are distinct for all small \(\lambda\ne0\). The direction of \(d(z)\) is given by the ratio of its entries,
\[
\rho(z)=\frac{Rz-h/2}{R/z-h/2}=\frac{z(Rz-h/2)}{R-hz/2},
\]
which is holomorphic near \(0\) with \(\rho(0)=0\) and \(\rho'(0)=-h/(2R)\ne0\). So \(\rho\) is injective near \(0\), and the two small roots give distinct directions, both near the direction \(\rho=0\). At \(z=b\) the entries of \(d(b)\) are \(Rb-h/2=3h/2\) and \(R/b-h/2=(R^2-h^2)/(2h)\), that is \((1-3h^2/4)/(2h)\), both nonzero, so the third direction tends to a direction with \(\rho\ne0\), distinct from the other two for small \(\lambda\). A vector \((x,y)\) is isotropic exactly when \(x=0\) or \(y=0\); the entries of \(d(z_i)\) tend to nonzero limits or to infinity, so the three vectors are nonisotropic for small \(\lambda\ne0\).

Finally, for \(\nu\in\mathbb C^*\) the map \((x,y)\mapsto(\nu x,\nu^{-1}y)\) is an isometry; applied to all six vectors it preserves (4.1) and multiplies every ratio \(\rho\) by \(\nu^2\). A prescribed finite set of directions excludes only finitely many values of \(\nu^2\) for each of the three directions, so a suitable \(\nu\) avoids it. \(\square\)

**The marked points.** Apply Lemma 4.1 to \((H^0(\Gamma,\Phi)^*,Q)\), excluding the branch values of \(\varphi_\Phi\). Each of the three directions is \([\mathrm{ev}_q]\) for exactly two distinct points of \(\Gamma\), a fibre \(\{q,\iota_\Phi(q)\}\) of \(\varphi_\Phi\). Label the six points \(q_1,\ldots,q_6\) so that \([w_j]=[\mathrm{ev}_{q_j}]\), and put
\[
Z=q_1+\cdots+q_6 .
\tag{4.2}
\]
Each pair \(q_{2i-1}+q_{2i}\) is a divisor of \(\Phi\), so \(Z\) is a divisor of \(3\Phi=M\). Choose a section \(\beta\) of \(M\) with divisor \(Z\). The directions are nonisotropic, so by Proposition 3.3 no \(q_j\) is a ramification point of the first projection. The first coordinates \(x(q_j)\) are not all equal, because a vertical line meets \(\Gamma\) in at most two points.

**Summary.** The smooth curve \(\Gamma\subset\Sigma\) of bidegree \((2,2)\) and genus one carries: the line bundles \(F,S,D_0,\Delta,\Phi,M\) with the identifications (2.2) and (2.3); the logarithmic form \(\Omega\) and its residue \(\omega\); the nondegenerate quadratic form \(Q\) of Proposition 3.3; six distinct points \(q_1,\ldots,q_6\), none a ramification point of the first projection, with \(Z\) a divisor of \(M\) cut out by \(\beta\); and nonzero vectors \(w_j\in H^0(\Gamma,\Phi)^*\) in the directions \([\mathrm{ev}_{q_j}]\), using three distinct directions, satisfying (4.1).

## 5. Exercises

**5.1** (easy). Verify that the eight zigzag points lie on \(g=0\), and derive the factorizations of \(g\) on the eight grid lines.

**5.2** (medium). Prove the converse in Lemma 2.1: if \(\delta\) has a multiple zero, or vanishes identically, then \(V(G)\) is singular.

**5.3** (medium). Let \(\Gamma'\subset\Sigma\) be a smooth curve of bidegree \((2,2)\) passing through the six points \((x_0,y_0),(x_0,y_1),(x_1,y_1)\), \((x_1,y_2),(x_2,y_2),(x_2,y_0)\), with \(x_0,x_1,x_2\) distinct and \(y_0,y_1,y_2\) distinct. Show that \(\mathcal O(-1,1)|_{\Gamma'}\) has exact order three.

**5.4** (medium). Show that \(\iota_\Phi\) has exactly four fixed points, and that a point \(p\) is fixed by \(\iota_\Phi\) if and only if \(\iota_F(p)=T^2(p)\).

**5.5** (medium). Check directly that the residue \(\omega\) of \(\Omega\) has no zero at the points of \(\Gamma\) with \(x=\infty\), using the chart \((x',y)\), \(x'=1/x\).

## 6. Solutions

**5.1.** Substitution gives \(g=0\) at each point. For example,
\[
\begin{aligned}
g(0,y)&=-3y^2+3y=-3y(y-1),\\
g(x,1)&=(1-5+3)x^2\\
&\quad+(-1+11-9)x+(-3+3)\\
&=-x^2+x=-x(x-1),\\
g(3,y)&=(9-3-3)y^2\\
&\quad+(-45+33+3)y+(27-27)\\
&=3y^2-9y=3y(y-3);
\end{aligned}
\]
the others are similar.

**5.2.** Suppose first that \(q_x\equiv0\) for some \(x\). Then \(\alpha,\beta,\gamma\) vanish at \(x\), so near the fibre \(G=tH\), where \(t\) is a local coordinate on the first factor vanishing at \(x\) and \(H\) restricts to the fibre as a binary quadratic form \(H_0\), possibly zero. Along the fibre, \(\partial G/\partial s=tH_s=0\) and \(\partial G/\partial t=H\). Every binary quadratic form over \(\mathbb C\), including zero, has a zero on \(\mathbb P^1\); at such a point of the fibre both partial derivatives vanish, so \(V(G)\) is singular there.

Otherwise \(q_x\ne0\) for every \(x\). If \(\delta\) has a multiple zero at \(x\), which happens at every \(x\) when \(\delta\equiv0\), then \(q_x\) has a double zero \(y_0\). In the coordinates of the proof of Lemma 2.1, \(b^2-4ac\) is a unit times \(\delta\), so its derivative at \(t=0\) vanishes: \(-4a'(0)c(0)=0\). As \(c(0)\ne0\), \(a'(0)=0\), and both partial derivatives \(a'(0)\) and \(b(0)\) of \(G\) vanish at \((x,y_0)\).

**5.3.** The vertical and horizontal lines through the six points meet \(\Gamma'\) exactly in these points, two on each line, because a line of either ruling meets \(\Gamma'\) in a divisor of degree two. With \(T'=\iota_S\iota_F\) on \(\Gamma'\), one gets \(T'(x_0,y_0)=(x_1,y_1)\), \(T'^2(x_0,y_0)=(x_2,y_2)\), \(T'^3(x_0,y_0)=(x_0,y_0)\). Lemma 2.3 holds for any smooth curve of bidegree \((2,2)\) (its proof uses only Lemma 2.2 and genus one), so \(3(S-F)\) is trivial and \(S-F\) is not; the order is three.

**5.4.** By Lemma 3.2, \(\iota_\Phi(p)=T^2\iota_F(p)\), so \(\iota_\Phi(p)=p\) if and only if \(\iota_F(p)=T^{-2}(p)\), and \(T^{-2}=T^2\). To count the fixed points, which are the ramification points of \(\varphi_\Phi\), choose an affine coordinate \(\tau\) on the target \(\mathbb P^1\) such that \(\tau=\infty\) is not a branch value, and let \(\nu=d\tau\), a meromorphic differential without zeros and with a double pole at \(\infty\). Where \(\varphi_\Phi\) is unramified, \(\varphi_\Phi^*\nu\) has the same order as \(\nu\) at the image point. At a ramification point \(p\), \(\tau-\tau(p)\) is a unit times the square of a local coordinate, so \(\varphi_\Phi^*\nu\) has a simple zero. Hence the divisor of \(\varphi_\Phi^*\nu\) is the sum of the ramification points minus twice the two points over \(\infty\). Its degree is \(\deg K_\Gamma=0\), so there are exactly four ramification points.

**5.5.** In the chart \((x',y)\), \(\Omega=-dx'\wedge dy/g'\) with \(g'(x',y)=x'^2g(1/x',y)\). Where \(g'_{y}\ne0\), \(\omega=dx'/g'_y\), and where \(g'_{x'}\ne0\), \(\omega=-dy/g'_{x'}\). These are the expressions of Lemma 1.3 with the sign of \(\varepsilon\) in this chart; by smoothness one of \(g'_{x'},g'_y\) is nonzero at each point, and the corresponding differential \(dx'\) or \(dy\) generates \(\Omega^1_\Gamma\) there. So \(\omega\) has no zero.

## Sources

- [OpenAI-048] OpenAI, *A singular normal affine surface with free tangent sheaf* (manuscript, 23 September 2026), in the release github.com/openai/math, family 048. Section 2: the elliptic model, the quadratic form and the six-vector lemma, for an arbitrary elliptic curve with a line bundle of order four, using its group law. The zigzag curve of Section 2 is a concrete instance, and the switches of Lemma 2.3 serve for the group law.
