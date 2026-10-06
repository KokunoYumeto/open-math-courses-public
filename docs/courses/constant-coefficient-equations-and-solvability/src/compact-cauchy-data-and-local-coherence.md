# Compact Cauchy data and local coherence

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Compact Cauchy data allow a cutoff only where the solution is already zero. Slab uniqueness then makes the data vanish locally, while a compact-frequency construction still supplies a dense class of admissible data.

Read [Uniqueness in a slab with bounded support](bounded-support-slab-uniqueness.md), [Cauchy data, regularity and spacelike initial surfaces](cauchy-data-regularity-and-spacelike-initial-surfaces.md).

One prerequisite remains planned in [Distributions, kernels and analytic singularities](../prerequisites/planned-foundation-proofs.html): a distribution solving an analytic-coefficient equation and vanishing on one side of a noncharacteristic \(C^1\) surface vanishes near that surface. The uses of this Holmgren theorem below are conditional on that planned proof.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs below use the linked prerequisite lessons and the stated planned results.

## From zero traces to local vanishing

Use coordinates \((y,t)\) with \(t=x\cdot N\), \(N\ne0\), and write
\[
\begin{gathered}
P(D_y,D_t)=\sum_{\ell=0}^{m} A_\ell(D_y)D_t^\ell,\\
\qquad
 A_m=P_m(N)\ne0,\\
\qquad \deg A_\ell\le m-\ell.
\end{gathered}
\tag{1}
\]
Such coordinates follow from any real complementary frequency basis with last column \(N\). A rescaled normal changes the trace convention by nonzero factors, not their zero sets or supports.

**Lemma 1 (the zero-trace consequence of Holmgren).** Let \(u\) be \(C^m\) up to a local piece of \(t=0\) from \(t\ge0\), solve \(P(D)u=0\) for \(t>0\), and have
\[
\begin{gathered}
(D_t^j u)(y,0)=0,\\
\qquad j=0,\ldots,m-1,
\end{gathered}
\tag{2}
\]
on an open part of the plane. Then \(u=0\) in a one-sided neighborhood of each point of that part, relative to the stated Holmgren theorem. The analogous assertion holds for \(t\le0\), and for a two-sided \(C^m\) solution.

**Proof.** Locally extend the function by zero to \(t<0\), calling the resulting distribution \(u_+\). Repeated one-dimensional integration by parts gives
\[
\begin{gathered}
D_t^\ell u_+
  \\
=(D_t^\ell u)_+
   \\
+\sum_{a=0}^{\ell-1}(-i)^{a+1}
        (D_t^{\ell-1-a}u)(y,0)\,\delta^{(a)}(t).
\end{gathered}
\tag{3}
\]
The sum is empty for \(\ell=0\); \(\delta^{(a)}\) means an ordinary distributional derivative. To verify it, the first derivative is \(D_tu_+=(D_tu)_+-iu(y,0)\delta\). Apply this first-derivative identity to the interior derivative in each inductive step and differentiate the existing boundary terms with \(D_t=-i\partial_t\). A new \(a=0\) term appears and the old \(a\)-terms move to \(a+1\) with exactly one additional \(-i\). This proves (3) for all \(\ell\le m\).

Every trace in its sum is zero by (2). Tangential application of \(A_\ell(D_y)\) introduces no new boundary term and leaves a zero trace zero. It is legitimate at the stated regularity: the operator has order at most \(m-\ell\), while the trace has \(m-(\ell-1-a)\) continuous tangential derivatives. Thus \(P(D)u_+=(P(D)u)_+=0\). This distribution vanishes on the negative side of the noncharacteristic plane. The exact planned Holmgren theorem makes it vanish near that plane; restriction to the positive side proves the assertion.

Replacing \(t\) by \(-t\) proves the negative-side version: the new principal value is \((-1)^mP_m(N)\ne0\), and the zero trace condition is unchanged. For a two-sided solution apply both versions. Their local neighborhoods intersect in a full neighborhood of the plane point, on which the original solution is zero. \(\square\)

## Cutting off only where the solution is already zero

**Theorem 2 (compact-data coherence).** Let \(X\subset\mathbb R^n\) be open and \(u\in C^m(X)\) satisfy \(P(D)u=0\), with \(P\) of order \(m\ge1\). Suppose the plane \(\Sigma=\{x:x\cdot N=0\}\) is noncharacteristic and every nonconstant irreducible factor has principal part not hyperbolic with respect to \(N\). If the union \(S\) of the relative supports of the \(m\) Cauchy traces on \(\Sigma\cap X\) is compact there, then \(u=0\) in a neighborhood of \(\Sigma\cap X\). In particular all those traces are zero.

**Proof.** Compactness in the relative open plane gives a compact subset \(S\) of the ambient plane contained in \(X\). If \(S\) is empty, Lemma 1 gives the conclusion at every plane point, so assume it is nonempty. Choose \(\chi\in C_c^\infty(X)\) equal to one on an open neighborhood of \(S\). Its existence follows by covering \(S\) by finitely many balls compactly contained in \(X\), choosing smooth cutoffs on these balls, and taking \(1-\prod(1-\chi_j)\).

Let \(T\) be the union of the supports of all derivatives \(\partial^\beta\chi\) with \(1\le|\beta|\le m\). This is compact in \(X\), and \(T\cap S=\varnothing\) because \(\chi=1\) on a neighborhood of \(S\). At every \(p\in T\cap\Sigma\), all Cauchy traces of \(u\) vanish in a relative plane neighborhood: \(p\) is outside their closed support union \(S\). Lemma 1 gives an open neighborhood on which \(u=0\). Their union \(O\) contains the compact set \(T\cap\Sigma\). There is \(\varepsilon>0\) with
\[
 T\cap\{|t|<\varepsilon\}\subset O.
 \tag{4}
\]
Otherwise choose points of \(T\setminus O\) with \(t\to0\). A compact subsequence has a limit in \(T\cap\Sigma\subset O\), contradicting openness of \(O\). If \(T\cap\Sigma\) is empty, the same argument gives a strip disjoint from \(T\).

Set \(v=\chi u\) on \(X\) and extend it by zero outside \(X\). Because \(\chi\) has compact support in \(X\), this is a global \(C^m\) function with compact support. On \(|t|<\varepsilon\),
\[
 P(D)v=\chi P(D)u+[P(D),\chi]u=0.
 \tag{5}
\]
Indeed, every commutator term contains a positive-order derivative of \(\chi\), whose support is in \(T\); (4) makes \(u\) and all its derivatives zero there. Outside \(T\) those terms vanish by the cutoff derivative itself. The identity also holds outside \(X\), where \(v\) is zero in a neighborhood.

Apply the arbitrary-distribution form of Theorem 5 in [Uniqueness in a slab with bounded support](bounded-support-slab-uniqueness.md) to \(v\) on this entire slab. Its relative support is bounded, so \(v=0\). Since \(\chi=1\) near \(S\), \(u=0\) near \(S\) within the slab. At every point of \((\Sigma\cap X)\setminus S\), Lemma 1 already gives local vanishing. These neighborhoods together give the conclusion on a neighborhood of all of \(\Sigma\cap X\). No uniform thickness over its possibly unbounded part is claimed. \(\square\)

**Corollary 3 (one-sided existence is enough).** The same conclusion, as a relative one-sided neighborhood, holds if the solution is only \(C^m\) up to \(\Sigma\cap X\) from \(t\ge0\), on a relative open neighborhood of that set in the closed halfspace. It suffices that the equation holds in its positive-side interior and the \(m\) traces have compact support. The corresponding negative-side statement also holds.

**Proof.** Lemma 1 gives one-sided vanishing off \(S\). The relative neighborhood of the compact \(S\) contains \(W\cap\{t\ge0\}\) for some full open neighborhood \(W\) of \(S\). Choose the cutoff with compact support in \(W\), equal to one near \(S\). In the preceding proof, use only the compact set \(T\cap\{t\ge0\}\). Its intersection with \(\Sigma\) is covered by one-sided neighborhoods of vanishing. Compactness gives
\[
 T\cap\{0<t<\varepsilon\}\subset\{u=0\},
 \tag{6}
\]
in the solution's one-sided domain, after shrinking \(\varepsilon\). The same subsequence argument as in (4) proves this.

Define \(v=\chi u\) only for \(0<t<\varepsilon\), extending it by zero across the spatial boundaries of its local domain. These extensions are \(C^m\) within the open positive slab because the cutoff has compact support in \(W\). The commutator vanishes by (6), so \(P(D)v=0\) throughout the slab \(0<t<\varepsilon\). Its relative support is bounded. Theorem 5 applies to this slab without a condition at its boundary \(t=0\), and gives \(v=0\) there. This makes \(u=0\) near \(S\) on the positive side. Continuity up to the plane gives zero there as well, and derivatives up to order \(m\) are zero on the side and have zero limits at the plane.

Together with local vanishing off \(S\), this proves the full relative one-sided conclusion. We have not extended nonzero Cauchy traces by zero through the plane; that would create the boundary terms (3). The negative-side case follows by reversal of the normal. \(\square\)

## Admissible data still form a dense class

Compact spatial support is a strong restriction. It does not imply that solvable Cauchy data obey a universal continuous linear relation on the Schwartz class.

**Proposition 4.** For any constant-coefficient polynomial of order \(m\) with \(P_m(N)\ne0\), arbitrary Cauchy data whose Fourier transforms belong to \(C_c^\infty(\mathbb R^{n-1})\) admit a global smooth homogeneous solution. These data are dense in \(\mathcal S(\mathbb R^{n-1})^m\). Consequently a continuous linear functional on that Schwartz product which vanishes on all admissible data is zero.

**Proof.** In (1), take spatial Fourier transforms and let \(g_j(\xi)\) be the prescribed transforms, \(0\le j<m\), all supported in one compact set. Put \(V=(U,D_tU,\ldots,D_t^{m-1}U)^T\). The equation becomes
\[
\begin{gathered}
D_tV=A(\xi)V,\\
\qquad
 V(\xi,t)=e^{itA(\xi)}(g_0(\xi),\ldots,g_{m-1}(\xi))^T,
\end{gathered}
\tag{7}
\]
where \(A\) has ones in its upper shift positions and last row
\((-A_0(\xi)/A_m,\ldots,-A_{m-1}(\xi)/A_m)\). The leading coefficient \(A_m\) is a nonzero constant, so every matrix entry is polynomial in \(\xi\). The power series for the exponential converges with all finite derivatives uniformly on compact \((\xi,t)\)-sets. Here is the derivative bound needed for that assertion. On a fixed compact set choose \(M\ge1\) bounding the matrix and all its derivatives up to a chosen order \(k\). A derivative of \(A^r\) has at most a constant times \((1+r)^k\) product terms, each bounded by \(M^r\); distributing the \(k\) derivative operations among the \(r\) factors proves this bound even if some factors are differentiated repeatedly. Time differentiation shifts the factorial denominator by the number of time derivatives. The resulting bounds are polynomial multiples of the convergent scalar exponential series. Termwise differentiation is therefore valid. It gives \(\partial_tV=iA(\xi)V\), hence the exact \(D_t=-i\partial_t\) equation, and the prescribed initial vector.

Take the inverse spatial Fourier transform of its first entry,
\[
\begin{gathered}
u(y,t)=(2\pi)^{-(n-1)}
       \\
\int_{\mathbb R^{n-1}}e^{iy\cdot\xi}U(\xi,t)\,d\xi.
\end{gathered}
\tag{8}
\]
The fixed compact frequency support permits every space/time derivative under this integral. It gives a global \(C^\infty\) solution, and Schwartz inversion gives exactly the prescribed \(D_t\)-traces. No hyperbolicity assumption is used. In fact the same compact integration makes this solution entire in complex \(y,t\): the finite-frequency integral is uniformly convergent on every complex compact set, and the matrix exponential is entire in \(t\).

For density, choose a smooth cutoff \(\theta=1\) on the unit ball and zero outside the ball of radius 2. For every Schwartz function \(g\), set \(g_R(\xi)=\theta(\xi/R)g(\xi)\). Leibniz's formula expresses every weighted derivative of \(g_R-g\) as either the Schwartz tail of a derivative of \(g\), or a term containing \(R^{-|\beta|}(\partial^\beta\theta)(\xi/R)\) on \(R\le|\xi|\le2R\). The rapid decay of each derivative of \(g\) makes every such weighted supremum tend to zero; there are finitely many terms for each seminorm. Thus \(g_R\to g\) in \(\mathcal S\). Fourier inversion is continuous for this topology by the Schwartz Fourier proof and its integration-by-parts seminorm bounds. The inverse transforms of compact-frequency smooth functions are therefore dense too. Apply this to all \(m\) components. A continuous linear functional vanishing on this dense subset vanishes on its closure. \(\square\)

## Exercises with complete solutions

**Exercise 1 — basic: compact support versus rapid decay.** For \(P(\zeta,s)=\zeta^2+s^2+1\), use Theorem 2 to determine the compactly supported Cauchy data of a \(C^2\) homogeneous solution near the full plane \(t=0\). Compare this with the data \(u(y,0)=e^{-y^2}\), \(D_tu(y,0)=0\).

**Solution.** The quadratic is irreducible by the rational-square argument in Exercise 3 of [Uniqueness in a slab with bounded support](bounded-support-slab-uniqueness.md). Its principal part has nonreal roots \(s=\pm i\zeta\) for real nonzero \(\zeta\), and \(P_2(0,1)=1\ne0\). Theorem 2 therefore makes every compactly supported pair of such Cauchy traces zero.

The Gaussian is Schwartz but has noncompact support. Its transform is \(\sqrt\pi e^{-\xi^2/4}\). Set
\[
 U(\xi,t)=\sqrt\pi e^{-\xi^2/4}
                \cosh\!\bigl(t\sqrt{\xi^2+1}\bigr).
 \tag{9}
\]
It satisfies \(U_{tt}=(\xi^2+1)U\), hence \((D_t^2+\xi^2+1)U=0\), with \(U(\xi,0)\) the Gaussian transform and \(D_tU(\xi,0)=0\). On every compact time interval, every differentiated integrand is bounded by a polynomial in \(|\xi|\) times \(e^{-\xi^2/4+C(1+|\xi|)}\), which is integrable with every power. Spatial derivatives have the same property. Its inverse Fourier transform is a global smooth solution with precisely those Gaussian data. It is nonzero at \(t=0\). This verifies why rapid decay cannot replace compact support in Theorem 2.

**Exercise 2 — intermediate: boundary phases at finite regularity.** Verify the boundary distribution for \(D_t^2+aD_t+B(D_y)\) acting on the positive-side extension of a \(C^2\) function. Explain which two traces must vanish before invoking Holmgren.

**Solution.** For \(\phi_0=u(y,0)\), \(\phi_1=D_tu(y,0)\), (3) gives
\[
\begin{gathered}
P(D)u_+=(P(D)u)_+
          \\
-i(\phi_1+a\phi_0)\delta(t)-\phi_0\delta'(t).
\end{gathered}
\tag{10}
\]
The tangential operator \(B(D_y)\) has no time derivative and creates no boundary distribution. The trace \(\phi_0\) must vanish to remove the \(\delta'\)-term; after that, \(\phi_1\) must vanish to remove the \(\delta\)-term. In ordinary derivatives this is the condition \(u(y,0)=u_t(y,0)=0\), and the second-order term is \(-u_t(y,0)\delta-u(y,0)\delta'\). The formula and its sign need only \(C^2\) up to the plane. Extending nonzero traces by zero produces a source, so Holmgren cannot be applied to that extension as a homogeneous solution.

**Exercise 3 — advanced: the conclusion is local in the given domain.** Give a homogeneous solution with compact Cauchy data which is zero near \(\Sigma\cap X\) but is not zero on all of a disconnected \(X\), under the operator in Exercise 1.

**Solution.** In \((y,t)\)-space take
\(X=B((0,0),1)\cup B((0,3),1)\). The second ball is disjoint from \(t=0\). Define \(u=0\) on the first ball and \(u=e^{-t}\) on the second. This is smooth on the disconnected open set. On the second ball,
\(D_y^2u=0\) and \(D_t^2u=-\partial_t^2e^{-t}=-e^{-t}\), so \((D_y^2+D_t^2+1)u=0\); the equation is also true on the first ball. All Cauchy traces on \(\Sigma\cap X\) are zero, with empty compact support. The theorem gives vanishing near that plane portion, while \(u\) remains nonzero on the remote component. The ambient domain is not an entire slab, so the bounded-support slab theorem cannot be applied directly to this \(u\).

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
