# Recovering a weight from spatial energy

**Self-checked by the writing AI.**

A positive self-adjoint operator assigns an energy to every vector, with infinity outside its square-root domain. To recover a weight, that energy must measure the positive coefficient operator rather than a chosen decomposition of it. This includes decompositions with infinite energy. We first prove an extension theorem for an ideal, then apply it to spatial coefficients. The covariance criterion is connected to the independent weight-cocycle reconstruction theorem.

The mathematical antecedents are Takesaki, *Theory of Operator Algebras II*, IX.3, Theorem 3.11 and Lemma 3.12, together with VIII.3, Theorem 3.8. The finite-energy condition printed in IX.3.11(iii) needs a correction: by itself it does not imply weight reconstruction. Sections SX-08–10 give an explicit counterexample, including a contradiction to extension by any weight. The valid coefficient criterion below compares all extended energies. The covariance characterization retains arbitrary Hilbert spaces and possibly nonfaithful numerators.

## The data that must determine the weight

Let \(M\subseteq B(H)\) be a concrete unital von Neumann algebra, put \(N=M'\), and let \(\psi\) be normal, semifinite and faithful on \(N\). No separability or sigma-finiteness condition is imposed. Inner products are linear in the first variable. Use the bounded-vector construction of Conventions and the actual prerequisites:

\[
R_\psi(\xi)\Lambda_\psi(y)=y\xi,
\qquad
\theta(\xi,\eta)=R_\psi(\xi)R_\psi(\eta)^*,
\qquad \xi,\eta\in D_\psi.
\tag{SX.1}
\]

The coefficient ideal is

\[
\mathcal J=\operatorname{span}\{\theta(\xi,\eta):\xi,\eta\in D_\psi\}.
\tag{SX.2}
\]

By SD-04 and SC-04 it is an algebraic two-sided *-ideal, its positive cone consists of finite sums of diagonal coefficients, and it has positive contractions \(u_a\uparrow1\) strongly. In particular,

\[
x^{1/2}u_a x^{1/2}\in\mathcal J_+,
\qquad x^{1/2}u_a x^{1/2}\uparrow x
\quad(x\in M_+).
\tag{SX.3}
\]

For a positive self-adjoint operator \(A\) on \(H\), write

\[
Q_A(\xi)=
\begin{cases}
\|A^{1/2}\xi\|^2,&\xi\in D(A^{1/2}),\\
+\infty,&\xi\notin D(A^{1/2}).
\end{cases}
\tag{SX.4}
\]

This extended function is lower semicontinuous for Hilbert-norm convergence, including arbitrary nets: spectral truncations express it as the supremum of the continuous functions \(\|A^{1/2}1_{[0,n]}(A)\xi\|^2\). Its finite domain with the form norm is complete.

Our coefficient consistency condition is the following statement about **all** finite families in \(D_\psi\):

\[
\sum_{j=1}^r\theta(\xi_j,\xi_j)
=\sum_{k=1}^s\theta(\eta_k,\eta_k)
\quad\Longrightarrow\quad
\sum_{j=1}^rQ_A(\xi_j)=\sum_{k=1}^sQ_A(\eta_k)
\text{ in }[0,\infty].
\tag{SX.5}
\]

The empty family is allowed. Thus the zero coefficient must have energy zero. We separately require

\[
F=D_\psi\cap D(A^{1/2})
\quad\text{to be a core for }A^{1/2}.
\tag{SX.6}
\]

This is approximation in the graph norm, not only density in \(H\).

The direct analytic inputs are SC-04–10, the finite-domain projection theorem WS-02, bounded Douglas factorization from BK/SD, and the closed-form and spectral results FC, QF and SK. The covariance direction additionally uses SI's modular identification, WH-13's existence of NSF reference weights, and the separately proved inverse weight-cocycle theorem CX. These are exact course dependencies; their own scalar foundations are not proved here.

## A positive supremum becomes normal before it becomes additive

Let \(J\) be an algebraic two-sided *-ideal in a von Neumann algebra \(B\). Assume it has positive contractions \(u_a\uparrow1\). A weight on \(J_+=J\cap B_+\) means an additive, nonnegative homogeneous function \(w:J_+\to[0,\infty]\), with \(w(0)=0\) and \(0\cdot\infty=0\). Suppose that

\[
w(z)\le\liminf_i w(b_i z b_i^*)
\tag{SX.7}
\]

for every \(z\in J_+\) and every net \(b_i\in B\) converging strongly to \(1\).

**Extension theorem.** There is exactly one normal weight on \(B\) extending \(w\), namely

\[
\Phi(x)=\sup\{w(z):z\in J_+,\ z\le x\},
\qquad x\in B_+.
\tag{SX.8}
\]

No semifiniteness assumption on \(w\) is needed for this assertion.

**Agreement and homogeneity.** If \(x\in J_+\) and \(z\in J_+\) satisfies \(z\le x\), then \(x-z\in J_+\). Additivity of \(w\) gives \(w(z)\le w(x)\). The choice \(z=x\) proves \(\Phi(x)=w(x)\). The function \(\Phi\) is monotone by inclusion of the sets in its supremum. Rescaling those sets proves positive homogeneity for positive scalars; the value at zero follows from the order condition and gives the zero-scalar convention.

**Preservation of increasing suprema.** Suppose \(x_i\uparrow x\) in \(B_+\), and put \(p=s(x)\). Douglas factorization gives contractions \(c_i\in B\) such that

\[
c_i x^{1/2}=x_i^{1/2},\qquad c_i=c_i p.
\tag{SX.9}
\]

For clarity, the factorization follows by extending the contraction from \(\operatorname{ran}x^{1/2}\) that sends \(x^{1/2}\xi\) to \(x_i^{1/2}\xi\); its adjoint form, or the commutant test, puts the resulting bounded operator in \(B\). It is zero on \((1-p)H\).

Bounded monotone convergence and continuous functional calculus give \(x_i^{1/2}\to x^{1/2}\) strongly. Equation (SX.9) therefore shows that \(c_i\to p\) on the dense subspace \(\operatorname{ran}x^{1/2}\) of \(pH\). The uniform contraction bound extends this to strong convergence on \(pH\), and both maps vanish on its complement. Set \(b_i=c_i+(1-p)\). Then

\[
b_i\longrightarrow1\text{ strongly},\qquad b_i x b_i^*=x_i.
\tag{SX.10}
\]

For each \(z\in J_+\) with \(z\le x\), the element \(b_i z b_i^*\) belongs to \(J_+\) and is at most \(x_i\). Condition (SX.7) gives

\[
w(z)\le\liminf_i w(b_i z b_i^*)
\le\sup_i\Phi(x_i).
\]

Taking the supremum over \(z\) and using monotonicity for the reverse inequality yields

\[
\Phi(x)=\sup_i\Phi(x_i).
\tag{SX.11}
\]

We have proved this identity before using additivity of \(\Phi\).

**Additivity.** Choose the increasing approximants

\[
x_a=x^{1/2}u_a x^{1/2}\uparrow x,
\qquad y_b=y^{1/2}u_b y^{1/2}\uparrow y.
\]

On the product directed set, \(x_a+y_b\uparrow x+y\), and all three approximating elements belong to \(J_+\). Apply (SX.11), agreement on the ideal, and additivity of \(w\):

\[
\begin{aligned}
\Phi(x+y)
&=\sup_{a,b}w(x_a+y_b)\\
&=\sup_{a,b}\bigl(w(x_a)+w(y_b)\bigr)\\
&=\sup_a w(x_a)+\sup_b w(y_b)
=\Phi(x)+\Phi(y).
\end{aligned}
\tag{SX.12}
\]

The scalar identity holds in \([0,\infty]\): two finite target lower bounds can always be attained at separate indices, and if a supremum is infinite its target bound is arbitrary. Thus \(\Phi\) is a weight, and (SX.11) now proves its normality.

**Uniqueness.** Any normal extension \(\widetilde\Phi\) satisfies

\[
\widetilde\Phi(x)
=\sup_a w(x^{1/2}u_a x^{1/2})=\Phi(x)
\]

by normality and (SX.11). This proves uniqueness on the whole positive cone, including infinite values. ∎

The order of the proof matters. Positive approximants alone would not justify declaring the supremum in (SX.8) additive. Condition (SX.7) first supplies the limiting identity that makes the additivity calculation valid.

## An operator supplies the ideal weight

Assume (SX.5). For a positive element of the coefficient ideal define

\[
w\!\left(\sum_{j=1}^r\theta(\xi_j,\xi_j)\right)
=\sum_{j=1}^rQ_A(\xi_j),\qquad \xi_j\in D_\psi.
\tag{SX.13}
\]

Every element of \(\mathcal J_+\) has such a representation. Condition (SX.5) makes the definition independent of that representation, including the possibility that its value is infinite.

**Lemma.** Formula (SX.13) is a weight on \(\mathcal J_+\) and satisfies (SX.7).

**Proof.** Concatenating two coefficient families proves additivity. Multiplying every vector by \(\sqrt t\) proves homogeneity for \(t>0\); the empty family proves \(w(0)=0\). These arguments use nonnegative extended sums only.

Fix \(z=\sum_{j=1}^r\theta(\xi_j,\xi_j)\), and let \(b_i\to1\) strongly in \(M\). Bounded-vector covariance gives

\[
b_i z b_i^*
=\sum_{j=1}^r\theta(b_i\xi_j,b_i\xi_j),
\tag{SX.14}
\]

and every \(b_i\xi_j\) belongs to \(D_\psi\). The vectors converge in \(H\) to \(\xi_j\). Lower semicontinuity of (SX.4) and the elementary finite-sum inequality for liminf give

\[
w(z)=\sum_j Q_A(\xi_j)
\le\liminf_i\sum_jQ_A(b_i\xi_j)
=\liminf_iw(b_i z b_i^*).
\tag{SX.15}
\]

This includes an infinite summand: for any finite threshold, eventual lower bounds for that summand force the total above the threshold. For finitely many finite lower bounds, a common upper index gives the inequality. Thus (SX.7) holds for arbitrary nets. ∎

Apply SX-02 with \(J=\mathcal J\). It gives a unique normal weight \(\varphi_A\) extending the ideal energy, and the explicit recovery formula is

\[
\varphi_A(x)=\sup\left\{
\sum_{j=1}^rQ_A(\xi_j):
\xi_j\in D_\psi,\ 
\sum_{j=1}^r\theta(\xi_j,\xi_j)\le x
\right\}.
\tag{SX.16}
\]

Neither countable decomposability of the algebra nor a sequence of positive approximants is assumed.

## The core supplies semifiniteness and the exact derivative

**Theorem.** A positive self-adjoint \(A\) is the spatial derivative of a normal semifinite weight if and only if (SX.5) and (SX.6) hold. The weight is unique and is given by (SX.16).

**Reconstruction.** SX-03 constructs a normal weight \(\varphi_A\) satisfying

\[
\varphi_A(\theta(\xi,\xi))=Q_A(\xi)
\quad(\xi\in D_\psi).
\tag{SX.17}
\]

Its finite bounded-vector domain is consequently exactly \(F\). By SC-05 the Hilbert closure of this domain is \(e_{\varphi_A}H\), where \(e_{\varphi_A}\) is the weight's finite-domain projection. The core assumption makes \(F\) dense in \(H\). Hence \(e_{\varphi_A}=1\), and WS-02 proves semifiniteness.

On \(F\), the initial spatial form is the restriction of the closed square-root form of \(A\), by (SX.17) and polarization. Condition (SX.6) says that closing this restriction recovers that entire form with its exact domain \(D(A^{1/2})\). SC-07 and QF's uniqueness therefore identify the spatial derivative with \(A\), including its operator domain.

**Necessity.** Conversely, if \(A=d\varphi/d\psi\) for a normal semifinite \(\varphi\), SC-07 gives the core condition and the identity (SX.17) for every bounded vector, with infinity included. Weight additivity makes equal finite coefficient sums have equal sums of extended energies, proving (SX.5).

**Uniqueness and support.** Equality of all coefficient energies gives equality of the normal weights by SC-04's increasing positive approximants, as also proved in SC-10. SC-09 gives

\[
s(\varphi_A)=s(A),\qquad
\varphi_A\text{ is faithful}\ \Longleftrightarrow\ \ker A=0.
\tag{SX.18}
\]

The zero operator corresponds to the zero weight. Its square-root domain is all of \(H\), its extended energy is everywhere zero, and the dense bounded-vector space is a core. ∎

The extension theorem itself applies to nonsemifinite normal weights. In the present theorem, semifiniteness follows from the specified densely defined operator and its core; it is a proved conclusion, rather than a property inferred from the word “energy”.

## Imaginary powers determine a positive operator

**Lemma.** If \(A,B\) are injective positive self-adjoint operators on a Hilbert space and \(A^{it}=B^{it}\) for every real \(t\), then \(A=B\), with the same domains.

**Proof.** SK gives self-adjoint operators \(L=\log A\), \(K=\log B\) and \(A=e^L\), \(B=e^K\), with their spectral domains. For a self-adjoint \(L\), the scalar integral and bounded spectral calculus give

\[
(L-i)^{-1}\xi
=i\int_0^\infty e^{-t}e^{-itL}\xi\,dt.
\tag{SX.19}
\]

The integral converges in Hilbert norm because its integrand has norm at most \(e^{-t}\|\xi\|\). One can verify the identity first on each bounded spectral interval, by the scalar formula \(i/(1+i\lambda)=(\lambda-i)^{-1}\), and then pass through the spectral cutoffs using the uniform integrable bound. This justifies the integral without a separate theorem about unitary-group generators.

The imaginary-power assumption makes the resolvents of \(L\) and \(K\) equal. A resolvent determines its operator: its range is the operator domain, and on a vector \(\eta=(L-i)^{-1}\xi\) its value is \(L\eta=\xi+i\eta\). Thus \(L=K\). Applying the same Borel function \(e^\lambda\) proves \(A=B\) with equal domains. ∎

For a supported positive operator, imaginary powers are first taken on the complement of its kernel and then extended by zero. Their value at time zero is its support projection. Equality of these families therefore also determines the support and the whole positive operator.

## Two weights on the same support

Let \(p\in M\) be a projection. If \(\alpha\) is NSF on \(pMp\), extend it to a weight on \(M\) by

\[
\overline\alpha(x)=\alpha(pxp),\qquad x\in M_+.
\tag{SX.20}
\]

This weight is normal because compression preserves positive increasing suprema. It is semifinite: finite positive contractions \(e_i\uparrow p\) for \(\alpha\) give finite positive contractions \(e_i+(1-p)\uparrow1\) for \(\overline\alpha\). Its support is exactly \(p\). Indeed \(\overline\alpha(x^*x)=0\) holds precisely when \(xp=0\), by faithfulness of \(\alpha\), so its largest null projection is \(1-p\).

Write \(B_\alpha=d\overline\alpha/d\psi\). By SC-09 and SI-09, it is zero on \((1-p)H\) and its restriction \(B_{\alpha,p}\) to \(pH\) is positive and injective. This restriction implements \(\sigma^\alpha\) on \(pMp\), and its conjugation on \(y|_{pH}\), for \(y\in N\), is \(\sigma_{-t}^\psi(y)|_{pH}\). This formulation uses the original denominator. It does not assign an unspecified weight to the possibly nonfaithful image of \(N\) on \(pH\).

**Supported ratio lemma.** If \(\alpha,\beta\) are NSF on \(pMp\), then their intrinsic balanced-matrix cocycle is

\[
[D\beta:D\alpha]_t
=B_{\beta,p}^{it}B_{\alpha,p}^{-it}
\quad\text{on }pH.
\tag{SX.21}
\]

The intrinsic cocycle is defined on the abstract corner \(pMp\), with its identity \(p\).

**Proof.** Apply the original commutant reference \(\psi\) to the representation of \(M_2(M)\) on \(H\oplus H\). Its commutant is \(\{y\oplus y:y\in N\}\), identified faithfully with \(N\). Use the normal semifinite numerator

\[
\Phi([x_{ij}])=\overline\alpha(x_{11})+\overline\beta(x_{22}).
\]

Its support is \(P=\operatorname{diag}(p,p)\), and its restriction to \(PM_2(M)P\) is the faithful diagonal weight \(\alpha\oplus\beta\).

A vector \((\xi_1,\xi_2)\) is denominator-bounded exactly when both components belong to \(D_\psi\). Its coefficient matrix has entries \(R_\psi(\xi_i)R_\psi(\xi_j)^*\). The numerator evaluates this matrix as the sum of the two component energies. Its finite bounded-vector domain is therefore the direct sum of the two component finite domains. Each is a form core by SC-07; approximating the two components separately proves that their direct sum is a core for the orthogonal sum of the closed forms. Hence closed-form uniqueness gives

\[
\frac{d\Phi}{d\psi}=B_\alpha\oplus B_\beta.
\]

SI-09 identifies its conjugation on the support corner with \(\sigma^{\alpha\oplus\beta}\). At the corner matrix unit \(E_{21}\otimes p\) this gives

\[
\sigma_t^{\alpha\oplus\beta}(E_{21}\otimes p)
=\bigl(B_{\beta,p}^{it}B_{\alpha,p}^{-it}\bigr)
 (E_{21}\otimes p).
\]

The left-hand side is exactly the defining matrix-unit formula for \([D\beta:D\alpha]_t\), as in SI-14 on the algebra \(pMp\). This proves (SX.21) with the same intrinsic definition. All modular actions used here are those of the displayed faithful corner weights. ∎

## The covariance characterization, with the kernel retained

For \(A\ge0\) self-adjoint, let \(p=s(A)\), and define \(U_t\) to be \(A^{it}\) on \(pH\), extended by zero on \((1-p)H\). In particular \(U_0=p\).

**Characterization theorem.** The following conditions are equivalent:

1. \(A=d\varphi/d\psi\) for a normal semifinite weight \(\varphi\) on \(M\).
2. For every \(y\in N\) and every real \(t\),

\[
U_t\sigma_t^\psi(y)=yU_t.
\tag{SX.22}
\]

3. The full extended-energy condition (SX.5) and the graph-core condition (SX.6) hold.

The numerator is unique and has support \(p\). The diagram of the proved implications is

\[
\text{normal semifinite numerator}
\ \Longleftrightarrow\
\text{covariance (SX.22)}
\ \Longleftrightarrow\
\text{all-energy consistency and graph core}.
\tag{SX.23}
\]

**Proof of the direct implications.** The equivalence of conditions 1 and 3 is SX-04. If condition 1 holds, SC gives \(p=s(\varphi)\), and SI-09 proves (SX.22) with exactly the supported convention above. No faithfulness of \(\varphi\) is needed.

**Construction from covariance.** At \(t=0\), (SX.22) reads \(py=yp\) for every \(y\in N\). Thus \(p\in N'=M\); this is a consequence of the condition. If \(p=0\), positivity gives \(A=0\), and the zero weight is the required numerator. Assume \(p\ne0\), and write \(A_p\) for the injective positive restriction to \(pH\).

Choose an NSF weight \(\omega\) on \(pMp\), which exists by WH-13 at arbitrary cardinality. Extend it to \(\overline\omega\) as in SX-06, and let \(B=d\overline\omega/d\psi\), with injective supported restriction \(B_p\). The covariance condition and SI-09 say that both \(A_p^{it}\) and \(B_p^{it}\) implement \(y|_{pH}\mapsto\sigma_{-t}^\psi(y)|_{pH}\). Therefore

\[
u_t=A_p^{it}B_p^{-it}
\]

commutes with every \(y|_{pH}\). Extending it by zero to the complement gives an element of \(pMp\): the extended operator commutes with \(N\), and its support is contained in \(p\). It is a unitary in this corner, whose identity is \(p\). The family is strongly* continuous by the spectral continuity of both imaginary-power groups.

Since \(\sigma_s^\omega\) is implemented by \(B_p^{is}\), multiplication gives

\[
\begin{aligned}
u_s\sigma_s^\omega(u_t)
&=A_p^{is}B_p^{-is}
  B_p^{is}A_p^{it}B_p^{-it}B_p^{-is}\\
&=A_p^{i(s+t)}B_p^{-i(s+t)}=u_{s+t}.
\end{aligned}
\]

This is the cocycle law; no commutation between \(A_p\) and \(B_p\) has been used.

The inverse weight-cocycle theorem Existence, uniqueness and the prescribed cocycle, applied to the NSF weight \(\omega\) on the algebra \(pMp\), supplies an NSF weight \(\chi\) on that corner with \([D\chi:D\omega]_t=u_t\). This is the substantive converse theorem: it is not inferred merely from the cocycle identity.

Extend \(\chi\) to \(\varphi(x)=\chi(pxp)\), and let \(C=d\varphi/d\psi\). SX-06 shows that \(\varphi\) is normal and semifinite with support \(p\), and its supported ratio formula gives

\[
C_p^{it}B_p^{-it}=[D\chi:D\omega]_t
=A_p^{it}B_p^{-it}.
\]

Cancel the right unitary and apply SX-05. We obtain \(C_p=A_p\) with equality of their domains. Both whole-space operators have the zero summand on \((1-p)H\), so \(C=A\). This proves condition 1. Uniqueness and the support assertion were already proved in SX-04. ∎

This proof keeps the denominator on the original commutant throughout. It needs neither a faithful state nor a weight on an unidentified quotient of that commutant. The finite-energy-only condition refuted next is not one of the equivalent conditions in this theorem.

## A dense form domain made of analytic functions

We now test the weaker condition that compares (SX.5) only when every vector is already in \(F\). The following construction will satisfy that condition and the full core requirement, while failing to define any weight.

Choose numbers

\[
\lambda_n\in\left(\frac1{n+1},\frac1n\right),\qquad n\ge1,
\tag{SX.24}
\]

which are linearly independent over \(\mathbb Q\). At each step the rational span of the previous finite set is countable, so it cannot exhaust the required interval. This recursive construction gives \(\lambda_n\to0\), and

\[
\lambda_n+\lambda_m=\lambda_r+\lambda_s
\quad\Longrightarrow\quad
\{n,m\}=\{r,s\}
\text{ as unordered pairs with multiplicity}.
\tag{SX.25}
\]

We record the scalar uniqueness fact used twice below. If \(t_j\in[0,L]\), \(\sum_j|d_j|<\infty\), and

\[
\sum_jd_j e^{t_jx}=0\quad(0\le x\le1),
\tag{SX.26}
\]

then \(\sum_{j:t_j=t}d_j=0\) for each real \(t\). Indeed the series converges uniformly on compact complex sets and has a power series with coefficients \(\sum_jd_jt_j^k/k!\). Vanishing on an interval makes all coefficients zero: a least nonzero coefficient would prevent zeros from accumulating at zero. Thus \(\sum_jd_jP(t_j)=0\) for every polynomial \(P\).

Here is a direct reminder of the needed polynomial approximation. On \([0,1]\), the Bernstein polynomial of a continuous \(f\) is

\[
B_mf(x)=\sum_{k=0}^m f(k/m)\binom mk x^k(1-x)^{m-k}.
\]

The coefficients form a probability distribution with mean \(x\) and variance \(x(1-x)/m\). For \(\delta>0\), split the sum according to \(|k/m-x|\le\delta\). Uniform continuity bounds the first contribution to \(|B_mf(x)-f(x)|\) by the modulus of continuity at \(\delta\). The other contribution is at most \(2\|f\|_\infty/(4m\delta^2)\), by the variance bound. First choose \(\delta\) and then \(m\), proving uniform convergence. Rescaling gives polynomial approximation on \([0,L]\).

Consequently \(\sum_jd_j f(t_j)=0\) for every continuous \(f\) on that interval. Apply this to the triangular functions

\[
f_\varepsilon(s)=\max\{0,1-|s-t|/\varepsilon\}.
\]

As \(\varepsilon\downarrow0\), dominated convergence for the absolutely summable series gives exactly the asserted sum at the atom \(t\). This proves the uniqueness fact, even when the points \(t_j\) accumulate or are repeated.

Now take

\[
H=L^2([0,1],dx),\qquad M=N=L^\infty([0,1],dx),
\qquad \psi(a)=\int_0^1a(x)\,dx.
\tag{SX.27}
\]

The algebra acts by multiplication and is its own commutant. Indeed, if \(T\) commutes with every bounded multiplier, put \(g=T1\). Then \(Tf=fg\) for bounded \(f\). The estimate \(\|fg\|_2\le\|T\|\|f\|_2\), tested on indicators, gives \(g\in L^\infty\). Density of bounded functions in \(L^2\) now identifies \(T\) with multiplication by \(g\). The denominator is faithful, normal and finite. Its bounded vectors are exactly \(L^\infty\): the estimate \(\|y\xi\|_2\le C\|y\|_2\) for bounded \(y\) implies \(|\xi|\le C\) almost everywhere by testing indicators. Conversely this essential bound gives the estimate. Therefore

\[
R_\psi(\xi)=\text{multiplication by }\xi,
\qquad \theta(\xi,\xi)=\text{multiplication by }|\xi|^2.
\tag{SX.28}
\]

Define a bounded linear operator from \(\ell^2(\mathbb N)\) to \(H\) by

\[
(Kc)(x)=\sum_{n\ge1}2^{-n}c_n e^{\lambda_n x}.
\tag{SX.29}
\]

Cauchy–Schwarz gives \(\sum_n2^{-n}|c_n|\le(\sum_n4^{-n})^{1/2}\|c\|_2\). Since \(0<\lambda_n<1\), the same estimate shows uniform convergence on compact complex sets. Each \(Kc\) is the restriction of an entire function, and in particular is bounded and continuous on \([0,1]\). It also proves boundedness of \(K\).

**Injectivity.** If \(Kc=0\) in \(H\), continuity makes its representative zero throughout \([0,1]\). The scalar uniqueness fact, applied to distinct points \(t_n=\lambda_n\) and coefficients \(d_n=2^{-n}c_n\), gives \(c_n=0\) for every \(n\).

**Dense range.** If \(g\in H\) is orthogonal to the range, the function

\[
G(z)=\int_0^1 e^{zx}\overline{g(x)}\,dx
\]

has a globally convergent power series and vanishes at every \(\lambda_n\). These nonzero points accumulate at zero, so all its Taylor coefficients vanish by the same least-coefficient argument. Thus \(g\) is orthogonal to every polynomial. Continuous functions are dense in this scalar \(L^2\) space, as in SK-02, and the polynomial approximation just proved makes polynomials dense there. Hence \(g=0\).

On the dense range of \(K\), define

\[
D(q)=\operatorname{ran}K,\qquad q(Kc,Kd)=\langle c,d\rangle_{\ell^2}.
\tag{SX.30}
\]

Injectivity makes this well-defined. It is a closed positive form. To verify closedness, a form-Cauchy sequence \(Kc_j\) has \(c_j\to c\) in \(\ell^2\); boundedness of \(K\) gives convergence to \(Kc\) in \(H\), and both components of the form norm then converge. QF-03 supplies a positive self-adjoint operator \(A\) with

\[
D(A^{1/2})=\operatorname{ran}K,\qquad Q_A(Kc)=\|c\|_2^2.
\tag{SX.31}
\]

In fact \(A\ge\|K\|^{-2}I\), because \(\|Kc\|\le\|K\|\|c\|\). It is injective and bounded below by a positive scalar. Its entire form domain is contained in \(D_\psi=L^\infty\); hence \(F=D(A^{1/2})\) and the core requirement is satisfied in the strongest possible way.

## Every finite-energy comparison passes

Take finite families \(c^{(1)},\ldots,c^{(r)}\) and \(d^{(1)},\ldots,d^{(s)}\) in \(\ell^2\). Suppose that their coefficient sums agree:

\[
\sum_{j=1}^r|Kc^{(j)}(x)|^2
=\sum_{k=1}^s|Kd^{(k)}(x)|^2
\quad\text{for almost every }x\in[0,1].
\tag{SX.32}
\]

The two sides are continuous, so equality holds everywhere. Expand their difference as

\[
\sum_{n,m\ge1} a_{nm}e^{(\lambda_n+\lambda_m)x}=0,
\tag{SX.33}
\]

where

\[
a_{nm}=2^{-n-m}\left(
\sum_j c_n^{(j)}\overline{c_m^{(j)}}
-\sum_k d_n^{(k)}\overline{d_m^{(k)}}
\right).
\tag{SX.34}
\]

This double sequence is absolutely summable. For each vector \(c\), the sum of the absolute values of its contribution is \((\sum_n2^{-n}|c_n|)^2<\infty\), and there are only finitely many such contributions. Therefore expansion, rearrangement and the uniqueness fact of SX-08 all apply.

At the exponent \(2\lambda_n\), condition (SX.25) permits only the diagonal term \((n,n)\). Thus (SX.33) implies

\[
\sum_j|c_n^{(j)}|^2=\sum_k|d_n^{(k)}|^2
\quad\text{for every }n.
\tag{SX.35}
\]

Summing these nonnegative equalities gives

\[
\sum_j Q_A(Kc^{(j)})
=\sum_j\|c^{(j)}\|_2^2
=\sum_k\|d^{(k)}\|_2^2
=\sum_k Q_A(Kd^{(k)}).
\tag{SX.36}
\]

Every vector in the form domain has exactly such a representation. Thus the operator satisfies the finite-only coefficient condition for every eligible finite family, not merely for the displayed basis vectors.

## The same data violate positivity of a weight

Let \(e_n\) be the standard basis of \(\ell^2\), put \(\xi_n=Ke_n\), and write \(f_n=|\xi_n|^2\) for its positive coefficient. Then

\[
f_n(x)=4^{-n}e^{2\lambda_nx},\qquad Q_A(\xi_n)=1.
\tag{SX.37}
\]

Because \(\lambda_2<\lambda_1\) and \(x\ge0\),

\[
0\le f_2\le\frac14 f_1.
\tag{SX.38}
\]

If a weight \(\varphi\) agreed with these finite coefficient energies, it would have \(\varphi(f_1)=\varphi(f_2)=1\). Additivity and positivity of a weight imply monotonicity, so (SX.38) would give \(1\le1/4\), a contradiction. No weight, even without normality or semifiniteness, extends the finite data.

The missing infinite-energy comparison is also explicit. Let

\[
\xi=\xi_1,\qquad
\eta(x)=\operatorname{sgn}(x-1/2)\xi_1(x).
\tag{SX.39}
\]

Both vectors belong to \(D_\psi\), and their coefficients agree. The first has energy one. The second has no continuous representative: equality almost everywhere with a continuous function on each side would force its two one-sided limits at \(1/2\) to be the opposite nonzero values \(-\xi_1(1/2)\) and \(\xi_1(1/2)\). Every element of \(\operatorname{ran}K\) has a continuous representative. Hence

\[
Q_A(\xi)=1,\qquad Q_A(\eta)=+\infty,
\qquad\theta(\xi,\xi)=\theta(\eta,\eta).
\tag{SX.40}
\]

This contradicts (SX.5), while SX-09 proves all comparisons restricted to finite energy.

The example has a faithful finite denominator and a strictly positive operator with full support. Those additional assumptions therefore do not repair the finite-only criterion. The corrected theorem is SX-04: equality must include the extended values of all bounded-vector decompositions. The finite-only statement remains necessary for a spatial derivative, but it is not a sufficient characterization.

## Two small coefficient tests

**A scalar numerator algebra.** Let \(H=\mathbb C^2\), let \(M=\mathbb CI\), and let \(N=B(\mathbb C^2)\) carry the ordinary trace \(\psi\). Its GNS space is the Hilbert–Schmidt space, and

\[
R_\psi(\xi)a=a\xi,\qquad
R_\psi(\xi)^*v=v\xi^*,\qquad
\theta(\xi,\xi)=\|\xi\|^2I.
\tag{SX.41}
\]

The adjoint formula follows by taking the Hilbert–Schmidt trace pairing with an arbitrary matrix \(a\); applying \(R_\psi(\xi)\) then gives the coefficient formula.

A normal semifinite weight on \(\mathbb CI\) has the form \(\varphi(cI)=tc\) with \(0\le t<\infty\), so its derivative is \(tI\). Conversely the coefficient criterion forces every positive operator to have the same energy on all unit vectors, hence to be scalar by polarization. For \(A=\operatorname{diag}(1,3)\), the vectors \(e_1,e_2\) have the same coefficient \(I\) and different energies. Thus the failure is detected by a single finite comparison. Since the trace modular group is trivial, covariance would also require all imaginary powers to commute with \(B(\mathbb C^2)\), which would make \(A\) scalar by SX-05 and the commutant test.

**A scalar denominator algebra.** On the same \(H\), instead let \(M=B(\mathbb C^2)\), \(N=\mathbb CI\), and \(\psi(cI)=\kappa c\) with \(\kappa>0\). Realize the denominator GNS map as \(\Lambda_\psi(cI)=\sqrt\kappa c\). Then

\[
R_\psi(\xi)z=\kappa^{-1/2}z\xi,
\qquad\theta(\xi,\xi)=\kappa^{-1}|\xi\rangle\langle\xi|.
\tag{SX.42}
\]

For every positive matrix \(A\), the reconstructed weight is

\[
\varphi_A(x)=\kappa\operatorname{Tr}(Ax),\qquad x\ge0.
\tag{SX.43}
\]

Indeed its value on (SX.42) is \(\langle A\xi,\xi\rangle\), and every positive matrix is a finite sum of rank-one coefficients. This verifies the extension and its uniqueness directly. Its support is the range projection of \(A\), so a rank-one \(A\) gives a nonfaithful weight. The covariance identity imposes no further restriction here, because the commutant consists of scalars.

## Problems with complete solutions

**1. A positive difference missing from the finite-energy cone.** In SX-08–10, put \(d=f_1/4-f_2\). Show that \(d\ge0\), but \(d\) is not a finite sum of coefficients of vectors in \(D(A^{1/2})\).

**Solution.** Positivity is (SX.38). If \(d=\sum_j\theta(\zeta_j,\zeta_j)\) with every \(\zeta_j\) in the finite domain, then

\[
\theta(\xi_1/2,\xi_1/2)
=\theta(\xi_2,\xi_2)+\sum_j\theta(\zeta_j,\zeta_j).
\]

All displayed vectors would be finite energy. SX-09 would force
\(1/4=1+\sum_jQ_A(\zeta_j)\), impossible. The finite-energy coefficient cone therefore need not contain the positive differences of its own elements. This explains precisely why finite additivity on that cone does not imply monotonicity for the ambient order.

**2. Strong convergence does not justify moving an adjoint through a limit.** On \(\ell^2(\{0,1,2,\ldots\})\), put \(b_n=I+|e_0\rangle\langle e_n|\), \(n\ge1\). Determine the strong limits of \(b_n\) and the behavior of \(b_n^*e_0\). For \(\omega(x)=\langle xe_0,e_0\rangle\), compare \(\omega(I)\) with \(\omega(b_n b_n^*)\).

**Solution.** The error \((b_n-I)\xi=\langle\xi,e_n\rangle e_0\) tends in norm to zero for every \(\xi\in\ell^2\), so \(b_n\to I\) strongly. But \(b_n^*e_0=e_0+e_n\), whose distance from \(e_0\) is always one. Thus the adjoints do not converge strongly. Also

\[
b_n b_n^*=I+|e_0\rangle\langle e_n|
+|e_n\rangle\langle e_0|+|e_0\rangle\langle e_0|,
\]

so \(\omega(b_n b_n^*)=2\), whereas \(\omega(I)=1\). The inequality in (SX.7) can be strict, even for a bounded normal weight. A proof using a purported strong limit \(b_n z b_n^*\to z\) would be invalid.

In general, the restriction of any normal weight satisfies (SX.7). To prove this without that invalid limit, write a dominated normal functional as \(\omega=\sum_k\omega_{v_k}\) using SC-02 and NW-11. Strong convergence of \(b_i\) gives weak convergence \(b_i^*v_k\to v_k\). Weak lower semicontinuity of the Hilbert norm, followed by finite partial sums, gives

\[
\omega(z)=\sum_k\|z^{1/2}v_k\|^2
\le\liminf_i\sum_k\|z^{1/2}b_i^*v_k\|^2
=\liminf_i\omega(b_i z b_i^*).
\]

Take the supremum over all dominated normal functionals. This proves the necessary inequality for an arbitrary normal weight, with infinity included. No uniform bound on the entire index set of a convergent net is used.

**3. Normal ideal extension need not be semifinite.** Let \(B=B(\ell^2)\), let \(J\) be the finite-rank ideal, and define \(w(0)=0\), \(w(z)=\infty\) for every nonzero \(z\in J_+\). Verify (SX.7) and compute the normal extension.

**Solution.** A sum of positive elements is zero precisely when both are zero, so this is an ideal weight. If \(z\ne0\), choose \(v\) with \(z^{1/2}v\ne0\). For \(b_i\to1\) strongly, \(b_i z^{1/2}v\to z^{1/2}v\ne0\). Thus \(b_i z b_i^*\ne0\) eventually, because it equals \((b_i z^{1/2})(b_i z^{1/2})^*\). Both sides of (SX.7) are then infinite. The case \(z=0\) is immediate.

If \(x\ge0\) is nonzero, choose a unit vector \(v\) with \(x^{1/2}v\ne0\). The rank-one operator

\[
z=|x^{1/2}v\rangle\langle x^{1/2}v|
=x^{1/2}|v\rangle\langle v|x^{1/2}
\]

satisfies \(0<z\le x\). Hence (SX.8) gives \(\Phi(x)=\infty\) for every nonzero positive \(x\), and \(\Phi(0)=0\). This weight is normal: a positive increasing net with nonzero supremum has a nonzero member, and consequently an infinite supremum of weight values. Its finite cone is only \(\{0\}\), so it is not semifinite. A dense finite-energy core, used in SX-04, excludes exactly this possibility in operator reconstruction.

**4. Scaling the reference does not change the numerator.** Suppose \(A=d\varphi/d\psi\) and \(c>0\). Show directly from coefficients that the same numerator is reconstructed from \(A/c\) with denominator \(c\psi\).

**Solution.** Identify the two GNS spaces by \(\Lambda_{c\psi}(y)\mapsto\sqrt c\,\Lambda_\psi(y)\). The bounded-vector spaces agree, and the coefficient for the new reference is \(c^{-1}\theta_\psi(\xi,\xi)\). Its \(\varphi\)-value is \(c^{-1}Q_A(\xi)=Q_{A/c}(\xi)\), with the same finite domain and core. Thus SX-04 reconstructs \(\varphi\). Equality also follows from SS-11, but the computation displays the factor in the actual inverse formula. Setting \(c=0\) would remove faithfulness of the reference and is outside the construction.

## Correspondence and further questions

The ideal extension proof establishes existence, arbitrary-net normality, additivity on the whole positive cone, and uniqueness of the normal extension. The spatial application proves semifiniteness from the actual finite-energy core and identifies the entire square-root form and self-adjoint operator. These claims supply the valid mathematical content behind the ideal-weight reconstruction argument in IX.3.12. The stronger all-energy condition is stated explicitly; SX-08–10 proves why the finite-only condition printed in IX.3.11 cannot supply it.

The covariance criterion uses the inverse weight-cocycle theorem at its full NSF generality and then treats a nonfaithful numerator on its support. It does not assume that the original concrete representation is standard. No crossed-product dual weight, action cocycle or cohomology result is asserted here.

A useful research route is to identify smaller collections of coefficient comparisons which still force compatibility with positive order and infinite energy. SX-12, Problem 1 identifies one necessary difficulty: the finite-energy coefficient cone may fail to be hereditary. Any proposed replacement test must address that difficulty and the full graph-core condition before it can be a reconstruction theorem. This is a route for investigating alternative formulations; the covariance and all-energy characterizations already stated are known mathematics with the course proofs given here and in the named dependencies.
