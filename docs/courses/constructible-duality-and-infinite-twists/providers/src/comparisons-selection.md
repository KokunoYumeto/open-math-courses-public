# Natural comparisons with infinite locally constant coefficients — proof selection

*Written by GPT-6.1 Sol (OpenAI), Ultra. Original exposition is public domain (CC0). The mathematical antecedents are credited below.*

This selection retains the complete natural-comparison arguments used by the duality lesson. The geometric stability of weak constructibility, the small-ball theorem, finite constructible duality and the bounded sheaf-operation results remain their stated prerequisite contracts. A locally constant twist may have infinite modules; finite evaluation is used for the untwisted constructible objects.

Complete original source · Editable proof selection · Reuse terms · Provenance

## Coefficients, bounds and the geometric criterion

Manifolds and maps are real analytic, Hausdorff and countable at infinity, with uniform finite dimension bounds. Vector bundles have fixed finite rank. Let \(k\) be a commutative ring of finite global dimension \(g\). Every input below is an actual bounded derived object. No Noetherian, finite-generation or perfect-stalk assumption is made.

The criterion we will apply repeatedly is

\[
H\text{ is weakly }\mathbb R\text{-constructible}
\quad\Longleftrightarrow\quad
\operatorname{SS}(H)\text{ is contained in a closed conic
subanalytic isotropic set}.
\tag{1}
\]

For such an \(H\), its actual \(\operatorname{SS}(H)\) is itself closed, conic, subanalytic and Lagrangian, hence isotropic. The empty set is allowed for the zero object.

The boundedness inputs must accompany the geometric estimates. Exact inverse image, derived tensor over this ring and the finite-dimensional direct/exceptional image operations preserve boundedness in the cases used here. Internal Hom has the explicit sufficient bound

\[
A\in D^{[a,b]}(k_X),\quad B\in D^{[c,d]}(k_X)
\ \Longrightarrow\
R\mathcal Hom(A,B)\in
D^{[c-b,\ d-a+3\dim X+g+1]}(k_X).
\tag{2}
\]

This is the existing bounded-Hom prerequisite, for arbitrary bounded coefficients. Normal specialization and Fourier transformation in fixed rank have finite amplitude as well. We retain these inputs rather than infer boundedness just from a symbol \(R\mathcal Hom\) or from fibrewise bounded stalks.


## Natural comparisons with infinite locally constant coefficients

The following results develop Andreas Hohl and Pierre Schapira's freely accessible paper [*Unusual functorialities for weakly constructible sheaves*](https://arxiv.org/html/2303.11189v2). Its new comparisons permit an arbitrary bounded locally constant coefficient complex. Its opening stability statements and small-ball lemma refer to earlier foundations; the proofs above and the small-ball lesson supply those arguments here, with their stronger arbitrary-module and support hypotheses retained.

Kashiwara and Schapira's freely available [*Microlocal Study of Sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf) gives the earlier perfect-stalk stability results. Its geometric proofs refer onward to microsupport estimates, normal-cone isotropy and Fourier transport. The explicit compactness, limiting-covector and bounded-operation arguments in this lesson retain those individual prerequisites; the later perfect-operation lesson supplies the finite coefficient arguments.

We keep the coefficient and manifold conventions of this lesson. A locally constant complex means a bounded derived object locally isomorphic to \(L_U\), for \(L\in D^b(k)\). In particular, the individual modules of \(L\) can be infinite. All tensors in this extension are derived, and every comparison is the usual map obtained from evaluation, adjunction or projection, rather than an unspecified isomorphism between its two objects.

### Small balls give the actual point comparisons

For weakly constructible \(G\), a point \(x\), and arbitrary \(L\in D^b(k)\), the natural maps are isomorphisms:

\[
\begin{aligned}
\bigl(R\mathcal Hom(L_X,G)\bigr)_x
&\longrightarrow R\operatorname{Hom}_k(L,G_x),\\
(i_x^!G)\otimes L
&\longrightarrow i_x^!(G\otimes L_X).
\end{aligned}
\tag{18}
\]

**Proof.** Use the small-ball theorem in a coordinate chart, with its compact support cutoff. It gives a cofinal basis of balls \(U\) on which the natural ordinary and compact comparisons for \(G\) are respectively \(R\Gamma(U;G)\simeq G_x\) and \(i_x^!G\simeq R\Gamma_c(U;G)\). The preceding stability proof also applies to \(R\mathcal Hom(L_X,G)\) and \(G\otimes L_X\). Shrink the balls so that their comparisons stabilize as well.

For every such ball, constant-sheaf adjunction and proper-support projection give

\[
\begin{aligned}
R\Gamma(U;R\mathcal Hom(L_U,G|_U))
&\simeq R\operatorname{Hom}_k(L,R\Gamma(U;G)),\\
R\Gamma_c(U;G|_U)\otimes L
&\simeq R\Gamma_c(U;G|_U\otimes L_U).
\end{aligned}
\tag{19}
\]

For the first identity, tensor–Hom adjunction followed by the adjunction between the constant-sheaf functor and sections gives the indicated derived coefficient Hom. For the second use projection for \(a_U:U\to\{\mathrm{pt}\}\), whose proper-support functor is compact cohomology. Neither identity needs a finite first Hom argument or a perfect tensor factor.

Insert the stabilized values into (19). Naturality in restriction and inclusion of supports identifies the resulting maps with (18): the stalk map is restriction followed by evaluation, and the costalk map is the tensor–exceptional comparison followed by the compact comparison. Thus these particular maps are invertible. We have applied Hom to an already stabilized value, never interchanged infinite Hom with an arbitrary filtered colimit. \(\square\)

### Costalks detect a weakly constructible object

**Lemma.** If \(H\) is bounded and weakly constructible and every \(i_x^!H\) vanishes, then \(H=0\). Consequently a morphism between bounded weakly constructible objects is an isomorphism if all its costalk maps are isomorphisms.

**Proof.** A constant complex \(A_B\) on a \(d\)-dimensional coordinate ball has

\[
i_x^!A_B\simeq A\otimes \mathrm{or}_{B,x}^{\vee}[-d].
\tag{20}
\]

This is the relative ball/sphere calculation, retaining the orientation line. For \(d=1\), ordinary restriction to the two punctured components is the diagonal \(A\to A\oplus A\); its difference quotient is \(A\), and its fibre is \(A[-1]\). For larger \(d\), a finite cellular cochain complex for the ball/sphere pair has one relative top generator; tensoring it with \(A\) gives (20). This finite free calculation is valid for arbitrary coefficient modules. The zero-dimensional case is ordinary evaluation. A line and a shift are invertible, so (20) vanishes exactly when \(A\) does.

Choose a locally finite subanalytic stratification on which the finitely many cohomology sheaves of \(H\) are locally constant, refining it to connected strata with the frontier condition. If \(H\neq0\), choose a stratum \(S\) of maximal dimension among those with nonzero cohomology. Near a point \(x\in S\), all other nonzero strata can be excluded: there are locally only finitely many of them, and if the closure of one met \(S\), the frontier condition would make its dimension strictly greater than \(\dim S\), contrary to maximality. Shrink also so that \(S\) is closed in the chosen ambient neighborhood.

On a smaller ball in \(S\), the whole derived restriction of \(H\) is constant. Here is why cohomological local constancy suffices. Trivialize all its finitely many cohomology sheaves on that ball. Constant sheaves with arbitrary coefficients are acyclic on smaller convex balls. The bounded hypercohomology sequence therefore identifies every cohomology group of its section complex with the corresponding stalk module. The counit from the constant section complex to the restriction is an isomorphism on every stalk, and hence is an isomorphism of derived sheaves.

In this neighborhood \(H\) has no stalks outside the closed \(S\). Closed-complement localization identifies it with the closed direct image of its restriction to \(S\). Exceptional composition then identifies its costalk at \(x\) with the intrinsic costalk on \(S\). Equation (20) makes that costalk a nonzero shifted, orientation-twisted coefficient, a contradiction. The morphism assertion follows by applying this argument to its cone, which remains bounded and weakly constructible. \(\square\)

The diagonal in dimension one is essential: an infinite module can be abstractly isomorphic to its double. Its natural restriction map can still have a nonzero cokernel.

### Analytic inverse images commute with these coefficients

Let \(f:X\to Y\) be analytic, let \(G\) be bounded weakly constructible, and let \(M\) be bounded locally constant on \(Y\). Then

\[
\begin{aligned}
f^{-1}R\mathcal Hom(M,G)
&\xrightarrow{\sim}R\mathcal Hom(f^{-1}M,f^{-1}G),\\
f^!G\otimes f^{-1}M
&\xrightarrow{\sim}f^!(G\otimes M).
\end{aligned}
\tag{21}
\]

**Proof.** Work near \(y=f(x)\), where \(M=L_Y\). At \(x\), the first comparison is the identity of \(R\operatorname{Hom}_k(L,G_y)\), by (18) and ordinary stalk composition. Stalks detect isomorphisms of sheaves, proving the first line.

For the second line take a costalk at \(x\). Equation (18), first for \(f^!G\) and then for \(G\), and exceptional composition identify the comparison with

\[
(i_x^!f^!G)\otimes L
\simeq(i_y^!G)\otimes L
\xrightarrow{\sim}i_y^!(G\otimes L_Y)
\simeq i_x^!f^!(G\otimes L_Y).
\tag{22}
\]

The two objects in the second line of (21) are bounded weakly constructible by the preceding stability sections. The costalk lemma proves that their canonical comparison is invertible. Local computations glue because all maps are the canonical ones. No noncharacteristic or perfection assumption on \(M\) is needed. \(\square\)

### Two different positions for the perfect factor

The elementary algebraic input is

\[
R\operatorname{Hom}_k(L,A)\otimes P
\xrightarrow{\sim}R\operatorname{Hom}_k(L,A\otimes P),
\qquad P\ \text{perfect},\quad L,A\in D^b(k).
\tag{23}
\]

For \(P=k\) this is the identity. Finite sums, shifts and direct summands give the result for a finite projective module in any degree. Represent a perfect \(P\) by a bounded finite-projective complex and filter it by its finitely many terms. Both sides and the comparison respect the resulting triangles. Induction and the five lemma give (23). This proves invertibility of the natural map, with no finiteness imposed on \(L\) or \(A\).

If \(K\) is bounded locally constant, \(G\) is bounded weakly constructible, and \(P\) is \(\mathbb R\)-constructible with perfect stalks, then

\[
\begin{aligned}
R\mathcal Hom(K,G)\otimes P
&\xrightarrow{\sim}R\mathcal Hom(K,G\otimes P),\\
R\mathcal Hom(P,G)\otimes K
&\xrightarrow{\sim}R\mathcal Hom(P,G\otimes K).
\end{aligned}
\tag{24}
\]

**Proof of the first line.** Locally put \(K=L_X\). At \(x\), (18) identifies the comparison with (23) for \(A=G_x\) and perfect \(P_x\). Stalks detect its invertibility.

For the second line we need the external comparison, and give its proof rather than infer it from Hom of ordinary stalks. For projections \(q_1,q_2:X\times X\to X\) there is the evaluation map

\[
D_XP\boxtimes G
\longrightarrow R\mathcal Hom(q_1^{-1}P,q_2^!G).
\tag{25}
\]

On a rectangle \(U\times V\), exceptional adjunction for its second projection and proper-support base change identify sections of the right side with

\[
R\operatorname{Hom}_k(R\Gamma_c(U;P),R\Gamma(V;G)).
\tag{26}
\]

Indeed the proper-support image of the first projection's inverse image of \(P|_U\) is the constant complex on \(V\) with value \(R\Gamma_c(U;P)\); adjunction with sections gives (26). These identities commute with shrinking both factors.

Choose cofinally small \(U\) at \(x\). The actual small-ball comparison identifies \(R\Gamma_c(U;P)\) with the perfect \(C_x=i_x^!P\). In the second variable stalk passage in (26) is valid because \(R\operatorname{Hom}_k(C_x,-)\) is represented by a bounded finite-projective dual tensor, which commutes with filtered stalk passage. Thus the right side's stalk at \((x,y)\) is \(R\operatorname{Hom}_k(C_x,G_y)\). The left side's stalk is \(C_x^\vee\otimes G_y\), by the stalk–costalk formula for \(D_XP\). Finite-projective evaluation identifies these stalks and is precisely (25) on them. This proves (25). This argument would also allow an arbitrary bounded \(G\).

Put \(H=D_XP\boxtimes G\) and let \(\delta:X\to X^2\) be the diagonal. The bounded exceptional internal-Hom identity and \(q_i\delta=\operatorname{id}\) give

\[
\delta^!H\simeq R\mathcal Hom(P,G).
\tag{27}
\]

The object \(D_XP\) is constructible by constructible duality, so \(H\) is weakly constructible. Apply the second line of (21) to \(\delta\), \(H\), and the locally constant \(q_2^{-1}K\). Using (25)–(27) before and after tensoring gives

\[
\delta^!H\otimes K
\xrightarrow{\sim}\delta^!(H\otimes q_2^{-1}K)
\simeq R\mathcal Hom(P,G\otimes K).
\tag{28}
\]

All external comparisons are evaluation maps; exceptional comparison is constructed by currying evaluation and trace. Their associativity identifies (28) with the second natural map in (24), including Koszul symmetry. This proves that map invertible. \(\square\)

In the first line of (24) perfection is in the tensor factor \(P\); in the second it is in the first Hom argument. Neither line asserts that a tensor with an arbitrary weak coefficient can be moved out of any Hom.

### An ambient extension controls an open boundary

Let \(j:U\hookrightarrow X\) be open and subanalytic, and suppose \(F\) on \(U\) is the restriction of a bounded weakly constructible \(G\) on \(X\). Let \(K\) be bounded locally constant on \(X\). Then

\[
\begin{aligned}
j_!R\mathcal Hom(j^{-1}K,F)
&\xrightarrow{\sim}R\mathcal Hom(K,j_!F),\\
(Rj_*F)\otimes K
&\xrightarrow{\sim}Rj_*(F\otimes j^{-1}K).
\end{aligned}
\tag{29}
\]

**Proof.** The two ambient descriptions are

\[
j_!F=k_U\otimes G,\qquad
Rj_*F=R\mathcal Hom(k_U,G),
\tag{30}
\]

where \(k_U=j_!k\) has perfect stalks. Apply the first line of (24) with \(P=k_U\). Its left side is \(j_!j^{-1}R\mathcal Hom(K,G)=j_!R\mathcal Hom(j^{-1}K,F)\), by open restriction. Its right side is \(R\mathcal Hom(K,j_!F)\). This gives the first natural map in (29).

The second line of (24), again with \(P=k_U\), gives
\(R\mathcal Hom(k_U,G)\otimes K\simeq R\mathcal Hom(k_U,G\otimes K)\). Equation (30) identifies these with the second map's two objects. All identities use the actual open adjunctions. Relative compactness is sufficient when needed below, but this proof only needs a subanalytic open set and the specified ambient extension. It does not assert this extension exists for an arbitrary weakly constructible object on \(U\). \(\square\)

### Nonproper maps with controlled behavior at infinity

A **b-analytic manifold** here is a pair \(X_\infty=(X,\widehat X)\), with \(X\) an open relatively compact subanalytic subset of a real analytic manifold \(\widehat X\). Write \(j_X:X\hookrightarrow\widehat X\). A morphism \(f:X_\infty\to Y_\infty\) is an analytic map \(f:X\to Y\) whose graph is subanalytic in \(\widehat X\times\widehat Y\). A bounded \(F\) is weakly constructible up to infinity if \(j_{X!}F\) is weakly constructible on \(\widehat X\).

Equivalently \(Rj_{X*}F\) is weakly constructible there. In one direction apply (30) with \(G=j_{X!}F\); in the other use \(j_{X!}F=k_X\otimes Rj_{X*}F\). Both implications are instances of the preceding tensor/Hom stability. The same equivalence with perfect stalks follows from perfect operations.

**Theorem.** Let \(f:X_\infty\to Y_\infty\) be such a morphism and \(F\) bounded weakly constructible up to infinity. Then \(Rf_!F\) and \(Rf_*F\) are bounded weakly constructible up to infinity on **\(Y_\infty\)**. For bounded locally constant \(M\) on \(Y\), the natural comparisons on \(Y\) are

\[
\begin{aligned}
Rf_!R\mathcal Hom(f^{-1}M,F)
&\xrightarrow{\sim}R\mathcal Hom(M,Rf_!F),\\
(Rf_*F)\otimes M
&\xrightarrow{\sim}Rf_*(F\otimes f^{-1}M).
\end{aligned}
\tag{31}
\]

**Proof of the image assertion.** Put \(Z=\widehat X\times\widehat Y\), with projections \(q_1,q_2\), and \(\Gamma=\Gamma_f\). The graph is closed in the open \(X\times Y\), so it is locally closed in \(Z\); its subanalytic cutoff \(k_\Gamma\) is constructible with perfect stalks. Define

\[
\begin{aligned}
A(F)&=q_1^{-1}j_{X!}F\otimes k_\Gamma,\\
B(F)&=R\mathcal Hom(k_\Gamma,q_1^!Rj_{X*}F).
\end{aligned}
\tag{32}
\]

These two objects are bounded weakly constructible by the preceding stability theorem. Their closed supports lie in \(\overline\Gamma\), a compact subset of \(Z\), because \(\Gamma\subset X\times Y\) and both factors are relatively compact. Consequently \(q_2\) is proper on these actual supports.

The graph formulas, with their natural maps, are

\[
Rf_!F\simeq j_Y^{-1}Rq_{2!}A(F),\qquad
Rf_*F\simeq j_Y^{-1}Rq_{2*}B(F).
\tag{33}
\]

For the first factor the graph embedding followed by \(q_2\), using ordinary restriction and zero extension. For the second use
\(R\mathcal Hom(k_\Gamma,H)=Ri_{\Gamma*}i_\Gamma^!H\). Exceptional composition identifies \(i_\Gamma^!q_1^!Rj_{X*}F=j_X^!Rj_{X*}F=F\). Restricting to the open \(Y\) then gives ordinary graph-image composition. Open \(j_Y^!\) and \(j_Y^{-1}\) coincide; this does not replace an exceptional inverse image for a general map.

Proper-support image stability makes both ambient images in (33) weakly constructible. Their restriction followed by \(j_{Y!}\) is their tensor with \(k_Y\), hence still weakly constructible. This proves the claim on the target pair. If \(F\) is constructible up to infinity with perfect stalks, every operation in (32), the proper images and the final cutoff preserves perfection by the existing perfect-operation and compact-fibre proofs. Thus both images are constructible up to infinity in this stronger sense as well.

**Proof of the comparisons.** The question is local on the output \(Y\). On a chart where \(M=L_Y\), we can test the canonical maps using the globally constant \(L_Y\): open base change restricts both images to that chart and their inputs to its inverse image. This does not assume a global constant trivialization, or an extension of \(M\) to \(\widehat Y\). Set \(L_Z\) and \(L_{\widehat X},L_{\widehat Y}\) to be the associated constant complexes.

For the first line of (31), (29), the first line of (21), and the first line of (24) with \(P=k_\Gamma\) give

\[
A(R\mathcal Hom(L_X,F))
\simeq R\mathcal Hom(L_Z,A(F)).
\tag{34}
\]

To spell out the order: commute \(j_{X!}\) with Hom from the constant coefficient using (29); commute \(q_1^{-1}\) with that Hom using (21); then move the perfect cutoff \(k_\Gamma\) into its target using (24). Every sheaf here has support in the compact \(\overline\Gamma\).

Internal-Hom direct-image adjunction always identifies
\(Rq_{2*}R\mathcal Hom(q_2^{-1}L_{\widehat Y},A(F))\)
with \(R\mathcal Hom(L_{\widehat Y},Rq_{2*}A(F))\). It follows by tensor–Hom adjunction and ordinary inverse/direct adjunction on each output open set; all operations are bounded. Support properness changes both images of the graph coefficients from \(*\) to \(!\). Equation (33) and open restriction now identify this adjunction map with the first comparison of (31).

For the second comparison, use (29) for \(j_X\), the exceptional line of (21) for \(q_1\), and the second line of (24) with first Hom argument \(k_\Gamma\). They give, in that order,

\[
B(F\otimes L_X)\simeq B(F)\otimes L_Z.
\tag{35}
\]

Projection for \(Rq_{2!}\) with arbitrary \(L\) is invertible; properness on the graph coefficient support identifies it with the ordinary-image projection for \(B(F)\). After (33) and open restriction this is the second comparison of (31). Evaluation and projection in (34)–(35) show that the resulting isomorphisms are the stated canonical maps. Their local forms therefore glue for arbitrary locally constant \(M\). \(\square\)

There is no properness assumption on \(f\) itself. Compact control entered through the graph coefficients in the ambient pair, and is additional information beyond weak constructibility on \(X\).

