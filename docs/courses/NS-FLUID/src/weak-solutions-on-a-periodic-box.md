# Weak solutions on a periodic box

The energy identity controls a velocity and its first spatial derivatives even when higher derivatives become large. We will use that control to construct a solution which exists for every finite time. The equation will hold after integration against smooth test fields. This is the meaning of a **weak solution** used here.

There are three things to prove. Finite approximations must exist without a time limit. A subsequence must converge strongly enough for the quadratic term to survive. Finally, the limiting velocity must retain the equation, the initial value and the energy inequality. We prove all three on a periodic box. We then recover its pressure and show that it agrees with a sufficiently regular solution whenever the two have the same data.

Read [the equations and energy lesson](forces-energy-and-vorticity.md) and [the pressure and projection lesson](pressure-and-the-divergence-free-projection.md) first. We use their Fourier convention, Parseval identity and periodic projection. We assume completeness of \(L^2\), elementary Lebesgue integration, Fubini's theorem and dominated convergence. The compactness and finite-dimensional existence arguments needed below are included.

## 1. The domain, force and meaning of solution

Fix an integer \(n\geq2\), lengths \(L_1,\ldots,L_n>0\), and viscosity \(\nu>0\). Keep all of them fixed. Write

\[
 D=\prod_{j=1}^n(\mathbb R/L_j\mathbb Z),\qquad
 V=\prod_{j=1}^nL_j,\qquad
 \kappa_k=(k_1/L_1,\ldots,k_n/L_n),\qquad
 \lambda_k=4\pi^2|\kappa_k|^2.
 \tag{1.1}
\]

For a periodic vector field its Fourier coefficient is

\[
 \widehat u_k=\frac1V\int_Du(x)e^{-2\pi i\kappa_k\cdot x}\,dx.
 \tag{1.2}
\]

All velocities and forces in the lesson are real. Thus their coefficients have conjugate symmetry. Complex coefficients are a convenient way to write real identities; scalar products below are real scalar products, or the real part of their Fourier expressions.

For every real \(s\), define \(H^s(D)\) by the norm

\[
 \|u\|_{H^s}^2=V\sum_{k\in\mathbb Z^n}(1+\lambda_k)^s|\widehat u_k|^2.
 \tag{1.3}
\]

For \(s<0\), the coefficient sequence defines a distribution: its pairing with a smooth function converges by Cauchy–Schwarz because that function's coefficients decay faster than every power. For \(s=1\), Parseval gives the exact identity

\[
 \|u\|_{H^1}^2=\|u\|_2^2+\|\nabla u\|_2^2.
 \tag{1.4}
\]

Here and below the norm of a matrix is its Euclidean, or Frobenius, norm. Let \(H^s_\sigma\) denote the closed subspace with

\[
 \kappa_k\cdot\widehat u_k=0\quad(k\ne0).
 \tag{1.5}
\]

This is precisely the condition \(\operatorname{div}u=0\) in distributions. It imposes no restriction on \(\widehat u_0\), the spatial mean.

The data are

\[
 u_0\in L^2_\sigma(D),\qquad
 f\in L^2(0,T;H^{-1}(D))\quad\hbox{for every finite }T>0.
 \tag{1.6}
\]

The time-dependent functions in these spaces are strongly measurable; changing them on a set of times of measure zero does not change the data. The force need not be divergence free and need not have zero mean. The duality between \(H^{-1}\) and \(H^1\) is

\[
 \langle f,v\rangle
 =V\operatorname{Re}\sum_k\widehat f_k\cdot\overline{\widehat v_k},
 \qquad
 |\langle f,v\rangle|\leq\|f\|_{H^{-1}}\|v\|_{H^1}.
 \tag{1.7}
\]

The bound follows by inserting the factors \((1+\lambda_k)^{-1/2}\) and \((1+\lambda_k)^{1/2}\) and applying Cauchy–Schwarz. It also shows that the integral of the force's work is defined for every velocity in \(L^2_tH^1_x\).

**Definition.** A periodic Leray–Hopf solution for these data is a velocity satisfying, for every finite \(T\),

\[
 u\in L^\infty(0,T;L^2_\sigma)\cap L^2(0,T;H^1_\sigma),
 \qquad u\in C_{\rm w}([0,\infty);L^2_\sigma),\qquad u(0)=u_0.
 \tag{1.8}
\]

Weak continuity, denoted by \(C_{\rm w}\), means that \(t\mapsto(u(t),h)_{L^2}\) is continuous for every fixed \(h\in L^2\). We require the identity

\[
 \begin{aligned}
 &-\int_0^\infty(u,\partial_t\phi)\,dt
 +\nu\int_0^\infty\int_D\nabla u : \nabla\phi\,dx\,dt\\
 &\quad-\int_0^\infty\int_D\sum_{i,j=1}^n u_i u_j\partial_j\phi_i\,dx\,dt\\
 &\qquad= (u_0,\phi(0))+\int_0^\infty\langle f,\phi\rangle\,dt.
 \end{aligned}
 \tag{1.9}
\]

for every smooth periodic divergence-free vector field \(\phi\) with compact support in \(t\in[0,\infty)\). The double contraction in the second term is \(\sum_{i,j}\partial_j u_i\partial_j\phi_i\). Since \(u\in L^2\) on each finite space-time cylinder, \(u_i u_j\) is integrable there. Thus each term is defined.

Finally, there must be a set \(G\subset(0,\infty)\) whose complement has measure zero such that, for \(s=0\) and for every \(s\in G\), the inequality

\[
 \frac12\|u(t)\|_2^2
 +\nu\int_s^t\|\nabla u(r)\|_2^2\,dr
 \leq\frac12\|u(s)\|_2^2
 +\int_s^t\langle f(r),u(r)\rangle\,dr
 \quad\hbox{holds for every }t\geq s.
 \tag{1.10}
\]

The set of permitted starting times is part of the statement. We will prove that the same set works for all ending times. We do not insert an unproved energy inequality at an exceptional starting time.

**Existence theorem.** For all the data in (1.1) and (1.6), a solution with properties (1.8)–(1.10) exists on \(0\leq t<\infty\). Its mean satisfies

\[
 \widehat u_0(t)=\widehat{u_0}_0+\int_0^t\widehat f_0(r)\,dr.
 \tag{1.11}
\]

It is strongly continuous from the right in \(L^2\) at \(0\) and at every \(s\in G\). There is a mean-zero pressure distribution \(p\) for which

\[
 \partial_tu+\operatorname{div}(u\otimes u)+\nabla p
 =\nu\Delta u+f,\qquad\operatorname{div}u=0.
 \tag{1.12}
\]

The tensor convention is \((u\otimes u)_{ij}=u_i u_j\), so its divergence has component \(\sum_j\partial_j(u_i u_j)\). Sections 2–6 prove the theorem, including a precise space for \(p\). Section 7 proves weak–strong uniqueness with its regularity assumptions stated explicitly.

## 2. Finite equations which preserve the energy calculation

Let \(E_N\) retain exactly the Fourier coefficients with \(|\kappa_k|\leq N\). These sets are finite, symmetric under \(k\mapsto-k\), increasing, and contain \(k=0\). Let \(P\) be the projection from the preceding lesson:

\[
 P_k=I-\frac{\kappa_k\otimes\kappa_k}{|\kappa_k|^2}\quad(k\ne0),
 \qquad P_0=I.
 \tag{2.1}
\]

The maps \(E_N\) and \(P\) commute, are self-adjoint, preserve real fields and have norm at most one on every \(H^s\). They commute with spatial derivatives. These assertions follow coefficient by coefficient from the orthogonal matrix projection in (2.1) and the scalar cutoff defining \(E_N\).

Seek \(u_N(t)\in E_NL^2_\sigma\) satisfying

\[
 \partial_tu_N=\nu\Delta u_N-E_NP\operatorname{div}(u_N\otimes u_N)+E_NPf,
 \qquad u_N(0)=E_Nu_0.
 \tag{2.2}
\]

Choose any real orthonormal basis of this finite-dimensional space. Equation (2.2) becomes

\[
 a'(t)=B(a(t))+b(t),
 \tag{2.3}
\]

where \(B\) is a polynomial of degree at most two and the finitely many components of \(b\) are in \(L^2(0,T)\). To see the last claim, (1.3) gives

\[
 |\widehat f_k(t)|\leq V^{-1/2}(1+\lambda_k)^{1/2}\|f(t)\|_{H^{-1}}.
 \tag{2.4}
\]

Here is the local existence argument for (2.3). Fix a starting value \(a_*\) and a closed ball of radius \(R>0\) about it. On that ball \(B\) is bounded by some \(M<\infty\) and is Lipschitz with some constant \(K<\infty\): each polynomial difference factors as a sum of a coordinate difference times bounded coordinates. On a short interval \([t_*,t_*+\delta]\), choose

\[
 M\delta+\int_{t_*}^{t_*+\delta}|b(r)|\,dr\leq R,
 \qquad K\delta<1.
 \tag{2.5}
\]

Such an interval exists because an integrable function has an absolutely continuous integral. The map

\[
 (\mathcal Ta)(t)=a_*+\int_{t_*}^t[B(a(r))+b(r)]\,dr
 \tag{2.6}
\]

maps the closed ball of continuous paths into itself. In the uniform norm its Lipschitz constant is at most \(K\delta\). Starting from the constant path, successive differences are bounded by a geometric series. The iterates therefore converge uniformly to a continuous fixed point. Passing under the integral is justified by uniform convergence and the Lipschitz bound. The fixed point is absolutely continuous, solves (2.3) almost everywhere and is unique on this interval. Repeating the argument gives a maximal solution.

We next prove it cannot end at a finite time. Take the scalar product of (2.2) with \(u_N\). Self-adjointness removes \(E_NP\) from this scalar product because \(E_NPu_N=u_N\). Periodic integration by parts gives

\[
 \begin{aligned}
 \int_D\sum_{i,j}u_{N,i}u_{N,j}\partial_j u_{N,i}\,dx
 &=\frac12\int_D\sum_j u_{N,j}\partial_j|u_N|^2\,dx\\
 &=-\frac12\int_D(\operatorname{div}u_N)|u_N|^2\,dx=0.
 \end{aligned}
 \tag{2.7}
\]

Set

\[
 E_N(t)=\|u_N(t)\|_2^2,\qquad
 D_N(t)=\|\nabla u_N(t)\|_2^2,\qquad F(t)=\|f(t)\|_{H^{-1}}.
 \tag{2.8}
\]

The finite system obeys the exact energy identity

\[
 \frac12 E_N'(t)+\nu D_N(t)=\langle f(t),u_N(t)\rangle
 \quad\hbox{for almost every }t.
 \tag{2.9}
\]

Cauchy–Schwarz in (1.7) and the nonnegative square

\[
 \left(\sqrt\nu\sqrt{E_N+D_N}-\frac{F}{\sqrt\nu}\right)^2\geq0
 \tag{2.10}
\]

give \(2F\sqrt{E_N+D_N}\leq\nu(E_N+D_N)+\nu^{-1}F^2\). Hence

\[
 E_N'+\nu D_N\leq\nu E_N+\nu^{-1}F^2.
 \tag{2.11}
\]

Multiplication by \(e^{-\nu t}\) and integration give

\[
 e^{-\nu t}E_N(t)+\nu\int_0^t e^{-\nu r}D_N(r)\,dr
 \leq\|u_0\|_2^2+\nu^{-1}\int_0^t e^{-\nu r}F(r)^2\,dr.
 \tag{2.12}
\]

For each finite \(T\), define the explicit bound

\[
 A_T=e^{\nu T}\left(\|u_0\|_2^2+\nu^{-1}\int_0^T F(r)^2\,dr\right).
 \tag{2.13}
\]

Multiplying (2.12) by \(e^{\nu t}\), and using \(e^{\nu(t-r)}\geq1\) for \(0\leq r\leq t\), proves

\[
 E_N(t)+\nu\int_0^tD_N(r)\,dr\leq A_T\quad(0\leq t\leq T),
 \qquad
 \int_0^T\|u_N(r)\|_{H^1}^2\,dr\leq T A_T+\frac{A_T}{\nu}.
 \tag{2.14}
\]

These bounds are independent of \(N\). In particular the finite coordinate vector stays in a bounded ball on every finite interval. On such a ball \(B(a)\) is bounded and \(b\in L^1\), so the integral of \(|a'|\) is finite. If its maximal interval had a finite endpoint, \(a(t)\) would be Cauchy there and have a finite limit. The local construction starting at that limit would extend it. This contradicts maximality. Thus every \(u_N\) exists for all finite times.

No Poincaré estimate was used on the constant mode. In fact the coefficient \(k=0\) in (2.2) is exactly

\[
 \frac{d}{dt}\widehat u_{N,0}=\widehat f_0.
 \tag{2.15}
\]

The Laplacian and the divergence of the quadratic term have zero mean; viscosity does not damp a constant velocity.

## 3. Compactness in space and time

Fix \(T<\infty\). A bounded sequence in \(L^2\) need not converge strongly. Even a bound on spatial derivatives alone does not rule out increasingly fast time oscillations; Exercise 2 gives an exact example. We use the equations to control each fixed Fourier coefficient in time.

For \(N\geq|\kappa_k|\), (2.2) says

\[
 \frac{d}{dt}\widehat u_{N,k}
 =-\nu\lambda_k\widehat u_{N,k}
 -2\pi iP_k\sum_{j=1}^n(\kappa_k)_j\widehat{u_{N,j}u_N}_k
 +P_k\widehat f_k.
 \tag{3.1}
\]

The vector in the middle has magnitude at most \(2\pi|\kappa_k|E_N/V\). Indeed its unprojected coefficient is

\[
 \frac{2\pi i}{V}\int_D(\kappa_k\cdot u_N)u_Ne^{-2\pi i\kappa_k\cdot x}\,dx,
 \tag{3.2}
\]

whose magnitude is bounded by \(2\pi|\kappa_k|\|u_N\|_2^2/V\), and \(\|P_k\|\leq1\). Parseval also gives \(|\widehat u_{N,k}|\leq V^{-1/2}\sqrt{A_T}\). Integrating (3.1) and using (2.4) yields, for \(0\leq s\leq t\leq T\),

\[
 \begin{aligned}
 |\widehat u_{N,k}(t)-\widehat u_{N,k}(s)|
 &\leq\left(\nu\lambda_k V^{-1/2}\sqrt{A_T}
       +\frac{2\pi|\kappa_k|}{V}A_T\right)(t-s)\\
 &\quad+V^{-1/2}(1+\lambda_k)^{1/2}
       \|F\|_{L^2(0,T)}(t-s)^{1/2}.
 \end{aligned}
 \tag{3.3}
\]

For each fixed \(k\), these coefficients are uniformly bounded and have a common modulus of continuity. We spell out why this gives a uniformly convergent subsequence. At each rational time in \([0,T]\), a bounded sequence in a finite-dimensional space has a convergent subsequence: repeatedly bisect a containing cube and keep an infinite occupied subcube to obtain a Cauchy subsequence. Choose subsequences successively for a countable dense set of times, and take the diagonal sequence. Given \(\varepsilon>0\), the common modulus of continuity permits a finite set of these times within distance \(\delta\) of every point, with each continuity error below \(\varepsilon/3\). On this finite set the diagonal sequence is Cauchy. Comparing two paths through the nearest chosen time makes their uniform difference less than \(\varepsilon\). Completeness then gives a continuous uniform limit.

Enumerate the countably many pairs consisting of a Fourier mode \(k\) and an integer time endpoint \(T=1,2,\ldots\). Apply the preceding subsequence argument successively and take a diagonal sequence. Along the resulting sequence, still denoted by \(u_N\), every fixed coefficient converges uniformly on every finite time interval to a continuous function \(a_k(t)\).

This is control of finitely many modes at a time. The gradient bound controls all remaining modes together. For any \(R>0\), Parseval gives

\[
 \begin{aligned}
 \int_0^T\|(I-E_R)u_N(r)\|_2^2\,dr
 &=V\int_0^T\sum_{|\kappa_k|>R}|\widehat u_{N,k}(r)|^2\,dr\\
 &\leq\frac1{4\pi^2R^2}\int_0^TD_N(r)\,dr
 \leq\frac{A_T}{4\pi^2\nu R^2}.
 \end{aligned}
 \tag{3.4}
\]

Given \(\varepsilon>0\), first choose \(R\) so that the square root of the last bound is less than \(\varepsilon/3\). The finitely many retained coefficients converge uniformly, so \(E_Ru_N\) is Cauchy in \(L^2(0,T;L^2)\). The triangle inequality, with the two omitted tails, makes \(u_N\) Cauchy in this space. Its completeness produces a limit \(u\) and

\[
 u_N\longrightarrow u\quad\hbox{strongly in }L^2(0,T;L^2(D))
 \quad\hbox{for every finite }T.
 \tag{3.5}
\]

### The gradient and the value at each time

We also need weak convergence in \(L^2(0,T;H^1)\). Here is the Hilbert-space argument behind it. In a separable Hilbert space with orthonormal basis \(e_1,e_2,\ldots\), a bounded sequence has a subsequence for which every coordinate converges. If its norms are at most \(M\), every finite sum of squared limiting coordinates is at most \(M^2\). Their series therefore defines a vector \(z\) with norm at most \(M\). For a finite linear combination of basis vectors, scalar products converge. For an arbitrary vector \(h\), approximate it by such combinations; the remaining scalar products are bounded by \(2M\) times the approximation error. Thus the subsequence converges weakly to \(z\).

The space \(L^2(0,T;H^1(D))\) is separable: finite Fourier sums with time coefficients that are step functions on rational intervals and have rational real and imaginary parts form a countable dense set. Density follows by first truncating Fourier series and then approximating the finitely many scalar \(L^2\) time functions by step functions. Applying the Hilbert argument to (2.14), then taking subsequences for integer \(T\), gives weak convergence in this space. Its limit is the same \(u\) as in (3.5), because the inclusion into \(L^2(0,T;L^2)\) is continuous and that space already has a strong limit. In particular

\[
 \nabla u_N\rightharpoonup\nabla u\quad\hbox{in }L^2((0,T)\times D).
 \tag{3.6}
\]

The identification also follows by testing spatial derivatives and integrating by parts. The Hilbert argument proves lower semicontinuity of the norm: every finite sum of squared limiting coordinates is bounded by the lower limit of the full squared norms, and taking the supremum over finite sums gives the assertion. The same argument applies on any time subinterval by restriction.

For a fixed time \(t\in[0,T]\) and any finite set of modes, the limit of the corresponding part of \(E_N(t)\) is at most \(A_T\). Increasing that finite set gives

\[
 V\sum_k|a_k(t)|^2\leq A_T.
 \tag{3.7}
\]

Thus the coefficients \(a_k(t)\) define an \(L^2\) vector at every time. It agrees almost everywhere in time with the strong space-time limit, since each of their Fourier coefficients agrees in \(L^2(0,T)\). We use this representative of \(u\) from now on. Conjugate symmetry and (1.5) pass to each coefficient.

To prove weak continuity, let \(h\in L^2\). The finite sum \((u(t),E_Rh)\) is continuous in \(t\). Its omitted part satisfies

\[
 |(u(t),(I-E_R)h)|\leq\sqrt{A_T}\|(I-E_R)h\|_2,
 \tag{3.8}
\]

uniformly on \([0,T]\), and the right side tends to zero. Hence \((u(t),h)\) is a uniform limit of continuous functions and is continuous. The same estimate, applied also to \(u_N\), proves

\[
 u_N(t)\rightharpoonup u(t)\quad\hbox{in }L^2(D)
 \quad\hbox{at every }t\geq0.
 \tag{3.9}
\]

At time zero the limiting coefficients are those of \(u_0\), so \(u(0)=u_0\). Equation (2.15) passes to the constant coefficient and proves (1.11).

## 4. Passing the quadratic equation to the limit

The strong convergence in (3.5) has a precise use. For vectors \(a,b\),

\[
 a\otimes a-b\otimes b=(a-b)\otimes a+b\otimes(a-b),
 \qquad |c\otimes d|=|c|\,|d|.
 \tag{4.1}
\]

Cauchy–Schwarz on the finite space-time cylinder therefore gives

\[
 \|u_N\otimes u_N-u\otimes u\|_{L^1_{t,x}}
 \leq(\|u_N\|_{L^2_{t,x}}+\|u\|_{L^2_{t,x}})
      \|u_N-u\|_{L^2_{t,x}}\longrightarrow0.
 \tag{4.2}
\]

Fix a test field \(\phi\) from (1.9), supported before a finite time \(T\). Pair (2.2) with \(E_N\phi\) and integrate in time. Since \(P\phi=\phi\), the resulting identity is

\[
 \begin{aligned}
 &-\int_0^T(u_N,\partial_tE_N\phi)\,dt
 +\nu\int_0^T\int_D\nabla u_N : \nabla E_N\phi\,dx\,dt\\
 &\quad-\int_0^T\int_D\sum_{i,j}u_{N,i}u_{N,j}\partial_jE_N\phi_i\,dx\,dt\\
 &\qquad= (E_Nu_0,E_N\phi(0))+\int_0^T\langle f,E_N\phi\rangle\,dt.
 \end{aligned}
 \tag{4.3}
\]

Every spatial derivative of \(E_N\phi\) converges uniformly to the corresponding derivative of \(\phi\), uniformly in time. To verify this, apply \((1-\Delta)^q\) to \(\phi\) and integrate by parts in (1.2). Its coefficient bounds are uniform in time and yield

\[
 |\widehat\phi_k(t)|\leq
 \frac{\sup_{0\leq r\leq T}\|(1-\Delta)^q\phi(r)\|_{L^1(D)}}
      {V(1+\lambda_k)^q}.
 \tag{4.4}
\]

Choose \(q\) large enough that this series still converges after multiplication by the needed derivative factors. For completeness, the number of lattice points with \(|\kappa_k|\leq R\) is at most \(\prod_j(2L_jR+1)\). Splitting into the shells \(2^a\leq|\kappa_k|<2^{a+1}\) proves that \(\sum_k(1+|\kappa_k|)^{-b}<\infty\) whenever \(b>n\). This proves the required summability. The same reasoning applies to time derivatives of \(\phi\).

The first term of (4.3) now converges by strong \(L^2\) convergence. The second converges by (3.6) and strong convergence of the test gradients. For the third, use (4.2) and the uniform bound on the test gradient; the additional difference between \(\nabla E_N\phi\) and \(\nabla\phi\) is bounded by its uniform norm times \(\|u\|_{L^2_{t,x}}^2\). The initial term converges because \(E_Nu_0\to u_0\) in \(L^2\). The last term converges by

\[
 \left|\int_0^T\langle f,E_N\phi-\phi\rangle\,dt\right|
 \leq\|f\|_{L^2_tH^{-1}_x}\|E_N\phi-\phi\|_{L^2_tH^1_x}\longrightarrow0.
 \tag{4.5}
\]

Taking the limit gives precisely (1.9), including all signs, the initial term and the unprojected force pairing.

## 5. Energy, permitted starting times and the initial value

Integrating the exact finite identity (2.9) from any \(s\) to any \(t\geq s\) gives

\[
 \frac12\|u_N(t)\|_2^2+\nu\int_s^t\|\nabla u_N(r)\|_2^2\,dr
 =\frac12\|u_N(s)\|_2^2+\int_s^t\langle f(r),u_N(r)\rangle\,dr.
 \tag{5.1}
\]

The force term converges for every fixed interval \([s,t]\). Indeed \(1_{(s,t)}f\in L^2_tH^{-1}_x\) defines a continuous linear functional on \(L^2_tH^1_x\), and we have weak convergence in that space. The two nonnegative terms on the left are lower semicontinuous by (3.6), (3.9) and the Hilbert argument above. At \(s=0\), the right-hand norm converges because \(E_Nu_0\to u_0\) strongly. We obtain (1.10) with \(s=0\), for every \(t\geq0\).

For other starting times the right-hand norm needs strong convergence. Choose a further subsequence, written \(u_{N_j}\), so that

\[
 \int_0^j\|u_{N_j}(r)-u(r)\|_2^2\,dr\leq2^{-j}.
 \tag{5.2}
\]

This is possible by (3.5), choosing successive indices. For each integer \(J\), Tonelli's theorem applied to the nonnegative sum gives

\[
 \int_0^J\sum_{j\geq J}\|u_{N_j}(r)-u(r)\|_2^2\,dr
 \leq\sum_{j\geq J}2^{-j}<\infty.
 \tag{5.3}
\]

Thus the summands tend to zero for almost every \(r\in(0,J)\). Taking the intersection of these full-measure sets over all \(J\) gives one set \(G\subset(0,\infty)\) such that \(u_{N_j}(s)\to u(s)\) strongly in \(L^2\) for every \(s\in G\). Discard, if necessary, the null set where the \(H^1\) representative is undefined.

Fix any one \(s\in G\). In (5.1) its initial norm now converges, the force work converges, and the left side is lower semicontinuous at every fixed \(t\geq s\). All the convergences used hold along the same subsequence at all ending times. Taking the lower limit proves (1.10) for this \(s\) and every \(t\geq s\). This establishes the stated quantifiers without an exceptional set of ending times depending on \(s\).

There is also strong right continuity at every permitted starting time. From (1.10), dropping its nonnegative dissipation term gives

\[
 \limsup_{t\downarrow s}\|u(t)\|_2^2\leq\|u(s)\|_2^2,
 \tag{5.4}
\]

because

\[
 \left|\int_s^t\langle f,u\rangle\,dr\right|
 \leq\left(\int_s^t\|f\|_{H^{-1}}^2\,dr\right)^{1/2}
      \left(\int_s^t\|u\|_{H^1}^2\,dr\right)^{1/2}\longrightarrow0.
 \tag{5.5}
\]

Weak continuity implies \((u(t),u(s))\to\|u(s)\|_2^2\). Therefore

\[
 \|u(t)-u(s)\|_2^2
 =\|u(t)\|_2^2+\|u(s)\|_2^2-2(u(t),u(s))\longrightarrow0
 \quad(t\downarrow s).
 \tag{5.6}
\]

This proof applies also at \(s=0\), giving the strong attainment of the original initial velocity.

## 6. Recovering pressure for a rough velocity and force

We have so far tested only divergence-free fields. We now construct the pressure which gives the full equation, with the original force \(f\). Choose any integer \(m>n/2+1\) and set \(L_{\max}=\max_jL_j\). Define

\[
 C_{D,m}=\left[\frac1V\sum_k
       4\pi^2|\kappa_k|^2(1+4\pi^2|\kappa_k|^2)^{-m}\right]^{1/2}.
 \tag{6.1}
\]

The lattice count in Section 4 proves this is finite: a dyadic shell has at most a constant times \(2^{an}\) points, and each summand there is bounded by a constant times \(2^{a(2-2m)}\). The resulting geometric series converges because \(n+2-2m<0\).

The Fourier series of the gradient and Cauchy–Schwarz give, first for finite sums and then by uniform convergence,

\[
 \|\nabla\phi\|_{L^\infty(D)}
 \leq\sum_k2\pi|\kappa_k|\,|\widehat\phi_k|
 \leq C_{D,m}\|\phi\|_{H^m}.
 \tag{6.2}
\]

Since \(|u\otimes u|=|u|^2\), its distributional divergence satisfies

\[
 \begin{aligned}
 \big|\langle\operatorname{div}(u\otimes u),\phi\rangle\big|
 &=\left|\int_D\sum_{i,j}u_i u_j\partial_j\phi_i\,dx\right|\\
 &\leq C_{D,m}\|u\|_2^2\|\phi\|_{H^m}.
 \end{aligned}
 \tag{6.3}
\]

Thus this divergence belongs to \(H^{-m}\), with norm at most \(C_{D,m}\|u\|_2^2\). The identification of a bounded functional on \(H^m\) with such a coefficient sequence follows directly by applying the functional to its weighted orthonormal Fourier basis and using the Hilbert-space coordinate argument from Section 3. In time, the map is strongly measurable: the estimate obtained by replacing \(u\otimes u\) with \(u\otimes u-v\otimes v\) is at most \(C_{D,m}(\|u\|_2+\|v\|_2)\|u-v\|_2\), so it is a continuous map from \(L^2\) into \(H^{-m}\).

Put

\[
 w=f-\operatorname{div}(u\otimes u).
 \tag{6.4}
\]

For every finite \(T\), \(w\in L^1(0,T;H^{-m})\): \(f\in L^2_tH^{-1}_x\subset L^1_tH^{-m}_x\), and the nonlinear term is bounded in \(H^{-m}\) by the energy bound. Define the mean-zero scalar distribution \(p\) by

\[
 \widehat p_0=0,\qquad
 \widehat p_k=\frac{\kappa_k\cdot\widehat w_k}{2\pi i|\kappa_k|^2}
 \quad(k\ne0).
 \tag{6.5}
\]

It is a real distribution by conjugate symmetry. Every nonzero frequency obeys \(|\kappa_k|\geq L_{\max}^{-1}\), so

\[
 \begin{aligned}
 \|p\|_{H^{1-m}}^2
 &\leq V\sum_{k\ne0}\frac{(1+\lambda_k)^{1-m}}{\lambda_k}|\widehat w_k|^2\\
 &\leq\left(1+\frac{L_{\max}^2}{4\pi^2}\right)
       \|w\|_{H^{-m}}^2.
 \end{aligned}
 \tag{6.6}
\]

The constant in (6.6) is the exact squared norm of this pressure operator from \(H^{-m}\) to \(H^{1-m}\). To see that it cannot be decreased, choose \(j\) with \(L_j=L_{\max}\), set \(k=e_j\), and take a real vector field whose only nonzero coefficients are \(\widehat w_k=\widehat w_{-k}=e_j\). They are parallel to the corresponding frequencies, so the coefficient Cauchy–Schwarz inequality in (6.6) is an equality. Both frequencies have \(\lambda_k=4\pi^2/L_{\max}^2\). Dividing the two squared norms gives exactly \((1+\lambda_k)/\lambda_k=1+L_{\max}^2/(4\pi^2)\). This sharpness assertion concerns the linear operator (6.5) on its stated spaces.

Consequently \(p\in L^1(0,T;H^{1-m})\). Multiplying (6.5) by \(2\pi i\kappa_k\) proves

\[
 \nabla p=(I-P)w,\qquad
 \Delta p=\operatorname{div}f-\sum_{i,j}\partial_i\partial_j(u_i u_j).
 \tag{6.7}
\]

These identities include the zero frequency: both gradients and divergences have zero constant coefficient.

To recover the equation, let \(\psi\) be any smooth test vector field. The map \(P\) preserves smooth periodic fields, as is seen from its bounded coefficients and rapid Fourier decay. Thus (1.9) can be tested with \(P\psi\), giving

\[
 \partial_tu=\nu\Delta u+Pw
 \quad\hbox{as a distribution}.
 \tag{6.8}
\]

Here \(Pu=u\), so applying \(P\) to its time or spatial derivatives has no further effect. Adding (6.7) to (6.8) gives (1.12). If two pressures have the same gradient, every nonzero Fourier coefficient of their difference is zero. Their difference is therefore a spatial constant, possibly a distribution in time; the mean-zero condition selects the pressure (6.5).

This completes the existence theorem. Its pressure class is stated in (6.6). No local energy inequality, pointwise differentiability of \(u\), or \(L^2\) pressure has been inferred from the energy estimate.

## 7. Agreement with a regular solution

The existence theorem alone does not assert uniqueness among all weak solutions. It does give a precise comparison with a regular solution. Retain the same domain and viscosity. On a finite interval \([0,T]\), suppose a divergence-free velocity \(v\) satisfies the same projected equation with force \(f\) and

\[
 v\in C^1([0,T];L^2_\sigma(D))\cap C([0,T];H^m_\sigma(D)),
 \qquad m\in\mathbb N,\quad m>n/2+1.
 \tag{7.1}
\]

The force is still allowed to have a gradient component in \(H^{-1}\). The projected equation is an equality in distributions. Under (7.1) it implies

\[
 Pf=\partial_tv-\nu\Delta v+P\operatorname{div}(v\otimes v)\in C([0,T];L^2).
 \tag{7.2}
\]

Indeed \(m\geq2\) gives \(\Delta v\in CL^2\), while (6.2) and \(v\in CL^2\) give \((v\cdot\nabla)v\in CL^2\). Pairing (7.2) with any divergence-free \(H^1\) field agrees with its original force pairing, since \(P\) is self-adjoint also under \(H^{-1},H^1\) duality.

Let

\[
 L(t)=\|\nabla v(t)\|_{L^\infty(D)}.
 \tag{7.3}
\]

This is a bounded continuous function by (6.2). For every \(s=0\) or \(s\in G\) and \(s\leq t\leq T\), we will prove

\[
 \|u(t)-v(t)\|_2^2
 \leq\|u(s)-v(s)\|_2^2
       \exp\left(2\int_s^t L(r)\,dr\right).
 \tag{7.4}
\]

In particular, equal initial data imply \(u(t)=v(t)\) at every time in this interval.

### The cross identity is an admissible use of the weak equation

We must justify testing against \(v\), which depends on time and is not declared smooth in all variables. First take \(E_Rv\). It is a finite spatial Fourier sum with \(C^1\) time coefficients. Multiplying it by a smooth scalar time test function is allowed in (1.9), by approximating its finitely many coefficients and their first derivatives uniformly with smooth functions in time. Such approximations are obtained by extending a \(C^1\) coefficient past the interval using its endpoint value and derivative and convolving with a smooth compactly supported kernel; continuity of the coefficient and its derivative gives uniform convergence on the interval.

The weak identity then proves, distributionally in time,

\[
 \frac{d}{dt}(u,E_Rv)
 =(u,\partial_tE_Rv)
 +\int_D\sum_{i,j}u_i u_j\partial_jE_Rv_i\,dx
 -\nu\int_D\nabla u : \nabla E_Rv\,dx
 +\langle f,E_Rv\rangle.
 \tag{7.5}
\]

Its right side is integrable. A locally integrable scalar function whose distributional derivative equals \(g\in L^1\) differs by a constant from \(\int g\): subtract the integral and test the resulting zero derivative against functions of integral zero, each of which is the derivative of a compactly supported smooth function. This proves the assertion. Since the left-hand pairing is continuous by weak continuity of \(u\), (7.5) integrates to an identity at every pair of endpoints.

Now send \(R\to\infty\). The convergences \(E_Rv\to v\) in \(CH^m\) and \(\partial_tE_Rv\to\partial_tv\) in \(CL^2\) are uniform in time. To verify uniformity, cover the compact image of a continuous function on \([0,T]\) by finitely many small balls in the relevant Hilbert space. Strong convergence of the contractions \(E_R\) at their finitely many centers, plus the contraction bound on each ball, gives uniform convergence. Equation (6.2) gives uniform convergence of the gradients in \(L^\infty_x\). These facts, \(u\in L^\infty_tL^2_x\cap L^2_tH^1_x\), and \(f\in L^2_tH^{-1}_x\), justify passing every term of the integrated identity to the limit. We obtain

\[
 \begin{aligned}
 &(u(t),v(t))-(u(s),v(s))\\
 &\quad=\int_s^t\bigg[(u,\partial_rv)
 +\int_D\sum_{i,j}u_i u_j\partial_jv_i\,dx\\
 &\hspace{6em}-\nu\int_D\nabla u : \nabla v\,dx
 +\langle f,v\rangle\bigg]dr.
 \end{aligned}
 \tag{7.6}
\]

This identity holds for all \(0\leq s\leq t\leq T\), before using any energy inequality.

### The relative energy calculation

The regular solution obeys an energy equality. The time derivative of its squared \(L^2\) norm is \(2(v,\partial_tv)\); (7.2), periodic integration by parts and divergence freedom give

\[
 \frac12\|v(t)\|_2^2+\nu\int_s^t\|\nabla v\|_2^2\,dr
 =\frac12\|v(s)\|_2^2+\int_s^t\langle f,v\rangle\,dr.
 \tag{7.7}
\]

The nonlinear cancellation is exactly (2.7) with \(v\) in place of \(u_N\). It follows at the stated regularity either by the product rule for the continuously differentiable spatial representative supplied by (6.2), or by Fourier approximation in \(H^m\).

Write \(z=u-v\). Pairing (7.2) with \(u\), which is in \(H^1_\sigma\) almost everywhere, gives

\[
 (u,\partial_tv)
 =-\nu\int_D\nabla u : \nabla v\,dx
 -\int_D\sum_{i,j}u_i v_j\partial_jv_i\,dx
 +\langle f,u\rangle.
 \tag{7.8}
\]

The sum of its quadratic term and the quadratic term in (7.6) is

\[
 \begin{aligned}
 \int_D\sum_{i,j}u_i(u_j-v_j)\partial_jv_i\,dx
 &=\int_D\sum_{i,j}z_i z_j\partial_jv_i\,dx
   +\frac12\int_D z\cdot\nabla|v|^2\,dx\\
 &=\int_D\sum_{i,j}z_i z_j\partial_jv_i\,dx.
 \end{aligned}
 \tag{7.9}
\]

For the last equality, \(z\) is divergence free and \(|v|^2\in H^1\). The distributional divergence identity extends from smooth scalar tests to \(H^1\) by Fourier density and the bound \(|\int z\cdot\nabla h|\leq\|z\|_2\|\nabla h\|_2\).

Add the weak energy inequality (1.10) and (7.7), then subtract (7.6), using (7.8) and (7.9). The two force pairings cancel exactly. The two gradient norms and their cross term combine to the full squared gradient of \(z\). Thus

\[
 \frac12\|z(t)\|_2^2+\nu\int_s^t\|\nabla z(r)\|_2^2\,dr
 \leq\frac12\|z(s)\|_2^2
 -\int_s^t\int_D\sum_{i,j}z_i z_j\partial_jv_i\,dx\,dr.
 \tag{7.10}
\]

This holds at exactly the permitted starting times of \(u\). The matrix Cauchy–Schwarz inequality bounds the absolute value of the spatial integral by \(L(r)\|z(r)\|_2^2\). With \(Y(t)=\|z(t)\|_2^2\), dropping the dissipation gives

\[
 Y(t)\leq Y(s)+2\int_s^tL(r)Y(r)\,dr.
 \tag{7.11}
\]

To finish without leaving a differential inequality implicit, put \(H(t)=Y(s)+2\int_s^tL(r)Y(r)\,dr\). It is absolutely continuous, \(Y\leq H\), and \(H'=2LY\leq2LH\) almost everywhere. Hence

\[
 \frac{d}{dt}\left[e^{-2\int_s^tL(r)dr}H(t)\right]\leq0
 \quad\hbox{almost everywhere}.
 \tag{7.12}
\]

Integrating and using \(Y\leq H\) proves (7.4). This proof also covers \(Y(s)=0\) directly; no division by the initial difference was used.

## 8. Five exercises with complete solutions

### Exercise 1. A force which changes only the mean

Let \(a,b\in\mathbb R^n\) be constant vectors, \(u_0(x)=a\) and \(f(t,x)=b\). Find a solution and check its complete energy equality. Explain why a gradient bound alone cannot control this velocity.

**Solution.** Take \(u(t,x)=a+tb\) and \(p=0\). Every spatial derivative vanishes, so (1.12) becomes \(b=b\), and the field is divergence free. Its energy and dissipation are

\[
 \|u(t)\|_2^2=V|a+tb|^2,\qquad\|\nabla u(t)\|_2^2=0.
 \tag{8.1}
\]

The work between any \(s\leq t\) is

\[
 \int_s^t\langle f,u\rangle\,dr
 =V\int_s^tb\cdot(a+rb)\,dr
 =V(t-s)a\cdot b+\frac V2(t^2-s^2)|b|^2
 =\frac V2\bigl(|a+tb|^2-|a+sb|^2\bigr).
 \tag{8.2}
\]

This is the exact energy equality. The gradient remains zero while the energy can be positive and grow. Thus an inequality bounding the full \(L^2\) norm by a constant times the gradient norm is false on this space. The undamped coefficient is exactly the mean in (1.11).

### Exercise 2. Why time control is necessary

Fix a nonzero smooth divergence-free periodic field \(e\). On \(0\leq t\leq2\pi\), set \(w_N(t,x)=e(x)\sin(Nt)\), for positive integers \(N\). Show that the spatial energy bounds alone do not yield a strongly convergent subsequence in \(L^2_{t,x}\).

**Solution.** We have

\[
 \sup_t\|w_N(t)\|_2^2\leq\|e\|_2^2,\qquad
 \int_0^{2\pi}\|\nabla w_N\|_2^2\,dt=\pi\|\nabla e\|_2^2.
 \tag{8.3}
\]

For distinct positive integers \(N,M\), use the identity

\[
 2\sin(Nt)\sin(Mt)=\cos((N-M)t)-\cos((N+M)t).
\]

Its integral over this interval is zero. Each squared sine has integral \(\pi\). Therefore

\[
 \|w_N-w_M\|_{L^2_{t,x}}^2=2\pi\|e\|_2^2>0.
 \tag{8.4}
\]

No subsequence is Cauchy. For any mode with \(\widehat e_k\ne0\), the coefficient changes from zero at \(t=0\) to \(\widehat e_k\) at \(t=\pi/(2N)\). These times tend to zero, so there is no common modulus of continuity. Estimate (3.3), which comes from the equation as well as energy, rules out this behavior for the Galerkin solutions with fixed data and force.

### Exercise 3. The quadratic limit and its exact coefficient

Prove (4.2) for any two vector fields \(a,b\in L^2(X;\mathbb R^n)\) on a measure space \(X\). Does the proof require a bound on their derivatives?

**Solution.** At each point use the exact tensor identity (4.1), the triangle inequality and \(|c\otimes d|=|c||d|\). After integration,

\[
 \begin{aligned}
 \|a\otimes a-b\otimes b\|_{L^1(X)}
 &\leq\int_X|a-b|\,|a|+|b|\,|a-b|\\
 &\leq\|a-b\|_2\|a\|_2+\|b\|_2\|a-b\|_2.
 \end{aligned}
 \tag{8.5}
\]

Both applications are precisely Cauchy–Schwarz, so the coefficient is one. No derivative is used in this estimate. Derivative and time estimates were used earlier to obtain the strong \(L^2\) convergence to which it applies.

### Exercise 4. Strong convergence at a permitted starting time

Assume weak continuity of \(u\), the energy inequality beginning at one time \(s\), and \(f\in L^2(s,s+\delta;H^{-1})\), \(u\in L^2(s,s+\delta;H^1)\). Prove \(u(t)\to u(s)\) strongly in \(L^2\) as \(t\downarrow s\). State the exact role of the starting-time hypothesis.

**Solution.** Cauchy–Schwarz gives (5.5), whose right side tends to zero by absolute continuity of the two integrals. The energy inequality, with its dissipation term nonnegative, gives (5.4). Weak continuity gives the limit of \((u(t),u(s))\). Inserting these facts into the Hilbert identity (5.6) shows that the lower limit of the squared difference is nonnegative and its upper limit is at most zero. Hence the difference tends to zero. The initial norm on the right side of the energy inequality is essential in this argument. An inequality beginning at a different time does not give (5.4) at the chosen \(s\). The theorem therefore asserts this conclusion at \(0\) and the set \(G\) which it actually constructs.

### Exercise 5. Stability when the forces differ

Let \(u\) be a weak solution with force \(f\), and let \(v\) satisfy (7.1) and the projected equation with force \(g\in L^2(0,T;H^{-1})\). With \(Y(t)=\|u(t)-v(t)\|_2^2\) and \(L(t)\) as in (7.3), prove, at every permitted starting time \(s\),

\[
 \begin{aligned}
 Y(t)\leq
 \exp\left(\int_s^t[2L(r)+\nu]dr\right)
 \left[Y(s)+\nu^{-1}\int_s^t
 \exp\left(-\int_s^r[2L(q)+\nu]dq\right)
 \|f(r)-g(r)\|_{H^{-1}}^2\,dr\right].
 \end{aligned}
 \tag{8.6}
\]

**Solution.** The cross identity (7.6) still uses \(f\), because it is the weak equation for \(u\). In (7.8) the force is now \(g\), and the energy equality for \(v\) also uses \(g\). Subtracting the cross identity from the two energy statements leaves

\[
 \frac12Y(t)+\nu\int_s^t\|\nabla z\|_2^2\,dr
 \leq\frac12Y(s)-\int_s^t\int_D\sum_{i,j}z_i z_j\partial_jv_i\,dx\,dr
 +\int_s^t\langle f-g,z\rangle\,dr,
 \quad z=u-v.
 \tag{8.7}
\]

There is exactly one difference-force pairing: \(\langle f,u\rangle+\langle g,v\rangle-\langle g,u\rangle-\langle f,v\rangle=\langle f-g,u-v\rangle\). Let \(B(r)=\|f(r)-g(r)\|_{H^{-1}}\). As in (2.10),

\[
 2|\langle f-g,z\rangle|
 \leq2B\sqrt{Y+\|\nabla z\|_2^2}
 \leq\nu Y+\nu\|\nabla z\|_2^2+\nu^{-1}B^2.
 \tag{8.8}
\]

Multiplying (8.7) by two, using the nonlinear bound and moving the indicated dissipation term to the left gives

\[
 Y(t)+\nu\int_s^t\|\nabla z\|_2^2\,dr
 \leq Y(s)+\int_s^t(2L+\nu)Y\,dr+\nu^{-1}\int_s^tB^2\,dr.
 \tag{8.9}
\]

Put \(a=2L+\nu\) and \(H(t)=Y(s)+\int_s^t[a(r)Y(r)+\nu^{-1}B(r)^2]dr\). Then \(Y\leq H\) and \(H'\leq aH+\nu^{-1}B^2\) almost everywhere. Multiplying by \(\exp(-\int_s^t a)\) and integrating proves (8.6). All terms arising from the full \(H^1\) norm, including its constant mode, remain in (8.8)–(8.9).

## 9. What this chapter supplies to the series

The proof constructs a velocity for every finite time on the original periodic box, with the original positive viscosity and the original force. It proves the full energy inequality at its stated times and gives an actual pressure distribution. Its weak–strong comparison shows that this weak solution must follow a regular solution with the same data throughout the regular solution's interval of existence.

The compactness step used a finite number of low spatial frequencies and the explicit tail estimate (3.4). On the whole space low frequencies form a continuum, so the argument there requires additional control. The whole-space construction is the next part of the weak-solution foundations. Higher regularity, broader uniqueness criteria, and the singularity constructions in the later lessons require their own proofs. This chapter makes no assertion that the energy estimate alone controls all derivatives.

**Sources and precise scope of use.** The exposition and all proofs above are independently written. The original author TeX sources of the following freely accessible editions were read for the stated comparisons; they are not reproduced in the course.

- Dallas Albritton, Elia Brué and Maria Colombo, [*Non-uniqueness of Leray solutions of the forced Navier–Stokes equations*, arXiv:2112.03116v1](https://arxiv.org/abs/2112.03116v1), introduction, definition with labels `eq:minimumregularity` and `eq:energyinequality` (author file `main.tex`, lines 342–369). Their definition there concerns \(\mathbb R^3\), viscosity one and \(L^1_tL^2_x\) forces. Our periodic \(L^2_tH^{-1}_x\) existence statement, positive viscosity and permitted starting-time assertion are proved above. Their nonuniqueness construction is not invoked here.
- Terence Tao, [*Localisation and compactness properties of the Navier–Stokes global regularity problem*, arXiv:1108.1165v4](https://arxiv.org/abs/1108.1165v4), discussion preceding Proposition `partial` and equation `tim` (author file `local_ns.tex`, lines 1787–1807). That passage concerns whole-space solutions and a further spatial regularity construction. Neither that additional regularity conclusion nor its construction is used in this periodic proof.

**Authorship and review.** GPT-6 Astra (OpenAI), Ultra; 8 October 2026. Author self-check only; no independent review is claimed. The independently authored mathematical text, proofs, exercises and solutions are dedicated under CC0 1.0. The cited works retain their own rights.
