# Smooth pullback and the actual time slices

This companion retains Sections 18.5–18.6, WF11–WF17, of AN03-U012, *Detecting regularity without choosing coordinates*, in *Elliptic Operators & Boundary Problems: Renewed 2026 Course Draft*. The retained mathematical body is unchanged. The added Sections S1–S2 below give fixed-wavefront sequential continuity and the identification with the continuous Sobolev trace used in U030.

Copyright © 2026 AN-03 course project contributors. Principal author entity: AN-03 course-writing task. The AN-03 course-writing task and OpenAI Codex are responsible for the renewed edition. This selected and extended edition was prepared by the AN-04 course-writing task and OpenAI Codex, 5 October 2026; publisher: AN-04 local course project.

Permission is granted to copy, distribute and modify this document under the GNU Free Documentation License, Version 1.2 only, with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. The complete licence is [COPYING](notices/COPYING). Retained [title-page information](notices/TITLE_PAGE.md), [rights notice](notices/RIGHTS.md) and [history](notices/HISTORY.md) accompany this component.

## Exact earlier proofs used by the retained text

WF1 is the full [Fourier inversion and distributional Fourier proof L1–L3](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md), including the Gaussian normalization. WF2's compact order, polynomial Fourier bound, cutoff convolution and local smoothness criterion are [T0 and W1](../20261004-free-intrinsic-graph/prerequisites/coordinate-and-wavefront-localization.md); its WF4 nonstationary estimate is W2 there, and WF5/WF7's exact coordinate transport is W3. The complete constant-factor projection converse WF10 is the included [tensor-wavefront companion, Section 18.4](../20261005-restored-real-principal/tensor-wavefront-and-projection.md). Compact product integration and domination are [M3–M4](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md). The [earlier finite inverse theorem P3 and bump construction U001-A4](../20261004-free-stationary-phase/proof-map.html) supply the actual charts and partitions; for a finite compact cover take positive bump functions with positive sum on the compact set and divide each by their sum there, inserting a cutoff before its zero set. The reciprocal is smooth on this neighborhood, so the sum is exactly one. Thus every use of finite localization is justified by that construction.

The mathematical antecedent for pullback is the approved Hörmander I, Theorem 8.2.4 eBook ISBN 978-3-642-61497-2 (2003). The retained AN-03 proof and its notices supply the actual programme proof; a citation does not replace it. The accompanying proof map binds every used input to an exact included source and locator.

### 18.5. Constructing the pullback for the original smooth map

Let \(F:X\subset\mathbb R^b\to Y\subset\mathbb R^a\) be smooth. Its precise normal set and the required condition are

\[
N_F=\{(F(x),\eta):\eta\ne0,\ DF(x)^T\eta=0\},
\qquad N_F\cap\operatorname{WF}(u)=\varnothing.
\tag{WF11}
\]

We construct the map under this original transversality condition; no pullback at a forbidden covector is assumed. Near any fixed \(x_0\), the unit directions in the kernel of \(DF(x_0)^T\) form a compact set, possibly empty. WF11 makes every such direction regular at \(F(x_0)\). A finite regular cone cover, a common sufficiently small target cutoff \(\chi\), and WF2 give an open cone \(V_{\rm reg}\) on which \(\widehat{\chi u}\) decreases to every order, containing an angular neighborhood of those kernel directions. On the compact complementary unit directions \(DF(x_0)^T\eta\) has a positive lower norm. Continuity allows a fixed original neighborhood \(U_0\) of \(x_0\) and a constant \(c>0\) with
\(|DF(x)^T\eta|\geq c|\eta|\) there for every complementary direction. Shrink \(U_0\) so its image lies in the region where \(\chi=1\).

For \(f\in C_c^\infty(U_0)\), put \(v=\chi u\) and define

\[
\langle F^*u,f\rangle
=(2\pi)^{-a}\int_{\mathbb R^a}\widehat v(\eta)
                   \left(\int_{U_0}f(x)e^{iF(x)\cdot\eta}dx\right)d\eta.
\tag{WF12}
\]

On \(V_{\rm reg}\), the rapid input decrease and \(\int|f|\) give an integrable bound. On its complement, the actual phase gradient is \(DF(x)^T\eta\), so WF4 gives a bound \(C_N(1+|\eta|)^{-N}\max_{|\alpha|\leq N}\|\partial^\alpha f\|_\infty\). Multiplying by the original polynomial bound for \(\widehat v\) and choosing \(N>m+a\) proves absolute convergence. It also proves a continuous finite-order distribution estimate on each original compact test support, with its complete coordinate and map derivative constants. For smooth \(u\), WF1 and absolute testing show that this is exactly the smooth scalar function \(u(F(x))\).

Here is the needed independence and locality, rather than an assumed gluing rule. Use the original Cartesian Gaussian regularization
\[
g_\epsilon(y)=(4\pi\epsilon)^{-a/2}
      e^{-|y|^2/(4\epsilon)},\qquad
v_\epsilon=g_\epsilon*v,\qquad
\widehat v_\epsilon(\eta)=e^{-\epsilon|\eta|^2}\widehat v(\eta).
\tag{WF13}
\]
Its full mass and Fourier identity are proved in the integration/Fourier chapters. The two absolute bounds for WF12 dominate uniformly for \(0<\epsilon\leq1\), since \(0<e^{-\epsilon|\eta|^2}\leq1\). Thus WF12 is the limit of the actual smooth pullbacks \(v_\epsilon\circ F\).

If two target cutoffs equal one near \(F(\operatorname{supp}f)\), their difference times \(u\) is a compact distribution \(w\) vanishing near that compact image. The distance between that image and \(\operatorname{supp}w\) is positive. Its original compact finite-order estimate, applied to every derivative of \(g_\epsilon(F(x)-y)\), shows uniform convergence to zero on that image, including every fixed \(x\)-derivative: the full differentiated Gaussian has finitely many polynomial factors in the original difference coordinates and inverse powers of \(\epsilon\), times the same exponential. For distance at least \(d>0\), each such factor is bounded by \(C\epsilon^{-M}e^{-d^2/(8\epsilon)}\), tending to zero. The inserted support cutoff derivatives also remain in this estimate. Consequently the two limits agree on \(f\).

The same argument handles restriction to smaller original neighborhoods. For a compact test crossing several \(U_0\)'s, choose a finite smooth partition subordinate to them and sum WF12. On an overlap the preceding common Gaussian comparison gives equality; refinements therefore have the same sum. This constructs a unique local distribution \(F^*u\) on all of \(X\) with these formulas, preserving the original map. It proves its locality and compatibility with restriction. At a diffeomorphism, the smooth Gaussian approximations and the full measure substitution show agreement with WF5, including its actual inverse Jacobian. At the projection the same approximations and the integrated test show agreement with WF10's construction.

Its precise wavefront bound is

\[
\operatorname{WF}(F^*u)
\subset\{(x,DF(x)^T\eta):(F(x),\eta)\in\operatorname{WF}(u)\}.
\tag{WF14}
\]

For completeness fix a nonzero \(\xi_0\) outside the displayed set over \(x_0\). The singular unit target directions over \(F(x_0)\) are compact. WF11 says their images under \(DF(x_0)^T\) never vanish, and the chosen output direction is different from every resulting direction. Compactness yields positive margins for both assertions. Choose a closed angular neighborhood \(\Gamma\) of that singular set retaining these margins. Its complementary directions have a finite regular cone cover; WF2 again chooses a common target cutoff so that \(\widehat v\) decreases to every order outside \(\Gamma\). Shrink both original base and output direction neighborhoods so the margins hold for all \(x\) in the support of a cutoff \(b\) and every allowed output \(\xi\). If the singular set is empty, local smoothness already proved in Section18.1 supplies the conclusion directly.

The localized output transform is WF12 with \(f(x)=b(x)e^{-ix\cdot\xi}\). Its inner phase is exactly \(F(x)\cdot\eta-x\cdot\xi\), with gradient \(DF(x)^T\eta-\xi\). For \(\eta\in\Gamma\), the two compact margins give
\(|DF(x)^T\eta-\xi|\geq c(|\eta|+|\xi|)\): normalize their combined lengths to one; if the continuous difference had zero minimum, the covectors would have the excluded common direction, or a nonzero singular target direction would map to zero. WF4 therefore beats the full polynomial input bound and gives every output inverse power after integration in \(\eta\).

For \(\eta\notin\Gamma\), use the rapidly decreasing input. Split at \(|\eta|\leq c_0|\xi|\), with \(c_0>0\) smaller than the reciprocal of twice the actual compact bound for \(\|DF^T\|\). On that region the gradient has norm at least \(|\xi|/2\), so WF4 and the rapid input bound give every output power. On the other region \(|\eta|>c_0|\xi|\), the original bound for the inner integral is \(\int|b|\); taking the input decay exponent larger than the requested output exponent plus \(a+1\) gives every output power after integrating the full tail. This proves WF14 with the original Fourier constant still present in WF12. It proves a bound, and does not claim a converse for an arbitrary smooth map.

For a submersion \(F\), the normal set is empty, so the construction applies to every \(u\). Retain a nonzero \(a\)-row derivative minor at \(x_0\) and complete \(F\)'s coordinates by the remaining original \(x\)-coordinates. The resulting map \(\kappa(x)=(F(x),x_J)\) has its actual nonzero determinant. The proved inverse/implicit theorem gives a local diffeomorphism; in these coordinates \(F=\pi\circ\kappa\). Gaussian comparison in WF12 proves \(F^*u=\kappa^*(\pi^*u)\). WF7 and the exact WF10 converse therefore give

\[
\operatorname{WF}(F^*u)
 =\{(x,DF(x)^T\eta):(F(x),\eta)\in\operatorname{WF}(u)\}
 \quad\text{for a submersion}.
\tag{WF15}
\]

The derivative identity is the original chain rule
\(DF^T=D\kappa^T D\pi^T\). Its injectivity on target covectors is precisely full row rank, so every right-hand covector is nonzero. Every dimension-zero case has its point mass and empty Fourier factor; when the target has dimension zero, its distributions are smooth constants and both wavefront sets are empty.

### 18.6. Absence of parameter-normal covectors gives the actual smooth family

Let \(u\) be a distribution on an open product in the original variables \((t,x)\in\mathbb R^p\times\mathbb R^q\), with no wavefront covector \((t,x;\tau,0)\), \(\tau\ne0\). Every slice embedding \(j_t(x)=(t,x)\) satisfies WF11, because its transpose sends \((\tau,\xi)\) to \(\xi\). Thus the already constructed restriction \(u_t=j_t^*u\) exists.

Fix compact spatial test support and a small compact parameter neighborhood. The compact base set and the compact unit sphere in the original \(\tau\)-coordinates have a finite regular cone/base cover. Use its finite spatial partition and common smaller parameter neighborhood. After each compact localization \(v\), WF2 gives a constant \(\delta>0\) such that \(\widehat v(\tau,\xi)\) decreases to every order when \(|\xi|\leq\delta|\tau|\); on the whole space it has the original polynomial bound \(C(1+|\tau|+|\xi|)^m\). Summing the finitely many localized formulas retains all their cutoff derivatives.

For a spatial test \(\psi\), the actual pairing on the neighborhood where the parameter cutoff is one is

\[
\langle u_t,\psi\rangle
=(2\pi)^{-(p+q)}
 \iint e^{it\cdot\tau}\widehat v(\tau,\xi)\widehat\psi(-\xi)
                           \,d\xi\,d\tau,\qquad
\partial_t^\alpha e^{it\cdot\tau}=(i\tau)^\alpha e^{it\cdot\tau}.
\tag{WF16}
\]

In \(|\xi|\leq\delta|\tau|\), the rapid decrease of \(\widehat v\) dominates every original factor \(\tau^\alpha\) and both integration dimensions, while \(|\widehat\psi|\leq\int|\psi|\). In the complementary region, \(|\tau|\leq|\xi|/\delta\). The polynomial bound for \(v\), multiplied by the Schwartz bound
\[
|\widehat\psi(\xi)|\leq
(1+|\xi|^2)^{-N}
\int |(1-\Delta_x)^N\psi(x)|dx,
\tag{WF17}
\]
is integrable after both integrations when \(2N>m+|\alpha|+p+q\). The integral in WF17 is bounded by finitely many original test derivative seminorms on the fixed support, with every binomial and derivative from \((1-\Delta)^N\) retained in that full operator. These bounds are uniform on bounded sets of tests. For each derivative order, take a corresponding \(N\); no one fixed finite test order for all parameter derivatives is inferred.

Dominated differentiation therefore gives every derivative in WF16. Taylor's remainder for \(e^{ih\cdot\tau}\), bounded by a constant times \(|h|^2|\tau|^2\), and the same bounds with two additional frequency powers prove convergence of difference quotients uniformly on every bounded set of spatial tests. Continuity uses the same dominated bounds. This is precisely smoothness into the strong distribution topology, whose seminorms are suprema of pairings over bounded test sets. It is stronger than only the smoothness of each single pairing.

To verify that WF16 is the original pullback, apply WF13 to \(v\), then restrict the smooth Gaussian approximations. Their transforms acquire the full factor \(e^{-\epsilon(|\tau|^2+|\xi|^2)}\), bounded by one. The just proved absolute envelopes allow its limit and every fixed parameter derivative in WF16, agreeing with WF12 for the slice map. Finally testing against any original compact smooth \(\varphi(t,x)\) and applying these absolute bounds permits integration in \(t\), and recovers the original distribution pairing by WF1. Thus the family reconstructs \(u\), rather than an unrelated family with the same notation. Finite localization and restriction compatibility paste these actual families on the whole parameter domain. For \(p=0\) there is no parameter derivative; for \(q=0\) the no-normal condition is absence of all nonzero covectors and Section18.1 proves the required scalar smoothness.

## S1. Sequential continuity with a fixed permitted wavefront cone

Let \(\Gamma\subset T^*Y\setminus0\) be closed and conic, with \(N_F\cap\Gamma=\varnothing\). The fixed-wavefront convergence used here means \(u_j\to u\) in distributions, all wavefronts contained in \(\Gamma\), and the following uniform bounds: for every compact target cutoff \(\chi\), every closed frequency cone \(V\) whose product with \(\operatorname{supp}\chi\) avoids \(\Gamma\), and every \(N\),
\[
\sup_j\sup_{\eta\in V}\langle\eta\rangle^N
             |\widehat{\chi u_j}(\eta)|<\infty.
\tag{SC1}
\]
The limit satisfies the same bounds. The [uniform distribution-order theorem U1](../20261004-free-tangent-zoom/prerequisites/uniform-distribution-bounds.md) gives one compact finite-order bound for all \(u_j\) and \(u\). Consequently their compactly localized transforms have one polynomial bound. Testing against \(\chi e^{-iy\cdot\eta}\) gives pointwise Fourier convergence. One further derivative in \(\eta\) is uniformly bounded on every bounded frequency set by that same finite-order estimate, because it merely inserts a bounded coordinate factor on the fixed support. A finite frequency grid and the mean-value estimate therefore give uniform convergence on bounded frequency sets.

For the pullback, choose the local regular cone in WF12 from the complement of \(\Gamma\), rather than separately from each input wavefront. The compact normal directions have a common angular neighborhood avoiding \(\Gamma\), with a common target cutoff, by closedness, transversality and finite covering. On this cone (SC1) gives one integrable rapid envelope; on its complement the nonstationary bound in WF12 times the common polynomial input bound gives another. The pointwise Fourier convergence and dominated integration prove \(F^*u_j\to F^*u\) on every compact test. All distribution estimates are uniform in \(j\).

The set \(F^*\Gamma\) is closed over compact source neighborhoods: transversality gives \(|DF(x)^T\eta|\geq c|\eta|\) on the relevant unit directions of \(\Gamma\), so any convergent nonzero output covectors have bounded target lifts; a subsequence and closedness give a lift of their limit. For an output cone avoiding this set, the full WF14 proof uses two fixed positive margins and the same uniform input bounds. In its singular angular part the phase gradient is bounded below by \(c(|\eta|+|\xi|)\); in the regular part split at \(|\eta|=c_0|\xi|\). All constants in that proof are uniform in \(j\), so every output analogue of (SC1) follows. This proves sequential continuity into the fixed cone \(F^*\Gamma\), including its actual wavefront containment.

One may equivalently require convergence, rather than boundedness, of each rapid seminorm of \(u_j-u\) on a smaller closed permitted cone. To see this, split at radius \(R\). Bounded-frequency convergence handles the ball; (SC1) at exponent \(N+1\) bounds the order-\(N\) tail by \(C/R\), uniformly. Let first \(j\) and then \(R\) tend to infinity. The same argument applies to the output sequence.

The smooth Gaussian approximations in WF13 have this convergence locally. Indeed after an extra output cutoff \(\theta\), their Fourier transform is the convolution of \(\widehat\theta\) with \(e^{-\epsilon|\eta|^2}\widehat v(\eta)\). On a slightly larger permitted cone the input has uniform rapid decay; off that cone, the angular separation forces \(|\xi-\eta|\geq c(|\xi|+|\eta|)\) when \(\xi\) is in the smaller cone. The Schwartz bound for \(\widehat\theta\) then beats the fixed polynomial input bound. These are exactly the two integrable regions in W1's cutoff-convolution proof, uniformly since the Gaussian multiplier is at most one. Distributional convergence follows by Fourier inversion and dominated testing. If the auxiliary compact target cutoff introduces a remote singularity, split it with a cutoff equal to one near \(\operatorname{supp}\theta\); the separated Gaussian estimate in WF13 sends the remote term to zero with every derivative on that support. Thus no new local forbidden cone is introduced. Smooth approximation and sequential continuity also give uniqueness of the extension agreeing with ordinary smooth pullback.

## S2. Identification with the continuous Sobolev trace

Suppose \(u\in C(I;H^r(\mathbb R^n))\), viewed as a joint distribution, and its wavefront contains no pure temporal covector. The retained Section 18.6 constructs a smooth distribution-valued family \(j_t^*u\) reconstructing that same joint distribution. The given continuous Sobolev family is continuous into distributions, since pairing with each compact smooth spatial test is bounded by its \(H^{-r}\) norm. For any such test \(\psi\), the continuous scalar function
\[
h_\psi(t)=\langle j_t^*u-u(t),\psi\rangle
\tag{SC2}
\]
has zero integral against every compact smooth time test: both families reconstruct the same joint distribution. A continuous nonzero scalar function cannot have this property. At a nonzero value rotate by its conjugate phase; on a small interval its real part then has one strict sign, and a nonnegative bump in that interval gives a nonzero integral. Thus \(h_\psi(t)=0\) at every time, for every test. The pullback is exactly the continuous \(H^r\) trace. This proves the identification without assuming that weak restriction containment is wavefront equality; the reverse inclusion in U030 still requires its transported elliptic test.
