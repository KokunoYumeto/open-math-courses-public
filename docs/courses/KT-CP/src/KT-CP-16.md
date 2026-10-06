# C*-algebras of foliations and their Morita equivalences

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A transversal records the transport between plaques, while the foliation algebra also contains the integral kernels along them. Groupoid equivalence explains precisely how these descriptions retain the same operator-module and K-theoretic information. We apply it to submersions, orbit foliations and suspensions, keeping track of which groupoid is actually the holonomy groupoid.

We use the groupoid equivalence theorem proved in [Lesson 15](KT-CP-15.md), the transformation-groupoid identifications of [Lesson 14](KT-CP-14.md), and the Thom and PV results of [Lesson 11](KT-CP-11.md). Throughout, manifolds are second countable and Hausdorff; foliations are smooth and have constant rank. Arrow spaces may be locally Hausdorff without being Hausdorff. In that case compactly supported kernels mean finite sums of kernels supported in Hausdorff charts, as in Lessons 13–15.

## The recalled construction and its scalar form

Let \(F\subset TV\) have rank \(p\), and let \(G=\operatorname{Hol}(V,F)\). An arrow is a leafwise path modulo equality of endpoints and holonomy germ. We recall the construction from *The C*-algebra of a foliation*, Lemma 1.1, Lemma 2.1 and Theorem 2.2: its local arrow coordinates are

\[
(t',t,u),\qquad
s(t',t,u)=(t,u),\quad r(t',t,u)=(t',h(u)).
\tag{16.1}
\]

Here \(t,t'\) are plaque coordinates and \(h\) is the transverse transport of the chosen path. The arrow manifold has dimension \(2p+q\), where \(q=\dim V-p\). Its source fibres are Hausdorff holonomy coverings of leaves, and \(r:G_x\to L_x\) is their covering map. Its orbits are the connected leaves. We use these construction results rather than reconstructing the atlas.

The same lesson, §3 and Definition 4.1, defines kernels with values in

\[
\Omega_\gamma^{1/2}
=D_{r\gamma}^{1/2}\otimes D_{s\gamma}^{1/2},
\qquad D_x^{1/2}=|\Lambda^p F_x^*|^{1/2}.
\tag{16.2}
\]

Convolution contracts the two half-densities at the intermediate endpoint; involution conjugates and exchanges endpoints. The **foliation algebra** in this lesson is the reduced completion of these kernels:

\[
\mathcal A_F=C_r^*(V,F).
\tag{16.3}
\]

The full groupoid algebra will always be written \(C^*(G)\). Using the same symbol for the two completions would obscure the orbit examples.

**Lemma 16.1.** A smooth positive leaf density \(\rho\) identifies the half-density completion with \(C_r^*(G,\lambda_\rho)\), with the conventions of Lesson 14.

**Proof.** Such a density exists by choosing a metric on \(F\). On \(G_x\), lift \(\rho\) along its local diffeomorphism \(r:G_x\to L_x\), obtaining \(\nu_x=r^*\rho\). Right multiplication preserves \(r\), so these source-fibre measures are right invariant. Inversion gives a left Haar system \(\lambda_\rho^x\). It has full support. Integration in the coordinates (16.1), followed by a finite chart partition for each compact kernel, proves continuity of its integrals.

Every half-density kernel has the unique scalar expression

\[
k(\gamma)=f(\gamma)\rho_{r\gamma}^{1/2}\otimes\rho_{s\gamma}^{1/2}.
\tag{16.4}
\]

The intermediate factors in a product give \(\rho\); integration over factorizations of \(\gamma\) is therefore exactly

\[
(f*g)(\gamma)=\int_{G^{r\gamma}}
 f(\eta)g(\eta^{-1}\gamma)\,d\lambda_\rho^{r\gamma}(\eta),
\qquad f^*(\gamma)=\overline{f(\gamma^{-1})}.
\tag{16.5}
\]

For the regular representation at \(x\), write a source-fibre half-density as \(\xi(\gamma)\nu_x(\gamma)^{1/2}\). This is a unitary identification with \(L^2(G_x,\nu_x)\). Contracting its density factor against (16.4) gives

\[
(\Lambda_x(f)\xi)(\gamma)
=\int_{G_x}f(\gamma\zeta^{-1})\xi(\zeta)\,d\nu_x(\zeta).
\tag{16.6}
\]

Thus each regular norm, and their supremum, agrees with Lesson 14's scalar norm. Smooth compact kernels and continuous compact kernels have the same completion: approximate each chart-supported scalar function uniformly by smooth functions in a fixed compact chart neighbourhood. A positive compact bump dominating that neighbourhood has bounded range and source Haar integrals, so the uniform error tends to zero in the \(I\)-norm and hence in the reduced norm. Finite sums handle all kernels. \(\square\)

For completeness, the scalar change under \(\rho'=b\rho\), \(b>0\), is

\[
f'(\gamma)=b(r\gamma)^{-1/2}f(\gamma)b(s\gamma)^{-1/2}.
\tag{16.7}
\]

Indeed \(\nu'_x=b\circ r\,\nu_x\), and \(\xi\mapsto(b\circ r)^{-1/2}\xi\) is a unitary between the two scalar \(L^2\)-spaces. Substitution in (16.6) intertwines their kernels. On any fixed compact support the two weights and their inverses are bounded. The formula consequently extends to the completions. This explicit identification is the density independence needed below.

## A complete transversal

A complete transversal is a second countable \(q\)-manifold \(N\) with a transverse immersion \(j:N\to V\), meeting every leaf. It may be a countable disjoint union of small slices. Transversality says

\[
dj(T_nN)\oplus F_{j(n)}=T_{j(n)}V.
\tag{16.8}
\]

An embedded transversal is a special case. For an immersion, remembering the point of \(N\) distinguishes overlapping slices. Define

\[
\begin{aligned}
H&=\{(n',\gamma,n):r\gamma=j(n'),\ s\gamma=j(n)\},\\
Z&=\{(\gamma,n):s\gamma=j(n)\},\\
r_Z(\gamma,n)&=r\gamma,\qquad s_Z(\gamma,n)=n.
\end{aligned}
\tag{16.9}
\]

The topology is the corresponding fibre-product topology. The units of \(H\) are \(N\), with source \(n\) and range \(n'\).

**Theorem 16.2.** The groupoid \(H\) is étale and has its counting Haar system. The space \(Z\) is a \(G\)-\(H\) equivalence. In particular

\[
\mathcal A_F\sim_M C_r^*(H).
\tag{16.10}
\]

The analogous Morita equivalence \(C^*(G)\sim_M C^*(H)\) holds for the full scalar algebras.

**Proof.** Work in (16.1) near an arrow whose source belongs to a chosen transverse slice. Transversality makes its transverse coordinate a local coordinate on that slice; its plaque coordinate is a smooth function of it. Restricting the source to \(j(N)\) leaves the coordinates \((t',u)\). The range map is \((t',u)\mapsto(t',h(u))\), a local diffeomorphism. Hence \(r_Z\) is open. It is onto because the transversal meets every leaf and any two points on a leaf are joined by a leafwise path. The map \(s_Z\) is locally the projection \((t',u)\mapsto n(u)\), so it too is open and onto.

Restrict the range to another transverse slice. Its plaque coordinate is again determined by its transverse coordinate, leaving only \(u\). Both \(s_H\) and \(r_H\) are local diffeomorphisms. This proves étaleness, including the topology rather than just a count of dimensions. The resulting arrow space is second countable and locally Hausdorff; its source and range fibres are discrete and Hausdorff. Counting measures have full support, are left invariant by the bijections of fibres, and integrate a compact chart function continuously. They are the required Haar system. Restricting the ambient leaf measures to \(N\) would usually give zero and is not this construction.

The actions are

\[
\eta\cdot(\gamma,n)=(\eta\gamma,n),\qquad
(\gamma,n')\cdot(n',\delta,n)=(\gamma\delta,n).
\tag{16.11}
\]

They preserve the opposite anchors and commute by associativity. For two points with the same \(s_Z\), the unique left division is \(\gamma_1\gamma_2^{-1}\). For two points with the same \(r_Z\), the unique right division is

\[
(n_1,\gamma_1^{-1}\gamma_2,n_2).
\tag{16.12}
\]

Multiplication and inversion make both division maps continuous. Thus each action-relation map is a homeomorphism onto the corresponding equal-anchor fibre product. Those fibre products are closed, since \(V\) and \(N\) are Hausdorff. Inclusion of a closed subspace is universally closed, so both actions are proper in the convention of Lesson 15. Uniqueness of division proves freeness. Division also says that left orbits are exactly the fibres of \(s_Z\), and right orbits the fibres of \(r_Z\). The two open surjections give exactly the quotient topologies. All equivalence conditions are now checked.

Lemma 16.1 supplies the Haar system on \(G\), and counting supplies it on \(H\). Apply Theorem 15.3 to obtain both Morita equivalences. \(\square\)

This proof also explains why an arbitrary subset meeting all leaves is insufficient. The local transverse coordinates establish open anchors. The counterexample to a mere closed full reduction in Lesson 13 does not satisfy this condition.

## Submersions and compact kernels

Let \(p:V\to B\) be a smooth surjective submersion with connected fibres. Give \(V\) the foliation \(F=\ker dp\).

**Proposition 16.3.** Its holonomy groupoid is the fibre-pair groupoid

\[
G=V\times_B V,\qquad
(v_2,v_1):v_1\longrightarrow v_2.
\tag{16.13}
\]

Both its full and reduced algebras are Morita equivalent to \(C_0(B)\).

**Proof.** A leaf is one fibre: a connected manifold is path connected, and the distribution \(\ker dp\) has exactly its fibre components as integral leaves. In submersion boxes the transverse coordinate is the value of \(p\). Transport along any path in a fibre keeps that coordinate fixed. All its loops have trivial holonomy, so paths with the same endpoints define the same arrow. Every pair in (16.13) is joined by a path. The arrow charts (16.1) become \((t',t,b)\), precisely the local fibre-product charts. The bijection is therefore a smooth groupoid isomorphism.

Use \(Z=V\) between \(G\) and the unit groupoid \(B\), with anchors \(\operatorname{id}_V,p\). Both are open surjections. The left action is \((v_2,v_1)v_1=v_2\); the right unit action fixes points. The left relation map is the identity identification with the closed relation \(p(v_2)=p(v_1)\), and the right relation map is the closed diagonal. They are proper and free. The left quotient is \(B\) by the open map \(p\), and the right quotient is \(V\). Smooth fibre densities give a full Haar system on \(G\); the unit system on \(B\) is counting. Theorem 15.3 gives the assertions. \(\square\)

There is an explicit module behind this equivalence. Choose a smooth positive density \(\rho_b\) on \(V_b=p^{-1}(b)\), and complete \(C_c^\infty(V)\) for

\[
(\xi a)(v)=\xi(v)a(p(v)),\qquad
\langle\xi,\eta\rangle(b)=
\int_{V_b}\overline{\xi(v)}\eta(v)\,d\rho_b(v).
\tag{16.14}
\]

Denote the resulting Hilbert \(C_0(B)\)-module by \(E_p\). Fibre integration in finitely many submersion boxes makes the inner product continuous; it is zero outside the compact image of the two supports. Positivity is pointwise, and a nonzero function has positive squared integral on some fibre. The completion is therefore a Hilbert module. For each \(b\), a bump nonzero at a point of \(V_b\) gives \(\langle\xi,\xi\rangle(b)>0\). These inner products generate an ideal with no common zero, hence all of \(C_0(B)\). The module is full.

Its fibre at \(b\) is \(L^2(V_b,\rho_b)\). Restrictions of smooth compact functions are dense there: a compact smooth function on \(V_b\) extends through finitely many submersion boxes and a partition of unity to a compact smooth function on \(V\). The inner-product formula then identifies the fibre norm with its \(L^2\)-norm.

**Proposition 16.4.** Under this module description,

\[
C^*(V\times_B V)\cong C_r^*(V\times_B V)
\cong\mathcal K(E_p),\qquad
k_{\xi,\eta}(v,w)=\xi(v)\overline{\eta(w)}
\longmapsto\Theta_{\xi,\eta}.
\tag{16.15}
\]

**Proof.** The module in Proposition 16.3 is exactly (16.14): substituting the unit-groupoid right side in (15.10) integrates over a fibre of \(p\). Its left form is \(k_{\xi,\eta}\), and its left action is fibrewise integration. The reduced equivalence theorem identifies the left algebra with the compact operators on that module; this is the complementary-full-corner identification used in Theorem 15.3. The full module has the same right algebra \(C_0(B)\) and the same inner-product norm on its dense core. It is therefore the same completed module. The full equivalence similarly identifies its left algebra with \(\mathcal K(E_p)\). Both identifications carry a rank kernel to the displayed rank operator, so the full-to-reduced map becomes the identity on a dense family and is an isomorphism. \(\square\)

A literal tensor-product description requires a specified global module trivialization. If

\[
E_p\cong C_0(B)\otimes\mathcal H
\quad\text{as Hilbert }C_0(B)\text{-modules},
\tag{16.16}
\]

then rank operators identify (16.15) with \(C_0(B)\otimes\mathcal K(\mathcal H)\). This means a trivialization compatible with the continuous sections and module structure, not just individual isomorphisms between fibre Hilbert spaces.

For \(V=B\times P\) with connected \(P\) and a fixed smooth positive density on \(P\), (16.16) is explicit with \(\mathcal H=L^2(P)\). Finite sums \(a(b)\xi(y)\) are dense in \(E_p\): approximate a compact smooth function on \(B\times P\) uniformly on a fixed compact support by such sums, and bound the module error by that compact set's finite \(\rho\)-measure. Hence

\[
\mathcal A_F\cong C_0(B)\otimes\mathcal K(L^2(P)).
\tag{16.17}
\]

When \(\dim P>0\), this is an infinite-dimensional separable Hilbert space. When connected \(P\) has dimension zero, \(P\) is one point and the compact-operator factor is \(\mathbb C\). Connectedness in Proposition 16.3 cannot be suppressed: for \(V=B\times\{0,1\}\), leaves are points, the holonomy algebra is \(C_0(B)\oplus C_0(B)\), whereas the full fibre-pair algebra would be \(M_2(C_0(B))\).

Morita invariance of K-theory now gives, without assuming (16.16),

\[
K_i(\mathcal A_{\ker dp})\cong K_i(C_0(B)).
\tag{16.18}
\]

Here and below Morita invariance uses the written programme proof in *Morita invariance of K-theory and maps induced by correspondences*, Corollary 2.2 and Theorem 5.1. The second countable foliation groupoids and transversals have separable C*-algebras, so its sigma-unital hypotheses hold.

## Orbit foliations: which arrows survive?

Suppose a connected Lie group \(H\) acts smoothly on \(V\), with constant-dimensional orbits defining \(F\). Assume specifically that the holonomy groupoid is isomorphic, over \(V\), to the transformation groupoid \(V\rtimes H\), including its smooth topology. For a free action this is the relevant transformation-groupoid hypothesis; the hypothesis also specifies the groupoid in cases where freeness is not imposed.

**Proposition 16.5.** Under that groupoid identification,

\[
\mathcal A_F\cong C_0(V)\rtimes_r H.
\tag{16.19}
\]

If \(H\) is amenable, this also equals the full crossed product.

**Proof.** Identify the leaf tangent bundle with the Lie algebroid of \(V\rtimes H\). Choose its density at the units from the fixed Haar density of \(H\), and right translate it on source fibres. For a holonomy groupoid its anchor is an isomorphism onto \(F\); right translation followed by \(dr\) is this anchor at the range point. Thus this density is the lifted leaf density used in Lemma 16.1. Inversion gives the usual left Haar system on the transformation groupoid. Lemma 16.1 and Theorem 14.3 give the reduced isomorphism. In target coordinates, the scalar convolution conversion is

\[
a(h)(v)=\Delta_H(h)^{-1/2}f(v,h).
\tag{16.20}
\]

This is the modular correction already verified in Lesson 14. Amenability gives full equals reduced by Lesson 4. \(\square\)

Local freeness only says that stabilizers are discrete. Holonomy instead identifies loops with the same transverse germ, so it can discard such stabilizers. Take the action of \(\mathbb R\) on \(\mathbb T=\mathbb R/\mathbb Z\) by translations. It is locally free, with stabilizer \(\mathbb Z\), and its orbit foliation has one leaf. With a zero-dimensional transversal every loop has trivial holonomy. Its holonomy groupoid is \(\mathbb T\times\mathbb T\), and Lesson 14's pair-groupoid calculation gives

\[
\mathcal A_F=\mathcal K(L^2(\mathbb T)),\qquad
K_0(\mathcal A_F)=\mathbb Z,\quad K_1(\mathcal A_F)=0.
\tag{16.21}
\]

The action groupoid retains isotropy \(\mathbb Z\). Green's theorem, with \(G=\mathbb R\) and subgroup \(\mathbb Z\), gives

\[
C(\mathbb T)\rtimes\mathbb R\sim_M C^*(\mathbb Z)=C(\mathbb T).
\tag{16.22}
\]

Its two K-groups are both \(\mathbb Z\). The real group is amenable, so the full and reduced action algebras agree, but neither is Morita equivalent to (16.21).

For an \(\mathbb R^n\)-orbit foliation satisfying the groupoid hypothesis of Proposition 16.5, the proved Thom theorem gives

\[
K_i(\mathcal A_F)\cong K_{i-n}(C_0(V)),\qquad i\in\mathbb Z/2.
\tag{16.23}
\]

Indeed identify its algebra with the crossed product, use amenability to pass to the full convention of Lesson 11, and apply that lesson's iterated Thom isomorphism. Its coordinate order and signs are those of (11.28)–(11.29); the displayed statement only records parity. For a connected simply connected solvable Lie group of dimension \(d\), under the same holonomy hypothesis, Proposition 11.4 and its Lie-group induction give \(K_i(\mathcal A_F)\cong K_{i-d}(C_0(V))\). Such groups are amenable as successive extensions by real groups, using Lesson 4. None of these conclusions follows just from local freeness.

## Suspensions and the groupoid of germs

Let \(B\) be a connected smooth manifold, \(\widetilde B\) its universal cover, and \(\Gamma=\pi_1(B)\). Let \(P\) be a smooth manifold and \(\rho:\Gamma\to\operatorname{Diff}(P)\) an action. Form

\[
M=(\widetilde B\times P)/\Gamma,\qquad
\gamma(b,x)=(\gamma b,\rho(\gamma)x).
\tag{16.24}
\]

The diagonal action is free and proper, since its projection to the covering space is the deck action. More explicitly, for two compact subsets of the product only finitely many deck transformations can move the first base projection into the second, and each such transformation has a closed graph. Covering boxes give the quotient smooth charts. The images of \(\widetilde B\times\{x\}\) define the horizontal foliation.

Fix a lift \(b_0\) of a point of \(B\). The map \(j(x)=[b_0,x]\) is an embedded complete transversal: deck freeness proves injectivity, a covering box gives the transverse charts, and a path in \(\widetilde B\) joins any base point to \(b_0\). Write \(\operatorname{Germ}(\Gamma,P)\) for the groupoid of germs of the action, with arrows

\[
[\gamma,x]:x\longrightarrow\rho(\gamma)x.
\tag{16.25}
\]

Two labels with the same source represent one arrow exactly when their action maps have the same germ there. A chart consists of \([\gamma,x]\) for \(x\) in an open subset of \(P\). Products compose the germs.

**Proposition 16.6.** The transversal reduction of \(\operatorname{Hol}(M,F)\) is \(\operatorname{Germ}(\Gamma,P)\). Consequently

\[
\mathcal A_F\sim_M C_r^*(\operatorname{Germ}(\Gamma,P)).
\tag{16.26}
\]

If the action satisfies

\[
\text{the germ of }\rho(\gamma)\text{ at }x\text{ is the identity}
\quad\Longrightarrow\quad\gamma=e,
\tag{16.27}
\]

for every \(x\in P\), then

\[
\mathcal A_F\sim_M C_0(P)\rtimes_r\Gamma.
\tag{16.28}
\]

For amenable \(\Gamma\), the right side may also be written as the full crossed product.

**Proof.** A horizontal leafwise path lifts to a path in \(\widetilde B\times\{x\}\). If both endpoints lie in \(j(P)\), its lifted endpoint has the form \((\gamma^{-1}b_0,x)\) for a unique deck label. Applying \(\gamma\) identifies that endpoint with \((b_0,\rho(\gamma)x)\). The transverse transport is precisely \(\rho(\gamma)\) near \(x\). Every \(\gamma\) occurs, because the universal cover is path connected. Paths with the same endpoints are holonomy equivalent exactly when these transverse germs agree. Thus the reduction has exactly the arrows (16.25), with the stated multiplication.

For topology, a fixed path is covered by a finite chain of covering boxes. Nearby horizontal paths in that chain carry the same deck label, and their transverse transports vary on an open domain of \(P\). This is the germ chart just described. Conversely every such germ chart can be obtained by shrinking the transverse domain along the fixed path. The bijection is therefore an isomorphism of étale groupoids. Apply Theorem 16.2 to get (16.26).

The transformation groupoid maps onto the germ groupoid by sending a labelled arrow to its germ. Its charts map homeomorphically to germ charts. If two labels \(\gamma,\delta\) have the same germ at \(x\), then \(\rho(\delta^{-1}\gamma)\) has identity germ at \(x\); (16.27) makes the labels equal. The map is thus a bijective local homeomorphism and a groupoid isomorphism. The discrete case of Theorem 14.3 identifies its reduced algebra with the reduced crossed product, giving (16.28). Lesson 4 proves the amenable assertion. \(\square\)

Condition (16.27) allows nontrivial stabilizers with nontrivial germs. It is stronger than a globally faithful action: a nonidentity smooth diffeomorphism can be the identity on an open set. For example, take the time-one map of a nonzero smooth vector field supported in a proper interval of the circle. It has infinite order, since a point where the field is nonzero moves strictly monotonically until it approaches an endpoint. Its powers give a faithful \(\mathbb Z\)-action, but every power has identity germ outside that interval. Such arrows collapse in the holonomy reduction. Even more directly, a trivial action gives \(M=B\times P\), so the connected-fibre result gives \(\mathcal A_F\sim_M C_0(P)\), rather than the generally larger algebra \(C_0(P)\rtimes\Gamma\).

For a circle diffeomorphism \(\varphi\), the suspension convention is

\[
\Sigma_\varphi=(\mathbb R\times\mathbb T)/
\bigl((t+1,x)\sim(t,\varphi x)\bigr).
\tag{16.29}
\]

Its return action is \(n:x\mapsto\varphi^n x\). The condition for (16.28) is that no nonzero iterate is the identity on any neighbourhood of any point. When it holds, let \(A=C(\mathbb T)\) and \(\alpha(a)=a\circ\varphi^{-1}\). The two PV cycles of (15.39) imply

\[
0\longrightarrow
\operatorname{coker}(1-\alpha_*|K_i(A))
\longrightarrow K_i(\mathcal A_F)
\longrightarrow
\ker(1-\alpha_*|K_{i-1}(A))
\longrightarrow0.
\tag{16.30}
\]

This follows by exactness at the crossed-product group in that cycle and the Morita isomorphism, so no splitting has been assumed. On \(K_0(C(\mathbb T))=\mathbb Z[1]\), \(\alpha_*\) is the identity. On \(K_1(C(\mathbb T))=\mathbb Z[v]\), it is multiplication by \(\deg\varphi\): the composed unitary has that winding number, with inverse degree equal to the same sign. Hence an orientation preserving diffeomorphism satisfying the germ condition gives

\[
K_0(\mathcal A_F)\cong\mathbb Z^2,\qquad
K_1(\mathcal A_F)\cong\mathbb Z^2.
\tag{16.31}
\]

Each short exact sequence splits because its quotient is free: lift a generator and extend by integer multiples. An orientation reversing diffeomorphism satisfying the same germ condition instead gives

\[
K_0(\mathcal A_F)\cong\mathbb Z,\qquad
K_1(\mathcal A_F)\cong\mathbb Z\oplus\mathbb Z/2.
\tag{16.32}
\]

For (16.32), the maps on \(K_0,K_1\) are respectively zero and multiplication by two. The even sequence has cokernel \(\mathbb Z\) and kernel zero; the odd sequence has cokernel \(\mathbb Z/2\) and quotient \(\mathbb Z\), which splits. An involution such as reflection fails the germ condition, since its square is the identity. Formula (16.32) still computes its action algebra, but cannot be assigned to its foliation algebra through (16.28).

## The Kronecker foliation

Take \(\varphi(x)=x+\theta\) on \(\mathbb T\), with irrational \(\theta\). The homeomorphism, in fact diffeomorphism,

\[
[t,x]\longmapsto(t\bmod1,\ x+\theta t\bmod1)
\tag{16.33}
\]

identifies its suspension with the torus carrying the flow

\[
s\cdot(a,b)=(a+s,b+\theta s).
\tag{16.34}
\]

The formula descends because \([t+1,x]=[t,x+\theta]\). Its inverse is obtained locally by lifting the first circle coordinate; changing that lift changes \(x\) by exactly the suspension relation.

Irrationality makes the flow free: a return requires \(s\in\mathbb Z\) and \(\theta s\in\mathbb Z\), hence \(s=0\). Every leaf is an injectively immersed copy of \(\mathbb R\) and has trivial holonomy. Between two points of a leaf there is exactly one flow parameter and one holonomy arrow. Locally their coordinates agree with the flow-box arrow charts, so this bijection is a smooth groupoid isomorphism \(G\cong\mathbb T^2\rtimes\mathbb R\).

The transversal \(\{0\}\times\mathbb T\) has integer returns, acting by \(x\mapsto x+n\theta\). Every nonzero such rotation has no fixed point, so (16.27) holds. Theorem 16.2, or the explicit equivalence in Lesson 15, therefore gives

\[
\mathcal A_{F_\theta}
\cong C(\mathbb T^2)\rtimes\mathbb R
\sim_M A_\theta,\qquad
A_\theta=C(\mathbb T)\rtimes_\alpha\mathbb Z.
\tag{16.35}
\]

Both acting groups are amenable, so full and reduced crossed products coincide. With \(v(x)=e^{2\pi ix}\) and \(u\) implementing \(\alpha\), our conventions are

\[
uvu^*=e^{-2\pi i\theta}v,
\qquad vu=e^{2\pi i\theta}uv.
\tag{16.36}
\]

Rotation is homotopic to the identity by \(x\mapsto x+s\theta\). Both PV maps \(1-\alpha_*\) vanish, and (16.30) proves, in each parity,

\[
K_0(\mathcal A_{F_\theta})\cong K_0(A_\theta)\cong\mathbb Z^2,
\qquad
K_1(\mathcal A_{F_\theta})\cong K_1(A_\theta)\cong\mathbb Z^2.
\tag{16.37}
\]

This proves the K-groups without importing a computation of the rotation algebra. It agrees with the Thom calculation in Lesson 11: split circle evaluation and Bott periodicity give \(K_0(C(\mathbb T^2))=K_1(C(\mathbb T^2))=\mathbb Z^2\), and the flow shifts parity once.

For contrast, let \(\theta=m/n\) in lowest terms, \(n>0\). The primitive character

\[
(a,b)\longmapsto nb-ma\bmod1
\tag{16.38}
\]

is a submersion onto the circle with connected circle fibres, which are the leaves. Proposition 16.3 gives the foliation algebra Morita equivalent to \(C(\mathbb T)\), so each K-group is \(\mathbb Z\). The flow has period \(n\), and its transformation groupoid retains this isotropy. Its algebra still has both K-groups \(\mathbb Z^2\) by Thom, or by Lesson 15's suspension equivalence. Thus (16.35), with the flow identified as the holonomy groupoid, genuinely needs the irrationality assumption. Lesson 15's equivalence of **transformation** groupoids works for all \(\theta\).

## The Reeb foliation of the three-sphere

We compute this example by an extension, rather than assuming an assembly comparison. First fix the usual two-component Reeb model. In a solid torus \(D^2\times\mathbb T\), use polar disk coordinates \((r,\phi)\) and longitudinal angle \(\theta\in\mathbb R/2\pi\mathbb Z\). In its interior the leaves are
\[
 \theta=H(r)+c\pmod{2\pi},
 \tag{16A.1}
\]
where \(H(r)=r^2\) near zero, is strictly increasing for \(r>0\), and tends to infinity as \(r\uparrow1\). Choose \(1/H'(r)\) smooth and flat at the boundary. The defining form \(d\theta-dH\) is smooth at the disk centre; near the boundary its equivalent form \(dr-(1/H')d\theta\) extends smoothly and is nonzero there. The boundary torus is a leaf. Each interior leaf is parametrized by the open disk through (16A.1), so is a plane.

Glue two such solid tori by the usual three-sphere Heegaard gluing, which interchanges meridian and longitude, reversing one orientation. The flat boundary terms make the foliations fit smoothly. A short transverse arc across the common torus is complete: for every \(c\), the equation \(H(r)=\theta_0-c+2\pi k\) gives intersections arbitrarily close to the boundary. On one side, a longitudinal return contracts that arc, and a meridional return is the identity germ. On the other side the roles interchange. The torus leaf's two generators therefore have independent one-sided holonomy. Each nonzero pair of powers changes at least one side, so its holonomy representation is injective and its holonomy cover is \(\mathbb R^2\). The other leaves have trivial holonomy and plane covers.

More explicitly, the return replaces \(H(r)\) by \(H(r)+2\pi\). A transverse coordinate proportional to \(\exp(-H(r)\log2/(2\pi))\) conjugates it to multiplication by \(1/2\). Use that coordinate on each side, with opposite signs. Thus the holonomy pseudogroup on the arc is the restriction of the pseudogroup on \(\mathbb R\) generated by
\[
 h_+(x)=\begin{cases}x/2&x>0,\\x&x\leq0,\end{cases}
 \qquad
 h_-(x)=\begin{cases}x&x\geq0,\\x/2&x<0.\end{cases}
 \tag{16A.2}
\]
These are homeomorphisms; the transverse conjugacy need not be smooth. It preserves the topological germ groupoid and its counting convolution algebra. At positive points the germ of \(h_-\) is identity, at negative points that of \(h_+\) is identity, and at zero no nontrivial pair of powers has identity germ. The description is exhaustive: on an interior plane any two endpoint paths have the same holonomy, and its successive intersections with the arc are exactly the integer returns above; on the torus, loops are precisely its meridian and longitude powers. Plaque-path neighborhoods give the corresponding germ charts.

Let \(\mathcal H\) be this germ groupoid on \(\mathbb R\). The small arc is an open full reduction, since every nonzero contraction orbit meets it. The transversal equivalence of Proposition 16.2 and the open-full reduction of Lesson 15 identify the reduced Reeb algebra up to Morita equivalence with \(C_r^*(\mathcal H)\). Both groupoids have their explicit smooth or counting Haar systems; no Hausdorff claim for the arrow space is needed.

We now identify both norms and the required extension. Let
\[
 B=C_0(\mathbb R)\rtimes\mathbb Z^2,
 \tag{16A.3}
\]
for the commuting actions (16A.2), and denote its canonical multiplier unitaries by \(U_+,U_-\). Let \(J\) be the closed ideal generated by
\[
 a(U_--1)\ (a\in C_0(\mathbb R_+)),\qquad
 b(U_+-1)\ (b\in C_0(\mathbb R_-)).
 \tag{16A.4}
\]
The quotient \(A=B/J\) is the full algebra of \(\mathcal H\). Here is a verification of that assertion and its norm, including the non-Hausdorff issue. A finite crossed-product kernel maps to the sum of its germ-bisection kernels. At \(x>0\), coefficients with equal \(U_+\)-power are added; at \(x<0\), coefficients with equal \(U_-\)-power are added; at zero all pairs of powers remain distinct. These are exactly the germ relations. Every compact patch kernel is a finite sum of such kernels, so this map is onto the patch algebra. Its nullspace is generated by (16A.4), after approximation: coefficients vanishing at zero can be cut off near zero in the crossed-product norm, and on each remaining half-line a finite sum with zero sum in the inactive power is a sum of multiples of \(U_\mp-1\).

Passing from action kernels to germ kernels decreases the \(I\)-norm, by adding coefficients and applying the triangle inequality. Consequently every full germ representation pulls back to a representation of \(B\) vanishing on \(J\). Conversely a representation of \(A\) splits into the reducing essential subspaces of its two orthogonal open-half-line ideals and their orthogonal complement. On the positive subspace \(U_-=1\); the algebra is the crossed product for the free proper \(h_+\)-action. Its full equals reduced norm, by amenability of \(\mathbb Z\), and its regular kernel uses the summed positive germ coefficients, so the Schur bound is the germ \(I\)-norm. Compact half-line cutoffs prove the same bound for kernels reaching zero, by strong convergence in this essential subspace. The negative subspace has the identical argument. On the remaining subspace the representation factors through \(C^*(\mathbb Z^2)\); its norm is bounded by the sum of the absolute coefficients at zero, again the germ \(I\)-norm. This proves the reverse universal bound and hence \(A=C^*(\mathcal H)\).

Full crossed-product exactness and the relations give the exact sequence
\[
 0\longrightarrow I_+\oplus I_-\longrightarrow A
      \longrightarrow C^*(\mathbb Z^2)=C(\mathbb T^2)\longrightarrow0,
 \quad I_\pm=C_0(\mathbb R_\pm)\rtimes\mathbb Z.
 \tag{16A.5}
\]
Indeed the unit-zero quotient of \(B\) is the group algebra, and every generator of \(J\) lies in an open-half-line ideal. Within the positive ideal, imposing \(U_-=1\) gives exactly the single-generator crossed product by its universal relations, and similarly on the negative side. The half-line ideals remain orthogonal.

This full algebra also equals its reduced algebra. The zero regular representation is the left regular representation of \(\mathbb Z^2\), faithful on \(C^*(\mathbb Z^2)\) by abelian amenability. If an element has zero reduced norm, its quotient in (16A.5) is therefore zero, so it lies in \(I_+\oplus I_-\). The positive and negative regular representations are faithful on these ideals, again by \(\mathbb Z\)-amenability. The element is zero. This proves injectivity of the full-to-reduced map without assuming general reduced invariant-ideal exactness.

The logarithmic coordinate changes each half-line action to integer translation on \(\mathbb R\). Its quotient is a circle, so the proper-action equivalence of Lesson 15 and written Morita K-invariance give
\[
 K_0(I_\pm)=\mathbb Z,\qquad K_1(I_\pm)=\mathbb Z.
 \tag{16A.6}
\]
It remains to compute the two boundary maps; knowing only the ideal and quotient groups would not determine the answer.

Consider the one-sided extension
\[
 0\to I_+\to E_+=C_0([0,\infty))\rtimes_{h_+}\mathbb Z
          \to C(\mathbb T)\to0.
 \tag{16A.7}
\]
The coefficient algebra is a cone: \(x\mapsto e^{-x}\) identifies it with \(C_0((0,1])\). Extend a cone function by zero at zero; \((H_sF)(y)=F(sy)\), for \(0\leq s\leq1\), contracts identity to zero, with point-norm continuity by uniform continuity on \([0,1]\). Its two K-groups therefore vanish. The PV cycle makes both K-groups of \(E_+\) vanish. Exactness of (16A.7) now says that both boundary maps are isomorphisms. Thus the unit in \(K_0(C(\mathbb T))\) maps to a generator of \(K_1(I_+)\), and the coordinate unitary in \(K_1(C(\mathbb T))\) maps to a generator of \(K_0(I_+)\). Choose those images as the generators, avoiding any implicit orientation sign. The negative half-line has the same conclusion for \(E_-\).

Collapse \(U_-\) to one and restrict coefficients to \(0,\infty)\). This gives a map from (16A.5) to (16A.7), identity on \(I_+\), zero on \(I_-\), and evaluation of the second torus coordinate at one on the quotient. It is well defined because it kills both families (16A.4). There is the corresponding map to \(E_-\), evaluating the first coordinate at one. Naturality of the six-term cycle consequently determines the two components of each boundary map.

Use the written circle-with-coefficients decomposition [Topological K-theory of spaces, pairs and vector bundles, Theorem 5.1 and Corollary 5.2. The quotient groups have bases
\[
 K_0(C(\mathbb T^2))=\mathbb Z[1]\oplus\mathbb Z\beta,
 \qquad K_1(C(\mathbb T^2))=\mathbb Z[u_+]\oplus\mathbb Z[u_-].
 \tag{16A.8}
\]
Here \(\beta\) is the reduced two-circle Bott class. Either coordinate evaluation kills \(\beta\); it keeps its corresponding coordinate unitary and kills the other. In the generators just chosen, naturality gives
\[
 \begin{aligned}
 \partial_0(a[1]+b\beta)&=(a,a),\\
 \partial_1(c[u_+]+d[u_-])&=(c,d).
 \end{aligned}
 \tag{16A.9}
\]
An inverse choice of a geometric circle generator changes its row sign; neither kernel nor cokernel changes. The second map is an isomorphism. Thus exactness identifies \(K_0(A)\) with \(\ker\partial_0=\mathbb Z\beta\), and \(K_1(A)\) with \(\operatorname{coker}\partial_0=\mathbb Z^2/\mathbb Z(1,1)\). Both groups are \(\mathbb Z\). Morita invariance and the proved equality of norms give
\[
 K_0(\mathcal A_{\mathrm{Reeb}})\cong\mathbb Z,\qquad
 K_1(\mathcal A_{\mathrm{Reeb}})\cong\mathbb Z.
 \tag{16.39}
\]
The extension approach is due to Torpe [1985]. The geometric facts agree with [Kordyukov, Examples 2.6 and 2.14]; [Macho-Stadler, §8, p. 646, item (3)] describes the related assembly comparison. The computation here supplies the germ model, its quotient relations, equality of norms and both boundary maps, and uses no assembly isomorphism.

## Exercises with solutions

**Exercise 1.** Determine the holonomy groupoid and reduced algebra of the product foliation on \(B\times P\), first for connected \(P\), then for arbitrary \(P\). Identify the K-groups.

**Solution.** Leaves are \(\{b\}\times P_j\), where the \(P_j\) are the connected components of \(P\). In a product chart the transverse coordinate is \(b\), so every leafwise loop has trivial holonomy. Hence there is one arrow between two points precisely when they have the same \(b\) and belong to the same component. The topology is the product fibre-pair topology from the arrow charts.

For connected \(P\), Proposition 16.4 with the fixed product density identifies the algebra with \(C_0(B)\otimes\mathcal K(L^2(P))\). Its K-groups are \(K_i(C_0(B))\) by Morita invariance, even when \(P\) is a point.

In general, a manifold's components are open and, by second countability, at most countably many. The groupoid is the disjoint union

\[
\coprod_j B\times(P_j\times P_j).
\tag{16.40}
\]

A compact subset of this disjoint union meets only finitely many components, since the components form an open cover. The convolution core is therefore the algebraic direct sum of the component cores. Its reduced norm is the supremum of their norms: every source fibre lies in just one component. Completion gives the \(c_0\)-direct sum of their algebras. K-theory continuity on increasing finite sums gives \(\bigoplus_j K_i(C_0(B))\). This also proves directly why replacing all components by the single fibre-pair groupoid changes the answer.

**Exercise 2.** Prove the submersion Morita equivalence using its module, and explain precisely what is needed for an isomorphism with \(C_0(B)\otimes\mathcal K\).

**Solution.** Take the full module \(E_p\) of (16.14). Inner products are continuous and vanish at infinity by submersion coordinates and compact support. For every \(b\) a bump on \(V_b\) has positive squared integral, so its inner-product ideal is \(C_0(B)\). The completed left action of the fibre-pair groupoid has the rank kernels (16.15) acting as rank operators. Proposition 16.4 identifies its algebra with all of \(\mathcal K(E_p)\), and not merely with a subalgebra of adjointable operators.

Thus \(E_p\), with its left inner product supplied by the rank kernels, is an imprimitivity module. Indeed the identity
\(\Theta_{\xi,\eta}\zeta=\xi\langle\eta,\zeta\rangle\)
is its compatibility identity, adjoints exchange \(\xi,\eta\), and rank operators span the compact operators. It gives the Morita equivalence. A global Hilbert \(C_0(B)\)-module unitary \(E_p\cong C_0(B)\otimes\ell^2\) carries each rank operator to the corresponding rank operator on the trivial module, and therefore yields the requested tensor isomorphism. Without that extra identification the proved conclusion remains \(\mathcal K(E_p)\) and Morita equivalence. If the trivialized fibre Hilbert space is finite dimensional, use its actual matrix algebra instead of \(\mathcal K(\ell^2)\).

**Exercise 3.** Compute both K-groups for the horizontal foliation of the suspension of an irrational rotation, checking the transversal and the rotation convention.

**Solution.** Use (16.29) with \(\varphi(x)=x+\theta\), \(\theta\notin\mathbb Q\). Every leaf meets \([0,\mathbb T]\): move horizontally from \([t,x]\) by \(-t\). Its return arrows have integer times \(n\), giving \(x\mapsto x+n\theta\). Since such a rotation has no fixed point for \(n\ne0\), none has identity germ. Proposition 16.6 and Theorem 16.2 give Morita equivalence with \(A_\theta\). The coefficient action sends \(v\) to \(e^{-2\pi i\theta}v\); covariance gives (16.36).

The circle has \(K_0=\mathbb Z[1]\) and \(K_1=\mathbb Z[v]\), and rotation induces the identity on both by its explicit rotation homotopy. Each PV sequence is \(0\to\mathbb Z\to K_i(A_\theta)\to\mathbb Z\to0\). Choose a lift of the quotient generator; its integer multiples split the quotient, proving \(K_i(A_\theta)\cong\mathbb Z^2\). Morita invariance gives this group for the foliation algebra separately at \(i=0,1\).

**Exercise 4.** Give a locally free action whose transformation groupoid differs from the orbit foliation's holonomy groupoid. Compare their algebras and K-groups, and decide whether full versus reduced completion explains the difference.

**Solution.** Let \(\mathbb R\) rotate \(\mathbb T\) at unit speed. Its stabilizer at each point is the discrete subgroup \(\mathbb Z\), so the action is locally free. The foliation has a single connected leaf, whose holonomy is trivial: its transversal is a point, so every loop has the identity germ. Its holonomy groupoid is the pair groupoid and its algebra is \(\mathcal K(L^2(\mathbb T))\), with K-groups \(\mathbb Z,0\). The action groupoid instead has isotropy \(\mathbb Z\). By Green's theorem its algebra is Morita equivalent to \(C^*(\mathbb Z)=C(\mathbb T)\), with K-groups \(\mathbb Z,\mathbb Z\). These algebras cannot be Morita equivalent since their odd K-groups differ. The real group is amenable, so the action's two completions agree. The pair groupoid's completions also agree by Proposition 16.4 with base a point. The difference is therefore already in which arrows are retained.

## What this lesson does not prove

The holonomy construction, its chart and covering theorem, and its intrinsic half-density kernels are recalled from *The C*-algebra of a foliation*, Lemma 1.1, Lemma 2.1, Theorem 2.2, §3 and Definition 4.1. They are also described in [Connes]. Lemma 16.1 proves the scalar Haar and regular-norm comparison needed to apply this course's equivalence theorem. The analytic theorem and its Hilbert-module corner prerequisites are proved or exactly imported in Lesson 15.

Morita invariance uses the exact written programme lesson linked above. Ordinary Bott periodicity and the circle K-groups are the written operator K-theory prerequisites identified in Lesson 11. We use that lesson's proved Thom isomorphisms and the PV cycle from Lesson 15, whose canonical coefficient maps are proved in *The Pimsner–Voiculescu exact sequence*, Lemma 2.1 and equation (2.9). No stable-isomorphism theorem is needed to deduce a tensor-product description from a Morita equivalence.

The Reeb example is proved by its complete transversal, the germ quotient of the two-contraction crossed product, and the exact one-sided boundary calculations. It uses the written torus generators in *Topological K-theory of spaces, pairs and vector bundles*, Theorem 5.1 and Corollary 5.2, together with the natural six-term cycle. No assembly comparison enters this calculation.

## References

- *The C*-algebra of a foliation*, in *Foliations and their operator algebras*, §§1–4.
- A. Connes, *A survey of foliations and operator algebras*, Proceedings of Symposia in Pure Mathematics 38, Part I, 1982, pp. 521–628, §§5–6, 8–10. These sections give the reduced algebra, non-Hausdorff kernels, transversal modules and the geometric/index viewpoint.
- A. Connes, [*Noncommutative Geometry*](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf), 1994, Chapter II, §8, pp. 123–128.
- Y. Li, [*Groupoid C*-algebras*](https://ncg-leiden.github.io/groupoid2022/groupoid_notes.pdf), version 7 February 2024, §5.1.1, p. 23. For the Kronecker example, the precise equivalence and integer returns are proved in Lesson 15 and used here.
- B. Blackadar, *K-Theory for Operator Algebras*, second edition, 1998, Exercise 10.11.6 and its remark, pp. 87–88, for crossed products and the foliation application. [Author's second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- Y. A. Kordyukov, [*Noncommutative geometry of foliations*](https://arxiv.org/pdf/math/0504095), arXiv:math/0504095v2, 2006, Examples 2.6 and 2.14, pp. 5–6 and 10.
- M. Macho-Stadler, [*Foliations, groupoids and Baum–Connes conjecture*](https://www.ehu.eus/~mtwmastm/JMS.pdf), Journal of Mathematical Sciences 113, 2003, pp. 637–646, §8, p. 646. It records the classifying and Reeb assembly comparison for context; the calculation here uses the explicit extension.
- A. M. Torpe, [*K-theory for the leaf space of foliations by Reeb components*](https://doi.org/10.1016/0022-1236(85)90038-2), Journal of Functional Analysis 61, 1985, pp. 15–71. Original source for the Reeb extension calculation; the model and both boundary maps are proved here.
- J. Rosenberg, *Examples and applications of noncommutative geometry and K-theory*, in *Topics in Noncommutative Geometry*, 2012, §§1.1–1.3 and §2.5, pp. 94–99 and 108; exact general K-theory prerequisites as in Lessons 11 and 15. [Electronic volume](https://www.claymath.org/wp-content/uploads/2022/03/cmip016c.pdf).

- *Topological K-theory of spaces, pairs and vector bundles*, Theorem 5.1 and Corollary 5.2, including the two-torus generators and their coordinate evaluations.
