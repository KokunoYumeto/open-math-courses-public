# Flow inverses and continuation on their actual domains

The following arguments are §§17.6–17.7 of the AN-03 programme reading *Geometric and microlocal calculus*. Its [local flow and every parameter derivative](smooth-parameter-flows-U072.md), NF1–NF15, are supplied separately. The [smooth inverse and implicit maps](implicit-maps-U070.md), §§16.4–16.5, supply the inverse construction used below. The [finite algebra](stable-prerequisite-bridges.md), §10, and [scalar calculus](metric-foundation-bridges.md), §§12–13, supply determinant differentiation, compactness, finite integration and the scalar exponential equation.

In the notation below \(E\) is the finite-dimensional state space, \(P\) the parameter space, and \(F(t,x,p)\) the smooth vector field on an actual open subset of \(\mathbb R\times E\times P\). The local solution satisfies \(\partial_tU=F(t,U,p)\) and its given initial value.

Programme proof: AN-03 course contributors, OpenAI Codex; CC0 1.0. [Programme credits](notices/TITLE_PAGE.md) and [rights notice](notices/RIGHTS.md) accompany the text.

### 17.6. Variable initial times without replacing the original time coordinate

Use the proved solution with the fixed original \(t_0\). Write \(U(t;t_0,y,p)\) for it. Near \((t_0,a,p_0)\), the actual finite map

\[
 \mathcal L(\tau,y,p)
   =(\tau,U(\tau;t_0,y,p),p)
 \tag{NF16}
\]

is \(C^r\). At \(\tau=t_0\) its state derivative is the original identity because \(U(t_0;t_0,y,p)=y\), its state derivative in \(p\) is zero, and its time derivative is \(F(t_0,y,p)\). Its full derivative is block triangular with diagonal identities; its inverse keeps the lower state/time block \(-F(t_0,y,p)\). The proved finite inverse/implicit theorem therefore constructs its actual local inverse, with second component \(Y(\tau,x,p)\). The unchanged original-time solution is

\[
 U(t;\tau,x,p)=U(t;t_0,Y(\tau,x,p),p),\qquad
 U(\tau;t_0,Y(\tau,x,p),p)=x .
 \tag{NF17}
\]

It is jointly \(C^r\), solves the original differential equation in the original \(t\), and has the original datum at the original time \(\tau\). Uniqueness was proved in Section17.1. Both maps in NF17 are explicit; no translated time equation or changed vector field is substituted for NF1.

Let \(M(t)=D_yU(t;t_0,y,p)\). Differentiating the already proved equation gives \(M'=D_xF(t,U,p)M\), \(M(t_0)=I_E\). NF8 proves that it is invertible with the constructed opposite-order inverse. Differentiate the second identity of NF17 and then its first identity to obtain the full initial-time derivative

\[
 \begin{aligned}
 D_\tau Y&=
  -D_yU(\tau;t_0,Y,p)^{-1}F(\tau,x,p),\\
 D_\tau U(t;\tau,x,p)&=
  -D_yU(t;t_0,Y,p)
   D_yU(\tau;t_0,Y,p)^{-1}F(\tau,x,p)\\
  &=-D_xU(t;\tau,x,p)F(\tau,x,p).
 \end{aligned}
 \tag{NF18}
\]

The last equality follows by differentiating NF17 in \(x\): \(D_xY=D_yU(\tau;t_0,Y,p)^{-1}\). All original inverse factors and endpoint evaluations appear before the comparison. Higher initial-time derivatives are the full finite composition and inverse partition formulas applied to NF16--NF17; they keep the entire time/state/parameter blocks.

### 17.7. Continuation, the exact composition law and coordinate transport

At every point of a solution, the local construction above applies with that original point and its original time as datum. Its local continuations agree by uniqueness. The union of all continuation intervals is an interval: each contains the original datum time, so two such intervals overlap; their agreeing solutions glue. This gives the unique maximal solution on that interval. If two overlapping continuations are first described through different chains of local rectangles, the same uniqueness argument on the connected time overlap makes them equal. No choice of a chart or of a time subdivision changes the solution.

The full admissible domain of \((t,\tau,x,p)\) is open and the solution is jointly \(C^r\) there. For an actual trajectory segment from \(\tau\) to \(t\), its compact graph is covered by finitely many construction rectangles with smaller time intervals. Subdivide that original time segment finely enough that each successive piece lies in one such rectangle: a Lebesgue number follows from compactness by taking finitely many smaller neighborhoods whose closures remain in the covering neighborhoods, or by the elementary compact interval subdivision argument. Each local solution map is defined on an open neighborhood of its intermediate datum. Continuity of the finite preceding composition lets one shrink the original data neighborhood so that all intermediate data stay in these open neighborhoods. The finite composition then exists near the given endpoint and is \(C^r\), and uniqueness identifies it with the maximal solution. Slightly moving both endpoint times uses the first and last rectangles. This proves openness and full local regularity throughout the actual domain.

Whenever all displayed solutions are defined along their connected common intervals,

\[
 U(t;s,U(s;\tau,x,p),p)=U(t;\tau,x,p),\qquad
 U(\tau;t,U(t;\tau,x,p),p)=x.
 \tag{NF19}
\]

Both sides of the first identity solve NF1 with the same datum at \(s\); uniqueness proves it, and the second is its endpoint case. For an autonomous field write \(\varphi_t(x,p)=U(t;0,x,p)\). NF19 gives the local flow law \(\varphi_t(\varphi_s(x,p),p)=\varphi_{t+s}(x,p)\), with their actual domains, and inverse \(\varphi_{-t}\). This is a local diffeomorphism, since both maps are the constructed smooth inverse maps on open sets. It is not an assertion that every field has a globally defined flow.

Under an original smooth coordinate diffeomorphism \(\kappa\), retain the transformed field
\(\widetilde F(t,\kappa(x),p)=D\kappa(x)F(t,x,p)\).
The chain rule proves that \(\kappa(U(t;\tau,x,p))\) solves its equation with datum \(\kappa(x)\). Applying uniqueness gives

\[
 \widetilde U(t;\tau,\kappa(x),p)
       =\kappa(U(t;\tau,x,p)).
 \tag{NF20}
\]

This is the exact map between coordinate presentations. For a smooth vector field on the given manifold, these transformations glue local chart solutions and all their parameter derivatives. Their domains are open by the finite-chain proof. For a manifold with boundary, the same assertion in boundary charts needs an actual smooth extension of the coefficients to an open coordinate neighborhood; no extension theorem is hidden in NF20. The collar lesson's stated coefficient extension or an explicitly given extension supplies that separate condition.

The determinant of the original state variation has all of its factors:

\[
 \det D_xU(t;\tau,x,p)
   =\exp\left(\int_\tau^t
             \operatorname{tr}D_xF(s,U(s;\tau,x,p),p)\,ds\right).
 \tag{NF21}
\]

Its derivative follows from the full cofactor determinant derivative and the two actual inverse products of NF8: for \(M'=AM\),
\((\det M)'=(\det M)\operatorname{tr}(M^{-1}AM)
=(\det M)\operatorname{tr}A\).
The trace equality is the finite sum
\(\sum_{i,j,k}(M^{-1})_{ij}A_{jk}M_{ki}
=\sum_{j,k}A_{jk}\sum_i M_{ki}(M^{-1})_{ij}
=\sum_jA_{jj}\).
The scalar integrating-factor proof and the initial determinant one give NF21. The original determinant, oriented time integral and original trace are all retained. Positivity of this determinant is the local orientation statement; no state norm or coordinate volume has been silently changed.

If the original state dimension is zero, the unique state is its zero vector, \(F\) is zero and the solution is constant. Every state inverse is the unique \(I_0\), every empty matrix determinant is one, and NF21 is \(1=\exp(0)\). No positive state comparison constant or division by a zero operator norm is needed. A zero-dimensional parameter space has no parameter directions; its derivative terms in the original formulas are zero. If \(W\) is empty there is no datum and no local assertion.
