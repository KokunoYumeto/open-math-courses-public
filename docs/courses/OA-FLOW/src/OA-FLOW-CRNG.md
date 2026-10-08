# The central functional classifies closed unitary orbits

<a id="crng-setting"></a>

The invariant is a positive normal functional on the center of the continuous core. It is not a central projection. Its mass retains the mass of the original functional, while the flow records scalar multiplication.

Earlier complete proofs: [CINV.MASS](OA-FLOW-CINV.md#cinv-mass), [CINV.INVERSE](OA-FLOW-CINV.md#cinv-inverse), [CINV.COVARIANCE](OA-FLOW-CINV.md#cinv-covariance), [CINV.METRIC](OA-FLOW-CINV.md#cinv-metric), [CSAS.DISTANCE](OA-FLOW-CSAS.md#csas-distance), [CSAS.RANGE](OA-FLOW-CSAS.md#csas-range), [CEXP.CONVERGENCE](OA-FLOW-CEXP.md#cexp-convergence), [CAPP.III-ZERO](OA-FLOW-CAPP.md#capp-iii-zero), [CPER.MASSES](OA-FLOW-CPER.md#cper-masses), [CPER.RANGE](OA-FLOW-CPER.md#cper-range), [MIV.1](OA-FLOW-MIV.md#miv-1), [MIV.2](OA-FLOW-MIV.md#miv-2), [HC.7](OA-FLOW-HC.md#oa-flow.hc.7), [SORB.TYPE-I](OA-FLOW-SORB.md#orbit-type-i), [SORB.RANGE](OA-FLOW-SORB.md#orbit-range), [CORE.9](OA-FLOW-CORE.md#core-9), [CSAS.TYPE-I](OA-FLOW-CSAS.md#csas-type-i), [CAPP.RESOLVENT](OA-FLOW-CAPP.md#capp-resolvent), [SORB.DIAMETERS](OA-FLOW-SORB.md#orbit-diameters).

<a id="crng-theorem"></a>
## 1. The full theorem

Let \(M\) be a nonzero infinite factor with separable predual. Let
\((C,\tau,\theta)\) be its common continuous core, with original Haar measure \(dt\), dual Haar measure \(ds/(2\pi)\), and \(\tau\theta_s=e^{-s}\tau\). Put \(Z=Z(C)\). For every \(\phi\in M_*^+\), including zero and nonfaithful functionals, use SCW's supported dual density and define
\[
 e_\phi=1_{(1,\infty)}(h_\phi),\qquad
 \chi_\phi(z)=2\pi\tau(e_\phi z)\quad(z\in Z).                      \tag{OR1}
\]
Then:

1. The projection \(e_\phi\) has trace \(\phi(1)/(2\pi)\), and
   \(\chi_\phi\) is positive normal with \(\|\chi_\phi\|=\phi(1)\).
2. Canonical normal chart identifications carry this functional to the same invariant; \(\chi_{\phi\circ\operatorname{Ad}u}=\chi_\phi\).
3. For all positive normal \(\phi,\psi\),
   \[
   \boxed{\quad
   \inf_{u\in\mathcal U(M)}\|\phi\circ\operatorname{Ad}u-\psi\|
          =\|\chi_\phi-\chi_\psi\| .
   \quad}                                                        \tag{OR2}
   \]
4. The map is a contraction for the predual norms, hence norm-continuous and Borel. For every \(c>0\),
   \[
   \chi_{c\phi}=c\,\chi_\phi\circ\theta_{\log c}.                   \tag{OR3}
   \]
   At \(c=0\) its value is zero.
5. If \(M\) is type II∞ or type III, its exact image is
   \[
   P_\theta=\{\chi\in Z_*^+:
               \chi\theta_s\ge e^{-s}\chi\text{ for every }s\ge0\}.
                                                                    \tag{OR4}
   \]
   For type I∞ the exact image is the discrete tail range in Section 3 below.
6. The family \(\{\chi_\phi:\phi\in M_*^+\}\) separates \(Z\): an element of \(Z\) annihilated by every member is zero.

Thus (OR1) induces an onto isometry from norm-closed unitary orbits onto the stated image. Equality of invariants is exactly equality of those closed orbits. Restricting to mass one gives the corresponding normal-state theorem. The domain must be the positive predual for (OR3); nontrivial scalar multiplication does not preserve the state space.

<a id="crng-cases"></a>
## 2. Proof of the distance and range in every type

[The finite spectral-cut construction](OA-FLOW-CINV.md#cinv-mass) proves the mass, chart covariance, inner invariance, scalar covariance, contraction and membership in \(P_\theta\), with the exact finite-domain pairings and full density domains. It also proves the metric on closed orbits is complete by a summable sequence of actual unitary alignments. Its support-sensitive partial-isometry approximation (CI18)–(CI19) retains zero complements and gives an explicit norm loss.

For type II∞, the [semifinite assembly](OA-FLOW-CSAS.md#csas-distance), including its [range construction](OA-FLOW-CSAS.md#csas-range), applies, with a one-point base in the factor case. Equations (SA12) and (SA18) prove (OR2) and (OR4). Its nonfactor theorem is needed below and was proved separately by measurable near-minimizers and a jointly selected full trace flag.

For type III\(_\lambda\), \(0<\lambda<1\), [the compact-to-continuous core comparison](OA-FLOW-CPER.md#cper-comparison) proves the normal spatial comparison between the compact and continuous cores, their exact trace scalar, the common supported densities and the actual central functional. Its unequal-mass extension (PCO13)–(PCO15) proves (OR2), and its full circle range (PCO16) proves (OR4). This use is a metric and range theorem; no diameter formula is substituted.

For type III₀, [the finite-orbit-block construction](OA-FLOW-CEXP.md#cexp-convergence) constructs increasing type II∞ subalgebras \(F_i\) of \(M\) with faithful normal compatible expectations satisfying
\(\|\eta E_i-\eta\|\to0\) for every \(\eta\in M_*\).
They are generally nonfactors. Their full distance and range statements are (SA12) and (SA18). [The core approximation argument](OA-FLOW-CAPP.md#capp-distance) lifts these expectations to the cores, proves exact trace preservation and supported-density inclusion, then proves the varying-center restriction-norm limit. Its equations (CM11) and (CM15) give (OR2) and (OR4) for the original type III₀ factor.

For completeness consider type III₁ explicitly. The actual modular-invariant theorem MIV1–2 identifies
\[
 S(M)\cap(0,\infty)=\exp K,\qquad
 K=\ker(\theta|_Z).
\]
Its normal center comparison and ergodicity are part of that theorem. Since \(S(M)=[0,\infty)\), injectivity of the real exponential gives \(K=\mathbb R\). Thus the center action is trivial; ergodicity then gives \(Z=\mathbb C1\). Formula (OR1) is therefore the scalar functional of mass \(\phi(1)\).

Let \(m=\phi(1)\), \(n=\psi(1)\). Testing on \(1\) gives the lower bound
\(\delta_M(\phi,\psi)\ge|m-n|\). If one mass is zero, the bound is equality by the positive-functional norm identity. Otherwise write
\(\phi=m\rho,\ \psi=n\sigma\), with normal states \(\rho,\sigma\).
The full normal-state homogeneity theorem HC, including its nonfaithful approximation in HC7, gives unitaries with
\(\|\rho\circ\operatorname{Ad}u-\sigma\|\to0\). Hence
\[
 \|\phi\circ\operatorname{Ad}u-\psi\|
 \le m\|\rho\circ\operatorname{Ad}u-\sigma\|+|m-n|
 \longrightarrow |m-n|.
\]
This proves
\[
 \delta_M(\phi,\psi)=|m-n|=\|\chi_\phi-\chi_\psi\|.                 \tag{OR5}
\]
Every nonnegative scalar is realized by a scalar multiple of one normal state. These are precisely the members of (OR4) on the scalar center.

<a id="crng-type-i"></a>
## 3. The exact type I∞ range

Use the usual trace on \(B(H)\), where \(H\) is separable and infinite-dimensional. In the Fourier coordinate of the continuous core, the central action is
\(\theta_s(z)(q)=z(q-s)\). If \(\lambda_1\ge\lambda_2\ge\cdots\ge0\) are the positive eigenvalues of the trace-class density, repeated with multiplicity and padded by zeros as needed, then
\[
 f_\phi(a)=\#\{j:\lambda_j>a\},\qquad
 \chi_\phi(z)=\int_{\mathbb R}z(q)e^{-q}f_\phi(e^{-q})\,dq.         \tag{OR6}
\]
SORB's actual finite-eigenvector matching proof gives
\[
 \delta_M(\phi,\psi)
   =\sum_j|\lambda_j(\phi)-\lambda_j(\psi)|
   =\int_0^\infty|f_\phi(a)-f_\psi(a)|\,da
   =\|\chi_\phi-\chi_\psi\|.
\]
The exact range consists of decreasing right-continuous integrable
\(f:(0,\infty)\to\mathbb N_0\) in (OR6). Conversely the eigenvalue formula
\(\lambda_j=\sup\{a:f(a)\ge j\}\) proves realization and
\(\sum_j\lambda_j=\int f\), as in SORB(SO26)–(SO27).
If the chosen semifinite trace is \(\alpha\operatorname{Tr}\), retain the corresponding value set \(\alpha\mathbb N_0\) and its trace-relative density; canonical chart covariance identifies the resulting core-center functional.

The continuous cone (OR4) has additional members. The profile
\(f(a)=\tfrac12 1_{(0,2)}(a)\) is decreasing, right-continuous, integrable with mass one, and gives a subinvariant functional by (OR6), but is not integer-valued. It is therefore absent from the type I∞ image. This is a range exception, not an exception to the isometry.

<a id="crng-separation"></a>
## 4. Separation of the entire center

First suppose \(M\) is type II∞ or III. [The resolvent-cone argument](OA-FLOW-CAPP.md#capp-resolvent), (CM12)–(CM13), proves that the positive resolvent averages
\[
 R\eta=\int_0^\infty e^{-t}\eta\theta_{-t}\,dt,\qquad\eta\in Z_*^+,
\]
belong to \(P_\theta\), and that their norm closure is \(P_\theta\).
Let \(z\in Z\) satisfy \(\chi(z)=0\) for every \(\chi\in P_\theta\).
Since the cone is invariant under every \(\theta_a\), also
\((R\eta)(\theta_a z)=0\) for all real \(a\). Write
\(h(a)=\eta(\theta_a z)\); this is bounded and continuous. Changing variables gives
\[
 0=e^a(R\eta)(\theta_a z)
   =\int_{-\infty}^a e^r h(r)\,dr\qquad(a\in\mathbb R).
\]
The integrand is continuous and integrable at \(-\infty\), so differentiation yields \(e^ah(a)=0\). In particular \(\eta(z)=0\) for every positive normal \(\eta\). Positive normal functionals separate \(Z\) (use vector functionals and polarization), hence \(z=0\). Full range (OR4) proves the asserted separation by the image.

For type I∞, use rank-one positive functionals of mass \(a>0\). Their profiles are \(1_{(0,a)}\). If \(z\) annihilates the whole image, then
\[
 \int_t^\infty e^{-q}z(q)\,dq=0\qquad(t\in\mathbb R),
\]
by putting \(a=e^{-t}\). Differences show that the integral of \(e^{-q}z(q)\) on every finite interval is zero. Its locally integrable density is therefore zero almost everywhere, for example by uniqueness of the scalar Radon–Nikodym derivative. Thus \(z=0\) in this case as well.

Equivalently, the norm-closed complex linear span of the image is \(Z_*\): if it were a proper closed subspace, Hahn–Banach and the concrete predual duality would supply a nonzero \(z\in Z\) annihilating it. This is a separation statement about normal functionals, not an algebra-generation assertion about them.

<a id="crng-checks"></a>
## 5. Exact consequences and checks

- The zero orbit maps to zero, and distance to that orbit is exactly \(\phi(1)\).
- For \(c=e^{-s}>0\), equation (OR3) reads
  \(\chi_{e^{-s}\phi}=e^{-s}\chi_\phi\theta_{-s}\), with both the mass factor and negative time retained.
- Equality of two invariants concerns closed orbits. It need not be attained by one unitary. Even on \(B(\ell^2)\), the densities with diagonal lists \((2^{-1},2^{-2},\ldots)\) and \((0,2^{-1},2^{-2},\ldots)\) have the same positive eigenvalues but different kernel dimensions.
- A scalar center has only two projections but has positive normal functionals of every nonnegative mass. The invariant in (OR1) therefore has the required codomain even in type III₁.

The human source is U. Haagerup and E. Størmer, [*Equivalence of Normal States on von Neumann Algebras and the Flow of Weights*](https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-haagerup/1990s/1990_Equivalence_of_normal_states_on_von_Neumann_algebras_and_the_flow_of_weights.pdf), Advances in Mathematics 83 (1990), 180–262, especially §§3–8. This theorem retains the separable-predual infinite-factor scope; it does not assert the paper's further arbitrary-cardinality extension.
