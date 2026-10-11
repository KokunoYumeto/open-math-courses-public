# GNS filters, modular spectra, and cocycle invariance

A faithful normal semifinite weight gives a dense GNS map that is usually unbounded for the operator norm. Fourier integration therefore needs a domain argument. We obtain that argument from bounded right multiplication: these operators both detect GNS vectors and turn their Fourier integrals into ordinary operator coefficients.

The first two sections apply to arbitrary von Neumann algebras with faithful normal semifinite weights and invariant real actions. The last section concerns real actions on factors and provides the cocycle invariance used in the continuous-core spectrum theorem. No faithful-state or separability reduction is used.

## Right multiplication detects the GNS graph

Let \(\phi\) be a faithful normal semifinite weight on a nonzero von Neumann algebra \(M\). Write \((H,\pi,\Lambda)\) for its GNS construction and \(\mathfrak n_\phi\) for its definition left ideal. The representation is faithful and normal by WG-007 and WG-010. Its full left Hilbert algebra, right algebra \(\mathcal A_r\), and bounded right multipliers \(R_\eta\), \(\eta\in\mathcal A_r\), are constructed in WH-03 and WH-11.

The two precise facts from those proofs are
\[
\begin{gathered}
\mathcal B_l
=\{\xi\in H:\exists C<\infty\
  \forall\eta\in\mathcal A_r,\
  \|R_\eta\xi\|\le C\|\eta\|\},\\
\lambda_\xi\eta=R_\eta\xi
\quad(\xi\in\mathcal B_l,\ \eta\in\mathcal A_r),
\end{gathered}
\tag{MSP.1}
\]
and
\[
\begin{gathered}
\mathcal B_l=\Lambda(\mathfrak n_\phi),\\
\lambda_{\Lambda(x)}=\pi(x)
\quad(x\in\mathfrak n_\phi).
\end{gathered}
\tag{MSP.2}
\]
The map \(\xi\mapsto\lambda_\xi\) is injective. In particular,
\[
R_\eta\Lambda(x)=\pi(x)\eta.
\tag{MSP.3}
\]

**A total set of tests.** The linear span of the vectors \(R_\eta^*\zeta\), for \(\eta\in\mathcal A_r\) and \(\zeta\in H\), is dense in \(H\). Indeed a vector perpendicular to that span satisfies \(R_\eta\xi=0\) for every \(\eta\). Formula (MSP.1), with \(C=0\), then puts it in \(\mathcal B_l\) and gives \(\lambda_\xi=0\). Injectivity gives \(\xi=0\). The Hilbert-space orthogonal-complement theorem BK-02 now gives density.

**Closed GNS graph.** Suppose a net \(x_i\in\mathfrak n_\phi\) converges ultraweakly to \(x\in M\), and \(\Lambda(x_i)\) converges weakly in \(H\) to \(\xi\). Normality of \(\pi\) and boundedness of each \(R_\eta\) give, by testing against an arbitrary vector,
\[
R_\eta\xi=\pi(x)\eta
\quad(\eta\in\mathcal A_r).
\tag{MSP.4}
\]
Thus \(\|R_\eta\xi\|\le\|x\|\|\eta\|\). Equations (MSP.1)–(MSP.2) yield \(\xi\in\mathcal B_l\), \(\lambda_\xi=\pi(x)\), and
\[
x\in\mathfrak n_\phi,\qquad \Lambda(x)=\xi.
\tag{MSP.5}
\]
This proves the precise graph closure, including the case of bounded strong-star operator convergence and Hilbert-norm convergence. The limiting vector is identified, rather than merely bounded by lower semicontinuity of the weight.

## An invariant weight realizes every Fourier filter

Let \(\alpha:\mathbb R\to\operatorname{Aut}(M)\) be point-ultraweakly continuous and suppose
\[
\phi\alpha_t=\phi\qquad(t\in\mathbb R).
\tag{MSP.6}
\]
Invariance preserves \(\mathfrak n_\phi\) and its GNS norm. It therefore defines unitaries
\[
U_t\Lambda(x)=\Lambda(\alpha_t(x)),
\qquad U_{s+t}=U_sU_t.
\tag{MSP.7}
\]
The inverse is \(U_{-t}\). We first prove strong continuity, which is needed before taking a vector integral.

For \(x\in\mathfrak n_\phi\), \(\eta\in\mathcal A_r\), and \(\zeta\in H\), (MSP.3) gives
\[
\langle U_t\Lambda(x),R_\eta^*\zeta\rangle
=\langle\pi(\alpha_t(x))\eta,\zeta\rangle.
\tag{MSP.8}
\]
The right side is continuous in \(t\), since \(\pi\) is normal. The totality statement in MSP-01 and the constant norm \(\|U_t\Lambda(x)\|=\|\Lambda(x)\|\) extend continuity to testing against every vector of \(H\). At zero,
\[
\begin{aligned}
\|U_t\Lambda(x)-\Lambda(x)\|^2
={}&2\|\Lambda(x)\|^2\\
&-2\operatorname{Re}
\langle U_t\Lambda(x),\Lambda(x)\rangle
\longrightarrow0.
\end{aligned}
\tag{MSP.9}
\]
Density of \(\Lambda(\mathfrak n_\phi)\), followed by the unitary norm bound, proves strong continuity on all of \(H\). The group law gives continuity at every time.

Use the positive Fourier convention of RSF-01:
\[
f(p)=\int_{\mathbb R}k(t)e^{itp}\,dt,
\qquad k\in L^1(\mathbb R).
\tag{MSP.10}
\]
Let \(\alpha_f\) be its normal ultraweak filter and let \(U_f\xi=\int k(t)U_t\xi\,dt\) be the Hilbert-norm integral. The vector integral exists by the bounded, strongly continuous orbit and the integration construction in BI-03. Both filter norms are at most \(\|k\|_1\).

Fix \(x\in\mathfrak n_\phi\) and put \(\xi=U_f\Lambda(x)\). Each right multiplier is bounded, so it can pass through this norm integral. Equation (MSP.8) and normality of the operator coefficient give
\[
\begin{aligned}
\langle R_\eta\xi,\zeta\rangle
&=\int k(t)
  \langle\pi(\alpha_t(x))\eta,\zeta\rangle\,dt\\
&=\langle\pi(\alpha_f(x))\eta,\zeta\rangle.
\end{aligned}
\tag{MSP.11}
\]
Consequently \(R_\eta\xi=\pi(\alpha_f(x))\eta\). Equations (MSP.1)–(MSP.2) prove
\[
\begin{gathered}
\alpha_f(x)\in\mathfrak n_\phi,\\
\Lambda(\alpha_f(x))=U_f\Lambda(x),\\
\|\Lambda(\alpha_f(x))\|
\le\|k\|_1\|\Lambda(x)\|.
\end{gathered}
\tag{MSP.12}
\]
Only bounded maps were moved through integrals. The unbounded GNS map is identified at the end by its multiplication operators.

The action and the implementing representation have the same Fourier-annihilator ideal. If \(\alpha_f=0\), (MSP.12) makes \(U_f\) zero on the dense GNS range, hence zero. If \(U_f=0\), (MSP.12) and injectivity of \(\Lambda\) make \(\alpha_f\) zero on \(\mathfrak n_\phi\). That ideal is ultraweakly dense by semifiniteness, WG-002–003, and \(\alpha_f\) is normal by RSF-01. Hence \(\alpha_f=0\) everywhere. Thus
\[
I(\alpha)=I(U),\qquad
\operatorname{Sp}(\alpha)=\operatorname{Sp}(U).
\tag{MSP.13}
\]
These are the actual annihilator ideals. No spectral-synthesis assumption identifies them with an arbitrary pointwise vanishing ideal.

**Modular specialization.** By MF-06, \(\sigma^\phi\) preserves \(\phi\), and its GNS implementation is \(U_t=\Delta_\phi^{it}\). Let \(B=\log\Delta_\phi\), with the unbounded spectral calculus of SK-05–07. The modular operator is injective; its zero spectral projection vanishes, so the logarithm is densely defined even when zero belongs to its spectrum.

Scalar spectral integration and Fubini against the finite vector measures give \(U_f=f(B)\). The support of the spectral measure of a self-adjoint operator is its spectrum: a spectral gap about \(r\) gives the bounded inverse \(\int(s-r)^{-1}\,dE_B(s)\), and a bounded inverse bounds \(\|(B-r)\xi\|\) below and excludes a sufficiently small spectral interval. Smooth compactly supported tests, which belong to the Fourier algebra by RSF-01, therefore show that the hull of \(\{f:f(B)=0\}\) is \(\operatorname{Sp}(B)\). This is the spectral-support criterion in SK-05, here applied to the actual Fourier filters.

For a finite real \(r\), a neighborhood of \(r\) has zero \(B\)-spectral projection exactly when its exponential has zero \(\Delta_\phi\)-spectral projection. It follows that
\[
\begin{aligned}
\operatorname{Sp}(\sigma^\phi)
&=\operatorname{Sp}(\log\Delta_\phi)\\
&=\log\bigl(\operatorname{Sp}(\Delta_\phi)
                  \setminus\{0\}\bigr).
\end{aligned}
\tag{MSP.14}
\]
Zero is removed before taking the logarithm. No assertion about closure at zero of the exponential of an unbounded real spectrum is needed.

For a finite matrix check, take the trace on \(M_2(\mathbb C)\) and \(\alpha_t=\operatorname{Ad}\operatorname{diag}(1,e^{it\omega})\). The diagonal matrix units have frequency zero, \(e_{12}\) has frequency \(-\omega\), and \(e_{21}\) has frequency \(\omega\). The trace GNS space is the same matrix space with its Hilbert–Schmidt norm, and (MSP.7) has those same eigenvectors. Both spectra in (MSP.13) are \(\{0,-\omega,\omega\}\).

## Cocycle invariance on factors from a matrix action

Let \(M\) be a factor, let \(\alpha\) be a point-ultraweakly continuous real action, and let \(u_t\) be a strongly continuous unitary \(\alpha\)-cocycle:
\[
u_{s+t}=u_s\alpha_s(u_t).
\tag{MSP.15}
\]
On \(Q=M\overline\otimes M_2(\mathbb C)\), put
\[
D_t=\operatorname{diag}(1,u_t),\qquad
\gamma_t=\operatorname{Ad}(D_t)
                 (\alpha_t\otimes\operatorname{id}).
\tag{MSP.16}
\]
The cocycle law gives \(D_s(\alpha_s\otimes\operatorname{id})(D_t)=D_{s+t}\), so \(\gamma\) is an action.

It is point-ultraweakly continuous. A strongly continuous unitary family is strong-star continuous, since
\[
\|(u_t^*-u_s^*)\xi\|
=\|(u_s-u_t)u_s^*\xi\|\longrightarrow0.
\tag{MSP.17}
\]
For a vector functional, conjugation by \(D_t\) therefore changes its two defining vectors continuously in norm. The estimate
\[
\|\omega_{\xi,\eta}-\omega_{\xi',\eta'}\|
\le\|\xi-\xi'\|\,\|\eta\|
  +\|\xi'\|\,\|\eta-\eta'\|
\tag{MSP.18}
\]
and the normal-functional approximation in CP-01 give norm continuity of the conjugated predual functional. Splitting a coefficient of \(\gamma_t(X)-\gamma_s(X)\) into this change and a fixed-functional coefficient of \(\alpha_t^{(2)}(X)-\alpha_s^{(2)}(X)\) proves the assertion.

The algebra \(Q\) is a factor: an element commuting with the scalar matrix units is \(\operatorname{diag}(z,z)\), and commuting also with \(\operatorname{diag}(x,x)\), \(x\in M\), forces \(z\in Z(M)=\mathbb C1\).

Both \(e_{11}\) and \(e_{22}\) are nonzero fixed projections for \(\gamma\). Their reduced actions, under the usual corner identifications, are
\[
\gamma^{e_{11}}=\alpha,\qquad
\gamma^{e_{22}}=\operatorname{Ad}(u)\alpha.
\tag{MSP.19}
\]
The fixed-corner invariance theorem CAM-02, (CAM.15) applies to the factor \(Q\). It gives
\[
\begin{aligned}
\Gamma(\alpha)
&=\Gamma(\gamma)\\
&=\Gamma(\operatorname{Ad}(u)\alpha).
\end{aligned}
\tag{MSP.20}
\]
This proof establishes the factor case needed by the continuous-core spectrum theorem directly from CAM-02. The broader equivalent-corner theorem for nonfactor actions retains its earlier programme proof in OA-FLOW lessons 111–112.

The invariant-weight spectral theorem is compared with M. Takesaki, *Theory of Operator Algebras II*, Proposition XI.1.24, printed page 329, and OA-FLOW lesson 100. The matrix construction is the one used in OA-FLOW lesson 112, (M1)–(M10). Here the GNS domain and continuity steps are supplied by the exact local Hilbert-algebra proofs, and factor cocycle invariance follows from the local fixed-corner theorem.
