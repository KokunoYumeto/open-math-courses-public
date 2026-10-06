# Modular curves over Q and the Eichler–Shimura congruence

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Hecke operator changes an elliptic curve by taking quotients by finite subgroups. Frobenius changes its coefficients by taking powers in a finite field. In characteristic \(p\), the degree-\(p\) Hecke correspondence separates into Frobenius and its transpose. This geometric identity produces the quadratic polynomials that will describe the Galois representations of weight-two forms.

There are two counting issues to keep distinct. An ordinary elliptic curve in characteristic \(p\) has two subgroup schemes of rank \(p\), while the Hecke correspondence still has degree \(p+1\). Also, a space of cusp forms of dimension \(g\) supplies a Tate module of dimension \(2g\), but its Hecke trace is the Frobenius trace, without an extra factor of two. We prove both assertions, including the linear algebra needed to obtain the characteristic polynomial.

## 1. Modular curves and their good models

For \(N\ge1\), let \(Y_0(N)\) classify elliptic curves together with a cyclic subgroup of order \(N\), and let \(Y_1(N)\) classify an elliptic curve together with a point of exact order \(N\). Over an algebraically closed field in which \(N\) is invertible, these descriptions mean isomorphism classes of pairs
\[
(E,C),\qquad (E,P).
\tag{1}
\]
The compactifications \(X_0(N)\) and \(X_1(N)\) add cusps. Over \(\mathbf C\), they are the compact Riemann surfaces attached to \(\Gamma_0(N)\) and \(\Gamma_1(N)\). The analytic construction is actually proved in the earlier *Modular curves and their genus*, §§1–2, and its moduli interpretation in *Complex tori, elliptic curves and the moduli interpretation of modular curves*, Theorem 4.1. The following stronger arithmetic theorem remains a required theorem; its construction is among the proof obligations identified in §7.

**Model theorem.** These curves have smooth projective models over \(\mathbf Z[1/N]\). Their noncuspidal parts have the moduli interpretation (1), and \(Y_1(N)\) is a fine moduli scheme for \(N\ge4\). In particular, \(X_0(N)\), \(X_1(N)\), and their Jacobians have good reduction at every prime \(p\nmid N\).

The distinction between a coarse space and a fine space matters. A point of a coarse curve over a nonclosed field is not a universal elliptic curve with its level structure. In particular, a coarse rational point records a Galois-invariant isomorphism class; twists and descent must still be considered. The fine scheme \(Y_1(N)\) represents the functor of isomorphism classes in families and carries a universal pair.

**Lemma 1.0 (the interior level and tame quotient calculations).** Once a smooth elliptic family is given over a base on which \(N\) is invertible, its full-level, cyclic-level and exact-order-point functors are finite étale over that base. At an interior coarse-moduli point in residue characteristic greater than three, a smooth one-parameter elliptic deformation chart has a smooth invariant chart under its stabilizer.

*Proof.* Multiplication by \(N\) has differential multiplication by \(N\) on the tangent line, at every point by translation, and is therefore étale. Its kernel is proper with finite fibres, hence finite étale. Its rank is \(N^2\) by the multiplication-degree proof in the earlier Tate-module lesson. Locally in the étale topology it is \((\mathbf Z/N)^2\). Choices of a basis, a cyclic direct summand, or an exact-order vector then form finite constant sets on this cover. Transition changes of basis permute the sets, which descend as finite étale schemes. The exact-order condition is checked prime by prime, so this includes composite \(N\).

In characteristic greater than three write the fibre as \(y^2=x^3+ax+b\). An origin-preserving automorphism has the form \((x,y)\mapsto(c^2x,c^3y)\), with \(c^4a=a\) and \(c^6b=b\). This follows by comparing the unique pole spaces of orders two and three at the origin: their bases are \(1,x\) and \(1,x,y\); substituting their possible affine changes into the short cubic eliminates the extra shifts. Since \(a,b\) are not both zero, its group is cyclic of order dividing four or six, and its order is invertible in the residue field.

In a strict complete one-parameter chart \(R[[t]]\), let a cyclic effective stabilizer of order \(e\) fix the origin. Its tangent action is faithful: an element of prime-to-characteristic order with tangent eigenvalue one has invariant parameter obtained by averaging its translates of \(t\); that parameter has unit linear coefficient, so fixing it makes the element the identity. Thus its tangent eigenvalue has order \(e\). Lift that eigenvalue \(\zeta\); the root-lifting proof in Lesson 01 lifts the prime-to-characteristic roots of unity to \(R\). Averaging
\[
 s=\frac1e\sum_{i=0}^{e-1}\zeta^{-i}\sigma^i(t)
\]
gives an eigenparameter, with unit linear coefficient. Formal substitution recursively inverts \(t\mapsto s\), and \(\sigma(s)=\zeta s\). Its invariant ring is exactly \(R[[s^e]]\): an invariant coefficient of \(s^n\) is zero unless \(e\mid n\), since \(1-\zeta^n\) is then a unit. This is a smooth formal chart. An ineffective stabilizer is discarded before applying the calculation. Thus tame coarse quotienting adds no singularity. This calculation proves the interior finite-level and tame-quotient steps; it does not construct the underlying elliptic deformation stack, its compactification, or the wild invariant charts in characteristics two and three. Those stronger steps of the stated model theorem are still required. ∎

The absence of automorphisms in the fine range can be checked on geometric fibers. First its geometric origin-preserving automorphism group is finite. The line bundle \(\mathcal O(3O)\) embeds it as a cubic, by the actual all-characteristic degree-three proof in *Abelian varieties*, Example 9.12. Every origin-preserving automorphism acts on its three-dimensional section space, and the group preserving the cubic and its origin is a closed subgroup of \(\operatorname{PGL}_3\), cut out by the polynomial-preservation equations. Its tangent space consists of vector fields vanishing at the origin: an infinitesimal map is locally the identity plus a derivation, and its overlaps identify those derivations as a global vector field. The elliptic tangent bundle is trivial by translation, while \(H^0(\mathcal O(-O))=0\) since a negative-degree line bundle has no section. Thus the group has zero tangent space, hence dimension zero at the identity and, by translation, everywhere. A zero-dimensional scheme of finite type has finitely many geometric points. Every such automorphism consequently has finite order.

A nonidentity origin-preserving automorphism \(u\) of an elliptic curve has \(\deg(u-1)\le4\); equality four occurs only for \(u=-1\). Indeed, its finite-order characteristic polynomial has roots \(\lambda,\lambda^{-1}\) on the unit circle, so
\[
\deg(u-1)=2-(\lambda+\lambda^{-1})\le4.
\tag{2}
\]
The degree and characteristic-polynomial identity is the one established for endomorphisms in the Tate-module lesson. If equality holds, \(u+1\) is nilpotent in the endomorphism algebra and hence zero: a nonzero endomorphism of an elliptic curve is an isogeny and becomes invertible in that algebra. If \(u\) fixes a point of order \(N\), its kernel contains the \(N\) distinct points generated by that point, so \(\deg(u-1)\ge N\). This is impossible for \(N\ge5\); for \(N=4\), the only remaining candidate \(-1\) does not fix a point of order four. The representability and construction of the scheme remain part of the model theorem.

At the cusp \(\infty\) of \(X_0(N)\), the Tate curve with parameter \(q\) and subgroup \(\mu_N\) gives the local expansion. At a general cusp of width \(w\), the analytic coordinate is \(q_c=e^{2\pi iz/w}\). The formal Tate-curve description supplies the corresponding algebraic coordinate, with roots of \(q\) and roots of unity as needed by the level structure. This is the geometric meaning of a \(q\)-expansion, rather than a new Galois representation at a cusp.

Write
\[
X=X_0(N),\qquad J=J_0(N)=\operatorname{Pic}^0(X),\qquad
g=\dim S_2(\Gamma_0(N)).
\tag{3}
\]
The cusp \(\infty\) is rational, so \(x\mapsto[x-\infty]\) defines the Abel–Jacobi map. The equality of the analytic genus with the dimension of holomorphic differentials is proved in *Dimension formulas for congruence subgroups*, Appendix A.7. The construction and dimension of the algebraic Jacobian are proved in *The Picard functor and the Picard scheme of a curve*, §§4–7, especially Theorems 6.2 and 7.2. Lemma 1.2 below identifies the analytic and algebraic genera. Thus both dimensions are \(g\).

**Lemma 1.1 (weight two and differentials).** The map \(f\mapsto f(z)\,dz\) identifies \(S_2(\Gamma_0(N))\) with the holomorphic differentials on \(X(\mathbf C)\).

*Proof.* The weight-two transformation law and \(d(\gamma z)=(cz+d)^{-2}dz\) make this differential invariant. At a cusp,
\[
f(z)\,dz=\frac{w}{2\pi i}\,f(q_c)\frac{dq_c}{q_c}.
\tag{4}
\]
It is holomorphic exactly when the constant term of the cusp expansion vanishes. There is no additional pole at an elliptic point. In a local coordinate \(u\) where its stabilizer acts by \(u\mapsto\zeta u\) of order \(e\), invariance of \(a(u)\,du\) forces \(a(u)=u^{e-1}b(u^e)\); putting \(t=u^e\) gives \(a(u)\,du=b(t)\,dt/e\). Thus it descends holomorphically. Conversely, pulling a holomorphic differential back to the upper half-plane gives a weight-two form, and (4) makes it cuspidal. These constructions are inverse. ∎

The decomposition needed in degree one is
\[
H^1(X(\mathbf C),\mathbf C)
\simeq S_2(\Gamma_0(N))\oplus\overline{S_2(\Gamma_0(N))}.
\tag{5}
\]
The bar denotes the antiholomorphic summand. It supplies the second copy of the Hecke spectrum; it does not double the eventual Frobenius trace.

**Lemma 1.2 (the curve realization and comparison).** For a smooth projective connected complex algebraic curve, analytification identifies algebraic and analytic line bundles and meromorphic functions, and identifies finite étale covers with finite analytic unramified covers. Consequently finite-coefficient degree-one étale cohomology equals degree-one cohomology of the analytic surface, naturally for finite correspondences. For the modular curve the decomposition (5) is Hecke equivariant. Passing to the coefficient limit gives Betti–étale comparison in degree one.

*Proof.* Here are the particular algebraization arguments needed, so that a general comparison theorem is not an unproved premise. The analytic Riemann–Roch and meromorphic-section proofs for arbitrary compact curves and arbitrary line bundles are written in *Dimension formulas for congruence subgroups*, Appendix A.1–A.7. Algebraic curve Riemann–Roch and canonical degree are proved in *Abelian varieties*, Lemma 9.11. The two genera agree: choose a separating rational function on the algebraic curve. Local parameters give the ramification orders of its derivative, hence the algebraic canonical degree is \(-2d+\sum(e_x-1)\). The same local maps, analytically \(u\mapsto u^{e_x}\), give the same number by the polygon proof in the earlier analytic Appendix A.7. The identities \(\deg K=2g-2\) on both sides prove equality of genera.

For an effective divisor \(D\), algebraic sections of \(\mathcal O(D)\) inject into analytic sections. If \(\deg D>2g-2\), the two Riemann–Roch formulas give the same dimension, so that injection is an isomorphism. Every meromorphic function has a finite pole divisor and therefore belongs to one such space after enlarging the divisor. Thus every analytic meromorphic function is rational. Every analytic line bundle has a nonzero meromorphic section by the earlier Appendix A.6, and is \(\mathcal O(D)\) for its finite divisor. All points of a complex algebraic curve are algebraic closed points. Its analytic line bundle consequently algebraizes. Meromorphic sections of the Hom bundle show that morphisms also algebraize: an analytic holomorphic morphism is a rational section with the prescribed nonnegative local orders, hence an algebraic morphism. This proves precisely the curve line-bundle comparison required here.

Let \(Z\to X^{\mathrm{an}}\) be a finite unramified analytic covering of degree \(d\), first with connected \(Z\). It is a compact Riemann surface. Analytic Riemann–Roch, after adding a sufficiently large pole divisor away from a regular fibre, permits arbitrary prescribed values at that fibre: apply its negative-degree dual correction to the evaluation exact sequence. Choose a meromorphic function \(t\) with pairwise distinct values on the \(d\) points. Symmetric functions of its values on the sheets are meromorphic functions on \(X^{\mathrm{an}}\). Near a pole, bounded pole orders on the finitely many sheets bound their elementary symmetric functions, so they extend meromorphically there. They are rational by the preceding paragraph. The monic polynomial
\[
 \prod_{z\mapsto x}(T-t(z))
\]
therefore has coefficients in \(\mathbf C(X)\). The sheets are distinguished generically. Analytic continuation on connected \(Z\) is transitive on them: lift paths between any two points of a fibre and project the paths. A factor of this polynomial over \(\mathbf C(X)\) would give a continuation-invariant proper collection of sheets. Hence it is irreducible and defines an extension of degree \(d\).

The normalization needed here is finite by the following algebra argument. On a smooth affine chart let \(A\) be its normal Noetherian coordinate domain, \(K\) its fraction field, and \(L/K\) this finite extension. Characteristic zero makes it separable. Choose a \(K\)-basis \(e_i\) integral over \(A\), by clearing denominators in their monic equations. The trace pairing is nondegenerate: a primitive element has distinct conjugates, and the Vandermonde matrix of their powers is invertible. Such an element exists by avoiding the finitely many linear equalities between distinct embeddings in the infinite field \(K\). For an integral \(b\in L\), every \(\operatorname{Tr}(be_i)\) is integral and lies in \(K\), hence in \(A\). Consequently the integral closure is contained in the free finite trace-dual lattice of \(\sum A e_i\). Its submodule is finite by Noetherianity. Integral closure commutes with localization: multiplying a monic equation over a localization by a suitable power of its denominator makes a multiple of the element integral before localization. These affine normalizations therefore glue. Their closed local rings are DVRs by the actual proof in *Discrete valuation rings, normal rings and Serre's criterion*, Lemma 1.1 and Theorem 1.2. This supplies both finiteness and the local description, rather than an unlocated normalization premise; freely accessible comparison materials are Stacks Tags 032L and 00PD.

Normalize the algebraic curve in \(L\) by this construction. The analytification of the resulting curve is \(Z\). Indeed, on a small disk every sheet is a disk over the same parameter; the integral closure of its convergent local ring in those local meromorphic sheets is the product of the disk rings, since each disk ring is a DVR. An element satisfying a monic equation with holomorphic coefficients has no pole, which also verifies this description directly. The generic identification given by \(t\) extends uniquely across its poles, by those discrete valuation rings. The algebraic map has ramification index one at every point, hence is étale. Conversely analytification of an étale map is a local biholomorphism by the local inverse theorem. An analytic map between two such covers algebraizes: its pullback on meromorphic functions is a map of the two function-field extensions, and the local valuation condition extends it on the normal curves. Disconnected covers are the disjoint union of this construction. Cover actions and equivariant maps are included by full faithfulness. This proves the finite-cover assertion.

Degree-one cohomology with a finite constant abelian group classifies torsors with that group. Algebraic and analytic transition cocycles correspond under the just-proved cover equivalence; their group laws and connecting maps are preserved. Thus the degree-one comparison is canonical and additive. Kummer is exact in both topologies, and the line-bundle comparison identifies its degree-two class with the winding number of a transition function. In the algebraic theory the actual proof in *Poincaré duality for curves*, §2, identifies \(H^2(X,\mu_n)\) with \(\mathbf Z/n\) by divisor degree; on the surface its oriented fundamental class does the same. A positive local parameter has winding one, so these generators and their traces agree. Cup products are formed from the same transition maps and therefore correspond. Pullback is natural; the trace of a finite map is the sum over its sheets, extended at a ramification point with its local length. Thus traces and correspondences correspond too.

For modular curves the period proof is actually written in *Group cohomology of \(\Gamma\) and the Eichler–Shimura isomorphism*, §§3–5, Theorem 5.3, including the weight-two dimension calculation. Its parabolic cocycles are exactly the period functionals on the compact surface: cusp loops are killed, and an elliptic loop has finite order and is killed with characteristic-zero constant coefficients. The handle presentation there identifies this space with \(H^1(X^{\mathrm{an}},\mathbf C)\). The integral double-coset cocycle and its period equivariance are proved in *Modular symbols and the algebraicity of Hecke eigenvalues*, §1, equations (1.3) and (1.8). This proves (5) with its Hecke action.

Finally the compact surface's handle cell complex is a finite free integral complex. Reducing it modulo \(\ell^r\), taking the inverse limit, and tensoring with \(\mathbf Q_\ell\) gives its rational cohomology tensored with \(\mathbf Q_\ell\); its first integral cohomology is free. The finite comparison maps commute with reduction. Finiteness makes these towers Mittag–Leffler, so the inverse-limit comparison has no extra \(\varprojlim^1\) term. This is degree-one Betti–étale comparison, rather than an application of a finite-coefficient theorem directly to \(\mathbf Q_\ell\). ∎

**Lemma 1.3 (Tate modules, pairings and good specialization).** Put \(J=\operatorname{Pic}^0(X)\). There are natural identifications
\[
 H^1_{\mathrm{\acute et}}(X,\mathbf Q_\ell(1))=V_\ell J,
 \qquad H^1_{\mathrm{\acute et}}(X,\mathbf Q_\ell)
       \simeq(V_\ell J)^\vee.
\]
The rational Tate module has a nondegenerate alternating pairing into \(\mathbf Q_\ell(1)\). A symmetric curve correspondence is self-adjoint. If \(J\) extends to an abelian scheme at \(p\ne\ell\), specialization identifies its generic and special Tate modules, and arithmetic Frobenius is the special-fibre Frobenius endomorphism.

*Proof.* On a projective geometrically connected curve, every global unit over the algebraic closure is constant, and constants have \(\ell^r\)-th roots. The Kummer exact sequence therefore identifies \(H^1(X,\mu_{\ell^r})\) with \(\operatorname{Pic}(X)[\ell^r]=J[\ell^r]\). The exact sequence and its maps are written in *Cohomology of curves*, §6, equations (6.1)–(6.4); its former stated Picard input is supplied by the actual Picard construction just bound above and the multiplication/torsion proofs in *Abelian varieties*, Theorems 6.2 and 7.2. Under reduction of coefficients the Kummer transition is multiplication by \(\ell\) on torsion. Taking the inverse limit gives the first identification.

Curve cup duality is proved for every invertible finite coefficient ring in *Poincaré duality for curves*, §§8–11, particularly Theorem 10.1, Corollary 10.2 and Theorem 11.1. Its §12 constructs the perfect cup pairing, without needing its separately stated comparison with a particular Weil-pairing convention. On the rational coefficient limit, graded commutativity gives alternation, since two is invertible even when \(\ell=2\). Twisting its trace once gives a perfect alternating form on \(V_\ell J\) into \(\mathbf Q_\ell(1)\). That form identifies \(V_\ell J(-1)\) with its dual and proves the second displayed identification. The projection formula for finite trace proves that pushforward is adjoint to pullback; the explicit trace and its compatibility with cup are in the same earlier lesson, §§2 and 7. Thus transposing a correspondence takes its adjoint.

For good specialization one can work directly on torsion. Multiplication by \(\ell^r\) on a smooth group has invertible differential, so its kernel on an abelian scheme is finite étale. Over a strictly henselian trait every finite étale scheme is a disjoint union of sections: lift each special point by the henselian root-lifting property, use the étale diagonal for uniqueness, and observe that their union has all the fibres and is the whole finite scheme. This argument is written in *Néron models*, Lemma 7.1. It identifies the torsion points compatibly for every \(r\), and inertia acts trivially. On a point of the special fibre, the \(p\)-power Frobenius endomorphism raises its coordinates to the \(p\)-th powers, exactly the action of arithmetic residue Frobenius. Taking the limit proves the claim. The cyclotomic character is unramified at \(p\ne\ell\) and has arithmetic Frobenius value \(p\), by Lesson 01, Lemma 0D.1, Proposition 0F.2 and Proposition 3.1. Galois equivariance of cup consequently gives multiplier \(p\) on the Tate-module pairing. ∎

**Lemma 1.4 (algebraically closed field extension in the degrees used here).** Let \(K\subset K'\) be algebraically closed fields, let \(X/K\) be a smooth projective connected curve, and let \(n\) be invertible in \(K\). Pullback gives an isomorphism
\[
 H^1_{\mathrm{\acute et}}(X,\mu_n)
 \xrightarrow{\ \sim\ }
 H^1_{\mathrm{\acute et}}(X_{K'},\mu_n).
\]
It preserves the degree-normalized trace in degree two, cup products, and finite curve correspondences. After compatible coefficient choices and passage to the limit it gives the degree-one \(\mathbf Q_\ell\) comparison needed to extend a geometric curve from \(\overline{\mathbf Q}\) to \(\mathbf C\).

*Proof.* Choose \(x\in X(K)\). The actual Picard construction in *The Picard functor and the Picard scheme of a curve*, Theorem 2.1, §§4–6 and Theorem 7.2, represents degree-zero line bundles normalized along \(x\), on every test scheme. Put \(J=\operatorname{Pic}^0_{X/K}\). Its base change represents that same functor for \(X_{K'}\): for any \(K'\)-scheme \(T\), a map \(T\to J_{K'}\) is precisely a \(K\)-map \(T\to J\), and
\[
 X_{K'}\times_{K'}T=X\times_KT.
\]
The bundle, its normalization along the section and its fibre degree in these two descriptions are identical. The functorial identifications commute with pullback, and therefore identify the representing schemes and their group laws. This proves the needed Jacobian base change directly from the written all-test-scheme Picard construction.

Global units on either projective connected curve are constants and have \(n\)-th roots in its algebraically closed field. The Kummer proof of Lemma 1.3 consequently gives the natural diagram
\
 \begin{array}{ccc}
 H^1_{\mathrm{\acute et}}(X,\mu_n)&\simeq&J[n\\
 \downarrow&&\downarrow\\
 H^1_{\mathrm{\acute et}}(X_{K'},\mu_n)&\simeq&J_{K'}n.
 \end{array}
\]
The scheme \(J[n]\) is finite étale by the multiplication proof used in Lemma 1.3. A finite étale algebra over an algebraically closed field is a product of copies of that field: its finite separable residue extensions are the field itself, and étaleness makes the local factors reduced. Tensoring this product with \(K'\) changes none of its component labels or group-law maps. Thus the right vertical arrow is a bijection and a group isomorphism, which proves the first assertion.

In degree two, *Poincaré duality for curves*, §2, identifies \(H^2(X,\mu_n)\) with \(\mathbf Z/n\) by divisor degree, and identifies the class of the point \(x\) with one. Its pullback is the point \(x_{K'}\), again of degree one. Naturality of the Kummer divisor class therefore makes pullback the identity under the two trace identifications. Pullback of cochains preserves cup products, so it also preserves their perfect degree-one pairing, whose proof was bound in Lemma 1.3.

For a finite generically étale map of smooth projective curves, pullback commutes with the field extension. Pushforward is its adjoint for this perfect cup pairing, by the finite trace projection formula proved in *Poincaré duality for curves*, §§2 and 7, as used in Lemma 1.3. An adjoint is unique: equality of its pairing against every vector determines the vector by perfection. The preserved pairings therefore make this pushforward commute with field extension.

Here is the additional argument for inseparable maps. A finite curve map in characteristic \(p\) factors into an iterated relative Frobenius \(h\), of degree \(d=p^r\), followed by a generically étale map. To check the factorization, a function field \(L\) of a smooth curve over the perfect field \(K\) has a separating parameter \(t\). Comparing the degrees over \(K(t^p)\) before and after the Frobenius field isomorphism gives \([L:L^p]=p\). Hence \(1,t,\ldots,t^{p-1}\) is a basis over \(L^p\), and differentiation shows \(\ker(d:L\to\Omega_{L/K})=L^p\). If the differential of a curve map vanishes, its pulled-back function field lies in \(L^p\), so its rational map factors through relative Frobenius. The rational factor extends at every point by the valuation rings of the smooth projective curves, as in Lemma 1.2. Each such factor removes a factor \(p\) from the finite degree, so this process terminates. The remaining map has nonzero differential; the differential exact sequence makes its relative differentials zero, and the minimal-polynomial derivative criterion makes its function-field extension separable.

The finite radicial map \(h\) is an integral universal homeomorphism. Its pullback induces an equivalence of étale topoi and therefore an isomorphism on these cohomology groups, by the actual strict-local proof in *Pushforward, pullback and finite morphisms*, Lemma 6.1 and Theorem 6.2. Define its degree-normalized pushforward by
\[
 h_*=d\,(h^*)^{-1}.
\]
This is the usual divisor normalization: the pullback of any point has length \(d\), so \(h^*\) multiplies the degree-two divisor class by \(d\), whereas the point's pushforward has degree one. The length assertion follows because a finite map of smooth curves is flat (a finite torsion-free module over a DVR is free), and a radicial fibre has one geometric point and total length its rank \(d\). Cup naturality then gives
\[
 \operatorname{tr}_X(h^*a\cup b)
 =d\,\operatorname{tr}_Y(a\cup(h^*)^{-1}b)
 =\operatorname{tr}_Y(a\cup h_*b).
\]
Thus this pushforward is also the required adjoint. Its formula commutes with algebraically closed field extension: pullback does and the finite flat degree \(d\) is preserved. Compose the radicial and generically étale pushforwards to obtain the adjoint, trace normalization and base-change compatibility for every finite curve map. Apply this to both projections of a finite correspondence; disconnected parameter curves are treated component by component. The correspondence action is consequently preserved.

Choose compatible primitive \(\ell^r\)-th roots in \(K\), also viewed in \(K'\), to identify constant coefficients with the corresponding twists. The finite comparison diagrams commute with coefficient reduction because Kummer does. Their inverse limits are isomorphic term by term; tensoring with \(\mathbf Q_\ell\) gives the rational degree-one identification. For \(K=\overline{\mathbf Q}\subset\mathbf C=K'\), combine this isomorphism with Lemma 1.2. This supplies the arithmetic application of the complex curve comparison, including the Hecke action and pairing used below. ∎

## 2. The Hecke correspondence over \(\mathbf Q\)

Fix a prime \(p\nmid N\). The correspondence has a parameter curve whose noncuspidal points are triples \((E,C,D)\), where \(D\subset E[p]\) is cyclic of order \(p\). Its two maps are
\[
\pi_1(E,C,D)=(E,C),\qquad
\pi_2(E,C,D)=\bigl(E/D,(C+D)/D\bigr).
\tag{6}
\]
They and their compactifications are defined over \(\mathbf Q\). Since \(p\nmid N\), the quotient map is injective on \(C\). In characteristic zero, \(E[p]\simeq(\mathbf Z/p)^2\), whose lines number
\[
\frac{p^2-1}{p-1}=p+1.
\tag{7}
\]
Thus both projections have generic degree \(p+1\).

On divisor classes and the Jacobian, our convention is
\[
T_p=(\pi_2)_*(\pi_1)^*.
\tag{8}
\]
Pullback includes the lengths of the fibers; pushforward then sends each divisor to its image. Replacing an isogeny by its dual exchanges the two projections: the composite is multiplication by \(p\), and multiplication by \(p\) preserves the cyclic subgroup \(C\). Consequently this correspondence on \(X_0(N)\) equals its transpose. The induced Hecke action on differentials is the classical action, with
\[
(T_pf)(z)=p\,f(pz)+\frac1p\sum_{j=0}^{p-1}
f\!\left(\frac{z+j}{p}\right).
\tag{9}
\]
For \(f=\sum_{n\ge1}b_nq^n\), the finite sum kills terms whose index is not divisible by \(p\), so the coefficient of \(q^n\) is
\[
b_{pn}+p\,b_{n/p},
\qquad b_{n/p}=0\ \text{if }p\nmid n.
\tag{10}
\]
In particular, a normalized eigenform \(f=q+\cdots\) has \(T_p\)-eigenvalue \(b_p\).

**Lemma 2.1 (normalization and the actual Hecke prerequisites).** The differential action of (8) is (9). The good-prime operators commute, are self-adjoint for the Petersson inner product, and have algebraic integer eigenvalues. They admit a common eigenbasis.

*Proof.* Present a complex elliptic curve by \(\mathbf C/(\mathbf Z+\mathbf Z z)\). Its order-\(p\) kernels are generated by \(1/p\), and by \((z+j)/p\), \(0\le j<p\). Quotient by the first has parameter \(pz\); quotient by the others has parameters \((z+j)/p\). On differentials of the parameter curve, the sum of pullbacks of \(f(w)\,dw\) is therefore
\[
 \left(pf(pz)+\frac1p\sum_jf((z+j)/p)\right)dz.
\]
This is exactly the transpose correspondence on differentials. Since the cyclic-level correspondence equals its transpose, it is also (8). This argument checks the factor at weight two directly; the invariant-differential version for general weight is actually proved in the earlier *Complex tori, elliptic curves and the moduli interpretation of modular curves*, Theorem 5.1.

The complete commutation and adjoint proofs, including unfolding the two finite-index fundamental domains, are in *Hecke operators for \(\Gamma_0(N)\) and \(\Gamma_1(N)\)*, Theorem 3.1, Lemma 4.1 and Theorem 4.2. Its last proof diagonalizes the whole commuting normal family, even an infinitely indexed family, by successively splitting finite-dimensional invariant eigenspaces. In trivial character the adjoint is \(T_p\), so all eigenvalues are real.

For algebraicity there is an integral cohomological proof before any arithmetic coefficient bound: *Modular symbols and the algebraicity of Hecke eigenvalues*, §1 and §2.2. Its formula (1.3) acts by integral coset transitions on cocycles and (1.8) identifies that action with periods. The finite-generator cocycle equations give a full integral lattice in rational parabolic cohomology. Reflection \(z\mapsto-\bar z\) commutes with Hecke and exchanges the two summands of (5); its positive rational eigenspace is isomorphic to the cusp-form space. The intersection with the integral lattice is a full Hecke-stable lattice. This construction also applies directly to \(\Gamma_0(N)\): alternatively take the diamond-invariant rational subspace of the \(\Gamma_1(N)\) construction and intersect its full lattice. The invariant subspace is rational because the finitely many diamond equations have integer matrices. Reflection still exchanges its two analytic summands. Each \(T_p\) is an integer matrix on the resulting positive lattice, so its monic characteristic polynomial on \(S_2(\Gamma_0(N))\) is integral. Every eigenvalue is an algebraic integer. No arithmetic Sturm theorem or future newform construction is used. ∎

Choose the common eigenbasis \(f_1,\ldots,f_g\). Write
\[
T_pf_j=a_p(f_j)f_j.
\tag{11}
\]
Here \(a_p(f_j)\) means the eigenvalue. If a basis vector is an oldform without first Fourier coefficient one, it does not mean its literal \(p\)th coefficient. Oldform multiplicities are included in this basis and in every product below.

By (5), the eigenvalue \(a\) of \(T_p\) of multiplicity \(m_a\) on \(S_2\) has multiplicity \(2m_a\) on the rational cohomology after extension to a splitting field. The eigenvalues are real, so the conjugate summand has the same spectrum. Comparison transfers this statement to the étale cohomology and, by duality, to \(V_\ell J\).

## 3. Ordinary \(p\)-torsion: points and fiber lengths

Let \(k=\overline{\mathbf F}_p\). An elliptic curve is ordinary when its geometric \(p\)-torsion has \(p\) points.

**Lemma 3.0 (the ordinary torsion structure).** An ordinary elliptic curve has
\[
E[p]\simeq \mu_p\times(\mathbf Z/p)_k.
\tag{12}
\]
The connected factor is \(\ker(F_E:E\to E^{(p)})\).

*Proof.* Relative Frobenius is radicial of degree \(p\), and its Verschiebung has degree \(p\), with \(VF=[p]\). These assertions, including the coordinate proof of Frobenius degree and the construction of Verschiebung, are actually proved in *Abelian varieties*, Theorems 8.2–8.4. Frobenius is a bijection on geometric points. Consequently the \(p\) geometric points of \(E[p]\) map to \(p\) distinct points of \(\ker V\). Its coordinate algebra has dimension \(p\), so these exhaust it and it is reduced, hence the constant group \(\mathbf Z/p\).

For an elliptic curve, \(E\simeq\operatorname{Pic}^0(E)\) by \(x\mapsto\mathcal O(x-0)\). This is an isomorphism of schemes, not just a bijection on points: the degree-one Abel fibre in *The Picard functor and the Picard scheme of a curve*, Proposition 7.1, is the projectivization of a one-dimensional section space, and its universal evaluation identifies the degree-one Picard scheme with \(E\). Translation identifies degree one with degree zero. The Cartier-dual-kernel theorem and Frobenius-duality proof in *Abelian varieties*, Theorem 6.34 and Proposition 6.42, therefore identify \(\ker F\) with \((\ker V)^D=\mu_p\). The equality \((\mathbf Z/p)^D=\mu_p\) follows on every algebra by sending a character to the image \(z\) of its generator, with the sole relation \(z^p=1\).

The reduced \(p\)-torsion points give a constant subgroup \(H\simeq\mathbf Z/p\) of \(E[p]\). It intersects the connected \(\ker F\) only in the identity scheme: each component of \(H\) is reduced and the only component meeting the connected kernel is its identity. Addition \(\ker F\times H\to E[p]\) is an isomorphism. Indeed the translates of the connected kernel by those \(p\) points are disjoint closed length-\(p\) subschemes. Their lengths total \(p^2\), the degree of \([p]\), so the induced closed immersion exhausts the coordinate algebra on each Artinian component. This proves (12). ∎

A subgroup here means a closed finite subgroup **scheme**, and its order means its rank. The scheme \(\mu_p\) has rank \(p\) but only one geometric point.

**Proposition 3.1.** The group scheme in (12) has exactly two subgroup schemes of rank \(p\): \(\mu_p\times0\), which is connected, and \(1\times(\mathbf Z/p)_k\), which is étale.

*Proof.* Let \(H\) have rank \(p\). Its group of geometric points injects into \((\mathbf Z/p)(k)\), so it has either one or \(p\) points. If it has one, \(H\) is connected. Its map to the constant group is trivial, since a connected scheme cannot map to different open-and-closed components and the identity maps to zero. Hence \(H\subset\mu_p\), and equality follows from their equal ranks.

If it has \(p\) points, its finite coordinate algebra has dimension \(p\) and at least \(p\) reduced geometric points, so it is reduced and étale. Its projection to \(\mathbf Z/p\) is an isomorphism; \(H\) is therefore the graph of a homomorphism \((\mathbf Z/p)_k\to\mu_p\). Such a homomorphism is trivial, because each of its \(p\) reduced points maps to the only \(k\)-point of \(\mu_p\). This gives the second subgroup and exhausts all possibilities. ∎

This calculation also determines the missing multiplicity. Let \(\mathcal S\) be the functor parameterizing finite locally free rank-\(p\) subgroups of the fixed group in (12). The next proof constructs its representing scheme; its existence does not have to be borrowed from the full modular-curve construction.

**Proposition 3.2.** As a \(k\)-scheme,
\[
\mathcal S\simeq\operatorname{Spec}k\ \amalg\ \mu_p.
\tag{13}
\]
The point representing the connected subgroup has length one; the point representing the étale subgroup has length \(p\).

*Proof.* Proposition 3.1 gives the two points. Compute their infinitesimal neighborhoods over any local Artinian \(k\)-algebra \(R\) with residue field \(k\).

A finite flat subgroup \(H_R\) reducing to \(\mu_p\) is topologically connected, since a nilpotent thickening has the same underlying topological space as its special fiber. Its projection to the constant group is trivial. Thus \(H_R\subset\mu_{p,R}\), and the inclusion is an equality. Indeed, the induced surjection of coordinate algebras is a map between free \(R\)-modules of the same rank, and is an isomorphism after reduction; its determinant is a unit. This subgroup has no nontrivial deformation.

A subgroup reducing to \((\mathbf Z/p)_k\) is étale over \(R\): its relative differentials vanish after reduction, hence vanish by Nakayama’s lemma, and it is finite flat. Its projection to \((\mathbf Z/p)_R\) is an isomorphism, again by reduction and the determinant argument. Such a subgroup is exactly the graph of a homomorphism
\[
(\mathbf Z/p)_R\longrightarrow\mu_{p,R}.
\]
The homomorphism is determined by the image \(z\) of the generator, and the only condition is \(z^p=1\). Write \(z=1+u\). In characteristic \(p\), this condition is \(u^p=0\). The local deformation ring is \(k[u]/(u^p)\).

These arguments actually work over an arbitrary local \(k\)-algebra \(R\), after extending its residue field algebraically. The inverse images in \(H_R\) of the components of \((\mathbf Z/p)_R\) are direct summands of its finite free coordinate module. In the connected special-fibre case, all summands except the zero component vanish modulo the maximal ideal and hence vanish by Nakayama. In the étale special-fibre case, relative differentials vanish by Nakayama and the projection is a determinant-unit isomorphism. Thus every local family belongs to exactly one of the two displayed functors. Their choice is locally constant on any base, since the ranks of those direct summands are locally constant. The descriptions glue on arbitrary bases: one branch has the unique subgroup \(\mu_p\), and the other is the graph of a uniquely specified element of \(\mu_p(R)\). This constructs the representing scheme \(\operatorname{Spec}k\amalg\mu_p\) on all test schemes. Its two rings are \(k\) and \(k[u]/(u^p)\), proving (13) and both lengths. ∎

There are thus two geometric subgroups, counted with total parameter length \(1+p\). The characteristic-zero \(p+1\) lines do not become \(p+1\) distinct subgroup schemes in the special fiber. The \(p\) nonconnected choices merge into the length-\(p\) infinitesimal neighborhood of the single étale subgroup.

This corrects an erroneous count in the freely accessible original of Deligne’s Bourbaki text, Proposition 3.15 proof, printed p.157: its characteristic-\(p\) count of one subgroup applies to the supersingular case, but not the ordinary case. Proposition 4.3 of the same work distinguishes the two ordinary branches correctly. The free original Deligne–Rapoport text, V.1, proof of Theorem 1.6 and Lemma 1.12, gives precisely the fiber (13). The proofs above independently construct the ordinary fibre.

## 4. Reduction of the correspondence and the congruence relation

**Lemma 4.0 (the integral modular polynomial and Kronecker congruence).** For every prime \(p\), there is a monic integral modular polynomial, of degree \(p+1\) in its target variable, and
\[
 \Phi_p(X,Y)\equiv (X-Y^p)(X^p-Y)\pmod p.
\]

*Proof.* The actual earlier proof of the \(j\)-coordinate and function field is *The valence formula and the ring of modular forms of level one*, Theorem 3.1. Its Theorem 4.1 proves the discriminant product, and *Modular forms, lattice functions and Eisenstein series*, Theorem 4.2, proves the integral Fourier series of \(E_4\). Hence
\(j=q^{-1}+744+\cdots\in\mathbf Z((q))\). Form the polynomial
\[
 P(X,z)=(X-j(pz))\prod_{b=0}^{p-1}
              \left(X-j((z+b)/p)\right).
\]
Its roots are the target invariants of all degree-\(p\) quotients. Changing the lattice basis permutes the kernels, so every coefficient is an invariant meromorphic function on \(X(1)\), holomorphic away from its cusp. It is thus a polynomial in \(j(z)\), by the proved coordinate theorem. This defines \(\Phi_p(X,Y)\) over \(\mathbf C\), monic of degree \(p+1\) in \(X\).

For completeness this is the symmetric modular equation, rather than a polynomial with an unnoticed repeated correspondence. A generic complex elliptic curve has endomorphism ring \(\mathbf Z\): a nonscalar lattice endomorphism of \(\mathbf Z+\mathbf Zz\) forces a nonzero quadratic equation over \(\mathbf Q\) for \(z\). If two distinct order-\(p\) kernels gave isomorphic quotients, composing one quotient isogeny, that isomorphism and the dual of the other would give a degree-\(p^2\) endomorphism. On such a generic curve it is \(\pm[p]\); canceling the isogeny then shows the two kernels agree. The target roots are therefore generically distinct. Reduction of integral matrices onto \(\operatorname{SL}_2(\mathbf F_p)\), proved in the earlier congruence-subgroup lesson, acts transitively on their kernel lines. Analytic continuation consequently makes \(\Phi_p\) irreducible over \(\mathbf C(Y)\). Duality preserves its zero set after exchanging \(X,Y\), so irreducibility gives equality up to a constant. In the expansion at infinity, its constant-in-\(X\) term has leading term \(q^{-(p+1)}\), with coefficient one; every other coefficient has smaller pole order, because it omits at least one target root. Hence the leading \(Y\)-coefficient is also one and the degree in \(Y\) is \(p+1\). Exchanging variables preserves the two monic normalizations, so the constant is one. This proves symmetry.

To prove integrality, expand with \(r=q^{1/p}\) and a primitive root \(\zeta_p\). Each root has Laurent coefficients in \(\mathbf Z[\zeta_p]\). The Laurent expansions of the symmetric coefficients are invariant under \(r\mapsto\zeta_pr\), so only integral powers of \(q\) occur. They are also invariant under every automorphism of \(\mathbf Q(\zeta_p)\), which permutes the \(p\) translated roots. Their coefficients are rational algebraic integers, hence integers; the latter elementary assertion is proved by the rational-root denominator argument for a monic polynomial. A polynomial in \(j\) with integral Laurent expansion has integral polynomial coefficients: subtract its leading Laurent coefficient times the matching power of \(j\), reducing its pole order, and continue to the constant. Thus \(\Phi_p\in\mathbf Z[X,Y]\). The dual-isogeny bijection makes its zero correspondence symmetric. No assumption that two distinct isogenies always have distinct pairs of invariants has been made.

Reduce the product in \(\mathbf Z\zeta_p)\) modulo \(1-\zeta_p\); its residue field is \(\mathbf F_p\). The first target series becomes \(j(q^p)=j(q)^p\). The \(p\) remaining series all become \(j(r)\), and their product becomes
\((X-j(r))^p=X^p-j(q)\). Therefore
\[
 \Phi_p(X,j(q))=(X-j(q)^p)(X^p-j(q))
       \quad\hbox{in }\mathbf F_p((q))[X].
\]
Substitution \(Y\mapsto j(q)\) is injective on \(\mathbf F_p[Y]\): a nonzero polynomial of degree \(d\) has nonzero leading Laurent coefficient at \(q^{-d}\). This proves the polynomial congruence, including \(p=2,3\). ∎

The following stronger reduction theorem remains a required geometric theorem. For \(p\nmid N\), the special fiber of the compactified degree-\(p\) correspondence is reduced, with two components whose normalizations are copies of \(X_0(N)_{\mathbf F_p}\). They meet at the supersingular points. On the ordinary locus, the two components describe the Frobenius isogeny and its dual. In particular, for \(N=1\), \(X_0(p)_{\mathbf F_p}\) consists of two copies of \(X(1)_{\mathbf F_p}=\mathbf P^1_{\mathbf F_p}\), glued at the supersingular points. This describes the Deligne–Rapoport model; resolving its total-space singularities can add exceptional components to a regular model. The polynomial lemma proves the plane-image congruence independently, but its normalization cannot supply this compact moduli theorem: normalization and reduction need not commute. The remaining construction and supersingular deformation obligations are recorded in §7.

Put \(\mathcal F:X_{\mathbf F_p}\to X_{\mathbf F_p}\) for the \(p\)-power Frobenius morphism. It has degree \(p\). The special-fiber correspondence cycle is
\[
\Gamma_{\mathcal F}+\Gamma_{\mathcal F}^{\,t}.
\tag{14}
\]
Here a graph \(\Gamma_h\) has first projection the identity and second projection \(h\); the superscript \(t\) exchanges projections.

The ordinary moduli explanation is explicit. Quotient by the connected subgroup is
\[
(E,C)\longmapsto(E^{(p)},C^{(p)}),
\tag{15}
\]
the Frobenius branch. For the étale subgroup, the quotient is the Verschiebung isogeny from \(E\) to \(E^{(1/p)}\); its dual is Frobenius. The prime-to-\(p\) level subgroup on the quotient is \(C^{(1/p)}\), since the composite is \([p]\) and this multiplication preserves \(C\). This is the transposed branch.

On a geometric ordinary point \(x\), (14) gives the divisor
\[
[\mathcal F(x)]+p[\mathcal F^{-1}(x)].
\tag{16}
\]
The second coefficient is a fiber length, not a count of \(p\) distinct étale subgroups. The Frobenius morphism is purely inseparable of degree \(p\), so its pullback of a point has length \(p\). This agrees with Proposition 3.2. The reduction theorem supplies the two components with multiplicity one; equality on their dense ordinary loci gives (14) as a cycle. Their isolated supersingular intersections do not contribute another one-dimensional component.

Let \(F=\mathcal F_*\) be the induced Frobenius endomorphism of \(J_{\mathbf F_p}\), and let \(V=\mathcal F^*\) on divisor classes. Pushforward followed by pullback, and the reverse composite for this purely inseparable map, give multiplication by \(p\). Thus (14) induces the **Eichler–Shimura congruence relation**
\[
T_p=F+V,\qquad FV=VF=[p].
\tag{17}
\]
The extension of the moduli correspondence over the cusps and supersingular points is part of the stated geometric theorem. The ordinary calculation explains its two terms and their multiplicities.

Choose \(\ell\ne p\). Good reduction identifies the Tate module of \(J\) with that of its special fiber. On \(V_\ell J\), the endomorphism \(F\) is the action of **arithmetic** Frobenius \(\mathrm{Fr}_p\). Hence
\[
T_p=F+pF^{-1},\qquad F^2-T_pF+p=0.
\tag{18}
\]
On
\[
W_\ell=H^1_{\mathrm{\acute et}}(X_{\overline{\mathbf Q}},\mathbf Q_\ell)
\simeq(V_\ell J)^\vee,
\tag{19}
\]
geometric Frobenius \(\Phi_p=\mathrm{Fr}_p^{-1}\) has the transpose of the arithmetic Frobenius matrix on \(V_\ell J\). Their characteristic polynomials therefore agree. Cup product gives a nondegenerate alternating pairing on \(W_\ell\) valued in \(\mathbf Q_\ell(-1)\). Geometric Frobenius acts on that target by \(p\), so its operator, again denoted \(F\), satisfies
\[
\langle Fx,Fy\rangle=p\langle x,y\rangle.
\tag{20}
\]
Equation (18) holds on this cohomology with that geometric operator. Equivalently \(V=pF^{-1}\) is the adjoint of \(F\), and \(T_p=F+V\) is self-adjoint for this alternating pairing.

These conventions agree with the preceding lessons: \(\Phi_p\) has local norm \(p^{-1}\), and geometric local reciprocity sends a uniformizer to \(\Phi_p\). The global weight-two Euler polynomial uses arithmetic Frobenius on the covariant Tate module.

## 5. The characteristic polynomial and the trace

Equation (18) is an annihilating polynomial. By itself it does not specify the multiplicities of its two roots. For example, over a field containing distinct roots \(\alpha,\beta\) with \(\alpha\beta=p\), the operators
\[
F=\alpha I_2,\qquad V=\beta I_2,\qquad
T=(\alpha+\beta)I_2
\tag{21}
\]
obey \(T=F+V\) and \(FV=p\), but the characteristic polynomial of \(F\) is \((X-\alpha)^2\). The missing information in this example is the nondegenerate pairing with multiplier \(p\). We now use that information and the Hecke multiplicities to prove the desired result.

**Theorem 5.1.** For \(p\nmid N\ell\), arithmetic Frobenius on \(V_\ell J_0(N)\) has characteristic polynomial
\[
\det(X-\mathrm{Fr}_p\mid V_\ell J_0(N))
=\prod_{j=1}^g\bigl(X^2-a_p(f_j)X+p\bigr).
\tag{22}
\]
The basis is any good-prime Hecke eigenbasis of \(S_2(\Gamma_0(N))\), with its full multiplicities. In particular,
\[
\operatorname{tr}(\mathrm{Fr}_p\mid V_\ell J_0(N))
=\operatorname{tr}(T_p\mid S_2(\Gamma_0(N))),
\qquad
\det(\mathrm{Fr}_p\mid V_\ell J_0(N))=p^g.
\tag{23}
\]

*Proof.* Work first on \(W_\ell\) with geometric Frobenius. Extend coefficients to an algebraic closure of \(\mathbf Q_\ell\), using an embedding of the algebraic Hecke eigenvalues. Characteristic polynomials can be computed after this extension. The comparison and Hecke decomposition in §2 show that \(T_p\) is semisimple and that its eigenspace \(U_a\) has dimension \(2m_a\), where \(m_a\) is the multiplicity of \(a\) on \(S_2\).

Distinct \(T_p\)-eigenspaces are orthogonal. Indeed, self-adjointness gives
\[
a\langle x,y\rangle
=\langle T_px,y\rangle
=\langle x,T_py\rangle
=b\langle x,y\rangle
\]
for \(x\in U_a\), \(y\in U_b\). If \(a\ne b\), the pairing vanishes. Its restriction to each \(U_a\) is therefore nondegenerate: a vector in its radical would pair trivially with all eigenspaces and hence with the whole space.

Since \(F\) commutes with \(T_p=F+pF^{-1}\), it preserves \(U_a\). On that space,
\[
F^2-aF+p=0.
\tag{24}
\]
Let \(\alpha,\beta\) be the roots, so \(\alpha+\beta=a\) and \(\alpha\beta=p\).

If \(\alpha\ne\beta\), the annihilating polynomial is separable, and \(U_a=U_\alpha\oplus U_\beta\) is the eigenspace decomposition for \(F\). For \(x\in U_\lambda\), \(y\in U_\mu\), (20) implies
\[
(\lambda\mu-p)\langle x,y\rangle=0.
\tag{25}
\]
Neither \(\alpha^2\) nor \(\beta^2\) equals \(p\), because such an equality would make the roots equal. Consequently each of \(U_\alpha,U_\beta\) is isotropic, and nondegeneracy on \(U_a\) makes the cross-pairing perfect. They have equal dimension, necessarily \(m_a\). The characteristic polynomial on \(U_a\) is
\[
(X-\alpha)^{m_a}(X-\beta)^{m_a}
=(X^2-aX+p)^{m_a}.
\]

If \(\alpha=\beta\), (24) says \((F-\alpha)^2=0\). All \(2m_a\) characteristic roots are \(\alpha\), even if the matrix has nontrivial Jordan blocks. Its characteristic polynomial is again
\[
(X-\alpha)^{2m_a}=(X^2-aX+p)^{m_a}.
\]
Thus no unproved Frobenius semisimplicity assertion is needed for this step.

Multiplying over \(a\) proves the polynomial on \(W_\ell\). Equation (19) identifies its geometric Frobenius matrix with the transpose of arithmetic Frobenius on \(V_\ell J\), proving (22). Each quadratic contributes trace \(a\) and determinant \(p\); this gives (23). ∎

The trace can also be checked directly. The adjoint \(V\) of \(F\) has the same trace as \(F\), since its matrix is conjugate to \(F^t\). Taking traces in (17) gives
\[
\operatorname{tr}(T_p\mid W_\ell)=2\operatorname{tr}(F\mid W_\ell).
\tag{26}
\]
But (5) gives \(\operatorname{tr}(T_p\mid W_\ell)=2\operatorname{tr}(T_p\mid S_2)\). Cancelling the two proves precisely (23). Taking the trace on \(S_2\oplus\overline{S_2}\) without this division would give an incorrect factor of two.

Equivalently, the good-prime Euler polynomial is
\[
\det(1-\mathrm{Fr}_p\,t\mid V_\ell J)
=\prod_{j=1}^g(1-a_p(f_j)t+pt^2).
\tag{27}
\]
The coefficients on the left are independent of \(\ell\): the right uses the classical algebraic Hecke eigenvalues, with their multiplicities. The identity concerns the entire Jacobian. Extracting the two-dimensional representation for one newform requires a Hecke quotient, which is the subject of the next lesson.

## 6. The genus-one example \(X_0(11)\)

A model of \(X_0(11)\), with the cusp \(\infty\) as the elliptic-curve origin, is
\[
y^2+y=x^3-x^2-10x-20.
\tag{28}
\]
Here is an explicit proof of the modular identification, using the actually proved earlier analytic inputs. The functions are constructed independently from the freely accessible calculation in Weston, *The modular curves \(X_0(11)\) and \(X_1(11)\)*, §4, pp.8–11; all their modularity and pole conditions are supplied below.

**Proposition 6.1 (the level-eleven model and form).** The compact analytic modular curve is the nonsingular cubic (28), with \(\infty\) as its origin. For its arithmetic model in §1 this identification descends to \(\mathbf Q\), once that model's rational Tate cusp has been constructed. The form in (32) spans \(S_2(\Gamma_0(11))\).

*Proof.* The complete eta multiplier computation and both cusp expansions are actually written in *Hecke operators for \(\Gamma_0(N)\) and \(\Gamma_1(N)\)*, §6. That proof starts from \(H=\eta^2\), \(H^{12}=\Delta\), and the character values \(\mu(T)=e^{2\pi i/12}\), \(\mu(S)=-i\). It gives coset-transition generators for all of \(\Gamma_0(11)\) and checks \(\mu(\gamma)\mu(\operatorname{diag}(11,1)\gamma\operatorname{diag}(11^{-1},1))=1\) on each generator. It also proves that
\[
 h=\eta(z)^2\eta(11z)^2
\]
has order exactly one at both cusps and no zero in the half-plane. Its valence argument proves the cusp space is exactly one-dimensional, without importing an unproved dimension assertion. The earlier genus proof gives index twelve, two cusps and no elliptic points, hence genus one by *Modular curves and their genus*, Theorem 3.3 and §4.

Use the Eisenstein series
\[
 A(z)=\frac{11E_2(11z)-E_2(z)}{10}
 =1+\frac{12}{5}\sum_{n\ge1}\sigma_1(n)q^n
       -\frac{132}{5}\sum_{n\ge1}\sigma_1(n)q^{11n}.
\]
Its weight-two modularity and all cusp conditions are proved in the earlier Hecke lesson, §7, proof of (7.3), from the explicitly proved \(E_2\) transformation law. Put
\[
 u=A/h+8/5,\qquad v=\frac{q\,du/dq}{h}.
\]
The derivative of a weight-zero function transforms with weight two, so both functions are modular functions. They have no poles in the half-plane, because \(h\) is nonzero there.

Let \(wz=-1/(11z)\). Conjugation by \(w\) preserves \(\Gamma_0(11)\) and exchanges its two cusps. The eta transformation already proved gives \(h(wz)=-11z^2h(z)\). Substitution in the proved \(E_2\) law gives \(A(wz)=-11z^2A(z)\): the two nonmodular linear terms cancel. Hence \(u\circ w=u\). Differentiating this identity gives \(u'(wz)=11z^2u'(z)\), and therefore \(v\circ w=-v\). This verifies the other cusp without a theta transformation premise.

Define
\[
 \begin{split}
 x_0&=(u^2-v-10u)/2,\\
 y_0&=(-uv+u^3-10u^2-22u)/2.
 \end{split}
\]
The product for \(h\) and the displayed series for \(A\) give
\[
 \begin{split}
 u&=q^{-1}+6+17q+46q^2+116q^3+252q^4+533q^5+
                 1034q^6+1961q^7+O(q^8),\\
 v&=-q^{-2}-2q^{-1}+12+116q+597q^2+2298q^3+
                 7616q^4+22396q^5+O(q^6),\\
 x_0&=q^{-2}+2q^{-1}-1+5q+8q^2+q^3+7q^4-11q^5+O(q^6),\\
 y_0&=q^{-3}+8q^{-2}+17q^{-1}+13+42q+66q^2+
                 24q^3+72q^4+O(q^5).
 \end{split}
\]
For reproducibility, coefficients of the product are computed by
\(c_r^{(n)}=c_r^{(n-1)}-2c_{r-n}^{(n-1)}+c_{r-2n}^{(n-1)}\), with negative indices zero; division by \(h/q\), whose constant is one, is the recursion
\(d_r=a_r-\sum_{i=1}^r c_i d_{r-i}\). These two recursions, followed by differentiation, give every displayed coefficient by finite rational arithmetic.

At the other cusp replace \(v\) by \(-v\). The negative terms cancel and give
\[
 x_0\circ w=11+121q+O(q^2),\qquad
 y_0\circ w=121+1331q+O(q^2).
\]
Thus \(x_0,y_0\) have their only poles at \(\infty\), of orders two and three. The function
\[
 R=y_0^2-x_0^3-10x_0y_0+11x_0^2-11y_0
\]
has no pole elsewhere and a possible pole of order at most six at \(\infty\). Substitution of the displayed expansions gives coefficient zero at every exponent \(-6,-5,\ldots,0\). To see that the finite truncations suffice, the constant of \(x_0^3\) uses \(x_0\) only through \(q^4\), and that of \(y_0^2\) uses \(y_0\) only through \(q^3\); all other terms require fewer coefficients. Hence \(R\) is globally holomorphic and has constant term zero. The compact-curve maximum principle makes it the constant zero. We have proved
\[
 y_0^2-10x_0y_0-11y_0=x_0^3-11x_0^2.
\]

The pole divisor of \(x_0\) has degree two, so its map to the sphere has degree two by the local-power and fibre-degree proof in the earlier analytic Appendix A.7. Moreover \(y_0\notin\mathbf C(x_0)\): a rational function of \(x_0\) with no pole above a finite value of \(x_0\) is a polynomial, whereas every polynomial has even pole order at \(\infty\). The sole pole of \(y_0\) has order three. Thus \(\mathbf C(X_0(11))=\mathbf C(x_0,y_0)\), a quadratic extension of \(\mathbf C(x_0)\). Set
\[
 x=x_0+5,\qquad y=y_0-5x_0-6.
\]
Direct substitution gives (28). Its discriminant computed in (29) is nonzero, so its projective cubic is nonsingular. Equality of the function fields makes the resulting map an isomorphism: the discrete valuation local rings of smooth projective curves extend a birational map and its inverse at every point. The only pole point maps to the cubic's origin.

For descent, Lemma 1.2 makes these meromorphic functions rational on the algebraic complex curve. Their Laurent expansions in the rational Tate parameter at \(\infty\) have rational coefficients. In a finite-dimensional rational section space \(H^0(X,\mathcal O(m\infty))\), expansion in that parameter is an injective rational linear map. A finite set of coefficients is already injective, since descending kernels in a finite-dimensional space stabilize; its matrix has rational entries. Solving for a section from these rational coefficients therefore gives rational coordinates in a rational basis. Thus \(x,y\) descend to \(\mathbf Q\), and so does the isomorphism. This last descent uses the rational arithmetic cusp from the still-required general model theorem; its exact unresolved construction is retained in §7. ∎

For (28), the standard Weierstrass formulas give
\[
b_2=-4,\quad b_4=-20,\quad b_6=-79,\quad b_8=-21,
\qquad c_4=496,\quad\Delta=-11^5.
\tag{29}
\]
The discriminant is a unit at every \(p\ne11\), so this is a smooth genus-one curve there. Its rational origin identifies it with its Jacobian. Hence \(g=1\), and the unique normalized weight-two eigenform at level 11 has
\[
\#X_0(11)(\mathbf F_p)=p+1-a_p,\qquad p\ne11.
\tag{30}
\]
This is the elliptic-curve Frobenius formula proved earlier, together with (22).

Here are complete small-prime counts. The entry in the third column lists the number of \(y\)-solutions as \(x\) runs through the field in increasing residue order. Add one for the origin at infinity.

| \(p\) | Values of \(x^3-x^2-10x-20\) modulo \(p\) | Number of \(y\)-solutions for each \(x\) | Total points | \(a_p\) |
|---:|---|---|---:|---:|
| 2 | \(0,0\) | \(2,2\) | 5 | \(-2\) |
| 3 | \(1,0,0\) | \(0,2,2\) | 5 | \(-1\) |
| 5 | \(0,0,4,3,3\) | \(2,2,0,0,0\) | 5 | \(1\) |

For verification, \(y^2+y\) takes the values \(0,0\) at \(p=2\), \(0,2,0\) at \(p=3\), and \(0,2,1,2,0\) at \(p=5\). Thus the three Frobenius polynomials are
\[
X^2+2X+2,\qquad X^2+X+3,\qquad X^2-X+5.
\tag{31}
\]
They all have constant term \(p\), and their traces agree with \(a_2=-2\), \(a_3=-1\), \(a_5=1\).

One may check these coefficients on the classical form
\[
f(z)=\eta(z)^2\eta(11z)^2
=q\prod_{n\ge1}(1-q^n)^2(1-q^{11n})^2
=q-2q^2-q^3+2q^4+q^5+2q^6-2q^7+\cdots.
\tag{32}
\]
Its membership in the one-dimensional cusp-form space is proved by the actual earlier eta calculation bound in Proposition 6.1. The displayed coefficients can be computed by finite multiplication: through degree seven only the factors \(n\le6\) in the first product contribute, and the second product contributes its constant term. Thus (32) checks the point counts, whose modular-curve identification was established by the functions above.

The earlier curve \(y^2+y=x^3-x^2\) is not the model (28). Their \(j\)-invariants are respectively \(-4096/11\) and \(-496^3/11^5\), so they are not isomorphic over \(\overline{\mathbf Q}\). Identifying a modular curve requires the modular construction, even when two elliptic curves happen to have the same initial good-prime traces.

## 7. Written proof bindings and remaining construction obligations

The proofs are now ordered before their uses. Lemma 1.0 proves the finite-level étale and tame interior calculations; Lemmas 1.2–1.3 give the particular curve comparison, Tate realization, cup pairing and good specialization; Lemma 2.1 binds the actual integral Hecke and adjoint proofs; Lemma 3.0 proves ordinary torsion, and Propositions 3.1–3.2 construct its subgroup scheme on all test bases. Lemma 4.0 proves the integral modular-polynomial congruence independently of a reduction-model citation. Theorem 5.1 retains its complete multiplicity argument. Proposition 6.1 gives explicit generators and the cubic relation for level eleven, together with the actual earlier proof of eta modularity. All exercise solutions remain written below.

There are still two substantial arithmetic construction obligations. The general model theorem needs an actual construction of the elliptic moduli stack, the fine full-level schemes, the compactification and the coarse curves, including the wild invariant charts in characteristics two and three. The formal Tate parameter and rationality of the chosen arithmetic cusp also belong to that construction. The free original Deligne–Rapoport text supplies material in III.2, IV.2–IV.3, VI.6 Proposition 6.7 and VII.1–VII.2. Reading that material is not a replacement for writing or binding those proofs. The relative Picard construction over the resulting smooth proper integral curve model is also needed to turn its field Jacobians into an abelian scheme over \(\mathbf Z[1/N]\). The actual earlier field Picard construction in *The Picard functor and the Picard scheme of a curve*, §§4–7, proves the field statement; it alone does not prove this relative extension.

The other obligation is the full compactified degree-\(p\) correspondence and its supersingular deformation calculation. The ordinary parameter fibre is fully proved here. The free original Deligne–Rapoport V.1.6–V.1.18 and VI.6.9–VI.6.10 describe the remaining construction, finite flatness, reducedness and coarse specialization. A proof must supply the supersingular fibre calculation, the Cohen–Macaulay argument excluding embedded components, the two global closed branch maps, and their coarse descent, before the cycle (14) has been established at arbitrary level. The ordinary argument alone does not prove those assertions. Accordingly the full congruence theorem (17)–(18) and Theorem 5.1 remain dependent on these unclosed core geometric theorems. Their original generality is retained; this lesson is not yet certified to satisfy the requirement that every used result have an actual earlier or local proof.

For point level the dual isogeny retains the changed generator, rather than merely its cyclic span. The good-prime formula therefore has the diamond term
\[
T_p=\mathrm{Fr}_p+p\langle p\rangle\mathrm{Fr}_p^{-1}.
\tag{33}
\]
The normalization of the point diamond and its classical term are actually checked in the earlier *Hecke operators for \(\Gamma_0(N)\) and \(\Gamma_1(N)\)*, Lemma 2.1 and Theorem 2.3, and in *Complex tori, elliptic curves and the moduli interpretation of modular curves*, §5. The two special branches transport the point through Frobenius and dual Frobenius; their double dual changes it by multiplication by \(p\), giving the displayed diamond in the same convention. This argument still has the global special-fibre construction dependency just specified. The diamond acts trivially on the \(\Gamma_0(N)\) space with trivial character, giving (18). For a nontrivial character, dropping it changes the determinant.

Lemma 1.4 supplies the algebraically closed field-extension step in the degree-one arithmetic comparison, including its trace, cup pairing and finite correspondences. Its Jacobian base-change argument uses the actual all-test-scheme representation and rigidification in the earlier Picard construction. The earlier Picard, duality and analytic Riemann–Roch proofs also have their own foundational dependencies, whose complete transitive proof and source audit is still required.

The sources listed below are freely accessible mathematical materials. Actual earlier programme proofs are bound by their written titles and numbered locators above. In particular none of the analytic comparison or algebraic-geometry bindings here asserts that an uninspected transitive prerequisite has been certified. The full analytic Abel–Jacobi torus uniformization is not used as a substitute for Lemma 1.3's Kummer and cup argument.

## 8. Graded exercises with complete solutions

**Exercise 8.1 (easy).** Use (28) to compute \(\#X_0(11)(\mathbf F_p)\) at \(p=2,3,5\), and recover the Hecke eigenvalues. Explain why counting points on \(y^2+y=x^3-x^2\) would not, by itself, identify that curve with \(X_0(11)\).

*Solution.* At 2 the right-hand side is zero for both \(x\), and each has both \(y\), giving four affine points. At 3 the right-hand sides are \(1,0,0\); \(y^2+y\) never equals 1 and equals zero twice, again giving four. At 5 the right-hand sides are \(0,0,4,3,3\); the values of \(y^2+y\) are \(0,2,1,2,0\), so only the first two \(x\) contribute, twice each. Adding the single point at infinity gives five points in all three cases. Thus \(a_p=p+1-5\) gives \(-2,-1,1\). Equations (22) and (30) identify these with the Hecke eigenvalues on the one-dimensional space. The other curve has a different \(j\)-invariant and is not isomorphic to (28); equality of these few point counts cannot replace a modular-curve identification.

**Exercise 8.2 (medium).** Prove (22) from \(T_p=F+V\) and \(FV=p\), explicitly specifying the pairing and Hecke multiplicity hypotheses. Give a counterexample if only the two operator equations are retained.

*Solution.* Use the semisimple \(T_p\)-action on \(W_\ell\), with eigenvalue \(a\) of multiplicity \(2m_a\), where \(m_a\) is its multiplicity on \(S_2\). The cup-product pairing is nondegenerate, \(T_p\) is self-adjoint, and \(F\) has multiplier \(p\). Distinct \(T_p\)-eigenspaces are orthogonal, so each block \(U_a\) is nondegenerate. On it \(F^2-aF+p=0\). If the roots \(\alpha,\beta\) differ, \(F\) is diagonalizable and its two eigenspaces pair perfectly, since their individual self-pairings vanish by \(\alpha^2,\beta^2\ne p\). Each therefore has dimension \(m_a\). If the roots coincide, all \(2m_a\) roots are \(\alpha\). In both cases the block polynomial is \((X^2-aX+p)^{m_a}\). Multiply the blocks and use duality to transfer geometric Frobenius on cohomology to arithmetic Frobenius on the Tate module. For the counterexample, (21) obeys both operator equations but has polynomial \((X-\alpha)^2\), with unequal root multiplicities. Its scalar \(F\) could have multiplier \(p\) for a nonzero pairing only if \(\alpha^2=p\), contradicting the distinct-root choice.

**Exercise 8.3 (medium).** Count the rank-\(p\) subgroup schemes of an ordinary elliptic curve over \(\overline{\mathbf F}_p\), identify the connected one, and recover the length \(p+1\) of the parameter fiber.

*Solution.* Use \(E[p]=\mu_p\times(\mathbf Z/p)\). A subgroup with one geometric point is connected, projects trivially to the constant factor, and is \(\mu_p\) by equal ranks. A subgroup with \(p\) points is étale and projects isomorphically to the constant factor. Its graph homomorphism to \(\mu_p\) is trivial over the field, so it is the single étale subgroup. The connected subgroup is \(\ker F_E\). Thus there are two geometric subgroup schemes. For the fiber length, the connected subgroup has no infinitesimal deformation. A deformation of the étale subgroup over a local Artinian algebra is a graph determined by \(1+u\in\mu_p(R)\), with \(u^p=0\). Its local ring is \(k[u]/(u^p)\), of length \(p\). Together with the reduced connected point this gives length \(1+p\), as claimed. The two counts measure different properties.

**Exercise 8.4 (hard).** Explain Kronecker’s congruence for the degree-\(p\) correspondence through ordinary moduli. Retain fiber multiplicities, explain the role of supersingular points, and deduce the correct trace identity.

*Solution.* On an ordinary pair \((E,C)\), quotient by \(\ker F_E\) gives \((E^{(p)},C^{(p)})\). The other subgroup is the kernel of the Verschiebung isogeny from \(E\) to \(E^{(1/p)}\); its dual is Frobenius. Since \(p\) is invertible on the level subgroup, multiplication by \(p\) preserves it. These two branches are \(\Gamma_{\mathcal F}\) and its transpose. The first projection has degrees one and \(p\), respectively, so their divisor action at a geometric point is \([\mathcal F(x)]+p[\mathcal F^{-1}(x)]\), not a sum over \(p+1\) distinct special-fiber subgroups.

The stated reduction theorem says these are the two reduced components of the compactified correspondence. They meet at supersingular points, but those intersections are zero-dimensional and do not add a component to the correspondence cycle. The cycle identity therefore induces \(T_p=F+V\) on the Jacobian, with \(FV=p\). For \(N=1\), on \(j\)-invariants the two relations are \(j'=j^p\) and \(j=(j')^p\), explaining the modular-polynomial congruence
\[
\Phi_p(j,j')\equiv(j^p-j')(j-(j')^p)\pmod p.
\tag{34}
\]
Lemma 4.0 proves the monic modular polynomial, its integral coefficients and this congruence. Its reduction records the two branches, but normalizing this reduced plane curve separates their intersections. More precisely, over an algebraically closed field \(k\) of characteristic \(p\), put
\[
A=k[X,Y]/((X^p-Y)(X-Y^p)).
\]
Its normalization is \(k[t]\times k[u]\), through \((X,Y)=(t,t^p)\) and \((X,Y)=(u^p,u)\). To verify this, the two distinct prime factors make \(A\) reduced and inject it into the product of its component rings. That product is finite as an \(A\)-module, hence integral over \(A\), and is integrally closed in the product of the component fraction fields. Any element integral over \(A\) satisfies the same monic equation over this larger ring, so belongs to it. This proves the normalization assertion. An intersection \((a,a^p)\), with \(a^{p^2}=a\), has one preimage on each normalized branch. In particular, normalization after reduction cannot be identified with the reduced moduli correspondence above, which retains its supersingular intersections.

Finally \(F\) and \(V\) are adjoints, so their traces on cohomology agree. Thus \(\operatorname{tr}(T_p\mid W_\ell)=2\operatorname{tr}(F\mid W_\ell)\). Hodge decomposition gives \(\operatorname{tr}(T_p\mid W_\ell)=2\operatorname{tr}(T_p\mid S_2)\). Dividing by two and translating Frobenius by (19) proves \(\operatorname{tr}(\mathrm{Fr}_p\mid V_\ell J)=\operatorname{tr}(T_p\mid S_2)\).

## References and next reading

- P. Deligne and M. Rapoport, *Les schémas de modules de courbes elliptiques* (1973), especially V.1.6–V.1.18, VI.6.7–VI.6.10 and VII.1–VII.2; [free original at IAS](https://publications.ias.edu/sites/default/files/Number22.pdf).
- P. Deligne, *Formes modulaires et représentations \(\ell\)-adiques*, Bourbaki exposé 355, February 1969, published 1971, §§2–4; [free original Bourbaki text](https://www.numdam.org/item/SB_1968-1969__11__139_0/). The ordinary-count correction above concerns printed p.157 of this original.
- T. Weston, *The modular curves \(X_0(11)\) and \(X_1(11)\)*, Arizona Winter School notes (2001), §4; [school’s copy](https://swc-math.github.io/aws/2001/01Weston1.pdf).
- The Stacks project authors, normalization and curve local rings: [Tag 032L](https://stacks.math.columbia.edu/tag/032L) and [Tag 00PD](https://stacks.math.columbia.edu/tag/00PD). The particular normalization proof used here is written in Lemma 1.2.

Continue with *Galois representations of weight-two newforms*. A Hecke quotient of the Jacobian will isolate one eigenform and its coefficient field from the complete polynomial (22).
