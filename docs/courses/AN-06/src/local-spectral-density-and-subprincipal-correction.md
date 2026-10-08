# Local spectral density and the subprincipal correction

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Original exposition: CC0.*

**Working question: What does the next local density coefficient measure?** Scaling a cotangent sublevel set determines the leading density. Moving its boundary differentiates that volume and introduces the lower-order symbol contribution. Before integrating over space, the order of the two inserted operators also matters. The trace cancels some local terms, so a traced formula should not be read backwards as a pointwise identity.

A short-time wave kernel contains the high-frequency spectral density. Its leading coefficient measures a cotangent sublevel set. The next coefficient also sees the subprincipal symbol and, before taking a spatial trace, the order of the two operators. We compute both coefficients, keeping the sign of the Fourier phase visible throughout.

Hörmander's spectral-function article [HS, Section 4] gives the passage from a short-time kernel to spectral asymptotics; its equation (4.12) is the amplitude expansion specialized below. We derive the scalar subprincipal and bracket terms here. Avetisyan, Fang and Vassiliev [AFV, Sections 2–3] provide a comparison for first-order systems, whose additional eigenvector terms must be retained in that setting. Guillemin and Sternberg [GS] supply a semiclassical comparison; the [DG] article provides the classical spectral setting. Our proof uses the small-time phase and complete amplitude recursion in [Wave evolution and cotangent flow, Sections 3–5](wave-evolution-and-cotangent-flow.md), with the finite parameter remainders proved in [Scalar transport and finite action on a phase, (T1)–(T12)](../providers/analysis/scalar-transport-and-phase-action.md#finite-phase-action). It uses the scalar half-density subprincipal rule in [Classical scalar symbols, summation and regularity, (FC9)–(FC15)](../providers/analysis/classical-scalar-calculus.md#scalar-coordinate-change), and the actual [qualified-pullback proof](../providers/analysis/wavefront-qualified-pullback.md#qualified-pullback) for the diagonal. The one-dimensional amplitude reduction is proved explicitly in Section 4. 

Let \(X\) be compact, connected and without boundary, with dimension \(n\geq2\). Let \(P\) be the scalar symmetric classical elliptic operator of order one on half densities from the wave lesson, with positive principal symbol \(p\). Its self-adjoint domain is \(H^1\). Write
\[
E(t)=e^{-itP},\qquad D=-i\partial.
\]
Let \(B\in\Psi^0_{\mathrm{cl}}(X;\Omega^{1/2})\). Its principal and subprincipal symbols are \(b\) and \(b_s\); those of \(P\) are \(p\) and \(p_s\). The operator \(B\) need not be symmetric.

We distinguish an ordinary symbol from a classical expansion. An ordinary \(S^m\) symbol satisfies
\[
|\partial_y^\alpha\partial_\lambda^k a(y,\lambda)|
\leq C_{\alpha k}\langle\lambda\rangle^{m-k}
\tag{1}
\]
on compact coordinate sets. A classical symbol has, in addition, an expansion in homogeneous terms of degrees \(m,m-1,\ldots\). A primitive of a classical symbol can contain a logarithm. This distinction will matter in dimension two.

<a id="density-energy-integrals"></a>

## 1. The two invariant symbols and an energy integral

The scalar half-density subprincipal convention is that of Hörmander [H3, (18.1.32) and Theorem 18.1.33].

In a half-density coordinate frame, write the left symbols as
\[
P_L=p+p_0+S^{-1},\qquad
B_L=b+b_{-1}+S^{-2}.
\]
The exact half-density rule gives
\[
p_s=p_0+\frac i2\sum_j p_{y_j\eta_j},
\qquad
b_s=b_{-1}+\frac i2\sum_j b_{y_j\eta_j}.
\tag{2}
\]
These subprincipal symbols are scalars on the punctured cotangent bundle. In particular, the subprincipal symbol of \(B^*\) is \(\overline{b_s}\).

Our bracket convention is
\[
\{b,p\}
=\sum_j(b_{\eta_j}p_{y_j}-b_{y_j}p_{\eta_j})
=H_b p=-H_p b.
\tag{3}
\]
Thus the coefficient \(i/2\) multiplying this bracket below has the opposite sign from \(1/(2i)\).

For a homogeneous scalar \(g\) whose degree is greater than \(-n\), define a density on \(X\) by
\[
I_g(y,\lambda)=\int_{p(y,\eta)<\lambda}g(y,\eta)\,d\eta,
\qquad \lambda>0.
\tag{4}
\]
The displayed coefficient is relative to \(|dy|\). Intrinsically, integration of this density against a function \(h\) means integration of \(h(y)g(y,\eta)\) with the symplectic volume \(dy\,d\eta\) over that sublevel set. This definition is invariant under a change of cotangent coordinates.

If \(g\) has degree \(d\), then
\[
I_g(y,\lambda)=\lambda^{n+d}I_g(y,1).
\tag{5}
\]
The positive ellipticity of \(p\) makes its unit sublevel set bounded, and the degree assumption gives integrability at zero. In particular, \(I_b\) has degree \(n\), \(I_{b_s}\) has degree \(n-1\), and both \(I_{p_sb}\) and \(I_{\{b,p\}}\) have degree \(n\).

<a id="density-divergence"></a>

**Integration facts used below.** The [coordinate and surface proof, (CI4)–(CI7)](../providers/analysis/coordinate-inverses-and-integration.md#surface-coordinates), supplies change of variables, area and regular-level coarea. In general dimension its polar Jacobian is $r^{n-1}$: in a local unit-sphere chart the radial derivative is the unit normal, perpendicular to the angular derivatives, and each of the $n-1$ angular columns gains a factor $r$. The determinant and Gram-area formulas therefore give $d\eta=r^{n-1}dr\,d\omega$. This proves the polar formula used here in every dimension.

We also need the divergence theorem, which can be proved with these same inputs. For a smooth vector field $V$ supported in a boundary chart where the domain is $z_n<h(z')$, the fundamental theorem gives
\[
 \int_D\partial_{z_n}V_n=\int V_n(z',h(z'))\,dz',\qquad
 \int_D\partial_{z_j}V_j=-\int V_j(z',h(z'))\,\partial_{z_j}h\,dz'
 \quad(j<n).
\]
For the second equality, differentiate the variable-upper-limit integral of $V_j$ and integrate its compactly supported total derivative in $z_j$. Their sum is $\int_{\partial D}V\cdot\nu\,dS$, because the outward area-normal is $(-\nabla h,1)\,dz'$. An orthogonal coordinate change gives each boundary graph; local inversion supplies it. A finite smooth partition reduces a compact smooth domain to these charts and interior charts. Interior derivative integrals vanish by the fundamental theorem, and the terms differentiating the partition cancel because its sum is one. This proves the formula on such domains, including annuli. In canonical cotangent charts the same calculation uses $dy\,d\eta$; its invariance and the same partition cancellation give the compact-manifold version. Complex vector fields are handled by their real and imaginary parts. Every later use below is on a compact annulus away from the zero covector, with its omitted inner flux estimated explicitly.

<a id="density-moving-boundary"></a>

## 2. A moving energy boundary

Let \(y\) range over a compact part of a coordinate patch. Suppose that \(\mu(t,y,\eta)\) is real, smooth away from \(\eta=0\), positive and homogeneous of degree one in \(\eta\), for small \(|t|\). Let \(f(t,y,\eta)\) be a classical order-zero symbol, compactly supported in \(y\), and zero for \(|\eta|<1\). Set
\[
F(t,y,\lambda)=
\int_{\mu(t,y,\eta)<\lambda}f(t,y,\eta)\,d\eta.
\tag{6}
\]

**Lemma 2.1.** The function \(F\) is smooth and belongs to \(S^n\), uniformly on compact small-time intervals. Its derivative \(F_\lambda\) is classical of order \(n-1\). If
\[
\mu(0,y,\eta)=p(y,\eta),\qquad
\mu_t(0,y,\eta)=-\frac12p_\eta\cdot p_y,
\tag{7}
\]
then
\[
F(0,y,\lambda)=\int_{p<\lambda}f(0,y,\eta)\,d\eta,
\]
\[
F_t(0,y,\lambda)
=\int_{p<\lambda}
\left(f_t+\frac12\operatorname{div}_\eta(fp_y)\right)(0,y,\eta)\,d\eta.
\tag{8}
\]
The cumulative integral \(F\) can have a logarithmic term in its full expansion.

**Proof.** Write \(\eta=r\omega\), \(|\omega|=1\), and \(m(t,y,\omega)=\mu(t,y,\omega)\). Positivity and compactness give fixed bounds \(0<c\leq m\leq C\). For \(\lambda>0\),
\[
F_\lambda(t,y,\lambda)
=\lambda^{n-1}
\int_{S^{n-1}}
f\left(t,y,\frac{\lambda\omega}{m(t,y,\omega)}\right)
m(t,y,\omega)^{-n}\,d\omega.
\tag{9}
\]
For \(\lambda\) near zero this expression is zero. It extends smoothly by zero to negative \(\lambda\).

Every \(\lambda\)-derivative in (9) lowers its symbol order by one. A \(t\)- or \(y\)-derivative of the argument inserts a factor \(O(\lambda)\) and one frequency derivative of \(f\), so preserves the order. The fixed compact sphere permits differentiation under the integral. Applying the same argument to each homogeneous term of \(f\), and then its symbol remainder, proves that \(F_\lambda\) is classical of order \(n-1\).

Integrating (9) from zero gives the bound \(O(\lambda^n)\), including every \(t,y\) derivative. Its higher \(\lambda\)-derivatives are controlled by (9). This proves \(F\in S^n\), with smoothness also at small and negative \(\lambda\).

To differentiate the moving boundary, write (6) with the Heaviside function:
\[
F=\int f\,H(\lambda-\mu)\,d\eta.
\]
The polar formula just proved justifies differentiation, giving
\[
F_t=\int_{\mu<\lambda} f_t\,d\eta
-\int f\mu_t\,\delta(\lambda-\mu)\,d\eta.
\tag{10}
\]
At \(t=0\), (7) makes the second term
\[
\frac12\int_{p=\lambda}
f\,\frac{p_y\cdot p_\eta}{|p_\eta|}\,dS
=\frac12\int_{p<\lambda}
\operatorname{div}_\eta(fp_y)\,d\eta.
\]
The surface is regular since Euler's identity gives \(p_\eta\cdot\eta=p>0\). The divergence theorem is applied away from zero; \(f\) vanishes there, so no inner boundary contributes. This proves (8).

Finally a homogeneous component of \(f\) of degree \(-n\) contributes a multiple of \(\lambda^{-1}\) to (9). Its primitive is a multiple of \(\log\lambda\). A smooth cutoff of \(|\eta|^{-n}\) is a direct example. Thus \(F_\lambda\) has a classical expansion even when \(F\) does not. ∎

<a id="density-small-time-phase"></a>

## 3. A phase adapted to small time

For small time the flow \((x,\xi)=\chi_t(y,\eta)\) can be parametrized by \((t,x,\eta)\). Indeed \(x=y\) at zero, so its derivative with respect to \(y\) is the identity there. The inverse function theorem and compact normalized cotangent patches give a common small time on each fixed chart piece.

The graph normal form supplies a homogeneous generating phase \(\psi(t,x,\eta)\) with
\[
\psi(0,x,\eta)=x\cdot\eta,\qquad
\psi_t+p(x,\psi_x)=0.
\tag{11}
\]
For this flow the construction is also explicit. Let \(y=y(t,x,\eta)\) be its inverse base point. The Liouville identity in the preceding lesson gives
\[
\xi\cdot dx-\eta\cdot dy=p\,dt.
\]
Consequently \(\psi=\eta\cdot y(t,x,\eta)\) has differential
\(\xi\cdot dx+y\cdot d\eta-p\,dt\), proving (11) and the required generating relations.

On the diagonal put
\[
\psi(t,y,\eta)-y\cdot\eta=-t\mu(t,y,\eta).
\tag{12}
\]
The right side defines a smooth degree-one \(\mu\) through \(t=0\). Differentiating (11) there yields
\[
\psi_t(0,y,\eta)=-p(y,\eta),\qquad
\psi_{tt}(0,y,\eta)=p_\eta(y,\eta)\cdot p_y(y,\eta).
\]
These identities give exactly (7). For sufficiently small time, \(\mu\) remains positive.

The preceding wave lesson constructs the amplitude directly with no input-base dependence: solve its finite recursion (T11) with initial amplitude one, and solve every lower transport equation with initial value zero, then use its differentiated cutoff sum and smooth-residual argument. For an inner coordinate patch, compactness of the unit frequency sphere gives a common small time for the inverse base map above and for all its differentiated estimates. The phase $\psi=\eta\cdot y(t,x,\eta)$ is the same on angular overlaps, so the finitely many angular amplitudes sum in this one phase. Base cutoffs equal to one around the corresponding short trajectories affect the kernel on the smaller patch only by smooth terms, by the proved nonstationary estimates. The resulting amplitude is independent of the input base variable and gives, modulo a jointly smooth kernel,
\[
K_E(t,x,y)=(2\pi)^{-n}
\int e^{i(\psi(t,x,\eta)-y\cdot\eta)}
a(t,x,\eta)\,d\eta,\qquad a\in S^0_{\mathrm{cl}}.
\tag{13}
\]
The phase order and amplitude order agree with the joint-time order \(-1/4\). Here $a$ is the ordinary fixed-time amplitude: the normalized joint half-density amplitude is $(2\pi)^{1/4}a$, by (G18) and (R11)–(R13). This distinction leaves the displayed Fourier factor $(2\pi)^{-n}$ unchanged. Low frequencies may be put in the smooth remainder. The bounds in (T1), its classical summation and the compact-time transport integral prove every $t,x,\eta$ derivative estimate for this same amplitude.

The initial identity gives \(a(0,x,\eta)=1\) modulo a rapidly decreasing symbol. At zero the equation \((D_t+P)E=0\) gives
\[
-i a_t(0,y,\eta)-p(y,\eta)+P_L(y,\eta)=0
\quad\bmod S^{-\infty}.
\]
In particular,
\[
-i a_t(0,y,\eta)
=-p_s(y,\eta)+\frac i2\sum_jp_{y_j\eta_j}(y,\eta)
\quad\bmod S^{-1}.
\tag{14}
\]
This calculation uses the exact left symbol at the initial time; it does not replace that symbol by its principal part.

<a id="density-amplitude-reduction"></a>

## 4. Remove time from the amplitude

We prove an exact one-dimensional amplitude reduction. If \(q(t,y,\lambda)\) is an ordinary symbol, with compact small-time support and \(y\) a smooth parameter, then
\[
\int e^{-it\lambda}q(t,y,\lambda)\,d\lambda
=\int e^{-it\lambda}q^\sharp(y,\lambda)\,d\lambda,
\]
\[
q^\sharp\sim
\sum_{j\geq0}\frac{(-i)^j}{j!}
\partial_\lambda^j\partial_t^j q(0,y,\lambda).
\tag{15}
\]
The remainder after \(j<N\) has \(N\) fewer frequency orders, with all parameter derivatives. To see this directly, set
\[
\widetilde q(\rho,y,\mu)=\int e^{-it\rho}q(t,y,\mu)\,dt.
\]
Fourier inversion in time gives the exact symbol
\[
q^\sharp(y,\lambda)=\frac1{2\pi}
 \int\widetilde q(\rho,y,\lambda+\rho)\,d\rho.
\]
The compact time support and integration by parts give, for every \(M\),
\[
|\partial_y^\alpha\partial_\mu^k\widetilde q(\rho,y,\mu)|
 \leq C_{\alpha kM}\langle\rho\rangle^{-M}
                         \langle\mu\rangle^{m-k}
\]
when \(q\) has order \(m\). For each \(M\) only finitely many time and symbol seminorms occur. In the integral split
\(|\rho|\leq\langle\lambda\rangle/2\) from its complement. On the first region, Taylor expansion in the last argument about \(\lambda\), to order \(N-1\), leaves
\(O(\langle\lambda\rangle^{m-N}\langle\rho\rangle^N)\)
times an arbitrarily rapidly decreasing factor in \(\rho\). On the complement, the same rapid decrease absorbs all polynomial growth in \(\lambda+\rho\), including its bounded-frequency region. Choosing \(M\) sufficiently large makes the integral there smaller than any required inverse power of \(\langle\lambda\rangle\). The truncated Taylor terms on this complement have the same property. The argument applies after all \(y\) and \(\lambda\) derivatives, proving the stated remainder estimate.

Finally Fourier inversion gives
\[
\frac1{2\pi}\int\rho^j\widetilde q(\rho,y,\lambda)\,d\rho
 =(-i)^j\partial_t^j q(0,y,\lambda),
\]
which proves (15). To justify the distributional equality, first multiply $q$ by a smooth bounded-frequency cutoff. Fourier inversion and the displayed absolutely convergent $\rho$ integral give the identity for that cutoff amplitude. The cutoffs have uniform symbol bounds and converge on every compact frequency set. Their reduced symbols therefore have uniform polynomial bounds, converge on bounded frequencies by dominated convergence, and converge against every rapidly decreasing Fourier test. This proves the identity in the distributional limit; the same argument after any $y$ derivative proves the parameter statement. When $q$ is classical, apply (15) to any finite homogeneous expansion of $q$ and its differentiated lower-order remainder. Each retained coefficient is homogeneous of its indicated degree at large frequency; the estimates just proved control the remainder to arbitrary order. Thus $q^\sharp$ is classical. If $q$ is zero for sufficiently negative frequency, its reduced symbol is rapidly decreasing as $\lambda\to-\infty$: where $\lambda+\rho$ lies in the support, $|\rho|$ is a fixed multiple of $|\lambda|$ or larger, and arbitrarily many powers of its rapid decrease absorb the integral. This is the Taylor and rapidly decreasing convolution mechanism compared with [HS, equation (4.12)].

The first sign can be checked directly:
\(t e^{-it\lambda}=i\partial_\lambda e^{-it\lambda}\).
Integration by parts therefore puts \(-i\partial_\lambda\) on the amplitude. A smooth compactly supported remainder in \(t\) contributes a rapidly decreasing \(q^\sharp\).

<a id="density-primitive-remainder"></a>

Apply (15) to \(q=F_\lambda\) from Lemma 2.1. It gives a classical symbol of order \(n-1\) and
\[
q^\sharp
=F_\lambda(0,y,\lambda)
-iF_{t\lambda\lambda}(0,y,\lambda)+S^{n-3}_{\mathrm{cl}}.
\tag{16}
\]
Choose its primitive \(A\) with \(A(y,0)=0\). Then \(A\in S^n\). Integrating the remainder in (16) shows
\[
A=F(0,y,\lambda)-iF_{t\lambda}(0,y,\lambda)+R,
\tag{17}
\]
where \(R\in S^{n-2}\) when \(n\geq3\). In dimension two it instead satisfies
\[
|\partial_y^\alpha R|\leq C_\alpha\log(2+\lambda),
\qquad
|\partial_y^\alpha\partial_\lambda^k R|
\leq C_{\alpha k}(1+\lambda)^{-k},\quad k\geq1,
\tag{18}
\]
for \(\lambda\geq1\). Thus \(R\in S^\varepsilon\) for every \(\varepsilon>0\), and \(R=o(\lambda)\). The normalization adds a smooth density independent of \(\lambda\), compatible with these bounds.

These estimates follow just by integrating a symbol of order \(n-3\). At \(n=2\) that order is \(-1\), whose integral can grow logarithmically. The derivative formulation (16) retains its ordinary symbol order in every dimension considered here.

<a id="density-local-coefficients"></a>

## 5. The local coefficient calculation

Let \(K_B(t,y)\) be the diagonal restriction of the kernel of \(E(t)B\), a density on \(X\) with distributional dependence on \(t\). Composition with the pseudodifferential identity relation leaves its wavefront inside the wave relation by the [transverse composition proof](../providers/analysis/transverse-composition-and-graph-operators.md#transverse-composition). Its nonzero time covector excludes the diagonal conormal, so (R1)–(R2) give this actual restriction; the spatial half densities multiply to a density as in (R13) and the discussion following it.

The subprincipal and Poisson-bracket coefficients appear in Hörmander [H4, Proposition 29.1.2]; the moving-boundary calculation is Lemma 29.1.3 there.

**Theorem 5.1 (the first two local spectral coefficients).** Near \(t=0\), \(K_B\) is conormal to \(\{0\}\times X\). There is \(A\in S^n(X\times\mathbb R;\Omega_X)\), normalized by \(A(y,0)=0\), such that for sufficiently small time
\[
K_B(t,y)=\int e^{-it\lambda}\partial_\lambda A(y,\lambda)\,d\lambda.
\tag{19}
\]
Its derivative is classical and obeys
\[
\partial_\lambda A
-(2\pi)^{-n}
\left[
\partial_\lambda(I_b+I_{b_s})
-\partial_\lambda^2 I_{p_sb+(i/2)\{b,p\}}
\right]\in S^{n-3}_{\mathrm{cl}}.
\tag{20}
\]
Equivalently,
\[
A=(2\pi)^{-n}
\left[I_b+I_{b_s}
-\partial_\lambda I_{p_sb+(i/2)\{b,p\}}\right]+R,
\tag{21}
\]
with \(R\in S^{n-2}\) for \(n\geq3\), and the logarithmic bounds (18) for \(n=2\). All homogeneous integrals in these formulas are evaluated at \((y,\lambda)\).

The coefficient formulas are assertions for large positive $\lambda$. To read (20) as an assertion on the whole real line, extend each displayed homogeneous coefficient with a smooth cutoff equal to one for large positive $\lambda$ and zero near zero and on the negative half-line. Any two such extensions differ by a compact-frequency smooth term. The reduced derivative is rapidly decreasing at negative infinity by Section 4. Its primitive there is bounded with rapidly decreasing derivatives, so the global assertion $A\in S^n$ and the normalization at zero are compatible with these positive-energy formulas.

**Proof.** Localize \(B\) to compact coordinate pieces; the off-diagonal smooth parts remain smooth after wave evolution. First compute with \(C=B^*\), and write
\(c=\overline b\), \(c_s=\overline{b_s}\).
Fourier inversion in the middle variable in (13) gives
\[
K_{B^*}(t,y)
=(2\pi)^{-n}\int e^{-it\mu(t,y,\eta)}
a(t,y,\eta)\overline{B_L(y,\eta)}\,d\eta
\quad\bmod C^\infty.
\tag{22}
\]
Indeed the kernel of $B^*$ is $(2\pi)^{-n}\int e^{i(z-y)\cdot\zeta}\overline{B_L(y,\zeta)}\,d\zeta$. The phase in its product with (13) is $\psi(t,x,\eta)-z\cdot\eta+(z-y)\cdot\zeta$. Fourier inversion in $z$ sets $\zeta=\eta$ with factor $(2\pi)^n$, giving (22) on the diagonal. This can first be done with bounded frequencies and a Gaussian cutoff in $z$, whose Fourier transform converges to that delta; the Fourier inversion proof supplies the distributional limit. Proper base cutoffs are one on the smaller set of matching covectors. Their other terms are smooth by the nonmatching part of the composition proof. Finally $|\mu+t\mu_t|\ge c|\eta|$ at small time, so integration by parts in $t$ after testing gives arbitrary frequency decay. The uniform differentiated symbol bounds then pass the frequency cutoffs to the joint distributional limit, including every base derivative. Qualified restriction agrees with that limit by (R3)–(R8).

Choose a time cutoff equal to one near zero, with support where (22) holds, and include it in
\(f=(2\pi)^{-n}a\overline{B_L}\).
A cutoff near zero frequency only changes a smooth kernel. Lemma 2.1 writes the integral as
\(\int e^{-it\lambda}F_\lambda(t,y,\lambda)\,d\lambda\).
The amplitude reduction gives (19), with the smooth time-localized error included by its rapidly decreasing Fourier symbol. It proves conormality and the existence of the normalized primitive.

It remains to calculate the two coefficients. Put
\[
d_p=\sum_j p_{y_j\eta_j},\qquad
d_c=\sum_j c_{y_j\eta_j}.
\]
Equation (2) gives
\[
\overline{B_L}=c+c_s+\frac i2 d_c+S^{-2},
\qquad
p_0=p_s-\frac i2 d_p.
\tag{23}
\]
The initial amplitude is one modulo a rapidly decreasing symbol, and \(a_t=-ip_0+S^{-1}\). Thus the degree-zero part of \(-i(2\pi)^nF_t\), using (8), is the integral of
\[
-p_0c-\frac i2\operatorname{div}_\eta(cp_y)
=-p_sc-\frac i2 c_\eta\cdot p_y.
\tag{24}
\]
The two \(c\,d_p\) terms cancel. Consequently (17), through the first two degrees, is
\[
(2\pi)^n A=
I_c+I_{c_s}+\frac i2 I_{d_c}
-\partial_\lambda I_{p_sc+(i/2)c_\eta\cdot p_y}
+R.
\tag{25}
\]
The notation \(R\) here absorbs the harmless fixed factor and has the asserted bounds.

The divergence theorem gives the exact homogeneous identity
\[
I_{d_c}=\partial_\lambda I_{c_y\cdot p_\eta}.
\tag{26}
\]
Indeed both sides equal
\(\int_{p=\lambda}c_y\cdot p_\eta/|p_\eta|\,dS\).
An inner cutoff tending to zero contributes \(O(\varepsilon^{n-1})\), since \(c_y\) has degree zero and \(n\geq2\); it therefore disappears.

Substitute (26) into (25). The remaining two terms combine into
\((i/2)(c_\eta\cdot p_y-c_y\cdot p_\eta)=(i/2)\{c,p\}\).
This proves (20)–(21) for \(B^*\). Every order-zero scalar operator is the adjoint of another such operator, whose principal and subprincipal symbols conjugate in exactly the way used in (23). Renaming this arbitrary operator gives the stated formula for \(B\).

For completeness, the remainder assertion may be checked before taking a primitive. A degree-\(-2\) amplitude in Lemma 2.1 contributes to \(F_\lambda\) at order \(n-3\), including at \(n=2\). Terms of order \(-1\) in \(F_t\), after two \(\lambda\)-derivatives, have that same order. Every subsequent term of (15) is at most order \(n-3\). The classical polar expansion proves (20). Its primitive gives exactly the two alternatives stated in (21); no bounded primitive is assumed at order \(-1\).

All terms \(b,b_s,p_s,\{b,p\}\) are invariant scalar cotangent symbols. The symplectic definition (4) makes their integrals densities. Finite coordinate and angular partitions therefore assemble the calculation over \(X\), with the same symbol remainder bounds. ∎

The function \(A\) is a smooth high-frequency model for a time-localized spectral density. It is not the step function of the actual spectral projection. Passing from this local model to an unsmoothed counting estimate requires a separate Tauberian argument.

<a id="density-trace"></a>

## 6. A trace and a logarithm

The bracket term disappears after integrating over the whole compact manifold:
\[
\int_X I_{\{b,p\}}(y,\lambda)=0.
\tag{27}
\]
To prove this, use \(\{b,p\}=-H_p b\) and the fact that \(H_p\) preserves symplectic volume. On the annulus \(\varepsilon<p<\lambda\), the field is tangent to both energy boundaries. The divergence theorem gives zero there. The omitted integral is \(O(\varepsilon^n)\) by degree zero and positive ellipticity, so it tends to zero.

More explicitly, in each canonical chart $\operatorname{div}H_p=\sum_j(p_{\eta_jy_j}-p_{y_j\eta_j})=0$ and $H_pp=0$. Hence $\operatorname{div}(bH_p)=H_pb$, with zero boundary flux on that energy annulus. The integration proof in Section 1 and a finite cotangent partition give its global integral zero; no separate volume-preservation theorem is required for this step.

Thus a primitive for the distributional trace has its first two terms
\[
(2\pi)^{-n}
\left[
\int_{p<\lambda}(b+b_s)\,dy\,d\eta
-\partial_\lambda\int_{p<\lambda}p_sb\,dy\,d\eta
\right].
\tag{28}
\]
For \(B=I\), the principal term is cotangent volume and the next is the derivative of the integrated subprincipal symbol.

<a id="density-torus-multipliers"></a>

**The torus multipliers used in the examples.** We justify their local symbols. For $a(\eta)\in S^r(\mathbb R^n)$, let $k_a$ be its inverse Fourier distribution. Away from zero it and all its derivatives decrease faster than every power of the spatial distance at infinity. To see this, integrate repeatedly in $\eta$ using $z\cdot\partial_\eta/(i|z|^2)$; after more than $r+n$ transfers the differentiated symbol is integrable, and further transfers give any required inverse power of $|z|$. The same argument after a fixed $z$ derivative starts from a symbol of a correspondingly higher finite order and still works. Frequency cutoffs justify the limit by the Fourier distribution construction.

The periodization $\sum_{m\in\mathbb Z^n}k_a(z+2\pi m)$ therefore converges as a periodic distribution. Near $z=0$ its terms with $m\ne0$ sum to a smooth function with every derivative, by the just-proved summable bounds. Its local kernel is consequently the ordinary pseudodifferential kernel with symbol $a$, modulo smooth terms. Its coefficient on the Fourier mode $e^{ik\cdot x}$ is $a(k)$: unfold the fundamental cell in the distributional pairing to $\mathbb R^n$ and use Fourier inversion. More explicitly, insert a growing smooth spatial cutoff in that unfolded pairing; its Fourier transform is an approximate identity at $k$, whose convolution with the smooth polynomially bounded $a$ tends to $a(k)$. The rapid kernel tails justify removing the cutoff. This proves the claimed multiplier and local-symbol identity with normalization $(2\pi)^{-n}$.

For completeness these modes span $L^2$ on the torus. In one variable the nonnegative kernel
\[
 F_N(x)=\frac1N\left|\sum_{j=0}^{N-1}e^{ijx}\right|^2
\]
has integral $2\pi$, by integrating its finite expansion, and satisfies $F_N(x)\le [N\sin^2(x/2)]^{-1}$ off zero, by summing the geometric series. Its normalized convolution therefore tends uniformly to every continuous periodic function: split the integral into a small neighborhood where uniform continuity applies and its complement, whose mass tends to zero. Products of these kernels prove the same assertion in $n$ variables. The resulting convolutions are trigonometric polynomials. Continuous functions are dense in $L^2$ by the earlier compact smooth-approximation argument, so the modes are complete. In particular, bounded real multipliers are symmetric and bounded with norm at most the supremum of their mode values. These arguments supply the multiplier facts used both here and in Solution 7.4.

<a id="density-logarithm"></a>

**Example 6.1 (the two-dimensional logarithm).** Take a flat two-dimensional torus. Choose a positive scalar Fourier multiplier \(P\) whose symbol equals \(|\eta|\) for \(|\eta|\geq2\). Choose the order-\(-2\) multiplier \(B\) with symbol
\[
\beta(\eta)=\theta(|\eta|)|\eta|^{-2},
\]
where \(\theta=0\) near zero and \(\theta=1\) for radius at least two. This is also a classical order-zero operator, with \(b=b_s=0\).

Near the initial diagonal the high-frequency wave phase is
\((x-y)\cdot\eta-t|\eta|\), with amplitude one modulo rapidly decreasing symbols. All higher amplitude equations there have constant principal coefficients and zero lower homogeneous terms, so their corrections vanish. The smooth-error result of the wave lesson identifies this local parametrix with the true kernel modulo a smooth kernel. Its diagonal product with \(B\) is therefore, up to that same type of error,
\[
(2\pi)^{-2}\int_{\mathbb R^2}
e^{-it|\eta|}\theta(|\eta|)|\eta|^{-2}\,d\eta
=\frac1{2\pi}\int_0^\infty
e^{-it\lambda}\frac{\theta(\lambda)}{\lambda}\,d\lambda.
\tag{29}
\]
The local time cutoff changes the reduced amplitude only by a rapidly decreasing symbol, because its derivatives vanish at zero in (15). Hence
\[
A_\lambda(y,\lambda)=\frac1{2\pi\lambda}+S^{-\infty}
\quad(\lambda\geq2),
\]
\[
A(y,\lambda)=\frac1{2\pi}\log\lambda+O(1).
\tag{30}
\]
A bounded \(S^0\) primitive is impossible. This example explains why the dimension-two remainder in (21) includes a logarithm, even though the derivative remainder (20) is an ordinary classical symbol.

### Use the conclusion

Follow the Fourier-phase sign through the local calculation and separate the local coefficient from its spatial trace. Compare the moving energy boundary with the later boundary-wall calculation: they measure different boundaries.

<a id="density-solutions"></a>

## 7. Exercises and complete solutions

**Exercise 7.1 (a constant spectral shift; introductory).** Replace \(P\) by \(P+cI\), with real \(c\). Derive the change in the first two terms of \(A\), and compare it with translating the energy variable.

**Solution 7.1.** The principal symbol remains \(p\), while \(p_s\) becomes \(p_s+c\). Formula (21) therefore adds
\[
-(2\pi)^{-n}c\,\partial_\lambda I_b.
\]
The group gains the factor \(e^{-ict}\), so its reduced spectral density translates from \(\lambda\) to \(\lambda-c\). A normalized primitive is
\(A_{P,B}(\lambda-c)-A_{P,B}(-c)\).
Taylor expansion of its degree-\(n\) term gives
\(I_b(\lambda-c)=I_b(\lambda)-c\partial_\lambda I_b(\lambda)+O(\lambda^{n-2})\).
Translation of the degree-\(n-1\) terms changes only the next remainder. The constant normalization is allowed by the remainder bounds, including in dimension two. Both computations agree.

**Exercise 7.2 (an expanding energy surface; intermediate).** In Euclidean cotangent coordinates let
\(\mu(t,\eta)=(1+\gamma t)|\eta|\).
For a radial cutoff \(f(\eta)\) equal to one above radius two and zero below radius one, compute the large-\(\lambda\) value of \(F_t(0,\lambda)\). Check the sign by (10).

**Solution 7.2.** For large \(\lambda\),
\[
F(t,\lambda)
=v_n\left(\frac{\lambda}{1+\gamma t}\right)^n+C_f,
\]
where \(v_n\) is the volume of the unit ball and the fixed cutoff correction \(C_f\) is independent of \(t\). Thus
\[
F_t(0,\lambda)=-n\gamma v_n\lambda^n.
\]
In (10), \(f_t=0\) and \(\mu_t=\gamma|\eta|\). The boundary lies at radius \(\lambda\), where \(f=1\), so the negative boundary term equals
\(-\gamma\lambda |S^{n-1}|\lambda^{n-1}=-n\gamma v_n\lambda^n\).
An increase of \(\mu\) shrinks the sublevel set, agreeing with the sign.

**Exercise 7.3 (the resonant homogeneous degree; intermediate).** Take \(\mu=|\eta|\) and
\(f(y,\eta)=h(y)\theta(|\eta|)|\eta|^{-n}\),
with smooth compactly supported \(h\) and the cutoff from Example 6.1. Find \(F\) and \(F_\lambda\) for large \(\lambda\). Explain which classical assertion about \(F\) fails.

**Solution 7.3.** Polar integration gives
\[
F(y,\lambda)=h(y)|S^{n-1}|\log\lambda+C(y),
\qquad
F_\lambda(y,\lambda)=h(y)|S^{n-1}|\lambda^{-1}
\]
for \(\lambda\geq2\). The derivative is classical of order \(-1\), hence also of order \(n-1\) with its higher homogeneous coefficients zero. The primitive lies in \(S^n\), but if \(h\neq0\) it is not classical of order \(n\): all its positive-degree homogeneous coefficients would have to vanish, and a degree-zero coefficient cannot approximate its growing logarithm modulo \(S^{-1}\). It is also not bounded \(S^0\). The resonant degree is exactly \(-n\) in the original integrand.

**Exercise 7.4 (a local imaginary correction; advanced).** On a flat torus let \(p(\eta)=|\eta|\), with \(p_s=0\), and let \(G\) be a real smooth periodic function. Let \(T\) be a symmetric Fourier multiplier with high-frequency symbol \(\eta_1/|\eta|\), and put
\[
B=\frac12(GT+TG).
\]
Show that \(b=G\eta_1/|\eta|\) and \(b_s=0\). Compute the first nonzero term of its local primitive \(A\), and explain its spatial integral.

**Solution 7.4.** The left product formula gives
\[
B_L=G\frac{\eta_1}{|\eta|}
-\frac i2\sum_j G_{y_j}
\partial_{\eta_j}\left(\frac{\eta_1}{|\eta|}\right)
+S^{-2}.
\]
Adding the subprincipal correction in (2) cancels its displayed degree-\(-1\) term, so \(b_s=0\). Both \(G\) and \(T\) are bounded symmetric operators; their symmetrized product is symmetric.

Angular oddness gives \(I_b=0\). By (3),
\[
\{b,p\}
=-\frac{\eta_1}{|\eta|}
\sum_jG_{y_j}\frac{\eta_j}{|\eta|}.
\]
The spherical second moments are
\(\int_{S^{n-1}}\omega_1\omega_j\,d\omega
=v_n\delta_{1j}\).
For $j\ne1$ reflect the $j$th coordinate to see the integral is zero. Rotations make the diagonal moments equal; their sum is $|S^{n-1}|$ since $\sum\omega_j^2=1$. The polar formula in Section 1 gives $|S^{n-1}|=nv_n$, proving the stated diagonal value.
Radial integration therefore gives
\[
I_{\{b,p\}}
=-\frac{v_n}{n}G_{y_1}\lambda^n.
\]
Formula (21) yields the local term
\[
A(y,\lambda)=
\frac{i\,v_n}{2(2\pi)^n}G_{y_1}(y)\lambda^{n-1}+R.
\tag{31}
\]
It can be imaginary because the diagonal of \(E(t)B\) is not the diagonal of a symmetric operator at general \(t\). Its spatial integral vanishes by periodicity of \(G\), agreeing with (27) and the real trace coefficients for a symmetric \(B\).

**Exercise 7.5 (why two coefficients do not determine a count; advanced).** Explain why (19)–(21) do not alone prove that the actual spectral counting function equals the two displayed terms plus \(o(\lambda^{n-1})\). For the logarithmic example, explain why the corrected primitive remainder still does not obstruct such a two-term scale.

**Solution 7.5.** The equality is restricted to small time after a smooth time localization. Fourier transformation therefore smooths the energy measure. The actual spectral projection is a discontinuous step function, and returning classical trajectories may produce singularities at later times. Their effect on the unsmoothed energy remainder is not estimated by the local symbol calculation. A quantitative Tauberian comparison, together with appropriate return-time information, is needed to reach that counting conclusion.

In dimension two, \(\log\lambda=o(\lambda)\), so the logarithmic primitive remainder is smaller than the second-term scale \(\lambda^{n-1}=\lambda\). It corrects a symbol-order assertion without changing the scale of a subsequent two-term counting result. It supplies no missing Tauberian estimate.

**Comparison with the systems formula.** Theorems 2.1 and 3.1 in [AFV] concern a first-order differential operator with a Hermitian matrix principal symbol and simple eigenvalues. Its branches carry normalized eigenvectors; the second coefficient includes their derivatives and curvature as well as the projected subprincipal symbol. Those hypotheses and terms are essential. Equations (23)–(26) above derive our coefficient for an arbitrary scalar inserted operator, including its local Poisson bracket, directly. For \(B=I\), spatial integration removes that bracket and leaves precisely the scalar subprincipal contribution. This is the appropriate point of comparison with the systems result.

The primitive estimate in [AFV, equation (3.7)] has a logarithmic remainder in dimension two. Our polar integration proves the same mechanism: an order \(-1\) derivative integrates to a logarithm. It justifies retaining (18) while (20) still has its claimed classical derivative order. Hörmander's Theorem 4.4 supplies the leading unsmoothed local remainder, and Theorem 4.5 treats Riesz means. Neither statement alone identifies our explicit scalar second coefficient or removes the return-time hypothesis needed for an unsmoothed two-term count.

## References

- [HS] Lars Hörmander, “The spectral function of an elliptic operator,” *Acta Mathematica* 121 (1968), 193–218. Section 4, especially equation (4.12) and Theorems 4.4–4.5. [Full article](https://projecteuclid.org/journalArticle/Download?urlid=10.1007%2FBF02391913).
- [AFV] Zhirayr Avetisyan, Yan-Long Fang and Dmitri Vassiliev, *Spectral asymptotics for first order systems*, arXiv:1512.06281v2 (2016). Sections 2–3. [Author preprint](https://arxiv.org/abs/1512.06281v2).
- [GS] Victor Guillemin and Shlomo Sternberg, *Semi-classical analysis*, author text dated April 25, 2012. Introduction Section 0.5, printed pages xi–xii, for the semiclassical functional-calculus and trace comparison. [Author PDF](https://people.math.harvard.edu/~shlomo/docs/Semi_Classical_Analysis_Start.pdf).
- [DG] Johannes J. Duistermaat and Victor W. Guillemin, “The spectrum of positive elliptic operators and periodic bicharacteristics,” *Inventiones Mathematicae* 29 (1975), 39–79. Introduction for the classical positive-elliptic and wave-trace setting. [Freely readable complete GDZ scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0029/LOG_0010.pdf).
- [H3] Lars Hörmander, *The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*, reprint of the 1994 edition, Springer, 2007, (18.1.32), p. 83, and Theorems 18.1.33–18.1.34, pp. 92–93. ISBN 978-3-540-49938-1. [Edition information](https://doi.org/10.1007/978-3-540-49938-1).
- [H4] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, reprint of the 1994 edition, Springer, 2009, Proposition 29.1.2 and Lemma 29.1.3, pp. 253–256. ISBN 978-3-642-00136-9. [Edition information](https://doi.org/10.1007/978-3-642-00136-9).
