# Recovering singularities from convolution profiles

Original exposition and proofs: GPT-6.1 Sol (OpenAI), Ultra. CC0 1.0. Self-checked by the writing AI; independent mathematical review is not claimed.

The Fourier transform turns convolution into multiplication. Logarithmic profiles record the singular geometry visible along particular escaping frequencies. We can select one such profile by convolving with a compact function singular at a single point. This gives exact criteria for recovering the possible input singularities from a bound on the output.

Basic references are Tao's *246B, Notes 2* and *245B, Notes 9*, and Hörmander's *The Analysis of Linear Partial Differential Operators I* and *II*. The prerequisites are Locating singularities through logarithmic Fourier strips, for the convex singular hull; Singularities and nonconvex logarithmic carriers, for localization in a closed union; Convolution and joint frequency carriers, for common-frequency addition; and Slow decrease and entire Fourier division, for invertibility. The [complete proof](singular-hull-realization-formal.md) supplies the realization, inverse criterion, universal hull addition, difference-set bound and full polynomial-profile argument, including the finite-jet description of point-supported distributions.

## 1. What a single profile can recover

Use
\[
 F_u(\zeta)=\langle u,e^{-ix\cdot\zeta}\rangle,\qquad
 L_u(z,c)=\frac{\log|F_u(c+z\log|c|)|}{\log|c|},
 \quad c\in\mathbb R^n,\quad |c|>2.
 \tag{T1}
\]
Proper profiles are canonical PSH local \(L^1\) limits. A collapsed profile tends uniformly locally to \(-\infty\). Write \(\mathcal J(u)\) for their indicators and \(C_h\) for an indicator's carrier. The proper carrier is nonempty and compact convex; the collapsed carrier is empty.

Let \(S_u=\operatorname{conv}(\operatorname{sing\,supp}u)\), including the empty hull. The earlier hull theorem says
\[
 S_u=\overline{\operatorname{conv}
                \bigcup_{h\in\mathcal J(u)} C_h}.
 \tag{T2}
\]
Individual carriers may differ. The hull combines all of them.

Theorem 2.1 of the complete proof selects any prescribed \(h\in\mathcal J(u)\): for every \(\varepsilon>0\), there is a compact continuous \(w\notin C^1\), supported in the radius-\(\varepsilon\) ball, with
\[
 \operatorname{sing\,supp}w=\{0\},\qquad S_{u*w}=C_h.
 \tag{T3}
\]
A collapsed \(h\) gives a smooth output. Translating this \(w\) to a point \(x\) translates the output hull to \(C_h+x\).

The construction keeps \(u\) controlled on expanding logarithmic neighborhoods of the chosen frequencies and makes \(w\) collapse outside those neighborhoods. At a subsequence of their original centers, \(w\)'s profile is exactly zero. The product therefore attains the chosen \(u\) profile. Every other proper output profile has a carrier inside its carrier, which proves the exact hull equality rather than just an upper bound.

## 2. The inverse criterion and two kinds of subtraction

Fix nonempty compact convex \(K,K'\), and let \(H_K\) be the support function of \(K\). The inverse criterion is
\[
 \begin{split}
 &\operatorname{sing\,supp}(u*w)\subset K
      \Longrightarrow \operatorname{sing\,supp}w\subset K'
      \quad\text{for every compact }w\\
 &\quad\Longleftrightarrow\\
 &\text{for every }h\in\mathcal J(u),\
      h(\eta)+x\cdot\eta\leq H_K(\eta)
      \text{ for all real }\eta
      \Longrightarrow x\in K'.
 \end{split}
 \tag{T4}
\]
For a proper \(h\), the displayed inequalities say exactly \(C_h+x\subset K\). Necessity follows by using the selected one-point singularity at \(x\). For sufficiency, place each proper \(w\) profile jointly with a \(u\) profile on the same frequencies. Their carrier sum is inside \(K\), so each point of the \(w\) carrier satisfies the geometric premise.

The sharper conclusion is
\[
 \operatorname{sing\,supp}w\subset\overline{T_K(u)},\qquad
 T_K(u)=\bigcup_{h\in\mathcal J(u)}
                     \{x:C_h+x\subset K\}.
 \tag{T5}
\]
For a collapsed indicator the corresponding set of \(x\)'s is all real space. The closure in (T5) is taken without a convex hull. Its proof uses the earlier localization in a closed union of carriers.

For a particular nonempty carrier \(C\), the allowable translations \(\{x:C+x\subset K\}\) require every point of the translated carrier to stay in \(K\). The Minkowski difference set is instead
\[
 K-C=\{k-c:k\in K,\ c\in C\}.
 \tag{T6}
\]
It permits a difference of some two points. These two sets can be quite different. The notation \(K-C\) in this lesson always means (T6).

![Exact rectangles compare all admissible translations of a carrier with the larger Minkowski difference set, and show one contained translation and one that leaves the output rectangle.](figures/admissible-translations-and-difference-sets.png)

*Figure 1.* Take \(K=[-3,5]\times[-2,4]\) and \(C=[1,2]\times[-1,1]\). The allowable translations form \([-4,3]\times[-1,3]\), whereas \(K-C=[-5,4]\times[-3,5]\). The translation \((2,1)\) is allowable. The translation \((4,4)\) lies in the difference set, but its translated carrier is not inside \(K\). These are geometric calculations for one carrier; they do not prescribe an actual distribution's whole profile family. Proof locators: complete proof, Theorem 3.1 and Corollary 6.1; Exercise 3. Background: Hörmander's convolution geometry.

If any \(u\) profile collapses, every point \(x\) is geometrically allowable. No compact \(K'\) can contain them all. Thus the inverse criterion requires invertibility.

For an invertible \(u\), the complete proof gives the uniform bound
\[
 S_w\subset S_{u*w}-S_u.
 \tag{T7}
\]
When the output is smooth, invertibility forces \(w\) to be smooth, and both sides are empty. For nonempty hulls the proof uses
\(h(\eta)+h(-\eta)\geq0\) for every nonempty carrier. It does not assume either of the separate support values is nonnegative.

## 3. Universal hull addition is a stronger condition

For a fixed compact \(u\), the exact identity
\[
 S_{u*w}=S_u+S_w\quad\text{for every compact }w
 \tag{T8}
\]
holds precisely when \(\mathcal J(u)\) is the singleton \(\{H_{S_u}\}\). If \(u\) is smooth, the singleton is the collapsed indicator \(-\infty\), and both sides of (T8) are empty.

For nonsmooth \(u\), all profile carriers must be the same \(S_u\). Necessity uses the one-point singularity test (T3). Sufficiency uses the joint-profile theorem: every proper output carrier is \(S_u+C_w\), and every proper \(w\) carrier occurs in such a joint pair. Taking support-function suprema gives the Minkowski sum of the singular hulls.

Invertibility rules out collapsed profiles. It does not require all the remaining carriers to coincide.

## 4. Four worked examples

### Example 1: different constant profiles with the same carrier

Take \(P(\zeta_1,\zeta_2)=\zeta_1^3\), the transform of \((-i\partial_1)^3\delta_0\). For \(t\to\infty\), choose
\(c(t)=(t^\alpha,t)\), \(0\leq\alpha\leq1\), and \(q=|c(t)|\). Then
\[
 L_u(z,c(t))=\frac{3\log|t^\alpha+z_1\log q|}{\log q}.
 \tag{T9}
\]
For \(0<\alpha\leq1\), factor out \(t^\alpha\). The ratio \(\log q/t^\alpha\) tends to zero, and \(\log t/\log q\to1\). Hence (T9) converges locally uniformly to \(3\alpha\).

For \(\alpha=0\), write
\[
 L_u(z,c(t))=\frac{3\log\log q}{\log q}
       +\frac{3\log|z_1+1/\log q|}{\log q}.
 \tag{T10}
\]
The second numerator converges in local \(L^1\) to \(3\log|z_1|\), by the polynomial-logarithm argument in Proposition 7.1 of the complete proof. Both terms of (T10) therefore tend to zero in local \(L^1\). Convergence is not uniform near the moving zero \(z_1=-1/\log q\).

This polynomial realizes all constants in \([0,3]\). Each constant's indicator is zero and its carrier is \(\{0\}\). Distinct profiles need not have distinct carriers.
For comparison, the one-dimensional polynomial \(P(\zeta)=\zeta^3\) has only the constant-three profile along escaping real frequencies: \(q=|c|\), and \(|c+z\log q|/q\to1\) uniformly on compact parameter sets. The general interval bound does not assert that every constant occurs for every polynomial.

### Example 2: an exact inverse bound for a point-supported operator

Let \(x_0=(2,-1)\) and
\[
 u=(1-\partial_1^2-\partial_2^2)\delta_{x_0},\qquad
 F_u(\zeta)=(1+\zeta_1^2+\zeta_2^2)e^{-ix_0\cdot\zeta}.
 \tag{T11}
\]
Every profile indicator of \(u\) is \(h(\eta)=2\eta_1-\eta_2\), by the polynomial and translation results in the complete proof. Its carrier and singular hull are \(\{x_0\}\).
If the output singular support is inside
\(K=[-3,5]\times[-2,4]\), the geometric criterion requires
\[
 x+x_0\in K,\qquad
 x\in K-x_0=[-5,3]\times[-1,5].
 \tag{T12}
\]
Thus every compact \(w\) with the specified output bound has its singular support in this exact rectangle.

The rectangle is sharp. For each \(x\) in it, take \(w=\delta_x\). Then \(u*w\) is the same nonzero polynomial operator at \(x+x_0\), singular only there, so it lies in \(K\); the input is singular at \(x\). A universal input bound must include every such \(x\).
The singleton-indicator theorem also gives the stronger exact identity \(S_{u*w}=x_0+S_w\) for every compact \(w\). It describes singular hulls, without asserting equality of arbitrary singular-support sets.

### Example 3: an invertible input whose singular hull can shrink

Choose a nonnegative smooth \(f\), positive on \((1,2)\), supported in \([1,2]\), with \(\int f=1\), and put
\[
 u=\delta_{(0,0)}+\tfrac14\delta_0\otimes f,\qquad
 F_u(\zeta_1,\zeta_2)=1+\tfrac14F_f(\zeta_2).
 \tag{T13}
\]
For real frequencies \(|F_f|\leq1\), so
\[
 |F_u(\xi)|\geq\tfrac34.
 \tag{T14}
\]
This implies the real logarithmic-window lower bound at every center, and hence invertibility.
Its singular support is
\(\{(0,0)\}\cup(\{0\}\times[1,2])\).
At a nonzero point of \(f\), the factor \(\delta_0\) is singular in the first coordinate. Boundary points belong to the singular support because every neighborhood contains such points. Near the origin the isolated point mass cannot cancel the line-supported term, whose support is separated from it. Outside these sets the distribution vanishes locally. Thus
\[
 S_u=\{0\}\times[0,2].
 \tag{T15}
\]

Nevertheless \(u\) has the zero profile. Take \(c_j=(e^j,e^{j/2})\), \(q_j=|c_j|\). On \(|z|\leq M\), the real part of \(e^{j/2}+z_2\log q_j\) has modulus at least \(q_j^{1/2}/4\) for all sufficiently large \(j\). Repeated integration by parts in the compact smooth \(f\) gives, for every integer \(k\),
\[
 |F_f(e^{j/2}+z_2\log q_j)|
       \leq 4^k\|f^{(k)}\|_1 q_j^{-k/2+2M}.
 \tag{T16}
\]
There are no boundary terms. The factor \(q_j^{2M}\) bounds the imaginary exponential on \(1\leq y\leq2\). Choose \(k>4M\); then this tends uniformly to zero. The transform in (T13) tends uniformly to one on the parameter compact set, so \(L_u\to0\) uniformly there.

Theorem 2.1 now supplies a compact continuous \(w\), singular exactly at zero, with
\[
 S_{u*w}=\{0\},\qquad S_u+S_w=\{0\}\times[0,2].
 \tag{T17}
\]
Thus universal hull addition fails for this invertible input. The selected output is also singular exactly at zero: its nonempty hull is that singleton. The hull recovery theorem forces some other proper carrier of \(u\) to differ from \(\{0\}\). We do not assert an explicit formula for the selected \(w\); the preceding complete construction proves its existence.

![The actual input has an isolated point and a vertical singular segment, the selected compact factor is singular only at the origin, and the output singular hull is the origin rather than their longer hull sum.](figures/invertibility-without-universal-hull-addition.png)

*Figure 2.* This is the exact singular geometry of (T13)–(T17), not a graph of distribution density. Blue marks the input singular locus; its convex hull is the vertical segment from zero to two. The selected factor is supported in a ball of radius \(1/5\) and singular only at its center; the circle is an allowed support bound. The green output hull is the singleton origin. The dashed vertical segment on the right is \(S_u+S_w\), which differs from the actual output hull. Proof locators: Example 3; complete proof, Theorems 2.1 and 5.1. Background: Hörmander's profile criteria and Tao's Fourier support discussion.

### Example 4: smooth inputs and the empty hull

Let \(u\) be any nonzero compact smooth function. Every profile collapses, \(S_u=\varnothing\), and \(u*w\) is smooth for every compact distribution \(w\). Therefore
\[
 S_{u*w}=\varnothing=\varnothing+S_w.
 \tag{T18}
\]
Universal hull addition holds in this empty case.
No compact \(K'\) can bound the input singularities from a fixed nonempty compact output bound \(K\). Choose \(x\notin K'\) and \(w=\delta_x\). The convolution is a smooth translate of \(u\), with empty singular support contained in \(K\), whereas \(w\) is singular at \(x\). This violates the proposed inverse bound. In the geometric criterion, the collapsed indicator makes every \(x\) allowable.

The zero input behaves the same way for these two statements: every output is smooth, universal empty-hull addition holds, and an inverse compact singular-support bound fails. This does not make it invertible.

## Exercises with complete solutions

The exercises total 100 points.

### Exercise 1: constant profiles versus zero indicators (8 points)

For \(P(\zeta_1,\zeta_2)=\zeta_1^3\), find a center sequence giving the constant \(3/2\). Explain why its carrier remains zero and why the analogous one-dimensional polynomial cannot give that constant.

*Solution.* Choose \(c(t)=(t^{1/2},t)\). Then \(q/t\to1\), and
\[
 \frac{3\log|t^{1/2}+z_1\log q|}{\log q}
 =\frac{(3/2)\log t}{\log q}
       +\frac{3\log|1+z_1\log q/t^{1/2}|}{\log q}
       \longrightarrow\tfrac32
 \tag{T19}
\]
locally uniformly. A finite constant divided by a large positive dilation has directional indicator zero, whose carrier is the singleton \(\{0\}\).
In one dimension, \(|c|=q\), so the cubic has normalized logarithm tending to three on compact parameter sets. There is no separate large coordinate that lets the polynomial's first coordinate grow as \(q^{1/2}\). The degree interval bounds possible constants without guaranteeing all of them.

### Exercise 2: the translation sign (8 points)

If \(w_x(y)=w(y-x)\), derive the change in its normalized logarithm and carrier. Apply it to \(x=(2,-1)\) and a zero-indicator profile.

*Solution.* Substituting the translation in the Fourier pairing gives \(F_{w_x}(\zeta)=e^{-ix\cdot\zeta}F_w(\zeta)\). At \(\zeta=c+z\log|c|\), the real \(c\) contributes a unit-modulus phase and
\[
 \log|e^{-ix\cdot(c+z\log|c|)}|
       =(x\cdot\operatorname{Im}z)\log|c|.
 \tag{T20}
\]
Thus \(L_{w_x}=L_w+x\cdot\operatorname{Im}z\). A proper indicator becomes \(h(\eta)+x\cdot\eta\), and its carrier becomes \(C_h+x\). A collapsed profile stays collapsed and its empty carrier stays empty.
For zero indicator and the stated \(x\), the new indicator is \(2\eta_1-\eta_2\), with carrier \(\{(2,-1)\}\). The sign is positive because the modulus of the spatial-translation exponential grows in the corresponding positive imaginary direction.

### Exercise 3: admissible rectangles and difference sets (10 points)

Take \(K=[-3,5]\times[-2,4]\), \(C=[1,2]\times[-1,1]\). Compute the allowable translation set and \(K-C\). Check \(x=(2,1)\) and \(x=(4,4)\).

*Solution.* Requiring every point of \(C+x\) to lie in \(K\) is exactly
\[
 x_1+1\geq-3,\quad x_1+2\leq5,\quad
 x_2-1\geq-2,\quad x_2+1\leq4.
 \tag{T21}
\]
Thus the allowable set is \([-4,3]\times[-1,3]\). Direct coordinate differences give \(K-C=[-5,4]\times[-3,5]\).
For \(x=(2,1)\), \(C+x=[3,4]\times[0,2]\subset K\).
For \(x=(4,4)\), \(C+x=[5,6]\times[3,5]\) exceeds both the right and upper bounds. Yet this \(x\) belongs to \(K-C\): for instance \((5,4)-(1,0)=(4,4)\), with the first point in \(K\) and the second in \(C\).
The existence of that one point difference does not place the whole translated carrier inside \(K\).

### Exercise 4: a nonconvex union of allowable translations (10 points)

Consider the hypothetical carrier family \(\{C_-,C_+\}\), with \(C_\pm=\{(\pm2,0)\}\), and let \(K\) be the closed unit disk. Compute its union of allowable translations. Show why adding a convex hull changes it. Does this calculation establish that a distribution has exactly this profile family?

*Solution.* For \(C_+\), the condition is \(x+(2,0)\in K\), so its allowable set is the closed unit disk centered at \((-2,0)\). For \(C_-\), it is the disk centered at \((2,0)\). Their union is closed and nonconvex:
\[
 T=\overline B_1((-2,0))\cup\overline B_1((2,0)).
 \tag{T22}
\]
The origin lies in their convex hull, as the midpoint of their centers, but in neither disk because its distance to each center is two. Taking only the closure preserves the exclusion of the origin.
This is a geometric calculation for a stated family. It does not establish its realization as some \(\mathcal J(u)\). Theorem 2.1 selects a profile already present in a known distribution; it does not prescribe arbitrary complete profile families.

### Exercise 5: why the selected hull is exact (10 points)

Suppose the construction has a proper selected \(u\) profile with carrier \(C_h\), a zero selected \(w\) profile, exterior collapse of \(w\), and singular support of \(w\) equal to \(\{0\}\). Explain both inclusions proving \(S_{u*w}=C_h\).

*Solution.* On the selected original centers, the product logarithms are the exact sum of the two input logarithms. Their proper \(L^1\) limit is the selected \(u\) profile plus zero. Its indicator is \(h\), so the output profile family contains the carrier \(C_h\). The hull formula (T2) gives \(C_h\subset S_{u*w}\).
Conversely a proper output profile cannot have infinitely many exterior centers: \(w\) collapses there and the other normalized logarithms are locally bounded above, which would collapse an output subsequence. Inside the selected neighborhood, extract both input profiles on the same subsequence. Both are proper. The \(u\) profile satisfies the global continuous ceiling \(N+h(\operatorname{Im}z)\), so its carrier is contained in \(C_h\).
The \(w\) carrier is a nonempty subset of its singular hull \(\{0\}\), hence equals \(\{0\}\). Exact indicator addition makes the output carrier the \(u\) carrier plus \(\{0\}\), still contained in \(C_h\). Every proper output carrier lies there, and \(C_h\) is closed convex. Their closed convex hull gives the reverse inclusion.

### Exercise 6: negative support values and the subtraction bound (8 points)

Let \(C=[2,4]\) and \(K=[-1,6]\) on the line. Find the support function \(h\), its values in directions one and minus one, and the exact translation set. Compare that set with \(K-C\), and verify the two-direction estimate used in Corollary 6.1.

*Solution.* The support function is \(h(\eta)=4\eta\) for \(\eta\geq0\), and \(h(\eta)=2\eta\) for \(\eta<0\). Thus \(h(1)=4\), \(h(-1)=-2\), while \(h(1)+h(-1)=2\geq0\).
The containment \(C+x\subset K\) gives \(x+2\geq-1\), \(x+4\leq6\), hence \(x\in[-3,2]\). The difference set is the larger \([-5,4]\).
For a permissible \(x\), the proof inequality is
\[
 x\eta\leq H_K(\eta)-h(\eta)
       \leq H_K(\eta)+h(-\eta).
 \tag{T23}
\]
At \(\eta=1\) its exact upper bound is \(x\leq6-4=2\), and the coarser difference bound is \(x\leq6-2=4\).
At \(\eta=-1\) its exact bound is \(-x\leq1-(-2)=3\), while the difference bound is \(-x\leq1+4=5\). A support function can be negative in one direction. The sum in opposite directions, not either separate sign, validates (T23).

### Exercise 7: a finite jet and its exact distribution order (12 points)

On the line define \(T(\phi)=3\phi(0)-2\phi''(0)+\phi'''(0)\). Write \(T\) as delta derivatives, compute its Fourier polynomial, prove its order is exactly three, and identify its possible logarithmic profiles.

*Solution.* Since \(\partial^k\delta_0(\phi)=(-1)^k\phi^{(k)}(0)\),
\[
 T=3\delta_0-2\partial^2\delta_0-\partial^3\delta_0,\qquad
 F_T(\zeta)=3-2(i\zeta)^2-(i\zeta)^3
          =3+2\zeta^2+i\zeta^3.
 \tag{T24}
\]
The representation gives a seminorm bound through order three. To rule out order two, choose a smooth compact \(\chi\) equal to one near zero and set \(\phi_\varepsilon(x)=x^3\chi(x/\varepsilon)/6\). Its lower jets at zero vanish and its third derivative there equals one, so \(T(\phi_\varepsilon)=1\). For \(k=0,1,2\), Leibniz's rule on the shrinking support gives \(\|\phi_\varepsilon^{(k)}\|_\infty=O(\varepsilon^{3-k})\to0\). An order-two continuity bound would make its distribution values tend to zero, a contradiction.
For real \(|c|=q\to\infty\), the leading cubic term dominates uniformly at \(c+z\log q\) on compact \(z\) sets. Its modulus divided by \(q^3\) tends to one. Thus the normalized logarithm tends to three, the only possible profile. Its indicator is zero and carrier \(\{0\}\), so \(T\) is invertible and has universal singular-hull addition.

### Exercise 8: a collapsed indicator defeats an inverse compact bound (10 points)

Let \(-\infty\in\mathcal J(u)\), and let \(K,K'\) be nonempty compact convex sets. Construct a counterexample to the implication in (T4), and explain why this does not contradict universal empty-hull addition for smooth \(u\).

*Solution.* Choose \(x\notin K'\). The collapsed-profile realization supplies a compact continuous \(w\), singular exactly at zero, with \(u*w\) smooth. Translate it to \(x\). The new input is singular exactly at \(x\), and the output is a smooth translate, whose empty singular support is contained in \(K\). The proposed implication fails.
Geometrically, \(-\infty+x\cdot\eta\leq H_K(\eta)\) holds for every direction and every \(x\), so the criterion would force \(K'\) to contain all real space.
If \(u\) is smooth, universal addition compares the output hull with \(S_u+S_w=\varnothing\). That identity is true for all \(w\), but it cannot bound their arbitrary singularities. The inverse criterion and universal addition are different statements.

### Exercise 9: the exact singleton-indicator condition (12 points)

Prove both directions of the universal hull-addition criterion. Explain why taking unrelated maximizing frequency sequences for the two inputs would not justify the sufficient direction.

*Solution.* Assume addition for every \(w\). Given any \(h\in\mathcal J(u)\), Theorem 2.1 gives a factor with \(S_w=\{0\}\) and output hull \(C_h\). Universal addition forces \(C_h=S_u\). If it is empty, \(u\) is smooth and all its profiles collapse. Otherwise every indicator equals \(H_{S_u}\), with no collapsed indicator.
Conversely suppose this singleton condition. If \(u\) is smooth, every output is smooth and the empty identity follows. Otherwise every proper \(w\) carrier \(C_w\) can be extracted jointly with a \(u\) profile whose carrier is \(S_u\); thus \(S_u+C_w\) is an output carrier. Every proper output also has such a joint extraction, and neither input can collapse. Therefore these are exactly the proper output carriers.
Taking support functions of their closed convex hull gives
\[
 H_{S_{u*w}}(\eta)
    =\sup_{h_w}\bigl(H_{S_u}(\eta)+h_w(\eta)\bigr)
    =H_{S_u}(\eta)+H_{S_w}(\eta).
 \tag{T25}
\]
If \(w\) is smooth, both sides have empty hulls instead. Equality of support functions gives the desired sum.
The product's two profiles must use the same real frequencies. Independent maximizing sequences need not give a joint pair and cannot be substituted in a convolution limit. The finite joint-projection theorem is what permits every proper \(w\) profile to appear in an actual common-frequency pair.

### Exercise 10: an invertible input with a smaller selected output (12 points)

For \(u\) in Example 3, prove its real transform bound. On \(|z|\leq M\), derive (T16), including the threshold for the real denominator, and explain the strict failure of universal hull addition.

*Solution.* The physical integral and \(\int f=1\) give \(|F_f(\xi_2)|\leq1\) on real frequencies. The reverse triangle inequality gives \(|1+\frac14F_f(\xi_2)|\geq3/4\), a uniform real lower bound. It implies slow decrease and invertibility by the preceding theorem.
For \(q_j=(e^{2j}+e^j)^{1/2}\), we have \(e^{j/2}\geq q_j^{1/2}/2\). Once \(M\log q_j\leq q_j^{1/2}/4\),
\[
 |\operatorname{Re}(e^{j/2}+z_2\log q_j)|
       \geq q_j^{1/2}/4.
 \tag{T26}
\]
Integrating the smooth compact \(f\) by parts \(k\) times gives a denominator with modulus at least \((q_j^{1/2}/4)^k\). On its support the exponential modulus is at most \(e^{2M\log q_j}=q_j^{2M}\). This proves (T16) with \(4^k\|f^{(k)}\|_1\). The threshold exists because \(\log q/q^{1/2}\to0\). Choose an integer \(k>4M\) to force uniform decay.
Thus the selected \(u\) profile is zero. The realization theorem produces \(w\) with singular support \(\{0\}\) and output hull \(\{0\}\). Meanwhile \(S_u\) is the nontrivial vertical segment (T15), so \(S_u+S_w=S_u\neq\{0\}\). Invertibility excludes collapsed profiles; it does not remove the different proper carriers responsible for this failure.

## References

- Terence Tao, [246B, Notes 2: Some connections with the Fourier transform](https://terrytao.wordpress.com/2021/01/23/246b-notes-2-some-connections-with-the-fourier-transform/), 2021. Background on compact support and Fourier transforms; its normalization differs from (T1).
- Terence Tao, [245B, Notes 9: The Baire category theorem and its Banach space consequences](https://terrytao.wordpress.com/2009/02/01/245b-notes-9-the-baire-category-theorem-and-its-banach-space-consequences/), 2009. Background on the preceding frequency-selective construction.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer, 1983.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, Springer, 1983, Chapter XVI. The complete realization and singular-hull arguments are supplied in the full proof above.
