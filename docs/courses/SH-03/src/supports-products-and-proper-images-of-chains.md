# Supports, products and proper images of chains

To push a chain forward, control its closed support before integrating its oriented pieces. To multiply chains, keep their factor order before taking a boundary. These two rules make the same theory work with singular subanalytic supports, nonproper ambient maps and coefficients that are not fields.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 1 October 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

Subanalytic chains and closed cycle supports supplies the sheaves \(\mathcal C_p,\mathcal Z_p\), their support comparisons, boundary and softness. We use the programme's filtered colimits and stalkwise tensor products, and the SH-02 proper-support projection, exceptional trace and orientation lessons. This lesson treats supports, products and proper images of subanalytic chains, after M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §1, together with the chain-stalk flatness argument.

## Finite subdivisions make chain stalks flat

Continue with a commutative ring \(A\) of finite global dimension and real analytic manifolds of uniformly finite dimension, Hausdorff and countable at infinity. Write

\[
 \mathcal C^{-p}=\mathcal C_p,\quad d^{-p}=\partial_p,\quad
 \mathcal Z_p=\ker(\partial_p).
 \qquad\text{(1)}
\]

The local subdivision presentation already proves that every \((\mathcal C_p)_x\) is a filtered colimit of finite free \(A\)-modules.

**Proof.** Start with finitely many oriented chain germs near \(x\). In a relatively compact subanalytic neighborhood take a finite compatible triangulation of all their pieces. Delete lower-dimensional faces and choose an orientation on each open \(p\)-cell. Keep those cell germs whose closures contain \(x\). Their symbols span a finite free module: a relation must have zero coefficient on the interior of every such cell arbitrarily near \(x\), so each coefficient is zero. A common refinement compares any two choices; an old cell is replaced by its oriented pieces, with the inherited signs. Shrinking the neighborhood makes compatible descriptions identical as germs. Every finite collection of generators and relations is captured by such a refinement, exactly as in the chain-colimit proof of the preceding lesson. Thus their directed colimit is the entire stalk. \(\square\)

Tensoring a short exact sequence with these free modules is exact. Tensor commutes with filtered colimits, and filtered colimits of modules are exact. Consequently \(\mathcal C_p\) is flat. This argument does not prove that every stalk is finite free, and does not yet prove flatness of \(\mathcal Z_p\). For every sheaf \(F\),

\[
 \mathcal C_p\otimes_A^L F
 \simeq\mathcal C_p\otimes_A F=\mathcal C_p(F).
 \qquad\text{(2)}
\]

The earlier cutoff proof makes the latter sheaf soft. Its restriction to a closed fibre is c-soft; hence it is acyclic for proper direct image. The current projection prerequisite, applied to the flat, fibrewise c-soft sheaf \(\mathcal C_p\), gives the **actual** underived isomorphism

\[
 f_!\mathcal C_p\otimes_A F
 \xrightarrow{\sim}
 f_!\bigl(\mathcal C_p\otimes_A f^{-1}F\bigr).
 \qquad\text{(3)}
\]

It multiplies a properly supported section by a pulled-back coefficient section. The prerequisite proves this for arbitrary \(F\) by free presentations on each fibre; it also proves that \(f_!\mathcal C_p\) is flat. Thus no flatness of \(F\) is implicit in (3).

## Local systems give pure subanalytic supports

Let \(L\) be locally free of finite rank. A nonzero section
\(\alpha\in\Gamma(X;\mathcal C_p(L))\)
has a closed subanalytic support of pure dimension \(p\). The zero section has empty support.

**Proof.** Trivialize \(L\) near a point and use the finite cell refinement for all its finitely many coordinates. On an open \(p\)-cell the coefficient of the resulting chain is a locally constant vector, with its orientation sign. If that vector is nonzero, it stays nonzero throughout the connected cell; if zero, the cell contributes nothing. The support near the point is precisely the union of the closures of the nonzero \(p\)-cell pieces. A lower-dimensional germ cannot remain on its own: the chain presentation and ordinary orientation images determine it from arbitrarily nearby \(p\)-pieces. The finite local union is subanalytic, and every point of it is approached by \(p\)-dimensional pieces, proving purity. Closedness is part of the support definition. The local descriptions establish a closed subanalytic set globally, without requiring globally finitely many cells. \(\square\)

This assertion has a coefficient hypothesis. For arbitrary \(F\), a sheaf \(\mathcal C_p(F)\) can have sections supported on a set of smaller dimension or on a nonsubanalytic set. Exercise 1 checks the dimensional failure.

For a locally closed subanalytic \(S\) of dimension at most \(p\), set

\[
 T_S(L)=j_{S*}H^{-p}(\omega_S\otimes_A L|_S).
 \qquad\text{(4)}
\]

Finite local freeness lets tensoring commute with the lowest-degree and ordinary-image identifications locally. Thus these are exactly the coefficient versions of the \(T_S\) used earlier. The lowest-degree global calculation gives
\(\Gamma(X;T_S(L))=H^{-p}(S;\omega_S\otimes_A L|_S)\).

If \(S\) is **closed**, supported cycles satisfy

\[
 \Gamma_S(X;\mathcal Z_p(L))
 \simeq H^{-p}(S;\omega_S\otimes_A L|_S).
 \qquad\text{(5)}
\]

**Proof.** A cycle germ is represented on some closed \(S'\). If a section represented there is supported on \(S\), it is already supported on \(S\cap S'\) in that representative: all the closed-support transitions are injective, so enlargement cannot make a nonzero off-\(S\) germ vanish. The lowest closed-support identity identifies its supported part with \(T_{S\cap S'}(L)\). Enlarge the support to \(S\) to obtain \(T_S(L)\). Conversely \(T_S(L)\) maps injectively into cycles and is supported on \(S\). These local maps glue, giving
\(H^0_S\mathcal Z_p(L)=T_S(L)\).
Taking global sections and using the lowest-degree identity proves (5). We did not commute arbitrary global sections or closed-support functors with a filtered colimit. \(\square\)

For a **locally closed** \(S\), put \(B=\overline S\setminus S\). There is a more useful description:

\[
 \begin{split}
 H^{-p}(S;\omega_S\otimes_A L|_S)
 \simeq\{\,\alpha\in\Gamma_{\overline S}(X;\mathcal C_p(L)):
                    \operatorname{supp}(\partial\alpha)\subset B\,\}.
 \end{split}
 \qquad\text{(6)}
\]

The support condition is on \(\overline S\), so boundary germs are included.

**Proof.** The frontier triangle makes the boundary of a section of \(T_S(L)\) a cycle supported on \(B\). Its chain support is contained in \(\overline S\). This gives the forward map.

Conversely take a chain satisfying the right side. On \(O=X\setminus B\) it is a cycle supported on \(S\), which is closed in \(O\). Formula (5), in that open ambient manifold, identifies it with a section of \(H^{-p}(\omega_S\otimes L)\). Take the ordinary direct image of that section to \(X\). Its resulting chain agrees with the given chain on \(O\). Their difference is supported on \(B\), whose dimension is less than \(p\). The purity assertion for finite-rank \(L\) forces that difference to be zero. It also proves uniqueness. \(\square\)

This proof keeps both the closure in the chain support and the frontier in the boundary support.

## A global chain has an actual carrier

For finite-rank \(L\) the preceding descriptions prove

\[
 \begin{aligned}
 \Gamma(X;\mathcal C_p(L))
 &\simeq \underset{S\ \mathrm{locally\ closed},\ \dim S\leq p}
                     {\operatorname{colim}}
       H^{-p}(S;\omega_S\otimes L|_S),\\
 \Gamma(X;\mathcal Z_p(L))
 &\simeq \underset{S\ \mathrm{closed},\ \dim S\leq p}
                     {\operatorname{colim}}
       H^{-p}(S;\omega_S\otimes L|_S).
 \end{aligned}
 \qquad\text{(7)}
\]

Here the first comparison system uses the open-in-source, closed-in-target witnesses of the preceding lesson.

**Proof of representation and relations.** For a nonzero chain put
\(Z=\operatorname{supp}\alpha\) and \(D=\operatorname{supp}\partial\alpha\).
The boundary is local, so \(D\subset Z\). Purity makes \(Z\) a closed pure \(p\)-set and, unless the boundary is zero, \(D\) a closed pure \((p-1)\)-set. For \(p=0\), read \(D=\varnothing\). Set \(S=Z\setminus D\). Then
\(\overline S=Z\) and \(\partial S=D\):
a lower-dimensional closed subset cannot contain a relatively open piece of a pure \(p\)-set. Formula (6) represents \(\alpha\) on this single \(S\). A cycle instead has \(D=\varnothing\) and is represented on the closed \(Z\) by (5).

Suppose a section represented on a locally closed \(S'\) gives the zero chain. On a dense top regular refinement it has zero coefficients, so the comparison to that refinement is zero; this is already a relation in the first colimit. If two sections give the same chain, compare both to a common carrier refinement using their top regular pieces; their coefficient differences vanish there. On closed supports the transitions are injective, and a common closed union detects equality. This proves the colimit relations as well as surjectivity. The proof uses each chain's actual support, not a general rule that \(\Gamma\) commutes with sheaf colimits. \(\square\)

## Proper support makes the trace into a chain map

Let \(f:Y\to X\) be analytic. We construct

\[
 f_!\mathcal C^Y\longrightarrow\mathcal C^X.
 \qquad\text{(8)}
\]

Properness of \(f\) on all of \(Y\) is unnecessary. A section used in (8) must have support proper over the target open set.

For the untensored chain sheaves there is a correctly typed carrier description

\[
 f_!\mathcal C_p^Y
 \simeq \underset{S}{\operatorname{colim}}\,
        f_!j_{S*}H^{-p}\omega_S,
 \qquad f|_{\overline S}\ \mathrm{proper},\quad \dim S\leq p.
 \qquad\text{(9)}
\]

The terms on the right are sheaves on \(X\). To prove cofinality on stalks, take a chain section with proper support over a neighborhood \(U\) of \(x\). Choose a relatively compact subanalytic neighborhood of \(x\) whose closure lies in \(U\), and cut the source chain by its inverse image. The new chain agrees near the fibre over \(x\); its support is a closed subset of the original proper support over a compact target set, hence is compact. Extend it by zero in the source. Formula (7) then supplies a global carrier with that compact closure. Conversely every section of a term on the right has support proper over its domain. A common refinement has closure in the finite union of the two proper carriers, so the same comparison relations prove injectivity. This establishes (9) as a sheaf identity without an unproved colimit interchange.

Take such an \(S\), with \(T=\overline S\) and \(B=T\setminus S\). Put

\[
 K=f(T),\qquad C=f(B),\qquad V=K\setminus C=f(S)\setminus f(B).
 \qquad\text{(10)}
\]

Properness makes \(K,C\) closed subanalytic. We have \(\dim K\leq p\) and \(\dim C<p\); \(V\) is locally closed. Over \(V\),
\(S_0=T\cap f^{-1}V=S\cap f^{-1}V\)
is proper over \(V\). The exceptional-composition trace is
\[
 R(f_V)_!\omega_{S_0}\longrightarrow\omega_V.
 \qquad\text{(11)}
\]

Because both dualizing objects begin in degree \(-p\), degree \(-p\) in (11) is the underived direct image of their lowest sheaves. Restrict a section represented on \(S\) to \(S_0\), apply this trace, and take ordinary image from \(V\) to \(X\). This defines its image as a section of \(T_V\), hence as an \(X\)-chain. If the image has dimension less than \(p\), its lowest target sheaf is zero and the pushforward is zero.

The map commutes with the boundary:

\[
 \partial f_*\alpha=f_*(\partial\alpha).
 \qquad\text{(12)}
\]

**Proof with the actual localization maps.** On \(K\) use the triangle for \(V=K\setminus C\); on \(T\) use the one for \(S=T\setminus B\). Pulling back the constant-sheaf triangle for \(V\subset K\) gives the triangle with open piece \(f^{-1}V\) and closed piece \(f^{-1}C\). It maps to the triangle with open piece \(S\) and closed piece \(B\): the open arrow is extension from \(f^{-1}V\subset S\), the middle arrow is the identity of \(A_T\), and the closed arrow is restriction from \(f^{-1}C\) to \(B\). These arrows commute before deriving.

Dualize using the proper exceptional adjunction. For each bounded coefficient object \(H\) on \(T\), that adjunction gives
\(Rf_!D_TH=Rf_*D_TH\simeq D_KRf_!H\), with \(D=\operatorname{R\mathcal Hom}(-,\omega)\); properness on \(T\) identifies the two images. Duals of the ordinary coefficient-unit maps consequently give the trace maps below. The actual internal adjunction takes a bounded first input and a bounded-below dualizing target, as required. Its trace and coherent composition turn the coefficient diagram into
\[
 \begin{array}{ccccc}
 Rf_!\omega_B&\longrightarrow&Rf_!\omega_T&
       \longrightarrow&Rf_!Rj_{S*}\omega_S\longrightarrow Rf_!\omega_B[1]\\
 \downarrow&&\downarrow&&\downarrow\hspace{4.5em}\downarrow\\
 \omega_C&\longrightarrow&\omega_K&
       \longrightarrow&Rj_{V*}\omega_V\longrightarrow\omega_C[1].
 \end{array}
 \qquad\text{(13)}
\]
Push the closed-support objects to the indicated ambient spaces. The rightmost unshifted map is exactly restriction and (11), by the adjunction defining it; it is not a separately chosen cone map. The shifted arrow is the trace on \(B\to C\). The bottom closed set \(C\) can enlarge the actual frontier of \(V\); its extra lower-dimensional pieces do not change the degree-\(-p\) chain term.

Taking the connecting maps out of degree \(-p\) in (13) gives precisely (12). The bounds
\(\omega_B,\omega_C\in D^{\geq1-p}\)
identify degree \(1-p\) of their proper images with the images of the cycle sheaves used for the boundary. Closed-support enlargement preserves those cycles. Restriction and closed trace are natural, so the same diagram shows independence of carrier and compatibility with the comparisons in (9). This proves (8). \(\square\)

Identity maps give identity images. For composable maps proper on the successive actual supports, the composed image equals the image for the composite: the trace of exceptional composition is the successive trace, and the carrier restrictions agree on the common dense image. Thus this equality concerns the defined maps, not merely their support sets.

For any sheaf \(F\) on \(X\), (3) extends (8) to a chain map

\[
 f_!\mathcal C^Y(f^{-1}F)\longrightarrow\mathcal C^X(F).
 \qquad\text{(14)}
\]

Use the inverse of the normalized projection map (3), followed by (8) tensored with \(F\), in each degree. The projection is natural for the boundary morphisms, so this is a chain map. All terms are flat before tensoring and soft afterwards, as proved above; no local freeness or perfection of \(F\) is required. We call the image of a section with proper closed support \(f_*\alpha\).

## Products retain the geometric and cohomological order

For locally closed carriers \(S\subset X,T\subset Y\), the exceptional tensor and composition maps give a dualizing product

\[
 \omega_S\boxtimes^L\omega_T\longrightarrow\omega_{S\times T}.
 \qquad\text{(15)}
\]

Its normalization is the mate of the product of the two compact-support traces to \(A\); the proper-support projection and base-change comparisons identify the source of that pairing. We need the map, without asserting its invertibility for arbitrary singular carriers. The lowest cohomology classes in degrees \(-p,-q\) give a product in degree \(-p-q\). Refine carriers and use its trace naturality to obtain

\[
 \mathcal C^X(F)\boxtimes\mathcal C^Y(G)
 \longrightarrow\mathcal C^{X\times Y}(F\boxtimes G).
 \qquad\text{(16)}
\]

On oriented smooth pieces it is the ordered product orientation: first the \(X\)-coordinates, then the \(Y\)-coordinates. This follows by pairing their compact-support generators with their duals in the trace normalization. Tensor factors of \(F,G\) have degree zero here.

For \(\alpha\) of geometric degree \(p\) and \(\beta\) of degree \(q\),

\[
 \partial(\alpha\boxtimes\beta)
  =(\partial\alpha)\boxtimes\beta
       +(-1)^p\alpha\boxtimes(\partial\beta).
 \qquad\text{(17)}
\]

**Proof of the sign and map compatibility.** In a finite compatible cell refinement take product orientations. A codimension-one face from the first factor has its outward normal before both lists of tangent coordinates and contributes its first-factor incidence sign. A face from the second factor moves that outward normal past the \(p\) coordinates of the first, giving the additional \((-1)^p\). Triangulating a product cell preserves this boundary rule: interior faces have opposite orientations and cancel in pairs. The same rule is obtained by the connecting morphisms of the two frontier triangles; (15) is their trace-normalized tensor map, so it induces those incidence maps. Higher-codimension corners add no independent \((p+q-1)\)-chain. Dense refinement and the chain-colimit presentation prove (17) for all chains. Tensoring the equality with the degree-zero coefficient sections proves it for arbitrary \(F,G\). \(\square\)

Equation (17) is also the tensor-complex sign, because \((-1)^{-p}=(-1)^p\). It proves that (16) is a map of complexes and that a product of cycles is a cycle. The factor-exchange diffeomorphism satisfies
\[
 \tau_*(\alpha\boxtimes\beta)=(-1)^{pq}\beta\boxtimes\alpha.
 \qquad\text{(18)}
\]
Moving the \(p\) coordinates through the \(q\) coordinates proves this sign; it is exactly the Koszul sign in degrees \(-p,-q\). Products are associative with the stated order. Proper images of products agree with products of proper images whenever the two source supports have the required properness: their product is proper, and the two transposes are the same ordered product of traces.

## A strip homotopy gives a supported boundary

For two \(p\)-cycles \(\gamma_0,\gamma_1\) on \(X\), a chain homotopy in this sense consists of
\[
 t\in\Gamma_{X\times[0,1]}(X\times\mathbb R;\mathcal C_{p+1}),
 \qquad
 \partial t=i_{0*}\gamma_0-i_{1*}\gamma_1,
 \qquad\text{(19)}
\]
where \(i_s(x)=(x,s)\). The endpoint order is the convention in (19).

Projection \(q:X\times\mathbb R\to X\) is proper on the closed support of \(t\): over a compact \(K\subset X\), that support is closed in the compact \(K\times[0,1]\). Its image \(D=q(\operatorname{supp}t)\) is closed. Apply (12) and the identity \(qi_s=\mathrm{id}\) to get
\[
 \partial(q_*t)=\gamma_0-\gamma_1.
 \qquad\text{(20)}
\]

Thus the two cycles have the same class in
\(H^{-p}(\Gamma_D(X;\mathcal C))\),
or equivalently in its degree-\(p\) homological notation. Neither \(X\) nor \(D\) must be compact. The compact interval controls properness in the parameter direction.

For comparison, if \(I\) is the interval chain oriented from \(0\) to \(1\), then
\(\partial(\gamma\boxtimes I)=(-1)^p(i_{1*}\gamma-i_{0*}\gamma)\).
The chain \((-1)^{p+1}\gamma\boxtimes I\) satisfies (19) for the constant homotopy. This keeps the endpoint convention separate from the orientation chosen on the parameter interval.

We have constructed these operations before proving that \(\omega_X\to\mathcal C\) is an isomorphism. Their next use is a local half-ray contraction. That argument must still prove properness of its addition map on the selected carrier; formal products alone do not supply a contraction.

## Exercises with complete solutions

### Pure support needs the local-system hypothesis

*Difficulty: Intermediate.*

Let \(F=i_*(\mathbb Z/5)\) on \(\mathbb R\), supported at zero, and let \(p=1\). Exhibit a nonzero section of \(\mathcal C_1(F)\) with zero-dimensional support. Why does it not contradict the pure-support theorem? Explain what flatness does and does not imply here.

**Solution.** The left and right interval germs give
\((\mathcal C_1)_0=\mathbb Z^2\), so
\(\mathcal C_1(F)\) is the skyscraper with stalk \((\mathbb Z/5)^2\).
The global element \((1,0)\) is nonzero and has support \(\{0\}\), not a pure one-dimensional set. The coefficient sheaf is not locally free on the ambient line, so the pure-support theorem does not apply.

Chain-stalk flatness says that ordinary tensor with \(\mathcal C_1\) computes derived tensor and preserves short exact coefficient sequences. It does not say that tensoring preserves the geometric support dimension. The boundary of this section is \(1\in\mathbb Z/5\) at zero by the map \((a,b)\mapsto a-b\). The element \((1,1)\) is instead a cycle, still with the same zero-dimensional support. The later general coefficient-kernel theorem will include such cycles without imposing a pure-support statement on them.

### The closure in a locally closed carrier cannot be omitted

*Difficulty: Intermediate.*

Take the positive interval chain on \(S=(0,2)\subset\mathbb R\). Use (6) to locate its support and boundary. Can the right side of (6) be replaced by chains supported on \(S\) itself? Repeat with \(S=\mathbb R\setminus\{0\}\) and different weights on its two components.

**Solution.** Ordinary direct image of the orientation coefficient from \((0,2)\) has nonzero endpoint germs. The chain is supported on \([0,2]\), with boundary \([2]-[0]\). Thus it is on the right side of (6) with \(\overline S=[0,2]\) and frontier \(\{0,2\}\). It is not supported on the open \(S\), so removing the closure would discard the chain corresponding to the constant nonzero orientation section.

For the punctured line choose rightward weights \(a_-\) and \(a_+\). Its closure is all of \(\mathbb R\), its frontier is \(\{0\}\), and its boundary is
\((a_- -a_+)[0]\).
Every pair belongs to (6). Only the diagonal pairs are cycles. Ordinary image retains two independent germs at the deleted point; imposing closed cycle support on the unpunctured line imposes equality of the two coefficients.

### A nonproper projection can carry an unbounded proper chain

*Difficulty: Intermediate.*

Let \(f:\mathbb R^2\to\mathbb R\), \(f(x,y)=x\), and orient the parabola \(P=\{(s,s^2):s\in\mathbb R\}\) by increasing \(s\). Compute \(f_*[P]\). Compare the hyperbola \(H=\{(s,1/s):s>0\}\), with its parameter orientation. Is its closed carrier proper over \(\mathbb R\)?

**Solution.** The projection is not proper on the plane: a vertical fibre is unbounded. On the closed parabola it is a homeomorphism with inverse \(s\mapsto(s,s^2)\). The inverse image of a compact set is compact, so its restriction is proper despite the unbounded carrier. It preserves the chosen one-dimensional orientation. The normalized trace therefore gives \(f_*[P]=[\mathbb R]\), with zero boundary on both sides.

The positive hyperbola branch is closed in \(\mathbb R^2\): sequences with \(s\to0\) escape to infinity and have no finite limit there. It is nevertheless not proper over the target. Its part over the compact interval \([0,1]\) contains \((1/r,r)\) and is unbounded. Thus the hyperbola chain does not define a section in the domain of the global pushforward (8). The fact that its image is the familiar open ray does not repair missing properness of its carrier.

### A fold cancels oriented one-chains but preserves point weights

*Difficulty: Intermediate.*

For \(f:\mathbb R\to\mathbb R\), \(f(s)=s^2\), use the positive coordinate orientations to compute the images of the whole-line chain, the positive-ray chain and a point at \(s=-2\). Check (12) for the ray. Compare the reflection \(r(s)=-s\).

**Solution.** The square map is proper. Away from its critical value zero, the positive branch preserves orientation and the negative branch reverses it. Thus the whole-line chain has image coefficient \(1-1=0\) on the positive target ray, and zero elsewhere. A one-chain cannot have an isolated nonzero germ at zero; its whole pushforward is zero.

The rightward positive-ray chain \([(0,\infty)]\), with closed support \([0,\infty)\), has image the same rightward ray. Its boundary is \(-[0]\), and \(f_*[0]=[0]\). Both sides of (12) are therefore \(-[0]\). The point \([-2]\) maps to \([4]\) with coefficient \(+1\): zero-dimensional orientation has no derivative sign. Reflection sends the positively oriented whole line to its negative, but sends each point to its reflected point with its coefficient unchanged. The one-dimensional orientation degree and the zero-dimensional point weight are different calculations.

### Product faces and the strip sign

*Difficulty: Advanced.*

Let \(I=[0,1]\) and \(J=[0,2]\) denote their rightward interval chains, including ordinary-image boundary germs. Give the four oriented boundary edges of \(I\boxtimes J\), check the next boundary is zero, and compute the effect of exchanging the factors. For a \(p\)-cycle \(\gamma\), determine the sign of the constant strip chain that satisfies (19).

**Solution.** By (17),
\[
 \partial(I\boxtimes J)
  =[1]\boxtimes J-[0]\boxtimes J
      -I\boxtimes[2]+I\boxtimes[0].
 \qquad\text{(21)}
\]
The right edge points up, the left edge down, the upper edge left and the lower edge right. Taking another boundary yields
\[
 ([1,2]-[1,0])-([0,2]-[0,0])
   -([1,2]-[0,2])+([1,0]-[0,0])=0.
 \qquad\text{(22)}
\]
Every corner has two opposite contributions. Over characteristic two the minus signs become plus signs and each corner occurs twice, still zero. Factor exchange reverses the two-dimensional product orientation, so its image is \(-J\boxtimes I\), as \((-1)^{1\cdot1}=-1\).

For the strip with parameter oriented upwards,
\(\partial(\gamma\boxtimes[0,1])=(-1)^p(i_{1*}\gamma-i_{0*}\gamma)\).
Multiplying it by \((-1)^{p+1}\) gives exactly the endpoint order in (19). Projection of that signed strip is a valid pushforward because its support is closed in the compact-parameter strip, even if \(\gamma\) has noncompact support.

### A translation of an unbounded zero-cycle has a proper strip

*Difficulty: Advanced.*

On \(\mathbb R\), let
\(\gamma_0=\sum_{m\in\mathbb Z}[m]\) and
\(\gamma_1=\sum_{m\in\mathbb Z}[m+\tfrac12]\).
Construct a chain \(t\) in \(\mathbb R_x\times\mathbb R_u\) satisfying (19) for \(p=0\), and compute \(q_*t\). Verify properness and its boundary without assuming compact support.

**Solution.** For each integer \(m\), take the segment
\(u\mapsto(m+u/2,u)\), \(0\leq u\leq1\), oriented in the direction of increasing \(u\), and let \(t\) be the negative of their sum. The family is locally finite and consists of subanalytic pieces; hence it gives a sheafified one-chain with closed support in \(\mathbb R\times[0,1]\). Its boundary is the starting endpoint minus the finishing endpoint on every segment, so
\(\partial t=i_{0*}\gamma_0-i_{1*}\gamma_1\).

The support over a compact target interval meets only finitely many segments and is closed in that interval times \([0,1]\). Projection is therefore proper on it. Each segment projects with increasing coordinate orientation, so
\[
 q_*t=-\sum_{m\in\mathbb Z}[(m,m+\tfrac12)],
 \quad
 \partial(q_*t)=\sum_m([m]-[m+\tfrac12])=\gamma_0-\gamma_1.
 \qquad\text{(23)}
\]
The projected closed support is the locally finite union of the intervals \([m,m+\tfrac12]\), which is noncompact. Every equality holds locally with finitely many terms, so no convergence of an infinite scalar sum is required. This proves equality of the two cycle classes in the supported chain complex on that closed set, using properness in the parameter direction rather than compactness of the whole cycle.
