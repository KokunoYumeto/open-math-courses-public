# Pulling back and combining analytic singularities

*Written by GPT-6.1 Sol (OpenAI), October 2026.  Public domain (CC0).*

A singular distribution can sometimes be restricted to a curve, multiplied by another singular distribution, or integrated along a fiber. The decision depends on covectors. A pullback must not annihilate a singular covector. A product must not join opposing singular covectors. A projection retains only source covectors whose fiber component is zero.

Basic references are [Detecting regularity without choosing coordinates][G] for the exact smooth operations, [Analytic directions of holomorphic boundary values][A] for analytic-wavefront sequences, and Brouder, Dang and Hélein [B] for the normal topology and continuity results. The [complete proof](pulling-back-and-combining-analytic-singularities-formal.md) supplies the analytic estimates and exact operation statements. [Dilation equations and tangential analytic singularities][E] gives the sphere-transversality input used below.

## 1. A transpose derivative decides whether a pullback exists

For a smooth map \(F:X\to Y\), its normal set consists of the nonzero target covectors killed by its transpose derivative:
\[
 N_F=\{(F(x),\eta):\eta\ne0,\ DF(x)^T\eta=0\}.
 \tag{1}
\]
If this set misses the ordinary wavefront of \(u\), the smooth pullback exists. Its wavefront has the bound
\[
 \operatorname{WF}(F^*u)
       \subseteq\{(x,DF(x)^T\eta):(F(x),\eta)\in\operatorname{WF}(u)\}.
 \tag{2}
\]
For an analytic map, the corresponding analytic condition and bound are
\[
 N_F\cap\operatorname{WF}_A(u)=\varnothing,\qquad
 \operatorname{WF}_A(F^*u)
       \subseteq\{(x,DF(x)^T\eta):(F(x),\eta)\in\operatorname{WF}_A(u)\}.
 \tag{3}
\]
All displayed wavefront covectors are nonzero. The analytic condition implies smooth existence, because ordinary wavefront is contained in analytic wavefront.

An embedding is the restriction case. Its killed covectors are exactly the conormals of the embedded submanifold. For a diffeomorphism the transpose derivative is invertible, so the bounds become equalities. The scalar distributional pullback includes the absolute determinant of the inverse map on tests; the covector map itself remains \(DF^T\).

The analytic proof is local. It writes the pullback Fourier transform with phase
\[
 \Phi(x,\xi,\eta)=F(x)\cdot\eta-x\cdot\xi,\qquad
 \nabla_x\Phi=DF(x)^T\eta-\xi.
 \tag{4}
\]
Where this gradient has a uniform lower bound by \(d(|\xi|+|\eta|)\), \(L\) integrations by parts with a controlled cutoff give
\[
 \left|\int b_L(x)e^{i\Phi(x,\xi,\eta)}dx\right|
       \leq C^{L+1}L^L(1+|\xi|+|\eta|)^{-L}.
 \tag{5}
\]
The complete proof retains the differentiated analytic coefficients and shows why they produce just one analytic factorial scale. Regular input directions supply the other part of the integral. The choice \(L=N+m+a+2\), for target dimension \(a\) and compact input order \(m\), gives the analytic-wavefront estimate at order \(N\). Its localized output sequence has a fixed plateau, common compact support and a common finite-order bound.

![Two parabolic maps meet the same singular line, with their exact derivative vectors and opposite outcomes for the normal covector.](figures/transverse-and-tangential-traces.png)

*Figure 1. The singular support is \(s=0\). The maps are \(F(r)=(r,r^2)\) and \(G(r)=(r^2,r)\), at \(r=0\). Their actual derivative vectors are \(DF(0)=(1,0)\) and \(DG(0)=(0,1)\). The normal covector \(ds\) pairs to one and zero respectively. The right panel uses the Euclidean identification to draw that covector; its arrow is translated vertically by \(4/25\) solely for visibility. The base point and the transpose pairings remain at zero. See Example 3, Solution 1, complete-proof Theorem 4.1 and Corollary 6.1.*

## 2. Zero components matter in tensors and products

Adjoin the zero covector over the support:
\[
 Z_u=\{(x,0):x\in\operatorname{supp}u\},\qquad
 \operatorname{WF}_{\star,0}(u)=\operatorname{WF}_{\star}(u)\cup Z_u,
          \quad \star\in\{\text{ordinary},A\}.
 \tag{6}
\]
The tensor bound is
\[
 \operatorname{WF}_{\star}(u\otimes v)
    \subseteq
       \big(\operatorname{WF}_{\star,0}(u)\times
                  \operatorname{WF}_{\star,0}(v)\big)\setminus0.
 \tag{7}
\]
For instance \(u\otimes1\) can be singular even though the constant factor has empty wavefront. Its covectors have zero component in that smooth factor.

Multiplication is pullback to the diagonal:
\[
 uv=\Delta^*(u\otimes v),\qquad
 \Delta(x)=(x,x),\qquad D\Delta^T(\xi,\eta)=\xi+\eta.
 \tag{8}
\]
Thus a sufficient condition is the absence of pairs \(\xi,-\xi\) in the two wavefront sets at the same point. Under the ordinary condition the product exists. Under the analytic condition it also has the analytic sum bound:
\[
 \operatorname{WF}_{\star}(uv)
 \subseteq\{(x,\xi+\eta):
       (x,\xi)\in\operatorname{WF}_{\star,0}(u),\
       (x,\eta)\in\operatorname{WF}_{\star,0}(v)\}\setminus0.
 \tag{9}
\]
The zero components retain the single-factor terms. This is a sufficient condition, so failure of the condition does not by itself prove that every particular proposed product is impossible.

## 3. Projection integration needs proper support

Let \(\pi(x,y)=x\). If its restriction to \(\operatorname{supp}u\) is proper, integration in \(y\) defines \(\pi_*u\). A compact target test sees a compact source support, so a cutoff in \(y\) makes its lifted test legitimate and does not change the pairing.

The smooth and analytic bound is
\[
 \operatorname{WF}_{\star}(\pi_*u)
    \subseteq\{(x,\xi):\xi\ne0,\
        (x,y;\xi,0)\in\operatorname{WF}_{\star}(u)
                                      \text{ for some }y\}.
 \tag{10}
\]
Only zero fiber covectors contribute. For a compact source distribution the Fourier identity is simply
\[
 \widehat{\pi_*u}(\xi)=\widehat u(\xi,0).
 \tag{11}
\]
The analytic proof uses finite controlled partitions near the compact fiber. Their sum is one there, while their high derivatives retain the single analytic scale. It then applies (11) to their localized sequences.

## 4. Four worked examples

### Example 1: a positive ray has a well-defined sphere trace.

In the plane let \(u=H(s)\delta_0(t)\), the positive-ray distribution. It has degree \(-1\). The Euler theorem [E], Theorem 4.1, places its wavefront covectors at nonzero base points in \(s\xi+t\eta=0\). Sphere conormals are nonzero multiples of \((s,t)\), with nonzero radial pairing. Therefore restriction to every circle of radius \(a>0\) exists, by complete-proof Corollary 6.1.

Parameterize the circle by \(j(\theta)=(a\cos\theta,a\sin\theta)\), and use test density \(d\theta\). Near \(\theta=0\) the positive-ray factor is one, and the scalar delta composition is
\[
 \delta_0(a\sin\theta)=\frac1a\delta_0(\theta).
 \tag{12}
\]
Indeed the coordinate \(r=a\sin\theta\) has derivative \(a\) at zero; the scalar pullback of a point delta carries the reciprocal absolute derivative. Near \(\theta=\pi\) the positive-ray factor is zero, and outside those two possible intersections the line delta vanishes. Thus the full periodic trace is one angular point delta with coefficient \(1/a\).

At the positive-ray point \((a,0)\), the original covectors are \((0,\eta)\), of either nonzero sign. The transpose of \(Dj=(0,a)^T\) sends them to \(a\eta\), giving every nonzero angular covector at \(\theta=0\). Formula (12) confirms this exact fiber. The coefficient is stated for \(d\theta\); converting the test density to arclength \(a\,d\theta\) converts its pairing accordingly.

### Example 2: transverse poles multiply, while opposing poles can diverge.

The upper pole \(p(r)=(r+i0)^{-1}\) has only positive covectors at zero, with the convention in [A], Example 1. Put
\[
 u(s,t)=p(s),\qquad v(s,t)=p(t).
 \tag{13}
\]
Their covectors lie respectively in the positive horizontal and positive vertical frequency directions, so they never oppose. The product is \(p(s)\otimes p(t)\), and the analytic sum bound at the crossing is the closed positive quadrant with zero removed.

This is the exact fiber, as proved for the same two-pole distribution in [A], Example 4. The tensor transform is \((-2\pi i)^2H(\xi)H(\eta)\). For any compact cutoff equal to one at zero, convolution with its Schwartz transform approaches the nonzero constant \(-4\pi^2\) along each interior positive-quadrant ray. Ordinary wavefront therefore contains those rays; closedness adds the two boundary rays. The analytic upper bound and ordinary inclusion give the exact analytic quadrant. Along either occupied axis away from the crossing, only the positive normal covectors remain.

In contrast, on one line the regularized opposite poles give
\[
 \frac1{r+i\varepsilon}\frac1{r-i\varepsilon}
                 =\frac1{r^2+\varepsilon^2}.
 \tag{14}
\]
For a nonnegative compact test \(\psi\) with \(\psi(0)>0\),
\[
 \varepsilon\int\frac{\psi(r)}{r^2+\varepsilon^2}\,dr
     =\int\frac{\psi(\varepsilon z)}{1+z^2}\,dz
            \longrightarrow\pi\psi(0)>0.
 \tag{15}
\]
Dominated convergence uses \(\|\psi\|_\infty/(1+z^2)\). The unscaled pairings diverge. This proposed common regularization has no distributional limit. Its two singular covectors oppose, exactly the obstruction left out of the product theorem.

### Example 3: the map matters even for the same line delta.

Let \(U(s,t)=\delta_0(s)\). Its smooth and analytic wavefront at \((0,t)\) is exactly \((\tau,0)\), \(\tau\ne0\). The tensor bound gives the upper inclusion; the Fourier transform of a localized trace is independent of the normal frequency and supplies both signs for the ordinary lower bound.

For \(F(r)=(r,r^2)\),
\[
 DF(r)^T(\tau,0)=\tau,
             \qquad F^*U=\delta_0(r).
 \tag{16}
\]
It is transverse at the only intersection \(r=0\). Both smooth and analytic fibers there are every nonzero one-dimensional covector.

For \(G(r)=(r^2,r)\), the transpose sends the same covector to \(2r\tau\), which vanishes at zero. Transversality fails. The Gaussian regularization
\[
 g_\varepsilon(s)=(4\pi\varepsilon)^{-1/2}e^{-s^2/(4\varepsilon)}
 \tag{17}
\]
would give \(g_\varepsilon(r^2)\). Its test pairing is
\[
 \int g_\varepsilon(r^2)\psi(r)\,dr
   =\frac{\varepsilon^{-1/4}}{\sqrt{4\pi}}
       \int e^{-z^4/4}\psi(\varepsilon^{1/4}z)\,dz.
 \tag{18}
\]
The integral after the prefactor tends to a positive constant when \(\psi(0)>0\). For nonnegative \(\psi\), dominated convergence is immediate from the integrable quartic exponential. Thus these pairings diverge like \(\varepsilon^{-1/4}\). This natural proposed trace has no distributional limit.

### Example 4: a fold projects a smooth curve density to a singular density.

Choose a real compact smooth \(\chi(t)\), equal to one near zero, and define
\[
 w(\Psi)=\int\chi(t)\Psi(t^2,t)\,dt.
 \tag{19}
\]
Its support is a compact portion of a parabola, so \(\pi(s,t)=s\) is proper on its support. Substitution at the two roots gives the projected density, for \(s>0\),
\[
 (\pi_*w)(s)
       =\frac{\chi(\sqrt s)+\chi(-\sqrt s)}{2\sqrt s},
              \qquad(\pi_*w)(s)=0\quad(s<0).
 \tag{20}
\]
Near zero this is \(H(s)/\sqrt s\), a locally integrable density that is not smooth at zero. Its realness makes ordinary wavefront symmetric under covector negation: Fourier conjugation replaces a qualifying cutoff by its conjugate and reverses the frequency. In one dimension there are only two direction rays. Absence of both would imply smoothness, so both occur. Ordinary inclusion gives every nonzero analytic covector at zero; away from zero the local density is analytic.

The source covectors near the vertex explain where this happens. The analytic coordinate map \(\kappa(s,t)=(s-t^2,t)\) has determinant one and carries \(w\), where \(\chi=1\), to the line-delta model. Its normal covectors are
\[
 (s,t;\tau,-2t\tau),\qquad s=t^2,\quad\tau\ne0.
 \tag{21}
\]
The projection rule retains a covector only when \(-2t\tau=0\), hence only at \(t=0\). Its source base projects to \(s=0\), exactly the singular point of (20).

![The fold curve and both signs of its exact conormals, beside the projected square-root density and its full nonzero origin fiber.](figures/fold-projection-and-zero-fiber-covectors.png)

*Figure 2. The source curve is \(s=t^2\), shown for \(|t|\leq17/20\). Its marked parameters are \(t=-2/5,0,2/5\), with conormal segments \(\lambda(1,-2t)\), \(\lambda=\pm11/50\), drawn at equal Euclidean coordinate scales. Projection retains only zero \(t\)-covector components, hence only the marked vertex. The cutoff is one for \(|t|\leq1/2\) and supported in \(|t|\leq1\); its projected density is exactly \(H(s)/\sqrt s\) in the displayed interval \(-3/20<s\leq1/4\). The density graph's finite vertical window clips its divergence, which is labelled. The right panel represents both one-dimensional covector rays at \(s=0\), with zero removed. See Example 4, Solution 7 and complete-proof Theorem 7.1.*

## 5. Convergence must retain both directions and support

For a fixed closed ordinary wavefront bound \(\Gamma\), sequential convergence requires weak distributional convergence and convergence of every rapid Fourier seminorm on a compact cutoff and closed cone disjoint from \(\Gamma\). The normal topology uses those seminorms together with uniform pairings on bounded compact-test families. For sequences the two convergence descriptions agree by the complete bounded-test argument [Q], Lemma 3.2.

The complete proof gives normal-topology continuity for a transverse pullback and proper projection. Tensor and nonopposing product are hypocontinuous: continuity in one factor is uniform over a bounded set of the other. They are consequently sequentially continuous. Brouder, Dang and Hélein [B] give the named normal-topology theorems and Alesker's counterexample for the weaker topology.

A projection limit also needs one common proper support. For example
\[
 w_j=\delta_{(0,j)}\quad\hbox{on }\mathbb R^2
                       \longrightarrow0
 \tag{22}
\]
on every bounded compact-test family: eventually every test in such a family has support away from the point. The corresponding local rapid Fourier seminorms also become exactly zero. Yet \(\pi_*w_j=\delta_0\) for every \(j\). Each individual point support is proper, while their closed union over \(s=0\) is not proper. The missing common-support condition explains the failure of the projected limit.

## 6. Exercises, 100 points

1. **Transpose geometry, 10 points.** For \(F(r)=(r,r^2)\), compute \(DF^T(\xi,\eta)\). Identify its normal directions at \(r=0\). Apply this to \(\delta_0(s)\) and \(\delta_0(t)\), explaining which trace is transverse. Compute the transverse trace and its coefficient.
2. **One analytic scale, 12 points.** In complete-proof Lemma 3.1, derive the identity used to sum the multi-index product coefficients, bound the sum (25), and justify the induction (24). Explain why multiplying two factorial scales would lose the required analytic estimate.
3. **A controlled partition, 12 points.** For three cutoffs between zero and one, use (15) of the complete proof to write all partition functions and sum them. Prove the fixed plateau and both kinds of derivative bounds. Explain why each partition support remains inside its own regular neighborhood.
4. **Tensor zeros and positive sums, 14 points.** Determine the full analytic wavefront of \(\delta_0(s)\otimes1\). Explain the needed zero term in the tensor bound. For the two upper poles of Example 2, give their exact analytic fibers on each support axis and at the crossing, including the boundary directions of the quadrant.
5. **Opposition and a divergent product, 12 points.** Derive the diagonal normal set and the sum map on covectors. Use it to explain the two cases in Example 2. Prove (15), with its constant, and show that (14) has no distributional limit.
6. **The sphere trace coefficient, 12 points.** For the positive-ray distribution, prove that its trace on a circle of radius \(a>0\) is the periodic angular delta divided by \(a\), in test density \(d\theta\). Compute the transported covectors at the intersection and explain the arclength pairing.
7. **The fold and the forbidden trace, 14 points.** Derive both (18) and (20), including all constants. Determine the exact source conormals and the smooth/analytic wavefront of the projected density near zero. Explain why the proper projection is allowed while the tangential trace in Example 3 is not supplied by the restriction theorem.
8. **The actual convergence conditions, 14 points.** Describe the normal topology and its sequential convention precisely. Explain how hypocontinuity gives convergence of products for two convergent sequences with fixed nonopposing wavefront bounds. Prove the failure in (22), including its local Fourier seminorms, and identify exactly which common-support hypothesis fails.

## 7. Complete solutions

### Solution 1

The derivative is the column \((1,2r)^T\), so
\[
 DF(r)^T(\xi,\eta)=\xi+2r\eta.
\]
At zero the normal directions are \((0,\eta)\), \(\eta\ne0\).
The line delta \(\delta_0(s)\) has covectors \((\xi,0)\), \(\xi\ne0\), at \(s=0\), so none is normal to this map. Its first coordinate is \(r\), giving the point delta \(\delta_0(r)\) with coefficient one, because that derivative is one. Its complete fiber has both nonzero signs.

The line delta \(\delta_0(t)\) has covectors \((0,\eta)\) at \(t=0\). At the intersection \(r=0\) these are killed. Thus the theorem does not define its trace along \(F\). It is the same scalar difficulty as \(\delta_0(r^2)\) in Example 3: applying the Gaussian regularization in the \(t\) variable gives (18), whose pairings diverge for a nonnegative test nonzero at zero.

### Solution 2

For \(\alpha\) of total order \(p\), the coefficient of \(t^s\) in
\[
 \prod_i(1+t)^{\alpha_i}=(1+t)^p
\]
is both \(\sum_{|\beta|=s,\beta\leq\alpha}\binom\alpha\beta\) and \(\binom ps\). This proves the exact sum identity.
Since \(p\leq L\),
\[
 \binom ps s!=p(p-1)\cdots(p-s+1)\leq L^s.
\]
With \(D\geq2B_1\), the sum of the factors in complete-proof (25) is bounded by
\[
 B_0\sum_{s=0}^p(B_1/D)^s\leq2B_0.
\]
The bound is independent of \(p,L\).

In the induction, \(k\) integrations and \(p\) remaining derivatives have total budget \(k+p\leq L\). A derivative term \(b_j\partial_j\) uses one more amplitude derivative. Splitting \(s\) derivatives onto \(b_j\) leaves \(p-s+1+k\leq L\) for the induction hypothesis. The preceding sum bounds the product rule by a fixed multiple of \((DL)^{p+k+1}\). The zeroth-order coefficient leaves one less derivative and is also bounded by this expression because \(DL\geq1\). Absorb the fixed number of coefficients into \(C_1\), proving (24).

At \(k=L,p=0\), the bound is \(C^{L+1}L^L\). Multiplication by \(R^{-L}\) comes from the \(L\) normalized integration operators. The analytic coefficient factorials have already been absorbed by the geometric product sum. Adding another \(L!\) would instead produce an extra scale of order \(L^L\), and would not establish the bounded-sequence analytic criterion. The calculation prevents that extra factor.

### Solution 3

The three functions are
\[
 p_1=\chi_1,\qquad
 p_2=(1-\chi_1)\chi_2,\qquad
 p_3=(1-\chi_1)(1-\chi_2)\chi_3.
\]
Their sum is \(1-(1-\chi_1)(1-\chi_2)(1-\chi_3)\).
It equals one wherever one cutoff equals one. Thus plateaux covering the compact set give a fixed neighborhood on which the sum equals one for every \(L\).

Each \(p_j\) contains its own factor \(\chi_j\), so its support is contained in \(\operatorname{supp}\chi_j\). Every derivative of \(\chi_j\) is also supported there, and the extension by zero outside the chart is smooth.
For a derivative of total order \(k\leq L\), the full product rule distributes the derivatives among at most three factors. Their multinomial coefficient sum is at most \(3^k\). Each factor contributes a bound \(C(CL)^{k_i}\), and the total powers sum to \(k\). Hence the bound is \(C'(3CL)^k\), with a fixed number of zeroth-order constants absorbed into \(C'\). For any fixed derivative order, use the uniform fixed-order bounds of all factors; the finite product rule then gives a bound independent of \(L\). No reciprocal normalization of the cutoffs is needed.

### Solution 4

A one-dimensional point delta has every nonzero smooth and analytic covector at zero, [E], Example 3. The constant factor has empty wavefront and full support. The tensor bound therefore permits exactly
\[
 \{(0,t;\xi,0):t\in\mathbb R,\ \xi\ne0\}.
\]
Every permitted direction occurs in ordinary wavefront. For any cutoff equal to one near \((0,t_0)\), the localized transform is
\[
 \widehat{\chi(\delta_0\otimes1)}(\xi,\eta)
                  =\widehat{\chi(0,\cdot)}(\eta).
\]
The nonzero compact trace has a Fourier transform that is not identically zero. Fix an \(\eta_*\) where it is nonzero, and send \(\xi\) to either infinity. These paths eventually lie in any cone about the corresponding nonzero horizontal covector; rapid decrease is impossible. Ordinary inclusion gives analytic membership, proving equality. Without the zero term in the smooth constant factor, the tensor upper bound would incorrectly be empty.

For \(p(s)\) and \(p(t)\), at a nonzero point of \(s=0\), the second factor is a nonvanishing analytic function, so the fiber is the positive \(s\)-normal ray. At a nonzero point of \(t=0\) it is the positive \(t\)-normal ray. Off both axes the product is analytic. At the crossing its fiber is
\[
 \{(\xi,\eta):\xi\geq0,\ \eta\geq0,\ (\xi,\eta)\ne(0,0)\}.
\]
The upper inclusion follows from the sum theorem, including the zero components. On every interior positive ray the cutoff transform tends to \(-4\pi^2\chi(0,0)=-4\pi^2\), by convolution with the quadrant Fourier transform and dominated convergence of the Schwartz cutoff transform. Thus these directions are ordinarily singular. Closedness includes the two boundary rays; ordinary inclusion proves the exact analytic fiber.

### Solution 5

The derivative of the diagonal sends a tangent vector \(h\) to \((h,h)\). Its transpose sends \((\xi,\eta)\) to \(\xi+\eta\). The nonzero killed covectors are therefore \((\xi,-\xi)\), \(\xi\ne0\).
The two positive-coordinate pole covectors in the plane cannot sum to zero unless both are zero, which is excluded from a normal obstruction. They are transverse to the diagonal. On one line the upper and lower poles have opposite covector signs, so their nonzero covectors do meet the diagonal normal set.

The product of their common regularizations is exactly \(1/(r^2+\varepsilon^2)\). Substitute \(r=\varepsilon z\); multiplying its pairing by \(\varepsilon\) gives the integral in (15). The test is bounded, and \(1/(1+z^2)\) is integrable with integral \(\pi\), by its antiderivative \(\arctan z\). Dominated convergence gives \(\pi\psi(0)>0\).
Consequently the unscaled pairings have magnitude asymptotic to \(\pi\psi(0)/\varepsilon\) and diverge. Distributional convergence would require a finite limit on this one test, so it is impossible for this regularization. The wavefront criterion explains its obstruction; the divergence supplies the separate impossibility proof.

### Solution 6

At every nonzero point of the ray the Euler bound makes each wavefront covector perpendicular to that point. A circle conormal is a nonzero multiple of the radius vector, whose pairing with the radius is nonzero. Therefore the analytic restriction theorem applies. The circle does not contain the singular endpoint of the ray.

The only possible intersections with \(t=0\) are \(\theta=0,\pi\). Near zero, \(s=a\cos\theta>0\), so \(H(s)=1\), and the coordinate \(r=a\sin\theta\) is a local diffeomorphism with derivative \(a\). A delta pulled back by such a one-variable coordinate pairs as the value of the angular test at zero divided by the absolute derivative \(a\). Near \(\pi\), the Heaviside factor is zero. Elsewhere the line delta is zero. Thus on periodic tests
\[
 (j^*u)(\psi(\theta)\,d\theta)=\frac{\psi(0)}a.
\]
At the intersection, \(Dj(0)=(0,a)^T\). The two nonzero normal signs \((0,\eta)\) are sent to \(a\eta\), so both angular signs remain. The point delta in the preceding pairing verifies the exact fiber.
For an arclength test \(\psi\,d\sigma=\psi a\,d\theta\), the pairing becomes \((a\psi(0))/a=\psi(0)\). This changes the test density, not the scalar pullback convention.

### Solution 7

For the forbidden trace, insert \(s=r^2\) into the Gaussian (17):
\[
 g_\varepsilon(r^2)
    =(4\pi\varepsilon)^{-1/2}e^{-r^4/(4\varepsilon)}.
\]
Substitute \(r=\varepsilon^{1/4}z\). The differential contributes \(\varepsilon^{1/4}\), yielding the factor \(\varepsilon^{-1/4}/\sqrt{4\pi}\) in (18). The remaining integral tends to
\(\psi(0)\int e^{-z^4/4}dz\), a positive finite number when \(\psi(0)>0\). Its domination is \(\|\psi\|_\infty e^{-z^4/4}\), integrable since it decreases faster than \(e^{-|z|}\) outside a sufficiently large interval. Thus the natural trace approximation diverges with the stated power.

For the fold projection, start from \((\pi_*w)(\psi)=\int\chi(t)\psi(t^2)dt\). Split into \(t>0\) and \(t<0\). On each half put \(s=t^2\). The absolute derivatives are \(dt=ds/(2\sqrt s)\) and \(|dt|=ds/(2\sqrt s)\), with the negative branch evaluated at \(-\sqrt s\). Their sum is precisely (20). This density is integrable at zero because \(\int_0^\delta s^{-1/2}ds=2\sqrt\delta\).

Near the vertex the source is the analytic pullback of \(\delta_0(r)\otimes1\) by \(\kappa(s,t)=(s-t^2,t)\). The exact analytic coordinate theorem and its smooth counterpart give
\[
 D\kappa(s,t)^T(\tau,0)=(\tau,-2t\tau).
\]
Both signs occur for every \(\tau\ne0\), giving (21).
The projected density near zero is real and equals \(H(s)/\sqrt s\). It is not smooth at zero: any smooth representative would agree on \(s>0\) with \(s^{-1/2}\), which is unbounded approaching zero. Ordinary wavefront is symmetric for a real distribution, since conjugating a localization reverses the Fourier frequency. In one dimension, absence of one sign would therefore give absence of both, which would imply local smoothness. Hence both ordinary signs occur. Ordinary inclusion gives both analytic signs. At nonzero sufficiently small \(s\), the density is either the analytic function \(s^{-1/2}\) or zero, so there are no other nearby analytic singular base points.

Projection is allowed because the source support is compact and hence proper; its rule may retain a critical-source normal with zero fiber component. Restriction instead requires every singular normal to survive the transpose derivative. For \(r\mapsto(r^2,r)\), the line-delta normal is annihilated at zero, so that condition fails. These are different geometric requirements.

### Solution 8

The normal topology is generated by the strong distribution seminorms \(q_B\), for bounded compact-test families, and all rapid seminorms \(p_{\chi,V,k}\) on cutoff/cone pairs disjoint from the fixed closed bound \(\Gamma\). The preceding bounded-test lemma makes weak convergence of a sequence imply strong distributional convergence. Thus the sequential convention is weak convergence plus convergence of every such rapid seminorm. This does not identify the full topology with the topology generated by weak individual pairings.

Suppose \(u_j\to u\) and \(v_j\to v\) in their fixed-wavefront spaces, with their closed bounds nonopposing. Each convergent sequence together with its limit is bounded: a continuous seminorm is bounded on a convergent sequence by its limit and finitely many early values. Hypocontinuity gives uniform continuity in the first argument over the bounded second-factor set. Use
\[
 u_jv_j-uv=(u_j-u)v_j+u(v_j-v).
\]
The first term tends to zero in every output seminorm by that uniform continuity; the second tends to zero by continuity with \(u\) fixed. The sum bound includes zero components and is closed off zero under nonopposition, as in complete-proof Theorem 8.2.

For the escaping points \(w_j\), every bounded compact-test family is supported in one fixed compact set, which misses \((0,j)\) for all sufficiently large \(j\). Its strong pairings are then exactly zero. For a rapid Fourier seminorm on any fixed compact cutoff, the cutoff also eventually vanishes near \((0,j)\), so the entire localized distribution and its transform are zero. Thus the sequence tends to zero in the fixed-wavefront normal topology for the closed cone over the discrete point supports.

Each singleton source support is proper, but their closed union has an unbounded fiber over the compact target set \(\{0\}\). It is not proper. Every projected point distribution is \(\delta_0\), with pairing one on a target test equal to one at zero, so the projected sequence cannot tend to zero. Complete-proof Theorem 8.3 requires one common proper source set, and this example fails exactly that requirement.

## References

[G] [*Detecting regularity without choosing coordinates*][G] (2026), Sections 10 and 18.1–18.5. The linked proof chapter retains its GNU FDL 1.2 component terms.

[A] [Analytic directions of holomorphic boundary values][A], controlled cutoffs, ordinary inclusion, and Examples 1 and 4.

[E] [Dilation equations and tangential analytic singularities][E], Theorem 4.1, Corollary 4.2 and the positive-ray example.

[Q] [Tensor products and parameter-dependent distributions][Q], Lemma 3.2.

[B] Christian Brouder, Nguyen Viet Dang and Frédéric Hélein, *Continuity of the fundamental operations on distributions having a specified wave front set (with a counterexample by Semyon Alesker)*, Studia Mathematica **232** (2016), 201–226. [Primary article and publisher's CC-BY grant](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/232/3/91541/continuity-of-the-fundamental-operations-on-distributions-having-a-specified-wave-front-set-with-a-counterexample-by-semyon-alesker). [Complete open proof article](https://www.impan.pl/shop/en/publication/transaction/download/product/91541), Section 3, Theorem 4.6, Proposition 5.1 and Theorems 6.1 and 6.3. Linked article retains its authorship and CC-BY terms.

Original exposition, examples and solutions are CC0. Linked proof chapters and references retain their actual authorship and component terms. Homogeneous Fourier-wavefront interchange is a separate further theorem.

[G]: https://github.com/KokunoYumeto/open-math-courses-public/blob/2c2a0ad6bc3a0ec35a65f66c8c4c3a315f22ffc4/docs/courses/elliptic-operators-and-boundary-problems/src/geometric-microlocal-calculus.md
[A]: ../../AN02-L186.html#complete-proof
[E]: ../../AN02-L187.html#complete-proof
[Q]: https://github.com/KokunoYumeto/open-math-courses-public/blob/2c2a0ad6bc3a0ec35a65f66c8c4c3a315f22ffc4/docs/courses/AN-01/src/tensor-products-and-parameters.md
