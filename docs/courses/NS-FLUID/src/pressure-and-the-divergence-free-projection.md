# Pressure and the divergence-free projection

*Written by GPT-6 Astra (OpenAI) at Ultra, October 2026. Self-checked by GPT-6 Astra; no independent review of this version is claimed. Mathematical text dedicated to the public domain under CC0.*

An incompressible velocity cannot move independently in every direction: its divergence must stay zero. Pressure supplies the part of the acceleration needed to respect that constraint. We will construct the operator that removes gradient fields, prove exactly which fields it keeps, and recover the pressure after applying it.

There are two settings: the whole space \(\mathbb R^n\), with \(n\geq2\), and a periodic box with arbitrary side lengths \(L_1,\ldots,L_n>0\). We retain the volume of the box, the factors \(2\pi\) in Fourier differentiation, and the viscosity \(\nu\). The spatially constant mode needs explicit treatment in the periodic case.

The earlier lesson [Forces, energy and vorticity in incompressible flow](forces-energy-and-vorticity.md) supplies the equations and the exact similarity transformation. Here we also use the basic rules of Lebesgue integration, completeness of \(L^2\), dominated convergence and Fubini's theorem. Section 8 proves the Fourier identities used in the construction. A distribution means a continuous linear functional on smooth compactly supported test functions; its derivative is defined by integration by parts. A tempered distribution acts continuously on Schwartz functions, which are smooth functions whose derivatives decrease faster than every inverse power of distance.

Tao [T, Section 1] writes the pressure projection and the symmetric Euler bilinear operator that we study in Section 5. We prove the needed operator statements here, with the external force and viscosity retained. The averaged equation treated later in that paper is a different evolution and is not a theorem about the unmodified equations.

## 1. One frequency at a time

Our whole-space Fourier transform is
\[
\widehat v(\xi)=\int_{\mathbb R^n}e^{-2\pi i x\cdot\xi}v(x)\,dx.
                                                               \tag{1.1}
\]
For square-integrable fields this is understood by the \(L^2\) extension proved in Section 8. The corresponding formulas are
\[
\|v\|_2^2=\int_{\mathbb R^n}|\widehat v(\xi)|^2\,d\xi,\qquad
\widehat{\partial_jv}=2\pi i\xi_j\widehat v,\qquad
\widehat{\Delta v}=-4\pi^2|\xi|^2\widehat v.                   \tag{1.2}
\]

At a nonzero frequency \(\xi\), define two real symmetric matrices
\[
Q(\xi)=\frac{\xi\xi^T}{|\xi|^2},\qquad P(\xi)=I-Q(\xi).
                                                               \tag{1.3}
\]
They also act on complex vectors. Inner products on complex vectors use complex conjugation in the second factor. Because \(\xi\) is real, the condition for being orthogonal to \(\xi\) is still \(\xi\cdot a=0\).

For any \(a\in\mathbb C^n\),
\[
Qa=\frac{\xi\cdot a}{|\xi|^2}\xi,\qquad
\xi\cdot Pa=0,\qquad a=Pa+Qa.                                \tag{1.4}
\]
The two terms are orthogonal. Indeed,
\(\langle Pa,Qa\rangle=\overline{(\xi\cdot a)/|\xi|^2}\,
\xi\cdot Pa=0\). Hence
\[
|a|^2=|Pa|^2+|Qa|^2,\quad
P^2=P,\quad Q^2=Q,\quad PQ=QP=0.                             \tag{1.5}
\]
For instance, \(Q^2a=Q(\xi)(\xi\cdot a)/|\xi|^2=Qa\), since \(Q\xi=\xi\); the other identities follow from \(P=I-Q\). Both matrices are self-adjoint and have norm at most one.

At \(\xi=0\), set \(P(0)=I\) and \(Q(0)=0\). Changing a matrix value at this single point changes no whole-space \(L^2\) function. In a Fourier series, however, the zero coefficient is an actual summand. We will keep the stated values there.

## 2. The whole-space decomposition

Let
\[
\mathcal H=L^2(\mathbb R^n;\mathbb C^n),\qquad
\mathcal S_\sigma
=\{v\in\mathcal H:\operatorname{div}v=0
                 \text{ as a distribution}\},
\]
and let
\[
\mathcal G=\overline{\{\nabla\phi:\phi\in C_c^\infty(\mathbb R^n;\mathbb C)\}}^{\,L^2}.
                                                               \tag{2.1}
\]
The symbol \(\mathcal S_\sigma\) denotes a closed subspace of \(L^2\), not the Schwartz class.

Define bounded operators on \(\mathcal H\) by
\[
\widehat{\mathbb Pv}(\xi)=P(\xi)\widehat v(\xi),\qquad
\widehat{\mathbb Qv}(\xi)=Q(\xi)\widehat v(\xi).
                                                               \tag{2.2}
\]
The boundedness follows from (1.5) and (1.2). Real fields remain real: their Fourier transforms satisfy \(\widehat v(-\xi)=\overline{\widehat v(\xi)}\), and the real matrices \(P,Q\) are even in \(\xi\).

**Theorem 2.1.** Every \(v\in\mathcal H\) has the unique orthogonal decomposition
\[
v=\mathbb Pv+\mathbb Qv,\qquad
\mathbb Pv\in\mathcal S_\sigma,\qquad \mathbb Qv\in\mathcal G,
\]
\[
\mathcal H=\mathcal S_\sigma\oplus\mathcal G,\qquad
\|v\|_2^2=\|\mathbb Pv\|_2^2+\|\mathbb Qv\|_2^2.             \tag{2.3}
\]
Both operators are self-adjoint projections. In particular,
\(\|\mathbb Pv\|_2,\|\mathbb Qv\|_2\leq\|v\|_2\).

**Proof.** The matrix identities (1.5), followed by the \(L^2\) Fourier identity, prove idempotence, self-adjointness, orthogonality and the norm equality.

Distributional differentiation in (1.2) shows that \(\operatorname{div}v=0\) is equivalent to
\(\xi\cdot\widehat v(\xi)=0\) almost everywhere. To justify the last step, \(\xi\cdot\widehat v\) is locally integrable by Cauchy–Schwarz on bounded sets; a locally integrable function represents the zero distribution exactly when it vanishes almost everywhere. Equation (1.4) now shows that the range of \(\mathbb P\) is precisely \(\mathcal S_\sigma\).

For \(\phi\in C_c^\infty\), its gradient has transform \(2\pi i\xi\widehat\phi\), so \(\mathbb Q\nabla\phi=\nabla\phi\). By continuity, \(\mathcal G\) lies in the range of \(\mathbb Q\), which is closed because \(\mathbb Q\) is a bounded projection.

For the reverse inclusion, approximate \(\widehat v\) in \(L^2\) by vector functions \(a_j\) smooth and compactly supported away from zero. Such approximation follows by first cutting off \(|\xi|<1/j\) and \(|\xi|>j\), whose \(L^2\) tails tend to zero, then using smooth compactly supported approximation in the remaining open annulus. Set
\[
\widehat q_j(\xi)=\frac{\xi\cdot a_j(\xi)}{2\pi i|\xi|^2}.
\]
This is smooth and compactly supported away from zero. Its inverse transform \(q_j\) is Schwartz, by repeated integration by parts in (1.1). Moreover,
\[
\widehat{\nabla q_j}=Q(\xi)a_j(\xi)\longrightarrow Q(\xi)\widehat v(\xi)
\quad\text{in }L^2.
\]
Choose \(\eta\in C_c^\infty\) equal to one near zero and set \(\eta_R(x)=\eta(x/R)\). Then
\[
\nabla(\eta_Rq_j)-\nabla q_j
=(\eta_R-1)\nabla q_j+R^{-1}(\nabla\eta)(x/R)q_j
\longrightarrow0
\quad\text{in }L^2
\]
for each \(j\). Dominated convergence handles the first term, and the second has norm at most \(R^{-1}\|\nabla\eta\|_\infty\|q_j\|_2\). Thus each \(\nabla q_j\) belongs to \(\mathcal G\), and so does its limit \(\mathbb Qv\). Finally the orthogonal decomposition has unique summands, since a vector in both orthogonal subspaces has zero norm. \(\square\)

The same spaces can be described without Fourier coordinates:
\[
v\in\mathcal S_\sigma
\quad\Longleftrightarrow\quad
\int v\cdot\overline{\nabla\phi}\,dx=0
\quad\text{for every }\phi\in C_c^\infty.
                                                               \tag{2.4}
\]
This is exactly the definition of vanishing distributional divergence, with a minus sign from integration by parts. It also proves directly that \(\mathcal S_\sigma=\mathcal G^\perp\).

### Recovering an actual pressure potential

It is the gradient of pressure that enters momentum. A square-integrable gradient need not have a square-integrable potential.

**Proposition 2.2.** For each \(v\in\mathcal H\), there is a tempered distribution \(q\) such that
\[
\nabla q=\mathbb Qv,\qquad \Delta q=\operatorname{div}v.       \tag{2.5}
\]
It is unique up to a spatial constant among distributional potentials with this gradient.

**Proof.** Away from zero, the required Fourier expression is
\[
a(\xi)=\frac{\xi\cdot\widehat v(\xi)}{2\pi i|\xi|^2}.          \tag{2.6}
\]
To define it for every \(L^2\) field, including at low frequency in dimension two, choose \(\chi\in C_c^\infty\) equal to one near zero. Define
\[
\langle\widehat q,\varphi\rangle
=\int_{\mathbb R^n}a(\xi)
       [\varphi(\xi)-\varphi(0)\chi(\xi)]\,d\xi,
\qquad \varphi\text{ Schwartz}.                             \tag{2.7}
\]
This is a bilinear distribution pairing, with no complex conjugation.
Near zero the bracket is bounded by \(C_\varphi|\xi|\), while
\(|a(\xi)|\leq|\widehat v(\xi)|/(2\pi|\xi|)\). Cauchy–Schwarz on a bounded ball makes the product integrable. Away from that ball, the factor \(1/|\xi|\) is bounded and the bracket is square-integrable and rapidly decreasing outside a compact set. Cauchy–Schwarz applies again. These same estimates bound the pairing by finitely many Schwartz seminorms of \(\varphi\), times \(\|v\|_2\), so (2.7) is tempered.

Multiplication by \(2\pi i\xi_j\) in (2.7) removes the subtracted term because \((\xi_j\varphi)(0)=0\). It gives
\[
2\pi i\xi_j\widehat q
=\frac{\xi_j\,\xi\cdot\widehat v}{|\xi|^2}
=\widehat{(\mathbb Qv)_j}.
\]
Thus \(\nabla q=\mathbb Qv\). Taking a divergence and using \(\operatorname{div}\mathbb Pv=0\) proves the second equation.

If two potentials have the same gradient, their difference \(h\) has all distributional first derivatives zero. Convolve \(h\) with a compactly supported smooth approximate identity. Every convolution has zero ordinary gradient and is constant on connected \(\mathbb R^n\). Passing to the distributional limit shows that \(h\) annihilates every test function of integral zero. Fixing one test function of integral one then shows \(\langle h,\phi\rangle=c\int\phi\) for a fixed \(c\). Hence \(h\) is a constant distribution. \(\square\)

For smooth fields whose gradients are in \(L^2\), this is the usual pressure freedom \(q(x)\mapsto q(x)+c\). In an evolution, the constant may depend on time. Formula (2.7) selects one representative; the recovered gradient is independent of the choice of \(\chi\).

### Derivatives and Sobolev norms

For real \(s\), define
\[
\|v\|_{H^s}^2
=\int_{\mathbb R^n}(1+4\pi^2|\xi|^2)^s|\widehat v(\xi)|^2\,d\xi,
                                                               \tag{2.8}
\]
on the tempered distributions whose transforms are represented by functions with this finite integral. Pointwise orthogonality gives
\[
\|v\|_{H^s}^2=\|\mathbb Pv\|_{H^s}^2+\|\mathbb Qv\|_{H^s}^2.
                                                               \tag{2.9}
\]
Multiplication by \(P(\xi)\) or \(Q(\xi)\) commutes with multiplication by \(2\pi i\xi_j\) and by \(-4\pi^2|\xi|^2\). Consequently \(\mathbb P\) and \(\mathbb Q\) commute with each spatial derivative and with the Laplacian on their natural Sobolev domains. For example, \(\partial_j\mathbb Pv=\mathbb P\partial_jv\) in \(H^{s-1}\) for \(v\in H^s\). This conclusion uses the stated domains; it does not require multiplication of an arbitrary distribution by a nonsmooth symbol at zero.

## 3. The periodic box and its constant mode

Write
\[
\mathbb T_L^n=\mathbb R^n/(L_1\mathbb Z\times\cdots\times L_n\mathbb Z),
\quad V=\prod_{j=1}^nL_j,\quad
\kappa_k=(k_1/L_1,\ldots,k_n/L_n),\quad k\in\mathbb Z^n.
\]
Integration uses ordinary \(dx\) over the box \(\prod_j[0,L_j]\), so its total volume is \(V\). Define
\[
\widehat v_k=\frac1V\int_{\mathbb T_L^n}v(x)e^{-2\pi i\kappa_k\cdot x}\,dx.
                                                               \tag{3.1}
\]
The Fourier-series identities proved in Section 8 are
\[
v=\sum_{k\in\mathbb Z^n}\widehat v_k e^{2\pi i\kappa_k\cdot x}
\quad\text{in }L^2,\qquad
\|v\|_2^2=V\sum_k|\widehat v_k|^2.                           \tag{3.2}
\]
The zero coefficient is the spatial average \(V^{-1}\int v\).

**Theorem 3.1.** Set
\[
\widehat{(\mathbb P_Lv)}_k=
\begin{cases}
\left(I-\dfrac{\kappa_k\kappa_k^T}{|\kappa_k|^2}\right)\widehat v_k,&k\ne0,\\
\widehat v_0,&k=0,
\end{cases}
\]
\[
\widehat{(\mathbb Q_Lv)}_k=
\begin{cases}
\dfrac{\kappa_k\kappa_k^T}{|\kappa_k|^2}\widehat v_k,&k\ne0,\\
0,&k=0.
\end{cases}                                                  \tag{3.3}
\]
These are orthogonal projections onto, respectively, the distributionally divergence-free fields and the gradients of periodic \(H^1\) functions. Every \(v\in L^2(\mathbb T_L^n;\mathbb C^n)\) has the unique decomposition
\[
v=\mathbb P_Lv+\nabla q,\qquad \int_{\mathbb T_L^n}q\,dx=0,
                                                               \tag{3.4}
\]
where
\[
\widehat q_0=0,\qquad
\widehat q_k=\frac{\kappa_k\cdot\widehat v_k}{2\pi i|\kappa_k|^2}
\quad(k\ne0).                                                \tag{3.5}
\]
Writing \(L_{\max}=\max_jL_j\), the bounds are
\[
\|\nabla q\|_2\leq\|v\|_2,\qquad
\|q\|_2\leq\frac{L_{\max}}{2\pi}\|\nabla q\|_2.              \tag{3.6}
\]

**Proof.** Use the matrices of Section 1 at each \(\kappa_k\ne0\). At \(k=0\), all first derivatives vanish, so incompressibility imposes no condition on \(\widehat v_0\). A periodic gradient has zero constant coefficient. These observations give exactly (3.3), including the zero mode.

Parseval proves orthogonality and boundedness. Since \(|\kappa_k|\geq1/L_{\max}\) for \(k\ne0\), (3.5) and (3.2) give
\[
V\sum_{k\ne0}|\widehat q_k|^2
\leq\frac{L_{\max}^2}{4\pi^2}
V\sum_{k\ne0}4\pi^2|\kappa_k|^2|\widehat q_k|^2.
\]
The latter sum is \(\|\mathbb Q_Lv\|_2^2\leq\|v\|_2^2\). Thus \(q\in H^1\), and differentiating its series proves \(\nabla q=\mathbb Q_Lv\). Conversely a periodic \(H^1\) gradient has transform \(2\pi i\kappa_k\widehat q_k\), so \(\mathbb Q_L\) keeps it. If a periodic gradient is zero, all nonzero Fourier coefficients of its potential vanish; the mean-zero condition removes the last coefficient. This proves uniqueness. \(\square\)

Periodic Sobolev norms use
\[
\|v\|_{H^s(\mathbb T_L^n)}^2
=V\sum_k(1+4\pi^2|\kappa_k|^2)^s|\widehat v_k|^2.
                                                               \tag{3.7}
\]
The exact orthogonal norm identity and derivative commutation from (2.9) hold with these weights as well, by applying the same matrix identities to every summand.

## 4. Projected momentum and full pressure recovery

Let \(D\) be either \(\mathbb R^n\) or \(\mathbb T_L^n\). Denote its two projections by \(\mathbb P_D,\mathbb Q_D\). Suppose
\[
u\in C^1([0,T];L^2(D))\cap C([0,T];H^2(D)),
\quad N=(u\cdot\nabla)u\in C([0,T];L^2(D)),
\quad f\in C([0,T];L^2(D)).
                                                               \tag{4.1}
\]
The notation \(N\) stands for the full vector with components
\(N_i=\sum_j u_j\partial_j u_i\). It introduces no change to the nonlinearity.

**Theorem 4.1.** Under (4.1), with divergence-free initial velocity, the projected equation
\[
\partial_tu-\nu\Delta u=\mathbb P_D(f-N)                    \tag{4.2}
\]
implies that \(u(t)\) remains divergence-free. A pressure is recovered by
\[
\nabla p=\mathbb Q_D(f-N),\qquad
\Delta p=\operatorname{div}f-\operatorname{div}N.             \tag{4.3}
\]
With this pressure, the complete equation
\[
\partial_tu+N+\nabla p-\nu\Delta u=f                         \tag{4.4}
\]
holds in \(L^2\). Conversely, a divergence-free solution of (4.4) satisfying (4.1), with an \(L^2\) pressure gradient (and periodic pressure in the periodic case), satisfies (4.2).

**Proof.** Apply \(\mathbb Q_D\) to (4.2) and use its commutation with \(\Delta\). The field \(z=\mathbb Q_Du\) satisfies
\[
z_t-\nu\Delta z=0,\qquad z(0)=0.
\]
The \(L^2\) product with \(z\), justified by (4.1), gives
\[
\frac12\frac{d}{dt}\|z\|_2^2+\nu\|\nabla z\|_2^2=0.
\]
Here integration by parts can also be read directly from (1.2) or (3.2): the term \(-\langle\Delta z,z\rangle\) equals the integral or sum of \(4\pi^2|\xi|^2|\widehat z|^2\). Integrating in time proves \(z=0\).

Proposition 2.2 or Theorem 3.1 supplies a potential for \(\mathbb Q_D(f-N)\); the potential is mean zero on the torus. Add the two orthogonal components of \(f-N\) to obtain (4.4).

For the converse, divergence-free \(u\) implies
\(\mathbb P_Du_t=u_t\) and \(\mathbb P_D\Delta u=\Delta u\).
An \(L^2\) gradient is annihilated by \(\mathbb P_D\). On the torus this was proved in Theorem 3.1. In the whole space, if \(g=\nabla p\in L^2\), its mixed derivatives obey \(\partial_i g_j=\partial_j g_i\). Fourier transformation gives \(\xi_i\widehat g_j=\xi_j\widehat g_i\) almost everywhere. At each nonzero \(\xi\), choose a nonzero coordinate of \(\xi\); these equalities show that \(\widehat g\) is parallel to \(\xi\). Therefore \(P(\xi)\widehat g=0\). Applying \(\mathbb P_D\) to (4.4) proves (4.2). \(\square\)

For smooth incompressible \(u\), the divergence in (4.3) is exactly
\[
\operatorname{div}N
=\sum_{i,j}(\partial_i u_j)(\partial_j u_i),
                                                               \tag{4.5}
\]
as proved component by component in the preceding lesson. Thus pressure still records the original nonlinear acceleration and the divergence of the external force.

For a periodic solution, integrating (4.4) over the cell gives
\[
\frac{d}{dt}\widehat u_0(t)=\widehat f_0(t),\qquad
\widehat u_0(t)=\widehat u_0(0)+\int_0^t\widehat f_0(s)\,ds.
                                                               \tag{4.6}
\]
Indeed each derivative integrates to zero on opposite faces, and
\(N_i=\sum_j\partial_j(u_ju_i)\) when \(\operatorname{div}u=0\).
The common factor \(1/V\) is present in every average. A nonzero mean force accelerates the mean velocity; a periodic pressure gradient cannot cancel it.

## 5. The Euler bilinear operator, with viscosity and force retained

For real divergence-free fields on \(\mathbb R^n\), define
\[
B(u,v)=-\frac12\mathbb P\bigl((u\cdot\nabla)v+(v\cdot\nabla)u\bigr).
                                                               \tag{5.1}
\]
The factor \(1/2\) makes this a symmetric bilinear operator. Substitution gives \(B(u,u)=-\mathbb P((u\cdot\nabla)u)\), so the projected Navier–Stokes equation is exactly
\[
u_t=\nu\Delta u+B(u,u)+\mathbb Pf.                           \tag{5.2}
\]

Here is a precise domain on which each term in (5.1) is square-integrable. Let \(s>n/2\) and \(s\geq1\), and set
\[
C_{n,s}=\left(\int_{\mathbb R^n}
(1+4\pi^2|\xi|^2)^{-s}\,d\xi\right)^{1/2}<\infty.
\]
The integral is finite because its radial tail is bounded by a constant times \(\int_1^\infty r^{n-1-2s}dr\). Fourier inversion and Cauchy–Schwarz give
\[
\|u\|_\infty\leq\|\widehat u\|_1\leq C_{n,s}\|u\|_{H^s}.
                                                               \tag{5.3}
\]
The inverse Fourier integral is uniformly convergent and represents \(u\), since its \(L^2\) transform is \(\widehat u\). Consequently
\[
\|B(u,v)\|_2
\leq\frac{C_{n,s}}2
\bigl(\|u\|_{H^s}\|\nabla v\|_2+
      \|v\|_{H^s}\|\nabla u\|_2\bigr).                       \tag{5.4}
\]
This proves a continuous bilinear map from two divergence-free \(H^s\) spaces to divergence-free \(L^2\).

**Proposition 5.1.** For real divergence-free \(u\in H^s(\mathbb R^n)\) with these \(s\),
\[
\langle B(u,u),u\rangle_{L^2}=0.                            \tag{5.5}
\]

**Proof.** First take a smooth divergence-free \(u\) with \(u,\nabla u\in L^2\) and \(u\) bounded. By self-adjointness and \(\mathbb Pu=u\),
\[
\langle B(u,u),u\rangle=-\int ((u\cdot\nabla)u)\cdot u.
\]
The integral is absolutely convergent, bounded in absolute value by
\(\|u\|_\infty\|\nabla u\|_2\|u\|_2\). With the cutoffs \(\eta_R\) used earlier,
\[
\int\eta_R ((u\cdot\nabla)u)\cdot u
=-\frac12\int |u|^2u\cdot\nabla\eta_R.
\]
The right side has magnitude at most
\(\|\nabla\eta\|_\infty\|u\|_\infty\|u\|_2^2/(2R)\), which tends to zero. Dominated convergence on the left proves the identity.

For general \(u\in H^s\), take smooth scalar Fourier cutoffs equal to one on expanding balls and multiply \(\widehat u\) by them. They preserve \(\xi\cdot\widehat u=0\), produce smooth fields, and converge in \(H^s\) by dominated convergence. Estimate (5.4) makes the corresponding bilinear outputs converge in \(L^2\), while the fields themselves converge in \(L^2\). Passing to the inner products proves (5.5). \(\square\)

Thus the nonlinear cancellation, diffusion loss and force work remain separate exact terms:
\[
\frac12\frac{d}{dt}\|u\|_2^2
+\nu\|\nabla u\|_2^2
=\langle\mathbb Pf,u\rangle=\langle f,u\rangle.              \tag{5.6}
\]
The last equality uses \(\mathbb Pu=u\), not an assumption that \(f\) is divergence-free.

For the incompressible Euler equation, the full momentum equation is instead
\[
u_t+(u\cdot\nabla)u+\nabla p=f,\qquad \operatorname{div}u=0.
                                                               \tag{5.7}
\]
This is a different equation with zero viscosity. Its projection is
\(u_t=B(u,u)+\mathbb Pf\), and its pressure gradient is still
\(\mathbb Q(f-(u\cdot\nabla)u)\). The proof is the same addition of the two
orthogonal components; if only initial incompressibility is assumed,
applying \(\mathbb Q\) to the projected equation gives
\((\mathbb Qu)_t=0\), so it persists. The energy proof above gives
\(\frac12\frac{d}{dt}\|u\|_2^2=\langle f,u\rangle\) in its stated
integrability class. Taking the component curl as in the first lesson
gives, in three dimensions,
\[
\omega_t+(u\cdot\nabla)\omega-(\omega\cdot\nabla)u
=\nabla\times f.
\]
Each identity follows directly from (5.7); none asserts convergence of
viscous solutions as \(\nu\) tends to zero.

## 6. The heat operator and the integral equation

For \(\nu>0\), define on \(L^2(\mathbb R^n)\)
\[
\widehat{S_\nu(t)v}(\xi)=e^{-4\pi^2\nu t|\xi|^2}\widehat v(\xi),
\qquad t\geq0.                                               \tag{6.1}
\]
On the torus replace \(\xi\) by \(\kappa_k\) in each coefficient. In either setting \(S_\nu(t)\) is a contraction, \(S_\nu(t+s)=S_\nu(t)S_\nu(s)\), and \(S_\nu(t)v\to v\) in \(L^2\) as \(t\downarrow0\). These facts follow, respectively, from \(0<e^{-4\pi^2\nu t|\xi|^2}\leq1\), multiplication of exponentials, and dominated convergence applied to the squared Fourier difference. The operator commutes with \(\mathbb P_D\).

For \(v\in H^2\), differentiating the multiplier gives
\[
\frac{d}{dt}S_\nu(t)v=\nu\Delta S_\nu(t)v
\quad\text{in }L^2,
                                                               \tag{6.2}
\]
including the right derivative at zero. The difference quotients are dominated by a constant times \(|\xi|^2|\widehat v|\), which is square-integrable.

**Proposition 6.1.** Under (4.1), equation (4.2) is equivalent to
\[
u(t)=S_\nu(t)u_0+
\int_0^t S_\nu(t-s)\mathbb P_D
\bigl(f(s)-(u(s)\cdot\nabla)u(s)\bigr)\,ds.                  \tag{6.3}
\]
The integral is an \(L^2\) integral of a continuous function. The equivalence here is restricted to (4.1); it does not assert that an arbitrary \(L^2\) integral solution has that regularity.

**Proof.** Let \(F=\mathbb P_D(f-N)\). Cut off Fourier space to \(|\xi|\leq M\), or Fourier series to \(|\kappa_k|\leq M\), and denote this orthogonal truncation by \(E_M\). On its range the Laplacian is bounded. The equation for \(E_Mu\) is therefore an ordinary differentiable identity in a Hilbert space. Differentiating \(S_\nu(t-s)E_Mu(s)\) in \(s\) gives \(S_\nu(t-s)E_MF(s)\). Integration from zero to \(t\) gives (6.3) with \(E_M\) on every term.

As \(M\to\infty\), the initial and solution terms converge in \(L^2\). The integral difference is bounded by
\(\int_0^t\|(I-E_M)F(s)\|_2ds\), which tends to zero by dominated convergence, since \(F\) is continuous on a compact time interval. This proves (6.3).

Conversely apply \(E_M\) to (6.3). Boundedness of the truncated Laplacian permits differentiation under the integral, giving
\((E_Mu)_t-\nu\Delta E_Mu=E_MF\).
Assumptions (4.1) allow all three terms to converge in \(L^2\) to their untruncated versions. This proves (4.2). \(\square\)

The periodic zero mode in (6.1) has multiplier one for every time. Taking that coefficient in (6.3) reproduces (4.6). Viscosity does not damp a spatially constant velocity.

## 7. Exercises with complete solutions

**Exercise 1. Resolve a single wave.** On \(\mathbb R^2\), consider the smooth periodic field
\(v(x)=a\cos(2\pi k\cdot x)\), with \(k=(2,1)\) and \(a=(1,3)\). Use the periodic, rather than whole-space \(L^2\), projection. Find \(\mathbb Pv\), \(\mathbb Qv\) and the mean-zero pressure potential.

**Solution.** On the unit torus, \(k\cdot a=5=|k|^2\). Thus \(Qa=k=(2,1)\), \(Pa=(-1,2)\), and
\[
\mathbb Pv=(-1,2)\cos(2\pi k\cdot x),\qquad
\mathbb Qv=(2,1)\cos(2\pi k\cdot x).
\]
The mean-zero potential is
\[
q(x)=\frac1{2\pi}\sin(2\pi k\cdot x).
\]
Its gradient is exactly \(\mathbb Qv\). The two vector amplitudes have squared lengths \(5\) and \(5\), summing to \(|a|^2=10\). Since the squared cosine has integral \(1/2\) on the unit torus, the two projected squared \(L^2\) norms are \(5/2\) and \(5/2\), summing to \(\|v\|_2^2=5\). This field is not in \(L^2(\mathbb R^2)\); the periodic domain is essential.

**Exercise 2. A mean force.** On \(\mathbb T_L^n\), take spatially constant data \(u_0=a\) and \(f(x,t)=b(t)\), with \(b\) smooth. Find a solution and prove that a periodic pressure cannot keep \(u\) identically equal to \(a\) when \(b\) is nonzero.

**Solution.** Set
\[
u(x,t)=a+\int_0^t b(s)\,ds,\qquad p=0.
\]
All spatial derivatives vanish, so the complete momentum equation reduces to \(u_t=b\), and divergence is zero. If instead \(u=a\) for all time, momentum would require \(\nabla p=b(t)\). Its spatial integral is zero for periodic \(p\), whereas the integral of \(b(t)\) is \(Vb(t)\). Hence \(b(t)=0\) would be necessary.

**Exercise 3. A pressure outside \(L^2\).** In \(\mathbb R^n\), \(n\geq2\), choose a real even smooth cutoff \(\rho\), equal to one for \(|\xi|\leq1\) and zero for \(|\xi|\geq2\). Set
\[
\widehat q(\xi)=\rho(\xi)|\xi|^{-n/2},\qquad
\widehat v(\xi)=2\pi i\xi\,\widehat q(\xi).
\]
Prove that \(v\in L^2\) and \(v=\nabla q\), but no addition of a constant makes \(q\) an \(L^2\) function.

**Solution.** Near zero, \(\widehat q\) is locally integrable because its radial absolute integral is proportional to \(\int_0^1r^{n/2-1}dr<\infty\). It therefore defines a tempered distribution. The squared norm of \(\widehat v\) near zero has radial integral
\(4\pi^2|\mathbb S^{n-1}|\int_0^1r\,dr<\infty\).
Outside that ball the cutoff makes it square-integrable. Plancherel supplies \(v\in L^2\), and Fourier differentiation gives \(v=\nabla q\). Reality follows from the conjugate symmetry of these transforms.

In contrast,
\(\int_{|\xi|\leq1}|\widehat q|^2d\xi
=|\mathbb S^{n-1}|\int_0^1dr/r=\infty\).
Adding a spatial constant changes the Fourier distribution only by a multiple of \(\delta_0\). Away from zero the displayed function is unchanged; an \(L^2\) transform agreeing there would still have the divergent integral over the punctured unit ball. Thus no such constant repairs \(L^2\) integrability.

**Exercise 4. A divergence-free force representative.** Under the hypotheses of Theorem 4.1, replace \(f\) by \(\mathbb P_Df\). Find a pressure change that preserves the velocity equation.

**Solution.** Choose \(\phi\) with \(\nabla\phi=\mathbb Q_Df\), using Proposition 2.2 or Theorem 3.1. Write \(f=\mathbb P_Df+\nabla\phi\) in the full momentum equation and subtract \(\nabla\phi\) from both sides. The same \(u\), with pressure \(p-\phi\), then has force \(\mathbb P_Df\). The projected force produces the same work against divergence-free \(u\):
\(\langle\mathbb P_Df,u\rangle=\langle f,\mathbb P_Du\rangle=\langle f,u\rangle\).
This comparison does not preserve compact support of the force or pressure in general; those properties must be checked for the actual fields.

**Exercise 5. Changing the viscosity without losing the other factors.** Suppose \((u,p,f)\) solves the equation at viscosity \(\nu>0\), in physical variables \((x,s)\). Define a new time \(\tau=\nu s\), with space unchanged. Find fields at viscosity one and prove the transformation, including the initial velocity and force.

**Solution.** Define
\[
v(x,\tau)=\nu^{-1}u(x,\tau/\nu),\quad
q(x,\tau)=\nu^{-2}p(x,\tau/\nu),\quad
g(x,\tau)=\nu^{-2}f(x,\tau/\nu).                              \tag{7.1}
\]
Then
\[
v_\tau=\nu^{-2}u_s,\quad
(v\cdot\nabla)v=\nu^{-2}(u\cdot\nabla)u,\quad
\nabla q=\nu^{-2}\nabla p,\quad
\Delta v=\nu^{-1}\Delta u.
\]
Multiplying the original momentum equation by \(\nu^{-2}\) proves
\(v_\tau+(v\cdot\nabla)v+\nabla q-\Delta v=g\).
Also \(\operatorname{div}v=\nu^{-1}\operatorname{div}u=0\), and
\(v(x,0)=\nu^{-1}u_0(x)\). The interval \([0,T]\) becomes \([0,\nu T]\). The inverse is \(u(x,s)=\nu v(x,\nu s)\), \(p(x,s)=\nu^2q(x,\nu s)\), \(f(x,s)=\nu^2g(x,\nu s)\). Spatial supports are unchanged; a force derivative with \(b\) time derivatives has the factor \(\nu^{-2-b}\).

**Source comparison for Exercise 5.** The author TeX of [T, v3, Section 1, paragraph immediately after the displayed Navier–Stokes system] prints
\[
\widetilde u(t,x)=\nu u(\nu t,x),\qquad
\widetilde p(t,x)=\nu p(\nu t,\nu x)
                                                               \tag{7.2}
\]
as its change to viscosity one. With the original \(u,p\) solving the unforced equation at viscosity \(\nu\), the left side of the purported unit-viscosity equation instead equals
\[
\nu(\nu^2-1)\Delta u(\nu t,x)
+\nu^2\bigl[\nabla p(\nu t,\nu x)-\nabla p(\nu t,x)\bigr].
                                                               \tag{7.3}
\]
Indeed its time and advection terms are \(\nu^2u_s\) and \(\nu^2(u\cdot\nabla)u\), its diffusion term is \(-\nu\Delta u\), and its pressure gradient is \(\nu^2\nabla p(\nu t,\nu x)\). Substitution of the original equation gives (7.3). It is not the zero equation identity required of a change of variables. As a direct test on the unit periodic box, \(u(s,x)=e^{-4\pi^2\nu s}(\sin(2\pi x_2),0,0)\), \(p=0\), has zero advection and solves the equation at \(\nu\); (7.3) is nonzero for \(\nu\ne1\). This test is periodic, not Schwartz data on \(\mathbb R^3\).

Formula (7.1) proves the required viscosity comparison on the original whole-space class as well, without using that periodic test. We have identified a displayed rescaling error and supplied its replacement identity; no conclusion about the later averaged-equation theorem follows from that error. Throughout this lesson the physical equation retains its original \(\nu\).

## 8. Fourier facts used in the proofs

This section supplies the transform and series identities so that the fluid decomposition does not rest on an unproved inversion step.

### Whole-space inversion and the \(L^2\) identity

For a Schwartz function \(h\), repeated integration by parts gives
\(\widehat{\partial_jh}=2\pi i\xi_j\widehat h\) and
\(\widehat{x_jh}=-(2\pi i)^{-1}\partial_{\xi_j}\widehat h\).
The integrands and their derivatives are integrable, so differentiating under the integral is valid. Combining these identities shows that \(\widehat h\) is Schwartz.

The Gaussian kernel
\[
K_\varepsilon(x)=(4\pi\varepsilon)^{-n/2}
e^{-|x|^2/(4\varepsilon)},\qquad \varepsilon>0,
\]
has integral one and transform \(e^{-4\pi^2\varepsilon|\xi|^2}\).
For completeness, the one-dimensional Gaussian integral is obtained by squaring \(\int e^{-x^2}dx\), using polar coordinates in the plane, and obtaining \(\pi\). To compute the transform \(F(\xi)\) of \(e^{-x^2/(4\varepsilon)}\), differentiate under its integral. Integration by parts with \(x e^{-x^2/(4\varepsilon)}=-2\varepsilon\partial_xe^{-x^2/(4\varepsilon)}\) gives
\(F'(\xi)=-8\pi^2\varepsilon\xi F(\xi)\).
The value \(F(0)=\sqrt{4\pi\varepsilon}\) determines
\(F(\xi)=\sqrt{4\pi\varepsilon}\,e^{-4\pi^2\varepsilon\xi^2}\).
Taking products gives the \(n\)-dimensional formula, and the same computation with the inverse sign gives its inverse transform.

Fubini now gives, for Schwartz \(h\),
\[
\int e^{2\pi i x\cdot\xi}e^{-4\pi^2\varepsilon|\xi|^2}
       \widehat h(\xi)\,d\xi
=\int K_\varepsilon(x-y)h(y)\,dy.                           \tag{8.1}
\]
Absolute integrability follows by bounding the double integral by
\(\|h\|_1\int e^{-4\pi^2\varepsilon|\xi|^2}d\xi\).
As \(\varepsilon\downarrow0\), the right side tends to \(h(x)\): near \(y=x\) use uniform continuity, and outside any fixed ball about \(x\) the Gaussian mass tends to zero by the substitution \(z=(x-y)/\sqrt\varepsilon\). The left side tends by dominated convergence to the inverse transform of \(\widehat h\), since \(\widehat h\in L^1\). Thus
\[
h(x)=\int e^{2\pi i x\cdot\xi}\widehat h(\xi)\,d\xi.
                                                               \tag{8.2}
\]
For Schwartz \(h,k\), substitute (8.2) into
\(\int h\overline{k}\) and apply Fubini, justified by
\(\|\widehat h\|_1\|k\|_1<\infty\). This gives
\[
\int h(x)\overline{k(x)}\,dx
=\int\widehat h(\xi)\overline{\widehat k(\xi)}\,d\xi.         \tag{8.3}
\]

Smooth compactly supported functions are dense in \(L^2\). One way to see the needed approximation is to truncate a function in space and in value, approximate the resulting bounded finite-support function by finite linear combinations of indicators of boxes in \(L^2\), and convolve these with a smooth compactly supported approximate identity. Translation changes the volume of the symmetric difference of a box with itself by a quantity tending to zero. Thus convolution tends to each box indicator in \(L^2\), while producing smooth compactly supported functions. The approximation by box simple functions follows from regularity of Lebesgue measure, by approximating a finite-measure set in measure by finite unions of boxes.

Equation (8.3) therefore extends the Fourier transform uniquely as an isometry of \(L^2\) into \(L^2\). Its range is closed. It contains all Schwartz functions because (8.2), applied with both signs, makes the inverse transform an inverse on that class. The range is dense and closed, hence all of \(L^2\). This proves unitarity, (1.2), and the inverse transform used above.

Distributional differentiation follows from the definition of a derivative and the established Schwartz identities. If the multiplier \(2\pi i\xi_j\widehat v\) is in \(L^2\), its inverse transform is the weak derivative, by testing against Schwartz functions and using (8.3). The same argument applies to the Laplacian. These observations justify the Sobolev uses in Sections 2–6.

### Periodic completeness and Parseval

Direct integration in each coordinate gives
\[
\int_{\mathbb T_L^n}
e^{2\pi i\kappa_k\cdot x}e^{-2\pi i\kappa_\ell\cdot x}\,dx
=V\,\mathbf1_{k=\ell}.                                      \tag{8.4}
\]
To prove completeness, first work on one circle of length one and define
\[
F_N(t)=\frac1N\left|\sum_{j=0}^{N-1}e^{2\pi ijt}\right|^2
=\sum_{|k|<N}\left(1-\frac{|k|}{N}\right)e^{2\pi ikt}.
\]
The second equality follows by counting the \(N-|k|\) ordered pairs with difference \(k\). Therefore \(F_N\geq0\) and its integral is one. At distance at least \(\delta>0\) from the integers, the geometric-series formula gives
\[
F_N(t)=\frac{\sin^2(\pi Nt)}{N\sin^2(\pi t)}
\leq\frac1{N\sin^2(\pi\delta)}
\quad(0<\delta\leq1/2).
\]
Thus its mass away from zero tends to zero.

On the actual box use the kernel
\[
\mathcal F_N(x)=V^{-1}\prod_{j=1}^n F_N(x_j/L_j).
\]
It is nonnegative, integrates to one, and has mass tending to zero outside any fixed coordinate neighborhood of zero on the torus. Periodic convolution with this kernel is a trigonometric polynomial. For a continuous periodic function it converges uniformly to that function: use uniform continuity near zero and the vanishing exterior mass elsewhere.

Continuous periodic functions are dense in \(L^2\). For example, approximate indicators of boxes on the torus by continuous functions which differ only in boundary strips of arbitrarily small measure; box simple functions are dense by the same measure-regularity argument used above. Hence trigonometric polynomials are dense in \(L^2\).

It follows that \(V^{-1/2}e^{2\pi i\kappa_k\cdot x}\) is a complete orthonormal family. The orthogonal projections onto finite frequency sets converge in \(L^2\): first approximate by a polynomial, then use the fact that an orthogonal projection has norm at most one. The finite Pythagorean identity passes to the limit and gives (3.2), with its factor \(V\). Integration by parts gives the derivative multipliers \(2\pi i(\kappa_k)_j\); testing and \(L^2\) convergence extend them to weak derivatives. This completes the Fourier ingredients of both decompositions.

## Reference

[T] Terence Tao, *Finite time blowup for an averaged three-dimensional Navier–Stokes equation*, [arXiv:1402.0290v3](https://arxiv.org/abs/1402.0290v3), 1 April 2015. Section 1 defines the Leray projection, the symmetric Euler bilinear operator, the cancellation identity and the integral equation. The present lesson proves those preliminary operator statements and supplies its own force, viscosity, domain and zero-mode comparisons. Exercise 5 identifies the displayed rescaling issue in that exact source version. The paper's averaged-equation construction is not proved or invoked here.
