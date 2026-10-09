# Spatial operators inside spacetime microlocal tests

This independently written companion proves the mixed composition used in U030. Its mathematical antecedent is Hörmander III, Theorem 18.1.35 in the approved 2007 eBook. This exposition is CC0.

## M1. Classes, operator domains and the ordinary prerequisites

Write \(z=(t,x)\), \(\zeta=(\tau,\xi)\), with left quantization and \(D=-i\partial\). Suppose \(a\in S^m_{1,0}(\mathbb R^{1+n}_z\times\mathbb R^{1+n}_\zeta)\) and
\[
a(z,\tau,\xi)=0\quad\text{if }\epsilon|\tau|>1,
\quad |\xi|\leq\epsilon|\tau|.
\tag{MC1}
\]
Let \(b(t,x,\xi)\) satisfy
\[
|\partial_{t,x}^{\beta}\partial_\xi^\alpha b|
 \leq C_{\alpha\beta}\langle\xi\rangle^{m'-|\alpha|}.
\tag{MC2}
\]
Set \(A=\operatorname{Op}_{t,x}(a)\), \(B=b(t,x,D_x)\). The conclusion is that both \(BA\) and \(AB\) are ordinary spacetime operators of order \(m+m'\). Their symbols have the usual full left expansions, with all differentiated remainder estimates. Local versions follow by extending coefficients after a compact base cutoff; throughout the proof the bounds are global.

We use the included [ordinary calculus, O1–O6](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md): Schwartz continuity and distributional extensions, composition, adjoints, and complete amplitude/off-diagonal estimates. O3's estimates are continuous in finitely many input symbol seminorms at every fixed output seminorm. Consequently they apply uniformly to an extra parameter, and differentiation in that parameter follows by the product rule, first in the regularized integrals and then in their proved seminorm limits. This is a consequence of those estimates, rather than an additional parameter theorem.

In particular \(B\) and its adjoint preserve spacetime Schwartz functions. For \(\partial_t^kBv\), expand the finite sum of \((\partial_t^j b)(t,x,D_x)\partial_t^{k-j}v\). Each spatial Schwartz estimate is uniform in \(t\), and time weights commute with the spatial operator. Every joint Schwartz seminorm is therefore bounded by finitely many input ones. The spatial adjoint is \(B^*=b^*(t,x,D_x)\), with \(b^*\) satisfying (MC2), by O3 and the same differentiated estimates. This proves the consistent extension to joint tempered distributions by transposition.

## M2. The full smoothing ideal survives a spatial factor

If \(C=\operatorname{Op}_{t,x}(c)\) with \(c\in S^{-\infty}\), then \(BC\) and \(CB\) have full ordinary smoothing symbols. Here are the estimates that matter near the temporal axis. For every \(N,L,k,\ell\),
\[
\langle\tau\rangle^N\partial_\tau^k\partial_t^\ell
c(t,x,\tau,\xi)
\quad\text{is uniformly bounded in }S_x^{-L}.
\tag{MC3}
\]
Indeed any specified spatial seminorm follows from the full smoothing estimate of a sufficiently large negative order, using
\(\langle\tau\rangle^N\langle\xi\rangle^L\leq\langle\zeta\rangle^{N+L}\).
For each \((t,\tau)\), compose in \(x\) and let
\(d(t,x,\tau,\xi)=b(t)\mathbin{\#_x}c(t,\tau)\).
The spatial O3 estimates, applied with arbitrarily negative input order in (MC3), give for all prescribed derivatives and all \(N,L\)
\[
|\partial_{t,x}^{\beta}\partial_{\tau,\xi}^{\alpha}d|
 \leq C_{N,L,\alpha,\beta}
       \langle\tau\rangle^{-N}\langle\xi\rangle^{-L}.
\tag{MC4}
\]
Time derivatives distribute between the two factors and \(\tau\) derivatives fall only on \(c\); the polynomial \(\tau\) weight is constant in the spatial calculus. Take \(N=L\) arbitrarily large, and use
\(\langle\zeta\rangle\leq\langle\tau\rangle\langle\xi\rangle\).
This proves every full smoothing seminorm. The operator identity \(BC=\operatorname{Op}(d)\) follows by writing the full inverse time-Fourier integral for \(C\) and moving \(B(t)\) through it. On Schwartz inputs the uniform estimates (MC3) make this integral converge in every spatial Schwartz seminorm, including time derivatives. Thus the spatial composition identity applies inside the actual integral. Continuity gives the same identity on tempered distributions. Taking adjoints and applying this result to \(B^*C^*\) proves the assertion for \(CB\).

## M3. The product with the spatial operator on the left

Choose a smooth frequency cutoff \(\chi(\tau,\xi)\in S^0\), supported strictly inside the region where (MC1) gives zero, and equal to one on a narrower temporal cone at sufficiently large frequency. It can be obtained by multiplying a radial high-frequency cutoff and a smooth angular cutoff whose closed support satisfies \(|\xi|<\epsilon|\tau|\), with a positive margin. Increase the radial threshold so that \(\epsilon|\tau|>1\) throughout its support. The earlier bump construction supplies both cutoffs. On the high-frequency support of \(1-\chi\),
\(\langle\xi\rangle\) and \(\langle\zeta\rangle\) are comparable. Hence
\[
b_1(z,\zeta)=(1-\chi(\zeta))b(z,\xi)\in S^{m'},
\qquad B=\operatorname{Op}(b_1)+B\chi(D_z).
\tag{MC5}
\]
The identity is exact: right multiplication by a frequency multiplier multiplies a left symbol without derivative corrections. To verify the class for every real \(m'\), use comparability on each term containing \(1-\chi\), and on every derivative of the cutoff. Positive \(\tau\) derivatives of \(b\) vanish. In the bounded-frequency region all remaining derivatives are bounded. This proves every required isotropic loss, including when the resulting exponent is negative.

The full expansion of \(\chi(D_z)A\) has terms
\((\partial_\zeta^\alpha\chi)D_z^\alpha a/\alpha!\).
They all vanish: the cutoff and every nonzero derivative are supported inside the open zero region of \(a\). At every finite depth \(J\), O3 bounds the remainder in \(S^{m-J}\). The actual symbol therefore belongs to \(S^{-\infty}\). By M2,
\[
BA=\operatorname{Op}(b_1)A+B[\chi(D_z)A]
       \in\operatorname{Op}(S^{m+m'}).
\tag{MC6}
\]
Its expansion is
\[
\sigma(BA)\sim\sum_\alpha\frac{1}{\alpha!}
          (\partial_\zeta^\alpha b)D_z^\alpha a.
\tag{MC7}
\]
Indeed replacing \(b_1\) by \(b\) in any coefficient changes it by zero for the same support reason. Terms with a positive temporal component of \(\alpha\) vanish. For each \(J\) the difference from the sum over \(|\alpha|<J\) is in \(S^{m+m'-J}\), with every derivative and constants controlled by finitely many stated seminorms. The smoothing summand has every such bound by M2. This is an asymptotic expansion, without any assertion of convergence of the infinite formal series.

## M4. The other multiplication order and all remainder terms

The adjoint \(A^*\) need not have an exactly zero symbol on the original cone. Its ordinary adjoint expansion shows, however, that its full symbol is smoothing on every narrower temporal cone: all terms
\(\partial_\zeta^\alpha D_z^\alpha\overline a/\alpha!\)
vanish there, and the full remainder has arbitrarily negative order there. Choose a cutoff \(\chi_1\) supported in that narrower cone and equal to one in a still narrower cone. Then, exactly at the full-symbol level,
\[
A^*=A_2+C_1,\qquad
\sigma(A_2)=(1-\chi_1)\sigma(A^*),\qquad C_1\in\operatorname{Op}(S^{-\infty}).
\tag{MC8}
\]
The bounded-frequency part is smoothing as well. The symbol of \(A_2\) has the zero condition (MC1) with smaller \(\epsilon\) and a larger radial threshold, an immaterial change in M3's construction. Apply M3 to \(B^*A_2\) and M2 to \(B^*C_1\). Their sum is ordinary of order \(m+m'\); taking its full ordinary adjoint proves the same for \(AB\).

For clarity the resulting expansion is
\[
\sigma(AB)\sim\sum_\alpha\frac{1}{\alpha!}
             (\partial_\zeta^\alpha a)D_z^\alpha b.
\tag{MC9}
\]
All temporal derivatives of \(b\) on the right are allowed. Here is the finite algebra behind the adjoint reversal. Write \(T=\sum_j\partial_{\zeta_j}D_{z_j}\). The formal adjoint is \(e^T\overline a\); applying it twice gives \(e^Te^{-T}a=a\), because conjugation changes the sign of every \(D\). On two factors the Leibniz rule splits \(T\) into the two internal operators and the two cross operators \(\sum\partial_{\zeta}^{(1)}D_z^{(2)}\) and \(\sum\partial_{\zeta}^{(2)}D_z^{(1)}\). These constant-coefficient derivative operators commute. Expanding their exponentials to any fixed total degree, the internal terms and the cross term of the old product cancel, leaving exactly the opposite cross term in (MC9). The cancellation at degree \(\alpha\ne0\) is the finite binomial identity \(\sum_{\beta\leq\alpha}(-1)^{|\beta|}\binom\alpha\beta=0\). Truncate at degree \(J-1\); every discarded term is controlled by the ordinary composition and adjoint remainder at order \(m+m'-J\). The pieces involving \(C_1\) are smoothing by M2. Thus this formal computation proves the full differentiated finite-remainder statement, rather than assuming an unproved infinite-operator identity.

Each term of (MC9) is an ordinary symbol of its indicated order: where its \(a\) factor or derivatives are nonzero at large frequency, \(\langle\xi\rangle\) and \(\langle\zeta\rangle\) are comparable. The same reasoning also proves M3–M4 when \(a\) is merely smoothing on a temporal cone. Split it into an exactly vanishing-cone symbol and a globally smoothing symbol as in (MC8), and use M2 for both products with the latter.

## M5. Global tempered localization and the Cauchy receiver

We record explicitly why the proper-operator wavefront proof [W4](../20261004-free-intrinsic-graph/prerequisites/coordinate-and-wavefront-localization.md) applies to the global operators here on \(\mathcal S'\). For a global ordinary symbol \(p\), its kernel off the diagonal has arbitrary decay in the input position when the output ranges in a fixed compact. Apply \((-\Delta_\zeta)^N\) to \(p(z,\zeta)\) inside its Fourier integral and divide by \(|z-w|^{2N}\). Choosing \(2N\) greater than the symbol order, dimension and all requested output/input derivative orders makes the differentiated integral absolutely convergent. Increasing \(N\) gives every required power of \(w\). A smooth cutoff removing a neighborhood of the diagonal preserves these estimates by the product rule. This kernel is therefore a smooth family of Schwartz tests in the input on every compact output set. Its pairing with a tempered distribution is smooth, with every derivative obtained by pairing the corresponding test derivative. The near-diagonal part is proper after compact output localization, and W4 applies to it. This proves global tempered pseudolocality and the same essential-support bound. The included [conic parametrix K3](../20261004-free-intrinsic-graph/prerequisites/conic-parametrices-and-localization.md) then supplies elliptic regularity with its full remainder.

For use here and in U030, the Fourier Sobolev embedding has the following direct proof in dimension \(d\). If \(s>k+d/2\), Cauchy–Schwarz bounds \(\int |\zeta|^k|\widehat v(\zeta)|\,d\zeta\) by a constant times \(\|v\|_{H^s}\): the remaining squared weight is bounded by \(\langle\zeta\rangle^{-2(s-k)}\), whose integral converges by dividing into dyadic annuli and summing \(\sum_j2^{j(d-2(s-k))}\). Fourier inversion is then absolutely convergent with all derivatives through order \(k\); dominated difference quotients and continuity give a bounded continuous derivative for each. The distributional Fourier identity identifies these derivatives with those of \(v\). Choosing arbitrarily large \(s\) proves that membership in all Sobolev spaces implies smoothness. The same bound proves continuity, and differentiability when available, of a parameter family in these derivatives.

Now let \(u\in C_tH^r_x\) solve \((D_t+b(t,x,D_x))u=0\) on an open time interval, with smooth time coefficients and real homogeneous degree-one principal part \(b_0\). Fix an interior time and a compact time cutoff \(\rho\), equal to one nearby. The distribution \(v=\rho u\), extended by zero, is tempered: its pairing is bounded by a finite Schwartz seminorm using the compact time interval and the uniform \(H^r\) norm. Extend the coefficients smoothly with bounded symbol seminorms outside a slightly larger time interval. Choose an ordinary conic test \(C=\operatorname{Op}(c)\) of order zero, elliptic at the chosen covector with \(\xi\ne0\), with its frequency support away from the temporal axis. M3–M4 imply that
\[
C(D_t+B)\text{ is ordinary of order one, with principal symbol }
c_0(t,x,\tau,\xi)(\tau+b_0(t,x,\xi)).
\tag{MC10}
\]
Its value on \(v\) is \(-iC(\rho'u)\). Near the chosen time this is smooth: the input time support is separated, and the off-diagonal Schwartz-kernel estimate just proved applies, including its unbounded spatial input. Elliptic regularity consequently excludes every \(\xi\ne0\) covector with \(\tau+b_0\ne0\).

For the transported spatial test \(Q\) of U030, M3–M4 likewise make \(CQ\) ordinary, elliptic wherever \(c_0Q_0\ne0\). If \(Qu\) and all its time derivatives are continuous in every spatial Sobolev order, then \(\rho Qu\) is in every joint Sobolev order. To see this, integrate the squared spatial Sobolev norms of each time derivative on the compact time support, use the proved time Fourier Plancherel identity, and bound every nonnegative integer power of \(\langle(\tau,\xi)\rangle\) by a finite sum of products of time powers and spatial weights. All real orders follow by comparison. Thus \(C(\rho Qu)\) is smooth by the global Sobolev bounds and Fourier Sobolev embedding. Since \(Q\rho=\rho Q\), this is exactly \(CQv\), so elliptic regularity removes the selected spacetime covector. No assertion that a spatial-only symbol is globally ordinary was used.

*Proof and exposition: GPT-6 Astra (OpenAI), Ultra, 5 October 2026. Exact current prerequisite bindings and source hashes are in the accompanying proof map.*
