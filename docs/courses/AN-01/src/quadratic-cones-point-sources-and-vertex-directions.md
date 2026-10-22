# Quadratic cones, point sources and vertex directions

*Exposition and figure: GPT-6 Astra (OpenAI), October 2026. Original exposition: CC0. Supplied programme readings retain their stated credits and licences.*

A quadratic cone is smooth away from its vertex. There, its singular directions come from a one-dimensional boundary value. At the vertex a point source can force every direction to be singular, whereas a homogeneous equation permits only characteristic directions. The signature determines which of these two mechanisms governs a normalized one-sided power. More general holomorphic boundary values also admit moving smooth arguments, with a precise distinction between regular and critical limiting maps.

We use the complete boundary-power construction in [Complex powers at a boundary](complex-powers-at-a-boundary.md), Lemma 1.1, Proposition 1.2, Theorem 2.1, Proposition 3.1, Corollary 3.2 and Theorem 4.1. [Homogeneous extensions and angular moments](homogeneous-extensions-and-angular-moments.md), Theorems 1.2–3.1, constructs the angular representation and the unique continuous nonresonant extension. [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Theorem 1.1 and Lemma 2.1, proves the Laplacian source constants, symmetric diagonalization and the determinant branch. The parameter estimates and holomorphic identity argument are also developed in [Complex quadratic powers and the Cauchy kernel](complex-quadratic-powers-and-the-cauchy-kernel.md), Section 1.

The supplied [smooth pullback reading](../prerequisites/U011-free-foundations/smooth-pullback-and-fourier-normal-condition.md), Sections 18.1–18.5, proves ordinary wavefront localization, coordinate covariance and the exact submersion converse, especially (WF12)–(WF15). Its coordinate completion is [Regular level sets and transverse convolution](regular-level-sets-and-transverse-convolution.md), Lemma 0.2. [Cones and derivative-growth wavefronts](cones-and-derivative-growth-wavefronts.md), Theorem 6, proves \(\operatorname{WF}\subset\operatorname{WF}_A\); [Analytic equations and characteristic directions](analytic-equations-and-characteristic-directions.md), Theorem 3 and its preceding finite transpose construction, proves analytic regularity outside the characteristic set. The [Fourier](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), [Gamma](../prerequisites/U011-free-foundations/gamma-foundations-U016.md) and [angular](../prerequisites/U011-free-foundations/angular-foundations-U018.md) foundations supply the integrals, recurrence and sphere measure used below.

The first classifications use ordinary smooth wavefront. Theorem 11 proves the same sets at analytic regularity and in every derivative-growth class defined below. Fourier transformation uses \(e^{-ix\cdot\xi}\). Pairings are complex bilinear.

## Scalar directions and the two boundary signs

Write
\[
 b_\pm^\alpha(s)=(s\pm i0)^\alpha,\qquad
 \ell_\pm(s)=\log|s|\pm i\pi H(-s),\qquad
 \chi_-^\alpha(s)=\chi_+^\alpha(-s).
 \tag{Q1}
\]
Here \(\chi_+^\alpha\) is the entire normalized family initially equal to \(s_+^\alpha/\Gamma(\alpha+1)\). In particular \(\chi_+^0=H\) and \(\chi_+^{-k}=\delta_0^{(k-1)}\) for \(k\ge1\). The boundary-power reading proves these identities as distributions.

**Lemma 1 (scalar wavefronts).** For every real \(\alpha<0\),
\[
 \operatorname{WF}(b_\pm^\alpha)
   =\operatorname{WF}(\ell_\pm)
   =\{(0,\tau):\ \pm\tau>0\}.
 \tag{Q2}
\]
For every real \(\beta\),
\[
 \operatorname{WF}(\chi_+^\beta)
 =\operatorname{WF}(\chi_-^\beta)
 =\{(0,\tau):\tau\ne0\}.
 \tag{Q3}
\]

**Proof.** Corollary 3.2 of the boundary-power reading gives
\[
 \widehat b_+^\alpha(\eta)
   =\frac{2\pi e^{i\pi\alpha/2}}{\Gamma(-\alpha)}
      \boldsymbol1_{\{\eta>0\}}\eta^{-\alpha-1}.
\]
The exponent at zero is greater than \(-1\). For a compact smooth cutoff \(\rho\), the product-transform formula gives an absolutely convergent convolution with \(\widehat\rho\). If \(\xi<-1\), its absolute value is at most
\[
 C_M\int_0^\infty \eta^{-\alpha-1}
                 (1+|\xi|+\eta)^{-M}\,d\eta
 \le C'_M(1+|\xi|)^{-M-\alpha}.
\]
The last integral follows by \(\eta=(1+|\xi|)v\); it is finite for \(M>-\alpha\). Taking \(M\) arbitrarily large excludes every negative direction. The distribution is smooth away from zero. It is not smooth at zero, since on \(s>0\) it equals \(s^\alpha\), which is unbounded as \(s\downarrow0\). The ordinary wavefront projection theorem therefore supplies a direction at zero; conicity leaves exactly the positive ray. Complex conjugation gives the negative ray for \(b_-^\alpha\).

For the logarithm, choose \(\rho=1\) near zero. Theorem 4.1 of that reading gives
\[
 \partial_s(\rho\ell_+)=\rho b_+^{-1}+\rho'\ell_+ .
\]
The second term is smooth and compactly supported, since \(\rho'\) vanishes near zero. The first has rapid Fourier decrease on the negative ray by the preceding calculation. Fourier differentiation and division by \(i\xi\) there give the same decrease for \(\rho\ell_+\). Its unbounded logarithm at zero supplies the positive ray. Conjugation again gives the lower sign.

Each \(\chi_+^\beta\) is real, supported in \([0,\infty)\), smooth away from zero and nonzero. At a negative integer it is a nonzero delta derivative. At every other real parameter it has the nonzero density \(s^\beta/\Gamma(\beta+1)\) on \(s>0\). If it were smooth at zero, its vanishing on the negative side would force every Taylor coefficient there to vanish. Taylor's estimate of order \(N>\beta\), compared with that density as \(s\downarrow0\), is impossible. A nonzero delta derivative is also not smooth: a continuous function supported at a point is zero. Thus zero is its singular base point. For a real cutoff and a real distribution, the Fourier values in opposite directions are complex conjugates. Regularity in one ray is consequently equivalent to regularity in the other. Projection and conicity give both rays. Reflection proves the assertion for \(\chi_-^\beta\). \(\square\)

## Constructing the quadratic distributions through the vertex

Let \(n\ge2\), and let \(A=A^T\) be a nonsingular real \(n\times n\) matrix. Define
\[
 Q(x)=x^TAx,\qquad B(\xi)=\xi^TA^{-1}\xi,\qquad
 P_A=\sum_{j,k}(A^{-1})_{jk}\partial_j\partial_k,\qquad
 d_A=|\det A|^{1/2}.
 \tag{Q4}
\]
Let \((n_+,n_-)\) be its positive and negative eigenvalue counts; thus \(n_++n_-=n\). These counts include the definite cases. The differential \(dQ(x)=2Ax\) is nonzero whenever \(x\ne0\).

For \(n\ge3\) put \(\alpha=1-n/2\). On punctured space the submersion pullbacks \(Q^*b_\pm^\alpha\) and \(Q^*\chi_\pm^\alpha\) are defined. Their degree is \(2\alpha=2-n\): the pullback composition law and \(Q(tx)=t^2Q(x)\) give this scaling on tests. This degree is nonresonant and greater than \(-n\). Let \(U_\pm,V_\pm\) be their unique homogeneous extensions through zero. For \(n=2\) define instead
\[
 U_\pm=\log|Q|\pm i\pi H(-Q),\qquad
 V_+=H(Q),\quad V_-=H(-Q).
 \tag{Q5}
\]
These are locally integrable functions. Values on \(Q=0\) do not change them as distributions. The logarithm, rather than the constant power \(Q^0=1\), is the two-dimensional point-source expression.

**Lemma 2 (the actual boundary approach).** For \(n\ge3\),
\[
 (Q(x)\pm i\varepsilon|x|^2)^{1-n/2}
       \longrightarrow U_\pm
       \quad\hbox{in }\mathcal D'(\mathbb R^n)
       \quad(\varepsilon\downarrow0).
 \tag{Q6}
\]
For \(n=2\) the corresponding logarithms converge to the \(U_\pm\) in (Q5). All logarithms use argument in \((0,\pi)\) above the real axis and in \((-\pi,0)\) below it.

**Proof away from zero.** Complete \(s=Q(x)\) to smooth local coordinates \((s,y)\). In them the upper argument is \(z_\varepsilon=s+i\varepsilon h(s,y)\), with the positive smooth \(h=|x(s,y)|^2\). We give a direct argument for every negative integer or half-integer \(\alpha=1-n/2\).

If \(\alpha\) is not an integer, choose an integer \(N\) with \(\alpha+N>0\) and set
\[
 F(z)=\frac{z^{\alpha+N}}{(\alpha+1)\cdots(\alpha+N)}.
\]
Then \(F^{(N)}(z)=z^\alpha\), and \(F\) extends continuously across the boundary, including zero, from the upper half-plane. If \(\alpha=-k\), take \(N=k+1\) and
\[
 F(z)=\frac{z\operatorname{Log}z}{(-1)^{k-1}(k-1)!}.
\]
Differentiating \(z\operatorname{Log}z\) first gives \(\operatorname{Log}z+1\); the next \(k\) derivatives give \((-1)^{k-1}(k-1)!z^{-k}\). This \(F\) is again continuous at zero.

On a fixed compact chart and for small \(\varepsilon\), let
\[
 L_\varepsilon=(1+i\varepsilon\partial_s h)^{-1}\partial_s,
 \qquad
 L_\varepsilon^t\psi
     =-\partial_s\!\left(\frac{\psi}{1+i\varepsilon\partial_s h}\right).
\]
Repeated chain differentiation gives \(L_\varepsilon^N F(z_\varepsilon)=z_\varepsilon^\alpha\). Integration by parts therefore pairs the power against a test by pairing \(F(z_\varepsilon)\) against \((L_\varepsilon^t)^N\) of that test. The coordinate Jacobian is included in the test. The functions \(F(z_\varepsilon)\) converge uniformly on its compact support, while these transposed tests converge in every smooth seminorm to \((-\partial_s)^N\psi\). The limit is exactly \(b_+^\alpha\) applied in the \(s\) coordinate: the same calculation with \(h=1\) identifies its boundary trace. A finite partition covers every compact punctured support. Conjugation proves the lower case.

**Proof at the vertex.** For each fixed \(\varepsilon>0\), the power in (Q6) has absolute value bounded by \(C_\varepsilon |x|^{2-n}\), so it is locally integrable and homogeneous of degree \(2-n\) on the whole space. Its global value is thus the unique nonresonant extension of its punctured restriction. The weak continuity of that extension in the homogeneous-extension reading, Theorem 3.1, transports the proved punctured convergence to every test on \(\mathbb R^n\). No point-supported term is discarded.

For the logarithm write \(x=r\omega\) and \(a(\omega)=Q(\omega)\). The upper logarithm is
\[
 2\log r+\operatorname{Log}(a(\omega)+i\varepsilon).
\]
At a zero of \(a\) its tangential derivative on the sphere is \(2A\omega\), since \(Q(\omega)=0\); it is nonzero. Coordinate completion on the sphere therefore makes each such zero a regular \(s=0\) surface. In those charts \(1+|\log|a||\) is integrable, by \(\int_0^1|\log s|\,ds<\infty\); a finite cover handles the compact sphere. Where \(a\ne0\), it is bounded locally. For \(0<\varepsilon\le1\),
\[
 |\operatorname{Log}(a+i\varepsilon)|
      \le C+|\log|a||
\]
off the measure-zero set \(a=0\): its argument is bounded by \(\pi\), its positive real part is bounded on the compact sphere, and its negative real part is at most \(|\log|a||\). The radial bound \(\int_0^R r(1+|\log r|)\,dr<\infty\) now proves local integrability and dominated convergence to (Q5), using the full polar Jacobian. The definite case has no angular zeros and the same argument is simpler. Conjugation gives the lower limit. \(\square\)

## The exact source and its signature

Let \(\sigma_{n-1}=2\pi^{n/2}/\Gamma(n/2)\) be the sphere area, and put
\[
 c_n=\begin{cases}(2-n)\sigma_{n-1},&n\ge3,\\
 4\pi,&n=2.\end{cases}
\]

**Theorem 3 (quadratic boundary sources).** On the whole space,
\[
              P_AU_\pm
        =\frac{c_n}{d_A}e^{\mp i\pi n_-/2}\delta_0.
 \tag{Q7}
\]
In particular the coefficient is nonzero for every signature.

**Proof of the complex identity.** For a complex symmetric \(M\) with \(\operatorname{Re}M>0\), let \(g(M)\) be the determinant branch proved in the point-source reading, and let \(P_M\) use \(M^{-1}\) as in (Q4). We first establish
\[
 \begin{aligned}
 P_M(x^TMx)^{1-n/2}&=c_n g(M)^{-1}\delta_0 &&(n\ge3),\\
 P_M\operatorname{Log}(x^TMx)&=4\pi g(M)^{-1}\delta_0 &&(n=2).
 \end{aligned}
 \tag{Q8}
\]
For real positive \(M\), diagonalization supplies \(S=M^{1/2}\) and \(x^TMx=|Sx|^2\). The test-level linear chain rule gives \(P_M S^*f=S^*\Delta f\), while \(S^*\delta_0=|\det S|^{-1}\delta_0\). The point-source reading proves \(\Delta |x|^{2-n}=c_n\delta_0\) and \(\Delta\log|x|^2=4\pi\delta_0\). These prove (Q8) for all real positive \(M\).

Both sides paired with any compact test are holomorphic in the independent complex entries of \(M\). Here is the integrability justification. On a compact subset of the positive-real-part domain, \(|x^TMx|\ge c|x|^2\). Every parameter derivative of the power is bounded by a constant times \(|x|^{2-n}\), since each differentiating quadratic numerator cancels the degree of its additional denominator. This is locally integrable. For the logarithm the undifferentiated bound is \(C+2|\log|x||\); every positive parameter derivative is bounded. The adjugate formula gives holomorphic, locally bounded derivatives of \(M^{-1}\). Dominated difference quotients give coordinate holomorphy and joint continuity of the pairings; the polydisk proof in the complex-quadratic reading gives joint holomorphy.

In a small polydisk about \(I\), the paired difference in (Q8) vanishes when all entries are real and close to those of \(I\). Apply the one-variable identity principle successively to each independent entry, keeping the others real until their turn. The difference vanishes on that polydisk. The domain \(\operatorname{Re}M>0\) is convex. For any target \(M\), restriction to the complex parameter line \(I+z(M-I)\), on a connected neighborhood of the real segment \(0\le z\le1\), propagates this zero to \(M\). This proves (Q8) throughout the domain.

**Proof of the boundary constant.** Set \(M_\varepsilon=\varepsilon I-iA\). The determinant-branch lemma gives
\[
 M_\varepsilon^{-1}\longrightarrow iA^{-1},\qquad
 g(M_\varepsilon)^{-1}
   \longrightarrow d_A^{-1}e^{i\pi(n_+-n_-)/4}.
 \tag{Q9}
\]
For \(n\ge3\), with \(\alpha=1-n/2\), the branch relation is
\[
 (x^TM_\varepsilon x)^\alpha
   =e^{-i\pi\alpha/2}(Q+i\varepsilon|x|^2)^\alpha.
\]
Multiply (Q8) by \(e^{i\pi\alpha/2}\), and use Lemma 2 and coefficient convergence. The limit on the left is \(iP_AU_+\). Dividing by \(i\), the phase on the right is
\[
 \exp\!\left(i\pi\left[\frac{\alpha}{2}
             +\frac{n_+-n_-}{4}-\frac12\right]\right)
      =e^{-i\pi n_-/2}.
\]
Convergence with the varying differential operator is legitimate: each fixed derivative of the convergent distributions converges, and each matrix coefficient converges.

For \(n=2\), the logarithm relation has the additive constant \(-i\pi/2\). Its derivatives vanish, so the same limit of the second line of (Q8) gives the phase
\(\exp(i\pi[(n_+-n_-)/4-1/2])=e^{-i\pi n_-/2}\).
The real coefficients of \(P_A\) and complex conjugation give the lower sign in every dimension. \(\square\)

**Theorem 4 (one-sided source coefficients).** With the \(V_\pm\) defined above, for every \(n\ge2\),
\[
 \begin{aligned}
 P_AV_+&=\frac{4\pi^{(n-2)/2}}{d_A}
                         \sin(\pi n_+/2)\,\delta_0,\\
 P_AV_-&=-\frac{4\pi^{(n-2)/2}}{d_A}
                         \sin(\pi n_-/2)\,\delta_0 .
 \end{aligned}
 \tag{Q10}
\]
Thus the first coefficient is nonzero exactly when \(n_+\) is odd, and the second exactly when \(n_-\) is odd.

**Proof for \(n\ge3\).** At \(\alpha=1-n/2\) the scalar identities are
\[
 \begin{aligned}
 \chi_+^\alpha
  &=\frac{i\Gamma(-\alpha)}{2\pi}
       \left(e^{i\pi\alpha}b_-^\alpha
                       -e^{-i\pi\alpha}b_+^\alpha\right),\\
 \chi_-^\alpha
  &=\frac{i\Gamma(-\alpha)}{2\pi}
                         (b_+^\alpha-b_-^\alpha).
 \end{aligned}
 \tag{Q11}
\]
We verify all parameters needed here without assuming a reflection formula. At \(\alpha=-1/2\), the ordinary integrable boundary values on the two half-lines and \(\Gamma(1/2)=\sqrt\pi\) give
\(\chi_+^{-1/2}=(b_+^{-1/2}+b_-^{-1/2})/(2\sqrt\pi)\) and
\(\chi_-^{-1/2}=i(b_+^{-1/2}-b_-^{-1/2})/(2\sqrt\pi)\).
At \(\alpha=-1\), the proved jump \(b_+^{-1}-b_-^{-1}=-2\pi i\delta_0\) gives both identities. Differentiation gives
\[
 (\chi_+^\alpha)'=\chi_+^{\alpha-1},\quad
 (\chi_-^\alpha)'=-\chi_-^{\alpha-1},\quad
 (b_\pm^\alpha)'=\alpha b_\pm^{\alpha-1}.
\]
Together with \(\Gamma(1-\alpha)=-\alpha\Gamma(-\alpha)\) and
\(e^{\pm i\pi(\alpha-1)}=-e^{\pm i\pi\alpha}\), these prove (Q11) by induction down each of the two parameter sequences. Those sequences contain every \(1-n/2\), \(n\ge3\).

Pull back (Q11) on punctured space and extend homogeneously. Linearity and uniqueness of the degree-\((2-n)\) extension give the same identities with \(V_\pm,U_\pm\). Apply Theorem 3. For the positive side the difference of phases gives
\[
 -\frac{c_n\Gamma(n/2-1)}{\pi d_A}
       \sin\!\left(\pi(1-n/2)+\pi n_-/2\right).
\]
Gamma recurrence and the sphere constant give
\(c_n\Gamma(n/2-1)/\pi=-4\pi^{(n-2)/2}\);
the sine is \(\sin(\pi n_+/2)\). The second line of (Q11) gives
\(c_n\Gamma(n/2-1)\sin(\pi n_-/2)/(\pi d_A)\).
These are exactly (Q10).

**Proof for \(n=2\).** Formula (Q5) gives
\[
 V_-=\frac{U_+-U_-}{2\pi i},\qquad V_+=1-V_- .
\]
Theorem 3 consequently gives coefficients
\(-4d_A^{-1}\sin(\pi n_-/2)\) and its negative. Since \(n_+=2-n_-\),
\(\sin(\pi n_+/2)=\sin(\pi n_-/2)\), proving (Q10). \(\square\)

## Every wavefront covector, including the vertex

Use the following subsets of \(T^*\mathbb R^n\setminus0\):
\[
 \begin{aligned}
 \mathcal C_\pm&=\{(x,\tau\,dQ(x)):x\ne0,\ Q(x)=0,\ \pm\tau>0\},\\
 \mathcal C&=\{(x,\tau\,dQ(x)):x\ne0,\ Q(x)=0,\ \tau\ne0\},\\
 \mathcal V&=\{(0,\xi):\xi\ne0\},\\
 \mathcal N&=\{(0,\xi):\xi\ne0,\ B(\xi)=0\}.
 \end{aligned}
 \tag{Q12}
\]

**Theorem 5 (the full quadratic wavefronts).** For every nonsingular real symmetric \(A\) and every \(n\ge2\),
\[
 \begin{aligned}
 \operatorname{WF}(U_\pm)&=\mathcal C_\pm\cup\mathcal V,\\
 \operatorname{WF}(V_+)&=
    \mathcal C\cup
       \begin{cases}\mathcal V,&n_+\ \hbox{odd},\\
                     \mathcal N,&n_+\ \hbox{even},\end{cases}\\
 \operatorname{WF}(V_-)&=
    \mathcal C\cup
       \begin{cases}\mathcal V,&n_-\ \hbox{odd},\\
                     \mathcal N,&n_-\ \hbox{even}.\end{cases}
 \end{aligned}
 \tag{Q13}
\]
The first line uses the logarithmic \(U_\pm\) when \(n=2\). Empty quadratic cones and empty null fibers are allowed.

**Proof away from the vertex.** Since \(dQ\ne0\) there, the exact submersion wavefront equality (WF15) and Lemma 1 give precisely \(\mathcal C_\pm\) for \(U_\pm\) and \(\mathcal C\) for \(V_\pm\). These distributions are smooth where \(Q\ne0\). Thus no nonvertex covector has been omitted or added.

**Proof at a nonzero point source.** A finite constant-coefficient differential operator cannot enlarge ordinary wavefront. To recall the local argument, choose cutoffs inside a neighborhood on which a compact representative of \(u\) has rapid decay in a cone. Smooth localization gives that same decay, on a smaller cone, for every smooth compact multiplier there. The identity
\(\rho\,\partial_j u=\partial_j(\rho u)-(\partial_j\rho)u\)
then proves the derivative inclusion: its first term acquires only a Fourier polynomial, and the second is another localized multiplier. Iterate and take finite sums. Also every cutoff equal to one near zero leaves \(\widehat{\rho\delta_0}=1\). Hence
\[
 Pu=c\delta_0,\quad c\ne0
       \quad\Longrightarrow\quad
       \mathcal V\subset\operatorname{WF}(u).
 \tag{Q14}
\]
Theorem 3 applies this to each \(U_\pm\). The nonzero cases of Theorem 4 give the odd-signature cases for \(V_\pm\).

**Proof when the source vanishes.** In an even-signature case, Theorem 4 gives \(P_AV_\pm=0\) everywhere. The analytic differential regularity theorem applies to this constant-coefficient operator, whose symbol in the convention \(D=-i\partial\) is \(-B(\xi)\). It gives
\[
 \operatorname{WF}(V_\pm)\subset
 \operatorname{WF}_A(V_\pm)\subset\{(x,\xi):\xi\ne0,\ B(\xi)=0\}.
 \tag{Q15}
\]
This proves the required upper bound at zero, including when \(B\) is definite.

For the lower bound retain any \(\xi\ne0\) with \(B(\xi)=0\), and let
\[
 x_s=\frac{s}{2}A^{-1}\xi,\qquad s>0.
 \quad\text{Then}\quad
 Q(x_s)=\frac{s^2}{4}B(\xi)=0,\qquad dQ(x_s)=s\xi.
 \tag{Q16}
\]
Each \(x_s\ne0\), so the already proved full nonvertex conormal formula contains \((x_s,\xi)\), with multiplier \(1/s\). Ordinary wavefront is closed in the punctured cotangent bundle; its complement is open directly from the cutoff-and-cone definition. Letting \(s\downarrow0\), while retaining the same nonzero \(\xi\), gives \((0,\xi)\). This proves every point of \(\mathcal N\). Together with (Q15) it proves equality and completes all cases. \(\square\)

![A quadratic cone section and the full and null vertex-direction sections.](../figures/quadratic-vertex-directions.png)

*For \(Q(t,x,y)=t^2-x^2-y^2\), the left panel shows the base section \(y=0\) and the two normal signs at \((1,1,0)\); the displayed normal arrows are scaled copies of \((2,-2,0)\). The other panels show unit covectors in the section \(\xi_y=0\), not the whole three-dimensional fiber. The boundary values \(U_\pm\) and the positive-side \(V_+\) have every vertex direction. The negative-side \(V_-\) has exactly the null ones; in this section they are the four points \((\tau,\xi_x)=(\pm1/\sqrt2,\pm1/\sqrt2)\). Theorem 5 proves the complete sets. [Reproducible figure source](../figures/quadratic-vertex-directions.py).*

## Forward wave powers retain the whole vertex fiber

Let \(m\ge1\) be the spatial dimension, \(k\ge0\) an integer, \(c\ne0\) real, and \(s=|c|\). The full construction in [Causal point sources and characteristic cones](causal-point-sources-and-characteristic-cones.md), Lemma 4.0, and [Wave powers and complex potentials](wave-powers-and-complex-potentials.md), Theorem 1.1, supplies \(E_k\) with
\(\Box^{k+1}E_k=\delta_0\), \(\Box=\partial_t^2-\Delta_x\).
On \(t>0\),
\[
 E_k(t,x)=\frac{2^{-2k-1}\pi^{(1-m)/2}}{k!}
       \chi_+^{\,k+(1-m)/2}(t^2-|x|^2).
\]
Its global value and vertex source are already supplied by that construction.

**Corollary 6 (all forward wave powers and speeds).** Put
\[
 P_c=c^{-2}\partial_t^2-\Delta_x,\qquad
 E_{k,c}(t,x)=sE_k(st,x),\qquad q_c=c^2t^2-|x|^2.
\]
Then \(P_c^{k+1}E_{k,c}=\delta_0\), and
\[
 \operatorname{WF}(E_{k,c})
 =\{(t,x;\lambda\,dq_c(t,x)):t>0,\ q_c=0,\ \lambda\ne0\}
       \ \cup\ \{(0,0;\tau,\xi):(\tau,\xi)\ne0\}.
 \tag{Q17}
\]
The backward kernel obtained by \(t\mapsto-t\) has the same full vertex fiber and the corresponding \(t<0\) cone.

**Proof.** For \(T(t,x)=(st,x)\), the exact linear chain rule gives
\(P_cT^*u=T^*\Box u\), and \(T^*\delta_0=s^{-1}\delta_0\).
Iteration proves the displayed source identity, with the factor \(s\) retained for every \(k\). At each nonzero forward cone point, the local formula has a nonzero constant and the scalar family of Lemma 1. Its exact submersion pullback therefore has both conormal signs. Away from that cone and the vertex the kernel is smooth: its interior formula is a smooth power, or zero at a delta-derivative parameter, and it vanishes outside its supporting cone. Finally (Q14), applied to \(P_c^{k+1}\), gives every nonzero vertex covector. Coordinate covariance transports the cone differential to \(dq_c\). Time reflection has absolute determinant one, preserves the source and gives the backward statement. \(\square\)

## Boundary values along arbitrary smooth approaches

The boundary limit also survives a moving complex argument. The hypotheses concern its real limiting map and its convergence in the smooth topology; the height need not be proportional to the parameter, and the real part may move.

We use [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Theorem 3.1 and Corollary 3.2, for the horizontal boundary distribution on finite-regularity tests. [Gluing holomorphic sides](gluing-holomorphic-sides.md), Lemma 1.1, constructs an \(N\)-fold primitive with logarithmic growth. The exact submersion construction is the supplied smooth pullback reading, Section 18.5; its completed coordinates and Jacobian are supplied by the coordinate-completion lemma cited at the start of this lesson.

Let \(I\) be an open interval, let \(\gamma>0\), and set
\[
 Z=I+i(0,\gamma).
 \tag{A1}
\]
Let \(f\) be holomorphic on \(Z\). On each compact interval \(J\Subset I\), assume a bound
\[
 |f(s+it)|\le C_J t^{-N_J},
 \qquad s\in J,\quad 0<t<T_J,
 \tag{A2}
\]
where \(N_J\) is a nonnegative integer and \(T_J>0\). Larger compact intervals may require larger integers. These local bounds give the boundary distribution \(f_+=f(\,\cdot+i0)\).

**Lemma 7 (a continuous primitive at the boundary).** Locally near any compact subinterval, choose a slightly larger interval on which (A2) holds with exponent \(N\), and put \(m=N+1\). There is a holomorphic \(H\), continuous up to that real interval, such that
\[
 H^{(m)}=f,\qquad
 f_+=\partial_s^m H_0,\qquad H_0(s)=H(s).
 \tag{A3}
\]
In particular, this representation acts continuously on compact \(C^m\) tests.

**Proof.** The gluing lesson's Lemma 1.1 constructs a holomorphic \(G\) with \(G^{(N)}=f\) and
\[
 |G(s+it)|\le C\bigl(1+\log(T/t)\bigr),\qquad 0<t<T,
 \tag{A4}
\]
uniformly on each retained compact horizontal interval. For \(N=0\), take \(G=f\); its boundedness implies the displayed, weaker bound. Choose a reference point \(s_*\) and height \(T\) inside a slightly larger rectangle, and define
\[
 H(s+it)=\int_{s_*}^s G(r+iT)\,dr
                 +i\int_T^t G(s+ir)\,dr .
 \tag{A5}
\]
The fundamental theorem and \(G_t=iG_s\) give \(H_s=G\) and \(H_t=iG\), exactly as in that primitive construction. Thus \(H\) is holomorphic and \(H^{(m)}=f\).

The second integral in (A5) converges at \(t=0\), uniformly in the retained horizontal interval. Indeed,
\[
 \int_0^t \bigl(1+\log(T/r)\bigr)\,dr
          =t\bigl(2+\log(T/t)\bigr)\longrightarrow0.
 \tag{A6}
\]
The equality follows by integration of \(1+\log(T/r)\); the limit follows, for example, by writing \(t=Te^{-v}\) and comparing \(v e^{-v}\) with the exponential series. Hence \(H(s+it)\) converges uniformly to a continuous function \(H_0(s)\). Continuity of that limit and the same uniform estimate prove joint continuity at the real boundary.

For a compact \(C^m\) test \(\psi\), horizontal integration by parts gives
\[
 \int f(s+it)\psi(s)\,ds
       =(-1)^m\int H(s+it)\psi^{(m)}(s)\,ds
       \longrightarrow(-1)^m\int H_0(s)\psi^{(m)}(s)\,ds.
 \tag{A7}
\]
There are no end terms. The horizontal boundary theorem identifies the left limit with \(f_+(\psi)\). The right side is bounded by a compact-interval constant times \(\|\psi\|_{C^m}\). This proves (A3) and its stated test continuity. \(\square\)

**Theorem 8 (moving-map boundary limit).** Let \(X\subset\mathbb R^d\) be open, \(d\ge1\), and let \(g:X\to I\) be smooth with \(dg(x)\ne0\) everywhere. For each \(\varepsilon>0\), let \(F_\varepsilon:X\to Z\) be smooth and complex valued, with
\[
             F_\varepsilon\longrightarrow g
                     \quad\hbox{in }C^\infty_{\mathrm{loc}}(X).
 \tag{A8}
\]
Then
\[
               f(F_\varepsilon)\longrightarrow g^*f_+
                          \quad\hbox{in }\mathcal D'(X).
 \tag{A9}
\]
More precisely, on every fixed compact test support \(K\Subset X\), there are an integer \(m\), a constant \(C_K\), and numbers \(r_K(\varepsilon)\to0\) such that
\[
 \begin{aligned}
 |\langle f(F_\varepsilon)-g^*f_+,\phi\rangle|
       &\le r_K(\varepsilon)\|\phi\|_{C^m},\\
 |\langle f(F_\varepsilon),\phi\rangle|
       +|\langle g^*f_+,\phi\rangle|
       &\le C_K\|\phi\|_{C^m}
 \end{aligned}
 \tag{A10}
\]
for all sufficiently small \(\varepsilon\) and all smooth tests supported in \(K\). These pairings extend to compact \(C^m\) tests. Consequently the convergence is uniform on bounded sets of smooth tests, and permits moving tests converging in that fixed \(C^m\) norm. The corresponding statement holds for approaches from the lower half-plane and \(f_-\).

**Proof in completed coordinates.** Since \(dg\ne0\), complete \(s=g(x)\) to coordinates \((s,y)\) in a neighborhood of any point. Use a compactly supported local test and a slightly larger such chart. Replace \(F_\varepsilon\) by its expression in these coordinates; it converges to \(s\) in every smooth seminorm. The test becomes
\[
 \psi(s,y)=\phi(x(s,y))\,|\det D_{(s,y)}x|.
 \tag{A11}
\]
The absolute Jacobian is essential. It is smooth and positive on this chart. Every test derivative through any fixed order is bounded by a constant times the corresponding finite norm of \(\phi\), by the product and chain rules. Its support lies in one fixed compact set.

The real projections of \(F_\varepsilon\) of that compact set lie in one retained interval for small \(\varepsilon\), and their imaginary parts tend uniformly to zero from above. Choose the continuous primitive \(H\) of Lemma 7 on a larger rectangle, and write \(m=N+1\). On a neighborhood of the test support put
\[
 a_\varepsilon=(\partial_s F_\varepsilon)^{-1},\qquad
 L_\varepsilon=a_\varepsilon\partial_s,\qquad
 L_\varepsilon^t\psi=-\partial_s(a_\varepsilon\psi).
 \tag{A12}
\]
The denominator tends to \(1\) with every derivative, so it is nonzero there for small \(\varepsilon\), and \(a_\varepsilon\to1\) in every smooth seminorm. The transpose is bilinear: there is no complex conjugation of \(a_\varepsilon\).

The complex chain rule gives
\(L_\varepsilon(H^{(j)}(F_\varepsilon))=H^{(j+1)}(F_\varepsilon)\).
After \(m\) integrations by parts,
\[
 \int f(F_\varepsilon(s,y))\psi(s,y)\,ds\,dy
       =\int H(F_\varepsilon(s,y))
                     (L_\varepsilon^t)^m\psi(s,y)\,ds\,dy.
 \tag{A13}
\]
Only \(s\) is integrated by parts, and compact support removes each end term.

Here are estimates uniform in the test. Expanding the finite product of first-order operators gives
\[
 \begin{aligned}
 \|(L_\varepsilon^t)^m\psi\|_{L^1}
       &\le C\|\psi\|_{C^m},\\
 \|(L_\varepsilon^t)^m\psi-(-\partial_s)^m\psi\|_{L^1}
       &\le e_\varepsilon\|\psi\|_{C^m},\qquad e_\varepsilon\to0.
 \end{aligned}
 \tag{A14}
\]
To justify these expansions, start from
\(L_\varepsilon^t\psi=-a_\varepsilon\psi_s-(\partial_s a_\varepsilon)\psi\).
An induction writes its \(j\)-th power as a sum of derivatives \(\partial_s^k\psi\), \(k\le j\), with coefficients that are finite sums of products of derivatives of \(a_\varepsilon\) through order \(j\). Differentiating once and using the product rule proves the next step. All coefficients are uniformly bounded on the fixed support, and converge to those of \((-\partial_s)^j\), because \(a_\varepsilon\to1\) in \(C^j\). Multiplying their supremum bounds by the finite support volume proves (A14).

Uniform continuity of \(H\) on the relevant closed rectangle gives
\[
 \eta_\varepsilon
   =\sup_{\operatorname{supp}\psi}
       |H(F_\varepsilon(s,y))-H_0(s)|\longrightarrow0.
\]
Subtract \(\int H_0(s)(-\partial_s)^m\psi\,ds\,dy\) from (A13). Equations (A14) bound the difference by
\[
       \bigl(C\eta_\varepsilon+C'e_\varepsilon\bigr)
                      \|\psi\|_{C^m}.
 \tag{A15}
\]
The limit integral, by (A7) and integration in \(y\), is
\[
 \left\langle f_+,\,s\longmapsto\int\psi(s,y)\,dy\right\rangle .
 \tag{A16}
\]
This is precisely the previously constructed submersion pullback in completed coordinates, including its absolute density factor. No value of \(f\) on the real axis has been substituted into a singular expression.

**Localization and the test topology.** Cover \(K\) by finitely many such charts and use a fixed smooth partition. If their growth exponents differ, take the largest of their finite test orders. Each partition multiplier and coordinate change is continuous in that finite norm. Summing (A15) gives the first estimate in (A10); boundedness of \(H(F_\varepsilon)\), (A14), and the corresponding limit integral give the second. The submersion pullbacks agree on overlaps by their proved coordinate construction, so the limit is \(g^*f_+\) on all of \(X\).

The same formulas extend continuously to \(C^m\) tests with fixed support, by the supplied finite-norm smoothing approximation; equivalently one may integrate by parts directly for those tests. If \(\phi_\varepsilon\to\phi\) in \(C^m\) with common support, the common bound controls the pairing with \(\phi_\varepsilon-\phi\), and the fixed-test difference tends to zero by (A10). A bounded smooth test set has a common compact support and bounded \(C^m\) norm, so (A10) proves strong distributional convergence. For the lower side apply the upper theorem to \(h(z)=f(-z)\), the maps \(-F_\varepsilon\), and the submersion \(-g\). Reflection and the already proved pullback composition law identify the limit with \(g^*f_-\). \(\square\)

No estimate of the form \(\operatorname{Im}F_\varepsilon\ge c\varepsilon^q\) occurs in this proof. In particular, a jointly smooth map \(F(x,\varepsilon)\) with \(F(x,0)=g(x)\), nonzero \(dg\), and positive-height values satisfies (A8) on each compact set and therefore (A9). This includes arbitrary smooth real drift and heights flat at \(\varepsilon=0\).

**Corollary 9 (critical points over regular boundary values).** Retain the hypotheses on \(f\) and \(F_\varepsilon\), but allow \(dg=0\) at some points. Suppose that at every such point \(x_0\), \(f\) extends holomorphically to a complex neighborhood of \(g(x_0)\), agreeing with its original values above the interval. Then \(f(F_\varepsilon)\) still has a distributional limit. Near regular points it is the submersion pullback of Theorem 8; near each critical point it is the smooth function given by the holomorphic extension composed with \(g\).

**Proof.** Around a critical point, shrink the source neighborhood so that the image of its closure under \(g\) lies in a compact subset of the extension domain. For small \(\varepsilon\), its image under \(F_\varepsilon\) remains in that domain. Uniform continuity of each derivative of the extension on a slightly larger compact set, together with the finite chain rule and (A8), gives convergence in every smooth seminorm to the extension composed with \(g\). Around regular points Theorem 8 applies. On an overlap the local distributional limits coincide, since they are limits of the same functions against every test there. A finite partition on each compact support therefore defines the global limit, with the local finite-test estimates already proved. This argument asserts no pullback at a critical point lying over a singular boundary value. \(\square\)

![Moving approaches with a regular limiting coordinate, and concentration at a critical coordinate.](../figures/moving-boundary-and-critical-concentration.png)

*Left: the paths \(F_\varepsilon(s)=s+\varepsilon+i\varepsilon^2\), for \(s=-1/2,0,1/2\) and \(0\le\varepsilon\le0.4\), end at a real map with derivative one. Theorem 8 preserves the boundary distribution despite the real drift and changing height. Right: the exact profiles \(-\operatorname{Im}(x^2+i\varepsilon)^{-1}=\varepsilon/(x^4+\varepsilon^2)\), at \(\varepsilon=0.16,0.04,0.01\), have height \(\varepsilon^{-1}\) and a core width proportional to \(\sqrt\varepsilon\). Exercise 8 proves divergent mass near the critical point; the plotted samples are illustrations of that proof. [Reproducible figure source](../figures/moving-boundary-and-critical-concentration.py).*


## Analytic directions and every derivative-growth class

The scalar boundary signs also determine analytic directions. We use [Holomorphic boundaries and analytic directions](holomorphic-boundaries-and-analytic-directions.md), Lemma 1 and Theorem 2, for the proved polynomial-growth boundary estimate, and [Analytic pullback and cotangent directions](analytic-pullback-and-cotangent-directions.md), Theorems 4 and 6, for exact analytic coordinate and submersion covariance. The regularity comparisons and analytic-multiplier inclusion are [Cones and derivative-growth wavefronts](cones-and-derivative-growth-wavefronts.md), Theorems 6–7.

Fix any nondecreasing sequence \(L_0=1\), \(j\le L_j\), \(L_{j+1}\le C L_j\). These hypotheses are the derivative-growth convention of that reading. In particular they include \(L_j=(j+1)^s\), \(s\ge1\). Its comparison theorem gives
\[
 \operatorname{WF}(u)\subset\operatorname{WF}_L(u)
                       \subset\operatorname{WF}_A(u).
 \tag{B1}
\]
For the second inclusion, the analytic sequence \(j+1\) is at most \(2L_j\) for \(j\ge1\); the harmless constant is absorbed into the witness estimate.

**Lemma 10 (analytic scalar boundary signs).** Every equality in (Q2)–(Q3) holds with \(\operatorname{WF}\) replaced by \(\operatorname{WF}_A\), and also by \(\operatorname{WF}_L\).

**Proof.** For real \(\alpha<0\), choose the holomorphic branch \(z^\alpha=\exp(\alpha\operatorname{Log}z)\) in the upper half-plane, with argument between zero and \(\pi\). At \(z=s+it\), \(t>0\),
\[
 |z^\alpha|=|z|^\alpha\le t^\alpha.
 \tag{B2}
\]
On \(0<t<1\), this is bounded by \(t^{-m}\) for any integer \(m\ge-\alpha\). The boundary-power construction identifies its boundary as \(b_+^\alpha\). The dual of the positive imaginary ray is the nonnegative frequency ray in our Fourier convention. The cited boundary theorem therefore excludes all negative analytic directions.

The same theorem applies to the upper logarithm. On a bounded real interval and \(0<t<1\), its argument is bounded by \(\pi\), its positive logarithmic part is bounded, and its negative logarithmic part is at most \(|\log t|\). Consequently
\[
 |\operatorname{Log}(s+it)|\le C+|\log t|
                             \le C'(1+t^{-1}).
 \tag{B3}
\]
The last inequality follows, for example, from
\(-\log t=\int_t^1v^{-1}\,dv\le t^{-1}\).
The boundary is \(\ell_+\), by the earlier logarithmic limit. Thus it too has no negative analytic direction.

Both boundary functions are real analytic away from zero, including on the negative real half-line: near each nonzero real point their chosen branch has a holomorphic extension to a small disk avoiding zero. One can construct that local branch by the convergent logarithm series about the point, choosing its constant to match the upper value. The local analytic-function criterion therefore excludes every covector away from zero. Lemma 1 and (B1) force the positive ray at zero. This proves the upper-sign equalities. The lower branches satisfy the same polynomial bounds on the lower half-plane, whose imaginary cone has nonpositive dual; the same argument, with Lemma 1's lower ray, proves their equalities.

For every real \(\beta\), \(\chi_\pm^\beta\) is analytic on each open half-line. At a negative integer it is supported at zero; otherwise its nonzero half-line density is a constant multiple of \(\exp(\beta\log|s|)\), an analytic function there. Hence its analytic wavefront is contained in the full punctured fiber at zero. Lemma 1 and (B1) already include that whole fiber. Finally (B1) places every intermediate \(\operatorname{WF}_L\) between two equal sets in all these cases. \(\square\)

**Theorem 11 (the quadratic and causal classifications in every class).** For the distributions \(U_\pm,V_\pm\) of (Q4)–(Q5), all three sets
\(\operatorname{WF}\), \(\operatorname{WF}_L\) and \(\operatorname{WF}_A\)
are equal, with the exact values in (Q13). The same assertion holds for every forward or backward \(E_{k,c}\) in Corollary 6, with its exact set (Q17).

**Proof for quadratic distributions.** On punctured space \(Q\) is an analytic submersion. Lemma 10 and exact analytic submersion covariance give precisely \(\mathcal C_\pm\) for \(U_\pm\), and \(\mathcal C\) for \(V_\pm\). Where \(Q\ne0\) the local formulas are analytic, so these exhaust the nonvertex analytic directions.

At the vertex, each \(U_\pm\), and each odd-signature \(V_\pm\) specified in (Q13), already has the entire punctured smooth-wavefront fiber by the nonzero source identity. Inclusion (B1) gives the entire analytic fiber as well. A fiber has no additional nonzero covectors to include.

In the remaining signature cases \(P_AV_\pm=0\) on the whole space. The analytic differential regularity theorem used in (Q15) gives the analytic upper bound \(B(\xi)=0\). The exact path (Q16) and closedness already give every one of these covectors in smooth wavefront. Thus the analytic and smooth fibers agree here too. This argument includes definite forms, for which the nonzero null fiber is empty, and the logarithmic two-dimensional cases. It uses the whole-space source identity at zero, not a nonexistent submersion at that point.

**Proof for causal powers.** At a nonvertex forward cone point, \(t>0\) and \(dq_c\ne0\). The local formula in Corollary 6 is a nonzero scalar multiple of an analytic submersion pullback of \(\chi_+^\beta\), with \(\beta=k+(1-m)/2\). Lemma 10 gives both conormal signs exactly. In the cone interior the ordinary power is analytic; at negative integral parameters the scalar distribution vanishes there instead. Outside the cone the kernel is locally zero. Points with \(t=0\) other than the vertex also have a neighborhood disjoint from the supporting cone. Thus there are no other nonvertex analytic directions. At the vertex the equation \(P_c^{k+1}E_{k,c}=\delta_0\) supplies the full smooth fiber by (Q14), hence the full analytic fiber. Time reflection is an analytic diffeomorphism, so it proves the backward assertion. Finally (B1) gives every stated intermediate class. \(\square\)

The distinction between a homogeneous equation and a point-source equation remains essential at analytic regularity. Characteristic directions bound the former. The latter can have a full vertex fiber even when nonvertex conormals have only characteristic limits.

**Proposition 12 (analytic coordinates and nonvanishing weights).** Let \(\kappa:X\to Y\) be an analytic diffeomorphism, let \(a\) be a nowhere-zero complex-valued real analytic function on \(X\), and let \(u\) be any distribution in Theorem 11, restricted to \(Y\). Put \(v=a\,\kappa^*u\). Then
\[
 \operatorname{WF}(v)=\operatorname{WF}_L(v)=\operatorname{WF}_A(v)
 =\{(x,D\kappa(x)^T\eta):
                 (\kappa(x),\eta)\in\operatorname{WF}(u)\}.
 \tag{B4}
\]
**Proof.** Analytic diffeomorphism covariance gives equality for \(\operatorname{WF}_L\) and \(\operatorname{WF}_A\); the supplied smooth covariance gives it for \(\operatorname{WF}\). Multiplication by \(a\) gives inclusion for each class. Its reciprocal is real analytic locally: extend its power series holomorphically, shrink until it stays nonzero, and expand \(1/a\) by the geometric series about its value at the center. Multiplication by that reciprocal gives the reverse inclusion. For smooth wavefront the same reciprocal is smooth. Theorem 11 therefore gives (B4). No assertion about a weight at one of its zeros follows from this argument. \(\square\)

![An analytic bending of the forward wave cone and the full vertex covector circle.](../figures/analytic-curved-wave-cone.png)

*The left panel uses the analytic map \(\kappa(r,z)=(r,z+r^2)\). Its forward cone boundaries are \(z=\pm r-r^2\), \(r>0\). The displayed arrows are normalized samples of both signs of the exact covectors \(d[r^2-(z+r^2)^2]\); they represent covectors in these fixed Euclidean coordinates, not propagation velocities. At the origin, the right panel shows every unit covector. The four marked null directions are only the limits of nonvertex conormals. Exercises 10–11 prove the formulas and the strict distinction. [Vector figure](../figures/analytic-curved-wave-cone.svg) · [Reproducible figure source](../figures/analytic-curved-wave-cone.py).*


## Exercises with complete solutions

**Exercise 1 (foundation: the three-dimensional saddle).** Take \(Q=t^2-x^2-y^2\). Compute all four point-source coefficients and compare the vertex wavefronts of \(V_+\) and \(V_-\).

**Solution.** Here \(n=3\), \(d_A=1\), \((n_+,n_-)=(1,2)\), and \(P_A=\partial_t^2-\partial_x^2-\partial_y^2\). Since \(c_3=-4\pi\) and \(e^{\mp i\pi}=-1\),
\[
 P_AU_+=P_AU_-=4\pi\delta_0,\qquad
 P_AV_+=4\sqrt\pi\,\delta_0,\qquad P_AV_-=0.
\]
The normalized powers are the locally integrable functions
\(V_\pm=\boldsymbol1_{\{\pm Q>0\}}|Q|^{-1/2}/\sqrt\pi\).
Both have every nonzero conormal over each nonvertex cone point. At the vertex \(V_+\) has every nonzero covector, whereas \(V_-\) has exactly
\(\tau^2=\xi_x^2+\xi_y^2\), with the joint zero removed. Its nonzero interior values on \(Q<0\) do not introduce any wavefront there, since they are smooth. These are the sets displayed in the figure's sections. \(\square\)

**Exercise 2 (intermediate: a cone delta with no point source).** Let \(Q=x_1^2+x_2^2-x_3^2-x_4^2\). Identify \(V_+\) and \(V_-\), compute their source, and give their vertex wavefront.

**Solution.** Now \(\alpha=-1\), and both scalar families equal \(\delta_0\). Thus \(V_+=V_-\) is the unique degree-\((-2)\) extension of the punctured pullback \(\delta_0(Q)\). The notation specifies that extension; it is not an unsupported pullback at the critical point. The signature is \((2,2)\), so both sines in (Q10) vanish. Consequently \(P_AV_\pm=0\), with \(P_A=\partial_1^2+\partial_2^2-\partial_3^2-\partial_4^2\). The vertex fiber is precisely the nonzero set
\(\xi_1^2+\xi_2^2=\xi_3^2+\xi_4^2\).
The full wavefront also includes every nonzero multiple of \(dQ\) over every nonvertex cone point. In contrast, each \(U_\pm\) has source \(4\pi^2\delta_0\) and a full vertex fiber: \(c_4=-4\pi^2\), and its determinant phase is again \(-1\). Subtracting the two boundary-source equations agrees with the zero source of the delta term in their boundary jump. \(\square\)

**Exercise 3 (intermediate: verify the logarithmic source directly).** In two dimensions take \(Q=t^2-x^2\). Check the constants in Theorems 3–4 using characteristic coordinates.

**Solution.** Set \(u=t-x\), \(v=t+x\). Then \(Q=uv\), \(P_A=4\partial_u\partial_v\), and the coordinate determinant has absolute value two. Almost everywhere,
\[
 H(uv)=H(u)H(v)+H(-u)H(-v).
\]
Each mixed derivative on the right is \(\delta_0(u)\delta_0(v)\). Returning to \((t,x)\) gives
\(\delta_0(u)\delta_0(v)=\tfrac12\delta_{(0,0)}(t,x)\).
Therefore \(P_AH(Q)=4\delta_0\), and \(P_AH(-Q)=-4\delta_0\). Also
\(\log|uv|=\log|u|+\log|v|\) as locally integrable functions. Its mixed derivative is zero, since each summand is independent of one variable. Formula (Q5) hence gives
\[
 P_AU_+=-4\pi i\delta_0,\qquad P_AU_-=4\pi i\delta_0.
\]
These agree with \(n_-=1\) in (Q7). All four distributions have a full vertex wavefront. Away from the vertex, the logarithms have their respective single normal signs, while the Heaviside distributions have both signs. \(\square\)

**Exercise 4 (advanced: the definite cases are part of the theorem).** For \(Q=|x|^2\), determine \(V_\pm\) and their wavefronts in every \(n\ge2\).

**Solution.** The negative-side pullback is zero off the origin. Its unique homogeneous extension is zero for \(n\ge3\); for \(n=2\), \(H(-|x|^2)=0\) almost everywhere. Thus \(V_-=0\) in every case. For odd \(n\ge3\), the positive-side value is
\[
 V_+=\frac{|x|^{2-n}}{\Gamma(2-n/2)} .
\]
Its denominator is finite and nonzero, as follows from the half-integer Gamma recurrence. The coefficient in (Q10) is nonzero, and its wavefront is the full vertex fiber. For even \(n\ge4\), \(\alpha\) is a negative integer, so the scalar \(\chi_+^\alpha\) is supported at zero. Its pullback on punctured space is zero because \(Q>0\) there; uniqueness again gives \(V_+=0\). Finally \(n=2\) gives \(V_+=1\). All even-dimensional cases therefore have empty wavefront. This is exactly (Q13): the nonvertex cone and the nonzero null fiber are empty for a definite form. The logarithmic \(U_\pm\) in dimension two still have a point source and a full vertex fiber. \(\square\)

**Exercise 5 (advanced: retain an anisotropic determinant).** Let \(Q=4t^2-x^2-9y^2\). Compute the source coefficients, the dual null cone and the nonvertex normals.

**Solution.** The coordinate map \((t,x,y)\mapsto(2t,x,3y)\) has absolute determinant six. Thus \(d_A=6\), \((n_+,n_-)=(1,2)\), and
\[
 P_A=\tfrac14\partial_t^2-\partial_x^2-\tfrac19\partial_y^2,\qquad
 B(\tau,\xi,\eta)=\tfrac14\tau^2-\xi^2-\tfrac19\eta^2.
\]
Theorems 3–4 give
\[
 P_AU_\pm=\tfrac{2\pi}{3}\delta_0,\qquad
 P_AV_+=\tfrac{2\sqrt\pi}{3}\delta_0,\qquad P_AV_-=0.
\]
These are also the constants of Exercise 1 multiplied by \(1/6\), the pullback factor of a point mass. Nonvertex normals are multiples of
\(dQ=(8t,-2x,-18y)\) at \(Q=0\). The \(U_\pm\) retain respectively positive and negative multiples there and all vertex directions. The \(V_\pm\) retain both signs there; at zero \(V_+\) has every direction and \(V_-\) has precisely \(B=0\), with zero excluded. For every such nonzero covector, the exact path \(x_s=(s/2)A^{-1}(\tau,\xi,\eta)\) from (Q16) verifies the limiting lower inclusion without replacing \(A\) by an unrecorded normalized form. \(\square\)

**Exercise 6 (foundation: a height flatter than every power).** For \(\varepsilon>0\), set
\[
 F_\varepsilon(x)=x+\varepsilon\sin x
       +i e^{-1/\varepsilon^2}(2+\cos x).
 \tag{A17}
\]
Determine the distributional limit of \(1/F_\varepsilon(x)\). Determine also the limit when the sign of the imaginary part is reversed, and for the upper approach with limiting real map \(-x\).

**Solution.** The imaginary part in (A17) is positive. On each compact set every \(x\)-derivative of \(F_\varepsilon-x\) tends to zero; thus (A8) holds with \(g=x\). Theorem 8 and the previously proved pole limits give
\[
 \frac1{F_\varepsilon}\longrightarrow
       \operatorname{pv}\frac1x-i\pi\delta_0 .
 \tag{A18}
\]
For a fixed strip height \(\gamma\), the maps lie in that strip when \(3e^{-1/\varepsilon^2}<\gamma\). Reversing the imaginary sign gives
\(\operatorname{pv}(1/x)+i\pi\delta_0\).

The height has no positive lower bound by \(c\varepsilon^q\), for any fixed \(c>0\) and \(q\). Indeed, with \(v=1/\varepsilon\), the quantity \(v^q e^{-v^2}\) tends to zero: choose an integer \(k>q/2\) in \(e^{v^2}\ge v^{2k}/k!\). Defining the exponential factor to be zero at \(\varepsilon=0\) gives a smooth function there. Repeated differentiation for \(\varepsilon\ne0\) has the form a polynomial in \(\varepsilon^{-1}\) times \(e^{-1/\varepsilon^2}\); the same bound makes each derivative tend to zero, and the fundamental theorem successively identifies the extensions as derivatives at zero. Hence this is also a jointly smooth approach, with all height derivatives zero at the boundary.

For the upper approach
\(-x+\varepsilon\sin x+i e^{-1/\varepsilon^2}(2+\cos x)\),
the limiting map is reflection. The scalar identity
\(1/(-x+i\eta)=-1/(x-i\eta)\), \(\eta>0\), gives
\[
 (-\mathrm{id})^*(x+i0)^{-1}
       =-\operatorname{pv}\frac1x-i\pi\delta_0 .
 \tag{A19}
\]
The delta coefficient retains its sign because scalar distributional pullback uses the absolute Jacobian. The same result follows by reflection in Theorem 8. \(\square\)

**Exercise 7 (intermediate: two simple level zeros and one harmless critical point).** Let
\[
 F_\varepsilon(x)=x^2-1+\varepsilon\sin x
                         +i\varepsilon^3(2+\cos x),
 \qquad \varepsilon>0.
 \tag{A20}
\]
Find the distributional limit of \(1/F_\varepsilon\) on the whole real line, including \(x=0\) and the two roots of the limiting real map.

**Solution.** The maps approach \(g(x)=x^2-1\) in the smooth topology. Their positive heights are at most \(3\varepsilon^3\). The sole critical point of \(g\) is zero, whose image is \(-1\); the function \(f(z)=1/z\) is holomorphic near that image. Corollary 9 therefore applies at zero, giving the ordinary smooth limit \(1/(x^2-1)\) there. At each of the roots \(r=1,-1\), \(g'(r)=2r\ne0\), so Theorem 8 and the pole formula apply. They give
\[
 \begin{aligned}
 \frac1{F_\varepsilon}
 &\longrightarrow
 \frac12\left(\operatorname{pv}\frac1{x-1}
                     -\operatorname{pv}\frac1{x+1}\right)
       -\frac{i\pi}{2}(\delta_1+\delta_{-1}).
 \end{aligned}
 \tag{A21}
\]

Here are the real principal-value and density factors explicitly. The pulled-back delta has coefficient \(1/|g'(r)|=1/2\) at each root, by the one-dimensional change-of-variables test formula. The pulled-back principal value is the limit of
\(\int_{|g(x)|>\delta}\phi(x)/g(x)\,dx\).
To identify it, use
\[
 \frac1{x^2-1}=\frac12\left(\frac1{x-1}-\frac1{x+1}\right)
                       \qquad (x\ne\pm1).
\]
Near \(r\), write \(x=r+h\), so \(g(x)=h(2r+h)\). The endpoints removed by \(|g|\le\delta\) satisfy
\(h_\pm=\pm\delta/2+O(\delta^2)\).
This follows directly by solving the two quadratic equations, or by Taylor's formula for their local inverse, whose derivative has magnitude \(1/2\). Replacing these endpoints by the symmetric endpoints \(\pm\delta/2\) changes the singular integral by \(O(\delta)\): the endpoint differences have length \(O(\delta^2)\), and the integrand has size \(O(\delta^{-1})\) on those small intervals. The remaining local term is bounded. Thus the level-deletion limit is exactly the displayed combination of ordinary principal values. Away from the two roots it is the ordinary function. These local descriptions agree on overlaps and establish (A21) globally, without treating the critical point over \(-1\) as a singular level. \(\square\)

**Exercise 8 (advanced: concentration at a critical singular level).** Show that the smooth upper approach \(F_\varepsilon(x)=x^2+i\varepsilon\) does not give a distributional limit for \(f(z)=1/z\). Explain why this does not assert failure for every holomorphic \(f\) at every critical map.

**Solution.** Choose a nonnegative compact smooth test \(\phi\), equal to one on \([-a,a]\), \(a>0\). Direct algebra gives
\[
 -\operatorname{Im}\frac1{x^2+i\varepsilon}
              =\frac{\varepsilon}{x^4+\varepsilon^2}.
 \tag{A22}
\]
For \(0<\varepsilon<a^2\) and \(|x|\le\sqrt\varepsilon\), the denominator is at most \(2\varepsilon^2\). Hence
\[
 -\operatorname{Im}\left\langle
                 \frac1{x^2+i\varepsilon},\phi\right\rangle
       \ge \int_{-\sqrt\varepsilon}^{\sqrt\varepsilon}
                   \frac{dx}{2\varepsilon}
       =\varepsilon^{-1/2}\longrightarrow+\infty .
 \tag{A23}
\]
A distributional limit would have a finite limit on this one fixed test, so it cannot exist. Both the nonzero-derivative hypothesis of Theorem 8 and the holomorphic-extension condition at the critical image in Corollary 9 fail at zero. The figure shows the exact concentration profiles in (A22); the inequality above proves the divergence for every sufficiently small parameter, independently of those samples.

For contrast within this same calculation, \(f(z)=z\) has no singular boundary value: \(f(F_\varepsilon)=x^2+i\varepsilon\to x^2\) smoothly, although the limiting map remains critical at zero. Thus the submersion condition is sufficient for all the admitted boundary functions, and cannot simply be dropped for that entire class; it is not necessary for each individual regular function. \(\square\)


**Exercise 9 (foundation: a zero of an analytic weight).** For an integer \(k\ge1\), determine the smooth, analytic and derivative-growth wavefronts of \(s^k b_+^{-k}\). Explain the role of the nonvanishing assumption in Proposition 12.

**Solution.** The boundary-power construction gives \((s+it)^{-k}\to b_+^{-k}\) in distributions. On each compact test support these distributions have a common finite-order bound, by the boundary estimate. The multipliers \((s+it)^k\) tend to \(s^k\) with all derivatives there. Pairing the difference against a fixed test thus tends to zero by that common bound. Since the product before taking the limit is identically one,
\[
                  s^k b_+^{-k}=1.
 \tag{B5}
\]
This function is analytic and every one of its wavefronts is empty. In contrast, Lemma 10 gives the positive ray at zero for \(b_+^{-k}\) in all three classes. The analytic weight has a zero at exactly that base point; its reciprocal is unavailable there. Thus analytic multiplication always gives the inclusion, but need not give equality at a zero. \(\square\)

**Exercise 10 (intermediate: an analytic bending of a causal cone).** In one space dimension with speed one, let \(E_0(t,x)\) be the forward wave kernel of Corollary 6. For \(\kappa(r,z)=(r,z+r^2)\), compute all three wavefronts of
\[
                         v(r,z)=e^z\kappa^*E_0.
 \tag{B6}
\]
Give its locally integrable density and the exact covectors on its two curved boundary branches.

**Solution.** The inverse is \((t,x)\mapsto(t,x-t^2)\); both maps are polynomial and their Jacobian determinant is one. The causal formula for \(m=1,k=0\) is
\(E_0(t,x)=\tfrac12\boldsymbol1_{\{t\ge|x|\}}\) almost everywhere. Consequently
\[
 v(r,z)=\tfrac12e^z\boldsymbol1_{\{r\ge|z+r^2|\}},\qquad
 q(r,z)=r^2-(z+r^2)^2 .
 \tag{B7}
\]
The zero-measure boundary does not affect this locally integrable density. The weight is nowhere zero and analytic. Since
\[
 D\kappa(r,z)^T(\tau,\xi)=(\tau+2r\xi,\xi),\qquad
 dq=(2r-4r(z+r^2),-2(z+r^2)),
 \tag{B8}
\]
Proposition 12 gives the nonvertex pairs \((r,z;\lambda\,dq)\) with \(r>0\), \(z=\pm r-r^2\), \(\lambda\ne0\), together with the entire punctured fiber at \((0,0)\). There are no other pairs. On the branch \(z=\varepsilon r-r^2\), \(\varepsilon=\pm1\), the covector is
\[
                     dq=(2r-4\varepsilon r^2,-2\varepsilon r).
 \tag{B9}
\]
Its pairing with the tangent \((1,\varepsilon-2r)\) is zero. Both signs of every nonzero multiple occur. This proves the formulas displayed in the figure for smooth, analytic and every admitted derivative-growth wavefront. \(\square\)

**Exercise 11 (advanced: what closure of the punctured cone misses).** For the distribution in Exercise 10, determine the fiber at zero of the closure, in the punctured cotangent space, of its nonvertex conormal set. Compare it with the actual wavefront fiber.

**Solution.** Write the nonvertex covector on branch \(\varepsilon\) as
\[
       \lambda\,dq
           =2r\lambda(1-2\varepsilon r,-\varepsilon).
 \tag{B10}
\]
If these covectors tend to a finite nonzero \((\tau,\xi)\) as the base tends to zero, pass to one branch along a subsequence. The second component shows that \(2r\lambda\) has a finite limit \(b=-\varepsilon\xi\); the first then has limit \(b\). The limit is nonzero only if \(b\ne0\). Conversely, take \(\lambda=b/(2r)\) for any \(b\ne0\) and let \(r\downarrow0\). The resulting fiber is exactly
\[
             \{(\tau,\xi)\ne0:\tau^2=\xi^2\}.
 \tag{B11}
\]
It has four directions on the unit circle. The actual wavefront at zero, by Theorem 11 and (B4), is the whole punctured plane: the point source supplies the other directions. For example \((1,0)\) is in all three wavefronts and is absent from this conormal closure. Taking the closure is necessary to retain the limiting null covectors, but cannot replace the separate vertex argument. \(\square\)



## Fourier transforms on the dual quadratic cone

Throughout this section \(n\ge3\), \(\alpha=1-n/2\), and \(Q,B,P_A,d_A\) have the meanings in (Q4). Write \(p=n_+\), \(q=n_-\), so that \(p+q=n\). We use the positive constant
\[
 \kappa_n=(n-2)|S^{n-1}|=\frac{4\pi^{n/2}}{\Gamma(n/2-1)}=-c_n,
 \tag{F1}
\]
where \(c_n\) is the point-source constant in Theorem 3. The sphere and Gamma foundations prove the equality. The Fourier transform remains \(\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx\), with bilinear distributional transpose.

The passage to the boundary must control Schwartz tests at both zero and infinity. [Order, positivity and distributional limits](order-positivity-and-limits.md), Theorem 5.1, supplies a common finite order for a convergent sequence on a fixed compact test support. [Compact factors and homogeneous equations](compact-factors-and-homogeneous-equations.md), Proposition 3.1 and Theorem 3.2, supplies Fourier dilation and the annular construction of tempered extensions. The following estimate gives the particular continuity needed here.

**Lemma 13 (homogeneous limits on Schwartz tests).** Fix a real \(\lambda>-n\). Suppose that \(u_j\) are globally homogeneous distributions of degree \(\lambda\), and their restrictions to \(\mathbb R^n\setminus\{0\}\) converge in \(\mathcal D'\) to \(v\). Then \(v\) has a unique globally homogeneous extension \(u\) of that degree. Every \(u_j\) and \(u\) is tempered, and
\[
                 \langle u_j,\phi\rangle\longrightarrow
                 \langle u,\phi\rangle\qquad(\phi\in\mathcal S).
 \tag{F2}
\]
One finite Schwartz seminorm bounds all these distributions.

**Proof.** Passing the dilation identity to the limit on each compact test proves homogeneity of \(v\). Theorem 3.1 of the homogeneous-extension lesson gives its unique extension, since \(\lambda>-n\) is nonresonant. Choose a smooth cutoff \(\chi\), equal to one on the unit ball and zero outside the ball of radius two, and put \(\psi(x)=\chi(x)-\chi(2x)\). Its support lies in \(K=\{1/2\le |x|\le2\}\). Telescoping gives \(\sum_{l\in\mathbb Z}\psi(2^{-l}x)=1\) for \(x\ne0\). Homogeneity gives the annular identity
\[
 \langle w,\psi(2^{-l}\,\cdot)\phi\rangle
   =2^{l(n+\lambda)}\langle w,\psi(y)\phi(2^ly)\rangle
 \tag{F3}
\]
for any one of \(w=u_j,u\), initially on compact tests. These annular terms sum to \(w(\phi)\). Indeed the unsummed small ball has the form \(w(\chi(\cdot/\varepsilon)\phi)\), which equals
\(\varepsilon^{n+\lambda}w(\chi(y)\phi(\varepsilon y))\).
The finite-order bound for this fixed \(w\) on the ball of radius two makes the latter tend to zero. For a compact test the large-ball cutoff is eventually identically one on its support.

Apply Theorem 5.1 of the distributional-limits lesson on \(K\) to the convergent restrictions, including the limit. There are one order \(k\) and one constant \(C\) such that their absolute pairings with any test supported in \(K\) are at most \(C\|\cdot\|_{C^k}\). Define
\[
 p_{N,k}(\phi)=\max_{|\beta|\le k}\sup_x(1+|x|)^N|\partial^\beta\phi(x)|.
\]
Product differentiation in (F3) then gives
\[
 |\text{term}_l|\le
 \begin{cases}
 C'2^{l(n+\lambda)}p_{0,k}(\phi),&l\le0,\\
 C'_N2^{l(n+\lambda+k-N)}p_{N,k}(\phi),&l\ge0.
 \end{cases}
 \tag{F4}
\]
For the second inequality \(1+|2^ly|\ge2^{l-1}\) on \(K\); each derivative on the rescaled test contributes at most \(2^{lk}\). For the first all such factors are at most one. Choose an integer \(N>n+\lambda+k\). Both geometric tails are summable, uniformly in \(j\). Thus the annular series defines a continuous functional on \(\mathcal S\), agreeing with \(w\) on compact tests and bounded by \(C''p_{N,k}\). Compact-test density in \(\mathcal S\), proved in the Fourier foundations, gives uniqueness. For each fixed \(l\) the compact annular pairing converges. First make both uniform tails small and then pass to the limit in the finite middle sum. This proves (F2). \(\square\)

Let \(U_\pm\) and \(V_\pm\) denote the quadratic distributions already constructed, respectively from \(b_\pm^\alpha\) and \(\chi_\pm^\alpha\). On the punctured frequency space \(dB(\xi)=2A^{-1}\xi\ne0\). Define
\[
 W_\pm=\operatorname{Ext}_{-2}\bigl(B^*(s\pm i0)^{-1}\bigr).
 \tag{F5}
\]
These extensions are unique because \(-2>-n\). Their restrictions are homogeneous of degree \(-2\) by the scalar boundary law and the quadratic dilation. Lemma 13, or the annular tempered-extension theorem, makes them tempered on the whole frequency space.

**Theorem 14 (both quadratic boundary transforms).** For every real nonsingular symmetric \(A\) in dimension \(n\ge3\),
\[
 \boxed{\quad\widehat U_\pm
       =\frac{\kappa_n}{d_A}e^{\mp i\pi q/2}W_\mp.\quad}
 \tag{F6}
\]
The identity holds on all Schwartz tests, including tests meeting the vertex of the dual cone.

**Proof.** Set \(M_\varepsilon=\varepsilon I-iA\), \(\varepsilon>0\). Its real part is positive definite. Theorem 1.2 of [Complex quadratic powers and the Cauchy kernel](complex-quadratic-powers-and-the-cauchy-kernel.md), with its exponent \(a=n-2\in(0,n)\), gives the whole-space identity
\[
 \mathcal F\bigl[(x^TM_\varepsilon x)^\alpha\bigr]
 =\kappa_n g(M_\varepsilon)^{-1}
                  (\xi^TM_\varepsilon^{-1}\xi)^{-1}.
 \tag{F7}
\]
Here \(g\) is the canonical square root of the determinant, positive on positive definite real matrices. The cited theorem proves the two absolute integration interchanges on Schwartz tests, so (F7) includes frequency zero.

Put \(B_\varepsilon(\xi)=\xi^T(A+i\varepsilon I)^{-1}\xi\). Since \(M_\varepsilon=-i(A+i\varepsilon I)\), its inverse quadratic is \(iB_\varepsilon\). In a real orthogonal eigenbasis of \(A\), with nonzero eigenvalues \(a_j\),
\[
 \operatorname{Im}B_\varepsilon(\xi)
      =-\varepsilon\sum_j\frac{(\xi'_j)^2}{a_j^2+\varepsilon^2}<0
                          \quad(\xi\ne0).
 \tag{F8}
\]
Also \(B_\varepsilon\to B\) in every smooth seminorm on compact sets. The lower-half-plane version of Theorem 8, applied to \(f(z)=1/z\) and the submersion \(B\), proves
\(B_\varepsilon^{-1}\to B^*(s-i0)^{-1}\) on the punctured space. Each reciprocal is a locally integrable global homogeneous function of degree \(-2\): for fixed \(\varepsilon\), (F8) bounds its absolute value by \(C_\varepsilon|\xi|^{-2}\). Lemma 13 upgrades this to convergence to \(W_-\) on Schwartz tests. Formally, apply that lemma along every sequence \(\varepsilon_j\downarrow0\); failure of any scalar test limit would supply a sequence contradicting the lemma.

On the physical side, the principal argument of \(Q+i\varepsilon|x|^2\) lies in \((0,\pi)\) when \(x\ne0\). Multiplication by \(-i\) subtracts \(\pi/2\) without crossing the branch cut, so
\[
 (x^TM_\varepsilon x)^\alpha
    =e^{-i\pi\alpha/2}(Q+i\varepsilon|x|^2)^\alpha.
 \tag{F9}
\]
For fixed \(\varepsilon\) these functions are locally integrable, homogeneous of degree \(2-n>-n\). Lemma 2 and Lemma 13 give the Schwartz-test limit \(e^{-i\pi\alpha/2}U_+\). The determinant branch proved in Lemma 2.1 of the Gaussian lesson gives
\[
 g(M_\varepsilon)^{-1}\longrightarrow
             d_A^{-1}e^{i\pi(p-q)/4}.
 \tag{F10}
\]
Taking (F7) to the limit is legitimate because the Fourier transform maps each Schwartz test to a Schwartz test. Since \((iB_\varepsilon)^{-1}=-iB_\varepsilon^{-1}\), the total phase after solving for \(\widehat U_+\) is
\[
 e^{i\pi\alpha/2}(-i)e^{i\pi(p-q)/4}
                  =e^{-i\pi q/2},
 \tag{F11}
\]
using \(\alpha=1-(p+q)/2\). This proves the upper sign. Complex conjugation satisfies
\(\mathcal F(\overline u)(\xi)=\overline{\widehat u(-\xi)}\), by the test-transform definition. Each quadratic distribution is even: reflection preserves its punctured definition and homogeneity, hence preserves the unique extension. Moreover \(\overline{U_+}=U_-\) and \(\overline{W_-}=W_+\), first off the vertex and then by uniqueness. Conjugating the upper identity with the required reflection proves the lower one. \(\square\)

## Principal values and the measure on the dual cone

**Theorem 15 (one-sided powers and cone mass).** Define the canonical homogeneous distributions
\[
 R_B=\tfrac12(W_++W_-),\qquad
 \Delta_B=\frac{W_--W_+}{2\pi i}.
 \tag{F12}
\]
On the punctured space these are respectively the submersion pullbacks of \(\operatorname{pv}(1/s)\) and \(\delta_0(s)\). On the whole space,
\[
 BR_B=1,\qquad B\Delta_B=0,
 \tag{F13}
\]
and the normalized one-sided powers have transforms
\[
 \begin{aligned}
 \widehat V_+
  &=\frac{2\pi^{(n-2)/2}}{d_A}
       \left(i e^{i\pi p/2}W_- -i e^{-i\pi p/2}W_+\right)\\
  &=-\frac{4\pi^{(n-2)/2}}{d_A}
       \left(\sin(\pi p/2)R_B+\pi\cos(\pi p/2)\Delta_B\right),\\
 \widehat V_-
  &=\frac{2\pi^{(n-2)/2}}{d_A}
       \left(i e^{-i\pi q/2}W_- -i e^{i\pi q/2}W_+\right)\\
  &=\frac{4\pi^{(n-2)/2}}{d_A}
       \left(\sin(\pi q/2)R_B-\pi\cos(\pi q/2)\Delta_B\right).
 \end{aligned}
 \tag{F14}
\]
The distribution \(\Delta_B\) is a positive locally finite tempered measure. Writing \(b(\omega)=B(\omega)\) on the unit sphere and \(\Sigma=\{\omega:b(\omega)=0\}\), it is given by
\[
 \langle\Delta_B,\phi\rangle
  =\int_0^\infty r^{n-3}
        \int_\Sigma\frac{\phi(r\omega)}{|\nabla_S b(\omega)|}
                              \,dS_\Sigma(\omega)\,dr.
 \tag{F15}
\]
If \(A\) is definite, this measure is zero. If \(A\) is indefinite, its support is the entire dual null cone \(\{B=0\}\), including its vertex.

**Proof of the transform identities.** The scalar boundary formula
\((s\pm i0)^{-1}=\operatorname{pv}(1/s)\mp i\pi\delta_0\), proved in the boundary-power lesson, proves (F12) off zero. There it also gives (F13), since \(s\operatorname{pv}(1/s)=1\) and \(s\delta_0=0\). The two sides of each identity are homogeneous of degree zero. The uniqueness of nonresonant extension from the punctured space proves their equality globally; it excludes an additional point-supported term.

Equation (Q11), whose scalar identities are proved in Theorem 4, gives
\[
 V_+=\frac{i\Gamma(-\alpha)}{2\pi}
             (e^{i\pi\alpha}U_- -e^{-i\pi\alpha}U_+),\qquad
 V_-=\frac{i\Gamma(-\alpha)}{2\pi}(U_+-U_-).
 \tag{F16}
\]
Use (F6), \(\Gamma(-\alpha)\kappa_n/(2\pi)=2\pi^{(n-2)/2}\), and \(p+q=n\). In the first identity the coefficient of \(W_-\) is
\(-i e^{-i\pi\alpha-i\pi q/2}=i e^{i\pi p/2}\);
the coefficient of \(W_+\) is
\(i e^{i\pi\alpha+i\pi q/2}=-i e^{-i\pi p/2}\).
The second identity gives the corresponding phases with \(q\) directly. Finally substitute \(W_-=R_B+i\pi\Delta_B\) and \(W_+=R_B-i\pi\Delta_B\); \(e^{i\theta}-e^{-i\theta}=2i\sin\theta\) and \(e^{i\theta}+e^{-i\theta}=2\cos\theta\) give the real forms in (F14).

**Proof of the measure formula.** On \(\Sigma\) the spherical gradient is \(\nabla_S b=2A^{-1}\omega\), because its radial component is \(2B(\omega)=0\). It never vanishes. Theorem 1.1 of [Regular level sets and transverse convolution](regular-level-sets-and-transverse-convolution.md) gives the density \(dS/|\nabla B|\) on the punctured cone. To express that density radially, take a local parametrization \(\omega=\gamma(y)\) of \(\Sigma\). The cone chart is \((r,y)\mapsto r\gamma(y)\). Since \(|\gamma|=1\), differentiating this identity gives \(\gamma\cdot\partial_{y_j}\gamma=0\). Its Gram matrix is therefore block diagonal, with radial entry \(1\) and angular block \(r^2D\gamma^TD\gamma\). The surface density is \(r^{n-2}dr\,dS_\Sigma\), while \(|\nabla B(r\omega)|=r|\nabla_Sb(\omega)|\). Division gives (F15), by the exact surface-coordinate change formula of that theorem and a finite chart partition. This computation is in regular coordinates away from zero; it does not assert a submersion pullback at the vertex.

The compact regular hypersurface \(\Sigma\) has finite induced measure, by a finite smooth graph cover and the surface integration formula. Its gradient norm has a positive minimum. Consequently (F15) is bounded near zero by \(C\|\phi\|_\infty\int_0^1r^{n-3}dr<\infty\). At infinity a Schwartz seminorm with exponent \(N>n-2\) bounds the integral by \(C p_{N,0}(\phi)\int_1^\infty r^{n-3-N}dr\). Thus it defines a positive tempered measure on the whole space. A radial substitution proves degree \(-2\), and uniqueness identifies it with \(\Delta_B\). If \(A\) is definite then \(\Sigma\) is empty. Otherwise eigenvectors of both signs give a nonzero null vector by balancing their squared coefficients, so \(\Sigma\ne\varnothing\). The positive smooth density has support all of \(\Sigma\), and radial integration gives every nonzero point of the null cone. Every neighborhood of the vertex contains such points with positive measure. This proves the support assertion. \(\square\)

For an indefinite form, (F14) has a useful parity interpretation. If \(p\) is odd, \(\widehat V_+\) is a nonzero multiple of \(R_B\), of support all of \(\mathbb R^n\). If \(p\) is even, it is a nonzero multiple of \(\Delta_B\), of support exactly the dual cone. The same assertion holds for \(V_-\) with \(q\). To check the full support of \(R_B\), every nonempty open set meets \(\{B\ne0\}\): a nonzero polynomial cannot vanish on an open ball, by its finite Taylor expansion. On that set \(R_B=1/B\ne0\), which a sufficiently small test of constant sign detects. Both spectral alternatives therefore have exactly the stated supports.

**Corollary 16 (normalized fundamental solutions).** Put
\[
 E_\pm=\frac{d_A}{c_n}e^{\pm i\pi q/2}U_\pm.
 \tag{F17}
\]
Then \(P_AE_\pm=\delta_0\), and
\[
 \widehat E_\pm=-W_\mp,\qquad
 \mathcal F\bigl((E_++E_-)/2\bigr)=-R_B,\qquad
 \mathcal F(E_+-E_-)=-2\pi i\Delta_B.
 \tag{F18}
\]
The difference is a solution of \(P_Au=0\). It vanishes precisely when \(A\) is definite.

**Proof.** Theorem 3 and (F17) give the point source. Equation (F6) and \(c_n=-\kappa_n\) give the first transform in (F18), and (F12) gives the other two. Fourier differentiation gives the multiplier \(-B\) for \(P_A\); (F13) also verifies both the source and the homogeneous equation in frequency space. Fourier injectivity from the supplied inversion theorem, together with the zero and nonzero alternatives for \(\Delta_B\), proves the last assertion. \(\square\)

These boundary choices do not select a direction of physical time. Both \(E_\pm\) are even under simultaneous reflection of all physical coordinates. A causal fundamental solution requires its separate support condition, as in the earlier causal constructions.

![Both sheets of the three-dimensional dual null cone and its exact Gaussian radial density](../figures/quadratic-dual-cone-and-gaussian-mass.png)

**Figure.** For \(B(\tau,\xi,\eta)=\tau^2-\xi^2-\eta^2\), the left panel displays both sheets \(\tau=\pm r\), \((\xi,\eta)=(r\cos\theta,r\sin\theta)\), truncated at \(r=2\). The right panel shows the exact radial densities \(2\pi e^{-2br^2}\) of the Gaussian-weighted cone measure for three positive \(b\). Here \(r\) is the spatial radius and the Euclidean radius on the cone is \(\sqrt2r\). The support is proved in Theorem 15; the density and its integral are proved in Exercise 17. [Reproducible figure source](../figures/quadratic-dual-cone-and-gaussian-mass.py).

## Exercises on quadratic Fourier transforms

**Exercise 12 (basic: a three-dimensional saddle).** Let \(Q(t,x,y)=t^2-x^2-y^2\). Compute the transforms of \(U_\pm,V_\pm\) and recover the two point-source equations for \(V_\pm\) by Fourier differentiation.

**Solution.** Here \(p=1,q=2,d_A=1\), \(\kappa_3=4\pi\), and \(B(\tau,\xi,\eta)=\tau^2-\xi^2-\eta^2\). Equations (F6) and (F14) give
\[
 \widehat U_\pm=-4\pi W_\mp,\qquad
 \widehat V_+=-4\sqrt\pi R_B,\qquad
 \widehat V_-=4\pi^{3/2}\Delta_B.
 \tag{F19}
\]
The Fourier multiplier of \(P_A=\partial_t^2-\partial_x^2-\partial_y^2\) is \(-B\). By (F13), multiplication of the last two expressions by \(-B\) gives \(4\sqrt\pi\) and zero, respectively. Since \(\widehat{\delta_0}=1\) and the transform is injective, \(P_AV_+=4\sqrt\pi\delta_0\) and \(P_AV_-=0\). Thus a nonzero physical one-sided power can have its whole Fourier transform on the dual cone.

**Exercise 13 (intermediate: the split four-dimensional cone).** Let \(Q=x_1^2+x_2^2-x_3^2-x_4^2\). Interpret \(\delta_0(Q)\) through its vertex and calculate its Fourier transform. Check the result by applying the transform twice.

**Solution.** The vertex interpretation is the unique degree-\(-2\) homogeneous extension of the regular-level measure off zero. Formula (F15), now on the physical space, makes it a locally finite positive measure. Here \(\alpha=-1\), so \(\chi_+^{-1}=\delta_0=\chi_-^{-1}\); hence \(V_+=V_-=\delta_0(Q)\). Since \(p=q=2,d_A=1\), and \(B\) has the same expression in frequency coordinates, (F14) gives
\[
                    \mathcal F[\delta_0(Q)]=4\pi^2\delta_0(B).
 \tag{F20}
\]
Applying the same formula again gives \(16\pi^4\delta_0(Q)=(2\pi)^4\delta_0(Q)\). This agrees with \(\mathcal F^2=(2\pi)^4\mathcal R\), since the measure is even. No unspecified vertex mass is compatible with its degree.

**Exercise 14 (intermediate: anisotropic constants).** Take \(A=\operatorname{diag}(4,-1,-9)\) in dimension three. Compute the transforms and then express them using \(\widetilde B=9\tau^2-36\xi^2-4\eta^2\).

**Solution.** Now \(d_A=6,p=1,q=2\) and \(B=\tau^2/4-\xi^2-\eta^2/9=\widetilde B/36\). Therefore
\[
 \widehat U_\pm=-\frac{2\pi}{3}W_\mp^B,\qquad
 \widehat V_+=-\frac{2\sqrt\pi}{3}R_B,\qquad
 \widehat V_-=\frac{2\pi^{3/2}}3\Delta_B.
 \tag{F21}
\]
The scalar positive-rescaling laws for the pole, principal value and delta give \(W_\pm^B=36W_\pm^{\widetilde B}\), \(R_B=36R_{\widetilde B}\) and \(\Delta_B=36\Delta_{\widetilde B}\), first off zero and then by homogeneous uniqueness. Thus the three coefficients in (F21), in terms of \(\widetilde B\), become \(-24\pi\), \(-24\sqrt\pi\) and \(24\pi^{3/2}\). Both the determinant factor and the pole rescaling are needed.

**Exercise 15 (basic: definite signatures).** Compute the boundary and one-sided transforms for \(A=-I\) in dimension three and for \(A=I\) in dimension four. Explain the absence of cone mass.

**Solution.** For \(n=3,A=-I\), \(Q=-|x|^2\), \(B=-|\xi|^2\), and the principal arguments give \(U_+=-i|x|^{-1}\), \(U_-=i|x|^{-1}\). Also \(V_+=0\) and \(V_-=|x|^{-1}/\sqrt\pi\). Because \(W_+=W_-=-|\xi|^{-2}\), (F6) and (F14) give
\[
 \widehat U_+=-4\pi i|\xi|^{-2},\qquad
 \widehat U_-=4\pi i|\xi|^{-2},\qquad
 \widehat V_-=4\sqrt\pi|\xi|^{-2}.
 \tag{F22}
\]
For \(n=4,A=I\), \(U_\pm=|x|^{-2}\) and \(\widehat U_\pm=4\pi^2|\xi|^{-2}\). Both \(V_\pm\) vanish: their punctured definitions pull back \(\delta_0\) along the strictly positive \(Q\), hence are zero, and degree \(-2\) has a unique extension. In each case the spherical zero set is empty, so (F15) gives \(\Delta_B=0\); no atom at zero has the required degree.

**Exercise 16 (advanced: a homogeneous difference of fundamental solutions).** In the saddle of Exercise 12, find \(E_+-E_-\) as a locally integrable function and compute the inverse transform of \(\Delta_B\). Decide whether the difference has one-sided time support.

**Solution.** Here \(c_3=-4\pi\) and \(e^{\pm i\pi q/2}=-1\), so \(E_\pm=U_\pm/(4\pi)\). The upper and lower square-root powers agree on \(Q>0\) and have values \(-i/\sqrt{-Q}\) and \(i/\sqrt{-Q}\) on \(Q<0\). Thus
\[
 E_+-E_-=-\frac{i}{2\pi}\frac{H(-Q)}{\sqrt{-Q}},\qquad
 \mathcal F^{-1}\Delta_B=\frac1{4\pi^2}\frac{H(-Q)}{\sqrt{-Q}}.
 \tag{F23}
\]
The cone singularity is locally integrable away from zero by regular coordinates and the exponent \(-1/2>-1\). At zero its homogeneous degree is \(-1>-3\), and the angular integral is finite by the same regular-coordinate calculation, so polar integration proves local integrability there too. The second formula follows from (F19) and \(V_-=H(-Q)/(\sqrt\pi\sqrt{-Q})\). Multiplying it by \(-2\pi i\) verifies (F18) directly. The first function is nonzero and solves \(P_Au=0\) by Corollary 16. Its support contains points with both positive and negative \(t\), for example \((t,2|t|,0)\) for every \(t\ne0\). It therefore has neither future-only nor past-only time support.

**Exercise 17 (advanced: Gaussian mass and an independent normalization).** For the dual cone of Exercise 12 and \(b>0\), evaluate \(\langle\Delta_B,e^{-b(\tau^2+\xi^2+\eta^2)}\rangle\). Verify the corresponding pairing for \(\widehat V_-\) by a direct integral on the physical side.

**Solution.** Write \((\xi,\eta)=(r\cos\theta,r\sin\theta)\). For \(r>0\), the two simple roots in \(\tau\) yield
\(\delta_0(\tau^2-r^2)=[\delta_r(\tau)+\delta_{-r}(\tau)]/(2r)\).
The spatial Jacobian \(r\), the two sheets, and angular integration therefore give
\[
 \langle\Delta_B,e^{-b|\cdot|^2}\rangle
    =2\pi\int_0^\infty e^{-2br^2}\,dr
    =\frac{\pi^{3/2}}{\sqrt{2b}}.
 \tag{F24}
\]
The whole-space measure construction in (F15) justifies passage through \(r=0\); there is no additional atom. The Gaussian integral is proved in the Fourier foundations. By (F19), the resulting pairing for \(\widehat V_-\) is \(4\pi^3/\sqrt{2b}\).

For a second calculation, the transform of \(\phi_b=e^{-b|\cdot|^2}\) is \((\pi/b)^{3/2}e^{-|\cdot|^2/(4b)}\). Pair this with \(V_-=H(r^2-t^2)/(\sqrt\pi\sqrt{r^2-t^2})\). For \(r>0\) substitute \(t=r\sin\vartheta\), \(-\pi/2<\vartheta<\pi/2\). Then \(dt/\sqrt{r^2-t^2}=d\vartheta\). All integrands are nonnegative, so the order of integration is justified by Tonelli, and the evaluations show finiteness:
\[
 \begin{aligned}
 \left\langle V_-,e^{-|\cdot|^2/(4b)}\right\rangle
 &=2\sqrt\pi\int_{-\pi/2}^{\pi/2}\int_0^\infty
          r e^{-r^2(1+\sin^2\vartheta)/(4b)}\,dr\,d\vartheta\\
 &=4b\sqrt\pi\int_{-\pi/2}^{\pi/2}
                     \frac{d\vartheta}{1+\sin^2\vartheta}
   =2\sqrt2\pi^{3/2}b.
 \end{aligned}
 \tag{F25}
\]
For the last integral set \(u=\tan\vartheta\), giving \(\int_{\mathbb R}du/(1+2u^2)=\pi/\sqrt2\), by the antiderivative \(2^{-1/2}\arctan(\sqrt2u)\). Multiplication by \((\pi/b)^{3/2}\) gives \(2\sqrt2\pi^3/\sqrt b=4\pi^3/\sqrt{2b}\), exactly the frequency-side value. The transpose identity has no conjugation and no extra \(2\pi\) factor.


## Sources

Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, reprint of the second edition (1990), Springer, 2003, [doi:10.1007/978-3-642-61497-2](https://doi.org/10.1007/978-3-642-61497-2), Theorem 6.2.1, Lemma 6.2.2, the two-dimensional remark following that lemma, and Example 8.2.6. The point-source and wavefront results are developed here with the exact earlier programme proofs listed above. The exposition, examples, exercises and figure are independently expressed.

- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second-edition reprint, Springer, 2003, [doi:10.1007/978-3-642-61497-2](https://doi.org/10.1007/978-3-642-61497-2), Section 8.5, the analytic quadratic-boundary observation following Theorem 8.5.2. Lemma 10 and Theorem 11 give complete analytic and derivative-growth classifications, including logarithmic, one-sided and causal cases; Proposition 12 and Exercises 9–11 treat analytic coordinates and weights.


Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition, 2003 reprint, §7.1, Theorem 7.1.23, together with Theorem 6.2.1 and Lemma 6.2.2. The Fourier normalization, homogeneous extension and both quadratic boundary limits are proved in Theorems 14–15 above.
