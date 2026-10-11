# Relation cores and lifted symmetries

Adding a positive height to a measured relation turns its change of measure into a measure-preserving action. The resulting relation algebra is the continuous core. We first identify the exact existing proof of that assertion, including its Fourier sign and trace constant. We then lift every diagonal-preserving symmetry, transport its normalized weight cocycle, and compare the resulting core coordinates for arbitrary equivalent measures.

Throughout, a countable group acts nonsingularly on a nonzero standard Borel sigma-finite space \((X,\mu)\). Its principal relation is \(R\), its algebra is \(M\), its diagonal is \(D\), and \(\varphi_\mu=\mu\circ E\). Arrows are \((y,x):x\to y\), with source-counting measure \(\nu_s\) and modulus \(\delta=d\nu_r/d\nu_s\). Stabilizers, infinite orbits, infinite total measure and nonergodic actions are allowed.

## 1. The lifted relation and the exact core theorem

The complete earlier proof is Lifted orbit relations and the normalized core, abbreviated LFT. Its **right-counting** measure \(\nu_r\) is our **source-counting** measure \(\nu_s\); the modulus has the same orientation. The complete weight model needed to apply it is 1. Counting arrows and fixing the derivative through 2. The weight model at infinite mass. All cocycle identities are taken on the invariant conull version constructed there.

Put \(\widetilde X=X\times(0,\infty)\), with measure \(d\mu(x)d\lambda\), and define

\[
 \widetilde g(x,\lambda)
  =\bigl(gx,\delta(x,gx)\lambda\bigr).
 \tag{RCS.1}
\]

LFT Section 1 proves that this countable action preserves the measure and has exactly one lifted point over each distinct \(y\sim x\):

\[
 (y,\lambda_y),\qquad \lambda_y=\delta(x,y)\lambda.
 \tag{RCS.2}
\]

Thus its regular Hilbert space and algebra are

\[
 \widetilde H=L^2(R\times(0,\infty),\nu_s\,d\lambda),
 \qquad N=M(\widetilde R,\mu\,d\lambda).
 \tag{RCS.3}
\]

The lifted diagonal multiplier associated with a base function \(F\) acts by
\(\widetilde M_F\eta(y,x;\lambda)=F(y,\lambda_y)\eta(y,x;\lambda)\).
The source height \(\lambda\) and the target height \(\lambda_y\) are distinct.

For clarity, the precise proof route in LFT is:

- Section 1, equations LFT1.b–i: the invariant lift, distinct orbit points, the full orbit-field criterion and inversion of counting measure.
- Section 2, LFT2.a–i: the whole basepoint trace, including arbitrary-net normality, full traciality and order semifiniteness; the complete center.
- Section 3, LFT3.a–o: strongly continuous dilation, trace scaling and the entire fixed algebra, with both maps normal. Rational translation invariance is proved to make each bounded matrix coefficient constant.
- Section 4, LFT4.a–m: the onto Fourier unitary, both algebra inclusions, dual-flow covariance and the complete core-density domains.
- Section 5, LFT5.a–g: the constant in the canonical trace, first on diagonal tests and then on the whole positive cone by central trace-density uniqueness.

Here is the resulting theorem in our coordinates. Let
\(C_\mu=M\rtimes_{\sigma^{\varphi_\mu}}\mathbb R\), with regular generators

\[
 (\Pi_\mu(A)\xi)(r)=\sigma_{-r}^{\varphi_\mu}(A)\xi(r),
 \qquad (\Lambda_\mu(t)\xi)(r)=\xi(r-t).
 \tag{RCS.4}
\]

Then there is an onto normal isomorphism \(\Gamma_\mu:C_\mu\to N\) satisfying

\[
 \begin{aligned}
 \Gamma_\mu(\Pi_\mu(A))&=j(A),\\
 \Gamma_\mu(\Lambda_\mu(t))&=\widetilde M_{a^{-it}},\\
 (\theta_s A)(x,\lambda)&=A(x,e^s\lambda).
 \end{aligned} \tag{RCS.5}
\]

Here \(j(A)(x,\lambda)=A(x)\), and \(a\) denotes the height variable in a function on \(\widetilde X\); the represented value of \(a^{-it}\) is \(\lambda_y^{-it}\). The isomorphism carries the dual action, with
\(\widehat\sigma_s(\Lambda_\mu(t))=e^{-ist}\Lambda_\mu(t)\), to \(\theta_s\).

For group measure \(dt\) and dual measure \(ds/(2\pi)\), the normalized trace is

\[
 \tau_{\rm core}=\frac1{2\pi}\tau_{\rm bp},\qquad
 \tau_{\rm bp}(A)=\int_X\int_0^\infty
       \langle A(x,\lambda)e_x,e_x\rangle\,d\lambda\,d\mu(x).
 \tag{RCS.6}
\]

Both traces are faithful normal semifinite, and
\(\tau_{\rm bp}\circ\theta_s=e^{-s}\tau_{\rm bp}\).
Moreover

\[
 N^\theta=j(M),\qquad
 Z(N)=\widetilde M_{L^\infty(\widetilde X)^\Gamma},\qquad
 Z(N)^\theta=j(Z(M)).
 \tag{RCS.7}
\]

These are statements about the entire algebras. In particular an ergodic original relation has an ergodic associated flow on the displayed center; the center itself need not be scalar.

## 2. Why the Fourier, trace and product conventions matter

We record the actual unitary in the cited proof, so its signs can be used in the symmetry calculation. Take the normalized negative Fourier transform in \(r\), initially on integrable square-integrable tensors and then by its full Plancherel extension. The map is

\[
 (\mathcal W\xi)(y,x;\lambda)
   =\lambda^{-1/2}\widehat\xi
          \bigl(y,x;\log(\delta(x,y)\lambda)\bigr).
 \tag{RCS.8}
\]

Its inverse after Fourier transformation is

\[
 \widehat\xi(y,x;p)
  =\bigl(\delta(y,x)e^p\bigr)^{1/2}
        \eta\bigl(y,x;\delta(y,x)e^p\bigr).
 \tag{RCS.9}
\]

The substitution \(p=\log(\delta(x,y)\lambda)\) has \(dp=d\lambda/\lambda\), so these are inverse isometries on the full Hilbert spaces. LFT4 proves that the two generator images in (RCS.5) generate all of \(N\), rather than merely a subalgebra. The Fourier transform of \(\xi(r-t)\) is \(e^{-itp}\widehat\xi(p)\); this forces reciprocal height.

Accordingly the core density for \(\varphi_\mu\) is the affiliated operator

\[
 A_1=m_{\lambda_y^{-1}},\qquad
 D(A_1^z)=
 \left\{\eta:\int \lambda_y^{-2\operatorname{Re}z}|\eta|^2\,
                              d\nu_s\,d\lambda<\infty\right\}.
 \tag{RCS.10}
\]

Its imaginary powers are the second generators of (RCS.5). The positive finite height gives an injective operator; no boundedness of it or of its inverse is asserted.

The full-fibre expression
\(\int\operatorname{Tr}_{\ell^2([x])}(A(x,\lambda))\,d\mu(x)d\lambda\)
cannot replace (RCS.6). LFT Section 7, through LFT7.o, gives a complete example with an irrational rotation and an ineffective \(C_2\)-factor in which that expression is infinite on every nonzero positive element. Its finite positive cone is zero, so it fails semifiniteness. The basepoint trace, in contrast, is finite on \(1_{(1,2)}(\lambda)1\). This is the already established correction to the trace formula in the proof of Takesaki XIII.2.23.

There is also a separate continuous-orbit construction in LFT Section 6. It specifies the Hilbert space

\[
 H_\mu\otimes L^2((0,\infty),d\zeta/\zeta)
       \otimes L^2((0,\infty),d\lambda)
\]

and its generators. The continuous orbit coordinate is \(\zeta\); the remaining base multiplicity is \(\lambda\). Equations LFT6.b–l prove, in both directions, that its algebra is

\[
 \bigl(M\overline\otimes B(L^2(d\zeta/\zeta))\bigr)
                  \otimes1_{L^2(d\lambda)}.
 \tag{RCS.11}
\]

LFT6.n–s identify it normally with the double crossing, with exact generator and bidual-action formulas. It is not the lifted countable-relation algebra \(N\). The printed continuous product-action notation needs a continuous representation; the countable counting-fibre definition alone does not provide one. The specified theorem just cited supplies that representation. No undefined extension of the printed notation is used here.

These precise earlier proofs establish Theorem XIII.2.23's continuous-core and associated-flow conclusions, including their sigma-finite and nonfree scope, with the trace correction. The source's Definition 2.24 names the center flow the associated flow.

## 3. Lifting a geometric symmetry

Let \(\phi\in\operatorname{Aut}(R)\), and write
\(h_\phi=d(\phi_*\mu)/d\mu\), as in 3. The geometric unitary and its density. Define

\[
 L_\phi(x,\lambda)
       =\bigl(\phi x,h_\phi(\phi x)\lambda\bigr).
 \tag{RCS.12}
\]

Its inverse is
\(L_\phi^{-1}(x,\lambda)=(\phi^{-1}x,\lambda/h_\phi(x))\).
The derivative is positive and finite, so both maps are Borel on the appropriate conull space.

This lift preserves \(\mu\,d\lambda\). For a nonnegative Borel \(F\), substitution in the height and then the defining pushforward identity give

\[
 \begin{aligned}
 &\int_X\int_0^\infty
          F(\phi x,h_\phi(\phi x)\lambda)\,d\lambda\,d\mu(x)\\
 &=\int_X\frac1{h_\phi(\phi x)}
                  \int_0^\infty F(\phi x,u)\,du\,d\mu(x)\\
 &=\int_X\int_0^\infty F(y,u)\,du\,d\mu(y).
 \end{aligned} \tag{RCS.13}
\]

Tonelli permits infinite values. In the last line the factor \(h_\phi(y)\) from pushforward cancels the reciprocal factor. Using \(\lambda/h_\phi(\phi x)\) in (RCS.12) would reverse this cancellation.

RSY.11 gives

\[
 \delta(x,y)
   =\frac{h_\phi(\phi x)}{h_\phi(\phi y)}
                       \delta(\phi x,\phi y).
 \tag{RCS.14}
\]

Hence the lifted pair from (RCS.2) is sent to the pair

\[
 \bigl(\phi y,h_\phi(\phi y)\delta(x,y)\lambda\bigr),
 \quad
 \bigl(\phi x,h_\phi(\phi x)\lambda\bigr),
\]

which satisfies the lifted relation identity by (RCS.14). The inverse gives the reverse implication. Thus \(L_\phi\) is a measure-preserving automorphism of \(\widetilde R\). It commutes with all height dilations.

The chain rule \(h_{\phi\psi}=h_\phi(h_\psi\circ\phi^{-1})\) proves

\[
 L_\phi L_\psi=L_{\phi\psi}.
 \tag{RCS.15}
\]

All statements involve each specified pair of maps on a common conull set; they do not demand simultaneous representatives for the uncountable group of all symmetries.

## 4. Phases and the canonical extension

For a circle-valued relation cocycle \(c\), define its lifted cocycle by

\[
 \widetilde c\bigl((y,\lambda_y),(x,\lambda)\bigr)=c(y,x).
 \tag{RCS.16}
\]

Composing lifted arrows composes their underlying arrows, so the cocycle identity follows immediately. The symmetry classification and its complete kernel formulas are 2. Applying the symmetry theorems at infinite mass through 4. Weight transport on the entire finite left ideal, with the exact earlier proofs listed there.

For \(\alpha=\alpha_c\beta_\phi\), take the lifted automorphism
\(\widetilde\alpha=\alpha_{\widetilde c}\beta_{L_\phi}\).
Its standard implementer on (RCS.3) is

\[
 (\widetilde U_\alpha\eta)(y,x;\lambda)
   =c(y,x)\eta\left(\phi^{-1}y,\phi^{-1}x;
                                      \frac{\lambda}{h_\phi(x)}\right).
 \tag{RCS.17}
\]

There is no square-root prefactor here: \(L_\phi\) preserves the entire lifted base measure. Explicitly, substitute \(\lambda=h_\phi(x)u\) in the norm of (RCS.17), reindex the orbit sum, and use
\(h_\phi(x)d\mu(x)=d(\phi_*\mu)(x)\).
This proves the isometry; the inverse maps and conjugate transported phase prove surjectivity. Applying RSY-04 to the lifted relation proves that it preserves its natural cone and is the canonical implementer, including when its trace is infinite at the identity.

On the constant-field copy,

\[
 \widetilde\alpha(j(T))=j(\alpha(T)).
 \tag{RCS.18}
\]

For diagonal functions this is pullback by \(\phi^{-1}\). For an orbit generator, the geometric lift conjugates its motion to \(\phi g\phi^{-1}\), by (RCS.14); the cocycle contributes the phase \(c(y,\phi g^{-1}\phi^{-1}y)\), exactly as in RSY's kernel formula. These verify (RCS.18) on all generators. Both sides are normal maps, so the identity holds on all of \(M\).

At the lifted target, the inverse geometric map divides its height by \(h_\phi(y)\). Therefore

\[
 \begin{aligned}
 \widetilde\alpha(\widetilde M_{a^{-it}})
   &=j(M_{h_\phi^{it}})\widetilde M_{a^{-it}},\\
 \widetilde\alpha\theta_s&=\theta_s\widetilde\alpha .
 \end{aligned} \tag{RCS.19}
\]

The phase multiplier commutes with every diagonal multiplier; it does not contribute an extra height factor.

Transport back by \(\Gamma_\mu\). We have constructed a normal automorphism of the whole regular core, uniquely determined by

\[
 \begin{aligned}
 \alpha^{\rm core}(\Pi_\mu(T))&=\Pi_\mu(\alpha(T)),\\
 \alpha^{\rm core}(\Lambda_\mu(t))
   &=\Pi_\mu\bigl([D(\varphi_\mu\circ\alpha^{-1})
                                  :D\varphi_\mu]_t\bigr)\Lambda_\mu(t).
 \end{aligned} \tag{RCS.20}
\]

Indeed RSY-05 identifies the normalized cocycle in this equation with \(M_{h_\phi^{it}}\). Existence and normality come from the explicit onto lifted unitary and the full core isomorphism; they have not been inferred from an arbitrary covariant representation. Uniqueness follows because these are the defining generators of the regular core. This is the canonical extension with our numerator-first cocycle convention.

Finally \(\widetilde\alpha\) preserves \(\tau_{\rm bp}\): phases fix the diagonal expectation, and \(L_\phi\) preserves the integrating measure in (RCS.6). This holds on the entire positive cone, with infinite values. Thus it also preserves the normalized trace \(\tau_{\rm core}\).

## 5. Measure changes and the full density domains

Let \(\mu_q=q\mu\), with \(q\) positive and finite almost everywhere. RWT-03 proves
\(\delta_q(y,x)=q(y)\delta(y,x)/q(x)\).
Between the two lifted bases put

\[
 F_q(x,\lambda)=(x,\lambda/q(x)).
 \tag{RCS.21}
\]

Substitution proves that \((F_q)_*(\mu\,d\lambda)=\mu_q\,d\lambda\).
Also
\(\delta_q(x,y)\lambda/q(x)=\delta(x,y)\lambda/q(y)\);
therefore \(F_q\) carries \(\widetilde R_\mu\) onto \(\widetilde R_{\mu_q}\).
It commutes with dilations.

The induced onto unitary and normal algebra isomorphism are

\[
 \begin{gathered}
 Q_q:\widetilde H_\mu\longrightarrow\widetilde H_{\mu_q},
 \qquad (Q_q\eta)(y,x;\lambda')=\eta(y,x;q(x)\lambda'),\\
 C_q(T)=Q_qTQ_q^*,\qquad C_q(j_\mu(A))=j_{\mu_q}(A).
 \end{gathered} \tag{RCS.22}
\]

The norm identity uses \(q(x)d\mu(x)d\lambda'\); the inverse substitutes
\(\lambda'=\lambda/q(x)\). This proves unitarity on the whole Hilbert spaces for unbounded \(q\) as well. The algebra identity on constant fields follows first on the diagonal and orbit generators, then by normality. In the normalized core coordinates,

\[
 \begin{aligned}
 C_q(\Gamma_\mu(\Lambda_\mu(t)))
   &=j_{\mu_q}(M_{q^{-it}})
                      \Gamma_{\mu_q}(\Lambda_{\mu_q}(t)),\\
 \tau_{{\rm core},\mu_q}\circ C_q&=\tau_{{\rm core},\mu}.
 \end{aligned} \tag{RCS.23}
\]

For the first line the old target height is \(q(y)\) times the new target height. RWT-06 identifies \(q^{-it}\) with
\([D\varphi_\mu:D\varphi_q]_t\), fixing the sign and normalization. The second line follows from the measure transport and the common constant \(1/(2\pi)\).

Represent the core density of \(\varphi_q\) in the fixed \(\mu\)-model by \(C_q^{-1}\). Equations (RCS.10) and (RCS.23) give

\[
 A_q=m_{q(y)/\lambda_y},\qquad
 D(A_q^z)=\{\eta:(q(y)/\lambda_y)^{\operatorname{Re}z}\eta
                                      \in\widetilde H_\mu\}.
 \tag{RCS.24}
\]

This is a positive injective affiliated operator, with the displayed maximal complex-power domains. Its imaginary powers are
\(j(M_{q^{it}})\Gamma_\mu(\Lambda_\mu(t))\).
The commuting scalar multiplication functions justify this product; no unspecified product of unbounded operators is used.

Put \(q^\alpha=h_\phi(q\circ\phi^{-1})\). Using (RCS.17) at the target gives

\[
 \begin{gathered}
 \widetilde U_\alpha A_q^z\widetilde U_\alpha^*=A_{q^\alpha}^z,\\
 \widetilde U_\alpha D(A_q^z)=D(A_{q^\alpha}^z)
                       \qquad(z\in\mathbb C).
 \end{gathered} \tag{RCS.25}
\]

For the domain claim, apply the norm change of variables of (RCS.17) to the nonnegative measurable integrand
\((q(y)/\lambda_y)^{2\operatorname{Re}z}|\eta|^2\).
It gives equality of the two integrals, including \(+\infty\). The inverse gives both domain inclusions. The multiplier value at the inverse target is
\(q(\phi^{-1}y)h_\phi(y)/\lambda_y\), proving the operator formula. The logarithmic domains transport in the same way, with the squared logarithm in the integral.

The operators \(A_q\) live in the core and depend on height. They are different from the relative modular operators on \(H_\mu\), whose multiplier is \(q_2(y)\delta(y,x)/q_1(x)\) in RWT-05.

## 6. Compatibility, inner symmetries and the center flow

The derivative of \(\phi\) relative to \(q\mu\) is

\[
 h_\phi^{(q)}
       =h_\phi\,\frac{q\circ\phi^{-1}}q
\]

by RSY-06. Direct substitution gives the commuting coordinate identity

\[
 F_qL_\phi^{(\mu)}=L_\phi^{(q\mu)}F_q.
 \tag{RCS.26}
\]

Both sides send \((x,\lambda)\) to
\((\phi x,h_\phi(\phi x)\lambda/q(\phi x))\).
The lifted phases agree because \(F_q\) leaves the underlying endpoints unchanged. It follows, on the full represented algebras, that

\[
 C_q\widetilde\alpha^{(\mu)}
       =\widetilde\alpha^{(q\mu)}C_q.
 \tag{RCS.27}
\]

Thus the canonical extension is compatible with changing the diagonal reference weight, with the exact transition cocycle in (RCS.23).

Products of symmetries are compatible too. RSY-04 gives
\((c,\phi)(d,\psi)=(c(d\circ(\phi^{-1},\phi^{-1})),\phi\psi)\).
Equation (RCS.15) and the same endpoint formula for lifted phases prove

\[
 \widetilde{\alpha\beta}=\widetilde\alpha\,\widetilde\beta.
 \tag{RCS.28}
\]

The identity and inverse follow as special cases. This is an actual action on the core, not an assignment only up to an inner automorphism.

If \(\alpha=\operatorname{Ad}(M_bV_\theta)\) is inner and preserves the diagonal, then

\[
 \widetilde\alpha=\operatorname{Ad}(j(M_bV_\theta)).
 \tag{RCS.29}
\]

To see this explicitly, \(h_\theta(\theta x)=\delta(x,\theta x)\), so \(L_\theta\) is the full-group motion along the lifted orbit. Its unitary in \(N\) is \(j(V_\theta)\). The phase coboundary
\(b(y)\overline{b(x)}\) lifts to the coboundary of the base function
\((x,\lambda)\mapsto b(x)\). RSY-06's innerness proof now gives (RCS.29).

On the center, any diagonal phase acts trivially, and the geometric part is

\[
 (\widetilde\alpha F)(x,\lambda)
       =F\left(\phi^{-1}x,\frac{\lambda}{h_\phi(x)}\right),
 \qquad F\in L^\infty(\widetilde X)^\Gamma.
 \tag{RCS.30}
\]

Relation preservation ensures that the result is still invariant, and (RCS.19) makes this a conjugacy commuting with the associated flow. Formula (RCS.29) shows directly that inner diagonal-preserving automorphisms act trivially on the center. Equation (RCS.27) makes this center action independent of the chosen equivalent measure, under the specified conjugacy. No standard Borel quotient of the set of lifted orbits is assumed.

## 7. A finite model and a proper unbounded domain

Let \(X=\{1,\ldots,n\}\) with masses \(p_i>0\), and take the full relation. Its lifted orbits hold
\(w=p_x\lambda=p_y\lambda_y\) fixed. The unitary

\[
 (V\eta)_{yx}(w)=\eta(y,x;w/p_x)
\]

identifies \(\widetilde H\) with \(L^2((0,\infty),dw;M_n{}_{\rm HS})\):
the substitution \(w=p_x\lambda\) cancels the source mass in each norm integral. All bounded measurable diagonal matrix fields are lifted diagonal multipliers, and constant orbit permutations yield the matrix units. Thus they generate all bounded measurable matrix fields, and

\[
 \begin{gathered}
 N=M_n(\mathbb C)\overline\otimes L^\infty((0,\infty),dw),\\
 \tau_{\rm core}=\frac1{2\pi}\int_0^\infty\operatorname{Tr}_n(\,\cdot\,)\,dw,
 \qquad A_q(w)=\operatorname{diag}(p_iq_i/w).
 \end{gathered} \tag{RCS.31}
\]

Conversely each generator has this form, proving the entire algebra equality. The trace follows by substituting \(w=p_x\lambda\) into its basepoint formula and summing the \(n\) diagonal entries.

For a permutation \(\phi\),
\(h_\phi(i)=p_{\phi^{-1}i}/p_i\).
Its lift sends \(w\) to the same \(w\):
\(p_{\phi x}h_\phi(\phi x)\lambda=p_x\lambda\).
Hence its core extension is conjugation by the permutation matrix, with any prescribed diagonal coboundary phase added. The diagonal entries of \(A_{q^\alpha}\) are
\(p_{\phi^{-1}i}q_{\phi^{-1}i}/w\), exactly the permuted entries in (RCS.31). Under \(F_q\), the new coordinate is also
\((p_xq_x)(\lambda/q_x)=w\).
This model checks both covariance and measure independence without dropping unequal masses.

Already for the one-point space with unit mass, \(N=L^\infty(0,\infty)\) and \(A_1=m_{1/\lambda}\). The vector \(\eta=1_{(0,1)}\) has norm one but

\[
 \int_0^1\lambda^{-1}|\eta(\lambda)|^2\,d\lambda=\infty.
\]

It is outside \(D(A_1^{1/2})\). Every imaginary power remains an everywhere-defined unitary multiplier. Thus the full-domain clauses in Section 5 have content even in the smallest original algebra.

## 8. Problems with complete solutions

**Problem 1.** Determine the lift of the modular automorphism
\(\sigma_t^{\varphi_\mu}\), and give an implementing unitary inside the core.

**Solution.** On original kernels this automorphism has cocycle
\(c_t(y,x)=\delta(y,x)^{it}\) and identity geometric motion, by RWT-02. Its lifted cocycle is the coboundary of
\(b_t(x,\lambda)=\lambda^{-it}\), since

\[
 b_t(y,\lambda_y)\overline{b_t(x,\lambda)}
       =(\lambda_y/\lambda)^{-it}=\delta(y,x)^{it}.
\]

Therefore its extension is \(\operatorname{Ad}(A_1^{it})\). This proves innerness of the extension without claiming that the original relation cocycle was a coboundary on \(X\).

**Problem 2.** A geometric symmetry exchanges two different original orbits. Does formula (RCS.12) still make sense?

**Solution.** Yes. The derivative \(h_\phi=d(\phi_*\mu)/d\mu\) is defined on the base for every measure-class symmetry. Formula (RCS.14) compares pairs that are related on each side, which suffices to prove lift preservation. It never evaluates \(\delta(\phi^{-1}x,x)\) when that pair is outside \(R\). For the identity relation on two atoms, the exchange simply exchanges the two vertical components with the height scale from the ratio of their masses.

**Problem 3.** In the one-point example, replace the base mass \(1\) by \(q>0\). Check the normalization of the core trace and the transition generator.

**Solution.** The new basepoint trace is \(q\int d\lambda'\). The map \(F_q(\lambda)=\lambda/q\) has \(d\lambda=q\,d\lambda'\), so \(C_q\) preserves the normalized traces \((2\pi)^{-1}\int d\lambda\) and \((2\pi)^{-1}q\int d\lambda'\). The old generator becomes
\((q\lambda')^{-it}=q^{-it}(\lambda')^{-it}\), exactly (RCS.23). This scalar factor is visible even though the original modular action is trivial.

**Problem 4.** Let \(B\subset X\) have positive measure. Track its standard corner under the lifted symmetry.

**Solution.** RWT-07 cuts both endpoints to \(B\); the core's lifted coefficient projection is
\(j(M_{1_B})=\widetilde M_{1_{B\times(0,\infty)}}\).
In the tracial standard form its left and right projections cut the two lifted endpoints to that set. Formula (RCS.17) carries this Hilbert space onto the one with both endpoints in \(\phi B\times(0,\infty)\). The indicator cutdowns commute with every density multiplier in (RCS.24). Applying the nonnegative norm identity used in (RCS.25) with these indicators proves covariance on every corresponding full complex-power domain. Neither \(B\) nor its lifted corner is required to have finite trace.

## References

Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XIII, Section 2, Theorem 2.23 and Definition 2.24, pp. 28–30, gives the associated-flow construction. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8). The full programme proofs and their precise source corrections are located in Sections 1–2 above. Lifted relations and the associated flow, Sections 1–5, provides the complementary relation-theoretic route. Our core input is the current LFT lesson at the exact locators stated here. New exposition and the symmetry calculations are independently written and released under CC0.

