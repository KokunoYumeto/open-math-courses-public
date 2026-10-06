# Orientations of conormal cycles and transverse intersections

A normalized conormal cycle is an orientation-valued cycle. Its cotangent-fibre coefficient lets the local descriptions agree across charts that reverse orientation. Keeping that coefficient also explains why the ordered intersection with a differential graph is the sign of the Hessian on the submanifold.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 2 October 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

Read Lagrangian cycles and proper cotangent images for the supported cycle coefficient, and Pulling back Lagrangian cycles through a graph for the normalized point, zero section and closed conormal. The normal-chart proof for conormal pullback fixes the actual Thom units and embedding traces. Intersections of supported subanalytic cycles supplies the ordered supported cup and point trace. Continuous sections and supported cycle intersections supplies the section unit and its coefficient map. Their exact written prerequisites retain their stated lower and transitive obligations.

The index applications use Differential sections and proper-below Euler indices, including its full-support compactness and ordinary-versus-compact conventions. This lesson gives the coordinate realization of those maps; it does not replace their finiteness proofs.

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

The shifted inverse pairings in (4) are those fixed by the relative trace. For a smooth \(n\)-dimensional carrier \(Z\), its supported degree-zero \(E\)-coefficient is therefore represented by

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

then the positive normal Thom class with coefficient \(o\) corresponds to the cycle coefficient \(\operatorname{sgn}(\theta|_Z)\otimes b\).

**Proof.** In product coordinates \((r,z)\) with \(Z=\{r=0\}\), the closed embedding costalk has normal coefficient \(\operatorname{or}_r[-n]\). Its ordered pairing with the ambient dualizing coefficient cancels the normal factor, leaving \(\operatorname{or}_Z[n]\). The normal point trace sends its positive generator to one. Under the cycle comparison (4), this is precisely the normal-first rule (6), with the remaining coefficient \(b\). This is the coordinate Thom and trace calculation already used in the normal-chart conormal proof. A positive change of either frame preserves the generators; a negative change reverses both sides of the corresponding orientation pairing. Thus the rule determines the actual local comparison and glues. \(\square\)

The forms in this dictionary record orientations, not differential-form representatives for sheaf cohomology. The supported classes are the Thom classes defined by the embedding counit.

## The normalized conormal keeps a codimension sign

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
 (-1)^c\operatorname{sgn}(d\zeta\wedge dt)
       \otimes\operatorname{sgn}(d\zeta\wedge d\tau).
 \qquad\text{(9)}
\]

**Proof of the normalization.** The preceding normal-chart proof describes the actual morphism defining \(i_*[T_Y^*Y]\). The tangent zero section contributes the zero-point Thom unit in the \(\tau\) variables. The embedding contributes the positive normal trace in the \(u\) variables. In the tangent-first product order, their normal cochain orientation is \(d\tau\wedge du\), and their base coefficient orientation is \(dt\wedge du\).

Convert both to the normal-first base order in (7). Exchanging the two blocks of the normal cochain contributes \((-1)^{c\ell}\), and exchanging the two blocks of the base coefficient contributes the same sign. Their product is one. Thus the normalized supported class is the positive normal Thom class in \((u,\tau)\), with coefficient \(\operatorname{sgn}(du\wedge dt)\).

Apply (6). The complete wedge calculation is

\[
 (du\wedge d\tau)\wedge(d\zeta\wedge dt)
   =(-1)^{c^2+2c\ell}
       d\zeta\wedge d\tau\wedge du\wedge dt
   =(-1)^c\Omega.
 \qquad\text{(10)}
\]

Hence the required tangent orientation is \((-1)^c\operatorname{sgn}(d\zeta\wedge dt)\). The remaining fibre coefficient is \(b=\operatorname{sgn}(d\zeta\wedge d\tau)\), proving (9). The zero-point and embedding maps used here are the normalized counits; no scalar rescaling has been introduced. \(\square\)

The endpoints are useful checks. For \(c=0\), (9) is the base-oriented zero section, tensored with the fibre orientation. For \(c=n\), it is the full point conormal with tangent orientation \((-1)^n\operatorname{sgn}(d\xi)\), still tensored with \(\operatorname{sgn}(d\xi)\).

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

## A differential graph has the base orientation

Let \(\varphi:X\to\mathbb R\) be real analytic, let \(\sigma_\varphi=d\varphi\), and write \(L_\varphi=\sigma_\varphi(X)\). The graph is closed and analytic. Its projection to \(X\) is a diffeomorphism. Symmetry of second derivatives gives \(\sigma_\varphi^*\omega=0\), so it is Lagrangian, although it is generally not conic.

The section class is the unit

\[
 [\sigma_\varphi]\in H^0_{L_\varphi}(M;P)
       \simeq H^0(X;A_X),\qquad [\sigma_\varphi]\longleftrightarrow1.
 \qquad\text{(12)}
\]

Use the dual-frame and \(\Omega\) comparisons above to write it as an orientation-valued \(n\)-cycle. Its coefficient is

\[
 \operatorname{sgn}(\pi|_{L_\varphi}^*dx)
        \otimes\operatorname{sgn}(d\xi).
 \qquad\text{(13)}
\]

**Proof.** In a bundle chart put \(\eta=\xi-d\varphi(x)\). The graph is \(\eta=0\); the fibre translation has determinant one and keeps the relative trace. The equality \(\pi\sigma_\varphi=1_X\) identifies the graph embedding costalk of \(P\) with \(A_X\). Thus (12) is its positive fibre-normal Thom unit. Moreover

\[
 d\eta\wedge dx=d\xi\wedge dx=\Omega,
 \qquad\text{(14)}
\]

because every other term contains an additional base differential. The dictionary (6) gives (13). Across a chart reversal its tangent and fibre factors change by the same sign, so their tensor glues. \(\square\)

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
\(\operatorname{sgn}(\theta_i|_{Z_i})\otimes b\) have ordered local intersection number \(+1\).

**Proof from the actual cup.** Transversality permits local defining coordinates for the two submanifolds whose combined derivative is invertible. The inverse function theorem simultaneously makes them complementary coordinate planes. Normalize the chosen forms by positive scalars so \(\theta_1\wedge\theta_2\) represents \(\Omega\). For \(Z_1\), a normal-first Thom orientation is \(\nu_1=(-1)^n\theta_2\), since \(\nu_1\wedge\theta_1\) has ambient orientation. For \(Z_2\), it is \(\nu_2=\theta_1\).

The ordered supported cup is the product of these normal Thom units. Its normal orientation is

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

For a section and a Lagrangian cycle, the cup in (15)–(18) is the orientation-valued form of the actual coefficient map \(P\otimes E\to\omega_M\). Indeed its first normal Thom unit is the unit in (12); its second is the cycle comparison (4); and (6) identifies their ordered evaluation with the two normal generators used in (17). The fibre square becomes the same \(\Omega\) coefficient in (15). Thus this coordinate convention computes the earlier section-intersection trace.

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
         =\operatorname{sgn}\det H_{tt}=(-1)^q.
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

The conormal orientation in (9) contributes \((-1)^c\), while the graph has its parameter orientation by (13). Formula (18) therefore cancels the two codimension signs and gives \(\operatorname{sgn}\det H_{tt}\). Diagonalization of the real symmetric nonsingular restricted Hessian gives \((-1)^q\). \(\square\)

This proof allows arbitrary normal and mixed Hessian blocks. Nonsingularity of the full ambient Hessian is neither necessary nor sufficient for this graph-conormal transversality.

If, near \(x_0\), \(F=i_*L[s]\), where \(L\) is a rank-\(m\) local system on \(Y\) and \(s\in\mathbb Z\), the characteristic-cycle normalization gives

\[
 \operatorname{CC}(F)=(-1)^s m[T_Y^*X],\qquad
 \#\bigl([\sigma_\varphi]\cap\operatorname{CC}(F)\bigr)_p
       =(-1)^{s+q}m.
 \qquad\text{(23)}
\]

For this characteristic-cycle statement take the existing cycle-theory hypotheses: a characteristic-zero field and bounded real-constructible perfect coefficients. The orientation and cup calculations (1)–(22) themselves work over \(A\). Locally the closed Morse test is \(L_{x_0}[s-q]\), with its possible orientation line; its Euler sign is the same as (23).

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

No transversality at the zero covector is required for (28). In the smooth conormal model, (21) checks the signs directly: the positive restricted Hessian has \(q=0\); the negative one has \(q=\ell\).

**Why no formulas have changed.** The graph presentation was obtained from its actual section unit. The conormal presentation was obtained from its actual zero-point and closed-embedding counits. The transverse convention was obtained from the actual ordered supported cup and point trace. Thus every local coefficient is identified before integration. For a singular or excess intersection one keeps the same supported class; a transverse tangent determinant is not required for its definition. Proper trace, compact support-forgetting and ordinary descent are the same maps proved in the preceding lessons. Applying their finiteness and isolation theorems therefore yields (24)–(28). A coordinate rewrite creates no new properness hypothesis or unrestricted integral on a noncompact support.

## Exercises with complete solutions

### A line conormal in three dimensions

*Difficulty: Introductory.*

Let \(X=\mathbb R^3\), \(Y=\{x_1=x_2=0\}\), and
\(\varphi=x_1+2x_2-x_3^2/2\). Give the normalized conormal coefficient at the intersection, compute the graph-first local number and then reverse the two inputs.

**Solution.** The carrier is \(x_1=x_2=\xi_3=0\), with parameters \((\xi_1,\xi_2,x_3)\). Here \(c=2\), so its coefficient is
\(\operatorname{sgn}(d\xi_1\wedge d\xi_2\wedge dx_3)\otimes
\operatorname{sgn}(d\xi_1\wedge d\xi_2\wedge d\xi_3)\).
The restricted critical point is \(x_3=0\), and the graph intersection is
\(p=(0;1,2,0)\). The restricted Hessian is \((-1)\), so the intersection is transverse and its graph-first number is \(-1\). The raw determinant in (22) is also \(-1\), since \(c\) is even. Reversal contributes \((-1)^3=-1\), so the conormal-first number is \(+1\).

### A chart reversal changes both factors

*Difficulty: Intermediate.*

In coordinates \((u,t;\zeta,\tau)\) on \(T^*\mathbb R^2\), take \(Y=\{u=0\}\). Express (9) after the change \(u'=-u,\ t'=t\). Explain how the coefficient prevents an orientation obstruction on a nonorientable base.

**Solution.** Initially the coefficient is
\(-\operatorname{sgn}(d\zeta\wedge dt)\otimes
\operatorname{sgn}(d\zeta\wedge d\tau)\).
The dual variables are \(\zeta'=-\zeta,\ \tau'=\tau\). Hence both
\(\operatorname{sgn}(d\zeta'\wedge dt')\) and
\(\operatorname{sgn}(d\zeta'\wedge d\tau')\) are the negatives of their unprimed versions. Their tensor is unchanged, including the fixed codimension sign \(-1\).

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

**Solution.** The restricted block has determinant \((-2)\cdot3\cdot5=-30\) and one negative eigenvalue. Since \(c=1\), (22) gives raw determinant \(+30\). The normalized conormal coefficient supplies the additional sign \(-1\), so the number is \(-1\).

After the replacement, the restricted block has kernel spanned by the \(t_1\)-vector. The full Hessian has determinant \(-15\): expand along its second row and then the remaining diagonal \(3,5\) block. It is nonsingular. Nevertheless (22) has zero determinant. Explicitly the graph tangent corresponding to \(\delta t_1=1,\delta u=\delta t_2=\delta t_3=0\) has base component \(\delta t_1=1\) and fibre component \(\delta\zeta=1,\delta\tau=0\). This is also a conormal tangent. Thus the intersection is not transverse, and (21) cannot assign a transverse sign by the ambient Hessian.

### Integral signs before reduction modulo two

*Difficulty: Introductory.*

On \(T^*\mathbb R\), intersect an analytic section with the normalized full fibre over a point. Compute both orders over \(\mathbb Z\), and then extend the cycle coefficients to \(\mathbb Z/2\).

**Solution.** The section orientation is \(dx\) and the fibre orientation is \(-d\xi\), each with the common coefficient \(\operatorname{sgn}(d\xi)\). Their ordered tangent orientation is \(dx\wedge(-d\xi)=d\xi\wedge dx=\Omega\), so the section-first number is \(+1\). The fibre-first number is \(-1\), by (19). Reduction modulo two sends both to \(1\). The equality after reduction does not change the integral normalization from which the two values came. This is a calculation of orientation-valued cycles; it does not enlarge the characteristic-zero hypotheses of the characteristic-cycle construction.

### Ordinary, compact, stalk and costalk signs in one model

*Difficulty: Advanced.*

Let \(Y=\mathbb R\) be a closed coordinate line in \(X=\mathbb R^4\), let
\(F=i_*k_Y^3[2]\), and let \(\rho=|x|^2/2\). Check the two global finiteness conditions and compute the positive and negative graph numbers. Compare them with ordinary and compact cohomology, and with the stalk and ambient point costalk at zero.

**Solution.** Closed support sublevels of \(\rho\) are either empty or closed bounded intervals on \(Y\), hence compact. The full microsupport is \(T_Y^*X\), which is antipodally invariant. Both graphs meet it only at \((0;0)\), so both compactness tests hold. Here \(\ell=1,c=3,s=2,m=3\). The restricted Hessians have indices zero and one. Formula (23) gives \(+3\) for \(d\rho\) and \(-3\) for \(-d\rho\).

Ordinary cohomology is \(k^3[2]\), with Euler number \(+3\). Compact cohomology on the line is \(k^3[-1][2]=k^3[1]\), with Euler number \(-3\). The stalk is \(k^3[2]\), while the ambient point costalk is the line costalk shifted by two, namely \(\operatorname{or}_{Y,0}\otimes k^3[1]\). Its Euler number is \(-3\). Thus (26)–(28) give all four values with the same ordered orientation convention, despite the ambient dimension being even.

## References and further reading

For a later comparison with families, R. Fernandes, K. Kudomi and K. Takeuchi, [*Characteristic cycles of real and complex constructible sheaves, revisited*, arXiv2603.14821v2, 10 July 2026](https://arxiv.org/abs/2603.14821v2), §2.3, formulate intersection numbers through supported cup products and proper traces. Their family and limiting-cycle hypotheses require separate verification; the pointwise orientation calculation here does not establish that additional deformation theorem.

The orientation convention for conormal cycles and transverse intersections follows the theory of characteristic cycles of M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985). The supported operations and index proofs are in the lessons linked above; the normal-first wedge proof, the transition calculation and the full mixed-block determinant are proved here.

M. Kashiwara's [*Index theorem for constructible sheaves*](https://www.numdam.org/article/AST_1985__130__193_0.pdf), Astérisque 130 (1985), 193–209, §2.2, gives the earlier orientation-valued conormal normalization. W. Schmid and K. Vilonen's [*Characteristic cycles of constructible sheaves*](https://people.math.harvard.edu/~schmid/articles/cycles.dvi), published in *Inventiones Mathematicae* 124 (1996), 451–502, §2, gives an oriented-base formulation. Their base and fibre ordering should be compared together; (9) retains the fibre sign line explicitly. These are reading references; no expression or external proof replaces the internal arguments.
