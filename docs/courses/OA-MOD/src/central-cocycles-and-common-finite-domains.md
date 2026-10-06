# Central cocycles and common finite domains

**Self-checked by the writing AI.**

Commutation of modular automorphisms leaves a central obstruction to invariance of the weights. On a factor it is one scalar rate, as in VE-02. On a general algebra its generator can be unbounded over the center. Spectral cutoffs control that rate without imposing a countable exhaustion on the algebra. Gaussian smoothing then gives a dense common finite ideal.

The source targets are Takesaki, *Theory of Operator Algebras II*, Exercises VIII.3(1)–(2). Both concern arbitrary von Neumann algebras and faithful normal semifinite weights. The second assumes that at least one weight is finite. Exercises 3–5 and 9 retain separate solution obligations.

The exact inputs are GC-08's normalized modular intertwiner; PT-02/03/04/05's cocycle transport, affiliated generator and invariant-weight equivalence; CH-01's ordered chain rule; CX-10's fixed-reference injectivity and CX-03's full entire right multiplier; CZ-05/07/08's centralizer and density rules; NW-12's sigma-strong/weak closed GNS graph and normal sums; WG's finite ideals and semifiniteness criterion; HAP-05's contractive approximation; and MA/SK's integration and spectral calculus. Scalar integration and complex analysis retain their separate provider status. No assumption of a faithful state, finite total masses, bounded central generator, or separable Hilbert space is made.

## Equal modular groups determine an exact central density

**Lemma.** If faithful normal semifinite weights \(\rho,\eta\) on \(M\) have the same modular group, there is a unique positive injective self-adjoint \(h\), affiliated with \(Z(M)\), such that

\[
 \eta=\rho_h,\qquad [D\eta:D\rho]_s=h^{is}.
 \tag{CM.1}
\]

The weight identity is on every positive element, including infinite values.

**Proof.** GC-08 gives \(\sigma_s^\eta=\operatorname{Ad}(u_s)\sigma_s^\rho\), where \(u_s=[D\eta:D\rho]_s\). Equality and surjectivity of the automorphisms imply \(u_s\in Z(M)\). The center is fixed pointwise by every modular group: a bounded central element and its adjoint are left and right finite-ideal multipliers, and commute on the finite linear domain, so CZ-05 applies. The cocycle law therefore becomes \(u_{s+r}=u_su_r\). PT-03 gives \(u_s=h^{is}\) with \(h\) centrally affiliated. PT-04 computes the same cocycle for \(\rho_h\), and CX-10 identifies the weights on all positives. The same generator argument proves uniqueness. \(\square\)

Here is a normalization consequence when \(\rho\) is finite. If, in addition, \(\eta(z)=\rho(z)\) for every central positive \(z\), then \(h=1\). Indeed, if
\(p=1_{(1+\delta,\infty)}(h)\ne0\), \(\delta>0\), then
\(\rho_h(p)\geq(1+\delta)\rho(p)>\rho(p)\). This follows by increasing bounded regularizations and CZ-07's density order. If \(q=1_{[0,1-\delta]}(h)\ne0\), \(0<\delta<1\), then
\(\rho_h(q)\leq(1-\delta)\rho(q)<\rho(q)\). Faithfulness and finiteness give \(0<\rho(p),\rho(q)<\infty\) when the projections are nonzero. These contradictions exclude all spectrum away from 1. The zero algebra satisfies the assertion trivially. Finite mass is essential in these strict inequalities; two infinite values cannot distinguish a density.

## Commuting flows produce a central bicharacter

Let \(\alpha_t=\sigma_t^\varphi\), \(\beta_s=\sigma_s^\psi\), and \(u_s=[D\psi:D\varphi]_s\), for faithful normal semifinite \(\varphi,\psi\). Suppose \(\alpha_t\beta_s=\beta_s\alpha_t\). There is a unique centrally affiliated self-adjoint \(\Theta\) such that

\[
 \alpha_t(u_s)=e^{ist\Theta}u_s,\qquad
 \psi\circ\alpha_t=\psi_{e^{-t\Theta}}.
 \tag{CM.2}
\]

All spectral powers have their full spectral domains. The exponential in the second identity can be unbounded, and that identity includes all positive energies.

**Proof.** Both \(u_s\) and \(\alpha_t(u_s)\) implement the same automorphism \(\beta_s\alpha_{-s}\): conjugate GC-08's intertwining identity by \(\alpha_t\) and use commutation. Thus
\(q(s,t)=\alpha_t(u_s)u_s^*\) is central. The modular actions fix the center. Applying the cocycle law in \(s\) and the action law in \(t\) gives

\[
 q(s+r,t)=q(s,t)q(r,t),\qquad
 q(s,t+v)=q(s,t)q(s,v).
 \tag{CM.3}
\]

The functions are jointly strongly continuous. In a faithful normal modular representation, \(\alpha_t(x)=\Delta_\varphi^{it}x\Delta_\varphi^{-it}\); joint continuity follows from strong continuity of these unitaries, strong continuity of \(u_s\), and their uniform norm bounds.

PT-03 applied to the central unitary group \(t\mapsto q(1,t)\) gives \(q(1,t)=e^{it\Theta}\), with \(\Theta=\log h\) centrally affiliated. For integers \(m\) and positive integers \(n\), both group laws give

\[
 q(m/n,t)=q(m/n,t/n)^n=q(m,t/n)=q(1,mt/n).
 \tag{CM.4}
\]

Taking rational approximations to real \(s\), and using strong spectral continuity, proves \(q(s,t)=e^{ist\Theta}\). This also proves uniqueness from the generator of \(q(1,t)\); no pointwise choice of roots or central measurable decomposition is needed.

Put \(\psi_t=\psi\circ\alpha_t\). Since \(\varphi\circ\alpha_t=\varphi\), PT-02 gives

\[
 [D\psi_t:D\varphi]_s=\alpha_{-t}(u_s)=e^{-ist\Theta}u_s.
 \tag{CM.5}
\]

The positive injective \(h_t=e^{-t\Theta}\) is centrally affiliated, hence affiliated with \(M_\psi\). PT-04 gives \([D\psi_{h_t}:D\psi]_s=h_t^{is}\); the ordered chain rule CH-01 then gives
\([D\psi_{h_t}:D\varphi]_s=h_t^{is}u_s\), exactly (CM.5). CX-10 identifies the two weights. This proves (CM.2) at infinite as well as finite values. \(\square\)

For \(p_N=1_{[-N,N]}(\Theta)\), \(N=1,2,\ldots\), the projections are central, are fixed by both modular groups, and increase strongly to 1. For \(x\geq0\), central compression and CZ-07/08's bounded-density order give

\[
 e^{-N|t|}\psi(p_Nxp_N)
 \leq\psi(\alpha_t(p_Nxp_N))
 \leq e^{N|t|}\psi(p_Nxp_N).
 \tag{CM.6}
\]

For clarity, on \(p_NH\) the density is bounded between \(e^{-N|t|}p_N\) and \(e^{N|t|}p_N\). Its bounded regularizations, evaluated on this corner, tend to that bounded density; CZ-07's increasing-continuity rule proves the identification with (CM.2). Thus (CM.6) is an all-positive inequality, rather than a formal product of unbounded operators. This countable sequence cuts one spectral operator; it is not an assumption that the algebra admits a countable finite projection exhaustion.

On a nonzero factor, \(\Theta=-\theta1\), with \(\theta\) as in VE-02. Consequently \(\psi\circ\alpha_t=e^{\theta t}\psi\). This comparison fixes the minus sign in the central density formula.

## A dense common finite ideal proves semifiniteness of the sum

**Theorem, Exercise VIII.3(1).** If the modular groups of faithful normal semifinite \(\varphi,\psi\) commute, then \(\varphi+\psi\) is semifinite.

**Proof.** NW-12 makes the sum a normal weight. Its finite left ideal is exactly

\[
 \mathfrak n_{\varphi+\psi}
   =\mathfrak n_\varphi\cap\mathfrak n_\psi.
 \tag{CM.7}
\]

We prove this ideal sigma-weakly dense. Fix \(x\in\mathfrak n_\psi\), fix \(N\), and set \(b=p_Nx\). Centrality and \(0\leq p_N\leq1\) give \(b\in\mathfrak n_\psi\). By (CM.6), every \(\alpha_t(b)\) is in that ideal and

\[
 \|\Lambda_\psi(\alpha_t(b))\|
       \leq e^{N|t|/2}\|\Lambda_\psi(b)\|.
 \tag{CM.8}
\]

We first justify the GNS integral without presuming norm continuity of this orbit. On a compact interval the displayed vectors lie in a fixed weakly compact Hilbert ball. If \(t_j\to t\), any weak cluster subnet, paired with
\(\alpha_{t_j}(b)\to\alpha_t(b)\) sigma-strongly, is identified by NW-12 with \(\Lambda_\psi(\alpha_t(b))\). Compactness and this unique cluster value prove weak continuity, for nets as well as sequences. On a bounded interval, weak Riemann integration is now obtained by integrating every scalar pairing and using the Riesz representation theorem. Its norm is at most the integral of the norm bound (CM.8). The same argument applies to continuous scalar multiples of the orbit.

For \(r>0\), define the strong* Gaussian operator integral

\[
 b_r=\sqrt{r/\pi}\int_{\mathbb R}e^{-rt^2}\alpha_t(b)\,dt.
 \tag{CM.9}
\]

On each finite interval use the same Riemann sums in \(M\) and \(H_\psi\). The operator sums converge sigma-strongly, and the GNS sums converge weakly to their Riesz integral. NW-12 puts the pair of integrals in the graph of \(\Lambda_\psi\). Gaussian tails of the operator integrals tend to zero in norm. The corresponding GNS tails tend to zero in norm, since

\[
 \|\Lambda_\psi(b_r)\|
 \leq\sqrt{r/\pi}\int_{\mathbb R}
          e^{-rt^2+N|t|/2}\,dt\ \|\Lambda_\psi(b)\|<\infty.
 \tag{CM.10}
\]

The last scalar integral is finite by completing the square separately on the two half-lines. A final application of NW-12 proves \(b_r\in\mathfrak n_\psi\) and the exact GNS integral identity. All operator Riemann sums have uniform norm bounds from scalar absolute integrals. Strong convergence on bounded sets therefore supplies the stated sigma-strong limits. No unbounded weight has been interchanged with an operator integral.

The formula
\(F_r(z)=\sqrt{r/\pi}\int e^{-r(t-z)^2}\alpha_t(b)dt\)
is norm-holomorphic in \(z\), satisfies \(F_r(0)=b_r\) and
\(\alpha_s(F_r(z))=F_r(z+s)\), and obeys
\(\|F_r(z)\|\leq e^{r(\operatorname{Im}z)^2}\|b\|\).
Scalar Gaussian domination on compact sets justifies all complex derivatives. Thus \(b_r\) is an entire element for \(\alpha\), bounded on each horizontal strip, and \(b_r\to b\) sigma-strongly* as \(r\to\infty\).

If \(y\in\mathfrak n_\varphi\), CX-03's full analytic right-multiplier theorem gives \(yb_r\in\mathfrak n_\varphi\). Since \(b_r\in\mathfrak n_\psi\) and \(\mathfrak n_\psi\) is a left ideal, it also gives \(yb_r\in\mathfrak n_\psi\). The finite linear domain \(\mathfrak m_\varphi\) is a sigma-weakly dense *-algebra contained in \(\mathfrak n_\varphi\). HAP-05 supplies contractions \(y_j\) in that algebra tending sigma-strongly* to 1. Therefore

\[
 y_jb_r\in\mathfrak n_\varphi\cap\mathfrak n_\psi,
 \qquad y_jb_r\longrightarrow b_r\quad\text{sigma-strongly}.
 \tag{CM.11}
\]

The sigma-weak closure of the intersection consequently contains every \(b_r\), then every \(p_Nx\), then every \(x\in\mathfrak n_\psi\), since \(p_N\uparrow1\). Semifiniteness of \(\psi\) makes this last ideal sigma-weakly dense. The intersection is therefore dense.

Here is the precise passage from a dense left ideal to WG-008's finite-positive criterion. For \(\chi=\varphi+\psi\), let \(p\) be the complement of the join of the supports of \(x^*x\), \(x\in\mathfrak n_\chi\). Then \(xp=0\) for every such \(x\); separate sigma-weak continuity of multiplication and density force \(p=0\). The supports of these finite positives thus join to 1. WG-008's construction \(e_a=a(1+a)^{-1}\), indexed by all finite positive \(a\) in their directed operator order, has a strong supremum dominating every one of these supports, hence supremum 1. Its converse proves that \(\mathfrak m_\chi\) is sigma-weakly dense, exactly semifiniteness. Faithfulness of the sum follows from that of either summand. \(\square\)

The proof uses weak GNS integration precisely where a norm-continuous GNS action has not been established. Ordinary algebra strong continuity alone would not justify such a norm-continuity assertion for an unbounded weight.

## Finite mass removes the central obstruction

**Theorem, Exercise VIII.3(2).** Let \(\varphi,\psi\) be faithful normal semifinite weights on an arbitrary \(M\), and assume at least one is a finite positive functional. Then the following are equivalent:

1. Their modular automorphism groups commute.
2. \(\varphi\circ\sigma_t^\psi=\varphi\) for every real \(t\).
3. \(\psi\circ\sigma_t^\varphi=\psi\) for every real \(t\).

**Proof of \(1\Rightarrow2,3\).** Suppose first that \(\psi\) is finite. For fixed \(t\), modular transport KM-06 and commutation give
\(\sigma^{\psi\circ\alpha_t}=\alpha_{-t}\sigma^\psi\alpha_t=\sigma^\psi\).
CM-01 expresses \(\psi\circ\alpha_t=\psi_h\) with a central positive injective density. For every central positive \(z\),
\((\psi\circ\alpha_t)(z)=\psi(z)\), since \(\alpha_t(z)=z\). The finite normalization consequence of CM-01 gives \(h=1\). Thus condition 3 holds on every positive element. PT-05 then gives condition 2. If \(\varphi\) is finite, interchange the two weights and apply the same argument. The finite weight is not required to be normalized to a state, and no factor hypothesis has entered the proof.

**Proof of \(2\) or \(3\Rightarrow1\).** Conditions 2 and 3 are equivalent by PT-05, without any finiteness assumption. Under condition 3 that theorem supplies \(\psi=\varphi_h\) with \(h\) affiliated with \(M_\varphi\), and CZ-11 gives

\[
 \sigma_s^\psi=\operatorname{Ad}(h^{is})\alpha_s,
 \qquad \alpha_t(h^{is})=h^{is}.
 \tag{CM.12}
\]

Hence \(\alpha_t\sigma_s^\psi=\sigma_s^\psi\alpha_t\). This proves the remaining implication. \(\square\)

Equivalently, the central generator \(\Theta\) of CM-02 vanishes whenever the commuting-flow hypothesis and finite-mass hypothesis hold. Indeed the resulting invariance gives \(\alpha_t(u_s)=u_s\) by PT-02 and cocycle injectivity; therefore \(q(1,t)=1\), whose generator is zero. In VE-03 both masses are infinite, so its nonzero scalar obstruction is consistent with this theorem.

## Three domain and normalization problems

**Problem 1. A bounded spectral cut is not finite mass.** Does \(p_N\) in CM-02 have to satisfy \(\varphi(p_N),\psi(p_N)<\infty\)?

**Solution.** No. In VE-03 the algebra is \(B(L^2(\mathbb R))\), the central generator is \(-1\), and \(p_N=1\) for every integer \(N\geq1\). Both total weights are infinite. The cut bounds the rate in (CM.6); it does not bound either mass. CM-03 separately starts with \(x\in\mathfrak n_\psi\), obtains a smoothed finite element, and uses a finite left multiplier for \(\varphi\). Each of those domain steps is necessary.

**Problem 2. Why weak integration suffices.** A bounded-interval GNS orbit is weakly continuous but its norm continuity has not been proved. What limit theorem identifies its integral with the GNS vector of the algebra integral?

**Solution.** NW-12 requires sigma-strong convergence of algebra entries and weak convergence of GNS entries. The same finite Riemann sums satisfy precisely these two conditions. The Riesz integral has the norm bound obtained by integrating (CM.8), so Gaussian tails converge in Hilbert norm. A second graph limit covers the whole real line. Neither separability nor a norm-continuous GNS action is needed.

**Problem 3. Finite mass can remove a nonscalar density.** On \(M=\mathbb C\oplus\mathbb C\), let \(\rho(x_1,x_2)=x_1+2x_2\) and \(h=(3,1/2)\). Are \(\rho\) and \(\rho_h\) determined by their modular groups? By their values on the center?

**Solution.** Their modular groups are both trivial, while \(\rho_h(x_1,x_2)=3x_1+x_2\). In particular their values at the central projection \((1,0)\) are 1 and 3. Agreement of modular groups permits this nonscalar density. Agreement on all central positives would force \(h=1\), by the finite normalization lemma. Merely agreeing at 1 is weaker: the distinct density \((2,1/2)\) gives \(\rho_h(1)=3=\rho(1)\).

## Source, dependency and illustration scope

CM-01–04 give full arbitrary-algebra arguments for Exercises VIII.3(1)–(2). The central bicharacter, its unique generator, all-positive density transport, bounded-cut estimates, weak GNS integral and contractive common-ideal approximation are separate visible steps. The finite argument uses central projection tests, rather than extending a factor's scalar-rate conclusion to a general center. The final problems distinguish a rate cutoff from finite mass, the two topologies of the graph theorem, and full central normalization from one total-mass value.

The reproducible original three-panel figure retained with this tranche shows the central character \(e^{ist\Theta}\), opposite density sign \(e^{-t\Theta}\), the integrable Gaussian bound \(e^{-rt^2+N|t|/2}\), and the two independent finite-domain operations. Its labels point to (CM.2), (CM.6), (CM.10) and (CM.11). The plotted central fibers and scalar bound are illustrations of proved formulas, not a central decomposition hypothesis or finite projection exhaustion.

Exercises VIII.3(3)–(5) and (9) are not solved in this lesson. In particular the all-positive identity in Exercise 9 cannot be credited merely because a dense finite algebra has matching quadratic values; VR-07 gives the reason for that caution.
