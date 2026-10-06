# Commuting modular flows and relative half-strip multipliers

**Self-checked by the writing AI.**

Two modular flows may commute while each rescales the other weight. A position–momentum example displays this phenomenon with exact signs and full operator domains. A second mechanism identifies an interweight right multiplier with the norm of its relative half-strip endpoint.

The source targets proved in this tranche are Takesaki, *Theory of Operator Algebras II*, Exercises VIII.3(6)–(8). The source has **nine** exercises: number 9 appears on printed page 133 before §4. Exercises 1–5 and 9 retain separate full-scope solution obligations. The present lesson proves 6–8; it does not mark the whole exercise set complete.

Inputs are KM-06's actual modular transport, PT-02/03/04's normalized cocycle transport and unitary generators, GC-08's modular intertwining, CX-10's fixed-reference injectivity, NW's lower semicontinuity, CZ's trace densities, HS-01–03's full closed-strip domains, and MA/SK/TC's integration, spectral calculus and adjoint-domain rules. Scalar Lebesgue integration and the scalar \(L^2\) Hilbert-space facts are further inputs; they are not proved in this lesson. Inner products are linear in their first slot. Weight identities on positives include infinite values.

## Equal modular groups on a factor differ by one scalar

Let \(M\ne0\) be a factor, and let \(\rho,\eta\) be faithful normal semifinite weights with \(\sigma^\rho=\sigma^\eta\). For \(u_t=[D\eta:D\rho]_t\), modular intertwining gives \(\operatorname{Ad}(u_t)\sigma_t^\rho=\sigma_t^\rho\). Surjectivity of each automorphism implies \(u_t\in\mathcal Z(M)=\mathbb C1\). Its cocycle law becomes an ordinary scalar group law, and its strong continuity gives

\[
 u_t=c^{it}1\quad(t\in\mathbb R),\qquad c>0.
 \tag{E3.1}
\]

For completeness, the continuous scalar unitary group has generator \(\lambda1\) by PT-03, and \(c=e^\lambda\). PT-04 computes the cocycle of \(c\rho\) as \(c^{it}1\). CX-10 then identifies the weights on every positive element:

\[
 \eta=c\rho.
 \tag{E3.2}
\]

The factor hypothesis is used exactly at the scalar center step. Equality of modular groups on a general algebra would instead allow a nonscalar central affiliated density.

## Commuting flows on a factor have opposite scaling rates

**Theorem, Exercise VIII.3(7).** If \(\varphi,\psi\) are faithful normal semifinite weights on a nonzero factor and their modular automorphism groups commute, there is \(\theta\in\mathbb R\) such that

\[
 \psi\circ\sigma_t^\varphi=e^{\theta t}\psi,
 \qquad \varphi\circ\sigma_s^\psi=e^{-\theta s}\varphi
 \quad(s,t\in\mathbb R).
 \tag{E3.3}
\]

**Proof.** Put \(\psi_t=\psi\circ\sigma_t^\varphi\). Modular transport KM-06 gives
\(\sigma_s^{\psi_t}=\sigma_{-t}^\varphi\sigma_s^\psi\sigma_t^\varphi=\sigma_s^\psi\).
VE-01 implies \(\psi_t=c(t)\psi\) with a unique \(c(t)>0\). Uniqueness and composition show \(c(t+r)=c(t)c(r)\), \(c(0)=1\). Choose \(x\geq0\) with \(0<\psi(x)<\infty\), which exists by nonzero faithfulness and semifiniteness. Lower semicontinuity of \(\psi\) on the sigma-weakly continuous orbit of \(x\) makes \(c(t)=\psi(\sigma_t^\varphi(x))/\psi(x)\) lower semicontinuous. Since \(c(-t)=1/c(t)\), it is also upper semicontinuous and hence continuous. Its real logarithm is additive and continuous, so its rational values and continuity give \(c(t)=e^{\theta t}\).

It remains to prove the sign in the second identity. Let \(u_s=[D\psi:D\varphi]_s\). PT-02 transports the normalized cocycle under \(\sigma_t^\varphi\). Scaling its numerator multiplies it by \(e^{i\theta ts}\), by PT-04 (or the spatial formula SI-14 and scalar functional calculus). Thus

\[
 \sigma_{-t}^\varphi(u_s)=e^{i\theta ts}u_s,
 \qquad\sigma_t^\varphi(u_s)=e^{-i\theta st}u_s.
 \tag{E3.4}
\]

For fixed \(s\) the last orbit is norm-entire, bounded on the lower half-strip, with endpoint

\[
 \sigma_{-i/2}^\varphi(u_s)=e^{-\theta s/2}u_s.
 \tag{E3.5}
\]

HS-03 therefore gives \(\varphi(u_sxu_s^*)\leq e^{-\theta s}\varphi(x)\) for all positives. Apply the same result to \(u_s^*\), whose eigenvalue and endpoint have the opposite exponents, then to \(u_sxu_s^*\). This gives the reverse inequality, including infinite values. Hence equality holds. Finally \(\sigma_s^\psi=\operatorname{Ad}(u_s)\sigma_s^\varphi\), and \(\varphi\) is invariant under its own modular group. This proves the second identity in (E3.3) with the exact negative sign. \(\square\)

If either weight is a finite positive functional, evaluating its scaling identity at 1 forces \(\theta=0\). This proves the finite-factor specialization of the invariance assertion; it does not replace Exercise 2's arbitrary-algebra scope.

## Position and momentum: commuting flows without commuting weights

Work on \(\mathcal H=L^2(\mathbb R,ds)\). The multiplication operator and momentum operator have the maximal domains

\[
 (Hf)(s)=sf(s),\quad D(H)=\{f:sf\in L^2\},\qquad
 Kf=-if',\quad D(K)=H^1(\mathbb R)=\{f\in L^2:f'\in L^2\text{ weakly}\}.
 \tag{E3.6}
\]

An \(H^1\) class has a locally absolutely continuous representative whose almost-everywhere derivative is the weak derivative. This is the precise self-adjoint interpretation of the derivative domain in the printed exercise; requiring an everywhere differentiable representative would not state the maximal domain.

**The full operator domains.** Real multiplication with its maximal square-integrability domain is self-adjoint by the scalar spectral model. Here is a direct check for \(K\) that avoids a Fourier-transform import. Compact smooth functions form a dense subspace of \(L^2\): approximate first by finite step functions on bounded intervals and then by smoothing their endpoints, using scalar dominated convergence. They belong to \(D(K)\). Integration by parts with compact cutoffs shows symmetry on all of \(H^1\). The extra cutoff term tends to zero by Cauchy–Schwarz and a cutoff derivative bounded by \(C/R\).

For \(\lambda>0\), the following Hilbert-norm integrals are bounded by \(\lambda^{-1}\|g\|_2\):

\[
 R_-g(s)=i\int_0^\infty e^{-\lambda t}g(s-t)dt,
 \qquad R_+g(s)=-i\int_0^\infty e^{-\lambda t}g(s+t)dt.
 \tag{E3.7}
\]

Translation is strongly continuous on \(L^2\), first on interval step functions and then by their density and the isometric bound. MA-02 therefore defines these vector integrals. Fubini, tested against compact smooth functions, gives
\((R_-g)'=ig-\lambda R_-g\) and \((R_+g)'=ig+\lambda R_+g\).
These derivatives lie in \(L^2\); integrating their local \(L^1\) representatives gives the locally absolutely continuous version. Thus

\[
 (K-i\lambda)R_-=I,\qquad(K+i\lambda)R_+=I.
 \tag{E3.8}
\]

Both ranges are all of \(\mathcal H\). To see that this proves self-adjointness, take \(z\in D(K^*)\), choose \(f\in D(K)\) with \((K-i)f=(K^*-i)z\), and use
\(z-f\in\ker(K^*-i)=\operatorname{ran}(K+i)^\perp=0\).
Consequently \(D(K^*)=D(K)\), proving the claim and closedness.

Its spectral unitary group and that of \(H\) are

\[
 (U_tf)(r)=e^{itr}f(r)=e^{itH}f(r),\qquad
 (V_sf)(r)=f(r+s)=e^{isK}f(r).
 \tag{E3.9}
\]

For the second identification, \(V_s\) preserves \(H^1\) and has norm derivative \(iKV_sf\) there, by the integral fundamental theorem and translation continuity of \(f'\). The spectral derivative of \(e^{isK}f\) is the same by dominated convergence on \(D(K)\). Differentiating \(e^{-isK}V_sf\) therefore gives zero; at zero it equals \(f\). Density extends the identity to all \(L^2\).

Put \(h=e^H\), \(k=e^K\), and \(\varphi=\operatorname{Tr}_h\), \(\psi=\operatorname{Tr}_k\) on \(B(\mathcal H)\). These are the normal semifinite faithful trace-density weights of CZ/PT. No trace measurability of \(h\) or \(k\) is required. Their modular actions are \(\operatorname{Ad}(U_t)\) and \(\operatorname{Ad}(V_s)\). Direct evaluation gives

\[
 U_tV_s=e^{-its}V_sU_t.
 \tag{E3.10}
\]

The scalar phase cancels in conjugation, so the two modular actions commute. They do not preserve the other weight. Indeed full-domain unitary transport gives

\[
 U_t^*KU_t=K+tI,\qquad V_s^*HV_s=H-sI,
 \qquad U_t^*kU_t=e^t k,\quad V_s^*hV_s=e^{-s}h.
 \tag{E3.11}
\]

Multiplication by the smooth phase preserves \(H^1\), so the first equality uses its whole domain. Translation preserves \(D(H)\) since adding a scalar does not change square integrability of \(rf(r)\). Spectral transport proves the exponential identities with their actual form domains. Trace-density covariance, equivalently the positive spectral regularizations of CZ-08, now gives

\[
 \psi\circ\sigma_t^\varphi=e^t\psi,
 \qquad\varphi\circ\sigma_s^\psi=e^{-s}\varphi.
 \tag{E3.12}
\]

Thus the rates in VE-02 are \(\theta=1\) and \(-1\), and the weights do not commute in the modular-invariance sense of PT-05. Their densities also fail to strongly commute, since their spectral unitary groups have the nontrivial Weyl phase (E3.10).

For a finite, nonzero observation take \(g(r)=\pi^{-1/4}e^{-r^2/2}\) and its rank-one projection \(p_g\). Gaussian integration gives \(\varphi(p_g)=e^{1/4}\). The Hilbert-norm entire translation of \(g\) is \(g(r+z)\), bounded on each horizontal strip. MA-09's spectral continuation criterion gives \(e^{K/2}g(r)=g(r-i/2)=e^{1/8}e^{ir/2}g(r)\); hence \(\psi(p_g)=e^{1/4}\) as well. Equation (E3.12) then changes this finite value by \(e^t\), which explicitly detects noninvariance. This solves Exercise VIII.3(6) with its unbounded-operator domains retained.

## An interweight multiplier is a relative half-strip norm

**Theorem, Exercise VIII.3(8).** Let \(\varphi,\psi\) be faithful normal semifinite weights on arbitrary \(M\), \(a\in M\), and \(k>0\). With \(\tau_t(a)=[D\psi:D\varphi]_t\sigma_t^\varphi(a)\), the following are equivalent:

1. \(\psi(axa^*)\leq k^2\varphi(x)\) for every \(x\in M_+\).
2. \(\mathfrak n_\varphi a^*\subseteq\mathfrak n_\psi\) and \(\|\Lambda_\psi(xa^*)\|\leq k\|\Lambda_\varphi(x)\|\) for every \(x\in\mathfrak n_\varphi\).
3. \(a\in D(\tau_{-i/2})\) and \(\|\tau_{-i/2}(a)\|\leq k\), with the full bounded closed-strip domain of AG-01.

**Proof.** Applying 1 to \(x^*x\) gives 2. Conversely apply 2 to the square root of every positive with finite \(\varphi\)-weight; at infinite reference weight the inequality in 1 is automatic.

For the equivalence with 3 use \(\Omega(X)=\varphi(X_{11})+\psi(X_{22})\) on \(M_2(M)\), and \(A=aE_{21}\). Its exact modular orbit and weight sandwich are

\[
 \sigma_t^\Omega(A)=\tau_t(a)E_{21},\qquad
 \Omega(AXA^*)=\psi(aX_{11}a^*)\quad(X\geq0).
 \tag{E3.13}
\]

If 1 holds, the last expression is bounded by \(k^2\varphi(X_{11})\leq k^2\Omega(X)\). HS-02/03, applied to \(A/k\), produce its lower half-strip and endpoint norm at most one. All entries except the 21 entry vanish on the real edge, so boundary uniqueness keeps them zero throughout; the remaining entry is \(\tau_z(a)/k\). This proves 3, including boundedness on the whole closed strip.

Conversely 3 supplies that matrix strip with endpoint norm at most \(k\). HS-03 gives \(\Omega(AXA^*)\leq k^2\Omega(X)\) on all positives. Set \(X=xE_{11}\) to obtain exactly 1. No corner energy or finite-domain condition was dropped. \(\square\)

If the notation \(\mathbb R_+\) is taken to include zero, the equivalence extends to \(k=0\): faithfulness and the full finite-ideal test force \(a=0\) in 1 or 2; a zero strip endpoint forces the same by inverse graphs AG-01. The zero element satisfies all three, interpreting the right side in 1 as the zero weight.

## Three solved sign and scope tests

**Problem 1: when does flow commutation imply mutual invariance on a factor?** **Solution.** It does exactly when \(\theta=0\) in (E3.3). If either weight is finite, evaluating the corresponding identity at the identity projection forces this. VE-03 shows why neither conclusion follows when both weights are infinite.

**Problem 2: reverse the momentum sign.** Replace \(K\) by \(-K\) and compute the rates. **Solution.** Its unitary is \(V_{-s}\), so the Weyl phase becomes \(e^{its}\). The transported exponentials are \(U_t^*e^{-K}U_t=e^{-t}e^{-K}\) and \(V_{-s}^*e^HV_{-s}=e^s e^H\). Thus the first rate is \(-1\), the other \(+1\); the modular actions still commute.

**Problem 3: a finite matrix test for an arbitrary multiplier.** Take \(h=\operatorname{diag}(1,4)\), \(l=\operatorname{diag}(2,8)\), the trace-density functionals \(\varphi_h,\psi_l\), and \(a=E_{12}\). Find the least \(k\) in VE-04. **Solution.** The entire relative orbit is \(l^{it}ah^{-it}\), so its endpoint is \(l^{1/2}ah^{-1/2}=E_{12}/\sqrt2\). Thus \(k=1/\sqrt2\). Directly \(\psi_l(axa^*)=2x_{22}\), whereas \(\varphi_h(x)=x_{11}+4x_{22}\) for \(x\geq0\). The sharp inequality is \(2x_{22}\leq(1/2)(x_{11}+4x_{22})\), with equality at \(x=E_{22}\). The reference weight on the right and the numerator on the left retain the orientation of (E3.13).
