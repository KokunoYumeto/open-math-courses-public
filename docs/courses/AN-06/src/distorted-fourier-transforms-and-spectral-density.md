# Distorted Fourier transforms and spectral density

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: How does a shell observation become a spectral transform?** At one energy the observation is an amplitude on a surface; over an interval it is a function of momentum. The coarea factor connects these descriptions. In the free square example there are two momenta at each positive energy, whereas the bound-state example requires removing a discrete spectral component before claiming a norm identity.

Resolvent boundary values determine the continuous spectral measure. Their free Fourier traces can be assembled into measurable functions of momentum, giving two distorted Fourier transforms. These maps preserve the norm of the continuous part and turn the perturbed operator into multiplication by the free polynomial.

<a id="distorted-setting"></a>

Retain the hypotheses of [Limiting absorption and point spectrum](limiting-absorption-and-point-spectrum.md): a real simply characteristic \(p\) without invariant directions, a symmetric short-range differential \(V\), and the self-adjoint closure \(H\) of \(p(D)+V\) on \(\mathcal S\). Write

\[
 \Sigma=Z(p)\cup\mathcal A,\quad
 \Omega=\mathbb R\setminus\Sigma,\quad
 M_\lambda=\{\xi:p(\xi)=\lambda\},\quad
 g(\xi)=|\nabla p(\xi)|.
\tag{1}
\]

The [exceptional-set proof](limiting-absorption-and-point-spectrum.md#limiting-absorption-discrete) shows that \(\Sigma\) is closed and countable. Since \(n\geq1\) and \(p\) has no invariant directions, \(p\) is nonconstant: a constant polynomial would be invariant under every translation. For \(\lambda\in\Omega\) define the strongly continuous \(B\)-valued forcing

\[
 a_\pm(\lambda,f)=(I+VR_{0,\pm}(\lambda))^{-1}f,
 \qquad f\in B.
\tag{2}
\]

Use the unitary Fourier transform
\(\widehat f(\xi)=(2\pi)^{-n/2}\int e^{-ix\cdot\xi}f(x)\,dx\).
The canonical trace \(T_\lambda:B\to L^2(M_\lambda,dS)\) is from [Global radiation and flux](global-radiation-and-flux.md). An \(L^2\) Fourier representative by itself need not have a meaningful restriction to \(M_\lambda\).

The functional-analysis prerequisite is the full local proof of [Self-adjoint spectral calculus with the original domain](../providers/analysis/self-adjoint-spectral-domains.md#self-adjoint-pvm-domain). Its Cayley-transform construction gives the unique projection-valued measure, bounded Borel calculus and every maximal unbounded multiplier domain for an arbitrary self-adjoint operator, with \(D(H)=\{f:\int t^2\,d(E(t)f,f)<\infty\}\) equal to the original operator domain. Neither a lower bound nor separability is assumed. Write \(E\) for the spectral measure of \(H\) and

\[
 \mu_f(A)=(E(A)f,f),\qquad
 E^d=E(\Sigma),\quad E^c=E(\Omega).
\tag{3}
\]

For further reading on spectral calculus and inversion, see Teschl [T], Sections 3.1 and 3.4; for perturbed spectral representations, see Kuroda [K], Section 4.2.

## 1. Continuous test functions recover the spectral measure

This is the continuous-test counterpart of the interval formula in [Resolvents, domains and spectral density](resolvents-domains-and-spectral-density.md), Section 4. Here the explicit general spectral prerequisite permits a free polynomial and its perturbation to be unbounded in both spectral directions.

<a id="distorted-poisson"></a>

**Lemma 1.1.** For a self-adjoint \(H\), \(f\in L^2\) and real \(\chi\in C_c(\mathbb R)\),

\[
 \int\chi\,d\mu_f
 =\lim_{\varepsilon\downarrow0}
      \frac{\pm1}{\pi}\int_{\mathbb R}
       \chi(\lambda)\operatorname{Im}
          ((H-\lambda\mp i\varepsilon)^{-1}f,f)\,d\lambda.
\tag{4}
\]

**Proof.** By the spectral theorem the signed imaginary part of the resolvent pairing is

\[
 \pm\operatorname{Im}((H-\lambda\mp i\varepsilon)^{-1}f,f)
       =\int_{\mathbb R}
            \frac{\varepsilon}{(t-\lambda)^2+\varepsilon^2}\,d\mu_f(t).
\tag{5}
\]

The [arctangent normalization](../providers/analysis/elementary-functions-and-cutoffs.md#arctangent-and-poisson-kernel) gives integral \(\pi\) for this kernel in \(\lambda\), while \(\mu_f(\mathbb R)=\|f\|_2^2\). The [general product theorem](../providers/analysis/finite-derivative-l2.md#general-tonelli-fubini), applied to the finite spectral measure and Lebesgue measure, therefore justifies Fubini even for a signed bounded \(\chi\). The right side of (4) before its limit is
\(\int(P_\varepsilon*\chi)(t)\,d\mu_f(t)\), where
\[
 P_\varepsilon(s)=\frac{\varepsilon}{\pi(s^2+\varepsilon^2)}.
\]
This convolution converges uniformly to \(\chi\). Indeed, given \(\delta>0\), the integral on \(|s|\leq\delta\) is bounded by the uniform modulus of continuity \(\omega_\chi(\delta)\). On its complement the error is bounded by \(2\|\chi\|_\infty\) times a kernel mass at most \(2\varepsilon/(\pi\delta)\). Let \(\varepsilon\to0\), then \(\delta\to0\). Integration against the finite measure proves (4). \(\square\)

<a id="distorted-density"></a>

**Theorem 1.2.** For \(f\in B\), the restriction of \(\mu_f\) to \(\Omega\) has a nonnegative continuous density. With either sign it is

\[
 q_f(\lambda)
 =\int_{M_\lambda}
        |T_\lambda a_\pm(\lambda,f)(\xi)|^2
                     \frac{dS(\xi)}{g(\xi)}
 =\frac{\pm1}{\pi}\operatorname{Im}(R_{H,\pm}(\lambda)f,f).
\tag{6}
\]

**Proof.** Let \(a=a_\pm(\lambda,f)\) and \(u=R_{0,\pm}(\lambda)a=R_{H,\pm}(\lambda)f\). The factorization says \(f=a+Vu\). The [extended endpoint symmetry](self-adjoint-short-range-operators.md#short-range-endpoint-symmetry) makes \((u,Vu)\) real. Hence
\[
 \operatorname{Im}(u,f)=\operatorname{Im}(u,a).
\]
The [free forcing-flux formula](global-radiation-and-flux.md#global-amplitude-flux) gives
\[
 \pm2\operatorname{Im}(u,a)
      =2\pi\int_{M_\lambda}|T_\lambda a|^2\,dS/g,
\]
proving the second equality in (6) and its nonnegativity. All pairings converge because \(u\in X_p\subset B^*\) and \(f,a,Vu\in B\). The threshold estimate bounds \(1/g\) uniformly on compact regular energy sets; consequently the integral is finite.

For real \(\chi\in C_c(\Omega)\), limiting absorption bounds \(R_H(\lambda\pm i\varepsilon):B\to B^*\) uniformly on a compact neighborhood of its support. It also makes the pairing on a fixed \(f\) continuous up to the boundary. Dominated convergence in (4) therefore gives

\[
 \int\chi\,d\mu_f=\int_\Omega\chi(\lambda)q_f(\lambda)\,d\lambda.
\tag{7}
\]

The last expression in (6) is continuous, by weak-star continuity of the resolvent against \(f\in B\). Thus \(q_f\) is continuous. Equality for compact continuous tests determines the measures on \(\Omega\). Indeed, if \((a,b)\) has compact closure in \(\Omega\), the continuous tents \(\min\{1,k\operatorname{dist}(\lambda,\mathbb R\setminus(a,b))\}\) increase to its indicator. Monotone convergence gives equality on that interval. Fix such an interval \(U\); both measures are finite there, and the same argument gives equality on every relatively open subinterval of \(U\), including \(U\) itself. These intervals are closed under finite intersections and generate the Borel sets of \(U\). The [finite-measure uniqueness proof](../providers/analysis/finite-derivative-l2.md#pi-lambda-uniqueness) therefore gives equality on all those Borel sets. Countably many such intervals cover \(\Omega\); disjointifying that cover and using countable additivity gives the claim on all of \(\Omega\). Both signs in (7) give the same measure and continuous density, so their two expressions in (6) agree at every \(\lambda\in\Omega\). \(\square\)

The factor \(1/\pi\) in (6) and the factor \(2\pi\) in free flux cancel. The unitary Fourier convention leaves no further factor in the surface density.

<a id="distorted-bound-only"></a>

Absolute continuity alone already follows from the locally uniform \(B\)-to-\(B^*\) bound in the limiting-absorption lesson. Indeed, on a compact good-energy interval it bounds the positive scalar imaginary part by \(C_I\|f\|_B^2\). Apply the positive-kernel proof of Theorem 5.1 in [Resolvents, domains and spectral density](resolvents-domains-and-spectral-density.md#u001-weighted-spectral-density), using the general spectral measure supplied here. It gives a density bounded locally by \(C_I\|f\|_B^2/\pi\); dense \(B\) tests then exclude singular spectral mass on \(\Omega\). The boundary convergence and free flux calculation above give the stronger continuous density and its exact surface formula (6), which are needed for the spectral transform.

## 2. Choosing measurable functions with the prescribed surface traces

<a id="distorted-parameter-partition"></a>

The change-of-variables and surface-measure facts used here are proved in [Coordinate inverses and integration, CI1–CI7](../providers/analysis/coordinate-inverses-and-integration.md#coordinate-integration). We also give the parameter partition construction, including the extra time parameter used in the next lesson. For any open \(O\subset\mathbb R^d\), put
\[
 K_m=\{x\in O:|x|\leq m,\ \operatorname{dist}(x,\mathbb R^d\setminus O)\geq1/m\},
 \qquad m\geq1,
\]
with distance to the empty set taken as infinity and \(K_0=K_{-1}=\varnothing\). These compact sets exhaust \(O\) and \(K_m\subset\operatorname{int}K_{m+1}\). Given an open cover of \(O\), cover each compact band \(K_m\setminus\operatorname{int}K_{m-1}\) by finitely many balls whose slightly larger closed balls lie in a member of that cover and in \(\operatorname{int}K_{m+1}\setminus K_{m-2}\). This is possible because the band is disjoint from \(K_{m-2}\). Choose a smooth nonnegative bump supported in each larger ball and positive on the corresponding smaller ball. The collection is locally finite: a neighborhood of any point lies in some \(\operatorname{int}K_M\), and every sufficiently late ball avoids \(K_M\). The sum of the bumps is smooth and strictly positive on \(O\). Dividing each bump by their sum gives the required locally finite smooth partition with supports subordinate to the cover. This proof works for \(d=1\) here and \(d=2\) for the energy-time parameter.

<a id="distorted-measurable-assembly"></a>

**Lemma 2.1.** For each \(f\in B\), there are measurable functions \(J_\pm f\) on \(\mathbb R^n\) such that, for every \(\lambda\in\Omega\),

\[
 (J_\pm f)|_{M_\lambda}=T_\lambda a_\pm(\lambda,f)
       \quad\text{for almost every point of }M_\lambda.
\tag{8}
\]

They are unique up to Lebesgue-null sets. They may be chosen to vanish on \(p^{-1}(\Sigma)\).

**Proof.** Fix a sign and write \(a(\lambda)=a_\pm(\lambda,f)\), a continuous \(B\)-valued function on \(\Omega\). For each integer \(j\geq1\), construct a continuous \(B\)-valued approximation \(h_j(\lambda)\), each of whose values has smooth compact Fourier support, with
\[
 \|h_j(\lambda)-a(\lambda)\|_B\leq2^{-j}
       \quad(\lambda\in\Omega).
\tag{9}
\]
Here are the details. Schwartz functions are dense in \(B\) by the shell approximation in [Endpoint spaces and flat energy shells](endpoint-spaces-and-flat-energy-shells.md). For a Schwartz function, multiplying its Fourier transform by a smooth cutoff equal to one on a ball of radius tending to infinity converges in every Schwartz seminorm, by Leibniz and its rapidly decreasing derivatives. [Fourier inversion on Schwartz space](../providers/analysis/finite-derivative-l2.md#fourier-normalization) preserves this convergence. For its implication in \(B\), let \(v\in\mathcal S\) and choose an integer \(N>(n+1)/2\). The shell of radius \(R_\ell=2^\ell\) has volume at most \(C_nR_\ell^n\). Thus its contribution to \(\|v\|_B\) is at most \(C_{n,N}R_\ell^{(n+1)/2-N}\sup_x(1+|x|)^N|v(x)|\), with the inner shell bounded by the same seminorm. The geometric series converges. Consequently convergence in Schwartz space implies convergence in \(B\). Thus \(\mathcal F^{-1}C_c^\infty\) is dense in \(B\). At each parameter choose a member of this subspace approximating \(a\) within \(2^{-j-2}\); continuity gives a neighborhood on which the same member approximates \(a\) within \(2^{-j-1}\). Apply the partition construction above to this cover and take the corresponding convex combinations of the chosen members. Only finitely many terms occur near each parameter, so \(h_j\) is continuous in \(B\) and its Fourier values are jointly measurable in \((\lambda,\xi)\). Its value at every fixed parameter is a finite sum of smooth compact Fourier functions. Convexity proves (9).

Define on \(p^{-1}(\Omega)\)
\[
 G_j(\xi)=\widehat{h_j(p(\xi))}(\xi).
\tag{10}
\]
Each \(G_j\) is continuous on \(p^{-1}(\Omega)\): locally in the energy parameter the defining partition has only finitely many terms, each a smooth parameter coefficient times a smooth Fourier function. In particular it is Borel measurable. On \(M_\lambda\) it is the classical Fourier restriction of \(h_j(\lambda)\). Uniform trace bounds on compact regular energy intervals give
\[
 \|G_j|_{M_\lambda}-T_\lambda a(\lambda)\|_{L^2(dS)}
       \leq C_I2^{-j},\qquad \lambda\in I\Subset\Omega.
\tag{11}
\]
In particular, for every fixed \(\lambda\), the sum of the \(L^2(dS)\) norms of the successive differences is finite. The nonnegative sums \(\sum_j|G_{j+1}-G_j|\) have uniformly bounded \(L^2\) norm on that surface by the triangle inequality; monotone convergence makes the full sum finite almost everywhere. Thus \(G_j\) converges pointwise almost everywhere on each fixed \(M_\lambda\). Its \(L^2\) limit is the trace in (11).

Define \(J_\pm f(\xi)\) to be this pointwise limit wherever it exists in \(p^{-1}(\Omega)\), and zero elsewhere. The convergence set is Borel by the countable Cauchy criterion; on it the real and imaginary limits are Borel functions. Extending by zero is therefore Borel measurable. This proves (8) for every regular \(\lambda\in\Omega\), with a possibly different exceptional surface-null set for each \(\lambda\).

<a id="distorted-polynomial-null"></a>

For the assertion in ambient measure, use the local energy coordinate \(p(\xi)\) and the coarea formula
\[
 \int_{p^{-1}(\Omega)}F(\xi)\,d\xi
 =\int_\Omega\int_{M_\lambda}F(\xi)\,\frac{dS(\xi)}{g(\xi)}\,d\lambda,
 \qquad F\geq0.
\tag{12}
\]
On compact subsets of \(p^{-1}(\Omega)\), \(g\) is bounded below and (11) supplies the required locally integrable estimates. For the Jacobian explicitly, where \(\partial_1p\ne0\) write \(\xi=(h(\lambda,\eta),\eta)\). Implicit differentiation gives \(\partial_\lambda h=(\partial_1p)^{-1}\) and \(\nabla_\eta h=-\nabla_\eta p/\partial_1p\). Hence the energy-coordinate volume Jacobian is \(1/|\partial_1p|\), while
\[
 \frac{dS}{g}
 =\frac{\sqrt{1+|\nabla_\eta h|^2}}{|\nabla p|}\,d\eta
 =\frac{d\eta}{|\partial_1p|}.
\]
The usual change-of-variables theorem in these coordinate patches and a partition of unity yield (12); increasing compact cutoffs gives its full nonnegative form. Surface-null sets at every \(\lambda\) therefore give an ambient null set. Also each level set \(p^{-1}(\lambda)\) has Lebesgue measure zero, since \(p-\lambda\) is a nonzero polynomial. Here is the full elementary argument. A nonzero one-variable polynomial of degree \(d\) has at most \(d\) distinct roots: if \(a\) is a root, the identities \(t^k-a^k=(t-a)\sum_{r=0}^{k-1}t^{k-1-r}a^r\) factor out \(t-a\), and induction on the degree applies to the other roots. A nonzero constant has none. In dimension \(n>1\), write a nonzero polynomial as \(Q(x',t)=\sum_{r=0}^d c_r(x')t^r\) and select one coefficient which is not the zero polynomial. By dimension induction its zero set in \(x'\) is null. Outside this null set the section in \(t\) has only finitely many roots. Inside any bounded box the zero-set indicator is Borel, its one-dimensional section integral is zero outside the exceptional set, and is bounded by the box length on that set. Tonelli therefore gives zero volume in the box. A countable union of boxes proves the claim in all of \(\mathbb R^n\). Since \(\Sigma\) is countable, \(p^{-1}(\Sigma)\) is null. These facts prove uniqueness almost everywhere and justify the prescribed zero values. \(\square\)

The construction uses canonical \(B\) traces before taking a diagonal in energy and frequency. It preserves the statement on every good surface, as required for subsequent energy-by-energy formulas.

## 3. The norm identity and the two spectral parts

<a id="distorted-norm"></a>

**Theorem 3.1.** For \(f\in B\), \(J_\pm f\in L^2(d\xi)\), and

\[
 \|J_\pm f\|_{L^2(d\xi)}^2=\|E^cf\|_2^2.
\tag{13}
\]

The maps extend uniquely to bounded linear operators
\[
 J_\pm:L^2(dx)\longrightarrow L^2(d\xi).
\]
They vanish on \(E^dL^2\) and are isometries on \(E^cL^2\). The subspace \(E^dL^2\) is the closed span of all \(L^2\) eigenfunctions of \(H\), and \(E^cL^2=\mathcal H_{\mathrm{ac}}(H)\). Thus \(H\) has no singular continuous spectrum.

**Proof.** Exhaust \(\Omega\) by compact continuous tests \(0\leq\chi_k\uparrow1\). Such a sequence exists because \(\Omega\) is open: use an increasing cutoff in \(|\lambda|\) and an increasing cutoff which vanishes where \(\operatorname{dist}(\lambda,\Sigma)\leq1/k\). If \(\Sigma\) is empty, only the first cutoff is needed. Monotone convergence in (7), followed by (8) and (12), gives
\[
 \|E^cf\|_2^2
 =\int_\Omega q_f(\lambda)\,d\lambda
 =\int_{p^{-1}(\Omega)}|J_\pm f(\xi)|^2\,d\xi.
\]
The prescribed values off \(p^{-1}(\Omega)\) prove (13). Linearity holds as an \(L^2\) identity: the canonical traces in (8) are linear in \(f\), so coarea and uniqueness identify the representative for a linear combination with that linear combination of representatives. Formula (13) bounds these operators by one on the dense subspace \(B\subset L^2\), giving their unique bounded extensions. Passing to \(L^2\) limits preserves (13), which shows that they vanish on \(E^dL^2\) and preserve norm on its orthogonal complement.

<a id="distorted-spectral-parts"></a>

For an atom \(\lambda\), the spectral theorem gives
\[
 E(\{\lambda\})L^2=\ker(H-\lambda).
\tag{14}
\]
Indeed a vector in the range has spectral measure supported at \(\lambda\), hence finite second moment and \((H-\lambda)\) norm zero. Conversely an eigenvector has \(\int|t-\lambda|^2\,d\mu=0\), so its measure is supported at \(\lambda\) and it belongs to that range. Countable strong additivity over \(\Sigma\) now makes \(E^dL^2\) the closed span of the corresponding eigenspaces. The previous lesson identifies every eigenvalue outside \(Z(p)\) with \(\mathcal A\), so there are no eigenvectors in \(E^cL^2\), and all eigenvectors belong to \(E^dL^2\). No multiplicity or decay assertion at a threshold is needed here.

Let \(N\subset\Omega\) be a Lebesgue-null Borel set. Theorem 1.2 gives
\(\|E(N)f\|_2^2=\mu_f(N)=0\) for \(f\in B\). Density and boundedness of \(E(N)\) give \(E(N)=0\) on all \(L^2\). For \(u\in E^cL^2\), its spectral measure also vanishes on \(\Sigma\), so it is absolutely continuous on all of \(\mathbb R\). Conversely, for an absolutely continuous vector all singleton projections in the countable set \(\Sigma\) vanish; strong additivity gives \(E^du=0\), so \(u\in E^cL^2\). On \(E^dL^2\) all measures are countable sums of atoms. These orthogonal reducing parts sum to \(L^2\), excluding a singular continuous component. \(\square\)

Surjectivity of \(J_\pm:E^cL^2\to L^2(d\xi)\) will follow from comparison with the time-dependent wave operators. The present theorem proves its isometric range without assuming that comparison.

## 4. Intertwining the closed operator and its group

Let \(M_p\) be the maximal self-adjoint multiplication operator by \(p(\xi)\) on \(L^2(d\xi)\).

<a id="distorted-core"></a>

**Theorem 4.1.** For every \(f\in\mathcal D(H)\),

\[
 J_\pm f\in\mathcal D(M_p),\qquad
 J_\pm Hf=M_pJ_\pm f.
\tag{15}
\]

For every \(f\in L^2\) and \(t\in\mathbb R\),

\[
 J_\pm e^{itH}f=e^{itM_p}J_\pm f.
\tag{16}
\]

**Proof.** First take \(\phi\in\mathcal S\). Its initial operator image \(H\phi=p(D)\phi+V\phi\) belongs to \(B\): the polynomial part is Schwartz, while \(\phi\in X_p\) and the [short-range compact extension](short-range-compactness-and-local-tests.md#short-range-local-criterion) sends it into \(B\). At a regular energy,
\[
 R_{0,\pm}(\lambda)(P_0-\lambda)\phi=\phi.
\tag{17}
\]
For example, the nonreal identity is
\(R_0(z)(P_0-\lambda)\phi=\phi+(z-\lambda)R_0(z)\phi\); free endpoint bounds make its last term tend to zero distributionally as \(z\to\lambda\) on either side. Therefore
\[
 (H-\lambda)\phi
  =(I+VR_{0,\pm}(\lambda))(P_0-\lambda)\phi.
\]
Invert this equality at \(\lambda\in\Omega\). Taking the canonical Fourier trace of its right forcing gives
\[
 T_\lambda a_\pm(\lambda,(H-\lambda)\phi)
       =T_\lambda(P_0-\lambda)\phi=0.
\]
Linearity in the forcing, (8) and coarea imply
\[
 J_\pm H\phi(\xi)=p(\xi)J_\pm\phi(\xi)
       \quad\text{almost everywhere}.
\tag{18}
\]
In particular the right side is \(L^2\), proving domain membership for these core vectors.

<a id="distorted-domain"></a>

Since \(H\) is the closure of its Schwartz restriction, any \(f\in\mathcal D(H)\) has \(\phi_j\in\mathcal S\) with \(\phi_j\to f\) and \(H\phi_j\to Hf\) in \(L^2\). Boundedness of \(J_\pm\) gives \(J_\pm\phi_j\to J_\pm f\) and \(M_pJ_\pm\phi_j=J_\pm H\phi_j\to J_\pm Hf\). Multiplication by \(p\) is closed. To see this directly, from \(v_j\to v\) and \(pv_j\to w\) in \(L^2\) choose a common subsequence with \(\sum_k(\|v_{j_k}-v\|_2^2+\|pv_{j_k}-w\|_2^2)<\infty\). Tonelli makes both error sums finite almost everywhere, so both errors tend to zero there. Since \(p\) is finite everywhere, \(w=pv\) almost everywhere; hence \(v\) belongs to the maximal domain and has the required image. This proves (15).

<a id="distorted-group"></a>

For the group statement, the bounded spectral calculus gives domain invariance and differentiation on \(\mathcal D(H)\). They also follow directly from the second moment: multiplication by \(e^{it\lambda}\) preserves \(\int\lambda^2\,d\mu_f\), and \(|(e^{ih\lambda}-1)/h|\leq|\lambda|\) permits dominated convergence of the difference quotient. The same statements hold for \(M_p\). For \(f\in\mathcal D(H)\) differentiate the \(L^2(d\xi)\)-valued function
\[
 b(t)=e^{-itM_p}J_\pm e^{itH}f.
\]
To justify the product rule, write \(y(t)=J_\pm e^{itH}f\). It lies in \(D(M_p)\) by (15), has derivative \(iJ_\pm He^{itH}f\), and \(M_py(t)=J_\pm e^{itH}Hf\) is continuous. Split the difference quotient of \(e^{-itM_p}y(t)\) into the change of \(y\) multiplied by the nearby unitary and the change of the unitary on the fixed domain vector \(y(t)\). Strong continuity treats the first term and the domain derivative treats the second. Its derivative is
\[
 b'(t)=i e^{-itM_p}(J_\pm H-M_pJ_\pm)e^{itH}f=0.
\]
Thus \(b(t)=b(0)\), proving (16) on the domain. This domain is dense, and both sides are bounded on \(L^2\), so (16) holds for every \(f\). \(\square\)

<a id="distorted-free-square"></a>

**Example 4.2 (the free square).** For \(V=0\) and \(p(\xi)=\xi^2\) in one dimension, \(J_\pm=\mathcal F\). Indeed \(a_\pm(\lambda,f)=f\); for a Schwartz \(f\), (8) gives its ordinary Fourier values on every nonzero level. The excluded preimage of \(\Sigma\) is null by Lemma 2.1, so the two functions agree in ambient measure. Since both operators are bounded and Schwartz functions are dense in \(L^2\), the equality extends to every \(L^2\) vector. The free measure is absolutely continuous, and for \(\lambda>0\),

\[
 q_f(\lambda)=
 \frac{|\widehat f(\sqrt\lambda)|^2+
       |\widehat f(-\sqrt\lambda)|^2}{2\sqrt\lambda}.
\tag{19}
\]

For \(\lambda<0\) it is zero. Each one-point surface branch has zero-dimensional measure one, and \(g(\pm\sqrt\lambda)=2\sqrt\lambda\), which explains both terms. The threshold zero is excluded from the continuity assertion.

<a id="distorted-bound-state"></a>

**Example 4.3 (removing a bound state).** For \(H=-\partial_x^2-2\operatorname{sech}^2x\), [the bound-state example](limiting-absorption-and-point-spectrum.md#limiting-absorption-example) proves that \(u=\operatorname{sech}x\) is an eigenfunction at \(-1\). Its exponential bound \(|u(x)|\leq2e^{-|x|}\) also puts it in \(B\): in one dimension the outer shell contribution is at most \(C R_j e^{-R_j/2}\), a summable sequence. For example \(e^t\geq t^3/6\) bounds this by \(C R_j^{-2}\); the inner shell is finite. Thus \(E^cu=0\) and \(J_\pm u=0\) in \(L^2(d\xi)\). More precisely, (6) is continuous and nonnegative on \(\Omega\), and its integral for this \(u\) is zero. It vanishes at every \(\lambda\in\Omega\), so \(T_\lambda a_\pm(\lambda,u)=0\) on every such surface. The distorted transform removes the bound state by its energy-dependent forcing correction.

### Use the conclusion

Check the sign of the Poisson formula, then the exact coarea density and the operator domain after transformation. The transform's isometry on continuous states is a separate step from the later onto theorem.

<a id="distorted-exercises"></a>

## 5. Exercises

**Exercise 5.1 (foundation).** Prove the estimate
\[
 \|P_\varepsilon*\chi-\chi\|_\infty
 \leq\omega_\chi(\delta)
           +\frac{4\varepsilon\|\chi\|_\infty}{\pi\delta}.
\]
Explain why it applies uniformly even when the centre \(t\) lies outside the support of \(\chi\).

**Exercise 5.2 (foundation).** Derive (19) by changing variables separately on \(\xi>0\) and \(\xi<0\). Verify that its integral over \(\lambda>0\) equals \(\|f\|_2^2\).

**Exercise 5.3 (intermediate).** Let \(p(\xi)=\xi\) on \(\mathbb R\), and let \(h_\lambda(\xi)=\mathbf1_{\{\lambda\}}(\xi)\). Each \(h_\lambda\) represents zero in ambient \(L^2(d\xi)\). Compute \(h_{p(\xi)}(\xi)\), and explain why this choice cannot represent the canonical trace of the zero \(B\) function.

**Exercise 5.4 (intermediate).** Suppose \(f\in B\) and \(E^cf=0\). Prove that both \(T_\lambda a_\pm(\lambda,f)\) vanish for every \(\lambda\in\Omega\), not merely almost every energy.

**Exercise 5.5 (advanced).** Let \(A,B\) be self-adjoint operators on Hilbert spaces and \(J\) a bounded map. Suppose a core \(\mathcal C\) of \(A\) satisfies \(J\mathcal C\subset\mathcal D(B)\) and \(JA\phi=BJ\phi\). Prove domain intertwining and group intertwining on the full spaces, carefully justifying the product derivative.

<a id="distorted-solutions"></a>

## 6. Complete solutions

**Solution 5.1.** Write the difference as
\(\int P_\varepsilon(s)[\chi(t-s)-\chi(t)]\,ds\).
The integrand difference is at most \(\omega_\chi(\delta)\) when \(|s|\leq\delta\). On the complement it is at most \(2\|\chi\|_\infty\), and
\[
 \int_{|s|>\delta}P_\varepsilon(s)\,ds
 \leq\frac{2\varepsilon}{\pi}\int_\delta^\infty s^{-2}\,ds
 =\frac{2\varepsilon}{\pi\delta}.
\]
The kernel's total mass is one. Adding the two bounds proves the estimate. Neither bound depends on \(t\); compact continuous \(\chi\), extended by zero, is uniformly continuous on the whole line, so the estimate also applies outside its support.

**Solution 5.2.** On the positive branch \(\lambda=\xi^2\) has \(d\xi=d\lambda/(2\sqrt\lambda)\); on the negative branch the same absolute Jacobian appears. Therefore, for a nonnegative test \(\chi\),
\[
 \int\chi(\xi^2)|\widehat f(\xi)|^2\,d\xi
 =\int_0^\infty\chi(\lambda)
       \frac{|\widehat f(\sqrt\lambda)|^2+
             |\widehat f(-\sqrt\lambda)|^2}
                  {2\sqrt\lambda}\,d\lambda.
\]
The change of variables is first valid away from zero and then on the full half-lines by monotone convergence. This gives (19). Taking tests increasing to one gives the full Fourier \(L^2\) norm, equal to \(\|f\|_2^2\) by unitary Plancherel.

**Solution 5.3.** At every \(\xi\), \(h_{p(\xi)}(\xi)=h_\xi(\xi)=1\). Thus an arbitrary selection of ambient null-set representatives can create the constant function one on the energy-frequency diagonal, despite representing zero for every fixed parameter in ambient \(L^2\). Here \(M_\lambda=\{\lambda\}\) has zero-dimensional surface measure one. The canonical trace of the zero \(B\) function is zero on that point, while the selected representative has value one. Lemma 2.1 first approximates in \(B\) and controls the actual trace on each surface; an arbitrary ambient representative has no such control.

**Solution 5.4.** By (13), \(\int_\Omega q_f(\lambda)\,d\lambda=0\). The nonnegative continuous function \(q_f\) must vanish everywhere in the open set \(\Omega\): a positive value would remain bounded below by a positive number on a small interval and give a positive integral. Formula (6) now gives a zero integral of \(|T_\lambda a_\pm|^2/g\) for every \(\lambda\). On each compact surface patch \(g\) is positive and finite, so a zero weighted integral forces the trace to vanish almost everywhere there. A countable patch exhaustion gives its vanishing on the whole surface for each fixed energy and both signs.

**Solution 5.5.** Given \(f\in\mathcal D(A)\), choose \(\phi_j\in\mathcal C\) with \(\phi_j\to f\) and \(A\phi_j\to Af\). Boundedness gives \(J\phi_j\to Jf\) and \(BJ\phi_j=JA\phi_j\to JAf\). Closedness of \(B\) proves \(Jf\in\mathcal D(B)\) and \(BJf=JAf\).

For \(f\in\mathcal D(A)\), the curve \(y(t)=Je^{itA}f\) takes values in \(\mathcal D(B)\), is differentiable as a Hilbert-space curve with \(y'(t)=iJAe^{itA}f\), and satisfies \(By(t)=JAe^{itA}f\). The latter is continuous in \(t\), since \(Ae^{itA}f=e^{itA}Af\). To differentiate \(e^{-itB}y(t)\), split its difference quotient into the change in \(y\), multiplied by the nearby unitary, and the change in that unitary on the fixed vector \(y(t)\in\mathcal D(B)\). Strong continuity handles the first term and the domain derivative handles the second. The result is \(e^{-itB}[y'(t)-iBy(t)]=0\). Hence \(e^{-itB}Je^{itA}f=Jf\). Dense-domain approximation, boundedness of \(J\), and unitarity extend the identity to all \(f\).

## References


- [K] Shige Toshi Kuroda, *Scattering theory for differential operators, I, operator theory*, Journal of the Mathematical Society of Japan **25** (1973), 75–104, Section 4.2, Proposition 4.2 and equations (4.11)–(4.18). [Freely accessible journal PDF](https://www.jstage.jst.go.jp/article/jmath1948/25/1/25_1_75/_pdf/-char/en).
- [T] Gerald Teschl, *Mathematical Methods in Quantum Mechanics: With Applications to Schrödinger Operators*, second edition, American Mathematical Society, 2014, Sections 3.1 and 3.4, especially Theorems 3.2 and 3.6 and results 3.19–3.23. [Author's authorized online edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).
