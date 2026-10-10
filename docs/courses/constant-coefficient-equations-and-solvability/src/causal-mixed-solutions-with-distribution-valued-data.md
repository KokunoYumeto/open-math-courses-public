# Causal mixed solutions with distribution-valued data

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A boundary impulse is a natural datum even when it has no classical value at the initial corner. The appropriate class is smooth in the boundary-normal coordinate and distributional in the remaining variables. Causality replaces an initial trace that need not exist. We construct and characterize the unique solution in this class without a spatial growth condition.

Read [Compatible smooth mixed data and the data that determine a solution](compatible-smooth-mixed-data-and-determination.md), [Boundary fundamental kernels and their propagation support](boundary-fundamental-kernels-and-their-propagation-support.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies the Fourier convention and Gaussian formula; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies scalar calculus and cutoffs. [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html) supplies finite scalar and polynomial algebra. [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html), Section 6, supplies the complete-metric Baire theorem. [Tensor products and parameter-dependent distributions](../prerequisites/tensor-products-and-parameters.html) supplies compact parameter and tensor operations. [Convolution as addition of supports](../prerequisites/convolution-as-addition-of-supports.html) supplies proper convolution.

Existence uses the available cone theorem in [Real roots and their convex component](../AN02-L192.html#4-pass-to-multiple-roots-and-obtain-convexity), Theorem 4.1, and the planned analytic zero-order theorem stated in [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md). Uniqueness also uses the available local Holmgren theorem in [Analytic coefficients and one-sided uniqueness](../AN02-L191.html#3-a-continuously-differentiable-surface-needs-no-analytic-flattening), Theorem 3.2, and the two planned analytic support-normal and analytic convolution-ellipticity theorems stated in [Uniqueness from the principal boundary symbol](uniqueness-from-the-principal-boundary-symbol.md). The remaining planned uses are conditional on their specified proofs.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's treatment of constant-coefficient equations. The linked lessons supply the prerequisite proofs used below.

## The exact distribution class

Keep the balanced hyperbolic polynomial system, coordinates \(x=(a,x')=(a,z,t)\), cones C and S, and boundary operators \(B_k\) of [Boundary fundamental kernels and their propagation support](boundary-fundamental-kernels-and-their-propagation-support.md) and [Compatible smooth mixed data and the data that determine a solution](compatible-smooth-mixed-data-and-determination.md). In particular \(C,S\subset\{t\ge b|x|\}\) for some positive b. Data consist of a right-normal smooth family \(f(a)\in\mathcal D'(\mathbb R^{n-1}_{x'})\), \(a\ge0\), and distributions \(g_k\) on the boundary. Their supports lie in \(t\ge0\).

**Theorem.** There is exactly one right-normal smooth distribution family u such that
\[
\begin{gathered}
P(D)u=f\\
\quad(a>0),\\
\qquad
 B_k(D)u|_{a=0}=g_k,\\
\qquad
 \operatorname{supp}u\subset\{t\ge0\},\\
\qquad
 u\in C^\infty([0,\infty)_a;\mathcal D'_{x'}).
\end{gathered}
\tag{1}
\]
The equation holds for all tangent times as a distribution, including initial time. No classical time trace is asserted. This is the causal distribution version with zero Cauchy data, rather than a rule for multiplying a nonexistent initial trace. No separate formal corner compatibility is required for these causal boundary distributions.

Here smoothness means that pairing with each fixed compact smooth tangent test is a smooth scalar function of a, with all one-sided derivatives at zero. Its derivatives are distributions and smooth weak families. The local boundedness argument below verifies this last assertion if smoothness is initially given only through scalar pairings.

## Uniform orders and moving tests

For a compact tangent set K let \(\mathcal D_K\) be the space of smooth tests supported in K, with seminorms \(p_{K,q}\) given by all derivatives through order q. This space is complete: a seminorm-Cauchy sequence and all its derivatives converge uniformly; coordinate integral identities identify successive derivatives, and the limit vanishes outside K. The metric made from the countable seminorms is complete by the same limit argument.

If T(a) is a weakly continuous distribution family on a compact parameter interval I, every fixed test pairing is bounded. The closed sets of tests on which \(\sup_{a\in I}|T(a)(\phi)|\le l\), \(l=1,2,\ldots\), cover \(\mathcal D_K\). [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html), Section 6 gives one set an interior point. Subtracting the estimate at that point from its estimate at nearby tests gives a uniform bound on a neighborhood of zero. Such a neighborhood contains a condition \(p_{K,q}(\phi)<\epsilon\); scaling yields
\[
 \sup_{a\in I}|T(a)(\phi)|\le A\,p_{K,q}(\phi).
 \tag{2}
\]
If this seminorm is zero, scaling any multiple of the test in the neighborhood gives zero pairing. Thus no exceptional case is omitted. The same argument applies to any weakly continuous derivative family and to bounded families of difference quotients. Scalar convergence of difference quotients and 2 make their limits continuous linear test functionals; iterating proves that scalar weak smoothness has distribution-valued derivatives.

Uniform bounds also make weak convergence uniform on compact sets of tests. A finite net in the controlling seminorm bounds the error off the net, while convergence controls the finite net itself. In particular, if \(h(a,y)\) is a smooth test family with locally common compact support in y, then
\[
\begin{gathered}
\frac{d^j}{da^j}\langle T(a),h(a,\cdot)\rangle
   \\
=\sum_{\ell=0}^j\binom j\ell
       \langle T^{(\ell)}(a),\partial_a^{j-\ell}h(a,\cdot)\rangle .
\end{gathered}
\tag{3}
\]
For j=1, split the difference quotient into change of T against the fixed test and change of test against T at the new parameter. The first converges weakly; 2 bounds the Taylor remainder in the second. Compact-test uniform convergence gives continuity of both resulting pairings. Induction proves the full formula. The argument with several parameters proves the corresponding mixed derivatives and right endpoints. When only one factor varies, this is the compact-parameter lemma in [Tensor products and parameter-dependent distributions](../prerequisites/tensor-products-and-parameters.html); 2 supplies the additional moving-distribution step.

## Extending an existing right-normal family

An arbitrary sequence of distribution jets can have increasing orders, so [Compatible smooth mixed data and the data that determine a solution](compatible-smooth-mixed-data-and-determination.md)'s scalar parameter Borel series cannot simply be applied to it with a single fixed distribution estimate. Instead use values of the existing family. Put \(b_k=2^k\), \(k\ge0\), and define real coefficients
\[
 c_k=\prod_{\substack{j\ge0\\j\ne k}}
                \frac{-1-b_j}{b_k-b_j}.
 \tag{4}
\]
The factors with j<k form a finite product. For j>k the ratio is \((1+2^{-j})/(1-2^{k-j})\); its infinite product converges to a nonzero finite value. Indeed the sums of the numerator increments and denominator decrements converge, and \(-2x\le\log(1-x)\le0\) for \(0\le x\le1/2\), while \(0\le\log(1+x)\le x\). These inequalities follow by differentiating the two scalar functions.

The product truncated at N, denoted \(c_{k,N}\) for k≤N and zero otherwise, obeys a bound independent of N:
\[
\begin{gathered}
|c_{k,N}|,\ |c_k|
       \le e^4\,2^{-k(k-3)/2},\\
\qquad
           \sum_{k\ge0}|c_k|b_k^q<\infty\\
\quad(q\ge0).
\end{gathered}
\tag{5}
\]
For j<k, \((1+b_j)/(b_k-b_j)\le2^{j-k+2}\); multiplying gives the displayed power. The upper product is bounded by the exponential inequalities just given, with both geometric sums at most two. The resulting quadratic exponent beats any fixed linear exponent qk, proving the series statement, for example by comparing the ratio of late terms with 1/2.

Finite Lagrange interpolation at the distinct nodes \(b_0,\ldots,b_N\), evaluated at -1, gives \(\sum_{k=0}^Nc_{k,N}b_k^q=(-1)^q\) whenever q≤N. For completeness, the interpolation polynomial agrees with \(r^q\) at every node; their difference has degree at most N and N+1 distinct roots, so is zero by finite factorization. 5 controls tails uniformly in N, while each fixed coefficient converges. Passing first the finite head and then its uniformly small tail gives
\[
                 \sum_{k\ge0}c_k(-b_k)^q=1
                                      \quad(q=0,1,\ldots).
 \tag{6}
\]

Choose a smooth scalar cutoff χ on the nonnegative line, one near zero and zero for arguments ≥1. For a right-normal smooth family F, define
\[
\begin{gathered}
\widetilde F(a)\\
=  \begin{cases}
 F(a),&a\ge0,\\
 \displaystyle\sum_{k\ge0}c_k\,\chi(-b_ka)F(-b_ka),&a<0 .
 \end{cases}
\end{gathered}
\tag{7}
\]
The sum is locally finite at every negative a. For each derivative order q, the family \((\chi F)^{(q)}(v)\), \(0\le v\le1\), is uniformly bounded by one finite test seminorm on each compact tangent support, by 2 and the finite product formula. 5 therefore bounds its differentiated series uniformly in that seminorm, including as a approaches zero from the left. It defines a distribution, not merely separate scalar limits. 6 gives
\[
\begin{gathered}
\lim_{a\uparrow0}\partial_a^q\widetilde F(a)
   \\
=\sum_{k\ge0}c_k(-b_k)^q F^{(q)}(0)
   \\
=F^{(q)}(0).
\end{gathered}
\tag{8}
\]
All scalar derivatives match. The coordinate integral identities show that the joined scalar pairings are smooth, and 2 gives the required derivative distributions. This proves a smooth extension of every existing right-normal family. If F is supported in \(t\ge0\), the extension is too: the formula uses only scalar multiples of members of that same causal family. No common order across all q is assumed.

## A causal Cauchy solution smooth in the normal variable

Apply 7 to the given forcing and call its whole-normal extension F. It defines a full distribution by
\[
\begin{gathered}
\langle\mathcal F,\Psi\rangle
          =\int_{\mathbb R}\langle F(a),\Psi(a,\cdot)\rangle\,da,
                   \\
\qquad \operatorname{supp}\mathcal F\subset\{t\ge0\}.
\end{gathered}
\tag{9}
\]
2 on the compact normal interval and 3 for the varying test give continuity and ordinary integrability. Integration by parts in a identifies normal distribution derivatives with the integrated family derivatives.

[equation 6 in Compatible smooth mixed data and the data that determine a solution](compatible-smooth-mixed-data-and-determination.md) constructs E with \(P(D)E=\delta\) and support in C. Addition is proper on \(C\times\{t\ge0\}\); [equation 7 in Compatible smooth mixed data and the data that determine a solution](compatible-smooth-mixed-data-and-determination.md) consequently gives the full distribution \(E*\mathcal F\) as a causal solution. It is also a whole-normal smooth family, which requires an argument rather than an unverified restriction of E to a slice.

For a tangent test φ and a in a compact interval, use coordinates \((b,y)\) for E. Choose one compact smooth θ in these coordinates, equal to one on all relevant support pairs. Such a cutoff exists: if \(y+v\) belongs to the compact support of φ, \(v_t\ge0\), and \((b,y)\in C\), then \(0\le y_t\le\max_{\operatorname{supp}\phi}t\); C's positive time bound controls both b and y, hence also v. If that maximum is negative there are no relevant pairs. Define
\[
\begin{gathered}
\langle u_0(a),\phi\rangle
    \\
=\left\langle E(b,y),
        \\
\begin{gathered}\theta(b,y)\\
\left\langle F(a-b,v),\phi(y+v)\right\rangle\end{gathered}
      \right\rangle .
\end{gathered}
\tag{10}
\]
The inner expression is jointly smooth in a,b,y by 3, with one compact set of v for bounded y. The outer fixed distribution pairing and [Tensor products and parameter-dependent distributions](../prerequisites/tensor-products-and-parameters.html), Lemma 1.1, then prove all normal derivatives. 2 gives a finite seminorm bound in φ, so each result is a distribution. Integrating in a and using the tensor pairing with the same proper cutoffs identifies this family with \(E*\mathcal F\); the two iterated pairings agree by [Tensor products and parameter-dependent distributions](../prerequisites/tensor-products-and-parameters.html)'s tensor theorem. To commute the remaining scalar normal integral with the compact E pairing, approximate that integral by Riemann sums: every derivative through the finite order controlling E converges uniformly on the common compact product, by the already proved moving-test smoothness. Thus the distribution pairing commutes with the integral as well. Therefore
\[
\begin{gathered}
P(D)u_0=F,\\
\qquad
        u_0\in C^\infty(\mathbb R_a;\mathcal D'_{x'}),\\
\qquad
                    \operatorname{supp}u_0\subset\{t\ge0\}.
\end{gathered}
\tag{11}
\]
Equality of full distributions implies equality of these smooth families: pair a fixed tangent test, then every compact normal test; the resulting continuous scalar function must vanish. The construction covers characteristic boundary normals and operators independent of a. It never assumes that E itself has a classical normal trace.

## Correcting the boundary distributions

Normal family derivatives and polynomial tangent derivatives give every trace of \(B_ku_0\) at zero. Each is a causal distribution. Set
\[
                    \psi_k=g_k-B_k(D)u_0|_{a=0}.
 \tag{12}
\]
These residuals are already distributions supported in nonnegative time. There is no operation of extending a time trace across zero and no flatness condition to impose.

[Boundary fundamental kernels and their propagation support](boundary-fundamental-kernels-and-their-propagation-support.md) supplies a smooth right-normal distribution family \(e_k(a)\), with identity original boundary traces and joint support in S. Define
\[
\begin{gathered}
v(a)=\sum_{k=1}^h e_k(a)*\psi_k,\\
\qquad
                             u=u_0+v\\
\quad(a\ge0),
\end{gathered}
\tag{13}
\]
where convolution is tangent only. It is proper uniformly on compact normal intervals: the S time bound controls each kernel displacement when its sum with a causal residual lies in a compact tangent output set. Derivatives of the kernel family have the same support bound. Indeed a point outside the closed joint support has a product neighborhood where every member vanishes, and all parameter derivatives vanish there too.

Choose independent compact cutoffs in the two tangent input variables, equal to one on all relevant pairs for a fixed compact output set and compact normal interval. For a fixed output test the convolution pairing is then a tensor pairing of the cut-off family \(e_k(a)\) and the fixed cut-off residual. Weak difference quotients of the first factor converge to its derivatives and are uniformly bounded by 2. [Tensor products and parameter-dependent distributions](../prerequisites/tensor-products-and-parameters.html), Theorem 3.1, on sequential tensor limits proves convergence of the paired difference quotients; its same argument proves continuity. Induct on derivative order. This establishes weak smoothness and commutation of all normal derivatives, with the tangent derivative identities supplied by [Convolution as addition of supports](../prerequisites/convolution-as-addition-of-supports.html).

Consequently
\[
\begin{gathered}
P(D)v=0\\
\quad(a>0),\\
\qquad
 B_j(D)v|_0=\psi_j,\\
\qquad
        \operatorname{supp}v\subset\{t\ge0\}.
\end{gathered}
\tag{14}
\]
Equations 11–14 prove existence. When h=0, the correction sum is empty. All data may have arbitrary spatial growth; each required pairing has been made proper by its actual causal support.

## Uniqueness by smoothing into positive time

Let w be the difference of two solutions. It is a right-normal smooth causal distribution family with zero equation and zero boundary traces. Choose compact smooth tangent approximate identities of integral one, with
\[
\begin{gathered}
\operatorname{supp}\rho_\epsilon
       \subset\{|z|\le\epsilon,\ \epsilon<t<2\epsilon\},
                  \\
\qquad w_\epsilon(a)=w(a)*\rho_\epsilon .
\end{gathered}
\tag{15}
\]
For example scale a fixed product bump supported in the indicated unit box, choosing a slightly smaller box in its interior. Pairing w with the translated bump and applying 3 gives a jointly smooth function of a,z,t, including right normal derivatives. Proper convolution with the compact bump commutes with every polynomial differential operator and trace. Thus
\[
\begin{gathered}
P(D)w_\epsilon=0,\\
\qquad
 B_k(D)w_\epsilon|_0=0,\\
\qquad
            \operatorname{supp}w_\epsilon\subset\{t\ge\epsilon\}.
\end{gathered}
\tag{16}
\]
Every classical initial time jet is zero. [Uniqueness from the principal boundary symbol](uniqueness-from-the-principal-boundary-symbol.md)'s smooth arbitrary-growth causal uniqueness theorem makes \(w_\epsilon=0\) on \(a,t\ge0\), and its support makes it zero for negative time as well.

For each fixed a and tangent test φ, the inverse-translated bump average converges to φ with every derivative on one compact support. Taylor's integral identity, or uniform continuity of each test derivative on that compact set, proves this directly. Continuity of the distribution \(w(a)\) gives
\[
                 w_\epsilon(a)\longrightarrow w(a)
                        \quad\hbox{weakly in }\mathcal D'_{x'}.
 \tag{17}
\]
Hence w(a)=0 for every a. This proves uniqueness in exactly the claimed class. Only this uniqueness step uses [Uniqueness from the principal boundary symbol](uniqueness-from-the-principal-boundary-symbol.md)'s two further planned analytic entries and the available Holmgren theorem; existence retains the two [Incoming normal roots at a flat boundary](incoming-normal-roots-at-a-flat-boundary.md) cone/order entries.

## Exercises with complete solutions

**Exercise 1 (entry: an incoming boundary impulse).** For \(P(w,s)=(s-i)^2-w^2\) and Dirichlet boundary datum \(\delta_0(t)\), with zero forcing, construct the causal normal-smooth solution. Explain why a smooth-data corner condition cannot be required of this datum.

**Solution.** [Boundary fundamental kernels and their propagation support](boundary-fundamental-kernels-and-their-propagation-support.md)'s Dirichlet kernel gives
\[
                     u(a,t)=e^{-a}\delta(t-a),\qquad a\ge0 .
 \tag{18}
\]
Its test pairing is \(e^{-a}\phi(a)\), a smooth function of a, including zero. Differentiating the translated delta distribution yields
\[
\begin{gathered}
D_a^ju(a,t)=i^je^{-a}
          \\
\sum_{k=0}^j\binom jk\,\delta^{(k)}(t-a),\\
\qquad j\ge0 .
\end{gathered}
\tag{19}
\]
The j=1 formula follows by differentiating the damping and the translation; induction with the product rule gives the full binomial coefficients. Substitution of j=0,1,2 in the shifted wave operator, or the Fourier multiplier \(e^{-a-ias}\), verifies the zero interior equation. The right boundary trace is \(\delta(t)\), and support is the causal ray \(t=a\). The datum has no ordinary smooth Taylor series at t=0. Nevertheless it is a valid causal boundary distribution and has the unique solution 18. The theorem does not turn it into a classical smooth corner datum.

**Exercise 2 (intermediate: causality with a characteristic spatial boundary).** Take \(P(D)=D_t\), no boundary operators, and forcing \(f(a,t)=\delta(t)\), independent of a. Find the causal solution and explain the sense of zero Cauchy data.

**Solution.** The time principal value is one and the normal polynomial has degree zero. Thus h=0, the empty determinant is one, and the mixed system is hyperbolic. Its causal interior inverse in \((a,t)\) is
\[
                         E(a,t)=i\,\delta(a)H(t).
 \tag{20}
\]
Indeed \(D_tH=-i\delta\), so \(D_tE=\delta(a)\delta(t)\). Its support is the positive time axis, the polar of the full time half-space with unrestricted normal covector. Proper convolution, or direct integration, gives
\[
                   u(a,t)=iH(t),\qquad D_tu=\delta(t).
 \tag{21}
\]
This is a constant, hence smooth, normal family of tangent distributions and is causal. It has a jump in time and no canonical classical value at t=0. A homogeneous solution of \(D_tu=0\) is constant in time, and causality forces that constant distribution to be zero; this also follows from the theorem. Zero Cauchy data here means the causal distribution problem. It does not require assigning a zero one-sided value to \(iH\). Notice that E itself contains a normal delta at zero; 10 constructs the smooth solution family without assuming a normal trace of E.

**Exercise 3 (advanced: why finite extrapolation misses higher jets).** Use only the nodes \(1,2,4,8\) in the Lagrange construction of 4. Compute its coefficients and moments. Apply this finite extension to the scalar function \(F(a)=a^4\).

**Solution.** Evaluating the four Lagrange polynomials at -1 gives
\[
\begin{gathered}
(c_{0,3},c_{1,3},c_{2,3},c_{3,3})
                       \\
=(45/7,-15/2,9/4,-5/28).
\end{gathered}
\tag{22}
\]
For example the first coefficient is
\((-3)(-5)(-9)/[(-1)(-3)(-7)]=45/7\); the other three follow from omitting their respective node factors. Exact summation gives
\[
\begin{gathered}
\sum_{k=0}^3c_{k,3}(-2^k)^q=1\ (0\le q\le3),\\
\qquad
                   \sum_{k=0}^3c_{k,3}(-2^k)^4=-269 .
\end{gathered}
\tag{23}
\]
For the fourth moment, the interpolation error for \(r^4\) is the monic nodal product. At r=-1 its value is \((-2)(-3)(-5)(-9)=270\), so the interpolant has value \(1-270=-269\). This gives the same sum without a decimal computation. Choose the cutoff to be one near zero. The finite extension of \(a^4\) is \(-269a^4\) on a small negative interval and \(a^4\) on the positive interval. Its derivatives through order three match at zero, but its fourth derivatives are \(-269\cdot24\) and 24. It is not a smooth extension. The infinite construction passes every moment, not just a chosen finite number, while 5 permits all derivative limits.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Open lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
