# Independent gradients and tangent directions

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson extracts local geometry from the limiting measures of [Limiting measures](limiting-measures.md) [OpenAI-HL, Section 4]. A fixed pair of windows \(A,B\) gives every label a position \(p\) in the open unit square, and every other rank coordinate becomes, in the limit, a monotone function \(f_C\) of \(p\), differentiable at almost every \(p\). Two consequences are proved. First, on a positive part of edge mass, every window active at a label contains two windows whose gradients at \(p\) are independent; this uses the crossing measures and the critical-image lemma of [Monotone functions of two variables](monotone-functions-of-two-variables.md). Second, lines of a fixed direction \(t\) of the sweep have, after zooming in at \(p\), limiting directions confined to an arc \(D_p(t)\), and arcs for different times are disjoint when edge activity separates the times. Three times with three different single directions are found; the next lessons turn them into a Euclidean normalization.

We keep the subsequence of configurations of [Limiting measures](limiting-measures.md) and pass to further subsequences when needed; every statement about "late configurations" refers to the current subsequence.

## 1. A pair of windows

By Lemma 3.1 of [Limiting measures](limiting-measures.md), for \(\lambda\)-almost every \(z\) the measure \(h_z\) has no atoms, so its support in \((0,1)\) is infinite, and two dyadic windows whose closures are disjoint and lie in \((0,1)\) both have positive \(h_z\)-mass. There are countably many pairs of windows, so we can fix such windows \(K,K'\) for which
\[
E=\{z:h_z(K)>0,\ h_z(K')>0\}
\]
has \(\lambda(E)>0\).

Lemma 4.1 of [Limiting measures](limiting-measures.md), applied to \(K'\), and \(\lambda_{K'}=h_z(K')\lambda\) with \(h_z(K')>0\) on \(E\), show that \(\lambda|_E\) vanishes on every set that is null for all crossing measures \(\sigma_{CD}\) with \(C,D\subseteq K'\) disjoint. Let \(\Sigma=\sum c_{CD}\sigma_{CD}\) over these countably many pairs, with positive weights and finite total mass, and let \(g_{CD}\) be a density of \(\sigma_{CD}\) with respect to \(\Sigma\) [Fremlin, 232E]. Since \(\sum c_{CD}g_{CD}=1\) \(\Sigma\)-almost everywhere, the sets \(\{g_{CD}>0\}\) cover \(Z\) up to a \(\Sigma\)-null, hence \(\lambda|_E\)-null, set; so one of them, \(\{g_{AB}>0\}\), meets \(E\) in a set of positive \(\lambda\)-measure. Replace \(E\) by this intersection, and name the windows so that \(A\) precedes \(B\). If \(F\subseteq E\) is \(\sigma_{AB}\)-null, then \(\int_Fg_{AB}\,d\Sigma=0\), so \(\Sigma(F)=0\) and \(\lambda(F)=0\). Thus
\[
\lambda|_E\ \text{vanishes on }\sigma_{AB}\text{-null sets.}
\]
For a label \(z\) put \(p(z)=(z_A,z_B)\in[0,1]^2\). By Lemma 1.1(c) of [Limiting measures](limiting-measures.md), the image of \(\sigma_{AB}\) under \(p\) is at most Lebesgue measure, so the image of \(\lambda|_E\) under \(p\) vanishes on Lebesgue-null sets: it is absolutely continuous. In particular \(p(z)\in(0,1)^2\) for \(\lambda\)-almost every \(z\in E\).

## 2. Limit functions

Every window \(C\subseteq K\) is disjoint from \(A\) and \(B\), and since \(K\) and \(K'\) are disjoint, \(C\) either precedes both or follows both. By Proposition 3.3 of [Rank coordinates](rank-coordinates.md), in each configuration
\[
F_C^{(n)}=r_C\circ(r_A,r_B)^{-1}:(0,1)^2\to(0,1)
\]
is monotone in each coordinate with signs \((+,-)\) if \(C\) precedes \(A\) and \((-,+)\) if \(B\) precedes \(C\). Reflecting a coordinate where it decreases, we treat it as nondecreasing in both; write \(u<w\) when \(u_1<w_1\) and \(u_2<w_2\) in the reflected coordinates. Let \(G\) be the points of \((0,1)^2\) with rational coordinates. A diagonal subsequence makes \(F_C^{(n)}(q)\) converge, to \(\phi_C(q)\), for all \(q\in G\) and all the countably many \(C\). Define
\[
\begin{gathered}
f_C(p)=\sup\{\phi_C(q):q\in G,\ q<p\},\\
\bar f_C(p)=\inf\{\phi_C(q):q\in G,\ q>p\}.
\end{gathered}
\]
Both are nondecreasing and \(f_C\le\bar f_C\); \(f_C\) is Borel, as a countable supremum of Borel functions. Call \(p\) *regular* for \(C\) if \(f_C(p)=\bar f_C(p)\).

**Lemma 2.1.** (a) If \(p\) is regular for \(C\) and \(p_n\to p\), then \(F_C^{(n)}(p_n)\to f_C(p)\).

(b) Every point where \(f_C\) is continuous is regular for \(C\). Almost every point of \((0,1)^2\) is regular, and \(f_C\) is differentiable at almost every point.

*Proof.* (a) For grid points \(q^-<p<q^+\), eventually \(q^-<p_n<q^+\), so \(F_C^{(n)}(q^-)\le F_C^{(n)}(p_n)\le F_C^{(n)}(q^+)\); in the limit,
\[
\begin{aligned}
\phi_C(q^-)&\le\liminf F_C^{(n)}(p_n)\\
&\le\limsup F_C^{(n)}(p_n)\le\phi_C(q^+).
\end{aligned}
\]
Taking the supremum over \(q^-\) and the infimum over \(q^+\) gives \(f_C(p)\le\liminf\) and \(\limsup\le\bar f_C(p)=f_C(p)\).

(b) If \(p<p''\), a grid point \(q\) with \(p<q<p''\) has \(\bar f_C(p)\le\phi_C(q)\le f_C(p'')\). Letting \(p''\to p\) at a continuity point gives \(\bar f_C(p)\le f_C(p)\). By Theorem 2.2 of [Monotone functions of two variables](monotone-functions-of-two-variables.md), \(f_C\), which is bounded, Borel and monotone in each variable, is differentiable, hence continuous, almost everywhere. \(\square\)

**Lemma 2.2** (coordinate identities). Let \(z\) lie in the support of \(\lambda\), with \(p=p(z)\in(0,1)^2\) regular for \(C\). Then \(z_C=f_C(p)\).

*Proof.* For every \(k\), the ball of radius \(1/k\) about \(z\) has positive \(\lambda\)-mass, so by Lemma 2.1(a) of [Measures on compact metric spaces](measures-on-compact-metric-spaces.md) it contains the label of a left endpoint of an edge in every late configuration. Choosing diagonally, there are vertices \(q_n\) of configuration \(n\) whose labels \(z^{(n)}\) tend to \(z\). Then \(p(z^{(n)})=(r_A,r_B)(q_n)\to p\) and \(z^{(n)}_C=r_C(q_n)=F_C^{(n)}(p(z^{(n)}))\), which tends to \(f_C(p)\) by Lemma 2.1(a); it also tends to \(z_C\). \(\square\)

The points \(p\) that fail to be regular for some \(C\), or where some \(f_C\) is not differentiable, form a Lebesgue-null set, a countable union of null sets. Its preimage under \(p\) is \(\lambda|_E\)-null, by absolute continuity. Removing it, and the \(\lambda\)-null complement of the support of \(\lambda\), from \(E\), we may assume that for every \(z\in E\): \(p=p(z)\in(0,1)^2\), every \(f_C\) with \(C\subseteq K\) is differentiable at \(p\), and \(z_C=f_C(p)\).

## 3. Independent gradients

**Lemma 3.1.** After removing a further \(\lambda\)-null set from \(E\), every \(z\in E\) has the following property: if \(J\subseteq K\) is a window with \(h_z(J)>0\), then some disjoint windows \(C,D\subseteq J\) satisfy
\[
\det\begin{pmatrix}\nabla f_C(p)\\\nabla f_D(p)\end{pmatrix}\ne0,\qquad p=p(z).
\]

*Proof.* Fix \(J\subseteq K\), and let \(B_J\) be the set of \(z\in E\) with \(h_z(J)>0\) at which the determinant vanishes for all disjoint \(C,D\subseteq J\). For each such pair, Lemma 3.1 of [Monotone functions of two variables](monotone-functions-of-two-variables.md), applied to \(F=(f_C,f_D)\) on \((0,1)^2\), gives a Borel null set \(N_{CD}\) containing the values \(F(p)\) at the points where \(F\) is differentiable with \(\det DF(p)=0\). For \(z\in B_J\), \((z_C,z_D)=(f_C(p),f_D(p))\in N_{CD}\), by Lemma 2.2. By Lemma 1.1(c) of [Limiting measures](limiting-measures.md), the image of \(\sigma_{CD}\) under \(z\mapsto(z_C,z_D)\) is at most Lebesgue measure, so \(\sigma_{CD}(B_J)=0\). This holds for all disjoint \(C,D\subseteq J\), so Lemma 4.1 of [Limiting measures](limiting-measures.md) gives \(\lambda_J(B_J)=0\), that is, \(\int_{B_J}h_z(J)\,d\lambda=0\). Since \(h_z(J)>0\) on \(B_J\), \(\lambda(B_J)=0\). Remove \(B_J\) for all countably many \(J\). \(\square\)

## 4. First-order expansions

Fix \(z\in E\) and \(p=p(z)\).

**Lemma 4.1.** Let \(\mathcal C\) be a finite set of windows in \(K\), \(\rho<\infty\) and \(\epsilon>0\). There is \(h_0>0\) such that for every \(h\in(0,h_0)\) there is \(n_0(h)\) with
\[
\begin{aligned}
&\bigl|F_C^{(n)}(p+hw)-f_C(p)\\
&\quad-h\nabla f_C(p)\cdot w\bigr|\le\epsilon h
\end{aligned}
\]
for all \(C\in\mathcal C\), \(|w|\le\rho\) and \(n\ge n_0(h)\).

*Proof.* Let \(\eta>0\) be small. By differentiability, for \(h<h_0\) the function \(f_C(p+hw)\) differs from \(f_C(p)+h\nabla f_C(p)\cdot w\) by at most \(\eta h\) for \(|w|\le\rho+1\) and all \(C\in\mathcal C\). Fix such \(h\). Regular points are dense, so there is a finite set of regular points \(q\) in the disk of radius \((\rho+1)h\) about \(p\) such that every point \(x=p+hw\), \(|w|\le\rho\), has points of the set in each of the four closed quadrants with vertex \(x\), within distance \(\eta h/(1+\max_C|\nabla f_C(p)|)\) of \(x\). For each \(C\), two of them satisfy \(q^-\le x\le q^+\) in the order of the reflected chart of \(C\). By Lemma 2.1(a) with constant sequences, \(F_C^{(n)}(q)\to f_C(q)\) at these finitely many points; take \(n_0(h)\) with all errors at most \(\eta h\). Monotonicity squeezes \(F_C^{(n)}(p+hw)\) between \(F_C^{(n)}(q^\pm)\), which are within \(\eta h+\eta h+\eta h\) of \(f_C(p)+h\nabla f_C(p)\cdot w\). Choose \(\eta=\epsilon/3\). \(\square\)

A *fast diagonal* is a pair of sequences \(h_j\downarrow0\) and indices \(n_j\to\infty\) such that for every finite \(\mathcal C\), every \(\rho\) and every \(\epsilon>0\), the inequality of Lemma 4.1 holds with \(h=h_j\), \(n=n_j\) for all large \(j\). Fast diagonals exist: enumerate the windows of \(K\) as \(C_1,C_2,\dots\), and for each \(j\) choose \(h_j<h_0\) and \(n_j\ge n_0(h_j)\) for \(\mathcal C=\{C_1,\dots,C_j\}\), \(\rho=j\) and \(\epsilon=1/j\). Subsequences of fast diagonals are fast diagonals. For a point \(X\) of configuration \(n_j\), its *zoom coordinate* is \(w=((r_A,r_B)(X)-p)/h_j\).

## 5. Tangent directions

For \(t\) in the interior \(K^\circ\) of \(K\), the direction \(\varsigma(t)\) of [Rank coordinates](rank-coordinates.md) lies, in late configurations, outside the spans of \(A\) and \(B\), on the same side of both, because \(t\) and \(K'\) are separated by a positive gap. By Exercise 7.3 of [Rank coordinates](rank-coordinates.md), along a line of direction \(t\), oriented by increasing first coordinate, both \(r_A\) and \(r_B\) increase strictly if the span of \(K\) lies above those of \(A,B\), and both decrease strictly otherwise. Let \(Q\) be the corresponding closed quadrant, \(\{w:w_1,w_2\ge0\}\) or \(\{w:w_1,w_2\le0\}\); forward displacements along lines of direction \(t\) have rank displacements in \(Q\).

Say that a window \(C\subseteq K\) lies *strictly before* \(t\) if its closure lies in \([0,t)\), and *strictly after* \(t\) if its closure lies in \((t,1]\). For \(t\in K^\circ\) let \(D_p(t)\) be the set of unit vectors \(d\in Q\) with \(\nabla f_C(p)\cdot d\ge0\) for every window \(C\subseteq K\) lying strictly before \(t\), and \(\nabla f_C(p)\cdot d\le0\) for every \(C\subseteq K\) lying strictly after \(t\). It is the intersection of the unit circle with a closed convex cone inside \(Q\), so a closed arc of length at most \(\pi/2\), or empty.

**Lemma 5.1** (directions of lines). Let \((h_j,n_j)\) be a fast diagonal and \(t\in K^\circ\). Let \(X_j,Y_j\) lie on one line of direction \(t\) in configuration \(n_j\), with \(Y_j\) forward of \(X_j\), and suppose their zoom coordinates converge to \(w\ne w'\). Then \((w'-w)/|w'-w|\in D_p(t)\). Moreover \(D_p(t)\) is not empty.

*Proof.* The rank displacement from \(X_j\) to \(Y_j\) lies in \(Q\), so \(w'-w\in Q\). Let \(C\subseteq K\) lie strictly before \(t\). In late configurations the span of \(C\) lies below \(\varsigma(t)\), so \(r_C\) increases along the line (Exercise 7.3 of [Rank coordinates](rank-coordinates.md)), and \(F_C^{(n_j)}\) at the rank point of \(Y_j\) is at least its value at that of \(X_j\). By the fast diagonal, these values are \(f_C(p)+h_j\nabla f_C(p)\cdot w_j+o(h_j)\) and the same with \(w'_j\), where \(w_j\to w\) and \(w'_j\to w'\) are the zoom coordinates; so \(\nabla f_C(p)\cdot(w'-w)\ge0\). For \(C\) strictly after \(t\) the inequality is reversed.

For non-emptiness, let \(X_j\) be the point of configuration \(n_j\) with \((r_A,r_B)(X_j)=p\), and follow the forward ray of direction \(t\) from \(X_j\). The preimage of the closed disk of radius \(h_j\) about \(p\) is compact, by Proposition 3.2 of [Rank coordinates](rank-coordinates.md), so the ray leaves it; let \(Y_j\) be its first point with zoom coordinate of length one. Along a subsequence these zoom coordinates converge to some \(w'\) of length one, and the first part gives \(w'\in D_p(t)\). \(\square\)

**Lemma 5.2** (separated directions). Let \(s<t\) lie in \(K^\circ\) with \(h_z((s,t))>0\). Then \(D_p(s)\cap D_p(t)=\varnothing\). There are times \(\tau_1<\tau_2<\tau_3\) in \(K^\circ\) for which \(D_p(\tau_i)\) are single unit vectors \(d_i\), no two of them parallel.

*Proof.* Choose a window \(J\) whose closure lies in \((s,t)\) with \(h_z(J)>0\); one exists, since \((s,t)\) is a countable union of such windows. By Lemma 3.1 there are disjoint \(C,D\subseteq J\) with independent gradients. Both lie strictly after \(s\) and strictly before \(t\). A vector in \(D_p(s)\cap D_p(t)\) would have nonpositive and nonnegative scalar products with both gradients, hence zero products, and would be zero.

Let \(T\) be the support of \(h_z\) in \(K^\circ\), with the endpoints of the components of \(K^\circ\setminus T\) removed; only countably many points are removed, and \(h_z(T)=h_z(K)>0\) since \(h_z\) has no atoms. Two points \(s<t\) of \(T\) have \(h_z((s,t))>0\): otherwise \((s,t)\) would lie in a component of the complement of the support, with \(s\) and \(t\) among its endpoints. So the arcs \(D_p(t)\), \(t\in T\), are pairwise disjoint and nonempty. Disjoint arcs of positive length contain different rational angles, so only countably many \(t\in T\) have \(D_p(t)\) of positive length; removing them leaves a set of positive \(h_z\)-measure, in particular three points \(\tau_1<\tau_2<\tau_3\). Their directions lie in the quadrant \(Q\) and are distinct, so no two are parallel. \(\square\)

## 6. One triple for all labels

The times of Lemma 5.2 depend on \(z\). A common normalization of the configurations needs one fixed triple. For every \(z\in E\), since \(h_z\) has no atoms and \(h_z(K)>0\), there are rational times \(t_1<t_2<t_3\) in \(K^\circ\) with \(h_z((t_1,t_2))>0\) and \(h_z((t_2,t_3))>0\). There are countably many rational triples, so one triple serves on a subset of \(E\) of positive \(\lambda\)-measure; then a window \(K_0\) with closure in \((t_1,t_2)\) has \(h_z(K_0)>0\) on a subset of positive measure. Restrict \(E\) to it. We have reached:

**Proposition 6.1.** There are windows \(A,B\) and \(K_0\), times \(t_1<t_2<t_3\) in \(K^\circ\) with \(K_0\) inside \((t_1,t_2)\), and a Borel set \(E\subseteq Z\) with \(\lambda_{K_0}(E)>0\), such that the image of \(\lambda|_E\) under \(p\) is absolutely continuous, and for every \(z\in E\) and \(p=p(z)\): every \(f_C\), \(C\subseteq K\), is differentiable at \(p\) with \(z_C=f_C(p)\); Lemma 3.1 holds at \(z\); \(D_p(t_1),D_p(t_2),D_p(t_3)\) are pairwise disjoint closed arcs; and three times \(\tau_1<\tau_2<\tau_3\) in \(K^\circ\) have single, pairwise non-parallel directions \(D_p(\tau_i)=\{d_i\}\).

The disjointness of the three arcs follows from Lemma 5.2, since \(h_z((t_1,t_2))\), \(h_z((t_2,t_3))\) and \(h_z((t_1,t_3))\) are positive. \(\lambda_{K_0}(E)=\int_Eh_z(K_0)\,d\lambda>0\).

## 7. Exercises

**7.1** (easy). Show that the intersection of a closed convex cone contained in a closed quadrant with the unit circle is a closed arc of length at most \(\pi/2\), or empty.

**7.2** (medium). In Lemma 2.1, give an example of nondecreasing functions \(F^{(n)}\) on \((0,1)\), converging at rational points, for which \(F^{(n)}(p_n)\) does not converge to \(f(p)\) at a point \(p\) where \(f\) jumps. Why does this not harm the argument?

**7.3** (medium). Why must \(C\) and \(D\) in Lemma 3.1 be windows inside \(J\), rather than arbitrary windows of \(K\)?

## 8. Solutions

**7.1.** In polar angle, a closed convex cone of angle less than \(\pi\) is the set of vectors with angle in a closed interval; inside a quadrant this interval has length at most \(\pi/2\).

**7.2.** Let \(F^{(n)}=\mathbf 1_{[1/2+1/n,1)}\) on \((0,1)\). At every rational \(q\), \(F^{(n)}(q)\to\mathbf 1_{q>1/2}\), so \(f(1/2)=0\) and \(\bar f(1/2)=1\): the point \(1/2\) is not regular. Along \(p_n=1/2+2/n\to1/2\), \(F^{(n)}(p_n)=1\), which does not tend to \(f(1/2)\). The lemma is applied only at regular points, which fill the square up to a null set, and the measures involved do not charge null sets of the square.

**7.3.** The conclusion is used to separate the directions \(D_p(s)\) and \(D_p(t)\), and this needs windows lying strictly between \(s\) and \(t\). Windows elsewhere in \(K\) give constraints of the same sign at both times.

## References

- [Fremlin] D. H. Fremlin, *Measure Theory*, Volume 2, 232E (Radon–Nikodym theorem); the text of the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10). https://www1.essex.ac.uk/maths/people/fremlin/mt.htm
- [OpenAI-HL] OpenAI, *A power saving for planar halving lines*, OpenAI Math Release preprint, 25 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/A-power-saving-for-planar-halving-lines-September-25-2026
