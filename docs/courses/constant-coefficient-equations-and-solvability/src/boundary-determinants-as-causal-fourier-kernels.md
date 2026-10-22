# Boundary determinants as causal Fourier kernels

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026.  Public domain (CC0).*

The determinant of the normal half-line problem is independent of normal frequency. It therefore lives on the projected boundary tube. A representative with zero normal coordinate need not lie in the original zero-free tube; the selected factor must be transported before it is evaluated there. We prove this descent, its global polynomial bound and algebraicity. We also construct the causal distribution from a polynomially bounded tube function, and prove directly that a nonzero algebraic transform cannot hide a positive time gap.

Read [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md), [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md), [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies the Schwartz Fourier transform; [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html) supplies finite algebra and matrices; [Boundary flux and weak identities](../prerequisites/boundary-flux-and-weak-identities.html) supplies the complex Green identity.

The homogeneous real-root hyperbolic polynomial component is an open convex cone, every direction in it is hyperbolic, and its imaginary tube is zero-free; [Real roots and their convex component](../AN02-L192.html#4-pass-to-multiple-roots-and-obtain-convexity), Theorem 4.1, gives the full proof. The analytic-order prerequisite is proved in [One-sided root bounds and Taylor order](../AN02-L193.html#4-the-zero-bound-forces-the-taylor-order), Theorem 4.1: a holomorphic germ of \(z\)-axis order \(d\), whose local zeros for a real parameter \(r\) satisfy \(\operatorname{Im}z\le C|r|\), has total Taylor order at least \(d\). Their full contracts are stated in [Hyperbolicity and lower order terms](hyperbolicity-and-lower-order-terms.md). Both analytic inputs therefore have available full proofs.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's treatment of constant-coefficient equations. The linked prerequisite lessons supply the proofs used below.

## Normal-frequency descent

Use the original polynomial, boundary symbols and real barrier \(\tau_0\) of [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md). First prove the assertions in coordinates with \(N=e_n\) and \(\theta=e_1\), without translating any polynomial. Write \(\zeta=(\zeta_1,\zeta')\), with \(\zeta'\in\mathbb C^{n-1}\), and let \(\pi\) discard the first coordinate. Put
\[
\begin{gathered}
\mathcal T=\{\zeta:\operatorname{Im}\zeta\in\tau_0N-\Gamma\},\\
\Omega=\{\zeta':\operatorname{Im}\zeta'\in\tau_0N'-\pi\Gamma\},
\qquad N'=\pi N .
\end{gathered}
\tag{1}
\]
For arbitrary independent original vectors, fix a real invertible matrix \(E\) with \(Ee_1=\theta\), \(Ee_n=N\). The coordinate polynomials are exactly \(P_E(z)=P(Ez)\), \(B_{j,E}(z)=B_j(Ez)\), and the cone is \(\Gamma_E=E^{-1}\Gamma\). The proof in these coordinates applies to these specified polynomials. Physical coordinates are \(y=E^Tx\); the distributional return map and its density Jacobian are given after (24). In the calculation through (24), \(P,B_j\) denote the unshifted polynomials of the coordinate case just stated.

The linear projection of an open convex cone is an open convex cone. Here is the elementary openness check: a ball of radius \(r\) about a lift projects onto a ball of radius \(r\) about its image in these coordinates. Its convexity and positive scaling are preserved by the linear map. In particular \(\pi\Gamma\) contains \(N'\), and \(N'\ne0\).

[Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md) gives the monic analytic factors \(P_\pm(w,\zeta)\), of fixed degrees \(h=m_+\), \(\ell=m_-\), and the nonzero polynomial \(q\), independent of \(\zeta_1\). For real \(a\),
\[
 P_\pm(w,\zeta+a e_1)=P_\pm(w+a,\zeta).
 \tag{2}
\]
Differentiate this identity in real \(a\); holomorphy makes it the complex differential identity
\(\partial_{\zeta_1}P_\pm=\partial_wP_\pm\).
For a fixed \(\zeta'\in\Omega\), its admissible first coordinates form a nonempty connected complex domain: the real part is unrestricted, and the permitted imaginary parts form an open interval, by convexity of the cone. Consequently
\[
 R_\pm(w,\zeta')=
       P_\pm(w-\zeta_1,(\zeta_1,\zeta'))
 \tag{3}
\]
is independent of the admissible choice of \(\zeta_1\). The derivative with respect to this coordinate is zero, and integration along a path in its connected fiber proves independence. The coefficients are holomorphic on \(\Omega\): near any \(\zeta'\) choose a fixed admissible first coordinate and retain it on a small neighborhood. Such local definitions agree on overlaps by the fiber argument.

Their product is the transported factorization
\[
 P((w,\zeta'))=q(\zeta')R_+(w,\zeta')R_-(w,\zeta').
 \tag{4}
\]
It follows from [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)'s factorization with \(w\) replaced by \(w-\zeta_1\). This identity is valid even if \((0,\zeta')\notin\mathcal T\). On the smaller intersection tube where \((0,\operatorname{Im}\zeta')\in-\Gamma\), the transported upper factor is the upper factor at zero normal coordinate. Outside that intersection, it is a selected analytic factor, and its roots need not all lie in the upper halfplane. This distinction preserves the determinant while avoiding an unjustified halfplane assertion.

Let \(B_1,\ldots,B_\mu\) be fixed polynomial boundary symbols. At an admissible full frequency the rectangular boundary matrix is
\[
\begin{gathered}
M_{jk}(\zeta)=\frac1{2\pi i}\\
\int_{\mathcal C}
       \frac{B_j(\zeta+w e_1)w^{k-1}}{P_+(w,\zeta)}\,dw,
 \\
1\le j\le\mu,\ 1\le k\le h .
\end{gathered}
\tag{5}
\]
For a chosen \(h\) rows, call its determinant \(L(\zeta)\). [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md)'s polynomial coefficient formula makes it holomorphic. 2 and simultaneous real translation in [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md) give \(L(\zeta+a e_1)=L(\zeta)\). It is therefore constant on every connected complex first-coordinate fiber, and descends to a holomorphic function \(L^\partial\) on \(\Omega\).

Equivalently, let \(\beta_{\zeta'}\) be [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md)'s coefficient-at-infinity pairing with denominator \(R_+(\cdot,\zeta')\). Then
\[
\begin{gathered}
M^\partial_{jk}(\zeta')=
       \beta_{\zeta'}(B_j((w,\zeta')),w^{k-1}),
 \\
\qquad
 L^\partial=\det M^\partial
 \\
\quad\text{for the selected }h\text{ rows}.
\end{gathered}
\tag{6}
\]
The substitution \(y=w+\zeta_1\) in 5 gives the monomials \((y-\zeta_1)^{k-1}\). Their change from \(y^{k-1}\) is triangular with diagonal one, so each maximal determinant is unchanged. The rectangular matrix's rank is also unchanged, since its columns are multiplied by that invertible triangular matrix. The pairing formula can be computed at infinity and therefore is valid for the transported factor even when its roots are no longer upper. If \(h=0\), the maximal determinant is the empty determinant one.

This proves the full analyticity and normal invariance in the projected determinant statement, including its projected interpretation.

## A bound on the entire projected cone

For each \(a>0\), use the sub-tube
\[
Y=\pi\Gamma,\qquad
\Omega_a=\{\zeta':\operatorname{Im}\zeta'\in(\tau_0-a)N'-Y\}
\subset\Omega .
\tag{7}
\]
The inclusion holds because \(\eta'+aN'\in Y\) whenever \(\eta'\in Y\). Let \(\zeta'=\xi'+i((\tau_0-a)N'-\eta')\) and choose a lift \(\eta\in\Gamma\) of \(\eta'\). For a complex time-line parameter \(z=u+iv\), with \(v<a\), the imaginary part of \((0,\zeta')+zN\), modulo the normal direction, is \(\tau_0N-[\eta+(a-v)N]\). This belongs to the enlarged zero-free region in [equation (11) of Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md). The real part \(uN\) is absorbed in the unrestricted real frequency. Hence every root of \(z\mapsto q(\zeta'+zN')\) has imaginary part at least \(a\). Its degree is \(m_0\), with leading coefficient \(G(N)\ne0\). Evaluation at zero gives
\[
|q(\zeta')|\ge |G(N)|a^{m_0},
\qquad \zeta'\in\Omega_a .
\tag{8}
\]
For \(m_0=0\) the empty root product gives the same assertion.

Write the original polynomial in (4) as \(\sum_{k=0}^d a_k(\zeta')w^k\), with \(a_d=q\). Let \(C_0\ge1\) bound, for every \(a_k\), the sum of the absolute values of its coefficients. Since its degree is at most \(m\), we have \(|a_k(\zeta')|\le C_0(1+|\zeta'|)^m\). The elementary monic root estimate and (8) give
\[
|\rho|\le 1+C_0|G(N)|^{-1}a^{-m_0}(1+|\zeta'|)^m,
\quad \zeta'\in\Omega_a,
\tag{9}
\]
for every normal root, with its multiplicity. Vieta bounds the coefficients of both selected monic factors by finite powers of this expression. The coefficient-at-infinity pairing is a finite polynomial expression in those coefficients and in the original boundary-symbol coefficients, and a determinant is a finite sum of products of pairing entries. Consequently each such expression \(A\), including every maximal determinant and each appended-row determinant, has fixed nonnegative integers \(E_A,M_A\) and a constant \(C_A\) such that
\[
|A(\zeta')|\le C_A
\bigl(1+|G(N)|^{-1}a^{-m_0}\bigr)^{E_A}
(1+|\zeta'|)^{M_A},
\quad \zeta'\in\Omega_a .
\tag{10}
\]
Indeed expand each of those finite polynomial expressions into monomials, apply (9) to each factor, and enlarge the exponents to the largest degrees in the finite list. Degree-zero expressions use empty products. The constants and exponents are determined by the original polynomial and boundary symbols. For each fixed \(a>0\) the bound is uniform on the entire sub-tube. No uniform bound as \(a\downarrow0\) is asserted.

## Algebraicity with an explicit nonzero relation

Each maximal determinant above is algebraic over the rational function field \(\mathbb C(\zeta')\). We prove the claim and retain a denominator that can be controlled on each \(\Omega_a\).

Let \(\rho_1,\ldots,\rho_d\) be the roots, counted with multiplicity, of the monic polynomial \(P((w,\zeta'))/q(\zeta')\). For every subset \(I\subset\{1,\ldots,d\}\) of cardinality \(h\), let \(D_I\) be the determinant computed with the monic denominator \(\prod_{\nu\in I}(w-\rho_\nu)\) and the fixed selected boundary symbols. [equation 17 in Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md) shows that \(D_I\) is a polynomial in the elementary symmetric functions of the selected roots and the polynomial coefficients of the boundary symbols. Form
\[
 \mathcal A(Z,\zeta')=
       \prod_{\substack{I\subset\{1,\ldots,d\}\\
|I|=h}}
                       (Z-D_I).
 \tag{11}
\]
Its coefficients are symmetric polynomials in all \(d\) roots. A permutation of root indices permutes the factors of the product, including repeated equal roots.

For completeness, every symmetric polynomial is a polynomial in the elementary symmetric functions. Order its monomials lexicographically. Symmetry makes the exponent vector of a largest monomial weakly decreasing. If it is \((a_1,\ldots,a_d)\), subtract its coefficient times
\(e_1^{a_1-a_2}e_2^{a_2-a_3}\cdots e_d^{a_d}\).
The largest monomial cancels, with coefficient one in this product. Repeat. Total degree does not increase, so only finitely many exponent vectors are possible and the process terminates. This proof works with coefficients in \(\mathbb C[\zeta']\), or its rational function field.

The elementary symmetric functions of all roots are signed coefficients of \(P/q\). Thus the coefficients of 11 are rational functions whose denominators are powers of \(q\). The selected analytic factor \(R_+\) uses one of the root subsets at every regular parameter, so \(L^\partial\) annihilates 11 there. The equality persists at repeated roots by continuity, or directly by counting root indices with multiplicity. Clearing a sufficiently large power of \(q\) produces
\[
\begin{gathered}
A(Z,\zeta')\in\mathbb C[Z,\zeta'],\\
\qquad
 A(L^\partial(\zeta'),\zeta')=0,
 \\
\quad
 [Z^{\binom dh}]A=q(\zeta')^K\ne0
       \\
\quad(\zeta'\in\Omega).
\end{gathered}
\tag{12}
\]
Here \(K\ge0\) is fixed. The empty normal-product case uses the single empty subset and \(Z-1\). This relation is nonzero, has a leading coefficient known not to vanish on the projected tube, and applies to every appended-row determinant as well. We have not substituted an unverified semialgebraic selection claim for algebraicity.

## Constructing a distribution from a flat tube

We now prove the exact transform statement used for these determinants. Let \(V\subset\mathbb R^r\) be a nonempty open convex cone, and let \(F\) be holomorphic on \(\mathbb R^r-iV\) with a uniform bound
\[
\begin{gathered}
|F(\xi+i\eta)|\le C(1+|\xi+i\eta|)^M,
 \\
\qquad \eta\in-V.
\end{gathered}
\tag{13}
\]
For a compactly supported smooth test function \(\phi\), define, using any such \(\eta\),
\[
\begin{gathered}
\langle T,\phi\rangle
   \\
=(2\pi)^{-r}\int_{\mathbb R^r}
        F(\xi+i\eta)\\
\widehat\phi(-\xi-i\eta)\,d\xi.
\end{gathered}
\tag{14}
\]
The integral is absolutely convergent: the second factor is the Fourier transform of the compact smooth function \(e^{-\eta\cdot x}\phi(x)\), evaluated at \(-\xi\), and decreases faster than every power of \(|\xi|\). 13 makes the pairing a continuous distributional functional on each fixed compact test family.

The result is independent of \(\eta\). Join two imaginary vectors by a segment inside the convex open cone. Along this compact segment the integrand, and its derivatives, decrease faster than a fixed integrable power of \(|\xi|\), uniformly in the segment parameter. For the \(F\) derivatives, use Cauchy's estimate on a common small complex ball whose imaginary parts remain inside the tube; 13 bounds its supremum polynomially in \(|\xi|\). For the test transform derivatives, use compact integration by parts. Holomorphy gives
\[
\begin{gathered}
\frac d{da}\bigl[
 F(\xi+i\eta(a))\\
\widehat\phi(-\xi-i\eta(a))\bigr]
    \\
=i\sum_{k=1}^r\eta_k'(a)\,\partial_{\xi_k}
       \bigl[F(\xi+i\eta(a))
                    \\
\widehat\phi(-\xi-i\eta(a))\bigr].
\end{gathered}
\tag{15}
\]
Integrating over expanding real cubes, their boundary integrals tend to zero by the rapid bounds just proved. Differentiation under the absolutely convergent integral is justified by the same common bound. The integral is constant on the segment.

Let \(T_\eta=\mathcal F^{-1}(F(\cdot+i\eta))\), a tempered distribution by its polynomial growth. 14 states
\[
\begin{gathered}
T=e^{-\eta\cdot x}T_\eta,\\
\qquad
 e^{\eta\cdot x}T=T_\eta
 \\
\quad\text{as distributions}.
\end{gathered}
\tag{16}
\]
The multiplication is initially in ordinary distributions; the second expression is tempered because it equals the explicitly constructed \(T_\eta\). The underlying \(T\) itself is tempered. Indeed take \(\eta\to0\) along a fixed negative cone ray with \(|\eta|\le1\). The bound on \(F(\cdot+i\eta)\) is then \(C'(1+|\xi|)^M\), uniformly. The Schwartz Fourier continuity estimate bounds its inverse pairing by a fixed finite sum of Schwartz seminorms. Apply this to \(e^{-\eta\cdot x}\phi\) in 16 and let \(\eta\to0\); for a fixed compact \(\phi\) these functions converge in every Schwartz seminorm to \(\phi\). Thus \(T\)'s test bound uses those same fixed seminorms, independently of the test support. Compact smooth functions are dense in Schwartz functions: multiplying by a fixed smooth cutoff at radius \(R\), the Leibniz formula and rapid tails make every Schwartz seminorm of the difference tend to zero. The functional therefore extends continuously to the full Schwartz space.

The support is causal in the polar cone
\[
\begin{gathered}
C_V=V^*=\{x:x\cdot\nu\ge0\\
\text{ for all }\nu\in V\},
 \\
\operatorname{supp}T\subset C_V.
\end{gathered}
\tag{17}
\]
If a test support satisfies \(x\cdot\nu\le-\varepsilon<0\) for some \(\nu\in V\), put \(\eta=-R\nu\) in 14. The test factor is the Fourier transform at \(-\xi\) of \(e^{R\nu\cdot x}\phi\). Repeated integration by parts bounds it by
\(C_k(1+R)^{2k}e^{-\varepsilon R}(1+|\xi|)^{-2k}\).
13 contributes at most \(C'(1+R)^M(1+|\xi|)^M\). Choose \(2k>M+r\); the integral tends to zero as \(R\to\infty\). Independence forces its original value to be zero. Every point outside \(C_V\) has such a separating cone vector and a small neighborhood satisfying the strict inequality. This proves 17.

Uniqueness follows from 16 and injectivity of the tempered Fourier transform for any fixed \(\eta\). Differentiation of \(T\) corresponds to multiplication of \(F\) by the same polynomial in \(\xi+i\eta\), directly by integration by parts in 14. If several tube functions depend smoothly on a real parameter with uniform polynomial bounds for each parameter derivative on compact parameter intervals, 14 can be differentiated under its integral. It defines a smooth family of distributions with the same support control, including one-sided endpoint limits. This last assertion uses fixed compact tests and a fixed \(\eta\); no differentiability of a moving contour is needed.

Apply this flat-tube theorem to the original determinant as follows. Fix \(a>0\), set \(b_a=\tau_0-a\), and define
\[
F_a(z')=L^\partial(z'+ib_aN'),
\qquad z'\in\mathbb R^{n-1}-iY.
\tag{18a}
\]
The estimate (10) gives (13), with a constant that also includes \((1+|b_a||N'|)^{M_A}\), since \(1+|z'+ib_aN'|\le(1+|b_a||N'|)(1+|z'|)\). Let \(T_a\) be its tempered inverse from (14)–(17), and define the original boundary kernel
\[
U=e^{-b_aN'\cdot x'}T_a,
\qquad
\operatorname{supp}U\subset Y^*
=\{x':(0,x')\in\Gamma^*\}.
\tag{18}
\]
This multiplication is in ordinary distributions. The kernel \(U\) need not be tempered; the distributions \(T_a\) are the tempered objects proved above. Multiplication by a smooth nowhere-zero exponential preserves support, which proves the inclusion.

The definition is independent of \(a\). For \(a,b>0\),
\[
\begin{gathered}
F_b(z')=F_a(z'+i(a-b)N'),\\
T_b=e^{(a-b)N'\cdot x'}T_a.
\end{gathered}
\tag{18b}
\]
To prove the second identity, take an imaginary vector \(\eta'\) sufficiently deep in \(-Y\) that both \(\eta'\) and \(\eta'+(a-b)N'\) lie there. Such a vector exists on the negative \(N'\)-ray. Formula (16) and Fourier uniqueness on this common slice give
\(e^{\eta'\cdot x'}T_b=e^{(\eta'+(a-b)N')\cdot x'}T_a\) as ordinary distributions. Removing the nowhere-zero multiplier gives (18b), and substitution in (18) proves independence.

For every \(\eta'\in\tau_0N'-Y\), write \(\eta'=\tau_0N'-\nu'\). Openness allows a sufficiently small \(a>0\) with \(\nu'-aN'\in Y\). Thus \(\eta'-b_aN'=aN'-\nu'\in-Y\), and (16) gives the exact original transform identity
\[
\begin{gathered}
e^{\eta'\cdot x'}U\in\mathcal S',\\
\mathcal F(e^{\eta'\cdot x'}U)(\xi')\\
=L^\partial(\xi'+i\eta').
\end{gathered}
\tag{18c}
\]
Every slice in the original projected tube is therefore represented, with its original time barrier. Tensoring \(U\) with \(\delta_0(x_1)\) gives the coordinate-case full kernel supported in \(\partial H_\theta\cap\Gamma^*\).

## A direct algebraic obstruction to a positive time gap

Retain 13 and assume \(V\) contains a vector \(N_0\). Its polar has a strict normal bound
\[
 N_0\cdot x\ge b|x|\quad(x\in C_V)
 \tag{19}
\]
for some \(b>0\), because a ball \(B(N_0,2b)\) lies in \(V\); test the defining polar inequality at \(N_0-bx/|x|\). If \(C_V=\{0\}\), the conclusion below is immediate for a nonzero distribution.

Suppose \(F\) is nonzero and has a polynomial relation whose leading coefficient does not vanish in the tube, as in 12. Choose \(\zeta_*\) there with \(F(\zeta_*)\ne0\). On the ray
\[
 f(R)=F(\zeta_*-iRN_0),\qquad R\ge0,
 \tag{20}
\]
the relation becomes a nonzero polynomial \(A(R,Z)\). For 12 its leading coefficient is a power of \(q(\zeta_*-iRN_0)\), which never vanishes, so this specialization cannot become the zero polynomial.

Remove the largest factor \(Z^a\) from this relation. The resulting relation still annihilates \(f\): it does so where \(f\ne0\), and then at all other points by continuity and analytic identity on the connected ray neighborhoods. Its constant coefficient \(a_0(R)\) is a nonzero polynomial. For sufficiently large real \(R\),
\[
\begin{gathered}
|a_0(R)|\ge cR^{d_0},\\
\qquad
 |a_k(R)|\le C R^D .
\end{gathered}
\tag{21}
\]
If \(|f(R)|\le1\), the relation implies
\(|a_0(R)|\le C'R^D|f(R)|\).
If \(|f(R)|>1\), a polynomial lower bound is already true. Decrease the constant and take \(K\ge\max(D-d_0,0)\). We have
\[
\begin{gathered}
|F(\zeta_*-iRN_0)|\ge c'(1+R)^{-K}
 \\
\quad\text{for all sufficiently large }R.
\end{gathered}
\tag{22}
\]
No supremum attainment, Puiseux curve selection or unstated semialgebraic power theorem is used.

If \(0\notin\operatorname{supp}T\), its closed support stays a positive distance \(\delta\) from zero. 17–19 put it in \(N_0\cdot x\ge c=b\delta>0\). Write \(\zeta_*=\xi_*+i\eta_*\). The distribution \(T_{\eta_*}=e^{\eta_*\cdot x}T\) is tempered and has the same support. Choose a smooth cutoff equal to one on a neighborhood of that support and supported where
\(N_0\cdot x\ge c/2\) and \(N_0\cdot x\ge b_0\langle x\rangle\), for a fixed \(b_0>0\). Such a cutoff is explicit from two smooth one-variable steps applied to \(N_0\cdot x\) and to \(N_0\cdot x/\langle x\rangle\); 19 and the lower distance \(\delta\) give a strictly positive lower ratio on the support. Use slightly smaller thresholds for the cutoff's support.

The test functions
\(\chi(x)e^{-RN_0\cdot x}e^{-i\xi_*\cdot x}\)
are Schwartz for \(R\ge1\). Every fixed Schwartz seminorm is at most a polynomial in \(R\) times \(e^{-cR/4}\): use half of the exponential for the time gap and half for the radial decay on the cutoff cone; derivatives add only fixed powers of \(R\) and bounded or polynomial cutoff derivatives. 16 identifies their pairing with
\[
\begin{gathered}
F(\zeta_*-iRN_0)
   =\langle T_{\eta_*},
       \\
\chi e^{-RN_0\cdot x}e^{-i\xi_*\cdot x}\rangle,
 \\
|F(\zeta_*-iRN_0)|\\
\le C(1+R)^J e^{-cR/4}.
\end{gathered}
\tag{23}
\]
For the equality, 16 gives
\(T_{\eta_*-RN_0}=e^{-RN_0\cdot x}T_{\eta_*}\).
The cutoff-weighted expression is Schwartz in \(x\) with all \(x\)-moments, so its Fourier transform is a smooth function of real frequency. Fourier uniqueness identifies it with the holomorphic function \(F(\cdot+i\eta_*-iRN_0)\); evaluating at \(\xi_*\) proves the formula. The cutoff is one near the distributional support and does not change the pairing.

The exponential estimate contradicts 22. Hence
\[
\begin{gathered}
F\not\equiv0\text{ and algebraic as above}
       \\
\quad\Longrightarrow\\
\quad0\in\operatorname{supp}T.
\end{gathered}
\tag{24}
\]
This proves the exact non-delay step required for the appended-row boundary determinants in the rank-deficiency theorem. 


For the original determinant, the affine substitution (18a) preserves the nonzero polynomial relation (12), with its leading coefficient still nonvanishing on the flat tube. If \(L^\partial\not\equiv0\), (24) applied to \(F_a\) gives \(0\in\operatorname{supp}T_a\). The multiplier in (18) is nowhere zero, so \(0\in\operatorname{supp}U\). Thus the no-delay conclusion holds for the original kernel, even when it is not tempered.

**Simultaneous translation of all symbols.** A barrier-one comparison may be made with \(\sigma=\tau_0-1\),
\[
Q(\zeta)=P(\zeta+i\sigma N),\qquad
Q_j(\zeta)=B_j(\zeta+i\sigma N).
\tag{24a}
\]
The original normal factorization evaluated at the shifted parameter is a monic factorization with the selected upper and lower roots for \(Q\); uniqueness of the monic factors therefore identifies it with that factorization. The coefficient-at-infinity pairing uses the same shifted boundary polynomials. Hence its projected factors, localization, entries and determinants satisfy
\[
q_Q(\zeta')=q_P(\zeta'+i\sigma N'),\qquad
R_{\pm,Q}(w,\zeta')=R_{\pm,P}(w,\zeta'+i\sigma N'),
\]
\[
L_Q^\partial(\zeta')=L_P^\partial(\zeta'+i\sigma N'),
\qquad T_Q=e^{\sigma N'\cdot x'}U.
\tag{24b}
\]
For the kernels, the identity follows on a common Fourier–Laplace slice by (18c) and uniqueness. With \(D=-i\partial\), direct differentiation gives
\[
D(e^{-\sigma N\cdot x}v)
=e^{-\sigma N\cdot x}(D+i\sigma N)v,
\]
\[
Q(D)=e^{\sigma N\cdot x}P(D)e^{-\sigma N\cdot x},\qquad
Q_j(D)=e^{\sigma N\cdot x}B_j(D)e^{-\sigma N\cdot x}.
\tag{24c}
\]
Restriction to the boundary retains the same nonzero exponential. Translating the equation while keeping its boundary operators fixed gives a different boundary problem.

**Return to the original linear coordinates.** For the matrix \(E\) specified before (1), apply the coordinate-case construction to \(P_E,B_{j,E},\Gamma_E\), obtaining \(U_E\). Let \(A=E^{-T}\). The full kernel in the original physical variables is the pushforward
\[
U_{\mathrm{full}}=A_*(\delta_0(y_1)\otimes U_E),\qquad
\langle U_{\mathrm{full}},\phi\rangle
=\bigl\langle U_E,\,y'\mapsto\phi(E^{-T}(0,y'))\bigr\rangle.
\tag{24d}
\]
On each admissible exponentially weighted slice, \(\zeta\cdot E^{-T}y=(E^{-1}\zeta)\cdot y\), so its Fourier–Laplace transform is exactly \(L_E^\partial(\pi(E^{-1}\zeta))\). The operator map follows from \(D_x(v(E^Tx))=E(D_yv)(E^Tx)\): the original equation and every original boundary operator act as \(P_E(D_y)\) and \(B_{j,E}(D_y)\) in these coordinates. For an ordinary full-space density \(f(y)\), change of variables gives \(A_*f=|\det E|f(E^Tx)\). If \(U_E\) has boundary density \(k\), this reads
\[
U_{\mathrm{full}}=|\det E|\,\delta(\theta\cdot x)k((E^Tx)'),
\tag{24e}
\]
or surface density \(|\det E|/|\theta|\) times \(k((E^Tx)')\) on that hyperplane. Formula (24d) defines the pushforward even when no density exists. Polarity gives \((E^{-1}\Gamma)^*=E^T\Gamma^*\), directly from the defining pairings. Thus (24d) has support contained in \(\{x:\theta\cdot x=0\}\cap\Gamma^*\). The invertible map preserves whether zero belongs to the support. The Fourier inverse factor \((2\pi)^{-r}\) remains tied to the coordinate measures in (14); the Jacobian in (24e) accounts for the return to the original variables.

## Exercises with complete solutions

**Exercise 1 (entry: the normalized wave determinant).** Take \(P(\xi,s)=(s-i)^2-\xi^2\), \(N=e_s\), \(\theta=e_\xi\), and \(B(\xi,s)=\xi+\kappa s+c\). Compute the projected factor, determinant and boundary kernel.

**Solution.** The principal cone is \(s>|\xi|\), so \(Y=\{s>0\}\) and \(\Omega_0=\{\operatorname{Im}s<0\}\). There is one upper and one lower mode, \(q=-1\), and
\[
\begin{gathered}
R_+(w,s)=w+s-i,\\
\qquad
 R_-(w,s)=w-s+i,\\
\qquad
 L^\partial(s)=(\kappa-1)s+c+i.
\end{gathered}
\tag{25}
\]
The upper root at the zero representative is \(i-s\), and the scalar pairing evaluates \(B\) at that root. The inverse distribution on the boundary time line is
\((\kappa-1)D_t\delta_0+(c+i)\delta_0\).
It has the correct transform because \(D_t\) multiplies the Fourier transform by \(s\). If \(\kappa=1,c=-i\), the determinant is identically zero: this boundary symbol annihilates the decaying normal mode. Otherwise the kernel is nonzero and supported at the origin, in agreement with 24.

**Exercise 2 (intermediate: a large lift and a transported lower root).** Let
\[
\begin{gathered}
P(w,y,s)\\
=(s-i)(w+s-i)-y^2,\\
N=e_s,\\
\theta=e_w.
\end{gathered}
\tag{26}
\]
Describe the projected cone and factor. Show why the transported root can be lower, and why its bound is nevertheless polynomial on the whole projected tube.

**Solution.** The principal cone is
\(\Gamma=\{s>0,\ w+s>y^2/s\}\), the positive-definite cone of the real symmetric matrix with entries \(s,y,w+s\). It is the component containing \(N\). Projection discards \(w\), and choosing \(w\) sufficiently large shows \(Y=\{(\eta_y,\eta_s):\eta_s>0\}\). The principal line \(F(\theta-tN)=t(t-1)\) has one positive and one zero root. Thus \(h=1,\ell=0,m_0=1\), and
\[
\begin{gathered}
q=s-i,\\
R_+(w,y,s)\\
=w+s-i-\frac{y^2}{s-i},\\
\rho=\frac{y^2}{s-i}-s+i.
\end{gathered}
\tag{27}
\]
For \(\operatorname{Im}s<0\), \(|s-i|\ge1\), so
\[
|\rho|\le |y|^2+|s|+1
\].
At \(y=iA,s=-i\varepsilon\), \(A,\varepsilon>0\),
\(\operatorname{Im}\rho=1+\varepsilon-A^2/(1+\varepsilon)\), which is negative for \(A>1+\varepsilon\). This representative is outside the full zero-free tube when that happens; the selected factor is transported, rather than asserted to remain upper at zero normal coordinate. A full negative-cone lift can require a normal imaginary component of size \(A^2/\varepsilon\), unbounded as \(\varepsilon\downarrow0\). The denominator \(s-i\), whose uniform lower bound is one, avoids any such loss in the projected coefficient bound. For the boundary symbol \(B=w\), \(L^\partial=\rho\) is rational and uniformly polynomially bounded, as predicted.

**Exercise 3 (advanced: algebraicity and a delayed kernel).** In one boundary variable compare \(F(\zeta)=(\zeta-i)^{-k}\), \(k\ge1\), with \(G(\zeta)=e^{-ia\zeta}\), \(a>0\), on the lower halfplane. Find their inverse distributions and explain exactly which hypothesis prevents delay.

**Solution.** The first-order transform is
\(\mathcal F(i\,\mathbf1_{t\ge0}e^{-t})=(\zeta-i)^{-1}\).
Convolving \(k\) such kernels gives
\[
\begin{gathered}
T(t)=\frac{i^k}{(k-1)!}\,
       \mathbf1_{t\ge0}t^{k-1}e^{-t},
 \\
\qquad
 F(-iR)=\frac{i^k}{(R+1)^k}.
\end{gathered}
\tag{28}
\]
The simplex convolution supplies the factorial and retains the phase. This nonzero kernel has the origin in its support and has exactly polynomial transform decay on that ray. The second transform is that of \(\delta_a\), whose support has the positive time gap \(a\). Both functions are holomorphic and bounded by one on the lower halfplane. However \(G(-iR)=e^{-aR}\). If it satisfied a nonzero polynomial relation with nonvanishing leading coefficient on this ray, the constant-coefficient removal argument 21–22 would force a polynomial lower bound, contradicting this exponential decay. Thus it is not algebraic in the required sense. Polynomial tube growth alone proves cone support; algebraicity is the additional condition that forces support to meet the origin.

**Exercise 4 (intermediate: the original barrier and all boundary symbols).** Let \(\tau_0\in\mathbb R\), \(P(\xi,s)=(s-i\tau_0)^2-\xi^2\) and \(B(\xi,s)=\xi+\kappa s+c\). Compute the original determinant and its simultaneous barrier-one translation. Give an original-tube transform whose causal kernel need not be tempered.

**Solution.** The selected projected upper factor is \(w+s-i\tau_0\), so its root is \(i\tau_0-s\) and
\[
L_P^\partial(s)=(\kappa-1)s+c+i\tau_0.
\tag{29}
\]
Put \(\sigma=\tau_0-1\). Then \(Q(\xi,s)=(s-i)^2-\xi^2\), while \(Q_B(\xi,s)=\xi+\kappa s+c+i\kappa\sigma\). Evaluation at the selected root \(i-s\) gives
\[
L_Q^\partial(s)=(\kappa-1)s+c+i+i\kappa(\tau_0-1)
=L_P^\partial(s+i\sigma).
\tag{30}
\]
Keeping \(B\) unshifted instead gives \((\kappa-1)s+c+i\), missing the term \(i\kappa(\tau_0-1)\). For example, \(\kappa=2,c=0,\tau_0=3\) gives the simultaneous determinant \(s+5i\), whereas that different boundary problem gives \(s+i\).

For \(\operatorname{Im}s<\tau_0\), direct integration gives
\[
\mathcal F\bigl(i\mathbf1_{t\ge0}e^{-\tau_0t}\bigr)(s)
=i\int_0^\infty e^{-(\tau_0+is)t}\,dt
=\frac1{s-i\tau_0}.
\tag{31}
\]
When \(\tau_0<0\) this kernel grows exponentially and is not tempered. To see this without a growth criterion, translate a nonnegative compact test supported in \((0,1)\) to \((R,R+1)\); its pairing has size a positive constant times \(e^{-\tau_0R}\), while each fixed finite collection of Schwartz seminorms grows only polynomially in \(R\). Such a bound cannot define a tempered functional. For \(b_a=\tau_0-a\), its weighted kernel is \(i\mathbf1_{t\ge0}e^{-at}\), which is tempered for every \(a>0\), exactly as in (18). The origin belongs to every one of these supports.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Open lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
