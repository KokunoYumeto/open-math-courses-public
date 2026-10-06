# Stable modes and the algebra of boundary data

A frozen boundary equation asks which normal profiles remain bounded inside the domain, and which boundary measurements determine those profiles. For systems, the number of profiles counts algebraic multiplicity. Eigenvectors alone can miss solutions. This lesson constructs the bounded solution space from Cauchy data, then changes the equation while preserving that space and its boundary measurements.

Section 13 of [Metric and topological foundations](metric-foundation-bridges.md#original-scalar-calculus-and-its-finite-coordinate-receivers) proves the full original scalar and finite-coordinate calculus. Its Section 13.12 gives the exact Gaussian, Rayleigh, logarithmic-contour, matrix and half-line receiving maps, retaining every original factor, endpoint and norm.

The complete original real-number, compactness, extrema and finite-norm proofs are in Section 12 of [Metric and topological foundations](metric-foundation-bridges.md#real-numbers-and-finite-dimensional-topology). Its Section 12.10 gives the exact receiving minimum and spectral-contour maps; the original coordinates, norms and constants are retained.

Throughout, vector spaces are finite-dimensional and complex, coefficients are constant in the normal variable, and

\[
D=-i\frac{d}{dt},\qquad t\in\mathbb R.
\]

We call a solution *stable* when it is bounded for \(t\geq0\). Under the no-real-root hypotheses below, this is equivalent to exponential decay of the solution and every derivative. No diagonalizability, simplicity of roots, commutation of matrix coefficients, or prescribed number of boundary equations is assumed.

[Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md) proves scalar polynomial division over \(\mathbb C\), Bézout, Cayley–Hamilton, complex triangularization, and the contour moments for globally convergent power-series numerators with specified spectral indices. That lesson now proves the complex-root theorem and the full determinant, kernel and invariant-quotient maps in Section 9. Sections 10.1--10.9 there supply the full finite bases and direct sums, projection rank and trace, matrix algebra, original-inner-product adjoints and operator norms. Compactness of the original unit sphere retains its separate topological base. Section 16 below makes the original annihilator and Cauchy receiving maps explicit. We also use its locally uniform exponential-series calculus, termwise differentiation and integration under uniform convergence, and dominated differentiation of exponentially decreasing tails. The spectral and ODE consequences needed here are proved below.

## 1. Spectral calculus without an eigenbasis

Let \(V\) be a finite-dimensional complex vector space and \(A\in\operatorname{End}(V)\). Choose any norm. The series

\[
E_A(t)=\sum_{k=0}^{\infty}\frac{(itA)^k}{k!}
\]

converges locally uniformly with all derivatives, since its norms and the norms of its differentiated terms are bounded by scalar exponential series. Thus \(DE_A=AE_A\), \(E_A(0)=I\), and multiplication of absolutely convergent series gives \(E_A(-t)E_A(t)=I\). If \(Du=Au\), differentiating \(E_A(-t)u(t)\) shows that it is constant. Consequently

\[
u(t)=E_A(t)v                                                 \tag{S1}
\]

is the unique solution with \(u(0)=v\). In particular the solution space has dimension \(\dim V\).

Here is the spectral information, including the nilpotent terms. Keep an original least-degree nonzero annihilator \(m\) with leading coefficient \(c_m\ne0\). Its named monic comparison has factorization \(\prod_{\zeta}(z-\zeta)^{\nu_\zeta}\); the original polynomial is \(m=c_m\prod_{\zeta}(z-\zeta)^{\nu_\zeta}\), with every unit and multiplicity retained. Section 16.1 proves the full scalar-unit and polynomial evaluation maps. The spectral label \(\lambda\) used there denotes the same actual root as \(\zeta\) here, through the identity \(\lambda=\zeta\). The factors are pairwise relatively prime. Repeated Bézout identities give polynomials \(e_\zeta\) which are one modulo \((z-\zeta)^{\nu_\zeta}\) and zero modulo every other factor. Their sum is one modulo the named comparison, while the full original calculation uses \(M_\zeta=m/(z-\zeta)^{\nu_\zeta}=c_mH_\zeta\) and \(e_\zeta=(c_m^{-1}b_\zeta)M_\zeta\). Formula (SR2) retains both original scalar factors. Evaluation at \(A\) therefore gives projections

\[
Q_\zeta=e_\zeta(A),\quad
Q_\zeta Q_\eta=0\ (\zeta\ne\eta),\quad
\sum_\zeta Q_\zeta=I.
\]

Their images are exactly

\[
V_\zeta=\ker(A-\zeta I)^{\nu_\zeta}.
\]

Indeed, the polynomial congruences show both inclusion in this kernel and that \(Q_\zeta\) is the identity there. Thus \(V=\bigoplus V_\zeta\). On \(V_\zeta\), write \(A=\zeta I+N_\zeta\), where \(N_\zeta^{\nu_\zeta}=0\). The inverse and the evolution on that summand are

\[
(zI-A)^{-1}|_{V_\zeta}
=\sum_{k=0}^{\nu_\zeta-1}\frac{N_\zeta^k}{(z-\zeta)^{k+1}},
\qquad
E_A(t)|_{V_\zeta}
=e^{it\zeta}\sum_{k=0}^{\nu_\zeta-1}\frac{(it)^kN_\zeta^k}{k!}. \tag{S2}
\]

The first identity follows by multiplying a finite geometric series; the second follows from the exponential series for commuting \(\zeta I\) and \(N_\zeta\). The entire-series contour moment formula from the preceding lesson, applied to the first identity, yields

\[
E_A(t)=\frac{1}{2\pi i}\int_\Gamma
e^{itz}(zI-A)^{-1}\,dz,                                    \tag{S3}
\]

where \(\Gamma\) is a finite union of positively oriented closed contours enclosing every eigenvalue once and no point of the spectrum on the contours. Integrating the resolvent alone around a single eigenvalue gives \(Q_\zeta\). These assertions also follow directly from (S2), so multiple poles are included.

The full characteristic/pole comparison is proved in Sections 16.2--16.3, including the exact nonzero leading resolvent coefficient. For later counting, \(\dim V_\zeta\) equals the algebraic multiplicity of \(\zeta\) in \(\det(zI-A)\). The direct sum decomposes the determinant into the determinants of the restrictions. A nilpotent map is upper triangular with zero diagonal in a basis adapted to its successive kernels; the restriction to \(V_\zeta\) therefore contributes \((z-\zeta)^{\dim V_\zeta}\). The length of a nilpotent chain affects polynomial factors in time, while the dimension of the whole generalized eigenspace determines the number of solutions.

The exact original annihilator and scalar-unit calculation in Sections 16.1--16.4 proves these same operators and contour formulas with every leading factor shown.

## 2. A monic equation and its complete Cauchy coordinates

Let \(E\) have dimension \(N\), let \(m\geq1\), and put

\[
p(z)=z^m I+\sum_{j=0}^{m-1}p_jz^j,
\qquad p_j\in\operatorname{End}(E).                         \tag{S4}
\]

The scalar variable \(z\) commutes with every coefficient; the coefficients need not commute with each other. The case \(E=0\) has only zero solutions and determinant one; the following arguments can be read with \(N>0\).

For \(x=(x_0,\ldots,x_{m-1})\in E^m\), define the companion map

\[
C_px=(x_1,\ldots,x_{m-1},-p_0x_0-\cdots-p_{m-1}x_{m-1}).
\]

If \(p(D)u=0\), its state \(J u=(u,Du,\ldots,D^{m-1}u)\) satisfies \(D(Ju)=C_pJu\). Conversely, the first \(m-1\) rows of this first-order equation imply that any state solution is the jet of its first component, and the last row gives \(p(D)u=0\). Applying Section 1 proves existence and uniqueness for arbitrary Cauchy data and gives \(\dim\ker p(D)=mN\).

We will need the exact characteristic polynomial:

\[
\det(zI_{E^m}-C_p)=\det p(z).                              \tag{S5}
\]

For a direct determinant check, make the triangular change of variables
\(x_0=y_0\) and \(x_j=zx_{j-1}+y_j\) for \(1\leq j<m\); its determinant is one. The first \(m-1\) rows of \((zI-C_p)x\) become \(-y_1,\ldots,-y_{m-1}\), and the coefficient of \(y_0\) in the last row is \(p(z)\). Move that last block row to the front and eliminate its other entries using the identity block rows. The block-row permutation has sign \((-1)^{N^2(m-1)}\), and the negative identities contribute \((-1)^{N(m-1)}\). Their product is one. This proves (S5), as a polynomial identity, without assuming that any \(p_j\) is invertible.

There is also a useful polynomial encoding of a jet. Set \(p_m=I\) and

\[
\mathcal U_x(z)=
\sum_{0\leq k\leq j<m}p_{j+1}x_{j-k}z^k.                 \tag{S6}
\]

This maps \(E^m\) bijectively onto the \(E\)-valued polynomials of degree less than \(m\). To see this, read coefficients from the highest power downwards: the coefficient of \(z^{m-1}\) is \(x_0\), the next is \(x_1+p_{m-1}x_0\), and in general the next unknown \(x_r\) occurs with coefficient \(I\), accompanied only by already recovered \(x_0,\ldots,x_{r-1}\).

Let \(\pi_0:E^m\to E\) be the first coordinate. Solving \((zI-C_p)w=x\) gives

\[
w_j=z^jw_0-\sum_{r=0}^{j-1}z^{j-1-r}x_r,
\qquad
p(z)w_0=\mathcal U_x(z).
\]

The latter equality follows by substituting the first formula into the last block row; its coefficient of \(x_r\) is \(\sum_{j=r}^{m-1}p_{j+1}z^{j-r}\). Consequently (S3), applied to \(C_p\), gives the solution with jet \(x\):

\[
u(t)=\frac{1}{2\pi i}\int_\Gamma
p(z)^{-1}\mathcal U_x(z)e^{itz}\,dz.                       \tag{S7}
\]

The contours enclose all roots of \(\det p\). Formula (S7) is valid for repeated roots and matrix poles of arbitrary order. It is the finite sum of the pole moments computed from (S2). The triangular bijection above proves uniqueness of the polynomial in this representation, as well as existence. In particular, it does not require a factorization of \(p\) into linear matrix factors.

Section 16.7 proves the corresponding original numerator, inverse coordinates, resolvent and contour maps when the actual leading matrix is any invertible \(p_m\). It retains its full determinant and both block signs.

## 3. Bounded solutions, derivatives, and multiplicity

First, boundedness of a solution of a monic constant-coefficient equation controls all its derivatives. This fact is useful before any spectral separation is imposed.

**Lemma.** If \(r\) is any monic matrix polynomial and \(r(D)u=0\), then boundedness of \(u\) on \([0,\infty)\) implies boundedness there of \(D^ku\) for every \(k\geq0\).

**Proof.** Write \(C=C_r\), with state space \(W\), and define

\[
h(v)=\int_0^1\|\pi_0E_C(s)v\|^2\,ds.
\]

If \(h(v)=0\), the continuous integrand vanishes on the interval. Its derivatives at zero then vanish, so every Cauchy coordinate of \(v\) is zero. The positive function \(h\) has a positive minimum \(c\) on the unit sphere. Thus for every \(t\geq0\),

\[
c\|Ju(t)\|^2\leq
\int_0^1\|u(t+s)\|^2\,ds.
\]

All components of the state are bounded. Repeated differentiation of \(D(Ju)=CJu\) expresses every higher derivative through a fixed power of \(C\), proving the claim. The same argument with integration over \([-1,0]\) proves the negative-half-line version. An equation with invertible leading coefficient is first multiplied on the left by its inverse. \(\square\)

Assume now that \(A\) has no real eigenvalues. Define

\[
q_A=\sum_{\operatorname{Im}\zeta>0}Q_\zeta
=\frac{1}{2\pi i}\int_{\Gamma_+}(zI-A)^{-1}\,dz,             \tag{S8}
\]

where \(\Gamma_+\) surrounds precisely the upper-half-plane spectrum. This is a projection commuting with \(A\). On its image, (S2) shows that \(E_A(t)\) and all its derivatives decay as \(t\to+\infty\): every polynomial factor is dominated by the exponential \(e^{-t\operatorname{Im}\zeta}\). On the image of \(I-q_A\), the corresponding decay holds as \(t\to-\infty\).

Conversely, if \(E_A(t)v\) is bounded for \(t\geq0\), set \(v_-=(I-q_A)v\). Then

\[
v_-=E_A(-t)(I-q_A)E_A(t)v.
\]

The norm of \(E_A(-t)\) on the lower spectral subspace tends to zero, by (S2), while the last factor is bounded. Taking \(t\to\infty\) gives \(v_-=0\). The negative-half-line assertion follows with signs reversed. Hence initial evaluation identifies the two bounded solution spaces with \(q_AV\) and \((I-q_A)V\), and every solution splits uniquely into one of each kind.

For (S4), assume

\[
\det p(\xi)\ne0\qquad(\xi\in\mathbb R).                    \tag{S9}
\]

The companion characteristic identity and the lemma imply that its stable solution space

\[
\mathcal M^+(p)=
\{u\in C^\infty(\mathbb R,E):p(D)u=0,
\ \sup_{t\geq0}\|u(t)\|<\infty\}
\]

corresponds under \(J\) exactly to \(q_{C_p}E^m\). All its derivatives decay exponentially. The dimension is the sum of the algebraic multiplicities of the roots of \(\det p\) in the upper half-plane. The analogous lower space gives a direct-sum decomposition of all solutions. The statement counts generalized modes, even if the scalar determinant has high multiplicity and the space of ordinary eigenvectors is small.

Section 16.5 also proves the exact bounded modes when real roots are present; those extra modes are distinguished from the original no-real-root decay assertion above.

## 4. Parameters and fixed projections

Suppose \(A(y)\) is a \(C^r\) family on an open parameter set, where \(0\leq r\leq\infty\), and every \(A(y)\) has no real eigenvalues. Near a fixed parameter one can choose the same contours in (S8): invertibility on a compact contour persists under small matrix perturbations. The resolvent is \(C^r\), and, for one derivative,

\[
\partial_y(zI-A)^{-1}
=(zI-A)^{-1}(\partial_y A)(zI-A)^{-1}.                      \tag{S10}
\]

Repeated differentiation gives finite sums of ordered products of such factors; their order cannot be changed when matrices do not commute. Differentiating the contour integral proves that \(q_A(y)\) is \(C^r\). Since the rank of a projection is its integer-valued trace, its rank is locally constant. A basis of its image at one parameter remains a basis after applying nearby projections, so the stable spaces form a \(C^r\) vector bundle. A global eigenbasis or a splitting into individual eigenvalue branches is unnecessary.

On a compact parameter set contained in this no-real-spectrum region, there are constants \(\delta>0\) and \(C_k\) such that

\[
\|D_t^k E_{A(y)}(t)q_{A(y)}\|\leq C_k e^{-\delta t}
\qquad(t\geq0).                                           \tag{S11}
\]

To justify the common contour used for this estimate, matrix norms give a common bound for all eigenvalues. If their distances from the real axis had no positive lower bound, a convergent sequence of parameters and a convergent subsequence of eigenvalues would give a real eigenvalue at the limiting parameter, by continuity of the determinant. Choose a rectangle enclosing all upper eigenvalues with its lower side strictly above the real axis, and with its other sides beyond the common spectral bound. Its distance from the spectra is positive. Formula (S3) with this contour, and \(D_t^ke^{itz}=z^ke^{itz}\), proves (S11). In parameter charts, derivatives through order \(r\) obey the corresponding estimate by (S10). Constants are local on the parameter space; no global spectral gap is asserted on a noncompact parameter set.

These results apply to \(C_{p(y)}\) when the coefficients of a fixed-degree monic polynomial vary \(C^r\) and (S9) holds. Collisions among roots in one half-plane do not damage the stable bundle or these estimates.

Section 16.6 gives every ordered multiindex derivative with its full multiplicity and the original contour length, spectral-gap and resolvent constants.

## 5. Collapsing rates within their half-planes

Let \(q=q_A\), let \(\lambda>0\), and let \(0\leq\tau\leq1\). Put

\[
A_\tau=(1-\tau)A+i\tau\lambda(2q-I).                      \tag{S12}
\]

**Theorem.** Each \(A_\tau\) has no real eigenvalues, and its upper spectral projection is exactly \(q\). At \(\tau=1\), its solution with initial value \(v\) is

\[
e^{-\lambda t}qv+e^{\lambda t}(I-q)v.                     \tag{S13}
\]

**Proof.** On an original primary summand \(V_\zeta\), the restriction is

\[
\big((1-\tau)\zeta+i\tau\lambda\,
\operatorname{sgn}(\operatorname{Im}\zeta)\big)I
+(1-\tau)N_\zeta.
\]

Its only eigenvalue has the same strict imaginary-part sign as \(\zeta\), including at both endpoints. The fixed direct sum of all original upper summands is therefore the full upper primary subspace for every \(\tau\), and the lower sum is its complementary lower subspace. The spectral projection is uniquely the projection onto the first along the second, hence equals \(q\). Formula (S13) follows by exponentiating the restrictions \(i\lambda I\) and \(-i\lambda I\).

Distinct original eigenvalues can coalesce during this deformation, and at the last endpoint nilpotent parts vanish. Individual generalized eigenspaces labelled by *distinct moving eigenvalues* therefore need not stay individually identifiable. The two half-plane sums and their projection are what remain fixed. \(\square\)

For parameter-dependent \(A\) and positive \(\lambda\), (S12) has the same regularity as those data by Section 4. There is no additional requirement that \(\lambda\) avoid the original eigenvalues.

## 6. Polynomial coordinates adapted to two half-planes

Return to (S4), now with \(m>1\), and fix \(\lambda>0\). Write

\[
L(z)=z+i\lambda,\qquad R(z)=z-i\lambda.
\]

There are unique coefficients \(a_0,\ldots,a_m\in\operatorname{End}(E)\) with

\[
p(z)=\sum_{j=0}^m a_j R(z)^jL(z)^{m-j}.                   \tag{S14}
\]

For completeness, set \(w=R(z)/L(z)\), so \(z=i\lambda(1+w)/(1-w)\) and \(L(z)=2i\lambda/(1-w)\). Then the coefficients are those of the polynomial

\[
\sum_{j=0}^m a_jw^j
=\sum_{k=0}^m\frac{i^{k-m}}{2^m}\lambda^{k-m}
 p_k(1+w)^k(1-w)^{m-k}.                                  \tag{S15}
\]

This gives an explicit formula

\[
a_j=\sum_{k=0}^m c_{jk}p_k\lambda^{k-m},\qquad
c_{jk}=\frac{i^{k-m}}{2^m}
\sum_{r=0}^{j}(-1)^{j-r}
\binom{k}{r}\binom{m-k}{j-r},                             \tag{S16}
\]

with binomial coefficients outside their ordinary range interpreted as zero. The right side of (S15) has degree at most \(m\), proving existence. If a combination in (S14) vanishes, divide by \(L(z)^m\) for \(z\ne-i\lambda\); the polynomial \(\sum a_jw^j\) vanishes on infinitely many \(w\), so each coefficient vanishes. This proves uniqueness and invertibility of the change of basis. Comparing the coefficient of \(z^m\) gives

\[
\sum_{j=0}^m a_j=I.                                      \tag{S17}
\]

Neither \(a_0\) nor \(a_m\), nor any intermediate coefficient, is assumed invertible. The negative powers of \(\lambda\) in (S16) require \(\lambda>0\); there is no claim of uniformity as \(\lambda\downarrow0\).

## 7. First-order coordinates that respect decay

For a solution of \(p(D)u=0\), define

\[
v_j=R(D)^jL(D)^{m-1-j}u,\qquad 0\leq j<m.                \tag{S18}
\]

The polynomials \(R^jL^{m-1-j}\) form a basis of the scalar polynomials of degree at most \(m-1\), by the same argument as in Section 6. Thus (S18) is an invertible, constant, scalar-block change from the Cauchy state \((u,Du,\ldots,D^{m-1}u)\). There is no loss of a Cauchy coordinate.

The transformed equations are

\[
\begin{aligned}
&\sum_{j=0}^{m-1}a_jL(D)v_j+a_mR(D)v_{m-1}=0,\\
&L(D)v_j-R(D)v_{j-1}=0\quad(1\leq j<m).
\end{aligned}                                             \tag{S19}
\]

The second equations follow by commuting scalar polynomials in \(D\); the first is precisely (S14) applied to \(u\). We have only moved scalar differential factors past constant matrix coefficients, never exchanged two matrix coefficients.

These equations are exactly a first-order system, not merely consequences that define a larger space. One way to check the converse is to let \(T\) denote the invertible change in (S18). The leading matrix of the left side of (S19) has row zero
\((a_0,a_1,\ldots,a_{m-2},a_{m-1}+a_m)\), and lower rows have \(-I,I\) in adjacent columns. Its determinant is one by the factorization in the next result at \(\tau=1\). Call that leading matrix \(C\), and the constant matrix \(K\). Every jet initial value yields a transformed solution, so
\((CTC_p+KT)x=0\) for every initial vector \(x\). Hence \(CD+K=CT(D-C_p)T^{-1}\). Invertibility of \(C,T\) proves the converse.

This change of state is an exact first-order reduction. The next construction has a different purpose: it produces a homotopy of fixed-degree polynomial systems beginning with the original equation plus auxiliary equations. Choosing \(L(D)^m\) for those auxiliary equations places their characteristic root at \(-i\lambda\), where they have no stable solutions. Auxiliary equations \(D^m v=0\) would instead introduce the real root zero.

## 8. An explicit stabilization and its leading coefficient

For \(0\leq\tau\leq1\), define the degree-\(m\) polynomial \(P_\tau(z)\in\operatorname{End}(E^m)[z]\) by its action on \(U=(U_0,\ldots,U_{m-1})\). The first component is

\[
\begin{aligned}
(P_\tau(z)U)_0={}&
\big((1-\tau^m)p(z)+\tau^m a_0L(z)^m\big)U_0\\
&+\sum_{j=1}^{m-2}\tau^{m-j}a_jL(z)^mU_j\\
&+\tau\big(a_{m-1}L(z)^m+a_mR(z)L(z)^{m-1}\big)U_{m-1},
\end{aligned}                                             \tag{S20}
\]

and the remaining components are

\[
(P_\tau(z)U)_j=L(z)^mU_j-
\tau R(z)L(z)^{m-1}U_{j-1}\quad(1\leq j<m).               \tag{S21}
\]

For \(m=2\), the sum in the middle line of (S20) is empty; the last block appears only once. At the endpoints,

\[
P_0(z)=\operatorname{diag}(p(z),L(z)^mI,\ldots,L(z)^mI),    \tag{S22}
\]

and every entry of \(P_1(z)\) contains \(L(z)^{m-1}\). After that scalar factor is removed, its equations are (S19).

Let \(C_\tau\) be the coefficient of \(z^m\) in \(P_\tau\). Define \(S:E^m\to E^m\) by \((SU)_0=0\), \((SU)_j=U_{j-1}\), and let \(H_\tau\) have identity diagonal, zero off-diagonal entries except in its first row, and

\[
(H_\tau)_{0j}=h_j
=\tau^{m-j}\sum_{k=j}^m a_k\quad(1\leq j<m).
\]

Then

\[
C_\tau=H_\tau(I-\tau S).                                 \tag{S23}
\]

To verify this, its first block is \(I-\tau h_1=I-\tau^m\sum_{k=1}^ma_k=(1-\tau^m)I+\tau^ma_0\). Its intermediate first-row blocks are \(h_j-\tau h_{j+1}=\tau^{m-j}a_j\), and its last block is \(h_{m-1}=\tau(a_{m-1}+a_m)\). The lower rows are exactly \(-\tau I,I\). These are the leading blocks of (S20)–(S21).

Both factors in (S23) are block triangular with identity diagonal. Therefore

\[
\det C_\tau=1.                                            \tag{S24}
\]

Moreover, \(H_\tau=I+N_\tau\) with \(N_\tau^2=0\), while \(S^m=0\). Its inverse is the explicit finite expression

\[
C_\tau^{-1}
=\left(\sum_{r=0}^{m-1}\tau^rS^r\right)(I-N_\tau).          \tag{S25}
\]

In block form, \((C_\tau^{-1})_{i0}=\tau^iI\), and for \(j\geq1\),

\[
(C_\tau^{-1})_{ij}
=\begin{cases}
\tau^{i-j}I-\tau^i h_j,&i\geq j,\\
-\tau^i h_j,&i<j,
\end{cases}
\qquad 0\leq i<m.                                        \tag{S26}
\]

Every entry has degree at most one in the \(a_k\); using (S17) to replace \(I\) makes it a linear combination of them. No product of two \(a_k\)'s occurs. The factorization uses only addition, composition with scalar multiples of identity, and the relation (S17). Consequently the inverse calculation also works for coefficients in any unital, possibly noncommutative, algebra satisfying that relation. Only the determinant statement is restricted here to finite-dimensional matrices.

## 9. A determinant identity retaining every root

For every complex \(z\) and every \(0\leq\tau\leq1\),

\[
\det P_\tau(z)=\det p(z)\,L(z)^{m(m-1)N}.                 \tag{S27}
\]

**Proof.** First suppose \(L(z)\ne0\). The block of rows and columns indexed \(1,\ldots,m-1\) is lower triangular with diagonal \(L(z)^m I\), and therefore has determinant \(L(z)^{m(m-1)N}\). Eliminating these rows expresses the auxiliary components as

\[
U_j=\left(\tau\frac{R(z)}{L(z)}\right)^jU_0.
\]

The Schur complement in the first row is

\[
(1-\tau^m)p(z)
+\tau^m\sum_{j=0}^ma_jR(z)^jL(z)^{m-j}=p(z).
\]

The block determinant formula proves (S27) whenever \(L(z)\ne0\). Both sides are polynomials in \(z\), so equality on that set proves equality also at \(z=-i\lambda\). The calculation never assumes invertibility of \(p(z)\). \(\square\)

If (S9) holds, (S27) proves that \(P_\tau\) is invertible at every real \(z\). It also records multiplicity: the upper-half-plane roots, with algebraic multiplicity, are exactly those of \(\det p\); the auxiliary factor adds only the lower root \(-i\lambda\), with multiplicity \(m(m-1)N\). If this is already a root of \(\det p\), multiplicities add. At \(\tau=1\), writing \(P_1=L^{m-1}F\), where \(F\) is the first-order polynomial of (S19), gives \(\det F=\det p\). A zero of the auxiliary factor is not discarded from the full equation.

## 10. The stable space is preserved, with an explicit inverse

Assume (S9), and write \(\mathcal M^+_\tau=\mathcal M^+(P_\tau)\), with the definition extended to invertible leading coefficient by left normalization.

**Theorem.** For every \(0\leq\tau\leq1\),

\[
\Pi_\tau:\mathcal M^+_\tau\longrightarrow\mathcal M^+(p),
\qquad U\longmapsto U_0                                  \tag{S28}
\]

is a linear isomorphism. On these spaces,

\[
L(D)U_j=\tau R(D)U_{j-1},\qquad
L(D)^jU_j=\tau^jR(D)^jU_0.                               \tag{S29}
\]

**Proof.** The leading coefficient is invertible by (S24), and the determinant has no real zeros by (S27). Section 3 therefore applies to \(P_\tau\): every stable solution and all its derivatives decay exponentially.

Equation (S21) says
\(L(D)^{m-1}(L(D)U_j-\tau R(D)U_{j-1})=0\).
The expression in parentheses is bounded. The kernel of \(L(D)^k\), for \(k\geq1\), consists exactly of \(e^{\lambda t}\) times vector polynomials of degree less than \(k\): substitute \(f=e^{\lambda t}g\) and use \(L(D)f=-ie^{\lambda t}g'\). No nonzero such function is bounded for \(t\geq0\). Cancellation is therefore valid on this bounded solution space, giving the first recurrence in (S29). Iteration gives the second one.

For \(j<m\), multiply the second identity by \(L(D)^{m-j}\). In the last term of (S20), use \(R(D)L(D)^{m-1}U_{m-1}=\tau^{m-1}R(D)^mU_0\). The first row of the differential equation becomes

\[
(1-\tau^m)p(D)U_0+
\tau^m\sum_{j=0}^ma_jR(D)^jL(D)^{m-j}U_0=p(D)U_0=0.
\]

Thus \(\Pi_\tau\) has the asserted codomain.

To construct the inverse, first observe that for a smooth exponentially decreasing function \(g\), whose derivatives have the same property, the unique bounded solution of \(L(D)f=g\) is

\[
(T_\lambda g)(t)
=-i\int_0^\infty e^{-\lambda s}g(t+s)\,ds.                \tag{S30}
\]

Differentiating the integral or integrating once by parts gives
\(f'-\lambda f=ig\), which is equivalent to \(L(D)f=g\). The difference of any two bounded solutions is \(ce^{\lambda t}\), so is zero. Differentiation under the integral is justified by the exponential derivative bounds. If \(\|D^kg(t)\|\leq M_ke^{-\delta t}\), then

\[
\|D^kT_\lambda g(t)\|\leq
\frac{M_k}{\lambda+\delta}e^{-\delta t}
\quad(t\geq0).                                          \tag{S31}
\]

Every \(u\in\mathcal M^+(p)\) has these bounds by Section 3. Define

\[
U_0=u,\qquad U_j=\tau T_\lambda R(D)U_{j-1}\ (1\leq j<m). \tag{S32}
\]

These functions are defined on all real \(t\); for fixed \(t\), the integration tail still lies in the decaying region. They and all their derivatives decay on the positive half-line, satisfy (S29), and hence satisfy every lower row of \(P_\tau(D)U=0\). Substituting the recurrences into the first row gives \(p(D)u=0\), as above. This proves surjectivity. If \(U_0=0\), each successive bounded solution of \(L(D)U_j=\tau R(D)U_{j-1}\) is zero by uniqueness, proving injectivity. \(\square\)

Since \(T_\lambda\) commutes with scalar constant-coefficient differentiation on these functions, the lift can also be written

\[
U_j=\tau^j(T_\lambda R(D))^ju.
\]

At \(\tau=0\), this is exactly \((u,0,\ldots,0)\); no division by \(\tau\) is needed. The same estimates show local \(C^r\) dependence of the lift on \(C^r\) coefficients and on \(\lambda>0\). In Cauchy coordinates this is an isomorphism of the stable bundles from Section 4. On compact parameter sets, differentiation of (S30) in \(\lambda\) introduces powers of \(s\), whose integrals remain finite because \(\lambda\) has a positive lower bound and the stable decay estimates are uniform.

## 11. Boundary measurements, their orders, and the zero endpoint

For \(1\leq\ell\leq J\), let \(G_\ell\) be a finite-dimensional complex vector space and

\[
B_\ell(z)=\sum_{r=0}^{d_\ell}b_{\ell r}z^r,
\qquad b_{\ell r}\in\operatorname{Hom}(E,G_\ell),
\qquad d_\ell\geq0.
\]

The boundary map is

\[
\mathcal B:\mathcal M^+(p)\longrightarrow
G:=\bigoplus_{\ell=1}^J G_\ell,
\qquad
u\longmapsto\big(B_\ell(D)u(0)\big)_\ell.                 \tag{S33}
\]

The empty family is allowed, with target zero. We call these measurements *complementing* precisely when (S33) is bijective. In particular its domain and target dimensions must agree; injectivity alone does not establish complementing data with arbitrary targets.

For any finite orders \(d_\ell\), composition with (S28) gives

\[
\mathcal B_\tau(U)=\big(B_\ell(D)U_0(0)\big)_\ell,
\qquad \mathcal B_\tau=\mathcal B\Pi_\tau.                 \tag{S34}
\]

Since \(\Pi_\tau\) is an isomorphism, \(\mathcal B_\tau\) is bijective if and only if \(\mathcal B\) is. This statement includes both \(\tau=0\) and \(\tau=1\), and does not require \(d_\ell<m\).

The preserved data form the commuting square

\[
\begin{array}{ccc}
\mathcal M^+_\tau&\xrightarrow{\mathcal B_\tau}&G\\
\Pi_\tau\downarrow&&\downarrow I_G\\
\mathcal M^+(p)&\xrightarrow{\mathcal B}&G.
\end{array}
\]

The left vertical arrow is invertible; the bottom measurement map is invertible exactly when the top one is. This diagram concerns solution spaces, so it does not extend an expression with singular coefficients to arbitrary Cauchy vectors.

For the following alternative expression, impose the additional hypothesis \(d_\ell<m\). There are unique coefficients \(\beta_{\ell k}\in\operatorname{Hom}(E,G_\ell)\) such that

\[
B_\ell(z)=\sum_{k=0}^{m-1}
\beta_{\ell k}R(z)^kL(z)^{m-1-k}.                         \tag{S35}
\]

Repeating the change of variables with degree \(m-1\) gives

\[
\sum_{k=0}^{m-1}\beta_{\ell k}w^k
=\sum_{r=0}^{d_\ell}
\frac{i^{r+1-m}}{2^{m-1}}\lambda^{r+1-m}
b_{\ell r}(1+w)^r(1-w)^{m-1-r}.                          \tag{S36}
\]

Thus \(\beta_{\ell k}=\sum_{r=0}^{d_\ell}c'_{kr}b_{\ell r}\lambda^{r+1-m}\), where

\[
c'_{kr}=\frac{i^{r+1-m}}{2^{m-1}}
\sum_{a=0}^k(-1)^{k-a}
\binom{r}{a}\binom{m-1-r}{k-a}.
\]

The degrees and powers of \(\lambda\) follow from (S36), including when the actual order is less than \(m-1\). From (S29),

\[
L(D)^{m-1}U_k
=\tau^kR(D)^kL(D)^{m-1-k}U_0.
\]

Consequently for \(0<\tau\leq1\) and \(U\in\mathcal M^+_\tau\),

\[
B_\ell(D)U_0
=\sum_{k=0}^{m-1}\tau^{-k}\beta_{\ell k}
L(D)^{m-1}U_k.                                          \tag{S37}
\]

This is equality of functions of \(t\), so it remains true at the boundary after evaluation at zero. The factors \(\tau^{-k}\) make (S37) unsuitable as a formula for an ambient boundary operator at \(\tau=0\). The correct endpoint map is (S34). On the explicitly lifted stable vectors (S32), the factors cancel with \(\tau^k\), but this cancellation does not define \(\tau^{-k}\) on arbitrary vectors at zero.

Here the orders are orders in the single normal variable. In a boundary PDE, tangential orders and their Sobolev shifts are additional data. None of the finite-dimensional statements permits dropping them or replacing an arbitrary boundary system by Dirichlet data.

## 12. The reduction with its leading coefficient retained

Combine the preceding statements under exactly these assumptions: \(E\) is finite-dimensional over \(\mathbb C\); \(m>1\); \(p\) has degree \(m\) and leading coefficient \(I\); \(\det p(\xi)\ne0\) for every real \(\xi\); \(\lambda>0\); and \(0\leq\tau\leq1\).

The family \(P_\tau\) in (S20)–(S21) begins with the stabilized equation (S22), has no real characteristic roots, preserves the full stable solution space by first-coordinate projection, and preserves bijectivity of every finite collection of boundary measurements transported by that projection. Its leading coefficient has determinant one and inverse entries linear in \(a_0,\ldots,a_m\). The extra boundary expression (S37) requires orders less than \(m\) and \(\tau>0\).

Define

\[
\widehat P_\tau(z)=C_\tau^{-1}P_\tau(z).                  \tag{S38}
\]

It is monic of degree \(m\). Left multiplication by the invertible constant matrix changes neither the differential equation's solutions nor any of their boundary measurements. Because \(\det C_\tau=1\), it also leaves (S27) unchanged. At \(\tau=0\), (S23) gives \(C_0=I\), so the starting polynomial is unchanged. At \(\tau=1\),

\[
\widehat P_1(z)=L(z)^{m-1}(zI-A_*)                        \tag{S39}
\]

for a matrix \(A_*\) with no real eigenvalues: the first-order factor is monic and its determinant is \(\det p(z)\). Thus its stable equation can be further deformed by Section 5. The scalar factor in (S39) has only the lower root \(-i\lambda\); cancellation of that factor is valid for bounded solutions by Section 10, and is not an equality of full solution spaces.

The preceding construction begins with a monic polynomial because its Cauchy coordinates use the leading identity. For an original polynomial
\[
p(z)=p_m z^m+\sum_{j=0}^{m-1}p_jz^j,\qquad p_m\in\operatorname{GL}(E),
\]
retain \(p\) and every leading-coefficient factor. Set \(r(z)=p_m^{-1}p(z)\) only to calculate the monic comparison, and let \(P_\tau[r]\) and \(C_\tau[r]\) denote (S20)–(S23) formed from \(r\). The expression \(p_m^{-1}p\) is used only for this comparison; multiplication is on the left. The family attached to the original equation is
\
\mathcal P_\tau(z)
=\operatorname{diag}(p_m,I,\ldots,I)P_\tau[r.
\]
Its first row has the original left factor \(p_m\); the other rows are unchanged. In particular,
\[
\mathcal P_0(z)=\operatorname{diag}(p(z),L(z)^mI,\ldots,L(z)^mI),
\qquad
\det\mathcal P_\tau(z)=\det p(z)\,L(z)^{m(m-1)N}.
\]
The determinant identity follows without cancellation: \(\det r(z)=(\det p_m)^{-1}\det p(z)\), while left multiplication contributes \(\det p_m\). The leading matrix is
\[
\mathcal C_\tau
=\operatorname{diag}(p_m,I,\ldots,I)C_\tau[r],
\qquad
\det\mathcal C_\tau=\det p_m,\qquad
\mathcal C_\tau^{-1}
=C_\tau[r]^{-1}\operatorname{diag}(p_m^{-1},I,\ldots,I).
\]
These orders follow from matrix multiplication; no commutation of \(p_m\) with the other coefficients is used. Since the diagonal left factor is invertible, \(\mathcal P_\tau(D)U=0\) if and only if \(P_\taurU=0\), and \(p(D)u=0\) if and only if \(r(D)u=0\). Thus the first-coordinate stable isomorphism and every transported boundary measurement remain exact for the original equation. The monic comparison satisfies \(\mathcal C_\tau^{-1}\mathcal P_\tau=C_\tau[r]^{-1}P_\tau[r]\); it does not erase \(\det p_m\) from the original family. For singular \(p_m\), this comparison is unavailable and the full \(mN\)-dimensional Cauchy space can fail, as Problem 6 shows.

## 13. Example: cubic time factors in a four-dimensional stable space

Let \(E=\mathbb C^2\), let \(\kappa\ne0\), and consider

\[
p(z)=
\begin{pmatrix}(z-i)^2&\kappa\\0&(z-i)^2\end{pmatrix}.
\]

It is monic of degree two, and its determinant is \((z-i)^4\), so every solution is stable. To see all four coordinates directly, write

\[
u_2(t)=e^{-t}(a+bt),\qquad
u_1(t)=e^{-t}
\left(c+dt+\frac{\kappa a}{2}t^2+\frac{\kappa b}{6}t^3\right).
\]

Since \((D-i)(e^{-t}f)=-ie^{-t}f'\), substitution proves the equation. The free constants \(a,b,c,d\) give all four solutions by Cauchy uniqueness. Thus a second-order matrix equation can contain a cubic polynomial times an exponential; the order of the scalar equation alone does not bound the length of a generalized chain for the full state matrix. In agreement, the upper-right entry of \(p(z)^{-1}\) is \(-\kappa(z-i)^{-4}\).

The pair of measurements \(u(0)\in E\), \(Du(0)\in E\) is complementing because every Cauchy jet is stable. Under the construction with \(\lambda=2\), the stabilized system has determinant \((z-i)^4(z+2i)^4\). Its stable dimension remains four, while its total solution dimension is eight.

## 14. Example: noncommuting coefficients and an unsuitable trace

Consider

\[
p(z)=
\begin{pmatrix}(z-i)^2&1\\0&(z+2i)^2\end{pmatrix}.
\]

Its coefficients \(p_1=\operatorname{diag}(-2i,4i)\) and
\(p_0=\left(\begin{smallmatrix}-1&1\\0&-4\end{smallmatrix}\right)\)
do not commute: \(p_1p_0-p_0p_1\) has upper-right entry \(-6i\). The determinant is \((z-i)^2(z+2i)^2\). A bounded solution must have \(u_2=0\), since its second component solves \((D+2i)^2u_2=0\). Therefore

\[
u(t)=\big(e^{-t}(a+bt),0\big),\qquad a,b\in\mathbb C.
\]

The stable dimension is two. The ordinary vector trace \(u(0)\in\mathbb C^2\) has image \(\mathbb C\times\{0\}\) and a one-dimensional kernel, despite equality of source and target dimensions. In contrast, the two scalar measurements

\[
B_1(D)u(0)=u_1(0)=a,\qquad
B_2(D)u(0)=Du_1(0)=i(a-b)
\]

are bijective onto \(\mathbb C\oplus\mathbb C\). The entire construction above applies without changing the coefficient order or imposing a scalar boundary model.

## 15. Problems with solutions

**Problem 1: a real root at the boundary of the hypothesis.** Let
\(A_\varepsilon=\left(\begin{smallmatrix}i\varepsilon&1\\0&i\varepsilon\end{smallmatrix}\right)\), for real \(\varepsilon\). Determine the positive-half-line bounded initial values, including \(\varepsilon=0\). Explain the failure of a continuous stable projection across zero.

**Solution.** The solution is
\(e^{-\varepsilon t}(v_1+itv_2,v_2)\). For \(\varepsilon>0\), every initial vector is stable. For \(\varepsilon<0\), only zero is bounded. At zero, precisely vectors with \(v_2=0\) are bounded, and their solutions are constant. Thus the bounded dimensions are respectively two, zero, and one. The upper spectral projection is \(I\) for positive \(\varepsilon\) and zero for negative \(\varepsilon\), so cannot extend continuously across zero. At zero, boundedness does not imply decay, and the upper/lower splitting omits the real generalized eigenspace. This identifies why the no-real-spectrum hypothesis is used.

**Problem 2: the smallest block homotopy.** For \(m=2\), write \(P_\tau\), its leading coefficient, and an inverse of that coefficient. Verify the determinant-one assertion without commutativity assumptions.

**Solution.** With \(a_0+a_1+a_2=I\),

\[
P_\tau=
\begin{pmatrix}
(1-\tau^2)p+\tau^2a_0L^2&\tau(a_1L^2+a_2RL)\\
-\tau RL&L^2I
\end{pmatrix}.
\]

Writing \(b=\tau(a_1+a_2)\), its leading coefficient and inverse are

\[
C_\tau=
\begin{pmatrix}I-\tau b&b\\-\tau I&I\end{pmatrix}
=\begin{pmatrix}I&b\\0&I\end{pmatrix}
\begin{pmatrix}I&0\\-\tau I&I\end{pmatrix},
\qquad
C_\tau^{-1}=
\begin{pmatrix}I&-b\\\tau I&I-\tau b\end{pmatrix}.
\]

Multiplying the two displayed factors or multiplying \(C_\tau C_\tau^{-1}\) verifies the formulas; no two unrelated coefficient matrices are interchanged. Each triangular factor has determinant one. In addition, (S27) reads \(\det P_\tau=\det p\,L^{2N}\).

**Problem 3: boundary orders beyond the coordinate basis.** Let \(B(z)\in\operatorname{Hom}(E,G)[z]\) have arbitrary finite degree and let \(p\) be monic of degree \(m\). Prove a unique division formula \(B=Qp+R_B\) with \(\deg R_B<m\). Which factor order is required, and what does this imply on solutions?

**Solution.** If \(B\) has leading term \(bz^d\) with \(d\geq m\), subtract \(bz^{d-m}p(z)\). The leading term cancels because \(p_m=I\), and the degree decreases. Iterating constructs \(Q\in\operatorname{Hom}(E,G)[z]\) and \(R_B\) of degree below \(m\). If two decompositions exist, a nonzero difference \(Q_1-Q_2\) of degree \(s\) makes \((Q_1-Q_2)p\) have degree exactly \(s+m\), since its leading coefficient is unchanged by multiplication by \(I\). It cannot equal a polynomial of degree below \(m\); hence both differences vanish. The required order is \(Qp\), which composes \(E\xrightarrow{p}E\xrightarrow{Q}G\). On constant-coefficient solutions, \(B(D)u=R_B(D)u\). This justifies normal-order reduction for this algebraic model. A PDE with variable coefficients or tangential orders needs its own division and mapping argument.

**Problem 4: a negative power of the homotopy parameter.** Take \(m=2\), \(B(z)=z\), and any stable scalar solution \(u\). Find \(\beta_0,\beta_1\), verify (S37), and identify its valid zero-parameter interpretation.

**Solution.** Since \(z=\tfrac12(z+i\lambda)+\tfrac12(z-i\lambda)\), one has \(\beta_0=\beta_1=1/2\). For \(\tau>0\), the recurrence gives \(LU_1=\tau RU_0\), so
\(\tfrac12 LU_0+\tfrac1{2\tau}LU_1=\tfrac12(L+R)U_0=DU_0\).
At zero, the stable lift has \(U_1=0\); inserting this into \(\tau^{-1}LU_1\) is undefined. The correct boundary functional remains \(DU_0(0)\) from (S34). Along a lifted family, its limiting value can be computed before setting \(\tau=0\), using \(\tau^{-1}LU_1=RU_0\). It is not an ambient formula at zero.

**Problem 5: nilpotent coalescence at the last endpoint.** Let \(A\) be the direct sum of the blocks \(iI+N\) on \(\mathbb C^2\), \(2i\) on \(\mathbb C\), and \(-3i\) on \(\mathbb C\), where \(N=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)\). Describe (S12) when \(\lambda=1\).

**Solution.** The first block is \(iI+(1-\tau)N\), the next is \(i(2-\tau)\), and the last is \(-i(3-2\tau)\). The upper projection is always \(\operatorname{diag}(I_2,1,0)\). For \(\tau<1\), the first and second upper blocks have distinct eigenvalues; at one, their eigenvalues coalesce at \(i\) and the nilpotent part of the first vanishes. The full \(i\)-eigenspace at one has dimension three. Thus individual primary summands associated with distinct spectral values have merged, while the upper spectral subspace has remained the same three-dimensional space throughout.

**Problem 6: why the leading coefficient matters.** Treat \(r(z)=\operatorname{diag}(z,1)\) as a degree-one matrix polynomial on \(\mathbb C^2\). Determine the solutions and compare their dimension with the formal count \(m\dim E\).

**Solution.** The equations are \(Du_1=0\) and \(u_2=0\), so the solution space is one-dimensional, although \(m\dim E=2\). The leading coefficient is \(\operatorname{diag}(1,0)\), which is singular. Initial values are constrained, and multiplication by the inverse leading coefficient is impossible. In contrast, a genuinely monic degree-one polynomial supplies two free initial coordinates. This example concerns the leading-coefficient hypothesis; its determinant also has a real root, so it is not an example within the stable reduction theorem.

## 16. Full original factors in the spectral and Cauchy maps

We make explicit every scalar and matrix leading factor used by Sections 1--5 and 12. The original characteristic multiplicities, nilpotent orders, projection maps, Cauchy coordinates and contour conventions remain in the calculation. The bounded-mode classification at real roots and the complete original-leading-matrix numerator map are stated as additional results; they do not silently change the no-real-root assumptions of the earlier reduction.

The entry proof is [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md), Sections 2--4 and 9: original polynomial division and Bézout, full complex roots/factorization, original scalar units, determinant signs, kernel coordinates and both invariant quotient maps. We retain the finite basis and scalar-calculus entry definitions used there. Each argument below preserves the chosen original norm and actual coordinates; no Jordan decomposition or selected smooth eigenvalue branch is assumed.

### 16.1. The original annihilator and complete primary projection maps

Let \(V\) be the original finite-dimensional complex vector space, \(n=\dim V\), and \(A\in\operatorname{End}(V)\). Cayley--Hamilton in Section 4 of [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md) supplies a nonzero annihilator. Keep an original least-degree nonzero annihilator \(m\), with original leading coefficient \(c_m\ne0\). That lesson proves that \(m\) divides every annihilator. For \(n>0\), \(m\) is nonconstant, because a nonzero constant acts as that nonzero scalar times the nonzero identity. The full factorization proved there is
\[
\begin{gathered}
m(z)=c_m\prod_{\lambda\in Z(m)}h_\lambda(z),\quad
 h_\lambda(z)=(z-\lambda)^{\nu_\lambda},\quad
 \nu_\lambda\geq1,\quad\\
 H_\lambda(z)=\prod_{\mu\ne\lambda}h_\mu(z),\quad
 M_\lambda(z)=m(z)/h_\lambda(z)=c_mH_\lambda(z).
\end{gathered} \tag{SR1}
\]
Every original leading unit and root multiplicity is retained. A least-degree choice is unique up to its nonzero original scalar unit, by division in both directions. The named monic polynomial is exactly \(c_m^{-1}m\), as a comparison; it does not replace \(m\) in this calculation.

The coprime-factor proof in Section 3 of [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md) gives \(a_\lambda h_\lambda+b_\lambda H_\lambda=1\). In the original quotient calculation set \(\beta_\lambda=c_m^{-1}b_\lambda\). The full identities are
\[
 a_\lambda h_\lambda+\beta_\lambda M_\lambda=1,\qquad
 e_\lambda=\beta_\lambda M_\lambda
              =c_m^{-1}b_\lambda\,c_mH_\lambda,\qquad
 Q_\lambda=(c_m^{-1}b_\lambda)(A)(c_mH_\lambda)(A).
                                                               \tag{SR2}
\]
For the factor \(h_\lambda\), \(e_\lambda\) is one modulo that factor; for every other factor it is zero. Thus each of
\(\sum_\lambda e_\lambda-1\), \(e_\lambda^2-e_\lambda\), and
\(e_\lambda e_\mu\) for \(\lambda\ne\mu\) is divisible by every factor. The exact Bézout divisibility proof in Section 3 of [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md) makes it divisible by their full product \(H=c_m^{-1}m\). Its evaluation is zero because \(H(A)=c_m^{-1}m(A)=0\). Consequently
\[
 Q_\lambda^2=Q_\lambda,\quad Q_\lambda Q_\mu=0\ (\lambda\ne\mu),
 \quad\sum_\lambda Q_\lambda=I_V,\quad
 V=\bigoplus_\lambda W_\lambda,\quad
 W_\lambda=\operatorname{im}Q_\lambda
            =\ker(A-\lambda I)^{\nu_\lambda}.                  \tag{SR3}
\]
Here the image equality is an exact map: \(h_\lambda e_\lambda=\beta_\lambda m\) gives the first inclusion; \(1-e_\lambda=a_\lambda h_\lambda\) gives \(v=Q_\lambda v\) on the kernel. Applying \(Q_\mu\) to a zero sum proves directness. Each projection commutes with \(A\), since it is an evaluated scalar polynomial.

A different Bézout choice has the same factorwise remainders. Its difference from \(e_\lambda\) is a multiple of \(H=c_m^{-1}m\), whose full evaluation is zero. Thus it gives the same actual \(Q_\lambda\), not just the same abstract summand. Under an original coordinate change \(T\), polynomial evaluation gives
\(f(T^{-1}AT)=T^{-1}f(A)T\): expand every finite power and use the ordered adjacent products \(TT^{-1}=I\). Applied separately to both factors in (SR2), this gives
\[
 (c_m^{-1}b_\lambda)(T^{-1}AT)
 (c_mH_\lambda)(T^{-1}AT)=T^{-1}Q_\lambda T.                  \tag{SR4}
\]
This is the exact coordinate map for the full original projection.

If \(V=0\), a least-degree annihilator can be the original nonzero constant \(m=c_m\). Its root set is empty, and the empty projection sum is zero, exactly the identity of the zero vector space. The empty decomposition in (SR3) therefore includes that case without adding a root or assigning a multiplicity.

### 16.2. Actual nilpotent order and characteristic multiplicity

On \(W_\lambda\) define the original restricted operator
\(N_\lambda=A|_{W_\lambda}-\lambda I_{W_\lambda}\).
Equation (SR3) gives \(N_\lambda^{\nu_\lambda}=0\). In fact every \(W_\lambda\) is nonzero and this exponent is exact.

To prove both assertions without a Jordan assumption, suppose that
\(N_\lambda^{\nu_\lambda-1}=0\), also including an empty \(W_\lambda\). The original polynomial
\[
 m_\lambda(z)=m(z)/(z-\lambda)
       =c_m(z-\lambda)^{\nu_\lambda-1}
                    \prod_{\mu\ne\lambda}(z-\mu)^{\nu_\mu}
                                                               \tag{SR5}
\]
would annihilate \(W_\lambda\) by that supposed zero power. It annihilates every other \(W_\mu\) through the retained full factor \((A-\mu I)^{\nu_\mu}\). The direct sum (SR3) would then make it an annihilator of \(V\), with its original nonzero leading coefficient \(c_m\) and degree one less than \(m\). Minimality excludes this. Hence
\(N_\lambda^{\nu_\lambda-1}\ne0\); in particular \(W_\lambda\ne0\).

Choose an actual \(w\in W_\lambda\) for which
\(N_\lambda^{\nu_\lambda-1}w\ne0\). The original vectors
\(w,N_\lambda w,\ldots,N_\lambda^{\nu_\lambda-1}w\)
are independent. If their linear combination vanished, take its smallest index \(j\) with nonzero coefficient and apply
\(N_\lambda^{\nu_\lambda-1-j}\). The full higher terms vanish by the known zero power, leaving that nonzero coefficient times the unchanged nonzero vector
\(N_\lambda^{\nu_\lambda-1}w\), a contradiction. Thus
\[
             1\leq\nu_\lambda\leq d_\lambda,
                 \qquad d_\lambda=\dim W_\lambda.             \tag{SR6}
\]

For the full determinant calculation choose a basis by successively extending bases of
\(\ker N_\lambda^j\) for \(j=0,\ldots,\nu_\lambda\).
The actual map sends each such space into the preceding one. In that ordered basis its matrix is upper triangular with every diagonal entry zero; no vector or matrix entry is rescaled. For the full original change of basis \(T_\lambda\), the determinant identities proved there give
\[
 \det(zI_{W_\lambda}-A|_{W_\lambda})
   =\det(T_\lambda)(z-\lambda)^{d_\lambda}\det(T_\lambda^{-1}),
       \qquad \det(T_\lambda)\det(T_\lambda^{-1})=1.           \tag{SR7}
\]
Choose bases of the original direct summands and concatenate them, with full coordinate matrix \(T\). The original operator is block diagonal in those coordinates. Its full characteristic polynomial is therefore
\[
 \chi_A(z)=\det(T)\prod_\lambda
       \bigl[\det(T_\lambda)(z-\lambda)^{d_\lambda}
                         \det(T_\lambda^{-1})\bigr]\det(T^{-1}).
                                                               \tag{SR8}
\]
All determinant factors remain explicit and their inverse products are proved; the characteristic leading coefficient one was computed from the original permutation sums in the polynomial and contour lesson, rather than imposed on the original annihilator. Each root's characteristic multiplicity is exactly \(d_\lambda\), while the annihilator exponent is exactly \(\nu_\lambda\). The opposite determinant convention retains the full factor
\(\det(A-zI)=(-1)^n\chi_A(z)\).

An eigenvalue is a root of \(m\): if \(Av=\lambda v\), \(v\ne0\), then the original finite polynomial gives \(m(A)v=m(\lambda)v=0\). Conversely each \(W_\lambda\ne0\) has a nonzero vector in \(\ker N_\lambda\), for example \(N_\lambda^{\nu_\lambda-1}w\) above. Thus \(Z(m)\) is precisely the original spectrum. For \(n=0\), both spectra are empty and the actual characteristic determinant is the empty product one.

### 16.3. The original resolvent, pole orders and every unit factor

For \(z\notin Z(m)\), multiplication of the full finite geometric sum gives on the original summand
\[
 (zI-A)^{-1}|_{W_\lambda}
   =\sum_{k=0}^{\nu_\lambda-1}
                         \frac{N_\lambda^k}{(z-\lambda)^{k+1}}.
                                                               \tag{SR9}
\]
Indeed multiplication by \((z-\lambda)I-N_\lambda\) produces the identity minus
\(N_\lambda^{\nu_\lambda}/(z-\lambda)^{\nu_\lambda}\), and that full terminal term is zero by (SR3). The product in the opposite order is the same since every factor is a power of the same original restricted operator. Using (SR2)--(SR3), the full global operator formula is
\[
 (zI-A)^{-1}
 =\sum_\lambda\sum_{k=0}^{\nu_\lambda-1}
  \frac{(A-\lambda I)^k
        (c_m^{-1}b_\lambda)(A)(c_mH_\lambda)(A)}
       {(z-\lambda)^{k+1}}.                                  \tag{SR10}
\]
Every actual scalar-unit and projection factor is present. Acting on each original summand proves both inverse identities for this original matrix; no leading coefficient has been dropped from the receiving map.

Multiplying (SR10) by the full power \((z-\lambda)^{\nu_\lambda}\) and taking \(z\to\lambda\) gives
\[
 \lim_{z\to\lambda}(z-\lambda)^{\nu_\lambda}(zI-A)^{-1}
       =(A-\lambda I)^{\nu_\lambda-1}
              (c_m^{-1}b_\lambda)(A)(c_mH_\lambda)(A)\ne0.     \tag{SR11}
\]
All terms with a smaller pole power at \(\lambda\) tend to zero; every term at a distinct root has a bounded nonzero denominator near \(\lambda\) and also tends to zero after that multiplication. The nonzero conclusion follows by applying the right side to the unchanged \(w\) from Section 16.2. Hence the resolvent's pole order is exactly \(\nu_\lambda\), which need not equal the characteristic multiplicity \(d_\lambda\). This is an exact nonzero coefficient and limit, not merely a distinction between two names.

For example, in the original three coordinates let
\[
 A=\begin{pmatrix}\lambda&1&0\\0&\lambda&0\\0&0&\lambda\end{pmatrix},
 \quad
 (zI-A)^{-1}=
 \begin{pmatrix}
 (z-\lambda)^{-1}&(z-\lambda)^{-2}&0\\
 0&(z-\lambda)^{-1}&0\\0&0&(z-\lambda)^{-1}
 \end{pmatrix}.                                               \tag{SR12}
\]
Direct multiplication gives both inverse identities and all displayed zeros. The full determinant is \((z-\lambda)^3\). An original least-degree annihilator is \(c_m(z-\lambda)^2\), for any original \(c_m\ne0\): the actual nilpotent part has square zero and is nonzero. A nonzero degree-zero annihilator is impossible; a degree-one annihilator would have to vanish on all diagonal entries, leaving its nonzero leading coefficient in the actual upper-right entry, also impossible. Thus the characteristic multiplicity is three and the exact annihilator/resolvent order is two.

### 16.4. Original contour and exponential receivers at every order

Let \(\Gamma\) be a finite integer linear combination of the original piecewise \(C^1\) closed paths, avoiding every root. Keep
\[
 \operatorname{ind}_\Gamma(\lambda)
       =\frac{1}{2\pi i}\int_\Gamma\frac{dz}{z-\lambda}.        \tag{SR13}
\]
For a numerator \(\phi\) having its asserted globally convergent power series about each of these finitely many roots, the proved entire-series moment formula of [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md) gives the full receiving identity
\[
 \frac{1}{2\pi i}\int_\Gamma\phi(z)(zI-A)^{-1}\,dz
 =\sum_\lambda\operatorname{ind}_\Gamma(\lambda)
    \sum_{k=0}^{\nu_\lambda-1}\frac{\phi^{(k)}(\lambda)}{k!}
        (A-\lambda I)^k
        (c_m^{-1}b_\lambda)(A)(c_mH_\lambda)(A).               \tag{SR14}
\]
This follows by integrating the actual finite sum (SR10). No sum/interchange beyond the proved scalar moments is needed. Every factorial, root repetition, nilpotent power, contour index and original projection factor remains. The stated entire-series hypothesis includes constants, polynomials and exponentials. No formula for an arbitrary holomorphic numerator on an arbitrary domain is inferred here.

For \(\phi=1\), all higher derivatives vanish exactly; a contour with index one at precisely the selected roots and zero at the others therefore gives the sum of their actual \(Q_\lambda\). For \(\phi(z)=e^{itz}\), the original derivative is
\(\phi^{(k)}(\lambda)=(it)^k e^{it\lambda}\), so (SR14) retains all powers of \(i,t\) and every factorial.

The corresponding exponential equality is obtained directly from the original operator series, without a contour assumption:
\[
 E_A(t)=\sum_{r=0}^{\infty}\frac{(itA)^r}{r!}
       =\sum_\lambda e^{it\lambda}
          \sum_{k=0}^{\nu_\lambda-1}\frac{(it)^k}{k!}
            (A-\lambda I)^k
            (c_m^{-1}b_\lambda)(A)(c_mH_\lambda)(A).          \tag{SR15}
\]
On each original \(W_\lambda\), the two operators \(\lambda I\) and \(N_\lambda\) commute. Expand every finite binomial power of their sum. The scalar exponential majorants give absolute convergence on each compact time interval, including the differentiated series, so regrouping by the finitely many surviving powers \(k<\nu_\lambda\) is valid. The full factorial relation
\(\binom{r}{k}/r!=1/(k!(r-k)!)\) gives the two series product. All higher nilpotent terms are the proved zero operators, not omitted nonzero contributions. Acting on the full direct sum proves (SR15).

Termwise differentiation of the actual series gives \(D_tE_A=AE_A\), where \(D_t=-i\partial_t\), and repeated differentiation gives \(D_t^jE_A=A^jE_A\). The original addition identity gives \(E_A(-t)E_A(t)=I\). Thus every solution of \(D_tu=Au\) is \(u(t)=E_A(t)v\), because differentiating the full product \(E_A(-t)u(t)\) gives zero. Initial evaluation \(u\mapsto u(0)\) and \(v\mapsto E_A(t)v\) are inverse linear maps; these are the actual Cauchy maps used in the source.

### 16.5. Complete bounded-mode classification, including the real roots

First every linear map is bounded for the original chosen norm. Choose an actual basis \(v_1,\ldots,v_n\), retaining these vectors. If \(v=\sum x_jv_j\), triangle inequality and Cauchy--Schwarz give
\(\|v\|\leq B|x|_2\), with the full constant
\(B=(\sum_j\|v_j\|^2)^{1/2}\).
On the coordinate unit sphere the actual function
\(x\mapsto\|\sum_jx_jv_j\|\) is continuous by that inequality, and is everywhere positive by independence. Coordinate compactness supplies its actual minimum \(b>0\). Homogeneity then gives
\(b|x|_2\leq\|v\|\).
For any original linear map \(T\), this proves
\[
 \|Tv\|\leq
     \frac{(\sum_j\|Tv_j\|^2)^{1/2}}{b}\,\|v\|.               \tag{SR16}
\]
Every original basis vector and both comparison constants are retained. These are comparison maps, not replacements of the original norm. In particular all projections and coordinate functionals used below are bounded. The zero-dimensional case requires no positive sphere minimum and every map is the zero map.

On \(W_\lambda\), (SR15) gives for an actual \(v\)
\[
 \|E_A(t)v\|\leq e^{-t\,\operatorname{Im}\lambda}
        \sum_{k=0}^{\nu_\lambda-1}
                    \frac{|t|^k}{k!}\|N_\lambda^kv\|.         \tag{SR17}
\]
For \(\operatorname{Im}\lambda>0\) every full term tends to zero as \(t\to+\infty\). To prove the elementary exponential domination, choose any
\(0<a<\operatorname{Im}\lambda\). The scalar series gives
\(e^{at}\geq (at)^{k+1}/(k+1)!\) for \(t>0\), so
\(t^ke^{-at}\leq(k+1)!/(a^{k+1}t)\).
The remaining factor \(e^{-(\operatorname{Im}\lambda-a)t}\) is bounded and tends to zero. Every derivative is covered by the same actual finite expansion with the additional fixed factor \(A^j\).

Conversely take \(v\ne0\) and the largest \(j\) for which \(N_\lambda^jv\ne0\). It exists and lies between zero and \(\nu_\lambda-1\). Some actual coordinate functional \(\ell\) has
\(\ell(N_\lambda^jv)\ne0\); boundedness was proved in (SR16), without changing \(v\) or \(\ell\). The complete scalar polynomial in
\[
 \ell(E_A(t)v)=e^{it\lambda}
       \sum_{k=0}^j\frac{i^kt^k}{k!}\ell(N_\lambda^kv)         \tag{SR18}
\]
has nonzero leading coefficient
\(i^j\ell(N_\lambda^jv)/j!\).
For \(t\geq1\), the full reverse triangle inequality bounds its modulus below by
\[
 \frac{|\ell(N_\lambda^jv)|}{j!}t^j
  -\sum_{k=0}^{j-1}\frac{|\ell(N_\lambda^kv)|}{k!}t^k.
                                                               \tag{SR19}
\]
If \(j\geq1\), the lower sum is at most \(t^{j-1}\) times its full coefficient sum. Taking \(t\) at least twice that coefficient sum divided by the actual nonzero leading modulus makes (SR19) at least half the full leading term. If \(j=0\), the lower sum is empty and the modulus is its exact nonzero constant.

It follows that when \(\operatorname{Im}\lambda<0\), every nonzero \(v\) gives an unbounded solution on the positive half-line, since its scalar lower bound contains
\(e^{-t\operatorname{Im}\lambda}\).
When \(\operatorname{Im}\lambda=0\), it is bounded exactly when \(j=0\), equivalently \(N_\lambda v=0\); then the solution is exactly \(e^{it\lambda}v\). On a general \(v\), applying the bounded actual projection \(Q_\lambda\) to a bounded solution isolates each such component; components cannot conceal one another's growth. Thus the complete positive-half-line bounded initial space is
\[
 B_A^+=\bigoplus_{\operatorname{Im}\lambda>0}W_\lambda
       \ \oplus\
       \bigoplus_{\operatorname{Im}\lambda=0}
                         \ker(A-\lambda I).                  \tag{SR20}
\]
With \(t=-s\), \(s\geq0\), the same full expansions and inequalities reverse the imaginary-part signs, giving
\[
 B_A^-=\bigoplus_{\operatorname{Im}\lambda<0}W_\lambda
       \ \oplus\
       \bigoplus_{\operatorname{Im}\lambda=0}
                         \ker(A-\lambda I).                  \tag{SR21}
\]
These formulas prove the precise additional real-root modes rather than simply discarding the no-real-root hypothesis. Under the original no-real-spectrum assumption in Section 3 the extra sums are empty, so its actual upper projection gives \(B_A^+=q_AV\), its lower projection gives \(B_A^-=(I-q_A)V\), and every such solution and derivative decays in its own half-line. The original stable dimension counts \(d_\lambda\) in the upper half-plane, by (SR8), whereas time-polynomial degree is bounded by \(\nu_\lambda-1\). Neither count can be substituted for the other.

### 16.6. Full ordered parameter derivatives and common contour bounds

For an original \(C^r\) family \(A(y)\), near a fixed parameter a compact contour avoiding its spectrum stays disjoint from nearby spectra. Indeed the original determinant is continuous on the compact contour, has a strictly positive modulus minimum there, and small changes of its full finitely many coefficients preserve half that minimum. Inversion is continuous through its full cofactor matrix divided by that nonzero determinant. Differentiating
\((zI-A)R=I\) and multiplying by the actual inverse gives
\(\partial_jR=R(\partial_jA)R\), with this exact product order.

For a nonzero multiindex \(\alpha\), \(|\alpha|\leq r\), the full formula is
\[
 \partial^\alpha R
 =\sum_{k=1}^{|\alpha|}
   \ \sum_{\substack{\alpha^1+\cdots+\alpha^k=\alpha\\
                     |\alpha^1|,\ldots,|\alpha^k|>0}}
    \frac{\alpha!}{\alpha^1!\cdots\alpha^k!}
    R(\partial^{\alpha^1}A)R\cdots
                      (\partial^{\alpha^k}A)R.               \tag{SR22}
\]
Here every inner list is ordered; matrices are never commuted. One direct proof retains the actual Neumann series
\(R(y+h)=\sum_{k\geq0}(R(y)(A(y+h)-A(y)))^kR(y)\)
for the original difference small enough that its operator product norm is less than one. Its finite Taylor coefficient at \(h^\alpha\) is the sum over ordered nonzero lists in (SR22); each coefficient is divided by
\(\alpha^1!\cdots\alpha^k!\), and differentiation multiplies it by the full \(\alpha!\). Terms with more than \(|\alpha|\) differences have no such coefficient. The remainder bounds in the finite Taylor theorem and the geometric-series tail make the coefficient passage valid through order \(r\). Equivalently, labeling each of the \(|\alpha|\) successive derivative applications partitions the labels into ordered nonempty batches; their multinomial counts are precisely the displayed coefficients. Both constructions include every repeated derivative and every original factor.

For a compact parameter set with no real spectrum, the original norm has a common bound \(M\) for \(A(y)\), and every eigenvalue satisfies \(|\lambda|\leq M\) by the original eigenvector inequality in Section 9.8 of [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md). A hypothetical sequence of spectral points whose imaginary parts tend to zero has a convergent parameter subsequence and a bounded complex-point subsequence. Continuity of the original full determinant would give a real eigenvalue at the limit, contradicting the original hypothesis. Thus there is an actual gap \(g>0\).

Choose an original positive rectangle enclosing all upper roots, with lower height
\(0<\gamma<g\), upper height greater than \(M\), and left/right coordinates beyond \(-M,M\). Its orientation and all its edges are retained; the proven rectangle index is one at every upper root and zero at every lower root. Let \(L_\Gamma\) be its full length and let
\(C_R=\sup_{y,z\in K\times\Gamma}\|R(y,z)\|\).
This is finite by the original determinant/cofactor continuity and compactness. The original contour formula therefore gives
\[
 \|D_t^jE_{A(y)}(t)q_{A(y)}\|
 \leq \frac{L_\Gamma}{2\pi}
       \bigl(\sup_{z\in\Gamma}|z|^j\bigr) C_R e^{-\gamma t},
                     \qquad t\geq0.                          \tag{SR23}
\]
The full \(1/(2\pi i)\) contour factor yields \(1/(2\pi)\) in the norm bound, and \(D_t^j e^{itz}=z^j e^{itz}\) retains the original differential convention.

For each parameter derivative in a fixed original chart, insert every term of (SR22) into the same contour. Its original operator norm is bounded by
\[
 \frac{L_\Gamma}{2\pi}\sup_\Gamma|z|^j\, e^{-\gamma t}
 \sum_{k=1}^{|\alpha|}
 \ \sum_{\substack{\alpha^1+\cdots+\alpha^k=\alpha\\
                   |\alpha^\ell|>0}}
   \frac{\alpha!}{\alpha^1!\cdots\alpha^k!}
   C_R^{\,k+1}\prod_{\ell=1}^k
          \sup_{y\in K}\|\partial^{\alpha^\ell}A(y)\|.          \tag{SR24}
\]
For \(\alpha=0\) the actual bound is (SR23). The finite derivative bounds hold in each chart on the compact set under consideration. This proves the full regularity and uniform decay statements in Section 4 even when roots collide in one half-plane; no selection of individual smooth roots was used. It makes no global gap claim on a noncompact parameter set.

### 16.7. Original matrix-polynomial Cauchy and numerator maps

In this section \(m\) has the original meaning in Section 2 as matrix-polynomial order. Keep
\(p(z)=p_m z^m+\sum_{j=0}^{m-1}p_jz^j\), with \(m\geq1\),
\(p_m\in\operatorname{GL}(E)\), and all original matrix coefficients in their original order. If \(E=0\), all state spaces and solution spaces are zero and every determinant is the empty product one. Otherwise let \(N=\dim E>0\). The actual original-equation companion and jet maps are
\[
 C(x_0,\ldots,x_{m-1})
  =(x_1,\ldots,x_{m-1},-\sum_{j=0}^{m-1}p_m^{-1}p_jx_j),
 \qquad Ju=(u,Du,\ldots,D^{m-1}u).                            \tag{SR25}
\]
The original equation implies \(D(Ju)=CJu\) through its last row after multiplying on the left by the displayed \(p_m^{-1}\). Conversely the first \(m-1\) rows give every jet coordinate from the first, and multiplying the full last row by the original \(p_m\) gives exactly
\(p_mD^mu+\sum_{j=0}^{m-1}p_jD^ju=0\).
Both implications retain every left factor and do not commute any coefficients. Therefore the actual map \(u\mapsto Ju(0)\) is inverse to
\(x\mapsto \pi_0 E_C(t)x\), by the already proved first-order uniqueness; the original solution dimension is \(mN\).

For a direct characteristic calculation make the original triangular coordinate change
\(x_0=y_0,\ x_j=zx_{j-1}+y_j\), \(1\leq j<m\), on the state coordinates. Its original block diagonal is all identities, so its determinant is one. The first \(m-1\) output rows of \((zI-C)x\) are
\(-y_1,\ldots,-y_{m-1}\). The coefficient of \(y_0\) in the last row is exactly \(p_m^{-1}p(z)\), with this order. Move that last block row to the front: its full sign is
\((-1)^{N^2(m-1)}\). Each remaining negative identity gives the total factor
\((-1)^{N(m-1)}\). Eliminate every other entry of the first row by those identity rows, retaining the original determinant under each row addition. Thus
\[
 \det(zI_{E^m}-C)
   =(-1)^{N^2(m-1)}(-1)^{N(m-1)}
           \det(p_m^{-1}p(z))
   =(-1)^{N^2(m-1)}(-1)^{N(m-1)}
           \det(p_m^{-1})\det p(z).                           \tag{SR26}
\]
Both signs are retained and their product is one because their full exponent is
\(N(N+1)(m-1)\), an even integer. Also
\(\det(p_m^{-1})\det p_m=1\) by the original determinant multiplication proof. Hence the nonzero original prefactor preserves every root and multiplicity through an explicit scalar-unit map. It is not a replacement of the original determinant. All formulas include \(m=1\), where the negative block list and row permutation are empty.

The full original polynomial numerator of an arbitrary actual state is
\[
 \mathcal U_x^p(z)
     =\sum_{0\leq k\leq j<m}p_{j+1}x_{j-k}z^k,\qquad
 \mathcal U_x^p(z)=\sum_{k=0}^{m-1}u_kz^k.                    \tag{SR27}
\]
Here \(p_m\) is the original invertible leading matrix, including at the highest coefficient \(u_{m-1}=p_mx_0\). The inverse map from the full numerator coefficients is the ordered triangular recursion
\[
 x_r=p_m^{-1}
       \left(u_{m-1-r}
           -\sum_{q=0}^{r-1}p_{m-r+q}x_q\right),
                   \qquad r=0,\ldots,m-1.                    \tag{SR28}
\]
For \(r=0\) the sum is empty. To verify each row, the coefficient of \(z^{m-1-r}\) in (SR27) is
\(\sum_{q=0}^r p_{m-r+q}x_q\); its last term is precisely \(p_mx_r\).
Multiplication on the left by the actual inverse yields (SR28). Thus the original numerator map is a linear bijection, with every matrix order and leading factor explicit. Its monic comparison \(r(z)=p_m^{-1}p(z)\) has
\(\mathcal U_x^r=p_m^{-1}\mathcal U_x^p\); the comparison does not erase \(p_m\) from either actual forward or inverse map.

To find the first coordinate of the actual resolvent solve
\((zI-C)w=x\). Its first \(m-1\) rows give
\[
 w_j=z^jw_0-\sum_{q=0}^{j-1}z^{j-1-q}x_q,\quad
 p(z)w_0=\mathcal U_x^p(z),\quad
 \pi_0(zI-C)^{-1}x=p(z)^{-1}\mathcal U_x^p(z).                \tag{SR29}
\]
For the last row, multiply by the original \(p_m\) and substitute all preceding rows. Its right side becomes the full sum
\(p_mx_{m-1}+p_m\sum_{q=0}^{m-2}z^{m-1-q}x_q+
  \sum_{j=1}^{m-1}p_j\sum_{q=0}^{j-1}z^{j-1-q}x_q\).
For each original \(x_q\), its coefficient is exactly
\(\sum_{j=q}^{m-1}p_{j+1}z^{j-q}\), proving the second identity. All denominators are legitimate exactly away from the original roots by (SR26) and the actual determinant-inverse criterion; no linear factorization of a matrix polynomial has been assumed. Applying the already proved exponential contour receiver to the original \(C\) gives
\[
 u(t)=\frac{1}{2\pi i}\int_\Gamma
                   p(z)^{-1}\mathcal U_x^p(z)e^{itz}\,dz,
                  \qquad Ju(0)=x.                            \tag{SR30}
\]
Every root multiplicity, matrix pole order, original leading factor, factorial in the earlier scalar pole moments and the original contour prefactor is retained. This is the full original-equation receiving extension of the monic formula (S7) in Section 2; its arbitrary numerator is unique through (SR28).

Boundedness of the original first component gives boundedness of the full original state without assuming spectral separation. With the original state and component norms let
\(h(x)=\int_0^1\|\pi_0E_C(s)x\|^2\,ds\).
If \(h(x)=0\), continuity makes its integrand zero on the entire interval. The first-coordinate solution is then identically zero there. Its derivatives at zero vanish, and its Cauchy coordinates \(x_0,\ldots,x_{m-1}\) vanish by the first rows of (SR25). Thus \(h\) is positive on the original nonzero state space. Its continuity follows from the original finite matrix exponential and norm bounds; the original unit sphere is compact by the retained coordinate comparisons (SR16). Let \(c>0\) be its actual minimum on that sphere. Homogeneity and the original flow addition rule then give
\[
 c\|Ju(t)\|^2\leq
        \int_0^1\|u(t+s)\|^2\,ds,\qquad t\geq0.              \tag{SR31}
\]
Hence a bounded \(u\) has a bounded original jet; conversely its first-coordinate projection is bounded whenever its jet is bounded. The exact derivative conventions are \(D_t^ku=\pi_0C^kJu(t)\) and \(\partial_t^ku=i^k\pi_0C^kJu(t)\), retaining the full original factor \(i^k\). The actual finite operator norm bounds prove boundedness for every derivative. The negative-half-line proof uses the original interval \([-1,0]\) with its own positive minimum and the same exact Cauchy map. For the zero state space the implication is immediate and no minimum on an empty sphere is introduced.

When the original determinant has no real roots, (SR26), (SR20)--(SR21) and (SR31) identify the original bounded solution space with the companion's upper primary space and prove decay of every derivative. Its dimension is the sum of the upper-root algebraic multiplicities of the original \(\det p\), with the original \(\det(p_m^{-1})\) map displayed in (SR26). The full leading-coefficient homotopy and transported boundary measurements in Section 12 retain their separate original formulas and proofs. Formulas (SR25)--(SR31) give the complete original-equation Cauchy, numerator, resolvent and contour maps without dropping its leading matrix.

## 17. Bounded profiles with complex parameters {#AN03-STB-BOUNDED-001}

This separate extension allows real characteristic roots and complex stabilization parameters. Sections 3--12 keep their original stable, no-real-root statements. Here bounded profiles may contain nondecaying real-root modes. The complete classification and jet estimate in Sections 16.5 and 16.7 provide the additional argument; no uniform bundle claim through a real-root crossing is made.

### 17.1. The original polynomial and its full stabilized family

Keep the original finite-dimensional complex space, its chosen norm, and
\[
 p(z)=p_mz^m+\sum_{j=0}^{m-1}p_jz^j,\quad
 p_m\in\operatorname{GL}(E),\quad m>1,\quad N=\dim E,
 \quad D=-i\partial_t.
 \tag{SB1}
\]
There is no restriction on the real roots of \(\det p\). Fix
\[
 \tau\in\mathbb C,\qquad \lambda\in\mathbb C,
 \qquad \alpha=\operatorname{Re}\lambda>0,
 \qquad L(z)=z+i\lambda,\quad R(z)=z-i\lambda.
 \tag{SB2}
\]
Use \(r(z)=p_m^{-1}p(z)\) only for the coefficient calculation (S15)--(S17), retaining the original polynomial. Those identities use \(\lambda\ne0\), scalar polynomial algebra and the actual ordered coefficients; their proofs hold for complex \(\lambda\) without a positivity assumption. Form \(P_\tau[r]\) by exactly (S20)--(S21), with every displayed power of \(\tau\), including the empty middle sum when \(m=2\). The original family and leading coefficient are
\
 \begin{split}
 \mathcal P_\tau(z)&=\operatorname{diag}(p_m,I,\ldots,I)P_\tau[r,\\
 \mathcal C_\tau&=\operatorname{diag}(p_m,I,\ldots,I)C_\tau[r],\\
 \mathcal C_\tau^{-1}&=C_\tau[r]^{-1}
                         \operatorname{diag}(p_m^{-1},I,\ldots,I),\\
 \det\mathcal C_\tau&=\det p_m.
 \end{split}
 \tag{SB3}
\]
Indeed the factorization (S23) is still \(H_\tau(I-\tau S)\). Its actual nilpotents satisfy \(N_\tau^2=0\), \(S^m=0\), so (S25)--(S26) is the same finite inverse for every complex \(\tau\). Both triangular determinants equal one. This proves (SB3), keeping the inverse product in its required order.

The lower-block elimination in Section 9 also uses no real-parameter restriction. For \(L(z)\ne0\) it has the same lower-block determinant and the same Schur complement \(r(z)\). Thus, with both original determinant factors visible,
\[
 \begin{split}
 \det\mathcal P_\tau(z)
   &=\det p_m\,\det r(z)\,L(z)^{m(m-1)N}\\
   &=\det p_m\,\det(p_m^{-1})\det p(z)\,
                                  L(z)^{m(m-1)N}\\
   &=\det p(z)\,L(z)^{m(m-1)N}.
 \end{split}
 \tag{SB4}
\]
Both sides are polynomials, so the identity holds also at \(L(z)=0\). The auxiliary root is \(-i\lambda\), with imaginary part \(-\alpha<0\) and multiplicity \(m(m-1)N\). If it is already an original root, the multiplicities add. Every original real root remains in the determinant, with its full algebraic multiplicity.

### 17.2. The bounded inverse and all original derivative bounds

Let \(\mathcal B^+(p)\) consist of smooth solutions of the original equation on \(\mathbb R\) that are bounded for \(t\geq0\); define \(\mathcal B^+(\mathcal P_\tau)\) in the same way. They include all bounded real-root modes. By (SR31) and (SB3), boundedness of either solution controls its complete original Cauchy jet and every derivative. This implication requires neither spectral separation nor exponential decay.

If \(g\) is smooth on \(\mathbb R\) and all its derivatives are bounded on the positive half-line, set
\[
 T_\lambda g(t)=-i\int_0^\infty e^{-\lambda s}g(t+s)\,ds.
 \tag{SB5}
\]
For negative \(t\), split this integral at \(\max(0,-t)\). Its first part is over a finite interval of smooth values; its tail has the same exponential majorant as on the positive half-line. On a compact set of \(t\)'s the finite interval can be chosen uniformly. This proves convergence and justifies every differentiation in \(t\) by the corresponding derivative majorant.

To verify the equation, integrate the derivative of \(e^{-\lambda s}g(t+s)\). The upper endpoint is zero, the lower endpoint is \(g(t)\), and consequently
\(\int_0^\infty e^{-\lambda s}g'(t+s)\,ds
 =-g(t)+\lambda\int_0^\infty e^{-\lambda s}g(t+s)\,ds\).
Including the original factor \(-i\) gives
\((T_\lambda g)'=\lambda T_\lambda g+ig\), hence
\(L(D)T_\lambda g=g\).
Two bounded solutions differ by \(ce^{\lambda t}\). Its norm is \(\|c\|e^{\alpha t}\), so boundedness forces \(c=0\). Thus (SB5) is the unique bounded inverse. It commutes with each \(D^k\), by the just-proved differentiation.

For \(d\geq0\), retain the actual constants
\(\|D^kg(t)\|\leq M_{k,d}e^{-dt}\), \(t\geq0\). Direct integration yields
\[
 \|D^kT_\lambda g(t)\|
       \leq\frac{M_{k,d}}{\alpha+d}e^{-dt}.
 \tag{SB6}
\]
In particular \(d=0\) gives the full bounded, nondecaying case with denominator \(\alpha\).

**Theorem.** For every parameter pair (SB2), first-coordinate projection is a linear bijection
\[
 \Pi:\mathcal B^+(\mathcal P_\tau)\longrightarrow\mathcal B^+(p),
 \qquad U\longmapsto U_0.
 \tag{SB7}
\]
Its inverse is exactly
\[
 U_0=u,\qquad U_j=\tau T_\lambda R(D)U_{j-1},\quad 1\leq j<m.
 \tag{SB8}
\]
If \(\|D^ku(t)\|\leq M_{0,k,d}e^{-dt}\) for all required derivatives, then the lifted components satisfy
\[
 \|D^kU_j(t)\|\leq
 \frac{|\tau|^j}{(\alpha+d)^j}e^{-dt}
 \sum_{a=0}^j\binom ja |\lambda|^{j-a}M_{0,k+a,d}.
 \tag{SB9}
\]
For \(j=0\), the single summand is the original bound.

**Proof.** For a bounded original family solution the lower row says
\(L(D)^{m-1}g_j=0\), where
\(g_j=L(D)U_j-\tau R(D)U_{j-1}\). All its derivatives, and thus \(g_j\), are bounded by (SR31). Substituting \(g_j=e^{\lambda t}h_j\) gives
\(L(D)^{m-1}g_j=(-i)^{m-1}e^{\lambda t}h_j^{(m-1)}\).
Thus \(h_j\) is a vector polynomial of degree at most \(m-2\). If it is nonzero, an actual bounded coordinate functional detects a nonzero leading coefficient. The full polynomial lower bound (SR19), multiplied by \(e^{\alpha t}\), is unbounded. Therefore \(g_j=0\). This proves every recurrence (S29) on the present bounded space, including complex \(\tau\).

Substitute these recurrences in the original first row. Its complete expression is
\[
 p_m\left((1-\tau^m)r(D)U_0+
       \tau^m\sum_{j=0}^ma_jR(D)^jL(D)^{m-j}U_0\right)
                  =p_mr(D)U_0=p(D)U_0=0.
 \tag{SB10}
\]
The last summand uses the additional \(R(D)\) in (S20), exactly as in Section 10. This proves the codomain of (SB7).

Conversely, (SR31) bounds every derivative of a bounded original \(u\), so each step (SB8) is defined by (SB5), has bounded derivatives by (SB6), and satisfies the actual lower row. Equation (SB10) gives the first row. This proves surjectivity. Uniqueness of the bounded inverse successively shows that a lifted solution with \(U_0=0\) has every component zero, proving injectivity. In particular \(\tau=0\) gives \((u,0,\ldots,0)\) with no division by that parameter.

Finally \(R(D)=D-i\lambda\) and (SB6) give the recursion for the derivative bounds
\(M_{j,k,d}\leq |\tau|(\alpha+d)^{-1}
 (M_{j-1,k+1,d}+|\lambda|M_{j-1,k,d})\).
Starting at \(j=0\), its two finite sums combine by
\(\binom{j-1}{a-1}+\binom{j-1}a=\binom ja\), with each endpoint term retained. Induction proves exactly (SB9). \(\square\)

### 17.3. Exact iterated kernels and parameter derivatives

The lift has a full integral formula, rather than only a formal inverse power. For \(j\geq1\),
\[
 T_\lambda^jg(t)=\frac{(-i)^j}{(j-1)!}
        \int_0^\infty s^{j-1}e^{-\lambda s}g(t+s)\,ds.
 \tag{SB11}
\]
Induction proves this formula. The step from \(j\) to \(j+1\) has an absolutely integrable double integral, bounded on the positive half-line by the complete product envelope \(M_{0,d}r^{j-1}e^{-(\alpha+d)(r+s)}\). For negative \(t\), use the same finite-interval/tail split as above. Fubini therefore applies. The substitution \(v=r+s\), with Jacobian one and \(0\leq r\leq v\), has inner integral
\(\int_0^v r^{j-1}/(j-1)!\,dr=v^j/j!\).
The factor becomes exactly \((-i)^{j+1}\), proving (SB11) with its full factorial.

Only scalar constant-coefficient operators are commuted in the following binomial calculation:
\[
 U_j=\tau^j\sum_{a=0}^j\binom ja(-i\lambda)^{j-a}
                      T_\lambda^jD^au,\qquad j\geq1.
 \tag{SB12}
\]
Indeed \(T_\lambda\) commutes with \(D\), and expansion of \((D-i\lambda)^j\) supplies precisely these coefficients. No two original matrix coefficients are commuted.

For each integer \(b\geq0\), differentiation in \(\lambda\) gives
\[
 \partial_\lambda^bT_\lambda^jg(t)
  =\frac{(-i)^j(-1)^b}{(j-1)!}
       \int_0^\infty s^{j+b-1}e^{-\lambda s}g(t+s)\,ds,
 \tag{SB13}
\]
and
\[
 \|D^k\partial_\lambda^bT_\lambda^jg(t)\|
 \leq\frac{(j+b-1)!}{(j-1)!}
       \frac{M_{k,d}}{(\alpha+d)^{j+b}}e^{-dt}.
 \tag{SB14}
\]
On a compact subset of \(\operatorname{Re}\lambda>0\), the displayed integrals have common integrable derivative envelopes, which justifies the differentiation. The scalar moment used here is exact:
\(\int_0^\infty s^he^{-cs}\,ds=h!c^{-h-1}\) for \(c>0\), \(h\geq0\). At \(h=0\) it is direct integration. For \(h>0\), integration by parts has zero upper endpoint and zero lower endpoint, and gives \(h/c\) times the preceding moment. This proves every factorial in (SB14).

For \(c\geq0\) the full product rule for the original lift is
\[
 \begin{split}
 \partial_\lambda^cU_j={}&\tau^j\sum_{a=0}^j\binom ja
   \sum_{\substack{0\leq b\leq c\\c-b\leq j-a}}
    \binom cb(-i)^{j-a}\frac{(j-a)!}{(j-a-c+b)!}\\
 &\hspace{15mm}\cdot\lambda^{j-a-c+b}
       \partial_\lambda^b(T_\lambda^jD^au),\qquad j\geq1.
 \end{split}
 \tag{SB15}
\]
Its indices make every factorial and power defined; differentiated polynomial terms outside this range are zero. Taking norms and using (SB14) proves the explicit bound
\[
 \begin{split}
 \|D^k\partial_\lambda^cU_j(t)\|
 \leq{}&|\tau|^je^{-dt}\sum_{a=0}^j\binom ja
   \sum_{\substack{0\leq b\leq c\\c-b\leq j-a}}
     \binom cb\frac{(j-a)!}{(j-a-c+b)!}
             |\lambda|^{j-a-c+b}\\
 &\hspace{8mm}\cdot\frac{(j+b-1)!}{(j-1)!}
             \frac{M_{0,k+a,d}}{(\alpha+d)^{j+b}}.
 \end{split}
 \tag{SB16}
\]
Here \(\lambda\ne0\) by (SB2), and every power-zero factor equals one. For the other parameter, the complete formula is
\[
 \partial_\tau^qU_j=
 \begin{cases}
 \displaystyle\frac{j!}{(j-q)!}\tau^{j-q}(T_\lambda R(D))^ju,
                                      &0\leq q\leq j,\\
 0,&q>j.
 \end{cases}
 \tag{SB17}
\]
At \(\tau=0\) the power-zero term is one. The coordinate \(U_0=u\) is independent of both parameters; its positive-order parameter derivatives vanish. Applying (SB17) to (SB15) gives all mixed derivatives, with exactly the same finite product-rule coefficients.

For fixed \(p\) and \(u\), these formulas prove holomorphic dependence of the lift on \(\lambda\) in its right half-plane and polynomial dependence on \(\tau\). To verify the analytic assertion directly, expand \(e^{-hs}\) in (SB5) at a fixed \(\lambda\). For \(|h|<\alpha\), the sum of integral norms in any bounded derivative seminorm is at most
\(M_{k,0}\alpha^{-1}\sum_{a\geq0}(|h|/\alpha)^a\).
It converges, so termwise integration gives the Taylor series in that seminorm. On a compact negative \(t\) interval, the finite first part has uniformly bounded smooth input values and an entire exponential series; the remaining tail has the same convergent majorant, with its finite shift factor. This proves the assertion in each local derivative seminorm as well. Formula (SB11), finite products and (SB12) then give the asserted dependence of every component. This concerns a fixed original solution space; it does not assert smoothness of bounded spaces when an original root crosses the real axis.

### 17.4. Real modes, multiplicities and the exact Cauchy maps

For the original companion \(C\) in (SR25), the bounded initial space is exactly
\[
 J\mathcal B^+(p)(0)=
  \bigoplus_{\operatorname{Im}\zeta>0}W_\zeta(C)
  \ \oplus\!\bigoplus_{\zeta\in\mathbb R}\ker(C-\zeta I).
 \tag{SB18}
\]
Only actual roots contribute a summand. Formula (SR20) proves this for the full state and (SR31) identifies first-coordinate boundedness with state boundedness. The original Cauchy map and its inverse in (SR25) identify it with the actual solution space.

The exact real-root kernel map, for each real \(\zeta\), is
\[
 \ker p(\zeta)\longrightarrow\ker(C-\zeta I),\qquad
 v\longmapsto(v,\zeta v,\ldots,\zeta^{m-1}v),
 \qquad\text{inverse }\pi_0.
 \tag{SB19}
\]
The first \(m-1\) rows of the eigenvector equation force precisely these coordinates. The last row, multiplied on the left by the actual \(p_m\), says
\(p_m\zeta^mv+\sum_{j=0}^{m-1}p_j\zeta^jv=p(\zeta)v=0\).
Both directions follow, proving the map and inverse without dropping the leading coefficient. Formula (SR26) retains its complete signs and factor \(\det(p_m^{-1})\); hence every upper-root primary dimension equals the algebraic multiplicity of that root in the original \(\det p\). Consequently
\[
 \dim\mathcal B^+(p)
 =\sum_{\operatorname{Im}\zeta>0}
                     \operatorname{mult}_\zeta(\det p)
       +\sum_{\zeta\in\mathbb R}\dim\ker p(\zeta).
 \tag{SB20}
\]
Real bounded modes are counted by their geometric nullities, not by substituting their entire algebraic multiplicities. Higher real Jordan terms give the unbounded time polynomials already proved in (SR18)--(SR20).

For real \(\zeta\), \(L(\zeta)\ne0\), since its imaginary part is \(\alpha\). The original stabilized real-root kernel and its inverse are
\[
 v\longmapsto
       \left(\left(\tau\frac{R(\zeta)}{L(\zeta)}\right)^jv
                         \right)_{j=0}^{m-1},
 \qquad
 \ker p(\zeta)\simeq\ker\mathcal P_\tau(\zeta),
 \qquad\text{inverse }\pi_0.
 \tag{SB21}
\]
The lower rows uniquely force these coordinates because \(L(\zeta)\ne0\); the first row is the actual Schur complement \(p(\zeta)v\) proved in (SB4). This proves the displayed bijection. For \(u(t)=e^{it\zeta}v\), direct integration in (SB5) gives
\(T_\lambda u=-i(\lambda-i\zeta)^{-1}u\), and
\(L(\zeta)=i(\lambda-i\zeta)\). Thus (SB8) gives exactly the coefficient in (SB21), preserving the original frequency and factor \(-i\). At \(\tau=0\), its first coordinate is one times \(v\), and every positive-index coordinate is zero. The auxiliary lower root supplies no additional bounded mode by the classification (SR20).

### 17.5. Every finite boundary measurement and its ordered remainder

For the original finite family (S33), with arbitrary finite normal orders, put
\[
 \mathfrak B u=(B_\ell(D)u(0))_\ell,
 \quad\mathfrak B_\tau U=(B_\ell(D)U_0(0))_\ell,
 \quad\mathfrak B_\tau=\mathfrak B\Pi.
 \tag{SB22}
\]
The target remains the actual \(G=\bigoplus_\ell G_\ell\), including the empty target. The bijection (SB7) proves
\(\ker\mathfrak B_\tau=\Pi^{-1}(\ker\mathfrak B)\) and
\(\operatorname{im}\mathfrak B_\tau=\operatorname{im}\mathfrak B\): the first follows by evaluating (SB22), and the second follows in both directions using the inverse lift. Thus bijectivity, kernel dimension and image are preserved for every complex \(\tau\), including zero, and every \(\lambda\) in (SB2).

When \(d_\ell<m\), equations (S35)--(S36) retain exactly their full coefficients, including \(i^{r+1-m}\), \(2^{1-m}\), \(\lambda^{r+1-m}\), and the entire signed binomial sum. The polynomial change of variables needs only \(\lambda\ne0\), so applies here. The same recurrence proves (S37) for \(\tau\ne0\) as an equality of functions on the lifted bounded space. It remains unsuitable for an ambient operator at zero; (SB22) is the actual endpoint map.

For any larger boundary degree one can also prove an exact polynomial reduction without altering the original equation. If its current leading coefficient is \(b\) and its degree is \(d\geq m\), subtract
\[
 (b p_m^{-1})z^{d-m}p(z).
 \tag{SB23}
\]
This cancels exactly the leading term \(bz^d\), with the original composition order. Repeating the strict degree decrease gives
\(B(z)=Q(z)p(z)+B_{<m}(z)\), where \(\deg B_{<m}<m\).
Uniqueness follows because any nonzero difference \(Q\), with leading coefficient \(q\), gives the nonzero leading coefficient \(q p_m\) in \(Qp\); invertibility of \(p_m\) makes its degree at least \(m\). It cannot equal a polynomial of degree less than \(m\). On actual solutions, constant-coefficient differentiation and these ordered compositions give
\(B(D)u=Q(D)p(D)u+B_{<m}(D)u=B_{<m}(D)u\).
Thus the actual arbitrary-order measurements can be computed by this remainder and the original coefficient formula (S36), with every subtracted term recorded. This finite-dimensional normal-variable proof makes no reduction of tangential PDE orders or their Sobolev shifts.

### 17.6. The exact measurement map during rate deformation

Return only for this paragraph to the original no-real-root branch (S9). Let \(C\) be the original companion, \(q=q_C\) its full upper projection, and \(\lambda_0>0\) a fixed real number. The deformation in Section 5 is
\[
 C_\theta=(1-\theta)C+i\theta\lambda_0(2q-I),
       \qquad0\leq\theta\leq1.
 \tag{SB24}
\]
Its bounded initial space is the same \(qE^m\), by (S12). An original profile is \(u(t)=\pi_0E_C(t)v\); the new first-order state profile is \(w(t)=E_{C_\theta}(t)v\), for the same \(v\in qE^m\). Sending \(u\) to \(w\) is a bijection: its forward map uses the unique original Cauchy state, and its inverse is
\(w\mapsto\pi_0E_C(t)w(0)\). First-order uniqueness and (SR25) prove both compositions to be identities.

For the original boundary polynomial, keep every original coefficient and derivative order in
\[
 H_\ell=\sum_{r=0}^{d_\ell}b_{\ell r}\pi_0 C^r,
 \qquad\widetilde{\mathfrak B}_\theta(w)
                         =(H_\ell w(0))_\ell.
 \tag{SB25}
\]
Since \(D^ru(0)=\pi_0C^rv\), this is precisely the transported original measurement. Its commuting map is proved by substituting \(w(0)=v\), so it preserves the original kernel, image and bijectivity.

If one instead applies the unchanged polynomial \(B_\ell(D)\) to the first coordinate of the new state profile, the measurement is
\(\sum_r b_{\ell r}\pi_0C_\theta^rv\). The complete difference from (SB25) is
\[
 \begin{split}
 \Delta_{\ell,\theta}
  &=\sum_{r=1}^{d_\ell}b_{\ell r}\pi_0
       \sum_{a=0}^{r-1}C_\theta^{r-1-a}(C_\theta-C)C^a,\\
 C_\theta-C&=\theta\big(i\lambda_0(2q-I)-C\big).
 \end{split}
 \tag{SB26}
\]
For each \(r\), expansion of the middle difference produces
\(C_\theta^{r-a}C^a-C_\theta^{r-1-a}C^{a+1}\).
Successive terms telescope, retaining their order, to \(C_\theta^r-C^r\). This proves (SB26) without assuming commutation. The zero-order summand has zero difference; for degree zero the displayed sum is empty.

A concrete original order-two example shows why this receiving map matters. Take
\[
 p(z)=(z-i)^2,\quad
 C=\begin{pmatrix}0&1\\1&2i\end{pmatrix},\quad
 q=I,\quad v=(1,i),\quad\lambda_0=2,\quad B(z)=z.
 \tag{SB27}
\]
Here \(Cv=iv\), \(C_\theta v=i(1+\theta)v\), and \(v\) belongs to the bounded upper space. The original measurement and its transported value are both \(i\). Applying the unchanged derivative polynomial to the deformed first coordinate instead gives \(i(1+\theta)\), with difference \(i\theta\). Both profiles are exponentially decreasing. This proves that preservation of the initial stable space does not itself preserve unchanged derivative expressions; (SB25) supplies the exact correspondence. The earlier stable-bundle statement is retained with its original scope.

### 17.7. A real double root and an exact complex lift

![Original real and auxiliary roots, with the exact bounded lifted profile](../figures/bounded-boundary-original-modes.png)

The figure uses the original polynomial \(p(z)=3z^2\), \(E=\mathbb C\), \(m=2\), \(\lambda=1+i\), \(\tau=i\). The coefficient calculation gives \(a_0=1/4,a_1=1/2,a_2=1/4\), since
\(r(z)=z^2=(L(z)+R(z))^2/4\). The full original determinant is
\[
 \det\mathcal P_\tau(z)=3z^2(z+i\lambda)^2,
                  \qquad\det\mathcal C_\tau=3.
 \tag{SB28}
\]
The original root zero has algebraic multiplicity two, but its bounded original space consists exactly of constants and has dimension one: \(D^2u=0\) gives \(u=a+bt\), bounded exactly when \(b=0\). The auxiliary root \(-i\lambda=1-i\) also has multiplicity two and has no bounded positive-half-line mode. Formula (SB21) gives the exact lifted constant
\(U=(1,-\tau)=(1,-i)\).
The original first-row value at \(D=0\) is
\(3[-\tau^2\lambda^2/4+\tau^2\lambda^2/4]=0\), while the lower row is
\(-\lambda^2(-\tau)-\tau\lambda^2=0\).
These are symbolic equalities with all factors retained. The right panel shows \(\operatorname{Re}U_0=1\), \(\operatorname{Im}U_1=-1\), and both zero components. Its finite plotting interval is an illustration of this exact profile, not a numerical proof of boundedness. The editable figure source and parameters preserve these original coordinates. Hörmander's boundary-system setting is the human antecedent identified in the references.

If \(E=0\), both solution spaces and all kernels above are zero, every determinant is the empty product one, and every measurement has the zero-domain image. The proofs use no minimum on an empty sphere. All statements about nonzero leading coordinates and roots then disappear, while the zero-space bijections and arbitrary target convention remain exact.

## Further questions and analytic use

The next analytic use of this algebra is a family over nonzero tangential covectors. Section 4 supplies its stable vector bundle, and (S33) supplies the finite-dimensional complementing map. A global boundary parametrix also needs symbol calculus, coordinate invariance, bundle gluing and adjoint theory; Cauchy data from jumps and residues and Solving an elliptic system from compatible boundary measurements develop those analytic steps. A fiberwise stable isomorphism alone does not establish their Sobolev estimates or index statements.

For the analytic use of a homogeneous differential principal polynomial, Cauchy data from jumps and residues, Section9 proves the exact reflection of the original solutions and every Cauchy jet. Its positive mode bundle together with the antipodal pullback of that bundle maps bijectively onto the entire original jet bundle, with an explicit inverse. In dimension at least three the original stable rank is necessarily half the total solution rank; in dimension two the antipodal ranks are complementary and may differ. These conclusions use the additional homogeneous differential and ellipticity hypotheses proved there. They are not imposed on the arbitrary matrix polynomials or bounded real-root constructions of this lesson.

Two useful research questions are to identify when the stable bundle admits a globally chosen system of boundary measurements, and to determine which additional estimates survive when spectral roots approach the real axis. The examples here already distinguish the local rank condition from a global choice of boundary data, and show why estimates uniform through a real crossing cannot be inferred from this lesson.

## References

Lars Hörmander, *The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*, corrected second printing (1994), §20.1, gives the setting of elliptic boundary systems. The finite-dimensional algebra, decay estimates, examples and solved problems in this lesson are given above.

[Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md), Sections 2–9, proves the exact scalar algebra and contour tools used here.