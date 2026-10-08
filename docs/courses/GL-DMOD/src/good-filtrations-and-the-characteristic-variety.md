# Good filtrations and the characteristic variety

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The two operators \(x\partial\) and \(x^2\partial-1\) on the line have leading symbols \(x\xi\) and \(x^2\xi\). Both vanish on the same cross in the cotangent plane: the zero section and the fiber over zero. But the second symbol vanishes twice along that fiber. We will attach this geometric support, together with its multiplicities, to the module of an equation. The construction must survive changing the generators and the filtration used to expose the leading terms.

We assume the [differential-operator algebra](differential-operators-and-the-weyl-algebra.md), the [connection interpretation of D-modules](d-modules-flat-connections-and-local-systems.md), and commutative algebra concerning finite modules, localization, support and composition length. The [Algebraic Geometry Bridge](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D100) supplies the geometric background. The filtration and characteristic-cycle arguments are developed here, together with the complete general involutivity proof in Section 7.

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

**Theorem 7.0 (Gabber involutivity).** For a filtered Noetherian ring with commutative Noetherian associated graded containing \(\mathbf Q\), the radical of the annihilator of the graded module of a finite module with a good filtration is involutive for the commutator Poisson bracket. In our setting, if \(I\) is the reduced ideal of \(\operatorname{Ch}(M)\), the conclusion is

\[
\{I,I\}\subset I.
\tag{7.1}
\]

The proof below follows the first-order trace strategy in Ginzburg's freely accessible [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), Theorem 1.2.8 and Lemma 1.2.9, and in Singh and Kumar's [freely accessible author version](https://www.researchgate.net/publication/263610454_On_the_Involutivity_of_the_Characteristic_Variety), Sections 3–5. We prove the coefficient-field and fraction constructions needed to retain the full Noetherian statement, including associated graded rings that are not of finite type over a field. The order filtration of $\mathcal D_X$ supplies the hypotheses by the preceding lesson.

**Proof of Theorem 7.0.** Write $S=\operatorname{gr}_F A$ and $N=\operatorname{gr}_G M$. A good filtration supplies a finite $S$-module $N$. The argument below only requires these graded finiteness hypotheses, so it also covers integer-indexed filtrations without a finite-type assumption on $S$.

### First-order Rees quotient

Use a central indeterminate \(t\) and form the Rees ring and module
\[
\mathcal R=\bigoplus_{j\in\mathbf Z}F_jA\,t^j
       \subseteq A[t,t^{-1}],\qquad
\mathcal L=\bigoplus_{j\in\mathbf Z}G_jM\,t^j
       \subseteq M[t,t^{-1}].
\]
Since \(1\in F_0A\subseteq F_1A\), multiplication by \(t\) is an operation on both objects. It is injective, by their inclusions in the Laurent objects. Put
\[
\mathcal A=\mathcal R/t^2\mathcal R,\qquad
\mathcal M=\mathcal L/t^2\mathcal L,\qquad h=t.
\tag{7.1a}
\]
The parameter \(h\) is central and \(h^2=0\). Degree by degree,
\[
\mathcal A/h\mathcal A=S,\qquad
\mathcal M/h\mathcal M=N.
\]
Cancellation of \(t\) in the Laurent objects proves
\[
\ker(h:\mathcal A\to\mathcal A)=h\mathcal A,\qquad
\ker(h:\mathcal M\to\mathcal M)=h\mathcal M.
\tag{7.1b}
\]
For example \(t\ell\in t^2\mathcal L\) implies
\(\ell\in t\mathcal L\). Consequently multiplication by \(h\) identifies
\(\mathcal A/h\mathcal A\) with \(h\mathcal A\), and \(N\) with
\(h\mathcal M\).

The first-order ring \(\mathcal A\) canonically contains \(\mathbf Q\), even if this was not assumed for \(A\). An integer \(n>0\) is invertible modulo \(h\mathcal A\). Choose \(u\) with \(nu=1+hv\). Since \((1+hv)^{-1}=1-hv\), \(n\) is invertible in \(\mathcal A\). Its inverse is central, so the rational scalars give a central field. The kernel/image identities (7.1b) say precisely that these objects are free, hence flat, over \(\mathbf Q[h]/(h^2)\): lift a \(\mathbf Q\)-basis of the quotient. Subtracting a finite combination of its lifts from any vector leaves \(h y\); reducing \(y\) and subtracting its basis combination gives the required expression in those lifts and their \(h\)-multiples. A relation \(\sum_i(q_i+h r_i)e_i=0\) first gives \(q_i=0\) after reduction. Then (7.1b) gives \(\sum_i r_i e_i\in h\mathcal M\), so a second reduction gives \(r_i=0\). The same argument applies to the ring.

The module \(\mathcal M\) is finite over \(\mathcal A\). Lift finitely many \(S\)-generators of \(N\), and let \(P\) be their \(\mathcal A\)-span. For \(Q=\mathcal M/P\), reduction gives \(Q=hQ\); hence \(Q=h^2Q=0\). This does not require \(\mathcal L\) to be finite over \(\mathcal R\).
Similarly \(\mathcal A\) is left and right Noetherian: the ideal \(h\mathcal A\) and quotient \(\mathcal A/h\mathcal A\) are Noetherian modules over \(S\), so their two-step extension is Noetherian on each side. Indeed, in an ascending chain of ideals the images in the quotient and the intersections with the ideal eventually stabilize. A later member can then have no nonzero quotient over that fixed member: subtract an element with the same image and use the equal intersections. Thus the chain itself stabilizes. No Noetherianity assertion for \(\mathcal R\) is used.

Commutativity of \(S\) gives
\([F_iA,F_jA]\subseteq F_{i+j-1}A\), and therefore
\([\mathcal R,\mathcal R]\subseteq t\mathcal R\). Dividing a first-order commutator by \(h\) using (7.1b) gives exactly
\[
\{\sigma_i(a),\sigma_j(b)\}
   =\sigma_{i+j-1}([a,b]).
\tag{7.1c}
\]
Changing lifts changes only lower-order terms. The commutator Leibniz and Jacobi identities prove that (7.1c) is the usual Poisson bracket. It remains to prove radical-annihilator involutivity for the finite flat first-order module \(\mathcal M\).

### Localization of first-order modules

More generally let \(\mathcal A\) have a central \(h\), with \(h^2=0\), let \(B=\mathcal A/h\mathcal A\) be commutative, and assume the ring identity in (7.1b). Suppose \(\mathcal M\) satisfies the module identity in (7.1b).
Fix a prime \(\mathfrak p\) of \(B\), and let \(T\) be the full preimage of \(B\setminus\mathfrak p\).

Every commutator belongs to \(h\mathcal A\), and is central: if
\(c=hr\), then \([c,a]=h[r,a]=0\).
For \(s\in T\), \(a\in\mathcal A\), and \(c=[s,a]\), we have
\[
s^2a=(as+2c)s,\qquad
as^2=s(sa-2c).
\tag{7.1d}
\]
These are the left and right common-multiple conditions for denominators. Moreover
\[
as=0\ \Longrightarrow\ s^2a=0,\qquad
sa=0\ \Longrightarrow\ as^2=0.
\tag{7.1e}
\]
For the first implication, \(c=sa\), and
\(s^2a=s(as)+sc=sc=cs=(sa)s=0\); the other is symmetric.
Thus denominator torsion can also be removed on the required side.

Here is the fraction construction and the exactness fact used below. Left fractions in a module are pairs \((s,m)\), written \(s^{-1}m\). Two pairs \((s,m)\), \((u,n)\) are equivalent when there are \(v,w\in T\) such that
\[
vs=wu,\qquad vm=wn.
\tag{7.1f}
\]
Common left multiples exist by (7.1d). When both factors being compared are denominators, all multipliers can be chosen in \(T\): their reductions lie outside the prime \(\mathfrak p\). This also proves transitivity of (7.1f), by taking a common left multiple of the two intervening multipliers.

Addition uses a common left denominator. For multiplication or the localized scalar action, choose \(v\in T,c\in\mathcal A\) with \(va=cu\), and use
\[
(s^{-1}a)(u^{-1}m)=(vs)^{-1}(cm).
\tag{7.1g}
\]
Formula (7.1d) supplies such \(v,c\), for example \(v=u^2\).
These operations are independent of choices. To verify this, refine any two common-denominator expressions to a common left multiple. Any discrepancy between their coefficient multipliers annihilates an original denominator; (7.1e) supplies a further denominator annihilating that discrepancy. A common left multiple handles the finitely many discrepancies together. The resulting numerators are equal. For associativity of three fractions \(s^{-1}a,u^{-1}b,v^{-1}m\), choose \(pa=qu\), \(rb=wv\), and \(tq=zr\), with \(p,r,t\in T\), by the common-multiple formula. Both parenthesizations then give \((tps)^{-1}zwm\): for the left one use \(tp(ab)=zwv\), and for the right one use \(tp,a=z(ru)\). Independence of choices was just proved, so these common choices establish associativity. Refining to common left denominators similarly makes the two distributive identities the ordinary distributive identities in \(\mathcal A\) and its module. Thus these formulas construct the ring \(\mathcal A_T\) and modules \(\mathcal M_T\). A map making every element of \(T\) invertible necessarily sends \(s^{-1}a\) to the corresponding inverse product, proving the universal property.

An immediate consequence of (7.1f) is the precise zero criterion
\[
s^{-1}m=0
 \quad\Longleftrightarrow\quad
vm=0\text{ for some }v\in T.
\tag{7.1h}
\]
Localization is exact. Surjections lift numerators. If the image of
\(s^{-1}m\) in a localized quotient is zero, (7.1h) supplies \(v\in T\)
with \(vm\) in the original kernel; then
\(s^{-1}m=(vs)^{-1}(vm)\) comes from the localization of that kernel.
Finite generation is also preserved, by writing each numerator in terms of a fixed finite generating set.

Reduction of the fraction construction gives
\[
\mathcal A_T/h\mathcal A_T=B_{\mathfrak p},\qquad
\mathcal M_T/h\mathcal M_T=N_{\mathfrak p}.
\tag{7.1i}
\]
The kernel/image condition for \(h\) is preserved. If
\(h\,s^{-1}m=0\), clear a denominator by (7.1h) to obtain
\(hvm=0\). Before localization, (7.1b) gives \(vm=hy\); hence
\[
s^{-1}m=(vs)^{-1}(hy)\in h\mathcal M_T.
\]
The reverse containment is automatic, and the same proof applies to the ring.

The first-order commutator bracket on \(B_{\mathfrak p}\) is the extension of the bracket on \(B\): restricting to \(B\) agrees, and the derivation identity forces
\(\{s^{-1},b\}=-s^{-2}\{s,b\}\).
In particular it agrees with the original symbol bracket after the reduction (7.1a). For reference the denominator formula is
\[
\left\{\frac a s,\frac b u\right\}
=\frac{\{a,b\}}{su}
 -\frac{b\{a,u\}}{su^2}
 -\frac{a\{s,b\}}{s^2u}
 +\frac{ab\{s,u\}}{s^2u^2}.
\tag{7.1j}
\]
Its derivation follows by expanding both arguments as products with inverses.
An arbitrary first-order deformation gives an antisymmetric biderivation; Jacobi is not needed in the local trace argument. In our Rees situation Jacobi was already proved in (7.1c).

### Coefficient field in a finite Artin quotient

We prove the needed elementary coefficient-field fact. Let \(C\) be a commutative Artin local \(\mathbf Q\)-algebra with nilpotent maximal ideal and residue field \(K\). There is a subfield of \(C\) whose residue map is an isomorphism onto \(K\).

Choose a transcendence basis \(T_0\) of \(K/\mathbf Q\), of arbitrary cardinality, and choose lifts of all its elements to \(C\). A nonzero polynomial in finitely many such lifts has nonzero residue, so is a unit. Thus these lifts embed
\(F=\mathbf Q(T_0)\) into \(C\).
The extension \(K/F\) is algebraic. We lift it by adjoining algebraic elements, without any finiteness restriction on that extension. Partially order the pairs consisting of an intermediate field \(F\subseteq L\subseteq K\) and a field embedding \(L\to C\) extending the chosen embedding of \(F\) and inducing the identity on residues. A chain has the union of its fields and embeddings as an upper bound. Zorn's lemma gives a maximal pair.

If \(\theta\in K\setminus L\), let \(p(T)\in L[T]\) be its irreducible polynomial and view its coefficients in \(C\). In characteristic zero, \(p'\ne0\) and \(\deg p'<\deg p\); irreducibility implies \(p'(\theta)\ne0\). For any lift \(x\in C\) of \(\theta\), \(p(x)\) is in the nilpotent maximal ideal \(\mathfrak n\), and \(p'(x)\) is a unit. The correction

\[
x' = x-p(x)p'(x)^{-1}
\]

satisfies \(p(x')\in (p(x))^2\), by expanding the polynomial at \(x\): its constant and linear terms cancel and each remaining term contains the square of the correction. Iteration therefore puts the error in \(\mathfrak n^{2^r}\), which is zero for some finite \(r\). The corrected \(x\) is an exact root with residue \(\theta\). Evaluation gives a unital homomorphism \(L[T]/(p)\to C\). Its domain is the field \(L(\theta)\), so its kernel is zero. This extends the maximal pair, a contradiction. Hence the maximal field is all of \(K\), proving the assertion. The transcendence basis itself exists by the same maximal-chain argument on algebraically independent subsets: maximality makes every remaining element algebraic. No completeness or infinite Newton limit is used.

### The finite-length trace

Localize the first-order pair at a minimal prime of the support of \(N\), using the fraction construction above, and keep the notation \(\mathcal A,\mathcal M\) for the localized objects. Put
\[
R=B_{\mathfrak p},\quad \mathfrak m=\mathfrak pR,\quad
K=R/\mathfrak m,\quad N=N_{\mathfrak p}.
\]
The finite module \(N\) is nonzero and its support is just the closed point.
Indeed a support prime contained in \(\mathfrak p\) equals \(\mathfrak p\) by minimality.
Finiteness gives
\(\operatorname{Supp}N=V(\operatorname{Ann}_RN)\): a product of denominators killing a finite generating set proves the converse to the immediate inclusion.
Hence \(\sqrt{\operatorname{Ann}_RN}=\mathfrak m\).
If \(x_1,\ldots,x_e\) generate \(\mathfrak m\) and each
\(x_j^{a_j}\) annihilates \(N\), every monomial of total degree
\(1+\sum_j(a_j-1)\) annihilates \(N\). Thus
\[
\mathfrak m^sN=0
\tag{7.1k}
\]
for some \(s\geq1\).
Its finite \(\mathfrak m\)-adic filtration has finite-dimensional \(K\)-quotients, so \(N\) has finite positive length. Here length and its additivity are the proved AG-CA 03, Theorem 3.3; refining each vector-space layer by a basis gives its composition series.

Let \(\mathfrak q\subseteq\mathcal A\) be the inverse image of
\(\mathfrak m\). Reduction and centrality of \(h\) give
\[
\mathfrak q^s\mathcal M\subseteq h\mathcal M,\qquad
\mathfrak q^{2s}\mathcal M
 \subseteq h\mathfrak q^s\mathcal M=0.
\tag{7.1l}
\]
The commutative ring \(C=R/\mathfrak m^{2s}\) is Artin: its finite maximal-ideal filtration has finite-dimensional residue-field quotients, since \(\mathfrak m\) is finitely generated. Their finite total composition length bounds the number of strict inclusions in any descending chain of ideals, proving the Artin assertion. Apply the coefficient-field construction above to choose its coefficient field \(K\). Since the \(R\)-action on \(N\) factors through \(C\), this makes \(N\) a finite-dimensional \(K\)-space.

Choose a \(K\)-basis \(n_1,\ldots,n_\ell\) adapted to the
\(\mathfrak m\)-adic filtration and lift it to \(m_i\in\mathcal M\).
Write \(w_i\) for its filtration levels. We say a matrix is strictly block triangular when its \(ij\)-entry is zero unless \(w_j>w_i\).
Multiplication by an element of \(\mathfrak m\) has this property; multiplication by any element of \(R\) preserves the filtration.

Choose coefficient lifts \(\sigma:K\to\mathcal A\) through the chosen field in \(C\), retaining zero as zero. One may choose them \(\mathbf Q\)-linearly. Their reductions in \(R\) need not form a field, and no \(K\)-action on \(\mathcal M\) is asserted. They act on \(N\) as their exact \(K\)-scalars. Products of coefficient lifts agree with the field products modulo
\[
h\mathcal A+\mathfrak q^{2s},
\tag{7.1m}
\]
because their reductions agree modulo \(\mathfrak m^{2s}\).
The reduction of \(\mathfrak q^{2s}\) surjects onto
\(\mathfrak m^{2s}\), by lifting sums of products; subtracting such lifts proves (7.1m).

Take \(a,b\in\mathcal A\) with reductions in \(\mathfrak m\).
Their actions on \(N\) have strictly block-triangular matrices
\(U_0,V_0\) over \(K\).
The identification \(h\mathcal M\simeq N\) in (7.1b) supplies correction matrices \(U_1,V_1\) over \(K\), so that
\[
\begin{split}
a m_i&=\sum_j\sigma((U_0)_{ij})m_j+
                h\sum_j\sigma((U_1)_{ij})m_j,\\
b m_i&=\sum_j\sigma((V_0)_{ij})m_j+
                h\sum_j\sigma((V_1)_{ij})m_j .
\end{split}
\tag{7.1n}
\]
All sums and matrices are finite.

Expand \(abm_i-bam_i\), moving \(a,b\) past these coefficient lifts. There are exactly three kinds of contributions.

First, the leading coefficient matrix has entries
\[
\sum_j\left(
\sigma((V_0)_{ij})\sigma((U_0)_{jk})
-\sigma((U_0)_{ij})\sigma((V_0)_{jk})\right).
\tag{7.1o}
\]
It is strictly block triangular. Its image in \(C\) is
\(V_0U_0-U_0V_0=0\), because the two multiplication operators on \(N\) commute. Each entry of (7.1o) therefore lies in
\(h\mathcal A+\mathfrak q^{2s}\).
The \(\mathfrak q^{2s}\)-part acts by zero by (7.1l).
The remaining part is \(h\) times multiplication by an element of \(R\), applied in an already strictly triangular position.
Since such multiplication preserves filtration, its resulting operator on \(N\) is still strictly block triangular and has zero \(K\)-trace.

Second, moving coefficients gives terms
\[
[a,\sigma((V_0)_{ij})]m_j
 -[b,\sigma((U_0)_{ij})]m_j.
\tag{7.1p}
\]
Each commutator is \(h\) times an element of \(R\).
Each nonzero original position has \(w_j>w_i\).
The same filtration argument makes this contribution to the operator on \(N\) strictly block triangular, of trace zero.

Third, the mixed matrix terms, after division by \(h\) and identification with \(N\), are the ordinary \(K\)-matrix
\[
V_0U_1+V_1U_0-U_0V_1-U_1V_0
 =[V_0,U_1]+[V_1,U_0].
\tag{7.1q}
\]
Coefficient multiplication here is exactly multiplication in \(K\), since it acts on \(N\). The trace of each matrix commutator is zero by interchanging the finite summation indices and using commutativity of \(K\).

It follows from (7.1o)–(7.1q) that multiplication by
\(c=\{\bar a,\bar b\}\) on \(N\), which is the operator obtained from
\([a,b]=hz\), where \(z\in\mathcal A\) lifts \(c\), has zero \(K\)-trace.
For any \(c\in R\), however, multiplication on each quotient
\(\mathfrak m^jN/\mathfrak m^{j+1}N\) is its residue scalar
\(c_0\in K\). In an adapted basis this computes its trace:
\[
\operatorname{tr}_K(c:N\to N)
   =\ell_R(N)\,c_0.
\tag{7.1r}
\]
The length is a positive integer, invertible in \(K\).
Thus the residue of \(\{\bar a,\bar b\}\) is zero. We have proved
\[
\{\mathfrak m,\mathfrak m\}\subseteq\mathfrak m.
\tag{7.1s}
\]

### Return to the radical ideal

The needed commutative facts were proved in AG-CA 02, Theorem 3.1 and Proposition 6.1, and AG-CA 03, Proposition 2.2: prime correspondence for localization, support equal to the annihilator locus for a finite module, and the finite minimal-prime decomposition of a radical in a Noetherian ring. Thus there are finitely many minimal primes
\(\mathfrak p_1,\ldots,\mathfrak p_r\) over
\(\operatorname{Ann}_B N\), with
\[
\sqrt{\operatorname{Ann}_B N}=\bigcap_j\mathfrak p_j.
\]
For completeness, the radical is the intersection of the primes containing the annihilator: if \(f\) is outside that radical, localization of the quotient at its powers is a nonzero ring. A maximal ideal there contracts to a prime containing the annihilator and excluding \(f\), by the proved localized prime correspondence. Every such prime contains a minimal one: the intersection of a descending chain of primes is prime, so the maximal-chain principle applied with reverse inclusion gives a minimal prime below it. This also proves the displayed finite intersection identity. Apply the finite-length trace argument above at each such prime.
For \(f,g\in\mathfrak p_j\), (7.1s) puts
\(\{f,g\}/1\) in \(\mathfrak p_jB_{\mathfrak p_j}\).
Clearing a denominator outside \(\mathfrak p_j\) and using primality gives
\(\{f,g\}\in\mathfrak p_j\).
Therefore each minimal support prime is involutive, and so is their finite intersection. For \(N=0\) the annihilator is the whole ring and the conclusion is immediate.

Applying this result to the first-order Rees pair proves (7.1), with exactly the original commutator Poisson bracket by (7.1c). This completes the full filtered Noetherian statement. \(\square\)

Involutivity here is the coisotropic condition. It requires brackets of two equations for the variety to vanish on the variety. It does **not** require \(\{S,I\}\subset I\): for the zero section, \(\xi_i\in I\) but \(\{\xi_i,x_i\}=1\).

**Corollary 7.1 (componentwise dimension and coisotropy).** Every irreducible component of \(\operatorname{Ch}(M)\) has dimension at least \(d\). In particular \(M\ne0\) implies \(\dim\operatorname{Ch}(M)\geq d\).

**Proof.** For an irreducible component \(C\), remove the other components and choose a smooth point of \(C\). Such points form a dense open set by the proved AG-CA 18, Corollary 3.3. On this open set the ideal in (7.1) is the ideal of \(C\), so the same bracket condition holds. Localization preserves it by the quotient rule and the Leibniz identity.

The cotangent form can be checked directly. For the projection \(\pi:T^*X\to X\), define the tautological one-form by \(\theta_\lambda(v)=\lambda(d\pi(v))\). In cotangent coordinates, \(\theta=\sum_i\xi_i\,dx_i\), so \(\omega=-d\theta=\sum_i dx_i\wedge d\xi_i\) is closed and nondegenerate. The matrix of this form is invertible in every coordinate chart. Its Hamiltonian bracket has \(\{\xi_i,x_j\}=\delta_{ij}\), agreeing with the commutator symbol convention; this follows by solving \(\omega(H_f,-)=df\) in these coordinates and evaluating \(H_f(g)\). Thus the construction glues independently of coordinates. Let \(V=T_p(T^*X)\), of dimension \(2d\), with this form, and \(W=T_pC\). By the tangent-space definition, \(W\) consists exactly of the tangent vectors that annihilate all local equations of \(C\). Linear algebra therefore identifies the span of their differentials with the conormal space, the annihilator of \(W\). The symplectic identification sends this conormal space to \(W^\perp\). Condition (7.1) says that these Hamiltonian vectors annihilate every other defining function, hence are tangent to \(C\). Thus \(W^\perp\subset W\). Since \(\dim W^\perp=2d-\dim W\), it follows that \(2d-\dim W\leq\dim W\), or \(\dim C\geq d\). Nonzero modules have nonempty characteristic varieties by Section 2, giving the last assertion. \(\square\)

By Theorem 7.0, components of dimension \(d\) are Lagrangian at their smooth points: the inclusion has equal dimensions and becomes \(W^\perp=W\). The next lesson studies minimal whole-dimension modules, called holonomic modules. The independent result below proves the dimension bound needed for their finite-length and duality arguments.

### 7.1. An independent whole-dimension bound

The PBW normal form, symbol algebra and left/right Noetherianity are proved in Differential operators and the Weyl algebra, Theorems 3.2, 4.1 and 5.1, including the smooth-affine extension following Theorem 5.1. Good-filtration existence, comparability and characteristic-support independence are proved in Sections 1–2 above. Those proofs use no algebraic closedness: homogeneous generators, bounded-below reduction and symbol annihilators work over any characteristic-zero field. The geometric prerequisites are the dense smooth-locus theorem, AG-CA 18 Corollary 3.3, and the differential-basis coordinate criterion, AG-FSE Theorem 4.1. The normal-direction decomposition, its coherence, and its characteristic-support calculation are proved below. No involutivity theorem, Gabber theorem, or later closed-immersion equivalence is used.

**Theorem 7.2 (whole-dimension Bernstein inequality).** Let \(k\) have characteristic zero, let \(X/k\) be smooth, separated and of finite type, of pure dimension \(d\), and let \(M\ne0\) be a coherent left \(\mathcal D_X\)-module, quasi-coherent over \(\mathcal O_X\). Then

\[
\dim\operatorname{Ch}(M)\ge d.
\tag{7.2}
\]

This concerns the dimension of the whole support. It does not say that every irreducible component has dimension at least \(d\). For a smooth scheme with components of different dimensions, apply the statement separately to each open and closed component where \(M\ne0\); a bound using a larger component where \(M=0\) would be false.

#### Finite normal Taylor decomposition

Let \(R\) be an affine smooth ring with étale coordinates
\((z_1,\ldots,z_s,t_1,\ldots,t_c)\). Put \(I=(t_1,\ldots,t_c)\), \(A=R/I\), and assume \(Z=\operatorname{Spec}A\) is the smooth coordinate subvariety. All coordinate derivations commute. Write \(\partial_i=\partial_{t_i}\), so

\[
[\partial_i,t_j]=\delta_{ij},\qquad [t_i,\partial_j]=-\delta_{ij}.
\tag{7.3}
\]

Let \(L\) be a left \(D_R\)-module on which every \(t_i\) acts locally nilpotently. For each \(m\), if \(t_i^{q_i}m=0\), every sufficiently large total-degree monomial in the commuting \(t_i\) kills \(m\). Thus \(I^qm=0\) for some \(q\) depending on \(m\).

Set

\[
N=\bigcap_i\ker(t_i:L\to L),\qquad
\pi(m)=\sum_{\alpha\in\mathbf N^c}
 \frac{1}{\alpha!}\partial_t^\alpha t^\alpha m.
\tag{7.4}
\]

Every sum is finite on each vector. The projection signs are positive for (7.3). In one variable,
\[
t\partial^a=\partial^at-a\partial^{a-1},\qquad
t^a\partial=\partial t^a-at^{a-1}.
\]
Substitute these into (7.4) and reindex to obtain \(t\pi=0\) and \(\pi\partial=0\). The highest terms vanish by local nilpotence. Different normal directions commute, so the product of the one-variable projections is (7.4). Hence

\[
\pi(L)\subset N,\quad \pi|_N=\mathrm{id},\quad
\pi(\partial_t^\alpha n)=0\quad(n\in N,\ \alpha\ne0).
\tag{7.5}
\]

The reconstruction formula is

\[
m=\sum_{\alpha\in\mathbf N^c}
 \frac{(-1)^{|\alpha|}}{\alpha!}
 \partial_t^\alpha\pi(t^\alpha m).
\tag{7.6}
\]

Insert (7.4) on the right and collect terms with \(\gamma=\alpha+\beta\). The coefficient of \(\partial_t^\gamma t^\gamma m\) is
\[
\sum_{\alpha\le\gamma}
 \frac{(-1)^{|\alpha|}}{\alpha!(\gamma-\alpha)!}
=\frac{1}{\gamma!}\prod_i\sum_{a=0}^{\gamma_i}
 (-1)^a\binom{\gamma_i}{a}.
\]
It is \(1\) for \(\gamma=0\), and \(0\) otherwise. The sums are finite, proving (7.6). Thus reconstruction, unlike projection, has alternating signs.

The sum is direct. For \(n\in N\), commutation followed by (7.5) gives
\[
\pi(t^\alpha\partial_t^\beta n)
=\begin{cases}(-1)^{|\alpha|}\alpha!\,n,&\alpha=\beta,\\
0,&\alpha\ne\beta.
\end{cases}
\tag{7.7}
\]
If \(\alpha\le\beta\), first obtain a scalar multiple of
\(\partial_t^{\beta-\alpha}n\); otherwise a remaining \(t_i\) kills \(n\).
Applying \(\pi t^\alpha\) to a finite relation therefore extracts its
\(\alpha\)-coefficient. We have proved the \(k\)-linear decomposition
\[
L=\bigoplus_{\alpha\in\mathbf N^c}\partial_t^\alpha N.
\tag{7.8}
\]
No assertion that \(R=A[t]\) has been made; it is generally false on an arbitrary étale chart.

#### Tangential action and coherence

The ring \(A\) acts on \(N\) by choosing a coefficient lift to \(R\). Different lifts differ by \(I\), which kills \(N\). The tangential derivations \(\partial_{z_j}\) preserve \(N\), induce the coordinate derivations of \(A\), and satisfy its differential-operator relations. PBW supplies a left \(D_A\)-action.

Suppose \(L\) is finite over \(D_R\). Expand finitely many generators \(m_\ell\) by (7.6). There are finitely many coefficients
\[
n_{\ell,\alpha}=\frac{(-1)^{|\alpha|}}{\alpha!}\pi(t^\alpha m_\ell)\in N.
\]
Let \(N_0\) be their \(D_A\)-span and \(L_0=\sum_\alpha\partial_t^\alpha N_0\).
Normal derivations preserve \(L_0\) by raising exponents. Tangential derivations preserve it because they commute with normal derivations. Coefficient multiplication preserves it by the exact identity
\[
r\partial_t^\alpha n
=\sum_{\beta\le\alpha}(-1)^{|\beta|}
 \binom{\alpha}{\beta}\partial_t^{\alpha-\beta}
 ((\partial_t^\beta r)n).
\tag{7.9}
\]
Here \((\partial_t^\beta r)n\) depends only on its coefficient class in \(A\), and belongs to \(N_0\). PBW therefore makes \(L_0\) a \(D_R\)-submodule. It contains all the original generators, so \(L_0=L\). Applying \(\pi\) gives \(N=N_0\). Thus \(N\) is finite over \(D_A\), and Noetherianity proves coherence.

Sheaf-theoretically, the kernel intersection defining \(N\) is quasi-coherent over \(Z\), because the maps \(t_i\) are coefficient-linear. Kernels commute with localization. Finite generation on this affine chart therefore gives a coherent \(\mathcal D_Z\)-module. This proves the required local nilpotent normal-form fact directly.

#### A good total-order filtration

Choose a good order filtration \(G_jN\) generated in degree zero by finitely many \(D_A\)-generators, with \(G_jN=0\) for \(j<0\). Each piece is finite over \(A\), and \(\operatorname{gr}_G N\) is finite over \(A[\zeta_1,\ldots,\zeta_s]\). Define
\[
F_pL=\bigoplus_{|\alpha|\le p}
 \partial_t^\alpha G_{p-|\alpha|}N\quad(p\ge0),\qquad
F_pL=0\quad(p<0).
\tag{7.10}
\]
Directness and exhaustiveness follow from (7.8). Formula (7.9) makes each piece an \(R\)-submodule.

Each piece is finite over \(R\). Choose finite \(A\)-generators of the finitely many \(G_jN\) for \(0\le j\le p\). For \(a\in A\), choose a lift \(r\in R\); then
\[
\partial_t^\alpha(an)
=\sum_{\beta\le\alpha}\binom{\alpha}{\beta}
 (\partial_t^\beta r)\partial_t^{\alpha-\beta}n.
\]
The finitely many allowed normal powers of those chosen generators therefore generate \(F_pL\) over \(R\). This does not extend an \(A\)-action to the whole \(L\).

Coefficients preserve \(F_p\), and normal and tangential derivations take it into \(F_{p+1}\). PBW proves full order compatibility. Symbols of the chosen generators generate the associated graded over the full symbol ring, so this is a good order filtration.

Send the symbol of \(n\in G_jN\), multiplied by \(\eta^\alpha\), to the symbol of \(\partial_t^\alpha n\) in degree \(j+|\alpha|\). The direct sum (7.10) proves bijectivity degree by degree. In (7.9), terms with \(\beta\ne0\) lower the total filtration degree, so the coefficient action on the associated graded is through \(R\to A\). Tangential symbols act on \(\operatorname{gr}N\), and normal symbols multiply by \(\eta_i\). Also
\[
t_i\partial_t^\alpha n=-\alpha_i\partial_t^{\alpha-e_i}n,
\]
so \(t_iF_pL\subset F_{p-1}L\). We obtain an actual graded symbol-module isomorphism
\[
\begin{aligned}
\operatorname{gr}_F L&\simeq(\operatorname{gr}_G N)[\eta_1,\ldots,\eta_c],\\
I\operatorname{gr}_F L&=0.
\end{aligned}
\tag{7.11}
\]

Its support, inside the closed coefficient locus \(Z\), is
\(\operatorname{Ch}_Z(N)\times\mathbf A^c\) in these cotangent coordinates.
Indeed the annihilator of a polynomial extension is the polynomial extension of the annihilator: a polynomial annihilates every constant vector exactly when each coefficient does. Each reduced support component becomes its product with affine \(c\)-space. Adjoining \(c\) independent transcendental variables to its function field adds \(c\) to its dimension. Characteristic-support independence gives
\[
\dim\operatorname{Ch}_U(L)=\dim\operatorname{Ch}_Z(N)+c.
\tag{7.12}
\]

#### Proof of the theorem

The coefficient support of a coherent D-module is locally closed without an infinite-union argument. On an affine chart choose finitely many D-generators and their \(\mathcal O\)-span \(H\). This span is coherent over the Noetherian coefficient ring. Its stalk is zero precisely when all the generators vanish on a neighborhood, precisely when the D-module stalk is zero. Thus the coefficient support equals \(\operatorname{Supp}H\) on that chart. These local closed sets agree, giving a closed set \(S=\operatorname{Supp}_{\mathcal O_X}M\).

Choose a maximal-dimensional irreducible component \(Z\) of \(S\), of dimension \(s\), and its generic point \(\gamma\). Give \(Z\) its reduced structure. The earlier dense smooth-locus theorem applies in characteristic zero. Remove the other support components and the nonsmooth locus of \(Z\). After shrinking about \(\gamma\), the support is exactly the smooth closed subvariety \(Z\).

We construct an affine adapted coordinate neighborhood \(U\), with \(Z\cap U=V(t_1,\ldots,t_c)\), \(c=d-s\), and tangent coordinates \(z_1,\ldots,z_s\). Put \(K=k(Z)\) and let \(I\) be the ideal of \(Z\). Smooth local rings are regular by AG-CA 18 Theorem 3.2, and the height formula, AG-CA 09 Theorem 4.3, gives \(\dim\mathcal O_{X,\gamma}=c\). Its maximal ideal is \(I_\gamma\), so \(I_\gamma/I_\gamma^2\) has dimension \(c\) over \(K\). The conormal sequence and separable-field differential calculation, AG-CA 16 Theorem 3.3 and Theorem 6.2, give
\[
I_\gamma/I_\gamma^2\longrightarrow
\Omega^1_{X/k}\otimes K\longrightarrow\Omega^1_{K/k}\longrightarrow0.
\]
The middle and last dimensions are \(d\) and \(s\). Thus the first map has rank \(c\) and is injective; independence of the conormal differentials has been justified at the actual generic point.

Choose \(t_1,\ldots,t_c\in I\) representing this basis and a separating transcendence basis \(z_1,\ldots,z_s\) of \(K/k\). After shrinking, the \(z_j\) are regular on \(Z\) and have coefficient lifts to \(X\). Their differentials together with the \(dt_i\) form a basis of the differential fibre at \(\gamma\). Nakayama gives \(I_\gamma=(t_1,\ldots,t_c)_\gamma\). The finite ambient module \(I/(t_1,\ldots,t_c)\) then vanishes on a principal neighborhood by clearing denominators, so these equations define \(Z\cap U\) scheme-theoretically. Invert the determinant of the combined differentials and apply the earlier coordinate criterion, which holds at arbitrary scheme points. The resulting map \(U\to\mathbf A_k^d\) is étale. Its base change along the zero normal-coordinate locus makes \(Z\cap U\to\mathbf A_k^s\) étale too. No splitting of the coefficient ring is asserted.

Put \(L=\Gamma(U,M)\). It is finite over \(D_R\). Since \(M|_{D(t_i)}=0\), quasi-coherent affine localization gives \(L[t_i^{-1}]=0\), so each \(t_i\) acts locally nilpotently. Apply the proved normal decomposition and filtration.

The resulting \(N\) is nonzero at \(\gamma\). Kernels commute with stalk localization, and (7.6) holds in the localized module too. If their intersection were zero there, reconstruction would force \(M_\gamma=0\).

We have \(\dim\operatorname{Ch}_Z(N)\ge s\) by an elementary graded support argument, rather than a Bernstein inequality on \(Z\). Choose the filtration above generated in degree zero. Its degree-zero term is nonzero at \(\gamma\): its elements generate \(N\) over \(D_Z\), so their simultaneous vanishing would imply \(N_\gamma=0\). The degree-zero part of
\[
(\operatorname{gr}N)/(\zeta_1,\ldots,\zeta_s)\operatorname{gr}N
\]
at \(\gamma\) is that nonzero coefficient space. More explicitly, \(E=(\operatorname{gr}_G N)\otimes_A K\) is nonnegatively graded with \(E_0\ne0\). Hence \(E/(\zeta)E\ne0\); this quotient remains nonzero on localization at \((\zeta)\subset K[\zeta]\), so \(E\) also remains nonzero there. Thus the zero cotangent vector over \(\gamma\) belongs to \(\operatorname{Ch}_Z(N)\). Closedness makes its closure, the zero section over \(Z\cap U\), belong to that support. Its dimension is \(s\).

Equation (7.12) now yields
\[
\dim\operatorname{Ch}_U(M)\ge s+c=d.
\]
Characteristic support restricts to \(T^*U\); its dimension there is at most its global dimension. This proves (7.2). The argument includes \(c=0\), with no normal variables and identity projection, and \(s=0\), with no tangential variables. \(\square\)

The inequality holds for right modules as well. The canonical-bundle side change proved in the preceding connection lesson sends a right module to a coherent left module. In a volume trivialization, transposition fixes coefficient symbols and negates covector symbols; its volume correction has order zero. The induced map \((x,\xi)\mapsto(x,-\xi)\) preserves each conic characteristic support, and tensoring with a line bundle changes no support. Thus it preserves characteristic dimension and the left inequality applies.

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

Theorem 7.0 proves radical-annihilator involutivity in the full filtered Noetherian setting, using the first-order Rees quotient, exact fraction localization, the finite Artin coefficient field and the finite-length trace. Corollary 7.1 proves coisotropy and the dimension bound for each irreducible characteristic component. Theorem 7.2 separately proves the whole-dimension inequality without using involutivity. No step infers radical bracket closure merely from bracket closure of an unreduced symbol ideal.

The remaining imported background consists of elementary support and length theory for finite modules over Noetherian commutative rings, smooth adapted étale coordinates for a smooth closed embedding, and the cotangent bundle's nondegenerate symplectic form. The normal-form and Noetherian arguments for \(\mathcal D_X\), and canonical-bundle side-changing, were proved in the preceding lessons. This lesson proves filtration existence and comparability, support and multiplicity independence, the exact-sequence statements, the cyclic hypersurface formula, the zero-section criterion, and all displayed characteristic-variety and cycle calculations. It does not prove regularity or classify all extensions of the punctured-line connection.

## References

- M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §6.4 and §10.1, for involutivity and the characteristic variety of analytic D-modules; V. Ginzburg, [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), for good filtrations. The Rees Noetherian argument above proves the good-submodule property in the algebraic setting used here.
- Victor Ginzburg, with Vladimir Baranovsky and Sam Evens, *Lectures on D-modules*, 1998, Sections 1.1.10–1.1.23 for good filtrations and lattice comparison; Theorem 1.2.5 and Corollary 1.2.10 for involutivity. [University-hosted notes](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf). Multiplicities in this lesson are the generic composition lengths (3.1); Exercise 8.3 explains why reduction before taking a rank loses information.
- Jyoti Singh and Shiv Datt Kumar, *On the Involutivity of the Characteristic Variety*, Sections 3–5. [Free full-text version uploaded by the author](https://www.researchgate.net/publication/263610454_On_the_Involutivity_of_the_Characteristic_Variety). The coefficient-field construction and the full first-order trace calculation used here are proved in Section 7.
- Roman Bezrukavnikov, *Noncommutative Algebra*, MIT 18.706, spring 2023, Section 24.6 for the related filtered growth dimension of a module. [Open course materials](https://ocw.mit.edu/courses/18-706-noncommutative-algebra-spring-2023/). That dimension and the Bernstein filtration will be treated in the next lesson.
- Alexander Beilinson and Vladimir Drinfeld, [*Quantization of Hitchin's integrable system and Hecke eigensheaves*, free author draft](https://www.math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf), Section 1.1.4 for the filtration on differential operators and its cotangent interpretation. The calculation here concerns smooth varieties; it does not assume a global filtration on a stack.
- The Stacks project, *Commutative Algebra*, [Tag 09CH, Differential operators](https://stacks.math.columbia.edu/tag/09CH), as compared in the [AI Integrated Stacks Project English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#section-differential-operators). AI Integrated Stacks Project is an edition with AI-proposed corrections and additions, not reviewed by the official Stacks maintainers. The characteristic variety and cycle constructions here go beyond that section.
