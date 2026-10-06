# Working with logarithmic Fourier graphs

*Complete solved exercises accompanying [Logarithmic Fourier graphs construct a cone-supported inverse](manuscript.md). Original exposition: CC0. Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026.*

The exercises use the exact conventions of Theorem 1.1: pairings are complex-linear, \(\widehat\mu(\zeta)=\langle\mu,e^{-ix\cdot\zeta}\rangle\), and the test factor is \(F_\phi(\zeta)=\widehat\phi(-\zeta)\). Their cone is nonempty, ordinarily convex, open, dilation-invariant, and excludes zero. The original source's broader convention remains unresolved. No exercise silently upgrades that statement.

## 1. A complex determinant is not a surface-area factor

**Problem.** Let \(n=2\), \(u=(4,2)\), and \(h(\xi)=\log(2+\xi_1^2+\xi_2^2)\). Write the complete derivative matrix of \(z(\xi)=\xi+iuh(\xi)\), expand its determinant, and explain what multiplies \(d\xi_1\wedge d\xi_2\) in the graph integral.

**Solution.** Put \(t=2+\xi_1^2+\xi_2^2\). The matrix is

\[
A=\begin{pmatrix}
1+8i\xi_1/t&8i\xi_2/t\\
4i\xi_1/t&1+4i\xi_2/t
\end{pmatrix}.
\]

Its determinant is

\[
(1+8i\xi_1/t)(1+4i\xi_2/t)
-(8i\xi_2/t)(4i\xi_1/t)
=1+i(8\xi_1+4\xi_2)/t.
\]

The quadratic terms cancel exactly. Thus \(z^*(dz_1\wedge dz_2)=\det(A)d\xi_1\wedge d\xi_2\). The factor is the displayed complex number, including its imaginary part; replacing it by \(|\det A|\) would change the differential form and destroy the closed-form calculation in Section 5. Its real part equals one, so it is never zero.

## 2. A logarithmic height must dominate its own contribution to frequency

**Problem.** For \(\mu=\delta'_0\), \(C=2\), and \(\Gamma=(0,\infty)\), prove that every graph \(z_L(\xi)=\xi+iL\log(2+\xi^2)\), \(L\ge12\), lies in \(\operatorname{Im}z>2\log(|z|+2)\). Also verify the reciprocal bound with \(p=A=0\).

**Solution.** Write \(r=|\xi|\), \(t=2+r^2\), \(h=\log t\). We have \(r\le t\), \(2\le t\), and \(h\le t\), hence \(|z_L|+2\le r+Lh+2\le(L+2)t\). Therefore

\[
2\log(|z_L|+2)\le2\log(L+2)+2h.
\]

It is enough to have \((L/2-1)\log2>\log(L+2)\). At \(L=12\), its left side is \(5\log2=\log32>\log14\). The difference has derivative \(\tfrac12\log2-1/(L+2)>0\) for \(L\ge12\), so the inequality continues to hold. This proves the threshold, including at \(\xi=0\). Moreover \(\widehat\mu(z)=iz\), whose only zero is zero. On the stated region, \(|1/(iz)|\le1/\operatorname{Im}z<1/(2\log2)<2\), proving (1.6) with the same \(C=2\). The contribution \(Lh\) to \(|z|\) has been included in the argument.

## 3. A finite test order can be large and still prove continuity

**Problem.** Suppose a graph in dimension two has already been validated, and on it \(p=3\), \(U=L|\theta|=6\), \(A=1\). Test supports lie in a compact set with \(R_B=2\). Use (4.8) to find a valid test derivative order for absolute convergence. Use (5.11) to find one that also proves the cutoff side term tends to zero. Does this establish a global finite order for \(E\)?

**Solution.** Here \((p+n)/2=5/2\), and \(U(A+R_B)=18\). Condition (4.8) is \(N>21.5\), so \(N=22\) gives a bound through order \(2N=44\) on this fixed compact support. For the side term, (5.11) requires \(N>22.5\); choose \(N=23\), hence order 46. The choice is conservative and no optimality is claimed. It assumes the graph's zero-free threshold has been checked separately; the numbers in this problem do not certify that threshold. As \(B\) changes, \(R_B\), and consequently the required order, may change. This is precisely enough for a distribution in \(\mathcal D'\), and is not a claim of one global finite order or temperedness.

## 4. Compute a moving-graph side coefficient

**Problem.** In dimension two, let \(u(s)=(1,s)\), \(0\le s\le1\), and \(v=\nabla h\). For a holomorphic coefficient \(f\), compute the vector \(B\) in (5.5). Suppose along this homotopy \(|f(Z(s,\xi))|\le D(1+|\xi|^2)^{-4}h^6\). Prove that the side term for \(\chi_R\) tends to zero.

**Solution.** Here \(u'=(0,1)\), \(u\cdot v=v_1+sv_2\), and \(v\cdot u'=v_2\). Thus

\[
B=f(Z)h\left((0,i)-(0,v_1+sv_2)+(v_2,sv_2)\right)
=f(Z)h(v_2,i-v_1).
\]

The bound \(|v|\le1/\sqrt2\) gives \(|B|\le D'|f(Z)|h\). For \(R\ge1\), the annulus \(R\le|\xi|\le2R\) has area at most \(D''R^2\), and \(|\nabla\chi_R|\le D_\chi/R\). The absolute right side of (5.8) is consequently bounded by

\[
D''' R(1+R^2)^{-4}\bigl(\log(2+4R^2)\bigr)^7
=O\bigl(R^{-7}(\log R)^7\bigr),
\]

which tends to zero. This is a compact cutoff estimate, not an appeal to an unspecified contour at infinity. Its holomorphicity assumption must hold on a neighborhood of the entire truncated homotopy; if \(f=qF_\phi\), that requires the explicit no-zero check.

## 5. Find the convolution reflection sign with a translated point mass

**Problem.** Let \(\mu=\delta_a\) in \(\mathbb R^n\). Calculate \(g_\phi\), \(F_{g_\phi}\), and the inverse obtained by the graph formula. Compare its support function with the bound obtained by taking \(A=|a|\).

**Solution.** The reflected test is \(g_\phi(x)=\phi(x+a)\). With \(v=x+a\),

\[
F_{g_\phi}(\zeta)=e^{-ia\cdot\zeta}F_\phi(\zeta)
=\widehat\mu(\zeta)F_\phi(\zeta).
\]

Here \(\widehat\mu=e^{-ia\cdot\zeta}\) has no zeros, and \(q=e^{ia\cdot\zeta}\). The graph formula has coefficient

\[
e^{ia\cdot\zeta}F_\phi(\zeta)
=\int\phi(x)e^{i(x+a)\cdot\zeta}dx.
\]

This is the entire transform factor associated with the test \(\psi(v)=\phi(v-a)\). Equations (6.1)–(6.3) deform it to the real plane and give \(E(\phi)=\psi(0)=\phi(-a)\). Thus \(E=\delta_{-a}\), and \(\mu*E=\delta_0\). Its exact support function is \(H_K(\theta)=-a\cdot\theta\). Since \(|q(\xi+iy)|=e^{-a\cdot y}\le e^{|a||y|}\), the general theorem with \(A=|a|\) gives the valid, possibly nonsharp estimate \(-a\cdot\theta\le|a||\theta|\). The transform multiplier has the sign in (7.6); changing it would yield the wrong point mass.

## 6. Strictly beyond the supporting plane

**Problem.** In (8.1), why is the condition \(d>0\) used rather than \(d\ge0\)? Exhibit an inverse for which the distribution does not vanish on the bounding plane. Prove the uniform scale absorption (8.4) without assuming that each scale integral separately converges.

**Solution.** If \(d>0\), the factor \(e^{-dLh}\) defeats every fixed power of \(L\), uniformly after one half of its decay is used to make a majorant. If \(d=0\), that decay disappears and the same proof fails. The equation \(\delta_0*\delta_0=\delta_0\), with \(A=0\), has inverse \(E=\delta_0\) supported on the plane \(x\cdot\theta=0\). A test nonzero at zero has nonzero pairing, so the conclusion must concern the open half-space \(x\cdot\theta>0\), not the closed one.

For the absorption, set \(c=d\log2/2>0\). Since \(h\ge\log2\), \((1+L)^k e^{-dLh/2}\le(1+L)^k e^{-cL}\). Expand \((1+L)^k=\sum_{j=0}^k\binom kj L^j\). The \(j=0\) term is at most one; for \(j>0\), differentiating \(L^j e^{-cL}\) gives its maximum \((j/(ce))^j\). Their finite sum gives a constant independent of \(L\). The remaining half of the exponential is at most one, leaving the integrable majorant (8.5). That one bound, followed by pointwise decay, is what permits dominated convergence.

## 7. Opposite directions do not select the same derivative inverse

**Problem.** Prove that \(E_+=-H(-x)\) and \(E_-=H(x)\) both satisfy \(E'=\delta_0\). Compute their supports and difference. Prove that no compactly supported inverse exists. Explain exactly which hypothesis of Theorem 1.1 prevents identifying them by a direction deformation.

**Solution.** For a compact smooth test,

\[
E_+'(\phi)=\int_{-\infty}^0\phi'(x)dx=\phi(0),
\qquad E_-'(\phi)=-\int_0^\infty\phi'(x)dx=\phi(0).
\]

The densities are nonzero on every open interval strictly within their respective half-lines, and vanish on the opposite open half-lines. Their supports are therefore exactly \(( -\infty,0]\) and \([0,\infty)\). Their difference pairs as \(\int_0^\infty\phi+\int_{-\infty}^0\phi=\int_\mathbb R\phi\), the constant distribution one. The first has finite support function in positive directions; the second has finite support function in negative directions.

If \(E\) had compact support and \(E'=\delta_0\), choose a compact smooth \(\chi\) equal to one near \(\operatorname{supp}E\cup\{0\}\). Then \(\chi'=0\) near that support, and \(E'(\chi)=-E(\chi')=0\); but \(\delta_0(\chi)=1\). This contradiction proves the obstruction. Ordinary convexity of a cone containing \(+1\) and \(-1\) would put their midpoint zero in it. The punctured cone in Theorem 1.1 excludes zero; hence it cannot contain both directions. In dimension one the punctured union of the two rays is also disconnected and not ordinarily convex. No permitted homotopy connects the two graphs through the required zero-free logarithmic region.

## 8. A delay inverse is unique on its support side, but can grow exponentially

**Problem.** For \(v>0\), \(c>1\), prove every assertion in Example 9.2 and show that the inverse supported in \([0,\infty)\) is unique among distributions with that support. Explain why that uniqueness does not require Fourier transforming the inverse.

**Solution.** The atoms at \(jv\) meet a compact set only finitely often, so \(E(\phi)=\sum_{j\ge0}c^j\phi(jv)\) is locally a finite sum of order-zero distributions. It therefore satisfies a finite local test bound. The shift by \(v\) gives

\[
c\delta_v*E=\sum_{j\ge0}c^{j+1}\delta_{(j+1)v}
=\sum_{j\ge1}c^j\delta_{jv}.
\]

Subtracting from \(E\) leaves \(\delta_0\), exactly in \(\mathcal D'\). Every coefficient is nonzero at a distinct atom, so the support is the discrete set \(v\mathbb N_0\), and its closed convex hull is \([0,\infty)\). Its supporting value is zero at negative directions.

The compact transform is \(1-ce^{-iv\zeta}\). A zero must satisfy \(ce^{vy}=1\) and \(e^{-iv\xi}=1\), giving \(y=-(\log c)/v\), \(\xi=2\pi k/v\). When \(y<-(\log(2c))/v\), the second term has modulus below \(1/2\), so the reciprocal has modulus at most two. Choosing \(C\ge\max\{2,\log(2c)/(v\log2)\}\) makes the theorem's negative logarithmic-height region lie there.

For non-temperedness, choose a fixed compact bump \(\rho\) supported in \((-v/3,v/3)\), with \(\rho(0)=1\), and set \(\rho_j(x)=\rho(x-jv)\). Then \(E(\rho_j)=c^j\). Every fixed Schwartz seminorm of \(\rho_j\) is at most a constant times a power of \(1+j\), since the derivatives are fixed translates and their support lies within \(v/3\) of \(jv\). A continuous tempered functional has a bound by finitely many of those seminorms, contradicting \(c^j\)'s exponential growth.

For uniqueness, subtract two supported inverses to obtain \(T\) supported in \([0,\infty)\) with \(T=c\delta_v*T\). Iterating the distributional equality gives \(T=c^m\delta_{mv}*T\), whose support lies in \([mv,\infty)\). For a fixed compact test choose \(m\) so large that its support lies below \(mv\); its pairing with \(T\) is zero. Every test vanishes this way, so \(T=0\). The argument uses only shifts and support. In particular it identifies the graph-constructed inverse with the explicit sum without introducing a transform of that non-tempered sum.

## 9. A half-space cone in several dimensions

**Problem.** In \(\mathbb R^n\), take \(\mu=\partial_{x_1}\delta_0\), \(\Gamma=\{\theta:\theta_1>0\}\), and

\[
E(\phi)=-\int_{-\infty}^0\phi(s,0,\ldots,0)ds.
\]

Prove the convolution equation, the exact support, and the reciprocal condition on every closed angular subcone. Does \(\overline\Gamma\) have to be pointed?

**Solution.** Integration by parts gives

\[
\partial_{x_1}E(\phi)
=\int_{-\infty}^0\partial_{x_1}\phi(s,0,\ldots,0)ds
=\phi(0).
\]

Thus \(\mu*E=\delta_0\). The distribution vanishes off the closed negative first-coordinate ray, and every neighborhood of a point on that ray contains a test whose restriction to the ray has a nonzero integral. Its support and closed convex hull are that ray. Consequently \(H_K(\theta)=0\) when \(\theta_1\ge0\), and \(+\infty\) when \(\theta_1<0\).

For a closed angular subcone with a nonzero direction, compactness of its unit directions inside \(\Gamma\) gives \(\varepsilon>0\) with \(y_1\ge\varepsilon|y|\) there. The compact transform is \(i\zeta_1\), so it is nonzero when \(y_1>0\), and

\[
|1/(i\zeta_1)|\le1/y_1\le1/(\varepsilon|y|).
\]

Choosing \(C\ge\max\{1,1/(\varepsilon\log2)\}\), the logarithmic region has \(|y|>C\log2\), and the last quantity is at most \(C\). This proves the hypothesis with \(A=p=0\). A cone containing only zero has an empty height region and needs no estimate. For \(n\ge2\), \(\overline\Gamma=\{\theta_1\ge0\}\) contains every line in the hyperplane \(\theta_1=0\). Our open cone excludes zero and opposite interior directions, but its closure need not be pointed. That distinction is why the chapter states its convention explicitly.

## 10. Why one common distribution is necessary

**Problem.** Suppose \(\theta_0,\theta_1\) belong to a cone satisfying (1.1). Prove that the straight segment stays a positive distance from zero, that its generated ray cone is closed, and that graph equality really identifies the original ray constructions even when their reciprocal constants differ.

**Solution.** Convexity puts every segment point in \(\Gamma\); none equals zero. Its norm is continuous on a compact interval, so its minimum \(m\) is attained and positive. If \(\rho_j\theta(s_j)\) converges, its boundedness and \(m>0\) bound \(\rho_j\). Subsequence compactness yields a limit \(\rho\theta(s)\), proving that the generated ray cone is closed. It is contained in \(\Gamma\cup\{0\}\) by dilation invariance.

Use that cone's constants to choose one common scale \(L\) large enough for (3.8); also make it at least the two individual ray thresholds. The original ray graph at \(\theta_0\) can first be raised to \(L\) using its own ray estimate; Section 5 proves equality on that finite safe scale interval. Do the same for \(\theta_1\). The segment deformation at the common scale is uniformly zero-free by the generated cone's estimate, and its cutoff side term vanishes by (5.10). Thus the original constructions agree. Repeating with arbitrary pairs gives one \(E\), so each directional half-space bound applies to its same support. Different constants are allowed; different unidentified inverses would not prove simultaneous support control.

The background credit and exact proof dependencies remain those of the main manuscript. The solved examples use only its proved graph construction, compact-factor convolution, finite test continuity, and the stated support definition. They do not require the unresolved unrestricted source convention or a paid proof.
