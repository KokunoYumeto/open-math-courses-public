# Coefficients in a quantization of the identity

An identity contact transformation fixes the covectors, but its sheaf operator can still change the coefficients. A diagonal kernel with coefficient \(k[r]\) shifts every input by \(r\); a diagonal kernel with coefficient \(\mathbb Z/7\) over \(\mathbb Z\) kills rational coefficients. The question is therefore whether the coefficient operation itself is invertible. We will detect its inverse by applying a counit to one conormal test object \(k_S\), and we will also prove the full coefficient description of the conormal category.

The geometric inputs are [When a kernel quantizes a contact transformation](../../sheaf-proof-readings/src/SH03/when-a-kernel-quantizes-a-contact-transformation.md), [Local existence of contact kernel equivalences](local-existence-of-contact-kernel-equivalences.md), and [Microlocal composition at prescribed covectors](../../microlocal-composition-and-pure-sheaves/src/microlocal-composition-at-prescribed-covectors.md). Throughout, \(k\) is a commutative ring of finite global dimension \(g\), and our coefficient categories contain arbitrary bounded complexes of \(k\)-modules. Manifolds have the standing finite-dimensional, Hausdorff, countable-at-infinity hypotheses. Finite generation, perfectness and a field assumption are not implicit.

*Written by GPT-6.1 Sol and GPT-6 Astra (OpenAI), Ultra, September–October 2026. New original text is public domain (CC0).*

## The conormal category, including its morphisms

Fix a smooth closed submanifold \(i:S\hookrightarrow X\) in a coordinate neighborhood and a covector \(p\in T_S^*X\). Let \(\mathcal C_S(p)\) be the full subcategory of \(D^b(k_X;p)\) consisting of objects whose microsupport is contained in \(T_S^*X\) near \(p\). An isomorphism in the localized category preserves the microsupport germ, so this condition does not depend on the representative.

For \(A\in D^b(k)\), put \(A_S=i_*\underline A_S\), where \(\underline A_S\) is the constant complex on \(S\). We may shrink the chart throughout. Thus this notation describes a local coefficient model; it does not require the original sheaf to be constant along an entire global submanifold. The [supported conormal model, LFI9–LFI10](../../sheaf-proof-readings/src/SH02/local-forms-and-inverse-image.md#sh02-lfi-supported--replacing-a-complex-by-one-on-a-submanifold), supplies such an \(A_S\) for every object of \(\mathcal C_S(p)\).

We need to determine arrows as well as objects. For arbitrary bounded \(A,B\), the functor of constant extension and closed direct image induces an isomorphism

\[
\operatorname{Hom}_{D^b(k)}(A,B[j])
\xrightarrow{\sim}
\operatorname{Hom}_{D^b(k_X;p)}(A_S,B_S[j])
\quad(j\in\mathbb Z),
\qquad\text{(1)}
\]

We prove this by following two functorial comparisons. Write \(N=T_S^*X\), let \(j:N\hookrightarrow T^*X\) be the inclusion, and let \(\pi:N\to S\) be the projection. The calculation to establish is

\[
\mu\operatorname{hom}_X(A_S,B_S)
\simeq j_*\pi^{-1}\underline{R\operatorname{Hom}_k(A,B)}_S.
\]

**First comparison: form constant complexes on \(S\).** Take the submersion \(q:S\to\{*\}\). Its cotangent correspondence is \(T^*S\xleftarrow{z}S\xrightarrow q\{*\}\), with \(z\) the zero section. At a point, microlocal Hom is derived module Hom. The upper arrow of [MH12 and its submersion isomorphism proof](../../sheaf-proof-readings/src/SH02/microlocal-hom.md#sh02-mh-pair-transport--moving-both-arguments-at-once) therefore gives

\[
z_*\underline{R\operatorname{Hom}_k(A,B)}_S
\xrightarrow{\sim}
\mu\operatorname{hom}_S(q^!A,q^{-1}B\otimes\omega_S).
\]

The proper direct image by \(z\) is its exact closed direct image. Since \(q^!A=\underline A_S\otimes\omega_S\), the two Hom inputs carry the same invertible orientation complex. The evaluation-compatible [common-twist comparison MH1](../../sheaf-proof-readings/src/SH02/microlocal-hom.md#sh02-mh-twists--twisting-both-arguments-and-changing-an-arrow) cancels that factor. We have consequently identified the left side with \(\mu\operatorname{hom}_S(\underline A_S,\underline B_S)\). This argument retains \(R\operatorname{Hom}_k(A,B)\); it needs no expression of it as a tensor product with a dual of \(A\).

**Second comparison: extend the complexes from \(S\) to \(X\).** Let \(E_i=S\times_XT^*X\), and denote its covector maps by \(\rho_i:E_i\to T^*S\) and \(\varpi_i:E_i\to T^*X\). The upper arrow of [MH13 and its closed-embedding isomorphism proof](../../sheaf-proof-readings/src/SH02/microlocal-hom.md#sh02-mh-pair-transport--moving-both-arguments-at-once) is

\[
R\varpi_{i!}\rho_i^{-1}
\mu\operatorname{hom}_S(\underline A_S,\underline B_S)
\xrightarrow{\sim}
\mu\operatorname{hom}_X(i_*\underline A_S,i_*\underline B_S).
\]

Here \(Ri_!=Ri_*=i_*\), since \(i\) is closed. The inverse image of the zero section by \(\rho_i\) is precisely \(N\). If \(u:N\hookrightarrow E_i\), inverse image of closed extension gives
\(\rho_i^{-1}z_*\underline{R\operatorname{Hom}_k(A,B)}_S
\simeq u_*\pi^{-1}\underline{R\operatorname{Hom}_k(A,B)}_S\).
This identity can be checked on stalks. Applying \(R\varpi_{i!}\) yields \(j_*\pi^{-1}\underline{R\operatorname{Hom}_k(A,B)}_S\), because \(\varpi_i u=j\) is closed. Substitution in the preceding comparison proves the claimed calculation. The common orientation was canceled in the first comparison, so no codimension shift remains.

These maps also determine the normalization in (1). MH12 is built from pulled-back evaluation and its adjoint. After the common orientation is removed, it carries \(A\to B[r]\) to the corresponding constant sheaf arrow on \(S\). MH13 is built from evaluation and the ordinary direct-image counit, so for this closed embedding it carries that arrow to its image under \(i_*\). Their composite is therefore the actual coefficient arrow furnished by \(A\mapsto A_S\). Taking a stalk at \(p\) and using the point-localized morphism theorem MC.4 identifies its degree \(r\) with
\(H^rR\operatorname{Hom}_k(A,B)=\operatorname{Hom}_{D^b(k)}(A,B[r])\).
This proves (1) with identities and composition, since the identified map comes from the stated functor. Both the conormal calculation and MC.4 include zero covectors.

Combining this morphism calculation with the bounded object model gives

\[
I_S:D^b(k)\xrightarrow{\sim}\mathcal C_S(p),
\qquad A\longmapsto A_S.
\qquad\text{(2)}
\]

The object model proves essential surjectivity, and (1) proves full faithfulness for every pair. Constant extension and closed direct image preserve triangles, so the equivalence is exact. The argument establishes more than the existence of coefficient models, and more than a calculation with the single first argument \(k_S\).

That single first argument nevertheless provides a useful probe. Set \(Q_S(F)=\mu\operatorname{hom}_X(k_S,F)_p\). The [microlocal-Hom support bound MO15](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-microlocal-support--where-directional-sheaves-can-live) makes \(Q_S\) an exact functor on \(D^b(k_X;p)\): a cone whose microsupport misses \(p\) has zero image. The [submanifold formula](../../sheaf-proof-readings/src/SH02/microlocal-hom.md#sh02-mh-submanifold--recovering-microlocalization-from-hom) identifies this probe with the stalk of microlocalization along \(S\). For \(A_S\), specialization is the constant complex with coefficient \(A\) on the zero section of the normal bundle, extended by zero. Fourier transformation sends it to that same constant coefficient on the dual bundle. Thus \(Q_S(A_S)\simeq A\), without a shift. This is the supported-coefficient version of the [normalized conormal example](../../sheaf-proof-readings/src/SH02/microlocal-hom.md#sh02-mh-examples--models-that-test-the-hypotheses), and also follows from the arbitrary-pair calculation above with \(A=k\).

Every cotangent point has such a local probe. At \(p=(x;0)\), take \(S=X\) in a small chart. At \(p=(x;\xi)\) with \(\xi\ne0\), choose a coordinate \(t\) with \(dt_x=\xi\) and take \(S=\{t=t(x)\}\). Both the coefficient extraction and (2) are consequently available at zero and nonzero covectors.

## A diagonal coefficient is the local identity kernel

Let \(K\) be a kernel over the identity on a chosen cotangent neighborhood \(\Omega\) of \(p\). The physical graph uses the antipodal covector on the second factor:

\[
\Lambda_{\mathrm{id}}=
\{(x,x;\xi,-\xi):(x;\xi)\in\Omega\}
\subset T_\Delta^*(X\times X),
\qquad\text{(3)}
\]

Here \(\Delta\subset X\times X\) is the diagonal. Impose the two selected-region microsupport conditions of [the contact-kernel theorem](../../sheaf-proof-readings/src/SH03/when-a-kernel-quantizes-a-contact-transformation.md). Applying [LFI9–LFI10](../../sheaf-proof-readings/src/SH02/local-forms-and-inverse-image.md#sh02-lfi-supported--replacing-a-complex-by-one-on-a-submanifold) to this diagonal conormal produces \(M\in D^b(k)\) and

\[
K\simeq M_\Delta
\quad\text{in }D^b(k_{X\times X};(p,p^a)).
\qquad\text{(4)}
\]

The passage from this kernel isomorphism to a sheaf operator uses [Kernels that act on every incoming germ, formulas (14)–(16)](../../microlocal-composition-and-pure-sheaves/src/microlocal-composition-at-prescribed-covectors.md#kernels-that-act-on-every-incoming-germ). The full selected-region containment imposed above says that every kernel covector over the selected output neighborhood lies on the identity graph, so it excludes a second branch coming from a different input covector. A graph description only near the chosen kernel covector would not provide this exclusion. The confined-representative comparison there therefore identifies its germ action with the regional localized operator. Consequently a roof representing (4) acts through that kernel-germ calculus, and for \(G\in D^b(k_X;p)\) we obtain naturally

\[
\Phi_KG\simeq\Phi_{M_\Delta}G
\simeq M_X\otimes_k^LG.
\qquad\text{(5)}
\]

The second identification is an ordinary sheaf calculation before localization. Let \(\delta:X\hookrightarrow X\times X\) be the diagonal map and \(q_1,q_2\) the two projections. The closed-embedding projection formula gives
\(M_\Delta\otimes_k^Lq_2^{-1}G\simeq\delta_*(M_X\otimes_k^LG)\).
The restriction of \(q_1\) to this closed support is the identity, so applying \(Rq_{1!}\) gives \(M_X\otimes_k^LG\). This calculation introduces neither a dualizing factor nor a dimension shift; it explains the shift example in the introduction.

The conclusion concerns the germ at \((p,p^a)\) and its action at \(p\). It supplies no globally constant diagonal model on all of \(X\times X\), nor one coefficient complex valid throughout an arbitrary large cotangent region. In particular it does not discard the possibility of nontrivial coefficient local systems in a global identity kernel.

## A directional tensor equivalence forces a coefficient equivalence

**Theorem.** For any \(p\in T^*X\) and any \(M\in D^b(k)\), suppose

\[
L=M_X\otimes_k^L-:
D^b(k_X;p)\longrightarrow D^b(k_X;p)
\qquad\text{(6)}
\]

is an equivalence. Then

\[
T_M=M\otimes_k^L-:
D^b(k)\longrightarrow D^b(k)
\qquad\text{(7)}
\]

is an equivalence as well.

**Proof by extracting the inverse coefficient.** The proposed right adjoint on sheaves is

\[
R=R\mathcal Hom(M_X,-).
\qquad\text{(8)}
\]

It must first be checked in the bounded categories being used. If \(M\) has cohomology in \([a,b]\) and \(F\) in \([c,d]\), M43–M44, bounded Hom for arbitrary inputs, place (8) in \([c-b,d-a+3n+g+1]\) on an \(n\)-manifold. This bound allows arbitrary coefficient modules. Finite global dimension also keeps tensor products bounded.

The [noncharacteristic tensor and Hom estimates MO21–MO22](../../sheaf-proof-readings/src/SH02/microsupport-operations.md#sh02-mo-diagonal--tensor-and-hom-on-one-manifold) give

\[
\operatorname{SS}(LF)\subset\operatorname{SS}(F),
\qquad \operatorname{SS}(RF)\subset\operatorname{SS}(F).
\qquad\text{(9)}
\]

Indeed \(M_X\) has microsupport in the zero section, so both no-cancellation conditions hold, and adding its possible zero covectors cannot enlarge the other microsupport. These are the tensor and Hom estimates themselves; the separate evaluation assertion MO23, with its constructibility hypothesis, is unnecessary here.

Both functors therefore send objects null at \(p\) to objects null at \(p\). Their tensor–Hom unit and counit descend to the localized category and still satisfy the triangle identities. Hence (8) is right adjoint to (6). Since (6) is an equivalence, this right adjoint is its inverse, and the counit \(\epsilon:LR\to\mathrm{id}\) is an isomorphism in that category.

Choose a local \(S\) as above and apply the inverse to \(k_S\). By (9), \(R(k_S)\) belongs to \(\mathcal C_S(p)\). The [bounded conormal object model LFI9–LFI10](../../sheaf-proof-readings/src/SH02/local-forms-and-inverse-image.md#sh02-lfi-supported--replacing-a-complex-by-one-on-a-submanifold) gives \(N\in D^b(k)\) and an isomorphism \(u:N_S\xrightarrow{\sim}R(k_S)\). Closed extension commutes with tensoring by a constant coefficient, so the actual counit at this test object gives an isomorphism

\[
(M\otimes_k^L N)_S
\xrightarrow{\sim}L(N_S)
\xrightarrow{L(u)}LR(k_S)
\xrightarrow{\epsilon_{k_S}}k_S.
\]

Apply the exact probe \(Q_S=\mu\operatorname{hom}_X(k_S,-)_p\). Its supported-coefficient calculation gives an isomorphism \(M\otimes_k^L N\xrightarrow{\sim}k\). Associativity and symmetry of derived tensor now identify both composites of \(M\otimes_k^L-\) and \(N\otimes_k^L-\) with the identity. These functors remain bounded by finite global dimension. Thus \(N\otimes_k^L-\) is a two-sided inverse of (7). This proof uses the object model and the single coefficient probe; it does not require full faithfulness for every pair of conormal objects. \(\square\)

**Second proof through the whole conormal category.** Equation (9) says that both \(L\) and its inverse \(R\) preserve \(\mathcal C_S(p)\). Their unit and counit restrict to isomorphisms on that full subcategory. In particular every conormal \(F\) has the conormal preimage \(RF\), with \(LRF\simeq F\). Thus the restricted functors are inverse equivalences. This is where preservation by the inverse is needed; preservation by \(L\) alone would not provide those preimages.

For any coefficient complex \(A\), tensor and closed extension give the natural comparison

\[
L I_S(A)=(M_X\otimes A_S)
\simeq(M\otimes A)_S=I_S T_M(A).
\qquad\text{(10)}
\]

Conjugating the restricted equivalence by (2) and using (10) identifies it with \(T_M\), which proves (7) again. This second argument uses the full arbitrary-pair morphism statement (1). It explains categorically why both preservation assertions are required, while the first argument exhibits an inverse coefficient directly. \(\square\)

Conversely, a tensor inverse in the coefficient category supplies inverse tensor functors on sheaves and hence at every covector. We spell out the module criterion next, including the counit that produces such an inverse from a coefficient equivalence.

## What invertibility means over the ring

For \(M\in D^b(k)\), the following conditions are equivalent:

1. \(T_M\) is an equivalence of \(D^b(k)\).
2. Some \(N\in D^b(k)\) satisfies \(M\otimes_k^LN\simeq k\).

**Proof.** The right adjoint of \(T_M\) is \(R\operatorname{Hom}_k(M,-)\). It is bounded: if the two inputs have cohomology in \([a,b]\) and \([c,d]\), respectively, its cohomology lies in \([c-b,d-a+g]\). When \(T_M\) is an equivalence, its right adjoint is its inverse, so the adjunction counit evaluated at \(k\) is an isomorphism

\[
M\otimes_k^L R\operatorname{Hom}_k(M,k)
\xrightarrow{\sim}k.
\qquad\text{(11)}
\]

Taking \(N=R\operatorname{Hom}_k(M,k)\) proves the second condition. Conversely, the identity \(M\otimes_k^LN\simeq k\), together with associativity and symmetry, identifies \(T_MT_N\) and \(T_NT_M\) with the identity. The same calculation on sheaves makes \(M_X\otimes_k^L-\) and \(N_X\otimes_k^L-\) inverse equivalences. Equation (9), applied to these constant coefficients, gives their descent at every cotangent point. \(\square\)

For example, an invertible module \(P\) is finite projective of rank one, with \(P\otimes_kP^\vee\simeq k\). It gives the inverse pair \(P[r]\) and \(P^\vee[-r]\). This produces invertible complexes over a general ring, but it does not classify every invertible complex as one shifted invertible module. The last exercise shows why one global shift can fail.

Over a nonzero field, however, an invertible bounded complex is exactly a shifted one-dimensional vector space. To see this, choose an inverse \(N\) using (11). The bounded Künneth formula is
\(H^*(M\otimes_k^LN)=H^*(M)\otimes_kH^*(N)\).
Both graded factors are nonzero, since their tensor is \(k\). If either factor had nonzero terms in two degrees, tensoring them with any fixed nonzero term of the other factor would produce nonzero terms in two different output degrees. Hence each factor has just one nonzero degree. The tensor in that degree has dimension one, which forces both factors to be one-dimensional, even though finite-dimensionality was not assumed. A bounded complex over a field splits as its cohomology, so \(M\) is a shifted line. A shifted line plainly has the opposite shift of its dual as tensor inverse.

If \(k\) is the zero ring, all the categories in question are zero categories and their unique functor is an equivalence. The one-dimensional conclusion belongs only to the nonzero-field case.

## Exercises with complete solutions

### The diagonal does not add a dimension shift

*Difficulty: Introductory.*

On an \(n\)-manifold take \(K=k_\Delta[r]\). Compute its operator and inverse at an arbitrary covector. Explain why the codimension \(n\) of the diagonal does not contribute another shift.

**Solution.** Formula (5) gives \(\Phi_KG=G[r]\), whose inverse is \(G\mapsto G[-r]\). The calculation uses closed direct image and the identity projection of the diagonal, not exceptional inverse image along the diagonal. Projection formula and \(q_1\delta=\mathrm{id}\) produce no dualizing complex. Consequently the only shift is the explicitly supplied \(r\).

### Preservation alone does not restrict an equivalence

*Difficulty: Intermediate.*

Find an equivalence of a category that takes a full subcategory into itself but whose restriction is not essentially surjective. Locate the extra check in the proof of the theorem.

**Solution.** Regard \(\mathbb Z\) as a discrete category and use the equivalence \(n\mapsto n+1\). The full subcategory on nonnegative integers is preserved, but zero is absent from the restricted image. In the theorem the right adjoint is an inverse to \(L\), and the second estimate in (9) shows that this inverse also preserves the conormal subcategory. For every conormal object \(F\), its inverse \(RF\) is again conormal and \(LRF\simeq F\). This is the missing essential-surjectivity check.

### A torsion coefficient cannot quantize the identity invertibly

*Difficulty: Intermediate.*

Let \(k=\mathbb Z\) and \(M=\mathbb Z/7\) in degree zero. Show that \(M\otimes^L-\) is not a coefficient equivalence. Explain its consequence for a directional identity operator.

**Solution.** The nonzero module \(\mathbb Q\) is flat over \(\mathbb Z\), and \((\mathbb Z/7)\otimes\mathbb Q=0\). Thus \(M\otimes^L\mathbb Q=0\), so the functor sends a nonzero object to zero and cannot be an equivalence. The theorem rules out an equivalence \(M_X\otimes-\) at any covector. One may also test the nonzero conormal object \(\mathbb Q_S\): (2) proves it is nonzero at \(p\), while (10) shows its image is zero.

### Different components can carry different shifts

*Difficulty: Advanced.*

Let \(k=k_1\times k_2\), with both factors nonzero and of finite global dimension. Write \(e_1,e_2\) for the central orthogonal idempotents. For integers \(r\ne s\), prove that
\(M=e_1k[r]\oplus e_2k[s]\)
is invertible. Show that it is not a single shifted invertible module over \(k\).

**Solution.** The idempotent summands are projective, their mixed tensor products are zero, and \(e_i k\otimes e_i k\simeq e_i k\). Hence with \(N=e_1k[-r]\oplus e_2k[-s]\) the tensor \(M\otimes^L N\) is \(e_1k\oplus e_2k=k\). The preceding criterion proves invertibility. On an arbitrary complex \(A\), tensor with \(M\) shifts \(e_1A\) by \(r\) and \(e_2A\) by \(s\). Because the factors are nonzero and \(r\ne s\), \(M\) has nonzero cohomology in two different degrees. A single shifted module has cohomology in at most one degree, so no such description is possible. Its diagonal kernel is nevertheless an equivalence above the identity. This example explains why the field classification cannot be imposed over a disconnected coefficient ring.

## References

The reduction from an identity contact action to an equivalence of coefficient complexes is classical. Its direct antecedent is M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque **128** (1985), **Remark 6.3.6, printed pp. 114–115 / PDF pp. 117–118**. The remark uses a conormal test category and the coefficient object model of Proposition 6.2.2, printed p. 106 / PDF p. 109. Those arguments underlie the local coefficient reduction here.

The operator convention matters. On printed p. 109 / PDF p. 112, the source uses \(Rq_{1*}R\mathcal Hom(K,q_2^!G)\), whose coefficient operation is derived Hom from \(M\). This lesson uses \(Rq_{1!}(K\otimes_k^Lq_2^{-1}G)\), whose diagonal coefficient operation is \(M\otimes_k^L-\). Formula (5) and the two counit arguments establish the tensor-convention statements directly. The source section works primarily in \(D^+\) under finite weak global dimension; here the standing hypothesis is finite global dimension, and the boundedness argument above is retained for arbitrary bounded coefficient modules.

The arbitrary-pair conormal morphism assertion is proved here using the linked MH12 submersion comparison, MH1 common-orientation cancellation, MH13 closed-embedding comparison and MC.4 point-morphism theorem. Together with LFI9–LFI10, this supplies the full category used in the classical reduction. The linked proofs specify the six-operation, specialization, Fourier and cutoff inputs on which their comparisons depend. The present coefficient argument stays at one cotangent point and makes no global classification of identity kernels or of invertible complexes over all rings.

For broader orientation, P. Schapira's [*A short review on microlocal sheaf theory*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf) (2016) is further reading. The exact antecedent for this lesson is the Astérisque remark identified above.
