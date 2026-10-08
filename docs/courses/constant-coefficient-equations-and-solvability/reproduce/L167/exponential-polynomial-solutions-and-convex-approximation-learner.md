# Learning convex approximation for convolution equations

Original exposition, examples and solutions: GPT-6.1 Sol (OpenAI), Ultra. CC0 1.0. Self-checked by the writing AI; independent mathematical review is not claimed.

A compact convolution kernel determines where a local equation makes sense. Its complex characteristic frequencies supply explicit entire solutions. On an open convex set, finite sums of these solutions approximate every smooth homogeneous solution, with all derivatives on each compact observation set. The proof connects three objects: an annihilator, an entire quotient, and a convex analytic carrier.

Basic references are Grubb's [Fourier transformation of distributions](https://web.math.ku.dk/~grubb/dist5.pdf), Melrose's [Tempered distributions and the Fourier transform](https://math.mit.edu/~rbm/iml/Chapter1.pdf), and Hörmander's *The Analysis of Linear Partial Differential Operators I* and *II*. Read Compact Fourier division and multiplicity-sensitive annihilators for the negative-exponential transform convention, and Fourier transforms of analytic functionals on a real convex carrier for the precise small-exponential-loss criterion. The complete arguments for this lesson are Theorems 1.1, 3.1 and 5.1 and Lemmas 4.1–4.2 below.

## 1. The equation and the approximation topology

For a nonzero compact distribution \(\mu\), put
\[
 X_\mu=\{x:x-\operatorname{supp}\mu\subset X\}.
 \tag{L1}
\]
Every point used in the convolution must belong to \(X\). This condition, together with a neighborhood of the compact translated support, lets the finite-order distribution act on \(y\mapsto u(x-y)\). The set \(X_\mu\) is open. It is convex when \(X\) is convex.

The homogeneous solution space is
\[
 N_\mu(X)=\{u\in C^\infty(X):\mu*u=0\text{ in }X_\mu\}.
 \tag{L2}
\]
The approximating space \(E_\mu\) consists of finite linear combinations of
\[
 f(x)e^{ix\cdot\lambda},\qquad
 f\text{ a polynomial},\quad\lambda\in\mathbb C^n,
 \quad\mu*(f e^{ix\cdot\lambda})=0\text{ everywhere}.
 \tag{L3}
\]
The polynomial factors remember zero multiplicities. Theorem 5.1 says that for each compact \(K\subset X\), derivative order \(m\), and tolerance \(\varepsilon>0\), a single such finite sum satisfies
\[
 \max_{|\alpha|\leq m}\sup_K|\partial^\alpha(u-h)|<\varepsilon.
 \tag{L4}
\]
An approximation on one compact set does not impose a global growth bound on \(u\), and the finite sum can change when the set, derivative order or tolerance changes.

## 2. Why the reflected symbol appears

Write
\[
 F_v(\zeta)=v(e^{-ix\cdot\zeta}),\qquad
 B(\zeta)=F_\mu(-\zeta).
 \tag{L5}
\]
Then
\[
 \mu*e^{-ix\cdot\zeta}=B(\zeta)e^{-ix\cdot\zeta}.
 \tag{L6}
\]
At a zero of \(B\) of directional order \(r\), differentiating (L6) \(k<r\) times produces the solutions
\((-ix\cdot\theta)^k e^{-ix\cdot\zeta}\).
If a compact \(v\) kills all solutions, its transform has all the corresponding zero derivatives. One-variable division on transverse complex lines removes every zero of \(B\). A Cauchy circle that surrounds the roots makes the quotient holomorphic in the other variables too, even when roots collide. Theorem 1.1 gives the exact equivalence
\[
 v(E_\mu)=0
 \quad\Longleftrightarrow\quad
 F_v=B G\text{ with }G\text{ entire}.
 \tag{L7}
\]
The converse uses the full finite polynomial-jet product identity, so it covers arbitrary polynomial factors rather than only powers of one directional coordinate.

**Example 1: a shifted first derivative.** Let \(\mu=\delta'_a\) on the line, with \(a=3/4\). The derivative distribution acts by \(\delta'_a(\phi)=-\phi'(a)\). Consequently
\[
 \mu*u(x)=u'(x-a),\qquad
 F_\mu(\zeta)=i\zeta e^{-ia\zeta},\qquad
 B(\zeta)=-i\zeta e^{ia\zeta}.
 \tag{L8}
\]
Take \(X=(-2,2)\). Then \(X_\mu=(a-2,a+2)\), and the local equation says \(u'=0\) throughout \(X\). Its solutions are constants.
At a characteristic frequency the polynomial factor must also be constant: the only zero of \(B\) is the simple zero at the origin. Thus \(E_\mu\) consists exactly of constants, and approximation is equality in this example.

For \(v=\delta_{-1}-\delta_1\), the transform is \(2i\sin\zeta\), and its quotient is
\[
 G(\zeta)=-2e^{-ia\zeta}\frac{\sin\zeta}{\zeta}.
 \tag{L9}
\]
The apparent singularity at zero is removable. The quotient's carrier is \([a-1,a+1]\), because \(\sin\zeta/\zeta\) is the transform of the probability measure with constant density \(1/2\) on \([-1,1]\). Multiplication by \(-2e^{-ia\zeta}\) scales and translates that measure. The reflected derivative carrier is \(\{-a\}\), and their sum is \([-1,1]=\operatorname{conv}\operatorname{supp}v\). All signs locate the carrier correctly.

**Example 2: a double translation difference.** Let \(a>0\) and
\[
 \mu=(\delta_0-\delta_a)*(\delta_0-\delta_a)
             =\delta_0-2\delta_a+\delta_{2a}.
 \tag{L10}
\]
The reflected symbol is \(B(\zeta)=(1-e^{ia\zeta})^2\). Its zeros \(2\pi k/a\) have order two, so the polynomial solutions at each frequency have the form
\[
 (A+Bx)e^{2\pi ikx/a}.
 \tag{L11}
\]
To see that there are no higher-degree polynomial factors, the second difference of a polynomial of degree \(d\geq2\) has leading coefficient \(a^2d(d-1)\) times its original leading coefficient and degree \(d-2\).

A smooth global homogeneous solution has the form
\[
 u(x)=p(x)+xq(x),\qquad p,q\text{ smooth and }a\text{-periodic}.
 \tag{L12}
\]
Indeed \(g(x)=u(x)-u(x-a)\) is periodic by the homogeneous equation. Set \(q=g/a\) and \(p=u-xq\). Then
\(p(x)-p(x-a)=g(x)-a q(x)=0\).
Conversely the second difference of (L12) is zero. Fourier partial sums for \(p,q\) converge with every fixed derivative: integrating their coefficients by parts arbitrarily many times gives bounds by every negative power of the integer frequency. On a bounded interval, multiplying the second sum by \(x\) preserves each fixed derivative convergence. This gives an explicit approximation by (L11).

## 3. Quotients have convex analytic carriers

The logarithm of a nonzero entire function is PSH, allowing minus infinity at its zeros. After smoothing the compact distributions by one nonzero compact smooth \(\phi\), the two products
\[
 F_\phi F_{\check\mu},\qquad F_\phi F_v
 \tag{L13}
\]
are transforms of compact smooth functions. Their logarithms have uniform imaginary-growth bounds and exact support indicators. Theorem 3.1 proves that their indicator difference is a support function, and gives
\[
 |G(\zeta)|\leq C_\varepsilon
 e^{H_{K_2}(\operatorname{Im}\zeta)+\varepsilon|\zeta|}
 \quad\text{for every }\varepsilon>0,
 \qquad
 K_2+\operatorname{conv}\operatorname{supp}\check\mu
       =\operatorname{conv}\operatorname{supp}v.
 \tag{L14}
\]
Every small loss is allowed, with its own constant. A real-axis polynomial bound is not asserted. The analytic-functional theorem supplies \(\sigma\) carried by \(K_2\) with \(F_\sigma=G\), including a proved action on holomorphic germs near that real convex carrier.

**Example 3: three translated rectangles.** In two dimensions take
\[
 \mu=\delta_{(0,0)}+2\delta_{(2,0)}+3\delta_{(0,1)},\qquad
 K_2=[-1/2,1/2]\times[-1/4,1/4].
 \tag{L15}
\]
Let \(\sigma\) be the probability measure with constant density on \(K_2\), and set \(v=\sigma*\check\mu\). Direct convolution pairing gives
\(v(h)=\sigma(\mu*h)=0\) for every entire homogeneous solution.
Its quotient is
\[
 G(\zeta)=
 \frac{\sin(\zeta_1/2)}{\zeta_1/2}
 \frac{\sin(\zeta_2/4)}{\zeta_2/4},
 \qquad
 H_{K_2}(\eta)=\tfrac12|\eta_1|+\tfrac14|\eta_2|.
 \tag{L16}
\]
Each sine quotient takes value one at zero. The reflected support triangle has vertices \((0,0),(-2,0),(0,-1)\) and support function
\[
 H_{K_-}(\eta)=\max\{0,-2\eta_1,-\eta_2\}.
 \tag{L17}
\]
Positive weights make the actual support of \(v\) the union of the three translated rectangles. Its convex hull is the pentagon with vertices
\[
 (-5/2,-1/4),\ (-1/2,-5/4),\ (1/2,-5/4),\
 (1/2,1/4),\ (-5/2,1/4).
 \tag{L18}
\]
Its support function is \(H_{K_2}+H_{K_-}\).
For \(X=(-3,1)\times(-2,1)\), every vertex and the whole pentagon lie in \(X\). The exact convolution domain is \(X_\mu=(-1,1)^2\), which contains \(K_2\).

![Three reflected translates of the rectangle give the actual support of the annihilator; their convex hull lies inside the open domain, and the original rectangle lies inside the convolution domain.](figures/reflected-carriers-and-convex-domain.png)

The shaded translated rectangles are the actual support. The dashed pentagon is its convex hull \(K_v=K_2+K_-\). The second panel shows the open domain \(X\), its erosion \(X_\mu\), and the analytic carrier \(K_2\). Boundary lines show the defining inequalities; they do not add boundary points to the two open sets. The caption illustrates (5.9), not an equality of nonconvex supports for arbitrary complex kernels.

## 4. From entire tests to local homogeneous solutions

On entire tests, the transform identity gives
\[
 v(h)=\sigma(\mu*h).
 \tag{L19}
\]
Differentiating at frequency zero gives every polynomial moment. Uniform Taylor convergence and the two continuity bounds then prove this identity for all entire tests.

A general smooth test cannot be inserted into an analytic functional. Instead take a compact smooth \(w\) and Gaussian-smoothed entire \(w_j=E_j*w\). Then
\[
 w_j\longrightarrow w\text{ smoothly on the real space},\qquad
 \mu*w_j=E_j*(\mu*w).
 \tag{L20}
\]
If \(\mu*w\) is analytic near \(K_2\), Lemma 4.1 proves uniform complex convergence near that carrier. Its contour move removes the positive factor from the imaginary part of the Gaussian exponent.

![A one-variable Gaussian contour is moved from the real interval to the height of the complex observation point; vertical endpoint contributions have a strictly negative exponential bound.](figures/gaussian-contour-localization.png)

For this diagram \(R=1\), \(z=2/5+i/5\), and the integration interval is \([-2,2]\). The shifted horizontal contour has height \(1/5\). The normalized logarithmic modulus on it is \(-(2/5-t)^2\). On the right and left vertical sides it is at most \(-63/25\) and \(-143/25\), respectively. Both are below the general bound \(-15/16\) used in (4.9). The curves show the actual exponent per \(j\), not a numerical proof of convergence.

To use the local equation, choose a cutoff equal to one near the whole convex carrier \(K_v\), with support in \(X\), and set \(w=\chi u\). Then \(v(w)=v(u)\), and \(\mu*w=0\) near \(K_2\). The real smooth limit controls the left side of (L19); the uniform complex limit controls the right side. Thus \(v(u)=0\). Continuous separation proves the density.

**Example 4: an empty convolution domain can still give useful approximants.** Let \(\mu=\delta_0-\delta_2\) and \(X=(-3/4,3/4)\). Then
\[
 X_\mu=X\cap(X+2)=\varnothing.
 \tag{L21}
\]
The local equation imposes no condition. Nevertheless the restrictions of the two-periodic exponentials \(e^{i\pi kx}\) are dense in all smooth functions on \(X\).
Here is a direct construction. For a compact observation set \(K\subset X\), choose \(\chi\in C_c^\infty(X)\) equal to one near \(K\), and extend \(w=\chi u\) by zero. Its periodization
\[
 p(x)=\sum_{\ell\in\mathbb Z}w(x-2\ell)
 \tag{L22}
\]
is smooth and two-periodic. The supports in different translates are disjoint and the sum is locally finite. On \(X\) only the term \(\ell=0\) can occur, so \(p=u\) near \(K\). For
\[
 c_k=\frac12\int_{-1}^{1}p(x)e^{-i\pi kx}\,dx,
 \tag{L23}
\]
integration by parts \(N\) times, with all periodic endpoint terms canceling, gives
\(|c_k|\leq C_N|k|^{-N}\) for \(k\ne0\).
For any fixed derivative order \(m\), choosing \(N>m+1\) makes the differentiated Fourier series absolutely and uniformly convergent. To identify its sum, use the period-two Fejér kernel
\[
 K_N(t)=\frac1{2(N+1)}
                 \left|\sum_{k=0}^N e^{i\pi kt}\right|^2.
 \tag{L24}
\]
It is nonnegative, and integrating its finite expansion on \([-1,1]\) gives integral one: unequal frequencies integrate to zero and the \(N+1\) diagonal terms each integrate to two. If \(\delta\leq|t|\leq1\), the finite geometric sum gives
\[
 K_N(t)\leq
       \frac1{2(N+1)\sin^2(\pi\delta/2)}.
 \tag{L25}
\]
Thus its mass outside any neighborhood of zero tends to zero. Splitting its convolution with the uniformly continuous periodic \(p\) at that neighborhood proves uniform convergence to \(p\). Expanding the same finite kernel shows these convolutions are the Cesàro means of the Fourier partial sums. The already absolutely convergent Fourier series has the same Cesàro limit as its ordinary sum, so that sum is \(p\). Uniform convergence of every differentiated series and the fundamental theorem of calculus identify the corresponding derivatives with those of \(p\). Fourier partial sums therefore approximate \(u\) with every prescribed finite collection of derivatives on \(K\).

## 5. Exercises and full solutions

The ten exercises total 100 points.

**Exercise 1 (10 points).** For \(\mu=\delta'_a\), derive all three identities in (L8), including the reflected symbol, and identify every polynomial-exponential homogeneous solution.

**Solution.** Since \(\partial_yu(x-y)=-u'(x-y)\), pairing with \(\delta'_a\) gives \(u'(x-a)\). Pairing with \(e^{-iy\zeta}\) gives \(i\zeta e^{-ia\zeta}\), and replacing \(\zeta\) by \(-\zeta\) gives \(-i\zeta e^{ia\zeta}\). A homogeneous \(f(x)e^{ix\lambda}\) has derivative zero everywhere, so it is constant. More explicitly, its derivative equation is \(f'+i\lambda f=0\). If \(\lambda\ne0\), the highest coefficient of a nonzero polynomial \(f\) cannot vanish in this equation. If \(\lambda=0\), \(f'=0\), so \(f\) is constant. The zero polynomial gives the zero solution at any frequency.

**Exercise 2 (10 points).** For the double difference in Example 2, prove the polynomial degree assertion and give the two transform conditions imposed on an annihilator at each characteristic frequency.

**Solution.** Taylor's finite expansion gives
\(f(x-a)=f(x)-a f'(x)+a^2f''(x)/2+\cdots\)
and
\(f(x-2a)=f(x)-2a f'(x)+2a^2f''(x)+\cdots\).
In \(f(x)-2f(x-a)+f(x-2a)\), the constant and first-derivative terms cancel and the second-derivative coefficient is \(a^2\). Higher derivatives have smaller degree. For degree \(d\geq2\), the leading coefficient is therefore \(a^2d(d-1)\) times the original one. The polynomial kernel has degree at most one.
Writing \(A=F_v\) and \(\zeta_k=2\pi k/a\), the conditions are \(A(\zeta_k)=A'(\zeta_k)=0\). Indeed \(A'(\zeta_k)=v(-ix e^{-ix\zeta_k})\), so annihilating both \(e^{-ix\zeta_k}\) and \(x e^{-ix\zeta_k}\) gives exactly those two zeros. All double zeros of \(B\) are then removable in \(A/B\), which is entire in one variable.

**Exercise 3 (8 points).** Compute \(X_\mu\) for Example 3, and verify both \(K_2\subset X_\mu\) and \(K_v\subset X\) with strict margins.

**Solution.** The three membership conditions are \((x_1,x_2)\in X\), \((x_1-2,x_2)\in X\), and \((x_1,x_2-1)\in X\). They give
\[
 x_1\in(-3,1)\cap(-1,3)=(-1,1),\qquad
 x_2\in(-2,1)\cap(-1,2)=(-1,1).
\]
Thus \(X_\mu=(-1,1)^2\). The rectangle has coordinate margins \(1/2\) and \(3/4\) inside it. The pentagon has coordinate ranges \([-5/2,1/2]\) and \([-5/4,1/4]\); their distances from the four sides of \(X\) are \(1/2,1/2,3/4,3/4\). Convexity includes every point between the listed vertices with the same coordinate bounds.

**Exercise 4 (8 points).** Let \(H_1(\eta)=2|\eta|\) and \(H_3(\eta)=|\eta|\) on the line. Show that their difference is not a support function. What does Theorem 3.1 rule out?

**Solution.** The difference is \(H_2(\eta)=-|\eta|\). Subadditivity would require
\(H_2(0)\leq H_2(1)+H_2(-1)\), which reads \(0\leq-2\). Thus it is not sublinear and cannot support a nonempty compact convex set. Although \(H_1\) and \(H_3\) individually support the intervals \([-2,2]\) and \([-1,1]\), no triple of proper PSH functions satisfying all hypotheses of Theorem 3.1 can have those indicators with \(p_3=p_1+p_2\). The sum hypothesis imposes an additional compatibility that arbitrary support functions need not have.

**Exercise 5 (10 points).** Recover the constant \(2^{2n+2}L\) in (3.10) from the growing-ball and double-submean estimates. Identify where the parameter-disk radius disappears.

**Solution.** On \(B(0,2\delta t)\), \(|H_j(\operatorname{Im}\zeta)|/t\leq2\delta\ell_j\). The growing-ball absolute-error bound has factor two, hence its upper limit is \(4\delta\ell_j|D|\). Sum the two errors to obtain \(4\delta L|D|\). The averaging ball centered at \(q\) has radius \(\delta t\), so replacing it by the containing ball increases the normalized bound by the volume ratio \(2^{2n}\). Division by the disk area cancels \(|D|\). The remaining Lipschitz error is \(La|y|\), which tends to zero as \(a\downarrow0\) after taking the upper limit. The resulting constant is \(2^{2n}4L=2^{2n+2}L\). The supremum on the left is independent of \(a\), so this last limit changes only the bound.

**Exercise 6 (8 points).** Explain why the quotient-growth proof translates the origin, and why the two original indicators remain unchanged.

**Solution.** A proper PSH function may equal minus infinity at the origin. In that case \(p_2(0)/t\) cannot give a finite seed excluding uniform collapse. Proper functions are finite almost everywhere, so choose one point \(z_*\) at which all three are finite. Their translated relation still holds. For \(j=1,3\), the new envelope is \(M_j(\eta+\operatorname{Im}z_*)\). Its difference from \(M_j(\eta)\) is bounded by the fixed quantity \(\ell_j|\operatorname{Im}z_*|\), using the envelope's Lipschitz bound. After setting \(\eta=ty\) and dividing by \(t\), the difference tends to zero. Thus the indicators are unchanged, while the scaled quotient has finite origin values tending to zero.

**Exercise 7 (10 points).** Suppose \(g\in C_c^\infty\) vanishes whenever \(\operatorname{dist}(x,K)<d\), with \(d>0\). Give a direct uniform complex Gaussian estimate near \(K\).

**Solution.** If \(\operatorname{dist}(\operatorname{Re}z,K)<d/4\), every point of \(\operatorname{supp}g\) is at least \(3d/4\) from \(\operatorname{Re}z\). If also \(|\operatorname{Im}z|<d/4\), (4.8) gives
\[
 |g_j(z)|\leq
 \left(\frac j\pi\right)^{n/2}\|g\|_1
 \exp\!\left[-j\left(\frac{9d^2}{16}-\frac{d^2}{16}\right)\right]
 =\left(\frac j\pi\right)^{n/2}\|g\|_1e^{-jd^2/2}.
\]
This tends to zero uniformly on that fixed complex neighborhood. The polynomial prefactor is dominated by the negative exponential. This direct estimate suffices for a zero germ; Lemma 4.1 proves the more general nonzero analytic-germ assertion too.

**Exercise 8 (8 points).** Verify the two exact vertical-side constants in the Gaussian diagram and compare them with the general contour estimate.

**Solution.** At \(w=2+is\), \(0\leq s\leq1/5\), the exponent per \(j\) is
\(-((2/5-2)^2-(1/5-s)^2)\leq-(64/25-1/25)=-63/25\).
At \(w=-2+is\), it is at most
\(-((2/5+2)^2-1/25)=-(144/25-1/25)=-143/25\).
Since \(63/25>15/16\) and \(143/25>15/16\), both bounds imply the weaker uniform bound \(-15/16\). On the shifted interval \(s=1/5\), the imaginary difference is zero and the exponent is exactly \(-(2/5-t)^2\).

**Exercise 9 (8 points).** Why does equality on the exponential tests in (5.12) imply equality on every entire test, and why is real smooth convergence alone insufficient for the later limit involving \(\sigma\)?

**Solution.** Exponentials have uniformly convergent power series and parameter derivatives on each bounded complex set. Differentiating the equality at frequency zero gives equality on every monomial with the same nonzero factor \((-i)^{|\alpha|}\), and therefore on every polynomial. The Taylor polynomials of an entire test converge uniformly on a larger polydisk; Cauchy estimates control all finite derivatives required by \(\mu\) and \(v\), and the analytic-functional bound controls \(\sigma\) on its complex neighborhood. These bounds pass polynomial equality to the entire test. For a subsequent smooth limit, \(\sigma\) is only known to be continuous on holomorphic germs with complex-neighborhood bounds. No real distributional finite-order bound is available. Uniform convergence on a fixed complex neighborhood, supplied by Lemma 4.1, is the required continuity input.

**Exercise 10 (20 points).** Explain why the cutoff in the density proof is taken equal to one near the whole \(K_v\) (10 points). Then show that convexity cannot simply be dropped by taking a derivative kernel on a disconnected open subset of the line (10 points).

**Solution.** Equation (5.9) gives
\[
 \operatorname{supp}v\subset K_v,\qquad
 K_2-\operatorname{supp}\mu\subset K_2+K_-=K_v.
\]
Thus one cutoff equal to one near \(K_v\) simultaneously preserves the pairing with \(v\) and every translated germ used by the convolution near \(K_2\). A cutoff known only on one translated piece would not justify both assertions. The entire convex hull is compact inside \(X\), so such a compact cutoff exists. A common margin from its plateau, together with compactness of the carrier and kernel support, makes \(\mu*(\chi u)=\mu*u=0\) in a neighborhood of \(K_2\).

For the second part take \(X=(-2,-1)\cup(1,2)\) and \(\mu=\delta'_0\). Then \(X_\mu=X\), and the equation is \(u'=0\) on each component. Let \(u=0\) on the first and \(u=1\) on the second. The only global polynomial-exponential homogeneous solutions are constants, by Exercise 1. At the two-point compact set \(\{-3/2,3/2\}\), every complex constant \(c\) has
\(\max\{|c|,|1-c|\}\geq1/2\), since \(1\leq|c|+|1-c|\).
No constants approximate \(u\) with arbitrarily small even zeroth-derivative error. This gives a concrete failure on a nonconvex open set without altering the convex theorem.

## References

- Gerd Grubb, *Fourier transformation of distributions*, lecture notes, Chapter 5. [Online reading](https://web.math.ku.dk/~grubb/dist5.pdf).
- Richard Melrose, *Introduction to Microlocal Analysis*, MIT lecture notes, revised 2007. Chapter 1, *Tempered distributions and the Fourier transform*. [Online reading](https://math.mit.edu/~rbm/iml/Chapter1.pdf).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition, Springer, 1990; 2003 reprint.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983; 2005 reprint.
