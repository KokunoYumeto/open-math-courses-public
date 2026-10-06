# Flat transport traces and the norm boundary limit

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

This reading supplies the complete flat-transport example used in the first spectral lesson. It retains the course's existing shell, trace and transport arguments, including surjectivity of every flat trace, the exact distance to vanishing tails, both resolvent signs and arbitrary approaches within either half-plane. Its inputs are the proved local measure, Fourier, elementary-function and Banach-valued integration readings; it does not require any later AN-06 lesson.

Agmon's [*Limiting Absorption Principle for Long Range Potentials*](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2020/08/AGMON.pdf), lectures of July 1978 based on Karl Gustafson's notes and reworked by Michael Taylor, Section 1, (1.5)–(1.9), also treats these shell spaces. The notes' ball norm is equivalent to the shell norm below; all constants, duality assertions and transport refinements used here have the following complete programme proofs. No general perturbed limiting-absorption theorem is an input.

For the Hilbert-valued integrals and their norm, measurability and limit rules, read [the complete integral construction](hilbert-valued-integration.md#bochner-integral). [Approximation and convolution](euclidean-approximation-and-convolution.md#mollification) supplies compact smooth density with controlled support. [Elementary exponential and trigonometric calculus](elementary-functions-and-cutoffs.md#scalar-exponential) supplies the scalar integrations, difference bounds and oscillatory factors. We use inner products linear in the first variable. When the transverse dimension is zero, the slice Hilbert space is the scalar field.

<a id="transport-shell-duality"></a>

## 1. Measuring one shell at a time

Read the [Euclidean product and Fourier proofs](finite-derivative-l2.md#euclidean-products), in the order specified there, before this lesson. They prove the integration, smooth density, Gaussian transform and Plancherel facts used below. Multiplying that reading's forward Fourier transform by \((2\pi)^{-n/2}\) gives our unitary convention.

<a id="transport-hilbert-separation"></a>

**Hilbert representation and separation used below.** If \(C\) is a nonempty closed convex subset of a Hilbert space and \(d=\inf_{c\in C}\|x-c\|\), a minimizing sequence \(c_j\) satisfies
\[
 \|c_j-c_k\|^2
 =2\|x-c_j\|^2+2\|x-c_k\|^2
   -4\left\|x-\frac{c_j+c_k}{2}\right\|^2\longrightarrow0.
\]
The midpoint belongs to \(C\), so its squared distance is at least \(d^2\). Completeness and closedness give a minimizing point \(c\). For every \(z\in C\), compare \(c\) with \(c+t(z-c)\), \(0<t\le1\), expand the squared distance, divide by \(t\) and let \(t\downarrow0\). The result is \(\operatorname{Re}(x-c,z-c)\le0\). If \(x\notin C\), this separates \(x\) strictly from \(C\). If \(C\) is a closed linear subspace, use \(z=c+tv\) and \(z=c+itv\), with both signs of real \(t\), to obtain \(x-c\perp C\).

For a nonzero bounded linear functional \(\ell\), apply this projection to its closed kernel and to a vector outside that kernel. Normalize its nonzero orthogonal residual to a unit vector \(e\). For each \(x\), the vector \(x-\ell(x)e/\ell(e)\) lies in the kernel; orthogonality gives \(\ell(x)=\ell(e)(x,e)\). Thus \(\ell(x)=(x,\overline{\ell(e)}e)\), with representing-vector norm exactly \(\|\ell\|\). The zero functional has the zero representative, and testing their difference proves uniqueness. This supplies the Hilbert representation used on every shell. The same projection proof supplies the separation of closed convex subsets of a Hilbert space used in the onto criterion.

Set \(R_j=2^j\),

\[
 A_0=\{|x|<1\},\qquad
 A_j=\{2^{j-1}\leq|x|<2^j\}\quad(j\geq1).
\]

Boundary spheres have measure zero and play no role. Indeed a sphere of radius \(r>0\) is contained in every shell \(r-\delta<|x|<r+\delta\). The change-of-variables formula gives \(|B_R|=R^n|B_1|\), so the volumes of these shells tend to zero with \(\delta\). The unit ball has finite volume because it lies in a bounded cube. Define

\[
 \|f\|_B=\sum_{j\geq0}R_j^{1/2}\|f\|_{L^2(A_j)},
 \qquad
 \|u\|_{B^*}=\sup_{j\geq0}R_j^{-1/2}\|u\|_{L^2(A_j)}.
\]

The spaces \(B\) and \(B^*\) contain exactly the locally square-integrable functions with finite indicated norms. The star denotes the integral dual, not a Sobolev exponent.

**Theorem 1.1.** Both spaces are Banach. The pairing

\[
 (f,u)=\int f(x)\overline{u(x)}\,dx
\]

identifies every continuous linear functional on \(B\) with a unique \(u\in B^*\), and its norm is exactly \(\|u\|_{B^*}\). Smooth compactly supported functions are dense in \(B\).

**Proof.** Map \(f\) to the sequence \((R_j^{1/2}f|_{A_j})_j\). This is an isometric bijection from \(B\) to the \(\ell^1\) sum of the Hilbert spaces \(L^2(A_j)\); the corresponding \(\ell^\infty\) sum represents \(B^*\). For completeness, each component of a Cauchy sequence converges in its Hilbert space. Once two sequence indices are large, the norm of their difference is at most \(\varepsilon\). Pass to the component limit on each finite set of indices, then take the supremum over those finite sets. This bounds the sum, or the supremum, of the limiting difference by \(\varepsilon\). Comparing with one fixed sequence member gives a finite norm for the limit and proves convergence in the claimed space.

Cauchy–Schwarz on every shell proves \(|(f,u)|\leq\|f\|_B\|u\|_{B^*}\). Conversely, the restriction of a functional to each one-shell Hilbert space is represented by a unique vector \(u_j\); its norm bound says \(R_j^{-1/2}\|u_j\|_2\leq\|\ell\|\). Join these vectors into \(u\). Finite shell sums have the claimed representation, and their density in the \(\ell^1\) sum extends it to all \(B\). Testing with a unit vector supported in one shell, and taking the supremum over shells, proves the exact norm equality and uniqueness.

For density, first discard all shells beyond a finite index; their \(B\) norm tends to zero. The truncated function is supported in a fixed ball. Approximate it in \(L^2\) by smooth functions supported in a slightly larger ball. Only finitely many shells then occur, so their \(B\) norm is bounded by a fixed constant times the \(L^2\) error. \(\square\)

The same proof shows \(B\subset L^2\), since \(\|f\|_2\leq\sum_j\|f\|_{L^2(A_j)}\leq\|f\|_B\).

<a id="transport-vanishing-tails"></a>

## 2. The waves that carry no mass at infinity

Define \(B^*_0\) by the additional condition

\[
 R_j^{-1/2}\|u\|_{L^2(A_j)}\longrightarrow0.
\]

**Theorem 2.1.** For \(u\in B^*\),

\[
 \|u\|_{B^*}^2\leq
 \sup_{R\geq1}\frac1R\int_{|x|<R}|u|^2\,dx
 \leq4\|u\|_{B^*}^2.
\]

Moreover \(u\in B^*_0\) exactly when

\[
 \frac1R\int_{|x|<R}|u|^2\,dx\longrightarrow0.
\]

The space \(B^*_0\) is the \(B^*\)-norm closure of \(C_c^\infty\), and its continuous dual is \(B\) under the integral pairing.

**Proof.** For each \(j\), the shell integral divided by \(R_j\) is at most the ball integral with radius \(R_j\) divided by \(R_j\). This proves the first inequality. Choose \(j\) with \(R_{j-1}<R\leq R_j\), or \(j=0\) when \(R=1\). The ball is contained in the union of shells with index at most \(j\), and

\[
 \int_{|x|<R}|u|^2\leq
 \|u\|_{B^*}^2\sum_{k=0}^jR_k
 \leq2R_j\|u\|_{B^*}^2\leq4R\|u\|_{B^*}^2.
\]

If the ball quotient tends to zero, the shell quotients do too. Conversely, split the ball integral into finitely many early shells and the tail. The early integral divided by \(R\) tends to zero, while if each tail shell quotient is at most \(\delta^2\), the preceding geometric sum bounds the tail ball quotient by \(4\delta^2\). Let \(\delta\downarrow0\).

Truncation to finitely many shells converges in \(B^*\) exactly under this vanishing condition. Approximation in \(L^2\) on a fixed ball then gives smooth compactly supported approximants as in Theorem 1.1. Conversely, every such smooth function has vanishing tails, and the vanishing-tail subspace is norm closed.

Finally \(B^*_0\) is the \(c_0\) sum of the weighted shell Hilbert spaces. To see its dual explicitly, restrict a functional to the individual components. If those restrictions have norms \(a_j\), choose finitely many unit component vectors whose functional values are nonnegative real and arbitrarily close to \(a_j\). Their combined vector has supremum norm one, giving \(\sum_{j\leq N}a_j\leq\|\ell\|\). Hence \((a_j)\in\ell^1\). The Hilbert representatives therefore combine into a vector of \(B\). Finite component sums are dense in \(c_0\), so the representation extends to every vector. The reverse bound and exact norm follow by the same test. \(\square\)

Every \(L^2\) function belongs to \(B^*_0\). A function with a nonzero average mass per unit radius does not. The distinction between \(B^*\) and \(B^*_0\) is essential in radiation conditions.

<a id="transport-exact-distance"></a>

**Proposition 2.2 (exact distance to vanishing tails).** For every \(u\in B^*\),

\[
 \operatorname{dist}_{B^*}(u,B^*_0)
 =\limsup_{j\to\infty}R_j^{-1/2}\|u\|_{L^2(A_j)}.
\]

If the ball average has a limit \(L\), then

\[
 \lim_{R\to\infty}\frac1R\int_{|x|<R}|u|^2\,dx=L
 \quad\Longrightarrow\quad
 \operatorname{dist}_{B^*}(u,B^*_0)=\sqrt{L/2}.
\]

**Proof.** For \(v\in B^*_0\), the reverse triangle inequality on each shell gives

\[
 \|u-v\|_{B^*}\geq
 R_j^{-1/2}\|u\|_{L^2(A_j)}-R_j^{-1/2}\|v\|_{L^2(A_j)}.
\]

Take the limsup; the second term tends to zero. This proves the lower bound for every \(v\). For the reverse bound, truncate \(u\) to the shells with index at most \(N\). This locally square-integrable, compactly supported truncation belongs to \(B^*_0\), and its error has norm exactly
\(\sup_{j>N}R_j^{-1/2}\|u\|_{L^2(A_j)}\).
Let \(N\to\infty\).

Write \(q(R)=R^{-1}\int_{|x|<R}|u|^2\). For \(j\geq1\), the squared shell norm is

\[
 R_j^{-1}\|u\|_{L^2(A_j)}^2
 =q(R_j)-\tfrac12q(R_j/2)\longrightarrow L/2.
\]

The factor one half comes from the inner radius of our dyadic shell. Taking square roots proves the second assertion. \(\square\)

<a id="transport-trace"></a>

## 3. Slicing space and tracing Fourier space

Write \(x=(t,y)\in\mathbb R\times\mathbb R^{n-1}\).

**Lemma 3.1.** Every \(f\in B\) satisfies

\[
 \int_{\mathbb R}\|f(t,\cdot)\|_{L^2_y}\,dt\leq\sqrt2\|f\|_B.
\]

Every \(u\in L^\infty(\mathbb R_t;L^2_y)\) satisfies

\[
 \|u\|_{B^*}\leq\sqrt2\mathop{\mathrm{ess\,sup}}_t\|u(t,\cdot)\|_2.
\]

**Proof.** Let \(f_j=f1_{A_j}\). Its slices vanish when \(|t|>R_j\). Cauchy–Schwarz in \(t\), followed by Fubini, gives

\[
 \int\|f_j(t,\cdot)\|_2\,dt\leq(2R_j)^{1/2}\|f_j\|_2.
\]

Sum this inequality and use the triangle inequality in \(L^2_y\). For \(u\), integrate its slice bound on \([-R_j,R_j]\) to obtain \(\|u\|_{L^2(A_j)}^2\leq2R_j\sup_t\|u(t,\cdot)\|_2^2\). \(\square\)

The unitary Fourier convention is the one proved in the earlier Fourier reading. The partial Fourier transform in \(y\), denoted \(\mathcal F_y\), is unitary on the slice Hilbert space. The Hilbert-valued integrals here can be constructed from simple functions: set \(\int\sum_j1_{E_j}v_j=\sum_j|E_j|v_j\) for disjoint measurable sets of finite measure, and use \(\|\int g\|\le\int\|g\|\) to extend by completion in \(L^1(\mathbb R;\mathcal H)\). This also proves continuity of the integral and permits scalar dominated convergence applied to the norm of an error. The slice functions used here are strongly measurable: approximation of an \(L^2\) function by finite rectangle simple functions, followed by a subsequence whose squared \(L^2\) errors are summable, gives almost-everywhere convergence in the slice Hilbert space by Tonelli. A bounded partial Fourier transform preserves this measurability. Lemma 3.1 gives their integrable slice norm, so the construction applies. For \(\lambda\in\mathbb R\), define the flat-shell trace by this integral:

\[
 T_\lambda f(\eta)
 =(2\pi)^{-1/2}\int_{\mathbb R}
       e^{-it\lambda}(\mathcal F_yf)(t,\eta)\,dt.
\]

**Theorem 3.2.** The map \(T_\lambda:B\to L^2(\mathbb R^{n-1})\) is bounded and onto, with norm at most \(\pi^{-1/2}\), uniformly in \(\lambda\). For each \(f\in B\), \(\lambda\mapsto T_\lambda f\) is continuous in \(L^2\), and it agrees with \(\mathcal Ff(\lambda,\eta)\) for Schwartz functions. Its restriction to any measurable set \(K\) of the \(\eta\) variables is onto \(L^2(K)\). For \(n=1\), the target is \(\mathbb C\).

**Proof.** Minkowski's integral inequality, slice Plancherel and Lemma 3.1 give the bound. Dominated convergence for the Bochner integral gives continuity. Fubini proves the agreement on Schwartz functions.

For surjectivity on bounded \(K\), put

\[
 E_\lambda a(t,y)=(2\pi)^{-1/2}e^{it\lambda}\mathcal F_y^{-1}(1_Ka)(y).
\]

The pairing satisfies \((T_\lambda f,a)_{L^2(K)}=(f,E_\lambda a)\), first for test functions and then by density. Lemma 3.1 shows \(\|E_\lambda a\|_{B^*}\leq\pi^{-1/2}\|a\|_2\). A lower bound is also needed. Write \(v=\mathcal F_y^{-1}(1_Ka)\). For each \(R\geq1\),

\[
 \frac1R\int_{|x|<R}|E_\lambda a|^2\,dx
 =\frac1\pi\int_{|y|<R}
       \sqrt{1-|y|^2/R^2}\,|v(y)|^2\,dy.
\]

Dominated convergence gives the limit \(\pi^{-1}\|a\|_2^2\). Proposition 2.2 gives the exact quotient distance and hence the stronger lower bound

\[
 \operatorname{dist}_{B^*}(E_\lambda a,B^*_0)
 =(2\pi)^{-1/2}\|a\|_2
 \leq\|E_\lambda a\|_{B^*}.
\]

This argument did not use boundedness of \(K\), so it holds for every measurable \(K\), including \(\mathbb R^{n-1}\). The exact equality concerns distance to the vanishing-tail subspace; no equality for the ordinary \(B^*\) norm is asserted.

Here is the Banach-space implication, including the onto assertion. If a bounded map \(T:X\to\mathcal H\), with \(X\) Banach and \(\mathcal H\) Hilbert, has \(\|T^*a\|\geq c\|a\|\), then \(T\) is onto. Put \(C=\overline{T(\{\|x\|\leq1\})}\). It is closed, convex and balanced, and its support function in direction \(a\) is \(\|T^*a\|\): multiplying an input by a unit complex scalar turns the modulus of its pairing into its real part. If some \(h\) with \(\|h\|\le c\) were outside \(C\), the closest-point separation proved in Section 1 would give a nonzero \(a\) with \(\sup_{v\in C}\operatorname{Re}(v,a)<\operatorname{Re}(h,a)\le c\|a\|\), contradicting the lower bound. Thus \(C\) contains that ball. For any target \(h\), closure and scaling give \(x_1\) with \(\|x_1\|\leq2\|h\|/c\) and \(\|h-Tx_1\|\leq\|h\|/2\). Repeat on the residual. The resulting series \(\sum x_j\) converges in \(X\), has norm at most \(4\|h\|/c\), and its image is \(h\). Apply this to \(T_\lambda\) and the extension just constructed. It proves surjectivity on the entire flat hyperplane, and hence all the claimed special cases. For \(n=1\), the slice space is \(\mathbb C\) and the same argument applies. \(\square\)

<a id="transport-trace-separation"></a>

**Proposition 3.3 (trace operators remain separated).** If \(\lambda\ne\mu\), then

\[
 \|T_\lambda-T_\mu\|_{B\to L^2}\geq\pi^{-1/2}.
\]

Thus the family is nowhere continuous in operator norm, even though Theorem 3.2 proves continuity on each fixed \(f\).

**Proof.** Choose \(a\) of \(L^2\) norm one, put \(v=\mathcal F_y^{-1}a\), and set

\[
 w(t,y)=(E_\lambda-E_\mu)a
 =(2\pi)^{-1/2}(e^{it\lambda}-e^{it\mu})v(y).
\]

Let \(\delta=\lambda-\mu\ne0\) and \(b_R(y)=\sqrt{R^2-|y|^2}\) on \(|y|<R\). Integration over \(-b_R<t<b_R\) gives exactly

\[
 \frac1R\int_{|x|<R}|w|^2\,dx
 =\frac1{2\pi}\int_{|y|<R}
 \left(\frac{4b_R(y)}R-
       \frac{4\sin(\delta b_R(y))}{\delta R}\right)|v(y)|^2\,dy.
\]

The first term tends to \(4\|v\|_2^2=4\) by dominated convergence. The absolute integral of the second is at most \(4/(|\delta|R)\). The ball average therefore tends to \(2/\pi\), and Proposition 2.2 gives
\(\operatorname{dist}(w,B^*_0)=1/\sqrt\pi\).
For \(n=1\), the same calculation uses the scalar slice space and \(b_R=R\).

Integral duality from Theorem 1.1 identifies \(w\) with the adjoint action of \(T_\lambda-T_\mu\) on \(a\). Consequently

\[
 \|T_\lambda-T_\mu\|
 \geq\|(E_\lambda-E_\mu)a\|_{B^*}
 \geq\operatorname{dist}(w,B^*_0)=\pi^{-1/2}.
\]

This uniform separation for distinct energies proves the claim. \(\square\)

The trace theorem extends to rotated affine hyperplanes: the shell norms are invariant under orthogonal rotations, and multiplication by \(e^{ix\cdot\xi_0}\) is an isometry. Curvature, or a nonlinear change of Fourier variables, is not accounted for by these two operations.

<a id="transport-resolvent"></a>

## 4. An exact transport resolvent

Consider \(H_0=D_t\) on \(L^2(\mathbb R_t\times\mathbb R^{n-1}_y)\), with domain \(\{u:D_tu\in L^2\}\). The earlier Fourier duality proof identifies this domain with the maximal domain of multiplication by the real frequency \(\tau\). That multiplication domain is dense: cut off any \(L^2\) function to \(|\tau|\leq N\) and use dominated convergence. Multiplication is symmetric there. If \(v\) is in its adjoint domain with value \(w\), test against every \(L^2\) function supported where \(|\tau|\leq N\). Such functions are in the original domain, and the adjoint identity gives \(1_{|\tau|\leq N}w=\tau1_{|\tau|\leq N}v\). Monotone convergence gives \(\tau v\in L^2\) and then \(w=\tau v\). Thus the two domains agree and the operator is self-adjoint. Unitary conjugation gives the stated realization of \(D_t\). No spatial boundary is imposed.

**Theorem 4.1.** For \(f\in B\) and \(\operatorname{Im}z>0\), the Hilbert-space resolvent is

\[
 R_0(z)f(t,y)=i\int_{-\infty}^t e^{iz(t-s)}f(s,y)\,ds.
\]

For \(\operatorname{Im}z<0\), it is

\[
 R_0(z)f(t,y)=-i\int_t^{\infty}e^{iz(t-s)}f(s,y)\,ds.
\]

The upper and lower boundary values at every real \(\lambda\) exist as \(B^*\)-valued weak-star limits. They are given by the same integrals with \(z=\lambda\). Their operator norms from \(B\) to \(B^*\) are at most two. They satisfy \((D_t-\lambda)u=f\) distributionally, and

\[
 R_0(\lambda+i0)f-R_0(\lambda-i0)f
 =i\sqrt{2\pi}\,e^{it\lambda}
    \mathcal F_y^{-1}(T_\lambda f).
\]

**Proof.** The slice \(L^1_tL^2_y\) bound makes both integrals well defined and bounds their slice norms by \(\sqrt2\|f\|_B\); the exponential has modulus at most one on the respective integration region. Lemma 3.1 gives the \(B^*\) bound two. Differentiation for smooth compactly supported \(f\) proves the equation, with \((-i)\cdot i=1\) in the upper formula and the analogous lower-endpoint sign in the second. Density in \(B\) proves the distributional equation in general.

For nonreal \(z\), convolution in \(t\) with the exponential kernel is bounded on \(L^2\), since the kernel has \(L^1\) norm \(|\operatorname{Im}z|^{-1}\). Explicitly, the integral triangle inequality followed by weighted Cauchy–Schwarz bounds the squared slice norm by \(\|k\|_1\int |k(t-s)|\|f(s,\cdot)\|_2^2ds\); integrating in \(t\) gives the squared \(L^2\) bound \(\|k\|_1^2\|f\|_2^2\). Its Fourier multiplier is \((\tau-z)^{-1}\), which identifies it with the Hilbert-space resolvent, including its domain. As \(z\to\lambda\) in the relevant half-plane, dominated convergence gives convergence of each slice in \(L^2_y\). On any bounded ball this gives \(L^2\) convergence by the uniform slice bound. To pass to weak-star convergence against \(g\in B\), first truncate \(g\) to a ball, and then use the uniform \(B^*\) bound to make the pairing with its \(B\)-small tail uniformly small. This proves the asserted topology. Subtracting the two boundary integrals joins them into the full Fourier integral in \(s\), giving the displayed jump. \(\square\)

<a id="transport-radiation"></a>

## 5. Radiation, vanishing flux and uniqueness

Define

\[
 v_+=i\int_{\mathbb R}e^{-is\lambda}f(s,\cdot)\,ds
      =i\sqrt{2\pi}\,\mathcal F_y^{-1}(T_\lambda f).
\]

For the upper solution \(u_+=R_0(\lambda+i0)f\), its slice satisfies

\[
 e^{-it\lambda}u_+(t,\cdot)\longrightarrow
 \begin{cases}0,&t\to-\infty,\\v_+,&t\to+\infty,\end{cases}
\]

in \(L^2_y\). These limits follow directly from the tail of the \(L^1_tL^2_y\) integral. The lower solution has the reversed direction, with limiting amplitude \(-v_+\) at \(-\infty\).

**Theorem 5.1.** The following conditions on \(f\in B\) are equivalent:

1. \(T_\lambda f=0\).
2. The upper and lower boundary solutions agree.
3. The upper solution belongs to \(B^*_0\).
4. The lower solution belongs to \(B^*_0\).

Moreover

\[
 \lim_{R\to\infty}\frac1R\int_{|x|<R}|u_+|^2\,dx
 =\|v_+\|_2^2
 =2\pi\|T_\lambda f\|_2^2
 =2\operatorname{Im}(u_+,f).
\]

**Proof.** The jump formula proves equivalence of 1 and 2. Approximate \(u_+\) by the model \(w(t,y)=1_{\{t>0\}}e^{it\lambda}v_+(y)\). Their difference has bounded slice norms tending to zero as \(t\to\pm\infty\). For any \(\delta>0\), choose \(T\) so the slice norm outside \([-T,T]\) is at most \(\delta\). Its integral over a ball, divided by \(R\), is bounded by \(C_T/R+2\delta^2\). Therefore \(u_+-w\in B^*_0\) by Theorem 2.1.

The ball average of \(w\) is

\[
 \int_{|y|<R}\sqrt{1-|y|^2/R^2}\,|v_+(y)|^2\,dy,
\]

which tends to \(\|v_+\|_2^2\). The cross term between \(w\) and \(u_+-w\), divided by \(R\), tends to zero by Cauchy–Schwarz and the vanishing average of the difference. This proves the first limit and equivalence of 1 and 3. The lower solution has the same limiting squared mass, proving 4.

For the last equality put \(g(t)=e^{-it\lambda}f(t,\cdot)\) and \(G(t)=\int_{-\infty}^tg(s)\,ds\). These are Hilbert-valued functions, \(g\in L^1\) and \(G\) bounded. The pairing is absolutely integrable, and

\[
 \operatorname{Im}(u_+,f)
 =\operatorname{Re}\int(G(t),g(t))_{L^2_y}\,dt
 =\tfrac12\|G(+\infty)\|_2^2.
\]

To justify the second equality directly for every \(L^1\) slice forcing, expand \(\|\int g\|^2=\iint(g(s),g(t))\,ds\,dt\). The absolute double integral is at most \((\int\|g\|)^2\). The diagonal is null, and the two half-planes \(s<t\) and \(s>t\) give conjugate integrals. Their sum is therefore \(2\operatorname{Re}\int(G(t),g(t))dt\). This proves the identity without differentiability of the forcing. Since \(v_+=iG(+\infty)\), the result follows. \(\square\)

<a id="transport-norm-limit"></a>

**Theorem 5.2 (the exact obstruction to norm convergence).** For either boundary value \(u_\pm=R_0(\lambda\pm i0)f\),

\[
 \operatorname{dist}_{B^*}(u_\pm,B^*_0)
 =\sqrt\pi\,\|T_\lambda f\|_2.
\]

Every nonreal \(z\) therefore satisfies

\[
 \|R_0(z)f-u_\pm\|_{B^*}
 \geq\sqrt\pi\,\|T_\lambda f\|_2.
\]

As \(z\to\lambda\) in the corresponding half-plane, convergence to \(u_\pm\) in \(B^*\) norm holds if and only if \(T_\lambda f=0\). The approach may change both the real and imaginary parts of \(z\).

**Proof.** Theorem 5.1 gives the ball-mass limit \(2\pi\|T_\lambda f\|_2^2\) for each sign. Proposition 2.2 gives the distance. Since \(f\in B\subset L^2\), every nonreal Hilbert-space resolvent \(R_0(z)f\) lies in \(L^2\subset B^*_0\). The distance consequently bounds its error from below, proving necessity of zero trace.

We prove sufficiency, including arbitrary upper-half-plane approaches. Put
\(g(s)=e^{-is\lambda}f(s,\cdot)\) in the slice Hilbert space \(\mathcal H=L^2_y\), or \(\mathbb C\) when \(n=1\). Lemma 3.1 gives \(g\in L^1(\mathbb R;\mathcal H)\), and zero trace says \(\int g=0\). For \(h=z-\lambda\) with \(\operatorname{Im}h\geq0\), define

\[
 (K_hg)(t)=i\int_{-\infty}^t e^{ih(t-s)}g(s)\,ds.
\]

Its norm from \(L^1\) to \(L^\infty\) is at most one, including \(h=0\). The resolvent and boundary solution are \(e^{it\lambda}K_hg\) and \(e^{it\lambda}K_0g\).

Choose a scalar \(\psi\in C_c^\infty([-1,1])\), \(\psi\geq0\), \(\int\psi=1\). For \(M\geq1\) put

\[
 g_M=1_{[-M,M]}g-\psi\int_{-M}^M g(s)\,ds.
\]

Then \(g_M\) is supported in \([-M,M]\), its integral is zero, and

\[
 \|g-g_M\|_{L^1}
 \leq2\int_{|s|>M}\|g(s)\|_{\mathcal H}\,ds\longrightarrow0.
\]

We need only this slice approximation; \(g_M\) need not belong to \(B\). For \(\ell\geq0\) and \(\operatorname{Im}h\geq0\), integration of the derivative of \(e^{ih\ell}\) gives
\(|e^{ih\ell}-1|\leq |h|\ell\).
When \(-M\leq t\leq M\), the upper integral therefore yields

\[
 \|(K_h-K_0)g_M(t)\|_{\mathcal H}
 \leq2M|h|\|g_M\|_{L^1}.
\]

Both integrals vanish for \(t<-M\). For \(t>M\), \(K_0g_M=0\) and cancellation gives

\[
 K_hg_M(t)=i e^{ih(t-M)}\int_{-M}^M
                  (e^{ih(M-s)}-1)g_M(s)\,ds.
\]

The exterior factor has modulus at most one, so the same bound holds there. Thus

\[
 \|(K_h-K_0)g\|_{L^\infty}
 \leq2\|g-g_M\|_{L^1}+2M|h|\|g_M\|_{L^1}.
\]

First choose \(M\) to make the first term small, and then let \(h\to0\) with that \(M\) fixed. The slice supremum tends to zero, and Lemma 3.1 transfers this convergence to \(B^*\). Reflection \(t\mapsto-t\) changes the lower integral into an upper integral with parameter \(-h\), whose imaginary part is nonnegative. It preserves the zero-integral condition and the norms, so the same proof handles the lower half-plane. \(\square\)

This criterion has been proved for \(D_t\) and its explicit transport integral. The general curved and perturbed resolvent lessons specify their boundary topologies separately.

<a id="transport-homogeneous-uniqueness"></a>

A homogeneous solution \(u\in B^*\) of \((D_t-\lambda)u=0\) is \(e^{it\lambda}v(y)\), with \(v\in L^2_y\). To prove the distributional representation, put \(U=e^{-it\lambda}u\) and choose \(\rho\in C_c^\infty(\mathbb R)\) with \(\int\rho=1\). For a compact smooth test \(\varphi(t,y)\), set \(a(y)=\int\varphi(t,y)dt\). The function \(\varphi-\rho a\) has zero integral in \(t\), so its primitive from \(-\infty\) is a compactly supported smooth test \(\Psi(t,y)\). Since \(\partial_tU=0\), we have \(U(\varphi)=U(\rho a)\). Defining \(v(a)=U(\rho a)\) proves \(U=1\otimes v\). Local \(L^2\) makes \(v\) a locally square-integrable function by Cauchy–Schwarz applied to \(\int\rho(t)U(t,y)dt\). The \(B^*\) ball bound, applied to cylinders \(|y|<L\), \(|t|<R/2\) contained in a ball of radius \(R\) for large \(R\), bounds \(\int_{|y|<L}|v|^2\) uniformly in \(L\). Thus \(v\in L^2\). Its ball average tends to \(2\|v\|^2\), so the only homogeneous solution in \(B^*_0\) is zero. This proves uniqueness in the vanishing-mass class when the Fourier trace vanishes.


