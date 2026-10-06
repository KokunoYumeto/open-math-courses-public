# Global inverses and the circle multiplier

This companion supplies the two remaining prerequisite arguments for [Graph operators, continuity and Egorov](graph-operators-continuity-and-egorov.md). The proofs below are independently written. Author: GPT-6 Astra (OpenAI), Ultra, 5 October 2026. This component is dedicated under CC0-1.0. Earlier linked components retain their individual licences.

The exact inputs are [conic parametrices K2–K4](../20261004-free-intrinsic-graph/prerequisites/conic-parametrices-and-localization.md), [ordinary composition and proper support O3–O6](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md), [conic smoothing T2](../20261004-free-intrinsic-graph/prerequisites/coordinate-and-wavefront-localization.md), [partitions PS5](../20261004-free-intrinsic-graph/prerequisites/global-principal-symbol.md), [Hilbert space and compactness T1–T2](../20261004-free-canonical-composition/compactness-and-essential-norms.md), [measure and compact smooth density M7](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md), and [periodic Fourier reconstruction, Section 13.2](../20261005-restored-analytic-composition/scalar-kernels-and-strong-topology.md). The [proof map](proof-map.json) binds the Fourier, integral and elementary calculus inputs as well.

## G0. A global proper inverse from local conic inverses

Let \(P\) be a properly supported ordinary pseudodifferential operator of order \(d\) between finite-rank bundles on a smooth Hausdorff second-countable manifold. Assume ellipticity in the symbol sense of K2: on every compact base and sufficiently small closed direction patch, its symbol has a two-sided matrix inverse of order \(-d\), with all derivative estimates. No uniform constant on the whole manifold is assumed. We prove that there is a proper \(R\in\Psi^{-d}\) for which both \(RP-I\) and \(PR-I\) have smooth kernels.

Use the proved locally finite partition construction PS5 to choose precompact bundle coordinate neighborhoods \(V_i\), whose closures form a locally finite family, and a subordinate partition \(\sum_i\varphi_i=1\) with \(\operatorname{supp}\varphi_i\Subset V_i\). On the compact cosphere over each support, choose finitely many small elliptic cone patches. Shrink the retained patches inside larger patches before quantizing. K3 supplies a two-sided conic inverse \(Q_{i\ell}\) on each larger patch. All its base kernel cutoffs can be chosen compactly inside \(V_i\times V_i\), since the retained base support is an interior compact set. Its left and right errors are smoothing on a fixed open error cone containing the closure of the retained patch.

K4, with these retained patches, supplies order-zero operators \(E_{i\ell}\) with kernels compactly supported inside \(V_i\times V_i\), essential symbol support in the assigned error cone, and
\[
 \sum_\ell E_{i\ell}=\varphi_i I+S_i,
 \qquad S_i\text{ has a smooth compactly supported kernel}.
 \tag{GI1}
\]
For operators between different bundles, perform this construction separately on the source and target bundles, using the scalar partition times the identity in their respective frames. Denote the resulting source and target cutoffs by \(E^s_{i\ell}\) and \(E^t_{i\ell}\). Each has (GI1) on its own bundle and can use the same retained cone cover. Define the ordered sums
\[
 R_L=\sum_{i,\ell}E^s_{i\ell}Q_{i\ell},
 \qquad R_R=\sum_{i,\ell}Q_{i\ell}E^t_{i\ell}.
 \tag{GI2}
\]
Every product kernel in these sums has both variables in \(\overline V_i\). The sums are locally finite, hence define ordinary operators of order \(-d\); each compact coordinate set needs only finitely many local symbol estimates. They are proper: a compact set in either variable meets only finitely many \(\overline V_i\), and the other variable is then confined to the finite union of those compact sets. In particular these are actual distributional kernel sums, not merely formal symbol sums.

By (GI1),
\[
 R_LP-I=\sum_{i,\ell}E^s_{i\ell}(Q_{i\ell}P-I)+\sum_i S_i^s,
 \qquad
 PR_R-I=\sum_{i,\ell}(PQ_{i\ell}-I)E^t_{i\ell}+\sum_i S_i^t.
 \tag{GI3}
\]
Each product on the right is smoothing by T2: the cutoff's closed essential support lies inside the fixed error cone where the adjacent error has every negative-order estimate. Outside that cone the cutoff is smoothing; a finite conic partition proves all the resulting derivative estimates. The first sum in (GI3) is locally finite in its output variable, and the second is locally finite in its input variable. Thus their smooth kernels sum smoothly on every compact product. The remainders are also proper, since they are differences of proper products and identity. This establishes the left and right inverse identities globally.

Finally,
\[
 R_L-R_R=R_L(I-PR_R)+(R_LP-I)R_R.
 \tag{GI4}
\]
The proper smoothing ideal O6 shows that this difference is smoothing. Composing that smoothing difference with \(P\) preserves smoothness, so either \(R_L\) or \(R_R\) is a two-sided parametrix. All matrix products have retained their order. This argument uses the fully proved local asymptotic construction K3 and locally finite kernel sums; it makes no assertion about convergence of an operator Neumann series. For a single retained cone, K3 itself gives the corresponding microlocal assertion. ∎

## G1. Fourier modes form a complete circle basis

Use the circle of length \(2\pi\), the Lebesgue density \(dx\), and
\[
 e_k(x)=(2\pi)^{-1/2}e^{ikx},\qquad k\in\mathbb Z.
 \tag{CF1}
\]
The elementary exponential and period proofs P15–P16 give
\(\int_0^{2\pi}e^{i(k-j)x}\,dx=2\pi\delta_{jk}\), hence orthonormality. Compact smooth functions in the interval \((0,2\pi)\) are dense in its \(L^2\) space by M7. Equivalently, first remove arbitrarily small endpoint tails in \(L^2\), then apply its compact smooth approximation on the remaining interior set. Their zero extensions are smooth periodic functions. Section 13.2 of the kernel companion proves that the Fejér trigonometric polynomials converge uniformly to any continuous periodic function. Uniform convergence on this finite interval implies \(L^2\) convergence. The trigonometric polynomials are consequently dense in circle \(L^2\).

Let \(P_Nu=\sum_{|k|\le N}(u,e_k)e_k\). Finite orthogonality gives \(\|P_Nu\|_2\le\|u\|_2\). Given a trigonometric polynomial \(v\), for all sufficiently large \(N\) one has \(P_Nv=v\), and therefore \(\|u-P_Nu\|_2\le2\|u-v\|_2\). Density proves \(P_Nu\to u\). Applying finite Pythagoras and taking limits proves Parseval:
\[
 \|u\|_2^2=\sum_{k\in\mathbb Z}|(u,e_k)|^2.
 \tag{CF2}
\]
For a bounded sequence \(m_k\), the finite sums with coefficients \(m_k(u,e_k)\) are Cauchy by (CF2), so define a bounded diagonal multiplier. Its norm is at most \(\sup_k|m_k|\), and evaluation on each \(e_k\) proves equality. Its tail after \(|k|\le N\) has norm exactly \(\sup_{|k|>N}|m_k|\). This also proves uniqueness of the multiplier from its mode action. A sequence with \(m_k\to0\) gives a compact operator, since these truncations are finite rank and converge in norm, by T1. ∎

## G2. Periodization proves the local pseudodifferential claim

Put \(m(\xi)=(1+\xi^2)^{-1/2}\). The power and chain rules give
\(|\partial_\xi^jm(\xi)|\le C_j\langle\xi\rangle^{-1-j}\) for every \(j\); this also follows inductively by writing each differentiated term as a polynomial times a power of \(1+\xi^2\). Taylor's integral formula applied to \((1+s)^{-1/2}\) near \(s=0\), with \(s=\xi^{-2}\), shows that \(m(\xi)-|\xi|^{-1}\in S^{-3}\) off zero. Thus \(m\) has ordinary order \(-1\), with principal symbol \(|\xi|^{-1}\).

Let \(k=\mathcal F^{-1}m\) as a tempered distribution, with inverse factor \((2\pi)^{-1}\). Fourier inversion and its distributional extension were proved in Q3–Q4 and L3. For integers \(a,N\ge0\) with \(2N>a\), the function \(\partial_\xi^{2N}[(i\xi)^a m(\xi)]\) is integrable. The Fourier differentiation identity gives
\[
 x^{2N}\partial_x^ak(x)
 =(-1)^N(2\pi)^{-1}\int_{\mathbb R}e^{ix\xi}
       \partial_\xi^{2N}[(i\xi)^a m(\xi)]\,d\xi.
 \tag{CF3}
\]
Initially this is a distributional identity, obtained by testing Fourier inversion; the integral on the right is a continuous bounded function. Applying it at every derivative order shows that \(k\) is smooth off zero and every derivative decreases faster than any prescribed inverse power as \(|x|\to\infty\). Smoothness follows, for example, successively from the distributional derivative identities: a function whose distributional first derivative is continuous equals a continuously differentiable primitive plus a constant, by the test-function fundamental theorem. The same argument iterates. This is also the off-diagonal kernel proof O4 specialized to a multiplier.

Choose \(\chi\in C_c^\infty((-\pi/2,\pi/2))\), equal to one near zero. Then \(k=\chi k+(1-\chi)k\) is the sum of a compactly supported distribution and a Schwartz function. Consequently
\[
 K(t)=\sum_{\ell\in\mathbb Z}k(t+2\pi\ell)
 \tag{CF4}
\]
is a well-defined periodic distribution: the compact-distribution part is locally finite, and the Schwartz part and all its derivative series converge absolutely and uniformly on compact sets. These statements follow directly from (CF3) and comparison with \(\sum_{\ell\ne0}|\ell|^{-2}\). They justify translating and regrouping the terms.

The Fourier coefficient of (CF4) at an integer \(j\) is
\[
 \frac1{2\pi}\langle K,e^{-ijt}\rangle_{S^1}
   =\frac1{2\pi}\langle k,e^{-ijt}\rangle_{\mathbb R}
   =\frac{m(j)}{2\pi}.
 \tag{CF5}
\]
For the first equality, periodize the compact part and integrate the Schwartz tails, splitting the real line into translated period intervals. Integer \(j\) makes the exponential invariant under those translations, and the tail convergence just proved justifies the sum. For the second equality, the whole-line pairing is defined as the pairing with the compact distribution plus the absolutely convergent Schwartz integral. Their Fourier transforms are smooth functions. Their sum equals \(m\) as a tempered distribution by inversion, hence pointwise as smooth functions, which justifies evaluating at \(j\). No unproved summation formula is used.

Define convolution by this periodic kernel. On a smooth periodic function, it can either be evaluated as a distribution paired with \(u(x-\cdot)\), or term by term in its Fourier series. Section 13.2 proves convergence of that series in every smooth seminorm, which justifies the pairing and gives
\[
 Ru(x)=\int_0^{2\pi}K(x-y)u(y)\,dy,
 \qquad Re_j=m(j)e_j.
 \tag{CF6}
\]
The integral denotes distributional convolution. G1 shows that this is the unique bounded circle multiplier with the stated mode action.

On a short coordinate chart with \(|x-y|<\pi\), the terms with \(\ell\ne0\) in \(K(x-y)\) form a smooth kernel, with all derivatives converging absolutely. The remaining term is \(k(x-y)\), exactly the ordinary multiplier kernel of the symbol \(m\). Away from the circle diagonal the whole kernel is smooth, by the same estimate and the off-zero smoothness of \(k\). Localizing by chart cutoffs and using O4 therefore proves that \(R\) is an ordinary pseudodifferential operator of order \(-1\) on the circle, with principal symbol \(|\eta|^{-1}\). The circle is compact, so this operator is proper. This proves the precise calculus assertion used in Exercise 9.4 of the graph lesson.

Finally the tail norm in G1 is
\[
 \sup_{|j|>N}(1+j^2)^{-1/2}=(1+(N+1)^2)^{-1/2}\longrightarrow0.
 \tag{CF7}
\]
Thus the same operator is compact by finite-rank approximation, including the zero mode \(m(0)=1\). Translation preserves the circle density and has unit norm, so its composition with this regularizer remains compact. ∎
