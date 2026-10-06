# The tangent groupoid and deformation to the normal cone

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A pair of nearby points records a displacement. Dividing that displacement by a parameter \(t\) makes its limit a tangent vector. The tangent groupoid organizes this limit so that composition of pairs becomes addition of vectors. Its operator algebra consequently has compact operators at \(t>0\) and functions on the cotangent bundle at \(t=0\). Evaluation at the two ends will give a map from symbol classes to integers.

Let \(M\) be a nonempty, Hausdorff, second countable smooth manifold of pure dimension \(n\), without boundary. Compactness is unnecessary for the groupoid and its algebra below. It will be required in the comparison with classical elliptic operators. The parameter space is \([0,1]\), so the groupoid itself has boundary at its parameter ends.

We use the groupoid conventions and the full invariant-ideal exactness of *Groupoid C*-algebras: full and reduced*. Choose a positive smooth density \(\mu\) on \(M\). A Riemannian metric, smooth cutoffs, coordinate changes, and the inverse function theorem are differential-geometric prerequisites. The final Bott exercise uses the exact oscillator and compactified-symbol results in *The Bott operator, suspension, and reduction of the index to Euclidean space*.

## Rescaling the diagonal

The normal space of the diagonal at \((x,x)\) is
\[
 \frac{T_xM\oplus T_xM}{\{(v,v):v\in T_xM\}}
       \longrightarrow T_xM,\qquad [(v,w)]\longmapsto v-w.
 \tag{17.1}
\]
The displayed map is an isomorphism: it is onto, and its kernel is exactly the diagonal subspace. This fixes the sign of the tangent coordinate.

Form the set
\[
 \mathbb T M=(M\times M\times(0,1])\ \sqcup\ (TM\times\{0\}).
 \tag{17.2}
\]
Here \(\mathbb T M\) denotes the tangent groupoid, while \(TM\) denotes the ordinary tangent bundle. Take a coordinate map \(q:U\to O\subseteq\mathbb R^n\). For \(X\in O\), \(V\in\mathbb R^n\) and sufficiently small \(t\geq0\), use
\[
\begin{aligned}
 \Psi_q(X,V,t)
   &=(q^{-1}X,q^{-1}(X-tV),t),&&t>0,\\
 \Psi_q(X,V,0)
   &=(q^{-1}X,d(q^{-1})_X V,0).
\end{aligned}
 \tag{17.3}
\]
The chart domain requires \(X-tV\in O\); near a prescribed \((X,V,0)\) it is an open neighborhood in the parameter half-space. At \(t>0\) its inverse is \(X=q(x)\), \(V=(q(x)-q(y))/t\). Together with the ordinary charts on \(M\times M\times(0,1]\), these maps specify the topology.

**Lemma 17.1.** The charts (17.3) give \(\mathbb T M\) a Hausdorff, second countable smooth structure, independent of the coordinates.

**Proof.** On an overlap write \(h=q'\circ q^{-1}\). The transition in the displacement variable is
\[
 \frac{h(X)-h(X-tV)}t
    =\int_0^1 Dh(X-stV)V\,ds.
 \tag{17.4}
\]
For the local transition calculation choose a ball with closure in the overlap and shrink the domain so the segment lies there. The right side is smooth through \(t=0\), where it equals \(Dh(X)V\). The inverse transition has the same form with \(h^{-1}\). Thus these are compatible smooth charts.

The maps recording \(t,x,y\), with \(y=x\) at \(t=0\), are continuous. Points with different parameter or base coordinates can therefore be separated in Hausdorff spaces. Two distinct boundary vectors at the same \(x\) lie in a common chart (17.3), with disjoint neighborhoods in its \(V\)-coordinate. This separates all remaining distinct points. A countable manifold atlas and countably many bounded coordinate balls in \(X,V,t\), together with the ordinary positive-parameter atlas, give a countable base. ∎

In these charts, approaching a boundary vector means
\[
 t_j\to0,\qquad x_j,y_j\to x,\qquad
       \frac{q(x_j)-q(y_j)}{t_j}\to dq_x(v).
 \tag{17.5}
\]
Equation (17.4) proves that this condition is intrinsic. This is the deformation to the normal cone of the diagonal: the diagonal is replaced at parameter zero by its normal bundle (17.1). More generally, in coordinates \((u,w)\) where a closed embedded submanifold is \(w=0\), the normal rescaling is \((u,v,t)\mapsto(u,tv,t)\) for \(t>0\), with \((u,v)\) at zero. The divided difference in its coordinate transitions extends by the same integral formula.

A Riemannian metric provides the alternative local expression
\[
 (x,v,t)\longmapsto (x,\exp_x(-tv),t),\qquad t>0.
 \tag{17.6}
\]
This is used on a neighborhood of a particular boundary vector. The inverse function theorem and the Taylor formula for the exponential show that (17.6) has the transition (17.4) with derivative equal to the identity at zero. Thus it yields the same smooth structure. There is no claim that the exponential gives an injective chart on all of \(TM\) for one positive parameter.

## The groupoid and its Haar system

The unit space is \(M\times[0,1]\). At positive parameter the structure is the pair groupoid; at zero each tangent space is an additive group:
\[
\begin{aligned}
 r(x,y,t)&=(x,t),&s(x,y,t)&=(y,t),\\
 (x,y,t)(y,z,t)&=(x,z,t),&
 (x,y,t)^{-1}&=(y,x,t),\\
 r(x,v,0)&=s(x,v,0)=(x,0),\\
 (x,v,0)(x,w,0)&=(x,v+w,0),&
 (x,v,0)^{-1}&=(x,-v,0).
\end{aligned}
 \tag{17.7}
\]
Arrows with different parameter values do not compose. The unit at positive \(t\) is \((x,x,t)\); at zero it is \((x,0,0)\).

**Proposition 17.2.** These operations make \(\mathbb T M\) a Lie groupoid with parameter boundary.

**Proof.** In (17.3) the two maps to units are
\[
 r(X,V,t)=(X,t),\qquad s(X,V,t)=(X-tV,t).
 \tag{17.8}
\]
Both are submersions, including at zero: their differentials in \(X,t\) have full rank. The same coordinates give
\[
\begin{aligned}
 (X,V,t)(X-tV,W,t)&=(X,V+W,t),\\
 (X,V,t)^{-1}&=(X-tV,-V,t).
\end{aligned}
 \tag{17.9}
\]
Thus multiplication on the manifold of composable pairs, inversion, and the zero-displacement unit map are smooth. Around a composable pair at zero one can choose a single base chart and bounded neighborhoods of both vectors and their sum; for small \(t\), all three points stay in that chart. Around positive-parameter arrows the ordinary pair-groupoid formulas suffice. Associativity and the unit and inverse identities hold separately on each parameter fiber, hence globally. ∎

For \(M=\mathbb R^n\), the coordinates \((X,V,t)\) are global. The positive-parameter pair \((x,y)\) corresponds to \(X=x,V=(x-y)/t\), and (17.9) becomes addition of displacements. Equivalently, \(\mathbb T\mathbb R^n\) is the transformation groupoid for the action
\[
 a\cdot(X,t)=(X+ta,t)
       \quad\text{of }\mathbb R^n\text{ on }\mathbb R^n\times[0,1].
 \tag{17.10}
\]
An arrow with range \(X\) has source \(X-ta\); take \(a=V\). At zero the action is trivial, so its isotropy is the whole additive tangent space.

The density \(\mu\) gives a translation-invariant density \(\mu_x^{\mathrm{lin}}\) on the vector space \(T_xM\). Define a left Haar system by
\[
\begin{aligned}
 \int f\,d\lambda^{(x,t)}
    &=t^{-n}\int_M f(x,y,t)\,d\mu(y),&&t>0,\\
 \int f\,d\lambda^{(x,0)}
    &=\int_{T_xM}f(x,v,0)\,d\mu_x^{\mathrm{lin}}(v).
\end{aligned}
 \tag{17.11}
\]

**Lemma 17.3.** This is a full-support continuous Haar system.

**Proof.** Left multiplication at positive parameter changes the first coordinate of \((y,z,t)\) and leaves \(z\) unchanged; the density in (17.11) is unchanged. At zero left multiplication translates \(v\), which preserves \(\mu_x^{\mathrm{lin}}\). Positivity of the density gives full support on every range fiber.

Write \(d\mu=m(X)dX\) in a chart. On the range fiber, substituting \(q(y)=X-tV\) gives
\[
 t^{-n}d\mu(y)=m(X-tV)\,dV
       \longrightarrow m(X)\,dV.
 \tag{17.12}
\]
For a continuous compactly supported function in a chart (17.3), the integrand has a fixed compact set of \(V\)'s locally in \(X,t\). Dominated convergence proves continuity at zero. At positive parameter ordinary compact integration proves it. Cover any compact support by finitely many such charts and positive-parameter charts and split the function with a compactly supported partition of unity. Summing proves the required continuity for every \(f\in C_c(\mathbb T M)\). ∎

The factor \(t^{-n}\) is essential: without it the substitution in (17.12) would leave \(t^n\), and the positive-parameter integrals would approach zero instead of the tangent-fiber integral.

Use this Haar system and the convolution and involution of Lesson 14 to define
\[
 \mathcal A_M=C^*(\mathbb T M).
 \tag{17.13}
\]
The smooth compactly supported scalar core is dense: smooth approximation on finitely many compact coordinate neighborhoods converges in the \(I\)-norm, because compactly supported positive envelopes have bounded Haar integrals on their compact unit supports. The full norm is bounded by the \(I\)-norm. A half-density formulation gives the same algebra after trivialization by (17.11), as in Lesson 16.

## The parameter fibers

The parameter function is constant along each arrow. Thus \(b\in C([0,1])\) acts centrally by \(f(\gamma)\mapsto b(t(\gamma))f(\gamma)\). It defines a unital homomorphism into \(ZM(\mathcal A_M)\). Let
\[
 I_t=C_0([0,1]\setminus\{t\})\mathcal A_M,\qquad
       (\mathcal A_M)_t=\mathcal A_M/I_t,
 \tag{17.14}
\]
where the first expression means the closed span of central products.

**Proposition 17.4.** Restriction to the parameter fibers identifies
\[
 (\mathcal A_M)_0\cong C_0(T^*M),\qquad
 (\mathcal A_M)_t\cong\mathcal K(L^2(M,\mu)),\quad t>0.
 \tag{17.15}
\]
Every evaluation map is onto, and \(\|a\|=\sup_{0\leq t\leq1}\|a_t\|\).

**Proof.** The units with parameter \(t\) form a closed invariant subset. Full invariant-ideal exactness from Lesson 14 identifies its quotient with the full algebra of the restricted groupoid. Its open-complement ideal is exactly \(I_t\): a compactly supported core function in that complement has parameter support bounded away from \(t\), so a central function vanishing at \(t\) and equal to one on that support fixes it. Conversely central products vanishing at \(t\) lie in the complement ideal, by approximation of such scalar functions by ones supported away from \(t\). This proves the quotient assertion and surjectivity.

At \(t>0\) the restricted groupoid is \(M\times M\). Its full and reduced algebras are the compact operators by the pair-groupoid calculation in Lesson 14. On the fixed space \(L^2(M,\mu)\) its representation is
\[
 (A_t(f)\psi)(x)=t^{-n}\int_M f(x,y,t)\psi(y)\,d\mu(y).
 \tag{17.16}
\]
The source-fiber measure is \(t^{-n}\mu\); multiplying vectors by a constant \(t^{-n/2}\) identifies its \(L^2\)-space with this fixed one and leaves formula (17.16) unchanged.

At zero the groupoid is the additive vector bundle \(TM\). We choose the geometric Fourier convention
\[
 \mathcal F_{\mathrm{geo}}f(x,\eta)
   =\int_{T_xM}e^{-i\langle\eta,v\rangle}
                   f(x,v,0)\,d\mu_x^{\mathrm{lin}}(v).
 \tag{17.17}
\]
Convolution in each vector space becomes multiplication and involution becomes complex conjugation. Its full and reduced norms coincide, since an additive vector space is amenable; its Fourier C*-norm is the supremum over \(\eta\). These facts follow from Lessons 4 and 6, applied in linear coordinates. Full group-bundle fiber detection from Lesson 14 therefore gives the norm \(\sup_{x,\eta}|\mathcal F_{\mathrm{geo}}f(x,\eta)|\).

For a smooth compactly supported \(f\), (17.17) is continuous. Integration by parts in finitely many bundle charts gives uniform decay as \(|\eta|\to\infty\) over its compact base support; it is consequently in \(C_0(T^*M)\). Such transforms form a self-adjoint algebra. They separate different base points by base cutoffs and different covectors over one point by the distinct Fourier characters on that vector space. At every covector some localized Fourier integral is nonzero. The locally compact Stone–Weierstrass theorem gives dense range. The norm equality gives closed range after completion, proving the first isomorphism of (17.15).

Finally, in every nonzero irreducible representation the unital central action of \(C([0,1])\) is scalar by Schur's lemma. Its character is evaluation at some \(t\), so the representation kills \(I_t\) and factors through that fiber. Irreducible representations detect the C*-norm. This proves the supremum formula. ∎

The Fourier choice (17.17) uses radians and a negative sign. Relative to the positive transform \(\int e^{2\pi i\xi(v)}f(v)\,dv\) used earlier for dual actions, its cotangent coordinate is
\[
 \eta=-2\pi\xi.
 \tag{17.18}
\]
This coordinate change matters when specifying an oriented Bott class. With (17.17), ordinary quantization uses \(e^{i(x-y)\cdot\eta}\), and the symbol of \(-i\partial_j\) is \(\eta_j\).

**Corollary 17.5.** The full and reduced algebras of \(\mathbb T M\) coincide.

**Proof.** Every source fiber lies at one parameter. The supremum defining the reduced norm is therefore the supremum of the reduced norms of the parameter restrictions. At positive parameters these equal the full pair-groupoid norms, and at zero they equal the full vector-bundle norm. Proposition 17.4 identifies their supremum with the full norm. Thus the canonical quotient is isometric. ∎

This argument uses exactness for the full algebra and equality on the individual fibers. It does not presume reduced exactness for arbitrary groupoids.

## Continuity at the tangent end

**Theorem 17.6.** With the evaluations in (17.15), \(\mathcal A_M\) is the section algebra of a continuous field over \([0,1]\): every function \(t\mapsto\|a_t\|\) is continuous.

**Proof.** First we prove upper semicontinuity. Fix \(t_0\) and choose \(c\in I_{t_0}\) with \(\|a+c\|<\|a_{t_0}\|+\varepsilon\), using the quotient norm. Approximate \(c\) by finite sums \(\sum h_jb_j\), with \(h_j(t_0)=0\). Their fiber norms approach zero as \(t\to t_0\); the uniform norm bound on the approximation shows \(\|c_t\|\to0\). Consequently
\[
 \limsup_{t\to t_0}\|a_t\|
       \leq\|a_{t_0}\|+\varepsilon.
 \tag{17.19}
\]
Let \(\varepsilon\to0\).

It suffices to prove the remaining continuity on the smooth compact core, since approximation in \(\mathcal A_M\) is uniform in all fiber norms. For \(t_0>0\), the kernel \(t^{-n}f(x,y,t)\) varies continuously in Hilbert–Schmidt norm near \(t_0\). Indeed its support lies in a fixed compact subset of \(M\times M\) there, and dominated convergence applies to its squared absolute value. Operator norm is bounded by Hilbert–Schmidt norm, so \(t\mapsto\|f_t\|\) is continuous at \(t_0\).

For the lower bound at zero, fix \((x_0,\eta_0)\in T^*M\), and use coordinates \(X=q(x)\), \(X_0=q(x_0)\), with \(d\mu=m(X)dX\). Let \(\chi\in C_c^\infty(\mathbb R^n)\) satisfy \(\|\chi\|_{L^2(dX)}=1\). For small \(t>0\), set
\[
 \psi_t(q^{-1}X)
   =c_t t^{-n/4}\chi\!\left(\frac{X-X_0}{\sqrt t}\right)
             e^{i\eta_0\cdot(X-X_0)/t},
 \qquad\|\psi_t\|_{L^2(\mu)}=1.
 \tag{17.20}
\]
Extend it by zero outside the coordinate chart. Its support stays inside that chart, and the normalization satisfies \(c_t\to m(X_0)^{-1/2}\).

Put \(F(X,V,t)=f(\Psi_q(X,V,t))\). On the part of the support contributing to (17.16) for this packet, \(V\) remains bounded uniformly for small \(t\). To see this, a contrary sequence of contributing arrows has a convergent subsequence in the compact support of \(f\); its parameter tends to zero and its source tends to \(x_0\). Its limit is therefore a tangent vector at \(x_0\), and (17.3) then bounds \(V\). The same argument places the ranges in the chart. Writing \(Y=(X-X_0)/\sqrt t\), substitution of (17.20) and (17.12) gives
\[
\begin{aligned}
 A_t(f)\psi_t(q^{-1}X)
 &=c_t t^{-n/4}e^{i\eta_0\cdot(X-X_0)/t}\\
 &\quad{}\times\int F(X,V,t)e^{-i\eta_0\cdot V}
                 \chi(Y-\sqrt tV)m(X-tV)\,dV.
\end{aligned}
 \tag{17.21}
\]
The integral tends uniformly on its relevant bounded \(Y\)-set to
\[
 \chi(Y)m(X_0)\int F(X_0,V,0)e^{-i\eta_0\cdot V}\,dV
    =\chi(Y)\mathcal F_{\mathrm{geo}}f(x_0,\eta_0).
 \tag{17.22}
\]
All outputs are supported in one bounded \(Y\)-set: the input support is fixed in \(Y\), and the bounded displacement adds only \(\sqrt tV\). Dominated convergence, after \(X=X_0+\sqrt tY\), therefore proves
\[
 \|A_t(f)\psi_t-\mathcal F_{\mathrm{geo}}f(x_0,\eta_0)\psi_t\|
       \longrightarrow0.
 \tag{17.23}
\]
It follows that \(\liminf_{t\downarrow0}\|f_t\|\geq
|\mathcal F_{\mathrm{geo}}f(x_0,\eta_0)|\). Taking the supremum over all covectors gives \(\liminf\|f_t\|\geq\|f_0\|\). Together with (17.19), this proves continuity at zero. For dimension zero the same calculation uses the normalized point vector at \(x_0\); compact support near that boundary unit excludes off-diagonal arrows at small \(t\). Approximation extends continuity to every \(a\). Proposition 17.4 supplies full fibers and the supremum norm, and the central action supplies multiplication by scalar sections. These are the continuous-field properties. ∎

## The deformation index

**Theorem 17.7.** There is an exact sequence
\[
 0\longrightarrow C_0((0,1])\otimes\mathcal K(L^2(M,\mu))
   \longrightarrow\mathcal A_M
   \xrightarrow{\mathrm{ev}_0} C_0(T^*M)
   \longrightarrow0.
 \tag{17.24}
\]
Its ideal is contractible. Consequently \((\mathrm{ev}_0)_*\) is an isomorphism on both K-groups.

**Proof.** Full invariant-ideal exactness identifies the kernel with the algebra of \(M\times M\times(0,1]\). Its compactly supported kernels represent the continuous compact-operator functions on \((0,1]\) by (17.16). Finite sums of a scalar parameter function times a compactly supported rank-one kernel are dense on every compact parameter interval, by kernel approximation and partitions of unity. The fiber supremum norm proves that the completed ideal is \(C_0((0,1],\mathcal K)\). Equivalently this is the spatial tensor product in (17.24). Surjectivity and the zero fiber were proved in Proposition 17.4.

Extend \(F\in C_0((0,1],\mathcal K)\) by \(F(0)=0\). For \(0\leq s\leq1\), define
\[
 (H_sF)(t)=F(st).
 \tag{17.25}
\]
Each \(H_s\) is a *-homomorphism and a contraction. At \(s=0\) it is zero; at \(s=1\) it is identity. Uniform continuity of \(F\) on \([0,1]\) proves point-norm continuity in \(s\). Thus the ideal contracts, and homotopy invariance makes its two K-groups zero. The natural six-term sequence The six-term exact sequence and the exponential map, Theorem 2.1 now makes the quotient map a K-isomorphism in both degrees. ∎

Choose the rank normalization \(K_0(\mathcal K)=\mathbb Z\), sending a rank-one projection to \(1\). The index furnished by the deformation is
\[
\begin{aligned}
 \operatorname{Ind}^{\mathrm{def}}_M
   &=(\mathrm{ev}_1)_*(\mathrm{ev}_0)_*^{-1}\\
   &:K_0(C_0(T^*M))\longrightarrow\mathbb Z.
\end{aligned}
 \tag{17.26}
\]
Here \(K_0(C_0(T^*M))=K_c^0(T^*M)\) uses compact supports on the total cotangent space. The analogous odd map has zero target, since \(K_1(\mathcal K)=0\). Although the ideal is contractible, the algebra \(\mathcal A_M\) need not be: it has the K-theory of the cotangent bundle.

The interval in (17.24) contains \(1\). Replacing it by \((0,1)\) would give a suspension ideal, whose K-theory generally does not vanish. The contraction (17.25) also imposes no covariance condition; it is used on this ordinary ideal, with its already established trivialization.

**Proposition 17.8 (Locality).** If \(U\subseteq M\) is a nonempty open submanifold, extension of compactly supported groupoid functions by zero induces an isometric homomorphism
\[
 j_{\mathcal A}:\mathcal A_U\longrightarrow\mathcal A_M.
 \tag{17.27}
\]
If \(j_0:C_0(T^*U)\to C_0(T^*M)\) is zero extension, then
\[
 \operatorname{Ind}^{\mathrm{def}}_M (j_0)_*
          =\operatorname{Ind}^{\mathrm{def}}_U.
 \tag{17.28}
\]

**Proof.** Restrict \(\mu\) to \(U\). The subgroupoid \(\mathbb T U\) is the open restriction to \(U\times[0,1]\). Zero extension preserves convolution: a nonzero product of the two extended factors has its intermediate unit in \(U\). It preserves involution as well. A compact support inside this open subgroupoid extends continuously, or smoothly for a smooth core.

At zero its Fourier transform is zero extension on \(T^*U\), hence isometric. At \(t>0\), let \(J:L^2(U,\mu)\to L^2(M,\mu)\) be extension by zero. The kernel operator becomes \(J A_t(f)J^*\), which has the same norm. Proposition 17.4 gives equality of the full norms after taking the parameter supremum. Completion proves (17.27).

The two evaluation squares commute, with maps \(j_0\) at zero and \(k\mapsto JkJ^*\) at one. The latter sends a rank-one projection to a rank-one projection, so induces identity under the two integer normalizations. For a class \(b\in K_0(C_0(T^*U))\), the class \(j_{\mathcal A*}(\mathrm{ev}_0^U)_*^{-1}b\) evaluates at zero to \(j_{0*}b\). The uniqueness in Theorem 17.7 identifies it with \((\mathrm{ev}_0^M)_*^{-1}j_{0*}b\). Evaluation at one proves (17.28). ∎

The open subset \(U\) need not be invariant under the pair groupoid. The norm proof in Proposition 17.8 establishes precisely the open-restriction inclusion used there.

## The comparison with elliptic operators

**Theorem (elliptic comparison).** If \(M\) is compact and \(D\) is a classical elliptic pseudodifferential operator between smooth complex vector bundles, then
\[
 \operatorname{Ind}^{\mathrm{def}}_M[\sigma(D)]
       =\dim\ker D-\dim\operatorname{coker}D.
 \tag{17.29}
\]

**Proof.** We construct a projection in the tangent-groupoid algebra whose two evaluations have these meanings. The analytic prerequisites are the finite-seminorm composition and adjoint theorem of [Euclidean symbol calculus, AN03-EUC-005, (E20)–(E21)], its geometric assembly [Geometric microlocal calculus, AN03-GEO-004 and AN03-GEO-006], and exact order changes and elliptic regularity Symbols, finite defects, and the index on a closed manifold, AN03-GSI-002–003. The parameter estimates needed below are supplied here.

First replace \(D\) by an operator \(A\) of positive order \(r>\dim M+1\), composing on its target with the exact order-changing isomorphism of AN03-GSI-003. This preserves kernel-minus-cokernel dimension. Its principal symbol is the old symbol multiplied by a positive scalar cotangent power, which preserves the compact-support symbol class after polar normalization. Realize \(A\) as a closed operator \(H^r(E)\to L^2(F)\). Elliptic regularity identifies its Hilbert adjoint's kernel with the smooth classical cokernel, and its range is closed.

Take finitely many charts, bundle frames and density identifications. In each localized full symbol \(a(x,\xi)\) choose a smooth cutoff \(\chi(\eta)\), zero near \(\eta=0\) and one for large \(|\eta|\), and put
\[
 a_t(x,\eta)=\chi(\eta)t^r a(x,\eta/t),\quad t>0,
 \qquad a_0(x,\eta)=\chi(\eta)\sigma_r(A)(x,\eta).
 \tag{17B.1}
\]
Assemble the quantizations with phase \(e^{i(x-y)\cdot\eta/t}\), using the fixed chart cutoffs. Denote their sum by \(A_t\). For every fixed \(t>0\), it differs from \(t^rA\) by a smoothing operator: the omitted physical frequencies lie in a bounded set, and the off-diagonal localization error is a smooth kernel. Thus every \(A_t\) is elliptic and Fredholm with the same index as \(D\).

The classical expansion of \(a\), on the region \(|\eta|\) bounded away from zero, proves that \(a_t\) is uniformly bounded in \(S^r_{1,0}\), in every fixed seminorm, and converges to \(a_0\) in those seminorms. Its successive terms have the form \(t^j\chi(\eta)a_{r-j}(x,\eta)\). The cutoff avoids any differentiability issue for a homogeneous symbol at the origin. After assembly, the boundary symbol, call it \(a_0\) again, agrees with \(\sigma_r(A)\) outside a compact cotangent disk and therefore represents the same symbol class.

Here are the uniform inversion estimates. In one chart, the product and adjoint formulas with the scaled phase read
\[
 b\mathbin{\#_t}c
   =\sum_{|\alpha|<N}\frac{t^{|\alpha|}}{\alpha!}
       (\partial_\eta^\alpha b)(D_x^\alpha c)
       +t^N R_{N,t},
 \qquad R_{N,t}\in S^{\operatorname{ord}b+\operatorname{ord}c-N},
 \tag{17B.2}
\]
with uniform finite-seminorm bounds; here \(D_x=(1/i)\partial_x\). The adjoint has the corresponding formula with \(c^*\). To check the parameter factor, apply the proof of (E20)–(E21) after the unitary change \(x=tX\). Each base derivative in its integral Taylor remainder then contributes \(t\). Differentiating the original symbols first proves the same bounds for every required remainder derivative. Their uniform symbol bounds supply the constants independently of \(t\). The coordinate-change proof and finite bundle assembly use the same Taylor expansion, so these estimates hold globally with the fixed atlas. Off-diagonal chart errors are \(O(t^N)\) for every \(N\), by integration by parts in the scaled phase.

Start with the positive matrix inverse
\(b_{0,t}=(1+a_t^*a_t)^{-1}\), of uniform order \(-2r\). The pointwise positivity controls its derivatives on bounded frequencies; ellipticity controls them at infinity. Inverting the symbol of \(1+A_t^*A_t\) recursively using (17B.2) gives, for any \(N\),
\[
 b_t^{(N)}=b_{0,t}+\sum_{j=1}^{N-1}t^j b_{j,t},
 \quad b_{j,t}\in S^{-2r-j},
 \qquad (1+A_t^*A_t)B_t^{(N)}=1+t^N R_t,
 \tag{17B.3}
\]
where \(B_t^{(N)}\) is its assembled quantization and \(R_t\) has uniformly bounded order \(-N\). The recursion is finite: if the current coefficient of \(t^j\) is \(e_{j,t}\), add \(-t^j b_{0,t}e_{j,t}\) to cancel it in the left product. Formula (17B.2) places the new error at the next order. At every stage products preserve the bundle types; a finite partition assembles the local leading inverse and the correction operators before the next error is computed. This also absorbs the coordinate and cutoff errors. The identical recursion applies to \(1+A_tA_t^*\).

Choose \(N>\dim M\). The remainders in (17B.3) are uniformly bounded on \(L^2\). A direct bound, sufficient here, is useful: a symbol \(b_t\) of uniform order \(-q\), \(q>\dim M\), has inverse Fourier kernel satisfying
\[
 |k_t(x,V)|\leq C_L(1+|V|)^{-L}
 \tag{17B.4}
\]
for any fixed \(L\), uniformly in \(t\). For bounded \(V\) integrate its integrable frequency bound; for large \(V\) integrate by parts \(L\) times in a frequency direction. The same estimates apply to the needed derivatives. The scaled kernel is \(t^{-\dim M}k_t(x,(x-y)/t)\). Taking \(L>\dim M\) and substituting \(V=(x-y)/t\) bounds both Schur integrals uniformly. Finite charts and density factors preserve this bound.

Write \(R_t^E=(1+A_t^*A_t)^{-1}\). Positivity gives \(\|R_t^E\|\leq1\) and \(\|A_tR_t^E\|\leq1/2\). These bounds can also be obtained without an unbounded functional-calculus formula: minimize \(\|u\|^2+\|A_tu\|^2-2\operatorname{Re}\langle y,u\rangle\) in the graph Hilbert space and use \(\|u\|^2+\|A_tu\|^2\leq\|y\|\|u\|\). Multiplying (17B.3) by the actual inverse yields
\[
 \|R_t^E-B_t^{(N)}\|=O(t^N),
 \qquad\|A_tR_t^E-A_tB_t^{(N)}\|=O(t^N).
 \tag{17B.5}
\]
Thus the first block is a quantization of uniform order \(-2r\), and the off-diagonal block a quantization of uniform order \(-r\), up to errors tending to zero in norm. The same holds on \(F\).

These quantizations are actual sections of the tangent-groupoid algebra. Their inverse Fourier kernels, written in (17.3), converge on compact sets to the boundary kernels. Equation (17B.4) makes their tails outside \(|V|\leq R\) tend to zero uniformly in the \(I\)-norm. Truncating those tails and using the finite chart cutoffs gives compactly supported continuous groupoid kernels. The density conversion is exactly (17.12), so their zero evaluations are the prescribed symbols with Fourier convention (17.17). Completion gives the claimed sections. The errors in (17B.5) are compact at positive parameter and norm-continuous there, by elliptic inversion and the resolvent identity between the fixed Sobolev spaces. They vanish in norm at zero, so belong to the cone ideal in (17.24). This proves the section assertion for the actual inverses and off-diagonal blocks, not only for parametrices.

The orthogonal graph projection is
\[
 P_t=\begin{pmatrix}
 R_t^E&(A_tR_t^E)^*\\
 A_tR_t^E&1-(1+A_tA_t^*)^{-1}
 \end{pmatrix},\qquad P_F=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
 \tag{17B.6}
\]
Solving the least-distance problem to the graph gives this formula on smooth vectors; the displayed bounds extend it to all vectors. At zero the same formula is the finite-dimensional graph projection of \(a_0(x,\eta)\). Every block of \(P-P_F\) is a section just proved. If the bundles are nontrivial, embed \(E\oplus F\) into a finite trivial bundle over compact \(M\). Its base projections are multipliers of a matrix algebra over \(\mathcal A_M\); the same block argument gives projections \(P,P_F\) with difference in that matrix algebra. Fibre detection verifies the projection identities also for the completed section.

The relative-triple excision theorem specified below therefore defines
\[
 y=[P]-[P_F]\in K_0(\mathcal A_M).
 \tag{17B.7}
\]
This difference notation is valid for these multiplier projections: their quotient projections are equal, with the identity comparison, and relative excision sends that triple to \(K_0(\mathcal A_M)\). It does not assert that a nonconstant bundle projection lies in the scalar unitization.

At zero, the graph bundle is isomorphic to \(E\), through
\(u\mapsto((1+a_0^*a_0)^{-1/2}u,
a_0(1+a_0^*a_0)^{-1/2}u)\). Projection from that graph to \(F\) gives the comparison map \(a_0(1+a_0^*a_0)^{-1/2}\), invertible outside the compact disk. Removing its positive factor gives the same relative class as \(a_0\). Since \(P_0-P_F\) vanishes at cotangent infinity, its quotient comparison is the identity, so relative excision identifies
\[
 (\mathrm{ev}_0)_*y=[\sigma(D)].
 \tag{17B.8}
\]

At one, multiply \(A_1\) by a real scalar \(s\to\infty\) in (17B.6). Closed range gives a positive lower bound for \(\|A_1u\|/\|u\|\) off its kernel, and for the adjoint off its kernel. The inverse blocks then converge in norm to the respective kernel projections, and the off-diagonal blocks converge to zero. This supplies a norm-continuous graph-projection homotopy whose limiting difference is the kernel projection on \(E\) minus the cokernel projection on \(F\). Both are finite rank. Hence
\[
 (\mathrm{ev}_1)_*y=\dim\ker A_1-\dim\operatorname{coker}A_1
                      =\operatorname{ind}D.
 \tag{17B.9}
\]
Theorem 17.7 makes \(y\) the unique inverse image of (17B.8), proving (17.29). On a zero-dimensional compact manifold all spaces are finite-dimensional. The family \(tD\) gives the same graph construction, with diagonal identity on \(E\) at zero and zero off-diagonal entries. Its two differences both have value \(\dim E-\dim F\), equal to kernel-minus-cokernel dimension. This includes that case. ∎

The comparison is due to [Connes 1994]; [Li, §11.2.1, Proposition 11.12, p. 47] gives the same assertion. The proof above supplies the parameter estimates and the graph class connecting its two evaluations.

An ordinary positive-order principal symbol is homogeneous away from the zero section; it is not itself a function vanishing at cotangent infinity. Its class comes from the bundle map being invertible away from the zero section, with the usual compact-support symbol construction. Equation (17.29) concerns that class. It does not apply the Fourier isomorphism to an unbounded principal symbol as if it were an element of \(C_0(T^*M)\).

The comparison also evaluates the class of a continuous bundle-map symbol \(p\) invertible outside a compact set on \(T^*M\), when \(M\) is compact. The exact prerequisite Symbols, finite defects, and the index on a closed manifold, AN03-GSI-008 defines \(\operatorname{s-ind}p\) by restricting to a sufficiently large cotangent sphere, smoothly approximating that invertible restriction and quantizing its homogeneous extension. Its radial homotopy and the straight homotopy to a sufficiently close approximation stay invertible outside one fixed compact disk bundle. These are also homotopies of compact-support K-theory triples. Thus \([p]\) equals the class of the resulting smooth elliptic principal symbol, and (17.29) gives \(\operatorname{Ind}^{\mathrm{def}}_M[p]=\operatorname{s-ind}p\). This reduction is the form used for the compactified Bott symbol below.

For a point, all arrows are units: \(\mathbb T\{\mathrm{pt}\}=[0,1]\) and \(\mathcal A_{\mathrm{pt}}=C([0,1])\). Both evaluations give the rank map on \(K_0\). Thus (17.26) is identity on \(\mathbb Z\).

For \(\mathbb R^n\), (17.3) is global and \(\mu=dX\). Its zero algebra is \(C_0(\mathbb R^n_X\times\mathbb R^n_\eta)\); every positive fiber is \(\mathcal K(L^2(\mathbb R^n))\). The symbol coordinate \(\eta\) is the one in (17.17), not the positive Fourier coordinate \(\xi\) of (17.18). The Bott exercise below fixes the value on an oriented generator.

On the circle \(\mathbb T=\mathbb R/\mathbb Z\), consider
\[
 D=\frac1{2\pi i}\frac{d}{d\theta}:
          H^1(\mathbb T)\longrightarrow L^2(\mathbb T).
 \tag{17.30}
\]
For \(e_k(\theta)=e^{2\pi ik\theta}\), \(De_k=ke_k\). Its kernel is the constants. Its range is the closed subspace of functions with zero constant Fourier coefficient: for such a function with coefficients \(b_k\), set \(a_k=b_k/k\) for \(k\ne0\); the resulting series is in \(H^1\), since \((1+k^2)/k^2\leq2\). Its cokernel is therefore also one-dimensional. The index is zero, and (17.29) gives
\[
 \operatorname{Ind}^{\mathrm{def}}_{\mathbb T}[\sigma(D)]=0.
 \tag{17.31}
\]
The same computation for \(D+a\), with constant \(a\in\mathbb C\), gives a bijection when \(k+a\ne0\) for every integer \(k\), and a one-dimensional kernel and cokernel otherwise. In either case its index remains zero. This example computes this differential symbol, not the indices of all circle pseudodifferential operators.

## Deformation classes and wrong-way maps

For the bivariant assertions we use the bivariant prerequisite *Asymptotic morphisms and E-theory* in *Kasparov's KK-theory*, specifically its composition theorem and its exact sequences for every extension of separable C*-algebras. Its convention is \(E(A,B)=[[SA,SB\otimes\mathcal K]]\), with product in the order of composition. Homotopy invariance, stability and the natural functor \(KK\to E\) are part of that same prerequisite. This is a proof prerequisite not included in this edition, rather than an assertion that its text is already available. The groupoid algebras below are separable: countable coordinate covers and compact exhaustions give countable dense sets in the compact test-function spaces and hence in their C*-completions.

**Lemma (the class of a deformation).** Suppose a separable section algebra \(D\) fits into an extension
\[
 0\longrightarrow C_0((0,1])\otimes B\longrightarrow D
       \xrightarrow{e_0}A\longrightarrow0,
 \tag{17A.1}
\]
with positive-parameter evaluations in \(B\). Then \([e_0]\) is invertible in E-theory, and
\[
 d_D=[e_0]^{-1}\otimes_D[e_1]\in E(A,B).
 \tag{17A.2}
\]
Its map on K-theory is \((e_1)_*(e_0)_*^{-1}\).

**Proof.** The cone ideal contracts by (17.25). The exact E-theory sequences in each variable, together with homotopy invariance, say that composing with \([e_0]\) is an isomorphism. In particular there is \(x\in E(A,D)\) with \(x\otimes_D[e_0]=1_A\). Injectivity of composition on \(E(D,D)\), and associativity, then imply \([e_0]\otimes_A x=1_D\). This proves invertibility and (17A.2). The identification \(E(\mathbb C,B)=K_0(B)\), and its suspension version, identify composition with the stated K-maps. ∎

Applying this lemma to (17.24) gives the tangent-groupoid index element. The construction uses E-theory exactness, in addition to the ordinary K-theory proof in Theorem 17.7; it does not infer a KK-inverse from a K-isomorphism.

We next build the two deformations used for a general smooth map. For a linear map \(L:E\to F\) of finite-dimensional real vector spaces, use the translation groupoid with
\[
 r(\eta,\zeta)=\eta,\qquad s(\eta,\zeta)=\eta+L\zeta.
 \tag{17.32}
\]
At scale \(\varepsilon\in[0,1]\), replace \(L\) by \(\varepsilon L\). Lebesgue measure in \(E\) is a Haar system. The full algebra is the crossed product of \(C_0(F\times[0,1])\) by this continuous vector-group action. At zero its fibre is \(C_0(F\oplus E^*)\), by the trivial-action tensor identification and Fourier theorem in Lessons 4 and 6. At every positive scale, \((\eta,\zeta)\mapsto(\eta,\varepsilon\zeta)\) identifies the groupoid with the scale-one groupoid. On kernels the isomorphism includes the factor \(\varepsilon^{-\dim E}\) from the change of Haar measure.

This is a continuous field. Full crossed-product exactness identifies the parameter fibres and proves upper semicontinuity, as in (17.19). For a compact test kernel \(a\), the regular representation on \(L^2(E)\) is
\[
 (\Lambda_{\varepsilon,\eta}(a)\psi)(v)
    =\int_E a(\eta-\varepsilon Lv,w,\varepsilon)\psi(v-w)\,dw.
 \tag{17A.3}
\]
For compactly supported \(\psi\), uniform convergence on compact sets proves convergence of these operators on every compact output set when \(\varepsilon\) varies. At a fixed scale, choose \(\eta,\psi\) and an output cutoff approximating the regular norm. This proves lower semicontinuity of that norm. Vector-group amenability gives full equals reduced by Lesson 4, so it proves the needed lower bound for the full norm. Density proves continuity for all sections. The positive-parameter ideal is the trivial cone on the scale-one algebra, by the explicit scaling isomorphisms. The preceding lemma therefore gives the linear deformation class. No surjectivity or injectivity of \(L\) was required.

Now let \(f:M\to N\) be a smooth map between Hausdorff second countable manifolds without boundary. Write \(m=\dim M\), and use a metric to identify \(TM\) with \(T^*M\) when discussing orientations. The **differential index groupoid** \(J_f\) has unit space \(f^*TN\), and arrows \((x,\eta,v)\), with
\[
 r(x,\eta,v)=(x,\eta),\qquad
 s(x,\eta,v)=(x,\eta+df_xv).
 \tag{17A.4}
\]
Its product adds the two tangent vectors, and its Haar measure is the linear density on \(T_xM\). Scaling \(df\) gives the first deformation, from the commutative algebra
\(C_0(T^*M\oplus f^*TN)\) to \(C^*(J_f)\). Here \(\oplus\) means the fibre sum over \(M\). The preceding proof applies in bundle charts. More explicitly, central fibre detection over \(x\in M\) reduces full and reduced norms to the vector-group crossed products at \(x\); lower bounds at a fixed \(x\) use (17A.3). Compact base partitions supply density and upper semicontinuity globally. Scaling the vector variable trivializes the positive ideal with the same \(\varepsilon^{-m}\) factor. Thus its E-class, say \(\theta_f\), is defined by (17A.2).

The second deformation has arrow and unit spaces
\[
 \begin{aligned}
 \mathcal D_f&=(N\times M\times M\times(0,1])
                         \sqcup(J_f\times\{0\}),\\
 \mathcal D_f^{(0)}&=(N\times M\times(0,1])
                         \sqcup(f^*TN\times\{0\}).
 \end{aligned}
 \tag{17A.5}
\]
At positive parameter it is the pair groupoid in the \(M\)-variables, leaving the \(N\)-coordinate fixed. It is the normal deformation of the subgroupoid of units \(x\mapsto(f(x),x,x)\). To verify its boundary rather than merely name it, take coordinate maps on both manifolds and write \(F\) for the coordinate expression of \(f\). Its local arrows are
\[
 (X,\eta,V,t)\longmapsto
       (F(X)+t\eta,X,X-tV,t),\qquad t>0.
 \tag{17A.6}
\]
At zero they are \((x,\eta,v)\). The source unit's rescaled normal coordinate is
\[
 \frac{F(X)+t\eta-F(X-tV)}t
       =\eta+\int_0^1DF(X-stV)V\,ds.
 \tag{17A.7}
\]
It tends to \(\eta+df_xv\), as in (17A.4). Range is \((X,\eta,t)\), and multiplication adds displacement vectors after making this source-coordinate change. Inversion reverses the displacement. Coordinate transitions in the \(N\)-variable use the same divided-difference formula as (17.4), based at \(F(X)\); transitions in \(M\) are exactly (17.4). Thus all operations extend smoothly, with range and source submersions. The Hausdorff and countable-chart arguments of Lemma 17.1 apply to this normal deformation as well.

Choose a positive density \(\mu\) on \(M\). The positive-parameter Haar measure is \(t^{-m}d\mu(y)\) in the last \(M\)-variable, and the zero measure is its linear density in \(v\). Formula (17.12), now in the \(M\)-coordinates of (17A.6), proves continuity; left invariance follows from the pair and translation products. Full invariant-ideal exactness and the pair calculation of Lesson 14 give
\[
 0\longrightarrow C_0((0,1])\otimes C_0(N)\otimes\mathcal K(L^2M)
   \longrightarrow C^*(\mathcal D_f)
   \xrightarrow{e_0}C^*(J_f)\longrightarrow0.
 \tag{17A.8}
\]
There is no properness assumption on \(f\): kernels have compact support in the displayed arrow space, and the positive fibre is the full pair algebra over \(N\).

For completeness, continuity at zero follows without assuming a general continuity theorem for deformations. Every parameter fibre has full equals reduced: at zero use the fibrewise vector actions, and at positive parameter use the pair groupoids. Consequently the full fibre supremum and the reduced source-fibre supremum agree, as in Corollary 17.5. Fix a zero source unit \((x_0,\eta_0)\). In positive fibres take the source units \((F(X_0)+t\eta_0,x_0)\). A compactly supported vector \(\psi(W)\) in the zero regular space is represented at \(t>0\) by a vector supported at \(X=X_0+tW\), multiplied by \(t^{-m/2}\) and the smooth density normalization. In the range and source integral, change the input variable likewise to \(X_0+tW'\). For a smooth compact kernel its rescaled matrix is, on fixed compact \(W,W'\)-sets,
\[
 a_t\bigl(X_0+tW,\eta_t(W),W-W'\bigr)
          \rho(X_0+tW')\longrightarrow
 a_0\bigl(X_0,\eta_0-df_{x_0}W,W-W'\bigr)\rho(X_0).
 \tag{17A.9}
\]
Here \(d\mu=\rho(X)dX\) and \(\eta_t(W)=(F(X_0)+t\eta_0-F(X_0+tW))/t\). The right side is the zero regular kernel; (17A.7) verifies its sign. Uniform convergence proves convergence on any compact output set. Compactly supported inputs are dense, and increasing compact output cutoffs approximate their output norm. Taking the supremum over zero units proves the lower norm bound. Upper semicontinuity follows from the full quotient extension, and smooth-core density completes the proof. At positive parameter compact kernels and compact \(N\)-cutoffs give ordinary operator-norm continuity. Thus (17A.8) is indeed the required continuous deformation.

Let \(\delta_f\in E(C^*(J_f),C_0(N)\otimes\mathcal K)\) be its class. Stability identifies the last algebra with \(C_0(N)\) in E-theory; equivalently use the inverse of the rank-one corner, whose stabilization is an equivalence by the E-theory prerequisite specified below. The two deformations therefore produce
\[
 f!_{\mathrm{def}}=\theta_f\otimes_{C^*(J_f)}\delta_f
       \otimes_{C_0(N)\otimes\mathcal K}[\text{corner}]^{-1}
       \in E(C_0(T^*M\oplus f^*TN),C_0(N)).
 \tag{17.33}
\]
The construction and its original attribution are [Connes 1994]. The groupoids, parameter extensions and bivariant class used here have now been constructed explicitly.

A chosen \(\operatorname{Spin}^c\) structure on \(V=T^*M\oplus f^*TN\) supplies its Thom class from \(C_0(M)\), of degree \(m+\dim N\) modulo two. The fibre convention and compact-base Thom theorem belong to the bivariant prerequisite *Thom isomorphisms and K-orientations in KK*, §1–§3, in *Kasparov's KK-theory*. Its positive fibre class is the ordered Bott class.

The class itself exists also when \(M\) is noncompact, as needed here. For even rank use the graded spinor bundle \(S=S^+\oplus S^-\), the Hilbert \(C_0(V)\)-module of sections vanishing at infinity of \(\pi^*S\), and the action of \(a\in C_0(M)\) by multiplication by \(a\circ\pi\). The odd self-adjoint multiplier is
\[
 F(v)=\frac{c(v)}{\sqrt{1+|v|^2}},\qquad c(v)^2=|v|^2.
 \tag{17A.10}
\]
It commutes with the base action, and \((F^2-1)a=-a(\pi(v))/(1+|v|^2)\) is a compact module endomorphism: this continuous endomorphism vanishes at infinity, by a compact base cutoff followed by a bounded-radius fibre cutoff. Locally finite trivializations approximate it by finite sums of rank-one endomorphisms. The remaining Kasparov defects are zero. Thus this is an actual Thom cycle on the noncompact base. For odd rank the same Clifford construction, with one graded \(\mathrm{Cl}_1\) factor, gives the odd class. Its restriction to a compact base has exactly the specified prerequisite's normalization. Applying the functor \(KK\to E\) and composing with (17.33) defines the oriented class without requiring \(f\) to be proper.

The agreement of this composite with the manifold wrong-way class, and hence its factorization independence, homotopy invariance, composition and projection formulas, is the exact deformation-comparison topic of the bivariant prerequisite *Wrong-way maps for K-oriented maps*, §5, together with its manifold factorization theorem in §4. Its comparison uses the two unoriented deformations just constructed and identifies their Thom composite with the embedding-and-projection construction. These are proof prerequisites not included in this edition in the KK course, including the full comparison. They do not assert a previously written proof. Only the geometric construction and the two parameter extensions above are needed from this lesson; no product law is used to construct them. Thus these dependencies do not require the wrong-way comparison as their own input.

## Exercises with solutions

**Exercise 1 (A point).** Give all structure maps, the algebra, the exact sequence, and the deformation index when \(M\) is a point.

**Solution.** Every parameter contributes one identity arrow. Range and source are both the parameter, each arrow is its own inverse, and only identical arrows compose. Counting Haar measure on each one-point fiber makes convolution and involution pointwise multiplication and complex conjugation. Hence the algebra is \(C([0,1])\), and the sequence is
\[
 0\to C_0((0,1])\to C([0,1])
           \xrightarrow{a\mapsto a(0)}\mathbb C\to0.
 \tag{17.34}
\]
Evaluation at zero is a K-isomorphism by Theorem 17.7, or by the homotopy \(a(t)\mapsto a(st)\). Constants give its inverse on K-theory. Evaluation at one sends the constant rank-one projection to \(1\), so the index on \(K_0(\mathbb C)=\mathbb Z\) is identity; \(K_1(\mathbb C)=0\). ∎

**Exercise 2 (Normal-cone coordinates).** Identify the normal bundle of the diagonal in \(\mathbb R^n\times\mathbb R^n\), write global tangent-groupoid coordinates, and verify multiplication, inversion, and the Haar limit in those coordinates.

**Solution.** A normal vector is a class of \((v,w)\) modulo vectors \((a,a)\). The map \([(v,w)]\mapsto v-w\) is onto with precisely that kernel, identifying it with \(\mathbb R^n_X\times\mathbb R^n_V\). The chart is \((X,V,t)\mapsto(X,X-tV,t)\) at positive parameter, and \((X,V,0)\) at zero. Its inverse at positive parameter divides \(X-y\) by \(t\).

Composability requires the second arrow's range to be \(X-tV\). The product of the pairs is
\((X,X-t(V+W),t)\), giving \((X,V+W,t)\). The reversed pair has coordinates \((X-tV,-V,t)\). At zero these are exactly vector addition and additive inversion. Both maps are smooth, and the maps \((X,V,t)\mapsto(X,t)\) and \((X-tV,t)\) have surjective differentials. Finally \(y=X-tV\) gives \(t^{-n}dy=dV\), so the range-fiber integrals converge to ordinary vector-space convolution. This also derives the action (17.10). ∎

**Exercise 3 (The contractible ideal).** Prove point-norm continuity of (17.25), including at \(s=0\), and give the two uses of exactness that make evaluation at zero a K-isomorphism.

**Solution.** For \(F\), extended by \(F(0)=0\), define its modulus of continuity
\(\omega_F(\delta)=\sup_{|u-v|\leq\delta}\|F(u)-F(v)\|\). It tends to zero by uniform continuity. Thus
\[
 \|H_sF-H_rF\|\leq\omega_F(|s-r|).
 \tag{17.35}
\]
At zero this proves convergence to the zero homomorphism; at one it proves convergence to identity. Products and adjoints are preserved by evaluation at \(st\), so it is a homotopy of homomorphisms. Both K-groups of the ideal vanish.

In the six-term cycle of (17.24), exactness at \(K_i(\mathcal A_M)\) says the kernel of \((\mathrm{ev}_0)_*\) is the image of the zero group \(K_i(I)\), proving injectivity. Exactness at \(K_i(C_0(T^*M))\) says its image is the kernel of the boundary to \(K_{1-i}(I)=0\), proving surjectivity. This works for \(i=0,1\). It does not invert evaluation as an algebra homomorphism or supply a multiplicative section. ∎

**Exercise 4 (The Bott symbol).** With the convention (17.17), show that the deformation index of the Bott class on \(T^*\mathbb R^n\) is \(1\), by comparison with the harmonic oscillator. Specify exactly which analytic results enter.

**Solution.** Suppose \(n\geq1\). On \(\Lambda^*\mathbb C^n\), let \(\varepsilon_j\) be exterior multiplication by the \(j\)-th basis vector and \(\iota_j=\varepsilon_j^*\). Define the map from even to odd exterior powers by
\[
 p(w)=\left.
       \sum_j(w_j\varepsilon_j+\overline w_j\iota_j)
                      \right|_{\Lambda^{\mathrm{even}}},
 \qquad w=x+i\eta.
 \tag{17.36}
\]
The Clifford relations give \(p(w)^*p(w)=|w|^2\) and \(p(w)p(w)^*=|w|^2\), so the bundle-map triple is invertible off the origin and defines \(b_n\in K_c^0(\mathbb R^{2n})\). The even-to-odd direction and \(x+i\eta\) fix its orientation.

We reuse The Bott operator, suspension, and reduction of the index to Euclidean space, Proposition 4.4: replacing \(\eta_j\) by \(D_j=-i\partial_j\) gives
\[
 P=\left.\sum_j\big((x_j+\partial_j)\varepsilon_j
                     +(x_j-\partial_j)\iota_j\big)
                        \right|_{\Lambda^{\mathrm{even}}}.
 \tag{17.37}
\]
As a bounded map from the weighted first-order space to odd \(L^2\)-forms, it is surjective, with kernel the degree-zero Gaussian \(e^{-|x|^2/2}\), hence index \(1\). The prerequisite proves the domain, closed range and cokernel assertions; a formal Gaussian computation alone would not establish them.

To connect this noncompact model to the compact comparison (17.29), use the same prerequisite's compactification, §8, Proposition 8.1 and Corollary 10.1(1). On \(S^n=\mathbb R^n\cup\{\infty\}\), its Bott bundles \(E_B,F_B\) and symbol
\[
 \beta_S(x,\eta)=\psi(x)p(x+i\phi(x)\eta)
 \tag{17.38}
\]
have \(\phi=1\) near \(0\), \(\phi=0\) outside a large ball, \(\psi>0\), and \(\psi(x)=|x|^{-1}\) near infinity. The target bundle is glued by \(p(x/|x|)\). Thus (17.38) is identity in the target's second trivialization near infinity, and is invertible except at \((0,0)\). The cited corollary proves that its symbol index is \(1\), by the order reduction and compactification of the oscillator. In a small cotangent neighborhood of the origin, it is the positive scalar multiple \(\psi(x)p(x+i\eta)\). Compact-support symbol excision therefore identifies its class with \((j_0)_*b_n\), for the open chart \(j:\mathbb R^n\hookrightarrow S^n\): both triples have support at that origin and agree there up to a positive scalar homotopy.

Apply Proposition 17.8 and then the compact comparison to obtain
\[
 \operatorname{Ind}^{\mathrm{def}}_{\mathbb R^n}(b_n)
   =\operatorname{Ind}^{\mathrm{def}}_{S^n}[\beta_S]
   =\operatorname{s-ind}(\beta_S)=1.
 \tag{17.39}
\]
The oscillator and its compactified symbol are written prerequisites. Equality with the classical symbol index on \(S^n\) is the comparison theorem proved above; locality of the deformation index was proved here. No compact-manifold comparison was silently applied directly on \(\mathbb R^n\). For \(n=0\) the Bott class is the unit on a point, handled by Exercise 1. ∎

## What this lesson does not prove

We use smooth-manifold foundations, including the inverse function theorem, densities, metrics and partitions of unity; ordinary Fourier analysis and the locally compact Stone–Weierstrass theorem; and homotopy invariance, rank normalization and stability in K-theory. The positive natural six-term cycle is The six-term exact sequence and the exponential map, Theorem 2.1. The bundle-triple model is Topological K-theory of spaces, pairs and vector bundles, §2, Theorem 2.1, and its algebraic excision map is The six-term exact sequence and the exponential map, Theorem 6.1. For a cotangent symbol on compact \(M\), embed the bundles into finite trivial bundles over \(M\) and pull their projections back to \(T^*M\). Polar normalization of the symbol outside a compact disk gives a bounded partial isometry there; a radial cutoff extends it to a bounded matrix on the total space. Its initial and final projections agree with the bundle projections modulo \(C_0(T^*M)\). The exact relative-triple excision theorem, applied to \(C_0(T^*M)\subset C_b(T^*M)\), therefore defines its K-class. Homotopies invertible outside one common compact set give relative-triple homotopies. This proves the compact-support use here without requiring those pulled-back bundles to extend over cotangent infinity. The full groupoid construction, invariant-ideal exactness, pair algebra and group-bundle norm detection are from Lesson 14. Vector-space amenability and Fourier C*-duality are from Lessons 4 and 6.

The classical elliptic comparison (17.29) is proved above, using the written Euclidean and geometric symbol calculus and elliptic order-change theorems specified there. Its uniform parameter estimates and graph-projection class are included. Exercise 4 reuses the harmonic oscillator theorem and the sphere Bott-symbol computation, with their exact locators in *The Bott operator, suspension, and reduction of the index to Euclidean space*. The two differential-index deformations and their extensions are constructed above. Their E-classes use the exact E-theory composition and extension theorems identified in that section. The oriented comparison and product laws are the specified bivariant manifold wrong-way lesson; its deformation comparison takes the constructed groupoids as inputs. The noncompact Thom cycle is supplied here.

The rescaled smooth groupoid, Haar system, full and reduced fiber identifications, continuous field, exact contractible-ideal extension, K-theoretic deformation map, locality and the four applications above have been proved within these prerequisites.

## References

[Connes 1994] A. Connes, *Noncommutative Geometry*, [author's electronic edition](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf), Chapter II, §5, pp. 104–111: Proposition 4 and Proposition 5, p. 108, for the tangent construction and its algebra; Lemma 6, p. 109, for the stated analytic comparison. Chapter II, §6, pp. 111–116: Proposition 1, p. 112; §6β, p. 113; Definitions 2 and 4, p. 114; and Theorem 7, pp. 115–116, for wrong-way deformations and orientations.

[Li] Y. Li, *Groupoid C*-algebras*, [Leiden seminar notes](https://ncg-leiden.github.io/groupoid2022/groupoid_notes.pdf), fall 2022, version dated 7 February 2024, §11.1–11.2, pp. 44–49. Definition 11.10, Definition and Lemma 11.11, and Proposition 11.12 are on p. 47. The exponential charts are understood locally on bounded tangent neighborhoods.

The six-term exact sequence and the exponential map K-theory for operator algebras, Lesson 11, Theorem 2.1, the exact natural K-theory cycle.

The Bott operator, suspension, and reduction of the index to Euclidean space Index theory of elliptic operators, Proposition 4.4, §8 and Proposition 8.1, and Corollary 10.1(1). These provide the weighted oscillator of index one and its compactified Bott symbol.

Symbols, finite defects, and the index on a closed manifold Symbols, finite defects, and the index on a closed manifold, AN03-GSI-007 and AN03-GSI-008: radial reduction and the index of a continuous bundle-map symbol.

Topological K-theory of spaces, pairs and vector bundles K-theory of C*-algebras, Lesson 12, §2, Theorem 2.1, the difference-bundle model. The algebraic relative excision used on the cotangent total space is Theorem 6.1 of the six-term lesson cited above.

[Bivariant prerequisites] Kasparov's KK-theory: *Asymptotic morphisms and E-theory*, Outline 2–5 (separable composition, exact sequences, stability and comparison); *Thom isomorphisms and K-orientations in KK*, Outline 1–3 (compact-base fibre convention); and *Wrong-way maps for K-oriented maps*, Outline 4–5 (general manifold factorization and its deformation comparison). The proofs of these three bivariant prerequisites are not included in this edition. The corresponding bivariant assertions are conditional on them; see Prerequisites.

[Euclidean symbol calculus] From symbol estimates to operators on every Sobolev scale, AN03-EUC-005, equations (E20)–(E21), with finite-seminorm product and adjoint remainder control.

[Geometric microlocal calculus] Detecting regularity without choosing coordinates, AN03-GEO-004 and AN03-GEO-006, finite-atlas bundle assembly and elliptic parametrices. The compact elliptic alternative and exact order changes are AN03-GSI-002–003 of the closed-manifold symbol lesson cited above.
