# Scattering matrices at regular energies

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: Can an eigenfunction change the stationary solution without changing scattering?** Adding a bound state changes the interior solution but leaves its two radiating amplitudes unchanged. Thus the scattering matrix acts on amplitudes rather than on a chosen representative of the solution. The weighted norm comes from the free velocity on the energy surface and must be preserved even where that weight becomes small.

A stationary scattering solution has incoming and outgoing free waves. Their amplitudes determine each other even when an eigenfunction can be added to the solution. This lesson constructs that amplitude map at every regular energy, proves its compactness and weighted unitarity, and identifies it with the global scattering operator. For further reading, see Kuroda [K1], Section 6.2, Kuroda [K2], Section 3, and Yafaev [Y], Section 2.

<a id="scattering-matrix-setting"></a>

Use the real simply characteristic polynomial \(p\), the absence of invariant directions, the symmetric short-range differential perturbation \(V:X_p\to B\), and the self-adjoint closure \(H\) from [Limiting absorption and point spectrum](limiting-absorption-and-point-spectrum.md). In particular \(V\) is compact and symmetric in the extended \(B,B^*\) pairings. Let \(R_{0,\pm}(\lambda)\) be the free upper and lower boundary resolvents. For any \(\lambda\notin Z(p)\), write

\[
 M_\lambda=\{p=\lambda\},\quad g=|\nabla p|,\quad
 \mathcal H_{\lambda,\kappa}=L^2(M_\lambda,g^{-\kappa}dS),
 \qquad 0\leq\kappa\leq2.
\tag{1}
\]

The threshold estimates give \(g\geq c\widetilde p>0\) on this surface. If it is empty, all the spaces in (1) are the zero space, with their unique identity operator. The statements below include that case.

We use the homogeneous-wave, trace and flux theorems from [Global radiation and flux](global-radiation-and-flux.md#global-homogeneous-classification), the rapid-decay and domain results from [Limiting absorption and point spectrum](limiting-absorption-and-point-spectrum.md), the arbitrary-Banach-space compact alternative proved in [Self-adjoint short-range operators](self-adjoint-short-range-operators.md#short-range-compact-alternative), and Theorem 3.1 of [Compact perturbations in weighted Hilbert spaces](compact-perturbations-in-weighted-hilbert-spaces.md#weighted-compact-preserved-norm). The bounded Fredholm range solver is constructed in the proof of Theorem 3.1 below. The global comparison uses the onto distorted transforms proved in [Asymptotic completeness for short-range operators](asymptotic-completeness-for-short-range-operators.md#completeness-onto).

## 1. Energy amplitudes and stationary pairings

For \(b\in\mathcal H_{\lambda,0}\), define

\[
 \mathcal E_\lambda b=\mathcal F^{-1}\big(b\,\delta(p-\lambda)\big)
   =\mathcal F^{-1}\big((b/g)dS\big).
\tag{2}
\]

Here \(\mathcal F\) is unitary. The earlier homogeneous-wave lessons use densities \(v\,dS\); the energy amplitude in (2) is \(b=gv\).

<a id="scattering-energy-amplitudes"></a>

**Lemma 1.1.** The map \(\mathcal E_\lambda\) is a bounded bijection from \(\mathcal H_{\lambda,0}\) onto the homogeneous solutions of \((p(D)-\lambda)u=0\) in \(X_p\). Its inverse is bounded. If \(u\in X_p\) solves

\[
 (p(D)+V-\lambda)u=0,
\tag{3}
\]

there are unique \(b_+,b_-\in\mathcal H_{\lambda,0}\) with

\[
 u_\pm=\mathcal E_\lambda b_\pm
        =u+R_{0,\mp}(\lambda)Vu,
 \qquad b_+-b_-=-2\pi i\,T_\lambda Vu.
\tag{4}
\]

Their physical weighted norms agree:

\[
 \|b_+\|_{\lambda,1}=\|b_-\|_{\lambda,1}.
\tag{5}
\]

**Proof.** For \(b\in L^2(dS)\), every polynomial graph component of (2) has surface density \((\partial^\alpha p)b/g\). These densities are in \(L^2(dS)\) because \(|\partial^\alpha p|/g\) is bounded on \(M_\lambda\). The [global trace-extension theorem](global-radiation-and-flux.md#global-trace-extension) bounds their \(B^*\) norms by \(C\|b\|_2\), proving the forward graph bound.

Conversely the homogeneous classification gives \(\widehat u=v\,dS\), and bounds the \(L^2\) density of each graph component by its \(B^*\) norm. In particular the gradient components satisfy

\[
 \|gv\|_2^2=\sum_{j=1}^n\|(\partial_jp)v\|_2^2
                       \leq C\|u\|_{X_p}^2.
\tag{6}
\]

Thus \(b=gv\in L^2(dS)\), and (2) gives the inverse. Uniqueness follows from uniqueness of the surface density. This proves both graph-norm bounds without requiring \(g\) to be bounded above.

For (3), apply the [forced decomposition and flux theorem](global-radiation-and-flux.md#global-amplitude-flux) to forcing \(-Vu\in B\). Since the free resolvent terms belong to \(X_p\), both homogeneous additions do too. The first assertion makes their amplitudes lie in \(L^2(dS)\). The resolvent jump is \(R_{0,+}-R_{0,-}=2\pi i\mathcal E_\lambda T_\lambda\), giving the second identity in (4).

The forced flux identity has left side \(\int g(|v_+|^2-|v_-|^2)dS\) and right side \(4\pi\operatorname{Im}(u,-Vu)\). Symmetry makes the right side zero. Substitute \(v_\pm=b_\pm/g\) to obtain (5). Both separate integrals are finite here, because \(1/g\) is bounded and \(b_\pm\in L^2(dS)\). \(\square\)

Let \(\Sigma\) be the closed countable exceptional set from the spectral-density lesson, and \(\Omega=\mathbb R\setminus\Sigma\). At \(\lambda\in\Omega\), define for \(f\in B\)

\[
 h_\pm=(I+VR_{0,\pm}(\lambda))^{-1}f,
 \qquad (J_\pm f)_\lambda=T_\lambda h_\pm.
\tag{7}
\]

These are the canonical traces of the distorted transforms.

<a id="scattering-stationary-pairing"></a>

**Lemma 1.2.** For every solution in Lemma 1.1, every \(f\in B\), and \(\lambda\in\Omega\),

\[
 \big((J_\pm f)_\lambda,b_\pm\big)_{\lambda,1}=(f,u).
\tag{8}
\]

**Proof.** Trace-extension adjointness in (2) gives the left side as \((h_\pm,u_\pm)\). Insert (4) and use free boundary adjointness:

\[
 \begin{aligned}
 (h_\pm,u_\pm)
 &= (h_\pm,u)+(h_\pm,R_{0,\mp}Vu)\\
 &= (h_\pm,u)+(R_{0,\pm}h_\pm,Vu)\\
 &= (h_\pm+VR_{0,\pm}h_\pm,u)=(f,u).
 \end{aligned}
\tag{9}
\]

The middle equality uses [extended symmetry of \(V\)](self-adjoint-short-range-operators.md#short-range-endpoint-symmetry) on \(X_p\). All pairings are defined: \(Vu,VR_{0,\pm}h_\pm\in B\), while the other vectors are in \(B^*\). Free boundary adjointness follows from adjointness at conjugate nonreal points and their weak-star limits against fixed elements of \(B\). With the unitary Fourier convention there is no additional \((2\pi)^n\) factor in (8). \(\square\)

## 2. The exact Fredholm obstruction

Set

\[
 A_\pm=I+R_{0,\pm}(\lambda)V:X_p\longrightarrow X_p.
\tag{10}
\]

They are identity plus compact operators. Their kernels agree; call the common kernel \(N_\lambda\).

<a id="scattering-fredholm-obstruction"></a>

**Theorem 2.1.** The space \(N_\lambda\) is exactly the space of \(X_p\) solutions of (3) whose two homogeneous additions in (4) vanish. It is the entire \(L^2\) eigenspace of \(H\) at \(\lambda\), and is finite dimensional. For either sign,

\[
 \operatorname{ran}A_\pm
   =\{v\in X_p:(v,Vw)=0\ \hbox{for every }w\in N_\lambda\}.
\tag{11}
\]

**Proof.** If \(A_+u=0\), applying \(p(D)-\lambda\) gives (3), and \(u_-=0\). Equation (5) makes \(u_+=0\) as well. Thus \(A_-u=0\). Exchange the signs for the reverse inclusion. The converse characterization follows directly from (4).

The [rapid-decay theorem](limiting-absorption-and-point-spectrum.md#limiting-absorption-rapid) and its [closure-domain argument](limiting-absorption-and-point-spectrum.md#limiting-absorption-domain) put every such vector in the actual closed domain of \(H\), with \(Hu=\lambda u\). The [theorem identifying every \(L^2\) eigenfunction](limiting-absorption-and-point-spectrum.md#limiting-absorption-eigenfunctions) gives the converse, including equality with these two boundary kernels. Identity plus compact gives finite dimension and closed range of codimension \(r=\dim N_\lambda\).

The map \(V:N_\lambda\to B\) is injective: \(Vw=0\) and \(A_\pm w=0\) give \(w=0\). For arbitrary \(u\in X_p\) and \(w\in N_\lambda\), the opposite-sign kernel equation and symmetry give

\[
 \begin{aligned}
 (A_\pm u,Vw)
 &= (u,Vw)+(Vu,R_{0,\mp}Vw)\\
 &= (u,Vw)-(Vu,w)=0.
 \end{aligned}
\tag{12}
\]

Choose a basis \(w_1,\ldots,w_r\) of \(N_\lambda\). The functionals \(v\mapsto(v,Vw_j)\) are independent on \(X_p\): if a combination vanishes, testing against all compact smooth \(v\in X_p\) says that the corresponding combination of \(Vw_j\)'s is the zero distribution; injectivity of \(V\) on \(N_\lambda\) forces all coefficients to vanish. Their simultaneous kernel has codimension \(r\). By (12) it contains the closed range, which has the same codimension. Hence they are equal, proving (11). This argument identifies the annihilator without assuming that every element of the Banach dual of \(X_p\) is represented by an element of \(B\). \(\square\)

## 3. A matrix at every regular energy

<a id="scattering-regular-matrix"></a>

This is the scattering-matrix theorem of Hörmander [H2, Theorem 14.6.8].

**Theorem 3.1.** For every \(\lambda\notin Z(p)\), assigning the outgoing amplitude to an incoming amplitude by (4) defines a bounded bijection

\[
 S_\lambda:b_-\longmapsto b_+
       \quad\hbox{on }\mathcal H_{\lambda,0}.
\tag{13}
\]

It extends compatibly to a bounded bijection on every \(\mathcal H_{\lambda,\kappa}\), \(0\leq\kappa\leq2\). It is unitary for \(\kappa=1\), and \(S_\lambda-I\) is compact in all these spaces. This includes regular energies in the point spectrum.

**Proof.** Given \(b_-\in\mathcal H_{\lambda,0}\), we must solve
\(A_+u=\mathcal E_\lambda b_-\). If \(w\in N_\lambda\), its two boundary values agree, so the zero-trace criterion gives \(T_\lambda Vw=0\). Trace-extension adjointness now gives

\[
 (\mathcal E_\lambda b_-,Vw)
       =\int_{M_\lambda}(b_-/g)\overline{T_\lambda Vw}\,dS=0.
\tag{14}
\]

The range formula (11) therefore proves solvability. Applying \(p(D)-\lambda\) gives (3). Two choices of \(u\) differ by a vector of \(N_\lambda\), whose two additions vanish, so their outgoing amplitudes are equal. The map in (13) is well defined and linear.

Reverse the signs: for any prescribed \(b_+\), the same obstruction calculation solves \(A_-u=\mathcal E_\lambda b_+\). The two constructions undo each other, since one solution supplies both its amplitudes, and their uniqueness was just proved. Thus (13) is a bijection.

<a id="scattering-range-solver"></a>

Here is the required bounded range solver. Choose a basis \(w_1,\ldots,w_r\) of \(N_\lambda\). The [finite-dimensional complement proof](../providers/analysis/compact-fredholm-families.md#fredholm-finite-tools) gives continuous coordinate functionals and their bounded extensions to \(X_p\) by Hahn–Banach. They define a bounded projection \(P_N\) onto \(N_\lambda\). The closed subspace \(Y=\ker P_N\) complements the kernel, so \(A_+|_Y\) is a bijection onto the closed range in (11). Its inverse is bounded directly: otherwise there would be unit \(y_j\in Y\) with \(A_+y_j\to0\); compactness of \(R_{0,+}V\) would give a subsequence for which \(y_j=A_+y_j-R_{0,+}Vy_j\) converges to a unit vector in \(Y\cap N_\lambda=0\), a contradiction. Compose this inverse with the inclusion \(Y\hookrightarrow X_p\) to obtain a bounded linear range solver \(G_+\). The same argument applies to the opposite sign. Consequently we may take \(u=G_+\mathcal E_\lambda b_-\), and (4) gives

\[
 S_\lambda-I=-2\pi i\,T_\lambda V G_+\mathcal E_\lambda.
\tag{15}
\]

All the maps in (15) are bounded on their stated spaces, and \(V:X_p\to B\) is compact. Thus the difference is compact on unweighted \(L^2(dS)\), and \(S_\lambda\) is bounded there. The reverse-sign solver likewise bounds its inverse. In particular a bound-state ambiguity in \(u\) does not enter the operator in (15).

<a id="scattering-weighted-extension"></a>

Equation (5) says that this identity-plus-compact map preserves the norm of \(L^2(dS/g)\) on \(L^2(dS)\). Apply the weighted theorem with \(a=1/g\), \(\mu=dS\), and \(T=S_\lambda-I\). The positive bounded continuous weight meets all its hypotheses. It gives every assertion for \(0\leq\kappa\leq2\), including physical unitarity and compactness. \(\square\)

The term “matrix” permits an infinite-dimensional energy shell. The construction proves boundedness at each fixed regular energy. It does not assert operator norm continuity as the energy varies.

## 4. Identification with the global scattering operator

Let \(W_\pm\) be the complete wave operators, \(\mathscr S=W_+^*W_-\), and

\[
 Q=\mathcal F\mathscr S\mathcal F^{-1}=J_+J_-^{-1}
                 \quad\hbox{on }L^2(d\xi).
\tag{16}
\]

The inverse \(J_-^{-1}\) in (16) takes values in the absolutely continuous subspace of \(H\). Both sides of (16) were proved in the completeness lesson. Coarea writes the momentum norm as

\[
 \|h\|_{L^2(d\xi)}^2
     =\int_{\mathbb R}\|h_\lambda\|_{\lambda,1}^2\,d\lambda.
\tag{17}
\]

Fiber restrictions in (17) are understood for almost every energy.

<a id="scattering-global-identification"></a>

**Theorem 4.1.** For every \(h\in L^2(d\xi)\),

\[
 (Qh)_\lambda=S_\lambda h_\lambda
          \quad\hbox{for almost every }\lambda.
\tag{18}
\]

The right side has a measurable momentum representative, as an \(L^2\) section. The almost-everywhere meaning in (18) is independent of all choices of representatives.

**Proof.** First take \(f\in B\) and \(\lambda\in\Omega\). For arbitrary \(b\in\mathcal H_{\lambda,0}\), choose the stationary solution with incoming \(b\) and outgoing \(S_\lambda b\). The two pairings in (8) give

\[
 \big((J_+f)_\lambda,S_\lambda b\big)_{\lambda,1}
        =\big((J_-f)_\lambda,b\big)_{\lambda,1}.
\]

The unweighted space is dense in the physical space: for \(h\in\mathcal H_{\lambda,1}\), the truncations \(h_N=\mathbf1_{\{g\leq N\}}h\) satisfy \(\|h_N\|_{\lambda,0}^2\leq N\|h\|_{\lambda,1}^2\), while \(h_N\to h\) in the physical norm by dominated convergence. Since \(S_\lambda\) is unitary in that space,

\[
 (J_+f)_\lambda=S_\lambda(J_-f)_\lambda
                       \qquad(\lambda\in\Omega).
\tag{19}
\]

This is an equality of canonical \(B\)-trace amplitudes at every good energy.

<a id="scattering-summable-fibers"></a>

Surjectivity of \(J_-\) and density of \(B\) in the initial Hilbert space imply that \(J_-B\) is dense in \(L^2(d\xi)\). Given \(h\), choose \(f_j\in B\) so that \(h_j=J_-f_j\) satisfies \(\|h_j-h\|_2\leq2^{-j}\). Put \(q_j=J_+f_j=Qh_j\). Unitarity of \(Q\) gives \(\|q_j-Qh\|_2\leq2^{-j}\).

By (17) and the triangle inequality in scalar \(L^2(d\lambda)\),

\[
 \left\|\sum_j\|(h_j-h)_\lambda\|_{\lambda,1}
                                    \right\|_{L^2(d\lambda)}
       \leq\sum_j\|h_j-h\|_2<\infty.
\tag{20}
\]

Use monotone convergence on the increasing partial sums to justify the infinite sum. The same bound holds for \(q_j-Qh\). Thus outside one null set both sequences converge in the fiber Hilbert norm to the restrictions of \(h\) and \(Qh\). The canonical representatives from the distorted-transform lesson agree with these momentum restrictions almost everywhere; take a countable union of their null sets. On the remaining good energies, (19) and the fiber unitarity show that the limit of \((q_j)_\lambda\) is \(S_\lambda h_\lambda\). It is also \((Qh)_\lambda\), proving (18).

The omitted energy set \(\Sigma\) is countable and hence Lebesgue null. Its momentum preimage is null, as proved in the distorted-transform lesson. The limit just constructed supplies measurability of the fiberwise action for every input. Two ambient representatives agree on almost all fibers by (17), and a bounded \(S_\lambda\) preserves that agreement. This proves the asserted independence. \(\square\)

<a id="scattering-bound-state"></a>

**Example 4.2.** A bound state can change the stationary solution without changing its incoming or outgoing amplitudes. Indeed, add any \(w\in N_\lambda\) to \(u\). Equation (4) changes each \(u_\pm\) by \(w+R_{0,\mp}Vw=0\). For an explicit instance, the [bound-state example](limiting-absorption-and-point-spectrum.md#limiting-absorption-example) gives \(H=-\partial_x^2-2\operatorname{sech}^2x\) with eigenfunction \(\operatorname{sech}x\) at \(-1\). That energy is regular for \(p(\xi)=\xi^2\), but its free shell is empty; the amplitude spaces are zero while \(N_{-1}\) is nonzero. This is consistent with the unique identity on the zero space in Theorem 3.1.

<a id="scattering-forward-kernel"></a>

**Fast decay need not make the forward kernel vanish.** A smooth compactly supported potential satisfies bounds \(|\partial^\alpha V(x)|\leq C_\alpha\langle x\rangle^{-\rho-|\alpha|}\) for every multi-index and every fixed \(\rho>1\). Nevertheless, such a potential need not have a scattering kernel satisfying

\[
 |k(\omega,\omega')|\leq C|\omega-\omega'|^{-d+\rho}
\]

for all those exponents. When \(\rho>d\), that inequality would force the kernel to vanish as the two directions approach one another. The following example gives a positive lower bound near the diagonal for \(d=3,\rho=4\).

<a id="scattering-compact-potential"></a>

**A compact-potential counterexample.** Take \(d=3\), \(\lambda=1\), the closed unit ball \(\mathbb B=\{x\in\mathbb R^3:|x|\leq1\}\), and

\[
 \begin{gathered}
 V(x)=\kappa w(x),\qquad \kappa=\tfrac1{16},\\
 w(x)=\begin{cases}
 \exp[-1/(1-|x|^2)],&|x|<1,\\
 0,&|x|\geq1,
 \end{cases}\\
 I_w=\int_{\mathbb B}w(y)\,dy>0.
 \end{gathered}
\]

The [flat smooth cutoff](../providers/analysis/elementary-functions-and-cutoffs.md#smooth-flat-cutoffs), composed with \(1-|x|^2\), proves that \(w\) is smooth through \(|x|=1\). Each derivative is compactly supported and bounded, so every weighted derivative has finite supremum. Thus this real potential satisfies the displayed derivative bounds with \(\rho=4\). It is positive on the open ball, which proves \(I_w>0\); for example it has a positive minimum on the ball of radius \(1/2\). The bounded-potential realization of \(-\Delta+V\) has domain \(H^2(\mathbb R^3)\), as proved in [Resolvents, domains and spectral density](resolvents-domains-and-spectral-density.md#u001-specified-domains). The free upper boundary kernel at energy one is \(G(x)=e^{i|x|}/(4\pi|x|)\).

<a id="scattering-green-kernel"></a>

For a radial function \(F(r)\), differentiating \(r=|x|\) gives \(\Delta F=F''+2F'/r\) off zero; substituting \(G\) gives \((-\Delta-1)G=0\) there. Here is its distributional normalization. Choose a smooth scalar cutoff \(\eta\) equal to zero on \(( -\infty,1]\) and one on \([2,\infty)\), and set \(\chi_\delta(x)=\eta(|x|/\delta)\). For a compact smooth test \(\phi\), the function \(\chi_\delta\phi\) is supported away from zero, where ordinary compactly supported integration by parts gives \(\int G(-\Delta-1)(\chi_\delta\phi)=0\). Expanding this product gives \(\int\chi_\delta G(-\Delta-1)\phi=\int G(2\nabla\chi_\delta\cdot\nabla\phi+\phi\Delta\chi_\delta)\). The first term on the right is \(O(\delta)\): its support is \(\delta\leq|x|\leq2\delta\), and its factors have sizes \(O(\delta^{-1})\), \(O(\delta^{-1})\) and \(O(1)\), in a region of volume \(O(\delta^3)\). For the second term, the [radial measure formula](quadratic-weights-and-uniqueness-at-infinity.md#quadratic-radius), with \(G=I\), and the [sphere area \(4\pi\)](quadratic-weights-and-uniqueness-at-infinity.md#quadratic-radial-mass) give, after \(r=\delta t\), the limit \(\phi(0)\int_1^2(t\eta''(t)+2\eta'(t))dt=\phi(0)\). The last integral is one by scalar integration by parts and the endpoint values of \(\eta\). Dominated convergence on the fixed annulus justifies this limit. On the left, local integrability of \(G\) gives convergence to \(\int G(-\Delta-1)\phi\). Hence \((-\Delta-1)G=\delta_0\). The direct flux check is consistent: \(-4\pi r^2\partial_rG=e^{ir}(1-ir)\to1\), while the integral of \(G\) over the shrinking ball tends to zero.

For \(z=1+i\varepsilon\), take the explicit root \(\zeta_\varepsilon=a_\varepsilon+ib_\varepsilon\), where \(a_\varepsilon=((\sqrt{1+\varepsilon^2}+1)/2)^{1/2}\) and \(b_\varepsilon=\varepsilon/(2a_\varepsilon)>0\). Then \(\zeta_\varepsilon^2=z\), \(\zeta_\varepsilon\to1\), and \(G_\varepsilon(x)=e^{i\zeta_\varepsilon|x|}/(4\pi|x|)\) lies in \(L^1\cap L^2\). The same cutoff computation proves \((-\Delta-z)G_\varepsilon=\delta_0\). For a bounded compactly supported \(h\), [Young's inequality](../providers/analysis/euclidean-approximation-and-convolution.md#holder-and-young) gives \(v=G_\varepsilon*h\in L^2\); distributionally \(-\Delta v=zv+h\in L^2\). Plancherel gives \(|\xi|^2\widehat v\in L^2\), so \(v\in H^2\), and nonreal resolvent uniqueness identifies \(v=R_0(z)h\). On bounded sets, \(|G_\varepsilon(x)|\leq1/(4\pi|x|)\). Splitting the convolution into \(|x-y|<\eta\) and its complement bounds the first part uniformly by \(\|h\|_\infty\eta^2/2\), while on the second the kernels converge uniformly on compact sets. Thus \(G_\varepsilon*h\to G*h\) locally uniformly. The [free boundary theorem](global-polynomial-resolvent-estimates.md#uniform-local-division), applied to \(h\in B\), also gives distributional convergence to \(R_{0,+}(1)h\). Uniqueness of the limit proves \(R_{0,+}(1)h=G*h\).

<a id="scattering-directional-solution"></a>

Define on \(C(\mathbb B)\)

\[
 (Kq)(x)=\kappa\int_{\mathbb B}G(x-y)w(y)q(y)\,dy.
\]

The normed space \(C(\mathbb B)\) is complete: a uniformly Cauchy sequence converges pointwise by scalar completeness, converges uniformly to that limit, and the uniform limit is continuous. The singular part with \(|x-y|<\eta\) has norm at most \(\kappa\|q\|_\infty\eta^2/2\), by radial integration. To justify continuity, multiply the kernel by a continuous radial cutoff that is zero below \(\eta\) and one above \(2\eta\). The resulting kernel is continuous on the compact set of pairs \((x,y)\in\mathbb B^2\), so its integral is continuous in \(x\) by uniform continuity. The removed part has norm at most \(2\kappa\|q\|_\infty\eta^2\). Thus \(Kq\) is a uniform limit of continuous functions. Since \(\mathbb B-x\subset\{|z|\leq2\}\),

\[
 \|K\|\leq\kappa\int_{|z|\leq2}\frac{dz}{4\pi|z|}
       =2\kappa=\tfrac18.
\]

The Neumann series has norm tail at most \((1/8)^{N+1}/(1-1/8)\). Multiplying its finite partial sums by \(I+K\), on either side, leaves remainder \((-K)^{N+1}\); its norm tends to zero, proving both inverse identities. The bound \(\|(I+K)^{-1}-I\|\leq(1/8)/(1-1/8)=1/7\) gives, for each \(\omega'\in\mathbb S^2\),

\[
 \begin{gathered}
 \psi_{\omega'}|_{\mathbb B}=(I+K)^{-1}e^{i\omega'\cdot x}|_{\mathbb B},\\
 \|\psi_{\omega'}-e^{i\omega'\cdot x}\|_{C(\mathbb B)}\leq\tfrac17.
 \end{gathered}
\]

Extend it by \(\psi_{\omega'}=e^{i\omega'\cdot x}-R_{0,+}(1)V\psi_{\omega'}\). It restricts to the stated solution on \(\mathbb B\), solves \((-\Delta+V-1)\psi_{\omega'}=0\) distributionally, and has an outgoing correction. This dependence on the incident direction is smooth as a \(C(\mathbb B)\)-valued map. In any smooth sphere chart, each parameter derivative of \(e^{i\omega'\cdot x}\) is a finite sum of bounded polynomials in \(x\) times the exponential, with smooth parameter coefficients. Taylor remainders are uniform for \(|x|\leq1\) on a compact subchart, so these are derivatives in the supremum norm. The fixed bounded inverse commutes with those norm limits.

<a id="scattering-exact-kernel"></a>

**The exact scattering kernel.** Put

\[
 J(\omega,\omega')=\int_{\mathbb B}e^{-i\omega\cdot y}
                         w(y)\psi_{\omega'}(y)\,dy.
\]

At this energy \(M_1=\mathbb S^2\) and \(g=2\), so (2) gives the coefficient \(1/[2(2\pi)^{3/2}]\) when integrating the incident waves against an amplitude \(b\in L^2(\mathbb S^2)\). Integrate the constructed solutions against \(b(\omega')dS(\omega')\) with this same coefficient. Cauchy–Schwarz and the finite sphere measure give \(\|b\|_1\leq(4\pi)^{1/2}\|b\|_2\). The continuous, uniformly bounded \(C(\mathbb B)\)-valued family of solutions, multiplied by this measurable \(b\), is strongly measurable and has integrable norm. The [Banach-valued integral theorem](../providers/analysis/hilbert-valued-integration.md#bochner-integral) therefore constructs its integral and allows the bounded inverse and point evaluations to commute with it. For the extension off the ball, scalar Fubini applies because \(\int_{\mathbb B}|G(x-y)|dy<\infty\) for each fixed \(x\), and the incident solutions are uniformly bounded on the ball. Consequently the averaged function satisfies \(u=\mathcal E_1b-R_{0,+}(1)Vu\) everywhere. Its free term \(\mathcal E_1b\) belongs to \(X_p\), and its forcing \(Vu\) is bounded with compact support, hence belongs to the course's endpoint space \(B\). The free boundary map then puts the integrated solution in \(X_p\). This applies (15) to an actual graph-space solution without asserting that an individual plane wave is in \(X_p\).

The unitary Fourier trace of \(Vu\) has kernel \(\kappa J/[2(2\pi)^3]\); multiplying by the jump factor \(-2\pi i\) in (15) gives

\[
 k(\omega,\omega')=-\frac{i\kappa}{8\pi^2}J(\omega,\omega').
\]

The sphere normalization in Yafaev [Y], (2.7), has spectral trace \(2^{-1/2}\widehat f|_{\mathbb S^2}\) at \(d=3,\lambda=1\). The conversion from the physical shell norm \(L^2(dS/g)\) is multiplication by \(1/\sqrt2\); conjugating by that same scalar on input and output leaves this integral kernel unchanged.

The spherical outgoing amplitude can also be read directly. Uniformly for \(|y|\leq1\) and \(\omega\in\mathbb S^2\), the identity
\(|r\omega-y|-(r-\omega\cdot y)=(|y|^2-(\omega\cdot y)^2)/(|r\omega-y|+r-\omega\cdot y)\)
gives \(|r\omega-y|=r-\omega\cdot y+O(r^{-1})\). Also \(|r\omega-y|^{-1}=r^{-1}+O(r^{-2})\). The bound \(|e^{it}-e^{is}|\leq|t-s|\) therefore gives \(G(r\omega-y)=e^{ir}e^{-i\omega\cdot y}/(4\pi r)+O(r^{-2})\), uniformly. Integrating the bounded compact forcing proves the outgoing expansion with amplitude \(a=-\kappa J/(4\pi)\). Multiplication by the normalization factor \(\gamma c(1)=i/(2\pi)\) in [Y], (2.15), gives the same \(k\).

If \(\delta=|\omega-\omega'|\), then \(|e^{i(\omega'-\omega)\cdot y}-1|\leq\delta\) on \(\mathbb B\). Together with the Neumann bound this yields

\[
 \begin{gathered}
 |J(\omega,\omega')-I_w|\leq I_w(\tfrac17+\delta),\\
 |k(\omega,\omega')|\geq\frac{5\kappa I_w}{56\pi^2}>0,
 \qquad 0<\delta\leq\tfrac17.
 \end{gathered}
\]

For \(\rho=4,d=3\), the proposed estimate would instead be \(|k|\leq C\delta\), which is incompatible with this positive lower bound as \(\delta\downarrow0\). For any proposed finite \(C>0\), choose a nonempty open set of direction pairs with \(0<\delta<\min(1/7,5\kappa I_w/(56\pi^2C))\). Such a set has positive product surface measure, by the positive surface Jacobians in local sphere charts. The two bounds contradict each other there. The case \(C=0\) is immediate. Thus changing a kernel on a null set cannot repair the estimate. This example has a smooth bounded kernel, with \(|k|\leq\kappa I_w/(7\pi^2)\); fast spatial decay does not force forward vanishing. Smoothness follows by differentiating the compact integral in both direction variables, using the previously proved supremum-norm derivatives of \(\psi_{\omega'}\). Choosing a smaller decay exponent gives a different inequality and does not establish the \(\rho=4\) bound.

<a id="scattering-spectrum"></a>

**The spectral point at one.** The point \(1\) must be treated separately even when \(S_\lambda-I\) is compact. For \(V=0\), \(S_\lambda=I\); on the sphere this has an infinite-dimensional \(1\)-eigenspace. For example the bands \(2^{-j-1}<\omega_3<2^{-j}\), \(j\geq1\), have positive area \(2\pi\,2^{-j-1}\) by the sphere coordinates above. Their normalized indicators are mutually orthogonal nonzero vectors.

Here is the full compactness consequence in the physical Hilbert space. Write \(S_\lambda=I+K_\lambda\). Unitarity confines the spectrum to \(|s|=1\): if \(|s|>1\), invert \(S_\lambda-sI=-s(I-S_\lambda/s)\) by a Neumann series; if \(|s|<1\), invert \(S_\lambda-sI=S_\lambda(I-sS_\lambda^*)\) in the same way. For \(s\ne1\), the factorization \(S_\lambda-sI=(1-s)(I+K_\lambda/(1-s))\) and the [compact alternative](compact-perturbations-in-weighted-hilbert-spaces.md#weighted-compact-alternative) show that every noninvertible value is an eigenvalue. Its eigenspace is finite dimensional, since on that space \(K_\lambda=(s-1)I\), and an infinite orthonormal sequence would contradict compactness. Distinct eigenvalues have orthogonal eigenvectors: for unitary \(S_\lambda\), \((u,v)=(S_\lambda u,S_\lambda v)=s\overline t(u,v)\), and distinct unit-modulus \(s,t\) have \(s\overline t\ne1\). If infinitely many distinct eigenvalues stayed a positive distance from one, normalized eigenvectors would have pairwise separated images under \(K_\lambda\), again contradicting compactness. Hence eigenvalues different from one have finite multiplicity and can accumulate only at one, while no finite multiplicity is asserted at one itself.

### Use the conclusion

Check the exact kernel of the amplitude map and the sign in the Lippmann–Schwinger equation. Then distinguish construction at a fixed regular energy from its identification with the global scattering operator.

<a id="scattering-exercises"></a>

## 5. Exercises and checked solutions

**Exercise 5.1 (foundation).** For \(p(\xi)=\xi^2\), \(\lambda=k^2>0\), write \(\mathcal E_\lambda b\) explicitly in terms of \(b(k),b(-k)\). Determine its physical amplitude norm.

**Exercise 5.2 (intermediate).** Let \(r=\dim N_\lambda\). Explain why the \(r\) functionals in (11) determine the whole Fredholm range, even if the full Banach dual of \(X_p\) is larger than the functions in \(B\).

**Exercise 5.3 (intermediate).** Write \(K_\lambda=S_\lambda-I\). Prove the exact relation
\(2\operatorname{Re}(K_\lambda b,b)_{\lambda,1}
 +\|K_\lambda b\|_{\lambda,1}^2=0\).
If \(b\) is an eigenvector of \(S_\lambda\) with eigenvalue \(s\), show that \(|s|=1\).

**Exercise 5.4 (intermediate).** If two stationary solutions have identical incoming amplitudes, prove that their difference is a rapidly decreasing \(L^2\) eigenfunction, and that their outgoing amplitudes coincide. Does an incoming amplitude determine the solution itself?

**Exercise 5.5 (advanced).** In the proof of Theorem 4.1 replace the error bound \(2^{-j}\) by any summable positive sequence. Prove convergence on almost every fiber. Explain why arbitrary \(L^2(d\xi)\) convergence alone would not justify passing to every fixed energy surface.

<a id="scattering-solutions"></a>

**Solution 5.1.** Surface measure on the two-point shell is counting measure and \(g=2k\). Hence

\[
 \mathcal E_\lambda b(x)=
 \frac{b(k)e^{ikx}+b(-k)e^{-ikx}}{2k\sqrt{2\pi}},\qquad
 \|b\|_{\lambda,1}^2=
      \frac{|b(k)|^2+|b(-k)|^2}{2k}.
\]

The common factor \(2k\sqrt{2\pi}\) converts physical plane-wave coefficients into energy amplitudes. It therefore cancels from a matrix mapping incoming to outgoing coefficients.

**Solution 5.2.** Index zero gives a closed range of codimension \(r\). Injectivity of \(V\) on \(N_\lambda\) and compact smooth testing make the \(r\) indicated continuous functionals independent. Their joint kernel also has codimension \(r\): the map to \(\mathbb C^r\) given by their values is onto, since a proper range would have a nonzero linear annihilator, contradicting independence. Equation (12) puts the Fredholm range inside that joint kernel. Equal finite codimension forces equality, by taking the quotient of one subspace by the other. No representation theorem for the entire dual is involved.

**Solution 5.3.** Expand
\(\|b+K_\lambda b\|_{\lambda,1}^2=\|b\|_{\lambda,1}^2\) using a pairing linear in the first variable. The cross terms are twice the real part of \((K_\lambda b,b)\), giving the identity. For a nonzero eigenvector, physical unitarity gives
\(|s|^2\|b\|_{\lambda,1}^2=\|b\|_{\lambda,1}^2\), so \(|s|=1\). Equivalently the displayed relation becomes \(2\operatorname{Re}(s-1)+|s-1|^2=0\), the same condition.

**Solution 5.4.** The difference \(w\) solves (3) and has \(w_-=0\). Equation (5) makes \(w_+=0\), so \(w\in N_\lambda\). Theorem 2.1 and its rapid-decay input identify it as a rapidly decreasing \(L^2\) eigenfunction in the actual domain of \(H\). Both amplitudes of \(w\) vanish, proving equality of the outgoing amplitudes. The solution itself is unique exactly when \(N_\lambda=0\); in general its ambiguity is precisely that finite-dimensional space.

**Solution 5.5.** If \(\sum_j\varepsilon_j<\infty\) and \(\|h_j-h\|_2\leq\varepsilon_j\), coarea and the triangle inequality bound the \(L^2(d\lambda)\) norm of each partial sum of fiber errors by \(\sum_j\varepsilon_j\). Monotone convergence of their squares gives a finite-norm infinite sum. It is finite almost everywhere, so the fiber errors tend to zero there. Apply the same argument to \(Qh_j-Qh\). For arbitrary \(L^2\) convergence one may first select a subsequence with summable errors, but one cannot evaluate unrestricted ambient representatives on a fixed surface. Changing a function solely on that surface leaves its ambient \(L^2\) class unchanged. The canonical trace construction and the almost-everywhere coarea limit provide the two distinct meanings used in this proof.

## References

- [K1] Shige Toshi Kuroda, [*Scattering theory for differential operators, I, operator theory*](https://www.jstage.jst.go.jp/article/jmath1948/25/1/25_1_75/_pdf/-char/en), *Journal of the Mathematical Society of Japan* **25** (1973), 75–104. Section 6.2, Theorem 6.3, printed pages 101–103.
- [K2] Shige Toshi Kuroda, [*Scattering theory for differential operators, II, self-adjoint elliptic operators*](https://www.jstage.jst.go.jp/article/jmath1948/25/2/25_2_222/_pdf/-char/en), *Journal of the Mathematical Society of Japan* **25** (1973), 222–234. Section 3, printed page 232, with the trace estimates in Section 2.3.
- [Y] Dmitri Yafaev, [*Lectures on scattering theory*, v1](https://arxiv.org/abs/math/0403213v1), 2004. Section 2, especially the spectral normalization (2.7) and the scattering formulas (2.15)–(2.16).
- [H2] Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, reprint of the 1983 edition, Springer, 2005, Section 14.6, Lemmas 14.6.6–14.6.7, Theorem 14.6.8 and Lemma 14.6.9, pp. 259–263. ISBN 978-3-540-26964-9. [Edition information](https://doi.org/10.1007/b138375).
