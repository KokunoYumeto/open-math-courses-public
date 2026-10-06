# Lefschetz traces of constructible correspondences

A correspondence can move information from one point to another before taking a trace. Its local class lives where the two maps coincide. Compactness of their common support makes the trace finite even when the original sheaf has noncompact support and infinite-dimensional global cohomology.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 2 October 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

Learn first Constructible traces and local Euler indices, Closed supports and evaluated proper transport, and Proper characteristic classes and the compact index. We use their actual diagonal comparison, graded evaluation, exceptional counit and compatibility of supported evaluation with the proper trace. Perfect operations and finite microlocal coefficients proves the compact supported-cohomology finiteness needed here. The supported cycle intersection supplies the graph interpretation. These are written programme proofs relative to their stated foundations; transitive prerequisite closure remains open.

## The two maps determine three supports

Let \(k\) be a characteristic-zero field. Manifolds are real analytic, Hausdorff and countable at infinity, with the standing finite uniform dimension bounds. Let \(f,g\) be real analytic maps and take

\[
 f,g:Y\longrightarrow X,\qquad
 F\in D^b_{\mathbb R\text{-c}}(k_X),\qquad
 \phi:f^{-1}F\longrightarrow g^!F.
 \qquad\text{(1)}
\]

Constructibility includes perfect stalks. Set

\[
 \begin{aligned}
 S&=\operatorname{supp}(F),\\
 T&=f^{-1}S\cap g^{-1}S,\\
 W&=\{y:f(y)=g(y)\},\qquad Z=T\cap W.
 \end{aligned}
 \qquad\text{(2)}
\]

Support means **closed support**: the complement of the largest open set where the complex vanishes. Thus \(S,T,Z\) are closed subanalytic sets. The equality set \(W\) is the inverse image of the closed diagonal under \(h=(f,g)\).

Put \(A=f^{-1}F\) and \(B=g^!F\). The perfect-operation theorem makes both constructible. Their supports lie in \(f^{-1}S\) and \(g^{-1}S\), respectively. Since the source \(A\) is supported on \(f^{-1}S\), supported adjunction gives a unique lift

\[
 \widehat\phi:A\longrightarrow R\Gamma_TB
 \longrightarrow B
 \qquad\text{(3)}
\]

of \(\phi\). Indeed \(R\Gamma_{f^{-1}S}A=A\), and
\(R\Gamma_{f^{-1}S}B=R\Gamma_TB\): \(B\) already vanishes outside \(g^{-1}S\). The equality uses the composition law for closed support functors. The lift comes from a supported **source**, rather than from an arbitrary map whose restriction happens to vanish.

Assume for the trace theorem that

\[
 T\text{ is compact}.
 \qquad\text{(4)}
\]

Then

\[
 C=R\Gamma(X;F),\qquad P=R\Gamma_T(Y;B)
 \qquad\text{(5)}
\]

have different roles. The complex \(P\) is perfect by compact supported-cohomology finiteness. The cohomology of \(C\) need not be finite-dimensional.

Ordinary pullback followed by (3) gives \(a:C\to P\). For the return map use

\[
 \begin{aligned}
 b:P&=R\Gamma_c(Y;R\Gamma_TB)
 \longrightarrow R\Gamma_c(Y;g^!F)\\
 &\longrightarrow R\Gamma_c(X;F)
 \longrightarrow R\Gamma(X;F)=C.
 \end{aligned}
 \qquad\text{(6)}
\]

The middle arrow is the exceptional counit \(Rg_!g^!F\to F\); the last forgets compact support. The first equality follows from compactness of \(T\). This constructs the correspondence endomorphism

\[
 U_\phi=ba:C\longrightarrow C.
 \qquad\text{(7)}
\]

No ordinary direct-image counit \(Rg_*g^!F\to F\) has been inserted. It would not be supplied by the adjunction being used when \(g\) is nonproper.

## A finite-rank trace does not require a finite vector space

For a finite-rank endomorphism \(u:V\to V\), choose a finite-dimensional subspace \(E\) containing its image. It is invariant under \(u\), and define

\[
 \operatorname{tr}_{\mathrm{fin}}(u)=\operatorname{tr}(u|_E).
 \qquad\text{(8)}
\]

**Lemma.** This definition is independent of \(E\). If \(p:V\to Q\) and \(q:Q\to V\), with \(Q\) finite-dimensional, then

\[
 \operatorname{tr}_{\mathrm{fin}}(qp)=\operatorname{tr}(pq).
 \qquad\text{(9)}
\]

**Proof.** For two choices \(E_1,E_2\), work in \(E_1+E_2\). Its quotient by either \(E_i\) has zero induced endomorphism because the full image lies in \(E_i\). A basis adapted to an invariant subspace gives a block triangular matrix, so the trace on the sum equals the trace on either \(E_i\).

For (9), take \(E=\operatorname{im}q\). Regard \(q\) as a map \(Q\to E\) and restrict \(p\) to \(E\). In finite bases the two traces are both the sum \(\sum_{i,j}q_{ij}p_{ji}\). This proves (9), including nonsurjective \(q\) and noninjective \(p\). \(\square\)

Each \(H^j(U_\phi)\) factors through the finite-dimensional \(H^j(P)\). It has finite rank, and it is zero whenever \(H^j(P)=0\). Consequently

\[
 L(\phi)=\sum_j(-1)^j
       \operatorname{tr}_{\mathrm{fin}}H^j(U_\phi)
       =\operatorname{str}(ab:P\to P)
 \qquad\text{(10)}
\]

is a finite sum. The point trace proof in the first prerequisite identifies the supertrace of a perfect complex endomorphism with this alternating cohomology trace. Formula (9) proves the equality in (10) degree by degree.

This is a trace in \(k\). It need not be an integer: the correspondence may act by arbitrary coefficient endomorphisms. If \(F\) has compact closed support, \(C\) is perfect, and (10) is its usual supertrace.

## Pull the diagonal identity to the coincidence set

Write \(D_XF=R\mathcal Hom(F,\omega_X)\) and \(K=F\boxtimes D_XF\). The normalized diagonal comparison from the trace prerequisite is

\[
 R\mathcal Hom(F,F)\simeq\delta^!K,\qquad
 \delta:X\hookrightarrow X\times X.
 \qquad\text{(11)}
\]

Under global adjunction, the identity of \(F\) gives a supported diagonal class

\[
 e_\Delta(F)\in H^0_\Delta(X\times X;K).
 \qquad\text{(12)}
\]

Its underlying construction is the actual exceptional diagonal restriction, with the product evaluation and its graded tensor order.

For any map \(h\), the ordinary unit \(K\to Rh_*h^{-1}K\), followed by supported sections, supplies

\[
 R\Gamma_\Delta(X\times X;K)
 \longrightarrow R\Gamma_{h^{-1}\Delta}(Y;h^{-1}K).
 \qquad\text{(13)}
\]

Here is the derived adjunction check of the support comparison. Let \(i:W=h^{-1}\Delta\hookrightarrow Y\) and let \(v:W\to X\) be the map to the diagonal. Closed proper base change gives \(h^{-1}\delta_*Q=i_*v^{-1}Q\). For a bounded test object \(Q\), the adjunctions consequently give
\[
 \begin{aligned}
 \operatorname{Hom}(Q,\delta^!Rh_*H)
 &\simeq\operatorname{Hom}(\delta_*Q,Rh_*H)\\
 &\simeq\operatorname{Hom}(h^{-1}\delta_*Q,H)\\
 &\simeq\operatorname{Hom}(v^{-1}Q,i^!H)
 \simeq\operatorname{Hom}(Q,Rv_*i^!H).
 \end{aligned}
 \qquad\text{(13a)}
\]
Thus \(\delta^!Rh_*H\simeq Rv_*i^!H\), with the isomorphism fixed by these adjunctions. Apply it to the ordinary unit \(K\to Rh_*h^{-1}K\), then take global sections. The result is (13), since \(R\Gamma(W;i^!h^{-1}K)=R\Gamma_W(Y;h^{-1}K)\). This proves its map and support, without imposing properness on \(h\) or choosing a pullback of dualizing complexes.

For \(h=(f,g)\), constructible duality gives the evaluated comparison

\[
 h^{-1}K
 =f^{-1}F\otimes g^{-1}D_XF
 \simeq A\otimes D_YB.
 \qquad\text{(14)}
\]

Here \(D_Y(g^!F)\simeq g^{-1}D_XF\), by exceptional-Hom duality and biduality. Both sides are supported on \(T\); therefore the class pulled back in (13) refines from support \(W\) to \(Z=W\cap T\).

Apply \(\phi\) to the first factor and then the ordered contraction
\(B\otimes D_YB\to\omega_Y\). This defines

\[
 C(\phi)\in H^0_Z(Y;\omega_Y).
 \qquad\text{(15)}
\]

Construction (11)–(15) does **not** require (4). Only integrating it and using the finite intermediate trace will require compactness. The contraction is symmetry followed by dual-first evaluation, so its point value is the supertrace with signs \((-1)^j\).

The class is linear in \(\phi\), invariant under an isomorphism of the coefficient complex compatible with \(\phi\), and compatible with open restriction. These follow from the actual units, counits, support comparison and evaluation: conjugating the coefficient object conjugates the identity in (12), and evaluation cancels the two conjugate factors.

## The compact-support trace square

**Theorem.** Under (1) and (4), with the finite-rank meaning (10),

\[
 L(\phi)=\int_Y C(\phi).
 \qquad\text{(16)}
\]

The integral is the map from support \(Z\) to compact support, followed by the proper point trace \(R\Gamma_c(Y;\omega_Y)\to k\).

First suppose that \(S\) is compact. Then \(C\) is perfect, and proper duality for \(X\to\mathrm{pt}\) identifies
\(R\Gamma(X;D_XF)\) with \(C^\vee\). The product and diagonal maps in the proper characteristic-class proof, **before contraction**, identify (12) with the tensor representing \(\mathrm{id}_C\). This uses its Hom comparison and evaluation square, not only its final identity index formula.

The ordinary \(f\)-pullback and \(\phi\) send the first tensor factor to \(P\) by \(a\). Perfect duality and the compact support cutoff identify \(P^\vee\) with \(R\Gamma(T;(D_YB)|_T)\): the internal-Hom formula gives \(D_Y(R\Gamma_TB)=k_T\otimes D_YB\), and properly supported global duality gives the stated pairing. The second factor therefore goes by ordinary \(g\)-pullback to sections of \(D_YB\) and then to its restriction on \(T\). This is exactly the dual \(b^\vee:C^\vee\to P^\vee\).

To verify the last assertion, pair a section of \(R\Gamma_TB\) with the pulled-back dual section. The evaluated internal-adjunction formula in the closed-support prerequisite says that integrating their contraction equals pairing the original dual section with (6): projection, the ordinary counit, evaluation, then the exceptional counit give the same ordered pairing. Compactness of \(T\) supplies the proper support throughout. Currying this equality determines \(b^\vee\).

The resulting trace square can be written

\[
 \begin{array}{ccc}
 k&\xrightarrow{\mathrm{coev}_C}&C\otimes C^\vee\\
 &&\downarrow\,a\otimes b^\vee\\
 &&P\otimes P^\vee\xrightarrow{\mathrm{contr}_P}k.
 \end{array}
 \qquad\text{(17)}
\]

For a homogeneous basis \(e_{j,r}\) of a finite representative of \(C\), its value is
\(\sum_{j,r}(-1)^j e^*_{j,r}(ba(e_{j,r}))\). Boundary traces cancel by the point trace proof, leaving \(\operatorname{str}(ba)\).

On the sheaf side, the same path is (13)–(15) followed by integration: it pulls both factors to \(Y\), retains the coincidence support, applies \(\phi\), and evaluates. Enlarging \(Z\) to \(T\) for this pairing uses the natural inclusion of support conditions; it does not change the final properly supported trace. The evaluated identity above verifies the bottom cell of this comparison, and the proper diagonal/Hom comparison verifies its top cell. Thus (17) is the full trace diagram with its maps specified. It proves (16) for compact \(S\).

## A compact cutoff removes the extra support assumption

Keep compact \(T\), but allow \(S\) to be noncompact. Choose a compact subanalytic \(K_0\subset X\) whose interior contains \(f(T)\cup g(T)\). Such a set is obtained from finitely many closed coordinate balls covering this compact image, with closures inside their charts.

Set

\[
 G=R\Gamma_{K_0}F,\qquad c:G\longrightarrow F.
 \qquad\text{(18)}
\]

The perfect-operation theorem makes \(G\) constructible; its support is contained in \(S\cap K_0\), hence compact. On the interior of \(K_0\), \(c\) is the identity comparison. It therefore induces an isomorphism

\[
 R\Gamma_T(g^!G)\xrightarrow{\sim}R\Gamma_T(g^!F).
 \qquad\text{(19)}
\]

Indeed \(g^!c\) is an isomorphism on the open neighbourhood \(g^{-1}(\operatorname{int}K_0)\) of \(T\); supported excision proves (19).

Define the cutoff correspondence by

\[
 f^{-1}G\longrightarrow f^{-1}F
 \xrightarrow{\widehat\phi}R\Gamma_Tg^!F
 \xrightarrow{(19)^{-1}}R\Gamma_Tg^!G
 \longrightarrow g^!G.
 \qquad\text{(20)}
\]

Its common closed support \(T_G\) equals \(T\). Support containment gives \(T_G\subset T\), while at every \(y\in T\), \(G\) agrees with \(F\) near both \(f(y)\) and \(g(y)\), proving the reverse inclusion. On a neighbourhood of \(T\), the maps and objects in (20) identify with those of \(\phi\). In particular \(Z_G=Z\). Excision and the naturality of (11)–(15) consequently give

\[
 C(\phi_G)=C(\phi)\quad\text{in }H_Z^0(Y;\omega_Y).
 \qquad\text{(21)}
\]

For the traces, identify the intermediate supported complex by (19). Put \(C_G=R\Gamma(X;G)\), and let \(c_C:C_G\to C\) be induced by \(c\). Naturality of ordinary pullback and of the exceptional counit gives

\[
 a_G=a\,c_C,\qquad b=c_C\,b_G.
 \qquad\text{(22)}
\]

Therefore \(U_\phi=c_Cb_Ga\) and \(U_{\phi_G}=b_Gac_C\). Each degree factors through finite-dimensional \(H^j(C_G)\), so (9) proves equality of their alternating traces. Applying the compact-\(S\) theorem to \(G\) and using (21) proves (16) in full.

This proves the noncompact-support extension in Exercise IX.9. The cutoff is a proof device: independence of its choice follows because its trace is the intrinsic finite-rank trace of (7), and its class is the intrinsic supported class (15).

## Local contributions keep their own trace

For an isolated \(y\in Z\), support excision separates \(y\) from \(Z\setminus\{y\}\). Project (15) to
\(H^0_{\{y\}}(Y;\omega_Y)=k\), using the normalized point trace, and call the result \(C_y(\phi)\). If \(Z\) is finite, disjoint neighbourhoods give the direct sum of its point-supported complexes. Proper trace additivity and (16) then yield

\[
 L(\phi)=\sum_{y\in Z}C_y(\phi).
 \qquad\text{(23)}
\]

The point identification retains the orientation line and dimension shift in
\(i_y^!\omega_Y=k\); it introduces no additional ambient sign.

Now specialize to \(Y=X\), \(g=\mathrm{id}\), and \(\phi:f^{-1}F\to F\). At a fixed point \(x\), ordinary restriction gives a stalk endomorphism \(\phi_x\). If \(x\) is also isolated in \(f^{-1}(x)\cap T\), there is a point-support action on the complexes of sections

\[
 \begin{aligned}
 R\Gamma_{\{x\}}(X;F)
 &\longrightarrow R\Gamma_{f^{-1}(x)}(X;f^{-1}F)\\
 &\longrightarrow R\Gamma_{f^{-1}(x)}(X;F)
 \longrightarrow R\Gamma_{\{x\}}(X;F).
 \end{aligned}
 \qquad\text{(24)}
\]

The last arrow projects the isolated component of the support, after intersecting it with \(T\). It is not an ordinary stalk restriction. The induced traces of \(\phi_x\), of (24), and the number \(C_x(\phi)\) can differ.

The local number depends only on the germ of the pair: if \(F\) and \(F'\) are isomorphic on a neighbourhood \(U\) of an isolated fixed point, and the isomorphism intertwines their morphisms on \(U\cap f^{-1}U\), then
\[
 C_x(\phi)=C_x(\phi').
 \qquad\text{(25)}
\]
To prove this, choose a smaller neighbourhood whose image under \(f\) remains in \(U\). Open restriction of (11)–(15) identifies the two classes there; excision and the same normalized point trace identify their local numbers. No global isomorphism is needed.

## The constant sheaf gives a graph intersection

Let \(X\) be compact, \(F=k_X\), and \(\phi:f^{-1}k_X\to k_X\) the canonical map. Write \(\Gamma_f=\{(f(x),x)\}\). Then

\[
 C(\phi)=[\Gamma_f]\cap[\Delta_X],\qquad
 \sum_j(-1)^j\operatorname{tr}H^j(f^*)
       =\#([\Gamma_f]\cap[\Delta_X]).
 \qquad\text{(26)}
\]

The class on the right is supported on the fixed locus, with its graph parameter identified with \(X\). Both fundamental classes use the orientation coefficient inherited from the second projection, as in the normalized diagonal construction; no global orientation of \(X\) is chosen.

On the coincidence set the first and second projections agree. Their orientation lines are therefore canonically identified there, and the integral orientation-square pairing supplies the output dualizing coefficient. This is the coefficient pairing in (26); it does not assert a global trivialization of the orientation line on \(X\times X\). With an excess fixed locus, the intersection remains a supported cohomology class, as in the intersection prerequisite, rather than a literal zero-dimensional cycle.

**Proof.** Here \(K=k_X\boxtimes\omega_X\). The product evaluation identifies the diagonal identity (12) with the normalized diagonal fundamental class: in a coordinate ball, exceptional diagonal restriction cancels the normal orientation and dimension shift, and its point trace sends the positive generator to one. These are exactly the normal Thom and fundamental-cycle maps in the supported intersection prerequisite.

Restriction to \(h=(f,\mathrm{id})\) pulls that diagonal class to the graph. The fundamental-class projection formula for a closed graph identifies this pullback, with its retained support, with the intersection of the graph fundamental class and the diagonal class. This is the actual supported cup/intersection construction: it is defined by the same restriction, normal counit and coefficient pairing, also at nontransverse intersections. In (14) the first factor is \(k_X\), and the last contraction is \(k_X\otimes\omega_X\to\omega_X\), the identity. Thus (15) is precisely that supported intersection class. Integrating and applying (16) proves (26). \(\square\)

When there are no coincidences, (15) lies in the zero support group, so the correspondence trace is zero. A positive-dimensional fixed locus still has the supported class and global integral; the finite point sum (23) is used only for a finite locus. Computing general isolated contributions from specialization and expanding or shrinking spaces is the next treatment.

## Exercises with complete solutions

### An infinite global space with a three-point correspondence

*Difficulty: Intermediate.*

Take \(X=\mathbb N\) with its discrete zero-dimensional analytic structure, \(F=k_X\), and \(Y=\{a,b,c\}\). Let
\[
 (f(a),g(a))=(1,2),\quad
 (f(b),g(b))=(2,1),\quad
 (f(c),g(c))=(3,3),
\]
and let the three coefficient maps be multiplication by \(4,5,7\). Compute \(T,Z,P,U_\phi\), and both sides of (16). Repeat for \(F[1]\).

**Solution.** All points are in \(S\), so \(T=Y\) is compact and \(Z=\{c\}\). Global sections are the infinite-dimensional product \(C=\prod_{n\ge1}k\) in degree zero, whereas \(P=k^3\). Ordinary pullback followed by the coefficient maps gives
\(a(v)=(4v_1,5v_2,7v_3)\). The properly supported \(g\)-trace sends these three values to coordinates \(2,1,3\), respectively. Hence
\[
 U_\phi(v)=(5v_2,4v_1,7v_3,0,\ldots).
\]
Its image lies in the first three coordinates, and its finite-rank trace is \(7\). Equivalently \(ab\) on \(P\) has a \(2\times2\) off-diagonal block and diagonal entry \(7\); its trace is \(7\).

Only \(c\) is a coincidence. At a zero-dimensional point the dualizing trace is ordinary coefficient evaluation, so \(C_c(\phi)=7\), and its integral is \(7\). The two off-diagonal arrows contribute no local class. Shifting the input by \([1]\) places both intermediate and global cohomology in degree \(-1\), giving trace and local contribution \(-7\). Infinite-dimensional global sections have not been assigned an identity trace.

### Two graded loops must cancel the boundary terms

*Difficulty: Intermediate.*

Let \(X\) be a point, \(Y\) two points, and both maps constant. Let \(F\) be the complex \(k^2\to k^3\) in degrees zero and one, with \(d(x,y)=(x,0,0)\). At the first point use the chain map with matrices
\(\operatorname{diag}(2,3)\) and \(\operatorname{diag}(2,5,7)\); at the second use \(4\,\mathrm{id}_F\). Compute the local contributions and the global trace.

**Solution.** The first map commutes with \(d\), since both composites send \((x,y)\) to \((2x,0,0)\). Its cohomology action is multiplication by \(3\) on \(H^0=k\), and by \(5,7\) on \(H^1=k^2\). Its local supertrace is \(3-5-7=-9\). On terms it is \((2+3)-(2+5+7)=-9\); the boundary entry \(2\) cancels.

The second local contribution is \(4(1-2)=-4\). The exceptional trace from two points adds the maps, so the global endomorphism is their sum and its supertrace is \(-13\). Both points are coincidences, and the integral of the two point classes is \(-9-4=-13\). Ignoring the degree-one coefficient or summing ungraded matrix traces would give a different number.

### Two endpoint stalks cannot be the two local contributions

*Difficulty: Advanced.*

On \(\mathbb R\), put
\[
 f(t)=t+\tfrac1{10}t(1-t)e^{-t^2},\qquad F=k_{[0,1]}.
\]
Verify that \(f\) is an analytic diffeomorphism with exactly two fixed points and that it preserves the interval. For the canonical coefficient isomorphism, compare the global trace, the two stalk traces, and the two point-support traces. What follows about the local contributions without yet computing each separately?

**Solution.** The derivative of \(t(1-t)e^{-t^2}\) is
\((1-2t-2t^2+2t^3)e^{-t^2}\). Each of
\(|t|e^{-t^2},t^2e^{-t^2},|t|^3e^{-t^2}\) is at most one, so its absolute value is at most seven. Thus \(f'(t)\ge3/10>0\). Also \(f(t)-t\to0\) at both infinities. The map is bijective, and its nonzero derivative makes its inverse analytic. Its displacement vanishes exactly at \(0,1\); monotonicity makes it a homeomorphism of \([0,1]\).

Here \(T=[0,1]\), \(Z=\{0,1\}\), and \(R\Gamma(\mathbb R;F)=k\). Pullback of a constant interval section is the same section, so \(L(\phi)=1\). Both endpoint stalk actions are the identity on \(k\), with trace one.

Both endpoint costalks of the closed-interval sheaf are zero. At either endpoint, a small neighbourhood restricts \(F\) to a closed half-interval; deleting the endpoint leaves a contractible half-interval, and restriction of constant sections is an isomorphism. The localization triangle therefore has zero point-support term. The actions (24) have trace zero.

Nevertheless \(C_0(\phi)+C_1(\phi)=1\) by (23). They cannot both equal their stalk traces, whose sum is two, nor both equal their point-support traces, whose sum is zero. Their individual values require the later local localization calculation; the discrepancy already follows from this complete global calculation.

### A reflection changes the costalk action

*Difficulty: Intermediate.*

Let \(f(t)=1-t\), \(F=k_{[0,1]}[r]\), and take the canonical coefficient map. Find the local contribution at \(1/2\), the stalk trace, and the trace of (24). Explain the orientation sign in the last calculation.

**Solution.** The global section complex is \(k[r]\), and reflection fixes its constant section. Thus \(L(\phi)=(-1)^r\). The only fixed point in the support is \(1/2\), so its local contribution is the same number by (23). Its stalk is \(k[r]\) with identity action, giving the same trace.

Its point costalk is \(\operatorname{or}_{\mathbb R,1/2}\otimes k[r-1]\). Reflection reverses the local orientation and acts by \(-1\) on the point-support generator. One can compute this from the localization cokernel: deletion gives two components, and the quotient of \(k^2\) by the diagonal \(k\) is the support cohomology in degree one; exchanging the two components acts by \(-1\). The action (24) consequently has supertrace
\((-1)^{r-1}(-1)=(-1)^r\). Using only the costalk Euler number and ignoring its induced map would give the opposite sign.

### A circle map has a negative local contribution

*Difficulty: Advanced.*

Let \(X=S^1\), \(f(e^{2\pi it})=e^{4\pi it}\), \(F=k_X\), and take the canonical coefficient map. Compute the global trace and the local contribution at its fixed point. Compare with the stalk action, and with (26).

**Solution.** The map has exactly one fixed point: \(2t=t\) modulo integers forces \(t=0\) modulo integers. The circle has \(H^0=k,H^1=k\). The action on \(H^0\) is one. The action on \(H^1\) is multiplication by two: subdivide a positively oriented loop at the two preimages of a chosen point. Each of the two arcs maps once around the target loop, so evaluation of a pulled-back Čech or cellular degree-one cocycle on the loop is twice the original evaluation. This computes the induced cohomology map, rather than merely its stalk map.

The global supertrace is \(1-2=-1\). Since the fixed locus is one point, (23) gives local contribution \(-1\). Its stalk map is the identity on \(k\), with trace \(+1\). The supported graph-diagonal intersection in (26) therefore has number \(-1\), agreeing with the global trace. No transversality-based formula was needed to infer this particular number.

### Compactness of the common support is a substantive hypothesis

*Difficulty: Introductory.*

On the same infinite discrete \(X=\mathbb N\), take \(Y=X\), \(f=g=\mathrm{id}\), \(F=k_X\), and \(\phi=\mathrm{id}\). Explain exactly which construction remains valid and which trace argument fails. Does replacing \(\phi\) by zero make compactness a logically necessary condition for every trace?

**Solution.** The supported class (15) is still defined, with \(S=T=Z=X\). At every point it is the coefficient identity class. But \(P=C=\prod_{n\ge1}k\) is not perfect, and the identity has infinite-dimensional image. No finite-dimensional invariant subspace can contain it, so (8) does not define its trace. The infinitely many local contributions cannot be summed by the finite support argument (23), and there is no proper point trace for this noncompactly supported class.

For the zero correspondence the induced endomorphism has rank zero, so its finite-rank trace is zero even though \(T\) is still noncompact. Thus (4) is a sufficient geometric hypothesis for the theorem, not a claim that every individually traceable map must have compact \(T\). The counterexample concerns the identity and the failure of the theorem's general finiteness and proper integration guarantees.

## References and further reading

Lefschetz traces of constructible correspondences go back to Kashiwara's microlocal Lefschetz fixed-point formula for constructible sheaves. The compact cutoff argument above supplies the extension, with finite-rank trace understood explicitly.

Y. Matsui and K. Takeuchi, [*Microlocal study of Lefschetz fixed point formulas for higher-dimensional fixed point sets*, arXiv0812.4480v1, 24 December 2008](https://arxiv.org/abs/0812.4480v1), §2, describes the self-map characteristic class and local contributions with complex coefficients and compact sheaf support. Its later sections study smooth fixed components and Lefschetz cycles under additional hypotheses. Those component-localization results are separate from the general correspondence trace proved here.

Y. Ike, [*Microlocal Lefschetz classes of graph trace kernels*, arXiv1504.05439v3, 15 February 2016](https://arxiv.org/abs/1504.05439v3), §3.2, packages a self-map identity and evaluation into a graph trace kernel. Lemma3.7 constructs its two maps by diagonal and graph adjunction; equations(3.15)–(3.16) recover the graded trace over a point. The paper uses the graph \((x,f(x))\) and dual-first factors. Comparing with our \((f(x),x)\) requires the graded exchange of both factors. Its microlocal composition theorem is further reading.
