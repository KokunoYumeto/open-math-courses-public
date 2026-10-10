# Complex oblique derivatives for the wave equation

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

An oblique boundary derivative can change the directions in which wave data propagate. Complex coefficients require more than the usual real sign test: their real and imaginary parts obey an exact Lorentz inequality. We prove the full coefficient classification, including null and purely imaginary endpoints, and compute the real propagation cone.

Read [Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md), [Extending a boundary time strip to its propagation cone](extending-a-boundary-time-strip-to-its-propagation-cone.md), [Boundary fundamental kernels and their propagation support](boundary-fundamental-kernels-and-their-propagation-support.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies the Fourier convention and Gaussian formula; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies scalar calculus and cutoffs. [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html) supplies finite scalar and polynomial algebra. 

The coefficient classification and explicit principal-cone calculations use the linked finite algebra, calculus and root-count proofs. Interpreting the cones as the supports of the general boundary kernels uses the available cone theorem in [Real roots and their convex component](../AN02-L192.html#4-pass-to-multiple-roots-and-obtain-convexity), Theorem 4.1, and retains the planned analytic zero-order prerequisite of [Boundary fundamental kernels and their propagation support](boundary-fundamental-kernels-and-their-propagation-support.md). The explicit two-spatial-dimensional point-source support theorem is proved separately in [A reflected wave and its faster boundary pulse](a-reflected-wave-and-its-faster-boundary-pulse.md).

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's treatment of constant-coefficient equations. The linked lessons supply the prerequisite proofs used below.

## The system and the two coefficient families

Write \(x=(a,z,t)\), \(z\in\mathbb R^d\), d=n-2≥2. Use frequency variables \((w,y,s)\), and put
\[
\begin{gathered}
P(w,y,s)=w^2+|y|^2-s^2,\\
\qquad
 B(D)=D_a+\beta\cdot D_z+bD_t,\\
\qquad
                  \beta\in\mathbb C^d,\\
\quad b\in\mathbb C .
\end{gathered}
\tag{1}
\]
Here \(|y|^2=\sum y_j^2\) as a polynomial when y is complex, and D=-i∂. The normal derivative coefficient is exactly one. The time principal value is -1; the time roots for real spatial frequencies are real. There is one upper normal root on every lower-time line, so one boundary condition is the balanced count.

**Theorem (full coefficient classification).** This mixed system is hyperbolic in the zero-free-strip definition exactly when at least one of the following holds:
\[
 \begin{array}{ll}
 \mathrm{A}:& \beta,b\ \hbox{are real and }b<1;\\[2mm]
 \mathrm{B}:& \begin{gathered}F\ \hbox{is future causal},\\
\quad
       1+[E,E]\ge0,\\
\quad
       [E,F]^2\le[F,F]\{1+[E,E]\}.\end{gathered}
 \end{array}
 \tag{2}
\]
In B the vectors and the Lorentz form are
\[
\begin{gathered}
\beta=p+iq,\\
\quad b=\alpha+i\gamma,\\
\quad
 F=(p,-\alpha),\\
\quad E=(q,-\gamma),\\
\qquad
 [v,v']=v_t v'_t-v_z\cdot v'_z,\\
\qquad
 F_t\ge|F_z|.
\end{gathered}
\tag{3}
\]
“Future causal” includes the closed null cone and the zero vector. Families A and B may overlap. The separate condition \(1+[E,E]\ge0\) is essential when F is null or zero.

## Reducing the strip test to a quadratic

For real y and \(\operatorname{Im}s<0\), choose the square root R of \(s^2-|y|^2\) whose imaginary part is negative. It is nonzero: if its square were a nonnegative real number, the imaginary part of s² would force \(\operatorname{Re}s=0\), but then \(s^2-|y|^2<0\). This also gives the unique negative-imaginary root; continuity or the local simple-root expansion makes the choice analytic. The upper normal root is \(\lambda=-R\). The residue determinant is
\[
\begin{gathered}
L(y,s)=\beta\cdot y+bs-R,\\
\qquad
                         L_0(0,1)=b-1 .
\end{gathered}
\tag{4}
\]
At y=0, R=s. The principal value is therefore nonzero exactly when b≠1. Homogeneity implies that any zero with negative imaginary time can be scaled to arbitrarily negative time; conversely, if there is no such zero, every strictly lower line is zero-free. Thus the strip condition is exactly absence of zeros in that whole lower-time region.

For y≠0 put \(\rho=|y|\), \(\theta=y/\rho\), \(\zeta=s/\rho\). On the slit plane \(\mathbb C\setminus[-1,1]\), use \(R_1(\zeta)=\sqrt{\zeta^2-1}\) with \(R_1/\zeta\to1\) at infinity. Equivalently, for the lower half-plane its imaginary part is negative. Its Joukowsky coordinate is
\[
\begin{gathered}
q_0=\zeta-R_1(\zeta),\\
\qquad
 0<|q_0|<1,\\
\quad\operatorname{Im}q_0>0,\\
\qquad
 \zeta=\tfrac12(q_0+q_0^{-1}),\\
\quad
 R_1=\tfrac12(q_0^{-1}-q_0).
\end{gathered}
\tag{5}
\]
These identities follow by multiplication of \(\zeta\pm R_1\). For a nonreal ζ, neither root q of \(q+q^{-1}=2\zeta\) has modulus one, since a unit q gives real ζ. Their product is one, so exactly one lies inside the unit disk. The displayed inverse has imaginary part \(\operatorname{Im}q(1-|q|^{-2})/2\); hence that inside root lies in the upper half-disk when ζ is in the lower half-plane. The root selected at large negative imaginary ζ is the same root throughout by continuity. This proves every branch and domain assertion in 5 without a conformal-mapping theorem.

Define
\[
\begin{gathered}
T_b(q_0)\\
=\tfrac12\left\{\begin{gathered}(b+1)q_0\\
+(b-1)q_0^{-1}\end{gathered}\right\},
 \\
\qquad
 L/\rho=T_b(q_0)+\beta\cdot\theta,\\
\qquad
 W=\{\beta\cdot\theta:|\theta|=1,\ \theta\in\mathbb R^d\}.
\end{gathered}
\tag{6}
\]
The coefficient set W is centrally symmetric. Its exact geometry is
\[
\begin{gathered}
W\\
=  \begin{cases}
 \{0\},&\operatorname{rank}(p,q)=0,\\
 \begin{gathered}\hbox{a closed centered }\\
\hbox{line segment}\end{gathered},&\operatorname{rank}(p,q)=1,\\
 \begin{gathered}\hbox{the boundary of a }\\
\hbox{nondegenerate ellipse}\end{gathered},&\begin{gathered}d=2,\ \\
\operatorname{rank}(p,q)=2\end{gathered},\\
 \begin{gathered}\hbox{the filled }\\
\hbox{nondegenerate ellipse}\end{gathered},&\begin{gathered}d>2,\ \\
\operatorname{rank}(p,q)=2 .\end{gathered}
 \end{cases}
\end{gathered}
\tag{7}
\]
To verify this, decompose a preimage orthogonally into the row space of the real map \(\theta\mapsto(p\cdot\theta,q\cdot\theta)\) and its kernel. The row-space preimage of a point is unique and of smallest norm. If the kernel is nonzero, any smallest norm at most one can be raised to one by adding a kernel vector of the required length. If the kernel is zero, only norm exactly one is allowed. In the rank-two case the squared smallest norm is a positive definite quadratic form on the image, giving precisely the ellipse and its boundary. The rank-one case gives the full interval because d≥2 leaves a nonzero kernel. This is also where the dimension assumption first enters.

Oddness of T and symmetry of W make avoidance in the upper half-disk equivalent to avoidance in both nonreal halves of the disk. Therefore the complete coefficient test is
\[
\begin{gathered}
b\ne1,\\
\qquad
 W\cap\\
T_b(\{q:0<|q|<1,\ \operatorname{Im}q\ne0\})=\varnothing .
\end{gathered}
\tag{8}
\]
For a proposed value \(\omega\), its preimages are the roots of
\[
\begin{gathered}
(b+1)q^2-2\omega q+(b-1)=0,\\
\qquad
           q_1q_2=\frac{b-1}{b+1}\\
\quad(b\ne-1).
\end{gathered}
\tag{9}
\]
No root is zero when b≠1. For b=-1 the equation is linear and \(T_{-1}(q)=-1/q\).

## Unit-circle images and exceptional real preimages

On the unit circle,
\[
             T_b(e^{i\vartheta})
                    =b\cos\vartheta+i\sin\vartheta .
 \tag{10}
\]
When α=\(\operatorname{Re}b\ne0\), this is a simple nondegenerate ellipse. Let \(\mathcal E_b\) be its filled interior. In coordinates \(\omega=u+iv\), membership is
\[
\begin{gathered}
\omega\in\mathcal E_b
       \\
\quad\Longleftrightarrow\\
\quad
       (u/\alpha)^2+(v-\gamma u/\alpha)^2\le1 .
\end{gathered}
\tag{11}
\]
The ellipse's interior and exterior are connected: the invertible real linear map \((X,Y)\mapsto(\alpha X,\gamma X+Y)\) carries the disk and its complement to them.

If α<0 then \(|(b-1)/(b+1)|>1\), so at most one quadratic root can be inside the unit circle. At \(\omega=0\) neither is inside, since their squares are \((1-b)/(1+b)\), of modulus greater than one. The argument-principle count is locally constant off the boundary ellipse. There are thus no inside roots throughout its interior. At large \(\omega\), \(2|\omega|>|b+1|+|b-1|\) makes the linear term dominate the other two on the unit circle. Actual Rouché counting gives exactly one inside root. Hence throughout the connected exterior there is exactly one inside root. At a boundary value one root has modulus one and the other has modulus greater than one, so neither is strictly inside. The linear b=-1 case gives the same result directly:
\[
\begin{gathered}
\alpha<0:\\
\quad
 \begin{cases}
 \text{no inside root},&\omega\in\mathcal E_b,\\
 \text{one inside root},&\omega\notin\mathcal E_b .
 \end{cases}
\end{gathered}
\tag{12}
\]
The root-count step is the actual written argument principle on the unit disk; the compact unit contour has no zero along any parameter path off its image. Repeated roots outside the disk do not affect that count.

An inside root is excluded from 8 only when it is real. For \(q=r\), real and \(0<|r|<1\), put \(X=(r+r^{-1})/2\), \(Y=(r-r^{-1})/2\). Then \(\omega=bX+Y\) and \(X^2-Y^2=1\). If γ≠0 its image therefore lies on the hyperbola
\[
                  (v/\gamma)^2-(u-\alpha v/\gamma)^2=1 .
 \tag{13}
\]
If γ=0 it lies on the real axis. These are the only exceptional inside-root images. The hyperbola does not pass through zero, and its quadratic form has one positive and one negative direction.

We use the following elementary confinement observation several times. A centered nondegenerate ellipse boundary cannot have a nonempty open arc on that hyperbola. Parametrize the ellipse by \(A(\cos\vartheta,\sin\vartheta)\), with A invertible. If the quadratic identity holds on an open arc, its finite trigonometric polynomial is identically constant: after multiplication by \(e^{2i\vartheta}\) it is a polynomial of degree at most four with infinitely many roots. It then holds on the entire circle and implies
\[
                         A^{T}HA=I_2 ,
 \tag{14}
\]
where H is the hyperbola's indefinite quadratic matrix. This is impossible: choose a vector in a negative direction for H and pull it back by \(A^{-1}\). A nontrivial straight segment also cannot lie on the hyperbola; along a line through zero the expression is \(r^2H(v)\), which cannot equal one on an interval. A filled ellipse cannot have an open part on this hyperbola because a nonzero quadratic polynomial cannot vanish on an open ball; restricting to coordinate lines proves that elementary fact. The same assertions for a line replacing the hyperbola are immediate from these parametrizations. Thus a W from 7 cannot protrude beyond a closed ellipse or segment while having every protruding point confined to these exceptional curves, except when the exceptional curve and W are the same real line segment.

## All time-coefficient cases

Suppose first α>0. The root-product modulus is less than one, so every value ω has at least one inside root. If b is nonreal, a missing value in 8 must lie on 13. Rank-zero and rank-one W contain zero, but zero is attained by nonreal inside roots: \(q^2=(1-b)/(1+b)\) is nonreal and has modulus less than one. A filled rank-two ellipse also contains zero. A rank-two ellipse boundary cannot lie on 13 by 14. No such nonreal b is admissible.

If b is real and \(0<b<1\), the product is negative. For real ω the quadratic discriminant is positive and all roots are real, so no admissible nonreal inside preimage exists. For nonreal ω, an inside root exists and cannot be real because T takes real roots to real values. Its nonreal image is therefore exactly the complement of the real axis. Avoidance is precisely \(W\subset\mathbb R\), equivalently β real. If b>1, zero is attained by the inside nonreal roots \(q^2=(1-b)/(1+b)<0\), so the W cases containing zero fail; a rank-two ellipse boundary cannot be confined to the real exceptional images. The value b=1 was already excluded. Consequently
\[
\begin{gathered}
\alpha>0:\\
\quad
      \text{admissible exactly when }\\
0<b<1,\\
\quad\beta\in\mathbb R^d .
\end{gathered}
\tag{15}
\]

Now let α=0. If γ≠0, the unit-circle image in 10 is the segment
\[
                      \mathcal E_{i\gamma}
                 =i[-\sqrt{1+\gamma^2},\sqrt{1+\gamma^2}].
 \tag{16}
\]
Every value on that segment has a unit root and, because the root-product modulus is one, its second root is also unit. There are no inside roots there. Off the segment the complement is connected; neither root is unit, and their product modulus is one, so exactly one is inside. The exceptional real inside root images lie on 13. The confinement observation forces \(W\subset\mathcal E_{i\gamma}\), and this inclusion is sufficient.

When b=0, the unit image is \(i[-1,1]\), and the exceptional real inside images comprise all nonzero real values. Thus the missing set is \(\mathbb R\cup i[-1,1]\). A rank-two W cannot be contained in these two lines. A rank-one centered segment must lie on one of the axes. Combining these cases yields
\[
 \alpha=0:\quad
 \begin{cases}
 b=0,\quad\beta\in\mathbb R^d; \quad\text{or}\\
 p=0,\quad |q|^2\le1+\gamma^2 .
 \end{cases}
 \tag{17}
\]
In the second line γ may also be zero. This is exactly A's b=0 endpoint together with B's F=0 endpoint.

Finally let α<0. 12 says that any value outside \(\mathcal E_b\) has one inside root. If γ≠0, every missing exterior value lies on 13; the confinement observation forces \(W\subset\mathcal E_b\). If γ=0, an exterior missing value must be real. Either W is entirely real, in which case every size of its centered segment is admissible, or the same confinement argument forces \(W\subset\mathcal E_b\). Sufficiency of ellipse inclusion follows directly from 12. For real β and real b<0, any nonreal inside root at a real value would have its conjugate also inside, contradicting the at-most-one count; the linear b=-1 case has a real root directly. Every inside root is therefore real and excluded from the test. This proves the second sufficiency. Thus
\[
\begin{gathered}
\alpha<0:\\
\quad
        \text{admissible iff }W\subset\mathcal E_b
          \\
\ \text{or }(\beta,b\ \text{both real}).
\end{gathered}
\tag{18}
\]
This includes b=-1. No coefficient case remains.

## Converting ellipse containment to the Lorentz test

For α<0, substitute \(\omega=p\cdot\theta+i q\cdot\theta\) into 11. Containment is exactly
\[
\begin{gathered}
|A\theta|^2\le1\ (|\theta|=1),\\
\qquad
 A=\begin{pmatrix}p^T/\alpha\\(q-\gamma p/\alpha)^T\end{pmatrix}.
\end{gathered}
\tag{19}
\]
This is equivalent to \(I_2-AA^T\) being positive semidefinite. Indeed the Euclidean identity \(|v|=\sup_{|e|=1}e\cdot v\) gives equality of the operator norms of A and \(A^T\), by two finite suprema and Cauchy's inequality. A matrix has norm at most one precisely when the corresponding quadratic inequality holds. No spectral-decomposition theorem is required.

Put \(\Delta=[F,F]\), \(R_E=1+[E,E]\), and \(K_E=[E,F]\). Direct finite expansion gives
\[
\begin{gathered}
\Delta=\alpha^2-|p|^2,\\
\quad
 R_E=1+\gamma^2-|q|^2,\\
\quad
 K_E=\alpha\gamma-p\cdot q,\\
\qquad
 (I_2-AA^T)_{11}=\Delta/\alpha^2,\\
\quad
 \det(I_2-AA^T)\\
=(\Delta R_E-K_E^2)/\alpha^2 .
\end{gathered}
\tag{20}
\]
If \(\Delta>0\), nonnegative determinant and the positive first diagonal entry give positive semidefiniteness by completing the square. They also imply \(R_E\ge0\). If \(\Delta=0\), the determinant condition forces \(K_E=0\). In that case the off-diagonal entry is zero, and the remaining diagonal entry is \(R_E\). It must be tested separately. Conversely, if the matrix is positive semidefinite and \(\Delta=0\), its off-diagonal entry must vanish (test vectors \((1,r)\) for arbitrarily small signed r), so exactly these same conditions follow. Because α<0, \(\Delta\ge0\) is equivalent to F being future causal. Hence
\[
\begin{gathered}
W\subset\mathcal E_b
 \\
\quad\Longleftrightarrow\\
\quad
 F\ \text{future causal},\\
\quad R_E\ge0,\\
\quad
                                     K_E^2\le\Delta R_E .
\end{gathered}
\tag{21}
\]
For α=0, future causality forces p=0, and this same criterion becomes precisely the second line of 17. For α>0, F cannot be future causal. Combining 15, 17, 18 and 21 proves the complete theorem 2.

## Principal cones and directional propagation

The interior wave cone and its projection are, explicitly,
\[
\begin{gathered}
\Gamma=\{(w,y,s):s>\sqrt{w^2+|y|^2}\},\\
\quad
 \Omega=\{(y,s):s>|y|\},\\
\qquad
 C\\
=\{(a,z,t):t\ge\sqrt{a^2+|z|^2}\}.
\end{gathered}
\tag{22}
\]
The cone C is their nonnegative-pairing polar: Cauchy's inequality proves nonnegative pairings, while a spatial covector opposite a proposed spatial vector proves the converse. Projection of Γ allows w=0 and is exactly Ω.

For real family A the principal symbol on Ω is
\[
\begin{gathered}
L_0(y,s)=\beta\cdot y+bs-\sqrt{s^2-|y|^2},\\
\qquad
 \Sigma\\
=\left\{\begin{gathered}(y,s):s>\\
\sqrt{|y|^2+
                       \max(0,\beta\cdot y+bs)^2}\end{gathered}\right\}.
\end{gathered}
\tag{23}
\]
The local positive square root is the real continuation of the root at the time direction, as the elementary simple-root expansion verifies. Its sign cannot change on Ω. At time, \(L_0=b-1<0\). The displayed inequality is exactly \(L_0<0\): a nonpositive linear term needs no square test; a positive one may be squared without changing the inequality. Normalize by s>0 to obtain the section
\[
\begin{gathered}
K\\
=\left\{\begin{gathered}v\in\mathbb R^d:\\
|v|^2\\
+\max(0,\beta\cdot v+b)^2<1\end{gathered}\right\},
       \\
\qquad (y,s)\in\Sigma\ \Longleftrightarrow\ y/s\in K .
\end{gathered}
\tag{24}
\]
The squared positive part of an affine function is convex: its derivative as a scalar function is nondecreasing, or its defining chord inequality follows by its two quadratic pieces. Adding the strictly convex squared norm makes this strict sublevel convex. It contains zero because b<1, using the positive part when b<0. Thus it is connected and is exactly the nonzero principal component containing time, not just a subset of that component. Its closure is the nonstrict sublevel: continuity gives one inclusion, and a point on level one is approached by its segments toward zero, where convexity and the strict value at zero give values below one.

For unit spatial q define \(h_K(-q)=\sup_{v\in\overline K}(-q)\cdot v\). Since K contains a neighborhood of zero and is contained in the unit ball, this number is positive and at most one. The embedded boundary polar and directional speed bound are
\[
\begin{gathered}
C_\partial\\
=\{(0,z,t):t\ge h_K(-z)\},\\
\qquad
 v_{\rm bdry}(q)=1/h_K(-q),\\
\qquad
 v_{\rm bdry}(q)>1\ \Longleftrightarrow\\
\ b-\beta\cdot q>0 .
\end{gathered}
\tag{25}
\]
Here \(h_K\) is positively homogeneous; its definition for any z is the same finite compact supremum. The polar formula is the normalized pairing \(t+z\cdot v\ge0\). For the speed test, equality \(h_K(-q)=1\) can occur in the unit ball only at the unique maximizer v=-q. That point belongs to \(\overline K\) exactly when \(\beta\cdot(-q)+b\le0\). If it fails this condition, compactness gives a strict smaller supremum. This proves the directional criterion including its equality case.

Consequently every direction has increased boundary speed exactly when b>|β|; no direction has increased speed exactly when b≤-|β|. The first is the interior forward Lorentz cone for \((\beta,b)\); the second is its closed backward cone. The other real coefficients can change a proper set of directions. These conclusions concern the sharp cone bound supplied by the principal symbol, not a claim that every datum attains every part of its support.

For family B write \(\eta=(y,s)\in\Omega\). Future causality gives \([F,\eta]\ge0\), by Cauchy's inequality. Hence
\[
\begin{gathered}
L_0(\eta)=-[F,\eta]-\sqrt{[\eta,\eta]}-i[E,\eta],
       \\
\qquad \operatorname{Re}L_0(\eta)<0,\\
\qquad \Sigma=\Omega .
\end{gathered}
\tag{26}
\]
Its boundary polar is the ordinary tangent light cone, already contained in C. Thus
\[
\begin{gathered}
C_\partial\subset C,\\
\qquad
                 S=C+C_\partial=C\\
\quad\text{in family B}.
\end{gathered}
\tag{27}
\]
The conditions in B are invariant under real Lorentz maps preserving future orientation, since they consist only of the form and that cone. Such maps act on the complex tangent coefficient vector \(F+iE\) and leave the coefficient of \(D_a\) equal to one. The unchanged real cone follows explicitly from 26–27; invariance alone is not used as a missing proof.

For real isotropic \(0<b<1,\ \beta=0\), put c=\(\sqrt{1-b^2}\). Then
\[
\begin{gathered}
\Sigma=\{s>|y|/c\},\\
\quad
 C_\partial\\
=\{a=0,\ t\ge c|z|\},\\
\quad
              v_{\rm bdry}=1/c .
\end{gathered}
\tag{28}
\]
For the full combined cone S, minimize the sum of an interior time and a boundary time. For fixed normal a and tangent radius ρ=|z|, the triangle inequality bounds the boundary displacement below by the difference of the two tangent lengths. Equality is attained with aligned tangent vectors. An interior tangent length r>ρ cannot minimize, since both terms then increase as r increases; opposite alignment only enlarges the boundary length. The exact minimum therefore reduces to
\[
\begin{gathered}
T_S(a,\rho)\\
=\min_{0\le r\le\rho}\\
                  \{\sqrt{a^2+r^2}+c(\rho-r)\}.
\end{gathered}
\tag{29}
\]
The derivative is \(r/\sqrt{a^2+r^2}-c\), increasing in r when a≠0. It vanishes at \(r_*=c|a|/\sqrt{1-c^2}\). The a=0 case is the immediate minimum cρ at r=0. Therefore
\[
\begin{gathered}
T_S(a,\rho)\\
=  \begin{cases}
 \sqrt{a^2+\rho^2},&\begin{gathered}\rho\le\\
c|a|/\sqrt{1-c^2}\end{gathered},\\
 \sqrt{1-c^2}|a|+c\rho,&\begin{gathered}\rho\ge\\
c|a|/\sqrt{1-c^2}\end{gathered}.
 \end{cases}
\end{gathered}
\tag{30}
\]
Both formulas agree at the threshold with matching first derivative. This is an exact closed-cone computation. [Boundary fundamental kernels and their propagation support](boundary-fundamental-kernels-and-their-propagation-support.md) gives this S as a support bound for the boundary kernels relative to its two declared inputs.

A source at positive normal position a0 has a direct unit-speed interior path and a path that reaches the boundary, uses its faster tangent cone, and returns into the half-space. Minimizing the two interior legs by the triangle inequality combines their normal lengths a0+a. Equality is attained by dividing their combined tangent displacement in the ratio a0:a; zero legs use the evident zero displacement, and when both are zero the tangent triangle inequality suffices. The geometric causal-path bound is
\[
\begin{gathered}
T_{\rm paths}(a,\rho;a_0)\\
=        \min\left\{\begin{gathered}\sqrt{(a-a_0)^2+\rho^2},\\
\ T_S(a+a_0,\rho)\end{gathered}\right\},
                   \\
\qquad a,a_0\ge0 .
\end{gathered}
\tag{31}
\]
This is a bound determined by the propagation cones. Proving that a specified forced Green function is nonzero on every part of this envelope requires a separate kernel argument; the picture alone does not prove that support equality. The explicit point-source argument is given in [A reflected wave and its faster boundary pulse](a-reflected-wave-and-its-faster-boundary-pulse.md).

## Exercises with complete solutions

**Exercise 1 (entry: twice the speed of light).** Find an admissible real isotropic boundary derivative whose boundary cone has speed two. Compute its combined cone front and contrast it with b=2.

**Solution.** Take β=0 and \(b=\sqrt3/2<1\). Family A holds and c=1/2. Equations 28–30 give
\[
\begin{gathered}
v_{\rm bdry}=2,\\
\qquad
 T_S(a,\rho)\\
=  \begin{cases}\sqrt{a^2+\rho^2},&\rho\le|a|/\sqrt3,\\
 (\sqrt3/2)|a|+\rho/2,&\rho\ge|a|/\sqrt3.
 \end{cases}
\end{gathered}
\tag{32}
\]
The faster branch begins exactly where the interior tangent slope equals one half. For b=2 and β=0, the quadratic at ω=0 has \(q^2=-1/3\); its inside imaginary root is admissible. It gives a negative-imaginary time zero for the actual determinant, so no lower strip can remain zero-free. A large positive real time coefficient is therefore not an admissible faster-speed parameter.

**Exercise 2 (intermediate: the null Lorentz endpoint).** Test the complex coefficients \(\beta=(1/2+i/2,i/2)\), \(b=-2+i\). Then compare \(\beta=(1-i,i)\), \(b=-1+i\), with the same β first component but second component 2i. Explain the role of the separate inequality in 2.

**Solution.** In the first system p=(1/2,0), q=(1/2,1/2), α=-2, γ=1. Thus
\[
\begin{gathered}{}
[F,F]=15/4,\\
\quad 1+[E,E]=3/2,\\
\quad [E,F]=-9/4,\\
\qquad
 [F,F](1+[E,E])\\
-[E,F]^2=9/16>0 .
\end{gathered}
\tag{33}
\]
F is strictly future timelike because its time component is two and its spatial length is one half. The system is admissible in family B and its propagation cone is the ordinary light cone. Its finite containment matrix is \(I_2-AA^T=\begin{pmatrix}15/16&3/16\\3/16&3/16\end{pmatrix}\), with determinant 9/64; this agrees exactly with 20.

For the second pair F=(1,0,1) is future null and E=(-1,1,-1), so
\[
\begin{gathered}{}
[F,F]=0,\\
\quad [E,F]=0,\\
\quad1+[E,E]=0;
 \\
\qquad
 \beta=(1-i,2i):\\
\quad1+[E,E]=-3 .
\end{gathered}
\tag{34}
\]
The first null pair is admissible, including equality in both Lorentz inequalities. In the altered pair the determinant inequality still reads 0≤0, but the separate nonnegative condition fails. It is not admissible. In the corresponding containment matrix the zero first diagonal and off-diagonal entries leave precisely the remaining value \(1+[E,E]\); dropping its sign would accept a negative quadratic direction.

**Exercise 3 (advanced: a lower-dimensional exception).** Take only one tangent spatial coordinate, so d=1 and n=3. Set \(b=2+i\), \(\beta=(14+13i)/5\). Verify that this is hyperbolic even though it belongs to neither family in 2. Identify the failed geometric step if the n≥4 hypothesis were dropped.

**Solution.** W consists of the two points ±β, rather than an interval or a full ellipse. The quadratic preimages of β are
\[
                         T_b(q)=\beta:\qquad q=1/5,\ 2+i .
 \tag{35}
\]
Their product is \((2+i)/5=(b-1)/(b+1)\), and their sum is \(2\beta/(b+1)\), directly verifying the quadratic. The first root is real inside the unit disk, so is excluded from the nonreal test. The second lies outside the disk. For -β the roots are their negatives, with the same exclusions. Consequently no selected lower-time root gives a determinant zero. The time principal value b-1 is nonzero, and homogeneity gives the zero-free strip. Explicitly,
\[
\begin{gathered}
q=1/5:\\
\quad\zeta=(q+q^{-1})/2=13/5\ \text{is real};
                \\
\qquad |2+i|=\sqrt5>1 .
\end{gathered}
\tag{36}
\]
An exterior q can map to a nonreal ζ but is the wrong square-root branch; it cannot be substituted into the selected determinant. The system fails A because its coefficients are nonreal and fails B because \(\operatorname{Re}b>0\). There is no contradiction: in d=1, W has two isolated points and can sit on the exceptional real-preimage curve. The interval/ellipse confinement in 7–14 requires d≥2. The source dimension is retained exactly.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Open lecture notes](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
