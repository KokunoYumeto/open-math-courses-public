# Degenerate boundary symbols and smooth nonuniqueness

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A mixed boundary determinant can be nonzero on every real spatial frequency at a fixed negative imaginary time, yet still fail to determine a smooth causal solution uniquely. Its principal symbol detects a complex frequency branch approaching the time direction. We construct a solution from that branch and show that its support reaches every boundary point of nonnegative time.

Read [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md), [Missing boundary rank produces a causal solution](missing-boundary-rank-produces-a-causal-solution.md), [Two-dimensional evolution roots and model components](two-dimensional-evolution-roots-and-model-components.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies the Schwartz Fourier transform; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies compact extrema and cutoffs; [Convolution as addition of supports](../prerequisites/convolution-as-addition-of-supports.html) supplies proper convolution.

The hyperbolic-cone theorem is proved in [Real roots and their convex component](../AN02-L192.html#4-pass-to-multiple-roots-and-obtain-convexity), Theorem 4.1. The analytic zero-order prerequisite remains planned in [Distributions, kernels and analytic singularities](../prerequisites/planned-foundation-proofs.html); its precise statement is given in [Hyperbolicity and lower order terms](hyperbolicity-and-lower-order-terms.md). The analytic-order uses remain conditional on its planned proof.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's treatment of constant-coefficient equations. The written prerequisite lessons supply the auxiliary proofs used below.

## The statement and selected bases

Use [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md)'s normalized polynomial, [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md)'s projected determinant and [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md)'s principal symbol. Work in coordinates with \(N=e_n,\theta=e_1\), normal position \(a=x_1\), and tangential position \(x'=(z,t)\), where \(t=x_n\). There are \(h=m_+\) boundary symbols \(B_1,\ldots,B_h\), and
\[
\begin{gathered}
L^\partial\not\equiv0,\\
\qquad
 \widehat\Lambda_0(N')=0,\\
\qquad
 H=\{t\ge0\},\\
\quad H'=\{a\ge0\}.
\end{gathered}
\tag{1}
\]
**Theorem.** There is a function \(u\), jointly smooth up to the boundary of \(H'\), which is zero for \(t<0\), solves \(P(D)u=0\) in \(a>0\), and satisfies every homogeneous boundary condition \(B_j(D)u|_{a=0}=0\). Moreover every point of \(H\cap\partial H'\) belongs to its support. Its initial jets therefore vanish at \(t=0\), but it is nonzero.

This proves the smooth nonuniqueness theorem. [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md) supplies analytic scaling at a characteristic boundary and its invariant principal symbol; [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md) supplies the residue pairing; [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md) and [Missing boundary rank produces a causal solution](missing-boundary-rank-produces-a-causal-solution.md) supply upper-root bounds and the cofactor construction. The [Two-dimensional evolution roots and model components](two-dimensional-evolution-roots-and-model-components.md) finite-cover proof is used only for its path/grid continuation mechanism. We prove here the required analytic-germ coefficient adapter rather than importing a general Puiseux or Weierstrass theorem. The linked Fourier, polynomial and matrix, finite-coordinate and Cauchy lessons supply the auxiliary results. The cone theorem is available in [Real roots and their convex component](../AN02-L192.html#4-pass-to-multiple-roots-and-obtain-convexity), Theorem 4.1, while the analytic-order theorem remains planned through [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md). Holmgren and analytic-wavefront regularity are not used in this construction.

## An analytic zero branch with a finite cover

By [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md)'s complex homogeneous extension, \(\widehat\Lambda_0\) is holomorphic near \(N'\). Its restriction to the affine plane whose time coordinate is one is not identically zero. Otherwise homogeneity would make it vanish in a full neighborhood of \(N'\), and analytic identity on the connected saturated tube would contradict \(L^\partial\not\equiv0\) and the nonzero principal symbol. A first nonzero Taylor coefficient on that affine plane is a nonzero complex polynomial in its spatial coordinates. Such a polynomial cannot vanish on every real vector, by applying the one-variable polynomial identity successively to each real coordinate. Choose a real spatial vector \(Z\), with zero time component, for which the restriction \(\widehat\Lambda_0(N'+wZ)\) has finite positive order \(q\) at \(w=0\). If the tangent dimension is one, its affine plane has no spatial variable and a nonzero homogeneous function cannot vanish at \(N'\); equation 1 cannot occur there.

Let \(\Lambda(\zeta',\epsilon)\) be the analytic zero-scale function in [equation 14 in The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md) and let \(\kappa\) be its integer principal degree. The germ
\[
\begin{gathered}
\Psi(w,v)=(-i)^{-\kappa}
       \\
\Lambda(-i(N'+wZ),-iv),\\
\qquad
 \Psi(w,0)=\widehat\Lambda_0(N'+wZ)
\end{gathered}
\tag{2}
\]
is jointly holomorphic near \((0,0)\). Where the full determinant is defined it equals
\(v^\kappa L^\partial((N'+wZ)/v)\).
This equality follows by the exact scale substitution, including both factors of \(-i\). At \(v=i/R\), \(R>0\) large, [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md)'s scale \(\epsilon=-iv=1/R\) is positive, so it is the original determinant identity. Analytic continuation then gives the identity on the connected admissible large-\(s\) region specified below.

Choose a small circle \(|w|=r\) enclosing only the \(q\)-fold zero at zero of \(\Psi(\cdot,0)\). On that circle \(\Psi\) remains nonzero for small \(|v|\), and Rouché retains exactly \(q\) zeros inside it. The power sums
\[
\begin{gathered}
c_k(v)=\frac1{2\pi i}\int_{|w|=r}
           w^k\frac{\partial_w\Psi(w,v)}{\Psi(w,v)}\,dw,
 \\
\quad1\le k\le q,\\
\qquad
 W(w,v)=w^q+\sum_{j<q}a_j(v)w^j
\end{gathered}
\tag{3}
\]
and Newton's identities give a monic polynomial \(W\) with coefficients holomorphic in \(v\), whose roots are precisely those zeros, with their multiplicities. Shrinking a zero-free circle at \(v=0\) shows that all these roots tend to zero. No division of \(\Psi\) by \(W\) or analytic unit is needed.

Here is the field step needed to remove persistent multiplicities. Every nonzero holomorphic germ in \(v\) has the form \(v^k b(v)\), with \(b(0)\ne0\), by its first nonzero Taylor coefficient. Its reciprocal is a meromorphic germ with a finite pole at zero. Quotients of holomorphic germs consequently form a field. The finite Euclidean algorithm for polynomials over that field gives division, gcd and Bézout identities exactly as over the complex numbers. Choose a positive-degree monic divisor \(S\) of \(W\) of least possible positive degree. It is irreducible over this field. In characteristic zero \(S_w\ne0\) and has smaller degree, so irreducibility gives
\[
       A(w,v)S(w,v)+B(w,v)S_w(w,v)=1
 \tag{4}
\]
with meromorphic-germ polynomial coefficients.

All coefficients in this finite identity, the divisor and its complementary factor are meromorphic on one sufficiently small punctured disk with no other poles: finitely many denominators have nonzero first Taylor terms. There \(S\) has simple roots by equation 4, and its roots are a subset of those of \(W\). They are bounded and tend to zero. The elementary symmetric formulas therefore bound every coefficient of the monic \(S\). The bounded removable-singularity proof in [Two-dimensional evolution roots and model components](two-dimensional-evolution-roots-and-model-components.md)/[Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md) extends these coefficients holomorphically to zero. Thus we have a finite simple-root cover on a punctured disk, with bounded roots; this includes the possibility \(S=w\).

For completeness, pull the cover back to the convex logarithmic half-plane \(\{\operatorname{Re}\lambda<\log r_0\}\), using \(v=e^\lambda\). Local roots are holomorphic by the one-root Cauchy integral on a small zero-free circle. On any compact parameter path the roots are bounded, leading coefficient is one and the roots are simple; finite root-chart covers and a subdivision continue every label to the endpoint. For a homotopy of two paths, cover its compact image by such complete root charts and subdivide the homotopy square into sufficiently small rectangles. Continuation around each rectangle returns to the same label. Opposite internal edges cancel, so homotopic paths have the same endpoint label. Straight interpolation in the logarithmic half-plane gives global holomorphic labels.

Translation by \(2\pi i\) permutes the finitely many labels, with one fixed permutation by analytic identity. A selected cycle of length \(p\le\deg S\le q\) becomes single-valued after \(v=\tau^p\). Its bounded holomorphic label has a removable singularity at \(\tau=0\), and its value there is zero. Hence
\[
\begin{gathered}
w(v)=\sum_{j\ge1}d_jv^{j/p},\\
\qquad
 T(s)=s\,w(1/s),\\
\qquad
 L^\partial(sN'+T(s)Z)=0\\
\text{ in the admissible region},\\
\qquad
 |T(s)|\le C|s|^\alpha,\\
\quad \alpha=1-\frac1p<1 .
\end{gathered}
\tag{5}
\]
The series converges on a chosen cover for large \(|s|\). Fix the determination of \(s^{-1/p}\) by \(-\pi<\arg s<0\), and continue it slightly across both real rays when needed below. If the chosen label is identically zero, take \(p=1,T=0\). The bound with \(\alpha=0\) then holds as well. The root identity in equation 5 is asserted on the connected region used below, where the parameter belongs to the original projected tube; outside it the germs only supply analytic continuation.

## Meromorphic cofactor data at infinity

The normalized factors in [equation 8 in The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md), evaluated at
\(-i(N'+w(1/s)Z)\) and \(\epsilon=-i/s\), are holomorphic functions of \(\tau=s^{-1/p}\) at zero. Undoing normal scaling gives
\[
\begin{gathered}
R_+(\xi,sN'+T(s)Z)
   \\
=(-i/s)^{-h}
      \\
A_+\bigl((0,-i(N'+w(1/s)Z)),\\
(-i/s)\xi,-i/s\bigr).
\end{gathered}
\tag{6}
\]
The first argument of \(A_+\) is [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md)'s full zero normal representative, and the second is its normal polynomial variable. Initially this equality is the scaled-factor identity on the negative imaginary \(s\)-axis; the right side supplies its analytic continuation. Thus every coefficient is meromorphic in \(\tau\) with a finite pole. The same is true of each restricted polynomial boundary symbol. [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md)'s finite Laurent recurrence makes all matrix entries of
\[
\begin{gathered}
M_{jk}(s)\\
=\beta_{R_+}\bigl(B_j(\cdot,sN'+T(s)Z),\xi^k\bigr),
       \\
\quad1\le j\le h,\ 0\le k<h
\end{gathered}
\tag{7}
\]
meromorphic in \(\tau\). Its determinant is zero by equation 5 and analytic identity of these germs. The case \(h=0\) is excluded by equation 1, since its principal symbol would be one.

Over the meromorphic-germ field choose the maximal rank \(r<h\) of this matrix and fixed \(r\) independent original rows. The normal monomial rows form a basis by [Boundary data for a decaying half-line equation](boundary-data-for-a-decaying-half-line-equation.md)'s nondegenerate Gram matrix. Add fixed rows from that basis to obtain an \((h-1)\)-row matrix \(C(s)\) of rank \(h-1\). As in [Missing boundary rank produces a causal solution](missing-boundary-rank-produces-a-causal-solution.md), form its signed cofactors
\[
 K(\xi,s)=\sum_{k=0}^{h-1}(-1)^{h+k+1}
          \det C_{\widehat k}(s)\,\xi^k .
 \tag{8}
\]
This is not identically zero. It has meromorphic coefficients and uses no division by a minor. Appending any original row to \(C\) gives determinant zero over the field, because that row lies in the span of the selected original rows. Expanding in the last row yields
\(\beta_{R_+}(B_j,K)=0\)
as a meromorphic identity for every original boundary row. The pairing is nondegenerate, so at least one fixed \(j\), \(0\le j<h\), satisfies
\[
                   G_j(s)=\beta_{R_+}(\xi^j,K)\not\equiv0 .
 \tag{9}
\]
Every finite \(G_j\), including higher jets, is meromorphic in \(s^{-1/p}\).

Because \(N'\) is interior to the intersection cone \(V\) of [Boundary determinants as causal Fourier kernels](boundary-determinants-as-causal-fourier-kernels.md), a constant \(C_0\) can be chosen such that
\[
\begin{gathered}
\mathscr A\\
=\{s:-\operatorname{Im}s>C_1(1+|\operatorname{Re}s|)^\alpha\},
 \\
\qquad
 -\operatorname{Im}s>C_0(|T(s)|+1)
       \\
\quad\Longrightarrow\\
\quad
       sN'+T(s)Z\in\mathbb R^{n-1}-iV .
\end{gathered}
\tag{10}
\]
Indeed the time component has that positive cone margin and the perturbation has norm at most \(|Z||T|\); a small ball about \(N'\) inside \(V\) absorbs it. Choose \(C_1\) so large that the connected region \(\mathscr A\) satisfies the second displayed inequality and stays beyond the fixed germ radius. This follows from
\(|T(s)|\le C\{(1+|\operatorname{Re}s|)^\alpha+|\operatorname{Im}s|^\alpha\}\):
the first term is absorbed by the definition of \(\mathscr A\), and the second by its uniformly large imaginary height since \(\alpha<1\). When \(\alpha=0\), both terms are simply bounded constants. The branch determinant identity and the equality of the continued factor with the upper factor hold on the negative imaginary axis by [The principal boundary symbol at high frequency](the-principal-boundary-symbol-at-high-frequency.md)'s positive scaling, and hence on all of \(\mathscr A\) by analytic identity. This proves the admissible assertions in equations 5–6 without making a halfplane-root claim on the later rotated rays.

On \(\mathscr A\) the factor in equation 6 is the upper normal factor, not merely a continued factor. Define, with positive contours enclosing all its roots,
\[
\begin{gathered}
U(a,s)\\
=\frac1{2\pi i}\\
\int_{\mathcal C_+(s)}
           \frac{K(\xi,s)e^{ia\xi}}{R_+(\xi,sN'+T(s)Z)}\,d\xi .
\end{gathered}
\tag{11}
\]
Locally fixed contours prove holomorphy in \(s\) and smoothness in \(a\ge0\), also at repeated roots. In the normal PDE the quotient becomes the entire function \(qR_-K e^{ia\xi}\). In every original boundary trace it becomes the residue pairing just shown to vanish. Therefore
\[
\begin{gathered}
P(D_a,sN'+T(s)Z)U=0,\\
\qquad
 B_j(D_a,sN'+T(s)Z)U|_{a=0}\\
=0,\\
\qquad
 D_a^jU(0,s)=G_j(s).
\end{gathered}
\tag{12}
\]

The meromorphic-germ coefficients of \(K\) have polynomial bounds in \(|s|\). [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md) bounds the upper-factor coefficients and roots polynomially in the tangent frequency, which is \(O(|s|)\) here. [Missing boundary rank produces a causal solution](missing-boundary-rank-produces-a-causal-solution.md)'s union-of-disks contour, with common radius between one and two, has length at most \(4\pi h\), distance at least one from every root, and imaginary part greater than minus two. Consequently, for each integer \(k\ge0\),
\[
          |D_a^kU(a,s)|\le C_k e^{2a}(1+|s|)^{M_k}.
 \tag{13}
\]
The integers \(M_k\) can depend on \(k\). The bound is uniform in \(\mathscr A\) after increasing its defining constant. It includes \(a=0\), and requires no labeling or separation of repeated upper roots.

## A curved inverse integral which vanishes in the past

Choose numbers \(\alpha<\rho_0<\rho<1\), with \(\rho_0>0\), and let
\[
\begin{gathered}
H(\sigma)=(\sigma^2+1)^{\rho_0/2},\\
\qquad
 \gamma_\tau:\ s=\sigma-iH(\sigma)-i\tau,\\
\quad-\infty<\sigma<\infty .
\end{gathered}
\tag{14}
\]
For all sufficiently large \(\tau\), the whole curve and the vertical region between any two such curves lie in \(\mathscr A\) and satisfy equation 10. To verify this uniformly, use
\(|s|\le C(1+|\sigma|+\tau)\)
and
\(|T(s)|\le C'(1+|\sigma|^\alpha+\tau^\alpha)\).
The term \(H(\sigma)\) dominates any fixed multiple of \(|\sigma|^\alpha\) outside a bounded interval because \(\rho_0>\alpha\); the term \(\tau\) dominates any fixed multiple of \(\tau^\alpha\) and covers that bounded interval. The arclength derivative is bounded since \(|H'(\sigma)|\) is bounded.

On the lower half-plane use the branch of \((is)^\rho\) with
\(-\pi/2<\arg(is)<\pi/2\).
Then \(\operatorname{Re}((is)^\rho)\ge\cos(\rho\pi/2)|s|^\rho>0\). For \(a\ge0\), define
\[
\begin{gathered}
u(a,z,t)\\
=\frac1{2\pi}\int_{\gamma_\tau}
       e^{ist+i(z\cdot Z)T(s)-(is)^\rho}\\
U(a,s)\,ds .
\end{gathered}
\tag{15}
\]
On each compact set of physical variables and for fixed \(\tau\), its differentiated integrands are bounded by a polynomial times
\[
       e^{2a}\exp\{-c|s|^\rho+C|s|^{\rho_0}+C|s|^\alpha\}.
 \tag{16}
\]
This is integrable, as are all differentiated integrands, since both positive powers are strictly below \(\rho\). Thus \(u\) is jointly \(C^\infty\) up to \(a=0\); normal right derivatives and all tangent derivatives pass through the integral.

The result is independent of sufficiently large \(\tau\). Integrate the holomorphic integrand around the region between two truncated curves, adding vertical segments at \(\sigma=\pm R\). All its points satisfy equation 10. On the joining segments equation 16 has the same bound, with a fixed segment length \(|\tau_2-\tau_1|\); it tends to zero as \(R\to\infty\). Complex Green/Cauchy then makes the two curved integrals equal. Applying equation 12 inside the convergent integrals proves the interior PDE and all boundary conditions.

For \(t\le-\eta<0\) on any compact physical set, the time factor instead gives \(\exp\{-\eta(H(\sigma)+\tau)\}\). Absorb the \(T\)-phase bound using \(\alpha<\rho\) and \(\alpha<1\). The differentiated integral is bounded, for large \(\tau\), by
\[
\begin{gathered}
C(1+\tau)^M e^{-\eta\tau/2}
       \\
\int_{\mathbb R}(1+|\sigma|)^M e^{-c'|\sigma|^\rho}\,d\sigma
                 \\
\longrightarrow0 .
\end{gathered}
\tag{17}
\]
For example \(\tau^\alpha\le\varepsilon\tau+C_\varepsilon\) and
\(|\sigma|^\alpha\le\varepsilon|\sigma|^\rho+C_\varepsilon\) follow directly by splitting each variable into a bounded part and a sufficiently large part. Polynomial powers of \(|s|\) are bounded by \(C(1+\tau)^M(1+|\sigma|)^M\). Independence of \(\tau\) now proves \(u=0\) for \(t<0\). Since \(u\) is smooth across \(t=0\), every initial jet is zero there.

## A nonzero analytic boundary jet and full boundary support

For the fixed index in equation 9, its boundary jet is
\[
\begin{gathered}
v_j(z,t)\\
=D_a^ju(0,z,t)
       \\
=\frac1{2\pi}\int_{\gamma_\tau}
           e^{ist+i(z\cdot Z)T(s)-(is)^\rho}G_j(s)\,ds .
\end{gathered}
\tag{18}
\]
At \(z=0\), deform the curve to the horizontal line \(s=\sigma-i\tau\), with \(\tau\) larger than the germ radius. This deformation uses only \(G_j\), not \(U\). All the meromorphic-germ coefficient functions continue to the whole large lower half-plane with the fixed determination of \(s^{-1/p}\), regardless of whether normal root signs persist there. Along the region between the two curves the negative imaginary height is at most \(H(\sigma)+\tau\). The same damping versus \(|s|^{\rho_0}\) bound makes the joining tails vanish for every fixed real \(t\), and there are no poles in the deformation region. Hence
\[
\begin{gathered}
e^{-\tau t}v_j(0,t)
   \\
=\mathcal F^{-1}_{\sigma\to t}
       \left[e^{-(i(\sigma-i\tau))^\rho}G_j(\sigma-i\tau)\right].
\end{gathered}
\tag{19}
\]
The bracket is a Schwartz function: meromorphic Puiseux coefficients and all their derivatives grow at most polynomially on this line, and the exponential has stretched-exponential decay. It is nonzero, since \(G_j\not\equiv0\) and a holomorphic nonzero function cannot vanish along an entire line segment. Schwartz Fourier injectivity proves \(v_j(0,\cdot)\not\equiv0\). Since it is smooth and zero for negative time, it cannot vanish at every positive time.

We next prove real analyticity of \(v_j\) on the entire positive-time boundary. Choose a fixed small angle \(\theta>0\) such that
\[
\begin{gathered}
\rho(\pi/2+\theta)<\pi/2,\\
\qquad
 G_j,T\\
\text{ use the continued determination }\\
                -\pi-\theta<\arg s<\theta .
\end{gathered}
\tag{20}
\]
Their meromorphic power series at infinity define them on this sector, after increasing the radius. The two infinite tails of \(\gamma_\tau\) can be rotated to the upper-half-plane rays with arguments \(\theta\) and \(-\pi-\theta\). On the connecting large-circle arcs, \(\operatorname{Re}((is)^\rho)\ge c|s|^\rho\). For real \(t>0\), the time exponential is at most \(\exp(C|s|^{\rho_0})\): any negative imaginary part on those arcs is no larger in modulus than at the original curve endpoints, while positive imaginary part only decreases that exponential. The spatial phase grows at most \(\exp(C|s|^\alpha)\). Polynomial factors and arc length are dominated by the negative \(|s|^\rho\) term. The arc integrals therefore tend to zero. A finite connecting contour plus those two rays represents equation 18 for every real \(z,t\) with \(t>0\).

Fix \(t_*>0\). On either rotated ray \(s=re^{i\varphi}\), its imaginary part is \(r\sin\theta>0\) and \(|\operatorname{Re}s|=r\cos\theta\). For complex \(t\) sufficiently close to \(t_*\), in particular \(\operatorname{Re}t>t_*/2\) and \(|\operatorname{Im}t|<t_*\tan\theta/4\),
\[
 \operatorname{Re}(ist)
   \le-r\,t_*\sin\theta/4 .
 \tag{21}
\]
For complex spatial variables in any fixed small neighborhood, the extra phase has modulus at most \(\exp(Cr^\alpha)\). Every fixed derivative adds only polynomial powers, and \(\alpha,\rho<1\). Thus both ray integrals converge locally uniformly with all derivatives in these complex physical variables. Iterated Cauchy formulas, or their uniformly convergent contour integrals, prove a local joint holomorphic extension. The finite contour part is entire. This proves that \(v_j\) is real analytic for every real \(z\) and \(t>0\).

The positive-time boundary is connected. A real analytic function vanishing on a nonempty open subset there vanishes everywhere: its local holomorphic extensions have all Taylor coefficients zero on that subset, and overlapping disks along a finite subdivision of any path propagate the identity. Since equation 19 proves nonzero values, \(v_j\) has no such open zero set. If \(u\) vanished in a relative neighborhood of any point \(a=0,t>0\), its \(j\)-th right normal derivative would vanish on a boundary open set, a contradiction. Closure of the support then includes time zero as well. Consequently
\[
                \{a=0,\ t\ge0,\ z\in\mathbb R^{n-2}\}
                            \subset\operatorname{supp}u .
 \tag{22}
\]
This completes every assertion of the theorem, including full boundary support and all zero initial jets. No spatial growth estimate is asserted or needed for the resulting \(u\).

## Exercises with complete solutions

**Exercise 1 (entry: a local branch and admissible curve powers).** For the analytic zero cluster \(\Psi(w,v)=(w^2-v)(w-v)\), find the finite-cover periods and the resulting large-\(s\) functions \(T(s)\). Choose concrete \(\rho_0,\rho,\theta\) for the square-root branch and verify the inequalities used above.

**Solution.** At \(v=0\) the zero has multiplicity three. On a sufficiently small punctured disk the roots are \(\sqrt v,-\sqrt v,v\). A loop exchanges the first two and fixes the last. Thus a selected square-root branch has \(p=2\), while the linear branch has \(p=1\). The corresponding functions are
\[
\begin{gathered}
T(s)=s^{1/2},\ -s^{1/2},\ 1,\\
\qquad
 \rho_0=\frac23,\\
\quad\rho=\frac56,\\
\quad\theta=\frac{\pi}{24}.
\end{gathered}
\tag{23}
\]
For either square-root branch \(\alpha=1/2<2/3<5/6<1\). The rotation angle satisfies
\(\rho(\pi/2+\theta)=65\pi/144<\pi/2\).
The damping lower bound on the lower half-plane is \(\cos(5\pi/12)|s|^{5/6}>0\). The spatial phase has only a \(|s|^{1/2}\) power, and the curved time shift has \(|s|^{2/3}\), so the damping dominates both. The fixed branch \(T=1\) needs only \(\alpha=0\), and the same powers work. The labels \(\sqrt v\) are not single-valued before the twofold cover; the integral uses one consistent determination.

**Exercise 2 (intermediate: repeated modes and a detecting boundary jet).** At a scalar fiber take \(R_+(\xi)=(\xi-\lambda)^2\), with \(\operatorname{Im}\lambda>0\), and boundary symbols \(b_1=\xi+\chi-2\lambda\), \(b_2=\chi b_1\). Compute the boundary matrix, a cofactor polynomial, its normal contour mode and one nonzero boundary jet. This exercise concerns the scalar fiber algebra; it does not posit a separate global PDE.

**Solution.** The pairing extracts the coefficient of \(\xi\) in the remainder modulo \((\xi-\lambda)^2\). Since \(\xi^2\) has remainder \(2\lambda\xi-\lambda^2\), the matrix is
\[
\begin{gathered}
M=\begin{pmatrix}1&\chi\\ \chi&\chi^2\end{pmatrix},\\
\quad
 K(\xi)=\xi-\chi,\\
\quad
 U(a)=e^{ia\lambda}\{1+ia(\lambda-\chi)\},\\
\quad
 G_0=1,\\
\quad G_1=2\lambda-\chi .
\end{gathered}
\tag{24}
\]
The first row is independent and has signed last-row cofactors \((-\chi,1)\). The last-row determinant equals its pairing with \(K\). The product \(b_1K\) has constant remainder \(-(\lambda-\chi)^2\), so its pairing is zero; the second row gives the same zero times \(\chi\). The contour mode is the derivative at the double pole, hence the formula for \(U\). It solves \(R_+(D_a)U=0\), and \(b_1(D_a)U(0)=(2\lambda-\chi)+(\chi-2\lambda)=0\), with the same conclusion for \(b_2\). Its zeroth boundary jet is one, so nonzero detection does not require a simple-root assumption or a division by a minor.

**Exercise 3 (advanced: an explicit solution when every negative-line determinant is nonzero).** Take
\[
\begin{gathered}
P(\xi,y,s)=(s-i)(\xi+s-i)-y^2,\\
\qquad B_1=\xi+s,\\
\qquad
 L^\partial(y,s)=i+\frac{y^2}{s-i},\\
\quad
 \Lambda_0(y,s)=\frac{y^2}{s}.
\end{gathered}
\tag{25}
\]
Verify hyperbolicity, the principal degeneracy and the nonvanishing of the full determinant at real \(y\) and \(\operatorname{Im}s<0\). Construct a nonzero smooth causal zero-data solution, with support reaching the whole positive-time boundary.

**Solution.** Put \(z=s-i\). For real \(\xi,y\), the time polynomial \(z^2+\xi z-y^2\) has real roots \((-\xi\pm\sqrt{\xi^2+4y^2})/2\). The time roots in \(s\) have imaginary part one, and \(P_m(N)=1\); thus it is hyperbolic. The normal leading coefficient is \(s-i\), with one upper root \(y^2/(s-i)-s+i\), and the boundary symbol evaluated there gives the stated \(L^\partial\). Scaling gives principal degree one and \(\Lambda_0(N')=0\). If \(s=\sigma-iT\), \(T>0\), and \(y\) is real, then
\(\operatorname{Im}L^\partial=1+y^2(T+1)/(\sigma^2+(T+1)^2)\ge1\).
Every such full determinant is nonzero. Complex spatial roots, satisfying \(y^2=-is-1\), still approach the time direction and explain the principal degeneracy.

Define \(f(t)=e^{-1/t^2}\) for \(t>0\), and \(f(t)=0\) for \(t\le0\). For a positive \(t\), the disk \(|z-t|\le t/8\) stays away from zero. Writing \(z=t(x+iy)\) gives \(x\ge7/8\), \(|y|\le1/8\), and \(|x+iy|\le9/8\), so
\(\operatorname{Re}(1/z^2)\ge1/(4t^2)\).
Cauchy's estimate and a scalar maximum yield
\[
\begin{gathered}
|f^{(k)}(t)|\\
\le k!(8/t)^k e^{-1/(4t^2)}
        \\
\le12^k(k!)^{3/2}\\
\quad(k\ge0).
\end{gathered}
\tag{26}
\]
For \(k\ge1\), maximize \(t^{-k}e^{-1/(4t^2)}\) to get \((2k/e)^{k/2}\); the exponential series gives \(k^k/k!\le e^k\), hence the second estimate with \(8\sqrt2<12\). For \(k=0\) the bound is one. The first estimate also makes every fixed derivative tend to zero at \(t=0\), so the zero extension is smooth and flat.

Set \(F(y,t)=\sum_{k\ge0}f^{(k)}(t)y^{2k}/(2k)!\). For fixed derivative orders \(j,r\) and \(|y|\le R\), the absolute differentiated summands, after finitely many initial terms, are bounded by
\[
 C_{j,r,R}
   \frac{\{12\max(1,R)^2\}^k(k+j)^{3j/2}(2k)^r}{(k!)^{1/2}} .
 \tag{27}
\]
Indeed \((2k)!\ge(k!)^2\), \((k+j)!\le k!(k+j)^j\), and differentiation of the monomial adds a factor at most \((2k)^r\). The ratio of consecutive majorants tends to zero. These bounds are uniform in all real \(t\), using equation 26 and flatness in the past. Thus the series and all derivatives converge uniformly on compact sets, including through \(t=0\). Termwise differentiation proves \(F_t=F_{yy}\), while \(F(0,t)=f(t)\ne0\) for \(t>0\).

Now put
\[
\begin{gathered}
u(a,y,t)=e^{-(t-a)}F(y,t-a),\\
\qquad
 (D_a+D_t)u=0,\\
\qquad
 P(D)u=(\partial_y^2-\partial_t-1)u=0 .
\end{gathered}
\tag{28}
\]
The damped heat equation in the last identity follows directly from \(F_t=F_{yy}\). The boundary condition is zero, and the smooth function vanishes for \(t<a\), so all initial jets at \(t=0\) vanish for \(a\ge0\). It is nonzero at \(y=0,t>a\). For each fixed positive boundary time, its boundary value is entire in \(y\), by local complex Cauchy bounds for \(f^{(k)}\), and is nonzero at \(y=0\). It cannot vanish on any spatial open interval at that time. Therefore no positive-time boundary neighborhood is disjoint from its support; closure includes time zero. This is an explicit instance of the full theorem. Its spatial growth is unrestricted, so the nonuniqueness does not assert a failure of a growth-restricted heat solution class.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Open lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
