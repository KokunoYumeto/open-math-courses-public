# Evolution operators in a component of equal strength

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Equal strength measures how much regularity a symbol controls. It does not determine which time direction permits supported solutions. The forward and backward heat symbols have identical derivative norms but different supported-solvability behavior. We prove that this behavior is constant on each connected component of an equal-strength class. The proof needs a uniform small-perturbation estimate and both openness and closedness; openness alone would not suffice.

Read [Analytic root barriers and supported solvability](analytic-root-barriers-and-supported-solvability.md), [Weighted control on the negative half-space](weighted-control-on-the-negative-half-space.md), [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md), [Continuous functionals, test families and compact limits](continuous-functionals-and-test-families.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz Fourier inversion; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies finite coordinates, scalar calculus and compact cutoffs; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the norm, extension and integration estimates.

One prerequisite remains planned in [Distributions, kernels and analytic singularities](../prerequisites/planned-foundation-proofs.html): a distribution solving an analytic-coefficient equation and vanishing on one side of a noncharacteristic \(C^1\) surface vanishes near that surface. The uses of this Holmgren theorem are conditional on that planned proof.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs use the linked prerequisite lessons and any stated planned theorem.

## The topology of an equal-strength class

Fix \(P\ne0\), of degree \(m\), and a half-space \(H=\{t\ge0\}\). Write \(S_P\) for the exact polynomial derivative norm. Let \(W_P\) be the vector space of polynomials weaker than \(P\), and let \(\mathcal E_P\) be the set of nonzero polynomials of equal strength to \(P\). Define
\[
 \|R\|_P=\sup_{\xi\in\mathbb R^n}\frac{S_R(\xi)}{S_P(\xi)},
                       \qquad R\in W_P.
 \tag{1}
\]
This is a norm. The derivative-vector triangle inequality proves its triangle inequality, and its zero value forces every coefficient of \(R\) to vanish. The written degree lemma puts \(W_P\) in the finite-dimensional space of degree at most \(m\).

Its norm topology is exactly its coefficient topology. Evaluation of the full jet at zero gives \(S_R(0)\le S_P(0)\|R\|_P\), which bounds every coefficient by a constant times this norm. Conversely choose a finite basis of \(W_P\). The triangle inequality bounds the norm of a linear combination by the sum of the absolute coefficients times the fixed basis norms; finite-dimensional coordinate changes give the reverse topological implication. Give \(\mathcal E_P\) the resulting relative topology. Every member has degree exactly \(m\), by applying the degree lemma in both directions.

Call a symbol an **evolution symbol** for \(H\) when it satisfies the five equivalent conditions already proved. For degree zero every nonzero constant is an evolution symbol, since its fundamental solution is its reciprocal times \(\delta_0\); the theorem is immediate. Assume \(m\ge1\) below.

## A uniform normalized estimate

Fix once and for all a bounded open neighborhood \(X\) of zero. We use the exact negative-half-space restriction norm with exponent \(p=1\). This choice controls point evaluation by the Fourier \(L^1\) norm. Suppose a nonzero degree-at-most-\(m\) symbol \(A(z,s)\) obeys
\[
\begin{gathered}
\tau\text{ analytic on }B(c,1),\\
\quad A(z,\tau(z))=0,\\
\quad c\text{ real}
             \\
\quad\Longrightarrow\\
\quad \sup_{B(c,1)}\operatorname{Im}\tau\ge2.
\end{gathered}
\tag{2}
\]
For symbols satisfying this condition, the [Weighted control on the negative half-space](weighted-control-on-the-negative-half-space.md) proof gives constants \(C_*,\kappa_*\), depending only on \(n,m\), for which
\[
\begin{gathered}
\|v\|^-_{1,1}\le C_*e^{\kappa_*L}
                   \|A(D)v\|^-_{1,1/S_A},
        \\
\qquad v\in C_c^\infty,\\
\quad
        |x|\le L\text{ on }\operatorname{supp}v\cap\{t<0\}.
\end{gathered}
\tag{3}
\]
Here uniformity means independence of the coefficients of \(A\), including their sizes. We justify that strengthening of the earlier coefficient-dependent statement by tracing its proof.

The finite jet-shift matrices depend only on \(n,m\). Consequently
\[
\begin{gathered}
\frac{S_A(\xi+h)}{S_A(\xi)}
       \le(1+C_{n,m}|h|)^m,\\
\qquad
 \frac{S_A(\xi)}{S_A(\xi+h)}
       \le(1+C_{n,m}|h|)^m
\end{gathered}
\tag{4}
\]
also at complex base points. Thus every reciprocal symbol weight used in [Weighted control on the negative half-space](weighted-control-on-the-negative-half-space.md) has uniform moderation constants. For products of factors, the reciprocal product has exponent at most \(m\) and a uniform constant, since the sum of factor degrees is at most \(m\).

For an irreducible factor of positive normal degree, the nonzero exceptional polynomial used in [Weighted estimates from analytic root branches](weighted-estimates-from-analytic-root-branches.md) has a degree bounded solely by \(m\). For example, the monic rescaling in L054 has coefficient degrees at most \(m^2\); its Sylvester determinant has at most \(2m-1\) rows. Multiplying by the leading coefficient still gives degree at most \(m+2m^3\). The [Regular balls, moving roots and complex gauges](regular-balls-moving-roots-and-complex-gauges.md) zero-free-subball proof therefore has one permissible radius ratio for this entire degree-bounded family: it obtains its minimum on a unit coefficient sphere and a fixed real half-ball, so it never uses the unnormalized coefficient size.

All regular-ball radii in [Weighted estimates from analytic root branches](weighted-estimates-from-analytic-root-branches.md) can now be fixed with \(A=1\). [Uniform bounds for algebraic analytic branches](uniform-bounds-for-algebraic-analytic-branches.md)'s branch comparison and positive-imaginary ball depend only on degree and these fixed concentric domains. [Root factors and the full symbol norm](root-factors-and-the-full-symbol-norm.md)'s factor norm and zero-free leading-coefficient ratios depend only on degree and radius ratios. [Weighted inversion on a half-line](weighted-inversion-on-a-half-line.md)'s inverse identity has constant one for every positive moderate weight. [Analytic norms and propagation on complex balls](analytic-norms-and-complex-ball-propagation.md)'s interpolation power depends only on the fixed ball radii. There are at most \(m\) root-shift removals. Thus the constants and the positive exponent canceled in [equation 19 in Weighted estimates from analytic root branches](weighted-estimates-from-analytic-root-branches.md)–[equation 21 in Weighted estimates from analytic root branches](weighted-estimates-from-analytic-root-branches.md) have common finite bounds and a common positive lower bound, respectively.

[Weighted control on the negative half-space](weighted-control-on-the-negative-half-space.md)'s spatial cutoff is a fixed chosen function; its frequency jet comparison uses(4). Its modulated window has a fixed Schwartz transform. The later \(L^1\) kernel integral uses only the uniform moderation constants just described. The exact [Disintegrating half-space restriction norms](disintegrating-half-space-restriction-norms.md) disintegration and Young's inequality introduce no symbol coefficients. The finite product-norm comparison depends only on the factor degree bounds, and at most \(m\) nonconstant factors occur. Scalars cancel exactly. Tangential-only factors are covered by [Weighted estimates from analytic root branches](weighted-estimates-from-analytic-root-branches.md)'s coefficient-ratio argument; zero tangential dimension uses its direct scalar-root argument. This proves(3) with the claimed uniform constants for every factorization and multiplicity.

We also need a uniform estimate when the radius-one root height is merely at least minus one. Set
\[
\begin{gathered}
B(z,s)=A(z,s-3i),\\
\qquad w(y)=e^{-3t}v(y).
           \\
\quad B(D)w=e^{-3t}A(D)v.
\end{gathered}
\tag{5}
\]
Every analytic root of \(B\) is an analytic root of \(A\) plus \(3i\); the hypothesis therefore becomes(2). The derivative norms \(S_B,S_A\) are uniformly comparable by the complex jet shift of size three. Choose one compact smooth cutoff equal to one near \(\overline X\). On negative-time restrictions of \(v,w,A(D)v\), multiplication by the cutoff times \(e^{3t}\) or \(e^{-3t}\) implements the indicated gauge and its inverse. These are fixed compact multipliers. The weighted multiplier theorem and(4) bound their actions uniformly on weights \(1,1/S_A,1/S_B\).

Take the fixed spatial bound of \(X\) in(3) and combine these comparisons. There is \(C_0=C_0(n,m,X)<\infty\), independent of \(A\), such that
\[
\begin{gathered}
\|v\|^-_{1,1}\le C_0\|A(D)v\|^-_{1,1/S_A},
                   \\
\qquad v\in C_c^\infty(X),
\end{gathered}
\tag{6}
\]
whenever every radius-one normal-root branch has imaginary supremum at least minus one. Compact multipliers are used only on the relevant supported restrictions; no unbounded exponential is asserted to act on a global weighted space.

## Dilating an evolution symbol and absorbing a weaker perturbation

Let \(A\) now be any evolution symbol of degree \(m\). [Analytic root barriers and supported solvability](analytic-root-barriers-and-supported-solvability.md) and the full-frequency/tangential adapter give a tangential root radius \(a>0\) and height \(b\in\mathbb R\). Put \(A_\epsilon(\xi)=A(\xi/\epsilon)\). An analytic root \(\tau\) of \(A_\epsilon\) on \(B(c,1)\) corresponds to the root \(\tau(\epsilon z)/\epsilon\) of \(A\) on \(B(c/\epsilon,1/\epsilon)\). When \(1/\epsilon\ge a\), restrict to the concentric radius-\(a\) ball. Its height bound gives \(\sup\operatorname{Im}\tau\ge\epsilon b\). Choose \(0<\epsilon\le1\) sufficiently small that also \(\epsilon b\ge-1\). Then(6) holds for \(A_\epsilon\) with the same \(C_0\).

If \(R\in W_A\) and \(M=\|R\|_A\), the rescaled strength comparison yields a constant \(C_1=C_1(n,m)\) such that
\[
\begin{gathered}
S_{R_\epsilon}(\xi)
   \\
=S_R(\xi/\epsilon,1/\epsilon)
   \\
\le C_1 M S_A(\xi/\epsilon,1/\epsilon)
   \\
=C_1 M S_{A_\epsilon}(\xi),\\0<\epsilon\le1.
\end{gathered}
\tag{7}
\]
The constant is independent of the coefficients and of \(\epsilon\): the proof of the rescaled comparison uses degree-bounded coefficient norms and radius ratios at most two. If \(R=0\), the same inequality holds with \(M=0\).

For any Schwartz extension of \(v\)'s negative-time restriction, applying \(R_\epsilon(D)\) gives an extension of the corresponding differential expression by locality. The pointwise Fourier multiplier bound from(7), followed by the extension infimum, gives
\[
 \|R_\epsilon(D)v\|^-_{1,1/S_{A_\epsilon}}
                  \le C_1M\|v\|^-_{1,1}.
 \tag{8}
\]
Use the triangle inequality in(6) and absorb this term. Choose
\(\eta_0=\min(1/2,1/(2C_0C_1))>0\). For \(M<\eta_0\),
\[
\begin{gathered}
\|v\|^-_{1,1}\le
       2C_0\|(A_\epsilon+R_\epsilon)(D)v\|^-_{1,1/S_{A_\epsilon}},
                             \\
\qquad v\in C_c^\infty(X).
\end{gathered}
\tag{9}
\]
The smallness threshold depends only on \(n,m,X\). Although the dilation parameter can depend on \(A\), this threshold does not.

## Extracting the exact compact test estimate

Every Schwartz extension \(\widetilde v\) agreeing with \(v\) for \(t<0\) also agrees at zero by continuity. Fourier inversion with our exact normalization therefore gives
\[
\begin{gathered}
|v(0)|\le(2\pi)^{-n}\int|\widehat{\widetilde v}(\xi)|\,d\xi
            =\|\widetilde v\|_{1,1},
                  \\
\qquad |v(0)|\le\|v\|^-_{1,1}.
\end{gathered}
\tag{10}
\]
Put \(T_\epsilon=A_\epsilon+R_\epsilon\). On the range of \(v\mapsto[T_\epsilon(D)v]\) in the negative-restriction normed space with weight \(1/S_{A_\epsilon}\), define
\[
              F([T_\epsilon(D)v])=v(0).
 \tag{11}
\]
Equations(9)–(10) make this well-defined and bounded. If two images coincide their difference has restriction norm zero, forcing the difference of the origin values to vanish. The written complex Hahn–Banach theorem extends \(F\) to the entire restriction space with the same bound.

Choose a compact neighborhood \(K\) of zero inside \(X\) and \(\chi\in C_c^\infty(X)\) equal to one near \(K\). For smooth tests define
\[
                        U(\phi)=F([\chi\phi]).
 \tag{12}
\]
This is a compactly supported distribution. Indeed \(S_{A_\epsilon}\) has a positive global lower bound; the full \(B_{1,1}\) norm of \(\chi\phi\) is bounded by finitely many suprema of its derivatives on the fixed compact support, using integration by parts of order \(2a>n\). The restriction norm is at most the full norm. This proves the required finite-order bound for \(U\). Its support is in \(\operatorname{supp}\chi\cap\{t\le0\}\), since every test supported in \(t>0\) has zero negative restriction.

For \(v\in C_c^\infty\) supported in \(K\), locality gives \(T_\epsilon(D)v\) supported in \(K\), hence \(U(T_\epsilon(D)v)=v(0)\). Apply [Supported fundamental solutions and test estimates](supported-fundamental-solutions-and-test-estimates.md)'s already proved compact negative-support finite-order estimate to \(U\). For some finite integer \(J\) and \(C\),
\[
\begin{gathered}
|v(0)|\le C\sum_{|\alpha|\le J}
          \sup_{\{t\le0\}}|D^\alpha T_\epsilon(D)v|,
                    \\
\qquad\operatorname{supp}v\subset K.
\end{gathered}
\tag{13}
\]
This is exactly clause(ii), including its negative-side derivative seminorms. The constants here may depend on the symbol; their uniformity is unnecessary for that clause. This extraction uses a compact negative distribution and the finite-order reflection estimate. It assumes neither an attained restriction infimum nor a general smooth extension with uniform bounds.

By the full equivalence, \(T_\epsilon\) is an evolution symbol. Undoing dilation preserves clause(ii) directly. For a test \(u\), set \(v(y)=u(\epsilon y)\). Then
\[
\begin{gathered}
T_\epsilon(D_y)v(y)=(A+R)(D_x)u(\epsilon y),\\D_y^\alpha T_\epsilon(D_y)v
       \\
=\epsilon^{|\alpha|}(D_x^\alpha(A+R)(D_x)u)(\epsilon y).
\end{gathered}
\tag{14}
\]
The test support changes from \(K\) to \(\epsilon K\), still a compact neighborhood of zero, and positive dilation preserves the half-space. Thus \(A+R\) satisfies(ii) and is an evolution symbol. Smallness \(M<1/2\) also gives \(S_{A+R}\ge(1-M)S_A\), so this symbol is nonzero and has equal strength to \(A\).

We have proved the uniform perturbation statement: any evolution symbol of degree \(m\) remains an evolution symbol after a weaker perturbation of relative strength norm less than \(\eta_0\).

## Both openness and closedness

Let \(\mathcal V\subset\mathcal E_P\) consist of the evolution symbols. It is open. At \(A\in\mathcal V\), equal strength gives \(S_P\le C_A S_A\), and therefore
\[
                      \|R\|_A\le C_A\|R\|_P.
 \tag{15}
\]
Every sufficiently small displacement in \(W_P\) is weaker than \(A\) with norm less than \(\eta_0\), so the uniform perturbation statement applies.

It is also closed in \(\mathcal E_P\). Suppose \(A_j\in\mathcal V\) tends to \(A\in\mathcal E_P\) in coefficient topology. Equation(15), now for this fixed limiting \(A\), gives \(d_j=\|A_j-A\|_A\to0\). For \(d_j<1\), the derivative-vector reverse triangle inequality gives
\[
\begin{gathered}
S_{A_j}\ge(1-d_j)S_A,\\
\qquad
             \|A-A_j\|_{A_j}\le\frac{d_j}{1-d_j}.
\end{gathered}
\tag{16}
\]
All these symbols have the same degree. Eventually the last ratio is less than the same \(\eta_0\), independent of \(j\). Apply the perturbation statement to the known evolution symbol \(A_j\) with perturbation \(A-A_j\); it makes \(A\) an evolution symbol. This proves closedness. Sequential closedness suffices because the coefficient topology is metrizable by finite coordinates.

On a connected component, an open-and-closed subset is either empty or the entire component: otherwise its intersection and complement would separate that component into two nonempty relative open sets. Hence if \(P\) is an evolution symbol, every member of its component in \(\mathcal E_P\) is one. This proves the full [the five-way theorem](analytic-root-barriers-and-supported-solvability.md)7 theorem. The argument uses connectedness, without assuming that an arbitrary connected component has been described by paths.

As a useful consequence, every dominated correction \(R\ll P\) preserves evolution solvability. For \(0\le a\le1\), the polynomial \(aR\) is still dominated by \(P\); the strength lemma makes \(P+aR\) equally strong to \(P\). This continuous path is a connected subset of \(\mathcal E_P\) containing \(P\), so the component theorem applies at \(a=1\). No small coefficient bound is needed for a dominated correction.

Arbitrary nonzero half-space normals reduce to these coordinates by [equation 24 in Analytic root barriers and supported solvability](analytic-root-barriers-and-supported-solvability.md)'s orthogonal jet comparisons. The linear coordinate map on the finite coefficient spaces preserves their topology and takes equal-strength classes and components to the corresponding classes and components.

## Examples and complete exercises

**Exercise 1 (entry).** Compare the two heat symbols \(P(\xi,s)=\xi^2+is\) and \(Q(\xi,s)=\xi^2-is\) for \(H=\{t\ge0\}\). Explain why equal strength does not settle the supported-solvability question.

**Solution.** On real frequencies,
\[
                         S_P^2=S_Q^2=\xi^4+s^2+4\xi^2+5.
 \tag{17}
\]
Their normal roots are respectively \(\tau_P(z)=iz^2\) and \(\tau_Q(z)=-iz^2\). At every real center \(c\), \(\operatorname{Im}\tau_P(c)=c^2\ge0\), so \(P\) satisfies a fixed-radius tangential root barrier. The equivalence makes it an evolution symbol. For any proposed radius \(a>0\) and real \(c>a\), write \(z=c+u+iv\), \(u^2+v^2<a^2\). Then
\[
\begin{gathered}
\operatorname{Im}\tau_Q(z)\\
=-(c+u)^2+v^2
                         \\
\le-(c-a)^2+a^2\\
\longrightarrow-\infty.
\end{gathered}
\tag{18}
\]
Its analytic branch therefore violates every uniform height bound, so \(Q\) is not an evolution symbol. The component theorem implies these two equally strong symbols belong to different connected components. In physical variables they give the heat equation with opposite choices of time direction.

**Exercise 2 (intermediate).** Suppose a sequence of known evolution symbols \(A_j\) converges to an equally strong \(A\), and \(\|A_j-A\|_A\le1/10\) for one index. Bound the reverse perturbation size. Explain why a perturbation radius allowed to shrink arbitrarily with \(j\) would not prove closedness.

**Solution.** Equation(16) gives \(\|A-A_j\|_{A_j}\le(1/10)/(9/10)=1/9\). More generally this ratio tends to zero as the original displacement does. With the uniform threshold \(\eta_0\), eventually it is small enough to apply the perturbation theorem to some known evolution symbol \(A_j\). A radius \(\eta_j>0\) depending on \(j\) could decay faster than the displacement; coefficient convergence alone would not ensure that any inequality \(\|A-A_j\|_{A_j}<\eta_j\) holds. The degree-only threshold is precisely what removes that gap.

**Exercise 3 (advanced).** In the family \(R_b(\xi,s)=\xi^2+bs\), \(b\in\mathbb C\), determine which members have equal strength to \(R_i\), and which of those are evolution symbols for \(t\ge0\). Relate the two regions to the component theorem without claiming a classification of the whole equal-strength space.

**Solution.** If \(\operatorname{Im}b\ne0\), the real linear map \((u,s)\mapsto u+bs\in\mathbb C\) is invertible. Its fixed finite-dimensional norm comparison gives
\[
\begin{gathered}
|u+bs|^2\asymp u^2+s^2,\\S_{R_b}(\xi,s)^2\\
=|\xi^2+bs|^2+4\xi^2+|b|^2+4
                         \\
\asymp S_{R_i}(\xi,s)^2.
\end{gathered}
\tag{19}
\]
Take \(u=\xi^2\). If \(b\) is nonzero and real, set \(\xi=r,s=-r^2/b\): the value of \(R_b\) is zero and \(S_{R_b}=O(r)\), whereas \(S_{R_i}\) grows like \(r^2\). For \(b=0\), use \(\xi=0,s\to\infty\). Thus the equal-strength members of this family are exactly those with nonreal \(b\).

Their root is \(\tau_b(z)=-z^2/b\). The coefficient \(a_b=-1/b\) has imaginary part \(\operatorname{Im}b/|b|^2\). If it is positive, evaluation at real centers gives the uniform height bound zero. If it is negative, on any fixed-radius ball about real \(c\) the imaginary part equals \((\operatorname{Im}a_b)c^2+O(|c|+1)\), uniformly on the ball, and tends to minus infinity. The root criterion therefore makes exactly the upper-half-plane parameter members evolution symbols. The upper and lower parameter regions are separately connected; a continuous path within this family cannot cross between them without meeting a real parameter that loses equal strength. This family illustrates the component result, while the theorem itself also controls possible paths and connected subsets outside this family.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
