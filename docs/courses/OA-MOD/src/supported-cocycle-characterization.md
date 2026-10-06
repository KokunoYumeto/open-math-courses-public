# Partial cocycles and their exact mixed KMS domains

**Self-checked by the writing AI.**

A nonfaithful weight has a fixed support, while its cocycle relative to a faithful weight has a moving initial projection. The comparison still has a mixed KMS formula. Its two boundary values belong to two different finite linear domains, so a proof must verify both before using the formula.

The source targets are Takesaki, *Theory of Operator Algebras II*, VIII.3.19–21. The inverse construction for 3.21 is already written in PL-01–04; this unit proves the missing six-clause characterization and identifies the two definitions of the supported derivative. Exact inputs are WS-04–06 and CW-05–06 for supports, lifted corners and faithful completion; WH-13 for arbitrary NSF weight existence; CZ-09 for modular restriction to a centralizer corner; GC-03–08 for the faithful balanced cocycle, mixed strips, trajectory recognition and dense mixed domain; WG-003–005 for finite linear domains and Cauchy–Schwarz; PL-03–04 and SI-09/14 for the full spatial corner identity and intrinsic cocycle; and MA-08 for scalar boundary uniqueness and the bounded-strip maximum principle. These are named inputs with their separate closure status retained. No countability or finite mass at the identity is assumed.

Throughout, \(\varphi\) is faithful normal semifinite, \(\psi\) is normal semifinite, \(e=s(\psi)\), and \(\sigma_t=\sigma_t^\varphi\). Write \(\psi_e\) for the faithful NSF restriction to \(eMe\). Its modular group acts on that corner. Semifiniteness here is a hypothesis: the restriction of an arbitrary normal weight to its support need not be semifinite.

## Compress the finite domains before filling the complement

Put

\[
 I=\mathfrak n_\psi^*\cap\mathfrak n_\varphi,
 \qquad I^*=\mathfrak n_\psi\cap\mathfrak n_\varphi^*.
 \tag{PC.1}
\]

Choose an NSF weight \(\eta\) on \((1-e)M(1-e)\) by WH-13 and set

\[
 \eta^\uparrow(a)=\eta((1-e)a(1-e)),\qquad
 \rho=\psi+\eta^\uparrow\quad(a\in M_+).
 \tag{PC.2}
\]

CW-05–06 show that \(\rho\) is faithful normal semifinite and that \(e\in M_\rho\). In particular \(\rho_e=\psi_e\), \(\rho(eae)=\psi(a)\), and CZ-09 identifies the modular restriction to \(eMe\). The complement weight vanishes on the \(e\)-corner. These statements include \(e=0\) and \(e=1\), using the zero weight on a zero complement.

Let \(I_\rho=\mathfrak n_\rho^*\cap\mathfrak n_\varphi\). For \(y\in I\) and \(x\in I^*\),

\[
 ey\in I_\rho,\qquad xe\in I_\rho^*.
 \tag{PC.3}
\]

Indeed support compression and order give

\[
 \begin{aligned}
 \rho(eyy^*e)&=\psi(yy^*)<\infty,&
 \varphi(y^*ey)&\leq\varphi(y^*y)<\infty,\\
 \rho(ex^*xe)&=\psi(x^*x)<\infty,&
 \varphi(xex^*)&\leq\varphi(xx^*)<\infty.
 \end{aligned}
 \tag{PC.4}
\]

Thus the compressed pair lies in the faithful mixed domains even if the original pair has infinite complement energy. In contrast, \(I_\rho\subseteq I\) because \(\rho\geq\psi\). GC-07's faithful mixed-domain argument makes \(I_\rho\) sigma-strong* dense in \(M\); therefore \(I\) is also dense. This is density of a vector space, not an assertion that it is a two-sided ideal.

## The support moves on the initial side

Use the numerator-first faithful cocycle of GC-08 and put

\[
 w_t=(D\rho:D\varphi)_t,\qquad u_t=ew_t.
 \tag{PC.5}
\]

Since \(e\) is fixed by \(\sigma^\rho\), modular intertwining gives

\[
 w_t\sigma_t(e)w_t^*=e,\qquad
 w_t\sigma_t(e)=ew_t.
 \tag{PC.6}
\]

It follows that

\[
 u_tu_t^*=e,\qquad u_t^*u_t=\sigma_t(e),\qquad u_0=e.
 \tag{PC.7}
\]

So \(u_t\) is a partial isometry from \(\sigma_t(e)H\) onto \(eH\) in any faithful normal representation. Multiplication by a fixed projection preserves sigma-strong* continuity of the bounded family \(w\). Moreover,

\[
 \begin{aligned}
 u_s\sigma_s(u_t)
 &=ew_s\sigma_s(e)\sigma_s(w_t)\\
 &=ew_s\sigma_s(w_t)=ew_{s+t}=u_{s+t}.
 \end{aligned}
 \tag{PC.8}
\]

Both cancellations involve bounded operators and the projection relation (PC.6).

For \(a\in eMe\), modular restriction to the centralizer corner gives

\[
 \sigma_t^{\psi_e}(a)
 =\sigma_t^\rho(a)
 =u_t\sigma_t(a)u_t^*.
 \tag{PC.9}
\]

The last expression is in \(eMe\). This does not define an automorphism of all of \(M\) for the nonfaithful weight.

## A mixed strip with two verified finite boundaries

For \(y\in I\), set \(z_t=u_t\sigma_t(y)\). Formula (PC.6) and faithful modular intertwining imply

\[
 z_t=w_t\sigma_t(ey),\qquad ez_t=z_t,
 \qquad z_tz_t^*=\sigma_t^\rho(eyy^*e).
 \tag{PC.10}
\]

Consequently

\[
 \psi(z_tz_t^*)=\psi(yy^*),\qquad
 \varphi(z_t^*z_t)=\varphi(y^*ey)\leq\varphi(y^*y).
 \tag{PC.11}
\]

The first identity uses \(\rho=\psi\) on the \(e\)-corner and invariance of \(\rho\); the second uses \(u_t^*u_t=\sigma_t(e)\) and invariance of \(\varphi\). Thus

\[
 u_t\sigma_t(I)\subseteq I\quad(t\in\mathbb R).
 \tag{PC.12}
\]

We retain the source's inclusion: \(u_t\) need not be invertible on all of \(M\).

For every \(x\in I^*\), \(y\in I\), there is a bounded continuous scalar function \(F_{x,y}\), holomorphic on \(0<\operatorname{Im}z<1\), with

\[
 F_{x,y}(t)=\psi(u_t\sigma_t(y)x),\qquad
 F_{x,y}(t+i)=\varphi(xu_t\sigma_t(y)).
 \tag{PC.13}
\]

Every weight value here is its finite complex linear extension. In fact \(z_t\in\mathfrak n_\psi^*\cap\mathfrak n_\varphi\), so \(z_tx\in\mathfrak m_\psi\) and \(xz_t\in\mathfrak m_\varphi\) by WG.

**Proof of the strip.** Apply GC-05, with numerator \(\rho\) and denominator \(\varphi\), to the pair \(ey\in I_\rho\), \(xe\in I_\rho^*\). Its lower boundary is

\[
 \rho(w_t\sigma_t(ey)xe)=\rho(z_txe)=\psi(z_tx),
 \tag{PC.14}
\]

because the middle product is an \(e\)-corner element and \(\psi\) evaluates its support compression. Its upper boundary is

\[
 \varphi(xew_t\sigma_t(ey))=\varphi(xz_t).
 \tag{PC.15}
\]

Here \(ew_t\sigma_t(ey)=w_t\sigma_t(ey)=z_t\) by (PC.10). This proves (PC.13), including the continuous boundaries and global strip bound. Cauchy–Schwarz and MA-08 also give the explicit bound

\[
 \|F_{x,y}\|_\infty\leq
 \max\!\left\{
 \psi(yy^*)^{1/2}\psi(x^*x)^{1/2},
 \varphi(xx^*)^{1/2}\varphi(y^*ey)^{1/2}
 \right\}.
 \tag{PC.16}
\]

All four energies are finite. Nothing in this argument subtracts infinite weights.

## Recognition and independence of the complement

Suppose \(v_t\) is another sigma-strong* continuous family satisfying the cocycle law, the projections (PC.7), the mixed-domain inclusion (PC.12), the mixed strip (PC.13), and the corner implementation (PC.9). Then \(v_t=u_t\) for every \(t\).

First the cocycle law at zero gives \(v_0^2=v_0\). Both support projections of \(v_0\) are \(e\), so it is a unitary in \(eMe\); an idempotent unitary equals \(e\). Fix \(y\in I_\rho\) and put \(Y(t)=v_t\sigma_t(y)\). This is sigma-strongly continuous and left supported by \(e\). Its two faithful-completion energies are

\[
 \rho(Y(t)Y(t)^*)=\psi(yy^*),\qquad
 \varphi(Y(t)^*Y(t))=\varphi(y^*ey).
 \tag{PC.17}
\]

For the first, use the competing family's corner implementation on the positive corner element \(eyy^*e\), and invariance of \(\psi_e\). The second follows from its initial projection. Both are finite and independent of \(t\). Thus \(Y(t)\in I_\rho\) and has the bounded energies required by GC-07.

Every \(x\in I_\rho^*\) also belongs to \(I^*\), so the competing mixed condition gives a strip with boundaries \(\psi(Y(t)x)\), \(\varphi(xY(t))\). Since \(eY(t)=Y(t)\) and the product is \(\rho\)-finite, its first value equals \(\rho(Y(t)x)\). GC-07, applied to the faithful pair \(\rho,\varphi\), now yields

\[
 v_t\sigma_t(y)=w_t\sigma_t(ey)=u_t\sigma_t(y)
 \quad(y\in I_\rho).
 \tag{PC.18}
\]

The bounded mixed-domain approximations of GC-07 converge sigma-strong* to every algebra element. Since \(\sigma_t\) preserves that convergence, testing (PC.18) on a bounded net approaching \(1\) proves \(v_t=u_t\). This verifies uniqueness at every real parameter.

Any other faithful complement completion produces a family with all the same six properties. The uniqueness just proved makes the result independent of the chosen complement weight. Because the faithful balanced cocycle is intrinsic, the supported family is intrinsic too.

**The normalization in the mixed characterization matters.** The source's sentence that its mixed condition determines the cocycle is read in the stated class of families. The bare existence of the two boundary values alone is insufficient: with \(M=\mathbb C\), \(\varphi=\psi\) the usual scalar weight, every constant phase \(v_t=c\), \(|c|=1\), has \(F_{x,y}(z)=cxy\). Its cocycle law requires \(c=c^2\), hence \(c=1\). Our uniqueness proof explicitly retains the initial value, finite domains and bounded energies provided by the other stated conditions.

## The six-clause derivative and the spatial interface

**Supported derivative theorem.** For a faithful NSF \(\varphi\) and a normal semifinite \(\psi\) on an arbitrary von Neumann algebra, there is a unique family \(u_t\) with all of the following properties:

1. It is sigma-strong* continuous.
2. It obeys \(u_{s+t}=u_s\sigma_s^\varphi(u_t)\).
3. Its final projection is \(s(\psi)\) and its initial projection is \(\sigma_t^\varphi(s(\psi))\).
4. It maps \(\sigma_t^\varphi(\mathfrak n_\psi^*\cap\mathfrak n_\varphi)\) into \(\mathfrak n_\psi^*\cap\mathfrak n_\varphi\).
5. Each pair \(x\in\mathfrak n_\psi\cap\mathfrak n_\varphi^*\), \(y\in\mathfrak n_\varphi\cap\mathfrak n_\psi^*\) has the mixed upper-strip function (PC.13), with both weight values finite in their linear definition algebras.
6. It implements \(\sigma^{\psi_e}\) on \(eMe\) by (PC.9).

PC-01–04 prove existence and uniqueness, including \(\psi=0\). In that case \(u_t=0\) and both mixed boundary values are zero. Definition VIII.3.20 names this family the cocycle derivative of \(\psi\) relative to \(\varphi\); we write

\[
 (D\psi:D\varphi)_t=u_t=e(D\rho:D\varphi)_t.
 \tag{PC.19}
\]

The complement \(\rho\) in this display is an auxiliary faithful completion, not part of the definition.

This agrees with the supported spatial cocycle in PL. Fix an NSF commutant reference \(\kappa\), and write \(A_\beta=d\beta/d\kappa\). The full corner-form identity proved in PL-03 gives

\[
 A_\psi^{it}=eA_\rho^{it},\qquad
 A_\psi^{it}A_\varphi^{-it}
 =e(D\rho:D\varphi)_t=u_t.
 \tag{PC.20}
\]

The first power is unitary on \(eH\) and zero on its orthogonal complement; at \(t=0\) it is \(e\). The form identity retains the entire square-root domain, rather than merely a Hilbert-dense set of bounded vectors. The second equality uses SI-14's faithful spatial normalization. Thus the spatial expression is independent of \(\kappa\) and has precisely the six properties above. No inverse of the noninjective \(A_\psi\) on all of \(H\) is used.

## An exact moving-projection model

On \(M=M_2(\mathbb C)\), take

\[
 h=\begin{pmatrix}1&0\\0&4\end{pmatrix},\quad
 v=2^{-1/2}\binom11,\quad e=vv^*,\quad
 \varphi(a)=\operatorname{Tr}(ha),\quad
 \psi(a)=3\operatorname{Tr}(ea).
 \tag{PC.21}
\]

The numerator is finite normal with rank-one support; the denominator is faithful finite. Fill the complement with \(5\operatorname{Tr}((1-e)\,\cdot)\). Its faithful completion has density \(k=3e+5(1-e)\). Finite trace spectral calculus, or the balanced matrix computation of GC-09, gives

\[
 u_t=e k^{it}h^{-it}=3^{it}e h^{-it}
 =\frac{3^{it}}2
   \begin{pmatrix}1&4^{-it}\\1&4^{-it}\end{pmatrix}.
 \tag{PC.22}
\]

The complement coefficient \(5\) disappears. Direct multiplication yields

\[
 u_tu_t^*=e,\qquad
 u_t^*u_t=e_t=h^{it}eh^{-it}
 =\frac12\begin{pmatrix}1&4^{-it}\\4^{it}&1\end{pmatrix}.
 \tag{PC.23}
\]

The initial ray is generated by \(v_t=h^{it}v\), and

\[
 u_tv_t=3^{it}v.
 \tag{PC.24}
\]

The final ray stays fixed. At \(t=\pi/(2\log4)\), the initial projection has off-diagonal entries \(-i/2,i/2\), whereas \(e\) has entries \(1/2,1/2\). Hence the numerator's fixed support need not centralize the denominator. On the one-dimensional corner \(eMe\), the numerator modular group is the identity, as (PC.9) predicts.

Every finite domain in this matrix example is all of \(M\). For arbitrary \(x,y\in M\), the exact mixed function is

\[
 F_{x,y}(z)=3^{1+iz}\operatorname{Tr}(eyh^{-iz}x).
 \tag{PC.25}
\]

It is entire and bounded on the closed upper strip. At the real boundary it is \(\psi(u_t\sigma_t(y)x)\). At \(z=t+i\), its scalar factor becomes \(3^{it}\) and its matrix power becomes \(h^{1-it}\). Finite trace cyclicity gives \(\varphi(xu_t\sigma_t(y))\), with the order in (PC.13) intact.

## Inverse correspondence and solved domain problems

**The inverse correspondence.** Suppose a sigma-strong* continuous partial-isometry family satisfies the cocycle law and the two projection equations (PC.7), for a fixed projection \(e\). PL-01–04 construct exactly one normal semifinite \(\theta\) with support \(e\) and supported spatial cocycle \(u_t\). By (PC.20), this is exactly the derivative defined in (PC.19). Therefore this construction proves VIII.3.21 with the same reference convention as VIII.3.19–20. The projection \(e\) may be zero or one and may fail to be fixed by \(\sigma^\varphi\). PL's completion and spatial recovery proofs retain all positive weight values, including infinity; no finite-state reconstruction is substituted.

**Problem 1. Where does the complement finiteness enter the strip proof?** Explain why an arbitrary \(y\in I\) need not be in \(I_\rho\), and why the proof can still apply the faithful mixed theorem.

**Solution.** Membership in \(I\) bounds \(\psi(yy^*)\), but need not bound \(\eta^\uparrow(yy^*)\). Left compression replaces \(y\) by \(ey\), whose complement energy is zero, while the left ideal of \(\varphi\) and the inequality \(y^*ey\leq y^*y\) keep its denominator energy finite. Likewise \(xe\) is in the faithful dual mixed domain. Equations (PC.14–15) recover the original two finite boundary values after those compressions. There is no unproved equality of the two mixed domains.

**Problem 2. The projection at zero.** A partial-isometry family has both projections \(e\) at zero and satisfies the cocycle law. Prove its value at zero equals \(e\), then explain why a constant nontrivial phase is excluded by the derivative theorem.

**Solution.** The zero-parameter law makes \(u_0\) idempotent. The two support equations make it a unitary in \(eMe\), so multiplying \(u_0^2=u_0\) by its inverse gives \(u_0=e\). A constant phase \(c\neq1\) in a nonzero scalar corner preserves the bare mixed boundaries but violates that law. On the zero corner the sole family is zero. This supplies the exact normalization used in PC-04's trajectory recognition.

**Problem 3. Keep arbitrary cardinality and unbounded masses.** Take \(M=\prod_{j\in J}M_2(\mathbb C)\) with any nonempty index set and positive finite numbers \(r_j\), with no common bound required. Lift (PC.21) blockwise with weights

\[
 \varphi(a)=\sum_j r_j\operatorname{Tr}(ha_j),\qquad
 \psi(a)=\sum_j 3r_j\operatorname{Tr}(ea_j).
 \tag{PC.26}
\]

Determine the support and cocycle, and prove semifiniteness and the mixed strip bounds.

**Solution.** The positive sums are suprema of finite subsums. The weights are normal; the denominator is faithful and the numerator has support \((e)_j\). Finite-coordinate projections increase strongly to one and have finite values, proving semifiniteness. Fill each complement by density \(5r_j(1-e)\). In its faithful cocycle the scalar powers \(r_j^{it}\) cancel, so each supported block is exactly (PC.22). Thus the family is bounded, has the stated moving initial projection, and is sigma-strong* continuous; bounded pointwise block convergence suffices in the product's normal representation. Formula (PC.16) is finite for the stated mixed pairs by Cauchy–Schwarz on the positive sums. The general theorem supplies their bounded strip even when a termwise infinite series has no uniform absolute bound outside that strip. The density families may be unbounded and not trace-measurable. No countability of \(J\) is used.

The six-clause supported derivative, its intrinsic normalization, and the earlier inverse construction have one explicit interface here. Analytic-generator recognition and the remaining VIII.3 results and exercises are not treated in this lesson.
