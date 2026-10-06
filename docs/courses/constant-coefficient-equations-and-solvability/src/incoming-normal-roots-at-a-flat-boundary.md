# Incoming normal roots at a flat boundary

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A partial Fourier–Laplace transform parallel to a boundary leaves a polynomial in its normal frequency. Its degree can be smaller than the total order of the equation. We determine that degree and count its upper and lower roots, including repeated roots and characteristic boundary directions. We then construct the two analytic factors and prove polynomial bounds for their coefficients.

Read [Hyperbolicity and lower order terms](hyperbolicity-and-lower-order-terms.md), [Multiple characteristics and allowed lower order terms](multiple-characteristics-and-allowed-lower-order-terms.md), [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md), [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies the Schwartz Fourier transform; [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html) supplies finite algebra and matrices; [Boundary flux and weak identities](../prerequisites/boundary-flux-and-weak-identities.html) supplies the complex Green identity.

Two prerequisites remain planned in [Distributions, kernels and analytic singularities](../prerequisites/planned-foundation-proofs.html): a homogeneous real-root hyperbolic polynomial has an open convex component cone, every direction in that cone is hyperbolic and its imaginary tube is zero-free; a holomorphic germ of \(z\)-axis order \(d\), whose local zeros for a real parameter \(r\) satisfy \(\operatorname{Im}z\le C|r|\), has total Taylor order at least \(d\). Their full contracts are stated in [Hyperbolicity and lower order terms](hyperbolicity-and-lower-order-terms.md). Uses of those two entries are conditional on their planned proofs.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's treatment of constant-coefficient equations. The linked prerequisite lessons supply the proofs used below.

## Time and boundary normals

Let \(P=\sum_{j=0}^mP_j\) be a nonzero complex polynomial on \(\mathbb R^n\), of total degree \(m\ge1\). Write \(F=P_m\). Let \(N,\theta\) be real and linearly independent. The physical regions are
\[
\begin{gathered}
H_N=\{x:x\cdot N\ge0\},\\
\qquad
 H_\theta=\{x:x\cdot\theta\ge0\}.
\end{gathered}
\tag{1}
\]
Assume \(P\) is hyperbolic in \(N\): \(F(N)\ne0\), and for some real \(\tau_0\),
\[
 P(\xi+i\tau N)\ne0
 \quad(\xi\in\mathbb R^n,\ \tau<\tau_0).
 \tag{2}
\]
The homogeneous principal polynomial is hyperbolic in \(N\). Its cone
\(\Gamma=\Gamma(F,N)\) is the open convex component containing \(N\), relative to the planned homogeneous-cone theorem. The transport argument gives the full zero-free tube
\[
\begin{gathered}
\mathcal T=\{\zeta\in\mathbb C^n:
                \operatorname{Im}\zeta\in\tau_0N-\Gamma\},
 \\
\qquad P(\zeta)\ne0\\
\quad(\zeta\in\mathcal T).
\end{gathered}
\tag{3}
\]
Indeed take the cone direction in the transport argument and a small negative additional \(N\)-shift; openness permits the required splitting. This formulation uses the original barrier, with an open cone.

Let \(m_+,m_-,m_0\) count the positive, negative and zero roots, respectively, of \(t\mapsto F(\theta-tN)\), with multiplicities. All its roots are real, and its degree is exactly \(m\). Put
\[
 d=m_++m_-=m-m_0.
 \tag{4}
\]
The distinction between \(m\) and \(d\) will be essential.

## The exact localization and its leading coefficient

The multivariable vanishing order of \(F\) at \(\theta\) equals \(m_0\). To see this directly from the linked proof, apply [Multiple characteristics and allowed lower order terms](multiple-characteristics-and-allowed-lower-order-terms.md)'s multiple-characteristic statement to the homogeneous polynomial \(F\) itself, with the zero root of \(F(\theta+tN)\). It says that every derivative of total order below \(m_0\) vanishes at \(\theta\). The derivative \(\partial_N^{m_0}F(\theta)\) is nonzero by the definition of line multiplicity. Consequently
\[
\begin{gathered}
G(\zeta)=
 \sum_{|\alpha|=m_0}
     \frac{\partial^\alpha F(\theta)}{\alpha!}\zeta^\alpha,
 \\
\qquad
 G(N)\ne0.
\end{gathered}
\tag{5}
\]
When \(m_0=0\), \(G=F(\theta)\ne0\). Thus the limit
\[
 \varepsilon^{-m_0}F(\theta+\varepsilon\zeta)
       \longrightarrow G(\zeta)
 \tag{6}
\]
exists in coefficients. No assertion of simple principal roots is required.

For every real \(\eta\), the polynomials
\(\varepsilon^{-m_0}F(\theta+\varepsilon(\eta+zN))\) have only real zeros in \(z\). They converge to \(G(\eta+zN)\), of degree \(m_0\) and nonzero leading coefficient \(G(N)\). A hypothetical nonreal zero has a small surrounding circle disjoint from the real axis and with zero-free boundary. [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md)'s Rouché theorem would give a zero of the approximating polynomial there, a contradiction. Therefore \(G\) is homogeneous hyperbolic in \(N\), including the constant convention at \(m_0=0\).

Apply [Multiple characteristics and allowed lower order terms](multiple-characteristics-and-allowed-lower-order-terms.md) instead to the full hyperbolic polynomial \(P\), at the same principal-line root. For its degree-\(j\) part it supplies
\[
 \partial^\alpha P_j(\theta)=0
 \quad\text{if }|\alpha|<m_0+j-m.
 \tag{7}
\]
A nonpositive requested order imposes no condition; a constant component is included whenever that order is positive. Homogeneity and the finite Taylor formula now give
\[
\begin{gathered}
\varepsilon^d P(\zeta+\theta/\varepsilon)
  \\
=\sum_{j=0}^m\sum_\alpha
      \varepsilon^{d-j+|\alpha|}
      \frac{\partial^\alpha P_j(\theta)}{\alpha!}\zeta^\alpha.
\end{gathered}
\tag{8}
\]
Every coefficient with a negative exponent of \(\varepsilon\) is zero by 7. Hence the nonzero polynomial limit is
\[
 q(\zeta)=
 \sum_{j=0}^m
 \sum_{\substack{|\alpha|=j-d\\
|\alpha|\ge0}}
       \frac{\partial^\alpha P_j(\theta)}{\alpha!}\zeta^\alpha.
 \tag{9}
\]
Its degree is \(m_0\), its principal part is \(G\), and its existence has been proved without discarding lower-order terms.

Expand \(P(\zeta+w\theta)=\sum_r A_r(\zeta)w^r\). 8 is also
\(\sum_r A_r(\zeta)\varepsilon^{d-r}\). Existence of the limit at every complex \(\zeta\) implies \(A_r=0\) for \(r>d\) and \(A_d=q\). Conversely \(q\ne0\) shows that the polynomial has degree \(d\) at every \(\zeta\) with \(q(\zeta)\ne0\). The top coefficient is unchanged by translating \(w\), so
\[
 q(\zeta+a\theta)=q(\zeta)
 \quad(a\in\mathbb C).
 \tag{10}
\]
For precision, translating a degree-at-most-\(d\) polynomial in \(w\) does not change its \(w^d\) coefficient. This proves the identity first directly for every complex \(a,\zeta\); no continuation across an exceptional fiber is being assumed.

## Zero exclusion and the root count

For each positive \(\varepsilon\), the polynomial in 8 is nonzero throughout \(\mathcal T\), because its additional shift \(\theta/\varepsilon\) is real. Its locally uniform limit \(q\) is also nonzero there. Here is a local proof of this form of Hurwitz. If \(q(\zeta_*)=0\), choose a complex line through \(\zeta_*\) on which the polynomial restriction of \(q\) is not identically zero; such a line exists because \(q\) is a nonzero polynomial. A small line disk stays in the open tube, has a zero at its center and has zero-free boundary. Uniform convergence and Rouché put a zero of 8 inside it, contradicting zero exclusion. Thus, using 10 as well,
\[
 q(\zeta)\ne0
 \quad\text{if }\operatorname{Im}\zeta
       \in\tau_0N-\Gamma+\mathbb R\theta .
 \tag{11}
\]
To pass to the enlarged region subtract \(ia\theta\) for the appropriate real \(a\); the value of \(q\) is unchanged.

For \(\zeta\in\mathcal T\), the polynomial \(w\mapsto P(\zeta+w\theta)\) has degree \(d\) and leading coefficient \(q(\zeta)\ne0\). It has no real root, by 3. Its numbers of roots in the two open halfplanes are locally constant as functions of \(\zeta\). In a small parameter neighborhood the leading coefficient stays away from zero, so the elementary root bound puts all roots in a common disk; disjoint circles around its upper and lower root clusters and Rouché retain their counts. Roots therefore neither cross the real axis nor escape at a finite parameter point.

The tube is convex and hence connected, so these counts are constant. Determine them at \(\zeta=-iTN\), for sufficiently large positive \(T\). With \(w=TW\),
\[
\begin{gathered}
(i/T)^mP(-iTN+TW\theta)
       \\
\longrightarrow F(N+iW\theta).
\end{gathered}
\tag{12}
\]
The limit has degree exactly \(d\) and nonzero leading coefficient: this follows either from 5–9, or from the following factorization. If \(t_1,\ldots,t_m\) are the real roots of \(F(\theta-tN)\), then
\[
\begin{gathered}
F(N+iW\theta)
       \\
=F(N)\prod_{\ell=1}^m(1+iWt_\ell).
\end{gathered}
\tag{13}
\]
This identity first follows for \(W\ne0\) by homogeneity and the factorization of \(F(\theta+zN)\), and then holds polynomially at \(W=0\). A zero \(t_\ell=0\) contributes the constant factor one. A nonzero \(t_\ell\) gives the root \(W=i/t_\ell\), which is upper precisely when \(t_\ell>0\), and lower precisely when \(t_\ell<0\).

12 converges in coefficients with the same final degree \(d\) and nonzero limiting leading coefficient. Root persistence gives the same upper and lower counts for large \(T\), and positive real rescaling \(w=TW\) preserves their signs. Constancy on the tube proves
\[
\begin{gathered}
\#\{\operatorname{Im}w>0:P(\zeta+w\theta)=0\}\\
=m_+,\\
\#\{\operatorname{Im}w<0:P(\zeta+w\theta)=0\}\\
=m_-.
\end{gathered}
\tag{14}
\]
Both counts include multiplicities. This proves all assertions of the normal-root theorem. If \(d=0\), there is no root to count, \(P\) is independent of the \(\theta\)-frequency, and the same argument reads as an empty product.

## Analytic upper and lower factors

For \(\zeta\in\mathcal T\), group the roots according to their strict halfplane signs and define the monic polynomials \(P_+(w,\zeta)\) and \(P_-(w,\zeta)\). Their degrees are \(m_+\) and \(m_-\), respectively, and
\[
 P(\zeta+w\theta)
       =q(\zeta)P_+(w,\zeta)P_-(w,\zeta).
 \tag{15}
\]
Each factor's coefficients are holomorphic functions of \(\zeta\), even when individual roots coalesce. Around a fixed parameter choose a finite union of disjoint small circles around its distinct upper roots, with all disks in the upper halfplane. On a small parameter neighborhood their boundaries stay zero-free and retain all upper roots. The integrals
\[
\begin{gathered}
\sigma_k(\zeta)=\frac1{2\pi i}
       \\
\int_{\mathcal C_+}
            w^k\,\frac{\partial_wP(\zeta+w\theta)}
                         {P(\zeta+w\theta)}\,dw,
 \\
k=1,\ldots,m_+,
\end{gathered}
\tag{16}
\]
are their power sums counted with multiplicity, by [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md)'s weighted argument principle. Compact contour differentiation makes them holomorphic. Newton's elementary identities express the elementary symmetric coefficients recursively in these power sums, dividing only by the positive integers \(1,\ldots,m_+\). Thus the coefficients of \(P_+\) are holomorphic. The lower factor has the same proof. On overlaps the selected multisets are the same, so the coefficients agree; this gives global factors without choosing global individual root labels. A degree-zero factor is the constant one.

For real \(a\), root translation and monicity give
\[
 P_\pm(w,\zeta+a\theta)=P_\pm(w+a,\zeta).
 \tag{17}
\]
Real translation is stipulated here because it preserves the halfplane splitting.

## A uniform polynomial coefficient bound

A translation \(P(\zeta)\mapsto P(\zeta+i(\tau_0-1)N)\) changes its barrier to one and leaves the principal part, \(m_\pm,m_0\) and \(d\) unchanged. Its localization is translated in the same way. Work with this normalized polynomial and write it again as \(P\), so \(\tau_0=1\). The smaller tube
\[
 \mathcal T_0=\{\zeta:\operatorname{Im}\zeta\in-\Gamma\}
       \subset\mathcal T
 \tag{18}
\]
is included because \(\eta+N\in\Gamma\) for \(\eta\in\Gamma\).

We need a lower bound for \(q\) uniform throughout this tube. Fix \(\zeta=\xi-i\eta\), with \(\xi\) real and \(\eta\in\Gamma\). For every real \(b<1\), \(q(\zeta+ibN)\ne0\): its imaginary part is \(bN-\eta=N-(\eta+(1-b)N)\), which lies in \(N-\Gamma\). The polynomial \(z\mapsto q(\zeta+zN)\) has degree \(m_0\) and leading coefficient \(G(N)\). If \(z=a+ib\) is a root, absorb \(aN\) into the real vector \(\xi\); zero exclusion forces \(b\ge1\). Its factorization at \(z=0\) therefore gives
\[
 |q(\zeta)|\ge |G(N)|
 \quad(\zeta\in\mathcal T_0).
 \tag{19}
\]
For \(m_0=0\), the same formula is equality for the nonzero constant \(q=G\).

Let \(J(A)=(\sum_k|A^{(k)}(0)|^2)^{1/2}\) for a one-variable polynomial. [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md)'s product lemma applies to arbitrary complex coefficients at zero, so
\[
\begin{gathered}
J(P_+(\cdot,\zeta))\,J(P_-(\cdot,\zeta))
 \\
\le C|q(\zeta)|^{-1}J(P(\zeta+\cdot\,\theta))
 \\
\le C' S_P(\zeta).
\end{gathered}
\tag{20}
\]
Here \(S_P(\zeta)\) denotes the same finite derivative-vector norm evaluated at a complex point. The second inequality follows from 19 and
\(\partial_w^kP(\zeta+w\theta)|_{w=0}=\partial_\theta^kP(\zeta)\), a fixed linear combination of its multivariable derivatives. The constants depend on \(P,\theta\) and the fixed degrees, not on \(\zeta\).

Each monic degree-\(a\) polynomial satisfies \(J\ge a!\), including \(0!=1\). Consequently 20 bounds both factors separately, and
\[
\begin{gathered}
\sum_{k=0}^{m_+}|\partial_w^kP_+(0,\zeta)|
 \\
\sum_{k=0}^{m_-}|\partial_w^kP_-(0,\zeta)|
 \\
\le C'' S_P(\zeta)
 \\
\le C'''(1+|\zeta|)^m
 \\
(\zeta\in\mathcal T_0).
\end{gathered}
\tag{21}
\]
The passage from Euclidean sums to absolute sums uses only their fixed finite lengths. Dividing the \(k\)-th derivative by \(k!\) bounds every coefficient. The proof gives a bound up to the cone's boundary approached from within; it introduces no reciprocal distance loss. This is precisely the coefficient control needed before forming parameter-dependent boundary determinants.

## Exercises with complete solutions

**Exercise 1 (entry: both orientations).** Take \(F(\xi,s)=s^2-\xi^2\), \(N=(0,1)\), and \(\theta=(1,a)\), where \(a\) is real. Determine the three principal counts, the normal degree, and the leading normal coefficient in the timelike, spacelike and characteristic cases.

**Solution.** The principal-line polynomial is \((a-t)^2-1\), with roots \(a-1,a+1\). If \(a>1\), both are positive, so \((m_+,m_-,m_0)=(2,0,0)\); if \(a<-1\), the count is \((0,2,0)\); and if \(|a|<1\), it is \((1,1,0)\). In all three cases \(d=2\) and \(q=a^2-1\). At \(a=1\), the roots are \(0,2\), so the count is \((1,0,1)\), \(d=1\), and Taylor expansion gives \(q(\xi,s)=2(s-\xi)\). At \(a=-1\), the roots are \(0,-2\), so the count is \((0,1,1)\), \(d=1\), and \(q(\xi,s)=-2(s+\xi)\). These formulas also follow by expanding \(F((\xi,s)+w(1,a))\). On the negative time tube \(s=-iT,\xi=0\), the characteristic upper case has root \(w=iT/2\), while the characteristic lower case has root \(w=-iT/2\). A zero principal root removes a normal mode; it does not create a real root in the permitted complex tube.

**Exercise 2 (intermediate: complex lower terms at a characteristic boundary).** Let
\[
\begin{gathered}
P(\xi,s)=(s-\xi+i)(s+\xi+2i),\\
\qquad
 N=(0,1),\\
\quad\theta=(1,1).
\end{gathered}
\tag{22}
\]
Compute \(q\), the upper factor and the lower factor for a suitable tube. Check directly why the imaginary displacement of the lower-order terms does not alter the count.

**Solution.** The principal polynomial is again \(s^2-\xi^2\), so \(m_+=1,m_-=0,m_0=1\). The full time roots at real \(\xi\) are \(\xi-i\) and \(-\xi-2i\); any barrier below \(-2\) works. Choose \(\tau_0=-3\), with \(\Gamma=\{(\eta_\xi,\eta_s):\eta_s>|\eta_\xi|\}\). Direct expansion yields
\[
\begin{gathered}
P((\xi,s)+w(1,1))
   \\
=(s-\xi+i)(s+\xi+2i+2w),
 \\
q=2(s-\xi+i).
\end{gathered}
\tag{23}
\]
Thus \(P_+=w+(s+\xi+2i)/2\) and \(P_-=1\). In the tube, write \(\operatorname{Im}(\xi,s)=(-\eta_\xi,-3-\eta_s)\), with \(\eta_s>|\eta_\xi|\). The root has imaginary part \((1+\eta_s+\eta_\xi)/2>0\). The leading coefficient has imaginary part \(2(-2-\eta_s+\eta_\xi)<0\), so it is nonzero. The limit \(\varepsilon P((\xi,s)+\theta/\varepsilon)\) is the stated \(q\); its linear principal part is \(2(s-\xi)\), and its constant \(2i\) must be retained.

**Exercise 3 (advanced: no normal mode).** Let \(P(\xi,s)=(s+i)^m\), with \(m\ge1\), \(N=(0,1)\) and \(\theta=(1,0)\). Identify every object above and explain what the result says about the number of scalar boundary conditions.

**Solution.** \(F(\theta-tN)=(-t)^m\), so \(m_0=m\) and \(m_+=m_-=d=0\). The localization is \(q=P\), with principal part \(G=s^m\), and \(P(\zeta+w\theta)=P(\zeta)\) is independent of \(w\). Both factors in 15 equal one. A barrier \(\tau_0<-1\) gives the zero-free tube, and the upper and lower counts are empty. The scalar half-line reduction therefore has no decaying homogeneous normal mode to prescribe: its required independent boundary-condition count is zero. Imposing an arbitrary additional scalar boundary datum generally makes the reduction incompatible. This example has positive total order despite zero boundary-normal degree, so replacing \(m_+\) by the total order would give an incorrect count.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Open lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
