# Causal kernels, initial data, and short-time geometry

**AN-03 · Unit AN03-U021 · Independent Self-checked by the writing AI.**

A wave kernel has two useful descriptions. In frequency space it solves an ordinary differential equation with prescribed initial data. In physical space its singularities sit on a cone. The frequency description fixes constants and initial traces; the cone description explains which parts of a local geometric construction can influence a short time interval. We develop both descriptions before introducing variable coefficients.

The spatial dimension is any integer \(n\geq1\). The variable-coefficient construction also permits complex matrix lower-order coefficients, without diagonalizing them. Its principal symbol must be a positive scalar quadratic form times the identity. A general system with several characteristic speeds is a different problem.

## AN03-WHK-001 — Conventions and the causal distribution problem

For spatial Fourier transformation use
\[
 \widehat f(\xi)=\int_{\mathbb R^n}e^{-ix\cdot\xi}f(x)\,dx,
 \qquad f(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}\widehat f(\xi)\,d\xi.
 \tag{W1}
\]
The same convention applies in time. Set
\[
 L=\partial_t^2-\Delta_x,\qquad
 C_+=\{(t,x):t\geq |x|\},\qquad q(t,x)=t^2-|x|^2.
 \tag{W2}
\]
Distributions supported in \(C_+\) will be called causal. Reflection means
\(\widetilde T(t,x)=T(-t,-x)\); for the radial kernels below it equals \(T(-t,x)\).

Our entry contracts are explicit. **AN03-BASE-WHK-FOURIER** consists of the Fourier inversion and distribution extension conventions in AN03-DEP-001 and AN03-DEP-002, elementary integration of absolutely integrable functions, the gamma integral and beta identity, holomorphic differentiation under a dominated integral, and the identity theorem. It also includes Cauchy's residue theorem, with contour orientation and winding numbers, for finite-pole meromorphic integrands on contours avoiding their poles, and Cauchy's theorem for deforming contours through regions where the integrand is holomorphic. Vanishing of the added contour pieces must be justified in each application; WHK-005 does this after testing and Gaussian regularization. The beta and gamma normalizations used here are displayed in the proof. **AN03-BASE-WHK-DISTRIBUTIONS** consists of distributional derivatives, multiplication by smooth functions, changes of variables by diffeomorphisms, compact-support distribution estimates, and the wavefront pullback theorem for a submersion with its converse in product coordinates. For wavefront sets we additionally use the exact constant-coefficient microlocal ellipticity implication
\[
 P(D)u\in C^\infty\quad\Longrightarrow\quad
 WF(u)\subset\{(z,\zeta):p_m(\zeta)=0\},
 \tag{W3}
\]
where \(p_m\) is the principal symbol, and the parameter theorem that absence of covectors normal to the parameter fibers gives smooth distribution-valued dependence. These are other-volume prerequisites; no propagation theorem or global wave existence theorem is presumed.

**AN03-DEP-WHK-GEOMETRY** is precisely the normal-coordinate and transport construction in AN03-EHP-004, AN03-EHP-005 and AN03-EHP-006 of *Building a local inverse from radial singularities*. It supplies the jointly smooth exponential chart, its transformed drift, the radial metric identity, and the ordered matrix transport solution. The interface is stated again in WHK-009. All estimates for the causal distributions themselves are proved below.

When a time distribution is viewed as a function of a spatial parameter, continuity into distributions of order at most \(m\geq0\) means the following local statement: it acts on compactly supported \(C^m\) tests, the pairings are continuous in the parameter, and on compact parameter sets they obey a common \(C^m\)-seminorm bound. This weak finite-order continuity does not assert operator-norm continuity on the dual of \(C^m\).

## AN03-WHK-002 — A Laplace calculation that constructs the whole family

There is an entire distribution family \(\lambda\mapsto R_\lambda\), supported in \(C_+\), whose Fourier–Laplace transform is
\[
 \int e^{-st-ix\cdot\xi}R_\lambda(t,x)\,dt\,dx
       =(s^2+|\xi|^2)^{-\lambda},\qquad s>0.
 \tag{W4}
\]
The integral denotes distributional pairing, equivalently the Fourier transform of the exponentially damped distribution. The power is determined by continuation from positive \(s\) and \(\xi=0\). The family satisfies
\[
 LR_{\lambda+1}=R_\lambda,\qquad R_0=\delta_{(0,0)},\qquad
 R_\lambda(at,ax)=a^{2\lambda-n-1}R_\lambda(t,x)\quad(a>0).
 \tag{W5}
\]

**Proof.** We first justify the gamma normalization for complex parameters. For \(\operatorname{Re}z>0\), let \(\Gamma(z)=\int_0^\infty e^{-u}u^{z-1}\,du\), using the real logarithm for positive \(u\). For an integer \(N\geq1\), repeated integration by parts in the beta integral gives
\[
 B(z,N+1)=\int_0^1 t^{z-1}(1-t)^N\,dt
 =\frac{N!}{z(z+1)\cdots(z+N)},\qquad
 N^zB(z,N+1)\longrightarrow\Gamma(z).
 \tag{W4a}
\]
For the rational identity, one integration replaces the integral by \(N/z\) times the integral with parameters \(z+1,N\); the final integral is \(1/(z+N)\). No gamma division is used. For the limit put \(u=Nt\). On a compact subset of the right half-plane choose \(0<\sigma\leq\operatorname{Re}z\leq M\). The resulting integrands are bounded in absolute value by \((u^{\sigma-1}+u^{M-1})e^{-u}\), since \((1-u/N)^N\leq e^{-u}\) for \(0<u<N\). Pointwise convergence is uniform for \(z\) in that compact set, and the integrable bound makes the integral convergence locally uniform.

Define \(H_N=\sum_{k=1}^N k^{-1}\). The numbers \(H_N-\log N\) decrease and are bounded below: the decrease follows from \(\log(1+1/N)>1/(N+1)\), and comparison with the integral of \(1/t\) gives the lower bound. Write their limit as \(\gamma\). The exact reciprocal of the scaled beta expression in (W4a) is the entire finite product
\[
 P_N(z)=zN^{-z}\prod_{k=1}^N(1+z/k)
 =z\exp\bigl(z(H_N-\log N)\bigr)
       \prod_{k=1}^N(1+z/k)e^{-z/k}.
 \tag{W4b}
\]
Its limit exists locally uniformly on the whole plane. Indeed, on \(|z|\leq R\) choose an integer \(K>2R\). For \(k>K\), use the logarithm defined by its power series at one; then
\[
 \log(1+z/k)-z/k
 =\sum_{j=2}^{\infty}\frac{(-1)^{j+1}}{j}(z/k)^j,
 \qquad
 \bigl|\log(1+z/k)-z/k\bigr|\leq 2R^2/k^2.
 \tag{W4c}
\]
Thus the sum of these tail logarithms converges uniformly on this disk. The derivative of each tail logarithm is \(-z/[k(k+z)]\), uniformly \(O_R(k^{-2})\); uniform convergence of this derivative series also proves that the tail sum is holomorphic. Exponentiating it, and retaining the first \(K\) factors as polynomials times exponentials, proves local uniform convergence to an entire function
\[
 G(z)=z e^{\gamma z}\prod_{k=1}^{\infty}(1+z/k)e^{-z/k}.
 \tag{W4d}
\]
The exponential of the tail sum never vanishes. Consequently the finite initial factors show that the only zeros are \(0,-1,-2,\ldots\), each simple: near any of these points precisely one polynomial factor has a simple zero and all the others are nonzero. This argument uses logarithms only for the tail factors close to one, including when the disk contains zeros of the full product.

For \(\operatorname{Re}z>0\), the product of \(P_N(z)\) and \(N^zB(z,N+1)\) is exactly one. Passing to the two locally uniform limits gives \(G(z)\Gamma(z)=1\); in particular the gamma integral has no zero there. This identifies \(G\) as the entire reciprocal of the meromorphic continuation of gamma, with the constant fixed by the original integral, rather than only up to a nonzero factor. Explicitly \(P_N(1)=(N+1)/N\), so \(G(1)=1\). Integration by parts in the gamma integral gives \(\Gamma(z+1)=z\Gamma(z)\) in the right half-plane. It follows that \(G(z)=zG(z+1)\) there, hence everywhere by the identity theorem. Iterating at \(z=-m\), for an integer \(m\geq0\), gives
\[
 G'(-m)=(-1)^m m!,\qquad
 \operatorname*{Res}_{z=-m}\Gamma(z)=\frac{(-1)^m}{m!}.
 \tag{W4e}
\]
For this derivative, differentiate \(G(z)=z(z+1)\cdots(z+m)G(z+m+1)\) at \(-m\) and use \(G(1)=1\); its reciprocal has the stated residue. These facts justify both complex gamma normalizations below and the pole cancellation in WHK-003.

Initially suppose \(\operatorname{Re}\lambda>\max(0,(n-1)/2)\). The locally integrable function
\[
 R_\lambda(t,x)=
 \frac{2^{1-2\lambda}\pi^{(1-n)/2}}
 {\Gamma(\lambda)\Gamma(\lambda+(1-n)/2)}
 \boldsymbol1_{\{t>|x|\}}q(t,x)^{\lambda-(n+1)/2}
 \tag{W6}
\]
has locally integrable cone boundary because the exponent is greater than \(-1\). At the vertex, radial integration in \(x\) gives a power \(t^{2\operatorname{Re}\lambda-1}\), which is integrable by the other inequality. On compact subsets of this half-plane the same estimates hold after inserting any fixed power of \(|\log q|\). Thus (W6) is holomorphic as a distribution there.

At \(\xi=0\), put \(x=ty\). The elementary ball integral, obtained by polar coordinates and \(u=|y|^2\), is
\[
 \int_{|y|<1}(1-|y|^2)^{\lambda-(n+1)/2}\,dy
 =\pi^{n/2}\frac{\Gamma(\lambda+(1-n)/2)}{\Gamma(\lambda+1/2)}.
 \tag{W7}
\]
For \(n=1\) the two half-intervals give the same formula. The time integral is
\(\int_0^\infty e^{-st}t^{2\lambda-1}dt=\Gamma(2\lambda)s^{-2\lambda}\).
Their product with the constant in (W6) is \(s^{-2\lambda}\), because
\[
 \Gamma(2\lambda)=2^{2\lambda-1}\pi^{-1/2}
                  \Gamma(\lambda)\Gamma(\lambda+1/2).
 \tag{W8}
\]
One can obtain (W8), in the region needed here, by evaluating the product of two one-dimensional gamma integrals after the polar substitution in a Gaussian integral; holomorphic continuation gives the displayed identity throughout its domain.

To retain the spatial frequency, first replace \(-i\xi\) by a real vector \(\eta\) with \(|\eta|<s\). The integral with weight \(e^{-st+\eta\cdot x}\) is absolutely convergent. Rotate \(\eta\) onto the first spatial axis, and in the \((t,x_1)\)-plane make a real linear change preserving \(t^2-x_1^2\), the future cone, and determinant one. Explicitly its coefficients are \(\cosh\theta=s/(s^2-|\eta|^2)^{1/2}\) and \(\sinh\theta=|\eta|/(s^2-|\eta|^2)^{1/2}\). It transforms the linear form \(st-\eta\cdot x\) into \((s^2-|\eta|^2)^{1/2}t\). The preceding evaluation is therefore
\((s^2-\eta\cdot\eta)^{-\lambda}\). Both sides are holomorphic for complex \(\eta\) with \(|\operatorname{Re}\eta|<s\). Successive one-variable identity theorems extend their equality from a real neighborhood to that tube. Taking \(\eta=-i\xi\) proves (W4) in the initial range.

For larger real part, ordinary distributional differentiation, including the boundary where the function and the necessary traces vanish, gives
\[
 Lq^b=2b(2b+n-1)q^{b-1}.
 \tag{W9}
\]
Indeed \(\partial_tq=2t\), \(\partial_{x_j}q=-2x_j\), \(Lq=2(n+1)\), and the difference of the squared gradients is \(4q\). The gamma functional equation makes the constants in (W6) satisfy \(LR_{\lambda+1}=R_\lambda\). The identity then holds throughout the initial half-plane by holomorphic continuation. For arbitrary \(\lambda\), choose an integer \(j\geq0\) so that \(\lambda+j\) is in that half-plane and define
\[
                       R_\lambda=L^jR_{\lambda+j}.
 \tag{W10}
\]
The recursion shows that different choices give the same result. This constructs an entire family, since it constructs it holomorphically on successively larger half-planes. Its support remains in \(C_+\). Its members are tempered: (W6) has polynomial growth, and (W10) applies only finitely many derivatives. On the cone, exponential damping makes their transforms meaningful; differentiation proves (W4) for (W10). Fourier injectivity then proves \(R_0=\delta\). Homogeneity follows by scaling (W6), then applying (W10); the degree decreases by two at each application of \(L\). This also checks the vertex in (W5), not merely points with positive time.

For every integer \(\nu\geq0\), define
\[
                              E_\nu=\nu!R_{\nu+1}.
 \tag{W11}
\]
If \(\sigma>0\), (W4), with the time frequency on the line \(\tau\in\mathbb R-i\sigma\), gives the contour formula
\[
 E_\nu(t,x)=\frac{\nu!}{(2\pi)^{n+1}}
 \int_{\operatorname{Im}\tau=-\sigma}\int_{\mathbb R^n}
 \frac{e^{i(x\cdot\xi+t\tau)}}{(|\xi|^2-\tau^2)^{\nu+1}}
 \,d\xi\,d\tau.
 \tag{W12}
\]
The right side is a distributional inverse Fourier–Laplace transform. It is not an absolutely convergent integral at arbitrary dimension. For fixed \(\sigma\), the denominator is nowhere zero on the real integration variables and its inverse and derivatives have polynomial growth, so the inverse transform exists. Formula (W4) identifies it with (W11) for every \(\sigma>0\), proving independence of the contour height. In particular the support is the full causal cone condition \(t\geq|x|\), including its vertex, rather than merely \(t\geq0\).

## AN03-WHK-003 — Cone formulas and exact recursion

Let \(\chi_+^a(s)=s_+^a/\Gamma(a+1)\) for \(\operatorname{Re}a>-1\). Its entire continuation is determined by
\[
 \partial_s\chi_+^{a+1}=\chi_+^a,\qquad
 \chi_+^0=\boldsymbol1_{\{s>0\}},\qquad \chi_+^{-1}=\delta_0.
 \tag{W13}
\]
The entire reciprocal gamma function and its simple zeros were proved in WHK-002. For completeness, integrate the initial definition against a compactly supported smooth test after subtracting its Taylor polynomial at zero. The remainder is \(O(s^M)\), so its integral continues to \(\operatorname{Re}a>-M-1\); the removed monomials give simple fractions in \(a\), whose poles are canceled by \(1/\Gamma(a+1)\). Increasing \(M\) gives the entire family. Integration by parts proves the first identity initially, hence everywhere. This construction also gives \(\chi_+^{-j-1}=\delta^{(j)}\) for \(j\geq0\).

Write
\[
 A_\nu=2^{-2\nu-1}\pi^{(1-n)/2},\qquad
 a_\nu=\nu+(1-n)/2.
 \tag{W14}
\]
On the open set \(t>0\),
\[
                         E_\nu(t,x)=A_\nu\chi_+^{a_\nu}(q(t,x)).
 \tag{W15}
\]
At nonzero points of \(q=0\), the map \(q\) is a submersion, so this is a legitimate distributional pullback. At the vertex (W15) is interpreted by the construction of WHK-002, not by substituting into a singular one-dimensional distribution at a critical point. To prove (W15), use (W6) in its initial range, restrict to \(t>0\), and apply the compatible differential continuations (W10) and (W13). The chain-rule calculation in (W9), now in normalized form, reads
\[
 L\chi_+^a(q)=(4a+2n-2)\chi_+^{a-1}(q)
 \quad\text{away from the vertex}.
 \tag{W16}
\]
There is no claim that (W16) discards the vertex term in the fundamental solution. That term was fixed separately by (W5).

The global recursions, including every vertex contribution, are
\[
 LE_0=\delta_{(0,0)},\qquad LE_\nu=\nu E_{\nu-1}\quad(\nu\geq1),
 \qquad -2\partial_{x_j}E_\nu=x_jE_{\nu-1}\quad(\nu\geq1).
 \tag{W17}
\]
The first two follow from (W5). For the last, apply spatial Fourier–Laplace transformation. Multiplication by \(x_j\) becomes \(i\partial_{\xi_j}\), and
\[
 i\partial_{\xi_j}\bigl((\nu-1)!(|\xi|^2-\tau^2)^{-\nu}\bigr)
       =-2i\xi_j\nu!(|\xi|^2-\tau^2)^{-\nu-1}.
 \tag{W18}
\]
The identity follows by injectivity; it therefore has no possible omitted distribution supported at the origin. The degree of homogeneity of \(E_\nu\) is \(2\nu+1-n\).

## AN03-WHK-004 — Initial traces from a Volterra problem

Each \(E_\nu\), restricted to nonnegative time, is a one-sided \(C^\infty\) function of \(t\) with values in \(\mathcal D'(\mathbb R^n)\). Its initial traces are
\[
 \partial_t^jE_\nu(0+,\cdot)=0\quad(0\leq j\leq2\nu),\qquad
 \partial_t^{2\nu+1}E_\nu(0+,\cdot)=\nu!\delta_0.
 \tag{W19}
\]
These are traces of the one-sided function. Repeatedly differentiating its extension by zero to negative time can also produce distributions at \(t=0\).

**Proof.** Put \(\omega=|\xi|\), and define
\[
 S_\omega(t)=\begin{cases}\sin(t\omega)/\omega,&\omega\ne0,\\t,&\omega=0.\end{cases}
 \tag{W20}
\]
For \(t\geq0\), its Volterra convolution with a function \(f\) is
\((S_\omega*f)(t)=\int_0^tS_\omega(t-s)f(s)\,ds\).
Differentiating twice proves
\((\partial_t^2+\omega^2)(S_\omega*f)=f\), with zero initial value and derivative. Its Laplace transform is \((s^2+\omega^2)^{-1}\). Hence (W4) implies
\[
 \widehat E_\nu(t,\xi)=h_\nu(t,\omega),\qquad
 h_\nu=\nu!\underbrace{S_\omega*\cdots*S_\omega}_{\nu+1\text{ factors}}
 \quad(t\geq0).
 \tag{W21}
\]
All interchanges here can first be made after multiplying the spatial transform by a Schwartz cutoff; the bounds below then permit its removal.

There is a useful version on a fixed simplex. For \(\nu\geq1\), integrate over \(u_i\geq0\), \(\sum_{i=1}^{\nu}u_i\leq1\), and put \(u_{\nu+1}=1-\sum_{i=1}^{\nu}u_i\). With the evident single factor interpretation for \(\nu=0\),
\[
 h_\nu(t,\omega)=\nu!t^{2\nu+1}
 \int_{\Sigma_\nu}\prod_{i=1}^{\nu+1}
       u_i\,\frac{\sin(t\omega u_i)}{t\omega u_i}\,du_1\cdots du_\nu.
 \tag{W22}
\]
This follows by changing the \(\nu\) time variables in the convolution to \(tu_i\). The removable quotients have value one at zero. Their derivatives in real \(t\) obey polynomial bounds in \(\omega\) on bounded time intervals; for example \(\sin z/z=\int_0^1\cos(sz)ds\). Thus each \(\partial_t^jh_\nu\) has a bound \(C_{j,T}(1+\omega)^j\) times a fixed polynomial in \(T\). Every compactly supported smooth spatial test has a rapidly decreasing Fourier transform, so inversion and dominated differentiation yield all one-sided distributional derivatives. Uniformity over bounded sets of tests follows from their common Fourier decay seminorms, giving the strong distribution topology as well.

At zero, the simplex integral is
\[
                       \int_{\Sigma_\nu}\prod_i u_i\,du
                                  =\frac1{(2\nu+1)!}.
 \tag{W23}
\]
One proves this by successively applying \(\int_0^1v^{p-1}(1-v)^{q-1}dv=\Gamma(p)\Gamma(q)/\Gamma(p+q)\), beginning with parameters all equal to two. Therefore the first nonzero Taylor term in (W22) is \(\nu!t^{2\nu+1}/(2\nu+1)!\). Its inverse spatial Fourier transform is exactly (W19). The same expression extends to an odd smooth distribution-valued function on all real \(t\), namely
\[
                              W_\nu=E_\nu-\widetilde E_\nu.
 \tag{W24}
\]
The distinction between this odd extension and the causal extension will be essential when time distributions are restricted at a spatial point.

## AN03-WHK-005 — The cosine kernel and its spectral measure

The derivative of the odd fundamental kernel satisfies
\[
 \mathcal F_x(\partial_tW_0)(t,\xi)=\cos(t|\xi|).
 \tag{W25}
\]
Define the flat spectral cutoff kernel for \(\lambda\in\mathbb R\) by
\[
 e(x,\lambda^2)=(2\pi)^{-n}\int_{|\xi|<|\lambda|}e^{ix\cdot\xi}\,d\xi.
 \tag{W26}
\]
Let \(d_\lambda e(x,\lambda^2)\) mean its distributional differential in \(\lambda\), not differentiation with respect to \(\lambda^2\). The measure-valued tempered distribution
\[
                         d\mu_x(\lambda)=\tfrac12
                    \operatorname{sgn}\lambda\,d_\lambda e(x,\lambda^2)
 \tag{W27}
\]
satisfies
\[
                  \partial_tW_0(t,x)=\int_{\mathbb R}e^{it\lambda}\,d\mu_x(\lambda).
 \tag{W28}
\]
Here the transform of the measure has no additional \((2\pi)^{-1}\) factor. In the normalized inverse-transform convention, its time Fourier transform is \(2\pi\mu_x\).

**Proof.** Differentiating (W20) proves (W25). For a fixed \(\omega>0\),
\[
 d_\lambda\boldsymbol1_{\{|\lambda|>\omega\}}
              =\delta_\omega-\delta_{-\omega}.
 \tag{W29}
\]
Multiplication by \(\tfrac12\operatorname{sgn}\lambda\) makes this
\(\tfrac12(\delta_\omega+\delta_{-\omega})\). Its transform in (W28) is \(\cos(t\omega)\). The set \(\xi=0\) has Lebesgue measure zero since \(n\geq1\), and alternatively the two-point measures converge to \(\delta_0\) as \(\omega\downarrow0\). Pairing with Schwartz tests justifies integration in \(\xi\) and proves (W28) with the stated constants.

The contour prescription can also be checked without an interchange of unregularized oscillatory integrals. Insert \(e^{-\varepsilon|\xi|^2}\), \(\varepsilon>0\), in (W12) for \(\nu=0\). For fixed \(\xi\), inverse transformation of \((\omega^2-\tau^2)^{-1}\) on a line below the poles gives \(\boldsymbol1_{t>0}S_\omega(t)\). For \(t>0\), closing upward, the residues of
\(i\tau e^{it\tau}/(\omega^2-\tau^2)\) at \(\tau=\omega,-\omega\) are \(-ie^{it\omega}/2\) and \(-ie^{-it\omega}/2\). Multiplication by \(2\pi i\), then by \((2\pi)^{-1}\), gives \(\cos(t\omega)\). For \(t<0\), closing downward contains no poles and gives zero. At \(\omega=0\), the limiting residue gives the same value. One may justify the closures first with a compact time test supported away from zero; its transform decays on the closing contour after integration by parts. The initial value \(S_\omega(0)=0\) then shows that differentiating its causal extension adds no Dirac term.

Subtract the reflected causal kernel. Its derivative is now the cosine for either sign of time. The Gaussian makes the remaining spatial integral absolutely convergent, and it also gives the version of (W27) with \(e^{-\varepsilon\lambda^2}\). Finally \(e^{-\varepsilon|\xi|^2}\to1\) on Schwartz tests with all required dominated seminorm bounds. Thus the regularized distributions converge, proving the contour and spectral computations agree. This argument records both the time-contour signs and the role of the Gaussian; neither is hidden in a formal residue integral.

## AN03-WHK-006 — Testing at the spatial center with finite regularity

Put \(a=a_\nu=\nu-(n-1)/2\) and \(c_{\nu,n}=A_\nu\), as in (W14). For nonzero \(x\), the odd kernel is \(c_{\nu,n}\operatorname{sgn}(t)\chi_+^a(t^2-|x|^2)\). This expression uses a submersion near its nonzero cone points; its value at \(x=0\) requires the construction that follows. The finite-order topology is the weak topology on compactly supported \(C^m\) tests specified in WHK-001.

For an even function \(\phi\in C_c^{j+2}(\mathbb R)\), define
\[
 (T\phi)(t)=\frac{\phi'(t)}{2t}\quad(t\ne0),\qquad
 (T\phi)(0)=\frac{\phi''(0)}2.
 \tag{OE3}
\]
This defines an even \(C^j\) function with support contained in the support of \(\phi\). To see both regularity and the quantitative bound, use \(\phi'(0)=0\) and write
\[
 (T\phi)^{(j)}(t)
   =\frac12\int_0^1 s^j\phi^{(j+2)}(st)\,ds,
 \qquad
 \|(T\phi)^{(j)}\|_\infty
   \leq\frac{\|\phi^{(j+2)}\|_\infty}{2(j+1)}.
 \tag{OE4}
\]
Differentiation under this integral is allowed for the displayed regularity, and it also proves the formula at zero. Away from the support, the original quotient vanishes. Iteration therefore gives a continuous operation from even \(C_c^{2k}\) functions to \(C_c^0\), and
\[
 \|T^k\phi\|_\infty
     \leq\frac{k!}{(2k)!}\|\phi^{(2k)}\|_\infty,
 \qquad
 (T^k\phi)(0)=\frac{k!}{(2k)!}\phi^{(2k)}(0).
 \tag{OE5}
\]
The norm bound follows by applying (OE4) with derivative indices \(0,2,\ldots,2k-2\). The value at zero follows from the Taylor polynomial of the even function through degree \(2k\), because \(T(t^{2j})=j t^{2j-2}\). For \(k=0\), both formulas mean the identity operation.

**Positive measures and finite-order distributions.**

Fix \(\delta\geq0\). For \(b>0\), define the even positive measure \(e_{\delta,b}\) by
\[
 \langle e_{\delta,b},\phi\rangle
   =\frac1{\Gamma(b)}\int_0^\infty
       s^{b-1}\bigl[\phi(\sqrt{s+\delta})+
                         \phi(-\sqrt{s+\delta})\bigr] \,ds.
 \tag{OE6}
\]
At \(b=0\), use
\[
 e_{\delta,0}=\delta_{\sqrt\delta}+\delta_{-\sqrt\delta};
 \quad e_{0,0}=2\delta_0.
 \tag{OE7}
\]
Thus (OE6) agrees, when it is an ordinary function, with
\(2|t|\chi_+^{b-1}(t^2-\delta)\). For tests supported in \([-R,R]\), the mass bounds are
\[
 |\langle e_{\delta,b},\phi\rangle|
 \leq M_{b,R}\|\phi\|_\infty,
 \quad
 M_{b,R}=
 \begin{cases}
 2,&b=0,\\
 2R^{2b}/\Gamma(b+1),&b>0.
 \end{cases}
 \tag{OE8}
\]
They hold for every \(\delta\geq0\); if \(\delta>R^2\), the pairing vanishes. For a fixed continuous test, (OE6) varies continuously with \(\delta\): its integrand converges pointwise, and a constant times \(s^{b-1}\) on \([0,R^2]\) dominates it. Formula (OE7) proves the same assertion for \(b=0\). In particular these are weakly continuous measures even at \(\delta=0\).

For even smooth tests, integration by parts in \(s\) gives
\[
 \langle e_{\delta,b},\phi\rangle
       =-\langle e_{\delta,b+1},T\phi\rangle,
       \qquad b\geq0.
 \tag{OE9}
\]
For \(b>0\), differentiate \(s^b/\Gamma(b+1)\) and use
\(d\phi(\sqrt{s+\delta})/ds=(T\phi)(\sqrt{s+\delta})\).
The boundary at zero vanishes. For \(b=0\), the boundary term is precisely the two evaluations in (OE7). This argument includes \(\delta=0\), because (OE3) supplies the continuous derivative of the even function of \(\sqrt s\).

Now let \(a\) be any real number, choose \(k\in\mathbb N_0\) with \(a+k\geq0\), and set \(\phi_{\mathrm e}(t)=(\phi(t)+\phi(-t))/2\). Define
\[
 \langle e_{\delta,a},\phi\rangle
       =(-1)^k\langle e_{\delta,a+k},T^k\phi_{\mathrm e}\rangle.
 \tag{OE10}
\]
Applying (OE9) once proves that increasing \(k\) does not change this definition. The definition kills odd tests. It agrees for \(\delta>0\) with the distribution
\(2|t|\chi_+^{a-1}(t^2-\delta)\), by the same integration by parts on each side of the two nonzero roots, or equivalently by the differential recurrence for \(\chi_+^a\). At \(\delta=0\), (OE10), rather than an undefined pullback, specifies its extension.

Equations (OE5), (OE8) and (OE10) imply
\[
 |\langle e_{\delta,a},\phi\rangle|
   \leq M_{a+k,R}\frac{k!}{(2k)!}
                    \|\phi^{(2k)}\|_\infty.
 \tag{OE11}
\]
For \(k=0\), the last norm is \(\|\phi\|_\infty\). The estimate is valid on every fixed compact test support and is uniform in \(\delta\geq0\). Since \(T^k\phi_{\mathrm e}\) is continuous for \(\phi\in C_c^{2k}\), weak measure continuity of the base family proves continuity of the pairing in (OE10) for every \(C_c^{2k}\) test. It also proves joint continuity when \(\delta_j\to\delta\) and \(\phi_j\to\phi\) in \(C^{2k}\) on one compact support: use (OE11) for the changing test and pointwise continuity for the fixed test. This establishes the finite-order topology directly, including equality in \(a+k\geq0\).

No norm continuity is hidden here. For \(\delta>0\), the measure
\(\delta_{\sqrt\delta}+\delta_{-\sqrt\delta}-2\delta_0\) has total variation \(4\) on an interval containing all three points. Nevertheless its pairing with every continuous test tends to zero as \(\delta\downarrow0\).

The same formulas yield smooth dependence on \(x\) with values in ordinary distributions, without asserting a fixed finite order for all parameter derivatives. For smooth even tests, differentiate (OE6) in \(\delta\); the derivative of the test is \(T\phi\), and all derivatives are dominated on a fixed bounded \(s\) interval. Equations (OE9)–(OE10) then give, including one-sided derivatives at zero,
\[
 \partial_\delta^j\langle e_{\delta,a},\phi\rangle
       =(-1)^j\langle e_{\delta,a-j},\phi\rangle.
 \tag{OE12}
\]
The same conclusion for the base \(b=0\) follows from the smoothness of \(\phi(\sqrt\delta)\) for even smooth \(\phi\), whose successive derivatives are \((T^j\phi)(\sqrt\delta)\). Composing with \(\delta=|x|^2\) gives smooth functions of \(x\): differentiation produces polynomials in \(x\) multiplying the continuous one-sided derivatives in (OE12), and induction extends every such derivative through \(x=0\). Each parameter derivative has an estimate of the form (OE11), at an order that may increase with the derivative. This is the requisite distribution-valued smoothness.

**The odd primitive retains the order.**

For \(x\ne0\), differentiation of the cone expression (W15) and its odd reflection gives
\[
 \partial_tW_\nu(t,x)=c_{\nu,n}e_{|x|^2,a}(t).
 \tag{OE13}
\]
To recover an odd primitive while keeping its finite order, let
\(\phi_{\mathrm o}(t)=(\phi(t)-\phi(-t))/2\), and set
\[
 (J\phi)(t)=\int_{-\infty}^t\phi_{\mathrm o}(s)\,ds.
 \tag{OE14}
\]
The total integral of an odd compactly supported function is zero, so \(J\phi\) is compactly supported. It is even, and its support lies in \([-R,R]\) if that of \(\phi\) does. Moreover,
\[
 \|J\phi\|_\infty\leq2R\|\phi\|_\infty,
 \qquad
 \|(J\phi)^{(j)}\|_\infty\leq
              \|\phi^{(j-1)}\|_\infty\quad(j\geq1).
 \tag{OE15}
\]
For an even distribution \(h\), define its odd primitive by
\[
 \langle Ah,\phi\rangle=-\langle h,J\phi\rangle.
 \tag{OE16}
\]
It is odd because \(J\) kills even tests. Further,
\(J(\phi')=\phi_{\mathrm e}\), which gives
\(\langle\partial_tAh,\phi\rangle=\langle h,\phi\rangle\).
An odd primitive is unique: a distribution with derivative zero is constant, and a constant distribution is even. For completeness, the first fact follows by writing any integral-zero test as the derivative of its compactly supported primitive; a distribution killing all such tests depends only on their integral.

Define \(W_\nu(\cdot,x)=A(c_{\nu,n}e_{|x|^2,a})\) also at \(x=0\). For \(x\ne0\), uniqueness identifies it with the odd reflection of (W15). Estimate (OE15) proves that \(A\) preserves every nonnegative finite order; it is not necessary to differentiate the test one extra time. It also preserves the weak continuity just proved. Consequently,
\[
 x\longmapsto W_\nu(\cdot,x),\quad
 x\longmapsto\partial_tW_\nu(\cdot,x)
 \quad\hbox{are continuous in order at most }2k
 \tag{OE17}
\]
for every
\[
 k\in\mathbb N_0,\qquad k\geq\frac{n-1}{2}-\nu.
 \tag{OE18}
\]
This includes the threshold whenever the right side is a nonnegative integer. Equations (OE12) and (OE16) also give their smooth dependence on \(x\) with values in ordinary distributions. The restriction at \(x=0\) is obtained by this continuity. It agrees with the restriction of the full spacetime odd kernel; one may either use its already established distribution-valued smoothness or the wavefront criterion proved below.

## AN03-WHK-007 — The exact endpoint and the meaning of the integer parameter

Suppose \(a=-k\) with \(k\in\mathbb N_0\). Equations (OE7), (OE10) and (OE5) give, for every smooth test,
\[
 \langle e_{0,-k},\phi\rangle
   =2(-1)^k(T^k\phi_{\mathrm e})(0)
   =\frac{2(-1)^kk!}{(2k)!}\phi^{(2k)}(0).
\]
The derivative order is even, so the sign in the action of \(\delta^{(2k)}\) is positive. Hence
\[
 e_{0,-k}=\frac{2(-1)^kk!}{(2k)!}\delta^{(2k)},
 \qquad
 \partial_tW_\nu(t,0)
 =2^{2k-n+1}\pi^{(1-n)/2}
       \frac{(-1)^kk!}{(2k)!}\delta^{(2k)}(t).
 \tag{OE19}
\]
In the last equality we used \(2\nu=n-1-2k\). For \(k=0\), this states that the derivative is \(2c_{\nu,n}\delta_0\), with odd primitive \(c_{\nu,n}\operatorname{sgn}(t)\). For \(k\geq1\), replace \(\delta^{(2k)}\) by \(\delta^{(2k-1)}\) in the second formula to obtain \(W_\nu(t,0)\).

The endpoint order \(2k\) for the derivative is exact when \(k>0\). Indeed, a nonzero multiple of \(\delta^{(2k)}\) cannot have order at most \(2k-1\): choose a compactly supported smooth \(\psi\) with \(\psi^{(2k)}(0)\ne0\), and test against \(\epsilon^{2k-1}\psi(t/\epsilon)\). Derivatives through order \(2k-1\) stay bounded, while the pairing grows like \(\epsilon^{-1}\). The case \(k=0\) is a nonzero measure.

**Positive exponents and the domain of the order notation.**

The assertion (OE18) uses a nonnegative distribution order. No negative-order notation is needed to describe the case \(a>0\); (OE17) then holds already with \(k=0\). One can also state its classical regularity directly. At any nonzero cone point, a smooth local coordinate is \(q\), and the factors \(\operatorname{sgn}(t)\) and \(|t|\) are smooth and nonzero there.

If \(a=j\) is a positive integer, \(W_\nu\) is locally \(C^{j-1}\) but not \(C^j\) across that cone, because the \(j\)-th derivative of \(q_+^j\) jumps. Its time derivative is locally \(C^{j-2}\) but not \(C^{j-1}\) for \(j\geq2\); for \(j=1\) it has a jump. If \(a=m+1/2\), \(m\in\mathbb N_0\), then \(W_\nu\) is locally \(C^m\) but not \(C^{m+1}\). Its derivative is locally \(C^{m-1}\) but not \(C^m\) for \(m\geq1\); for \(m=0\) the derivative is locally integrable and unbounded on the cone. These failures follow by differentiating the one-sided powers in the transverse coordinate. Since \(\partial_tq=2t\ne0\), the time derivative has the asserted nonzero leading coefficient.

The fixed-\(x=0\) profiles can be smoother than the profiles through a nonzero cone point. For \(a>0\), the continuous extension constructed above is
\[
 W_\nu(t,0)=\frac{c_{\nu,n}}{\Gamma(a+1)}
                      \operatorname{sgn}(t)|t|^{2a},
 \qquad
 \partial_tW_\nu(t,0)=\frac{2c_{\nu,n}}{\Gamma(a)}|t|^{2a-1}.
 \tag{OE23}
\]
There is no point mass in this derivative because the first expression is continuous at zero. When \(a=j\) is a positive integer, these profiles have respectively exact classical regularity \(C^{2j-1}\) and \(C^{2j-2}\). When \(a=m+1/2\), both profiles are polynomials in \(t\) and hence smooth. Thus an invented identification of a negative distribution-order index with a positive differentiability index would produce false conclusions at nonzero cone points, and sometimes already at the vertex.

The finite-order notation used in Hörmander's volume I, §2.1, bounds derivatives through a nonnegative integer order. Lemma 17.4.2 of volume III says that \(k\) is an integer satisfying the inequality, without restating this domain. In that notation the precise domain is (OE18); it does not define negative distribution orders. Its factorial endpoint formula likewise applies when \(k\) is nonnegative. For instance, \(n=1,\nu=1\) would give \(k=-1\) from the bare equality, although neither \((-1)!\) nor a derivative of order \(-2\) occurs in that formula. Here the actual profiles are \(W_1(t,0)=t|t|/8\) and \(\partial_tW_1(t,0)=|t|/4\). The direct formulas (OE23) cover this case. This domain reconciliation preserves every finite-order assertion with defined notation; it does not insert a positive-regularity meaning for a negative index.

## AN03-WHK-008 — Every wavefront covector, including those over the vertex

For this paragraph the exact prerequisite interface consists of coordinate invariance of the wavefront set, the wavefront formula for the product of a one-variable distribution with a smooth constant factor, and microlocal elliptic regularity for differential operators. The latter says that \(\operatorname{WF}(u)\) outside the characteristic set of \(L\) is contained in \(\operatorname{WF}(Lu)\).

The one-dimensional distribution \(\chi_+^a\) is smooth away from zero and has both nonzero cotangent directions at zero in its wavefront set. Here is why there is no exceptional \(a\) in the present half-integer family. It is a nonzero homogeneous distribution supported on the nonnegative half-line. If it were smooth at zero, it would be flat there because it vanishes on the negative side; homogeneity would then force it to vanish, a contradiction. Thus zero is singular. The distribution is real, so the Fourier transform of a real cutoff of it has equal magnitude in opposite directions. In one dimension both directions must therefore occur.

At a nonzero cone point, \(dq=2(t,-x)\ne0\). Taking \(q\) as one local coordinate and the remaining variables as transverse coordinates reduces the odd reflection of (W15) to a nonvanishing smooth factor times \(\chi_+^a(q)\). The product and coordinate rules give exactly the nonzero multiples of \(dq\); there are no tangential covectors. Away from the cone the kernel is smooth. At such nonzero cone points, the result is equivalently
\[
 t^2=|x|^2,\qquad \tau^2=|\xi|^2,\qquad
                  \tau x+t\xi=0.
 \tag{OE20}
\]
For example, the equivalence follows from \(t\ne0\) and \(\xi=-(\tau/t)x\).

At the vertex, the retarded recursion and time reflection imply
\[
 (\partial_t^2-\Delta_x)^{\nu+1}W_\nu=0.
 \tag{OE21}
\]
The two point-source terms have the same coefficient \(\nu!\) and cancel. The principal symbol in (OE21) vanishes exactly when \(\tau^2=|\xi|^2\). Microlocal elliptic regularity excludes every other nonzero covector at the vertex. Conversely, fix any nonzero null covector \((\tau,\xi)\). At the cone points
\((t_s,x_s)=s(\tau,-\xi)\), \(s>0\), this same covector is a nonzero multiple of \(dq(t_s,x_s)\). It belongs to the wavefront set at every such point. Closure of the wavefront set as \(s\downarrow0\) therefore puts it in the wavefront set at the vertex. We obtain the equality
\[
 \operatorname{WF}(W_\nu)=
 \{(t,x;\tau,\xi):
   (\tau,\xi)\ne0,\ t^2=|x|^2,
   \tau^2=|\xi|^2,\ \tau x+t\xi=0\}.
 \tag{OE22}
\]
There is no covector in this set with \(\tau=0\). In particular the standard pullback criterion permits restriction to each fixed \(x\), including zero. The direct calculation (OE10)–(OE17) supplies both the value of that restriction and its stronger finite-test-regularity control.

## AN03-WHK-009 — The precise geometric and matrix interface

Let \(X\subset\mathbb R^n\) be open. The operator acts on column vectors in \(\mathbb C^r\), for any fixed finite \(r\), and has the form
\[
 P=-\partial_j(g^{jk}(x)\partial_k)I_r+b^j(x)\partial_j+c(x).
 \tag{WG1}
\]
Repeated spatial indices are summed. The real symmetric matrix \(G=(g^{jk})\) is smooth and positive definite at every point; \(b^j,c\) are arbitrary smooth complex matrices. All uniform estimates below concern specified compact subsets. Uniform ellipticity on an unbounded \(X\), self-adjointness, positivity of \(c\), and commutation of the lower-order matrices are not hypotheses. Put \(H=G^{-1}\), and let \(s(x,y)\) denote Riemannian distance for \(H\) where the points are in the small normal neighborhood used below.

Here is the full interface needed from AN03-EHP-004–006. The unnormalized exponential chart \(x=\gamma(v,y)\) is jointly smooth near \(v=0\), has \(\gamma(0,y)=y\) and \(d_v\gamma(0,y)=I\), and is a diffeomorphism jointly with the retained center \(y\). If tildes denote the coefficients in this chart and \(J=|\det d_v\gamma|\), then
\[
\begin{split}
 \widetilde G(v,y)H(y)v&=v,\qquad
 s(\gamma(v,y),y)^2=v^tH(y)v,\\
 \widetilde b^{\,i}(v,y)&=(d_v\gamma)^{-1}_{ij}b^j(\gamma(v,y))
       -\widetilde g^{ik}\partial_k\log J\,I_r.
\end{split}
 \tag{WG2}
\]
Thus the transformed operator is again in divergence form with the drift shown in (WG2). In particular it is not obtained by merely substituting \(x=\gamma(v,y)\) into \(b\). Set
\[
 \mathcal E=v\cdot\partial_v,\qquad
 h(v,y)=\widetilde b^{\,j}(v,y)(H(y)v)_j.
 \tag{WG3}
\]
The matrix \(h\) is smooth and vanishes at \(v=0\). There is a unique smooth invertible \(S(v,y)\) with \(2\mathcal ES=hS\), \(S(0,y)=I_r\). Its defining ordered series is the solution of
\[
 Y'(a)=\frac{h(av,y)}{2a}Y(a),\qquad Y(0)=I_r,
 \qquad S(v,y)=Y(1).
 \tag{WG4}
\]
The quotient extends smoothly to \(a=0\). The ordinary exponential of its integral is not asserted to solve this equation when the coefficients do not commute. The following recursion fixes all amplitudes:
\[
\begin{split} u_0&=S,\\ u_\nu(v,y)&=-S(v,y)\int_0^1 a^{\nu-1}S(av,y)^{-1}(\widetilde P u_{\nu-1})(av,y)\,da, \qquad \nu\geq1,\\ (\nu I_r-h/2)u_\nu+\mathcal Eu_\nu&=-\widetilde Pu_{\nu-1}. \end{split} \tag{WG5} \] The integral is convergent with all parameter derivatives; \(a^{\nu-1}\) is integrable. The normalization at the center and the order of matrix multiplication are part of this interface. The cited unit proves the normal-chart statements from the geodesic equation and the matrix statement by a factorially convergent iterated-integral series.

We give a distributional meaning to the shorthand \(E_\nu(t,s(x,y))\) before using it. Write \(T(y)=H(y)^{1/2}\), the smooth positive square root, and \(w=T(y)v\). The map
\[
 (t,v,y)\longmapsto(t,w,y)
 \tag{WG6}
\]
is a smooth diffeomorphism on its domain. Pull back the distribution \(E_\nu(t,w)\), tensor the smooth constant in \(y\), and then use the inverse normal chart. This defines the shorthand jointly, including \(t=0,x=y\). It never calls for a pullback of a one-dimensional singular distribution by the nonsmooth distance function at its diagonal. The same construction applies to the entire family \(R_\lambda\).

## AN03-WHK-010 — Finite cancellation as an identity of distributions

In normal coordinates fix \(y\), set \(G_0=G(y)\), and put
\[
 \mathscr L_0=\partial_t^2-g_0^{jk}\partial_{v_j}\partial_{v_k},
 \qquad F_\nu(t,v)=E_\nu(t,T(y)v).
 \tag{WG7}
\]
Linear change of variables in (W17) gives
\[
\begin{split}
 \mathscr L_0F_0&=\sqrt{\det G_0}\,\delta_{(0,0)},\\
 \mathscr L_0F_\nu&=\nu F_{\nu-1},\qquad
 \nabla_vF_\nu=-\tfrac12H(y)v F_{\nu-1}\quad(\nu\geq1).
\end{split}
 \tag{WG8}
\]
The determinant is the inverse of \(\det T(y)\); time is unchanged by this linear map.

The scalar divergence part of the variable-coefficient operator has exactly the same action on these radial distributions as its frozen value. More precisely,
\[
 (\widetilde G-G_0)\nabla_vR_\lambda(t,T(y)v)=0,
 \qquad
 \partial_{v_j}(\widetilde g^{jk}\partial_{v_k}F_\nu)
       =g_0^{jk}\partial_{v_j}\partial_{v_k}F_\nu.
 \tag{WG9}
\]
To prove the first identity, begin with \(\operatorname{Re}\lambda\) large enough that the cone formula is continuously differentiable. Its gradient is a scalar multiple of \(H(y)v\). Equation (WG2) implies \((\widetilde G-G_0)H(y)v=0\), including the sign that comes from \(t^2-v^tHv\). Thus the product vanishes as an ordinary function and hence as a distribution. Pairing with a fixed compactly supported test makes both sides entire in \(\lambda\), by WHK-002 and the smooth pullback (WG6). The identity theorem gives the first formula for every \(\lambda\). Taking its distributional divergence and specializing proves the second. This argument retains every distribution at the cone vertex; it uses no local integrability assertion for a high-dimensional fundamental kernel.

For a smooth matrix \(u(v)\) and \(\nu\geq1\), expand the differential product and apply (WG8)–(WG9):
\[
\begin{split}
 (\partial_t^2+\widetilde P)(uF_\nu)
  &=u\mathscr L_0F_\nu+(\widetilde Pu)F_\nu
       -2\widetilde g^{jk}(\partial_ju)(\partial_kF_\nu)
       +(\widetilde b^{\,j}u)\partial_jF_\nu\\
  &=(\widetilde Pu)F_\nu+
       (\nu u+\mathcal Eu-hu/2)F_{\nu-1}.
\end{split}
 \tag{WG10}
\]
The coefficient in the last product of the first line is \(\widetilde b^{\,j}u\), with that order. This is why the last coefficient of the second line is \(hu\).

For \(\nu=0\) there is no kernel \(F_{-1}\). The cross terms for \(u_0=S\) vanish nonetheless, including at the vertex. In the differentiable range of \(R_\lambda\), write its cone expression as a function \(f(t^2-v^tHv)\). Its gradient is \(-2Hv f'\). The sum of the two cross terms in the first line of (WG10) is consequently
\[
                     (4\mathcal Eu_0-2hu_0)f'=0.
 \tag{WG11}
\]
This identity continues to every \(\lambda\) as an identity between smooth coefficients times distributional first derivatives, just as in (WG9). There is no undefined product with a separate critical-point pullback \(f'\) in this continuation. At \(\lambda=1\) we obtain
\[
 (\partial_t^2+\widetilde P)(u_0F_0)
   =\sqrt{\det G_0}\,\delta_{(0,0)}I_r
                           +(\widetilde Pu_0)F_0.
 \tag{WG12}
\]
Here multiplication of the point mass uses \(u_0(0)=I_r\). Substituting the recursion (WG5) into (WG10) cancels adjacent terms. Therefore for every integer \(N\geq0\),
\[
 (\partial_t^2+\widetilde P)\sum_{\nu=0}^Nu_\nu F_\nu
   =\sqrt{\det G(y)}\,\delta_{(0,0)}I_r
                             +(\widetilde Pu_N)F_N.
 \tag{WG13}
\]
This is a finite, exact distribution identity; no convergence of an infinite formal series is involved.

## AN03-WHK-011 — The strict regularity bound and the causal extension

The error in (WG13) belongs to \(C^k\) for every nonnegative integer \(k\) satisfying
\[
                            k<N-\frac{n-1}{2}.
 \tag{WG14}
\]
The assertion includes regularity through the cone vertex and across \(t=0\). It remains true jointly with a smooth center parameter on compact sets.

**Proof.** Set \(a=N-(n-1)/2\). Under (WG14), \(a>k\geq0\), and the causal kernel is the ordinary function
\[
 F_N(t,v)=\frac{A_N}{\Gamma(a+1)}
             \boldsymbol1_{\{t>0\}}(t^2-v^tH(y)v)_+^a.
 \tag{WG15}
\]
At a nonzero cone point, \(q=t^2-v^tHv\) is a smooth transverse coordinate. The one-variable function \(q_+^a\) is \(C^k\) when \(k<a\): differentiating \(j\leq k\) times gives a constant times \(q_+^{a-j}\), which tends to zero at the boundary. On a compact annulus centered at \((t,v)=0\), every derivative of total order \(j\leq k\) is consequently bounded and continuous. Homogeneity rescales that bound to
\[
 |\partial_{t,v}^{\alpha}F_N(t,v)|
       \leq C_\alpha (|t|+|v|)^{2a-|\alpha|},
       \qquad |\alpha|\leq k.
 \tag{WG16}
\]
The estimate is meant for small nonzero \((t,v)\), with the derivatives extended continuously across the nonzero cone. All the powers on the right are positive. Inductively extend these derivatives by zero at the origin. To check that they are the derivatives there, an order-\(j\) candidate has increment \(O(|(t,v)|^{2a-j})=o(|(t,v)|)\) when \(j<k\), since \(2a-j>1\). Its derivative at zero is thus zero. This proves the induction and \(C^k\) regularity. The case \(k=0\) follows directly from the positive zeroth power. For a compact center set, \(H(y)^{1/2}\) and its derivatives are bounded and invertible with uniform bounds. Composition with (WG6) and then with the smooth normal chart preserves joint \(C^k\) regularity, including all mixed derivatives. Multiplication by the smooth matrix \(\widetilde Pu_N\) gives the error claim.

The strict inequality cannot be replaced uniformly by an equality. At a nonzero cone point with positive integer \(a=k\), the \(k\)-th transverse derivative of \(q_+^k\) jumps. For nonintegral \(a\), the first derivative above \(a\) is unbounded. A particular amplitude \(\widetilde Pu_N\) may vanish on the cone and improve this error, but the construction makes no such general assumption. If no nonnegative integer satisfies (WG14), the identity (WG13) is still valid as a distribution identity.

Choose \(c>0\) so that the closed metric ball \(r=(v^tHv)^{1/2}\leq c\) lies strictly inside the normal chart. Extend the amplitudes smoothly to a larger spatial domain. On \(t<c\), the kernel \(F_\nu\) is zero wherever \(r\geq c\), and in fact near each point of that set within the open time interval \(t<c\). Indeed \(t< c\leq r\) is a strict failure of causal support. Hence the extension has no effect on the product, on any of its distributional derivatives, or on (WG13). Cutoffs whose derivatives lie outside that ball cause no error on \(t<c\). The endpoint \(t=c\) is deliberately absent from this conclusion.

At time zero the notation in (WG13) is interpreted by the one-sided distribution-valued traces proved in WHK-004 and the smooth coordinate changes. For example the finite sum has initial value zero and first time derivative \(\sqrt{\det G(y)}\delta_0I_r\); higher-index terms have zero first trace. The delta term in the full spacetime identity is consistent with these data, since the second derivative of the causal extension of a one-sided smooth function with initial value zero contributes its first trace times \(\delta(t)\).

## AN03-WHK-012 — A common short time for a compact set of centers

Let \(Y\Subset X\) be open. There are \(c>0\) and smooth amplitudes \(U_\nu\in C^\infty(X\times Y;\operatorname{Mat}_r(\mathbb C))\), \(\nu\geq0\), such that on \((-\infty,c)\times X\times Y\),
\[
\begin{split}
 (\partial_t^2+P_x)\sum_{\nu=0}^N
           U_\nu(x,y)E_\nu(t,s(x,y))
   &=\sqrt{\det G(y)}\,\delta(t)\delta_y(x)I_r\\
   &\quad +(P_xU_N)(x,y)E_N(t,s(x,y)).
\end{split}
 \tag{WG17}
\]
Near the diagonal \(U_\nu(\gamma(v,y),y)=u_\nu(v,y)\); in particular \(U_0(y,y)=I_r\). The error has the joint regularity (WG14). The expression involving \(s\) uses the local distribution construction (WG6) and zero extension in the causally irrelevant region, so it does not require smooth global distance across a cut locus.

**Proof.** The compact set \(\overline Y\) lies in \(X\). On a compact coordinate neighborhood of it, the eigenvalues of \(H\) have a positive lower and finite upper bound. The parameter inverse function theorem and the geodesic construction of EHP-004 give a common normal radius over finitely many center neighborhoods covering \(\overline Y\). Shrinking that radius retains a normal chart over an open set of centers containing \(\overline Y\). A path that leaves this coordinate neighborhood costs a fixed positive length: until its first exit its metric speed is bounded below by a fixed constant times its Euclidean speed, and its endpoints have a fixed positive Euclidean separation. Thus a sufficiently small common metric radius excludes every such path. The radial minimizing identity in (WG2) now agrees with the actual metric distance on that common ball, even if \(X\) is not complete.

Choose \(c\) smaller than this radius, leaving a larger radius between \(c\) and the boundary of the common chart. A smooth cutoff equal to one on the smaller tube and supported in the larger one is obtained by applying a fixed smooth cutoff to the jointly smooth squared distance there. Multiply the transported amplitudes by it and extend by zero to \(X\times Y\). The products are smooth because the cutoff support lies inside the chart. On \(s<c\) these amplitudes equal the transported ones. For \(s\geq c\), all local kernel factors vanish near every point with \(t<c\), as proved in WHK-011. The finite identity (WG13) therefore persists after extension.

The change \(x=\gamma(v,y)\) has Jacobian one at \(v=0\), so the coefficient of the delta at a fixed \(y\) remains \(\sqrt{\det G(y)}\). To justify the identity jointly in \(y\), apply (WG6) to a compactly supported test and integrate its smooth \(y\)-dependent pairing with the fixed distribution \(E_\nu(t,w)\). The distributional finite-order estimates on one compact support control all these pairings and permit differentiation in \(y\). The fixed-center identity consequently integrates to (WG17). For the delta term the pairing is simply the test evaluated at \(t=0,x=y\), times its smooth coefficient. This proves the joint identity without a measure-theoretic interchange of singular pointwise functions.

The density convention can be checked directly. Put
\[
 d\mu(y)=\rho(y)\,dy,\qquad
 \rho(y)=(\det G(y))^{-1/2}.
 \tag{WG18}
\]
Integration of the point-source term of (WG17) against \(f(y)d\mu(y)\) gives \(\delta(t)f(x)\). Relative to coordinate volume \(dy\), multiply the entire kernel by \(\rho(y)\) to obtain that same normalization. As a result the causal finite parametrix sends initial velocity \(f\) to a kernel with the correct first trace, relative to the selected density. We have constructed a local approximate solution with an explicit error, not presumed a global Cauchy evolution.

On a smooth vector bundle this argument is made in local frames. Under a frame change \(T(x)\), the amplitudes transform as \(T(x)^{-1}U_\nu(x,y)T(y)\). This follows from uniqueness of the normalized matrix transport, exactly as in EHP-006; the scalar radial factor is unchanged. The local expressions therefore agree on overlaps, with their density factor, and define the same bundle-valued short-time kernel. The positive scalar principal symbol is essential to this one-distance construction. Systems with several principal characteristic cones require additional arguments.

There is a useful version reaching an entire bounded domain. Suppose \(\overline X\) is compact, the coefficients extend smoothly to an open neighborhood \(X'\) of \(\overline X\), and the principal matrix is positive definite on \(\overline X\). Positivity persists on a smaller neighborhood: the least eigenvalue has a positive minimum on the compact closure, and continuity preserves a positive lower bound nearby. Apply (WG17) on this smaller ambient neighborhood with the relatively compact center set \(Y=X\). Restricting the resulting distribution identity to \(x,y\in X\) gives a common positive time for all centers of \(X\), including those arbitrarily near its boundary. The distance here is that of the extended ambient metric. It need not be the intrinsic distance obtained by forcing paths to stay in a nonconvex \(X\). This restriction imposes no boundary condition.

The clause after Proposition 17.4.3 allowing \(Y=X\) after extension is used here with the compact-closure hypothesis needed for its uniform-radius argument. Smooth extension and pointwise ellipticity alone on a noncompact closure do not supply a positive uniform radius. This unit makes no such noncompact uniform-radius assertion. The compact-center theorem itself requires no boundedness of the larger ambient domain.

## AN03-WHK-013 — Four concrete checks

**Two spatial dimensions have an interior tail.** At \(n=2,\nu=0\), (W15) gives
\[
 E_0(t,x)=\frac{\boldsymbol1_{\{t>|x|\}}}{2\pi\sqrt{t^2-|x|^2}}.
 \tag{WX1}
\]
The factor is \(A_0/\Gamma(1/2)=1/(2\pi)\). Its total spatial mass at time \(t>0\) is
\(\int_0^t r(t^2-r^2)^{-1/2}dr=t\). Thus a spatial test equal to one near the shrinking support gives first initial derivative one, as required by (W19). The support includes the interior of the cone; a statement that all wave kernels live only on its surface would fail here.

**Coalescing spheres can have a finite odd difference.** At \(n=3,\nu=0\), the time distribution for \(r=|x|>0\) is
\[
 E_0(t,x)=\frac{\delta(t-r)}{4\pi r},\qquad
 W_0(t,x)=\frac{\delta(t-r)-\delta(t+r)}{4\pi r}.
 \tag{WX2}
\]
Pairing the second expression with \(\phi\) gives \((\phi(r)-\phi(-r))/(4\pi r)\), which tends to \(\phi'(0)/(2\pi)\). Therefore \(W_0(t,0)=-\delta'(t)/(2\pi)\) and \(\partial_tW_0(t,0)=-\delta''(t)/(2\pi)\). This is (OE19) with \(k=1\). Pairing the first expression with a test equal to one near zero instead diverges. The reflected difference is essential to the finite-order parameter statement.

**An anisotropic metric changes the delta weight.** In two dimensions take \(G=\operatorname{diag}(9,4)\) and \(b=c=0\). Then
\[
 s(x,y)^2=(x_1-y_1)^2/9+(x_2-y_2)^2/4,
 \qquad d\mu=dy/6.
 \tag{WX3}
\]
The leading amplitude is one and all later ones vanish. The kernel \(E_0(t,s(x,y))\) has point-source coefficient \(6\), because the linear map to isotropic coordinates has determinant \(1/6\). Its convolution with \(dy/6\) has the unit initial-velocity normalization. Its spatial support at fixed \(t>0\) is an ellipse, not a Euclidean ball of radius \(t\).

**A constant matrix potential keeps its order in the expansion.** Let \(P=-\Delta I_r+C\), with any fixed complex matrix \(C\). Then \(h=0\), \(u_0=I_r\), and (WG5) gives
\[
 u_\nu=\frac{(-C)^\nu}{\nu!},\qquad
 (\partial_t^2+P)\sum_{\nu=0}^N\frac{(-C)^\nu}{\nu!}E_\nu
  =\delta I_r+\frac{(-1)^NC^{N+1}}{N!}E_N.
 \tag{WX4}
\]
The formula follows by induction: the transport equation for a constant amplitude is \(\nu u_\nu=-Cu_{\nu-1}\). No diagonalization, real eigenvalues or positivity are used. If \(C^m=0\), the finite sum with \(N=m-1\) is already an exact causal fundamental kernel, since the displayed remainder vanishes.

## AN03-WHK-014 — Problems and complete solutions

**Problem 1 — The first three initial traces in one dimension.** Compute \(E_1\) for \(n=1\), integrate it against a smooth spatial test, and verify the first nonzero initial derivative.

**Solution.** Here \(a=1\), \(A_1=1/8\), so \(E_1(t,x)=\boldsymbol1_{\{t>0\}}(t^2-x^2)_+/8\). At \(t>0\), substitution \(x=tu\) gives
\[
 \langle E_1(t,\cdot),\phi\rangle
     =\frac{t^3}{8}\int_{-1}^{1}(1-u^2)\phi(tu)\,du
     =\frac{t^3}{6}\phi(0)+O(t^5).
 \tag{WP1}
\]
The odd Taylor term integrates to zero, and the remainder bound follows from the second derivative of \(\phi\) on a fixed compact interval. Smoothness in \(t\geq0\) follows by differentiating the fixed integral. Derivatives of orders zero, one and two vanish at zero; the third derivative is \(\phi(0)\). Thus the trace is \(1!\delta_0\), with the exact normalization.

**Problem 2 — Why the test order cannot be lowered.** At \(n=5,\nu=0\), find \(\partial_tW_0(t,0)\), and show that a uniform order-three estimate cannot hold near \(x=0\).

**Solution.** Now \(k=2\), \(a=-2\), and (OE19) gives
\[
                       \partial_tW_0(t,0)=\frac1{12\pi^2}\delta^{(4)}(t).
 \tag{WP2}
\]
Indeed \(2^{2k-n+1}=1\) and \(k!/(2k)!=1/12\). If an order-three estimate uniform near \(x=0\) held, continuity on smooth tests would pass that estimate to \(x=0\). Choose \(\psi\in C_c^\infty\) with \(\psi^{(4)}(0)\ne0\), and let \(\phi_\varepsilon(t)=\varepsilon^3\psi(t/\varepsilon)\). Its derivatives through order three stay bounded on one fixed support, but the pairing with (WP2) grows as \(\varepsilon^{-1}\). This contradiction proves the claim.

**Problem 3 — Weak convergence is not norm convergence.** For \(e_{\delta,0}\), compute its distance from \(e_{0,0}\) in total variation and its limit against a continuous test.

**Solution.** For \(\delta>0\), the three support points \(\sqrt\delta,-\sqrt\delta,0\) are distinct. The signed difference has masses \(1,1,-2\), so its total variation is \(4\). On a continuous test \(\phi\), its value is \(\phi(\sqrt\delta)+\phi(-\sqrt\delta)-2\phi(0)\), which tends to zero by continuity at the origin. These facts hold even on a fixed interval containing all points for small \(\delta\). They explain precisely why the topology in WHK-006 was specified on fixed \(C^m\) tests.

**Problem 4 — Design an error with three continuous derivatives.** In spatial dimension \(n=4\), choose the smallest truncation index guaranteed by this unit to give a \(C^3\) remainder for arbitrary smooth coefficients. Explain what fails at the next smaller index.

**Solution.** Inequality (WG14) reads \(3<N-3/2\), hence the smallest integer is \(N=5\). For \(N=4\), the exponent of the cone power is \(a=5/2\). At a nonzero cone point its third transverse derivative is a nonzero constant times \(q_+^{-1/2}\) and is unbounded. If \(P=-\Delta+1\), (WX4) makes the remainder amplitude a nonzero constant, so this failure actually occurs. At \(N=5\), \(a=7/2>3\), and WHK-011 controls the cone and its vertex.

**Problem 5 — A nilpotent system with an exact finite answer.** Let
\[
 C=\begin{pmatrix}0&2&0\\0&0&3\\0&0&0\end{pmatrix},
 \qquad P=-\Delta I_3+C.
 \tag{WP3}
\]
Find a causal fundamental kernel and its first initial traces.

**Solution.** Matrix multiplication gives \(C^2_{13}=6\), every other entry of \(C^2\) zero, and \(C^3=0\). Formula (WX4) with \(N=2\) therefore yields
\[
 K=E_0I_3-CE_1+\tfrac12C^2E_2
   =\begin{pmatrix}E_0&-2E_1&3E_2\\0&E_0&-3E_1\\0&0&E_0\end{pmatrix}.
 \tag{WP4}
\]
Its causal support follows term by term, and the exact equation is \((\partial_t^2+P)K=\delta I_3\). From (W19), \(K(0+,\cdot)=0\) and \(\partial_tK(0+,\cdot)=\delta_0I_3\). Terms with \(E_1,E_2\) start at orders three and five; they do not alter those initial data. This system is not diagonalizable, so an argument requiring diagonalization would miss it.

**Problem 6 — A cutoff and the first affected time.** A smooth function \(\theta(x,y)\) equals one where \(s(x,y)\leq2c\), and its derivatives are supported where \(s(x,y)>2c\) inside a larger normal neighborhood. Show that multiplying every amplitude by \(\theta\) changes no finite wave identity on \(t<2c\). Determine whether the same conclusion necessarily holds at \(t=2c\).

**Solution.** Each commutator term from \(P_x\) contains a derivative of \(\theta\) multiplied by a smooth coefficient, an amplitude, and a spatial derivative of \(E_\nu\). Distributional derivatives have support contained in that of \(E_\nu\), namely \(t\geq s(x,y)\). At every point with \(t<2c<s\), a neighborhood still satisfies \(t<s\); therefore each such term is zero there. The difference from the uncut product is zero by the same argument.

Under the stated stronger hypothesis the answer at \(t=2c\) is also yes, locally near each point of that time slice. At \(s=2c\), the closed support of each derivative of \(\theta\) is absent from a neighborhood, because that support lies in the open set \(s>2c\). Hence \(\theta\) is locally constant there, and its value is one by continuity from \(s<2c\). At \(s<2c\) it is already one, while at \(s>2c\) causal support makes the kernel vanish near \(t=2c\). These three cases prove the local assertion. A single larger time interval would require a uniform positive gap between the affected region and \(s=2c\); it is not implied just by local separation over a noncompact set. The basic extension theorem in WHK-011 uses only the open time interval and needs no such gap.

## Reading, provenance, and further routes

The mathematical antecedent is Lars Hörmander, *The Analysis of Linear Partial Differential Operators III*, corrected second printing (1994), Lemma 17.4.2, its subsidiary arguments, and Proposition 17.4.3. Volume I, second edition (1990), §2.1 fixes the finite distribution-order convention. This unit obtains the causal constants from a Laplace integral and the time traces from a Volterra simplex, then treats finite-order restriction and geometric cancellation separately. The domain reconciliation in WHK-007 is explicit because a negative factorial or a negative derivative order cannot be inserted into the printed endpoint expression.

Christian Bär, Nicolas Ginoux and Frank Pfäffle, [*Wave Equations on Lorentzian Manifolds and Quantization*, arXiv:0806.1036v1](https://arxiv.org/abs/0806.1036v1), §§1.2 and 2.1–2.4, compares Lorentzian Riesz distributions and bundle Hadamard coefficients. Their dimension is spacetime dimension, \(n+1\) here, and their parameter is \(2\lambda\). They call the future-supported branch “advanced”; our causal kernel satisfies \(E_\nu=\nu!R_+(2\nu+2)\) in their flat notation. Proposition 2.3.1 covers normally hyperbolic bundle operators, and their finite-sum identity (2.13) checks the cancellation. The finite-order restriction, vertex coefficient, and flat cosine normalization required here are proved explicitly above. The inspected version carries a nonexclusive arXiv distribution license; its prose is not reproduced here.

Three directions continue the work. **Quantitative coefficient dependence:** for a fixed compact center set and a prescribed \(C^k\) error norm, derive the finite list of coefficient seminorms needed in the transport and coordinate estimates. The proof supplies bounds but does not optimize that list. **From finite parametrices to evolution:** combine increasing-order causal errors with a suitable local solution operator to obtain an exact evolution and compare the resulting kernel with the flat cosine spectral relation. Such a step requires an existence and uniqueness theorem at the selected coefficient regularity; the finite identity alone is insufficient. **Reflection at a boundary:** construct the reflected exponential map and the boundary matching amplitudes before imposing Dirichlet or other boundary data. A cutoff of an interior normal kernel supplies neither the reflected ray nor a boundary condition. These are further course and research routes, not claims that established wave theory is conjectural.

The independently written programme exposition is dedicated under **CC0 1.0 Universal**, as specified in the course license.
