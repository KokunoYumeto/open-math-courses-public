# Angular contours and polynomial continuation

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Homogeneous polynomial equations connect three kinds of geometry: tangent cones in frequency space, complex contours that avoid the characteristic divisor, and affine cycles that control polynomial values of the causal inverse. This reading supplies the full authored analytic route from the tangent model to both oriented contour formulas and the all-powers polynomial continuation argument. It also proves the global exponential bound for the lower-order series and includes all the original solved exercises.

Basic references are Atiyah, Bott and Gårding [A, B] for the hyperbolic contour and lacuna methods. The proof is supplied below at the explicit preceding inputs stated next. The complete all-integer parity-sensitive angular Fourier identity is proved in [Angular distributions and their full Fourier transforms](../../AN02-L185.html#4-the-angular-fourier-identity-on-the-whole-frequency-space), Theorem 4.1, with arbitrary angular distributions and the full frequency origin retained. The positive-polar analytic tube bound, analytic differential decrease and ordinary-wavefront inclusion are proved in Analytic directions of holomorphic boundary values. The homogeneous Euler bound and sphere-conormal exclusion are proved in Dilation equations and tangential analytic singularities, Theorem 4.1 and Corollary 4.2. General wavefront operations and homogeneous Fourier-wavefront interchange remain explicitly planned. General wavefront-operation assertions remain separate from the supplied boundary, differential and Euler results.

## Mathematical prerequisites

**Hyperbolicity and strength.** [Hyperbolicity and lower order terms](../../AN02-L038.html) gives all directions in the principal hyperbolicity cone, the full component-strength comparison and the shifted derivative estimate. [Multiple characteristics and allowed lower order terms](../../AN02-L039.html) gives multivariable derivative vanishing at each principal-line multiplicity, including the principal part itself.

**Regular-inverse wavefronts.** [Wavefronts of regular kernels](../../AN02-L019.html), Theorem 1.1, extracts a regular inverse of each normalized high-frequency localization, with its support in the corresponding ordinary wavefront fiber. The statement concerns every regular fundamental solution and does not assume global temperedness. [Symbols at infinity](../../AN02-L018.html) supplies the normalized derivative-vector compactness model.

**Causal inverses.** [Causal fundamental solutions and lower order expansions](../../AN02-L040.html) constructs the regular causal inverse, proves uniqueness in the full distributional halfspace class, and gives the causal lower-order expansion and its support cone. The scalar and Fourier conventions of that proof are retained.

**Elementary complex analysis.** [Cauchy bounds, root counts and analytic extensions](../../src/cauchy-bounds-and-root-counts.md) supplies the one-variable Cauchy, Rouché, Hurwitz and compact-contour statements. Polynomial Taylor expansion, finite root counts and compactness are used below with their exact task-specific bounds. The complete preceding [Tangent cones that permit an imaginary push](../../AN02-L118.html) gives the local cone persistence, positive-polar closed graph and uniform power denominator bound, including the full-sphere extension of an equatorial field. That polynomial input is proved; it is not a remaining general microhyperbolicity premise.

**Holomorphic boundaries and their analytic directions.** The full cone distributional limit and uniform finite-test estimate are proved in [Holomorphic boundaries in convex cones](../../prerequisites/holomorphic-boundaries-in-convex-cones.html), Theorem 2.1. Analytic directions of holomorphic boundary values proves the additional analytic statements: Theorem 4.1 gives the positive-polar analytic wavefront bound at every locally uniform polynomial growth exponent; Corollary 2.3 gives analytic-coefficient differential decrease; and Theorem 3.1 gives ordinary-wavefront inclusion. The complete controlled-sequence estimates, including common support and uniform distributional order, are supplied there.

**Angular Fourier identity and planned wavefront operations.** [Angular distributions and their full Fourier transforms](../../AN02-L185.html#4-the-angular-fourier-identity-on-the-whole-frequency-space), Theorem 4.1, proves the all-integer parity-sensitive angular Fourier identity on every Schwartz test, including its sphere-density normalization, one-dimensional finite parts, homogeneous-extension convention and frequency-origin terms. Dilation equations and tangential analytic singularities, Theorem 4.1 and Corollary 4.2, proves the homogeneous Euler wavefront bound and its sphere-conormal exclusion. Further required statements are the smooth and analytic wavefront bounds for transverse pullback, tensor products, products without opposing covectors, submanifold restriction and proper-support projection integration; continuity in distributions with a fixed closed ordinary wavefront bound; and homogeneous Fourier-wavefront interchange away from both origins. The argument below verifies all the receiving covectors, supports and signs. These general foundation statements retain an honest planned status, and do not make the entire prerequisite course or this course proof-closed.

The polynomial, contour, residue, compact-cycle and analytic-identity arguments themselves are fully written below. Rational finite-cycle comparison and the separate global component argument are supplied in the accompanying equatorial-cycle chapter. No integral torsion conclusion is inferred from a complex period.

## 1. A tangent polynomial and the full limiting operator

Fix \(\zeta\in\mathbb R^n\setminus\{0\}\). Define the multivariable vanishing order
\[
\mu=\min\{|\alpha|:\partial^\alpha F(\zeta)\ne0\},
\qquad
H_\zeta(\eta)=
\sum_{|\alpha|=\mu}
\frac{\partial^\alpha F(\zeta)}{\alpha!}\eta^\alpha.
\tag{1}
\]
Thus \(0\le\mu\le m\), and \(H_\zeta\) is a nonzero homogeneous polynomial of degree \(\mu\).

The multiplicity at zero of \(t\mapsto F(\zeta+tN)\) is exactly \(\mu\). If \(F(\zeta)\ne0\), both orders are zero. Otherwise \(\zeta\) is not proportional to \(N\), since \(F(N)\ne0\). Let the line multiplicity be \(\nu\). The multivariable Taylor order implies that all directional derivatives of orders below \(\mu\) vanish, so \(\nu\ge\mu\). the hyperbolicity and strength input's multiple-characteristic result with \(j=0\) makes every multivariable derivative of order below \(\nu\) vanish; hence \(\mu\ge\nu\). Equality follows, and
\[
H_\zeta(N)=\partial_N^\mu F(\zeta)/\mu!\ne0.
\tag{2}
\]

For real \(\eta\), the polynomials
\[
\varepsilon^{-\mu}
F\bigl(\zeta+\varepsilon(\eta+zN)\bigr)
\longrightarrow H_\zeta(\eta+zN)
\quad(\varepsilon\downarrow0)
\tag{3}
\]
converge in coefficients and locally uniformly in \(z\in\mathbb C\). Every polynomial before the limit has only real zeros in \(z\). The limit has degree \(\mu\) and nonzero leading coefficient (2). If it had a nonreal zero, a small disk around that zero disjoint from the real axis, with a zero-free boundary, would have a zero of the approximating polynomial by Rouché's theorem. This is impossible. Thus \(H_\zeta\) is homogeneous hyperbolic in \(N\).

The same argument applies to every \(\theta\in\Gamma\). the hyperbolicity and strength input first makes \(F\) hyperbolic in \(\theta\). Its line multiplicity at \(\zeta\), compared to the multivariable order exactly as above, is again \(\mu\), and \(H_\zeta(\theta)\ne0\). The connected cone \(\Gamma\) is therefore contained in the component of \(\{H_\zeta\ne0\}\) containing \(N\):
\[
\Gamma\subset\Gamma(H_\zeta,N),
\qquad
C_\zeta:=\Gamma(H_\zeta,N)^*\subset C.
\tag{4}
\]
For \(\mu=0\), use the scalar convention \(\Gamma(H_\zeta,N)=\mathbb R^n\) and \(C_\zeta=\{0\}\).

The limiting operator must retain the lower order components of \(P\). Set
\[
L_\zeta(\eta)=
\sum_{j=0}^m\
\sum_{\substack{|\alpha|=\mu+j-m\\|\alpha|\ge0}}
\frac{\partial^\alpha P_j(\zeta)}{\alpha!}\eta^\alpha.
\tag{5}
\]
An inner sum with negative requested order is empty. Its \(j=m\) term is \(H_\zeta\); every other term has degree less than \(\mu\). We claim
\[
\varepsilon^{m-\mu}P(\zeta/\varepsilon+\eta)
\longrightarrow L_\zeta(\eta)
\quad\text{in coefficients}.
\tag{6}
\]

Indeed homogeneity and the finite Taylor formula give for the component of degree \(j\)
\[
\varepsilon^{m-\mu}P_j(\zeta/\varepsilon+\eta)
=\sum_\alpha
\varepsilon^{m-\mu-j+|\alpha|}
\frac{\partial^\alpha P_j(\zeta)}{\alpha!}\eta^\alpha.
\tag{7}
\]
the hyperbolicity and strength input's multiple-characteristic result, now with degree \(j=m-d\), says
\(\partial^\alpha P_j(\zeta)=0\) whenever
\(|\alpha|<\mu+j-m\). At a noncharacteristic \(\zeta\), the latter bound is nonpositive and needs no vanishing assertion. Thus all coefficients of negative powers of \(\varepsilon\) in (7) are zero; exponent zero gives exactly (5), and positive exponents tend to zero. This proves (6), including the endpoint degree-zero terms.

The derivative-vector norm is homogeneous under scalar multiplication and continuous in the coefficients. Consequently
\[
\varepsilon^{m-\mu}S_P(\zeta/\varepsilon)
\longrightarrow S_{L_\zeta}(0)>0,
\qquad
\frac{P(\zeta/\varepsilon+\eta)}{S_P(\zeta/\varepsilon)}
\longrightarrow
Q_\zeta(\eta):=\frac{L_\zeta(\eta)}{S_{L_\zeta}(0)}.
\tag{8}
\]
Therefore \(Q_\zeta\) is an exact normalized high-frequency localization in direction \(\zeta\). The full limit is \(L_\zeta\), rather than just \(H_\zeta\). When \(\mu=0\), (5) reduces to the nonzero constant \(F(\zeta)\).

## 2. The cone forced in each wavefront fiber

For the causal inverse \(E\), define
\[
D_\zeta=\{x:(x,\zeta)\in\operatorname{WF}(E)\}.
\tag{9}
\]
Then the closed convex cone generated by \(D_\zeta\) contains \(C_\zeta\). Here “generated” includes closure and all nonnegative finite linear combinations; no assertion that the fiber itself fills that cone is made.

Apply the regular-inverse wavefront input to (8). It gives a regular fundamental solution \(G_\zeta\) of \(Q_\zeta(D)\), with
\[
\operatorname{supp}G_\zeta\subset D_\zeta.
\tag{10}
\]
Let
\[
E_\zeta=G_\zeta/S_{L_\zeta}(0).
\tag{11}
\]
Since \(Q_\zeta(D)G_\zeta=\delta_0\), formula (11) gives
\(L_\zeta(D)E_\zeta=\delta_0\). Its support is unchanged.

One also has \(D_\zeta\subset\operatorname{supp}E\subset C\). To justify the first inclusion, a distribution vanishing on an open neighborhood has a zero localized Fourier transform there in every direction, by the defining wavefront test. The cone \(C\) has the quantitative strict-normal bound proved in the causal-inverse lesson:
\[
N\cdot x\ge b|x|\qquad(x\in C)
\tag{12}
\]
for some \(b>0\). Thus \(E_\zeta\) is supported in a closed cone strictly positive in normal \(N\) away from zero.

If \(\mu\ge1\), the causal inverse input's cone converse makes \(L_\zeta\) hyperbolic in \(N\). Its principal part is \(H_\zeta\). The canonical causal inverse of \(L_\zeta\) has support in \(C_\zeta\subset C\subset H_N\); \(E_\zeta\) is also supported in \(H_N\). the causal inverse input's arbitrary-distribution halfspace uniqueness identifies the two inverses. The minimal closed convex cone containing \(\operatorname{supp}E_\zeta\) is therefore exactly \(C_\zeta\). By (10), that cone is contained in the closed convex cone generated by \(D_\zeta\), as claimed.

If \(\mu=0\), \(L_\zeta=F(\zeta)\ne0\) is scalar. Its only fundamental solution is \(F(\zeta)^{-1}\delta_0\). Hence \(0\in D_\zeta\), and \(C_\zeta=\{0\}\) is again contained in the generated cone. This handles noncharacteristic frequencies without imposing a positive tangent degree. In fact, for every \(\zeta\), the equation \(L_\zeta(D)E_\zeta=\delta_0\) forces \(0\in\operatorname{supp}E_\zeta\), since differentiation cannot enlarge support. Thus the origin lies in every \(D_\zeta\).

The proof uses regularity of the actual causal inverse, the universal extraction theorem, the full limiting operator, and arbitrary-growth uniqueness. The canonical upper bound for a different averaging inverse in the regular-kernel wavefront lesson is not substituted for any of these steps.

## 3. A uniform conic zero-free region

Fix \(\zeta_0\ne0\). Let \(\Gamma_1\) be an open convex cone containing \(N\), with
\[
\overline{\Gamma_1}\setminus\{0\}
\subset\Gamma(H_{\zeta_0},N).
\tag{13}
\]
There are a real barrier \(\tau'_0\), a conic neighborhood \(W\) of \(\zeta_0\), constants \(\gamma>0\) and \(R<\infty\), such that
\[
\begin{gathered}
|P(\xi+i\tau N+i q)|\ge\gamma,\\
\xi\in W,\quad|\xi|\ge R,\quad
\tau<\tau'_0,\quad
q\in-\Gamma_1,\quad |q|\le\gamma|\xi|,
\quad|\tau|\le\gamma|\xi|.
\end{gathered}
\tag{14}
\]
The same conclusion includes \(q=0\), by the argument below. The single \(\gamma\) is used for both perturbation bounds and the denominator lower bound.

First suppose \(\mu=\deg H_{\zeta_0}\ge1\). Choose a full-polynomial barrier \(\tau_0<0\), reducing an available barrier if necessary. Homogenize:
\[
p(w,s)=s^mP(w/s)
=\sum_{j=0}^m s^{m-j}P_j(w).
\tag{15}
\]
For real \(w\), \(s>0\), and \(t<\tau_0s\), one has \(p(w+itN,s)\ne0\). For \(s=0\) and \(t<0\), this follows instead from homogeneous hyperbolicity of \(F\).

The compact set
\[
K=\overline{\Gamma_1}\cap S^{n-1}
\tag{16}
\]
lies inside \(\Gamma(H_{\zeta_0},N)\). Its leading values satisfy
\(\inf_{\theta\in K}|H_{\zeta_0}(\theta)|>0\). Uniform Taylor expansion gives
\[
p(\zeta_0+iz\theta,0)
=(iz)^\mu H_{\zeta_0}(\theta)+O(|z|^{\mu+1}),
\quad\theta\in K.
\tag{17}
\]
All constants are uniform on \(K\). Choose \(r>0\) so small that the zero at \(z=0\) has exactly multiplicity \(\mu\), with no other zero on \(|z|\le2r\), uniformly in \(\theta\). One obtains this directly by dividing (17) by \(z^\mu\) and keeping its uniformly nonzero leading value.

For real \(w\) close to \(\zeta_0\), small real \(t\), and small \(s\ge0\), Rouché's theorem now gives exactly \(\mu\) zeros of
\[
z\longmapsto p(w+itN+iz\theta,s)
\tag{18}
\]
inside \(|z|<r\), counting multiplicity; after reducing the parameter neighborhood, all those zeros lie in \(|z|<r/4\). There is a uniform positive lower bound for the absolute value of (18) on \(|z|=r\). This uniform form follows from compactness of \(K\), uniform polynomial coefficient continuity, and the two circles in the preceding zero-free disk.

For
\[
s\ge0,\qquad t<\tau_0s,
\tag{19}
\]
none of the zeros in that disk is on the imaginary axis. Indeed, if \(z=i v\), \(v\in\mathbb R\), then \(iz\theta=-v\theta\) is real, and the full or principal barrier following (15) applies. Their real parts are all positive. To verify the sign, deform the parameters within (19) to \(s=0\), \(w=\zeta_0\), and \(\theta=N/|N|\). The small real parameter domain in (19) is connected, and \(K\) is connected by normalized convex combinations with \(N/|N|\). No root crosses the imaginary axis or the disk boundary during this deformation. At the final parameters, homogeneous hyperbolicity gives
\[
\operatorname{Re}z=-t|N|>0
\tag{20}
\]
for every root of \(F(\zeta_0+i(t+z/|N|)N)\). This proves the sign for all the \(\mu\) small roots of (18).

Denote these roots by \(z_1,\ldots,z_\mu\), repeated by multiplicity, and divide (18) by their product. The resulting holomorphic quotient has no zero on \(|z|\le r\). On \(|z|=r\), its modulus has a positive uniform lower bound, because (18) has such a bound and each \(|z-z_\nu|\le5r/4\). The maximum principle applied to the reciprocal extends the same lower bound to the disk. For real \(-r/2\le a\le0\), (20) gives \(|a-z_\nu|\ge|a|\). Thus, with one \(c>0\),
\[
|p(w+itN+ia\theta,s)|\ge c|a|^\mu
\tag{21}
\]
for all the stated nearby parameters satisfying (19).

Write \(s=|\zeta_0|/|\xi|\), \(w=s\xi\), \(t=s\tau\), and \(a=s\sigma\). Choose a conic neighborhood \(W\) so that \(w\) is in the preceding neighborhood of \(\zeta_0\). Formula (15) and (21) give constants \(c_1,A,B,R_1>0\) such that
\[
\begin{gathered}
|P(\xi+i\tau N+i q)|
\ge c_1|q|^\mu|\xi|^{m-\mu},\\
\xi\in W,\quad|\xi|\ge R_1,\quad\tau<\tau_0,\\
q\in-\overline{\Gamma_1},\quad |q|\le A|\xi|,
\quad|\tau|\le B|\xi|.
\end{gathered}
\tag{22}
\]
Here \(q=\sigma\theta\), \(\sigma\le0\), \(\theta\in K\). The constants \(A,B\) are chosen to keep \(a,t,s\) in the bounded parameter region. If \(q=0\), the inequality (22) is trivial, but the next step gives a positive bound there too.

Since \(N\in\Gamma_1\) and \(\Gamma(H_{\zeta_0},N)\) is an open convex hyperbolicity cone of positive degree, \(-N\) cannot lie in that latter cone: its convexity would otherwise include zero. By (13),
\[
d:=\operatorname{dist}(N,-\overline{\Gamma_1})>0.
\tag{23}
\]
For \(q\in-\Gamma_1\) or \(q=0\), one has \(q-N\in-\Gamma_1\) and \(|q-N|\ge d\). Rewrite the same complex frequency as
\[
\xi+i\tau N+iq
=\xi+i(\tau+1)N+i(q-N).
\tag{24}
\]
Take \(\tau'_0=\tau_0-1\). Choose \(\gamma\) initially smaller than \(A/2\) and \(B/2\), and increase \(R\) so that the constants \(|N|\) and \(1\) in the modified size bounds fit in the remaining halves of \(A|\xi|\) and \(B|\xi|\). Then (22), applied to (24), gives
\[
|P(\xi+i\tau N+iq)|
\ge c_1d^\mu|\xi|^{m-\mu}.
\tag{25}
\]
Since \(m-\mu\ge0\), for \(R\ge1\) we can decrease \(\gamma\) once more to obtain (14). This proves a fixed positive lower bound, rather than only absence of zeros.

If \(\mu=0\), \(F(\zeta_0)\ne0\). Compactness and continuity instead give a uniform nonzero principal value in a small complex neighborhood of the normalized real direction \(\zeta_0/|\zeta_0|\). For \(\xi\) in a sufficiently narrow real cone and
\(|q|,|\tau|\le\gamma|\xi|\), the normalized point
\[
\xi/|\xi|+i(\tau/|\xi|)N+i q/|\xi|
\tag{26}
\]
lies in that complex neighborhood when \(\gamma\) is small. Thus the principal contribution has absolute value at least \(c|\xi|^m\). The sum of the lower order contributions has absolute value at most \(C|\xi|^{m-1}\), uniformly over these normalized points. Increase \(R\) to absorb it and decrease \(\gamma\) below the resulting positive bound. This proves (14) in the noncharacteristic case, even without a sign restriction on \(q\). It also avoids any appeal to (23) for a degree-zero tangent cone.

## 4. The analytic upper wavefront cone

For the same actual causal inverse \(E\),
\[
\operatorname{WF}_A(E)
\subset\{(x,\zeta):\zeta\ne0,\ x\in C_\zeta\}.
\tag{30}
\]
Thus the upper bound applies to analytic singularities, while the lower wavefront-cone section supplies the ordinary wavefront lower bound. the lower wavefront-cone section and \(\operatorname{WF}\subset\operatorname{WF}_A\) give every nonzero covector at the origin for both notions.

Fix \(\zeta_0\ne0\) and \(x_0\notin C_{\zeta_0}\). By the polar definition there is \(v\in\Gamma(H_{\zeta_0},N)\) with \(x_0\cdot v<0\). At positive tangent degree, choose an open convex cone \(\Gamma_1\) containing \(N,v\), whose nonzero closure lies in that tangent cone. Take the conic hull of sufficiently small balls about \(N,v\): their normalized convex combinations form a compact set in the tangent cone and miss zero, since a positive-degree open convex cone cannot contain opposite vectors. Small balls retain the angular margin. At degree zero take \(\Gamma_1=\mathbb R^n\), using the uniform zero-free-region section's degree-zero argument.

Apply the uniform zero-free-region section to \(\Gamma_1\). Choose a negative \(\tau<\tau'_0\), also below the causal inverse input's global full-polynomial barrier. Choose
\[
\theta=-\varepsilon v,\quad
0<|\theta|<\min(\gamma/2,1/4),\quad
x_0\cdot\theta>0.
\tag{31}
\]
Here \(\gamma,W,R\) are from (14). The halfspace \(X_\theta=\{x:x\cdot\theta>0\}\) contains \(x_0\). Every real base below is relatively compact in this halfspace, so \(x\cdot\theta\ge c_X>0\).

For \(a>|\tau N|^2+1\), put
\[
Q(z)=(a+z\cdot z)^n.
\tag{32}
\]
The dot product is complex bilinear. On \(z=\xi+i\tau N\), the real part of \(a+z\cdot z\) is at least \(1+|\xi|^2\). The global root barrier bounds \(|P(\xi+i\tau N)|\) below by a positive constant. Hence
\[
E_1(x)=(2\pi)^{-n}
\int_{\mathbb R^n}
\frac{e^{ix\cdot(\xi+i\tau N)}}{Q(\xi+i\tau N)P(\xi+i\tau N)}
\,d\xi
\tag{33}
\]
converges absolutely, locally uniformly in real \(x\), with integrand \(O((1+|\xi|)^{-2n})\). Acting distributionally by \((a-\Delta)^n\), first pairing with a compact test whose Fourier–Laplace transform decreases rapidly, cancels \(Q\). the causal inverse input's construction of the actual causal inverse gives
\[
E=(a-\Delta)^nE_1.
\tag{34}
\]
There is no global temperedness assertion for \(E\).

Choose a smooth degree-zero \(\chi\) on \(\mathbb R^n\setminus0\), \(0\le\chi\le1\), equal to one near \(\mathbb R_+\zeta_0\), with angular support compactly inside \(W\). Increase \(R_0\ge R\) so that for \(r=|\xi|\ge R_0\), \(|\tau|\) satisfies (14) and \(|\tau N|+|\theta|r\le r/2\). For \(T>R_0\) deform the exterior contour by
\[
G_T(\xi)=
\xi+i\tau N+i\chi(\xi)\min(r,T)\theta,
\qquad r\ge R_0.
\tag{35}
\]
The homotopy replaces \(\theta\) by \(s\theta\), \(0\le s\le1\). Where \(\chi>0\), the extra imaginary vector lies in \(-\Gamma_1\), has norm at most \(\gamma r\), and the uniform zero-free-region section gives \(|P|\ge\gamma\), including \(s=0\). Where \(\chi=0\), use the global base-contour bound. Every intermediate contour also satisfies
\[
\operatorname{Re}(a+z\cdot z)
=a+r^2-|\operatorname{Im}z|^2\ge3r^2/4.
\tag{36}
\]
Thus \(Q\) is zero-free and \(|Q|\ge c r^{2n}\), uniformly in \(T,s\).

Write \(b_T=\chi\min(r,T)\). Its gradient is uniformly bounded, since \(\nabla\chi=O(r^{-1})\), \(\min(r,T)\le r\), and the radial factor is Lipschitz with derivative at most one. The volume-form Jacobian is
\[
J_T=\det(I+i\theta\otimes\nabla b_T)
=1+i\,\nabla b_T\cdot\theta,\qquad |J_T|\le C.
\tag{37}
\]
Divide at the kink \(r=T\), apply Stokes on both smooth pieces, and cancel the common boundary. Alternatively use smooth monotone radial approximants with the same bounds and dominated convergence.

The holomorphic \(n\)-form in (33) is closed away from denominator zeros. Apply Stokes to the homotopy on \(R_0\le r\le M\). On a compact real base in \(X_\theta\),
\[
|e^{ix\cdot z}|
=e^{-\tau x\cdot N-sb_T(\xi)x\cdot\theta}\le C_X.
\tag{38}
\]
The outer lateral surface has pullback volume at most \(CM^n\), including the homotopy direction, and rational factor \(O(M^{-2n})\). Its integral is \(O_X(M^{-n})\to0\). The interior \(r<R_0\) and compact connector at \(r=R_0\) give an entire function \(B_\theta(x)\), since their contours and zero-free denominators are compact and fixed.

As \(T\to\infty\), exterior integrands with Jacobians are bounded by \(C_Xr^{-2n}\), integrable for every \(n\ge1\). At each fixed exterior frequency, they eventually stabilize to the graph and Jacobian
\[
G(\xi)=\xi+i\tau N+i\chi(\xi)r\theta,\qquad
J=1+i\,\nabla(\chi r)\cdot\theta.
\tag{39}
\]
Dominated convergence gives the actual equality
\[
E_1(x)=B_\theta(x)
+(2\pi)^{-n}
\int_{r\ge R_0}
\frac{e^{ix\cdot G(\xi)}J(\xi)}
{Q(G(\xi))P(G(\xi))}\,d\xi,\quad x\in X_\theta.
\tag{40}
\]

Choose a degree-zero cutoff \(\rho\), equal to one in a smaller conic neighborhood of \(\zeta_0\), with angular support in \(\{\chi=1\}\). The integral part \(A_\theta\) with factor \(\rho\) is analytic on \(X_\theta\). On its support, \(\operatorname{Im}G=\tau N+r\theta\). For \(z=x+iy\) close to a compact real base,
\[
|e^{iz\cdot G(\xi)}|
\le C_X\exp(-c_Xr+|y|r).
\tag{41}
\]
For \(|y|<c_X/2\) this provides an integrable exponential majorant for every derivative. Uniform convergence on complex compact subsets proves holomorphy.

Cover the compact angular support of \(1-\rho\) by finitely many sets \(V_j\), with a smooth partition \(\sum_j\psi_j=1\) there. Choose open convex cones \(Y_j\) and \(d_j>0\) such that, with \(\omega_0=\zeta_0/|\zeta_0|\),
\[
y\cdot\omega\ge d_j|y|
\quad(\omega\in V_j,\ y\in Y_j),\qquad
y_j\cdot\omega_0<0\quad\text{for some }y_j\in Y_j.
\tag{42}
\]
For a unit \(\omega\ne\omega_0\), take \(y_j=\omega-\omega_0\). Its dot products with \(\omega,\omega_0\) are respectively \(1-\omega_0\cdot\omega>0\) and \(\omega_0\cdot\omega-1<0\). Narrow neighborhoods preserve both signs. The support stays a positive angle away from \(\omega_0\), so compactness supplies the finite cover and positive constants.

Let \(R_j(z)\) be the exterior integral with factor \((1-\rho)\psi_j\). For a compact real base, \(y\in Y_j\), and small \(|y|\),
\[
|e^{i(x+iy)\cdot G(\xi)}|
\le C_X\exp(-c_X\chi(\xi)r-d_j|y|r).
\tag{43}
\]
It is holomorphic in this tube, with derivatives justified for positive \(|y|\) by exponential decay. The rational factor and Jacobian retain the integrable bound \(Cr^{-2n}\); thus \(R_j\) is uniformly bounded as \(y\to0\) in \(Y_j\). Dominated convergence gives its continuous, hence distributional, boundary value with the exact real integral. These are the boundary and analytic-wavefront input's complete hypotheses, with growth exponent zero. Therefore
\[
\operatorname{WF}_A(R_j)
\subset X_\theta\times(Y_j^*\setminus\{0\}).
\tag{44}
\]
The second inequality in (42) excludes \(\zeta_0\) from \(Y_j^*\). Since \(B_\theta+A_\theta\) is analytic and \(E_1=B_\theta+A_\theta+\sum_jR_j\) is a finite sum, \((x,\zeta_0)\notin\operatorname{WF}_A(E_1)\) for every \(x\in X_\theta\). Differential decrease in the boundary and analytic-wavefront input and (34) give the same exclusion for \(E\), in particular at \(x_0\).

Every point outside \(C_{\zeta_0}\) admits a separating \(v\), and every nonzero \(\zeta_0\), including degree zero, has been allowed. This proves (30). The proof retains the compact entire connector, uniform integrable graph bound, holomorphic interior part and finitely many separated tube boundary values. Smooth Fourier decay alone is not used as an analytic-wavefront criterion.

## 5. Making the angular Fourier formula a distributional formula

Let \(k\in\mathbb Z\), and let \(u\in\mathcal S'(\mathbb R^n)\) be homogeneous of degree \(-n-k\) and have parity opposite to \(k\):
\[
u(-x)=(-1)^{k+1}u(x).
\tag{47}
\]
Define the real one-dimensional distributions
\[
\sigma_k(t)=
\begin{cases}
\dfrac{\operatorname{sgn}(t)t^k}{2k!},&k\ge0,\\[4pt]
\delta^{(-k-1)}(t),&k<0.
\end{cases}
\tag{48}
\]
Theorem 4.1 of [Angular distributions and their full Fourier transforms](../../AN02-L185.html#4-the-angular-fourier-identity-on-the-whole-frequency-space) gives the full test-pairing identity
\[
\widehat u(\xi)=
\pi i^{-1-k}
\int_{S^{n-1}}u(x)\sigma_k(x\cdot\xi)\,dS(x).
\tag{49}
\]
The right-hand side means a canonical product, sphere restriction, and compact-fiber projection. It is not a pointwise multiplication of arbitrary distributions.

Euler's identity for \(u\) is
\((x\cdot\partial_x+n+k)u=0\). The analytic Euler operator has principal symbol proportional to \(x\cdot\eta\). Dilation equations and tangential analytic singularities, Theorem 4.1, gives, for \(\mathcal W=\operatorname{WF}\) or \(\operatorname{WF}_A\), and hence also for any intermediate \(WF_L\),
\[
(x,\eta)\in\mathcal W(u)\quad\Longrightarrow\quad
x\cdot\eta=0.
\tag{50}
\]
Reflection (47), the pullback rule, and multiplication by its nonzero scalar also give
\[
(x,\eta)\in\mathcal W(u)
\quad\Longleftrightarrow\quad
(-x,-\eta)\in\mathcal W(u).
\tag{51}
\]
Positive dilations of \(x\) leave its covector ray unchanged in these wavefront sets, because \(u\) is homogeneous and the dilation pullback changes the covector by a positive scalar.

On \((\mathbb R^n\setminus0)\times\mathbb R^n\), let \(f(x,\xi)=x\cdot\xi\). Its differential and transpose are
\[
df(x,\xi)(v,w)=v\cdot\xi+x\cdot w,\qquad
{}^tdf(x,\xi)t=(t\xi,tx).
\tag{52}
\]
This is a submersion, since \(x\ne0\). The only singular base point of \(\sigma_k\) is zero. For \(k<0\) the delta derivative has both nonzero frequency rays there. For \(k\ge0\), its \(k\)-th derivative is a nonzero multiple of \(\operatorname{sgn}t\), its next derivative a nonzero multiple of \(\delta_0\); smoothness away from zero and differential decrease therefore give the same two rays. Since the ordinary set is already both rays and the analytic set can contain no other base point, all the indicated wavefront notions have exactly that one-dimensional set. The submersion pullback, in local coordinates with \(f\) as one coordinate, yields
\[
\mathcal W(\sigma_k(x\cdot\xi))
=\{(x,\xi;t\xi,tx):x\cdot\xi=0,\ t\ne0\}.
\tag{53}
\]
The equality, rather than just inclusion, follows in those coordinates from \(\sigma_k\) tensored with the constant distribution in the remaining variables.

The tensor-product rule gives
\[
\mathcal W(u(x)\otimes1)
=\{(x,\xi;\eta,0):(x,\eta)\in\mathcal W(u)\}.
\tag{54}
\]
A nonzero covector in (53) has second component \(tx\ne0\), whereas every covector in (54) has second component zero. Opposing covectors from these two sets cannot sum to zero. Thus the distribution product
\[
A(x,\xi)=u(x)\sigma_k(x\cdot\xi)
\tag{55}
\]
is canonically defined throughout \(x\ne0\). The product rule retains all three contributions:
\[
\begin{split}
\mathcal W(A)\subset{}&
\{(x,\xi;\eta+t\xi,tx):
x\cdot\xi=0,\ t\ne0,\ (x,\eta)\in\mathcal W(u)\}\\
&{}\cup\mathcal W(u\otimes1)
\cup\mathcal W(\sigma_k(x\cdot\xi)).
\end{split}
\tag{56}
\]
Support restrictions could narrow the last two sets, but are unnecessary for this valid upper bound.

Every first covector \(\lambda\) in (56) satisfies \(x\cdot\lambda=0\), using (50) and \(x\cdot\xi=0\). The conormal of the sphere restriction
\[
j:S^{n-1}\times\mathbb R^n\longrightarrow
(\mathbb R^n\setminus0)\times\mathbb R^n
\]
consists of \((x,\xi;a x,0)\), \(a\ne0\). It cannot intersect (56), since \(x\cdot(ax)=a\ne0\). Therefore \(j^*A\) exists, with the exact operation-continuity contract in the angular Fourier and wavefront-operation inputs. Projection
\(\pi:S^{n-1}\times\mathbb R^n\to\mathbb R^n\) is proper on its support: the inverse image of a compact frequency set lies in the compact product with the sphere. Hence \(\pi_*j^*A\), with the standard sphere density \(dS\), is a well-defined distribution. This proves that (49) is a genuine distributional expression. Pairing it with a test in \(\xi\) agrees with the Radon test-pairing identity in the complete angular Fourier theorem, so it equals \(\widehat u\), with the constant in (49) unchanged.

The proper projection rule permits a nonzero output covector \(y\) only if a covector in (56) restricts to zero in the sphere variable. Such a first covector is proportional to \(x\); orthogonality (50) forces it to be zero. The tensor-only term then has output covector zero, which is excluded. For \(\xi\ne0\), the \(\sigma_k\)-only term would require \(t\xi=0\), also impossible. The mixed term requires
\[
\eta=-t\xi,\qquad y=tx,\qquad t\ne0.
\tag{57}
\]
Consequently
\[
\mathcal W(\widehat u)
\subset
\{(\xi,tx):\xi\ne0,\ t\ne0,\ (x,-t\xi)\in\mathcal W(u)\}
\cup\{(0,y):y\ne0\}.
\tag{58}
\]
Equations (51), positive homogeneity in the base point, and positive conicity in covectors turn its first set into
\[
\{(\xi,y):\xi\ne0,\ y\ne0,\ (-y,\xi)\in\mathcal W(u)\}.
\tag{59}
\]
For example, if \(t>0\), reflect \((x,-\xi)\) to \((-x,\xi)\), then dilate the base by \(t\); if \(t<0\), dilate \((x,\xi)\) by \(-t\). This verifies the signs in (59). the angular Fourier and wavefront-operation inputs's homogeneous Fourier interchange supplies the reverse implication away from both origins.

Fix \(\xi_0\ne0\). To restrict \(A\) directly to \(S^{n-1}\times\{\xi_0\}\), its ambient conormal is \((a x,\nu)\), where \(\nu\) is arbitrary and a nonzero pair is required. Orthogonality again forces \(a=0\). A tensor-only covector cannot then be nonzero. A \(\sigma_k\)-only covector would have \(t\xi_0=0\), impossible. In the mixed case the only obstruction is
\[
(x,-t\xi_0)\in\mathcal W(u)
\quad\text{for some }|x|=1,\ t\ne0.
\tag{60}
\]
Reflection and conicity show that this is equivalent to \((x,\xi_0)\in\mathcal W(u)\) for some \(x\ne0\). Thus (49) has a canonical pointwise value whenever
\[
(x,\xi_0)\notin\mathcal W(u)\quad\text{for every }x\ne0.
\tag{61}
\]
The homogeneous Fourier interchange and the base projection of each wavefront notion identify this domain exactly with the complement of the corresponding singular support of \(\widehat u\), away from zero. On an open neighborhood satisfying (61), the sphere distribution and its projection vary in the required regularity class, so the pointwise value agrees with the smooth, analytic or \(C^L\) representative there. This retains the analytic and all declared derivative-sequence variants; it does not interpret \(L\) as a Sobolev order.

In dimension one the sphere is the two-point manifold \(S^0\), with counting surface measure, and all compact-fiber and conormal calculations above still apply. Later equatorial cycle formulas require separate attention to dimension; no empty-sphere convention is silently inserted into (49).

## 6. The angular representation of homogeneous causal kernels

For this section let \(F\) itself be homogeneous, of degree \(m\ge1\), hyperbolic in \(N\). Let \(E_F\) be its positive-side causal inverse, and put
\[
E_\alpha=D^\alpha E_F,\qquad
q=m-n-|\alpha|,\qquad
W_F=\bigcup_{\xi\ne0}\Gamma(H_\xi,N)^*.
\tag{62}
\]
The set \(W_F\) contains zero and lies in \(C=\Gamma(F,N)^*\), by the tangent-polynomial section. It is a closed cone. To prove closure, positive rescaling of \(\xi\) multiplies its tangent polynomial by a nonzero scalar, so its component and polar are unchanged. For a convergent sequence \(x_j\in W_F\), choose witnessing frequencies of unit length. A subsequence converges to a nonzero unit \(\xi\); the proved polynomial tangent-cone input's closed graph then puts the limit \(x\) in \(\Gamma(H_\xi,N)^*\). Conicity follows from each polar being a cone. No assertion that \(W_F\) is convex is needed.

the causal inverse input gives the tempered homogeneous boundary value
\[
\widehat E_\alpha(\xi)
=\frac{\xi^\alpha}{F(\xi-i0N)},
\qquad
\deg\widehat E_\alpha=|\alpha|-m=-n-q.
\tag{63}
\]
Define the parity-selected jump
\[
\begin{split}
u_\alpha(\xi)
&=\widehat E_\alpha(\xi)
-(-1)^q\widehat E_\alpha(-\xi)\\
&=\xi^\alpha
\left(\frac1{F(\xi-i0N)}
-\frac{(-1)^n}{F(\xi+i0N)}\right).
\end{split}
\tag{64}
\]
For the second equality, homogeneity gives
\(\widehat E_\alpha(-\xi)=(-1)^{|\alpha|-m}
\xi^\alpha/F(\xi+i0N)\), and
\(q+|\alpha|-m=-n\). Thus \(u_\alpha\) has degree \(-n-q\) and parity \((-1)^{q+1}\), exactly the two hypotheses of the angular distribution section with \(k=q\). Its Fourier transform is
\[
\widehat u_\alpha(x)
=(2\pi)^n\bigl(E_\alpha(-x)-(-1)^qE_\alpha(x)\bigr),
\tag{65}
\]
by the squared-Fourier identity with reflection and the fixed unnormalized convention.

Apply (49) at argument \(-x\). Equations (64)–(65) give, as a distribution identity in \(x\),
\[
\begin{split}
E_\alpha(x)-(-1)^qE_\alpha(-x)
={}&(2\pi)^{-n}\pi i^{-1-q}
\int_{S^{n-1}}\sigma_q(-x\cdot\xi)\,\xi^\alpha\\
&\quad\cdot
\left(\frac1{F(\xi-i0N)}
-\frac{(-1)^n}{F(\xi+i0N)}\right)dS(\xi).
\end{split}
\tag{66}
\]
All products and sphere integrations carry the angular distribution section's verified hypotheses. In particular no value of a singular rational function on the real characteristic set is chosen arbitrarily.

The analytic wavefront set of the jump obeys
\[
(\xi,y)\in\operatorname{WF}_A(u_\alpha),\quad
\xi\ne0
\quad\Longrightarrow\quad
y\in C_\xi\cup(-C_\xi).
\tag{67}
\]
Indeed differential decrease gives
\(\operatorname{WF}_A(E_\alpha)\subset
\{(x,\xi):x\in C_\xi\}\) from the analytic upper-cone section. The homogeneous Fourier interchange in the angular Fourier and wavefront-operation inputs then gives
\(\operatorname{WF}_A(\widehat E_\alpha)\subset
\{(\xi,y):-y\in C_\xi\}\) away from both origins. Reflection of (63) supplies the other sign in (64). For homogeneous \(F\), its Taylor expansion at \(-\xi\) has the same vanishing order as at \(\xi\) and
\[
H_{-\xi}(h)=(-1)^{m-\deg H_\xi}H_\xi(h).
\tag{68}
\]
The nonzero sets and components containing \(N\) agree, so \(C_{-\xi}=C_\xi\). These facts prove (67); a covector \(y=0\) is excluded throughout.

If \(x\notin W_F\cup(-W_F)\), (67) excludes every obstruction to the pointwise sphere formula in the angular distribution section, and (66) is valid as an analytic identity near \(x\). Its left-hand side has analytic singular support contained in \(W_F\cup(-W_F)\) away from zero. Also \(E_\alpha(-x)\) vanishes outside \(-C\), since differentiation preserves the support of \(E_F\). Therefore for
\[
x\notin W_F\cup(-C)
\tag{69}
\]
the right-hand side of (66) equals \(D^\alpha E_F(x)\) pointwise and analytically. This region is contained in the complement of \(W_F\cup(-W_F)\), because \(W_F\subset C\). the analytic upper-cone section separately shows that \(E_\alpha\) itself is analytic outside \(W_F\). The difference's symmetric singular bound and the individual kernel's sharper bound are distinguished.

When \(n\) is even, the parenthesis in (64) vanishes on every real open set where \(F\ne0\); both boundary values there equal the same smooth \(1/F\). Thus its support lies in \(\{F=0\}\). If \(F\) has real coefficients and is of real principal type, its characteristic gradient is nonzero for \(\xi\ne0\), and
\[
\frac1{F(\xi-i0N)}-\frac1{F(\xi+i0N)}
=2\pi i\,
\operatorname{sgn}(\partial_NF(\xi))\,\delta(F(\xi))
\quad(\xi\ne0).
\tag{70}
\]
The nonzero directional derivative follows from the hyperbolicity and strength input's simple-root criterion. In a coordinate with \(F\) as one variable, the imaginary sign is that of \(\partial_NF\); the one-dimensional boundary jump \(1/(s-i0)-1/(s+i0)=2\pi i\delta(s)\) gives (70), with its exact sign. This is a smooth density on the characteristic hypersurface in the distributional coarea sense.

For \(q<0\), (48) localizes the angular expression to the intersection
\[
\{\xi\in S^{n-1}:F(\xi)=0,\ x\cdot\xi=0\}.
\tag{71}
\]
For \(x\) in (69) and real principal type, this intersection is transverse. On \(F=0\), Euler's identity makes \(\nabla F\) tangent to the sphere. On \(x\cdot\xi=0\), \(x\) is tangent too. Dependence of these two tangent normals would make \(x\) proportional to \(\nabla F(\xi)\); the tangent polar of this simple characteristic is the appropriate ray on that line, so \(x\) would be in \(W_F\cup(-W_F)\), a contradiction. At \(q=-1\), the two delta factors give the ordinary coarea integral over (71), with the signs and factor in (66),(70). At \(q<-1\), the derivative \(\delta^{(-q-1)}\) gives the corresponding transverse normal derivatives of that density; these derivatives are retained. This states precisely the characteristic-surface version of the angular formula and the extent to which its value is localized at the equator.

## 7. A transverse analytic deformation and its boundary value

Fix \(x\notin W_F\cup(-W_F)\). For every \(\xi\ne0\), the linear form \(v\mapsto x\cdot v\) takes both signs on \(\Gamma(H_\xi,N)\). Otherwise one of \(x,-x\) would belong to its polar. Choose two cone vectors with opposite signs and take their positive convex combination with zero \(x\)-pairing. This supplies a vector in the cone and in \(x^\perp\). At a degree-zero tangent point the cone is all of \(\mathbb R^n\), and zero is allowed; at positive tangent degree the selected vector cannot be zero.

the proved polynomial tangent-cone input's local cone stability keeps a selected vector valid in a neighborhood of its direction. Equation (68) permits the same choice near the opposite direction. A finite even partition of unity on the sphere combines these choices, by convexity of each component, into a smooth even degree-zero field. It has the properties
\[
x\cdot\Theta(\xi)=0,\qquad
\Theta(t\xi)=\Theta(\xi)\ (t\ne0),\qquad
\Theta(\xi)\in\Gamma(H_\xi,N).
\tag{72}
\]
It can be made real analytic without losing these properties. Extend it smoothly and evenly to a bounded annulus, multiply by an even radial compact cutoff equal to one near the unit sphere, and convolve with a narrow Gaussian. This gives an even real analytic vector field uniformly close to the original on the sphere. The identity \(x\cdot\Theta=0\) is linear and is preserved exactly by extension and convolution. Restriction to the sphere followed by \(\xi\mapsto\xi/|\xi|\) restores degree zero and remains real analytic away from zero. There is a uniform permitted approximation error: each original sphere value has a ball inside its tangent cone, this ball remains valid in a neighborhood by the proved polynomial tangent-cone input, and a finite subcover gives a positive minimum radius. Thus sufficiently close approximation retains the strict cone membership in (72).

For sufficiently small \(\varepsilon>0\), the two sphere deformations
\[
c_\varepsilon^\pm(\xi)=\xi\pm i\varepsilon\Theta(\xi),
\qquad |\xi|=1
\tag{73}
\]
avoid \(F=0\). the proved polynomial tangent-cone input gives this uniformly on the compact sphere, with a bound \(c\varepsilon^M\) for some finite \(M\). At noncharacteristic points use the ordinary nonzero neighborhood instead. The two signs have the same zero-exclusion property: \(F\) is real after the hyperbolicity and strength input's scalar normalization, and conjugation interchanges them.

We need the exact variable-direction boundary value, including the topology required to multiply and restrict it. In a neighborhood of a characteristic \(\xi_*\), choose a smaller pointed cone \(G\) with closure in \(\Gamma(H_{\xi_*},N)\), containing \(N\), the neighboring values of \(\Theta\), and any finite further interior directions needed to test a wavefront exclusion. Narrow it in angle so that it has a uniformly positive linear functional on its nonzero unit section. the proved polynomial tangent-cone input supplies a zero-free tube with power bound. Write \(f(z)=1/F(z)\) there, and
\[
f_\varepsilon(z)=f(z-i\varepsilon\Theta(z))
\tag{74}
\]
using the local holomorphic extension of the real analytic field. For \(z=w-iy\), \(y\in G\), and small \(|y|,\varepsilon\), the new imaginary magnitude is \(y+\varepsilon\operatorname{Re}\Theta(z)\). It remains in a compact smaller cone and has norm at least \(c(|y|+\varepsilon)\). The positive functional proves the latter assertion; the small complex-extension perturbation and the cone's angular margin preserve it. The real displacement \(\varepsilon\operatorname{Im}\Theta(z)=O(\varepsilon|y|)\) remains in the local real base. Thus
\[
|f_\varepsilon(w-iy)|
\le C(|y|+\varepsilon)^{-M}
\le C'|y|^{-M}
\tag{75}
\]
uniformly in \(\varepsilon\). On complex compact subsets with \(y\ne0\), \(f_\varepsilon\to f\) holomorphically.

Apply the finite-test boundary formula(2.8) in the boundary and analytic-wavefront input's actual the holomorphic-boundary lesson proof to this uniformly bounded family, with imaginary direction \(-Y\), \(Y\in G\). Its remainder contains \(t^M f_\varepsilon(w-itY)\), bounded independently of \(\varepsilon\). At each \(t>0\) it converges to \(t^Mf(w-itY)\); dominated convergence therefore makes the boundary values converge in distributions. The boundary value of \(f_\varepsilon\) on the real base is the actual analytic function \(1/F(w-i\varepsilon\Theta(w))\). The limit agrees with \(1/F(w-i0N)\), since \(N\in G\) and the full-cone boundary limit in that written proof is independent of the approach inside the cone.

For precision, the convergence also holds in the fixed-wavefront topology needed by the angular Fourier and wavefront-operation inputs. For a compact smooth cutoff \(\phi\) and a closed test-frequency cone outside the negative polar of \(G\), choose \(Y\in-G\) with \(Y\cdot\eta\le-c|\eta|\) on a smaller test cone. Apply the same almost analytic formula to the compact test \(\phi(w)e^{-iw\cdot\eta}\), keeping the exponential holomorphic and extending only \(\phi\) to order \(\ell\). The top face has exponential decay; the remainder is bounded by
\[
C_\ell\int_0^1
t^{\ell-M}e^{-ct|\eta|}\,dt
\le C'_\ell(1+|\eta|)^{-\ell+M-1},
\qquad \ell\ge M.
\tag{76}
\]
All constants are uniform in \(\varepsilon\). Since \(\ell\) is arbitrary, this is uniform rapid Fourier decay on that test cone. Distributional convergence gives uniform convergence on bounded frequency sets; use a higher-order bound (76) on the tail to obtain convergence in every weighted rapid-decay seminorm. If a tested covector lies outside \(-C_\xi\), its separating cone vector can be added to the compact smaller cone \(G\). A finite local cover then gives precisely the closed graph bound \(\{(\xi,\eta):\eta\in-C_\xi,\eta\ne0\}\). At noncharacteristic points ordinary holomorphic convergence gives smooth convergence directly. Conjugation gives the corresponding positive-boundary statement. This proves the variable analytic deformation limit, rather than assuming that a variable direction may be inserted into a distributional limit.

Let
\[
\omega(\zeta)=
\sum_{j=1}^n(-1)^{j-1}\zeta_j\,
d\zeta_1\wedge\cdots\wedge\widehat{d\zeta_j}
\wedge\cdots\wedge d\zeta_n
\tag{77}
\]
be the Kronecker form. On the real unit sphere it is the usual oriented surface form. The sphere restriction is transverse to the homogeneous boundary wavefront set by (50). At fixed \(x\notin W_F\cup(-W_F)\), the multiplier \(\sigma_q(-x\cdot\xi)\) has no opposing covector with either rational boundary value, by (67). The convergence just proved, the angular Fourier and wavefront-operation inputs's continuous restriction and product, and the smooth convergence of the pulled-back numerator and form therefore permit both deformed sphere integrals to converge to (66). Their arguments satisfy \(x\cdot c_\varepsilon^\pm(\xi)=x\cdot\xi\), so the one-dimensional distribution in this operation retains its real argument exactly. These observations justify using \(\omega\) on the deformed contours, including when \(q<0\) and the factor is a delta derivative.

## 8. The two oriented contour formulas

Assume \(n\ge2\), and fix \(x\) in (69), with \(\Theta\) as in the transverse deformation section. All orientations below start from the standard outward orientation of \(S^{n-1}\). Let
\[
\alpha_+=c_\varepsilon^-(S^{n-1})
+(-1)^{n-1}c_\varepsilon^+(S^{n-1}).
\tag{78}
\]
This is a formal oriented sum of cycles. For \(q\ge0\), the formula is
\[
D^\alpha E_F(x)=
\frac{(2\pi)^{1-n}i}{4q!}
\int_{\alpha_+}
(ix\cdot\zeta)^q\operatorname{sgn}(x\cdot\zeta)
\frac{\zeta^\alpha}{F(\zeta)}\,\omega(\zeta).
\tag{79}
\]
The sign is well defined because \(x\cdot\zeta=x\cdot\xi\) is real on the cycles; its value on the equator does not affect the hemisphere-chain integral.

To prove (79), substitute
\(\sigma_q(-x\cdot\xi)=(-1)^{q+1}
\operatorname{sgn}(x\cdot\xi)(x\cdot\xi)^q/(2q!)\)
into the transverse deformation section's deformation limit of (66). The negative-boundary contour has weight one and the positive-boundary contour weight \(-(-1)^n=(-1)^{n-1}\). Its scalar is
\((2\pi)^{-n}\pi i^{-1-q}(-1)^{q+1}/(2q!)
=(2\pi)^{1-n}i^{q+1}/(4q!)\).
This is exactly the constant and the factor \((ix\cdot\zeta)^q\) in (79).

The resulting integral is independent of sufficiently small positive \(\varepsilon\). If \(R=\sum\zeta_j\partial_{\zeta_j}\) and \(\Omega=d\zeta_1\wedge\cdots\wedge d\zeta_n\), then \(\omega=\iota_R\Omega\). The scalar
\((x\cdot\zeta)^q\zeta^\alpha/F(\zeta)\) has degree \(-n\). Hence
\[
d\bigl((x\cdot\zeta)^q\zeta^\alpha
F(\zeta)^{-1}\omega(\zeta)\bigr)=0
\quad(F(\zeta)\ne0).
\tag{80}
\]
This follows directly from
\(d(h\,\iota_R\Omega)=(Rh+nh)\Omega\).
Apply Stokes separately on the two hemispheres \(x\cdot\xi>0\) and \(x\cdot\xi<0\), during the zero-free homotopy between two small deformation parameters. The connecting equatorial part lies in \(H_x=\{\zeta:x\cdot\zeta=0\}\). The pullback of \(\omega\) to this complex hyperplane is zero: the radial vector is tangent to it, and \(n\) vectors in its \((n-1)\)-dimensional tangent space give zero under \(\Omega\). Thus even at \(q=0\) this connecting part contributes zero. The limit supplied by the transverse deformation section equals each of the constant integrals, proving (79).

Multiplying a hemisphere chain's orientation by \(\operatorname{sgn}(x\cdot\xi)\) removes the sign factor. Denote the resulting chain from (78) by \(\widetilde\alpha_+\). Put \(K_x=S^{n-1}\cap x^\perp\), oriented as the boundary of the negative hemisphere \(\{x\cdot\xi<0\}\), and let \(K^\pm=c_\varepsilon^\pm(K_x)\). The positive hemisphere has boundary \(-K_x\), so
\[
\partial\widetilde\alpha_+
=-2\bigl(K^-+(-1)^{n-1}K^+\bigr).
\tag{81}
\]
This is the exact boundary relation. Its boundary is a cycle in \(H_x\); the full hemisphere chain is not said to lie in that hyperplane.

For \(q<0\), put \(k=-q-1\), and choose a small positively oriented complex circle \(|z|=\delta\). Define
\[
\begin{split}
\alpha_-={}&
\{zx+\xi-i\varepsilon\Theta(\xi):
|z|=\delta,\ \xi\in K_x\}\\
&{}+(-1)^{n-1}
\{zx+\xi+i\varepsilon\Theta(\xi):
|z|=\delta,\ \xi\in K_x\}.
\end{split}
\tag{82}
\]
Each product cycle uses circle orientation first, then \(K_x\)'s boundary orientation. For a fixed sufficiently small \(\varepsilon>0\), compactness of \(K^\pm\) gives \(\delta_\varepsilon>0\) so that these cycles avoid \(F=0\) whenever \(0<\delta<\delta_\varepsilon\). They also avoid \(x\cdot\zeta=0\), because \(x\cdot\zeta=z|x|^2\). The second formula is
\[
D^\alpha E_F(x)=
\frac{(2\pi)^{-n}(-1)^{q+1}(-q-1)!}{2}
\int_{\alpha_-}
(ix\cdot\zeta)^q
\frac{\zeta^\alpha}{F(\zeta)}\,\omega(\zeta).
\tag{83}
\]

Here is the residue calculation, including its orientation. Rotate by an orientation-preserving orthogonal map to \(x=re_1\), \(r>0\), and use the local cylinder \(\xi=(t,y)\), \(|y|=1\), around the equator. Radial projection of this cylinder to the sphere preserves the angular integral of a homogeneous degree-\(-n\) density. The delta factor is supported at \(t=0\), so a cylinder neighborhood suffices. Put \(s(t)=\sqrt{1+t^2}\) and choose the sphere field locally by \(\Theta((t,y)/s(t))=\Theta(0,y)/s(t)\). Radially multiplying its deformed sphere by \(s(t)\) then gives exactly \((t,y)-i\varepsilon\Theta(0,y)\), with constant imaginary displacement in the \(t\) direction. The full scalar times Kronecker form in (66) has degree zero as an angular density, so this radial change introduces no extra factor. the proved polynomial tangent-cone input keeps the new sphere field allowed for small \(t\). It is real analytic on a neighborhood of the equator, which is all that the transverse deformation section's boundary-limit proof needs for this delta-supported integral. A smooth even cutoff can extend it elsewhere; no global analytic cutoff is asserted or needed. Its equatorial values, and hence the tube cycles (82), are unchanged.

Write \(\omega'\) for the Kronecker form in the last \(n-1\) variables and \(b(\zeta)=\zeta^\alpha/F(\zeta)\). Since
\(\sigma_q(-rt)=(-r)^{-k}r^{-1}\delta^{(k)}(t)\),
the two signs of differentiation cancel. The deformed angular expression is therefore
\[
J_\varepsilon=
(2\pi)^{-n}\pi i^k r^{-k-1}
\left(\int_{S^{n-2}}\partial_t^k b(0,y-i\varepsilon\Theta(y))\omega'
-(-1)^n\int_{S^{n-2}}\partial_t^k b(0,y+i\varepsilon\Theta(y))\omega'\right).
\tag{84}
\]
Its limit as \(\varepsilon\downarrow0\) is \(D^\alpha E_F(x)\), by the transverse deformation section applied locally near the equator.
Both spheres in this display have their standard orientation. At \(t=0\), the full Kronecker form on the cylinder is \(-dt\wedge\omega'\). The boundary orientation of the negative hemisphere is therefore minus the standard orientation of this \(S^{n-2}\). On the tube \(\zeta=zx+\beta\), \(\beta\in K^\pm\), one has
\(\omega=-r\,dz\wedge\omega'(\beta)\) and \(ix\cdot\zeta=ir^2z\).
Cauchy's residue formula gives
\(\oint z^{-k-1}b(rz,\beta)\,dz
=2\pi i\,r^k\partial_t^kb(0,\beta)/k!\).
The two minus signs from the form and the equatorial orientation cancel. Thus each tube integral is
\(2\pi i^{-k}r^{-k-1}/k!\) times its corresponding standard-sphere derivative integral. Substituting in (84) expresses \(J_\varepsilon\) as the right side of (83), since \(q+1=-k\). The closed-form period argument in the next paragraph makes that expression independent of sufficiently small positive \(\varepsilon\). Its the transverse deformation section limit is the actual kernel derivative, proving (83) at each such \(\varepsilon\), rather than identifying a finite deformation with its boundary limit prematurely.

The integrand in (83) is closed by the same degree calculation as (80), on \(\{F\ne0,\ x\cdot\zeta\ne0\}\). Its period is unchanged by small changes of the circle radius and by allowed equatorial deformations; compare parameter intervals using a common sufficiently small circle. Equation (81) says that the centers of the tube cycles in (82) are exactly \(-\tfrac12\partial\widetilde\alpha_+\), including multiplicities. This proves both formulas and their relation, with no unrecorded orientation sign.

For \(n=1\), the negative-\(q\) equatorial cycle is replaced by the direct scalar calculation. Write \(F(\xi)=a\xi^m\), with the positive direction oriented by \(N=1\). Then \(E_F(t)=a^{-1}i^m H(t)t^{m-1}/(m-1)!\). On \(t>0\), \(D^\alpha E_F\) is a polynomial derivative, and is zero when \(\alpha\ge m\), exactly the \(q<0\) case. The \(q\ge0\) formula uses the two-point oriented \(S^0\) interpretation of (78)–(79). No \(S^{-1}\) is used to supply a purported residue integral.

## 9. From a bounding cycle to a polynomial lacuna and an entire kernel

Assume first \(n\ge2\). For \(x\notin W_F\cup(-C)\), put
\[
M_x=\{\zeta\in\mathbb C^n:x\cdot\zeta=0,\ F(\zeta)\ne0\}.
\tag{85}
\]
The condition needed below is that \(K^-\) from the oriented contour section bounds a finite piecewise smooth singular chain \(T\) in \(M_x\). Fix the coefficient ring when stating null homology; the proof works over \(\mathbb Z\), \(\mathbb R\), or \(\mathbb C\). In particular, integral null homology implies the real or complex version. Stokes on such chains is the ordinary simplex Stokes theorem, extended linearly. No conclusion about integral torsion follows from the vanishing of periods.

### The cycle does not depend on its allowed deformation

For a fixed \(x\), take two allowed equatorial fields and interpolate them convexly. Each value stays in the open convex cone \(\Gamma(H_\xi,N)\), has zero \(x\)-pairing, and retains evenness. the proved polynomial tangent-cone input and compactness of the sphere times the interpolation interval give one small positive upper bound for the deformation parameter under which all resulting cycles avoid \(F=0\). The resulting cylinder in \(M_x\) has boundary equal to the difference of the two cycles. Changing between two sufficiently small positive parameters gives another such cylinder. Thus the homology class of \(K^-\), and whether it bounds \(T\), are independent of the allowed field and small parameter. Real analytic representatives can be used throughout; the interpolation of two such representatives is real analytic.

The bounding-chain property persists near a point where it holds. Let \(x_0\) be such a point and choose orientation-preserving orthogonal maps \(L_x\), continuous for \(x\) near \(x_0\), taking \(x_0/|x_0|\) to \(x/|x|\), with \(L_{x_0}=I\). One explicit local choice is the rotation in the plane spanned by these two unit vectors, with identity on its orthogonal complement; its limit at coincident vectors is the identity. It takes \(H_{x_0}\) to \(H_x\) and the oriented \(K_{x_0}\) to \(K_x\).

Transport the field by \(\Theta_x(\xi)=L_x\Theta_0(L_x^{-1}\xi)\). Compact local cone stability in the proved polynomial tangent-cone input makes it allowed for all \(x\) in a sufficiently small neighborhood. The chain \(T\) is compact and \(F\) has a positive minimum modulus on its support, so \(F(L_x\zeta)\ne0\) on that support when \(x\) is close enough to \(x_0\). Consequently \(L_xT\) bounds the transported allowed cycle in \(M_x\). Choice independence identifies it with any of the allowed cycles at that \(x\). This proves local persistence.

This argument proves openness of the set of points satisfying the condition. It does not, by itself, prove that its complement is open or that null homology is constant on an entire component: a compact bounding chain was available only at the starting point. The separate global topological implication is proved in [Equatorial cycles and the projective period test](../../AN02-L184.html#complete-proof). The component-wide mathematical consequence below has its own analytic proof and does not assume that implication.

### One bounding cycle gives homogeneous polynomials on the whole component

Let \(V\) be the connected component of \(\mathbb R^n\setminus(W_F\cup(-C))\) containing \(x_0\). For every integer \(k\ge1\), let \(E_k\) be the causal inverse of \(F(D)^k\), with support in \(C\). The hyperbolicity component of \(F^k\) is the same as that of \(F\), since their nonzero sets are the same. At a direction \(\xi\), the tangent polynomial is \(H_\xi^k\). Its nonzero component and polar are also unchanged. Therefore \(W_{F^k}=W_F\). The cycle and its bounding chain can be chosen independently of \(k\). the analytic upper-cone section gives analyticity of \(E_k\) outside \(W_F\); the homogeneous representation section gives homogeneity of degree
\[
d_k=mk-n.
\tag{86}
\]

For each \(x\) in the neighborhood where a bounding chain exists, conjugation gives a chain bounding \(K^+\) as well. This uses the real scalar normalization of \(F\) from the hyperbolicity and strength input; its zero set is invariant under conjugation. Choose a small common circle \(|z|=\delta\) such that \(F(zx+\zeta)\ne0\) for every \(\zeta\) on these two compact chains. On their products with the circle, \(x\cdot(zx+\zeta)=z|x|^2\ne0\).

If \(|\alpha|>d_k\), the integrand in (83), with \(F\) replaced by \(F^k\), is a closed \((n-1)\)-form on this product region. The circle-first product orientation satisfies
\(\partial(S^1\times T)=-S^1\times\partial T\).
Stokes therefore makes each of the two tube periods zero. Formula (83) yields
\[
D^\alpha E_k(x)=0\qquad(|\alpha|>d_k)
\tag{87}
\]
on a nonempty open neighborhood of \(x_0\).

Each derivative in (87) is analytic on all of \(V\). The real analytic identity principle extends its zero value to \(V\). For completeness, the set where an analytic function and all its derivatives vanish is closed by continuity and open by its convergent Taylor series; starting from a nonempty open zero set, connectedness makes it all of \(V\).

If \(d_k<0\), (87) already includes \(\alpha=0\), so \(E_k=0\) on \(V\). If \(d_k\ge0\), all ordinary partial derivatives of order \(d_k+1\) vanish there, since \(D=-i\partial\). A Taylor expansion on a ball in \(V\) consequently truncates at degree \(d_k\). It gives a polynomial \(Q_k\) on that ball. The same analytic identity principle gives
\[
E_k|_V=Q_k|_V,\qquad \deg Q_k\le d_k.
\tag{88}
\]
The sets \(W_F\) and \(C\) are cones. For each positive \(\lambda\), the path \(s\mapsto((1-s)+s\lambda)x\) stays in their complement, so \(\lambda V=V\). Homogeneity gives \(Q_k(\lambda x)=\lambda^{d_k}Q_k(x)\) on this open set, hence as a polynomial identity. Differentiating in \(\lambda\) at one shows \((\sum x_j\partial_j-d_k)Q_k=0\); comparison of monomials removes every degree other than \(d_k\). Thus \(Q_k\) is homogeneous of degree \(mk-n\), or is the zero polynomial. When that degree is negative, only the zero case is meant.

We have proved the full component-wide polynomial conclusion from the existence of a bounding cycle at one point, without assuming component constancy of null homology.

### The lower order expansion has a global exponential bound

Let \(P\) be any hyperbolic polynomial with principal part \(F\), and put
\[
R=F-P,\qquad \deg R\le m-1.
\tag{89}
\]
the causal inverse input supplies the distributionally convergent causal expansion
\[
E_P=\sum_{j=0}^{\infty}R(D)^j E_{j+1}.
\tag{90}
\]
We now prove normal convergence of the corresponding polynomial series on all of \(\mathbb C^n\), not merely convergence on \(V\).

Fix a single \(x_*\in V\), an allowed field, and a sufficiently small deformation parameter for the cycles \(\alpha_+\) in the oriented contour section. They are fixed compact cycles, independent of \(k\), on which
\[
|F(\zeta)|\ge c>0,\qquad
\max_\ell|\zeta_\ell|\le M.
\tag{91}
\]
Apply (79) with \(q=0\) to \(F^k\) and \(|\alpha|=d_k\ge0\). The cycle coefficient, sign factor, and pulled-back Kronecker form have a finite total variation independent of \(k,\alpha\). Also
\(|\zeta^\alpha|\le\max(1,M)^{mk}\).
It follows that some \(A,B\ge1\), depending only on these fixed cycles and \(F\), satisfy
\[
|D^\alpha Q_k|\le A B^k
\qquad(|\alpha|=mk-n\ge0).
\tag{92}
\]
These highest derivatives are constants, so their value at \(x_*\) bounds them everywhere. Absolute values of \(D^\alpha Q_k\) and \(\partial^\alpha Q_k\) agree. Negative-degree \(Q_k=0\) need no estimate.

Write \(R(\xi)=\sum_\beta r_\beta\xi^\beta\) and let \(K=\sum_\beta|r_\beta|\). The sum of the absolute values of the coefficients of \(R^j\) is at most \(K^j\), by the finite convolution formula for polynomial multiplication. Set
\[
T_j(z)=R(D)^jQ_{j+1}(z)
=\sum_\alpha c_{j,\alpha}\frac{z^\alpha}{\alpha!}.
\tag{93}
\]
Because \(Q_{j+1}\) is homogeneous, the coefficient \(c_{j,\alpha}=\partial^\alpha T_j(0)\) contains only terms for which
\(|\alpha|+|\beta|=m(j+1)-n\).
Every derivative of \(R^j\) has order \(0\le|\beta|\le j(m-1)\). Therefore a nonzero coefficient requires
\[
m+j-n\le|\alpha|\le m(j+1)-n,
\qquad
|c_{j,\alpha}|\le A B^{j+1}K^j.
\tag{94}
\]
The powers of \(-i\) from \(D^\beta\) have modulus one. If \(K=0\), all terms with \(j\ge1\) vanish, and the same bound is interpreted with \(K^0=1\).

Put \(C_2=\max(1,BK)\) and \(C=AB\). For a fixed \(a=|\alpha|\), the possible indices in (94) are finite:
\[
\max\!\left(0,\left\lceil\frac{a+n}{m}\right\rceil-1\right)
\le j\le a+n-m.
\tag{95}
\]
An empty interval contributes zero. There are at most \(a+n+1\) indices, and each satisfies \(j\le a+n\). Hence
\[
\sum_j|c_{j,\alpha}|
\le C C_2^{a+n}(a+n+1)
\le A_1 A_0^a,
\quad
A_1=C C_2^n(n+1),\quad A_0=2C_2.
\tag{96}
\]
The last step uses \(a+n+1\le(n+1)(a+1)\) and \(a+1\le2^a\) for integers \(a\ge0\). Thus
\[
\begin{split}
\sum_{j,\alpha}|c_{j,\alpha}|\frac{|z^\alpha|}{\alpha!}
&\le A_1\sum_{\alpha\in\mathbb N^n}
\frac{A_0^{|\alpha|}|z^\alpha|}{\alpha!}\\
&=A_1\exp\!\left(A_0\sum_{\ell=1}^n|z_\ell|\right).
\end{split}
\tag{97}
\]
On a compact complex set the same majorant, with its coordinate radii, is finite. Its tails prove normal convergence, including legitimate interchange of the two sums. The resulting function
\[
U_P(z)=\sum_{j=0}^{\infty}T_j(z)
\tag{98}
\]
is entire and satisfies the exponential-type bound in (97), or the Euclidean bound \(A_1e^{A_0\sqrt n\,|z|}\). Cauchy estimates on slightly larger compact sets give locally uniform convergence of every differentiated series. On \(V\), its partial sums are precisely the restrictions of those in (90). Their distributional limit is both \(U_P|_V\) and \(E_P|_V\). Therefore
\[
E_P|_V=U_P|_V.
\tag{99}
\]

For any positive integer \(\ell\), \(P^\ell\) is hyperbolic with principal part \(F^\ell\). The causal inverse of every principal power \((F^\ell)^k=F^{\ell k}\) is one of the polynomials already obtained in (88). Applying the same proof with degree \(m\ell\) proves that the causal inverse of \(P(D)^\ell\) also agrees on \(V\) with an entire function of exponential type. The constants can depend on \(\ell\); no uniform bound over all powers is asserted.

There is a useful weaker premise. For the entire-function conclusion, it suffices that every \(E_k|_V\) already agree with a homogeneous polynomial of degree \(mk-n\). The cycle null-homology condition is needed only to obtain those polynomials. Estimate (92) then follows from the already proved cycle formula, so (89)–(99) apply unchanged. This retains the full relaxed premise, rather than treating null homology as necessary for analyticity.

For \(n=1\), orient the positive normal by \(N=1\). Write \(F(\xi)=a\xi^m\). Its causal power kernels on \(V=(0,\infty)\) are
\[
E_k(t)=a^{-k}i^{mk}\frac{t^{mk-1}}{(mk-1)!}.
\tag{100}
\]
They are homogeneous polynomials there and their top derivative has modulus \(|a|^{-k}\). The coefficient proof above consequently applies directly. It requires no negative-dimensional equatorial cycle.

### An even-dimensional wave cone has a polynomial lacuna

Let the total space-time dimension be \(n=2a\ge2\), and let
\[
F(\tau,\eta)=\tau^2-|\eta|^2,\qquad N=(1,0,\ldots,0).
\tag{101}
\]
The characteristic tangent polar is a positive null ray, as computed in Exercise 4. Its union \(W_F\) is the future null-cone boundary, including the origin. The interior
\(V=\{(t,y):t>|y|\}\)
is therefore a component of the complement of \(W_F\cup(-C)\).

At \(x_0=e_1\), an allowed real analytic degree-zero field is
\[
\Theta(\tau,\eta)=
\left(0,-\frac{\tau\eta}{\tau^2+|\eta|^2}\right).
\tag{102}
\]
It is even and orthogonal to \(x_0\). At a characteristic point,
\(H_\xi(v)=2(\tau v_t-\eta\cdot v_y)\);
membership in the component containing \(N\) is the inequality
\(H_\xi(v)/H_\xi(N)>0\).
For (102) that quotient is \(|\eta|^2/|\xi|^2>0\). At noncharacteristic points the tangent cone is all of \(\mathbb R^n\), so no constraint is lost where the field is zero.

On the equator \(\tau=0\), the field vanishes. Thus \(K^-\) is the real unit sphere in the complex spatial hyperplane, with the equatorial boundary orientation, and \(F=-\sum\zeta_j^2=-1\) there. Consider the cylinder
\[
A:[0,\pi]\times K^-\longrightarrow M_{x_0},
\qquad A(s,y)=e^{is}y.
\tag{103}
\]
It remains in \(M_{x_0}\), since \(F(e^{is}y)=-e^{2is}\ne0\). The antipodal map on the oriented sphere \(S^{n-2}\) has degree \((-1)^{n-1}=-1\). Use an antipodally invariant triangulation, for example a radial projection of the boundary triangulation of the cross-polytope, so that the endpoint fundamental chains have that same orientation relation. Its cylinder boundary is therefore
\(\partial A=-K^--K^-=-2K^-\).
Consequently \(-A/2\) is a real or complex bounding chain for \(K^-\). This proves the real-coefficient condition at \(x_0\), including the oriented \(S^0\) case \(n=2\). It proves that twice the cycle is integrally null homologous; it does not assert that the single cycle has zero integral homology class.

Equations (86)–(88) now prove that every causal wave power \(E_k|_V\) is a homogeneous polynomial of degree \(2k-n\), and is zero for \(k<a\). In particular the wave kernel itself vanishes in the future interior for even total dimension \(n\ge4\). In total dimension two it has degree zero and is a nonzero constant there, with the \(D=-i\partial\) normalization \(-1/2\). A polynomial lacuna need not be a region of zero kernel. Every hyperbolic \(P\) with this wave principal part, and every positive power of \(P\), has the entire exponential-type continuation on \(V\) proved above.

As a check on the dimensions and signs, causal uniqueness makes each \(E_k\) invariant under proper, time-orientation-preserving Lorentz transformations: \(F\), \(\delta_0\), and the future support cone are all preserved. Spatial rotations and the elementary boost with velocity \(|y|/t<1\) take each point of \(V\) to \((\sqrt{t^2-|y|^2},0)\). Analyticity and homogeneity therefore give
\(E_k=A_k(t^2-|y|^2)^{k-a}\)
inside \(V\). Direct differentiation, with \(s=t^2-|y|^2\), gives
\[
\Box s^p=4p(p+a-1)s^{p-1},
\qquad
-4(k-a)(k-1)A_k=A_{k-1}\quad(k\ge2).
\tag{104}
\]
Here \(F(D)=-\Box\), which accounts for the minus sign. The zero polynomials for \(k<a\) and the nonnegative integer powers for \(k\ge a\) agree with this recurrence. The argument uses total dimension \(n\), not spatial dimension \(n-1\), in its parity statement.

## Original exercises with complete solutions

**Exercise1 (intermediate: a full tangent model with complex lower terms).** In two frequency variables put \(F(\tau,\eta)=(\tau^2-\eta^2)^2\), \(N=(1,0)\), and
\[
P(\tau,\eta)=F(\tau,\eta)
+a\tau(\tau^2-\eta^2)
+b\tau^2+c\tau\eta+d\eta^2+e\tau+f\eta+g,
\tag{27}
\]
where all seven coefficients are complex. Find the tangent degree, principal tangent polynomial and full localization at \(\zeta=(1,1)\), and explain why discarding every lower order term would be incorrect.

**Solution.** Put \(A(\tau,\eta)=\tau^2-\eta^2\). Its first derivatives and nonzero second derivatives give \(S_A(\xi)\ge c(1+|\xi|)\); hence \(\tau\prec A\). Product comparison gives \(S_{A^2}\) comparable to \(S_A^2\), so \(a\tau A\prec A^2\), and every quadratic or smaller polynomial is weaker than \(A^2\). The eight-criteria theorem of the hyperbolicity lesson therefore makes \(P\) hyperbolic in \(N\). With \(h=(h_\tau,h_\eta)\),
\[
(\tau^2-\eta^2)\bigm|_{(\tau,\eta)=\zeta+\varepsilon h}
=2\varepsilon(h_\tau-h_\eta)
+\varepsilon^2(h_\tau^2-h_\eta^2).
\]
Thus \(\mu=2\) and \(H_\zeta(h)=4(h_\tau-h_\eta)^2\). Directly in (6), the squared principal term tends to \(4(h_\tau-h_\eta)^2\), the cubic to \(2a(h_\tau-h_\eta)\), and the quadratic to \(b+c+d\). The linear and constant terms tend to zero. Therefore
\[
L_\zeta(h)
=4(h_\tau-h_\eta)^2
+2a(h_\tau-h_\eta)+(b+c+d).
\tag{28}
\]
Its hyperbolicity cone in direction \(N\) is \(h_\tau-h_\eta>0\); the principal square has two components and this is the one containing \(N\). Its polar is the ray
\[
C_\zeta=\{s(1,-1):s\ge0\}.
\tag{29}
\]
Formula (28) exhibits both a surviving first-order term and a surviving constant term. The wavefront extraction is applied to \(L_\zeta/S_{L_\zeta}(0)\), not merely to the principal square. The cone theorem still uses its principal part.

**Exercise2 (introductory: a noncharacteristic frequency).** Suppose \(F(\zeta)\ne0\). Compute \(L_\zeta\), its normalized localization, and the inverse obtained in the lower wavefront-cone section. What does this force in \(\operatorname{WF}(E)\)?

**Solution.** Here \(\mu=0\), and only \(j=m,\alpha=0\) occurs in (5). Thus \(L_\zeta=F(\zeta)\ne0\), \(Q_\zeta=F(\zeta)/|F(\zeta)|\), since the derivative-vector norm of a constant is its modulus. Its unique inverse is \(G_\zeta=|F(\zeta)|F(\zeta)^{-1}\delta_0\). Dividing by \(S_{L_\zeta}(0)=|F(\zeta)|\) gives \(E_\zeta=F(\zeta)^{-1}\delta_0\). Its support is the origin; (10) forces \((0,\zeta)\in\operatorname{WF}(E)\). The tangent polar is \(\{0\}\), so the lower cone assertion remains meaningful at degree zero.

**Exercise3 (intermediate: why the fixed extra normal shift is needed).** Explain why the factor \(|q|^\mu\) in (22) alone does not prove (14) when \(\mu>0\). Show explicitly how (24) resolves this for \(q=0\), without allowing an unbounded extra perturbation.

**Solution.** At \(q=0\), (22) gives only a zero lower bound. With \(\tau<\tau_0-1\),
\[
\xi+i\tau N
=\xi+i(\tau+1)N+i(-N).
\]
The vector \(-N\) lies in \(-\Gamma_1\), has fixed nonzero length, and the modified normal parameter is below \(\tau_0\). For large \(|\xi|\), its fixed length and the extra \(1\) satisfy the same bounds in (22), provided the original size constants have been reduced first. Hence the denominator is bounded below by \(c_1|N|^\mu|\xi|^{m-\mu}\). This is uniformly positive for \(|\xi|\ge1\), since \(m\ge\mu\). For general \(q\) in the negative cone, (23) replaces \(|N|\) by a single uniform positive distance.

**Exercise4 (advanced: an exact wavefront fiber for the wave operator).** Let \(n=d+1\ge2\), \(F(\tau,\eta)=\tau^2-|\eta|^2\), \(N=(1,0)\), and let \(E_F\) be the positive-time causal inverse. Use the tangent-polynomial section–the analytic upper-cone section and homogeneity to determine both its ordinary and analytic wavefront sets, including every noncharacteristic frequency at the origin. Explain why this argument does not assert that every general tangent polar is itself a wavefront fiber.

**Solution.** If \(F(\zeta)\ne0\), the tangent degree is zero and the upper bound restricts its fiber to the origin; the lower wavefront-cone section includes that origin. If \(\zeta=(\tau,\eta)\ne0\) is characteristic, then \(\tau\ne0\) and
\[
H_\zeta(h)=2\tau h_\tau-2\eta\cdot h_\eta.
\]
Its component containing \(N\) is
\(\{h:\operatorname{sgn}(\tau)(\tau h_\tau-\eta\cdot h_\eta)>0\}\). The polar is
\[
C_\zeta=
\{s(|\tau|,-\operatorname{sgn}(\tau)\eta):s\ge0\}.
\tag{45}
\]
Thus both wavefront fibers lie in this positive-time null ray, and the lower wavefront-cone section says that the closed convex cone generated by the ordinary fiber contains the whole ray. This forces at least one nonzero point on it: a subset of \(\{0\}\) generates no nonzero vector.

The causal inverse of the homogeneous polynomial has degree \(2-n\), by the causal inverse input and uniqueness. Its ordinary wavefront fiber is invariant under every positive dilation of the base point. To check this directly in the Fourier definition, dilate a cutoff centered at \(x\) to one centered at \(\lambda x\). Changing variables in its distributional Fourier pairing multiplies the transform by a fixed scalar and replaces frequency by \(\lambda\) or \(\lambda^{-1}\) times frequency. Conic rapid decay is unchanged. Homogeneity identifies the two localized distributions up to that nonzero scalar, so exclusion at one point is equivalent to exclusion at its positive dilation. Since the fiber has a nonzero point on (45), it contains every positive point on that ray. the lower wavefront-cone section also includes zero.

The ordinary fiber therefore equals \(C_\zeta\); inclusion of the ordinary wavefront set in the analytic one and the analytic upper-cone section's analytic upper bound show equality for the analytic fiber too. Consequently
\[
\begin{split}
\operatorname{WF}(E_F)=\operatorname{WF}_A(E_F)
={}&\{(0,\zeta):\zeta\ne0\}\\
&{}\cup
\{(s(|\tau|,-\operatorname{sgn}(\tau)\eta),(\tau,\eta)):
s>0,\ \tau^2=|\eta|^2,\ (\tau,\eta)\ne0\}.
\end{split}
\tag{46}
\]
The proof uses a one-dimensional tangent polar and base-point dilation invariance. A general closed convex cone can be generated by a proper subset of itself, and a full polynomial with lower terms need not give homogeneous base-point fibers. Thus the general conclusion in the lower wavefront-cone section is kept at its stated strength.

**Exercise 5 (intermediate: the contour phase in one dimension).** Take \(F(\xi)=a\xi^m\), \(a\ne0\), \(N=1\), \(x>0\), and \(0\le\alpha<m\). Verify (79) using the outward-oriented two-point sphere \(S^0\). Include the weights of both points, the factor \(\omega(\zeta)=\zeta\), and the fact that the two cycles in (78) coincide.

**Solution.** Every nonzero real frequency is noncharacteristic, so \(\Theta=0\) is allowed. The outward endpoint weights are \(+1\) at \(1\) and \(-1\) at \(-1\). Put \(q=m-1-\alpha\). At \(\zeta=1\) the integrand, including its orientation weight, is \(i^qx^q/a\). At \(\zeta=-1\) its sign relative to that value is
\((-1)^{q+\alpha-m+3}=1\):
one minus comes from the sign function, one from \(\omega\), and one from the endpoint orientation. Thus one sphere contributes \(2i^qx^q/a\). Since \((-1)^{n-1}=1\) when \(n=1\), the cycle \(\alpha_+\) is twice that sphere. Multiplication by \(i/(4q!)\) gives
\[
D^\alpha E_F(x)=a^{-1}i^{m-\alpha}\frac{x^{m-1-\alpha}}{(m-1-\alpha)!},
\tag{105}
\]
which is the direct derivative of the causal kernel in the oriented contour section. Dropping any one of the three negative-point signs would spoil this check.

**Exercise 6 (basic: a lower order term produces a whole exponential).** In dimension one let \(P(\xi)=\xi-b\), \(b\in\mathbb C\), with normal \(N=1\). Evaluate the principal-power expansion (90) on \(t>0\), identify its entire continuation, and verify \(P(D)E_P=\delta_0\).

**Solution.** Here \(F(\xi)=\xi\), \(R=b\), and (100) gives \(E_{j+1}(t)=i^{j+1}t^j/j!\) on \(t>0\). Therefore
\[
U_P(z)=\sum_{j=0}^{\infty}b^j i^{j+1}\frac{z^j}{j!}
=i e^{ibz},\qquad |U_P(z)|\le e^{|b||z|}.
\tag{106}
\]
The causal distribution is \(E_P=iH(t)e^{ibt}\). Since
\(\partial_t(H e^{ibt})=\delta_0+ibH e^{ibt}\),
application of \(-i\partial_t-b\) gives \(\delta_0\); the two terms containing \(b\) cancel. Causal uniqueness identifies it with the fundamental solution. The exponential need not be a polynomial, even though all the principal power kernels are polynomials on the positive half-line.

**Exercise 7 (intermediate: which expansion terms can contribute?).** In (93) take \(m=3\), \(n=4\), and a coefficient with \(|\alpha|=2\). Determine every possible index \(j\), and explain why the coefficient estimate uses a finite geometric sum even though (90) has infinitely many terms.

**Solution.** Formula (95) gives
\(\max(0,\lceil(2+4)/3\rceil-1)=1\)
as the lower limit, and \(2+4-3=3\) as the upper limit. Only \(j=1,2,3\) can contribute. Indeed \(Q_{j+1}\) has degree \(3j-1\), and \(R^j\) has differential order at most \(2j\), so its resulting monomial degrees lie between \(j-1\) and \(3j-1\). Degree two is in this interval exactly for these indices. A particular polynomial \(R\) can make some of those coefficients zero; the estimate permits every term the order bound allows. The contribution is at most \(C(C_2+C_2^2+C_2^3)\). More generally, each fixed multiindex has a finite interval (95), whose length and largest power grow at most linearly in \(|\alpha|\). Estimate (96) absorbs that finite geometric sum into an exponential in \(|\alpha|\); division by \(\alpha!\) then produces the entire-function majorant (97).

**Exercise 8 (advanced: the two-dimensional wave kernel and the factor two in homology).** For \(F(\tau,\eta)=\tau^2-\eta^2\), verify the constant value of the causal kernel inside the future cone. Explain exactly what the rotation cylinder (103) proves about integral and real homology.

**Solution.** Put \(u=t+y\), \(v=t-y\). Then \(\Box=4\partial_u\partial_v\) and
\(\delta_0(u)\delta_0(v)=\tfrac12\delta_0(t,y)\), since the coordinate Jacobian has absolute value two. Consequently
\[
E_F(t,y)=-\tfrac12 H(u)H(v),\qquad
F(D)E_F=-\Box E_F=\delta_0(t,y).
\tag{107}
\]
Its support is the closed future cone, so causal uniqueness applies. On its interior the value is \(-1/2\), which is a degree-zero polynomial and is nonzero. The equator is an oriented \(S^0\), a difference of two points; the antipodal map reverses this fundamental cycle. Hence the cylinder has integral boundary \(-2K^-\). It proves integral null homology of \(2K^-\). Multiplying the chain by \(-1/2\) proves real or complex null homology of \(K^-\), but is not an integral chain. Neither vanishing kernel derivatives nor the zero values of all relevant periods justify deleting that distinction.


## References

[A] Michael Atiyah, Raoul Bott and Lars Gårding, *Lacunas for hyperbolic differential operators with constant coefficients, I*, Acta Mathematica **124** (1970), 109–189. [Primary article](https://www.its.caltech.edu/~matilde/HypPDEAtiyahBottGarding.pdf).

[B] Michael Atiyah, Raoul Bott and Lars Gårding, *Lacunas for hyperbolic differential operators with constant coefficients, II*, Acta Mathematica **131** (1973), 145–206. [Primary article](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6156-11511_2006_Article_BF02392039.pdf).

These works credit the classical contour and lacuna methods. The complete authored receiving arguments above use the stated exact internal results and retain the explicitly planned general analytic prerequisites. Original prose and solved exercises are CC0-1.0; the linked historical works retain their own rights and are not reproduced.
