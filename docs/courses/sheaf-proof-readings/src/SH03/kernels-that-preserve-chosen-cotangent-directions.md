# Kernels that preserve chosen cotangent directions

A sheaf kernel can be useful in a cotangent region even when its support is nonproper. What matters in that region is whether its possible intermediate points and covectors can escape. We will impose a compactness condition on the kernel's cotangent relation, prove a composition estimate, and use it to define operators between localized sheaf categories.

The ordinary convolution and its associativity are prerequisites from Composing sheaf operators through an intermediate space. We also use the enlarged tensor estimate from Cotangent directions that survive a limiting operation, the microlocal proper-image theorem from Covectors at a boundary and at infinity, and the quotient category described in Categories and operations in one cotangent direction. The exact statements used here are given below.

The main source mechanism is Kashiwara and Schapira's *Microlocal Study of Sheaves*, Proposition 6.3.1, Remark 6.3.2 and Proposition 6.3.3, pp. 108–111. Their compactness argument bounds the forgotten covectors in an enlarged sum and then applies their Theorem 4.4.2. Here that argument is written for tensor convolution, with an arbitrary second kernel in Theorem 2, and with the compact preimage and quotient arguments supplied separately. The source's printed kernel conditions use conic regions and, for its Hom transform, an antipode on the output projection. The present convention instead twists the input covector as in (2); its general open-region claims are justified by the local compact-neighborhood proofs below.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

## Keeping only a cotangent region

Let \(k\) be a commutative ring with identity and finite global dimension \(g\). Our manifolds are smooth, Hausdorff, finite dimensional and countable at infinity. Complexes belong to \(D^b(k_M)\), with one global finite cohomological interval. Their cohomology sheaves may be arbitrary: neither constructibility nor finite generation is assumed. Derived tensor products are over \(k\). The finite coefficient and manifold dimension bounds ensure that the convolutions and direct images used below stay bounded. We use \(H^j(F[s])=H^{j+s}(F)\).

For an open subset \(\Omega\subset T^*M\), put

\[
\mathcal Z_M(\Omega)=\{F:\operatorname{SS}(F)\cap\Omega=\varnothing\},
\qquad
\mathcal D_M(\Omega)=D^b(k_M)/\mathcal Z_M(\Omega).
\tag{1}
\]

The subset \(\Omega\) need not be conic and may meet the zero section. The triangle inequality for microsupport makes \(\mathcal Z_M(\Omega)\) thick. The quotient inverts a morphism precisely when its cone has microsupport disjoint from \(\Omega\). Microsupport restricted to \(\Omega\) depends only on the quotient object. These are the quotient-category facts we use; no comparison with global sections of microlocal Hom is needed.

Write \(a(x,\xi)=(x,-\xi)\). For a bounded kernel \(K\) on \(X\times Y\), its twisted relation in chosen regions is

\[
\mathcal C_K=
\{((x,\xi),(y,\alpha)):
(x,y;\xi,-\alpha)\in\operatorname{SS}(K),\ (x,\xi)\in\Omega_X\}.
\tag{2}
\]

The input covector is \(\alpha\), so the actual \(Y\) component of the kernel covector is \(-\alpha\). We call \(K\) **admissible from \(\Omega_Y\) to \(\Omega_X\)** when

\[
\mathcal C_K\subset\Omega_X\times\Omega_Y,
\qquad
\mathcal C_K\longrightarrow\Omega_X
\quad\text{is proper}.
\tag{3}
\]

Properness means that the inverse image of every compact subset is compact. Thus a compact set of output covectors controls both the intermediate point \(y\) and the entire input covector \(\alpha\). This is stronger than merely confining \(y\).

The definition uses only microsupport on \(\Omega_X\times T^*Y\). It therefore defines a full subcategory \(\mathcal K(\Omega_X,\Omega_Y)\) of \(\mathcal D_{X\times Y}(\Omega_X\times T^*Y)\). Indeed, changing a representative by a localized isomorphism preserves precisely this portion of its microsupport. The subcategory is triangulated: for a cone, its relation is contained in the union of the two preceding relations; that finite union is proper over \(\Omega_X\), and the cone relation is relatively closed in it. Shifts preserve the relation. The same closed-subset argument applies to direct summands.

## Two estimates and the compactness they require

For closed conic subsets \(A,B\subset T^*M\), the enlarged sum \(A\widehat+ B\) allows nearby base points. In a smooth coordinate chart, \((u_0,\lambda_0)\) belongs to it precisely when there are

\[
(u_n,\lambda_n)\in A,\qquad (v_n,\mu_n)\in B,
\]

with

\[
u_n,v_n\longrightarrow u_0,\qquad
\lambda_n+\mu_n\longrightarrow\lambda_0,\qquad
|u_n-v_n|\,|\lambda_n|\longrightarrow0.
\tag{4}
\]

This is a coordinate description of the smooth invariant operation defined by the normal-cone construction. We use the general estimate

\[
\operatorname{SS}(E\otimes^L F)
\subset\operatorname{SS}(E)\widehat+\operatorname{SS}(F)
\tag{5}
\]

for bounded complexes. It requires no noncharacteristic hypothesis. When the two summand covectors in (4) remain bounded, a subsequence converges in both summands, and closedness produces an ordinary sum at one common base point. Admissibility will give exactly this boundedness in our output region.

The direct-image input concerns a projection \(q:M\times Y\to M\). Define

\[
P:T^*(M\times Y)\longrightarrow T^*M\times Y,
\qquad P(m,y;\lambda,\nu)=(m,\lambda,y).
\tag{6}
\]

For a bounded complex \(H\), the required condition is

\[
\overline{P(\operatorname{SS}(H))}\cap(\Omega\times Y)
\longrightarrow\Omega
\quad\text{proper}.
\tag{7}
\]

The closure in (7) is part of the condition. Equivalently, for every compact \(C\subset\Omega\) there is a compact \(B_C\subset Y\) such that

\[
\operatorname{SS}(H)\cap(C\times T^*Y)
\subset C\times T^*Y|_{B_C}.
\tag{8}
\]

The equivalence uses a compact neighborhood \(C'\subset\Omega\) of \(C\). Control over \(C'\) confines the \(Y\) coordinates of every sequence whose \(M\) covectors approach \(C\), thereby controlling the closure. The open set \(\Omega\) and the quantifier over every compact subset matter here.

The bar in (7) is also present in Kashiwara–Schapira's Theorem 4.4.2, equation (4.4.1), p. 75. Its proof, p. 76, places the forgotten manifold inside a Euclidean ball and uses the boundary estimates for extension by zero and ordinary direct image. Compactness of the projected microsupport keeps the relevant base points away from the added boundary; consequently the boundary contribution and the comparison cone are invisible in the chosen region. It is this boundary exclusion, rather than properness of the original support, that supplies (9). The enlarged tensor estimate (5) is Theorem 5.2.2(i), with the limiting sum described in Corollary 1.2.4.

Under (7), the microlocal proper-image theorem gives, for both \(!\) and \(*\),

\[
\operatorname{SS}(Rq_{!}H)\cap\Omega,
\ \operatorname{SS}(Rq_{*}H)\cap\Omega
\ \subset
\{(m,\lambda):\exists y,\ (m,y;\lambda,0)\in\operatorname{SS}(H)\}.
\tag{9}
\]

It also says that the canonical arrow \(Rq_!H\to Rq_*H\) has cone microsupport disjoint from \(\Omega\). We use this theorem through the linked boundary-and-infinity prerequisite, including its boundary proof and operation assumptions. The verification below controls the tensor product at every middle component before imposing the horizontal condition needed to calculate its image.

## Why the enlarged sum becomes an ordinary sum

On \(X\times Y\times Z\), let \(q_{12},q_{23},q_{13}\) be the three pair projections. For kernels \(K\) on \(X\times Y\) and \(L\) on \(Y\times Z\), put

\[
H=q_{12}^{-1}K\otimes^Lq_{23}^{-1}L,
\qquad K\circ_YL=Rq_{13!}H.
\tag{10}
\]

Submersion inverse image has the exact microsupport formula. Accordingly define

\[
\begin{aligned}
A&=\{(x,y,z;\xi,\eta,0):(x,y;\xi,\eta)\in\operatorname{SS}(K)\},\\
B&=\{(x,y,z;0,\theta,\zeta):(y,z;\theta,\zeta)\in\operatorname{SS}(L)\}.
\end{aligned}
\tag{11}
\]

**Lemma 1.** If \(K\) is admissible, then on the region where \((x,\xi)\in\Omega_X\),

\[
A\widehat+ B=A+B.
\tag{12}
\]

The proof implements the bounded-summand step in Proposition 6.3.1, followed here by a closedness argument on the full triple product. Only the first kernel provides compactness; no admissibility of the second kernel is needed at this point.

**Proof.** Fix a point \((x_0,y_0,z_0;\xi_0,\nu_0,\zeta_0)\) of the left side, with \((x_0,\xi_0)\in\Omega_X\). In charts, its sequence (4) has summand covectors

\[
(\xi_n,\eta_n,0),\qquad(0,\theta_n,\zeta_n).
\]

Since their sum converges, \(\xi_n\to\xi_0\), \(\zeta_n\to\zeta_0\), and \(\eta_n+\theta_n\to\nu_0\). The output base points of the first sequence approach \(x_0\). Put its sufficiently late output covectors in a compact neighborhood \(D\subset\Omega_X\). By (3), the corresponding kernel covectors \((x_n,y_n;\xi_n,\eta_n)\) lie in a compact set. In particular \(\eta_n\) is bounded. Then \(\theta_n\) is bounded too.

Pass to a subsequence on which these two middle components converge, to \(\eta\) and \(\theta\). Both summand base sequences approach \((x_0,y_0,z_0)\). Closedness of the two microsupports gives

\[
(x_0,y_0;\xi_0,\eta)\in\operatorname{SS}(K),
\qquad
(y_0,z_0;\theta,\zeta_0)\in\operatorname{SS}(L),
\]

and \(\eta+\theta=\nu_0\). This is an ordinary sum in (11). Conversely an ordinary sum is represented by constant sequences in (4). The equality follows. The weighted distance condition creates no additional point here because compactness has excluded unbounded summand covectors. \(\square\)

Together with (5), this proves

\[
\operatorname{SS}(H)\cap(\Omega_X\times T^*Y\times T^*Z)
\subset(A+B)\cap(\Omega_X\times T^*Y\times T^*Z).
\tag{13}
\]

## The localized composition theorem

**Theorem 2.** Let \(K\) be admissible from \(\Omega_Y\) to \(\Omega_X\), and let \(L\in D^b(k_{Y\times Z})\) be arbitrary. Then the canonical arrow

\[
K\circ_YL\longrightarrow Rq_{13*}
(q_{12}^{-1}K\otimes^Lq_{23}^{-1}L)
\tag{14}
\]

is an isomorphism in \(\mathcal D_{X\times Z}(\Omega_X\times T^*Z)\). Moreover,

\[
\begin{split}
\operatorname{SS}(K\circ_YL)\cap(\Omega_X\times T^*Z)
\subset\{(x,z;\xi,-\beta):\exists(y,\alpha)\in\Omega_Y,\\
((x,\xi),(y,\alpha))\in\mathcal C_K,
\quad(y,z;\alpha,-\beta)\in\operatorname{SS}(L)\}.
\end{split}
\tag{15}
\]

If \(L\) is also admissible from \(\Omega_Z\) to \(\Omega_Y\), then \(K\circ_YL\) is admissible from \(\Omega_Z\) to \(\Omega_X\), and

\[
\mathcal C_{K\circ_YL}\subset\mathcal C_K\circ\mathcal C_L.
\tag{16}
\]

**Proof.** We first verify (8) for \(H\) and \(q_{13}\), treating \(M=X\times Z\). Fix any compact \(C\subset\Omega_X\times T^*Z\). Its projection \(D\) to \(T^*X\) is compact and contained in \(\Omega_X\). The preimage of \(D\) in \(\mathcal C_K\) is compact; project it to \(Y\), obtaining a compact \(B_C\).

Take any covector of \(\operatorname{SS}(H)\) whose \((X,Z)\) covector lies in \(C\). Its middle component \(\nu\) is unrestricted. By (13) it has an ordinary-sum witness from \(K\) and \(L\). The first witness has output in \(D\), so its base point \(y\), which is also the base point of our covector of \(H\), lies in \(B_C\). This proves (8) for all middle components, hence (7), including its closure.

Apply (9) to \(q_{13}\). It proves (14) for the canonical comparison. For the microsupport estimate its contributing covector of \(H\) must have \(\nu=0\). Its witness in (11) then satisfies \(\theta=-\eta\). Put \(\alpha=-\eta\). The two witness conditions become those in (15); the first also forces \((y,\alpha)\in\Omega_Y\). This proves (15).

Now suppose \(L\) is admissible. Its condition (3) forces every \((z,\beta)\) in (15) to belong to \(\Omega_Z\), which proves the required input-region containment. To prove properness, again take compact \(D\subset\Omega_X\). Let \(U\) be its compact preimage in \(\mathcal C_K\), and let \(E\subset\Omega_Y\) be the projection of \(U\) to its input. The preimage \(V\) of \(E\) in \(\mathcal C_L\) is compact. Matching the middle covector defines a closed subset of \(U\times V\). Its image after forgetting that middle covector is compact, and contains the whole relation in (16) above \(D\).

The actual relation of \(K\circ_YL\) above \(D\) is closed in this compact image: it is the intersection with the twisted microsupport of the convolution, a closed subset of the ambient cotangent product. Thus it is compact. This proves properness and admissibility. \(\square\)

Unlike the global proper-support estimate, this proof imposed no global condition on \(\operatorname{supp}(K)\cap\operatorname{supp}(L)\) and no global noncancellation hypothesis. The compactness is at the selected output covectors.

## Passing to quotient categories

**Theorem 3.** Convolution defines an exact bifunctor

\[
\mathcal K(\Omega_X,\Omega_Y)\times
\mathcal D_{Y\times Z}(\Omega_Y\times T^*Z)
\longrightarrow\mathcal D_{X\times Z}(\Omega_X\times T^*Z).
\tag{17}
\]

It restricts to admissible kernels when its second argument is admissible. For \(Z=\{\mathrm{pt}\}\), a kernel gives an exact functor

\[
\Phi_K:\mathcal D_Y(\Omega_Y)\longrightarrow\mathcal D_X(\Omega_X),
\qquad \Phi_K(G)=Rq_{1!}(K\otimes^Lq_2^{-1}G).
\tag{18}
\]

**Proof.** Fix an admissible \(K\). If a bounded kernel \(T\) on \(Y\times Z\) has microsupport disjoint from \(\Omega_Y\times T^*Z\), then the right side of (15), with \(T\) in place of \(L\), is empty. Hence \(K\circ_YT\) is zero in the output quotient. Exactness of convolution says that the cone of a convolved arrow is the convolution of its cone. Every denominator in the second argument therefore becomes invertible.

For the first argument, a cone \(S\) with microsupport disjoint from \(\Omega_X\times T^*Y\) is itself admissible: its relation in (2) is empty. Applying (15) to \(S\) and any \(L\) gives an empty output relation. Thus denominators in the first argument also become invertible. Representatives in a fraction for an admissible object are admissible because their restricted microsupports agree. The universal property of the two quotients now supplies (17), with its ordinary natural transformations. The final assertion of Theorem 2 gives its restriction to admissible kernels. Taking \(Z\) to be a point gives (18). \(\square\)

In particular,

\[
\operatorname{SS}(\Phi_KG)\cap\Omega_X
\subset\{u\in\Omega_X:\exists v\in\operatorname{SS}(G)\cap\Omega_Y,
\ (u,v)\in\mathcal C_K\}.
\tag{19}
\]

The existence of an intermediate covector is necessary for an output singularity. It does not force that singularity to occur: sheaf cohomology can still vanish.

## Composition and inverse kernels

The ordinary convolution calculus has a natural associative comparison. One way to see its provenance is to put three kernels on \(X\times Y\times Z\times W\). Both parenthesizations are identified with the proper-support direct image of

\[
q_{12}^{-1}K\otimes^Lq_{23}^{-1}L\otimes^Lq_{34}^{-1}M
\]

to \(X\times W\), using proper base change, the projection formula and composition for \(!\). The tensor associator, including its cochain signs, gives the natural comparison. These are the ordinary identities imported from the kernel-calculus prerequisite.

For admissible kernels Theorem 2 makes both parenthesizations admissible. Theorem 3 makes the comparison independent of the chosen representatives. Consequently

\[
(K\circ_YL)\circ_ZM\simeq K\circ_Y(L\circ_ZM),
\qquad
\Phi_{K\circ_YL}\simeq\Phi_K\Phi_L.
\tag{20}
\]

The second identity takes the final kernel to be an object on \(Z\times\{\mathrm{pt}\}\). This proves it on the full localized categories, rather than merely on ordinary sheaf representatives.

The diagonal kernel \(k_{\Delta_X}\) is admissible from \(\Omega_X\) to itself. Its twisted relation is the diagonal of \(\Omega_X\times\Omega_X\), so projection to the output is a homeomorphism. Its transform is the identity by the ordinary diagonal formula.

**Theorem 4.** Suppose \(K\) and \(L\) are admissible in the two opposite directions and there are localized kernel isomorphisms

\[
K\circ_YL\simeq k_{\Delta_X}
\quad\text{on }\Omega_X\times T^*X,
\qquad
L\circ_XK\simeq k_{\Delta_Y}
\quad\text{on }\Omega_Y\times T^*Y.
\tag{21}
\]

Then \(\Phi_K\) and \(\Phi_L\) are inverse equivalences of the two localized sheaf categories.

**Proof.** A localized isomorphism in (21) induces an isomorphism of transforms by (17)–(18). Equation (20) therefore gives natural isomorphisms \(\Phi_K\Phi_L\simeq\mathrm{id}\) and \(\Phi_L\Phi_K\simeq\mathrm{id}\). These exhibit quasi-inverse functors. Both composites in (21) are needed; one composite alone gives only one of these natural isomorphisms. \(\square\)

This criterion requires sheaf-level kernel isomorphisms. Equality of their cotangent relations, even when both relations are diagonals, does not establish those isomorphisms.

## Exercises with solutions

### A nonproper component that disappears in the quotient

*Difficulty: Advanced.*

Take \(X=Y=\mathbb R\), \(k\ne0\), \(\Omega_X=\Omega_Y=\{(t,\tau):\tau>0\}\), and
\(K=k_\Delta\oplus k_{\mathbb R^2}\). Prove admissibility although the support projection is nonproper. Calculate its proper-support and ordinary transforms on \(k_\mathbb R\) and on \(k_{\{0\}}\). Compare with the identity kernel in the quotient.

**Solution.** The whole-plane constant summand has only zero covectors, so contributes nothing to (2). The diagonal summand gives \(\mathcal C_K=\{(u,u):u\in\Omega_X\}\), proper over its output. But the support of the other summand is all of \(\mathbb R^2\), whose projection has noncompact fibres.

On \(k_\mathbb R\), the diagonal gives \(k_\mathbb R\); the other summand gives \(k_\mathbb R[-1]\) for \(!\) and \(k_\mathbb R\) for \(*\), using compact-support and ordinary cohomology of a line. Thus the two answers are \(k_\mathbb R\oplus k_\mathbb R[-1]\) and \(k_\mathbb R\oplus k_\mathbb R\). They need not be globally isomorphic. All their microsupport lies on the zero section, so both are zero in the chosen quotient.

On \(k_{\{0\}}\), the extra summand is supported on \(\mathbb R\times\{0\}\), and both projections give \(k_\mathbb R\). Hence both transforms give \(k_{\{0\}}\oplus k_\mathbb R\). The constant summand disappears in the quotient, whereas the skyscraper's positive covectors remain. Projection \(K\to k_\Delta\) itself has a shifted constant kernel as cone, invisible on the selected output region. It therefore gives a natural localized identification of the whole transform with the identity. This is a nontrivial operator even though it contains a nonproper invisible component.

### Controlling points is weaker than controlling covectors

*Difficulty: Intermediate.*

Take \(K=k_{\{(0,0)\}}\) on \(\mathbb R_x\times\mathbb R_y\), with \(k\ne0\), \(\Omega_X=\{\xi>0\}\) and \(\Omega_Y=T^*\mathbb R\). Does confinement of the middle point imply (3)?

**Solution.** Its microsupport is the full cotangent fibre at \((0,0)\). For the compact singleton output \((0,1)\), the relation has every input \((0,\alpha)\), \(\alpha\in\mathbb R\). Every intermediate point is the single point zero, but the input covectors are unbounded. The preimage is noncompact, so (3) fails. The input-region containment holds because \(\Omega_Y\) is the entire cotangent bundle. This example isolates the failed properness hypothesis; it is not a claim that every conclusion of Theorem 2 fails for this kernel.

### A reflection chooses the opposite input region

*Difficulty: Intermediate.*

Let \(f(t)=-t\) and \(K=k_{\Gamma_f}\), with \(k\ne0\). Choose \(\Omega_X=\{\xi>0\}\). Find the input region making the graph kernel admissible, and test its action on the open and closed positive half-line sheaves.

**Solution.** The twisted graph relation is \((x,\xi)=(-y,-\alpha)\). Thus \(\Omega_Y=\{\alpha<0\}\) works; projection to \(\Omega_X\) is a homeomorphism. Choosing instead \(\{\alpha>0\}\) violates input-region containment. Reflection sends \(k_{(0,\infty)}\) to \(k_{(-\infty,0)}\). The first has negative nonzero boundary covectors and the second positive ones, so the chosen localized action retains this boundary. It sends \(k_{[0,\infty)}\) to \(k_{(-\infty,0]}\); their nonzero boundary covectors are respectively positive and negative. Both of these closed-half-line objects are invisible in their respective chosen regions. A diffeomorphism adds no cohomological shift.

### A zero input covector at a critical point

*Difficulty: Advanced.*

Let \(f(y)=2y\), \(g(z)=z^3\), and take their graph kernels, with \(k\ne0\). Choose positive output covectors in both \(T^*X\) and \(T^*Y\). Can the input region for \(g\) also consist only of positive covectors? Compute the composite relation and a valid input region.

**Solution.** For \(f\), the relation has \(x=2y\) and \(\alpha=2\xi\), so it is admissible between the positive regions. For \(g\), it has \(y=z^3\) and \(\beta=3z^2\alpha\). At \(z=0\), a positive \(\alpha\) gives \(\beta=0\), which is outside the strictly positive region. Thus that choice fails input-region containment. The whole \(T^*Z\) is a valid input region: compact output covectors confine \(y\) and \(\alpha\), then \(z=\sqrt[3]{y}\) and \(\beta\) are confined too; closedness gives compact preimages. The composite graph is \(x=2z^3\) and \(\beta=6z^2\xi\), as either graph composition or the chain rule gives. The zero input at the critical point is allowed. Admissibility does not assert that the graph is a contact diffeomorphism.

### Why both diagonal composites matter

*Difficulty: Advanced.*

In Theorem 4, suppose only the first isomorphism in (21) is known. What can be concluded categorically? Give an elementary pair of exact functors showing that a one-sided identity does not imply an equivalence.

**Solution.** It gives \(\Phi_K\Phi_L\simeq\mathrm{id}\) on the output category. Thus \(\Phi_K\) is essentially surjective and \(\Phi_L\) is faithful, but this alone does not make them quasi-inverse. For a concrete exact example use \(D^b(k)\) and \(D^b(k)\times D^b(k)\), with \(k\ne0\). Projection \(P(A,B)=A\) and inclusion \(I(A)=(A,0)\) satisfy \(PI=\mathrm{id}\). The other composite sends \((A,B)\) to \((A,0)\), and is not isomorphic to the identity when \(B\ne0\). These are categorical functors, not proposed sheaf kernels. They identify exactly the missing step in a purported equivalence proof.

## References

- Masaki Kashiwara and Pierre Schapira, [*Microlocal Study of Sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985): Corollary 1.2.4, p. 18, for the limiting sum; Theorem 4.4.2 and proof, pp. 75–76, for the microlocal proper-image comparison; Theorem 5.2.2(i), p. 82, for the enlarged tensor estimate; §6.1, pp. 103–104, for the microsupport quotient and its universal property; Proposition 6.3.1, Remark 6.3.2 and Proposition 6.3.3 with proof, pp. 108–111, for compactness and localized composition.
- Pierre Schapira, [*A short review on microlocal sheaf theory*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), 19 January 2016, §§2.2–2.4, pp. 6–14. The ring convention agrees with the one here. Its kernel estimate uses ordinary support properness and a global noncharacteristic condition; it is a useful comparison with, rather than a proof of, the present localized result.

**What is proved here.** Theorem 2 follows the human source's compactness mechanism but supplies the full triple-product argument: bound the two middle summands, confine every possible middle base point, apply the image estimate, and finally enforce cancellation. The second admissibility condition is used only afterward, to prove properness of the composed relation as a closed subset of the compact matching space. Theorem 3 checks denominators in both variables, and Theorem 4 uses two specified diagonal kernel isomorphisms. It does not infer an equivalence from a cotangent relation alone. In particular, it does not import the stronger contact-equivalence criterion of the source's Theorem 6.3.4, which also requires a cohomologically constructible kernel and a microlocal endomorphism condition.

**Scope of the dependence.** The general-open-region and bounded-complex formulation, the explicit compactness verification, and all five exercises are independently expressed programme arguments built on the linked operation, limiting-sum, boundary and localization prerequisites. The source's finite weak global dimension convention is sufficient for its tensor statements; the present finite global dimension and manifold bounds also control the bounded categories used here. The source proof of Theorem 4.4.2 itself uses boundary estimates, and the six-operation associativity remains a prerequisite. These dependencies are retained, not counted as discharged by the source comparison.
