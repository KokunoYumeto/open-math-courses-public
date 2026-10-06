# Stable modes and the algebra of boundary data

**AN-03 · Unit AN03-U003 · Independent English AI draft, not admitted.**

A frozen boundary equation asks which normal profiles remain bounded inside the domain, and which boundary measurements determine those profiles. For systems, the number of profiles counts algebraic multiplicity. Eigenvectors alone can miss solutions. This unit constructs the bounded solution space from Cauchy data, then changes the equation while preserving that space and its boundary measurements.

Throughout, vector spaces are finite-dimensional and complex, coefficients are constant in the normal variable, and

\[
D=-i\frac{d}{dt},\qquad t\in\mathbb R.
\]

We call a solution *stable* when it is bounded for \(t\geq0\). Under the no-real-root hypotheses below, this is equivalent to exponential decay of the solution and every derivative. No diagonalizability, simplicity of roots, commutation of matrix coefficients, or prescribed number of boundary equations is assumed.

The elementary prerequisite contracts are polynomial division and Bézout identities over \(\mathbb C\), the fundamental theorem of algebra, Cayley–Hamilton, and the contour moment identities for globally convergent power-series numerators with prescribed spectral indices, with the exact reading and finite entry-base boundaries specified in [AN03-P002](stable-prerequisite-bridges.md). The finite-dimensional linear algebra used includes bases and direct sums, rank and trace of projections, determinant multiplicativity and block-triangular determinants, elementary row and column operations, operator norms and continuity of matrix inversion. The calculus used includes locally uniformly convergent exponential series, termwise differentiation and integration when the differentiated series converge locally uniformly, dominated differentiation of exponentially decreasing integration tails, and compactness of the unit sphere. The spectral and ODE results needed here are proved below. These contracts specify mathematical dependencies; no existing exposition is imported as text.

## AN03-STB-001 — Spectral calculus without an eigenbasis

Let \(V\) be a finite-dimensional complex vector space and \(A\in\operatorname{End}(V)\). Choose any norm. The series

\[
E_A(t)=\sum_{k=0}^{\infty}\frac{(itA)^k}{k!}
\]

converges locally uniformly with all derivatives, since its norms and the norms of its differentiated terms are bounded by scalar exponential series. Thus \(DE_A=AE_A\), \(E_A(0)=I\), and multiplication of absolutely convergent series gives \(E_A(-t)E_A(t)=I\). If \(Du=Au\), differentiating \(E_A(-t)u(t)\) shows that it is constant. Consequently

\[
u(t)=E_A(t)v                                                 \tag{S1}
\]

is the unique solution with \(u(0)=v\). In particular the solution space has dimension \(\dim V\).

Here is the spectral information, including the nilpotent terms. Factor the minimal polynomial as \(\prod_{\zeta}(z-\zeta)^{\nu_\zeta}\). The factors are pairwise relatively prime. Repeated Bézout identities give polynomials \(e_\zeta\) which are one modulo \((z-\zeta)^{\nu_\zeta}\) and zero modulo every other factor. Their sum is one modulo the minimal polynomial. Evaluation at \(A\) therefore gives projections

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

The first identity follows by multiplying a finite geometric series; the second follows from the exponential series for commuting \(\zeta I\) and \(N_\zeta\). The Cauchy formula applied to the first identity yields

\[
E_A(t)=\frac{1}{2\pi i}\int_\Gamma
e^{itz}(zI-A)^{-1}\,dz,                                    \tag{S3}
\]

where \(\Gamma\) is a finite union of positively oriented closed contours enclosing every eigenvalue once and no point of the spectrum on the contours. Integrating the resolvent alone around a single eigenvalue gives \(Q_\zeta\). These assertions also follow directly from (S2), so multiple poles are included.

For later counting, \(\dim V_\zeta\) equals the algebraic multiplicity of \(\zeta\) in \(\det(zI-A)\). The direct sum decomposes the determinant into the determinants of the restrictions. A nilpotent map is upper triangular with zero diagonal in a basis adapted to its successive kernels; the restriction to \(V_\zeta\) therefore contributes \((z-\zeta)^{\dim V_\zeta}\). The length of a nilpotent chain affects polynomial factors in time, while the dimension of the whole generalized eigenspace determines the number of solutions.

## AN03-STB-002 — A monic equation and its complete Cauchy coordinates

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

If \(p(D)u=0\), its state \(J u=(u,Du,\ldots,D^{m-1}u)\) satisfies \(D(Ju)=C_pJu\). Conversely, the first \(m-1\) rows of this first-order equation imply that any state solution is the jet of its first component, and the last row gives \(p(D)u=0\). Applying AN03-STB-001 proves existence and uniqueness for arbitrary Cauchy data and gives \(\dim\ker p(D)=mN\).

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

The contours enclose all roots of \(\det p\). Formula (S7) is valid for repeated roots and matrix poles of arbitrary order. It is the sum of the corresponding residues. The triangular bijection above proves uniqueness of the polynomial in this representation, as well as existence. In particular, it does not require a factorization of \(p\) into linear matrix factors.

## AN03-STB-003 — Bounded solutions, derivatives, and multiplicity

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

## AN03-STB-004 — Parameters and fixed projections

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

## AN03-STB-005 — Collapsing rates within their half-planes

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

For parameter-dependent \(A\) and positive \(\lambda\), (S12) has the same regularity as those data by AN03-STB-004. There is no additional requirement that \(\lambda\) avoid the original eigenvalues.

## AN03-STB-006 — Polynomial coordinates adapted to two half-planes

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

## AN03-STB-007 — First-order coordinates that respect decay

For a solution of \(p(D)u=0\), define

\[
v_j=R(D)^jL(D)^{m-1-j}u,\qquad 0\leq j<m.                \tag{S18}
\]

The polynomials \(R^jL^{m-1-j}\) form a basis of the scalar polynomials of degree at most \(m-1\), by the same argument as in AN03-STB-006. Thus (S18) is an invertible, constant, scalar-block change from the Cauchy state \((u,Du,\ldots,D^{m-1}u)\). There is no loss of a Cauchy coordinate.

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

## AN03-STB-008 — An explicit stabilization and its leading coefficient

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

## AN03-STB-009 — A determinant identity retaining every root

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

## AN03-STB-010 — The stable space is preserved, with an explicit inverse

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

**Proof.** The leading coefficient is invertible by (S24), and the determinant has no real zeros by (S27). AN03-STB-003 therefore applies to \(P_\tau\): every stable solution and all its derivatives decay exponentially.

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

Every \(u\in\mathcal M^+(p)\) has these bounds by AN03-STB-003. Define

\[
U_0=u,\qquad U_j=\tau T_\lambda R(D)U_{j-1}\ (1\leq j<m). \tag{S32}
\]

These functions are defined on all real \(t\); for fixed \(t\), the integration tail still lies in the decaying region. They and all their derivatives decay on the positive half-line, satisfy (S29), and hence satisfy every lower row of \(P_\tau(D)U=0\). Substituting the recurrences into the first row gives \(p(D)u=0\), as above. This proves surjectivity. If \(U_0=0\), each successive bounded solution of \(L(D)U_j=\tau R(D)U_{j-1}\) is zero by uniqueness, proving injectivity. \(\square\)

Since \(T_\lambda\) commutes with scalar constant-coefficient differentiation on these functions, the lift can also be written

\[
U_j=\tau^j(T_\lambda R(D))^ju.
\]

At \(\tau=0\), this is exactly \((u,0,\ldots,0)\); no division by \(\tau\) is needed. The same estimates show local \(C^r\) dependence of the lift on \(C^r\) coefficients and on \(\lambda>0\). In Cauchy coordinates this is an isomorphism of the stable bundles from AN03-STB-004. On compact parameter sets, differentiation of (S30) in \(\lambda\) introduces powers of \(s\), whose integrals remain finite because \(\lambda\) has a positive lower bound and the stable decay estimates are uniform.

## AN03-STB-011 — Boundary measurements, their orders, and the zero endpoint

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

## AN03-STB-012 — The normalized reduction package

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

for a matrix \(A_*\) with no real eigenvalues: the first-order factor is monic and its determinant is \(\det p(z)\). Thus its stable equation can be further deformed by AN03-STB-005. The scalar factor in (S39) has only the lower root \(-i\lambda\); cancellation of that factor is valid for bounded solutions by AN03-STB-010, and is not an equality of full solution spaces.

An original polynomial with invertible leading coefficient \(p_m\) can first be replaced by \(p_m^{-1}p\), which has the same solutions and real invertibility. All displayed determinant-one claims then refer to the construction from that *normalized* polynomial. A singular leading coefficient falls outside this package: neither the full \(mN\)-dimensional Cauchy coordinate space nor this normalization is available in general.

## AN03-STB-EX-001 — A four-dimensional stable space with cubic time factors

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

## AN03-STB-EX-002 — Noncommuting coefficients and an unsuitable trace

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

## AN03-STB-PS-001 — Problems with solutions

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

## Further directions and claim boundary

The next analytic use of this algebra is a family over nonzero tangential covectors. AN03-STB-004 supplies its stable vector bundle, and (S33) supplies the finite-dimensional complementing map. Constructing a global boundary parametrix, proving its Sobolev mapping properties, and deriving an index theorem require the symbol calculus, coordinate invariance, bundle gluing, and adjoint theory developed in other units. A fiberwise stable isomorphism alone proves none of those analytic conclusions.

Two useful research questions are to identify when the stable bundle admits a globally chosen system of boundary measurements, and to determine which additional estimates survive when spectral roots approach the real axis. The examples here already distinguish the local rank condition from a global choice of boundary data, and show why estimates uniform through a real crossing cannot be inferred from this unit.

The mathematical antecedents are the finite-dimensional resolvent calculus and Lars Hörmander's treatment of the algebra underlying elliptic boundary problems. The determinant calculation, the derivative estimate through an observation integral, and the examples and exercises above are written for this course.
