# Good filtrations and the characteristic variety

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The two operators \(x\partial\) and \(x^2\partial-1\) on the line have leading symbols \(x\xi\) and \(x^2\xi\). Both vanish on the same cross in the cotangent plane: the zero section and the fiber over zero. But the second symbol vanishes twice along that fiber. We will attach this geometric support, together with its multiplicities, to the module of an equation. The construction must survive changing the generators and the filtration used to expose the leading terms.

We assume the [differential-operator algebra](differential-operators-and-the-weyl-algebra.md), the [connection interpretation of D-modules](d-modules-flat-connections-and-local-systems.md), and commutative algebra concerning finite modules, localization, support and composition length. The [Algebraic Geometry Bridge](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D100) supplies the geometric background. All arguments except the explicitly stated involutivity theorem are developed here.

Let \(k\) be algebraically closed of characteristic zero, and let \(X\) be a smooth separated variety of pure dimension \(d\). D-modules are left modules quasi-coherent over \(\mathcal O_X\). The order filtration on \(\mathcal D_X\) has \(F_{-1}\mathcal D_X=0\) and

\[
\operatorname{gr}\mathcal D_X\cong\operatorname{Sym}_{\mathcal O_X}\mathcal T_X.
\tag{1.1}
\]

On an affine coordinate chart this is a Noetherian commutative ring \(S\), whose spectrum is \(T^*X\) restricted to the chart. It carries the Poisson convention \(\{\xi_i,x_j\}=\delta_{ij}\). When taking a support we use its reduced closed set. When taking a multiplicity we retain the full graded module, including its nilpotents.

## 1. Finite generation with controlled orders

A coherent D-module is locally finitely generated over \(\mathcal D_X\); its local relations are finite as well, by the Noetherianity proved in the first lesson. A compatible filtration \(G_pM\), indexed by \(p\in\mathbf Z\), will always mean an increasing exhaustive filtration by coherent \(\mathcal O_X\)-submodules, locally zero for sufficiently negative \(p\), satisfying

\[
F_a\mathcal D_X\,G_bM\subset G_{a+b}M.
\tag{1.2}
\]

It is **good** if \(\operatorname{gr}^GM\) is locally finite over \(\operatorname{gr}\mathcal D_X\). The lower bound is part of our definition of compatible filtrations; finite generation of a graded module alone would not imply it.

**Proposition 1.1.** Good filtrations exist locally. They are precisely the filtrations which, locally, can be written

\[
G_pM=\sum_{j=1}^r F_{p-a_j}\mathcal D_X\,m_j
\tag{1.3}
\]

for finitely many local sections \(m_j\) and integers \(a_j\), with negative order pieces of \(\mathcal D_X\) interpreted as zero.

**Proof.** Given local D-generators, (1.3) defines a compatible filtration, with coherent pieces because every finite order piece of \(\mathcal D_X\) is locally free of finite rank over \(\mathcal O_X\). Exhaustiveness follows from D-generation. The classes of the \(m_j\) generate its associated graded, so the filtration is good.

Conversely, choose finitely many homogeneous graded generators of degrees \(a_j\), and lift them to sections \(m_j\in G_{a_j}M\), after shrinking the chart. For \(m\in G_pM\), express its class in degree \(p\) as a sum of symbols multiplying those generators and lift the symbols to operators. Subtracting \(\sum P_jm_j\) leaves an element of \(G_{p-1}M\). Repeat. The process terminates at the lower bound, proving (1.3). \(\square\)

**Theorem 1.2.** Two good filtrations \(G,H\) on the same coherent D-module are locally comparable: for some integer \(c\geq0\),

\[
G_{p-c}M\subset H_pM\subset G_{p+c}M
\quad\text{for every }p.
\tag{1.4}
\]

**Proof.** Use generators and degrees in (1.3) for \(G\). Exhaustiveness of \(H\) places each \(m_j\) in some \(H_{b_j}M\). Compatibility gives \(G_pM\subset H_{p+\max_j(b_j-a_j)}M\). Interchanging the filtrations gives the other inclusion. Choose \(c\) at least both bounds and zero. Only finitely many generators were used, so one common \(c\) works on the chosen neighborhood. \(\square\)

Comparability controls order up to a bounded error. It does not assert that the graded modules themselves are isomorphic. In fact their scheme-theoretic annihilators can differ.

## 2. A support that does not depend on order choices

For a good filtration define

\[
\operatorname{Ch}_G(M)=\operatorname{Supp}_S(\operatorname{gr}^GM)
=V\bigl(\operatorname{Ann}_S\operatorname{gr}^GM\bigr).
\tag{2.1}
\]

The annihilator is homogeneous, so this support is closed and conic for scaling the cotangent fibers.

**Theorem 2.1.** This reduced support is independent of the good filtration. The local supports glue to a closed conic subset \(\operatorname{Ch}(M)\subset T^*X\), called the characteristic variety.

**Proof.** Work on a common coordinate chart and choose \(c\) as in (1.4). Let \(h\) be a homogeneous element of degree \(q\) annihilating \(\operatorname{gr}^GM\), and lift it to \(P\in F_q\mathcal D\). Annihilation means

\[
P G_pM\subset G_{p+q-1}M
\quad\text{for every }p.
\tag{2.2}
\]

Iteration and comparability yield

\[
P^nH_pM\subset P^nG_{p+c}M
\subset G_{p+c+nq-n}M
\subset H_{p+nq+2c-n}M.
\tag{2.3}
\]

Choose \(n>2c\). Then \(h^n=\sigma_{nq}(P^n)\) annihilates \(\operatorname{gr}^HM\). The symbol identity holds even when the symbol is zero, by multiplicativity of the graded action. Since annihilators of graded modules are homogeneous, this proves one inclusion between their radicals. Interchange \(G,H\) for the reverse inclusion. Hence their zero sets agree.

The symbol algebra (1.1) is intrinsic. A filtration defined on a neighborhood restricts to a good filtration on overlaps, and any other local filtration gives the same support there by the argument just given. Thus the supports glue. Closedness and conicity are local on \(X\). \(\square\)

If \(M\ne0\), a good filtration has a nonzero graded piece: choose a nonzero section and its least filtration degree. Thus its characteristic variety is nonempty on a neighborhood where that section survives.

## 3. Multiplicity and a deformation parameter

Let \(Z\) be an irreducible component of \(\operatorname{Ch}(M)\), and let \(\mathfrak p\) be its generic prime in a chart meeting its generic point. Define

\[
m_Z(M)=\operatorname{length}_{S_{\mathfrak p}}
\bigl((\operatorname{gr}^GM)_{\mathfrak p}\bigr).
\tag{3.1}
\]

This length is finite. The prime is minimal in the support; after localization the support consists only of the maximal ideal of \(S_{\mathfrak p}\). A power of that maximal ideal annihilates the finite localized module. Its successive quotients are finite-dimensional over the residue field, giving finite composition length. The length is positive because the localized module is nonzero.

For example, \(S=k[x,\xi]\) and \(N=S/(\xi^2)\) have reduced support \(\xi=0\). At its generic point the chain

\[
0\subset(\xi)/(\xi^2)\subset S_{(\xi)}/(\xi^2)
\tag{3.2}
\]

has two residue-field factors, so its multiplicity is two. Tensoring first with \(S/(\xi)\) would erase one factor and incorrectly give one. Reduced support and generic length are distinct operations.

We now prove that (3.1) survives changing the filtration. Introduce a central variable \(t\) and the Rees objects

\[
R=\bigoplus_{p\geq0}F_p\mathcal D\,t^p\subset\mathcal D[t],
\qquad L_G=\bigoplus_{p\in\mathbf Z}G_pM\,t^p
\subset M[t,t^{-1}].
\tag{3.3}
\]

Division by \(t\) in the quotients gives

\[
R/tR\cong S,\qquad L_G/tL_G\cong\operatorname{gr}^GM.
\tag{3.4}
\]

A good filtration makes \(L_G\) finite over \(R\), generated by \(m_jt^{a_j}\). After inverting \(t\), it fills \(M[t,t^{-1}]\). Such a finite \(R\)-submodule of this ambient module will be called a lattice.

The ring \(R\) is Noetherian on the chart. To check this rather than assuming it, write \(b_i=t\partial_i\). Its normal form has basis \(t^j b^\alpha\), \(j\geq0\), over the coordinate ring. Filter by the number of \(b\)'s, leaving \(t\) in degree zero. Since \([b_i,a]=t\partial_i(a)\) lowers this degree, the new associated graded is the polynomial ring \(\mathcal O_X[t,\zeta_1,\ldots,\zeta_d]\). The nonnegative filtered Noetherian argument of the first lesson applies. Thus submodules and quotients of finite lattices are finite.

**Lemma 3.1.** If two lattices satisfy \(tL\subset L'\subset L\), the \(S\)-modules \(L/tL\) and \(L'/tL'\) have the same support and the same generic length on every irreducible component of that support.

**Proof.** Put \(A=L'/tL\) and \(B=L/L'\). Both are finite \(S\)-modules, because \(t\) kills them. The two exact sequences are

\[
0\longrightarrow A\longrightarrow L/tL\longrightarrow B\longrightarrow0,
\tag{3.5}
\]

\[
0\longrightarrow tL/tL'\longrightarrow L'/tL'
\longrightarrow A\longrightarrow0.
\tag{3.6}
\]

Multiplication by \(t\), invertible on the ambient module, identifies \(B\) with \(tL/tL'\). Therefore both middle modules have support \(\operatorname{Supp}A\cup\operatorname{Supp}B\). At the generic prime of any component of this union, all the localized modules in (3.5)–(3.6) have finite length by the argument preceding (3.2). Additivity of composition length makes each middle length the sum of the lengths of \(A\) and \(B\). These sums agree. \(\square\)

**Theorem 3.2.** Every multiplicity \(m_Z(M)\) is independent of the good filtration. Consequently the cycle

\[
\operatorname{CC}(M)=\sum_{Z\text{ component of }\operatorname{Ch}(M)}m_Z(M)[Z]
\tag{3.7}
\]

is intrinsic. If the support has components of different dimensions, this is a sum of cycles of those dimensions; additivity below concerns its top-dimensional part.

**Proof.** Let \(L=L_G\) and \(K=L_H\). Comparability gives \(t^cK\subset L\subset t^{-c}K\). Set \(L_j=L+t^jK\). Then

\[
tL_j\subset L_{j+1}\subset L_j.
\tag{3.8}
\]

For \(j\) sufficiently large, \(L_j=L\); for \(j\) sufficiently negative, \(L_j=t^jK\). All are finite lattices, so Lemma 3.1 can be applied to the finite chain between these two endpoints. It gives equality of supports and generic lengths at every step. Multiplication by \(t^j\) identifies \(t^jK/t^{j+1}K\) with \(K/tK\), including its \(S\)-action. The endpoint lengths are therefore precisely those for \(G\) and \(H\) in (3.1). On overlapping charts, localization preserves these generic-point calculations; the weights thus glue on the global components. \(\square\)

This proof uses two exact sequences with the same factors; it does not require identifying the graded modules or passing to reduced fibers. The lattice comparison is the standard mechanism behind filtration independence, as in [Ginzburg, Sections 1.1.15–1.1.23].

## 4. Submodules, quotients and exact sequences

**Theorem 4.1.** For a short exact sequence of coherent D-modules,

\[
0\longrightarrow M'\longrightarrow M\longrightarrow M''\longrightarrow0,
\tag{4.1}
\]

one has \(\operatorname{Ch}(M)=\operatorname{Ch}(M')\cup\operatorname{Ch}(M'')\). If \(M\ne0\) and \(r=\dim\operatorname{Ch}(M)\), the parts of dimension \(r\) in their cycles satisfy

\[
\operatorname{CC}_r(M)=\operatorname{CC}_r(M')+\operatorname{CC}_r(M'').
\tag{4.2}
\]

**Proof.** Give \(M\) a local good filtration, \(M'\) its intersection filtration, and \(M''\) the image filtration. The intersection Rees module is a submodule of the finite \(R\)-module \(L_G\), so it is finite by Noetherianity of \(R\). Its pieces are coherent submodules of the coherent pieces of \(G\). Thus the induced filtration is good by the same homogeneous-generator argument as Proposition 1.1; the image filtration is good as a quotient. These filtrations are strict by construction, giving

\[
0\longrightarrow\operatorname{gr}M'
\longrightarrow\operatorname{gr}M
\longrightarrow\operatorname{gr}M''\longrightarrow0.
\tag{4.3}
\]

For the middle exactness, if \(m\in G_pM\) maps into \(G_{p-1}M''\), choose \(n\in G_{p-1}M\) with the same image. Then \(m-n\in M'\cap G_pM\), representing the required graded preimage. The other two exactness assertions follow directly from intersection and image.

Localizing (4.3) shows that the middle support is the union of the other supports. At a generic point of a dimension-\(r\) component, every nonzero localized term has finite length; any dimension-\(r\) component of a submodule or quotient is a component of the union. Length additivity gives (4.2). Filtration independence removes the choices. \(\square\)

For the zero module the characteristic variety is empty and its cycle is zero, so exactness gives the same assertions trivially. The dimension qualifier matters for nonzero modules. For \(d>0\), take \(M=\mathcal D_X\oplus\mathcal O_X\). Its characteristic variety is all of \(T^*X\), so its only components are those of that space; the zero section contributed by the second summand is contained in the larger support. The top-dimensional cycle is additive, but the sum over all components of the two separate supports has an extra lower-dimensional zero-section term. Thus an unrestricted additivity assertion for the mixed-dimensional cycle (3.7) would be false.

## 5. One equation and its leading hypersurface

**Theorem 5.1.** On an integral coordinate chart, let \(P\ne0\) be an operator of order \(m\). The quotient module \(Q=\mathcal D/\mathcal D P\), with its image order filtration, has

\[
\operatorname{gr}Q\cong S/(\sigma_m(P)),
\qquad \operatorname{Ch}(Q)=V(\sigma_m(P)).
\tag{5.1}
\]

**Proof.** The symbol ring on this chart is a domain. Thus for a nonzero \(A\in\mathcal D\), the product \(AP\) has order \(\operatorname{ord}(A)+m\) and symbol \(\sigma(A)\sigma(P)\). Every element of the principal left ideal is a single product \(AP\), so its associated graded ideal is exactly \(S\sigma(P)\). Indeed every homogeneous multiple of \(\sigma(P)\) is realized by lifting its homogeneous coefficient to such an \(A\). The image filtration on the quotient therefore has the displayed graded module. It is good, and its support is the displayed zero set. \(\square\)

The hypothesis about an integral chart allows us to multiply nonzero symbols without cancellation. Smooth varieties have disjoint integral components locally, so the calculation applies component by component wherever \(P\) is nonzero. If \(P\) is zero on a whole component, the quotient there is \(\mathcal D\), with full cotangent support.

On the line write \(Z=\{\xi=0\}\) for the zero section and \(F=\{x=0\}\) for the fiber at zero. The initial examples give

\[
\operatorname{CC}(A_1/A_1(x\partial))=[Z]+[F],
\qquad
\operatorname{CC}(A_1/A_1(x^2\partial-1))=[Z]+2[F].
\tag{5.2}
\]

For the first quotient its graded module is \(k[x,\xi]/(x\xi)\). At \((\xi)\), \(x\) is invertible, and at \((x)\), \(\xi\) is invertible. Each localization thus has one residue-field factor. For the second quotient the graded module is \(k[x,\xi]/(x^2\xi)\). Localization at \((\xi)\) still gives length one; localization at \((x)\) gives the quotient by \(x^2\), of length two. Both reduced supports are \(Z\cup F\), but their cycles distinguish these multiplicities.

Their scalar equations on the punctured line are respectively \(u'=0\) and \(u'=x^{-2}u\), with solutions \(c\) and \(c e^{-1/x}\). The later regular-singularity criterion will distinguish their behavior at zero. The characteristic variety alone does not make that distinction; even the cycle does not record the full analytic growth data.

## 6. Bundles, a closed subvariety and Laurent functions

### A connection has no nonzero cotangent direction

If \(E\) is a finite-rank bundle with integrable connection, give it the filtration \(G_pE=0\) for \(p<0\) and \(G_pE=E\) for \(p\geq0\). Its graded module is concentrated in degree zero, so every positive-degree symbol acts by zero. On a component where the bundle has rank \(r>0\),

\[
\operatorname{Ch}(E)=\text{zero section},
\qquad \operatorname{CC}(E)=r[\text{zero section}].
\tag{6.1}
\]

The generic length is the dimension of the bundle fiber over the function field of that component, namely \(r\). Rank-zero components contribute nothing. In particular this computes \(\mathcal O_X\). By contrast, the regular module \(\mathcal D_X\) has graded module \(S\), full cotangent support, and generic multiplicity one on each component of \(T^*X\).

**Proposition 6.1.** For a coherent D-module, containment of its characteristic variety in the zero section is equivalent to coherence over \(\mathcal O_X\).

**Proof.** The reverse direction follows from the preceding lesson's local-freeness theorem and (6.1). For the forward direction let \(N=\operatorname{gr}^GM\) on a coordinate chart. Containment in the zero section says that each \(\xi_i\) belongs to the radical of \(\operatorname{Ann}_S N\). Choose integers \(n_i>0\) with \(\xi_i^{n_i}N=0\). Every monomial of total degree at least \(N_0=1+\sum_i(n_i-1)\) is divisible by one of these powers, and therefore annihilates \(N\).

Choose finite homogeneous generators of \(N\) and let \(a\) be their largest degree. Since \(S\) is generated over its degree-zero ring by the \(\xi_i\), all graded pieces of \(N\) in degrees greater than \(a+N_0-1\) vanish. Thus \(G_pM=G_{p-1}M\) above this bound. Exhaustiveness implies \(M=G_{a+N_0-1}M\), which is coherent over \(\mathcal O_X\). This is a local argument and hence proves coherence on \(X\). \(\square\)

The finite-rank qualifier in (6.1) is essential. An arbitrary quasi-coherent module with an integrable connection can be infinite over \(\mathcal O_X\): the regular D-module itself is such a module by the connection correspondence, and its characteristic variety is the whole cotangent bundle.

### The conormal bundle of a smooth closed subvariety

Let \(i:Z\hookrightarrow X\) be a smooth closed subvariety of codimension \(c\). In adapted étale coordinates \((z_1,\ldots,z_c,y_1,\ldots,y_{d-c})\), its ideal is \((z_1,\ldots,z_c)\). The closed-embedding image of its trivial connection has the local presentation

\[
\mathcal D_X\Big/
\left(\sum_i\mathcal D_Xz_i+
\sum_j\mathcal D_X\partial_{y_j}\right).
\tag{6.2}
\]

Here is an intrinsic construction to fix which module this presentation describes. Put

\[
T=\mathcal O_Z\otimes_{i^{-1}\mathcal O_X}i^{-1}\mathcal D_X.
\tag{6.3}
\]

It is a right \(i^{-1}\mathcal D_X\)-module by multiplication on the operator factor. A vector field \(\eta\) on \(Z\) acts on the left by

\[
\eta(a\otimes P)=\eta(a)\otimes P+a\otimes\widetilde\eta P,
\tag{6.4}
\]

where \(\widetilde\eta\) is any local lift tangent to \(Z\). Adapted coordinates supply such lifts. Changing the lift changes its coefficients by elements of the ideal of \(Z\), which disappear in (6.3), so the formula is independent of the lift. Its compatibility with the tensor relation follows from the Leibniz rule, and its curvature is zero because a commutator of lifts differs from a lift of the bracket by those same vanishing coefficients. The connection correspondence gives a left \(\mathcal D_Z\)-action, commuting with the right action. Change both sides by the canonical bundles as in the preceding lesson and define the module on \(X\)

\[
i_+\mathcal O_Z=
i_*\left[
\left(\omega_Z\otimes_{\mathcal O_Z}T
\otimes_{i^{-1}\mathcal O_X}i^{-1}\omega_X^{-1}\right)
\otimes_{\mathcal D_Z}\mathcal O_Z
\right].
\tag{6.5}
\]

The bracketed transfer module has a left \(i^{-1}\mathcal D_X\)-action and right \(\mathcal D_Z\)-action. Equation (6.5) is only the ordinary module needed for this example; the derived direct-image functor will be constructed later.

Choose the coordinate volume forms in (6.5). Normal form, followed by transposition on both sides, identifies it with (6.2). More explicitly, a generator \(\delta\) is killed by the \(z_i\) and the tangent derivatives of its constant coefficient. The remaining independent expressions are

\[
\sum_{\alpha\in\mathbf N^c} a_\alpha(y)\partial_z^\alpha\delta,
\qquad a_\alpha\in\mathcal O_Z,
\tag{6.6}
\]

with finite sums. Independence also follows directly from (6.3): ordering normal derivatives first makes the transfer module free on those derivatives over the tangent operator algebra; tensoring that algebra with its trivial connection leaves the coefficients \(\mathcal O_Z\). Tangent derivatives differentiate those coefficients, while

\[
z_i\partial_z^\alpha\delta=-\alpha_i\partial_z^{\alpha-e_i}\delta.
\tag{6.7}
\]

Filter (6.6) by \(|\alpha|\). Equation (6.7) lowers degree and the tangent derivatives preserve it. The graded module is therefore

\[
\mathcal O_Z[\xi_1,\ldots,\xi_c],
\quad z_i=0,\quad\eta_j=0,
\tag{6.8}
\]

where \(\eta_j\) are the tangent derivative symbols. These equations say that the covector annihilates \(T_zZ\). Consequently

\[
\operatorname{Ch}(i_+\mathcal O_Z)=T_Z^*X,
\qquad \operatorname{CC}(i_+\mathcal O_Z)=[T_Z^*X]
\tag{6.9}
\]

on each irreducible component of \(Z\). The generic length is one, since (6.8) is the reduced coordinate ring of that conormal bundle. The intrinsic construction and the intrinsic conormal equations make these chart computations global.

For example, for the parabola \(y=x^2\) in the plane, adapted coordinates are \(z=y-x^2\), \(t=x\). Its conormal bundle is parametrized in the original cotangent coordinates by

\[
(t,a)\longmapsto
(x,y;\xi_x,\xi_y)=(t,t^2;-2ta,a).
\tag{6.10}
\]

Indeed the tangent operator is \(\partial_x+2x\partial_y\), whose symbol vanishes exactly when \(\xi_x+2x\xi_y=0\). This computation shows explicitly how a conormal direction changes when the subvariety is curved.

### Laurent functions on the affine line

The module \(L=k[x,x^{-1}]\) with its ordinary derivative is generated over \(A_1\) by \(x^{-1}\). The Euler operator gives \((\theta+1)x^{-1}=0\), so there is a surjection

\[
Q_{-1}=A_1/A_1(\theta+1)\longrightarrow L.
\tag{6.11}
\]

It is an isomorphism. In the weight basis from the preceding lesson, the positive vectors map to \(x^{j-1}\), \(j\geq0\), and the negative vectors \(\partial^s e\) map to \((-1)^s s!x^{-s-1}\), \(s\geq1\). These are nonzero multiples of all Laurent monomials, with no repeated exponent, so they form a basis. Theorem 5.1 gives

\[
\operatorname{Ch}(L)=Z\cup F,
\qquad \operatorname{CC}(L)=[Z]+[F].
\tag{6.12}
\]

One can also recover this from the exact sequence

\[
0\longrightarrow k[x]\longrightarrow L
\longrightarrow\delta_0\longrightarrow0.
\tag{6.13}
\]

For its last isomorphism send the generator of \(\delta_0\) to the class of \(x^{-1}\). It is killed by \(x\), and its successive derivatives are the independent negative Laurent monomials modulo polynomials. Theorem 4.1 then combines the zero-section and fiber cycles.

## 7. Involutivity and the dimension bound

**Gabber's involutivity theorem (statement).** For a filtered Noetherian ring with commutative Noetherian associated graded containing \(\mathbf Q\), the radical of the annihilator of the graded module of a finite module with a good filtration is involutive for the commutator Poisson bracket. In our setting, if \(I\) is the reduced ideal of \(\operatorname{Ch}(M)\), the conclusion is

\[
\{I,I\}\subset I.
\tag{7.1}
\]

This is [Kashiwara–Schapira, Theorem 11.2.2], a theorem about filtered rings before its analytic specialization. The characteristic-zero hypothesis supplies \(\mathbf Q\); the order filtration and its Noetherianity supply the other hypotheses. We use the theorem as a stated external result. It is not proved in this lesson.

Involutivity here is the coisotropic condition. It requires brackets of two equations for the variety to vanish on the variety. It does **not** require \(\{S,I\}\subset I\): for the zero section, \(\xi_i\in I\) but \(\{\xi_i,x_i\}=1\).

**Corollary 7.1.** Every irreducible component of \(\operatorname{Ch}(M)\) has dimension at least \(d\). In particular \(M\ne0\) implies \(\dim\operatorname{Ch}(M)\geq d\).

**Proof.** For an irreducible component \(C\), remove the other components and choose a smooth point of \(C\). Such points form a dense open set in characteristic zero. On this open set the ideal in (7.1) is the ideal of \(C\), so the same bracket condition holds. Localization preserves it by the quotient rule and the Leibniz identity.

Let \(V=T_p(T^*X)\), of dimension \(2d\), with its nondegenerate symplectic form, and \(W=T_pC\). Differentials of functions vanishing on \(C\) span its conormal space, the annihilator of \(W\). The symplectic identification sends this conormal space to \(W^\perp\). Condition (7.1) says that these Hamiltonian vectors annihilate every other defining function, hence are tangent to \(C\). Thus \(W^\perp\subset W\). Since \(\dim W^\perp=2d-\dim W\), it follows that \(2d-\dim W\leq\dim W\), or \(\dim C\geq d\). Nonzero modules have nonempty characteristic varieties by Section 2, giving the last assertion. \(\square\)

When all components have dimension \(d\), they are Lagrangian at their smooth points: the same inclusion has equal dimensions and becomes \(W^\perp=W\). The next lesson will study these minimal-dimension modules, called holonomic modules, and give an algebraic dimension argument for Weyl algebras.

## 8. Exercises with complete solutions

**Exercise 8.1 (easy).** Compute the characteristic variety and cycle of the Airy module \(A_1/A_1(\partial^2-x)\). Give its underlying finite-rank connection.

**Solution.** The principal symbol is \(\xi^2\), so Theorem 5.1 gives the zero section as the reduced support. Localization of \(k[x,\xi]/(\xi^2)\) at \((\xi)\) has two residue-field factors as in (3.2); the cycle is \(2[Z]\). Division by the operator monic in \(\partial\) gives the free \(k[x]\)-basis \(e_0=e\), \(e_1=\partial e\). The actions \(\partial e_0=e_1\), \(\partial e_1=x e_0\) give the connection matrix

\[
A(x)=\begin{pmatrix}0&x\\1&0\end{pmatrix}.
\tag{8.1}
\]

Its curvature is zero in dimension one. The constant bundle filtration has two graded generators in degree zero killed by \(\xi\), whereas the quotient order filtration has graded module \(S/(\xi^2)\). Both give multiplicity two, illustrating filtration independence without an isomorphism of graded modules.

**Exercise 8.2 (easy).** Compute the characteristic variety and cycle of a finite-rank bundle with integrable connection. Explain why the finite-rank hypothesis cannot be omitted when a connection is allowed on an arbitrary quasi-coherent module.

**Solution.** Use the constant filtration in Section 6. It is good because the bundle is finite over \(\mathcal O_X\). The positive-degree symbols annihilate its graded module, giving the zero section over every component with positive rank; its generic length is that rank. The regular D-module has an integrable connection by the preceding lesson but is infinite over \(\mathcal O_X\), and its characteristic variety is all of \(T^*X\). Therefore the statement concerns finite-rank connections, not every quasi-coherent module with connection.

**Exercise 8.3 (medium).** Prove that two good filtrations give the same component multiplicities, and show explicitly why the rank of the graded module after restriction to reduced support is not a valid replacement for generic length.

**Solution.** Form the two finite Rees lattices \(L,K\). Comparability gives a finite chain \(L+t^jK\) between \(L\) and a power of \(t\) times \(K\). For each adjacent pair \(tL_j\subset L_{j+1}\subset L_j\), equations (3.5)–(3.6) express the two graded quotients as extensions of the same two finite symbol modules. Their supports agree. At the generic point of any component of that support, those two factors have finite length and each middle length is their sum. Multiplication by \(t^j\) identifies the endpoint quotient with \(K/tK\), proving equality for the original filtrations.

For a concrete failure of reduced rank, take \(M=A_1/A_1\partial^2\). The quotient order filtration has graded module \(S/(\xi^2)\), whose tensor product with the reduced zero section \(S/(\xi)\) has generic rank one. As a \(k[x]\)-module, \(M\) is free on \(e,\partial e\); its connection has \(\partial e\) as the derivative of the first basis vector and derivative zero on the second. The constant bundle filtration has graded module \(k[x]^2\) on the zero section, with reduced rank two. Generic length in \(S_{(\xi)}\) is two for both. Only that length is independent of the filtration.

**Exercise 8.4 (medium).** Prove that a coherent D-module with characteristic variety contained in the zero section is coherent over \(\mathcal O_X\).

**Solution.** On a coordinate chart let \(N=\operatorname{gr}M\). Each positive-degree coordinate \(\xi_i\) vanishes on its support, so a power \(\xi_i^{n_i}\) annihilates \(N\). Every symbol monomial of degree at least \(1+\sum_i(n_i-1)\) then annihilates it. Finite homogeneous generation bounds above the degrees in which \(N\) is nonzero, because \(S\) is generated by degree-one symbols over \(\mathcal O_X\). Above that bound the good filtration stabilizes. Exhaustiveness identifies \(M\) with one coherent filtration piece, proving the assertion locally and hence globally. This argument establishes the criterion in Proposition 6.1 without an appeal to involutivity.

**Exercise 8.5 (hard).** Compute the characteristic cycles of \(Q_\lambda=A_1/A_1(x\partial-\lambda)\) for \(\lambda\notin\mathbf Z\) and for \(\lambda=0\). Explain how their module structures differ despite the same cycle.

**Solution.** For every \(\lambda\), the principal symbol is \(x\xi\). Each of its two factors occurs once, so

\[
\operatorname{CC}(Q_\lambda)=[Z]+[F]
\quad\text{for all }\lambda.
\tag{8.2}
\]

For a nonintegral parameter, the weight basis \(u_j\), \(j\in\mathbf Z\), from the preceding lesson has distinct eigenvalues \(\lambda+j\) for \(\theta\). Every vector is a finite combination of these basis vectors. Polynomial interpolation in \(\theta\) projects any nonzero such combination onto a nonzero weight vector. The transition coefficients in the actions of \(x\) and \(\partial\) are all nonzero for nonintegral \(\lambda\), so one weight vector generates all the others. Hence \(Q_\lambda\) is simple.

For \(\lambda=0\), the vectors \(\partial e,\partial^2e,\ldots\) span a submodule: \(x\partial e=0\), and the remaining actions are exactly those of \(\delta_0\), with generator \(\partial e\). The quotient is freely spanned by \(e,xe,x^2e,\ldots\), with \(\partial e=0\), and is \(k[x]\). Thus

\[
0\longrightarrow\delta_0\longrightarrow Q_0
\longrightarrow k[x]\longrightarrow0.
\tag{8.3}
\]

This sequence is not split. A section of the quotient sending \(1\) to a lift must choose \(e+v\), with \(v\) in the span of the negative weight vectors. But \(\partial e=u_{-1}\), while \(\partial v\) lies in the span of \(u_{-2},u_{-3},\ldots\); their sum cannot vanish. There is no D-linear lift of the generator of \(k[x]\). The module is therefore reducible with a nonsplit extension, although its cycle equals that of the simple nonintegral modules. Exact-sequence additivity recovers the same cycle from its two factors.

**Exercise 8.6 (medium).** Let \(0\to M'\to M\to M''\to0\) be exact. Prove the union formula for characteristic varieties using induced filtrations, and identify the precise dimension range in which component multiplicities are additive.

**Solution.** Give \(M'\) the intersection filtration and \(M''\) the image filtration from a good filtration of \(M\). Their Rees modules are a finite submodule and quotient of the Rees module of \(M\), so both filtrations are good. Strictness gives (4.3). An exact sequence of localized symbol modules has a zero middle term precisely when both end terms are zero, giving the union formula. At a generic point of a component of maximal dimension \(r\) of the union, all nonzero terms have finite length. Their lengths add, proving additivity of the dimension-\(r\) cycles. For a component of an end term contained properly in a larger component of the middle support, it is no longer a component of that union; no such formula for the full mixed-dimensional cycle follows. The example \(\mathcal D_X\oplus\mathcal O_X\) in Section 4 shows the failure explicitly.

## What this lesson does not prove

Gabber's involutivity theorem is the external theorem used in Section 7, in exactly its filtered-ring characteristic-zero form [Kashiwara–Schapira, Theorem 11.2.2]. We prove its symplectic dimension consequence, not its general algebraic proof. [Ginzburg, Theorem 1.2.5 and Corollary 1.2.10] give the same involutivity statement and discuss its proof. Proving that an unradicalized symbol ideal is closed under brackets does not by itself prove the theorem about its radical.

The remaining imported background consists of elementary support and length theory for finite modules over Noetherian commutative rings, smooth adapted étale coordinates for a smooth closed embedding, and the cotangent bundle's nondegenerate symplectic form. The normal-form and Noetherian arguments for \(\mathcal D_X\), and canonical-bundle side-changing, were proved in the preceding lessons. This lesson proves filtration existence and comparability, support and multiplicity independence, the exact-sequence statements, the cyclic hypersurface formula, the zero-section criterion, and all displayed characteristic-variety and cycle calculations. It does not prove regularity or classify all extensions of the punctured-line connection.

## References

- M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §6.4 and §10.1, for involutivity and the characteristic variety of analytic D-modules; V. Ginzburg, [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), for good filtrations. The Rees Noetherian argument above proves the good-submodule property in the algebraic setting used here.
- Victor Ginzburg, with Vladimir Baranovsky and Sam Evens, *Lectures on D-modules*, 1998, Sections 1.1.10–1.1.23 for good filtrations and lattice comparison; Theorem 1.2.5 and Corollary 1.2.10 for involutivity. [University-hosted notes](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf). Multiplicities in this lesson are the generic composition lengths (3.1); Exercise 8.3 explains why reduction before taking a rank loses information.
- Roman Bezrukavnikov, *Noncommutative Algebra*, MIT 18.706, spring 2023, Section 24.6 for the related filtered growth dimension of a module. [Open course materials](https://ocw.mit.edu/courses/18-706-noncommutative-algebra-spring-2023/). That dimension and the Bernstein filtration will be treated in the next lesson.
- Alexander Beilinson and Vladimir Drinfeld, *Quantization of Hitchin's integrable system and Hecke eigensheaves*, Section 1.1.4 for the filtration on differential operators and its cotangent interpretation. The calculation here concerns smooth varieties; it does not assume a global filtration on a stack.
- The Stacks project, *Commutative Algebra*, [Tag 09CH, Differential operators](https://stacks.math.columbia.edu/tag/09CH), as compared in the [AI Integrated Stacks Project English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#section-differential-operators). AI Integrated Stacks Project is an edition with AI-proposed corrections and additions, not reviewed by the official Stacks maintainers. The characteristic variety and cycle constructions here go beyond that section.
