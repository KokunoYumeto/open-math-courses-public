# Orientations of conormal cycles and transverse intersections

A conormal generator and a sheaf characteristic cycle have different coefficients. We calculate both from their supported Thom maps, then compare their intersections with a differential graph. The fibre orientation line makes the calculation valid on a nonorientable base; the tangent dimension distinguishes the normalized generator from the Morse Euler sign.

*Course text, proofs, examples and solutions: CC0 1.0. Human sources retain their own rights.*

Read [Lagrangian cycles and proper cotangent images](lagrangian-cycles-and-proper-cotangent-images.md#the-orientation-coefficient-fixes-the-dimension) for the supported cycle coefficient, and [Pulling back Lagrangian cycles through a graph](pulling-back-lagrangian-cycles-through-a-graph.md#supported-inverse-images-and-fundamental-cycles) for the normalized point, zero section and closed conormal. The [normal-chart proof for conormal pullback](transverse-pullback-of-normalized-conormal-cycles.md#the-coefficient-and-normalization-in-the-normal-chart) fixes the actual Thom units and embedding traces. [Intersections of supported subanalytic cycles](intersections-of-supported-subanalytic-cycles.md#the-actual-cup-product-retains-both-supports) supplies the ordered supported cup and point trace. [Continuous sections and supported cycle intersections](continuous-sections-and-supported-cycle-intersections.md#a-continuous-section-supplies-a-supported-unit) supplies the section unit and its coefficient map. The coefficient maps in these prerequisites fix the signs used below.

The index applications use [Differential sections and proper-below Euler indices](differential-sections-and-proper-below-euler-indices.md), including its full-support compactness and ordinary-versus-compact conventions. This lesson gives the coordinate realization of those maps; it does not replace their finiteness proofs.

## Cotangent orientation and the relative sign line

Let \(A\) be a commutative coefficient ring of finite global dimension. Let \(X\) be a real analytic \(n\)-manifold, Hausdorff and countable at infinity, with uniformly bounded finite dimension. Put

\[
 M=T^*X,\qquad \pi:M\longrightarrow X,\qquad
 B=\operatorname{or}_{M/X},\qquad
 P=\pi^!A_X,\qquad E=\pi^{-1}\omega_X.
 \qquad\text{(1)}
\]

The sign line \(B\) is the orientation of a cotangent fibre. An integral orientation generator has canonical square one; extend this pairing to \(A\).
For coordinates \(x=(x_1,\ldots,x_n)\), use the dual fibre coordinates \(\xi\), and abbreviate

\[
 dx=dx_1\wedge\cdots\wedge dx_n,\qquad
 d\xi=d\xi_1\wedge\cdots\wedge d\xi_n,\qquad
 \Omega=d\xi\wedge dx.
 \qquad\text{(2)}
\]

The dual-frame identification sends \(\operatorname{sgn}(d\xi)\) in \(B\) to \(\operatorname{sgn}(dx)\) in \(\pi^{-1}\operatorname{or}_X\). This identification is canonical.

**Proof.** If \(x'=f(x)\) has Jacobian \(J\), then the fibre transformation is \(\xi'=J^{-t}\xi\). Its vertical determinant has sign \(\operatorname{sgn}\det J\), the same as the determinant of the base transformation. Hence the two orientation generators change by the same sign.

The full cotangent Jacobian is block triangular with determinants \(\det J\) and \((\det J)^{-1}\). Its determinant is positive, including for an orientation-reversing base chart. Thus \(\operatorname{sgn}\Omega\) is a global orientation of \(M\). In the wedge in (2), the base terms in \(d\xi'\) vanish against the full \(dx'\); the two determinant factors cancel. \(\square\)

This global orientation has a specific relation to the symplectic orientation. With \(\alpha=\sum_i\xi_i\,dx_i\) and \(\omega=d\alpha\),

\[
 \frac{\omega^n}{n!}
  =\bigwedge_{i=1}^n(d\xi_i\wedge dx_i)
  =(-1)^{n(n-1)/2}\Omega.
 \qquad\text{(3)}
\]

Moving \(dx_i\) past the later \(d\xi_j\) gives \(n(n-1)/2\) exchanges. We use \(\Omega\) for the ordered intersection convention. Replacing it by the symplectic orientation without (3) would change the answer in some dimensions.

The actual relative dualizing comparison gives

\[
 \omega_M\simeq B[n]\otimes_A E,\qquad
 E\simeq\omega_M\otimes_A B[-n].
 \qquad\text{(4)}
\]

The shifted inverse pairing in the second map of (4) moves \(B[-n]\) past \(E\), whose orientation generator has degree \(-n\), before evaluating the adjacent inverse fibre factors. Its graded symmetry contributes \((-1)^{n^2}=(-1)^n\). This is the ordered cancellation fixed in the first prerequisite. For a smooth \(n\)-dimensional carrier \(Z\), the resulting supported degree-zero \(E\)-coefficient is represented by

\[
 \operatorname{or}_Z\otimes_A B|_Z.
 \qquad\text{(5)}
\]

This is the earlier cycle comparison, not an independent choice of a generator. A local expression for an orientation-valued cycle is a tangent orientation tensored with a fibre sign generator.

## The normal-first Thom dictionary

Here is the local dictionary for (5). Trivialize \(B\) by \(b=\operatorname{sgn}(d\xi)\), and identify it with the base generator \(o=\operatorname{sgn}(dx)\). Let \(Z\) be smooth of dimension \(n\) in \(M\). Choose a nonzero normal \(n\)-form \(\nu\) and a tangent \(n\)-form \(\theta\), with the normal variables placed first. If

\[
 \operatorname{sgn}(\nu\wedge\theta)=\operatorname{sgn}\Omega,
 \qquad\text{(6)}
\]

then the positive normal Thom class with coefficient \(o\) corresponds to the cycle coefficient \((-1)^n\operatorname{sgn}(\theta|_Z)\otimes b\).

**Proof.** In product coordinates \((r,z)\) with \(Z=\{r=0\}\), the closed embedding costalk has normal coefficient \(\operatorname{or}_r[-n]\). Its pairing with the ambient dualizing coefficient uses normal-then-tangent order and leaves \(\operatorname{or}_Z[n]\); the positive normal point trace has value one. To apply this to \(E\), first use its specified comparison with \(\omega_M\otimes B[-n]\) in (4). The crossing of the inverse fibre line and the base dualizing line contributes \((-1)^n\), so the normal-first orientation rule (6) must retain that factor. A frame reversal changes the paired orientation generators together, and the shifted cancellation depends only on the dimension. Consequently this dictionary gives the actual comparison on every chart and glues. \(\square\)

The forms in this dictionary record orientations, not differential-form representatives for sheaf cohomology. The supported classes are the Thom classes defined by the embedding counit.

## The normalized conormal retains the tangent zero-section sign

Let \(i:Y\hookrightarrow X\) be a closed analytic submanifold of codimension \(c\), with \(\ell=n-c\). Locally choose normal coordinates first:

\[
 x=(u,t),\qquad u\in\mathbb R^c,\quad t\in\mathbb R^\ell,
 \qquad Y=\{u=0\},\qquad \xi=(\zeta,\tau).
 \qquad\text{(7)}
\]

The conormal carrier is

\[
 \Lambda=T_Y^*X=\{u=0,\ \tau=0\}.
 \qquad\text{(8)}
\]

Its parameter order will be \((\zeta,t)\). The normalized cycle
\([T_Y^*X]=i_*[T_Y^*Y]\) is

\[
 [T_Y^*X]
 \quad\longleftrightarrow\quad
 \operatorname{sgn}(d\zeta\wedge dt)
       \otimes\operatorname{sgn}(d\zeta\wedge d\tau).
 \qquad\text{(9)}
\]

**Proof of the normalization.** The [normal-chart calculation](transverse-pullback-of-normalized-conormal-cycles.md#the-coefficient-and-normalization-in-the-normal-chart) specifies the morphism defining \(i_*[T_Y^*Y]\). The normalized tangent zero cycle is \((-1)^\ell\) times the positive zero-point Thom unit in the \(\tau\) variables. This scalar comes from the graph inverse coefficient for \(Y\to\mathrm{pt}\): its comparison with the geometric fibre trace is \((-1)^\ell\), as proved by the negative-Fourier-cut calculation in the [relative coefficient theorem](transverse-pullback-of-normalized-conormal-cycles.md#the-graph-coefficient-and-the-relative-fibre-trace). The closed embedding then supplies the positive normal trace in the \(u\) variables, preserving that tangent scalar.

Keep the tangent-first product order temporarily. The normal cochain orientation is \(d\tau\wedge du\), and the base coefficient orientation is \(dt\wedge du\). Changing both to the normal-first base order in (7) contributes \((-1)^{c\ell}\) twice. Thus the normalized supported class is \((-1)^\ell\) times the positive normal Thom class in \((u,\tau)\), with coefficient \(\operatorname{sgn}(du\wedge dt)\). The two frame exchanges cancel; the graph scalar remains.

Apply (6). The complete wedge calculation is

\[
 (du\wedge d\tau)\wedge(d\zeta\wedge dt)
   =(-1)^{c^2+2c\ell}
       d\zeta\wedge d\tau\wedge du\wedge dt
   =(-1)^c\Omega.
 \qquad\text{(10)}
\]

The normal-first wedge in (10) contributes \((-1)^c\). The cycle comparison adds \((-1)^n\) by the dictionary above, and the prescribed tangent zero-section scalar is \((-1)^\ell\). Their product is \((-1)^{c+n+\ell}=1\). The remaining fibre coefficient is \(b=\operatorname{sgn}(d\zeta\wedge d\tau)\), proving (9). The graph scalar, normal Thom orientation and shifted cancellation have each been retained before passing to the final coefficient. \(\square\)

At \(c=0\), the normalized zero cycle has the positive base parameter orientation with its fibre coefficient. At \(c=n\), the full point conormal has the positive fibre parameter orientation, with the same fibre coefficient. These are the positive horizontal and vertical generators used in the one-dimensional ray calculation. The positive section unit (12), when written through the same \(E\)-to-cycle comparison, instead has the factor \((-1)^n\) in (13). These endpoint calibrations give graph intersection \((-1)^{n+q}\) and \(+1\), respectively.

**Why the formula is intrinsic.** On \(Y\), the derivative of an adapted coordinate change has the form

\[
 \frac{\partial(u',t')}{\partial(u,t)}
   =\begin{pmatrix}C&0\\ D&T\end{pmatrix},
 \qquad C,T\text{ invertible}.
 \qquad\text{(11)}
\]

The conormal change is \(\zeta'=C^{-t}\zeta\), together with \(t'=t'(t)\). Its parameter Jacobian in \((\zeta,t)\) is block triangular, with determinant sign
\(\operatorname{sgn}\det C\,\operatorname{sgn}\det T\).
The full cotangent-fibre coefficient in (9) changes by this same sign, since the base Jacobian has determinant \(\det C\,\det T\). Their product is positive. The off-diagonal blocks and the \(t\)-dependence of \(C\) do not affect the determinants. Thus (9) glues without choosing an orientation of \(Y\) or \(X\).

## A differential graph retains the coefficient-comparison sign

Let \(\varphi:X\to\mathbb R\) be real analytic, let \(\sigma_\varphi=d\varphi\), and write \(L_\varphi=\sigma_\varphi(X)\). The graph is closed and analytic. Its projection to \(X\) is a diffeomorphism. Symmetry of second derivatives gives \(\sigma_\varphi^*\omega=0\), so it is Lagrangian, although it is generally not conic.

The section class is the unit

\[
 [\sigma_\varphi]\in H^0_{L_\varphi}(M;P)
       \simeq H^0(X;A_X),\qquad [\sigma_\varphi]\longleftrightarrow1.
 \qquad\text{(12)}
\]

To use the same cycle coordinates for both inputs, identify \(P=B[n]\) with \(E=\pi^{-1}\operatorname{or}_X[n]\) by the positive dual-frame map \(b[n]\mapsto o[n]\), and then apply the \(E\)-to-cycle comparison (4). In these coordinates the section coefficient is

\[
 (-1)^n\operatorname{sgn}(\pi|_{L_\varphi}^*dx)
        \otimes\operatorname{sgn}(d\xi).
 \qquad\text{(13)}
\]

**Proof.** In a bundle chart put \(\eta=\xi-d\varphi(x)\). The graph is \(\eta=0\); the fibre translation has determinant one and keeps the relative trace. The equality \(\pi\sigma_\varphi=1_X\) identifies the graph embedding costalk of \(P\) with \(A_X\). Thus (12) is its positive fibre-normal Thom unit. Moreover

\[
 d\eta\wedge dx=d\xi\wedge dx=\Omega,
 \qquad\text{(14)}
\]

because every other term contains an additional base differential. After the positive dual-frame map, this is the positive normal Thom class with coefficient \(o\). The dictionary (6), including its shifted cancellation factor \((-1)^n\), gives (13). Across a chart reversal its tangent and fibre factors change by the same sign, so their tensor glues. \(\square\)

The underlying supported unit exists for every continuous section. In that generality one keeps the supported class and trace; one need not have a subanalytic graph cycle. Formula (13) is the cycle description when the graph is analytic. Neither description asserts that a nonconic graph is a section of the conic cycle sheaf \(\mathcal L_X\).

## Ordered transverse forms give the local number

Take two smooth analytic \(n\)-dimensional submanifolds \(Z_1,Z_2\subset M\), transverse at \(p\). Trivialize the common fibre coefficient by \(b\). The scalar pairing is

\[
 B\otimes_A B\longrightarrow A_M
    \longrightarrow\operatorname{or}_M,\qquad
 b\otimes b\longmapsto1\longmapsto\operatorname{sgn}\Omega.
 \qquad\text{(15)}
\]

It uses the canonical integral square and the specified ambient orientation. Choose \(n\)-forms \(\theta_1,\theta_2\) at \(p\) such that \(\theta_1\) annihilates \(T_pZ_2\), \(\theta_2\) annihilates \(T_pZ_1\), and both restrictions to their own tangent planes are nonzero. If

\[
 \operatorname{sgn}(\theta_1\wedge\theta_2)
          =\operatorname{sgn}\Omega,
 \qquad\text{(16)}
\]

then the cycles with coefficients
\(\operatorname{sgn}(\theta_i|_{Z_i})\otimes b\) have ordered local intersection number \(+1\). Here the sign of a nonzero top form means its integral orientation, subsequently extended to \(A\); it does not impose an order on the coefficient ring.

**Proof from the actual cup.** Transversality permits local defining coordinates for the two submanifolds whose combined derivative is invertible. The inverse function theorem simultaneously makes them complementary coordinate planes. Normalize the chosen forms by positive scalars so \(\theta_1\wedge\theta_2\) represents \(\Omega\). For \(Z_1\), a normal-first Thom orientation is \(\nu_1=(-1)^n\theta_2\), since \(\nu_1\wedge\theta_1\) has ambient orientation. For \(Z_2\), it is \(\nu_2=\theta_1\). Under the same \(E\)-to-cycle comparison, a cycle with either displayed positive tangent coefficient is \((-1)^n\) times its corresponding positive normal Thom class. The two scalar factors cancel in their ordered product.

The remaining ordered product of the normal Thom units has normal orientation

\[
 \nu_1\wedge\nu_2=(-1)^n\theta_2\wedge\theta_1
       =(-1)^{n+n^2}\theta_1\wedge\theta_2
       =\theta_1\wedge\theta_2.
 \qquad\text{(17)}
\]

This is the positive point-supported generator after (15). The normalized point trace sends it to one. Restriction to a smaller coordinate neighborhood and composition of open-extension traces preserve that value. Thus it is the isolated-point number of the supported cup, with its actual support and coefficient maps. \(\square\)

If the sign in (16) is negative, the number is \(-1\). For weights \(a_1,a_2\in A\), multiply by \(a_1a_2\).
Equivalently choose positive parameter frames \(v_1,v_2\) for the two displayed tangent orientations. Then

\[
 \#(Z_1,Z_2)_p
    =a_1a_2\,
      \operatorname{sgn}\det\nolimits_\Omega[v_1\ v_2].
 \qquad\text{(18)}
\]

The columns are ordered first by \(Z_1\), then by \(Z_2\). Exchanging two blocks of \(n\) columns gives

\[
 \#(Z_2,Z_1)_p=(-1)^n\#(Z_1,Z_2)_p.
 \qquad\text{(19)}
\]

This agrees with the earlier codimension cup sign \((-1)^{n^2}\). It is not permissible to exchange the inputs silently in odd base dimension.

For a section and a Lagrangian cycle, we now check that (15) is the pairing induced by the actual map \(P\otimes E\to\omega_M\) after the common cycle-coordinate comparison. This needs a normalization check because the comparison includes shifted lines. Work in a cotangent chart, take the zero-section unit, and take the full point conormal obtained from the positive closed point trace. Their actual cup has trace \(+1\): the section counit restricts the relative fibre dualizing object to its unit, leaving the positive base point trace, whose counit is the identity. In the cycle coordinates already proved, their ordered tangent frames are \((-1)^n dx\) and \(d\xi\); their determinant relative to \(\Omega\) is \((-1)^n(-1)^{n^2}=+1\). These Thom classes generate the two local rank-one support groups. Evaluating their product therefore fixes the scalar of the induced coefficient pairing to one, so it is exactly (15). Restriction and change of chart preserve the same counits and orientation square. Thus no residual shift sign is missing from (15)–(18), and their value is the earlier section-intersection trace.

## Only the restricted Hessian determines the Morse sign

Return to \(Y=\{u=0\}\) and \(\Lambda\) in (7)–(8). A point \(p=d\varphi(x_0)\) lies in \(\Lambda\) precisely when \(x_0\in Y\) and \(d(\varphi|_Y)_{x_0}=0\). Write the Hessian of \(\varphi\) in these adapted coordinates as

\[
 H=\begin{pmatrix}H_{uu}&H_{ut}\\ H_{tu}&H_{tt}\end{pmatrix}.
 \qquad\text{(20)}
\]

Here \(H_{tt}\) is the Hessian of the restricted function at its critical point. Its congruence class is independent of the adapted chart.
The graph and conormal are transverse exactly when \(H_{tt}\) is nonsingular. If \(q\) is the number of its negative eigenvalues, then

\[
 \#\bigl([\sigma_\varphi]\cap[T_Y^*X]\bigr)_p
         =(-1)^\ell\operatorname{sgn}\det H_{tt}=(-1)^{\ell+q}.
 \qquad\text{(21)}
\]

**Proof.** In the row order \((\zeta,\tau,u,t)\) of \(\Omega\), take the graph parameter columns in order \((u,t)\), followed by conormal columns in order \((\zeta,t)\). Their matrix is

\[
 \mathcal M=
 \begin{pmatrix}
  H_{uu}&H_{ut}&I_c&0\\
  H_{tu}&H_{tt}&0&0\\
  I_c&0&0&0\\
  0&I_\ell&0&I_\ell
 \end{pmatrix},
 \qquad \det\mathcal M=(-1)^c\det H_{tt}.
 \qquad\text{(22)}
\]

Expand along the \(u\)-rows with their identity \(u\)-columns. The expansion sign is \((-1)^{cn}\). In the remaining matrix, selecting the \(\zeta\)-identity block exchanges blocks of sizes \(c,\ell\), giving \((-1)^{c\ell}\); the remaining blocks are \(H_{tt}\) and \(I_\ell\). Since \(cn+c\ell=c^2+2c\ell\), this proves the determinant formula. It also proves the transversality criterion; equivalently a common tangent has \(u\)-component zero and \(t\)-component in \(\ker H_{tt}\).

The conormal coefficient in (9) has its positive parameter orientation. The graph coefficient in (13) contributes \((-1)^n\). Multiplication with the determinant sign \((-1)^c\) in (22) gives \((-1)^{n+c}=(-1)^\ell\). The remaining determinant has sign \((-1)^q\), by diagonalizing the nonsingular real symmetric restricted Hessian. This proves (21) with the graph first. \(\square\)

This proof allows arbitrary normal and mixed Hessian blocks. Nonsingularity of the full ambient Hessian is neither necessary nor sufficient for this graph-conormal transversality.

If, near \(x_0\), \(F=i_*L[s]\), where \(L\) is a rank-\(m\) local system on \(Y\) and \(s\in\mathbb Z\), the characteristic-cycle normalization gives

\[
 \operatorname{CC}(F)=(-1)^{\ell+s}m[T_Y^*X],\qquad
 \#\bigl([\sigma_\varphi]\cap\operatorname{CC}(F)\bigr)_p
       =(-1)^{s+q}m.
 \qquad\text{(23)}
\]

For this characteristic-cycle statement take a characteristic-zero field and bounded real-constructible perfect coefficients. The [constant-coefficient normalization](transporting-characteristic-cycles-through-a-graph.md#globally-constant-finite-coefficients-fix-conormal-normalization) gives the first equality after trivializing the local system on a small chart. Multiplying its coefficient by (21) yields \((-1)^{\ell+s}(-1)^{\ell+q}m=(-1)^{s+q}m\), giving the second equality. This calculation is local, so monodromy does not require a global trivialization of \(L\).

The orientation and cup calculations (1)–(22) themselves work over \(A\). To compare the field-valued index with cohomology, take Morse coordinates for \(\varphi|_Y\). For \(q>0\), its negative set in a small Morse ball retracts to \(S^{q-1}\). The support triangle is the fibre of the actual restriction from the ball's constant cochains to the negative set's cochains. This is the negative-space orientation line placed in cohomological degree \(q\); for \(q=1\), it is the fibre of the diagonal \(k\to k^2\), and for \(q=0\) the negative set is empty. The complete [relative-sphere test](pure-test-degrees-and-strong-morse-inequalities.md) identifies the same maps and stalk limit. Tensoring with \(L_{x_0}\) and shifting by \(s\) gives the closed test \(L_{x_0}[s-q]\), tensored with that orientation line. Its Euler sign is \((-1)^{q-s}m=(-1)^{q+s}m\), as in (23).

## The coordinate presentation preserves the index formulas

Keep a characteristic-zero field \(k\), a globally bounded real-constructible \(F\) with perfect stalks, and the full closed support \(D=\operatorname{supp}F=\pi\operatorname{SS}(F)\). The supported comparison just proved retains the order \([\sigma]\), then \(\operatorname{CC}(F)\). Consequently the preceding index theorems take the following coordinate form.

For compact \(D\), every continuous section has the supported intersection number

\[
 \chi(X;F)=\chi_c(X;F)
       =\#\bigl([\sigma]\cap\operatorname{CC}(F)\bigr).
 \qquad\text{(24)}
\]

Use (13) when the graph is analytic; for a general continuous graph use its supported unit. Its intersection over compact \(D\) is compact.

For an analytic \(\varphi:X\to\mathbb R\), assume

\[
 D\cap\{\varphi\leq a\}\text{ compact for every }a\in\mathbb R.
 \qquad\text{(25)}
\]

If \(L_\varphi\cap\operatorname{SS}(F)\) is compact, ordinary cohomology is bounded and finite dimensional, and

\[
 \chi(X;F)=\#\bigl([\sigma_\varphi]\cap\operatorname{CC}(F)\bigr).
 \qquad\text{(26)}
\]

For compact cohomology retain (25), and instead require
\(L_\varphi\cap\operatorname{SS}(F)^a\) compact, where the superscript \(a\) denotes the antipodal image. Then

\[
 \chi_c(X;F)=\#\bigl([\sigma_{-\varphi}]\cap\operatorname{CC}(F)\bigr).
 \qquad\text{(27)}
\]

The sublevel condition stays on \(\varphi\). Full microsupport controls finiteness even when the characteristic cycle has cancellations.

At a strict analytic minimum \(\rho(x_0)=0\), \(d\rho(x_0)=0\), \(\operatorname{Hess}\rho(x_0)>0\), the earlier local isolation and shrinking-restriction proof gives

\[
 \chi(F_{x_0})=\#\bigl([\sigma_\rho]\cap\operatorname{CC}(F)\bigr)_{(x_0;0)},
 \qquad
 \chi(i_{x_0}^!F)=\#\bigl([\sigma_{-\rho}]\cap\operatorname{CC}(F)\bigr)_{(x_0;0)}.
 \qquad\text{(28)}
\]

No transversality at the zero covector is required for (28). In the smooth conormal model, the positive restricted Hessian has \(q=0\) and the negative one has \(q=\ell\). Apply (23), including the sheaf-cycle coefficient, to recover stalk and costalk Euler signs. Applying (21) alone would compute the intersection with the normalized conormal generator.

**Compatibility with the supported index.** The graph presentation was obtained from its actual section unit. The conormal presentation was obtained from its actual zero-point and closed-embedding counits. The transverse convention was obtained from the actual ordered supported cup and point trace. Thus every local coefficient is identified before integration. For a singular or excess intersection one keeps the same supported class; a transverse tangent determinant is not required for its definition. Proper trace, compact support-forgetting and ordinary descent are the same maps proved in the preceding lessons. Applying their finiteness and isolation theorems therefore yields (24)–(28). A coordinate rewrite creates no new properness hypothesis or unrestricted integral on a noncompact support.

## Exercises with complete solutions

### A line conormal in three dimensions

*Difficulty: Introductory.*

Let \(X=\mathbb R^3\), \(Y=\{x_1=x_2=0\}\), and
\(\varphi=x_1+2x_2-x_3^2/2\). Give the normalized conormal coefficient at the intersection, compute the graph-first local number and then reverse the two inputs.

**Solution.** The carrier is \(x_1=x_2=\xi_3=0\), with parameters \((\xi_1,\xi_2,x_3)\). Here \(n=3,c=2,\ell=1\), so its coefficient is
\(\operatorname{sgn}(d\xi_1\wedge d\xi_2\wedge dx_3)\otimes
\operatorname{sgn}(d\xi_1\wedge d\xi_2\wedge d\xi_3)\).
The restricted critical point is \(x_3=0\), and the graph intersection is \(p=(0;1,2,0)\). The restricted Hessian is \((-1)\), so the intersection is transverse. Equation (22) gives raw determinant \(-1\), since \(c\) is even. The conormal parameter coefficient is positive, while (13) gives graph coefficient \((-1)^n=-1\). Their product therefore gives graph-first number \(+1=(-1)^{\ell+q}\). Reversal contributes \((-1)^3=-1\), so the conormal-first number is \(-1\). If the second input were \(\operatorname{CC}(k_Y)=-[T_Y^*X]\), its graph-first number would instead be \(-1\), the degree-one Morse test.

### A chart reversal changes both factors

*Difficulty: Intermediate.*

In coordinates \((u,t;\zeta,\tau)\) on \(T^*\mathbb R^2\), take \(Y=\{u=0\}\). Express (9) after the change \(u'=-u,\ t'=t\). Explain how the coefficient prevents an orientation obstruction on a nonorientable base.

**Solution.** Initially the coefficient is
\(\operatorname{sgn}(d\zeta\wedge dt)\otimes
\operatorname{sgn}(d\zeta\wedge d\tau)\), as in (9).
The dual variables are \(\zeta'=-\zeta,\ \tau'=\tau\). Hence both
\(\operatorname{sgn}(d\zeta'\wedge dt')\) and
\(\operatorname{sgn}(d\zeta'\wedge d\tau')\) are the negatives of their unprimed versions. Their tensor is unchanged. In the Thom calculation the wedge sign \((-1)^c=-1\), tangent zero-section scalar \((-1)^\ell=-1\), and shifted cancellation \((-1)^n=+1\) multiply to the same positive parameter coefficient.

More generally (11) gives equal transition signs on the conormal tangent and fibre coefficient. They cancel on every adapted overlap, so the twisted coefficient glues without a global orientation. Dropping the fibre factor would leave a sign-changing local description on an orientation-reversing overlap.

### The symplectic orientation can give the opposite number

*Difficulty: Intermediate.*

On \(X=\mathbb R^2\), let \(\varphi=x_1x_2\) and intersect \(L_\varphi\) with the normalized zero section. Compute the number with (2), and the number obtained if only the ambient orientation in the scalar pairing is changed to \(\operatorname{sgn}(\omega^2)\).

**Solution.** The Hessian is
\(\begin{pmatrix}0&1\\1&0\end{pmatrix}\), with determinant \(-1\) and one negative eigenvalue. For \(Y=X\), \(c=0\), so the graph-first normalized number is \(-1\). In dimension two, (3) says \(\omega^2/2=-\Omega\). Changing only the ambient orientation in (15) negates the scalar pairing, so the number becomes \(+1\). This altered number does not use the convention of (21). To rewrite the index theorem with that ambient orientation, the corresponding coefficient comparison would have to be changed too.

### Mixed blocks do not repair a degenerate restricted Hessian

*Difficulty: Advanced.*

Let \(X=\mathbb R^4\), with coordinates \((u,t_1,t_2,t_3)\), and \(Y=\{u=0\}\). At a restricted critical point suppose the Hessian is

\[
 H=\begin{pmatrix}
  7&1&2&3\\
  1&-2&0&0\\
  2&0&3&0\\
  3&0&0&5
 \end{pmatrix}.
\]

Compute the raw ordered tangent determinant and the normalized number. Then replace the entry \(-2\) by zero. Is the full ambient Hessian still nonsingular? Are the graph and conormal transverse?

**Solution.** The restricted block has determinant \((-2)\cdot3\cdot5=-30\) and one negative eigenvalue. Since \(c=1\), (22) gives raw determinant \(+30\). The normalized conormal has positive parameter coefficient, and the graph coefficient is \((-1)^n=+1\), so the number is \(+1=(-1)^{\ell+q}\). The sheaf cycle \(\operatorname{CC}(k_Y)=-[T_Y^*X]\) would have index \(-1\).

After the replacement, the restricted block has kernel spanned by the \(t_1\)-vector. The full Hessian has determinant \(-15\): expand along its second row and then the remaining diagonal \(3,5\) block. It is nonsingular. Nevertheless (22) has zero determinant. Explicitly the graph tangent corresponding to \(\delta t_1=1,\delta u=\delta t_2=\delta t_3=0\) has base component \(\delta t_1=1\) and fibre component \(\delta\zeta=1,\delta\tau=0\). This is also a conormal tangent. Thus the intersection is not transverse, and (21) cannot assign a transverse sign by the ambient Hessian.

### Integral signs before reduction modulo two

*Difficulty: Introductory.*

On \(T^*\mathbb R\), intersect an analytic section with the normalized full fibre over a point. Compute both orders over \(\mathbb Z\), and then extend the cycle coefficients to \(\mathbb Z/2\).

**Solution.** In the common cycle coordinates the section orientation is \(-dx\) and the fibre orientation is \(d\xi\), each with coefficient \(\operatorname{sgn}(d\xi)\). Their ordered tangent orientation is \((-dx)\wedge d\xi=d\xi\wedge dx=\Omega\), so the section-first number is \(+1\). The fibre-first number is \(-1\), by (19). Reduction modulo two sends both to \(1\). The equality after reduction does not change the integral normalization from which the two values came. This is a calculation of orientation-valued cycles; it does not enlarge the characteristic-zero hypotheses of the characteristic-cycle construction.

### Ordinary, compact, stalk and costalk signs in one model

*Difficulty: Advanced.*

Let \(Y=\mathbb R\) be a closed coordinate line in \(X=\mathbb R^4\), let
\(F=i_*k_Y^3[2]\), and let \(\rho=|x|^2/2\). Check the two global finiteness conditions and compute the positive and negative graph numbers. Compare them with ordinary and compact cohomology, and with the stalk and ambient point costalk at zero.

**Solution.** Closed support sublevels of \(\rho\) are either empty or closed bounded intervals on \(Y\), hence compact. The full microsupport is \(T_Y^*X\), which is antipodally invariant. Both graphs meet it only at \((0;0)\), so both compactness tests hold. Here \(\ell=1,c=3,s=2,m=3\). The restricted Hessians have indices zero and one. Their intersections with the normalized generator are respectively \(-1\) and \(+1\) by (21). The characteristic cycle is \(-3[T_Y^*X]\), since \((-1)^{\ell+s}m=-3\). Formula (23) therefore gives \(+3\) for \(d\rho\) and \(-3\) for \(-d\rho\).

Ordinary cohomology is \(k^3[2]\), with Euler number \(+3\). Compact cohomology on the line is \(k^3[-1][2]=k^3[1]\), with Euler number \(-3\). The stalk is \(k^3[2]\), while the ambient point costalk is the line costalk shifted by two, namely \(\operatorname{or}_{Y,0}\otimes k^3[1]\). Its Euler number is \(-3\). Thus (26)–(28) give all four values with the same ordered orientation convention, despite the ambient dimension being even.

## References and further reading

M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §2.2, printed p. 197, constructs the orientation-valued conormal generator. In the normal-first coordinates used above, that convention has coefficient \((-1)^c\). The programme generator (9), expressed through its fixed ordered cycle comparison, has positive parameter coefficient and is therefore \((-1)^c\) times that historical generator. Its calculation retains both the tangent zero-section scalar \((-1)^\ell\) and the shifted cancellation \((-1)^n\), with \(\ell=n-c\). Formula (23) supplies the corresponding sheaf coefficient; its product with (21) is the Morse sign \((-1)^{s+q}\).

W. Schmid and K. Vilonen, [*Characteristic cycles of constructible sheaves*](https://people.math.harvard.edu/~schmid/articles/cycles.dvi), author version of the article published in *Inventiones Mathematicae* 124 (1996), 451–502, §2, give an oriented-base formulation. Comparing that formulation with (9) requires keeping both the tangent orientation and the fibre sign line; choosing only the base orientation does not determine the comparison.

For intersection classes in families, R. Fernandes, K. Kudomi and K. Takeuchi, [*Characteristic cycles of real and complex constructible sheaves, revisited*](https://arxiv.org/abs/2603.14821v2), arXiv 2603.14821v2, 10 July 2026, §2.3, formulate the supported cup product and the proper trace over a parameter interval. Their family and limiting-cycle hypotheses are additional to the pointwise calculation above. The normal-first wedge, transition signs and full mixed-block determinant in this lesson give the local orientation comparison used in (21)–(23).
