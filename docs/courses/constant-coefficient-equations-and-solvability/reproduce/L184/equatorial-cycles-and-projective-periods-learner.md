# Equatorial cycles and the projective period test

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A deformed affine equator and a projective normal tube are different geometric objects. This chapter computes the map between them. The two signed equatorial centers give a factor of two; one positive normal disc gives a tube coefficient of one. The polynomial's degree is a third quantity and does not replace either factor.

Basic references are Atiyah, Bott and Gårding [A, B] for the classical contour method, and Hatcher [H] for finite-chain homology. The preceding [Rational top forms detect cycles in a hypersurface complement](../../AN02-L182.html) and [Finite covers and normal circles in projective complements](../../AN02-L183.html) prove the two general projective ingredients. [Tangent cones that permit an imaginary push](../../AN02-L118.html) supplies the compact zero-free deformation and whole-sphere extension. The complete proof below gives the remaining geometric and affine-fiber arguments.

The [full angular-contour and polynomial-continuation reading](angular-contours-and-polynomial-continuation.md) supplies the analytic argument and its exact constants. The complete all-integer parity-sensitive angular Fourier identity is proved in [Angular distributions and their full Fourier transforms](../../AN02-L185.html#4-the-angular-fourier-identity-on-the-whole-frequency-space), Theorem 4.1, with arbitrary angular distributions and the full frequency origin retained. The positive-polar analytic tube bound, analytic differential decrease and ordinary-wavefront inclusion are proved in Analytic directions of holomorphic boundary values. The homogeneous Euler bound and sphere-conormal exclusion are proved in Dilation equations and tangential analytic singularities, Theorem 4.1 and Corollary 4.2. General smooth and analytic wavefront operations are proved in Pulling back and combining analytic singularities, Sections 4–8. Gaussian packets and homogeneous Fourier directions, Theorem 8.1, proves exact ordinary and analytic Fourier-wavefront interchange away from both origins for arbitrary complex degree, finite Euler chains and arbitrary origin extensions. [Derivative sequences and microlocal regularity](../../AN02-L190.html#complete-proof), Sections 1–8, supplies the exact admissible derivative-sequence convention, bounded localization and base regularity, all analytic-map operation bounds, homogeneous Fourier interchange away from both origins, and the uniform class estimates needed for limits. Ordinary normal continuity and hypocontinuity retain their stated hypotheses; stronger class estimates require the stated uniform constants. The component conclusion here retains the remaining analytic hypotheses.

## 1. The two factors in the comparison

Let \(F\) be homogeneous of degree \(m\), let \(x\ne0\) be real, and put \(L(\zeta)=x\cdot\zeta\). A permitted even equatorial field gives two cycles
\[
 k^-(\xi)=\xi-i\varepsilon\Theta(\xi),\qquad
 k^+(\xi)=\xi+i\varepsilon\Theta(\xi),
 \quad \xi\in S^{n-1}\cap x^\perp .
 \tag{1}
\]
They avoid \(F=0\) and lie in \(L=0\). The sphere is oriented as the boundary of the negative hemisphere. Its antipodal degree is \((-1)^{n-1}\). Evenness gives
\[
 k^+(-\xi)=-k^-(\xi).
 \tag{2}
\]
Complex scalar rotation from \(1\) to \(-1\) avoids the homogeneous zero set, so the scalar minus sign is homotopic to identity in this affine complement. Hence
\[
 [k^+]=(-1)^{n-1}[k^-],\qquad
 [k^-]+(-1)^{n-1}[k^+]=2[k^-].
 \tag{3}
\]

For one center cycle \(k\), a small positive complex normal disc is
\[
 \Phi(z,\xi)=[k(\xi)+zx],\qquad |z|\leq\delta.
 \tag{4}
\]
Compactness lets us choose \(\delta>0\) so its image avoids the removed divisor. Its normal coordinate satisfies
\[
 L(k(\xi)+zx)=z|x|^2.
 \tag{5}
\]
Thus the disc meets the projective hyperplane only at its center, and its complex normal derivative has positive real determinant. The full argument identifies its relative class with the exact Thom map applied to the projected center. Its boundary is one positive normal circle, normal first.

If \(\pi\) is projectivization and \(\tau\) that precise tube map, the actual signed contour therefore satisfies
\[
 \pi_*[\alpha_-]=2\tau(\pi_*[k^-]).
 \tag{6}
\]
The factor two comes from the centers in (3). The single-center tube coefficient comes from the relative disc in (4). The degree \(m\) enters the separate cover \(F=1\), used in the preceding homology theorem.



![Signed equatorial centers, the positive normal-disc comparison and the scalar-fiber period.](figures/centers-normal-tube-and-scalar-fiber.png)

*Figure 1. The left panel lists the actual antipodal degree and second-center weight in dimensions three, four and five; their product gives the center class \(2[k^-]\). The middle panel represents the exact relative-disc map \(\Phi(z,\xi)=[k^-(\xi)+zx]\), whose positive normal boundary has coefficient one, and the resulting identity \(\pi_*[\alpha_-]=2\tau(\beta)\). This is a diagram of the specified maps and classes, not a spatial embedding in arbitrary dimension. The right panel shows the exact scalar-fiber model \(k(t)=(e^{it},0)\) in \(\mathbb C^*\times\mathbb C\), whose projection is the point \([1:0]\) while its logarithmic period is \(2\pi i\). This model is not a canonical even-field equator. The whole-sphere logarithm eliminates its winding in the canonical argument. Complete proof Sections 1, 2 and 4; Examples 1–2 below. Original figure, CC0; classical method context [A, B, H].*

## 2. Why the affine logarithm is also needed

Projectivizing forgets a scalar-circle direction. On the affine complement in \(L=0\), the global closed form
\[
 \vartheta=\frac{dF}{mF}
 \tag{7}
\]
has period \(2\pi i\) on a positive scalar fiber. Radial retraction and circle averaging give a complete decomposition
\[
 H^r_{\mathrm{dR}}(M;\mathbb C)
   =p^*H^r_{\mathrm{dR}}(Y;\mathbb C)
      \oplus[\vartheta]\wedge p^*H^{r-1}_{\mathrm{dR}}(Y;\mathbb C).
 \tag{8}
\]
The complete proof includes surjectivity, injectivity and the signs of the primitives. A zero projected class kills the first summand's periods, but not automatically the second's.

For a canonical equator in dimension \(n\geq3\), extend its permitted even field to the whole sphere using the preceding compact-cone theorem. The nonvanishing function
\[
 \Phi(\xi)=F(\xi-i\varepsilon V(\xi))
 \tag{9}
\]
has a logarithm on \(S^{n-1}\), because every loop there contracts. Restriction gives \(k^*\vartheta=m^{-1}dg\) on the equator. Its products with closed pulled-back base forms are exact, and all the remaining affine periods vanish. The smooth-period detection and faithful rational coefficient comparison then give rational affine null homology.

In dimension \(n=2\), the equator is a difference of two points. The affine hyperplane is a complex line, and its polynomial complement is \(\mathbb C^*\) whenever the zero-free equator exists. A path bounds that reduced zero-cycle. It must not be replaced by the ordinary positive generator of a projective point.

## 3. Four worked examples

### Example 1. Parity cancels out of the final multiplicity

In \(n=3\), the equator is \(S^1\), whose antipodal degree is \(+1\). Thus \([k^+]=[k^-]\), and the contour uses their sum, giving \(2[k^-]\).

In \(n=4\), the equator is \(S^2\), whose antipodal degree is \(-1\). Thus \([k^+]=-[k^-]\), while the contour's second weight is also \(-1\). Its center class is again
\([k^-]-[k^+]=2[k^-]\).

The two signs are separate before they cancel. Assuming an unsigned second sphere in every dimension would give an erroneous zero in one parity.

### Example 2. A zero projected class with a nonzero affine period

In \(\mathbb C^2\) let \(F(a,b)=a\), so \(M=\mathbb C^*\times\mathbb C\). Projectivization maps it onto \(\mathbb P^1\setminus\{a=0\}\cong\mathbb C\). The loop
\[
 k(t)=(e^{it},0),\qquad0\leq t\leq2\pi,
 \tag{10}
\]
projects to the constant projective point \([1:0]\), so its projected one-dimensional class is zero. But
\[
 \int_k\vartheta=\int_k\frac{da}{a}=2\pi i.
 \tag{11}
\]
Stokes therefore prevents it from bounding in the affine complement.

This loop is a model of the scalar fiber, not a canonical even-field equator. Its function \(F(k)=e^{it}\) has winding one and no global logarithm on the circle. The logarithm hypothesis in the canonical argument is what excludes this obstruction.

### Example 3. An actual canonical circle with an affine filling disc

In real dimension three take \(F(\tau,\eta,\sigma)=\tau\), \(N=e_\tau\) and \(x=e_\sigma\). On the equator use the constant even field \(\Theta=N\), which is perpendicular to \(x\) and permitted in every tangent component. Then
\[
 k(\theta)=(\cos\theta-i\varepsilon,\sin\theta,0).
 \tag{12}
\]
At characteristic frequencies the tangent component is \(v_\tau>0\); at noncharacteristic frequencies every vector is permitted. Thus this is an allowed field with a uniformly nonzero polynomial value.

With the ambient outward sphere orientation, the boundary of the negative \(\sigma\)-hemisphere traverses this equator with decreasing \(\theta\). Indeed its tangent orientation in coordinates \((\theta,\sigma)\) is \(d\theta\wedge d\sigma\); the outward boundary direction from \(\sigma<0\) is \(+\partial_\sigma\), so its remaining oriented tangent is \(-\partial_\theta\).

The map
\[
 D(u,v)=(u-i\varepsilon,v,0),\qquad u^2+v^2\leq1,
 \tag{13}
\]
has \(F(D)=u-i\varepsilon\ne0\). Give its real parameter disc the negative of the usual \(du\wedge dv\) orientation. Its boundary is exactly the inherited canonical circle (12). This is an actual finite smooth affine filling after a finite oriented disc triangulation.

The full-sphere extension is the same constant field \(N\). Its polynomial value \(\xi_\tau-i\varepsilon\) lies strictly in the lower half-plane, where a continuous holomorphic logarithm is available. Thus its logarithmic period is zero, consistent with the filling disc. This contrasts with the positive scalar-fiber loop in Example 2.



![The actual negatively oriented canonical circle bounds a displaced real disc, with its exact projective image.](figures/canonical-disc-and-projective-image.png)

*Figure 2. Here \(F=\tau\), \(N=e_\tau\), \(x=e_\sigma\) and \(\varepsilon=7/20\). The left panel shows the real parameters of the exact affine disc \(D(u,v)=(u-i\varepsilon,v,0)\), with constant \(\operatorname{Im}\tau=-\varepsilon\), \(\operatorname{Im}\eta=0\), \(\sigma=0\). Its orientation is the negative of \(du\wedge dv\), so its boundary arrows follow the inherited decreasing angle. The whole disc has \(|F(D)|\geq\varepsilon\). The right panel plots the same boundary after projectivization in \(y=\eta/\tau=\sin\theta/(\cos\theta-i\varepsilon)\). Both panels retain the actual maps; the right curve can intersect itself although the affine circle is embedded. The projected center has a filling given by the same disc map, rather than inferred from the plotted shape. Example 3 and complete proof Section 4. Original exact coordinate figure, CC0; classical deformation context [A, B].*

### Example 4. A normal scale changes size but not orientation

For a center cycle in \(x^\perp\), replacing \(x\) by \(cx\), \(c>0\), in (4) rescales the positive complex normal direction by \(c\). Its real determinant on the two normal coordinates is \(c^2>0\). The same oriented local disc generator is obtained after adjusting its small radius.

The full-bundle tubular map introduces another positive scalar, \(\rho>0\), on its normal derivative. Inverting it changes that derivative by \(\rho^{-1}\), whose real determinant is \(\rho^{-2}>0\). Neither operation changes the tube coefficient one.

Even multiplying a complex normal coordinate by a nonzero complex number \(a\) has real determinant \(|a|^2>0\). Complex conjugation is different: its real determinant is \(-1\), so it reverses the normal-disc and normal-circle orientations. An arbitrary real change of normal coordinates therefore needs an orientation check; a nonzero complex-linear change already has the positive sign.

## 4. Exercises, 100 points

1. **The parity and the factor two, 10 points.** Derive (3) in dimensions \(n=3,4,5\). Explain why the inherited orientation does not change the antipodal degree. Is complex scalar multiplication by \(-1\) itself an orientation reversal of the affine complex space?
2. **The actual cap naturality, 12 points.** For a degree-two relative cocycle \(u\) and a map \(B\) of pairs, verify \(B_\#R_{B^*u}c=R_uB_\#c\) on a singular simplex of dimension \(j+2\). Explain how Thom pullback uniqueness and disc-first product normalization turn this into the first identity in the formal proof's (9).
3. **The full-bundle radial scale, 12 points.** For \(h(v)=\rho v/\sqrt{1+\|v\|^2}\), \(\rho>0\), compute its derivative at zero. In a normal bundle chart let \(v(sz,\xi)=sA_\xi z+O(s^2|z|^2)\). Explain why \(v(sz,\xi)/s\) extends to the required linear map and why its boundary remains outside the zero section.
4. **Both halves of the circle-average decomposition, 14 points.** For an invariant form \(w\) on the circle bundle, compute \(b=-i\iota_Zw\) and \(h=w-i\alpha\wedge b\). Prove horizontality. For closed \(w\), prove that these descend to closed base forms. If \(p^*\eta+i\alpha\wedge p^*\gamma=du\), compute the signs of the base primitives after averaging \(u\).
5. **A logarithm versus a fiber period, 12 points.** Compute the periods in Examples 2 and 3. Why does a logarithm on the whole sphere imply zero equatorial winding? Why does nonvanishing only on a circle fail to provide that implication?
6. **The inherited equator and its disc, 12 points.** Verify the decreasing-\(\theta\) orientation in Example 3 from the outward sphere orientation. Show that the disc map (13), with its stated orientation, gives the required boundary and never meets \(F=0\). Explain why this example permits integral null homology without proving it for every canonical cycle.
7. **Every positive pole exponent is received, 14 points.** For \(F\) of degree \(m\), choose a positive pole exponent \(s\) and an inverse power \(k\). Determine the required derivative order and the value of the contour exponent \(q\). Explain why every homogeneous numerator is covered and why the monomials with negative requested degree cause no missing forms.
8. **Rational descent and the two-point case, 14 points.** Give the chain of implications from zero signed-contour periods to rational affine null homology, including the factor two, tube injection and fiber logarithm. Explain why neither division by two nor complex periods prove integral null homology. In \(n=2\), show directly why the inherited zero-cycle bounds.

## 5. Complete solutions

### Solution 1

The antipodal degree of the equator \(S^{n-2}\) is \((-1)^{n-1}\). In dimensions \(3,4,5\), this is respectively \(+1,-1,+1\). The exact map identity \(k^+\circ a=-k^-\) and the scalar rotation homotopy give \([k^+]=(-1)^{n-1}[k^-]\). In each case the contour's second weight has the same sign, so
\([k^-]+(-1)^{n-1}[k^+]=2[k^-]\).
**5 points.**

Changing both source and target sphere orientations reverses their generators simultaneously; the scalar degree of a self-map is unchanged. Thus the inherited boundary orientation does not alter the antipodal degree. **2 points.** On a complex vector space of complex dimension \(r\), scalar multiplication by \(-1\) has real determinant \((-1)^{2r}=+1\). It is also homotopic to identity through multiplication by \(e^{it}\). The real equatorial antipodal degree and that ambient complex scalar map have different domains; their orientation conclusions must not be interchanged. **3 points.**

### Solution 2

On a simplex \(\sigma:\Delta^{j+2}\to E\),
\[
 B_\#R_{B^*u}\sigma
   =(B^*u)(\sigma[j,j+1,j+2])\,B\sigma[0,\ldots,j]
   =u(B\sigma[j,j+1,j+2])\,B\sigma[0,\ldots,j]
   =R_uB_\#\sigma .
 \tag{14}
\]
This is literal equality with the same front face and coefficient. Linear extension gives it on chains, and relative vanishing of \(u\) makes it descend to the pairs. **5 points.**

For the fiberwise complex-linear normal map, pullback of the normal Thom class has value one on each positive fiber generator. The exact Thom uniqueness statement makes that pullback the positive trivial Thom class. Its cap map sends the positive fiber disc crossed with the base cycle to that base cycle. **4 points.** The source product convention puts the disc last; moving its dimension two past a base of dimension \(n-2\) gives \((-1)^{2(n-2)}=1\). The disc-first normalization is therefore the same. Composing (14) with bundle projections identifies the cap of the pushed-forward relative disc with \(p_*[k]\); the cap isomorphism's inverse gives the stated Thom class equality. **3 points.**

### Solution 3

Differentiating the radial map gives \(Dh_0(v)=\rho v\), since the derivative of its denominator contributes a term quadratic in \(v\). It is positive scalar multiplication on the normal plane; the inverse derivative is \(\rho^{-1}I\). Both preserve its orientation, with real determinants \(\rho^2\) and \(\rho^{-2}\). **4 points.**

Taylor's formula gives
\[
 s^{-1}v(sz,\xi)=A_\xi z+O(s|z|^2).
 \tag{15}
\]
The compact parameter domain permits uniform remainder bounds on finitely many bundle charts, so the maps extend continuously to \(s=0\), with the displayed linear limit. Their base points also converge to \(p(k(\xi))\). Bundle transition functions preserve this limit. **4 points.** On \(|z|=\delta\), for \(s>0\), the original point has nonzero normal coordinate because its projective \(L\)-coordinate is nonzero. Scaling a nonzero vector by \(s^{-1}\) keeps it nonzero. At \(s=0\), the nonzero complex-linear map \(A_\xi\) takes nonzero \(z\) to a nonzero normal vector. Thus the homotopy is a homotopy of pairs, not merely a homotopy of ambient maps. **4 points.**

### Solution 4

Contraction squares to zero, so \(\iota_Zb=0\). Since \(\alpha(Z)=1\),
\[
 \iota_Z(i\alpha\wedge b)
     =i\bigl(\alpha(Z)b-\alpha\wedge\iota_Zb\bigr)
     =ib=\iota_Zw .
 \tag{16}
\]
Hence \(\iota_Zh=0\). Invariance of \(w,\alpha,Z\) gives invariance of \(b,h\) as well. **4 points.**

If \(dw=0\) and \(\mathcal L_Zw=0\), Cartan's identity gives \(d\iota_Zw=0\), so \(db=0\). Since \(d\alpha=0\), \(dh=0\). In a local circle chart, horizontality removes the angular differential, and invariance removes angular dependence from the remaining coefficients. Thus both forms descend uniquely to closed base forms. **4 points.**

Averaging a primitive preserves its differential because pullback commutes with \(d\). Decompose that averaged primitive as
\(u=p^*u_0+i\alpha\wedge p^*u_1\).
Then
\[
 du=p^*du_0-i\alpha\wedge p^*du_1.
 \tag{17}
\]
Comparing its horizontal and vertical parts gives \(\eta=du_0\) and \(\gamma=-du_1\). This proves injectivity of the two summands; merely obtaining a decomposition of closed forms would have established only surjectivity. **6 points.**

### Solution 5

Example 2 has \(F(k)=e^{it}\), so \(k^*\vartheta=i\,dt\) and its period is \(2\pi i\). Its projected one-dimensional cycle is zero, yet its affine cycle is detected by this fiber form. **3 points.** Example 3 has \(F(k)=\cos\theta-i\varepsilon\), contained in the lower half-plane. A logarithm there gives \(k^*\vartheta=d\log F(k)\), whose period on the closed curve is zero in either orientation. Its explicit filling disc also proves that period vanishes by Stokes. **3 points.**

When \(n\geq3\), the nonvanishing whole-sphere function has zero logarithmic periods: every loop misses a point, contracts through stereographic coordinates, and Stokes applies to the closed form \(d\Phi/\Phi\). Integrating this form gives the global logarithm. Restricting it to the equator makes the logarithmic derivative exact there. **4 points.** A nonvanishing function on a circle can instead have nonzero winding; \(e^{it}\) is the explicit counterexample. Nonvanishing alone on that circle does not give a logarithm. **2 points.**

### Solution 6

At the equator the ordered vectors
\[
 (\cos\theta,\sin\theta,0),\quad
 (-\sin\theta,\cos\theta,0),\quad (0,0,1)
 \tag{18}
\]
have determinant \(+1\). The first is the outward sphere normal, so the sphere's tangent orientation is \((\partial_\theta,\partial_\sigma)\). The outward boundary direction from the negative hemisphere is \(\partial_\sigma\); the ordered pair \((\partial_\sigma,-\partial_\theta)\) has that same tangent orientation. Hence the boundary traverses decreasing \(\theta\). **5 points.**

The negatively oriented parameter disc has that negative-circle boundary. Under (13) it maps to precisely the canonical circle, and its polynomial value \(u-i\varepsilon\) has nonzero imaginary part at every point. Thus its entire finite smooth triangulated image stays in the affine complement and bounds the inherited cycle over the integers. **4 points.** This particular filling is an integral chain. It proves integral null homology for this example alone; other canonical cycles may have integral torsion, as the preceding wave-sphere example demonstrates. A rational theorem cannot supply such an integral filling in every case. **3 points.**

### Solution 7

For \(F^k\), the homogeneous inverse degree is \(mk-n\). To receive a denominator exponent \(s\geq1\), choose
\[
 |\alpha|=mk+s-n,\qquad
 q=mk-n-|\alpha|=-s .
 \tag{19}
\]
The derivative order exceeds the polynomial degree by \(s\), so the all-powers polynomial conclusion makes that derivative zero. The negative-exponent contour formula has a nonzero scalar and \((iL)^{-s}=i^{-s}L^{-s}\), hence gives zero period of the desired rational monomial form. **6 points.**

Every homogeneous polynomial of nonnegative degree \(mk+s-n\) is a finite linear combination of monomials \(\zeta^\alpha\) of that degree. Linearity therefore covers every numerator, not just selected derivative directions. **4 points.** If the requested degree is negative, there is no nonzero homogeneous polynomial numerator, so there is no missed form. The projective descent rule is exactly \(\deg P=mk+s-d-1\) with \(d=n-1\), giving the same number \(mk+s-n\). All positive \(k,s\) are covered, and the preceding theorem already permits redundant or removable pole factors. **4 points.**

### Solution 8

The exact comparison is \(\pi_*[\alpha_-]=2\tau(\beta)\), \(\beta=p_*[k^-]\). Vanished periods of the signed contour imply vanished rational-top-form periods of \(\tau\beta\), because two is invertible over \(\mathbb Q\). The preceding rational-form theorem and tube injection give \(\beta=0\) in rational homology. **4 points.**

The affine decomposition then leaves only the scalar-fiber summand. The whole-sphere logarithm makes \(k^*\vartheta\) exact, and its wedge products with closed pulled-back base forms are exact. Thus every closed smooth topological-degree form has zero period on the affine cycle. Smooth-period detection gives complex null homology, and faithful rational coefficient extension gives rational null homology with a finite bounding chain. **5 points.**

An integral class can have order two; dividing a relation for twice that class by two does not produce an integral chain. Complex periods likewise vanish on integral torsion. Neither step proves integral null homology in general. **2 points.** In \(n=2\), the restricted homogeneous polynomial is a nonzero monomial on the one-dimensional complex hyperplane, so its complement is \(\mathbb C^*\). The inherited two points have opposite coefficients. A path between them has their difference as boundary, with its sign chosen for the inherited order. This is the direct reduced-zero argument; it uses no negative-degree fiber group. **3 points.**

## 6. The component conclusion

If the canonical equator bounds over the rationals at one point, the complete analytic reading makes every principal-power inverse a homogeneous polynomial throughout the connected component. Derivatives above its degree give zero periods against every positive-pole homogeneous rational top form. The comparison (6) and the projective receiver then give zero projected center class at every component point. The logarithm and the affine splitting (8) give rational affine null homology there. Thus the condition is constant on the component, at the exact analytic prerequisites stated above. The all-powers polynomial conclusion is used before the topological component conclusion, so the argument does not assume its own result.

The same analytic reading proves the entire exponential bound for hyperbolic lower-order completions and their positive powers. Rational null homology is the coefficient convention of this chapter. Integral torsion and the direct two-point calculation retain their separate conclusions.

## References

[A] Michael Atiyah, Raoul Bott and Lars Gårding, *Lacunas for hyperbolic differential operators with constant coefficients, I*, Acta Mathematica **124** (1970), 109–189. [Primary article](https://www.its.caltech.edu/~matilde/HypPDEAtiyahBottGarding.pdf).

[B] Michael Atiyah, Raoul Bott and Lars Gårding, *Lacunas for hyperbolic differential operators with constant coefficients, II*, Acta Mathematica **131** (1973), 145–206. [Primary article](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6156-11511_2006_Article_BF02392039.pdf).

[H] Allen Hatcher, *Algebraic Topology*, Cambridge University Press (2002), §§3.3 and 3.G. [Author's freely readable text](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf). The exact relative-cap and tubular arguments used here are the complete linked internal proofs.

Original exposition, examples, solutions and figures are CC0-1.0. Linked historical works retain their own rights and are not reproduced. The rational theorem detects no integral torsion.
