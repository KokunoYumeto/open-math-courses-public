# A spatial measure

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The contradiction in [Boundary activity](boundary-activity.md) counts participating vertices in narrow strips of the plane, so it needs a Euclidean picture of the vertex measure, while keeping a positive amount of edge mass. This lesson constructs one limit position for a positive part of the labels [OpenAI-HL, Section 6]. The radial comparison of [The zoom at a rank point](the-zoom-at-a-rank-point.md) holds at one point and one radius at a time, with a threshold for the configuration that depends on both. A Hausdorff limit of the graphs of the normalized inverse rank maps allows this threshold to be used one point and one scale at a time, and gives a limit position \(l(p)\) satisfying an inverse Hölder bound. Combined with a bounded density of vertex mass in rank coordinates, it gives disks of radius \(r\) mass \(O(r^{32/17})\), and strips of width \(r\) mass \(O(r^{15/17})\).

Notation: \(D=(0,1)^2\); \(p(z)=(z_A,z_B)\); \(L_n:D\to\mathbb R^2\) is the common normalization of [The zoom at a rank point](the-zoom-at-a-rank-point.md), a homeomorphism onto the plane, with \(U_n(p,h)\) and \(V_n(p,h)\) the largest and smallest distance from \(L_n(p)\) of the image of the circle of radius \(h\) about \(p\). The set \(E\), the window \(K_0\) and \(\lambda_{K_0}(E)>0\) are those of Proposition 6.1 of [Independent gradients and tangent directions](independent-gradients-and-tangent-directions.md); the radial comparison, Proposition 4.1 of [The zoom at a rank point](the-zoom-at-a-rank-point.md), holds at every \(p\in p(E)\). We also use \(\lambda\ll\mu\) from [Limiting measures](limiting-measures.md).

## 1. The statement

**Proposition 1.1** (spatial limit; OpenAI). Let \(\eta=1/16\). There are a Borel set \(G\subseteq E\) with \(\lambda_{K_0}(G)>0\), a further subsequence of configurations, and translations and positive rescalings of the normalized planes, with the following properties.

(a) Let \(\Gamma\) be the Hausdorff limit of the closed graphs of the \(L_n\) (Section 4). Over every \(p\in p(G)\), \(\Gamma\) has exactly one point \((p,l(p))\), with \(|l(p)|\le1\), and \(L_n(p)\to l(p)\).

(b) There is \(c_G>0\) with \(|l(p)-l(q)|\ge c_G|p-q|^{1+\eta}\) for \(p,q\in p(G)\).

(c) Attach to every vertex its normalized position as an additional label, take weak limits, and let \(\beta\) be the image, on the position coordinate, of the limiting vertex measure restricted to the labels with \(z\in G\). Then, with \(d_*=2/(1+\eta)=32/17\),
\[
\beta(B(x,r))\le C_Gr^{d_*}
\]
for \(x\in\mathbb R^2\) and \(0<r<1\);
every strip of width \(r<1\) has \(\beta\)-mass at most \(C'_Gr^{d_*-1}\), and every line has \(\beta\)-mass zero.

The numerical fact used later is \(d_*=32/17>7/4\); the strip exponent \(d_*-1=15/17\) is an auxiliary exponent, unrelated to the final power saving.

## 2. Common scales and bounded density

For integers \(T\ge2\) and \(m\ge0\) put \(h_j=T^{-m-j}\), \(\alpha=T^{-1-\eta}\) and \(\beta_T=T^{-1+\eta}\). Let \(\mathcal P_{T,m}\) be the set of \(p\in D\) with \(\bar B(p,h_0)\subseteq D\) such that for every \(j\ge0\), in all sufficiently late configurations,
\[
\begin{gathered}
V_n(p,h_{j+1})\ge\alpha\,U_n(p,h_j),\\
U_n(p,h_{j+1})\le\beta_T\,V_n(p,h_j).
\end{gathered}
\]
For a fixed radius, \(U_n\) and \(V_n\) are continuous functions of \(p\), so \(\mathcal P_{T,m}\) is Borel: "in all late configurations" is a countable union over thresholds of countable intersections. For \(p\in p(E)\), choose \(T\) with \(C_p\le T^\eta\), for the constant \(C_p\) of the radial comparison, and then \(m\) with \(h_0=T^{-m}<h_{p,T}\); the radial comparison with radii \(h_j\) gives \(p\in\mathcal P_{T,m}\), since \(1/(C_pT)\ge\alpha\) and \(C_p/T\le\beta_T\). So the countably many sets \(p^{-1}(\mathcal P_{T,m})\) cover \(E\); fix \(T,m\) for which \(E\cap p^{-1}(\mathcal P_{T,m})\) has positive \(\lambda_{K_0}\)-mass, and replace \(E\) by it. There is no common threshold for the configurations over \(E\).

Next, the vertex measure. By the Lebesgue decomposition [Fremlin, 232I] and the Radon–Nikodym theorem [Fremlin, 232E], the image of \(\mu\) under \(p\) is \(\phi\,dp+\sigma_s\), with a Borel density \(\phi\) and a measure \(\sigma_s\) carried by a Lebesgue-null Borel set \(S\). Enlarging \(S\) by the null set where \(\phi=\infty\), remove \(p^{-1}(S)\) from \(E\); this removes no \(\lambda\)-mass, because the image of \(\lambda|_E\) under \(p\) is absolutely continuous. Then for a large \(M\) the labels with \(\phi(p(z))\le M\) still carry positive \(\lambda_{K_0}\)-mass; restrict to them. The resulting set \(G\) satisfies
\[
\begin{aligned}
&\mu\bigl(G\cap p^{-1}(Y)\bigr)\\
&\quad\le\int_{Y\cap\{\phi\le M\}\setminus S}\phi\,dp\le M|Y|
\end{aligned}
\]
for Borel \(Y\subseteq D\).
Absolute continuity of the image of edge mass alone would not give this; the singular part of the vertex measure had to be removed.

Finally, cover \(D\) by countably many disks of radius \(h_0/8\), restrict \(G\) to one meeting it in positive \(\lambda_{K_0}\)-mass, and fix \(p_0\in p(G)\). Then \(|p-p_0|<h_0/4\) for all \(p\in p(G)\). In each configuration translate and rescale the plane so that
\[
L_n(p_0)=0,\qquad U_n(p_0,h_0)=1 .
\]
The defining inequalities of \(\mathcal P_{T,m}\) are unchanged.

## 3. Bounds at fixed scales

**Lemma 3.1** (radial enclosure). For \(\bar B(p,h)\subseteq D\),
\[
\begin{aligned}
&B\bigl(L_n(p),V_n(p,h)\bigr)\\
&\quad\subseteq L_n\bigl(B(p,h)\bigr)\\
&\quad\subseteq\bar B\bigl(L_n(p),U_n(p,h)\bigr),
\end{aligned}
\]
and every point outside \(B(p,h)\) has image at distance at least \(V_n(p,h)\) from \(L_n(p)\).

*Proof.* \(L_n\) is a homeomorphism of \(D\) onto the plane, so \(L_n(B(p,h))\) is open, \(L_n(\bar B(p,h))\) is compact, and the boundary of \(L_n(B(p,h))\) is the image of the circle. A segment from \(L_n(p)\) to a point outside \(L_n(B(p,h))\) leaves this open set through a boundary point, at distance at least \(V_n(p,h)\). The largest distance from \(L_n(p)\) on the compact set \(L_n(\bar B(p,h))\) is attained at a boundary point, since an interior point can be moved further away, so it is at most \(U_n(p,h)\). A point outside \(B(p,h)\) has its image outside \(L_n(B(p,h))\), by injectivity. \(\square\)

**Lemma 3.2.** For \(p\in p(G)\) and \(j\ge1\), in all sufficiently late configurations, with a threshold depending on \(p\) and \(j\),
\[
\begin{gathered}
|L_n(p)|\le1,\qquad V_n(p,h_j)\ge\alpha^{j+1},\\
U_n(p,h_j)\le2\beta_T^{\,j-1}.
\end{gathered}
\]

*Proof.* Since \(T\ge2\) and \(|p-p_0|<h_0/4\), \(B(p_0,h_1)\subseteq B(p,h_0)\) and \(\bar B(p,h_1)\subseteq B(p_0,h_0)\). Late, \(V_n(p_0,h_1)\ge\alpha U_n(p_0,h_0)=\alpha\), so by Lemma 3.1 the set \(L_n(B(p,h_0))\) contains \(B(0,\alpha)\), and its largest distance from \(L_n(p)\), which is \(U_n(p,h_0)\), is at least \(\alpha\). Also \(L_n(\bar B(p,h_1))\subseteq L_n(B(p_0,h_0))\subseteq\bar B(0,1)\), so \(|L_n(p)|\le1\) and \(U_n(p,h_1)\le2\). Iterating the inequalities of \(\mathcal P_{T,m}\) at \(p\) for the first \(j\) radii, with \(V_n\le U_n\), gives \(V_n(p,h_j)\ge\alpha^jU_n(p,h_0)\ge\alpha^{j+1}\) and \(U_n(p,h_j)\le\beta_T^{\,j-1}U_n(p,h_1)\le2\beta_T^{\,j-1}\). \(\square\)

## 4. One limit position

Let \(X\) be the one-point compactification of the plane, a compact metric space (for example the sphere, with the chordal metric). Let \(\Gamma_n\subseteq[0,1]^2\times X\) be the closure of the graph of \(L_n\). By Theorem 4.1 of [Measures on compact metric spaces](measures-on-compact-metric-spaces.md), along a subsequence \(\Gamma_n\to\Gamma\) in Hausdorff distance. Over a point \(u\in D\), \(\Gamma_n\) contains only \((u,L_n(u))\), by continuity of \(L_n\).

*Proof of (a).* Let \(p\in p(G)\). The points \((p,L_n(p))\) have \(|L_n(p)|\le1\) for late \(n\) (Lemma 3.2), so they have limit points, which lie in \(\Gamma\) by Lemma 4.2(a) there: the fiber of \(\Gamma\) over \(p\) is nonempty. A point \((p,x)\in\Gamma\) is the limit of points \((u_n,L_n(u_n))\in\Gamma_n\) with \(u_n\to p\); late, \(u_n\in B(p_0,h_0)\), whose image lies in \(\bar B(0,1)\), so \(|x|\le1\). If \((p,x)\) and \((p,y)\) are in \(\Gamma\), choose such approximations at the same indices. For fixed \(j\), late, both \(u_n\) and \(u'_n\) lie in \(B(p,h_j)\), and by Lemmas 3.1 and 3.2 their images are within \(2U_n(p,h_j)\le4\beta_T^{\,j-1}\) of each other. So \(|x-y|\le4\beta_T^{\,j-1}\) for every \(j\), and \(x=y\) since \(\beta_T<1\). Call this point \(l(p)\). The bounded sequence \(L_n(p)\) has all its limit points in the fiber, so \(L_n(p)\to l(p)\). \(\square\)

*Proof of (b).* Let \(p\ne q\) in \(p(G)\), \(d=|p-q|<h_0/2\), and let \(j\ge1\) be least with \(h_j<d\); then \(h_j\ge d/T\). The point \(q\) is outside \(B(p,h_j)\), so by Lemmas 3.1 and 3.2, late, \(|L_n(q)-L_n(p)|\ge V_n(p,h_j)\ge\alpha^{j+1}\). Both sequences converge, so
\[
\begin{aligned}
|l(q)-l(p)|&\ge\alpha^{j+1}=\alpha\Bigl(\frac{h_j}{h_0}\Bigr)^{1+\eta}\\
&\ge\frac\alpha{(Th_0)^{1+\eta}}\,d^{1+\eta}. \qquad\square
\end{aligned}
\]
Only finitely many scales are used for each pair, so no common threshold over \(G\) is needed.

## 5. The spatial measure

Attach to each vertex \(q\) of configuration \(n\) its normalized position, which is \(L_n(p(z(q)))\), as a label in \(X\), and define the vertex, participating-vertex and edge measures on \(Z\times X\) and \(Z\times X\times[0,1]\) as in [Limiting measures](limiting-measures.md). Pass to a subsequence along which they converge weakly; their images on the old coordinates are the old limits. The image of the vertex measures on the pair \((p(z),x)\) is concentrated on the graph of \(L_n\), so by Lemma 4.2(c) of [Measures on compact metric spaces](measures-on-compact-metric-spaces.md) its limit is concentrated on \(\Gamma\). Restricting the limit to the labels with \(z\in G\), which is done after the limit, the position \(x\) equals \(l(p(z))\) almost everywhere, by (a). Let \(\beta\) be the image of this restricted measure on the position coordinate.

*Proof of (c).* If a disk of radius \(r\) contains \(l(p)\) and \(l(q)\), then \(|p-q|\le\rho_r=(2r/c_G)^{1/(1+\eta)}\) by (b), so the set of \(p\in p(G)\) with \(l(p)\in B(x,r)\) lies in a disk \(Y\) of radius \(\rho_r\). By the density bound of Section 2,
\[
\begin{aligned}
\beta(B(x,r))&\le\mu\bigl(G\cap p^{-1}(Y)\bigr)\\
&\le M\pi\rho_r^2=C_Gr^{2/(1+\eta)} .
\end{aligned}
\]
\(\beta\) is carried by the closed unit disk, and the part of a strip of width \(r\) inside it is covered by at most \(4/r+2\) disks of radius \(r\), which gives the strip bound with \(d_*-1\). A line lies in strips of every width, so it has mass zero. \(\square\)

The enhanced measures keep all the relations of [Limiting measures](limiting-measures.md): \(\mu_J\le\mu\); \(\lambda_{K_0}(\{z\in G\})=\lambda_{K_0}(G)>0\) for the enhanced edge measure; and the inequality \(\lambda_J(F)^3\le Cs_J^3\mu_J(F)\) for Borel sets of enhanced labels, by its last assertion (Lemma 2.1 there).

## 6. Exercises

**6.1** (easy). Check that \(1/(C_pT)\ge T^{-1-\eta}\) and \(C_p/T\le T^{-1+\eta}\) when \(C_p\le T^\eta\).

**6.2** (medium). Let \(l\) be a map from a set \(P\subseteq\mathbb R^2\) to the plane with \(|l(p)-l(q)|\ge c|p-q|^{1+\eta}\), and let \(\mu\) on \(P\) have \(\mu(Y)\le M|Y|\) for disks \(Y\). Show that the image measure gives a disk of radius \(r\) mass at most \(C r^{2/(1+\eta)}\), and that this exponent cannot be improved in general.

**6.3** (medium). Why does the proof remove the singular part of the image of \(\mu\), rather than of the image of \(\lambda\)?

## 7. Solutions

**6.1.** \(1/(C_pT)\ge1/(T^\eta T)=T^{-1-\eta}\), and \(C_p/T\le T^\eta/T\).

**6.2.** As in the proof of (c): the preimage of a disk of radius \(r\) has diameter at most \(2(2r/c)^{1/(1+\eta)}\). For \(l(p)=|p|^\eta p\) on a disk around \(0\) and \(\mu\) Lebesgue measure, \(|l(p)-l(q)|\ge c|p-q|^{1+\eta}\) holds near \(0\), and the disk of radius \(r\) about \(0\) has preimage the disk of radius \(r^{1/(1+\eta)}\), of area \(\pi r^{2/(1+\eta)}\).

**6.3.** The disk and strip bounds concern participating vertices, which are counted by the vertex measures \(\mu_J\le\mu\) in [Boundary activity](boundary-activity.md). The image of edge mass is already absolutely continuous, but that does not bound the vertex measure: a set of vertices of small edge mass but large vertex mass would escape the bound.

## References

- [Fremlin] D. H. Fremlin, *Measure Theory*, Volume 2, 232E (Radon–Nikodym theorem) and 232I (Lebesgue decomposition); the text of the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10). https://www1.essex.ac.uk/maths/people/fremlin/mt.htm
- [OpenAI-HL] OpenAI, *A power saving for planar halving lines*, OpenAI Math Release preprint, 25 September 2026, Section 6. https://github.com/openai/math/tree/main/preprints/A-power-saving-for-planar-halving-lines-September-25-2026
