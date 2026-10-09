# Continuous sections and supported cycle intersections

A section of a cotangent bundle has a canonical supported class even when the section is only continuous. Intersecting that class with a Lagrangian cycle gives a dualizing class on their actual intersection. A proper trace carries it to the base. The resulting class agrees with an ordinary descent of the cycle, with both output supports retained.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

Use [Intersections of supported subanalytic cycles](intersections-of-supported-subanalytic-cycles.md) for the evaluated supported cup, compact integration and excess intersections. [Lagrangian cycles and proper cotangent images](lagrangian-cycles-and-proper-cotangent-images.md) and [Pulling back Lagrangian cycles through a graph](pulling-back-lagrangian-cycles-through-a-graph.md) supply the cycle coefficient and normalized point, zero-section and closed conormal cycles. The sheaf operations used below are the [trace-preserving exceptional composition](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-composition--composition-restriction-and-change-of-base), [closed-support adjunction](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-embedding--open-closed-and-locally-closed-inclusions), [internal adjunction](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-internal--internal-adjunction-and-its-tensor-structure), and [normalized tensor comparison](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-tensor--the-normalized-tensor-comparison). The relative dualizing formula, compact-coordinate generator, and submersion trace fix their coefficients and normalization. We prove the required ordinary bundle-unit identity explicitly below; the general version is descent along acyclic submersions.

M. Kashiwara's [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §§1.5–2.3, pp. 196–197, supplies the coefficient-chain and conormal framework. The supported comparison below is proved from the ordinary section unit, exceptional tensor map and trace; it applies to continuous sections without an analytic graph hypothesis. The normalized transverse conormal formula is proved in [Transverse pullback of normalized conormal cycles](transverse-pullback-of-normalized-conormal-cycles.md).

## A continuous section supplies a supported unit

Let \(A\) be a commutative ring of finite global dimension and \(X\) a real analytic \(n\)-manifold, Hausdorff and countable at infinity, of uniformly bounded dimension. Put

\[
 M=T^*X,\qquad \pi:M\to X,\qquad
 P=\pi^!A_X,\qquad E=\pi^{-1}\omega_X.
 \qquad\text{(1)}
\]

These operations apply to the continuous maps used here. The bundle projection is a topological submersion with \(n\)-dimensional fibres; its proper direct image has cohomological dimension at most \(n\), by the submersion proof. A closed embedding has exact proper direct image and bound zero. The finite-dimensional, locally compact hypotheses therefore give the exceptional adjoints and their composition comparisons for both maps. No analytic regularity of the section is required.
Let \(\sigma:X\to M\) be a continuous section, so \(\pi\sigma=\operatorname{id}_X\), and write \(G=\sigma(X)\). This is a closed subset: in a bundle chart its fibre coordinate is the graph of a continuous function into a Hausdorff vector space. The map \(\sigma\) is a homeomorphism onto that closed graph and hence a proper closed embedding.

For a closed subset \(S\), our convention is

\(H^0_S(M;F)=H^0R\Gamma(M;R\mathcal Hom(A_S,F))=\operatorname{Hom}_{D(A_M)}(A_S,F)\).

The last equality uses global derived Hom. It does not assert that taking sections commutes with tensor products. Since \(A_G=\sigma_*A_X\), closed-support adjunction and exceptional composition give the actual identifications

\[
 H^0_G(M;P)
     \simeq H^0(X;\sigma^!\pi^!A_X)
     \simeq H^0(X;A_X).
 \qquad\text{(2)}
\]

The second is the composition comparison for \(\pi\sigma=\operatorname{id}\). Define \([\sigma]\) to be the class corresponding to \(1\). As a derived sheaf morphism it is

\[
 A_G=\sigma_*A_X
   \longrightarrow \sigma_*\sigma^!P
   \xrightarrow{\varepsilon_\sigma}P,
 \qquad\text{(3)}
\]

where the first map uses the inverse of \(\sigma^!P\simeq A_X\). Thus the section class has a specified counit normalization. Smoothness, analyticity and isotropy of the graph are unnecessary. In particular (2) does not assert that an arbitrary section class belongs to the sheaf of Lagrangian cycles.

The dualizing coefficient of \([\sigma]\) is \(P\). The relative formula gives

\[
 P\simeq\omega_M\otimes\pi^{-1}\operatorname{or}_X[-n].
 \qquad\text{(4)}
\]

This is the ordered exceptional comparison, including the integral orientation square and shifted evaluation. If an orientation \(\varepsilon:\operatorname{or}_M\simeq A_M\) is chosen, (4) gives an identification
\(\theta_\varepsilon:P\simeq E\), since \(\omega_M\) has shift \([2n]\) and the remaining factor has shift \([-n]\). That orientation choice is part of this rewritten description. Formula (3) itself needs no such choice.

## The cup retains the actual intersection

For closed \(S_1,S_2\subset M\), put \(K=S_1\cap S_2\). Write \(A_S\) for the constant sheaf on a closed subset extended by its closed inclusion. The support operation is \(R\mathcal Hom(A_S,-)\); on stalks \(A_S\) is \(A\) or zero, and
\(A_{S_1}\otimes A_{S_2}\simeq A_K\).

Tensor the two support evaluations in their given order, then use the exceptional tensor comparison

\[
 q:P\otimes^L E
       =\pi^!A_X\otimes^L\pi^{-1}\omega_X
          \longrightarrow\pi^!\omega_X\simeq\omega_M.
 \qquad\text{(5)}
\]

The result is the supported cup

\[
 H^0_{S_1}(M;P)\otimes_A H^0_{S_2}(M;E)
             \longrightarrow H^0_K(M;\omega_M),
 \qquad \gamma\otimes\lambda\longmapsto\gamma\cap\lambda.
 \qquad\text{(6)}
\]

For classes represented by \(u:A_{S_1}\to P\) and \(v:A_{S_2}\to E\), its morphism is
\(A_K\simeq A_{S_1}\otimes A_{S_2}\xrightarrow{u\otimes v}P\otimes^LE\xrightarrow q\omega_M\).
This specifies all evaluation and support maps, including the factor order. Both inputs have supported degree zero, so their product has degree zero. A positive-dimensional intersection still gives the class (6); it need not be a literal zero-dimensional chain.

If \(K\) is compact, the number is the composite

\[
 H^0_K(M;\omega_M)\longrightarrow H_c^0(M;\omega_M)
                    \xrightarrow{\operatorname{tr}_{a_M}}A,
 \qquad \#(\gamma\cap\lambda)=\int_M\gamma\cap\lambda.
 \qquad\text{(7)}
\]

Compactness is required for this supported-to-compact map. Neither input carrier has to be compact.
If \(p\) is isolated in \(K\), choose an open \(U\ni p\) with \(U\cap K=\{p\}\). The restricted product has compact point support and defines \(\#(\gamma\cap\lambda)_p\) by the trace on \(U\).

**Independence of the neighborhood.** For smaller \(V\subset U\) containing \(p\), open restriction of the dualizing object gives the same supported point class. Open extension followed by the trace on \(U\) is the trace on \(V\), by exceptional composition. Thus both numbers agree. Two admissible neighborhoods have an admissible common smaller neighborhood. This proves independence, while an intersection component of positive dimension is not assigned an isolated-point number by this construction.

## Proper trace and ordinary descent have different domains

First let \(S\subset M\) be closed and \(\pi\) proper on \(S\). Its image \(D_S=\pi S\) is closed. For a class \(c:A_S\to\omega_M\), define

\[
 \begin{aligned}
 \alpha_S(c):A_{D_S}
 &\longrightarrow R\pi_*A_S
   \simeq R\pi_!A_S\\
 &\xrightarrow{R\pi_!c}R\pi_!\omega_M
   \xrightarrow{\varepsilon_\pi}\omega_X.
 \end{aligned}
 \qquad\text{(8)}
\]

The first arrow is the ordinary adjoint of the closed-constant restriction
\(\pi^{-1}A_{D_S}\to A_S\). Properness on \(S\) supplies the middle comparison for this supported object. Hence (8) is the actual map
\(H^0_S(M;\omega_M)\to H^0_{D_S}(X;\omega_X)\).
It retains the closed output support. The trace exists for \(\pi\) itself, but properness on \(S\) is what permits this transport of the input class.

Now let \(\Lambda\subset M\) be closed and positively conic, and put \(D=\pi\Lambda\). Then

\[
 D=\{x\in X:0_x\in\Lambda\},
 \qquad\text{(9)}
\]

so \(D\) is closed. Indeed positive scaling of any covector of \(\Lambda\) over \(x\) converges to \(0_x\), and closedness retains the limit. The reverse inclusion in (9) is immediate. No properness of \(\pi|_\Lambda\) is asserted.

The ordinary adjunction unit

\[
 \eta_H:H\longrightarrow R\pi_*\pi^{-1}H
 \qquad\text{(10)}
\]

is an isomorphism for every bounded coefficient complex \(H\) on \(X\). To prove this for the specified arrow, recall \(P=\omega_\pi=\pi^!A_X\) and put \(C=R\pi_!P\). On a fibre the relative coefficient is \(\omega_{\mathbb R^n}\). Its compact trace is \(R\Gamma_c(\mathbb R^n;\omega_{\mathbb R^n})\to A\): the ordered interval generator and its orientation dual identify this map with \(+1\). Proper-support base change and the submersion comparison identify each stalk of \(\operatorname{tr}_\pi:C\to A_X\) with that fibre trace. Thus this trace is an isomorphism, including over nonorientable \(X\); no global orientation has been chosen.

The submersion tensor map \(q_H:P\otimes^L\pi^{-1}H\to\pi^!H\) is an isomorphism. The shifted orientation line \(P\) is invertible, so currying \(q_H\) identifies \(\pi^{-1}H\) with \(R\mathcal Hom(P,\pi^!H)\). Internal adjunction then gives

\[
 R\pi_*\pi^{-1}H
 \simeq R\mathcal Hom(R\pi_!\omega_\pi,H)
 \simeq H.
 \qquad\text{(11)}
\]

It remains to identify the image of the actual unit \(\eta_H\) in \(R\mathcal Hom(C,H)\). Uncurry it with the factor \(C\) first. The evaluated internal adjunction sends it to

\(C\otimes^LH\simeq R\pi_!(P\otimes^L\pi^{-1}H)\xrightarrow{R\pi_!q_H}R\pi_!\pi^!H\xrightarrow{\varepsilon_\pi}H\).

Indeed the ordinary counit in that evaluation cancels the pulled-back ordinary unit by the adjunction triangle identity. By the defining transpose of the exceptional tensor map, this displayed composite is \(\operatorname{tr}_\pi\otimes1_H:C\otimes^LH\to H\). Thus under (11), \(\eta_H\) corresponds to precomposition with \(\operatorname{tr}_\pi\). Since that trace is invertible, the map is the identity after identifying \(C\) with \(A_X\). This proves that (10), rather than an unspecified isomorphism between its endpoints, is invertible. Only proper-support fibre base change has been used.

For \(\lambda:A_\Lambda\to E\), ordinary descent is

\[
 \beta_\pi(\lambda):A_D
  \longrightarrow R\pi_*A_\Lambda
  \xrightarrow{R\pi_*\lambda}R\pi_*E
  \xrightarrow{\eta_{\omega_X}^{-1}}\omega_X.
 \qquad\text{(12)}
\]

Again the first arrow is the adjoint of closed-constant restriction
\(\pi^{-1}A_D\to A_\Lambda\). Thus (12) lies in \(H^0_D(X;\omega_X)\). It uses the ordinary inverse unit, while (8) uses the proper trace. We write \(\beta_\pi\) to distinguish this descent from the cotangent coefficient adjoint \(\beta_f\) in the preceding lesson.

## The complete supported section-intersection comparison

Let \(\lambda\) be a Lagrangian cycle supported on a closed conic subanalytic isotropic \(\Lambda\). Define

\[
 J=\sigma^{-1}\Lambda,\qquad K=G\cap\Lambda,\qquad D=\pi\Lambda.
 \qquad\text{(13)}
\]

The sets \(J,K,D\) are closed. Projection identifies \(K\) homeomorphically with \(J\), so \(\pi\) is proper on \(K\), even when \(J\) is noncompact. The theorem is

\[
 \iota_{J,D}\,\alpha_K([\sigma]\cap\lambda)
             =\beta_\pi(\lambda)
       \quad\text{in }H^0_D(X;\omega_X),
 \qquad\text{(14)}
\]

where \(\iota_{J,D}\) enlarges the closed support from \(J\) to \(D\). In terms of morphisms, that map precomposes \(A_J\to\omega_X\) with the restriction \(A_D\to A_J\).

We compare two explicit representatives of the class. Ordinary restriction to the graph calculates the descent map. Transposing the supported cup along the graph and composing its trace calculates proper transport. Both calculations retain the map from the closed output support.

**The ordinary right cell.** The embedding unit \(u_\sigma:E\to\sigma_*\sigma^{-1}E\) gives

\[
 t_\sigma:R\pi_*E
     \xrightarrow{R\pi_*u_\sigma}
        R\pi_*\sigma_*\sigma^{-1}E
     \simeq\omega_X.
 \qquad\text{(15)}
\]

Since \(\pi\sigma=\operatorname{id}\), composition of ordinary units gives
\(t_\sigma\eta_{\omega_X}=1_{\omega_X}\).
The unit in (10) is invertible, so
\(t_\sigma=\eta_{\omega_X}^{-1}\) as actual morphisms.

Apply naturality of \(u_\sigma\) to \(\lambda:A_\Lambda\to E\). Pullback of the closed constant is
\(\sigma^{-1}A_\Lambda=A_J\), while \(\sigma^{-1}E=\omega_X\). Its support map gives the full commuting route

\[
 \begin{array}{ccccc}
 A_D&\longrightarrow&R\pi_*A_\Lambda
       &\xrightarrow{R\pi_*\lambda}&R\pi_*E\\
 \downarrow&&\downarrow&&\downarrow t_\sigma\\
 A_J&\xrightarrow{1}&A_J
       &\xrightarrow{\sigma^{-1}\lambda}&\omega_X.
 \end{array}
 \qquad\text{(16)}
\]

The middle vertical arrow applies the same ordinary section unit to \(A_\Lambda\), then uses \(\pi\sigma=\operatorname{id}\). The left arrow is closed-constant restriction. The left square commutes because both maps are the adjoint restriction of \(\pi^{-1}A_D\) along \(\Lambda\), followed by restriction to \(\sigma\). The right square is unit naturality. Together with (15), this identifies (12) with

\[
 A_D\longrightarrow A_J
             \xrightarrow{\sigma^{-1}\lambda}\omega_X.
 \qquad\text{(17)}
\]

This identification already includes the output support; it is stronger than equality after passage to unrestricted cohomology.

**The cup and the exceptional left cell.** In (3), \([\sigma]\) is the \(\sigma_*\dashv\sigma^!\) counit applied to the unit \(1:A_X\to\sigma^!P\). Tensor it with \(\lambda\) in the order \(P,E\), then use (5). The closed-support projection comparison is

\[
 \sigma_*A_X\otimes^L A_\Lambda
       \simeq\sigma_*(A_X\otimes^L\sigma^{-1}A_\Lambda)
       =\sigma_*A_J=A_K.
 \qquad\text{(18)}
\]

The projection isomorphism in (18) followed by the closed embedding counit is the transpose that defines the exceptional tensor map. Applying its naturality to \(\lambda\) therefore makes the \(\sigma\)-adjoint of the cup equal to the following composite. The tensor map is invertible here as well: locally \(E\) is the tensor unit with a shift, and the normalized comparison for that unit is the identity; these local isomorphisms glue. Thus neither a flatness assumption on \(\lambda\) nor a differentiability assumption on \(\sigma\) is being inserted:

\[
 \begin{aligned}
 A_J&\simeq A_X\otimes A_J
   \longrightarrow\sigma^!P\otimes\sigma^{-1}E\\
   &\longrightarrow\sigma^!(P\otimes^LE)
   \xrightarrow{\sigma^!q}\sigma^!\pi^!\omega_X
   \simeq\omega_X.
 \end{aligned}
 \qquad\text{(19)}
\]

The first map is the unit \(1\) of the section class tensored with \(\sigma^{-1}\lambda\). Here is why the remaining coefficient comparison has the required normalization. Transpose successively along \(\sigma\) and \(\pi\). The definition of each tensor map replaces it by the corresponding projection formula followed by its exceptional counit, tensored with the last factor. Projection and composition associativity identify the result with \(\varepsilon_\pi R\pi_!(\varepsilon_\sigma)\otimes1_{\omega_X}\). The composition identification is defined by this very composite counit; for \(\pi\sigma=\operatorname{id}\) it is the identity. Adjunction is bijective on morphisms, so equality of these transposes proves equality of the original coefficient maps.

Consequently the identifications \(\sigma^!\pi^!A_X=A_X\) and \(\sigma^!\pi^!\omega_X=\omega_X\) turn that coefficient comparison into the tensor map for the identity functor. Its unit compatibility makes (19) exactly \(\sigma^{-1}\lambda\). Throughout, the order is the section coefficient followed by the cycle coefficient; no factor exchange and no extra sign has occurred.

Let \(c=[\sigma]\cap\lambda:A_K=\sigma_*A_J\to\omega_M\). Transpose (19) back, then apply \(R\pi_!\) and the \(\pi\)-trace. Composition of exceptional counits gives

\[
 \varepsilon_\pi\,R\pi_!(\varepsilon_\sigma)
        =\varepsilon_{\pi\sigma}=1.
 \qquad\text{(20)}
\]

Moreover \(R\pi_!A_K=A_J\), with its canonical graph identification. Thus (8) applied to \(c\) is the morphism \(A_J\xrightarrow{\sigma^{-1}\lambda}\omega_X\). This proves the exceptional lower cell and the cup-to-section cell with their actual tensor and counit maps. Precomposing with \(A_D\to A_J\) gives (17), proving (14).

This argument in fact works for every class \(\lambda\in H^0_\Lambda(M;E)\) on a closed carrier whose image \(D\) is closed. Conicity supplies that closed-image property in the stated theorem; the Lagrangian hypotheses supply its cycle class. The equality retains the intermediate support \(J\), the ordinary unit, and the chosen exceptional counits, so it also covers excess intersections and a nondifferentiable section.

If \(K\) is compact, its proper trace produces a class with compact support \(J\). The equality after support enlargement still holds on \(D\), which may be noncompact. The number is obtained by integrating that compactly supported class on \(J\); composition of traces makes it equal to (7). An unrestricted class merely supported on a noncompact \(D\) is not automatically given an integral.

## Exercises with complete solutions

### A corner in a continuous graph still has a class

*Difficulty: Intermediate.*

For \(X=\mathbb R\), take \(\sigma(x)=(x;|x|\,dx)\). Construct its supported class and explain why no differentiability at zero is required. Does this construction make its graph an allowed Lagrangian cycle carrier?

**Solution.** The fibre coordinate is continuous, so the graph is closed and the projection from it to \(\mathbb R\) is a homeomorphism. The section is a proper closed embedding, and \(\sigma^!\pi^!A=A\). Formula (3) sends \(1\) through this identification and the closed embedding counit, producing \([\sigma]\in H^0_G(M;P)\). No tangent or derivative of the graph enters this construction.

This graph is not conic: a point with \(x\ne0\) has fibre value \(|x|\), and multiplying that fibre value by two leaves the graph. Its regular graph arcs are symplectically isotropic, because every two-form restricts to zero on a one-dimensional manifold. The canonical one-form restricts to \(|x|\,dx\), which is nonzero away from zero. This does not contradict symplectic isotropy: equivalence with vanishing of the canonical one-form uses the conic hypothesis, as proved in [isotropic cotangent transport](../../sheaf-proof-readings/src/SH03/isotropic-cotangent-transport-and-discrete-critical-values.md#singular-form-calculus). Nonconicity excludes this graph from the closed conic isotropic carriers defining \(\mathcal L_X\). Its supported section class still exists, and intersections in (6) permit this first input.

### Every section meets a full point conormal with number one

*Difficulty: Advanced.*

Let \(i:\{x\}\hookrightarrow X\) and \(\lambda=[T^*_{\{x\}}X]=i_*[\mathrm{pt}]\), normalized by the preceding lesson. Compute \(\beta_\pi(\lambda)\) and \(\#([\sigma]\cap\lambda)\) for any continuous section. Explain why proper trace on the entire conormal carrier is unavailable when \(n>0\).

**Solution.** Write \(V=T_x^*X\). Its cycle class is the actual Cartesian base change of the closed point trace
\(\tau_i:i_*A\to\omega_X\). Indeed the direct-image coefficient construction gives
\[
 A_V\simeq\pi^{-1}i_*A
       \xrightarrow{\pi^{-1}\tau_i}E.
 \qquad\text{(21)}
\]
The point's supported pullback sends its unit to the unit on \(V\), so (21) represents this particular \(\lambda\).

In (12), the map \(i_*A\to R\pi_*A_V\) is the ordinary unit for \(i_*A\). Naturality of (10) with \(\tau_i\), followed by its inverse for \(\omega_X\), therefore gives
\(\beta_\pi(\lambda)=\tau_i\) as a supported morphism. The graph meets \(V\) at the single point \(\sigma(x)\); hence \(J=\{x\}\) and \(K=\{\sigma(x)\}\) are compact. The theorem identifies \(\alpha_K([\sigma]\cap\lambda)\) with \(\tau_i\). Exceptional composition for \(a_Xi:\{x\}\to\mathrm{pt}\) makes its integral the point trace of \(1\), namely
\[
 \#([\sigma]\cap[T_x^*X])=1\in A.
 \qquad\text{(22)}
\]
This proves the sign using the actual normalized point trace.

For \(n>0\), the whole \(V\simeq\mathbb R^n\) is noncompact and maps to a single base point, so \(\pi|_V\) is not proper. Thus \(\alpha_V\) is unavailable on that whole carrier. The ordinary map \(\beta_\pi\) remains defined, and the section intersection has its separate compact support \(K\).

### A noncompact intersection has no unrestricted scalar

*Difficulty: Intermediate.*

On \(X=\mathbb R\), let \(\lambda\) be the normalized zero-section cycle. Compare the section \(\sigma_0=0\) with \(\sigma_1=dx\). What follows about the supported base class, and what compactness condition changes?

**Solution.** For \(\sigma_1\), the graph has fibre value one and is disjoint from the zero section. Its cup with \(\lambda\) is zero. The theorem gives \(\beta_\pi(\lambda)=0\). For \(\sigma_0\), the intersection is the entire zero section, homeomorphic to \(\mathbb R\), so \(K\) and \(J\) are noncompact. Projection is still proper on \(K\), because it is a homeomorphism there. The supported trace and equality (14) are defined and yield the same zero base class.

There is no general scalar map (7) on this noncompact intersection support. The fact that this particular output class is zero does not create such a trace domain for arbitrary classes. Both inputs exist, proper transport on the section graph exists, and compact integration is a further requirement. In this example \(H^0(\mathbb R;\omega_{\mathbb R})=H^1(\mathbb R;A)=0\), consistently with the base-class calculation.

### Infinitely many local numbers need not have a total

*Difficulty: Advanced.*

In \(T^*\mathbb R\), let \(\lambda\) have normalized weight \(a_k\in A\) on the full fibre over each integer \(k\). Show that this defines a Lagrangian cycle, compute its intersection numbers with an arbitrary continuous section locally, and determine when a finite total is supplied by compact support.

**Solution.** The union of these fibres is closed and locally finite in the ambient cotangent bundle. Near any ambient point it is a finite subanalytic union; each fibre is conic and isotropic. Thus it is an allowed carrier. Its normalized one-cycle coefficients are independently constant on the disjoint full fibres and have no endpoint boundaries. Sheaf gluing over the locally finite family permits the weights \(a_k\), including unbounded integer weights when \(A=\mathbb Z\).

The section meets each fibre at \(\sigma(k)\). A sufficiently small base interval around \(k\) contains no other integer. The restriction of \(\lambda\) there is \(a_k\) times the normalized point conormal. Exercise 2 and the neighborhood independence of the local trace give
\[
 \#([\sigma]\cap\lambda)_{\sigma(k)}=a_k.
 \qquad\text{(23)}
\]
No sum over other integers is involved in that local number.

If infinitely many weights are nonzero, their base support is an infinite subset of the integers and is noncompact. The intersection's actual support is therefore noncompact as well. The ring \(A\) carries no prescribed infinite summation operation, so these local numbers have no total supplied by (7). If only finitely many weights are nonzero, choose their finite union of full fibres as the carrier. The section intersection then has finite compact support, and the compact trace is the sum of those weights. The input fibres themselves remain noncompact.

### A nonvanishing one-form kills the circle's zero-section class after descent

*Difficulty: Intermediate.*

Let \(X=S^1\), \(\lambda=[T_X^*X]\), and let \(\sigma\) be a nonvanishing continuous one-form. Prove that \(\beta_\pi(\lambda)=0\) as a supported base class. Does the compactness of the base make the whole cotangent carrier proper over it?

**Solution.** The tangent bundle of the circle is trivial: the angular tangent vector has a global nonzero dual one-form. For example the restriction of \(x\,dy-y\,dx\) to the unit circle is everywhere nonzero. Its graph is disjoint from the zero section. Hence \([\sigma]\cap\lambda=0\), and (14) gives \(\beta_\pi(\lambda)=0\) in \(H^0(S^1;\omega_{S^1})\), with the entire base support retained. This uses the supported comparison and does not require a characteristic-cycle index theorem.

The full cotangent bundle has noncompact line fibres, so its projection is not proper even over the compact base. Properness on the zero section or on a section-intersection support is a different statement. Those restrictions are homeomorphisms onto their closed base subsets and are proper.

### Reversing an auxiliary orientation leaves the intrinsic intersection unchanged

*Difficulty: Intermediate.*

Choose an orientation \(\varepsilon\) of \(M\) and rewrite \([\sigma]\) as an \(E\)-class using \(\theta_\varepsilon:P\to E\). Determine what changes if the orientation is reversed. Track the coefficient map as well as the section class, including in characteristic two.

**Solution.** Reversing the orientation replaces \(\theta_\varepsilon\) by \(-\theta_\varepsilon\). Thus the rewritten section class changes sign. The rewritten cup coefficient map is
\[
 q_\varepsilon=q\circ(\theta_\varepsilon^{-1}\otimes1):
                         E\otimes^LE\longrightarrow\omega_M.
 \qquad\text{(24)}
\]
It too changes sign, because the inverse of \(-\theta_\varepsilon\) is \(-\theta_\varepsilon^{-1}\). Consequently its evaluation on the negated first input is unchanged: the two factors of \(-1\) multiply to \(+1\). The intrinsic class (6), which uses \(P\) for the first input, and every defined scalar (7) are independent of this auxiliary rewriting. In characteristic two both signs already act as the identity, and the conclusion is the same. Reversing the auxiliary orientation while keeping the rewritten coefficient map fixed would omit one of the two required changes.

## Mathematical sources

M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §§1.5–2.3, pp. 196–197, supplies the coefficient-chain and conormal framework. The supported intersection construction used here is proved in the preceding programme lesson. The continuous section contributes a counit-normalized supported class independently of whether its graph is conic or Lagrangian.

P. Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=95), edition dated 01/08/2026, Corollary 4.6.2, Propositions 4.6.4, 4.6.6–4.6.7, §4.7, Proposition 5.1.5(a)–(c) and Proposition 5.1.9, pp. 95–98 and 107–108, treats the exceptional and orientation operations. The proof above evaluates the ordinary bundle unit against the compact fibre trace, then compares graph restriction with the adjoint of the supported cup. It keeps both output supports and proves the identity for the actual maps. The exercises distinguish conicity from symplectic isotropy, local numbers from compact totals, and intrinsic coefficients from an auxiliary orientation. The human sources retain their authorship and their own terms.
