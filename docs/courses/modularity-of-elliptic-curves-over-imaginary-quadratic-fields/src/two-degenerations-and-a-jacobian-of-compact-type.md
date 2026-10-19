# Two degenerations and a Jacobian of compact type

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The family of cyclic covers \(C_{m,R}\colon Y^m=f_R(Z)\) over the moving point \(R\in E\) degenerates where branch points collide. Two such collisions are useful. When \(R\) tends to the origin, all four special points collide at once, and after one blow-up the cover breaks into \(m\) copies of \(E\) attached to a rational curve. The Jacobian then extends across this parameter with fibre \(E^m\), and the deck transformations permute the factors. When \([n]R\) tends to a nonzero \(2\)-torsion point, only the two branch points collide, and the cover acquires \(m\) nodes, each with the simplest possible local equation. The first degeneration controls integral homology and local reduction types (Lessons 4 and 6); the second produces explicit monodromy (Lesson 4).

**Prerequisites.** [*Cyclic covers of an elliptic curve with two branch points*](cyclic-covers-of-an-elliptic-curve-with-two-branch-points.md), especially Lemma 2.1, Proposition 4.2 and Section 6. From *The étale fundamental group*: [*The étale fundamental group*](course:AG-DFG/etale-fundamental-group), the Riemann–Hurwitz formula (5.5).

**Conventions.** As in the previous lesson, \(k\) has characteristic zero, \(n\ge3\) is odd and \(m>1\) divides \(n\). The constant surface is \(E\times E\), with the point \(Z\) in the first factor and the parameter \(R\) in the second; the family \(\mathcal C^E_m\to E^\circ\) is the normalization of \(E\times E^\circ\) in \(Y^m=f_R(Z)\), where \(f_R\) is normalized by \(f_R(O)=1\). A *node* is a point at which a curve is étale-locally isomorphic to \(xy=0\).

## 1. The two boundary parameters

The parameters excluded from \(E^\circ\) are those at which two of the points \(O,\pm R,\pm[n]R\) coincide. We use two of them:
\[
\begin{gathered}
R=O,\qquad\text{and}\\
R=R_*\ \text{ with }\ [n]R_*\in E[2]\setminus\{O\},\\
O,\pm R_*,[n]R_*\ \text{distinct}.\quad(1.1)
\end{gathered}
\]
At \(R=O\) all of \(\pm R\) and \(\pm[n]R\) collide with \(O\). At \(R=R_*\) the two branch points \([n]R_*\) and \(-[n]R_*\) coincide, because \([n]R_*\) is \(2\)-torsion, and nothing else collides. Points \(R_*\) as in (1.1) exist over \(\bar k\): any point of exact order \(2n\) works, since then \([n]R_*\) has order \(2\), and \([n\mp1]R_*\ne O\) because \(2n\) does not divide \(n\pm1\). Over \(\mathbb C\), with a period basis \(a,b\) of \(E(\mathbb C)=\mathbb C/(\mathbb Za+\mathbb Zb)\), we take \(R_*=a/(2n)\).

## 2. The degeneration at the origin

Fix an odd uniformizer \(u\) of \(E\) at \(O\), for example \(u=x/y\), which satisfies \(u\circ[-1]=-u\). Near \((Z,R)=(O,O)\) use the coordinates
\[
z=u(Z),\qquad r=u(R).
\]
Since \([-1]\) and \([n]\) are group homomorphisms with derivatives \(-1\) and \(n\) at \(O\), the four sections through \((O,O)\) have equations
\[
\begin{gathered}
z=r,\qquad z=-r,\\
z=nr+O(r^3),\\
z=-nr+O(r^3)\quad(2.1)
\end{gathered}
\]
for \(Z=R\), \(Z=-R\), \(Z=[n]R\) and \(Z=-[n]R\). The cubic error term has no quadratic part because \(u\circ[n]\) is an odd function of \(u\).

Let \(\widetilde{\mathcal S}\) be the blow-up of \(E\times E\) at \((O,O)\), restricted over a neighbourhood \(N\) of \(O\) in the parameter curve that contains no other excluded parameter. In the chart \(z=rv\) the exceptional curve \(P\cong\mathbb P^1\) is \(r=0\) with coordinate \(v=z/r\), and by (2.1) the strict transforms of the four sections meet it at
\[
\begin{gathered}
v=1,\quad v=-1,\\
v=n,\quad v=-n ,\quad(2.2)
\end{gathered}
\]
which are distinct because \(n\ge3\). The strict transform of the zero section \(z=0\) meets \(P\) at \(v=0\). The strict transform \(\widetilde F\cong E\) of the fibre \(r=0\) of \(E\times E\) meets \(P\) at \(v=\infty\); in the chart \(r=wz\), with \(w=1/v\), the fibre over the parameter \(r\) is \(wz=r\), so the two components of the new fibre meet in a node whose smoothing parameter is \(r\) itself.

**Lemma 2.1.** On \(\widetilde{\mathcal S}\) the divisor of the Kummer function \(f\) consists of the strict transforms of the four sections, with multiplicities \(-n,n,1,-1\) for \(Z=R,-R,[n]R,-[n]R\). In particular \(f\) is a unit at the node \(P\cap\widetilde F\) and along \(\widetilde F\).

**Proof.** Away from the fibre over \(O\), the divisor of \(f\) is that of Section 4 of the previous lesson. The only other possible components are \(P\) and \(\widetilde F\). The automorphism \(\iota(Z,R)=(-Z,R)\) of \(E\times E\) fixes \((O,O)\), so it lifts to \(\widetilde{\mathcal S}\), where it maps \(P\) to itself (by \(v\mapsto-v\)) and \(\widetilde F\) to itself. Since \(f\circ\iota=f^{-1}\) by (2.2) of the previous lesson, the multiplicities of \(P\) and \(\widetilde F\) in \(\operatorname{div}(f)\) are their own negatives, hence zero. The four strict transforms meet the special fibre only at the points (2.2) of \(P\), none of which is the node \(v=\infty\). \(\square\)

**Proposition 2.2 (the exceptional function).** The restriction of \(f\) to \(P\) is
\[
f_{\mathrm{exc}}(v)=\frac{v-n}{v+n}\Bigl(\frac{v+1}{v-1}\Bigr)^{n},\quad(2.3)
\]
and the restriction of \(f\) to \(\widetilde F\) is the constant \(1\).

**Proof.** By Lemma 2.1 and (2.2), the restriction of \(f\) to \(P\) has divisor \((n)-(-n)-n(1)+n(-1)\), so it equals \(c\,f_{\mathrm{exc}}\) for a constant \(c\). The zero section meets \(P\) at \(v=0\), where \(f=1\). Since \(n\) is odd,
\[
\begin{aligned}
f_{\mathrm{exc}}(0)&=\frac{-n}{n}\cdot\Bigl(\frac{1}{-1}\Bigr)^{n}\\
&=(-1)\cdot(-1)=1,
\end{aligned}
\]
so \(c=1\). The restriction of \(f\) to \(\widetilde F\cong E\) has no zeros or poles, by Lemma 2.1, so it is constant, and at the node its value is \(f_{\mathrm{exc}}(\infty)=1\). \(\square\)

**Proposition 2.3 (a model of compact type).** Let \(\widetilde{\mathcal C}_m\) be the normalization of \(\widetilde{\mathcal S}\) in \(Y^m=f\). Then \(\widetilde{\mathcal C}_m\to N\) is proper and flat with regular total space, smooth outside \(m\) points of the fibre over \(O\), and each of these \(m\) points is a node with local equation \(xy=r\). If \(\mu_m\subset k\), the fibre over \(O\) is the union of

- \(m\) copies \(E_\zeta\), \(\zeta\in\mu_m\), of \(E\), the components \(Y=\zeta\) over \(\widetilde F\), and
- one smooth rational curve \(P'\) over \(P\),

where \(E_\zeta\) meets \(P'\) in exactly one point, the point of \(P'\) over \(v=\infty\) with \(Y=\zeta\), and the \(E_\zeta\) are pairwise disjoint. The rotation \(u_\zeta\) maps \(E_{\xi}\) to \(E_{\zeta\xi}\).

**Proof.** Away from the node of the special fibre, \(\widetilde{\mathcal S}\to N\) is smooth: along \(P\) minus \(v=\infty\) the fibre is the reduced smooth curve \(r=0\) in the coordinates \((r,v)\), and along \(\widetilde F\) minus the node nothing has changed. The local analysis of Proposition 4.2 of the previous lesson therefore applies there, using Lemma 2.1 for the four sections, and shows that \(\widetilde{\mathcal C}_m\) is smooth over \(N\) at all points not above the node.

Near the node, \(f\) is a unit (Lemma 2.1), so \(Y^m=f\) is finite étale over \(\widetilde{\mathcal S}\) there and the node has \(m\) preimages. An étale morphism preserves the local equation: each preimage is a node of its fibre with local equation \(wz=r\). The total space is regular at these points, since \(wz=r\) defines a regular surface with parameters \(w,z\).

Over \(\widetilde F\) the cover is \(Y^m=1\), by Proposition 2.2, which splits into the \(m\) components \(Y=\zeta\), each isomorphic to \(\widetilde F\cong E\). Over \(P\), put
\[
\begin{gathered}
Y'=Y\Bigl(\frac{v-1}{v+1}\Bigr)^{n/m},\\
\text{so that}\qquad Y'^m=\frac{v-n}{v+n}.
\end{gathered}
\]
This is a cyclic cover of \(\mathbb P^1\) of degree \(m\), totally ramified over \(v=\pm n\) and unramified elsewhere; it is irreducible by the valuation argument of Proposition 3.1 of the previous lesson, and by Riemann–Hurwitz \(2g-2=m(-2)+2(m-1)=-2\), so \(g=0\). Over \(v=\infty\) we have \((v-1)/(v+1)=1\), so \(Y'=Y\) and \(Y'^m=1\): the \(m\) points of \(P'\) over \(v=\infty\) are \(Y=\zeta\), \(\zeta\in\mu_m\), all defined over \(k\). The point with \(Y=\zeta\) lies on \(E_\zeta\), which gives the attachments. The rotation \(Y\mapsto\zeta Y\) maps the component \(Y=\xi\) to \(Y=\zeta\xi\). \(\square\)

The dual graph of this fibre has one vertex for \(P'\), one for each \(E_\zeta\), and one edge for each node: it is a star with \(m\) leaves, in particular a tree. A nodal curve whose dual graph is a tree is said to be *of compact type*. The fibre is the minimal regular model of its generic fibre over the local ring at \(O\): its rational component has self-intersection \(-m\) (Exercise 4.3).

**Lemma 2.4 (Picard groups of nodal curves).** Let \(D\) be a connected reduced proper curve over an algebraically closed field \(\kappa\), whose singularities are \(\delta\) nodes and whose \(c\) irreducible components \(D_1,\ldots,D_c\) are smooth. Then restriction to the components gives an exact sequence
\[
1\to T\to\operatorname{Pic}(D)\to\prod_{i=1}^c\operatorname{Pic}(D_i)\to0,
\]
in which \(T\) is the quotient of \((\kappa^\times)^\delta\) by the image of \((\kappa^\times)^c\) under the coboundary map of the dual graph, a torus of dimension \(\delta-c+1\). If the dual graph is a tree, \(T\) is trivial and \(\operatorname{Pic}^0(D)\cong\prod_i\operatorname{Pic}^0(D_i)\).

**Proof.** Let \(\nu\colon\widetilde D=\bigsqcup_iD_i\to D\) be the normalization. At a node \(x\) with preimages \(x',x''\), a function on \(\widetilde D\) near \(x',x''\) descends to \(D\) exactly when its values at \(x'\) and \(x''\) agree. This gives the exact sequence of sheaves
\[
1\longrightarrow\mathcal O_D^\times\longrightarrow\nu_*\mathcal O_{\widetilde D}^\times\longrightarrow\bigoplus_x\kappa_x^\times\longrightarrow1,
\]
where \(\kappa_x^\times\) is the skyscraper \(\kappa^\times\) at the node \(x\) and the last map is \(g\mapsto g(x')/g(x'')\) for a chosen ordering of the branches. Since \(\nu\) is finite, \(H^1(D,\nu_*\mathcal O^\times_{\widetilde D})=\operatorname{Pic}(\widetilde D)\), and the long exact sequence reads
\[
\begin{gathered}
\kappa^\times\to(\kappa^\times)^c\xrightarrow{\ \partial\ }(\kappa^\times)^\delta\\
\to\operatorname{Pic}(D)\to\operatorname{Pic}(\widetilde D)\to0,
\end{gathered}
\]
because \(H^1\) of a skyscraper sheaf vanishes and \(H^0(D,\mathcal O_D^\times)=\kappa^\times\) for a connected reduced proper curve. The map \(\partial\) sends constants \((a_i)\) on the components to \((a_{i(x')}/a_{i(x'')})_x\): it is the coboundary of the dual graph with coefficients in \(\kappa^\times\). For a connected graph its kernel is the diagonal \(\kappa^\times\) and its cokernel is a torus of dimension \(\delta-c+1\), the first Betti number of the graph. For a tree \(\delta=c-1\) and \(\partial\) is surjective: one solves for the constants component by component, moving away from a root. Restricting to line bundles of degree zero on every component gives the last assertion. \(\square\)

We use the following theorem of Raynaud, in the form recorded by Deligne and Mumford.

**Theorem 2.5 (named result N6: Raynaud's theorem on the Picard functor).** Let \(A\) be a discrete valuation ring whose fraction field \(F_0\) has characteristic zero, \(C/F_0\) a smooth projective geometrically connected curve of positive genus, and \(\mathcal C\) the minimal regular model of \(C\) over \(A\). If the special fibre of \(\mathcal C\) is reduced, then the identity component of the Néron model of the Jacobian of \(C\) represents the relative Picard functor \(\operatorname{Pic}^0_{\mathcal C/A}\). In particular, its special fibre is \(\operatorname{Pic}^0\) of the special fibre of \(\mathcal C\).

This is Theorem (2.5) of [DM], with the explanation following it of how it comes out of Raynaud's work. The course uses it without proof.

**Corollary 2.6.** Suppose \(\mu_m\subset k\), and let \(A\) be the local ring of the parameter curve at \(O\). There is a smooth separated commutative group scheme \(\mathcal J_m\) of finite type over \(A\) whose generic fibre is the Jacobian of the generic curve \(C_m\) and whose special fibre is
\[
\mathcal J_{m,O}\cong\prod_{\zeta\in\mu_m}E_\zeta\cong E^m .
\]
The rotations act on \(\mathcal J_m\); on the special fibre, \(u_\zeta\) maps the factor \(E_\xi\) to \(E_{\zeta\xi}\) by the identity of \(E\).

**Proof.** The model of Proposition 2.3 is regular, proper and flat over \(A\), its generic fibre is geometrically connected of genus \(m\) (Proposition 3.1 of the previous lesson), its special fibre is reduced, and it is minimal by Exercise 4.3. Let \(\mathcal J_m\) be the identity component of the Néron model of the Jacobian of the generic fibre. By Theorem 2.5 it represents \(\operatorname{Pic}^0\) of the model, so its special fibre is \(\operatorname{Pic}^0\) of the fibre over \(O\). By Lemma 2.4, applied over \(\bar k\), this is \(\prod_\zeta\operatorname{Pic}^0(E_\zeta)\times\operatorname{Pic}^0(P')\), and \(\operatorname{Pic}^0(P')=0\) because \(P'\) is rational. All components are defined over \(k\), so the identification holds over \(k\). The rotations act on the model compatibly with the projection to the parameter curve, hence on the relative Picard functor, and on the special fibre through their action on the components (Proposition 2.3). \(\square\)

Lesson 6 uses this group scheme only through its torsion.

**Corollary 2.7.** In the situation of Corollary 2.6, let \(N\ge1\). There are an open neighbourhood \(X_N\) of \(O\) in the parameter curve and a finite étale group scheme \(\mathcal T_N\to X_N\), with an action of the rotations, whose fibre at \(O\) is \(E^m[N]\) and whose fibre at every other point \(R\in X_N\) is the \(N\)-torsion \(\operatorname{Jac}(C_{m,R})[N]\), compatibly with the rotations.

**Proof.** Multiplication by \(N\) on the smooth group scheme \(\mathcal J_m\) is étale, because \(N\) is invertible and it is étale on both fibres, where it is an isogeny of abelian varieties of dimension \(m\) of degree \(N^{2m}\). So \(\mathcal J_m[N]\to\operatorname{Spec}A\) is étale, separated and quasi-finite, with \(N^{2m}\) geometric points in each fibre. By Zariski's main theorem it is an open subscheme of a finite \(A\)-scheme. Let \(\overline{T}\) be the closure of its generic fibre there; it is finite and flat over \(A\) of degree \(N^{2m}\), and it contains every point of \(\mathcal J_m[N]\), because a flat morphism allows generization of points. Its special fibre has at most \(N^{2m}\) geometric points, all of which are already in the étale special fibre of \(\mathcal J_m[N]\). Hence \(\mathcal J_m[N]=\overline T\) is finite étale over \(A\). A finite étale group scheme over the local ring \(A\), together with its identification with \(\operatorname{Jac}(C_m)[N]\) over the generic point and the action of the rotations, extends to a finite étale group scheme over some open neighbourhood \(X_N\) of \(O\), which agrees with the torsion of the Jacobian family over \(X_N\setminus\{O\}\) after shrinking. \(\square\)

**Remark 2.8.** Everything in this section happens over the characteristic-zero parameter curve. No model of the curves over a ring of integers is used, in particular none in residue characteristic dividing \(m\). After completing \(k\) at a place, Corollary 2.7 gives, for each \(N\), a family of finite Galois modules over a neighbourhood of \(O\) in the \(p\)-adic points of the parameter curve; the arithmetic reduction types of the nearby Jacobians are determined in Lesson 6 from these families, not from an integral model of the covers.

## 3. The degeneration at a two-torsion collision

Work over \(\mathbb C\), with \(E(\mathbb C)=\mathbb C/(\mathbb Za+\mathbb Zb)\) and \(R_*=a/(2n)\). Put \(Q=a/2=[n]R_*\), a nonzero \(2\)-torsion point, and use the additive coordinates
\[
t=R-R_*,\qquad z=Z-Q
\]
near \((Z,R)=(Q,R_*)\). Then \([n]R=Q+nt\) and \(-[n]R=-Q-nt=Q-nt\), so the two colliding branch points are the curves \(z=nt\) and \(z=-nt\); the points \(\pm R\) and \(O\) stay away from \(Q\).

**Lemma 3.1 (the node equation).** Blow up \(E\times E\) at \((Q,R_*)\) and normalize in \(Y^m=f_R(Z)\). Near the fibre over \(R_*\), the result is a family over a disc in the parameter \(t\) whose fibre over \(t=0\) consists of two components, an elliptic curve \(E'\) and a smooth rational curve, meeting in exactly \(m\) nodes. Near each node the family has the analytic local equation
\[
XU=-2nt
\tag{3.1}
\]
in suitable local coordinates \(X,U\). In particular the smoothing parameter of every node is \(t\) to the first power.

**Proof.** Near \((Q,R_*)\) the divisor of \(f_R(Z)\) is \((z-nt)-(z+nt)\) in the sense of the two sections, so
\[
f_R=g(z,t)\,\frac{z-nt}{z+nt}
\]
with \(g\) holomorphic and nowhere zero near \((0,0)\). Choose a holomorphic \(m\)-th root \(g^{1/m}\) and put \(V=Y/g^{1/m}\). The equation \(Y^m=f_R\) becomes \(V^m(z+nt)=z-nt\), that is,
\[
(z+nt)(V^m-1)=-2nt .
\tag{3.2}
\]
Near a point with \(V=\zeta\in\mu_m\), the function \(U=V^m-1\) is a local coordinate in \(V\), since its derivative \(mV^{m-1}\) does not vanish. With \(X=z+nt\), equation (3.2) is (3.1), and there are exactly \(m\) such points, one for each \(\zeta\). The surface \(XU=-2nt\) is smooth in the coordinates \(X,U\), with \(t=-XU/(2n)\), and it is the chart of the normalized blow-up near these points: the component \(U=0\), where \(V^m=1\), is the strict transform of the fibre \(t=0\), and the component \(X=0\) lies over the blown-up point. The nonzero constant \(-2n\) changes no vanishing order.

On the strict transform of the fibre over \(R_*\), the divisor of the limit function \(f_{R_*}\) is \(n(-R_*)-n(R_*)\): the contributions \(\pm1\) of the colliding branch points cancel at \(Q\). Write this divisor as \(m\cdot D\) with
\[
D=\frac nm\bigl((-R_*)-(R_*)\bigr).
\]
The cover \(Y^m=f_{R_*}\) of \(E\) is unramified. It is connected exactly when the class of \(D\) in \(\operatorname{Pic}^0(E)\) has order \(m\) (Exercise 4.2). Under \(\operatorname{Pic}^0(E)\cong E\), \(D\mapsto\) the sum of \(D\), this class corresponds to
\[
-\frac{2n}{m}R_*=-\frac am ,
\]
a point of exact order \(m\). So the cover is a connected unramified cover of degree \(m\) of an elliptic curve, and by Riemann–Hurwitz it is an elliptic curve \(E'\).

On the exceptional curve, only the two colliding sections meet it, at two distinct points (their slopes \(\pm n\) are different), with multiplicities \(1\) and \(-1\). The cover over it is cyclic of degree \(m\), totally ramified at these two points, and therefore a smooth rational curve, by the computation in Proposition 2.3. Its \(m\) points over the node of the blown-up surface are the \(m\) nodes found above. \(\square\)

The dual graph of the fibre over \(R_*\) has two vertices joined by \(m\) edges, so its first Betti number is \(m-1\). In contrast to the fibre over \(O\), this fibre is not of compact type: by Lemma 2.4 its generalized Jacobian is an extension of \(E'\) by a torus of dimension \(m-1\). The \(m\) nodes come from the boundary of a small disc around \(Q\) in \(E\), lifted to the \(m\) sheets; Lesson 4 identifies their classes in homology.

## 4. Exercises

**4.1.** Show that in the chart \(z=rv\) of the blow-up at \((O,O)\), the strict transform of the section \(Z=[n]R\) is the curve \(v=n+O(r^2)\), and deduce that it meets the exceptional curve transversally at \(v=n\).

**4.2.** Let \(E\) be an elliptic curve over an algebraically closed field of characteristic zero, \(m\ge2\) odd, and \(g\) a rational function with \(\operatorname{div}(g)=mD\). Show that the cover \(Y^m=g\) is unramified, and that it is connected if and only if the class of \(D\) in \(\operatorname{Pic}^0(E)\) has order exactly \(m\).

**4.3.** For the fibre over \(O\) in Proposition 2.3, compute the self-intersection of the rational component \(P'\) on the surface \(\widetilde{\mathcal C}_m\), and conclude that the model contains no smooth rational curve of self-intersection \(-1\) in that fibre.

**4.4.** Compute the arithmetic genus of the fibre over \(R_*\) in Lemma 3.1 from its components and nodes, and check that it equals \(m\).

## 5. Solutions

**4.1.** The section is \(z=\phi(r)\) with \(\phi(r)=nr+cr^3+O(r^4)\) by (2.1). In the chart \(z=rv\) its total transform is \(r(v-\phi(r)/r)=0\); removing the exceptional factor \(r\) leaves \(v=\phi(r)/r=n+cr^2+O(r^3)\). At \(r=0\) this is the point \(v=n\), and the curve is a graph over the \(r\)-axis, hence transverse to the exceptional curve \(r=0\).

**4.2.** At each point, \(g=\pi^{ma}\varepsilon\) with a unit \(\varepsilon\), so the argument of Proposition 3.1(2) of the previous lesson shows that the cover is unramified. If the class of \(D\) has order \(d<m\), then \(d\mid m\) and \(dD=\operatorname{div}(\psi)\) for some \(\psi\). Then \(\operatorname{div}(g)=\operatorname{div}(\psi^{m/d})\), so \(g=c\psi^{m/d}\) with \(c\) a constant, which has an \((m/d)\)-th root \(c_0\). The polynomial \(Y^m-g\) has the factor \(Y^d-c_0\psi\), so the cover is disconnected. Conversely, if \(Y^m-g\) is reducible over the function field \(K\), then since \(m\) is odd, Capelli's theorem gives a prime \(p\mid m\) with \(g=\phi^p\) for some \(\phi\in K\). Then \(mD=p\operatorname{div}(\phi)\), so \(\operatorname{div}(\phi)=(m/p)D\) and the class of \(D\) has order dividing \(m/p<m\).

**4.3.** The fibre over \(O\) is a principal divisor on the surface, so it has intersection number zero with each of its components. The fibre is reduced, equal to \(P'+\sum_\zeta E_\zeta\), and \(P'\) meets \(\sum_\zeta E_\zeta\) in \(m\) transverse points. Hence \(P'^2=-P'\cdot\sum_\zeta E_\zeta=-m\le-3\). The other components are elliptic curves. So no component is a smooth rational curve of self-intersection \(-1\), and the model is the minimal regular model of its generic fibre.

**4.4.** For a reduced nodal curve with components \(D_i\) of genera \(g_i\) and \(\delta\) nodes, the arithmetic genus is \(\sum_ig_i+\delta-c+1\), where \(c\) is the number of components (this follows from \(\chi(\mathcal O)=\sum_i\chi(\mathcal O_{D_i})-\delta\)). Here \(g(E')=1\), the rational component has genus \(0\), \(\delta=m\) and \(c=2\), so the arithmetic genus is \(1+m-2+1=m\), the genus of the nearby smooth fibres, as it must be in a flat family.

## Sources

- [OpenAI-030] OpenAI, *Modularity of elliptic curves over imaginary quadratic fields*, OpenAI Math Release preprint, 4 October 2026, Section 3 (cyclic covers and two degenerations). https://github.com/openai/math/tree/main/preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026
- [DM] P. Deligne and D. Mumford, *The irreducibility of the space of curves of given genus*, Publ. Math. IHÉS 36 (1969), Section 2, Theorem (2.5) (Raynaud's theorem) and the paragraph following it. https://publications.ias.edu/sites/default/files/Number7.pdf
