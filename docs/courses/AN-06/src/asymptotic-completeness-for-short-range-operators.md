# Asymptotic completeness for short-range operators

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Original exposition: CC0.*

**Working question: How does a time comparison prove that no continuous states are missing?** A wave operator can preserve every norm and still miss a subspace. The unilateral shift in the guide makes this visible. Here the matching-sign composition with a stationary transform equals the ordinary Fourier transform. Its surjectivity is the extra information that recovers every continuous interacting state.

The time-dependent wave operators and the stationary distorted Fourier transforms describe the same continuous states. Their composition is the ordinary Fourier transform. Because that transform is onto, every absolutely continuous perturbed state has both an incoming and an outgoing free comparison state.

<a id="completeness-setting"></a>

Use the real simply characteristic polynomial \(p\), its absence of invariant directions, the symmetric short-range differential perturbation \(V\), and the self-adjoint closure \(H\) from [Wave operators for differential perturbations](wave-operators-for-differential-perturbations.md#wave-differential-existence). Write \(H_0=p(D)\), and use the unitary Fourier transform \(\mathcal F\). The existence theorem there gives isometries

\[
 W_\pm=\mathop{\mathrm{s\!-\!lim}}_{t\to\pm\infty}
                    e^{itH}e^{-itH_0}.
\tag{1}
\]

[Distorted Fourier transforms and spectral density](distorted-fourier-transforms-and-spectral-density.md) supplies \(J_\pm\), the closed countable exceptional set \(\Sigma\), its complement \(\Omega\), and the projection \(E^c=E_H(\Omega)\). In particular,

\[
 \|J_\pm u\|_2=\|E^cu\|_2,\qquad
 J_\pm e^{itH}=e^{itM_p}J_\pm.
\tag{2}
\]

The same lesson proves \(\mathcal H_{\mathrm{ac}}(H)=E^cL^2\), and the existence theorem puts the ranges of \(W_\pm\) inside this subspace.

For further reading on stationary spectral representations and scattering completeness, see Kuroda [K], Section 4.2, Yafaev [Y], Section 2, and Teschl [T], Section 12.1.

## 1. Damped integrals and their two signs

The continuous Banach-valued integrals below use the [norm-integral construction](../providers/analysis/hilbert-valued-integration.md#bochner-integral) and [continuous primitive theorem](../providers/analysis/hilbert-valued-integration.md#vector-primitives) from Hilbert-valued integration, whose proofs also apply to arbitrary Banach spaces. Completeness and the scalar norm bound construct the improper integrals. Bounded linear maps commute with them, first on Riemann sums and then by the norm limit. In Section 2 we prove the additional interchange with surface representatives directly from scalar Fubini.

Let
\[
 \mathcal D=\mathcal F^{-1}C_c^\infty(\{\nabla p\ne0\}),
 \qquad F_t=e^{-itH_0}f,\quad f\in\mathcal D.
\]
The [wave-packet and shell-integrability proof](wave-operators-for-differential-perturbations.md#wave-differential-packets) shows density of \(\mathcal D\) and
\[
 \int_{\mathbb R}\|VF_t\|_2\,dt<\infty.
\tag{3}
\]
Its product derivative therefore gives
\[
 W_+f=f+\int_0^\infty i e^{itH}VF_t\,dt,\qquad
 W_-f=f-\int_{-\infty}^0 i e^{itH}VF_t\,dt,
\tag{4}
\]
with absolutely convergent \(L^2\) integrals.

<a id="completeness-abel-integral"></a>

**Lemma 1.1.** The function \(t\mapsto VF_t\) is continuous and bounded in \(B\). For \(\varepsilon>0\), \(\lambda\in\mathbb R\), and \(\sigma\in\{+1,-1\}\),
\[
 \sigma\int_{\sigma t>0}
       i e^{-\varepsilon|t|}e^{it\lambda}VF_t\,dt
       =VR_0(\lambda+\sigma i\varepsilon)f
       \quad\text{in }B.
\tag{5}
\]

**Proof.** All graph components of \(F_t\) have their free \(L^2\) norms preserved, so
\[
 \|F_t\|_{X_p}
 \leq\sum_\alpha\|(\partial^\alpha p)(D)f\|_2
       \quad(t\in\mathbb R).
\tag{6}
\]
Each component is \(L^2\)-continuous in \(t\), by dominated convergence of its Fourier phase. Since the \(B^*\) norm is bounded by the \(L^2\) norm, the path is continuous in \(X_p\). Boundedness of \(V:X_p\to B\) proves the first claim. The exponential damping makes (5) absolutely convergent in \(B\), and also makes its free input integral absolutely convergent in \(X_p\).

For a real scalar \(a\),
\[
 i\int_0^\infty e^{-\varepsilon t}e^{-ita}\,dt
       =\frac1{a-i\varepsilon},\qquad
 -i\int_{-\infty}^0e^{\varepsilon t}e^{-ita}\,dt
       =\frac1{a+i\varepsilon}.
\tag{7}
\]
Apply these identities with \(a=p(\xi)-\lambda\). Each free graph component has a fixed compact smooth Fourier amplitude. On a finite time interval, the bounded Fourier map commutes with the norm integral; scalar integration gives the truncated version of (7). Its remaining scalar tail is bounded by \(e^{-\varepsilon T}/\varepsilon\), uniformly in the real number \(a\). Multiplying by each fixed \(L^2\) Fourier amplitude therefore bounds its tail norm by \(e^{-\varepsilon T}/\varepsilon\) times that amplitude norm. Passing to infinity in all finitely many graph components identifies the free input integral with \(R_0(\lambda+\sigma i\varepsilon)f\). Applying the bounded map \(V\) to the \(X_p\) integral proves (5). \(\square\)

The undamped integral in (4) is controlled in \(L^2\) by (3). Formula (5) uses a separate \(B\) integral with damping; no undamped time integrability in \(B\) is required.

## 2. Comparing time evolution with the surface transform

For \(\lambda\in\Omega\) let
\[
 A_\sigma(\lambda)=(I+VR_{0,\sigma}(\lambda))^{-1}:B\to B.
\]
The [boundary-family proof](limiting-absorption-and-point-spectrum.md#limiting-absorption-boundary) proves its strong continuity, local uniform norm bounds, and strong continuity of \(VR_0(z)\) up to each boundary.

<a id="completeness-comparison"></a>

**Theorem 2.1.** With matching signs,
\[
 J_\pm W_\pm=\mathcal F
       \quad\text{on }L^2(dx).
\tag{8}
\]

**Proof.** Start with \(f\in\mathcal D\). For \(\varepsilon>0\), set
\[
 y_{\sigma,\varepsilon}
 =f+\sigma\int_{\sigma t>0}
       i e^{-\varepsilon|t|}e^{itH}VF_t\,dt.
\tag{9}
\]
Dominated convergence using (3) gives \(y_{\sigma,\varepsilon}\to W_\sigma f\) in \(L^2\). Boundedness and (2) give
\[
 J_\sigma y_{\sigma,\varepsilon}
 =J_\sigma f+\sigma\int_{\sigma t>0}
     i e^{-\varepsilon|t|}e^{itM_p}J_\sigma(VF_t)\,dt
 \longrightarrow J_\sigma W_\sigma f
       \quad\text{in }L^2(d\xi).
\tag{10}
\]

<a id="completeness-joint-assembly"></a>

We spell out how to interpret this time integral on surfaces. The path \(b(t)=VF_t\) is continuous in \(B\). On every compact \((\lambda,t)\) set in \(\Omega\times\mathbb R\), \(A_\sigma(\lambda)b(t)\) is continuous in \(B\): split the difference into the change in \(b\), controlled by the local uniform norm bound, and the change in \(A_\sigma\) on a fixed vector. The [parameter partition and measurable-assembly proof](distorted-fourier-transforms-and-spectral-density.md#distorted-parameter-partition) therefore applies with \(t\) as an additional parameter. Approximate this \(B\)-valued function by locally finite smooth partitions of unity in \((\lambda,t)\), with fixed compact-Fourier values. More explicitly, let \(h_j(\lambda,t)\) be these approximations, with \(B\)-error at most \(2^{-j}\), and form \(G_j(t,\xi)=\mathcal Fh_j(p(\xi),t)(\xi)\). Each is locally a finite sum of continuous functions, hence jointly Borel. At every fixed \((\lambda,t)\) the trace errors are summable in surface \(L^2\), so the sequence converges outside a surface-null set to \(T_\lambda A_\sigma(\lambda)b(t)\). The pointwise Cauchy set in \((t,\xi)\) is Borel; define the limit there and zero elsewhere. Coarea at each fixed \(t\) identifies this function with the already defined \(L^2\) class \(J_\sigma b(t)\). This constructs the representatives needed for Fubini, rather than choosing arbitrary ambient \(L^2\) values.

<a id="completeness-fubini"></a>

On a compact energy interval \(I\Subset\Omega\), the trace and inverse bounds and Lemma 1.1 give
\[
 \|T_\lambda A_\sigma(\lambda)b(t)\|_{L^2(dS)}
       \leq C_{I,f}
       \quad(\lambda\in I,\ t\in\mathbb R).
\tag{11}
\]
With the factor \(e^{-\varepsilon|t|}\), this is integrable in \(t\). Here is the required interchange proof. On a compact frequency patch \(K\) inside one energy chart, \(g^{-1}\) is bounded; coarea and (11) bound the \(L^2(K)\) norm of the jointly measurable integrand by \(C_K e^{-\varepsilon|t|}\). More generally, for jointly measurable \(F(t,\xi)\) on \(\mathbb R\times K\) with
\[
 M=\int_{\mathbb R}\|F(t,\cdot)\|_{L^2(K)}\,dt<\infty,
\]
Tonelli and Cauchy–Schwarz give \(\int\!\int_K|F|\leq |K|^{1/2}M\). The scalar integral \(h(\xi)=\int F(t,\xi)\,dt\) therefore exists almost everywhere. For \(q\in L^2(K)\), the integral of \(|F\overline q|\) is at most \(M\|q\|_2\), so scalar Fubini gives \((h,q)=\int(F(t),q)\,dt\). To verify \(h\in L^2\) without assuming it, test with \(q=h\mathbf1_{\{|h|\leq N\}}\), which lies in \(L^2(K)\) since \(K\) has finite measure. The resulting inequality bounds \(\|h\mathbf1_{\{|h|\leq N\}}\|_2\) by \(M\). Monotone convergence gives \(\|h\|_2\leq M\). Bounded scalar pairings commute with the continuous vector integrals already constructed, so equality of all these pairings identifies their \(L^2(K)\) integral with \(h\).

The same argument applies on each compact surface patch with \(dS\), for each fixed energy: the canonical trace is continuous in \(t\) and its norm has the integrable bound (11) with damping. Scalar Fubini in \((t,\lambda,\eta)\) on each coordinate patch then identifies these surface integrals with the ambient representative for almost every energy. A countable patch cover suffices. Thus (10) is identified, for almost every energy and surface point, with the measurable surface expression
\[
 G_{\sigma,\varepsilon}|_{M_\lambda}
 =T_\lambda A_\sigma(\lambda)
       [f+VR_0(\lambda+\sigma i\varepsilon)f].
\tag{12}
\]
Indeed \(e^{itM_p}\) becomes the scalar \(e^{it\lambda}\) on that surface, and (5) evaluates its remaining \(B\) integral. For the identification in ambient \(L^2\), the integral in (10) is absolutely convergent there by (3); the locally defined surface integrals give the same representative by Fubini on a countable energy-coordinate cover. This requires only equality at almost every energy for the time integral.

<a id="completeness-boundary-limit"></a>

For every fixed \(\lambda\in\Omega\), strong boundary continuity gives
\[
 VR_0(\lambda+\sigma i\varepsilon)f
       \longrightarrow VR_{0,\sigma}(\lambda)f\quad\text{in }B.
\]
Thus (12) tends in surface \(L^2\) to
\[
 T_\lambda A_\sigma(\lambda)
       (I+VR_{0,\sigma}(\lambda))f
       =T_\lambda f.
\tag{13}
\]
This convergence also holds in \(L^2\) on every compact frequency subset of \(p^{-1}(\Omega)\). To see it, its image under \(p\) lies in a compact subset of \(\Omega\); cover that energy set by finitely many compact intervals there. All free graph, inverse and trace norms are uniformly bounded on this compact set, including \(0\leq\varepsilon\leq\varepsilon_0\). Surface squared differences in (13) are therefore uniformly bounded and tend to zero. On the compact frequency set, \(g=|\nabla p|\) has a positive minimum, since its energies lie in \(\Omega\). Thus the coarea factor \(1/g\) is uniformly bounded on that set. Integrating the surface squared differences over the finite energy cover and applying dominated convergence gives the claimed local \(L^2\) convergence.

The global \(L^2\) limit in (10) and this local limit must agree. Since \(f\) has smooth Fourier support, \(T_\lambda f\) is the restriction of \(\widehat f\). A countable compact exhaustion of \(p^{-1}(\Omega)\) proves \(J_\sigma W_\sigma f=\widehat f\) there. Its complement \(p^{-1}(\Sigma)\) is null, as proved in the distorted-transform lesson, so (8) holds in full \(L^2(d\xi)\) on \(\mathcal D\). Density of \(\mathcal D\), boundedness of \(J_\sigma\), isometry of \(W_\sigma\), and unitary Plancherel extend it to every \(f\). \(\square\)

## 3. Completeness and the scattering operator

<a id="completeness-onto"></a>

**Theorem 3.1.** The maps
\[
 W_\pm:L^2(dx)\longrightarrow E^cL^2(dx),\qquad
 J_\pm:E^cL^2(dx)\longrightarrow L^2(d\xi)
\tag{14}
\]
are unitary onto the indicated spaces. In particular
\[
 \operatorname{ran}W_+=\operatorname{ran}W_-
       =\mathcal H_{\mathrm{ac}}(H).
\tag{15}
\]
The scattering operator
\[
 S=W_+^*W_-
\tag{16}
\]
is unitary on the free space and commutes with \(e^{itH_0}\). In momentum space,
\[
 \mathcal F S\mathcal F^{-1}
       =J_+J_-^{-1},
\tag{17}
\]
where the inverse in (17) is the inverse of \(J_-\) restricted to \(E^cL^2\).

**Proof.** \(W_\sigma\) is already an isometry with range in \(E^cL^2\), and \(J_\sigma\) is an isometry on that subspace. Equation (8) and surjectivity of \(\mathcal F\) first prove that \(J_\sigma\) is onto. For \(u\in E^cL^2\), choose
\(f=\mathcal F^{-1}J_\sigma u\). Then
\(J_\sigma W_\sigma f=\mathcal Ff=J_\sigma u\).
The difference \(W_\sigma f-u\) lies in \(E^cL^2\), where \(J_\sigma\) is injective, so it is zero. This proves surjectivity of \(W_\sigma\) and (14)-(15).

An isometry onto \(E^cL^2\) satisfies \(W_\sigma^*W_\sigma=I\) and \(W_\sigma W_\sigma^*=E^c\): the latter operator is the identity on the range and zero on its orthogonal complement. Consequently \(S^*S=W_-^*E^cW_-=I\), and similarly \(SS^*=I\). The [group intertwining](wave-operators-for-differential-perturbations.md#wave-differential-intertwining) and its adjoint give \(Se^{itH_0}=W_+^*e^{itH}W_-=e^{itH_0}S\).

Equation (8) on the common range gives \(\mathcal F W_+^*=J_+\), while \(W_-\mathcal F^{-1}=J_-^{-1}\). Their composition proves (17). \(\square\)

<a id="completeness-spectral-regions"></a>

The [spectral-measure argument in Modified waves and the direction of escape](modified-waves-and-the-direction-of-escape.md#modified-wave-spectral-measures) applies to the isometry \(S\) intertwining the free group with itself. It proves \(\|E_0(A)Sf\|^2=\|E_0(A)f\|^2\) for every vector and every Borel energy set \(A\), by the damped resolvent integral and scalar spectral inversion. Polarization gives \(S^*E_0(A)S=E_0(A)\); multiplication on the left by the now proved unitary \(S\) gives \(SE_0(A)=E_0(A)S\). In momentum space these projections multiply by \(\mathbf1_{\{p(\xi)\in A\}}\). Thus (17) restricts to a unitary on every such energy region. The operator on an individual energy surface requires the further stationary scattering-matrix construction.

<a id="completeness-domains"></a>

The closed-operator domain identities are included in this unitary equivalence. The earlier inclusion \(HW_\sigma f=W_\sigma H_0f\) for \(f\in\mathcal D(H_0)\), together with the unitary group equivalence and its generator domains, gives
\[
 W_\sigma\mathcal D(H_0)=
       \mathcal D(H)\cap E^cL^2.
\]
The orthogonal complement is the closed span of bound states, including any threshold eigenfunctions. This completeness theorem does not impose decay or finite multiplicity at thresholds.

<a id="completeness-logarithmic-example"></a>

**Example 3.2.** A bounded real potential satisfying
\[
 |V(x)|\leq
       \frac{C}{(1+|x|)[\log(e+|x|)]^2}
\]
is covered by the [summable local criterion and logarithmic example](wave-operators-for-differential-perturbations.md#wave-differential-examples) and hence by (15). For \(H_0=-\Delta\), the derivative weight satisfies \(\widetilde p(\xi)^2=|\xi|^4+4|\xi|^2+4n\leq C_n(1+|\xi|^2)^2\), which proves the simply characteristic inequality \(\widetilde p\leq C(1+|p|+|\nabla p|)\). If \(p(\xi+tv)=p(\xi)\) for all \(t\), the quadratic coefficient \(|v|^2\) is zero, so there is no nonzero invariant direction. The cited logarithmic example proves that the envelope is slower than every fixed \((1+|x|)^{-1-\delta}\), while its dyadic contributions sum like \(\sum_j(1+j)^{-2}\). Completeness follows from the full local short-range condition and the stationary comparison, in addition to wave-operator existence.

<a id="completeness-eigenfunction-sign"></a>

**The sign in the eigenfunction equation.** Let \(H=H_0+V\), \(R_0(z)=(H_0-z)^{-1}\), and \((H_0-\lambda)\psi_0=0\). With these conventions the outgoing integral equation is

\[
 \psi=\psi_0-R_0(\lambda+i0)V\psi.
\]

Indeed, wherever the boundary product is defined, applying \(H_0-\lambda\) gives \((H_0-\lambda)\psi=-V\psi\), as required by \((H-\lambda)\psi=0\). The opposite sign would instead give \((H_0-\lambda)\psi=V\psi\). Rearranging the correct equation and multiplying by \(V\) gives \((I+VR_{0,+})V\psi=V\psi_0\), explaining the plus inside the forcing inverse. Taking adjoints exchanges upper and lower resolvent boundaries; it does not change the sign of \(V\) in \(H\). For eigenfunction expansions, see Yafaev [Y], Section 2.

<a id="completeness-green-kernel"></a>

**A concrete verification of the sign.** On the line take \(H_0=-\partial_x^2\), \(\lambda=1\), \(\psi_0=e^{ix}\), and

\[
 V=\tfrac18w,\qquad
 w(x)=\begin{cases}
 e^{-1/(1-x^2)},&|x|<1,\\
 0,&|x|\geq1.
 \end{cases}
\]

The [smooth cutoff construction](../providers/analysis/elementary-functions-and-cutoffs.md#smooth-flat-cutoffs) makes \(w\) smooth across its endpoints. This real smooth compact potential satisfies the local short-range criterion, and the [bounded-perturbation domain proof](resolvents-domains-and-spectral-density.md#u001-specified-domains) makes \(H=H_0+V\) self-adjoint on \(H^2(\mathbb R)\). The free upper boundary kernel is \(G(x)=(i/2)e^{i|x|}\): it solves \(-G''-G=0\) off zero and has derivative jump \(-1\). Integrating by parts on the two half-lines against a compactly supported smooth test leaves minus that jump times its value at zero; the continuity of \(G\) cancels the terms containing the derivative of the test. Hence \(-G''-G=\delta_0\).

To identify it with the resolvent boundary, put \(z=1+i\varepsilon\), \(a_\varepsilon=((\sqrt{1+\varepsilon^2}+1)/2)^{1/2}\), \(b_\varepsilon=\varepsilon/(2a_\varepsilon)\), and \(\kappa_\varepsilon=a_\varepsilon+ib_\varepsilon\). Then \(\kappa_\varepsilon^2=z\), \(b_\varepsilon>0\), and \(\kappa_\varepsilon\to1\). The kernel \(G_\varepsilon(x)=i e^{i\kappa_\varepsilon|x|}/(2\kappa_\varepsilon)\) is in \(L^1\cap L^2\), and the same derivative-jump computation gives \(( -\partial_x^2-z)G_\varepsilon=\delta_0\). For compactly supported bounded \(h\), which belongs to \(B\) because it meets only finitely many dyadic shells, [Young's inequality](../providers/analysis/euclidean-approximation-and-convolution.md#holder-and-young) puts \(v=G_\varepsilon*h\) in \(L^2\). Distributional differentiation gives \(v''=-zv-h\in L^2\); Plancherel then gives \(\xi^2\widehat v\in L^2\), hence \(v\in H^2\). Uniqueness of the nonreal self-adjoint resolvent solution proves \(v=R_0(z)h\). The kernels converge uniformly on compact sets to \(G\), so convolution with this compactly supported \(L^1\) function converges locally uniformly to \(G*h\). The free boundary limit also converges as a distribution, by the earlier limiting-absorption theorem. Uniqueness of that limit proves \(R_{0,+}(1)h=G*h\).

<a id="completeness-neumann-example"></a>

On \(I=[-1,1]\), let \(K:C(I)\to C(I)\) be

\[
 (Kh)(x)=\frac{i}{16}\int_I
              e^{i|x-y|}w(y)h(y)\,dy.
\]

The uniform limit of continuous functions is continuous, and a uniformly Cauchy sequence has a pointwise limit by scalar completeness; thus \(C(I)\) is complete. Since \(0\leq w\leq1\), the integral gives \(\|K\|\leq1/8\). It also gives \(|Kh(x)-Kh(x')|\leq\|h\|_\infty|x-x'|/8\), using \(|e^{iu}-e^{iv}|\leq|u-v|\), which follows by integrating the derivative of the exponential. Thus \(K\) indeed maps \(C(I)\) to itself. The Neumann inverse \((I+K)^{-1}=\sum_{m\geq0}(-K)^m\) therefore converges in norm, with its tail bounded by \((1/8)^{N+1}/(1-1/8)\). The finite partial sums satisfy \((I+K)\sum_{m=0}^N(-K)^m=I-(-K)^{N+1}\), and the same identity holds in the other order. The remainder norm tends to zero, proving both inverse identities. Put \(\psi_I=(I+K)^{-1}\psi_0|_I\). Then

\[
 \begin{gathered}
 \|\psi_I-\psi_0\|_\infty\leq\tfrac17,\\
 |\psi_I|\geq\tfrac67\quad\text{on }I.
 \end{gathered}
\]

Extend it to the line by

\[
 \psi(x)=e^{ix}-\frac{i}{16}\int_I
                    e^{i|x-y|}w(y)\psi_I(y)\,dy.
\]

The defining equation on \(I\) proves that this extension restricts to \(\psi_I\). The kernel identity gives \((H-1)\psi=0\) distributionally. Here are the regularity details. The integral makes \(\psi\) continuous, so \(F=(V-1)\psi\) is continuous and \(\psi''=F\) distributionally. On any bounded open interval, twice integrating \(F\) from an interior point gives a \(C^2\) function \(P\) with \(P''=F\). A distribution with zero first derivative is constant: every compactly supported smooth test of integral zero has a compactly supported smooth primitive, so the distribution annihilates it; subtracting a fixed test of integral one identifies its value on every test. Applying this fact first to \((\psi-P)'\) and then after subtracting the resulting linear function shows that \(\psi-P\) is affine. Thus \(\psi\) is \(C^2\). The equation \(\psi''=(V-1)\psi\) and the scalar primitive theorem now raise its regularity by two derivatives at each step, giving \(\psi\in C^\infty\). For \(x>1\), the correction is \(-i e^{ix}\int_Ie^{-iy}w(y)\psi_I(y)\,dy/16\); for \(x<-1\), it is \(-i e^{-ix}\int_Ie^{iy}w(y)\psi_I(y)\,dy/16\). These are exactly outgoing waves on their respective ends. Since \(|V\psi|\geq3w/28\) in \((-1,1)\), it is nonzero. The residual of the opposite-sign equation is \(-2R_{0,+}(1)V\psi\); it cannot vanish, because applying \(-\partial_x^2-1\) would give \(-2V\psi=0\). This nonzero smooth compact potential therefore rules out accidental cancellation in the opposite-sign equation.

### Use the conclusion

Locate the matching signs in the Abel comparison, then write the preimage of a continuous state. Keep the stationary identity and the time-dependent existence theorem as distinct inputs to the range argument.

<a id="completeness-exercises"></a>

## 4. Exercises

**Exercise 4.1 (foundation).** Evaluate both scalar integrals in (7), including their signs, and determine the corresponding upper or lower resolvent parameter.

**Exercise 4.2 (foundation).** Let \(W:X\to Y\) and \(J:Y\to Z\) be isometries of Hilbert spaces. If \(JW:X\to Z\) is onto, prove that both \(J\) and \(W\) are onto.

**Exercise 4.3 (intermediate).** Suppose the known estimate is \(\int\|VF_t\|_2\,dt<\infty\) and \(\sup_t\|VF_t\|_B<\infty\). Identify which estimate justifies (10), and which justifies (5). Prove convergence of \(y_{\sigma,\varepsilon}\) to \(W_\sigma f\) without assuming \(\int\|VF_t\|_B\,dt<\infty\).

**Exercise 4.4 (intermediate).** Derive (17) from the two identities \(J_\pm W_\pm=\mathcal F\) and their unitary ranges. Specify the domain of each inverse and adjoint.

**Exercise 4.5 (advanced).** In the general theorem, prove the equality of the closed operator domains under \(W_\sigma\) from the group identity and surjectivity. Explain why the equality does not identify \(\mathcal D(H)\) with the full free domain as sets of functions.

<a id="completeness-solutions"></a>

## 5. Complete solutions

**Solution 4.1.** The positive-time integral is \(i/(\varepsilon+ia)=1/(a-i\varepsilon)\), since \(\varepsilon+ia=i(a-i\varepsilon)\). The negative-time integral is \(-i/(\varepsilon-ia)=1/(a+i\varepsilon)\), since \(\varepsilon-ia=-i(a+i\varepsilon)\). With \(a=p(\xi)-\lambda\), they give \(R_0(\lambda+i\varepsilon)\) and \(R_0(\lambda-i\varepsilon)\), respectively. The minus sign in the negative-time version is part of (4); keeping it gives the plus \(VR_0\) correction on both sides in (12).

**Solution 4.2.** Surjectivity of \(JW\) immediately implies surjectivity of \(J\). For \(y\in Y\), choose \(x\in X\) with \(JWx=Jy\). Injectivity of the isometry \(J\) gives \(Wx=y\), proving surjectivity of \(W\). With the same proof, \(Y\) may be a specified closed subspace of a larger Hilbert space; only that subspace is the domain on which \(J\) must be isometric.

**Solution 4.3.** In (10), \(\|J_\sigma e^{itH}VF_t\|_2\leq\|VF_t\|_2\), by boundedness of \(J_\sigma\) and unitarity. This supplies the integrable \(L^2\) majorant. In (5), the exponential factor and the uniform \(B\) bound give
\(\int_{\sigma t>0}e^{-\varepsilon|t|}\|VF_t\|_B\,dt\leq C/\varepsilon\).
The undamped \(B\) integral is not used. Subtract (4) from (9) and estimate
\[
 \|y_{\sigma,\varepsilon}-W_\sigma f\|_2
 \leq\int_{\sigma t>0}
       |e^{-\varepsilon|t|}-1|\,\|VF_t\|_2\,dt.
\]
Its integrand tends pointwise to zero and is bounded by the integrable function \(\|VF_t\|_2\). Dominated convergence proves the limit.

**Solution 4.4.** The maps \(W_\pm\) are unitaries from the free \(L^2(dx)\) onto \(E^cL^2(dx)\); their adjoints restricted to this range are their inverse unitaries. The restrictions \(J_\pm:E^cL^2(dx)\to L^2(d\xi)\) are unitaries. For \(u\in E^cL^2\), write \(u=W_+f\). Then \(J_+u=\mathcal Ff=\mathcal F W_+^*u\), proving \(\mathcal F W_+^*=J_+\) on the range. Similarly \(J_-W_-\mathcal F^{-1}=I\) gives \(W_-\mathcal F^{-1}=J_-^{-1}\), with inverse domain \(L^2(d\xi)\) and target \(E^cL^2\). Composing these identities with \(S=W_+^*W_-\) yields (17).

**Solution 4.5.** The group identity is \(e^{itH}W_\sigma=W_\sigma e^{itH_0}\). If \(f\in\mathcal D(H_0)\), differentiation at zero gives \(W_\sigma f\in\mathcal D(H)\) and \(HW_\sigma f=W_\sigma H_0f\). Conversely, for \(u\in\mathcal D(H)\cap E^cL^2\), surjectivity supplies \(f=W_\sigma^{-1}u\). Applying that inverse to the group identity shows that the orbit \(e^{itH_0}f\) is norm differentiable at zero. The self-adjoint generator-domain criterion gives \(f\in\mathcal D(H_0)\). Thus the domain equality is carried by the unitary \(W_\sigma\). It compares a free function with its transformed perturbed state; it does not say the same function lies in both domains. Bound states lie outside this comparison subspace as well.

## References


- [K] Shige Toshi Kuroda, *Scattering theory for differential operators, I, operator theory*, Journal of the Mathematical Society of Japan **25** (1973), 75–104, Section 4.2, pages 87–89. [Freely accessible journal PDF](https://www.jstage.jst.go.jp/article/jmath1948/25/1/25_1_75/_pdf/-char/en).
- [Y] Dmitri Yafaev, *Lectures on scattering theory*, 2004. [arXiv:math/0403213v1](https://arxiv.org/abs/math/0403213v1).
- [T] Gerald Teschl, *Mathematical Methods in Quantum Mechanics: With Applications to Schrödinger Operators*, second edition, American Mathematical Society, 2014, Section 12.1, Lemma 12.1 and Theorem 12.2. [Author's authorized online edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).
