# Boundary determinants as causal Fourier kernels

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The determinant of the normal half-line problem is independent of normal frequency. It therefore lives on the projected boundary tube. A representative with zero normal coordinate need not lie in the original zero-free tube; the selected factor must be transported before it is evaluated there. We prove this descent, its global polynomial bound and algebraicity. We also construct the causal distribution from a polynomially bounded tube function, and prove directly that a nonzero algebraic transform cannot hide a positive time gap.

Read [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md), [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md), [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies the Schwartz Fourier transform; [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html) supplies finite algebra and matrices; [Boundary flux and weak identities](../prerequisites/boundary-flux-and-weak-identities.html) supplies the complex Green identity.

Two prerequisites remain planned in [Distributions, kernels and analytic singularities](../prerequisites/planned-foundation-proofs.html): a homogeneous real-root hyperbolic polynomial has an open convex component cone, every direction in that cone is hyperbolic and its imaginary tube is zero-free; a holomorphic germ of \(z\)-axis order \(d\), whose local zeros for a real parameter \(r\) satisfy \(\operatorname{Im}z\le C|r|\), has total Taylor order at least \(d\). Their full contracts are stated in [Hyperbolicity and lower order terms](hyperbolicity-and-lower-order-terms.md). Uses of those two entries are conditional on their planned proofs.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's treatment of constant-coefficient equations. The linked prerequisite lessons supply the proofs used below.

## Normal-frequency descent

Use [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)'s notation after normalizing the barrier to one. An invertible linear coordinate change can put the independent frequency vectors at \(N=e_n\), \(\theta=e_1\); physical coordinates transform dually. Thus write \(\zeta=(\zeta_1,\zeta')\), with \(\zeta'\in\mathbb C^{n-1}\), and let \(\pi\) discard the first coordinate. This choice preserves the pairings with the two original normals. Put
\[
\begin{gathered}
\mathcal T=\{\zeta:\operatorname{Im}\zeta\in N-\Gamma\},
 \\
\quad
 \Omega=\{\zeta':\operatorname{Im}\zeta'\in N'-\pi\Gamma\},
 \\
\quad N'=\pi N .
\end{gathered}
\tag{1}
\]
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

Set
\[
 Y=\pi\Gamma,\qquad
 \Omega_0=\mathbb R^{n-1}-iY\subset\Omega .
 \tag{7}
\]
The localization \(q\) is nonzero on \(\Omega\), by [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)'s extended zero exclusion. For \(\zeta'=\xi'-i\eta'\), \(\eta'\in Y\), choose any real lift \(\eta\in\Gamma\). For \(b<1\), the imaginary part of \((0,\zeta')+ibN\) lies in \(N-\Gamma+\mathbb Re_1\), since \(\eta+(1-b)N\in\Gamma\). [equation 11 in Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md) therefore excludes a zero of \(q(\zeta'+ibN')\). Real translation along \(N'\) absorbs the real part of any putative time-line root. Factoring this degree-\(m_0\) polynomial, with leading coefficient \(G(N)\ne0\), yields
\[
 |q(\zeta')|\ge |G(N)|
 \quad(\zeta'\in\Omega_0).
 \tag{8}
\]
The constant case \(m_0=0\) is included.

Write the left side of 4 as \(\sum_{k=0}^d a_k(\zeta')w^k\), with \(a_d=q\). Every \(a_k\) is a fixed polynomial of degree at most \(m\). 8 bounds all coefficients of the monic polynomial \(P((w,\zeta'))/q(\zeta')\) by \(C(1+|\zeta'|)^m\). The elementary monic root estimate gives
\[
\begin{gathered}
|\rho|\le C'(1+|\zeta'|)^m
 \\
\quad\text{for every root }\rho,\\
\quad \zeta'\in\Omega_0.
\end{gathered}
\tag{9}
\]
Every root of \(R_+\) or \(R_-\) is among these roots, with its multiplicity. Vieta bounds their coefficients by fixed powers of the right side. Thus all transported factor coefficients, pairing entries, maximal determinants and their cofactors satisfy
\[
\begin{gathered}
|A(\zeta')|\le C_A(1+|\zeta'|)^{M_A}
 \\
\quad(\zeta'\in\Omega_0)
\end{gathered}
\tag{10}
\]
for fixed constants and integer exponents. The same holds for any pairing or maximal determinant obtained by appending another fixed polynomial \(B\).

This argument does not require an admissible full-frequency lift of size comparable to \(|\zeta'|\). Such a lift can grow without bound near the edge of the projected cone. The uniform lower bound on \(q\), followed by a root estimate at the transported zero representative, is what gives 10.

## Algebraicity with an explicit nonzero relation

Each maximal determinant above is algebraic over the rational function field \(\mathbb C(\zeta')\). We prove the claim and retain a denominator that can be controlled on \(\Omega_0\).

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
\quad(\zeta'\in\Omega_0).
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

For \(F=L^\partial\), 10 supplies 13 with \(V=Y=\pi\Gamma\). Thus its inverse boundary distribution satisfies
\[
 \operatorname{supp}\mathcal L^\partial
    \subset Y^*
    =\{x':(0,x')\in\Gamma^*\}.
 \tag{18}
\]
The equality follows directly: \(x'\cdot\pi\eta=(0,x')\cdot\eta\). Tensoring this boundary distribution with \(\delta(x_1)\) gives a distribution in full space supported in \(\partial H_\theta\cap\Gamma^*\), with transform \(L\). This is the determinant kernel used in the mixed uniqueness argument.

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

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Open lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, Springer, 1983.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
