# Connections and parallel transport

*Original programme exposition is dedicated under CC0 1.0.*

A bundle supplies a fibre at each point. A connection specifies how to compare nearby fibres along a chosen direction. We first express that choice as a splitting of tangent spaces, then as local one-forms. The same formulas will construct connections, extend prescribed ones, and transport a point or vector along an entire path.

Manifolds and Lie groups are finite dimensional, Hausdorff, second countable, smooth and without boundary. Bundles have finite dimensional fibres. Paths are continuous and have finitely many smooth pieces, each smooth up to its endpoints; smooth dependence on parameters always uses a fixed finite division into such pieces. A right principal action is written \(p\mapsto pa\). All group and associated-bundle conventions are those of the earlier [Principal bundles and associated bundles](https://kokunoyumeto.github.io/open-math-courses-public/courses/DG-FND/principal-bundles-and-associated-bundles.html), abbreviated **PB**.

We use complete earlier programme proofs in Local tools for bundles and transport: finite linear algebra 0.2, calculus 0.3, smooth inversion 0.4, scalar exponential and flat functions 0.5, inverse functions 1.2, local differential equations with parameters 2.1, the global invariant group equation 2.2, the group exponential 2.3, and partitions and cutoffs 3.1. PB A.2 proves smooth division and principal trivializations; PB B.1–B.2 prove associated bundles and their sections; PB C.2–C.3 construct tangent and tensor bundles and the adjoint representation. The one circular normalization used in E.1 has its integral proof in [DG-CHAR-17, Lemma A.5](https://kokunoyumeto.github.io/open-math-courses-public/courses/DG-CHAR/DG-CHAR-17.html).

## A. Splittings and one-forms describe the same choice

A vector-bundle-valued one-form on a manifold assigns a linear map on each tangent space with smooth matrix entries in local charts and local frames. For an ordinary vector space \(W\), write \(\Omega^1(N,W)\) for these \(W\)-valued one-forms. A smooth **distribution** means a vector subbundle of the tangent bundle, so it has local smooth frames of its specified rank.

**Lemma A.1 (three descriptions of a bundle connection).** For a smooth fibre bundle \(\pi:E\to M\), put \(VE=\ker d\pi\). The following data are equivalent:

1. A smooth subbundle \(HE\) with \(TE=HE\oplus VE\).
2. A smooth fibrewise linear map \(\Phi:TE\to VE\) whose restriction to \(VE\) is the identity.
3. A smooth family of linear maps \(L_p:T_{\pi(p)}M\to T_pE\), with \(d\pi_p L_p=\mathrm{id}\).

The correspondence is
\[
HE=\ker\Phi,\qquad
\Phi(w)=w-L_p(d\pi_p w),\qquad
L_p=(d\pi_p|_{H_pE})^{-1}.
\tag{A.1}
\]
In particular \(\Phi^2=\Phi\), its image is \(VE\), and \(\mathrm{id}-\Phi\) is the horizontal projection.

**Proof.** In a fibre-bundle chart and then an ordinary chart of its model fibre, write tangent coordinates as \((v,w)\), with \(d\pi(v,w)=v\). Thus \(VE\) has local form \(\{0\}\times\mathbb R^k\), proving it is a smooth vector subbundle.

Suppose \(\Phi\) is given. In these coordinates its condition on vertical vectors forces the form
\[
\Phi(v,w)=(0,B(p)v+w)
\]
for a smooth matrix \(B(p)\). Its kernel is the graph \(\{(v,-B(p)v)\}\), with smooth frame obtained by taking \(v\) to be each coordinate basis vector. This proves smoothness and the complement property without assuming a constant-rank theorem for bundle maps. The formula \(L_p(v)=(v,-B(p)v)\) is its smooth lift, and direct substitution gives (A.1).

Conversely, for a given smooth complement \(HE\), \(d\pi_p|_{H_pE}\) is injective because its kernel is \(H_pE\cap V_pE=0\); it is onto because every tangent vector decomposes into its horizontal and vertical parts. In local frames of \(HE\) and \(TM\), it is therefore an invertible matrix. Local tools 0.4 makes its inverse smooth. This gives \(L_p\) and the smooth \(\Phi\) in (A.1).

Finally if \(L_p\) is given, it is injective since \(d\pi_p L_p=\mathrm{id}\). In the same product coordinates it has form \(L_p(v)=(v,C(p)v)\); hence its image is a smooth complement and \(w-L_p(d\pi_p w)\) is its vertical projection. All three constructions are inverse in these coordinates. The claimed projection identities follow either from them or from \(\Phi|_{VE}=\mathrm{id}\). □

For a principal \(G\)-bundle \(P\to M\), let \(\mathfrak g=T_eG\), with the Lie algebra and adjoint action proved in PB C.3. For \(X\in\mathfrak g\), its fundamental vector at \(p\) is
\[
\zeta_X(p)=d(a\mapsto pa)_e X
=\left.\frac{d}{dt}\right|_{0}p\exp(tX).
\tag{A.2}
\]
The second equality is Local tools 2.3. A principal connection is a complement \(HP\) as in A.1 that satisfies \(dR_a(H_pP)=H_{pa}P\).

**Theorem A.2 (principal connection forms).** The map \(X\mapsto\zeta_X(p)\) is a smoothly varying linear isomorphism \(\mathfrak g\to V_pP\), and
\[
dR_a\,\zeta_X(p)=\zeta_{\operatorname{Ad}(a^{-1})X}(pa).
\tag{A.3}
\]
Principal connections correspond bijectively to \(\omega\in\Omega^1(P,\mathfrak g)\) satisfying
\[
\omega_p(\zeta_X(p))=X,\qquad
\omega_{pa}(dR_a w)=\operatorname{Ad}(a^{-1})\omega_p(w).
\tag{A.4}
\]
Their horizontal distribution, vertical projection and lift are given by
\[
H_pP=\ker\omega_p,\qquad
\Phi_p(w)=\zeta_{\omega_p(w)}(p),\qquad
d\pi_p L_p(v)=v,\quad \omega_p(L_p(v))=0.
\tag{A.5}
\]

**Proof.** PB A.2 shows that \(a\mapsto pa\) is a diffeomorphism from \(G\) onto \(P_{\pi(p)}\), so its derivative is the asserted linear isomorphism. In a local product chart it is \((p,X)\mapsto(0,dL_g X)\) when \(p=s(x)g\). Multiplication is smooth, and its inverse trivialization uses \(dL_{g^{-1}}\), also smooth. Thus the isomorphisms and their inverses vary smoothly. Differentiating
\[
(p\exp(tX))a=pa\exp(t\operatorname{Ad}(a^{-1})X),
\]
which is the conjugation identity in Local tools 2.3, proves (A.3).

For a principal complement, its vertical projection \(\Phi\) commutes with \(dR_a\): right translation preserves both the vertical subbundle, since \(\pi R_a=\pi\), and the given horizontal subbundle, so it carries each of the two components of a vector to the corresponding components of its image. Define \(\omega_p=\zeta_p^{-1}\Phi_p\). Smoothness follows from A.1 and the smooth inverse just proved. Vertical reproduction gives the first equation of (A.4); commutation and (A.3) give the second.

Conversely (A.4) makes the map \(\Phi\) in (A.5) a smooth vertical projection equal to the identity on vertical vectors. By A.1 its kernel is a smooth complement, and \(\ker\Phi=\ker\omega\) because \(\zeta_p\) is injective. The second equation in (A.4) preserves this kernel under \(dR_a\), in both directions by replacing \(a\) by \(a^{-1}\). Thus it is principal. The lift in (A.5) exists, is unique and is smooth by A.1. Reproduction of vertical vectors also shows that constructing \(\omega\) back from \(\Phi\) recovers it exactly. □

**Theorem A.3 (local potentials and their change of section).** Define the left Maurer–Cartan one-form on \(G\) by
\[
\theta_g(\eta)=dL_{g^{-1}}\eta.
\]
For a local section \(s:U\to P\) set \(A=s^*\omega\in\Omega^1(U,\mathfrak g)\). In the chart \(\Psi(x,g)=s(x)g\), the full connection form is
\[
(\Psi^*\omega)_{(x,g)}(v,\eta)
=\operatorname{Ad}(g^{-1})A_x(v)+\theta_g(\eta).
\tag{A.6}
\]
For \(s'=sh\), with smooth \(h:U\to G\), the potentials satisfy
\[
A'=\operatorname{Ad}(h^{-1})A+h^*\theta.
\tag{A.7}
\]
Every smooth \(A\) defines a connection on the product chart by (A.6). Potentials on a principal atlas give a global connection exactly when they obey (A.7) on overlaps.

**Proof.** Differentiating \(\Psi\) in its two variables gives
\[
d\Psi(v,\eta)=dR_g(ds(v))+d(a\mapsto s(x)a)_g\eta.
\]
Write \(\eta=dL_g X\), where \(X=\theta_g\eta\). The second term is \(\zeta_X(s(x)g)\), since \(a=g\exp(tX)\) has initial velocity \(\eta\). Applying (A.4) proves (A.6). Evaluating it along \(x\mapsto(x,h(x))\) proves (A.7).

We check the converse and the overlap assertion. Under right multiplication by a constant \(a\), the left form satisfies
\[
\theta_{ga}(dR_a\eta)=\operatorname{Ad}(a^{-1})\theta_g(\eta).
\tag{A.8}
\]
Indeed for \(\eta=dL_g X\), the curve \(g\exp(tX)a=ga\exp(t\operatorname{Ad}(a^{-1})X)\) verifies this identity, and all \(\eta\) have that form. Formula (A.6) therefore satisfies equivariance because
\(\operatorname{Ad}((ga)^{-1})=\operatorname{Ad}(a^{-1})\operatorname{Ad}(g^{-1})\).
A fundamental vector in this chart is \((0,dL_g X)\), on which (A.6) is \(X\). A.2 now proves that it is a connection.

For variable \(g,h\), the product rule for multiplication gives
\[
\theta_{gh}\bigl(d\mu_{(g,h)}(\eta,\nu)\bigr)
=\operatorname{Ad}(h^{-1})\theta_g(\eta)+\theta_h(\nu).
\tag{A.9}
\]
To verify this, split the differential into \(dR_h\eta+dL_g\nu\). Its first term is handled by (A.8), and applying \(dL_{(gh)^{-1}}dL_g=dL_{h^{-1}}\) to the second gives the other term.

If \(s_j=s_i h\), the coordinate identification is \((x,g)\) in the \(j\)-chart with \((x,h(x)g)\) in the \(i\)-chart. Applying (A.9) to this product turns the \(i\)-formula into
\[
\operatorname{Ad}(g^{-1})
\bigl(\operatorname{Ad}(h^{-1})A_i+h^*\theta\bigr)+\theta_g.
\]
This equals the \(j\)-formula exactly when (A.7) holds. Equality follows for every tangent vector, so the local one-forms glue smoothly; conversely a global form has (A.7) by the first part. □

**Theorem A.4 (differences and adjoint-valued one-forms).** The difference of two principal connection forms is a horizontal, adjoint-equivariant \(\mathfrak g\)-valued one-form. Here horizontal means that it vanishes on every vertical vector. Such forms correspond bijectively to \(\Omega^1(M,\operatorname{ad}(P))\). Adding any one of them to a connection again gives a connection, so the set of connections, when nonempty, is an affine space over \(\Omega^1(M,\operatorname{ad}(P))\).

**Proof.** Subtraction in (A.4) cancels the reproduced \(X\) and preserves equivariance; this proves the first assertion. Conversely addition of a horizontal equivariant form preserves both conditions of (A.4), proving the last assertion once the correspondence is established.

For such an \(\alpha\), define
\[
\beta_x(v)=[p,\alpha_p(w)],
\qquad p\in P_x,\quad d\pi_p w=v.
\tag{A.10}
\]
There is a lift \(w\), for example in any local product chart. Changing \(w\) at fixed \(p\) changes it by a vertical vector and hence leaves the value unchanged. Replacing \(p\) by \(pa\), we may use \(dR_a w\); equivariance gives
\([pa,\alpha_{pa}(dR_a w)]=[pa,\operatorname{Ad}(a^{-1})\alpha_p(w)]=[p,\alpha_p(w)]\).
PB B.1 supplies the last associated-bundle identity. Thus (A.10) is a well-defined fibrewise linear map \(TM\to\operatorname{ad}(P)\). A local section \(s\) gives its coordinates \(s^*\alpha\), proving smoothness.

Conversely, for each \(p\) over \(x\) and \(w\in T_pP\), there is a unique \(X\in\mathfrak g\) with \(\beta_x(d\pi_p w)=[p,X]\), since \(X\mapsto[p,X]\) is an isomorphism by PB B.1. Define \(\alpha_p(w)=X\). This is linear in \(w\); in a local section chart it has coordinates \(\operatorname{Ad}(g^{-1})\beta_i(d\pi w)\), so it is smooth. The formula also proves horizontality and equivariance. Its construction is pointwise inverse to (A.10). Addition acts freely and transitively on connections, since their actual difference is uniquely determined. □

## B. Constructing and extending connections

**Theorem B.1 (existence).** Every principal bundle over \(M\) admits a smooth principal connection.

**Proof.** Choose a trivializing open cover. On each member use the product connection of A.3 with \(A=0\). By Local tools 3.1 there is a locally finite smooth partition \((\phi_i)\) with each support contained in a member of a trivializing refinement; let \(\omega_i\) be the corresponding product connection. Set
\[
\omega=\sum_i(\phi_i\circ\pi)\,\omega_i.
\tag{B.1}
\]
Each term is extended by zero off that chart. It is smooth there because every point outside the chart has a neighbourhood disjoint from the closed support of its coefficient. The pullback family is locally finite: a neighbourhood of \(\pi(p)\) meeting finitely many base supports pulls back to a neighbourhood of \(p\) meeting only their pullbacks. Thus the sum is smooth.

Right translation leaves \(\phi_i\circ\pi\) fixed, so every term has the required equivariance. On \(\zeta_X\) the sum equals \((\sum_i\phi_i)X=X\). A.2 proves it is a connection. The proof uses only a smooth subordinate partition, so applies verbatim to any base and principal atlas for which that partition exists. □

**Theorem B.2 (closed sets with locally extendible data).** Let \(K\subset M\) be closed. Suppose a connection splitting of the full \(T_pP\) is prescribed for each \(p\) over \(K\), satisfying the principal identities, and suppose these data agree locally with a smooth connection on \(P|_U\) for neighbourhoods \(U\) of points of \(K\). Then they extend to a global smooth connection. If a connection is specified on an open neighbourhood \(U\) of \(K\), a global extension may be chosen to agree with it on a smaller open neighbourhood of \(K\).

**Proof.** Translate the prescribed splittings to connection-form values by the fibrewise construction in A.2. For the first assertion cover \(K\) by neighbourhoods with the stipulated local connections and add \(M\setminus K\). On this last open set use the restriction of a global connection \(\omega_0\), provided by B.1. Apply the partition construction (B.1) to this cover and these connections. At a point over \(K\), a coefficient assigned to \(M\setminus K\) is zero. Every remaining local connection having a nonzero coefficient agrees with the prescribed form on the whole tangent space there. Their coefficients sum to one; hence the result has exactly the prescribed value. A.2 then recovers the prescribed splitting.

For the stronger neighbourhood statement, choose by Local tools 3.1 a smooth \(\chi:M\to[0,1]\) equal to one on a neighbourhood of \(K\), with support contained in \(U\). On \(P|_U\) the difference \(\omega_U-\omega_0\) is horizontal and equivariant by A.4. Define
\[
\omega=\omega_0+(\chi\circ\pi)(\omega_U-\omega_0),
\tag{B.2}
\]
with the second term extended by zero. The same closed-support argument proves smoothness. A.4 proves it is a connection, and where \(\chi=1\) it equals \(\omega_U\). No smooth extension property is claimed for arbitrary pointwise data on a closed set; the stated local extendibility is the hypothesis used. □

**Theorem B.3 (a connection on a closed embedded submanifold).** Let \(S\subset M\) be a closed embedded submanifold. Every connection on \(P|_S\to S\) is the restriction of a global connection on \(P\).

**Proof.** Restriction means pulling back the connection form to \(P|_S\), so it specifies tangent directions along \(S\), not arbitrary normal directions. Fix \(x\in S\). Choose an ambient trivialization of \(P\) and a smaller submanifold coordinate neighbourhood \((y,z)\) with \(S=\{z=0\}\). Shrink it to a product of open coordinate boxes. The ambient section restricts to a section on \(S\); its given potential has the form
\[
A_S=\sum_{j=1}^{\dim S}a_j(y)\,dy^j.
\]
Each smooth \(\mathfrak g\)-valued coefficient extends to the ambient product box by \(a_j(y,z)=a_j(y)\). Set all \(dz\) coefficients to zero. This defines a smooth ambient potential, and A.3 gives an ambient local connection whose pullback to \(P|_S\) is the prescribed one. This last assertion follows from the full formula (A.6), which restricts to the same tangential potential and the same group term.

Cover \(S\) by these boxes and add the open set \(M\setminus S\), on which use any connection from B.1. Patch them by a subordinate partition as in B.1. At a point over \(S\), all nonzero terms have the same pullback on \(T(P|_S)\), and the coefficients sum to one. The resulting restriction is the given connection. The locally chosen normal components need not agree, and the argument never assumes that they do. □

## C. A horizontal lift exists along the whole path

For a path \(\gamma:[a,b]\to M\), a horizontal lift is a continuous path \(p(t)\) with \(\pi(p(t))=\gamma(t)\), smooth on each smooth piece, and \(\omega(p'(t))=0\) there. At an endpoint or a corner, the derivatives mean the appropriate one-sided derivatives of the smooth pieces.

**Theorem C.1 (global path lifting).** Every initial point \(p_a\in P_{\gamma(a)}\) has a unique horizontal lift on all of \([a,b]\). In a section chart \(p(t)=s(\gamma(t))g(t)\), its group equation is
\[
g'(t)=-dR_{g(t)}\,A_{\gamma(t)}(\gamma'(t)).
\tag{C.1}
\]

**Proof.** Formula (A.6) makes horizontality equivalent to
\(\theta_g g'=-\operatorname{Ad}(g^{-1})A(\gamma')\).
The identity
\[
dL_g\,\operatorname{Ad}(g^{-1})X=dR_g X
\]
follows by differentiating \(g\exp(t\operatorname{Ad}(g^{-1})X)=\exp(tX)g\) at zero, using Local tools 2.3. Applying \(dL_g\) proves (C.1), including its minus sign.

On any closed time segment whose path image lies in a single section chart, \(b(t)=-A_{\gamma(t)}(\gamma'(t))\) is continuous on each of its finitely many smooth pieces and has finite one-sided limits at their endpoints. Local tools 2.2 therefore solves the right invariant equation \(g'=dR_g b(t)\) on the entire segment, for any initial value. Its result does not assume compactness of \(G\) or completeness of a Riemannian metric. Where \(b\) is smooth, Local tools 2.1 gives a smooth solution.

We justify a finite subdivision into such segments. The inverse images of trivializing sets are an open cover of the compact interval. Around each time \(t\), choose a relative interval of radius \(2\epsilon_t>0\) contained in one inverse image. Finitely many intervals of radii \(\epsilon_t\) cover \([a,b]\), by Local tools 0.1. Let \(\delta>0\) be smaller than all those finitely many \(\epsilon_t\). If an interval has length less than \(\delta\), choose one of its points and one of the smaller intervals containing that point; every point of the original interval then lies within \(2\epsilon_t\) of its centre. Thus its entire image lies in the chosen trivializing set. Partition \([a,b]\) into intervals of length below \(\delta\), also inserting the original path corners. Finiteness and existence of such a subdivision follow by choosing an integer larger than \((b-a)/\delta\).

Solve successively on these segments, using the endpoint of one as the initial point of the next. In each chart the right invariant equation has a unique solution. Consequently any two constructed lifts agree first near the initial time and then on each subsequent segment. At an artificially inserted division point where \(\gamma\) is smooth, choose a chart around the value of \(\gamma\) there; the local smooth equation and uniqueness identify the two pieces with one smooth solution. Thus no new corner was introduced. This gives a lift on the whole path and proves its uniqueness. The same argument runs backwards from any specified time. For \(a=b\), the lift is the single given point. □

**Theorem C.2 (smoothness and the transport identities).** Let \(T_\gamma:P_{\gamma(a)}\to P_{\gamma(b)}\) send an initial point to the endpoint of its horizontal lift. It is a smooth \(G\)-equivariant diffeomorphism. Reversing the path inverts it, and following \(\gamma_1\) by \(\gamma_2\) gives \(T_{\gamma_2}\circ T_{\gamma_1}\). Orientation-preserving piecewise smooth reparametrizations leave transport unchanged. Lifts depend smoothly on initial data and on finite dimensional smooth families of paths, on each fixed smooth piece.

**Proof.** We first make the parameter statement precise. Let \(\lambda\) range in an open subset of a finite dimensional Euclidean space; assume \((\lambda,t)\mapsto\gamma_\lambda(t)\) is smooth on each fixed closed time piece, in the sense that it extends smoothly near that piece. For a fixed \(\lambda_0\), choose the subdivision in C.1 with each closed segment lying inside an open trivializing set. Each such containment persists for all \(\lambda\) sufficiently near \(\lambda_0\): for every time in the segment, continuity gives a product of a parameter neighbourhood and a time neighbourhood mapping into that trivializing set; finitely many time neighbourhoods cover the compact segment, and their parameter neighbourhoods have an open intersection containing \(\lambda_0\). Take the intersection over the finitely many segments as well. Thus the same finite subdivision and charts work near \(\lambda_0\).

In each chart (C.1) is a smooth ordinary differential equation in time, position and parameter on a fixed piece. Local tools 2.1 supplies smooth dependence locally around every point of a reference solution. To obtain dependence up to a fixed segment endpoint, cover the reference graph on that segment by finitely many such local existence neighbourhoods and choose a subdivision fine enough to remain in them. Iterating their smooth solution maps gives smooth dependence at each successive endpoint. After each iteration, shrink the neighbourhood of the initial datum and parameter if necessary so that its endpoint lies in the next existence neighbourhood; only finitely many restrictions are made. This constructs a common neighbourhood with smooth dependence across the whole segment. Changes of principal chart are smooth by PB A.2, and composition over the finite path subdivision proves the assertion. Initial points in varying initial fibres are described using a section near \(\gamma_{\lambda_0}(a)\); this gives precisely the local meaning of smooth dependence on initial data. The assertion on each fixed smooth piece follows from the corresponding local time-dependent solution maps. In particular \(T_\gamma\) is smooth.

If \(p(t)\) is horizontal, (A.4) makes \(p(t)c\) horizontal for any fixed \(c\in G\), with initial point \(p(a)c\). Uniqueness gives \(T_\gamma(pc)=T_\gamma(p)c\). The reversed lift \(p(a+b-t)\) is horizontal by the chain rule; its endpoint is the original initial point. Hence reverse transport is a two-sided inverse, and is smooth by the first part. Concatenated lifts give the composite endpoint map; uniqueness proves the stated order.

For reparametrization, let \(\tau:[c,d]\to[a,b]\) be a continuous, piecewise smooth, increasing bijection with the endpoints in this order. Then \(p\circ\tau\) lifts \(\gamma\circ\tau\), and on each smooth piece
\(\omega((p\circ\tau)')=\tau'\omega(p'\circ\tau)=0\).
Preimages of the finitely many corners introduce only finitely many additional division points. This holds even where \(\tau'=0\); no division by that derivative is used. Uniqueness proves equality of transport. The same proof permits nondecreasing surjections with finitely many smooth pieces: preimages of original corner times are intervals or points, so their finitely many endpoints suffice, and the lift is constant on each intervening constant interval. □

## D. The derivative on an associated vector bundle

Let \(\rho:G\to\mathrm{GL}(W)\) be a smooth representation on a finite dimensional real or complex vector space \(W\); a complex representation is smooth with respect to the underlying real manifolds. Let \(\rho_*:\mathfrak g\to\operatorname{End}(W)\) be its derivative at \(e\), using the open matrix model for \(\mathrm{GL}(W)\). Set \(E=P\times_G W\).

**Theorem D.1 (induced covariant derivative).** If a section \(\sigma\) corresponds by PB B.2 to the equivariant function \(u:P\to W\), define
\[
(\nabla_v\sigma)(x)=[p,du_p(L_p(v))],
\qquad v\in T_xM,\quad p\in P_x.
\tag{D.1}
\]
This is well defined and smooth. For a local section \(s\) and coordinate function \(u_s=u\circ s\), its formula is
\[
(\nabla\sigma)_s=du_s+\rho_*(A)u_s.
\tag{D.2}
\]
It is linear over smooth functions in the tangent direction, linear over constants in \(\sigma\), and satisfies
\(\nabla_v(f\sigma)=df(v)\sigma+f\nabla_v\sigma\).

**Proof.** From the uniqueness in (A.5) and equivariance of the connection,
\(L_{pa}(v)=dR_a L_p(v)\).
Differentiating \(u(pa)=\rho(a^{-1})u(p)\) for a constant \(a\) yields
\[
du_{pa}(dR_a w)=\rho(a^{-1})du_p(w).
\]
The associated relation in PB B.1 now proves that (D.1) is independent of \(p\). Smoothness follows in local charts from smoothness of \(u,L\) and the associated quotient chart.

For a vertical vector, use the equivariance along \(p\exp(tX)\). The derivative at zero of \(\rho(\exp(-tX))\) is \(-\rho_*X\), by the chain rule and \(d\exp_0=\mathrm{id}\), proved in Local tools 2.3. Therefore
\[
du_p(\zeta_X(p))=-\rho_*X\,u(p).
\tag{D.3}
\]
At \(p=s(x)\), the vector \(ds(v)-\zeta_{A(v)}(s(x))\) projects to \(v\) and has zero \(\omega\)-value. It is \(L_{s(x)}(v)\) by (A.5). Substitution into (D.1), followed by (D.3), gives (D.2).

The map \(v\mapsto L_p(v)\) and the differential \(du_p\) are linear, so multiplication of a vector field by a smooth scalar multiplies (D.1) by that scalar. Constant linear combinations of sections give the same linear combinations of their equivariant functions and differentials. For \(f\sigma\), that function is \((f\circ\pi)u\); its differential on \(L_p(v)\) is
\(df_x(v)u(p)+f(x)du_p(L_p(v))\)
by the product rule and \(d\pi L_p=\mathrm{id}\). This proves Leibniz. All formulas also hold for vector fields by applying them at each point. □

**Theorem D.2 (associated transport and the equation for parallel vectors).** Principal transport induces the smooth linear isomorphism
\[
\mathcal T_\gamma:E_{\gamma(a)}\to E_{\gamma(b)},
\qquad [p,w]\longmapsto[T_\gamma(p),w].
\tag{D.4}
\]
It is the unique transport for which vectors along a path satisfy the local equation
\[
v'(t)+\rho_*(A_{\gamma(t)}(\gamma'(t)))v(t)=0.
\tag{D.5}
\]
In particular it is the parallel transport of the derivative (D.2).

**Proof.** If a representative is changed to \((pc,\rho(c^{-1})w)\), equivariance of \(T_\gamma\) makes the output class unchanged. In fibre charts (D.4) is multiplication by a matrix \(\rho(g)\), so it is smooth and linear. The reverse path gives its smooth linear inverse by C.2.

We verify its differential equation without assuming any exponential identity for representations. For \(X\in\mathfrak g\), differentiating
\(\rho(\exp(tX)g)=\rho(\exp(tX))\rho(g)\)
at zero gives
\[
d\rho_g(dR_g X)=\rho_*X\,\rho(g).
\tag{D.6}
\]
If \(p(t)=s(\gamma(t))g(t)\) is horizontal, the coordinate of \([p(t),w]\) is \(v(t)=\rho(g(t))w\). Combining (C.1) with (D.6) yields exactly (D.5). For arbitrary initial \(v(a)\), (D.4) provides a solution on the whole path. Uniqueness is the local linear differential-equation uniqueness in Local tools 2.1, applied successively on the same finite chart subdivision; hence it is the unique solution.

For completeness, the derivative of a general vector field \(v(t)\) along a smooth path is locally \(v'+\rho_*(A(\gamma'))v\). This is (D.2) applied to the pullback bundle over the time interval. The pullback principal charts are those of PB A.3, and (A.7) pulled back along \(\gamma\) proves that their potentials still transform correctly. Thus the derivative is independent of the chart, and its zero equation is (D.5). For a section of \(E\), substituting its values along the path recovers D.1 by the chain rule. □

## E. Product transport and transport on the Hopf bundle

**Lemma E.1 (the circle parameter and the constant \(\pi\)).** On \(U(1)\) the group exponential \(z(t)=\exp_{U(1)}(it)\) has \(z'=iz\), \(z(0)=1\), and period \(2\pi\). It is injective on \([0,2\pi)\) and traverses the unit circle once with positive tangent \(iz\). For a real smooth function \(b(t)\), the scalar equation \(g'=-ib(t)g\) has solution
\[
g(t)=\exp_{U(1)}\!\left(-i\int_a^t b(s)\,ds\right)g(a).
\tag{E.1}
\]

**Proof.** PB E.1 constructs \(U(1)\) as a smooth level set. At \(1\) its tangent space is \(i\mathbb R\), since the derivative of \(|z|^2\) is \(2\operatorname{Re}(\bar z\,\cdot)\). The group exponential of Local tools 2.3 solves \(z'=iz\), has the addition identity \(z(t+s)=z(t)z(s)\), and exists for all real \(t\).

We identify its period with the circular constant, rather than assume it. DG-CHAR-17 A.5 proves
\[
\pi=4\int_0^1\frac{du}{1+u^2},
\tag{E.2}
\]
with \(\pi\) also equal to the unit disk area. Define
\[
\alpha(u)=\frac{1+iu}{1-iu},\qquad
t(u)=2\int_0^u\frac{dr}{1+r^2}.
\]
The denominator is never zero for real \(u\), and \(|\alpha(u)|=1\). Differentiation gives
\(\alpha'(u)=2i\alpha(u)/(1+u^2)=i\alpha(u)t'(u)\).
The map \(t(u)\) is strictly increasing because \(t'(u)>0\); its inverse is smooth on its range by Local tools 1.2. Substitution \(r=1/s\) in the integral from \(1\) to a finite \(R>1\), followed by \(R\to\infty\), shows
\(\int_0^\infty dr/(1+r^2)=2\int_0^1 dr/(1+r^2)=\pi/2\).
The integrand is even, so the range of \(t(u)\) is \((-\pi,\pi)\). Here the inverse exists onto this interval by strict monotonicity, continuity and the intermediate value theorem in Local tools 0.0. The curve \(\alpha(u(t))\) solves \(z'=iz\) with value \(1\) at zero; uniqueness in Local tools 2.1 identifies it with \(z(t)\) on that interval.

The map \(\alpha\) is a bijection from \(\mathbb R\) to \(U(1)\setminus\{-1\}\): for \(z=X+iY\ne-1\) on the circle, its inverse is \(u=Y/(1+X)\), as substitution verifies using \(X^2+Y^2=1\). Also \(\alpha(u)\to-1\) as \(u\to\pm\infty\). Continuity of the global solution therefore gives \(z(\pi)=z(-\pi)=-1\). The addition identity gives \(z(2\pi)=1\) and \(z(t+2\pi)=z(t)\). On \((-\pi,\pi)\), injectivity follows from \(\alpha\) and the strict increase of \(t(u)\), with neither endpoint value \(-1\) attained inside. Every half-open interval of length \(2\pi\), in particular \([0,2\pi)\), consequently gives each circle point once, by shifting the parameter and multiplying by the fixed value of \(z\) at the shift. The tangent is \(iz\), which fixes the positive orientation.

Finally the chain rule and the fundamental theorem applied to the integral in (E.1) show that its right side has derivative \(-ib(t)\) times itself and the correct initial value. Uniqueness proves (E.1). The same formula on successive pieces handles a continuous, piecewise smooth \(b\). We may write this group exponential simply as \(\exp(it)\) in the calculations below. □

**Example E.2 (a zero potential and its other descriptions).** On \(M\times G\), \(A=0\) gives the connection \(\omega=\theta\). Its transport keeps the group coordinate constant. After replacing the standard section by \(s'=sh\), its potential is \(h^*\theta\), which need not vanish.

**Proof.** A.3 proves that \(\omega=\theta\) is a connection. Equation (C.1) is now \(g'=0\), so its solution is the constant \(g(t)=g(a)\), by Local tools 0.3 or uniqueness in 2.1. Formula (A.7) gives \(A'=h^*\theta\). For an explicit nonzero example take \(G=(\mathbb R,+)\), \(M=\mathbb R\), and \(h(x)=x\). Its left form is \(dg\), so the new potential is \(dx\), though the total connection has not changed. □

**Example E.3 (the Hopf connection and its latitude transport).** On the principal bundle \(S^3\to\mathbb {CP}^1\) of PB E.1, the form
\[
\omega=\bar z_0\,dz_0+\bar z_1\,dz_1
\tag{E.3}
\]
is a \(U(1)\)-connection. In the unit section \(s_0(w)=(1,w)/\sqrt{1+|w|^2}\), its potential is
\[
A_0=\frac{\bar w\,dw-w\,d\bar w}{2(1+|w|^2)}.
\tag{E.4}
\]
For the loop \(w(\phi)=r\exp(i\phi)\), \(0\le\phi\le2\pi\), its transport from \(s_0(r)\) ends at
\[
s_0(r)\exp\!\left(-\frac{2\pi i r^2}{1+r^2}\right).
\tag{E.5}
\]
The induced derivative on the associated tautological line is the orthogonal projection of the ordinary derivative in the product \(\mathbb C^2\)-bundle.

**Proof.** For a tangent vector \(v\) to \(S^3\), differentiation of \(|z_0|^2+|z_1|^2=1\) gives
\(2\operatorname{Re}(\bar z_0v_0+\bar z_1v_1)=0\).
Thus (E.3) takes values in \(i\mathbb R=\mathfrak u(1)\). The fundamental vector for \(i\tau\) is \(i\tau z\), by differentiating scalar multiplication; its \(\omega\)-value is \(i\tau(|z_0|^2+|z_1|^2)=i\tau\). For fixed \(a\in U(1)\), replacing \((z,v)\) by \((za,va)\) leaves each \(\bar z_jv_j\) unchanged. Since \(U(1)\) is abelian, its conjugations and therefore its adjoint action are the identity. These are precisely (A.4), proving it is a connection.

Write \(h=1+|w|^2\). Directly differentiating \(s_0=h^{-1/2}(1,w)\), and using \(dh=\bar w\,dw+w\,d\bar w\), gives
\[
s_0^*ds_0=h^{-1}\bar w\,dw-\frac{dh}{2h},
\]
which is (E.4); here the star means the conjugate transpose of the column \(s_0\). Smoothness of the positive square root follows from Local tools 1.2 as in PB D.2. Along the loop, E.1 gives \(dw=iw\,d\phi\) and \(d\bar w=-i\bar w\,d\phi\), so
\[
A_0(\partial_\phi)=\frac{ir^2}{1+r^2}.
\]
The horizontal equation (C.1) is the scalar equation of E.1, with this constant coefficient. Starting at group coordinate \(1\) and integrating over \(2\pi\) proves (E.5). For \(r=0\) the path and its lift are constant, also agreeing with the formula.

To see path dependence at a fixed base point, take two distinct finite positive radii. Their factors in (E.5) are distinct, because \(r^2/(1+r^2)\) is strictly increasing in \(r>0\), has values in \((0,1)\), and E.1 proves injectivity of the exponential over one period. For each radius, precede its loop by the radial segment from \(w=0\) to \(w=r\), and follow it by the reverse radial segment. Formula (E.4) vanishes on these real radial segments, so their lifts have constant section coordinate; C.2 shows that the two resulting loops, now both based at \(w=0\), have exactly the two distinct factors. Hence the endpoints alone do not determine transport.

PB E.1 identifies the associated standard line with the tautological line. In its unit frame \(s_0\), a local vector is \(s_0 u\) for a complex scalar \(u\). Orthogonal projection of a vector \(v\in\mathbb C^2\) onto this line is \(s_0(s_0^*v)\): its difference from \(v\) has inner product zero with \(s_0\), and \(s_0^*s_0=1\). Projecting \(d(s_0u)\) therefore gives
\[
s_0\bigl(du+(s_0^*ds_0)u\bigr)=s_0(du+A_0u).
\]
D.1 gives this same formula for the induced derivative. The second unit chart gives the same conclusion and covers the remaining point; both constructions are intrinsic under change of frame. □

## F. Exercises with complete solutions

**Exercise F.1 (check the matrix formula).** Let \(G\) be an embedded matrix Lie group and \(A\in\Omega^1(M,\mathfrak g)\). Verify directly that on \(M\times G\)
\[
\omega=g^{-1}Ag+g^{-1}dg
\tag{F.1}
\]
is a principal connection.

**Solution.** Left multiplication and inversion in the matrix group give \(\theta_g(\eta)=g^{-1}\eta\); differentiating conjugation gives \(\operatorname{Ad}(g^{-1})X=g^{-1}Xg\). These expressions belong to \(\mathfrak g\), since they are derivatives at the identity of curves in \(G\). Thus (F.1) is a smooth \(\mathfrak g\)-valued form. A fundamental vector is \((0,gX)\), on which it has value \(X\). For constant \(a\in G\), a tangent \((v,\eta)\) at \((x,g)\) is sent to \((v,\eta a)\) at \((x,ga)\), and (F.1) there equals
\[
a^{-1}\bigl(g^{-1}A(v)g+g^{-1}\eta\bigr)a
=\operatorname{Ad}(a^{-1})\omega(v,\eta).
\]
A.2 supplies exactly the two necessary and sufficient identities, so this proves the assertion directly. □

**Exercise F.2 (transport around an abelian rectangle).** On the trivial \(U(1)\)-bundle over \(\mathbb R^2\), take \(A=i x\,dy\). Starting at group coordinate \(1\) over \((0,0)\), compute transport along the positively oriented boundary of \([0,a]\times[0,b]\), where \(a,b>0\).

**Solution.** Travel first in the positive \(x\)-direction, then the positive \(y\)-direction, then backwards in \(x\), then backwards in \(y\). On the first and third sides \(dy=0\), so the group coordinate does not change by (C.1). On the second side \(x=a\), and E.1 gives the factor \(\exp(-iab)\). On the final side \(x=0\), so its factor is \(1\). C.2 composes them to \(\exp(-iab)\). For any initial group coordinate \(c\), equivariance gives endpoint \(\exp(-iab)c\). This computation uses the four ordinary differential equations, without assuming a curvature or Stokes theorem. □

**Exercise F.3 (extend an axis potential with a cutoff).** Let \(f:\mathbb R\to\mathbb R\) be smooth. Extend \(A_S=i f(x)\,dx\) from the \(x\)-axis to a potential on the plane which vanishes outside \(|y|<2\).

**Solution.** Let \(\eta(t)=e^{-1/t^2}\) for \(t>0\), zero for \(t\le0\), the smooth flat function of Local tools 0.5, and put
\[
\chi(y)=\frac{\eta(3-y^2)}
 {\eta(3-y^2)+\eta(y^2-1)}.
\tag{F.2}
\]
The denominator is positive everywhere: its first term is positive when \(y^2<3\), while its second term is positive when \(y^2>1\), and these two conditions cover all real \(y\). Thus \(\chi\) is smooth, lies between zero and one, equals one for \(|y|\le1\), and equals zero for \(|y|\ge\sqrt3\). Define \(A=i\chi(y)f(x)\,dx\). It pulls back to \(A_S\) on \(y=0\), and vanishes for \(|y|\ge2\); indeed its support in the \(y\)-direction is contained in \([-\sqrt3,\sqrt3]\subset(-2,2)\). A.3 gives the full principal connection from this potential. This extends the tangential data as in B.3, without prescribing unrelated normal data. □

**Exercise F.4 (a noncommuting rectangle).** On the trivial real or complex rank-two vector bundle over \(\mathbb R^2\), let the connection potential be \(A=B\,dx+C\,dy\), for fixed matrices \(B,C\). Determine the transport matrix around the same positive rectangle and its leading term as \(a,b\to0\).

**Solution.** Use the standard representation of the corresponding general linear group. D.2 gives \(v'=-A(\gamma')v\). For a constant matrix \(D\), the matrix exponential \(e^{tD}\) is the group exponential of Local tools 2.3, equivalently the solution of \(U'=DU,\ U(0)=I\). To verify the latter description from that lesson's left invariant convention, it first gives \(U'=UD\). The function \(V(t)=DU(t)-U(t)D\) then satisfies \(V'=VD,\ V(0)=0\); uniqueness of the linear matrix equation by Local tools 2.1 makes \(V=0\). Thus \(U'=DU\) as well. This also proves the constant-coefficient transport formula without assuming a power-series theorem.

The four successive factors are \(e^{-aB}\), \(e^{-bC}\), \(e^{aB}\), and \(e^{bC}\), each acting on the left of the current vector. Therefore
\[
H(a,b)=e^{bC}e^{aB}e^{-bC}e^{-aB}.
\tag{F.3}
\]
In particular \(H(a,0)=H(0,b)=I\), by the group exponential addition identity. Differentiate first in \(a\) at \(a=0\):
\[
\partial_aH(0,b)=e^{bC}Be^{-bC}-B.
\]
Differentiating this in \(b\) at zero gives
\(\partial_b\partial_aH(0,0)=CB-BC=-[B,C]\),
where \([B,C]=BC-CB\). The mixed partials commute by PB C.3. Twice applying the fundamental theorem, using the two constant axis values, yields
\[
H(a,b)-I
=\int_0^a\int_0^b
 \partial_a\partial_b H(s,t)\,dt\,ds.
\tag{F.4}
\]
The group exponential is smooth by Local tools 2.3, so \(H\) has continuous third derivatives. On a fixed small compact rectangle these are bounded by Local tools 0.1. The segment estimate in 0.3 then bounds
\(\|\partial_a\partial_bH(s,t)-\partial_a\partial_bH(0,0)\|\)
by \(K(|s|+|t|)\), for some \(K\). Integrating this bound, also for negative oriented endpoints by taking absolute values of the integrals, proves
\[
H(a,b)=I-ab[B,C]
 +O\!\left(|ab|(|a|+|b|)\right).
\tag{F.5}
\]
This remainder estimate remains valid when either side is zero, because then the exact transport is \(I\). It fixes both the travel order and the sign of the leading commutator. □

## Free construction source

Peter W. Michor, [*Topics in Differential Geometry*, freely accessible author draft](https://www.mat.univie.ac.at/~michor/dgbook.pdf), Section 17.3 for projections, complements and horizontal lifts; Sections 19.1, 19.3–19.4 and 19.6 for principal forms, local potentials, existence and transport; Sections 19.8, 19.10, 19.12 and 19.14–19.15 for associated transport and derivatives. Only the connection and degree-zero derivative constructions are used here; curvature, higher covariant exterior derivatives and general holonomy theorems are not prerequisites. The invariant equation and parameter arguments are proved in the earlier Local tools lesson, and the local proofs above supply the extension, equivariance and coordinate calculations.

Original exposition: CC0 1.0. The freely accessible human construction source is credited above. Earlier programme lessons retain their own source credits and licences.

## References

[Meinrenken] Eckhard Meinrenken, *Principal bundles and connections*, lecture notes, [University of Toronto](https://www.math.toronto.edu/mein/teaching/moduli.pdf).

