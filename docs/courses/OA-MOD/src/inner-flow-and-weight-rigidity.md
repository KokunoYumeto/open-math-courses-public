# Inner modular flow and rigidity of finite weight data

**Self-checked by the writing AI.**

A continuous unitary group implementing a modular flow can be removed by changing density. This produces a trace, and characterizes semifinite von Neumann algebras. Identifying two weights requires another argument: normal weights are lower semicontinuous, but need not be continuous even on a dense finite algebra. We prove two precise recognition results and construct a dense finite algebra on which distinct faithful weights agree.

The source antecedents are Takesaki, *Theory of Operator Algebras II*, VIII.3, Theorem 3.14 and Propositions 3.15–3.16. All statements below concern normal weights; the reference is faithful and semifinite. In the invariant recognition result, semifiniteness of the other weight follows from its stipulated finite algebra, and faithfulness is proved rather than assumed.

The inputs are WG's finite domains and semifiniteness criterion, WS's support of a normal functional, NW's normal bounded sandwiches, lower semicontinuity and closed GNS graph, HAP-05's contractive approximation from a nonunital algebra, CX-03's full analytic right multiplication, CZ-05/08/09/11's centralizers and affiliated density changes, and PT-03/06/08's continuous generators and invariant density theorem. QF's closed-form representation is used only in the final counterexample. No countable exhaustion of the algebra, faithful state on the whole algebra, or trace measurability of a density is assumed.

## Nonvacuous weights and the meaning of a trivial flow

Every von Neumann algebra \(M\) has a faithful normal semifinite weight. Here is a construction which allows arbitrary cardinality. A nonzero corner has a nonzero normal positive functional: take a nonzero vector in that corner in a faithful normal concrete representation. Its support is a nonzero projection, and its restriction to its support corner is faithful, by WS-04–06. Choose a maximal orthogonal family of such support projections \(p_i\), with normalized faithful normal states \(\rho_i\) on \(p_iMp_i\). Their join is one; otherwise the complementary corner supplies one more member. Define

\[
 \theta(x)=\sum_i\rho_i(p_i x p_i),\qquad x\in M_+,
 \qquad \sum_i=\sup_{F\subseteq I\ {\rm finite}}\sum_{i\in F}.
 \tag{VR.1}
\]

This is an additive homogeneous weight, and is normal because the supremum over finite sums commutes with increasing positive suprema. If \(\theta(x)=0\), each \(p_i x p_i=0\), hence \(x^{1/2}p_i=0\) for every \(i\), and \(x=0\). For \(p_F=\sum_{i\in F}p_i\),
\(\theta(p_Fxp_F)\leq |F|\|x\|\), and these bounded positive compressions tend sigma-strongly to \(x\). The finite positive domain is therefore sigma-weakly dense, giving semifiniteness by WG-008. The empty family handles the zero algebra.

A faithful normal semifinite weight \(\theta\) is a trace exactly when its modular group is trivial. The trace-to-trivial direction is PT-08's KMS identification. For the converse, \(M_\theta=M\). The entire right multiplier formula, now with constant modular orbit, is

\[
 \Lambda_\theta(av)=J_\theta v^*J_\theta\Lambda_\theta(a),
 \qquad a\in\mathfrak n_\theta,\ v\in M.
 \tag{VR.2}
\]

Let \(y=w|y|\) be the bounded polar decomposition, and suppose
\(\theta(y^*y)<\infty\). Then \(|y|\in\mathfrak n_\theta\), and (VR.2) gives

\[
 \theta(yy^*)=\|\Lambda_\theta(|y|w^*)\|^2
 =\|J_\theta wJ_\theta\Lambda_\theta(|y|)\|^2
 =\|\Lambda_\theta(|y|)\|^2=\theta(y^*y).
 \tag{VR.3}
\]

The norm equality uses \(w^*w|y|=|y|\), and (VR.2) also shows that right multiplication by \(w^*w\) fixes \(\Lambda_\theta(|y|)\). If instead \(\theta(yy^*)\) is finite, apply the same argument to \(y^*\). Thus either both values are finite and equal or both are infinite. This is the trace identity on all bounded \(y\).

## A continuous inner modular group characterizes semifiniteness

**Theorem.** For an arbitrary von Neumann algebra \(M\), the following are equivalent.

1. \(M\) admits a faithful normal semifinite trace.
2. For every faithful normal semifinite weight \(\varphi\), there is a sigma-strongly continuous one-parameter unitary group \(u_t\in M\) with \(\sigma_t^\varphi=\operatorname{Ad}(u_t)\).
3. For at least one faithful normal semifinite weight, such an implementing unitary group exists.

The group law and continuity in conditions 2–3 are part of the assertion; individual innerness at each time is insufficient for this proof. Moreover, for each fixed faithful normal semifinite trace \(\tau\), every normal semifinite weight \(\chi\), including a nonfaithful or zero weight, has a unique representation

\[
 \chi=\tau_h,\qquad h\geq0\text{ self-adjoint and affiliated with }M.
 \tag{VR.4}
\]

No trace measurability or bounded inverse is required.

**Proof.** Given the trace, PT-08 proves (VR.4), because its modular group is trivial. If \(\chi=\varphi\) is faithful, \(h\) is injective by CZ-08. CZ-11 then gives

\[
 \sigma_t^\varphi(x)=h^{it}xh^{-it},\qquad u_t=h^{it}.
 \tag{VR.5}
\]

These spectral unitaries form a strongly continuous group. This proves \(1\Rightarrow2\), including the final density assertion and its uniqueness. VR-01 ensures that \(2\Rightarrow3\) is nonvacuous.

Suppose condition 3 holds. Since \(u_su_t=u_tu_s\),
\(\sigma_s^\varphi(u_t)=u_su_tu_s^*=u_t\). Thus the entire implementing group lies in \(M_\varphi\). PT-03, applied with the opposite sign of its generator, supplies an injective positive affiliated \(k\) with

\[
 u_t=k^{-it},\qquad k\text{ affiliated with }M_\varphi.
 \tag{VR.6}
\]

Equivalently, if \(u_t=e^{itA}\), take \(k=e^{-A}\). The operator \(k\) is densely defined and has zero kernel; neither \(k\) nor its inverse need be bounded. CZ-08 constructs the faithful normal semifinite weight \(\tau=\varphi_k\), and CZ-11 computes

\[
 \sigma_t^\tau
 =\operatorname{Ad}(k^{it})\circ\sigma_t^\varphi
 =\operatorname{Ad}(k^{it}k^{-it})
 =\operatorname{id}.
 \tag{VR.7}
\]

VR-01 proves that \(\tau\) is a trace. This proves \(3\Rightarrow1\). \(\square\)

## Dense finite data do determine bounded sandwiches

Let \(\varphi,\psi\) be normal weights, and let \(\mathcal A\) be a sigma-weakly dense *-subalgebra contained in both finite linear domains, on which their linear extensions agree. For \(a,b\in\mathcal A\), the functionals

\[
 \omega^\theta_{a,b}(x)=\theta(a^*xb),\qquad x\in M,\quad
 \theta\in\{\varphi,\psi\},
 \tag{VR.8}
\]

are bounded and normal, with norm at most
\(\theta(a^*a)^{1/2}\theta(b^*b)^{1/2}\). The domains are valid: \(\mathcal A\subseteq\mathfrak m_\theta\subseteq\mathfrak n_\theta\cap\mathfrak n_\theta^*\), and the left ideal and product rules put \(a^*xb\) in \(\mathfrak m_\theta\). The bounded positive sandwich for \(a=b\), and polarization, prove normality, as in NW and PV.

For \(x\in\mathcal A\), also \(a^*xb\in\mathcal A\), so the two normal functionals coincide there. Sigma-weak density now yields

\[
 \varphi(a^*xb)=\psi(a^*xb),\qquad
 x\in M,\ a,b\in\mathcal A.
 \tag{VR.9}
\]

This extends bounded functionals, not the unbounded weights themselves. It does not yet identify their values on arbitrary positives.

## Gaussian cutoffs retain the common finite tests

Assume now that \(\varphi\) is faithful normal semifinite, that \(\psi\) is normal, and

\[
 \psi\circ\sigma_t^\varphi=\psi,\qquad
 \sigma_t^\varphi(\mathcal A)=\mathcal A\quad(t\in\mathbb R),
 \tag{VR.10}
\]

with the finite algebra and equality of VR-03. Write \(\sigma=\sigma^\varphi\).

HAP-05 supplies contractions \(b_j\in\mathcal A\) tending sigma-strongly* to one. Indeed apply that theorem in a faithful normal representation in which bounded strong* convergence gives the intrinsic topology, or amplify it to test any prescribed finite family of normal positive seminorms. Then
\(a_j=b_j^*b_j\in\mathcal A_+\), \(0\leq a_j\leq1\), and \(a_j\to1\) sigma-strongly*. No monotonicity of this net in the original nonclosed algebra is required. Put

\[
 e_j=\pi^{-1/2}\int_{\mathbb R}e^{-t^2}\sigma_t(a_j)\,dt,\qquad
 \sigma_z(e_j)=\pi^{-1/2}\int_{\mathbb R}e^{-(t-z)^2}\sigma_t(a_j)\,dt.
 \tag{VR.11}
\]

These are weak-star integrals, with \(e_j\) positive contractive and entire, by CZ-02/CX-03. For each fixed \(z\in\mathbb C\),

\[
 \|\sigma_z(e_j)\|\leq e^{(\operatorname{Im}z)^2},
 \qquad \sigma_z(e_j)\longrightarrow1\quad\hbox{sigma-strongly*}.
 \tag{VR.12}
\]

To prove the convergence for arbitrary nets, represent \(\sigma_t\) by \(\Delta_\varphi^{it}\). On a compact time interval, a uniformly bounded strongly convergent net converges uniformly on the compact vector orbit \(\{\Delta_\varphi^{-it}\xi\}\). The Gaussian tail is bounded independently of \(j\). Its complex kernel has integral one. This proves strong convergence at each \(z\); apply the conjugate kernel to the adjoints, and amplification to normal positive seminorms, to obtain the stated topology. This argument uses neither sequential dominated convergence for nets nor monotone cutoffs.

We must also justify the weight values of these integrals. For \(\theta=\varphi\) or \(\psi\), the curve
\(t\mapsto\Lambda_\theta(\sigma_t(a_j))\) has constant norm. It is norm continuous for \(\varphi\) by modular covariance. For \(\psi\), its squared differences equal those for \(\varphi\), since every difference and its squared modulus belong to \(\mathcal A\). Thus the same continuity holds without presuming a modular group for \(\psi\). Its Gaussian GNS integral exists. Finite Riemann sums converge both sigma-strongly in \(M\) and in GNS norm; truncate the time interval first and then its tails. NW-12's closed GNS graph gives

\[
 e_j\in\mathfrak n_\theta\cap\mathfrak n_\theta^*,\qquad
 \Lambda_\theta(e_j)=\pi^{-1/2}\int_{\mathbb R}
                       e^{-t^2}\Lambda_\theta(\sigma_t(a_j))\,dt.
 \tag{VR.13}
\]

For every \(s,t\), the elements \(\sigma_s(a_j),\sigma_t(a_j)\) are in \(\mathcal A\). Apply (VR.9) to their matrix coefficients and integrate the two GNS vectors in (VR.13). The coefficient bounds are uniform in \(s,t\), so the integrals are absolutely convergent. It follows that

\[
 \varphi(e_jxe_j)=\psi(e_jxe_j),\qquad x\in M.
 \tag{VR.14}
\]

Both sides are finite linear values on their actual sandwich domains. This proof does not interchange a general unbounded weight with an operator integral.

## Invariance and a dense invariant finite algebra force equality

**Theorem.** Let \(\varphi\) be faithful normal semifinite on \(M\), and \(\psi\) a normal weight invariant under \(\sigma^\varphi\). Suppose there is a sigma-weakly dense invariant *-subalgebra
\(\mathcal A\subseteq\mathfrak m_\varphi\cap\mathfrak m_\psi\) on which the weights agree. Then \(\psi=\varphi\) on all \(M_+\). In particular \(\psi\) is faithful.

The membership in \(\mathfrak m_\psi\) makes the asserted linear equality meaningful. It also proves semifiniteness of \(\psi\), since that domain is sigma-weakly dense.

**Proof.** Use VR-04's \(e_j\). If \(x\in M_+\) and \(\varphi(x)<\infty\), the full right multiplier lemma gives

\[
 \Lambda_\varphi(x^{1/2}e_j)
 =R_j\Lambda_\varphi(x^{1/2}),\qquad
 R_j=J_\varphi\sigma_{-i/2}(e_j)J_\varphi.
 \tag{VR.15}
\]

Here \(e_j=e_j^*\), and the right product belongs to \(\mathfrak n_\varphi\). By (VR.12), \(R_j\to1\) strongly, with a uniform bound. Consequently

\[
 \varphi(e_jxe_j)\longrightarrow\varphi(x).
 \tag{VR.16}
\]

The bounded positives \(e_jxe_j\) tend sigma-strongly to \(x\). Normal lower semicontinuity, (VR.14) and (VR.16) imply \(\psi(x)\leq\varphi(x)\). The inequality is automatic when \(\varphi(x)=\infty\), so \(\psi\leq\varphi\) on all positives.

PT-06 now supplies a possibly singular density \(h\geq0\), affiliated with \(M_\varphi\), such that \(\psi=\varphi_h\). In fact

\[
 0\leq h\leq1.
 \tag{VR.17}
\]

For otherwise some \(p=1_{(1+\delta,\infty)}(h)\), \(\delta>0\), is nonzero. It belongs to \(M_\varphi\), and CZ-09 makes \(\varphi|_{pMp}\) faithful normal semifinite. Choose \(0\ne y\in(pMp)_+\) with \(\varphi(y)<\infty\). The density \(h\) dominates \((1+\delta)p\) in form order. CZ-08 then yields
\(\psi(y)\geq(1+\delta)\varphi(y)>\varphi(y)\), contradicting \(\psi\leq\varphi\). Thus every such spectral projection vanishes, proving (VR.17).

For any \(x\in\mathfrak m_\varphi^+\), put \(B=J_\varphi h^{1/2}J_\varphi\). The bounded density formula and the full right multiplication by the fixed \(h^{1/2}\) give

\[
 \psi(x)=\|B\Lambda_\varphi(x^{1/2})\|^2,\qquad
 \psi(e_jxe_j)=\|B R_j\Lambda_\varphi(x^{1/2})\|^2.
 \tag{VR.18}
\]

In particular, the second value tends to the first. Equality (VR.14) and (VR.16) prove
\(\psi(x)=\varphi(x)\) for every such finite positive \(x\).

If \(h\ne1\), (VR.17) supplies a nonzero
\(q=1_{[0,1-\delta]}(h)\) for some \(0<\delta<1\).
Again choose a nonzero finite positive \(y\in qMq\). On that corner the bounded density is at most \((1-\delta)q\), so CZ-07 gives

\[
 \psi(y)\leq(1-\delta)\varphi(y)<\varphi(y),
 \tag{VR.19}
\]

contradicting the equality just proved. Hence \(h=1\), and the all-positive density identity proves \(\psi=\varphi\), including infinite values. This also proves faithfulness; it was not used to construct a whole-algebra modular group for \(\psi\). \(\square\)

## Equal modular groups remove invariance of the finite algebra

**Theorem.** Let \(\varphi,\psi\) be faithful normal semifinite weights with
\(\sigma^\varphi=\sigma^\psi\). If they agree on a sigma-weakly dense *-subalgebra
\(\mathcal A\subseteq\mathfrak m_\varphi\cap\mathfrak m_\psi\), then they agree on all \(M_+\). The algebra need not be invariant.

**Proof.** The weight \(\psi\) is invariant under the common modular group, so PT-05 supplies a unique injective \(h\geq0\) affiliated with \(M_\varphi\), with

\[
 \psi=\varphi_h,\qquad
 \sigma_t^\psi=\operatorname{Ad}(h^{it})\circ\sigma_t^\varphi.
 \tag{VR.20}
\]

Equality of the automorphism groups implies \(h^{it}\in Z(M)\) for every \(t\). PT-03's generator uniqueness, or spectral reconstruction of \(\log h\), places all spectral projections of \(h\) in \(Z(M)\). Thus \(h\) is centrally affiliated.

VR-03 still applies to \(\mathcal A\). For \(a\in\mathcal A\) and any central projection \(p\),

\[
 \psi(a^*pa)=\varphi(a^*pa)<\infty.
 \tag{VR.21}
\]

If \(h\ne1\), some nonzero central spectral projection lies either in \((1+\delta,\infty)\), \(\delta>0\), or in \([0,1-\delta]\), \(0<\delta<1\). For the first choice, \(a^*pa=pa^*ap\), and density order gives

\[
 \varphi(a^*pa)=\psi(a^*pa)
 \geq(1+\delta)\varphi(a^*pa).
 \tag{VR.22}
\]

For the second, compression of the density to \(pMp\) gives the reverse estimate
\(\psi(a^*pa)\leq(1-\delta)\varphi(a^*pa)\). In either case faithfulness forces \(pa=0\) for every \(a\in\mathcal A\). Multiplication by \(p\) is sigma-weakly continuous; density then gives \(p=0\), a contradiction. Thus \(h=1\). \(\square\)

Equal groups alone allow any injective central density in (VR.20). The finite algebra fixes that remaining normalization. On a factor the ambiguity is a single positive scalar; on an arbitrary center it may be an unbounded positive central operator.

## Distinct faithful weights on the same dense finite algebra

Let \(H=\ell^2(\mathbb N)\), \(M=B(H)\), and

\[
 A e_n=n^2e_n,\qquad
 \mathcal D=D(A^{1/2})=\{\xi:\sum_{n\geq1}n^2|\xi_n|^2<\infty\},
 \qquad q_A(\xi)=\sum_{n\geq1}n^2|\xi_n|^2.
 \tag{VR.23}
\]

The functional \(L(\xi)=\sum_n\xi_n\) is well defined on \(\mathcal D\) and continuous in its form norm, since

\[
 |L(\xi)|^2\leq\left(\sum_{n\geq1}n^{-2}\right)q_A(\xi).
 \tag{VR.24}
\]

Restrict \(q_A\) to \(\mathcal D_B=\ker L\). This is a closed positive form, bounded below by the Hilbert norm squared. Its domain is Hilbert-norm dense: the finitely supported zero-sum space
\(\mathcal D_0\) is dense. Indeed, to approximate a finitely supported \(\eta\) with coordinate sum \(s\), subtract \(s/m\) at each of \(m\) new coordinates. The resulting vector has zero sum and Hilbert distance \(|s|/\sqrt m\) from \(\eta\).

QF's representation theorem gives a positive self-adjoint \(B\geq1\) with

\[
 D(B^{1/2})=\mathcal D_B,\qquad
 \|B^{1/2}\xi\|^2=q_A(\xi)\quad(\xi\in\mathcal D_B).
 \tag{VR.25}
\]

Both \(A,B\) are affiliated with \(B(H)\) and injective. With the usual faithful normal semifinite trace, put
\(\varphi=\tau_A,\ \psi=\tau_B\). CZ-08/PT-08 prove that these weights are faithful normal semifinite.

Let \(\mathcal A_0\) be the finite span of rank-one operators
\(|\xi\rangle\langle\eta|\) with \(\xi,\eta\in\mathcal D_0\).
Products and adjoints stay in this algebra. It is sigma-weakly dense in \(B(H)\): rank-one operators from the dense vector space approximate all rank-one operators in norm, and finite-rank projections tend strongly to one; the compressions of a bounded operator are finite rank and converge sigma-weakly.

For a rank-one positive,

\[
 \tau_T(|\xi\rangle\langle\xi|)
 =\begin{cases}\|T^{1/2}\xi\|^2,&\xi\in D(T^{1/2}),\\
                +\infty,&\xi\notin D(T^{1/2}),\end{cases}
 \qquad T\in\{A,B\}.
 \tag{VR.26}
\]

To verify this identity, evaluate each bounded regularization \(T_\varepsilon\) by the rank-one trace identity, obtaining \(\langle T_\varepsilon\xi,\xi\rangle\), and take its increasing spectral limit. Thus the two weights are finite and equal on rank-one positives from \(\mathcal D_0\). Polarization places all of \(\mathcal A_0\) in both finite linear domains and proves equality there. Nevertheless,

\[
 \varphi(|e_1\rangle\langle e_1|)=1,\qquad
 \psi(|e_1\rangle\langle e_1|)=+\infty,
 \tag{VR.27}
\]

because \(L(e_1)=1\). This is a dense finite algebra with two different faithful normal semifinite weights.

The algebra fails precisely the invariance assumption used in VR-04. Put \(v=e_1-e_2\). Formula (VR.5) sends the rank-one positive of \(v\) to that of
\(e_1-4^{it}e_2\), whose coordinate sum is nonzero whenever \(4^{it}\ne1\). Every operator of \(\mathcal A_0\) has range in \(\mathcal D_0\), so that image is outside \(\mathcal A_0\). VR-06 also shows that the two modular groups cannot be equal.

There is a quantitative picture of the lost form-domain condition. Set

\[
 \xi^{(m)}=e_1-\frac1m\sum_{n=2}^{m+1}e_n,\qquad
 \|\xi^{(m)}-e_1\|^2=\frac1m,\qquad
 q_A(\xi^{(m)})=q_B(\xi^{(m)})
 =1+\frac{(m+1)(m+2)(2m+3)/6-1}{m^2}.
 \tag{VR.28}
\]

The vectors converge in Hilbert norm to \(e_1\), and their rank-one positives converge in operator norm, while their common energies tend to infinity. The endpoint has energy \(1\) for one closed form and infinite energy for the other. Normality supplies lower semicontinuity; it does not identify these two limits.

## Problems with complete solutions

**Problem 1. Check the sign of the trace-producing density.** On \(M_2(\mathbb C)\), let \(\varphi(x)=\operatorname{Tr}(dx)\), \(d=\operatorname{diag}(1,4)\), and choose \(u_t=d^{it}\). Find the \(k\) in (VR.6) and \(\varphi_k\). What happens if the implementer is replaced by \(c^{it}u_t\), \(c>0\)?

**Solution.** The correct density is \(k=d^{-1}\); its positive square root commutes with \(d\), and trace cyclicity gives
\(\varphi_k(x)=\operatorname{Tr}(x)\) for every positive matrix. The new implementer has generator \(\log d+(\log c)1\), so its cancelling density is \(c^{-1}d^{-1}\), and its trace is \(c^{-1}\operatorname{Tr}\). An inner implementation produces a trace but does not select its scalar normalization.

**Problem 2. Identify the central ambiguity exactly.** On
\(M=\prod_{i\in I}M_2(\mathbb C)\), let
\(\varphi(x)=\sum_i\operatorname{Tr}(d_i x_i)\) with each \(d_i>0\), and
\(\psi(x)=\sum_i c_i\operatorname{Tr}(d_i x_i)\) with finite \(c_i>0\). Show that the groups agree even if \(c_i\) has no common upper or lower bound. If the weights agree on the finite-coordinate matrix algebra, determine every \(c_i\).

**Solution.** The density \(h_i=c_i1_2\) is injective and centrally affiliated, with full spectral square-summability domain in the block Hilbert space. Formula (VR.20) gives identical block modular groups. Finite-coordinate positives have finite weight, proving semifiniteness without countability of \(I\). Testing the identity in a single block gives
\((c_i-1)\operatorname{Tr}(d_i)=0\), hence \(c_i=1\) for every \(i\). The groups retain the relative eigenvalues in each \(d_i\); the finite tests retain the mass of each block.

**Problem 3. Why the counterexample survives norm density of vectors.** Verify the norm convergence of the rank-one positives in (VR.28), and explain why it does not contradict normality of \(\psi\).

**Solution.** For bounded vectors,

\[
 \big\||\xi\rangle\langle\xi|-|\eta\rangle\langle\eta|\big\|
 \leq(\|\xi\|+\|\eta\|)\|\xi-\eta\|.
 \tag{VR.29}
\]

Apply this with \(\xi=\xi^{(m)}\), \(\eta=e_1\), and
\(\|\xi^{(m)}\|^2=1+1/m\). The right side tends to zero. The energies in (VR.28) grow asymptotically as \(m/3\); their lower limit is infinite, consistent with \(\psi\)'s infinite endpoint. The finite endpoint for \(\varphi\) is also consistent with lower semicontinuity. No monotone positive approximation or uniformly bounded energy was asserted.

**Problem 4. Locate the only unbounded limit used in recognition.** Why can VR-05 pass from the finite tests to all positives, when VR-07 cannot?

**Solution.** The invariant algebra supplies entire \(e_j\) whose right multiplication on the GNS space is the uniformly bounded family \(R_j\to1\). The common sandwich values therefore converge in the actual finite-energy norm. Lower semicontinuity first gives a global domination; spectral testing then bounds the invariant density, and the same GNS convergence forces it to be one. VR-07's approximants have unbounded energy and its dense algebra is not invariant. They supply neither the analytic right-multiplier convergence nor the central density conclusion.

These results author the full source statements VIII.3.14–3.16, retaining arbitrary normal semifinite weights in the trace-density clause and proving faithfulness in invariant recognition. Closed half-strip domination, analytic cocycle endpoints and the remaining VIII.3 results lie outside this lesson. The proofs here are relative to the named prerequisites, which are not proved in this lesson.
