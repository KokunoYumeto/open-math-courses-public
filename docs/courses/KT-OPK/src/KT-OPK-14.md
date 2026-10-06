# Determinants of traces and the pairing with K_1

*Written by GPT-6.1 Sol (OpenAI), October 2026, at Ultra. Public domain (CC0).*

Independently authored CC0 lesson; self-checked by the writing AI.

Integrating a logarithmic derivative gives a determinant. Different paths to the same invertible differ by a loop, and the trace of that loop is a K-theory period. For an extension, a path to an ideal unitary becomes a loop in the quotient; its period detects the exponential boundary. A twisted endpoint condition leads instead to a real-valued homomorphism on a mapping torus.

Throughout, \(\tau\) is a bounded positive trace, with the unnormalized matrix extensions and pairing \(\tau_*\) proved in [Lesson 13, Theorem 1.1](KT-OPK-13.md#1-a-bounded-trace-measures-a-k-class). We use stable invertibles and polar decomposition from Lesson 6, the positive Bott map \(\beta_A:K_0(A)\to K_1(SA)\) from [Lesson 10, Theorem 4.1](KT-OPK-10.md#4-the-boundary-proves-periodicity-and-fixes-its-sign), and the positive exponential boundary and exact sequence from [Lesson 11, Theorems 1.1 and 2.1](KT-OPK-11.md). No computation here requires the later mapping-torus or crossed-product K-theory theorems.

## 1. The logarithmic integral and its periods

Let \(\xi:[0,1]\to GL_n(A)\) be piecewise continuously differentiable. For unital \(A\), define

\[
\begin{gathered}
\Gamma_\tau(\xi)\\
=\frac1{2\pi i}\int_0^1\tau_n(\xi'(t)\xi(t)^{-1})\,dt.
\end{gathered}
\tag{1.1}
\]

For nonunital \(A\), paths lie in \(GL_n(A^+)\) with scalar part constantly \(1_n\); apply the linear extension \(\tau^0(a+\lambda1)=\tau(a)\) from Lesson 13. Their logarithmic derivatives lie in \(M_n(A)\), so this convention agrees with evaluating the original trace. Identity stabilization adds zero to (1.1).

Concatenation adds integrals, reversal negates them, and an increasing piecewise smooth reparametrization preserves the integral, by change of variable. For pointwise path products, the product rule and trace cyclicity give

\[
\Gamma_\tau(\xi\eta)
=\Gamma_\tau(\xi)+\Gamma_\tau(\eta).
\tag{1.2}
\]

Indeed, \((\xi\eta)'(\xi\eta)^{-1}=\xi'\xi^{-1}+\xi(\eta'\eta^{-1})\xi^{-1}\), and the second summand has the same trace as \(\eta'\eta^{-1}\). The integral also adds on block sums and is unchanged by conjugation by a fixed invertible.

**Lemma 1.1 (variation).** For a sufficiently differentiable two-parameter family \(\xi(s,t)\) of invertibles,

\[
\begin{gathered}
\frac{d}{ds}\Gamma_\tau(\xi(s,\cdot))\\
=\frac1{2\pi i}\tau_n(Y(s,1))\\
-\frac1{2\pi i}\tau_n(Y(s,0)),
\end{gathered}
\tag{1.3}
\]

where \(Y=\xi_s\xi^{-1}\). In particular the integral is invariant under homotopies which keep both endpoints fixed.

*Proof.* Put \(X=\xi_t\xi^{-1}\). Differentiating the inverse gives

\[
\partial_sX-\partial_tY=[Y,X].
\tag{1.4}
\]

The trace of the commutator is zero. Integrate in \(t\) and differentiate under the integral, which is permitted because the trace is bounded and the family has continuous derivatives on each compact smooth piece. Internal subdivision boundary terms cancel. If the endpoints are fixed, \(Y\) is zero there. \(\square\)

The same invariance holds for continuous homotopies between piecewise smooth paths. Work in one finite matrix size after stabilization. A compact homotopy has a uniform inverse bound. Approximate it on a fine finite subdivision by affine interpolation of its values, retaining the endpoint boundary; sufficiently small uniform error keeps every interpolant invertible. Retain the prescribed piecewise smooth paths at the two homotopy ends, using their common subdivisions. On the resulting pieces, the calculation of Lemma 1.1 applies, and the internal boundary terms cancel. This connects the endpoints by a homotopy for which the calculation is valid. This argument also proves that every continuous based loop can be replaced by a piecewise smooth based loop in its homotopy class.

Set

\[
H_\tau=\tau_*(K_0(A))\subset\mathbb R.
\tag{1.5}
\]

**Theorem 1.2 (the period group).** The integrals of stable based loops of invertibles are exactly \(H_\tau\).

*Proof.* A based loop represents a class of \(K_1(SA)\); its endpoints are the identity. Bott periodicity identifies every such class with a class of \(K_0(A)\). For a unital projection \(e\), its positive loop is \(\exp(2\pi it e)\). Its logarithmic derivative is \(2\pi i e\), so its integral is \(\tau_n(e)\). For a general normalized relative class \([e]-[P]\), the corresponding positive loop is

\[
\begin{gathered}
f_e(t)=\exp(2\pi it e),\\
\ell_{e,P}(t)=f_e(t)f_P(t)^{-1},\\
P=\epsilon_n(e).
\end{gathered}
\tag{1.6}
\]

Both endpoints and the scalar part are the identity. By (1.2), its integral is \(\tau_n(e-P)\), where the trace is evaluated on the nonscalar difference, as in Lesson 13. This is exactly \(\tau_*([e]-[P])\). The positive loop model is the one fixed in Lesson 10. Homotopy invariance from Lemma 1.1 now puts the integral of every loop in \(H_\tau\). Conversely each K-class has such a stable loop representative, so every element of \(H_\tau\) occurs. \(\square\)

Only the stable loop identification is needed here. The integral of a loop is a real period even when its chosen representative passes through nonunitary invertibles.

## 2. The determinant and its normalization

Write \(GL_\infty(A)_0\) for the stable identity component, using normalized scalar parts in the nonunital case. Each element has a piecewise smooth path from the identity. For example subdivide a continuous path until each consecutive multiplicative increment is within distance less than one of the identity; its convergent logarithm gives an exponential path for that increment. Concatenate these finitely many paths.

**Theorem 2.1 (de la Harpe–Skandalis determinant).** For \(u\in GL_\infty(A)_0\), choose such a path \(\xi\) from \(1\) to \(u\). Then

\[
\Delta_\tau(u)=\Gamma_\tau(\xi)\pmod{H_\tau}
\tag{2.1}
\]

defines a homomorphism \(GL_\infty(A)_0\to\mathbb C/H_\tau\). On the unitary identity component its values lie in \(\mathbb R/H_\tau\).

*Proof.* Two paths to \(u\), with the second reversed, concatenate to a based loop. Their integral difference belongs to \(H_\tau\) by Theorem 1.2. Thus the value is independent of the path. Pointwise multiplication of paths from the identity gives a path to the product, so (1.2) proves the homomorphism assertion. Identity padding preserves it. For a unitary path, differentiating \(\xi\xi^*=1\) shows \(\xi'\xi^*\) is skew-adjoint. A positive trace takes real values on selfadjoint elements and consequently imaginary values on skew-adjoint elements. Division by \(2\pi i\) makes the integral real. \(\square\)

For any finite collection \(x_k\in M_n(A)\), not necessarily selfadjoint,

\[
\begin{gathered}
\Delta_\tau\left(\prod_k\exp(2\pi i x_k)\right)\\
=\sum_k\tau_n(x_k)\pmod{H_\tau}.
\end{gathered}
\tag{2.2}
\]

Use the exponential paths and their constant logarithmic derivatives, then (1.2). Selfadjoint \(x_k\) give unitary exponentials and real values. Positivity of the trace does not make the determinant of every invertible real: for \(r\in\mathbb R\), \(\exp(r)1\) has integral \(r\tau(1)/(2\pi i)\), which is imaginary when nonzero. The real assertion in Theorem 2.1 has a unitary hypothesis.

On \(M_n(\mathbb C)\), take first \(\tau=\operatorname{Tr}_n\). Minimal projections have value one, so \(H_\tau=\mathbb Z\). For a matrix path, differentiating its ordinary determinant gives \((\det\xi)'/\det\xi=\operatorname{Tr}(\xi'\xi^{-1})\). This identity follows by differentiating the determinant's multilinear column formula and multiplying by \(\xi^{-1}\), or the same cofactor expansion. Integrating along the path therefore gives

\[
\begin{gathered}
\Delta_{\operatorname{Tr}}(u)
=\frac1{2\pi i}\log\det u\\
\pmod{\mathbb Z}.
\end{gathered}
\tag{2.3}
\]

Different logarithms differ by \(2\pi i\mathbb Z\). On stabilized matrices over \(M_n\), the unnormalized extension is the ordinary trace on the full block matrix, so the same formula applies. For the normalized state \(\tau=\operatorname{Tr}_n/n\), both the integral and the period group are divided by \(n\):

\[
\begin{gathered}
\Delta_\tau(u)=\frac1{2\pi i n}\log\det u\\
\pmod{\tfrac1n\mathbb Z}.
\end{gathered}
\tag{2.4}
\]

For \(A=C(\mathbb T)\) and probability measure \(\mu\), the K-pairing is rank by Lesson 13, so \(H_\tau=\mathbb Z\). The path \(\xi(t,z)=\exp(2\pi it f(z))\) gives

\[
\begin{gathered}
\Delta_\tau(\exp(2\pi i f))\\
=\int_{\mathbb T}f\,d\mu\pmod{\mathbb Z}.
\end{gathered}
\tag{2.5}
\]

Lebesgue measure is the standard example. For real \(f\) the function is unitary. A determinant is a coset; we quotient by the actual group \(H_\tau\), without replacing it by its closure or choosing a preferred real lift.

### 2.1. A determinant for every bounded trace at once

The positivity assumption on \(\tau\) in §§1–2 is useful for real values. The integral itself needs only a bounded tracial linear map. We now allow a complex Banach space \(F\) and a bounded linear map \(t:A\to F\) satisfying \(t(ab)=t(ba)\). Put \(t_n((a_{ij}))=\sum_i t(a_{ii})\). Integrals in \(F\) are Bochner integrals; here their integrands are continuous on finitely many compact pieces, so they are limits of Riemann sums in a complete normed space.

**Lemma 2.2 (Banach-valued periods).** There is a pairing \(t_*:K_0(A)\to F\). With normalized scalar parts for nonunital \(A\), the integrals

\[
\begin{gathered}
\Gamma_t(\xi)=\frac1{2\pi i}
\int_0^1 t_n(\xi'\xi^{-1})\,dt,\\
\{\Gamma_t(\ell):\ell\text{ a stable based loop}\}\\
=t_*(K_0(A)).
\end{gathered}
\tag{2.6}
\]

Consequently \(\Delta_t(u)=\Gamma_t(\xi)\bmod t_*(K_0(A))\) is a homomorphism on \(GL_\infty(A)_0\).

*Proof.* The matrix cyclicity calculation in Lesson13, (1.2), works with values in \(F\). If \(v^*v=p\), \(vv^*=q\), it gives \(t(p)=t(q)\), without using positivity. Close projections are unitarily equivalent, so a subdivision of a projection homotopy makes its value constant. Block additivity gives the group-completion pairing. For nonunital \(A\), extend by \(t^0(a+\lambda1)=t(a)\) and restrict to relative classes: their values are \(t_n(e-P)\). This proves all the relations, including the scalar cancellation.

The product rule, variation identity (1.4) and trace cancellation also work in \(F\). Boundedness permits differentiation under each compact-piece integral. The smoothing argument following Lemma1.1 works in the algebra of matrices, independently of the target, and proves invariance under continuous endpoint-fixed homotopies. The positive Bott loop of a projection has integral \(t_n(p)\); the normalized relative loop (1.6) has integral \(t_n(e-P)\). The full Bott identification used in Theorem1.2 now gives both inclusions in (2.6). The same difference-of-paths and product-path arguments as in Theorem2.1 prove the final assertion. \(\square\)

Let \(C_A\) be the norm-closed complex linear span of the additive commutators \(ab-ba\) in \(A\), and put \(E_A=A/C_A\). This is a quotient Banach space, not generally an algebra: \(C_A\) need not be an ideal. Denote the quotient map by \(T_A\). Every bounded tracial \(t:A\to F\) vanishes on \(C_A\), so there is a unique bounded linear \(\lambda:E_A\to F\) with \(t=\lambda T_A\). The quotient norm gives \(\|\lambda\|=\|t\|\).

**Theorem 2.3 (universal determinant).** Set \(P_A=(T_A)_*(K_0(A))\), an actual additive subgroup of \(E_A\). Then

\[
\begin{gathered}
\Delta_A:GL_\infty(A)_0\longrightarrow E_A/P_A,\\
\Delta_A(\exp(2\pi i a))=T_A(a)+P_A,\\
a\in A
\end{gathered}
\tag{2.7}
\]

is a surjective homomorphism. Every \(\Delta_t\) factors through it by the induced map \(\lambda:E_A/P_A\to F/t_*(K_0(A))\).

*Proof.* The quotient map is bounded and tracial, so Lemma2.2 constructs the homomorphism. The exponential path \(s\mapsto\exp(2\pi i s a)\) has constant logarithmic derivative \(2\pi i a\), proving the displayed formula. The surjectivity of \(T_A:A\to E_A\) proves surjectivity onto its further quotient. The identity \(t_n=\lambda(T_A)_n\) commutes with Riemann sums, integrals and the pairing. Thus \(\lambda(P_A)=t_*(K_0(A))\), and applying \(\lambda\) to the path integral gives exactly \(\Delta_t\). \(\square\)

We do not close \(P_A\). When it is not closed, the quotient topology is not Hausdorff. Replacing \(P_A\) by its closure changes the determinant and its kernel.

**Lemma 2.4 (kernel and local logarithms).** For a bounded tracial \(t\), an element \(u\) belongs to \(\ker\Delta_t\) if and only if, after one finite identity stabilization, there are \(y_1,\ldots,y_r\in M_N(A)\) with

\[
\begin{gathered}
u=\prod_{j=1}^r\exp(y_j),\\
\sum_{j=1}^r t_N(y_j)=0.
\end{gathered}
\tag{2.8}
\]

For \(x_1,\ldots,x_r\) of normalized scalar part \(1\), let \(d_j=\|x_j-1\|<1\). If \(\prod_j(1-d_j)>1/2\), their convergent logarithms satisfy

\[
\begin{gathered}
t_N\!\left(\log\!\left(\prod_jx_j\right)\right)\\
=\sum_j t_N(\log x_j).
\end{gathered}
\tag{2.9}
\]

*Proof.* Choose a path from \(1\) to \(u\). If its integral is a period, prepend a based loop with the negative of that integral, supplied by Lemma2.2. After one common finite padding this is a path \(\xi\) with exactly zero integral. On a sufficiently fine subdivision define
\(y_j=\log(\xi(s_{j-1})^{-1}\xi(s_j))\). These logarithms belong to \(M_N(A)\) in the nonunital case. The piecewise path
\(\eta(s)=\xi(s_{j-1})\exp((s-s_{j-1})y_j/(s_j-s_{j-1}))\)
has the same endpoints and can be made uniformly close to \(\xi\). Indeed, the original path and its inverse are uniformly continuous on a compact interval, and these logarithms tend uniformly to zero with the mesh. The affine interpolation between the paths is invertible when \(\|\eta(s)\xi(s)^{-1}-1\|<1\), so it is an endpoint-fixed homotopy. Its integral is therefore zero. Cyclicity evaluates the integral of each segment as \(t_N(y_j)/(2\pi i)\). The endpoint identity is the telescoping ordered product in (2.8). Conversely the product of exponential paths in (2.8) has integral zero, and hence determinant zero.

For (2.9) put \(z_j=\log x_j\) and \(\zeta(s)=\prod_j\exp(s z_j)\), for \(0\leq s\leq1\). The logarithm series and exponential series give
\(\|z_j\|\leq-\log(1-d_j)\),
\(\|\exp(s z_j)\|\leq(1-d_j)^{-1}\), and
\(\|\exp(s z_j)-1\|\leq(1-d_j)^{-1}-1\).
The telescoping product estimate consequently gives
\(\|\zeta(s)-1\|\leq\prod_j(1-d_j)^{-1}-1<1\).
Thus the logarithm of every \(\zeta(s)\) is defined. Interpolating in these logarithms between \(\log\zeta(s)\) and \(s\log\zeta(1)\), then exponentiating, gives an endpoint-fixed homotopy to the single exponential path. The integral of the product path is \(\sum_jt_N(z_j)/(2\pi i)\), while that of the single exponential path is \(t_N(\log\zeta(1))/(2\pi i)\). Homotopy invariance proves (2.9). \(\square\)

### 2.2. Commutators, closures and trace separation

For each finite size let \(G_N=GL_N(A)_0\), using normalized scalar parts if \(A\) is nonunital, and let \(D_N\) be the subgroup generated by its multiplicative commutators \(vwv^{-1}w^{-1}\). “Generated” means finite products and inverses. Let \(D\) be the corresponding subgroup of the stable identity component.

**Proposition 2.5 (what the universal kernel says about commutators).** We have \(D\subseteq\ker\Delta_A\). Every element of \(\ker\Delta_A\), after finite identity padding, is a norm limit of elements of a single \(D_N\). In particular \(D\) and \(\ker\Delta_A\) have equal closures in the stable final topology from the finite normed stages. The assertion concerns closures; it does not identify the two algebraic subgroups.

*Proof.* A homomorphism to an abelian group kills every multiplicative commutator, proving the first inclusion. Let \(C_N\) be the norm-closed complex linear span of the additive commutators of elements of \(M_N(A)\). We identify the matrix trace kernel:

\[
\ker (T_A)_N=C_N.
\tag{2.10}
\]

The right side is contained in the left by the matrix trace calculation. Conversely every off-diagonal \(aE_{ij}\) is a norm limit of \([aE_{ij},e_\lambda E_{jj}]\), where \((e_\lambda)\) is a two-sided approximate unit of \(A\). For \(i>1\), \(aE_{ii}-aE_{11}\) is the limit of \([aE_{i1},e_\lambda E_{1i}]\). The diagonal remainders reduce any matrix to \((\sum_i a_{ii})E_{11}\) modulo the closed span. If its matrix trace is zero, \(\sum_i a_{ii}\in C_A\). Placing each approximating additive commutator from \(A\) in the \(11\)-corner proves (2.10). In a unital algebra the approximate unit can be replaced by the identity. This argument uses only commutators of elements of \(M_N(A)\), including when its scalar matrix units themselves are unavailable.

Write \(\overline{D_N}\) for closure in \(G_N\), a closed normal subgroup. For \(a,b\in M_N(A)\), the exponential series gives
\[
\begin{gathered}
e^{s a}e^{s b}e^{-s a}e^{-s b}\\
=1+s^2[a,b]+O(s^3),\qquad s\to0.
\end{gathered}
\]
With \(s=m^{-1/2}\), the \(m\)-th power tends in norm to \(e^{[a,b]}\). To see the error explicitly, compare it with \((1+[a,b]/m)^m\): a telescoping difference has \(m\) terms bounded by a uniform exponential bound times \(O(m^{-3/2})\), and hence tends to zero. The latter product tends to the exponential by its power series. Every approximating product lies in \(D_N\).

In the abelian topological quotient \(G_N/\overline{D_N}\), the Lie product formula
\(e^{a+b}=\lim_m(e^{a/m}e^{b/m})^m\)
therefore identifies the image of \(e^{a+b}\) with the product of the images of \(e^a,e^b\). The formula follows by comparing the factor with \(1+(a+b)/m+O(m^{-2})\) and using the same telescoping estimate. Induction treats any finite sum. Multiplying one entry of an additive commutator by a complex scalar handles scalar coefficients. Continuity of the exponential then shows \(e^c\in\overline{D_N}\) for every \(c\) in the closed span in (2.10).

Finally, Lemma2.4 writes a padded \(u\in\ker\Delta_A\) as a finite product \(e^{y_j}\) with \((T_A)_N(\sum_jy_j)=0\). In the abelian quotient its image is that of \(e^{\sum_jy_j}\). By (2.10) and the preceding paragraph this image is the identity. Thus \(u\in\overline{D_N}\). Inclusion of a finite normed stage in the stable final topology is continuous, so every such \(u\) belongs to the closure of \(D\). Together with \(D\subseteq\ker\Delta_A\), this proves the equality of closures. \(\square\)

**Theorem 2.6 (separable trace detection).** If \(A\) is separable, then

\[
\begin{gathered}
\ker\Delta_A
=\bigcap_{t\in\operatorname{Tr}_b(A)}\ker\Delta_t\\
=\bigcap_{t\in\operatorname{Tr}_b^+(A)}\ker\Delta_t.
\end{gathered}
\tag{2.11}
\]

Here the first family consists of all bounded complex tracial functionals, and the second of all bounded positive traces. Each scalar determinant uses its own actual period group \(t_*(K_0(A))\).

*Proof.* The zero algebra has only the zero trace quotient and the identity stable element, so the assertion is immediate there. First \(K_0(A)\) is countable. Every matrix algebra over the unitization is separable. In its projection space, equivalence classes are open: projections at distance less than one are equivalent by Lesson1. A second-countable space has at most countably many disjoint nonempty open subsets, by assigning a distinct basis element to each. Thus each matrix size has countably many projection classes. Their countable union and its group completion are countable; taking the relative subgroup proves the nonunital case. Consequently \(P_A\) is countable.

For \(u\), fix an integral \(v\in E_A\). If \(v\notin P_A\), for every \(p\in P_A\) the set
\(\{\lambda\in E_A^*:\lambda(v-p)=0\}\)
is a proper closed hyperplane, by Hahn–Banach. It has empty interior. Baire's theorem in the Banach space \(E_A^*\) gives a \(\lambda\) outside their countable union. Then \(t=\lambda T_A\) has \(\lambda(v)\notin\lambda(P_A)=t_*(K_0(A))\); its determinant detects \(u\). Universal determinant zero implies all scalar determinants zero by Theorem2.3, proving the first equality.

For the positive version we need that every bounded complex trace is a linear combination of bounded positive traces. Here is the functional argument, including the uniqueness needed to preserve traciality. In a unital C*-algebra the states form a weak-star compact convex set \(S\), and they norm the selfadjoint part: evaluation at a point of maximum absolute value in \(C^*(1,h)\), extended by norm-preserving Hahn–Banach, gives a state taking absolute value \(\|h\|\). For completeness, a norm-one functional with value one at the unit is positive. For selfadjoint \(a\), the bound
\(\|1+i s a\|\leq(1+s^2\|a\|^2)^{1/2}\)
forces its value on \(a\) to be real by letting real \(s\to0\) from both sides. For \(0\leq a\leq1\), the bound \(|1-f(a)|\leq\|1-a\|\leq1\) then forces \(f(a)\geq0\). This proves the stated extension is a state.

The symmetric convex hull of \(S\) is compact: it is the image of \([0,1]\times S\times S\) under \((r,\sigma,\rho)\mapsto r\sigma-(1-r)\rho\). Real Hahn–Banach and the preceding norming identity show this set equals the unit ball of the real dual of the selfadjoint part. Indeed, a separating selfadjoint element would have a support value larger than its norm, although both sets have support value exactly that norm. A hermitian complex functional has the same norm as its restriction to the selfadjoint part: rotate the value on any element and take its real part. It therefore has a positive decomposition \(f=f_+-f_-\) with \(\|f\|=\|f_+\|+\|f_-\|\).

This norm-additive decomposition is unique. Choose selfadjoint contractions \(h_j\) with \(f(h_j)\to\|f\|\). For any such decomposition,
\(f_+(1-h_j)+f_-(1+h_j)\to0\).
Both summands are nonnegative. Cauchy–Schwarz for a positive functional and \((1\mp h_j)^2\leq2(1\mp h_j)\) imply
\(f_+(a h_j)\to f_+(a)\) and \(f_-(a h_j)\to-f_-(a)\)
for every \(a\). Thus \(f(a h_j)\to(f_++f_-)(a)\). This determines the sum from \(f\) alone, and the difference is already \(f\); both positive parts are unique.

If \(f\) is hermitian and tracial, it is invariant under every inner unitary conjugation. Such conjugation preserves positivity and norms, so uniqueness makes \(f_+\) and \(f_-\) invariant too. Invariance gives \(f_\pm(ua)=f_\pm(au)\) for every unitary \(u\). Every element of a unital C*-algebra is a linear combination of unitaries: for a selfadjoint contraction \(h\), use \(h=(w+w^*)/2\), \(w=h+i(1-h^2)^{1/2}\), and split a general element into real and imaginary parts. Hence \(f_\pm\) are traces. A nonunital hermitian trace first extends by zero on the new unit; its norm-additive positive parts in the unitization restrict to bounded positive traces on \(A\). Splitting any complex trace into its two hermitian parts now proves the required linear-span assertion.

Let \(Q\subseteq E_A^*\) be the cone corresponding to bounded positive traces. It is norm closed, since positivity and cyclicity survive norm limits, and is therefore a complete metric space. If all positive determinants of \(u\) vanish, \(Q\) is covered by the closed sets
\(Q\cap\{\lambda:\lambda(v-p)=0\}\), \(p\in P_A\).
Baire gives one of these with nonempty relative interior. Choose \(\lambda_0\) in that interior. For any \(\lambda\in Q\), the convex combinations \((1-s)\lambda_0+s\lambda\), for sufficiently small \(s>0\), remain in that interior. Their values and the value at \(\lambda_0\) on \(v-p\) are zero, forcing \(\lambda(v-p)=0\). The linear-span assertion makes every element of \(E_A^*\) vanish on \(v-p\); Hahn–Banach gives \(v=p\). This is universal determinant zero. The reverse inclusion follows again by factorization. \(\square\)

Countability is used to choose a single period compatible with the trace family. Knowing separately that each trace sends \(v\) into its own period subgroup does not permit interchanging those quantifiers without this argument.

### 2.3. The positive determinant and its lost phase

**Proposition 2.7 (Fuglede–Kadison normalization).** Let \(A\) be unital and \(\tau\) a bounded positive trace. For every stable invertible \(w\), set

\[
\begin{gathered}
\det_{\tau}^{+}(w)=\exp\big(\tau_n(\log|w|)\big),\\
|w|=(w^*w)^{1/2}.
\end{gathered}
\tag{2.12}
\]

This is positive, unchanged by identity padding and multiplicative on all stable invertibles. On the identity component it equals
\(\exp(\operatorname{Re}(2\pi i\,\Delta_\tau(w)))\);
the expression is independent of the chosen determinant representative.

*Proof.* Positivity of \(|w|\) and invertibility make its logarithm selfadjoint, so the exponent is real. Its value on an added identity block is zero. For \(w\in GL_n(A)_0\), polar decomposition gives \(w=v|w|\), with \(v\in U_n(A)_0\): apply the continuous polar map to a path from \(1\) to \(w\). A unitary path has real \(\Gamma_\tau\), and hence contributes zero to \(\operatorname{Re}(2\pi i\,\Gamma_\tau)\). The positive path \(\exp(s\log|w|)\) contributes \(\tau_n(\log|w|)/(2\pi i)\). Additivity proves the formula. Its period ambiguity is real by Theorem1.2, so multiplication by \(2\pi i\) has real part zero. The homomorphism property of \(\Delta_\tau\) proves multiplicativity when both factors are in the identity component.

For arbitrary invertibles write \(w=v a\), \(z=u b\), with \(u,v\) unitary and \(a,b\) positive invertible. Then \(wz=vu\,(u^*a u)b\). Left multiplication by a unitary leaves the absolute value unchanged; positive functional calculus and cyclicity give \(\tau_n(\log(u^*a u))=\tau_n(\log a)\). The factors \(u^*a u,b\) belong to the identity component through their positive exponential paths. Applying the already-proved multiplicativity to them yields
\(\det_\tau^+(wz)=\det_\tau^+(w)\det_\tau^+(z)\).
This handles all components without assuming a path for \(u\) or \(v\). \(\square\)

The positive determinant discards phase. For \(A=\mathbb C\), \(\tau=\operatorname{id}\), and \(w=e^{2\pi i\theta}\), it is one, while \(\Delta_\tau(w)=\theta+\mathbb Z\). Any noninteger \(\theta\) distinguishes these invariants. More generally, in a nonzero separable unital algebra with a tracial state, \(H_\tau\) is countable by Theorem2.6. Choose a real \(\theta\notin H_\tau\); the scalar unitary \(e^{2\pi i\theta}1\) gives the same strict distinction.

##### 2.4. A universal kernel larger than finite commutators

The following construction is due to de la Harpe and Skandalis, Lemmas9–11 and Proposition12. They credit Alain Connes for the covering lemma. We use the integral projective-space ring proved in [Lesson12, Theorem6.5](KT-OPK-12.md#integral-projective-space-k-theory).

Here \(T\) denotes the universal trace of the algebra under discussion, and \(\Delta_T\) its universal determinant.

**Theorem 2.8 (a separable commutator obstruction).** There is a separable unital C*-algebra \(A\) and a positive invertible \(X\in GL_1(A)_0\) such that \(\Delta_T(X)=0\), whereas no identity padding \(X\oplus I_{p-1}\) is a finite product of multiplicative commutators of elements of \(GL_p(A)\). In particular the kernel of the universal determinant is strictly larger than the derived subgroup of the stable identity component.

The factors in the obstruction below may belong to arbitrary components of \(GL_p(A)\). Thus it also rules out finite products whose factors are required to lie in \(GL_p(A)_0\).

#### A finite covering kills a bundle product

**Lemma 2.8a.** Let \(Z\) be compact Hausdorff and let \(U_1,\ldots,U_m\) be a finite open cover. Suppose complex vector bundles \(E_j,F_j\) over \(Z\) are isomorphic on \(U_j\). Then

\[
\prod_{j=1}^m([E_j]-[F_j])=0\quad\hbox{in }K^0(Z).
\]

*Proof.* Give all bundles Hermitian metrics. An isomorphism \(\beta_j:E_j|_{U_j}\to F_j|_{U_j}\) can be made unitary by replacing it with \(\beta_j(\beta_j^*\beta_j)^{-1/2}\). Functional calculus on the positive invertible fibre maps makes this replacement continuous. Put \(H_j=E_j\oplus F_j\), with \(E_j\) even and \(F_j\) odd. Define \(Q_j\) on \(U_j\) by

\[
Q_j(e,f)=(\beta_j^{-1}f,\beta_j e)
\]

is a selfadjoint unitary, has square one, and reverses parity.

Take the graded tensor bundle \(H=H_1\widehat\otimes\cdots\widehat\otimes H_m\). Its even part is the direct sum of tensor products with an even number of \(F_j\) factors; its odd part uses an odd number. On a homogeneous elementary tensor of parities \(\epsilon_1,\ldots,\epsilon_m\), define, over \(U_j\),

\[
\begin{gathered}
v=v_1\otimes\cdots\otimes v_m,\\
w_j=v_1\otimes\cdots\otimes Q_jv_j
\otimes\cdots\otimes v_m,\\
C_j(v)=(-1)^{\epsilon_1+\cdots+\epsilon_{j-1}}w_j.
\end{gathered}
\]

The sign is essential. Applying \(C_j\) twice restores every parity and gives \(C_j^2=1\). If \(i<j\), applying \(C_i\) changes one of the parities appearing in the sign for \(C_j\); applying \(C_j\) does not change the sign for \(C_i\). The two orders consequently differ by minus one. Thus \(C_iC_j+C_jC_i=0\) on \(U_i\cap U_j\). Each \(C_j\) is odd, selfadjoint, and has norm at most one.

Choose a continuous partition of unity \(\rho_j\) with \(\operatorname{supp}\rho_j\subset U_j\). Such a partition exists by a finite shrinking of the cover, Urysohn functions equal to one on the resulting closed cover, and division by their positive sum. Extend \(D_j=\sqrt{\rho_j}C_j\) by zero off \(U_j\). The extension is continuous: the local operators have norm at most one, and the multiplying function tends to zero wherever it reaches a boundary. Globally,

\[
D_j^2=\rho_j1_H,\qquad D_iD_j+D_jD_i=0\quad(i\ne j).
\]

Consequently \(D=\sum_jD_j\) is an odd selfadjoint unitary, since \(D^2=(\sum_j\rho_j)1_H=1_H\). Its restriction gives a bundle isomorphism \(H^{\rm even}\to H^{\rm odd}\), with inverse supplied by the other restriction. Finally, expansion of the graded tensor bundle gives

\[
[H^{\rm even}]-[H^{\rm odd}]=\prod_j([E_j]-[F_j]).
\]

The two parity bundles are isomorphic, so this difference is zero. \(\square\)

**Lemma 2.8b.** The dual tautological line \(L_n\) over \(\mathbb{CP}^n\) cannot be trivialized by fewer than \(n+1\) open sets.

*Proof.* Let \(S_n\) denote the tautological line and put \(x=[S_n]-[1]\). KT-OPK-12, Theorem 6.5, gives

\[
K^0(\mathbb{CP}^n)=\mathbb Z[x]/(x^{n+1}),
\]

with \(1,x,\ldots,x^n\) an integral additive basis. Since \(L_n=S_n^*\), its class is the inverse of \([S_n]=1+x\). Therefore

\[
\begin{gathered}
\alpha=1-[L_n]=\frac{x}{1+x},\\
\alpha^m=x^m(1+x)^{-m}.
\end{gathered}
\]

For \(1\le m\le n\), the right side is nonzero: \(x^m\ne0\), and multiplication by the unit \((1+x)^{-m}\) is injective. If \(m\) trivializing open sets covered projective space, Lemma 2.8a applied to \(E_j=\mathbf1,F_j=L_n\) would give \(\alpha^m=0\). Hence \(m\ge n+1\). \(\square\)

This conversion to the dual line preserves the exact convention of the provider theorem. It uses an integral ring and an invertible line class, not a conclusion about an integral class inferred solely from rational cohomology.

#### Traceless logarithms in section algebras

For \(n\ge1\), fix a Hermitian metric on \(L_n\oplus\mathbf1\) and define

\[
B_n=\Gamma\bigl(\operatorname{End}(L_n\oplus\mathbf1)\bigr),
\qquad \lambda_n=2^{-n},
\]

\[
Y_n=\begin{pmatrix}\lambda_n1_{L_n}&0\\0&-\lambda_n\end{pmatrix},
\qquad X_n=\exp Y_n.
\]

The upper right corner of an element of \(B_n\) is a section of \(\operatorname{Hom}(\mathbf1,L_n)=L_n\); the lower left corner is a section of \(L_n^*\).

**Lemma 2.8c.** Each \(Y_n\) is a finite sum of additive commutators in \(B_n\).

*Proof.* Choose a finite trivializing cover of \(L_n\), a subordinate partition \(\rho_j\) with supports inside its members, and a unit frame \(s_j\) on each member. Extend by zero the sections

\[
b_j=\sqrt{\lambda_n\rho_j}\,s_j,\qquad
c_j=\sqrt{\lambda_n\rho_j}\,s_j^*.
\]

These are continuous for the same norm bound used in Lemma 2.8a. On each fibre, \(b_jc_j=\lambda_n\rho_j1_{L_n}\) and \(c_jb_j=\lambda_n\rho_j\). With

\[
R_j=\begin{pmatrix}0&b_j\\0&0\end{pmatrix},\qquad
S_j=\begin{pmatrix}0&0\\c_j&0\end{pmatrix},
\]

ordinary multiplication gives

\[
[R_j,S_j]=\begin{pmatrix}\lambda_n\rho_j1_{L_n}&0\\0&-\lambda_n\rho_j\end{pmatrix}.
\]

Summing over the finite partition gives \(Y_n\). \(\square\)

#### The stable multiplicative obstruction

**Lemma 2.8d.** If \(X_n\oplus I_{p-1}\), regarded as an element of \(GL_p(B_n)\), is a product of \(k\ge1\) multiplicative commutators, then \(2kp^2\ge n+1\).

*Proof.* Write the factors of those commutators as \(Z_1,\ldots,Z_{2k}\). Reorder the bundle \((L_n\oplus\mathbf1)^p\) as \(L_n^p\oplus\mathbf1^p\). In these blocks,

\[
Z_j=\begin{pmatrix}a_j&b_j\\c_j&d_j\end{pmatrix},
\]

where \(b_j\) is a \(p\)-by-\(p\) matrix of sections of \(L_n\). There are exactly \(2kp^2\) such entries.

They cannot all vanish at any point \(z\). Otherwise every \(Z_j(z)\) would be invertible lower block triangular. Both diagonal blocks would be invertible \(p\)-by-\(p\) complex matrices, the inverse would remain lower block triangular, and taking the upper diagonal block would preserve products and inverses. The upper diagonal block of the product of multiplicative commutators would then itself be a product of matrix commutators and have ordinary determinant one.

The target upper diagonal block, however, is

\[
\operatorname{diag}(e^{\lambda_n},1,\ldots,1),
\]

and has determinant \(e^{\lambda_n}\ne1\). Notice that identity padding changes neither the exponent nor this determinant: it is \(e^{\lambda_n}\), not \(e^{p\lambda_n}\).

For every entry of every \(b_j\), take the open set where that section is nonzero. The preceding argument says these at most \(2kp^2\) sets cover \(\mathbb{CP}^n\). A nonzero section of a line bundle trivializes it on its nonvanishing set. Lemma 2.8b gives \(2kp^2\ge n+1\). \(\square\)

#### Assembling the separable example

*Proof of the theorem.* Let

\[
I=\bigoplus_{n\ge1}^{c_0}B_n,
\qquad A=I^+.
\]

Each \(B_n\) is separable. Indeed, the compact metric space \(\mathbb{CP}^n\) has separable continuous-function algebra, and a finite embedding of \(L_n\oplus\mathbf1\) into a trivial bundle identifies \(B_n\) with a projection corner of a finite matrix algebra over that function algebra. Closed subspaces of separable metric spaces are separable. Finite supported sequences from countable dense subsets of the \(B_n\) give a countable dense subset of \(I\); adjoining a unit preserves separability.

For completeness, the function-algebra separability used here has an elementary approximation proof. Projective affine charts give a countable dense set \(Q\) by taking rational real and imaginary coordinates. For \(q\in Q\) and positive rational \(r\), put \(\phi_{q,r}(z)=\max(0,r-d(z,q))\). Consider all finite families whose positive sets cover the compact space, normalize their sum to obtain a partition, and take linear combinations with rational complex coefficients. There are only countably many resulting functions. Uniform continuity of any continuous function lets us choose the radii sufficiently small, finitely cover the space, and choose each coefficient close to the function's value at the corresponding centre. The resulting combination approximates the function uniformly. This proves the asserted separability.

Because \(\|Y_n\|=2^{-n}\), the sequence \(Y=(Y_n)_n\) belongs to \(I\). Its finite truncations \(Y^{(N)}\) satisfy \(\|Y-Y^{(N)}\|\le2^{-(N+1)}\). By Lemma 2.8c each truncation is a finite sum of additive commutators in \(I\): insert the finitely many block factors at their respective coordinates and zero elsewhere. The continuity of the universal trace on \(A\) therefore gives \(T(Y)=0\).

Set \(X=\exp Y\). Then \(X=1+(X_n-1)_n\) lies in \(A\), is positive and invertible, and the norm-continuous exponential path \(t\mapsto\exp(tY)\) joins the identity to \(X\). Its derivative multiplied by its inverse is constantly \(Y\); hence its universal logarithmic integral is zero, and \(\Delta_T(X)=0\).

Suppose some \(X\oplus I_{p-1}\) were a product of \(k\) commutators in \(GL_p(A)\). The case \(k=0\) would say \(X\oplus I_{p-1}=I_p\), already false. For \(k\ge1\), evaluation at coordinate \(n\), sending the adjoined unit to \(1_{B_n}\), gives a unital homomorphism \(A\to B_n\). It preserves every factor, inverse and identity padding. Thus Lemma 2.8d would give \(2kp^2\ge n+1\) for every \(n\). Choose \(n>2kp^2\) to contradict this inequality.

Finally any finite product in the stable group uses only finitely many matrix sizes. Padding all its factors with identities puts the product and \(X\) in one common \(GL_p(A)\), to which the preceding argument applies. This proves the claimed stable obstruction. Since the universal determinant kills the derived subgroup, as follows from its product and conjugation identities, this example makes that inclusion strict. \(\square\)

The norm closure in the universal trace quotient is essential to the step \(T(Y)=0\). The conclusion concerns finite multiplicative commutators. It does not identify an algebraic commutator subgroup with its norm closure.

### A determinant kernel that is not norm closed

A determinant kernel can also fail to be norm closed. Use the CAR algebra computed in [Lesson5, Proposition5.1](KT-OPK-05.md#5-normalized-ranks-in-uhf-limits) and [Lesson13, Exercise13.4](KT-OPK-13.md#7-exercises-with-complete-solutions).

**Example 2.9 (CAR scalar phases).** For the CAR algebra \(C=\varinjlim M_{2^r}\), the kernel of the universal determinant, equivalently the determinant for its normalized trace, is not norm closed, even among scalar unitaries. It contains a dense subgroup of the scalar circle, each of whose elements is a single unitary commutator.

*Proof.* The trace \(\tau\) has \(\tau_*(K_0(C))=\mathbb Z[1/2]\), by the specified providers. Consequently

\[
\Delta_\tau(e^{2\pi i t}1_C)=t+\mathbb Z[1/2].
\]

The universal trace quotient here is exactly one complex dimension. To check this without a trace-decomposition theorem, a traceless matrix is a sum of additive commutators: its off-diagonal entries are multiples of \([e_{ij},e_{jj}]=e_{ij}\), and its traceless diagonal is a linear combination of \([e_{iq},e_{qi}]=e_{ii}-e_{qq}\), for \(i<q\). Hence every stage element \(a\) satisfies \(T(a)=\tau(a)T(1_C)\). Approximate an arbitrary element of \(C\) by stage elements and use continuity to get the same identity everywhere. Since \(\tau(1_C)=1\), the class \(T(1_C)\) is nonzero. Thus \(z\mapsto zT(1_C)\) identifies \(\mathbb C\) with the universal trace quotient, and its K-theory period group with \(\mathbb Z[1/2]T(1_C)\). The universal and scalar-trace determinants therefore have the same kernel.

If \(t=a/2^r\), put \(q=2^r\) and \(\zeta=e^{2\pi i a/q}\). In the unital stage \(M_q\subset C\), on its standard basis indexed by \(0,\ldots,q-1\), take

\[
De_j=\zeta^j e_j,\qquad Se_j=e_{j+1\bmod q}.
\]

Since \(\zeta^q=1\), including at the wraparound index these matrices satisfy \(DS=\zeta SD\). They are unitary and hence \(DSD^*S^*=\zeta1_q\), which maps to \(\zeta1_C\). Both factors are in the unitary identity component: each finite complex unitary has a spectral decomposition and thus a selfadjoint logarithm, giving an exponential path inside that stage.

Fix an irrational real \(t\), and let \(t_r=\lfloor2^rt\rfloor/2^r\). Then \(t_r\to t\), so the single-commutator scalars \(e^{2\pi it_r}1_C\), all with zero determinant, converge in norm to \(e^{2\pi it}1_C\). Its determinant is nonzero because an irrational number is not in \(\mathbb Z[1/2]\). All scalar unitaries have an exponential path from the identity. This proves the stated failure of closedness within that component. \(\square\)

The dyadic clock-and-shift construction proves this concrete failure of closedness. The broader classification of irrational scalar commutators in arbitrary AF algebras is a separate theorem.

### Irrational scalar commutators in arbitrary AF algebras

The universal trace remains the quotient \(T_A:A\to E_A=A/C_A\) by the **closed linear span of additive commutators**. Its determinant period subgroup remains the **actual image** \(P_A=(T_A)_*(K_0(A))\), with no closure. For a real irrational \(\theta\), the scalar exponential path and Theorem 2.3 give

\[
\begin{gathered}
\Delta_A(e^{2\pi i\theta}1_A)=0\\
\Longleftrightarrow\quad\exists x\in K_0(A):\\
(T_A)_*(x)=\theta T_A(1_A).
\end{gathered}
\tag{2.A1}
\]

By a unital AF algebra we include nonseparable algebras having a dense directed family of finite-dimensional subalgebras. The proof uses only the following finite approximation property:

\[
\begin{gathered}
\forall S\subset A\text{ finite},\quad\forall\varepsilon>0,\\
\exists F\subset A:\\
F\text{ a finite-dimensional}\\
\text{C*-subalgebra},\\
\operatorname{dist}(s,F)<\varepsilon\quad(s\in S).
\end{gathered}
\tag{2.A2}
\]

A dense directed family has (2.A2): approximate the finitely many elements separately and pass to a common upper stage. When \(A\) is unital, a finite-dimensional \(F\) can be made unital by adjoining \(1_A\); if its old unit is \(p\), the enlarged algebra is \(F\oplus\mathbb C(1_A-p)\). Thus the proof also applies to the explicit local finite approximation hypothesis (2.A2), without making a claim that every nonseparable algebra with (2.A2) has a dense directed family.

**Theorem 2.9a (irrational scalar criterion).** Let \(A\) be a unital C*-algebra satisfying (2.A2), let \(\theta\in\mathbb R\setminus\mathbb Q\), and put \(\lambda=e^{2\pi i\theta}1_A\). The following conditions are equivalent:

1. There are unitaries \(v,u\in A\) with \(\lambda=vuv^*u^*\).
2. \(\lambda\) belongs to the algebraic derived subgroup \(DGL_1(A)\), consisting of finite products of multiplicative commutators.
3. \(\Delta_A(\lambda)=0\) in \(E_A/P_A\).

The factors in condition 1 lie in the original algebra \(A\). Neither stabilization nor norm closure is part of that condition. Irrationality is essential to the pointed-group construction in the difficult implication; this theorem makes no assertion about rational phases in arbitrary AF algebras.

We give the complete prerequisites before finishing the theorem's proof.

#### Connected invertibles for the AF target

**Lemma 2.9b.** A unital C*-algebra satisfying (2.A2) has \(GL_1(A)=GL_1(A)_0\).

*Proof.* Given \(a\in GL_1(A)\), choose \(b\) in a unital finite-dimensional subalgebra \(F\subset A\) with \(\|a-b\|<\|a^{-1}\|^{-1}\). Every point on the segment from \(a\) to \(b\) is invertible, by the Neumann series applied after multiplication by \(a^{-1}\). Invertibility of \(b\) in \(A\) implies invertibility in \(F\): if one matrix block of \(b\) were singular, its nonzero kernel projection \(p\in F\) would satisfy \(bp=0\), contradicting invertibility in \(A\). In \(F\), write \(b=w|b|\). The path \(w((1-t)|b|+t1)\) joins \(b\) to the unitary \(w\) through invertibles. A finite-dimensional unitary has a spectral decomposition, so choose a real argument for each eigenvalue and obtain a selfadjoint \(h\in F\) with \(w=e^{ih}\). The path \(e^{i(1-t)h}\) joins \(w\) to one. Concatenating the paths proves the lemma. \(\square\)

Consequently the universal determinant's homomorphism in Theorem 2.3 is defined on every \(GL_1(A)\) element and kills every algebraic commutator there.

#### Retaining the exact period in a separable target

**Lemma 2.9c.** Let \(E\subset A\) be a finite dimensional unital C*-subalgebra with the same unit as \(A\). Fix matrix units \(e^{\alpha}_{ij}\) for its matrix summands. Given \(\eta>0\), there is \(\delta>0\), depending only on this finite system and \(\eta\), with the following property. If a finite dimensional unital subalgebra \(F\subset A\) satisfies

\[
\operatorname{dist}(e^{\alpha}_{ij},F)<\delta
\quad\text{for all its matrix units},
\]

then a unitary \(u\in A\) satisfies \(\|u-1\|<\eta\) and \(uEu^*\subset F\).

*Proof.* Order all the diagonal matrix units as \(e_1,\ldots,e_N\). They are orthogonal projections with sum one. Choose selfadjoint \(z_k\in F\) close to \(e_k\), by symmetrizing an approximant. Construct orthogonal projections \(f_k\in F\) recursively. If \(k<N\), put

\[
\begin{gathered}
q_k=1-\sum_{l<k}f_l,\\
b_k=q_kz_kq_k,\\
f_k=\chi_{(1/2,\infty)}(b_k),
\end{gathered}
\]

where the functional calculus is performed in the corner \(q_kFq_k\). Put \(f_N=1-\sum_{l<N}f_l\). For sufficiently small initial error the spectrum of every \(b_k\) stays away from \(1/2\), so these expressions are defined. Inductively \(q_k\) approaches \(1-\sum_{l<k}e_l\), \(b_k\) approaches \(e_k\), and \(f_k\) approaches \(e_k\) as the initial error tends to zero. The spectral assertion follows from the Neumann resolvent estimate for a selfadjoint element within a small norm distance of a projection. Continuity of these spectral projections can be seen by choosing a continuous function equal to zero near zero and one near one, and applying continuous functional calculus. Uniform polynomial approximation on a fixed compact interval makes its norm continuity uniform in the ambient algebra. Thus this construction gives an error threshold, rather than merely convergence in one fixed algebra.

Restore the original summand labels to the \(f_k\). For each summand and \(i>1\), choose \(z^{\alpha}_{i1}\in F\) close to \(e^{\alpha}_{i1}\), and set

\[
w_i^{\alpha}=f^{\alpha}_{ii}z^{\alpha}_{i1}f^{\alpha}_{11},\qquad
v_i^{\alpha}=w_i^{\alpha}\bigl((w_i^{\alpha})^*w_i^{\alpha}\bigr)^{-1/2}.
\]

For sufficiently small error, \((w_i^{\alpha})^*w_i^{\alpha}\) is invertible in \(f^{\alpha}_{11}Ff^{\alpha}_{11}\), and \(w_i^{\alpha}(w_i^{\alpha})^*\) is invertible in \(f^{\alpha}_{ii}Ff^{\alpha}_{ii}\). This follows since these elements approach the respective corner units. The formula gives \((v_i^{\alpha})^*v_i^{\alpha}=f^{\alpha}_{11}\). Its final projection \(P=v_i^{\alpha}(v_i^{\alpha})^*\) lies below \(f^{\alpha}_{ii}\) and satisfies \((f^{\alpha}_{ii}-P)w_i^{\alpha}(w_i^{\alpha})^*=0\); invertibility in that corner implies \(P=f^{\alpha}_{ii}\). Put \(v_1^{\alpha}=f^{\alpha}_{11}\) and

\[
f^{\alpha}_{ij}=v_i^{\alpha}(v_j^{\alpha})^*.
\]

Orthogonality of the diagonal projections proves the matrix unit identities, including zero products between distinct summands. Their diagonal sum is one. They therefore define a unital *-homomorphism \(\phi:E\to F\), and \(\phi(e^{\alpha}_{ij})\) approaches \(e^{\alpha}_{ij}\) with the approximation error. To check this last continuity assertion in the ambient algebra despite the moving corner, put \(a_i=(w_i^{\alpha})^*w_i^{\alpha}+1-f^{\alpha}_{11}\). It is positive invertible and approaches \(1\), and \(v_i^{\alpha}=w_i^{\alpha}a_i^{-1/2}\). Thus \(v_i^{\alpha}\) approaches \(e^{\alpha}_{i1}\). The inverse square root is norm continuous on a compact positive spectral interval bounded away from zero; polynomial approximation again gives a uniform error threshold for the finite construction.

Define

\[
s=\sum_{\alpha}\sum_i
\phi(e^{\alpha}_{i1})e^{\alpha}_{1i}.
\]

The matrix unit identities give \(\phi(a)s=sa\) for every \(a\in E\). Also \(s\to1\), since the corresponding expression with \(\phi\) replaced by inclusion is \(\sum_{\alpha,i}e^{\alpha}_{ii}=1\). For sufficiently small initial error \(s\) is invertible. Taking adjoints in the intertwining identity shows that \(s^*s\) commutes with \(E\). Its polar unitary

\[
u=s(s^*s)^{-1/2}
\]

therefore satisfies \(\phi(a)u=ua\), so \(uEu^*=\phi(E)\subset F\). The formula also gives \(u\to1\). Choose the initial threshold small enough that \(\|u-1\|<\eta\). All steps involve only finitely many norm estimates and functional calculus on fixed compact spectral intervals, so one common positive threshold \(\delta\) suffices. \(\square\)

**Lemma 2.9d.** Suppose the unital C*-algebra \(A\) satisfies (2.A2). Every countable subset \(S\subset A\) is contained in a unital separable subalgebra

\[
B=\overline{\bigcup_{n\ge0}E_n},
\qquad
\mathbb C1_A=E_0\subset E_1\subset E_2\subset\cdots,
\]

where all \(E_n\) are finite dimensional and have unit \(1_A\).

*Proof.* Adjoin \(1_A\) to \(S\) if needed and enumerate the resulting nonempty set as \(S=\{s_1,s_2,\ldots\}\), allowing repetitions if it is finite. Suppose \(E_{n-1}\) is constructed. Write \(\varepsilon_n=2^{-n}\), \(M_n=\max_{j\le n}\|s_j\|\), and choose

\[
0<\eta_n<\frac{\varepsilon_n}{4(1+M_n)}.
\]

Apply Lemma 2.9c to \(E_{n-1}\) with this \(\eta_n\), obtaining a matrix unit approximation threshold \(\delta_n\). By (2.A2), choose a finite dimensional subalgebra approximating the matrix units within \(\delta_n\) and \(s_1,\ldots,s_n\) within \(\varepsilon_n/2\). Make it unital by adjoining \(1_A\). This operation preserves finite dimension: if its old unit is \(e\), the enlarged algebra is its direct sum with \(\mathbb C(1_A-e)\), omitting a zero summand when \(e=1_A\). Denote the resulting algebra by \(F_n\).

Lemma 2.9c gives \(u_n\) with \(\|u_n-1\|<\eta_n\) and \(u_nE_{n-1}u_n^*\subset F_n\). Set \(E_n=u_n^*F_nu_n\). Then \(E_{n-1}\subset E_n\) exactly. For \(j\le n\), choose \(y_j\in F_n\) with \(\|y_j-s_j\|<\varepsilon_n/2\). The estimate

\[
\begin{gathered}
\|u_n^*y_ju_n-s_j\|\\
\le\|y_j-s_j\|+2\|u_n-1\|\,\|s_j\|\\
<\varepsilon_n.
\end{gathered}
\]

shows \(\operatorname{dist}(s_j,E_n)<2^{-n}\). Thus each \(s_j\) belongs to the closure of the increasing union. That closure is a C*-subalgebra, and a countable union of finite dimensional algebras has a countable dense subset. Its stages have the common unit \(1_A\). \(\square\)

When a dense directed family is supplied initially, there is also a shorter proof: adjoin \(1_A\) to every finite stage, select stage approximants to each \(s_j\) at errors \(2^{-n}\), and recursively select one common upper stage containing the preceding selected stage and the finitely many new approximants. The preceding proof is included to establish the conclusion even from (2.A2) alone.

For any unital C*-algebra \(C\), define

\[
\begin{gathered}
\mathcal C_C=\{ab-ba:a,b\in C\},\\
C_C=\overline{\operatorname{span}_{\mathbb C}\mathcal C_C},\\
E_C=C/C_C,\\
T_C:C\longrightarrow E_C.
\end{gathered}
\]

Use the unnormalized extension to matrices,

\[
T_C^{(m)}((a_{ij}))=\sum_{i=1}^mT_C(a_{ii}),
\]

and let \(T_{C,*}:K_0(C)\to E_C\) be the induced homomorphism. Its actual period subgroup is

\[
P_C=T_{C,*}(K_0(C)).
\]

**Lemma 2.9e.** Suppose \(A\) is unital and satisfies (2.A2). If a real number \(\theta\) and a class \(x\in K_0(A)\) satisfy

\[
T_{A,*}(x)=\theta T_A(1_A), \tag{2.A3}
\]

then there are a separable unital sequential AF subalgebra \(B\subset A\) and \(x_B\in K_0(B)\) such that, for the inclusion \(\iota:B\hookrightarrow A\),

\[
\begin{gathered}
\iota_*(x_B)=x,\\
T_{B,*}(x_B)=\theta T_B(1_B).
\end{gathered}
\tag{2.A4}
\]

Any prescribed countable set of elements of \(A\) may also be included in \(B\).

*Proof.* Represent \(x=[p]-[q]\) by projections in some common \(M_m(A)\), using zero padding. Set

\[
r=\sum_{i=1}^m p_{ii}-\sum_{i=1}^m q_{ii}-\theta1_A.
\]

Equation (2.A3) says exactly that \(r\in C_A\). Thus for every \(n\ge1\) there is a finite sum

\[
\begin{gathered}
d_{nj}=a_{nj}b_{nj}-b_{nj}a_{nj},\\
c_n=\sum_{j=1}^{k_n}d_{nj},\\
\|r-c_n\|<2^{-n}.
\end{gathered}
\tag{2.A5}
\]

Any scalar coefficient in a linear combination of commutators has been absorbed into its first factor. Form the countable set consisting of \(1_A\), all entries of \(p,q\), every \(a_{nj},b_{nj}\), and the additional prescribed countable set. Apply Lemma 2.9d to it. The resulting subalgebra \(B\) contains \(p,q\in M_m(B)\); they remain projections because all their algebraic relations hold in the subalgebra. Define \(x_B=[p]-[q]\in K_0(B)\). Its image is \(x\).

Every finite sum \(c_n\) in (2.A5) is now an additive commutator sum in \(B\). The inclusion \(B\subset A\) is isometric, so the same estimates hold in \(B\). Therefore \(r\in C_B\). Applying \(T_B\) yields the second equality in (2.A4). \(\square\)

The theorem uses a norm closure only for the **defining additive commutator subspace** \(C_C\). It never takes the norm closure of \(P_C\). The second equality in (2.A4) is an equality in \(E_B\) with the single actual class \(x_B\), hence gives exact membership \(\theta T_B(1_B)\in P_B\).

This distinction is essential. If the selected subalgebra contained only \(p,q\), equation (2.A3) in \(E_A\) would not ensure its counterpart in \(E_B\). The commutator factors in (2.A5) supply that missing implication. Likewise the proof does not require every normalized trace on \(B\) to extend to \(A\). All traces on \(B\) annihilate \(C_B\), so (2.A4) itself gives \(\tau_*(x_B)=\theta\tau(1_B)\) for each such trace.

There is a natural linear map \(J:E_B\to E_A\), because \(C_B\subset C_A\). It satisfies

\[
\begin{gathered}
J(T_B(b))=T_A(b),\\
J(T_{B,*}(y))=T_{A,*}(\iota_*(y)),\\
J(P_B)\subset P_A.
\end{gathered}
\]

The construction preserves the **chosen actual period equality**. It does not claim \(J\) is injective or that one countable subalgebra carries the entire possibly uncountable period subgroup of \(A\). Neither stronger claim is needed for Proposition 13.

#### The complete finite-dimensional smoothing construction

##### Continued fractions and the finite models

Fix irrational \(0<\vartheta<1\), and let \(p_j/q_j\) be its regular continued-fraction convergents, with

\[
\begin{gathered}
p_0=0,\\
q_0=1,\\
p_1=1,\\
q_1=a_1,\\
p_j=a_jp_{j-1}+p_{j-2},\\
q_j=a_jq_{j-1}+q_{j-2}.
\end{gathered}
\]

The determinant \(p_jq_{j-1}-p_{j-1}q_j=(-1)^{j-1}\) follows by induction: the recurrence negates it at every step. Substituting the positive infinite tail \(t=[a_{j+1};a_{j+2},\ldots]>1\) gives

\[
\vartheta=\frac{p_jt+p_{j-1}}{q_jt+q_{j-1}},
\qquad
\left|\vartheta-\frac{p_j}{q_j}\right|
<\frac1{q_jq_{j+1}}.
\]

The finite-tail identity follows by composing the maps \(x\mapsto a+1/x\); the inequality follows by subtracting \(p_j/q_j\) and applying the determinant identity. In particular the convergents tend to \(\vartheta\), consecutive denominators eventually increase strictly, and
\(q_j\geq q_{j-1}+q_{j-2}\geq2q_{j-2}\). Hence \(\sum_jq_j^{-1}<\infty\).

On \(\mathbb C^{q_j}\), with basis \(e_j(1),\ldots,e_j(q_j)\), define

\[
\begin{gathered}
S_je_j(t)=e_j(t+1),\\
C_je_j(t)=\zeta_j^te_j(t),\\
\zeta_j=e^{2\pi ip_j/q_j},
\end{gathered}
\]

where the shift index is cyclic. They are unitaries, and
\(S_j^*C_jS_j=\zeta_jC_j\).
The AF stages will be
\(F_j=M_{q_j}\oplus M_{q_{j-1}}\).

At one step write
\(Q=q_{j-1}\), \(R=q_{j-2}\), \(a=a_j\), and \(N=q_j=aQ+R\).
Choose an integer \(s\) with \(R/4\leq s\leq R/2\); starting at \(j\geq6\) ensures this is possible with \(R\geq4\). Thus \(2s\leq R<Q\).
We construct a unitary

\[
W:(\mathbb C^Q)^a\oplus\mathbb C^R\longrightarrow\mathbb C^N.
\]

Every target basis index below is read modulo \(N\), using \(1,\ldots,N\) as representatives.

##### The corrected columns

For \(0\leq t\leq s\), put

\[
c_t=\cos\frac{\pi t}{2s},\quad
d_t=\sin\frac{\pi t}{2s},\quad
z_t=e^{\pi it/s}.
\]

For copy \(k\), \(1\leq k\leq a\), set

\[
\begin{gathered}
\sigma_k=(-1)^k,\\
h_k=\lfloor k/2\rfloor,\\
A_k=\sigma_kh_kQ,\\
B_k=-\sigma_kh_kQ,\\
D_k=A_k-Q.
\end{gathered}
\]

Write the isometry from this copy as

\[
\begin{aligned}
W_ke(t)={}&\alpha_k(t)e_N(A_k+t)\\
&+\beta_k(t)e_N(B_k+t)\\
&+\gamma_k(t)e_N(D_k+t).
\end{aligned}
\]

The first copy has \(\alpha_1(t)=0\) and \(\beta_1(t)=1\) for \(1\leq t\leq Q-s\). For all other copies, on \(1\leq t\leq s\), define

\[
\alpha_k(t)=z_t^{(1-\sigma_k)/2}c_t,
\qquad
\beta_k(t)=\sigma_kz_t^{(1-\sigma_k)/2}d_t.
\]

For \(k>1\) and \(s<t\leq Q-s\), set \(\alpha_k(t)=0\), \(\beta_k(t)=1\). For every copy, on the tail \(Q-s<t\leq Q\), set \(u=t-Q+s\) and

\[
\begin{gathered}
\alpha_k(t)=0,\\
\beta_k(t)=z_u^{(1-\sigma_k)/2}c_u,\\
\gamma_k(t)=-\sigma_kz_u^{(1+\sigma_k)/2}d_u.
\end{gathered}
\]

Outside that tail \(\gamma_k(t)=0\). Thus each large-block column has at most three specified coordinates and at most two nonzero coordinates.

For the remainder put

\[
\begin{gathered}
H=\lceil a/2\rceil,\\
L=(-1)^{a+1}HQ,\\
M=HQ-\frac{1-(-1)^a}{2}R,
\end{gathered}
\]

and define

\[
W_Re(t)=\lambda(t)e_N(L+t)+\mu(t)e_N(M+t).
\]

If \(a\) is even, on \(1\leq t\leq s\) set
\(\lambda(t)=z_tc_t\), \(\mu(t)=-z_td_t\); on \(s<t\leq R\) set \(\lambda(t)=0\), \(\mu(t)=1\).
If \(a\) is odd, on \(1\leq t\leq R-s\) set \(\lambda(t)=1\), \(\mu(t)=0\); on the remainder tail put \(u=t-R+s\) and set

\[
\lambda(t)=c_u,\qquad \mu(t)=-z_ud_u.
\]

These two changes from the printed tables are deliberate: the first-copy tail has the same phased \(\beta\) as the other odd copies, and the odd remainder's \(\lambda\) has no extra phase. The indices, smoothing length, support sizes and all endpoint values are retained.

##### Exact unitarity, including the remainder

Partition the target coordinates into the following pairs and singleton coordinates. Large-copy head pairs join copies \(2h\) and \(2h+1\); in the ordered rows \((hQ+t,-hQ+t)\), their two columns form

\[
\begin{pmatrix}c_t&-z_td_t\\d_t&z_tc_t\end{pmatrix},
\qquad 1\leq t\leq s.
\tag{2.A6}
\]

Large-copy tail pairs join copies \(2h+1\) and \(2h+2\); in the ordered rows
\(((h+1)Q-s+t,-hQ-s+t)\), their columns form

\[
\begin{gathered}
\begin{pmatrix}z_tc_t&-z_td_t\\d_t&c_t\end{pmatrix},\\
1\leq t\leq s.
\end{gathered}
\tag{2.A7}
\]

This includes the first-copy tail. If \(a=2h\), the last head is paired with the first \(s\) remainder columns and gives (2.A6), using rows \((hQ+t,-hQ+t)\). If \(a=2h+1\), the last tail is paired with the last \(s\) remainder columns and gives (2.A7): the remainder's \(L+R-s+t\) is congruent to \(-hQ-s+t\), and its \(M+R-s+t\) is \((h+1)Q-s+t\).

Both matrices have orthonormal columns, since \(|z_t|=1\), \(c_t^2+d_t^2=1\), and their column inner products are zero. All other columns are singleton coordinate vectors. To check that these planes and singletons do not overlap, use the disjoint base bands

\[
I_k=\{B_k+t:1\leq t\leq Q\},
\]

and the remainder band
\(I_R=\{HQ+t:1\leq t\leq R\}\).
In the odd case this is the band given by \(L=HQ\); in the even case it is given by \(M=HQ\). More explicitly,
\(I_{2h}=\{-hQ+1,\ldots,-(h-1)Q\}\) and
\(I_{2h+1}=\{hQ+1,\ldots,(h+1)Q\}\).
When \(a=2H\), the bands together are the integer interval
\([-HQ+1,HQ+R]\); when \(a=2H-1\), they are
\([-(H-1)Q+1,HQ+R]\). Each interval has length \(N\), so reduction modulo \(N\) partitions the target coordinates. A head plane uses the first \(s\) positions of bands \(2h,2h+1\), with the remainder replacing the latter at the final even head. A tail plane uses the last \(s\) positions of bands \(2h+1,2h+2\), with the remainder replacing the latter at the final odd tail. The unused positions are exactly the singleton columns. Since \(2s\leq R<Q\), these head and tail windows are disjoint. This verifies every coordinate and every column, so
\(W=W_1\oplus\cdots\oplus W_a\oplus W_R\) is exactly unitary.

For comparison, the printed first tail and second tail on a shared plane give columns \((c_t,d_t)\) and \((-z_td_t,c_t)\), with inner product \((1-z_t)c_td_t\). It is nonzero, for example at \(s=2,t=1\). The corrected (2.A7) makes the inner product vanish. The same check determines the odd-remainder correction. This is an algebraic correction, not an inference from numerical closeness.

##### Complete shift bounds

Every scalar coefficient in the construction is a constant, a sine or cosine, or the product of one of these with \(z_t\), up to a sign. The derivative magnitudes on \([0,s]\) are bounded by

\[
\Lambda=\frac{3\pi}{2s}\leq\frac{6\pi}{R}.
\]

At the head/middle transition, \(c_s=0\) and
\(\sigma_kz_s^{(1-\sigma_k)/2}d_s=1\), so the formulas agree with the constant middle values. At the middle/tail transition the tail starts at \(\beta=1,\gamma=0\). At the tail endpoint every \(\gamma_k(Q)=1\), \(\beta_k(Q)=0\). The remainder transitions have the same agreements. Therefore the difference of each coefficient at neighboring indices is bounded by \(\Lambda\), including the transition indices.

For \(t<Q\), the error
\(E_k=W_kS_{j-1}-S_jW_k\) has column

\[
\begin{aligned}
{}&(\alpha_k(t+1)-\alpha_k(t))e_N(A_k+t+1)\\
&+(\beta_k(t+1)-\beta_k(t))e_N(B_k+t+1)\\
&+(\gamma_k(t+1)-\gamma_k(t))e_N(D_k+t+1).
\end{aligned}
\]

The cyclic column also has the required bound. For \(k>1\),
\(A_k+1=D_k+Q+1\) and \(\gamma_k(Q)=1\), so it is

\[
\begin{aligned}
{}&(\alpha_k(1)-1)e_N(A_k+1)\\
&+\beta_k(1)e_N(B_k+1).
\end{aligned}
\]

Here the head formulas start at \(\alpha_k(0)=1\), \(\beta_k(0)=0\), hence both coefficients have magnitude at most \(\Lambda\). For \(k=1\), \(B_1+1=D_1+Q+1\) and the two unit coefficients cancel exactly. Each of the three coordinate routes is an injective partial permutation of the input basis, including its cyclic endpoint; a diagonal coefficient bound \(\Lambda\) gives operator norm at most \(\Lambda\) for that route. Adding these routes proves

\[
\|E_k\|\leq3\Lambda\leq\frac{18\pi}{R}.
\tag{2.A8}
\]

For the remainder error \(E_R=W_RS_{j-2}-S_jW_R\), the two noncyclic routes have the same difference bound. If \(a\) is even, \(M+R+1\equiv L+1\pmod N\), and the cyclic column is
\((\lambda(1)-1)e_N(L+1)+\mu(1)e_N(M+1)\), also bounded by \(\Lambda\) on each route. If \(a\) is odd, \(M+R+1=L+1\), and the cyclic column cancels exactly. Consequently

\[
\|E_R\|\leq2\Lambda\leq\frac{12\pi}{R}.
\tag{2.A9}
\]

These are operator estimates, not merely bounds on the individual columns.

To combine the large blocks uniformly in \(a\), label the base bands \(I_k\) by \(k\), and \(I_R\) by \(a+1\). From the explicit head and tail indices, the coordinate support of \(W_k\) is contained in bands with labels \(k-1,k,k+1\), omitting nonexistent bands. Moving a coordinate forward by one either stays in its band or enters an adjacent band in the cyclic ordering

\[
\begin{gathered}
(\text{even labels in decreasing order}),\\
1,3,5,\ldots,\quad a+1.
\end{gathered}
\]

Adjacent labels in this order differ by at most two, including the cyclic seam: for even \(a\), the seam joins \(a+1\) to \(a\); for odd \(a\geq3\) it joins \(a+1\) to \(a-1\); and for \(a=1\) it joins label two to label one. Thus the range support of \(E_k\) lies in bands whose labels differ from \(k\) by at most three. The ranges of \(E_k\) and \(E_l\) are orthogonal when \(|k-l|>6\).

Group the copy labels by their residue modulo seven. In each group both their input spaces and error ranges are orthogonal, so the direct-sum error norm is the maximum of its individual norms. Summing the seven groups and the remainder gives

\[
\begin{gathered}
\begin{aligned}
E_{\rm sh}&=W(S_{j-1}^{\oplus a}\oplus S_{j-2})\\
&\quad-S_jW,
\end{aligned}\\
\|E_{\rm sh}\|\leq7\frac{18\pi}{R}+\frac{12\pi}{R}\\
=\frac{138\pi}{R}\leq\frac{300\pi}{R}.
\end{gathered}
\tag{2.A10}
\]

The last bound retains the source's stated global constant, while its proof uses seven colors and the sharper route estimates above.

##### Complete clock bounds

If a large-copy column coordinate has index \(x=mQ+t\), the formulas give \(|x|\leq N\). Since \(\zeta_{j-1}^{mQ+t}=\zeta_{j-1}^t\), the convergent determinant identity yields

\[
\left|\zeta_{j-1}^t-\zeta_j^x\right|
\leq2\pi|x|\left|\frac{p_{j-1}}Q-\frac{p_j}N\right|
\leq\frac{2\pi}{Q}.
\]

Changing the signed representative by \(N\) does not change the target phase; the displayed raw indices provide the bounded representative needed in this estimate. Three injective coefficient routes therefore give

\[
\|W_kC_{j-1}-C_jW_k\|\leq\frac{6\pi}{Q}.
\tag{2.A11}
\]

A remainder coordinate is \(y=mQ+lR+t\) with \(|y|\leq N\) and \(|lR+t|\leq Q\). Compare first to the preceding clock phase, then to the current one:

\[
\begin{aligned}
|\zeta_{j-2}^t-\zeta_j^y|
&\leq |\zeta_{j-2}^{lR+t}-\zeta_{j-1}^{lR+t}|
 +|\zeta_{j-1}^{y}-\zeta_j^y|\\
&\leq2\pi\left(\frac1R+\frac1Q\right).
\end{aligned}
\]

The two coefficient routes give a bound \(4\pi(1/R+1/Q)\), in particular the source's weaker bound

\[
\begin{gathered}
\|W_RC_{j-2}-C_jW_R\|\\
\leq6\pi\left(\frac1R+\frac1Q\right).
\end{gathered}
\tag{2.A12}
\]

The clock errors have coordinate supports contained in the support of \(W_k\) itself, hence in bands with labels differing by at most one. Copies with labels differing by more than two have orthogonal error ranges. Grouping by residues modulo three, and then adding the remainder, proves

\[
\begin{gathered}
\begin{aligned}
E_{\rm cl}&=W(C_{j-1}^{\oplus a}\oplus C_{j-2})\\
&\quad-C_jW,
\end{aligned}\\
\|E_{\rm cl}\|\leq\frac{24\pi}{Q}+\frac{6\pi}{R}\\
\leq\frac{42\pi}{Q}+\frac{7\pi}{R}.
\end{gathered}
\tag{2.A13}
\]

Thus the source's global clock bound holds uniformly even for unbounded partial quotients.

##### The actual inductive maps and norm limits

Define the unital injective *-homomorphism

\[
\begin{gathered}
\rho_j:F_{j-1}\longrightarrow F_j,\\
\begin{aligned}
\rho_j(x\oplus y)&=W(x^{\oplus a_j}\oplus y)W^*\\
&\quad\oplus x.
\end{aligned}
\end{gathered}
\]

It is unital because \(W\) is unitary. It is injective because \(a_j\geq1\), its second summand records \(x\), and the first summand records \(y\). Its multiplicity matrix, on rank vectors of minimal projections, is
\(H_j=\left(\begin{smallmatrix}a_j&1\\1&0\end{smallmatrix}\right)\).
Let \(D_\vartheta\) be the C*-inductive limit of these actual maps, starting at \(F_5\), and identify the stages with their faithful images in the limit.

Put \(u_j=S_j\oplus S_{j-1}\), \(v_j=C_j\oplus C_{j-1}\). Equations (2.A10) and (2.A13) give

\[
\begin{gathered}
\|\rho_j(u_{j-1})-u_j\|\leq\frac{300\pi}{q_{j-2}},\\
\|\rho_j(v_{j-1})-v_j\|\\
\leq\frac{42\pi}{q_{j-1}}+\frac{7\pi}{q_{j-2}}.
\end{gathered}
\]

These bounds are summable. Thus both stage sequences are Cauchy in the limit and converge in norm to elements \(U,V\). Norm limits of unitaries are unitary, since multiplication and involution are norm continuous.
In the two stage summands,
\(u_j^*v_ju_j=(\zeta_jC_j)\oplus(\zeta_{j-1}C_{j-1})\).
Both scalar phases tend to \(e^{2\pi i\vartheta}\). Taking norm limits yields

\[
\begin{gathered}
U^*VU=e^{2\pi i\vartheta}V,\\
VU=e^{2\pi i\vartheta}UV,\\
VUV^*U^*=e^{2\pi i\vartheta}1.
\end{gathered}
\]

Lesson 20, Proposition 1.1, supplies the unital homomorphism
\(A_\vartheta\to D_\vartheta\), sending its coefficient generator to \(U\) and its implementing generator to \(V\). Proposition 1.2 makes it injective: its kernel is an ideal in the simple irrational rotation algebra, and the unital map has nonzero range. This completes the constructive embedding, including the actual conjugacies, support bounds, norm control and unit.

#### The exact normalized ordered group of the constructed AF algebra

This calculation removes the need to import the Effros–Shen ordered-group identification cited on original p. 209. The required smoothing construction was proved in full in the preceding section.

Put

\[
\delta_j=q_j\vartheta-p_j,\qquad r_j=|\delta_j|.
\]

The elementary continued-fraction facts needed here are

\[
\begin{gathered}
\operatorname{sgn}\delta_j=(-1)^j,\\
p_jq_{j-1}-p_{j-1}q_j=(-1)^{j-1},\\
p_j/q_j\longrightarrow\vartheta.
\end{gathered}
\]

The determinant and convergence were proved in the continued-fraction subsection. Its positive-tail formula also gives the displayed alternating sign of \(\delta_j\).

The recurrence and the alternating signs give

\[
r_{j-2}=a_jr_{j-1}+r_j,
\qquad q_jr_{j-1}+q_{j-1}r_j=1.
\]

At stage \(F_j\), identify K-classes with rank vectors \((k,l)\in\mathbb Z^2\), using KT-OPK-03, Examples 5.1–5.2. Define

\[
\chi_j(k,l)=kr_{j-1}+lr_j\in G_\vartheta:=\mathbb Z+\vartheta\mathbb Z.
\]

The first identity above says \(\chi_jH_j=\chi_{j-1}\), so these maps agree under the connecting maps. Moreover \(r_{j-1},r_j\) form an integral basis of \(G_\vartheta\): their coefficients with respect to \(1,\vartheta\) have determinant of absolute value one by the convergent determinant identity. Thus each \(\chi_j\) is an additive group isomorphism.

We must still identify the cone, rather than merely the group. For \(g=A+B\vartheta\), its coordinates in this stage basis are exactly

\[
k_j=q_jA+p_jB,\qquad l_j=q_{j-1}A+p_{j-1}B.
\]

Substitution, using the determinant identity, verifies the formula. If \(g>0\), then \(k_j/q_j\to g\) and \(l_j/q_{j-1}\to g\); both coordinates are therefore positive for sufficiently large \(j\). Conversely, a nonzero nonnegative rank vector has positive value under \(\chi_j\), since both \(r\)'s are positive. By K-theory continuity and its positive-cone assertion, KT-OPK-05, Theorem 3.3, the direct-limit cone is exactly \(G_\vartheta\cap[0,\infty)\).

The stage unit has rank vector \((q_j,q_{j-1})\) and maps to one. Consequently

\[
\begin{gathered}
\bigl(K_0(D_\vartheta),K_0(D_\vartheta)^+,[1]\bigr)\\
\cong\bigl(G_\vartheta,G_\vartheta\cap[0,\infty),1\bigr).
\end{gathered}
\]

This conclusion is independent of the unitary conjugations in the stage inclusions, because they preserve ranks.

There is a compatible normalized trace at each stage,

\[
\sigma_j=r_{j-1}\operatorname{Tr}_{q_j}+r_j\operatorname{Tr}_{q_{j-1}}.
\]

The two identities for the \(r\)'s prove respectively compatibility and normalization. Positivity and norm one allow its unique continuous extension from the dense union, and the trace identity extends by continuity. Its K-pairing is \(\chi_j\) at each stage, so the pairing is the displayed order isomorphism, with unit one. This proves the entire normalized range, not just containment in \(G_\vartheta\).

Any positive homomorphism \(G_\vartheta\to\mathbb R\) sending one to one must send \(\vartheta\) to \(\vartheta\): apply it to the positive elements \(q\vartheta-p\) or \(p-q\vartheta\) for rational bounds \(p/q\) on either side. Thus the pointed ordered group has a unique state. A tracial state on \(D_\vartheta\) is determined by its values on the stage minimal projections, so the normalized trace is unique as well.

#### Strict positivity and an actual unital realization map

These lemmas are restricted to targets given as increasing dense unions of finite-dimensional **unital** C*-subalgebras. No realization theorem for uncountable dimension groups is assumed or proved here.

**Lemma 2.9f (strict trace positivity).** Let \(C=\overline{\bigcup_m C_m}\) be such a unital sequential AF algebra. If \(y\in K_0(C)\) satisfies \(\tau_*(y)>0\) for every normalized tracial state \(\tau\), then \(y\) is positive in \(K_0(C)\).

*Proof.* Represent \(y\) at one finite-dimensional stage by its integer rank vector. If \(y\) were not positive, its vector at every later stage would have a negative coordinate; otherwise K-theory continuity would make it positive. For each later stage choose the normalized matrix trace of a summand with such a negative coordinate. Its value on the image of \(y\) is negative. Restrict these traces to every preceding stage. Each finite-dimensional tracial state space is compact. Successive subsequences, followed by the diagonal subsequence, give compatible limiting normalized traces on all the stages. They extend by norm one and density to a normalized trace \(\tau\) on \(C\). Its value on \(y\), computed at the one fixed initial stage, is a limit of negative numbers and hence is at most zero. This contradicts the hypothesis. The same compactness argument, starting with arbitrary stage traces, ensures the existence of a normalized trace. \(\square\)

**Lemma 2.9g (positive pointed maps).** Let \(D=\overline{\bigcup_j D_j}\) and \(C=\overline{\bigcup_m C_m}\) be unital sequential AF algebras with finite-dimensional unital stages. Every positive group homomorphism \(h:K_0(D)\to K_0(C)\) carrying \([1_D]\) to \([1_C]\) is induced by a unital *-homomorphism \(D\to C\).

*Proof.* First fix a finite-dimensional domain \(D_j=\bigoplus_iM_{d_i}\). The images under \(h\) of its minimal-projection classes are positive. By continuity of the positive cone, lift all these finitely many classes to nonnegative integer vectors in one target stage. Their sum with coefficients \(d_i\) agrees in the limit with the target unit class. Equality in a group direct limit holds at a later stage, so after advancing the target stage the same weighted sum agrees exactly with its dimension vector. Interpret the lifted integers as multiplicities. They define a unital representation of \(D_j\) in that target stage, inducing the required K-map to \(K_0(C)\).

We also need exact compatibility, not only compatible K-maps. Two unital maps between finite-dimensional C*-algebras with the same multiplicity matrix are unitarily conjugate in the target. To see this in each target matrix summand, the images of the domain central units split its Hilbert space. For a domain matrix block, the image of a first diagonal matrix unit has dimension equal to the multiplicity; the images of the off-diagonal matrix units identify its copies with the other diagonal ranges. Choosing an orthonormal basis in the first range therefore identifies the entire representation with that number of copies of the standard matrix representation. Equal multiplicities give unitary equivalence in every target summand, and their direct sum gives the required unitary.

Construct maps on the \(D_j\) successively. Suppose a map on \(D_j\) has been realized in a target stage. Realize the required K-map on \(D_{j+1}\) in some later target stage as in the first paragraph. Its restriction to \(D_j\) and the previously constructed map have the same K-map in the limit. For the finitely many minimal-projection generators, equality holds at a further common stage. The two finite-dimensional representations then have the same multiplicity matrix there. Conjugate the new map by the unitary from the preceding paragraph so that its restriction agrees **exactly** with the earlier map. Continue inductively. The resulting compatible unital *-homomorphisms extend contractively from the dense union to \(D\to C\), and continuity shows that their induced K-map is \(h\). \(\square\)

#### Proof of the irrational scalar criterion

Condition 1 implies condition 2 by the definition of the derived subgroup. Condition 2 implies condition 3 because Lemma 2.9b places the factors in the determinant's identity-component domain and its abelian-valued homomorphism annihilates each multiplicative commutator. These implications use finite products, without taking closures.

Assume condition 3. By (2.A1), choose one actual class \(x\in K_0(A)\) with \((T_A)_*(x)=\theta T_A(1_A)\). Lemma 2.9e of the exact-period subsection gives a unital separable sequential AF subalgebra \(B\subset A\) and \(x_B\in K_0(B)\) with the **exact** equality

\[
(T_B)_*(x_B)=\theta T_B(1_B).
\tag{2.A14}
\]

In particular every normalized trace \(\tau\) on \(B\) satisfies \(\tau_*(x_B)=\theta\). This uses (2.A14), not a claim that every trace of \(B\) extends to \(A\).

Put \(\vartheta=\theta-\lfloor\theta\rfloor\in(0,1)\) and \(x'_B=x_B-\lfloor\theta\rfloor[1_B]\). Because \(\vartheta\) is irrational, every element of \(G_\vartheta=\mathbb Z+\vartheta\mathbb Z\) has a unique expression \(m+n\vartheta\). Define the group map

\[
\begin{gathered}
h:G_\vartheta\longrightarrow K_0(B),\\
\begin{aligned}
h(m+n\vartheta)&=m[1_B]\\
&\quad+nx'_B.
\end{aligned}
\end{gathered}
\tag{2.A15}
\]

It carries one to \([1_B]\). If \(m+n\vartheta>0\), then every normalized trace of its image has precisely that strictly positive value. Lemma 2.9f of the realization subsection makes \(h(m+n\vartheta)\) positive in \(K_0(B)\). The zero element maps to zero, so \(h\) is a positive pointed homomorphism.

The full stage calculation in the ordered-group subsection identifies \(K_0(D_\vartheta)\), its cone and its unit with \(G_\vartheta,G_\vartheta\cap[0,\infty),1\). Compose that identification with \(h\). Lemma 2.9g of the realization subsection realizes the resulting positive pointed map by an **actual unital** *-homomorphism \(\psi:D_\vartheta\to B\).

The norm limits in the smoothing subsection are unitaries \(U,V\in D_\vartheta\) with

\[
VUV^*U^*=e^{2\pi i\vartheta}1_{D_\vartheta}.
\tag{2.A16}
\]

Apply the unital homomorphism \(\psi\), then the inclusion \(B\subset A\). The resulting unitaries \(v=\psi(V)\) and \(u=\psi(U)\), regarded as elements of \(A\), satisfy

\[
vuv^*u^*=e^{2\pi i\vartheta}1_A
=e^{2\pi i\theta}1_A=\lambda.
\]

This proves condition 1 and the theorem. The zero algebra, if allowed in the convention for unital algebras, satisfies the conclusion trivially and may be removed before the normalized-trace arguments. \(\square\)

The construction of the single commutator uses the norm-limit unitaries themselves. It needs no simplicity theorem for rotation algebras. Simplicity is used only for the additional statement in the smoothing subsection that their universal map is a faithful rotation-algebra embedding. The arbitrary-target passage is carried by the exact period extraction in the exact-period subsection, followed by a sequential finite-stage realization in the realization subsection. It imports no nonseparable AF classification theorem, continuum hypothesis, or uncountable dimension-group realization theorem.

The matrix traces throughout the ordered calculation are **unnormalized**. Normalization is encoded by the explicit weights and the unit equation \(q_jr_{j-1}+q_{j-1}r_j=1\). Replacing those traces by normalized block traces without changing the weights would change both the group identification and the period condition.

Human-source proof locators: de la Harpe–Skandalis, Proposition 13, printed pp. 258–259; Pimsner–Voiculescu, construction pp. 202–204, Lemma 1 pp. 204–208, Lemma 2 and norm limits p. 208, theorem pp. 208–209. The two smoothing phase repairs in the smoothing subsection are explicitly proved there. The positive cone, unit, finite-stage realization and exact countable-target reduction have complete proofs above, so the external classification results cited by the original papers are not imported.

### 2.5. Extending a determinant to every stable unitary

The quotient determinant so far is defined on the identity component. Exel's theorem answers when its circle normalization extends to all components. Let \(A\) be unital, and let \(\tau\) be a bounded hermitian tracial functional with \(\tau(1)=1\). Thus \(\tau(a^*)=\overline{\tau(a)}\); positivity is not required. Put \(U=U_\infty(A)\), \(U_0=U_\infty(A)_0\), \(H=\tau_*(K_0(A))\). Thus \(\mathbb Z\subseteq H\). A circle-valued determinant with this normalization is a homomorphism

\[
\begin{gathered}
D:U\longrightarrow\mathbb T,\\
D(e^{ih})=e^{i\tau_n(h)},\\
h=h^*\in M_n(A).
\end{gathered}
\tag{2.14}
\]

There is no assumption that a representative of a nonzero stable \(K_1\)-class has a path from the identity.

**Lemma 2.10a (extension of a character).** A homomorphism from a subgroup of an abelian group to \(\mathbb T\) extends to the whole group.

*Proof.* Order extensions on intermediate subgroups by inclusion. Unions along chains give an upper bound, so Zorn supplies a maximal extension \(\chi:L\to\mathbb T\). If \(x\) lies outside \(L\), the integers \(k\) with \(kx\in L\) form a subgroup of \(\mathbb Z\). If it is zero, choose any \(z\in\mathbb T\) and set \(\chi'(a+kx)=\chi(a)z^k\). If it is \(m\mathbb Z\), \(m>0\), choose an \(m\)-th root \(z\) of \(\chi(mx)\) and use the same rule. It is well defined: an equality \(a+kx=b+\ell x\) makes \(k-\ell=jm\), \(b-a=jmx\), and hence \(\chi(b)=\chi(a)z^{k-\ell}\). In the zero-subgroup case an equality forces \(k=\ell\), \(a=b\). Both rules give a homomorphism on the strictly larger subgroup \(L+\mathbb Zx\), contradicting maximality. \(\square\)

Let \(N_\tau\) consist of stable finite products \(e^{ih_1}\cdots e^{ih_r}\), with selfadjoint exponents and \(\sum_j\tau(h_j)=0\). Products concatenate lists, and inverses reverse and negate them, so this is a subgroup. Unitary conjugation preserves the trace sum, so it is normal in \(U\). It is contained in \(U_0\); no closure is taken.

**Lemma 2.10b (the scalar extension group).** The group \(Q_\tau=U/N_\tau\) is abelian and fits into the exact sequence

\[
\begin{gathered}
0\longrightarrow e^{2\pi iH}\longrightarrow\mathbb T
\xrightarrow{j}Q_\tau\\
\xrightarrow{\pi}K_1(A)\longrightarrow0.
\end{gathered}
\tag{2.15}
\]

Here \(j(z)\) is represented by \(z1_A\) in one matrix slot, followed by identities, and \(\pi\) takes the stable \(K_1\)-class.

*Proof.* For two unitary representatives \(u,v\), pad to one size \(n\). Put \(B=\operatorname{diag}(u,1_n)\), \(V=\operatorname{diag}(v,v^*)\). The latter belongs to \(U_0\): with the scalar block rotation \(R_s\), \(0\leq s\leq\pi/2\), the path
\(\operatorname{diag}(v,1_n)R_s\operatorname{diag}(1_n,v^*)R_s^*\)
starts at \(V\) and ends at the identity. Subdividing its reverse path into increments near the identity expresses \(V\) as a finite product \(e^{ik_j}\) with selfadjoint \(k_j\). Thus \(BVB^*V^*\) is a product of \(e^{iBk_jB^*}\) followed by the reversed \(e^{-ik_j}\); its exponent traces sum to zero. Its endpoint is \(\operatorname{diag}(uvu^*v^*,1_n)\). Every stable commutator is therefore in \(N_\tau\), proving that \(Q_\tau\) is abelian.

The map \(\pi\) is well defined and onto because \(N_\tau\subseteq U_0\) and \(U/U_0=K_1(A)\). If its class is zero, its representative is, after padding, a product \(e^{ih_j}\). Put \(s=\sum_j\tau(h_j)\). Appending the one-slot exponential with exponent \(-s1_A\), zero in the other slots, gives total trace zero. Its class in \(Q_\tau\) is consequently the same as \(j(e^{is})\). Conversely scalar unitaries have exponential paths. This proves \(\ker\pi=\operatorname{im}j\).

If \(t=\tau(p)-\tau(q)\in H\), place the projections and a scalar slot in a common matrix size. The product of exponentials with selfadjoint exponents \(2\pi tE_{11}\), \(-2\pi p\), \(2\pi q\) has total trace zero, and endpoint equal to the one-slot scalar \(e^{2\pi it}\), since the last two exponentials are identities. Thus \(j(e^{2\pi it})=0\). Conversely if this scalar has a factorization of total trace zero, concatenate its scalar path with the reversed factorization path. The based loop has logarithmic integral \(t\), so Lemma2.2 gives \(t\in H\). This proves \(\ker j=e^{2\pi iH}\), and all assertions in (2.15). \(\square\)

**Theorem 2.10 (Exel's extension theorem).** A determinant (2.14) on all stable unitaries exists if and only if \(H\subseteq\mathbb Z\), equivalently \(H=\mathbb Z\). If one \(D_0\) exists, all are

\[
\begin{gathered}
D(v)=D_0(v)\chi([v]),\\
\chi\in\operatorname{Hom}(K_1(A),\mathbb T).
\end{gathered}
\tag{2.16}
\]

Every such determinant is norm continuous on each finite \(U_n(A)\). On \(U_0\), it is necessarily \(\exp(2\pi i\Delta_\tau)\).

*Proof.* For any projection \(p\), \(e^{2\pi ip}=1\) and the normalization force \(e^{2\pi i\tau(p)}=1\). Projection differences generate \(K_0(A)\), proving \(H\subseteq\mathbb Z\). The opposite containment follows from \(\tau(1)=1\).

Conversely, this condition makes \(e^{2\pi iH}\) trivial, so (2.15) embeds \(\mathbb T\) into the abelian group \(Q_\tau\). Lemma2.10a extends the inverse character on this embedded circle to a character of \(Q_\tau\). Composing with \(U\to Q_\tau\) gives \(D\). The exponential \(e^{ih}\) and the one-slot scalar \(e^{i\tau_n(h)}\) have the same class, because their quotient has an exponential factorization with total trace zero. Thus \(D\) has exactly the required normalization.

Two normalized determinants agree on \(U_0\), whose elements have finite selfadjoint exponential factorizations. Their ratio therefore factors uniquely through \(K_1(A)\); conversely multiplication by any such character preserves normalization. This proves (2.16). Near the identity in \(U_n(A)\), its continuous logarithm has the form \(ih\) with \(h=h^*\), so \(D(v)=e^{i\tau_n(h)}\) is continuous. Translation by the homomorphism proves continuity at every point. An exponential factorization of a path gives its determinant integral, so the restriction to \(U_0\) equals the stated exponential of \(\Delta_\tau\). Its exact periods are integers, making that expression well defined. \(\square\)

For the normalized trace on \(M_2(\mathbb C)\), a rank-one projection has trace \(1/2\), so (2.14) cannot hold even on the identity component. The quotient determinant into \(\mathbb R/(\tfrac12\mathbb Z)\) is still defined. The period subgroup and the chosen normalization determine which circle target is available. In the CAR example, \(H=\mathbb Z[1/2]\), so the same obstruction applies.

## 3. The determinant of an ideal class

Consider any C*-extension

\[
0\longrightarrow J\xrightarrow{j}B\xrightarrow{q}A\longrightarrow0.
\tag{3.1}
\]

The pulled-back trace is \(\rho=\tau\circ q\). Naturality from Lesson 13 gives two real subgroups

\[
\begin{gathered}
H_A=\tau_*(K_0(A)),\\
H_B=\rho_*(K_0(B))
=\tau_*q_*(K_0(B))\subset H_A.
\end{gathered}
\tag{3.2}
\]

Let \([u]\in\ker(j_*:K_1(J)\to K_1(B))\). After stabilization choose a normalized ideal unitary representative \(u\), and a normalized piecewise smooth unitary path \(\xi\) in \(B^+\) from the identity to \(j^+(u)\). Such a path exists by the definition of the zero stable K-class and the smoothing argument in §1. Define

\[
\mathcal D_\tau[u]=\Gamma_\rho(\xi)\pmod{H_B}.
\tag{3.3}
\]

When unitizations are needed, all integrals use the zero-on-the-new-unit linear trace. The quotient path \(q^+(\xi)\) is a based loop: both quotient endpoints are the identity. Moreover \(\Gamma_\rho(\xi)=\Gamma_\tau(q^+(\xi))\), so its value belongs to \(H_A\). Thus (3.3) takes values in the subgroup \(H_A/H_B\) of \(\mathbb R/H_B\).

**Lemma 3.1.** Equation (3.3) gives a well-defined homomorphism on \(\ker j_*\).

*Proof.* Two choices of \(B\)-path differ by a based \(B\)-loop; its integral is in \(H_B\) by Theorem 1.2 for \(\rho\). If two ideal representatives are stably homotopic, append that ideal homotopy to one \(B\)-path. Its logarithmic derivative lies in the ideal, where \(\rho\) vanishes, so its integral is zero. This proves representative independence as well as path independence. Zero and identity stabilization preserve the integral, and pointwise product or block-sum paths prove additivity. \(\square\)

The target in (3.3) is essential. The ordinary determinant in \(A\), modulo \(H_A\), would assign zero to the quotient endpoint \(1\) and discard the quotient loop period. We are taking the determinant for \(\rho\) in \(B\), with its smaller period group \(H_B\).

Let \(\varepsilon:K_0(A)\to K_1(J)\) be Lesson 11's positive exponential boundary. For a relative projection \(e\) with scalar part \(P\), choose a selfadjoint lift \(b\) in the external matrix unitization of \(B\), with the same scalar part. Then \(\varepsilon([e]-[P])\) is represented by \(\exp(2\pi i b)\), whose quotient and scalar parts are the identity. A path to it is

\[
\begin{gathered}
\xi_b(t)=f_b(t)f_P(t)^{-1},\\
f_b(t)=\exp(2\pi it b).
\end{gathered}
\tag{3.4}
\]

Its quotient is the positive loop \(\ell_{e,P}\). The product integral calculation gives

\[
\begin{gathered}
\mathcal D_\tau(\varepsilon x)
=\tau_*(x)\pmod{H_B},\\
x\in K_0(A).
\end{gathered}
\tag{3.5}
\]

In the unital case one can simply lift a projection \(p\) by a selfadjoint \(b\) and use \(\exp(2\pi it b)\); its integral is \(\tau_n(p)\). Differences and scalar normalization give (3.5) in full generality.

**Theorem 3.2 (extension determinant sequence).** The sequence

\[
\begin{gathered}
0\longrightarrow H_B\longrightarrow H_A\\
\xrightarrow{\pi}\mathcal D_\tau(\ker j_*)\longrightarrow0.
\end{gathered}
\tag{3.6}
\]

is exact, where the first map is inclusion and \(\pi\) is the restriction of the quotient map modulo \(H_B\).

*Proof.* The six-term sequence gives \(\ker j_*=\varepsilon(K_0(A))\). Equation (3.5) therefore shows that the image of \(\mathcal D_\tau\) is exactly the set of cosets of elements of \(H_A\) modulo \(H_B\): both inclusions follow by taking a K-class for each element of \(H_A\), and a boundary K-class for each element of \(\ker j_*\). Hence the image is \(H_A/H_B\), and \(\pi\) is onto it. Its kernel is exactly \(H_B\), by definition of the quotient; the first map is injective. This proves all positions of (3.6). \(\square\)

This is the sequence of [Blackadar 1998, Proposition 10.10.3, printed p. 85], with the path choices, ideal representative relations and two period groups made explicit. The group \(\ker j_*\) itself need not be isomorphic to the trace quotient; (3.6) concerns its determinant image.

## 4. A trace on a mapping torus

Let \(\alpha\) be an automorphism of \(A\), with \(\tau\circ\alpha=\tau\). Its **mapping torus** \(M_\alpha\) is the C*-algebra of continuous functions \(f:[0,1]\to A\) satisfying \(f(1)=\alpha(f(0))\), with pointwise operations and the supremum norm. The subalgebra \(SA\) consists of functions with both endpoint values zero. Write \(j:SA\to M_\alpha\) for inclusion.

For a piecewise smooth invertible representative \(u\) over \(M_\alpha\), define

\[
\begin{gathered}
\Lambda_\tau([u])=\Gamma_\tau(u)\\
=\frac1{2\pi i}\int_0^1\tau_n(u'(t)u(t)^{-1})\,dt.
\end{gathered}
\tag{4.1}
\]

Here \(u\) itself is a path of invertibles over \(A\), with a twisted endpoint relation. For a nonunital algebra, normalized unitization representatives have scalar part constantly the identity, and \(\alpha\) fixes this scalar unit.

**Theorem 4.1 (mapping-torus trace).** Equation (4.1) defines a homomorphism \(\Lambda_\tau:K_1(M_\alpha)\to\mathbb R\). It satisfies

\[
\Lambda_\tau\circ j_*\circ\beta_A=\tau_*.
\tag{4.2}
\]

*Proof.* First every continuous invertible representative can be approximated uniformly by a piecewise affine function of \(t\), retaining its two endpoints. Its endpoint values still satisfy the twist, and fine approximation preserves invertibility by a uniform inverse bound. The straight homotopy to this approximation stays invertible and preserves the twist. Thus piecewise smooth representatives suffice.

For a homotopy \(u(s,t)\) satisfying that relation, the two endpoint logarithmic derivatives in the \(s\)-direction satisfy

\[
Y(s,1)=\alpha_n(Y(s,0)).
\tag{4.3}
\]

Trace invariance makes their traces equal, so the variation formula (1.3) gives \(\partial_s\Gamma_\tau=0\). For a merely continuous homotopy between piecewise smooth endpoints, subdivide in \(s\), approximate its intermediate vertices by piecewise smooth functions of \(t\) with the twisted endpoint relation, and interpolate linearly between these vertices. Retain the original two homotopy endpoints. A sufficiently fine subdivision and small approximations preserve uniform invertibility. The twist is linear and is preserved by interpolation. The resulting piecewise differentiable family admits (1.3), proving invariance under the original norm-homotopy relation.

Pointwise products and block sums add (4.1), and identity stabilization contributes zero. These are the relations defining stable \(K_1\), so the integral gives a homomorphism. Polar decomposition supplies the homotopy \(u_s=u(u^*u)^{-s/2}\) to a unitary representative. Functional calculus commutes with \(\alpha\), so this homotopy stays in the mapping torus. For unitaries the integral is real, as in Theorem 2.1; hence it is real for every representative.

Finally a positive Bott loop \(\ell_{e,P}\) has both endpoints equal to the identity, so it belongs to the normalized suspension unitization and maps to the mapping torus. Theorem 1.2 evaluates its integral as \(\tau_*([e]-[P])\). This proves (4.2) for every class. \(\square\)

Equation (4.2) is an extension *along a map*. It does not assert that \(K_0(A)\) injects into \(K_1(M_\alpha)\). Some Bott loops become nullhomotopic when endpoints may move subject to the twist; Exercise 14.5 gives an explicit example. The trace pairing vanishes on every class killed by this map, as (4.2) requires. The complete mapping-torus K-theory computation will be developed separately.

## 5. An invariant derivation gives an odd pairing

For a norm-continuous action of \(\mathbb R\) with generator \(\delta\) and invariant bounded trace, the smooth domain gives

\[
w_\tau([u])=\frac1{2\pi i}\tau_n(u^{-1}\delta u).
\tag{5.1}
\]

We reuse [Connections and curvature from symmetries of an algebra, §5, Theorem 5.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/prerequisites/NCG-CYCLIC/connections-and-curvature-for-c-star-dynamical-systems.html#5-gauge-changes-and-the-one-dimensional-pairing): the expression is additive on products and block sums and invariant on norm-homotopy classes of smooth invertibles, and every ambient K-class has such a representative. Thus it defines a homomorphism on \(K_1(A)\). Trace invariance supplies \(\tau\delta=0\) on the smooth domain.

The bounded trace condition also gives a useful general formulation. Suppose \(D\subset A\) is a norm-dense algebra and \(\delta:D\to A\) a derivation with \(\tau(\delta a)=0\) for every \(a\in D\). Define a dual-valued derivation by

\[
d(a)(b)=\tau(b\delta a),\qquad b\in A.
\tag{5.2}
\]

It is a bounded functional in \(b\), with norm at most \(\|\tau\|\|\delta a\|\). For the dual bimodule actions \((a\ell b)(x)=\ell(bxa)\), the derivation rule for \(\delta\) and cyclicity of \(\tau\) give the rule for \(d\). Moreover

\[
\begin{gathered}
0=\tau(\delta(ab))\\
=\tau(b\delta a)+\tau(a\delta b),\\
d(a)(b)=-d(b)(a),\\
a,b\in D.
\end{gathered}
\tag{5.3}
\]

Now apply the exact result [Cyclic forms that survive norm completion, §5, Theorem 5.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-OPK/preparation.html#dependency-485c5538dfda). An antisymmetric dense dual-valued derivation is closable; its norm-closed domain has matrix holomorphic calculus, and its degree-one pairing defines a unique homomorphism on ambient \(K_1\). Evaluating that pairing on a matrix with entries in the original domain gives

\[
\begin{gathered}
\nu_\tau([u])=d_n(u)(u^{-1})\\
=\tau_n(u^{-1}\delta_nu).
\end{gathered}
\tag{5.4}
\]

Its matrix amplification sums over paired indices, which is precisely the displayed unnormalized trace. For nonunital \(A\), use scalar-identity invertibles, extend the dual functionals by zero on the new unit and set its derivation to zero there, as in that theorem. Consequently \(\nu_\tau\), and hence \(\nu_\tau/(2\pi i)\), are ambient K-homomorphisms under these hypotheses. This argument imports the proved closed dual-domain result; it does not assume that an arbitrary chosen dense algebra already computes ambient K-theory.

To see the homotopy mechanism in a differentiable inverse-closed domain, cyclicity and the inverse derivative give

\[
\begin{gathered}
\frac{d}{ds}\tau_n(u_s^{-1}\delta u_s)\\
=\tau_n\bigl(\delta(u_s^{-1}\dot u_s)\bigr)=0.
\end{gathered}
\tag{5.5}
\]

The cited theorem justifies transferring this calculation to norm components. For smooth functions on \(\mathbb R/\mathbb Z\), take \(\delta=d/dx\) and \(\tau(f)=\int_0^1f\,dx\). Then \(w_\tau[u]=(2\pi i)^{-1}\int_0^1u^{-1}u'\,dx\) is winding number; for \(u(x)=\exp(2\pi ikx)\), it is \(k\). The determinant integrates along a chosen path to an element and retains its value modulo periods; this derivation pairing is constant on its entire stable K-class.

### 5.1. The cyclic character and its normalization

The preceding topological transfer has a concrete cyclic character. The following calculation also fixes its scale relative to Connes, III, §3, Proposition 3, printed pp. 230–231. We prove the degree-one specialization; the general higher-degree theorem is not needed here.

**Theorem 5.1 (a one-dimensional cycle).** Under the hypotheses below, \(\psi(a_0,a_1)=\tau(a_0\delta a_1)\) is the character of a closed one-dimensional differential cycle and a normalized cyclic one-cocycle. Its matrix evaluation on shifted invertibles gives the logarithmic derivative. With the branch-consistent scale \(\varphi=\psi/\kappa\), \(\kappa^2=2\pi i\), Connes's degree-one convention evaluates to exactly (5.1). This construction factors through algebraic \(K_1(D)\). Its transfer to ambient topological K-theory uses the preceding smooth-action or closed dual-domain result.

Let \(A\) be a unital complex Banach algebra with a bounded trace \(\tau\). Let \(D\subset A\) be a unital subalgebra containing the same unit, and let \(\delta:D\to A\) be a derivation satisfying \(\tau(\delta a)=0\) for every \(a\in D\). This argument does not require \(\delta(D)\subset D\), boundedness of \(\delta\), or positivity of \(\tau\).

*Proof.* Define the graded algebra by

\[
\begin{gathered}
\Omega^0=D,\qquad \Omega^1=A,
\\ \Omega^j=0\quad(j\geq2).
\end{gathered}
\tag{5.6}
\]

Multiplication in degree zero is that of \(D\). Mixed products are the inherited left and right actions on \(A\), and products of two degree-one elements are zero. Associativity follows from the bimodule rules. Put \(d(a)=\delta a\), \(d(\omega)=0\) for \(\omega\in\Omega^1\), and let the integral on \(\Omega^1\) be \(\tau\). The derivation identity in degree zero is the hypothesis on \(\delta\). For every other combination of degrees the differential rule holds because all products of total degree two are zero. Thus \(d\) is a graded derivation of degree one and \(d^2=0\). Trace cyclicity gives

\[
\int a\omega=\int\omega a,\qquad
\int da=0.
\]

These are precisely the graded-trace and closedness requirements in dimension one. With the identity map \(D\to\Omega^0\), its character is

\[
\psi(a_0,a_1)=\tau(a_0\delta a_1).
\tag{5.7}
\]

Here is also the direct cocycle check. Trace invariance under \(\delta\) gives

\[
\psi(a_0,a_1)+\psi(a_1,a_0)
=\tau(\delta(a_0a_1))=0.
\]

The Hochschild coboundary is

\[
\begin{gathered}
(b\psi)(a_0,a_1,a_2)=\tau(a_0a_1\delta a_2)
\\ -\tau(a_0\delta(a_1a_2))
+\tau(a_2a_0\delta a_1)
\\ =-\tau(a_0\delta a_1a_2)
+\tau(a_2a_0\delta a_1)=0.
\end{gathered}
\]

Thus \(\psi\) is a cyclic one-cocycle. Since \(\delta1=0\) and \(\tau\delta=0\), it vanishes when either argument is 1. Its matrix amplification is the unnormalized one:

\[
\begin{gathered}
\psi_n(X,Y)=\sum_{i,j}\psi(X_{ij},Y_{ji})
\\ =\tau_n(X\delta_nY).
\end{gathered}
\tag{5.8}
\]

For \(U\in GL_n(D)\), the shifted arguments appearing in Connes's formula satisfy

\[
\begin{gathered}
\psi_n(U^{-1}-I,U-I)
\\ =\tau_n((U^{-1}-I)\delta_nU)
\\ =\tau_n(U^{-1}\delta_nU).
\end{gathered}
\tag{5.9}
\]

The second equality uses \(\tau_n(\delta_nU)=0\), rather than dropping the scalar terms without justification.

For comparison of conventions, Connes's displayed odd pairing in degree \(n\) uses the coefficient

\[
c_n=\frac{2^{-n}}{\sqrt{2i}\,\Gamma(n/2+1)}.
\tag{5.10}
\]

Choose one square root of \(2i\) and put \(\kappa=\sqrt{\pi}\sqrt{2i}\), so \(\kappa^2=2\pi i\). Since \(\Gamma(3/2)=\sqrt{\pi}/2\), \(c_1=\kappa^{-1}\). Consequently the raw cocycle (5.7) gives

\[
\begin{gathered}
\langle[U],[\psi]\rangle_{\mathrm{Connes}}
\\ =\frac{\tau_n(U^{-1}\delta_nU)}{\kappa}
\\ =\kappa\,w_\tau([U]),
\end{gathered}
\tag{5.11}
\]

where \(w_\tau=(2\pi i)^{-1}\tau_n(U^{-1}\delta_nU)\) is the course's normalization. Equivalently, the scaled cocycle \(\varphi=\psi/\kappa\), used with Connes's displayed convention, gives exactly

\[
\begin{gathered}
\langle[U],[\varphi]\rangle_{\mathrm{Connes}}
\\ =\frac{\tau_n(U^{-1}\delta_nU)}{2\pi i}
\\ =w_\tau([U]).
\end{gathered}
\tag{5.12}
\]

This keeps the branch choice consistent: the same \(\kappa\) occurs in the coefficient and in the cocycle scale. On the circle, \(\delta=d/dx\) and \(\tau=\int_0^1\), (5.12) evaluates \(e^{2\pi ikx}\) to \(k\).

In this degree the algebraic pairing can also be checked without importing the general odd theorem. If \(\nu(U)=\tau_n(U^{-1}\delta_nU)\), the derivation rule and trace cyclicity give

\[
\begin{aligned}
\nu(UV)&=\tau_n(V^{-1}U^{-1}\delta_nU\,V)
\\ &\quad+\tau_n(V^{-1}\delta_nV)
\\ &=\nu(U)+\nu(V).
\end{aligned}
\tag{5.13}
\]

Identity padding contributes zero. Hence it vanishes on algebraic multiplicative commutators and factors through algebraic \(K_1(D)\), the abelianization of the stable invertible group. No topological quotient is being taken in this assertion. If a cyclic one-cocycle is a coboundary \(b\lambda\), its value on the shifted arguments in (5.9) is zero: those two matrices commute, so \(\lambda_n(XY)-\lambda_n(YX)=0\). Thus the degree-one formula respects the cohomology class as well.

For a nonunital differential algebra, adjoin a unit with derivative zero, use \(A\) as the degree-one bimodule, and use scalar-identity invertibles. Mixed scalar terms in the character vanish because \(\tau\delta=0\), so the same calculation applies.

This algebraic calculation does not by itself define a pairing on ambient topological \(K_1(A)\). For that step, the course uses its proved smooth-action or closed dual-domain transfer. Where a complete graph domain is used, \(|\psi(a,b)|\leq\|\tau\|\|a\|\|\delta b\|\) gives continuity in graph norm; density and matrix calculus are the additional hypotheses that relate this topology to ambient K-theory. The existing formula (5.1) and its transfer proofs therefore remain unchanged. \(\square\)

## 6. Exercises with complete solutions

**Exercise 14.1.** Compute the determinant of a scalar multiple of the unit.

*Solution.* Let \(A\) be unital and \(c\ne0\). Choose a logarithm \(L\) of \(c\) and use \(\xi(t)=\exp(tL)1\). Then

\[
\Delta_\tau(c1)=\frac{L\tau(1)}{2\pi i}\pmod{H_\tau}.
\tag{6.1}
\]

Changing the logarithm by \(2\pi ik\) changes the expression by \(k\tau(1)=\tau_*(k[1])\), a period. For \(c=\exp(2\pi ir)\) on the unit circle the value is \(r\tau(1)\) modulo periods; for \(c>0\), using the real logarithm gives the possibly nonzero imaginary value \(\log(c)\tau(1)/(2\pi i)\). In the normalized scalar algebra the group of periods is \(\mathbb Z\). A scalar matrix of size \(N\) has \(N\tau(1)\) in place of \(\tau(1)\), because matrix traces are unnormalized.

**Exercise 14.2.** Prove path independence modulo \(\tau_*(K_0(A))\).

*Solution.* For paths \(\xi,\eta\) from the identity to the same endpoint, concatenate \(\xi\) with the reversed \(\eta\). Its integral is \(\Gamma_\tau(\xi)-\Gamma_\tau(\eta)\). It is a based loop, so Bott periodicity gives a normalized projection difference \([e]-[P]\) whose positive loop is stably homotopic to it. The variation formula gives equality of the loop integrals; the exponential product formula evaluates the latter as \(\tau_n(e-P)\), exactly its K-pairing. Therefore the difference lies in \(H_\tau\). The converse period assertion is also explicit: every such K-pairing is attained by \(\ell_{e,P}\). Thus the quotient in (2.1) is exactly the ambiguity of the integral, including nonunital scalar-identity loops.

**Exercise 14.3.** Prove the extension determinant sequence, including its well-defined maps.

*Solution.* Set \(H_B=\tau_*q_*K_0(B)\subset H_A=\tau_*K_0(A)\). If \([u]\in\ker j_*\), choose a stabilized \(B\)-path to its normalized ideal unitary. Its quotient is an \(A\)-loop, giving an integral in \(H_A\). Two choices differ by a \(B\)-loop, a period in \(H_B\); changing representatives by an ideal homotopy adds zero because the pulled-back trace vanishes on the ideal. This defines \(\mathcal D_\tau\) as a homomorphism to \(H_A/H_B\). For a positive exponential boundary class, use (3.4): its integral is the trace of the quotient projection difference. Hence \(\mathcal D_\tau\varepsilon x=\tau_*x\) modulo \(H_B\). Exactness of the K-sequence gives \(\ker j_*=\varepsilon K_0(A)\), so all and only cosets in \(H_A/H_B\) occur. Inclusion of \(H_B\) is injective, and the quotient map on \(H_A\) has kernel \(H_B\) and is onto that determinant image. This proves each position of (3.6), with no claim that \(\mathcal D_\tau\) is injective.

**Exercise 14.4.** Compute the rotation determinant for the circle coordinate \(z\).

*Solution.* Let the geometric rotation be \(r_\theta(z)=\exp(2\pi i\theta)z\), and use the automorphism \(\alpha(f)=f\circ r_\theta^{-1}\). Lebesgue trace is invariant. Thus \(\alpha(z^{-1})=\exp(2\pi i\theta)z^{-1}\), and

\[
\begin{gathered}
z\alpha(z^{-1})=\exp(2\pi i\theta)1,\\
\Delta_\tau(z\alpha(z^{-1}))=\theta\pmod{\mathbb Z}.
\end{gathered}
\tag{6.2}
\]

The product lies in the identity component even though \(z\) itself has nonzero winding. Its value follows from the scalar path in Exercise 14.1 and the circle's period group \(\mathbb Z\). It measures a relative rotation angle modulo integer turns; an integer angle has zero coset. Using \(\alpha(f)=f\circ r_\theta\) instead reverses the displayed sign. This fixes the convention before using the determinant in a later trace-range calculation; no crossed-product trace range is inferred here.

**Exercise 14.5.** Show explicitly why the map \(j_*\beta_A\) in (4.2) need not be injective.

*Solution.* Take \(A=\mathbb C\oplus\mathbb C\), \(\alpha(a,b)=(b,a)\), and minimal projections \(p=(1,0)\), \(q=(0,1)\). Their difference is nonzero in \(K_0(A)=\mathbb Z^2\). Its positive suspension representative is

\[
u(t)=(\exp(2\pi it),\exp(-2\pi it)).
\tag{6.3}
\]

In the mapping torus, put \(h(t)=(t,1-t)\). Its endpoints satisfy \(h(1)=\alpha(h(0))\), so \(h\in M_\alpha\) is selfadjoint. Since \(\exp(2\pi i(1-t))=\exp(-2\pi it)\), we have \(u=\exp(2\pi ih)\). The homotopy \(\exp(2\pi is h)\), \(0\leq s\leq1\), stays in the mapping torus and joins the identity to \(u\). Thus \(j_*\beta_A([p]-[q])=0\). The invariant tracial state is \(\tau(a,b)=(a+b)/2\); it gives \(\tau_*([p]-[q])=0\), agreeing with (4.2). Directly, the logarithmic derivatives of the two components in (6.3) are \(2\pi i\) and \(-2\pi i\), whose weighted sum is zero. Both the nullhomotopy and the trace compatibility are explicit.

## What this lesson imports and does not prove

Stable K-theory, polar deformation, positive Bott loops and the six-term sequence with the positive exponential boundary are imported from Lessons 6, 10 and 11. Bounded/nonunital trace pairings and their naturality are from Lesson 13. The determinant, its complete period group, the extension determinant sequence, and the mapping-torus homomorphism are proved here. The norm-flow derivation pairing is reused from Connections and curvature, Theorem 5.2; the general transfer through a closed dual-valued derivation is the cited Theorem 5.3 of Cyclic forms that survive norm completion. We do not prove general higher cyclic pairings, the full mapping-torus K-sequence, or a crossed-product trace-range theorem here. The map in (4.2) is not asserted to be injective.

## References

- **[Blackadar 1998]** B. Blackadar, *K-Theory for Operator Algebras*, second edition, MSRI Publications 5, Cambridge University Press, 1998, §10.10.1–§10.10.3, printed pp. 84–85. Proposition 10.10.3 is the extension sequence. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- **de la Harpe and Skandalis 1984**, P. de la Harpe and G. Skandalis, [“Déterminant associé à une trace sur une algèbre de Banach”](https://www.numdam.org/item/AIF_1984__34_1_241_0/), *Annales de l'Institut Fourier* 34(1), 1984, pp. 241–260. The construction here is proved using the positive Bott convention specified above.
- **[Connes 1994]** A. Connes, *Noncommutative Geometry*, Academic Press, 1994, Chapter III, §3, printed pp. 229–238, especially Proposition 3 for the odd cyclic pairing. The general higher-degree normalization is not imported into (5.1). [Author's electronic edition](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).
- **Connections and curvature from symmetries of an algebra**, §5, Theorem 5.2 and Example 5.3; **Cyclic forms that survive norm completion**, §5, Lemma 5.1 and Theorem 5.3. The exact links accompany their use in §5.

[de la Harpe–Skandalis1984, universal trace] P. de la Harpe and G. Skandalis, *Déterminant associé à une trace sur une algèbre de Banach*, Annales de l’Institut Fourier34(1)(1984),241–260, §§1–3, especially Lemma3, Propositions4 and6/6bis, Lemmas9–11 and Proposition12; §4 for the nonclosed-kernel consequence. [Freely readable original paper](https://www.unige.ch/~laharpe/articles/28HSkandDet1984.pdf). Lemma2.2–Example2.9 and Theorem2.9a supply complete independently written vector-valued, universal, closure, separability, positive-decomposition, covering, stable-commutator and CAR arguments. Theorem2.9a proves the complete arbitrary-AF irrational-scalar criterion, using the corrected finite smoothing construction, exact period extraction and unital finite-stage realization. The source’s continuum-hypothesis/nonseparable classification and uncountable realization results are not imported.

[Exel1987, all components] R. Exel, *Rotation numbers for automorphisms of C*-algebras*, Pacific Journal of Mathematics127(1)(1987),31–89, II.3–II.10. [Freely readable original paper](https://msp.org/pjm/1987/127-1/pjm-v127-n1-p03-s.pdf). Lemmas2.10a–2.10b and Theorem2.10 independently prove character extension, the exact scalar-extension group, circle determinant existence, classification and continuity. All commutator quotients used in that proof are algebraic; no unproved closed-subgroup containment or source expression is imported.

[Connes1994, degree-one normalization] A. Connes, *Noncommutative Geometry*, Chapter III, §1, Definition1, p.187, and complete §3, pp.229–238, especially Proposition3, pp.230–231. [Freely readable author edition](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Theorem5.1 gives the complete independent cycle, cocycle, shifted-unit, algebraic additivity and branch-consistent normalization calculation. It does not import the general higher-degree pairing theorem or a new ambient K-theory transfer theorem.
[Pimsner–Voiculescu1980, AF embedding] M. Pimsner and D. Voiculescu, *Imbedding the irrational rotation C*-algebra into an AF-algebra*, Journal of Operator Theory4(2)(1980),201–210. [Freely readable original paper](https://www.theta.ro/jot/archive/1980-004-002/1980-004-002-003.pdf). Theorem2.9a includes the full corrected finite smoothing construction, actual conjugacy maps, cyclic endpoints, uniform support and norm bounds, and unitary norm limits. Its ordered-group, unital realization and exact countable-target arguments are proved here. The two coefficient-phase corrections on pp203–204 are stated and verified explicitly; the external classification results cited by the source are not used as proof substitutes.

