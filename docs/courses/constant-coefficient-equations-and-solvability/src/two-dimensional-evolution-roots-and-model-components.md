# Two-dimensional evolution roots and model components

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

In two variables the characteristic roots can be followed all the way around infinity. Their leading phases and the first lower powers determine whether a fixed complex ball can always find an upper root value. We prove the finite-cover expansion, the complete root criterion, and the dominated comparison with polynomial model operators. The sufficient solvability and component statements use the root-barrier equivalence and its planned Holmgren theorem.

Read [Analytic root barriers and supported solvability](analytic-root-barriers-and-supported-solvability.md), [Evolution operators in a component of equal strength](evolution-operators-in-a-component-of-equal-strength.md), [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md), [Primitive factors and moving polynomial roots](primitive-factors-and-moving-roots.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies the Schwartz Fourier transform; [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html) supplies finite algebra and matrices; Boundary flux and weak identities supplies the complex Green identity.

One prerequisite remains planned in [Distributions, kernels and analytic singularities](../prerequisites/planned-foundation-proofs.html): a distribution solving an analytic-coefficient equation and vanishing on one side of a noncharacteristic \(C^1\) surface vanishes near that surface. The sufficient solvability and component uses here are conditional on that planned Holmgren proof.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's treatment of constant-coefficient equations. The linked prerequisite lessons supply the proofs used below.

## Conventions and the complete statement

Use \(D=-i\partial\), tangential frequency \(z\), normal frequency \(s\), and \(H=\{t\ge0\}\). An evolution polynomial is a nonzero \(P\in\mathbb C[z,s]\) satisfying the five equivalent conditions of [Analytic root barriers and supported solvability](analytic-root-barriers-and-supported-solvability.md)/[Supported fundamental solutions and test estimates](supported-fundamental-solutions-and-test-estimates.md)/[Global supported solvability on countably many scales](global-supported-solvability-on-countably-many-scales.md), with the planned Holmgren theorem in the sufficient direction. Set
\[
\begin{gathered}
S_P(\xi,T)=
 \left(\sum_\alpha T^{2|\alpha|}
                  |\partial^\alpha P(\xi)|^2\right)^{1/2},
 \\
\qquad T\ge1.
\end{gathered}
\tag{1}
\]
Domination means \(\sup_{\xi\in\mathbb R^2}S_R(\xi,1)/S_P(\xi,T)\to0\) as \(T\to\infty\), exactly as in [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md). It does not mean decay of the ratio at spatial frequency infinity.

**Theorem.** Every nonzero \(P(z,s)\) has finitely many normal root branches at infinity, counted with multiplicity. After a finite cover, each nonzero branch has a convergent expansion
\[
\begin{gathered}
\tau(z)=\sum_{j=-\infty}^{k}c_j z^{j/p},
 \\
\qquad p\in\mathbb Z_{\ge1},\\
\quad c_k\ne0.
\end{gathered}
\tag{2}
\]
An identically zero branch is treated as bounded. The polynomial is an evolution polynomial if and only if every branch is either bounded, or has one of these two forms:

* its leading exponent is a positive even integer and its leading coefficient has strictly positive imaginary part;
* its leading exponent is a positive integer \(M\), its leading coefficient is nonzero and real, and every coefficient with exponent strictly between \(M-1\) and \(M\) vanishes.

Branches and every sheet of their finite cover are included. A polynomial with normal degree zero has no normal branches and satisfies the criterion.

Write \(a(z)\) for the leading normal coefficient, \(a(z)=a_0z^\mu+O(z^{\mu-1})\), with \(a_0\ne0,\mu\ge0\). Let \(q_0\) count the bounded normal branches, and write \(c_jz^{M_j}\), \(j=1,\ldots,h\), for the leading terms of the unbounded branches. Then, whenever the root criterion holds, the polynomial
\[
 p_0(z,s)=a_0z^\mu s^{q_0}
                  \prod_{j=1}^{h}(s-c_jz^{M_j})
 \tag{3}
\]
has equal strength to \(P\), \(P-p_0\ll p_0\), and \(P\) belongs to the same connected equal-strength component as \(p_0\). Conversely every member of such a component is an evolution polynomial.

In this model bounded branches are replaced by zero. Their possibly nonreal constant terms are dominated corrections. This explicit convention gives a polynomial normal form even when a bounded branch has a fractional or negative leading exponent. 

## A finite cover and a convergent Laurent series

Factor \(P\) by the Gauss/UFD proof in [Primitive factors and moving polynomial roots](primitive-factors-and-moving-roots.md). Factors independent of \(s\) contribute no analytic normal root on an open \(z\)-disk: a nonzero polynomial in \(z\) cannot vanish identically there. For an irreducible factor \(Q(z,s)\) of positive normal degree \(q\), [Uniqueness in a slab with bounded support](bounded-support-slab-uniqueness.md)'s nonmonic Sylvester argument supplies a nonzero exceptional polynomial whose zeros include all leading-coefficient zeros and all multiple-fiber points. Choose \(R>1\) beyond its finitely many complex zeros.

On \(|z|>R\), all \(q\) roots are simple and have local holomorphic graph charts by [Primitive factors and moving polynomial roots](primitive-factors-and-moving-roots.md)'s implicit-function proof. On the convex logarithmic half-plane \(\{\operatorname{Re}w>\log R\}\), the equation \(Q(e^w,s)=0\) has global analytic labels. Here is the needed continuation argument in full.

Along a compact path in this half-plane, the leading coefficient has a positive minimum and all polynomial coefficients have finite maxima. The elementary weighted root bound in [Regular balls, moving roots and complex gauges](regular-balls-moving-roots-and-complex-gauges.md) therefore bounds every root. Local implicit charts cover the compact set of parameter-root pairs over the path. A finite subcover and uniform continuity permit a subdivision of the path such that its successive parameter pieces stay in chart neighborhoods. Continuation is forced by the value of the preceding piece; simple roots cannot switch inside a chart. It exists to the path's endpoint because all roots remain in that compact bounded set.

For two paths homotopic with fixed endpoints, the homotopy image is compact. The same leading lower bound, root upper bound and finite chart cover apply on this image. Uniform continuity allows a rectangular subdivision of the homotopy square fine enough that each parameter rectangle lies in a neighborhood carrying all its distinct root graphs. Continuation around that rectangle returns to the initial graph. The opposite internal edges of adjoining rectangles cancel as path continuation followed by its inverse. The two remaining boundary paths consequently have the same endpoint label. Straight interpolation homotopes any path to its straight segment in the convex half-plane. Thus labels are well-defined there and agree with the local holomorphic charts.

Translation \(w\mapsto w+2\pi i\) permutes these labels. The permutation is fixed: identify it near one point, and then the analytic identity principle propagates the same equality throughout the connected half-plane. A selected permutation cycle has finite length \(p\le q\), hence its label \(F\) obeys
\[
\begin{gathered}
F(w+2\pi ip)=F(w),\\
\qquad
 \tau(u^p)=F(p\log u)\\
\quad (|u|>R^{1/p}).
\end{gathered}
\tag{4}
\]
Changing the local logarithm of \(u\) changes \(p\log u\) by an integer multiple of \(2\pi ip\); the right side is therefore a single-valued holomorphic function of \(u\) on that exterior disk. All labels arise this way. Repeated irreducible factors simply repeat their labels.

The weighted polynomial root bound, together with the leading coefficient's lower polynomial bound outside a sufficiently large disk, gives an integer \(L\ge0\) and constant \(C\) such that
\[
 |\tau(u^p)|\le C(1+|u|)^L.
 \tag{5}
\]
Set \(v=1/u\), \(h(v)=\tau(v^{-p})\). For an integer \(N\ge L\), the holomorphic function
\[
\begin{gathered}
g(v)=v^N h(v),\\
\qquad 0<|v|<R^{-1/p},
 \\
\qquad |g(v)|\le C'
\end{gathered}
\tag{6}
\]
has a removable singularity at zero. To prove that assertion locally, apply the complex Green identity of Boundary flux and weak identities to \(g(\zeta)/(\zeta-v)\) on an annulus with a small circle around \(v\) removed. It is holomorphic there; the integral on the small circle at \(v\) tends to \(2\pi i g(v)\) by continuity. This gives the outer circle Cauchy integral minus the inner circle integral. The latter tends to zero as the inner radius tends to zero, because \(g\) is bounded and \(|\zeta-v|\) stays bounded away from zero. The outer integral defines a holomorphic function on its interior by its uniformly convergent denominator power series. It equals \(g\) at every nonzero interior point and supplies its extension at zero.

The disk Cauchy series of this extension now gives
\[
\begin{gathered}
h(v)=\sum_{\ell=-N}^{\infty}b_\ell v^\ell,
 \\
\qquad
 \tau(u^p)=\sum_{j=-\infty}^{N}c_j u^j.
\end{gathered}
\tag{7}
\]
Only finitely many positive powers occur, and convergence is uniform on sufficiently large closed circles in \(u\), including every argument. Taking the last nonzero positive or zero index, or the first nonzero negative index, proves 2. If all coefficients vanish, the branch is identically zero. The geometric majorants on smaller \(v\)-disks allow termwise differentiation and uniform remainder bounds. This proves the finite-cover Puiseux expansion here; it does not import the still separately audited monodromy sentence in older [Symbols at infinity](symbols-at-infinity.md).

## Which leading phases are possible

Assume the receiving root condition with fixed radius \(A>0\) and height \(B\). For all sufficiently large real centers \(c\), every simple root label is analytic on \(B(c,A)\). If a branch has leading exponent \(\lambda=k/p>0\), 7 and termwise differentiation give, uniformly in every sheet,
\[
 |\tau'(z)|\le C|z|^{\lambda-1}
 \quad(|z|>R_1).
 \tag{8}
\]
Integrate this derivative along the segment from \(c\) to any point of the fixed ball. The root-height condition consequently implies
\[
\begin{gathered}
\operatorname{Im}\tau(c)
 \\
\ge B-C_A|c|^{\lambda-1}
 \\
\ge-C_A'(1+|c|^{\lambda-1}).
\end{gathered}
\tag{9}
\]
The second form is valid also when \(\lambda<1\). Only this fixed-ball oscillation estimate is needed for the necessity argument.

For \(z=r e^{i\nu\pi}\), \(r>R_1\), every integer \(\nu\) is an available lift on the cover. Its leading imaginary coefficient is
\[
 \operatorname{Im}\bigl(c_k e^{ik\nu\pi/p}\bigr).
 \tag{10}
\]
A negative value would give a negative term of order \(r^{k/p}\), contradicting 9, whose negative allowance is of strictly smaller order. Every value in 10 is therefore nonnegative.

Put \(\omega=e^{ik\pi/p}\). If \(\omega\ne1\), its finite cyclic sum is zero, by the geometric-sum identity. The imaginary parts of \(c_k,c_k\omega,\ldots\) are nonnegative and have sum zero, so each is zero. A nonzero complex number can have all those rotated values real only if \(\omega\) has order at most two: the first value makes \(c_k\) real, and the next makes \(\omega\) real. Order two means \(k/p\) is an odd integer and \(c_k\) is real. If \(\omega=1\), \(k/p\) is an even integer and \(\operatorname{Im}c_k\ge0\). These conclusions are exactly
\[
\begin{gathered}
k/p=M\in\mathbb Z_{>0},\qquad
 \\
\begin{cases}
  c_k\in\mathbb R\setminus\{0\},&M\text{ odd},\\
  \operatorname{Im}c_k\ge0,&M\text{ even}.
 \end{cases}
\end{gathered}
\tag{11}
\]
When \(k\le0\), 7 already gives a bounded branch and imposes no sign condition on its finite limit.

Suppose the leading coefficient is real and there is a nonzero coefficient with \(k-p<j<k\). Choose the largest such \(j\). The leading term \(c_kz^M\) is real at either real center, on every lifted sheet. All the intervening coefficients above \(j\) vanish by its choice. The exponent \(j/p\) is not an integer, so the same finite-phase argument supplies a lift with
\[
\begin{gathered}
\operatorname{Im}\tau(r e^{i\nu\pi})
 =-b\,r^{j/p}+o(r^{j/p}),\\
\qquad
 b>0,\\
\quad j/p>M-1.
\end{gathered}
\tag{12}
\]
This contradicts 9 for the leading exponent \(M\). Every intermediate coefficient must vanish. This proves necessity of all three root cases, including the bounded case.

## A common radius and height for all branches

Conversely suppose every branch has the stated form. A bounded branch has a uniform bound outside a disk, by the uniform Laurent remainder. A branch with positive imaginary leading coefficient and positive even exponent \(M\) has, at real \(c\),
\[
\begin{gathered}
\operatorname{Im}\tau(c)
 =(\operatorname{Im}c_k)c^M+o(|c|^M)\ge0
 \\
\quad\text{for sufficiently large }|c|.
\end{gathered}
\tag{13}
\]
There are only finitely many labels, so thresholds and bounds can be chosen in common.

For a real-leading branch the vanished intermediate band yields
\[
\begin{gathered}
\tau(z)=b z^M+E(z),\\
\qquad
 b\in\mathbb R\setminus\{0\},\\
\quad
 |E(z)|\le C|z|^{M-1}.
\end{gathered}
\tag{14}
\]
Choose a fixed \(\delta>0\) with \(M|b|\delta>4C\), for every such label. At real \(c\), choose \(y=\delta\,\operatorname{sign}(b c^{M-1})\). The finite binomial formula and 14 give
\[
\begin{gathered}
\operatorname{Im}\tau(c+iy)
 \\
\ge (M|b|\delta-2C)|c|^{M-1}
          -C_\delta |c|^{M-2}\\
\ge0
\end{gathered}
\tag{15}
\]
for sufficiently large \(|c|\). For \(M=1\) the binomial remainder is zero and the same choice directly gives a positive constant. Uniform Laurent bounds make these estimates valid on all sheets; there is no freely chosen incompatible label at \(c+iy\).

Fix \(A>\max(\delta,R+1)\). Increasing the large-center threshold if necessary ensures that every ball with large real center lies in the exterior regular region. Any analytic normal root of \(P\) on such a ball lies in one of the irreducible factors identically: if a finite product of holomorphic functions vanishes on a connected domain, the identity principle makes one factor identically zero. Local distinctness then identifies that root with one of the already estimated sheets. Its supremum is bounded below by the bounded-branch bound or by 13/15.

For the remaining centers \(|c|\le C_0\), set \(b_c=c+\operatorname{sign}_0(c)(R+1)\), where \(\operatorname{sign}_0(0)=1\). Then
\[
\begin{gathered}
|b_c-c|=R+1<A,\\
\qquad
 R+1\le |b_c|\le C_0+R+1.
\end{gathered}
\tag{16}
\]
The leading coefficient is nonzero on this compact real annulus. The elementary polynomial root bound therefore bounds every normal root there in absolute value by one constant \(M_0\). Evaluation at \(b_c\) gives height at least \(-M_0\), for every analytic root on the original ball. A common radius and height have been established for all real centers. [Analytic root barriers and supported solvability](analytic-root-barriers-and-supported-solvability.md)'s full-frequency/tangential adapter and the root-barrier equivalence prove supported solvability, with the planned Holmgren use in the sufficient direction.

## The polynomial model and the large-window comparison

Form the polynomial \(p_0\) in 3, replacing bounded branches by zero and retaining every unbounded branch with multiplicity. Put \(r_j(x)=c_jx^{M_j}\) for its unbounded roots and \(r_j=0\) for its bounded roots. Every \(M_j\) is a positive integer. For the tangential factor its scaled derivative norm satisfies
\[
 S_{z^\mu}(x,T)\asymp(|x|+T)^\mu,
 \tag{17}
\]
including \(\mu=0\). The upper bound is its finite derivative sum; the lower follows from its undifferentiated term and its \(\mu\)-th derivative. Constants depend on the fixed degree and coefficient.

Write \(W_j=S_{s-r_j}(x,s,T)\). For a real unbounded coefficient and \(|x|\ge2T\), direct differentiation gives
\[
 W_j\asymp |s-c_jx^{M_j}|
                     +T|x|^{M_j-1}.
 \tag{18}
\]
Indeed the first tangential derivative supplies the second term; the normal derivative supplies \(T\), which is bounded by a constant times that second term when \(M_j\ge1\). Every higher tangential derivative is bounded by a constant times \(T|x|^{M_j-1}\) because \(T/|x|\le1/2\).

For a heat coefficient, \(\operatorname{Im}c_j>0\) and \(M_j\) is even. The real linear map \((s,u)\mapsto s-c_ju\) is invertible, so its Euclidean norm bounds \(|s|+|u|\) below. With \(u=x^{M_j}\) and \(|x|\ge2T\),
\[
 W_j\asymp |s|+|x|^{M_j}.
 \tag{19}
\]
The same derivative upper bounds give the reverse comparison. For a bounded model root, \(W_j=(s^2+T^2)^{1/2}\asymp|s|+T\).

At real \(|x|\) large, the leading coefficient differs from \(a_0x^\mu\) by \(O(|x|^{\mu-1})\), if \(\mu>0\); for \(\mu=0\) it is exactly constant. A bounded root differs from zero by \(O(1)\). A real-type root differs from \(r_j\) by \(O(|x|^{M_j-1})\). A heat-type root differs by \(O(|x|^{M_j-\epsilon_j})\) for some \(\epsilon_j>0\), by its convergent expansion. Choose \(0<\epsilon\le1\) below all the finitely many \(\epsilon_j\).

For \(|x|\ge2T\), each root difference divided by its \(W_j\) is at most \(C T^{-\epsilon}\): use 18 for real roots, 19 for heat roots and \(|s|+T\) for bounded roots. The leading-coefficient difference divided by \((|x|+T)^\mu\) obeys the same bound. Telescope the finite product \(a(x)\prod(s-\tau_j(x))\) against 3. Every unchanged or changed factor is bounded by a constant times its model norm. [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md)'s product-norm lemma now proves
\[
\begin{gathered}
|P(x,s)-p_0(x,s)|\\
\le
 C T^{-\epsilon}S_{p_0}(x,s,T)
 \\
(|x|\ge2T,\ \\
T\text{ sufficiently large}).
\end{gathered}
\tag{20}
\]
No individual branch factor needs to be a polynomial for this pointwise telescoping: only their product \(P\) and the model \(p_0\) are used in the norm lemma.

We must also control \(|x|\le2T\), including singular finite fibers. Order the unbounded exponents \(M_1\ge\cdots\ge M_h\ge1\), and write
\[
\begin{gathered}
P-p_0=\sum_{r=0}^{q}d_r(x)s^{q-r},\\
\quad q=h+q_0,\qquad
 \\
\begin{cases}
 \begin{gathered}\deg d_r\le\mu\\
+\sum_{j=1}^{r}M_j-1,\end{gathered}&0\le r\le h,\\
 \begin{gathered}\deg d_r\le\mu\\
+\sum_{j=1}^{h}M_j,\end{gathered}&h<r\le q .
 \end{cases}
\end{gathered}
\tag{21}
\]
A negative degree bound means the polynomial is zero. Here is why these coefficient bounds hold. Coefficients are the leading coefficient times elementary symmetric root products. For \(r\le h\), their largest possible growth power is \(\mu+\sum_{j=1}^rM_j\); bounded-root factors cannot attain that power, since replacing any selected positive exponent by zero loses at least one. Among unbounded roots, the products of leading monomials with that maximal power agree in \(P\) and \(p_0\). The differences are little-oh of that power, because each unbounded root has remainder little-oh of its leading term and the leading coefficient has relative error \(O(1/x)\). The difference coefficient is a polynomial with integer degree, so little-oh forces degree at most one less. For \(r>h\), at most all \(h\) positive exponents can occur; remaining roots are bounded and contribute no positive growth. This proves the second bound. This reasoning uses absolute-value bounds along the positive real ray and is unaffected by cancellation of several leading products.

On \(|x|\le2T\), direct differentiation shows \(W_j\ge cT^{M_j}\) for an unbounded factor, using its highest tangential derivative. Since \(|c_jx^{M_j}|\le C T^{M_j}\), its undifferentiated term also gives \(|s|\le W_j+C T^{M_j}\). Thus \(W_j\ge c'(|s|+T^{M_j})\); the bounded factor gives \(|s|+T\) directly. Consequently the product-norm lower bound yields
\[
\begin{gathered}
S_{p_0}(x,s,T)\ge
 c T^\mu
       \\
\prod_{j=1}^{h}(|s|+T^{M_j})(|s|+T)^{q_0},
 \\
|x|\le2T.
\end{gathered}
\tag{22}
\]
For \(r\le h\), the positive product on the right contains the term \(T^{\sum_{j=1}^rM_j}|s|^{q-r}\). 21 bounds the corresponding numerator term by \(C T^{\mu+\sum_{j=1}^rM_j-1}|s|^{q-r}\). For \(r>h\), use the term \(T^{\sum_{j=1}^hM_j+r-h}|s|^{q-r}\), which gains at least one power beyond the coefficient bound. Sum these finitely many comparisons. We obtain \(|P-p_0|\le (C/T)S_{p_0}\) throughout the remaining region, including \(x=0\) and every finite leading-coefficient zero.

Combine this with 20 and use [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md) Proposition3.1, which upgrades the undifferentiated bound to the full derivative definition:
\[
\begin{gathered}
\sup_{(x,s)\in\mathbb R^2}
       \frac{|P(x,s)-p_0(x,s)|}{S_{p_0}(x,s,T)}
 \\
\le C T^{-\epsilon}\longrightarrow0,\\
P-p_0\ll p_0.
\end{gathered}
\tag{23}
\]
This includes \(q=0\): 21 is then just the lower-degree remainder of \(a(z)\), and the empty products in 22 are one.

Every basic normal factor of \(p_0\) has imaginary root value nonnegative at its real center: it is zero for real \(c_j\), nonnegative for heat coefficients with even exponent, and zero for bounded model factors \(s\). A holomorphic root of their product equals one of them identically, by the analytic product identity. The tangential factor contributes no root on an open disk. Hence \(p_0\) satisfies a root barrier of radius one and height zero and is an evolution polynomial relative to the root-barrier equivalence.

Finally [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md) Lemma3.3 gives equal strength on the entire continuous path
\[
 p_0+\lambda(P-p_0),\qquad 0\le\lambda\le1.
 \tag{24}
\]
All these polynomials are nonzero. The path is connected in coefficient topology and lies in one equal-strength class, so its endpoints belong to the same connected component. [Evolution operators in a component of equal strength](evolution-operators-in-a-component-of-equal-strength.md) proves that evolution solvability is constant on that component. Conversely every symbol in a component containing a model of 3 is an evolution symbol by [Evolution operators in a component of equal strength](evolution-operators-in-a-component-of-equal-strength.md); the necessity already proved then supplies its root cases. This completes the two-dimensional root and component classification. It does not assert path connectedness of every component.

## Exercises with complete solutions

**Exercise 1 (entry).** Classify
\[
\begin{gathered}
P(z,s)\\
=z(s-z^3-i z^2)(s-i z^2-z)
\end{gathered}
\tag{25}
\]
and give its polynomial model. Identify each of the three types of factor.

**Solution.** The first normal root is \(z^3+i z^2\). Its leading coefficient is real, its positive exponent is three, and its first lower term has exponent \(M-1=2\), which is allowed; there is no intervening fractional term. The second root is \(i z^2+z\), with positive imaginary leading coefficient and even exponent two. The leading normal coefficient is \(z\). Thus \(p_0=z(s-z^3)(s-i z^2)\), and 23 proves \(P-p_0\ll p_0\). The factor \(z\) is tangential; \(s-z^3\) has Schrödinger-type real dispersion, while \(s-i z^2\) is of heat type. The dominated path 24 puts \(P\) in the same strength component as this supported-solvable model. The tangential factor is permitted even though the time normal is characteristic for the highest total-degree part.

**Exercise 2 (intermediate).** Explain why a real positive integer leading exponent alone does not suffice for
\[
\begin{gathered}
Q(z,s)=(s-z^2)^2-z^3,\\
\qquad
 \tau_\pm(z)=z^2\pm z^{3/2}.
\end{gathered}
\tag{26}
\]
Check directly how one fixed-radius ball violates every proposed height bound.

**Solution.** On the cover \(z=u^2\), the roots are \(u^4\pm u^3\). Here \(p=2,k=4\), and the nonzero term at \(j=3\) lies strictly between \(k-p=2\) and \(k=4\). It is forbidden. At a negative real center \(z=-r\), one analytic sheet has value \(r^2-i r^{3/2}\). On any fixed-radius disk about that center, sufficiently large \(r\) makes the disk disjoint from zero, so the sheet is analytic there. Its derivative is \(2z\) plus or minus \((3/2)z^{1/2}\), bounded by \(C_A r\) on that disk. Its imaginary supremum is therefore at most \(-r^{3/2}+C_A r\), which tends to minus infinity. This defeats every fixed height. The naive model \((s-z^2)^2\) cannot supply a valid dominated comparison: on \((x,s)=(r,r^2)\), its derivative norm grows only as \(r^2\), while the correction \(z^3\) grows as \(r^3\). This confirms the necessity of the intermediate-band condition.

**Exercise 3 (advanced).** For \(P(z,s)=z(s^2+1)-1\), identify the bounded branches and model, and prove domination directly. Explain why the negative limiting root causes no obstruction.

**Solution.** For large \(z\), the roots solve \(s^2=-1+1/z\) and tend to \(i\) and \(-i\). The finite-cover construction and the implicit charts at these two distinct limits give bounded branches, so both satisfy the bounded case, irrespective of the sign of their limit. The model is \(p_0=zs^2\), and \(P-p_0=z-1\). Direct differentiation gives, for real \(x,s\) and \(T\ge1\),
\[
\begin{gathered}
S_{z-1}(x,s,1)^2=(x-1)^2+1\\
\le C(x^2+1),\\
S_{zs^2}(x,s,T)^2\\
\ge4T^4x^2+4T^6.
\end{gathered}
\tag{27}
\]
Thus the full derivative-norm ratio is at most \(C'/T^2\), uniformly in both frequencies. At \(s=0,T=1\), however, \(S_{zs^2}^2=4x^2+4\), and the same ratio tends to \(1/2\) as \(x\to+\infty\). Domination is the large-window property, not that frequency limit. The negative branch stays near the fixed height \(-1\), so it never escapes every uniform lower height; a root barrier allows a finite negative height. The path \(zs^2+\lambda(z-1)\) remains equally strong and connects this equation to the model.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Open lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
