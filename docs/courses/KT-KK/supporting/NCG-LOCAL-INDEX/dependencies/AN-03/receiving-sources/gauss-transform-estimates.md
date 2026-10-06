# Quadratic Fourier multipliers at a moving scale

**AN-03 · Unit AN03-U002 · Independent English AI draft, not admitted.**

A quadratic Fourier multiplier spreads a localized function in directions determined by the quadratic form. Its Taylor polynomial is local, while its remaining tail can cross many localization balls. We will estimate the two parts separately and then prove that they combine in the full slowly varying metric symbol class.

The local-symbol definitions, partitions and reconstruction estimates are those of AN03-U001. The additional prerequisites are Fourier inversion and Plancherel on Schwartz functions, the behavior of the Fourier transform under derivatives and multiplication by coordinates, and separation of finite-dimensional convex sets. These are explicit external prerequisite contracts; their open-import identities remain outstanding in the course ledger. The arguments below prove the estimates from those contracts. They do not establish the whole course's prerequisite closure.

## AN03-GAU-001 — Conventions and the dual distance

Let \(E=\mathbb R^d\), with dual pairing \(\langle X,\Xi\rangle\). We use

\[
\widehat u(\Xi)=\int e^{-i\langle X,\Xi\rangle}u(X)\,dX,\qquad
u(X)=(2\pi)^{-d}\int e^{i\langle X,\Xi\rangle}\widehat u(\Xi)\,d\Xi,
\qquad D=-i\partial.
\]

Let \(A\) be any real quadratic form on \(E^*\). Its associated symmetric linear map \(B:E^*\to E\) is specified by \(A(\Xi)=\langle B\Xi,\Xi\rangle\); in particular \(A'(\Xi)=2B\Xi\). Define

\[
T_Au=\mathcal F^{-1}(e^{iA}\widehat u).
\]

Multiplication by \(e^{iA}\) preserves Schwartz space: every derivative of that function is a polynomial times it, so the product rule controls all Schwartz seminorms. Thus \(T_A\) acts on Schwartz functions, and by duality on tempered distributions. It commutes with constant-coefficient derivatives.

For a positive-definite quadratic form \(Q\) on \(E\), set

\[
Q^A(Z)=\sup_{\Xi:\,Q(B\Xi)<1}|\langle Z,\Xi\rangle|^2.
                                                               \tag{G1}
\]

The value is \(+\infty\) unless \(Z\in\operatorname{ran}B\). Indeed, if \(Z\) does not annihilate \(\ker B\), a multiple of a kernel vector makes the numerator arbitrarily large with zero denominator. Conversely, on the quotient \(E^*/\ker B\), the form \(Q(B\Xi)\) is positive definite, so its dual is a finite positive-definite form on the annihilator \((\ker B)^\perp=\operatorname{ran}B\). This also proves that (G1), restricted to that range, is a quadratic form.

In coordinates in which \(Q\) is Euclidean and \(B\) is diagonal with eigenvalues \(\beta_j\),

\[
Q^A(Z)=\sum_{\beta_j\ne0}\frac{Z_j^2}{\beta_j^2}
\quad\text{if }Z_j=0\text{ whenever }\beta_j=0.
                                                               \tag{G2}
\]

Off that subspace it is infinite. Consequently

\[
h_Q=\sup_{\Xi\ne0}\frac{|A(\Xi)|}{Q^{-1}(\Xi)}
=\max_j|\beta_j|,
\qquad
Q(Z)\leq h_Q^2Q^A(Z).                                         \tag{G3}
\]

Equivalently \(h_Q^2=\sup_{Z\ne0}Q(Z)/Q^A(Z)\), where the ratio is zero off \(\operatorname{ran}B\). Formula (G2) proves this by maximizing on the eigen-directions with \(\beta_j\ne0\); when \(B=0\), every ratio in this convention is zero.

Here \(Q^{-1}\) is the ordinary dual quadratic form. If \(B=0\), take \(h_Q=0\); the inequality means \(Q(0)=0\) on the finite domain of \(Q^A\), with the off-domain case interpreted directly rather than as the undefined product \(0\cdot\infty\).

If \(Q_1\leq M Q_2\), their phase-dual forms obey \(Q_1^A\geq M^{-1}Q_2^A\), because the defining ellipsoid for the first supremum contains a suitable dilation of the ellipsoid for the second. Both are infinite off the same range, and the assertion on that range is the usual reversal of positive quadratic forms.

## AN03-GAU-002 — A Taylor bound uniform in the phase

**Theorem.** Let \(K=\{X:Q(X)<1\}\), \(u\in C_c^\infty(K)\), and let \(s\) be an integer with \(s>d/2\). For every integer \(N\geq0\),

\[
\sup_X\left|T_Au(X)-\sum_{j<N}\frac{(iA(D))^ju(X)}{j!}\right|
\leq \frac{C_{d,s}}{N!}
\max_{0\leq j\leq s}\sup_{Y\in K}|A(D)^Nu|_{j,Q}(Y).          \tag{G4}
\]

The constant is independent of \(A\) and \(Q\); for \(N=0\) the sum is empty.

**Proof.** Make a linear change of variables that sends \(Q\) to the Euclidean metric. The Fourier Jacobian and inverse-transform Jacobian cancel, so it suffices to prove the same estimate on the Euclidean unit ball. For real \(t\), Taylor's integral remainder gives

\[
\left|e^{it}-\sum_{j<N}(it)^j/j!\right|\leq |t|^N/N!.
\]

For \(N=0\) this is simply \(|e^{it}|=1\). Fourier inversion therefore bounds the left side of (G4) by
\((2\pi)^{-d}\|\widehat{A(D)^Nu}\|_{L^1}/N!\).
For any smooth \(v\) supported in the unit ball, Cauchy–Schwarz gives

\[
\|\widehat v\|_{L^1}
\leq \left(\int\langle\Xi\rangle^{-2s}\,d\Xi\right)^{1/2}
\|\langle\Xi\rangle^s\widehat v\|_{L^2}
\leq C_{d,s}\sum_{|\alpha|\leq s}\|\partial^\alpha v\|_{L^2}.
\]

The integral is finite exactly for \(s>d/2\). Plancherel proves the last estimate, and the fixed volume of the support bounds the \(L^2\) norms by derivative suprema. This proves (G4), including its uniformity. ∎

The same reasoning at a fixed support radius \(a>0\) gives a constant depending also on \(a\). Combining (G3) with diagonalization yields the useful consequence

\[
\|T_Au-\sum_{j<N}(iA(D))^ju/j!\|_\infty
\leq C_{d,s,N,a}\,h_Q^N
\max_{j\leq s+2N}\sup|u|_{j,Q},\qquad
\operatorname{supp}u\subset\{Q<a^2\}.                         \tag{G5}
\]

To see the coefficient bound explicitly, in orthonormal eigen-coordinates
\(A(D)=\sum_j\beta_jD_j^2\). Expanding its \(N\)-th power has the sum of absolute coefficients bounded by
\((\sum_j|\beta_j|)^N\leq d^Nh_Q^N\).
Applying at most \(s\) further derivatives gives (G5).

## AN03-GAU-003 — An affine denominator and repeated integration by parts

**Lemma.** Let \(L\) be real affine and nonzero on \(\{Q<R^2\}\), with \(R>1\). Then for \(Y\in K\) and every integer \(k\geq0\),

\[
|L(0)/L|_{k,Q}(Y)\leq k!R(R-1)^{-k-1}.                      \tag{G6}
\]

**Proof.** The assumption implies \(L(0)\ne0\). In \(Q\)-orthonormal coordinates, write \(L(Y)/L(0)=1-\ell\cdot Y\). Its zero hyperplane misses the open ball of radius \(R\), so \(|\ell|\leq R^{-1}\). Direct differentiation gives

\[
\partial_{T_1}\cdots\partial_{T_k}(1-\ell\cdot Y)^{-1}
=k!\frac{\prod_j(\ell\cdot T_j)}{(1-\ell\cdot Y)^{k+1}}.
\]

For unit directions and \(|Y|<1\), its absolute value is at most
\(k!R^{-k}(1-R^{-1})^{-k-1}\), which is (G6). ∎

For affine \(L\), the Fourier multiplication/derivative identities give the exact commutator

\[
[T_A,L]=T_A\langle A'(D),L'\rangle.                           \tag{G7}
\]

For example, Fourier transforming multiplication by \(X_j\) gives \(i\partial_{\Xi_j}\); subtracting in the order \(T_AX_j-X_jT_A\) leaves \(A'_{\Xi_j}e^{iA}\), confirming the sign in (G7). Constant terms commute.

Fix an observation point \(X\), choose \(\eta\in E^*\), and put \(L(Y)=\langle Y-X,\eta\rangle\). If it is nonzero on a neighborhood of \(\operatorname{supp}u\), the function \(L^{-1}u\), extended by zero, is smooth and compactly supported. Evaluating (G7) at \(X\), where \(L(X)=0\), gives

\[
T_Au(X)=2T_A\big(\langle B\eta,D\rangle(L^{-1}u)\big)(X).
                                                               \tag{G8}
\]

Iteration preserves the support. Using (G6), the product rule and the fact that a directional derivative along \(B\eta\) costs \(Q(B\eta)^{1/2}\), induction proves

\[
|T_Au(X)|
\leq C_{k,R,d,s}
\left(\frac{Q(B\eta)^{1/2}}{|L(0)|}\right)^k
\max_{j\leq s+k}\sup_{Y\in K}|u|_{j,Q}(Y).                    \tag{G9}
\]

For the induction, define \(Vv=\langle B\eta,D\rangle(L^{-1}v)\). Formula (G6) bounds derivatives of \(L^{-1}\) by a constant divided by \(|L(0)|\); therefore
\(\max_{j\leq l}|Vv|_{j,Q}\leq C_{l,R}Q(B\eta)^{1/2}|L(0)|^{-1}\max_{j\leq l+1}|v|_{j,Q}\).
Apply this \(k\) times and then (G4) with \(N=0\) to \(V^ku\). This proves (G9) with no assumption that \(A\) is invertible or definite.

## AN03-GAU-004 — The full off-support estimate

**Theorem.** Under the hypotheses of AN03-GAU-002, for \(R>1\) and \(k\geq0\),

\[
|T_Au(X)|\leq C_{k,R,d,s}
\left(1+\inf_{Y\in RK}Q^A(X-Y)\right)^{-k/2}
\max_{j\leq s+k}\sup_K|u|_{j,Q}.                              \tag{G10}
\]

For \(k>0\), an infinite infimum makes the right side zero. For \(k=0\), the factor is defined to be one.

**Proof.** Denote the square root of the infimum by \(d_A\). The open unit ball of \(Q^A\) is a bounded convex ellipsoid inside \(\operatorname{ran}B\), and its support function at \(\eta\) is \(Q(B\eta)^{1/2}\), by duality on the quotient used in (G1). The support function of \(RK\) is \(R Q^{-1}(\eta)^{1/2}\).

Choose \(0<a<d_A\). The point \(X\) is outside the open convex set
\(RK+\{Z:Q^A(Z)<a^2\}\). Separation supplies a nonzero \(\eta\), with orientation chosen so that

\[
\langle X,\eta\rangle
\geq RQ^{-1}(\eta)^{1/2}+aQ(B\eta)^{1/2}.                    \tag{G11}
\]

This separation statement also applies when the second ellipsoid is lower dimensional, since \(RK\) makes the sum open in \(E\). Formula (G11) shows that \(L(Y)=\langle Y-X,\eta\rangle\) has no zero in \(RK\), and
\(Q(B\eta)^{1/2}/|L(0)|\leq a^{-1}\).
If \(Q(B\eta)=0\), (G8) already gives \(T_Au(X)=0\), so no division by it is needed. Otherwise (G9) bounds the left side by \(C a^{-k}\) times the indicated derivative norm.

Let \(a\) tend to \(d_A\). When \(d_A=\infty\), let \(a\) tend to infinity, obtaining zero for \(k>0\). For \(d_A\leq1\), use the global estimate (G4) with \(N=0\). Combining that bound with the one for \(d_A>1\) changes the constant by at most \(2^{k/2}\) and proves (G10). ∎

Translations and fixed rescalings of \(K\) give the same estimate for a function supported in \(B_Z(a)\), with its tail measured from a larger ball \(B_Z(b)\), \(0<a<b\). Constants depend on the two radii and their gap. Applying (G10) to a derivative gives the corresponding differentiated estimate, since \(T_A\) commutes with that derivative.

## AN03-GAU-005 — Temperateness based at the observation point

Let \(g\) be slowly varying and let \(m\) be a positive \(g\)-continuous weight in the sense of AN03-U001. Fix an observation point \(X\). The required additional assumptions are

\[
g_X\leq g_X^A,                                                \tag{G12}
\]
\[
g_Y(T)\leq C\,g_X(T)(1+g_Y^A(X-Y))^{N_g},\qquad
m(Y)\leq C\,m(X)(1+g_Y^A(X-Y))^{N_m}.                         \tag{G13}
\]

These hold for every \(Y,T\), with fixed finite exponents \(N_g,N_m\geq0\) and positive constants. This normalization loses no generality: any valid negative exponent can be enlarged to zero because the base \(1+g_Y^A(X-Y)\) is at least one. They are conditions at \(X\); at this stage no such estimate is assumed at another observation point. In particular the phase-dual form on the right is based at **\(Y\)**. Infinite values impose no comparison across the corresponding directions; the inequalities are required on their finite-distance domain.

Reversal of quadratic forms, as in AN03-GAU-001, gives

\[
g_X^A(T)\leq C\,g_Y^A(T)(1+g_Y^A(X-Y))^{N_g};
\]

applying this to \(T=X-Y\) yields

\[
1+g_X^A(X-Y)\leq C'(1+g_Y^A(X-Y))^{N_g+1}.                  \tag{G14}
\]

All useful estimates here are on the common finite domain \(\operatorname{ran}B\); elsewhere the extended-valued inequality has its evident meaning. If \(B\) is invertible, dualizing once more shows the equivalence of the metric condition in (G13) and the displayed phase-dual comparison. We make no such equivalence claim for a degenerate \(B\), since a restriction to \(\operatorname{ran}B\) need not determine a quadratic form on all of \(E\).

Write \(h(Y)=h_{g_Y}\), using (G3). When \(A\ne0\), \(h\) is positive. It is \(g\)-continuous because comparable metrics give comparable \(h\)'s. More precisely, if \(g_Y\leq M g_X\), then \(g_Y^{-1}\geq M^{-1}g_X^{-1}\), and the first formula in (G3) gives \(h(Y)\leq Mh(X)\). Thus (G13) implies

\[
h(Y)\leq C h(X)(1+g_Y^A(X-Y))^{N_g}.                         \tag{G15}
\]

This argument does not differentiate the possibly nonsmooth metric. Assumption (G12) says \(h(X)\leq1\).

## AN03-GAU-006 — Counting localization balls by their phase distance

Choose a partition \((\phi_\nu)\) from AN03-U001, with support balls \(B_{X_\nu}(a)\), and choose fixed larger radii
\(0<a<b<c<r_*\). Write \(U_\nu=B_{X_\nu}(b)\) and \(U'_\nu=B_{X_\nu}(c)\). These three families have uniformly bounded multiplicity and are locally finite. Set

\[
d_\nu(X)=\inf_{Y\in U_\nu}g_{X_\nu}^A(X-Y).                  \tag{G16}
\]

**Lemma.** Under (G12) and the metric part of (G13), there are constants \(C,L\), depending only on dimension, the three radii and metric structural constants, for which

\[
\#\{\nu:d_\nu(X)\leq t\}\leq Ct^L\quad(t\geq1).
                                                               \tag{G17}
\]

Consequently \(\sum_\nu(1+d_\nu(X))^{-M}\leq C_M\) for any \(M>L\), uniformly when the structural constants are uniform. Terms with \(d_\nu=\infty\) are zero.

**Proof.** Use linear coordinates in which \(g_X\) is Euclidean. For each index being counted choose \(Y_\nu\in U_\nu\) with
\(g_{X_\nu}^A(X-Y_\nu)\leq2t\); using \(2t\) avoids any need for attainment. Slow variation compares \(g_{Y_\nu}\) with \(g_{X_\nu}\), hence also their phase-dual forms. Thus
\(g_{Y_\nu}^A(X-Y_\nu)\leq C_1t\).
Equations (G13)–(G14) and (G12) now imply

\[
g_{X_\nu}\leq C_2t^{N_g}g_X,\qquad
g_X(X-Y_\nu)\leq C_3t^{N_g+1}.                              \tag{G18}
\]

Every Euclidean ball centered at \(Y_\nu\) of radius
\(\kappa t^{-N_g/2}\), with a sufficiently small structural \(\kappa>0\), lies in \(U'_\nu\): its \(g_{X_\nu}\)-radius is less than the gap \(c-b\). These balls have the bounded multiplicity of the \(U'_\nu\)'s. Their centers, by (G18), lie in a Euclidean ball of radius \(C_4t^{(N_g+1)/2}\), and the small balls lie in a fixed constant enlargement of it. Integrating their characteristic functions and dividing by their common volume gives

\[
\#\{\nu:d_\nu(X)\leq t\}
\leq C_5t^{d(2N_g+1)/2}.
\]

This argument first applies to any finite subcollection and therefore also bounds the entire set. It proves (G17) with \(L=d(2N_g+1)/2\). Split indices into \(d_\nu\leq1\) and the dyadic bands \(2^j<d_\nu\leq2^{j+1}\). The band contribution is at most \(C2^{(j+1)L}2^{-jM}\); the resulting geometric series converges for \(M>L\). ∎

## AN03-GAU-007 — Evaluation, derivatives and the correct continuity

**Theorem.** Under (G12)–(G13), the map \(u\mapsto T_Au(X)\) on \(C_c^\infty(E)\) has a unique continuous extension to \(S(m,g)\) which is continuous on each bounded subset when that subset is given the \(C^\infty_{\rm loc}\) topology. For some finite \(J\),

\[
|T_Au(X)|\leq C m(X)p_{\leq J}(u;m,g).                       \tag{G19}
\]

The constants and \(J\) depend only on the metric/weight structural constants and dimension.

**Proof.** Put \(u_\nu=\phi_\nu u\). The localization estimate of AN03-U001 and (G10), with the gap between the support radius \(a\) and \(b\), give

\[
|T_Au_\nu(X)|
\leq C_k m(X_\nu)p_{\leq s+k}(u;m,g)
(1+d_\nu(X))^{-k/2}.                                       \tag{G20}
\]

For finite \(d_\nu\), choose a point nearly attaining (G16). Local comparison and the weight part of (G13) give
\(m(X_\nu)\leq C m(X)(1+d_\nu(X))^{N_m}\), with a harmless change of constant. For infinite \(d_\nu\), (G10) makes the left side of (G20) zero. Choose \(k\) so that \(k/2-N_m>L\), where \(L\) comes from (G17). The series \(\sum_\nu T_Au_\nu(X)\) converges absolutely and gives (G19).

Its majorant is uniform for \(u\) in a bounded set of \(S(m,g)\). Each finite partial sum is continuous in \(C^\infty_{\rm loc}\), since each \(\phi_\nu u\) has fixed compact support and (G4) gives a finite derivative bound for its image at \(X\). Uniform convergence of these continuous functions on the bounded set proves the stated continuity. If \(u\) has compact support, the partition sum is finite and agrees with the original \(T_Au(X)\). Finally, the bounded compactly supported approximation in AN03-MET-007 shows uniqueness: any extension with this bounded-set continuity must take the limit of the same compactly supported partial sums. This also proves independence of the chosen partition. ∎

This bounded-set continuity is called weak continuity in this course's symbol estimates. It is stronger than merely specifying a continuous functional on the Fréchet symbol space: compactly supported functions need not be dense in that Fréchet topology.

For fixed directions \(T_1,\ldots,T_l\), let
\(m_T(Y)=m(Y)\prod_jg_Y(T_j)^{1/2}\).
If a direction is zero the derivative statement below is trivial; otherwise \(m_T\) is positive and satisfies local continuity and the weight condition (G13), with exponent \(N_m+lN_g/2\). The function
\(v=\partial_{T_1}\cdots\partial_{T_l}u\) obeys
\(p_j(v;m_T,g)\leq p_{j+l}(u;m,g)\).
Using (G19) for \(v\) and commuting derivatives first gives the following estimate for compactly supported \(u\):

\[
|\partial_{T_1}\cdots\partial_{T_l}T_Au(X)|
\leq C_lm(X)\prod_jg_X(T_j)^{1/2}
p_{l\leq j\leq J_l}(u;m,g).                                \tag{G21}
\]

The notation on the right means the maximum of exactly that finite range of seminorms. No lower derivative seminorm is needed.

For a general symbol at a single distinguished observation point, the left side of (G21) denotes the jet value defined by \(T_A(\partial_{T_1}\cdots\partial_{T_l}u)(X)\). No derivative of a function defined only at one point is asserted. Actual tangential derivatives are identified under the uniform subspace hypotheses in the next paragraph.

If the hypotheses hold uniformly for \(X\) in a linear subspace \(E_0\), these formulas define a smooth restriction \(T_Au|_{E_0}\) in \(S(m|_{E_0},g|_{TE_0})\). Here is a justification of smoothness, which is not implicit in pointwise extension. Bounded compactly supported approximants to \(u\) have, by (G21), locally uniformly bounded derivatives of every order on \(E_0\), and each derivative has a pointwise limit by the scalar extension argument. On a compact coordinate box, one additional derivative gives equicontinuity; a finite grid then upgrades pointwise convergence to uniform convergence. The fundamental theorem of calculus identifies the limits as derivatives of one smooth function, successively in every order. Thus the restriction has (G21). The same bounded-derivative argument applied to a convergent net or sequence on a bounded source set proves weak continuity of the restriction. On these bounded sets the usual \(C^\infty_{\rm loc}\) topology is metrizable, so sequential continuity suffices.

## AN03-GAU-008 — The full small-parameter remainder

**Theorem.** Assume (G12)–(G13) uniformly on a linear subspace \(E_0\), and suppose \(A\ne0\). For every integer \(N\geq0\), define

\[
R_Nu=T_Au-\sum_{j<N}(iA(D))^ju/j!.
\]

Then \(R_N:S(m,g)\to S(mh^N,g)|_{E_0}\) is weakly continuous. For every \(l\), some finite \(J_{N,l}\) satisfies

\[
|\partial_{T_1}\cdots\partial_{T_l}R_Nu(X)|
\leq C_{N,l}m(X)h(X)^N
\prod_jg_X(T_j)^{1/2}p_{\leq J_{N,l}}(u;m,g),\quad X\in E_0.
                                                               \tag{G22}
\]

Only dimension, \(N,l\) and the structural metric/weight constants determine the seminorm and estimate. If \(A=0\), then \(R_N=0\) for \(N\geq1\) and \(R_0\) is the identity restriction; this case is stated directly, without treating a zero function as a positive weight.

**Proof.** It suffices initially to consider compactly supported \(u\) and \(l=0\). Use the partition from AN03-GAU-006. At a fixed \(X\), only a bounded number of indices have \(X\in U'_\nu\). For these near indices, slow variation compares \(g_{X_\nu}\) with \(g_X\), the weights with \(m(X)\), and \(h(X_\nu)\) with \(h(X)\). Applying (G5) to \(u_\nu\) in the frozen metric yields

\[
|R_Nu_\nu(X)|\leq C_Nm(X)h(X)^Np_{\leq s+2N}(u;m,g).
\]

Their sum has the same bound with a structural multiplicity factor.

For a far index \(X\notin U'_\nu\), every \(Y\in U_\nu\) satisfies
\(g_{X_\nu}(X-Y)^{1/2}\geq c-b\).
Slow variation between \(Y\) and \(X_\nu\) implies \(g_Y(X-Y)\geq c_0>0\). If \(g_Y^A(X-Y)\) is finite, (G3) and (G15) give

\[
c_0\leq h(Y)^2g_Y^A(X-Y)
\leq C h(X)^2(1+g_Y^A(X-Y))^{2N_g+1}.
\]

Choose \(Y\) nearly attaining (G16) and compare its metric with the center metric. For finite \(d_\nu(X)\) this proves

\[
1\leq C h(X)(1+d_\nu(X))^{N_g+1/2}.                        \tag{G23}
\]

Terms with infinite \(d_\nu\) are zero in (G20). Since \(u_\nu\) vanishes on a neighborhood of \(X\) for every far index, all Taylor-polynomial terms vanish there, and \(R_Nu_\nu(X)=T_Au_\nu(X)\). Multiply the bound (G20) by the \(N\)-th power of (G23), using the right side to bound one from above. After weight comparison it becomes

\[
|R_Nu_\nu(X)|
\leq C m(X)h(X)^Np_{\leq s+k}(u;m,g)
(1+d_\nu(X))^{-k/2+N_m+N(N_g+1/2)}.
\]

Choose \(k\) so that the negative exponent exceeds the counting exponent \(L\). Summation by AN03-GAU-006 proves (G22) for \(l=0\). Notice that the gain was extracted from the fixed separation of the far support, not from an unproved asymptotic summation theorem.

For derivatives, apply this scalar estimate to
\(v=\partial_{T_1}\cdots\partial_{T_l}u\) and the modified weight \(m_T\) used in (G21). The operator \(R_N\) commutes with those derivatives. The modified weight has controlled structural constants, so this gives (G22) for arbitrary \(l\), uniformly in the directions.

Finally, \(h\) is positive, locally \(g\)-continuous, and satisfies (G15), so \(mh^N\) is an allowed target weight on \(E_0\). The continuous differential part of \(R_N\) is already defined on symbols. The weak extension of \(T_A\) from AN03-GAU-007, bounded approximation, and (G22) extend the identity and estimate to every \(u\in S(m,g)\). The locally bounded derivative argument there proves smoothness and weak continuity in the target symbol class. ∎

No conclusion here requires \(h(X)\to0\). If \(h=1\) on a region, the remainder belongs to the same weight class there and the theorem gives no decreasing-order filtration on that region. This is a quantitative Taylor theorem for one operator, not a construction that sums every prescribed formal sequence of symbols.

## AN03-GEX-001 — A degenerate phase and an endpoint

Take \(E=\mathbb R^2\), \(Q=|dX|^2\) and \(A(\Xi)=\tau\Xi_1^2\), with \(\tau\ne0\). Then
\(Q^A(Z)=Z_1^2/\tau^2\) when \(Z_2=0\), and it is infinite otherwise. The Fourier multiplier acts in the first variable only. If a function is supported in the unit disk, the result vanishes for \(|X_2|\geq1\). The infinite-distance case of (G10) captures this exact support restriction rather than merely a large finite decay factor. Meanwhile \(h_Q=|\tau|\); (G5) gives a remainder of order \(|\tau|^N\), uniformly as \(\tau\to0\).

As a different example, \(g_X=Q\) constant and \(m=1\) satisfy the global hypotheses whenever \(h_Q\leq1\). If \(h_Q=1\), (G22) still holds but its factor \(h_Q^N\) is one for every \(N\). No successive order gain can be read into that endpoint.

## AN03-GPS-001 — Problems with solutions

**Problem 1.** Identify exactly where real-valuedness of \(A\) is used.

**Solution.** It makes \(|e^{iA}|=1\), so Fourier multiplication preserves the relevant \(L^2\) modulus and the real-variable Taylor remainder is bounded by \(|A|^N/N!\). It also makes \(B\) a real symmetric map, permitting real orthogonal diagonalization and real affine separating directions. For a complex phase the multiplier may grow exponentially; the proof does not carry over merely by replacing real eigenvalues with complex ones.

**Problem 2.** Why does the proof of (G17) use small balls around \(Y_\nu\), instead of estimating the volume of each whole \(U_\nu\)?

**Solution.** Temperateness based only at the observation point gives the upper form bound in (G18), which ensures a small Euclidean ball fits near \(Y_\nu\). It need not give the two-sided comparison that would control the entire shape of \(U_\nu\). The enlargement gap puts each small ball inside \(U'_\nu\), whose multiplicity is known, and that is sufficient for the integrated counting estimate.

**Problem 3.** In dimension \(d\), suppose the metric exponent in (G13) is \(N_g=2\), the weight exponent is \(N_m=3\), and a remainder of order \(N=4\) is wanted. Give a sufficient tail-iteration requirement.

**Solution.** The proof gives \(L=5d/2\). For the far remainder sum it requires
\(k/2-3-4(2+1/2)>5d/2\), or \(k>5d+26\). Any integer satisfying that strict inequality works, with input derivative order at most \(s+k\) in this part and \(s+8\) in the near part. This is a sufficient structural choice, not an assertion of optimal derivative count.

**Problem 4.** Why does uniqueness in AN03-GAU-007 fail if the bounded-set continuity requirement is simply omitted from the argument?

**Solution.** The compactly supported approximants are bounded and converge locally smoothly, but need not converge in the Fréchet symbol topology. A merely Fréchet-continuous functional therefore cannot be passed through this approximation without a further argument. The proof of uniqueness explicitly uses continuity on the bounded approximating set. This explains the logical need in that proof; it does not by itself construct a second extension in every possible symbol space.

## References and exact claim boundary

The mathematical antecedents include Lars Hörmander's [The Weyl calculus of pseudo-differential operators](https://onlinelibrary.wiley.com/doi/10.1002/cpa.3160320304), *Communications on Pure and Applied Mathematics* 32 (1979), 359–443, and the subsequent metric calculus in Volume III of *The Analysis of Linear Partial Differential Operators*. Nicolas Lerner's [Introduction to the Weyl–Hörmander Calculus](https://webusers.imj-prg.fr/~nicolas.lerner/PSEUDO.2005.pdf) is an additional comparison reference. No prose or proof text from these works is imported.

The unit's remaining audits are exact statement correspondence, an independent proof review and external prerequisite import closure. Weyl composition, general quantization changes, operator continuity/positivity and the full elliptic/boundary course remain separate obligations.
