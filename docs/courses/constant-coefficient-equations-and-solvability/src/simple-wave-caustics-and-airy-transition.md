# Simple wave caustics and the Airy transition

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A regular ray amplitude contains the inverse square root of a projection Jacobian. When that Jacobian vanishes, the regular formula loses its validity. At a simple fold, two critical points merge. Keeping the cubic direction intact while integrating the remaining directions gives an Airy function and a uniform transition between two-ray oscillation and shadow.

We use the phase, ray maps and complementary Hessian calculation in [Wave rays, caustics, and stationary amplitudes](wave-rays-caustics-and-stationary-amplitudes.md). Three precise analytic prerequisites suffice: compact stationary phase from [Stationary phase and critical manifolds][stationary]; the controlled even/odd square decomposition from [Folds, reflections and uniform smooth descent][descent]; and the cutoff Airy definition and real derivative bounds from [Airy functions and fold model operators][airy]. We prove the full local cubic normal form and the amplitude reduction needed for this wave problem.

All expansions below hold locally with every prescribed observation derivative, up to a remainder \(O(\omega^{-\infty})\). The explicit Airy terms decay exponentially in a fixed shadow region. A general smooth localized contribution has the retained rapid remainder, so an exponential bound for that entire contribution requires an additional argument.

Take \(n\geq2\), real smooth \(\phi\) with nonzero gradient, and compact smooth \(a\). The wave equation has zero initial displacement and initial velocity \(a e^{i\omega\phi}\). Fix one branch \(\sigma=\pm1\) of the Fourier sine split. At its critical point write \(k=\nabla\phi=\kappa e_1\), and diagonalize the restriction of \(B=\phi''\) to \(e_1^\perp\), with eigenvalues \(b_2,\ldots,b_n\). Its ray is \(x=y-\sigma t k/|k|\). These are the conventions from the preceding lesson.

## A simple center and its cubic contact

Keep the coordinates of the Hessian calculation and suppose exactly one tangential index \(j\) satisfies \(\sigma t b_j/\kappa=1\). Then \(b_j\ne0\), and the Hessian has a one-dimensional kernel. A vector in it, normalized by \(\delta y_j=1\), is
\[
\begin{gathered}
\delta y=e_j,\qquad \delta\eta_j=b_j,\quad\delta\eta_1=B_{1j},\\
\delta\eta_\ell=0\quad(\ell\ne1,j).
\end{gathered}
\]
This follows directly from \(H_\sigma(\delta\eta,\delta y)=0\); in particular the normal component \(B_{1j}\) must not be discarded.

Expand \(|\kappa e_1+\delta\eta|\). Its cubic term is
\(-\delta\eta_1|\delta\eta'|^2/(2\kappa^2)\). Restricting the third-order part of \(\Psi_\sigma\) to the kernel line therefore gives
\[
\left(\frac{\phi_{jjj}}6-\frac{b_jB_{1j}}{2\kappa}\right)s^3 .
\]
The actual third derivative on the normalized kernel vector is
\(\phi_{jjj}-3b_jB_{1j}/\kappa\). This is the nonzero-cubic hypothesis.

The normal plane section of the level surface in direction \(e_j\) has expansion
\[
y_1=-\frac{b_j}{2\kappa}s^2
-\left(\frac{\phi_{jjj}}{6\kappa}
-\frac{b_jB_{1j}}{2\kappa^2}\right)s^3+O(s^4).
\]
To verify it, substitute \(y_1=c_2s^2+c_3s^3+O(s^4)\) into the Taylor series of \(\phi\): the terms through cubic order are \(\kappa y_1+b_js^2/2+B_{1j}y_1s+\phi_{jjj}s^3/6\). The successive coefficients give precisely the formula above. The osculating circle with signed radius \(-\kappa/b_j\) has that same quadratic coefficient and no cubic term. Consequently the nonzero-cubic hypothesis is exactly the absence of third-order contact with that circle in this normal section.

The parameter family has an actual transverse unfolding direction. At a full critical point the derivative, with respect to \(x\), of the first phase derivative along the kernel vector is \(\delta\eta\); this vector is nonzero because \(b_j\ne0\). Thus a parameter variation in \(x\) makes that first derivative nonzero. The following arguments prove the needed general local reduction; the fixed Airy model alone is not used as a theorem for arbitrary wave phases.

## Divide the amplitude on both sides of the fold

Corollary 5.2 of [Folds, reflections and uniform smooth descent][descent] gives the following controlled square decomposition. For a smooth \(b(z,p)\), that corollary supplies smooth \(E(r,p),O(r,p)\), on a full neighborhood of \(r=0\), satisfying
\[
b(z,p)=E(z^2,p)+zO(z^2,p).
\]
The choice is linear in \(b\), each prescribed mixed derivative is bounded by finitely many mixed derivatives of \(b\), and external parameter derivatives commute with the construction. This full negative-\(r\) extension is necessary below; a formula merely on the attained side would not suffice.

Allow one parameter to be \(h\), and set
\[
\begin{gathered}
A(h,p)=E(-h,h,p),\\
B(h,p)=O(-h,h,p).
\end{gathered}
\]
The fundamental theorem of calculus gives the exact division
\[
\begin{aligned}
b(z,h,p)&=A(h,p)+zB(h,p)\\
&\quad+(z^2+h)C(z,h,p).
\end{aligned}
\]
where \(r_s=-h+s(z^2+h)\), and
\[
\begin{aligned}
C(z,h,p)&=\int_0^1E_r(r_s,h,p)\,ds\\
&\quad+z\int_0^1O_r(r_s,h,p)\,ds .
\end{aligned}
\]
Shrink the fixed neighborhoods so the line segment lies in the extension domain. This proves joint smoothness across \(h=0\), including the shadow side \(h>0\). All maps are linear in \(b\), and their estimates follow by the chain rule on compact neighborhoods and the prerequisite's finite-seminorm bounds. If \(b(z,h,p,\omega)\) is a symbol of order \(\mu\), uniformly with all \(z,h,p\) derivatives, the same construction preserves that symbol order with every \(\omega\) derivative: all kernels and coordinate operations are fixed independently of \(\omega\).

At \(h=0\), \(A=b(0,0,p)\), \(B=b_z(0,0,p)\). These values follow either from the identity or from the attained-side parity decomposition. The division is not claimed unique in the shadow; the fixed extension gives one controlled choice.

## A cubic normal form with transverse unfolding

**Theorem 1 (a transverse cubic normal form).** Let \(f(p,z)\) be real and smooth, with, at the marked point,
\[
f_z=f_{zz}=0,\qquad f_{zzz}\ne0,\qquad d_p f_z\ne0 .
\]
There are smooth real \(\rho(p),\psi(p)\) and a smooth fiber coordinate \(Z(p,w)\), a local diffeomorphism in \(w\), such that
\[
\begin{gathered}
f(p,Z(p,w))=\rho(p)+\frac{w^3}{3}+\psi(p)w,\\
\psi(p_0)=0,\qquad d\psi(p_0)\ne0 .
\end{gathered}
\]
The final formula uses the original parameter \(p\), without changing which wave observation it denotes.

To prove it, reverse the fiber coordinate if necessary so \(f_{zzz}>0\) at the marked point. The implicit function theorem solves \(f_{zz}(p,r(p))=0\). Translate by \(r(p)\), then rescale the fiber by the positive smooth factor \((2/f_{zzz}(p,r(p)))^{1/3}\). Subtract the new value \(\rho_0(p)\) at zero. The resulting phase is exactly
\[
\begin{gathered}
g(p,z)=h(p)z+z^3/3+r(p,z),\\
r(p,z)=z^4a(p,z).
\end{gathered}
\]
Taylor's integral remainder proves the smooth factorization. The parameter differential of the new \(h=g_z(p,0)\) is nonzero at the marked point: translating the inflection point adds \(f_{zz}\,dr=0\) there, and the rescaling is nonzero. Use \((h,q)\) as parameter coordinates, where \(q\) are the remaining parameters.

Set
\[
\begin{gathered}
g_\tau(h,q,z)=hz+z^3/3+\tau r(h,q,z),\\
0\leq\tau\leq1 .
\end{gathered}
\]
Since \(r_z=z^3d\) for a smooth \(d\),
\[
\begin{gathered}
(g_\tau)_z=h+z^2(1+\tau z d)=h+w_\tau^2,\\
w_\tau=z\sqrt{1+\tau z d}.
\end{gathered}
\]
This is a smooth fiber diffeomorphism on one common sufficiently small neighborhood, for every \(\tau\). Divide both \(r\) and \((g_\tau)_h\), using the quadratic-division lemma in the \(w_\tau\) coordinate:
\[
\begin{gathered}
r=A+B w_\tau+(g_\tau)_z C,\\
(g_\tau)_h=D+E w_\tau+(g_\tau)_z G .
\end{gathered}
\]
All coefficients are smooth in \(h,q,\tau\). At \(h=0,w_\tau=0\), \(r\) vanishes to order four in \(w_\tau\), so \(A=B=0\) and \(C=O(w_\tau^2)\). At that point \((g_\tau)_h=z+\tau r_h\) has value zero and first \(w_\tau\) derivative one, so \(D=0,E=1\). Shrink uniformly in \(\tau\) so \(E\) never vanishes.
In fact \(A,B=O(h^2)\), uniformly in the other parameters: the attained-side even and divided-odd square coefficients of \(r\) have both their value and first square derivative zero at zero, for every \(h,q,\tau\). Their full smooth extensions retain these two jets. Taylor's formula then gives that order on evaluating the square variable at \(-h\). Consequently the parameter flow below has identity first differential in \(h\) at \(h=0\).

Define a vector field, with zero \(q\) component, by
\[
\begin{gathered}
V_h=-B/E,\qquad V_z=-C+(B/E)G,\\
K=A-(B/E)D .
\end{gathered}
\]
Direct substitution proves
\[
\partial_\tau g_\tau+V_h(g_\tau)_h+V_z(g_\tau)_z=K(h,q,\tau).
\]
Crucially \(V_h\) and \(K\) depend only on the parameters. The field vanishes at \(h=z=0\); standard local smooth ODE existence, after shrinking, gives its flow for all \(0\leq\tau\leq1\). To justify the common time interval, take a compact neighborhood on which the field and its derivative are uniformly bounded in \(\tau\); it is uniformly Lipschitz and zero at the marked point, so Grönwall bounds displacement by a fixed multiple of the initial distance. A smaller initial neighborhood then stays inside that compact neighborhood for the entire unit interval.

Write the flow as
\((h,q,z)\mapsto(H_\tau(h,q),q,Z_\tau(h,q,z))\).
The parameter flow is independent of \(z\), and each \(H_\tau\) is a local diffeomorphism in \(h\). The fiber map is a diffeomorphism as well: its derivative in the initial \(z\) satisfies a scalar linear ODE, initially one, and is a positive exponential. Along the flow,
\[
\begin{gathered}
g_1(H_1(h,q),q,Z_1(h,q,z))\\
=hz+z^3/3+\int_0^1K(H_\tau(h,q),q,\tau)\,d\tau .
\end{gathered}
\]
The last term is independent of \(z\). Invert the parameter map \(h\mapsto H_1(h,q)\). Set \(\psi\) equal to its inverse first coordinate, add the displayed parameter integral to the original \(\rho_0\), and compose the fiber flow with the preliminary translation and scaling. This gives the claimed formula in the original parameter.

Since \(B=0\) at \(h=0\), the parameter flow preserves \(h=0\); thus \(\psi(p_0)=0\). The inverse flow has nonzero \(h\) derivative and the preliminary \(h\) had nonzero parameter differential, proving \(d\psi(p_0)\ne0\). This is a proof for the transverse unfolding required here. No general preparation theorem for arbitrary singularities has been inferred from it.

## Integrate the nondegenerate directions

Consider one simple wave caustic as in the cubic-contact calculation, with nonzero cubic coefficient. Use a linear basis in the \(2n\) integration variables whose first vector is the Hessian kernel and whose other \(2n-1\) vectors span a complementary subspace on which the Hessian is nondegenerate. Denote the resulting variables by \((z,q)\) and the observation parameter by \(p=(t,x)\).

The equations \(\partial_q\Psi_\sigma=0\) have a unique smooth solution \(q=Q(p,z)\) near the marked point. Put
\[
f(p,z)=\Psi_\sigma(p,z,Q(p,z)).
\]
The first two \(z\) derivatives vanish at the marked point. The third is the cubic derivative on the original kernel. Indeed, differentiate along the curve \((z,Q(p_0,z))\): its initial tangent is the kernel vector, because the mixed Hessian with that vector is zero and the complementary Hessian is invertible. In the third derivative, the term involving the Hessian paired with that tangent is zero, and the term involving the phase gradient is zero. Thus only \(D^3\Psi_\sigma\) on the kernel remains. This also proves that the nonzero kernel cubic is invariant under smooth changes of integration coordinates.

Furthermore \(d_p f_z\ne0\). In these kernel coordinates the mixed Hessian \(H_{zq}\) is zero at the marked point, so differentiating \(Q\) contributes nothing to \(d_p f_z\) there. Its \(x\) differential is the nonzero \(\delta\eta\) calculated in the cubic-contact calculation. Hence the cubic-normal-form theorem applies with a genuine transverse \(\psi\).

Localize the branch integral with a smooth cutoff supported in this critical neighborhood and equal to one near the marked critical point. Apply the compact stationary-phase theorem in [Stationary phase and critical manifolds][stationary] in the \(q\) variables, treating \((p,z)\) as finite parameters. On a smaller common compact neighborhood, the complementary Hessian has bounded inverse, and the compact portion away from \(Q(p,z)\) has a uniformly nonzero \(q\) gradient. The theorem and its symbol corollary, followed by the classical realization in the preceding lesson with a fixed compact \(z\) cutoff, give
\[
\begin{gathered}
I_\omega(p)=\int e^{i\omega f(p,z)}b(p,z,\omega)\,dz,\\
\begin{aligned}
u_{\omega,\mathrm{loc}}^\sigma(p)
&=(2\pi)^{-1/2}\omega^{-1/2}I_\omega(p)\\
&\quad+O(\omega^{-\infty}).
\end{aligned}
\end{gathered}
\]
Here \(b\) is a classical order-zero symbol with compact fixed fiber support, uniformly with all local parameter derivatives. The constant follows from
\((2\pi)^{-n}(2\pi)^{(2n-1)/2}=(2\pi)^{-1/2}\)
and
\(\omega^{n-1-(2n-1)/2}=\omega^{-1/2}\).
The complementary signature, Hessian determinant, original amplitude and coordinate Jacobians are included in \(b\); none is discarded. The normalized stationary remainder gives a rapid full remainder after integrating the compact \(z\) variable, because any fixed number of derivatives costs only a fixed polynomial in \(\omega\).

Make the cubic-normal-form theorem fiber change and absorb its absolute Jacobian into \(b\). The local contribution becomes
\[
\begin{gathered}
(2\pi)^{-1/2}\omega^{-1/2}e^{i\omega\rho(p)}
J_\omega(p)+O(\omega^{-\infty}),\\
J_\omega(p)=\int
e^{i\omega(z^3/3+\psi(p)z)}b(p,z,\omega)\,dz .
\end{gathered}
\]
All coordinate changes are smooth and independent of \(\omega\); therefore the complete order-zero symbol estimates survive. The change may reverse orientation in the preliminary step, and the integration Jacobian uses its absolute value.

## Obtain both Airy coefficients to every order

The cutoff definition, all real derivatives and the bounds we use are proved in Section 1 of [Airy functions and fold model operators][airy].

In this convention the exact canonical identities are
\[
\begin{split}
\operatorname{Os}\int_{\mathbb R}e^{i\omega(z^3/3+\psi z)}\,dz
&=2\pi\omega^{-1/3}\operatorname{Ai}(\omega^{2/3}\psi),\\
\operatorname{Os}\int_{\mathbb R}z e^{i\omega(z^3/3+\psi z)}\,dz
&=-2\pi i\,\omega^{-2/3}\operatorname{Ai}'(\omega^{2/3}\psi).
\end{split}
\]
The first follows by \(s=\omega^{1/3}z\) in the exact Fourier definition. The second follows by differentiating that definition in its real argument, whose legitimacy is part of the exact cutoff lemma. The sign is \(1/i=-i\).

In the remaining displays write \(\zeta=\omega^{2/3}\psi(p)\).

Choose a fixed cutoff \(\theta(z)\), equal to one near zero, and shrink \(|\psi|\) so all possible local critical points \(z=\pm\sqrt{-\psi}\) are in its one region. It is supported in a slightly larger coordinate neighborhood. The two integrals with \(\theta\) differ from the canonical identities by \(O(\omega^{-\infty})\), uniformly with every fixed parameter derivative. Here is the needed tail justification. On the support of \(1-\theta\),
\(|z^2+\psi|\geq c(1+z^2)\) outside a fixed central interval. Use transposed integration by parts
\[
T_\psi c=-\partial_z\!\left(\frac{c}{i(z^2+\psi)}\right).
\]
For a polynomial amplitude of degree \(m\), each application lowers its order at infinity by three, with uniform bounds in small \(\psi\). After any fixed parameter or frequency derivatives the initial amplitude still has a finite polynomial order (parameter differentiation inserts \(\omega z\), frequency differentiation inserts the cubic phase). Take enough applications that the resulting order is integrable; each integration supplies \(\omega^{-1}\). To justify removal of the remote cutoff, put in \(\chi(z/R)\) first. On its derivative support the quotient denominator has size \(R^2\), the cutoff derivatives supply the usual \(R^{-1}\) factors, and after sufficiently many applications the integrated terms there are \(O(R^{m-3N+1})\to0\). Dominated convergence then leaves the integrable tail. Increasing \(N\) proves the asserted rapid estimates, without analytically continuing a smooth cutoff.

Apply the quadratic-division lemma to \(b\), with \(h=\psi\) and all remaining variables as parameters:
\[
b=A_0+zB_0+(z^2+\psi)C_0 .
\]
For iteration we need compact quotients. Define
\[
\widetilde C_0=\frac{b-\theta(A_0+zB_0)}{z^2+\psi}.
\]
Where \(\theta=1\), this is the smooth \(C_0\) just constructed. On the rest of the common support neighborhood the denominator is uniformly nonzero. Extend by zero outside the compact supports. Thus \(\widetilde C_0\) is smooth, compactly supported and an order-zero symbol with all finite-seminorm estimates. The supports can be put inside a fixed interval on which the parity extension is defined; choose nested central and support intervals at the start.

Integration by parts, with no boundary term, gives the exact recurrence modulo the rapid canonical-cutoff tails:
\[
\begin{aligned}
J_\omega[b]&=2\pi\omega^{-1/3}A_0\operatorname{Ai}(\zeta)\\
&\quad-2\pi i\,\omega^{-2/3}B_0\operatorname{Ai}'(\zeta)\\
&\quad+\omega^{-1}J_\omega[b_1]+O(\omega^{-\infty}),\\
b_1&=i\,\partial_z\widetilde C_0 .
\end{aligned}
\]
In particular the quotient step has sign \(+i/\omega\). Repeat with \(b_1,b_2,\ldots\), using the same fixed intervals and cutoff. The controlled linear operations preserve order zero and the classical expansions in \(\omega^{-1}\). For every \(N\),
\[
\begin{gathered}
\begin{aligned}
T_j&=A_j(p,\omega)\operatorname{Ai}(\zeta)\\
&\quad-i\omega^{-1/3}B_j(p,\omega)\operatorname{Ai}'(\zeta),\\
J_\omega&=2\pi\omega^{-1/3}\sum_{j<N}\omega^{-j}T_j\\
&\quad+\omega^{-N}J_\omega[b_N]+O(\omega^{-\infty}).
\end{aligned}
\end{gathered}
\]
The remainder integral is \(O(1)\) before differentiation, simply by compact support and bounded amplitude. Any prescribed derivatives cost a fixed polynomial in \(\omega\), so choosing \(N\) sufficiently large gives any required negative order. This elementary bound suffices; a uniform cubic decay theorem is not assumed in this step.

Collect the classical coefficients from both \(j\) and each \(A_j,B_j\) expansion. Use the classical realization in the preceding lesson to obtain classical order-zero symbols \(\mathcal A,\mathcal B\) for these two collected series. The exact Airy derivative bounds imply at most polynomial \(\omega\) growth for every fixed parameter or frequency derivative of the Airy factors on a fixed compact parameter set. Hence the replacement of a sufficiently long finite expansion by the two realizations leaves a rapid remainder, after choosing the truncation order to absorb those polynomial factors. We obtain
\[
\begin{aligned}
J_\omega&=2\pi\omega^{-1/3}\mathcal A(p,\omega)\operatorname{Ai}(\zeta)\\
&\quad-2\pi i\,\omega^{-2/3}\mathcal B(p,\omega)\operatorname{Ai}'(\zeta)\\
&\quad+O(\omega^{-\infty}).
\end{aligned}
\]
All remainders here are local \(C^\infty\) rapid remainders, including any fixed frequency derivatives. The leading coefficients satisfy
\[
\begin{gathered}
\mathcal A_0(p)=E_0(-\psi(p),p),\\
\mathcal B_0(p)=O_0(-\psi(p),p).
\end{gathered}
\]
for the chosen parity extensions of \(b_0\). On \(\psi<0\), with \(r=\sqrt{-\psi}\),
\(b_0(p,\pm r)=\mathcal A_0\pm r\mathcal B_0\).
At \(\psi=0\), \(\mathcal A_0=b_0(p,0)\).

## The local wave formula and its three regimes

**Theorem 2 (the uniform local wave fold).** Under the simple-center and nonzero-cubic hypotheses above, the localized branch has the expansion
\[
\begin{gathered}
\begin{aligned}
W_\omega(p)&=A(p,\omega)\operatorname{Ai}(\zeta)\\
&\quad+\omega^{-1/3}B(p,\omega)\operatorname{Ai}'(\zeta),\\
u_{\omega,\mathrm{loc}}^\sigma(p)
&=\omega^{-5/6}e^{i\omega\rho(p)}W_\omega(p)\\
&\quad+O(\omega^{-\infty}).
\end{aligned}
\end{gathered}
\]
where \(\zeta=\omega^{2/3}\psi(p)\), \(A=\sqrt{2\pi}\mathcal A\), \(B=-i\sqrt{2\pi}\mathcal B\) are classical order-zero symbols, \(\psi(p_0)=0\), and \(d\psi(p_0)\ne0\). This is the contribution of one localized branch neighborhood; other ray branches, and the outer difference \(u^+-u^-\), retain their separate contributions.

The power \(-5/6\) has a precise dimensional origin:
\[
(n-1)-\frac{2n-1}{2}-\frac13=-\frac56 .
\]
The derivative-Airy term has the additional power \(-1/3\). A phase with a more degenerate Hessian or vanishing kernel cubic is outside this theorem.

For \(\psi<0\), the cubic has two real critical points \(z=\pm r\), \(r=\sqrt{-\psi}\). Their reduced critical phases are
\(\rho-2r^3/3\) and \(\rho+2r^3/3\), respectively, and their scalar Hessians are \(2r\) and \(-2r\). The complementary Hessian remains invertible, so these are precisely two nondegenerate critical points of the original local wave phase. The leading negative-Airy formulas give
\[
\begin{split}
J_\omega\sim
\sqrt{\frac{2\pi}{\omega}}\,
\frac1{\sqrt{2r}}\big[
&b_0(p,r)e^{-2i\omega r^3/3+i\pi/4}\\
&+b_0(p,-r)e^{2i\omega r^3/3-i\pi/4}\big].
\end{split}
\]
To check both signs explicitly, put \(\Theta=2\omega r^3/3-\pi/4\). The Airy combination is proportional to

\[
\begin{gathered}
\mathcal A_0\cos\Theta-ir\mathcal B_0\sin\Theta\\
=\tfrac12(\mathcal A_0-r\mathcal B_0)e^{i\Theta}\\
+\tfrac12(\mathcal A_0+r\mathcal B_0)e^{-i\Theta}.
\end{gathered}
\]
This is exactly the two stationary contributions above. The full agreement also follows by applying the nondegenerate stationary-phase theorem directly to those two critical neighborhoods; since the Airy expansion approximates the same integral to arbitrary order, its collected expansion must match. Multiplication by the complementary stationary-phase prefactor restores the usual wave order \(\omega^{-1}\) and the signatures of the Hessian calculation.

For \(\psi>0\), there is no real critical point in this localized neighborhood. On each compact subset bounded away from \(\psi=0\), direct integration by parts gives \(O(\omega^{-\infty})\) for the actual local wave contribution, with all derivatives. The explicit Airy factors obey an exponential bound with exponent
\(-2\omega\psi^{3/2}/3\); for example
\[
\begin{gathered}
|\operatorname{Ai}(R)|\leq CR^{-1/4}e^{-2R^{3/2}/3},\\
|\operatorname{Ai}'(R)|\leq CR^{1/4}e^{-2R^{3/2}/3},\\
R\geq1 .
\end{gathered}
\]
After adding the general smooth-data rapid remainder, no exponential estimate for the entire localized contribution is asserted. The formal Airy terms exhibit exponential shadow decay; the proved actual contribution is rapidly decreasing on a fixed shadow compact. This distinction preserves the actual asymptotic contract.

In the transition region \(|\omega^{2/3}\psi|\leq C\), both Airy factors are bounded. Hence the local contribution is \(O(\omega^{-5/6})\), with the displayed additional \(\omega^{-1/3}\) correction. Since \(d\psi\ne0\), \(\psi\) is a smooth transverse defining coordinate for the local caustic; the transition has transverse width comparable to \(\omega^{-2/3}\). On the illuminated side the two-ray approximation is appropriate when \(\omega|\psi|^{3/2}\) is large. On the shadow side that same scaled quantity controls the canonical exponential.

At the marked fold the leading coefficient \(A_0\) is nonzero if \(a(y_0)\ne0\). The original amplitude is \(a(y_0)/(2i\kappa)\), and all complementary determinants and coordinate Jacobians in the complementary stationary reduction are nonzero. Moreover \(\operatorname{Ai}(0)>0\). For an explicit verification in this convention,
\[
\operatorname{Ai}(0)
=\frac{3^{-2/3}}{\pi}\Gamma(1/3)\cos(\pi/6)>0 .
\]
Substitute \(s=z^3/3\) in the cosine integral and insert \(e^{-\varepsilon s}\); the Laplace identity
\(\int_0^\infty s^{\alpha-1}e^{-ws}\,ds=\Gamma(\alpha)w^{-\alpha}\)
for \(\Re w>0\) follows from its positive-real version by holomorphic uniqueness. Let \(w=\varepsilon-i\), \(\varepsilon\downarrow0\), using Dirichlet convergence for \(\alpha=1/3\). This gives the formula. Thus generically the fold has an actual nonzero \(\omega^{-5/6}\) leading value, larger than the regular \(\omega^{-1}\) scale by \(\omega^{1/6}\), while the exact solution remains smooth for each fixed frequency.

## Exercises with complete solutions

**Exercise 1 (introductory: count the powers).** The wave integral has prefactor \(\omega^{n-1}\). A simple fold leaves one cubic direction among its \(2n\) integration variables. Compute its uniform order for \(n=2\) and for general \(n\), and the transverse transition width.

**Solution.** The \(2n-1\) nondegenerate directions contribute \(\omega^{-(2n-1)/2}\), and the cubic integral contributes \(\omega^{-1/3}\). Thus
\[
\omega^{n-1-(2n-1)/2-1/3}=\omega^{-5/6}.
\]
For \(n=2\) this is \(\omega^1\omega^{-3/2}\omega^{-1/3}\), with the same result. The Airy argument is \(\omega^{2/3}\psi\), so its bounded transition occurs on \(|\psi|=O(\omega^{-2/3})\). Since \(d\psi\ne0\), this is also the order of the width in any smooth transverse distance coordinate.

**Exercise 2 (introductory: divide a polynomial).** Divide
\[
b(z,h)=1+2z+3z^2+4z^3+5z^4
\]
by \(z^2+h\), leaving a remainder \(A(h)+zB(h)\). Find the first amplitude created by one integration by parts in the cubic integral. Interpret this calculation with a compact cutoff equal to one near both critical points.

**Solution.** Direct multiplication gives
\[
\begin{aligned}
A(h)&=1-3h+5h^2,\\
B(h)&=2-4h,\\
C(z,h)&=3-5h+4z+5z^2.
\end{aligned}
\]
The identity is \(b=A+zB+(z^2+h)C\). The next amplitude is \(iC_z=i(4+10z)\), so its two remainders are \(4i\) and \(10i\), with no further polynomial quotient. For a cutoff that is one near the critical points, its derivatives occur in a nonstationary annulus and contribute a rapid remainder. Therefore the first two formal coefficient terms are \(A+4i/\omega\) and \(B+10i/\omega\). The derivative-Airy coefficient in the integral additionally has the factor \(-i\), as the theorem specifies.

**Exercise 3 (intermediate: the mixed normal derivative is essential).** Let
\[
\phi(y_1,y_2)=e^{\varepsilon y_2}y_1
+\frac{\beta}{2}y_2^2+\frac{\gamma}{6}y_2^3,
\qquad\beta>0.
\]
At zero, compute the Hessian-kernel cubic for the \(+\) branch at \(t=1/\beta\). Compare \((\beta,\varepsilon,\gamma)=(1,1,0)\) and \((1,1,3)\). Check that the gradient is globally nonzero.

**Solution.** The first gradient component is \(e^{\varepsilon y_2}>0\), so it never vanishes. At zero, \(\kappa=1\), \(b_2=\beta\), \(B_{12}=\varepsilon\), and \(\phi_{222}=\gamma\). The normalized kernel vector has \(\delta y=(0,1)\), \(\delta\eta=(\varepsilon,\beta)\). Its third derivative is
\[
\gamma-3\beta\varepsilon,
\]
and its Taylor cubic coefficient is \(\gamma/6-\beta\varepsilon/2\). For the first triple it is \(-3\ne0\), although \(\phi_{222}=0\); this is a fold. For the second it is zero, although \(\phi_{222}=3\ne0\); the ordinary fold theorem does not apply. Indeed the level graph is
\[
\begin{aligned}
y_1&=-e^{-\varepsilon s}
\left(\frac{\beta s^2}{2}+\frac{\gamma s^3}{6}\right)\\
&=-\frac{\beta s^2}{2}
-\left(\frac{\gamma}{6}-\frac{\beta\varepsilon}{2}\right)s^3
+O(s^4).
\end{aligned}
\]
This is precisely the osculating-circle contact test. The pure tangent third derivative alone gives the wrong criterion.

**Exercise 4 (intermediate: recover the two ray amplitudes).** For \(\psi=-r^2<0\), suppose the reduced leading amplitude has remainder \(A+zB\) modulo \(z^2+\psi\). Match the Airy expression with the two nondegenerate stationary contributions, including their signs and constants.

**Solution.** The critical points \(r,-r\) have phases \(-2r^3/3,2r^3/3\) and Hessians \(2r,-2r\). Their amplitudes are \(A+rB,A-rB\). Put \(\Theta=2\omega r^3/3-\pi/4\). The leading Airy combination is
\[
2\sqrt\pi\,\omega^{-1/2}r^{-1/2}
\left(A\cos\Theta-irB\sin\Theta\right).
\]
Expand it into exponentials:
\[
\sqrt\pi\,\omega^{-1/2}r^{-1/2}
\left[(A-rB)e^{i\Theta}+(A+rB)e^{-i\Theta}\right].
\]
Since \(\sqrt\pi\,\omega^{-1/2}r^{-1/2}
=\sqrt{2\pi/\omega}/\sqrt{2r}\), the first term is the saddle at \(-r\), with phase \(+2\omega r^3/3-\pi/4\), and the second is the saddle at \(r\), with phase \(-2\omega r^3/3+\pi/4\). This checks the negative \(i\) in front of the derivative Airy function.

**Exercise 5 (advanced: determine an illuminated side).** Take
\(\phi(y)=y_1+y_2^2/2+y_2^3/6\), and consider the \(+\) branch near \(t=1,y=0,x=(-1,0)\). Expand the second ray-map component at \(t=1\). Determine the locally illuminated and shadow sides in the \(x_2\) direction, and the first differential of the canonical \(\psi\).

**Solution.** Write \(s=y_2\), \(g(s)=s+s^2/2\). Then
\[
\begin{aligned}
F^+_{1,2}(y)&=s-\frac{g(s)}{\sqrt{1+g(s)^2}}\\
&=-\frac12s^2+\frac12s^3+O(s^4).
\end{aligned}
\]
It has a strict local maximum at zero. Near the marked point, \(x_2<0\) has two local initial points and \(x_2>0\) has none; \(x_1\) can be adjusted by \(y_1\). Hence \(x_2<0\) is the local illuminated side. The normalized raw kernel direction has cubic coefficient \(1/6\) and its unfolding coefficient in \(x_2\) is one. Rescaling the old fiber \(s=2^{1/3}z\) gives \(z^3/3+2^{1/3}x_2z\) to first parameter order. The homotopy preserves that first-order unfolding, since its parameter field vanishes to at least second order in \(h\). Thus at the marked point
\[
d\psi=2^{1/3}\,dx_2.
\]
Its positive side is the same local shadow. This identifies the sign rather than inferring it from a picture of rays.

**Exercise 6 (advanced: exponential terms and a smooth shadow remainder).** Fix \(\psi>0\) and a real, nonzero \(b\in C^\infty_c(\mathbb R)\). Show that
\[
J(\omega)=\int e^{i\omega(z^3/3+\psi z)}b(z)\,dz
\]
is rapidly decreasing but cannot satisfy \(|J(\omega)|\leq Ce^{-c\omega}\) for every sufficiently large positive \(\omega\), with \(c>0\). You may use Fourier inversion and holomorphic uniqueness.

**Solution.** The phase derivative is \(z^2+\psi>0\), so repeated integration by parts on the compact support gives rapid decay. The map \(q=z^3/3+\psi z\) is a smooth increasing global diffeomorphism. Changing variables gives
\[
J(\omega)=\int e^{i\omega q}v(q)\,dq,\qquad
v(q)=\frac{b(z(q))}{z(q)^2+\psi}.
\]
Here \(v\) is real, nonzero and compactly supported. If the proposed positive-frequency exponential bound held, reality would give the same bound at negative frequencies because \(J(-\omega)=\overline{J(\omega)}\). Enlarging the constant covers bounded frequencies. The inverse Fourier integral would then define \(v\) holomorphically in the strip \(|\operatorname{Im}q|<c\): on every smaller closed strip the exponential Fourier bound supplies absolute convergence of the integral and all differentiated integrals. But \(v\) vanishes on a real interval outside its compact support. Holomorphic uniqueness forces it to vanish everywhere, a contradiction.

Thus smooth localization permits a rapid shadow remainder that is not exponentially bounded. The Airy terms' exponential shadow decay remains valid and useful; it does not impose a stronger bound on this entire smooth localized integral.

## References

[stationary]: ../prerequisites/stationary-phase-and-critical-manifolds.html
[descent]: ../prerequisites/folds-reflections-and-uniform-descent.html
[airy]: ../prerequisites/airy-functions-and-fold-model-operators.html

[stationary] *Stationary phase and critical manifolds*, Theorem 5.1 and Corollary 6.1: the compact expansion with smooth parameters and symbol amplitudes.

[descent] *Folds, reflections and uniform smooth descent*, Corollary 5.2 and its proof: controlled smooth even/odd square decomposition across the fold.

[airy] *Airy functions and fold model operators*, Section 1: cutoff Airy integrals, all real derivatives and shadow and two-saddle estimates.

NIST, *Digital Library of Mathematical Functions*, [§9.5](https://dlmf.nist.gov/9.5) and [§9.7](https://dlmf.nist.gov/9.7), for the Airy integral convention and its positive and negative real regimes.
