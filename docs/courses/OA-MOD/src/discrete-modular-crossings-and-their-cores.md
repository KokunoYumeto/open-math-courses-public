# Discrete modular crossings and their cores

Sampling a modular group at one nonzero time changes the type of a type III₁ factor in a precisely controlled way. The new continuous core has a circle in its centre. A change of coordinates identifies that circle and the exact speed of its rotation.

The proof begins with an arbitrary algebra carrying a faithful normal state. Computing the full Tomita operator gives the modular action on its discrete crossed product. A unitary shear then identifies the entire continuous core, including its dual action.

## 1. The theorem and the earlier proofs

**Theorem 1.1.** Let \(M\) be a factor of type III₁, let \(\varphi\) be a faithful normal state, and let \(T>0\). Set

\[
 \alpha=\sigma_T^\varphi,\qquad
 N=M\rtimes_\alpha\mathbb Z,\qquad
 \lambda=e^{-2\pi/T}.
 \tag{1}
\]

Then \(N\) is a factor of type \(\mathrm{III}_\lambda\). The conclusion does not require approximate finite dimensionality or separable predual. Existence of the stated faithful normal state is a hypothesis.

For any von Neumann algebra \(M\) with such a state, write

\[
 C_\varphi(M)=M\rtimes_{\sigma^\varphi}\mathbb R,
 \qquad \theta_s(\ell_t)=e^{-ist}\ell_t,
 \qquad \theta_s(x)=x.
 \tag{2}
\]

Real Haar measure is \(dt\). If \(E:N\to M\) is the coefficient expectation and \(\psi=\varphi E\), there is a normal isomorphism with normal inverse

\[
 C_\psi(N)\cong C_\varphi(M)\bar\otimes L(\mathbb Z).
 \tag{3}
\]

It sends the coefficient copy of \(x\in M\) to \(x\otimes1\), the real core unitary at time \(t\) to \(\ell_t\otimes1\), and the discrete implementing unitary \(V\) to \(\ell_T\otimes S\), where \(S\delta_n=\delta_{n+1}\). Consequently the central circle coordinate, when \(M\) is type III₁, is

\[
 W=\ell_{-T}V,\qquad \widehat{\sigma^\psi}_s(W)=e^{isT}W.
 \tag{4}
\]

Its least positive flow period is \(2\pi/T\), rather than the modular sampling time \(T\).

Here are the precise earlier inputs.

- Faithful-state modular theory, FS02–FS04 and FS09 constructs the faithful GNS representation, the closed Tomita operator, its full polar domains and the modular group. Spectral calculus, SK04 and SK08 supplies the unbounded spectral domain and transport rules.
- The normal regular construction, NR3–NR4 constructs crossed products in arbitrary faithful normal representations and proves representation independence with normal inverse. We also use NR5 for the precise cocycle change in Section 6.
- Circle Fourier analysis, CC0 proves completeness of the characters and the positive Fejér approximate identities with normalized Haar measure. Tensor commutants, TF6–TF7 proves the centre formula for arbitrary spatial tensor products.
- CORE8, equation CORE.8.f proves \(Z(C(A))^\theta=Z(A)\), with the coefficient embedding understood, for every algebra with a faithful normal semifinite weight.
- MIV2, equation MIV2.h proves, for every nonzero factor \(A\) and every faithful normal semifinite weight \(\omega\),

  \[
   S_+(A):=\left(\bigcap_\rho\operatorname{Sp}\Delta_\rho\right)
                      \cap(0,\infty)
      =\exp\Gamma(\sigma^\omega).
   \tag{5}
  \]

  The intersection is over all faithful normal semifinite weights. The dual-centre kernel theorem, L115, K43 identifies \(\Gamma(\sigma^\omega)\) with the kernel of the dual flow on the whole core centre. Neither result assumes that the factor is already type III.
- The finite-corner trace construction, L18 Section 6 proves that a factor with a nonzero finite projection has a faithful normal semifinite trace. This is the step needed to deduce type III, as opposed to computing only a positive spectral intersection.

These are previously written mathematical proofs. The source context is Takesaki, *Theory of Operator Algebras III*, XVIII.4, Lemma 4.17(i), printed pages 389–390. The regular-coordinate proof below also establishes (3) without a dominant-weight reduction.

## 2. The discrete crossing and its faithful state

Work in the faithful GNS representation \((M,H,\xi)\) of \(\varphi\). Put \(U_t=\Delta_\varphi^{it}\). Thus \(U_t\xi=\xi\) and \(U_txU_t^*=\sigma_t^\varphi(x)\). On \(K=\ell^2(\mathbb Z,H)\), the regular generators are

\[
 [\pi(x)\eta]_n=\alpha^{-n}(x)\eta_n,
 \qquad [V\eta]_n=\eta_{n-1}.
 \tag{6}
\]

They satisfy \(V\pi(x)V^*=\pi(\alpha(x))\), and generate \(N\). We identify \(M\) with \(\pi(M)\) when writing products.

Let \(I_n:H\to K\) be the coordinate inclusion. For a finite polynomial \(X=\sum_j\pi(x_j)V^j\),

\[
 I_k^*XI_l=\alpha^{-k}(x_{k-l}).
 \tag{7}
\]

Compression at \(0\) therefore takes values in \(M\). This remains true on the generated von Neumann algebra: compression is ultraweakly continuous, \(M\) is ultraweakly closed, and the polynomial algebra is ultraweakly dense. Set

\[
 E(X)=I_0^*XI_0\in M.
 \tag{8}
\]

This map is normal, unital, positive and \(M\)-bimodular. For every \(X\in N\), put \(x_j=E(XV^{-j})\). Equation (7) holds with these coefficients by the same ultraweak-density argument. In particular, the diagonal entries are \(\alpha^{-k}(E(X))\).

If \(X\ge0\) and \(E(X)=0\), then
\(\|X^{1/2}I_k\eta\|^2=\langle I_k^*XI_k\eta,\eta\rangle=0\)
for every \(k,\eta\). The coordinate vectors span a dense subspace, so \(X=0\). Thus \(E\) is faithful. The functional

\[
 \psi=\varphi\circ E=\omega_\Omega,
 \qquad \Omega=I_0\xi,
 \tag{9}
\]

is a faithful normal state. Also

\[
 \pi(x)V^n\Omega=I_n\alpha^{-n}(x)\xi.
 \tag{10}
\]

Each \(M\xi\) is dense in \(H\), so \(\Omega\) is cyclic. Faithfulness makes it separating. This is the full faithful GNS representation of \(\psi\).

We need graph density, not merely ultraweak density. For \(z\in\mathbb T\), define \(D_zI_n\eta=z^nI_n\eta\). This is a strongly continuous unitary representation, first on finite-coordinate vectors and then on all vectors by approximation. Its conjugation fixes \(\pi(M)\) and sends \(V\) to \(zV\). Write \(\gamma_z=\operatorname{Ad}D_z\). The weak operator integrals of \(\gamma_z(X)\) exist by integration of bounded continuous vector coefficients and bounded sesquilinear representation. The Fourier coefficient of degree \(j\) is, by (7),

\[
 \int_{\mathbb T}z^{-j}\gamma_z(X)\,dh(z)=\pi(x_j)V^j,
 \tag{11}
\]

where \(h\) is probability Haar measure. Equality of all matrix entries proves equality of these bounded operators.

The positive Fejér kernels from CC0 consequently give

\[
 X_m=\sum_{|j|<m}(1-|j|/m)\pi(x_j)V^j,
 \qquad \|X_m\|\le\|X\|,
 \qquad X_m\longrightarrow X\text{ strongly*}.
 \tag{12}
\]

For the last assertion, fix a vector \(\eta\). The map \(z\mapsto\gamma_z(X)\eta\) is norm continuous at \(1\). Split its Fejér integral into a small neighbourhood of \(1\) and its complement; the first error is uniformly small and the kernel mass on the complement tends to zero. Apply the same argument to \(X^*\). Thus \(X_m\Omega\to X\Omega\) and \(X_m^*\Omega\to X^*\Omega\). Polynomial vectors form a graph core for the Tomita operator of \(\psi\).

## 3. The complete modular operator

Let \(S_\varphi\) and \(S_\psi\) denote the closed Tomita operators. A vector \(I_n a\xi\), with \(a\in M\), is the polynomial vector in (10) for \(x=\alpha^n(a)\). Taking its adjoint polynomial gives

\[
 S_\psi(I_n a\xi)
   =I_{-n}\alpha^n(a^*)\xi
   =I_{-n}U_{nT}S_\varphi(a\xi).
 \tag{13}
\]

The complete domain, including infinite coordinate families, is

\[
 \begin{split}
 D(S_\psi)=\bigl\{\eta=(\eta_n):\;&\eta_n\in D(S_\varphi),\\
                 &\sum_n\|S_\varphi\eta_n\|^2<\infty\bigr\},\\
 (S_\psi\eta)_{-n}&=U_{nT}S_\varphi\eta_n.
 \end{split}
 \tag{14}
\]

Here \(\eta\in K\) already means \(\sum_n\|\eta_n\|^2<\infty\).

To prove this domain equality, the operator displayed in (14) is closed: convergence in its graph implies convergence in every coordinate graph, and the proposed limit has the stated square-summable image. Truncating to finitely many coordinates converges in its graph norm. In each remaining coordinate, \(M\xi\) is a graph core for \(S_\varphi\), by FS03. Thus the finite vectors used in (13) are a graph core for (14). They are also a graph core for \(S_\psi\) by (12), proving equality.

Define

\[
 A=\bigoplus_{n\in\mathbb Z}\Delta_\varphi^{1/2},
 \qquad J_\psi(I_n\eta)=I_{-n}U_{nT}J_\varphi\eta.
 \tag{15}
\]

The second map is an onto antiunitary. It squares to the identity since \(J_\varphi U_t=U_tJ_\varphi\), with this same time sign, as proved in FS04. The direct sum \(A\) is positive self-adjoint on its square-summable spectral domain: the spectral projections act coordinatewise, and their squared-integral domain test is exactly (14). Formula (13) and graph closure give \(S_\psi=J_\psi A\). Uniqueness of the full polar decomposition in FS04 now proves

\[
 \Delta_\psi=\bigoplus_n\Delta_\varphi,
 \qquad \Delta_\psi^{it}=\bigoplus_n U_t.
 \tag{16}
\]

In particular the domain of \(\Delta_\psi\) is the set of \(\eta\) with every \(\eta_n\in D(\Delta_\varphi)\) and \(\sum_n\|\Delta_\varphi\eta_n\|^2<\infty\). No boundedness of either modular operator has been assumed.

Conjugating (6) by the last unitary in (16), and using commutation of all modular times, gives the complete dual-state formula

\[
 \sigma_t^\psi(\pi(x))=\pi(\sigma_t^\varphi(x)),
 \qquad \sigma_t^\psi(V)=V.
 \tag{17}
\]

Both sides are normal maps and the two families generate \(N\), so this determines the action everywhere.

## 4. A unitary shear gives the entire core

Form the regular core of \(N\) in the faithful representation just constructed. Its Hilbert space is \(L^2(\mathbb R_t,\ell^2(\mathbb Z,H))\). Write \(L_s\) for the real core translations and still write \(V\) for the constant discrete unitary. Formula (17) gives

\[
 \begin{aligned}
 [x\zeta](t,n)&=\sigma_{-(t+nT)}^\varphi(x)\zeta(t,n),\\
 [V\zeta](t,n)&=\zeta(t,n-1),\\
 [L_s\zeta](t,n)&=\zeta(t-s,n).
 \end{aligned}
 \tag{18}
\]

Fubini for a countable sum identifies this Hilbert space with \(\ell^2(\mathbb Z,L^2(\mathbb R,H))\). Define the shear and its inverse by

\[
 [Q\zeta](r,n)=\zeta(r-nT,n),
 \qquad [Q^*\eta](t,n)=\eta(t+nT,n).
 \tag{19}
\]

Translation invariance in each real coordinate shows that both maps preserve the squared norm; their displayed formulas are inverse. They are consequently onto unitaries. The construction remains valid for arbitrary \(H\): finite sums of strongly measurable simple vectors are dense, and coordinate translation preserves their completed \(L^2\) classes.

On \(L^2(\mathbb R_r,H)\), let

\[
 [\rho(x)\eta](r)=\sigma_{-r}^\varphi(x)\eta(r),
 \qquad [\ell_s\eta](r)=\eta(r-s).
\]

After the Hilbert tensor regrouping, direct substitution in (18) yields

\[
 QxQ^*=\rho(x)\otimes1,
 \qquad QL_sQ^*=\ell_s\otimes1,
 \qquad QVQ^*=\ell_T\otimes S.
 \tag{20}
\]

The first two families generate \(C_\varphi(M)\otimes1\). Multiplying the third by \(\ell_{-T}\otimes1\) gives \(1\otimes S\). Hence the whole generated image is exactly

\[
 Q C_\psi(N)Q^*=C_\varphi(M)\bar\otimes L(\mathbb Z).
 \tag{21}
\]

Every generator on either side has been accounted for. Conjugation by the actual onto unitary and its inverse proves normality, faithfulness and surjectivity. A covariant assignment on formal generators alone would not prove these properties.

The dual flow of the real crossing before the shear is conjugation by multiplication by \(e^{-ist}\). In the new coordinates this multiplier is

\[
 e^{-is(r-nT)}=e^{-isr}e^{isnT}.
 \tag{22}
\]

Thus (21) intertwines that flow with

\[
 \theta_s\bar\otimes\rho_s^{\mathbb T},
 \qquad \rho_s^{\mathbb T}(S)=e^{isT}S.
 \tag{23}
\]

This checks both the negative real-core character and the positive circle rotation.

## 5. The centre, factoriality and the exact subtype

First suppose that \(M\) is type III₁. By definition \(S(M)=[0,\infty)\), so (5) and the dual-centre kernel theorem give

\[
 \Gamma(\sigma^\varphi)=\mathbb R,
 \qquad \theta_s|_{Z(C_\varphi(M))}=\mathrm{id}
 \quad(s\in\mathbb R).
 \tag{24}
\]

The exponential is injective on the real line, so no spectral information is lost in the first implication. By CORE8,

\[
 Z(C_\varphi(M))
 =Z(C_\varphi(M))^\theta
 =\pi(Z(M))=\mathbb C1.
 \tag{25}
\]

In particular the original core is a factor.

The tensor centre formula TF7 and (21) give

\[
 Z(C_\psi(N))\cong1\otimes L(\mathbb Z).
 \tag{26}
\]

This is precisely the full circle algebra with Haar measure. Explicitly the Fourier unitary

\[
 \mathcal F:\ell^2(\mathbb Z)\longrightarrow L^2(\mathbb T,h),
 \qquad \mathcal F\delta_n(z)=z^n
 \tag{27}
\]

is onto by CC0. It sends \(S\) to multiplication by \(z\). Borel functional calculus gives all multiplication operators by bounded Borel functions on the circle, and completed Haar classes have Borel representatives. Conversely these multiplication operators form a von Neumann algebra, so the algebra generated by multiplication by \(z\) is exactly \(L^\infty(\mathbb T,h)\). The onto unitary also rules out a singular spectral summand.

Under this identification, (23) acts by

\[
 (\rho_s^{\mathbb T}f)(z)=f(e^{isT}z).
 \tag{28}
\]

If \(f\in L^\infty(\mathbb T,h)\) is fixed for every \(s\), its \(n\)-th Fourier coefficient satisfies
\(\widehat f(n)=e^{insT}\widehat f(n)\) for every \(s\). For \(n\ne0\), choose \(s\) with \(e^{insT}\ne1\); hence that coefficient vanishes. Completeness in \(L^2\), which contains \(L^\infty\) here because \(h\) is finite, makes \(f\) constant. The centre flow is therefore ergodic. Applying CORE8 now to \(N\) proves

\[
 Z(N)=\mathbb C1.
 \tag{29}
\]

Factoriality is established before any factor-only spectral theorem is applied to \(N\).

An automorphism in (28) is the identity precisely when it fixes the generating function \(z\), namely when \(e^{isT}=1\). Its complete kernel is

\[
 K_N=(2\pi/T)\mathbb Z.
 \tag{30}
\]

Equations (5) and K43, now valid for the factor \(N\), give

\[
 S_+(N)=\exp K_N
       =\{e^{2\pi n/T}:n\in\mathbb Z\}
       =\lambda^{\mathbb Z}.
 \tag{31}
\]

Each full modular spectrum is closed and contains \(\lambda^n\) for all positive integers \(n\). These numbers tend to zero, so zero belongs to every spectrum. Positivity of the modular operators excludes negative numbers. Thus

\[
 S(N)=\{0\}\cup\lambda^{\mathbb Z}.
 \tag{32}
\]


It remains to justify that \(N\) has no nonzero finite projection. If it had one, the finite-corner trace theorem L18 Section 6 would produce a faithful normal semifinite trace \(\tau\) on this factor. For a trace, the GNS involution is isometric on its dense finite-star domain; its closure has modular operator \(1\). Thus \(\operatorname{Sp}\Delta_\tau=\{1\}\), contradicting (31), since \(0<\lambda<1\). Consequently \(N\) is type III, and (32) is exactly its subtype \(\mathrm{III}_\lambda\). This proves Theorem 1.1.

## 6. Changing weight and the visible inner time

The particular faithful state does not affect the isomorphism type of the discrete crossing. More generally let \(\chi\) be any faithful normal semifinite weight on the same \(M\). The normalized cocycle theorem SI14 gives

\[
 u_t=[D\chi:D\varphi]_t,
 \qquad \sigma_t^\chi=\operatorname{Ad}(u_t)\sigma_t^\varphi,
 \qquad u_{t+r}=u_t\sigma_t^\varphi(u_r).
 \tag{33}
\]

Restricting to \(t=nT\) is a \(\mathbb Z\)-cocycle, including negative integers. NR5's explicit unitary on the regular Hilbert space proves a normal isomorphism

\[
 M\rtimes_{\sigma_T^\chi}\mathbb Z
   \longrightarrow M\rtimes_{\sigma_T^\varphi}\mathbb Z,
 \qquad x\longmapsto x,
 \qquad V_\chi\longmapsto u_TV_\varphi.
 \tag{34}
\]

The inverse fixes \(M\) and sends \(V_\varphi\) to \(u_T^*V_\chi\). Multiplication by the coordinate cocycle is an onto unitary in NR5, so these are maps of the full von Neumann algebras. Theorem 1.1 therefore also determines the type of the crossing made with \(\chi\). This conclusion still assumes that the original type III₁ factor has the faithful normal state used above.

There is a useful direct check on the two time scales. Formula (17) shows that

\[
 \sigma_T^\psi=\operatorname{Ad}V
 \quad\text{on }N.
 \tag{35}
\]

They agree on \(M\), and both fix \(V\). This is an inner modular time of \(N\), not the period \(2\pi/T\) of its core centre flow. The dual flow fixes \(V\), while it multiplies the compensating real unitary \(\ell_{-T}\) by \(e^{isT}\). That distinction explains (4) without changing either convention.

## 7. Three exact checks

**The parameter \(1/4\).** Taking \(T=2\pi/\log4\) gives \(\lambda=1/4\). At the flow time \(s=\log4\), equation (4) multiplies \(W\) by \(e^{2\pi i}=1\). At time \(s=\log4/2\), it multiplies \(W\) by \(-1\). The least positive period is therefore \(\log4\), as also proved by (30). Replacing the sampling time by \(T/2\) gives parameter \(1/16\).

**Why the initial III₁ assumption matters.** Let \(M=M_d(\mathbb C)\) and let \(\varphi\) be its normalized trace. The modular action is trivial, so (6) is simply \(\pi(x)=1\otimes x\), and

\[
 N=M_d(\mathbb C)\bar\otimes L(\mathbb Z).
 \tag{36}
\]

Its centre is the full circle algebra. It is not a factor. The general core isomorphism (3) still holds, but (25) does not. Thus factoriality of an arbitrary \(M\) alone is insufficient.

**Why the shear contains \(nT\).** Replacing \(r=t+nT\) by \(r=t-nT\) in (19) would turn the first line of (18) into a coefficient depending on \(r+2nT\), rather than on \(r\) alone. The correct shear removes the discrete coordinate from every coefficient, sends \(V\) to \(\ell_T\otimes S\), and leaves the centre coordinate \(\ell_{-T}V\). These three simultaneous checks determine its sign.

The result supplies the discrete modular-crossing step in the classification of approximately finite-dimensional type III₁ factors. The tensor-product circle crossing in Lemma 4.17(ii), classification of its actions, and the final uniqueness argument require their own proofs.
