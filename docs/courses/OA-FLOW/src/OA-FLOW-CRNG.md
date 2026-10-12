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
## 5. Exact consequences and projection coordinates

- The zero orbit maps to zero, and distance to that orbit is exactly \(\phi(1)\).
- For \(c=e^{-s}>0\), equation (OR3) reads
  \(\chi_{e^{-s}\phi}=e^{-s}\chi_\phi\theta_{-s}\), with both the mass factor and negative time retained.
- Equality of two invariants concerns closed orbits. It need not be attained by one unitary. Even on \(B(\ell^2)\), the densities with diagonal lists \((2^{-1},2^{-2},\ldots)\) and \((0,2^{-1},2^{-2},\ldots)\) have the same positive eigenvalues but different kernel dimensions.
- A scalar center has only two projections but has positive normal functionals of every nonnegative mass. The invariant in (OR1) therefore has the required codomain even in type III₁.

<a id="crng-projection-coordinates"></a>
### Central projections as countable coordinates

Fix a faithful normal state \(\rho\) on \(Z\). Such a state exists: the regular core embeds in \(M\bar\otimes B(L^2(\mathbb R))\). The tensor-functional density argument in [CAPP, Section 2](OA-FLOW-CAPP.md#capp-lift), together with the separability of \(M_*\) and of the trace-class operators on \(L^2(\mathbb R)\), makes the ambient predual separable. The normal restriction quotients in [CP6](OA-FLOW-CP.md#oa-flow.cp.6) give separability for \(C_*\) and \(Z_*\). The explicit faithful-state construction in [HC7](OA-FLOW-HC.md#oa-flow.hc.7) then applies.

For the required separable Hilbert realization, [CR8](OA-FLOW-CR.md#oa-flow.cr.8) sends a countable norm-dense set of positive normal functionals of \(M\) to a dense set in its standard cone, since \(\|\xi_f-\xi_g\|^2\le\|f-g\|\). [CR1](OA-FLOW-CR.md#oa-flow.cr.1) proves that the complex span of that cone is the full standard Hilbert space. It is therefore separable, as is the regular core space \(L^2(\mathbb R,H)\). In particular its represented center satisfies DC06's separable-Hilbert-space hypothesis.

Use the abelian realization in [DC06](../../OA-MOD/OA-MOD-DC.html#realizing-an-abelian-algebra-as-the-diagonal-algebra) and the finite-measure density proof in [DC05](../../OA-MOD/OA-MOD-DC.html#a-finite-radon-nikodym-density-from-hilbert-representation). They give a unique nonnegative \(g_\phi\in L^1(Z,\rho)\) with
\[
 \chi_\phi(z)=\rho(g_\phi z),\qquad
 \rho(g_\phi)=\phi(1),\qquad
 \|\chi_\phi-\chi_\psi\|=\rho(|g_\phi-g_\psi|).
 \tag{OR7}
\]
The last equality follows by testing the bounded sign of the real density difference; the reverse inequality is the integral triangle inequality. Faithfulness of \(\rho\) identifies its null sets with the null projections of \(Z\).

For every positive rational \(r\), define
\[
 p_{\phi,r}=1_{(r,\infty)}(g_\phi)\in\operatorname{Proj}(Z),\qquad
 \mathbf p_\rho(\phi)=(p_{\phi,r})_{r\in\mathbb Q_{>0}}.
 \tag{OR8}
\]
The densities are finite almost everywhere, so their rational strict superlevel sets determine them. Explicitly, outside the union of the countably many null sets where two corresponding cuts differ, distinct finite density values would have a positive rational strictly between them. Thus the coordinate families coincide exactly when \(g_\phi=g_\psi\), equivalently \(\chi_\phi=\chi_\psi\), equivalently the norm-closed unitary orbits coincide by (OR2). This includes zero and all nonfaithful functionals.

Represent \(Z\) on \(L^2(Z,\rho)\), and give its projection space the strong-operator Borel structure, metrized by \(d_\rho(p,q)=\rho(|p-q|^2)^{1/2}\). On uniformly bounded multiplication operators, convergence in \(L^2(\rho)\) implies strong convergence: truncate any test vector to a bounded vector, use the \(L^2\) bound on that part, then use the common operator bound on the remaining vector tail. Conversely strong convergence tested on the constant vector gives \(L^2\) convergence. This also proves the asserted description on the projection space.

Each map \(\phi\mapsto p_{\phi,r}\) is Borel. Indeed (OR7) and contraction of \(\chi\) make \(\phi\mapsto g_\phi\) continuous from the positive predual norm into \(L^1(\rho)\). Put
\[
 F_{n,r}(t)=\min(1,n(t-r)_+).
\]
For nonnegative \(g,h\),
\(\|F_{n,r}(g)-F_{n,r}(h)\|_2^2\le n\|g-h\|_1\),
since the function has Lipschitz constant \(n\) and its values lie in \([0,1]\). Hence these bounded-operator maps are continuous. Dominated convergence gives \(F_{n,r}(g)\to1_{(r,\infty)}(g)\) strongly. A pointwise limit of Borel maps into the metric space of positive contractions with metric \(d_\rho\) is Borel: distance to every closed set is the limit of the corresponding distances, and open sets can be tested by positive distance to their complements. The countable product map in (OR8) is consequently Borel.

The coordinate projections from the **full positive predual** generate \(Z\). Let \(B\) be the von Neumann algebra they generate. All \(g_\phi\) are measurable for \(B\), because their rational spectral cuts lie in \(B\). Section 4 proves that the complex linear span of the \(\chi_\phi\) is norm dense in \(Z_*\); by (OR7), the same density holds for the span of the \(g_\phi\) in \(L^1(\rho)\). Given a selfadjoint \(z\in Z\), \(\|z\|\le K\), approximate it in \(L^1\) by real linear combinations of the \(g_\phi\), taking real parts of complex approximations. Clip those combinations to \([-K,K]\). The clipped functions belong to \(B\), and clipping cannot increase their pointwise distance from \(z\). Thus they converge to \(z\) in \(L^1\), hence in \(L^2\) by the common bound, and strongly by the preceding vector-tail argument. Strong closedness gives \(z\in B\), proving \(B=Z\).

### Scalar covariance and the role of the domain

For real \(s\), let \(d_s=d(\rho\theta_s)/d\rho\). It is positive and finite almost everywhere, because both states are faithful. For a nonnegative density \(g\), first use bounded cutoffs and then monotone convergence to obtain
\[
 (g\rho)\theta_s(z)=\rho\bigl(d_s\,\theta_{-s}(g)\,z\bigr)
 \qquad(z\in Z_+).
\]
Indeed the right side is \((\rho\theta_s)(\theta_{-s}(g)z)=\rho(g\theta_s(z))\). Formula (OR3) therefore becomes
\[
 g_{c\phi}=c\,d_{\log c}\,\theta_{-\log c}(g_\phi),\qquad
 p_{c\phi,r}=1_{(r,\infty)}
       \bigl(c\,d_{\log c}\,\theta_{-\log c}(g_\phi)\bigr)
 \quad(c>0).
 \tag{OR9}
\]
The products are products of commuting measurable functions, and the displayed integral proves their integrability. At \(c=0\) every coordinate is zero. For a state \(\phi\), the functional \(e^{-s}\phi\) has mass \(e^{-s}\), so it belongs to the state space only when \(s=0\). The positive-predual domain and the density factor in (OR9) are therefore part of the statement.

State inputs alone need not generate the center by these coordinates. For \(M=B(\ell^2)\), a trace-class state density has every eigenvalue at most one. Formula (OR6) makes \(\chi_\phi\), and hence \(g_\phi\), vanish on the half-line \(q\le0\). All its positive spectral cuts vanish there. Their generated unital algebra restricts to scalars on that half-line, whereas \(L^\infty(\mathbb R)\) contains nonconstant functions supported there. Thus the generation theorem just proved genuinely requires the full positive domain.

The single spectral projection \(e_\phi\) of (OR1) is a different object: it lies in \(C\) and need not be central or constant on a unitary orbit. In the same type I example, the vector state at a basis vector \(e_j\) has
\(e_\phi=|e_j\rangle\langle e_j|\otimes1_{(0,\infty)}(q)\).
Matrix units show this projection is noncentral; exchanging two basis vectors changes it within one state orbit. The central functional in (OR1) is unchanged.

Finally, no map into \(\operatorname{Proj}(Z)\) alone can separate all positive-functional orbits for every infinite factor. In type III₁, \(Z=\mathbb C\) has only two projections, while (OR5) gives distinct orbits for any three distinct positive masses. The family (OR8) has the stated separation property. Its countable-coordinate assertion is distinct from a single-projection coding of the mass-one orbit space.

<a id="crng-single-projection"></a>
### One central projection for each closed state orbit

There does exist a Borel map
\[
 p:S_*(M)\longrightarrow\operatorname{Proj}(Z)
 \tag{OR10}
\]
such that \(p(\phi)=p(\psi)\) exactly when the closed state orbits coincide, and \(p(S_*(M))\) generates \(Z\). The following explicit coding proves existence. It is a choice of labels; its projections need not be the spectral projections in (OR1) or (OR8).

First \(Z\) is either scalar or diffuse. [CORE8](OA-FLOW-CORE.md#core-8) proves \(Z^\theta=\mathbb C1\) because \(M\) is a factor. If \(e\) is a nonzero minimal projection of \(Z\), each \(\theta_s(e)\) is either \(e\) or is orthogonal to \(e\). In the latter case
\(\rho(|\theta_s(e)-e|^2)\ge\rho(e)>0\).
Continuity makes \(\theta_s(e)=e\) for all sufficiently small \(s\). Dividing any real \(s\) into sufficiently small equal increments proves invariance for every \(s\). Ergodicity gives \(e=1\), and minimality of \(1\) means \(Z=\mathbb C1\). In this scalar case (OR2) makes all states have the same closed orbit, so \(p(\phi)=1\) proves (OR10) and generation.

Suppose now \(Z\) is diffuse. DC06 supplies a bounded positive selfadjoint generator \(h\) of \(Z\). Its spectral probability measure
\(\mu(E)=\rho(1_E(h))\) has no atoms: a nonzero projection \(1_{\{a\}}(h)\) would be minimal in \(Z=\{h\}''\). Thus the distribution
\(F(a)=\mu((-\infty,a])\) is continuous. For \(0<t<1\), put
\[
 q_t=\inf\{a:F(a)\ge t\},\qquad P_t=1_{(-\infty,q_t]}(h).
\]
The bounded support and continuity of \(F\) give \(F(q_t)=t\), so \(\rho(P_t)=t\). The projections are nested and
\(d_\rho(P_t,P_v)^2=|t-v|\); hence \(t\mapsto P_t\) is continuous and injective. They generate \(Z\) even if only rational parameters are retained. Indeed
\[
 1_{(-\infty,a]}(h)
 =\bigvee_{\substack{t\in\mathbb Q\\0<t<F(a)}} P_t .
\]
The right side is below the left and has the same \(\rho\)-value \(F(a)\), by normality; faithfulness proves equality. The formula includes the cases \(F(a)=0\) and \(F(a)=1\). All spectral projections of the generator therefore belong to the generated algebra.

We need a sequence \((\chi_n)\) of distinct invariants of states. In type I∞, take trace-class densities with the two positive eigenvalues
\(1/2+1/(n+2)\) and \(1/2-1/(n+2)\), \(n\ge1\); (OR6) separates their orbits. In type II∞ or III, the unit-mass slice of \(P_\theta\) is convex and is exactly the state image by (OR4) and mass preservation. It cannot be a singleton: then the full cone would be a single ray, and Section 4's dense-span conclusion would make \(Z_*\), hence \(Z\), one-dimensional. Take two distinct points in that slice and their convex combinations with coefficients \(1/(n+1)\). These give the required sequence; every \(\chi_n\) is realized by a state.

Choose a countable norm base \((B_j)\) for the separable metric space \(Z_*\), using rational-radius balls about a countable dense set. Membership in these balls separates points. Let \(a_j=1\) when \(j\) is a power of two and \(a_j=0\) otherwise, and set
\[
 b(\chi)=\sum_{j\ge1}
 \left(3^{-(2j-1)}1_{B_j}(\chi)+3^{-2j}a_j\right).
\]
The series is uniformly convergent, so \(b\) is Borel. The first differing ternary digit dominates the remaining tail, hence \(b\) is injective. Its values lie in \((0,1)\) and are irrational. To verify the latter assertion, a rational number has an eventually periodic base-three expansion, by the finite-remainder long-division algorithm; the terminating expansion has the same property. Our expansion has only digits zero and one, and its even-position subsequence is \((a_j)\), which is not eventually periodic because it has infinitely many ones and unbounded gaps between them. Thus this expansion cannot represent a rational number.

Enumerate the rational numbers in \((0,1)\) without repetition as \((t_n)\). Modify the code only at the selected invariants:
\[
 \beta(\chi)=
 \begin{cases}
 t_n,&\chi=\chi_n,\\
 b(\chi),&\chi\notin\{\chi_n:n\ge1\}.
 \end{cases}
\]
Singletons are norm closed, so the countable modification is Borel. It stays injective: the exceptional values are distinct rationals, and every other value is irrational. Now define
\[
 p(\phi)=P_{\beta(\chi_\phi)} .
 \tag{OR11}
\]
This is Borel by the continuity of \(\phi\mapsto\chi_\phi\) and \(t\mapsto P_t\). Injectivity of the two scalar codes and (OR2) prove exactly the equivalence in (OR10). The state image contains every \(P_{t_n}\), since every \(\chi_n\) is realized. The rational-parameter argument proves that this image generates \(Z\).

<a id="crng-scaling-extension"></a>
### Extend the state labels before applying scalar multiplication

Define a map on all positive normal functionals by
\[
 \widehat p(0)=0,\qquad
 \widehat p(\phi)=
 \theta_{-\log m}\bigl(p(\phi/m)\bigr),\qquad m=\phi(1)>0.
 \tag{OR12}
\]
It agrees with \(p\) on states. The map is Borel, including at zero. Mass and normalization are continuous on the punctured positive cone. For completeness the flow is jointly continuous on \(\mathbb R\times\operatorname{Proj}(Z)\): if \(s_n\to s\) and \(e_n\to e\) in \(d_\rho\), then
\[
 \rho\theta_{s_n}(|e_n-e|^2)
 \le\|\rho\theta_{s_n}-\rho\theta_s\|
       +\rho\theta_s(|e_n-e|^2)\longrightarrow0.
\]
The first term tends to zero by the predual norm-continuity proof in [CAPP's resolvent section](OA-FLOW-CAPP.md#capp-resolvent). For the second, write \(\rho\theta_s=d_s\rho\), truncate \(d_s\), and use \(0\le|e_n-e|^2\le1\). Pointwise continuity of \(s\mapsto\theta_s(e)\), followed by the triangle inequality, proves joint continuity. Thus (OR12) is a composition of Borel maps on the punctured cone, with the Borel singleton zero handled separately.

For every real \(s\) and every positive normal \(\phi\), direct substitution gives
\[
 \widehat p(e^{-s}\phi)=\theta_s(\widehat p(\phi)).
 \tag{OR13}
\]
For nonzero \(\phi\), its normalized state is unchanged by this scaling, while its new mass is \(e^{-s}m\); the group parameter in (OR12) becomes \(s-\log m\). For zero both sides are zero. This is the scalar-equivariant projection statement with a domain on which both sides are defined.

Only the state restriction was asserted to separate orbits by a projection alone. On the whole positive cone the pair
\((\phi(1),\widehat p(\phi))\) separates closed orbits: equal positive masses let us undo the same \(\theta_{-\log m}\) and apply the state result; mass zero forces both functionals to be zero. Conversely equal closed positive orbits have equal masses and equal normalized closed state orbits. In the scalar-center case, \(\widehat p\) is simply one on every nonzero functional, illustrating why that additional mass coordinate cannot be discarded.

A normal conjugacy of center flows transports these projections to any other normal flow chart. It preserves their equality and generated von Neumann algebra. It also preserves the bounded strong Borel structure: the defining normal-positive-functional seminorms pull back along the isomorphism and its normal inverse. Intertwining the two actions transports (OR13) with the same parameter and sign.

The human source is U. Haagerup and E. Størmer, [*Equivalence of Normal States on von Neumann Algebras and the Flow of Weights*](https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-haagerup/1990s/1990_Equivalence_of_normal_states_on_von_Neumann_algebras_and_the_flow_of_weights.pdf), Advances in Mathematics 83 (1990), 180–262, especially §§3–8. This theorem retains the separable-predual infinite-factor scope; it does not assert the paper's further arbitrary-cardinality extension.
