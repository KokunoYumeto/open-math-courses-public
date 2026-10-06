# Geometry of singular supports

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The subspace invariant has two complementary uses. A zero value produces singular homogeneous solutions on an affine plane. A positive value allows smoothness to pass across a barrier whose normal lies in the measured subspace. We combine these facts to obtain geometric criteria for convex continuation, minimal linear carriers, and closed convex singular sets.

Read [Subspace detection and singularity carriers](subspace-detection-and-singularity-carriers.md) and [Logarithmic inverses and smooth barriers](logarithmic-inverses-and-smooth-barriers.md). We also use the singular-support boundary-distance criterion from [Singular supports and arbitrary distribution data](singular-supports-and-distribution-data.md) and [Boundary distance and propagation](boundary-distance-and-propagation.md). The convex arguments use nearest points and smooth approximation of convex bodies; the complete proofs are in [Smooth convex sweeps and first contact](smooth-convex-sweeps-and-first-contact.md). Kalmes [Kalmes] studies related geometric solvability conditions, while Hörmander [Hormander] develops the localization viewpoint.

Keep \(D=-i\partial\), and let \(P\ne0\) have arbitrary complex coefficients. The invariant \(\sigma_P(W)\) is defined using the real frequency subspace \(W\). Physical subspaces are denoted by \(V\); their perpendiculars are used as frequency subspaces.

[Smooth convex sweeps and first contact](smooth-convex-sweeps-and-first-contact.md) proves the nested smooth outer approximation, positive curvature, strict nesting, entry gradient and first contact used in the continuation argument.

## A necessary boundary-distance condition

For an open set \(X\) with nonempty complement, let
\[
d_X(x)=\operatorname{dist}(x,\mathbb R^n\setminus X).
\tag{1}
\]
A function satisfies the minimum principle in an affine plane \(F\) if every nonempty compact \(K\subset F\cap X\) obeys
\[
\min_Kd_X=\min_{\partial_FK}d_X.
\tag{2}
\]
Only sets with nonempty relative boundary need consideration; if the relative interior is empty, that boundary is all of \(K\). The cases \(X=\varnothing\) or \(X=\mathbb R^n\) have vacuous or infinite-distance formulations.

Recall that \(X\) is \(P\)-convex for singular supports precisely when every compactly supported distribution \(v\) in \(X\) satisfies
\[
\begin{gathered}
\operatorname{dist}(\operatorname{sing\,supp}v,X^c)\\
=\operatorname{dist}(\operatorname{sing\,supp}P(-D)v,X^c).
\end{gathered}
\tag{3}
\]
with empty-set distance interpreted as infinity. This is the boundary-distance criterion proved in the preceding lessons.

**Theorem 1.1.** If \(X\) is \(P\)-convex for singular supports and \(\sigma_P(V^\perp)=0\), then \(d_X\) satisfies the minimum principle in every affine plane parallel to \(V\).

**Proof.** Replacing \(P(\xi)\) by \(P(-\xi)\) preserves its invariant: change \(\xi,\theta\) to \(-\xi,-\theta\) in the defining ratios. The carrier theorem therefore gives a global solution \(P(-D)u=0\) with singular support exactly the chosen affine plane \(F\).

Suppose (2) fails. There are compact \(K\subset F\cap X\) and a number \(c\) with
\[
\min_Kd_X<c<\min_{\partial_FK}d_X.
\tag{4}
\]
Choose a smooth tangential cutoff equal to one near \(K\), supported in a small neighborhood of \(K\) in \(F\), whose derivatives occur only near \(\partial_FK\). Such a cutoff is obtained by smoothing the indicator of a small metric neighborhood of \(K\); it is constant on points a fixed distance inside or outside that neighborhood. Make its collar small enough that \(d_X>c\) on its derivative support in \(F\).

Multiply by a normal cutoff equal to one near \(F\), supported in a sufficiently thin tube that the product \(\chi\) has compact support in \(X\). The normal derivatives miss \(F\); the tangential derivatives meet it only in the high-distance collar. Hence
\[
\begin{gathered}
K\subset\operatorname{sing\,supp}(\chi u),\\
\operatorname{sing\,supp}P(-D)(\chi u)
\subset F\cap\operatorname{supp}d\chi,\\
d_X>c\quad\text{on this latter set}.
\end{gathered}
\tag{5}
\]
Here \(P(-D)(\chi u)=[P(-D),\chi]u\), and differential operators do not create singularities off the singular support of \(u\). All positive cutoff derivatives are supported in the support of its first derivative. The left side of (3) is at most \(\min_Kd_X<c\); the right side is greater than \(c\), or infinite. This contradicts (3). \(\square\)

**Corollary 1.2.** Every open set is \(P\)-convex for singular supports if and only if \(P\) is hypoelliptic.

**Proof.** For a hypoelliptic polynomial, \(P(-D)\) is also hypoelliptic and
\(\operatorname{sing\,supp}P(-D)v=\operatorname{sing\,supp}v\).
Thus (3) holds on every open set.

If \(P\) is not hypoelliptic, [Hypoellipticity and complex zeros](hypoellipticity-and-complex-zeros.md) gives a nonconstant polynomial localization \(Q\) at infinity. The localization geometry in [Symbols at infinity](symbols-at-infinity.md) gives a nonzero inactive direction of \(Q\). Its full inactive subspace \(\Lambda(Q)\) is therefore nonzero and proper.

For each fixed \(t\), coefficient convergence of the normalized translates gives
\[
\begin{gathered}
\sigma_P(\Lambda(Q))\\
\leq\frac{A_{Q,\Lambda(Q)}(0,t)}{A_Q(0,t)}
=\frac{|Q(0)|}{A_Q(0,t)}.
\end{gathered}
\tag{6}
\]
Since \(Q\) is nonconstant, the denominator tends to infinity as \(t\to\infty\); hence this invariant is zero. Set \(V=\Lambda(Q)^\perp\), which also has positive dimension and is proper.

Choose nonzero \(q\in V^\perp\). In \(X=\mathbb R^n\setminus\{0\}\), take the compact disk
\[
K=\{q+v:v\in V,\ |v|\leq1\}.
\]
On it, \(d_X(q+v)=\sqrt{|q|^2+|v|^2}\). The minimum is \(|q|\) in its relative interior, while its relative boundary has value \(\sqrt{|q|^2+1}\). Theorem 1.1 therefore rules out \(P\)-convexity for singular supports on this explicit domain. \(\square\)

This characterization concerns singular supports. It does not identify them with supports.

## Convex continuation through hyperplanes

Call a real hyperplane with normal \(\nu\ne0\) bad when \(\sigma_P(\mathbb R\nu)=0\).

**Theorem 2.1.** Let \(X_1\subset X_2\) be nonempty convex open sets. The following are equivalent:

1. Every homogeneous distributional solution on \(X_2\) which is smooth on \(X_1\) is smooth on \(X_2\).
2. Every bad hyperplane meeting \(X_2\) also meets \(X_1\).

Under condition 2, the same continuation holds for a distribution \(u\) with smooth \(P(D)u\) on \(X_2\).

**Proof.** If a bad hyperplane \(H\) meets \(X_2\) but misses \(X_1\), the carrier theorem supplies a global homogeneous solution with singular support exactly \(H\). Its restriction disproves condition 1.

Conversely assume condition 2 and let \(P(D)u\) be smooth on \(X_2\), with \(u\) smooth on \(X_1\). Suppose \(x_*\in X_2\) is singular. Choose a compact target ball \(T\) containing \(x_*\) in its interior and lying inside \(X_2\). Let \(B\) be the set of bad unit normals. It is compact by continuity of the invariant.

For a fixed \(\nu\in B\), projections of \(X_1,X_2\) onto its normal line are equal. They are open intervals, and a value lies in such an interval precisely when the corresponding hyperplane meets that open set. The compact target's projection therefore lies strictly inside the projection of \(X_1\).

Write \(h_C(\nu)=\max_{x\in C}\nu\cdot x\) for a compact set's support function. For each \(\nu\in B\), choose a point of \(X_1\) beyond \(h_T(\nu)\). Continuity preserves a positive margin on a neighborhood of that normal. A finite cover of \(B\), together with a small ball in \(X_1\), gives a compact full-dimensional convex \(K_1\subset X_1\) and \(q_0>0\) such that
\[
h_T(\nu)\leq h_{K_1}(\nu)-q_0,\qquad \nu\in B.
\tag{7}
\]
Both signs of each bad normal belong to \(B\), so both projection endpoints are controlled. If \(B\) is empty, choose any such \(K_1\); all inequalities involving \(B\) are vacuous.

Take \(d>0\) with \(K_1+B(0,d)\subset X_1\), and let \(D_0\) bound distances between \(K_1\) and \(T\). For \(K=\operatorname{conv}(K_1\cup T)\), write \(z=(1-s)y+sw\), with \(y\in K_1,w\in T\). If \(\operatorname{dist}(z,K_1)\geq d/2\), then \(s\geq d/(2D_0)\), and (7) yields
\[
\begin{gathered}
\nu\cdot z\leq h_{K_1}(\nu)-q_0d/(2D_0),\\
\nu\in B.
\end{gathered}
\tag{8}
\]
Choose a sufficiently small \(\eta>0\). Every point of \(K+B(0,\eta)\) outside \(X_1\) then has
\[
\nu\cdot x<h_{K_1}(\nu),\qquad \nu\in B.
\tag{9}
\]
To see this, its nearby point in \(K\) has distance at least \(d/2\) from \(K_1\) if \(\eta<d/2\); choose \(\eta\) smaller also than half the margin in (8). Take the compact enlargement inside \(X_2\).

Choose nested smooth strongly convex bodies \(L_0,L_1\) such that \(K_1\subset\operatorname{int}L_0\), \(L_0\subset X_1\), \(K\subset\operatorname{int}L_1\), and \(L_1\subset K+B(0,\eta)\). The nested approximation lemmas in [Smooth convex sweeps and first contact](smooth-convex-sweeps-and-first-contact.md), Section 1, give these bodies, including lower-dimensional compact sets. One construction mollifies their squared distance functions and adds a small positive quadratic term. The resulting function has positive Hessian; a regular sublevel above its minimum contains the original compact set and remains in any prescribed neighborhood. Choose the approximations so that \(L_0\subset\operatorname{int}L_1\).

The Minkowski interpolation
\[
\begin{gathered}
L_s=(1-s)L_0+sL_1,\\
0\leq s\leq1.
\end{gathered}
\tag{10}
\]
is strictly nested with smooth positively curved boundary. Its support function is \((1-s)h_{L_0}+sh_{L_1}\). The spherical support-curvature matrices are positive convex combinations of the endpoint matrices, so they stay positive. Also \(h_{L_1}-h_{L_0}\) has a positive minimum on the unit sphere, which gives strict nesting and continuous entry times.

The singular set inside \(L_1\) is compact. It misses \(L_0\) and contains \(x_*\) in the interior of \(L_1\). There is a first \(s_0\in(0,1)\) for which \(L_{s_0}\) meets it. A first contact point \(y\) lies on the boundary, and \(u\) is smooth in the interior. Its outward normal cannot be bad. Indeed the tangent plane has offset \(h_{L_{s_0}}(\nu)\geq h_{K_1}(\nu)\), whereas \(y\), being singular and thus outside \(X_1\), obeys (9) for every bad normal.

The one-barrier case of [Logarithmic inverses and smooth barriers](logarithmic-inverses-and-smooth-barriers.md) applies to a local defining function of this boundary, since its normal has positive invariant. It makes \(u\) smooth near \(y\), contradicting its selection as a singular point. This proves the continuation and its smooth-data extension. \(\square\)

## A minimal linear carrier

**Theorem 3.1.** Suppose
\[
\begin{gathered}
\sigma_P(V^\perp)=0,\\
\sigma_P(U^\perp)>0,\\
\text{for every proper subspace }U\subset V.
\end{gathered}
\tag{11}
\]
If \(P(D)u\) is smooth on all space and \(\operatorname{sing\,supp}u\subset V\), then the singular support is either \(V\) or empty.

**Proof.** If \(u\) is regular at one point of \(V\), translate it to zero. Choose \(r>0\) so that \(u\) is smooth on \(B(0,r)\). In coordinates \(V=\{x'=0\}\), it is smooth wherever \(x'\ne0\) or \(|x''|<r\).

At \(x_0=(0,x_0'')\), \(|x_0''|=r\), use the \(k+1\) barriers
\[
\begin{gathered}
\phi_0(x)=|x''|^2-r^2,\\
\phi_j(x)=|x''|^2-r^2-x_j',\\
1\leq j\leq k.
\end{gathered}
\tag{12}
\]
Their gradients are independent and span
\[
W=V^\perp+\mathbb R x_0''.
\]
This equals \(U^\perp\) for the proper subspace \(U=V\cap(x_0'')^\perp\); hence \(\sigma_P(W)>0\). The union of the negative barrier sides lies in the known smooth region: off \(V\) everything is smooth, and on \(V\) negativity means \(|x''|<r\).

The barrier theorem makes \(u\) smooth near every point of the radius-\(r\) sphere in \(V\). If the supremum of its smooth-ball radii were finite, their union would give smoothness on the corresponding open ball. Apply the same argument on its boundary sphere and use compactness to extend the radius, a contradiction. The supremum is infinite, so \(u\) is smooth everywhere. Thus any regular point of \(V\) forces an empty singular support; otherwise every point of \(V\) is singular. \(\square\)

The hypothesis cannot hold for \(V=\{0\}\), since \(\sigma_P(\mathbb R^n)=1\).

## Why complete straight lines need not propagate

The preceding theorem has a minimality hypothesis. Arbitrary singular supports of homogeneous solutions can behave differently.

In \(\mathbb R^3\), let
\[
\begin{gathered}
P(D)=D_2D_3,\\
u=\delta_0(x_1)b(x_2,x_3),\\
b(x_2,x_3)=\mathbf1_{(-1,1)}(x_2)-\mathbf1_{(2,3)}(x_3).
\end{gathered}
\tag{13}
\]
The mixed derivative vanishes: each summand in \(b\) is independent of one differentiated coordinate. The origin is singular, since \(b\) equals one near it.

No complete straight line through zero is contained in the singular support. A line leaving \(x_1=0\) immediately leaves the support. In that plane write it as \((x_2,x_3)=(at,bt)\). If \(a\ne0\), for large enough \(|t|\) both indicators vanish, including when \(b=0\). If \(a=0,b\ne0\), choose \(bt\in(2,3)\); both indicators equal one near that point and cancel. In either case an open part of the line is regular.

## Convex carriers and lineality

For a nonempty closed convex set \(I\), its lineality is the largest vector space \(V\) satisfying \(I+V=I\). Equivalently it consists of the directions whose full lines through points of \(I\) stay in \(I\).

**Lemma 5.1.** A nonempty closed convex set \(C\) which contains no lines and does not contain zero is contained in a closed pointed cone. That cone admits a unit vector \(\nu\) and \(c>0\) such that
\[
\begin{gathered}
\nu\cdot w\leq-c|w|,\\
\text{for every }w\text{ in the cone}.
\end{gathered}
\tag{14}
\]

**Proof.** Take the closure \(K\) of the conic hull \(\{\lambda y\colon\lambda\geq0,\ y\in C\}\). It is convex because \(C\) is convex. To prove it is pointed, suppose a nonzero \(w\) and its negative belong to \(K\). Approximate each by \(\lambda_jy_j\). Since \(\operatorname{dist}(0,C)>0\), the factors \(\lambda_j\) are bounded above. Pass to limits.

If their limit is positive, the corresponding ray contains a point of \(C\). If their limit is zero, the direction is a recession direction: for any \(y\in C\) and \(s\geq0\), convexity puts
\((1-s\lambda_j)y+s\lambda_jy_j\) in \(C\) for large \(j\), and its limit is \(y+sw\). Closedness retains that point.

Two opposite point rays put zero in \(C\) by convexity. A point ray and its opposite recession direction do the same by moving along that recession direction. Two opposite recession directions give a line in \(C\). All alternatives contradict the hypotheses. Hence \(K\) is pointed.

Its unit section \(S=K\cap\{|w|=1\}\) is nonempty compact. Zero does not belong to \(\operatorname{conv}S\): a convex combination equal to zero expresses the negative of one participating unit vector as a positive combination of the others, producing a line in \(K\).

The convex hull is compact in finite dimension. Indeed affine dependence lets one eliminate positive coefficients until at most \(d+1\) points remain in dimension \(d\); it is then the image of a compact simplex times \(S^{d+1}\).

Let \(q\ne0\) be its nearest point to zero. For \(z\in\operatorname{conv}S\), differentiating \(|q+s(z-q)|^2\) at \(s=0\) gives \(q\cdot z\geq|q|^2\). This is the nearest-point step in the AN-03 lesson *Prerequisite bridges*, convex separation bridge. Set \(\nu=-q/|q|\) and \(c=|q|\); homogeneity gives (14). The uniform cone estimate follows from this compact-section argument, beyond the bridge's open-convex-separation statement. \(\square\)

**Theorem 5.2.** Let \(I\ne\varnothing\) be closed and convex, with lineality \(V\). Every global homogeneous distributional solution with singular support contained in \(I\) is smooth if and only if
\[
\sigma_P(V^\perp)>0.
\tag{15}
\]

**Proof.** If the invariant is zero, choose \(y\in I\). The carrier theorem gives a nonsmooth homogeneous solution with singular support exactly \(y+V\subset I\). This disproves universal smoothness.

Suppose the invariant is positive, and write \(W=V^\perp\). First consider \(I=\mathbb R^n\). Then \(W=\{0\}\). Positive \(\sigma_P(\{0\})\) is equivalent to hypoellipticity. For a hypoelliptic polynomial, the derivative quotients tend to zero, so at each fixed radius \(A_P(\xi,t)/|P(\xi)|\to1\), giving invariant one. Conversely a nonconstant localization \(Q\) at infinity gives
\[
\sigma_P(\{0\})\leq
\inf_{t\geq1}\frac{|Q(0)|}{A_Q(0,t)}=0.
\]
Thus the global homogeneous solutions are smooth by hypoellipticity.

For proper \(I\), translate an exterior point to zero. The orthogonal projection \(C=\pi_WI\) equals \(I\cap W\), because \(I+V=I\). It is therefore closed and convex, misses zero, and has no lines. Indeed, if \(z+\mathbb Rw\subset C\), convexity gives \((1-s/t)y+(s/t)(z+tw)\in C\) for every \(y\in C\), fixed \(s\geq0\), and large \(t\). Closedness gives \(y+sw\in C\); the negative direction follows as well. Thus \(w\) would be a lineality direction, contradicting the removal of \(V\). Lemma 5.1 places \(C\) in a pointed cone with estimate (14).

Choose \(0<\kappa<\min(c,1)\), and use the annulus smoothing lemma from [Logarithmic inverses and smooth barriers](logarithmic-inverses-and-smooth-barriers.md). For every nonzero \(x\) in the inverse image of that cone,
\[
\begin{gathered}
\kappa|x_W|+x\cdot\nu-\tfrac{p_0}2|x|\\
\leq-(c-\kappa)|x_W|-\tfrac{p_0}2|x|<0.
\end{gathered}
\tag{16}
\]
Hence its bad source annulus lies outside this cone, where \(u\) is smooth because its singular support is contained in \(I\).

The smoothing lemma applies for every \(\varepsilon>0\). Its output contains a ball of radius \(c_0\varepsilon\), where \(c_0>0\) is independent of \(\varepsilon\). To check this scale uniformity, the annulus geometry in (16) has a fixed angular margin. Choose the source cutoffs once on the unit annulus and rescale them by \(\varepsilon\); the inner ball, cone and outer support alternatives in the convolution argument retain the same margin. The distributional order changes only the required kernel differentiability, not this geometric radius. Letting \(\varepsilon\to\infty\) proves smoothness on all space. \(\square\)

If \(I=\varnothing\), the premise already says that the singular support is empty. Universal smoothness then holds for every \(P\), without a condition on a subspace invariant.

The carrier construction also gives the stronger converse example: whenever \(\sigma_P(V^\perp)=0\), any closed \(F\) with \(F+V=F\) can be the exact singular support, with any prescribed finite global differentiability order.

## Exercises and full solutions

**Exercise 1. The punctured domain (basic).** For \(P(\xi)=\xi_1\) in \(\mathbb R^2\), show explicitly that \(\mathbb R^2\setminus\{0\}\) fails \(P\)-convexity for singular supports.

**Solution.** Take \(V=\mathbb Re_1\), so \(V^\perp=\mathbb Re_2\) and the transport computation gives \(\sigma_P(V^\perp)=0\). For \(q=e_2\), the compact interval \(K=\{(s,1):|s|\leq1\}\) has distance \(\sqrt{s^2+1}\) to the missing point. Its minimum is one at \((0,1)\), while both relative boundary points have distance \(\sqrt2\). This violates the necessary minimum principle in Theorem 1.1.

**Exercise 2. Transport continuation (basic).** In \(\mathbb R^2\), take \(P(\xi)=\xi_1\). Identify the bad hyperplanes and state the convex continuation criterion in coordinate terms.

**Solution.** For a unit normal \(\nu\), the transport invariant is \(|\nu\cdot e_1|\). The bad normals are multiples of \(e_2\); the bad hyperplanes are horizontal lines \(x_2=c\). Theorem 2.1 says that every horizontal line meeting \(X_2\) must also meet \(X_1\), equivalently the two open convex sets have the same projection onto the \(x_2\) axis. A solution of \(D_1u=0\) is independent of \(x_1\), so this projection criterion also follows directly from its distributional form.

**Exercise 3. A minimal carrier (intermediate).** For transport in \(\mathbb R^n\), \(n\geq2\), show that \(V=\mathbb Re_1\) meets (11). Explain why a homogeneous solution whose singular support is contained in that one line is either regular everywhere or singular on the whole line.

**Solution.** The perpendicular \(V^\perp\) has zero invariant. The only proper subspace of the one-dimensional \(V\) is \(\{0\}\); its perpendicular is the full frequency space and has invariant one. Thus (11) holds, and Theorem 3.1 applies. Directly, independence of the transport coordinate makes the singular set invariant under all translations along the line. A nonempty singular set contained in that line must therefore be the whole line.

**Exercise 4. Checking the line counterexample (intermediate).** Verify the homogeneous equation and the two in-plane line cases in (13). Why does this example leave Theorem 3.1 intact?

**Solution.** The first summand depends on \(x_2\) but not \(x_3\), and the second on \(x_3\) but not \(x_2\), so applying both derivatives gives zero. Near the origin the bracket is one, making its delta factor singular. For an in-plane line with \(a\ne0\), take \(|t|\) large enough that \(at\notin[-1,1]\) and, when \(b\ne0\), \(bt\notin[2,3]\); when \(b=0\), the second indicator is already zero. Both terms vanish in a neighborhood. For \(a=0,b\ne0\), choose \(bt\) strictly inside \((2,3)\); then both terms are one in a neighborhood and cancel. The theorem assumes a minimal linear carrier and singular support contained in that carrier. It does not assert that every singular point of every homogeneous solution belongs to a complete singular line. The example addresses that stronger assertion.

**Exercise 5. Strict cone separation (advanced).** Let \(K\ne\{0\}\) be a closed convex pointed cone in a finite-dimensional Euclidean space. Prove (14) using its unit section, and identify where pointedness and compactness enter.

**Solution.** The unit section \(S\) is compact by closedness and boundedness. If \(0=\sum\lambda_ju_j\) with \(\lambda_j\geq0\), sum one, choose an index with \(\lambda_j>0\). Then \(-u_j\) is a nonnegative combination of the others, so both \(u_j\) and \(-u_j\) lie in \(K\), contradicting pointedness. Thus \(0\notin\operatorname{conv}S\). Finite-dimensional coefficient elimination makes that convex hull compact, so its nearest point \(q\) to zero exists and is nonzero. The projection inequality gives \(q\cdot u\geq|q|^2\) for all unit \(u\in K\). Taking \(\nu=-q/|q|\) and rescaling a general cone point proves (14) with \(c=|q|>0\). Pointedness excludes zero from the convex hull; compactness makes the resulting gap uniform.

**Exercise 6. Lineality and an empty set (advanced).** For \(P(\xi)=\xi_1\) on \(\mathbb R^2\), compare the closed disk, the strip \(\{|x_2|\leq1\}\), the strip \(\{|x_1|\leq1\}\), and the empty set as possible containers of singular support of global homogeneous solutions.

**Solution.** The disk has zero lineality, so its perpendicular is all frequency space and has invariant one. Theorem 5.2 forces every homogeneous solution with singular support there to be smooth. The horizontal strip has lineality \(\mathbb Re_1\); its perpendicular has zero transport invariant. It can contain a nonsmooth solution with singular support any horizontal line in the strip, for example \(u=1(x_1)\otimes\delta_0(x_2)\). The vertical strip has lineality \(\mathbb Re_2\); its perpendicular \(\mathbb Re_1\) has invariant one, so it forces smoothness. This also follows because a nonempty transport-invariant singular set would have to contain a complete horizontal line, which cannot fit in that strip. For the empty set, containment means empty singular support directly, so the solution is smooth without invoking any invariant criterion.

## References

- **[Hormander]** Lars Hörmander, “On the singularities of solutions of partial differential equations with constant coefficients,” *Séminaire Goulaouic–Schwartz*, 1971–1972, exposé 25, 1–6. [Original article](https://www.numdam.org/item/SEDP_1971-1972____A25_0/).
- **[Kalmes]** Thomas Kalmes, “Surjectivity of differential operators and linear topological invariants for spaces of zero solutions,” *Revista Matemática Complutense* 32 (2019), 37–55, sections on boundary distance and \(P\)-convexity. [Author's preprint](https://arxiv.org/abs/1408.4356).
