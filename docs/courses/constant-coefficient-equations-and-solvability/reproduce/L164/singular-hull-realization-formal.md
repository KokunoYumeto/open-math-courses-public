# Recovering singularities from convolution profiles

Original exposition and proofs: GPT-6.1 Sol (OpenAI), Ultra. CC0 1.0. Self-checked by the writing AI; independent mathematical review is not claimed.

A convolution can remove singularities, even when both inputs are singular. Logarithmic Fourier profiles describe which part of an input's singular geometry survives at a prescribed sequence of frequencies. We first realize any one of these profiles as an exact convolution singular hull. We then turn that realization into a criterion for bounding the singularities of an unknown input, and characterize when singular hulls always add.

Basic references are Tao's *246B, Notes 2* and *245B, Notes 9*, and Hörmander's *The Analysis of Linear Partial Differential Operators I* and *II*. The exact preceding proofs are Locating singularities through logarithmic Fourier strips, Theorem 4.1, for recovery of the convex singular hull; Singularities and nonconvex logarithmic carriers, Theorem 1.1, for localization in a closed union; Convolution and joint frequency carriers, for joint profile sums; Changing centers in Fourier windows, for a neighborhood controlled by one profile; Frequency-selective singularities and smooth convolutions, Theorem 4.1 and Corollary 4.2, for a compact isolated-singularity construction; and Slow decrease and entire Fourier division, Theorem 1.1, for invertibility. These available proofs, rather than an external reference, supply the mathematical inputs.

The polynomial-profile argument also uses Entire logarithms and the approximation of plurisubharmonic functions, for logarithm integrability and zero-set volume, and Local compactness and Hartogs bounds, for the full PSH compactness alternative. The finite-jet description of point-supported distributions is proved here.

## 1. Carriers and singular hulls

For a compact distribution \(u\) on \(\mathbb R^n\), \(n\geq1\), use
\[
 F_u(\zeta)=\langle u,e^{-ix\cdot\zeta}\rangle,\qquad
 L_u(z,c)=\frac{\log|F_u(c+z\log|c|)|}{\log|c|},
 \quad c\in\mathbb R^n,\quad |c|>2.
 \tag{1.1}
\]
A profile is a proper canonical PSH local \(L^1\) limit along an escaping real sequence, or uniform local collapse to \(-\infty\). Write \(\mathcal J(u)\) for the family of their indicators. A proper indicator \(h\) is the support function of a nonempty compact convex carrier \(C_h\). For the collapsed case set \(h=-\infty\) and \(C_h=\varnothing\).

Let
\[
 S_u=\operatorname{conv}(\operatorname{sing\,supp}u).
 \tag{1.2}
\]
The empty hull is empty and its support function is \(-\infty\). For compact nonempty convex sets, write \(H_K(\eta)=\max_{x\in K}x\cdot\eta\). The preceding singular-hull theorem states
\[
 S_u=\overline{\operatorname{conv}
              \bigcup_{h\in\mathcal J(u)}C_h}.
 \tag{1.3}
\]
The preceding nonconvex localization theorem supplies the stronger containment
\[
 \operatorname{sing\,supp}u
       \subset\overline{\bigcup_{h\in\mathcal J(u)}C_h}.
 \tag{1.4}
\]
Neither statement says that each carrier consists entirely of singular points. In particular every individual carrier lies in \(S_u\), although it may contain smooth points inside that hull.

The finite joint-profile theorem lets us extract a profile of a second compact distribution on the same subsequence as a prescribed first profile. With two proper profiles, Fourier multiplication and exact indicator additivity give
\[
 L_{u*w}=L_u+L_w,\qquad C_{u*w}=C_u+C_w.
 \tag{1.5}
\]
Here the carrier notation in the second equality refers to that particular joint profile. A collapsed input makes the convolution profile collapse because the other normalized logarithms have a common upper bound on each parameter compact set.

We use ordinary Minkowski operations on sets. In particular
\[
 K-L=K+(-L)=\{x-y:x\in K,\ y\in L\}.
 \tag{1.6}
\]
This is the difference set, not a set of translations which place all of \(L\) inside \(K\). Addition or difference with an empty set is empty.

## 2. Realizing one prescribed convolution hull

**Theorem 2.1 (isolated singularity with a prescribed output hull).** Let \(u\) be a compact distribution and \(h\in\mathcal J(u)\). For every \(\varepsilon>0\), there is a compact continuous \(w\notin C^1\), supported in \(\overline B_\varepsilon(0)\), such that
\[
 \operatorname{sing\,supp}w=\{0\},\qquad S_{u*w}=C_h.
 \tag{2.1}
\]
The conclusion includes \(h=-\infty\), in which case \(u*w\) is smooth and the output hull is empty.

*Proof for a proper profile.* Choose escaping real centers \(c_j\) with \(L_u(\cdot,c_j)\to V\) properly in local \(L^1\), and let \(h\) be the indicator of \(V\). The expanding-neighborhood theorem gives \(r_j\to\infty\) and
\[
 E=\bigcup_j B_{\mathbb R^n}(c_j,r_j\log|c_j|)
 \tag{2.2}
\]
such that, for a finite Fourier order \(N\), every compact parameter set and every positive tolerance eventually have
\[
 L_u(z,d)\leq N+h(\operatorname{Im}z)+\text{tolerance},
 \qquad d\in E,\quad |d|\to\infty.
 \tag{2.3}
\]
This is a uniform bound on the chosen parameter set, including moving parameter points.

Apply the complete frequency-selective construction to these exact centers and radii, with physical support radius \(\varepsilon\). It supplies a continuous compact \(w\notin C^1\), singular exactly at zero, for which
\[
 L_w(\cdot,d)\longrightarrow-\infty
       \quad(d\notin E,\ |d|\to\infty),
 \qquad
 L_w(\cdot,c_{j_k})\longrightarrow0
       \quad\text{in local }L^1
 \tag{2.4}
\]
on a subsequence of the original centers. The first convergence is uniform on every compact complex parameter set. The construction's support-radius freedom and exact selected-center conclusion are both proved in that earlier chapter.

On the selected subsequence, the product identity gives \(L_{u*w}\to V+0=V\) properly. Thus \(C_h\) actually occurs as one output profile carrier.

We next control every other proper output profile. Suppose \(L_{u*w}(\cdot,d_k)\to Q\) properly. Infinitely many centers outside \(E\) would, by (2.4) and a local common upper bound for \(L_u\), give a collapsed further subsequence. That contradicts the proper \(L^1\) limit \(Q\). Hence a tail lies in \(E\).

Extract joint input profiles along a further subsequence. Neither can collapse, since a collapsed input would collapse the product. Denote their proper limits by \(U,W\). Passing the continuous upper bound (2.3) to the canonical \(L^1\) representative gives
\[
 U(z)\leq N+h(\operatorname{Im}z).
 \tag{2.5}
\]
For completeness, the almost-everywhere limit after an \(L^1\) extraction first gives this inequality almost everywhere. Submean inequalities on small balls, followed by shrinking their radii, give it at every point because the right side is continuous. Dividing (2.5) along the indicator's positive dilation and letting its radius tend to infinity yields \(h_U\leq h\), hence \(C_U\subset C_h\).

Every proper profile carrier of \(w\) lies in \(S_w=\{0\}\) by (1.3). It is nonempty, so \(C_W=\{0\}\). The exact joint addition theorem gives
\[
 C_Q=C_U+\{0\}=C_U\subset C_h.
 \tag{2.6}
\]
All proper output carriers therefore lie in \(C_h\), and one equals \(C_h\). Taking their closed convex hull in (1.3) proves \(S_{u*w}=C_h\).

*Proof for a collapsed profile.* Choose a collapsing sequence for \(u\), its expanding neighborhood \(E\), and the same isolated-singularity construction for \(w\). On escaping centers inside \(E\), \(L_u\) collapses uniformly locally. Outside \(E\), \(L_w\) does so. On each fixed parameter compact set the other input has a common upper bound.
Given any required negative product bound, take the larger of the two frequency thresholds for these regions. The product sum then satisfies that negative bound at every sufficiently large real center, inside or outside \(E\). Consequently all output profiles collapse. The empty-profile Fourier-inversion lemma in the preceding nonconvex localization chapter makes \(u*w\) smooth. Thus \(S_{u*w}=\varnothing=C_h\). This includes \(u=0\). \(\square\)

**Corollary 2.2 (translation of the realization).** The distribution \(w_x(y)=w(y-x)\) is singular exactly at \(x\), has arbitrarily small support about \(x\), and satisfies
\[
 S_{u*w_x}=C_h+x.
 \tag{2.7}
\]
For an empty carrier, its translate remains empty.

*Proof.* Translation multiplies the transform by \(e^{-ix\cdot\zeta}\), so adds \(x\cdot\operatorname{Im}z\) to each normalized logarithm. It translates the singular support and every proper carrier by \(x\). Convolution commutes with this translation. Apply Theorem 2.1. \(\square\)

## 3. An exact criterion for bounding the unknown singularities

**Theorem 3.1 (the inverse singular-support criterion).** Fix a compact distribution \(u\), and nonempty compact convex sets \(K,K'\) with support functions \(H,H'\). The following assertions are equivalent:

1. For every compact distribution \(w\),
   \[
   \operatorname{sing\,supp}(u*w)\subset K
       \quad\Longrightarrow\quad
   \operatorname{sing\,supp}w\subset K'.
   \tag{3.1}
   \]
2. For every \(h\in\mathcal J(u)\) and every \(x\in\mathbb R^n\),
   \[
   h(\eta)+x\cdot\eta\leq H(\eta)\quad
       \text{for all }\eta\in\mathbb R^n
       \quad\Longrightarrow\quad x\in K'.
   \tag{3.2}
   \]

The extended inequality for \(h=-\infty\) holds for every \(x\). Either equivalent assertion therefore requires \(u\) to be invertible.

*Proof of necessity.* Suppose (3.1). Given \(h,x\) satisfying the inequalities in (3.2), use the translated realization \(w_x\) of Corollary 2.2. For proper \(h\), its output hull \(C_h+x\) has support function \(h(\eta)+x\cdot\eta\), so is contained in \(K\). Support functions determine compact convex containment by separation, as proved in the preceding support-function chapter. The singular support is contained in its hull, hence lies in \(K\). For collapsed \(h\), the output is smooth, so its empty singular support also lies in \(K\).
Apply (3.1). The input has singular support exactly \(\{x\}\), giving \(x\in K'\). Thus (3.2) holds.

*Proof of sufficiency.* Assume (3.2), and suppose the output singular support lies in \(K\). Take any proper input profile of \(w\), with indicator \(h_w\) and carrier \(C_w\). The finite joint-profile projection theorem supplies an indicator \(h\in\mathcal J(u)\) along a further extraction on the same frequency sequence.

There is no collapsed indicator in \(\mathcal J(u)\): such an indicator would make the premise of (3.2) true for every real \(x\), forcing the compact set \(K'\) to contain \(\mathbb R^n\), impossible. Thus the joint \(u\) profile is proper. Their sum is a proper output profile, whose carrier is contained in the output hull, and that hull is contained in \(K\). Therefore
\[
 h(\eta)+h_w(\eta)\leq H(\eta)\quad(\eta\in\mathbb R^n).
 \tag{3.3}
\]
For every \(x\in C_w\), \(x\cdot\eta\leq h_w(\eta)\). Hence (3.3) gives the premise of (3.2), proving \(C_w\subset K'\).
All proper profile carriers of \(w\) lie in \(K'\). Taking their closed convex hull in (1.3), including the empty case, gives \(S_w\subset K'\), so its singular support lies there as required.

The absence of a collapsed \(u\) profile is exactly the first slow-decrease criterion in the preceding entire-division theorem. It proves the asserted invertibility requirement. \(\square\)

The criterion uses every profile of the fixed known input. Replacing their family by its largest singular hull can lose information.

## 4. A sharper localization before convexification

For nonempty compact convex \(K\), define the set of admissible singular-point translations
\[
 T_K(u)=\{x\in\mathbb R^n:
       \text{some }h\in\mathcal J(u)
       \text{ satisfies }h(\eta)+x\cdot\eta\leq H_K(\eta)
       \text{ for all }\eta\}.
 \tag{4.1}
\]
For proper \(h\), the inequality says exactly \(C_h+x\subset K\). A collapsed profile makes \(T_K(u)=\mathbb R^n\).

**Proposition 4.1 (nonconvex localization).** If \(\operatorname{sing\,supp}(u*w)\subset K\), then
\[
 \operatorname{sing\,supp}w\subset\overline{T_K(u)}.
 \tag{4.2}
\]
The closure is taken without first forming a convex hull.

*Proof.* If \(u\) has a collapsed profile, the right side is all real space and the assertion follows. Otherwise take any proper \(w\) carrier \(C_w\), and extract its joint proper \(u\) profile as in the proof of Theorem 3.1. Their output carrier lies in \(K\), giving (3.3). For every \(x\in C_w\), \(h+x\cdot\eta\leq H_K\), so \(x\in T_K(u)\).
Thus the union of all proper \(w\) carriers lies in \(T_K(u)\). Apply the actual preceding closed-union localization (1.4), not just its convex-hull version (1.3), and take closures. This proves (4.2). \(\square\)

This stronger conclusion also explains the convex criterion. If every admissible translation lies in the closed convex \(K'\), then its closure lies there and (4.2) gives (3.1).

## 5. When singular hulls always add

**Theorem 5.1 (universal singular-hull addition).** For a compact distribution \(u\), the identity
\[
 S_{u*w}=S_u+S_w\quad\text{for every compact distribution }w
 \tag{5.1}
\]
holds if and only if
\[
 \mathcal J(u)=\{H_{S_u}\}.
 \tag{5.2}
\]
For smooth \(u\), the support function here is \(-\infty\) and the sole indicator is collapsed. For nonsmooth \(u\), the sole indicator is a proper support function.

*Proof of necessity.* For each \(h\in\mathcal J(u)\), realize it by Theorem 2.1 with \(S_w=\{0\}\). Then (5.1) gives
\[
 C_h=S_{u*w}=S_u+\{0\}=S_u.
 \tag{5.3}
\]
For proper \(h\), equality of carriers gives \(h=H_{S_u}\). For collapsed \(h\), (5.3) makes \(S_u\) empty, so \(u\) is smooth.
If \(u\) is smooth, the preceding full logarithmic-strip theorem makes every escaping profile collapse, and \(\mathcal J(u)=\{-\infty\}\). Conversely the profile family is nonempty for any compact distribution, by the compactness alternative on any escaping real sequence. Thus (5.3) yields exactly the singleton family (5.2) in all cases.

*Proof of sufficiency in the empty case.* If \(S_u=\varnothing\), \(u\) is smooth. The convolution with any compact distribution is smooth: differentiate the compact smooth factor in the distribution pairing, with fixed cutoffs on the other compact support. All derivatives pass through that pairing. Hence both sides of (5.1) are empty. This includes \(u=0\).

*Proof of sufficiency in the nonempty case.* Suppose \(S_u\neq\varnothing\) and (5.2). Every \(u\) profile is proper, with carrier exactly \(S_u\). Take any proper \(w\) profile carrier \(C_w\); the finite joint projection theorem realizes it jointly with a \(u\) profile, so \(S_u+C_w\) is an output profile carrier. Conversely every proper output profile has a joint extraction of its inputs. Neither input can collapse, and its carrier is therefore \(S_u+C_w\) for some proper \(w\) carrier. Collapsed \(w\) profiles only give empty output carriers.

If \(w\) has no proper profile, (1.3) makes it smooth and both sides of (5.1) are empty. Otherwise their support functions satisfy
\[
 \begin{split}
 H_{S_{u*w}}(\eta)
 &=\sup_{h_w\in\mathcal J(w),\ h_w\neq-\infty}
                      \bigl(H_{S_u}(\eta)+h_w(\eta)\bigr)\\
 &=H_{S_u}(\eta)+H_{S_w}(\eta).
 \end{split}
 \tag{5.4}
\]
The first and last equalities use (1.3): closing and taking a convex hull do not alter the supremum of a continuous linear functional. The final expression is the support function of the compact convex Minkowski sum. Equality of support functions proves (5.1). \(\square\)

For nonsmooth \(u\), singleton-indicator addition in particular implies invertibility. Invertibility alone excludes collapsed profiles but allows several different proper carriers.

## 6. A uniform difference-set bound for invertible inputs

**Corollary 6.1 (singular-hull subtraction bound).** If \(u\) is invertible, then every compact distribution \(w\) satisfies
\[
 S_w\subset S_{u*w}-S_u.
 \tag{6.1}
\]
The subtraction is the Minkowski difference set (1.6).

*Proof.* An invertible compact distribution is not smooth: a compact smooth transform collapses on every escaping real sequence, violating slow decrease. Thus \(S_u\) is nonempty.
If \(u*w\) is smooth, the smoothing characterization in the preceding frequency-selective chapter implies \(w\) is smooth, since otherwise \(u\) would have a collapsed profile. Both sides of (6.1) are then empty.

Assume now that \(K=S_{u*w}\) is nonempty, and set \(K'=K-S_u\). These are nonempty compact convex sets. Every \(h\in\mathcal J(u)\) is proper and \(C_h\subset S_u\). If a real \(x\) satisfies \(h(\eta)+x\cdot\eta\leq H_K(\eta)\) for all \(\eta\), then
\[
 \begin{split}
 x\cdot\eta
 &\leq H_K(\eta)-h(\eta)\\
 &\leq H_K(\eta)+h(-\eta)\\
 &\leq H_K(\eta)+H_{S_u}(-\eta)
   =H_{K-S_u}(\eta).
 \end{split}
 \tag{6.2}
\]
The middle inequality uses \(h(\eta)+h(-\eta)\geq0\): pick any point of the nonempty carrier, evaluate it in the two opposite directions, and add. The last inequality uses \(C_h\subset S_u\). Support-function separation gives \(x\in K'\).
Thus the geometric criterion of Theorem 3.1 holds for \(K,K'\). It places \(\operatorname{sing\,supp}w\) in \(K'\), and convexity of \(K'\) places its hull there too. This proves (6.1). \(\square\)

No sign restriction on \(h(\eta)\) is used. Individual support values may be negative; only the sum of the opposite values is nonnegative.

## 7. Polynomial symbols concentrated at one point

**Proposition 7.1 (all normalized polynomial profiles are constant).** Let \(P\) be a nonzero polynomial on \(\mathbb C^n\) of degree \(N\), and let \(u=P(-i\partial)\delta_0\), so that \(F_u=P\). Every proper logarithmic profile is a constant \(\tau\in[0,N]\). Every escaping real sequence has a proper extracted profile, so there is no collapsed profile. All its indicators equal zero and all its carriers equal \(\{0\}\).

The assertion is that all occurring constants lie in \([0,N]\), not that every value in that interval occurs for each polynomial.

*Proof.* For \(q=|c|>2\), Taylor expansion gives
\[
 P(c+z\log q)=\sum_{|\alpha|\leq N}b_\alpha(c)z^\alpha,\qquad
 b_\alpha(c)=\frac{\partial^\alpha P(c)}{\alpha!}(\log q)^{|\alpha|}.
 \tag{7.1}
\]
Let \(a(c)=\max_{|\alpha|\leq N}|b_\alpha(c)|\), and put \(p_c(z)=P(c+z\log q)/a(c)\). At least one degree-\(N\) coefficient of \(P\) is nonzero, so its corresponding \(\partial^\alpha P/\alpha!\) is a fixed nonzero constant. Thus \(a(c)>0\), and for fixed positive constants,
\[
 C_1(\log q)^N\leq a(c)\leq C_2(1+q)^N.
 \tag{7.2}
\]
The upper bound follows from \(|\partial^\alpha P(c)|\leq C_\alpha(1+q)^{N-|\alpha|}\) and \(\log q\leq1+q\). The same formulas apply when \(N=0\).
Every coefficient of \(p_c\) has modulus at most one and their maximum modulus is one.

Given any escaping sequence, finite-dimensional coefficient compactness supplies a subsequence \(p_{c_j}\to p\) locally uniformly, where \(p\) is a nonzero polynomial: the maximum coefficient modulus remains one. By (7.2), after another extraction,
\[
 \frac{\log a(c_j)}{\log|c_j|}\longrightarrow\tau\in[0,N].
 \tag{7.3}
\]
Indeed the lower bound tends to zero after taking this logarithmic ratio, and the upper bound tends to \(N\).

We justify the needed logarithm convergence. The \(\log|p_{c_j}|\) form a locally uniformly upper-bounded PSH family. At a point where \(p\neq0\), their values converge to the finite \(\log|p|\), so uniform local collapse is impossible. Every PSH compactness extraction has a proper local \(L^1\) further limit. On the open set where \(p\neq0\), uniform polynomial convergence implies local uniform convergence of these logarithms. Any proper \(L^1\) limit therefore equals \(\log|p|\) there. The zero set of the nonzero polynomial has real volume zero, by the precise holomorphic-logarithm theorem. The two functions consequently agree almost everywhere.
All possible proper \(L^1\) extractions have this same limit. If convergence failed on one compact observation region, a subsequence whose \(L^1\) distance stayed positive would have a further proper extraction with that limit, a contradiction. Hence
\[
 \log|p_{c_j}|\longrightarrow\log|p|
                  \quad\text{in local }L^1.
 \tag{7.4}
\]
In particular these logarithms have bounded \(L^1\) norms on compact sets. Since \(\log|c_j|\to\infty\),
\[
 L_u(z,c_j)
 =\frac{\log a(c_j)}{\log|c_j|}
       +\frac{\log|p_{c_j}(z)|}{\log|c_j|}
 \longrightarrow\tau
       \quad\text{in local }L^1.
 \tag{7.5}
\]
This produces a proper constant extraction from every escaping sequence and rules out collapse.
If a sequence already has a specified proper profile, applying the same coefficient and scalar extractions to it identifies that profile with a constant in \([0,N]\). The constant's directional indicator is zero, whose unique nonempty compact convex carrier is \(\{0\}\). \(\square\)

**Lemma 7.2 (point support is a finite jet).** A distribution supported at zero is a finite linear combination of derivatives of \(\delta_0\). For a nonzero such distribution, its Fourier polynomial's degree equals its order.

*Proof.* Fix a smooth compact cutoff \(\chi\) equal to one near zero. On a fixed compact neighborhood of its support, continuity of the distribution \(T\) gives an integer \(m\) and constant \(C\) with
\[
 |T(\psi)|\leq C\max_{|\alpha|\leq m}\|\partial^\alpha\psi\|_\infty
 \tag{7.6}
\]
for test functions supported there. Indeed a continuous linear functional on the test-function space restricted to that compact set is bounded on a neighborhood defined by finitely many derivative seminorms; take their largest order and scale the function.

If all derivatives of \(\phi\) through order \(m\) vanish at zero, Taylor's formula with a continuous highest derivative gives
\(\partial^\beta\phi(x)=o(|x|^{m-|\beta|})\) for \(|\beta|\leq m\). Put \(\chi_\varepsilon(x)=\chi(x/\varepsilon)\). Since the difference vanishes near the distribution's support, \(T(\phi)=T(\chi_\varepsilon\phi)\). Leibniz's rule gives, for \(|\alpha|\leq m\), each summand
\[
 \varepsilon^{-|\gamma|}
 (\partial^\gamma\chi)(x/\varepsilon)
 (\partial^{\alpha-\gamma}\phi)(x)
       =o(\varepsilon^{m-|\alpha|})
 \tag{7.7}
\]
uniformly on the shrinking cutoff support. The finite sum is \(o(1)\). The estimate (7.6) therefore gives \(T(\phi)=0\).

Subtract from any test function its degree-\(m\) Taylor polynomial times the fixed cutoff. The remainder has all these jets zero. Thus
\[
 T(\phi)=\sum_{|\alpha|\leq m}
       T\!\left(\chi\,\frac{x^\alpha}{\alpha!}\right)
                  \partial^\alpha\phi(0).
 \tag{7.8}
\]
This is a finite combination of \(\partial^\alpha\delta_0\), whose action is \((-1)^{|\alpha|}\partial^\alpha\phi(0)\). Its Fourier transform is a polynomial, and it is nonzero if \(T\neq0\): the cutoff monomials independently prescribe the finite jets.

Let \(N\) be the largest degree of a nonzero coefficient in that representation. Its action is bounded by derivative seminorms through order \(N\), so its order is at most \(N\). If \(N\geq1\), choose a cutoff monomial \(\phi\) whose degree-\(N\) jet pairs nontrivially with the top-order coefficients and whose lower jets vanish. For
\(\phi_\varepsilon(x)=\varepsilon^N\phi(x/\varepsilon)\), its value under \(T\) is a fixed nonzero constant, while every derivative seminorm through order \(N-1\) tends to zero. No estimate of order \(N-1\) is possible. If \(N=0\), the nonzero distribution is a multiple of \(\delta_0\), of order zero. This proves the order assertion. \(\square\)

**Corollary 7.3 (point-supported polynomial operators).** A nonzero distribution supported at one point \(x_0\) is invertible, has exactly the indicator \(x_0\cdot\eta\), and satisfies
\[
 S_{u*w}=\{x_0\}+S_w
       \quad\text{for every compact distribution }w.
 \tag{7.9}
\]

*Proof.* Translate the point-supported distribution to zero and apply Lemma 7.2. It is a nonzero polynomial differential operator on \(\delta_{x_0}\). Translation adds \(x_0\cdot\operatorname{Im}z\) to Proposition 7.1's constant profiles, so every indicator is \(x_0\cdot\eta\). There is no collapsed profile; the slow-decrease theorem gives invertibility. Its singular hull is \(\{x_0\}\). Theorem 5.1 gives (7.9). \(\square\)

This concerns the singular hull. It does not assert pointwise equality of the two singular-support sets.

## References

- Terence Tao, [246B, Notes 2: Some connections with the Fourier transform](https://terrytao.wordpress.com/2021/01/23/246b-notes-2-some-connections-with-the-fourier-transform/), 2021. Background on support and entire Fourier transforms; its normalization differs from (1.1).
- Terence Tao, [245B, Notes 9: The Baire category theorem and its Banach space consequences](https://terrytao.wordpress.com/2009/02/01/245b-notes-9-the-baire-category-theorem-and-its-banach-space-consequences/), 2009. Background on the isolated-singularity construction in the preceding lesson.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer, 1983. Compact distributions, polynomial symbols and singular support.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, Springer, 1983, Chapter XVI. Convolution profiles and singular-hull bounds. The realization, inverse criterion, nonconvex localization, universal addition and polynomial profile proofs are supplied above.
