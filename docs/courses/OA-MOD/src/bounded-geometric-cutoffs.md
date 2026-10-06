# Polynomial cutoffs for the range of an operator

**Original mathematical exposition, reconstructed from the written programme foundations. New prose: CC0-1.0.**

A positive operator may have a dense range that is not closed. The polynomials below recover the projection onto the closure of that range. The proof works on every complex Hilbert space, including nonseparable spaces, and requires no inverse.

The earlier programme proof The bounded prerequisite boundary constructs orthogonal projections, complex adjoints and their norm identities. Its interval calculus is constructed explicitly in GP0, equations GP0.1–GP0.5, using the projection and Riesz proofs in the first section of the real Hilbert-space foundation. For a positive contraction, GP0 proves that polynomial evaluation preserves order on \([0,1]\) and has norm at most the scalar supremum on that interval. These are the only earlier operator-theoretic inputs; the range identity, sharp scalar bound and strong limit are proved below.

Jones's freely available notes describe the general range-projection approximation in §3.4, EP6, page 20. The explicit sequence and its quantitative estimate here are established by the following local argument; the reference supplies no missing proof.

## Geometric cutoffs and the range projection

Let \(B\) be a positive contraction on a complex Hilbert space \(H\), and let \(s(B)=P_{\overline{\operatorname{ran}B}}\). For integers \(n\geq1\), define

\[
p_n(t)=1-(1-t)^n,\qquad P_n=p_n(B)=I-(I-B)^n.
\]

The polynomial \(p_n\) has real coefficients and no constant term. We claim

\[
0\leq P_n\leq P_{n+1}\leq I,
\qquad
P_n\longrightarrow s(B)\quad\text{strongly}.
\]

More precisely, the estimate on vectors already in the range is

\[
\bigl\|(I-B)^nB\bigr\|
\leq\max_{0\leq t\leq1}t(1-t)^n
=\frac{n^n}{(n+1)^{n+1}}
\leq\frac1{n+1}.
\tag{BC.1}
\]

**Proof.** The assertions are immediate when \(H=\{0\}\), so suppose \(H\ne\{0\}\). For \(0\leq t\leq1\), both \(0\leq p_n(t)\leq1\) and
\(p_{n+1}(t)-p_n(t)=t(1-t)^n\geq0\).
Order preservation in the continuous functional calculus yields the operator inequalities. In particular \(Q_n=(I-B)^n\) is a positive contraction.

Here is a finite algebraic proof of the exact scalar maximum. For \(u\geq0\), multiplication of the finite sum gives

\[
1-(n+1)u^n+nu^{n+1}
=(1-u)^2\sum_{k=0}^{n-1}(k+1)u^k\geq0.
\]

Indeed, expansion leaves constant coefficient \(1\), coefficient \(-(n+1)\) at degree \(n\), and coefficient \(n\) at degree \(n+1\); every intermediate coefficient cancels. Set

\[
u=\frac{n+1}{n}(1-t),\qquad
M_n=\frac{n^n}{(n+1)^{n+1}}.
\]

For \(0\leq t\leq1\), this gives

\[
t(1-t)^n
=M_n\bigl((n+1)u^n-nu^{n+1}\bigr)\leq M_n.
\]

Equality holds at \(u=1\), or \(t=1/(n+1)\). Also
\(M_n=(n/(n+1))^n/(n+1)\leq1/(n+1)\).
The polynomial norm bound on \([0,1]\), proved in GP0, now gives (BC.1). No differentiation or additional extremum theorem is being imported.

Each \(Q_n\) acts as the identity on \(\ker B\). If \(\zeta=B\xi\) is in the range, (BC.1) gives

\[
\|Q_n\zeta\|\leq\frac{\|\xi\|}{n+1}\longrightarrow0.
\]

The uniform bound \(\|Q_n\|\leq1\) extends this convergence to the closure of the range. Explicitly, for \(\zeta\in\overline{\operatorname{ran}B}\), choose \(\xi\) with \(\|\zeta-B\xi\|<\varepsilon\); then

\[
\|Q_n\zeta\|\leq\varepsilon+\frac{\|\xi\|}{n+1}.
\]

First send \(n\) to infinity, then \(\varepsilon\) to zero.

For completeness, the range-kernel identity used here follows directly from the adjoint pairing. A vector \(\eta\) is orthogonal to \(\operatorname{ran}T\) exactly when
\(\langle T\xi,\eta\rangle=\langle\xi,T^*\eta\rangle=0\) for all \(\xi\), which is equivalent to \(T^*\eta=0\) (test \(\xi=T^*\eta\)). Orthogonality is unchanged by taking a closure. The orthogonal projection constructed in BK-01 therefore gives

\[
\overline{\operatorname{ran}T}=(\ker T^*)^\perp.
\]

In particular, since \(B=B^*\),

\[
H=\ker B\ \oplus\ \overline{\operatorname{ran}B}.
\]

Consequently \(Q_n\) converges strongly to \(I-s(B)\), and \(P_n=I-Q_n\) converges strongly to \(s(B)\). This also covers \(B=0\).

For any bounded \(a\) with \(\|a\|\leq1\), apply this result to \(aa^*\). The adjoint norm identity gives \(\|a^*\|=\|a\|\leq1\); hence the following quadratic form is nonnegative and at most \(\|\xi\|^2\), so \(0\leq aa^*\leq I\). Moreover,

\[
\langle aa^*\xi,\xi\rangle=\|a^*\xi\|^2
\]

gives \(\ker(aa^*)=\ker a^*\), hence

\[
\overline{\operatorname{ran}(aa^*)}
=(\ker a^*)^\perp
=\overline{\operatorname{ran}a}.
\]

Therefore

\[
p_n(aa^*)\longrightarrow P_{\overline{\operatorname{ran}a}}
\quad\text{strongly}.
\tag{BC.2}
\]

\(\square\)

**Example: why the topology matters.** On \(H=\mathbb C\oplus\ell^2(\mathbb N)\), set

\[
B(z,\xi_1,\xi_2,\ldots)
=(0,\xi_1,\xi_2/2,\ldots,\xi_j/j,\ldots).
\]

Its kernel is the first summand; finitely supported vectors lie in its range, so its range is dense in the second summand. Thus

\[
s(B)=0\oplus I,\qquad
(s(B)-P_n)(z,\xi)
=\left(0,\bigl((1-1/j)^n\xi_j\bigr)_{j\geq1}\right).
\]

For a fixed vector, split the square-summable sequence into a finite head and a small tail. The head tends to zero coordinatewise, while the tail stays uniformly small because \(0\leq(1-1/j)^n\leq1\). This gives strong convergence directly. Yet for every fixed \(n\),

\[
\|s(B)-P_n\|=\sup_{j\geq1}(1-1/j)^n=1.
\]

So no operator-norm convergence follows from the theorem. The bounded approximation also says nothing by itself about graph cores for unbounded modular operators.

## Freely accessible source

- Vaughan F. R. Jones, [*Von Neumann Algebras*, version dated 29 November 2010, §3.4, EP6, printed/PDF page 20](https://math.berkeley.edu/~vfr/MATH20909/VonNeumann2009.pdf#page=20). This is a comparison for approximation of range projections; the sequence, bound and example in this lesson have complete proofs above.
