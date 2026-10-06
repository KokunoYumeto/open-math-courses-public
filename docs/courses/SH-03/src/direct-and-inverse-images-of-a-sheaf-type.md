# Direct and inverse images of a sheaf type

For a smooth map of manifolds, a selected covector has two associated cotangent points. The direction on the source controls a microlocal direct image; the direction on the target controls an inverse image. When the relevant cotangent map is transverse to the input Lagrangian, the output is a bounded germ with a smooth Lagrangian microsupport bound. Its coefficient type can then be calculated by the graph kernel.

Use The type and shift of a transverse kernel composition for the graph-kernel degree formula. The formal operations, their representation and their relative dualizing comparison use the exact programme proofs linked below. Those arguments retain their stated geometric and sheaf-operation prerequisites. Coefficients are arbitrary bounded complexes over a commutative finite-global-dimension ring \(k\). Manifolds are smooth, finite dimensional, real, Hausdorff and second countable.

*Written by GPT-6.1 Sol (OpenAI), Ultra; revised by GPT-6 Astra (OpenAI), Ultra, 6 October 2026. Self-checked by the writing AI. Original programme text is public domain (CC0).*

## Two cotangent maps with different fibres

Let \(f:Y\to X\) be a smooth map, and write

\[
P=Y\times_X T^*X,\qquad
f_\pi(y;\xi)=(f(y);\xi),\qquad
f_d(y;\xi)=(y;d f_y^t\xi).
\qquad\text{(1)}
\]

Fix \(p\in P\), with \(p_X=f_\pi(p)\) and \(p_Y=f_d(p)\). No nonzero-covector assumption is added. The differentials of these maps are understood at \(p\) whenever tangent Lagrangian planes are propagated below.

For direct image assume \(\operatorname{SS}(G)\subset\Lambda_Y\) near \(p_Y\), where \(\Lambda_Y\) is a smooth conic Lagrangian germ through \(p_Y\), and require \(f_d\) transverse to \(\Lambda_Y\). The incidence

\[
I_Y=f_d^{-1}\Lambda_Y
\qquad\text{(2)}
\]

is then smooth of dimension \(\dim X\). After shrinking near \(p\), its image under \(f_\pi\) is a locally embedded Lagrangian \(\Lambda_X\).

For inverse image instead assume \(\operatorname{SS}(F)\subset\Lambda_X\) near \(p_X\), where \(\Lambda_X\) is a smooth conic Lagrangian germ through \(p_X\), and require \(f_\pi\) transverse to \(\Lambda_X\). The incidence

\[
I_X=f_\pi^{-1}\Lambda_X
\qquad\text{(3)}
\]

has dimension \(\dim Y\), and \(f_d\) identifies a small neighborhood in it with a locally embedded Lagrangian \(\Lambda_Y\).

These assertions include local injectivity, not a global injectivity claim. To verify them, identify \(P\) with the conormal of the graph of \(f\), using its twisted kernel convention. For (2) compose that Lagrangian relation with \(\Lambda_Y\), considered as a kernel to a point. For (3) use the transposed graph and compose with \(\Lambda_X\). The middle transversality is exactly the respective assumption above. The tangent argument for transverse composition gives the stated dimensions, zero kernel of the output differential, and a Lagrangian image. Its constant-rank conclusion gives the local embedding. The smooth incidence thus contains only the selected point over the fixed output covector after shrinking.

## Formal images and their canonical comparisons

At the selected lift the proper-support microlocal direct image is represented by

\[
f_{!,p}^\mu G
\simeq\text{“}\!\lim_{U\ni y_0}\!\text{”}\, Rf_!(G_U)
\quad\text{in }D^b(k_X;p_X),
\qquad y_0=\pi_Y(p_Y).
\qquad\text{(4)}
\]

The direct-image germ-neighborhood proof identifies this system with the formal operation indexed by all incoming denominators. Its local isolated incidence, supplied by (2), satisfies the isolated direct-image representation theorem, so it is represented by an ordinary bounded object. That theorem identifies the ordinary microlocal direct image with it by the **canonical** proper-to-ordinary comparison. It also confines its microsupport witnesses to an arbitrarily small neighborhood of \(p\), giving the bound by \(\Lambda_X\).

For (3), the represented ordinary and exceptional microlocal inverse images are

\[
\begin{split}
f_{\mu,p}^{-1}F
 &=\text{“}\!\lim_{F'\to F}\!\text{”}\,f^{-1}F',\\
f_{\mu,p}^{!}F
 &=\text{“}\!\operatorname{colim}_{F\to F'}\!\text{”}\,f^!F',\\
\omega_{Y/X}\otimes^L f_{\mu,p}^{-1}F
 &\xrightarrow{\sim} f_{\mu,p}^{!}F.
\end{split}
\qquad\text{(5)}
\]

All indexing arrows are isomorphisms at \(p_X\), with the two opposite variances shown. The formal-operation definitions and comparison maps fix those variances and the particular arrow in (5). The isolated inverse-image representation theorem applies because (3) isolates the lift over \(p_Y\). It represents both formal objects, identifies the displayed canonical comparison and confines their microsupport to \(\Lambda_Y\). Locally \(\omega_{Y/X}=\operatorname{or}_{Y/X}[\dim Y-\dim X]\); the relative orientation line is retained before any trivialization.

Quotation marks in (4)–(5) denote formal pro or ind objects. They do not denote an ordinary inverse or direct limit of sheaves. The representation theorem concerns their morphisms against test objects. Likewise these represented germs need not be the ordinary global images of the original representative. That stronger statement requires the separate full-fibre and support/noncharacteristic hypotheses of the representation theorem.

## The direct-image formula uses a plane in the source cotangent space

Suppose \(G\) has coefficient type \(L\) with shift \(d\) along \(\Lambda_Y\) at \(p_Y\). Put \(A_Y=T_{p_Y}\Lambda_Y\), and propagate the target vertical through the graph correspondence into \(E_Y=T_{p_Y}T^*Y\):

\[
B_Y=(d f_d)\bigl((d f_\pi)^{-1}V_X\bigr),
\qquad
r_Y=\tau_{E_Y}(V_Y,A_Y,B_Y).
\qquad\text{(6)}
\]

Linear Lagrangian relation composition makes \(B_Y\) Lagrangian. Then the represented direct image (4) has type \(L\) and normalized shift

\[
d_{\mathrm{dir}}
=d-\frac12\bigl[\dim Y-\dim X+r_Y\bigr].
\qquad\text{(7)}
\]

**Proof.** Let \(\Gamma_f\subset X\times Y\) be the graph. Its codimension is \(\dim X\), so \(k_{\Gamma_f}\) is simple with normalized shift \(\dim X/2\). Ordinary convolution with this kernel is \(Rf_!\). The selected formal convolution agrees with (4): use the closed-graph projection formula for ordinary representatives, then the isolated-image comparison on the joint denominator and neighborhood system. A denominator cone at the selected graph point or at \(p_Y\) has no retained incidence after common refinements. This identifies their output-germ morphism colimits; it does not assert pre-image cofinality of base restrictions among arbitrary denominators.

The graph's twisted middle map is \(f_d\). Its transversality to \(\Lambda_Y\) is precisely the hypothesis for general kernel composition. The first propagated plane is \(B_Y\), and the second is \(A_Y\), because the last manifold is a point. The general relation index is consequently the ordered source-space index (6). Substitution into the composition theorem gives
\(\dim X/2+d-(\dim Y+r_Y)/2\), which is (7), with coefficient \(k\otimes^L L=L\). The represented output has exactly the Lagrangian bound already established in (2). \(\square\)

The location of the three planes in (6) matters. An index in the other cotangent space cannot be substituted without an additional proved identity. The fold calculation below checks this point, including the sign and shift parity.

## Ordinary inverse image preserves the normalized shift

Under the inverse-image assumptions, if \(F\) has type \(L\) with shift \(d\), then

\[
f_{\mu,p}^{-1}F\text{ has type }L\text{ with shift }d.
\qquad\text{(8)}
\]

**Proof.** Use \(\Gamma_f\subset Y\times X\) as the transposed graph kernel. Its codimension is again \(\dim X\), so its normalized shift is \(\dim X/2\). Its ordinary transform is \(f^{-1}\): the projection of the graph onto \(Y\) is an isomorphism, and restricting the second factor to \(x=f(y)\) gives the ordinary pullback. The incoming denominator system and the isolated inverse-image comparison identify its represented microlocal transform with the first object of (5).

Its middle space is now \(E_X\). Propagating \(V_Y\) backward through the graph gives **all** of \(V_X\): a vertical source variation has zero base variation \(\delta y\), while its lift \(\delta\xi\) can be any target vertical covector. The first propagated middle plane is therefore \(V_X\); the second is \(T_{p_X}\Lambda_X\). The relation index is \(\tau(V_X,T_{p_X}\Lambda_X,V_X)=0\). The degree formula gives
\(\dim X/2+d-\dim X/2=d\), proving (8). \(\square\)

By (5), the exceptional inverse has coefficient type
\(L\otimes_k\operatorname{or}_{Y/X,y_0}\) and normalized shift
\(d+\dim Y-\dim X\). Locally the orientation line can be trivialized to name the type as \(L\), but (5) retains its actual canonical line and map. Ordinary and exceptional inverse images therefore have different degree normalizations when the relative dimension is nonzero.

## A fold checks the direct degree and the index space

Take \(f:\mathbb R_y\to\mathbb R_x\), \(f(y)=y^2\), and \(G=k_{\mathbb R}\), with \(k\ne0\). Select \(p=(0;\xi\,dx)\) with \(\xi\ne0\). Its source covector \(p_Y\) is zero; \(G\) has type \(k\), shift zero, along the zero section.

The cotangent maps and their derivatives at this lift are

\[
\begin{split}
f_\pi(y;\xi)&=(y^2;\xi),&
d f_\pi(a,b)&=(0,b),\\
f_d(y;\xi)&=(y;2y\xi),&
d f_d(a,b)&=(a,2\xi a).
\end{split}
\qquad\text{(9)}
\]

The latter image is transverse to the zero-section tangent since \(\xi\ne0\). Its inverse incidence is \(y=0\), whose image is the conormal to \(\{0\}\) in \(X\). In (6), \((d f_\pi)^{-1}V_X\) is the full lift tangent, so \(B_Y\) is the graph line \(\eta=2\xi y\).

With the convention \(\omega=d\eta\wedge dy\), the ordered index of vertical, horizontal, and this graph is

\[
r_Y=\tau(V_Y,T_Y^*Y,B_Y)=-\operatorname{sign}\xi.
\qquad\text{(10)}
\]

For an explicit sign check, write the three vectors as \((0,u),(v,0),(w,aw)\), with \(a=2\xi\). Their index quadratic form is
\(u(v-w)-avw\). Set \(z=v-w\); it becomes
\(z(u-aw)-aw^2\), a hyperbolic pair of signature zero plus \(-aw^2\). This proves (10) without choosing another sign convention.

The relative dimension is zero. Formula (7) therefore gives shift \(1/2\) at \(+dx\) and \(-1/2\) at \(-dx\), both with type \(k\).

The map \(y\mapsto y^2\) is proper, and the entire incidence over each fixed nonzero \((0;\xi)\) consists of the single lift \(y=0\). Thus the original ordinary direct image represents the microlocal image by the full proper isolated-incidence prerequisite. Proper base change gives its stalks: zero for \(x<0\), \(k\) at zero, and \(k\oplus k\) for \(x>0\). The generization to the two positive branches is the diagonal \(k\to k\oplus k\).

## A diagram of the fold and its two tests

![The fold and its direct-image stalks](figures/fold-direct-image.svg)

*The curve is drawn from 401 samples of \(x=y^2\); the marked points \((y,x)=(\pm1/2,1/4)\) and \((0,0)\) are exact. The right-hand diagram records the actual direct-image stalks and diagonal generization. The two covector tests at zero have coefficient complexes \(k\) and \(k[-1]\), respectively. This is the fold calculation (9)–(11), not a global claim that either single half-line coefficient represents the full direct image.*

The two support triangles compute the raw tests directly:

\[
C_x(Rf_*k_{\mathbb R})=k,
\qquad
C_{-x}(Rf_*k_{\mathbb R})
=\operatorname{Cone}(k\xrightarrow{\mathrm{diag}}k\oplus k)[-1]
\simeq k[-1].
\qquad\text{(11)}
\]

The output Lagrangian is a point conormal. Its tangent is vertical and each graph test has index zero, so the normalized exponent is \(-d+1/2\). The two degrees just computed give exactly the two shifts above. They also show why a shift zero would be incorrect: it has the wrong half-intersection parity.

The fold also checks which cotangent space carries the ordered index. Propagating the source vertical into the target gives \((d f_\pi)(d f_d)^{-1}V_Y=V_X\) in this example, and the output conormal tangent is vertical too. An index formed from those repeated target planes is zero, whereas the support tests in (11) require the two half-integer shifts. Formula (6) retains the source-space planes used in the graph-composition proof of (7).

## Exercises with complete solutions

### A closed embedding gains half its codimension on direct image

*Difficulty: Introductory.*

Let \(i:Y\hookrightarrow X\) be a closed embedding of codimension \(c\), and take a constant coefficient \(L_Y\), with type \(L\), shift zero along the zero section. Compute its represented direct-image degree at a selected conormal. Check the plane \(B_Y\).

**Solution.** Since \(di\) is injective, \(f_\pi\)'s base differential can be vertical only if \(\delta y=0\). The transpose \(di^t\) is surjective on covectors, so \(B_Y=V_Y\). The ordered index \(\tau(V_Y,T_Y^*Y,V_Y)\) is zero. The relative dimension is \(-c\); (7) gives \(c/2\), exactly the normalized degree of \(L_Y\) extended by zero to its codimension-\(c\) support in \(X\). The cotangent transversality also holds, because \(f_d\) is a submersion along this graph correspondence.

### A section of a projection has zero direct degree

*Difficulty: Intermediate.*

For \(f:\mathbb R^m\times X\to X\), take \(G=L_{\{0\}\times X}\). At the zero selected covectors, compute its input degree, the direct-image index and its output degree.

**Solution.** The input support has codimension \(m\), hence degree \(m/2\). In the source tangent space the conormal tangent is vertical in the \(\mathbb R^m\) factor and horizontal in \(X\), while \(B_Y\) is horizontal in the first factor and vertical in \(X\). Against the full vertical plane, the index splits into triples with repeated planes in both factors and is zero. The relative dimension is \(m\), so (7) gives degree zero. The restriction of \(f\) to the support is an isomorphism, giving the coefficient \(L_X\) directly. This case satisfies the isolated incidence and checks the zero-covector normalization.

### Ordinary and exceptional inverse images of a constant

*Difficulty: Intermediate.*

For a codimension-\(c\) embedding, let \(F=k_X\), shift zero along the zero section. Identify the two inverse coefficient types and shifts under the transverse hypotheses.

**Solution.** The ordinary inverse is \(k_Y\), type \(k\) with shift zero by (8). The exceptional inverse is the relative orientation line shifted by \([-c]\), so its intrinsic coefficient type is \(\operatorname{or}_{Y/X,y_0}\) with normalized shift \(-c\). A local orientation identifies that type with \(k\); the canonical comparison (5) retains the orientation line. The opposite denominator directions in (5) do not add a second degree shift.

### Compute the negative fold test from its gluing map

*Difficulty: Advanced.*

At zero for \(f(y)=y^2\), derive the second complex in (11) from the support triangle. Describe a quotient identifying its coefficient with \(k\).

**Solution.** For the closed support \(x\le0\), its complement is \(x>0\). The direct-image stalk at zero is \(k\), while the nearby-complement section complex is \(k\oplus k\) in degree zero; the actual map is diagonal. Thus the support triangle gives \(\operatorname{Cone}(\mathrm{diag})[-1]\). The diagonal is injective, and \((a,b)\mapsto b-a\) identifies its cokernel with \(k\). The support complex is therefore \(k[-1]\). At the negative covector the point conormal has zero test index, and the normalized exponent for degree \(-1/2\) is one, giving type \(k\).

### Why a local lift does not determine a whole global direct image

*Difficulty: Advanced.*

Suppose the local transverse direct-image hypotheses hold at one \(p\), but another source point has a cotangent incidence over the same \(p_X\). Can one replace (4) by the original global \(Rf_!G\) solely from local transversality?

**Solution.** No. Local transversality identifies one embedded incidence branch and gives its represented microlocal germ. The original global image can also receive the other branch, and boundary or nonproper support can add further contributions. Identifying the original global representative requires the theorem's entire-fibre incidence condition and proper support. The local formula (4) instead confines neighborhoods around the chosen source base point and uses boundary-controlled comparisons. It retains the selected branch without asserting that other global contributions vanish.

## References

The direct- and inverse-image degree formulas above apply the programme’s transverse kernel-composition theorem to the graph kernel. Its ordered middle-plane convention gives (6), and its coefficient and degree formula gives (7)–(8). That theorem retains its explicit geometric and sheaf-operation prerequisites.

The exact formal providers are isolated inverse-image representation, direct-image germ neighborhoods, and isolated direct-image representation. They specify the canonical maps and distinguish local representation from identification with an original global image. The common comparison-map construction fixes the relative orientation complex and the direction of each arrow. These written arguments retain their own lower foundational dependencies.

For context on pure sheaves and their relation to perversity, see M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*, Astérisque 128 (1985), §9.5, pp.170–172](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf). The source passage discusses microlocal purity through the regular Riemann–Hilbert correspondence. The graph-kernel and representation arguments identified above supply this lesson’s formulas.
