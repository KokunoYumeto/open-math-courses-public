# Compact forcing, moments and positive error kernels

*Reconstructed by GPT-6 Astra (OpenAI), Ultra reasoning effort, 4 October 2026. Public domain (CC0).*

A compact source can produce a noncompact potential. Moment conditions remove its exterior terms. We first prove this mechanism for coordinate primitives and ordinary differential equations, then for the planar Laplacian. Two explicit potentials show why the source at a singularity must be computed distributionally. Finally, a compact fourth primitive becomes a positive kernel for a quadrature error.

Pairings are complex-linear. Write \(\partial_j=\partial/\partial x_j\), \(\mathcal D'= \mathcal D'(\mathbb R^n)\), and \(\mathcal E'\) for compactly supported distributions. A compact distribution acts on a smooth function by inserting a smooth cutoff equal to one near its support; the value is independent of the cutoff. Its finite-order bound and this extension are proved in [U008](order-positivity-and-limits.md), Proposition 1.2, and [U021](convolution-as-addition-of-supports.md), B0. U021, B1–B3, Theorems 1.1, 2.1, 3.1 and Corollary 4.2, proves all convolution, parameter, associativity and smoothness statements used here.

The scalar calculus and measure proofs are in the [metric](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), Sections 12–13, and [integration](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), Sections 15–16, foundations. The [Fourier foundations](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F3, supplies the complete Gaussian integral. The constant-coordinate theorem is [U032](regularity-across-a-distinguished-variable.md), Lemma 1.3. Further exact earlier proofs are identified at their use below; the new moment, matrix, branch, endpoint and error-kernel arguments are given in full.

## A compact primitive is decided by moments

**Lemma 1.1 (lower-coordinate uniqueness).** Let \(w\) have support in \(\prod_{j=1}^n[L_j,\infty)\). If a product of positive powers of any selected coordinate derivatives annihilates \(w\), then \(w=0\).

**Proof.** Suppose first \(\partial_jw=0\). U032, Lemma 1.3, gives a distribution independent of that coordinate. Pair with a mass-one bump supported strictly below \(L_j\) and an arbitrary test in the other coordinates. The pairing is zero by support and equals the pairing of the reduced distribution with that arbitrary test. Thus the reduced distribution, and \(w\), vanish. If \(\partial_j^m w=0\), apply this argument successively to \(\partial_j^{m-1}w,\ldots,w\); their supports retain the same bound. For a product, treat all but one factor as already applied to \(w\), remove the remaining factor by pure-coordinate uniqueness, and repeat. This proves the assertion for every selected subset and every positive order. \(\square\)

We also record directly that
\[
 A_m(t)=\frac{t_+^{m-1}}{(m-1)!},\qquad m\ge1,
 \qquad A_m^{(m)}=\delta_0.
\]
Here \(A_1=1_{(0,\infty)}\). Its derivative pairs as \(-\int_0^\infty\phi'=\phi(0)\). For \(m>1\), integration by parts gives \(A_m'=A_{m-1}\), since the positive power has zero value at the endpoint. Repetition proves the formula, including all signs.

**Lemma 1.2 (polynomial moments determine compact distributions).** If \(T\in\mathcal E'(\mathbb R^d)\) and \(T(x^\beta)=0\) for every multiindex \(\beta\), then \(T=0\).

**Proof.** In dimension zero, the constant monomial suffices. Otherwise let \(K\) be a compact neighborhood of the support on which the action is controlled by derivatives through order \(N\). For fixed \(t>0,y\in\mathbb R^d\), put \(Q(x)=-|y-x|^2/(4t)\). The exponential series is a limit of polynomials in the controlling norm. Indeed, on \(K\), bound \(Q\) and its first two derivatives by \(R\ge1\). A derivative of order at most \(N\) of \(Q^j\) is a sum of at most \(C_N(1+j)^N\) products, each bounded by a fixed geometric power \(R_1^j\). Thus
\[
 \max_{|\beta|\le N}\sup_K|\partial^\beta(Q^j/j!)|
                 \le C_N(1+j)^N R_1^j/j!,
\]
whose series converges because the ratio tends to zero. The finite-order action therefore gives \(T(e^Q)=0\).

Set \(K_t(x)=(4\pi t)^{-d/2}e^{-|x|^2/(4t)}\). Its mass is one by the supplied Gaussian proof. Consequently \(K_t*T=0\). For a compact smooth \(\phi\), each derivative of \(\phi\) is bounded and uniformly continuous, and
\[
 \partial^\beta(K_t*\phi)(x)-\partial^\beta\phi(x)
 =\int_{\mathbb R^d}K_1(z)
       [\partial^\beta\phi(x-\sqrt t\,z)-\partial^\beta\phi(x)]\,dz.
\]
Split at \(|z|=M\). The tail is at most
\(2\|\partial^\beta\phi\|_\infty\int_{|z|>M}K_1\), tending to zero as \(M\to\infty\). On the inner set uniform continuity makes the difference uniformly small as \(t\downarrow0\). Thus convergence holds uniformly for every derivative.

Compact parameter integration through \(T\), justified by U021 B1 with a fixed cutoff on \(K\), now yields
\[
       0=\langle K_t*T,\phi\rangle
         =T(K_t*\phi)\longrightarrow T(\phi).
\]
The even Gaussian accounts for the reflected argument. Its derivatives on the product of \(K\) and the compact \(\phi\)-support are bounded, so the parameter interchange has precisely the common finite-order bound required there. All tests have zero pairing. \(\square\)

**Theorem 1.3 (compact multiindex primitives).** For \(f\in\mathcal E'(\mathbb R^n)\) and \(\alpha\in\mathbb N_0^n\), a compact solution of \(\partial^\alpha u=f\) exists exactly when
\[
             \langle f,x^\beta\rangle=0
                   \quad\text{for every }\beta\not\ge\alpha.
\]
The inequality is coordinatewise. The compact solution is unique and lies in every closed coordinate box containing \(\operatorname{supp}f\). For \(\alpha=0\), the condition is empty and \(u=f\).

**Proof.** Transposition proves necessity: if \(\beta_j<\alpha_j\), then \(\partial^\alpha x^\beta=0\), and the sign is \((-1)^{|\alpha|}\).

For an active coordinate \(j\), form the compact distribution on the remaining coordinates
\[
 M_{j,\ell}(f)(\psi)=f(x_j^\ell\psi(x_{\widehat j})),
                           \qquad 0\le\ell<\alpha_j.
\]
A fixed cutoff near \(\operatorname{supp}f\) defines the action, bounds its order, and puts its support in the projection of that compact set. Every polynomial moment of this distribution vanishes by hypothesis. Lemma 1.2, including its dimension-zero case, gives \(M_{j,\ell}(f)=0\).

Suppose \(\operatorname{supp}f\subset B=\prod[L_i,R_i]\). Convolve with
\[
                 G_j=A_{\alpha_j}(x_j)\otimes\delta_0(x_{\widehat j}).
\]
Then \(\partial_j^{\alpha_j}(G_j*f)=f\). Support addition preserves the bounds in all other coordinates and the lower bound \(L_j\). On the region \(x_j>R_j\), the positive-part kernel is an ordinary polynomial in \(x_j-y_j\). Its binomial expansion, paired with the compact input, is the distribution-valued function
\[
 \sum_{\ell=0}^{\alpha_j-1}
       \frac{(-1)^\ell x_j^{\alpha_j-1-\ell}}
            {\ell!(\alpha_j-1-\ell)!}\,M_{j,\ell}(f).
\]
This is zero. The formula also holds on joint tests, by the compact parameter-pairing identity in U021 B1; the transverse delta simply identifies the other coordinates. Hence the primitive is supported in \(B\).

Repeat this integration in each active coordinate. To justify that the next moments still vanish, let \(g=G_i*f\) be the compact result of one step and \(j\ne i\). Pairing compactly in coordinate \(j\) commutes with derivatives in \(i\), so
\[
       \partial_i^{\alpha_i}M_{j,\ell}(g)=M_{j,\ell}(f)=0.
\]
The left input is compact on the remaining coordinates. Lemma 1.1 makes it zero. Thus each successive step retains every still-needed partial moment and remains in \(B\). Commuting coordinate derivatives proves that the final primitive solves the stated equation. Two compact solutions differ by a distribution satisfying the product equation; choose lower bounds for its compact support and apply Lemma 1.1. Empty forcing and degenerate boxes cause no change to this argument. \(\square\)

**Theorem 1.4 (all scalar constant-coefficient ODEs).** For a complex polynomial \(P\) and \(f\in\mathcal E'(\mathbb R)\), a compact solution of \(P(\partial)u=f\) exists if and only if
\[
       \langle f,\phi\rangle=0
          \quad\text{for every smooth }\phi\text{ with }P(-\partial)\phi=0.
\]
For \(P\ne0\), the compact solution is unique and supported in the smallest closed interval containing \(\operatorname{supp}f\).

**Proof.** The compact transpose identity is
\(\langle P(\partial)u,\phi\rangle=\langle u,P(-\partial)\phi\rangle\), with no complex conjugation. Take cutoffs equal to one on a common neighborhood of the support; their derivatives contribute zero there. This proves necessity.

Let \(P(z)=\sum_{j=0}^m a_jz^j\), \(m\ge1,a_m\ne0\). Define its companion matrix \(A\) with superdiagonal ones and last row \((-a_0/a_m,\ldots,-a_{m-1}/a_m)\), and \(b=e_m/a_m\). Use, for example, the maximum row-sum matrix norm; summing products gives \(\|BC\|\le\|B\|\|C\|\). The series
\[
                         F(x)=e^{xA}=\sum_{\ell\ge0}x^\ell A^\ell/\ell!
\]
and every derivative converge uniformly on bounded intervals by the corresponding scalar exponential series. Hence \(F'=AF=FA\), \(F(0)=I\), and \((F(-x)F(x))'=0\) gives \(F(-x)F(x)=I\). Differentiating \(F(x+t)F(-t)\) in \(t\) likewise gives \(F(x+t)=F(x)F(t)\).

For \(G=HFb\), the proved step derivative and product rule yield \(G'=AG+b\delta_0\). Thus \(Y=G*f\) satisfies \(Y'=AY+bf\). Its first \(m-1\) rows give \(Y_j=\partial^{j-1}Y_1\); the last gives \(P(\partial)Y_1=f\).

If \(\operatorname{supp}f\subset[L,R]\), then \(Y=0\) below \(L\). Above \(R\), compact smooth-kernel pairing and the exponential product identity give
\[
                 Y(x)=F(x)c,\qquad c=\langle f(t),F(-t)b\rangle.
\]
Every scalar component of \(F(-t)b\) is an adjoint null solution. To verify this without assuming a matrix-polynomial theorem, observe that \(e_1^TA^j=e_{j+1}^T\) for \(0\le j<m\), and the last row gives \(e_1^TP(A)=0\). Multiplying by \(A^{j-1}\) and using its commutation with \(P(A)\) proves \(e_j^TP(A)=0\) for every row, so \(P(A)=0\). Therefore
\[
                       P(-\partial_t)F(-t)b=P(A)F(-t)b=0.
\]
The moment hypothesis gives \(c=0\), making \(u=Y_1\) compact in \([L,R]\).

For uniqueness, a homogeneous distributional solution \(w\) has companion vector \(W=(w,\partial w,\ldots,\partial^{m-1}w)^T\) satisfying \(W'=AW\). The product rule gives \((F(-x)W)'=0\), so U032, Lemma 1.3, gives a constant vector \(d\). Thus \(W=F(x)d\). If \(w\) is compact, this vector is zero on an exterior interval; invertibility forces \(d=0\). Applying the same support conclusion to every containing interval gives the stated smallest interval. For zero forcing uniqueness gives the zero solution.

For nonzero constant \(P=a_0\), the solution is \(f/a_0\) and the adjoint null space is zero. For \(P=0\), the moment condition against all smooth functions says \(f=0\); exactly then every compact \(u\) solves the equation. This covers repeated and nonreal roots without factorization. \(\square\)

## A rough kernel can detect smoothness

**Theorem 2.1 (one input used twice).** If \(u\in\mathcal D'(\mathbb R)\) and, for a fixed \(k\ge0\), \(u*f*f\) is smooth for every \(f\in C_c^k(\mathbb R)\), then \(u\) is smooth.

**Proof.** Set \(m=k+2\) and choose a smooth compact cutoff \(\chi=1\) near zero. The function \(h=\chi A_m\) belongs to \(C_c^{m-2}=C_c^k\). Leibniz' rule and \(A_m^{(m)}=\delta_0\) give
\[
 h^{(m)}=\delta_0+r,\qquad
 r=\sum_{\ell=1}^m\binom m\ell\chi^{(\ell)}A_m^{(m-\ell)}
                                               \in C_c^\infty.
\]
Each term in \(r\) is supported away from zero, where the remaining positive-part derivatives are smooth. In the term \(\ell=0\), \(\chi\delta_0=\delta_0\).
All convolutions below are proper because the two kernel factors are compact. The exact identities in U021 therefore give
\[
        \partial^{2m}(u*h*h)=u*(\delta_0+r)*(\delta_0+r)
                           =u+2u*r+u*r*r.
\]
The left side is smooth by hypothesis. The last two terms are smooth because they have compact smooth kernel factors. Solving this equality for \(u\) proves the assertion, including \(k=0\). \(\square\)

**Theorem 2.2 (continuous repeated mixed derivatives).** If \(u\in\mathcal E'(\mathbb R^n)\) and \((\partial_1\cdots\partial_n)^ku\) is continuous for every integer \(k\ge1\), then \(u\in C_c^\infty\).

**Proof.** Denote that continuous function by \(f_k\). Its distributional support is contained in \(\operatorname{supp}u\); continuity makes it zero on the complement, so \(f_k\) is compactly supported. Let
\[
 B_k(x)=\prod_{j=1}^n A_k(x_j),\qquad v_k=B_k*f_k.
\]
Tensor differentiation gives \((\partial_1\cdots\partial_n)^kB_k=\delta_0\). Both \(v_k\) and \(u\) have lower coordinate support bounds: for \(v_k\) this follows from its explicit integral
\[
 v_k(x)=\int_{\{y_j\le x_j\}}
          \prod_{j=1}^n\frac{(x_j-y_j)^{k-1}}{(k-1)!}\,f_k(y)\,dy.
\]
Their difference solves the homogeneous mixed equation, so Lemma 1.1 gives \(v_k=u\).

For \(\alpha_j\le k-1\), differentiating the successive one-dimensional integrals yields
\[
 \partial^\alpha v_k(x)=\int_{\{y_j\le x_j\}}
       \prod_{j=1}^n
        \frac{(x_j-y_j)^{k-1-\alpha_j}}{(k-1-\alpha_j)!}\,f_k(y)\,dy.
\]
At every differentiation a positive power reaches at worst zero; its preceding endpoint value is zero, so no boundary term occurs. On bounded \(x\)-sets the compact \(y\)-support and bounded polynomial factors give one integrable majorant. The integration indicators converge off finitely many coordinate hyperplanes, which have measure zero. Dominated convergence proves continuity of every displayed derivative. The one-dimensional fundamental theorem at each step then identifies them as classical derivatives. For any \(N\), take \(k=N+1\); all multiindices of total order at most \(N\) are permitted. Hence \(u\in C^N\) for every \(N\), with its original compact support. \(\square\)

## Look at the potential outside its source

The exact sources \(\Phi_2(z)=(2\pi)^{-1}\log|z|\) and \(\Phi_3(x)=-1/(4\pi|x|)\) satisfy \(\Delta\Phi_n=\delta_0\), by [U020](point-sources-and-complex-gaussian-kernels.md), Theorem 1.1. [U031](fundamental-solutions-continuation-and-approximation.md), Proposition 1.1 and Theorem 1.2, proves both compact inverse identities and that a distribution harmonic on an open set is smooth there.

**Theorem 3.1 (both complex moment families).** For \(f\in\mathcal E'(\mathbb R^2)\), a compact solution of \(\Delta u=f\) exists exactly when
\[
                    f(z^j)=f(\bar z^j)=0,\qquad j=0,1,2,\ldots.
\]
It is unique. The forcing may be complex, so the two families are separate conditions.

**Proof.** Necessity follows by transposition, since both polynomial families are harmonic. For sufficiency put \(u=\Phi_2*f\). Choose \(R>0\) with \(\operatorname{supp}f\subset\{|w|<R\}\). When \(|z|>2R\), the scalar logarithmic series gives
\[
 \log|z-w|=\log|z|
    -\frac12\sum_{j\ge1}\frac{w^jz^{-j}+\bar w^j\bar z^{-j}}j.
\]
The logarithmic series and its identification with the real logarithm follow from the exponential-series argument in U020, Corollary 1.2. On a fixed slightly enlarged input neighborhood still inside \(|w|<|z|\), each derivative introduces only a polynomial factor in \(j\); the geometric ratio stays below one. The series therefore converges in the finite derivative norm controlling \(f\). Pairing term by term gives zero. Smooth compact-kernel evaluation identifies this pairing with the potential outside the source, so \(u=0\) for \(|z|>2R\), and \(u\) is compact.

If \(w\) is a compact null solution, the compact inverse identity immediately gives \(w=\Phi_2*(\Delta w)=0\). Thus uniqueness does not require an additional energy or maximum theorem. Because pairings are complex-linear, conjugation of a moment of \(f\) would instead give a moment of its conjugate distribution; it cannot replace the second family here. \(\square\)

**Theorem 3.2 (the exact Newton far field).** Suppose \(V\in\mathcal D'(\mathbb R^3)\) is harmonic outside a compact set, and its smooth exterior representative tends to zero at infinity. Then \(f=\Delta V\) is compact and
\[
               -4\pi|x|V(x)\longrightarrow \langle f,1\rangle
                             \quad (|x|\to\infty),
\]
uniformly in direction.

**Proof.** Put \(W=\Phi_3*f\). On any fixed compact neighborhood \(K\) of the input support, homogeneity of differentiated kernels gives, uniformly for large \(|x|\),
\[
      \sup_{y\in K}|\partial_y^\beta\Phi_3(x-y)|
                           \le C_{\beta,K}|x|^{-1-|\beta|}.
\]
Indeed \(|x-y|\ge|x|/2\) and each derivative has the stated degree and bounded spherical profile. The compact finite-order bound gives \(W(x)=O(|x|^{-1})\). The difference \(h=V-W\) is globally harmonic, hence smooth by U031. It tends to zero at infinity. The maximum principle in [U023](positive-derivatives-and-canonical-representatives.md), Theorem 3.4, applied on balls to \(\operatorname{Re}h,-\operatorname{Re}h,\operatorname{Im}h,-\operatorname{Im}h\), bounds every fixed value by the boundary supremum on arbitrarily large spheres. These tend to zero, so \(h=0\).

Uniformly on \(K\), \(|x|/|x-y|\to1\). The positive-order bounds above tend to zero after multiplication by \(|x|\). Hence
\[
                  |x|\Phi_3(x-\cdot)\longrightarrow-1/(4\pi)
                         \quad\text{in every }C^N(K).
\]
Pair with \(f\) to get the claimed limit and its sign. Decay is essential: \(V=1\) has \(f=0\) but the rescaled potential diverges. \(\square\)

## Sources hidden by an ordinary formula

**Theorem 4.1 (a quadratic spherical principal value).** Let \(A=(a_{jk})\) be a complex symmetric \(3\)-by-\(3\) matrix, and \(q(x)=x^TAx/|x|^5\) for \(x\ne0\). The limit of the pairings over \(|x|>\varepsilon\) exists as a distribution exactly when \(\operatorname{tr}A=0\). For that trace-free case, \(F=\operatorname{pv}q\) satisfies
\[
 \Delta F=-\frac{4\pi}{3}\sum_{j,k=1}^3a_{jk}\partial_j\partial_k\delta_0,
                         \qquad F=\Phi_3*(\Delta F).
\]
The sum is the full double sum, so both equal off-diagonal entries contribute.

**Proof.** [U028](radial-sources-and-quadratic-logarithms.md), Solution 8, proves by spherical excision and integration by parts the precise identity
\[
 \partial_j\partial_k\Phi_3
 =\operatorname{pv}\frac{\delta_{jk}|x|^2-3x_jx_k}{4\pi|x|^5}
                       +\frac{\delta_{jk}}3\delta_0.
\]
The same proof establishes the spherical moments
\(\int_{\mathbb S^2}\omega_j\omega_k\,d\sigma=(4\pi/3)\delta_{jk}\): reflections kill the off-diagonal moments, permutations equalize the diagonal ones, and their sum is the sphere area \(4\pi\). Consequently
\[
             \int_{\mathbb S^2}q(r\omega)\,d\sigma(\omega)
                         =\frac{4\pi}{3}r^{-3}\operatorname{tr}A.
\]

If this trace is nonzero, a test equal to one near zero has truncated pairing with term \((4\pi/3)\operatorname{tr}A\log(1/\varepsilon)\), which cannot converge. If the trace is zero, subtract the test's value at zero within the unit ball. The segment fundamental theorem bounds the difference by \(r\|\nabla\phi\|_\infty\); multiplication by the degree-\(-3\) kernel and polar volume gives the integrable bound \(C\|\nabla\phi\|_\infty\,dr\). Outside that ball, up to the fixed test radius \(R\), the bound is \(C\|\phi\|_\infty\,dr/r\). These bounds prove existence and distributional continuity for exactly spherical truncations.

Contract the proved Hessian identity with \(A\). Both terms involving its trace vanish, leaving
\[
                    \sum_{j,k}a_{jk}\partial_j\partial_k\Phi_3
                                        =-\frac3{4\pi}F.
\]
Apply \(\Delta\) and use the normalized point source to obtain the first assertion. Convolving that compact point-jet source with \(\Phi_3\), and moving the derivatives to the kernel, recovers the displayed identity and hence \(F\). \(\square\)

**Theorem 4.2 (the entire potential of a quadratic cut).** On \(\Omega=\mathbb C\setminus[-1,1]\), there is a unique holomorphic \(f\) such that
\[
                    f^2-2zf+1=0,\qquad |f|>1.
\]
It has \(f(2)>1\), and \(f=z+S\) where \(S^2=z^2-1\) and \(S(z)/z\to1\) at infinity. The positive harmonic function \(\log|f|\) extends continuously by zero on the interval. Denote this nonnegative extension by \(g\). Its source and full potential are
\[
 \mu=\Delta g=\frac{2\,1_{(-1,1)}(x)}{\sqrt{1-x^2}}\,dx\otimes\delta_0(dy),
            \qquad (\Phi_2*\mu)(z)=g(z)-\log2
                                      \quad\text{for every }z\in\mathbb C.
\]
There are no endpoint atoms or other endpoint-supported terms.

**Proof: root and boundary.** The two quadratic roots have product one. Existence of the two roots uses only a square root of the nonzero complex number \(z^2-1\), obtained by halving a polar argument. A root \(w\) has \(|w|=1\) only if \(z=(w+w^{-1})/2=\operatorname{Re}w\in[-1,1]\). Off this interval the roots are distinct and neither lies on the circle; exactly one has modulus greater than one. [U025](zero-hypersurfaces-as-curvature-measures.md), Lemma 2.1, proves a holomorphic local root near each simple root. The unique exterior-modulus choices agree on overlaps, giving the required global function. On \(z>1\) it is \(z+\sqrt{z^2-1}\). The identity \(f+f^{-1}=2z\) gives \(f/(2z)\to1\), since \(|f^{-1}|<1\), and hence \(S=f-z\) has the asserted asymptotic. Differentiation gives \(f'/f=1/S\).

The local logarithm proof in U020, Corollary 1.2, shows that \(\log|f|\) is harmonic. For any sequence approaching the cut, the equation bounds \(|f|\le2|z|+1\); every limiting root over a cut point lies on the unit circle. Thus \(\log|f|\to0\), including at both endpoints, proving continuity.

Over a compact interior part of the cut, the two simple local roots continue smoothly from each side. Their \(S\)-limits are \(+i\sqrt{1-x^2}\) above and \(-i\sqrt{1-x^2}\) below. To fix the signs, at \(z=iy\), \(y>0\), the exterior root is \(i(y+\sqrt{1+y^2})\); continuity along the connected interior interval keeps the sign, and complex conjugation, which preserves the defining exterior choice, gives the lower sign. Since \(\partial_y\log|f|=\operatorname{Re}(if'/f)\), the normal derivatives are
\[
                (\partial_yg)_+=(1-x^2)^{-1/2},
                    \qquad(\partial_yg)_-=-(1-x^2)^{-1/2}.
\]
U011, Theorem 2.1 and Corollaries 2.2 and 2.4, supplies Green's formula on the two sides, including the finitely many boundary corners. Their equal zero function traces cancel the terms with derivatives of the test; the difference of the normal derivatives gives exactly the positive density in the statement.

At \(p=\pm1\), \(S^2=(z-p)(z+p)\) implies \(S=O(|z-p|^{1/2})\), so \(f=p+O(|z-p|^{1/2})\), \(g=O(|z-p|^{1/2})\), and \(|\nabla g|=|S|^{-1}=O(|z-p|^{-1/2})\). The logarithm bound follows from its bounded derivative near modulus one. Excise circles of radius \(\varepsilon\) about the endpoints before applying Green's formula. Their two error bounds are \(C\varepsilon^{3/2}\|\nabla\phi\|_\infty\) and \(C\varepsilon^{1/2}\|\phi\|_\infty\), both tending to zero. The cut density is integrable at the endpoints. Passing to the limit on every test proves the full distribution identity, with no additional endpoint term. Substitution \(x=\cos\theta\) gives total mass \(2\pi\).

**Proof: potential, including the cut.** The proposed ordinary integral is
\[
 W(z)=\frac1\pi\int_{-1}^1\frac{\log|z-t|}{\sqrt{1-t^2}}\,dt
     =\frac1\pi\int_0^\pi\log|z-\cos\theta|\,d\theta.
\]
The scalar substitution follows first away from the endpoints by the fundamental theorem, then for nonnegative parts by monotone convergence. We now prove absolute integrability also at its possible logarithmic singularities.

For \(z\notin[-1,1]\), put \(w=f(z)\). The algebraic factorization
\[
     z-\cos\theta
       =\frac w2(1-w^{-1}e^{i\theta})(1-w^{-1}e^{-i\theta})
\]
and \(|w^{-1}|<1\) allow the uniformly absolutely convergent series
\[
          \log|1-ae^{i\theta}|
                 =-\operatorname{Re}\sum_{j\ge1}\frac{a^je^{ij\theta}}j.
\]
The two angular terms together integrate over a full circle. Each exponential of positive integer frequency has zero integral, by its scalar primitive, so their combined integral is zero. This gives \(W(z)=\log|w|-\log2\).

For \(z\) on the cut, choose either root \(w\) of modulus one, so the same factorization holds. Its factors may have angular zeros. The necessary endpoint passage is elementary:
\[
               |1-re^{is}|^2=(1-r)^2+2r(1-\cos s).
\]
For \(r\ge1/2\) and small \(|s|\), the right side is at least \(c s^2\). Indeed \(1-\cos s=2\sin^2(s/2)\), and \(\sin t/t\to1\) follows by integrating the continuous cosine. The positive logarithm is bounded by \(\log2\), while the negative part is bounded by \(C+|\log|s||\). The integral of this bound on \(|s|<\delta\) tends to zero, since it is at most \(C\delta(1+|\log\delta|)\), by the scalar logarithmic primitive. Away from those neighborhoods convergence as \(r\uparrow1\) is uniform. Thus the full-circle logarithmic mean stays zero for \(|a|=1\), and every angular integral is absolutely finite. At an endpoint the two angular zeros can coincide, but the sum of the two integrable bounds still applies. The factorization yields \(W=-\log2=g-\log2\) at every cut point.

Finally, this ordinary potential represents the distributional convolution: for a compact output set the integral of \(|\log|z-t||\) in \(z\) is uniformly bounded for \(-1\le t\le1\), by translation into one fixed ball and planar polar integration near zero. Tonelli with the finite positive measure \(\mu\) justifies pairing and Fubini. This identifies \(\Phi_2*\mu\) with \(W\), completing the pointwise and distributional conclusions. \(\square\)

## A positive kernel measures quadrature error

**Theorem 5.1 (two-node positive error kernel).** For \(0<a<1\), the equation
\[
                      u^{(4)}=1_{(-1,1)}-\delta_a-\delta_{-a}
\]
has a compact \(C^2\) solution exactly when \(a=1/\sqrt3\). That solution is unique, is positive on \((-1,1)\), and has integral \(1/135\). For every complex \(F\in C^4([-1,1])\),
\[
       \int_{-1}^1F(x)\,dx-F(a)-F(-a)
                       =\int_{-1}^1u(t)F^{(4)}(t)\,dt,
\]
so the absolute error is at most \(\|F^{(4)}\|_\infty/135\), with sharp constant.

**Proof.** A compact fourth derivative annihilates monomials of degree at most three. The second moment of the forcing is \(2/3-2a^2\), so \(a=1/\sqrt3\) is necessary. At this value its zeroth and odd moments vanish as well.

We derive the kernel from the finite Taylor remainder, following the Peano-kernel method and proving its required steps. Four repeated applications of the scalar fundamental theorem give
\[
       F(x)=\sum_{j=0}^3\frac{F^{(j)}(-1)}{j!}(x+1)^j
                     +\int_{-1}^1\frac{(x-t)_+^3}{6}F^{(4)}(t)\,dt.
\]
For a direct verification, differentiate the right side up to four times on \([-1,1]\); it has fourth derivative \(F^{(4)}\) and the same first four initial jets. The difference has fourth derivative zero and all four initial values zero, so integrating backward through those derivatives gives zero.

Let \(E(F)=\int_{-1}^1F-F(a)-F(-a)\). Its action on the polynomial part is zero. Fubini for continuous bounded integrands on the compact square gives
\[
 E(F)=\int_{-1}^1 K(t)F^{(4)}(t)\,dt,\qquad
 K(t)=\frac{(1-t)^4}{24}
          -\frac{(a-t)_+^3+(-a-t)_+^3}{6},\quad -1\le t\le1.
\]
This is an explicit derivation of the error identity for the stated \(C^4\) functions.

Define on the whole line
\[
 u(t)=\frac{(1-t)_+^4-(-1-t)_+^4}{24}
                -\frac{(a-t)_+^3+(-a-t)_+^3}{6}.
\]
For \(t>1\) it is zero. For \(t<-1\), polynomial expansion leaves
\((a^2-1/3)t=0\). On \([-1,1]\) it equals \(K\). Positive-part differentiation shows it is \(C^2\) and has exactly the asserted fourth derivative: the two reversed quartics give \(1_{(-1,1)}\), and each reversed cubic has fourth derivative \(+\delta\), with the prefixed minus sign retained. Thus this is a compact solution. Lemma 1.1 proves uniqueness; reflection preserves the forcing, so \(u\) is even.

For \(a\le t<1\), \(24u(t)=(1-t)^4>0\). For \(0\le t\le a\), expand using \(a^2=1/3\):
\[
            24u(t)=1-\frac{4a}{3}+(6-12a)t^2+t^4.
\]
Its derivative is \(t(12-24a+4t^2)\). Since \(t^2\le1/3\), the bracket is at most \(40/3-8\sqrt3<0\); the latter inequality follows by squaring \(40<24\sqrt3\), namely \(1600<1728\). Thus \(u\) decreases on \([0,a]\) and is at least its positive value \(u(a)=(1-a)^4/24\). Evenness proves positivity throughout the interior.

Compact transposition against \(t^4\) gives
\[
        24\int u=\langle u^{(4)},t^4\rangle
                       =\frac25-2a^4=\frac8{45}.
\]
Therefore \(\int u=1/135\). The already proved error identity and positivity yield the bound for complex \(F\) as well. Equality holds for \(F(x)=x^4\), whose error is \(8/45\) and fourth derivative is \(24\). This proves sharpness. \(\square\)

## Exercises

**Exercise 1 (basic).** Find the compact distribution \(u\) with \(u'=\delta_{-2}-\delta_3\), and prove uniqueness. Explain why \(u'=\delta_0+\delta_1\) has no compact solution.

**Exercise 2 (basic).** For
\[
                 A=\begin{pmatrix}1&2&0\\2&-1&0\\0&0&0\end{pmatrix},
\]
write the principal value \(F\) and its complete point-jet Laplacian. What happens if \(A\) is replaced by \(A+\lambda I\), with \(\lambda\in\mathbb C\)?

**Exercise 3 (intermediate).** For arbitrary complex \(\lambda\), solve
\[
      (\partial-\lambda)^2u
                    =\delta_0-2e^\lambda\delta_1+e^{2\lambda}\delta_2
\]
with compact support. Derive the two adjoint moment conditions and determine every coefficient triple on the same three points that permits a compact solution.

**Exercise 4 (intermediate).** Set
\[
                f=(\delta_{-1}'-\delta_1')\otimes(\delta_0-\delta_2).
\]
Find the compact solution of \(\partial_x^2\partial_yu=f\) and verify every excluded monomial moment. Show why requiring only moments of total degree below three to vanish would be insufficient.

**Exercise 5 (intermediate).** Put \(z=x+iy\) and \(f=(\partial_x+i\partial_y)\delta_0\). Compute all \(\langle f,z^j\rangle\) and \(\langle f,\bar z^j\rangle\). Does \(f\) admit a compact Laplace solution? Compare \(g=\Delta\delta_a\), for arbitrary \(a\in\mathbb R^2\).

**Exercise 6 (intermediate).** In \(\mathbb R^3\), let \(a=(2,-1,0)\), \(b=(-1,1,3)\), and
\[
                         V(x)=\Phi_3(x-a)-\Phi_3(x-b).
\]
Compute its forcing and monopole limit. Find the limit of \(-4\pi R^2V(R\omega)\), uniformly for \(|\omega|=1\). Explain what adding a constant changes.

**Exercise 7 (advanced).** For real \(t\), compute the two-node quadrature error for \(F(x)=e^{tx}\). Prove its sign, an explicit bound and its first nonzero Taylor coefficient at \(t=0\). Transfer the complete kernel and sharp error estimate to \([c-R,c+R]\), with \(R>0\).

**Exercise 8 (advanced).** Let \(c\in\mathbb C\), \(R>0\), \(\theta\in\mathbb R\), and define \(g_R(z)=g((z-c)/(Re^{i\theta}))\), using Theorem 4.2. Find its source measure, total mass and full logarithmic potential. Evaluate the potential at the center and endpoints for \(c=1-2i\), \(R=3\), \(\theta=\pi/4\).

**Exercise 9 (advanced).** Prove that a finite sum of point masses at distinct planar points can be the Laplacian of a compact distribution only when all its coefficients vanish. Give a nonzero compactly supported point-jet forcing that does admit a compact solution.

**Exercise 10 (advanced).** In Theorem 2.1 take a compact smooth cutoff equal to one near zero and \(h(x)=\chi(x)x_+^{k+1}/(k+1)!\). Determine the exact formula for \(h*h\) near zero and its sharp differentiability class there. What does this show about the distinction between high finite regularity and smoothness of a double convolution?

## Complete solutions

**Solution 1.** Take \(u=1_{(-2,3)}\). Its derivative pairs with \(\phi\) as
\[
             -\int_{-2}^3\phi'(x)\,dx=\phi(-2)-\phi(3).
\]
Its compact support is \([-2,3]\); endpoint values do not affect the distribution. The difference of two compact solutions has zero derivative and is zero by Lemma 1.1. The forcing \(\delta_0+\delta_1\) has total mass two, whereas a compact derivative pairs with the constant function as zero. Thus the second equation has no compact solution.

**Solution 2.** The trace is zero, and the quadratic form is \(x_1^2-x_2^2+4x_1x_2\). Theorem 4.1 therefore gives
\[
 F=\operatorname{pv}\frac{x_1^2-x_2^2+4x_1x_2}{|x|^5},\qquad
 \Delta F=-\frac{4\pi}{3}
             (\partial_1^2-\partial_2^2+4\partial_1\partial_2)\delta_0.
\]
The coefficient four is the sum of both off-diagonal contributions. This source is nonzero: a test equal to \(x_1^2\) near zero gives \(-8\pi/3\). Its support is consequently exactly \(\{0\}\).
Replacing \(A\) by \(A+\lambda I\) adds \(\lambda|x|^{-3}\) to the ordinary kernel and changes the trace to \(3\lambda\). On a test equal to one near zero, the added truncated integral is \(4\pi\lambda\log(1/\varepsilon)\) plus a constant. A spherical principal value exists only for \(\lambda=0\), including complex \(\lambda\).

**Solution 3.** Substitution \(\phi=e^{-\lambda x}q\) changes the adjoint equation \((-\partial-\lambda)^2\phi=0\) into \(q''=0\). Scalar integration gives \(q=A+Bx\). Thus the required moments are against \(e^{-\lambda x}\) and \(xe^{-\lambda x}\). For \(f=\sum_{j=0}^2c_j\delta_j\), put \(d_j=c_je^{-\lambda j}\). The conditions become
\[
                     d_0+d_1+d_2=0,\qquad d_1+2d_2=0.
\]
Solving them gives precisely
\[
               (c_0,c_1,c_2)=C(1,-2e^\lambda,e^{2\lambda}),
                                           \qquad C\in\mathbb C.
\]
For \(C=1\), the solution is
\[
             u(x)=e^{\lambda x}
                    \bigl(x_+-2(x-1)_++(x-2)_+\bigr).
\]
The bracket is \(x\) on \([0,1]\), \(2-x\) on \([1,2]\), and zero elsewhere. It is continuous and its piecewise constant derivative has jumps \(1,-2,1\), so its second distributional derivative is \(\delta_0-2\delta_1+\delta_2\). The product rule
\((\partial-\lambda)(e^{\lambda x}v)=e^{\lambda x}v'\),
applied twice, proves the exact equation with the weighted masses. Its support is \([0,2]\). Multiplication by \(C\) gives every permitted forcing, and Theorem 1.4 proves compact uniqueness.

**Solution 4.** Direct interval integration by parts gives
\[
       \partial_x^2 1_{(-1,1)}=\delta_{-1}'-\delta_1',
                   \qquad \partial_y1_{(0,2)}=\delta_0-\delta_2.
\]
Hence the unique compact solution is \(u=1_{(-1,1)}\otimes1_{(0,2)}\), supported exactly in \([-1,1]\times[0,2]\). Tensor differentiation proves the equation and Theorem 1.3 proves uniqueness.

For \(x^ry^s\), the first pairing is zero at \(r=0\), and for \(r\ge1\) equals
\(-r((-1)^{r-1}-1)\); in particular it vanishes at \(r=1\). The second pairing is zero at \(s=0\) and equals \(-2^s\) for \(s\ge1\). Every moment with \(r<2\) or \(s<1\) therefore vanishes, exactly the coordinate exclusions. For comparison,
\[
                          \langle f,x^2y\rangle=4(-2)=-8.
\]
The weaker total-degree condition would incorrectly allow
\(\widetilde f=\partial_x^3\delta_{(0,0)}\). It kills every polynomial of total degree below three, but \(x^3\) is coordinatewise excluded because its \(y\)-degree is zero, and \(\langle\widetilde f,x^3\rangle=-6\). Theorem 1.3 rules out a compact \(\partial_x^2\partial_y\) primitive for this example.

**Solution 5.** The ordinary polynomial derivatives satisfy
\[
 (\partial_x+i\partial_y)z^j=0,\qquad
 (\partial_x+i\partial_y)\bar z^j=2j\bar z^{j-1}.
\]
Pairing a first derivative of a point mass changes the sign. Thus \(f(z^j)=0\) for all \(j\), while \(f(\bar z^j)=0\) except at \(j=1\), where it is \(-2\). The constant moment is zero in both families. Theorem 3.1 excludes a compact Laplace solution and demonstrates why the second family is necessary.
For \(g=\Delta\delta_a\), both families vanish by harmonicity. The solution is the compact distribution \(u=\delta_a\), uniquely by that theorem, and
\[
                \Phi_2*(\Delta\delta_a)
                        =(\Delta\Phi_2)*\delta_a=\delta_a.
\]
This last potential is a distribution; it need not have pointwise function values.

**Solution 6.** The forcing is \(\delta_a-\delta_b\), with zero total mass. The potential decays, so its monopole limit is zero by Theorem 3.2. For the next term, write
\[
 |R\omega-y|^{-1}
     =R^{-1}(1+s)^{-1/2},\qquad
 s=-2\omega\cdot y/R+|y|^2/R^2.
\]
For bounded \(y\), \(s=O(R^{-1})\) uniformly on the unit sphere. The second derivative of \(H(s)=(1+s)^{-1/2}\) is bounded on \([-1/2,1/2]\). Twice the fundamental theorem gives
\[
 H(s)=H(0)+sH'(0)+s^2\int_0^1(1-t)H''(ts)\,dt
                          =1-\tfrac12s+O(s^2).
\]
The bound is uniform for both signs of \(s\), so
\[
       |R\omega-y|^{-1}
             =R^{-1}+(\omega\cdot y)R^{-2}+O(R^{-3}).
\]
Subtract the expansions for \(a,b\) and keep the negative Newton normalization. It follows uniformly that
\[
        -4\pi R^2V(R\omega)\longrightarrow\omega\cdot(a-b)
                                 =3\omega_1-2\omega_2-3\omega_3.
\]
A nonzero added constant changes no forcing but destroys decay and introduces a divergent term in both rescaled expressions.

**Solution 7.** Define \(\sinh t=(e^t-e^{-t})/2\) and \(\cosh t=(e^t+e^{-t})/2\). Integration gives
\[
 E(t)=2\sinh(t)/t-2\cosh(t/\sqrt3)\quad(t\ne0),
                              \qquad E(0)=0.
\]
The proved error identity expresses this also as
\[
                   E(t)=t^4\int_{-1}^1u(x)e^{tx}\,dx.
\]
For real \(t\ne0\), strict positivity of \(u\) on the interior gives \(E(t)>0\), and
\(0\le E(t)\le t^4e^{|t|}/135\). The exponential series gives zero constant and quadratic coefficients; the quartic coefficient is
\[
                   2\left(\frac1{120}-\frac1{216}\right)=\frac1{135}.
\]
The function is even and its series converges absolutely on bounded \(t\)-sets, so the remaining terms are \(O(t^6)\). Thus \(E(t)=t^4/135+O(t^6)\).

For a real interval center \(c\), put \(U_R(x)=R^4u((x-c)/R)\). It is compact \(C^2\), positive on \((c-R,c+R)\), and the distributional change of variable gives
\[
 U_R^{(4)}
        =1_{(c-R,c+R)}
              -R\delta_{c-R/\sqrt3}-R\delta_{c+R/\sqrt3}.
\]
The mass is \(R^5/135\). To verify both the point-mass factors and the error identity directly, apply Theorem 5.1 to \(F(s)=f(c+Rs)\), whose fourth derivative is \(R^4 f^{(4)}(c+Rs)\), and multiply by \(R\). The result is
\[
 \begin{aligned}
 \int_{c-R}^{c+R}f(x)\,dx
   -R f(c-R/\sqrt3)-R f(c+R/\sqrt3)
             &=\int_{c-R}^{c+R}U_R(x)f^{(4)}(x)\,dx .
 \end{aligned}
\]
Its absolute value is at most \(R^5\|f^{(4)}\|_\infty/135\). Equality for \(f(x)=(x-c)^4\) proves that the scaled constant is sharp.

**Solution 8.** Let \(T(s)=c+Re^{i\theta}s\). The source is the pushforward of \(\mu\):
\[
       \langle\mu_R,\phi\rangle
                  =2\int_{-1}^1
                    \frac{\phi(c+Re^{i\theta}s)}{\sqrt{1-s^2}}\,ds.
\]
Indeed in \(\langle g_R,\Delta\phi\rangle\), the planar affine change of variable has Jacobian \(R^2\), while
\(\Delta_\zeta(\phi(c+Re^{i\theta}\zeta))=R^2(\Delta_z\phi)(c+Re^{i\theta}\zeta)\), by the chain rule and orthogonality of rotation. Their cancellation gives exactly the displayed pairing with \(\mu\). The mass remains \(2\pi\); arclength on the segment is \(R\,ds\), so the density with respect to arclength is \(2/(R\sqrt{1-s^2})\), with no endpoint atoms.

For \(z=c+Re^{i\theta}\zeta\), the pointwise finite potential satisfies
\[
 \begin{aligned}
 (\Phi_2*\mu_R)(z)
   &=\frac1{2\pi}\int\bigl(\log R+\log|\zeta-s|\bigr)\,d\mu(s)\\
   &=\log R+g(\zeta)-\log2
    =g_R(z)+\log R-\log2 .
 \end{aligned}
\]
Theorem 4.2 proves absolute finiteness even at the center and endpoints, so this calculation includes those points. For the specified values they are \(1-2i\) and
\[
                         1-2i\ \pm\frac3{\sqrt2}(1+i).
\]
At each one \(g_R=0\), and the potential is \(\log(3/2)\).

**Solution 9.** Write \(f=\sum_{j=1}^m c_j\delta_{z_j}\) with distinct \(z_j\). A compact Laplace primitive forces every holomorphic polynomial moment to vanish. For each \(j\), the polynomial
\[
                      L_j(z)=\prod_{\ell\ne j}
                                    \frac{z-z_\ell}{z_j-z_\ell}
\]
has \(L_j(z_\ell)=\delta_{j\ell}\). All denominators are nonzero, so \(0=f(L_j)=c_j\). For \(m=1\) the product is one; the empty sum is already zero. The zero forcing has the unique compact zero solution.

In contrast \(f=\Delta\delta_0\) is a nonzero point-jet forcing with compact solution \(u=\delta_0\). It is nonzero because a test equal to \(x^2\) near zero pairs as \(2\). Both moment families vanish since the corresponding polynomials are harmonic. This distinguishes point jets from sums of undifferentiated point masses.

**Solution 10.** Since both factors vanish for negative arguments, \(h*h=0\) on the negative half-line. If \(x>0\) is sufficiently small, every contributing argument \(t,x-t\) belongs to the region where \(\chi=1\). Therefore
\[
             (h*h)(x)=\frac1{((k+1)!)^2}
                             \int_0^x t^{k+1}(x-t)^{k+1}\,dt.
\]
Here the integer beta coefficient has an elementary proof. For integers \(p,q\ge0\), write \(B(p,q)=\int_0^1s^p(1-s)^q\,ds\). If \(q\ge1\), integration by parts with primitive \(s^{p+1}/(p+1)\) gives
\[
                     B(p,q)=\frac q{p+1}B(p+1,q-1).
\]
Both boundary terms vanish. Iterating to \(B(p+q,0)=1/(p+q+1)\) yields \(B(p,q)=p!q!/(p+q+1)!\). With \(p=q=k+1\), substitution \(t=xs\) proves the exact local formula
\[
                         h*h=\frac{x_+^{2k+3}}{(2k+3)!}.
\]
Its derivatives through order \(2k+2\) are continuous across zero. The last of these is \(x_+\), whose left and right derivatives at zero are zero and one. Thus no classical derivative of order \(2k+3\) exists there: the sharp local class is \(C^{2k+2}\). The two inputs are smooth off zero; U021, Corollary 4.2, puts the singular support of their convolution inside \(\{0\}+\{0\}\), so it is smooth elsewhere.

For \(u=\delta_0\), the doubled output is exactly \(h*h\). Choosing large \(k\) makes its finite regularity arbitrarily high, but never smooth. This particular admissible \(h\) already violates the smooth-output hypothesis of Theorem 2.1; high finite regularity of selected doubled outputs cannot replace that hypothesis for every \(C_c^k\) input.

## Free sources and exact proof dependencies

The freely accessible notes of M. R. O'Donohoe, [*Numerical Analysis II*](https://help.uis.cam.ac.uk/system/files/documents/na2.pdf), Theorems 2.1–2.2, pages 18–19, give the integral Taylor remainder and Peano-kernel construction. Section 5 above proves the needed remainder, derives the actual two-node kernel, and establishes its positivity and sharp constant. The general Gaussian-quadrature assertions on page 21 are not prerequisites.

E. B. Saff's free author preprint [*Logarithmic Potential Theory with Applications to Approximation Theory*](https://arxiv.org/abs/1010.3760), Examples 1.10, 1.11 and 3.6, PDF pages 9–10 and 21, supplies the circle/interval potential formulas and quadratic inverse map. Section 4 proves the branch, source measure and entire potential directly, including the logarithmic angular limits at both endpoints. No conformal-mapping existence theorem or equilibrium-measure theorem is assumed.

V. Hnizdo's free preprint [*Generalized second-order partial derivatives of \(1/r\)*](https://arxiv.org/abs/1009.2480), version 2, pages 1–3, specifies the spherical regularization and contact term. The complete integration-by-parts proof used here is supplied in [U028](radial-sources-and-quadratic-logarithms.md), Solution 8, and its contraction is proved in Theorem 4.1. The other exact programme dependencies are the finite-order, Gaussian, convolution and constant-coordinate proofs named before Section 1; U020's normalized point sources and local logarithm; U031's compact inverse and local regularity; U023's maximum principle; U025's scalar implicit graph; and U011's flux and Green identities. Every solution above includes its additional calculation and proof.
