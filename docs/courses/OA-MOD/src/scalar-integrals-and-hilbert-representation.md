# Scalar integrals and Hilbert representation

The density construction for finite measures rests on two facts: scalar \(L^2\) is complete, and every bounded functional on a Hilbert space is represented by a vector. We prove those facts from the measure axioms, scalar completeness and the inner-product axioms. Neither separability nor completeness of the measure is assumed.

These arguments reuse the programme's earlier real Hilbert-space proof and its *Measure and Hilbert space tools for Haar integration*, Sections 2–3, with the completeness proof specialized to \(p=2\). Their original exposition and this adaptation are CC0-1.0.

## Projection and representation on a Hilbert space

A Hilbert space is complete for the norm supplied by its inner product. Complex inner products here are linear in the first variable. Its underlying real Hilbert space has pairing \((x,y)_{\mathbb R}=\operatorname{Re}\langle x,y\rangle\). The same arguments below apply directly to real Hilbert spaces.

**The inner-product inequalities.** Positivity and definiteness are inner-product axioms. If \(y\ne0\), expansion using the linear-first convention gives
\[
0\leq\left\|x-\frac{\langle x,y\rangle}{\|y\|^2}y\right\|^2
=\|x\|^2-\frac{|\langle x,y\rangle|^2}{\|y\|^2}.
\]
Hence \(|\langle x,y\rangle|\leq\|x\|\|y\|\); the case \(y=0\) is immediate. For a real inner product the same computation uses the real scalar \((x,y)_{\mathbb R}/\|y\|^2\). Expansion and this inequality give
\[
\|x+y\|^2
=\|x\|^2+2\operatorname{Re}\langle x,y\rangle+\|y\|^2
\leq(\|x\|+\|y\|)^2,
\]
so the induced norm satisfies the triangle inequality. Expanding both squares and cancelling the mixed terms also gives the parallelogram identity
\[
\|x+y\|^2+\|x-y\|^2=2\|x\|^2+2\|y\|^2.
\]
These computations apply in arbitrary dimension and to the underlying real Hilbert space.

Let \(E\) be a closed real subspace of a Hilbert space regarded as real. Every \(x\) has a unique closest point \(P_E x\) in \(E\). Indeed, if \(d=\inf_{e\in E}\|x-e\|\) and \(e_n\) is a minimizing sequence, the parallelogram identity gives
\[
\|e_n-e_m\|^2
\leq 2\|x-e_n\|^2+2\|x-e_m\|^2-4d^2\longrightarrow0.
\]
Completeness and closedness give a minimizing limit. Varying that limit by \(t e\), for real \(t\) and \(e\in E\), shows that the residual is real-orthogonal to \(E\). This orthogonality proves uniqueness, real-linearity of \(P_E\), and \(\|P_E x\|\leq\|x\|\).

Every bounded real-linear functional \(\ell\) on a real Hilbert space has a unique vector \(v\) such that \(\ell(z)=(v,z)_{\mathbb R}\), with \(\|v\|=\|\ell\|\). To see this without an additional representation theorem, suppose \(\ell\ne0\), put \(N=\ker\ell\), and choose \(x_0\notin N\). The preceding projection construction gives \(u=x_0-P_Nx_0\ne0\), with \(u\perp_{\mathbb R}N\) and \(\ell(u)=\ell(x_0)\ne0\). Since
\[
z-\frac{\ell(z)}{\ell(u)}u\in N,
\]
one may take \(v=\ell(u)u/\|u\|^2\). The case \(\ell=0\) uses \(v=0\). The norm equality follows from Cauchy–Schwarz and testing at \(v/\|v\|\) when \(v\ne0\). Uniqueness follows by testing the difference of two representing vectors against itself.

For a closed complex subspace \(E\), the residual of its real orthogonal projection pairs to zero with both \(e\) and \(ie\), for every \(e\in E\). Both real and imaginary parts of its complex pairing with \(e\) vanish. Thus it is the complex orthogonal projection; uniqueness of the orthogonal decomposition makes it complex-linear.

Let \(L\) be a bounded complex-linear functional. Apply the real representation just proved to \(\ell(x)=\operatorname{Re}L(x)\), obtaining \(v\) with \(\operatorname{Re}L(x)=\operatorname{Re}\langle x,v\rangle\). Evaluation at \(ix\) identifies the imaginary parts too, and hence
\[
L(x)=\langle x,v\rangle\qquad(x\in H).
\tag{LH.1}
\]
The real norm of \(\ell\) equals the complex norm of \(L\): for each \(x\), multiply it by a complex scalar of modulus one so that the new value of \(L\) is nonnegative real. This proves \(\|L\|=\|v\|\). Testing the difference of two representing vectors against itself proves uniqueness. The zero functional and zero Hilbert space are included.

## Nonnegative integration and monotone convergence

Fix a measure space \((X,\Sigma,\mu)\). A measurable real function is one for which \(\{f>t\}\in\Sigma\) for every real \(t\). Countable suprema and infima are measurable: use \(\{\sup_n f_n>t\}=\bigcup_n\{f_n>t\}\), and negate for infima. Limits are measurable because \(\liminf f_n=\sup_N\inf_{n\geq N}f_n\). Complex functions are measurable when their real and imaginary parts are.

For a nonnegative simple function \(s=\sum_{j=1}^r a_j1_{E_j}\), with disjoint measurable \(E_j\) and \(a_j\geq0\), define \(\int s=\sum_j a_j\mu(E_j)\), with \(0\cdot\infty=0\). Refining two partitions proves independence of the presentation, monotonicity, and additivity for simple functions. For measurable \(f\geq0\), define
\[
\int f=\sup\{\int s:0\leq s\leq f,\ s\text{ simple}\}.
\]
There are increasing simple \(s_n\to f\): truncate \(f\) at \(n\) and round down to multiples of \(2^{-n}\). The truncation bounds and the refining dyadic grids ensure monotonicity.

Countable additivity implies continuity from below: if \(E_n\uparrow E\), write \(E\) as the disjoint union of \(E_1,E_2\setminus E_1,\ldots\). Then \(\mu(E_n)\uparrow\mu(E)\). If \(\mu(E_1)<\infty\) and \(E_n\downarrow E\), apply this to \(E_1\setminus E_n\) to obtain continuity from above.

**Monotone convergence.** If \(0\leq f_n\uparrow f\) almost everywhere, then \(\int f_n\uparrow\int f\).

*Proof.* Discard one measurable null set to obtain pointwise inequalities; changing values there changes none of the integrals. Monotonicity gives \(\lim\int f_n\leq\int f\). For simple \(s\leq f\) and \(0<t<1\), the sets \(A_n=\{f_n\geq ts\}\) increase and cover \(\{s>0\}\). Consequently continuity from below on the finitely many level sets of \(s\) gives \(\int s1_{A_n}\uparrow\int s\). Since \(f_n\geq ts1_{A_n}\), the limit of their integrals is at least \(t\int s\). Let \(t\uparrow1\) and then take the supremum over \(s\). The same argument works when \(\int s=\infty\). \(\square\)

Applying this to increasing simple approximations of \(f,g\geq0\) proves \(\int(f+g)=\int f+\int g\). Applying it to partial sums proves
\[
\int\sum_n f_n=\sum_n\int f_n\qquad(f_n\geq0).
\tag{LH.2}
\]
These identities justify defining the integral of an integrable real function as \(\int f^+-\int f^-\), and then treating complex functions by real and imaginary parts. Here integrable means \(\int|f|<\infty\). Linearity follows from nonnegative additivity by moving all negative parts to the opposite side of the desired equality. Choosing a phase so that \(e^{i\theta}\int f\) is nonnegative real gives \(|\int f|\leq\int|f|\).

For \(u\ge0\), the integral is zero exactly when \(u\) vanishes almost everywhere: \(\mu(\{u\ge1/n\})\le n\int u\) proves one implication, and simple approximation proves the other. Measurable almost-everywhere limits are understood through measurable representatives. In particular, a limit defined on the measurable set where a sequence converges and set equal to zero on its measurable null complement is still measurable. No arbitrary modification on a nonmeasurable subset of a null set is used.

## Completeness of scalar L2 on an arbitrary measure space

Let \(L^2(\mu)\) consist of measurable complex functions with finite \(\int|f|^2\), modulo almost-everywhere equality. The integral of \(f\overline g\) exists for \(f,g\in L^2\), since \(2|f g|\le |f|^2+|g|^2\). The pairing
\[
\langle f,g\rangle=\int f\overline g\,d\mu
\tag{LH.3}
\]
is independent of the representatives, linear first, conjugate-symmetric, and positive definite on the quotient, by the zero-integral criterion above. The elementary inner-product calculations in LH-01, which use no completeness assumption, give Cauchy–Schwarz and the triangle inequality. Thus \(\|f\|_2=(\int|f|^2)^{1/2}\) is a norm.

Take a Cauchy sequence \((f_n)\) in this norm. Choose a subsequence \((f_{n_j})\) with \(\|f_{n_{j+1}}-f_{n_j}\|_2\le2^{-j}\), and choose measurable representatives. The partial sums of
\[
v=\sum_{j\ge1}|f_{n_{j+1}}-f_{n_j}|
\]
have norm at most one by the triangle inequality. Monotone convergence applied to their squares gives \(\int v^2\le1\). Hence \(v\) is finite outside a measurable null set \(N\): if \(\mu(\{v=\infty\})>0\), the lower bounds by arbitrarily large constants on that set would contradict the finite integral. The subsequence converges pointwise off \(N\). Define its limit \(f\) to be zero on \(N\); countable suprema, infima and limits of the real and imaginary parts show that it is measurable for the original sigma-algebra.

Off \(N\), the tail estimate is
\[
|f-f_{n_j}|\le\sum_{k\ge j}|f_{n_{k+1}}-f_{n_k}|,
\qquad
\|f-f_{n_j}\|_2\le\sum_{k\ge j}2^{-k}.
\tag{LH.4}
\]
The norm bound follows first for finite tail sums from the triangle inequality, and then for the full nonnegative tail from monotone convergence of its square. In particular \(f\in L^2\), and the subsequence converges to it in norm. The Cauchy property brings the entire sequence to the same limit. This proves completeness for every measure on every measurable space, with no finiteness, sigma-finiteness or completed-measure hypothesis. Thus (LH.3) makes \(L^2\) a Hilbert space, and LH-01 applies to its bounded linear functionals.

### Application to the finite density construction

For finite positive measures \(\nu\ll\mu\), put \(\tau=\mu+\nu\). The functional \(f\mapsto\int f\,d\nu\) on \(L^2(\tau)\) has bound \(\nu(X)^{1/2}\|f\|_{L^2(\tau)}\), by Cauchy–Schwarz in \(L^2(\nu)\) and \(\nu\le\tau\). LH-03 supplies completeness and LH-01 supplies the representing vector. DC05 then tests indicators and constructs the density; its use of nonnegative approximation is covered by LH-02. This route does not use any Radon–Nikodym theorem to prove Hilbert representation or scalar L2 completeness.
