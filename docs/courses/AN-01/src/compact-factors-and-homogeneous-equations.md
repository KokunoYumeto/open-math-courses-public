# Compact factors and homogeneous equations

*Original edition by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Repaired and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Original exposition: public domain (CC0); supplied prerequisites retain their stated licences.*

Complex Fourier zeros determine which compact distributions on the line admit nontrivial convolution factors. We classify every distribution whose compact factorizations are trivial and construct an actual compact factor from any complex zero. In several dimensions, homogeneity makes polynomial null solutions dense in every smooth global null solution. The same polynomial moment condition characterizes compactly supported solutions of the forced equation. We prove the entire quotient convergence, its growth and its compact inverse transform, including complex coefficients, repeated factors and zero or constant symbols. Finite complex zero sets characterize point jets, compact solutions have the exact forcing hull, and polynomial approximations can preserve any finite compatible observations.

Our convention is \(Fu(\xi)=\int e^{-ix\cdot\xi}u(x)dx\), \(D=-i\partial\), and bilinear complex-linear distributional pairings. [Convolution as addition of supports](convolution-as-addition-of-supports.md), B0–B3 and Theorem1.1, supplies compact actions, locality, parameter pairing, convolution and differentiation. [Compact forcing, moments and positive error kernels](compact-forcing-moments-and-positive-error-kernels.md), Lemma1.2 and Theorem1.3, proves polynomial-moment detection and compact primitives. [Fundamental solutions, continuation and approximation](fundamental-solutions-continuation-and-approximation.md), B1–B2 and Lemma3.1, supplies smooth completeness, compact duality and separation, using the supplied [functional foundation](../prerequisites/U011-free-foundations/functional-foundations-U008.md), §5, for complex Hahn–Banach.

[Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Theorem1.1 and Corollary2.2, supplies Cauchy integration, Taylor series and coefficient estimates. Boundary flux and weak identities, Corollaries2.3–2.4, proves complex Green and its finite-corner form. The finite-order construction in the proof of [Sharp bounds for compact spectra](sharp-bounds-for-compact-spectra.md), Theorem3.1, applies to any compact distribution; its Lemma0.1 supplies the identity principle. The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves inversion and coordinate rules. The supplied [finite algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.5, proves basis extension, elimination and orthogonal coordinates; [scalar](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, and [integration](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15–16, foundations supply the calculus, convergence and substitution used below. We prove the needed polynomial factorization next.

## Polynomial roots from the Cauchy estimate

**Lemma 0.1 (complete one-variable factorization).** A nonzero complex polynomial of degree \(d\) is its leading coefficient times a product of \(d\) linear factors, with every root repeated according to its multiplicity. For \(d=0\) the product is empty.

**Proof.** First, a bounded entire function \(g\), with \(|g|\le M\), is constant. At any centre \(a\), the Cauchy coefficient estimate from U013, Corollary2.2, on every circle of radius \(R\) gives \(|g'(a)|\le M/R\). Let \(R\to\infty\); all first derivatives vanish. Integrating along each line segment by the scalar fundamental theorem shows that \(g\) is constant on the plane.

Suppose \(p(z)=a_dz^d+\cdots+a_0\), \(d\ge1\), has no zero. Its reciprocal is entire by the quotient derivative rule and U013, Corollary2.2. Since \(p(z)/(a_dz^d)\to1\) as \(|z|\to\infty\), choose \(R_0\) such that \(|p(z)|\ge |a_d||z|^d/2\) outside that disk. On the disk, continuity and nonvanishing give a positive minimum of \(|p|\). Thus \(1/p\) is bounded on the whole plane and tends to zero at infinity. The preceding argument makes it identically zero, contradicting \(p(0)(1/p(0))=1\). Hence a root \(r\) exists.

The finite telescoping identity
\[
 p(z)-p(r)=(z-r)\sum_{k=1}^d a_k
                         \sum_{j=0}^{k-1}z^{k-1-j}r^j
\]
divides out that root and leaves a degree-\(d-1\) polynomial with leading coefficient \(a_d\). Induction completes the factorization. At any root, the number of its occurrences in the product is exactly the first nonzero Taylor order, because all other factors are nonzero there. This proves the multiplicity statement and also the bound of \(d\) on the number of distinct roots. \(\square\)

## Every compact distribution with only trivial convolution factors

Call a factor trivial when it is a nonzero scalar multiple of a shifted point mass. A factorization is trivial when at least one of its factors is trivial. These are the units of the compact-distribution convolution algebra: \(c\delta_a\) has inverse \(c^{-1}\delta_{-a}\). Treating only the mass-one \(\delta_a\) as trivial would make scalar refactorizations of every nonzero input fail the intended condition; the algebraic unit convention makes that distinction explicit.

**Theorem 1.1.** A nonzero \(u\in\mathcal E'(\mathbb R)\) has only trivial convolution factorizations \(u=v*w\), \(v,w\in\mathcal E'(\mathbb R)\), if and only if
\[
\begin{gathered}
u=c\delta_a+d\delta_a',\\
a\in\mathbb R,\quad c,d\in\mathbb C,\\
(c,d)\ne(0,0).
\end{gathered}
\tag{1.1}
\]

**Every zero-free compact transform is a point mass.** For \(w\in\mathcal E'(\mathbb R)\), its entire Fourier transform
\[
W(z)=\langle w(x),e^{-izx}\rangle
\]
is justified by the same finite-order exponential-series construction as in [*Sharp bounds for compact spectra*](sharp-bounds-for-compact-spectra.md), formula (3.2), with the exponent sign changed and the inverse-transform normalization omitted. That argument uses only compact finite order for its entire construction and test interchange; the later norm estimates of that theorem are not required here. A compact cutoff supported in some \([-A,A]\) and the finite-order estimate give
\[
|W(z)|\le C(1+|z|)^N e^{A|\operatorname{Im}z|}.
\tag{1.2}
\]
The real restriction is the whole tempered Fourier transform, by the absolute finite-order test interchange already proved in [*Sharp bounds for compact spectra*](sharp-bounds-for-compact-spectra.md), Theorem 3.1. If \(w\ne0\), Fourier injectivity gives \(W\not\equiv0\).

Suppose \(W\) has no complex zeros. The entire function \(W'/W\) has, by [*Cauchy kernels and distributional boundary limits*](cauchy-kernels-and-boundary-limits.md)'s Cauchy coefficients, a Taylor series about zero that converges on every disk. Integrating that series termwise gives an entire primitive \(L\) with \(L(0)=0\). Choose a complex number \(b\) with \(e^b=W(0)\), using its nonzero polar form, and put \(J=b+L\). Differentiation shows that \(e^{-J}W\) is constant and its value at zero is one, so \(W=e^J\) on the whole plane.

Write \(J(z)=\sum_{k\ge0}a_kz^k\). Formula (1.2) implies
\[
\operatorname{Re}J(z)
\le\log C+N\log(1+|z|)+A|z|.
\]
For each \(R>1\), denote the right side at radius \(R\) by \(M_R\). On the circle \(Re^{i\theta}\), the real function
\(q_R(\theta)=M_R-\operatorname{Re}J(Re^{i\theta})\) is nonnegative. Uniform convergence of the Taylor series on this circle, obtained from any larger Cauchy circle, gives its mean \(M_R-\operatorname{Re}a_0\). For \(k\ge1\), the \(k\)-th positive Fourier coefficient of \(\operatorname{Re}J(Re^{i\theta})\) is \(a_kR^k/2\). Consequently
\[
\begin{gathered}
\frac{|a_k|R^k}{2}\\
\le\frac1{2\pi}\int_0^{2\pi}q_R(\theta)d\theta\\
=M_R-\operatorname{Re}a_0.
\end{gathered}
\tag{1.3}
\]
For every \(k\ge2\), let \(R\to\infty\); the right side is \(O(R+\log R)\), so \(a_k=0\). Therefore \(W(z)=C_0e^{a_1z}\), with \(C_0\ne0\). On the real axis (1.2) is merely a polynomial bound. Applying it in both directions \(x\to\infty\) and \(x\to-\infty\) forces \(\operatorname{Re}a_1=0\). Write \(a_1=-ia\), \(a\in\mathbb R\). Fourier injectivity now gives \(w=C_0\delta_a\). This proves the entire zero-free assertion, including the reality of the point location, without an unsupported entire-factorization theorem.

**A complex zero gives an actual compact factor.** Suppose \(U=Fu\) has a zero at \(z_0\in\mathbb C\). Set \(f=i e^{-iz_0x}u\), a compact distribution. Its total mass is \(iU(z_0)=0\). [*Compact forcing, moments and positive error kernels*](compact-forcing-moments-and-positive-error-kernels.md)'s complete compact-primitive theorem, with \(n=1\) and order one, produces a compact distribution \(R\) with \(R'=f\), supported in any closed interval containing the support of \(u\). Put \(v=e^{iz_0x}R\), still compact. The full distributional product rule gives
\[
(D-z_0)v
=-i e^{iz_0x}R'
=u.
\tag{1.4}
\]
Thus, with \(b_{z_0}=(D-z_0)\delta_0=-i\delta_0'-z_0\delta_0\),
\[
u=b_{z_0}*v.
\]
Compact-factor convolution and differentiation are the complete [*Convolution as addition of supports*](convolution-as-addition-of-supports.md) interfaces. The entire transform of \(b_{z_0}\) is \(z-z_0\), so this factor is not a unit. The factor \(v\) is nonzero because \(u\ne0\), and its entire transform is precisely the holomorphic quotient \(U(z)/(z-z_0)\), by (1.4). Compactness was proved directly by the moment theorem, rather than asserted from a growth theorem.

If every factorization of \(u\) is trivial, then either \(U\) is zero-free, in which case the preceding result gives \(u=C_0\delta_a\), or it has a complex zero. In the latter factorization \(v\) must be a unit, since \(b_{z_0}\) is not. Write \(v=C_0\delta_a\) and use (1.4):
\[
u=-C_0z_0\delta_a-iC_0\delta_a'.
\]
This is (1.1). It proves the complete necessity.

**Sufficiency, including every complex multiplicity.** If \(u\) has the form (1.1), its entire transform is
\[
U(z)=(c+idz)e^{-iaz}.
\tag{1.5}
\]
For any compact factorization \(u=v*w\), neither factor is zero. Their entire transforms multiply to \(U\): the compact convolution pairing applied to \(e^{-iz(x+y)}=e^{-izx}e^{-izy}\) separates into the two finite-order pairings. If \(d=0\), (1.5) has no zeros, so both factor transforms are zero-free. If \(d\ne0\), it has exactly one zero, of multiplicity one. Both factor transforms cannot have a zero: different zero locations would give two distinct zeros of the product, while the same location would give multiplicity at least two. The multiplicities add because each local Taylor series factors into its first nonzero power times a nonvanishing analytic function. Hence at least one factor is zero-free. The proved zero-free result makes that compact factor a nonzero scalar shifted point mass. This proves sufficiency in every case. Finally, any unit has a zero-free entire transform because its product with its inverse transform is one; the proved zero-free result and the explicit inverses above show that the scalar shifted point masses are all the units. \(\square\)

### When the linear factors give a finite factorization

Theorem 1.1 supplies a factor at each complex zero. A finite list of zeros has a particularly concrete meaning in physical space.

**Theorem 1.2 (finite zeros and point jets).** For nonzero \(u\in\mathcal E'(\mathbb R)\), the following conditions are equivalent: \(Fu\) has finitely many zeros counted with multiplicity; \(u\) is a finite point jet at one real point; and \(u\) is a finite convolution of units and the linear nonunit factors in Theorem 1.1. If its zeros are \(z_1,\ldots,z_m\), repeated according to multiplicity, then
\[
\begin{gathered}
u=C\prod_{\ell=1}^m(D-z_\ell)\delta_a,\\
Fu(z)=C e^{-iaz}\prod_{\ell=1}^m(z-z_\ell),\\
C\ne0,\qquad a\in\mathbb R.
\end{gathered}
\tag{K1}
\]
The zero-free case has \(m=0\) and is a unit.

**Proof.** At an isolated zero, the convergent Taylor series of a nonzero entire function has a first nonzero term of finite degree. The compact factor construction in the preceding proof removes one occurrence of that zero: it gives an actual compact \(u_1\) with \(Fu=(z-z_1)Fu_1\). The Taylor series shows that the multiplicity decreases by one there, and the quotient creates no other zeros. It is nonzero by this identity. Repeating through the finite list leaves a compact factor whose transform is zero-free. Theorem 1.1's proved zero-free classification makes it \(C\delta_a\), giving (K1) with the original Fourier signs.

If the product polynomial is \(\sum_k b_kz^k\), the ordinary point derivatives in (K1) have coefficients \(Cb_k(-i)^k\), because \(D^k\delta_a=(-i)^k\delta_a^{(k)}\). Conversely a nonzero finite jet \(\sum_k c_k\delta_a^{(k)}\) has transform \(e^{-iaz}\sum_k c_k(iz)^k\). At least one coefficient is nonzero because the given distribution is nonzero; thus that polynomial is nonzero. Lemma0.1 supplies its leading coefficient and every root with multiplicity, so it gives a finite convolution as in (K1). Finally each classified nonunit is a first-order point jet, and finite convolutions of point jets and units remain point jets at the sum of their real support points. This proves all implications. \(\square\)

The forcing \(\delta_0-\delta_a\), \(a>0\), has zeros \(2\pi k/a\) for every integer \(k\). Each zero supplies a compact linear factor, but Theorem 1.2 excludes a finite factorization solely into the classified linear factors and units. The distinction concerns the complete zero set, including every multiplicity.

## Homogeneous equations: compact solvability and smooth density

**Theorem 2.1.** Let \(P\) be a homogeneous complex polynomial in \(n\ge1\) variables, and let
\[
\mathcal N_P=\{v\in C^\infty(\mathbb R^n):P(D)v=0\}.
\]
Then its polynomial members are dense in \(\mathcal N_P\) in the topology of uniform convergence of every derivative on every compact set. For \(f\in\mathcal E'(\mathbb R^n)\), there exists \(q\in\mathcal E'(\mathbb R^n)\) with
\[
P(D)q=f
\tag{2.1}
\]
if and only if \(\langle f,p\rangle=0\) for every polynomial \(p\) satisfying \(P(D)p=0\). Both assertions include the zero polynomial \(P\) and the nonzero constant case.

We first prove the analytic mechanism and then turn the moment condition into exactly the required quotient.

### A uniform division estimate on short complex lines

Let \(P\ne0\) be homogeneous of degree \(m\ge1\). Choose a real vector \(a\) with \(P(a)\ne0\). Such a vector exists: a polynomial zero at every real point is zero, by induction on the number of variables, applying the one-variable finite root bound to each coefficient in the remaining variables. For every \(z\in\mathbb C^n\), the one-variable polynomial
\(\tau\mapsto P(z+\tau a)\) has degree \(m\) and the fixed leading coefficient \(P(a)\). Lemma0.1 writes it as
\[
P(z+\tau a)=P(a)\prod_{\ell=1}^m(\tau-\rho_\ell),
\]
retaining roots with all multiplicities. Set \(\delta=1/(4(m+1))\). Remove from \([1,2]\) the intervals of distance less than \(\delta\) from the \(m\) real numbers \(|\rho_\ell|\). Their total length is at most \(2m\delta<1\), so there is \(r\in[1,2]\) outside them. On the entire circle \(|\tau|=r\),
\[
\begin{gathered}
|P(z+\tau a)|\ge c_P,\\
c_P=|P(a)|\delta^m>0.
\end{gathered}
\tag{2.2}
\]
The radius may depend on \(z\); the lower bound does not.

If \(F=P Q\) with \(Q\) a polynomial or an entire function, the one-variable Cauchy mean formula for \(\tau\mapsto Q(z+\tau a)\) gives
\[
|Q(z)|\le c_P^{-1}
     \sup_{|\tau|=r}|F(z+\tau a)|.
\tag{2.3}
\]
This is also valid at zeros of \(P(z)\), because it applies to the already analytic \(Q\), without evaluating a singular pointwise quotient there.

In particular, suppose \(F\) satisfies the whole growth estimate
\[
\begin{gathered}
|F(z)|\le C(1+|z|)^N\\
{}\times e^{A|\operatorname{Im}z|},\qquad A\ge0.
\end{gathered}
\tag{2.4}
\]
If its quotient \(Q\) is entire, (2.3), \(|\tau|\le2\) and \(a\in\mathbb R^n\) give
\[
|Q(z)|\le C'(1+|z|)^N e^{A|\operatorname{Im}z|}.
\tag{2.5}
\]
Only the constant changes: \(|z+\tau a|\le|z|+2|a|\) and
\(|\operatorname{Im}(z+\tau a)|\le|\operatorname{Im}z|+2|a|\).
Thus division keeps polynomial growth on the real subspace and finite exponential growth in the imaginary directions.

### A compact inverse transform from that growth

We prove the exact range statement needed here. Let \(Q\) be any entire function on \(\mathbb C^n\) satisfying (2.5). Its real restriction has polynomial growth, so it is tempered, and \(q=G(Q|_{\mathbb R^n})\) is a well-defined tempered distribution. In fact
\[
\operatorname{supp}q\subset[-A,A]^n.
\tag{2.6}
\]
This coordinate bound establishes compactness. The next lemma gives the sharper Euclidean radius with the same exponent.

For \(0<\epsilon\le1\), put
\[
q_\epsilon(x)=(2\pi)^{-n}
 \int_{\mathbb R^n}Q(\xi)
       e^{-\epsilon|\xi|^2}e^{ix\cdot\xi}d\xi.
\]
The integral is absolute, and identifies its function distribution with the inverse transform of \(Q(\xi)e^{-\epsilon|\xi|^2}\), by absolute Fubini against a Schwartz test. As \(\epsilon\downarrow0\), the latter functions converge to \(Q\) in \(\mathcal S'\): the polynomial bound times any Schwartz test is integrable and dominates their differences. Fourier continuity therefore gives \(q_\epsilon\to q\) distributionally.

Fix a coordinate \(j\), a real vector \(x\), and a real height \(t\). Shift the \(j\)-th integration line from \(\xi_j\) to \(\xi_j+it\). The full identity is
\[
\begin{gathered}
\zeta=\xi+it e_j,\\
q_\epsilon(x)=(2\pi)^{-n}\int_{\mathbb R^n}Q(\zeta)\\
{}\times e^{-\epsilon\zeta\cdot\zeta+ix\cdot\zeta}d\xi.
\end{gathered}
\tag{2.7}
\]
Here is the contour justification, including the unbounded integration. Hold the other real coordinates fixed and use a rectangle with vertical sides at \(\pm R\) and the two horizontal heights \(0,t\). Its integrand is entire in that coordinate. Its closed integral is zero by the complex Green identity from Boundary flux and weak identities, Corollaries2.3–2.4: first round the four corners to apply the smooth-boundary identity, then let their radii tend to zero; continuity makes the four removed arc contributions tend to zero, and the area Cauchy–Riemann term is identically zero. On a vertical side, with height \(s\) between \(0,t\), the modulus is bounded by a polynomial in \(R,|\xi_{\widehat j}|,|t|\) times
\[
\exp(-\epsilon R^2-\epsilon|\xi_{\widehat j}|^2
            +\epsilon t^2+A|t|+|x_jt|).
\]
For fixed \(\epsilon,t,x\), its integral over \(s\) and over the other coordinates tends to zero as \(R\to\infty\); the Gaussian dominates that polynomial. The horizontal tails also tend to zero by the same majorant. Fubini is absolute in all these bounded-height integrals. This proves (2.7) for each fixed finite \(t\), of either sign.

Formula (2.5) in (2.7) gives, with constants independent of \(x,t,\epsilon\),
\[
\begin{gathered}
|q_\epsilon(x)|\le C''\epsilon^{-(N+n)/2}\\
{}\times(1+|t|)^N e^{-x_jt+A|t|+\epsilon t^2}.
\end{gathered}
\tag{2.8}
\]
For the integral bound use
\((1+|\xi|+|t|)^N\le(1+|\xi|)^N(1+|t|)^N\),
then the substitution \(\eta=\sqrt\epsilon\,\xi\); the integral of
\((1+|\eta|)^N e^{-|\eta|^2}\) is finite.

If \(x_j>A\), choose \(t=(x_j-A)/(2\epsilon)>0\). If \(x_j<-A\), choose \(t=-(|x_j|-A)/(2\epsilon)<0\). Both choices make the last exponential in (2.8) equal
\[
\exp\!\left(-\frac{(|x_j|-A)^2}{4\epsilon}\right).
\]
On every compact subset of \(\{|x_j|>A\}\), its distance from the box boundary is positive and \(|x_j|\) is bounded. Thus the polynomial factor in (2.8) is bounded by a fixed power of \(\epsilon^{-1}\), while this exponential tends to zero faster than any such power. Consequently \(q_\epsilon\to0\) uniformly there. Distributional convergence now gives \(q=0\) on that open coordinate region. The complement of \([-A,A]^n\) is the finite union of these coordinate regions; local smooth partitions of unity, or the locality of a zero distribution, give (2.6). In particular \(q\) is a compact distribution. This proves the full inverse-transform mechanism used below.

### The unchanged radial exponent gives a Euclidean ball

The coordinate argument also gives the sharper geometric interpretation of the same constant \(A\).

**Lemma 2.2 (radial support radius).** Under (2.5), the inverse transform satisfies
\[
\operatorname{supp}q\subset\overline B(0,A).
\tag{K2}
\]

**Proof.** Fix a real unit vector \(v\), and choose a real orthogonal coordinate matrix whose first coordinate direction is \(v\). To construct this matrix, extend the nonzero vector \(v\) to a real basis and apply the proved Gram process in the supplied finite algebra, §§10.1 and10.5, beginning with \(v\); its first normalized vector stays \(v\). The resulting matrix \(O\) satisfies \(O^TO=I\), so determinant multiplicativity gives \((\det O)^2=1\). Its real Jacobian therefore has absolute value one; it preserves the Euclidean norm and, after complex linear extension, the bilinear quadratic form \(\zeta\cdot\zeta\). In these coordinates the complete rectangle proof of (2.7) shifts the first line by \(it\), or equivalently shifts the original frequency vector to \(\xi+itv\), for each fixed \(t\ge0\).

The vertical sides still have Gaussian decay in their real coordinate and in all remaining real coordinates, multiplied by a polynomial at fixed finite height. Thus their integrals vanish, the horizontal tails converge, and all integrations are absolute exactly as in that proof. Applying the radial bound gives
\[
\begin{gathered}
|q_\epsilon(x)|\le C_v\epsilon^{-(N+n)/2}(1+t)^N\\
{}\times e^{-t(v\cdot x-A)+\epsilon t^2},\\
0<\epsilon\le1,\qquad t\ge0.
\end{gathered}
\tag{K3}
\]
No uniformity of the constant in \(v\) is needed. On a compact subset of \(v\cdot x>A\), take \(t=(v\cdot x-A)/(2\epsilon)\). The last exponential is \(e^{-(v\cdot x-A)^2/(4\epsilon)}\), with a uniform positive gap. It dominates every remaining inverse power of \(\epsilon\), so \(q_\epsilon\to0\) uniformly there. The already proved distributional convergence gives \(q=0\) on this open half-space.

For any \(x\) with \(|x|>A\), take \(v=x/|x|\). The strict half-space contains a neighborhood of \(x\). Thus that point is outside the support of \(q\), proving (K2), including \(A=0\). The exponent \(A\) was never enlarged. \(\square\)

### The moment condition produces an entire quotient

Let \(f\in\mathcal E'(\mathbb R^n)\) annihilate every polynomial in \(\mathcal N_P\). Its entire Fourier transform
\[
F(z)=\langle f(x),e^{-iz\cdot x}\rangle
=\sum_{k\ge0}F_k(z)
\]
has the homogeneous Taylor pieces
\[
F_k(z)=(-i)^k
       \sum_{|\alpha|=k}
          \frac{\langle f,x^\alpha\rangle}{\alpha!}z^\alpha.
\tag{2.9}
\]
The compact finite-order estimate proves entire convergence and (2.4), by the entire compact-Fourier construction in [*Sharp bounds for compact spectra*](sharp-bounds-for-compact-spectra.md), Theorem 3.1, and the preceding proof: choose a compact cutoff supported in a ball of radius \(A\); derivatives of the exponential give the polynomial factor, and its modulus is at most \(e^{A|\operatorname{Im}z|}\). Choose a larger \(A\) if necessary. The real restriction is exactly \(Ff\).

Let \(\mathcal H_k\) be the finite-dimensional space of homogeneous polynomials of degree \(k\). The bilinear coefficient pairing
\[
B_k(R,p)=p(\partial_z)R(0)
=\sum_{|\alpha|=k}\alpha!r_\alpha p_\alpha
\]
is nondegenerate. For \(p\in\mathcal H_k\), (2.9) says
\(B_k(F_k,p)=(-i)^k\langle f,p\rangle\).
For \(k<m\), \(P(D)\) kills all of \(\mathcal H_k\), so \(F_k=0\).
For \(k\ge m\), put
\[
A_k=P(D):\mathcal H_k\longrightarrow\mathcal H_{k-m}.
\]
The finite derivative identity, with all \(D=-i\partial\) factors retained, is
\[
\begin{gathered}
B_{k-m}(R,A_kp)\\
=(-i)^m B_k(PR,p).
\end{gathered}
\tag{2.10}
\]
It follows by expanding \(P\), \(R\) and \(p\) into their monomials: the factorial remaining after differentiation is exactly the coefficient pairing on the right.

The functional \(p\mapsto B_k(F_k,p)\) vanishes on \(\ker A_k\) by the moment hypothesis. It therefore factors through \(\operatorname{im}A_k\). Extend that finite-dimensional linear functional to \(\mathcal H_{k-m}\) by basis extension, and represent it as \(B_{k-m}(R,\cdot)\), using nondegeneracy. Formula (2.10) then gives
\[
\begin{gathered}
F_k=P Q_{k-m},\\
Q_{k-m}=(-i)^mR\in\mathcal H_{k-m}.
\end{gathered}
\tag{2.11}
\]
The quotient polynomial is unique because the complex polynomial ring has no zero divisors: the product of the leading monomials in any fixed lexicographic order has a nonzero coefficient. The scalar factors in (2.9)–(2.11) are never suppressed.

It remains to prove that the formal quotient actually converges everywhere. Apply (2.3) to the *polynomial* identity (2.11). For \(|z|\le R_0\), put \(B=R_0+2|a|>0\). On the selected circle, \(|z+\tau a|\le B\). For every \(L>B\), the one-variable Cauchy formula applied to \(s\mapsto F(s\omega)\), \(|\omega|\le1\), gives
\[
\begin{gathered}
\sup_{|\zeta|\le B}|F_k(\zeta)|\\
\le M_F(L)(B/L)^k,\\
M_F(L)=\max_{|\zeta|\le L}|F(\zeta)|.
\end{gathered}
\]
Indeed the coefficient of \(s^k\) is \(F_k(\omega)\), its Cauchy bound is \(M_F(L)L^{-k}\), and homogeneity supplies the factor \(B^k\). Thus
\[
\begin{gathered}
\sup_{|z|\le R_0}|Q_{k-m}(z)|\\
\le c_P^{-1}M_F(L)(B/L)^k.
\end{gathered}
\tag{2.12}
\]
The right side is a summable geometric sequence. Therefore
\(Q=\sum_{k\ge m}Q_{k-m}\) converges uniformly on every complex compact ball. It is entire: use the same uniform bounds on a slightly larger ball and apply the one-variable Cauchy derivative estimate successively in the coordinates to each polynomial term; every differentiated series is then locally uniformly convergent. Their sums satisfy the coordinate Cauchy–Riemann equations and the corresponding local multivariable power-series expansion. Multiplication by the fixed polynomial \(P\) passes through the locally uniform series, giving \(F=P Q\) everywhere.

Now (2.3) applies to that entire quotient and (2.4) gives (2.5). The proved inverse-transform statement supplies a compact \(q=GQ\). On real frequencies, \(P(\xi)Q(\xi)=Ff(\xi)\); the full distributional Fourier differentiation rule and injectivity give \(P(D)q=f\). This proves sufficiency in (2.1) for every nonzero homogeneous polynomial of positive degree.

Necessity retains the bilinear transpose sign. If \(f=P(D)q\) with \(q\) compact, then for every polynomial \(p\in\mathcal N_P\),
\[
\begin{gathered}
\langle f,p\rangle=\langle q,P(-D)p\rangle\\
=(-1)^m\langle q,P(D)p\rangle=0.
\end{gathered}
\tag{2.13}
\]
Compact support permits pairing with that global polynomial by a cutoff, and the distributional product and transpose rules give the displayed identity. The homogeneity is what makes \(P(-D)=(-1)^mP(D)\). This proves both directions of the exact compact-solvability criterion.

### Density in the full smooth topology

Let \(M\) be the closure in \(C^\infty(\mathbb R^n)\) of the vector space of polynomial null solutions. Continuity of \(P(D)\) makes \(\mathcal N_P\) closed, so \(M\subset\mathcal N_P\). Suppose \(v\in\mathcal N_P\setminus M\). The complete compact-distribution separation lemma [*Fundamental solutions, continuation and approximation*](fundamental-solutions-continuation-and-approximation.md), Lemma 3.1 produces \(f\in\mathcal E'\) with \(f|_M=0\) and \(\langle f,v\rangle=1\). In particular it annihilates all null polynomials. The just-proved criterion gives a compact \(q\) with \(P(D)q=f\). But (2.13), now applied to the smooth global null solution \(v\), gives
\[
1=\langle f,v\rangle
=(-1)^m\langle q,P(D)v\rangle=0,
\]
a contradiction. Therefore \(M=\mathcal N_P\).

This is sequential approximation in exactly the stated topology. For each integer \(j\ge1\), choose a null polynomial \(p_j\) so that
\[
\max_{|\alpha|\le j}\sup_{|x|\le j}
       |\partial^\alpha(v-p_j)(x)|<1/j.
\]
Closure in the smooth seminorm topology permits this finite-seminorm choice. Every fixed compact set and derivative order is contained in these controls for all sufficiently large \(j\), so \(p_j\to v\) with every derivative on every compact set. No bound on the growth of \(v\), ellipticity, real coefficients or simplicity of the factors of \(P\) was assumed.

If \(P\) is a nonzero constant, its smooth null space and polynomial null space are both zero, the moment condition is empty, and \(q=f/P\) is compact for every \(f\). If \(P=0\), all polynomials and all smooth functions are null. A compact \(f\) annihilating every polynomial is zero by [*Compact forcing, moments and positive error kernels*](compact-forcing-moments-and-positive-error-kernels.md), Lemma 1.2, so the compact equation \(0=f\) has a solution exactly under the stated condition. Polynomials are dense in the full smooth space: otherwise [*Fundamental solutions, continuation and approximation*](fundamental-solutions-continuation-and-approximation.md) separation would produce a nonzero compact distribution annihilating them, contradicting that same complete moment-detection lemma. The identical seminorm selection gives sequential approximation in this case too. All degenerate cases are thus included. \(\square\)

### Compact uniqueness and the actual support hull

Existence in Theorem 2.1 uses homogeneity. Once a compact solution exists, its uniqueness and support geometry hold for every nonzero polynomial.

**Corollary 2.3.** Let \(P\) be any nonzero complex polynomial on \(\mathbb R^n\). A compact solution of \(P(D)q=f\) is unique. For nonzero forcing,
\[
\operatorname{ch}\operatorname{supp}q
=\operatorname{ch}\operatorname{supp}f,
\tag{K4}
\]
where \(\operatorname{ch}\) denotes the closed convex hull. For zero forcing the unique compact solution is zero.

**Proof.** Set \(T=P(D)\delta_0\). Its support is contained in \(\{0\}\), and its entire transform is the nonzero polynomial \(P\), so \(T\ne0\) and its support is exactly \(\{0\}\). The differentiation and compact convolution rules give \(T*q=P(D)q\). The full compact convolution support theorem in [*Convex supports and convolution cancellation*](convex-supports-and-convolution-cancellation.md), Theorem 3.1, applies to arbitrary complex distributions and gives
\[
\begin{gathered}
\operatorname{ch}\operatorname{supp}(P(D)q)\\
=\{0\}+\operatorname{ch}\operatorname{supp}q.
\end{gathered}
\tag{K5}
\]
If \(q\ne0\), its hull is nonempty and the right side is nonempty, so \(P(D)q\ne0\). Apply this to the difference of two compact solutions to get uniqueness, and to a solution of nonzero forcing to get (K4). Nonzero constants are included. \(\square\)

Equality of hulls allows interior support to change. The compact primitive \(i\mathbf1_{(0,a)}\) of \(\delta_0-\delta_a\) has interval support, while the forcing has only two support points. This corollary does not extend the polynomial-moment existence criterion to nonhomogeneous symbols.

### Approximation that preserves finitely many observations

Smooth convergence controls derivative values at finitely many points. Those values can also be kept exactly at every approximating stage, provided they belong to the null solution being approximated.

**Corollary 2.4 (compatible finite constraints).** Keep the homogeneous or degenerate scope of Theorem 2.1. For \(v\in\mathcal N_P\) and any continuous complex-linear map \(J:C^\infty(\mathbb R^n)\to\mathbb C^r\), there are polynomial null solutions \(p_j\) with
\[
p_j\longrightarrow v\text{ in }C^\infty,\qquad Jp_j=Jv
\tag{K6}
\]
for every \(j\). This includes any finite set of derivative values at finitely many points.

**Proof.** Let \(V\) be the polynomial null space. Theorem 2.1 gives \(s_j\in V\) converging to \(v\). Choose a basis \(e_1,\ldots,e_d\) of \(E=J(V)\subset\mathbb C^r\). Finite elimination on the independent columns supplies \(d\) coordinate rows \(I\) such that the matrix \(A=((e_\ell)_I)\) is invertible. For \(b\in E\), its basis coordinates are \(A^{-1}b_I\), a continuous function of \(b\). If \(b_j\in E\) converges to \(b\) in \(\mathbb C^r\), pass to the limit in \(b_j=\sum_\ell(A^{-1}(b_j)_I)_\ell e_\ell\) to get that same identity for \(b\). Hence \(E\) is closed.

Continuity gives \(Js_j\to Jv\), so \(Jv\in E\). Choose \(h_\ell\in V\) with \(Jh_\ell=e_\ell\), and set
\[
\begin{gathered}
b_j=Jv-Js_j,\\
\lambda_j=A^{-1}(b_j)_I,\\
p_j=s_j+\sum_{\ell=1}^d(\lambda_j)_\ell h_\ell.
\end{gathered}
\tag{K7}
\]
Then \(p_j\) is null and \(Jp_j=Jv\). Since \(\lambda_j\to0\), every smooth compact seminorm \(p\) of the correction is bounded by \(\sum_\ell|(\lambda_j)_\ell|p(h_\ell)\to0\). This proves full smooth convergence. If \(d=0\), the map vanishes on the closure \(\mathcal N_P\) and the original \(s_j\) already has the required observations. The nonzero constant and zero-symbol cases follow from the corresponding cases of Theorem 2.1. \(\square\)

The target data are \(Jv\). A differential equation can make arbitrary jet assignments incompatible; the corollary preserves data of an actual solution.

## Exercises

**Exercise 1 (foundation: two opposite point sources).** For \(a>0\), give an explicit nontrivial compact convolution factorization of \(\delta_0-\delta_a\) through \(D\delta_0\). Compute the entire quotient transform, including its removable value at zero.

**Exercise 2 (intermediate: a second difference has a compact second primitive).** For \(a>0\), set \(f=\delta_0-2\delta_a+\delta_{2a}\). Compute a compact \(q\) with \(D^2q=f\), its full transform and its support. Give a convolution factorization and retain every root multiplicity.

**Exercise 3 (intermediate: two complex point-jet factors).** For \(z_1,z_2\in\mathbb C\), \(a\in\mathbb R\), expand
\(u=(D-z_1)(D-z_2)\delta_a\) into ordinary point derivatives. Determine whether its compact convolution factorizations are all trivial, including \(z_1=z_2\).

**Exercise 4 (foundation: an odd-order bilinear obstruction).** On \(\mathbb R^2\), set \(P(D)=D_1+iD_2\). For real points \(a,b\), determine exactly when \(P(D)q=\delta_a-\delta_b\) has a compact distribution solution. Exhibit the detecting null polynomial and the transpose sign.

**Exercise 5 (intermediate: zero mass and dipole moments are insufficient).** On \(\mathbb R^2\), let \(a>0\) and \(f=\delta_{(a,0)}+\delta_{(-a,0)}-2\delta_0\). Show that its constant and linear moments vanish, yet \((D_1^2+D_2^2)q=f\) has no compact solution. Compare with the forcing \((D_1^2+D_2^2)\delta_0\).

**Exercise 6 (advanced: no finite degree cutoff for the moment test).** For every integer \(N\ge0\), construct a compact distribution on \(\mathbb R^2\) annihilating every polynomial of degree at most \(N\), but having no compact solution under \(D_1^2+D_2^2\). Give one explicit higher-degree harmonic polynomial that detects it.

**Exercise 7 (intermediate: smooth null functions can be nonanalytic).** Determine every global smooth solution of \(D_1D_2u=0\) on \(\mathbb R^2\). Construct a sequence of polynomial null solutions converging with every derivative on every compact set, and explain why the construction covers a smooth function with a zero Taylor series at the origin that is not zero nearby.

**Exercise 8 (advanced: all degenerate symbols and the role of homogeneity).** State the compact-solvability criterion for the zero symbol and for a nonzero constant symbol. Then use \(P(D)=D_1^2+D_2^2+1\) to show that both the polynomial density and the compact-solvability criterion can fail if the homogeneity assumption is removed.

**Exercise 9 (intermediate: uniqueness, hulls and a sharp radius).** Prove conditional compact uniqueness and equality of support hulls for \(P(D)=D_1^2+D_2^2+1\), despite the failure of the homogeneous existence criterion. Compare the supports of \(\delta_0-\delta_a\) and its compact \(D\)-primitive. Finally, show that for \(q=\delta_b\) the radial exponent \(A=|b|\) cannot be improved even by allowing a polynomial prefactor.

**Exercise 10 (advanced: exact observations on a nonanalytic null solution).** Put \(v(x_1,x_2)=A(x_1)+B(x_2)\), where \(A,B\) are arbitrary smooth functions. Given finitely many points and finitely many derivative observations, construct polynomial solutions of \(D_1D_2p_j=0\) converging to \(v\) in the full smooth topology while preserving those observations exactly. Include a smooth flat nonanalytic \(A\), and explain why a prescribed nonzero mixed derivative at a point is incompatible.

**Exercise 11 (intermediate: a repeated complex factor is a point jet).** For \(C\ne0\), \(a\in\mathbb R\) and distinct \(r,s\in\mathbb C\), expand \(C(D-r)^2(D-s)\delta_a\) into ordinary point derivatives. Determine its full complex zero set and every multiplicity. Explain why \(\delta_0-\delta_a\), \(a>0\), cannot be a finite convolution of these classified first-order factors and units.

## Solutions

**Solution 1.** The ordinary derivative of \(\boldsymbol1_{(0,a)}\) is \(\delta_0-\delta_a\). Thus
\[
\begin{gathered}
q=i\boldsymbol1_{(0,a)},\\
Dq=\delta_0-\delta_a,\\
\delta_0-\delta_a=(D\delta_0)*q.
\end{gathered}
\]
Both factors are compact and neither is a scalar shifted point mass: one is a derivative point jet and the other is a nonzero interval function. The entire input transform is \(1-e^{-iaz}\), and
\[
Fq(z)=\frac{1-e^{-iaz}}z,
\qquad Fq(0)=ia.
\]
The finite interval integral gives this quotient and its entire extension directly. In particular the zero at the origin has been divided out with the correct Fourier and \(i\) factors.

**Solution 2.** Put \(v=i\boldsymbol1_{(0,a)}\) as above. Then \(q=v*v=-\ell_a\), where
\[
\ell_a(x)=
\begin{cases}
x,&0\le x\le a,\\
2a-x,&a\le x\le2a,\\
0,&x\notin[0,2a].
\end{cases}
\]
Its slope jumps are \(+1,-2,+1\), so
\(\ell_a''=\delta_0-2\delta_a+\delta_{2a}=f\).
Since \(D^2=-\partial^2\), \(D^2q=f\). The support is exactly \([0,2a]\), and
\[
Fq(z)=\left(\frac{1-e^{-iaz}}z\right)^2,
\qquad Fq(0)=-a^2.
\]
Also \(f=(\delta_0-\delta_a)*(\delta_0-\delta_a)\), with two nonunit compact factors. Its transform \((1-e^{-iaz})^2\) has double zeros at \(2\pi k/a\), every \(k\in\mathbb Z\); the numerator's first derivative is nonzero at each such point before squaring. The quotient removes exactly the double zero at zero and is entire.

**Solution 3.** Using \(D\delta_a=-i\delta_a'\), the expansion is
\[
u=-\delta_a''+i(z_1+z_2)\delta_a'
                     +z_1z_2\delta_a.
\]
It factors as \(((D-z_1)\delta_0)*((D-z_2)\delta_a)\). Each entire factor transform has a zero, so neither factor is a unit by Theorem 1.1's complete classification. Their product is
\((z-z_1)(z-z_2)e^{-iaz}\).
When the two points are distinct it has two simple zeros; when they coincide it has one double zero. In both cases the factorization is nontrivial. The second derivative coefficient is \(-1\), so the distribution is nonzero even in the coincident case.

**Solution 4.** The polynomial \(p(x)=x_1+ix_2\) satisfies
\(D_1p=-i\), \(D_2p=1\), and \(P(D)p=0\). Its pairing with the forcing is
\((a_1-b_1)+i(a_2-b_2)\), nonzero exactly when \(a\ne b\) because the coordinates are real. If a compact \(q\) existed, the bilinear transpose would give
\[
\begin{gathered}
\langle P(D)q,p\rangle\\
=\langle q,P(-D)p\rangle\\
=-\langle q,P(D)p\rangle=0.
\end{gathered}
\]
This excludes every distinct pair. If \(a=b\), the forcing is zero and \(q=0\) is compact. This proves the full characterization; no conjugation has entered the polynomial or the transpose.

**Solution 5.** The total mass is \(1+1-2=0\). The two first coordinates cancel and all second coordinates are zero, so both linear moments vanish. But \(p=x_1^2-x_2^2\) is a null polynomial for \(D_1^2+D_2^2=-\Delta\), and
\(\langle f,p\rangle=2a^2\ne0\). Theorem 2.1's necessary compact-moment condition rules out the solution. In contrast \(g=(D_1^2+D_2^2)\delta_0\) has the compact solution \(q=\delta_0\). For every harmonic polynomial \(p\), its pairing is \((D_1^2+D_2^2)p(0)=0\), with positive transpose sign because the degree is two. Thus the entire moment condition, rather than just its first two degrees, distinguishes these forcings.

**Solution 6.** Set \(m=N+1\) and \(f=\partial_1^m\delta_0\). Every polynomial of degree at most \(N\) has zero \(m\)-th derivative, so all the indicated moments vanish. The real polynomial
\[
p(x_1,x_2)=\operatorname{Re}(x_1+ix_2)^m
\]
is harmonic: differentiating the complex polynomial twice in the two coordinates gives opposite terms, including \(m=1\), where both second derivatives are zero. Its coefficient of \(x_1^m\) is one, hence
\(\langle f,p\rangle=(-1)^m m!\ne0\).
This null polynomial detects the obstruction in Theorem 2.1, so no compact Laplace-type solution exists. The argument works for every finite \(N\); a finite truncation of the polynomial-moment condition cannot replace all degrees.

**Solution 7.** The equation is \(\partial_1\partial_2u=0\). Twice applying the real fundamental theorem, including oriented integrals when a coordinate is negative, gives
\[
u(x_1,x_2)=u(x_1,0)+u(0,x_2)-u(0,0).
\]
Thus every solution is \(A(x_1)+B(x_2)\), and every such sum solves the equation. The zero-symbol density case of Theorem 2.1 in one dimension supplies polynomial sequences \(A_j,B_j\) approximating these smooth functions with all derivatives on compact intervals. Choose their \(j\)-th errors below \(1/(2j)\) through order \(j\) on \([-j,j]\), and set \(p_j=A_j(x_1)+B_j(x_2)\). Each mixed derivative is zero, while the pure derivative errors are controlled by the one-dimensional errors. These are polynomial null solutions converging in the full two-dimensional smooth topology.

For example take \(A(t)=e^{-1/t^2}\) for \(t>0\), and zero for \(t\le0\), with \(B=0\). Repeated differentiation on the positive side gives a polynomial in \(1/t\) times that exponential, tending to zero at \(0\) in every order; the negative side is zero. Thus this is smooth with zero Taylor series there but is positive arbitrarily nearby. The approximation uses smooth density, not convergence of its own Taylor series.

**Solution 8.** For \(P=0\), every polynomial is null. The compact moment-detection theorem makes the condition equivalent to \(f=0\), precisely the condition for the compact equation \(0=f\); any compact \(q\), including zero, then solves it. For a nonzero constant \(c\), only the zero polynomial is null, the condition is empty, and \(q=f/c\) is compact for every compact \(f\).

For the nonhomogeneous example \(P(D)=D_1^2+D_2^2+1=-\Delta+1\), a nonzero polynomial cannot be null: its highest-degree part survives the constant term and cannot be cancelled by the Laplacian, which lowers degree by two. Yet the smooth function \(u=e^{-x_1}\) is null and is nonzero at the origin. The zero polynomial space cannot approximate it even pointwise there. Finally the forcing \(f=\delta_0\) annihilates every polynomial null solution, since there are none except zero. A compact solution would have an entire transform \(Q\) satisfying
\[
(z_1^2+z_2^2+1)Q(z)=1.
\]
The real-frequency identity extends to all complex coordinates by the identity theorem. Evaluating at \(z=(i,0)\) gives \(0=1\), a contradiction. Thus both extensions fail when homogeneity is omitted, even though all finite-order transpose operations remain well defined.

**Solution 9.** The symbol is nonzero, so Corollary 2.3 gives uniqueness whenever a compact solution exists and equality of the actual hulls for nonzero forcing. This applies to this nonhomogeneous polynomial without an existence assertion: for example \(f=P(D)\delta_c\) has solution \(\delta_c\), while Solution 8 proves that \(\delta_0\) has no compact solution. These two conclusions are compatible. For the one-dimensional forcing, Solution 1 gives \(q=i\mathbf1_{(0,a)}\); its support is \([0,a]\), whereas the forcing support is \(\{0,a\}\). Both hulls are \([0,a]\).

For a real point \(b\), \(F\delta_b(z)=e^{-ib\cdot z}\), so its modulus is \(e^{b\cdot\operatorname{Im}z}\le e^{|b||\operatorname{Im}z|}\). If \(b\ne0\), evaluate a hypothetical bound with \(A<|b|\) at \(z=itb/|b|\):
\[
\begin{gathered}
e^{t(|b|-A)}\le C(1+t)^N,\\
t>0.
\end{gathered}
\tag{K8}
\]
Taking logarithms and dividing by \(t\) contradicts \(|b|-A>0\), because \(\log(1+t)/t\to0\). Thus \(A=|b|\) is sharp. If \(b=0\), the admissible nonnegative radius is already zero.

**Solution 10.** Every such \(v\) satisfies the equation because its mixed derivative is zero. Let \(J\) collect the given finite derivative observations. They are continuous complex-linear functionals in the smooth compact topology. Theorem 2.1 supplies polynomial null \(s_j\to v\). Form \(E=J(V)\), choose its basis, invertible coordinate minor and null-polynomial lifts \(h_\ell\) as in Corollary 2.4, and use exactly (K7). This is an explicit finite correction after each approximation: it preserves all observations, remains a polynomial null solution, and tends to zero in each smooth seminorm. If the observation image is zero, no correction is needed.

Take \(A(t)=e^{-1/t^2}\) for \(t>0\), zero otherwise, and \(B=0\). Every positive-side derivative is a polynomial in \(1/t\) times \(e^{-1/t^2}\), tending to zero at the origin; this verifies smoothness and flatness in every order, while \(A\) is positive arbitrarily close on the right. The construction therefore includes a nonanalytic solution and does not use its Taylor series as the approximating sequence. Conversely any \(D_1D_2\) null solution has \(\partial_1\partial_2v=0\) at every point, so prescribing that mixed derivative to be nonzero is incompatible with the equation. Corollary 2.4 prescribes the actual data of \(v\).

**Solution 11.** Expand the polynomial before inserting the differential signs:
\[
\begin{gathered}
(z-r)^2(z-s)\\
=z^3-(2r+s)z^2\\
{}+(r^2+2rs)z-r^2s,\\
u=C\bigl[i\delta_a^{(3)}+(2r+s)\delta_a''\\
{}-i(r^2+2rs)\delta_a'-r^2s\delta_a\bigr].
\end{gathered}
\tag{K9}
\]
Here \((-i)^3=i\), \((-i)^2=-1\), and \((-i)^1=-i\); thus every ordinary derivative coefficient has its correct sign. The highest coefficient \(Ci\) is nonzero. The transform is \(C e^{-iaz}(z-r)^2(z-s)\), with exactly a double zero at \(r\) and a simple zero at \(s\), since the exponential never vanishes and \(r\ne s\). Its compact convolution has two copies of \((D-r)\delta_0\), one \((D-s)\delta_0\), and the unit \(C\delta_a\). In contrast \(1-e^{-iaz}\) has a simple zero at every \(2\pi k/a\). There are infinitely many of them, so Theorem 1.2 excludes a finite convolution solely of classified first-order factors and units for that forcing.

## References

- [Convolution as addition of supports](convolution-as-addition-of-supports.md), B0–B3 and Theorem1.1: compact actions, locality and convolution. [Compact forcing, moments and positive error kernels](compact-forcing-moments-and-positive-error-kernels.md), Lemma1.2 and Theorem1.3: complete moment detection and compact primitives. [Fundamental solutions, continuation and approximation](fundamental-solutions-continuation-and-approximation.md), B1–B2 and Lemma3.1: smooth topology, compact duality and separation.
- [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Theorem1.1 and Corollary2.2: Cauchy and Taylor formulas. Boundary flux and weak identities, Corollaries2.3–2.4: complex Green, including corners. [Sharp bounds for compact spectra](sharp-bounds-for-compact-spectra.md), Lemma0.1 and the finite-order construction in Theorem3.1: identity principle and entire compact transforms. [Convex supports and convolution cancellation](convex-supports-and-convolution-cancellation.md), Theorem3.1: exact convex hulls for arbitrary complex compact distributions.
- Supplied [finite algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.5; [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5; [functional foundation](../prerequisites/U011-free-foundations/functional-foundations-U008.md), §5; and the scalar and integration foundations named above. These exact copies retain their stated licences. Lemma0.1 supplies the additional complete polynomial factorization proof.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, reprint of the second edition (1990), Exercises7.3.1 and7.3.5, printed page390, with answers on pages414–415. The compact factor construction, entire quotient argument, exact support radius, finite-observation correction and eleven graded problems above are independently expressed.
