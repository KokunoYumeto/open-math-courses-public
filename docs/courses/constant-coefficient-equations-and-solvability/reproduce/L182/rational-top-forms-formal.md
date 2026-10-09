# Rational top forms in a hypersurface complement

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(f\) be a nonzero complex polynomial on \(\mathbb C^d\), \(d\geq1\), and put \(V=\{f\ne0\}\). The zero set that has been removed can be singular, reducible or defined with repeated factors. We prove that the forms
\[
 \frac{p(z)}{f(z)^k}\,dz_1\wedge\cdots\wedge dz_d,
 \qquad p\in\mathbb C[z_1,\ldots,z_d],\quad k\geq0,
 \tag{1}
\]
span the smooth complex de Rham group \(H^d_{\mathrm{dR}}(V;\mathbb C)\). Their periods detect ordinary finite-cycle homology in degree \(d\), over \(\mathbb C\) and over \(\mathbb Q\). The proof includes the finite-dimensionality needed to pass from approximation to spanning.

Basic historical references are Hörmander's weighted Cauchy–Riemann existence theorem [H], Sard's critical-value theorem [S] and Grothendieck's algebraic de Rham comparison [G]. Here we give a direct top-degree proof for this particular affine complement. The all-degree weighted estimate and its smoothness argument are proved below. The exact previously written inputs are Hilbert representation in [Lebesgue duality and Fourier functionals, Lemma 1.1](../../AN02-L043.html#a-representing-vector-in-hilbert-space), Fourier inversion and the Schwartz Plancherel formula in [Fourier transforms, finite spectra and convex separation, §§1–2](../../prerequisites/prerequisite-bridges.html), semialgebraic projection in [Symbols at infinity, Lemma 2.1](../../AN02-L018.html#algebraic-inequalities-survive-projection), the finite-chain handle theorem in [Ordinary finite-chain Morse handles](../../AN02-L125.html#mh0-statement-coefficients-and-boundary-cases), and the actual integration comparison in [When zero smooth periods mean that a cycle bounds](../../AN02-L116.html#cd6-integration-and-smooth-continuous-comparison). Those are exact statement inputs, with their lower foundations retained. We do not use a general algebraic de Rham theorem as an unproved premise.

## 1. A smooth global Cauchy–Riemann solution in every positive degree

On \(\mathbb C^D\), let \(E_q\) be the coefficient space of \((0,q)\)-forms. The wedges \(d\bar Z_{i_1}\wedge\cdots\wedge d\bar Z_{i_q}\), with increasing indices, are orthonormal by convention. Let \(c_j\) denote exterior multiplication by \(d\bar Z_j\), and let \(c_j^*\) be its coefficient adjoint. Direct insertion and deletion of an index give
\[
 c_jc_k+c_kc_j=0,\qquad
 c_j^*c_k^*+c_k^*c_j^*=0,\qquad
 c_jc_k^*+c_k^*c_j=\delta_{jk}I.
 \tag{2}
\]
Indeed, two different insertions or deletions change sign when their order is swapped. For equal indices, a wedge either contains that index or does not; exactly one of deletion followed by insertion and insertion followed by deletion restores it.

**Lemma 1.1.** For any smooth finite coefficient vector \(a\) on \(\mathbb C^D\), there is a smooth real weight \(\phi\) such that its Levi matrix is at least \(I\) and \(\int|a|^2e^{-\phi}dV<\infty\).

**Proof.** Set \(A_j=\{j\leq|Z|^2\leq j+1\}\) and
\[
 K_j=\log\!\left(2^{j+1}(1+\sup_{A_j}|a|^2)
                                 (1+\operatorname{vol}A_j)\right).
\]
These numbers are finite and positive. Choose a smooth convex nonnegative \(b\), zero for \(t\leq0\), with \(b(1)>0\). One explicit choice has \(b''(t)=e^{-1/t}\) for \(t>0\), zero otherwise, and \(b(0)=b'(0)=0\). Choose \(C\geq K_0\) and \(c_j\geq0\) with \(c_jb(1)\geq K_{j+1}\). The locally finite smooth sum
\[
 h(t)=C+t+\sum_{j=0}^{\infty}c_jb(t-j),\qquad
 \phi(Z)=h(|Z|^2)
 \tag{3}
\]
has \(h'\geq1\) and \(h''\geq0\). Its Levi form is
\[
 \mathcal L_\phi(\eta)
 =h'(|Z|^2)|\eta|^2+h''(|Z|^2)|\bar Z\cdot\eta|^2
 \geq|\eta|^2 .
 \tag{4}
\]
On \(A_0\), \(\phi\geq K_0\); on \(A_j\), \(j\geq1\), the summand with index \(j-1\) gives \(\phi\geq K_j\). Thus the weighted integral over \(A_j\) is at most \(2^{-j-1}\). Summing proves the assertion. Annular boundary spheres have measure zero. \(\square\)

**Theorem 1.2.** Suppose \(\phi\) is smooth and real on \(\mathbb C^D\), with Levi matrix at least \(I\). If \(a\) is a smooth \(\bar\partial\)-closed \((0,q)\)-form, \(1\leq q\leq D\), and
\[
 \|a\|_\phi^2=\int |a|^2e^{-\phi}dV<\infty ,
\]
there is a smooth \((0,q-1)\)-form \(u\) such that
\[
 \bar\partial u=a,\qquad
 \|u\|_\phi\leq q^{-1/2}\|a\|_\phi.
 \tag{5}
\]
In particular every smooth closed form in a positive degree on the entire affine space has a smooth global solution, without a growth assumption: apply Lemma 1.1 to choose its weight.

**Proof of the estimate.** Put \(H_q=L^2(e^{-\phi}dV;E_q)\), with inner products linear in the first entry. The maximal distributional operator \(T_q:H_q\to H_{q+1}\) is \(\bar\partial\); its domain consists of the vectors whose indicated distributional derivative belongs to \(H_{q+1}\). The top operator \(T_D\) is zero. Each operator is closed, because weighted norm convergence implies local square-integrable convergence and hence distributional convergence. Its domain contains compact smooth forms and is dense.

Write \(\partial_j=\partial/\partial Z_j\), \(\bar\partial_j=\partial/\partial\bar Z_j\), and \(\delta_j=\partial_j-\phi_j\). Weighted integration by parts gives the formal adjoint and the commutator
\[
 T=\sum_jc_j\bar\partial_j,\qquad
 T^*=-\sum_kc_k^*\delta_k,\qquad
 [\delta_k,\bar\partial_j]=\phi_{k\bar j}.
 \tag{6}
\]
Expanding both products and using (2) therefore gives, on every degree,
\[
 TT^*+T^*T
 =-\sum_j\delta_j\bar\partial_j
       +\sum_{j,k}\phi_{k\bar j}c_jc_k^*.
 \tag{7}
\]
For a compact smooth \((0,q)\)-form \(v\), pair (7) with \(v\). Integration by parts in the first term yields
\[
 \|T_{q-1}^*v\|_\phi^2+\|T_qv\|_\phi^2
 =\sum_{j,I}\|\bar\partial_jv_I\|_\phi^2
   +\int\left\langle
        \sum_{j,k}\phi_{k\bar j}c_jc_k^*v,v
                 \right\rangle e^{-\phi}dV .
 \tag{8}
\]
At each point a unitary change of coefficient basis diagonalizes the Hermitian Levi matrix. In that basis the last operator is \(\sum_j\lambda_jc_jc_j^*\). On the wedge indexed by \(I\) it has eigenvalue \(\sum_{j\in I}\lambda_j\): the operator \(c_jc_j^*\) keeps the wedge precisely when \(j\in I\). Since all \(\lambda_j\geq1\), (8) implies
\[
 q\|v\|_\phi^2
       \leq\|T_{q-1}^*v\|_\phi^2+\|T_qv\|_\phi^2.
 \tag{9}
\]
The pointwise diagonalization is only an algebraic evaluation of the curvature term; no derivatives of a chosen eigenbasis enter the identity.

We justify the adjoint domain and the passage to it. Compact smooth forms are a graph core for a maximal \(T_j\). First multiply by a cutoff \(\chi_R(Z)=\chi(Z/R)\), equal to one near zero. The product rule adds exterior multiplication by \(\bar\partial\chi_R\), whose operator norm is \(O(R^{-1})\). Dominated convergence handles the old derivative. On the resulting fixed compact support, mollification commutes with the constant-coefficient \(T_j\); the smooth weight is bounded above and below by positive constants there. Local convolution convergence in ordinary \(L^2\) thus gives convergence in both weighted graph norms. This proves the core assertion.

It follows directly from the definition of a Hilbert adjoint and that core assertion that \(v\in\operatorname{Dom}T_{q-1}^*\) precisely when the distribution \(-\sum c_j^*\delta_jv\) belongs to \(H_{q-1}\). One direction follows by testing compact smooth forms. In the other direction integration by parts on those tests extends to all of \(\operatorname{Dom}T_{q-1}\) by its graph core, so it is the bounded adjoint pairing. Smooth positive weights allow ordinary distributional tests to be converted into weighted ones by multiplication by \(e^\phi\) on their compact support.

Now take \(v\) in the joint domain of \(T_{q-1}^*\) and \(T_q\). The same cutoffs give convergence in all three norms. For the adjoint the added term is \(-\sum c_j^*(\partial_j\chi_R)v\), again \(O(R^{-1})\|v\|_\phi\). After cutoff, mollification commutes with every derivative. Its only adjoint error consists of the finite coefficient brackets
\[
 \phi_j(v_I*\rho_\varepsilon)
                      -(\phi_jv_I)*\rho_\varepsilon.
 \tag{10}
\]
On the fixed compact neighborhood their ordinary \(L^2\) norms are bounded by \(\omega_{\phi_j}(\varepsilon)\|v_I\|_2\), where \(\omega\) is the coefficient's modulus of continuity. To see the bound, write the bracket as the integral of
\((\phi_j(Z)-\phi_j(Z-h))v_I(Z-h)\rho_\varepsilon(h)\)
and apply the integral triangle inequality and translation invariance. Thus all errors go to zero. Weighted comparability on that neighborhood gives a compact smooth joint graph core. Passing (9) to this core limit proves it on the full joint domain.

**Proof of existence.** Set \(T=T_{q-1}\), \(S=T_q\), and \(N=\ker S\subset H_q\). The kernel is closed, and \(\operatorname{Ran}T\subset N\) since distributional mixed derivatives commute. Take \(v\in\operatorname{Dom}T^*\) and decompose \(v=v_N+v_\perp\) by orthogonal projection onto \(N\). For every \(b\in\operatorname{Dom}T\), \(Tb\in N\), so \((Tb,v_\perp)_\phi=0\). By the definition of adjoint, \(v_\perp\in\operatorname{Dom}T^*\) with \(T^*v_\perp=0\). Consequently \(v_N\) belongs to the joint domain, \(Sv_N=0\), and \(T^*v_N=T^*v\). Estimate (9) gives
\[
 \sqrt q\,\|v_N\|_\phi\leq\|T^*v\|_\phi.
 \tag{11}
\]
Because \(a\in N\), the functional
\[
 \Lambda(T^*v)=(v,a)_\phi
 \tag{12}
\]
is well defined on \(\operatorname{Ran}T^*\) and bounded by \(q^{-1/2}\|a\|_\phi\). Indeed (11) bounds its absolute value, and the same bound makes it zero whenever \(T^*v=0\). Extend to the closure of that range and use the proved Hilbert representation theorem there. It gives \(u\in\overline{\operatorname{Ran}T^*}\) of the norm in (5), with
\[
 (T^*v,u)_\phi=(v,a)_\phi .
 \tag{13}
\]
Compact smooth testing says \(\bar\partial u=a\) as distributions. Since \(a\in H_q\), \(u\) belongs to the maximal domain of \(T\), so this is the asserted Hilbert equation as well.

It remains essential to prove that the chosen \(u\) is smooth. The construction in the range closure makes \(u\perp\ker T\). For \(q\geq2\), the range of \(T_{q-2}\) lies in \(\ker T\), so \(T_{q-2}^*u=0\), including as distributions. For \(q=1\) there is no lower-degree operator. Thus in both cases the distributional equation is
\[
 \square_{q-1}u=T_{q-1}^*a,\qquad
 \square_{q-1}=T_{q-2}T_{q-2}^*+T_{q-1}^*T_{q-1}.
 \tag{14}
\]
The absent first product for \(q=1\) is zero. By (7), this is a smooth-coefficient elliptic system with scalar principal part \(-\tfrac14\Delta\). Section 2 proves explicitly that a locally square-integrable solution of (14), with its smooth right side, is smooth. It applies to \(u\), completing (5). \(\square\)

## 2. The local regularity used in the solution

Here \(\Delta\) is the real Laplacian in \(n=2D\) coordinates. For clarity we prove the precise elementary elliptic fact needed above.

**Lemma 2.1.** If a finite coefficient vector \(u\) is locally square integrable and satisfies
\[
 \Delta u=\sum_{\ell=1}^n A_\ell(x)\partial_{x_\ell}u
                       +B(x)u+h(x)
 \tag{15}
\]
as distributions, where the matrices \(A_\ell,B\) and vector \(h\) are smooth, then \(u\) has a smooth representative.

**Proof.** Use the Fourier convention \(\widehat v(\xi)=\int e^{-ix\cdot\xi}v(x)\,dx\). The written Schwartz inversion and Plancherel formulas give
\(\|\widehat v\|_2=(2\pi)^{n/2}\|v\|_2\).
They extend to all \(L^2\): compact cutoffs followed by convolution approximate an \(L^2\) function by compact smooth functions, which belong to the Schwartz space. For the convolution step, translation continuity holds first for finite linear combinations of bounded-box indicators, by the measure of their translated symmetric differences, and then for all \(L^2\) by approximation and the translation isometry. The ordinary Lebesgue approximation of measurable finite-measure sets by finite unions of boxes gives that first dense class. The integral triangle inequality now proves convolution convergence. The Plancherel isometry extends by completion, and its range is all \(L^2\), since its range already contains every Schwartz function by inversion. This also retains the distributional differentiation identity.

For an integer \(s\), define \(H^s\) by the Fourier weight \((1+|\xi|^2)^{s/2}\), with norm
\[
 \|v\|_{H^s}^2=(2\pi)^{-n}
       \int(1+|\xi|^2)^s|\widehat v(\xi)|^2\,d\xi.
 \tag{16}
\]
For negative \(s\) this definition uses tempered distributions with the indicated weighted function transform. In particular \(H^{-1}\) is the dual of \(H^1\) under the \(L^2\) pairing. To verify the dual assertion, apply Cauchy–Schwarz with the reciprocal weights in (16); conversely Riesz representation after multiplying the transform by its \(H^1\) weight gives every bounded functional by a transform with the reciprocal weight. This uses the same proved Hilbert representation theorem.

For each nonnegative integer \(s\), expansion of \((1+\sum\xi_\ell^2)^s\) and Plancherel show that (16) is equivalent to the finite sum of the \(L^2\) derivative norms through order \(s\). This holds first on Schwartz functions and then on their \(H^s\) completion. The completion is exactly the Fourier-weighted space in (16): truncate a weighted-square-integrable transform on larger balls, approximate the truncated transform by compact smooth functions in the locally comparable weighted norm, and use Schwartz inversion. Those inverse transforms are Schwartz functions, dense in (16). Smooth compact multipliers are therefore bounded on \(H^s\) by the finite Leibniz rule, and on \(H^{-1}\) by the dual assertion. A derivative maps \(H^s\) to \(H^{s-1}\), since \(|\xi_\ell|\leq(1+|\xi|^2)^{1/2}\).

If \(v\in L^2\) and \(\Delta v\in H^r\), for an integer \(r\geq-1\), then
\[
 \|v\|_{H^{r+2}}\leq
       C_r\bigl(\|\Delta v\|_{H^r}+\|v\|_2\bigr).
 \tag{17}
\]
Indeed the transform of \(\Delta v\) is \(-|\xi|^2\widehat v\). On \(|\xi|\geq1\), the weight \((1+|\xi|^2)^{r+2}\) is bounded by a constant times \((1+|\xi|^2)^r|\xi|^4\). On \(|\xi|\leq1\) it is bounded, so the \(L^2\) norm supplies the remaining part. This proves (17) directly for the distributions in question.

Suppose \(u\) is locally in \(H^s\) for a nonnegative integer \(s\). Fix any compactly supported smooth \(\chi\) in a coordinate neighborhood, and choose a second cutoff \(\eta=1\) on a neighborhood of its support. In (15) replace \(u\) by \(\eta u\) when multiplying by \(\chi\). The right side, after this multiplication, belongs to \(H^{s-1}\), by the multiplier and derivative facts just proved. The identity
\[
 \Delta(\chi u)=\chi\Delta u+
            2\sum_\ell(\partial_{x_\ell}\chi)\partial_{x_\ell}u
                         +(\Delta\chi)u
 \tag{18}
\]
has the same property. The smooth term \(\chi h\) belongs to every such space. Since \(\chi u\in L^2\), (17) with \(r=s-1\) gives \(\chi u\in H^{s+1}\). Starting with \(s=0\), this proves local membership in every integer Sobolev space.

Finally take \(v=\chi u\in H^s\), with \(s>k+n/2\). Cauchy–Schwarz gives
\[
 \int|\xi|^k|\widehat v(\xi)|\,d\xi
 \leq
 \left(\int|\xi|^{2k}(1+|\xi|^2)^{-s}d\xi\right)^{1/2}
            (2\pi)^{n/2}\|v\|_{H^s}<\infty .
 \tag{19}
\]
The integrability follows near infinity from \(2k-2s<-n\) and near zero from \(k\geq0\). Fourier inversion of the integrable differentiated transforms, by dominated convergence, gives continuous derivatives through order \(k\); these representatives agree with the distributional derivatives. Arbitrarily large \(s\) and \(k\) give a smooth representative. Local representatives agree on overlaps because they represent the same distribution. This proves the lemma. \(\square\)

For (14), (7) reads explicitly
\[
 \square_{q-1}u
 =-\tfrac14\Delta u+\sum_j\phi_j\bar\partial_ju+
       \left(\sum_{j,k}\phi_{k\bar j}c_jc_k^*\right)u .
 \tag{20}
\]
The matrix term is taken in degree \(q-1\). Rearranging (14) gives (15), with smooth right side \(-4T_{q-1}^*a\) and smooth first- and zero-order coefficients. The factor \(1/4\) comes from \(\partial_j\bar\partial_j=(\partial_{x_j}^2+\partial_{y_j}^2)/4\).

## 3. Solving on the complement by using a closed graph

Set \(D=d+1\) and
\[
 G(z,w)=f(z)w-1,\qquad
 M=\{G=0\}\subset\mathbb C^{d+1},\qquad
 \iota(z)=(z,1/f(z)).
 \tag{21}
\]
The restriction of \(\pi(z,w)=z\) to \(M\) is the holomorphic inverse of \(\iota\). The graph is closed, and it is smooth because \(\partial G/\partial w=f(z)\ne0\) on it. These facts concern \(M\), not smoothness of the removed zero set of \(f\).

**Theorem 3.1.** Every smooth closed \((0,q)\)-form \(a\) on \(V\), \(1\leq q\leq d\), is \(\bar\partial b\) for a smooth \((0,q-1)\)-form \(b\) on \(V\).

**Proof.** Choose a smooth cutoff \(\chi_0:[0,\infty)\to[0,1]\), equal to one near zero and zero on \([1,\infty)\). On \(V\times\mathbb C\) put
\[
 h=\chi_0\!\left(\frac{|G|^2}{|f|^2}\right)\pi^*a ,
 \tag{22}
\]
and extend it by zero where \(f=0\). This is a smooth global ambient form. Near a finite point with \(f=0\), \(G\) is close to \(-1\); the quotient in the cutoff is greater than one on a whole neighborhood, so the form there is identically zero. No bound on \(a\) near the missing divisor is required.

Near each point of \(M\), the cutoff is one. There \(\bar\partial h=\pi^*\bar\partial a=0\). Consequently
\[
 A=G^{-1}\bar\partial h
 \tag{23}
\]
extends by zero across \(M\) to a smooth ambient \((0,q+1)\)-form. It is closed: off \(M\), holomorphy of \(G\) and \(\bar\partial^2=0\) give \(\bar\partial A=0\); near \(M\) it vanishes. Since \(q+1\leq d+1\), Theorem 1.2 with a weight from Lemma 1.1 gives a smooth ambient \((0,q)\)-form \(v\) with \(\bar\partial v=A\).

The smooth form \(H=h-Gv\) is closed. A second use of that theorem gives a smooth ambient \((0,q-1)\)-form \(u\) with \(\bar\partial u=H\). Pullback by the holomorphic map \(\iota\) is defined for these smooth forms and commutes with \(\bar\partial\), as follows coefficientwise from the ordinary chain rule. Since \(G\circ\iota=0\) and \(\iota^*h=a\), it follows that
\[
 \bar\partial(\iota^*u)=\iota^*H=a .
 \tag{24}
\]
Thus \(b=\iota^*u\) is the required smooth solution. In the endpoint \(q=d\), (23) has ambient degree \(d+1\), exactly the top permitted degree of Theorem 1.2. \(\square\)

## 4. Closed smooth top forms have holomorphic representatives

**Proposition 4.1.** Every closed smooth complex \(d\)-form \(\alpha\) on \(V\) is cohomologous to a holomorphic \(d\)-form.

**Proof.** Write \(\alpha=\sum_{p+q=d}\alpha^{p,q}\) by type. If a nonzero component has largest antiholomorphic degree \(q>0\), closure of \(\alpha\) in type \((p,q+1)\) says
\(\bar\partial\alpha^{p,q}=0\), because a component in degree \(q+1\) is absent. Use the global coordinate wedges to write
\[
 \alpha^{p,q}=\sum_{|I|=p}dz_I\wedge a_I .
\]
Each \(a_I\) is a closed \((0,q)\)-form: the identity
\(\bar\partial(dz_I\wedge a_I)=(-1)^p dz_I\wedge\bar\partial a_I\)
and linear independence of the \(dz_I\) give this conclusion. Theorem 3.1 gives smooth \(b_I\) with \(\bar\partial b_I=a_I\). Put
\[
 \beta^{p,q-1}=(-1)^p\sum_{|I|=p}dz_I\wedge b_I .
 \tag{25}
\]
Then \(\bar\partial\beta^{p,q-1}=\alpha^{p,q}\). Subtract \(d\beta^{p,q-1}\) from \(\alpha\). Its component with antiholomorphic degree \(q\) disappears, and the only other type changed is \((p+1,q-1)\). Closure is retained.

Repeat from \(q=d\) down to \(q=1\), skipping zero components. There are at most \(d\) steps. The resulting closed form \(\gamma\) has type \((d,0)\), so
\[
 \gamma=g(z)\,dz_1\wedge\cdots\wedge dz_d,\qquad
 \bar\partial g=0,\qquad
 \alpha-\gamma=d\beta
 \tag{26}
\]
for the finite sum \(\beta\) of the chosen primitives. A smooth function with all Cauchy–Riemann derivatives zero is holomorphic: apply the one-variable Cauchy formula successively on polydiscs. Thus \(\gamma\) is holomorphic. Stokes shows that \(\alpha\) and \(\gamma\) have the same period on every finite smooth cycle. \(\square\)

## 5. Entire extension and rational approximation

**Proposition 5.1.** Every holomorphic function \(g\) on \(V\) is the restriction, under \(\iota\), of an entire function on \(\mathbb C^{d+1}\). Consequently it can be approximated uniformly on each compact subset of \(V\) by \(\mathbb C[z,1/f]\), also with every fixed finite number of derivatives.

**Proof.** Form the smooth ambient function
\[
 h(z,w)=\chi_0\!\left(\frac{|G(z,w)|^2}{|f(z)|^2}\right)g(z),
 \tag{27}
\]
extended by zero where \(f=0\), exactly as in (22). It is holomorphic near \(M\). Therefore \(A=G^{-1}\bar\partial h\) is a smooth closed ambient \((0,1)\)-form, zero near \(M\). Lemma 1.1 and Theorem 1.2 give a smooth scalar \(v\) with \(\bar\partial v=A\). The function
\[
 H=h-Gv
 \tag{28}
\]
is smooth and \(\bar\partial\)-closed on the entire ambient affine space, hence entire. Its ordinary smooth restriction to \(M\) is \(h|_M\), since \(G|_M=0\). Thus \(H\circ\iota=g\).

For compact \(K\subset V\), \(\iota(K)\) is compact. Put it inside a polydisc of coordinate radius \(r<R\). The repeated Cauchy estimate bounds the Taylor coefficients of \(H\) by \(M_RR^{-|\nu|}\), and
\[
 \sum_{\nu\in\mathbb N^{d+1}}(r/R)^{|\nu|}
                      =(1-r/R)^{-d-1}<\infty .
 \tag{29}
\]
The tails of its entire Taylor polynomials therefore tend uniformly to zero there. Differentiated series have the same property on strictly smaller polydiscs, by the same bound with the finite polynomial factors in \(\nu\).

Restricting an ambient polynomial to \(w=1/f(z)\) gives an element of \(\mathbb C[z,1/f]\). Its finitely many denominators can be cleared to the form \(p/f^k\). For derivative approximation, first choose a compact neighborhood of \(K\) still inside \(V\), perform the ambient approximation on its graph, and use the finite chain rule and bounded derivatives of \(\iota\) on that neighborhood. This proves all the claims. \(\square\)

## 6. Why the graph has finite-dimensional ordinary homology

Approximation will yield spanning only after we prove finite-dimensionality. We construct a proper strictly plurisubharmonic Morse function with finitely many critical points on \(M\).

**Lemma 6.1 (equal-dimensional critical values).** For a \(C^1\) map \(F:O\to\mathbb R^N\), where \(O\subset\mathbb R^N\) is open and \(N\geq1\), the images of points with singular derivative have Lebesgue measure zero.

**Proof.** Fix a compact set \(Q\subset O\), and a larger compact neighborhood still in \(O\). There the derivative has bound \(B\) and is uniformly continuous. Given \(\varepsilon>0\), choose a grid size \(\delta>0\) so small that derivatives at distance at most \(\sqrt N\,\delta\) differ by at most \(\varepsilon\), and every grid cube meeting \(Q\) stays in that neighborhood. There are at most \(C_Q\delta^{-N}\) such cubes.

For a cube meeting the critical set in \(Q\), choose a critical point \(c\) in that intersection. The integral first-order remainder along segments gives, for \(x\) in the cube,
\[
 F(x)=F(c)+DF(c)(x-c)+R(x),\qquad
                     |R(x)|\leq\varepsilon\sqrt N\,\delta .
 \tag{30}
\]
The linear image lies in a subspace of dimension at most \(N-1\) and has radius at most \(B\sqrt N\,\delta\). Enlarge that subspace to an \((N-1)\)-plane if necessary. After an orthogonal change of target coordinates, (30) places the image inside a rectangular box whose first \(N-1\) side lengths are at most \(C_N(B+\varepsilon)\delta\), and last side length at most \(C_N\varepsilon\delta\). Its volume is at most
\[
 C_N(B+\varepsilon)^{N-1}\varepsilon\,\delta^N .
 \tag{31}
\]
This argument also covers \(N=1\), when the first product is empty. Summing over the cubes bounds the outer measure of the critical image from \(Q\) by \(C_QC_N(B+\varepsilon)^{N-1}\varepsilon\). Let \(\varepsilon\downarrow0\). A countable compact exhaustion of \(O\) proves the assertion. In particular regular values exist; their complement cannot contain an open ball of positive measure. This is the equal-dimensional case of Sard's theorem, with its proof given here. \(\square\)

**Lemma 6.2.** A discrete semialgebraic subset of a Euclidean space is finite.

**Proof.** A discrete subset is countable: for each point choose a ball from the countable rational-center rational-radius basis that meets the subset in that point alone, and choose the first such ball in a fixed enumeration. This is an injection into that basis.

By the exact semialgebraic projection theorem cited above, each coordinate projection of the subset is semialgebraic. It is also countable. A semialgebraic subset of the real line is a finite union of points and intervals. Indeed, use the finite polynomials in its Boolean description, omit identically zero polynomials after recording their signs, and divide the line at their finitely many real roots. Every polynomial has constant nonzero sign on each intervening interval, so membership is constant there; the endpoints are finitely many single points. A countable such set contains no nonempty interval and is therefore finite.

Each coordinate projection is thus finite, and the original subset lies in the finite Cartesian product of those projections. It is finite. \(\square\)

**Proposition 6.3.** There is a center \(a\in\mathbb C^{d+1}\) such that
\[
 \rho_a(x)=|x-a|^2\quad(x\in M)
 \tag{32}
\]
is proper, bounded below, strictly plurisubharmonic and Morse, and has finitely many critical points.

**Proof.** Write the ambient affine space as \(\mathbb R^N\), \(N=2d+2\), and \(g_1=\operatorname{Re}G\), \(g_2=\operatorname{Im}G\). These are real polynomials. Their gradients \(n_1=\nabla g_1,n_2=\nabla g_2\) are independent at every point of \(M\): the complex derivative \(\partial G/\partial w=f\ne0\) has real rank two. They span the normal space to \(M\).

In the global real coordinates supplied by \(\iota:V\to M\), consider the map on the open subset \(V\times\mathbb R^2\) of \(\mathbb R^N\),
\[
 \Phi(x,\lambda)=x-\lambda_1n_1(x)-\lambda_2n_2(x).
 \tag{33}
\]
Here \(x\in M\) is evaluated using those coordinates. The domain and target have the same real dimension \(N\). Lemma 6.1 gives a regular value \(a\).

A point \(x\in M\) is critical for \(\rho_a|_M\) precisely when
\[
 x-a=\lambda_1n_1(x)+\lambda_2n_2(x)
 \tag{34}
\]
for a unique \(\lambda\). This is exactly \(\Phi(x,\lambda)=a\). Set
\(A=I-\sum_j\lambda_j\operatorname{Hess}g_j(x)\).
For tangent vectors \(v,t\in T_xM\), the restricted Hessian of \(\rho_a\) is
\[
 B_x(v,t)=2\,v\cdot At .
 \tag{35}
\]
To verify it, differentiate a curve in \(M\) twice: \(n_j\cdot x''=-v\cdot(\operatorname{Hess}g_j)v\), and insert (34) into
\(\rho_a''=2|v|^2+2(x-a)\cdot x''\).
This gives (35) on the diagonal, and polarization gives the bilinear formula.

The differential of (33) at a critical pair is
\[
 D\Phi(v,\mu)=Av-\mu_1n_1-\mu_2n_2 .
 \tag{36}
\]
Project onto \(T_xM\). The result is the tangent operator \(P_TAv\), one-half the Hessian (35). If that operator is invertible, its tangent output first determines \(v\), and independence of the normals then determines \(\mu\) from the normal output; thus (36) is invertible. Conversely a nonzero vector in the tangent kernel gives \(Av\) normal, and unique \(\mu\) then makes (36) zero. Hence (36) is invertible exactly when (35) is nonsingular. The chosen regular value makes every critical point Morse.

The actual critical pairs form the real polynomial solution set
\[
 S_a=\left\{(x,\lambda):
       g_1(x)=g_2(x)=0,\ 
       x-a=\lambda_1\nabla g_1(x)+\lambda_2\nabla g_2(x)
                         \right\}\subset\mathbb R^{N+2}.
 \tag{37}
\]
Every solution lies in \(M\), and \(\lambda\) is unique. Because \(a\) is regular in (33), the inverse function theorem makes each preimage isolated in the smooth coordinates \(M\times\mathbb R^2\). Those coordinates give the subspace topology of the set in (37), so \(S_a\) is discrete as a subset of the ambient Euclidean space. It is semialgebraic by its displayed equations. Lemma 6.2 shows that it is finite, and hence the critical points are finite.

Since \(M\) is closed in the ambient Euclidean space, the intersection of \(M\) with a closed ball centered at \(a\) is compact. This proves properness of (32); its lower bound is zero. Under \(\iota\), the function is
\[
 \rho_a(z)=\sum_{j=1}^d|z_j-a_j|^2
                         +|1/f(z)-a_{d+1}|^2 .
 \tag{38}
\]
All the functions inside the squared norms are holomorphic. Its Levi form on a complex tangent vector \(v\) is
\[
 \mathcal L_{\rho_a}(v)
       =|v|^2+|d(1/f)_z(v)|^2\geq|v|^2>0
                                      \quad(v\ne0).
 \tag{39}
\]
It is therefore strictly plurisubharmonic. No smoothness or square-free hypothesis on \(f\) has entered. \(\square\)

**Corollary 6.4.** All ordinary groups \(H_j(V;\mathbb C)\) and \(H_j(V;\mathbb Q)\) are finite dimensional, and they vanish for \(j>d\).

**Proof.** At a critical point the real Hessian \(B\) of a strictly plurisubharmonic function satisfies
\[
 B(v,v)+B(Jv,Jv)=4\mathcal L_\rho(v)>0 .
 \tag{40}
\]
This follows by expanding the Wirtinger derivatives at the critical point, where the Hessian is coordinate invariant. If the negative eigenspace \(W\) had real dimension \(r>d\), then \(\dim(W\cap JW)\geq2r-2d>0\). Choose \(0\ne v=Jw\in W\cap JW\), with \(w\in W\); then \(Jv=-w\in W\). Both terms on the left of (40) would be negative, a contradiction. All Morse indices are thus at most \(d\).

Apply the cited full finite-chain Morse handle theorem to (32). Begin with an empty regular sublevel below its lower bound and cross the finitely many critical values using its actual open sublevels \(W_i\). Each relative group \(H_j(W_i,W_{i-1};k)\), \(k=\mathbb C\) or \(\mathbb Q\), is a finite direct sum of copies of \(k\), one for each crossed point of index \(j\). The exact pair segment
\[
 H_j(W_{i-1};k)\longrightarrow H_j(W_i;k)
                   \longrightarrow H_j(W_i,W_{i-1};k)
 \tag{41}
\]
proves finite-dimensionality by induction: the kernel of the second arrow is an image of a finite-dimensional space, and its image lies in a finite-dimensional relative group. In fact
\(\dim H_j(W_i;k)\leq\dim H_j(W_{i-1};k)+
\dim H_j(W_i,W_{i-1};k)\).
Above degree \(d\), the outer groups in (41) are zero and the new absolute group is zero.

Choose a regular level above every critical value. Beyond it every relative group is zero; the adjacent pair sequences, including the relative group in degree \(j+1\), make all later stage maps isomorphisms. Every finite chain has compact image and belongs to one stage of the increasing open cover. Every finite bounding relation likewise belongs to some later stage. Thus the actual direct-limit comparison proved in the cited handle theorem's passage to the whole manifold identifies \(H_j(M;k)\) with that one finite-dimensional stage group. This is ordinary homology, with finite chains; no locally finite-chain or compact-support conclusion is being inferred. The diffeomorphism \(V\cong M\) proves the corollary. \(\square\)

## 7. Rational spanning and the exact period test

**Theorem 7.1.** The forms (1) span \(H^d_{\mathrm{dR}}(V;\mathbb C)\). A finite smooth \(d\)-cycle \(c\) with complex coefficients is zero in ordinary homology if and only if all the periods of (1) on \(c\) vanish. The same assertion holds for rational cycles in \(H_d(V;\mathbb Q)\).

**Proof of detection.** A holomorphic top form has the unique expression \(g(z)\,dz_1\wedge\cdots\wedge dz_d\). For any fixed finite smooth cycle \(c=\sum_\sigma c_\sigma\sigma\), the simplex images form a compact set \(K\subset V\), and
\[
 B_c=\sum_\sigma|c_\sigma|\int_{\Delta^d}
       \left|\sigma^*(dz_1\wedge\cdots\wedge dz_d)\right|<\infty .
 \tag{42}
\]
The absolute value here is that of the coefficient of the oriented real parameter volume. Smooth simplex maps on their compact domains have bounded derivatives, so the integral is finite. Proposition 5.1 approximates \(g\) uniformly on \(K\) by coefficients \(p/f^k\), and the difference of the two periods is bounded by \(B_c\) times the uniform error.

Thus vanishing of all rational periods implies vanishing of all holomorphic top-form periods. Proposition 4.1 then gives vanishing against every closed smooth complex \(d\)-form. The integration/de Rham detection theorem cited above gives a finite smooth bounding chain over \(\mathbb C\). Conversely such a boundary has zero rational periods by Stokes: every form (1) is holomorphic and closed, its possible poles lying outside \(V\).

For a rational cycle, the exact faithful rational-coefficient comparison in that lesson gives
\[
 H_d(V;\mathbb Q)\otimes_{\mathbb Q}\mathbb C
                       \cong H_d(V;\mathbb C),
 \tag{43}
\]
and injection of \(h\mapsto h\otimes1\). Complex vanishing of the rational class therefore implies rational vanishing, with a finite smooth rational bounding chain by the same smooth/continuous comparison. The converse again follows by Stokes. No integral torsion conclusion is asserted.

**Proof of spanning.** By Corollary 6.4, \(r=\dim_\mathbb C H_d(V;\mathbb C)\) is finite. The cited integration isomorphism, combined with its algebraic cochain-dual argument, identifies
\[
 H^d_{\mathrm{dR}}(V;\mathbb C)
               \cong\operatorname{Hom}_\mathbb C(H_d(V;\mathbb C),\mathbb C)
 \tag{44}
\]
via actual integration. If \(r=0\), there is no nonzero class to span. Suppose \(r\geq1\). Choose a basis represented by finite smooth cycles \(c_1,\ldots,c_r\), using the proved smooth/continuous homology comparison. The dual coordinate functionals in (44) give closed smooth forms \(\alpha_1,\ldots,\alpha_r\) with
\(\int_{c_i}\alpha_j=\delta_{ij}\).
Proposition 4.1 replaces them by holomorphic top forms
\(\gamma_j=g_j\,dz_1\wedge\cdots\wedge dz_d\)
with exactly the same periods.

Take the compact union \(K\) of all the chosen simplex images, and let \(B=\max_i B_{c_i}\), using (42). Approximate every \(g_j\) on \(K\) by a rational coefficient \(r_j=p_j/f^{k_j}\), with error less than
\[
 \varepsilon=\frac{1}{2r(1+B)} .
 \tag{45}
\]
The period matrix
\[
 P_{ij}=\int_{c_i} r_j\,dz_1\wedge\cdots\wedge dz_d
 \tag{46}
\]
satisfies \(|P_{ij}-\delta_{ij}|<1/(2r)\), and hence
\(\|P-I\|_\infty<1/2\)
in the row-sum matrix norm. It is invertible: if \(Pv=0\) for a nonzero column vector \(v\), then
\(\|v\|_\infty=\|(I-P)v\|_\infty<\tfrac12\|v\|_\infty\),
a contradiction. Injectivity of a square finite-dimensional matrix gives surjectivity as well.

The \(r\) rational-form classes therefore have independent period columns and are a basis under (44). Every class is a finite complex linear combination of them. That finite combination itself has a common denominator \(f^K\), with polynomial numerator, so every class has a representative of the single form (1). This establishes exact cohomological spanning, not merely density in a space of coefficients. \(\square\)

## 8. The projective homogeneous family, with positive pole exponents

Let \(F\) be a nonzero homogeneous polynomial of degree \(m\geq1\) on \(\mathbb C^{d+1}\), let \(L\) be a nonzero linear form, and put
\[
 V_{\mathrm{pr}}=\mathbb P^d\setminus\{FL=0\}.
 \tag{47}
\]
Choose linear coordinates \(Z_0=L,Z_1,\ldots,Z_d\). This complement lies entirely in the chart \(Z_0\ne0\), identified with \(V=\{f\ne0\}\) in \(\mathbb C^d\), where \(z_j=Z_j/Z_0\) and \(f(z)=F(1,z)\). The polynomial \(f\) is nonzero, although its degree can be smaller than \(m\) and it can be constant.

Set
\[
 \omega=\sum_{j=0}^d(-1)^j Z_j\,
          dZ_0\wedge\cdots\wedge\widehat{dZ_j}
                              \wedge\cdots\wedge dZ_d.
 \tag{48}
\]
For positive integers \(k,s\) and a homogeneous polynomial \(P\) with
\[
 \deg P=mk+s-d-1,
 \tag{49}
\]
the form \(P\omega/(F^kL^s)\) is horizontal for the scalar action and invariant under it. Horizontality follows because \(\omega\) is the contraction of the ambient volume form with the Euler vector field; contracting it with that field again is zero. The weight of \(\omega\) under \(Z\mapsto tZ\) is \(d+1\), so (49) makes the total weight zero. Consequently this is a well-defined holomorphic top form on (47). More explicitly the pullback to the section \(Z_0=1\) is
\[
 \frac{P(1,z)}{f(z)^k}\,dz_1\wedge\cdots\wedge dz_d .
 \tag{50}
\]
The section identifies the complement with one affine chart, and weight-zero horizontality proves equality under its scalar representatives.

**Corollary 8.1.** The forms
\[
 \frac{P\omega}{F^kL^s},
 \qquad k,s\geq1,\qquad\deg P=mk+s-d-1
 \tag{51}
\]
span \(H^d_{\mathrm{dR}}(V_{\mathrm{pr}};\mathbb C)\) and detect ordinary finite \(d\)-cycle homology over \(\mathbb C\) and \(\mathbb Q\), with the given chart identification and orientations.

**Proof.** Every form (51) restricts to one in (1). Conversely start with a nonzero polynomial numerator \(p\) in (1). If \(k=0\), replace it by \(k=1\) and numerator \(pf\); this does not change the form. Choose an integer \(D_0\geq\deg p\) so large that
\[
 s=D_0-mk+d+1\geq1.
 \tag{52}
\]
Its homogenization
\[
 P(Z)=Z_0^{D_0}p(Z_1/Z_0,\ldots,Z_d/Z_0)
 \tag{53}
\]
is a homogeneous polynomial of degree \(D_0\), satisfies (49), and gives precisely the initial form in (50). The zero form is immediate. Thus the two families have the same affine representatives, and Theorem 7.1 applies. This covers singular and repeated \(F\), including a factor equal to \(L\). The exponents in (51) are positive even if a particular form has removable poles. \(\square\)

## References

[H] Lars Hörmander, *\(L^2\) estimates and existence theorems for the \(\bar\partial\) operator*, Acta Mathematica **113** (1965), 89–152. [Primary article](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5989-11511_2006_Article_BF02391775.pdf), [journal bibliographic record](https://www.mathnet.ru/eng/mat389). The weighted Hilbert method is the classical source; §§1–3 give the precise smooth all-degree proof consumed here.

[S] Arthur Sard, *The measure of the critical values of differentiable maps*, Bulletin of the American Mathematical Society **48** (1942), 883–890. [Original article](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/sard.pdf). Lemma 6.1 proves the equal-dimensional \(C^1\) case needed for the finite-dimensional normal-parameter map.

[G] Alexander Grothendieck, *On the de Rham cohomology of algebraic varieties*, Publications Mathématiques de l'IHÉS **29** (1966), 95–103. [Primary article](https://www.numdam.org/item/PMIHES_1966__29__95_0.pdf). It establishes the broader algebraic comparison. The present argument proves the stated top-degree conclusion for a principal polynomial complement directly, with its exact internal topology inputs; it does not prove that broader theorem.

All original prose and mathematical figures accompanying this exposition are CC0-1.0. The linked historical articles retain their own rights and are not reproduced. The proof detects ordinary rational or complex cycles; it does not detect integral torsion. Applying Corollary 8.1 to a specified affine cycle still requires the actual affine/projective comparison, including the chosen tube orientation, sign and multiplicity. Rational-form spanning alone does not identify that geometric cycle or prove a component-constancy statement.
