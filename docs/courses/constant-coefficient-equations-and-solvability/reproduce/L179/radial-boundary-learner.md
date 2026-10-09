# Radial boundary kernels and regularity of convolution

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI. Public domain (CC0 1.0).*

A sphere can carry a singular distribution whose convolution detects every nonsmooth input. The crucial feature is a boundary-value sign: it selects one Fourier phase. After a smooth cutoff makes the kernel compact, that phase survives in every logarithmic complex strip. We will see why this gives regularity, how translation and radius change the answer, and how a smooth perturbation can destroy radial symmetry without changing regularity.

Assume the definitions of distributions, Fourier transforms and compact convolution. The exact regularity and parametrix criterion is proved in Logarithmic zero retreat and reflected singularities, Theorems 3.4 and 6.1; its Corollary 7.1 explains compact representatives modulo smooth functions. The [complete proof](radial-boundary-formal.md) below supplies the boundary distribution, both base-dimensional Fourier calculations, all uniform estimates and the profile calculation.

Basic references are Richard Melrose's [Differential Analysis](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/), Gerd Grubb's [Fourier transformation of distributions](https://web.math.ku.dk/~grubb/dist5.pdf), and Lars Hörmander's *The Analysis of Linear Partial Differential Operators*, volumes I and II. We use
\[
 F(\zeta)=\langle\mu,e^{-ix\cdot\zeta}\rangle,\qquad
 \zeta=\xi+i\eta,\qquad \xi,\eta\in\mathbb R^n.
 \tag{E1.1}
\]
The dot product in the exponential is bilinear.

## 1. The sphere is the singularity, and the sign selects a phase

Consider the tempered boundary value
\[
 \lambda_n=(1-|x|^2-i0)^{-1}
     =\lim_{\varepsilon\downarrow0}(1-|x|^2-i\varepsilon)^{-1}.
 \tag{E1.2}
\]
The limit is distributional. Close to the sphere the variable \(q=1-|x|^2\) is a genuine smooth normal coordinate. The one-variable identity gives
\[
 (q-i0)^{-1}=\operatorname{pv}(1/q)+i\pi\delta_0(q).
 \tag{E1.3}
\]
Because \(|\nabla q|=2\) on the unit sphere, the result is
\[
 \lambda_n=\operatorname{pv}_{q}(1-|x|^2)^{-1}
                    +\frac{i\pi}{2}\sigma_{n-1}.
 \tag{E1.4}
\]
Here \(\sigma_{n-1}\) is surface measure on the unit sphere, and the principal value is taken in \(q\). In dimension one the surface measure is \(\delta_{-1}+\delta_1\). The sphere is the exact singular support: the imaginary part is nonzero surface measure near every one of its points, and off the sphere the kernel is an ordinary smooth function. [Lemma 1.1](radial-boundary-formal.md#1-a-boundary-value-supported-by-an-actual-normal-coordinate) proves the limit and this exact singular-set statement.

Choose a smooth compact cutoff \(\chi\), equal to one near the sphere, and put \(\mu=\chi\lambda_n\). Then \(\mu\) is compact, and \(\lambda_n-\mu\) is smooth. Consequently \(\mu*u\) exists for every global distribution \(u\). The original noncompact \(\lambda_n*u\) does not acquire such an existence assertion.

For a radial cutoff, let \(F_n\) be the entire transform of \(\mu\). The real transform of the global boundary value, off frequency zero, has the phase
\[
 G_n(r)\sim C_n r^{-\alpha_n}e^{-ir},\qquad
 \alpha_n=(n-1)/2,\qquad
 C_n=i\pi(2\pi)^{\alpha_n}e^{i\pi\alpha_n/2}.
 \tag{E1.5}
\]
The coefficient is nonzero. Replacing \(-i0\) by \(+i0\) conjugates the physical distribution and reverses this radial phase. We will keep track of this sign explicitly.

The two starting dimensions are derived, rather than inferred from a special-function name:
\[
 G_1(r)=i\pi e^{-ir},\qquad
 G_2(r)=-4\pi e^{-i\pi/4}e^{-ir}
             \int_0^\infty\frac{e^{-2ru^2}}{\sqrt{1-iu^2}}\,du,
 \quad \operatorname{Re}r>0.
 \tag{E1.6}
\]
Every higher dimension follows by
\[
 G_{n+2}(r)=-\frac{2\pi}{r}G_n'(r).
 \tag{E1.7}
\]
The first formula is the preceding lesson's exact one-dimensional calculation. The second is [Lemma 5.1](radial-boundary-formal.md#5-the-two-base-dimensions-including-the-boundary-value-sign): restrict the derived three-dimensional transform to a physical coordinate plane, then rotate an explicitly controlled contour to obtain the absolutely convergent Gaussian integral. The recurrence is [Lemma 2.1 and its global limit](radial-boundary-formal.md#4-removing-a-smooth-tail-does-not-change-the-real-high-frequency-phase).

## 2. The regularity conclusion

**Theorem.** For every dimension \(n\ge1\) and every compact cutoff equal to one near the unit sphere, the compact kernel \(\mu=\chi\lambda_n\) satisfies
\[
 u\in\mathcal D'(\mathbb R^n),\quad
 \mu*u\in C^\infty(\mathbb R^n)
       \quad\Longrightarrow\quad
 u\in C^\infty(\mathbb R^n).
 \tag{E2.1}
\]
There is a compact parametrix \(P\) with
\[
 \mu*P=\delta_0+h,\qquad h\in C_c^\infty,\qquad
 \operatorname{sing\,supp}P=\mathbb S^{n-1}.
 \tag{E2.2}
\]
The sphere on the right is the reflection of the kernel's singular sphere about the origin. Reflection preserves this centered sphere, but exchanges its individual points. [Theorem 8.1](radial-boundary-formal.md#8-full-regularity-in-all-dimensions) proves the complete statement.

The input in (E2.1) is an arbitrary global distribution. It has no compact-support or tempered-growth restriction. A proof about compact inputs alone would not prove this theorem.

Here is the mechanism. A radial compact transform satisfies
\[
 F_n(\zeta)=f_n(r),\qquad r=\sqrt{\zeta\cdot\zeta},
 \tag{E2.3}
\]
using the square root with positive real part near large real frequencies. If \(R=|\xi|>0\) and \(|\eta|\le R/2\), then
\[
 \frac{\sqrt3}{2}R\le\operatorname{Re}r\le R,\qquad
 |\operatorname{Im}r|\le|\eta|,\qquad
 \frac{\sqrt3}{2}R\le|r|\le\frac{\sqrt5}{2}R.
 \tag{E2.4}
\]
The scalar \(r\) is a square root of the **bilinear** square; it is not the Euclidean norm of the complex vector. [Lemma 7.2](radial-boundary-formal.md#7-from-a-scalar-half-plane-to-complex-vector-frequencies) proves both this identity and the bounds.

Removing the smooth physical tail gives rapid Fourier decrease on the real axis. A half-plane maximum argument carries that decrease into the complex domain with one fixed exponential type:
\[
 |f_n(r)-G_n(r)|\le K_N|r+1|^{-N}e^{B|\operatorname{Im}r|}.
 \tag{E2.5}
\]
Here \(N\) can be any nonnegative integer; the number \(B\) does not depend on it. [Lemmas 3.1, 4.1 and 7.1](radial-boundary-formal.md#3-rapid-real-decay-extends-to-a-complex-half-plane) supply the exact proof. No complex transform of the noncompact tail is assumed to exist.

In a strip \(|\eta|\le m\log R\), divide (E2.5) by the nonzero leading term in (E1.5). The relative cutoff error is bounded by
\[
 K'_N R^{-N+\alpha_n+(B+1)m}.
 \tag{E2.6}
\]
Choose \(N>\alpha_n+(B+1)m+1\). The relative error tends uniformly to zero; the differentiated Gaussian asymptotic supplies the remaining \(O(R^{-1})\) term. Thus
\[
 F_n(\zeta)=C_n r^{-\alpha_n}e^{-ir}(1+o(1))
 \quad\text{uniformly in each fixed logarithmic strip}.
 \tag{E2.7}
\]
It cannot vanish there once \(R\) is large. On real frequencies the same formula gives a polynomial lower bound, hence slow decrease. The exact reflected support function is \(H_{\mathbb S^{n-1}}(-\eta)=|\eta|\). After increasing each strip's threshold, **one** exponent, independent of its width, gives
\[
 |F_n(\zeta)^{-1}|\le|\zeta|^{\alpha_n+1}e^{|\eta|}.
 \tag{E2.8}
\]
These are the hypotheses of the available regularity criterion. A larger strip changes its threshold and the error estimate needed to prove it; it does not change the exponent in (E2.8).

The compact parametrix also explains (E2.1) directly. Associativity with compact factors gives
\[
 u=P*(\mu*u)-h*u.
 \tag{E2.9}
\]
If \(\mu*u\) is smooth, its convolution with compact \(P\) is smooth. Convolution of the compact smooth \(h\) with any distribution is smooth: on a compact range of the output variable, the translated test \(h(x-\cdot)\) stays supported in one compact set, and every derivative passes through the distributional pairing. Hence both terms on the right are smooth.

## 3. Four worked examples

**Example 1. The exact phase in dimension three.** The recurrence applied to \(G_1\) gives
\[
 G_3(r)=-2\pi^2r^{-1}e^{-ir}.
 \tag{E3.1}
\]
There is no asymptotic remainder in this global model. At a complex radial frequency \(r=a+ib\),
\[
 |G_3(r)|=2\pi^2|r|^{-1}e^b.
 \tag{E3.2}
\]
A radial compact representative adds the error (E2.5). The proof in Section 2 makes this error relatively small in each logarithmic strip, so the exact model's nonvanishing gives eventual nonvanishing of the compact transform.

For an escaping real center \(c=R\theta\), \(|\theta|=1\), and fixed complex \(z\),
\[
 \sqrt{(R\theta+z\log R)\cdot(R\theta+z\log R)}
       =R+\theta\cdot z\log R+O((\log R)^2/R).
 \tag{E3.3}
\]
Therefore its compact transform has logarithmic profile
\[
 \frac{\log|F_3(R\theta+z\log R)|}{\log R}
       \longrightarrow\theta\cdot\operatorname{Im}z-1.
 \tag{E3.4}
\]
The entire unit sphere occurs as the slopes of these profiles. The exact singular support was already found in (E1.4); the profile calculation now identifies those same points through their Fourier growth. [Proposition 9.1](radial-boundary-formal.md#9-the-entire-family-of-logarithmic-profiles) proves local uniform convergence and exhausts all escaping-real-center profiles.

**Example 2. A translated circle of radius \(3/2\).** In dimension two set \(a=(1,-1/2)\) and
\[
 \Lambda(x)=\bigl(9/4-|x-a|^2-i0\bigr)^{-1}.
 \tag{E3.5}
\]
Its imaginary part is \(\pi/3\) times surface measure on the circle \(a+(3/2)\mathbb S^1\). Transporting the radial cutoff under \(x=a+(3/2)y\) gives
\[
 F_{a,3/2}(\zeta)=e^{-ia\cdot\zeta}F_2((3/2)\zeta).
 \tag{E3.6}
\]
The dimensional factor here is \((3/2)^{n-2}=1\). Its leading coefficient and phase are
\[
 C_2\sqrt{2/3}\,r^{-1/2}
          e^{-i(a\cdot\zeta+(3/2)r)},\qquad
 C_2=i\pi\sqrt{2\pi}\,e^{i\pi/4}.
 \tag{E3.7}
\]
For the unit direction \(\theta=(3/5,4/5)\), the profile slope is
\[
 a+(3/2)\theta=(19/10,7/10).
 \tag{E3.8}
\]
Thus the corresponding profile is
\((19/10)\operatorname{Im}z_1+(7/10)\operatorname{Im}z_2-1/2\).
The compact parametrix has singular circle centered at \(-a=(-1,1/2)\), of the same radius, and contains the reflected point \((-19/10,-7/10)\). The support factor in the reciprocal estimate is exactly
\[
 e^{H_{a+(3/2)\mathbb S^1}(-\eta)}
       =e^{-\eta_1+\eta_2/2+(3/2)|\eta|}.
 \tag{E3.9}
\]
[Proposition 10.1 and Figure 1](radial-boundary-formal.md#10-radius-translation-and-the-opposite-boundary-value) give the scaling proof and exact geometric illustration. The singular sets in that picture are circles, not filled disks.

**Example 3. Reverse the boundary sign in dimension five.** Take
\[
 \Lambda^+(x)=(4-|x|^2+i0)^{-1}\quad\text{on }\mathbb R^5.
 \tag{E3.10}
\]
The unit-radius minus-boundary model is
\[
 G_5^-(r)=-4\pi^3e^{-ir}(ir^{-2}+r^{-3}).
 \tag{E3.11}
\]
Conjugate its real-frequency formula and scale the radius to two. The exact global model becomes
\[
 G_{5,2}^+(r)=e^{2ir}(8\pi^3ir^{-2}-4\pi^3r^{-3})
       =8\pi^3ir^{-2}e^{2ir}\left(1+\frac{i}{2r}\right).
 \tag{E3.12}
\]
The phase is now \(e^{2ir}\), and the profile in direction \(\theta\) is
\[
 -2\theta\cdot\operatorname{Im}z-2.
 \tag{E3.13}
\]
As \(\theta\) ranges over the unit sphere, the slopes still fill the radius-two singular sphere. The compact representatives remain hypoelliptic: conjugating an equation for the plus-boundary kernel produces an equation for the minus-boundary kernel with conjugate input. The reflected parametrix sphere is again the radius-two sphere. This is a full regularity statement, not just a comparison of real Fourier magnitudes.

At positive real \(r\), the relative error in the unscaled minus-boundary dimension-five model is exactly \(-i/r\). In dimension two the derived Gaussian integral gives \(|W_2(r)-1|\le1/(8r)\), where \(W_n=e^{ir}r^{\alpha_n}G_n/C_n\). [Figure 2](radial-boundary-formal.md#10-radius-translation-and-the-opposite-boundary-value) illustrates these bounds and the dimension-two profile limit. Its samples use the global model; the compact-transform conclusion is proved by (E2.5)–(E2.7).

**Example 4. Radial symmetry can be lost while regularity remains.** Start with a compact radial representative \(\mu\) in dimension two. Define
\[
 b(x)=
 \begin{cases}
  \exp\!\bigl(-1/(1-16|x-(3,0)|^2)\bigr),
                &|x-(3,0)|<1/4,\\
  0,&|x-(3,0)|\ge1/4.
 \end{cases}
 \tag{E3.14}
\]
It is smooth and compact: at the edge, each derivative is a finite sum of powers of \((1-16|x-(3,0)|^2)^{-1}\) times the displayed exponential, which tends to zero faster than each such power grows. Its support is disjoint from the unit sphere.

The kernel \(\widetilde\mu=\mu+b\) is no longer radial, but it is another compact representative of \(\lambda_2\) modulo smooth functions. Its singular support is unchanged. If \(P\) is the compact parametrix in (E2.2), then
\[
 \widetilde\mu*P=\delta_0+h+b*P.
 \tag{E3.15}
\]
The new error is compact and smooth. Apply the identity (E2.9) with that error to any global distribution input. It proves regularity for \(\widetilde\mu\) immediately. Radial symmetry was useful for deriving one representative's Fourier estimates; it is not a restriction on all equivalent representatives.

## 4. What the calculation does and does not say about support

The singular support of a compact representative is the sphere. Its ordinary support can be much larger: it includes whatever smooth part the cutoff retained. The compact parametrix has the reflected **singular** sphere; this does not specify its ordinary support or turn it into a surface measure.

The global boundary value has a smooth tail of size \(|x|^{-2}\). That tail need not be integrable in the ambient dimension, and arbitrary global distribution inputs can grow much faster. The regularity statement for this global kernel is defined through a compact representative modulo smooth functions. It makes no universal ordinary-convolution existence claim for the noncompact distribution.

Finally, the zeros excluded by the argument are the high-frequency zeros in each fixed logarithmic strip. Compact transforms can have zeros elsewhere. Slow decrease supplies the exact solvability condition used by the preceding criterion; zero-free logarithmic strips supply its additional regularity condition. They are separate facts, both proved here for the compact representatives.

## 5. Exercises and full solutions

There are **100 points in total**. Use the Fourier convention (E1.1). Each solution includes its grading allocation.

### Exercise 1. The coefficient on a sphere of radius two — 10 points

Find the imaginary part and exact singular support of \((4-|x|^2-i0)^{-1}\) on \(\mathbb R^3\). Explain the coefficient using the normal coordinate \(q=4-|x|^2\).

**Solution.** The scalar boundary identity contributes \(i\pi\delta(q)\). On the radius-two sphere, \(|\nabla q|=2|x|=4\). Polar coordinates, or the normal-coordinate change of variables, therefore give
\[
 \operatorname{Im}(4-|x|^2-i0)^{-1}
                  =\frac{\pi}{4}\sigma_{\{|x|=2\}}.
 \tag{E5.1}
\]
The real part is the principal value in \(q\). Off this sphere the denominator is nonzero and the distribution is smooth. At each sphere point its imaginary part is nonzero surface measure, which cannot equal a smooth density there: a test narrowed only in the normal direction retains a fixed surface pairing but has smooth-density pairing tending to zero. Thus the singular support is exactly the radius-two sphere.

**Grading:** 3 points for the scalar boundary sign, 4 for the gradient and coefficient, and 3 for both inclusions in the singular-support assertion.

### Exercise 2. One more odd dimension — 10 points

Derive the exact global model \(G_7\) from (E3.11), and verify its leading constant.

**Solution.** Differentiate the dimension-five expression before multiplying by the recurrence factor:
\[
 G_5'(r)=e^{-ir}
       (-4\pi^3r^{-2}+12\pi^3ir^{-3}+12\pi^3r^{-4}).
 \tag{E5.2}
\]
Consequently
\[
 G_7(r)=8\pi^4r^{-3}e^{-ir}
           \left(1-\frac{3i}{r}-\frac3{r^2}\right).
 \tag{E5.3}
\]
Here \(\alpha_7=3\) and \(C_7=8\pi^4\). Formula (E1.5) gives the same constant:
\(i\pi(2\pi)^3e^{3\pi i/2}=8\pi^4\).
These are exact global off-zero formulas; a compact cutoff adds the rapidly decreasing remainder described above.

**Grading:** 4 points for the differentiated expression, 4 for the recurrence and full result, and 2 for the independent leading-constant check.

### Exercise 3. Perpendicular imaginary frequencies — 10 points

In dimension two take \(\xi=(12,0)\), first with \(\eta=(0,5)\), then with \(\eta=(5,0)\) and \(\eta=(-5,0)\). Compute the positive-real-part radial square root in each case. Compare the phase magnitude \(e^{\operatorname{Im}r}\) with its worst lower envelope \(e^{-|\eta|}\).

**Solution.** For the perpendicular vectors the bilinear square is \(144-25=119\), so
\[
 r=\sqrt{119},\qquad \operatorname{Im}r=0,\qquad
 |e^{-ir}|=1.
 \tag{E5.4}
\]
The bounds (E2.4) hold: \(6\sqrt3\le\sqrt{119}\le12\), while the imaginary bound is strict. For the parallel and antiparallel cases the squares are \((12+5i)^2\) and \((12-5i)^2\), and the selected roots are \(12+5i\) and \(12-5i\). The phase magnitudes are therefore \(e^5\) and \(e^{-5}\).

All three imaginary vectors have norm five, so the lower envelope is \(e^{-5}\). It is attained by the antiparallel case; the perpendicular case is larger by a factor \(e^5\), and the parallel case by a factor \(e^{10}\). The bilinear radial coordinate retains this directional information.

**Grading:** 4 points for the three roots, 3 for their phase magnitudes, and 3 for the envelope comparison and directional explanation.

### Exercise 4. Spend enough powers to control a strip — 10 points

Suppose \(n=4\), the fixed exponential type in (E2.5) is \(B=3\), and the strip width is \(m=2\). What is the smallest integer \(N\) for which (E2.6) bounds the cutoff relative error by \(O(R^{-1})\)? Explain why \(N=6\) does not provide this conclusion.

**Solution.** Here \(\alpha_n=3/2\). The exponent in (E2.6) is
\[
 -N+\frac32+(3+1)2=-N+\frac{19}{2}.
 \tag{E5.5}
\]
To make it at most \(-1\), we need \(N\ge21/2\). The smallest integer is \(N=11\), which actually gives \(O(R^{-3/2})\). The Gaussian model's separate relative error is \(O(R^{-1})\), so the total relative error still tends to zero.

At \(N=6\) the displayed upper bound is \(O(R^{7/2})\). It does not prove smallness. This does not assert that the actual error grows: it says that these insufficiently many powers do not control the exponential factor in the strip. One may choose a larger \(N\), because the real cutoff error decreases faster than every inverse power and the half-plane bound retains the same \(B\).

**Grading:** 4 points for the exponent, 3 for \(N=11\), and 3 for distinguishing an inadequate bound from a claim about actual growth.

### Exercise 5. An explicit Gaussian remainder budget — 15 points

Prove \(|W_2(r)-1|\le1/(8r)\) for real \(r>0\), directly from (E1.6). Deduce a positive real lower bound for \(G_2\) when \(r\ge1/4\). Explain why this threshold is not automatically a threshold for every compact-cutoff transform.

**Solution.** Put \(a(u)=(1-iu^2)^{-1/2}\). Along \(t=u^2\ge0\),
\[
 \left|\frac{d}{dt}(1-it)^{-1/2}\right|
       =\frac12(1+t^2)^{-3/4}\le\frac12.
 \tag{E5.6}
\]
Thus \(|a(u)-1|\le u^2/2\). The Gaussian formula gives
\[
 \left|e^{ir}G_2(r)-C_2r^{-1/2}\right|
   \le2\pi\int_0^\infty u^2e^{-2ru^2}\,du
   =\frac{\pi^{3/2}}{2(2r)^{3/2}}.
 \tag{E5.7}
\]
The Gaussian moment is obtained by differentiating
\(\int_0^\infty e^{-2ru^2}du=\sqrt\pi/(2\sqrt{2r})\).
Divide (E5.7) by \(|C_2|r^{-1/2}=\sqrt2\,\pi^{3/2}r^{-1/2}\):
\[
 |W_2(r)-1|\le\frac1{8r}.
 \tag{E5.8}
\]
For \(r\ge1/4\) the relative error is at most \(1/2\), giving
\[
 |G_2(r)|\ge\frac{|C_2|}{2}r^{-1/2}>0.
 \tag{E5.9}
\]
A compact transform is \(f_2=G_2+q\), with a cutoff-dependent rapidly decreasing error \(q\). At a fixed frequency this error need not be small relative to \(G_2\); its controlling constants depend on the cutoff. Eventual nonvanishing follows only after estimating that additional error and increasing the threshold. The threshold \(1/4\) just proved belongs to the global model.

**Grading:** 4 points for the amplitude inequality, 5 for the Gaussian moment and exact constant, 3 for the lower bound, and 3 for the compact-cutoff distinction.

### Exercise 6. A shifted radius-two sphere — 15 points

In dimension three let \(a=(-2,1,0)\), \(R_0=2\), and use the minus boundary value. Find the leading compact-transform expression, the profile in direction \(\theta=(0,1,0)\), the singular sphere of a compact parametrix, and the reflected support factor.

**Solution.** Formula (10.3) of the complete proof gives the scaling factor \(2^{n-2}=2\). Substitute the exact dimension-three model at \(2r\):
\[
 2e^{-ia\cdot\zeta}G_3(2r)
       =-2\pi^2r^{-1}e^{-i(a\cdot\zeta+2r)}.
 \tag{E5.10}
\]
This is the leading compact-transform expression, with a relative error tending to zero in each logarithmic strip. The leading coefficient is independent of the radius in dimension three because \((n-3)/2=0\).

The direction gives \(a+2\theta=(-2,3,0)\), so its profile is
\[
 -2\operatorname{Im}z_1+3\operatorname{Im}z_2-1.
 \tag{E5.11}
\]
The kernel's singular sphere is centered at \((-2,1,0)\), of radius two. The parametrix's singular sphere is centered at \((2,-1,0)\), of radius two, and contains the reflected point \((2,-3,0)\). Finally,
\[
 H_{a+2\mathbb S^2}(-\eta)=2\eta_1-\eta_2+2|\eta|.
 \tag{E5.12}
\]
Its exponential is the factor in the reciprocal bound. These are singular supports and Fourier estimates; they do not describe the ordinary support of the parametrix.

**Grading:** 3 points for the coefficient and phase, 3 for the profile, 4 for the reflected sphere and point, 3 for the support function, and 2 for the support distinction.

### Exercise 7. Smooth perturbations and arbitrary inputs — 15 points

Let \(\mu*P=\delta_0+h\), with \(\mu,P\) compact and \(h\) compact smooth. Let \(b\) be any compact smooth function. Prove directly that smoothness of \((\mu+b)*u\), for arbitrary \(u\in\mathcal D'\), implies smoothness of \(u\). Explain what happens to the singular supports.

**Solution.** Compact convolution gives
\[
 (\mu+b)*P=\delta_0+h+b*P.
 \tag{E5.13}
\]
The term \(b*P\) is smooth by differentiating the compact distributional pairing, and compact because both factors are compact. Write \(k=h+b*P\). Associativity with compact factors gives
\[
 u=P*((\mu+b)*u)-k*u.
 \tag{E5.14}
\]
The first term is smooth under the stated hypothesis. For the second, on each compact range of \(x\) the tests \(k(x-\cdot)\) and all their derivatives have one compact support and bounded smooth seminorms. Pairing with the finite-order restriction of \(u\) therefore defines a smooth function, with derivatives obtained by differentiating \(k\). Thus \(k*u\) is smooth without any compactness or growth assumption on \(u\). Equation (E5.14) proves the result.

Adding the smooth \(b\) changes no singular point of the kernel: if either kernel were smooth near a point where the other was not, subtracting \(b\) would contradict that nonsmoothness. The same \(P\) is still a compact parametrix, since only its smooth error changed; its singular support is unchanged. In the spherical case that set is the exact reflected sphere.

**Grading:** 4 points for the new parametrix equation, 4 for the associative identity, 4 for the all-distribution smoothness argument, and 3 for the singular supports.

### Exercise 8. A smooth input with a divergent global tail — 15 points

Give a smooth global input for which the ordinary convolution integral with the noncompact \(\lambda_n\) has a divergent tail, in every dimension \(n\ge1\). Explain why this is consistent with the regularity theorem.

**Solution.** Choose \(u(y)=e^{|y|^2}\). It is smooth and defines a distribution on every compact test support, so \(u\in\mathcal D'(\mathbb R^n)\), even though it is not tempered. Fix an output point \(x\). For sufficiently large \(|y|\), \(|x-y|>2\), and the physical kernel has no boundary singularity there:
\[
 \lambda_n(x-y)u(y)=\frac{e^{|y|^2}}{1-|x-y|^2}.
 \tag{E5.15}
\]
Its real sign is negative. Once \(|y|\) exceeds a bound depending on \(x\), its absolute value is bounded below by
\(c_x e^{|y|^2}/|y|^2\). Polar integration of this lower bound diverges in every dimension; the exponential defeats any radial power. Thus the tail integral diverges, independently of any principal-value treatment near the sphere. There is no oscillatory tail cancellation here.

For a compact representative \(\mu\), the convolution \(\mu*u\) exists and is smooth, by the same compact pairing argument used in Exercise 7. The regularity theorem says that if this compact-kernel output is smooth then the input is smooth, which is true of the chosen input. For the global \(\lambda_n\), hypoellipticity modulo smooth functions is defined through such a compact representative. It asserts no universal ordinary-convolution existence statement for the global tail.

**Grading:** 4 points for a valid smooth distributional input, 5 for the sign and divergence argument in every dimension, and 6 for the exact compact-representative interpretation.

## References

- Richard B. Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course materials](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Gerd Grubb, *Fourier transformation of distributions*. [Author-hosted chapter](https://web.math.ku.dk/~grubb/dist5.pdf).
- Logarithmic zero retreat and reflected singularities, Theorems 3.4 and 6.1, Corollary 7.1 and the exact one-dimensional boundary-value example.
- [Radial boundary kernels and regularity of convolution: complete proof](radial-boundary-formal.md), Lemmas 1.1–7.2, Theorem 8.1 and Propositions 9.1–10.1.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators*, volumes I and II, Springer.
