# Modular curves and their genus

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A fundamental set records how a group identifies points. A modular curve turns those identifications into a complex surface, with one added point for each end. The genus then measures how much topology remains after the identifications. Three finite counts determine it: the index, the elliptic points and the cusps.

We use Congruence subgroups, cusps and elliptic points, basic complex analysis and the topology of compact oriented surfaces. The free background texts are [Voight open book, Chapters 34–35], [Teleman 2003] and [Stein author PDF, Chapter 6]. The genus calculation below derives its covering count from the explicit two-triangle decomposition of the modular domain; it does not take a general covering formula as an unexplained numerical input.

Throughout, \(\Gamma\) is a subgroup of finite index in \(\mathrm{SL}_2(\mathbb Z)\), and
\[
G=\mathrm{PSL}_2(\mathbb Z),\qquad H=\bar{\Gamma}\subset G,\qquad d=[G:H].
\]
The action and all surface invariants depend on \(H\). In particular, an irregular cusp still has its *projective* width, as defined in the preceding lesson. Write
\[
Y(\Gamma)=H\backslash\mathfrak H,\qquad
X(\Gamma)=H\backslash\mathfrak H^*,\qquad
\mathfrak H^*=\mathfrak H\cup\mathbb P^1(\mathbb Q).
\]
We will specify the topology on the last two spaces. We use \(X_0(N)\), \(X_1(N)\) and \(X(N)\) for the groups \(\Gamma_0(N)\), \(\Gamma_1(N)\) and \(\Gamma(N)\).

## 1. Why the quotient is a surface

**Lemma 1.1 (finiteness on compact sets).** For compact subsets \(K_1,K_2\subset\mathfrak H\), only finitely many \(\gamma\in\mathrm{SL}_2(\mathbb Z)\) satisfy \(\gamma K_1\cap K_2\ne\varnothing\).

*Proof.* Empty sets cause no difficulty, so choose constants \(0<A\le B\) and \(M>0\) such that every point of either compact set has height between \(A\) and \(B\), and real part of absolute value at most \(M\). If
\[
\gamma=\begin{pmatrix}a&b\\c&d_0\end{pmatrix},
\quad z\in K_1,\quad \gamma z\in K_2,
\]
the imaginary-part identity from the first lesson gives
\[
|cz+d_0|^2=\frac{\operatorname{Im}z}{\operatorname{Im}(\gamma z)}
\le B/A.
\]
Put \(R=\sqrt{B/A}\). The imaginary part of \(cz+d_0\) gives \(|c|\le R/A\); its real part then gives \(|d_0|\le R+|c|M\). There are finitely many possible integral bottom rows.

For each such primitive row choose one determinant-one matrix \(\gamma_0\) with that row. Any other has top row differing by an integral multiple of \((c,d_0)\), because the difference has zero determinant with this primitive row. Thus it is \(T^n\gamma_0\), where \(n\in\mathbb Z\). The compact set \(\gamma_0K_1\) has bounded real parts, and \(T^n\) adds \(n\). Meeting \(K_2\) therefore bounds \(n\). There are finitely many choices altogether. \(\square\)

**Proposition 1.2.** The space \(Y(\Gamma)\) is Hausdorff. At each \(\tau\in\mathfrak H\) there is an open neighborhood \(U\) with
\[
\{\gamma\in H:\gamma U\cap U\ne\varnothing\}
=\operatorname{Stab}_H(\tau).
\]
The neighborhood may be chosen invariant under the stabilizer.

*Proof.* Choose a small closed disc about \(\tau\) lying in \(\mathfrak H\). Lemma 1.1 leaves only finitely many elements whose translates can meet it. For each of these that does not fix \(\tau\), shrink an open neighborhood so that its translate misses it; continuity and \(\gamma\tau\ne\tau\) permit this. The intersection of the finitely many neighborhoods has the required exclusion property. Intersect its translates under the finite stabilizer to make it invariant. Every stabilizer element then meets it, since it contains \(\tau\).

For Hausdorffness take points \(\tau,\sigma\) in distinct orbits and small compact disc neighborhoods. Only finitely many \(\gamma\) can carry the first disc into the second. For each, \(\gamma\tau\ne\sigma\), so shrink the two neighborhoods to exclude that intersection. Their orbit images are disjoint open sets. These images are open because the inverse image of an orbit image is the union of all translates of the original open set. \(\square\)

At \(\tau\), use the disc coordinate
\[
w_\tau(z)=\frac{z-\tau}{z-\bar\tau}.
\]
It maps \(\mathfrak H\) biholomorphically to the unit disc and sends \(\tau\) to \(0\): solving for \(z\) gives \(z=(\tau-w\bar\tau)/(1-w)\), and direct subtraction of its conjugate gives positive imaginary part exactly when \(|w|<1\). For a real determinant-one matrix \(\gamma\) with bottom row \((c,d_0)\), direct cross-multiplication gives
\[
w_{\gamma\tau}(\gamma z)
=\frac{c\bar\tau+d_0}{c\tau+d_0}w_\tau(z).
\]
The multiplier has modulus one. Thus a transformation fixing \(\tau\) becomes a rotation, without invoking Schwarz's lemma. The trivial rotation subgroup is cyclic of order one. For a nontrivial finite subgroup take its smallest positive argument \(\theta\), divide every other argument by \(\theta\) with a remainder in \([0,\theta)\), and use closure under quotient to rule out a positive remainder. Dividing \(2\pi\) in the same way shows \(2\pi=e\theta\). The subgroup consists of all \(e\)-th roots of unity.

**Proposition 1.3 (the interior charts).** A coordinate on \(Y(\Gamma)\) near the orbit of \(\tau\) is
\[
u=w_\tau(z)^e,\qquad e=|\operatorname{Stab}_H(\tau)|.
\]
Here \(e=1,2\) or \(3\). These charts make \(Y(\Gamma)\) a Riemann surface.

*Proof.* Choose a sufficiently small round disc \(|w_\tau|<r\) satisfying Proposition 1.2. Two points in this disc have the same orbit exactly when their \(w_\tau\)-coordinates differ by an \(e\)-th root of unity. The power map consequently identifies its quotient with the disc \(|u|<r^e\). It is a homeomorphism on the quotient: the power map is open and its fibers are exactly these finite rotation orbits. The possible orders follow from the stabilizer classification in the first lesson.

Away from the centers, a local branch of the \(e\)-th root has nonzero derivative. Changes of lift are fractional linear transformations, so all transitions there are holomorphic with nonzero derivative. If an overlap contains an elliptic center, its two lifts are \(\tau\) and \(\gamma\tau\) for some \(\gamma\in H\). The map
\[
w_{\gamma\tau}(\gamma z)=\lambda w_\tau(z),\qquad |\lambda|=1,
\]
is a disc automorphism fixing zero. Both stabilizers have the same order. Hence the transition between the quotient coordinates is \(u\mapsto\lambda^e u\), again biholomorphic. This checks the centers as well. \(\square\)

An elliptic point is therefore a smooth point of the resulting Riemann surface. The quotient map from \(\mathfrak H\) branches there. The hyperbolic metric retains a cone angle \(2\pi/e\), which is additional geometric information; it does not make the complex surface singular.

## 2. Filling each end with a cusp

For \(Y>0\), put
\[
B_Y=\{z\in\mathfrak H:\operatorname{Im}z>Y\}.
\]
Give \(\mathfrak H^*\) its usual topology on \(\mathfrak H\) and the neighborhoods
\[
\alpha B_Y\cup\{\alpha\infty\},
\qquad \alpha\in\mathrm{SL}_2(\mathbb Z),
\]
at a rational boundary point. A different integral \(\alpha\) with the same boundary point differs by \(\pm T^n\); it defines the same horoballs. The modular group acts by homeomorphisms. We give \(X(\Gamma)\) the quotient topology.

**Lemma 2.1 (separation of horoballs).** If \(Y>1\), two horoballs \(\alpha B_Y\) and \(\gamma\beta B_Y\), with \(\gamma\in H\), can meet only if \(\alpha\infty\) and \(\beta\infty\) are the same cusp of \(H\).

*Proof.* Set \(g=\alpha^{-1}\gamma\beta\) and write its bottom row as \((c,d_0)\). If \(c\ne0\) and \(\operatorname{Im}z=y>Y\), then
\[
\operatorname{Im}(gz)
=\frac{y}{|cz+d_0|^2}
\le\frac{1}{c^2y}<1/Y<Y.
\]
So \(gB_Y\) cannot meet \(B_Y\). If \(c=0\), the integral determinant-one matrix \(g\) fixes \(\infty\), so \(\gamma\beta\infty=\alpha\infty\), as asserted. \(\square\)

Let \(s=\alpha\infty\), and let \(h\) be its projective width. The stabilizer of \(\infty\) in \(\alpha^{-1}H\alpha\) is generated by \(T^h\).

**Proposition 2.2 (the cusp chart).** On a sufficiently high horoball, the coordinate
\[
q_s=\exp\left(\frac{2\pi i\,\alpha^{-1}z}{h}\right)
\]
identifies a neighborhood of \(s\) in \(X(\Gamma)\) with a disc, sending \(s\) to \(0\). It is compatible with the interior charts.

*Proof.* Lemma 2.1 says that any identification within \(\alpha B_Y\) comes from the stabilizer of \(s\). In the coordinate \(\zeta=\alpha^{-1}z\), these identifications are exactly \(\zeta\mapsto\zeta+nh\). Exponentiation identifies the quotient of \(B_Y\) with
\[
0<|q_s|<\exp(-2\pi Y/h).
\]
Its fibers are exactly those translations; it is open, and its derivative never vanishes. Adding \(s\) fills the puncture. The horoball neighborhoods correspond to smaller discs about zero, so this extension is a homeomorphism.

For a second representative of the same cusp, write \(\beta=\gamma\alpha T^n\) projectively, with \(\gamma\in H\). The width is still \(h\); on the quotient the new coordinate is \(\exp(-2\pi i n/h)q_s\). Thus transitions at a cusp are biholomorphic. Overlaps with interior charts avoid the added point. There we may choose a branch of the logarithm and, where needed, of the root used in Proposition 1.3. These recover the holomorphic lifts with nonzero derivative. \(\square\)

**Theorem 2.3.** The space \(X(\Gamma)\) is a compact connected Riemann surface.

*Proof.* We first check the remaining separation issue. Distinct cusps have disjoint neighborhoods by Lemma 2.1. A cusp can also be separated from an interior orbit. For a compact disc \(K\subset\mathfrak H\), let \(A\le\operatorname{Im}z\le B\) on \(K\). Every integral fractional linear image of a point of \(K\) has height at most \(\max(B,1/A)\): if its bottom-left entry is zero, its bottom-right entry is \(\pm1\); otherwise use the estimate in Lemma 2.1. Apply this to \(\alpha^{-1}\gamma K\), for all \(\gamma\in H\), and choose a higher horoball. Its cusp neighborhood misses the orbit image of the interior of \(K\). Together with Proposition 1.2 this proves Hausdorffness.

The charts in Propositions 1.3 and 2.2 give the compatible complex structure. Second countability can also be checked directly: use a countable disc base on \(\mathfrak H\), and at each of the countably many rational cusps use heights \(Y\in\mathbb Z_{>0}\). Their orbit images form a countable base because the quotient map is open.

Let
\[
F=\{z\in\mathfrak H:|\operatorname{Re}z|\le1/2,\ |z|\ge1\}.
\]
The space \(F\cup\{\infty\}\), with the topology just defined, is compact. Indeed, any open cover contains a neighborhood of \(\infty\), hence covers the part of \(F\) above some height \(Y\). The remainder has \(\sqrt3/2\le y\le Y\) and \(|x|\le1/2\); it is a compact Euclidean set and has a finite subcover.

Choose representatives \(r_1,\ldots,r_d\) for \(H\backslash G\). Reduction to \(F\) shows that \(\bigcup_j r_jF\) maps onto \(Y(\Gamma)\). Every rational cusp is \(g\infty\) for some \(g\in G\); writing \(g=hr_j\) shows that the same finite union of \(r_j(F\cup\{\infty\})\) maps onto \(X(\Gamma)\). These are continuous images of compact spaces, proving compactness. Finally \(Y(\Gamma)\) is connected as an image of \(\mathfrak H\), and every added cusp is in its closure. Hence \(X(\Gamma)\) is connected. \(\square\)

## 3. The covering map and the genus

Write \(X(1)=G\backslash\mathfrak H^*\).

**Lemma 3.1.** The underlying topological space of \(X(1)\) is a sphere.

*Proof.* Cut \(F\cup\{\infty\}\) along the positive imaginary axis. The two pieces are closed topological triangles, with vertices \((\rho,i,\infty)\) and \((\rho+1,i,\infty)\), where \(\rho=(-1+i\sqrt3)/2\). Their vertical sides are identified by \(T\), their circular sides by \(S\), and their common imaginary side by the identity. The complete boundary-identification theorem from the first lesson supplies precisely these identifications, including their endpoints. Thus the quotient consists of two closed discs with their boundary circles identified by a homeomorphism. Extending a parametrization of that boundary into each disc identifies the quotient with the two hemispheres of a sphere. Equivalently, it has three vertices, three edges and two faces, hence Euler characteristic \(3-3+2=2\). \(\square\)

This is a topological statement. The later construction of \(j\) will give a particular holomorphic isomorphism \(X(1)\to\mathbb P^1(\mathbb C)\).

**Proposition 3.2 (all branching).** The natural map
\[
\pi:X(\Gamma)\longrightarrow X(1)
\]
is holomorphic of degree \(d\). Away from the images of \(i,\rho,\infty\) it is unramified. At an interior lift \(\tau\), let \(E=|\operatorname{Stab}_G(\tau)|\) and \(e=|\operatorname{Stab}_H(\tau)|\). Its ramification index is \(E/e\). At a cusp its ramification index is the projective width \(h\).

*Proof.* At an ordinary point the same small disc is a coordinate upstairs and downstairs, so the map is locally a biholomorphism. At an elliptic lift, the coordinates constructed above are \(u=w_\tau^e\) and \(v=w_\tau^E\). The map is
\[
v=u^{E/e}.
\]
At a cusp \(s=\alpha\infty\), use \(\zeta=\alpha^{-1}z\). The downstairs width is \(1\), so its coordinate is \(\exp(2\pi i\zeta)\), while the upstairs coordinate is \(\exp(2\pi i\zeta/h)\). The map is \(q\mapsto q^h\). These formulas prove holomorphicity, including the added points, and identify all the ramification.

For a point \(z\in\mathfrak H\) with trivial \(G\)-stabilizer, its fiber consists of the points represented by \(gz\), indexed without repetitions by \(H\backslash G\). There are \(d\) of them. This proves the degree assertion. \(\square\)

The only general formula needed is the following.

**Riemann–Hurwitz formula.** If \(f:C\to D\) is a nonconstant holomorphic map of degree \(d_f\) between compact connected Riemann surfaces, and \(r_P\) is its local ramification index at \(P\), then
\[
2g(C)-2=d_f(2g(D)-2)+\sum_{P\in C}(r_P-1).
\]
Only finitely many summands are nonzero. The general statement is recorded in the free notes [Teleman 2003, Theorem 5.17 and Lecture 7]. Here is a direct proof of exactly the modular-cover case used in this lesson.

*Proof for \(\pi:X(\Gamma)\to X(1)\).* The two triangles in Lemma 3.1 give a finite cell decomposition of the sphere: three vertices \(i,\rho,\infty\), three edges and two faces. Proposition 3.2 places every branch value at a vertex. Each open edge and face has \(d\) disjoint lifts. Indeed, path lifting on an edge follows by continuing local inverses along successive small coordinate discs; compactness prevents a continuation from escaping. For a triangle interior, two continued inverses along homotopic paths agree: subdivide a path homotopy into rectangles lying in coordinate discs and use uniqueness of the local inverse on each rectangle. The interior is a disc, so every loop contracts, and the \(d\) inverse branches extend throughout it. Closure of the lifted cells attaches at their endpoint vertices by the local maps \(u\mapsto u^{r_P}\) in Proposition 3.2. There are consequently \(3d\) edges and \(2d\) faces upstairs.

Over any vertex the local indices sum to \(d\), since a nearby ordinary point has \(d\) inverse images and a local map of index \(r_P\) supplies \(r_P\) of them. Thus the number of vertices upstairs is
\[
3d-\sum_P(r_P-1).
\]
Subtracting the edge count and adding the face count gives
\(\chi(X)=2d-\sum_P(r_P-1)\). Using Appendix A, Theorem S, this cell count is \(2-2g\), with \(g\) the number of torus handles. \(\square\)

Let \(\varepsilon_2,\varepsilon_3\) be the numbers of elliptic points of \(H\) of orders \(2,3\), and let \(c\) be its number of cusps.

**Theorem 3.3 (the genus formula).**
\[
\boxed{\displaystyle
g(X(\Gamma))=1+\frac d{12}
-\frac{\varepsilon_2}{4}
-\frac{\varepsilon_3}{3}
-\frac c2.}
\]

*Proof.* The fiber over \(i\) contains \(\varepsilon_2\) points with ramification index \(1\); the other points have ramification index \(2\). Since the indices in this fiber sum to \(d\), there are \((d-\varepsilon_2)/2\) of the latter, contributing \((d-\varepsilon_2)/2\) to Riemann–Hurwitz. More explicitly, right multiplication by \(S\) partitions \(H\backslash G\) into fixed points and two-cycles. A fixed coset is exactly a point whose upstairs stabilizer retains the order-two symmetry.

Similarly, right multiplication by \(ST\) has fixed points and three-cycles. The fiber over \(\rho\) contributes \(2(d-\varepsilon_3)/3\). The cusps contribute
\[
\sum_s(h_s-1)=d-c,
\]
because the cusp-width sum is \(d\), as proved in the preceding lesson. Proposition 3.2 excludes all other ramification. Since \(X(1)\) has genus zero, Riemann–Hurwitz now gives
\[
2g-2=-2d+\frac{d-\varepsilon_2}{2}
+\frac{2(d-\varepsilon_3)}3+d-c
=\frac d6-\frac{\varepsilon_2}{2}
-\frac{2\varepsilon_3}{3}-c.
\]
Dividing by two and adding one proves the formula. \(\square\)

As a check on the signs, multiplying a fundamental set's area \(\pi/3\) by \(d\) and rearranging this identity yields
\[
\mu(Y(\Gamma))
=2\pi\left(2g-2+c+\frac{\varepsilon_2}{2}
+\frac{2\varepsilon_3}{3}\right).
\]
Thus the cusp and elliptic terms correct the Euler characteristic in exactly the way the local geometry suggests.

## 4. Computing the examples

For \(\Gamma_0(N)\), the preceding lesson gives
\[
d=N\prod_{p\mid N}(1+p^{-1}),\qquad
c=\sum_{\delta\mid N}\varphi(\gcd(\delta,N/\delta)).
\]
The counts \(\varepsilon_2,\varepsilon_3\) are respectively the numbers of roots of \(x^2+1\) and \(x^2+x+1\) modulo \(N\). The empty product at \(N=1\) is \(1\). The prime-power root formulas and the Chinese remainder theorem evaluate them. Here is the whole calculation for \(N\le30\); each row displays every input to Theorem 3.3.

| \(N\) | \(d\) | \(\varepsilon_2\) | \(\varepsilon_3\) | \(c\) | \(g(X_0(N))\) |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 | 0 |
| 2 | 3 | 1 | 0 | 2 | 0 |
| 3 | 4 | 0 | 1 | 2 | 0 |
| 4 | 6 | 0 | 0 | 3 | 0 |
| 5 | 6 | 2 | 0 | 2 | 0 |
| 6 | 12 | 0 | 0 | 4 | 0 |
| 7 | 8 | 0 | 2 | 2 | 0 |
| 8 | 12 | 0 | 0 | 4 | 0 |
| 9 | 12 | 0 | 0 | 4 | 0 |
| 10 | 18 | 2 | 0 | 4 | 0 |
| 11 | 12 | 0 | 0 | 2 | 1 |
| 12 | 24 | 0 | 0 | 6 | 0 |
| 13 | 14 | 2 | 2 | 2 | 0 |
| 14 | 24 | 0 | 0 | 4 | 1 |
| 15 | 24 | 0 | 0 | 4 | 1 |
| 16 | 24 | 0 | 0 | 6 | 0 |
| 17 | 18 | 2 | 0 | 2 | 1 |
| 18 | 36 | 0 | 0 | 8 | 0 |
| 19 | 20 | 0 | 2 | 2 | 1 |
| 20 | 36 | 0 | 0 | 6 | 1 |
| 21 | 32 | 0 | 2 | 4 | 1 |
| 22 | 36 | 0 | 0 | 4 | 2 |
| 23 | 24 | 0 | 0 | 2 | 2 |
| 24 | 48 | 0 | 0 | 8 | 1 |
| 25 | 30 | 2 | 0 | 6 | 0 |
| 26 | 42 | 2 | 0 | 4 | 2 |
| 27 | 36 | 0 | 0 | 6 | 1 |
| 28 | 48 | 0 | 0 | 6 | 2 |
| 29 | 30 | 2 | 0 | 2 | 2 |
| 30 | 72 | 0 | 0 | 8 | 3 |

For example, the divisors of \(18\) give cusp contributions \(1,1,2,2,1,1\), so \(c=8\). Its index is \(18(3/2)(4/3)=36\). Reduction modulo \(3\) excludes roots of \(x^2+1\); reduction modulo \(2\) excludes roots of \(x^2+x+1\). Hence its genus is \(1+36/12-8/2=0\). At \(25\), the cusp contributions are \(1,4,1\); the two roots of \(x^2+1\) modulo \(5\) lift uniquely modulo \(25\), and \(x^2+x+1\) has no root already modulo \(5\). Thus \(1+30/12-2/4-6/2=0\).

**Prime levels.** At \(11\), both elliptic counts vanish and there are two cusps:
\[
g(X_0(11))=1+12/12-2/2=1.
\]
At \(23\) the same counts give \(g=1+24/12-1=2\). At \(37\), both elliptic counts are \(2\), so
\[
g(X_0(37))=1+38/12-2/4-2/3-1=2.
\]
For a prime \(p\equiv1\pmod{12}\), this simplifies to
\[
g(X_0(p))=\frac{p-13}{12}.
\]
For completeness, when \(p>3\), the four residue classes \(1,5,7,11\) modulo \(12\) give respectively
\[
\frac{p-13}{12},\quad\frac{p-5}{12},\quad
\frac{p-7}{12},\quad\frac{p+1}{12}.
\]
These follow by inserting \((\varepsilon_2,\varepsilon_3)=(2,2),(2,0),(0,2),(0,0)\).

**Principal level.** For \(N\ge3\), the projective index is
\[
d=\frac{N^3}{2}\prod_{p\mid N}(1-p^{-2}),
\]
there are no elliptic points, and every cusp has width \(N\). To see the last assertion, normality reduces it to \(\infty\), where \(T^h\equiv\pm I\pmod N\) forces the positive sign, since \(1\not\equiv-1\pmod N\), and then \(N\mid h\). The width sum gives \(c=d/N\). In particular \(X(7)\) has \(d=168\), \(c=24\), and
\[
g(X(7))=1+168/12-24/2=3.
\]
Here are the small principal levels, including the exceptional index at \(2\).

| \(N\) | \(d\) | \(c\) | \(g(X(N))\) |
|---:|---:|---:|---:|
| 2 | 6 | 3 | 0 |
| 3 | 12 | 4 | 0 |
| 4 | 24 | 6 | 0 |
| 5 | 60 | 12 | 0 |
| 6 | 72 | 12 | 1 |
| 7 | 168 | 24 | 3 |
| 8 | 192 | 24 | 5 |
| 9 | 324 | 36 | 10 |
| 10 | 360 | 36 | 13 |

At \(N=2\), torsion-freeness, index \(6\) and the three width-two cusps were proved in the preceding lesson, giving the first row directly.

**A marked point of order eleven.** The projective index for \(\Gamma_1(11)\) is \(60\), and it has no elliptic points. Its cusp count is
\[
c=\frac12\sum_{\delta\mid11}\varphi(\delta)\varphi(11/\delta)
=\frac12(10+10)=10.
\]
Thus \(g(X_1(11))=1+60/12-10/2=1\).

**An irregular cusp does not change the surface coordinate.** The image of \(\Gamma_1(4)\) equals the image of \(\Gamma_0(4)\): a diagonal unit modulo \(4\) is \(1\) or \(-1\), and changing the matrix sign puts it in \(\Gamma_1(4)\). Consequently \(X_1(4)\) has \(d=6\), no elliptic points and three cusps of projective widths \(1,4,1\). Its genus is \(0\). The cusp \(1/2\) is irregular; using its positive width \(2\) in the surface construction would give the wrong width sum. The surface chart uses projective width \(1\).

## 5. Exercises

1. **Easy.** Use the index, root and cusp formulas to calculate \(g(X_0(13))\) and \(g(X_0(22))\). Display all four inputs, rather than only the resulting genus.
2. **Medium.** Determine exactly which \(N\le25\) have \(g(X_0(N))=0\). Explain why the finite list is exhaustive.
3. **Medium.** Show that \(X(2)\) has three cusps and genus zero. Identify cusp representatives and explain the degree of its map to \(X(1)\).
4. **Hard.** For every \(N\ge3\), prove
   \[
   g(X(N))=1+\frac{N^2(N-6)}{24}
   \prod_{p\mid N}(1-p^{-2}).
   \]
   Explain why the calculation must be adjusted at \(N=2\).

## 6. Solutions

**1.** For \(13\), \(d=14\), the two elliptic counts are \(2\), and the divisors \(1,13\) each contribute one cusp. Therefore
\[
g=1+14/12-2/4-2/3-2/2=0.
\]
For \(22=2\cdot11\), \(d=22(3/2)(12/11)=36\). The factor \(11\equiv3\pmod4\) excludes order-two elliptic points, and reduction modulo \(2\) excludes order-three elliptic points. Since \(22\) is squarefree, every divisor \(\delta\) has \(\gcd(\delta,22/\delta)=1\); its four divisors each contribute one cusp. Thus
\[
g=1+36/12-0-0-4/2=2.
\]

**2.** The zero-genus levels in the table are
\[
1,2,3,4,5,6,7,8,9,10,12,13,16,18,25.
\]
The remaining levels up to \(25\) are \(11,14,15,17,19,20,21,22,23,24\); their genera, in that order, are
\[
1,1,1,1,1,1,1,2,2,1.
\]
Every integer from \(1\) to \(25\) appears in exactly one of these lists. The table was obtained by the proved finite formulas, with all inputs displayed, so this proves both inclusion and exclusion. No assertion about levels above \(25\) is needed.

**3.** Surjective reduction gives
\[
G/\bar{\Gamma}(2)\simeq\mathrm{SL}_2(\mathbb F_2),
\]
of order \(6\). The cusps can be classified by the nonzero reductions of primitive first columns modulo \(2\). There are three: \((1,0),(0,1),(1,1)\), represented by \(\infty,0,1\). Here is also a proof that these labels are complete. Given two primitive integral first columns with the same nonzero reduction, complete each to a determinant-one matrix. Their second columns modulo \(2\) can differ only by a multiple of their common first column. Right multiplication of one matrix by an appropriate \(T^n\) makes the entire reductions equal, without changing its cusp. The quotient of the adjusted matrices is then in \(\Gamma(2)\). Conversely a matrix in \(\Gamma(2)\) fixes each first-column reduction. Thus there are exactly three cusp orbits.

The group is projectively torsion-free, and normality makes the widths equal to the width at \(\infty\), namely \(2\). Hence
\[
g=1+6/12-3/2=0.
\]
The covering has degree \(6\), with three points of ramification index \(2\) over \(i\), two of index \(3\) over \(\rho\), and the three width-two cusps over \(\infty\). Their total contribution is \(3+4+3=10\), and Riemann–Hurwitz checks \(2g-2=-12+10=-2\).

**4.** For \(N\ge3\), the projective index is half the \(\mathrm{SL}_2\)-index, giving
\[
d=\frac{N^3}{2}\prod_{p\mid N}(1-p^{-2}).
\]
Torsion-freeness makes both elliptic counts zero. Normality and the congruence calculation at \(\infty\) above give width \(N\) at every cusp, and hence \(c=d/N\). Substitution gives
\[
g=1+\frac d{12}-\frac d{2N}
=1+\frac{d(N-6)}{12N}
=1+\frac{N^2(N-6)}{24}\prod_{p\mid N}(1-p^{-2}).
\]
At \(2\), the matrix \(-I\) already belongs to \(\Gamma(2)\). Its projective index is therefore the full \(\mathrm{SL}_2\)-index \(6\), not half that number. The widths are still \(2\), yielding three cusps and genus zero as in Solution 3.

## Appendix A. From polygon cells to the genus

The modular covering in Section 3 supplies a finite polygonal presentation. The following proof identifies its cell count with the number of torus handles. It also proves independence of that count for any other finite polygon presentation of the same surface. A surface given only by an arbitrary topological atlas would require an additional finite-presentation theorem; that hypothesis is already supplied in the present application.

The complex charts orient the modular surface. A holomorphic transition with derivative \(f'\ne0\) has real derivative matrix
\[
 \begin{pmatrix}
 \operatorname{Re}f'&-\operatorname{Im}f'\\
 \operatorname{Im}f'&\operatorname{Re}f'
 \end{pmatrix},
\]
whose determinant is \(|f'|^2>0\). The quotient charts of Sections 1–2 give disk neighborhoods, including the elliptic and cusp points. Thus the lifted polygon cells in Section 3 meet the oriented-surface and disk-neighborhood hypotheses of Theorem S.

The elementary foundations retained here are quotient topology, finite graphs and reduced words, compactness of closed finite polyhedra, the intermediate value property, and continuity in intervals and disks. No surface classification, general triangulation, homology classification, van Kampen or Jordan–Schoenflies theorem is assumed. The disk, rectangle and homotopy operations needed below are written out.

**Theorem S.** Let \(X\) be a compact connected oriented surface without boundary, supplied with a finite polygonal cell decomposition. Its face interiors are disks, its edge interiors are intervals, every edge has two face-side incidences, and the finite corner identifications have the disk neighborhoods required of a surface. If its numbers of vertices, edges and faces are \(V,E,F\), then there is a unique integer \(g\geq0\) such that \(X\) is homeomorphic to a sphere with \(g\) torus handles, and
\[
 V-E+F=2-2g. \tag{S0}
\]
The count is independent of the supplied finite polygon decomposition. Here a torus is specifically \(\mathbb R^2/\mathbb Z^2\). Adding a handle means removing a disk from each of the current closed surface and that torus and identifying the two boundary circles with opposite boundary orientations. The genus in (S0) is this number of handles, not a number newly defined from the Euler count.

### A.1. Disk operations and refinement of the supplied cells

A prescribed homeomorphism of boundary circles extends to the disks: in radial coordinates the extension is \(re^{i\theta}\mapsto r h(e^{i\theta})\), with the center mapped to the center. This map and its inverse are continuous at the center as well as elsewhere. An interval homeomorphism extends across a rectangle by acting in its first coordinate. These extensions permit all gluing parametrizations below to be straightened.

Two disks glued along one boundary interval are a disk. To see the map rather than appeal to the appearance of a picture, identify the disks with the upper and lower halves of a round disk, and the interval with their shared diameter. First parametrize the two boundaries so that the chosen intervals are precisely the diameter boundaries of the half-disks and agree there; extend these boundary parametrizations into the half-disks by the preceding cone construction. They give a continuous bijection from the glued pair to the disk. Its inverse is continuous on each half and agrees on the diameter. The same argument shows that two disks joined by a rectangle, using its two short sides, form a disk: divide the rectangle in half and absorb a half into each disk using the interval gluing just proved. These facts also hold for polygon disks, after triangulating a convex polygon from its center and mapping the resulting sectors radially.

The input decomposition can have loops, multiple edges, or repeated vertices on the boundary of one face. We first refine it, rather than silently treat it as a simplicial complex. Insert two distinct new points in every edge interior, dividing each edge into three. In every abstract polygon insert a new interior center and join it to each successive boundary vertex. Because each old side now has two new vertices, each resulting triangle has three distinct vertices in the quotient; its closed triangular disk is embedded. Its new radial edges can still have the same endpoints as another radial edge, but are distinct cells. The change from subdividing an edge has equal increments in \(V,E\). A face with \(k\) boundary sides, counted with their incidences, is replaced by \(k\) triangles; adding its center and radial edges changes the count by
\[
 \begin{aligned}
 \Delta(V-E+F)&=1-k+(k-1)\\
 &=0.
 \end{aligned}\tag{S1}
\]

This is now a finite regular triangular cell structure: every closed triangle and closed edge is embedded, and any intersection is a union of its cells. Subdivide it barycentrically, placing a distinct midpoint in every edge and a distinct center in every triangle. The new triangles correspond to flags \(v\subset e\subset f\). No two flags give the same triple of new vertices, since vertices identify individual old cells, so this is a genuine finite simplicial complex. Its realization maps to \(X\) by the linear maps in the individual triangular cells; the maps agree on shared cells, and their inverses agree as well. If the regular triangular structure had counts \(V_1,E_1,F_1\), the new counts are
\[
 \begin{gathered}
 V_2=V_1+E_1+F_1,\\
 E_2=2E_1+6F_1,\\
 F_2=6F_1.
 \end{gathered}
\]
Thus its count is again \(V_1-E_1+F_1\). This proves the required preservation under this refinement by actual counts, without a general invariance theorem.

Here is why the local construction has the required disk geometry. In a polygon quotient the corner sectors at a vertex form the cone on their link. Every link vertex has degree two, because an edge interior has exactly two sides in a surface. The finite link is consequently a disjoint union of circles. There can be only one circle at a vertex: otherwise the punctured sufficiently small corner neighborhood has several components; a smaller coordinate disk about the vertex would meet all the sectors and have connected punctured interior, which is impossible. Its cone is a disk, with each incident half-edge meeting the boundary in its cyclic order. This gives the vertex disks and edge rectangles used in the following steps. It also proves the local link statement for the refined triangulation rather than assuming it from a drawing.

For the reduction we may therefore work with that finite triangulation. Denote its counts by \(V,E,F\) temporarily; (S1) and the barycentric count show that its Euler count equals the original input count.

### A.2. Merge faces along a dual spanning tree

The dual graph has one vertex for each triangle and one edge for each shared triangle side. It is connected. Indeed, the surface is path connected: in a locally path connected space the set of points reachable from a fixed point is open, and its complement is also open, so connectedness gives the assertion. A path between two face interiors can be moved off the finitely many triangulation vertices, using a small punctured vertex disk. Inside the triangles and the small edge rectangles it can be replaced by finitely many polygonal arcs transverse to sides. This yields a succession of side-adjacent triangles and hence a dual path. The finite replacement follows by subdividing the compact path into portions contained in these finite disk and rectangle neighborhoods.

Choose a spanning tree of this finite dual graph. It exists by adding edges that reach new vertices until all vertices are reached, and has \(F-1\) edges. Glue the **abstract** triangles along only these chosen side pairs. Attaching a leaf triangle to the previously glued component is gluing disks along an interval, so induction produces one abstract polygonal disk \(P\). The remaining original side identifications are still to be made on its boundary. This construction is about abstract disks: unchosen sides are not identified prematurely, even when their original faces are already in the same component.

Every original vertex still has at least one corner on the boundary of \(P\). The triangles around a vertex form a cyclic fan. If all its sides were removed by the dual tree, that tree would contain the complete cycle of adjacent triangles around the vertex, a contradiction. We used a genuine simplicial triangulation here so that this fan is an actual cycle. The remaining edges and their endpoints give an embedded connected graph \(G\subset X\): it is the image of the connected boundary of \(P\), and contains all the original vertices. Its counts and the number of faces are
\[
 \begin{gathered}
 V_G=V,\\
 E_G=E-F+1,\\
 F_G=1.
 \end{gathered}\tag{S2}
\]
Orientation makes the two occurrences of each boundary edge run in opposite directions. The face merging removes one edge and one face each time, so its Euler count remains \(V-E+F\).

Take small disjoint disks about the vertices of \(G\), and a narrow rectangle along the interior of each edge, its short ends attached to disjoint intervals in the vertex-disk boundaries. Their union \(N\) is a closed neighborhood of \(G\). It can be constructed directly from \(P\): cut off small corner sectors and narrow strips along the boundary sides before making the boundary identifications. At each quotient vertex the sectors assemble into the disk described in A.1, and the paired strips assemble into the edge rectangles. The part of \(P\) left after trimming is a disk. Thus
\[
 \begin{gathered}
 X=N\cup D,\\
 N\cap D=\partial N=\partial D\cong S^1.
 \end{gathered}\tag{S3}
\]
and \(N\) has exactly one boundary component. This explicitly identifies the complement; we have not inferred it from an Euler count.

Choose a spanning tree \(T\subset G\). The vertex disks and just the \(V-1\) rectangles of \(T\) form a disk \(D_0\). Prove this by removing a leaf of the tree: its vertex disk and its incident rectangle attach to the previous disk by the disk-plus-rectangle operation of A.1. Starting with a single vertex disk completes the induction. There remain
\[
 \begin{aligned}
 r&=E_G-(V-1)\\
  &=E-V-F+2\\
  &=2-(V-E+F).
 \end{aligned}\tag{S4}
\]
rectangles, each attached along two disjoint intervals on the boundary of what has already been built. Such a rectangle is called a band. All of its future attaching intervals remain available until that band is attached. Formula (S4) is an exact edge count, and \(r\geq0\).

### A.3. What an oriented band does

Write \(S_{g,b}\), for \(b\geq1\), for the concrete surface obtained from a sphere by adding \(g\) standard torus handles and deleting \(b\) open disks in a planar portion away from those handles. The disks are chosen with disjoint collars. In particular \(S_{0,1}\) is a disk and \(S_{0,2}\) is an annulus. We establish, rather than import from classification, the following two rules for attaching a band in an oriented surface:
For ends on the same boundary component the result is \(S_{g,b+1}\), with \(b+1\) boundary components. For ends on distinct boundary components the result is \(S_{g+1,b-1}\), with \(b-1\) boundary components:
\[
 \begin{gathered}
 S_{g,b}\longmapsto S_{g,b+1}\quad\text{(same)},\\
 S_{g,b}\longmapsto S_{g+1,b-1}\quad\text{(distinct)}.
 \end{gathered}\tag{S5}
\]
In the second rule \(b\geq2\). An oriented band is attached with the reversals required for the orientation of the surface and rectangle to agree at both seams. The alternative gluing on one boundary would give a twisted band and a nonorientable neighborhood, so is excluded by the orientation already on \(N\subset X\).

The boundary change can also be checked without either block identification. Remove the two attaching intervals and insert the rectangle's two long sides. If the intervals belonged to one oriented circle, its two remaining arcs close separately along the two long sides, giving two circles. If they belonged to different circles, the two remaining arcs and both long sides form one circle. All other circles are untouched. These are respectively the changes \(+1\) and \(-1\) in (S5); the orientation determines which ends of the arcs are joined.

First normalize the endpoint intervals. On a boundary circle an orientation-preserving reparametrization can carry any two prescribed disjoint intervals to fixed positions in their cyclic order. It extends to a collar, fixing the other edge of that collar: if its increasing lift is \(H:\mathbb R\to\mathbb R\) with \(H(t+1)=H(t)+1\), use the lifts
\(H_s(t)=(1-s)H(t)+st\), \(0\leq s\leq1\). Each is strictly increasing, and its inverse varies continuously, so this is a collar homeomorphism. For ends on different circles do this independently in their disjoint collars. The short-side parametrizations of the band are straightened by the rectangle extension in A.1. Consequently the local homeomorphism type does not depend on the lengths or positions of the endpoint intervals.

There are two elementary blocks to check. A disk with one oriented band is an annulus: identify the disk and band with consecutive rectangles in a strip whose two ends are identified preserving the transverse coordinate. This is \(S^1\times[0,1]\); the two long edges are its two boundary circles. If a second band joins these two circles, the result is a torus with one disk removed. Here is an exact square model. Identify opposite sides of \([0,1]^2\) by translations. The map to \(\mathbb R^2/\mathbb Z^2\) is bijective after these identifications, and has its continuous inverse in the usual quotient charts. A small neighborhood of the image of the square boundary consists of one vertex disk and two bands. The four attaching intervals on that disk occur in alternating order
\[
 a,\ b,\ a^{-1},\ b^{-1}. \tag{S6}
\]
The first band creates an annulus. In that annulus the two intervals for the second band lie on different boundary components: following the unused boundary arcs after the first gluing verifies this directly. The square's remaining central portion is a disk. Thus this two-band neighborhood is the claimed punctured torus. Conversely, the collar reparametrizations above carry any annulus band joining the two boundaries to this model. This proves the block assertion independently of the surface classification theorem.

For the first rule of (S5), take a narrow collar of the affected boundary. A band attached to its one outer boundary replaces the collar annulus by a sphere with three disks removed, usually called a pair of pants. To verify the block, cap the collar's inner circle temporarily. There is then a disk with one oriented band, the annulus just checked. Removing the temporary cap produces the annulus minus one disk, equivalently a sphere minus three disks. One collar boundary used to attach this block to the rest of \(S_{g,b}\) is unchanged; its previous other boundary has become two. The block is planar and contains no handle. Gluing it back gives the concrete model \(S_{g,b+1}\).

For the second rule, the deleted disks in the model \(S_{g,b}\) lie in a planar region. Join the chosen two disks by a polygonal simple arc avoiding the other deleted disks. Such an arc is obtained from a polygonal path in that connected planar region, detouring round the finitely many obstructing disks and removing a segment between a pair of self-intersections whenever one occurs. A narrow neighborhood of the two disks and this arc is itself a disk: it is two disks joined by a rectangular strip, as in A.1. Its intersection with \(S_{g,b}\) is a pair of pants \(P_0\), with two boundary circles equal to the chosen boundary components and a third circle attached to the unaffected rest of the surface. The complement is still the planar region with this neighborhood treated as one hole, together with the \(g\) already existing handles.

The pair of pants may be viewed as an annulus with a disk removed, with the annulus's two boundary circles being the **chosen** two circles. The boundary permutation needed for this assertion has an explicit model: take a sphere minus three congruent small round caps with centers equally spaced on its equator. Its rotations by \(2\pi/3\) about the polar axis, and by \(\pi\) about an axis through one cap center, realize respectively a three-cycle and a transposition of its boundary components, all preserving surface orientation. Stereographic projection from inside a cap realizes it as a disk minus two disks. Collar reparametrization and radial extension normalize their parametrizations. Equivalently, cut the disk-with-two-holes model along two narrow disjoint corridors to its outer boundary; it becomes a disk, and these boundary maps extend by the disk cone construction and glue back. These give the required identification of \(P_0\) with the symmetric model, with any designated boundary labels.

One can check the last cut-to-disk operation in finite rectangle coordinates, so that it is not an appeal to a general planar curve theorem. Take the outer rectangle \([-3,3]\times[-2,2]\), remove the two inner open rectangles \((-2,-1)\times(-1,1)\) and \((1,2)\times(-1,1)\), and cut from their bottom sides to the outer bottom side along \(x=-3/2\) and \(x=3/2\). The cut space consists of the top bar \([-3,3]\times[1,2]\), the three vertical bars with \(x\)-ranges \([-3,-2],[-1,1],[2,3]\) and \(y\)-range \([-2,1]\), and the four half-rectangles below the two holes separated by the cuts. The top bar is joined to the three vertical bars, and each half-rectangle to its adjacent vertical bar. This adjacency is a tree with eight vertices and seven interval gluings. A.1 proves that its union is a disk. Round boundaries are obtained from these rectangle boundaries by radial parametrizations in collars. For the disk-and-strip neighborhood defining \(P_0\), use the two disk collars and the strip coordinates to make these same two cuts; their unrolled collar pieces and strip pieces have the same disk gluing pattern. The same construction applies after stereographic projection to the three-cap model. Choose the boundary map of the two cut disks to agree on each paired cut side as well as on the three boundary contours. Its cone extension then respects those pairs and descends to the desired pair-of-pants homeomorphism. This supplies the finite disk-gluing justification for the boundary permutation, including the label of the boundary attached to the rest of the surface.

Now attach the new band to the two chosen circles of this annulus-minus-a-disk. The annulus-plus-band computation (S6) shows that the block becomes a torus with **two** disks removed: one is the annulus-plus-band block's remaining boundary, and the other is the disk already removed from the pair of pants. Glue its designated third boundary back to the unaffected rest. This adds exactly one torus handle and replaces the two original boundary circles by one. The concrete result is \(S_{g+1,b-1}\). In particular a pair of pants plus this band has two boundary components, not one; confusing this count would invalidate the handle argument.

The collar and disk extensions also show that the standard disks used in these models can be transported within a planar patch. To exchange two disks, take a disk-and-strip neighborhood of the two, map it to a round disk with two symmetric holes, rotate the inside through \(\pi\), and taper that rotation to the identity in its outside collar. To reposition a disk along a polygonal corridor use a finite succession of such disk neighborhoods. These constructions justify choosing the two holes in the preceding argument and making all residual holes lie in the chosen planar region. They do not require a classification of surfaces with boundary.

Attach the \(r\) bands of A.2 in any order. Start with \(D_0=S_{0,1}\). The rules (S5), proved in the explicit models, show inductively that every intermediate surface is some \(S_{g,b}\). Let \(s\) be the number of attachments with both ends on the same boundary component, and let \(m\) be the number with ends on different components. Then
\[
 \begin{gathered}
 r=s+m,\\
 b=1+s-m,\\
 g=m.
 \end{gathered} \tag{S7}
\]
The final neighborhood \(N\) has \(b=1\) by (S3). Hence \(s=m\), \(r=2m=2g\), and capping that boundary disk gives a sphere with \(g\) standard torus handles. Equations (S4) and (S7) prove
\[
 V-E+F=2-r=2-2g. \tag{S8}
\]
At this point existence and the count for the supplied presentation are proved. Uniqueness and independence of presentation still need an invariant; we supply it next.

### A.4. An elementary invariant, with the required attachment proof

For a based space let \(\pi_1\) be the group of based loops modulo based homotopies, with multiplication given by concatenation. Reparametrizing a concatenation gives associativity on classes; reversing a path gives its inverse since traversing a path and immediately reversing it contracts by shortening the distance traversed. A homeomorphism gives an isomorphism by composition with loops and homotopies. Moving the basepoint along a path gives the isomorphism \(\gamma\mapsto p\gamma p^{-1}\), with inverse obtained by the reversed path. These facts follow from the displayed constructions and are sufficient here.

The neighborhood \(N\) deformation retracts onto its core graph \(G\) by an explicit quotient homotopy. Choose a boundary parametrization of the abstract polygon disk \(P\) and extend it radially to the disk as in A.1. Let \(N\) be the quotient of its outer annular collar, with the outer edge identified by the polygon boundary map \(w\colon\partial P\to G\); its remaining inner circle is \(\partial N\). This is the neighborhood already constructed in (S3), after straightening the corner sectors and edge strips. Equivalently it is the mapping cylinder \((\partial P\times[0,1])\sqcup G\), with \((x,0)\) identified to \(w(x)\). The homotopy \([x,t]\mapsto[x,(1-s)t]\), fixing each point of \(G\), is continuous on this quotient and is a deformation retraction at \(s=1\). It proves the group comparison by composition with loops and homotopies; no general regular-neighborhood theorem is used.

For a finite connected graph, a spanning tree gives \(E_G-V_G+1=r\) loop generators and no relations other than free cancellation. Here are the needed path and homotopy details. Cover the graph by small vertex stars and the interiors of its edge intervals, each a tree. Subdivide a loop into finitely many pieces within these sets and replace each piece by the unique reduced arc between its endpoints in that small tree. Sliding in a tree to this arc is a homotopy, obtained by contracting its finite branches. This gives an edge path after joining successive portions and, if necessary, inserting edge subdivisions. A homotopy of loops is a map from a compact square. The inverse images of the small trees have a Lebesgue number: otherwise subsets of diameter tending to zero with no member containing them would have a convergent sequence of points and eventually lie in the member containing the limit, a contradiction. A sufficiently fine square grid therefore has each closed triangle mapped into one small tree. Its boundary edge paths reduce to the empty path; sweeping its triangles replaces paths only by insertion or removal of a consecutive edge and its reverse. Thus a graph homotopy introduces precisely these cancellations.

Use the unique tree paths from a fixed root to the endpoints of every edge outside \(T\) to make its generator loop. A tree-edge traversal contributes no letter after cancellation; an edge outside \(T\) contributes its generator or its inverse. Conversely replacing such letters by their generator loops recovers every based edge path up to cancellation. Hence reduced words in the \(r\) generators give exactly the graph group. In particular its abelianization, the quotient obtained by making all generators commute, is \(\mathbb Z^r\): a commuting word is determined by its exponent sums, and every integer exponent vector occurs.

We must determine what capping \(N\) does to this group. We prove the specific cell-attachment assertion required rather than cite van Kampen. Take open neighborhoods \(U,V\subset X\), where \(U\) consists of \(N\) with a collar extending a little into the cap, and \(V\) is the cap disk with a collar extending a little into \(N\). Then \(U\) retracts to \(N\), \(V\) is an open disk and hence contractible, and \(C=U\cap V\) is an open annulus. Put the basepoint in \(C\).

Every loop in \(X\) can be subdivided into finitely many pieces in \(U\) or \(V\), by the compactness argument for a Lebesgue number just given. Where its type changes, its endpoints lie in \(C\). Join these endpoints to the basepoint by paths in \(C\). Inserting a connector followed by its reverse expresses the original loop as a product of loops in \(U\) and \(V\). The \(V\)-loops contract. A loop in \(C\), considered in \(U\), contracts in \(V\), so all its conjugates and products lie in the kernel of \(\pi_1(U)\to\pi_1(X)\).

There are no further relations. For completeness, subdivide a null-homotopy square into a fine triangular grid so that every closed triangle maps into \(U\) or \(V\). At each grid vertex choose a path from the basepoint in \(U\), in \(V\), or in \(C\), respectively when its image belongs only to \(U\), only to \(V\), or to both. An edge in a triangle of type \(U\) then has both endpoint paths in \(U\), and defines a based \(U\)-loop by those paths and the image edge; similarly for \(V\). The product around each triangle is trivial in its assigned group because its image fills that triangle there. If an edge is shared by triangles of different types, its image and both endpoint paths lie in \(C\); its two descriptions agree after imposing the \(C\)-loop identifications. Here is an ordered cancellation, so that noncommutativity causes no omitted step. Work in the group of the \(U,V\) loop words with the \(C\) identifications just described. For an oriented grid edge \(u\to v\), let \(g_{uv}\) be its based loop class using the chosen endpoint paths, so \(g_{vu}=g_{uv}^{-1}\). A triangle with successively oriented vertices \(u,v,z\) gives
\[
 g_{uv}g_{vz}=g_{uz}.
 \tag{S9a}
\]
Give every small grid square the southwest-to-northeast diagonal. Sweep squares from left to right in the bottom row, then from left to right in each successive row above it. In the bottom row, insert each square's west-side triangle first and its southeast triangle second; start with the west-side triangle of the bottom-left square. In every higher row, insert the south-side triangle first and the northwest triangle second. This choice matters: the first triangle of a later bottom-row square shares its west edge with the preceding square, while the first triangle of a higher-row square shares its south edge with the completed row below. The second triangle shares the diagonal and, if applicable, the other already exposed side. Finish both triangles of one square before moving to the next. At each step the new triangle meets the already swept region in one boundary edge or in two consecutive boundary edges. Replace that oriented boundary arc by the remaining edge or edges of the triangle using (S9a), or its inverse, inside the unchanged preceding and following boundary words. This substitution preserves the ordered product; it does not commute any factors. The reverse-edge identity handles the orientation opposite to the displayed one. The swept region is a disk at every such step, as is seen directly from the rectangular row order; the first triangle has trivial boundary word by its own relation. Induction therefore gives the identity for the final outer boundary word. The constant parts of the null-homotopy boundary contribute the identity, so the original loop word is trivial in this group. This supplies the finite grid argument with its noncommutative order fixed. This verifies the reverse kernel inclusion. Paths on the outer boundary can use the original subdivision; refine the grid there to include its finitely many endpoints.

The open annulus has group \(\mathbb Z\) generated by a core circle. In its product coordinates, contracting the interval coordinate to a fixed interior value is a deformation retraction to that circle. This core is homotopic in \(U\) to the original capping circle \(\partial N\), through the collar. A path in the circle has a continuous angle lift, obtained by successively choosing inverse angles on overlapping proper arcs; its endpoint change on a loop is an integral multiple of \(2\pi\). It is unchanged in a homotopy by subdividing the homotopy square into arc neighborhoods and using uniqueness of the local lifts. A zero-change lifted loop contracts by linear interpolation of its lifted angle with its initial angle. Every integer occurs by going round the circle that many times. This proves the asserted circle and annulus calculation. Therefore the attachment just proved gives
\[
 \pi_1(X)=\pi_1(G)/\langle\!\langle w\rangle\!\rangle, \tag{S9}
\]
where \(w\) is the boundary circle of \(N\) and the double brackets mean the subgroup generated by its conjugates and their inverses.

Under the retraction to \(G\), this boundary goes along each edge once on each of its two sides. Orientation makes these traversals opposite. Every generator edge outside the spanning tree thus has exponent sum zero in \(w\). Making (S9) abelian kills no additional exponent vector: the normal subgroup generated by \(w\) has zero image in \(\mathbb Z^r\). Consequently
\[
 \pi_1(X)^{\mathrm{ab}}\cong\mathbb Z^r=\mathbb Z^{2g}. \tag{S10}
\]

The standard \(h\)-handle model itself has a disk-and-\(2h\)-band presentation: starting from a disk, attach one band to split its boundary and a second to join the resulting two components, returning to one boundary and adding exactly the torus block (S6); repeat this pair \(h\) times and cap the remaining boundary. The local connected-sum description in A.3 identifies each pair with one standard handle. The argument (S9)–(S10) for this presentation gives abelianization \(\mathbb Z^{2h}\), without assuming that a handle count already determines Euler characteristic.

This is a homeomorphism invariant by the loop construction. If \(\mathbb Z^r\cong\mathbb Z^{r'}\), quotienting by doubles gives groups with respectively \(2^r\) and \(2^{r'}\) elements, so \(r=r'\). We used no classification theorem for finitely generated abelian groups. In particular two handle models of \(X\) have the same \(g\). Repeating A.1–A.4 for any other finite polygon decomposition of \(X\) gives the same \(r\), hence the same Euler count \(2-r\). The theorem S is proved for its stated finite-presentation hypothesis, including the uniqueness and invariance assertions.

## What this lesson does not prove

Section 3 proves the required Riemann–Hurwitz count for the modular covering from its explicit cells. The general Riemann–Hurwitz statement is retained for context, but no unproved general instance is used. Appendix A, Theorem S, proves the identification of that finite-polygon cell count with \(2-2g\), where genus counts torus handles, including uniqueness and independence of the presentation. Planar compactness and the real-analysis foundations also remain without verified earlier programme proof locators here. These are residual proof-closure gaps, not consequences certified merely by citing free notes.

We also mention, without using it in the construction or genus calculation, the algebraization theorem: every compact connected Riemann surface is the analytic surface of a smooth projective complex algebraic curve. [Teleman 2003, Lecture 14] explains the theorem through meromorphic functions and a finite map to the projective line. Serre's GAGA comparison theorems apply once projectivity is available; they alone are not the existence theorem needed here. See [Serre 1956, introduction and §3]. The algebraic Riemann–Hurwitz formula in characteristic zero is [Stacks, Tag 0C1B]; it concerns smooth proper curves and is not used to assume algebraicity prematurely.

The index, cusp-width, root-count and torsion-freeness results used in Section 4 were proved in the preceding lesson. We do not yet construct \(j\) or a projective equation for any positive-genus modular curve.

The local power-series, inverse and branching facts have a written earlier proof in lesson 01, Lemma 0.2 and its local inverse consequence. The finite-polygon topology and handle-genus identification are proved in Appendix A. Algebraization and the elementary foundations listed above remain separate obligations.

## References

- **Teleman 2003.** C. Teleman, *Riemann Surfaces*, Lent-term lecture notes. Theorem 5.17 and Lecture 7 contain the analytic Riemann–Hurwitz statement and proof; Lecture 14 discusses algebraization. [Author's notes](https://math.berkeley.edu/~teleman/math/Riemann.pdf).
- **Voight open book.** J. Voight, *Quaternion Algebras*, freely distributed stable post-publication version 1.0.5 (10 January 2024), Chapters 34–35, especially Theorem 34.2.1 and Sections 34.3–34.8 and 35.4. [Author's stable free PDF](https://jvoight.github.io/quat-book-v1.0.5.pdf).
- **Stein author PDF.** W. Stein, *Modular Forms: A Computational Approach*, freely distributed PDF on the author's website, Chapter 6, §§6.1–6.2. [Free author PDF](https://wstein.org/books/modform/stein-modform.pdf).
- **Serre 1956.** J.-P. Serre, *Géométrie algébrique et géométrie analytique*, introduction and §3. [Original paper](https://www.numdam.org/item/AIF_1956__6__1_0/).
- **Stacks.** The Stacks project, [Tag 0C1B](https://stacks.math.columbia.edu/tag/0C1B), Riemann–Hurwitz. We consult the corresponding text in the AI Integrated Stacks Project, an edition with AI-proposed corrections and AI-written additions not reviewed by the official Stacks project maintainers; its [English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) retains the original tags.

- **Gallier.** J. Gallier, *The Classification Theorem for Compact Surfaces And A Detour On Fractals*, §§5.1–5.3. [Free arXiv version](https://arxiv.org/abs/0805.0562v1). The finite-polygon proof required here is written in Appendix A.
- **Hatcher.** A. Hatcher, *Algebraic Topology*, Chapter 1, §1.2, Proposition 1.26(a). [Author's free Chapter 1](https://pi.math.cornell.edu/~hatcher/AT/ATch1.pdf). Appendix A.4 proves the particular cell-attachment assertion used here.
- **Putman.** A. Putman, *A quick proof of the classification of surfaces*. [Author's free note](https://academicweb.nd.edu/~andyp/notes/ClassificationSurfaces.pdf).
