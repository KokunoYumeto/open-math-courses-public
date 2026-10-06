# The sharp lower bound for a finite system

The boundary energy argument uses a positive \(2\times2\) matrix symbol. This companion proves its full sharp lower bound by applying the already proved scalar moving probe to each component. The result holds for every fixed finite matrix size \(N\). Constants may depend on \(N\); no dimension-independent or infinite-dimensional assertion is made.

This connecting exposition is dedicated to CC0 1.0. The linked scalar probe and its cancellation proof are separately licensed under GFDL 1.2 only; their original notices remain with those components.

## M1. Matrix Sobolev bounds and ordered remainders

Use \(D=-i\partial\), left quantization and the inner product linear in its first argument. For \(u=(u_1,\ldots,u_N)\), define
\[
\|u\|_{s,N}^2=\sum_{j=1}^N\|u_j\|_s^2,\qquad
p_{r,L}^{(N)}(a)=\max_{j,k}p_{r,L}(a_{jk}).
\tag{MG1}
\]
The scalar seminorm and norm are those in [the complete scalar companion, G1](../20261005-cauchy-foundations/sharp-lower-bound.md#g1-global-sobolev-bounds-with-the-original-norms). That proof gives completeness, Schwartz density and the scalar global operator bound. Finite sums give completeness and simultaneous density in these vector norms. Applying the scalar bound entry by entry and Cauchy–Schwarz to the finite row sum gives
\[
\|\operatorname{Op}(a)u\|_{s-r,N}
\le NC_{r,s,n}p_{r,J}^{(N)}(a)\|u\|_{s,N}.
\tag{MG2}
\]
Indeed each row is bounded by \(C p\sum_k\|u_k\|_s\le C p\sqrt N\|u\|_{s,N}\), and summing the \(N\) squared row bounds gives MG2. The Fourier dual pairing therefore gives
\[
|(\operatorname{Op}(d)u,u)|
\le NC_{m,n}p_{2m,J}^{(N)}(d)\|u\|_{m,N}^2
\quad(d\in S^{2m}).
\tag{MG3}
\]

The [ordinary composition and adjoint proof O3](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md) also applies entry by entry: the \((j,k)\) entry of a composition is the finite sum over \(\ell\) of the scalar composition of \(a_{j\ell}\) and \(b_{\ell k}\). Every differentiated term keeps this order. The \((j,k)\) entry of the adjoint is the scalar adjoint of \(a_{kj}\). Each finite remainder has its stated order with a constant multiplied by at most a finite power of \(N\). Thus a Hermitian symbol \(B\in S^r\) satisfies
\[
\operatorname{Op}(B)-\operatorname{Op}(B)^*
\in\operatorname{Op}(S^{r-1}).
\tag{MG4}
\]
No diagonalization depending on phase space is required.

## M2. A positive matrix quadratic form from scalar probes

Use the even normalized bump, scalar \(B=\operatorname{Op}(\varphi)\), scalar Schwartz symbol \(\psi\) of \(B^*B\), and scalar unitary \(U_{y,\eta,q}\) from the [included probe proof, G4](../20261005-cauchy-foundations/sharp-lower-bound.md#g4-a-positive-scalar-probe-and-its-moving-copies). There \(\int\psi=1\), the exact conjugation identity P26 holds, and \(q(\eta)=\langle\eta\rangle^{1/2}\). Apply \(B,U\) separately to each of the \(N\) entries. A constant matrix commutes with both scalar kernels.

For a Hermitian pointwise nonnegative matrix symbol \(A\in S^r\), define \(A_+=\mathcal I_\psi A\) entry by entry by P29. The scalar convergence estimate P30 proves that each entry is smooth and every differentiated integral is locally absolutely convergent. The quadratic form identity is
\[
(\operatorname{Op}(A_+)u,u)
=\iint_{\mathbb R^{2n}}
\bigl(A(y,\eta)B U_{y,\eta,q(\eta)}^*u,\,
 B U_{y,\eta,q(\eta)}^*u\bigr)_{L^2(\mathbb R^n;\mathbb C^N)}
\,dy\,d\eta\ge0 .
\tag{MG5}
\]
Here the matrix is constant in the inner \(t\) variable of the \(L^2\) pairing. To justify the integral, apply the full P32 integration-by-parts estimate to each \(u_j\). For every \(M\) it bounds each \(L^2_t\) norm of \(BU^*u_j\) by \(C_{u,M}\langle y\rangle^{-M}\langle\eta\rangle^{-M}\). There are finitely many entries, and \(\|A(y,\eta)\|\le Np_{r,0}^{(N)}(A)\langle\eta\rangle^r\). The quadratic integrand is therefore absolutely integrable, including for positive \(r\).

For compact parameter cutoffs, expand the finite matrix pairing and use the scalar kernel identity P26, ordinary Fubini and polarization on its finitely many pairs of scalar inputs. This proves the equality with the cutoff integral. P30 on the symbol side and P32 on the form side permit dominated convergence as the cutoffs tend to one. This proves MG5. Its nonnegativity follows pointwise from \(A\ge0\), integrated first in \(t\) and then in \((y,\eta)\). It is a statement on Schwartz vectors, with no prior boundedness assertion for a positive-order operator.

## M3. The full one-order improvement and lower bound

The exact scalar cancellation proof [G5, P33–P42](../20261005-cauchy-foundations/sharp-lower-bound.md#g5-two-cancellations-and-the-full-error), with \(\rho=1,\delta=0\), applies to each entry. In particular, with every differentiated remainder and finite-seminorm bound,
\[
A-A_+\in S^{r-1}(\mathbb R^{2n};\mathbb C^{N\times N}).
\tag{MG6}
\]
For a general complex matrix symbol \(a\in S^{2m+1}\), suppose its Hermitian part \(A=(a+a^*)/2\) is nonnegative. Write \(a=A+iB\), where \(B=(a-a^*)/(2i)\) is Hermitian. MG5 and MG6, followed by MG3, give the lower bound for \(\operatorname{Op}(A)\). For \(B\), MG4 and the convention that the inner product is linear in its first argument give
\[
\operatorname{Re}(i\operatorname{Op}(B)u,u)
=\frac{i}{2}
\bigl((\operatorname{Op}(B)-\operatorname{Op}(B)^*)u,u\bigr).
\tag{MG7}
\]
The right side is real and is bounded in absolute value by MG3. Both matrix parts have seminorms controlled by those of \(a\). We conclude that for every real \(m\), with a fixed finite \(J\),
\[
\operatorname{Re}(\operatorname{Op}(a)u,u)
\ge-C_{m,n,N}p_{2m+1,J}^{(N)}(a)\|u\|_{m,N}^2,
\qquad u\in\mathcal S(\mathbb R^n;\mathbb C^N).
\tag{MG8}
\]
The constant is uniform over bounded symbol families. All estimates are global in the base variable because the earlier scalar proofs have that scope.

## M4. The two energy receivers and time dependence

For \(a\in S^2\) with nonnegative Hermitian part, choose \(m=1/2\) in MG8. For \(a\in S^0\) choose \(m=-1/2\). Thus
\[
\begin{aligned}
\operatorname{Re}(\operatorname{Op}(a)u,u)&\ge-C\|u\|_{1/2,N}^2
&& (a\in S^2),\\
\operatorname{Re}(\operatorname{Op}(a)u,u)&\ge-C\|u\|_{-1/2,N}^2
&& (a\in S^0).
\end{aligned}
\tag{MG9}
\]
These statements retain their half-derivative losses.

More generally conjugate by the scalar weight \(E_s I_N\). The ordered composition just proved gives a full symbol
\[
E_s\operatorname{Op}(a)E_{-s}
=\operatorname{Op}(a+d_s),\qquad d_s\in S^{r-1},
\tag{MG10}
\]
for \(a\in S^r\), uniformly in bounded families. The zeroth term is \(a\); every other term and the finite remainder lose an order, since a frequency derivative of a scalar weight lowers its order. Apply MG8 to \(a\), and MG3 to \(d_s\), with \(m=(r-1)/2\). With \(v=E_su\),
\[
\operatorname{Re}(E_s\operatorname{Op}(a)u,E_su)
\ge-C_{r,s,n,N}\|u\|_{s+(r-1)/2,N}^2 .
\tag{MG11}
\]
This starts on Schwartz vectors; simultaneous approximation passes to any Sobolev class where the pairing is defined. For a bounded time-dependent symbol family the same finite seminorm bounds make the constants uniform. If each entry is distributionally continuous in \((x,\xi)\), the complete scalar G7 argument gives strong continuity \(H^s\to H^{s-r}\) for each entry; the finite sum and MG2 give it for the matrix operator.

For example \(z\in\mathbb C\) and \(\varepsilon\ge0\) give
\[
A=\begin{pmatrix}1&z\\\bar z&|z|^2+\varepsilon\end{pmatrix},
\qquad (Aw,w)=|w_1+z w_2|^2+\varepsilon|w_2|^2\ge0.
\tag{MG12}
\]
The identity follows by expanding the squared modulus with the stated inner product convention. It supplies a non-diagonal positive matrix at each point when \(z,\varepsilon\) vary; only the appropriate symbol bounds are then additionally required. This pointwise example illustrates the hypothesis, while MG5–MG11 prove the operator estimates.

The mathematical antecedent of the scalar probe is Hörmander, *The Analysis of Linear Partial Differential Operators III*, approved 2007 eBook, Theorem 18.1.14. The actual earlier programme proof, including its full convergence and cancellation estimates, is the linked CE companion. This finite-matrix adapter proves every additional finite-sum step. It does not supply the scalar Fefferman–Phong estimate, whose order-two \(L^2\) error is stronger than MG9.
