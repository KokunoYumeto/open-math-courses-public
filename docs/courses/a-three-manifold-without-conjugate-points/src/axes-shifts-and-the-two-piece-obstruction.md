# Axes, shifts and the two-piece obstruction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves that the manifold \(M\) of [The manifold and its fundamental group](the-manifold-and-its-fundamental-group.md) carries no Riemannian metric of nonpositive sectional curvature, and more generally that its fundamental group admits no proper cocompact isometric action on a proper CAT(0) space ([OpenAI-NC, Theorem 2.1, Proposition 2.3]). Isometries of a space with the CN inequality have translation lengths and minimal sets; a hyperbolic isometry has axes, and elements commuting with it shift its axes by a well-defined amount, which defines a homomorphism to the real numbers. Commutators have shift zero, and for an element of shift zero the translation lengths obey an exact Pythagorean formula. In \(M\), each surface boundary is a commutator in the centralizer of its circle factor, so each piece gives such a formula, and the twisted gluing makes the two formulas contradict each other.

- Translation length, minimal sets and axes (Section 1).
- Shifts and the length formula (Section 2).
- Proper cocompact actions (Section 3).
- The obstruction (Section 4).

Throughout, \(X\) is a CN space as in [Spaces with the CN inequality](spaces-with-the-cn-inequality.md), whose results are quoted by number with the prefix CN.

## 1. Translation length, minimal sets and axes

For an isometry \(g\) of \(X\), the *displacement* is \(d_g(x)=d(x,gx)\), the *translation length* is \(\ell(g)=\inf_xd_g(x)\), and the *minimal set* is \(\operatorname{Min}(g)=\{x:d_g(x)=\ell(g)\}\). The isometry is *semisimple* if \(\operatorname{Min}(g)\ne\varnothing\), and *hyperbolic* if it is semisimple with \(\ell(g)>0\). A semisimple isometry with \(\ell(g)=0\) fixes a point. We write \(C(g)\) for the set of isometries commuting with \(g\).

**Lemma 1.1.** (1) \(d_g\) is \(2\)-Lipschitz and convex along every geodesic segment parametrized proportionally to arc length. (2) \(\operatorname{Min}(g)\) is closed and convex, hence complete if \(X\) is complete. (3) \(\ell(kgk^{-1})=\ell(g)\) for every isometry \(k\), and every \(h\in C(g)\) satisfies \(h(\operatorname{Min}(g))=\operatorname{Min}(g)\).

*Proof.* (1) \(|d(x,gx)-d(y,gy)|\le2d(x,y)\), by the triangle inequality and \(d(gx,gy)=d(x,y)\). If \(c\) is a geodesic segment, so is \(g\circ c\), and CN Proposition 2.3 gives convexity of \(t\mapsto d(c(t),gc(t))\). (2) \(\operatorname{Min}(g)=\{d_g\le\ell(g)\}\) is closed by continuity; if \(x,y\) lie in it, the convex function \(d_g\) is at most \(\ell(g)\) at the ends of \([x,y]\), hence on all of it. (3) \(d_{kgk^{-1}}(kx)=d(kx,kgx)=d_g(x)\); for \(h\in C(g)\) this reads \(d_g(hx)=d_g(x)\), and \(h^{-1}\in C(g)\) as well. \(\square\)

**Proposition 1.2** (axes). Let \(g\) be hyperbolic, \(\ell=\ell(g)\) and \(x\in\operatorname{Min}(g)\).

1. \(d(g^jx,g^kx)=|j-k|\,\ell\) for all integers \(j,k\).
2. The segments \([g^kx,g^{k+1}x]\), \(k\in\mathbb Z\), concatenate to a geodesic line \(c\) with \(c(0)=x\) and \(g\,c(s)=c(s+\ell)\) for all \(s\). We call such a line an *axis* of \(g\).
3. \(\ell(g^n)=|n|\,\ell\), and \(\operatorname{Min}(g)\subseteq\operatorname{Min}(g^n)\), for every \(n\ne0\).

Every axis lies in \(\operatorname{Min}(g)\), and every point of \(\operatorname{Min}(g)\) lies on an axis.

*Proof.* First, \(\ell(g^2)\ge2\ell(g)\) for every isometry \(g\): for \(y\in X\), let \(\mu\) be the midpoint of \([y,gy]\); then \(g\mu\) is the midpoint of \([gy,g^2y]\), and CN Lemma 2.2, applied from the point \(gy\), gives \(d(\mu,g\mu)\le\frac12d(y,g^2y)\), so \(d(y,g^2y)\ge2\ell(g)\). For \(x\in\operatorname{Min}(g)\), \(d(x,g^2x)\le2\ell\); hence \(\ell(g^2)=2\ell\) and \(x\in\operatorname{Min}(g^2)\). Applying this to \(g^2,g^4,\dots\) gives \(d(x,g^{2^m}x)=2^m\ell\) for all \(m\). For \(0<n<2^m\),
\[
\begin{aligned}
2^m\ell&=d(x,g^{2^m}x)\\
&\le d(x,g^nx)+d(g^nx,g^{2^m}x)\\
&\le d(x,g^nx)+(2^m-n)\ell,
\end{aligned}
\]
so \(d(x,g^nx)\ge n\ell\), and the triangle inequality gives equality. Since \(g\) is an isometry, (1) follows.

(2) Parametrize the concatenation by arc length, \(c(k\ell)=g^kx\). For \(a<b\) with \(a\in[j\ell,(j+1)\ell]\) and \(b\in[k\ell,(k+1)\ell]\), \(j\le k\), the path from \(c(a)\) to \(c(b)\) has length \(b-a\), so \(d(c(a),c(b))\le b-a\); and by (1)
\[
\begin{aligned}
(k+1-j)\ell&\le(a-j\ell)+d(c(a),c(b))\\
&\quad+((k+1)\ell-b),
\end{aligned}
\]
so \(d(c(a),c(b))\ge b-a\). The isometry \(g\) maps \([g^kx,g^{k+1}x]\) onto \([g^{k+1}x,g^{k+2}x]\) by uniqueness of segments, hence \(gc(s)=c(s+\ell)\).

(3) \(g^n\) maps \(c(\mathbb R)\) onto itself, so by CN Proposition 3.1 the projection \(\pi_c\) commutes with \(g^n\) and does not increase distances: \(d(\pi_cy,g^n\pi_cy)\le d(y,g^ny)\) for all \(y\). On the line, \(d(c(s),g^nc(s))=|n|\ell\). So \(\ell(g^n)=|n|\ell\), attained at \(x\).

Finally, \(d(c(s),gc(s))=\ell\) on an axis, and (2) puts every point of \(\operatorname{Min}(g)\) on an axis. \(\square\)

**Lemma 1.3.** Let \(g\) be hyperbolic. (1) Any two axes of \(g\) are parallel. (2) If \(h\in C(g)\) and \(c\) is an axis of \(g\), then \(h\circ c\) is an axis of \(g\).

*Proof.* (1) For axes \(c_1,c_2\), the function \(d(c_1(s),c_2(s))\) is continuous and periodic of period \(\ell(g)\), because \(g\) maps both lines forward by \(\ell(g)\); hence it is bounded. (2) \(h\circ c\) is a geodesic line and \(g\,hc(s)=h\,gc(s)=hc(s+\ell(g))\). \(\square\)

## 2. Shifts and the length formula

Let \(g\) be hyperbolic. All its axes are parallel (Lemma 1.3), and \(\operatorname{Min}(g)\) is the union of their images. Fix an axis \(c_0\) and let \(b=b_{c_0}\) be its Busemann function (CN Section 4).

**Proposition 2.1** (the shift homomorphism). For \(h\in C(g)\), the number
\[
\tau_g(h)=b(hx)-b(x)
\]
is the same for all \(x\in\operatorname{Min}(g)\), and it does not depend on the choice of the axis \(c_0\). The map \(\tau_g\colon C(g)\to(\mathbb R,+)\) is a homomorphism, \(\tau_g(g)=-\ell(g)\), and \(\tau_g\) vanishes on the commutator subgroup \([C(g),C(g)]\) and on every element of finite order.

*Proof.* By CN Lemma 4.2(2), \(b(hx)=b_{h^{-1}\circ c_0}(x)\). Since \(h^{-1}\in C(g)\), \(h^{-1}\circ c_0\) is an axis of \(g\) (Lemma 1.3), parallel to \(c_0\), and every point of \(\operatorname{Min}(g)\) lies on a line parallel to \(c_0\). By CN Corollary 4.4, \(b_{h^{-1}\circ c_0}-b=-\sigma(c_0,h^{-1}\circ c_0)\) on \(\operatorname{Min}(g)\). So \(b(hx)-b(x)\) does not depend on \(x\in\operatorname{Min}(g)\). Another axis \(c_0'\) gives a Busemann function differing from \(b\) by a constant on \(\operatorname{Min}(g)\) (CN Corollary 4.4 again), and both \(x\) and \(hx\) lie in \(\operatorname{Min}(g)\), so the difference is unchanged.

For \(h,k\in C(g)\) and \(x\in\operatorname{Min}(g)\), the point \(kx\) lies in \(\operatorname{Min}(g)\) (Lemma 1.1), so
\[
\begin{aligned}
\tau_g(hk)&=\bigl(b(hkx)-b(kx)\bigr)\\
&\quad+\bigl(b(kx)-b(x)\bigr)\\
&=\tau_g(h)+\tau_g(k).
\end{aligned}
\]
With \(x=c_0(0)\), \(\tau_g(g)=b(c_0(\ell(g)))-b(c_0(0))=-\ell(g)\) by CN Lemma 4.2(1). A homomorphism to an abelian group without torsion vanishes on commutators and on elements of finite order. \(\square\)

**Proposition 2.2** (the Pythagorean formula for shift zero). Let \(g\) be hyperbolic, \(h\in C(g)\) with \(\tau_g(h)=0\), and \(x\in\operatorname{Min}(g)\). Then for every integer \(m\)
\[
\begin{aligned}
&d(x,g^mhx)^2\\
&\quad=d(x,hx)^2+m^2\ell(g)^2 .
\end{aligned} \tag{2.1}
\]

*Proof.* Let \(c\) be the axis of \(g\) with \(c(0)=x\) (Proposition 1.2) and \(c'=h\circ c\), an axis through \(hx=c'(0)\), parallel to \(c\). By CN Lemma 4.2(3), \(b_c(c'(u))=\sigma(c,c')-u\). On the other hand, computing \(\tau_g\) with the axis \(c\), \(b_c(c'(u))=b_c(hc(u))\), which equals \(b_c(c(u))+\tau_g(h)=-u\). Hence \(\sigma(c,c')=0\), and CN Proposition 4.1 gives
\[
d(c(s),c'(u))^2=D^2+(s-u)^2,
\]
where \(D=d(c(0),c'(0))=d(x,hx)\).
Since \(g\) and \(h\) commute, \(g^mhx=hg^mx=hc(m\ell(g))=c'(m\ell(g))\), and the formula with \(s=0\), \(u=m\ell(g)\) is (2.1). \(\square\)

**Lemma 2.3.** Let \(X\) be complete, \(g\) semisimple and \(\gamma\in C(g)\). Then \(\ell(\gamma)=\inf_{x\in\operatorname{Min}(g)}d(x,\gamma x)\).

*Proof.* \(\operatorname{Min}(g)\) is nonempty, convex and complete (Lemma 1.1), and \(\gamma\) maps it onto itself. By CN Proposition 3.1(3) and (5), the projection \(\pi\) onto it satisfies \(d(\pi y,\gamma\pi y)=d(\pi y,\pi\gamma y)\le d(y,\gamma y)\) for all \(y\in X\). \(\square\)

**Proposition 2.4** (the length formula). Let \(X\) be complete, \(g\) hyperbolic, and \(h\in C(g)\) semisimple with \(\tau_g(h)=0\). Then for all integers \(m,n\)
\[
\begin{aligned}
&\ell(g^mh^n)^2\\
&\quad=m^2\ell(g)^2+n^2\ell(h)^2 .
\end{aligned} \tag{2.2}
\]

*Proof.* The element \(h^n\) lies in \(C(g)\) and \(\tau_g(h^n)=n\tau_g(h)=0\). By Lemma 2.3 for \(\gamma=g^mh^n\) and by (2.1) for \(h^n\),
\[
\begin{aligned}
&\ell(g^mh^n)^2\\
&\quad=\inf_{x\in\operatorname{Min}(g)}\bigl(d(x,h^nx)^2+m^2\ell(g)^2\bigr)\\
&\quad=\ell(h^n)^2+m^2\ell(g)^2,
\end{aligned}
\]
where Lemma 2.3 was used again for \(\gamma=h^n\). If \(\ell(h)>0\), Proposition 1.2(3) gives \(\ell(h^n)=|n|\ell(h)\); if \(\ell(h)=0\), \(h\) fixes a point, so does \(h^n\), and both sides vanish. \(\square\)

So on the group generated by \(g\) and a commuting element \(h\) of shift zero, the squared translation length is a positive semidefinite quadratic form for which \(g\) and \(h\) are orthogonal.

## 3. Proper cocompact actions

A group \(\Gamma\) acts on \(X\) by isometries *properly* if for every compact \(K\subseteq X\) only finitely many \(\gamma\in\Gamma\) satisfy \(\gamma K\cap K\ne\varnothing\), and *cocompactly* if \(\Gamma K=X\) for some compact \(K\). The metric space \(X\) is *proper* if its closed bounded subsets are compact; a proper metric space is complete.

**Proposition 3.1** ([OpenAI-NC, proof of Theorem 2.1]). Let \(\Gamma\) act properly and cocompactly by isometries on a proper CN space \(X\). Then every element of \(\Gamma\) is semisimple, and every element of infinite order is hyperbolic.

*Proof.* Let \(\gamma\in\Gamma\), choose \(x_n\) with \(d(x_n,\gamma x_n)\to\ell(\gamma)\) and a compact \(K\) with \(\Gamma K=X\), and pick \(k_n\in\Gamma\) with \(y_n=k_nx_n\in K\). Put \(\gamma_n=k_n\gamma k_n^{-1}\); then \(d(y_n,\gamma_ny_n)=d(x_n,\gamma x_n)\). For large \(n\) this is at most \(\ell(\gamma)+1\), so \(\gamma_ny_n\) lies in the closed \((\ell(\gamma)+1)\)-neighbourhood \(N\) of \(K\), which is closed and bounded, hence compact. Since \(\gamma_nN\cap N\ne\varnothing\), properness allows only finitely many distinct \(\gamma_n\). Passing to a subsequence, \(\gamma_n=\gamma_*\) and \(y_n\to y\in K\), so \(d(y,\gamma_*y)=\ell(\gamma)\). With \(k=k_n\) for such \(n\), \(\gamma_*=k\gamma k^{-1}\) and \(d(k^{-1}y,\gamma k^{-1}y)=\ell(\gamma)\), so \(k^{-1}y\in\operatorname{Min}(\gamma)\).

If \(\ell(\gamma)=0\), \(\gamma\) fixes a point \(p\), and so does every power of \(\gamma\). Properness with \(K=\{p\}\) shows that only finitely many elements fix \(p\), so \(\gamma\) has finite order. \(\square\)

**Lemma 3.2** (deck groups). Let \(N\) be a compact connected Riemannian manifold, \(\widetilde N\) its universal covering with the lifted metric, and \(\Delta\) its group of deck transformations. Then \(\widetilde N\) is complete, \(\Delta\) acts by isometries, properly and cocompactly, and \(\Delta\cong\pi_1(N)\).

*Proof.* Deck transformations preserve the lifted metric. Geodesics of \(\widetilde N\) project to geodesics of \(N\), which are defined for all time because \(N\) is compact, and lifting the extended geodesics shows that \(\widetilde N\) is geodesically complete, hence complete by the Hopf–Rinow theorem ([Completeness and the Hopf–Rinow theorem](course:DG-FND/completeness-and-the-hopf-rinow-theorem)); in particular closed balls in \(\widetilde N\) are compact. The isomorphism \(\Delta\cong\pi_1(N)\) is part of the classification of covering spaces (Theorem 9 of Roberts's notes in the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60)).

Every point of \(N\) has an evenly covered open neighbourhood; by compactness and the Lebesgue number lemma there is \(r>0\) such that every open ball of radius \(2r\) in \(N\) lies in an evenly covered set \(V\). If \(\gamma\in\Delta\setminus\{1\}\) and \(d(\tilde x,\gamma\tilde x)<2r\), a minimizing geodesic from \(\tilde x\) to \(\gamma\tilde x\) projects into such a \(V\), so it lies in one sheet over \(V\), on which the projection is injective; but its two end points have the same projection. Hence \(d(\tilde x,\gamma\tilde x)\ge2r\) for all \(\tilde x\) and \(\gamma\ne1\).

*Proper.* Suppose infinitely many distinct \(\gamma_n\) satisfy \(\gamma_nK\cap K\ne\varnothing\) for a compact \(K\). Choose \(k_n\in K\) with \(\gamma_nk_n\in K\); after passing to a subsequence, \(k_n\to k\) and \(\gamma_nk_n\) converges. Then
\[
\begin{aligned}
&d(\gamma_nk,\gamma_mk)\le d(k,k_n)\\
&\quad+d(\gamma_nk_n,\gamma_mk_m)+d(k_m,k)\to0,
\end{aligned}
\]
so \(d(\gamma_m^{-1}\gamma_nk,k)<2r\) and \(\gamma_n=\gamma_m\) for large \(n,m\), a contradiction.

*Cocompact.* Let \(R\) be the diameter of \(N\) and \(\tilde x_0\in\widetilde N\). For \(\tilde y\in\widetilde N\), a path of length at most \(R+1\) from the projection of \(\tilde y\) to that of \(\tilde x_0\) lifts to a path from \(\tilde y\) to some \(\gamma\tilde x_0\), so \(\tilde y\) lies in \(\gamma\bar B(\tilde x_0,R+1)\). \(\square\)

## 4. The obstruction

**Theorem 4.1** ([OpenAI-NC, Theorem 2.1]). The fundamental group \(\Gamma\) of the manifold \(M\) admits no proper cocompact isometric action on a nonempty proper CN space. In particular it admits none on a nonempty proper CAT(0) space.

*Proof.* Suppose \(\Gamma\) acts in this way on \(X\). By Proposition 4.1 of [The manifold and its fundamental group](the-manifold-and-its-fundamental-group.md), \(\Gamma\) contains commuting elements \(h_1,f_1\) generating a subgroup isomorphic to \(\mathbb Z^2\), and elements \(f_2=h_1\), \(h_2=h_1f_1\), such that \(h_i\in C_\Gamma(f_i)\) lies in the commutator subgroup of the centralizer \(C_\Gamma(f_i)\), \(i=1,2\). The elements \(f_1\), \(f_2=h_1\) and \(h_2\) have infinite order, so by Proposition 3.1 they are hyperbolic, and all elements of \(\Gamma\) are semisimple.

Each element of \(C_\Gamma(f_i)\) acts as an isometry commuting with \(f_i\), so Proposition 2.1 applies to the restriction of \(\tau_{f_i}\) to \(C_\Gamma(f_i)\), which is a homomorphism and therefore vanishes on its commutator subgroup: \(\tau_{f_i}(h_i)=0\). Proposition 2.4 for \((g,h)=(f_1,h_1)\) and for \((g,h)=(f_2,h_2)\) gives, for all integers \(m,n\),
\[
\begin{aligned}
\ell(f_1^mh_1^n)^2&=m^2\ell(f_1)^2\\
&\quad+n^2\ell(h_1)^2,\\
\ell(f_2^mh_2^n)^2&=m^2\ell(f_2)^2\\
&\quad+n^2\ell(h_2)^2 .
\end{aligned} \tag{4.1}
\]
Since \(h_1\) and \(f_1\) commute, \(f_2h_2=h_1\cdot h_1f_1=f_1h_1^2\). The first formula with \((m,n)=(1,2)\) and with \((m,n)=(1,1)\) gives
\[
\begin{aligned}
\ell(f_1h_1^2)^2&=\ell(f_1)^2+4\ell(h_1)^2,\\
\ell(h_2)^2=\ell(f_1h_1)^2&=\ell(f_1)^2+\ell(h_1)^2 .
\end{aligned}
\]
The second formula with \((m,n)=(1,1)\) gives
\[
\begin{aligned}
\ell(f_1h_1^2)^2=\ell(f_2h_2)^2&=\ell(h_1)^2+\ell(h_2)^2\\
&=\ell(f_1)^2+2\ell(h_1)^2 .
\end{aligned}
\]
Comparing, \(2\ell(h_1)^2=0\), contradicting \(\ell(h_1)>0\). The second assertion follows from CN Proposition 1.3. \(\square\)

In the flat language of [OpenAI-NC]: the squared translation length on \(\langle h_1,f_1\rangle\cong\mathbb Z^2\) is the restriction of a Euclidean norm, the first piece makes \(h_1\) orthogonal to \(f_1\), and the second makes \(h_2=h_1+f_1\) orthogonal to \(f_2=h_1\), which forces \(|h_1|^2=0\).

**Corollary 4.2** ([OpenAI-NC, Proposition 2.3]). The manifold \(M\) admits no smooth Riemannian metric of nonpositive sectional curvature.

*Proof.* Suppose \(g\) is such a metric. By Lemma 3.2, the universal covering \(\widetilde M\) with the lifted metric is complete, and the deck group, isomorphic to \(\Gamma\), acts by isometries properly and cocompactly. \(\widetilde M\) is connected, simply connected and has nonpositive sectional curvature, so it is a Hadamard manifold, which is a proper CN space by CN Proposition 1.4. This contradicts Theorem 4.1. \(\square\)

The same argument excludes metric spaces of nonpositive curvature in the sense of comparison triangles, given the metric form of the Cartan–Hadamard theorem.

**(MCH) The metric Cartan–Hadamard theorem.** If \((Y,d)\) is a compact connected length space that is locally CAT(0), then its universal covering, with the lifted length metric, is a proper CAT(0) space on which the deck group, isomorphic to \(\pi_1(Y)\), acts by isometries, properly and cocompactly. (The Cartan–Hadamard theorem for complete length spaces and the Hopf–Rinow theorem for length spaces, with proofs in [Poulsen, Theorems 3.5.1 and 1.3.5]; the deck group statements are proved as in Lemma 3.2.)

**Corollary 4.3** ([OpenAI-NC, Corollary 2.2]). Assume (MCH). Then \(M\) admits no locally CAT(0) length metric inducing its topology.

*Proof.* Such a metric makes \(M\) a compact connected locally CAT(0) length space, and (MCH) gives a proper cocompact action of \(\Gamma\) on a proper CAT(0) space, contrary to Theorem 4.1. \(\square\)

A metric *without focal points* is one in which every nonzero Jacobi field \(J\) along a unit-speed geodesic with \(J(0)=0\) and \(J\perp\dot\gamma\) has \(\frac{d}{ds}|J(s)|^2>0\) for \(s>0\). Ivanov and Kapovitch prove that a closed three-manifold carries a metric without focal points exactly when it carries one of nonpositive sectional curvature [IK, Theorem 7.1]. With Corollary 4.2, their theorem shows that \(M\) carries no metric without focal points, although it carries one without conjugate points (Theorem 3.1 of [Conjugate points and index forms](conjugate-points-and-index-forms.md)). Their theorem is not proved in this programme.

## 5. Exercises

**5.1.** Let \(X=\mathbb R^2\) and let \(g\), \(h\) be the translations by vectors \(u\), \(w\). Compute \(\operatorname{Min}(g)\), the axes of \(g\), and \(\tau_g(h)\), and check (2.2) when \(\langle u,w\rangle=0\).

**5.2.** Let \(X=\mathbb R^2\), \(g\) the translation by \(e_1\) and \(h\) the reflection in the \(x_1\)-axis composed with the translation by \(e_1\) (a glide reflection). Show that \(h\in C(g)\) and that \(h\) is semisimple, compute \(\tau_g(h)\) and \(\ell(h)\), and show that (2.2) fails for \((m,n)=(-1,1)\). Which hypothesis of Proposition 2.4 is violated?

**5.3.** Show that \(\ell(g^2)=2\ell(g)\) for every isometry \(g\) of a CN space, semisimple or not.

**5.4.** Show that in Theorem 4.1 the hypothesis that the action is proper cannot be dropped: \(\Gamma\) acts by isometries on a one-point space.

**5.5.** Let \(\Gamma=\mathbb Z^2\) act on \(\mathbb R^2\) by translations through a lattice. Show that the squared translation length is the restriction of a positive definite quadratic form and that it is invariant under the automorphisms of \(\mathbb Z^2\) induced by isometries normalizing the action.

## 6. Solutions

**5.1.** \(d_g\equiv|u|\), so \(\operatorname{Min}(g)=\mathbb R^2\) and the axes are the lines \(s\mapsto p+su/|u|\) for \(u\ne0\). The Busemann function of such a line is \(b(x)=-\langle x-p,u\rangle/|u|\), so \(\tau_g(h)=-\langle w,u\rangle/|u|\). If \(\langle u,w\rangle=0\), then \(\ell(g^mh^n)^2=|mu+nw|^2\), which is \(m^2|u|^2+n^2|w|^2\).

**5.2.** \(h(x_1,x_2)=(x_1+1,-x_2)\) commutes with the translation \(g\). Its displacement is \(\sqrt{1+4x_2^2}\), so \(\ell(h)=1\) and \(\operatorname{Min}(h)\) is the \(x_1\)-axis; \(h\) is semisimple. The axes of \(g\) are the horizontal lines and \(b(x)=-x_1+\text{const}\), so \(\tau_g(h)=-1\ne0\), and this is the violated hypothesis. Indeed \(g^{-1}h\) is the reflection in the \(x_1\)-axis, so \(\ell(g^{-1}h)=0\), while the right side of (2.2) for \((m,n)=(-1,1)\) is \(\ell(g)^2+\ell(h)^2=2\).

**5.3.** Section 1 shows \(\ell(g^2)\ge2\ell(g)\); for \(\varepsilon>0\) and \(y\) with \(d(y,gy)<\ell(g)+\varepsilon\), \(d(y,g^2y)<2\ell(g)+2\varepsilon\).

**5.4.** The one-point space is a proper CN space and every action on it is cocompact; the conclusion fails because the action is not proper (the infinite group fixes the point).

**5.5.** For \(v\) in the lattice, \(\ell(v)^2=|v|^2\), a positive definite form. An isometry \(k\) normalizing the action conjugates translations to translations by the image of the vector under the linear part of \(k\), which preserves \(|\cdot|^2\); Lemma 1.1(3) states the same invariance in general.

## References

- [OpenAI-NC] OpenAI, *A Three-Manifold Without Conjugate Points and Without a Nonpositively Curved Metric*, OpenAI Math Release preprint, 24 September 2026, Section 2 (Theorem 2.1, Corollary 2.2, Proposition 2.3). https://github.com/openai/math/tree/main/preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026
- [Poulsen] S. R. B. Poulsen, *A gentle introduction to CAT(0) spaces*, arXiv:2406.09883, Theorems 1.3.5 and 3.5.1. https://arxiv.org/abs/2406.09883
- [IK] S. Ivanov and V. Kapovitch, *Manifolds without conjugate points and their fundamental groups*, arXiv:1205.4455, Theorem 7.1. https://arxiv.org/abs/1205.4455
- D. M. Roberts, *Algebraic Topology*, lecture notes, 2019 (core course Algebraic Topology), Theorem 9. https://github.com/DavidMichaelRoberts/AlgebraicTopology2019
